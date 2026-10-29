"""
Ask the absorber overhead KG (piece 6) 100 questions whose expected answers come from the
documents (the team then traces and checks it on the P&ID), not from the KG. Piece 6 links to items in other
sections, so the questions run on the joined full plant.
Run from the repo root (after ccpp/build_full_plant.py):   python abs_overhead/ask_100_abs_overhead.py
Output: abs_overhead/hundred_results_abs_overhead.md
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
def INSTEP(loop, item): return f"ASK {{ {T(loop)} ccpp:hasStep/ccpp:stepItem {T(item)} }}"
def OIA(t): return f"SELECT ?o WHERE {{ ?o a ccpp:OpenItem ; ccpp:about {T(t)} }}"
def CLSP(c, prefix): return (f"SELECT DISTINCT ?t WHERE {{ ?x a/rdfs:subClassOf* {T(c)} ; ccpp:tag ?t ; ccpp:citedIn ?c . "
                             f"FILTER(CONTAINS(STR(?c), \"__{prefix}cit\")) }}")
def CNTOI(prefix): return f"SELECT (COUNT(?o) AS ?n) WHERE {{ ?o a ccpp:OpenItem ; ccpp:foundBy \"{prefix} section build, Oct 2026\" }}"


P = "aov"
L = "AbsorberOverheadRoute"
Q = [
 ("F01","Flow","Where does the gas go after leaving the top of E101?", OUT("E101_N_gas_outlet","feedsInto"), ["K402"]),
 ("F02","Flow","What does K402 feed on the vent route?", OUT("K402","feedsInto"), ["PCV300"]),
 ("F03","Flow","What does PCV300 feed?", OUT("PCV300","feedsInto"), ["VENT_E101"]),
 ("F04","Flow","What feeds PCV300?", INN("feedsInto","PCV300"), ["K402"]),
 ("F05","Flow","What feeds the absorber vent?", INN("feedsInto","VENT_E101"), ["PCV300"]),
 ("F06","Flow","Does gas from the top of E101 reach the vent?", PATH("E101_N_gas_outlet","feedsInto","VENT_E101"), ["true"]),
 ("F07","Flow","Does K402 feed the vent directly (bypassing PCV300)?", DIRECT("K402","feedsInto","VENT_E101"), ["false"]),
 ("F08","Flow","Does vented gas come back to E101?", PATH("VENT_E101","feedsInto","E101"), ["false"]),
 ("F09","Flow","Does E101 feed its overhead nozzle directly?", DIRECT("E101","feedsInto","E101_N_gas_outlet"), ["true"]),
 ("F10","Flow","Does the overhead route pass through K402?", INSTEP(L,"K402"), ["true"]),
 ("F11","Flow","Does the overhead route include V409?", INSTEP(L,"V409"), ["true"]),
 ("F12","Flow","Does the overhead route include PT403?", INSTEP(L,"PT403"), ["true"]),
 ("P01","Piping","What is K402 piped to (vent line and liquid return)?", OUT("K402","pipedTo"), ["PCV300","E101"]),
 ("P02","Piping","Where does RV400 discharge?", OUT("RV400","pipedTo"), ["K403"]),
 ("P03","Piping","Where does RV401 discharge?", OUT("RV401","pipedTo"), ["K403"]),
 ("P04","Piping","Which relief valves discharge into K403?", INN("pipedTo","K403"), ["RV400","RV401"]),
 ("P05","Piping","Is E101 piped to RV400?", DIRECT("E101","pipedTo","RV400"), ["true"]),
 ("P06","Piping","Which equipment is the N2 return outlet on?", VAL("K402_N_gas_to_return","onEquipment"), ["K402"]),
 ("P07","Piping","Which equipment is the overhead gas outlet on?", VAL("E101_N_gas_outlet","onEquipment"), ["E101"]),
 ("P08","Piping","What is PCV300 piped to?", OUT("PCV300","pipedTo"), ["VENT_E101"]),
 ("E01","Equipment","Which cyclone separator is there?", CLSP("CycloneSeparator",P), ["K402"]),
 ("E02","Equipment","Which knockout drum does this piece add?", CLSP("KnockoutDrum",P), ["K403"]),
 ("E03","Equipment","Which vent connection does this piece add?", CLSP("VentConnection",P), ["VENT_E101"]),
 ("E04","Equipment","Which pressure control valve does this piece add?", CLSP("PressureControlValve",P), ["PCV300"]),
 ("E05","Equipment","Which manual valves does this piece add?", CLSP("ManualValve",P), ["V409","V310","V313","V408"]),
 ("E06","Equipment","Does the K403 note say it collects the RV400 discharge?", CONTAINS("K403","note","RV400"), ["true"]),
 ("E07","Equipment","What grid is K403 at?", VAL("K403","gridReference"), ["E15"]),
 ("E08","Equipment","Which floor is K402 on?", VAL("K402","floor"), ["4"]),
 ("E09","Equipment","Which floor is K403 on?", VAL("K403","floor"), ["4"]),
 ("E10","Equipment","Which floor is the absorber vent on?", VAL("VENT_E101","floor"), ["3"]),
 ("V01","Valves","What grid is PCV300 at?", VAL("PCV300","gridReference"), ["G18"]),
 ("V02","Valves","Which floor is PCV300 on?", VAL("PCV300","floor"), ["3"]),
 ("V03","Valves","Is PCV300 open in normal running?", VAL("PCV300","normalPosition"), ["open"]),
 ("V04","Valves","What type of valve is PCV300?", VAL("PCV300","valveType"), ["pressure control"]),
 ("V05","Valves","What grid is V409 at?", VAL("V409","gridReference"), ["E16"]),
 ("V06","Valves","Which floor is V409 on?", VAL("V409","floor"), ["4"]),
 ("V07","Valves","Is V409 locked?", VAL("V409","hasLockingHandle"), ["true"]),
 ("V08","Valves","Is V409 open in normal running?", VAL("V409","normalPosition"), ["open"]),
 ("V09","Valves","What type of valve is V310?", VAL("V310","valveType"), ["3-way ball"]),
 ("V10","Valves","What grid is V310 at?", VAL("V310","gridReference"), ["F17"]),
 ("V11","Valves","Which floor is V310 on?", VAL("V310","floor"), ["3"]),
 ("V12","Valves","What type of valve is V313?", VAL("V313","valveType"), ["3-way ball"]),
 ("V13","Valves","What type of valve is V408?", VAL("V408","valveType"), ["needle"]),
 ("V14","Valves","What grid is V408 at?", VAL("V408","gridReference"), ["F16"]),
 ("I01","Instruments","What grid is TT412 at?", VAL("TT412","gridReference"), ["F15"]),
 ("I02","Instruments","Which floor is TT412 on?", VAL("TT412","floor"), ["4"]),
 ("I03","Instruments","What type of sensor is TT412?", VAL("TT412","sensorType"), ["PRT"]),
 ("I04","Instruments","What signal does TT412 use?", VAL("TT412","signalType"), ["Fieldbus"]),
 ("I05","Instruments","What grid is TT413 at?", VAL("TT413","gridReference"), ["E16"]),
 ("I06","Instruments","Which floor is TT413 on?", VAL("TT413","floor"), ["4"]),
 ("I07","Instruments","What signal does TT413 use?", VAL("TT413","signalType"), ["Fieldbus"]),
 ("I08","Instruments","What type of transmitter is PT403?", VAL("PT403","sensorType"), ["gauge pressure transmitter"]),
 ("I09","Instruments","What grid is PT403 at?", VAL("PT403","gridReference"), ["D16"]),
 ("I10","Instruments","What signal does PT403 use?", VAL("PT403","signalType"), ["Fieldbus"]),
 ("I11","Instruments","Which floor is PT403 on?", VAL("PT403","floor"), ["4"]),
 ("I12","Instruments","What type of meter is FT300?", VAL("FT300","sensorType"), ["thermal mass flow meter"]),
 ("I13","Instruments","What grid is FT300 at?", VAL("FT300","gridReference"), ["G18"]),
 ("I14","Instruments","What type of meter is FT301?", VAL("FT301","sensorType"), ["swirl volumetric flow meter"]),
 ("I15","Instruments","What grid is FT301 at?", VAL("FT301","gridReference"), ["G20"]),
 ("I16","Instruments","What signal does FT302 use?", VAL("FT302","signalType"), ["Profibus-DP"]),
 ("I17","Instruments","Which flow meters are on the K402 overhead side?", INN("monitors","K402"), ["FT300","FT301","FT302"]),
 ("I18","Instruments","What does PT403 measure?", VAL("PT403","measuredVariable"), ["absorber (E101) pressure"]),
 ("I19","Instruments","What does PT403 monitor?", OUT("PT403","monitors"), ["E101"]),
 ("I20","Instruments","Which floor is TT411 (top of E101, liquid) on?", VAL("TT411","floor"), ["4"]),
 ("C01","Control","Which controller acts on PCV300?", INN("controls","PCV300","Controller"), ["PIC403"]),
 ("C02","Control","Which sensor does the absorber pressure loop use?", OUT("CL_E101_pressure","hasSensor"), ["PT403"]),
 ("C03","Control","Which controller does the absorber pressure loop use?", OUT("CL_E101_pressure","hasController"), ["PIC403"]),
 ("C04","Control","Which valve does the absorber pressure loop move?", OUT("CL_E101_pressure","hasFinalElement"), ["PCV300"]),
 ("C05","Control","What does the absorber pressure loop control?", VAL("CL_E101_pressure","controlledVariable"), ["Pressure in E101"]),
 ("C06","Control","What does the absorber pressure loop manipulate?", VAL("CL_E101_pressure","manipulatedVariable"), ["Opening of PCV300 (lean gas vent rate)"]),
 ("C07","Control","What does PIC403 control?", OUT("PIC403","controls"), ["PCV300"]),
 ("C08","Control","Is the stripper pressure loop separate (does it act on PCV119, not PCV300)?", OUT("CL_E100_pressure","hasFinalElement"), ["PCV119"]),
 ("S01","Sampling","Which valve serves sample point 1 (assumed)?", OUT("E101_sample_1","sampleValve"), ["V408"]),
 ("S02","Sampling","Which valve serves sample point 2?", OUT("E101_sample_2","sampleValve"), ["V308"]),
 ("S03","Sampling","At what height is sample point 1?", VAL("E101_sample_1","height_m"), ["6.85"]),
 ("D01","Discrepancies","Which discrepancy concerns K403?", DISC("K403"), ["discrepancy_K403_not_on_PID"]),
 ("D02","Discrepancies","Which discrepancy concerns FT301?", DISC("FT301"), ["discrepancy_FT301_FT302_order"]),
 ("D03","Discrepancies","Which discrepancy concerns V310?", DISC("V310"), ["discrepancy_V313_V310_branch"]),
 ("D04","Discrepancies","Where is the V313 branch really connected?", VAL("discrepancy_V313_V310_branch","asBuilt"), ["Branch connected at V310"]),
 ("D05","Discrepancies","What is wrong with FT301 and FT302 on the P&ID?", VAL("discrepancy_FT301_FT302_order","asBuilt"), ["Order reversed"]),
 ("H01","HAZOP","Which HAZOP deviations concern K402?", HDEV("K402"), ["HAZOP_10_01","HAZOP_10_05"]),
 ("H02","HAZOP","Which HAZOP deviations concern PIC403?", HDEV("PIC403"), ["HAZOP_3_02","HAZOP_3_03"]),
 ("H03","HAZOP","Which HAZOP element covers RV400?", COV("RV400"), ["10"]),
 ("H04","HAZOP","Does HAZOP 10.8 say RV400 is sized for the maximum gas filling rate?", CONTAINS("HAZOP_10_08","recommendedAction","size RV400"), ["true"]),
 ("H05","HAZOP","Was gas analysis put on the top floor, above the K402 liquid switch?", CONTAINS("HAZOP_10_05","recommendedAction","above liquid switch on K402"), ["true"]),
 ("H06","HAZOP","Was liquid level detection added downstream of K402?", CONTAINS("HAZOP_10_01","recommendedAction","downstream of K402"), ["true"]),
 ("M01","HMT","Is more than 400 kg/h of gas leaving the top of E101 (recommended case)?", HMTASK("E101","ventGas_kg_h",">",400), ["true"]),
 ("M02","HMT","Is less than 0.1 kg/h of CO2 left in that gas?", HMTASK("E101","ventGasCO2_kg_h","<",0.1), ["true"]),
 ("M03","HMT","Does the gas leave E101 above 50 C?", HMTASK("E101","ventGasTemperature_C",">",50), ["true"]),
 ("M04","HMT","Does the Aspen note say there is no K402 in the model?", CONTAINS("aspen_v3_vent_gas","note","no K402"), ["true"]),
 ("O01","Open items","Which open items concern K402?", OIA("K402"), ["AV01","AV08"]),
 ("O02","Open items","Which open item concerns PCV300?", OIA("PCV300"), ["AV01"]),
 ("O03","Open items","Which open item concerns V310?", OIA("V310"), ["AV03"]),
 ("O04","Open items","Which open item concerns V408?", OIA("V408"), ["AV05"]),
 ("O05","Open items","Which open item concerns K403?", OIA("K403"), ["AV06"]),
 ("O06","Open items","How many open items did this piece raise?", CNTOI(P), ["8"]),
 ("X01","Join","Is E101 connected through RV400 to K403?", PATH("E101","pipedTo","K403"), ["true"]),
 ("X02","Join","Can fresh CO2 travel through the absorber to the vent?", PATH("CO2_SUPPLY","feedsInto","VENT_E101"), ["true"]),
 ("X03","Join","Is the stripper relief RV401 connected to K403?", DIRECT("RV401","pipedTo","K403"), ["true"]),
 ("X04","Join","Does the absorber pressure loop share a valve with the stripper pressure loop?", OUT("CL_E101_pressure","hasFinalElement"), ["PCV300"]),
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
lines = ["# Absorber overhead KG: 100-question run", "", f"PASS {count['PASS']}, FAIL {count['FAIL']}, QUERY ERROR {count['QUERY ERROR']}", ""]
for qid, cat, question, expect, rows, status, err in results:
    lines += [f"## {qid} [{cat}] {status}", "", f"**{question}**", "", f"- Expected: {', '.join(expect)}"]
    lines += [f"- Error: {err}"] if err else [f"- KG: {', '.join(r[0] for r in rows) or '(no rows)'}"]
    lines.append("")
(HERE / "hundred_results_abs_overhead.md").write_text("\n".join(lines))
for qid, cat, question, expect, rows, status, err in results:
    if status != "PASS":
        print(f"[{qid}] {status} {question}\n      expected: {expect}\n      got: {[r[0] for r in rows]} {err or ''}")
print(f"\nPASS {count['PASS']}, FAIL {count['FAIL']}, QUERY ERROR {count['QUERY ERROR']}  (details in abs_overhead/hundred_results_abs_overhead.md)")
sys.exit(1 if count["FAIL"] or count["QUERY ERROR"] else 0)
