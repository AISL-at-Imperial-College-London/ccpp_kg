# KG_A: third-party question test

| Category | Questions | Supported | Partial | Not supported | Mean key-item recall |
|---|---|---|---|---|---|
| cause_and_effect | 18 | 14 | 4 | 0 | 83% |
| control | 10 | 9 | 1 | 0 | 92% |
| fact | 12 | 10 | 2 | 0 | 94% |
| multi_hop | 14 | 8 | 2 | 4 | 68% |
| safety_actions | 12 | 6 | 6 | 0 | 79% |
| topology | 14 | 9 | 3 | 2 | 80% |
| **All** | 80 | 56 | 18 | 6 | 82% |

## Q01 [fact] SUPPORTED (100%)

**What is the grid reference of pump J100?**

- Expected: Pump J100 is located at grid reference M10 on floor 1. It transfers lean MEA from the stripper E100 towards the absorber E101.
- Source: PilotPlantReport_Group6_2.0.pdf, Appendix F, Figure F.6
- Key items found: J100, M10, 1
- Key items missing: none
- Evidence lines: 400

## Q02 [fact] SUPPORTED (100%)

**Where is pump J101b located?**

- Expected: Pump J101b is located at grid reference N16 on floor 1. It is one of the two pumps used to transfer rich MEA from E101 towards E100.
- Source: PilotPlantReport_Group6_2.0.pdf, Appendix F, Figure F.6
- Key items found: J101b, N16, 1
- Key items missing: none
- Evidence lines: 400

## Q03 [fact] SUPPORTED (100%)

**On which floor and at which grid reference is heater H200a located?**

- Expected: H200a is located on floor 2 at grid reference J10. It is one of the two pre-heaters associated with the rich MEA feed to E100.
- Source: PilotPlantReport_Group6_2.0.pdf, Appendix F, Figure F.5
- Key items found: H200a, J10, 2
- Key items missing: none
- Evidence lines: 284

## Q04 [fact] SUPPORTED (100%)

**What is the grid reference of the steam flow control valve FCV110?**

- Expected: FCV110 is located at grid reference L5 on floor 1. It controls steam flow towards reboiler H100.
- Source: PilotPlantReport_Group6_2.0.pdf, Appendix F, Figure F.11
- Key items found: FCV110, L5, 1
- Key items missing: none
- Evidence lines: 192

## Q05 [fact] SUPPORTED (100%)

**Which communication protocol is specified for level transmitter LT101?**

- Expected: LT101 uses Profibus-PA. It is a differential-pressure-based level transmitter located at grid K8 on floor 1, measuring the liquid level in E100.
- Source: PilotPlantReport_Group6_2.0.pdf, Appendix C.4.2, Figure C.13
- Key items found: LT101, Profibus-PA, K8
- Key items missing: none
- Evidence lines: 60

## Q06 [fact] SUPPORTED (100%)

**What type of flowmeter is FT108?**

- Expected: FT108 is a Coriolis mass flow meter. It is situated at grid N13 on floor 1 and uses a 4-20mA signal. It measures rich MEA flow in the transfer system from E101 towards E100.
- Source: PilotPlantReport_Group6_2.0.pdf, Appendix C.5.2, Figure C.23
- Key items found: FT108, N13, 4-20mA
- Key items missing: none
- Evidence lines: 150

## Q07 [fact] PARTIAL (67%)

**What measurement method and signal protocol does AT400 use?**

- Expected: AT400 uses infrared absorption for gas composition analysis and transmits a 4-20mA signal. It is associated with the absorber gas sampling system on floor 4.
- Source: PilotPlantReport_Group6_2.0.pdf, Appendix C.6.2, Figure C.28; P&ID Differences.pdf, page 1
- Key items found: AT400, 4
- Key items missing: 4-20mA
- Evidence lines: 70

## Q08 [fact] SUPPORTED (100%)

**At which grid reference is the absorber level transmitter LT108 located?**

- Expected: LT108 is located at grid K15 on floor 1. It measures the liquid level in the absorber column E101.
- Source: PilotPlantReport_Group6_2.0.pdf, Appendix C.4.2, Figure C.13
- Key items found: LT108, K15, E101
- Key items missing: none
- Evidence lines: 400

## Q09 [fact] SUPPORTED (100%)

**What is the actual operating pressure of B300, rather than the value shown on the P&ID?**

- Expected: B300 operates at 3 bar, rather than the 8 bar indicated on the original drawing. The discrepancy is identified at grid G9.
- Source: P&ID Differences.pdf, page 2, B300, grid G9
- Key items found: B300, 3 bar, 8 bar
- Key items missing: none
- Evidence lines: 70

## Q10 [fact] PARTIAL (67%)

**On which floor are V402 and V403 physically located?**

- Expected: V402 and V403 are physically located on 3/F, not 4/F as might be inferred from the original P&ID. Their drawing reference is F8.
- Source: P&ID Differences.pdf, page 1, V402 & V403, grid F8
- Key items found: V402, V403
- Key items missing: 3/F
- Evidence lines: 368

## Q11 [fact] SUPPORTED (100%)

**Where should PCV120b be located in the actual plant?**

- Expected: PCV120b, which is not shown on the original P&ID, should be located between pump J101b and B103b. The indicated drawing location is grid N17.
- Source: P&ID Differences.pdf, page 2, PCV120b, grid N17
- Key items found: PCV120b, J101b, B103b, N17
- Key items missing: none
- Evidence lines: 123

## Q12 [fact] SUPPORTED (100%)

**Which vessel receives the relief connections from RV400 and RV401?**

- Expected: K403 is the knockout drum connected to RV400 and RV401. It is an additional safety vessel not included in the original P&ID.
- Source: P&ID Differences.pdf, page 1, K403, grids E15/16 and E7
- Key items found: K403, RV400, RV401
- Key items missing: none
- Evidence lines: 242

## Q13 [topology] PARTIAL (60%)

**Trace the main rich MEA route from the bottom of E101 to the inlet of E100.**

- Expected: Rich MEA leaves the bottom of the absorber E101, is transferred by the operating rich MEA pump J101a or J101b, and passes through the cross exchanger C100, where it is heated by hot lean MEA. It is subsequently heated by the H200 pre-heater arrangement before entering the top of the stripper E100.
- Source: PilotPlantReport_Group6_2.0.pdf, Appendix F.3 and Figure F.1; Appendix D.4.1
- Key items found: E101, J101a, E100
- Key items missing: J101b, C100
- Evidence lines: 400

## Q14 [topology] NOT SUPPORTED (20%)

**Trace the lean MEA circulation route from E100 back to E101, identifying the main heat-transfer equipment and pump.**

- Expected: Lean MEA leaves the bottom of E100 and enters C100, where it transfers heat to the incoming rich MEA. The cooled lean stream travels to J100, through the lean MEA transfer and filtration system incorporating Z102, and then to the trim cooler C200. From C200, lean MEA enters the top of E101 for renewed CO2 absorption.
- Source: PilotPlantReport_Group6_2.0.pdf, Section 3.2, Appendix F.3 and Figure F.1; 27794_Plant_HAZREP, Element 7
- Key items found: E100
- Key items missing: C100, J100, Z102, C200
- Evidence lines: 400

## Q15 [topology] SUPPORTED (100%)

**Which process streams pass through the two sides of C100, and where do those streams originate?**

