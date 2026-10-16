# Stripping loop KG: query answers with sources


## 01_loop_order

**CQ1: In what order does the solvent pass through the stripping loop?**

- idx = 0 | name = E100 draw-off nozzle below TT103 (chimney tray, to H100) | type = inline
- idx = 1 | name = FT102 | type = inline
  - Sources: P&ID grid M6; Pilot Plant Report Appendix B instrument list
- idx = 2 | name = FI102 | type = tie-in
  - Sources: P&ID grid M6
- idx = 3 | name = DI100 | type = tie-in
  - Sources: P&ID on FT102, grid M6; Team check tag is DI100, not DE100
- idx = 4 | name = Q105 | type = inline
  - Sources: P&ID line Q105, near grid M6; Team check reboiler circuit trace
- idx = 5 | name = H100 | type = inline
  - Sources: Aspen v3 blocks H100REAC and H100HEAT; P&ID reboiler H100, near grid L6; Plant summary 2023-24 p.102
- idx = 6 | name = TT100 | type = tie-in
  - Sources: P&ID on line Q106, grid L6; Pilot Plant Report Appendix B instrument list; Team check TT100 confirmed on Q106
- idx = 7 | name = TI100 | type = tie-in
  - Sources: P&ID grid K6
- idx = 8 | name = Q106 | type = inline
  - Sources: P&ID line Q106, grids L6 to L7; Team check Q106 returns from H100 to E100
- idx = 9 | name = E100 sump return nozzle from H100 (below chimney tray) | type = inline
  - Sources: Aspen v3 H100 return to stage 12 (stream S24); P&ID E100 sump, grid K7; Team check Q106 returns here
- idx = 10 | name = E100 | type = inline
  - Sources: Aspen v3 block E100 (RadFrac internals); P&ID column E100, grids F7 to K8
- idx = 11 | name = E100 sump outlet nozzle (to V110) | type = inline
  - Sources: P&ID E100 sump outlet to V110, grid K7; Pilot Plant Report Fig E.1/E.2 (stripping loop commissioning line-up)
- idx = 12 | name = V110 | type = inline
  - Sources: P&ID grid L7; Pilot Plant Report Fig E.1/E.2 (stripping loop commissioning line-up); Team check first valve after the sump outlet
- idx = 13 | name = V112 | type = inline
  - Sources: P&ID grid M8; Pilot Plant Report Fig E.1/E.2 (stripping loop commissioning line-up)
- idx = 14 | name = TT104 | type = tie-in
  - Sources: P&ID grid M8; Pilot Plant Report Appendix B instrument list
- idx = 15 | name = PT103 | type = tie-in
  - Sources: P&ID grid M8; Pilot Plant Report Appendix B instrument list
- idx = 16 | name = C100 | type = inline
  - Sources: Aspen v3 block C100; P&ID interchanger C100, grid M8 to M9; Pilot Plant Report section 3; Plant summary 2023-24 p.106
- idx = 17 | name = TE105 | type = tie-in
  - Sources: P&ID grid M9 (tagged TE105); Pilot Plant Report Appendix B lists it as TT105; Appendix D calls it TE105
- idx = 18 | name = V113a | type = inline
  - Sources: P&ID grid M9; Pilot Plant Report Fig E.1/E.2 (stripping loop commissioning line-up)
- idx = 19 | name = V113b | type = inline
  - Sources: P&ID grid M10; Pilot Plant Report Fig E.1/E.2 (stripping loop commissioning line-up)
- idx = 20 | name = J100 | type = inline
  - Sources: P&ID grid M10; Pilot Plant Report section 2.5 (pump trials)
- idx = 21 | name = TT106 | type = tie-in
  - Sources: P&ID grid L10; Pilot Plant Report Appendix B instrument list; Team check TT106 confirmed at J100
- idx = 22 | name = B101 | type = tie-in
  - Sources: P&ID differences row PT104 & B101 (M10); P&ID grid M10
- idx = 23 | name = PT104 | type = tie-in
  - Sources: P&ID grid L10; Pilot Plant Report Appendix B instrument list
- idx = 24 | name = PCV122 | type = inline
  - Sources: P&ID grid M10
- idx = 25 | name = V116 | type = inline
  - Sources: P&ID grid M11; Pilot Plant Report Fig E.1/E.2 (stripping loop commissioning line-up)
