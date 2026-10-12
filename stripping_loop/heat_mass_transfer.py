"""
Heat and mass transfer calculations for the stripping loop.

Works on the JSON extracted from Aspen (tools/extract_aspen.py) and returns
plain dictionaries that build_stripping_loop.py writes into the KG.

What it calculates for each simulation case:
  * Heat exchangers: duty from each side, energy balance error, end
    temperature differences, counter-current LMTD, UA = Q / LMTD,
    effectiveness, and a temperature-cross flag.
  * Stripper E100: CO2 and energy balance around the column, CO2 stripped,
    rich and lean loading, reboiler duty, specific reboiler duty, and the
    CO2 desorbed on each stage from the vapour profile.

The rigorous rate-based model stays in Aspen. This layer checks and
summarises the transfer results so they can be queried with SPARQL.
"""
import math

MW_CO2 = 44.0098

# Which Aspen streams sit on each side of each exchanger, per case.
# Electric heaters only have a process side, so "hot" is None.
HX_MAP = {
    "aspen_v3": {
        "C100": {"hot": [("S3", "S2")], "cold": [("S8", "S15")]},
        "H100": {"hot": [("S19", "S18"), ("S20", "S23")], "cold": [("S14", "S24")]},
        "H200a": {"hot": None, "cold": [("S5", "S7")]},
        "H200b": {"hot": None, "cold": [("S4", "S9")]},
    },
    "aspen_v6_1": {
        "C100": {"hot": [("S3BACKUP", "S2")], "cold": [("S8", "S27")]},
        "H100": {"hot": [("S31", "S17")], "cold": [("S23", "S14")]},
        "H200a": {"hot": None, "cold": [("S5", "S7")]},
        "H200b": {"hot": None, "cold": [("S4", "S9")]},
    },
}

# Streams around E100 in each case.
COLUMN_MAP = {
    "aspen_v3": {"feeds": ["S10", "S24"], "products": ["S13", "S6", "S14"],
                 "rich": "S10", "lean": "S6", "overhead": "S13", "co2_product": "S16"},
    "aspen_v6_1": {"feeds": ["S10", "S14"], "products": ["S15", "S12", "S23"],
                   "rich": "S10", "lean": "S12", "overhead": "S15", "co2_product": "S16"},
}

# Aspen blocks that make up each piece of physical equipment.
AREA_BLOCKS = {"aspen_v3": {"C100": ["C100"], "H100": ["H100REAC", "H100HEAT"]},
               "aspen_v6_1": {"C100": ["C100"], "H100": ["H100"]}}


def _lmtd(dt1, dt2):
    if dt1 <= 0 or dt2 <= 0:
        return None
    if abs(dt1 - dt2) < 1e-6:
        return dt1
    return (dt1 - dt2) / math.log(dt1 / dt2)


def heat_exchanger_performance(case_key, data):
    s = data["streams"]
    out = {}
    for eq, sides in HX_MAP[case_key].items():
        cold = sides["cold"]
        q_cold = sum(s[o]["enthalpy_flow_W"] - s[i]["enthalpy_flow_W"] for i, o in cold) / 1000
        r = {"equipment": eq, "coldSideDuty_kW": q_cold, "duty_kW": q_cold,
             "coldInlet_C": s[cold[0][0]]["T_C"], "coldOutlet_C": s[cold[-1][1]]["T_C"]}
        if sides["hot"]:
            hot = sides["hot"]
            q_hot = sum(s[i]["enthalpy_flow_W"] - s[o]["enthalpy_flow_W"] for i, o in hot) / 1000
            th_in = s[hot[0][0]]["T_C"]
            th_out = sum(s[o]["T_C"] for _, o in hot) / len(hot)
            tc_in, tc_out = r["coldInlet_C"], r["coldOutlet_C"]
            dt1, dt2 = th_in - tc_out, th_out - tc_in
            lm = _lmtd(dt1, dt2)
            # effectiveness from effective heat capacity rates (Q / dT on each side)
            c_hot = q_hot / (th_in - th_out) if th_in != th_out else float("inf")
            c_cold = q_cold / (tc_out - tc_in) if tc_out != tc_in else float("inf")
            c_min = min(c_hot, c_cold)
            q_max = c_min * (th_in - tc_in) if math.isfinite(c_min) else None
            r.update({
                "hotSideDuty_kW": q_hot, "duty_kW": (q_hot + q_cold) / 2,
                "hotInlet_C": th_in, "hotOutlet_C": th_out,
                "energyBalanceError_pct": 100 * abs(q_hot - q_cold) / max(abs(q_hot), 1e-9),
                "temperatureCross": lm is None,
                "lmtd_K": lm,
                "ua_W_K": (1000 * q_cold / lm) if lm else None,
                "effectiveness": (q_cold / q_max) if q_max else None,
            })
            blocks = AREA_BLOCKS[case_key].get(eq, [])
            hx = data.get("heat_exchangers", {})
            if blocks and all(b in hx for b in blocks):
                area = sum(hx[b]["area_m2"] for b in blocks)
                r["area_m2"] = area
                r["overallU_W_m2K"] = sum(hx[b]["U_W_m2K"] * hx[b]["area_m2"] for b in blocks) / area
        out[eq] = r
    return out


