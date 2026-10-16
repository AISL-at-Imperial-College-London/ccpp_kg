"""
Build the knowledge graph for the stripping loop of Pilot Plant 2514 (v2).

Loop (stripping loop line-up, absorber isolated):
E100 draw-off (stage 11) > FT102 > Q105 > H100 > Q106 > E100 sump (stage 12)
> V110 > V112 > C100 > V113a > V113b > J100 > PCV122 > V116 > V117a > Z102 > V117b
> V121 > FT103 > FT104 > SDV125 > H200a | H200b > V403 > V402 > E100 top (stage 1)
Z102 bypass: V116 > V120 > V121 (normally closed).

All plant data lives in loop_data.py. Run from the repo root:
    python stripping_loop/build_stripping_loop.py
Output: stripping_loop/stripping_loop.ttl
"""
import json
import pathlib
import re
import sys

from rdflib import Graph, Literal, Namespace, RDF, RDFS, XSD

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import loop_data as D  # noqa: E402
import sources as S  # noqa: E402
from heat_mass_transfer import COLUMN_MAP, HX_MAP, analyse  # noqa: E402

ROOT = HERE.parent
CCPP = Namespace("http://imperial.ac.uk/ccpp#")
RETURN_STAGE = D.NOZZLES["E100_N_top_inlet"][1]  # single source: the nozzle table

g = Graph()
g.bind("ccpp", CCPP)
g.bind("rdfs", RDFS)


def uri(name):
    return CCPP[re.sub(r"[^A-Za-z0-9_\-]", "_", name)]


def lit(v):
    if isinstance(v, bool):
        return Literal(v, datatype=XSD.boolean)
    if isinstance(v, int):
        return Literal(v, datatype=XSD.integer)
    if isinstance(v, float):
        return Literal(v, datatype=XSD.double)
    return Literal(str(v))  # plain literal (matches "text" in SPARQL)


def add(s, p, o):
    """Add a triple; plain Python values become typed literals, None is skipped."""
    if o is None:
        return
    if isinstance(o, (str, int, float, bool)):
        o = lit(o)
    g.add((s, p, o))


def node(name, cls, label=None):
    s = uri(name)
    g.add((s, RDF.type, CCPP[cls]))
    add(s, RDFS.label, label or name)
    return s


def tagged(tag, cls, label=None):
    s = node(tag, cls, label)
    add(s, CCPP.tag, tag)
    return s


def stage(n):
    return uri(f"E100_stage_{n:02d}")


# ---------------------------------------------------------------------------
# 1. Physical items
# ---------------------------------------------------------------------------
for tag, (cls, label, props) in D.EQUIPMENT.items():
    s = tagged(tag, cls, label)
    for k, v in props.items():
        add(s, CCPP[k], v)

for tag, (cls, vtype, floor, grid, pos, note) in D.VALVES.items():
    s = tagged(tag, cls)
    add(s, CCPP.valveType, vtype)
    add(s, CCPP.floor, floor)
    add(s, CCPP.gridReference, grid)
    add(s, CCPP.normalPosition, pos)
    add(s, CCPP.note, note)
g.add((uri("RV101"), CCPP.protects, uri("J100")))
g.add((uri("RV401"), CCPP.protects, uri("E100")))

for tag, note in D.PIPES.items():
    s = tagged(tag, "PipeSegment", f"Line {tag}")
    add(s, CCPP.note, note)

for n, (cls, h, ptype, psize, mat, rxn, floor) in D.STAGES.items():
    s = node(f"E100_stage_{n:02d}", cls, f"E100 stage {n}")
    add(s, CCPP.stageNumber, n)
    add(s, CCPP.sectionHeight_mm, h)
    add(s, CCPP.packingType, ptype)
    add(s, CCPP.packingSize_mm, psize)
    add(s, CCPP.packingMaterial, mat)
    add(s, CCPP.reactionModel, rxn)
    add(s, CCPP.floor, floor)
    g.add((uri("E100"), CCPP.hasStage, s))

for name, (label, st) in D.NOZZLES.items():
    s = node(name, "Nozzle", label)
    g.add((s, CCPP.onEquipment, uri("E100")))
    g.add((s, CCPP.atStage, stage(st)))
