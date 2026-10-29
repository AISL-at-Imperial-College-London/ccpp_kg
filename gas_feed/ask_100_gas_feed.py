"""
Ask the feed gas and K101 saturator KG (piece 5) 100 questions whose expected answers come from the
documents (the team then traces and checks it on the P&ID), not from the KG. Piece 5 links to items in other
sections, so the questions run on the joined full plant.
Run from the repo root (after ccpp/build_full_plant.py):   python gas_feed/ask_100_gas_feed.py
Output: gas_feed/hundred_results_gas_feed.md
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
def VAL(s, p): return f"SELECT ?v WHERE {{ {T(s)} {T(p)} ?v }}"
def LIM(l, which): return f"SELECT ?v WHERE {{ {T('limit_' + l)} {T(which + 'Value')} ?v }}"
def ALARM(t): return f"SELECT ?l WHERE {{ ?x ccpp:appliesTo {T(t)} ; ccpp:limitType \"alarm\" ; rdfs:label ?l }}"
def DISC(t): return f"SELECT ?d WHERE {{ ?d a ccpp:PIDDiscrepancy ; ccpp:concerns {T(t)} }}"
def COV(t): return f"SELECT ?el WHERE {{ ?e a ccpp:HazopElement ; ccpp:covers {T(t)} ; ccpp:elementNumber ?el }}"
def HDEV(t): return f"SELECT ?d WHERE {{ ?d a ccpp:HazopDeviation ; ccpp:concerns {T(t)} }}"
def CONTAINS(s, p, text): return f"ASK {{ {T(s)} {T(p)} ?v . FILTER(CONTAINS(STR(?v), \"{text}\")) }}"
def HMTASK(eq, prop, op, v): return (f"ASK {{ ?p ccpp:ofEquipment {T(eq)} ; ccpp:inCase ?c ; {T(prop)} ?x . "
                                     f"?c ccpp:recommendedForUse true . FILTER(?x {op} {v}) }}")
def OIA(t): return f"SELECT ?o WHERE {{ ?o a ccpp:OpenItem ; ccpp:about {T(t)} }}"
def CLSP(c, prefix): return (f"SELECT DISTINCT ?t WHERE {{ ?x a/rdfs:subClassOf* {T(c)} ; ccpp:tag ?t ; ccpp:citedIn ?c . "
                             f"FILTER(CONTAINS(STR(?c), \"__{prefix}cit\")) }}")
def CNTOI(prefix): return f"SELECT (COUNT(?o) AS ?n) WHERE {{ ?o a ccpp:OpenItem ; ccpp:foundBy \"{prefix} section build, Oct 2026\" }}"


P = "gas"
Q = [
 ("F01","Flow","What comes first after the CO2 supply?", OUT("CO2_SUPPLY","feedsInto"), ["V128"]),
 ("F02","Flow","What does V128 feed?", OUT("V128","feedsInto"), ["PCV116"]),
 ("F03","Flow","What does PCV116 feed?", OUT("PCV116","feedsInto"), ["FT105"]),
 ("F04","Flow","What does FT105 feed?", OUT("FT105","feedsInto"), ["FCV105"]),
 ("F05","Flow","What does FCV105 feed?", OUT("FCV105","feedsInto"), ["NRV101"]),
 ("F06","Flow","Where does the CO2 line end?", OUT("NRV101","feedsInto"), ["FEED_GAS_HEADER"]),
 ("F07","Flow","What does V127 feed?", OUT("V127","feedsInto"), ["PCV117"]),
 ("F08","Flow","What does PCV117 feed?", OUT("PCV117","feedsInto"), ["PCV115"]),
 ("F09","Flow","What does PCV115 feed?", OUT("PCV115","feedsInto"), ["FCV116"]),
 ("F10","Flow","What does FCV116 feed?", OUT("FCV116","feedsInto"), ["NRV102"]),
 ("F11","Flow","Which lines meet at the common inlet (the tee)?", INN("feedsInto","FEED_GAS_HEADER"), ["NRV101","NRV102"]),
 ("F12","Flow","Where does the common inlet go (inferred)?", OUT("FEED_GAS_HEADER","feedsInto"), ["K101"]),
 ("F13","Flow","Does the CO2 supply reach E101?", PATH("CO2_SUPPLY","feedsInto","E101"), ["true"]),
 ("F14","Flow","Does the CO2 line feed straight into the N2 line?", DIRECT("FCV105","feedsInto","FCV116"), ["false"]),
 ("P01","Piping","What is PCV116 piped to?", OUT("PCV116","pipedTo"), ["FT105","RV103"]),
 ("P02","Piping","What is PCV117 piped to?", OUT("PCV117","pipedTo"), ["PCV115","RV104"]),
 ("P03","Piping","What is the common inlet piped to?", OUT("FEED_GAS_HEADER","pipedTo"), ["K101"]),
 ("P04","Piping","What is piped into K101?", INN("pipedTo","K101"), ["FEED_GAS_HEADER","C106"]),
 ("P05","Piping","Which tagged item does K101 send water to?", OUT("K101","pipedTo"), ["J104"]),
 ("P06","Piping","What is J104 piped to?", OUT("J104","pipedTo"), ["C106","RV102"]),
 ("P07","Piping","What is C106 piped to?", OUT("C106","pipedTo"), ["K101"]),
 ("P08","Piping","Which equipment is the gas inlet nozzle on?", VAL("E101_N_gas_inlet","onEquipment"), ["E101"]),
 ("E01","Equipment","Which saturator is there?", CLSP("Saturator",P), ["K101"]),
 ("E02","Equipment","Which supply connections are there?", CLSP("SupplyConnection",P), ["CO2_SUPPLY","N2_SUPPLY"]),
 ("E03","Equipment","Which pump does this piece add?", CLSP("Pump",P), ["J104"]),
 ("E04","Equipment","Which check valves does this piece add?", CLSP("CheckValve",P), ["NRV101","NRV102","NRV111"]),
 ("E05","Equipment","Which shutdown valve does this piece add?", CLSP("ShutdownValve",P), ["SDV170"]),
 ("E06","Equipment","Which relief valves does this piece add?", CLSP("ReliefValve",P), ["RV102","RV103","RV104"]),
 ("E07","Equipment","Which flow control valves does this piece add?", CLSP("FlowControlValve",P), ["FCV105","FCV116","FCV111","FCV102"]),
 ("E08","Equipment","Which pressure control valves does this piece add?", CLSP("PressureControlValve",P), ["PCV116","PCV115","PCV117"]),
 ("E09","Equipment","Which cooler does this piece add?", CLSP("TrimCooler",P), ["C106"]),
 ("E10","Equipment","What grid is J104 at?", VAL("J104","gridReference"), ["O18"]),
 ("V01","Valves","What grid is PCV116 at?", VAL("PCV116","gridReference"), ["K22"]),
 ("V02","Valves","What grid is FCV105 at?", VAL("FCV105","gridReference"), ["K21"]),
 ("V03","Valves","What grid is NRV101 at?", VAL("NRV101","gridReference"), ["K21"]),
 ("V04","Valves","What grid is RV103 at?", VAL("RV103","gridReference"), ["K22"]),
 ("V05","Valves","What grid is V127 at?", VAL("V127","gridReference"), ["Q19"]),
 ("V06","Valves","What grid is PCV117 at?", VAL("PCV117","gridReference"), ["P21"]),
 ("V07","Valves","What grid is RV104 at?", VAL("RV104","gridReference"), ["P21"]),
 ("V08","Valves","What grid is PCV115 at?", VAL("PCV115","gridReference"), ["N22"]),
 ("V09","Valves","What grid is FCV116 at?", VAL("FCV116","gridReference"), ["N21"]),
 ("V10","Valves","What grid is NRV102 at?", VAL("NRV102","gridReference"), ["N20"]),
 ("V11","Valves","What grid is FCV111 at?", VAL("FCV111","gridReference"), ["K17"]),
 ("V12","Valves","What grid is FCV102 at?", VAL("FCV102","gridReference"), ["Q16"]),
 ("I01","Instruments","What type of meter is FT105?", VAL("FT105","sensorType"), ["thermal mass flow meter"]),
 ("I02","Instruments","What signal does FT105 use?", VAL("FT105","signalType"), ["4-20mA"]),
 ("I03","Instruments","What grid is FT105 at?", VAL("FT105","gridReference"), ["K21"]),
 ("I04","Instruments","What grid is TT121 at?", VAL("TT121","gridReference"), ["L18"]),
 ("I05","Instruments","What type of sensor is TT121?", VAL("TT121","sensorType"), ["PRT"]),
 ("I06","Instruments","What type of meter is FT106?", VAL("FT106","sensorType"), ["electromagnetic volumetric flow meter"]),
 ("I07","Instruments","What grid is FT106 at?", VAL("FT106","gridReference"), ["R16"]),
 ("I08","Instruments","What type of meter is FT303?", VAL("FT303","sensorType"), ["vortex volumetric flow meter"]),
 ("I09","Instruments","What signal does FT304 use?", VAL("FT304","signalType"), ["Profibus-PA"]),
 ("I10","Instruments","Which floor is FT303 on?", VAL("FT303","floor"), ["3"]),
 ("I11","Instruments","Which temperature instruments are recorded against E101 (now including TT107)?", INN("monitors","E101","TemperatureInstrument"), ["TT107","TT109","TT204","TT205","TT206","TT207","TT305","TT306","TT307","TT308","TT411","TT413"]),
 ("I12","Instruments","Which flow instruments are recorded against E101?", INN("monitors","E101","FlowInstrument"), ["FT108","FI108","DI108","FT109","FI109","FT303","FT304"]),
 ("C01","Control","Which controller acts on FCV105?", INN("controls","FCV105","Controller"), ["FIC105"]),
 ("C02","Control","Which controller acts on FCV116?", INN("controls","FCV116","Controller"), ["FIC116"]),
 ("C03","Control","Which controllers act on FCV111?", INN("controls","FCV111","Controller"), ["FIC303","FIC304"]),
 ("C04","Control","Which controllers act on FCV102?", INN("controls","FCV102","Controller"), ["TIC121","FIC106"]),
 ("C05","Control","Which sensor does the CO2 feed loop use?", OUT("CL_CO2_feed","hasSensor"), ["FT105"]),
 ("C06","Control","Which sensor does the N2 feed loop use?", OUT("CL_N2_feed","hasSensor"), ["FT116"]),
 ("C07","Control","Which sensors does the N2-to-E101 loop use?", OUT("CL_N2_to_E101","hasSensor"), ["FT303","FT304"]),
 ("C08","Control","Which valve does the N2-to-E101 loop move?", OUT("CL_N2_to_E101","hasFinalElement"), ["FCV111"]),
 ("C09","Control","Which sensor does the K101 temperature loop use?", OUT("CL_K101_temperature","hasSensor"), ["TT121"]),
 ("C10","Control","Which loop is the K101 temperature loop master of?", VAL("CL_K101_temperature","cascadeMasterOf"), ["CL_C106_cooling_water"]),
 ("C11","Control","Which sensor does the C106 cooling water loop use?", OUT("CL_C106_cooling_water","hasSensor"), ["FT106"]),
 ("C12","Control","What does the N2-to-E101 loop manipulate?", VAL("CL_N2_to_E101","manipulatedVariable"), ["K101 bypass rate (FCV111)"]),
 ("L01","Limits","What is the top of the PCV116 output range?", LIM("PCV116_output","high"), ["10"]),
 ("L02","Limits","What is the bottom of the PT113 range?", LIM("PT113_range","low"), ["-1"]),
 ("L03","Limits","Which alarm is on the N2 feed?", ALARM("FCV116"), ["FAL_N2_feed"]),
 ("L04","Limits","Which alarms are on K101?", ALARM("K101"), ["LZAH_K101","LAL_K101","LZAL_K101"]),
 ("L05","Limits","What does RV102 protect?", OUT("RV102","protects"), ["J104"]),
 ("L06","Limits","What does RV103 protect (per REPORT grid)?", OUT("RV103","protects"), ["PCV116"]),
 ("L07","Limits","What does RV104 protect (per REPORT grid)?", OUT("RV104","protects"), ["PCV117"]),
 ("B01","Bypass","What is SDV170 piped to?", OUT("SDV170","pipedTo"), ["FCV111"]),
 ("B02","Bypass","What is FCV111 piped to?", OUT("FCV111","pipedTo"), ["NRV111"]),
 ("B03","Bypass","Which equipment is the NRV111 base inlet on?", VAL("E101_N_base_inlet","onEquipment"), ["E101"]),
 ("D01","Discrepancies","Which discrepancy concerns the CO2 supply?", DISC("CO2_SUPPLY"), ["discrepancy_CO2_supply_label"]),
 ("D02","Discrepancies","What is the CO2 supply line really named?", VAL("discrepancy_CO2_supply_label","asBuilt"), ["Named 'compressed air'"]),
 ("H01","HAZOP","Which HAZOP element covers V128?", COV("V128"), ["1"]),
 ("H02","HAZOP","Which HAZOP element covers V127?", COV("V127"), ["2"]),
 ("H03","HAZOP","Which HAZOP element covers K101?", COV("K101"), ["3"]),
 ("H04","HAZOP","Which HAZOP element covers J104?", COV("J104"), ["4"]),
 ("H05","HAZOP","Which HAZOP deviations concern FCV105?", HDEV("FCV105"), ["HAZOP_1_03","HAZOP_1_06"]),
 ("H06","HAZOP","Which HAZOP deviations concern PCV116?", HDEV("PCV116"), ["HAZOP_1_07","HAZOP_1_08"]),
 ("H07","HAZOP","Which HAZOP deviations concern PCV117?", HDEV("PCV117"), ["HAZOP_2_05","HAZOP_2_08","HAZOP_2_10"]),
 ("H08","HAZOP","Which HAZOP deviation concerns RV102?", HDEV("RV102"), ["HAZOP_4_03"]),
 ("H09","HAZOP","Which HAZOP deviations concern K101?", HDEV("K101"), ["HAZOP_3_05","HAZOP_4_02","HAZOP_4_06","HAZOP_4_07"]),
 ("H10","HAZOP","Was a bypass line added after HAZOP 1.2?", CONTAINS("HAZOP_1_02","actionTaken","Bypass line added"), ["true"]),
 ("M01","HMT","Is the recommended-case feed gas flow above 400 kg/h?", HMTASK("E101","feedMassFlow_kg_h",">",400), ["true"]),
 ("M02","HMT","Is the recommended-case feed below 10 % CO2 by mass?", HMTASK("E101","feedCO2MassFraction","<",0.1), ["true"]),
 ("M03","HMT","Does the feed gas enter below 45 C?", HMTASK("E101","feedTemperature_C","<",45), ["true"]),
 ("M04","HMT","Does the feed gas enter above 1.5 bar?", HMTASK("E101","feedPressure_bar",">",1.5), ["true"]),
 ("M05","HMT","What is the feed gas flow in the pilot-scale case (v6.1)?", VAL("aspen_v6_1_feed_gas","feedMassFlow_kg_h"), ["45"]),
 ("O01","Open items","Which open item concerns FCV111?", OIA("FCV111"), ["GOI03"]),
 ("O02","Open items","Which open item concerns RV103?", OIA("RV103"), ["GOI05"]),
 ("O03","Open items","Which open item concerns the CO2 supply?", OIA("CO2_SUPPLY"), ["GOI06"]),
 ("O04","Open items","Which open items concern K101?", OIA("K101"), ["GOI02","GOI07","GOI09"]),
 ("O05","Open items","How many open items did this piece raise?", CNTOI(P), ["9"]),
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
lines = ["# Feed gas KG: 100-question run", "", f"PASS {count['PASS']}, FAIL {count['FAIL']}, QUERY ERROR {count['QUERY ERROR']}", ""]
for qid, cat, question, expect, rows, status, err in results:
    lines += [f"## {qid} [{cat}] {status}", "", f"**{question}**", "", f"- Expected: {', '.join(expect)}"]
    lines += [f"- Error: {err}"] if err else [f"- KG: {', '.join(r[0] for r in rows) or '(no rows)'}"]
    lines.append("")
(HERE / "hundred_results_gas_feed.md").write_text("\n".join(lines))
for qid, cat, question, expect, rows, status, err in results:
    if status != "PASS":
        print(f"[{qid}] {status} {question}\n      expected: {expect}\n      got: {[r[0] for r in rows]} {err or ''}")
print(f"\nPASS {count['PASS']}, FAIL {count['FAIL']}, QUERY ERROR {count['QUERY ERROR']}  (details in gas_feed/hundred_results_gas_feed.md)")
sys.exit(1 if count["FAIL"] or count["QUERY ERROR"] else 0)