- idx = 26 | name = V117a | type = inline
  - Sources: P&ID grid M11; Pilot Plant Report Fig E.1/E.2 (stripping loop commissioning line-up) and Fig F.21
- idx = 27 | name = Z102 | type = inline
  - Sources: P&ID grid M11; Pilot Plant Report section E.3.6 and Fig F.21
- idx = 28 | name = PDT105 | type = tie-in
  - Sources: P&ID grid M11; Pilot Plant Report Appendix B instrument list
- idx = 29 | name = V117b | type = inline
  - Sources: P&ID grid M11; Pilot Plant Report Fig E.1/E.2 (stripping loop commissioning line-up) and Fig F.21; Team check order Z102 > V117b > V121
- idx = 30 | name = V121 | type = inline
  - Sources: P&ID grid M11; Pilot Plant Report Fig E.1/E.2 (stripping loop commissioning line-up); Team check order Z102 > V117b > V121
- idx = 31 | name = FT103 | type = inline
  - Sources: P&ID grid L12; Pilot Plant Report Appendix B instrument list
- idx = 32 | name = FI103 | type = tie-in
  - Sources: P&ID on J100
- idx = 33 | name = FT104 | type = inline
  - Sources: P&ID grid L12; Pilot Plant Report Appendix B instrument list
- idx = 34 | name = FI104 | type = tie-in
  - Sources: P&ID on J100
- idx = 35 | name = SOV125 | type = inline
  - Sources: P&ID grid L11; Pilot Plant Report Fig E.1/E.2 (stripping loop commissioning line-up)
- idx = 36 | name = H200a | type = inline
  - Sources: P&ID heater control section (grids J9 to J11); Pilot Plant Report start-up tables, heater H200a (J10, floor 2)
- idx = 36 | name = H200b | type = inline
  - Sources: P&ID heater control section (grids J9 to J11); Pilot Plant Report start-up tables, heater H200b (J11, floor 2)
- idx = 37 | name = TT213 | type = tie-in
  - Sources: P&ID grid H13; Pilot Plant Report Appendix B instrument list
- idx = 38 | name = TI213 | type = tie-in
  - Sources: P&ID heater control section (grids J9 to J11)
- idx = 39 | name = V403 | type = inline
  - Sources: P&ID differences row V402 & V403 (F8); P&ID grid F8; Pilot Plant Report Fig E.1/E.2 (stripping loop commissioning line-up)
- idx = 40 | name = V402 | type = inline
  - Sources: P&ID differences row V402 & V403 (F8); P&ID grid F8; Pilot Plant Report Fig E.1/E.2 (stripping loop commissioning line-up)
- idx = 41 | name = E100 top inlet nozzle after V402 (above top packed bed) | type = inline
  - Sources: Aspen v3 E100 feed to stage 1 (stream S10); P&ID E100 top, after V402, grid F8; Team check flow re-enters E100 after V402
- idx = 42 | name = E100 | type = inline
  - Sources: Aspen v3 block E100 (RadFrac internals); P&ID column E100, grids F7 to K8

## 02_between_Z102_and_FT103

**CQ2: Which inline items sit between Z102 and FT103?**

- tag = V117b
  - Sources: P&ID grid M11; Pilot Plant Report Fig E.1/E.2 (stripping loop commissioning line-up) and Fig F.21; Team check order Z102 > V117b > V121
- tag = V121
  - Sources: P&ID grid M11; Pilot Plant Report Fig E.1/E.2 (stripping loop commissioning line-up); Team check order Z102 > V117b > V121

## 03_loop_is_closed

**CQ3: Can solvent leaving E100 get back to E100 (is the loop closed)?**

- Answer: True

## 04_bypass_check

**CQ4: Is the Z102 bypass valve on the active flow path, and is it physically piped in?**

- valve = V120 | position = closed | onActivePath = false | pipedIn = true
  - Sources: P&ID grid L11; Pilot Plant Report Fig F.21 (Z102 bypass) and Fig E.1/E.2 (stripping loop commissioning line-up)

## 05_converged_cases

**CQ5: Which Aspen cases converged and are safe to use?**

- file = ABB_pilot_plant_final_3.apwz | saved = Wed Oct  2 19:47:24 2024 | recommended = true

## 06_problem_blocks

**CQ6: Which Aspen blocks have errors or warnings, and in which file?**

