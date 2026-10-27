"""
Plant data for the absorption loop KG (Pilot Plant 2514), with the citation
for every fact kept next to the fact.

Flow direction (from the documents, not the drawing alone):
  E101 sump > J101a or J101b (one runs at a time) > FT108 > FT109 > V124
  > V119b > V119a > V211 > N200 > V213 > C200 > NRV400 > E101 top
  REPORT: TT209 = "lean MEA ... entering C200"; TT210 = "lean MEA leaving C200";
  SUMMARY p.190: TT210 = "temperature of MEA entering the absorber E101";
  REPORT D.4: "Pumps J101a and J101b both work to pump fluid out of the bottom of the absorber".

Citation keys are the same as stripping_loop/sources.py (PID, DIFF, REPORT, SUMMARY, HAZOP, ASPEN_V3, ...).
"""

FIG8 = "start-up tables Fig F.8 (J101a) / Fig F.9 (J101b)"
LEAN_TABLE = "lean MEA valve list (Appendix B)"
INSTR = "Appendix B instrument list"

# ---------------------------------------------------------------------------
# Equipment and valves: tag -> dict(cls, label, floor, grid, valve, pos, note, cite)
# ---------------------------------------------------------------------------
ITEMS = {
    "E101": dict(cls="AbsorptionColumn", label="E101 absorber", floor=1,
                 note="Lean MEA enters at the top through NRV400; rich MEA leaves from the sump to J101a/b. The air admittance valve shown on the P&ID has been removed from the plant (DIFF, E14/15).",
                 props={"diameter_mm": 230.0,
                        "designBasis": "Packing and column designed for 2.3-2.5 bar operation on MEA and 50 kg/h CO2 (HAZOP 10.4)"},
                 cite=[("PID", "column E101, grids F15 to K16"), ("REPORT", "section D.4 (absorber level control)"),
                       ("ASPEN_V3", "block E101")]),
    "J101a": dict(cls="Pump", label="J101a rich MEA pump (duty or standby)", floor=1, grid="N15",
                  note="J101a and J101b are in parallel; only one runs at a time (SIC101a or SIC101b).",
                  cite=[("PID", "grid N15"), ("REPORT", "section D.4 and " + FIG8)]),
    "J101b": dict(cls="Pump", label="J101b rich MEA pump (duty or standby)", floor=1, grid="N16",
                  note="Parallel to J101a; only one runs at a time.",
                  cite=[("PID", "J101b, grid N16"), ("REPORT", "section D.4, " + FIG8 + " and pump list (N16, floor 1)")]),
    "B103a": dict(cls="PulsationDampener", label="B103a pulsation dampener on the J101a discharge", floor=1,
                  note="Function inferred from the P&ID symbol (same as B101 on J100): smooths pressure pulses from the pump. Not described in the documents (AOI03).",
                  cite=[("PID", "next to J101a")]),
    "B103b": dict(cls="PulsationDampener", label="B103b pulsation dampener on the J101b discharge", floor=1,
                  note="Function inferred from the P&ID symbol (same as B101 on J100). DIFF: PCV120b sits between J101b and B103b but is not drawn.",
                  cite=[("PID", "next to J101b"), ("DIFF", "row PCV120b (N17)")]),
    "N200": dict(cls="Filter", label="N200 lean MEA filter", floor=2,
                 note="Bypass V212 (REPORT F.8.3.2, Fig F.22). How a blockage is detected is not documented (AOI06).",
                 cite=[("PID", "grid J12 to K13"), ("REPORT", "section F.8.3.2 and Fig F.22")]),
    "C200": dict(cls="TrimCooler", label="C200 lean MEA trim cooler (water cooled)", floor=2,
                 note="Cools lean MEA before the absorber; cooling water flow set by FIC201 (cascade from TIC210).",
                 cite=[("PID", "grid J13"), ("REPORT", "section 3 (C200 is a trim cooler, second floor)"), ("ASPEN_V3", "block C200")]),
    "FM_TEST_SPOOL": dict(cls="FlowMeterTestSpool", label="Flow meter test spool (between V198a and V198b)", floor=2,
                          note="Untagged on the P&ID (labelled 'Flow Meter Test Spool'). Used to insert a test flow meter; normally isolated.",
                          cite=[("PID", "grid L12 to L13, 'Flow Meter Test Spool'")]),
    "V134a": dict(cls="ManualValve", valve="ball", floor=1, grid="M15", pos="open", cite=[("PID", "grid M15"), ("REPORT", FIG8)]),
    "V135a": dict(cls="ManualValve", valve="ball", floor=1, grid="N15", pos="open", cite=[("PID", "grid N15"), ("REPORT", FIG8)]),
    "V143a": dict(cls="ManualValve", valve="ball", floor=1, grid="N14", pos="open", cite=[("PID", "grid N14"), ("REPORT", FIG8)]),
    "V144a": dict(cls="ManualValve", valve="ball", floor=1, grid="N14", pos="open", cite=[("PID", "grid N14"), ("REPORT", FIG8)]),
    "V134b": dict(cls="ManualValve", valve="ball", floor=1, grid="M15", pos="closed", cite=[("PID", "grid M15"), ("REPORT", FIG8)]),
    "V135b": dict(cls="ManualValve", valve="ball", floor=1, grid="N15", pos="closed", cite=[("PID", "grid N15"), ("REPORT", FIG8)]),
    "V143b": dict(cls="ManualValve", valve="ball", floor=1, grid="L14", pos="closed", cite=[("PID", "grid L14"), ("REPORT", FIG8)]),
    "V144b": dict(cls="ManualValve", valve="ball", floor=1, grid="L14", pos="closed", cite=[("PID", "grid L14"), ("REPORT", FIG8)]),
    "PCV120a": dict(cls="PressureControlValve", valve="pressure control", floor=1, grid="N14", pos="open",
                    cite=[("PID", "after J101a, 'SET TO 8 bar'"), ("REPORT", "valve list (N14, floor 1)")]),
    "PCV120b": dict(cls="PressureControlValve", valve="pressure control", floor=1, grid="L14", pos="open",
                    note="Not drawn on the P&ID; as-built it sits between J101b and B103b (DIFF).",
                    cite=[("DIFF", "row PCV120b (N17)"), ("REPORT", "valve list (L14, floor 1)")]),
    "V124": dict(cls="ManualValve", valve="ball", floor=1, grid="N12", pos="closed", props={"hasLockingHandle": True},
                 note="Links the J101 discharge to the lean line to C200 (absorber recirculation). Closed in normal and commissioning line-ups (REPORT Fig E.1, start-up tables); opened for the absorber recirculation route (AOI07).",
                 cite=[("PID", "grid N12"), ("REPORT", "Fig E.1 and start-up tables (ball, closed)"),
                       ("HAZOP", "element 8, item 3 (bypass left open; locking handles added)")]),
    "V119b": dict(cls="ManualValve", valve="3-way ball", floor=2, grid="L13", pos="open",
                  note="3-way ball valve: sends flow either along the main line or into the flow meter test spool.",
                  cite=[("PID", "grid L13"), ("REPORT", LEAN_TABLE + " (open in operation) and start-up tables (3-way ball)"), ("DIFF", "row V119a, V119b, V198a, V198b (floor 2)")]),
    "V119a": dict(cls="ManualValve", valve="3-way ball", floor=2, grid="L13", pos="open",
                  note="3-way ball valve: returns flow from the main line or from the flow meter test spool.",
                  cite=[("PID", "grid L13"), ("REPORT", LEAN_TABLE + " (open in operation) and start-up tables (3-way ball)"), ("DIFF", "row V119a, V119b, V198a, V198b (floor 2)")]),
    "V198b": dict(cls="ManualValve", valve="ball", floor=2, grid="L12", pos="closed", note="Isolates the flow meter test spool (normally closed).",
                  cite=[("PID", "grid L12"), ("REPORT", LEAN_TABLE + " (closed)"), ("DIFF", "row V119a, V119b, V198a, V198b (floor 2)")]),
    "V198a": dict(cls="ManualValve", valve="ball", floor=2, grid="K12", pos="closed", note="Isolates the flow meter test spool (normally closed).",
                  cite=[("PID", "grid K12"), ("REPORT", LEAN_TABLE + " (closed)"), ("DIFF", "row V119a, V119b, V198a, V198b (floor 2)")]),
    "V211": dict(cls="ManualValve", valve="ball", floor=2, grid="K13", pos="open", note="N200 inlet isolation.",
                 cite=[("PID", "grid K13"), ("REPORT", LEAN_TABLE + " and Fig F.22")]),
    "V213": dict(cls="ManualValve", valve="ball", floor=2, grid="J12", pos="open", note="N200 outlet isolation.",
                 cite=[("PID", "grid J12"), ("REPORT", LEAN_TABLE + " and Fig F.22")]),
    "V212": dict(cls="ManualValve", valve="ball", floor=2, grid="K13", pos="closed",
                 note="N200 bypass. REPORT Fig F.22 lists it on floor 1; the other tables give floor 2.",
                 cite=[("PID", "grid K13"), ("REPORT", "Fig F.22 (N200 bypass) and " + LEAN_TABLE)]),
    "V210": dict(cls="ManualValve", valve="ball", floor=2, pos="closed", note="N200 drain (from the P&ID).", cite=[("PID", "below N200")]),
    "NRV400": dict(cls="CheckValve", valve="check", floor=4, grid="F15", pos="open", note="Non-return valve on the lean MEA inlet to the top of E101.",
                   cite=[("PID", "grid F15, top of E101"), ("REPORT", "valve list (F15, floor 4)")]),
    "V217": dict(cls="ManualValve", valve="ball", floor=3, grid="G14", pos="closed",
                 note="Branch off the absorber feed line next to AT300 (L marking on the P&ID). Normally closed (REPORT lean MEA list); opened in the stripping loop commissioning test (Fig E.2).",
                 cite=[("PID", "grid G14, branch next to AT300"), ("REPORT", "lean MEA valve list (closed) and Fig E.2 (open for commissioning)")]),
    "SDV123": dict(cls="ShutdownValve", valve="shutdown (solenoid-operated)", floor=1, grid="L9", pos="closed",
                   note="Join point with the stripping loop: lean MEA from J100 enters the absorber feed line here (figure-of-eight). Closed in both loop tests.",
                   cite=[("PID", "grid L9, tagged SDV123"), ("REPORT", "Fig E.1/E.2 (stripping loop commissioning line-up) (listed as SOV123)")]),
    "FCV200": dict(cls="FlowControlValve", valve="flow control", floor=2, grid="H12", pos="open",
                   note="Cooling water valve for C200 driven by FIC201 (REPORT D.4.4.b, SUMMARY p.190). FCV201 is also on the cooling water line; its role is open item AOI08.",
                   cite=[("PID", "cooling water line to C200"), ("SUMMARY", "p.190 (control-loop table)"),
                         ("REPORT", "section D.4.4.b and start-up tables (FCV200, control, H12, floor 2)")]),
    "FCV201": dict(cls="FlowControlValve", valve="flow control", floor=2, grid="H11", pos="open",
                   note="On the C200 cooling water line; listed in the REPORT valve tables (H11). Role relative to FCV200 unclear (AOI08).",
                   cite=[("PID", "grid H11"), ("REPORT", "start-up tables (FCV201, control, open)")]),
    "RV106a": dict(cls="ReliefValve", valve="relief", floor=1, grid="M14", pos="closed", present=False,
                   note="Drawn on the P&ID (set to 10 bar) but not present on the plant (DIFF).",
                   cite=[("PID", "next to B103a, 'SET TO 10 bar'"), ("DIFF", "row RV106b & RV106a (M17 and M15)")]),
    "RV106b": dict(cls="ReliefValve", valve="relief", floor=1, grid="M16", pos="closed", present=False,
                   note="Drawn on the P&ID (set to 10 bar) but not present on the plant (DIFF).",
                   cite=[("PID", "next to B103b, 'SET TO 10 bar'"), ("DIFF", "row RV106b & RV106a (M17 and M15)")]),
}

