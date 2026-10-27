# Absorption loop KG: 100-question run

PASS 100, FAIL 0, QUERY ERROR 0

## F01 [Flow] PASS

**What does the E101 sump outlet feed?**

- Expected: V134a, V134b
- KG: V134a, V134b

## F02 [Flow] PASS

**What does V134a feed?**

- Expected: V135a
- KG: V135a

## F03 [Flow] PASS

**What does V135b feed?**

- Expected: J101b
- KG: J101b

## F04 [Flow] PASS

**What does J101a discharge into?**

- Expected: PCV120a
- KG: PCV120a

## F05 [Flow] PASS

**What does PCV120b feed?**

- Expected: V143b
- KG: V143b

## F06 [Flow] PASS

**What does V143a feed?**

- Expected: V144a
- KG: V144a

## F07 [Flow] PASS

**What feeds FT108?**

- Expected: V144a, V144b
- KG: V144a, V144b

## F08 [Flow] PASS

**What does FT108 feed?**

- Expected: FT109
- KG: FT109

## F09 [Flow] PASS

**What does FT109 feed?**

- Expected: V124
- KG: V124

## F10 [Flow] PASS

**What does V124 feed?**

- Expected: V119b
- KG: V119b

## F11 [Flow] PASS

**What does V119a feed on the main line?**

- Expected: V211
- KG: V211

## F12 [Flow] PASS

**What does N200 feed?**

- Expected: V213
- KG: V213

## F13 [Flow] PASS

**What does V213 feed?**

- Expected: C200
- KG: C200

## F14 [Flow] PASS

**What does C200 feed?**

- Expected: NRV400
- KG: NRV400

## F15 [Flow] PASS

**Is the absorption loop closed?**

- Expected: true
- KG: true

## F16 [Flow] PASS

**Does flow from NRV400 eventually reach J101a?**

- Expected: true
- KG: true

## F17 [Flow] PASS

**Does the J101a train feed straight into J101b?**

- Expected: false
- KG: false

## P01 [Piping] PASS

**What is V119a piped to?**

- Expected: V211, V212
- KG: V211, V212

## P02 [Piping] PASS

**What is V124 piped to?**

- Expected: V119b, V198b
- KG: V119b, V198b

## P03 [Piping] PASS

**What is V198a piped to?**

- Expected: V211
- KG: V211

## P04 [Piping] PASS

**Where does the N200 bypass V212 rejoin?**

- Expected: C200
- KG: C200

## P05 [Piping] PASS

**Where does the stripping loop lean feed join?**

- Expected: V119b
- KG: V119b

## P06 [Piping] PASS

**What is piped into N200?**

- Expected: V211, V210
- KG: V210, V211

## E01 [Equipment] PASS

**Which pumps are in the loop?**

- Expected: J101a, J101b
- KG: J101b, J101a

## E02 [Equipment] PASS

**Which pulsation dampeners are there?**

- Expected: B103a, B103b
- KG: B103a, B103b

## E03 [Equipment] PASS

**Which filters are there?**

- Expected: N200
- KG: N200

## E04 [Equipment] PASS

**Which trim cooler is there?**

- Expected: C200
- KG: C200

## E05 [Equipment] PASS

**Which check valves are there?**

- Expected: NRV400
- KG: NRV400

## E06 [Equipment] PASS

**Which shutdown valves are there?**

- Expected: SDV123
- KG: SDV123

## E07 [Equipment] PASS

**Which pressure control valves are there?**

- Expected: PCV120a, PCV120b
- KG: PCV120a, PCV120b

## E08 [Equipment] PASS

**Which relief valves are recorded (installed or drawn)?**

- Expected: RV106a, RV106b, RV400
- KG: RV106a, RV106b, RV400

## V01 [Valves] PASS

**What type of valve is V119a?**

- Expected: 3-way ball
- KG: 3-way ball

## V02 [Valves] PASS

**What type of valve is V119b?**

- Expected: 3-way ball
- KG: 3-way ball

## V03 [Valves] PASS

**What is V212's normal position?**

- Expected: closed
- KG: closed

## V04 [Valves] PASS

**What is V124's normal position?**

- Expected: closed
- KG: closed

## V05 [Valves] PASS

**Does V124 have a locking handle (HAZOP 8.3)?**

- Expected: true
- KG: true

## V06 [Valves] PASS

**Which floor is NRV400 on?**

