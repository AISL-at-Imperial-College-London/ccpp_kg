"""
Piece 12: operating procedures and alarm responses (Pilot Plant 2514), for the KG A+ improvements.

Sources, each checked in the document itself (not taken from the ChatGPT answers):
- REPORT Appendix F.8.4 (Alarms, pages 117 to 118): nine alarm responses, thresholds and ordered actions
- REPORT Appendix E.3.7 and E.3.8 (commissioning SOP): LT101 below 10% / above 90%
- REPORT Section 2.2 and 2.5: LSL 5% and LSLL 1% on LT101; J100 safe operating range 1%-57% (cavitation), 1%-60% theoretical
- HAZOP note M4 (PSH on E100 triggers plant shutdown at 2 barg) and element 10, item 8 (PSH on E101)
Each response is an AlarmResponse node linked to the instrument that triggers it, its threshold (an operating limit)
and the equipment it acts on, so 'LT108 is above 85%: what should I do?' is answered from the KG with a citation.
"""
F84 = "Appendix F.8.4 (Alarms)"

SECTION = dict(
    prefix="prc", loop_id="AlarmResponseRegister", mode="FigureOfEight", flow="feedsInto",
    loop_label="Alarm responses and operating envelopes (register, no flow route)",
    loop_note="Documented operator responses to level, heater and pressure alarms, with their thresholds.",
    loop_cite=[("REPORT", F84 + ", Appendix E.3.7 to E.3.8 and Sections 2.2 to 2.5"), ("HAZOP", "note M4 and element 10, item 8")],
)

def response(label, trigger, actions, cite, note=None):
    return dict(cls="AlarmResponse", label=label, note=note,
                props={"triggerCondition": trigger, "actionText": " ".join(f"{i}. {a}" for i, a in enumerate(actions, 1))},
                cite=cite)