# Instruments: tag -> (class, variable, sensor type, signal, grid, floor, monitors, citations)
INSTRUMENTS = {
    "LT108": ("LevelInstrument", "E101 sump level", "differential pressure transmitter", "Fieldbus", "K15", 1, "E101",
              [("PID", "grid K15"), ("REPORT", INSTR)]),
    "LSHH107": ("LevelInstrument", "level high-high switch", None, None, None, 1, "E101", [("PID", "E101 sump")]),
    "LSLL109": ("LevelInstrument", "level low-low switch", None, None, None, 1, "E101", [("PID", "E101 sump")]),
    "PT111": ("PressureInstrument", "E101 base pressure", "gauge pressure transmitter", "Fieldbus", "K16", 1, "E101",
              [("PID", "E101 base, '-1 to 4 barG'"), ("REPORT", INSTR + " (K16, floor 1)")]),
    "PSHH117": ("PressureInstrument", "pressure high-high switch", None, None, None, 1, "E101", [("PID", "E101 base, 'SET TO 3.5 barg RISING'")]),
    "TT111a": ("TemperatureInstrument", "J101a temperature", "K-type thermocouple", "4-20mA", "N15", 1, "J101a",
               [("PID", "on J101a"), ("REPORT", INSTR + " (N15, floor 1)")]),
    "TT111b": ("TemperatureInstrument", "J101b temperature", "K-type thermocouple", "4-20mA", "N16", 1, "J101b",
               [("PID", "on J101b"), ("REPORT", INSTR + " (N16, floor 1)")]),
    "PT115b": ("PressureInstrument", "J101b discharge pressure", "gauge pressure transmitter", "Fieldbus", "L14", 1, "J101b",
               [("PID", "J101b discharge, '-1 to 9 barg'"), ("REPORT", INSTR + " (L14, floor 1)")]),
    "FT108": ("FlowInstrument", "mass flow and density of rich MEA", "Coriolis mass flow meter", "4-20mA", "N13", 1, "E101",
              [("PID", "grid N13"), ("REPORT", INSTR + "; Appendix D: 'rich MEA leaving the absorber (E101) and entering C100'")]),
    "FI108": ("FlowInstrument", "flow indication", None, None, None, 1, "E101", [("PID", "on FT108")]),
    "DI108": ("FlowInstrument", "density indication (from FT108)", None, None, None, 1, "E101",
              [("PID", "on FT108"), ("SUMMARY", "p.190 note: FT108 also gives fluid density")]),
    "FT109": ("FlowInstrument", "volumetric flow (absorber recirculation line)", "variable area volumetric flow meter", "4-20mA", "N13", 1, "E101",
              [("PID", "grid N13, 'METAL VA METER 100-1250 kg/hr'"), ("REPORT", INSTR)]),
    "FI109": ("FlowInstrument", "flow indication", None, None, None, 1, "E101", [("PID", "on FT109")]),
    "TT209": ("TemperatureInstrument", "lean MEA entering C200", "PRT", "Fieldbus", "J12", 2, "C200",
              [("PID", "grid J12"), ("REPORT", INSTR + "; Appendix D: 'lean MEA leaving C100 and entering C200'"), ("DIFF", "row TT208 & TT209 (swapped on diagram, J12)")]),
    "TT208": ("TemperatureInstrument", "lean MEA before C200", "PRT", "Fieldbus", "J12", 2, "C200",
              [("PID", "grid J12"), ("REPORT", INSTR), ("DIFF", "row TT208 & TT209 (swapped on diagram, J12)")]),
    "TT210": ("TemperatureInstrument", "lean MEA leaving C200 (entering E101)", "PRT", "Fieldbus", "J14", 2, "C200",
              [("PID", "grid J14"), ("REPORT", INSTR + "; Appendix D: 'lean MEA leaving C200'"), ("SUMMARY", "p.190: temperature of MEA entering the absorber E101")]),
    "TI210": ("TemperatureInstrument", "temperature indication", None, None, None, 2, "C200", [("PID", "on TT210")]),
    "AT300": ("Instrument", "pH of lean MEA", "inline pH transmitter", "Profibus-DP", "G14", 3, "E101",
              [("PID", "grid G14, 'AT 300 pH 0-14'"), ("REPORT", INSTR), ("DIFF", "row AT 300 (next to the stripper, G13)")]),
    "AI300": ("Instrument", "pH indication", None, None, None, 3, "E101", [("PID", "on AT300")]),
    "FT201": ("FlowInstrument", "cooling water flow to C200", "electromagnetic volumetric flow meter", "4-20mA", "H12", 2, "C200",
              [("PID", "cooling water line to C200"), ("SUMMARY", "p.190 (control-loop table)"), ("REPORT", INSTR + " (H12, floor 2)")]),
}

