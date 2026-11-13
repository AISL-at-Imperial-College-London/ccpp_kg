"""
Ask the safety logic KG (piece 14) questions whose expected answers come from the cause and effect matrix (Rev 5) and
the relief valve schedule: what each trip detects, its set point, and what it stops, closes or opens. Runs on the full plant.
Run from the repo root (after ccpp/build_full_plant.py):   python safety_logic/ask_100_safety_logic.py
Output: safety_logic/hundred_results_safety_logic.md
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


P = "sfl"
Q = [
 ("R01","Register","Which trips does the cause and effect matrix define?", CLSP("SafetyTrip",P), ["TRIP_AZALL101", "TRIP_FALL301", "TRIP_HSZ", "TRIP_LAHH104", "TRIP_LALL104", "TRIP_LSHH100", "TRIP_LSHH103", "TRIP_LSHH107", "TRIP_LSHH110", "TRIP_LSHH111", "TRIP_LSHH112", "TRIP_LSHH116", "TRIP_LSHH400", "TRIP_LSHH403", "TRIP_LSHH404", "TRIP_LSLL102", "TRIP_LSLL105", "TRIP_LSLL109", "TRIP_LSLL112", "TRIP_LSLL114", "TRIP_LSLL402", "TRIP_LZALL405", "TRIP_PAHH401", "TRIP_PALL401", "TRIP_PSHH116", "TRIP_PSHH117", "TRIP_PSHH400", "TRIP_PSHH405", "TRIP_PZALL101", "TRIP_TSHH106", "TRIP_TSHH111a", "TRIP_TSHH111b", "TRIP_TSHH114", "TRIP_TSHH115", "TRIP_TSHH116", "TRIP_TSHH212a", "TRIP_TSHH212b", "TRIP_TSHH310", "TRIP_YS100", "TRIP_YS101"]),
 ("R02","Register","Which relief valves are in the relief valve schedule?", CLSP("ReliefScheduleEntry",P), ["RS_RV100", "RS_RV101", "RS_RV102", "RS_RV103", "RS_RV104", "RS_RV105", "RS_RV106a", "RS_RV106b", "RS_RV107", "RS_RV300", "RS_RV400"]),
 ("R03","Register","How many open items does this piece raise?", CNTOI(P), ["8"]),
 ("W01","Who acts on what","Which trips stop the filling pump J105?", WHO("stops","J105"), ["TRIP_AZALL101", "TRIP_HSZ", "TRIP_LSHH110", "TRIP_LSHH111", "TRIP_LSHH112", "TRIP_LSHH116", "TRIP_LSHH400", "TRIP_LSHH403", "TRIP_LSHH404", "TRIP_LSLL112", "TRIP_LSLL114", "TRIP_LZALL405", "TRIP_PSHH116", "TRIP_PSHH117", "TRIP_PSHH400", "TRIP_PSHH405", "TRIP_TSHH111a", "TRIP_TSHH111b", "TRIP_TSHH114", "TRIP_TSHH115", "TRIP_TSHH116", "TRIP_TSHH310", "TRIP_YS100", "TRIP_YS101"]),
 ("W02","Who acts on what","Which trips stop heater H200a?", WHO("stops","H200a"), ["TRIP_AZALL101", "TRIP_HSZ", "TRIP_LSHH110", "TRIP_LSHH116", "TRIP_LSHH400", "TRIP_LSHH403", "TRIP_LSHH404", "TRIP_LZALL405", "TRIP_PSHH116", "TRIP_PSHH117", "TRIP_PSHH400", "TRIP_PSHH405", "TRIP_TSHH111a", "TRIP_TSHH111b", "TRIP_TSHH114", "TRIP_TSHH115", "TRIP_TSHH212a", "TRIP_TSHH310"]),
 ("W03","Who acts on what","Which trips stop the CO2 compressor J103?", WHO("stops","J103"), ["TRIP_AZALL101", "TRIP_FALL301", "TRIP_HSZ", "TRIP_LSHH103", "TRIP_LSHH107", "TRIP_LSHH110", "TRIP_LSHH116", "TRIP_LSHH400", "TRIP_LSHH403", "TRIP_LSHH404", "TRIP_LZALL405", "TRIP_PSHH116", "TRIP_PSHH117", "TRIP_PSHH400", "TRIP_PSHH405", "TRIP_TSHH111a", "TRIP_TSHH111b", "TRIP_TSHH114", "TRIP_TSHH115", "TRIP_TSHH310"]),
 ("W04","Who acts on what","Which trips close the steam supply valve XV140?", WHO("closes","XV140"), ["TRIP_AZALL101", "TRIP_HSZ", "TRIP_LSHH100", "TRIP_LSHH107", "TRIP_LSHH110", "TRIP_LSHH116", "TRIP_LSHH400", "TRIP_LSHH403", "TRIP_LSHH404", "TRIP_LSLL102", "TRIP_LSLL109", "TRIP_LZALL405", "TRIP_PSHH116", "TRIP_PSHH117", "TRIP_PSHH400", "TRIP_PSHH405", "TRIP_PZALL101", "TRIP_TSHH111a", "TRIP_TSHH111b", "TRIP_TSHH114", "TRIP_TSHH115", "TRIP_TSHH310"]),
 ("W05","Who acts on what","What opens the C400 vent valve SDV421?", WHO("opens","SDV421"), ["TRIP_PAHH401"]),
 ("W06","Who acts on what","What opens the vacuum breaker SDV424?", WHO("opens","SDV424"), ["TRIP_PALL401"]),
 ("W07","Who acts on what","Which trips stop the K101 water pump J104?", WHO("stops","J104"), ["TRIP_AZALL101", "TRIP_HSZ", "TRIP_LSHH103", "TRIP_LSHH110", "TRIP_LSHH116", "TRIP_LSHH400", "TRIP_LSHH403", "TRIP_LSHH404", "TRIP_LSLL105", "TRIP_LZALL405", "TRIP_PSHH116", "TRIP_PSHH117", "TRIP_PSHH400", "TRIP_PSHH405", "TRIP_TSHH111a", "TRIP_TSHH111b", "TRIP_TSHH114", "TRIP_TSHH115", "TRIP_TSHH310"]),
 ("E01","Effects","Does the E100 bottom pressure trip stop every pump and close the steam and supply valves?", ALL(("TRIP_PSHH116","stops","J100"),("TRIP_PSHH116","stops","J103"),("TRIP_PSHH116","stops","H200a"),("TRIP_PSHH116","closes","XV140"),("TRIP_PSHH116","closes","XV128"),("TRIP_PSHH116","closes","FCV110")), ["true"]),
 ("E02","Effects","Does a J100 over-temperature stop J100?", DIRECT("TRIP_TSHH106","stops","J100"), ["true"]),
 ("E03","Effects","Does a J100 over-temperature also stop J101a (it should not)?", DIRECT("TRIP_TSHH106","stops","J101a"), ["false"]),
 ("E04","Effects","Does an E101 level HH stop the blower J102?", DIRECT("TRIP_LSHH107","stops","J102"), ["true"]),
 ("E05","Effects","Does an E100 level HH stop the blower J102 (it should not)?", DIRECT("TRIP_LSHH100","stops","J102"), ["false"]),
 ("E06","Effects","Does an E100 level HH close the steam supply valve?", DIRECT("TRIP_LSHH100","closes","XV140"), ["true"]),
 ("E07","Effects","Does a J101a over-temperature stop J300 (full plant shutdown)?", DIRECT("TRIP_TSHH111a","stops","J300"), ["true"]),
 ("E08","Effects","Does low steam pressure close FCV110?", DIRECT("TRIP_PZALL101","closes","FCV110"), ["true"]),
 ("E09","Effects","Does a K101 level LL stop J104?", DIRECT("TRIP_LSLL105","stops","J104"), ["true"]),
 ("E10","Effects","Is SDV170 opened by the operator on excess water in K101?", DIRECT("TRIP_LAHH104","actsOn","SDV170"), ["true"]),
 ("E11","Effects","Is SDV169 opened by the operator when K101 has no water?", DIRECT("TRIP_LALL104","actsOn","SDV169"), ["true"]),
 ("E12","Effects","Does low CO2 return flow stop J103?", DIRECT("TRIP_FALL301","stops","J103"), ["true"]),
 ("E13","Effects","Does a disengaged feed vessel stop J105?", DIRECT("TRIP_YS100","stops","J105"), ["true"]),
 ("S01","Set points","What is the E100 bottom pressure trip set point?", VAL("TRIP_PSHH116","setpointText"), ["2 barg (rising)"]),
 ("S02","Set points","What is the E101 bottom pressure trip set point?", VAL("TRIP_PSHH117","setpointText"), ["3.5 barg (rising)"]),
 ("S03","Set points","What is the low steam pressure trip set point?", VAL("TRIP_PZALL101","setpointText"), ["3.75 barg"]),
 ("S04","Set points","At what oxygen level does the plant trip?", VAL("TRIP_AZALL101","setpointText"), ["19.5%"]),
 ("S05","Set points","What is the H200a heater temperature trip?", VAL("TRIP_TSHH212a","setpointText"), ["250 degC"]),
 ("S06","Set points","What is the J300 temperature trip?", VAL("TRIP_TSHH310","setpointText"), ["60 degC"]),
 ("S07","Set points","What delay is on the E100 level HH trip?", VAL("TRIP_LSHH100","delayText"), ["1min."]),
 ("S08","Set points","What delay is on the C400 level HH trip?", VAL("TRIP_LSHH400","delayText"), ["5mins."]),
 ("S09","Set points","What delay is on the CO2 flow LL trip?", VAL("TRIP_FALL301","delayText"), ["2mins."]),
 ("S10","Set points","Which system handles the stripper pressure HH at 1.5 barg?", VAL("TRIP_PAHH401","handledBy"), ["process control system"]),
 ("S11","Set points","Which system handles the stripper top pressure HH at 2 barg?", VAL("TRIP_PSHH400","handledBy"), ["safety system"]),
 ("S12","Set points","Which switch detects the absorber top pressure HH?", VAL("TRIP_PSHH405","switchTag"), ["PSHH405"]),
 ("N01","Numbers","E101 pressure trip (barg)?", LIM("CE_PSHH117","high"), ["3.5"]),
 ("N02","Numbers","Low steam pressure trip (barg)?", LIM("CE_PZALL101","low"), ["3.75"]),
 ("N03","Numbers","Pressure at which the C400 vent opens (barg)?", LIM("CE_PAHH401","high"), ["1.5"]),
 ("N04","Numbers","Pressure at which the vacuum breaker opens (barg)?", LIM("CE_PALL401","low"), ["-0.05"]),
 ("N05","Numbers","K101 excess water level (%)?", LIM("CE_LAHH104","high"), ["55"]),
 ("N06","Numbers","J103 temperature trip (degC)?", LIM("CE_TSHH115","high"), ["85"]),
 ("N07","Numbers","RV104 set pressure (bar)?", LIM("RVSCHED_RV104","high"), ["1"]),
 ("N08","Numbers","RV400 set pressure (bar)?", LIM("RVSCHED_RV400","high"), ["3.8"]),
 ("N09","Numbers","RV103 set pressure (bar)?", LIM("RVSCHED_RV103","high"), ["10"]),
 ("N10","Numbers","RV105 set pressure (bar)?", LIM("RVSCHED_RV105","high"), ["3.8"]),
 ("C01","Text","Is the emergency stop a full plant shutdown?", CONTAINS("TRIP_HSZ","actionText","FULL PLANT SHUTDOWN"), ["true"]),
 ("C02","Text","Is a J100 over-temperature a full plant shutdown (it is not)?", CONTAINS("TRIP_TSHH106","actionText","FULL PLANT SHUTDOWN"), ["false"]),
 ("C03","Text","Does a full shutdown set all control loops to manual at 0%?", CONTAINS("TRIP_PSHH400","actionText","all control loops to manual, output 0%"), ["true"]),
 ("C04","Text","Does the CO2 flow trip have a start-up override?", CONTAINS("TRIP_FALL301","triggerCondition","try it three times"), ["true"]),
 ("G01","Safeguards","Is E100 pressure safeguarded by both pressure trips and the vent and vacuum actions?", ALL(("V_E100_P","safeguardedBy","TRIP_PSHH116"),("V_E100_P","safeguardedBy","TRIP_PSHH400"),("V_E100_P","safeguardedBy","TRIP_PAHH401"),("V_E100_P","safeguardedBy","TRIP_PALL401")), ["true"]),
 ("G02","Safeguards","Is the E101 level safeguarded by its HH and LL trips?", ALL(("V_E101_L","safeguardedBy","TRIP_LSHH107"),("V_E101_L","safeguardedBy","TRIP_LSLL109")), ["true"]),
 ("G03","Safeguards","Is the steam flow safeguarded by the low steam pressure trip?", ALL(("V_STEAM","safeguardedBy","TRIP_PZALL101")), ["true"]),
 ("D01","Detection","Is the K102 level HH detected at K102, and the K103 level HH at K103?", ALL(("TRIP_LSHH110","detectedAt","K102"),("TRIP_LSHH116","detectedAt","K103")), ["true"]),
 ("D02","Detection","Is the CO2 flow LL detected by FT301 and FT302?", ALL(("TRIP_FALL301","detectedAt","FT301"),("TRIP_FALL301","detectedAt","FT302")), ["true"]),
 ("V01","Relief","What is RV100's set pressure in the schedule?", VAL("RS_RV100","setPressureText"), ["3.8 bar"]),
 ("V02","Relief","Who supplied RV400?", VAL("RS_RV400","supplier"), ["Leser Valves"]),
 ("V03","Relief","Is the schedule entry for RV300 linked to RV300?", ALL(("RS_RV300","scheduleFor","RV300")), ["true"]),
 ("V04","Relief","Does the schedule include RV106a (absent on the plant per the differences document)?", VAL("RS_RV106a","setPressureText"), ["10 bar"]),
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
lines = ["# Safety logic KG: question run", "", f"PASS {count['PASS']}, FAIL {count['FAIL']}, QUERY ERROR {count['QUERY ERROR']}", ""]
for qid, cat, question, expect, rows, status, err in results:
    lines += [f"## {qid} [{cat}] {status}", "", f"**{question}**", "", f"- Expected: {', '.join(expect)}"]
    lines += [f"- Error: {err}"] if err else [f"- KG: {', '.join(r[0] for r in rows) or '(no rows)'}"]
    lines.append("")
(HERE / "hundred_results_safety_logic.md").write_text("\n".join(lines))
for qid, cat, question, expect, rows, status, err in results:
    if status != "PASS":
        print(f"[{qid}] {status} {question}\n      expected: {expect}\n      got: {[r[0] for r in rows]} {err or ''}")
print(f"\nPASS {count['PASS']}, FAIL {count['FAIL']}, QUERY ERROR {count['QUERY ERROR']}  (details in safety_logic/hundred_results_safety_logic.md)")
sys.exit(1 if count["FAIL"] or count["QUERY ERROR"] else 0)
