"""
Piece 9: MEA storage, filling and draining (Pilot Plant 2514). Built from the documents first, then traced by the team.

HAZOP element 9a (FILLING) and 9b (DRAINING); HAZOP note M9: the 2010 'B100' became two tanks, one feed and one receiver
(F100 and R100; DIFF says their labels are swapped on the P&ID). J105 pumps MEA from the feed tank along the long fill/drain
header at the bottom of the drawing into the plant (via V115/V122 at J100, HAZOP M14, and V146/V147 at the J101 pumps,
HAZOP 9b); for draining, equipment drains drop into the same header and liquid goes back to the receiver tank.
Grids: REPORT valve and instrument lists. ROUTE ORDER IS NOT DOCUMENTED: to be traced on the P&ID.
"""
VALVES = "valve lists"
INSTR = "Appendix B instrument list"
TO_TRACE = "connection inferred from the HAZOP and grids; to be traced on the P&ID"

SECTION = dict(
    prefix="mea", loop_id="MEAFillRoute", mode="Filling", flow="feedsInto",
    loop_label="MEA filling route (feed tank > J105 > fill/drain header)",
    loop_note="J105 pumps MEA from the feed tank into the fill/drain header, which connects to the plant at J100 (V115/V122) "
              "and at the J101 pumps (V146/V147). Draining uses the same header back to the receiver tank.",
    loop_cite=[("HAZOP", "elements 9a (filling) and 9b (draining); notes M9, M14, M16, M17"), ("DERIVED", TO_TRACE)],
)

ITEMS = {
    "F100": dict(cls="StorageTank", label="F100 MEA feed tank", floor=1, grid="N2",
                 note="Feed tank for filling the plant (HAZOP M9 'one feed, one receiver'; low-level trip M17). DIFF: the R100 and F100 labels are "
                      "swapped on the P&ID (N2 and N3), so this is the tank drawn as R100 (MS01).",
                 cite=[("PID", "tank at N2 (labelled R100)"), ("DIFF", "row R100 & F100 (wrong label on P&ID, N2 & N3)"), ("HAZOP", "notes M9 and M17")]),
    "R100": dict(cls="StorageTank", label="R100 MEA receiver tank", floor=1, grid="N3",
                 note="Receiver tank for draining the plant (HAZOP M9; high-level trip M16). DIFF: labels swapped on the P&ID, so this is the tank drawn as F100 (MS01).",
                 cite=[("PID", "tank at N3 (labelled F100)"), ("DIFF", "row R100 & F100 (wrong label on P&ID, N2 & N3)"), ("HAZOP", "notes M9 and M16")]),
    "J105": dict(cls="Pump", label="J105 MEA filling / draining pump", floor=1, grid="N4",
                 note="Speed-controlled with limited maximum flow (HAZOP 9a.4); check valves downstream (9a.6); thermal trip (9b.1); dry-run protection (9a.3); "
                      "stopped by the liquid flow switch at the manual vent V138 (9a.7).",
                 cite=[("PID", "grid N4"), ("REPORT", "pump list (J105, floor 1, N4)"), ("HAZOP", "element 9a, items 1 to 7; element 9b, items 1, 2 and 4")]),
    "PCV126": dict(cls="PressureControlValve", valve="pressure control", floor=1, grid="N5",
                   note="On the J105 discharge side; role (spillback or back-pressure) to trace (MS04).",
                   cite=[("PID", "grid N5, next to J105"), ("REPORT", VALVES + " (PCV126, N5, floor 1)")]),
    "V138": dict(cls="ManualValve", valve="manual vent", floor=1,
                 note="Manual vent ('valve N') on the filling line; a liquid flow switch on its right-hand side stops J105 (HAZOP 9a.7, 9b.4). Not in the REPORT lists (MS05).",
                 cite=[("HAZOP", "element 9a, item 7 and element 9b, item 4 ('Valve N (manual vent - V138)')")]),
    "FILL_DRAIN_HEADER": dict(cls="PipeSegment", label="MEA fill / drain header (long horizontal line along the bottom of the drawing)", floor=1,
                              note="Untagged. Connects J105 and the tanks to the plant drains and fill points (MS07, MS08).",
                              cite=[("PID", "long horizontal line along row O"), ("TEAM", "V126 line from K101 runs along it to the J105 system"), ("DERIVED", TO_TRACE)]),
}
# tank and pump valves (grids from the REPORT lists; positions to trace)
for tag, grid, note in [("V156", "N6", "Closed (start-up table, N5/6)."), ("V157", "N5", ""), ("V158", "O4", ""), ("V159a", "O3", ""), ("V159b", "O2", ""),
                        ("V161a", "O3", ""), ("V161b", "O2", ""), ("V162", "N2", "Near the tank at N2."), ("V163", "O3", ""), ("V164", "N3", "Near the tank at N3."),
                        ("V199", "O4", "")]:
    ITEMS[tag] = dict(cls="ManualValve", floor=1, grid=grid, pos="closed" if tag == "V156" else None,
                      note=("Valve around the MEA tanks and J105; position to trace (MS02). " + note).strip(),
                      cite=[("PID", f"grid {grid}"), ("REPORT", VALVES + f" ({tag}, {grid}, floor 1)")])
