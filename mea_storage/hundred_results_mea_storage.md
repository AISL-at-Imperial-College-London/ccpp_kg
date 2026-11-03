# MEA storage KG: 100-question run

PASS 100, FAIL 0, QUERY ERROR 0

## F01 [Filling] PASS

**What does the feed tank F100 feed?**

- Expected: J105
- KG: J105

## F02 [Filling] PASS

**What does J105 pump into?**

- Expected: FILL_DRAIN_HEADER
- KG: FILL_DRAIN_HEADER

## F03 [Filling] PASS

**Does MEA from F100 reach the fill/drain header?**

- Expected: true
- KG: true

## F04 [Filling] PASS

**Does the filling route leak into the normal E100 flow path (it must not)?**

- Expected: false
- KG: false

## F05 [Filling] PASS

**Does normal running flow into the receiver tank (it must not)?**

- Expected: false
- KG: false

## F06 [Filling] PASS

**Does the filling route include TT116?**

- Expected: true
- KG: true

## F07 [Filling] PASS

**Does the filling route include PCV126?**

- Expected: true
- KG: true

## F08 [Filling] PASS

**Does the filling route include the V138 manual vent?**

- Expected: true
- KG: true

## F09 [Filling] PASS

**Does F100 feed the header directly (skipping J105)?**

- Expected: false
- KG: false

## F10 [Filling] PASS

**Is the filling route in the Filling operating mode?**

- Expected: Filling
- KG: Filling

## P01 [Piping] PASS

**Is the header piped back to the receiver tank R100?**

- Expected: true
- KG: true

## P02 [Piping] PASS

**Is the header piped to V115 and V122 at J100 (HAZOP M14)?**

- Expected: true
- KG: true

## P03 [Piping] PASS

**Do the J101 fill/drain valves V146a/b and V147a/b connect to the header?**

- Expected: true
- KG: true

## P04 [Piping] PASS

**Do the drains V153, V154 and V155 drop to the header?**

- Expected: true
- KG: true

## P05 [Piping] PASS

**Do V160, V167 and V168 drop to the header?**

- Expected: true
- KG: true

## P06 [Piping] PASS

**Do V148 and V149 drop to the header?**

- Expected: true
- KG: true

## P07 [Piping] PASS

**Does the K101 bottom outlet V126 run to the header (team trace)?**

- Expected: true
- KG: true

## P08 [Piping] PASS

**Can K101 reach the header through V126?**

- Expected: true
- KG: true

## E01 [Equipment] PASS

**Which storage tanks are there?**

- Expected: F100, R100
- KG: F100, R100

## E02 [Equipment] PASS

**Which pump does this piece add?**

- Expected: J105
- KG: J105

## E03 [Equipment] PASS

**Which pressure control valve does this piece add?**

- Expected: PCV126
- KG: PCV126

## E04 [Equipment] PASS

**Which check valves does this piece add?**

- Expected: NRV107, NRV108
- KG: NRV107, NRV108

## E05 [Equipment] PASS

**What grid is J105 at?**

- Expected: N4
- KG: N4

## E06 [Equipment] PASS

**Which floor is J105 on?**

- Expected: 1
- KG: 1

## E07 [Equipment] PASS

**What grid is the feed tank F100 at (as built)?**

- Expected: N2
- KG: N2

## E08 [Equipment] PASS

**What grid is the receiver tank R100 at (as built)?**

- Expected: N3
- KG: N3

## E09 [Equipment] PASS

**Does the F100 note say it is the feed tank?**

- Expected: true
- KG: true

## E10 [Equipment] PASS

**Does the R100 note say it is the receiver tank?**

- Expected: true
- KG: true

## V01 [Valves] PASS

**What grid is PCV126 at?**

- Expected: N5
- KG: N5

## V02 [Valves] PASS

**What grid is V156 at?**

- Expected: N6
- KG: N6

## V03 [Valves] PASS

**Is V156 normally closed?**

- Expected: closed
- KG: closed

## V04 [Valves] PASS

**What grid is V157 at?**

- Expected: N5
- KG: N5

## V05 [Valves] PASS

**What grid is V158 at?**

- Expected: O4
- KG: O4

