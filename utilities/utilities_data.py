"""
Piece 8: utilities (Pilot Plant 2514): steam and condensate to H100, and the three cooling water streams.
Built from the documents first, then traced by the team.

Steam (HAZOP element 13): building steam > XV140 > V100 > PT101/PI100 > V101 > FT100 > V102 > FT101 > FCV110
    > H100 shell > TT118 > K100 > V103 > V105 > NRV110 > condensate return.  V106 bypasses K100 (HAZOP 13.6).
Cooling water ('the 3 cooling water streams', REPORT F.5.3, Fig F.4 and Fig B.22):
    C106 stream (floor 1): V194 > PCV103 > FCV102 > FT106 > C106 > TT119 > V136 > return
    C200 stream (floor 2): V208 > FCV201 > FCV200 > FT201 > C200 > V214 > return
    C400 stream (floor 4): V405 > PCV415 > FCV401 > FT402 > C400 > V410 > V411 > return
Utility flows pass through the exchanger shells via their own nozzles, so they never join the process flow paths.
ORDER ALONG EACH LINE IS INFERRED FROM THE VALVE TABLES AND GRIDS: to be traced.
"""
INSTR = "Appendix B instrument list"
STEAM_LIST = "Fig B.2 (valves along the steam stream)"
STEAM_UP = "Fig F.11 (steam start-up valves)"
STEAM_TX = "Fig F.12 (transmitters to monitor steam flow)"
CW_LIST = "Fig B.22 (valves along the cooling water stream)"
CW_UP = "Fig F.4 (cooling water start-up valves)"
TO_TRACE = "order inferred from the valve tables and grids; to be traced on the P&ID"

SECTION = dict(
    prefix="utl", loop_id="SteamRoute", mode="FigureOfEight", flow="feedsInto",
    loop_label="Steam and condensate route to H100",
    loop_note="Building steam heats the MEA in the H100 reboiler shell and leaves as condensate through the K100 trap. "
              "FCV110 sets the steam flow (TIC100 > FIC100 cascade, stripping loop).",
    loop_cite=[("REPORT", STEAM_LIST + ", " + STEAM_UP + ", " + STEAM_TX), ("HAZOP", "element 13 (STEAM / CONDENSATE SYSTEM to H1 (H100))"),
               ("DERIVED", TO_TRACE)],
)