CONTROLLERS = {
    "LIC108": (["J101a", "J101b"], "E101 level controller (PV LT108)", [("SUMMARY", "p.190"), ("REPORT", "section D.4")]),
    "SIC101a": (["J101a"], "J101a speed controller", [("SUMMARY", "p.190"), ("REPORT", "section D.4")]),
    "SIC101b": (["J101b"], "J101b speed controller", [("SUMMARY", "p.190"), ("REPORT", "section D.4")]),
    "TIC210": (["FCV200"], "C200 outlet temperature controller (cascade master)", [("PID", "grid J14"), ("SUMMARY", "p.190"), ("REPORT", "section D.4.4.b")]),
    "FIC201": (["FCV200"], "C200 cooling water flow controller (cascade slave)", [("PID", "cooling water line"), ("SUMMARY", "p.190"), ("REPORT", "section D.4.4.b")]),
}

NOZZLES = {
    "E101_N_sump_outlet": ("E101 sump outlet to J101a/b", [("PID", "E101 base")]),
    "E101_N_top_inlet": ("E101 top inlet after NRV400", [("PID", "top of E101, grid F15")]),
}

# ---------------------------------------------------------------------------
# The loop in flow order. A tuple of entries = parallel items (the two pump trains).
# ---------------------------------------------------------------------------
LOOP = [
    ("E101_N_sump_outlet", "inline"),
    (("V134a", "inline"), ("V134b", "inline")),
    (("V135a", "inline"), ("V135b", "inline")),
    (("J101a", "inline"), ("J101b", "inline")),
    (("TT111a", "tie-in"), ("TT111b", "tie-in")),
    (("PCV120a", "inline"), ("PCV120b", "inline")),
    (("B103a", "tie-in"), ("B103b", "tie-in")),
    ("PT115b", "tie-in"),
    (("V143a", "inline"), ("V143b", "inline")),
    (("V144a", "inline"), ("V144b", "inline")),
    ("FT108", "inline"), ("FI108", "tie-in"), ("DI108", "tie-in"),
    ("FT109", "inline"), ("FI109", "tie-in"),
    ("V124", "inline"),
    ("SDV123", "branch"),                 # lean feed from the stripping loop joins here (figure-of-eight)
    ("V119b", "inline"), ("V119a", "inline"),
    ("V211", "inline"), ("N200", "inline"), ("V213", "inline"),
    ("TT209", "tie-in"), ("TT208", "tie-in"),
    ("C200", "inline"),
    ("TT210", "tie-in"), ("TI210", "tie-in"),
    ("AT300", "tie-in"), ("AI300", "tie-in"),
    ("V217", "branch"),
    ("NRV400", "inline"),
    ("E101_N_top_inlet", "inline"),
    ("E101", "inline"),
]
TRAIN_A = ["V134a", "V135a", "J101a", "TT111a", "PCV120a", "B103a", "V143a", "V144a"]
TRAIN_B = ["V134b", "V135b", "J101b", "TT111b", "PCV120b", "B103b", "PT115b", "V143b", "V144b"]
EXTRA_PIPING = [("V124", "V198b"), ("V198b", "FM_TEST_SPOOL"), ("FM_TEST_SPOOL", "V198a"), ("V198a", "V211"),
                ("V119a", "V212"), ("V212", "C200"), ("V210", "N200"), ("SDV123", "V119b")]

