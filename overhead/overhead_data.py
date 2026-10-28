"""
Piece 4: stripper overhead and reflux (Pilot Plant 2514).

Vapour: top of E100 > PT401 > C400 condenser > LSHH400 > K401 knockout drum (demister)
        > gas out to the CO2 return (piece 7, via PT402 and PCV119)
Reflux: K401 > J300 > B300 (dead-end dampener) > PCV302 > TT309 > FT305 > joins the
        heater return at V403/V402 > top of E100. V317 is a branch off the reflux line.
Team trace (Oct 2026) with REPORT instrument/valve lists, SUMMARY control table (p.190),
DIFF (B300, LSHH400, TT309/FT305) and HAZOP element 12 (overheads).
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
INSTR = "Appendix B instrument list"
TRACE = "overhead and reflux traced on the P&ID (Oct 2026)"

SECTION = dict(
    prefix="ovh", loop_id="OverheadRefluxLoop", mode="FigureOfEight", flow="feedsInto",
    loop_label="Stripper overhead and reflux loop",
    loop_note="Runs whenever E100 is boiling. Vapour is condensed in C400; K401 separates the condensate (returned "
              "as reflux by J300) from the CO2-rich gas (to the CO2 return, piece 7).",
    loop_cite=[("PID", "E100 overhead to C400, K401 and J300, grids C8 to G10"), ("TEAM", TRACE),
               ("ASPEN_V3", "streams S13 > S11 (C400), C400COND (K401), S12 (reflux) and S16 (gas)")],
)

ITEMS = {
    "C400": dict(cls="Condenser", label="C400 overhead condenser (spiral heat exchanger)", floor=4,
                 note="Water-cooled; cooling water flow set by FIC402 on FCV401 (cascade from TIC410). Grid not in the REPORT lists (between C8 and E10 on the P&ID).",
                 cite=[("PID", "overhead line after PT401, top of the drawing"), ("SUMMARY", "p.110 (Spiral Heat Exchanger - C400) and p.190"),
                       ("DIFF", "row LSHH400 (between C400 and K401)"), ("ASPEN_V3", "block C400")]),
    "K401": dict(cls="KnockoutDrum", label="K401 knockout drum with demister", floor=4,
                 note="The vessel with the hatched demister symbol between C400 and J300. Its label is not legible on the team's P&ID copy; "
                      "the SUMMARY and DIFF call it K401. The 2010 HAZOP mentions both K400 and K401 (OOI01). Modelled in Aspen as the flash block C400COND.",
                 cite=[("PID", "vessel with hatched demister, near grid E10 to F10"), ("SUMMARY", "p.112 (Knock out Drum - Demister (K401))"),
                       ("DIFF", "row LSHH400 (between C400 and K401)"), ("TEAM", "hatched (demister) symbol inside the drum"), ("ASPEN_V3", "block C400COND")]),
    "J300": dict(cls="Pump", label="J300 reflux pump", floor=3, grid="G10",
                 note="Speed set by SIC300 from the K401 level (LT401, LIC401).",
                 cite=[("PID", "grid G10"), ("REPORT", "pump list (J300, floor 3, G10)"), ("SUMMARY", "p.190 (SIC300 / LT401 level control)"), ("TEAM", TRACE)]),
    "B300": dict(cls="PulsationDampener", label="B300 pulsation dampener on the J300 discharge", floor=3, grid="G9",
                 note="Dead-end branch (team trace). Operates at 3 bar, not the 8 bar shown near it on the P&ID; the 8 bar belongs to PCV302 (DIFF, team).",
                 cite=[("PID", "grid G9"), ("DIFF", "row B300 (operates at 3 bar not 8 bar, G9)"), ("TEAM", "B300 is a dead end; 8 bar is the PCV302 setting")]),
    "PCV302": dict(cls="PressureControlValve", valve="pressure control", floor=3, grid="G9", pos="open",
                   cite=[("PID", "grid G9, 'SET TO 8 bar'"), ("REPORT", "valve list (PCV302, G9, floor 3)"), ("TEAM", TRACE)]),
    "RV300": dict(cls="ReliefValve", valve="relief", floor=3, grid="G10", pos="closed", note="Relief on the J300 discharge, set to 10 bar.",
                  cite=[("PID", "grid G10, 'SET TO 10 bar'"), ("REPORT", "valve list (RV300, G10, floor 3)"), ("TEAM", "RV300 set to 10 bar")]),
    "V317": dict(cls="ManualValve", valve="ball", floor=3, grid="H9", pos="closed",
                 note="Branch off the reflux line, closed in operation. Where it leads is not identified (OOI02).",
                 cite=[("PID", "grid H9"), ("REPORT", "valve tables (ball, H9, floor 3, closed)"), ("TEAM", "V317 is a branch off the reflux line")]),
    "FCV401": dict(cls="FlowControlValve", valve="flow control", floor=4, grid="C12", pos="open",
                   note="Cooling water control valve for C400 (FIC402).",
                   cite=[("PID", "grid C12"), ("REPORT", "flow control valve list (C12, floor 4) and start-up tables"), ("SUMMARY", "p.190 (FCV401 / FT402 / FIC402)")]),
}

INSTRUMENTS = {
    "LSHH400": ("LevelInstrument", "level high-high switch on the overhead (C400 to K401)", None, None, "E10", 4, "K401",
                [("PID", "grid E10"), ("DIFF", "row LSHH400 (connected between C400 and K401, E10)")]),
    "LT401": ("LevelInstrument", "liquid level in K401 (control table: 'liquid level in condenser C400')", "differential pressure transmitter", "4-20mA", "F10", 4, "K401",
              [("PID", "grid F10"), ("REPORT", INSTR), ("SUMMARY", "p.190 (LT401 / LIC401)")]),
    "TT310": ("TemperatureInstrument", "temperature at the J300 discharge", "PRT", "4-20mA", "G9", 3, "J300", [("PID", "grid G9"), ("REPORT", INSTR)]),
    "TT410": ("TemperatureInstrument", "temperature of CO2 leaving C400", "PRT", "Fieldbus", "C15", 4, "C400",
              [("PID", "grid C15"), ("REPORT", INSTR), ("SUMMARY", "p.190 (TT410 / TIC410)")]),
    "FT402": ("FlowInstrument", "cooling water flow to C400", None, None, None, 4, "C400",
              [("SUMMARY", "p.190 (FCV401 / FT402 / FIC402)"), ("HAZOP", "element 12, item 7 (FT401 now FT402)")]),
    "FI401": ("FlowInstrument", "cooling water flow indication for C400", None, None, "C14", 4, "C400",
              [("PID", "grid C14"), ("REPORT", "instrument list (FI401, C14, floor 4)")]),
}

CONTROLLERS = {
    "LIC401": (["J300"], "K401 level controller (PV LT401)", [("SUMMARY", "p.190")]),
    "SIC300": (["J300"], "J300 speed controller", [("SUMMARY", "p.190")]),
    "TIC410": (["FCV401"], "C400 gas outlet temperature controller (cascade master)", [("SUMMARY", "p.190")]),
    "FIC402": (["FCV401"], "C400 cooling water flow controller (cascade slave)", [("SUMMARY", "p.190")]),
}

NOZZLES = {
    "E100_N_overhead": ("E100 vapour outlet at the top of the column", [("PID", "top of E100, grid F7"), ("TEAM", TRACE)], "E100"),
    "K401_N_gas_outlet": ("K401 gas outlet to the CO2 return (piece 7)", [("PID", "top of K401"), ("TEAM", TRACE)], "K401"),
}

LOOP = [
    ("E100", "inline"),
    ("E100_N_overhead", "inline"),
    ("PT401", "tie-in"),
    ("C400", "inline"),
    ("LSHH400", "tie-in"),
    ("K401", "inline"), ("LT401", "tie-in"),
    ("J300", "inline"), ("TT310", "tie-in"), ("RV300", "branch"), ("B300", "tie-in"),
    ("PCV302", "inline"), ("V317", "branch"),
    ("TT309", "tie-in"),           # DIFF: TT309 is below FT305 and the reflux flows upwards, so TT309 comes first
    ("FT305", "inline"),
    ("V403", "inline"), ("V402", "inline"), ("E100_N_top_inlet", "inline"),
    ("E100", "inline"),
]
EXTRA_PIPING = [("K401", "K401_N_gas_outlet"), ("J300", "RV300"), ("J300", "B300"), ("PCV302", "V317")]
LINKS = [("FT305", "monitors", "J300"), ("TT309", "monitors", "J300"), ("PT402", "monitors", "K401"),
         ("PT401", "monitors", "C400"), ("RV300", "protects", "J300")]
KNOWN_TAGS = ["PT401", "PT402", "PCV119", "FT305", "TT309"]   # add "J103" once piece 7 defines it

CONTROL_LOOPS = {
    "CL_K401_level": dict(label="K401 level (J300 speed)", sensors=["LT401"], controllers=["LIC401", "SIC300"], final=["J300"],
                          cv="Liquid level in K401 (condenser hold-up)", mv="Speed of J300", cite=[("SUMMARY", "p.190")]),
    "CL_C400_temperature": dict(label="Temperature of CO2 leaving C400 (cascade master)", sensors=["TT410"], controllers=["TIC410"],
                                final=["FCV401"], cv="Temperature of CO2 exiting C400", mv="Cooling water flow set point for FIC402",
                                cite=[("SUMMARY", "p.190")]),
    "CL_C400_cooling_water": dict(label="Cooling water flow to C400 (cascade slave)", sensors=["FT402"], controllers=["FIC402"],
                                  final=["FCV401"], cv="Cooling water flowrate to C400", mv="FCV401 opening", cite=[("SUMMARY", "p.190")]),
}
CASCADES = [("CL_C400_temperature", "CL_C400_cooling_water")]

LIMITS = {
    "RV300_set": ("RV300", "pressure", "relief", None, 10.0, "bar", [("PID", "grid G10, 'SET TO 10 bar'"), ("TEAM", "RV300 set to 10 bar")]),
    "PCV302_set": ("PCV302", "pressure", "setpoint", None, 8.0, "bar", [("PID", "grid G9, 'SET TO 8 bar'"), ("TEAM", "8 bar is the PCV302 setting")]),
    "B300_operating": ("B300", "pressure", "operating", None, 3.0, "bar", [("DIFF", "row B300 (operates at 3 bar not 8 bar)")]),
    "PDAH_K401_demister": ("K401", "differential pressure", "alarm", None, None, "bar",
                           [("HAZOP", "element 12, item 2 (PDAH between PT402 and PT401 for a blocked demister; added)")]),
    "FAL_FT402": ("FT402", "cooling water flow", "alarm", None, None, "-", [("HAZOP", "element 12, item 7 (FAL on FT402 for low coolant flow to C400)")]),
    "LZAH_K401": ("LSHH400", "level", "alarm", None, None, "-", [("HAZOP", "element 12, item 8 (LZAH added; HAZOP calls the vessel K400)")]),
    "LAL_K401": ("LT401", "level", "alarm", None, None, "-", [("HAZOP", "element 12, item 9 (LAL added; HAZOP calls the vessel K400)")]),
}

DISCREPANCIES = [
    ("B300_pressure", ["B300"], "G9", "8 bar shown next to B300", "B300 operates at 3 bar"),
    ("LSHH400_location", ["LSHH400"], "E10", "LSHH400 drawn elsewhere", "LSHH400 between C400 and K401"),
    ("TT309_FT305_order", ["TT309", "FT305"], "F9", "TT309 above FT305", "TT309 below FT305"),
]

HAZOP_ELEMENTS = {"12": "OVERHEADS to C300 (400)"}
HAZOP_COVERAGE = {"12": ["C400", "K401", "LSHH400", "LT401", "PT401", "PT402", "FT402", "J300"]}
HAZOP_ALIASES = {"FT401": "FT402", "C300": "C400", "K400": "K401"}

OPEN_ITEMS = {
    "OOI01": ("K401's label is not legible on the team's P&ID copy, and the 2010 HAZOP mentions both K400 and K401: is there a second pot?", ["K401"],
              "Full-size P&ID or site check"),
    "OOI02": ("Where V317 (branch off the reflux line) leads", ["V317"], "Full-size P&ID around grid H9, or site check"),
    "OOI03": ("Exactly where the reflux joins the solvent line at V403/V402", ["FT305", "V403"], "Full-size P&ID around grid F8"),
    "OOI04": ("Aspen returns the reflux to the rich feed before the heaters (MIXER2), but on the P&ID it joins after them at V403/V402", ["J300", "C400"],
              "Note for model comparison; update the Aspen flowsheet if needed"),
    "OOI05": ("Set points of the PDAH (demister), FAL (FT402), LZAH and LAL alarms are not documented", ["K401", "FT402", "LSHH400", "LT401"],
              "Control system settings"),
    "OOI06": ("C400 and K401 grid references are not in the REPORT lists (estimated from the P&ID)", ["C400", "K401"], "Full-size P&ID"),
}

# Aspen results: C400 duty and the K401 (C400COND) split. Converged case (v3) only: v6.1 did not
# converge and gives unphysical overhead values (negative condenser duty, almost no gas).
PERFORMANCE = []
for key, doc, label in [("aspen_v3", "ASPEN_V3", "ABB_pilot_plant_final_3")]:
    st = json.load(open(ROOT / "data" / "aspen" / f"{key}.json"))["streams"]
    if all(k in st for k in ("S13", "S11", "S12", "S16")):
        PERFORMANCE.append(dict(id=f"{key}_C400_performance", cls="HeatExchangerPerformance", label=f"C400 performance ({label})",
                                equipment="C400", case=f"case_{key}",
                                props={"duty_kW": (st["S13"]["enthalpy_flow_W"] - st["S11"]["enthalpy_flow_W"]) / 1000,
                                       "hotInlet_C": float(st["S13"]["T_C"]), "hotOutlet_C": float(st["S11"]["T_C"])},
                                note="Process side only; Aspen models C400 as a heater block, so the cooling water side is not simulated.",
                                cite=[(doc, "streams S13 and S11; calculated in overhead_data.py")]))
        PERFORMANCE.append(dict(id=f"{key}_K401_performance", cls="SeparatorPerformance", label=f"K401 split ({label})",
                                equipment="K401", case=f"case_{key}",
                                props={"condensate_kg_h": float(st["S12"]["mass_flow_kg_h"]), "offgas_kg_h": float(st["S16"]["mass_flow_kg_h"]),
                                       "offgasCO2_kg_h": float(st["S16"]["apparent_CO2_kg_h"]),
                                       "offgasCO2MassFraction": float(st["S16"]["apparent_CO2_kg_h"] / st["S16"]["mass_flow_kg_h"]),
                                       "refluxRatio": float(st["S12"]["mass_flow_kg_h"] / st["S16"]["mass_flow_kg_h"])},
                                note="Aspen block C400COND (flash) stands for K401.",
                                cite=[(doc, "streams S11, S12 and S16 (block C400COND); calculated in overhead_data.py")]))

HAZOP_ROWS = [
    {"element": "12", "item": 1, "parameter": "FLOW", "guideword": "NO", "cause": "Insufficient boiling in H100", "consequence": "", "safeguard": "", "action": "", "action_taken": ""},
    {"element": "12", "item": 2, "parameter": "FLOW", "guideword": "NO", "cause": "Blockage of K401 demister unit", "consequence": "No gas flow to compressor", "safeguard": "spillback around compressor", "action": "PDAH differential pressure alarm between PT402 and PT401", "action_taken": "PDAH added"},
    {"element": "12", "item": 3, "parameter": "FLOW", "guideword": "MORE", "cause": "Excessive boiling", "consequence": "Excess vapour carry-over to J103", "safeguard": "Excess waterflow through C300", "action": "Develop operating window during & post commissioning", "action_taken": "K400 & K401 added"},
    {"element": "12", "item": 4, "parameter": "FLOW", "guideword": "LESS", "cause": "Insufficient boiling in H100", "consequence": "", "safeguard": "", "action": "", "action_taken": ""},
    {"element": "12", "item": 5, "parameter": "TEMP.", "guideword": "HIGHER", "cause": "Higher pressure in column", "consequence": "", "safeguard": "", "action": "", "action_taken": ""},
    {"element": "12", "item": 6, "parameter": "TEMP.", "guideword": "LOWER", "cause": "Reduced pressure in column", "consequence": "Efficiency reduced?", "safeguard": "", "action": "", "action_taken": ""},
    {"element": "12", "item": 7, "parameter": "PRESSURE", "guideword": "HIGHER", "cause": "C300 failure to function", "consequence": "", "safeguard": "", "action": "Put FAL on FT401 (now FT402) to indicate low coolant flow thro C300 (now C400)", "action_taken": "Action complete"},
    {"element": "12", "item": 8, "parameter": "LEVEL", "guideword": "HIGHER", "cause": "Blockage of FCV402", "consequence": "Damage to J103", "safeguard": "Level controlled in K400", "action": "put LZAH on K400", "action_taken": "LZAH added"},
    {"element": "12", "item": 9, "parameter": "LEVEL", "guideword": "LOWER", "cause": "control valve open too much", "consequence": "Backflow through FCV402 - bypass cooler", "safeguard": "", "action": "put LAL on K400", "action_taken": "LAL added"},
    {"element": "12", "item": 10, "parameter": "LEVEL", "guideword": "NO", "cause": "as lower", "consequence": "", "safeguard": "", "action": "", "action_taken": ""},
]