ITEMS = {
    # ---- steam and condensate ----
    "STEAM_SUPPLY": dict(cls="SupplyConnection", label="Building steam supply", floor=1, grid="L2",
                         note="Untagged connection to the building steam supply (HAZOP 13.4 'excess demand on building steam supply').",
                         cite=[("PID", "steam supply arrow near L2"), ("HAZOP", "element 13, item 4")]),
    "XV140": dict(cls="ShutdownValve", valve="shutdown (SOV/XV)", floor=1, grid="L2", pos="open",
                  note="Steam isolation valve at the supply, opened at start-up and closed at shutdown. Not in the REPORT instrument or valve lists.",
                  cite=[("REPORT", STEAM_UP + " and Fig F.15 (XV140, SOV (XV), L2, floor 1)")]),
    "V100": dict(cls="ManualValve", valve="ball", floor=1, grid="L3", pos="open",
                 note="Steam isolation valve; the start-up and shutdown tables give grid L2.",
                 cite=[("PID", "grid L3"), ("REPORT", STEAM_LIST + " (L3, closed then open) and " + STEAM_UP + " (L2)")]),
    "V103": dict(cls="ManualValve", valve="ball", floor=1, grid="M5", pos="open", note="Condensate side valve (grid M5 in Fig B.2, M4 in Fig F.11).",
                 cite=[("PID", "grid M5"), ("REPORT", STEAM_LIST + " (M5, closed then open) and " + STEAM_UP + " (M4)")]),
    "V104": dict(cls="ManualValve", valve="ball", floor=1, grid="M4", pos="closed", note="Closed in operation (drain or blowdown; UT05).",
                 cite=[("PID", "grid M4"), ("REPORT", STEAM_LIST + " (M4, closed in operation) and " + STEAM_UP)]),
    "NRV110": dict(cls="CheckValve", valve="check", floor=1, grid="M3", pos="open", note="Non-return valve at the end of the steam/condensate stream.",
                   cite=[("PID", "grid M3"), ("REPORT", STEAM_LIST + " (NRV110, M3, closed then open)")]),
    "K100": dict(cls="SteamTrap", label="K100 condensate trap on the H100 steam side", floor=1,
                 note="HAZOP 13.6: a fault within K100 redirects flow via V106 (its bypass). Not in the REPORT lists; position UT02.",
                 cite=[("HAZOP", "element 13, items 1 and 6"), ("DERIVED", "role from HAZOP 13.6; to be traced")]),
    "RV107": dict(cls="ReliefValve", valve="relief", floor=1, grid="M5", pos="closed", note="Relief valve on the steam/condensate side (set pressure UT05).",
                  cite=[("PID", "grid M5"), ("REPORT", "valve list (RV107, M5, floor 1)")]),
    "CONDENSATE_RETURN": dict(cls="ReturnConnection", label="Condensate return", floor=1,
                              note="Untagged condensate return after NRV110.", cite=[("PID", "condensate line after NRV110"), ("DERIVED", TO_TRACE)]),
    # ---- cooling water ----
    "CW_SUPPLY": dict(cls="SupplyConnection", label="Cooling water supply (building)", floor=1,
                      note="Untagged connection feeding the three cooling water streams (C106, C200, C400).",
                      cite=[("REPORT", "section F.5.3 ('the 3 cooling water streams')")]),
    "CW_RETURN": dict(cls="ReturnConnection", label="Cooling water return ('COOLING WATER TO DWG 108712-10-002')", floor=1,
                      note="Untagged cooling water return.", cite=[("PID", "'COOLING WATER TO DWG N.108712-10-002'"), ("REPORT", "section F.5.3")]),
    "V194": dict(cls="ManualValve", valve="ball", floor=1, grid="R15", pos="open", note="C106 cooling water stream.",
                 cite=[("PID", "grid R15"), ("REPORT", CW_UP + " (V194, ball, R15, open)")]),
    "PCV103": dict(cls="PressureControlValve", valve="pressure control", floor=1, grid="R15", pos="open",
                   note="Pressure regulator on the C106 cooling water stream (UT09). Grid R15 in Fig F.4, Q16 in the valve list.",
                   cite=[("PID", "grid R15"), ("REPORT", CW_UP + " (PCV103, R15, open) and valve list (Q16)")]),
    "V195": dict(cls="ManualValve", valve="ball", floor=1, grid="R17", pos="closed", note="Closed on the C106 cooling water stream (drain?).",
                 cite=[("PID", "grid R17"), ("REPORT", CW_UP + " (V195, ball, R17, close)")]),
    "V136": dict(cls="ManualValve", floor=1, grid="P18", pos="open", note="On the C106 cooling water return ('COOLING WATER TO DWG' on the P&ID).",
                 cite=[("PID", "next to 'COOLING WATER TO DWG N.108712-10-002'"), ("REPORT", "valve list (V136, P18, floor 1)")]),
    "V196": dict(cls="ManualValve", valve="ball", floor=1, grid="N19", pos="open", note="In the cooling water start-up table; stream not identified (UT08).",
                 cite=[("REPORT", CW_UP + " (V196, ball, N19, open)")]),
    "V197": dict(cls="ManualValve", valve="ball", floor=1, grid="N19", pos="open", props={"hasLockingHandle": True},
                 note="In the cooling water start-up table (O17) and the vent start-up table (V197 (L), N19); stream not identified (UT07, UT08).",
                 cite=[("REPORT", CW_UP + " (V197, O17, open) and Fig F.3 (V197 (L), N19)")]),
    "V208": dict(cls="ManualValve", valve="ball", floor=2, grid="H11", pos="open", note="C200 cooling water stream.",
                 cite=[("PID", "grid H11"), ("REPORT", CW_LIST + " (V208, H11) and " + CW_UP + " (H12)")]),
    "V209": dict(cls="ManualValve", valve="ball", floor=2, grid="H13", pos="open", props={"hasLockingHandle": True},
                 note="In the cooling water valve list and the vent start-up table (V209 (L)); which line it is on is UT07.",
                 cite=[("PID", "grid H13"), ("REPORT", CW_LIST + " (V209, H13, closed then open) and Fig F.3 (V209 (L), H13)")]),
    "V214": dict(cls="ManualValve", valve="ball", floor=2, grid="K13", pos="open", note="C200 cooling water stream (return side).",
                 cite=[("PID", "grid K13"), ("REPORT", CW_LIST + " (V214, K13, closed then open) and " + CW_UP + " (K14)")]),
    "V215": dict(cls="ManualValve", valve="ball", floor=2, grid="K13", pos="closed", note="Closed on the C200 cooling water stream (drain?).",
                 cite=[("PID", "grid K13"), ("REPORT", CW_LIST + " (V215, K13, closed) and " + CW_UP + " (K14)")]),
    "V405": dict(cls="ManualValve", valve="ball", floor=4, grid="C14", pos="open", note="C400 cooling water stream.",
                 cite=[("PID", "grid C14"), ("REPORT", CW_LIST + " (V405, C14, closed then open) and " + CW_UP)]),
    "PCV415": dict(cls="PressureControlValve", valve="pressure control", floor=4, grid="C14", pos="open",
                   note="Pressure regulator on the C400 cooling water stream (UT09). The valve list gives floor 3.",
                   cite=[("PID", "grid C14"), ("REPORT", CW_UP + " (PCV415, C14, floor 4, open)")]),
    "V410": dict(cls="ManualValve", valve="ball", floor=4, grid="D10", pos="open", note="C400 cooling water stream (return side).",
                 cite=[("PID", "grid D10"), ("REPORT", CW_LIST + " (V410, D10, closed then open) and " + CW_UP)]),
    "V411": dict(cls="ManualValve", valve="ball", floor=4, grid="D10", pos="open", props={"hasLockingHandle": True},
                 note="C400 cooling water stream (return side); also in the vent start-up table as V411 (L) (UT07).",
                 cite=[("PID", "grid D10"), ("REPORT", CW_LIST + " (V411, D10) and Fig F.3 (V411 (L), D10)")]),
    "V412": dict(cls="ManualValve", valve="ball", floor=4, grid="D14", pos="closed", note="Closed on the C400 cooling water stream (drain?).",
                 cite=[("PID", "grid D14"), ("REPORT", CW_LIST + " (V412, D14, closed) and " + CW_UP + " (C14)")]),
}

