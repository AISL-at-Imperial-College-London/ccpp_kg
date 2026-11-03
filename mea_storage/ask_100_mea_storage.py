"""
Ask the MEA storage, filling and draining KG (piece 9) 100 questions whose expected answers come from the
documents (the team then traces and checks it on the P&ID), not from the KG. Piece 9 links to items in other
sections, so the questions run on the joined full plant.
Run from the repo root (after ccpp/build_full_plant.py):   python mea_storage/ask_100_mea_storage.py
Output: mea_storage/hundred_results_mea_storage.md
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
def INN(p, o, cls=None):
    c = f" ?x a/rdfs:subClassOf* {T(cls)} ." if cls else ""
    return f"SELECT ?t WHERE {{ ?x {T(p)} {T(o)} ; ccpp:tag ?t .{c} }}"
def PATH(a, p, b): return f"ASK {{ {T(a)} {T(p)}+ {T(b)} }}"
def DIRECT(a, p, b): return f"ASK {{ {T(a)} {T(p)} {T(b)} }}"
def CLS(c): return f"SELECT ?t WHERE {{ ?x a/rdfs:subClassOf* {T(c)} ; ccpp:tag ?t }}"
def VAL(s, p): return f"SELECT ?v WHERE {{ {T(s)} {T(p)} ?v }}"
def LIM(l, which): return f"SELECT ?v WHERE {{ {T('limit_' + l)} {T(which + 'Value')} ?v }}"
def ALARM(t): return f"SELECT ?l WHERE {{ ?x ccpp:appliesTo {T(t)} ; ccpp:limitType \"alarm\" ; rdfs:label ?l }}"
def DISC(t): return f"SELECT ?d WHERE {{ ?d a ccpp:PIDDiscrepancy ; ccpp:concerns {T(t)} }}"
def COV(t): return f"SELECT ?el WHERE {{ ?e a ccpp:HazopElement ; ccpp:covers {T(t)} ; ccpp:elementNumber ?el }}"
def HDEV(t): return f"SELECT ?d WHERE {{ ?d a ccpp:HazopDeviation ; ccpp:concerns {T(t)} }}"
def CONTAINS(s, p, text): return f"ASK {{ {T(s)} {T(p)} ?v . FILTER(CONTAINS(STR(?v), \"{text}\")) }}"
def HMTASK(eq, prop, op, v): return (f"ASK {{ ?p ccpp:ofEquipment {T(eq)} ; ccpp:inCase ?c ; {T(prop)} ?x . "
                                     f"?c ccpp:recommendedForUse true . FILTER(?x {op} {v}) }}")
def INSTEP(loop, item): return f"ASK {{ {T(loop)} ccpp:hasStep/ccpp:stepItem {T(item)} }}"
def OIA(t): return f"SELECT ?o WHERE {{ ?o a ccpp:OpenItem ; ccpp:about {T(t)} }}"
def CLSP(c, prefix): return (f"SELECT DISTINCT ?t WHERE {{ ?x a/rdfs:subClassOf* {T(c)} ; ccpp:tag ?t ; ccpp:citedIn ?c . "
                             f"FILTER(CONTAINS(STR(?c), \"__{prefix}cit\")) }}")
def CNTOI(prefix): return f"SELECT (COUNT(?o) AS ?n) WHERE {{ ?o a ccpp:OpenItem ; ccpp:foundBy \"{prefix} section build, Oct 2026\" }}"


P = "mea"
L = "MEAFillRoute"
Q = [
 ("F01","Filling","What does the feed tank F100 feed?", OUT("F100","feedsInto"), ["J105"]),
 ("F02","Filling","What does J105 pump into?", OUT("J105","feedsInto"), ["FILL_DRAIN_HEADER"]),
 ("F03","Filling","Does MEA from F100 reach the fill/drain header?", PATH("F100","feedsInto","FILL_DRAIN_HEADER"), ["true"]),
 ("F04","Filling","Does the filling route leak into the normal E100 flow path (it must not)?", PATH("F100","feedsInto","E100"), ["false"]),
 ("F05","Filling","Does normal running flow into the receiver tank (it must not)?", PATH("E100","feedsInto","R100"), ["false"]),
 ("F06","Filling","Does the filling route include TT116?", INSTEP(L,"TT116"), ["true"]),
 ("F07","Filling","Does the filling route include PCV126?", INSTEP(L,"PCV126"), ["true"]),
 ("F08","Filling","Does the filling route include the V138 manual vent?", INSTEP(L,"V138"), ["true"]),
 ("F09","Filling","Does F100 feed the header directly (skipping J105)?", DIRECT("F100","feedsInto","FILL_DRAIN_HEADER"), ["false"]),
 ("F10","Filling","Is the filling route in the Filling operating mode?", VAL(L,"inMode"), ["Filling"]),
 ("P01","Piping","Is the header piped back to the receiver tank R100?", DIRECT("FILL_DRAIN_HEADER","pipedTo","R100"), ["true"]),
 ("P02","Piping","Is the header piped to V115 and V122 at J100 (HAZOP M14)?", ALL(("FILL_DRAIN_HEADER","pipedTo","V115"),("FILL_DRAIN_HEADER","pipedTo","V122")), ["true"]),
 ("P03","Piping","Do the J101 fill/drain valves V146a/b and V147a/b connect to the header?", ALL(("V146a","pipedTo","FILL_DRAIN_HEADER"),("V146b","pipedTo","FILL_DRAIN_HEADER"),("V147a","pipedTo","FILL_DRAIN_HEADER"),("V147b","pipedTo","FILL_DRAIN_HEADER")), ["true"]),
 ("P04","Piping","Do the drains V153, V154 and V155 drop to the header?", ALL(("V153","pipedTo","FILL_DRAIN_HEADER"),("V154","pipedTo","FILL_DRAIN_HEADER"),("V155","pipedTo","FILL_DRAIN_HEADER")), ["true"]),
 ("P05","Piping","Do V160, V167 and V168 drop to the header?", ALL(("V160","pipedTo","FILL_DRAIN_HEADER"),("V167","pipedTo","FILL_DRAIN_HEADER"),("V168","pipedTo","FILL_DRAIN_HEADER")), ["true"]),
 ("P06","Piping","Do V148 and V149 drop to the header?", ALL(("V148","pipedTo","FILL_DRAIN_HEADER"),("V149","pipedTo","FILL_DRAIN_HEADER")), ["true"]),
 ("P07","Piping","Does the K101 bottom outlet V126 run to the header (team trace)?", DIRECT("V126","pipedTo","FILL_DRAIN_HEADER"), ["true"]),
 ("P08","Piping","Can K101 reach the header through V126?", PATH("K101","pipedTo","FILL_DRAIN_HEADER"), ["true"]),
 ("E01","Equipment","Which storage tanks are there?", CLSP("StorageTank",P), ["F100","R100"]),
 ("E02","Equipment","Which pump does this piece add?", CLSP("Pump",P), ["J105"]),
 ("E03","Equipment","Which pressure control valve does this piece add?", CLSP("PressureControlValve",P), ["PCV126"]),
 ("E04","Equipment","Which check valves does this piece add?", CLSP("CheckValve",P), ["NRV107","NRV108"]),
 ("E05","Equipment","What grid is J105 at?", VAL("J105","gridReference"), ["N4"]),
 ("E06","Equipment","Which floor is J105 on?", VAL("J105","floor"), ["1"]),
 ("E07","Equipment","What grid is the feed tank F100 at (as built)?", VAL("F100","gridReference"), ["N2"]),
 ("E08","Equipment","What grid is the receiver tank R100 at (as built)?", VAL("R100","gridReference"), ["N3"]),
 ("E09","Equipment","Does the F100 note say it is the feed tank?", CONTAINS("F100","note","Feed tank"), ["true"]),
 ("E10","Equipment","Does the R100 note say it is the receiver tank?", CONTAINS("R100","note","Receiver tank"), ["true"]),
 ("V01","Valves","What grid is PCV126 at?", VAL("PCV126","gridReference"), ["N5"]),
 ("V02","Valves","What grid is V156 at?", VAL("V156","gridReference"), ["N6"]),
 ("V03","Valves","Is V156 normally closed?", VAL("V156","normalPosition"), ["closed"]),
 ("V04","Valves","What grid is V157 at?", VAL("V157","gridReference"), ["N5"]),
 ("V05","Valves","What grid is V158 at?", VAL("V158","gridReference"), ["O4"]),
 ("V06","Valves","What grid is V159a at?", VAL("V159a","gridReference"), ["O3"]),
 ("V07","Valves","What grid is V159b at?", VAL("V159b","gridReference"), ["O2"]),
 ("V08","Valves","What grid is V161a at?", VAL("V161a","gridReference"), ["O3"]),
 ("V09","Valves","What grid is V161b at?", VAL("V161b","gridReference"), ["O2"]),
 ("V10","Valves","What grid is V162 at?", VAL("V162","gridReference"), ["N2"]),
 ("V11","Valves","What grid is V163 at?", VAL("V163","gridReference"), ["O3"]),
 ("V12","Valves","What grid is V164 at?", VAL("V164","gridReference"), ["N3"]),
 ("V13","Valves","What grid is V199 at?", VAL("V199","gridReference"), ["O4"]),
 ("V14","Valves","What grid is V153 at?", VAL("V153","gridReference"), ["O8"]),
 ("V15","Valves","Is V153 normally closed?", VAL("V153","normalPosition"), ["closed"]),
 ("V16","Valves","What grid is V155 at?", VAL("V155","gridReference"), ["O7"]),
 ("V17","Valves","What grid is V167 at?", VAL("V167","gridReference"), ["N9"]),
 ("V18","Valves","What grid is V149 at?", VAL("V149","gridReference"), ["O12"]),
 ("V19","Valves","What grid is V148 at?", VAL("V148","gridReference"), ["O13"]),
 ("V20","Valves","What grid is V146a at?", VAL("V146a","gridReference"), ["O15"]),
 ("V21","Valves","What grid is V147b at?", VAL("V147b","gridReference"), ["O16"]),
 ("V22","Valves","What grid is NRV107 at?", VAL("NRV107","gridReference"), ["N2"]),
 ("V23","Valves","What grid is NRV108 at?", VAL("NRV108","gridReference"), ["N3"]),
 ("V24","Valves","What kind of valve is V138?", VAL("V138","valveType"), ["manual vent"]),
 ("V25","Valves","What grid is V168 at?", VAL("V168","gridReference"), ["N9"]),
 ("I01","Instruments","What type of sensor is TT116?", VAL("TT116","sensorType"), ["PRT"]),
 ("I02","Instruments","What signal does TT116 use?", VAL("TT116","signalType"), ["4-20mA"]),
 ("I03","Instruments","What grid is TT116 at?", VAL("TT116","gridReference"), ["N5"]),
 ("I04","Instruments","What does TT116 monitor?", OUT("TT116","monitors"), ["J105"]),
 ("I05","Instruments","Do FI110 and PI112 sit at the tank at N2 (F100)?", ALL(("FI110","monitors","F100"),("PI112","monitors","F100")), ["true"]),
 ("I06","Instruments","Do FI111 and PI113 sit at the tank at N3 (R100)?", ALL(("FI111","monitors","R100"),("PI113","monitors","R100")), ["true"]),
 ("I07","Instruments","What grid is FI110 at?", VAL("FI110","gridReference"), ["N2"]),
 ("I08","Instruments","What grid is FI111 at?", VAL("FI111","gridReference"), ["M3"]),
 ("I09","Instruments","What grid is PI112 at?", VAL("PI112","gridReference"), ["N2"]),
 ("I10","Instruments","What grid is PI113 at?", VAL("PI113","gridReference"), ["M3"]),
 ("L01","Trips","What kind of limit is on the receiver tank level?", VAL("limit_TRIP_R100_high_level","limitType"), ["trip"]),
 ("L02","Trips","Does the receiver tank have a high-level trip (HAZOP M16)?", ALL(("limit_TRIP_R100_high_level","appliesTo","R100")), ["true"]),
 ("L03","Trips","Does the feed tank have a low-level trip (HAZOP M17)?", ALL(("limit_TRIP_F100_low_level","appliesTo","F100")), ["true"]),
 ("L04","Trips","Does J105 have a thermal trip (HAZOP 9b.1)?", ALL(("limit_TRIP_J105_thermal","appliesTo","J105")), ["true"]),
 ("L05","Trips","Is J105 stopped by liquid at the V138 vent (HAZOP 9a.7)?", ALL(("limit_TRIP_J105_liquid_at_vent","appliesTo","J105")), ["true"]),
 ("L06","Trips","Is J105 protected against running dry (HAZOP 9a.3)?", ALL(("limit_TRIP_J105_dry_run","appliesTo","J105")), ["true"]),
 ("D01","Discrepancies","Which discrepancy concerns R100?", DISC("R100"), ["discrepancy_R100_F100_labels"]),
 ("D02","Discrepancies","Which discrepancy concerns F100?", DISC("F100"), ["discrepancy_R100_F100_labels"]),
 ("D03","Discrepancies","What is the as-built situation for the tank labels?", VAL("discrepancy_R100_F100_labels","asBuilt"), ["Labels swapped (F100 at N2, R100 at N3)"]),
 ("H01","HAZOP","Does HAZOP element 9a cover J105?", ALL(("HAZOP_element_9a","covers","J105")), ["true"]),
 ("H02","HAZOP","Does HAZOP element 9b cover R100?", ALL(("HAZOP_element_9b","covers","R100")), ["true"]),
 ("H03","HAZOP","Does HAZOP element 9b cover V146a and V147a?", ALL(("HAZOP_element_9b","covers","V146a"),("HAZOP_element_9b","covers","V147a")), ["true"]),
 ("H04","HAZOP","Does HAZOP 9a.1 concern J105?", ALL(("HAZOP_9a_01","concerns","J105")), ["true"]),
 ("H05","HAZOP","Do HAZOP 9a.7 and 9b.4 concern V138?", ALL(("HAZOP_9a_07","concerns","V138"),("HAZOP_9b_04","concerns","V138")), ["true"]),
 ("H06","HAZOP","Does HAZOP 9b.4 concern V147a and V146a (V147/V146 in 2010)?", ALL(("HAZOP_9b_04","concerns","V147a"),("HAZOP_9b_04","concerns","V146a")), ["true"]),
 ("H07","HAZOP","Was an RV spillback added round J105 (HAZOP 9a.1)?", CONTAINS("HAZOP_9a_01","actionTaken","RV added"), ["true"]),
 ("H08","HAZOP","Were check valves included after the pump (HAZOP 9a.6)?", CONTAINS("HAZOP_9a_06","actionTaken","CVs included"), ["true"]),
 ("H09","HAZOP","Does HAZOP 9b.5 warn that wrong valving might fill E100/E101 instead of emptying?", CONTAINS("HAZOP_9b_05","consequence","fill E100/E101"), ["true"]),
 ("H10","HAZOP","Does HAZOP 9b.5 concern E100 and E101?", ALL(("HAZOP_9b_05","concerns","E100"),("HAZOP_9b_05","concerns","E101")), ["true"]),
 ("H12","HAZOP","Does HAZOP 9a.3 say the pump runs dry if the tank is empty?", CONTAINS("HAZOP_9a_03","consequence","Pump runs dry"), ["true"]),
 ("H11","HAZOP","Is HAZOP item 9a.11 (wrong tank attached to J105) in element 9a?", ALL(("HAZOP_9a_11","inElement","HAZOP_element_9a")), ["true"]),
 ("O01","Open items","Which open item asks which tank is which?", OIA("R100"), ["MS01","MS06","MS09"]),
 ("O02","Open items","Which open item concerns PCV126?", OIA("PCV126"), ["MS04"]),
 ("O03","Open items","Which open item concerns V138?", OIA("V138"), ["MS05"]),
 ("O04","Open items","Which open item flags RV107 (J105 spillback or steam relief)?", ALL(("MS03","about","J105")), ["true"]),
 ("O05","Open items","How many open items does this piece hold?", CNTOI(P), ["9"]),
 ("O06","Open items","Are MS07 and MS08 about the fill/drain header?", ALL(("MS07","about","FILL_DRAIN_HEADER"),("MS08","about","FILL_DRAIN_HEADER")), ["true"]),
 ("X01","Join","Is V122 (stripping loop) now piped from the fill/drain header?", DIRECT("FILL_DRAIN_HEADER","pipedTo","V122"), ["true"]),
 ("X02","Join","Is V126 (piece 5) still on the K101 bottom?", DIRECT("K101","pipedTo","V126"), ["true"]),
 ("X03","Join","Does the normal figure-of-eight still connect E100 to E101 (unchanged)?", PATH("E100","feedsInto","E101"), ["true"]),
 ("X04","Join","Does the K101 water loop still go through Z103 to J104?", ALL(("K101","pipedTo","Z103"),("Z103","pipedTo","J104")), ["true"]),
 ("X05","Join","Is J105 the only pump this piece adds?", CLSP("Pump",P), ["J105"]),
 ("X06","Join","Is the filling mode a declared operating mode?", ALL(("MEAFillRoute","inMode","Filling")), ["true"]),
 ("X07","Join","Do the drains from three or more areas share the header (O8, O12, O19)?", ALL(("V153","pipedTo","FILL_DRAIN_HEADER"),("V149","pipedTo","FILL_DRAIN_HEADER"),("V126","pipedTo","FILL_DRAIN_HEADER")), ["true"]),
 ("X08","Join","Is the header a pipe segment (not equipment)?", CLSP("PipeSegment",P), ["FILL_DRAIN_HEADER"]),
 ("X09","Join","Does V160 (shared with an earlier section) drop to the header?", DIRECT("V160","pipedTo","FILL_DRAIN_HEADER"), ["true"]),
 ("X10","Join","Can the receiver tank reach the feed tank (it must not, without a transfer line)?", PATH("R100","feedsInto","F100"), ["false"]),
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
lines = ["# MEA storage KG: 100-question run", "", f"PASS {count['PASS']}, FAIL {count['FAIL']}, QUERY ERROR {count['QUERY ERROR']}", ""]
for qid, cat, question, expect, rows, status, err in results:
    lines += [f"## {qid} [{cat}] {status}", "", f"**{question}**", "", f"- Expected: {', '.join(expect)}"]
    lines += [f"- Error: {err}"] if err else [f"- KG: {', '.join(r[0] for r in rows) or '(no rows)'}"]
    lines.append("")
(HERE / "hundred_results_mea_storage.md").write_text("\n".join(lines))
for qid, cat, question, expect, rows, status, err in results:
    if status != "PASS":
        print(f"[{qid}] {status} {question}\n      expected: {expect}\n      got: {[r[0] for r in rows]} {err or ''}")
print(f"\nPASS {count['PASS']}, FAIL {count['FAIL']}, QUERY ERROR {count['QUERY ERROR']}  (details in mea_storage/hundred_results_mea_storage.md)")
sys.exit(1 if count["FAIL"] or count["QUERY ERROR"] else 0)
