"""
Ask the fill-in section (the report tags not in any other piece) 100 questions whose expected answers come from the
documents (the team then traces and checks it on the P&ID), not from the KG. The fill-in links to items in other
sections, so the questions run on the joined full plant.
Run from the repo root (after ccpp/build_full_plant.py):   python fill_in/ask_100_fill_in.py
Output: fill_in/hundred_results_fill_in.md
"""
import collections
import pathlib
import sys

from rdflib import Graph

HERE = pathlib.Path(__file__).resolve().parent
NS = "http://imperial.ac.uk/ccpp#"
PRE = f"PREFIX ccpp: <{NS}>\nPREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>\n"
g = Graph()
g.parse(HERE.parent / "ontology" / "ccpp_ontology.ttl")
g.parse(HERE.parent / "ccpp" / "full_plant.ttl")


def T(x): return f"ccpp:{x}"
def ALL(*trip): return "ASK { " + " ".join(f"{T(s)} {T(p)} {T(o)} ." for s, p, o in trip) + " }"
def VAL(s, p): return f"SELECT ?v WHERE {{ {T(s)} {T(p)} ?v }}"
def CLSP(c, prefix): return (f"SELECT DISTINCT ?t WHERE {{ ?x a/rdfs:subClassOf* {T(c)} ; ccpp:tag ?t ; ccpp:citedIn ?c . "
                             f"FILTER(CONTAINS(STR(?c), \"__{prefix}cit\")) }}")
def CNTOI(prefix): return f"SELECT (COUNT(?o) AS ?n) WHERE {{ ?o a ccpp:OpenItem ; ccpp:foundBy \"{prefix} section build, Oct 2026\" }}"


P = "fil"
# expected values typed from the REPORT lists (independent of fill_in_data.py)
GRID = {"V107":"K8","V108":"L8","V200":"J8","V201":"J8","V202":"H8","V203":"H8","V300":"H8","V301":"H8","V400":"F8","V401":"F8","V131":"L16","V133":"O15",
        "V139a":"N15","V139b":"N16","V141a":"P14","V141b":"P16","V142a":"O14","V142b":"O17","NRV105a":"O14","NRV105b":"O16","V137a":"O19","V137b":"O19",
        "V166":"O18","V180":"O19","V181":"P19","V182a":"Q19","V182b":"Q19","V183":"P19","NRV100a":"Q19","NRV100b":"Q19","NRV109":"P21","V190":"K22",
        "NRV106":"M8","PCV104":"N17","RV105":"K19","RV301":"G8","SDV169":"P18","SDV421":"C10","SDV424":"D16","LI108":"K15","PT115a":"N14","TT110a":"N15",
        "TT110b":"N16","PI401":"C8","PI106":"K22","PI107":"K22","PI108":"N22","PI109":"N22","PI114":"P21","AT100":"N10","TT102":"K7","TT108":"L15",
        "TT120":"M18","TT211":"J14","TT214":"H13","TT215":"J13","TT216":"J13","TT217":"H7","TT402":"C7","TT403":"C11","TT404":"D9"}
SENSOR = {"PT115a":"gauge pressure transmitter","TT110a":"PRT","TT110b":"PRT","AT100":"inline pH transmitter","TT102":"PRT","TT108":"PRT","TT120":"PRT",
          "TT211":"K-type thermocouple","TT214":"PRT","TT215":"K-type thermocouple","TT216":"PRT","TT217":"K-type thermocouple","TT402":"PRT","TT403":"PRT","TT404":"PRT"}
MON = {"LI108":"E101","PT115a":"J101a","TT110a":"J101a","TT110b":"J101b","PI401":"E100","PI106":"CO2_SUPPLY","PI107":"CO2_SUPPLY","PI108":"N2_SUPPLY",
       "PI109":"N2_SUPPLY","PI114":"N2_SUPPLY"}
