"""
Piece 5: feed gas and the K101 saturator (Pilot Plant 2514). Built from the documents first,
then traced and checked by the team on the P&ID.

CO2 line (HAZOP element 1, 'V128 to tee'):  CO2 supply > V128 > PCV116 > FT105 > FCV105 > NRV101 > tee
N2 line  (HAZOP element 2, 'V127 to tee'):  N2 supply > V127 > PCV117 > PCV115 > FCV116 > NRV102 > tee
Common inlet > K101 saturator (element 3) > E101 gas inlet; FCV111 sets the K101 bypass rate (control table).
K101 water loop (element 4): K101 > J104 > C106 > back to K101.
Items and grids: REPORT instrument and valve lists. Controls: SUMMARY p.190. CONNECTIONS AFTER THE TEE ARE INFERRED.
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
INSTR = "Appendix B instrument list"
VALVES = "valve lists"
INFERRED = "connection inferred from the control table and HAZOP; to be traced on the P&ID"

SECTION = dict(
    prefix="gas", loop_id="GasFeedRoute", mode="FigureOfEight", flow="feedsInto",
    loop_label="Feed gas route (CO2 and N2 supplies to E101)",
    loop_note="Fresh CO2 and N2 are metered by mass flow controllers (FIC105, FIC116), meet at a tee, pass through the "
              "K101 saturator (or its bypass, FCV111) and enter the base of E101. The route after the tee is inferred.",
    loop_cite=[("HAZOP", "elements 1 (CO2 feed, V128 to tee), 2 (N2 feed, V127 to tee) and 3 (K101)"),
               ("SUMMARY", "p.190 (FIC105, FIC116, FIC304 on K101 bypass rate, TIC121)"),
               ("DERIVED", "route after the tee: " + INFERRED)],
)

ITEMS = {
    "CO2_SUPPLY": dict(cls="SupplyConnection", label="CO2 supply connection", floor=1, grid="K23",
                       note="Untagged supply point. The P&ID labels it 'CO2 FROM BLDG SUPPLY', but on the plant it is named 'compressed air' (DIFF). "
                            "HAZOP 1.5 also mentions a bottle being attached (GOI06).",
                       cite=[("PID", "'CO2 FROM BLDG SUPPLY', near grid K23"), ("DIFF", "row CO2 FROM BLDG SUPPLY (named 'compressed air', K23)")]),
    "N2_SUPPLY": dict(cls="SupplyConnection", label="N2 supply connection", floor=1,
                      note="Untagged supply point; the HAZOP N2 feed element starts at V127.", cite=[("HAZOP", "element 2 (N2 FEED, V127 to tee)")]),
    "V128": dict(cls="ManualValve", floor=1, pos="open", note="Start of the CO2 feed (HAZOP element 1). Not in the REPORT valve lists.",
                 cite=[("HAZOP", "element 1 (CO2 FEED, V128 to tee)")]),
    "PCV116": dict(cls="PressureControlValve", valve="pressure control", floor=1, grid="K22", pos="open",
                   note="CO2 pressure regulator, 0-10 bar output (HAZOP 1.7).",
                   cite=[("PID", "grid K22"), ("REPORT", VALVES + " (PCV116, K22, floor 1)"), ("HAZOP", "element 1, items 7 and 8")]),
    "FCV105": dict(cls="FlowControlValve", valve="flow control (mass flow controller)", floor=1, grid="K21", pos="open",
                   note="CO2 mass flow controller (FIC105); the 2010 HAZOP calls it FCV106.",
                   cite=[("PID", "grid K21"), ("REPORT", VALVES + " (FCV105, K21, floor 1)"), ("SUMMARY", "p.190 (FCV105 / FT105 / FIC105)"),
                         ("HAZOP", "element 1, items 3 and 6 ('FCV 106 (now FCV105)')")]),
    "NRV101": dict(cls="CheckValve", valve="check", floor=1, grid="K21", pos="open", note="Non-return valve on the CO2 line (HAZOP 1.1 calls the CO2 NRV 'NRV103').",
                   cite=[("PID", "grid K21"), ("REPORT", VALVES + " (NRV101, K21, floor 1)")]),
    "RV103": dict(cls="ReliefValve", valve="relief", floor=1, grid="K22", pos="closed",
                  note="Relief valve next to PCV116 on the CO2 line (REPORT grid). The 2010 HAZOP pairs RV103 (1 bar) with the N2 line, so the pairing and set pressure need checking (GOI05).",
                  cite=[("PID", "grid K22"), ("REPORT", VALVES + " (RV103, K22, floor 1)"), ("HAZOP", "element 2, item 8 ('RV103 at 1bar')")]),
    "V127": dict(cls="ManualValve", floor=1, grid="Q19", pos="open", note="Start of the N2 feed (HAZOP element 2).",
                 cite=[("PID", "grid Q19"), ("REPORT", VALVES + " (V127, Q19, floor 1)"), ("HAZOP", "element 2 (N2 FEED, V127 to tee)")]),
    "PCV117": dict(cls="PressureControlValve", valve="pressure control", floor=1, grid="P21", pos="open",
                   note="N2 header pressure regulator; its delivery line feeds several branches, each with a non-return valve (HAZOP 2.5).",
                   cite=[("PID", "grid P21"), ("REPORT", VALVES + " (PCV117, P21, floor 1)"), ("HAZOP", "element 2, items 5 and 10")]),
    "RV104": dict(cls="ReliefValve", valve="relief", floor=1, grid="P21", pos="closed",
                  note="Relief valve next to PCV117 on the N2 header (REPORT grid). The 2010 HAZOP pairs RV104 (10 bar) with the CO2 line (GOI05).",
                  cite=[("PID", "grid P21"), ("REPORT", VALVES + " (RV104, P21, floor 1)"), ("HAZOP", "element 1, item 7 ('RV104 at 10bar')")]),
    "PCV115": dict(cls="PressureControlValve", valve="pressure control", floor=1, grid="N22", pos="open",
                   note="N2 feed pressure regulator, 0-10 bar output (HAZOP 2.8).",
                   cite=[("PID", "grid N22"), ("REPORT", VALVES + " (PCV115, N22, floor 1)"), ("HAZOP", "element 2, item 8")]),
    "FCV116": dict(cls="FlowControlValve", valve="flow control (mass flow controller)", floor=1, grid="N21", pos="open",
                   note="N2 mass flow controller (FIC116). The 2010 HAZOP calls the N2 valve 'FCV107 (now FCV106)' (GOI04).",
                   cite=[("PID", "grid N21"), ("REPORT", VALVES + " (FCV116, N21, floor 1)"), ("SUMMARY", "p.190 (FCV116 / FT116 / FIC116)")]),
    "NRV102": dict(cls="CheckValve", valve="check", floor=1, grid="N20", pos="open", note="Non-return valve on the N2 line.",
                   cite=[("PID", "grid N20"), ("REPORT", VALVES + " (NRV102, N20, floor 1)")]),
    "FEED_GAS_HEADER": dict(cls="PipeSegment", label="Common N2 + CO2 inlet line to the plant (the HAZOP 'tee')", floor=1,
                            note="Untagged. HAZOP 1.2 / 2.1 added a bypass line for analysis on this common inlet (not modelled; GOI02).",
                            cite=[("HAZOP", "elements 1 and 2 ('to tee'; bypass line added on the common N2+CO2 inlet)")]),
    "K101": dict(cls="Saturator", label="K101 gas saturator", floor=1,
                 note="Saturates the feed gas with water before E101; temperature held by TIC121 using C106 on the recirculating water. "
                      "Grid not in the REPORT lists (near L17 to L18 on the P&ID). Not modelled in Aspen (GOI09).",
                 cite=[("SUMMARY", "p.190 ('Saturator K101 temperature (using C106)')"), ("HAZOP", "elements 3 (K101) and 4 (water recirculation)"),
                       ("REPORT", "section D.4 (TIC121 and C106)")]),
    "FCV111": dict(cls="FlowControlValve", valve="flow control", floor=1, grid="K17", pos="open",
                   note="Sets the K101 bypass rate, controlled by FIC304 from FT303/FT304 (control table). Its exact position is open item GOI03.",
                   cite=[("PID", "grid K17"), ("REPORT", VALVES + " (FCV111, K17, floor 1, open in operation)"), ("SUMMARY", "p.190 (FCV111 / FT303 / FT304 / FIC304 on K101 bypass rate)")]),
    "SDV170": dict(cls="ShutdownValve", valve="shutdown (solenoid-operated)", floor=1, grid="K17",
                   note="Next to FCV111 near the E101 gas inlet (P&ID shows SDV170 with HS170); the REPORT lists it as SOV170. Role and position: GOI03.",
                   cite=[("PID", "grid K17, SDV170 with HS170"), ("REPORT", VALVES + " (SOV170, K17, floor 1)")]),
    "NRV111": dict(cls="CheckValve", valve="check", floor=1, note="Non-return valve at the E101 gas inlet (P&ID, next to PSHH117). Position to confirm (GOI03).",
                   cite=[("PID", "E101 base, gas inlet side")]),
    "J104": dict(cls="Pump", label="J104 K101 water recirculation pump", floor=1, grid="O18",
                 note="Recirculates water over K101 (HAZOP element 4). A filter was added on its inlet (HAZOP 4.3).",
                 cite=[("PID", "grid O18"), ("REPORT", "pump list (J104, floor 1, O18)"), ("HAZOP", "element 4")]),
    "RV102": dict(cls="ReliefValve", valve="relief", floor=1, grid="N18", pos="closed", note="Relief on the J104 discharge (HAZOP 4.3).",
                  cite=[("PID", "grid N18"), ("REPORT", VALVES + " (RV102, N18, floor 1)"), ("HAZOP", "element 4, item 3")]),
    "C106": dict(cls="TrimCooler", label="C106 saturator water cooler", floor=1,
                 note="Cools the K101 recirculating water; cooling water flow set by FIC106 on FCV102 (cascade from TIC121).",
                 cite=[("SUMMARY", "p.190 (TIC121 using C106; FCV102 / FT106 / FIC106)"), ("REPORT", "section D.4")]),
    "FCV102": dict(cls="FlowControlValve", valve="flow control", floor=1, grid="Q16", pos="open",
                   note="Cooling water valve for C106. The REPORT valve tables give grids Q16 and R16.",
                   cite=[("PID", "grid Q16"), ("REPORT", VALVES + " (FCV102, Q16/R16, floor 1)"), ("SUMMARY", "p.190")]),
}

INSTRUMENTS = {
    "FT105": ("FlowInstrument", "CO2 feed mass flow", "thermal mass flow meter", "4-20mA", "K21", 1, "FCV105",
              [("PID", "grid K21"), ("REPORT", INSTR), ("SUMMARY", "p.190 (FT105, 'Sample 7')")]),
    "FT116": ("FlowInstrument", "N2 feed flow", None, None, None, 1, "FCV116", [("SUMMARY", "p.190 (FCV116 / FT116 / FIC116)")]),
    "TT121": ("TemperatureInstrument", "K101 saturator temperature", "PRT", "4-20mA", "L18", 1, "K101",
              [("PID", "grid L18"), ("REPORT", INSTR), ("SUMMARY", "p.190 (TT121 / TIC121)")]),
    "FT106": ("FlowInstrument", "cooling water flow to C106", "electromagnetic volumetric flow meter", "4-20mA", "R16", 1, "C106",
              [("PID", "grid R16"), ("REPORT", INSTR), ("SUMMARY", "p.190 (FT106 / FIC106)")]),
    "FT110": ("FlowInstrument", "K101 recirculating water flow", None, None, None, 1, "J104", [("HAZOP", "element 4, item 5 (FT110)")]),
    "FT303": ("FlowInstrument", "N2 flowrate entering E101", "vortex volumetric flow meter", "Fieldbus", "H17", 3, "E101",
              [("PID", "grid H17"), ("REPORT", INSTR), ("SUMMARY", "p.190 (FIC303, 'Nitrogen flowrate entering E101')")]),
    "FT304": ("FlowInstrument", "N2 flowrate entering E101", "thermal mass flow meter", "Profibus-PA", "H17", 3, "E101",
              [("PID", "grid H17"), ("REPORT", INSTR), ("SUMMARY", "p.190 (FT304 / FIC304)")]),
}

CONTROLLERS = {
    "FIC105": (["FCV105"], "CO2 feed flow controller (sets the CO2 concentration into the plant)", [("SUMMARY", "p.190")]),
    "FIC116": (["FCV116"], "N2 feed flow controller", [("SUMMARY", "p.190")]),
    "FIC303": (["FCV111"], "N2 flow into E101 controller (with FIC304)", [("SUMMARY", "p.190")]),
    "FIC304": (["FCV111"], "K101 bypass rate controller", [("SUMMARY", "p.190")]),
    "TIC121": (["FCV102"], "K101 saturator temperature controller (cascade master)", [("SUMMARY", "p.190")]),
    "FIC106": (["FCV102"], "C106 cooling water flow controller (cascade slave)", [("SUMMARY", "p.190")]),
}

NOZZLES = {"E101_N_gas_inlet": ("E101 gas inlet at the base of the column", [("PID", "E101 base"), ("ASPEN_V3", "stream 1 enters E101")], "E101")}

LOOP = [
    (("CO2_SUPPLY", "inline"), ("N2_SUPPLY", "inline")),
    (("V128", "inline"), ("V127", "inline")),
    (("PCV116", "inline"), ("PCV117", "inline")),
    (("FT105", "inline"), ("PCV115", "inline")),
    (("FCV105", "inline"), ("FCV116", "inline")),
    (("NRV101", "inline"), ("NRV102", "inline")),
    ("FEED_GAS_HEADER", "inline"),
    ("K101", "inline"), ("TT121", "tie-in"),
    ("E101_N_gas_inlet", "inline"),
    ("E101", "inline"),
]
TRAIN_A = ["CO2_SUPPLY", "V128", "PCV116", "FT105", "FCV105", "NRV101"]
TRAIN_B = ["N2_SUPPLY", "V127", "PCV117", "PCV115", "FCV116", "NRV102"]
EXTRA_PIPING = [("PCV116", "RV103"), ("PCV117", "RV104"),
                ("FEED_GAS_HEADER", "FCV111"), ("FCV111", "E101_N_gas_inlet"),            # K101 bypass (inferred)
                ("K101", "J104"), ("J104", "C106"), ("C106", "K101"), ("J104", "RV102")]  # K101 water loop (order inferred)
LINKS = [("RV102", "protects", "J104"), ("RV103", "protects", "PCV116"), ("RV104", "protects", "PCV117")]
KNOWN_TAGS = ["RV400", "E101"]

BYPASSES = {
    "K101_bypass": dict(label="K101 bypass via FCV111 (control table: 'on K101 bypass rate')", from_item="FEED_GAS_HEADER", via=["FCV111"],
                        to_item="E101_N_gas_inlet", bypasses=["K101"], state="modulating", procedure=None,
                        cite=[("SUMMARY", "p.190 (FCV111 / FIC304 on K101 bypass rate)"), ("DERIVED", INFERRED)]),
}

CONTROL_LOOPS = {
    "CL_CO2_feed": dict(label="CO2 feed rate (CO2 concentration into the plant)", sensors=["FT105"], controllers=["FIC105"], final=["FCV105"],
                        cv="CO2 feed rate", mv="FCV105 opening", cite=[("SUMMARY", "p.190")]),
    "CL_N2_feed": dict(label="N2 feed rate", sensors=["FT116"], controllers=["FIC116"], final=["FCV116"],
                       cv="Nitrogen feed rate", mv="FCV116 opening", cite=[("SUMMARY", "p.190")]),
    "CL_N2_to_E101": dict(label="N2 flowrate entering E101 (on K101 bypass rate)", sensors=["FT303", "FT304"], controllers=["FIC303", "FIC304"],
                          final=["FCV111"], cv="Nitrogen flowrate entering E101", mv="K101 bypass rate (FCV111)", cite=[("SUMMARY", "p.190")]),
    "CL_K101_temperature": dict(label="K101 saturator temperature (cascade master)", sensors=["TT121"], controllers=["TIC121"], final=["FCV102"],
                                cv="Saturator K101 temperature", mv="Cooling water flow set point for FIC106", cite=[("SUMMARY", "p.190")]),
    "CL_C106_cooling_water": dict(label="Cooling water flow to C106 (cascade slave)", sensors=["FT106"], controllers=["FIC106"], final=["FCV102"],
                                  cv="Flowrate of cooling water to C106", mv="FCV102 opening", cite=[("SUMMARY", "p.190")]),
}
CASCADES = [("CL_K101_temperature", "CL_C106_cooling_water")]

LIMITS = {
    "PCV116_output": ("PCV116", "pressure", "range", 0.0, 10.0, "bar", [("HAZOP", "element 1, item 7 (PCV116 0-10 bar output range)")]),
    "PCV115_output": ("PCV115", "pressure", "range", 0.0, 10.0, "bar", [("HAZOP", "element 2, item 8 (PCV115 0-10 bar output range)")]),
    "FAL_N2_feed": ("FCV116", "N2 feed flow", "alarm", None, None, "-", [("HAZOP", "element 2, item 9 (low flow alarm on the N2 flow controller added)")]),
    "LZAH_K101": ("K101", "level", "alarm", None, None, "-", [("HAZOP", "element 3, item 5 (LZAH104, now LZAH103; soft high alarm added)")]),
    "LAL_K101": ("K101", "level", "alarm", None, None, "-", [("HAZOP", "element 3, items 6 and 7 (LSL soft alarm added)")]),
    "LZAL_K101": ("K101", "level", "alarm", None, None, "-", [("HAZOP", "element 4, item 2 (LZAL on K101 added, not soft)")]),
}

DISCREPANCIES = [("CO2_supply_label", ["CO2_SUPPLY"], "K23", "Labelled 'CO2 FROM BLDG SUPPLY'", "Named 'compressed air'")]

HAZOP_ELEMENTS = {"1": "CO2 FEED (V128 to tee)", "2": "N2 FEED (V127 to tee)", "3": "K101",
                  "4": "WATER RECIRCULATION LOOP K101 to K101 via J104"}
HAZOP_COVERAGE = {"1": ["V128", "PCV116", "FCV105", "NRV101", "RV103"], "2": ["V127", "PCV117", "PCV115", "FCV116", "NRV102", "RV104"],
                  "3": ["K101"], "4": ["J104", "RV102", "FT110", "C106"]}
HAZOP_ALIASES = {"LZAH103": "K101", "LZAH104": "K101", "LIR104": "K101"}

OPEN_ITEMS = {
    "GOI01": ("Order of items on each supply line (regulator, flow meter, mass flow controller, non-return valve)", ["FCV105", "FCV116"], "Trace on the P&ID"),
    "GOI02": ("Where the common N2 + CO2 inlet goes after the tee (through K101 to the E101 base is inferred), and where the analysis bypass line is",
              ["FEED_GAS_HEADER", "K101"], "Trace on the P&ID"),
    "GOI03": ("Positions and roles of FCV111 (K101 bypass), SDV170 and NRV111 near the E101 gas inlet", ["FCV111", "SDV170", "NRV111"], "Trace on the P&ID"),
    "GOI04": ("Tag renumbering since 2010: HAZOP FCV106 = FCV105 (CO2) and FCV107 = FCV106 (N2), but the SUMMARY uses FCV116/FIC116 for N2 and FIC106 for C106 cooling water",
              ["FCV116", "FCV105"], "Instrument index or site check"),
    "GOI05": ("RV103 and RV104: which line each protects and their set pressures (HAZOP pairing contradicts the REPORT grids)", ["RV103", "RV104"],
              "Read the 'SET TO' values on the P&ID"),
    "GOI06": ("CO2 source: building supply (labelled 'compressed air', DIFF) or a bottle (HAZOP 1.5)", ["CO2_SUPPLY"], "Site check"),
    "GOI07": ("K101 water loop order (J104 > C106 > K101 assumed), where FT110 sits, and the K101 level instrument tags", ["K101", "J104", "C106"],
              "Trace on the P&ID"),
    "GOI08": ("FT303/FT304 are on floor 3 (H17) yet measure the N2 entering E101; they may be on the N2 return line (piece 7)", ["FT303", "FT304"],
              "Trace on the P&ID"),
    "GOI09": ("Aspen feeds the gas straight into E101 with no K101 saturator", ["K101"], "Note for model comparison"),
}

# Feed gas as specified in Aspen (stream 1). Inputs, so valid even for the unconverged v6.1 case.
PERFORMANCE = []
for key, doc, label in [("aspen_v3", "ASPEN_V3", "ABB_pilot_plant_final_3"), ("aspen_v6_1", "ASPEN_V61", "ABB_pilot_plant_final_6_1_SA_validation")]:
    s1 = json.load(open(ROOT / "data" / "aspen" / f"{key}.json"))["streams"].get("1")
    if s1:
        PERFORMANCE.append(dict(id=f"{key}_feed_gas", cls="FeedSpecification", label=f"Feed gas to E101 ({label})", equipment="E101", case=f"case_{key}",
                                props={"feedMassFlow_kg_h": float(s1["mass_flow_kg_h"]), "feedCO2_kg_h": float(s1["apparent_CO2_kg_h"]),
                                       "feedCO2MassFraction": float(s1["apparent_CO2_kg_h"] / s1["mass_flow_kg_h"]),
                                       "feedTemperature_C": float(s1["T_C"]), "feedPressure_bar": float(s1["P_bar"])},
                                note="Specified input (Aspen stream 1). Aspen has no K101, so this is the gas as it enters E101.",
                                cite=[(doc, "stream 1 (feed gas to E101)")]))

HAZOP_ROWS = [
    {"element": "1", "item": 1, "parameter": "FLOW", "guideword": "NO", "cause": "Seal failure in NRV103", "consequence": "No CO2 feed to plant; No means of depressurising line.", "safeguard": "Careful choice of sealing medium (AFLAS)", "action": "Consider manual vent valve", "action_taken": "Vent valve added"},
    {"element": "1", "item": 2, "parameter": "FLOW", "guideword": "NO", "cause": "FCV106 fail to open (electronic failure or valve seat problem)", "consequence": "No CO2 feed to plant; No means of depressurising line.", "safeguard": "All-metal seals in valve.  High MTBF for valve.", "action": "Put in a bypass line (for analysis) on the common N2+CO2 inlet to plant.", "action_taken": "Bypass line added"},
    {"element": "1", "item": 3, "parameter": "FLOW", "guideword": "MORE", "cause": "FCV 106 (now FCV105) jammed open", "consequence": "Wrong composition in plant", "safeguard": "Detectable by analysis", "action": "", "action_taken": ""},
    {"element": "1", "item": 4, "parameter": "FLOW", "guideword": "LESS", "cause": "As no flow", "consequence": "Wrong composition in plant", "safeguard": "Detectable by analysis", "action": "", "action_taken": ""},
    {"element": "1", "item": 5, "parameter": "FLOW", "guideword": "REVERSE", "cause": "Open inlet; NRV failure; no bottle attached.", "consequence": "Empty plant gas inventory via CO2 line", "safeguard": "Multiple failures", "action": "Operating procedures - cap off inlet when CO2 service disconnected", "action_taken": "Action complete"},
    {"element": "1", "item": 6, "parameter": "TEMP.", "guideword": "LOWER", "cause": "Excess flow", "consequence": "CO2 liquifying / solidifying", "safeguard": "none", "action": "Consider min operating safe temp of FCV106 (now FCV105)", "action_taken": "Action completed"},
    {"element": "1", "item": 7, "parameter": "PRESSURE", "guideword": "HIGHER", "cause": "PCV116 incorrectly set or defective", "consequence": "MFC off spec.", "safeguard": "PCV116 0-10 bar output range; RV104 at 10bar", "action": "", "action_taken": ""},
    {"element": "1", "item": 8, "parameter": "PRESSURE", "guideword": "LOWER", "cause": "CO2 cylinder exhausted; PCV116 incorrectly set or defective", "consequence": "none", "safeguard": "", "action": "", "action_taken": ""},
    {"element": "1", "item": 11, "parameter": "COMPOSITION", "guideword": "INCORRECT", "cause": "Wrong cylinder attached", "consequence": "", "safeguard": "SOPs", "action": "", "action_taken": ""},
    {"element": "2", "item": 1, "parameter": "FLOW", "guideword": "NO", "cause": "FCV107 (now FCV106) fail to open (electronic failure or valve seat problem)", "consequence": "No N2 feed to plant; No means of depressurising line; plant pressure control balance defeated.", "safeguard": "High MTBF for valve.", "action": "Put in a bypass line (for analysis) on the common N2 Co2 inlet to plant.  Consider soft low flow alarm on FIC107 (now FIC106).", "action_taken": "Bypass line added"},
    {"element": "2", "item": 2, "parameter": "FLOW", "guideword": "MORE", "cause": "FCV 107 jammed open", "consequence": "Wrong composition in plant", "safeguard": "Detectable by analysis", "action": "", "action_taken": ""},
    {"element": "2", "item": 3, "parameter": "FLOW", "guideword": "LESS", "cause": "As no flow", "consequence": "Wrong composition in plant", "safeguard": "Detectable by analysis", "action": "", "action_taken": ""},
    {"element": "2", "item": 4, "parameter": "FLOW", "guideword": "REVERSE", "cause": "NRV failure", "consequence": "", "safeguard": "", "action": "", "action_taken": ""},
    {"element": "2", "item": 5, "parameter": "FLOW", "guideword": "MISDIRECTED", "cause": "Backflow from PCV117", "consequence": "", "safeguard": "NRVs on all branches off PCV117 delivery line", "action": "", "action_taken": ""},
    {"element": "2", "item": 6, "parameter": "TEMP.", "guideword": "HIGHER", "cause": "", "consequence": "", "safeguard": "", "action": "", "action_taken": ""},
    {"element": "2", "item": 7, "parameter": "TEMP.", "guideword": "LOWER", "cause": "", "consequence": "", "safeguard": "", "action": "", "action_taken": ""},
    {"element": "2", "item": 8, "parameter": "PRESSURE", "guideword": "HIGHER", "cause": "PCV115 incorrectly set or defective", "consequence": "none", "safeguard": "PCV115 0-10 bar output range; RV103 at 1bar", "action": "Consider Need for RV103 v/v N2 supply (reposition d/s PCV 117?)", "action_taken": "Action completed"},
    {"element": "2", "item": 9, "parameter": "PRESSURE", "guideword": "LOWER", "cause": "N2 supply down, isolated or disconnected", "consequence": "Wrong composition in plant; plant depressurises", "safeguard": "none", "action": "Low flow alarm on FIC107", "action_taken": "low flow alarm added"},
    {"element": "2", "item": 10, "parameter": "COMPOSITION", "guideword": "INCORRECT", "cause": "Backflow from PCV117", "consequence": "", "safeguard": "NRVs", "action": "", "action_taken": ""},
    {"element": "3", "item": 1, "parameter": "TEMP.", "guideword": "HIGHER", "cause": "Warm CO2 entry & Recirculating water warming", "consequence": "More water required for saturation", "safeguard": "Heat loss to ATM", "action": "", "action_taken": ""},
    {"element": "3", "item": 2, "parameter": "PRESSURE", "guideword": "HIGHER", "cause": "Column at higher pressure", "consequence": "Compressor stall?", "safeguard": "PIC403; RV400", "action": "", "action_taken": ""},
    {"element": "3", "item": 3, "parameter": "PRESSURE", "guideword": "LOWER", "cause": "Column at lower pressure", "consequence": "", "safeguard": "PIC403", "action": "", "action_taken": ""},
    {"element": "3", "item": 4, "parameter": "PRESSURE", "guideword": "VACUUM", "cause": "As above", "consequence": "", "safeguard": "", "action": "", "action_taken": ""},
    {"element": "3", "item": 5, "parameter": "LEVEL", "guideword": "HIGHER", "cause": "Operator error (overfilling)", "consequence": "Damage to blower & compressor", "safeguard": "LZAH 104", "action": "LZAH104  (now LZAH103) needs to be below gas intakes; put soft alarms on LIR 104 (LSH); operating procs.", "action_taken": "Soft alarm added"},
    {"element": "3", "item": 6, "parameter": "LEVEL", "guideword": "LOWER", "cause": "Operator error (draining or not refilling)", "consequence": "Plant runs less efficiently;", "safeguard": "", "action": "LSL soft alarm", "action_taken": "Soft alarm added"},
    {"element": "3", "item": 7, "parameter": "LEVEL", "guideword": "NO", "cause": "", "consequence": "Plant runs less efficiently; damage J104", "safeguard": "", "action": "LSL soft alarm; consider exec action", "action_taken": "Soft alarm added"},
    {"element": "4", "item": 1, "parameter": "FLOW", "guideword": "NO", "cause": "Pump not functioning", "consequence": "Gas into plant not saturated", "safeguard": "", "action": "", "action_taken": ""},
    {"element": "4", "item": 2, "parameter": "FLOW", "guideword": "NO", "cause": "No water", "consequence": "pump damage", "safeguard": "LIs & SOPs", "action": "Soft LZAL on K101", "action_taken": "LZAL added, not soft."},
    {"element": "4", "item": 3, "parameter": "FLOW", "guideword": "NO", "cause": "Nozzle blocked", "consequence": "high P downstream of pump", "safeguard": "RV102", "action": "consider filter on pump inlet", "action_taken": "Filter added"},
    {"element": "4", "item": 4, "parameter": "FLOW", "guideword": "LESS", "cause": "As no flow", "consequence": "", "safeguard": "", "action": "", "action_taken": ""},
    {"element": "4", "item": 5, "parameter": "FLOW", "guideword": "MISDIRECTED", "cause": "RV jammed open", "consequence": "Gas into plant not saturated", "safeguard": "FT110", "action": "", "action_taken": ""},
    {"element": "4", "item": 6, "parameter": "TEMP.", "guideword": "HIGHER", "cause": "As K101", "consequence": "", "safeguard": "", "action": "", "action_taken": ""},
    {"element": "4", "item": 7, "parameter": "TEMP.", "guideword": "LOWER", "cause": "As K101", "consequence": "", "safeguard": "", "action": "", "action_taken": ""},
    {"element": "4", "item": 8, "parameter": "COMPOSITION", "guideword": "INCORRECT", "cause": "Hard water?", "consequence": "", "safeguard": "", "action": "Deionising cartridge on make-up water inlet d/s of NRVs", "action_taken": "Deionising cartridge added"},
]