- Expected: 4
- KG: 4

## V07 [Valves] PASS

**What is NRV400's grid reference?**

- Expected: F15
- KG: F15

## V08 [Valves] PASS

**What is V217's grid reference?**

- Expected: G14
- KG: G14

## V09 [Valves] PASS

**What is V198a's normal position?**

- Expected: closed
- KG: closed

## V10 [Valves] PASS

**What is FCV200's grid reference?**

- Expected: H12
- KG: H12

## V11 [Valves] PASS

**Which valves are needle valves (E101 sample valves)?**

- Expected: V205, V207, V306, V308
- KG: V205, V207, V306, V308

## V12 [Valves] PASS

**Which floor is sample valve V308 on?**

- Expected: 3
- KG: 3

## I01 [Instruments] PASS

**What type of transmitter is LT108?**

- Expected: differential pressure transmitter
- KG: differential pressure transmitter

## I02 [Instruments] PASS

**What is LT108's grid reference?**

- Expected: K15
- KG: K15

## I03 [Instruments] PASS

**What type of meter is FT108?**

- Expected: Coriolis mass flow meter
- KG: Coriolis mass flow meter

## I04 [Instruments] PASS

**What type of meter is FT109?**

- Expected: variable area volumetric flow meter
- KG: variable area volumetric flow meter

## I05 [Instruments] PASS

**What signal does FT109 use?**

- Expected: 4-20mA
- KG: 4-20mA

## I06 [Instruments] PASS

**What is TT210's grid reference?**

- Expected: J14
- KG: J14

## I07 [Instruments] PASS

**What signal does AT300 use?**

- Expected: Profibus-DP
- KG: Profibus-DP

## I08 [Instruments] PASS

**Which floor is AT300 on?**

- Expected: 3
- KG: 3

## I09 [Instruments] PASS

**What is PT111's grid reference?**

- Expected: K16
- KG: K16

## I10 [Instruments] PASS

**What type of transmitter is PT115b?**

- Expected: gauge pressure transmitter
- KG: gauge pressure transmitter

## I11 [Instruments] PASS

**What type of sensor is TT111a?**

- Expected: K-type thermocouple
- KG: K-type thermocouple

## I12 [Instruments] PASS

**What type of meter is FT201?**

- Expected: electromagnetic volumetric flow meter
- KG: electromagnetic volumetric flow meter

## I13 [Instruments] PASS

**Which temperature transmitters are on E101?**

- Expected: TT109, TT204, TT205, TT206, TT207, TT305, TT306, TT307, TT308, TT411, TT413
- KG: TT205, TT207, TT306, TT308, TT411, TT109, TT204, TT206, TT305, TT307, TT413

## I14 [Instruments] PASS

**What is TT305's grid reference?**

- Expected: G15
- KG: G15

## I15 [Instruments] PASS

**Does TT204 measure liquid or vapour?**

- Expected: liquid
- KG: liquid

## I16 [Instruments] PASS

**Does TT207 measure liquid or vapour?**

- Expected: vapour
- KG: vapour

## I17 [Instruments] PASS

**Which floor is TT411 on?**

- Expected: 4
- KG: 4

## S01 [Column] PASS

**How many gas sample points are on E101?**

- Expected: 6
- KG: 6

## S02 [Column] PASS

**Which temperature transmitter sits at the 4.11 m sample point?**

- Expected: TT305
- KG: TT305

## S03 [Column] PASS

**Which temperature transmitter sits at the bottom (0 m) sample point?**

- Expected: TT109
- KG: TT109

## S04 [Column] PASS

**Which analyser takes the E101 gas samples?**

- Expected: AT400
- KG: AT400

## S05 [Column] PASS

**Which valve serves sample point 2?**

- Expected: V308
- KG: V308

## S06 [Column] PASS

**What is the E101 diameter in mm?**

- Expected: 230
- KG: 230.0

## S07 [Column] PASS

**Is the E101 design pressure basis (2.3-2.5 bar) recorded?**

- Expected: true
- KG: true

## C01 [Control] PASS

**Which controllers act on J101a?**

- Expected: LIC108, SIC101a
- KG: LIC108, SIC101a

## C02 [Control] PASS

**Which controllers act on J101b?**

- Expected: LIC108, SIC101b
- KG: LIC108, SIC101b

## C03 [Control] PASS

**Which sensor does the E101 level loop use?**

