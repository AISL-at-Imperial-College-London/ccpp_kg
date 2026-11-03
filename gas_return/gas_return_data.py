"""
Piece 7: gas returns (Pilot Plant 2514). Built from the documents first, then traced by the team.

N2 return (HAZOP element 5, 'N2 RETURN E101 to E101 via K402, J102 (& K101)'), a closed loop:
    top of E101 > K402 > return line (TT304, FT303 and FT304 'next to each other on the N2 recycle stream pipe')
    > K102 > J102 lobe blower > K101 saturator > E101
    FCV111 (with SDV170) recycles N2 from K101 back to K102, reducing the N2 entering E101 (REPORT D.4, Fig D.6).
    PCV118 is the J102 spillback (HAZOP 5.2/5.3).
CO2 return (HAZOP element 6, 'CO2 RETURN FROM K401 to E101 via J103'):
    K401 > FT301/FT302 > K103 catchpot > J103 reciprocating compressor > NRV104 > fresh-gas header > K101 > E101
    PCV119 recycles CO2 around K103 to hold the E100 pressure (REPORT D.4, Fig D.16/D.17).
"""
INSTR = "Appendix B instrument list"
VALVES = "valve lists"
TO_TRACE = "order to be traced on the P&ID"

SECTION = dict(
    prefix="grt", loop_id="N2ReturnLoop", mode="FigureOfEight", flow="feedsInto",
    loop_label="N2 return loop (E101 > K402 > K102 > J102 > K101 > E101)",
    loop_note="N2 is not absorbed, so it is recirculated: J102 blows it from the K402 overhead back through K101 into E101. "
              "Fresh N2 and CO2 (piece 5) top it up. FCV111 recycles part of it from K101 back to K102 to set the N2 flow into E101.",
    loop_cite=[("HAZOP", "element 5 (N2 RETURN E101 to E101 via K402, J102 (& K101))"),
               ("REPORT", "section D.4, Fig D.6/D.7 (FT303/FT304 on the N2 recycle stream pipe; FCV111 bypass from K101 to K102)"),
               ("DERIVED", TO_TRACE)],
)

