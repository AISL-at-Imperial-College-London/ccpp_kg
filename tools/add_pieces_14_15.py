"""
Add piece 14 (safety logic) and piece 15 (electrical) to the join, the runner and the full-plant counts.
Safe to run more than once: each piece is added only if its files are complete and it is not already joined,
and the counts are changed only at the moment a piece is added.
Run from the repo root:   python tools/add_pieces_14_15.py
"""
import ast
import os
import pathlib
import re

ROOT = pathlib.Path(".")
onto = (ROOT / "ontology/ccpp_ontology.ttl").read_text()
PIECES = {   # name: (label in the runner, ontology term that must exist, open items it adds, source documents it adds)
    "safety_logic": ("Safety logic (cause and effect, relief schedule)", "ccpp:SafetyTrip", 8, 2),
    "electrical": ("Electrical power distribution", "ccpp:ElectricalPanel", 5, 1),
}

def expected(test_text, qid):
    m = re.search(r"(\('" + qid + r"', [^\n]*\n  [^\n]*\n  )(\[[^\n]*\])\),", test_text)
    return (m, ast.literal_eval(m.group(2))) if m else (None, None)

def set_expected(test_text, qid, value):
    m, _ = expected(test_text, qid)
    return test_text[:m.start(2)] + repr(value) + test_text[m.end(2):] if m else test_text

join_p, run_p, test_p = "ccpp/build_full_plant.py", "ccpp/build_and_test_all.py", "ccpp/test_full_plant.py"
join, runner, test = open(join_p).read(), open(run_p).read(), open(test_p).read()

if not os.path.exists("kgkit/new_sources.py"):
    raise SystemExit("MISSING kgkit/new_sources.py (both pieces need it)")

for name, (label, term, n_open, n_sources) in PIECES.items():
    files = [f"{name}/{name}_data.py", f"{name}/ask_100_{name}.py"]
    missing = [f for f in files if not os.path.exists(f)] + ([] if term in onto else ["its ontology block"])
    if missing:
        print(f"{name}: MISSING {', '.join(missing)}  (not added)")
        continue
    if f'"{name}":' in join:
        print(f"{name}: already joined")
        continue
    # join and runner: insert before the closing bracket of each list
    join = re.sub(r"(SECTIONS = \{.*?\n)(\})", lambda m: m.group(1) + f'    "{name}": ROOT / "{name}" / "{name}.ttl",\n' + m.group(2), join, count=1, flags=re.S)
    row = f'    ("{label}", "{name}/{name}_data.py", "{name}/{name}.ttl", "{name}/ask_100_{name}.py"),\n'
    runner = re.sub(r"(PIECES = \[.*?\n)(\])", lambda m: m.group(1) + row + m.group(2), runner, count=1, flags=re.S)
    # counts: open items (W09) and source documents (W05)
    for qid, add in (("W09", n_open), ("W05", n_sources)):
        m, val = expected(test, qid)
        if m:
            test = set_expected(test, qid, [str(int(val[0]) + add)])
    # shutdown valves (W02): XV128 and XV129 are added by piece 14 unless an earlier section already holds them
    if name == "safety_logic":
        other = "".join(p.read_text() for p in ROOT.glob("*/*.ttl") if p.parent.name not in ("safety_logic", "ccpp", "ontology"))
        new = [t for t in ("XV128", "XV129") if not re.search(r"^ccpp:" + t + r"\s+a\s", other, re.M)]
        m, val = expected(test, "W02")
        if m and new:
            test = set_expected(test, "W02", val + [t for t in new if t not in val])
    print(f"{name}: added")

open(join_p, "w").write(join); open(run_p, "w").write(runner); open(test_p, "w").write(test)
for qid, what in (("W02", "shutdown valves"), ("W05", "source documents"), ("W09", "open items")):
    print(f"  full-plant {qid} ({what}) now expects:", expected(test, qid)[1])
print("Join lists:", [n for n in PIECES if f'"{n}":' in join], "| runner lists:", [n for n in PIECES if f"{n}/{n}_data.py" in runner])
