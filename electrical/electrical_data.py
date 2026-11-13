"""
Piece 15: electrical power distribution (Pilot Plant 2514), for the KG A+ improvements.

Source (received from the plant, Nov 2026): cable diagrams C2286-CD-001, JMS Automation & Drives, sheets 1 and 2,
15 August 2011, marked PRELIMINARY (first issue).
- Sheet 1, power distribution: 415 V three-phase supply to the motor control panel +MC1, which feeds the two 9 kW
  heaters and the eight motors; three 230 V single-phase supplies, each through a UPS to a 16-way distribution board,
  feeding the control system panel, the remote I/O panels, the fieldbus panel and the CO2 analyser panel.
- Sheet 2, fieldbus power distribution: 110 V supplies from the fieldbus panel +FB1 to eight field instruments.
'powers' links run from each supply to what it feeds, so 'what is lost if MC1 or DB301 fails?' is a graph walk:
  SELECT ?x WHERE { ccpp:MC1 ccpp:powers+ ?x }
The drawing's levels are mapped to the KG's floors: Level 1 = floor 1, Level 1M = floor 2, Level 2 = floor 3,
Level 3 = floor 4 (checked against FT201 on floor 2 and PSH400 on floor 4).
"""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "kgkit"))

S1 = "sheet 1 (power distribution)"
S2 = "sheet 2 (fieldbus power distribution)"

SECTION = dict(
    prefix="ele", loop_id="PowerDistributionRegister", mode="FigureOfEight", flow="feedsInto",
    loop_label="Electrical power distribution (register, no process flow route)",
    loop_note="Supplies, panels, motors and the instruments powered from the fieldbus panel.",
    loop_cite=[("CABLE", "C2286-CD-001 sheets 1 and 2, 15 August 2011, preliminary")],
)

ITEMS = {}

def panel(key, cls, label, floor, note, where):
    ITEMS[key] = dict(cls=cls, label=label, floor=floor, note=note, cite=[("CABLE", where)])

panel("EL_415V", "PowerSupply", "415 V AC three-phase 100 A supply (existing supply)", 1, "Feeds the motor control panel +MC1.", S1 + ", Level 1")
panel("MC1", "ElectricalPanel", "+MC1 motor control panel", 1, "Feeds the two electric heaters and the eight motors, each through a local isolator.", S1 + ", Level 1")
for n, phase in ((1, "L1"), (2, "L2"), (3, "L3")):
    panel(f"EL_230V_{phase}", "PowerSupply", f"230 V AC single-phase 32 A supply {phase} (existing supply)", 3, f"Feeds UPS{n} through isolator Q30{n}.", S1 + ", Level 2")
    panel(f"UPS{n}", "ElectricalPanel", f"UPS{n}-30{n} uninterruptible power supply", 3, f"Between the 230 V supply {phase} and distribution board DB30{n}.", S1 + ", Level 2")
    panel(f"DB30{n}", "ElectricalPanel", f"DB30{n} 16-way distribution board", 3, "UPS-backed 230 V distribution.", S1 + ", Level 2")
panel("CS1", "ElectricalPanel", "+CS1 control system panel", 1, "Fed from DB301 and DB302; its 24 V supplies the pressure switches PSH116, PSH117 and PSH118.", S1 + ", Level 1")
panel("RC2", "ElectricalPanel", "+RC2 remote I/O panel", 2, "Fed from DB301 and DB302; 24 V to process panel +PP2.", S1 + ", Level 1M")
panel("RC3", "ElectricalPanel", "+RC3 remote I/O panel", 3, "Fed from DB301 and DB302.", S1 + ", Level 2")
panel("RC4", "ElectricalPanel", "+RC4 remote I/O panel", 4, "Fed from DB301 and DB302; 24 V to process panel +PP4 and to the switches PSH400, PSH405, LSHH400, LSH404, LSH405, LSLL402 and LSLL403.",
      S1 + ", Level 3, and sheet 2")