ITEMS = {
    "K102": dict(cls="KnockoutDrum", label="K102 knockout pot on the J102 suction", floor=1,
                 note="Catches liquid before the J102 blower (drain V187). The FCV111 recycle from K101 returns here (REPORT D.4). Grid not in the REPORT lists (near L16 to M17).",
                 cite=[("PID", "K102 next to J102, near L16"), ("REPORT", "section D.4 ('a bypass route is created from K101 to K102')")]),
    "J102": dict(cls="Blower", label="J102 lobe blower (N2 return)", floor=1, grid="L17",
                 note="Blows the recycled N2 from K102 into K101. Combined spillback (PCV118) and speed control (HAZOP 5.2).",
                 cite=[("PID", "grid L17"), ("REPORT", "pump list (J102, floor 1, L17)"), ("SUMMARY", "p.144 (Blower - J102, lobe blower)"), ("HAZOP", "element 5, items 1 to 4")]),
    "PCV118": dict(cls="PressureControlValve", valve="pressure control", floor=1, pos="open",
                   note="Spillback around J102 (HAZOP 5.3 'excess spillback via PCV118'). Not in the REPORT lists; position GR03.",
                   cite=[("HAZOP", "element 5, items 2 and 3")]),
    "PCV114": dict(cls="PressureControlValve", valve="pressure control", floor=1,
                   note="HAZOP 5.5: excess flow via PCV114 causes loss of plant pressure or a composition change. Not in the REPORT lists; position and role GR03.",
                   cite=[("HAZOP", "element 5, item 5 ('Excess flow via PCV 114')")]),
    "V187": dict(cls="ManualValve", valve="ball", floor=1, grid="M17", pos="closed", note="Drain valve on K102.",
                 cite=[("PID", "below K102, grid M17"), ("REPORT", VALVES + " (V187, ball, M17, floor 1, closed)")]),
    "K103": dict(cls="KnockoutDrum", label="K103 alarmed catchpot on the J103 suction", floor=1,
                 note="Protects the J103 compressor from liquid (HAZOP 6.9 'alarmed catchpot upstream of J103'). PCV119 recycles CO2 around it (REPORT D.4). Grid not in the REPORT lists (near M20).",
                 cite=[("PID", "K103 next to J103, near M20"), ("REPORT", "section D.4 ('the recycle loop around K103')"), ("HAZOP", "element 6, item 9")]),
    "J103": dict(cls="Compressor", label="J103 CO2 return compressor (single-stage reciprocating, air-cooled)", floor=1, grid="M20",
                 note="Compresses the CO2 from K401 and returns it to the absorber via NRV104 and K101. A shutdown trip protects it if it is starved (HAZOP 6.1).",
                 cite=[("PID", "grid M20"), ("REPORT", "pump list (J103, floor 1, M20)"), ("SUMMARY", "p.145 (Compressor - J103)"), ("HAZOP", "element 6")]),
    "V185": dict(cls="ManualValve", valve="ball", floor=1, grid="M20", pos="closed", props={"hasLockingHandle": True},
                 note="Locked ball valve at J103/K103 (drain); the REPORT gives M20 and M21.",
                 cite=[("PID", "grid M20"), ("REPORT", VALVES + " (V185 (L), ball, M20/M21, floor 1, closed)")]),
    "NRV104": dict(cls="CheckValve", valve="check", floor=1, grid="O18", pos="open",
                   note="Non-return valve on the CO2 return (HAZOP 6.3/6.5: 'Ensure NRV104 reliable on CO2').",
                   cite=[("PID", "grid O18"), ("REPORT", VALVES + " (NRV104, O18, floor 1)"), ("HAZOP", "element 6, items 3 and 5")]),
    "NRV401": dict(cls="CheckValve", valve="check", floor=4, grid="D18", pos="open",
                   note="Non-return valve on the top floor on the CO2 line from K401 (position to trace, GR05).",
                   cite=[("PID", "grid D18"), ("REPORT", VALVES + " (NRV401, D18, floor 4)")]),
    "V311": dict(cls="ManualValve", valve="ball", floor=3, grid="F17", pos="closed", note="Ball valve at the V310/V313 manifold on the overhead gas side (GR02).",
                 cite=[("PID", "grid F17"), ("REPORT", VALVES + " (V311, ball, F17, floor 3, closed)")]),
    "V312": dict(cls="ManualValve", valve="ball", floor=3, grid="F17", pos="closed", note="Ball valve at the V310/V313 manifold on the overhead gas side (GR02).",
                 cite=[("PID", "grid F17"), ("REPORT", VALVES + " (V312, ball, F17, floor 3, closed)")]),
    "SDV171": dict(cls="ShutdownValve", valve="shutdown (solenoid-operated)", floor=1, grid="L19", pos="open",
                   note="Shutdown valve next to K101 (the REPORT lists it as SOV171, closed at start, open in operation). Role GR08.",
                   cite=[("PID", "next to K101"), ("REPORT", VALVES + " (SOV171, L19, floor 1, open in operation)")]),
    "V172": dict(cls="ManualValve", floor=1, grid="L19", pos="open", note="Valve next to K101 and SDV171 (open in operation). Role GR08.",
                 cite=[("REPORT", VALVES + " (V172, L18/L19, floor 1, open in operation)")]),
}

