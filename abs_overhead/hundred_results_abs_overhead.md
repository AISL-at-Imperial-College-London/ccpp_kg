# Absorber overhead KG: 100-question run

PASS 100, FAIL 0, QUERY ERROR 0

## F01 [Flow] PASS

**Where does the gas go after leaving the top of E101?**

- Expected: K402
- KG: K402

## F02 [Flow] PASS

**What does K402 feed on the vent route?**

- Expected: PCV300
- KG: PCV300

## F03 [Flow] PASS

**What does PCV300 feed?**

- Expected: VENT_E101
- KG: VENT_E101

## F04 [Flow] PASS

**What feeds PCV300?**

- Expected: K402
- KG: K402

## F05 [Flow] PASS

**What feeds the absorber vent?**

- Expected: PCV300
- KG: PCV300

## F06 [Flow] PASS

**Does gas from the top of E101 reach the vent?**

- Expected: true
- KG: true

## F07 [Flow] PASS

**Does K402 feed the vent directly (bypassing PCV300)?**

- Expected: false
- KG: false

## F08 [Flow] PASS

**Does vented gas come back to E101?**

- Expected: false
- KG: false

## F09 [Flow] PASS

**Does E101 feed its overhead nozzle directly?**

- Expected: true
- KG: true

## F10 [Flow] PASS

**Does the overhead route pass through K402?**

- Expected: true
- KG: true

## F11 [Flow] PASS

**Does the overhead route include V409?**

- Expected: true
- KG: true

## F12 [Flow] PASS

**Does the overhead route include PT403?**

- Expected: true
- KG: true

## P01 [Piping] PASS

**What is K402 piped to (vent line and liquid return)?**

- Expected: PCV300, E101
- KG: E101, PCV300

## P02 [Piping] PASS

**Where does RV400 discharge?**

- Expected: K403
- KG: K403

## P03 [Piping] PASS

**Where does RV401 discharge?**

- Expected: K403
- KG: K403

## P04 [Piping] PASS

**Which relief valves discharge into K403?**

- Expected: RV400, RV401
- KG: RV401, RV400

## P05 [Piping] PASS

**Is E101 piped to RV400?**

- Expected: true
- KG: true

## P06 [Piping] PASS

**Which equipment is the N2 return outlet on?**

- Expected: K402
- KG: K402

## P07 [Piping] PASS

**Which equipment is the overhead gas outlet on?**

- Expected: E101
- KG: E101

## P08 [Piping] PASS

**What is PCV300 piped to?**

- Expected: VENT_E101
- KG: VENT_E101

## E01 [Equipment] PASS

**Which cyclone separator is there?**

- Expected: K402
- KG: K402

## E02 [Equipment] PASS

**Which knockout drum does this piece add?**

- Expected: K403
- KG: K403

## E03 [Equipment] PASS

**Which vent connection does this piece add?**

- Expected: VENT_E101
- KG: VENT_E101

## E04 [Equipment] PASS

**Which pressure control valve does this piece add?**

- Expected: PCV300
- KG: PCV300

## E05 [Equipment] PASS

**Which manual valves does this piece add?**

- Expected: V409, V310, V313, V408
- KG: V310, V313, V408, V409

## E06 [Equipment] PASS

**Does the K403 note say it collects the RV400 discharge?**

- Expected: true
- KG: true

## E07 [Equipment] PASS

**What grid is K403 at?**

- Expected: E15
- KG: E15

## E08 [Equipment] PASS

**Which floor is K402 on?**

- Expected: 4
- KG: 4

## E09 [Equipment] PASS

**Which floor is K403 on?**

- Expected: 4
- KG: 4

## E10 [Equipment] PASS

**Which floor is the absorber vent on?**

- Expected: 3
- KG: 3

## V01 [Valves] PASS

**What grid is PCV300 at?**

- Expected: G18
- KG: G18

## V02 [Valves] PASS

**Which floor is PCV300 on?**

- Expected: 3
- KG: 3

## V03 [Valves] PASS

**Is PCV300 open in normal running?**

- Expected: open
- KG: open

## V04 [Valves] PASS

**What type of valve is PCV300?**

- Expected: pressure control
- KG: pressure control

## V05 [Valves] PASS

