"""
Piece 14: safety logic (Pilot Plant 2514), for the KG A+ improvements.

Sources (received from the plant, Nov 2026):
- Cause and effect matrix, Rev 5, 06/10/2011, 'FINAL FOR CONSTRUCTION' (CauseAndEffectRev5_2.xls): 40 causes against 26 effects
- Relief valve schedule (RV_Schedule.xlsx): set pressure, size, part number and supplier of 11 relief valves
The trip rows below are generated from the spreadsheet cell by cell (legend: S = shutdown machinery, C = close valve,
O = open valve, H = open valve manually from the control system interface, M = control set to manual and output to 0%,
A = activate beacon / klaxon / alarm). Each trip is linked to where it is detected and to everything it stops, closes
or opens, and to the process variables it safeguards in the causal layer (piece 13).
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "kgkit"))

CE = "Cause and effect matrix Rev 5 (06/10/2011)"

SECTION = dict(
    prefix="sfl", loop_id="SafetyLogicRegister", mode="FigureOfEight", flow="feedsInto",
    loop_label="Safety logic: trips and relief valve schedule (register, no flow route)",
    loop_note="What each trip detects, its set point and delay, and what it stops, closes or opens.",
    loop_cite=[("CE", "whole matrix, sheet 'C & E Process and Safety'"), ("RVSCHED", "sheet 'RV'")],
)

ITEMS = {}

# The CO2 and N2 supply shutdown valves are in the matrix; add them only if no earlier section already has them
_other = "".join(p.read_text() for p in ROOT.glob("*/*.ttl") if p.parent.name not in ("safety_logic", "ccpp", "ontology"))
for tag, what in (("XV128", "CO2 supply"), ("XV129", "N2 supply")):
    if not re.search(r"^ccpp:" + tag + r"\s+a\s", _other, re.M):
        ITEMS[tag] = dict(cls="ShutdownValve", label=f"{tag} {what} shutdown valve (TSOV)", valve="shutdown (trip)",
                          note=f"{what} TSOV, closed by every full plant shutdown. In the cause and effect matrix but not in the REPORT lists (SL01).",
                          cite=[("CE", f"effect column {tag[:2]}-{tag[2:]} ('{what} TSOV')")])

# key, switch tag, interlock group, cause, detection, trip tag, set point, delay, start-up override, remark,
# detected at, stops, closes, opens, opened manually (H), other actions
TRIPS = [
    ("AZALL101", "AZALL101", "1", "O2 level LL", "Extreme low level in plant, AT-101, AT-102", "AZALL-101, AZALL-102", "19.5%", "", "", "", [], ["J100", "J101a", "J101b", "J102", "J103", "J104", "J105", "J300", "H200a", "H200b"], ["XV128", "XV129", "SDV171", "SDV123", "SDV125", "SDV152", "XV140", "FCV110"], [], [], ["all control loops to manual, output 0%", "beacon", "klaxon"]),
    ("FALL301", "FALL301", "2", "CO2 flow LL", "Extreme low CO2 return flow, F-301/302", "FALL-301, FALL-302", "User Set Point", "2mins.", "try it three times", "", ["FT301", "FT302"], ["J103"], [], [], [], ["alarm"]),
    ("HSZ", "HSZ4", "1", "Emergency shut-down", "Local emergency shut-down by operator, HSZ199/299/399/499/599", "HSZ-4", "", "", "", "", [], ["J100", "J101a", "J101b", "J102", "J103", "J104", "J105", "J300", "H200a", "H200b"], ["XV128", "XV129", "SDV171", "SDV123", "SDV125", "SDV152", "XV140", "FCV110"], [], [], ["all control loops to manual, output 0%", "beacon", "klaxon"]),
    ("LSHH100", "LSHH100", "5", "Stripper column level HH", "Stripper column E100 liquid level extremely high, LSHH-100", "LZAHH-100", "", "1min.", "", "", ["E100"], ["J100", "J101a", "J101b"], ["XV140", "FCV110"], [], [], ["alarm"]),
    ("LSLL102", "LSLL102", "5", "Stripper column level LL", "Stripper column E100 liquid level extremely low, LSLL-102", "LZALL-102", "", "1 min", "", "", ["E100"], ["J100", "J101a", "J101b"], ["XV140", "FCV110"], [], [], ["alarm"]),
    ("LSHH103", "LSHH103", "6", "Saturation tank level HH", "Saturation tank K101 liquid level extremely high, LSHH-103", "LZAHH-103", "", "", "", "", ["K101"], ["J102", "J103", "J104"], [], [], [], ["alarm"]),
    ("LSLL105", "LSLL105", "7", "Saturation tank level LL", "Saturation tank K101 liquid level extremely low, LSLL-105", "LZALL-105", "", "", "", "", ["K101"], ["J104"], [], [], [], ["alarm"]),
    ("LSHH107", "LSHH107", "4", "Absorber column level HH", "Absorber column E101 liquid level extremely high, LSHH-107", "LZAHH-107", "", "1min.", "", "", ["E101"], ["J100", "J101a", "J101b", "J102", "J103"], ["XV140", "FCV110"], [], [], ["alarm"]),
    ("LSLL109", "LSLL109", "5", "Absorber column level LL", "Absorber column E101 liquid level extremely low, LSLL-109", "LZALL-109", "", "1min.", "", "", ["E101"], ["J100", "J101a", "J101b"], ["XV140", "FCV110"], [], [], ["alarm"]),
    ("LSHH110", "LSHH110", "3", "Relief vessl level HH", "Relief collection vessel K102 liquid level high, LSHH-110", "LZAHH-110", "", "", "", "", ["K102"], ["J100", "J101a", "J101b", "J102", "J103", "J104", "J105", "J300", "H200a", "H200b"], ["XV128", "XV129", "SDV171", "SDV123", "SDV125", "SDV152", "XV140", "FCV110"], [], [], ["all control loops to manual, output 0%"]),
    ("LSHH111", "LSHH111", "8", "Storage tank level HH", "Storage tank R100 liquid level high, LSHH-111", "LZAHH-111", "", "", "", "", ["R100"], ["J105"], [], [], [], ["alarm"]),
    ("LSHH112", "LSHH112", "8", "Storage tank level HH", "Storage tank F100 liquid level high, LSHH-112", "LZAHH-112", "", "", "", "", ["F100"], ["J105"], [], [], [], ["alarm"]),
    ("LSLL112", "LSLL112", "8", "Storage tank level LL", "Storage tank F100 liquid level low, LSLL-112", "LZALL-112", "", "", "", "", ["F100"], ["J105"], [], [], [], ["alarm"]),
    ("LSLL114", "LSLL114", "8", "Pump inlet level LL", "Pump J105 liquid level low, LSLL-114", "LZALL-114", "", "", "", "", ["J105"], ["J105"], [], [], [], ["alarm"]),
    ("LSHH116", "LSHH116", "3", "Tank level HH", "Liquid level in K-103 extremely high, LSHH-116", "LZAHH-116", "", "", "", "", ["K103"], ["J100", "J101a", "J101b", "J102", "J103", "J104", "J105", "J300", "H200a", "H200b"], ["XV128", "XV129", "SDV171", "SDV123", "SDV125", "SDV152", "XV140", "FCV110"], [], [], ["all control loops to manual, output 0%"]),
    ("LSHH400", "LSHH400", "3", "Cooler level HH", "Liquid level in cooler C400 extremely high, LSHH-400", "LZAHH-400", "", "5mins.", "", "", ["C400"], ["J100", "J101a", "J101b", "J102", "J103", "J104", "J105", "J300", "H200a", "H200b"], ["XV128", "XV129", "SDV171", "SDV123", "SDV125", "SDV152", "XV140", "FCV110"], [], [], ["all control loops to manual, output 0%"]),
    ("LSLL402", "LSLL402", "9", "Cooler level LL", "Liquid level in cooler C400 extremely low, LSLL-402", "LZALL-402", "", "", "", "", ["C400"], ["J300"], [], [], [], []),
    ("LSHH403", "LSHH403", "3", "Separator level HH", "Separator liquid K401 level high, LSHH-403", "LZAHH-403", "", "", "", "", ["K401"], ["J100", "J101a", "J101b", "J102", "J103", "J104", "J105", "J300", "H200a", "H200b"], ["XV128", "XV129", "SDV171", "SDV123", "SDV125", "SDV152", "XV140", "FCV110"], [], [], ["all control loops to manual, output 0%"]),
    ("LSHH404", "LSHH404", "3", "Cyclone level HH", "Gas cyclone K402 level high, LSHH-404", "LZAHH-404", "", "", "", "", ["K402"], ["J100", "J101a", "J101b", "J102", "J103", "J104", "J105", "J300", "H200a", "H200b"], ["XV128", "XV129", "SDV171", "SDV123", "SDV125", "SDV152", "XV140", "FCV110"], [], [], ["all control loops to manual, output 0%"]),
    ("LZALL405", "LSH405", "3", "Purge line level HH", "Purge line liquid level high", "LZALL-405", "", "", "", "", [], ["J100", "J101a", "J101b", "J102", "J103", "J104", "J105", "J300", "H200a", "H200b"], ["XV128", "XV129", "SDV171", "SDV123", "SDV125", "SDV152", "XV140", "FCV110"], [], [], ["all control loops to manual, output 0%"]),
    ("PZALL101", "PT101", "10", "Steam pressure LL", "Steam supply pressure extremely low, PT-101", "PZALL-101", "3.75 barg", "", "", "", ["PT101"], [], ["XV140", "FCV110"], [], [], ["alarm"]),
    ("PSHH116", "PSHH116", "3", "Sripper bottom pressure HH", "Bottom of stripper column E100 pressure high, PSHH-116", "PZAHH-116", "2 barg (rising)", "", "", "", ["E100"], ["J100", "J101a", "J101b", "J102", "J103", "J104", "J105", "J300", "H200a", "H200b"], ["XV128", "XV129", "SDV171", "SDV123", "SDV125", "SDV152", "XV140", "FCV110"], [], [], ["all control loops to manual, output 0%"]),
    ("PSHH117", "PSHH117", "3", "Absorber bottom pressure HH", "Bottom of absorber column E101 pressure high, PSHH-117", "PZAHH-117", "3.5 barg (rising)", "", "", "", ["E101"], ["J100", "J101a", "J101b", "J102", "J103", "J104", "J105", "J300", "H200a", "H200b"], ["XV128", "XV129", "SDV171", "SDV123", "SDV125", "SDV152", "XV140", "FCV110"], [], [], ["all control loops to manual, output 0%"]),
    ("PSHH400", "PSHH400", "3", "Sripper top pressure HH", "Top of stripper column E100 pressure high, PSHH-400", "PZAHH-400", "2 barg (rising)", "", "", "", ["E100"], ["J100", "J101a", "J101b", "J102", "J103", "J104", "J105", "J300", "H200a", "H200b"], ["XV128", "XV129", "SDV171", "SDV123", "SDV125", "SDV152", "XV140", "FCV110"], [], [], ["all control loops to manual, output 0%"]),
    ("PSHH405", "PSHH405", "3", "Absorber top pressure HH", "Top of absorber column E101 pressure high, PSHH-405", "PZAHH-405", "3.5 barg (rising)", "", "", "", ["E101"], ["J100", "J101a", "J101b", "J102", "J103", "J104", "J105", "J300", "H200a", "H200b"], ["XV128", "XV129", "SDV171", "SDV123", "SDV125", "SDV152", "XV140", "FCV110"], [], [], ["all control loops to manual, output 0%"]),
    ("TSHH106", "TSHH106", "11", "Pump temperature HH", "Pump J100 temperature high, TSHH-106", "TZAHH-106", "85 degC", "", "", "", ["J100"], ["J100"], [], [], [], ["alarm"]),
    ("TSHH111a", "TSHH111a", "3", "Pump temperature HH", "Pump J101a temperature high, TSHH-111a", "TZAHH-111a", "85 degC", "", "", "", ["J101a"], ["J100", "J101a", "J101b", "J102", "J103", "J104", "J105", "J300", "H200a", "H200b"], ["XV128", "XV129", "SDV171", "SDV123", "SDV125", "SDV152", "XV140", "FCV110"], [], [], ["all control loops to manual, output 0%"]),
    ("TSHH111b", "TSHH111b", "3", "Pump temperature HH", "Pump J101b temperature high, TSHH-111b", "TZAHH-111b", "85 degC", "", "", "", ["J101b"], ["J100", "J101a", "J101b", "J102", "J103", "J104", "J105", "J300", "H200a", "H200b"], ["XV128", "XV129", "SDV171", "SDV123", "SDV125", "SDV152", "XV140", "FCV110"], [], [], ["all control loops to manual, output 0%"]),
    ("TSHH114", "TSHH114", "3", "Pump temperature HH", "Pump J102 temperature high, TSHH-114", "TZAHH-114", "85 degC", "", "", "", ["J102"], ["J100", "J101a", "J101b", "J102", "J103", "J104", "J105", "J300", "H200a", "H200b"], ["XV128", "XV129", "SDV171", "SDV123", "SDV125", "SDV152", "XV140", "FCV110"], [], [], ["all control loops to manual, output 0%"]),
    ("TSHH115", "TSHH115", "3", "Pump temperature HH", "Pump J103 temperature high, TSHH-115", "TZAHH-115", "85 degC", "", "", "", ["J103"], ["J100", "J101a", "J101b", "J102", "J103", "J104", "J105", "J300", "H200a", "H200b"], ["XV128", "XV129", "SDV171", "SDV123", "SDV125", "SDV152", "XV140", "FCV110"], [], [], ["all control loops to manual, output 0%"]),
    ("TSHH116", "TSHH116", "8", "Pump temperature HH", "Pump J105 temperature high, TSHH-116", "TZAHH-116", "85 degC", "", "", "", ["J105"], ["J105"], [], [], [], ["alarm"]),
    ("TSHH212a", "TSHH212a", "12", "Heater temperature HH", "Heater H200a temperature high, TSHH-212a", "TZAHH-212a", "250 degC", "", "", "", ["H200a"], ["H200a"], [], [], [], ["alarm"]),
    ("TSHH212b", "TSHH212b", "13", "Heater temperature HH", "Heater H200b temperature high, TSHH-212b", "TZAHH-212b", "250 degC", "", "", "", ["H200b"], ["H200b"], [], [], [], ["alarm"]),
    ("TSHH310", "TSHH310", "3", "Pump temperature HH", "Pump J300 temperature high, TSHH-310", "TZAHH-310", "60 degC", "", "", "", ["J300"], ["J100", "J101a", "J101b", "J102", "J103", "J104", "J105", "J300", "H200a", "H200b"], ["XV128", "XV129", "SDV171", "SDV123", "SDV125", "SDV152", "XV140", "FCV110"], [], [], ["all control loops to manual, output 0%"]),
    ("YS100", "YS100", "8", "Receiver vessel disengaged", "Feeder vessel F100 disengaged, YS-100", "YZA-100", "", "", "", "", ["F100"], ["J105"], [], [], [], ["alarm"]),
    ("YS101", "YS101", "8", "Feeder vessel disengaged", "Receiver vessel R100 disengaged, YS-101", "YZA-101", "", "", "", "", ["R100"], ["J105"], [], [], [], ["alarm"]),
    ("PAHH401", "PAHH401", "", "Stripper pressure HH", "Stripper pressure High High", "PAHH-401", "1.5 barg", "", "", "", ["E100"], [], [], ["SDV421"], [], ["alarm"]),
    ("PALL401", "PALL401", "", "Stripper Column pressure LL", "Stripper Column pressure Low Low", "PALL-401", "-0.05 barg", "", "", "See more logic in FAT reports", ["E100"], [], [], ["SDV424"], [], ["alarm"]),
    ("LAHH104", "LAHH104", "", "Excess water in K-101", "Excess water in K-101", "LAHH-104", "55%", "", "", "", ["K101"], [], [], [], ["SDV170"], []),
    ("LALL104", "LALL104", "", "No water in K-101", "No water in K-101", "LALL-104", "10%", "", "", "", ["K101"], [], [], [], ["SDV169"], []),
]

LINKS = []
FULL_SHUTDOWN = []
for (key, switch, group, cause, detection, trip_tag, setpoint, delay, override, remark, detected, stops, closes, opens, manual, other) in TRIPS:
    node = "TRIP_" + key
    process_control = group == ""
    full = len(stops) == 10
    if full:
        FULL_SHUTDOWN.append(node)
    actions = []
    if full:
        actions.append("FULL PLANT SHUTDOWN.")
    if stops:
        actions.append("Stops " + ", ".join(stops) + ".")
    if closes:
        actions.append("Closes " + ", ".join(closes) + ".")
    if opens:
        actions.append("Opens " + ", ".join(opens) + ".")
    if manual:
        actions.append("Operator opens " + ", ".join(manual) + " from the control system interface.")
    if other:
        actions.append("Also: " + "; ".join(other) + ".")
    trigger = f"{cause}: {detection} ({trip_tag})" + (f"; set point {setpoint}" if setpoint else "") + (f"; delay {delay}" if delay else "") \
              + (f"; start-up override: {override}" if override else "")
    props = {"switchTag": switch, "tripTag": trip_tag, "triggerCondition": trigger, "actionText": " ".join(actions),
             "handledBy": "process control system" if process_control else "safety system"}
    if group:
        props["interlockGroup"] = group
    if setpoint:
        props["setpointText"] = setpoint
    if delay:
        props["delayText"] = delay
    ITEMS[node] = dict(cls="SafetyTrip", label=f"{cause} ({trip_tag})", props=props, note=remark or None,
                       cite=[("CE", f"cause row '{cause}', tag {trip_tag}")])
    LINKS += [(node, "detectedAt", d) for d in detected] + [(node, "stops", x) for x in stops] + [(node, "closes", x) for x in closes] \
             + [(node, "opens", x) for x in opens] + [(node, "actsOn", x) for x in manual]

# trips as safeguards of the process variables in the causal layer (piece 13)
SAFEGUARDS = {
    "V_E100_P": ["PSHH116", "PSHH400", "PAHH401", "PALL401"], "V_E101_P": ["PSHH117", "PSHH405"],
    "V_E100_L": ["LSHH100", "LSLL102"], "V_E101_L": ["LSHH107", "LSLL109"], "V_K401_L": ["LSHH403", "LSHH400", "LSLL402"],
    "V_STEAM": ["PZALL101"], "V_CO2_RET": ["FALL301"], "V_K402_CARRY": ["LSHH404"], "V_J103_CARRY": ["LSHH116", "TSHH115"],
    "V_J100_CAV": ["TSHH106", "LSLL102"], "V_H200_DUTY": ["TSHH212a", "TSHH212b"],
}
LINKS += [(v, "safeguardedBy", "TRIP_" + t) for v, trips in SAFEGUARDS.items() for t in trips]

# Relief valve schedule: tag, set pressure (bar), inlet, outlet, part number, material, supplier
RELIEF = [
    ("RV100", 3.8, '1"', '2"', "4414.7912LL", "SS", "Leser Valves"),
    ("RV101", 10.0, '3/4" BSPF', '3/4" BSPF', '3/4"-1101-33', "316 SS", "Michael Smith"),
    ("RV102", 10.0, '3/8" BSPF', '3/8" BSPF', '3/8"-1101-30-HP', "316 SS / PTFE", "Michael Smith"),
    ("RV103", 10.0, '1/2" BSP', '3/4" BSP', "64610A1273", "SS", "Seetru"),
    ("RV104", 1.0, '1/2" BSP', '3/4" BSP', "64610A1273", "SS", "Seetru"),
    ("RV105", 3.8, '1 1/2"', '1 1/2"', "4414.7932LL", "SS", "Leser Valves"),
    ("RV106a", 10.0, '3/4" BSPF', '3/4" BSPF', '3/4"-1101-33', "316 SS", "Michael Smith"),
    ("RV106b", 10.0, '3/4" BSPF', '3/4" BSPF', '3/4"-1101-33', "316 SS", "Michael Smith"),
    ("RV107", 10.0, '3/8" BSPF', '3/8" BSPF', '3/8"-1101-30-HP', "316 SS / PTFE", "Michael Smith"),
    ("RV300", 10.0, '1/2" BSP', '3/4" BSP', "64610A1273", "SS", "Seetru"),
    ("RV400", 3.8, '2"', '3"', "4414.7942LL", "SS", "Leser Valves"),
]
IN_KG = ["RV101", "RV102", "RV103", "RV104", "RV105", "RV107", "RV300", "RV400"]     # relief valves an earlier section already holds
LIMITS = {}
for tag, bar, inlet, outlet, part, material, supplier in RELIEF:
    ITEMS["RS_" + tag] = dict(cls="ReliefScheduleEntry", label=f"{tag} relief valve schedule entry: set pressure {bar:g} bar",
                              props={"setPressureText": f"{bar:g} bar", "connectionText": f"inlet {inlet}, outlet {outlet}",
                                     "partNumber": part, "material": material, "supplier": supplier},
                              cite=[("RVSCHED", f"row {tag}")])
    if tag in IN_KG:
        LINKS.append(("RS_" + tag, "scheduleFor", tag))
        LIMITS["RVSCHED_" + tag] = (tag, "set pressure", "relief", None, bar, "bar", [("RVSCHED", f"row {tag}")])

# numeric trip set points, so they can be queried as numbers as well as read as text
for name, applies, quantity, low, high, unit, row in [
    ("CE_PSHH116", "E100", "pressure (column bottom)", None, 2.0, "barg", "PZAHH-116"), ("CE_PSHH400", "E100", "pressure (column top)", None, 2.0, "barg", "PZAHH-400"),
    ("CE_PSHH117", "E101", "pressure (column bottom)", None, 3.5, "barg", "PZAHH-117"), ("CE_PSHH405", "E101", "pressure (column top)", None, 3.5, "barg", "PZAHH-405"),
    ("CE_PAHH401", "E100", "pressure (opens the C400 vent SDV421)", None, 1.5, "barg", "PAHH-401"),
    ("CE_PALL401", "E100", "pressure (opens the vacuum breaker SDV424)", -0.05, None, "barg", "PALL-401"),
    ("CE_PZALL101", "PT101", "steam supply pressure", 3.75, None, "barg", "PZALL-101"),
    ("CE_LAHH104", "K101", "level (excess water)", None, 55.0, "%", "LAHH-104"), ("CE_LALL104", "K101", "level (no water)", 10.0, None, "%", "LALL-104"),
    ("CE_TSHH106", "J100", "pump temperature", None, 85.0, "degC", "TZAHH-106"), ("CE_TSHH111a", "J101a", "pump temperature", None, 85.0, "degC", "TZAHH-111a"),
    ("CE_TSHH111b", "J101b", "pump temperature", None, 85.0, "degC", "TZAHH-111b"), ("CE_TSHH114", "J102", "blower temperature", None, 85.0, "degC", "TZAHH-114"),
    ("CE_TSHH115", "J103", "compressor temperature", None, 85.0, "degC", "TZAHH-115"), ("CE_TSHH116", "J105", "pump temperature", None, 85.0, "degC", "TZAHH-116"),
    ("CE_TSHH212a", "H200a", "heater temperature", None, 250.0, "degC", "TZAHH-212a"), ("CE_TSHH212b", "H200b", "heater temperature", None, 250.0, "degC", "TZAHH-212b"),
    ("CE_TSHH310", "J300", "pump temperature", None, 60.0, "degC", "TZAHH-310"),
]:
    LIMITS[name] = (applies, quantity, "trip", low, high, unit, [("CE", f"cause row with tag {row}, set point column")])

KNOWN_TAGS = sorted({o for _, p, o in LINKS if p in ("detectedAt", "stops", "closes", "opens", "actsOn", "scheduleFor")})
LOOP = []

OPEN_ITEMS = {
    "SL01": ("XV128 (CO2 supply) and XV129 (N2 supply) shutdown valves are in the cause and effect matrix but not in the REPORT lists: find them on the P&ID "
             "near the supplies (K21 to K22 and N21 to N22)", ["XV128", "XV129"], "Trace on the P&ID"),
    "SL02": ("The matrix calls K102 the 'relief collection vessel' (LSHH-110, full plant shutdown); the KG holds K102 as the knockout drum ahead of J102",
             ["TRIP_LSHH110"], "Check on the P&ID and plant"),
    "SL03": ("The matrix describes SOV-170 as 'Feed to bottom of E-101' and SOV-171 as 'Feed to K-101'; the team trace has SDV170 on the N2 recycle from "
             "K101 to K102 (with FCV111)", ["TRIP_LAHH104", "TRIP_LALL104"], "Check on the P&ID and plant"),
    "SL04": ("The relief valve schedule lists RV100 (3.8 bar, 1 inch by 2 inch) but neither RV401 nor RV301; RV401 (E100 relief to K403) may be RV100 renumbered",
             ["RS_RV100"], "Ask the plant; check the valve nameplates"),
    "SL05": ("The relief valve schedule lists RV106a and RV106b (10 bar), which the P&ID differences document says are not on the plant", ["RS_RV106a", "RS_RV106b"],
             "Site check"),
    "SL06": ("The matrix is Rev 5 (2011) and says 'see more logic in FAT reports' for the vacuum breaker; the FAT reports or a later revision would confirm "
             "the as-installed logic", ["TRIP_PALL401"], "FAT reports from the plant"),
    "SL07": ("The oxygen analysers AT-101 and AT-102 (trip at 19.5% O2) are not in the P&ID-based KG", ["TRIP_AZALL101"], "Find on the plant; add as instruments"),
    "SL08": ("The 'description of interlocks' table at the foot of the matrix (groups 1 to 13) is blank", ["TRIP_HSZ"], "Ask the plant for the completed table"),
}
