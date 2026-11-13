"""
Register the documents received from the plant (Nov 2026) in the source register, and switch pieces 14 and 15 over
to it. Safe to run more than once.   Run from the repo root:   python tools/register_new_sources.py
"""
import re

NEW = [   # key, short name, title, file name
    ("CE", "C&E matrix Rev 5", "Cause and effect matrix, Rev 5, 06/10/2011, final for construction", "CauseAndEffectRev5_2.xls"),
    ("RVSCHED", "RV schedule", "Relief valve schedule", "RV_Schedule.xlsx"),
    ("CABLE", "Cable diagrams", "Cable diagrams C2286-CD-001, JMS Automation & Drives, 15 August 2011 (preliminary issue)", "Cable_Diagrams_-_Preliminary_Issue.pdf"),
]

# 1. the source register: add each new document after the HAZOP line, copying its indentation
p = "stripping_loop/sources.py"
s = open(p).read()
m = re.search(r'^(\s*)"HAZOP": \(.*\),\n', s, re.M)
if not m:
    raise SystemExit('Could not find the "HAZOP": (...) line in stripping_loop/sources.py; send me lines 15 to 30 of that file')
added = []
for key, short, title, fname in NEW:
    if f'"{key}": (' not in s:
        line = f'{m.group(1)}"{key}": ("{short}", "{title}", "{fname}"),\n'
        at = re.search(r'^(\s*)"HAZOP": \(.*\),\n', s, re.M).end()
        s = s[:at] + line + s[at:]
        added.append(key)
open(p, "w").write(s)
print("Source register: added", added or "nothing (already registered)")

# 2. pieces 14 and 15: the builder now creates the source nodes itself, so drop the helper lines
for p in ("safety_logic/safety_logic_data.py", "electrical/electrical_data.py"):
    s = open(p).read()
    s2 = re.sub(r'^ITEMS\.update\(source_item\(.*\)\)\n', "", s, flags=re.M)
    s2 = re.sub(r'^from new_sources import source_item.*\n', "", s2, flags=re.M)
    open(p, "w").write(s2)
    print(f"{p}: {'helper lines removed' if s2 != s else 'already clean'}")