g.add((uri("E100_N_drawoff"), CCPP.drawsFromStage, stage(11)))
g.add((uri("E100_N_reboiler_return"), CCPP.feedsStage, stage(12)))
g.add((uri("E100_N_sump_outlet"), CCPP.drawsFromStage, stage(12)))
g.add((uri("E100_N_top_inlet"), CCPP.feedsStage, stage(RETURN_STAGE)))

for tag, (cls, var, stype, sig, grid, floor, mon, stg, ph) in D.INSTRUMENTS.items():
    s = tagged(tag, cls)
    add(s, CCPP.measuredVariable, var)
    add(s, CCPP.sensorType, stype)
    add(s, CCPP.signalType, sig)
    add(s, CCPP.gridReference, grid)
    add(s, CCPP.floor, floor)
    add(s, CCPP.measuredPhase, ph)
    if mon:
        g.add((s, CCPP.monitors, uri(mon)))
    if stg:
        g.add((s, CCPP.locatedAtStage, stage(stg)))
        add(s, CCPP.note, D.STAGE_MAP_NOTE)

for tag, (targets, label) in D.CONTROLLERS.items():
    s = tagged(tag, "Controller", label)
    for t in ([targets] if isinstance(targets, str) else targets):
        g.add((s, CCPP.controls, uri(t)))

# ---------------------------------------------------------------------------
# 2. The loop: ordered steps, active flow (feedsInto) and physical piping (pipedTo)
# ---------------------------------------------------------------------------
LOOP = node("StrippingLoop", "Loop", "Stripping loop (absorber isolated)")
g.add((LOOP, CCPP.inMode, CCPP.StripperRecirculation))
g.add((LOOP, CCPP.returnsToStage, stage(RETURN_STAGE)))
add(LOOP, CCPP.source, "P&ID checked with the team; REPORT Fig 2.1 and Fig E.1/E.2")

steps = []  # (index, item, type)
for idx, entry in enumerate(D.LOOP):
    group = entry if isinstance(entry[0], tuple) else (entry,)
    for item, typ in group:
        steps.append((idx, item, typ))
        st = node(f"StrippingLoop_step_{idx:02d}_{item}", "LoopStep", f"Stripping loop step {idx}: {item}")
        g.add((LOOP, CCPP.hasStep, st))
        add(st, CCPP.stepIndex, idx)
        add(st, CCPP.stepType, typ)
        g.add((st, CCPP.stepItem, uri(item)))

inline = [(i, t) for i, t, typ in steps if typ == "inline"]
indices = sorted({i for i, _ in inline})
for a, b in zip(indices, indices[1:]):
    for x in [t for i, t in inline if i == a]:
        for y in [t for i, t in inline if i == b]:
            g.add((uri(x), CCPP.feedsInto, uri(y)))
            g.add((uri(x), CCPP.pipedTo, uri(y)))
# close the loop: the column (packing) delivers liquid to the draw-off nozzle
g.add((uri("E100"), CCPP.feedsInto, uri("E100_N_drawoff")))
g.add((uri("E100"), CCPP.pipedTo, uri("E100_N_drawoff")))
for a, b in D.EXTRA_PIPING:
    g.add((uri(a), CCPP.pipedTo, uri(b)))

REB = node("ReboilerCircuit", "Loop", "H100 reboiler circuit (part of the stripping loop)")
for i, item in enumerate(D.REBOILER_SUBLOOP):
    st = node(f"ReboilerCircuit_step_{i:02d}_{item}", "LoopStep", f"Reboiler circuit step {i}: {item}")
    g.add((REB, CCPP.hasStep, st))
    add(st, CCPP.stepIndex, i)
    add(st, CCPP.stepType, "inline")
    g.add((st, CCPP.stepItem, uri(item)))

# Z102 bypass route
b = D.BYPASS
BY = node("Z102_bypass", "BypassRoute", b["label"])
g.add((BY, CCPP.fromItem, uri(b["from_item"])))
for v in b["via"]:
    g.add((BY, CCPP.routeVia, uri(v)))
g.add((BY, CCPP.toItem, uri(b["to_item"])))
for t in b["bypasses"]:
    g.add((BY, CCPP.bypasses, uri(t)))
