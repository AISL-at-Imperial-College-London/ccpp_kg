# MEA storage KG: 100-question run

PASS 7, FAIL 93, QUERY ERROR 0

## F01 [Filling] FAIL

**What does the feed tank F100 feed?**

- Expected: J105
- KG: (no rows)

## F02 [Filling] FAIL

**What does J105 pump into?**

- Expected: FILL_DRAIN_HEADER
- KG: (no rows)

## F03 [Filling] FAIL

**Does MEA from F100 reach the fill/drain header?**

- Expected: true
- KG: false

## F04 [Filling] PASS

**Does the filling route leak into the normal E100 flow path (it must not)?**

- Expected: false
- KG: false

## F05 [Filling] PASS

**Does normal running flow into the receiver tank (it must not)?**

- Expected: false
- KG: false

## F06 [Filling] FAIL

**Does the filling route include TT116?**

- Expected: true
- KG: false

## F07 [Filling] FAIL

**Does the filling route include PCV126?**

- Expected: true
- KG: false

## F08 [Filling] FAIL

**Does the filling route include the V138 manual vent?**

- Expected: true
- KG: false

## F09 [Filling] PASS

**Does F100 feed the header directly (skipping J105)?**

- Expected: false
- KG: false

## F10 [Filling] FAIL

**Is the filling route in the Filling operating mode?**

- Expected: Filling
- KG: (no rows)

## P01 [Piping] FAIL

**Is the header piped back to the receiver tank R100?**

- Expected: true
- KG: false

## P02 [Piping] FAIL

**Is the header piped to V115 and V122 at J100 (HAZOP M14)?**

- Expected: true
- KG: false

## P03 [Piping] FAIL

**Do the J101 fill/drain valves V146a/b and V147a/b connect to the header?**

- Expected: true
- KG: false

## P04 [Piping] FAIL

**Do the drains V153, V154 and V155 drop to the header?**

- Expected: true
- KG: false

## P05 [Piping] FAIL

**Do V160, V167 and V168 drop to the header?**

- Expected: true
- KG: false

## P06 [Piping] FAIL

**Do V148 and V149 drop to the header?**

- Expected: true
- KG: false

## P07 [Piping] FAIL

**Does the K101 bottom outlet V126 run to the header (team trace)?**

- Expected: true
- KG: false

## P08 [Piping] FAIL

**Can K101 reach the header through V126?**

- Expected: true
- KG: false

## E01 [Equipment] FAIL

**Which storage tanks are there?**

- Expected: F100, R100
- KG: (no rows)

## E02 [Equipment] FAIL

**Which pump does this piece add?**

- Expected: J105
- KG: (no rows)

## E03 [Equipment] FAIL

**Which pressure control valve does this piece add?**

- Expected: PCV126
- KG: (no rows)

## E04 [Equipment] FAIL

**Which check valves does this piece add?**

- Expected: NRV107, NRV108
- KG: (no rows)

## E05 [Equipment] FAIL

**What grid is J105 at?**

- Expected: N4
- KG: (no rows)

## E06 [Equipment] FAIL

**Which floor is J105 on?**

- Expected: 1
- KG: (no rows)

## E07 [Equipment] FAIL

**What grid is the feed tank F100 at (as built)?**

- Expected: N2
- KG: (no rows)

## E08 [Equipment] FAIL

**What grid is the receiver tank R100 at (as built)?**

- Expected: N3
- KG: (no rows)

## E09 [Equipment] FAIL

**Does the F100 note say it is the feed tank?**

- Expected: true
- KG: false

## E10 [Equipment] FAIL

**Does the R100 note say it is the receiver tank?**

- Expected: true
- KG: false

## V01 [Valves] FAIL

**What grid is PCV126 at?**

- Expected: N5
- KG: (no rows)

## V02 [Valves] FAIL

**What grid is V156 at?**

- Expected: N6
- KG: (no rows)

## V03 [Valves] FAIL

**Is V156 normally closed?**

- Expected: closed
- KG: (no rows)

## V04 [Valves] FAIL

**What grid is V157 at?**

- Expected: N5
- KG: (no rows)

## V05 [Valves] FAIL