INSTRUMENTS = {
    "PT101": ("PressureInstrument", "steam supply pressure", "gauge pressure transmitter", "4-20mA", "L3", 1, "H100",
              [("PID", "grid L3"), ("REPORT", INSTR + " (PT101, L4) and " + STEAM_TX + " (L3)")]),
    "PI100": ("PressureInstrument", "steam pressure indication (local)", None, None, "L3", 1, "H100", [("PID", "grid L3"), ("REPORT", INSTR + " (PI100, L3)")]),
    "PI101": ("PressureInstrument", "steam/condensate pressure indication (local)", None, None, "K4", 1, "H100", [("PID", "grid K4"), ("REPORT", INSTR + " (PI101, K4)")]),
    "FI100": ("FlowInstrument", "steam flow indication (local, on FT100)", None, None, "L4", 1, "H100", [("PID", "on FT100"), ("REPORT", INSTR + " (FI100, L4)")]),
    "TT117": ("TemperatureInstrument", "steam temperature into H100", "PRT", "Profibus-PA", "L4", 1, "H100",
              [("PID", "grid L4"), ("REPORT", STEAM_TX + " (TT117, L4) and " + INSTR + " (M4)")]),
    "TT118": ("TemperatureInstrument", "condensate temperature out of H100", "PRT", "Profibus-PA", "M5", 1, "H100",
              [("PID", "grid M5"), ("REPORT", STEAM_TX + " (TT118, M5) and " + INSTR + " (L4)")]),
    "FI106": ("FlowInstrument", "C106 cooling water flow indication (local, on FT106)", None, None, "R16", 1, "C106", [("PID", "on FT106"), ("REPORT", INSTR + " (FI106, R16)")]),
    "TT119": ("TemperatureInstrument", "C106 cooling water temperature (UT11)", "PRT", "4-20mA", "R17", 1, "C106", [("PID", "grid R17"), ("REPORT", INSTR + " (TT119, R17)")]),
    "FI200": ("FlowInstrument", "C200 cooling water flow indication (local)", None, None, "H11", 2, "C200", [("PID", "grid H11"), ("REPORT", INSTR + " (FI200, H11)")]),
    "FI201": ("FlowInstrument", "C200 cooling water flow indication (local, on FT201)", None, None, "H12", 2, "C200", [("PID", "on FT201"), ("REPORT", INSTR + " (FI201, H12)")]),
}

NOZZLES = {
    "H100_N_steam_in": ("H100 steam inlet (shell side)", [("PID", "H100 steam side"), ("DERIVED", "utility side kept separate from the MEA side")], "H100"),
    "H100_N_condensate_out": ("H100 condensate outlet (shell side)", [("PID", "H100 steam side")], "H100"),
    "C106_N_cw_in": ("C106 cooling water inlet", [("PID", "C106")], "C106"),
    "C106_N_cw_out": ("C106 cooling water outlet", [("PID", "C106")], "C106"),
    "C200_N_cw_in": ("C200 cooling water inlet", [("PID", "C200")], "C200"),
    "C200_N_cw_out": ("C200 cooling water outlet", [("PID", "C200")], "C200"),
    "C400_N_cw_in": ("C400 cooling water inlet", [("PID", "C400")], "C400"),
    "C400_N_cw_out": ("C400 cooling water outlet", [("PID", "C400")], "C400"),
}

