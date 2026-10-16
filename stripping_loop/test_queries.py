"""
Run the SPARQL competency questions against the stripping loop KG and
check the answers.

Run from the repo root, after building the KG:
    python stripping_loop/build_stripping_loop.py
    python stripping_loop/test_queries.py

Each query lives in stripping_loop/queries/*.rq. The CHECKS dictionary
below holds the expected answer for each one. A failed check prints FAIL
with the reason; the script exits with code 1 if anything fails.
"""
import pathlib
import sys

from rdflib import Graph

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent


def py(v):
    return None if v is None else v.toPython()


def rows_of(result):
    return [{str(k): py(r[k]) for k in result.vars} for r in result]


def col(rows, name):
    return [r[name] for r in rows]


def approx(a, b, tol):
    return a is not None and abs(a - b) <= tol


def check_order(rows):
    idx = {}
    for r in rows:
        idx.setdefault(r["name"], []).append(r["idx"])
    expect(rows[0]["name"].startswith("E100 draw-off"), f"loop should start at the E100 draw-off nozzle, got {rows[0]['name']}")
    expect(rows[-1]["name"] == "E100", "loop should end back in E100")
    expect("V309" not in idx, "V309 should not be in the loop")
    expect(not {"V120", "SDV123", "V316", "RV101", "FT305", "TT309"} & set(idx), "closed branches and the reflux tie-in are not on the loop route")
    expect(idx["H100"][0] < idx["TT100"][0] < idx["Q106"][0], "TT100 and TI100 sit before Q106")
    expect(idx["FT102"][0] < idx["H100"][0] < idx["Q106"][0] < idx["V110"][0], "reboiler circuit comes before the sump outlet")
    expect(idx["V117b"][0] < idx["V121"][0] < idx["FT103"][0], "V117b then V121 then FT103")
    expect(idx["B101"][0] < idx["PT104"][0], "as-built order is B101 then PT104")
    expect(idx["H200a"] == idx["H200b"], "H200a and H200b are in parallel")
    expect(idx["SDV125"][0] < idx["H200a"][0] < idx["V403"][0] < idx["V402"][0], "SDV125, heaters, V403, V402")


def check_srd(rows):
    v3 = next(r for r in rows if r["file"].startswith("ABB_pilot_plant_final_3"))
    assert approx(v3["stripped"], 33.65, 0.1), v3["stripped"]
    assert v3["co2err"] < 1.0, "CO2 balance should close within 1 %"
    assert 0.25 < v3["lean"] < 0.35 and 0.55 < v3["rich"] < 0.65, (v3["lean"], v3["rich"])


def check_profile(rows):
    assert len(rows) == 12, len(rows)
    assert rows[-1]["T"] > rows[0]["T"], "sump should be hotter than the top"
    assert rows[0]["loading"] > rows[-1]["loading"], "loading should fall down the column"
    total = sum(r["desorbed"] for r in rows)
    assert approx(total, 33.65, 0.5), f"stage desorption sums to {total:.2f} kg/h, overhead CO2 is 33.65"


def expect(cond, msg):
    if not cond:
        raise AssertionError(msg)


def first(rows, tag):
    return next(x for x in rows if x["tag"] == tag)


