"""
Plant data for the stripping loop KG (Pilot Plant 2514).

Everything the build script needs is in plain Python tables here, so the
data can be checked line by line against the sources:

  P&ID     marked-up P&ID (Pilot Plant 2514) checked with the team
  DIFF     P_ID_Differences.pdf (as-built corrections)
  REPORT   PilotPlantReport_Group6_2_0.pdf
  SUMMARY  Carbon_Capture_plant_summary_2023-2024_v01.pdf (control-loop table)
  HAZOP    27794_Plant_HAZREP (2010)
"""

UNVERIFIED = "Value read from a low-resolution P&ID image; check against the full-size drawing."

# ---------------------------------------------------------------------------
# Equipment: tag -> (class, label, extra properties)
# ---------------------------------------------------------------------------
EQUIPMENT = {
    "E100": ("StrippingColumn", "E100 stripper (desorber)",
             dict(diameter_mm=264.62, floor=1,
                  note="Chimney tray below the bottom packed bed separates the draw-off section (stage 11) from the sump (stage 12).")),
    "H100": ("SteamReboiler", "H100 vertical thermosiphon steam reboiler",
             dict(floor=1, source="SUMMARY p.102")),
    "C100": ("LeanRichExchanger", "C100 lean/rich interchanger (gasketed plate heat exchanger)",
             dict(floor=1, source="SUMMARY p.106; REPORT section 3",
                  note="Hot side carries lean MEA from E100. In the stripping loop the rich (cold) side has no flow from the absorber. REPORT puts C100 efficiency at about 95 %.")),
    "J100": ("Pump", "J100 lean MEA pump", dict(floor=1, gridReference="M10",
             note="Speed set by SIC100. HAZOP 7.11 refers to diaphragm changes.")),
    "B101": ("PulsationDampener", "B101 pulsation dampener", dict(floor=1)),
    "Z102": ("Filter", "Z102 MEA filter", dict(floor=1, filterRating_um=50.0)),
    "H200a": ("ElectricHeater", "H200a electric heater", dict(floor=2, gridReference="J10")),
    "H200b": ("ElectricHeater", "H200b electric heater", dict(floor=2, gridReference="J11")),
}

# ---------------------------------------------------------------------------
# Valves: tag -> (class, valveType, floor, grid, position in stripping loop, label/note)
# Positions come from REPORT Fig E.1/E.2 (commissioning test = stripping loop line-up).
# ---------------------------------------------------------------------------
BALL_NOTE = "REPORT start-up tables (Fig F.7, F.21) list this as a ball valve; REPORT Fig B.29 lists it as a globe valve."
VALVES = {
    "V110": ("ManualValve", "ball", 1, "L7", "open", BALL_NOTE),
    "V112": ("ManualValve", "ball", 1, "M8", "open", BALL_NOTE),
    "V113a": ("ManualValve", "ball", 1, "M9", "open", BALL_NOTE),
    "V113b": ("ManualValve", "ball", 1, "M10", "open", BALL_NOTE),
    "V116": ("ManualValve", "ball", 1, "M11", "open", BALL_NOTE),
    "V117a": ("ManualValve", "ball", 1, "M11", "open", "Upstream isolation for Z102. " + BALL_NOTE),
    "V117b": ("ManualValve", "ball", 1, "M11", "open", "Downstream isolation for Z102. " + BALL_NOTE),
    "V120": ("ManualValve", "ball", 1, "L11", "closed", "Z102 bypass valve. " + BALL_NOTE),
    "V121": ("ManualValve", "ball", 1, "M11", "open", BALL_NOTE),
    "V403": ("ManualValve", "ball", 3, "F8", "open", "REPORT Fig B.24 gives floor 4; DIFF and REPORT Fig E.2 give floor 3."),
    "V402": ("ManualValve", "ball", 3, "F8", "open", "REPORT Fig B.24 gives floor 4; DIFF and REPORT Fig E.2 give floor 3."),
    "V315": ("ManualValve", "ball", 3, "G10", "closed", "Vent branch at top of heater riser (locked)."),
    "V316": ("ManualValve", "ball", 3, "G10", "closed", "Vent branch at top of heater riser. Closed in the stripping loop test (REPORT Fig E.1); opened in the full-plant gas start-up (REPORT Fig F.13)."),
    "SOV125": ("SolenoidValve", "solenoid", 1, "L11", "open", "Route from J100 discharge to H200a/b and E100 (stripping loop)."),
    "SOV123": ("SolenoidValve", "solenoid", 1, "L9", "closed", "Route from J100 discharge to C200 and the absorber; closed in the stripping loop."),
    "PCV122": ("PressureControlValve", "pressure control", 1, "M10", "open", None),
    "RV101": ("ReliefValve", "relief", 1, "L10", "closed", "Relief on J100 discharge."),
    "RV401": ("ReliefValve", "relief", 4, "F7", "closed", "E100 relief; discharges to knockout drum K403 (DIFF)."),
    "FCV110": ("FlowControlValve", "flow control", 1, "L5", "closed", "Steam control valve for H100, named ZS110 on site (DIFF). Closed in the stripping loop test: no steam (REPORT Fig E.1, F.5.4.3)."),
    "PCV119": ("PressureControlValve", "pressure control", 1, "K19", "open", "E100 pressure control valve on the overhead line (boundary of the loop)."),
    # steam-side valves used only by the reboiler bypass procedure (REPORT Fig F.23)
    "V101": ("ManualValve", "ball", 1, "L4", "closed", "Steam side of H100. Closed in the stripping loop test: no steam (REPORT Fig E.1)."),
    "V102": ("ManualValve", "ball", 1, "L4", "closed", "Steam side of H100. Closed in the stripping loop test: no steam (REPORT Fig E.1)."),
    "V105": ("ManualValve", "ball", 1, "M4", "closed", "Steam side of H100. Closed in the stripping loop test: no steam (REPORT Fig E.1)."),
    "V106": ("ManualValve", "ball", 1, "M3", "closed", "Steam bypass of H100."),
    "V109": ("ManualValve", "ball", 1, None, "closed", "Steam side of H100. REPORT gives grid M5 (Fig F.23) and N7 (Fig E.1)."),
}