## V06 [Valves] PASS

**What grid is V159a at?**

- Expected: O3
- KG: O3

## V07 [Valves] PASS

**What grid is V159b at?**

- Expected: O2
- KG: O2

## V08 [Valves] PASS

**What grid is V161a at?**

- Expected: O3
- KG: O3

## V09 [Valves] PASS

**What grid is V161b at?**

- Expected: O2
- KG: O2

## V10 [Valves] PASS

**What grid is V162 at?**

- Expected: N2
- KG: N2

## V11 [Valves] PASS

**What grid is V163 at?**

- Expected: O3
- KG: O3

## V12 [Valves] PASS

**What grid is V164 at?**

- Expected: N3
- KG: N3

## V13 [Valves] PASS

**What grid is V199 at?**

- Expected: O4
- KG: O4

## V14 [Valves] PASS

**What grid is V153 at?**

- Expected: O8
- KG: O8

## V15 [Valves] PASS

**Is V153 normally closed?**

- Expected: closed
- KG: closed

## V16 [Valves] PASS

**What grid is V155 at?**

- Expected: O7
- KG: O7

## V17 [Valves] PASS

**What grid is V167 at?**

- Expected: N9
- KG: N9

## V18 [Valves] PASS

**What grid is V149 at?**

- Expected: O12
- KG: O12

## V19 [Valves] PASS

**What grid is V148 at?**

- Expected: O13
- KG: O13

## V20 [Valves] PASS

**What grid is V146a at?**

- Expected: O15
- KG: O15

## V21 [Valves] PASS

**What grid is V147b at?**

- Expected: O16
- KG: O16

## V22 [Valves] PASS

**What grid is NRV107 at?**

- Expected: N2
- KG: N2

## V23 [Valves] PASS

**What grid is NRV108 at?**

- Expected: N3
- KG: N3

## V24 [Valves] PASS

**What kind of valve is V138?**

- Expected: manual vent
- KG: manual vent

## V25 [Valves] PASS

**What grid is V168 at?**

- Expected: N9
- KG: N9

## I01 [Instruments] PASS

**What type of sensor is TT116?**

- Expected: PRT
- KG: PRT

## I02 [Instruments] PASS

**What signal does TT116 use?**

- Expected: 4-20mA
- KG: 4-20mA

## I03 [Instruments] PASS

**What grid is TT116 at?**

- Expected: N5
- KG: N5

## I04 [Instruments] PASS

**What does TT116 monitor?**

- Expected: J105
- KG: J105

## I05 [Instruments] PASS

**Do FI110 and PI112 sit at the tank at N2 (F100)?**

- Expected: true
- KG: true

## I06 [Instruments] PASS

**Do FI111 and PI113 sit at the tank at N3 (R100)?**

- Expected: true
- KG: true

## I07 [Instruments] PASS

**What grid is FI110 at?**

- Expected: N2
- KG: N2

## I08 [Instruments] PASS

**What grid is FI111 at?**

- Expected: M3
- KG: M3

## I09 [Instruments] PASS

**What grid is PI112 at?**

- Expected: N2
- KG: N2

## I10 [Instruments] PASS

**What grid is PI113 at?**

- Expected: M3
- KG: M3

## L01 [Trips] PASS

**What kind of limit is on the receiver tank level?**

- Expected: trip
- KG: trip

## L02 [Trips] PASS

**Does the receiver tank have a high-level trip (HAZOP M16)?**

- Expected: true
- KG: true

## L03 [Trips] PASS

**Does the feed tank have a low-level trip (HAZOP M17)?**

- Expected: true
- KG: true

## L04 [Trips] PASS

**Does J105 have a thermal trip (HAZOP 9b.1)?**

- Expected: true
- KG: true

## L05 [Trips] PASS

**Is J105 stopped by liquid at the V138 vent (HAZOP 9a.7)?**

- Expected: true
- KG: true

## L06 [Trips] PASS

**Is J105 protected against running dry (HAZOP 9a.3)?**

- Expected: true
- KG: true

## D01 [Discrepancies] PASS

**Which discrepancy concerns R100?**

- Expected: discrepancy_R100_F100_labels
- KG: discrepancy_R100_F100_labels

