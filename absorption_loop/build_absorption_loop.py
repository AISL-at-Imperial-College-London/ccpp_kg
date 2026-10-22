"""
Build the knowledge graph for the absorption loop of Pilot Plant 2514.

Loop: E101 sump > J101a | J101b > FT108 > FT109 > V124 > V119b > V119a > V211 > N200
      > V213 > C200 > NRV400 > E101 top.
Uses the shared ontology (ontology/ccpp_ontology.ttl) and the shared source list
(stripping_loop/sources.py), so it can be joined to the stripping loop KG.

Run from the repo root:   python absorption_loop/build_absorption_loop.py
Output: absorption_loop/absorption_loop.ttl
"""
import json
import pathlib
import re
import sys

from rdflib import Graph, Literal, Namespace, RDF, RDFS, XSD

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(ROOT / "stripping_loop"))
import absorption_data as D  # noqa: E402
import sources as S  # noqa: E402  (shared source documents)

CCPP = Namespace("http://imperial.ac.uk/ccpp#")
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
    return Literal(str(v))


def add(s, p, o):
    if o is None:
        return
    g.add((s, p, lit(o) if isinstance(o, (str, int, float, bool)) else o))


def node(name, cls, label=None):
    s = uri(name)
    g.add((s, RDF.type, CCPP[cls]))
    add(s, RDFS.label, label or name)
    return s


_n = {}


def cite(name, citations):
    """Citation nodes get an 'abscit' name so they never clash with the stripping loop's when the KGs are joined."""
    for doc, loc in citations:
        i = _n.get(name, 0) + 1
        _n[name] = i
        c = node(f"{name}__abscit{i:02d}", "Citation", f"Citation {i} for {name} (absorption loop)")
        g.add((uri(name), CCPP.citedIn, c))
        g.add((c, CCPP.document, uri(f"SRC_{doc}")))
        add(c, CCPP.location, loc)
        add(c, CCPP.citationText, f"{S.SOURCE_DOCS[doc][0]} {loc}")


# 1. Source documents (identical to the stripping loop's, so they merge cleanly)
for key, (short, title, fname) in S.SOURCE_DOCS.items():
    d = node(f"SRC_{key}", "SourceDocument", title)
    add(d, CCPP.shortName, short)
    add(d, CCPP.fileName, fname)

# 2. Equipment and valves
for tag, it in D.ITEMS.items():
    s = node(tag, it["cls"], it.get("label") or tag)
    add(s, CCPP.tag, tag)
    add(s, CCPP.floor, it.get("floor"))
    add(s, CCPP.gridReference, it.get("grid"))
    add(s, CCPP.valveType, it.get("valve"))
    add(s, CCPP.normalPosition, it.get("pos"))
    add(s, CCPP.note, it.get("note"))
    if "present" in it:
        add(s, CCPP.presentOnPlant, it["present"])
    cite(tag, it["cite"])

# 3. Instruments, controllers and nozzles
for tag, (cls, var, stype, sig, grid, floor, mon, cits) in D.INSTRUMENTS.items():
    s = node(tag, cls)
    add(s, CCPP.tag, tag)
    add(s, CCPP.measuredVariable, var)
    add(s, CCPP.sensorType, stype)
    add(s, CCPP.signalType, sig)
    add(s, CCPP.gridReference, grid)
    add(s, CCPP.floor, floor)
    if mon:
        g.add((s, CCPP.monitors, uri(mon)))
    cite(tag, cits)
for tag, (targets, label, cits) in D.CONTROLLERS.items():
    s = node(tag, "Controller", label)
    add(s, CCPP.tag, tag)
    for t in targets:
        g.add((s, CCPP.controls, uri(t)))
    cite(tag, cits)
for name, (label, cits) in D.NOZZLES.items():
    s = node(name, "Nozzle", label)
    g.add((s, CCPP.onEquipment, uri("E101")))
    cite(name, cits)