# ---------------------------------------------------------------------------
# Pipe segments (line numbers on the P&ID)
# ---------------------------------------------------------------------------
PIPES = {
    "Q105": "Line from FT102 to the bottom (process inlet) of H100.",
    "Q106": "Line from the top (process outlet) of H100 back to the E100 sump nozzle below the chimney tray. TT100/TI100 sit on the H100 outlet before it. There is a small inline symbol on this line still to identify.",
}

# ---------------------------------------------------------------------------
# Instruments: tag -> (class, variable, sensor type, signal, grid, floor, monitors, stage, phase)
# Sensor type, signal, grid and floor from REPORT Appendix B instrument lists.
# ---------------------------------------------------------------------------
INSTRUMENTS = {
    "FT102": ("FlowInstrument", "mass flow, density and temperature", "Coriolis mass flow meter", "Profibus-PA", "M6", 1, "H100", None, None),
    "FI102": ("FlowInstrument", "mass flow indication", None, None, "M6", 1, "H100", None, None),
    "DI100": ("FlowInstrument", "density indication (from FT102)", None, None, None, 1, "H100", None, None),
    "TT100": ("TemperatureInstrument", "temperature of MEA leaving H100", "PRT", "Profibus-PA", "L6", 1, "H100", None, None),
    "TI100": ("TemperatureInstrument", "temperature indication", None, None, "K6", 1, "H100", None, None),
    "TT103": ("TemperatureInstrument", "temperature", "PRT", "Profibus-PA", "J7", 1, "E100", 11, None),
    "PT102": ("PressureInstrument", "pressure", "gauge pressure transmitter", "Profibus-PA", "K8", 1, "E100", 12, None),
    "PSHH116": ("PressureInstrument", "pressure high-high switch", None, None, None, 1, "E100", 11, None),
    "LT101": ("LevelInstrument", "level", "differential pressure transmitter", "Profibus-PA", "K8", 1, "E100", 12, None),
    "LSHH100": ("LevelInstrument", "level high-high switch", None, None, None, 1, "E100", 12, None),
    "LSLL102": ("LevelInstrument", "level low-low switch", None, None, None, 1, "E100", 12, None),
    "TT104": ("TemperatureInstrument", "temperature", "PRT", "Profibus-PA", "M8", 1, "C100", None, None),
    "PT103": ("PressureInstrument", "pressure", "gauge pressure transmitter", "Profibus-PA", "M8", 1, "C100", None, None),
    "TE105": ("TemperatureInstrument", "temperature", "PRT", "Profibus-PA", "M9", 1, "C100", None, None),
    "TT106": ("TemperatureInstrument", "temperature", "PRT", "4-20mA", "L10", 1, "J100", None, None),
    "PT104": ("PressureInstrument", "pressure", "gauge pressure transmitter", "Profibus-PA", "L10", 1, "J100", None, None),
    "PDT105": ("DifferentialPressureInstrument", "differential pressure across Z102", "differential pressure transmitter", "Profibus-PA", "M11", 1, "Z102", None, None),
    "FT103": ("FlowInstrument", "volumetric flow", "electromagnetic volumetric flow meter", "4-20mA", "L12", 1, "J100", None, None),
    "FI103": ("FlowInstrument", "flow indication", None, None, None, 1, "J100", None, None),
    "FT104": ("FlowInstrument", "volumetric flow", "swirl volumetric flow meter", "Fieldbus", "L12", 1, "J100", None, None),
    "FI104": ("FlowInstrument", "flow indication", None, None, None, 1, "J100", None, None),
    "TT212a": ("TemperatureInstrument", "heater temperature", "K-type thermocouple", "4-20mA", "J9", 2, "H200a", None, None),
    "TSHH212a": ("TemperatureInstrument", "temperature high-high switch", None, None, None, 2, "H200a", None, None),
    "TT212b": ("TemperatureInstrument", "heater temperature", "K-type thermocouple", "4-20mA", "J10", 2, "H200b", None, None),
    "TSHH212b": ("TemperatureInstrument", "temperature high-high switch", None, None, None, 2, "H200b", None, None),
    "TT213": ("TemperatureInstrument", "temperature of MEA leaving H200a/b", "PRT", "Profibus-PA", "H13", 2, None, None, None),
    "TI213": ("TemperatureInstrument", "temperature indication", None, None, "H10", 2, None, None, None),
    "FT305": ("FlowInstrument", "mass flow (reflux from J300)", "Coriolis mass flow meter", "Profibus-PA", "F9", 3, None, None, None),
    "TT309": ("TemperatureInstrument", "temperature (reflux from J300)", "PRT", "Profibus-PA", "F9", 3, None, None, None),
    "TT401": ("TemperatureInstrument", "temperature", "PRT", "Profibus-PA", "F7", 4, "E100", 1, "vapour"),
    "TT400": ("TemperatureInstrument", "temperature", "PRT", "Profibus-PA", "F7", 4, "E100", 1, "liquid"),
    "PSHH400": ("PressureInstrument", "pressure high-high switch", None, None, None, 4, "E100", 1, "vapour"),
    "TT303": ("TemperatureInstrument", "temperature", "PRT", "Profibus-PA", "G7", 3, "E100", 3, "vapour"),
    "TT302": ("TemperatureInstrument", "temperature", "PRT", "Profibus-PA", "G7", 3, "E100", 3, "liquid"),
    "TT301": ("TemperatureInstrument", "temperature", "PRT", "4-20mA", "G7", 3, "E100", 5, "vapour"),
    "TT300": ("TemperatureInstrument", "temperature", "PRT", "4-20mA", "G7", 3, "E100", 5, "liquid"),
    "TT203": ("TemperatureInstrument", "temperature", "PRT", "4-20mA", "H7", 2, "E100", 7, "vapour"),
    "TT202": ("TemperatureInstrument", "temperature", "PRT", "4-20mA", "H7", 2, "E100", 7, "liquid"),
    "TT201": ("TemperatureInstrument", "temperature", "PRT", "Profibus-PA", "J7", 2, "E100", 9, "vapour"),
    "TT200": ("TemperatureInstrument", "temperature", "PRT", "Profibus-PA", "J7", 2, "E100", 9, "liquid"),
    # steam side and overhead (used by control loops)
    "FT100": ("FlowInstrument", "steam flow to H100", "orifice flow meter", "Profibus-PA", "L4", 1, "H100", None, None),
    "FT101": ("FlowInstrument", "steam flow to H100", "swirl volumetric flow meter", "Profibus-PA", "L5", 1, "H100", None, None),
    "PT401": ("PressureInstrument", "E100 overhead pressure", "gauge pressure transmitter", "Profibus-PA", "C8", 4, "E100", None, None),
    "PT402": ("PressureInstrument", "pressure after K401", "gauge pressure transmitter", "Fieldbus", "C16", 4, "E100", None, None),
}
STAGE_MAP_NOTE = "Stage mapping inferred: odd Aspen stages are the gaps between packed beds where the side instruments sit; floors match REPORT."

