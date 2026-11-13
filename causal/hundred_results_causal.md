# Causal layer KG: question run

PASS 46, FAIL 0, QUERY ERROR 0

## R01 [Register] PASS

**Which process variables does the causal layer define?**

- Expected: V_C106_CW, V_C200_CW, V_C200_IN_T, V_C400_CW, V_C400_T, V_CO2_FEED, V_CO2_RET, V_E100_CO2_RELEASE, V_E100_L, V_E100_P, V_E100_T, V_E101_CO2_OUT, V_E101_GAS, V_E101_L, V_E101_P, V_FEED_SAT, V_H200_DUTY, V_J100_CAV, V_J103_CARRY, V_K101_T, V_K401_DP, V_K401_L, V_K402_CARRY, V_LEAN_FLOW, V_LEAN_T, V_RICH_FLOW, V_RICH_T, V_STEAM, V_Z102_DP
- KG: V_K401_L, V_C106_CW, V_H200_DUTY, V_FEED_SAT, V_K101_T, V_K401_DP, V_K402_CARRY, V_C200_CW, V_C400_CW, V_CO2_FEED, V_E100_CO2_RELEASE, V_RICH_T, V_Z102_DP, V_C200_IN_T, V_C400_T, V_E101_GAS, V_E101_P, V_J100_CAV, V_J103_CARRY, V_RICH_FLOW, V_CO2_RET, V_E100_L, V_E101_L, V_LEAN_T, V_STEAM, V_LEAN_FLOW, V_E100_T, V_E101_CO2_OUT, V_E100_P

## R02 [Register] PASS

**Which process events does the causal layer define?**

- Expected: X_C100_NO_XFLOW, X_C200_CW_LOST, X_C400_CW_LOST, X_FCV105_STUCK, X_FCV111_OPENS, X_GAS_FEED_HIGH, X_J100_FAST, X_J101_STOPS, X_J102_STOPS, X_J103_STOPS, X_J104_STOPS, X_K401_BLOCKED, X_PCV119_CLOSED, X_PCV300_CLOSED, X_STEAM_EXCESS, X_STEAM_FAIL, X_Z102_BLOCKED
- KG: X_C100_NO_XFLOW, X_C200_CW_LOST, X_C400_CW_LOST, X_FCV105_STUCK, X_FCV111_OPENS, X_GAS_FEED_HIGH, X_J100_FAST, X_J101_STOPS, X_J102_STOPS, X_J103_STOPS, X_J104_STOPS, X_PCV119_CLOSED, X_PCV300_CLOSED, X_STEAM_EXCESS, X_STEAM_FAIL, X_Z102_BLOCKED, X_K401_BLOCKED

## R03 [Register] PASS

**How many open items does the causal layer raise?**

- Expected: 2
- KG: 2

## C01 [Causes (multi-hop)] PASS

**What can affect E100 pressure, directly or through other variables?**

- Expected: V_C400_CW, V_C400_T, V_CO2_RET, V_E100_P, V_E100_T, V_H200_DUTY, V_RICH_T, V_STEAM, X_C400_CW_LOST, X_J103_STOPS, X_K401_BLOCKED, X_PCV119_CLOSED, X_STEAM_EXCESS, X_STEAM_FAIL
- KG: X_PCV119_CLOSED, V_C400_T, V_C400_CW, X_C400_CW_LOST, V_E100_T, V_RICH_T, V_H200_DUTY, V_STEAM, X_STEAM_EXCESS, X_STEAM_FAIL, V_E100_P, V_CO2_RET, X_J103_STOPS, X_K401_BLOCKED

## C02 [Causes (multi-hop)] PASS

**What can affect the CO2 left in the gas leaving E101, directly or through other variables?**

- Expected: V_C200_CW, V_C200_IN_T, V_C400_CW, V_C400_T, V_CO2_FEED, V_CO2_RET, V_E100_CO2_RELEASE, V_E100_P, V_E100_T, V_H200_DUTY, V_LEAN_FLOW, V_LEAN_T, V_RICH_T, V_STEAM, V_Z102_DP, X_C100_NO_XFLOW, X_C200_CW_LOST, X_C400_CW_LOST, X_FCV105_STUCK, X_J100_FAST, X_J103_STOPS, X_K401_BLOCKED, X_PCV119_CLOSED, X_STEAM_EXCESS, X_STEAM_FAIL, X_Z102_BLOCKED
- KG: V_CO2_FEED, X_FCV105_STUCK, V_LEAN_T, V_C200_IN_T, X_C100_NO_XFLOW, V_C200_CW, X_C200_CW_LOST, V_E100_CO2_RELEASE, V_E100_T, V_RICH_T, V_H200_DUTY, V_STEAM, X_STEAM_EXCESS, X_STEAM_FAIL, V_E100_P, X_PCV119_CLOSED, V_C400_T, V_C400_CW, X_C400_CW_LOST, V_CO2_RET, X_J103_STOPS, X_K401_BLOCKED, V_LEAN_FLOW, X_J100_FAST, V_Z102_DP, X_Z102_BLOCKED

