"""
Fill-in section (Pilot Plant 2514): the report-listed tags not yet in any piece (local gauges, drains, spare valves).
Each tag gets the type, grid, floor, signal and position the REPORT gives. A link to equipment is added only where the
documents support it (same loop number as a documented instrument, same grid and a/b suffix as a pump, or a HAZOP action);
everything else is flagged 'position to trace' (open items FI01 to FI07).
REPORT tags SOVxxx are written SDVxxx, as on the P&ID (as for SDV123, SDV125, SDV170, SDV171).
"""
VALVES = "valve lists and start-up tables"
INSTR = "Appendix B instrument list"

SECTION = dict(
    prefix="fil", loop_id="FillInRegister", mode="FigureOfEight", flow="feedsInto",
    loop_label="Fill-in register (report tags without a traced route)",
    loop_note="Register of report-listed items whose position on a line is still to be traced; no flow route.",
    loop_cite=[("REPORT", "Appendix B instrument and valve lists, start-up and shutdown tables")],
)

# tag: (class, valve type, floor, grid, normal position, note)
V = {
    "V107": ("ManualValve", "ball", 1, "K8", "closed", "Near the E100 base (J8/K8 in the tables). FI01"),
    "V108": ("ManualValve", None, 1, "L8", "closed", "Near the E100 base. FI01"),
    "V200": ("ManualValve", "ball", 2, "J8", "closed", "Ball/needle pair with V201 on E100, floor 2 (sample or drain point?). FI01"),
    "V201": ("ManualValve", "needle", 2, "J8", "closed", "Ball/needle pair with V200 on E100, floor 2 (tables also give H8). FI01"),
    "V202": ("ManualValve", "ball", 2, "H8", "closed", "Ball/needle pair with V203 on E100, floor 2. FI01"),
    "V203": ("ManualValve", "needle", 2, "H8", "closed", "Ball/needle pair with V202 on E100, floor 2. FI01"),
    "V300": ("ManualValve", "needle", 3, "H8", "closed", "Ball/needle pair with V301 on E100, floor 3. FI01"),
    "V301": ("ManualValve", "ball", 3, "H8", "closed", "Ball/needle pair with V300 on E100, floor 3. FI01"),
    "V400": ("ManualValve", "ball", 4, "F8", "closed", "Ball/needle pair with V401 on E100, floor 4. FI01"),
    "V401": ("ManualValve", "needle", 4, "F8", "closed", "Ball/needle pair with V400 on E100, floor 4. FI01"),
    "V131": ("ManualValve", "needle", 1, "L16", "closed", "Near the E101 base (PT111 at K16). FI07"),
    "V133": ("ManualValve", "ball", 1, "O15", "closed", "J101 pump area. FI02"),
    "V139a": ("ManualValve", "ball", 1, "N15", "closed", "J101a pump area (the valve list also gives O19). FI02"),
    "V139b": ("ManualValve", "ball", 1, "N16", "closed", "J101b pump area. FI02"),
    "V141a": ("ManualValve", "ball", 1, "P14", "closed", "J101a pump area. FI02"),
    "V141b": ("ManualValve", "ball", 1, "P16", "closed", "J101b pump area (tables give P16 and P17). FI02"),
    "V142a": ("ManualValve", "ball", 1, "O14", "closed", "J101a pump area. FI02"),
    "V142b": ("ManualValve", "ball", 1, "O17", "closed", "J101b pump area. FI02"),
    "NRV105a": ("CheckValve", "check", 1, "O14", None, "J101a pump area. FI02"),
    "NRV105b": ("CheckValve", "check", 1, "O16", None, "J101b pump area. FI02"),
    "V137a": ("ManualValve", None, 1, "O19", None, "Bottom right, near the make-up water and N2 lines. FI03"),
    "V137b": ("ManualValve", None, 1, "O19", None, "Bottom right, near the make-up water and N2 lines. FI03"),
    "V166": ("ManualValve", None, 1, "O18", None, "Near J104 and NRV104. FI03"),
    "V180": ("ManualValve", None, 1, "O19", None, "Bottom right (make-up water to K101?). FI03"),
    "V181": ("ManualValve", None, 1, "P19", None, "Bottom right (make-up water to K101?). FI03"),
    "V182a": ("ManualValve", None, 1, "Q19", None, "Bottom right (make-up water to K101?). FI03"),
    "V182b": ("ManualValve", None, 1, "Q19", None, "Bottom right (make-up water to K101?). FI03"),
    "V183": ("ManualValve", None, 1, "P19", None, "Bottom right (make-up water to K101?). FI03"),
    "NRV100a": ("CheckValve", "check", 1, "Q19", None, "Bottom right (make-up water to K101?). FI03"),
    "NRV100b": ("CheckValve", "check", 1, "Q19", None, "Bottom right (make-up water to K101?). FI03"),
    "NRV109": ("CheckValve", "check", 1, "P21", None, "Next to PCV117 on the N2 header; HAZOP 2.5: NRVs on all branches off the PCV117 delivery line. FI04"),
    "V190": ("ManualValve", "ball", 1, "K22", None, "Locked vent valve on the CO2 supply (vent start-up table: opened); matches HAZOP 1.1 'vent valve added'. FI04"),
    "NRV106": ("CheckValve", "check", 1, "M8", None, "Near V112 at the E100 sump outlet. FI07"),
    "PCV104": ("PressureControlValve", "pressure control", 1, "N17", None, "Near J102 and C106. FI07"),
    "RV105": ("ReliefValve", "relief", 1, "K19", "closed", "Next to PCV119 (CO2 return / J103 area). FI07"),
    "RV301": ("ReliefValve", "relief", 3, "G8", "closed", "Near the J300 reflux pump area (G8 to G10). FI07"),
    "SDV169": ("ShutdownValve", "shutdown (solenoid-operated)", 1, "P18", None, "REPORT tag SOV169. FI06"),
    "SDV421": ("ShutdownValve", "shutdown (solenoid-operated)", 4, "C10", None, "REPORT tag SOV421; opened in the vent stream start-up (Fig F.3), closed in the valve list. FI06"),
    "SDV424": ("ShutdownValve", "shutdown (solenoid-operated)", 4, "D16", "closed", "REPORT tag SOV424 (D15 in the valve list, D16 in the start-up table), near PT403. FI06"),
}
ITEMS = {}
for tag, (cls, vtype, floor, grid, pos, note) in V.items():
    report_tag = tag.replace("SDV", "SOV")
    ITEMS[tag] = dict(cls=cls, valve=vtype, floor=floor, grid=grid, pos=pos, note=note,
                      cite=[("PID", f"grid {grid}"), ("REPORT", VALVES + f" ({report_tag}, {grid}, floor {floor})")])

