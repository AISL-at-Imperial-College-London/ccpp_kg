# Gas returns KG: 100-question run

PASS 100, FAIL 0, QUERY ERROR 0

## F01 [N2 return] PASS

**Where does the N2 go after leaving K402 for the return line?**

- Expected: FT303
- KG: FT303

## F02 [N2 return] PASS

**What does FT303 feed?**

- Expected: FT304
- KG: FT304

## F03 [N2 return] PASS

**What does FT304 feed?**

- Expected: K102
- KG: K102

## F04 [N2 return] PASS

**What does K102 feed?**

- Expected: J102
- KG: J102

## F05 [N2 return] PASS

**What does J102 blow the N2 into?**

- Expected: K101
- KG: K101

## F06 [N2 return] PASS

**What feeds K102 on the return line?**

- Expected: FT304
- KG: FT304

## F07 [N2 return] PASS

**Does the returned N2 get back into E101?**

- Expected: true
- KG: true

## F08 [N2 return] PASS

**Is the N2 return a closed loop (E101 round to J102)?**

- Expected: true
- KG: true

## F09 [N2 return] PASS

**Does K102 feed K101 directly (skipping J102)?**

- Expected: false
- KG: false

## F10 [N2 return] PASS

**Does the N2 return loop include TT304?**

- Expected: true
- KG: true

## F11 [N2 return] PASS

**Is J102 still piped to PCV118 (it should not be: no spillback on the P&ID)?**

- Expected: false
- KG: false

## F12 [N2 return] PASS

**Does the N2 return loop include K101?**

- Expected: true
- KG: true

## C01 [CO2 return] PASS

**Where does gas from K401 go first?**

- Expected: NRV401
- KG: NRV401

## C02 [CO2 return] PASS

**What does NRV401 feed?**

- Expected: FT302
- KG: FT302

## C03 [CO2 return] PASS

**What does FT302 feed?**

- Expected: FT301
- KG: FT301

## C04 [CO2 return] PASS

**What does FT301 feed?**

- Expected: K103
- KG: K103

## C05 [CO2 return] PASS

**What does K103 feed?**

- Expected: J103
- KG: J103

## C06 [CO2 return] PASS

**What does J103 discharge into?**

- Expected: SDV171
- KG: SDV171

## C07 [CO2 return] PASS

**Where does the CO2 return enter (through V172)?**

- Expected: K101
- KG: K101

## C08 [CO2 return] PASS

**Does CO2 from K401 get back into E101?**

- Expected: true
- KG: true

## C09 [CO2 return] PASS

**Can CO2 stripped in E100 reach the absorber E101?**

- Expected: true
- KG: true

## C10 [CO2 return] PASS

**Does J103 feed K101 directly (skipping NRV104)?**

- Expected: false
- KG: false

## P01 [Piping] PASS

**Where does the FCV111 recycle go?**

- Expected: K102
- KG: K102

## P02 [Piping] PASS

**Is FCV111 still piped into the E101 base (it should not be)?**

- Expected: false
- KG: false

## P03 [Piping] PASS

**Is J102 piped to K101?**

- Expected: true
- KG: true

## P04 [Piping] PASS

**Does the PCV118 note say it is not on the current P&ID?**

- Expected: true
- KG: true

## P05 [Piping] PASS

**Are FT304 and FCV111 both piped into K102?**

- Expected: true
- KG: true

## P06 [Piping] PASS

**Is J103 piped to SDV171 and to PCV119?**

- Expected: true
- KG: true

## P07 [Piping] PASS

**Does PCV119 recycle CO2 back to K103?**

- Expected: true
- KG: true

## P08 [Piping] PASS

**Is K103 piped to J103 and to its drain V185?**

- Expected: true
- KG: true

## P09 [Piping] PASS

**Is K102 piped to J102 and to its drain V187?**

- Expected: true
- KG: true

## P10 [Piping] PASS

**Is K101 piped to SDV170 (start of the FCV111 recycle)?**

- Expected: true
- KG: true

## E01 [Equipment] PASS

**Which blower does this piece add?**

- Expected: J102
- KG: J102

## E02 [Equipment] PASS

**Which compressor does this piece add?**