CONTROLLERS = {
    # tag -> (controls, label)
    "SIC100": ("J100", "J100 speed controller"),
    "HS100": ("J100", "J100 hand switch"),
    "FIC103": ("J100", "MEA flow controller (PV FT103)"),
    "FIC104": ("J100", "MEA flow controller (PV FT104)"),
    "TIC213a": ("H200a", "Heater outlet temperature controller, leg A"),
    "TIC213b": ("H200b", "Heater outlet temperature controller, leg B"),
    "TY213a": ("H200a", "Power converter driving H200a"),
    "TY213b": ("H200b", "Power converter driving H200b"),
    "HS200a": ("H200a", "H200a hand switch"),
    "HS200b": ("H200b", "H200b hand switch"),
    "TZAHH212a": ("H200a", "H200a high-high temperature trip"),
    "TZAHH212b": ("H200b", "H200b high-high temperature trip"),
    "TZH213": (["H200a", "H200b"], "High temperature interlock on heater outlet (acts on both heaters)"),
    "TIC100": ("FCV110", "Reboiler outlet temperature controller (cascade master)"),
    "FIC100": ("FCV110", "Steam flow controller (cascade slave)"),
    "PIC401": ("PCV119", "E100 pressure controller"),
    "PIC402": ("PCV119", "E100 pressure controller"),
}

