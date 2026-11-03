"""
Piece 11: vents, the N2 purge/blanket header and make-up water (Pilot Plant 2514). Completes the lines of the P&ID.

Vents: REPORT Fig F.3 lists the valves on the vent stream (PCV119, V190, V197, V209, PCV300, V315, SOV421, V409, V411);
       on the P&ID the vent lines end at 'VENT VV' / 'VENT VI' arrows to drawing 108712-10-002.
N2 header: from the PCV117 delivery line (HAZOP 2.5: NRVs on all branches), along the bottom of the drawing (report colour
       P&ID, orange) to the MEA tanks, entering F100 via NRV107 and R100 via NRV108 (team trace); HAZOP M15.
Make-up water: building supply > NRV100a/b > deionising cartridge (HAZOP 4.8: 'd/s of NRVs') > K101.
Most routes are inferred from the tables, the HAZOP and the report's colour P&ID: to be traced.
"""
TO_TRACE = "connection inferred from the documents; to be traced on the P&ID"
VENT_TABLE = "Fig F.3 (vent stream start-up valve positions)"

SECTION = dict(
    prefix="vnt", loop_id="N2HeaderRoute", mode="FigureOfEight", flow="feedsInto",
    loop_label="N2 purge / blanket header (PCV117 > NRV109 > header > MEA tanks)",
    loop_note="Branch off the N2 supply after PCV117 that runs along the bottom of the drawing and blankets the MEA tanks.",
    loop_cite=[("HAZOP", "element 2, item 5 (NRVs on all branches off the PCV117 delivery line) and note M15 (N2 purging)"),
               ("REPORT", "colour-coded P&ID (Pilot Plant 2406): orange N2 line along the bottom to the tanks"),
               ("TEAM", "the line enters F100 via NRV107 and R100 via NRV108"), ("DERIVED", TO_TRACE)],
)

ITEMS = {
    "VENT_SYSTEM": dict(cls="VentConnection", label="Plant vent system ('VENT VV' / 'VENT VI' to drawing 108712-10-002)", floor=1,
                        note="Untagged destination of the vent lines. Fig F.3 lists the valves on the vent stream (VN01); what 'VV' and 'VI' mean is VN04.",
                        cite=[("PID", "'VENT VV' and 'VENT VI' arrows to drawing 108712-10-002"), ("REPORT", VENT_TABLE)]),
    "N2_PURGE_HEADER": dict(cls="PipeSegment", label="N2 purge / blanket header (long line along the bottom of the drawing)", floor=1,
                            note="Untagged. Fed from the PCV117 delivery line through NRV109; blankets the MEA tanks (VN05).",
                            cite=[("REPORT", "colour-coded P&ID (orange N2 line along the bottom)"), ("HAZOP", "element 2, item 5 and note M15"), ("DERIVED", TO_TRACE)]),
    "MAKEUP_WATER_SUPPLY": dict(cls="SupplyConnection", label="Make-up water from the building supply (battery limit)", floor=1, grid="Q18",
                                note="Untagged supply of make-up water to K101 (VN06).",
                                cite=[("PID", "'MAKE UP WATER FROM BLDG SUPPLY (BATTERY LIMIT)', bottom right"), ("HAZOP", "element 4, item 8")]),
    "DI_CARTRIDGE": dict(cls="Filter", label="Deionising cartridge on the make-up water inlet", floor=1,
                         note="Added after HAZOP 4.8 ('hard water?'): downstream of the NRVs on the make-up water inlet. Tag not documented (VN06).",
                         cite=[("HAZOP", "element 4, item 8 ('Deionising cartridge on make-up water inlet d/s of NRVs'; action taken: added)")]),
}

LOOP = [
    ("N2_SUPPLY", "inline"), ("V127", "inline"), ("PCV117", "inline"),
    ("NRV109", "inline"), ("PI114", "tie-in"),
    ("N2_PURGE_HEADER", "inline"),
    (("NRV107", "inline"), ("NRV108", "inline")),
    (("F100", "inline"), ("R100", "inline")),
]
TRAIN_A = ["NRV107", "F100"]
TRAIN_B = ["NRV108", "R100"]
VENT_VALVES = ["PCV119", "V190", "V197", "V209", "V315", "SDV421", "V409", "V411"]
EXTRA_PIPING = ([(v, "VENT_SYSTEM") for v in VENT_VALVES]
                + [("VENT_E101", "VENT_SYSTEM"),                                  # absorber vent after PCV300
                   ("N2_PURGE_HEADER", "NRV104"),                                 # NRV104 is on the N2 line (team trace)
                   ("MAKEUP_WATER_SUPPLY", "NRV100a"), ("NRV100a", "NRV100b"), ("NRV100b", "DI_CARTRIDGE"), ("DI_CARTRIDGE", "K101")])
LINKS = [("MAKEUP_WATER_SUPPLY", "feedsInto", "NRV100a"), ("NRV100a", "feedsInto", "NRV100b"), ("NRV100b", "feedsInto", "DI_CARTRIDGE"),
         ("DI_CARTRIDGE", "feedsInto", "K101"), ("HAZOP_4_08", "concerns", "DI_CARTRIDGE"), ("HAZOP_4_08", "concerns", "NRV100a")]
KNOWN_TAGS = ["K101", "PCV117", "NRV109", "NRV107", "NRV108", "F100", "R100"]

OPEN_ITEMS = {
    "VN01": ("Fig F.3 lists PCV119, V190, V197, V209, PCV300, V315, SDV421, V409 and V411 on the vent stream: trace each one's line to its vent outlet "
             "(V197, V209 and V411 also appear in the cooling water tables, UT07)", ["VENT_SYSTEM", "V409", "V315"], "Trace on the P&ID"),
    "VN02": ("Where the relief valves RV101, RV102, RV103, RV104, RV105, RV107, RV300 and RV301 discharge (vent, K403 or drain)", ["VENT_SYSTEM"],
             "Trace on the P&ID"),
    "VN03": ("Where K403 (relief knockout drum) drains or vents", ["K403"], "Trace on the report's colour P&ID"),
    "VN04": ("What the two vent destinations 'VENT VV' and 'VENT VI' on drawing 108712-10-002 are", ["VENT_SYSTEM"], "Drawing 108712-10-002"),
    "VN05": ("Other branches and purge points on the N2 header along the bottom of the drawing (HAZOP M15)", ["N2_PURGE_HEADER"], "Trace on the P&ID"),
    "VN06": ("Make-up water order (V180 to V183, V182a/b, NRV100a/b, deionising cartridge) between the building supply and K101", ["MAKEUP_WATER_SUPPLY", "DI_CARTRIDGE"],
             "Trace on the P&ID"),
}