- file = ABB_pilot_plant_final_3.apwz | block = E100 | status = WARNING | msg = FEED PRESSURE IS LOWER THAN STAGE PRESSURE. | equipment = E100
  - Sources: Aspen v3 block E100 (RadFrac internals); P&ID column E100, grids F7 to K8
- file = ABB_pilot_plant_final_6_1_SA_validation.apwz | block = C100 | status = WARNING | msg = TEMPERATURE CROSSOVER DETECTED | equipment = C100
  - Sources: Aspen v3 block C100; P&ID interchanger C100, grid M8 to M9; Pilot Plant Report section 3; Plant summary 2023-24 p.106
- file = ABB_pilot_plant_final_6_1_SA_validation.apwz | block = E100 | status = ERROR | msg = RATESEP CALCULATIONS FAILED TO CONVERGE. | equipment = E100
  - Sources: Aspen v3 block E100 (RadFrac internals); P&ID column E100, grids F7 to K8
- file = ABB_pilot_plant_final_6_1_SA_validation.apwz | block = H100 | status = ERROR | msg = INVALID INPUT SPECIFICATIONS SEE TASC BROWSER FOR INFO. | equipment = H100
  - Sources: Aspen v3 blocks H100REAC and H100HEAT; P&ID reboiler H100, near grid L6; Plant summary 2023-24 p.102

## 07_heat_exchanger_performance

**CQ7: Duty, LMTD, UA and energy balance error for each exchanger in the recommended case**

- tag = C100 | duty = 17.4097 | lmtd = 33.87373 | ua = 513.9585 | U = 849.4315 | area = 0.6046091 | eff = 0.5065029 | err = 0.0
  - Sources: Aspen v3 block C100; P&ID interchanger C100, grid M8 to M9; Pilot Plant Report section 3; Plant summary 2023-24 p.106
- tag = H100 | duty = 115.5627 | lmtd = 32.8462 | ua = 3517.69 | U = 448.1082 | area = 61.6081 | eff = 0.9911752 | err = 0.03452101
  - Sources: Aspen v3 blocks H100REAC and H100HEAT; P&ID reboiler H100, near grid L6; Plant summary 2023-24 p.102
- tag = H200a | duty = 3.679129 | lmtd =  | ua =  | U =  | area =  | eff =  | err = 
  - Sources: P&ID heater control section (grids J9 to J11); Pilot Plant Report start-up tables, heater H200a (J10, floor 2)
- tag = H200b | duty = 3.679129 | lmtd =  | ua =  | U =  | area =  | eff =  | err = 
  - Sources: P&ID heater control section (grids J9 to J11); Pilot Plant Report start-up tables, heater H200b (J11, floor 2)

## 08_stripper_profile

**CQ8: Temperature, loading and CO2 desorbed down E100 (recommended case)**

- stage = 1 | kind = http://imperial.ac.uk/ccpp#GapStage | T = 111.9226 | loading = 0.5204874 | yCO2 = 0.0967975 | desorbed = 9.566305
- stage = 2 | kind = http://imperial.ac.uk/ccpp#PackedBedStage | T = 114.8846 | loading = 0.4273935 | yCO2 = 0.05851605 | desorbed = 10.08366
- stage = 3 | kind = http://imperial.ac.uk/ccpp#GapStage | T = 115.8889 | loading = 0.424186 | yCO2 = 0.03248234 | desorbed = 0.3360303
- stage = 4 | kind = http://imperial.ac.uk/ccpp#PackedBedStage | T = 115.8383 | loading = 0.3827547 | yCO2 = 0.03148757 | desorbed = 4.491062
- stage = 5 | kind = http://imperial.ac.uk/ccpp#GapStage | T = 116.3429 | loading = 0.3884042 | yCO2 = 0.02088353 | desorbed = -0.6229549
- stage = 6 | kind = http://imperial.ac.uk/ccpp#PackedBedStage | T = 116.1519 | loading = 0.3587759 | yCO2 = 0.02227368 | desorbed = 3.210313
- stage = 7 | kind = http://imperial.ac.uk/ccpp#GapStage | T = 116.5286 | loading = 0.3643244 | yCO2 = 0.01486032 | desorbed = -0.6120049
- stage = 8 | kind = http://imperial.ac.uk/ccpp#PackedBedStage | T = 116.3564 | loading = 0.3375357 | yCO2 = 0.01623252 | desorbed = 2.892606
- stage = 9 | kind = http://imperial.ac.uk/ccpp#GapStage | T = 116.6573 | loading = 0.3396177 | yCO2 = 0.00964358 | desorbed = -0.2401578
- stage = 10 | kind = http://imperial.ac.uk/ccpp#PackedBedStage | T = 116.5558 | loading = 0.3080509 | yCO2 = 0.01017093 | desorbed = 3.362936
- stage = 11 | kind = http://imperial.ac.uk/ccpp#GapStage | T = 116.8438 | loading = 0.3074551 | yCO2 = 0.002624339 | desorbed = 0.03088097
- stage = 12 | kind = http://imperial.ac.uk/ccpp#SumpStage | T = 118.2966 | loading = 0.299444 | yCO2 = 0.002552205 | desorbed = 1.15034

