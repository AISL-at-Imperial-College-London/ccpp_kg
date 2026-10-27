"""
Join every section KG into the full-plant KG and check the joins.

Run from the repo root:   python ccpp/build_full_plant.py
Output: ccpp/full_plant.ttl and ccpp/join_report.md

Checks:
  1. Conflicts: an item described in two sections with different values (floor, grid, type, position, ...)
  2. Broken links: a reference to a node that no section defines
  3. Figure-of-eight: the route steps connect from the E101 sump all the way back to E101
"""
import pathlib
from collections import defaultdict

from rdflib import Graph, Namespace, RDF, URIRef

ROOT = pathlib.Path(__file__).resolve().parents[1]
CCPP = Namespace("http://imperial.ac.uk/ccpp#")
SECTIONS = {  # add each new section here as it is built
    "stripping": ROOT / "stripping_loop" / "stripping_loop.ttl",
    "absorption": ROOT / "absorption_loop" / "absorption_loop.ttl",
    "rich_link": ROOT / "rich_link" / "rich_link.ttl",
}
COMPARE = ["floor", "gridReference", "valveType", "normalPosition", "sensorType", "signalType"]
# Conflicts that are understood and correct (each value is right for its own operating mode)
EXPLAINED = {
    ("V217", "normalPosition"): "Open for the stripping loop commissioning test (REPORT Fig E.2), closed in normal running "
                                "(REPORT B.1.7). The figure-of-eight valve settings hold the normal-running position.",
}

ont = Graph().parse(ROOT / "ontology" / "ccpp_ontology.ttl")
full = Graph()
parts = {}
for name, path in SECTIONS.items():
    parts[name] = Graph().parse(path)
    full += parts[name]
    print(f"  {name:12s} {len(parts[name]):6d} triples")


def short(x):
    return str(x).replace(str(CCPP), "")


# 1. conflicts between sections
conflicts = []
tagged = defaultdict(set)
for name, g in parts.items():
    for s in g.subjects(CCPP.tag, None):
        tagged[s].add(name)
for s, names in sorted(tagged.items()):
    if len(names) < 2:
        continue
    for prop in COMPARE + ["type"]:
        p = RDF.type if prop == "type" else CCPP[prop]
        vals = {n: {short(o) for o in parts[n].objects(s, p)} for n in names}
        filled = {n: v for n, v in vals.items() if v}
        if len({frozenset(v) for v in filled.values()}) > 1:
            conflicts.append((short(s), prop, filled, EXPLAINED.get((short(s), prop))))

# 2. broken links (objects that nothing defines)
defined = set(full.subjects()) | set(ont.subjects())
broken = sorted({(short(s), short(p), short(o)) for s, p, o in full
                 if isinstance(o, URIRef) and str(o).startswith(str(CCPP)) and p != RDF.type and o not in defined})

# 3. figure-of-eight continuity
fig = CCPP.FigureOfEight
steps = list(full.objects(fig, CCPP.hasStep))
first = [s for s in steps if int(full.value(s, CCPP.stepIndex)) == 0]
last_idx = max(int(full.value(s, CCPP.stepIndex)) for s in steps) if steps else -1
reach, stack = set(first), list(first)
while stack:
    for nxt in full.objects(stack.pop(), CCPP.nextStep):
        if nxt not in reach:
            reach.add(nxt)
            stack.append(nxt)
fig_ok = any(int(full.value(s, CCPP.stepIndex)) == last_idx for s in reach)

out = ROOT / "ccpp" / "full_plant.ttl"
full.serialize(destination=str(out), format="turtle")
lines = ["# Full-plant join report", "", f"Sections: {', '.join(SECTIONS)}", f"Triples: {len(full)}", "",
         f"## Conflicts between sections ({len(conflicts)})", ""]
lines += [f"- {s} {prop}: " + "; ".join(f"{n} = {sorted(v)}" for n, v in vals.items())
          + (f"  EXPLAINED: {why}" if why else "  UNEXPLAINED: check the sources") for s, prop, vals, why in conflicts] or ["- none"]
lines += ["", f"## Broken links ({len(broken)})", ""] + ([f"- {s} {p} {o}" for s, p, o in broken] or ["- none"])
lines += ["", "## Figure-of-eight route", "", f"- {len(steps)} steps; connected from the E101 sump back to E101: {fig_ok}"]
(ROOT / "ccpp" / "join_report.md").write_text("\n".join(lines) + "\n")
print(f"Wrote {len(full)} triples to {out}")
unexplained = [c for c in conflicts if not c[3]]
print(f"Conflicts: {len(conflicts)} ({len(unexplained)} unexplained)  Broken links: {len(broken)}  Figure-of-eight connected: {fig_ok}")
for s, prop, vals, why in conflicts:
    print(f"  {'EXPLAINED' if why else 'UNEXPLAINED'} {s} {prop}: " + "; ".join(f"{n} = {sorted(v)}" for n, v in vals.items()))
for s, p, o in broken[:20]:
    print(f"  BROKEN {s} {p} {o}")
