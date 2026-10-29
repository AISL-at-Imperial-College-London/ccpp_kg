# Overhead and reflux KG: 100-question run

PASS 100, FAIL 0, QUERY ERROR 0

## F01 [Flow] PASS

**Where does the E100 overhead vapour go first?**

- Expected: C400
- KG: C400

## F02 [Flow] PASS

**What does C400 feed?**

- Expected: K401
- KG: K401

## F03 [Flow] PASS

**What does K401 feed (liquid side)?**

- Expected: J300
- KG: J300

## F04 [Flow] PASS

**What does J300 discharge into?**

- Expected: PCV302
- KG: PCV302

## F05 [Flow] PASS

**What does PCV302 feed?**

- Expected: FT305
- KG: FT305

## F06 [Flow] PASS

**Where does the reflux join the solvent line?**

- Expected: V403
- KG: V403

## F07 [Flow] PASS

**What feeds V403 (heaters and reflux)?**

- Expected: H200a, H200b, FT305
- KG: FT305, H200b, H200a

## F08 [Flow] PASS

**What feeds K401?**

- Expected: C400
- KG: C400

## F09 [Flow] PASS

**What feeds J300?**

- Expected: K401
- KG: K401

## F10 [Flow] PASS

**Does the overhead vapour get back to E100 as reflux?**

- Expected: true
- KG: true

## F11 [Flow] PASS

**Is the overhead loop closed (J300 round to C400)?**

- Expected: true
- KG: true

## F12 [Flow] PASS

**Does K401 feed PCV302 directly?**

- Expected: false
- KG: false

## F13 [Flow] PASS

**Can condensate from C400 reach J100 through E100?**

- Expected: true
- KG: true

## F14 [Flow] PASS

**Is B300 on the flow path (does it feed PCV302)?**

- Expected: false
- KG: false

## P01 [Piping] PASS

**What is J300 piped to?**

- Expected: PCV302, RV300, B300
- KG: B300, PCV302, RV300

## P02 [Piping] PASS

**What is PCV302 piped to?**

- Expected: FT305, V317
- KG: FT305, V317

## P03 [Piping] PASS

**Which tagged item is K401 piped to?**

- Expected: J300
- KG: J300

## P04 [Piping] PASS

**What is FT305 piped to?**

- Expected: V403
- KG: V403

## P05 [Piping] PASS

**What is piped into V403?**

- Expected: H200a, H200b, FT305
- KG: FT305, H200b, H200a

## P06 [Piping] PASS

**What is C400 piped to?**

- Expected: K401
- KG: K401

## P07 [Piping] PASS

**Which equipment is the gas outlet nozzle on?**

- Expected: K401
- KG: K401

## P08 [Piping] PASS

**Which equipment is the overhead nozzle on?**

- Expected: E100
- KG: E100

## E01 [Equipment] PASS

**Which condenser is there?**

- Expected: C400
- KG: C400

## E02 [Equipment] PASS

**Which knockout drum is there?**

- Expected: K401
- KG: K401

## E03 [Equipment] PASS

**Which pump does this piece add?**

- Expected: J300
- KG: J300

## E04 [Equipment] PASS

**Which pulsation dampener does this piece add?**

- Expected: B300
- KG: B300

## E05 [Equipment] PASS

**Which relief valve does this piece add?**

- Expected: RV300
- KG: RV300

## E06 [Equipment] PASS

**Which pressure control valve does this piece add?**

- Expected: PCV302
- KG: PCV302

## E07 [Equipment] PASS

**Which flow control valve does this piece add?**

- Expected: FCV401
- KG: FCV401

## E08 [Equipment] PASS

**Which floor is J300 on?**

- Expected: 3
- KG: 3

## E09 [Equipment] PASS

**What grid is J300 at?**

- Expected: G10
- KG: G10

## E10 [Equipment] PASS

**Which floor is C400 on?**

- Expected: 4
- KG: 4

## V01 [Valves] PASS

**What grid is PCV302 at?**

- Expected: G9
- KG: G9

## V02 [Valves] PASS

**Which floor is PCV302 on?**

- Expected: 3
- KG: 3

## V03 [Valves] PASS

**What grid is RV300 at?**

- Expected: G10
- KG: G10