BYPASSES = {
    "N200_bypass": dict(label="N200 bypass route via V212", from_item="V119a", via=["V212"], to_item="C200",
                        bypasses=["V211", "N200", "V213"], state="closed", procedure="PROC_N200_bypass",
                        cite=[("PID", "grids J12 to K13"), ("REPORT", "section F.8.3.2 and Fig F.22")]),
    "FM_spool_route": dict(label="Flow meter test spool route via V198b and V198a", from_item="V124",
                           via=["V198b", "FM_TEST_SPOOL", "V198a"], to_item="V211", bypasses=["V119b", "V119a"],
                           state="closed", procedure=None,
                           cite=[("PID", "grids K12 to L13, 'Flow Meter Test Spool'"), ("REPORT", LEAN_TABLE + " (V198a/b closed, V119a/b open)")]),
}

# Route scenarios: which pump train runs
ROUTES = {
    "AbsRoute_J101a": dict(label="Absorber recirculation on J101a", train="a",
                           settings={"V134a": "open", "V135a": "open", "V143a": "open", "V144a": "open",
                                     "V134b": "closed", "V135b": "closed", "V143b": "closed", "V144b": "closed",
                                     "V124": "open", "SDV123": "closed", "V212": "closed", "V198a": "closed", "V198b": "closed"},
                           cite=[("REPORT", "Fig F.8 (J101a start-up valves)"), ("DERIVED", "V124 open for recirculation (not documented, AOI07)")]),
    "AbsRoute_J101b": dict(label="Absorber recirculation on J101b", train="b",
                           settings={"V134b": "open", "V135b": "open", "V143b": "open", "V144b": "open",
                                     "V134a": "closed", "V135a": "closed", "V143a": "closed", "V144a": "closed",
                                     "V124": "open", "SDV123": "closed", "V212": "closed", "V198a": "closed", "V198b": "closed"},
                           cite=[("REPORT", "Fig F.9 (J101b start-up valves)"), ("DERIVED", "V124 open for recirculation (not documented, AOI07)")]),
}