ITEMS = {
    "ARP_LT101_L": response("LT101 low alarm response (E100 level)", "L alarm on LT101: E100 level below 5%; LL alarm below 1%",
        ["Reduce the pump power of J100 by 10%.", "Increase the pump power of J101a or J101b (whichever is in use) by 10%, without exceeding the maximum safe pump speed.",
         "Increase the pump power of J300 by 10%.", "Check that the MEA valves are opened and closed according to table F.5.",
         "If the level still falls and the LL alarm sounds (below 1%), initiate emergency shutdown."], [("REPORT", F84 + ".1, page 117")]),
    "ARP_LT101_H": response("LT101 high alarm response (E100 level)", "H alarm on LT101: E100 level above 85%; HH alarm above 95%",
        ["Increase the pump power of J100 by 10%.", "Decrease the pump power of J101a or J101b (whichever is in use) by 10%.",
         "Check that the MEA valves are opened and closed according to table F.5.",
         "If the level still rises and the HH alarm sounds (above 95%), initiate emergency shutdown."], [("REPORT", F84 + ".2, page 118")]),
    "ARP_LT104_L": response("LT104 low alarm response (K101 level)", "L alarm on LT104: K101 level below 5%; LL alarm (value not stated)",
        ["Increase the pump power of J102 by 10%.", "Increase the pump power of J103 by 5%.", "Check the valve positions against table F.5.",
         "If the level still falls and the LL alarm sounds, initiate emergency shutdown."], [("REPORT", F84 + ".3, page 118")]),
    "ARP_LT104_H": response("LT104 high alarm response (K101 level)", "H alarm on LT104: K101 level above 85%; HH alarm (value not stated)",
        ["Decrease the pump power of J102 by 10%.", "Decrease the pump power of J103 by 5%.", "Check the valve positions against table F.5.",
         "If the level still rises and the HH alarm sounds, initiate emergency shutdown."], [("REPORT", F84 + ".4, page 118")]),
    "ARP_LT108_L": response("LT108 low alarm response (E101 level)", "L alarm on LT108: E101 level below 5%; LL alarm (value not stated)",
        ["Decrease the pump power of J101a or J101b (whichever is in use) by 10%.", "Increase the pump power of J100 by 10%.",
         "Increase the pump power of J300 by 10%.", "Check the valve positions against table F.5.",
         "If the level still falls and the LL alarm sounds, initiate emergency shutdown."], [("REPORT", F84 + ".5, page 118")]),
    "ARP_LT108_H": response("LT108 high alarm response (E101 level)", "H alarm on LT108: E101 level above 85%; HH alarm (value not stated)",
        ["Increase the pump power of J101a or J101b (whichever is in use) by 10%, without exceeding the maximum safe pump speed.",
         "Decrease the pump power of J100 by 10%.", "Decrease the pump power of J300 by 10%.", "Check the valve positions against table F.5.",
         "If the level still rises and the HH alarm sounds, initiate emergency shutdown."], [("REPORT", F84 + ".6, page 119")]),
    "ARP_LT401_L": response("LT401 low alarm response (condensate level, C400/K401)", "L alarm on LT401: condensate level below 5%; LL alarm (value not stated)",
        ["Decrease the pump power of J300 by 10%.", "If the level still falls and the LL alarm sounds, initiate emergency shutdown."],
        [("REPORT", F84 + ".7, page 119")]),
    "ARP_LT401_H": response("LT401 high alarm response (condensate level, C400/K401)", "H alarm on LT401: condensate level above 85%; HH alarm (value not stated)",
        ["Increase the pump power of J300 by 10%.", "If the level still rises and the HH alarm sounds, initiate emergency shutdown."],
        [("REPORT", F84 + ".8, page 119")]),
    "ARP_H200_HH": response("H200a/H200b heater H and HH alarm response", "H and HH alarms from the electric heaters H200a and H200b (TIC213a, TIC213b)",
        ["Check the heater set point is at the desired value.", "If not, set the heaters to manual at their controllers in the control room, or, if in automatic, correct the set point.",
         "If the heaters do not respond, turn them off at the manual switch on floor 1."], [("REPORT", F84 + ".9, page 119")]),
    "ARP_E100_PSH": response("E100 high pressure shutdown (PSH at 2 barg)", "PSH on E100: plant shutdown at 2 barg, set well below the relief valve set point",
        ["The PSH kills the steam and electrical heating (H100 and H200a/b) and triggers plant shutdown at 2 barg.",
         "Pressure control is by PIC401/PIC402 on PCV119; relief is RV401 to K403 if pressure keeps rising."],
        [("HAZOP", "note M4 ('PSH on E100 to kill steam/electrical heating long before E100 pressure reaches RV set point'; 'PSH triggers plant shutdown at 2 barg')"),
         ("HAZOP", "element 11, item 8 (PSH added on the column)")]),
    "COM_LT101_LOW": response("Commissioning: LT101 dropping below 10% (J100 test)", "Commissioning SOP: LT101 below 10% during the J100 pump test",
        ["Decrease J100 to the second-to-last steady-state value.", "If the level keeps dropping over the next 2 minutes, reduce J100 speed by a further 10% every minute until it stops.",
         "Once the level is steady above 10%, return to the last steady-state speed.", "Increase pump speed by a smaller step than last time (10% to 5% to 2% to 1%); after a 1% step, the maximum pump power has been reached."],
        [("REPORT", "Appendix E.3.7 (commissioning SOP)")], note="Applies to the J100 commissioning test, not full operation (full operation uses the F.8.4 alarms at 5% and 1%)."),
    "COM_LT101_HIGH": response("Commissioning: LT101 rising above 90% (J100 test)", "Commissioning SOP: LT101 above 90% during the J100 pump test",
        ["Increase J100 pump power by 10% every 2 minutes until LT101 is below 90%.", "If the level still does not drop, send an operator into the plant to check V110 is open.",
         "Once steady below 90%, continue the test at 5% above the last steady-state pump power."],
        [("REPORT", "Appendix E.3.8 (commissioning SOP)")], note="Applies to the J100 commissioning test, not full operation (full operation uses the F.8.4 alarms at 85% and 95%)."),
    "ENV_J100": dict(cls="OperatingEnvelope", label="J100 safe operating range (pump power)",
                     props={"envelopeText": "J100 safe operating range: 1%-57% pump power, accounting for cavitation (audible vibration at 55%-60%); "
                                            "theoretical range 1%-60%. The lower limit 1% is the weakest pump setting that still lifts MEA to the top of E100."},
                     note="The upper limit keeps LT101 above about 10%, clear of the LSL (5%) and LSLL (1%) switches.",
                     cite=[("REPORT", "Sections 2.2 to 2.5 (J100 commissioning study)")]),
}

