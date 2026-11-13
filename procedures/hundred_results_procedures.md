# Procedures KG: question run

PASS 50, FAIL 0, QUERY ERROR 0

## R01 [Register] PASS

**Which alarm responses does the KG hold?**

- Expected: ARP_LT101_L, ARP_LT101_H, ARP_LT104_L, ARP_LT104_H, ARP_LT108_L, ARP_LT108_H, ARP_LT401_L, ARP_LT401_H, ARP_H200_HH, ARP_E100_PSH, COM_LT101_LOW, COM_LT101_HIGH
- KG: ARP_LT104_H, ARP_LT104_L, COM_LT101_HIGH, COM_LT101_LOW, ARP_E100_PSH, ARP_LT101_H, ARP_LT101_L, ARP_LT108_H, ARP_LT108_L, ARP_LT401_H, ARP_LT401_L, ARP_H200_HH

## R02 [Register] PASS

**Which operating envelope does the KG hold?**

- Expected: ENV_J100
- KG: ENV_J100

## L01 [Thresholds] PASS

**At what level does the LT101 L alarm sound?**

- Expected: 5
- KG: 5.0

## L02 [Thresholds] PASS

**At what level does the LT101 LL trip (emergency shutdown) act?**

- Expected: 1
- KG: 1.0

## L03 [Thresholds] PASS

**At what level does the LT101 H alarm sound?**

- Expected: 85
- KG: 85.0

## L04 [Thresholds] PASS

**At what level does the LT101 HH trip act?**

- Expected: 95
- KG: 95.0

## L05 [Thresholds] PASS

**At what level does the LT108 L alarm sound?**

- Expected: 5
- KG: 5.0

## L06 [Thresholds] PASS

**At what level does the LT108 H alarm sound?**

- Expected: 85
- KG: 85.0

## L07 [Thresholds] PASS

**At what level does the LT401 L alarm sound?**

- Expected: 5
- KG: 5.0

## L08 [Thresholds] PASS

**At what level does the LT401 H alarm sound?**

- Expected: 85
- KG: 85.0

## L09 [Thresholds] PASS

**At what level does the LT104 (K101) L alarm sound?**

- Expected: 5
- KG: 5.0

## L10 [Thresholds] PASS

**At what level does the LT104 H alarm sound?**

- Expected: 85
- KG: 85.0

## L11 [Thresholds] PASS

**What is the lower commissioning limit on LT101?**

- Expected: 10
- KG: 10.0

## L12 [Thresholds] PASS

**What is the upper commissioning limit on LT101?**

- Expected: 90
- KG: 90.0

## L13 [Thresholds] PASS

**At what pressure does the E100 PSH shut the plant down?**

- Expected: 2
- KG: 2.0

## L14 [Thresholds] PASS

**In what unit is the E100 PSH set?**

- Expected: barg
- KG: barg

## L15 [Thresholds] PASS

**What kind of limit is the E100 PSH?**

- Expected: trip
- KG: trip

## L16 [Thresholds] PASS

**What is J100's upper safe pump power, allowing for cavitation?**

- Expected: 57
- KG: 57.0

## L17 [Thresholds] PASS

**What is J100's theoretical upper safe pump power?**

- Expected: 60
- KG: 60.0

## L18 [Thresholds] PASS

**What is J100's lower pump power limit?**

- Expected: 1
- KG: 1.0

## L19 [Thresholds] PASS

**Is there a PSH on E101 (HAZOP 10.8)?**

- Expected: true
- KG: true

## T01 [Triggers] PASS

**Which instrument triggers the E100 level alarm responses?**

- Expected: true
- KG: true

## T02 [Triggers] PASS

**Which instrument triggers the E101 level alarm responses?**

- Expected: true
- KG: true

## T03 [Triggers] PASS

**Which instrument triggers the condensate level responses?**

- Expected: true
- KG: true

## T04 [Triggers] PASS

**Which instrument triggers the K101 level responses?**

- Expected: true
- KG: true

## T05 [Triggers] PASS

**Which controllers trigger the heater alarm response?**

- Expected: true
- KG: true

## T06 [Triggers] PASS

**Does the LT101 low response answer both the L (5%) and LL (1%) limits?**

- Expected: true
- KG: true

## T07 [Triggers] PASS

**Does the E100 shutdown response answer the 2 barg PSH?**

- Expected: true
- KG: true

## A01 [Actions] PASS

**LT101 below 5%: is J100 reduced by 10% first?**

- Expected: true
- KG: true

## A02 [Actions] PASS

**LT101 below 5%: is J300 increased by 10%?**

- Expected: true
- KG: true

## A03 [Actions] PASS

**LT101 below 1%: is emergency shutdown initiated?**

- Expected: true
- KG: true

## A04 [Actions] PASS

**LT101 above 85%: is J100 increased by 10% first?**

- Expected: true
- KG: true

## A05 [Actions] PASS

**LT101 above 95%: is emergency shutdown initiated?**

- Expected: true
- KG: true

## A06 [Actions] PASS

**LT108 below 5%: is the running J101 pump decreased first?**

- Expected: true
- KG: true

## A07 [Actions] PASS

**LT108 above 85%: is J300 decreased by 10%?**

- Expected: true
- KG: true

## A08 [Actions] PASS

**LT401 below 5%: is J300 decreased by 10%?**

- Expected: true
- KG: true

## A09 [Actions] PASS

**LT401 above 85%: is J300 increased by 10%?**

- Expected: true
- KG: true

## A10 [Actions] PASS

**LT104 below 5%: is J103 increased by 5%?**

- Expected: true
- KG: true

## A11 [Actions] PASS

**Heaters not responding: are they switched off at the manual switch on floor 1?**

- Expected: true
- KG: true

## A12 [Actions] PASS

**Does the E100 PSH kill the steam and electrical heating?**

- Expected: true
- KG: true

## A13 [Actions] PASS

**Commissioning, LT101 above 90%: is V110 checked if the level will not drop?**

- Expected: true
- KG: true

## A14 [Actions] PASS

**Do the LT101 responses act on J100, J101a, J101b and J300?**

- Expected: true
- KG: true

## A15 [Actions] PASS

**Does the E100 PSH act on H100 and both electric heaters?**

- Expected: true
- KG: true

## E01 [Envelope] PASS

**Does the J100 envelope give 1%-57%?**

- Expected: true
- KG: true

## E02 [Envelope] PASS

**Does the J100 envelope mention cavitation?**

- Expected: true
- KG: true

## E03 [Envelope] PASS

**Is the envelope linked to J100?**

- Expected: true
- KG: true

## X01 [Join] PASS

**Does LT401 now monitor both K401 and C400?**

- Expected: true
- KG: true

## X02 [Join] PASS

**Is the commissioning response marked as not for full operation?**

- Expected: true
- KG: true

## O01 [Open items] PASS

**How many open items does this piece raise?**

- Expected: 2
- KG: 2

## O02 [Open items] PASS

**Is PR01 about the missing LL/HH values for LT108?**

- Expected: true
- KG: true