# 4. The loop: ordered steps, active flow (feedsInto) and physical piping (pipedTo)
LOOP = node("AbsorptionLoop", "Loop", "Absorption loop (absorber recirculation)")
g.add((LOOP, CCPP.inMode, CCPP.AbsorberRecirculation))
add(LOOP, CCPP.note, "J101a and J101b are parallel trains; only one runs at a time (see the two route scenarios).")
cite("AbsorptionLoop", [("PID", "absorption loop route (team trace)"), ("REPORT", "section D.4 and Appendix D (flow direction)"),
                        ("DERIVED", "direction from TT209/TT210 descriptions and J101 duty")])
steps = []
for idx, entry in enumerate(D.LOOP):
    group = entry if isinstance(entry[0], tuple) else (entry,)
    for item, typ in group:
        steps.append((idx, item, typ))
        st = node(f"AbsorptionLoop_step_{idx:02d}_{item}", "LoopStep", f"Absorption loop step {idx}: {item}")
        g.add((LOOP, CCPP.hasStep, st))
        add(st, CCPP.stepIndex, idx)
        add(st, CCPP.stepType, typ)
        g.add((st, CCPP.stepItem, uri(item)))
inline = [(i, t) for i, t, typ in steps if typ == "inline"]
idxs = sorted({i for i, _ in inline})
for a, b in zip(idxs, idxs[1:]):
    for x in [t for i, t in inline if i == a]:
        for y in [t for i, t in inline if i == b]:
            if (x in D.TRAIN_A and y in D.TRAIN_B) or (x in D.TRAIN_B and y in D.TRAIN_A):
                continue  # keep the two pump trains separate
            g.add((uri(x), CCPP.feedsInto, uri(y)))
            g.add((uri(x), CCPP.pipedTo, uri(y)))
g.add((uri("E101"), CCPP.feedsInto, uri("E101_N_sump_outlet")))
g.add((uri("E101"), CCPP.pipedTo, uri("E101_N_sump_outlet")))
for a, b in D.EXTRA_PIPING:
    g.add((uri(a), CCPP.pipedTo, uri(b)))

# 5. Route scenarios (which pump train runs) with valve settings
for rid, r in D.ROUTES.items():
    R = node(rid, "RouteScenario", r["label"])
    g.add((R, CCPP.variantOf, LOOP))
    g.add((R, CCPP.inMode, CCPP.AbsorberRecirculation))
    other = D.TRAIN_B if r["train"] == "a" else D.TRAIN_A
    for i, item, typ in steps:
        if item in other:
            continue
        st = node(f"{rid}_step_{i:02d}_{item}", "LoopStep", f"{r['label']} step {i}: {item}")
        g.add((R, CCPP.hasStep, st))
        add(st, CCPP.stepIndex, i)
        add(st, CCPP.stepType, typ)
        g.add((st, CCPP.stepItem, uri(item)))
    for v, pos in r["settings"].items():
        vs = node(f"{rid}_setting_{v}", "ValveSetting", f"{v} in {r['label']}")
        g.add((R, CCPP.hasValveSetting, vs))
        g.add((vs, CCPP.valve, uri(v)))
        add(vs, CCPP.requiredPosition, pos)
    cite(rid, r["cite"])

# 6. Bypass routes (N200 filter, flow meter test spool)
for bid, b in D.BYPASSES.items():
    B = node(bid, "BypassRoute", b["label"])
    g.add((B, CCPP.fromItem, uri(b["from_item"])))
    for v in b["via"]:
        g.add((B, CCPP.routeVia, uri(v)))
    g.add((B, CCPP.toItem, uri(b["to_item"])))
    for t in b["bypasses"]:
        g.add((B, CCPP.bypasses, uri(t)))
    add(B, CCPP.normalState, b["state"])
    if b["procedure"]:
        g.add((B, CCPP.activatedBy, uri(b["procedure"])))
    cite(bid, b["cite"])
g.add((uri("V212"), CCPP.bypasses, uri("N200")))

# 7. Control loops, limits, procedures, discrepancies, open items
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
    cite(cid, c["cite"])
