import os, re

# 1. Which of pieces 12 and 13 are complete (both files saved and the ontology block added)?
onto = open("ontology/ccpp_ontology.ttl").read()
pieces = {
    "procedures": dict(files=["procedures/procedures_data.py", "procedures/ask_100_procedures.py"], term="ccpp:AlarmResponse",
                       row='    ("Procedures and alarm responses", "procedures/procedures_data.py", "procedures/procedures.ttl", "procedures/ask_100_procedures.py"),\n'),
    "causal": dict(files=["causal/causal_data.py", "causal/ask_100_causal.py"], term="ccpp:ProcessVariable",
                   row='    ("Causal layer", "causal/causal_data.py", "causal/causal.ttl", "causal/ask_100_causal.py"),\n'),
}
ready = {}
for name, p in pieces.items():
    missing = [f for f in p["files"] if not os.path.exists(f)] + ([] if p["term"] in onto else ["its ontology block"])
    ready[name] = not missing
    print(f"{name}: {'ready' if not missing else 'MISSING ' + ', '.join(missing)}")
if ready["causal"] and not ready["procedures"]:
    ready["causal"] = False
    print("causal: held back, it needs piece 12 (procedures) first")

# 2. Join: add each ready piece after the previous one
p = "ccpp/build_full_plant.py"
s = open(p).read()
after = '    "vents_n2": ROOT / "vents_n2" / "vents_n2.ttl",\n'
for name in ("procedures", "causal"):
    line = f'    "{name}": ROOT / "{name}" / "{name}.ttl",\n'
    if ready[name] and line not in s and after in s:
        s = s.replace(after, after + line, 1)
    after = line
open(p, "w").write(s)

# 3. Runner: same, after the vents row
p = "ccpp/build_and_test_all.py"
r = open(p).read()
m = re.search(r'    \("Vents, N2 header, make-up water",[^\n]*\n', r)
after = m.group(0) if m else None
for name in ("procedures", "causal"):
    row = pieces[name]["row"]
    if ready[name] and row not in r and after in r:
        r = r.replace(after, after + row, 1)
    after = row
open(p, "w").write(r)

# 4. Open item count: 94 for pieces 1 to 11, plus 2 for each of pieces 12 and 13 that is joined
count = 94 + sum(2 for name in pieces if f'"{name}":' in s)
p = "ccpp/test_full_plant.py"
t = open(p).read()
t, k = re.subn(r"(\('W09', [^\n]*\n  [^\n]*\n  )\[[^\n]*\]\),", lambda m2: m2.group(1) + f"['{count}']),", t, count=1)
open(p, "w").write(t)

print("Join lists procedures:", '"procedures":' in s, "| causal:", '"causal":' in s)
print("Runner lists procedures:", "procedures/procedures_data.py" in r, "| causal:", "causal/causal_data.py" in r)
print(f"Open item count set to {count}:", k == 1)