CHECKS = {
    "01_loop_order": check_order,
    "02_between_Z102_and_FT103": lambda r: expect(col(r, "tag") == ["V117b", "V121"], col(r, "tag")),
    "03_loop_is_closed": lambda ans: expect(ans is True, "loop is not closed"),
    "04_bypass_check": lambda r: expect(len(r) == 1 and r[0]["valve"] == "V120" and r[0]["position"] == "closed"
                                        and r[0]["onActivePath"] is False and r[0]["pipedIn"] is True, r),
    "05_converged_cases": lambda r: expect([x["file"] for x in r] == ["ABB_pilot_plant_final_3.apwz"], r),
    "06_problem_blocks": lambda r: expect({"E100", "H100", "C100"} <= {x["block"] for x in r if "6_1" in x["file"]}, r),
    "07_heat_exchanger_performance": lambda r: expect(approx(first(r, "C100")["duty"], 17.4, 0.2)
                                                      and first(r, "C100")["err"] < 1.0, first(r, "C100")),
    "08_stripper_profile": check_profile,
    "09_max_desorption_stage": lambda r: expect(r[0]["stage"] == 2, r),
    "10_column_performance": check_srd,
    "11_hazop_for_Z102": lambda r: expect(any("PDAH" in (x["safeguard"] or "") for x in r), r),
    "12_equipment_without_hazop": lambda r: expect(set(col(r, "tag")) == {"H200a", "H200b", "SDV125"}, col(r, "tag")),
    "13_instruments_at_stage5": lambda r: expect(set(col(r, "tag")) == {"TT300", "TT301"}, r),
    "14_protection_of_J100": lambda r: expect({"TZAH106", "RV101_set", "J100_flow_range", "J100_power_range",
                                               "LZAL102"} <= set(col(r, "limit")), col(r, "limit")),
    "15_pid_discrepancies": lambda r: expect(len(r) == 4, r),
    "16_valves_on_floor3": lambda r: expect(col(r, "tag") == ["V315", "V316", "V402", "V403"], col(r, "tag")),
    "17_unverified_values": lambda r: expect(len(r) == 0, col(r, "limit")),
    "18_compare_cases_C100": lambda r: expect(len(r) == 2, r),
    "19_bypass_route": lambda r: expect(set(col(r, "skipped")) == {"V117a", "Z102", "V117b"}
                                        and {x["via"] for x in r} == {"V120"} and r[0]["from"] == "V116"
                                        and r[0]["to"] == "V121", r),
    "20_bypass_procedure": lambda r: expect([x["item"] for x in r] == ["J100", "V120", "V117a", "V117b", "J100", "Z102"]
                                            and "0.45" in r[0]["trigger"], [x["item"] for x in r]),
    "21_heater_control": lambda r: expect(set(col(r, "sensor")) == {"TT213"}
                                          and {"TIC213a", "TIC213b"} <= set(col(r, "controller"))
                                          and set(col(r, "final")) == {"H200a", "H200b"}
                                          and all(x["controller"][-1] == x["final"][-1] for x in r), r),
    "22_lineup_open_valves": lambda r: expect(set(col(r, "tag")) == {"V110", "V112", "V113a", "V113b", "V116", "V117a",
                                                                     "V117b", "V121", "SDV125", "V403", "V402"}, col(r, "tag")),
    "23_reboiler_circuit": lambda r: expect([x["name"] for x in r][1:-1] == ["FT102", "Q105", "H100", "Q106"],
                                            [x["name"] for x in r]),
    "27_return_point": lambda r: expect(len(r) == 1 and r[0]["stage"] == 1 and r[0]["loopStage"] == 1, r),
    "25_lineup_conflicts": lambda r: expect(len(r) == 0, r),
    "26_closed_valves_on_flow_path": lambda r: expect(len(r) == 0, r),
    "24_cascade_and_interlocks": lambda r: expect(any(x["kind"] == "cascade" for x in r)
                                                  and {x["detail"] for x in r if x["kind"] == "interlock"} == {"H200a", "H200b"}, r),
}


def show(rows, limit=15):
    if not rows:
        print("    (no rows)")
        return
    keys = list(rows[0].keys())
    for r in rows[:limit]:
        print("    " + " | ".join(f"{k}={round(r[k], 3) if isinstance(r[k], float) else r[k]}" for k in keys))
    if len(rows) > limit:
        print(f"    ... {len(rows) - limit} more rows")


def main():
    g = Graph()
    g.parse(ROOT / "ontology" / "ccpp_ontology.ttl")
    g.parse(HERE / "stripping_loop.ttl")
    print(f"Loaded {len(g)} triples\n")

    failures = 0
    for q in sorted((HERE / "queries").glob("*.rq")):
        text = q.read_text()
        question = text.splitlines()[0].lstrip("# ")
        res = g.query(text)
        answer = res.askAnswer if res.type == "ASK" else rows_of(res)
        print(f"[{q.stem}] {question}")
        if res.type == "ASK":
            print(f"    {answer}")
        else:
            show(answer)
        check = CHECKS.get(q.stem)
        if check:
            try:
                check(answer)
                print("    PASS\n")
            except Exception as e:  # noqa: BLE001
                failures += 1
                print(f"    FAIL: {e}\n")
        else:
            print("    (no check)\n")

    try:
        from pyshacl import validate
        ok, _, report = validate(g, shacl_graph=str(HERE / "shapes.ttl"), inference="rdfs")
        print("SHACL validation:", "PASS" if ok else "FAIL")
        if not ok:
            failures += 1
            print(report)
    except ImportError:
        print("pyshacl not installed, skipping SHACL validation (pip install pyshacl)")

    print(f"\n{failures} failure(s)")
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