- Expected: C100 receives hot lean MEA originating from the stripper E100 and cooler rich MEA originating from the absorber E101. The lean MEA transfers heat to the rich MEA, cooling the former while preheating the latter before it proceeds towards E100.
- Source: PilotPlantReport_Group6_2.0.pdf, Section 3.2, pages 12-13
- Key items found: C100, E100, E101
- Key items missing: none
- Evidence lines: 400

## Q16 [topology] SUPPORTED (100%)

**Where does lean MEA flow after leaving C200, and which transmitter measures its outlet temperature?**

- Expected: Lean MEA leaving C200 flows towards the top of absorber E101. The temperature of the stream after cooling and before entry to the absorber is measured by TT210.
- Source: PilotPlantReport_Group6_2.0.pdf, Appendix D.4.4.d, Figures D.26-D.27
- Key items found: C200, E101, TT210
- Key items missing: none
- Evidence lines: 400

## Q17 [topology] PARTIAL (60%)

**Trace the CO2-rich overhead stream from E100 through the condensation and gas recovery system.**

- Expected: Vapour leaves the top of E100 and enters condenser C400. The overhead recovery arrangement also includes cooler C401 and separation equipment K401, which removes entrained liquid from the CO2-rich gas. The separated CO2 proceeds towards compressor J103 for recycling into the gas feed system. Condensed liquid is handled separately through the condensate return arrangement.
- Source: 27794_Plant_CP.docx, Process Overview and Overview instrumentation table; PilotPlantReport_Group6_2.0.pdf, Appendix F.1; 27794_Plant_HAZREP, Elements 6 and 12
- Key items found: E100, C400, K401
- Key items missing: C401, J103
- Evidence lines: 400

## Q18 [topology] SUPPORTED (100%)

**Where does liquid recovered in the condenser system return, and which pump provides the transfer?**

- Expected: Liquid collected in the condenser C400 system is transferred by pump J300 back towards the stripper E100 as the condensate or reflux return. The level in C400 is controlled through the operation of J300.
- Source: 27794_Plant_CP.docx, LIC-401 and SIC-300 control loops; PilotPlantReport_Group6_2.0.pdf, Appendix D.4.2.b
- Key items found: C400, J300, E100
- Key items missing: none
- Evidence lines: 400

## Q19 [topology] SUPPORTED (100%)

**What is the nitrogen return path after gas leaves the top of E101?**

- Expected: Nitrogen-rich gas exits the absorber E101 and passes through cyclone separator K402 to remove entrained liquid. It then enters the nitrogen return system containing blower J102. The returned nitrogen is recycled towards the gas mixing and saturation vessel K101 before re-entering E101.
- Source: 27794_Plant_HAZREP, Element 5; PilotPlantReport_Group6_2.0.pdf, Appendix F.3 and Figure F.1
- Key items found: E101, K402, J102, K101
- Key items missing: none
- Evidence lines: 400

## Q20 [topology] PARTIAL (75%)

**How do the fresh CO2 and N2 feeds reach the absorber?**

- Expected: The fresh CO2 supply passes through the feed arrangement containing FCV105, while nitrogen is supplied through the arrangement containing FCV116. These gases join the recirculated gas system and enter K101, where the feed mixture is prepared before it passes into absorber E101.
- Source: PilotPlantReport_Group6_2.0.pdf, Appendix D.4.1.a and D.4.1.c; Appendix F.5.6
- Key items found: FCV105, K101, E101
- Key items missing: FCV116
- Evidence lines: 400

## Q21 [topology] SUPPORTED (100%)

**How is water circulated around the gas saturator K101, and which exchanger is associated with its temperature regulation?**

- Expected: Water is recirculated from K101 back to K101 using pump J104. The temperature-regulation arrangement includes heat exchanger C106, where a separate cooling water supply removes heat from the circulating water before it is used for gas saturation.
- Source: 27794_Plant_HAZREP, Element 4; PilotPlantReport_Group6_2.0.pdf, Appendix D.4.4.b
- Key items found: K101, J104, C106
- Key items missing: none
- Evidence lines: 400

## Q22 [topology] SUPPORTED (100%)

**Which steam supply components are upstream of reboiler H100?**

- Expected: Steam is admitted through the steam supply system, which includes the main supply valves V100, V101 and V102, and the modulating valve FCV110. XV140 is also part of the steam start-up valve arrangement. Steam enters reboiler H100 to heat the circulating MEA, while condensate is removed through the steam and condensate system.
- Source: PilotPlantReport_Group6_2.0.pdf, Appendix F.5.5, Figure F.11
- Key items found: V100, V101, V102, FCV110, H100
- Key items missing: none
- Evidence lines: 400

## Q23 [topology] SUPPORTED (100%)

**Describe the cooling water route and associated instrumentation around C200, including the real position of FI200.**

- Expected: Cooling water enters the C200 cooling arrangement through the control valve FCV200. FT201 provides the flow measurement used by the cooling water control loop. FI200 is physically downstream of FCV200, even though the original P&ID shows it before the valve. This cooling circuit removes heat from lean MEA travelling towards E101.
- Source: PilotPlantReport_Group6_2.0.pdf, Appendix D.4.4.d; P&ID Differences.pdf, page 1, FI200
- Key items found: C200, FCV200, FT201, FI200
- Key items missing: none
- Evidence lines: 400

## Q24 [topology] SUPPORTED (100%)

**Which instruments and control valve are associated with the cooling water supply to condenser C400?**

- Expected: The C400 cooling water supply is measured by FT402, regulated by FIC402 and adjusted using FCV401. Cooling water passing through C400 removes heat from the stripper overhead stream.
- Source: PilotPlantReport_Group6_2.0.pdf, Appendix D.4.4.e, Figures D.28-D.29
- Key items found: C400, FT402, FIC402, FCV401
- Key items missing: none
- Evidence lines: 400

## Q25 [topology] NOT SUPPORTED (0%)

**Which control valve regulates the cooling water supplied to C401, and which controller operates it?**

- Expected: The water-cooled exchanger C401 has its cooling water flow regulated by FCV402 under the control of FIC404. Increasing the opening of FCV402 increases the cooling water flow through the exchanger.
- Source: 27794_Plant_CP.docx, Control Loops, FIC-404
- Key items found: none
- Key items missing: C401, FCV402, FIC404
- Evidence lines: 0

## Q26 [topology] SUPPORTED (100%)

**How is gas from the absorber connected to the controlled venting system?**

- Expected: Gas leaving E101 passes into the gas separation and return arrangement containing K402. A controlled vent path is provided through PCV300. The pressure control system regulates the amount of lean gas discharged rather than recirculated, helping maintain the pressure in E101.
- Source: PilotPlantReport_Group6_2.0.pdf, Appendix D.4.3.b; 27794_Plant_CP.docx, PIC-403 process control
- Key items found: E101, K402, PCV300
- Key items missing: none
- Evidence lines: 400

## Q27 [multi_hop] NOT SUPPORTED (20%)

**Starting with the flow measurement, which control chain adjusts lean MEA flow from E100 into E101?**

- Expected: FT103 or FT104 measures the lean MEA flow. The corresponding controller FIC103 or FIC104 compares the measurement with the operator's set point and sends a command to SIC100, which adjusts the speed of pump J100. Changing J100 speed changes the flow of regenerated lean MEA from E100 towards E101.
- Source: PilotPlantReport_Group6_2.0.pdf, Appendix D.4.1.d, Figures D.10-D.11
- Key items found: E101
- Key items missing: FT103, FIC103, SIC100, J100
- Evidence lines: 400

