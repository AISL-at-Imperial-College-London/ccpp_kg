# Safety logic KG: question run

PASS 58, FAIL 0, QUERY ERROR 0

## R01 [Register] PASS

**Which trips does the cause and effect matrix define?**

- Expected: TRIP_AZALL101, TRIP_FALL301, TRIP_HSZ, TRIP_LAHH104, TRIP_LALL104, TRIP_LSHH100, TRIP_LSHH103, TRIP_LSHH107, TRIP_LSHH110, TRIP_LSHH111, TRIP_LSHH112, TRIP_LSHH116, TRIP_LSHH400, TRIP_LSHH403, TRIP_LSHH404, TRIP_LSLL102, TRIP_LSLL105, TRIP_LSLL109, TRIP_LSLL112, TRIP_LSLL114, TRIP_LSLL402, TRIP_LZALL405, TRIP_PAHH401, TRIP_PALL401, TRIP_PSHH116, TRIP_PSHH117, TRIP_PSHH400, TRIP_PSHH405, TRIP_PZALL101, TRIP_TSHH106, TRIP_TSHH111a, TRIP_TSHH111b, TRIP_TSHH114, TRIP_TSHH115, TRIP_TSHH116, TRIP_TSHH212a, TRIP_TSHH212b, TRIP_TSHH310, TRIP_YS100, TRIP_YS101
- KG: TRIP_LSHH103, TRIP_LSHH111, TRIP_LSHH112, TRIP_LSLL105, TRIP_LSLL112, TRIP_LSLL114, TRIP_LZALL405, TRIP_TSHH111a, TRIP_TSHH111b, TRIP_TSHH114, TRIP_TSHH116, TRIP_TSHH310, TRIP_YS100, TRIP_YS101, TRIP_AZALL101, TRIP_FALL301, TRIP_HSZ, TRIP_LAHH104, TRIP_LALL104, TRIP_LSHH100, TRIP_LSHH107, TRIP_LSHH110, TRIP_LSHH116, TRIP_LSHH400, TRIP_LSHH403, TRIP_LSHH404, TRIP_LSLL109, TRIP_LSLL402, TRIP_PAHH401, TRIP_PSHH116, TRIP_PSHH117, TRIP_PSHH400, TRIP_PSHH405, TRIP_PZALL101, TRIP_TSHH106, TRIP_TSHH115, TRIP_TSHH212a, TRIP_TSHH212b, TRIP_LSLL102, TRIP_PALL401

## R02 [Register] PASS

**Which relief valves are in the relief valve schedule?**

- Expected: RS_RV100, RS_RV101, RS_RV102, RS_RV103, RS_RV104, RS_RV105, RS_RV106a, RS_RV106b, RS_RV107, RS_RV300, RS_RV400
- KG: RS_RV101, RS_RV102, RS_RV103, RS_RV104, RS_RV105, RS_RV107, RS_RV300, RS_RV400, RS_RV100, RS_RV106a, RS_RV106b

## R03 [Register] PASS

**How many open items does this piece raise?**

- Expected: 8
- KG: 8

## W01 [Who acts on what] PASS

**Which trips stop the filling pump J105?**

- Expected: TRIP_AZALL101, TRIP_HSZ, TRIP_LSHH110, TRIP_LSHH111, TRIP_LSHH112, TRIP_LSHH116, TRIP_LSHH400, TRIP_LSHH403, TRIP_LSHH404, TRIP_LSLL112, TRIP_LSLL114, TRIP_LZALL405, TRIP_PSHH116, TRIP_PSHH117, TRIP_PSHH400, TRIP_PSHH405, TRIP_TSHH111a, TRIP_TSHH111b, TRIP_TSHH114, TRIP_TSHH115, TRIP_TSHH116, TRIP_TSHH310, TRIP_YS100, TRIP_YS101
- KG: TRIP_LSHH111, TRIP_LSHH112, TRIP_LSLL112, TRIP_LSLL114, TRIP_LZALL405, TRIP_TSHH111a, TRIP_TSHH111b, TRIP_TSHH114, TRIP_TSHH116, TRIP_TSHH310, TRIP_YS100, TRIP_YS101, TRIP_AZALL101, TRIP_HSZ, TRIP_LSHH110, TRIP_LSHH116, TRIP_LSHH400, TRIP_LSHH403, TRIP_LSHH404, TRIP_PSHH116, TRIP_PSHH117, TRIP_PSHH400, TRIP_PSHH405, TRIP_TSHH115

