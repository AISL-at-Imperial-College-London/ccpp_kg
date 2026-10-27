"""
Section 3: the rich-side link, which joins the absorption and stripping loops into
the full figure-of-eight circulation (normal running).

Rich side: E101 > J101a|J101b > FT108 > V151 > C100 (cold side, TT112 in, TT113 out)
           > SDV152 > H200a|H200b > V403 > V402 > top of E100
REPORT 4.x: rich MEA "is pumped through heat exchangers (C100 and H200)" to the stripper.
REPORT B.1.6 / B.1.7 give the operational state of every valve on the rich and lean streams.
Items already in the stripping or absorption KG are referenced, not redefined.
"""
RICH_LIST = "list of valves along the rich MEA stream (B.1.6)"
LEAN_LIST = "list of valves along the lean MEA stream (B.1.7)"

SECTION = dict(
    prefix="rich", loop_id="FigureOfEight", mode="FigureOfEight", flow="nextStep",
    loop_label="Figure-of-eight circulation (normal running)",
    loop_note="Absorber and stripper circulating together. One J101 train runs at a time (J101a shown in the settings). "
              "The H100 reboiler circuit on E100 is a separate loop (ReboilerCircuit).",
    loop_cite=[("REPORT", "section 4 ('pumped through heat exchangers (C100 and H200)'), " + RICH_LIST + " and " + LEAN_LIST),
               ("ASPEN_V3", "streams S8 > S15 (rich through C100) and S3 > S2 > 2 (lean to E101)")],
    # operational states from REPORT B.1.6 and B.1.7
    settings={"V151": "open", "SDV152": "open", "SDV125": "closed", "V124": "closed", "V150": "closed",
              "V319": "closed", "V315": "closed", "V403": "open", "V402": "open",
              "V134a": "open", "V135a": "open", "V143a": "open", "V144a": "open",
              "V134b": "closed", "V135b": "closed", "V143b": "closed", "V144b": "closed",
              "SDV123": "open", "V119a": "open", "V119b": "open", "V198a": "closed", "V198b": "closed",
              "V211": "open", "V213": "open", "V212": "closed", "V217": "closed",
              "V110": "open", "V112": "open", "V113a": "open", "V113b": "open", "V116": "open",
              "V117a": "open", "V117b": "open", "V120": "closed", "V121": "open", "V309": "closed"},
)

ITEMS = {
    "V151": dict(cls="ManualValve", floor=1, grid="M9", pos="open",
                 note="On the rich line from FT108 to the C100 cold side. Other REPORT tables give grid N9 or N8.",
                 cite=[("PID", "rich line to C100, near grid M9"), ("REPORT", RICH_LIST + " (open in operation)")]),
    "V150": dict(cls="ManualValve", valve="ball", floor=1, grid="N10", pos="closed",
                 note="On the rich MEA stream list, closed in operation; its function is not identified (ROI01).",
                 cite=[("REPORT", RICH_LIST + " (closed) and start-up tables (ball, O10)")]),
    "SDV152": dict(cls="ShutdownValve", valve="shutdown (solenoid-operated)", floor=1, grid="L9", pos="open",
                   note="Sends rich MEA from the C100 cold side to the heaters H200a/b. Tagged SDV152 on the P&ID (team check); the REPORT calls it SOV152. Closed in the stripping loop test (SDV125 used instead).",
                   cite=[("PID", "grid L9, tagged SDV152"), ("REPORT", RICH_LIST + " (SOV152, open in operation) and SOV list"),
                         ("TEAM", "P&ID tags are SDV152 and SDV125")]),
    "V319": dict(cls="ManualValve", valve="ball", floor=3, grid="G8", pos="closed",
                 note="On the rich MEA stream list, closed in operation, at grid G8 next to the E100 side-return nozzle. May sit on the side-return line (ROI02).",
                 cite=[("REPORT", RICH_LIST + " (closed) and start-up tables (ball, G8, floor 3)")]),
    # valves on the lean list that were not in either loop KG yet (not traced on the P&ID)
    "V406": dict(cls="ManualValve", floor=4, grid="F14", pos="closed", note="On the lean MEA stream list (closed in operation); not yet traced (ROI04).",
                 cite=[("REPORT", LEAN_LIST + " (F14, floor 4, closed)")]),
    "V118": dict(cls="ManualValve", floor=1, grid="L11", pos="closed", note="On the lean MEA stream list (closed in operation); not yet traced (ROI04).",
                 cite=[("REPORT", LEAN_LIST + " (L11, floor 1, closed)")]),
    "V111": dict(cls="ManualValve", floor=1, grid="N8", pos="closed", note="On the lean MEA stream list (closed in operation); not yet traced (ROI04).",
                 cite=[("REPORT", LEAN_LIST + " (N8, floor 1, closed)")]),
    "V160": dict(cls="ManualValve", floor=1, grid="N8", pos="closed", note="On the lean MEA stream list (closed in operation); not yet traced (ROI04).",
                 cite=[("REPORT", LEAN_LIST + " (N8, floor 1, closed)")]),
    "V115": dict(cls="ManualValve", floor=1, grid="M11", pos="closed", note="On the lean MEA stream list (closed in operation); not yet traced (ROI04).",
                 cite=[("REPORT", LEAN_LIST + " (M11, floor 1, closed)")]),
    "V122": dict(cls="ManualValve", floor=1, grid="N11", pos="closed", note="On the lean MEA stream list (closed in operation); not yet traced (ROI04).",
                 cite=[("REPORT", LEAN_LIST + " (N11, floor 1, closed)")]),
}

