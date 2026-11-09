"""
Piece 13: the causal layer (Pilot Plant 2514), for the KG A+ improvements.

Adds what the rest of the KG cannot say: how one process variable affects another.
- ProcessVariable nodes: E100 pressure, lean MEA temperature into E101, K401 condensate level, ... each linked to the
  instruments that indicate it, the controllers that regulate it, and its safeguards (alarms, trips, relief, responses)
- ProcessEvent nodes: PCV119 fails closed, C400 cooling water lost, J103 stops, ...
- CausalLink nodes: cause > (raises | lowers) > effect, with the mechanism and its basis, each cited:
  HAZOP rows (cause and consequence), the report's control descriptions (D.4), or a stated physical rule.
Direct 'raises' / 'lowers' edges are added as well, so 'what could raise E100 pressure?' is a graph walk:
  SELECT ?c WHERE { ?c (ccpp:raises|ccpp:lowers)+ ccpp:V_E100_P }
Requires piece 12 (alarm responses and the E100 PSH) to be built first.
"""
PHYS = ("DERIVED", "physical rule (stated in the mechanism); not stated in a source document")

# id: (label, kind, equipment, instruments that indicate it, controllers that regulate it, safeguards)
VARS = {
    "V_E100_P": ("E100 (stripper) pressure, read by PT401 and PT402", "pressure", "E100", ["PT401", "PT402"], ["PIC401", "PIC402"], ["limit_PSH_E100_2barg", "ARP_E100_PSH", "RV401"]),
    "V_E100_T": ("E100 boil-up temperature (MEA returning from H100), read by TT100", "temperature", "E100", ["TT100"], ["TIC100"], []),
    "V_E100_L": ("E100 base level, read by LT101", "level", "E100", ["LT101"], [], ["ARP_LT101_L", "ARP_LT101_H", "limit_LZAH100", "limit_LZAL102"]),
    "V_E100_CO2_RELEASE": ("CO2 released from the MEA in E100 (stripping efficiency)", "rate", "E100", [], [], []),
    "V_STEAM": ("Steam flow to H100, read by FT100 and FT101", "flow", "H100", ["FT100", "FT101"], ["FIC100"], ["limit_H100_steam_limit"]),
    "V_H200_DUTY": ("Electric heater duty, H200a and H200b", "duty", "H200a", [], ["TIC213a", "TIC213b"], ["ARP_H200_HH"]),
    "V_RICH_T": ("Rich MEA temperature into E100, read by TT213", "temperature", "E100", ["TT213"], ["TIC213a", "TIC213b"], ["ARP_H200_HH"]),
    "V_RICH_FLOW": ("Rich MEA flow from E101 to E100 (J101a/J101b), read by FT108", "flow", "J101a", ["FT108"], ["LIC108"], []),
    "V_LEAN_FLOW": ("Lean MEA flow from E100 to E101 (J100), read by FT103", "flow", "J100", ["FT103"], [], []),
    "V_C200_IN_T": ("Lean MEA temperature into C200 (after C100)", "temperature", "C200", [], [], []),
    "V_LEAN_T": ("Lean MEA temperature into E101 (after C200), read by TT210", "temperature", "C200", ["TT210"], ["TIC210"], []),
    "V_C200_CW": ("Cooling water flow to C200, read by FT201", "flow", "C200", ["FT201"], ["FIC201"], []),
    "V_E101_L": ("E101 base level, read by LT108", "level", "E101", ["LT108"], ["LIC108"], ["ARP_LT108_L", "ARP_LT108_H"]),
    "V_E101_P": ("E101 (absorber) pressure, read by PT403", "pressure", "E101", ["PT403"], ["PIC403"], ["RV400", "limit_PSH_E101"]),
    "V_E101_CO2_OUT": ("CO2 left in the gas leaving E101 (capture performance), read by AT400", "composition", "E101", ["AT400"], [], []),
    "V_E101_GAS": ("N2 gas flow up E101 (N2 return), read by FT303 and FT304", "flow", "E101", ["FT303", "FT304"], ["FIC303", "FIC304"], ["limit_FAL_N2_return"]),
    "V_C400_CW": ("Cooling water flow to C400, read by FT402", "flow", "C400", ["FT402"], ["FIC402"], ["limit_FAL_FT402"]),
    "V_C400_T": ("Gas temperature leaving C400, read by TT410", "temperature", "C400", ["TT410"], ["TIC410"], ["limit_TAH_C400_carryover"]),
    "V_K401_DP": ("Pressure drop across the K401 demister (PT401 to PT402)", "pressure difference", "K401", ["PT401", "PT402"], [], ["limit_PDAH_K401_demister"]),
    "V_K401_L": ("Condensate level in K401 / C400, read by LT401", "level", "K401", ["LT401"], ["LIC401"], ["ARP_LT401_L", "ARP_LT401_H"]),
    "V_CO2_RET": ("CO2 return flow to J103, read by FT301 and FT302", "flow", "J103", ["FT301", "FT302"], [], ["limit_FAL_CO2_return", "limit_TRIP_J103_starved"]),
    "V_J103_CARRY": ("Vapour or liquid carry-over to the J103 compressor", "carry-over", "J103", [], [], ["limit_TAH_C400_carryover", "limit_LAH_K103"]),
    "V_CO2_FEED": ("Fresh CO2 feed flow, read by FT105", "flow", "FCV105", ["FT105"], ["FIC105"], []),
    "V_K101_T": ("K101 saturator temperature, read by TT121", "temperature", "K101", ["TT121"], ["TIC121"], []),
    "V_C106_CW": ("Cooling water flow to C106, read by FT106", "flow", "C106", ["FT106"], ["FIC106"], []),
    "V_FEED_SAT": ("Water saturation of the gas fed to E101", "saturation", "K101", [], [], []),
    "V_Z102_DP": ("Pressure drop across the Z102 filter, read by PDT105", "pressure difference", "Z102", ["PDT105"], [], []),
    "V_J100_CAV": ("J100 cavitation and starvation risk", "risk", "J100", [], [], ["ENV_J100", "limit_LZAL102"]),
    "V_K402_CARRY": ("Liquid carry-over from E101 into K402 and towards J102", "carry-over", "K402", [], [], []),
}