# drain valves dropping to the header, and the J101 fill/drain direction valves (HAZOP 9b)
for tag, grid, note in [("V153", "O8", "Drain, closed (start-up table)."), ("V154", "O8", "Drain, closed (start-up table gives O7)."), ("V155", "O7", "Drain, closed (start-up table)."),
                        ("V160", "N8", "Closed (start-up table)."), ("V167", "N9", ""), ("V168", "N9", ""), ("V149", "O12", ""), ("V148", "O13", "Ball valve, closed."),
                        ("V146a", "O15", "Sets fill or drain at J101a (HAZOP 9b.4/9b.5)."), ("V146b", "O16", "Sets fill or drain at J101b (HAZOP 9b.4/9b.5)."),
                        ("V147a", "O15", "Sets fill or drain at J101a (HAZOP 9b.4/9b.5)."), ("V147b", "O16", "Sets fill or drain at J101b (HAZOP 9b.4/9b.5).")]:
    ITEMS[tag] = dict(cls="ManualValve", floor=1, grid=grid, pos="closed",
                      note=("On a line dropping to the fill/drain header; which equipment it drains is MS07. " + note).strip(),
                      cite=[("PID", f"grid {grid}"), ("REPORT", VALVES + f" ({tag}, {grid}, floor 1)")] + ([("HAZOP", "element 9b, items 4 and 5")] if tag.startswith(("V146", "V147")) else []))
ITEMS["NRV107"] = dict(cls="CheckValve", valve="check", floor=1, grid="N2", pos="open", note="Check valve where the return line enters the left-hand tank, F100 (team trace).",
                       cite=[("PID", "grid N2"), ("REPORT", VALVES + " (NRV107, N2, floor 1)")])
ITEMS["NRV108"] = dict(cls="CheckValve", valve="check", floor=1, grid="N3", pos="open", note="Check valve where the return line enters the right-hand tank, R100 (team trace).",
                       cite=[("PID", "grid N3"), ("REPORT", VALVES + " (NRV108, N3, floor 1)")])

INSTRUMENTS = {
    "TT116": ("TemperatureInstrument", "MEA temperature at J105", "PRT", "4-20mA", "N5", 1, "J105", [("PID", "grid N5"), ("REPORT", INSTR + " (TT116, N5)")]),
    "FI110": ("FlowInstrument", "flow indication at the tank at N2 (local; N2 blanket? MS06)", None, None, "N2", 1, "F100", [("PID", "grid N2"), ("REPORT", INSTR + " (FI110, N2)")]),
    "PI112": ("PressureInstrument", "pressure indication at the tank at N2 (local)", None, None, "N2", 1, "F100", [("PID", "grid N2"), ("REPORT", INSTR + " (PI112, N2)")]),
    "FI111": ("FlowInstrument", "flow indication at the tank at N3 (local; N2 blanket? MS06)", None, None, "M3", 1, "R100", [("PID", "grid M3"), ("REPORT", INSTR + " (FI111, M3)")]),
    "PI113": ("PressureInstrument", "pressure indication at the tank at N3 (local)", None, None, "M3", 1, "R100", [("PID", "grid M3"), ("REPORT", INSTR + " (PI113, M3)")]),
}

LOOP = [
    ("F100", "inline"),
    ("J105", "inline"), ("TT116", "tie-in"), ("PCV126", "branch"), ("V138", "branch"),
    ("FILL_DRAIN_HEADER", "inline"),
]
DRAINS = ["V153", "V154", "V155", "V160", "V167", "V168", "V149", "V148", "V146a", "V146b", "V147a", "V147b", "V126"]
EXTRA_PIPING = ([("NRV107", "F100"), ("NRV108", "R100")]   # return line into both tanks (team trace)
                + [(d, "FILL_DRAIN_HEADER") for d in DRAINS]
                + [("FILL_DRAIN_HEADER", "R100"),                         # draining back to the receiver tank (HAZOP M9, M14)
                   ("FILL_DRAIN_HEADER", "V122"), ("FILL_DRAIN_HEADER", "V115")])  # filling line to J100 via V115 and V122 (HAZOP M14)