add(BY, CCPP.normalState, b["state"])
g.add((BY, CCPP.activatedBy, uri(b["procedure"])))
g.add((uri("V120"), CCPP.bypasses, uri("Z102")))

# ---------------------------------------------------------------------------
# 3. Control loops, interlocks, limits, procedures, discrepancies
# ---------------------------------------------------------------------------
for cid, c in D.CONTROL_LOOPS.items():
    s = node(cid, "ControlLoop", c["label"])
    for t in c["sensors"]:
        g.add((s, CCPP.hasSensor, uri(t)))
    for t in c["controllers"]:
        g.add((s, CCPP.hasController, uri(t)))
    for t in c["final"]:
        g.add((s, CCPP.hasFinalElement, uri(t)))
    add(s, CCPP.controlledVariable, c["cv"])
    add(s, CCPP.manipulatedVariable, c["mv"])
    add(s, CCPP.source, c["source"])
for master, slave in D.CASCADES:
    g.add((uri(master), CCPP.cascadeMasterOf, uri(slave)))

for iid, il in D.INTERLOCKS.items():
    s = node(iid, "Interlock", il["label"])
    for t in il["by"]:
        g.add((s, CCPP.initiatedBy, uri(t)))
    for t in il["trips"]:
        g.add((s, CCPP.tripsItem, uri(t)))

for lid, (tgt, var, typ, lo, hi, unit, src, ok, note) in D.LIMITS.items():
    s = node(f"limit_{lid}", "OperatingLimit", lid)
    g.add((s, CCPP.appliesTo, uri(tgt)))
    add(s, CCPP.variable, var)
    add(s, CCPP.limitType, typ)
    add(s, CCPP.lowValue, lo)
    add(s, CCPP.highValue, hi)
    add(s, CCPP.unit, unit)
    add(s, CCPP.source, src)
    add(s, CCPP.valueVerified, ok)
    add(s, CCPP.note, note)

for pid, p in D.PROCEDURES.items():
    s = node(pid, "Procedure", p["label"])
    add(s, CCPP.source, p["source"])
    add(s, CCPP.triggerCondition, p["trigger"])
    for i, (text, item, pos) in enumerate(p["steps"], start=1):
        st = node(f"{pid}_step_{i:02d}", "ProcedureStep", f"{p['label']} step {i}")
        g.add((s, CCPP.hasProcedureStep, st))
        add(st, CCPP.stepOrder, i)
        add(st, CCPP.instruction, text)
        g.add((st, CCPP.operatesOn, uri(item)))
        add(st, CCPP.requiredPosition, pos)

for did, tags, grid, drawn, built in D.DISCREPANCIES:
    s = node(f"discrepancy_{did}", "PIDDiscrepancy", did)
    for t in tags:
        g.add((s, CCPP.concerns, uri(t)))
    add(s, CCPP.gridReference, grid)
    add(s, CCPP.drawingShows, drawn)
    add(s, CCPP.asBuilt, built)
    add(s, CCPP.source, "P_ID_Differences.pdf")

# ---------------------------------------------------------------------------
# 4. HAZOP (elements 7, 8, 11, 13)
# ---------------------------------------------------------------------------
KNOWN = {str(o) for o in g.objects(None, CCPP.tag)}
hz = json.load(open(ROOT / "data" / "hazop" / "hazop_stripping_loop.json"))
titles = {r["element"]: r["element_title"] for r in hz["rows"]}
for el, tags in D.HAZOP_COVERAGE.items():
    s = node(f"HAZOP_element_{el}", "HazopElement", f"HAZOP element {el}: {titles.get(el, '')}")
    add(s, CCPP.elementNumber, el)
    add(s, CCPP.source, hz["source"])
    for t in tags:
        g.add((s, CCPP.covers, uri(t)))