# ---------------------------------------------------------------------------
# Nozzles on E100
# ---------------------------------------------------------------------------
NOZZLES = {
    "E100_N_drawoff": ("E100 draw-off nozzle below TT103 (chimney tray, to H100)", 11),
    "E100_N_reboiler_return": ("E100 sump return nozzle from H100 (below chimney tray)", 12),
    "E100_N_sump_outlet": ("E100 sump outlet nozzle (to V110)", 12),
    "E100_N_top_inlet": ("E100 top inlet nozzle after V402 (above top packed bed)", 1),
}

# ---------------------------------------------------------------------------
# The loop, in flow order. A list entry is one step; a tuple of entries is a
# set of parallel items sharing a step index. Types: inline / tie-in / branch.
# "branch" = a connection off the line that is closed in the stripping loop.
# ---------------------------------------------------------------------------
LOOP = [
    ("E100_N_drawoff", "inline"),
    ("FT102", "inline"), ("FI102", "tie-in"), ("DI100", "tie-in"),
    ("Q105", "inline"),
    ("H100", "inline"),
    ("TT100", "tie-in"), ("TI100", "tie-in"), ("Q106", "inline"),
    ("E100_N_reboiler_return", "inline"),
    ("E100", "inline"),                       # sump
    ("E100_N_sump_outlet", "inline"),
    ("V110", "inline"), ("V112", "inline"),
    ("TT104", "tie-in"), ("PT103", "tie-in"),
    ("C100", "inline"),
    ("TE105", "tie-in"),
    ("V113a", "inline"), ("V113b", "inline"),
    ("J100", "inline"), ("TT106", "tie-in"),
    ("B101", "tie-in"), ("PT104", "tie-in"),
    ("PCV122", "inline"),
    ("V116", "inline"),
    ("V117a", "inline"), ("Z102", "inline"), ("PDT105", "tie-in"), ("V117b", "inline"),
    ("V121", "inline"),                       # bypass rejoins upstream of V121
    ("FT103", "inline"), ("FI103", "tie-in"),
    ("FT104", "inline"), ("FI104", "tie-in"),
    ("SOV125", "inline"),
    (("H200a", "inline"), ("H200b", "inline")),
    ("TT213", "tie-in"), ("TI213", "tie-in"),
    ("V403", "inline"), ("V402", "inline"),
    ("E100_N_top_inlet", "inline"),
    ("E100", "inline"),                       # down the packing to the chimney tray
]
REBOILER_SUBLOOP = ["E100_N_drawoff", "FT102", "Q105", "H100", "Q106", "E100_N_reboiler_return"]
EXTRA_PIPING = [("V116", "V120"), ("V120", "V121"), ("J100", "RV101"), ("FT104", "SOV123"),
                ("V316", "V315")]