INSTRUMENTS = {
    "TT304": ("TemperatureInstrument", "N2 return temperature", "PRT", "Fieldbus", "G17", 3, "J102",
              [("PID", "grid G17, next to FT303"), ("REPORT", INSTR + " (TT304, G17, floor 3)")]),
    "FI303": ("FlowInstrument", "flow indication (N2 return)", None, None, "H17", 3, "J102", [("PID", "on FT303"), ("REPORT", INSTR + " (FI303, H17)")]),
    "FI304": ("FlowInstrument", "flow indication (N2 return)", None, None, "H17", 3, "J102", [("PID", "on FT304"), ("REPORT", INSTR + " (FI304, H17)")]),
    "TT114": ("TemperatureInstrument", "J102 temperature", "K-type thermocouple", "4-20mA", "L17", 1, "J102",
              [("PID", "grid L17"), ("REPORT", INSTR + " (TT114, L17)")]),
    "FT107": ("FlowInstrument", "flow at J102 (position to trace)", "variable area volumetric flow meter", "4-20mA", "L17", 1, "J102",
              [("PID", "grid L17"), ("REPORT", INSTR + " (FT107, L17)")]),
    "TT115": ("TemperatureInstrument", "J103 temperature", "K-type thermocouple", "4-20mA", "M20", 1, "J103",
              [("PID", "grid M20"), ("REPORT", INSTR + " (TT115, M20)")]),
    "LT104": ("LevelInstrument", "K101 level (HAZOP LIR104)", "differential pressure transmitter", "4-20mA", "M19", 1, "K101",
              [("PID", "on K101"), ("REPORT", INSTR + " (LT104, M19)"), ("HAZOP", "element 3, item 5 (LIR 104)")]),
    "LI106": ("LevelInstrument", "K101 level indication (local)", None, None, "L18", 1, "K101", [("PID", "on K101"), ("REPORT", INSTR + " (LI106, L18)")]),
    "TI121": ("TemperatureInstrument", "K101 temperature indication (local)", None, None, "L18", 1, "K101", [("PID", "on TT121"), ("REPORT", INSTR + " (TI121, L18)")]),
    "PT110": ("PressureInstrument", "gas pressure near K101 (may be the 'PT113' read on the K101 to E101 line, GR09)", "gauge pressure transmitter", "Fieldbus", "J18", 1, "E101",
              [("REPORT", INSTR + " (PT110, J18, floor 1)")]),
    "PI402": ("PressureInstrument", "pressure indication after K401 (local)", None, None, "C16", 4, "K401", [("PID", "on PT402, grid C16"), ("REPORT", INSTR + " (PI402, C16)")]),
    "PI403": ("PressureInstrument", "absorber pressure indication (local)", None, None, "D17", 4, "E101", [("PID", "near PT403, grid D17"), ("REPORT", INSTR + " (PI403, D17)")]),
    "TI410": ("TemperatureInstrument", "CO2 leaving C400 indication (local)", None, None, "C15", 4, "C400", [("PID", "on TT410, grid C15"), ("REPORT", INSTR + " (TI410, C15)")]),
    "FI402": ("FlowInstrument", "C400 cooling water flow indication (local)", None, None, "C13", 4, "C400", [("PID", "on FT402, grid C13"), ("REPORT", INSTR + " (FI402, C13)")]),
}

# N2 return loop in flow order (FT303 and FT304 are side by side; their order is to be traced)
LOOP = [
    ("E101", "inline"), ("E101_N_gas_outlet", "inline"), ("K402", "inline"), ("K402_N_gas_to_return", "inline"),
    ("TT304", "tie-in"),
    ("FT303", "inline"), ("FI303", "tie-in"),
    ("FT304", "inline"), ("FI304", "tie-in"),
    ("K102", "inline"), ("V187", "branch"),
    ("J102", "inline"), ("TT114", "tie-in"), ("FT107", "tie-in"), ("PCV118", "branch"),
    ("K101", "inline"),
    ("E101_N_gas_inlet", "inline"), ("E101", "inline"),
]
EXTRA_PIPING = [
    ("FCV111", "K102"),                                   # N2 recycle K101 > SDV170 > FCV111 > K102 (REPORT D.4)
    ("J102", "PCV118"), ("PCV118", "K102"),               # J102 spillback (HAZOP 5.3)
    ("K102", "V187"),
    # CO2 return (physical), in flow order: K401 > NRV401 > FT302 > FT301 > K103 > J103 > NRV104 > fresh-gas header
    ("K401_N_gas_outlet", "NRV401"), ("NRV401", "FT302"), ("FT302", "FT301"), ("FT301", "K103"), ("K103", "J103"),
    ("J103", "NRV104"), ("NRV104", "FEED_GAS_HEADER"),
    ("J103", "PCV119"), ("PCV119", "K103"),              # recycle loop around K103 (REPORT D.4)
    ("K103", "V185"),
]
LINKS = [
    # gas leaving K401 flows to its gas outlet (piece 4 had only the pipe); found by question C09
    ("K401", "feedsInto", "K401_N_gas_outlet"),
    # active flow along the CO2 return
    ("K401_N_gas_outlet", "feedsInto", "NRV401"), ("NRV401", "feedsInto", "FT302"), ("FT302", "feedsInto", "FT301"),
    ("FT301", "feedsInto", "K103"), ("K103", "feedsInto", "J103"), ("J103", "feedsInto", "NRV104"), ("NRV104", "feedsInto", "FEED_GAS_HEADER"),
]
KNOWN_TAGS = ["FT301", "FT302", "FT303", "FT304", "K401", "K402", "K101", "PCV119", "C400", "E101", "E100", "J102", "J103"]
HAZOP_ALIASES = {"C300": "C400"}