## W02 [Who acts on what] PASS

**Which trips stop heater H200a?**

- Expected: TRIP_AZALL101, TRIP_HSZ, TRIP_LSHH110, TRIP_LSHH116, TRIP_LSHH400, TRIP_LSHH403, TRIP_LSHH404, TRIP_LZALL405, TRIP_PSHH116, TRIP_PSHH117, TRIP_PSHH400, TRIP_PSHH405, TRIP_TSHH111a, TRIP_TSHH111b, TRIP_TSHH114, TRIP_TSHH115, TRIP_TSHH212a, TRIP_TSHH310
- KG: TRIP_LZALL405, TRIP_TSHH111a, TRIP_TSHH111b, TRIP_TSHH114, TRIP_TSHH310, TRIP_AZALL101, TRIP_HSZ, TRIP_LSHH110, TRIP_LSHH116, TRIP_LSHH400, TRIP_LSHH403, TRIP_LSHH404, TRIP_PSHH116, TRIP_PSHH117, TRIP_PSHH400, TRIP_PSHH405, TRIP_TSHH115, TRIP_TSHH212a

## W03 [Who acts on what] PASS

**Which trips stop the CO2 compressor J103?**

- Expected: TRIP_AZALL101, TRIP_FALL301, TRIP_HSZ, TRIP_LSHH103, TRIP_LSHH107, TRIP_LSHH110, TRIP_LSHH116, TRIP_LSHH400, TRIP_LSHH403, TRIP_LSHH404, TRIP_LZALL405, TRIP_PSHH116, TRIP_PSHH117, TRIP_PSHH400, TRIP_PSHH405, TRIP_TSHH111a, TRIP_TSHH111b, TRIP_TSHH114, TRIP_TSHH115, TRIP_TSHH310
- KG: TRIP_LSHH103, TRIP_LZALL405, TRIP_TSHH111a, TRIP_TSHH111b, TRIP_TSHH114, TRIP_TSHH310, TRIP_AZALL101, TRIP_FALL301, TRIP_HSZ, TRIP_LSHH107, TRIP_LSHH110, TRIP_LSHH116, TRIP_LSHH400, TRIP_LSHH403, TRIP_LSHH404, TRIP_PSHH116, TRIP_PSHH117, TRIP_PSHH400, TRIP_PSHH405, TRIP_TSHH115

## W04 [Who acts on what] PASS

**Which trips close the steam supply valve XV140?**

- Expected: TRIP_AZALL101, TRIP_HSZ, TRIP_LSHH100, TRIP_LSHH107, TRIP_LSHH110, TRIP_LSHH116, TRIP_LSHH400, TRIP_LSHH403, TRIP_LSHH404, TRIP_LSLL102, TRIP_LSLL109, TRIP_LZALL405, TRIP_PSHH116, TRIP_PSHH117, TRIP_PSHH400, TRIP_PSHH405, TRIP_PZALL101, TRIP_TSHH111a, TRIP_TSHH111b, TRIP_TSHH114, TRIP_TSHH115, TRIP_TSHH310
- KG: TRIP_LZALL405, TRIP_TSHH111a, TRIP_TSHH111b, TRIP_TSHH114, TRIP_TSHH310, TRIP_AZALL101, TRIP_HSZ, TRIP_LSHH100, TRIP_LSHH107, TRIP_LSHH110, TRIP_LSHH116, TRIP_LSHH400, TRIP_LSHH403, TRIP_LSHH404, TRIP_LSLL109, TRIP_PSHH116, TRIP_PSHH117, TRIP_PSHH400, TRIP_PSHH405, TRIP_PZALL101, TRIP_TSHH115, TRIP_LSLL102