## C03 [Causes (multi-hop)] PASS

**What can affect the lean MEA temperature into E101 (TT210), directly or through other variables?**

- Expected: V_C200_CW, V_C200_IN_T, X_C100_NO_XFLOW, X_C200_CW_LOST
- KG: V_C200_IN_T, X_C100_NO_XFLOW, V_C200_CW, X_C200_CW_LOST

## C04 [Causes (multi-hop)] PASS

**What can affect the E101 level (LT108), directly or through other variables?**

- Expected: V_LEAN_FLOW, V_RICH_FLOW, V_Z102_DP, X_J100_FAST, X_J101_STOPS, X_Z102_BLOCKED
- KG: V_LEAN_FLOW, X_J100_FAST, V_Z102_DP, X_Z102_BLOCKED, V_RICH_FLOW, X_J101_STOPS

## C05 [Causes (multi-hop)] PASS

**What can affect carry-over to J103, directly or through other variables?**

- Expected: V_C400_CW, V_C400_T, V_CO2_RET, V_E100_P, V_E100_T, V_H200_DUTY, V_RICH_T, V_STEAM, X_C400_CW_LOST, X_J103_STOPS, X_K401_BLOCKED, X_PCV119_CLOSED, X_STEAM_EXCESS, X_STEAM_FAIL
- KG: V_C400_T, V_C400_CW, X_C400_CW_LOST, V_E100_T, V_RICH_T, V_H200_DUTY, V_STEAM, X_STEAM_EXCESS, X_STEAM_FAIL, V_E100_P, X_PCV119_CLOSED, V_CO2_RET, X_J103_STOPS, X_K401_BLOCKED

## C06 [Causes (multi-hop)] PASS

**What can affect the J100 cavitation risk, directly or through other variables?**

- Expected: V_C200_IN_T, V_E100_L, V_LEAN_FLOW, V_RICH_FLOW, V_Z102_DP, X_C100_NO_XFLOW, X_J100_FAST, X_J101_STOPS, X_Z102_BLOCKED
- KG: V_C200_IN_T, X_C100_NO_XFLOW, V_E100_L, V_RICH_FLOW, X_J101_STOPS, V_LEAN_FLOW, X_J100_FAST, V_Z102_DP, X_Z102_BLOCKED

## C07 [Causes (multi-hop)] PASS

**What can affect the E100 level (LT101), directly or through other variables?**

- Expected: V_LEAN_FLOW, V_RICH_FLOW, V_Z102_DP, X_J100_FAST, X_J101_STOPS, X_Z102_BLOCKED
- KG: V_RICH_FLOW, X_J101_STOPS, V_LEAN_FLOW, X_J100_FAST, V_Z102_DP, X_Z102_BLOCKED

## F01 [Consequences (multi-hop)] PASS

**What is affected if cooling water to C400 is lost?**

- Expected: V_C400_CW, V_C400_T, V_E100_CO2_RELEASE, V_E100_P, V_E100_T, V_E101_CO2_OUT, V_J103_CARRY
- KG: V_C400_CW, V_C400_T, V_E100_P, V_E100_T, V_E100_CO2_RELEASE, V_E101_CO2_OUT, V_J103_CARRY

## F02 [Consequences (multi-hop)] PASS

**What is affected if the steam supply fails?**

- Expected: V_E100_CO2_RELEASE, V_E100_P, V_E100_T, V_E101_CO2_OUT, V_J103_CARRY, V_STEAM
- KG: V_STEAM, V_E100_T, V_E100_CO2_RELEASE, V_E101_CO2_OUT, V_E100_P, V_J103_CARRY

## F03 [Consequences (multi-hop)] PASS

**What is affected if the K401 demister blocks?**

- Expected: V_CO2_RET, V_E100_CO2_RELEASE, V_E100_P, V_E100_T, V_E101_CO2_OUT, V_J103_CARRY, V_K401_DP
- KG: V_K401_DP, V_CO2_RET, V_E100_P, V_E100_T, V_E100_CO2_RELEASE, V_E101_CO2_OUT, V_J103_CARRY

## F04 [Consequences (multi-hop)] PASS

**What is affected if J101 stops?**