INSTRUMENTS = {
    "TT112": ("TemperatureInstrument", "rich MEA leaving E101 and entering C100", "PRT", "Profibus-PA", "M9", 1, "C100",
              [("PID", "C100 cold inlet, grid M9"), ("REPORT", "Appendix B instrument list and Appendix D ('rich MEA leaving the absorber (E101) and entering C100')")]),
    "TT113": ("TemperatureInstrument", "rich MEA leaving C100", "PRT", "Profibus-PA", "L9", 1, "C100",
              [("PID", "C100 cold outlet, grid L9"), ("REPORT", "Appendix B instrument list and Appendix D ('rich MEA leaving C100')")]),
}

# The full figure-of-eight in flow order (items from all three sections). Parallel entries = pump or heater trains.
LOOP = [
    ("E101_N_sump_outlet", "inline"),
    (("V134a", "inline"), ("V134b", "inline")), (("V135a", "inline"), ("V135b", "inline")),
    (("J101a", "inline"), ("J101b", "inline")), (("PCV120a", "inline"), ("PCV120b", "inline")),
    (("V143a", "inline"), ("V143b", "inline")), (("V144a", "inline"), ("V144b", "inline")),
    ("FT108", "inline"),
    ("V151", "inline"),
    ("TT112", "tie-in"), ("C100", "inline"), ("TT113", "tie-in"),
    ("SDV152", "inline"),
    (("H200a", "inline"), ("H200b", "inline")),
    ("TT213", "tie-in"),
    ("V403", "inline"), ("V402", "inline"), ("E100_N_top_inlet", "inline"),
    ("E100", "inline"),
    ("E100_N_sump_outlet", "inline"),
    ("V110", "inline"), ("V112", "inline"), ("TT104", "tie-in"), ("C100", "inline"), ("TE105", "tie-in"),
    ("V113a", "inline"), ("V113b", "inline"), ("J100", "inline"), ("PCV122", "inline"), ("V116", "inline"),
    ("V117a", "inline"), ("Z102", "inline"), ("V117b", "inline"), ("V121", "inline"),
    ("FT103", "inline"), ("FT104", "inline"),
    ("SDV123", "inline"),
    ("V119b", "inline"), ("V119a", "inline"), ("V211", "inline"), ("N200", "inline"), ("V213", "inline"),
    ("TT209", "tie-in"), ("C200", "inline"), ("TT210", "tie-in"),
    ("NRV400", "inline"), ("E101_N_top_inlet", "inline"),
    ("E101", "inline"),
]
TRAIN_A = ["V134a", "V135a", "J101a", "PCV120a", "V143a", "V144a", "H200a"]
TRAIN_B = ["V134b", "V135b", "J101b", "PCV120b", "V143b", "V144b", "H200b"]

# Physical connections that join the two loops (cold side of C100 and the heater header)
EXTRA_PIPING = [("FT108", "V151"), ("V151", "C100"), ("C100", "SDV152"), ("SDV152", "H200a"), ("SDV152", "H200b"),
                ("FT104", "SDV123")]

PROCEDURES = {
    "PROC_figure_of_eight_lineup": dict(
        label="Figure-of-eight valve line-up (operational states)", trigger="Normal running of absorber and stripper together",
        cite=[("REPORT", RICH_LIST + " and " + LEAN_LIST + " (operational state column)")],
        steps=[(f"Set {v} {p}", v, p) for v, p in [
            ("V151", "open"), ("SDV152", "open"), ("SDV125", "closed"), ("V124", "closed"), ("V150", "closed"),
            ("V319", "closed"), ("V315", "closed"), ("V403", "open"), ("V402", "open"),
            ("V134a", "open"), ("V135a", "open"), ("V143a", "open"), ("V144a", "open"),
            ("V134b", "closed"), ("V135b", "closed"), ("V143b", "closed"), ("V144b", "closed"),
            ("SDV123", "open"), ("V406", "closed"), ("V119a", "open"), ("V119b", "open"), ("V198a", "closed"), ("V198b", "closed"),
            ("V210", "closed"), ("V211", "open"), ("V213", "open"), ("V217", "closed"),
            ("V110", "open"), ("V112", "open"), ("V113a", "open"), ("V113b", "open"), ("V116", "open"), ("V120", "closed"),
            ("V117a", "open"), ("V117b", "open"), ("V118", "closed"), ("V121", "open"), ("V109", "closed"),
            ("V111", "closed"), ("V160", "closed"), ("V115", "closed"), ("V122", "closed")]]),
}

HAZOP_COVERAGE = {"8": ["V151", "SDV152", "V150"]}

OPEN_ITEMS = {
    "ROI01": ("V150 is on the rich MEA stream list (closed) but its function and connection are not identified", ["V150"], "Full-size P&ID"),
    "ROI02": ("V319 is on the rich MEA stream list at grid G8, next to the E100 side-return nozzle; it may be on the side-return line (routes C and D)", ["V319", "V309"],
              "Full-size P&ID around grid G8"),
    "ROI03": ("Which J101 train is normally on duty in the figure-of-eight (the REPORT lists J101a open)", ["J101a", "J101b"], "Plant supervisor"),
    "ROI04": ("V406, V118, V111, V160, V115 and V122 are on the lean MEA stream list but not yet traced on the P&ID", ["V406", "V118", "V111", "V160", "V115", "V122"],
              "Full-size P&ID"),
}