# ---------------------------------------------------------------------------
# Control loops (SUMMARY p.190, REPORT Appendix D) and interlocks
# ---------------------------------------------------------------------------
CONTROL_LOOPS = {
    "CL_J100_flow": dict(label="MEA flow from E100 (pump speed)", sensors=["FT103", "FT104"],
                         controllers=["FIC103", "FIC104", "SIC100"], final=["J100"],
                         cv="MEA flowrate leaving E100", mv="J100 speed (via SIC100)",
                         source="SUMMARY p.190; REPORT D.4"),
    "CL_H200a_temperature": dict(label="Temperature of MEA entering E100, heater leg A", sensors=["TT213"],
                                 controllers=["TIC213a", "TY213a"], final=["H200a"],
                                 cv="Temperature of MEA entering E100", mv="Thermal duty of H200a",
                                 source="SUMMARY p.190; REPORT D.4.4.a"),
    "CL_H200b_temperature": dict(label="Temperature of MEA entering E100, heater leg B", sensors=["TT213"],
                                 controllers=["TIC213b", "TY213b"], final=["H200b"],
                                 cv="Temperature of MEA entering E100", mv="Thermal duty of H200b",
                                 source="SUMMARY p.190; REPORT D.4.4.a"),
    "CL_H100_temperature_master": dict(label="Temperature of MEA leaving H100 (cascade master)", sensors=["TT100"],
                                       controllers=["TIC100"], final=["FCV110"],
                                       cv="Temperature of MEA leaving H100 into E100",
                                       mv="Steam flow set point for FIC100",
                                       source="SUMMARY p.190; REPORT D.4.4.c"),
    "CL_H100_steam_slave": dict(label="Steam flow to H100 (cascade slave)", sensors=["FT100", "FT101"],
                                controllers=["FIC100"], final=["FCV110"],
                                cv="Steam flowrate to H100", mv="FCV110 opening",
                                source="SUMMARY p.190; REPORT D.4.4.c"),
    "CL_E100_pressure": dict(label="E100 pressure (boundary loop on overhead)", sensors=["PT401", "PT402"],
                             controllers=["PIC401", "PIC402"], final=["PCV119"],
                             cv="Pressure in E100", mv="PCV119 opening", source="SUMMARY p.190; REPORT D.4"),
}
CASCADES = [("CL_H100_temperature_master", "CL_H100_steam_slave")]

INTERLOCKS = {
    "IL_H200a_HH": dict(label="H200a high-high temperature trip", by=["TT212a", "TSHH212a"], trips=["H200a"]),
    "IL_H200b_HH": dict(label="H200b high-high temperature trip", by=["TT212b", "TSHH212b"], trips=["H200b"]),
    "IL_heater_outlet_H": dict(label="Heater outlet high temperature (TZH213)", by=["TT213"], trips=["H200a", "H200b"]),
    "IL_E100_level_LL": dict(label="E100 low-low level shutdown (protects J100)", by=["LT101", "LSLL102"], trips=["J100"]),
    "IL_E100_level_HH": dict(label="E100 high-high level shutdown", by=["LSHH100"], trips=["J100"]),
}

