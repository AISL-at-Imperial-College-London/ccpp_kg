# Electrical KG: question run

PASS 33, FAIL 0, QUERY ERROR 0

## R01 [Register] PASS

**Which motors does the cable diagram show?**

- Expected: M100, M101A, M101B, M102, M103, M104, M105, M300
- KG: M101A, M101B, M102, M103, M104, M105, M300, M100

## R02 [Register] PASS

**Which supplies does the cable diagram show?**

- Expected: EL_230V_L1, EL_230V_L2, EL_230V_L3, EL_415V
- KG: EL_230V_L1, EL_230V_L2, EL_230V_L3, EL_415V

## R03 [Register] PASS

**Which panels does the cable diagram show?**

- Expected: CA1, CS1, DB301, DB302, DB303, FB1, MC1, PP2, PP4, RC2, RC3, RC4, UPS1, UPS2, UPS3
- KG: CA1, DB301, DB302, DB303, PP2, PP4, UPS1, UPS2, UPS3, RC3, CS1, FB1, MC1, RC2, RC4

## R04 [Register] PASS

**How many open items does this piece raise?**

- Expected: 5
- KG: 5

## P01 [Power walk] PASS

**What is lost if the motor control panel MC1 loses power?**

- Expected: H200a, H200b, J100, J101a, J101b, J102, J103, J104, J105, J300, M100, M101A, M101B, M102, M103, M104, M105, M300
- KG: H200a, H200b, M100, J100, M101A, J101a, M101B, J101b, M102, J102, M103, J103, M104, J104, M105, J105, M300, J300

## P02 [Power walk] PASS

**What does distribution board DB303 feed?**

- Expected: CA1
- KG: CA1

## P03 [Power walk] PASS

**What is lost if UPS1 fails (its board DB301 and everything downstream)?**

- Expected: AT100, AT300, CS1, DB301, FB1, FT102, FT103, FT201, FT302, FT304, FT305, PP2, PP4, RC2, RC3, RC4
- KG: DB301, CS1, FB1, AT100, AT300, FT102, FT103, FT201, FT302, FT304, FT305, RC2, PP2, RC3, RC4, PP4

## P04 [Power walk] PASS

**Which instruments take 110 V from the fieldbus panel FB1?**

- Expected: AT100, AT300, FT102, FT103, FT201, FT302, FT304, FT305
- KG: AT100, AT300, FT102, FT103, FT201, FT302, FT304, FT305

## P05 [Power walk] PASS

**What feeds the CO2 compressor J103, back to the supply?**

- Expected: EL_415V, M103, MC1
- KG: M103, MC1, EL_415V

## P06 [Power walk] PASS

**What feeds FT201, back to the supplies?**

- Expected: DB301, DB302, EL_230V_L1, EL_230V_L2, FB1, UPS1, UPS2
- KG: FB1, DB301, UPS1, EL_230V_L1, DB302, UPS2, EL_230V_L2

## P07 [Power walk] PASS

**Does the 230 V supply L1 reach FT201?**

- Expected: true
- KG: true

## P08 [Power walk] PASS

**Does the 415 V supply reach FT201 (it should not)?**

- Expected: false
- KG: false

## P09 [Power walk] PASS

**Does UPS3 feed the control system panel CS1 (it should not)?**

- Expected: false
- KG: false

## P10 [Power walk] PASS

**Is the control system panel CS1 fed from both DB301 and DB302?**

- Expected: true
- KG: true

## P11 [Power walk] PASS

**Does the 415 V supply reach both heaters?**

- Expected: true
- KG: true

## M01 [Motors] PASS

**What is the rated power of M100 (J100)?**

- Expected: 2.2 kW
- KG: 2.2 kW

## M02 [Motors] PASS

**What is the rated power of M101A (J101a)?**

- Expected: 2.2 kW
- KG: 2.2 kW

## M03 [Motors] PASS

**What is the rated power of M101B (J101b)?**

- Expected: 2.2 kW
- KG: 2.2 kW

## M04 [Motors] PASS

**What is the rated power of M102 (J102)?**

- Expected: 3 kW
- KG: 3 kW

## M05 [Motors] PASS

**What is the rated power of M103 (J103)?**

- Expected: 4 kW
- KG: 4 kW

## M06 [Motors] PASS

**What is the rated power of M104 (J104)?**

- Expected: 0.55 kW
- KG: 0.55 kW

## M07 [Motors] PASS

**What is the rated power of M105 (J105)?**

- Expected: 0.55 kW
- KG: 0.55 kW

## M08 [Motors] PASS

**What is the rated power of M300 (J300)?**

- Expected: 0.37 kW
- KG: 0.37 kW

## M09 [Motors] PASS

**Which machine does M103 drive?**

- Expected: J103
- KG: J103

## M10 [Motors] PASS

**Which machine does M300 drive?**

- Expected: J300
- KG: J300

## N01 [Numbers] PASS

**J102 motor rating (kW)?**

- Expected: 3
- KG: 3.0

## N02 [Numbers] PASS

**J103 motor rating (kW)?**

- Expected: 4
- KG: 4.0

## N03 [Numbers] PASS

**H200a rating (kW)?**

- Expected: 9
- KG: 9.0

## N04 [Numbers] PASS

**J300 motor rating (kW)?**

- Expected: 0.37
- KG: 0.37

## F01 [Floors] PASS

**Which floor is the motor control panel on?**

- Expected: 1
- KG: 1

## F02 [Floors] PASS

**Which floor is remote I/O panel RC4 on?**

- Expected: 4
- KG: 4

## F03 [Floors] PASS

**Which floor is the J300 motor on?**

- Expected: 2
- KG: 2

## F04 [Floors] PASS

**Which floor is remote I/O panel RC2 on?**

- Expected: 2
- KG: 2