OI = {"FI01":"V200","FI02":"V133","FI03":"V180","FI04":"V190","FI05":"TT214","FI06":"SDV421","FI07":"AT100"}
Q = []
for i, (t, gr) in enumerate(GRID.items(), 1):
    Q.append((f"G{i:02d}", "Grid", f"What grid is {t} at?", VAL(t, "gridReference"), [gr]))
for i, (t, v) in enumerate(SENSOR.items(), 1):
    Q.append((f"S{i:02d}", "Sensor", f"What type of sensor is {t}?", VAL(t, "sensorType"), [v]))
for i, (t, e) in enumerate(MON.items(), 1):
    Q.append((f"M{i:02d}", "Links", f"Does {t} monitor {e}?", ALL((t, "monitors", e)), ["true"]))
for i, (o, t) in enumerate(OI.items(), 1):
    Q.append((f"O{i:02d}", "Open items", f"Is open item {o} about {t}?", ALL((o, "about", t)), ["true"]))
Q += [
 ("X01","Links","Does HAZOP 1.1 (vent valve added on the CO2 feed) concern V190?", ALL(("HAZOP_1_01","concerns","V190")), ["true"]),
 ("X02","Links","Does RV301 protect J300?", ALL(("RV301","protects","J300")), ["true"]),
 ("X03","Classes","Which shutdown valves does the fill-in add?", CLSP("ShutdownValve",P), ["SDV169","SDV421","SDV424"]),
 ("X04","Classes","Which relief valves does the fill-in add?", CLSP("ReliefValve",P), ["RV105","RV301"]),
 ("X05","Classes","Which check valves does the fill-in add?", CLSP("CheckValve",P), ["NRV100a","NRV100b","NRV105a","NRV105b","NRV106","NRV109"]),
 ("X06","Classes","Which pressure control valve does the fill-in add?", CLSP("PressureControlValve",P), ["PCV104"]),
 ("X07","Open items","How many open items does the fill-in hold?", CNTOI(P), ["7"]),
]


def norm(x):
    x = str(x).strip().replace(NS, "")
    try:
        return repr(float(x))
    except ValueError:
        return x


results = []
for qid, cat, question, sparql, expect in Q:
    try:
        res = g.query(PRE + sparql)
        rows = [[str(res.askAnswer).lower()]] if res.type == "ASK" else [
            ["" if v is None else str(v).replace(NS, "") for v in r] for r in res]
        err = None
    except Exception as e:  # noqa: BLE001
        rows, err = [], str(e)
    got = {norm(r[0]) for r in rows if r and r[0] != ""}
    status = "QUERY ERROR" if err else ("PASS" if got == {norm(x) for x in expect} else "FAIL")
    results.append((qid, cat, question, expect, rows, status, err))

count = collections.Counter(r[5] for r in results)
lines = ["# Fill-in KG: 100-question run", "", f"PASS {count['PASS']}, FAIL {count['FAIL']}, QUERY ERROR {count['QUERY ERROR']}", ""]
for qid, cat, question, expect, rows, status, err in results:
    lines += [f"## {qid} [{cat}] {status}", "", f"**{question}**", "", f"- Expected: {', '.join(expect)}"]
    lines += [f"- Error: {err}"] if err else [f"- KG: {', '.join(r[0] for r in rows) or '(no rows)'}"]
    lines.append("")
(HERE / "hundred_results_fill_in.md").write_text("\n".join(lines))
for qid, cat, question, expect, rows, status, err in results:
    if status != "PASS":
        print(f"[{qid}] {status} {question}\n      expected: {expect}\n      got: {[r[0] for r in rows]} {err or ''}")
print(f"\nPASS {count['PASS']}, FAIL {count['FAIL']}, QUERY ERROR {count['QUERY ERROR']}  (details in fill_in/hundred_results_fill_in.md)")
sys.exit(1 if count["FAIL"] or count["QUERY ERROR"] else 0)