# id: (label, equipment)
EVENTS = {
    "X_PCV119_CLOSED": ("PCV119 fails closed or cannot open", "PCV119"),
    "X_STEAM_EXCESS": ("Excessive steam admission (FCV110 too far open)", "FCV110"),
    "X_STEAM_FAIL": ("Steam supply failure", "STEAM_SUPPLY"),
    "X_C400_CW_LOST": ("Cooling water to C400 lost (C400 not working)", "C400"),
    "X_C200_CW_LOST": ("Coolant to C200 fails", "C200"),
    "X_K401_BLOCKED": ("K401 demister blocked", "K401"),
    "X_J103_STOPS": ("J103 compressor stops", "J103"),
    "X_PCV300_CLOSED": ("PCV300 fails closed or cannot open", "PCV300"),
    "X_GAS_FEED_HIGH": ("High gas rate up E101 from the CO2 and N2 feed", "K101"),
    "X_J102_STOPS": ("J102 blower stops", "J102"),
    "X_FCV111_OPENS": ("FCV111 opens further (more N2 recycled from K101 to K102)", "FCV111"),
    "X_J100_FAST": ("J100 running faster than J101 (or at overspeed)", "J100"),
    "X_J101_STOPS": ("J101a/J101b stops, or the E101 liquid outlet is interrupted", "J101a"),
    "X_Z102_BLOCKED": ("Z102 filter blocked (MEA degradation products)", "Z102"),
    "X_FCV105_STUCK": ("FCV105 jammed open", "FCV105"),
    "X_J104_STOPS": ("J104 stops (K101 water not circulating)", "J104"),
    "X_C100_NO_XFLOW": ("No rich MEA crossflow through C100", "C100"),
}

def H(el, item, what=""): return ("HAZOP", f"element {el}, item {item}" + (f" ({what})" if what else ""))
def R(where): return ("REPORT", where)