CONTROL_LOOPS = {
    "CL_E101_level": dict(label="E101 sump level (pump speed)", sensors=["LT108"], controllers=["LIC108", "SIC101a", "SIC101b"],
                          final=["J101a", "J101b"], cv="Level in the bottom of E101", mv="Speed of J101a/b",
                          cite=[("SUMMARY", "p.190"), ("REPORT", "section D.4")]),
    "CL_C200_temperature": dict(label="Temperature of MEA entering E101 (cascade master)", sensors=["TT210"], controllers=["TIC210"],
                                final=["FCV200"], cv="Temperature of lean MEA entering E101", mv="Cooling water flow set point for FIC201",
                                cite=[("SUMMARY", "p.190"), ("REPORT", "section D.4.4.b")]),
    "CL_C200_cooling_water": dict(label="Cooling water flow to C200 (cascade slave)", sensors=["FT201"], controllers=["FIC201"],
                                  final=["FCV200"], cv="Cooling water flowrate to C200", mv="FCV200 opening",
                                  cite=[("SUMMARY", "p.190"), ("REPORT", "section D.4.4.b")]),
}
CASCADES = [("CL_C200_temperature", "CL_C200_cooling_water")]

# Limits: id -> (applies to, variable, type, low, high, unit, citations). All read from the P&ID image, so unverified.
LIMITS = {
    "PSHH117_set": ("E101", "pressure", "trip", None, 3.5, "barg", [("PID", "E101 base, 'SET TO 3.5 barg RISING'")]),
    "PT111_range": ("PT111", "pressure", "range", -1.0, 4.0, "barg", [("PID", "E101 base, '-1 to 4 barG'")]),
    "PT115b_range": ("PT115b", "pressure", "range", -1.0, 9.0, "barg", [("PID", "J101b discharge, '-1 to 9 barg'")]),
    "FT109_range": ("FT109", "mass flow", "range", 100.0, 1250.0, "kg/h", [("PID", "grid N13, 'METAL VA METER 100-1250 kg/hr'")]),
    "AT300_range": ("AT300", "pH", "range", 0.0, 14.0, "pH", [("PID", "grid G14, 'pH 0-14'")]),
    "PCV120a_set": ("PCV120a", "pressure", "setpoint", None, 8.0, "bar", [("PID", "after J101a, 'SET TO 8 bar'")]),
    "PCV120b_set": ("PCV120b", "pressure", "setpoint", None, 8.0, "bar", [("PID", "'PCV SET TO 120b 8 bar'")]),
    "J101_start_power": ("J101a", "pump power", "setpoint", None, 10.0, "%", [("REPORT", "section F.5.4.6 (start at 10 %, then +10 % steps)")]),
}

PROCEDURES = {
    "PROC_J101a_startup": dict(label="J101a start-up valve line-up", trigger="J101a selected as the running pump",
                               cite=[("REPORT", "section F.5.4.6 and Fig F.8")],
                               steps=[("Close V134b, V135b, V143b and V144b (J101b train)", "J101b", None),
                                      ("Close V133, V139a/b, V141a/b and V142a/b (other J101 lines, Fig F.8)", "J101a", None),
                                      ("Open V134a", "V134a", "open"), ("Open V135a", "V135a", "open"),
                                      ("Open V143a", "V143a", "open"), ("Open V144a", "V144a", "open"),
                                      ("Start J101a from the control room at 10 % power, increasing in 10 % steps", "J101a", None)]),
    "PROC_J101b_startup": dict(label="J101b start-up valve line-up", trigger="J101b selected as the running pump",
                               cite=[("REPORT", "section F.5.4.8 and Fig F.9")],
                               steps=[("Close V134a, V135a, V143a and V144a (J101a train)", "J101a", None),
                                      ("Close V133, V139a/b, V141a/b and V142a/b (other J101 lines, Fig F.9)", "J101b", None),
                                      ("Open V134b", "V134b", "open"), ("Open V135b", "V135b", "open"),
                                      ("Open V143b", "V143b", "open"), ("Open V144b", "V144b", "open"),
                                      ("Start J101b from the control room at 10 % power, increasing in 10 % steps", "J101b", None)]),
    "PROC_pump_start_order": dict(label="Order of starting J100 and J101a/b", trigger="Starting the figure-of-eight circulation",
                                  cite=[("REPORT", "section F.5.4.5 and F.5.4.7")],
                                  steps=[("Compare LT101 (E100) and LT108 (E101)", "LT108", None),
                                         ("If LT101 < LT108, start J100 before J101a/b to avoid overfilling", "J101a", None),
                                         ("If LT101 >= LT108, start J101a/b before J100", "J101a", None),
                                         ("Leave a 1-minute gap before starting the second pump", "J101a", None)]),
    "PROC_N200_bypass": dict(label="N200 filter bypass", trigger="Blockage in N200",
                             cite=[("REPORT", "section F.8.3.2 and Fig F.22")],
                             steps=[("Open V212", "V212", "open"), ("Close V211", "V211", "closed"), ("Close V213", "V213", "closed"),
                                    ("Replace or fix N200", "N200", None)]),
}

