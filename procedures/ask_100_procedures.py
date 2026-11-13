"""
Ask the procedures and alarm responses KG (piece 12) questions whose expected answers come from the report and
HAZOP, not from the KG. Runs on the joined full plant.
Run from the repo root (after ccpp/build_full_plant.py):   python procedures/ask_100_procedures.py
Output: procedures/hundred_results_procedures.md
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
def LIM(l, which): return f"SELECT ?v WHERE {{ {T('limit_' + l)} {T(which + 'Value')} ?v }}"
def CONTAINS(s, p, text): return f"ASK {{ {T(s)} {T(p)} ?v . FILTER(CONTAINS(STR(?v), \"{text}\")) }}"
def CLSP(c, prefix): return (f"SELECT DISTINCT ?t WHERE {{ ?x a/rdfs:subClassOf* {T(c)} ; ccpp:tag ?t ; ccpp:citedIn ?c . "
                             f"FILTER(CONTAINS(STR(?c), \"__{prefix}cit\")) }}")
def CNTOI(prefix): return f"SELECT (COUNT(?o) AS ?n) WHERE {{ ?o a ccpp:OpenItem ; ccpp:foundBy \"{prefix} section build, Oct 2026\" }}"


P = "prc"
Q = [
 ("R01","Register","Which alarm responses does the KG hold?", CLSP("AlarmResponse",P),
  ["ARP_LT101_L","ARP_LT101_H","ARP_LT104_L","ARP_LT104_H","ARP_LT108_L","ARP_LT108_H","ARP_LT401_L","ARP_LT401_H","ARP_H200_HH","ARP_E100_PSH","COM_LT101_LOW","COM_LT101_HIGH"]),
 ("R02","Register","Which operating envelope does the KG hold?", CLSP("OperatingEnvelope",P), ["ENV_J100"]),
 ("L01","Thresholds","At what level does the LT101 L alarm sound?", LIM("F84_LT101_L","low"), ["5"]),
 ("L02","Thresholds","At what level does the LT101 LL trip (emergency shutdown) act?", LIM("F84_LT101_LL","low"), ["1"]),
 ("L03","Thresholds","At what level does the LT101 H alarm sound?", LIM("F84_LT101_H","high"), ["85"]),
 ("L04","Thresholds","At what level does the LT101 HH trip act?", LIM("F84_LT101_HH","high"), ["95"]),
 ("L05","Thresholds","At what level does the LT108 L alarm sound?", LIM("F84_LT108_L","low"), ["5"]),
 ("L06","Thresholds","At what level does the LT108 H alarm sound?", LIM("F84_LT108_H","high"), ["85"]),
 ("L07","Thresholds","At what level does the LT401 L alarm sound?", LIM("F84_LT401_L","low"), ["5"]),
 ("L08","Thresholds","At what level does the LT401 H alarm sound?", LIM("F84_LT401_H","high"), ["85"]),
 ("L09","Thresholds","At what level does the LT104 (K101) L alarm sound?", LIM("F84_LT104_L","low"), ["5"]),
 ("L10","Thresholds","At what level does the LT104 H alarm sound?", LIM("F84_LT104_H","high"), ["85"]),
 ("L11","Thresholds","What is the lower commissioning limit on LT101?", LIM("COM_LT101_10","low"), ["10"]),
 ("L12","Thresholds","What is the upper commissioning limit on LT101?", LIM("COM_LT101_10","high"), ["90"]),
 ("L13","Thresholds","At what pressure does the E100 PSH shut the plant down?", LIM("PSH_E100_2barg","high"), ["2"]),
 ("L14","Thresholds","In what unit is the E100 PSH set?", VAL("limit_PSH_E100_2barg","unit"), ["barg"]),
 ("L15","Thresholds","What kind of limit is the E100 PSH?", VAL("limit_PSH_E100_2barg","limitType"), ["trip"]),
 ("L16","Thresholds","What is J100's upper safe pump power, allowing for cavitation?", LIM("J100_range_cavitation","high"), ["57"]),
 ("L17","Thresholds","What is J100's theoretical upper safe pump power?", LIM("J100_range_theoretical","high"), ["60"]),
 ("L18","Thresholds","What is J100's lower pump power limit?", LIM("J100_range_cavitation","low"), ["1"]),
 ("L19","Thresholds","Is there a PSH on E101 (HAZOP 10.8)?", ALL(("limit_PSH_E101","appliesTo","E101")), ["true"]),
 ("T01","Triggers","Which instrument triggers the E100 level alarm responses?", ALL(("ARP_LT101_L","triggeredBy","LT101"),("ARP_LT101_H","triggeredBy","LT101")), ["true"]),
 ("T02","Triggers","Which instrument triggers the E101 level alarm responses?", ALL(("ARP_LT108_L","triggeredBy","LT108"),("ARP_LT108_H","triggeredBy","LT108")), ["true"]),
 ("T03","Triggers","Which instrument triggers the condensate level responses?", ALL(("ARP_LT401_L","triggeredBy","LT401"),("ARP_LT401_H","triggeredBy","LT401")), ["true"]),
 ("T04","Triggers","Which instrument triggers the K101 level responses?", ALL(("ARP_LT104_L","triggeredBy","LT104"),("ARP_LT104_H","triggeredBy","LT104")), ["true"]),
 ("T05","Triggers","Which controllers trigger the heater alarm response?", ALL(("ARP_H200_HH","triggeredBy","TIC213a"),("ARP_H200_HH","triggeredBy","TIC213b")), ["true"]),
 ("T06","Triggers","Does the LT101 low response answer both the L (5%) and LL (1%) limits?", ALL(("ARP_LT101_L","respondsTo","limit_F84_LT101_L"),("ARP_LT101_L","respondsTo","limit_F84_LT101_LL")), ["true"]),
 ("T07","Triggers","Does the E100 shutdown response answer the 2 barg PSH?", ALL(("ARP_E100_PSH","respondsTo","limit_PSH_E100_2barg")), ["true"]),
 ("A01","Actions","LT101 below 5%: is J100 reduced by 10% first?", CONTAINS("ARP_LT101_L","actionText","1. Reduce the pump power of J100 by 10%"), ["true"]),
 ("A02","Actions","LT101 below 5%: is J300 increased by 10%?", CONTAINS("ARP_LT101_L","actionText","Increase the pump power of J300 by 10%"), ["true"]),
 ("A03","Actions","LT101 below 1%: is emergency shutdown initiated?", CONTAINS("ARP_LT101_L","actionText","below 1%), initiate emergency shutdown"), ["true"]),
 ("A04","Actions","LT101 above 85%: is J100 increased by 10% first?", CONTAINS("ARP_LT101_H","actionText","1. Increase the pump power of J100 by 10%"), ["true"]),
 ("A05","Actions","LT101 above 95%: is emergency shutdown initiated?", CONTAINS("ARP_LT101_H","actionText","above 95%), initiate emergency shutdown"), ["true"]),
 ("A06","Actions","LT108 below 5%: is the running J101 pump decreased first?", CONTAINS("ARP_LT108_L","actionText","1. Decrease the pump power of J101a or J101b"), ["true"]),
 ("A07","Actions","LT108 above 85%: is J300 decreased by 10%?", CONTAINS("ARP_LT108_H","actionText","Decrease the pump power of J300 by 10%"), ["true"]),
 ("A08","Actions","LT401 below 5%: is J300 decreased by 10%?", CONTAINS("ARP_LT401_L","actionText","Decrease the pump power of J300 by 10%"), ["true"]),
 ("A09","Actions","LT401 above 85%: is J300 increased by 10%?", CONTAINS("ARP_LT401_H","actionText","Increase the pump power of J300 by 10%"), ["true"]),
 ("A10","Actions","LT104 below 5%: is J103 increased by 5%?", CONTAINS("ARP_LT104_L","actionText","Increase the pump power of J103 by 5%"), ["true"]),
 ("A11","Actions","Heaters not responding: are they switched off at the manual switch on floor 1?", CONTAINS("ARP_H200_HH","actionText","manual switch on floor 1"), ["true"]),
 ("A12","Actions","Does the E100 PSH kill the steam and electrical heating?", CONTAINS("ARP_E100_PSH","actionText","kills the steam and electrical heating"), ["true"]),
 ("A13","Actions","Commissioning, LT101 above 90%: is V110 checked if the level will not drop?", CONTAINS("COM_LT101_HIGH","actionText","check V110 is open"), ["true"]),
 ("A14","Actions","Do the LT101 responses act on J100, J101a, J101b and J300?", ALL(("ARP_LT101_L","actsOn","J100"),("ARP_LT101_L","actsOn","J101a"),("ARP_LT101_L","actsOn","J101b"),("ARP_LT101_L","actsOn","J300")), ["true"]),
 ("A15","Actions","Does the E100 PSH act on H100 and both electric heaters?", ALL(("ARP_E100_PSH","actsOn","H100"),("ARP_E100_PSH","actsOn","H200a"),("ARP_E100_PSH","actsOn","H200b")), ["true"]),
 ("E01","Envelope","Does the J100 envelope give 1%-57%?", CONTAINS("ENV_J100","envelopeText","1%-57%"), ["true"]),
 ("E02","Envelope","Does the J100 envelope mention cavitation?", CONTAINS("ENV_J100","envelopeText","cavitation"), ["true"]),
 ("E03","Envelope","Is the envelope linked to J100?", ALL(("ENV_J100","envelopeOf","J100")), ["true"]),
 ("X01","Join","Does LT401 now monitor both K401 and C400?", ALL(("LT401","monitors","K401"),("LT401","monitors","C400")), ["true"]),
 ("X02","Join","Is the commissioning response marked as not for full operation?", CONTAINS("COM_LT101_LOW","note","not full operation"), ["true"]),
 ("O01","Open items","How many open items does this piece raise?", CNTOI(P), ["2"]),
 ("O02","Open items","Is PR01 about the missing LL/HH values for LT108?", ALL(("PR01","about","LT108")), ["true"]),
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
lines = ["# Procedures KG: question run", "", f"PASS {count['PASS']}, FAIL {count['FAIL']}, QUERY ERROR {count['QUERY ERROR']}", ""]
for qid, cat, question, expect, rows, status, err in results:
    lines += [f"## {qid} [{cat}] {status}", "", f"**{question}**", "", f"- Expected: {', '.join(expect)}"]
    lines += [f"- Error: {err}"] if err else [f"- KG: {', '.join(r[0] for r in rows) or '(no rows)'}"]
    lines.append("")
(HERE / "hundred_results_procedures.md").write_text("\n".join(lines))
for qid, cat, question, expect, rows, status, err in results:
    if status != "PASS":
        print(f"[{qid}] {status} {question}\n      expected: {expect}\n      got: {[r[0] for r in rows]} {err or ''}")
print(f"\nPASS {count['PASS']}, FAIL {count['FAIL']}, QUERY ERROR {count['QUERY ERROR']}  (details in procedures/hundred_results_procedures.md)")
sys.exit(1 if count["FAIL"] or count["QUERY ERROR"] else 0)