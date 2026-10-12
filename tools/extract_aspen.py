"""
Extract results from an Aspen Plus compound file (.apwz) into JSON.

The .apwz is a zip archive containing a text backup (.bkp.backup).
Results live in Aspen's internal record format ("DSET ..." lines).

Usage (from the repo root):
    python tools/extract_aspen.py path/to/ABB_pilot_plant_final_3.apwz data/aspen/aspen_v3.json

Units (checked against the saved results):
    temperature degC, pressure bar, mass flow kg/h, mole flow kmol/h.
    Aspen stores enthalpy in kcal/kmol and enthalpy flow in cal/s;
    both are converted here to kJ/kmol and W (x 4.184).
"""
import json
import re
import sys
import zipfile

CAL_TO_J = 4.184
COMPONENTS = ["H2O", "N2", "CO2", "O2", "MEA", "MEACOO-", "MEA+",
              "H3O+", "HCO3-", "CO3-2", "OH-"]
MW = {"H2O": 18.0153, "N2": 28.0135, "CO2": 44.0098, "O2": 31.9988,
      "MEA": 61.0831, "MEACOO-": 104.085, "MEA+": 62.091, "H3O+": 19.023,
      "HCO3-": 61.017, "CO3-2": 60.009, "OH-": 17.007}


def read_backup(path):
    if path.endswith(".apwz"):
        with zipfile.ZipFile(path) as z:
            name = next(n for n in z.namelist() if n.endswith(".bkp.backup") or n.endswith(".bkp"))
            raw = z.read(name)
    else:
        raw = open(path, "rb").read()
    return raw.decode("latin-1").replace("\r", "")


def numbers(body):
    out = []
    for tok in re.sub(r"<\d+>", " ", body).split():
        if tok == "*":
            out.append(None)
            continue
        try:
            out.append(float(tok.replace("D", "E")))
        except ValueError:
            out.append(tok.strip('"'))
    return out


def records(text, prefix):
    pat = re.compile(re.escape(prefix) + r" @\S+ \((.*?)\)\s*\n (?=DSET|IDSET|LSET)", re.S)
    return [m.group(1) for m in pat.finditer(text)]


def apparent(mass):
    """Apparent CO2 loading (mol/mol) and apparent MEA mass (kg/h) from true species."""
    mol = {c: (mass.get(c) or 0.0) / MW[c] for c in COMPONENTS}
    co2 = mol["CO2"] + mol["MEACOO-"] + mol["HCO3-"] + mol["CO3-2"]
    mea = mol["MEA"] + mol["MEACOO-"] + mol["MEA+"]
    return (co2 / mea if mea > 1e-9 else None), mea * MW["MEA"], co2 * MW["CO2"]


def streams(text):
    out, n = {}, len(COMPONENTS)
    pat = re.compile(r"DSET STREAM MATERIAL (\S+) STR_MAIN @\S+ \((.*?)\)\s*\n DSET", re.S)
    for m in pat.finditer(text):
        v = numbers(m.group(2))
        src, dst, phase, x = v[0], v[1], v[2], v[4:]
        mass = dict(zip(COMPONENTS, x[2 * n:3 * n]))
        r = x[4 * n:]
        ld, mea_kg, co2_kg = apparent(mass)
        out[m.group(1)] = {
            "from_block": None if src == "*" else src,
            "to_block": None if dst == "*" else dst,
            "phase": phase,
            "T_C": r[3], "P_bar": r[4],
            "mass_flow_kg_h": r[1], "mole_flow_kmol_h": r[0], "volume_flow_m3_h": r[2],
            "vapour_fraction": r[5],
            "molar_enthalpy_kJ_kmol": r[8] * CAL_TO_J,
            "enthalpy_flow_W": r[10] * CAL_TO_J,
            "component_mass_flow_kg_h": mass,
            "apparent_CO2_kg_h": co2_kg,
            "apparent_CO2_loading_mol_mol": ld,
            "apparent_MEA_wt_frac": mea_kg / r[1] if r[1] else None,
        }
    return out


def block_status(text):
    out = {}
    for m in re.finditer(r"DSET BLOCK (\S+) (\S+) BLKSTAT @BLKSTAT \((\d) \d\)", text):
        code = int(m.group(3))
        out[m.group(2)] = {"aspen_model": m.group(1), "status": {0: "OK", 1: "ERROR", 2: "WARNING"}.get(code, "UNKNOWN"),
                           "message": None}
    for m in re.finditer(r"DSET BLOCK \S+ (\S+) BLKMSG @BLKMSG \((.*?)\)", text, re.S):
        msg = " ".join(re.findall(r'"([^"]*)"', m.group(2))).strip()
        if m.group(1) in out and msg:
            out[m.group(1)]["message"] = msg
    return out


def column_profile(text, block="E100", nstage=12):
    pro = [numbers(b) for b in records(text, f"DSET BLOCK RADFRAC {block} RAD_PRO2")]
    tx = records(text, f"DSET BLOCK RADFRAC {block} TRAY_X")
    ty = records(text, f"DSET BLOCK RADFRAC {block} TRAY_Y")
    if len(pro) < 5 or not tx or not ty:
        return None
    T, P, _Q, L, V = pro[:5]
    X, Y, nc = numbers(tx[0]), numbers(ty[0]), len(COMPONENTS)
    rows = []
    for s in range(nstage):
        x = dict(zip(COMPONENTS, X[s * nc:(s + 1) * nc]))
        y = dict(zip(COMPONENTS, Y[s * nc:(s + 1) * nc]))
        co2 = x["CO2"] + x["MEACOO-"] + x["HCO3-"] + x["CO3-2"]
        mea = x["MEA"] + x["MEACOO-"] + x["MEA+"]
        rows.append({"stage": s + 1, "T_C": T[s], "P_bar": P[s],
                     "liquid_flow_kmol_h": L[s], "vapour_flow_kmol_h": V[s],
                     "y_CO2": y["CO2"], "y_H2O": y["H2O"],
                     "liquid_CO2_loading_mol_mol": co2 / mea if mea else None})
    return rows


def heatx_results(text):
    """Area and overall U where Aspen reports them (C100 shortcut, H100 EDR)."""
    out = {}
    for m in re.finditer(r"DSET BLOCK HEATX (\S+) HTX_RES @\S+ \((.*?)\)\s*\n (?=DSET|IDSET|LSET)", text, re.S):
        hit = re.search(r"([\d.D+\-]+)\s+<3>\s+([\d.D+\-]+)\s+<1>\s+([\d.D+\-]+)\s+<3>", m.group(2))
        if hit:
            area = float(hit.group(2).replace("D", "E"))
            u = float(hit.group(3).replace("D", "E")) * CAL_TO_J * 1e4  # cal/s/cm2/K -> W/m2/K
            if area > 0:
                out[m.group(1)] = {"area_m2": area, "U_W_m2K": u}
    return out


def meta(text):
    d = re.search(r'DATETIME "([^"]+)"', text)
    v = re.search(r'VERSION "([^"]+)"', text)
    return {"saved": d.group(1).strip() if d else None, "aspen_version": v.group(1) if v else None}


if __name__ == "__main__":
    src, dst = sys.argv[1], sys.argv[2]
    txt = read_backup(src)
    res = {"source_file": src.split("/")[-1], **meta(txt), "block_status": block_status(txt),
           "streams": streams(txt), "heat_exchangers": heatx_results(txt),
           "E100_profile": column_profile(txt)}
    json.dump(res, open(dst, "w"), indent=1)
    print(f"{res['source_file']}: {len(res['streams'])} streams, {len(res['block_status'])} blocks -> {dst}")