## W05 [Who acts on what] PASS

**What opens the C400 vent valve SDV421?**

- Expected: TRIP_PAHH401
- KG: TRIP_PAHH401

## W06 [Who acts on what] PASS

**What opens the vacuum breaker SDV424?**

- Expected: TRIP_PALL401
- KG: TRIP_PALL401

## W07 [Who acts on what] PASS

**Which trips stop the K101 water pump J104?**

- Expected: TRIP_AZALL101, TRIP_HSZ, TRIP_LSHH103, TRIP_LSHH110, TRIP_LSHH116, TRIP_LSHH400, TRIP_LSHH403, TRIP_LSHH404, TRIP_LSLL105, TRIP_LZALL405, TRIP_PSHH116, TRIP_PSHH117, TRIP_PSHH400, TRIP_PSHH405, TRIP_TSHH111a, TRIP_TSHH111b, TRIP_TSHH114, TRIP_TSHH115, TRIP_TSHH310
- KG: TRIP_LSHH103, TRIP_LSLL105, TRIP_LZALL405, TRIP_TSHH111a, TRIP_TSHH111b, TRIP_TSHH114, TRIP_TSHH310, TRIP_AZALL101, TRIP_HSZ, TRIP_LSHH110, TRIP_LSHH116, TRIP_LSHH400, TRIP_LSHH403, TRIP_LSHH404, TRIP_PSHH116, TRIP_PSHH117, TRIP_PSHH400, TRIP_PSHH405, TRIP_TSHH115

## E01 [Effects] PASS

**Does the E100 bottom pressure trip stop every pump and close the steam and supply valves?**

- Expected: true
- KG: true

## E02 [Effects] PASS

**Does a J100 over-temperature stop J100?**

- Expected: true
- KG: true

## E03 [Effects] PASS

**Does a J100 over-temperature also stop J101a (it should not)?**

- Expected: false
- KG: false

## E04 [Effects] PASS

**Does an E101 level HH stop the blower J102?**

- Expected: true
- KG: true

## E05 [Effects] PASS

**Does an E100 level HH stop the blower J102 (it should not)?**

- Expected: false
- KG: false

## E06 [Effects] PASS

**Does an E100 level HH close the steam supply valve?**

- Expected: true
- KG: true

## E07 [Effects] PASS

**Does a J101a over-temperature stop J300 (full plant shutdown)?**

- Expected: true
- KG: true

## E08 [Effects] PASS

**Does low steam pressure close FCV110?**

- Expected: true
- KG: true

## E09 [Effects] PASS

**Does a K101 level LL stop J104?**

- Expected: true
- KG: true

## E10 [Effects] PASS

**Is SDV170 opened by the operator on excess water in K101?**

- Expected: true
- KG: true

## E11 [Effects] PASS

**Is SDV169 opened by the operator when K101 has no water?**

- Expected: true
- KG: true

## E12 [Effects] PASS

**Does low CO2 return flow stop J103?**

- Expected: true
- KG: true

## E13 [Effects] PASS

**Does a disengaged feed vessel stop J105?**

- Expected: true
- KG: true

## S01 [Set points] PASS

**What is the E100 bottom pressure trip set point?**

- Expected: 2 barg (rising)
- KG: 2 barg (rising)

## S02 [Set points] PASS

**What is the E101 bottom pressure trip set point?**

- Expected: 3.5 barg (rising)
- KG: 3.5 barg (rising)

## S03 [Set points] PASS

**What is the low steam pressure trip set point?**

- Expected: 3.75 barg
- KG: 3.75 barg

## S04 [Set points] PASS

**At what oxygen level does the plant trip?**

- Expected: 19.5%
- KG: 19.5%

## S05 [Set points] PASS

**What is the H200a heater temperature trip?**