## 09_max_desorption_stage

**CQ9: On which stage does most CO2 transfer from liquid to vapour?**

- stage = 2 | desorbed = 10.08366

## 10_column_performance

**CQ10: CO2 stripped, loadings and specific reboiler duty for E100 in each case**

- file = ABB_pilot_plant_final_3.apwz | stripped = 33.64901 | product = 29.07729 | rich = 0.6089843 | lean = 0.2994449 | Q = 115.5627 | srd = 14.30758 | co2err = 0.0002511364
- file = ABB_pilot_plant_final_6_1_SA_validation.apwz | stripped = 0.06897691 | product = 0.06823842 | rich = 0.6405806 | lean = 0.6381258 | Q = 0.0 | srd = 0.0 | co2err = 0.01514457

## 11_hazop_for_Z102

**CQ11: What HAZOP deviations concern Z102, and what safeguards exist?**

- dev = HAZOP 7.3 | param = FLOW | guide = NO | cause = Blocked filter Z102 (MEA degradation products?) | safeguard = DP alarm PDAH 105
  - Sources: HAZOP 2010 element 7, item 3

## 12_equipment_without_hazop

**CQ12: Which inline equipment in the loop is not covered by any HAZOP element?**

- tag = H200a
  - Sources: P&ID heater control section (grids J9 to J11); Pilot Plant Report start-up tables, heater H200a (J10, floor 2)
- tag = H200b
  - Sources: P&ID heater control section (grids J9 to J11); Pilot Plant Report start-up tables, heater H200b (J11, floor 2)
- tag = SOV125
  - Sources: P&ID grid L11; Pilot Plant Report Fig E.1/E.2 (stripping loop commissioning line-up)

## 13_instruments_at_stage5

**CQ13: Which instruments sit at Aspen stage 5 of E100?**

- tag = TT300 | var = temperature | phase = liquid
  - Sources: P&ID grid G7; Pilot Plant Report Appendix B instrument list
- tag = TT301 | var = temperature | phase = vapour
  - Sources: P&ID grid G7; Pilot Plant Report Appendix B instrument list

## 14_protection_of_J100

**CQ14: What limits, trips and relief protect pump J100?**

- limit = J100_cavitation | variable = pump power | type = alarm | low =  | high = 55.0 | unit = % | source = REPORT E.3.3
  - Sources: Pilot Plant Report E.3.3
- limit = J100_flow_range | variable = volumetric flow | type = range | low = 10.79 | high = 19.7 | unit = L/min | source = P&ID
  - Sources: P&ID grid M10
- limit = J100_power_range | variable = pump power | type = range | low = 1.0 | high = 60.0 | unit = % | source = REPORT 2.5
  - Sources: Pilot Plant Report 2.5
- limit = LZAL102 | variable = level | type = trip | low = 1.0 | high =  | unit = % | source = REPORT 2.2; HAZOP 7.15, 11.15
  - Sources: HAZOP 2010 7.15, 11.15; Pilot Plant Report 2.2
- limit = RV101_set | variable = pressure | type = relief | low =  | high = 10.0 | unit = bar | source = P&ID; HAZOP 7.14
  - Sources: HAZOP 2010 7.14; P&ID grid L10
- limit = TZAH106 | variable = temperature | type = trip | low =  | high =  | unit = C | source = HAZOP 7.1
  - Sources: HAZOP 2010 7.1; HAZOP 2010 element 7, item 1

## 15_pid_discrepancies

**CQ15: Where does the P&ID differ from the as-built plant on this loop?**