## V04 [Valves] PASS

**Is V317 normally open or closed?**

- Expected: closed
- KG: closed

## V05 [Valves] PASS

**What type of valve is V317?**

- Expected: ball
- KG: ball

## V06 [Valves] PASS

**What grid is V317 at?**

- Expected: H9
- KG: H9

## V07 [Valves] PASS

**What grid is FCV401 at?**

- Expected: C12
- KG: C12

## V08 [Valves] PASS

**Which floor is FCV401 on?**

- Expected: 4
- KG: 4

## I01 [Instruments] PASS

**What type of transmitter is LT401?**

- Expected: differential pressure transmitter
- KG: differential pressure transmitter

## I02 [Instruments] PASS

**What signal does LT401 use?**

- Expected: 4-20mA
- KG: 4-20mA

## I03 [Instruments] PASS

**What grid is LT401 at?**

- Expected: F10
- KG: F10

## I04 [Instruments] PASS

**What signal does TT310 use?**

- Expected: 4-20mA
- KG: 4-20mA

## I05 [Instruments] PASS

**What grid is TT310 at?**

- Expected: G9
- KG: G9

## I06 [Instruments] PASS

**What grid is TT410 at?**

- Expected: C15
- KG: C15

## I07 [Instruments] PASS

**What signal does TT410 use?**

- Expected: Fieldbus
- KG: Fieldbus

## I08 [Instruments] PASS

**What grid is LSHH400 at?**

- Expected: E10
- KG: E10

## I09 [Instruments] PASS

**What does LSHH400 monitor?**

- Expected: K401
- KG: K401

## I10 [Instruments] PASS

**Which instruments monitor K401?**

- Expected: LSHH400, LT401, PT402
- KG: PT402, LSHH400, LT401

## I11 [Instruments] PASS

**Which instruments monitor J300?**

- Expected: TT310, FT305, TT309
- KG: TT310, TT309, FT305

## I12 [Instruments] PASS

**Which instruments monitor C400?**

- Expected: TT410, FT402, FI401, PT401
- KG: FI401, TT410, PT401, FT402

## I13 [Instruments] PASS

**What type of meter is FT305?**

- Expected: Coriolis mass flow meter
- KG: Coriolis mass flow meter

## I14 [Instruments] PASS

**What grid is TT309 at?**

- Expected: F9
- KG: F9

## I15 [Instruments] PASS

**What grid is PT401 at?**

- Expected: C8
- KG: C8

## I16 [Instruments] PASS

**What grid is FI401 at?**

- Expected: C14
- KG: C14

## C01 [Control] PASS

**Which controllers act on J300?**

- Expected: LIC401, SIC300
- KG: LIC401, SIC300

## C02 [Control] PASS

**Which sensor does the K401 level loop use?**

- Expected: LT401
- KG: LT401

## C03 [Control] PASS

**What does the K401 level loop adjust?**

- Expected: J300
- KG: J300

## C04 [Control] PASS

**Which sensor does the C400 temperature loop use?**

- Expected: TT410
- KG: TT410

## C05 [Control] PASS

**Which controller is the C400 temperature master?**

- Expected: TIC410
- KG: TIC410

## C06 [Control] PASS

**Which sensor does the C400 cooling water loop use?**

- Expected: FT402
- KG: FT402

## C07 [Control] PASS

**Which valve does the C400 cooling water loop move?**

- Expected: FCV401
- KG: FCV401

## C08 [Control] PASS

**Which loop is the C400 temperature loop master of?**

- Expected: CL_C400_cooling_water
- KG: CL_C400_cooling_water

## C09 [Control] PASS

**Which controllers act on FCV401?**

- Expected: TIC410, FIC402
- KG: FIC402, TIC410

## C10 [Control] PASS

**Which valve sets the stripper pressure?**

- Expected: PCV119
- KG: PCV119

## L01 [Limits] PASS

**What is RV300 set to?**

- Expected: 10
- KG: 10.0

## L02 [Limits] PASS

**What is PCV302 set to?**

- Expected: 8
- KG: 8.0

## L03 [Limits] PASS

**What pressure does B300 operate at?**

- Expected: 3
- KG: 3.0

## L04 [Limits] PASS

**Which alarm detects a blocked K401 demister?**

