"""
Ask the utilities KG (piece 8) 100 questions whose expected answers come from the
documents (the team then traces and checks it on the P&ID), not from the KG. Piece 8 links to items in other
sections, so the questions run on the joined full plant.
Run from the repo root (after ccpp/build_full_plant.py):   python utilities/ask_100_utilities.py
Output: utilities/hundred_results_utilities.md
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


P = "utl"
L = "SteamRoute"
Q = [
 ("S01","Steam","What comes first after the building steam supply?", OUT("STEAM_SUPPLY","feedsInto"), ["XV140"]),
 ("S02","Steam","What does XV140 feed?", OUT("XV140","feedsInto"), ["V100"]),
 ("S03","Steam","What does V100 feed?", OUT("V100","feedsInto"), ["V101"]),
 ("S04","Steam","What does V101 feed?", OUT("V101","feedsInto"), ["FT100"]),
 ("S05","Steam","What does FT100 feed?", OUT("FT100","feedsInto"), ["V102"]),
 ("S06","Steam","What does V102 feed?", OUT("V102","feedsInto"), ["FT101"]),
 ("S07","Steam","What does FT101 feed?", OUT("FT101","feedsInto"), ["FCV110"]),
 ("S08","Steam","Does FCV110 feed the H100 steam inlet?", DIRECT("FCV110","feedsInto","H100_N_steam_in"), ["true"]),
 ("S09","Steam","What does K100 feed?", OUT("K100","feedsInto"), ["V103"]),
 ("S10","Steam","What does V103 feed?", OUT("V103","feedsInto"), ["V105"]),
 ("S11","Steam","What does V105 feed?", OUT("V105","feedsInto"), ["NRV110"]),
 ("S12","Steam","What does NRV110 feed?", OUT("NRV110","feedsInto"), ["CONDENSATE_RETURN"]),
 ("S13","Steam","Does steam reach the condensate return?", PATH("STEAM_SUPPLY","feedsInto","CONDENSATE_RETURN"), ["true"]),
 ("S14","Steam","Can steam flow into the E100 process side (it must not)?", PATH("STEAM_SUPPLY","feedsInto","E100"), ["false"]),
 ("S15","Steam","Does the steam route include PT101?", INSTEP(L,"PT101"), ["true"]),
 ("S16","Steam","Does the steam route include the RV107 relief?", INSTEP(L,"RV107"), ["true"]),
 ("W01","Cooling water","What does V194 feed?", OUT("V194","feedsInto"), ["PCV103"]),
 ("W02","Cooling water","What does PCV103 feed?", OUT("PCV103","feedsInto"), ["FCV102"]),
 ("W03","Cooling water","What does FCV102 feed?", OUT("FCV102","feedsInto"), ["FT106"]),
 ("W04","Cooling water","Does FT106 feed the C106 cooling water inlet?", DIRECT("FT106","feedsInto","C106_N_cw_in"), ["true"]),
 ("W05","Cooling water","What does V208 feed?", OUT("V208","feedsInto"), ["FCV201"]),
 ("W06","Cooling water","What does FCV201 feed?", OUT("FCV201","feedsInto"), ["FCV200"]),
 ("W07","Cooling water","What does FCV200 feed?", OUT("FCV200","feedsInto"), ["FT201"]),
 ("W08","Cooling water","What does V405 feed?", OUT("V405","feedsInto"), ["PCV415"]),
 ("W09","Cooling water","What does PCV415 feed?", OUT("PCV415","feedsInto"), ["FCV401"]),
 ("W10","Cooling water","What does V410 feed?", OUT("V410","feedsInto"), ["V411"]),
 ("W11","Cooling water","Which valves start the three cooling water streams?", ALL(("CW_SUPPLY","feedsInto","V194"),("CW_SUPPLY","feedsInto","V208"),("CW_SUPPLY","feedsInto","V405")), ["true"]),
 ("W12","Cooling water","Do all three streams end at the cooling water return?", ALL(("V136","feedsInto","CW_RETURN"),("V214","feedsInto","CW_RETURN"),("V411","feedsInto","CW_RETURN")), ["true"]),
 ("W13","Cooling water","Does cooling water reach its return?", PATH("CW_SUPPLY","feedsInto","CW_RETURN"), ["true"]),
 ("W14","Cooling water","Can cooling water flow into E101 (it must not)?", PATH("CW_SUPPLY","feedsInto","E101"), ["false"]),
 ("W15","Cooling water","Can cooling water flow into E100 (it must not)?", PATH("CW_SUPPLY","feedsInto","E100"), ["false"]),
 ("W16","Cooling water","Does the C400 cooling water pass through FCV401 before C400?", PATH("FCV401","feedsInto","C400_N_cw_in"), ["true"]),
 ("P01","Piping","Is V106 piped from the H100 condensate outlet (bypass round K100)?", DIRECT("H100_N_condensate_out","pipedTo","V106"), ["true"]),
 ("P02","Piping","Where does the V106 bypass rejoin?", OUT("V106","pipedTo"), ["V103"]),
 ("P03","Piping","Is V195 piped off the C106 cooling water outlet?", DIRECT("C106_N_cw_out","pipedTo","V195"), ["true"]),
 ("P04","Piping","Is V215 piped off the C200 cooling water outlet?", DIRECT("C200_N_cw_out","pipedTo","V215"), ["true"]),
 ("P05","Piping","Is V412 piped off the C400 cooling water outlet?", DIRECT("C400_N_cw_out","pipedTo","V412"), ["true"]),
 ("P06","Piping","Which equipment is the steam inlet on?", VAL("H100_N_steam_in","onEquipment"), ["H100"]),
 ("P07","Piping","Which equipment is the C200 cooling water inlet on?", VAL("C200_N_cw_in","onEquipment"), ["C200"]),
 ("P08","Piping","Which equipment is the C400 cooling water outlet on?", VAL("C400_N_cw_out","onEquipment"), ["C400"]),
 ("E01","Equipment","Which steam trap does this piece add?", CLSP("SteamTrap",P), ["K100"]),
 ("E02","Equipment","Which supply connections does this piece add?", CLSP("SupplyConnection",P), ["STEAM_SUPPLY","CW_SUPPLY"]),
 ("E03","Equipment","Which return connections does this piece add?", CLSP("ReturnConnection",P), ["CONDENSATE_RETURN","CW_RETURN"]),
 ("E04","Equipment","Which shutdown valve does this piece add?", CLSP("ShutdownValve",P), ["XV140"]),
 ("E05","Equipment","Which check valve does this piece add?", CLSP("CheckValve",P), ["NRV110"]),
 ("E06","Equipment","Which relief valve does this piece add?", CLSP("ReliefValve",P), ["RV107"]),
 ("E07","Equipment","Which pressure control valves does this piece add?", CLSP("PressureControlValve",P), ["PCV103","PCV415"]),
 ("E08","Equipment","Which manual valves does this piece add?", CLSP("ManualValve",P), ["V100","V103","V104","V194","V195","V136","V196","V197","V208","V209","V214","V215","V405","V410","V411","V412"]),
 ("E09","Equipment","Which floor is K100 on?", VAL("K100","floor"), ["1"]),
 ("V01","Valves","What grid is XV140 at?", VAL("XV140","gridReference"), ["L2"]),
 ("V02","Valves","What grid is V100 at?", VAL("V100","gridReference"), ["L3"]),
 ("V03","Valves","Is V100 open in normal running?", VAL("V100","normalPosition"), ["open"]),
 ("V04","Valves","What grid is V103 at?", VAL("V103","gridReference"), ["M5"]),
 ("V05","Valves","Is V104 closed in normal running?", VAL("V104","normalPosition"), ["closed"]),
 ("V06","Valves","What grid is NRV110 at?", VAL("NRV110","gridReference"), ["M3"]),
 ("V07","Valves","What grid is RV107 at?", VAL("RV107","gridReference"), ["M5"]),
 ("V08","Valves","What grid is V194 at?", VAL("V194","gridReference"), ["R15"]),
 ("V09","Valves","What grid is PCV103 at?", VAL("PCV103","gridReference"), ["R15"]),
 ("V10","Valves","Is V195 closed in normal running?", VAL("V195","normalPosition"), ["closed"]),
 ("V11","Valves","What grid is V208 at?", VAL("V208","gridReference"), ["H11"]),
 ("V12","Valves","Which floor is V208 on?", VAL("V208","floor"), ["2"]),
 ("V13","Valves","Is V209 locked?", VAL("V209","hasLockingHandle"), ["true"]),
 ("V14","Valves","What grid is V214 at?", VAL("V214","gridReference"), ["K13"]),
 ("V15","Valves","Is V215 closed in normal running?", VAL("V215","normalPosition"), ["closed"]),
 ("V16","Valves","What grid is PCV415 at?", VAL("PCV415","gridReference"), ["C14"]),
 ("V17","Valves","Which floor is PCV415 on?", VAL("PCV415","floor"), ["4"]),
 ("V18","Valves","What grid are V410 and V411 at?", VAL("V410","gridReference"), ["D10"]),
 ("V19","Valves","Is V411 locked?", VAL("V411","hasLockingHandle"), ["true"]),
 ("V20","Valves","Is V412 closed in normal running?", VAL("V412","normalPosition"), ["closed"]),
 ("V21","Valves","What grid is V136 at?", VAL("V136","gridReference"), ["P18"]),
 ("I01","Instruments","What type of transmitter is PT101?", VAL("PT101","sensorType"), ["gauge pressure transmitter"]),
 ("I02","Instruments","What grid is PT101 at?", VAL("PT101","gridReference"), ["L3"]),
 ("I03","Instruments","What signal does PT101 use?", VAL("PT101","signalType"), ["4-20mA"]),
 ("I04","Instruments","What grid is TT117 at (per Fig F.12)?", VAL("TT117","gridReference"), ["L4"]),
 ("I05","Instruments","What grid is TT118 at (per Fig F.12)?", VAL("TT118","gridReference"), ["M5"]),
 ("I06","Instruments","What signal do TT117 and TT118 use?", VAL("TT118","signalType"), ["Profibus-PA"]),
 ("I07","Instruments","What does TT117 measure?", VAL("TT117","measuredVariable"), ["steam temperature into H100"]),
 ("I08","Instruments","Do PT101, PI100, PI101, FI100, TT117 and TT118 monitor H100?", ALL(("PT101","monitors","H100"),("PI100","monitors","H100"),("PI101","monitors","H100"),("FI100","monitors","H100"),("TT117","monitors","H100"),("TT118","monitors","H100")), ["true"]),
 ("I09","Instruments","Do FI106 and TT119 monitor C106?", ALL(("FI106","monitors","C106"),("TT119","monitors","C106")), ["true"]),
 ("I10","Instruments","Do FI200 and FI201 monitor C200?", ALL(("FI200","monitors","C200"),("FI201","monitors","C200")), ["true"]),
 ("I11","Instruments","What grid is TT119 at?", VAL("TT119","gridReference"), ["R17"]),
 ("I12","Instruments","What grid is FI200 at?", VAL("FI200","gridReference"), ["H11"]),
 ("B01","Bypass","What does the V106 bypass skip?", OUT("K100_bypass","bypasses"), ["K100"]),
 ("B02","Bypass","Which valve is on the K100 bypass?", OUT("K100_bypass","routeVia"), ["V106"]),
 ("B03","Bypass","Is the K100 bypass normally closed?", VAL("K100_bypass","normalState"), ["closed"]),
 ("H01","HAZOP","Does HAZOP element 13 cover XV140?", ALL(("HAZOP_element_13","covers","XV140")), ["true"]),
 ("H02","HAZOP","Does HAZOP element 13 cover K100 and RV107?", ALL(("HAZOP_element_13","covers","K100"),("HAZOP_element_13","covers","RV107")), ["true"]),
 ("H03","HAZOP","Do HAZOP 13.1 and 13.6 concern V106?", ALL(("HAZOP_13_01","concerns","V106"),("HAZOP_13_06","concerns","V106")), ["true"]),
 ("H04","HAZOP","Does HAZOP 13.6 concern K100?", ALL(("HAZOP_13_06","concerns","K100")), ["true"]),
 ("H05","HAZOP","Does HAZOP 13.4 (steam limit ~140 kg/h) concern FCV110?", ALL(("HAZOP_13_04","concerns","FCV110")), ["true"]),
 ("H06","HAZOP","Was a plant shutdown on steam failure added (HAZOP 13.3)?", CONTAINS("HAZOP_13_03","actionTaken","shutdown"), ["true"]),
 ("O01","Open items","Which open item concerns K100?", ALL(("UT02","about","K100")), ["true"]),
 ("O02","Open items","Which open items concern V197?", ALL(("UT07","about","V197"),("UT08","about","V197")), ["true"]),
 ("O03","Open items","Which open item concerns TT117?", OIA("TT117"), ["UT04"]),
 ("O04","Open items","Which open item concerns RV107?", OIA("RV107"), ["UT05"]),
 ("O05","Open items","How many open items did this piece raise?", CNTOI(P), ["10"]),
 ("X01","Join","Is the H100 steam limit (140 kg/h) still on H100?", LIM("H100_steam_limit","high"), ["140"]),
 ("X02","Join","Is the C400 cooling water valve still controlled by FIC402?", ALL(("FIC402","controls","FCV401")), ["true"]),
 ("X03","Join","Is the C106 cooling water valve still controlled by FIC106 and TIC121?", ALL(("FIC106","controls","FCV102"),("TIC121","controls","FCV102")), ["true"]),
 ("X04","Join","Does the MEA side of H100 still feed E100 (process unaffected)?", PATH("H100","feedsInto","E100"), ["true"]),
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
lines = ["# Utilities KG: 100-question run", "", f"PASS {count['PASS']}, FAIL {count['FAIL']}, QUERY ERROR {count['QUERY ERROR']}", ""]
for qid, cat, question, expect, rows, status, err in results:
    lines += [f"## {qid} [{cat}] {status}", "", f"**{question}**", "", f"- Expected: {', '.join(expect)}"]
    lines += [f"- Error: {err}"] if err else [f"- KG: {', '.join(r[0] for r in rows) or '(no rows)'}"]
    lines.append("")
(HERE / "hundred_results_utilities.md").write_text("\n".join(lines))
for qid, cat, question, expect, rows, status, err in results:
    if status != "PASS":
        print(f"[{qid}] {status} {question}\n      expected: {expect}\n      got: {[r[0] for r in rows]} {err or ''}")
print(f"\nPASS {count['PASS']}, FAIL {count['FAIL']}, QUERY ERROR {count['QUERY ERROR']}  (details in utilities/hundred_results_utilities.md)")
sys.exit(1 if count["FAIL"] or count["QUERY ERROR"] else 0)