def column_performance(case_key, data, reboiler_duty_kW):
    s, m = data["streams"], COLUMN_MAP[case_key]
    co2_in = sum(s[k]["apparent_CO2_kg_h"] for k in m["feeds"])
    co2_out = sum(s[k]["apparent_CO2_kg_h"] for k in m["products"])
    h_in = sum(s[k]["enthalpy_flow_W"] for k in m["feeds"])
    h_out = sum(s[k]["enthalpy_flow_W"] for k in m["products"])
    stripped = s[m["overhead"]]["apparent_CO2_kg_h"]
    product = s[m["co2_product"]]["apparent_CO2_kg_h"]
    res = {
        "co2Stripped_kg_h": stripped,
        "co2Product_kg_h": product,
        "co2BalanceError_pct": 100 * abs(co2_in - co2_out) / max(co2_in, 1e-9),
        "energyBalanceError_pct": 100 * abs(h_in - h_out) / abs(h_in),
        "reboilerDuty_kW": reboiler_duty_kW,
        "richLoading_mol_mol": s[m["rich"]]["apparent_CO2_loading_mol_mol"],
        "leanLoading_mol_mol": s[m["lean"]]["apparent_CO2_loading_mol_mol"],
        # GJ per tonne = (kW * 3600 s/h / 1e6) / (kg/h / 1000)
        "specificReboilerDuty_GJ_t": (reboiler_duty_kW * 3.6e-3) / (product / 1000) if product > 1e-6 else None,
    }
    return res


def stage_desorption(profile):
    """CO2 moving from liquid to vapour on each stage, kg/h.
    Vapour flows upward, so stage n receives vapour from stage n+1."""
    if not profile:
        return {}
    co2_vap = {r["stage"]: r["vapour_flow_kmol_h"] * r["y_CO2"] for r in profile}
    n = max(co2_vap)
    return {st: (co2_vap[st] - co2_vap.get(st + 1, 0.0)) * MW_CO2 for st in range(1, n + 1)}


def analyse(case_key, data):
    hx = heat_exchanger_performance(case_key, data)
    col = column_performance(case_key, data, hx["H100"]["duty_kW"])
    return {"heat_exchangers": hx, "column": col, "stage_desorption": stage_desorption(data.get("E100_profile"))}


if __name__ == "__main__":
    import json
    import pathlib
    root = pathlib.Path(__file__).resolve().parents[1] / "data" / "aspen"
    for key in HX_MAP:
        res = analyse(key, json.load(open(root / f"{key}.json")))
        print(f"\n=== {key}")
        for eq, r in res["heat_exchangers"].items():
            print(eq, {k: round(v, 3) if isinstance(v, float) else v for k, v in r.items()})
        print("E100", {k: round(v, 3) if isinstance(v, float) else v for k, v in res["column"].items()})
        if res["stage_desorption"]:
            print("CO2 desorbed per stage (kg/h):", {k: round(v, 2) for k, v in res["stage_desorption"].items()})