for r in hz["rows"]:
    s = node(f"HAZOP_{r['element']}_{r['item']:02d}", "HazopDeviation", f"HAZOP {r['element']}.{r['item']}")
    g.add((s, CCPP.inElement, uri(f"HAZOP_element_{r['element']}")))
    add(s, CCPP.itemNumber, r["item"])
    for key, prop in [("parameter", "parameter"), ("guideword", "guideword"), ("cause", "cause"),
                      ("consequence", "consequence"), ("safeguard", "safeguard"),
                      ("action", "recommendedAction"), ("action_taken", "actionTaken")]:
        if r[key]:
            add(s, CCPP[prop], r[key])
    text = " ".join(r[k] for k in ("cause", "consequence", "safeguard", "action"))
    for old, new in D.HAZOP_RENAMES.items():
        text = text.replace(old, new)
    for t in set(re.findall(r"\b[A-Z]{1,4}\s?\d{3}[a-z]?\b", text)):
        t = t.replace(" ", "")
        if t in KNOWN:
            g.add((s, CCPP.concerns, uri(t)))
        elif t in D.HAZOP_ALARM_HOST:
            g.add((s, CCPP.concerns, uri(D.HAZOP_ALARM_HOST[t])))

# ---------------------------------------------------------------------------
# 5. Aspen simulation cases, stream states, stage results, heat and mass transfer
# ---------------------------------------------------------------------------
CASES = {
    "aspen_v3": dict(label="ABB_pilot_plant_final_3", recommended=True,
                     note="Converged full-plant model (figure of eight). Use for numbers.",
                     blocks={"E100": "E100", "C100": "C100", "H100REAC": "H100", "H100HEAT": "H100",
                             "H200A": "H200a", "H200B": "H200b"}),
    "aspen_v6_1": dict(label="ABB_pilot_plant_final_6_1_SA_validation", recommended=False,
                       note="Rescaled to pilot conditions with a sensitivity study for validation. Saved results did "
                            "not converge: E100 RateSep failed, H100 invalid input, C100 temperature crossover, "
                            "recycle opened at S3BACKUP.",
                       blocks={"E100": "E100", "C100": "C100", "H100": "H100", "H200A": "H200a", "H200B": "H200b"}),
}
for key, meta in CASES.items():
    data = json.load(open(ROOT / "data" / "aspen" / f"{key}.json"))
    case = node(f"case_{key}", "SimulationCase", meta["label"])
    add(case, CCPP.aspenFile, data["source_file"])
    add(case, CCPP.savedOn, data["saved"])
    add(case, CCPP.aspenVersion, data["aspen_version"])
    add(case, CCPP.converged, all(bs["status"] != "ERROR" for bs in data["block_status"].values()))
    add(case, CCPP.recommendedForUse, meta["recommended"])
    add(case, CCPP.note, meta["note"])
    g.add((case, CCPP.representsMode, CCPP.FigureOfEight))

    blk = {}
    for bid, st in data["block_status"].items():
        bnode = node(f"{key}_block_{bid}", "AspenBlock", f"{bid} ({meta['label']})")
        blk[bid] = bnode
        add(bnode, CCPP.blockId, bid)
        add(bnode, CCPP.aspenModel, st["aspen_model"])
        add(bnode, CCPP.status, st["status"])
        add(bnode, CCPP.statusMessage, st["message"])
        g.add((bnode, CCPP.inCase, case))
        if bid in meta["blocks"]:
            g.add((bnode, CCPP.represents, uri(meta["blocks"][bid])))

    for sid, s in data["streams"].items():
        n = node(f"{key}_stream_{sid}", "StreamState", f"{sid} ({meta['label']})")
        add(n, CCPP.streamId, sid)
        g.add((n, CCPP.inCase, case))
        if s["from_block"] in blk:
            g.add((n, CCPP.fromBlock, blk[s["from_block"]]))
        if s["to_block"] in blk:
            g.add((n, CCPP.toBlock, blk[s["to_block"]]))
        add(n, CCPP.phase, s["phase"])
        add(n, CCPP.temperature_C, float(s["T_C"]))
        add(n, CCPP.pressure_bar, float(s["P_bar"]))
        add(n, CCPP.massFlow_kg_h, float(s["mass_flow_kg_h"]))
        add(n, CCPP.moleFlow_kmol_h, float(s["mole_flow_kmol_h"]))
        add(n, CCPP.vapourFraction, float(s["vapour_fraction"]))
        add(n, CCPP.enthalpyFlow_W, float(s["enthalpy_flow_W"]))
        add(n, CCPP.apparentCO2_kg_h, float(s["apparent_CO2_kg_h"]))
        if s["apparent_CO2_loading_mol_mol"] is not None:
            add(n, CCPP.co2Loading_mol_mol, float(s["apparent_CO2_loading_mol_mol"]))
        if s["apparent_MEA_wt_frac"] is not None:
            add(n, CCPP.meaMassFraction, float(s["apparent_MEA_wt_frac"]))
        add(n, CCPP.waterFlow_kg_h, float(s["component_mass_flow_kg_h"]["H2O"]))

    res = analyse(key, data)
    for row in data.get("E100_profile") or []:
        n = node(f"{key}_E100_stage_{row['stage']:02d}", "StageResult", f"E100 stage {row['stage']} ({meta['label']})")
        g.add((n, CCPP.inCase, case))
        g.add((n, CCPP.ofStage, stage(row["stage"])))
        add(n, CCPP.temperature_C, float(row["T_C"]))
        add(n, CCPP.pressure_bar, float(row["P_bar"]))
        add(n, CCPP.liquidFlow_kmol_h, float(row["liquid_flow_kmol_h"]))
        add(n, CCPP.vapourFlow_kmol_h, float(row["vapour_flow_kmol_h"]))
        add(n, CCPP.vapourCO2MoleFraction, float(row["y_CO2"]))
        add(n, CCPP.co2Loading_mol_mol, float(row["liquid_CO2_loading_mol_mol"]))
        add(n, CCPP.co2Desorbed_kg_h, float(res["stage_desorption"][row["stage"]]))

    for eq, r in res["heat_exchangers"].items():
        n = node(f"{key}_{eq}_performance", "HeatExchangerPerformance", f"{eq} performance ({meta['label']})")
        g.add((n, CCPP.ofEquipment, uri(eq)))
        g.add((n, CCPP.inCase, case))
        add(n, CCPP.derivedBy, "heat_mass_transfer.py")
        for k, v in r.items():
            if k == "equipment" or v is None:
                continue
            add(n, CCPP[k], v if isinstance(v, bool) else float(v))

    n = node(f"{key}_E100_performance", "ColumnPerformance", f"E100 performance ({meta['label']})")
    g.add((n, CCPP.ofEquipment, uri("E100")))
    g.add((n, CCPP.inCase, case))
    add(n, CCPP.derivedBy, "heat_mass_transfer.py")
    for k, v in res["column"].items():
        if v is not None:
            add(n, CCPP[k], float(v))