# ---------------------------------------------------------------------------
# Operating limits: id -> (applies to, variable, type, low, high, unit, source, verified, note)
# ---------------------------------------------------------------------------
LIMITS = {
    "J100_power_range": ("J100", "pump power", "range", 1.0, 60.0, "%", "REPORT 2.5", True,
                         "Experimental safe range; 1 to 57 % allowing for cavitation."),
    "J100_flow_range": ("J100", "volumetric flow", "range", 10.79, 19.70, "L/min", "P&ID", True, None),
    "J100_cavitation": ("J100", "pump power", "alarm", None, 55.0, "%", "REPORT E.3.3", True,
                        "Above 55 % with audible vibration: open SOV204 to pressurise E100 with N2."),
    "RV101_set": ("RV101", "pressure", "relief", None, 10.0, "bar", "P&ID; HAZOP 7.14", True, None),
    "PCV122_set": ("PCV122", "pressure", "setpoint", None, 8.0, "bar", "P&ID", False, UNVERIFIED),
    "PDT105_range": ("PDT105", "differential pressure", "range", 0.0, 2.0, "bar", "P&ID", True, None),
    "PDT105_blocked_filter": ("Z102", "differential pressure", "alarm", None, 0.45, "bar", "REPORT E.3.6", True,
                              "At or above 0.45 bar Z102 is treated as blocked; follow the Z102 bypass procedure."),
    "TZAH106": ("J100", "temperature", "trip", None, None, "C", "HAZOP 7.1", True,
                "Pump overheat on no flow (formerly TZAH104); setpoint not stated."),
    "LT101_low_alarm": ("E100", "level", "alarm", 5.0, None, "%", "REPORT 2.2", True, "LSL: alerts control room."),
    "LZAL102": ("E100", "level", "trip", 1.0, None, "%", "REPORT 2.2; HAZOP 7.15, 11.15", True,
                "LSLL: emergency shutdown; protects J100 from starvation."),
    "LT101_operating_window": ("E100", "level", "range", 10.0, 90.0, "%", "REPORT E.3.7, E.3.8", True,
                               "Keep LT101 between 10 % and 90 % during the stripping loop test."),
    "LZAH100": ("E100", "level", "trip", None, None, "%", "HAZOP 11.12", True, "High level in sump; plant shutdown."),
    "PSHH400_set": ("E100", "pressure", "trip", None, 2.0, "barg", "P&ID", True, "Top of column, rising."),
    "PSHH116_set": ("E100", "pressure", "trip", None, 2.0, "barg", "P&ID", True, "Column base, rising."),
    "PT102_range": ("PT102", "pressure", "range", -1.0, 4.0, "barg", "P&ID", True, None),
    "H100_steam_limit": ("H100", "steam mass flow", "range", None, 140.0, "kg/h", "HAZOP 13.4", True,
                         "Limited via PCV113 output during commissioning."),
    "FT102_range": ("FT102", "mass flow", "range", 0.0, 600.0, "kg/h", "P&ID", False, UNVERIFIED),
    "FT103_range": ("FT103", "mass flow", "range", 100.0, 12000.0, "kg/h", "P&ID", False, UNVERIFIED),
    "FT104_range": ("FT104", "mass flow", "range", 100.0, 1600.0, "kg/h", "P&ID", False, UNVERIFIED),
    "FT104_min_reading": ("FT104", "mass flow", "range", 250.0, None, "kg/h", "REPORT E.2.1.12", True,
                          "FT104 does not read below about 250 kg/h (about 15 % J100 power)."),
    "TT213_setpoint_commissioning": ("TT213", "temperature", "setpoint", None, 25.0, "C", "REPORT E.2.1.9", True,
                                     "Heaters effectively off during the commissioning test."),
    "TSHH212a": ("H200a", "temperature", "trip", None, None, "C", "P&ID", True, "Setpoint not on drawing."),
    "TSHH212b": ("H200b", "temperature", "trip", None, None, "C", "P&ID", True, "Setpoint not on drawing."),
}

# ---------------------------------------------------------------------------
# Procedures (REPORT Appendix E and F)
# ---------------------------------------------------------------------------
LINEUP_OPEN = ["V110", "V112", "V113a", "V113b", "V116", "V117a", "V117b", "V121", "SOV125", "V403", "V402"]
LINEUP_CLOSED = ["V120", "SOV123", "V315", "V316", "FCV110", "V101", "V102", "V105", "V106"]
PROCEDURES = {
    "PROC_stripping_loop_lineup": dict(
        label="Stripping loop line-up (commissioning test start-up)",
        source="REPORT E.2.1 and Fig E.1/E.2",
        trigger="Before starting J100 for the stripping loop test",
        steps=[("Check J100 and J300 are off", "J100", None)]
              + [(f"Set {v} closed", v, "closed") for v in LINEUP_CLOSED]
              + [(f"Set {v} open", v, "open") for v in LINEUP_OPEN]
              + [("Check FT100 and FT101 read zero, so no steam reaches H100", "FT100", None),
                 ("Set heater outlet temperature set point to 25 C (read on TT213)", "TT213", None),
                 ("Start J100 at 15 % power", "J100", None)]),
    "PROC_Z102_bypass": dict(
        label="Z102 filter bypass",
        source="REPORT E.3.6 and Fig F.21",
        trigger="PDT105 at or above 0.45 bar (Z102 blocked)",
        steps=[("Reduce J100 power by 20 % per minute until it reaches 15 %", "J100", None),
               ("Manually open V120", "V120", "open"),
               ("Manually close V117a", "V117a", "closed"),
               ("Manually close V117b", "V117b", "closed"),
               ("Return J100 to the previous steady-state power", "J100", None),
               ("Replace or clean Z102", "Z102", None)]),
    "PROC_H100_steam_bypass": dict(
        label="H100 steam-side bypass",
        source="REPORT F.8.3.3 and Fig F.23",
        trigger="Large rise in temperature and pressure around H100 suggesting a blockage",
        steps=[("Open V106", "V106", "open"), ("Close V101", "V101", "closed"),
               ("Close V109", "V109", "closed"), ("Close V105", "V105", "closed"),
               ("Close V102", "V102", "closed"), ("Close FCV110", "FCV110", "closed")]),
}

