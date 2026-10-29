# Feed gas KG: 100-question run

PASS 100, FAIL 0, QUERY ERROR 0

## F01 [Flow] PASS

**What comes first after the CO2 supply?**

- Expected: V128
- KG: V128

## F02 [Flow] PASS

**What does V128 feed?**

- Expected: PCV116
- KG: PCV116

## F03 [Flow] PASS

**What does PCV116 feed?**

- Expected: FT105
- KG: FT105

## F04 [Flow] PASS

**What does FT105 feed?**

- Expected: FCV105
- KG: FCV105

## F05 [Flow] PASS

**What does FCV105 feed?**

- Expected: NRV101
- KG: NRV101

## F06 [Flow] PASS

**Where does the CO2 line end?**

- Expected: FEED_GAS_HEADER
- KG: FEED_GAS_HEADER

## F07 [Flow] PASS

**What does V127 feed?**

- Expected: PCV117
- KG: PCV117

## F08 [Flow] PASS

**What does PCV117 feed?**

- Expected: PCV115
- KG: PCV115

## F09 [Flow] PASS

**What does PCV115 feed?**

- Expected: FCV116
- KG: FCV116

## F10 [Flow] PASS

**What does FCV116 feed?**

- Expected: NRV102
- KG: NRV102

## F11 [Flow] PASS

**Which lines meet at the common inlet (the tee)?**

- Expected: NRV101, NRV102
- KG: NRV101, NRV102

## F12 [Flow] PASS

**Where does the common inlet go (inferred)?**

- Expected: K101
- KG: K101

## F13 [Flow] PASS

**Does the CO2 supply reach E101?**

- Expected: true
- KG: true

## F14 [Flow] PASS

**Does the CO2 line feed straight into the N2 line?**

- Expected: false
- KG: false

## P01 [Piping] PASS

**What is PCV116 piped to?**

- Expected: FT105, RV103
- KG: FT105, RV103

## P02 [Piping] PASS

**What is PCV117 piped to?**

- Expected: PCV115, RV104
- KG: PCV115, RV104

## P03 [Piping] PASS

**What is the common inlet piped to?**

- Expected: K101
- KG: K101

## P04 [Piping] PASS

**What is piped into K101?**

- Expected: FEED_GAS_HEADER, C106
- KG: C106, FEED_GAS_HEADER

## P05 [Piping] PASS

**Which tagged item does K101 send water to?**

- Expected: J104
- KG: J104

## P06 [Piping] PASS

**What is J104 piped to?**

- Expected: C106, RV102
- KG: C106, RV102

## P07 [Piping] PASS

**What is C106 piped to?**

- Expected: K101
- KG: K101

## P08 [Piping] PASS

**Which equipment is the gas inlet nozzle on?**

- Expected: E101
- KG: E101

## E01 [Equipment] PASS

**Which saturator is there?**

- Expected: K101
- KG: K101

## E02 [Equipment] PASS

**Which supply connections are there?**

- Expected: CO2_SUPPLY, N2_SUPPLY
- KG: N2_SUPPLY, CO2_SUPPLY

## E03 [Equipment] PASS

**Which pump does this piece add?**

- Expected: J104
- KG: J104

## E04 [Equipment] PASS

**Which check valves does this piece add?**

- Expected: NRV101, NRV102, NRV111
- KG: NRV111, NRV101, NRV102

## E05 [Equipment] PASS

**Which shutdown valve does this piece add?**

- Expected: SDV170
- KG: SDV170

## E06 [Equipment] PASS

**Which relief valves does this piece add?**

- Expected: RV102, RV103, RV104
- KG: RV102, RV103, RV104

## E07 [Equipment] PASS

**Which flow control valves does this piece add?**

- Expected: FCV105, FCV116, FCV111, FCV102
- KG: FCV102, FCV111, FCV116, FCV105

## E08 [Equipment] PASS

**Which pressure control valves does this piece add?**

- Expected: PCV116, PCV115, PCV117
- KG: PCV115, PCV116, PCV117

## E09 [Equipment] PASS

**Which cooler does this piece add?**

- Expected: C106
- KG: C106

## E10 [Equipment] PASS

**What grid is J104 at?**

- Expected: O18
- KG: O18

## V01 [Valves] PASS

**What grid is PCV116 at?**

- Expected: K22
- KG: K22

## V02 [Valves] PASS

**What grid is FCV105 at?**

- Expected: K21
- KG: K21

## V03 [Valves] PASS

**What grid is NRV101 at?**

- Expected: K21
- KG: K21

## V04 [Valves] PASS