# tag: (class, measured variable, sensor, signal, grid, floor, monitors, extra citation or None)
DERIVED = "DERIVED"
I = {
    "LI108": ("LevelInstrument", "E101 level indication (local, loop 108 with LT108)", None, None, "K15", 1, "E101", (DERIVED, "same loop number as LT108 on E101")),
    "PT115a": ("PressureInstrument", "J101a discharge pressure", "gauge pressure transmitter", "Fieldbus", "N14", 1, "J101a", (DERIVED, "pair of PT115b on J101b")),
    "TT110a": ("TemperatureInstrument", "J101a temperature", "PRT", "Fieldbus", "N15", 1, "J101a", (DERIVED, "same grid as J101a (N15), suffix a")),
    "TT110b": ("TemperatureInstrument", "J101b temperature", "PRT", "Fieldbus", "N16", 1, "J101b", (DERIVED, "same grid as J101b (N16), suffix b")),
    "PI401": ("PressureInstrument", "pressure indication (local, loop 401 with PT401)", None, None, "C8", 4, "E100", (DERIVED, "same loop number as PT401")),
    "PI106": ("PressureInstrument", "CO2 supply pressure indication (local)", None, None, "K22", 1, "CO2_SUPPLY", (DERIVED, "same grid as PCV116 on the CO2 supply (K22)")),
    "PI107": ("PressureInstrument", "CO2 supply pressure indication (local)", None, None, "K22", 1, "CO2_SUPPLY", (DERIVED, "same grid as PCV116 on the CO2 supply (K22)")),
    "PI108": ("PressureInstrument", "N2 supply pressure indication (local)", None, None, "N22", 1, "N2_SUPPLY", (DERIVED, "same grid as PCV115 on the N2 supply (N22)")),
    "PI109": ("PressureInstrument", "N2 supply pressure indication (local)", None, None, "N22", 1, "N2_SUPPLY", (DERIVED, "same grid as PCV115 on the N2 supply (N22)")),
    "PI114": ("PressureInstrument", "N2 header pressure indication (local)", None, None, "P21", 1, "N2_SUPPLY", (DERIVED, "same grid as PCV117 on the N2 header (P21)")),
    "AT100": ("Instrument", "inline pH (position to trace, FI07)", "inline pH transmitter", "Profibus-DP", "N10", 1, None, None),
    "TT102": ("TemperatureInstrument", "temperature near the E100 base (position to trace, FI05)", "PRT", "Profibus-PA", "K7", 1, None, None),
    "TT108": ("TemperatureInstrument", "temperature near the E101 base (position to trace, FI05)", "PRT", "Fieldbus", "L15", 1, None, None),
    "TT120": ("TemperatureInstrument", "temperature near K101 / J104 (position to trace, FI05)", "PRT", "4-20mA", "M18", 1, None, None),
    "TT211": ("TemperatureInstrument", "temperature near C200 (position to trace, FI05)", "K-type thermocouple", "Fieldbus", "J14", 2, None, None),
    "TT214": ("TemperatureInstrument", "temperature near C200 cooling water (position to trace, FI05)", "PRT", "Fieldbus", "H13", 2, None, None),
    "TT215": ("TemperatureInstrument", "temperature near C200 (position to trace, FI05)", "K-type thermocouple", "Fieldbus", "J13", 2, None, None),
    "TT216": ("TemperatureInstrument", "temperature near C200 (position to trace, FI05)", "PRT", "Fieldbus", "J13", 2, None, None),
    "TT217": ("TemperatureInstrument", "temperature near E100, floor 2 (position to trace, FI05)", "K-type thermocouple", "Fieldbus", "H7", 2, None, None),
    "TT402": ("TemperatureInstrument", "temperature on the E100 overhead, floor 4 (position to trace, FI05)", "PRT", "Profibus-PA", "C7", 4, None, None),
    "TT403": ("TemperatureInstrument", "temperature near C400 cooling water (position to trace, FI05)", "PRT", "4-20mA", "C11", 4, None, None),
    "TT404": ("TemperatureInstrument", "temperature near C400 (position to trace, FI05)", "PRT", "4-20mA", "D9", 4, None, None),
}
INSTRUMENTS = {}
for tag, (cls, var, sensor, signal, grid, floor, mon, extra) in I.items():
    cits = [("PID", f"grid {grid}"), ("REPORT", INSTR + f" ({tag}, {grid}, floor {floor})")] + ([extra] if extra else [])
    INSTRUMENTS[tag] = (cls, var, sensor, signal, grid, floor, mon, cits)