BYPASSES = {
    "K101_N2_recycle": dict(label="N2 recycle from K101 back to K102 via SDV170 and FCV111", from_item="K101", via=["SDV170", "FCV111"],
                            to_item="K102", bypasses=["E101"], state="modulating", procedure=None,
                            cite=[("REPORT", "section D.4, Fig D.6/D.7 ('a bypass route is created from K101 to K102')")]),
    "J102_spillback": dict(label="J102 spillback via PCV118", from_item="J102", via=["PCV118"], to_item="K102", bypasses=["K101"],
                           state="modulating", procedure=None, cite=[("HAZOP", "element 5, items 2 and 3")]),
    "K103_CO2_recycle": dict(label="CO2 recycle around K103 via PCV119 (E100 pressure control)", from_item="J103", via=["PCV119"], to_item="K103",
                             bypasses=["NRV104"], state="modulating", procedure=None,
                             cite=[("REPORT", "section D.4, Fig D.16/D.17 ('the recycle loop around K103')")]),
}

LIMITS = {
    "FAL_N2_return": ("FT303", "N2 return flow", "alarm", None, None, "-", [("HAZOP", "element 5, item 1 (FAL on FT303/304 added)")]),
    "FAL_CO2_return": ("FT301", "CO2 return flow", "alarm", None, None, "-", [("HAZOP", "element 6, item 3 (low flow alarm on FT301/302)")]),
    "LAH_K103": ("K103", "level", "alarm", None, None, "-", [("HAZOP", "element 6, item 9 (alarmed catchpot upstream of J103; alarm added)")]),
    "TRIP_J103_starved": ("J103", "suction flow", "trip", None, None, "-", [("HAZOP", "element 6, item 1 (pump shutdown trip added)")]),
    "TAH_C400_carryover": ("C400", "temperature", "alarm", None, None, "C", [("HAZOP", "element 6, item 6 (alarm around C300/C400 for vapour carry-over)")]),
}

HAZOP_ELEMENTS = {"5": "N2 RETURN E101 to E101 via K402, J102 (& K101)", "6": "CO2 RETURN FROM K401 to E101 via J103"}
HAZOP_COVERAGE = {"5": ["K402", "K102", "J102", "PCV118", "PCV114", "FT303", "FT304"],
                  "6": ["K401", "K103", "J103", "NRV104", "FT301", "FT302", "PCV119"]}

OPEN_ITEMS = {
    "GR01": ("Order of items on the N2 return line (TT304, FT303/FT304, K102, J102, TT114, FT107)", ["J102", "K102"], "Trace on the P&ID"),
    "GR02": ("Where the N2 return leaves the K402 vent line, and what the V310/V313/V311/V312 manifold does", ["V311", "V312", "K402"], "Trace on the P&ID"),
    "GR03": ("PCV118 (J102 spillback) and PCV114 (HAZOP 5.5) are not in the REPORT lists; their positions are unknown", ["PCV118", "PCV114"], "Full-size P&ID"),
    "GR04": ("K102 level switch tag (LSHH110 on the P&ID image) and the K103 alarm instrument tag", ["K102", "K103"], "Full-size P&ID"),
    "GR05": ("CO2 return order K401 > NRV401 > FT302 > FT301 > K103 > J103 > NRV104 is inferred; DIFF says FT301/FT302 are in the reverse order to the P&ID", ["NRV401", "J103"],
             "Trace on the P&ID"),
    "GR06": ("Where the J103 discharge joins: the fresh-gas header (assumed) or K101 directly", ["J103", "NRV104"], "Trace on the P&ID"),
    "GR07": ("PCV119 is in the vent start-up table (Fig F.3) but REPORT D.4 has it recycling CO2 around K103; does it also vent?", ["PCV119"], "Trace on the P&ID"),
    "GR08": ("Roles of SDV171 and V172 next to K101", ["SDV171", "V172"], "Trace on the P&ID"),
    "GR09": ("PT110 (REPORT, J18) may be the transmitter read as 'PT113' on the K101 to E101 line", ["PT110"], "Full-size P&ID"),
    "GR10": ("Aspen treats the gas as once-through (no N2 or CO2 recycle), so recycle flows are not simulated", ["J102", "J103"], "Note for model comparison"),
}

