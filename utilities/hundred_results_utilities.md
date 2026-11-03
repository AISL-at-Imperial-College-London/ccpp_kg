# Utilities KG: 100-question run

PASS 100, FAIL 0, QUERY ERROR 0

## S01 [Steam] PASS

**What comes first after the building steam supply?**

- Expected: XV140
- KG: XV140

## S02 [Steam] PASS

**What does XV140 feed?**

- Expected: V100
- KG: V100

## S03 [Steam] PASS

**What does V100 feed?**

- Expected: V101
- KG: V101

## S04 [Steam] PASS

**What does V101 feed?**

- Expected: FT100
- KG: FT100

## S05 [Steam] PASS

**What does FT100 feed?**

- Expected: V102
- KG: V102

## S06 [Steam] PASS

**What does V102 feed?**

- Expected: FT101
- KG: FT101

## S07 [Steam] PASS

**What does FT101 feed?**

- Expected: FCV110
- KG: FCV110

## S08 [Steam] PASS

**Does FCV110 feed the H100 steam inlet?**

- Expected: true
- KG: true

## S09 [Steam] PASS

**What does K100 feed?**

- Expected: V103
- KG: V103

## S10 [Steam] PASS

**What does V103 feed?**

- Expected: V105
- KG: V105

## S11 [Steam] PASS

**What does V105 feed?**

- Expected: NRV110
- KG: NRV110

## S12 [Steam] PASS

**What does NRV110 feed?**

- Expected: CONDENSATE_RETURN
- KG: CONDENSATE_RETURN

## S13 [Steam] PASS

**Does steam reach the condensate return?**

- Expected: true
- KG: true

## S14 [Steam] PASS

**Can steam flow into the E100 process side (it must not)?**

- Expected: false
- KG: false

## S15 [Steam] PASS

**Does the steam route include PT101?**

- Expected: true
- KG: true

## S16 [Steam] PASS

**Does the steam route include the RV107 relief?**

- Expected: true
- KG: true

## W01 [Cooling water] PASS

**What does V194 feed?**

- Expected: PCV103
- KG: PCV103

## W02 [Cooling water] PASS

**What does PCV103 feed?**

- Expected: FCV102
- KG: FCV102

## W03 [Cooling water] PASS

**What does FCV102 feed?**

- Expected: FT106
- KG: FT106

## W04 [Cooling water] PASS

**Does FT106 feed the C106 cooling water inlet?**

- Expected: true
- KG: true

## W05 [Cooling water] PASS

**What does V208 feed?**

- Expected: FCV201
- KG: FCV201

## W06 [Cooling water] PASS

**What does FCV201 feed?**

- Expected: FCV200
- KG: FCV200

## W07 [Cooling water] PASS

**What does FCV200 feed?**

- Expected: FT201
- KG: FT201

## W08 [Cooling water] PASS

**What does V405 feed?**

- Expected: PCV415
- KG: PCV415

## W09 [Cooling water] PASS

**What does PCV415 feed?**

- Expected: FCV401
- KG: FCV401

## W10 [Cooling water] PASS

**What does V410 feed?**

- Expected: V411
- KG: V411

## W11 [Cooling water] PASS

**Which valves start the three cooling water streams?**

- Expected: true
- KG: true

## W12 [Cooling water] PASS

**Do all three streams end at the cooling water return?**

- Expected: true
- KG: true

## W13 [Cooling water] PASS

**Does cooling water reach its return?**

- Expected: true
- KG: true

## W14 [Cooling water] PASS

**Can cooling water flow into E101 (it must not)?**

- Expected: false
- KG: false

## W15 [Cooling water] PASS

**Can cooling water flow into E100 (it must not)?**

- Expected: false
- KG: false

## W16 [Cooling water] PASS

**Does the C400 cooling water pass through FCV401 before C400?**

- Expected: true
- KG: true

## P01 [Piping] PASS

**Is V106 piped from the H100 condensate outlet (bypass round K100)?**

- Expected: true
- KG: true

## P02 [Piping] PASS

**Where does the V106 bypass rejoin?**