LOOP = []
LINKS = [("HAZOP_1_01", "concerns", "V190"), ("RV301", "protects", "J300")]
KNOWN_TAGS = ["E100", "E101", "J101a", "J101b", "J300"]

OPEN_ITEMS = {
    "FI01": ("E100 ball/needle pairs V200/V201, V202/V203 (floor 2), V300/V301 (floor 3), V400/V401 (floor 4), and V107/V108 at the base: sample or drain points?",
             ["V200", "V300", "V400", "V107"], "Trace on the P&ID"),
    "FI02": ("J101 pump-area valves V133, V139a/b, V141a/b, V142a/b and NRV105a/b: positions on the suction, discharge or drain lines", ["V133", "V141a", "NRV105a"],
             "Trace on the P&ID"),
    "FI03": ("Bottom-right valves V137a/b, V166, V180 to V183 and NRV100a/b: make-up water to K101, or the N2 line?", ["V180", "NRV100a", "V166"], "Trace on the P&ID"),
    "FI04": ("Supply-side items PI106/PI107 (CO2), PI108/PI109/PI114 and NRV109 (N2), V190 (CO2 vent): exact positions", ["V190", "NRV109"], "Trace on the P&ID"),
    "FI05": ("Temperature transmitters not yet placed on a line: TT102, TT108, TT120, TT211, TT214 to TT217, TT402 to TT404", ["TT102", "TT214", "TT402"],
             "Trace on the P&ID"),
    "FI06": ("Shutdown valves SDV169 (P18), SDV421 (C10, in the vent start-up table) and SDV424 (D16): what they isolate", ["SDV169", "SDV421", "SDV424"],
             "Trace on the P&ID"),
    "FI07": ("AT100 (inline pH, N10), PCV104 (N17), RV105 (K19), RV301 (G8), NRV106 (M8) and V131 (L16): positions and roles", ["AT100", "PCV104", "RV105"],
             "Trace on the P&ID"),
}