"""
Build and test every part of the pilot plant KG in the right order, then print one summary.

Run from the repo root:   python ccpp/build_and_test_all.py
Add --mutation to also run the absorption loop deliberate-error test (slower).

To add a new piece: add one line to PIECES (its data file, its .ttl, its 100-question file),
and add it to SECTIONS in ccpp/build_full_plant.py.
"""
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
PY = sys.executable

# Pieces built with the shared kgkit builder: (name, data file, output .ttl, 100-question file or None)
PIECES = [
    ("Rich-side link", "rich_link/rich_link_data.py", "rich_link/rich_link.ttl", None),
    ("Overhead and reflux", "overhead/overhead_data.py", "overhead/overhead.ttl", "overhead/ask_100_overhead.py"),
    ("Feed gas and K101", "gas_feed/gas_feed_data.py", "gas_feed/gas_feed.ttl", "gas_feed/ask_100_gas_feed.py"),
    ("Absorber overhead", "abs_overhead/abs_overhead_data.py", "abs_overhead/abs_overhead.ttl", "abs_overhead/ask_100_abs_overhead.py"),
]


def ok_exit(out, code):
    return code == 0


def ok_failures(out, code):
    return re.search(r"(?<!\d)0 failure\(s\)", out) is not None


def ok_join(out, code):
    return code == 0 and "(0 unexplained)" in out and "Broken links: 0" in out and "connected: True" in out


def ok_hundred(out, code):
    return code == 0 and "FAIL 0, QUERY ERROR 0" in out


STEPS = [
    ("Stripping loop: build", ["stripping_loop/build_stripping_loop.py"], ok_exit),
    ("Stripping loop: competency questions + SHACL", ["stripping_loop/test_queries.py"], ok_failures),
    ("Absorption loop: build", ["absorption_loop/build_absorption_loop.py"], ok_exit),
    ("Absorption loop: 38 tests + SHACL", ["absorption_loop/test_absorption.py"], ok_failures),
    ("Absorption loop: 100 questions", ["absorption_loop/ask_100_absorption.py"], ok_hundred),
]
STEPS += [(f"{name}: build", ["kgkit/build_section.py", data, ttl], ok_exit) for name, data, ttl, _ in PIECES]
STEPS += [("Full plant: join (conflicts, broken links, figure-of-eight)", ["ccpp/build_full_plant.py"], ok_join),
          ("Full plant: tests + SHACL", ["ccpp/test_full_plant.py"], ok_failures)]
STEPS += [(f"{name}: 100 questions", [ask], ok_hundred) for name, _, _, ask in PIECES if ask]
if "--mutation" in sys.argv:
    STEPS.append(("Absorption loop: mutation test", ["absorption_loop/mutation_test.py"],
                  lambda out, code: code == 0 and "13 of 13" in out))

results = []
for label, args, check in STEPS:
    if not (ROOT / args[0]).exists():
        results.append((label, "SKIPPED", f"{args[0]} not found"))
        continue
    run = subprocess.run([PY, *args], cwd=ROOT, capture_output=True, text=True)
    out = run.stdout + run.stderr
    last = [l for l in out.strip().splitlines() if l.strip()][-1:] or [""]
    status = "PASS" if check(out, run.returncode) else "FAIL"
    results.append((label, status, last[0][:110]))
    print(f"{status:7s} {label}\n        {last[0][:110]}")
    if status == "FAIL":
        print("        --- last lines of output ---")
        for l in out.strip().splitlines()[-12:]:
            print("        " + l[:140])

passed = sum(r[1] == "PASS" for r in results)
print(f"\n{passed} of {len(results)} steps passed" + ("" if passed == len(results) else "  (see FAIL lines above)"))
sys.exit(0 if passed == len(results) else 1)