- Expected: J103
- KG: J103

## E03 [Equipment] PASS

**Which knockout drums does this piece add?**

- Expected: K102, K103
- KG: K103, K102

## E04 [Equipment] PASS

**Which pressure control valves does this piece add?**

- Expected: PCV118, PCV114
- KG: PCV114, PCV118

## E05 [Equipment] PASS

**Which check valves does this piece add?**

- Expected: NRV104, NRV401
- KG: NRV401, NRV104

## E06 [Equipment] PASS

**Which shutdown valve does this piece add?**

- Expected: SDV171
- KG: SDV171

## E07 [Equipment] PASS

**Which manual valves does this piece add?**

- Expected: V187, V185, V311, V312, V172
- KG: V185, V311, V312, V172, V187

## E08 [Equipment] PASS

**What grid is J102 at?**

- Expected: L17
- KG: L17

## E09 [Equipment] PASS

**What grid is J103 at?**

- Expected: M20
- KG: M20

## E10 [Equipment] PASS

**Which floor is J103 on?**

- Expected: 1
- KG: 1

## V01 [Valves] PASS

**What grid is V187 at?**

- Expected: M17
- KG: M17

## V02 [Valves] PASS

**Is V187 normally closed?**

- Expected: closed
- KG: closed

## V03 [Valves] PASS

**Is V185 locked?**

- Expected: true
- KG: true

## V04 [Valves] PASS

**What grid is NRV104 at?**

- Expected: O18
- KG: O18

## V05 [Valves] PASS

**Which floor is NRV401 on?**

- Expected: 4
- KG: 4

## V06 [Valves] PASS

**What grid is NRV401 at?**

- Expected: D18
- KG: D18

## V07 [Valves] PASS

**What grid are V311 and V312 at?**

- Expected: F17
- KG: F17

## V08 [Valves] PASS

**Is V312 normally closed?**

- Expected: closed
- KG: closed

## V09 [Valves] PASS

**What grid is SDV171 at?**

- Expected: L19
- KG: L19

## V10 [Valves] PASS

**Is SDV171 open in normal running?**

- Expected: open
- KG: open

## I01 [Instruments] PASS

**What type of sensor is TT304?**

- Expected: PRT
- KG: PRT

## I02 [Instruments] PASS

**What grid is TT304 at?**

- Expected: G17
- KG: G17

## I03 [Instruments] PASS

**What type of sensor is TT114?**

- Expected: K-type thermocouple
- KG: K-type thermocouple

## I04 [Instruments] PASS

**What type of meter is FT107?**

- Expected: variable area volumetric flow meter
- KG: variable area volumetric flow meter

## I05 [Instruments] PASS

**What signal does TT115 use?**

- Expected: 4-20mA
- KG: 4-20mA

## I06 [Instruments] PASS

**What type of transmitter is LT104?**

- Expected: differential pressure transmitter
- KG: differential pressure transmitter

## I07 [Instruments] PASS

**What grid is LT104 at?**

- Expected: M19
- KG: M19

## I08 [Instruments] PASS

**What grid is PT110 at?**

- Expected: J18
- KG: J18

## I09 [Instruments] PASS

**What grid is PI402 at?**

- Expected: C16
- KG: C16

## I10 [Instruments] PASS

**What grid is PI403 at?**

- Expected: D17
- KG: D17

## I11 [Instruments] PASS

**Do TT304, FI303, FI304, TT114 and FT107 monitor J102?**

- Expected: true
- KG: true

## I12 [Instruments] PASS

**Does TT115 monitor J103?**

- Expected: true
- KG: true

## I13 [Instruments] PASS

**Are FT301 and FT302 on the CO2 return to J103?**

- Expected: true
- KG: true

## I14 [Instruments] PASS

**Do LT104, LI106 and TI121 monitor K101?**

- Expected: true
- KG: true

## I15 [Instruments] PASS

**Do the local indicators TI410 and FI402 monitor C400?**

- Expected: true
- KG: true

## I16 [Instruments] PASS

**What does FT301 measure now?**

- Expected: CO2 return flow (K401 to J103)
- KG: CO2 return flow (K401 to J103)

## B01 [Recycles] PASS

