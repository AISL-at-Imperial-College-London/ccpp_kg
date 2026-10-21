# Stripping loop KG: 100-question run

Questions asked: 100

| Category | PASS | FAIL | ANSWERED | NO ANSWER | GAP CONFIRMED | ANSWERED (gap probe) | QUERY ERROR |
|---|---|---|---|---|---|---|---|
| Routes | 13 | 0 | 1 | 0 | 1 | 0 | 0 |
| Topology | 12 | 0 | 0 | 0 | 0 | 0 | 0 |
| Valves | 10 | 0 | 0 | 0 | 0 | 0 | 0 |
| Instruments | 9 | 0 | 1 | 0 | 0 | 0 | 0 |
| Control | 7 | 0 | 0 | 0 | 0 | 1 | 0 |
| Limits | 10 | 0 | 0 | 0 | 1 | 0 | 0 |
| Procedures | 4 | 0 | 1 | 0 | 1 | 1 | 0 |
| HAZOP | 2 | 0 | 1 | 0 | 1 | 0 | 0 |
| Aspen/HMT | 4 | 0 | 4 | 0 | 1 | 0 | 0 |
| Grounding | 1 | 2 | 2 | 0 | 0 | 0 | 0 |
| Gap probes | 0 | 0 | 0 | 0 | 7 | 2 | 0 |
| **Total** | 72 | 2 | 10 | 0 | 12 | 4 | 0 |

## R01 [Routes] PASS

**How many route scenarios does the stripping loop have?**

- Expected: 4
- 4

## R02 [Routes] PASS

**Which route is the normal line-up?**

- Expected: Route_A_top_filter
- Route_A_top_filter

## R03 [Routes] PASS

**Which routes bypass Z102?**

- Expected: Route_B_top_bypass, Route_D_side_bypass
- Route_B_top_bypass
- Route_D_side_bypass

## R04 [Routes] PASS

**Which routes return to the side of E100 (stage 3)?**

- Expected: Route_C_side_filter, Route_D_side_bypass
- Route_C_side_filter
- Route_D_side_bypass

## R05 [Routes] PASS

**Which valve is open for the side return but closed in the normal route?**

- Expected: V309
- V309

## R06 [Routes] PASS

**In route D, which key valves are closed?**

- Expected: V117a, V117b, V403, V402, V318, V302, SDV123
- SDV123
- V117a
- V117b
- V302
- V318
- V402
- V403

## R07 [Routes] PASS

**In route C, which tagged items does the solvent pass after SDV125?**

- Expected: H200a, H200b, V309, E100
- H200a
- H200b
- E100
- V309

## R08 [Routes] PASS

**Does route B pass through Z102?**

- Expected: false
- false

## R10 [Routes] PASS

**Does route D pass through both V120 and V309?**

- Expected: true
- true

## R12 [Routes] PASS

**Which instruments sit at the stage where the side return enters?**

- Expected: TT302, TT303
- TT302
- TT303

## R13 [Routes] PASS

**Which tagged items are in route A but not route C?**

- Expected: V403, V402
- V403
- V402

## R14 [Routes] ANSWERED

**Is the side return simulated in Aspen?**

- Not simulated in Aspen: both Aspen models return the stream to stage 1, so the stage results describe the top return only.

## R15 [Routes] PASS

**What triggers moving from route A to route B?**

- Expected: PDT105 at or above 0.45 bar (Z102 blocked)
- PDT105 at or above 0.45 bar (Z102 blocked)

## R19 [Routes] PASS

**Is V309 covered by the HAZOP?**

- Expected: false
- false

## R20 [Routes] GAP CONFIRMED

**What is the rich loading for the side-return route?**

- (no rows)

## T01 [Topology] PASS

**What does Z102 feed directly into?**

- Expected: V117b
- V117b

## T02 [Topology] PASS

**What feeds directly into Z102?**

- Expected: V117a
- V117a

## T03 [Topology] PASS

**What feeds directly into J100?**

- Expected: V113b
- V113b

