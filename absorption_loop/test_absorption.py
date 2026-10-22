"""
Test the absorption loop KG: SPARQL questions with expected answers, then SHACL.

Expectation types:
  [values]  set of first-column values (order ignored)  -> PASS / FAIL
  []        expect no rows                              -> PASS / FAIL
  "ANY"     an answer should exist; printed for review -> ANSWERED / NO ANSWER
Run from the repo root:   python absorption_loop/test_absorption.py
"""
import pathlib
import sys

from rdflib import Graph

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
NS = "http://imperial.ac.uk/ccpp#"
PRE = f"PREFIX ccpp: <{NS}>\nPREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>\n"
g = Graph()
g.parse(ROOT / "ontology" / "ccpp_ontology.ttl")
g.parse(HERE / "absorption_loop.ttl")
REC = "?c ccpp:recommendedForUse true ."

Q = [
 # flow path
 ("A01", "What feeds directly into C200?", "SELECT ?t WHERE { ?x ccpp:feedsInto ccpp:C200 ; ccpp:tag ?t }", ["V213"]),
 ("A02", "What does C200 feed into?", "SELECT ?t WHERE { ccpp:C200 ccpp:feedsInto ?x . ?x ccpp:tag ?t }", ["NRV400"]),
 ("A03", "What does V124 feed into?", "SELECT ?t WHERE { ccpp:V124 ccpp:feedsInto ?x . ?x ccpp:tag ?t }", ["V119b"]),
 ("A04", "What does FT108 feed into?", "SELECT ?t WHERE { ccpp:FT108 ccpp:feedsInto ?x . ?x ccpp:tag ?t }", ["FT109"]),
 ("A05", "What feeds directly into FT108?", "SELECT ?t WHERE { ?x ccpp:feedsInto ccpp:FT108 ; ccpp:tag ?t }", ["V144a", "V144b"]),
 ("A06", "Is the absorption loop closed?", "ASK { ccpp:E101 ccpp:feedsInto+ ccpp:E101 }", ["true"]),
 ("A07", "Does the J101a train feed straight into J101b?", "ASK { ccpp:V135a ccpp:feedsInto ccpp:J101b }", ["false"]),
 ("A08", "Where does lean MEA from the stripping loop join this loop?", "SELECT ?t WHERE { ccpp:SDV123 ccpp:pipedTo ?x . ?x ccpp:tag ?t }", ["V119b"]),
 # equipment and valves
 ("A09", "Which pumps take liquid out of E101?", "SELECT ?t WHERE { ?p a ccpp:Pump ; ccpp:tag ?t }", ["J101a", "J101b"]),
 ("A10", "Which valve bypasses N200?", "SELECT ?t WHERE { ?v ccpp:bypasses ccpp:N200 ; ccpp:tag ?t }", ["V212"]),
 ("A11", "What does the N200 bypass skip?", "SELECT ?t WHERE { ccpp:N200_bypass ccpp:bypasses/ccpp:tag ?t }", ["V211", "N200", "V213"]),
 ("A12", "What does the flow meter test spool route skip?", "SELECT ?t WHERE { ccpp:FM_spool_route ccpp:bypasses/ccpp:tag ?t }", ["V119a", "V119b"]),
 ("A13", "Which items does the test spool route go through?", "SELECT ?x WHERE { ccpp:FM_spool_route ccpp:routeVia ?x }", ["V198b", "FM_TEST_SPOOL", "V198a"]),
 ("A14", "Which check valve is on the absorber inlet?", "SELECT ?t WHERE { ?v a ccpp:CheckValve ; ccpp:tag ?t }", ["NRV400"]),
 ("A15", "Which floor is NRV400 on?", "SELECT ?f WHERE { ccpp:NRV400 ccpp:floor ?f }", ["4"]),
 ("A16", "Which relief valves are drawn but not on the plant?", "SELECT ?t WHERE { ?v ccpp:presentOnPlant false ; ccpp:tag ?t }", ["RV106a", "RV106b"]),
 # routes
 ("A17", "Which valves must be open to run on J101b?",
  "SELECT ?t WHERE { ccpp:AbsRoute_J101b ccpp:hasValveSetting ?s . ?s ccpp:requiredPosition \"open\" ; ccpp:valve/ccpp:tag ?t }",
  ["V134b", "V135b", "V143b", "V144b", "V124"]),
 ("A18", "Does the J101a route include J101b?", "ASK { ccpp:AbsRoute_J101a ccpp:hasStep/ccpp:stepItem ccpp:J101b }", ["false"]),
 # instruments and control
 ("A19", "Which instrument measures the temperature of MEA entering E101?",
  "SELECT ?t WHERE { ?i ccpp:measuredVariable ?v ; ccpp:tag ?t . FILTER(CONTAINS(?v, \"entering E101\")) }", ["TT210"]),
 ("A20", "Which temperature instruments monitor C200?",
  "SELECT ?t WHERE { ?i a ccpp:TemperatureInstrument ; ccpp:monitors ccpp:C200 ; ccpp:tag ?t }", ["TT208", "TT209", "TT210", "TI210"]),
 ("A21", "Which instruments report density?", "SELECT ?t WHERE { ?i ccpp:measuredVariable ?v ; ccpp:tag ?t . FILTER(CONTAINS(?v, \"density\")) }", ["FT108", "DI108"]),
 ("A22", "Which control loop is the cascade master?", "SELECT ?m WHERE { ?m ccpp:cascadeMasterOf ?s }", ["CL_C200_temperature"]),
 ("A23", "What does the E101 level loop adjust?", "SELECT ?t WHERE { ccpp:CL_E101_level ccpp:hasFinalElement/ccpp:tag ?t }", ["J101a", "J101b"]),
 # limits and procedures
 ("A24", "At what pressure does PSHH117 trip?", "SELECT ?v WHERE { ccpp:limit_PSHH117_set ccpp:highValue ?v }", ["3.5"]),
 ("A25", "What is the top of the FT109 range?", "SELECT ?v WHERE { ccpp:limit_FT109_range ccpp:highValue ?v }", ["1250"]),
 ("A26", "Which valves are closed in the N200 bypass procedure?",
  "SELECT ?t WHERE { ccpp:PROC_N200_bypass ccpp:hasProcedureStep ?s . ?s ccpp:requiredPosition \"closed\" ; ccpp:operatesOn/ccpp:tag ?t }", ["V211", "V213"]),
 ("A27", "Which valves does the J101a start-up open?",
  "SELECT ?t WHERE { ccpp:PROC_J101a_startup ccpp:hasProcedureStep ?s . ?s ccpp:requiredPosition \"open\" ; ccpp:operatesOn/ccpp:tag ?t }",
  ["V134a", "V135a", "V143a", "V144a"]),
 ("A28", "Which HAZOP element covers J101a?", "SELECT ?el WHERE { ?e ccpp:covers ccpp:J101a ; ccpp:elementNumber ?el }", ["8"]),
 # heat and mass transfer
 ("A29", "What is the C200 duty in the recommended case?",
  f"SELECT ?d WHERE {{ ?p ccpp:ofEquipment ccpp:C200 ; ccpp:inCase ?c ; ccpp:duty_kW ?d . {REC} }}", "ANY"),
 ("A30", "What is the E101 CO2 capture efficiency in the recommended case?",
  f"SELECT ?e WHERE {{ ?p ccpp:ofEquipment ccpp:E101 ; ccpp:inCase ?c ; ccpp:captureEfficiency_pct ?e . {REC} }}", "ANY"),
 ("A31", "Does the E101 CO2 balance close within 1 %?",
  f"ASK {{ ?p ccpp:ofEquipment ccpp:E101 ; ccpp:inCase ?c ; ccpp:co2BalanceError_pct ?e . {REC} FILTER(?e < 1.0) }}", ["true"]),
 # documentation quality
 ("A32", "How many P&ID discrepancies are recorded for this loop?", "SELECT (COUNT(?d) AS ?n) WHERE { ?d a ccpp:PIDDiscrepancy }", ["5"]),
 ("A33", "How many open items did the absorption build raise?",
  "SELECT (COUNT(?o) AS ?n) WHERE { ?o a ccpp:OpenItem ; ccpp:foundBy \"absorption loop build, Oct 2026\" }", ["12"]),
 ("A34", "Which open items concern J101a?", "SELECT ?o WHERE { ?o a ccpp:OpenItem ; ccpp:about ccpp:J101a }", ["AOI02", "AOI04", "AOI09"]),
 ("A35", "Is any plant item missing a citation?",
  "SELECT ?t WHERE { ?i a/rdfs:subClassOf* ccpp:PlantItem ; ccpp:tag ?t . FILTER NOT EXISTS { ?i ccpp:citedIn ?c } }", []),
]


