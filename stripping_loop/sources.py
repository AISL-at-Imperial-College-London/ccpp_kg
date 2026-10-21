"""
Grounding layer: where every fact in the stripping loop KG comes from.

Each plant item, limit, procedure, control loop, HAZOP row and simulation
result gets one or more citations. A citation = (source document, location),
where location is a P&ID grid reference, a report figure or section, a HAZOP
item, or an Aspen block or stream.

To correct or add a reference, edit ITEM_CITATIONS below (or the "source"
text in loop_data.py, which is parsed automatically), then rebuild.
"""
import re

SOURCE_DOCS = {
    "PID": ("P&ID", "Pilot Plant 2514 P&ID (team marked-up copy)", "P&ID image, Pilot Plant 2514"),
    "PID2010": ("Original P&ID 2010", "Amine Scrubber P&ID, Strata Technology, issued for design review (2010)",
                "27794_Plant_HAZ_P_ID.PDF"),
    "DIFF": ("P&ID differences", "Differences between the P&ID and the as-built pilot plant", "P_ID_Differences.pdf"),
    "REPORT": ("Pilot Plant Report", "Pilot Plant Report, Group 6, v2.0", "PilotPlantReport_Group6_2_0.pdf"),
    "SUMMARY": ("Plant summary 2023-24", "Carbon Capture plant summary 2023-2024 v01",
                "Carbon_Capture_plant_summary_2023-2024_v01.pdf"),
    "HAZOP": ("HAZOP 2010", "HAZOP study, 6-7 May 2010", "27794_Plant_HAZREP_1.xls"),
    "ASPEN_V3": ("Aspen v3", "Aspen Plus model ABB_pilot_plant_final_3 (converged)", "ABB_pilot_plant_final_3.apwz"),
    "ASPEN_V61": ("Aspen v6.1", "Aspen Plus model ABB_pilot_plant_final_6_1_SA_validation (not converged)",
                  "ABB_pilot_plant_final_6_1_SA_validation.apwz"),
    "DERIVED": ("KG derivation", "Derived by the KG from other facts; not an approved document", "build_stripping_loop.py"),
    "TEAM": ("Team check", "Loop trace checked by the project team against the P&ID (Oct 2026)", "project notes"),
}

PREFIXES = [("P_ID_Differences.pdf", "DIFF"), ("P&ID", "PID"), ("REPORT", "REPORT"), ("SUMMARY", "SUMMARY"),
            ("HAZOP", "HAZOP"), ("DIFF", "DIFF"), ("TEAM", "TEAM"), ("DERIVED", "DERIVED")]


def parse(text):
    """'SUMMARY p.190; REPORT D.4' -> [('SUMMARY', 'p.190'), ('REPORT', 'D.4')]"""
    out = []
    for part in [p.strip() for p in (text or "").split(";") if p.strip()]:
        for prefix, key in PREFIXES:
            if part.startswith(prefix):
                loc = part[len(prefix):].strip(" ,:") or "whole document"
                out.append((key, loc))
                break
        else:
            raise ValueError(f"Unknown source prefix in '{part}'")
    return out