## Q28 [multi_hop] PARTIAL (60%)

**If J101b is the active rich MEA pump, how does the system measure and adjust the flow towards E100?**

- Expected: FT108 and FT109 provide alternative rich MEA flow measurements to FIC108 and FIC109. The selected flow controller supplies the required speed command to SIC101b, which adjusts J101b. This changes rich MEA transfer from the bottom of E101 through C100 towards E100. HS107 selects the alternative flow control loops.
- Source: 27794_Plant_CP.docx, Control Loops, FIC-108, FIC-109, HS-107 and SIC-101a/b
- Key items found: SIC101b, J101b, E100
- Key items missing: FT109, FIC109
- Evidence lines: 400

## Q29 [multi_hop] NOT SUPPORTED (0%)

**Which complete control chain responds when the lean MEA temperature entering E101 is above its set point?**

- Expected: TT210 detects the high lean MEA temperature after C200. TIC210 calculates a higher required cooling water flow and sends that requirement to FIC201 as its flow set point. FT201 measures actual cooling water flow, and FIC201 opens FCV200 further to increase cooling through C200. This reduces the lean MEA temperature entering E101.
- Source: PilotPlantReport_Group6_2.0.pdf, Appendix D.4.4.d, Figures D.26-D.27
- Key items found: none
- Key items missing: TT210, TIC210, FT201, FIC201, FCV200
- Evidence lines: 400

## Q30 [multi_hop] SUPPORTED (100%)

**Which linked instruments and controllers increase reboiler heating when the MEA temperature returning to E100 is too low?**

- Expected: TT100 measures the temperature of MEA returning from H100 to E100. TIC100 increases the steam flow set point for the secondary controller FIC100. FT100 and FT101 measure steam flow, allowing FIC100 to increase the opening of FCV110. More steam enters H100 and increases the heating of the MEA.
- Source: PilotPlantReport_Group6_2.0.pdf, Appendix D.4.4.c, Figures D.24-D.25
- Key items found: TT100, TIC100, FIC100, FCV110, H100
- Key items missing: none
- Evidence lines: 400

## Q31 [multi_hop] SUPPORTED (100%)

**Which instruments link a high temperature in the C400 overhead cooling system to an increase in cooling water flow?**

- Expected: The control description identifies TT410 as the temperature input to TIC410. TIC410 calculates a new cooling water flow set point for FIC402. FT402 measures the actual cooling water flow, and FIC402 increases the opening of FCV401 to increase cooling through C400. The Control Philosophy separately describes the TT410 measurement location as the gas line downstream of the condensate separator, so its exact physical position should be checked against that document.
- Source: PilotPlantReport_Group6_2.0.pdf, Appendix D.4.4.e, Figures D.28-D.29; 27794_Plant_CP.docx, Stripper Column instrumentation table
- Key items found: TT410, TIC410, FT402, FIC402, FCV401
- Key items missing: none
- Evidence lines: 400

## Q32 [multi_hop] SUPPORTED (100%)

**Which measurement, controller and actuator are linked to the pressure of E101?**

- Expected: PT403 provides the absorber pressure measurement used by PIC403. The controller compares this reading with its set point and adjusts PCV300, which controls the quantity of lean gas vented from the absorber return system. Increasing the vent flow reduces pressure in E101.
- Source: PilotPlantReport_Group6_2.0.pdf, Appendix D.4.3.b, Figures D.18-D.19
- Key items found: PT403, PIC403, PCV300, E101
- Key items missing: none
- Evidence lines: 400

## Q33 [multi_hop] SUPPORTED (100%)

**Which two pressure measurements can be selected to control PCV119, and where are they located?**

- Expected: PT401 is connected to the CO2 overhead line between E100 and C400 and supplies PIC401. PT402 is situated downstream of separator K401 and supplies PIC402. HS401 selects the pressure control loop, and the selected controller operates PCV119 to regulate the stripper pressure.
- Source: PilotPlantReport_Group6_2.0.pdf, Appendix D.4.3.a; 27794_Plant_CP.docx, PIC-401, PIC-402 and HS-401
- Key items found: PT401, PT402, PIC401, PIC402, PCV119
- Key items missing: none
- Evidence lines: 151

## Q34 [multi_hop] PARTIAL (75%)

**Which instrument chain controls the fresh nitrogen feed entering K101?**

- Expected: FT116 measures the fresh nitrogen supply flow to K101. FIC116 compares that flow with the required nitrogen feed rate and adjusts FCV116. Opening FCV116 increases the nitrogen supplied to the gas mixing system, changing the mixture sent towards E101.
- Source: PilotPlantReport_Group6_2.0.pdf, Appendix D.4.1.a, Figures D.4-D.5
- Key items found: FIC116, FCV116, K101
- Key items missing: FT116
- Evidence lines: 400

## Q35 [multi_hop] SUPPORTED (100%)

**Which components would be involved in correcting an excessive fresh CO2 feed concentration at K101?**

- Expected: The fresh CO2 flow is measured by FT105 and controlled by FIC105 acting on FCV105. A high CO2 concentration detected through the gas composition sampling system, including Sample 7, can indicate excessive CO2 addition. FIC105 can reduce the opening of FCV105 to decrease the fresh CO2 supplied to K101.
- Source: PilotPlantReport_Group6_2.0.pdf, Appendix D.4.1.c, Figures D.8-D.9
- Key items found: FT105, FIC105, FCV105, K101
- Key items missing: none
- Evidence lines: 400

## Q36 [multi_hop] SUPPORTED (100%)

**How do the nitrogen recycle flow measurements control the amount of gas returning to E101?**

- Expected: FT303 and FT304 measure nitrogen flow in the recycle system. Their corresponding controllers FIC303 and FIC304 control FCV111. Opening FCV111 increases the bypass or spillback flow in the nitrogen return circuit around J102 and reduces the amount passing towards E101. Closing FCV111 increases the nitrogen flow returning to the absorber.
- Source: PilotPlantReport_Group6_2.0.pdf, Appendix D.4.1.b; 27794_Plant_CP.docx, FIC-303 and FIC-304
- Key items found: FT303, FT304, FIC303, FCV111, J102
- Key items missing: none
- Evidence lines: 400

## Q37 [multi_hop] NOT SUPPORTED (0%)

**How is the condensate level measurement converted into a return-flow adjustment?**

- Expected: LT401 measures the condensate level in C400. LIC401 compares the measured level with its set point and sends a speed command through SIC300 to pump J300. Increasing the speed of J300 removes condensate faster and reduces the level in C400 while returning recovered liquid towards E100.
- Source: PilotPlantReport_Group6_2.0.pdf, Appendix D.4.2.b; 27794_Plant_CP.docx, LIC-401
- Key items found: none
- Key items missing: LT401, LIC401, SIC300, J300, C400
- Evidence lines: 0

## Q38 [multi_hop] NOT SUPPORTED (0%)

**Which two analytical instruments allow the operator to compare rich and lean MEA condition on opposite sides of the regeneration cycle?**

- Expected: AT100 measures the pH of rich MEA travelling from the absorber pumping system towards C100, while AT300 measures lean MEA pH after C200 on the return towards E101. Comparing AT100 and AT300 allows the operator to evaluate the condition of solvent on the rich and lean sides of the cycle. These readings are analytical information rather than a direct measure of CO2 loading.
- Source: 27794_Plant_CP.docx, Overview and Gas and pH Analysing tables; PilotPlantReport_Group6_2.0.pdf, Appendix C.6.2
- Key items found: none
- Key items missing: AT100, AT300, C100, C200
- Evidence lines: 0