**What grid is V409 at?**

- Expected: E16
- KG: E16

## V06 [Valves] PASS

**Which floor is V409 on?**

- Expected: 4
- KG: 4

## V07 [Valves] PASS

**Is V409 locked?**

- Expected: true
- KG: true

## V08 [Valves] PASS

**Is V409 open in normal running?**

- Expected: open
- KG: open

## V09 [Valves] PASS

**What type of valve is V310?**

- Expected: 3-way ball
- KG: 3-way ball

## V10 [Valves] PASS

**What grid is V310 at?**

- Expected: F17
- KG: F17

## V11 [Valves] PASS

**Which floor is V310 on?**

- Expected: 3
- KG: 3

## V12 [Valves] PASS

**What type of valve is V313?**

- Expected: 3-way ball
- KG: 3-way ball

## V13 [Valves] PASS

**What type of valve is V408?**

- Expected: needle
- KG: needle

## V14 [Valves] PASS

**What grid is V408 at?**

- Expected: F16
- KG: F16

## I01 [Instruments] PASS

**What grid is TT412 at?**

- Expected: F15
- KG: F15

## I02 [Instruments] PASS

**Which floor is TT412 on?**

- Expected: 4
- KG: 4

## I03 [Instruments] PASS

**What type of sensor is TT412?**

- Expected: PRT
- KG: PRT

## I04 [Instruments] PASS

**What signal does TT412 use?**

- Expected: Fieldbus
- KG: Fieldbus

## I05 [Instruments] PASS

**What grid is TT413 at?**

- Expected: E16
- KG: E16

## I06 [Instruments] PASS

**Which floor is TT413 on?**

- Expected: 4
- KG: 4

## I07 [Instruments] PASS

**What signal does TT413 use?**

- Expected: Fieldbus
- KG: Fieldbus

## I08 [Instruments] PASS

**What type of transmitter is PT403?**

- Expected: gauge pressure transmitter
- KG: gauge pressure transmitter

## I09 [Instruments] PASS

**What grid is PT403 at?**

- Expected: D16
- KG: D16

## I10 [Instruments] PASS

**What signal does PT403 use?**

- Expected: Fieldbus
- KG: Fieldbus

## I11 [Instruments] PASS

**Which floor is PT403 on?**

- Expected: 4
- KG: 4

## I12 [Instruments] PASS

**What type of meter is FT300?**

- Expected: thermal mass flow meter
- KG: thermal mass flow meter

## I13 [Instruments] PASS

**What grid is FT300 at?**

- Expected: G18
- KG: G18

## I14 [Instruments] PASS

**What type of meter is FT301?**

- Expected: swirl volumetric flow meter
- KG: swirl volumetric flow meter

## I15 [Instruments] PASS

**What grid is FT301 at?**

- Expected: G20
- KG: G20

## I16 [Instruments] PASS

**What signal does FT302 use?**

- Expected: Profibus-DP
- KG: Profibus-DP

## I17 [Instruments] PASS

**Which flow meters are on the K402 overhead side?**

- Expected: FT300, FT301, FT302
- KG: FT300, FT301, FT302

## I18 [Instruments] PASS

**What does PT403 measure?**

- Expected: absorber (E101) pressure
- KG: absorber (E101) pressure

## I19 [Instruments] PASS

**What does PT403 monitor?**

- Expected: E101
- KG: E101

## I20 [Instruments] PASS

**Which floor is TT411 (top of E101, liquid) on?**

- Expected: 4
- KG: 4

## C01 [Control] PASS

**Which controller acts on PCV300?**

- Expected: PIC403
- KG: PIC403

## C02 [Control] PASS

**Which sensor does the absorber pressure loop use?**

- Expected: PT403
- KG: PT403

## C03 [Control] PASS

**Which controller does the absorber pressure loop use?**

- Expected: PIC403
- KG: PIC403

## C04 [Control] PASS

**Which valve does the absorber pressure loop move?**

- Expected: PCV300
- KG: PCV300

## C05 [Control] PASS

**What does the absorber pressure loop control?**

- Expected: Pressure in E101
- KG: Pressure in E101

## C06 [Control] PASS

**What does the absorber pressure loop manipulate?**