**What does the K101 N2 recycle skip?**

- Expected: E101
- KG: E101

## B02 [Recycles] PASS

**Which valves are on the K101 N2 recycle?**

- Expected: SDV170, FCV111
- KG: FCV111, SDV170

## B03 [Recycles] PASS

**Where does the K101 N2 recycle end?**

- Expected: K102
- KG: K102

## B04 [Recycles] PASS

**Which instrument is the J103 discharge high-high pressure switch?**

- Expected: PSHH118
- KG: PSHH118

## B05 [Recycles] PASS

**Which valve recycles CO2 around K103?**

- Expected: PCV119
- KG: PCV119

## B06 [Recycles] PASS

**Where does the K103 recycle start?**

- Expected: J103
- KG: J103

## L01 [Alarms] PASS

**Which alarm is on the N2 return flow?**

- Expected: FAL_N2_return
- KG: FAL_N2_return

## L02 [Alarms] PASS

**Which alarm is on the CO2 return flow?**

- Expected: FAL_CO2_return
- KG: FAL_CO2_return

## L03 [Alarms] PASS

**Which alarm is on K103?**

- Expected: LAH_K103
- KG: LAH_K103

## L04 [Alarms] PASS

**Which alarms are on C400?**

- Expected: TAH_C400_carryover
- KG: TAH_C400_carryover

## L05 [Alarms] PASS

**What kind of limit protects J103 from starving?**

- Expected: trip
- KG: trip

## H01 [HAZOP] PASS

**Does HAZOP element 5 cover J102?**

- Expected: true
- KG: true

## H02 [HAZOP] PASS

**Does HAZOP element 6 cover J103?**

- Expected: true
- KG: true

## H03 [HAZOP] PASS

**Does HAZOP element 5 cover K402?**

- Expected: true
- KG: true

## H04 [HAZOP] PASS

**Does HAZOP element 6 cover PCV119?**

- Expected: true
- KG: true

## H05 [HAZOP] PASS

**Do HAZOP 5.1, 5.2, 5.4 and 5.9 concern J102?**

- Expected: true
- KG: true

## H06 [HAZOP] PASS

**Do HAZOP 6.1, 6.2, 6.5, 6.6 and 6.9 concern J103?**

- Expected: true
- KG: true

## H07 [HAZOP] PASS

**Does HAZOP 6.5 concern PCV119?**

- Expected: true
- KG: true

## H08 [HAZOP] PASS

**Do HAZOP 6.2 and 6.3 concern FT301?**

- Expected: true
- KG: true

## H09 [HAZOP] PASS

**Was a FAL added on FT303/304 (HAZOP 5.1)?**

- Expected: true
- KG: true

## H10 [HAZOP] PASS

**Was a J103 shutdown trip added (HAZOP 6.1)?**

- Expected: true
- KG: true

## H11 [HAZOP] PASS

**Does HAZOP 6.3 ask for NRV104 to be reliable on CO2?**

- Expected: true
- KG: true

## O01 [Open items] PASS

**Which open item concerns PCV119?**

- Expected: GR07
- KG: GR07

## O02 [Open items] PASS

**Which open item concerns NRV104?**

- Expected: GR11
- KG: GR11

## O03 [Open items] PASS

**Are GR05 and GR10 about J103?**

- Expected: true
- KG: true

## O04 [Open items] PASS

**Which open item concerns NRV111 now?**

- Expected: GOI03
- KG: GOI03

## O05 [Open items] PASS

**How many open items does this piece hold?**

- Expected: 8
- KG: 8

## X01 [Join] PASS

**Do the CO2 and N2 supplies both feed the common inlet?**

- Expected: true
- KG: true

## X02 [Join] PASS

**Do the fresh-gas header and J102 both feed K101?**

- Expected: true
- KG: true

## X03 [Join] PASS

**Does the stripper overhead (C400) lead to J103?**

- Expected: true
- KG: true

## X05 [Join] PASS

**Does K401 now flow to its gas outlet (fixed in piece 7)?**

- Expected: true
- KG: true

## X04 [Join] PASS

**Does the N2 return pass the absorber pressure valve PCV300?**

- Expected: false
- KG: false
