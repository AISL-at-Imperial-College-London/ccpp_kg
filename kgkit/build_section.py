"""
Shared builder for every plant section KG (Pilot Plant 2514).

A section is one data file (facts with their citations next to them). This
script turns it into a Turtle file using the shared ontology and source list.

Usage (from the repo root):
    python kgkit/build_section.py rich_link/rich_link_data.py rich_link/rich_link.ttl

Recognised names in a data file (all optional except SECTION):
  SECTION        dict(prefix, loop_id, loop_label, mode, loop_note, loop_cite, flow, settings, nozzle_on)
                 flow = "feedsInto" (a loop with its own active path) or "nextStep" (a route that
                 crosses other sections; ordered steps only, so it cannot clash with their flow links)
  ITEMS, INSTRUMENTS, PHASES, CONTROLLERS, NOZZLES, LOOP, TRAIN_A, TRAIN_B, EXTRA_PIPING,
  BYPASSES, CONTROL_LOOPS, CASCADES, LIMITS, PROCEDURES, DISCREPANCIES, HAZOP_COVERAGE,
  INTERLOCKS, OPEN_ITEMS
"""
import importlib.util
import pathlib
import re
import sys

from rdflib import Graph, Literal, Namespace, RDF, RDFS, XSD

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "stripping_loop"))
import sources as S  # noqa: E402  (shared source documents)

data_path, out_path = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
spec = importlib.util.spec_from_file_location("section_data", data_path)
D = importlib.util.module_from_spec(spec)
spec.loader.exec_module(D)
SEC = D.SECTION
get = lambda name, default: getattr(D, name, default)  # noqa: E731

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
    if o is not None:
        g.add((s, p, lit(o) if isinstance(o, (str, int, float, bool)) else o))


def node(name, cls, label=None):
    s = uri(name)
    g.add((s, RDF.type, CCPP[cls]))
    add(s, RDFS.label, label or name)
    return s


_n = {}


def cite(name, citations):
    """Citation nodes carry the section prefix so sections never clash when joined."""
    for doc, loc in citations:
        i = _n.get(name, 0) + 1
        _n[name] = i
        c = node(f"{name}__{SEC['prefix']}cit{i:02d}", "Citation", f"Citation {i} for {name} ({SEC['prefix']})")
        g.add((uri(name), CCPP.citedIn, c))
        g.add((c, CCPP.document, uri(f"SRC_{doc}")))
        add(c, CCPP.location, loc)
        add(c, CCPP.citationText, f"{S.SOURCE_DOCS[doc][0]} {loc}")


for key, (short, title, fname) in S.SOURCE_DOCS.items():
    d = node(f"SRC_{key}", "SourceDocument", title)
    add(d, CCPP.shortName, short)
    add(d, CCPP.fileName, fname)

# Items, instruments, controllers, nozzles
for tag, it in get("ITEMS", {}).items():
    s = node(tag, it["cls"], it.get("label") or tag)
    add(s, CCPP.tag, tag)
    for key, prop in [("floor", "floor"), ("grid", "gridReference"), ("valve", "valveType"), ("pos", "normalPosition"), ("note", "note")]:
        add(s, CCPP[prop], it.get(key))
    if "present" in it:
        add(s, CCPP.presentOnPlant, it["present"])
    for k, v in it.get("props", {}).items():
        add(s, CCPP[k], v)
    cite(tag, it["cite"])
for tag, (cls, var, stype, sig, grid, floor, mon, cits) in get("INSTRUMENTS", {}).items():
    s = node(tag, cls)
    add(s, CCPP.tag, tag)
    for prop, v in [("measuredVariable", var), ("measuredPhase", get("PHASES", {}).get(tag)), ("sensorType", stype),
                    ("signalType", sig), ("gridReference", grid), ("floor", floor)]:
        add(s, CCPP[prop], v)
    if mon:
        g.add((s, CCPP.monitors, uri(mon)))
    cite(tag, cits)
for tag, (targets, label, cits) in get("CONTROLLERS", {}).items():
    s = node(tag, "Controller", label)
    add(s, CCPP.tag, tag)
    for t in targets:
        g.add((s, CCPP.controls, uri(t)))
    cite(tag, cits)
for name, (label, cits) in get("NOZZLES", {}).items():
    s = node(name, "Nozzle", label)
    g.add((s, CCPP.onEquipment, uri(SEC["nozzle_on"])))
    cite(name, cits)

# The loop or cross-section route
TRAIN_A, TRAIN_B = get("TRAIN_A", []), get("TRAIN_B", [])
L = node(SEC["loop_id"], "Loop", SEC["loop_label"])
g.add((L, CCPP.inMode, CCPP[SEC["mode"]]))
add(L, CCPP.note, SEC.get("loop_note"))
cite(SEC["loop_id"], SEC["loop_cite"])
steps = []
for idx, entry in enumerate(get("LOOP", [])):
    group = entry if isinstance(entry[0], tuple) else (entry,)
    cur = []
    for item, typ in group:
        st = node(f"{SEC['loop_id']}_step_{idx:02d}_{item}", "LoopStep", f"{SEC['loop_label']} step {idx}: {item}")
        g.add((L, CCPP.hasStep, st))
        add(st, CCPP.stepIndex, idx)
        add(st, CCPP.stepType, typ)
        g.add((st, CCPP.stepItem, uri(item)))
        steps.append((idx, item, typ, st))