**What grid is V158 at?**

- Expected: O4
- KG: (no rows)

## V06 [Valves] FAIL

**What grid is V159a at?**

- Expected: O3
- KG: (no rows)

## V07 [Valves] FAIL

**What grid is V159b at?**

- Expected: O2
- KG: (no rows)

## V08 [Valves] FAIL

**What grid is V161a at?**

- Expected: O3
- KG: (no rows)

## V09 [Valves] FAIL

**What grid is V161b at?**

- Expected: O2
- KG: (no rows)

## V10 [Valves] FAIL

**What grid is V162 at?**

- Expected: N2
- KG: (no rows)

## V11 [Valves] FAIL

**What grid is V163 at?**

- Expected: O3
- KG: (no rows)

## V12 [Valves] FAIL

**What grid is V164 at?**

- Expected: N3
- KG: (no rows)

## V13 [Valves] FAIL

**What grid is V199 at?**

- Expected: O4
- KG: (no rows)

## V14 [Valves] FAIL

**What grid is V153 at?**

- Expected: O8
- KG: (no rows)

## V15 [Valves] FAIL

**Is V153 normally closed?**

- Expected: closed
- KG: (no rows)

## V16 [Valves] FAIL

**What grid is V155 at?**

- Expected: O7
- KG: (no rows)

## V17 [Valves] FAIL

**What grid is V167 at?**

- Expected: N9
- KG: (no rows)

## V18 [Valves] FAIL

**What grid is V149 at?**

- Expected: O12
- KG: (no rows)

## V19 [Valves] FAIL

**What grid is V148 at?**

- Expected: O13
- KG: (no rows)

## V20 [Valves] FAIL

**What grid is V146a at?**

- Expected: O15
- KG: (no rows)

## V21 [Valves] FAIL

**What grid is V147b at?**

- Expected: O16
- KG: (no rows)

## V22 [Valves] FAIL

**What grid is NRV107 at?**

- Expected: N2
- KG: (no rows)

## V23 [Valves] FAIL

**What grid is NRV108 at?**

- Expected: N3
- KG: (no rows)

## V24 [Valves] FAIL

**What kind of valve is V138?**

- Expected: manual vent
- KG: (no rows)

## V25 [Valves] FAIL

**What grid is V168 at?**

- Expected: N9
- KG: (no rows)

## I01 [Instruments] FAIL

**What type of sensor is TT116?**

- Expected: PRT
- KG: (no rows)

## I02 [Instruments] FAIL

**What signal does TT116 use?**

- Expected: 4-20mA
- KG: (no rows)

## I03 [Instruments] FAIL

**What grid is TT116 at?**

- Expected: N5
- KG: (no rows)

## I04 [Instruments] FAIL

**What does TT116 monitor?**

- Expected: J105
- KG: (no rows)

## I05 [Instruments] FAIL

**Do FI110 and PI112 sit at the tank at N2 (F100)?**

- Expected: true
- KG: false

## I06 [Instruments] FAIL

**Do FI111 and PI113 sit at the tank at N3 (R100)?**

- Expected: true
- KG: false

## I07 [Instruments] FAIL

**What grid is FI110 at?**

- Expected: N2
- KG: (no rows)

## I08 [Instruments] FAIL

**What grid is FI111 at?**

- Expected: M3
- KG: (no rows)

## I09 [Instruments] FAIL

**What grid is PI112 at?**

- Expected: N2
- KG: (no rows)

## I10 [Instruments] FAIL

**What grid is PI113 at?**

- Expected: M3
- KG: (no rows)

## L01 [Trips] FAIL

**What kind of limit is on the receiver tank level?**

- Expected: trip
- KG: (no rows)

## L02 [Trips] FAIL

**Does the receiver tank have a high-level trip (HAZOP M16)?**

- Expected: true
- KG: false

## L03 [Trips] FAIL

**Does the feed tank have a low-level trip (HAZOP M17)?**

- Expected: true
- KG: false

## L04 [Trips] FAIL

**Does J105 have a thermal trip (HAZOP 9b.1)?**

- Expected: true
- KG: false

## L05 [Trips] FAIL

