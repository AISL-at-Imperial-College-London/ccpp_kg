"""
Ask the overhead and reflux KG (piece 4) 100 questions whose expected answers come from the
documents and the team's P&ID trace, not from the KG. Piece 4 links to items in other
sections, so the questions run on the joined full plant.
Run from the repo root (after ccpp/build_full_plant.py):   python overhead/ask_100_overhead.py
Output: overhead/hundred_results_overhead.md
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
def HMTCMP(eq, a, b): return (f"ASK {{ ?p ccpp:ofEquipment {T(eq)} ; ccpp:inCase ?c ; {T(a)} ?x ; {T(b)} ?y . "
                              f"?c ccpp:recommendedForUse true . FILTER(?x > ?y) }}")
def OIA(t): return f"SELECT ?o WHERE {{ ?o a ccpp:OpenItem ; ccpp:about {T(t)} }}"
def CNT(c): return f"SELECT (COUNT(DISTINCT ?x) AS ?n) WHERE {{ ?x a/rdfs:subClassOf* {T(c)} }}"
def INSTEP(loop, item): return f"ASK {{ {T(loop)} ccpp:hasStep/ccpp:stepItem {T(item)} }}"
def CLSP(c, prefix): return (f"SELECT DISTINCT ?t WHERE {{ ?x a/rdfs:subClassOf* {T(c)} ; ccpp:tag ?t ; ccpp:citedIn ?c . "
                             f"FILTER(CONTAINS(STR(?c), \"__{prefix}cit\")) }}")
def CNTOI(prefix): return f"SELECT (COUNT(?o) AS ?n) WHERE {{ ?o a ccpp:OpenItem ; ccpp:foundBy \"{prefix} section build, Oct 2026\" }}"


L = "OverheadRefluxLoop"
Q = [
 ("F01", "Flow", "Where does the E100 overhead vapour go first?", OUT("E100_N_overhead", "feedsInto"), ["C400"]),
 ("F02", "Flow", "What does C400 feed?", OUT("C400", "feedsInto"), ["K401"]),
 ("F03", "Flow", "What does K401 feed (liquid side)?", OUT("K401", "feedsInto"), ["J300"]),
 ("F04", "Flow", "What does J300 discharge into?", OUT("J300", "feedsInto"), ["PCV302"]),
 ("F05", "Flow", "What does PCV302 feed?", OUT("PCV302", "feedsInto"), ["FT305"]),
 ("F06", "Flow", "Where does the reflux join the solvent line?", OUT("FT305", "feedsInto"), ["V403"]),
 ("F07", "Flow", "What feeds V403 (heaters and reflux)?", INN("feedsInto", "V403"), ["H200a", "H200b", "FT305"]),
 ("F08", "Flow", "What feeds K401?", INN("feedsInto", "K401"), ["C400"]),
 ("F09", "Flow", "What feeds J300?", INN("feedsInto", "J300"), ["K401"]),
 ("F10", "Flow", "Does the overhead vapour get back to E100 as reflux?", PATH("E100_N_overhead", "feedsInto", "E100"), ["true"]),
 ("F11", "Flow", "Is the overhead loop closed (J300 round to C400)?", PATH("J300", "feedsInto", "C400"), ["true"]),
 ("F12", "Flow", "Does K401 feed PCV302 directly?", DIRECT("K401", "feedsInto", "PCV302"), ["false"]),
 ("F13", "Flow", "Can condensate from C400 reach J100 through E100?", PATH("C400", "feedsInto", "J100"), ["true"]),
 ("F14", "Flow", "Is B300 on the flow path (does it feed PCV302)?", DIRECT("B300", "feedsInto", "PCV302"), ["false"]),
 ("P01", "Piping", "What is J300 piped to?", OUT("J300", "pipedTo"), ["PCV302", "RV300", "B300"]),
 ("P02", "Piping", "What is PCV302 piped to?", OUT("PCV302", "pipedTo"), ["FT305", "V317"]),
 ("P03", "Piping", "Which tagged item is K401 piped to?", OUT("K401", "pipedTo"), ["J300"]),
 ("P04", "Piping", "What is FT305 piped to?", OUT("FT305", "pipedTo"), ["V403"]),
 ("P05", "Piping", "What is piped into V403?", INN("pipedTo", "V403"), ["H200a", "H200b", "FT305"]),
 ("P06", "Piping", "What is C400 piped to?", OUT("C400", "pipedTo"), ["K401"]),
 ("P07", "Piping", "Which equipment is the gas outlet nozzle on?", VAL("K401_N_gas_outlet", "onEquipment"), ["K401"]),
 ("P08", "Piping", "Which equipment is the overhead nozzle on?", VAL("E100_N_overhead", "onEquipment"), ["E100"]),
 ("E01", "Equipment", "Which condenser does this piece add?", CLSP("Condenser", "ovh"), ["C400"]),
 ("E02", "Equipment", "Which knockout drum does this piece add?", CLSP("KnockoutDrum", "ovh"), ["K401"]),
 ("E03", "Equipment", "Which pump does this piece add?", CLSP("Pump", "ovh"), ["J300"]),
 ("E04", "Equipment", "Which pulsation dampener does this piece add?", CLSP("PulsationDampener", "ovh"), ["B300"]),
 ("E05", "Equipment", "Which relief valve does this piece add?", CLSP("ReliefValve", "ovh"), ["RV300"]),
 ("E06", "Equipment", "Which pressure control valve does this piece add?", CLSP("PressureControlValve", "ovh"), ["PCV302"]),
 ("E07", "Equipment", "Which flow control valve does this piece add?", CLSP("FlowControlValve", "ovh"), ["FCV401"]),
 ("E08", "Equipment", "Which floor is J300 on?", VAL("J300", "floor"), ["3"]),
 ("E09", "Equipment", "What grid is J300 at?", VAL("J300", "gridReference"), ["G10"]),
 ("E10", "Equipment", "Which floor is C400 on?", VAL("C400", "floor"), ["4"]),
 ("V01", "Valves", "What grid is PCV302 at?", VAL("PCV302", "gridReference"), ["G9"]),
 ("V02", "Valves", "Which floor is PCV302 on?", VAL("PCV302", "floor"), ["3"]),
 ("V03", "Valves", "What grid is RV300 at?", VAL("RV300", "gridReference"), ["G10"]),
 ("V04", "Valves", "Is V317 normally open or closed?", VAL("V317", "normalPosition"), ["closed"]),
 ("V05", "Valves", "What type of valve is V317?", VAL("V317", "valveType"), ["ball"]),
 ("V06", "Valves", "What grid is V317 at?", VAL("V317", "gridReference"), ["H9"]),
 ("V07", "Valves", "What grid is FCV401 at?", VAL("FCV401", "gridReference"), ["C12"]),
 ("V08", "Valves", "Which floor is FCV401 on?", VAL("FCV401", "floor"), ["4"]),
 ("I01", "Instruments", "What type of transmitter is LT401?", VAL("LT401", "sensorType"), ["differential pressure transmitter"]),
 ("I02", "Instruments", "What signal does LT401 use?", VAL("LT401", "signalType"), ["4-20mA"]),
 ("I03", "Instruments", "What grid is LT401 at?", VAL("LT401", "gridReference"), ["F10"]),
 ("I04", "Instruments", "What signal does TT310 use?", VAL("TT310", "signalType"), ["4-20mA"]),
 ("I05", "Instruments", "What grid is TT310 at?", VAL("TT310", "gridReference"), ["G9"]),
 ("I06", "Instruments", "What grid is TT410 at?", VAL("TT410", "gridReference"), ["C15"]),
 ("I07", "Instruments", "What signal does TT410 use?", VAL("TT410", "signalType"), ["Fieldbus"]),
 ("I08", "Instruments", "What grid is LSHH400 at?", VAL("LSHH400", "gridReference"), ["E10"]),
 ("I09", "Instruments", "What does LSHH400 monitor?", OUT("LSHH400", "monitors"), ["K401"]),
 ("I10", "Instruments", "Which instruments monitor K401?", INN("monitors", "K401"), ["LSHH400", "LT401", "PT402"]),
 ("I11", "Instruments", "Which instruments monitor J300?", INN("monitors", "J300"), ["TT310", "FT305", "TT309"]),
 ("I12", "Instruments", "Which instruments monitor C400?", INN("monitors", "C400"), ["TT410", "FT402", "FI401", "PT401"]),
 ("I13", "Instruments", "What type of meter is FT305?", VAL("FT305", "sensorType"), ["Coriolis mass flow meter"]),
 ("I14", "Instruments", "What grid is TT309 at?", VAL("TT309", "gridReference"), ["F9"]),
 ("I15", "Instruments", "What grid is PT401 at?", VAL("PT401", "gridReference"), ["C8"]),
 ("I16", "Instruments", "What grid is FI401 at?", VAL("FI401", "gridReference"), ["C14"]),
 ("C01", "Control", "Which controllers act on J300?", INN("controls", "J300", "Controller"), ["LIC401", "SIC300"]),
 ("C02", "Control", "Which sensor does the K401 level loop use?", OUT("CL_K401_level", "hasSensor"), ["LT401"]),
 ("C03", "Control", "What does the K401 level loop adjust?", OUT("CL_K401_level", "hasFinalElement"), ["J300"]),
 ("C04", "Control", "Which sensor does the C400 temperature loop use?", OUT("CL_C400_temperature", "hasSensor"), ["TT410"]),
 ("C05", "Control", "Which controller is the C400 temperature master?", OUT("CL_C400_temperature", "hasController"), ["TIC410"]),
 ("C06", "Control", "Which sensor does the C400 cooling water loop use?", OUT("CL_C400_cooling_water", "hasSensor"), ["FT402"]),
 ("C07", "Control", "Which valve does the C400 cooling water loop move?", OUT("CL_C400_cooling_water", "hasFinalElement"), ["FCV401"]),
 ("C08", "Control", "Which loop is the C400 temperature loop master of?", VAL("CL_C400_temperature", "cascadeMasterOf"), ["CL_C400_cooling_water"]),
 ("C09", "Control", "Which controllers act on FCV401?", INN("controls", "FCV401", "Controller"), ["TIC410", "FIC402"]),
 ("C10", "Control", "Which valve sets the stripper pressure?", OUT("CL_E100_pressure", "hasFinalElement"), ["PCV119"]),
 ("L01", "Limits", "What is RV300 set to?", LIM("RV300_set", "high"), ["10"]),
 ("L02", "Limits", "What is PCV302 set to?", LIM("PCV302_set", "high"), ["8"]),
 ("L03", "Limits", "What pressure does B300 operate at?", LIM("B300_operating", "high"), ["3"]),
 ("L04", "Limits", "Which alarm detects a blocked K401 demister?", ALARM("K401"), ["PDAH_K401_demister"]),
 ("L05", "Limits", "Which alarm detects low cooling water to C400?", ALARM("FT402"), ["FAL_FT402"]),
 ("L06", "Limits", "Which alarm is on LSHH400?", ALARM("LSHH400"), ["LZAH_K401"]),
 ("L07", "Limits", "Which alarm is on LT401?", ALARM("LT401"), ["LAL_K401"]),
 ("L08", "Limits", "What does RV300 protect?", OUT("RV300", "protects"), ["J300"]),
 ("L09", "Limits", "What unit is the RV300 setting in?", VAL("limit_RV300_set", "unit"), ["bar"]),
 ("D01", "Discrepancies", "Which discrepancy concerns B300?", DISC("B300"), ["discrepancy_B300_pressure"]),
 ("D02", "Discrepancies", "Which discrepancy concerns TT309?", DISC("TT309"), ["discrepancy_TT309_FT305_order"]),
 ("D03", "Discrepancies", "Which discrepancy concerns LSHH400?", DISC("LSHH400"), ["discrepancy_LSHH400_location"]),
 ("D04", "Discrepancies", "What does the plant really have for B300?", VAL("discrepancy_B300_pressure", "asBuilt"), ["B300 operates at 3 bar"]),
 ("H01", "HAZOP", "Which HAZOP element covers C400?", COV("C400"), ["12"]),
 ("H02", "HAZOP", "Which HAZOP element covers K401?", COV("K401"), ["12"]),
 ("H03", "HAZOP", "Which HAZOP element covers J300?", COV("J300"), ["12"]),
 ("H04", "HAZOP", "Which HAZOP deviation concerns PT402?", HDEV("PT402"), ["HAZOP_12_02"]),
 ("H05", "HAZOP", "Which HAZOP deviation concerns FT402 (FT401 in 2010)?", HDEV("FT402"), ["HAZOP_12_07"]),
 ("H06", "HAZOP", "Which HAZOP deviations concern K401 (K400/K401 in 2010)?", HDEV("K401"), ["HAZOP_12_02", "HAZOP_12_08", "HAZOP_12_09"]),
 ("H07", "HAZOP", "Which HAZOP deviations concern C400 (C300 in 2010)?", HDEV("C400"), ["HAZOP_12_03", "HAZOP_12_07"]),
 ("H08", "HAZOP", "Does HAZOP 12.2 recommend a PDAH?", CONTAINS("HAZOP_12_02", "recommendedAction", "PDAH"), ["true"]),
 ("M01", "HMT", "Is the C400 duty above 80 kW (recommended case)?", HMTASK("C400", "duty_kW", ">", 80), ["true"]),
 ("M02", "HMT", "Does C400 cool the gas below 60 C?", HMTASK("C400", "hotOutlet_C", "<", 60), ["true"]),
 ("M03", "HMT", "Is the off-gas more than 85 % CO2 by mass?", HMTASK("K401", "offgasCO2MassFraction", ">", 0.85), ["true"]),
 ("M04", "HMT", "Is the reflux ratio above 3?", HMTASK("K401", "refluxRatio", ">", 3), ["true"]),
 ("M05", "HMT", "Is more liquid condensed than gas sent on?", HMTCMP("K401", "condensate_kg_h", "offgas_kg_h"), ["true"]),
 ("O01", "Open items", "Which open item concerns V317?", OIA("V317"), ["OOI02"]),
 ("O02", "Open items", "Which open items concern K401?", OIA("K401"), ["OOI01", "OOI05", "OOI06"]),
 ("O03", "Open items", "How many open items did this piece raise?", CNTOI("ovh"), ["6"]),
 ("O04", "Open items", "Which open item concerns J300?", OIA("J300"), ["OOI04"]),
 ("X01", "Join", "Is E100 physically connected to K401?", PATH("E100", "pipedTo", "K401"), ["true"]),
 ("X02", "Join", "What feeds V402?", INN("feedsInto", "V402"), ["V403"]),
 ("X03", "Join", "Does the overhead loop pass through V403?", INSTEP(L, "V403"), ["true"]),
 ("X04", "Join", "Does the overhead loop pass through PCV302?", INSTEP(L, "PCV302"), ["true"]),
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
lines = ["# Overhead and reflux KG: 100-question run", "", f"PASS {count['PASS']}, FAIL {count['FAIL']}, QUERY ERROR {count['QUERY ERROR']}", ""]
for qid, cat, question, expect, rows, status, err in results:
    lines += [f"## {qid} [{cat}] {status}", "", f"**{question}**", "", f"- Expected: {', '.join(expect)}"]
    lines += [f"- Error: {err}"] if err else [f"- KG: {', '.join(r[0] for r in rows) or '(no rows)'}"]
    lines.append("")
(HERE / "hundred_results_overhead.md").write_text("\n".join(lines))
for qid, cat, question, expect, rows, status, err in results:
    if status != "PASS":
        print(f"[{qid}] {status} {question}\n      expected: {expect}\n      got: {[r[0] for r in rows]} {err or ''}")
print(f"\nPASS {count['PASS']}, FAIL {count['FAIL']}, QUERY ERROR {count['QUERY ERROR']}  (details in overhead/hundred_results_overhead.md)")
sys.exit(1 if count["FAIL"] or count["QUERY ERROR"] else 0)