**What grid is RV103 at?**

- Expected: K22
- KG: K22

## V05 [Valves] PASS

**What grid is V127 at?**

- Expected: Q19
- KG: Q19

## V06 [Valves] PASS

**What grid is PCV117 at?**

- Expected: P21
- KG: P21

## V07 [Valves] PASS

**What grid is RV104 at?**

- Expected: P21
- KG: P21

## V08 [Valves] PASS

**What grid is PCV115 at?**

- Expected: N22
- KG: N22

## V09 [Valves] PASS

**What grid is FCV116 at?**

- Expected: N21
- KG: N21

## V10 [Valves] PASS

**What grid is NRV102 at?**

- Expected: N20
- KG: N20

## V11 [Valves] PASS

**What grid is FCV111 at?**

- Expected: K17
- KG: K17

## V12 [Valves] PASS

**What grid is FCV102 at?**

- Expected: Q16
- KG: Q16

## I01 [Instruments] PASS

**What type of meter is FT105?**

- Expected: thermal mass flow meter
- KG: thermal mass flow meter

## I02 [Instruments] PASS

**What signal does FT105 use?**

- Expected: 4-20mA
- KG: 4-20mA

## I03 [Instruments] PASS

**What grid is FT105 at?**

- Expected: K21
- KG: K21

## I04 [Instruments] PASS

**What grid is TT121 at?**

- Expected: L18
- KG: L18

## I05 [Instruments] PASS

**What type of sensor is TT121?**

- Expected: PRT
- KG: PRT

## I06 [Instruments] PASS

**What type of meter is FT106?**

- Expected: electromagnetic volumetric flow meter
- KG: electromagnetic volumetric flow meter

## I07 [Instruments] PASS

**What grid is FT106 at?**

- Expected: R16
- KG: R16

## I08 [Instruments] PASS

**What type of meter is FT303?**

- Expected: vortex volumetric flow meter
- KG: vortex volumetric flow meter

## I09 [Instruments] PASS

**What signal does FT304 use?**

- Expected: Profibus-PA
- KG: Profibus-PA

## I10 [Instruments] PASS

**Which floor is FT303 on?**

- Expected: 3
- KG: 3

## I11 [Instruments] PASS

**Which temperature instruments are recorded against E101 (now including TT107)?**

- Expected: TT107, TT109, TT204, TT205, TT206, TT207, TT305, TT306, TT307, TT308, TT411, TT413
- KG: TT205, TT207, TT306, TT308, TT411, TT107, TT109, TT204, TT206, TT305, TT307, TT413

## I12 [Instruments] PASS

**Which flow instruments are recorded against E101?**

- Expected: FT108, FI108, DI108, FT109, FI109, FT303, FT304
- KG: FT303, FT304, DI108, FI108, FI109, FT109, FT108

## C01 [Control] PASS

**Which controller acts on FCV105?**

- Expected: FIC105
- KG: FIC105

## C02 [Control] PASS

**Which controller acts on FCV116?**

- Expected: FIC116
- KG: FIC116

## C03 [Control] PASS

**Which controllers act on FCV111?**

- Expected: FIC303, FIC304
- KG: FIC303, FIC304

## C04 [Control] PASS

**Which controllers act on FCV102?**

- Expected: TIC121, FIC106
- KG: FIC106, TIC121

## C05 [Control] PASS

**Which sensor does the CO2 feed loop use?**

- Expected: FT105
- KG: FT105

## C06 [Control] PASS

**Which sensor does the N2 feed loop use?**

- Expected: FT116
- KG: FT116

## C07 [Control] PASS

**Which sensors does the N2-to-E101 loop use?**

- Expected: FT303, FT304
- KG: FT303, FT304

## C08 [Control] PASS

**Which valve does the N2-to-E101 loop move?**

- Expected: FCV111
- KG: FCV111

## C09 [Control] PASS

**Which sensor does the K101 temperature loop use?**

- Expected: TT121
- KG: TT121

## C10 [Control] PASS

**Which loop is the K101 temperature loop master of?**

- Expected: CL_C106_cooling_water
- KG: CL_C106_cooling_water

## C11 [Control] PASS

**Which sensor does the C106 cooling water loop use?**

- Expected: FT106
- KG: FT106

## C12 [Control] PASS

**What does the N2-to-E101 loop manipulate?**

- Expected: K101 bypass rate (FCV111)
- KG: K101 bypass rate (FCV111)

## L01 [Limits] PASS

**What is the top of the PCV116 output range?**

- Expected: 10
- KG: 10.0