**Is J105 stopped by liquid at the V138 vent (HAZOP 9a.7)?**

- Expected: true
- KG: false

## L06 [Trips] FAIL

**Is J105 protected against running dry (HAZOP 9a.3)?**

- Expected: true
- KG: false

## D01 [Discrepancies] FAIL

**Which discrepancy concerns R100?**

- Expected: discrepancy_R100_F100_labels
- KG: (no rows)

## D02 [Discrepancies] FAIL

**Which discrepancy concerns F100?**

- Expected: discrepancy_R100_F100_labels
- KG: (no rows)

## D03 [Discrepancies] FAIL

**What is the as-built situation for the tank labels?**

- Expected: Labels swapped (F100 at N2, R100 at N3)
- KG: (no rows)

## H01 [HAZOP] FAIL

**Does HAZOP element 9a cover J105?**

- Expected: true
- KG: false

## H02 [HAZOP] FAIL

**Does HAZOP element 9b cover R100?**

- Expected: true
- KG: false

## H03 [HAZOP] FAIL

**Does HAZOP element 9b cover V146a and V147a?**

- Expected: true
- KG: false

## H04 [HAZOP] FAIL

**Does HAZOP 9a.1 concern J105?**

- Expected: true
- KG: false

## H05 [HAZOP] FAIL

**Do HAZOP 9a.7 and 9b.4 concern V138?**

- Expected: true
- KG: false

## H06 [HAZOP] FAIL

**Does HAZOP 9b.4 concern V147a and V146a (V147/V146 in 2010)?**

- Expected: true
- KG: false

## H07 [HAZOP] FAIL

**Was an RV spillback added round J105 (HAZOP 9a.1)?**

- Expected: true
- KG: false

## H08 [HAZOP] FAIL

**Were check valves included after the pump (HAZOP 9a.6)?**

- Expected: true
- KG: false

## H09 [HAZOP] FAIL

**Does HAZOP 9b.5 warn that wrong valving might fill E100/E101 instead of emptying?**

- Expected: true
- KG: false

## H10 [HAZOP] FAIL

**Does HAZOP 9b.5 concern E100 and E101?**

- Expected: true
- KG: false

## H12 [HAZOP] FAIL

**Does HAZOP 9a.3 say the pump runs dry if the tank is empty?**

- Expected: true
- KG: false

## H11 [HAZOP] FAIL

**Is HAZOP item 9a.11 (wrong tank attached to J105) in element 9a?**

- Expected: true
- KG: false

## O01 [Open items] FAIL

**Which open item asks which tank is which?**

- Expected: MS01, MS06, MS09
- KG: (no rows)

## O02 [Open items] FAIL

**Which open item concerns PCV126?**

- Expected: MS04
- KG: (no rows)

## O03 [Open items] FAIL

**Which open item concerns V138?**

- Expected: MS05
- KG: (no rows)

## O04 [Open items] FAIL

**Which open item flags RV107 (J105 spillback or steam relief)?**

- Expected: true
- KG: false

## O05 [Open items] FAIL

**How many open items does this piece hold?**

- Expected: 9
- KG: 0

## O06 [Open items] FAIL

**Are MS07 and MS08 about the fill/drain header?**

- Expected: true
- KG: false

## X01 [Join] FAIL

**Is V122 (stripping loop) now piped from the fill/drain header?**

- Expected: true
- KG: false

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

## X05 [Join] FAIL

**Is J105 the only pump this piece adds?**

- Expected: J105
- KG: (no rows)

## X06 [Join] FAIL

**Is the filling mode a declared operating mode?**

- Expected: true
- KG: false

## X07 [Join] FAIL

**Do the drains from three or more areas share the header (O8, O12, O19)?**

- Expected: true
- KG: false

## X08 [Join] FAIL

**Is the header a pipe segment (not equipment)?**

- Expected: FILL_DRAIN_HEADER
- KG: (no rows)

## X09 [Join] FAIL

**Does V160 (shared with an earlier section) drop to the header?**

- Expected: true
- KG: false

## X10 [Join] PASS

**Can the receiver tank reach the feed tank (it must not, without a transfer line)?**

- Expected: false
- KG: false