- Expected: 250 degC
- KG: 250 degC

## S06 [Set points] PASS

**What is the J300 temperature trip?**

- Expected: 60 degC
- KG: 60 degC

## S07 [Set points] PASS

**What delay is on the E100 level HH trip?**

- Expected: 1min.
- KG: 1min.

## S08 [Set points] PASS

**What delay is on the C400 level HH trip?**

- Expected: 5mins.
- KG: 5mins.

## S09 [Set points] PASS

**What delay is on the CO2 flow LL trip?**

- Expected: 2mins.
- KG: 2mins.

## S10 [Set points] PASS

**Which system handles the stripper pressure HH at 1.5 barg?**

- Expected: process control system
- KG: process control system

## S11 [Set points] PASS

**Which system handles the stripper top pressure HH at 2 barg?**

- Expected: safety system
- KG: safety system

## S12 [Set points] PASS

**Which switch detects the absorber top pressure HH?**

- Expected: PSHH405
- KG: PSHH405

## N01 [Numbers] PASS

**E101 pressure trip (barg)?**

- Expected: 3.5
- KG: 3.5

## N02 [Numbers] PASS

**Low steam pressure trip (barg)?**

- Expected: 3.75
- KG: 3.75

## N03 [Numbers] PASS

**Pressure at which the C400 vent opens (barg)?**

- Expected: 1.5
- KG: 1.5

## N04 [Numbers] PASS

**Pressure at which the vacuum breaker opens (barg)?**

- Expected: -0.05
- KG: -0.05

## N05 [Numbers] PASS

**K101 excess water level (%)?**

- Expected: 55
- KG: 55.0

## N06 [Numbers] PASS

**J103 temperature trip (degC)?**

- Expected: 85
- KG: 85.0

## N07 [Numbers] PASS

**RV104 set pressure (bar)?**

- Expected: 1
- KG: 1.0

## N08 [Numbers] PASS

**RV400 set pressure (bar)?**

- Expected: 3.8
- KG: 3.8

## N09 [Numbers] PASS

**RV103 set pressure (bar)?**

- Expected: 10
- KG: 10.0

## N10 [Numbers] PASS

**RV105 set pressure (bar)?**

- Expected: 3.8
- KG: 3.8

## C01 [Text] PASS

**Is the emergency stop a full plant shutdown?**

- Expected: true
- KG: true

## C02 [Text] PASS

**Is a J100 over-temperature a full plant shutdown (it is not)?**

- Expected: false
- KG: false

## C03 [Text] PASS

**Does a full shutdown set all control loops to manual at 0%?**

- Expected: true
- KG: true

## C04 [Text] PASS

**Does the CO2 flow trip have a start-up override?**

- Expected: true
- KG: true

## G01 [Safeguards] PASS

**Is E100 pressure safeguarded by both pressure trips and the vent and vacuum actions?**

- Expected: true
- KG: true

## G02 [Safeguards] PASS

**Is the E101 level safeguarded by its HH and LL trips?**

- Expected: true
- KG: true

## G03 [Safeguards] PASS

**Is the steam flow safeguarded by the low steam pressure trip?**

- Expected: true
- KG: true

## D01 [Detection] PASS

**Is the K102 level HH detected at K102, and the K103 level HH at K103?**

- Expected: true
- KG: true

## D02 [Detection] PASS

**Is the CO2 flow LL detected by FT301 and FT302?**

- Expected: true
- KG: true

## V01 [Relief] PASS

**What is RV100's set pressure in the schedule?**

- Expected: 3.8 bar
- KG: 3.8 bar

## V02 [Relief] PASS

**Who supplied RV400?**

- Expected: Leser Valves
- KG: Leser Valves

## V03 [Relief] PASS

**Is the schedule entry for RV300 linked to RV300?**

- Expected: true
- KG: true

## V04 [Relief] PASS

**Does the schedule include RV106a (absent on the plant per the differences document)?**

- Expected: 10 bar
- KG: 10 bar
