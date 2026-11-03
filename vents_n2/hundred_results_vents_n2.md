# Vents and N2 KG: question run

PASS 47, FAIL 0, QUERY ERROR 0

## V01 [Vents] PASS

**Is PCV119 on the vent stream (Fig F.3) to the vent system?**

- Expected: true
- KG: true

## V02 [Vents] PASS

**Is V190 on the vent stream (Fig F.3) to the vent system?**

- Expected: true
- KG: true

## V03 [Vents] PASS

**Is V197 on the vent stream (Fig F.3) to the vent system?**

- Expected: true
- KG: true

## V04 [Vents] PASS

**Is V209 on the vent stream (Fig F.3) to the vent system?**

- Expected: true
- KG: true

## V05 [Vents] PASS

**Is V315 on the vent stream (Fig F.3) to the vent system?**

- Expected: true
- KG: true

## V06 [Vents] PASS

**Is SDV421 on the vent stream (Fig F.3) to the vent system?**

- Expected: true
- KG: true

## V07 [Vents] PASS

**Is V409 on the vent stream (Fig F.3) to the vent system?**

- Expected: true
- KG: true

## V08 [Vents] PASS

**Is V411 on the vent stream (Fig F.3) to the vent system?**

- Expected: true
- KG: true

## V09 [Vents] PASS

**Does the absorber vent (after PCV300) discharge to the vent system?**

- Expected: true
- KG: true

## V10 [Vents] PASS

**Can gas from the top of E101 reach the vent system through PCV300?**

- Expected: true
- KG: true

## V11 [Vents] PASS

**Is the vent system a vent connection?**

- Expected: VENT_SYSTEM
- KG: VENT_SYSTEM

## V12 [Vents] PASS

**Do the relief valves RV400 and RV401 still discharge to K403?**

- Expected: true
- KG: true

## K01 [K403] PASS

**What grid is K403 at (report colour P&ID)?**

- Expected: B11
- KG: B11

## K02 [K403] PASS

**Does the K403 note cite the report colour P&ID?**

- Expected: true
- KG: true

## K03 [K403] PASS

**Is open item VN03 about where K403 drains?**

- Expected: true
- KG: true

## N01 [N2 header] PASS

**What comes after PCV117 on the N2 header branch?**

- Expected: true
- KG: true

## N02 [N2 header] PASS

**Does NRV109 feed the N2 header?**

- Expected: true
- KG: true

## N03 [N2 header] PASS

**Does the header feed both tank check valves?**

- Expected: true
- KG: true

## N04 [N2 header] PASS

**Does NRV107 feed F100 (left tank)?**

- Expected: true
- KG: true

## N05 [N2 header] PASS

**Does NRV108 feed R100 (right tank)?**

- Expected: true
- KG: true

## N06 [N2 header] PASS

**Does N2 from the supply reach both tanks?**

- Expected: true
- KG: true

## N07 [N2 header] PASS

**Can N2 from the supply reach F100?**

- Expected: true
- KG: true

## N08 [N2 header] PASS

**Can N2 from the header reach the E100 MEA side (it must not)?**

- Expected: false
- KG: false

## N09 [N2 header] PASS

**Is NRV104 on the N2 header (team trace)?**

- Expected: true
- KG: true

## N10 [N2 header] PASS

**Does the N2 header route include PI114?**

- Expected: true
- KG: true

## N11 [N2 header] PASS

**Does the N2 header route start at the N2 supply?**

- Expected: true
- KG: true

## N12 [N2 header] PASS

**Is the N2 header a pipe segment?**

- Expected: N2_PURGE_HEADER
- KG: N2_PURGE_HEADER

## N13 [N2 header] PASS

**Does PCV117 still feed PCV115 (the feed line is unchanged)?**

- Expected: true
- KG: true

## W01 [Make-up water] PASS

**What does the make-up water supply feed first?**

- Expected: NRV100a
- KG: NRV100a

## W02 [Make-up water] PASS

**What does NRV100a feed?**

- Expected: NRV100b
- KG: NRV100b

## W03 [Make-up water] PASS

**Is the deionising cartridge after the NRVs (HAZOP 4.8)?**

- Expected: true
- KG: true

## W04 [Make-up water] PASS

**Does the deionising cartridge feed K101?**

- Expected: true
- KG: true

## W05 [Make-up water] PASS

**Does make-up water reach K101?**

- Expected: true
- KG: true

## W06 [Make-up water] PASS

**What grid is the make-up water supply at?**

- Expected: Q18
- KG: Q18

## W07 [Make-up water] PASS

**Which supply connection does this piece add?**

- Expected: MAKEUP_WATER_SUPPLY
- KG: MAKEUP_WATER_SUPPLY

## W08 [Make-up water] PASS

**Which filter does this piece add?**

- Expected: DI_CARTRIDGE
- KG: DI_CARTRIDGE

## W09 [Make-up water] PASS

**Does HAZOP 4.8 concern the deionising cartridge?**

- Expected: true
- KG: true

## W10 [Make-up water] PASS

**Was a deionising cartridge added (HAZOP 4.8)?**

- Expected: true
- KG: true

## W11 [Make-up water] PASS

**Can make-up water reach E101 through K101?**

- Expected: true
- KG: true

## O01 [Open items] PASS

**How many open items does this piece hold?**

- Expected: 6
- KG: 6

## O02 [Open items] PASS

**Is VN01 about the vent system?**

- Expected: true
- KG: true

## O03 [Open items] PASS

**Is VN06 about the make-up water?**

- Expected: true
- KG: true

## O04 [Open items] PASS

**Is VN05 about the N2 header?**

- Expected: true
- KG: true

## X01 [Join] PASS

**Does the N2 header route use the N2 supply and V127 from piece 5?**

- Expected: true
- KG: true

## X02 [Join] PASS

**Is the MEA filling route unchanged (F100 still feeds J105)?**

- Expected: true
- KG: true

## X03 [Join] PASS

**Is the CO2 recycle round K103 unchanged (PCV119 to K103)?**

- Expected: true
- KG: true

## X04 [Join] PASS

**Is the K101 water loop unchanged (Z103 to J104)?**

- Expected: true
- KG: true