- Expected: Opening of PCV300 (lean gas vent rate)
- KG: Opening of PCV300 (lean gas vent rate)

## C07 [Control] PASS

**What does PIC403 control?**

- Expected: PCV300
- KG: PCV300

## C08 [Control] PASS

**Is the stripper pressure loop separate (does it act on PCV119, not PCV300)?**

- Expected: PCV119
- KG: PCV119

## S01 [Sampling] PASS

**Which valve serves sample point 1 (assumed)?**

- Expected: V408
- KG: V408

## S02 [Sampling] PASS

**Which valve serves sample point 2?**

- Expected: V308
- KG: V308

## S03 [Sampling] PASS

**At what height is sample point 1?**

- Expected: 6.85
- KG: 6.85

## D01 [Discrepancies] PASS

**Which discrepancy concerns K403?**

- Expected: discrepancy_K403_not_on_PID
- KG: discrepancy_K403_not_on_PID

## D02 [Discrepancies] PASS

**Which discrepancy concerns FT301?**

- Expected: discrepancy_FT301_FT302_order
- KG: discrepancy_FT301_FT302_order

## D03 [Discrepancies] PASS

**Which discrepancy concerns V310?**

- Expected: discrepancy_V313_V310_branch
- KG: discrepancy_V313_V310_branch

## D04 [Discrepancies] PASS

**Where is the V313 branch really connected?**

- Expected: Branch connected at V310
- KG: Branch connected at V310

## D05 [Discrepancies] PASS

**What is wrong with FT301 and FT302 on the P&ID?**

- Expected: Order reversed
- KG: Order reversed

## H01 [HAZOP] PASS

**Which HAZOP deviations concern K402?**

- Expected: HAZOP_10_01, HAZOP_10_05
- KG: HAZOP_10_01, HAZOP_10_05

## H02 [HAZOP] PASS

**Which HAZOP deviations concern PIC403?**

- Expected: HAZOP_3_02, HAZOP_3_03
- KG: HAZOP_3_02, HAZOP_3_03

## H03 [HAZOP] PASS

**Which HAZOP element covers RV400?**

- Expected: 10
- KG: 10

## H04 [HAZOP] PASS

**Does HAZOP 10.8 say RV400 is sized for the maximum gas filling rate?**

- Expected: true
- KG: true

## H05 [HAZOP] PASS

**Was gas analysis put on the top floor, above the K402 liquid switch?**

- Expected: true
- KG: true

## H06 [HAZOP] PASS

**Was liquid level detection added downstream of K402?**

- Expected: true
- KG: true

## M01 [HMT] PASS

**Is more than 400 kg/h of gas leaving the top of E101 (recommended case)?**

- Expected: true
- KG: true

## M02 [HMT] PASS

**Is less than 0.1 kg/h of CO2 left in that gas?**

- Expected: true
- KG: true

## M03 [HMT] PASS

**Does the gas leave E101 above 50 C?**

- Expected: true
- KG: true

## M04 [HMT] PASS

**Does the Aspen note say there is no K402 in the model?**

- Expected: true
- KG: true

## O01 [Open items] PASS

**Which open items concern K402?**

- Expected: AV01, AV08
- KG: AV01, AV08

## O02 [Open items] PASS

**Which open item concerns PCV300?**

- Expected: AV01
- KG: AV01

## O03 [Open items] PASS

**Which open item concerns V310?**

- Expected: AV03
- KG: AV03

## O04 [Open items] PASS

**Which open item concerns V408?**

- Expected: AV05
- KG: AV05

## O05 [Open items] PASS

**Which open item concerns K403?**

- Expected: AV06
- KG: AV06

## O06 [Open items] PASS

**How many open items did this piece raise?**

- Expected: 8
- KG: 8

## X01 [Join] PASS

**Is E101 connected through RV400 to K403?**

- Expected: true
- KG: true

## X02 [Join] PASS

**Can fresh CO2 travel through the absorber to the vent?**

- Expected: true
- KG: true

## X03 [Join] PASS

**Is the stripper relief RV401 connected to K403?**

- Expected: true
- KG: true

## X04 [Join] PASS

**Does the absorber pressure loop share a valve with the stripper pressure loop?**

- Expected: PCV300
- KG: PCV300