# ---------------------------------------------------------------------------
# 6. Grounding: source documents and a citation for every fact (W3C PROV-O)
# ---------------------------------------------------------------------------
# 6a. One node per source document
for key, (short, title, fname) in S.SOURCE_DOCS.items():
    doc_node = node(f"SRC_{key}", "SourceDocument", title)
    add(doc_node, CCPP.shortName, short)
    add(doc_node, CCPP.fileName, fname)

_cite_count = {}


def cite(name, citations):
    """Attach citations [(doc key, location), ...] to the node called `name`."""
    subj = uri(name)
    for doc, loc in citations:
        i = _cite_count.get(name, 0) + 1
        _cite_count[name] = i
        c = node(f"{name}__cit{i:02d}", "Citation", f"Citation {i} for {name}")
        g.add((subj, CCPP.citedIn, c))
        g.add((c, CCPP.document, uri(f"SRC_{doc}")))
        add(c, CCPP.location, loc)
        add(c, CCPP.citationText, f"{S.SOURCE_DOCS[doc][0]} {loc}")


GRIDS = {**{t: v[3] for t, v in D.VALVES.items()}, **{t: v[4] for t, v in D.INSTRUMENTS.items()},
         **{t: p.get("gridReference") for t, (_c, _l, p) in D.EQUIPMENT.items()}}


def cite_text(name, text, item=None):
    """Cite from free text like 'SUMMARY p.190; REPORT D.4'. A bare 'P&ID' uses the item's grid."""
    cits = []
    for doc, loc in S.parse(text):
        if doc == "PID" and loc == "whole document" and item and GRIDS.get(item):
            loc = f"grid {GRIDS[item]}"
        cits.append((doc, loc))
    cite(name, cits)