LOOP = [
    ("STEAM_SUPPLY", "inline"), ("XV140", "inline"), ("V100", "inline"),
    ("PT101", "tie-in"), ("PI100", "tie-in"),
    ("V101", "inline"), ("FT100", "inline"), ("FI100", "tie-in"), ("V102", "inline"), ("FT101", "inline"), ("FCV110", "inline"),
    ("TT117", "tie-in"),
    ("H100_N_steam_in", "inline"), ("H100_N_condensate_out", "inline"),
    ("TT118", "tie-in"), ("PI101", "tie-in"), ("RV107", "branch"),
    ("K100", "inline"), ("V106", "branch"),
    ("V103", "inline"), ("V104", "branch"), ("V105", "inline"), ("NRV110", "inline"),
    ("CONDENSATE_RETURN", "inline"),
]
CW_CHAINS = [
    ["CW_SUPPLY", "V194", "PCV103", "FCV102", "FT106", "C106_N_cw_in", "C106_N_cw_out", "V136", "CW_RETURN"],
    ["CW_SUPPLY", "V208", "FCV201", "FCV200", "FT201", "C200_N_cw_in", "C200_N_cw_out", "V214", "CW_RETURN"],
    ["CW_SUPPLY", "V405", "PCV415", "FCV401", "FT402", "C400_N_cw_in", "C400_N_cw_out", "V410", "V411", "CW_RETURN"],
]
EXTRA_PIPING = ([(a, b) for chain in CW_CHAINS for a, b in zip(chain, chain[1:])]
                + [("H100_N_condensate_out", "V106"), ("V106", "V103"),     # V106 bypasses K100 (HAZOP 13.6)
                   ("C106_N_cw_out", "V195"), ("C200_N_cw_out", "V215"), ("C400_N_cw_out", "V412")])
LINKS = ([(a, "feedsInto", b) for chain in CW_CHAINS for a, b in zip(chain, chain[1:])]
         + [("TT119", "monitors", "C106"), ("RV107", "protects", "H100"),
            ("HAZOP_13_01", "concerns", "V106"), ("HAZOP_13_06", "concerns", "V106"), ("HAZOP_13_06", "concerns", "K100"),
            ("HAZOP_13_04", "concerns", "FCV110")])
KNOWN_TAGS = ["H100", "FCV110", "V101", "V102", "V105", "V106", "FT100", "FT101"]

BYPASSES = {
    "K100_bypass": dict(label="Condensate bypass around K100 via V106", from_item="H100_N_condensate_out", via=["V106"], to_item="V103",
                        bypasses=["K100"], state="closed", procedure=None,
                        cite=[("HAZOP", "element 13, items 1 and 6 ('blowdown via bypass'; 'flow redirected via v106')")]),
}

HAZOP_COVERAGE = {"13": ["XV140", "V100", "V103", "V104", "NRV110", "K100", "RV107", "PT101", "TT117", "TT118"]}

OPEN_ITEMS = {
    "UT01": ("Order along the steam line (XV140 > V100 > PT101 > V101 > FT100 > V102 > FT101 > FCV110 > H100 > K100 > V103 > V105 > NRV110) is inferred",
             ["XV140", "V100", "K100", "NRV110"], "Trace on the P&ID"),
    "UT02": ("K100 (HAZOP 13: trap whose fault redirects flow via V106) is not in the REPORT lists; its tag and position need confirming", ["K100"],
             "Full-size P&ID"),
    "UT03": ("V101, V102, V105 and V106 are recorded closed (stripping loop test line-up) but V100 to V105 are open in normal running (Figs B.2, F.11)",
             ["V100", "V103"], "Mode-dependent valve settings, as for V217"),
    "UT04": ("TT117 and TT118 grids differ between the instrument list (M4 / L4) and Fig F.12 (L4 / M5)", ["TT117", "TT118"], "Trace on the P&ID"),
    "UT05": ("RV107 set pressure, and the role of V104 (closed in operation: drain or blowdown?)", ["RV107", "V104"], "Trace on the P&ID"),
    "UT06": ("Order along each cooling water stream and where they share supply and return headers", ["V194", "V208", "V405"], "Trace on the P&ID"),
    "UT07": ("V209, V411 and V197 appear in both the vent start-up table (Fig F.3) and the cooling water tables", ["V209", "V411", "V197"],
             "Trace on the P&ID"),
    "UT08": ("V196 and V197 (N19 / O17) are in the cooling water start-up table but their stream is not identified", ["V196", "V197"], "Trace on the P&ID"),
    "UT09": ("PCV103 (C106) and PCV415 (C400) are taken to be cooling water pressure regulators; no regulator is listed for C200", ["PCV103", "PCV415"],
             "Trace on the P&ID"),
    "UT10": ("Which cooling water temperatures exist (TT119 assumed on C106; TT214 to TT217 and TT402 to TT404 not yet placed)", ["TT119"], "Trace on the P&ID"),
}