for m, sl in D.CASCADES:
    g.add((uri(m), CCPP.cascadeMasterOf, uri(sl)))
for lid, (tgt, var, typ, lo, hi, unit, cits) in D.LIMITS.items():
    s = node(f"limit_{lid}", "OperatingLimit", lid)
    g.add((s, CCPP.appliesTo, uri(tgt)))
    add(s, CCPP.variable, var)
    add(s, CCPP.limitType, typ)
    add(s, CCPP.lowValue, lo)
    add(s, CCPP.highValue, hi)
    add(s, CCPP.unit, unit)
    add(s, CCPP.source, "; ".join(f"{d} {l}" for d, l in cits))
    add(s, CCPP.valueVerified, False)
    cite(f"limit_{lid}", cits)
for pid, p in D.PROCEDURES.items():
    s = node(pid, "Procedure", p["label"])
    add(s, CCPP.triggerCondition, p["trigger"])
    for i, (text, item, pos) in enumerate(p["steps"], start=1):
        st = node(f"{pid}_step_{i:02d}", "ProcedureStep", f"{p['label']} step {i}")
        g.add((s, CCPP.hasProcedureStep, st))
        add(st, CCPP.stepOrder, i)
        add(st, CCPP.instruction, text)
        g.add((st, CCPP.operatesOn, uri(item)))
        add(st, CCPP.requiredPosition, pos)
    cite(pid, p["cite"])
for did, tags, grid, drawn, built in D.DISCREPANCIES:
    s = node(f"discrepancy_{did}", "PIDDiscrepancy", did)
    for t in tags:
        g.add((s, CCPP.concerns, uri(t)))
    add(s, CCPP.gridReference, grid)
    add(s, CCPP.drawingShows, drawn)
    add(s, CCPP.asBuilt, built)
    cite(f"discrepancy_{did}", [("DIFF", f"row {', '.join(tags)} ({grid})")])
for oid, (desc, about, resolved_by) in D.OPEN_ITEMS.items():
    o = node(oid, "OpenItem", f"{oid}: {desc}")
    add(o, CCPP.description, desc)
    add(o, CCPP.resolvedBy, resolved_by)
    add(o, CCPP.itemStatus, "open")
    add(o, CCPP.foundBy, "absorption loop build, Oct 2026")
    for t in about:
        g.add((o, CCPP.about, uri(t)))
    cite(oid, [("TEAM", "absorption loop build, Oct 2026")])

# 8. HAZOP (elements 7 and 8 touch this loop; element 10 is open item AOI11)
hz = json.load(open(ROOT / "data" / "hazop" / "hazop_stripping_loop.json"))
titles = {r["element"]: r["element_title"] for r in hz["rows"]}
known = set(D.ITEMS) | set(D.INSTRUMENTS)
for el, tags in D.HAZOP_COVERAGE.items():
    e = node(f"HAZOP_element_{el}", "HazopElement", f"HAZOP element {el}: {titles.get(el, '')}")
    add(e, CCPP.elementNumber, el)
    add(e, CCPP.source, hz["source"])
    for t in tags:
        g.add((e, CCPP.covers, uri(t)))
for r in hz["rows"]:
    if r["element"] not in D.HAZOP_COVERAGE:
        continue
    s = node(f"HAZOP_{r['element']}_{r['item']:02d}", "HazopDeviation", f"HAZOP {r['element']}.{r['item']}")
    g.add((s, CCPP.inElement, uri(f"HAZOP_element_{r['element']}")))
    add(s, CCPP.itemNumber, r["item"])
    for key, prop in [("parameter", "parameter"), ("guideword", "guideword"), ("cause", "cause"),
                      ("consequence", "consequence"), ("safeguard", "safeguard"),
                      ("action", "recommendedAction"), ("action_taken", "actionTaken")]:
        if r[key]:
            add(s, CCPP[prop], r[key])
    text = " ".join(r[k] for k in ("cause", "consequence", "safeguard", "action"))
    for t in set(re.findall(r"\b[A-Z]{1,4}\s?\d{3}[a-z]?\b", text)):
        if t.replace(" ", "") in known:
            g.add((s, CCPP.concerns, uri(t.replace(" ", ""))))
    cite(f"HAZOP_{r['element']}_{r['item']:02d}", [("HAZOP", f"element {r['element']}, item {r['item']}")])