## D02 [Discrepancies] PASS

**Which discrepancy concerns F100?**

- Expected: discrepancy_R100_F100_labels
- KG: discrepancy_R100_F100_labels

## D03 [Discrepancies] PASS

**What is the as-built situation for the tank labels?**

- Expected: Labels swapped (F100 at N2, R100 at N3)
- KG: Labels swapped (F100 at N2, R100 at N3)

## H01 [HAZOP] PASS

**Does HAZOP element 9a cover J105?**

- Expected: true
- KG: true

## H02 [HAZOP] PASS

**Does HAZOP element 9b cover R100?**

- Expected: true
- KG: true

## H03 [HAZOP] PASS

**Does HAZOP element 9b cover V146a and V147a?**

- Expected: true
- KG: true

## H04 [HAZOP] PASS

**Does HAZOP 9a.1 concern J105?**

- Expected: true
- KG: true

## H05 [HAZOP] PASS

**Do HAZOP 9a.7 and 9b.4 concern V138?**

- Expected: true
- KG: true

## H06 [HAZOP] PASS

**Does HAZOP 9b.4 concern V147a and V146a (V147/V146 in 2010)?**

- Expected: true
- KG: true

## H07 [HAZOP] PASS

**Was an RV spillback added round J105 (HAZOP 9a.1)?**

- Expected: true
- KG: true

## H08 [HAZOP] PASS

**Were check valves included after the pump (HAZOP 9a.6)?**

- Expected: true
- KG: true

## H09 [HAZOP] PASS

**Does HAZOP 9b.5 warn that wrong valving might fill E100/E101 instead of emptying?**

- Expected: true
- KG: true

## H10 [HAZOP] PASS

**Does HAZOP 9b.5 concern E100 and E101?**

- Expected: true
- KG: true

## H12 [HAZOP] PASS

**Does HAZOP 9a.3 say the pump runs dry if the tank is empty?**

- Expected: true
- KG: true

## H11 [HAZOP] PASS

**Is HAZOP item 9a.11 (wrong tank attached to J105) in element 9a?**

- Expected: true
- KG: true

## O01 [Open items] PASS

**Which open item asks which tank is which?**

- Expected: MS01, MS06, MS09
- KG: MS01, MS06, MS09

## O02 [Open items] PASS

**Which open item concerns PCV126?**

- Expected: MS04
- KG: MS04

## O03 [Open items] PASS

**Which open item concerns V138?**

- Expected: MS05
- KG: MS05

## O04 [Open items] PASS

**Which open item flags RV107 (J105 spillback or steam relief)?**

- Expected: true
- KG: true

## O05 [Open items] PASS

**How many open items does this piece hold?**

- Expected: 9
- KG: 9

## O06 [Open items] PASS

**Are MS07 and MS08 about the fill/drain header?**

- Expected: true
- KG: true

## X01 [Join] PASS

**Is V122 (stripping loop) now piped from the fill/drain header?**

- Expected: true
- KG: true

## X02 [Join] PASS

**Is V126 (piece 5) still on the K101 bottom?**

- Expected: true
- KG: true

## X03 [Join] PASS

**Does the normal figure-of-eight still connect E100 to E101 (unchanged)?**

- Expected: true
- KG: true

## X04 [Join] PASS

**Does the K101 water loop still go through Z103 to J104?**

- Expected: true
- KG: true

## X05 [Join] PASS

**Is J105 the only pump this piece adds?**

- Expected: J105
- KG: J105

## X06 [Join] PASS

**Is the filling mode a declared operating mode?**

- Expected: true
- KG: true

## X07 [Join] PASS

**Do the drains from three or more areas share the header (O8, O12, O19)?**

- Expected: true
- KG: true

## X08 [Join] PASS

**Is the header a pipe segment (not equipment)?**

- Expected: FILL_DRAIN_HEADER
- KG: FILL_DRAIN_HEADER

## X09 [Join] PASS

**Does V160 (shared with an earlier section) drop to the header?**

- Expected: true
- KG: true

## X10 [Join] PASS

**Can the receiver tank reach the feed tank (it must not, without a transfer line)?**

- Expected: false
- KG: false