DISCREPANCIES = [
    ("TT208_TT209_swap", ["TT208", "TT209"], "J12", "TT208 and TT209 in one order", "TT208 and TT209 swapped on the diagram"),
    ("PCV120b_missing", ["PCV120b"], "N17", "PCV120b not shown", "PCV120b between J101b and B103b"),
    ("RV106_absent", ["RV106a", "RV106b"], "M15/M17", "RV106a and RV106b drawn (set to 10 bar)", "RV106a and RV106b not in the practical plant"),
    ("AT300_location", ["AT300"], "G13", "AT300 on the absorber feed line", "AT300 next to the stripper"),
    ("V119_V198_floor", ["V119a", "V119b", "V198a", "V198b"], "L13", "Would be assumed on floor 1", "On floor 2"),
]

HAZOP_COVERAGE = {"7": ["V119a", "V119b", "V211", "N200", "V213", "V212", "C200", "NRV400", "V124"],
                  "8": ["J101a", "J101b", "V134a", "V135a", "V143a", "V144a", "V134b", "V135b", "V143b", "V144b",
                        "PCV120a", "PCV120b", "FT108"]}

OPEN_ITEMS = {
    "AOI01": ("Flow direction deduced from the documents (TT209/TT210 descriptions, J101 duty); the arrangement of FT108, FT109 and V124 is inferred from the P&ID",
              ["FT108", "FT109", "V124"], "Team check on the full-size P&ID"),
    "AOI02": ("Which of J101a and J101b is the normal duty pump", ["J101a", "J101b"], "Plant supervisor or handover document (REPORT F.5.4.5)"),
    "AOI03": ("B103a and B103b are taken to be pulsation dampeners from their P&ID symbol; not described in the documents", ["B103a", "B103b"], "Equipment list or site check"),
    "AOI04": ("RV106a and RV106b are drawn but not on the plant, so J101a/b discharge relief protection is unclear", ["J101a", "J101b"], "Safety review or HAZOP of the J101 discharge"),
    "AOI05": ("AT300 location: drawn on the absorber feed line, but DIFF says it is next to the stripper", ["AT300"], "Site check"),
    "AOI06": ("No instrument shown to detect an N200 blockage", ["N200"], "Full-size P&ID or site check"),
    "AOI07": ("The absorber recirculation line-up (V124 open, rich route to C100 closed) is not documented", ["V124"], "Supervisor confirmation of the line-up"),
    "AOI08": ("FCV200 and FCV201 are both on the C200 cooling water line; FIC201 drives FCV200, but the role of FCV201 is not documented", ["FCV200", "FCV201"], "Site check"),
    "AOI09": ("Order of V134/V135 and V143/V144 in each pump train, and where PCV120a sits", ["J101a", "J101b"], "Full-size P&ID"),
    "AOI10": ("E101 stage profile and packing not yet extracted from Aspen", ["E101"], "Run tools/extract_aspen.py for block E101"),
    "AOI12": ("Procedure for using the flow meter test spool", ["FM_TEST_SPOOL"], "Operating procedures"),
}