## Q39 [multi_hop] SUPPORTED (100%)

**If H100 appears to be heating unexpectedly, which linked measurements and valves should be investigated?**

- Expected: First inspect FT100 and FT101 to establish whether steam is flowing towards H100. If flow exists unexpectedly, verify that FCV110 is closed and check the manual steam isolation valves V100, V101 and V102. Relevant temperature readings should also be compared. The commissioning SOP calls for further investigation by an engineer if temperatures continue rising despite the indicated valves being closed.
- Source: PilotPlantReport_Group6_2.0.pdf, Appendix E.3.5 and Appendix F.5.5
- Key items found: H100, FT100, FT101, FCV110, V100
- Key items missing: none
- Evidence lines: 400

## Q40 [multi_hop] SUPPORTED (100%)

**If J101a fails and J101b must take over, which pump and valve changes connect the standby route into the rich MEA loop?**

- Expected: J101a should be stopped and J101b selected as the redundant rich MEA pump. The J101a route is isolated and the J101b operating route is established using the valve positions in Figure F.9, including opening V134b, V135b, V143b and V144b. The redundant J101b pump is then started at 10% power and increased gradually according to the pump failure procedure. Operators should verify the correct rich MEA transfer and levels.
- Source: PilotPlantReport_Group6_2.0.pdf, Appendix F.8.2 and Figure F.9
- Key items found: J101a, J101b, V134b, V135b, V143b
- Key items missing: none
- Evidence lines: 400

## Q41 [control] SUPPORTED (80%)

**How does the E101 liquid level control loop work, including its sensor and actuator?**

- Expected: LT108 measures the liquid level in absorber E101. LIC108 compares the measurement with the operator's level set point and commands SIC101a or SIC101b, depending on which of J101a or J101b is operating. If the measured level is high, pump speed increases to remove rich MEA faster. If the measured level is low, pump speed decreases.
- Source: PilotPlantReport_Group6_2.0.pdf, Appendix D.4.2.a, Figures D.12-D.13
- Key items found: LT108, LIC108, J101a, E101
- Key items missing: SIC101a
- Evidence lines: 400

## Q42 [control] SUPPORTED (100%)

**Describe the stripper pressure control loop and the alternative measurement channels.**

- Expected: The stripper pressure control arrangement uses PT401 with PIC401 or PT402 with PIC402. HS401 selects between the alternative controllers. The selected controller regulates PCV119 in the CO2 recycle system. In the report's control-loop explanation, an increase in stripper pressure produces a command to open PCV119 further to increase bypass or recycle flow and reduce the pressure.
- Source: PilotPlantReport_Group6_2.0.pdf, Appendix D.4.3.a; 27794_Plant_CP.docx, Pressure Control Loops
- Key items found: PT401, PIC401, PT402, PIC402, PCV119
- Key items missing: none
- Evidence lines: 400

## Q43 [control] SUPPORTED (100%)

**What happens in the absorber pressure control loop when PT403 indicates pressure above the set point?**

- Expected: PT403 reports the absorber pressure to PIC403. PIC403 determines that E101 is above its pressure set point and instructs PCV300 to open further. Increasing the flow of vented lean gas reduces the absorber pressure. If the pressure falls below the set point, the reverse action reduces vent flow.
- Source: PilotPlantReport_Group6_2.0.pdf, Appendix D.4.3.b
- Key items found: PT403, PIC403, PCV300, E101
- Key items missing: none
- Evidence lines: 400

## Q44 [control] SUPPORTED (100%)

**Explain the master and slave controllers used to regulate heating through H100.**

- Expected: The master loop measures MEA temperature using TT100 and uses TIC100 to calculate the required steam flow set point. The secondary flow loop uses FT100 and FT101 with FIC100, which modulates FCV110. By increasing or decreasing steam entering H100, the cascade maintains the desired temperature of MEA returning to E100.
- Source: PilotPlantReport_Group6_2.0.pdf, Appendix D.4.4.c
- Key items found: TT100, TIC100, FIC100, FCV110, H100
- Key items missing: none
- Evidence lines: 400

## Q45 [control] SUPPORTED (100%)

**How does the cascade control system maintain the lean MEA temperature after C200?**

- Expected: TT210 measures lean MEA temperature after C200 and supplies the master controller TIC210. TIC210 calculates a cooling water flow set point for FIC201. FT201 supplies the actual flow measurement, and FIC201 modulates FCV200. Hotter-than-required MEA results in a higher cooling water flow set point; colder-than-required MEA results in a lower one.
- Source: PilotPlantReport_Group6_2.0.pdf, Appendix D.4.4.d
- Key items found: TT210, TIC210, FT201, FIC201, FCV200
- Key items missing: none
- Evidence lines: 400

## Q46 [control] SUPPORTED (100%)

**What are the master sensor, slave flow measurement and final actuator for the C400 cooling control system?**

- Expected: Appendix D identifies TT410 as the temperature measurement used by master controller TIC410. The slave flow control loop is FIC402, using FT402 to measure cooling water flow and FCV401 as the final actuator. TIC410 changes the cooling water set point to regulate temperature in the C400 overhead cooling arrangement.
- Source: PilotPlantReport_Group6_2.0.pdf, Appendix D.4.4.e
- Key items found: TT410, TIC410, FT402, FIC402, FCV401
- Key items missing: none
- Evidence lines: 400

## Q47 [control] SUPPORTED (100%)

**How is the temperature of water entering K101 regulated using C106?**

- Expected: TT121 measures the relevant water temperature for master controller TIC121. TIC121 adjusts the set point of the secondary flow controller FIC106. FT106 measures cooling water flow through C106, and FIC106 modulates FCV102. When the measured temperature is too high, the master loop requests more cooling water; when too low, it requests less.
- Source: PilotPlantReport_Group6_2.0.pdf, Appendix D.4.4.b
- Key items found: TT121, TIC121, FT106, FIC106, FCV102
- Key items missing: none
- Evidence lines: 400

## Q48 [control] PARTIAL (60%)

**Which controller maintains the condensate level in C400 and how is its output implemented?**

- Expected: LIC401 regulates condensate level in C400 using the measurement from LT401. Its output is sent through SIC300 to adjust J300 speed. Higher condensate level causes increased pumping, while lower condensate level causes reduced pumping.
- Source: 27794_Plant_CP.docx, LIC-401 and SIC-300; PilotPlantReport_Group6_2.0.pdf, Appendix D.4.2.b
- Key items found: LT401, J300, C400
- Key items missing: LIC401, SIC300
- Evidence lines: 400

## Q49 [control] SUPPORTED (80%)

**How does the control system regulate nitrogen return flow towards the absorber?**

- Expected: The alternative measurements FT303 and FT304 are associated with controllers FIC303 and FIC304. The selected controller operates FCV111 in the recycle bypass. Opening FCV111 increases nitrogen bypass flow and decreases the nitrogen returning to E101; closing it increases the amount returning to the absorber. HS301 selects the alternative control loops.
- Source: 27794_Plant_CP.docx, FIC-303, FIC-304 and HS-301; PilotPlantReport_Group6_2.0.pdf, Appendix D.4.1.b
- Key items found: FT303, FT304, FIC303, FCV111
- Key items missing: HS301
- Evidence lines: 400