- grid = E7 | tags = RV401 | drawn = No knockout drum on relief line | built = RV401 (E100) and RV400 (E101) relieve to knockout drum K403
  - Sources: P&ID differences row K403 (E7); P&ID grid F7
- grid = F8 | tags = V402, V403 | drawn = Valves on floor 4 | built = Valves on floor 3
  - Sources: P&ID differences row V402 & V403 (F8); P&ID grid F8; Pilot Plant Report Fig E.1/E.2 (stripping loop commissioning line-up)
- grid = L5 | tags = FCV110 | drawn = Labelled FCV110 | built = Labelled ZS110 on site
  - Sources: P&ID differences row FCV110 (L5); P&ID grid L5; Pilot Plant Report Fig E.1 and section F.5.4.3; Plant summary 2023-24 p.190 (control-loop table)
- grid = M10 | tags = B101, PT104 | drawn = PT104 tie-in before B101 | built = Stream passes B101 first, then PT104
  - Sources: P&ID differences row PT104 & B101 (M10); P&ID grid L10; P&ID grid M10; Pilot Plant Report Appendix B instrument list

## 16_valves_on_floor3

**CQ16: Which valves are on floor 3?**

- tag = V315
  - Sources: P&ID grid G10; Pilot Plant Report Fig E.1/E.2 (stripping loop commissioning line-up)
- tag = V316
  - Sources: P&ID grid G10; Pilot Plant Report Fig E.1/E.2 (stripping loop commissioning line-up)
- tag = V402
  - Sources: P&ID differences row V402 & V403 (F8); P&ID grid F8; Pilot Plant Report Fig E.1/E.2 (stripping loop commissioning line-up)
- tag = V403
  - Sources: P&ID differences row V402 & V403 (F8); P&ID grid F8; Pilot Plant Report Fig E.1/E.2 (stripping loop commissioning line-up)

## 17_unverified_values

**CQ17: Which numbers in the KG still need checking against the drawing?**

- limit = FT102_range | item = FT102 | high = 600.0 | unit = kg/h
  - Sources: P&ID grid M6; Pilot Plant Report Appendix B instrument list
- limit = FT103_range | item = FT103 | high = 12000.0 | unit = kg/h
  - Sources: P&ID grid L12; Pilot Plant Report Appendix B instrument list
- limit = FT104_range | item = FT104 | high = 1600.0 | unit = kg/h
  - Sources: P&ID grid L12; Pilot Plant Report Appendix B instrument list
- limit = PCV122_set | item = PCV122 | high = 8.0 | unit = bar
  - Sources: P&ID grid M10

## 18_compare_cases_C100

**CQ18: How does C100 compare between the two Aspen files?**

- file = ABB_pilot_plant_final_3.apwz | duty = 17.4097 | hin = 118.2711 | hout = 86.0 | cin = 51.29273 | cout = 85.21748 | lmtd = 33.87373 | cross = false
- file = ABB_pilot_plant_final_6_1_SA_validation.apwz | duty = 14.98997 | hin = 121.961 | hout = 70.52478 | cin = 69.53843 | cout = 115.2561 | lmtd = 2.98372 | cross = false

## 19_bypass_route

**CQ19: If Z102 is bypassed, which route does the solvent take and what does it skip?**

- from = V116 | via = V120 | to = V121 | skipped = V117a | state = closed
  - Sources: P&ID grid L11; P&ID grid M11; Pilot Plant Report Fig E.1/E.2 (stripping loop commissioning line-up); Pilot Plant Report Fig E.1/E.2 (stripping loop commissioning line-up) and Fig F.21; Pilot Plant Report Fig F.21 (Z102 bypass) and Fig E.1/E.2 (stripping loop commissioning line-up); Team check order Z102 > V117b > V121
- from = V116 | via = V120 | to = V121 | skipped = V117b | state = closed
  - Sources: P&ID grid L11; P&ID grid M11; Pilot Plant Report Fig E.1/E.2 (stripping loop commissioning line-up); Pilot Plant Report Fig E.1/E.2 (stripping loop commissioning line-up) and Fig F.21; Pilot Plant Report Fig F.21 (Z102 bypass) and Fig E.1/E.2 (stripping loop commissioning line-up); Team check order Z102 > V117b > V121