# 9. Heat and mass transfer from Aspen: C200 duty and E101 CO2 absorption
CASES = {"aspen_v3": ("ASPEN_V3", "ABB_pilot_plant_final_3", True),
         "aspen_v6_1": ("ASPEN_V61", "ABB_pilot_plant_final_6_1_SA_validation", False)}
for key, (doc, label, recommended) in CASES.items():
    data = json.load(open(ROOT / "data" / "aspen" / f"{key}.json"))
    st = data["streams"]
    case = node(f"case_{key}", "SimulationCase", label)
    add(case, CCPP.aspenFile, data["source_file"])
    add(case, CCPP.savedOn, data["saved"])
    add(case, CCPP.aspenVersion, data["aspen_version"])
    add(case, CCPP.converged, all(b["status"] != "ERROR" for b in data["block_status"].values()))
    add(case, CCPP.recommendedForUse, recommended)
    g.add((case, CCPP.representsMode, CCPP.FigureOfEight))
    if all(k in st for k in ("S2", "2")):
        n = node(f"{key}_C200_performance", "HeatExchangerPerformance", f"C200 performance ({label})")
        g.add((n, CCPP.ofEquipment, uri("C200")))
        g.add((n, CCPP.inCase, case))
        add(n, CCPP.duty_kW, (st["S2"]["enthalpy_flow_W"] - st["2"]["enthalpy_flow_W"]) / 1000)
        add(n, CCPP.hotInlet_C, float(st["S2"]["T_C"]))
        add(n, CCPP.hotOutlet_C, float(st["2"]["T_C"]))
        add(n, CCPP.derivedBy, "build_absorption_loop.py")
        add(n, CCPP.note, "Lean MEA side only; Aspen models C200 as a heater block, so the cooling water side is not simulated.")
        cite(f"{key}_C200_performance", [(doc, "streams S2 and 2; calculated by build_absorption_loop.py")])
    if all(k in st for k in ("1", "2", "4", "S8")):
        co2_in_gas, co2_out_gas = st["1"]["apparent_CO2_kg_h"], st["4"]["apparent_CO2_kg_h"]
        total_in = co2_in_gas + st["2"]["apparent_CO2_kg_h"]
        total_out = co2_out_gas + st["S8"]["apparent_CO2_kg_h"]
        n = node(f"{key}_E101_performance", "ColumnPerformance", f"E101 performance ({label})")
        g.add((n, CCPP.ofEquipment, uri("E101")))
        g.add((n, CCPP.inCase, case))
        add(n, CCPP.co2Absorbed_kg_h, float(co2_in_gas - co2_out_gas))
        if co2_in_gas:
            add(n, CCPP.captureEfficiency_pct, float(100 * (co2_in_gas - co2_out_gas) / co2_in_gas))
        add(n, CCPP.leanLoading_mol_mol, st["2"]["apparent_CO2_loading_mol_mol"])
        add(n, CCPP.richLoading_mol_mol, st["S8"]["apparent_CO2_loading_mol_mol"])
        add(n, CCPP.co2BalanceError_pct, float(100 * abs(total_in - total_out) / total_in))
        add(n, CCPP.liquidToGasRatio, float(st["2"]["mass_flow_kg_h"] / st["1"]["mass_flow_kg_h"]))
        add(n, CCPP.derivedBy, "build_absorption_loop.py")
        cite(f"{key}_E101_performance", [(doc, "streams 1, 2, 4 and S8; calculated by build_absorption_loop.py")])

out = HERE / "absorption_loop.ttl"
g.serialize(destination=str(out), format="turtle")
print(f"Wrote {len(g)} triples to {out}")