## Q50 [control] SUPPORTED (100%)

**Which sensor and controllers determine the heating duties of H200a and H200b?**

- Expected: TT213 measures the temperature of rich MEA entering E100 after the pre-heater arrangement. TIC213a and TIC213b use this temperature measurement to regulate H200a and H200b respectively. When the measured temperature is below the set point, heat duty is increased; when it is above the set point, heat duty is reduced.
- Source: PilotPlantReport_Group6_2.0.pdf, Appendix D.4.4.a
- Key items found: TT213, TIC213a, TIC213b, H200a, H200b
- Key items missing: none
- Evidence lines: 400

## Q51 [cause_and_effect] PARTIAL (60%)

**If the CO2 concentration in gas leaving the top of E101 increases unexpectedly, what plant changes could explain it?**

- Expected: Causes: Insufficient lean MEA entering E101 because J100 flow has decreased, or excessive fresh CO2 addition through FCV105, could increase the CO2 concentration reaching the top of the absorber. An excessively hot MEA feed after C200 can also impair absorption. Consequences: Less CO2 is captured and more CO2 remains in the nitrogen-rich outlet gas. Safeguards: FT103 and FT104 monitor lean MEA flow, FT105 monitors fresh CO2 flow, and the absorber gas analysis arrangement AT400 provides composition information. Actions: Compare the gas composition measurements with FT103, FT104 and FT105; inspect the temperature after C200; restore the documented MEA, gas feed and cooling control set points as appropriate.
- Source: PilotPlantReport_Group6_2.0.pdf, Sections 4.1-4.3 and Appendix D.4.1; 27794_Plant_HAZREP, Elements 1, 7 and 10
- Key items found: E101, FCV105, AT400
- Key items missing: J100, C200
- Evidence lines: 400

## Q52 [cause_and_effect] SUPPORTED (80%)

**If lean MEA leaving C100 is unusually hot, what could be wrong with the rich MEA side of the exchanger?**

- Expected: Causes: Low or absent rich MEA crossflow through C100 reduces the ability of that stream to remove heat from the hot lean MEA. This may result from reduced rich MEA circulation through J101a or J101b. Consequences: The lean stream remains hotter than expected, increasing the cooling demand on C200 and potentially contributing to poor J100 operating conditions or cavitation. Rich MEA also receives less useful preheating. Safeguards: Rich MEA flow is measured by FT108 and FT109, while the HAZOP records temperature warnings TAH210/211 for the downstream thermal condition. Actions: Compare rich and lean flow measurements, check the operating J101 pump and the C100 flow route, and investigate the temperature alarms before increasing circulation.
- Source: 27794_Plant_HAZREP, Element 7, TEMP (C200 inlet)—HIGHER; PilotPlantReport_Group6_2.0.pdf, Section 3.2
- Key items found: C100, J100, C200, FT108
- Key items missing: J101a
- Evidence lines: 400

## Q53 [cause_and_effect] PARTIAL (60%)

**TT210 shows the MEA entering E101 is too hot. What could cause this, and how would it affect absorption?**

- Expected: Causes: Insufficient cooling water through C200, reduced opening of FCV200, or a loss of cooling duty could produce a high TT210 reading. Consequences: Hotter MEA enters E101, reducing the efficiency of CO2 absorption as identified in the HAZOP. Safeguards: TIC210 and FIC201 regulate temperature and cooling water flow using FT201 and FCV200; the plant also has low cooling water flow warning FAL201. Actions: Check FT201, FCV200 and the cooling water supply, verify the temperature set point, and restore adequate cooling before continuing normal absorption operation.
- Source: 27794_Plant_HAZREP, Elements 7 and 10, TEMP—HIGHER; PilotPlantReport_Group6_2.0.pdf, Appendix D.4.4.d; 27794_Plant_CP.docx, Lean MEA alarm table
- Key items found: TT210, C200, E101
- Key items missing: FCV200, FAL201
- Evidence lines: 400

## Q54 [cause_and_effect] SUPPORTED (80%)

**If TT213 is below the required rich MEA feed temperature, what might be happening in the pre-heater system?**

- Expected: Causes: The heating duties of H200a or H200b may be insufficient, their temperature set points may be too low, or rich MEA may be arriving colder than expected from C100. Consequences: Rich MEA enters E100 at a lower temperature, increasing the heating requirement for regeneration and potentially reducing the rate of CO2 release. Safeguards: TT213 supplies temperature information to TIC213a and TIC213b, which regulate H200a and H200b. Actions: Check TT213 against the required set point, inspect the heater control settings and upstream C100 temperature, and correct the heating duty using the documented control arrangement.
- Source: PilotPlantReport_Group6_2.0.pdf, Appendix D.4.4.a; Appendix F.5.4
- Key items found: TT213, TIC213a, H200a, H200b
- Key items missing: C100
- Evidence lines: 117

## Q55 [cause_and_effect] PARTIAL (40%)

**The temperature and pressure in E100 are both rising. What heating-system faults could explain this?**

- Expected: Causes: Excessive steam admission through FCV110 into H100 or excessive heating of rich MEA by H200a and H200b could increase heat input to the stripper. Failure of the pressure control system could also contribute. Consequences: Increased boiling, higher vapour generation and pressure, and potentially increased MEA degradation. Safeguards: The temperature control loops TIC100 and TIC213a/b regulate heat input; the stripper pressure control arrangement uses PCV119. The HAZOP records a high-pressure shutdown at 2 barg. Actions: Check the temperature and pressure measurements, reduce excessive heat input using the applicable controls, investigate PCV119 and initiate the documented shutdown arrangements if the pressure trip condition is reached.
- Source: 27794_Plant_HAZREP, Element 11, TEMP and PRESSURE—HIGHER; MISC Notes M4; PilotPlantReport_Group6_2.0.pdf, Appendix D.4.3-D.4.4
- Key items found: E100, PCV119
- Key items missing: FCV110, H100, 2 barg
- Evidence lines: 400

## Q56 [cause_and_effect] SUPPORTED (100%)

**What happens to E100 regeneration if the steam supply to H100 is lost?**

- Expected: Causes: Loss of building steam supply, closed steam isolation valves, or an obstruction in the steam and condensate circuit can reduce or eliminate steam flow to H100. Consequences: Reboiler heating decreases, CO2 liberation from rich MEA is reduced, and the stripping process becomes inefficient or cannot operate as intended. Safeguards: FT100 and FT101 provide steam flow measurements, and the HAZOP records plant shutdown on steam failure or absence. Actions: Check FT100 and FT101, investigate the steam supply and valve lineup, do not assume the reboiler is operating normally, and follow the shutdown requirement for unavailable steam.
- Source: 27794_Plant_HAZREP, Element 13, FLOW—NO and TEMP—LOWER; PilotPlantReport_Group6_2.0.pdf, Appendix F.5.5
- Key items found: E100, H100, FT100, FT101
- Key items missing: none
- Evidence lines: 400

## Q57 [cause_and_effect] SUPPORTED (100%)

**If cooling water flow through C400 falls significantly, what could happen to the CO2 return system?**