# ---------------------------------------------------------------------------
# Additions from the 100-question review (Oct 2026)
# ---------------------------------------------------------------------------
COLUMN_TEMPS = "REPORT Appendix B instrument list"
ITEMS.update({
    "V205": dict(cls="ManualValve", valve="needle", floor=2, grid="J16", pos="closed", note="E101 gas sample valve (sample 5).",
                 cite=[("PID", "E101, 'SAMPLE 5 TO ABB GAS ANALYSER'"), ("REPORT", "valve tables (needle, J16, floor 2)")]),
    "V207": dict(cls="ManualValve", valve="needle", floor=2, grid="H16", pos="closed", note="E101 gas sample valve (sample 4).",
                 cite=[("PID", "E101, 'SAMPLE 4 TO ABB GAS ANALYSER'"), ("REPORT", "valve tables (needle, H16, floor 2)")]),
    "V306": dict(cls="ManualValve", valve="needle", floor=3, grid="H16", pos="closed", note="E101 gas sample valve (sample 3).",
                 cite=[("PID", "E101, 'SAMPLE 3 TO ABB GAS ANALYSER'"), ("REPORT", "valve tables (needle, H16, floor 3)")]),
    "V308": dict(cls="ManualValve", valve="needle", floor=3, grid="G16", pos="closed", note="E101 gas sample valve (sample 2).",
                 cite=[("PID", "E101, 'SAMPLE 2 TO ABB GAS ANALYSER'"), ("REPORT", "valve tables (needle, G16, floor 3)")]),
    "RV400": dict(cls="ReliefValve", valve="relief", grid="E15", pos="closed",
                  note="E101 relief valve, sized for maximum filling gas rate (HAZOP 10.8); discharges to knockout drum K403 (DIFF).",
                  cite=[("HAZOP", "element 10, item 8"), ("DIFF", "row K403 (RV400 at E15/16)")]),
})
INSTRUMENTS.update({
    "TT411": ("TemperatureInstrument", "E101 temperature", "PRT", "Fieldbus", "F15", 4, "E101", [("PID", "E101 top, 'LIQUID'"), ("REPORT", COLUMN_TEMPS)]),
    "TT308": ("TemperatureInstrument", "E101 temperature", "PRT", "Fieldbus", "G15", 3, "E101", [("PID", "E101, 'VAPOUR'"), ("REPORT", COLUMN_TEMPS)]),
    "TT307": ("TemperatureInstrument", "E101 temperature", "PRT", "Fieldbus", "G15", 3, "E101", [("PID", "E101, 'LIQUID'"), ("REPORT", COLUMN_TEMPS + " and Fig 4.1")]),
    "TT306": ("TemperatureInstrument", "E101 temperature", "PRT", "Fieldbus", "G15", 3, "E101", [("PID", "E101, 'VAPOUR'"), ("REPORT", COLUMN_TEMPS)]),
    "TT305": ("TemperatureInstrument", "E101 temperature", "PRT", "Fieldbus", "G15", 3, "E101", [("PID", "E101, 'LIQUID'"), ("REPORT", COLUMN_TEMPS + " and Fig 4.1")]),
    "TT207": ("TemperatureInstrument", "E101 temperature", "PRT", "Fieldbus", "H15", 2, "E101", [("PID", "E101, 'VAPOUR'"), ("REPORT", COLUMN_TEMPS)]),
    "TT206": ("TemperatureInstrument", "E101 temperature", "PRT", "Fieldbus", "H15", 2, "E101", [("PID", "E101, 'LIQUID'"), ("REPORT", COLUMN_TEMPS + " and Fig 4.1")]),
    "TT205": ("TemperatureInstrument", "E101 temperature", "PRT", "Fieldbus", "J15", 2, "E101", [("PID", "E101, 'VAPOUR'"), ("REPORT", COLUMN_TEMPS)]),
    "TT204": ("TemperatureInstrument", "E101 temperature", "PRT", "Fieldbus", "J15", 2, "E101", [("PID", "E101, 'LIQUID'"), ("REPORT", COLUMN_TEMPS + " and Fig 4.1")]),
    "TT109": ("TemperatureInstrument", "E101 bottom temperature", "PRT", "Fieldbus", "J15", 1, "E101", [("PID", "E101 base"), ("REPORT", COLUMN_TEMPS + " and Fig 4.1")]),
    "TT413": ("TemperatureInstrument", "E101 top temperature (sample point 1)", None, None, None, None, "E101",
              [("REPORT", "Fig 4.1 (paired with sample 1 at 6.85 m)")]),
    "AT400": ("Instrument", "CO2 in gas samples along E101", "ABB gas analyser", None, None, None, "E101",
              [("DIFF", "row AT400 (samples along the absorber, 'SAMPLE TO ABB GAS ANALYSER')"), ("REPORT", "Fig 4.1")]),
})
PHASES = {"TT411": "liquid", "TT308": "vapour", "TT307": "liquid", "TT306": "vapour", "TT305": "liquid",
          "TT207": "vapour", "TT206": "liquid", "TT205": "vapour", "TT204": "liquid"}

# sample id -> (sample number, height above sample 6 in m, paired TT, sample valve or None)
SAMPLE_POINTS = {
    "E101_sample_1": (1, 6.85, "TT413", None),
    "E101_sample_2": (2, 5.48, "TT307", "V308"),
    "E101_sample_3": (3, 4.11, "TT305", "V306"),
    "E101_sample_4": (4, 2.74, "TT206", "V207"),
    "E101_sample_5": (5, 1.37, "TT204", "V205"),
    "E101_sample_6": (6, 0.00, "TT109", None),
}

INTERLOCKS = {
    "IL_E101_level_LL": dict(label="E101 low-low level plant shutdown (LZAL109)", by=["LSLL109"], trips=["J101a", "J101b"],
                             cite=[("HAZOP", "element 8, item 2 and element 10, item 15")]),
    "IL_E101_level_HH": dict(label="E101 high-high level plant shutdown (LZAH107)", by=["LSHH107"], trips=["J101a", "J101b"],
                             cite=[("HAZOP", "element 10, items 11 and 12")]),
}
LIMITS.update({
    "LZAL109": ("E101", "level", "trip", None, None, "-", [("HAZOP", "element 8, item 2 and element 10, item 15")]),
    "LZAH107": ("E101", "level", "trip", None, None, "-", [("HAZOP", "element 10, items 11 and 12")]),
    "TAH_C200_outlet": ("TT210", "temperature", "alarm", None, None, "C", [("HAZOP", "element 10, item 7 (TAH added on the C200 process outlet)")]),
})
HAZOP_COVERAGE["10"] = ["E101", "RV400", "PSHH117", "LSHH107", "LSLL109"]
HAZOP_ALARM_HOST = {"LZAL109": "LSLL109", "LZAH107": "LSHH107"}
OPEN_ITEMS.update({
    "AOI13": ("Sample valves for E101 samples 1 and 6 are not identified on the P&ID", ["AT400"], "Full-size P&ID or site check"),
    "AOI14": ("TT413 (paired with sample 1) is in REPORT Fig 4.1 but not in the instrument list; its grid and floor are unknown", ["TT413"], "Full-size P&ID"),
    "AOI15": ("The setpoints of LZAL109, LZAH107 and the C200 outlet TAH are not documented", ["LSLL109", "LSHH107", "TT210"], "Control system settings"),
})

