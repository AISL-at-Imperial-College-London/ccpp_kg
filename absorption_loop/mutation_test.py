"""
Mutation test for the absorption loop KG: put one realistic mistake into
absorption_data.py at a time, rebuild, rerun test_absorption.py, and check a
question fails. The original file is always restored at the end.

Run from the repo root:   python absorption_loop/mutation_test.py
"""
import os
import pathlib
import re
import shutil
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE / "absorption_data.py"
BACKUP = HERE / "absorption_data.py.bak"
ENV = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")

MUTATIONS = [
    ("Swap V211 and V213 around N200",
     '("V211", "inline"), ("N200", "inline"), ("V213", "inline"),',
     '("V213", "inline"), ("N200", "inline"), ("V211", "inline"),'),
    ("Drop V124 from the loop",
     '    ("V124", "inline"),\n', ''),
    ("Merge the two pump trains (lose train separation)",
     'TRAIN_B = ["V134b", "V135b", "J101b", "TT111b", "PCV120b", "B103b", "PT115b", "V143b", "V144b"]',
     'TRAIN_B = []'),
    ("Make NRV400 an ordinary manual valve",
     '"NRV400": dict(cls="CheckValve"', '"NRV400": dict(cls="ManualValve"'),
    ("Claim RV106a is on the plant",
     '"RV106a": dict(cls="ReliefValve", valve="relief", floor=1, grid="M14", pos="closed", present=False,',
     '"RV106a": dict(cls="ReliefValve", valve="relief", floor=1, grid="M14", pos="closed", present=True,'),
    ("Open the wrong train's valve for J101b",
     'settings={"V134b": "open", "V135b": "open", "V143b": "open", "V144b": "open",\n                                     "V134a": "closed",',
     'settings={"V134b": "open", "V135b": "open", "V143b": "open", "V144b": "open",\n                                     "V134a": "open",'),
    ("Lose what TT210 measures",
     '"lean MEA leaving C200 (entering E101)"', '"lean MEA leaving C200"'),
    ("Reverse the C200 cascade",
     'CASCADES = [("CL_C200_temperature", "CL_C200_cooling_water")]',
     'CASCADES = [("CL_C200_cooling_water", "CL_C200_temperature")]'),
    ("Wrong PSHH117 trip pressure",
     '"PSHH117_set": ("E101", "pressure", "trip", None, 3.5,',
     '"PSHH117_set": ("E101", "pressure", "trip", None, 4.5,'),
    ("Close the wrong valve in the N200 bypass",
     '("Close V213", "V213", "closed")', '("Close V212", "V212", "closed")'),
    ("Remove J101a from HAZOP element 8",
     '"8": ["J101a", "J101b",', '"8": ["J101b",'),
    ("Delete the citations for E101",
     'cite=[("PID", "column E101, grids F15 to K16"), ("REPORT", "section D.4 (absorber level control)"),\n                       ("ASPEN_V3", "block E101")]),',
     'cite=[]),'),
    ("Call V119a an ordinary ball valve",
     '"V119a": dict(cls="ManualValve", valve="3-way ball"', '"V119a": dict(cls="ManualValve", valve="ball"'),
]


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True, env=ENV, cwd=HERE.parent)


original = DATA.read_text()
shutil.copy(DATA, BACKUP)
caught = 0
try:
    for name, old, new in MUTATIONS:
        if old not in original:
            print(f"SKIPPED  {name}: pattern not found (has the data file changed?)")
            continue
        DATA.write_text(original.replace(old, new, 1))
        shutil.rmtree(HERE / "__pycache__", ignore_errors=True)
        build = run([sys.executable, "absorption_loop/build_absorption_loop.py"])
        if build.returncode != 0:
            print(f"CAUGHT   {name}: the build itself failed")
            caught += 1
            continue
        test = run([sys.executable, "absorption_loop/test_absorption.py"])
        failed = re.findall(r"^\[(A\d+)\] (?:FAIL|QUERY ERROR|NO ANSWER)", test.stdout, re.M)
        shacl = "SHACL validation: FAIL" in test.stdout
        if failed or shacl:
            caught += 1
            print(f"CAUGHT   {name}: {', '.join(failed)}{' + SHACL' if shacl else ''}")
        else:
            print(f"MISSED   {name}")
finally:
    shutil.copy(BACKUP, DATA)
    BACKUP.unlink()
    shutil.rmtree(HERE / "__pycache__", ignore_errors=True)
    run([sys.executable, "absorption_loop/build_absorption_loop.py"])
print(f"\n{caught} of {len(MUTATIONS)} deliberate errors caught. Original data restored and KG rebuilt.")