- Expected: V103
- KG: V103

## P03 [Piping] PASS

**Is V195 piped off the C106 cooling water outlet?**

- Expected: true
- KG: true

## P04 [Piping] PASS

**Is V215 piped off the C200 cooling water outlet?**

- Expected: true
- KG: true

## P05 [Piping] PASS

**Is V412 piped off the C400 cooling water outlet?**

- Expected: true
- KG: true

## P06 [Piping] PASS

**Which equipment is the steam inlet on?**

- Expected: H100
- KG: H100

## P07 [Piping] PASS

**Which equipment is the C200 cooling water inlet on?**

- Expected: C200
- KG: C200

## P08 [Piping] PASS

**Which equipment is the C400 cooling water outlet on?**

- Expected: C400
- KG: C400

## E01 [Equipment] PASS

**Which steam trap does this piece add?**

- Expected: K100
- KG: K100

## E02 [Equipment] PASS

**Which supply connections does this piece add?**

- Expected: STEAM_SUPPLY, CW_SUPPLY
- KG: CW_SUPPLY, STEAM_SUPPLY

## E03 [Equipment] PASS

**Which return connections does this piece add?**

- Expected: CONDENSATE_RETURN, CW_RETURN
- KG: CONDENSATE_RETURN, CW_RETURN

## E04 [Equipment] PASS

**Which shutdown valve does this piece add?**

- Expected: XV140
- KG: XV140

## E05 [Equipment] PASS

**Which check valve does this piece add?**

- Expected: NRV110
- KG: NRV110

## E06 [Equipment] PASS

**Which relief valve does this piece add?**

- Expected: RV107
- KG: RV107

## E07 [Equipment] PASS

**Which pressure control valves does this piece add?**

- Expected: PCV103, PCV415
- KG: PCV103, PCV415

## E08 [Equipment] PASS

**Which manual valves does this piece add?**

- Expected: V100, V103, V104, V194, V195, V136, V196, V197, V208, V209, V214, V215, V405, V410, V411, V412
- KG: V195, V196, V209, V215, V412, V136, V197, V214, V410, V104, V194, V208, V405, V411, V100, V103

## E09 [Equipment] PASS

**Which floor is K100 on?**

- Expected: 1
- KG: 1

## V01 [Valves] PASS

**What grid is XV140 at?**

- Expected: L2
- KG: L2

## V02 [Valves] PASS

**What grid is V100 at?**

- Expected: L3
- KG: L3

## V03 [Valves] PASS

**Is V100 open in normal running?**

- Expected: open
- KG: open

## V04 [Valves] PASS

**What grid is V103 at?**

- Expected: M5
- KG: M5

## V05 [Valves] PASS

**Is V104 closed in normal running?**

- Expected: closed
- KG: closed

## V06 [Valves] PASS

**What grid is NRV110 at?**

- Expected: M3
- KG: M3

## V07 [Valves] PASS

**What grid is RV107 at?**

- Expected: M5
- KG: M5

## V08 [Valves] PASS

**What grid is V194 at?**

- Expected: R15
- KG: R15

## V09 [Valves] PASS

**What grid is PCV103 at?**

- Expected: R15
- KG: R15

## V10 [Valves] PASS

**Is V195 closed in normal running?**

- Expected: closed
- KG: closed

## V11 [Valves] PASS

**What grid is V208 at?**

- Expected: H11
- KG: H11

## V12 [Valves] PASS

**Which floor is V208 on?**

- Expected: 2
- KG: 2

## V13 [Valves] PASS

**Is V209 locked?**

- Expected: true
- KG: true

## V14 [Valves] PASS

**What grid is V214 at?**

- Expected: K13
- KG: K13

## V15 [Valves] PASS

**Is V215 closed in normal running?**

- Expected: closed
- KG: closed

## V16 [Valves] PASS

**What grid is PCV415 at?**

- Expected: C14
- KG: C14

## V17 [Valves] PASS

**Which floor is PCV415 on?**

- Expected: 4
- KG: 4

## V18 [Valves] PASS

**What grid are V410 and V411 at?**

