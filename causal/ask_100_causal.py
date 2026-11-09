"""
Ask the causal layer (piece 13) questions: single links, multi-hop causes and consequences, safeguards and the basis
of each link. Expected answers follow the HAZOP rows and report sections cited on each causal link. Runs on the full plant.
Run from the repo root (after ccpp/build_full_plant.py):   python causal/ask_100_causal.py
Output: causal/hundred_results_causal.md
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
def CONTAINS(s, p, text): return f"ASK {{ {T(s)} {T(p)} ?v . FILTER(CONTAINS(STR(?v), \"{text}\")) }}"
def CAUSES(v): return f"SELECT DISTINCT ?t WHERE {{ ?x (ccpp:raises|ccpp:lowers)+ {T(v)} . ?x ccpp:tag ?t }}"
def EFFECTS(x): return f"SELECT DISTINCT ?t WHERE {{ {T(x)} (ccpp:raises|ccpp:lowers)+ ?y . ?y ccpp:tag ?t }}"
def PATHC(a, b): return f"ASK {{ {T(a)} (ccpp:raises|ccpp:lowers)+ {T(b)} }}"
def CLSP(c, prefix): return (f"SELECT DISTINCT ?t WHERE {{ ?x a/rdfs:subClassOf* {T(c)} ; ccpp:tag ?t ; ccpp:citedIn ?c . "
                             f"FILTER(CONTAINS(STR(?c), \"__{prefix}cit\")) }}")
def CNTOI(prefix): return f"SELECT (COUNT(?o) AS ?n) WHERE {{ ?o a ccpp:OpenItem ; ccpp:foundBy \"{prefix} section build, Oct 2026\" }}"


P = "cau"
Q = [
 ("R01","Register","Which process variables does the causal layer define?", CLSP("ProcessVariable",P), ["V_C106_CW", "V_C200_CW", "V_C200_IN_T", "V_C400_CW", "V_C400_T", "V_CO2_FEED", "V_CO2_RET", "V_E100_CO2_RELEASE", "V_E100_L", "V_E100_P", "V_E100_T", "V_E101_CO2_OUT", "V_E101_GAS", "V_E101_L", "V_E101_P", "V_FEED_SAT", "V_H200_DUTY", "V_J100_CAV", "V_J103_CARRY", "V_K101_T", "V_K401_DP", "V_K401_L", "V_K402_CARRY", "V_LEAN_FLOW", "V_LEAN_T", "V_RICH_FLOW", "V_RICH_T", "V_STEAM", "V_Z102_DP"]),
 ("R02","Register","Which process events does the causal layer define?", CLSP("ProcessEvent",P), ["X_C100_NO_XFLOW", "X_C200_CW_LOST", "X_C400_CW_LOST", "X_FCV105_STUCK", "X_FCV111_OPENS", "X_GAS_FEED_HIGH", "X_J100_FAST", "X_J101_STOPS", "X_J102_STOPS", "X_J103_STOPS", "X_J104_STOPS", "X_K401_BLOCKED", "X_PCV119_CLOSED", "X_PCV300_CLOSED", "X_STEAM_EXCESS", "X_STEAM_FAIL", "X_Z102_BLOCKED"]),
 ("R03","Register","How many open items does the causal layer raise?", CNTOI(P), ["2"]),
 ("C01","Causes (multi-hop)","What can affect E100 pressure, directly or through other variables?", CAUSES("V_E100_P"), ["V_C400_CW", "V_C400_T", "V_CO2_RET", "V_E100_P", "V_E100_T", "V_H200_DUTY", "V_RICH_T", "V_STEAM", "X_C400_CW_LOST", "X_J103_STOPS", "X_K401_BLOCKED", "X_PCV119_CLOSED", "X_STEAM_EXCESS", "X_STEAM_FAIL"]),
 ("C02","Causes (multi-hop)","What can affect the CO2 left in the gas leaving E101, directly or through other variables?", CAUSES("V_E101_CO2_OUT"), ["V_C200_CW", "V_C200_IN_T", "V_C400_CW", "V_C400_T", "V_CO2_FEED", "V_CO2_RET", "V_E100_CO2_RELEASE", "V_E100_P", "V_E100_T", "V_H200_DUTY", "V_LEAN_FLOW", "V_LEAN_T", "V_RICH_T", "V_STEAM", "V_Z102_DP", "X_C100_NO_XFLOW", "X_C200_CW_LOST", "X_C400_CW_LOST", "X_FCV105_STUCK", "X_J100_FAST", "X_J103_STOPS", "X_K401_BLOCKED", "X_PCV119_CLOSED", "X_STEAM_EXCESS", "X_STEAM_FAIL", "X_Z102_BLOCKED"]),
 ("C03","Causes (multi-hop)","What can affect the lean MEA temperature into E101 (TT210), directly or through other variables?", CAUSES("V_LEAN_T"), ["V_C200_CW", "V_C200_IN_T", "X_C100_NO_XFLOW", "X_C200_CW_LOST"]),
 ("C04","Causes (multi-hop)","What can affect the E101 level (LT108), directly or through other variables?", CAUSES("V_E101_L"), ["V_LEAN_FLOW", "V_RICH_FLOW", "V_Z102_DP", "X_J100_FAST", "X_J101_STOPS", "X_Z102_BLOCKED"]),
 ("C05","Causes (multi-hop)","What can affect carry-over to J103, directly or through other variables?", CAUSES("V_J103_CARRY"), ["V_C400_CW", "V_C400_T", "V_CO2_RET", "V_E100_P", "V_E100_T", "V_H200_DUTY", "V_RICH_T", "V_STEAM", "X_C400_CW_LOST", "X_J103_STOPS", "X_K401_BLOCKED", "X_PCV119_CLOSED", "X_STEAM_EXCESS", "X_STEAM_FAIL"]),
 ("C06","Causes (multi-hop)","What can affect the J100 cavitation risk, directly or through other variables?", CAUSES("V_J100_CAV"), ["V_C200_IN_T", "V_E100_L", "V_LEAN_FLOW", "V_RICH_FLOW", "V_Z102_DP", "X_C100_NO_XFLOW", "X_J100_FAST", "X_J101_STOPS", "X_Z102_BLOCKED"]),
 ("C07","Causes (multi-hop)","What can affect the E100 level (LT101), directly or through other variables?", CAUSES("V_E100_L"), ["V_LEAN_FLOW", "V_RICH_FLOW", "V_Z102_DP", "X_J100_FAST", "X_J101_STOPS", "X_Z102_BLOCKED"]),
 ("F01","Consequences (multi-hop)","What is affected if cooling water to C400 is lost?", EFFECTS("X_C400_CW_LOST"), ["V_C400_CW", "V_C400_T", "V_E100_CO2_RELEASE", "V_E100_P", "V_E100_T", "V_E101_CO2_OUT", "V_J103_CARRY"]),
 ("F02","Consequences (multi-hop)","What is affected if the steam supply fails?", EFFECTS("X_STEAM_FAIL"), ["V_E100_CO2_RELEASE", "V_E100_P", "V_E100_T", "V_E101_CO2_OUT", "V_J103_CARRY", "V_STEAM"]),
 ("F03","Consequences (multi-hop)","What is affected if the K401 demister blocks?", EFFECTS("X_K401_BLOCKED"), ["V_CO2_RET", "V_E100_CO2_RELEASE", "V_E100_P", "V_E100_T", "V_E101_CO2_OUT", "V_J103_CARRY", "V_K401_DP"]),
 ("F04","Consequences (multi-hop)","What is affected if J101 stops?", EFFECTS("X_J101_STOPS"), ["V_E100_L", "V_E101_L", "V_J100_CAV", "V_K402_CARRY", "V_RICH_FLOW"]),
 ("F05","Consequences (multi-hop)","What is affected if rich MEA stops flowing through C100?", EFFECTS("X_C100_NO_XFLOW"), ["V_C200_IN_T", "V_E101_CO2_OUT", "V_J100_CAV", "V_LEAN_T"]),
 ("D01","Direction","Does PCV119 failing closed raise E100 pressure?", DIRECT("X_PCV119_CLOSED","raises","V_E100_P"), ["true"]),
 ("D02","Direction","Does hotter lean MEA raise the CO2 left in the E101 outlet gas?", DIRECT("V_LEAN_T","raises","V_E101_CO2_OUT"), ["true"]),
 ("D03","Direction","Does more C400 cooling water lower the C400 gas outlet temperature?", DIRECT("V_C400_CW","lowers","V_C400_T"), ["true"]),
 ("D04","Direction","Does more lean MEA flow lower the E100 level?", DIRECT("V_LEAN_FLOW","lowers","V_E100_L"), ["true"]),
 ("D05","Direction","Does more rich MEA flow raise the E100 level?", DIRECT("V_RICH_FLOW","raises","V_E100_L"), ["true"]),
 ("D06","Direction","Does a hotter C400 outlet raise E100 pressure (HAZOP 12.7)?", DIRECT("V_C400_T","raises","V_E100_P"), ["true"]),
 ("D07","Direction","Does J102 stopping lower the N2 flow up E101?", DIRECT("X_J102_STOPS","lowers","V_E101_GAS"), ["true"]),
 ("D08","Direction","Does a hotter stripper release more CO2?", DIRECT("V_E100_T","raises","V_E100_CO2_RELEASE"), ["true"]),
 ("D09","Direction","Does more lean MEA flow raise the E100 level (it should not)?", DIRECT("V_LEAN_FLOW","raises","V_E100_L"), ["false"]),
 ("P01","Paths","Can losing C400 cooling water raise E100 pressure through the chain?", PATHC("X_C400_CW_LOST","V_E100_P"), ["true"]),
 ("P02","Paths","Can a steam failure affect CO2 capture in E101 (four steps)?", PATHC("X_STEAM_FAIL","V_E101_CO2_OUT"), ["true"]),
 ("P03","Paths","Can J102 stopping affect E100 pressure (it should not, in this layer)?", PATHC("X_J102_STOPS","V_E100_P"), ["false"]),
 ("P04","Paths","Can a blocked Z102 affect the E101 level?", PATHC("X_Z102_BLOCKED","V_E101_L"), ["true"]),
 ("I01","Links","Which instruments read E100 pressure?", OUT("V_E100_P","indicatedBy"), ["PT401", "PT402"]),
 ("I02","Links","Which instrument reads the lean MEA temperature into E101?", OUT("V_LEAN_T","indicatedBy"), ["TT210"]),
 ("I03","Links","Which instrument reads the K401/C400 condensate level?", OUT("V_K401_L","indicatedBy"), ["LT401"]),
 ("I04","Links","Which controller regulates the lean MEA temperature into E101?", OUT("V_LEAN_T","regulatedBy"), ["TIC210"]),
 ("I05","Links","Which controllers regulate E100 pressure?", OUT("V_E100_P","regulatedBy"), ["PIC401", "PIC402"]),
 ("I06","Links","Which controller regulates the C400 gas outlet temperature?", OUT("V_C400_T","regulatedBy"), ["TIC410"]),
 ("S01","Safeguards","Is E100 pressure safeguarded by the 2 barg PSH, its shutdown response and RV401?", ALL(("V_E100_P","safeguardedBy","limit_PSH_E100_2barg"), ("V_E100_P","safeguardedBy","ARP_E100_PSH"), ("V_E100_P","safeguardedBy","RV401")), ["true"]),
 ("S02","Safeguards","Is E101 pressure safeguarded by RV400 and its PSH?", ALL(("V_E101_P","safeguardedBy","RV400"), ("V_E101_P","safeguardedBy","limit_PSH_E101")), ["true"]),
 ("S03","Safeguards","Is the C400 cooling water safeguarded by the FT402 low-flow alarm?", ALL(("V_C400_CW","safeguardedBy","limit_FAL_FT402")), ["true"]),
 ("S04","Safeguards","Is the CO2 return safeguarded by its low-flow alarm and the J103 trip?", ALL(("V_CO2_RET","safeguardedBy","limit_FAL_CO2_return"), ("V_CO2_RET","safeguardedBy","limit_TRIP_J103_starved")), ["true"]),
 ("S05","Safeguards","Are the LT101 alarm responses safeguards on the E100 level?", ALL(("V_E100_L","safeguardedBy","ARP_LT101_L"), ("V_E100_L","safeguardedBy","ARP_LT101_H")), ["true"]),
 ("S06","Safeguards","Is the J100 cavitation risk safeguarded by its envelope and LZAL102?", ALL(("V_J100_CAV","safeguardedBy","ENV_J100"), ("V_J100_CAV","safeguardedBy","limit_LZAL102")), ["true"]),
 ("B01","Basis","Is the C400-to-E100-pressure link based on the HAZOP?", CONTAINS("CE_13","basis","HAZOP"), ["true"]),
 ("B02","Basis","Does that link explain the mechanism (less condensation)?", CONTAINS("CE_13","mechanism","less condensation"), ["true"]),
 ("B03","Basis","Is the CO2-return-to-E100-pressure link marked as a physical rule?", CONTAINS("CE_19","basis","physical rule"), ["true"]),
 ("B04","Basis","Does the lean temperature link say hot MEA absorbs CO2 less well?", CONTAINS("CE_26","mechanism","absorbs CO2 less well"), ["true"]),
 ("X01","Join","Is the causal link for PCV119 recorded with its cause and effect nodes?", ALL(("CE_01","causeNode","X_PCV119_CLOSED"),("CE_01","effectNode","V_E100_P")), ["true"]),
 ("X02","Join","Is the steam failure event tied to the steam supply (piece 8)?", ALL(("X_STEAM_FAIL","eventOf","STEAM_SUPPLY")), ["true"]),
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
lines = ["# Causal layer KG: question run", "", f"PASS {count['PASS']}, FAIL {count['FAIL']}, QUERY ERROR {count['QUERY ERROR']}", ""]
for qid, cat, question, expect, rows, status, err in results:
    lines += [f"## {qid} [{cat}] {status}", "", f"**{question}**", "", f"- Expected: {', '.join(expect)}"]
    lines += [f"- Error: {err}"] if err else [f"- KG: {', '.join(r[0] for r in rows) or '(no rows)'}"]
    lines.append("")
(HERE / "hundred_results_causal.md").write_text("\n".join(lines))
for qid, cat, question, expect, rows, status, err in results:
    if status != "PASS":
        print(f"[{qid}] {status} {question}\n      expected: {expect}\n      got: {[r[0] for r in rows]} {err or ''}")
print(f"\nPASS {count['PASS']}, FAIL {count['FAIL']}, QUERY ERROR {count['QUERY ERROR']}  (details in causal/hundred_results_causal.md)")
sys.exit(1 if count["FAIL"] or count["QUERY ERROR"] else 0)