LINKS = [("TT116", "monitors", "J105")]
KNOWN_TAGS = ["E100", "E101", "J100", "V115", "V122", "V126"]
HAZOP_ALIASES = {"V146": "V146a", "V147": "V147a"}

LIMITS = {
    "TRIP_R100_high_level": ("R100", "level", "trip", None, None, "-", [("HAZOP", "note M16 (high-level trip on B100 as receiver from the plant)")]),
    "TRIP_F100_low_level": ("F100", "level", "trip", None, None, "-", [("HAZOP", "note M17 (low-level trip on B100 as feed vessel to the plant)")]),
    "TRIP_J105_thermal": ("J105", "motor temperature", "trip", None, None, "-", [("HAZOP", "element 9b, item 1 (thermal trip on pump)")]),
    "TRIP_J105_liquid_at_vent": ("J105", "liquid flow at V138", "trip", None, None, "-", [("HAZOP", "element 9a, item 7 (liquid flow switch shuts down J105)")]),
    "TRIP_J105_dry_run": ("J105", "liquid at pump inlet", "trip", None, None, "-", [("HAZOP", "element 9a, item 3 (liquid sensor upstream of pump kills the pump)")]),
}

DISCREPANCIES = [("R100_F100_labels", ["R100", "F100"], "N2/N3", "R100 at N2 and F100 at N3", "Labels swapped (F100 at N2, R100 at N3)")]

HAZOP_ELEMENTS = {"9a": "FILLING / EMPTYING Line - FILLING", "9b": "FILLING / EMPTYING Line - DRAINING"}
HAZOP_COVERAGE = {"9a": ["F100", "J105", "PCV126", "V138", "FILL_DRAIN_HEADER"], "9b": ["R100", "J105", "V146a", "V146b", "V147a", "V147b"]}

OPEN_ITEMS = {
    "MS01": ("Which tank is which on the plant (DIFF: R100 and F100 labels swapped on the P&ID), and which one feeds J105", ["F100", "R100"], "Site check"),
    "MS02": ("Order of the tank outlet valves (V158, V159a/b, V161a/b, V163, V199, V156, V157) between the tanks and J105", ["J105", "V158"], "Trace on the P&ID"),
    "MS03": ("RV107 (M5): the J105 spillback RV that HAZOP 9a.1 added, or a steam/condensate relief (where piece 8 put it)?", ["J105"], "Trace on the P&ID"),
    "MS04": ("Role of PCV126 on the J105 discharge (spillback or back-pressure)", ["PCV126"], "Trace on the P&ID"),
    "MS05": ("V138 (manual vent 'valve N') and the liquid flow switch that stops J105 are not in the REPORT lists", ["V138"], "Full-size P&ID"),
    "MS06": ("The return line enters F100 via NRV107 and R100 via NRV108 (team trace); confirm whether it is the drain return or the N2 line, and where FI110/PI112 and FI111/PI113 sit", ["F100", "R100", "NRV107", "NRV108"], "Trace on the P&ID"),
    "MS07": ("Which equipment drains into the header through V153, V154, V155, V160, V167, V168, V149 and V148", ["FILL_DRAIN_HEADER"], "Trace on the P&ID"),
    "MS08": ("How the header connects to the plant: V115/V122 at J100 (HAZOP M14) and V146a/b, V147a/b at the J101 pumps (HAZOP 9b)", ["FILL_DRAIN_HEADER", "V146a"],
             "Trace on the P&ID"),
    "MS09": ("HAZOP note M26: the area around B100 (now F100/R100) was not covered by the 2010 HAZOP", ["F100", "R100"], "Note"),
}