- Expected: D10
- KG: D10

## V19 [Valves] PASS

**Is V411 locked?**

- Expected: true
- KG: true

## V20 [Valves] PASS

**Is V412 closed in normal running?**

- Expected: closed
- KG: closed

## V21 [Valves] PASS

**What grid is V136 at?**

- Expected: P18
- KG: P18

## I01 [Instruments] PASS

**What type of transmitter is PT101?**

- Expected: gauge pressure transmitter
- KG: gauge pressure transmitter

## I02 [Instruments] PASS

**What grid is PT101 at?**

- Expected: L3
- KG: L3

## I03 [Instruments] PASS

**What signal does PT101 use?**

- Expected: 4-20mA
- KG: 4-20mA

## I04 [Instruments] PASS

**What grid is TT117 at (per Fig F.12)?**

- Expected: L4
- KG: L4

## I05 [Instruments] PASS

**What grid is TT118 at (per Fig F.12)?**

- Expected: M5
- KG: M5

## I06 [Instruments] PASS

**What signal do TT117 and TT118 use?**

- Expected: Profibus-PA
- KG: Profibus-PA

## I07 [Instruments] PASS

**What does TT117 measure?**

- Expected: steam temperature into H100
- KG: steam temperature into H100

## I08 [Instruments] PASS

**Do PT101, PI100, PI101, FI100, TT117 and TT118 monitor H100?**

- Expected: true
- KG: true

## I09 [Instruments] PASS

**Do FI106 and TT119 monitor C106?**

- Expected: true
- KG: true

## I10 [Instruments] PASS

**Do FI200 and FI201 monitor C200?**

- Expected: true
- KG: true

## I11 [Instruments] PASS

**What grid is TT119 at?**

- Expected: R17
- KG: R17

## I12 [Instruments] PASS

**What grid is FI200 at?**

- Expected: H11
- KG: H11

## B01 [Bypass] PASS

**What does the V106 bypass skip?**

- Expected: K100
- KG: K100

## B02 [Bypass] PASS

**Which valve is on the K100 bypass?**

- Expected: V106
- KG: V106

## B03 [Bypass] PASS

**Is the K100 bypass normally closed?**

- Expected: closed
- KG: closed

## H01 [HAZOP] PASS

**Does HAZOP element 13 cover XV140?**

- Expected: true
- KG: true

## H02 [HAZOP] PASS

**Does HAZOP element 13 cover K100 and RV107?**

- Expected: true
- KG: true

## H03 [HAZOP] PASS

**Do HAZOP 13.1 and 13.6 concern V106?**

- Expected: true
- KG: true

## H04 [HAZOP] PASS

**Does HAZOP 13.6 concern K100?**

- Expected: true
- KG: true

## H05 [HAZOP] PASS

**Does HAZOP 13.4 (steam limit ~140 kg/h) concern FCV110?**

- Expected: true
- KG: true

## H06 [HAZOP] PASS

**Was a plant shutdown on steam failure added (HAZOP 13.3)?**

- Expected: true
- KG: true

## O01 [Open items] PASS

**Which open item concerns K100?**

- Expected: true
- KG: true

## O02 [Open items] PASS

**Which open items concern V197?**

- Expected: true
- KG: true

## O03 [Open items] PASS

**Which open item concerns TT117?**

- Expected: UT04
- KG: UT04

## O04 [Open items] PASS

**Which open item concerns RV107?**

- Expected: UT05
- KG: UT05

## O05 [Open items] PASS

**How many open items did this piece raise?**

- Expected: 10
- KG: 10

## X01 [Join] PASS

**Is the H100 steam limit (140 kg/h) still on H100?**

- Expected: 140
- KG: 140.0

## X02 [Join] PASS

**Is the C400 cooling water valve still controlled by FIC402?**

- Expected: true
- KG: true

## X03 [Join] PASS

**Is the C106 cooling water valve still controlled by FIC106 and TIC121?**

- Expected: true
- KG: true

## X04 [Join] PASS

**Does the MEA side of H100 still feed E100 (process unaffected)?**

- Expected: true
- KG: true