HAZOP_ROWS = [
    {"element": "5", "item": 1, "parameter": "FLOW", "guideword": "NO", "cause": "J102 failed / non operative", "consequence": "No N2 gasflow up column", "safeguard": "Control system indicates no flow; no safety implications", "action": "Consider FAL on FT303/304", "action_taken": "FAL added"},
    {"element": "5", "item": 2, "parameter": "FLOW", "guideword": "MORE", "cause": "J102 running over fast", "consequence": "High N2 flow up column", "safeguard": "Combined spillback and speed control", "action": "none", "action_taken": "None"},
    {"element": "5", "item": 3, "parameter": "FLOW", "guideword": "LESS", "cause": "Excess spillback via PCV118", "consequence": "As NO", "safeguard": "Detectable on FT303/304", "action": "", "action_taken": ""},
    {"element": "5", "item": 4, "parameter": "FLOW", "guideword": "REVERSE", "cause": "J102 motor wrongly wired", "consequence": "Reverse flow in column", "safeguard": "Commissioning", "action": "", "action_taken": ""},
    {"element": "5", "item": 5, "parameter": "FLOW", "guideword": "MISDIRECTED", "cause": "Excess flow via PCV 114", "consequence": "Loss of pressure in plant / composition change", "safeguard": "", "action": "", "action_taken": ""},
    {"element": "5", "item": 6, "parameter": "TEMP.", "guideword": "HIGHER", "cause": "Failure of C200 (liquid into column E101)", "consequence": "n/a", "safeguard": "", "action": "", "action_taken": ""},
    {"element": "5", "item": 7, "parameter": "PRESSURE", "guideword": "HIGHER", "cause": "As E101", "consequence": "", "safeguard": "", "action": "", "action_taken": ""},
    {"element": "5", "item": 8, "parameter": "PRESSURE", "guideword": "LOWER", "cause": "As E101", "consequence": "", "safeguard": "", "action": "", "action_taken": ""},
    {"element": "5", "item": 9, "parameter": "COMPOSITION", "guideword": "INCORRECT", "cause": "Inefficient dewatering in K402", "consequence": "Liquid carry-over to J102", "safeguard": "Demister pad ; oversize liq return on K402", "action": "", "action_taken": ""},
    {"element": "6", "item": 1, "parameter": "FLOW", "guideword": "NO", "cause": "K401 / C300 (now C400) blocked", "consequence": "No flow to J103", "safeguard": "", "action": "Consider consequences of starving J103", "action_taken": "Pump shutdown trip added"},
    {"element": "6", "item": 2, "parameter": "FLOW", "guideword": "NO", "cause": "J103 not functioning", "consequence": "Plant not operating", "safeguard": "FT301/302", "action": "", "action_taken": ""},
    {"element": "6", "item": 3, "parameter": "FLOW", "guideword": "NO", "cause": "Blockage any position in flowline (NRV104??)", "consequence": "Plant not operating", "safeguard": "FT301/303", "action": "Ensure NRV104 reliable on CO2; low flow alarm on FT301/302", "action_taken": "Action completed"},
    {"element": "6", "item": 4, "parameter": "FLOW", "guideword": "LESS", "cause": "Loss of CO2 inventory over time", "consequence": "", "safeguard": "Analytical points; CO2 make-up", "action": "", "action_taken": ""},
    {"element": "6", "item": 5, "parameter": "FLOW", "guideword": "REVERSE", "cause": "Failure of NRV104 + low pressure d/s of C400", "consequence": "instable pressure control loop protecting J103", "safeguard": "NRV104", "action": "Consider control of PCV 119 on Flow (vs pressure) in light of spec. of J103", "action_taken": "Action completed"},
    {"element": "6", "item": 6, "parameter": "TEMP.", "guideword": "HIGHER", "cause": "C300 (C400) not working", "consequence": "Vapour carryover to J103; damage to J103", "safeguard": "Temp & flow indicators on C300 water throughput", "action": "Put an appropriate alarm around C300 to warn of vapour carryover", "action_taken": "Alarm added"},
    {"element": "6", "item": 7, "parameter": "PRESSURE", "guideword": "HIGHER", "cause": "As E100", "consequence": "", "safeguard": "", "action": "", "action_taken": ""},
    {"element": "6", "item": 8, "parameter": "PRESSURE", "guideword": "LOWER", "cause": "As E100", "consequence": "", "safeguard": "", "action": "", "action_taken": ""},
    {"element": "6", "item": 9, "parameter": "COMPOSITION", "guideword": "INCORRECT", "cause": "Excess water carryover", "consequence": "Damage to J103", "safeguard": "separator & demister pad", "action": "As above; consider alarmed catchpot upstream of J103", "action_taken": "Alarm added"},
]