# (cause, raises|lowers, effect, mechanism, basis, citations)
CAUSAL = [
    ("X_PCV119_CLOSED", "raises", "V_E100_P", "PCV119 holds the E100 pressure by recycling CO2 round K103; if it cannot open, pressure rises", "control loop",
     [R("section D.4, stripper pressure control (PIC401/PIC402 on PCV119)"), H(11, 8, "failure of pressure control system")]),
    ("X_STEAM_EXCESS", "raises", "V_STEAM", "a wider FCV110 opening admits more steam", "control loop", [R("section D.4.4.c (FIC100 modulates FCV110)")]),
    ("X_STEAM_FAIL", "lowers", "V_STEAM", "no steam reaches H100; the plant shuts down on steam failure", "HAZOP", [H(13, 3, "supply failure; plant shutdown on failure")]),
    ("V_STEAM", "raises", "V_E100_T", "more steam to H100 heats and boils more MEA", "control loop", [R("section D.4.4.c (TIC100 > FIC100 > FCV110)"), H(13, 8, "low steam pressure: reduced heat transfer in H100")]),
    ("V_E100_T", "raises", "V_E100_P", "more boil-up gives more vapour in the column", "HAZOP", [H(11, 3, "high rate of gas up column from H100"), H(12, 3, "excessive boiling")]),
    ("V_E100_P", "raises", "V_E100_T", "a higher column pressure raises the MEA boiling temperature", "HAZOP", [H(12, 5, "temperature higher: higher pressure in column")]),
    ("V_E100_T", "raises", "V_E100_CO2_RELEASE", "a hotter stripper releases more CO2 from the rich MEA", "HAZOP", [H(11, 16, "low temperature: efficiency of CO2 release reduced")]),
    ("V_E100_CO2_RELEASE", "lowers", "V_E101_CO2_OUT", "MEA stripped of more CO2 returns leaner and captures more in E101", "physical rule", [PHYS]),
    ("V_H200_DUTY", "raises", "V_RICH_T", "the electric heaters warm the rich MEA before E100", "control loop", [R("section D.4.4.a (TT213 with TIC213a/TIC213b on H200a/H200b)")]),
    ("V_RICH_T", "raises", "V_E100_T", "a hotter rich feed adds heat to the stripper", "physical rule", [PHYS]),
    ("V_C400_CW", "lowers", "V_C400_T", "more cooling water cools the overhead gas leaving C400", "control loop", [R("section D.4.4.e (TT410 > TIC410 > FIC402 > FCV401)")]),
    ("X_C400_CW_LOST", "lowers", "V_C400_CW", "the C400 cooling water stops", "HAZOP", [H(12, 7, "C300 (now C400) failure to function"), H(11, 11, "C300 not operating")]),
    ("V_C400_T", "raises", "V_E100_P", "less condensation in C400 leaves more vapour, raising the overhead and column pressure", "HAZOP", [H(12, 7, "pressure higher: C300 (now C400) failure to function")]),
    ("V_C400_T", "raises", "V_J103_CARRY", "hot, uncondensed vapour carries over to J103", "HAZOP", [H(6, 6, "C400 not working: vapour carry-over to J103; damage to J103")]),
    ("V_E100_T", "raises", "V_J103_CARRY", "excessive boiling sends excess vapour on to J103", "HAZOP", [H(12, 3, "excessive boiling: excess vapour carry-over to J103")]),
    ("X_K401_BLOCKED", "raises", "V_K401_DP", "a blocked demister raises the pressure drop between PT401 and PT402", "HAZOP", [H(12, 2, "PDAH between PT402 and PT401 added")]),
    ("X_K401_BLOCKED", "lowers", "V_CO2_RET", "a blocked demister stops gas reaching the compressor", "HAZOP", [H(12, 2, "no gas flow to compressor"), H(6, 1, "K401 blocked: no flow to J103")]),
    ("X_J103_STOPS", "lowers", "V_CO2_RET", "the compressor no longer draws CO2 from K401", "HAZOP", [H(6, 2, "J103 not functioning")]),
    ("V_CO2_RET", "lowers", "V_E100_P", "if gas cannot leave the overhead, the stripper pressure rises", "physical rule", [PHYS]),
    ("X_PCV300_CLOSED", "raises", "V_E101_P", "PCV300 holds the E101 pressure by venting lean gas; if it cannot open, pressure rises", "control loop",
     [R("section D.4, absorber pressure control (PIC403 on PCV300)"), H(10, 8, "failure of pressure control system")]),
    ("X_GAS_FEED_HIGH", "raises", "V_E101_P", "a high gas feed rate overpressures the lower section of E101 and K101", "HAZOP", [H(10, 3, "high rate of gas up column from CO2 and N2 feed")]),
    ("X_J102_STOPS", "lowers", "V_E101_GAS", "with the blower stopped, no N2 flows up the column", "HAZOP", [H(5, 1, "J102 failed: no N2 gas flow up column")]),
    ("X_FCV111_OPENS", "lowers", "V_E101_GAS", "more N2 is recycled from K101 back to K102 instead of entering E101", "control loop", [R("section D.4, Fig D.6/D.7 (FIC304 on the K101 bypass rate)")]),
    ("V_C200_CW", "lowers", "V_LEAN_T", "more cooling water cools the lean MEA leaving C200", "control loop", [R("section D.4.4.d (TT210 > TIC210 > FIC201 > FCV200)")]),
    ("X_C200_CW_LOST", "lowers", "V_C200_CW", "the C200 cooling water stops", "HAZOP", [H(10, 7, "failure of coolant to C200"), H(7, 12, "C200 not working")]),
    ("V_LEAN_T", "raises", "V_E101_CO2_OUT", "hotter lean MEA absorbs CO2 less well", "HAZOP", [H(7, 12, "CO2 absorption inhibited"), H(10, 7, "inefficiency in CO2 removal")]),
    ("X_C100_NO_XFLOW", "raises", "V_C200_IN_T", "without rich MEA crossflow, C100 no longer cools the lean MEA", "HAZOP", [H(7, 11, "temperature (C200 inlet) higher: no crossflow through C100")]),
    ("V_C200_IN_T", "raises", "V_LEAN_T", "a hotter C200 inlet gives a hotter outlet unless C200 compensates", "physical rule", [PHYS]),
    ("V_C200_IN_T", "raises", "V_J100_CAV", "hot lean MEA at the pump suction risks cavitation", "HAZOP", [H(7, 11, "inefficient pump operation (cavitation)")]),
    ("V_LEAN_FLOW", "lowers", "V_E101_CO2_OUT", "less solvent through E101 captures less CO2", "physical rule", [PHYS]),
    ("V_CO2_FEED", "raises", "V_E101_CO2_OUT", "more CO2 fed than the solvent can absorb leaves in the outlet gas", "HAZOP", [H(1, 3, "FCV105 jammed open: wrong composition in plant")]),
    ("X_FCV105_STUCK", "raises", "V_CO2_FEED", "a jammed-open FCV105 admits too much CO2", "HAZOP", [H(1, 3, "FCV 106 (now FCV105) jammed open")]),
    ("X_J100_FAST", "raises", "V_LEAN_FLOW", "a faster J100 pumps more lean MEA", "physical rule", [PHYS]),
    ("V_LEAN_FLOW", "lowers", "V_E100_L", "J100 draws MEA out of the E100 base; LT101 falls as J100 power rises", "report", [R("Sections 2.1 and 2.5 (LT101 against J100 pump power: negative linear)")]),
    ("V_LEAN_FLOW", "raises", "V_E101_L", "lean MEA arriving faster than it leaves fills the E101 base", "HAZOP", [H(10, 12, "J100 running faster than J101: overfilling column base")]),
    ("V_RICH_FLOW", "lowers", "V_E101_L", "J101 draws rich MEA out of the E101 base", "report", [R("Appendix F.8.4.6 (raise J101 power when LT108 is high)"), H(10, 11, "interruption to liquid flow out: overfilling")]),
    ("V_RICH_FLOW", "raises", "V_E100_L", "rich MEA arriving faster than J100 removes it fills the E100 base", "HAZOP", [H(11, 13, "J101 running faster than J100: overfilling column base")]),
    ("X_J101_STOPS", "lowers", "V_RICH_FLOW", "rich MEA stops leaving E101", "HAZOP", [H(10, 11, "interruption to liquid flow out")]),
    ("X_Z102_BLOCKED", "raises", "V_Z102_DP", "a blocked filter raises the pressure drop across Z102 (intervene at 0.45 bar)", "HAZOP", [H(7, 3, "blocked filter Z102; DP alarm PDAH105"), R("Appendix E.3.6 (0.45 bar)")]),
    ("V_Z102_DP", "lowers", "V_LEAN_FLOW", "a restricted filter reduces the lean MEA flow", "HAZOP", [H(7, 3, "flow no: blocked filter Z102")]),
    ("V_E100_L", "lowers", "V_J100_CAV", "a low E100 level starves J100", "HAZOP", [H(7, 15, "level lower: starvation of J100; LZAL102"), R("Section 2.1 (pump at risk if the level falls too low)")]),
    ("V_C106_CW", "lowers", "V_K101_T", "more cooling water through C106 cools the K101 water", "control loop", [R("section D.4.4.b (TT121 > TIC121 > FIC106 > FCV102)")]),
    ("X_J104_STOPS", "lowers", "V_FEED_SAT", "without circulating water, the gas into the plant is not saturated", "HAZOP", [H(4, 1, "pump not functioning: gas into plant not saturated")]),
    ("V_E101_L", "raises", "V_K402_CARRY", "liquid accumulating in E101 can reach K402 and the J102 inlet", "HAZOP", [H(10, 1, "accumulation of liquid; liquid into inlet of blower J102"), H(10, 5, "liquid switch on K402")]),
]

