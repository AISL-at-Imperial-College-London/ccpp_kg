# Stripping loop KG (v2)

Knowledge graph of the stripping loop of Pilot Plant 2514, used to test SPARQL
queries before expanding to the full plant.

## Loop (stripping loop line-up, absorber isolated)

E100 draw-off nozzle below TT103 (stage 11) > FT102 > Q105 > H100 > Q106 > Q103 >
E100 sump (stage 12) > V110 > V112 > C100 > V113a > V113b > J100 > PCV122 > V116 >
V117a > Z102 > V117b > V121 > FT103 > FT104 > SOV125 > H200a | H200b > V403 > V402 >
E100 top (stage 1) > down the packing to the chimney tray.

Tie-ins: FI102, DI100, TT100, TI100, TT104, PT103, TT105, TT106, B101, PT104,
PDT105, FI103, FI104, TT213, TI213, FT305, TT309.
Closed branches: RV101, V120 (Z102 bypass), SOV123 (to absorber), V316 (vent).

Z102 bypass: V116 > V120 > V121, normally closed. Opened when PDT105 >= 0.45 bar
(REPORT E.3.6): reduce J100 to 15 %, open V120, close V117a and V117b.

## Files

| File | Purpose |
|---|---|
| `../ontology/ccpp_ontology.ttl` | Shared vocabulary (v0.2) |
| `loop_data.py` | All plant data in plain tables, with sources |
| `heat_mass_transfer.py` | Energy balances, LMTD, UA, effectiveness, CO2 balance, stage desorption |
| `build_stripping_loop.py` | Builds `stripping_loop.ttl` from the tables, Aspen JSON and HAZOP JSON |
| `queries/*.rq` | 24 SPARQL competency questions |
| `test_queries.py` | Runs every query, checks each answer, then runs SHACL validation |
| `shapes.ttl` | SHACL structural rules |

## Run (from the repo root)

```bash
pip install rdflib pyshacl
python stripping_loop/build_stripping_loop.py
python stripping_loop/test_queries.py
```

## Sources

P&ID (marked up, checked with the team), P_ID_Differences.pdf, PilotPlantReport_Group6_2_0.pdf,
Carbon_Capture_plant_summary_2023-2024_v01.pdf, HAZOP 2010, Aspen files v3 and v6.1.

## Still to check (query 17)

PCV122 set pressure, and the FT102, FT103 and FT104 ranges, all read from a low-resolution image.