panel("PP2", "ElectricalPanel", "+PP2 process panel", 2, "24 V from +RC2.", S1 + ", Level 1M")
panel("PP4", "ElectricalPanel", "+PP4 process panel", 4, "24 V from +RC4.", S1 + ", Level 3")
panel("FB1", "ElectricalPanel", "+FB1 fieldbus panel (24 V and 110 V distribution)", 1, "Fed from DB301 and DB302; its 110 V distribution supplies eight field instruments.", S2 + ", Level 1")
panel("CA1", "ElectricalPanel", "+CA1 CO2 analyser panel", 4, "Fed from DB303.", S1 + ", Level 3")

# motor: (rated power kW, driven machine, description on the drawing)
MOTORS = {"M100": (2.2, "J100", "PUMP J100"), "M101A": (2.2, "J101a", "PUMP J101A"), "M101B": (2.2, "J101b", "PUMP J101B"), "M102": (3.0, "J102", "BLOWER J102"),
          "M103": (4.0, "J103", "COMP J103"), "M104": (0.55, "J104", "PUMP J104"), "M105": (0.55, "J105", "PUMP J105"), "M300": (0.37, "J300", "PUMP J300")}
LINKS = [("EL_415V", "powers", "MC1")]
LIMITS = {}
for m, (kw, machine, text) in MOTORS.items():
    ITEMS[m] = dict(cls="Motor", label=f"{m} motor, {kw:g} kW, driving {machine}", floor=2 if m == "M300" else 1,
                    props={"ratedPowerText": f"{kw:g} kW"}, note=f"Drawn as '{m} {kw:g}kW {text}', fed from +MC1 through a local isolator.",
                    cite=[("CABLE", S1 + f", motor {m}")])
    LINKS += [("MC1", "powers", m), (m, "powers", machine), (m, "drives", machine)]
    LIMITS[f"{m}_rated_power"] = (machine, "motor rated power", "rating", None, kw, "kW", [("CABLE", S1 + f", motor {m}")])
for h in ("H200a", "H200b"):
    LINKS.append(("MC1", "powers", h))
    LIMITS[f"{h}_rated_power"] = (h, "heater rated power", "rating", None, 9.0, "kW", [("CABLE", S1 + f", {h.upper()} 9kW circulation heater")])

for n, phase in ((1, "L1"), (2, "L2"), (3, "L3")):
    LINKS += [(f"EL_230V_{phase}", "powers", f"UPS{n}"), (f"UPS{n}", "powers", f"DB30{n}")]
for db in ("DB301", "DB302"):                       # both boards feed each of these panels
    LINKS += [(db, "powers", p) for p in ("RC4", "RC3", "RC2", "CS1", "FB1")]
LINKS += [("DB303", "powers", "CA1"), ("RC2", "powers", "PP2"), ("RC4", "powers", "PP4")]
FIELDBUS_110V = ["FT305", "FT304", "FT302", "AT300", "FT201", "AT100", "FT102", "FT103"]
LINKS += [("FB1", "powers", i) for i in FIELDBUS_110V]

KNOWN_TAGS = sorted({m[1] for m in MOTORS.values()} | {"H200a", "H200b"} | set(FIELDBUS_110V))
LOOP = []

OPEN_ITEMS = {
    "EL01": ("The cable diagrams are a PRELIMINARY first issue (August 2011): the final or as-built issue would confirm ratings, panels and cable routes",
             ["MC1"], "Final issue of C2286-CD-001 from the plant"),
    "EL02": ("Variable speed drives are not drawn, although J100, J101a/b and J300 are speed-controlled (SIC100, SIC101a/b, SIC300)", ["MC1", "M100"],
             "Motor control panel schedule or drive list"),
    "EL03": ("Only eight instruments are shown with a 110 V supply; the power source of the other instruments, the shutdown valve solenoids and the "
             "control valves is not shown", ["FB1"], "Instrument power schedule or loop diagrams"),
    "EL04": ("The mapping of the drawing's levels (1, 1M, 2, 3) to the KG's floors (1 to 4) is derived, not stated", ["RC2", "RC4"], "Site check"),
    "EL05": ("The switches drawn on the 24 V supplies are tagged PSH116/117/118, PSH400/405, LSHH400, LSH404/405 and LSLL402/403; the cause and effect "
             "matrix calls them PSHH and LSHH/LSLL", ["CS1", "RC4"], "Instrument index"),
}
