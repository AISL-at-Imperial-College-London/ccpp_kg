"""
Test the joined full-plant KG: the joins between sections, the figure-of-eight route,
and whole-plant consistency. Expected answers come from the documents.
Run from the repo root (after ccpp/build_full_plant.py):   python ccpp/test_full_plant.py
"""
import pathlib
import sys

from rdflib import Graph

ROOT = pathlib.Path(__file__).resolve().parents[1]
NS = "http://imperial.ac.uk/ccpp#"
PRE = f"PREFIX ccpp: <{NS}>\nPREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>\n"
g = Graph()
g.parse(ROOT / "ontology" / "ccpp_ontology.ttl")
g.parse(ROOT / "ccpp" / "full_plant.ttl")

Q = [
 ('J01', 'Join', 'What is FT108 piped to (recirculation and rich side)?',
  'SELECT ?t WHERE { ccpp:FT108 ccpp:pipedTo ?x . ?x ccpp:tag ?t }',
  ['FT109', 'V151']),
 ('J02', 'Join', 'What is V151 piped to?',
  'SELECT ?t WHERE { ccpp:V151 ccpp:pipedTo ?x . ?x ccpp:tag ?t }',
  ['C100']),
 ('J03', 'Join', 'What is piped into C100 (lean and rich sides)?',
  'SELECT ?t WHERE { ?x ccpp:pipedTo ccpp:C100 ; ccpp:tag ?t . }',
  ['V112', 'V151']),
 ('J04', 'Join', 'What is C100 piped to (lean and rich sides)?',
  'SELECT ?t WHERE { ccpp:C100 ccpp:pipedTo ?x . ?x ccpp:tag ?t }',
  ['V113a', 'SDV152']),
 ('J05', 'Join', 'What does SDV152 feed?',
  'SELECT ?t WHERE { ccpp:SDV152 ccpp:pipedTo ?x . ?x ccpp:tag ?t }',
  ['H200a', 'H200b']),
 ('J06', 'Join', 'Where does the lean line join the absorber section?',
  'SELECT ?t WHERE { ccpp:SDV123 ccpp:pipedTo ?x . ?x ccpp:tag ?t }',
  ['V119b']),
 ('J07', 'Join', 'Is E101 physically connected to E100 (rich side)?',
  'ASK { ccpp:E101 ccpp:pipedTo+ ccpp:E100 }',
  ['true']),
 ('J08', 'Join', 'Is E100 physically connected to E101 (lean side)?',
  'ASK { ccpp:E100 ccpp:pipedTo+ ccpp:E101 }',
  ['true']),
 ('F01', 'Figure-of-eight', 'After FT108, where does the rich MEA go in normal running?',
  'SELECT DISTINCT ?t WHERE { ccpp:FigureOfEight ccpp:hasStep ?a . ?a ccpp:stepItem ccpp:FT108 ; ccpp:nextStep ?b . ?b ccpp:stepItem ?x . ?x ccpp:tag ?t }',
  ['V151']),
 ('F02', 'Figure-of-eight', 'After SDV152, where does it go?',
  'SELECT DISTINCT ?t WHERE { ccpp:FigureOfEight ccpp:hasStep ?a . ?a ccpp:stepItem ccpp:SDV152 ; ccpp:nextStep ?b . ?b ccpp:stepItem ?x . ?x ccpp:tag ?t }',
  ['H200a', 'H200b']),
 ('F03', 'Figure-of-eight', 'After V402, is the next step an untagged item (the E100 top nozzle)?',
  'SELECT DISTINCT ?t WHERE { ccpp:FigureOfEight ccpp:hasStep ?a . ?a ccpp:stepItem ccpp:V402 ; ccpp:nextStep ?b . ?b ccpp:stepItem ?x . ?x ccpp:tag ?t }',
  []),
 ('F04', 'Figure-of-eight', 'After FT104, where does the lean MEA go in normal running?',
  'SELECT DISTINCT ?t WHERE { ccpp:FigureOfEight ccpp:hasStep ?a . ?a ccpp:stepItem ccpp:FT104 ; ccpp:nextStep ?b . ?b ccpp:stepItem ?x . ?x ccpp:tag ?t }',
  ['SDV123']),
 ('F05', 'Figure-of-eight', 'After SDV123, where does it go?',
  'SELECT DISTINCT ?t WHERE { ccpp:FigureOfEight ccpp:hasStep ?a . ?a ccpp:stepItem ccpp:SDV123 ; ccpp:nextStep ?b . ?b ccpp:stepItem ?x . ?x ccpp:tag ?t }',
  ['V119b']),
 ('F06', 'Figure-of-eight', 'After C200, what comes next?',
  'SELECT DISTINCT ?t WHERE { ccpp:FigureOfEight ccpp:hasStep ?a . ?a ccpp:stepItem ccpp:C200 ; ccpp:nextStep ?b . ?b ccpp:stepItem ?x . ?x ccpp:tag ?t }',
  ['NRV400']),
 ('F07', 'Figure-of-eight', 'Does the figure-of-eight route close back to E101?',
  'ASK { ccpp:FigureOfEight ccpp:hasStep ?a , ?b . ?a ccpp:stepIndex 0 . ?b ccpp:stepItem ccpp:E101 . ?a ccpp:nextStep+ ?b }',
  ['true']),
 ('F08', 'Figure-of-eight', 'How many times does the route pass through C100?',
  'SELECT (COUNT(?s) AS ?n) WHERE { ccpp:FigureOfEight ccpp:hasStep ?s . ?s ccpp:stepItem ccpp:C100 }',
  ['2']),
 ('F09', 'Figure-of-eight', 'Which shutdown valves are open in normal running?',
  'SELECT ?t WHERE { ccpp:FigureOfEight ccpp:hasValveSetting ?s . ?s ccpp:requiredPosition "open" ; ccpp:valve ?v . ?v a/rdfs:subClassOf* ccpp:ShutdownValve ; ccpp:tag ?t }',
  ['SDV123', 'SDV152']),
 ('F10', 'Figure-of-eight', 'Which shutdown valve is closed in normal running?',
  'SELECT ?t WHERE { ccpp:FigureOfEight ccpp:hasValveSetting ?s . ?s ccpp:requiredPosition "closed" ; ccpp:valve ?v . ?v a/rdfs:subClassOf* ccpp:ShutdownValve ; ccpp:tag ?t }',
  ['SDV125']),
 ('F11', 'Figure-of-eight', 'Which valves are closed in normal running?',
  'SELECT ?t WHERE { ccpp:FigureOfEight ccpp:hasValveSetting ?s . ?s ccpp:requiredPosition "closed" ; ccpp:valve/ccpp:tag ?t }',
  ['SDV125', 'V124', 'V150', 'V319', 'V315', 'V134b', 'V135b', 'V143b', 'V144b', 'V198a', 'V198b', 'V212', 'V217', 'V120', 'V309']),
 ('F12', 'Figure-of-eight', 'How many valves does the figure-of-eight line-up open?',
  'SELECT (COUNT(?s) AS ?n) WHERE { ccpp:PROC_figure_of_eight_lineup ccpp:hasProcedureStep ?s . ?s ccpp:requiredPosition "open" }',
  ['21']),
 ('F13', 'Figure-of-eight', 'How many valves does the figure-of-eight line-up close?',
  'SELECT (COUNT(?s) AS ?n) WHERE { ccpp:PROC_figure_of_eight_lineup ccpp:hasProcedureStep ?s . ?s ccpp:requiredPosition "closed" }',
  ['21']),
 ('R01', 'Rich side', 'What does TT112 measure?',
  'SELECT ?v WHERE { ccpp:TT112 ccpp:measuredVariable ?v }',
  ['rich MEA leaving E101 and entering C100']),
 ('R02', 'Rich side', 'What signal does TT113 use?',
  'SELECT ?v WHERE { ccpp:TT113 ccpp:signalType ?v }',
  ['Profibus-PA']),
 ('R03', 'Rich side', 'Which temperature transmitters are on C100?',
  'SELECT ?t WHERE { ?x ccpp:monitors ccpp:C100 ; ccpp:tag ?t . ?x a/rdfs:subClassOf* ccpp:TemperatureInstrument . }',
  ['TT104', 'TE105', 'TT112', 'TT113']),
 ('R04', 'Rich side', 'What grid reference is SDV152 at?',
  'SELECT ?v WHERE { ccpp:SDV152 ccpp:gridReference ?v }',
  ['L9']),
 ('R05', 'Rich side', 'Which HAZOP element covers SDV152?',
  'SELECT ?el WHERE { ?e a ccpp:HazopElement ; ccpp:covers ccpp:SDV152 ; ccpp:elementNumber ?el }',
  ['8']),
 ('R06', 'Rich side', 'Which open item concerns V319?',
  'SELECT ?o WHERE { ?o a ccpp:OpenItem ; ccpp:about ccpp:V319 }',
  ['ROI02']),
 ('W01', 'Whole plant', 'Which pumps are in the plant so far?',
  'SELECT ?t WHERE { ?x a/rdfs:subClassOf* ccpp:Pump ; ccpp:tag ?t }',
  ['J100', 'J101a', 'J101b', 'J300', 'J104']),
 ('W02', 'Whole plant', 'Which shutdown valves are in the plant so far?',
  'SELECT ?t WHERE { ?x a/rdfs:subClassOf* ccpp:ShutdownValve ; ccpp:tag ?t }',
  ['SDV123', 'SDV125', 'SDV152', 'SDV170']),
 ('W03', 'Whole plant', 'Which check valves are in the plant so far?',
  'SELECT ?t WHERE { ?x a/rdfs:subClassOf* ccpp:CheckValve ; ccpp:tag ?t }',
  ['V112', 'V113a', 'NRV400', 'NRV101', 'NRV102', 'NRV111']),
 ('W04', 'Whole plant', 'How many control loops are there?',
  'SELECT (COUNT(DISTINCT ?x) AS ?n) WHERE { ?x a/rdfs:subClassOf* ccpp:ControlLoop }',
  ['17']),
 ('W05', 'Whole plant', 'How many source documents are there?',
  'SELECT (COUNT(DISTINCT ?x) AS ?n) WHERE { ?x a/rdfs:subClassOf* ccpp:SourceDocument }',
  ['10']),
 ('W06', 'Whole plant', 'Does any item have two different tags?',
  'SELECT ?x WHERE { ?x ccpp:tag ?a , ?b . FILTER(?a != ?b) }',
  []),
 ('W07', 'Whole plant', 'Is any plant item missing a citation?',
  'SELECT ?t WHERE { ?i a/rdfs:subClassOf* ccpp:PlantItem ; ccpp:tag ?t . FILTER NOT EXISTS { ?i ccpp:citedIn ?c } }',
  []),
 ('W08', 'Whole plant', 'What positions does the KG hold for V217 (one per operating mode)?',
  'SELECT ?v WHERE { ccpp:V217 ccpp:normalPosition ?v }',
  ['open', 'closed']),
 ('W09', 'Whole plant', 'How many open items are there across the plant?',
  'SELECT (COUNT(DISTINCT ?x) AS ?n) WHERE { ?x a/rdfs:subClassOf* ccpp:OpenItem }',
  ['46']),
]


def norm(x):
    x = str(x).strip().replace(NS, "")
    try:
        return repr(float(x))
    except ValueError:
        return x


failures = 0
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
    if status != "PASS":
        failures += 1
    print(f"[{qid}] {status:11s} {question}")
    if status != "PASS":
        print(f"            expected: {expect}\n            got: {[r[0] for r in rows]} {err or ''}")

try:
    from pyshacl import validate
    ok, _, report = validate(g, shacl_graph=str(ROOT / "stripping_loop" / "shapes.ttl"), inference="rdfs")
    print("\nSHACL validation:", "PASS" if ok else "FAIL")
    if not ok:
        failures += 1
        print(report[:3000])
except ImportError:
    print("\npyshacl not installed, skipping SHACL validation")

print(f"\n{len(Q)} questions, {failures} failure(s)")
sys.exit(1 if failures else 0)