## L02 [Limits] PASS

**What is the bottom of the PT113 range?**

- Expected: -1
- KG: -1.0

## L03 [Limits] PASS

**Which alarm is on the N2 feed?**

- Expected: FAL_N2_feed
- KG: FAL_N2_feed

## L04 [Limits] PASS

**Which alarms are on K101?**

- Expected: LZAH_K101, LAL_K101, LZAL_K101
- KG: LAL_K101, LZAH_K101, LZAL_K101

## L05 [Limits] PASS

**What does RV102 protect?**

- Expected: J104
- KG: J104

## L06 [Limits] PASS

**What does RV103 protect (per REPORT grid)?**

- Expected: PCV116
- KG: PCV116

## L07 [Limits] PASS

**What does RV104 protect (per REPORT grid)?**

- Expected: PCV117
- KG: PCV117

## B01 [Bypass] PASS

**What is SDV170 piped to?**

- Expected: FCV111
- KG: FCV111

## B02 [Bypass] PASS

**What is FCV111 piped to?**

- Expected: NRV111
- KG: NRV111

## B03 [Bypass] PASS

**Which equipment is the NRV111 base inlet on?**

- Expected: E101
- KG: E101

## D01 [Discrepancies] PASS

**Which discrepancy concerns the CO2 supply?**

- Expected: discrepancy_CO2_supply_label
- KG: discrepancy_CO2_supply_label

## D02 [Discrepancies] PASS

**What is the CO2 supply line really named?**

- Expected: Named 'compressed air'
- KG: Named 'compressed air'

## H01 [HAZOP] PASS

**Which HAZOP element covers V128?**

- Expected: 1
- KG: 1

## H02 [HAZOP] PASS

**Which HAZOP element covers V127?**

- Expected: 2
- KG: 2

## H03 [HAZOP] PASS

**Which HAZOP element covers K101?**

- Expected: 3
- KG: 3

## H04 [HAZOP] PASS

**Which HAZOP element covers J104?**

- Expected: 4
- KG: 4

## H05 [HAZOP] PASS

**Which HAZOP deviations concern FCV105?**

- Expected: HAZOP_1_03, HAZOP_1_06
- KG: HAZOP_1_03, HAZOP_1_06

## H06 [HAZOP] PASS

**Which HAZOP deviations concern PCV116?**

- Expected: HAZOP_1_07, HAZOP_1_08
- KG: HAZOP_1_07, HAZOP_1_08

## H07 [HAZOP] PASS

**Which HAZOP deviations concern PCV117?**

- Expected: HAZOP_2_05, HAZOP_2_08, HAZOP_2_10
- KG: HAZOP_2_05, HAZOP_2_08, HAZOP_2_10

## H08 [HAZOP] PASS

**Which HAZOP deviation concerns RV102?**

- Expected: HAZOP_4_03
- KG: HAZOP_4_03

## H09 [HAZOP] PASS

**Which HAZOP deviations concern K101?**

- Expected: HAZOP_3_05, HAZOP_4_02, HAZOP_4_06, HAZOP_4_07
- KG: HAZOP_3_05, HAZOP_4_02, HAZOP_4_06, HAZOP_4_07

## H10 [HAZOP] PASS

**Was a bypass line added after HAZOP 1.2?**

- Expected: true
- KG: true

## M01 [HMT] PASS

**Is the recommended-case feed gas flow above 400 kg/h?**

- Expected: true
- KG: true

## M02 [HMT] PASS

**Is the recommended-case feed below 10 % CO2 by mass?**

- Expected: true
- KG: true

## M03 [HMT] PASS

**Does the feed gas enter below 45 C?**

- Expected: true
- KG: true

## M04 [HMT] PASS

**Does the feed gas enter above 1.5 bar?**

- Expected: true
- KG: true

## M05 [HMT] PASS

**What is the feed gas flow in the pilot-scale case (v6.1)?**

- Expected: 45
- KG: 45.0

## O01 [Open items] PASS

**Which open item concerns FCV111?**

- Expected: GOI03
- KG: GOI03

## O02 [Open items] PASS

**Which open item concerns RV103?**

- Expected: GOI05
- KG: GOI05

## O03 [Open items] PASS

**Which open item concerns the CO2 supply?**

- Expected: GOI06
- KG: GOI06

## O04 [Open items] PASS

**Which open items concern K101?**

- Expected: GOI02, GOI07, GOI09
- KG: GOI02, GOI07, GOI09

## O05 [Open items] PASS

**How many open items did this piece raise?**

- Expected: 9
- KG: 9