## T06 [Topology] PASS

**What does H100 feed directly into?**

- Expected: Q106
- Q106

## T08 [Topology] PASS

**Is V121 downstream of Z102 on the active path?**

- Expected: true
- true

## T09 [Topology] PASS

**Is SDV123 on the active flow path?**

- Expected: false
- false

## T10 [Topology] PASS

**What does SDV125 feed directly into?**

- Expected: H200a, H200b
- H200a
- H200b

## T12 [Topology] PASS

**Which items is V116 physically piped to?**

- Expected: V117a, V120
- V117a
- V120

## T13 [Topology] PASS

**Where can flow physically go after H200a?**

- Expected: V403, V309
- V309
- V403

## T14 [Topology] PASS

**How many inline steps does the normal loop have?**

- Expected: 29
- 29

## T15 [Topology] PASS

**What is the first valve after the E100 sump outlet?**

- Expected: V110
- V110

## T18 [Topology] PASS

**Can solvent leaving E100 get back to E100?**

- Expected: true
- true

## V01 [Valves] PASS

**Which valves are check valves?**

- Expected: V112, V113a
- V112
- V113a

## V02 [Valves] PASS

**Which valves are shutdown valves?**

- Expected: SDV123, SDV125
- SDV123
- SDV125

## V03 [Valves] PASS

**What type of valve is V302?**

- Expected: needle
- needle

## V05 [Valves] PASS

**Which valves on floor 1 are closed in the stripping loop line-up?**

- Expected: FCV110, RV101, SDV123, V101, V102, V105, V106, V109, V120
- V109
- V102
- V105
- V106
- V101
- RV101
- SDV123
- FCV110
- V120

## V06 [Valves] PASS

**Which valve bypasses Z102?**

- Expected: V120
- V120

## V07 [Valves] PASS

**Which valve protects J100?**

- Expected: RV101
- RV101

## V08 [Valves] PASS

**What is the set pressure of the relief valve protecting J100?**

- Expected: 10
- 10.0

## V09 [Valves] PASS

**Which valves are on floor 3?**

- Expected: V217, V302, V309, V315, V316, V318, V402, V403
- V316
- V217
- V315
- V302
- V318
- V309
- V402
- V403

## V11 [Valves] PASS

**Which valve is named ZS110 on site?**

- Expected: FCV110
- FCV110

## V12 [Valves] PASS

**Which valves on the flow route are not ball valves?**

- Expected: V112, V113a, PCV122, SDV125
- SDV125
- PCV122
- V112
- V113a

## I01 [Instruments] PASS

**Which instrument measures pressure drop across Z102?**

- Expected: PDT105
- PDT105

## I02 [Instruments] PASS

**What type of sensor is FT102?**

- Expected: Coriolis mass flow meter
- Coriolis mass flow meter

## I04 [Instruments] PASS

**Which instruments use a 4-20mA signal?**

- Expected: FT103, TT106, TT202, TT203, TT212a, TT212b, TT300, TT301
- TT202
- TT203
- TT300
- TT301
- TT212a
- TT212b
- TT106
- FT103

## I05 [Instruments] PASS

**Which instruments monitor H100?**

- Expected: DI100, FI102, FT100, FT101, FT102, TI100, TT100
- FT101
- FT100
- DI100
- FI102
- TI100
- TT100
- FT102

## I06 [Instruments] PASS

**Which instruments sit at stage 5?**

- Expected: TT300, TT301
- TT300
- TT301

## I07 [Instruments] PASS

**Which instruments measure in the vapour phase?**

- Expected: PSHH400, TT201, TT203, TT301, TT303, TT401
- PSHH400
- TT201
- TT203
- TT301
- TT303
- TT401

## I09 [Instruments] PASS

**Which instruments are K-type thermocouples?**

- Expected: TT212a, TT212b
- TT212a
- TT212b

## I10 [Instruments] PASS

**Which instrument measures liquid temperature at the top of E100?**

- Expected: TT400
- TT400

## I11 [Instruments] PASS