LINEUP = "Fig E.1/E.2 (stripping loop commissioning line-up)"
HEATER_PID = "heater control section (grids J9 to J11)"
ITEM_CITATIONS = {
    "TE105": [("PID", "grid M9 (tagged TE105)"), ("REPORT", "Appendix B lists it as TT105; Appendix D calls it TE105")],
    "E100": [("PID", "column E100, grids F7 to K8"), ("ASPEN_V3", "block E100 (RadFrac internals)")],
    "H100": [("PID", "reboiler H100, near grid L6"), ("SUMMARY", "p.102"),
             ("ASPEN_V3", "blocks H100REAC and H100HEAT")],
    "C100": [("PID", "interchanger C100, grid M8 to M9"), ("SUMMARY", "p.106"), ("REPORT", "section 3"),
             ("ASPEN_V3", "block C100")],
    "J100": [("PID", "grid M10"), ("REPORT", "section 2.5 (pump trials)")],
    "B101": [("PID", "grid M10"), ("DIFF", "row PT104 & B101 (M10)")],
    "Z102": [("PID", "grid M11"), ("REPORT", "section E.3.6 and Fig F.21")],
    "H200a": [("PID", HEATER_PID), ("REPORT", "start-up tables, heater H200a (J10, floor 2)")],
    "H200b": [("PID", HEATER_PID), ("REPORT", "start-up tables, heater H200b (J11, floor 2)")],
    "V402": [("PID", "grid F8"), ("REPORT", LINEUP), ("DIFF", "row V402 & V403 (F8)")],
    "V403": [("PID", "grid F8"), ("REPORT", LINEUP), ("DIFF", "row V402 & V403 (F8)")],
    "V120": [("PID", "grid L11"), ("REPORT", "Fig F.21 (Z102 bypass) and " + LINEUP)],
    "V117a": [("PID", "grid M11"), ("REPORT", LINEUP + " and Fig F.21")],
    "V117b": [("PID", "grid M11"), ("REPORT", LINEUP + " and Fig F.21"), ("TEAM", "order Z102 > V117b > V121")],
    "V121": [("PID", "grid M11"), ("REPORT", LINEUP), ("TEAM", "order Z102 > V117b > V121")],
    "V110": [("PID", "grid L7"), ("REPORT", LINEUP), ("TEAM", "first valve after the sump outlet")],
    "RV101": [("PID", "grid L10"), ("HAZOP", "element 7, item 14")],
    "RV401": [("PID", "grid F7"), ("DIFF", "row K403 (E7)")],
    "FCV110": [("PID", "grid L5"), ("DIFF", "row FCV110 (L5)"), ("SUMMARY", "p.190 (control-loop table)"),
               ("REPORT", "Fig E.1 and section F.5.4.3")],
    "PCV119": [("SUMMARY", "p.190 (control-loop table)")],
    "PCV122": [("PID", "grid M10")],
    "V101": [("REPORT", "Fig E.1 and Fig F.23")], "V102": [("REPORT", "Fig E.1 and Fig F.23")],
    "V105": [("REPORT", "Fig E.1 and Fig F.23")], "V106": [("REPORT", "Fig E.1 and Fig F.23")],
    "V109": [("REPORT", "Fig E.1 and Fig F.23")],
    "Q105": [("PID", "line Q105, near grid M6"), ("TEAM", "reboiler circuit trace")],
    "Q106": [("PID", "line Q106, grids L6 to L7"), ("TEAM", "Q106 returns from H100 to E100")],
    "DI100": [("PID", "on FT102, grid M6"), ("TEAM", "tag is DI100, not DE100")],
    "TT100": [("PID", "on line Q106, grid L6"), ("REPORT", "Appendix B instrument list"),
              ("TEAM", "TT100 confirmed on Q106")],
    "TT106": [("PID", "grid L10"), ("REPORT", "Appendix B instrument list"), ("TEAM", "TT106 confirmed at J100")],
    "TT303": [("PID", "column E100, grid G7 (tag hidden under marker 6)"), ("REPORT", "Appendix B instrument list")],
    "TT201": [("PID", "column E100, grid J7 (tag hidden under marker 7)"), ("REPORT", "Appendix B instrument list")],
    "SIC100": [("SUMMARY", "p.190 (control-loop table)"), ("PID2010", "J100 controls")],
    "HS100": [("PID2010", "J100 controls")],
    "FIC103": [("SUMMARY", "p.190 (control-loop table)"), ("PID", "grid M10")],
    "FIC104": [("SUMMARY", "p.190 (control-loop table)")],
    "TIC100": [("SUMMARY", "p.190 (control-loop table)")],
    "FIC100": [("SUMMARY", "p.190 (control-loop table)")],
    "PIC401": [("SUMMARY", "p.190 (control-loop table)")],
    "PIC402": [("SUMMARY", "p.190 (control-loop table)")],
}
for t in ["TIC213a", "TIC213b", "TY213a", "TY213b", "HS200a", "HS200b", "TZAHH212a", "TZAHH212b",
          "TSHH212a", "TSHH212b", "TZH213", "TI213"]:
    ITEM_CITATIONS.setdefault(t, [("PID", HEATER_PID)])
for t in ["TIC213a", "TIC213b"]:
    ITEM_CITATIONS[t] = ITEM_CITATIONS[t] + [("SUMMARY", "p.190 (control-loop table)")]