inline = [(i, t, st) for i, t, typ, st in steps if typ == "inline"]
idxs = sorted({i for i, _, _ in inline})
for a, b in zip(idxs, idxs[1:]):
    for x, sx in [(t, st) for i, t, st in inline if i == a]:
        for y, sy in [(t, st) for i, t, st in inline if i == b]:
            if (x in TRAIN_A and y in TRAIN_B) or (x in TRAIN_B and y in TRAIN_A):
                continue
            if SEC["flow"] == "feedsInto":
                g.add((uri(x), CCPP.feedsInto, uri(y)))
                g.add((uri(x), CCPP.pipedTo, uri(y)))
            else:
                g.add((sx, CCPP.nextStep, sy))
for v, pos in SEC.get("settings", {}).items():
    vs = node(f"{SEC['loop_id']}_setting_{v}", "ValveSetting", f"{v} in {SEC['loop_label']}")
    g.add((L, CCPP.hasValveSetting, vs))
    g.add((vs, CCPP.valve, uri(v)))
    add(vs, CCPP.requiredPosition, pos)
for a, b in get("EXTRA_PIPING", []):
    g.add((uri(a), CCPP.pipedTo, uri(b)))

# Bypasses, control loops, limits, procedures, discrepancies, interlocks, open items
for bid, b in get("BYPASSES", {}).items():
    B = node(bid, "BypassRoute", b["label"])
    g.add((B, CCPP.fromItem, uri(b["from_item"])))
    for v in b["via"]:
        g.add((B, CCPP.routeVia, uri(v)))
    g.add((B, CCPP.toItem, uri(b["to_item"])))
    for t in b["bypasses"]:
        g.add((B, CCPP.bypasses, uri(t)))
    add(B, CCPP.normalState, b["state"])
    if b.get("procedure"):
        g.add((B, CCPP.activatedBy, uri(b["procedure"])))
    cite(bid, b["cite"])
for cid, c in get("CONTROL_LOOPS", {}).items():
    s = node(cid, "ControlLoop", c["label"])
    for prop, key in [("hasSensor", "sensors"), ("hasController", "controllers"), ("hasFinalElement", "final")]:
        for t in c[key]:
            g.add((s, CCPP[prop], uri(t)))
    add(s, CCPP.controlledVariable, c["cv"])
    add(s, CCPP.manipulatedVariable, c["mv"])
    cite(cid, c["cite"])
for m, sl in get("CASCADES", []):
    g.add((uri(m), CCPP.cascadeMasterOf, uri(sl)))
for lid, (tgt, var, typ, lo, hi, unit, cits) in get("LIMITS", {}).items():
    s = node(f"limit_{lid}", "OperatingLimit", lid)
    g.add((s, CCPP.appliesTo, uri(tgt)))
    for prop, v in [("variable", var), ("limitType", typ), ("lowValue", lo), ("highValue", hi), ("unit", unit)]:
        add(s, CCPP[prop], v)
    add(s, CCPP.source, "; ".join(f"{d} {l}" for d, l in cits))
    add(s, CCPP.valueVerified, False)
    cite(f"limit_{lid}", cits)
for pid, p in get("PROCEDURES", {}).items():
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
for did, tags, grid, drawn, built in get("DISCREPANCIES", []):
    s = node(f"discrepancy_{did}", "PIDDiscrepancy", did)
    for t in tags:
        g.add((s, CCPP.concerns, uri(t)))
    add(s, CCPP.gridReference, grid)
    add(s, CCPP.drawingShows, drawn)
    add(s, CCPP.asBuilt, built)
    cite(f"discrepancy_{did}", [("DIFF", f"row {', '.join(tags)} ({grid})")])
for el, tags in get("HAZOP_COVERAGE", {}).items():
    e = uri(f"HAZOP_element_{el}")          # element nodes already exist in the loop KGs
    for t in tags:
        g.add((e, CCPP.covers, uri(t)))
for iid, il in get("INTERLOCKS", {}).items():
    s = node(iid, "Interlock", il["label"])
    for t in il["by"]:
        g.add((s, CCPP.initiatedBy, uri(t)))
    for t in il["trips"]:
        g.add((s, CCPP.tripsItem, uri(t)))
    cite(iid, il["cite"])
for oid, (desc, about, resolved_by) in get("OPEN_ITEMS", {}).items():
    o = node(oid, "OpenItem", f"{oid}: {desc}")
    add(o, CCPP.description, desc)
    add(o, CCPP.resolvedBy, resolved_by)
    add(o, CCPP.itemStatus, "open")
    add(o, CCPP.foundBy, f"{SEC['prefix']} section build, Oct 2026")
    for t in about:
        g.add((o, CCPP.about, uri(t)))
    cite(oid, [("TEAM", f"{SEC['prefix']} section build, Oct 2026")])

out_path.parent.mkdir(parents=True, exist_ok=True)
g.serialize(destination=str(out_path), format="turtle")
print(f"Wrote {len(g)} triples to {out_path}")
