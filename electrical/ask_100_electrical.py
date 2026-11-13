"""
Ask the electrical KG (piece 15) questions whose expected answers come from the cable diagrams C2286-CD-001:
what feeds what, motor ratings, and what is lost if a panel or supply fails. Runs on the full plant.
Run from the repo root (after ccpp/build_full_plant.py):   python electrical/ask_100_electrical.py
Output: electrical/hundred_results_electrical.md
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
def OUT(s, p): return f"SELECT ?t WHERE {{ {T(s)} {T(p)} ?x . ?x ccpp:tag ?t }}"
def DIRECT(a, p, b): return f"ASK {{ {T(a)} {T(p)} {T(b)} }}"
def PATH(a, p, b): return f"ASK {{ {T(a)} {T(p)}+ {T(b)} }}"
def VAL(s, p): return f"SELECT ?v WHERE {{ {T(s)} {T(p)} ?v }}"
def LIM(l, which): return f"SELECT ?v WHERE {{ {T('limit_' + l)} {T(which + 'Value')} ?v }}"
def CONTAINS(s, p, text): return f"ASK {{ {T(s)} {T(p)} ?v . FILTER(CONTAINS(STR(?v), \"{text}\")) }}"
def WHO(p, x): return f"SELECT DISTINCT ?t WHERE {{ ?s {T(p)} {T(x)} ; ccpp:tag ?t }}"
def FEEDS(x): return f"SELECT DISTINCT ?t WHERE {{ {T(x)} ccpp:powers+ ?y . ?y ccpp:tag ?t }}"
def FEDBY(x): return f"SELECT DISTINCT ?t WHERE {{ ?y ccpp:powers+ {T(x)} . ?y ccpp:tag ?t }}"
def CLSP(c, prefix): return (f"SELECT DISTINCT ?t WHERE {{ ?x a/rdfs:subClassOf* {T(c)} ; ccpp:tag ?t ; ccpp:citedIn ?c . "
                             f"FILTER(CONTAINS(STR(?c), \"__{prefix}cit\")) }}")
def CNTOI(prefix): return f"SELECT (COUNT(?o) AS ?n) WHERE {{ ?o a ccpp:OpenItem ; ccpp:foundBy \"{prefix} section build, Oct 2026\" }}"


P = "ele"
Q = [
 ("R01","Register","Which motors does the cable diagram show?", CLSP("Motor",P), ["M100", "M101A", "M101B", "M102", "M103", "M104", "M105", "M300"]),
 ("R02","Register","Which supplies does the cable diagram show?", CLSP("PowerSupply",P), ["EL_230V_L1", "EL_230V_L2", "EL_230V_L3", "EL_415V"]),
 ("R03","Register","Which panels does the cable diagram show?", CLSP("ElectricalPanel",P), ["CA1", "CS1", "DB301", "DB302", "DB303", "FB1", "MC1", "PP2", "PP4", "RC2", "RC3", "RC4", "UPS1", "UPS2", "UPS3"]),
 ("R04","Register","How many open items does this piece raise?", CNTOI(P), ["5"]),
 ("P01","Power walk","What is lost if the motor control panel MC1 loses power?", FEEDS("MC1"), ["H200a", "H200b", "J100", "J101a", "J101b", "J102", "J103", "J104", "J105", "J300", "M100", "M101A", "M101B", "M102", "M103", "M104", "M105", "M300"]),
 ("P02","Power walk","What does distribution board DB303 feed?", FEEDS("DB303"), ["CA1"]),
 ("P03","Power walk","What is lost if UPS1 fails (its board DB301 and everything downstream)?", FEEDS("UPS1"), ["AT100", "AT300", "CS1", "DB301", "FB1", "FT102", "FT103", "FT201", "FT302", "FT304", "FT305", "PP2", "PP4", "RC2", "RC3", "RC4"]),
 ("P04","Power walk","Which instruments take 110 V from the fieldbus panel FB1?", FEEDS("FB1"), ["AT100", "AT300", "FT102", "FT103", "FT201", "FT302", "FT304", "FT305"]),
 ("P05","Power walk","What feeds the CO2 compressor J103, back to the supply?", FEDBY("J103"), ["EL_415V", "M103", "MC1"]),
 ("P06","Power walk","What feeds FT201, back to the supplies?", FEDBY("FT201"), ["DB301", "DB302", "EL_230V_L1", "EL_230V_L2", "FB1", "UPS1", "UPS2"]),
 ("P07","Power walk","Does the 230 V supply L1 reach FT201?", PATH("EL_230V_L1","powers","FT201"), ["true"]),
 ("P08","Power walk","Does the 415 V supply reach FT201 (it should not)?", PATH("EL_415V","powers","FT201"), ["false"]),
 ("P09","Power walk","Does UPS3 feed the control system panel CS1 (it should not)?", PATH("UPS3","powers","CS1"), ["false"]),
 ("P10","Power walk","Is the control system panel CS1 fed from both DB301 and DB302?", ALL(("DB301","powers","CS1"),("DB302","powers","CS1")), ["true"]),
 ("P11","Power walk","Does the 415 V supply reach both heaters?", ALL(("MC1","powers","H200a"),("MC1","powers","H200b")), ["true"]),
 ("M01","Motors","What is the rated power of M100 (J100)?", VAL("M100","ratedPowerText"), ["2.2 kW"]),
 ("M02","Motors","What is the rated power of M101A (J101a)?", VAL("M101A","ratedPowerText"), ["2.2 kW"]),
 ("M03","Motors","What is the rated power of M101B (J101b)?", VAL("M101B","ratedPowerText"), ["2.2 kW"]),
 ("M04","Motors","What is the rated power of M102 (J102)?", VAL("M102","ratedPowerText"), ["3 kW"]),
 ("M05","Motors","What is the rated power of M103 (J103)?", VAL("M103","ratedPowerText"), ["4 kW"]),
 ("M06","Motors","What is the rated power of M104 (J104)?", VAL("M104","ratedPowerText"), ["0.55 kW"]),
 ("M07","Motors","What is the rated power of M105 (J105)?", VAL("M105","ratedPowerText"), ["0.55 kW"]),
 ("M08","Motors","What is the rated power of M300 (J300)?", VAL("M300","ratedPowerText"), ["0.37 kW"]),
 ("M09","Motors","Which machine does M103 drive?", OUT("M103","drives"), ["J103"]),
 ("M10","Motors","Which machine does M300 drive?", OUT("M300","drives"), ["J300"]),
 ("N01","Numbers","J102 motor rating (kW)?", LIM("M102_rated_power","high"), ["3"]),
 ("N02","Numbers","J103 motor rating (kW)?", LIM("M103_rated_power","high"), ["4"]),
 ("N03","Numbers","H200a rating (kW)?", LIM("H200a_rated_power","high"), ["9"]),
 ("N04","Numbers","J300 motor rating (kW)?", LIM("M300_rated_power","high"), ["0.37"]),
 ("F01","Floors","Which floor is the motor control panel on?", VAL("MC1","floor"), ["1"]),
 ("F02","Floors","Which floor is remote I/O panel RC4 on?", VAL("RC4","floor"), ["4"]),
 ("F03","Floors","Which floor is the J300 motor on?", VAL("M300","floor"), ["2"]),
 ("F04","Floors","Which floor is remote I/O panel RC2 on?", VAL("RC2","floor"), ["2"]),
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
lines = ["# Electrical KG: question run", "", f"PASS {count['PASS']}, FAIL {count['FAIL']}, QUERY ERROR {count['QUERY ERROR']}", ""]
for qid, cat, question, expect, rows, status, err in results:
    lines += [f"## {qid} [{cat}] {status}", "", f"**{question}**", "", f"- Expected: {', '.join(expect)}"]
    lines += [f"- Error: {err}"] if err else [f"- KG: {', '.join(r[0] for r in rows) or '(no rows)'}"]
    lines.append("")
(HERE / "hundred_results_electrical.md").write_text("\n".join(lines))
for qid, cat, question, expect, rows, status, err in results:
    if status != "PASS":
        print(f"[{qid}] {status} {question}\n      expected: {expect}\n      got: {[r[0] for r in rows]} {err or ''}")
print(f"\nPASS {count['PASS']}, FAIL {count['FAIL']}, QUERY ERROR {count['QUERY ERROR']}  (details in electrical/hundred_results_electrical.md)")
sys.exit(1 if count["FAIL"] or count["QUERY ERROR"] else 0)