- Expected: V_E100_L, V_E101_L, V_J100_CAV, V_K402_CARRY, V_RICH_FLOW
- KG: V_RICH_FLOW, V_E100_L, V_J100_CAV, V_E101_L, V_K402_CARRY

## F05 [Consequences (multi-hop)] PASS

**What is affected if rich MEA stops flowing through C100?**

- Expected: V_C200_IN_T, V_E101_CO2_OUT, V_J100_CAV, V_LEAN_T
- KG: V_C200_IN_T, V_J100_CAV, V_LEAN_T, V_E101_CO2_OUT

## D01 [Direction] PASS

**Does PCV119 failing closed raise E100 pressure?**

- Expected: true
- KG: true

## D02 [Direction] PASS

**Does hotter lean MEA raise the CO2 left in the E101 outlet gas?**

- Expected: true
- KG: true

## D03 [Direction] PASS

**Does more C400 cooling water lower the C400 gas outlet temperature?**

- Expected: true
- KG: true

## D04 [Direction] PASS

**Does more lean MEA flow lower the E100 level?**

- Expected: true
- KG: true

## D05 [Direction] PASS

**Does more rich MEA flow raise the E100 level?**

- Expected: true
- KG: true

## D06 [Direction] PASS

**Does a hotter C400 outlet raise E100 pressure (HAZOP 12.7)?**

- Expected: true
- KG: true

## D07 [Direction] PASS

**Does J102 stopping lower the N2 flow up E101?**

- Expected: true
- KG: true

## D08 [Direction] PASS

**Does a hotter stripper release more CO2?**

- Expected: true
- KG: true

## D09 [Direction] PASS

**Does more lean MEA flow raise the E100 level (it should not)?**

- Expected: false
- KG: false

## P01 [Paths] PASS

**Can losing C400 cooling water raise E100 pressure through the chain?**

- Expected: true
- KG: true

## P02 [Paths] PASS

**Can a steam failure affect CO2 capture in E101 (four steps)?**

- Expected: true
- KG: true

## P03 [Paths] PASS

**Can J102 stopping affect E100 pressure (it should not, in this layer)?**

- Expected: false
- KG: false

## P04 [Paths] PASS

**Can a blocked Z102 affect the E101 level?**

- Expected: true
- KG: true

## I01 [Links] PASS

**Which instruments read E100 pressure?**

- Expected: PT401, PT402
- KG: PT401, PT402

## I02 [Links] PASS

**Which instrument reads the lean MEA temperature into E101?**

- Expected: TT210
- KG: TT210

## I03 [Links] PASS

**Which instrument reads the K401/C400 condensate level?**

- Expected: LT401
- KG: LT401

## I04 [Links] PASS

**Which controller regulates the lean MEA temperature into E101?**

- Expected: TIC210
- KG: TIC210

## I05 [Links] PASS

**Which controllers regulate E100 pressure?**

- Expected: PIC401, PIC402
- KG: PIC401, PIC402

## I06 [Links] PASS

**Which controller regulates the C400 gas outlet temperature?**

- Expected: TIC410
- KG: TIC410

## S01 [Safeguards] PASS

**Is E100 pressure safeguarded by the 2 barg PSH, its shutdown response and RV401?**

- Expected: true
- KG: true

## S02 [Safeguards] PASS

**Is E101 pressure safeguarded by RV400 and its PSH?**

- Expected: true
- KG: true

## S03 [Safeguards] PASS

**Is the C400 cooling water safeguarded by the FT402 low-flow alarm?**

- Expected: true
- KG: true

## S04 [Safeguards] PASS

**Is the CO2 return safeguarded by its low-flow alarm and the J103 trip?**

- Expected: true
- KG: true

## S05 [Safeguards] PASS

**Are the LT101 alarm responses safeguards on the E100 level?**

- Expected: true
- KG: true

## S06 [Safeguards] PASS

**Is the J100 cavitation risk safeguarded by its envelope and LZAL102?**

- Expected: true
- KG: true

## B01 [Basis] PASS

**Is the C400-to-E100-pressure link based on the HAZOP?**

- Expected: true
- KG: true

## B02 [Basis] PASS

**Does that link explain the mechanism (less condensation)?**

- Expected: true
- KG: true

## B03 [Basis] PASS

**Is the CO2-return-to-E100-pressure link marked as a physical rule?**

- Expected: true
- KG: true

## B04 [Basis] PASS

**Does the lean temperature link say hot MEA absorbs CO2 less well?**

- Expected: true
- KG: true

## X01 [Join] PASS

**Is the causal link for PCV119 recorded with its cause and effect nodes?**

- Expected: true
- KG: true

## X02 [Join] PASS

**Is the steam failure event tied to the steam supply (piece 8)?**

- Expected: true
- KG: true