HAZOP_ROWS = [
    {"element": "9a", "item": 1, "parameter": "FLOW", "guideword": "NO", "cause": "Valve closed", "consequence": "Overpressure pump", "safeguard": "none", "action": "RV spillback around pump J105", "action_taken": "RV added"},
    {"element": "9a", "item": 2, "parameter": "FLOW", "guideword": "NO", "cause": "Pump non-functioning", "consequence": "Cannot fill plant", "safeguard": "n/a", "action": "", "action_taken": ""},
    {"element": "9a", "item": 3, "parameter": "FLOW", "guideword": "NO", "cause": "B100 empty or not connected", "consequence": "Pump runs dry", "safeguard": "", "action": "Ensure Pump OK for limited dry running.  Consider tuning-fork liquid sensor upstream of pump to kill pump (only) in absence of liquid", "action_taken": "Action completed"},
    {"element": "9a", "item": 4, "parameter": "FLOW", "guideword": "MORE", "cause": "", "consequence": "", "safeguard": "Pump will be speed-controlled & max flowrate limited", "action": "", "action_taken": ""},
    {"element": "9a", "item": 5, "parameter": "FLOW", "guideword": "LESS", "cause": "Partially closed valve", "consequence": "Takes longer to fill vessels etc", "safeguard": "", "action": "", "action_taken": ""},
    {"element": "9a", "item": 6, "parameter": "FLOW", "guideword": "REVERSE", "cause": "'Wrong' choice of pump - centrifugal - blowback from pressurised system through pump", "consequence": "Overfill feed tank", "safeguard": "", "action": "Either pump has built-in CVs or fit CV downstream of pump", "action_taken": "CVs included"},
    {"element": "9a", "item": 7, "parameter": "FLOW", "guideword": "MISDIRECTED", "cause": "Incorrect setting of valving", "consequence": "Liquid fill of whole of the filling line", "safeguard": "SOPs", "action": "Put liquid flow switch RHS of Valve 'N' (manual vent - V138) to shut down J105 only on liquid flow", "action_taken": "Liquid flow switch added"},
    {"element": "9a", "item": 8, "parameter": "TEMP.", "guideword": "HIGHER", "cause": "Diurnal temp variation operating on locked-in liquid inventory", "consequence": "High pressure in sections", "safeguard": "SOP issue", "action": "Valve op table to ensure no locked in sections containing liquid.  Check SOPs - esp for closedown", "action_taken": "See SOP"},
    {"element": "9a", "item": 9, "parameter": "TEMP.", "guideword": "LOWER", "cause": "Diurnal temp variation operating on locked-in liquid inventory", "consequence": " Freezing?", "safeguard": "Build heating - maintenance control", "action": "", "action_taken": ""},
    {"element": "9a", "item": 10, "parameter": "PRESSURE", "guideword": "HIGHER", "cause": "See temp above", "consequence": "", "safeguard": "", "action": "", "action_taken": ""},
    {"element": "9a", "item": 11, "parameter": "COMPOSITION", "guideword": "INCORRECT", "cause": "Wrong tank is attached to J105", "consequence": "", "safeguard": "SOP", "action": "", "action_taken": ""},
    {"element": "9b", "item": 1, "parameter": "FLOW", "guideword": "NO", "cause": "Valves incorrectly set", "consequence": "Starve pump / overheats", "safeguard": "SOP", "action": "Ensure there is a thermal trip on pump", "action_taken": "Action completed"},
    {"element": "9b", "item": 2, "parameter": "FLOW", "guideword": "NO", "cause": "Pump not running", "consequence": "Cannot drain line", "safeguard": "SOP  - pump shutdown on low liquid at inlet", "action": "Consider current monitoring on pumps", "action_taken": "Action completed"},
    {"element": "9b", "item": 3, "parameter": "FLOW", "guideword": "LESS", "cause": "partially closed valves", "consequence": "speed of draining impaired", "safeguard": "SOPs", "action": "", "action_taken": ""},
    {"element": "9b", "item": 4, "parameter": "FLOW", "guideword": "REVERSE", "cause": "V147/V146 incorrectly set", "consequence": "J105 bypass RV comes into play if resistance experienced down the line OR liquid reaches manual vent position", "safeguard": "SOPs", "action": "Pump kill (liquid) switch installed RHS of Valve 'N' (manual vent - V138)", "action_taken": "Action completed"},
    {"element": "9b", "item": 5, "parameter": "FLOW", "guideword": "REVERSE", "cause": "V147/V146 incorrectly set", "consequence": "Might fill E100/E101 instead of emptying", "safeguard": "", "action": "", "action_taken": ""},
    {"element": "9b", "item": 6, "parameter": "VACUUM", "guideword": "INSUFFICIENT", "cause": "Almost-closed air admittance valve", "consequence": "Pump thermal trip?", "safeguard": "SOPs", "action": "", "action_taken": ""},
]