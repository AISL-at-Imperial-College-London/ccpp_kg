# Stripping loop KG: validation record

## 1. Verification (is the KG built correctly?)

| Check | Method | Result |
|---|---|---|
| 27 competency questions | `test_queries.py` (SPARQL, each with an expected answer) | All pass |
| Structure | SHACL (`shapes.ttl`) with RDFS inference | Pass |
| Vocabulary | Every class and property used is declared in the ontology | Pass |
| Links | No reference points to an undefined node | Pass |
| Internal consistency | Q25: valve positions agree with the line-up procedure; Q26: no closed valve on the flow path | Pass |
| Physics | Energy balances close within 0.1 % on every exchanger; E100 CO2 balance closes; stage desorption sums to overhead CO2 (Q7, Q8, Q10) | Pass |

### Mutation testing (do the tests catch mistakes?)

Twelve deliberate errors were introduced one at a time. All twelve were caught.

| Deliberate error | Caught by |
|---|---|
| Swap V117b and V121 | Q1, Q2 |
| Swap B101 and PT104 | Q1 |
| Leave Z102 bypass V120 open | Q4, Q25 |
| Close V116 on the flow path | Q25, Q26 |
| Drop V121 from the line-up | Q22 |
| Move TT300 to stage 7 | Q13 |
| Wrong sensor on the heater control loop | Q21 |
| Claim H200a is covered by the HAZOP | Q12 |
| Bypass procedure steps out of order | Q20 |
| Loop returns to stage 5 instead of the top | Q27 (added after this mutation was first missed) |
| Remove Q105 from the reboiler circuit | Q23 |
| Mark an unconfirmed value as verified | Q17 |

## 2. Validation (does the KG match the real plant?)

### Cross-source audit (automated)

- 97 tagged items. 32 appear in two or more text sources (report, summary, HAZOP, differences document), 47 in one, and 18 only on the P&ID (heater control instruments from the high-resolution image, line numbers Q103/Q105/Q106 and DI100 confirmed by the team, and level and pressure switches).
- Valve positions: 21 valves checked against the report's commissioning-test line-up (Fig E.1/E.2). This found one genuine error, now fixed: the steam-side valves (FCV110, V101, V102, V105) were stored as open but are closed during the stripping loop test.
- Instrument details: 32 instruments checked against the report's instrument lists (sensor type, signal, grid, floor). No mismatches.

### Still needed (human and plant evidence)

- [ ] Walk the loop (Q1 output) against the P&ID with someone who did not build the KG.
- [ ] Walk the loop on site, valve by valve.
- [ ] Confirm the four flagged values (Q17): PCV122 setting, FT102, FT103 and FT104 ranges.
- [ ] Confirm the stage-to-instrument mapping (odd Aspen stages = gaps between beds).
- [ ] Identify V217, which the report lists as open for the commissioning test but is not on the loop as traced.
- [ ] Compare with plant data during a stripping loop run (FT103 vs FT104, LT101 vs J100 power, PDT105).