- from = V116 | via = V120 | to = V121 | skipped = Z102 | state = closed
  - Sources: P&ID grid L11; P&ID grid M11; Pilot Plant Report Fig E.1/E.2 (stripping loop commissioning line-up); Pilot Plant Report Fig F.21 (Z102 bypass) and Fig E.1/E.2 (stripping loop commissioning line-up); Pilot Plant Report section E.3.6 and Fig F.21; Team check order Z102 > V117b > V121

## 20_bypass_procedure

**CQ20: What are the steps to bypass Z102, and what triggers it?**

- order = 1 | instruction = Reduce J100 power by 20 % per minute until it reaches 15 % | item = J100 | position =  | trigger = PDT105 at or above 0.45 bar (Z102 blocked)
  - Sources: P&ID grid M10; Pilot Plant Report section 2.5 (pump trials)
- order = 2 | instruction = Manually open V120 | item = V120 | position = open | trigger = PDT105 at or above 0.45 bar (Z102 blocked)
  - Sources: P&ID grid L11; Pilot Plant Report Fig F.21 (Z102 bypass) and Fig E.1/E.2 (stripping loop commissioning line-up)
- order = 3 | instruction = Manually close V117a | item = V117a | position = closed | trigger = PDT105 at or above 0.45 bar (Z102 blocked)
  - Sources: P&ID grid M11; Pilot Plant Report Fig E.1/E.2 (stripping loop commissioning line-up) and Fig F.21
- order = 4 | instruction = Manually close V117b | item = V117b | position = closed | trigger = PDT105 at or above 0.45 bar (Z102 blocked)
  - Sources: P&ID grid M11; Pilot Plant Report Fig E.1/E.2 (stripping loop commissioning line-up) and Fig F.21; Team check order Z102 > V117b > V121
- order = 5 | instruction = Return J100 to the previous steady-state power | item = J100 | position =  | trigger = PDT105 at or above 0.45 bar (Z102 blocked)
  - Sources: P&ID grid M10; Pilot Plant Report section 2.5 (pump trials)
- order = 6 | instruction = Replace or clean Z102 | item = Z102 | position =  | trigger = PDT105 at or above 0.45 bar (Z102 blocked)
  - Sources: P&ID grid M11; Pilot Plant Report section E.3.6 and Fig F.21

## 21_heater_control

**CQ21: How is the temperature of MEA entering E100 controlled by the heaters?**

- loop = Temperature of MEA entering E100, heater leg A | sensor = TT213 | controller = TIC213a | final = H200a | mv = Thermal duty of H200a
  - Sources: P&ID grid H13; P&ID heater control section (grids J9 to J11); Pilot Plant Report Appendix B instrument list; Pilot Plant Report start-up tables, heater H200a (J10, floor 2); Plant summary 2023-24 p.190 (control-loop table)
- loop = Temperature of MEA entering E100, heater leg A | sensor = TT213 | controller = TY213a | final = H200a | mv = Thermal duty of H200a
  - Sources: P&ID grid H13; P&ID heater control section (grids J9 to J11); Pilot Plant Report Appendix B instrument list; Pilot Plant Report start-up tables, heater H200a (J10, floor 2)
- loop = Temperature of MEA entering E100, heater leg B | sensor = TT213 | controller = TIC213b | final = H200b | mv = Thermal duty of H200b
  - Sources: P&ID grid H13; P&ID heater control section (grids J9 to J11); Pilot Plant Report Appendix B instrument list; Pilot Plant Report start-up tables, heater H200b (J11, floor 2); Plant summary 2023-24 p.190 (control-loop table)
- loop = Temperature of MEA entering E100, heater leg B | sensor = TT213 | controller = TY213b | final = H200b | mv = Thermal duty of H200b
  - Sources: P&ID grid H13; P&ID heater control section (grids J9 to J11); Pilot Plant Report Appendix B instrument list; Pilot Plant Report start-up tables, heater H200b (J11, floor 2)

## 22_lineup_open_valves

**CQ22: Which valves must be open for the stripping loop line-up?**

- tag = SOV125
  - Sources: P&ID grid L11; Pilot Plant Report Fig E.1/E.2 (stripping loop commissioning line-up)
- tag = V110
  - Sources: P&ID grid L7; Pilot Plant Report Fig E.1/E.2 (stripping loop commissioning line-up); Team check first valve after the sump outlet
- tag = V112
  - Sources: P&ID grid M8; Pilot Plant Report Fig E.1/E.2 (stripping loop commissioning line-up)