def norm(x):
    x = str(x).strip().replace(NS, "")
    try:
        return repr(float(x))
    except ValueError:
        return x


failures = 0
for qid, question, sparql, expect in Q:
    try:
        res = g.query(PRE + sparql)
        rows = [[str(res.askAnswer).lower()]] if res.type == "ASK" else [
            ["" if v is None else str(v).replace(NS, "") for v in r] for r in res]
        err = None
    except Exception as e:  # noqa: BLE001
        rows, err = [], str(e)
    got = {norm(r[0]) for r in rows if r and r[0] != ""}
    if err:
        status = "QUERY ERROR"
    elif isinstance(expect, list):
        status = "PASS" if got == {norm(x) for x in expect} else "FAIL"
    else:
        status = "ANSWERED" if rows else "NO ANSWER"
    if status in ("FAIL", "QUERY ERROR", "NO ANSWER"):
        failures += 1
    shown = ", ".join(r[0] for r in rows[:8]) + (" ..." if len(rows) > 8 else "")
    print(f"[{qid}] {status:9s} {question}\n          got: {shown or '(no rows)'}" + (f"\n          error: {err}" if err else ""))
    if status == "FAIL":
        print(f"          expected: {', '.join(expect) or '(no rows)'}")

try:
    from pyshacl import validate
    ok, _, report = validate(g, shacl_graph=str(ROOT / "stripping_loop" / "shapes.ttl"), inference="rdfs")
    print("\nSHACL validation:", "PASS" if ok else "FAIL")
    if not ok:
        failures += 1
        print(report)
except ImportError:
    print("\npyshacl not installed, skipping SHACL validation")

print(f"\n{len(Q)} questions, {failures} failure(s)")
sys.exit(1 if failures else 0)