- Expected: Causes: Inadequate cooling water supply, reduced opening of FCV401, or a fault in the cooling water circuit could reduce the duty of C400. Consequences: The overhead vapour is not cooled sufficiently, potentially allowing hot vapour or water carryover towards K401 and J103, where it could damage the compressor. Safeguards: FT402 monitors the cooling water flow, FIC402 regulates FCV401, and the HAZOP records a low cooling flow alarm and additional warning against carryover. Actions: Check FT402 and FCV401, investigate the cooling supply and the separator condition, and restore cooling before continuing normal CO2 compression.
- Source: 27794_Plant_HAZREP, Elements 6 and 12; PilotPlantReport_Group6_2.0.pdf, Appendix D.4.4.e
- Key items found: C400, FCV401, FT402, K401, J103
- Key items missing: none
- Evidence lines: 400

## Q58 [cause_and_effect] SUPPORTED (100%)

**What would happen if the demister in K401 became blocked?**

- Expected: Causes: An obstruction in the K401 demister restricts the CO2 overhead flow after C400. Consequences: Gas flow towards J103 can fall or stop, disrupting CO2 recovery and recirculation. Safeguards: The HAZOP identifies the pressure measurements PT401 and PT402 and records an added differential-pressure high alarm across the overhead separation system. Compressor spillback is also identified as an existing safeguard. Actions: Investigate the pressure difference between PT401 and PT402, reduce operation of the affected CO2 return system as necessary, and arrange inspection or maintenance of K401 before restoring normal flow.
- Source: 27794_Plant_HAZREP, Element 12, FLOW—NO, K401 demister blockage
- Key items found: K401, PT401, PT402, J103, C400
- Key items missing: none
- Evidence lines: 374

## Q59 [cause_and_effect] SUPPORTED (100%)

**What would be the process consequences if compressor J103 stopped circulating CO2?**

- Expected: Causes: J103 could become non-operational, or an upstream obstruction in K401 or C400 could starve the compressor of gas. Consequences: The normal CO2 return flow is lost and the recycled gas supply to the process becomes unavailable, affecting continuous operation and feed composition. Safeguards: The HAZOP identifies FT301 and FT302 as flow measurements and records an added pump shutdown trip and low-flow protection. Actions: Check the CO2 flow readings, investigate J103 and its upstream recovery path, and follow the applicable shutdown arrangements rather than continuing operation without the required gas return.
- Source: 27794_Plant_HAZREP, Element 6, FLOW—NO
- Key items found: J103, K401, C400, FT301, FT302
- Key items missing: none
- Evidence lines: 267

## Q60 [cause_and_effect] SUPPORTED (100%)

**If J102 fails during normal operation, what happens to gas circulation through E101?**

- Expected: Causes: Failure or non-operation of nitrogen return blower J102 stops or reduces the recirculated nitrogen flow. Consequences: The normal nitrogen gas flow through E101 is lost, so the intended gas-liquid contacting and absorption process cannot continue normally. Safeguards: FT303 and FT304 monitor the nitrogen return flow, and the HAZOP records the addition of a low-flow alarm. Actions: Check the nitrogen flow readings, investigate J102 and the K402 return route, notify the control room and follow the relevant plant operating or shutdown procedure.
- Source: 27794_Plant_HAZREP, Element 5, FLOW—NO
- Key items found: J102, E101, K402, FT303, FT304
- Key items missing: none
- Evidence lines: 400

## Q61 [cause_and_effect] SUPPORTED (100%)

**What could happen if PCV300 remained excessively closed while gas continued entering E101?**

- Expected: Causes: Failure of PCV300 to open when required, or a malfunction in the pressure regulation system, could restrict the controlled vent flow. Consequences: Pressure may rise in E101 and connected gas equipment. Safeguards: PT403 and PIC403 provide pressure feedback control, and RV400 provides a relief route connected to K403. The HAZOP also records a high-pressure protection action for the absorber. Actions: Inspect the PT403 reading and PIC403 response, check PCV300 operation and reduce the gas feed or initiate a controlled shutdown if pressure cannot be maintained safely.
- Source: PilotPlantReport_Group6_2.0.pdf, Appendix D.4.3.b; 27794_Plant_HAZREP, Element 10, PRESSURE—HIGHER; P&ID Differences.pdf, page 1
- Key items found: PCV300, PT403, PIC403, RV400, K403
- Key items missing: none
- Evidence lines: 400

## Q62 [cause_and_effect] SUPPORTED (80%)

**What are the consequences if PCV119 cannot respond to increasing stripper pressure?**

- Expected: Causes: A malfunction or obstruction of PCV119, or failure of its pressure control arrangement, can prevent the intended adjustment of CO2 recycle flow. Consequences: Pressure in E100 may continue increasing, creating an overpressure hazard. Safeguards: PT401 and PT402 provide pressure measurements for PIC401 and PIC402. The HAZOP records a pressure shutdown at 2 barg, while RV401 provides relief to K403. Actions: Check the pressure measurements and PCV119 response, reduce heat input to E100 and follow the shutdown procedure if pressure cannot be safely controlled.
- Source: 27794_Plant_HAZREP, Element 11 and MISC Notes M4; P&ID Differences.pdf, page 1; PilotPlantReport_Group6_2.0.pdf, Appendix D.4.3.a
- Key items found: PCV119, E100, PT401, RV401
- Key items missing: 2 barg
- Evidence lines: 400

## Q63 [cause_and_effect] SUPPORTED (80%)

**If the liquid level in E101 rises rapidly, how could the two MEA transfer pumps be responsible?**

- Expected: Causes: J100 may be delivering lean MEA to E101 faster than J101a or J101b removes rich MEA. An interrupted outlet route or failed rich MEA pump can have the same effect. Consequences: Liquid accumulates in the absorber base, potentially flooding the column and disrupting absorption. Safeguards: LT108 measures absorber level, LIC108 can adjust rich MEA pump speed, and the HAZOP identifies LZAH107 as plant shutdown protection. Actions: Compare the inflow and outflow measurements, increase the operating J101 pump flow or decrease J100 flow according to the documented alarm response, and stop operation if the high-high level condition develops.
- Source: 27794_Plant_HAZREP, Element 10, LEVEL—HIGHER; PilotPlantReport_Group6_2.0.pdf, Appendices D.4.2.a and F.8.4.6
- Key items found: E101, J101a, LT108, LZAH107
- Key items missing: J100
- Evidence lines: 400

## Q64 [cause_and_effect] SUPPORTED (80%)

**If the level in E100 rises while rich MEA is being transferred, what imbalance should be investigated?**

- Expected: Causes: Rich MEA may be entering E100 through J101a or J101b faster than lean MEA leaves through J100, or the lean MEA outlet route may be restricted. Consequences: Liquid accumulates in the stripper base and may lead to overfilling. Safeguards: LT101 monitors the stripper level, while LZAH100 is identified in the HAZOP as high-level shutdown protection. Actions: Check the relative transfer pump speeds and flow measurements, increase J100 or reduce the active J101 pump as directed by the high-level procedure, and initiate emergency shutdown if the high-high level limit is reached.
- Source: 27794_Plant_HAZREP, Element 11, LEVEL—HIGHER; PilotPlantReport_Group6_2.0.pdf, Appendix F.8.4.2
- Key items found: E100, J100, LT101, LZAH100
- Key items missing: J101a
- Evidence lines: 400

## Q65 [cause_and_effect] PARTIAL (40%)

**Why might LT101 fall rapidly when J100 speed increases, and what could happen to the pump?**