- tag = V113a
  - Sources: P&ID grid M9; Pilot Plant Report Fig E.1/E.2 (stripping loop commissioning line-up)
- tag = V113b
  - Sources: P&ID grid M10; Pilot Plant Report Fig E.1/E.2 (stripping loop commissioning line-up)
- tag = V116
  - Sources: P&ID grid M11; Pilot Plant Report Fig E.1/E.2 (stripping loop commissioning line-up)
- tag = V117a
  - Sources: P&ID grid M11; Pilot Plant Report Fig E.1/E.2 (stripping loop commissioning line-up) and Fig F.21
- tag = V117b
  - Sources: P&ID grid M11; Pilot Plant Report Fig E.1/E.2 (stripping loop commissioning line-up) and Fig F.21; Team check order Z102 > V117b > V121
- tag = V121
  - Sources: P&ID grid M11; Pilot Plant Report Fig E.1/E.2 (stripping loop commissioning line-up); Team check order Z102 > V117b > V121
- tag = V402
  - Sources: P&ID differences row V402 & V403 (F8); P&ID grid F8; Pilot Plant Report Fig E.1/E.2 (stripping loop commissioning line-up)
- tag = V403
  - Sources: P&ID differences row V402 & V403 (F8); P&ID grid F8; Pilot Plant Report Fig E.1/E.2 (stripping loop commissioning line-up)

## 23_reboiler_circuit

**CQ23: What does the solvent pass through between leaving E100 and returning from H100?**

- idx = 0 | name = E100 draw-off nozzle below TT103 (chimney tray, to H100)
- idx = 1 | name = FT102
  - Sources: P&ID grid M6; Pilot Plant Report Appendix B instrument list
- idx = 2 | name = Q105
  - Sources: P&ID line Q105, near grid M6; Team check reboiler circuit trace
- idx = 3 | name = H100
  - Sources: Aspen v3 blocks H100REAC and H100HEAT; P&ID reboiler H100, near grid L6; Plant summary 2023-24 p.102
- idx = 4 | name = Q106
  - Sources: P&ID line Q106, grids L6 to L7; Team check Q106 returns from H100 to E100
- idx = 5 | name = E100 sump return nozzle from H100 (below chimney tray)
  - Sources: Aspen v3 H100 return to stage 12 (stream S24); P&ID E100 sump, grid K7; Team check Q106 returns here

## 24_cascade_and_interlocks

**CQ24: Which control loops are cascaded, and which interlocks can trip each heater?**

- kind = cascade | name = Temperature of MEA leaving H100 (cascade master) | detail = Steam flow to H100 (cascade slave)
  - Sources: Pilot Plant Report D.4.4.c; Plant summary 2023-24 p.190
- kind = interlock | name = H200a high-high temperature trip | detail = H200a
  - Sources: P&ID heater control section (grids J9 to J11); Pilot Plant Report start-up tables, heater H200a (J10, floor 2)
- kind = interlock | name = H200b high-high temperature trip | detail = H200b
  - Sources: P&ID heater control section (grids J9 to J11); Pilot Plant Report start-up tables, heater H200b (J11, floor 2)
- kind = interlock | name = Heater outlet high temperature (TZH213) | detail = H200a
  - Sources: P&ID heater control section (grids J9 to J11); Pilot Plant Report start-up tables, heater H200a (J10, floor 2)
- kind = interlock | name = Heater outlet high temperature (TZH213) | detail = H200b
  - Sources: P&ID heater control section (grids J9 to J11); Pilot Plant Report start-up tables, heater H200b (J11, floor 2)

## 25_lineup_conflicts

**CQ25: Does any valve's stored position contradict the stripping loop line-up procedure? (expect none)**

- (no rows)

## 26_closed_valves_on_flow_path

**CQ26: Is any valve on the active flow path closed, which would block the loop? (expect none)**

- (no rows)

## 27_return_point

**CQ27: Where does the stripping loop re-enter E100 after V402?**

- nozzle = E100 top inlet nozzle after V402 (above top packed bed) | stage = 1 | stageKind = http://imperial.ac.uk/ccpp#GapStage | loopStage = 1
  - Sources: Aspen v3 E100 feed to stage 1 (stream S10); P&ID E100 top, after V402, grid F8; Team check flow re-enters E100 after V402