- Expected: PDAH_K401_demister
- KG: PDAH_K401_demister

## L05 [Limits] PASS

**Which alarm detects low cooling water to C400?**

- Expected: FAL_FT402
- KG: FAL_FT402

## L06 [Limits] PASS

**Which alarm is on LSHH400?**

- Expected: LZAH_K401
- KG: LZAH_K401

## L07 [Limits] PASS

**Which alarm is on LT401?**

- Expected: LAL_K401
- KG: LAL_K401

## L08 [Limits] PASS

**What does RV300 protect?**

- Expected: J300
- KG: J300

## L09 [Limits] PASS

**What unit is the RV300 setting in?**

- Expected: bar
- KG: bar

## D01 [Discrepancies] PASS

**Which discrepancy concerns B300?**

- Expected: discrepancy_B300_pressure
- KG: discrepancy_B300_pressure

## D02 [Discrepancies] PASS

**Which discrepancy concerns TT309?**

- Expected: discrepancy_TT309_FT305_order
- KG: discrepancy_TT309_FT305_order

## D03 [Discrepancies] PASS

**Which discrepancy concerns LSHH400?**

- Expected: discrepancy_LSHH400_location
- KG: discrepancy_LSHH400_location

## D04 [Discrepancies] PASS

**What does the plant really have for B300?**

- Expected: B300 operates at 3 bar
- KG: B300 operates at 3 bar

## H01 [HAZOP] PASS

**Which HAZOP element covers C400?**

- Expected: 12
- KG: 12

## H02 [HAZOP] PASS

**Which HAZOP element covers K401?**

- Expected: 12
- KG: 12

## H03 [HAZOP] PASS

**Which HAZOP element covers J300?**

- Expected: 12
- KG: 12

## H04 [HAZOP] PASS

**Which HAZOP deviation concerns PT402?**

- Expected: HAZOP_12_02
- KG: HAZOP_12_02

## H05 [HAZOP] PASS

**Which HAZOP deviation concerns FT402 (FT401 in 2010)?**

- Expected: HAZOP_12_07
- KG: HAZOP_12_07

## H06 [HAZOP] PASS

**Which HAZOP deviations concern K401 (K400/K401 in 2010)?**

- Expected: HAZOP_12_02, HAZOP_12_08, HAZOP_12_09
- KG: HAZOP_12_02, HAZOP_12_08, HAZOP_12_09

## H07 [HAZOP] PASS

**Which HAZOP deviations concern C400 (C300 in 2010)?**

- Expected: HAZOP_12_03, HAZOP_12_07
- KG: HAZOP_12_03, HAZOP_12_07

## H08 [HAZOP] PASS

**Does HAZOP 12.2 recommend a PDAH?**

- Expected: true
- KG: true

## M01 [HMT] PASS

**Is the C400 duty above 80 kW (recommended case)?**

- Expected: true
- KG: true

## M02 [HMT] PASS

**Does C400 cool the gas below 60 C?**

- Expected: true
- KG: true

## M03 [HMT] PASS

**Is the off-gas more than 85 % CO2 by mass?**

- Expected: true
- KG: true

## M04 [HMT] PASS

**Is the reflux ratio above 3?**

- Expected: true
- KG: true

## M05 [HMT] PASS

**Is more liquid condensed than gas sent on?**

- Expected: true
- KG: true

## O01 [Open items] PASS

**Which open item concerns V317?**

- Expected: OOI02
- KG: OOI02

## O02 [Open items] PASS

**Which open items concern K401?**

- Expected: OOI01, OOI05, OOI06
- KG: OOI01, OOI05, OOI06

## O03 [Open items] PASS

**How many open items did this piece raise?**

- Expected: 6
- KG: 6

## O04 [Open items] PASS

**Which open item concerns J300?**

- Expected: OOI04
- KG: OOI04

## X01 [Join] PASS

**Is E100 physically connected to K401?**

- Expected: true
- KG: true

## X02 [Join] PASS

**What feeds V402?**

- Expected: V403
- KG: V403

## X03 [Join] PASS

**Does the overhead loop pass through V403?**

- Expected: true
- KG: true

## X04 [Join] PASS

**Does the overhead loop pass through PCV302?**

- Expected: true
- KG: true