- Expected: Causes: Increasing J100 speed transfers lean MEA out of E100 more rapidly, which can cause LT101 to decrease if liquid replacement does not match removal. Consequences: Excessive reduction in the stripper base level can starve J100 and lead to cavitation or pump damage. Safeguards: The commissioning study identifies a low-level warning below 5% and a low-low shutdown below 1%. It also records a practical J100 operating range of 1%-57% when audible vibration is considered. Actions: Reduce J100 speed and observe LT101 until a safe steady level is restored; do not continue increasing pump speed while the level is falling towards the low-level limits.
- Source: PilotPlantReport_Group6_2.0.pdf, Sections 2.1-2.5 and Appendix E.3.7
- Key items found: LT101, J100
- Key items missing: 5%, 1%, 1%-57%
- Evidence lines: 400

## Q66 [cause_and_effect] SUPPORTED (100%)

**What could explain a high differential-pressure reading across Z102, and how does it affect lean MEA circulation?**

- Expected: Causes: Accumulation of material in Z102 can restrict the lean MEA circulation route. Consequences: The increased resistance reduces circulation and may cause J100 to operate under unsuitable conditions. Safeguards: Differential pressure is monitored by PDT105, called PTD105 in the commissioning SOP, which identifies 0.45 bar as the filter-blockage intervention threshold. Actions: During the commissioning procedure, reduce J100 towards 15%, open bypass valve V120, close V117a and V117b, and then gradually restore the previous operating flow. The full-operation SOP likewise documents this bypass route.
- Source: PilotPlantReport_Group6_2.0.pdf, Appendices E.3.6 and F.8.3.1; Appendix C.3.2; 27794_Plant_HAZREP, Element 7
- Key items found: Z102, PDT105, 0.45 bar, V120, V117a
- Key items missing: none
- Evidence lines: 400

## Q67 [cause_and_effect] SUPPORTED (100%)

**If J104 stops circulating water around K101, what happens to the gas feed preparation?**

- Expected: Causes: J104 failure, insufficient water in K101 or an obstruction in its circulation system can reduce or stop water recirculation. Consequences: The gas mixture entering the absorber may no longer be properly saturated. If the water level is too low, J104 can also be damaged. Safeguards: LT104 provides a K101 level measurement, and the HAZOP records low-level alarm protection and RV102 for excessive pump discharge pressure associated with a blocked nozzle. Actions: Check the K101 water level, inspect J104 and the circulation path, correct inadequate water inventory and avoid continuing pump operation when starved of liquid.
- Source: 27794_Plant_HAZREP, Elements 3 and 4
- Key items found: J104, K101, LT104, RV102
- Key items missing: none
- Evidence lines: 400

## Q68 [cause_and_effect] SUPPORTED (100%)

**What would happen if FCV105 became stuck open during CO2 feed operation?**

- Expected: Causes: FCV105 may become jammed open or fail to regulate the fresh CO2 flow correctly. Consequences: Excess CO2 may enter K101, changing the composition of the gas sent to E101 away from its required value. Safeguards: FT105 and FIC105 provide flow measurement and control information, and the HAZOP identifies gas composition analysis as a means of detecting incorrect mixture composition. Actions: Compare the measured CO2 feed with the required set point and gas analyser readings, investigate FCV105 and isolate or correct the feed if it cannot be controlled normally.
- Source: 27794_Plant_HAZREP, Element 1, FLOW—MORE; PilotPlantReport_Group6_2.0.pdf, Appendix D.4.1.c
- Key items found: FCV105, FT105, FIC105, K101, E101
- Key items missing: none
- Evidence lines: 122

## Q69 [safety_actions] SUPPORTED (80%)

**Pressure in E100 is approaching the high-pressure shutdown condition. What protects the stripper and what should the operator do?**

- Expected: Causes: Failure of pressure control through PCV119, excessive boiling in H100, or excessive heating can raise E100 pressure. Consequences: Overpressure threatens the stripper and the connected overhead system. Safeguards: The HAZOP records a PSH shutdown at 2 barg, intended to remove heat input before the relief set point is reached. RV401 provides the stripper relief connection to K403, and PT401 and PT402 provide pressure monitoring. Actions: Inform the control room, inspect the pressure control response, reduce or isolate excessive steam and heating, allow the protective trip to operate and follow the plant emergency shutdown procedure if pressure cannot be controlled. The documents do not specify a manual relief-valve operating action.
- Source: 27794_Plant_HAZREP, Element 11 and MISC Notes M4; P&ID Differences.pdf, page 1, K403
- Key items found: E100, PCV119, RV401, K403
- Key items missing: 2 barg
- Evidence lines: 400

## Q70 [safety_actions] SUPPORTED (100%)

**The pressure in E101 is rising above its normal controlled value. Which safeguards apply and what actions are required?**

- Expected: Causes: Excessive gas feed, restricted outlet or vent flow, or failure of PCV300 can increase pressure in E101. Consequences: The absorber and connected K101 gas system may become overpressurised. Safeguards: PT403 and PIC403 regulate the pressure through PCV300, while RV400 provides a relief route into K403. The HAZOP also records high-pressure shutdown protection. Actions: Check the indicated pressure and PCV300 response, identify whether excess gas input or an obstructed outlet is responsible, reduce feed or perform a controlled shutdown if the condition persists, and keep personnel away from any active relief discharge.
- Source: 27794_Plant_HAZREP, Element 10, PRESSURE—HIGHER; PilotPlantReport_Group6_2.0.pdf, Appendix D.4.3.b; P&ID Differences.pdf, page 1
- Key items found: E101, PT403, PCV300, RV400, K403
- Key items missing: none
- Evidence lines: 400

## Q71 [safety_actions] PARTIAL (60%)

**LT101 falls below 5% during full plant operation. What is the required response, and what happens if it falls below 1%?**

- Expected: Causes: J100 may be withdrawing lean MEA from E100 faster than liquid is replenished, or rich MEA return may be inadequate. Consequences: E100 becomes depleted and J100 risks liquid starvation or cavitation. Safeguards: LT101 has a low-level alarm below 5% and low-low protection below 1%. Actions: Reduce J100 power by 10%, increase the active J101a or J101b pump by 10% without exceeding its safe speed, increase J300 power by 10%, and check the MEA valve lineup. If LT101 continues falling below 1%, initiate emergency shutdown.
- Source: PilotPlantReport_Group6_2.0.pdf, Appendix F.8.4.1; Section 2.2
- Key items found: LT101, J100, J101a
- Key items missing: J300, 1%
- Evidence lines: 60

## Q72 [safety_actions] PARTIAL (60%)

**LT101 rises above 85% during normal operation. What adjustments are specified, and what is the high-high response?**

- Expected: Causes: Excessive rich MEA addition to E100 through J101a or J101b, or inadequate removal by J100, can raise the stripper liquid level. Consequences: E100 can become overfilled, interfering with normal stripping. Safeguards: LT101 has a high-level alarm above 85% and an extreme high-level shutdown condition above 95%. Actions: Increase J100 power by 10%, decrease the operating J101 pump power by 10%, and check the MEA valve configuration. If the level continues increasing above 95%, initiate emergency shutdown.
- Source: PilotPlantReport_Group6_2.0.pdf, Appendix F.8.4.2
- Key items found: LT101, J100, J101a
- Key items missing: 85%, 95%
- Evidence lines: 60

## Q73 [safety_actions] PARTIAL (60%)

**The level in E101 falls below 5% on LT108. What must the operator do?**