# 6b. Plant items
for tag in D.EQUIPMENT:
    cite(tag, S.citations_for(tag, "equipment", D))
for tag in D.VALVES:
    cite(tag, S.citations_for(tag, "valve", D))
for tag in D.PIPES:
    cite(tag, S.citations_for(tag, "pipe", D))
for tag in D.INSTRUMENTS:
    cite(tag, S.citations_for(tag, "instrument", D))
for tag in D.CONTROLLERS:
    cite(tag, S.citations_for(tag, "controller", D))
for name in D.NOZZLES:
    cite(name, S.NOZZLE_CITATIONS[name])
for n in D.STAGES:
    cite(f"E100_stage_{n:02d}", [("ASPEN_V3", f"block E100, stage {n} (internals and reaction model)")])

# 6c. Loops, bypass, control, safety, procedures, discrepancies
cite("StrippingLoop", [("PID", "stripping loop route (team marked-up copy)"),
                       ("REPORT", "Fig 2.1 and " + S.LINEUP), ("TEAM", "loop traced item by item and confirmed")])
cite("ReboilerCircuit", [("PID", "H100 circuit, grids J7 to M6"),
                         ("TEAM", "draw-off below TT103 > FT102 > Q105 > H100 > Q106"),
                         ("ASPEN_V3", "streams S14 and S24")])
cite("Z102_bypass", [("PID", "grids L11 to M11 (V116, V120, V121)"), ("REPORT", "section E.3.6 and Fig F.21")])
for cid, cl in D.CONTROL_LOOPS.items():
    cite_text(cid, cl["source"])
for iid in D.INTERLOCKS:
    cite(iid, S.INTERLOCK_CITATIONS[iid])
for lid, (tgt, var, typ, lo, hi, unit, src, ok, note) in D.LIMITS.items():
    cite_text(f"limit_{lid}", src, item=tgt)
for pid, p in D.PROCEDURES.items():
    cite_text(pid, p["source"])
for did, tags, grid, drawn, built in D.DISCREPANCIES:
    cite(f"discrepancy_{did}", [("DIFF", f"row {', '.join(tags)} ({grid})")])

# 6d. HAZOP
for el in D.HAZOP_COVERAGE:
    cite(f"HAZOP_element_{el}", [("HAZOP", f"element {el}")])
for r in hz["rows"]:
    cite(f"HAZOP_{r['element']}_{r['item']:02d}", [("HAZOP", f"element {r['element']}, item {r['item']}")])

# 6e. Aspen results and the heat and mass transfer calculations
ASPEN_DOC = {"aspen_v3": "ASPEN_V3", "aspen_v6_1": "ASPEN_V61"}
for key in CASES:
    data = json.load(open(ROOT / "data" / "aspen" / f"{key}.json"))
    doc = ASPEN_DOC[key]
    cite(f"case_{key}", [(doc, "whole model (saved results)")])
    for bid in data["block_status"]:
        cite(f"{key}_block_{bid}", [(doc, f"block {bid} (run status)")])
    for sid in data["streams"]:
        cite(f"{key}_stream_{sid}", [(doc, f"stream {sid} results")])
    for row in data.get("E100_profile") or []:
        cite(f"{key}_E100_stage_{row['stage']:02d}", [(doc, f"block E100 profile, stage {row['stage']}")])
    for eq, sides in HX_MAP[key].items():
        streams = sorted({x for side in ("hot", "cold") for pair in (sides[side] or []) for x in pair})
        cite(f"{key}_{eq}_performance", [(doc, "streams " + ", ".join(streams) + "; calculated by heat_mass_transfer.py")])
    cm = COLUMN_MAP[key]
    cols = sorted(set(cm["feeds"] + cm["products"] + [cm["co2_product"]]))
    cite(f"{key}_E100_performance", [(doc, "streams " + ", ".join(cols) + "; calculated by heat_mass_transfer.py")])

# ---------------------------------------------------------------------------
out = HERE / "stripping_loop.ttl"
g.serialize(destination=str(out), format="turtle")
print(f"Wrote {len(g)} triples to {out}")