# Team checks against the full-size P&ID (Oct 2026)
J100_CHAIN = "J100 motor M > SIC100 > HS100 > FIC103"
ORDER_J100 = "order TT106 > B101 > PT104 > PCV122 > V116 confirmed"
ITEM_CITATIONS.update({
    "PT103": [("PID", "grid M8, on the lean line near TT104 before C100"), ("REPORT", "Appendix B instrument list"),
              ("TEAM", "on the lean line from the E100 sump, near TT104, entering C100")],
    "TT104": [("PID", "grid M8"), ("REPORT", "Appendix B instrument list"), ("TEAM", "next to PT103 on the lean line entering C100")],
    "SIC100": [("PID", "below J100, grid M10"), ("SUMMARY", "p.190 (control-loop table)"), ("PID2010", "J100 controls"), ("TEAM", J100_CHAIN)],
    "HS100": [("PID", "below J100, grid M10"), ("PID2010", "J100 controls"), ("TEAM", J100_CHAIN)],
    "FIC103": [("PID", "below J100, grid M10"), ("SUMMARY", "p.190 (control-loop table)"), ("TEAM", J100_CHAIN)],
    "B101": [("PID", "grid M10"), ("DIFF", "row PT104 & B101 (M10)"), ("TEAM", ORDER_J100)],
    "PT104": [("PID", "grid L10"), ("REPORT", "Appendix B instrument list"), ("DIFF", "row PT104 & B101 (M10)"), ("TEAM", ORDER_J100)],
    "PCV122": [("PID", "grid M10, after B101, set to 8 bar"), ("TEAM", ORDER_J100)],
    "FT103": [("PID", "grid L12"), ("REPORT", "Appendix B instrument list"), ("TEAM", "flow V121 > FT103 > FT104")],
    "FT104": [("PID", "grid L12"), ("REPORT", "Appendix B instrument list"), ("TEAM", "flow V121 > FT103 > FT104")],
    "SDV125": [("PID", "grid L11, tagged SDV125"), ("REPORT", LINEUP + " (listed as SOV125)"), ("TEAM", "tag is SDV125 on the P&ID")],
    "SDV123": [("PID", "grid L9, tagged SDV123"), ("REPORT", LINEUP + " (listed as SOV123)")],
    "V110": [("PID", "grid L7"), ("REPORT", LINEUP), ("TEAM", "first valve after the sump outlet; ball valve per valve schedule")],
    "V112": [("PID", "grid M8"), ("REPORT", LINEUP), ("TEAM", "check valve per valve schedule")],
    "V113a": [("PID", "grid M9"), ("REPORT", LINEUP), ("TEAM", "check valve per valve schedule")],
    "V113b": [("PID", "grid M10"), ("REPORT", LINEUP), ("TEAM", "ball valve per valve schedule")],
    "V315": [("PID", "grid G10"), ("REPORT", LINEUP), ("TEAM", "grid confirmed")],
    "V316": [("PID", "grid G10"), ("REPORT", LINEUP), ("TEAM", "grid confirmed")],
    "TT103": [("PID", "grid J7, left-hand side of E100"), ("REPORT", "Appendix B instrument list"), ("TEAM", "left-hand side of E100")],
    "PSHH116": [("PID", "E100 base, right-hand side"), ("TEAM", "right-hand side of E100")],
    "PT102": [("PID", "grid K8, E100 sump, left-hand side"), ("REPORT", "Appendix B instrument list"), ("TEAM", "left-hand side of E100 sump")],
    "LT101": [("PID", "grid K8, E100 sump, left-hand side"), ("REPORT", "Appendix B instrument list"), ("TEAM", "left-hand side of E100 sump")],
    "LSHH100": [("PID", "E100 sump, left-hand side"), ("TEAM", "left-hand side of E100 sump")],
    "LSLL102": [("PID", "E100 sump, left-hand side"), ("TEAM", "left-hand side of E100 sump")],
})
for _tag, _grid, _phase in [("TT401", "F7", "vapour"), ("TT400", "F7", "liquid"), ("TT302", "G7", "liquid"),
                            ("TT301", "G7", "vapour"), ("TT300", "G7", "liquid"), ("TT203", "H7", "vapour"),
                            ("TT202", "H7", "liquid"), ("TT200", "J7", "liquid")]:
    ITEM_CITATIONS[_tag] = [("PID", f"grid {_grid}"), ("REPORT", "Appendix B instrument list"),
                            ("TEAM", f"{_phase} measurement confirmed on full-size P&ID")]