HAZOP_E10_ROWS = [
    {"element": "10", "element_title": "ABSORBER COLUMN E101", "item": 1, "parameter": "FLOW", "guideword": "NO", "cause": "Blockage in the packing / trays / redistributors", "consequence": "Flowrate down column < inlet flowrate .: accumulation of liquid.  Worst scenario - liquid into inlet of blower J102 depending on height of blocked plane (i.e. liquid space above vs plant liquid inventory)", "safeguard": "Low fluid inventory in system", "action": "Tuning fork liquid level detection & trip downstream of K402 cyclone.", "action_taken": "Action completed"},
    {"element": "10", "element_title": "ABSORBER COLUMN E101", "item": 2, "parameter": "FLOW", "guideword": "MORE", "cause": "Pump J100 running at overspeed", "consequence": "", "safeguard": "Column is designed to accommodate excess flow", "action": "", "action_taken": ""},
    {"element": "10", "element_title": "ABSORBER COLUMN E101", "item": 3, "parameter": "FLOW", "guideword": "MORE", "cause": "High rate of gas up column from CO2 and N2 feed system", "consequence": "Overpressure lower section of E101 and K101", "safeguard": "", "action": "RV at outlet to K101?", "action_taken": "RV added"},
    {"element": "10", "element_title": "ABSORBER COLUMN E101", "item": 4, "parameter": "FLOW", "guideword": "LESS", "cause": "", "consequence": "", "safeguard": "", "action": "Note - packing & column designed for 2.3-2.5 bar operation on MEA & 50kg/hr CO2.", "action_taken": "None"},
    {"element": "10", "element_title": "ABSORBER COLUMN E101", "item": 5, "parameter": "FLOW", "guideword": "MISDIRECTED", "cause": "Liquid flow into gas sampling system", "consequence": "Blockage in column", "safeguard": "", "action": "Position gas analysis on top floor (above liquid switch on K402)", "action_taken": "Action completed"},
    {"element": "10", "element_title": "ABSORBER COLUMN E101", "item": 6, "parameter": "", "guideword": "", "cause": "Foaming within column?", "consequence": "", "safeguard": "", "action": "Ensure cleanliness at start-up / during commissioning", "action_taken": "See SOP and commisioning"},
    {"element": "10", "element_title": "ABSORBER COLUMN E101", "item": 7, "parameter": "TEMP.", "guideword": "HIGHER", "cause": "Failure of coolant to C200 - hot liquid entering", "consequence": "Inefficiency in CO2 removal", "safeguard": "", "action": "Consider TAH on process outlet from C200", "action_taken": "TAH added"},
    {"element": "10", "element_title": "ABSORBER COLUMN E101", "item": 8, "parameter": "PRESSURE", "guideword": "HIGHER", "cause": "Failure of pressure control system", "consequence": "", "safeguard": "RV400", "action": "Put a PSH onto the column; size RV400 for maximum filling gas feed rate", "action_taken": "Action completed"},
    {"element": "10", "element_title": "ABSORBER COLUMN E101", "item": 9, "parameter": "PRESSURE", "guideword": "LOWER", "cause": "Failure of pressure control system", "consequence": "", "safeguard": "", "action": "", "action_taken": ""},
    {"element": "10", "element_title": "ABSORBER COLUMN E101", "item": 10, "parameter": "PRESSURE", "guideword": "LOWER", "cause": "Leak or valve left open (air admittance or gas- or liquid-sampling);", "consequence": "", "safeguard": "AA valves normally locked in closed state.  Gas sampling flowrate heavily restricted.  SOP on liquid sampling.", "action": "Blanks on liquid sampling valves as part of SOP.", "action_taken": "None"},
    {"element": "10", "element_title": "ABSORBER COLUMN E101", "item": 11, "parameter": "LEVEL", "guideword": "HIGHER", "cause": "Interruption to liquid flow out", "consequence": "Overfilling column base", "safeguard": "LZAH107 plant shutdown", "action": "", "action_taken": ""},
    {"element": "10", "element_title": "ABSORBER COLUMN E101", "item": 12, "parameter": "LEVEL", "guideword": "HIGHER", "cause": "Pump J100 running substantially faster than J101", "consequence": "Overfilling column base", "safeguard": "LZAH107 plant shutdown", "action": "Differential flowrate alarm between respective flowmeters", "action_taken": "Action completed"},
    {"element": "10", "element_title": "ABSORBER COLUMN E101", "item": 13, "parameter": "LEVEL", "guideword": "HIGHER", "cause": "Plant quiescent", "consequence": "Liquid settles in column base", "safeguard": "Sizing of column base v/v plant inventory", "action": "", "action_taken": ""},
    {"element": "10", "element_title": "ABSORBER COLUMN E101", "item": 14, "parameter": "LEVEL", "guideword": "HIGHER", "cause": "Higher than expected water usage in K101", "consequence": "Water inventory in solution increases slowly over time", "safeguard": "Design for balanced inventory", "action": "Consider saturating with 15% MEA water?", "action_taken": "Action completed"},
    {"element": "10", "element_title": "ABSORBER COLUMN E101", "item": 15, "parameter": "LEVEL", "guideword": "LOWER", "cause": "Converse of some of the above", "consequence": "", "safeguard": "LZAL109", "action": "", "action_taken": ""},
    {"element": "10", "element_title": "ABSORBER COLUMN E101", "item": 16, "parameter": "Chem REACTION", "guideword": "MORE", "cause": "High Pressure", "consequence": "none", "safeguard": "pressure controls", "action": "", "action_taken": ""},
    {"element": "10", "element_title": "ABSORBER COLUMN E101", "item": 17, "parameter": "Chem REACTION", "guideword": "LESS", "cause": "Low pressure", "consequence": "none", "safeguard": "pressure controls", "action": "", "action_taken": ""},
]