ITEMS, LINKS = {}, []
for v, (label, kind, eq, ins, ctl, safe) in VARS.items():
    ITEMS[v] = dict(cls="ProcessVariable", label=label, props={"variableKind": kind},
                    cite=[("DERIVED", "process variable defined for the causal layer; the sources are on each causal link")])
    LINKS += [(v, "variableOf", eq)] + [(v, "indicatedBy", i) for i in ins] + [(v, "regulatedBy", c) for c in ctl] + [(v, "safeguardedBy", s) for s in safe]
for x, (label, eq) in EVENTS.items():
    ITEMS[x] = dict(cls="ProcessEvent", label=label, cite=[("DERIVED", "event defined for the causal layer; the sources are on each causal link")])
    LINKS.append((x, "eventOf", eq))
for n, (c, pol, e, mech, basis, cites) in enumerate(CAUSAL, 1):
    cid = f"CE_{n:02d}"
    ITEMS[cid] = dict(cls="CausalLink", label=f"{c} {pol} {e}", props={"polarity": pol, "mechanism": mech, "basis": basis}, cite=cites)
    LINKS += [(cid, "causeNode", c), (cid, "effectNode", e), (c, pol, e)]

KNOWN_TAGS = sorted({o for _, p, o in LINKS if p in ("variableOf", "indicatedBy", "regulatedBy", "safeguardedBy", "eventOf")})
LOOP = []
SECTION = dict(
    prefix="cau", loop_id="CausalLayer", mode="FigureOfEight", flow="feedsInto",
    loop_label="Causal layer (process variables, events and cause-and-effect links; no flow route)",
    loop_note="Cause-and-effect knowledge for 'what could cause...' questions: walk (raises|lowers)+ back from a process variable.",
    loop_cite=[("HAZOP", "elements 1, 4 to 7 and 10 to 13 (causes and consequences)"), R("section D.4 (control loop descriptions) and Sections 2.1 to 2.5")],
)
OPEN_ITEMS = {
    "CA01": ("Causal links marked 'physical rule' are engineering reasoning, not stated in a document: review CE_08, CE_10, CE_19, CE_28, CE_30 and CE_33", ["V_E100_P", "V_E101_CO2_OUT"],
             "Engineering review (supervisor or plant engineer)"),
    "CA02": ("Link strengths and time scales are not modelled (only the direction of each effect)", ["V_E100_P"], "Future work: dynamic model or plant data"),
}