BYPASS = dict(label="Z102 bypass route via V120", from_item="V116", via=["V120"], to_item="V121",
              bypasses=["V117a", "Z102", "V117b"], state="closed", procedure="PROC_Z102_bypass")

# ---------------------------------------------------------------------------
# P&ID discrepancies relevant to the loop
# ---------------------------------------------------------------------------
DISCREPANCIES = [
    ("B101_PT104_order", ["B101", "PT104"], "M10", "PT104 tie-in before B101", "Stream passes B101 first, then PT104"),
    ("V402_V403_floor", ["V402", "V403"], "F8", "Valves on floor 4", "Valves on floor 3"),
    ("K403_missing", ["RV401"], "E7", "No knockout drum on relief line",
     "RV401 (E100) and RV400 (E101) relieve to knockout drum K403"),
    ("FCV110_name", ["FCV110"], "L5", "Labelled FCV110", "Labelled ZS110 on site"),
]

# HAZOP element coverage (what each 2010 study node includes)
HAZOP_COVERAGE = {
    "7": ["V110", "V112", "C100", "V113a", "V113b", "J100", "B101", "PCV122", "V116", "V117a", "Z102",
          "V117b", "V120", "V121", "RV101", "SOV123"],
    "8": ["C100", "V403", "V402"],
    "11": ["E100", "H100", "RV401"],
    "13": ["H100", "FCV110", "V101", "V102", "V105", "V106", "V109"],
}
HAZOP_ALARM_HOST = {"TZAH106": "J100", "LZAL102": "E100", "LZAH100": "E100", "PDAH105": "Z102"}
HAZOP_RENAMES = {"TZAH104": "TZAH106", "PDAH 105": "PDAH105"}

# ---------------------------------------------------------------------------
# Column stages (Aspen numbering, 1 = top)
# ---------------------------------------------------------------------------
STAGES = {
    1: ("GapStage", 813.0, "Pall ring", 75.0, "plastic", "equilibrium (C-1)", 4),
    2: ("PackedBedStage", 1144.0, "IMTP", 25.0, "metal", "kinetic (STP-RXN)", None),
    3: ("GapStage", 677.0, "Pall ring", 75.0, "plastic", "equilibrium (C-1)", 3),
    4: ("PackedBedStage", 1144.0, "IMTP", 25.0, "metal", "kinetic (STP-RXN)", None),
    5: ("GapStage", 677.0, "Pall ring", 75.0, "plastic", "equilibrium (C-1)", 3),
    6: ("PackedBedStage", 1144.0, "IMTP", 25.0, "metal", "kinetic (STP-RXN)", None),
    7: ("GapStage", 677.0, "Pall ring", 75.0, "plastic", "equilibrium (C-1)", 2),
    8: ("PackedBedStage", 1144.0, "IMTP", 25.0, "metal", "kinetic (STP-RXN)", None),
    9: ("GapStage", 677.0, "Pall ring", 75.0, "plastic", "equilibrium (C-1)", 2),
    10: ("PackedBedStage", 1144.0, "IMTP", 25.0, "metal", "kinetic (STP-RXN)", None),
    11: ("GapStage", 495.0, "Pall ring", 75.0, "plastic", "none", 1),
    12: ("SumpStage", 1240.0, "Pall ring", 75.0, "plastic", "none", 1),
}
