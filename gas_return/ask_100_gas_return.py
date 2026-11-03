"""
Ask the gas returns KG (piece 7) 100 questions whose expected answers come from the
documents (the team then traces and checks it on the P&ID), not from the KG. Piece 7 links to items in other
sections, so the questions run on the joined full plant.
Run from the repo root (after ccpp/build_full_plant.py):   python gas_return/ask_100_gas_return.py
Output: gas_return/hundred_results_gas_return.md
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


P = "grt"
L = "N2ReturnLoop"
Q = [
 ("F01","N2 return","Where does the N2 go after leaving K402 for the return line?", OUT("K402_N_gas_to_return","feedsInto"), ["FT303"]),
 ("F02","N2 return","What does FT303 feed?", OUT("FT303","feedsInto"), ["FT304"]),
 ("F03","N2 return","What does FT304 feed?", OUT("FT304","feedsInto"), ["K102"]),
 ("F04","N2 return","What does K102 feed?", OUT("K102","feedsInto"), ["J102"]),
 ("F05","N2 return","What does J102 blow the N2 into?", OUT("J102","feedsInto"), ["K101"]),
 ("F06","N2 return","What feeds K102 on the return line?", INN("feedsInto","K102"), ["FT304"]),
 ("F07","N2 return","Does the returned N2 get back into E101?", PATH("J102","feedsInto","E101"), ["true"]),
 ("F08","N2 return","Is the N2 return a closed loop (E101 round to J102)?", PATH("E101","feedsInto","J102"), ["true"]),
 ("F09","N2 return","Does K102 feed K101 directly (skipping J102)?", DIRECT("K102","feedsInto","K101"), ["false"]),
 ("F10","N2 return","Does the N2 return loop include TT304?", INSTEP(L,"TT304"), ["true"]),
 ("F11","N2 return","Does the N2 return loop include the PCV118 spillback?", INSTEP(L,"PCV118"), ["true"]),
 ("F12","N2 return","Does the N2 return loop include K101?", INSTEP(L,"K101"), ["true"]),
 ("C01","CO2 return","Where does gas from K401 go first?", OUT("K401_N_gas_outlet","feedsInto"), ["NRV401"]),
 ("C02","CO2 return","What does NRV401 feed?", OUT("NRV401","feedsInto"), ["FT302"]),
 ("C03","CO2 return","What does FT302 feed?", OUT("FT302","feedsInto"), ["FT301"]),
 ("C04","CO2 return","What does FT301 feed?", OUT("FT301","feedsInto"), ["K103"]),
 ("C05","CO2 return","What does K103 feed?", OUT("K103","feedsInto"), ["J103"]),
 ("C06","CO2 return","What does J103 discharge into?", OUT("J103","feedsInto"), ["NRV104"]),
 ("C07","CO2 return","Where does the CO2 return join the feed?", OUT("NRV104","feedsInto"), ["FEED_GAS_HEADER"]),
 ("C08","CO2 return","Does CO2 from K401 get back into E101?", PATH("K401_N_gas_outlet","feedsInto","E101"), ["true"]),
 ("C09","CO2 return","Can CO2 stripped in E100 reach the absorber E101?", PATH("E100","feedsInto","E101"), ["true"]),
 ("C10","CO2 return","Does J103 feed K101 directly (skipping NRV104)?", DIRECT("J103","feedsInto","K101"), ["false"]),
 ("P01","Piping","Where does the FCV111 recycle go?", OUT("FCV111","pipedTo"), ["K102"]),
 ("P02","Piping","Is FCV111 still piped into the E101 base (it should not be)?", DIRECT("FCV111","pipedTo","NRV111"), ["false"]),
 ("P03","Piping","Is J102 piped to K101 and to PCV118?", ALL(("J102","pipedTo","K101"),("J102","pipedTo","PCV118")), ["true"]),
 ("P04","Piping","Where does PCV118 spill back to?", OUT("PCV118","pipedTo"), ["K102"]),
 ("P05","Piping","Are FT304, FCV111 and PCV118 all piped into K102?", ALL(("FT304","pipedTo","K102"),("FCV111","pipedTo","K102"),("PCV118","pipedTo","K102")), ["true"]),
 ("P06","Piping","Is J103 piped to NRV104 and to PCV119?", ALL(("J103","pipedTo","NRV104"),("J103","pipedTo","PCV119")), ["true"]),
 ("P07","Piping","Where does PCV119 recycle CO2 to?", OUT("PCV119","pipedTo"), ["K103"]),
 ("P08","Piping","Is K103 piped to J103 and to its drain V185?", ALL(("K103","pipedTo","J103"),("K103","pipedTo","V185")), ["true"]),
 ("P09","Piping","Is K102 piped to J102 and to its drain V187?", ALL(("K102","pipedTo","J102"),("K102","pipedTo","V187")), ["true"]),
 ("P10","Piping","Is K101 piped to SDV170 (start of the FCV111 recycle)?", DIRECT("K101","pipedTo","SDV170"), ["true"]),
 ("E01","Equipment","Which blower does this piece add?", CLSP("Blower",P), ["J102"]),
 ("E02","Equipment","Which compressor does this piece add?", CLSP("Compressor",P), ["J103"]),
 ("E03","Equipment","Which knockout drums does this piece add?", CLSP("KnockoutDrum",P), ["K102","K103"]),
 ("E04","Equipment","Which pressure control valves does this piece add?", CLSP("PressureControlValve",P), ["PCV118","PCV114"]),
 ("E05","Equipment","Which check valves does this piece add?", CLSP("CheckValve",P), ["NRV104","NRV401"]),
 ("E06","Equipment","Which shutdown valve does this piece add?", CLSP("ShutdownValve",P), ["SDV171"]),
 ("E07","Equipment","Which manual valves does this piece add?", CLSP("ManualValve",P), ["V187","V185","V311","V312","V172"]),
 ("E08","Equipment","What grid is J102 at?", VAL("J102","gridReference"), ["L17"]),
 ("E09","Equipment","What grid is J103 at?", VAL("J103","gridReference"), ["M20"]),
 ("E10","Equipment","Which floor is J103 on?", VAL("J103","floor"), ["1"]),
 ("V01","Valves","What grid is V187 at?", VAL("V187","gridReference"), ["M17"]),
 ("V02","Valves","Is V187 normally closed?", VAL("V187","normalPosition"), ["closed"]),
 ("V03","Valves","Is V185 locked?", VAL("V185","hasLockingHandle"), ["true"]),
 ("V04","Valves","What grid is NRV104 at?", VAL("NRV104","gridReference"), ["O18"]),
 ("V05","Valves","Which floor is NRV401 on?", VAL("NRV401","floor"), ["4"]),
 ("V06","Valves","What grid is NRV401 at?", VAL("NRV401","gridReference"), ["D18"]),
 ("V07","Valves","What grid are V311 and V312 at?", VAL("V311","gridReference"), ["F17"]),
 ("V08","Valves","Is V312 normally closed?", VAL("V312","normalPosition"), ["closed"]),
 ("V09","Valves","What grid is SDV171 at?", VAL("SDV171","gridReference"), ["L19"]),
 ("V10","Valves","Is SDV171 open in normal running?", VAL("SDV171","normalPosition"), ["open"]),
 ("I01","Instruments","What type of sensor is TT304?", VAL("TT304","sensorType"), ["PRT"]),
 ("I02","Instruments","What grid is TT304 at?", VAL("TT304","gridReference"), ["G17"]),
 ("I03","Instruments","What type of sensor is TT114?", VAL("TT114","sensorType"), ["K-type thermocouple"]),
 ("I04","Instruments","What type of meter is FT107?", VAL("FT107","sensorType"), ["variable area volumetric flow meter"]),
 ("I05","Instruments","What signal does TT115 use?", VAL("TT115","signalType"), ["4-20mA"]),
 ("I06","Instruments","What type of transmitter is LT104?", VAL("LT104","sensorType"), ["differential pressure transmitter"]),
 ("I07","Instruments","What grid is LT104 at?", VAL("LT104","gridReference"), ["M19"]),
 ("I08","Instruments","What grid is PT110 at?", VAL("PT110","gridReference"), ["J18"]),
 ("I09","Instruments","What grid is PI402 at?", VAL("PI402","gridReference"), ["C16"]),
 ("I10","Instruments","What grid is PI403 at?", VAL("PI403","gridReference"), ["D17"]),
 ("I11","Instruments","Do TT304, FI303, FI304, TT114 and FT107 monitor J102?", ALL(("TT304","monitors","J102"),("FI303","monitors","J102"),("FI304","monitors","J102"),("TT114","monitors","J102"),("FT107","monitors","J102")), ["true"]),
 ("I12","Instruments","Does TT115 monitor J103?", ALL(("TT115","monitors","J103")), ["true"]),
 ("I13","Instruments","Are FT301 and FT302 on the CO2 return to J103?", ALL(("FT301","monitors","J103"),("FT302","monitors","J103")), ["true"]),
 ("I14","Instruments","Do LT104, LI106 and TI121 monitor K101?", ALL(("LT104","monitors","K101"),("LI106","monitors","K101"),("TI121","monitors","K101")), ["true"]),
 ("I15","Instruments","Do the local indicators TI410 and FI402 monitor C400?", ALL(("TI410","monitors","C400"),("FI402","monitors","C400")), ["true"]),
 ("I16","Instruments","What does FT301 measure now?", VAL("FT301","measuredVariable"), ["CO2 return flow (K401 to J103)"]),
 ("B01","Recycles","What does the K101 N2 recycle skip?", OUT("K101_N2_recycle","bypasses"), ["E101"]),
 ("B02","Recycles","Which valves are on the K101 N2 recycle?", OUT("K101_N2_recycle","routeVia"), ["SDV170","FCV111"]),
 ("B03","Recycles","Where does the K101 N2 recycle end?", OUT("K101_N2_recycle","toItem"), ["K102"]),
 ("B04","Recycles","Which valve is the J102 spillback?", OUT("J102_spillback","routeVia"), ["PCV118"]),
 ("B05","Recycles","Which valve recycles CO2 around K103?", OUT("K103_CO2_recycle","routeVia"), ["PCV119"]),
 ("B06","Recycles","Where does the K103 recycle start?", OUT("K103_CO2_recycle","fromItem"), ["J103"]),
 ("L01","Alarms","Which alarm is on the N2 return flow?", ALARM("FT303"), ["FAL_N2_return"]),
 ("L02","Alarms","Which alarm is on the CO2 return flow?", ALARM("FT301"), ["FAL_CO2_return"]),
 ("L03","Alarms","Which alarm is on K103?", ALARM("K103"), ["LAH_K103"]),
 ("L04","Alarms","Which alarms are on C400?", ALARM("C400"), ["TAH_C400_carryover"]),
 ("L05","Alarms","What kind of limit protects J103 from starving?", VAL("limit_TRIP_J103_starved","limitType"), ["trip"]),
 ("H01","HAZOP","Does HAZOP element 5 cover J102?", ALL(("HAZOP_element_5","covers","J102")), ["true"]),
 ("H02","HAZOP","Does HAZOP element 6 cover J103?", ALL(("HAZOP_element_6","covers","J103")), ["true"]),
 ("H03","HAZOP","Does HAZOP element 5 cover K402?", ALL(("HAZOP_element_5","covers","K402")), ["true"]),
 ("H04","HAZOP","Does HAZOP element 6 cover PCV119?", ALL(("HAZOP_element_6","covers","PCV119")), ["true"]),
 ("H05","HAZOP","Do HAZOP 5.1, 5.2, 5.4 and 5.9 concern J102?", ALL(("HAZOP_5_01","concerns","J102"),("HAZOP_5_02","concerns","J102"),("HAZOP_5_04","concerns","J102"),("HAZOP_5_09","concerns","J102")), ["true"]),
 ("H06","HAZOP","Do HAZOP 6.1, 6.2, 6.5, 6.6 and 6.9 concern J103?", ALL(("HAZOP_6_01","concerns","J103"),("HAZOP_6_02","concerns","J103"),("HAZOP_6_05","concerns","J103"),("HAZOP_6_06","concerns","J103"),("HAZOP_6_09","concerns","J103")), ["true"]),
 ("H07","HAZOP","Does HAZOP 6.5 concern PCV119?", ALL(("HAZOP_6_05","concerns","PCV119")), ["true"]),
 ("H08","HAZOP","Do HAZOP 6.2 and 6.3 concern FT301?", ALL(("HAZOP_6_02","concerns","FT301"),("HAZOP_6_03","concerns","FT301")), ["true"]),
 ("H09","HAZOP","Was a FAL added on FT303/304 (HAZOP 5.1)?", CONTAINS("HAZOP_5_01","actionTaken","FAL added"), ["true"]),
 ("H10","HAZOP","Was a J103 shutdown trip added (HAZOP 6.1)?", CONTAINS("HAZOP_6_01","actionTaken","trip added"), ["true"]),
 ("H11","HAZOP","Does HAZOP 6.3 ask for NRV104 to be reliable on CO2?", CONTAINS("HAZOP_6_03","recommendedAction","NRV104 reliable"), ["true"]),
 ("O01","Open items","Which open item concerns PCV119?", OIA("PCV119"), ["GR07"]),
 ("O02","Open items","Which open item concerns PT110?", OIA("PT110"), ["GR09"]),
 ("O03","Open items","Are GR05, GR06 and GR10 about J103?", ALL(("GR05","about","J103"),("GR06","about","J103"),("GR10","about","J103")), ["true"]),
 ("O04","Open items","Which open item concerns NRV111 now?", OIA("NRV111"), ["GOI03"]),
 ("O05","Open items","How many open items did this piece raise?", CNTOI(P), ["10"]),
 ("X01","Join","Do the CO2 supply, N2 supply and CO2 return all feed the common inlet?", ALL(("NRV101","feedsInto","FEED_GAS_HEADER"),("NRV102","feedsInto","FEED_GAS_HEADER"),("NRV104","feedsInto","FEED_GAS_HEADER")), ["true"]),
 ("X02","Join","Do the fresh-gas header and J102 both feed K101?", ALL(("FEED_GAS_HEADER","feedsInto","K101"),("J102","feedsInto","K101")), ["true"]),
 ("X03","Join","Does the stripper overhead (C400) lead to J103?", PATH("C400","feedsInto","J103"), ["true"]),
 ("X05","Join","Does K401 now flow to its gas outlet (fixed in piece 7)?", DIRECT("K401","feedsInto","K401_N_gas_outlet"), ["true"]),
 ("X04","Join","Does the N2 return pass the absorber pressure valve PCV300?", INSTEP(L,"PCV300"), ["false"]),
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
lines = ["# Gas returns KG: 100-question run", "", f"PASS {count['PASS']}, FAIL {count['FAIL']}, QUERY ERROR {count['QUERY ERROR']}", ""]
for qid, cat, question, expect, rows, status, err in results:
    lines += [f"## {qid} [{cat}] {status}", "", f"**{question}**", "", f"- Expected: {', '.join(expect)}"]
    lines += [f"- Error: {err}"] if err else [f"- KG: {', '.join(r[0] for r in rows) or '(no rows)'}"]
    lines.append("")
(HERE / "hundred_results_gas_return.md").write_text("\n".join(lines))
for qid, cat, question, expect, rows, status, err in results:
    if status != "PASS":
        print(f"[{qid}] {status} {question}\n      expected: {expect}\n      got: {[r[0] for r in rows]} {err or ''}")
print(f"\nPASS {count['PASS']}, FAIL {count['FAIL']}, QUERY ERROR {count['QUERY ERROR']}  (details in gas_return/hundred_results_gas_return.md)")
sys.exit(1 if count["FAIL"] or count["QUERY ERROR"] else 0)