**Which instruments monitor J100?**

- Expected: FI103, FI104, FT103, FT104, PT104, TT106
- FI103
- FI104
- TT106
- PT104
- FT103
- FT104

## I13 [Instruments] ANSWERED

**What is TE105 called in the report?**

- Pilot Plant Report Appendix B lists it as TT105; Appendix D calls it TE105

## C01 [Control] PASS

**Which controllers act on J100?**

- Expected: FIC103, FIC104, HS100, SIC100
- HS100
- FIC103
- FIC104
- SIC100

## C02 [Control] PASS

**What does the J100 flow loop control?**

- Expected: MEA flowrate leaving E100
- MEA flowrate leaving E100

## C04 [Control] PASS

**Which controllers drive H200b?**

- Expected: TIC213b, TY213b
- TIC213b
- TY213b

## C05 [Control] PASS

**Which control loop is a cascade master?**

- Expected: CL_H100_temperature_master
- CL_H100_temperature_master

## C06 [Control] PASS

**What does the H100 steam loop adjust?**

- Expected: FCV110
- FCV110

## C07 [Control] PASS

**Which interlocks trip J100?**

- Expected: IL_E100_level_HH, IL_E100_level_LL
- IL_E100_level_HH
- IL_E100_level_LL

## C09 [Control] PASS

**How many control loops are modelled?**

- Expected: 6
- 6

## C10 [Control] ANSWERED (gap probe)

**What setpoint does TIC213a hold during normal running?**

- 25.0

## L01 [Limits] PASS

**What is PCV122 set to?**

- Expected: 8
- 8.0

## L04 [Limits] PASS

**At what PDT105 reading is Z102 treated as blocked?**

- Expected: 0.45
- 0.45

## L05 [Limits] PASS

**At what LT101 level is the low alarm?**

- Expected: 5
- 5.0

## L06 [Limits] PASS

**What is the lower end of the LT101 operating window?**

- Expected: 10
- 10.0

## L07 [Limits] PASS

**Above what pump power does J100 cavitate?**

- Expected: 55
- 55.0

## L08 [Limits] PASS

**What is the maximum safe J100 pump power?**

- Expected: 60
- 60.0

## L09 [Limits] PASS

**Are any operating limits still unverified?**

- Expected: (no rows)
- (no rows)

## L10 [Limits] PASS

**At what pressure does PSHH400 trip?**

- Expected: 2
- 2.0

## L11 [Limits] PASS

**What is the maximum steam flow to H100?**

- Expected: 140
- 140.0

## L12 [Limits] PASS

**Which limits have no value recorded?**

- Expected: LZAH100, TSHH212a, TSHH212b, TZAH106
- LZAH100
- TSHH212a
- TSHH212b
- TZAH106

## L14 [Limits] GAP CONFIRMED

**What temperature trips H200a?**

- (no rows)

## P01 [Procedures] PASS

**How many steps are in the Z102 bypass procedure?**

- Expected: 6
- 6

## P02 [Procedures] PASS

**What is the first step of the Z102 bypass?**

- Expected: Reduce J100 power by 20 % per minute until it reaches 15 %
- Reduce J100 power by 20 % per minute until it reaches 15 %

## P03 [Procedures] PASS

**Which valves are closed during the Z102 bypass?**

- Expected: V117a, V117b
- V117a
- V117b

## P04 [Procedures] PASS

**Which valves must be closed for the stripping loop line-up?**

- Expected: FCV110, SDV123, V101, V102, V105, V106, V120, V302, V309, V315, V316, V318
- V120
- SDV123
- V315
- V316
- FCV110
- V101
- V102
- V105
- V106
- V309
- V318
- V302

## P06 [Procedures] ANSWERED

**What should I do if PDT105 reads 0.5 bar?**

- Reduce J100 power by 20 % per minute until it reaches 15 %
- Manually open V120
- Manually close V117a
- Manually close V117b
- Return J100 to the previous steady-state power
- Replace or clean Z102

