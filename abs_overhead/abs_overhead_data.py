"""
Piece 6: absorber overhead (Pilot Plant 2514). Built from the documents first, then traced by the team.

Gas route:  top of E101 > TT412 / TT413 > K402 cyclone separator (demister pad; liquid back to E101)
            > PT403 > PCV300 (absorber pressure, 'on vent rate') > vent.
            Part of the K402 gas goes to the N2 return (J102, piece 7) instead of the vent.
Relief:     RV400 (E101) and RV401 (E100) > K403 knockout drum (not on the P&ID, DIFF).
Sources: REPORT instrument/valve lists, vent stream start-up table (Fig F.3), absorber pressure control (D.18/D.19);
SUMMARY p.114 (Cyclone Separator - K402) and p.190; DIFF (K403, FT301/FT302, V313/V310); HAZOP 3, 5 and 10.
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
INSTR = "Appendix B instrument list"
VALVES = "valve lists"
VENT_TABLE = "Fig F.3 (vent stream start-up valve positions)"

SECTION = dict(
    prefix="aov", loop_id="AbsorberOverheadRoute", mode="FigureOfEight", flow="feedsInto",
    loop_label="Absorber overhead and vent route",
    loop_note="Lean gas leaves the top of E101, passes the K402 cyclone separator (liquid returns to E101) and is vented "
              "through PCV300, which holds the E101 pressure (PIC403). Part of the gas goes to the N2 return (piece 7); "
              "where it splits from the vent line is to be traced (AV01).",
    loop_cite=[("REPORT", "section D.4 absorber pressure control (PCV300 varies 'the amount of lean gas being vented') and " + VENT_TABLE),
               ("SUMMARY", "p.114 (Cyclone Separator - K402) and p.190 (PCV300 / PT403 / PIC403 on vent rate)"),
               ("DERIVED", "order along the overhead line is to be traced on the P&ID")],
)

ITEMS = {
    "K402": dict(cls="CycloneSeparator", label="K402 cyclone separator on the E101 overhead", floor=4,
                 note="Removes liquid carried over from E101 (demister pad; oversized liquid return to E101, HAZOP 5.9). A tuning-fork liquid level "
                      "switch and trip were added downstream of it (HAZOP 10.1). Grid not in the REPORT lists.",
                 cite=[("PID", "top of E101"), ("SUMMARY", "p.114 (Cyclone Separator - K402)"), ("HAZOP", "element 5, item 9 and element 10, items 1 and 5")]),
    "PCV300": dict(cls="PressureControlValve", valve="pressure control", floor=3, grid="G18", pos="open",
                   note="Vents lean gas from the absorber to hold the E101 pressure (PIC403). Opened in the vent stream start-up (Fig F.3), closed at shutdown.",
                   cite=[("PID", "grid G18"), ("REPORT", VALVES + " (PCV300, G18, floor 3), " + VENT_TABLE + " and section D.4"),
                         ("SUMMARY", "p.190 (PCV300 / PT403 / PIC403 on vent rate)")]),
    "V409": dict(cls="ManualValve", valve="ball", floor=4, grid="E16", pos="open", props={"hasLockingHandle": True},
                 note="Locked ball valve on the vent stream, opened first at start-up (Fig F.3). The lean MEA list gives D16 and closed (AV04).",
                 cite=[("PID", "grid E16"), ("REPORT", VENT_TABLE + " (V409 (L), E16, floor 4, open) and " + VALVES + " (D16, closed)")]),
    "V310": dict(cls="ManualValve", valve="3-way ball", floor=3, grid="F17", pos="open",
                 note="3-way valve on the overhead gas side (F17). DIFF: the branch drawn to V313 is really connected at V310 (AV03).",
                 cite=[("PID", "grid F17"), ("REPORT", VALVES + " (V310, 3-way ball, F17, floor 3, open in operation)"), ("DIFF", "row V313 & V310 (F17 and G17)")]),
    "V313": dict(cls="ManualValve", valve="3-way ball", floor=3, grid="F17", pos="open",
                 note="3-way valve next to V310 (F17). DIFF: the branch drawn here is really connected at V310 (AV03).",
                 cite=[("PID", "grid F17"), ("REPORT", VALVES + " (V313, 3-way ball, F17, floor 3, open in operation)"), ("DIFF", "row V313 & V310 (F17 and G17)")]),
    "V408": dict(cls="ManualValve", valve="needle", floor=4, grid="F16", pos="closed",
                 note="Needle valve at the top of E101 (next to TT411 on the P&ID). Taken to be the sample 1 valve, following the pattern of the other "
                      "E101 sample valves V308, V306, V207 and V205 (AV05).",
                 cite=[("PID", "top of E101, next to TT411"), ("REPORT", VALVES + " (V408, needle, F16/G16, floor 4)"),
                       ("DERIVED", "sample 1 valve by the pattern of the other needle sample valves")]),
    "K403": dict(cls="KnockoutDrum", label="K403 relief knockout drum (RV400 and RV401)", floor=4, grid="E15",
                 note="Not drawn on the P&ID (DIFF). Collects the discharge of RV400 (E101) and RV401 (E100).",
                 cite=[("DIFF", "row K403 (not included in the original P&ID; E15/16 for RV400 and E7 for RV401)")]),
    "VENT_E101": dict(cls="VentConnection", label="Absorber vent ('VENT VI' to drawing 108712-10-002)", floor=3,
                      note="Untagged vent outlet downstream of PCV300; where it discharges is AV07.",
                      cite=[("PID", "'VENT VI' arrow near PCV300"), ("REPORT", "section D.4 (lean gas vented out of the process)")]),
}

INSTRUMENTS = {
    "TT412": ("TemperatureInstrument", "E101 top temperature", "PRT", "Fieldbus", "F15", 4, "E101", [("PID", "top of E101"), ("REPORT", INSTR + " (TT412, F15, floor 4)")]),
    "TT413": ("TemperatureInstrument", "E101 top temperature (sample point 1)", "PRT", "Fieldbus", "E16", 4, "E101",
              [("PID", "top of E101 / overhead"), ("REPORT", INSTR + " (TT413, E16, floor 4) and Fig 4.1")]),
    "PT403": ("PressureInstrument", "absorber (E101) pressure", "gauge pressure transmitter", "Fieldbus", "D16", 4, "E101",
              [("PID", "grid D16"), ("REPORT", INSTR + " (PT403, D16, floor 4) and section D.4"), ("SUMMARY", "p.190 (PT403 / PIC403)")]),
    "FT300": ("FlowInstrument", "gas flow on the overhead side", "thermal mass flow meter", "Fieldbus", "G18", 3, "K402",
              [("PID", "grid G18"), ("REPORT", INSTR + " (FT300, G18, floor 3)")]),
    "FT301": ("FlowInstrument", "gas flow on the overhead side", "swirl volumetric flow meter", "Fieldbus", "G20", 3, "K402",
              [("PID", "grid G20"), ("REPORT", INSTR + " (FT301, G20, floor 3)"), ("DIFF", "row FT 301 & FT 302 (order reversed, G20)")]),
    "FT302": ("FlowInstrument", "gas flow on the overhead side", "thermal mass flow meter", "Profibus-DP", "G18", 3, "K402",
              [("PID", "grid G18"), ("REPORT", INSTR + " (FT302, G18, floor 3)"), ("DIFF", "row FT 301 & FT 302 (order reversed, G20)")]),
}

CONTROLLERS = {"PIC403": (["PCV300"], "Absorber (E101) pressure controller (on vent rate)", [("SUMMARY", "p.190"), ("REPORT", "section D.4")])}

NOZZLES = {
    "E101_N_gas_outlet": ("E101 gas outlet at the top of the column", [("PID", "top of E101"), ("ASPEN_V3", "stream 4 leaves E101")], "E101"),
    "K402_N_gas_to_return": ("K402 gas outlet to the N2 return (piece 7)", [("HAZOP", "element 5 (N2 return E101 to E101 via K402, J102 and K101)")], "K402"),
}

LOOP = [
    ("E101", "inline"),
    ("E101_N_gas_outlet", "inline"),
    ("TT412", "tie-in"), ("TT413", "tie-in"),
    ("K402", "inline"),
    ("PT403", "tie-in"),
    ("V409", "branch"),
    ("PCV300", "inline"),
    ("FT300", "tie-in"), ("FT302", "tie-in"),
    ("VENT_E101", "inline"),
]
EXTRA_PIPING = [("K402", "E101"),                       # liquid return to E101 (HAZOP 5.9)
                ("K402", "K402_N_gas_to_return"),       # gas to the N2 return (piece 7)
                ("E101", "RV400"), ("RV400", "K403"), ("RV401", "K403")]
LINKS = [("E101_sample_1", "sampleValve", "V408"),
         ("HAZOP_10_01", "concerns", "K402"), ("HAZOP_10_05", "concerns", "K402"),
         ("HAZOP_3_02", "concerns", "PIC403"), ("HAZOP_3_03", "concerns", "PIC403")]

CONTROL_LOOPS = {
    "CL_E101_pressure": dict(label="Absorber (E101) pressure (on vent rate)", sensors=["PT403"], controllers=["PIC403"], final=["PCV300"],
                             cv="Pressure in E101", mv="Opening of PCV300 (lean gas vent rate)",
                             cite=[("SUMMARY", "p.190 (PCV300 / PT403 / PIC403 on vent rate)"),
                                   ("REPORT", "section D.4 and Fig D.19 (the table says 'stripper E101'; E101 is the absorber)")]),
}

DISCREPANCIES = [
    ("K403_not_on_PID", ["K403"], "E15/16", "K403 not drawn", "K403 knockout drum on the RV400 and RV401 discharges"),
    ("FT301_FT302_order", ["FT301", "FT302"], "G20", "FT301 then FT302", "Order reversed"),
    ("V313_V310_branch", ["V313", "V310"], "F17/G17", "Branch connected to V313", "Branch connected at V310"),
]

OPEN_ITEMS = {
    "AV01": ("The order of items on the E101 overhead line, and where the gas splits between the vent (PCV300) and the N2 return (J102, piece 7)",
             ["K402", "PCV300"], "Trace on the P&ID"),
    "AV02": ("Where FT300, FT301 and FT302 sit (vent line or N2 return), given that DIFF says FT301 and FT302 are in the reverse order", ["FT300", "FT301", "FT302"],
             "Trace on the P&ID"),
    "AV03": ("What the 3-way valves V310 and V313 switch between (DIFF: the branch drawn to V313 is connected at V310)", ["V310", "V313"], "Trace on the P&ID"),
    "AV04": ("V409: open in the vent start-up table but closed in the lean MEA list; its exact position on the vent line", ["V409"], "Trace on the P&ID"),
    "AV05": ("V408 is assumed to be the sample 1 valve (pattern of the other needle sample valves)", ["V408"], "Full-size P&ID"),
    "AV06": ("RV400 set pressure and how K403 drains are not documented", ["RV400", "K403"], "Site check or relief valve datasheet"),
    "AV07": ("Where the absorber vent discharges ('VENT VI' to drawing 108712-10-002)", ["VENT_E101"], "Drawing 108712-10-002"),
    "AV08": ("Where the K402 liquid return enters E101", ["K402"], "Trace on the P&ID"),
}

# Treated (lean) gas leaving the top of E101 in Aspen (stream 4), converged case only
PERFORMANCE = []
st = json.load(open(ROOT / "data" / "aspen" / "aspen_v3.json"))["streams"]
if "4" in st:
    s4 = st["4"]
    PERFORMANCE.append(dict(id="aspen_v3_vent_gas", cls="VentGasPerformance", label="Lean gas leaving E101 (ABB_pilot_plant_final_3)",
                            equipment="E101", case="case_aspen_v3",
                            props={"ventGas_kg_h": float(s4["mass_flow_kg_h"]), "ventGasCO2_kg_h": float(s4["apparent_CO2_kg_h"]),
                                   "ventGasTemperature_C": float(s4["T_C"])},
                            note="Aspen stream 4 (E101 overhead). Aspen has no K402, PCV300 or N2 return, so this is all the gas leaving the top of E101.",
                            cite=[("ASPEN_V3", "stream 4 (E101 overhead)")]))