- Expected: Causes: The active rich MEA pump J101a or J101b may be transferring liquid out of E101 faster than J100 supplies lean MEA, or the inlet flow may be restricted. Consequences: The absorber base level falls and the rich MEA pump risks operating without sufficient liquid. Safeguards: LT108 supplies the low-level warning, with low-low shutdown protection if the level continues decreasing. Actions: Decrease the operating J101 pump power by 10%, increase J100 power by 10%, increase J300 power by 10%, and verify that the relevant MEA valves are correctly positioned. If the low-low alarm occurs, initiate emergency shutdown.
- Source: PilotPlantReport_Group6_2.0.pdf, Appendix F.8.4.5; 27794_Plant_HAZREP, Element 10
- Key items found: E101, LT108, J101a
- Key items missing: J100, J300
- Evidence lines: 400

## Q74 [safety_actions] PARTIAL (40%)

**LT108 indicates the absorber level is above 85%. Which immediate process adjustments are specified?**

- Expected: Causes: J100 may be supplying liquid faster than the active J101 pump removes it, or the rich MEA outlet may be restricted. Consequences: Liquid accumulates in the base of E101, creating an overfilling and flooding hazard. Safeguards: LT108 provides the level warning, and the HAZOP identifies LZAH107 as high-level plant shutdown protection. Actions: Increase the operating J101a or J101b pump power by 10%, decrease J100 power by 10%, decrease J300 power by 10%, and check the MEA valve lineup. If the high-high alarm occurs, initiate emergency shutdown.
- Source: PilotPlantReport_Group6_2.0.pdf, Appendix F.8.4.6; 27794_Plant_HAZREP, Element 10
- Key items found: LT108, J101a
- Key items missing: 85%, J100, J300
- Evidence lines: 400

## Q75 [safety_actions] PARTIAL (75%)

**LT401 shows the liquid level in C400 has fallen below 5%. What is the correct response?**

- Expected: Causes: Condensate may be leaving C400 through J300 faster than liquid is being produced or collected. Consequences: The condensate collection system may become depleted, risking unsuitable operation of J300 and interruption of reflux return. Safeguards: LT401 provides a low-level alarm and a low-low shutdown condition. Actions: Decrease J300 power by 10% to reduce condensate removal. Continue monitoring LT401 and, if the level continues decreasing until the low-low alarm occurs, initiate emergency shutdown.
- Source: PilotPlantReport_Group6_2.0.pdf, Appendix F.8.4.7; Appendix D.4.2.b
- Key items found: LT401, C400, J300
- Key items missing: 5%
- Evidence lines: 400

## Q76 [safety_actions] PARTIAL (75%)

**The liquid level in C400 rises above 85%. What should be done before the high-high condition is reached?**

- Expected: Causes: Condensate accumulation can exceed removal if J300 is operating too slowly or the return flow is restricted. Consequences: C400 can become overfilled and the overhead liquid separation and recovery process can be disrupted. Safeguards: LT401 indicates the condensate level, with a high alarm above 85% and high-high shutdown protection. Actions: Increase J300 power by 10%, observe the resulting LT401 trend and investigate the condensate return route. If the high-high alarm occurs, initiate emergency shutdown.
- Source: PilotPlantReport_Group6_2.0.pdf, Appendix F.8.4.8
- Key items found: C400, LT401, J300
- Key items missing: 85%
- Evidence lines: 400

## Q77 [safety_actions] SUPPORTED (100%)

**A gas leak is suspected in the nitrogen return pipe between K402 and J102. What precautions and emergency actions are required?**

- Expected: Causes: A leaking connection, damaged line or faulty valve in the gas return route between K402 and J102 could release gas into the plant area. Consequences: The plant loses gas inventory, normal nitrogen circulation may be disrupted, and released nitrogen can create an oxygen-deficient atmosphere. Safeguards: The HAZOP records oxygen depletion sensors for the plant area, and the SOP provides an emergency shutdown procedure for gas leaks. Actions: Notify the plant supervisor, evacuate the plant and press the emergency shutdown button. Do not attempt to repair the leak while gas remains present; wait for the area to be declared safe and for any released gas to dissipate before maintenance.
- Source: PilotPlantReport_Group6_2.0.pdf, Appendix F.8.1; 27794_Plant_HAZREP, Element 5 and MISC Notes M1
- Key items found: K402, J102, E101
- Key items missing: none
- Evidence lines: 400

## Q78 [safety_actions] SUPPORTED (100%)

**Temperature and pressure around H100 rise sharply and a blockage is suspected. What is the documented bypass procedure?**

- Expected: Causes: A blockage or restriction in the reboiler or associated steam route can produce abnormal temperature and pressure conditions. Consequences: Heat-transfer operation becomes unsafe and the affected system may be subjected to excessive pressure. Safeguards: The plant has steam flow and temperature monitoring, pressure protection and a documented H100 bypass arrangement. Actions: Follow the reboiler bypass procedure by opening V106 and closing V101, V109, V105 and V102, together with FCV110. The isolated reboiler can then be examined by the external maintenance crew. The procedure must be coordinated with the control room and plant supervisor.
- Source: PilotPlantReport_Group6_2.0.pdf, Appendix F.8.3.3, Figure F.23
- Key items found: H100, V106, V101, V102, FCV110
- Key items missing: none
- Evidence lines: 400

## Q79 [safety_actions] SUPPORTED (100%)

**A significant nitrogen or carbon dioxide release occurs near the gas mixing system K101. What safeguards and operator actions apply?**

- Expected: Causes: Leakage from the nitrogen or CO2 feed connections, or a failure in the gas return circuits involving J102 or J103, could release gas near K101. Consequences: Gas inventory is lost, the feed mixture becomes difficult to maintain and the surrounding atmosphere may become oxygen-deficient. Safeguards: The HAZOP records the installation of oxygen depletion sensors, and the SOP identifies emergency shutdown and evacuation as the appropriate response to gas leakage. Actions: Inform the supervisor, evacuate personnel immediately, activate emergency shutdown, and prevent entry until the area is safe. Investigation and repair should take place only after gas has dissipated and the area has been made safe.
- Source: 27794_Plant_HAZREP, MISC Notes M1 and Elements 1-3; PilotPlantReport_Group6_2.0.pdf, Appendix F.8.1
- Key items found: K101, J102, J103
- Key items missing: none
- Evidence lines: 400

## Q80 [safety_actions] SUPPORTED (100%)

**During MEA filling, the storage or supply vessel B100 becomes empty while J105 is running. What hazards and protective actions are identified?**

- Expected: Causes: B100 may be empty, incorrectly connected or isolated while filling pump J105 continues operating. Consequences: The pump may run dry, interrupting MEA transfer and risking pump damage. A closed downstream filling valve may also cause excessive pump discharge pressure. Safeguards: The HAZOP recommends and records completed low-level trip protection on B100, a liquid-detection action to stop the pump in the absence of liquid, and a relief spillback route around J105. The HAZOP also records high-level trip protection when B100 is being used as a receiver. Actions: Stop J105 when adequate liquid supply is unavailable, verify the B100 inventory and connections, check the appropriate filling valve lineup, and only resume filling once the cause has been corrected and the pump can be operated safely.
- Source: 27794_Plant_HAZREP, Element 9a, FLOW—NO; MISC Notes M16 and M17
- Key items found: B100, J105
- Key items missing: none
- Evidence lines: 396
