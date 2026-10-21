"""Ask the stripping loop KG 100 questions and record how it does.

Each question has an expectation:
  [values]  exact answer expected (first column, order ignored)  -> PASS / FAIL
  []        expect no rows                                       -> PASS / FAIL
  "ANY"     a real answer should exist; shown for review         -> ANSWERED / NO ANSWER
  "GAP"     probing something we think the KG cannot answer     -> GAP CONFIRMED / ANSWERED
Usage (from the repo root):  python stripping_loop/ask_100.py
Output: stripping_loop/hundred_results.md
"""
import collections
import pathlib

from rdflib import Graph

HERE = pathlib.Path(__file__).resolve().parent
NS = "http://imperial.ac.uk/ccpp#"
PRE = f"PREFIX ccpp: <{NS}>\nPREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>\n"
g = Graph()
g.parse(HERE.parent / "ontology" / "ccpp_ontology.ttl")
g.parse(HERE / "stripping_loop.ttl")

REC = "?c ccpp:recommendedForUse true ."
Q = [
 # ---------------- Routes and scenarios ----------------
 ("R01", "Routes", "How many route scenarios does the stripping loop have?",
  "SELECT (COUNT(?r) AS ?n) WHERE { ?r a ccpp:RouteScenario }", ["4"]),
 ("R02", "Routes", "Which route is the normal line-up?",
  "SELECT ?r WHERE { ?r a ccpp:RouteScenario ; ccpp:isNormalRoute true }", ["Route_A_top_filter"]),
 ("R03", "Routes", "Which routes bypass Z102?",
  "SELECT ?r WHERE { ?r a ccpp:RouteScenario ; ccpp:usesFilter false }", ["Route_B_top_bypass", "Route_D_side_bypass"]),
 ("R04", "Routes", "Which routes return to the side of E100 (stage 3)?",
  "SELECT ?r WHERE { ?r a ccpp:RouteScenario ; ccpp:returnsToStage/ccpp:stageNumber 3 }", ["Route_C_side_filter", "Route_D_side_bypass"]),
 ("R05", "Routes", "Which valve is open for the side return but closed in the normal route?",
  "SELECT ?tag WHERE { ccpp:Route_C_side_filter ccpp:hasValveSetting ?s . ?s ccpp:requiredPosition \"open\" ; ccpp:valve/ccpp:tag ?tag . "
  "ccpp:Route_A_top_filter ccpp:hasValveSetting ?s2 . ?s2 ccpp:valve/ccpp:tag ?tag ; ccpp:requiredPosition \"closed\" }", ["V309"]),
 ("R06", "Routes", "In route D, which key valves are closed?",
  "SELECT ?tag WHERE { ccpp:Route_D_side_bypass ccpp:hasValveSetting ?s . ?s ccpp:requiredPosition \"closed\" ; ccpp:valve/ccpp:tag ?tag }",
  ["V117a", "V117b", "V403", "V402", "V318", "V302", "SDV123"]),
 ("R07", "Routes", "In route C, which tagged items does the solvent pass after SDV125?",
  "SELECT DISTINCT ?tag WHERE { ccpp:Route_C_side_filter ccpp:hasStep ?a , ?b . ?a ccpp:stepItem ccpp:SDV125 ; ccpp:stepIndex ?ia . "
  "?b ccpp:stepIndex ?ib ; ccpp:stepType \"inline\" ; ccpp:stepItem ?x . ?x ccpp:tag ?tag . FILTER(?ib > ?ia) }", ["H200a", "H200b", "V309", "E100"]),
 ("R08", "Routes", "Does route B pass through Z102?",
  "ASK { ccpp:Route_B_top_bypass ccpp:hasStep/ccpp:stepItem ccpp:Z102 }", ["false"]),
 ("R10", "Routes", "Does route D pass through both V120 and V309?",
  "ASK { ccpp:Route_D_side_bypass ccpp:hasStep/ccpp:stepItem ccpp:V120 , ccpp:V309 }", ["true"]),
 ("R12", "Routes", "Which instruments sit at the stage where the side return enters?",
  "SELECT ?tag WHERE { ccpp:E100_N_side_inlet ccpp:atStage ?s . ?i ccpp:locatedAtStage ?s ; ccpp:tag ?tag }", ["TT302", "TT303"]),
 ("R13", "Routes", "Which tagged items are in route A but not route C?",
  "SELECT DISTINCT ?tag WHERE { ccpp:Route_A_top_filter ccpp:hasStep/ccpp:stepItem ?x . ?x ccpp:tag ?tag . "
  "FILTER NOT EXISTS { ccpp:Route_C_side_filter ccpp:hasStep/ccpp:stepItem ?x } }", ["V403", "V402"]),
 ("R14", "Routes", "Is the side return simulated in Aspen?",
  "SELECT ?note WHERE { ccpp:Route_C_side_filter ccpp:note ?note }", "ANY"),
 ("R15", "Routes", "What triggers moving from route A to route B?",
  "SELECT ?t WHERE { ccpp:Z102_bypass ccpp:activatedBy/ccpp:triggerCondition ?t }", ["PDT105 at or above 0.45 bar (Z102 blocked)"]),
 ("R19", "Routes", "Is V309 covered by the HAZOP?",
  "ASK { ?e a ccpp:HazopElement ; ccpp:covers ccpp:V309 }", ["false"]),
 ("R20", "Routes", "What is the rich loading for the side-return route?",
  "SELECT ?x WHERE { ?p ccpp:ofEquipment ccpp:E100 ; ccpp:inCase ?case ; ccpp:richLoading_mol_mol ?x . ?case ccpp:representsMode ?m . "
  "ccpp:Route_C_side_filter ccpp:inMode ?m }", "GAP"),
 # ---------------- Topology ----------------
 ("T01", "Topology", "What does Z102 feed directly into?", "SELECT ?tag WHERE { ccpp:Z102 ccpp:feedsInto ?x . ?x ccpp:tag ?tag }", ["V117b"]),
 ("T02", "Topology", "What feeds directly into Z102?", "SELECT ?tag WHERE { ?x ccpp:feedsInto ccpp:Z102 ; ccpp:tag ?tag }", ["V117a"]),
 ("T03", "Topology", "What feeds directly into J100?", "SELECT ?tag WHERE { ?x ccpp:feedsInto ccpp:J100 ; ccpp:tag ?tag }", ["V113b"]),
 ("T06", "Topology", "What does H100 feed directly into?", "SELECT ?tag WHERE { ccpp:H100 ccpp:feedsInto ?x . ?x ccpp:tag ?tag }", ["Q106"]),
 ("T08", "Topology", "Is V121 downstream of Z102 on the active path?", "ASK { ccpp:Z102 ccpp:feedsInto+ ccpp:V121 }", ["true"]),
 ("T09", "Topology", "Is SDV123 on the active flow path?", "ASK { ccpp:E100 ccpp:feedsInto+ ccpp:SDV123 }", ["false"]),
 ("T10", "Topology", "What does SDV125 feed directly into?", "SELECT ?tag WHERE { ccpp:SDV125 ccpp:feedsInto ?x . ?x ccpp:tag ?tag }", ["H200a", "H200b"]),
 ("T12", "Topology", "Which items is V116 physically piped to?", "SELECT ?tag WHERE { ccpp:V116 ccpp:pipedTo ?x . ?x ccpp:tag ?tag }", ["V117a", "V120"]),
 ("T13", "Topology", "Where can flow physically go after H200a?", "SELECT DISTINCT ?tag WHERE { ccpp:H200a ccpp:pipedTo ?x . ?x ccpp:tag ?tag }", ["V403", "V309"]),
 ("T14", "Topology", "How many inline steps does the normal loop have?",
  "SELECT (COUNT(?s) AS ?n) WHERE { ccpp:StrippingLoop ccpp:hasStep ?s . ?s ccpp:stepType \"inline\" }", ["29"]),
 ("T15", "Topology", "What is the first valve after the E100 sump outlet?", "SELECT ?tag WHERE { ccpp:E100_N_sump_outlet ccpp:feedsInto ?x . ?x ccpp:tag ?tag }", ["V110"]),
 ("T18", "Topology", "Can solvent leaving E100 get back to E100?", "ASK { ccpp:E100 ccpp:feedsInto+ ccpp:E100 }", ["true"]),
 # ---------------- Valves ----------------
 ("V01", "Valves", "Which valves are check valves?", "SELECT ?tag WHERE { ?v a ccpp:CheckValve ; ccpp:tag ?tag }", ["V112", "V113a"]),
 ("V02", "Valves", "Which valves are shutdown valves?", "SELECT ?tag WHERE { ?v a ccpp:ShutdownValve ; ccpp:tag ?tag }", ["SDV123", "SDV125"]),
 ("V03", "Valves", "What type of valve is V302?", "SELECT ?t WHERE { ccpp:V302 ccpp:valveType ?t }", ["needle"]),
 ("V05", "Valves", "Which valves on floor 1 are closed in the stripping loop line-up?",
  "SELECT ?tag WHERE { ?v a/rdfs:subClassOf* ccpp:Valve ; ccpp:floor 1 ; ccpp:normalPosition \"closed\" ; ccpp:tag ?tag }",
  ["FCV110", "RV101", "SDV123", "V101", "V102", "V105", "V106", "V109", "V120"]),
 ("V06", "Valves", "Which valve bypasses Z102?", "SELECT ?tag WHERE { ?v ccpp:bypasses ccpp:Z102 ; ccpp:tag ?tag }", ["V120"]),
 ("V07", "Valves", "Which valve protects J100?", "SELECT ?tag WHERE { ?v ccpp:protects ccpp:J100 ; ccpp:tag ?tag }", ["RV101"]),
 ("V08", "Valves", "What is the set pressure of the relief valve protecting J100?",
  "SELECT ?p WHERE { ?v ccpp:protects ccpp:J100 . ?l ccpp:appliesTo ?v ; ccpp:limitType \"relief\" ; ccpp:highValue ?p }", ["10"]),
 ("V09", "Valves", "Which valves are on floor 3?", "SELECT ?tag WHERE { ?v a/rdfs:subClassOf* ccpp:Valve ; ccpp:floor 3 ; ccpp:tag ?tag }",
  ["V217", "V302", "V309", "V315", "V316", "V318", "V402", "V403"]),
 ("V11", "Valves", "Which valve is named ZS110 on site?",
  "SELECT ?tag WHERE { ?d a ccpp:PIDDiscrepancy ; ccpp:asBuilt ?b ; ccpp:concerns/ccpp:tag ?tag . FILTER(CONTAINS(?b, \"ZS110\")) }", ["FCV110"]),
 ("V12", "Valves", "Which valves on the flow route are not ball valves?",
  "SELECT DISTINCT ?tag WHERE { ccpp:StrippingLoop ccpp:hasStep/ccpp:stepItem ?v . ?v a/rdfs:subClassOf* ccpp:Valve ; ccpp:valveType ?t ; ccpp:tag ?tag . FILTER(?t != \"ball\") }",
  ["V112", "V113a", "PCV122", "SDV125"]),
 # ---------------- Instruments ----------------
 ("I01", "Instruments", "Which instrument measures pressure drop across Z102?",
  "SELECT ?tag WHERE { ?i a ccpp:DifferentialPressureInstrument ; ccpp:monitors ccpp:Z102 ; ccpp:tag ?tag }", ["PDT105"]),
 ("I02", "Instruments", "What type of sensor is FT102?", "SELECT ?t WHERE { ccpp:FT102 ccpp:sensorType ?t }", ["Coriolis mass flow meter"]),
 ("I04", "Instruments", "Which instruments use a 4-20mA signal?", "SELECT ?tag WHERE { ?i ccpp:signalType \"4-20mA\" ; ccpp:tag ?tag }",
  ["FT103", "TT106", "TT202", "TT203", "TT212a", "TT212b", "TT300", "TT301"]),
 ("I05", "Instruments", "Which instruments monitor H100?", "SELECT ?tag WHERE { ?i ccpp:monitors ccpp:H100 ; ccpp:tag ?tag }",
  ["DI100", "FI102", "FT100", "FT101", "FT102", "TI100", "TT100"]),
 ("I06", "Instruments", "Which instruments sit at stage 5?", "SELECT ?tag WHERE { ?i ccpp:locatedAtStage/ccpp:stageNumber 5 ; ccpp:tag ?tag }", ["TT300", "TT301"]),
 ("I07", "Instruments", "Which instruments measure in the vapour phase?", "SELECT ?tag WHERE { ?i ccpp:measuredPhase \"vapour\" ; ccpp:tag ?tag }",
  ["PSHH400", "TT201", "TT203", "TT301", "TT303", "TT401"]),
 ("I09", "Instruments", "Which instruments are K-type thermocouples?", "SELECT ?tag WHERE { ?i ccpp:sensorType \"K-type thermocouple\" ; ccpp:tag ?tag }", ["TT212a", "TT212b"]),
 ("I10", "Instruments", "Which instrument measures liquid temperature at the top of E100?",
  "SELECT ?tag WHERE { ?i ccpp:locatedAtStage/ccpp:stageNumber 1 ; ccpp:measuredPhase \"liquid\" ; ccpp:tag ?tag }", ["TT400"]),
 ("I11", "Instruments", "Which instruments monitor J100?", "SELECT ?tag WHERE { ?i ccpp:monitors ccpp:J100 ; ccpp:tag ?tag }",
  ["FI103", "FI104", "FT103", "FT104", "PT104", "TT106"]),
 ("I13", "Instruments", "What is TE105 called in the report?",
  "SELECT ?t WHERE { ccpp:TE105 ccpp:citedIn/ccpp:citationText ?t . FILTER(CONTAINS(?t, \"TT105\")) }", "ANY"),
 # ---------------- Control and interlocks ----------------
 ("C01", "Control", "Which controllers act on J100?", "SELECT ?tag WHERE { ?k ccpp:controls ccpp:J100 ; ccpp:tag ?tag }", ["FIC103", "FIC104", "HS100", "SIC100"]),
 ("C02", "Control", "What does the J100 flow loop control?", "SELECT ?cv WHERE { ccpp:CL_J100_flow ccpp:controlledVariable ?cv }", ["MEA flowrate leaving E100"]),
 ("C04", "Control", "Which controllers drive H200b?",
  "SELECT DISTINCT ?tag WHERE { ?cl ccpp:hasFinalElement ccpp:H200b ; ccpp:hasController/ccpp:tag ?tag }", ["TIC213b", "TY213b"]),
 ("C05", "Control", "Which control loop is a cascade master?", "SELECT ?m WHERE { ?m ccpp:cascadeMasterOf ?s }", ["CL_H100_temperature_master"]),
 ("C06", "Control", "What does the H100 steam loop adjust?", "SELECT ?tag WHERE { ccpp:CL_H100_steam_slave ccpp:hasFinalElement/ccpp:tag ?tag }", ["FCV110"]),
 ("C07", "Control", "Which interlocks trip J100?", "SELECT ?i WHERE { ?i a ccpp:Interlock ; ccpp:tripsItem ccpp:J100 }", ["IL_E100_level_HH", "IL_E100_level_LL"]),
 ("C09", "Control", "How many control loops are modelled?", "SELECT (COUNT(?l) AS ?n) WHERE { ?l a ccpp:ControlLoop }", ["6"]),
 ("C10", "Control", "What setpoint does TIC213a hold during normal running?",
  "SELECT ?v WHERE { ?l ccpp:appliesTo ?x ; ccpp:limitType \"setpoint\" ; ccpp:highValue ?v . ?x ccpp:tag ?tag . FILTER(?tag IN (\"TIC213a\", \"H200a\")) }", "GAP"),
 # ---------------- Limits and safety ----------------
 ("L01", "Limits", "What is PCV122 set to?", "SELECT ?v WHERE { ccpp:limit_PCV122_set ccpp:highValue ?v }", ["8"]),
 ("L04", "Limits", "At what PDT105 reading is Z102 treated as blocked?", "SELECT ?v WHERE { ccpp:limit_PDT105_blocked_filter ccpp:highValue ?v }", ["0.45"]),
 ("L05", "Limits", "At what LT101 level is the low alarm?", "SELECT ?v WHERE { ccpp:limit_LT101_low_alarm ccpp:lowValue ?v }", ["5"]),
 ("L06", "Limits", "What is the lower end of the LT101 operating window?", "SELECT ?v WHERE { ccpp:limit_LT101_operating_window ccpp:lowValue ?v }", ["10"]),
 ("L07", "Limits", "Above what pump power does J100 cavitate?", "SELECT ?v WHERE { ccpp:limit_J100_cavitation ccpp:highValue ?v }", ["55"]),
 ("L08", "Limits", "What is the maximum safe J100 pump power?", "SELECT ?v WHERE { ccpp:limit_J100_power_range ccpp:highValue ?v }", ["60"]),
 ("L09", "Limits", "Are any operating limits still unverified?", "SELECT ?l WHERE { ?l ccpp:valueVerified false }", []),
 ("L10", "Limits", "At what pressure does PSHH400 trip?", "SELECT ?v WHERE { ccpp:limit_PSHH400_set ccpp:highValue ?v }", ["2"]),
 ("L11", "Limits", "What is the maximum steam flow to H100?", "SELECT ?v WHERE { ccpp:limit_H100_steam_limit ccpp:highValue ?v }", ["140"]),
 ("L12", "Limits", "Which limits have no value recorded?",
  "SELECT ?lab WHERE { ?l a ccpp:OperatingLimit ; rdfs:label ?lab . FILTER NOT EXISTS { ?l ccpp:highValue ?h } FILTER NOT EXISTS { ?l ccpp:lowValue ?lo } }",
  ["LZAH100", "TSHH212a", "TSHH212b", "TZAH106"]),
 ("L14", "Limits", "What temperature trips H200a?", "SELECT ?v WHERE { ccpp:limit_TSHH212a ccpp:highValue ?v }", "GAP"),
 # ---------------- Procedures ----------------
 ("P01", "Procedures", "How many steps are in the Z102 bypass procedure?",
  "SELECT (COUNT(?s) AS ?n) WHERE { ccpp:PROC_Z102_bypass ccpp:hasProcedureStep ?s }", ["6"]),
 ("P02", "Procedures", "What is the first step of the Z102 bypass?",
  "SELECT ?i WHERE { ccpp:PROC_Z102_bypass ccpp:hasProcedureStep ?s . ?s ccpp:stepOrder 1 ; ccpp:instruction ?i }",
  ["Reduce J100 power by 20 % per minute until it reaches 15 %"]),
 ("P03", "Procedures", "Which valves are closed during the Z102 bypass?",
  "SELECT ?tag WHERE { ccpp:PROC_Z102_bypass ccpp:hasProcedureStep ?s . ?s ccpp:requiredPosition \"closed\" ; ccpp:operatesOn/ccpp:tag ?tag }", ["V117a", "V117b"]),
 ("P04", "Procedures", "Which valves must be closed for the stripping loop line-up?",
  "SELECT ?tag WHERE { ccpp:PROC_stripping_loop_lineup ccpp:hasProcedureStep ?s . ?s ccpp:requiredPosition \"closed\" ; ccpp:operatesOn/ccpp:tag ?tag }",
  ["FCV110", "SDV123", "V101", "V102", "V105", "V106", "V120", "V302", "V309", "V315", "V316", "V318"]),
 ("P06", "Procedures", "What should I do if PDT105 reads 0.5 bar?",
  "SELECT ?i WHERE { ?p ccpp:triggerCondition ?t ; ccpp:hasProcedureStep ?s . ?s ccpp:instruction ?i . FILTER(CONTAINS(?t, \"PDT105\")) }", "ANY"),
 ("P07", "Procedures", "What is the procedure to switch to the side return (route C)?",
  "SELECT ?p WHERE { ?p a ccpp:Procedure ; ccpp:triggerCondition ?t . FILTER(CONTAINS(LCASE(?t), \"side\")) }", "GAP"),
 ("P08", "Procedures", "How long does the Z102 bypass procedure take?",
  "SELECT ?d WHERE { ccpp:PROC_Z102_bypass ?p ?d . FILTER(CONTAINS(LCASE(STR(?p)), \"duration\")) }", "GAP"),
 # ---------------- HAZOP ----------------
 ("H02", "HAZOP", "Which HAZOP elements cover H100?", "SELECT ?el WHERE { ?e ccpp:covers ccpp:H100 ; ccpp:elementNumber ?el }", ["11", "13"]),
 ("H03", "HAZOP", "Which inline equipment in the normal loop has no HAZOP coverage?",
  "SELECT DISTINCT ?tag WHERE { ccpp:StrippingLoop ccpp:hasStep ?s . ?s ccpp:stepItem ?e ; ccpp:stepType \"inline\" . "
  "?e a/rdfs:subClassOf* ccpp:Equipment ; ccpp:tag ?tag . FILTER NOT EXISTS { ?h a ccpp:HazopElement ; ccpp:covers ?e } }", ["H200a", "H200b", "SDV125"]),
 ("H04", "HAZOP", "What safeguard does the HAZOP give for no flow due to a blocked filter?",
  "SELECT ?sg WHERE { ?d a ccpp:HazopDeviation ; ccpp:concerns ccpp:Z102 ; ccpp:safeguard ?sg }", "ANY"),
 ("H05", "HAZOP", "What does the HAZOP say about the H200 heaters?",
  "SELECT ?d WHERE { ?d a ccpp:HazopDeviation ; ccpp:concerns ?h . ?h a ccpp:ElectricHeater }", "GAP"),
 # ---------------- Heat and mass transfer, Aspen ----------------
 ("A01", "Aspen/HMT", "Which Aspen file is recommended?", "SELECT ?f WHERE { ?c ccpp:recommendedForUse true ; ccpp:aspenFile ?f }", ["ABB_pilot_plant_final_3.apwz"]),
 ("A02", "Aspen/HMT", "What is the C100 duty in the recommended case?",
  f"SELECT ?d WHERE {{ ?p ccpp:ofEquipment ccpp:C100 ; ccpp:inCase ?c ; ccpp:duty_kW ?d . {REC} }}", "ANY"),
 ("A03", "Aspen/HMT", "What is the H100 duty in the recommended case?",
  f"SELECT ?d WHERE {{ ?p ccpp:ofEquipment ccpp:H100 ; ccpp:inCase ?c ; ccpp:duty_kW ?d . {REC} }}", "ANY"),
 ("A04", "Aspen/HMT", "On which stage is most CO2 desorbed?",
  f"SELECT ?n WHERE {{ ?r a ccpp:StageResult ; ccpp:inCase ?c ; ccpp:ofStage/ccpp:stageNumber ?n ; ccpp:co2Desorbed_kg_h ?d . {REC} }} ORDER BY DESC(?d) LIMIT 1", ["2"]),
 ("A07", "Aspen/HMT", "Which exchangers show a temperature cross?",
  "SELECT DISTINCT ?tag WHERE { ?p ccpp:temperatureCross true ; ccpp:ofEquipment/ccpp:tag ?tag }", ["C100"]),
 ("A08", "Aspen/HMT", "Which Aspen blocks failed?", "SELECT ?b WHERE { ?x ccpp:status \"ERROR\" ; ccpp:blockId ?b }", ["E100", "H100"]),
 ("A09", "Aspen/HMT", "What is the specific reboiler duty?",
  f"SELECT ?v WHERE {{ ?p a ccpp:ColumnPerformance ; ccpp:inCase ?c ; ccpp:specificReboilerDuty_GJ_t ?v . {REC} }}", "ANY"),
 ("A10", "Aspen/HMT", "What MEA concentration is in the lean solvent?",
  f"SELECT ?w WHERE {{ ?s a ccpp:StreamState ; ccpp:inCase ?c ; ccpp:streamId \"S3\" ; ccpp:meaMassFraction ?w . {REC} }}", "ANY"),
 ("A11", "Aspen/HMT", "What heat duty do H200a/b need during the stripping loop test?",
  "SELECT ?d WHERE { ?p ccpp:ofEquipment ccpp:H200a ; ccpp:inCase ?c ; ccpp:duty_kW ?d . ?c ccpp:representsMode ccpp:StripperRecirculation }", "GAP"),
 # ---------------- Grounding ----------------
 ("G01", "Grounding", "How many source documents are in the KG?", "SELECT (COUNT(?d) AS ?n) WHERE { ?d a ccpp:SourceDocument }", ["9"]),
 ("G02", "Grounding", "Which facts cite HAZOP recommendation M4?",
  "SELECT ?x WHERE { ?x ccpp:citedIn/ccpp:citationText ?t . FILTER(CONTAINS(?t, \"recommendation M4\")) }", ["limit_PSHH116_set", "limit_PSHH400_set"]),
 ("G03", "Grounding", "Is any plant item missing a citation?",
  "SELECT ?tag WHERE { ?i a/rdfs:subClassOf* ccpp:PlantItem ; ccpp:tag ?tag . FILTER NOT EXISTS { ?i ccpp:citedIn ?c } }", []),
 ("G04", "Grounding", "Which plant items are cited only to the P&ID?",
  "SELECT ?tag WHERE { ?i a/rdfs:subClassOf* ccpp:PlantItem ; ccpp:tag ?tag ; ccpp:citedIn ?c0 . "
  "FILTER NOT EXISTS { ?i ccpp:citedIn/ccpp:document ?d . FILTER(?d != ccpp:SRC_PID) } }", "ANY"),
 ("G05", "Grounding", "How many citations come from the team's checks?",
  "SELECT (COUNT(?c) AS ?n) WHERE { ?c ccpp:document ccpp:SRC_TEAM }", "ANY"),
 # ---------------- Student questions and gap probes ----------------
 ("S01", "Gap probes", "What is the power rating of H200a?",
  "SELECT ?v WHERE { ccpp:H200a ?p ?v . FILTER(CONTAINS(LCASE(STR(?p)), \"power\") || CONTAINS(LCASE(STR(?p)), \"rating\")) }", "GAP"),
 ("S02", "Gap probes", "What electrical supply or breaker feeds H200a?",
  "SELECT ?x WHERE { ?x ?p ccpp:H200a ; a ?t . FILTER(CONTAINS(LCASE(STR(?t)), \"electric\") || CONTAINS(LCASE(STR(?t)), \"breaker\") || CONTAINS(LCASE(STR(?t)), \"supply\")) }", "GAP"),
 ("S03", "Gap probes", "What is the design pressure of E100?",
  "SELECT ?v WHERE { ccpp:E100 ?p ?v . FILTER(CONTAINS(LCASE(STR(?p)), \"design\")) }", "GAP"),
 ("S05", "Gap probes", "What is the hold-up volume of the E100 sump?",
  "SELECT ?v WHERE { ccpp:E100 ?p ?v . FILTER(CONTAINS(LCASE(STR(?p)), \"volume\") || CONTAINS(LCASE(STR(?p)), \"holdup\")) }", "GAP"),
 ("S06", "Gap probes", "Where is V217 and what does it do?", "SELECT ?x WHERE { ?x ccpp:tag \"V217\" }", "GAP"),
 ("S07", "Gap probes", "How much reflux from J300 joins the loop?",
  "SELECT ?v WHERE { ?s ccpp:streamId ?id ; ccpp:massFlow_kg_h ?v ; ccpp:toBlock/ccpp:represents ccpp:E100 . FILTER(CONTAINS(?id, \"reflux\")) }", "GAP"),
 ("S08", "Gap probes", "Who is authorised to open V120?",
  "SELECT ?x WHERE { ?x ?p ccpp:V120 . FILTER(CONTAINS(LCASE(STR(?p)), \"authori\") || CONTAINS(LCASE(STR(?p)), \"role\")) }", "GAP"),
 ("S10", "Gap probes", "What happens to the E100 level if J100 trips?",
  "SELECT ?c WHERE { ?d ccpp:concerns ccpp:J100 ; ccpp:consequence ?c . FILTER(CONTAINS(LCASE(?c), \"level\")) }", "GAP"),
 ("S12", "Gap probes", "Are V110, V112, V113a and V113b locked?",
  "SELECT ?tag WHERE { ?v ccpp:normalPosition \"locked open\" ; ccpp:tag ?tag }", "GAP"),
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
        if res.type == "ASK":
            rows = [[str(res.askAnswer).lower()]]
        else:
            rows = [["" if v is None else str(v).replace(NS, "") for v in r] for r in res]
        err = None
    except Exception as e:  # noqa: BLE001
        rows, err = [], str(e)
    first = {norm(r[0]) for r in rows if r and r[0] != ""}
    if err:
        status = "QUERY ERROR"
    elif isinstance(expect, list):
        status = "PASS" if first == {norm(x) for x in expect} else "FAIL"
    elif expect == "ANY":
        status = "ANSWERED" if rows else "NO ANSWER"
    else:
        status = "GAP CONFIRMED" if not rows else "ANSWERED (gap probe)"
    results.append((qid, cat, question, expect, rows, status, err))

summary = collections.Counter((r[1], r[5]) for r in results)
cats = list(dict.fromkeys(r[1] for r in results))
statuses = ["PASS", "FAIL", "ANSWERED", "NO ANSWER", "GAP CONFIRMED", "ANSWERED (gap probe)", "QUERY ERROR"]
lines = ["# Stripping loop KG: 100-question run", "", f"Questions asked: {len(results)}", "",
         "| Category | " + " | ".join(statuses) + " |", "|---|" + "---|" * len(statuses)]
for cat in cats:
    lines.append(f"| {cat} | " + " | ".join(str(summary.get((cat, s), 0)) for s in statuses) + " |")
lines.append("| **Total** | " + " | ".join(str(sum(1 for r in results if r[5] == s)) for s in statuses) + " |")
for qid, cat, question, expect, rows, status, err in results:
    lines += ["", f"## {qid} [{cat}] {status}", "", f"**{question}**", ""]
    if isinstance(expect, list):
        lines.append(f"- Expected: {', '.join(expect) if expect else '(no rows)'}")
    if err:
        lines.append(f"- Error: {err}")
    for r in rows[:12]:
        lines.append("- " + " | ".join(r))
    if len(rows) > 12:
        lines.append(f"- ... {len(rows) - 12} more rows")
    if not rows and not err:
        lines.append("- (no rows)")

out = HERE / "hundred_results.md"
out.write_text("\n".join(lines) + "\n")
print(f"{len(results)} questions asked")
for s in statuses:
    n = sum(1 for r in results if r[5] == s)
    if n:
        print(f"  {s}: {n}")
print(f"Results written to {out}")