LIMITS = {
    "F84_LT101_L": ("LT101", "level", "alarm", 5.0, None, "%", [("REPORT", F84 + ".1; Section 2.2 (LSL at 5%)")]),
    "F84_LT101_LL": ("LT101", "level", "trip", 1.0, None, "%", [("REPORT", F84 + ".1.5; Section 2.2 (LSLL emergency shutdown at 1%)")]),
    "F84_LT101_H": ("LT101", "level", "alarm", None, 85.0, "%", [("REPORT", F84 + ".2")]),
    "F84_LT101_HH": ("LT101", "level", "trip", None, 95.0, "%", [("REPORT", F84 + ".2.4")]),
    "F84_LT104_L": ("LT104", "level", "alarm", 5.0, None, "%", [("REPORT", F84 + ".3")]),
    "F84_LT104_H": ("LT104", "level", "alarm", None, 85.0, "%", [("REPORT", F84 + ".4")]),
    "F84_LT108_L": ("LT108", "level", "alarm", 5.0, None, "%", [("REPORT", F84 + ".5")]),
    "F84_LT108_H": ("LT108", "level", "alarm", None, 85.0, "%", [("REPORT", F84 + ".6")]),
    "F84_LT401_L": ("LT401", "level", "alarm", 5.0, None, "%", [("REPORT", F84 + ".7")]),
    "F84_LT401_H": ("LT401", "level", "alarm", None, 85.0, "%", [("REPORT", F84 + ".8")]),
    "COM_LT101_10": ("LT101", "level", "operating", 10.0, 90.0, "%", [("REPORT", "Appendix E.3.7 and E.3.8 (commissioning SOP limits)")]),
    "J100_range_cavitation": ("J100", "pump power", "range", 1.0, 57.0, "%", [("REPORT", "Section 2.5 (range accounting for cavitation)")]),
    "J100_range_theoretical": ("J100", "pump power", "range", 1.0, 60.0, "%", [("REPORT", "Section 2.5 (theoretical range)")]),
    "PSH_E100_2barg": ("E100", "pressure", "trip", None, 2.0, "barg", [("HAZOP", "note M4 (PSH triggers plant shutdown at 2 barg)")]),
    "PSH_E101": ("E101", "pressure", "trip", None, None, "barg", [("HAZOP", "element 10, item 8 (put a PSH onto the column; action completed)")]),
}

RESP_LINKS = {   # response: (triggering instrument, thresholds it answers, equipment it acts on)
    "ARP_LT101_L": ("LT101", ["F84_LT101_L", "F84_LT101_LL"], ["J100", "J101a", "J101b", "J300"]),
    "ARP_LT101_H": ("LT101", ["F84_LT101_H", "F84_LT101_HH"], ["J100", "J101a", "J101b"]),
    "ARP_LT104_L": ("LT104", ["F84_LT104_L"], ["J102", "J103"]),
    "ARP_LT104_H": ("LT104", ["F84_LT104_H"], ["J102", "J103"]),
    "ARP_LT108_L": ("LT108", ["F84_LT108_L"], ["J101a", "J101b", "J100", "J300"]),
    "ARP_LT108_H": ("LT108", ["F84_LT108_H"], ["J101a", "J101b", "J100", "J300"]),
    "ARP_LT401_L": ("LT401", ["F84_LT401_L"], ["J300"]),
    "ARP_LT401_H": ("LT401", ["F84_LT401_H"], ["J300"]),
    "ARP_H200_HH": ("TIC213a", [], ["H200a", "H200b"]),
    "ARP_E100_PSH": ("E100", ["PSH_E100_2barg"], ["H100", "H200a", "H200b"]),
    "COM_LT101_LOW": ("LT101", ["COM_LT101_10"], ["J100"]),
    "COM_LT101_HIGH": ("LT101", ["COM_LT101_10"], ["J100", "V110"]),
}
LINKS = ([(r, "triggeredBy", ins) for r, (ins, _, _) in RESP_LINKS.items()]
         + [(r, "respondsTo", f"limit_{l}") for r, (_, lims, _) in RESP_LINKS.items() for l in lims]
         + [(r, "actsOn", e) for r, (_, _, eqs) in RESP_LINKS.items() for e in eqs]
         + [("ARP_H200_HH", "triggeredBy", "TIC213b"), ("ENV_J100", "envelopeOf", "J100"),
            ("LT401", "monitors", "C400")])          # the report also calls LT401 the condenser (C400) level (D.4.2.b)
KNOWN_TAGS = ["LT101", "LT104", "LT108", "LT401", "J100", "J101a", "J101b", "J102", "J103", "J300", "H100", "H200a", "H200b",
              "TIC213a", "TIC213b", "E100", "E101", "C400", "V110"]

LOOP = []

OPEN_ITEMS = {
    "PR01": ("F.8.4 gives the LL and HH alarm percentages only for LT101 (1% and 95%); the LL/HH values for LT104, LT108 and LT401 are not stated",
             ["LT104", "LT108", "LT401"], "Alarm list from the control system (requested from Colin Hale)"),
    "PR02": ("REPORT Section 2.2 defines the maximum safe pump power as the power that 'produces an LT101 reading below 10%'; "
             "the method in Sections 2.3 to 2.5 means the highest power that keeps LT101 above 10%", ["J100", "ENV_J100"], "Note for the report"),
}