## P07 [Procedures] ANSWERED (gap probe)

**What is the procedure to switch to the side return (route C)?**

- PROC_switch_to_side_return

## P08 [Procedures] GAP CONFIRMED

**How long does the Z102 bypass procedure take?**

- (no rows)

## H02 [HAZOP] PASS

**Which HAZOP elements cover H100?**

- Expected: 11, 13
- 13
- 11

## H03 [HAZOP] PASS

**Which inline equipment in the normal loop has no HAZOP coverage?**

- Expected: H200a, H200b, SDV125
- SDV125
- H200a
- H200b

## H04 [HAZOP] ANSWERED

**What safeguard does the HAZOP give for no flow due to a blocked filter?**

- DP alarm PDAH 105

## H05 [HAZOP] GAP CONFIRMED

**What does the HAZOP say about the H200 heaters?**

- (no rows)

## A01 [Aspen/HMT] PASS

**Which Aspen file is recommended?**

- Expected: ABB_pilot_plant_final_3.apwz
- ABB_pilot_plant_final_3.apwz

## A02 [Aspen/HMT] ANSWERED

**What is the C100 duty in the recommended case?**

- 17.4097

## A03 [Aspen/HMT] ANSWERED

**What is the H100 duty in the recommended case?**

- 115.5627

## A04 [Aspen/HMT] PASS

**On which stage is most CO2 desorbed?**

- Expected: 2
- 2

## A07 [Aspen/HMT] PASS

**Which exchangers show a temperature cross?**

- Expected: C100
- C100

## A08 [Aspen/HMT] PASS

**Which Aspen blocks failed?**

- Expected: E100, H100
- H100
- E100

## A09 [Aspen/HMT] ANSWERED

**What is the specific reboiler duty?**

- 14.30758

## A10 [Aspen/HMT] ANSWERED

**What MEA concentration is in the lean solvent?**

- 0.272504

## A11 [Aspen/HMT] GAP CONFIRMED

**What heat duty do H200a/b need during the stripping loop test?**

- (no rows)

## G01 [Grounding] FAIL

**How many source documents are in the KG?**

- Expected: 9
- 10

## G02 [Grounding] FAIL

**Which facts cite HAZOP recommendation M4?**

- Expected: limit_PSHH116_set, limit_PSHH400_set
- PSHH116
- PSHH400
- limit_PSHH116_set
- limit_PSHH400_set

## G03 [Grounding] PASS

**Is any plant item missing a citation?**

- Expected: (no rows)
- (no rows)

## G04 [Grounding] ANSWERED

**Which plant items are cited only to the P&ID?**

- TSHH212a
- TSHH212b
- HS200a
- HS200b
- TZAHH212a
- TZAHH212b
- TZH213
- TY213a
- TY213b

## G05 [Grounding] ANSWERED

**How many citations come from the team's checks?**

- 70

## S01 [Gap probes] GAP CONFIRMED

**What is the power rating of H200a?**

- (no rows)

## S02 [Gap probes] GAP CONFIRMED

**What electrical supply or breaker feeds H200a?**

- (no rows)

## S03 [Gap probes] ANSWERED (gap probe)

**What is the design pressure of E100?**

- Designed for sub-atmospheric pressure (vacuum), per HAZOP element 11 item 10. Design pressure value not documented.

## S05 [Gap probes] GAP CONFIRMED

**What is the hold-up volume of the E100 sump?**

- (no rows)

## S06 [Gap probes] ANSWERED (gap probe)

**Where is V217 and what does it do?**

- V217

## S07 [Gap probes] GAP CONFIRMED

**How much reflux from J300 joins the loop?**

- (no rows)

## S08 [Gap probes] GAP CONFIRMED

**Who is authorised to open V120?**

- (no rows)

## S10 [Gap probes] GAP CONFIRMED

**What happens to the E100 level if J100 trips?**

- (no rows)

## S12 [Gap probes] GAP CONFIRMED

**Are V110, V112, V113a and V113b locked?**

- (no rows)