- Expected: LT108
- KG: LT108

## C04 [Control] PASS

**Which controller is the C200 temperature master?**

- Expected: TIC210
- KG: TIC210

## C05 [Control] PASS

**Which sensor does the C200 cooling water loop use?**

- Expected: FT201
- KG: FT201

## C06 [Control] PASS

**Which valve does the C200 cooling water loop move?**

- Expected: FCV200
- KG: FCV200

## C07 [Control] PASS

**Which loop is the C200 temperature loop master of?**

- Expected: CL_C200_cooling_water
- KG: CL_C200_cooling_water

## C08 [Control] PASS

**How many control loops does the absorption loop have?**

- Expected: 3
- KG: 3

## L01 [Safety] PASS

**Which interlocks trip J101a?**

- Expected: IL_E101_level_HH, IL_E101_level_LL
- KG: IL_E101_level_HH, IL_E101_level_LL

## L02 [Safety] PASS

**Which switch starts the E101 low-low level shutdown?**

- Expected: LSLL109
- KG: LSLL109

## L03 [Safety] PASS

**At what pressure does PSHH117 trip?**

- Expected: 3.5
- KG: 3.5

## L04 [Safety] PASS

**What is the top of the FT109 range?**

- Expected: 1250
- KG: 1250.0

## L05 [Safety] PASS

**What is PCV120b set to?**

- Expected: 8
- KG: 8.0

## L06 [Safety] PASS

**Which equipment does RV400 protect?**

- Expected: E101
- KG: E101

## L07 [Safety] PASS

**Which relief valves are drawn but not on the plant?**

- Expected: RV106a, RV106b
- KG: RV106a, RV106b

## L08 [Safety] PASS

**Which alarm is on the C200 outlet temperature (HAZOP 10.7)?**

- Expected: TAH_C200_outlet
- KG: TAH_C200_outlet

## R01 [Procedures] PASS

**Which valve opens in the N200 bypass?**

- Expected: V212
- KG: V212

## R02 [Procedures] PASS

**Which valves close in the N200 bypass?**

- Expected: V211, V213
- KG: V211, V213

## R03 [Procedures] PASS

**Which valves does the J101b start-up open?**

- Expected: V134b, V135b, V143b, V144b
- KG: V134b, V135b, V143b, V144b

## R04 [Procedures] PASS

**How many steps are in the J101a start-up?**

- Expected: 7
- KG: 7

## R05 [Procedures] PASS

**What is the first step when starting the pumps?**

- Expected: Compare LT101 (E100) and LT108 (E101)
- KG: Compare LT101 (E100) and LT108 (E101)

## R06 [Procedures] PASS

**What triggers the N200 bypass?**

- Expected: Blockage in N200
- KG: Blockage in N200

## B01 [Routes] PASS

**Which valves are open for the J101a route?**

- Expected: V134a, V135a, V143a, V144a, V124
- KG: V124, V134a, V135a, V143a, V144a

## B02 [Routes] PASS

**Which valves are closed for the J101b route?**

- Expected: V134a, V135a, V143a, V144a, SDV123, V212, V198a, V198b
- KG: SDV123, V134a, V135a, V143a, V144a, V198a, V198b, V212

## B03 [Routes] PASS

**What does the N200 bypass skip?**

- Expected: V211, N200, V213
- KG: N200, V211, V213

## B04 [Routes] PASS

**Which tagged items does the test spool route pass through?**

- Expected: V198b, V198a, FM_TEST_SPOOL
- KG: FM_TEST_SPOOL, V198a, V198b

## H01 [HAZOP] PASS

**Which HAZOP element covers J101a?**

- Expected: 8
- KG: 8

## H02 [HAZOP] PASS

**Which HAZOP element covers E101?**

- Expected: 10
- KG: 10

## H03 [HAZOP] PASS

**Which HAZOP deviation concerns V124?**

- Expected: HAZOP_8_03
- KG: HAZOP_8_03

## H04 [HAZOP] PASS

**Which HAZOP element covers RV400?**

- Expected: 10
- KG: 10

## M01 [HMT] PASS

**Is E101 capture above 99 % in the recommended case?**

- Expected: true
- KG: true

## M02 [HMT] PASS

**Is the C200 duty above 20 kW?**

- Expected: true
- KG: true

## M03 [HMT] PASS

**Is the rich loading higher than the lean loading?**

- Expected: true
- KG: true