NOZZLE_CITATIONS = {
    "E100_N_drawoff": [("PID", "E100 nozzle below TT103, grid J7"), ("TEAM", "loop starts at this nozzle"),
                       ("ASPEN_V3", "E100 side draw from stage 11 (stream S14)")],
    "E100_N_reboiler_return": [("PID", "E100 sump, grid K7"), ("TEAM", "Q106 returns here"),
                               ("ASPEN_V3", "H100 return to stage 12 (stream S24)")],
    "E100_N_sump_outlet": [("PID", "E100 sump outlet to V110, grid K7"), ("REPORT", LINEUP)],
    "E100_N_top_inlet": [("PID", "E100 top, after V402, grid F8"), ("TEAM", "flow re-enters E100 after V402"),
                         ("ASPEN_V3", "E100 feed to stage 1 (stream S10)")],
}

INTERLOCK_CITATIONS = {
    "IL_H200a_HH": [("PID", HEATER_PID)],
    "IL_H200b_HH": [("PID", HEATER_PID)],
    "IL_heater_outlet_H": [("PID", HEATER_PID)],
    "IL_E100_level_LL": [("REPORT", "section 2.2"), ("HAZOP", "element 7, item 15; element 11, item 15")],
    "IL_E100_level_HH": [("HAZOP", "element 11, item 12")],
}


def citations_for(tag, kind, D):
    """Return the citation list for a tagged item, with defaults where not listed explicitly."""
    if tag in ITEM_CITATIONS:
        return ITEM_CITATIONS[tag]
    if kind == "valve":
        cls, vt, floor, grid, pos, note = D.VALVES[tag]
        out = [("PID", f"grid {grid}")] if grid else []
        if tag in set(D.LINEUP_OPEN) | set(D.LINEUP_CLOSED):
            out.append(("REPORT", LINEUP))
        return out
    if kind == "instrument":
        cls, var, stype, sig, grid, floor, mon, stg, ph = D.INSTRUMENTS[tag]
        out = [("PID", f"grid {grid}" if grid else f"on {mon}" if mon else "loop instrument")]
        if stype:
            out.append(("REPORT", "Appendix B instrument list"))
        return out
    if kind == "pipe":
        return [("PID", f"line {tag}")]
    if kind == "controller":
        return [("PID", "controls for " + str(D.CONTROLLERS[tag][0]))]
    return []


# Side return items (added Oct 2026)
ITEM_CITATIONS.update({
    "V309": [("PID", "grid H10, branch from the heater return line to the E100 side inlet"),
             ("REPORT", "Fig E.1 (closed in the commissioning line-up) and Fig F.7 (grid G10)"),
             ("TEAM", "side return to E100 between V318 and V302")],
    "V318": [("PID", "grid G8, on E100 at the side-return gap"), ("REPORT", "Fig E.1 and start-up tables (ball valve, floor 3)")],
    "V302": [("PID", "grid G8, on E100 at the side-return gap"), ("REPORT", "Fig E.1 and start-up tables (needle valve, floor 3)")],
})
NOZZLE_CITATIONS["E100_N_side_inlet"] = [("PID", "E100 side nozzle between V318 and V302, grid G8"),
                                         ("TEAM", "stream can return to the stage below the top, between V302 and V318")]


# Second sources found during the 100-question review (Oct 2026)
M4 = "recommendation M4 (PSH on E100 trips the plant at 2 barg)"
ITEM_CITATIONS.update({
    "TI100": [("PID", "grid K6"), ("REPORT", "Appendix B instrument list (K6, floor 1)")],
    "TI213": [("PID", "heater control section"), ("REPORT", "Appendix B instrument list (H10, floor 2) and section E.3.4.1")],
    "FI102": [("PID", "grid M6"), ("REPORT", "Appendix B instrument list (M6, floor 1)")],
    "FI103": [("PID", "grid L12"), ("REPORT", "Appendix B instrument list (M12, floor 1)")],
    "FI104": [("PID", "grid L12"), ("REPORT", "Appendix B instrument list (M12, floor 1)")],
    "PSHH400": [("PID", "E100 top, grid F7"), ("HAZOP", M4)],
    "PSHH116": [("PID", "E100 base, right-hand side"), ("TEAM", "right-hand side of E100"), ("HAZOP", M4)],
    "V217": [("REPORT", "Fig E.2 (opened for the commissioning test; floor 3, grid G14)"),
             ("REPORT", "lean MEA valve list (floor 2, grid G14, normally closed) and start-up tables (ball, grid H14)")],
})
ITEM_CITATIONS["E100"] = ITEM_CITATIONS["E100"] + [("HAZOP", "element 11, item 10 (designed for sub-atmospheric pressure)")]
