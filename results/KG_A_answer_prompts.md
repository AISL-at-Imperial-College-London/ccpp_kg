## Q01

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
J100 --floor--> 1
J100 --gridReference--> M10
J100 --note--> Speed set by SIC100. HAZOP 7.11 refers to diaphragm changes.
J100 --feedsInto--> PCV122
J100 --type--> Pump
J100 --label--> J100 lean MEA pump
J100 --pipedTo--> PCV122
J100 --pipedTo--> RV101
J100 --tag--> J100
FI103 --monitors--> J100
PROC_Z102_bypass_step_01 --operatesOn--> J100
V113b --feedsInto--> J100
PROC_stripping_loop_lineup_step_28 --operatesOn--> J100
CL_J100_flow --hasFinalElement--> J100
FI104 --monitors--> J100
IL_E100_level_LL --tripsItem--> J100
HAZOP_7_14 --concerns--> J100
TT106 --monitors--> J100
V113b --pipedTo--> J100
HAZOP_7_01 --concerns--> J100
HAZOP_11_12 --concerns--> J100
HS100 --controls--> J100
FT103 --monitors--> J100
HAZOP_element_7 --covers--> J100
limit_J100_power_range --appliesTo--> J100
FIC104 --controls--> J100
HAZOP_11_13 --concerns--> J100
FT104 --monitors--> J100
limit_J100_cavitation --appliesTo--> J100
HAZOP_7_11 --concerns--> J100
PROC_Z102_bypass_step_05 --operatesOn--> J100
PT104 --monitors--> J100
limit_J100_flow_range --appliesTo--> J100
OI11 --about--> J100
PROC_stripping_loop_lineup_step_01 --operatesOn--> J100
RV101 --protects--> J100
FIC103 --controls--> J100
IL_E100_level_HH --tripsItem--> J100
SIC100 --controls--> J100
limit_TZAH106 --appliesTo--> J100
HAZOP_7_15 --concerns--> J100
HAZOP_7_02 --concerns--> J100
StrippingLoop_step_20_J100 --stepIndex--> 20
StrippingLoop_step_20_J100 --stepType--> inline
StrippingLoop_step_20_J100 --label--> Stripping loop step 20: J100
StrippingLoop_step_20_J100 --stepItem--> J100
StrippingLoop_step_20_J100 --type--> LoopStep
PROC_pump_start_order_step_01 --operatesOn--> LT108
PROC_pump_start_order_step_01 --stepOrder--> 1
PROC_pump_start_order_step_01 --type--> ProcedureStep
PROC_pump_start_order_step_01 --instruction--> Compare LT101 (E100) and LT108 (E101)
PROC_pump_start_order_step_01 --label--> Order of starting J100 and J101a/b step 1
PROC_pump_start_order --hasProcedureStep--> PROC_pump_start_order_step_01
HAZOP_7_14 --concerns--> RV101
HAZOP_7_14 --parameter--> PRESSURE
HAZOP_7_14 --label--> HAZOP 7.14
HAZOP_7_14 --guideword--> HIGHER
HAZOP_7_14 --type--> HazopDeviation
HAZOP_7_14 --cause--> Isolation d/s of J100
HAZOP_7_14 --safeguard--> RV101
HAZOP_7_14 --itemNumber--> 14
HAZOP_7_14 --inElement--> HAZOP_element_7
PROC_Z102_bypass_step_05 --type--> ProcedureStep
PROC_Z102_bypass_step_05 --label--> Z102 filter bypass step 5
PROC_Z102_bypass_step_05 --instruction--> Return J100 to the previous steady-state power
PROC_Z102_bypass_step_05 --stepOrder--> 5
PROC_Z102_bypass --hasProcedureStep--> PROC_Z102_bypass_step_05
Route_B_top_bypass_step_20_J100 --label--> Route B: top return (stage 1), Z102 bypassed step 20: J100
Route_B_top_bypass_step_20_J100 --stepType--> inline
Route_B_top_bypass_step_20_J100 --stepIndex--> 20
Route_B_top_bypass_step_20_J100 --type--> LoopStep
Route_B_top_bypass_step_20_J100 --nextStep--> Route_B_top_bypass_step_24_PCV122
Route_B_top_bypass_step_20_J100 --stepItem--> J100
Route_B_top_bypass_step_19_V113b --nextStep--> Route_B_top_bypass_step_20_J100
SIC100 --tag--> SIC100
SIC100 --type--> Controller
SIC100 --label--> J100 speed controller
CL_J100_flow --hasController--> SIC100
TT106 --gridReference--> L10
TT106 --sensorType--> PRT
TT106 --signalType--> 4-20mA
TT106 --floor--> 1
TT106 --type--> TemperatureInstrument
TT106 --label--> TT106
TT106 --measuredVariable--> temperature
TT106 --tag--> TT106
J100__cit02 --citationText--> Pilot Plant Report section 2.5 (pump trials)
J100__cit02 --document--> SRC_REPORT
J100__cit02 --location--> section 2.5 (pump trials)
J100__cit02 --label--> Citation 2 for J100
J100__cit02 --type--> Citation
limit_J100_flow_range --label--> J100_flow_range
limit_J100_flow_range --limitType--> range
limit_J100_flow_range --unit--> L/min
limit_J100_flow_range --lowValue--> 10.79
limit_J100_flow_range --note--> P&ID design range. In the commissioning test J100 delivered 272 to 1051 kg/h (about 4.5 to 17.5 L/min), so it ran below this range at low pump power.
limit_J100_flow_range --variable--> volumetric flow
limit_J100_flow_range --source--> P&ID; TEAM confirmed on full-size P&ID; REPORT Fig E.4
limit_J100_flow_range --type--> OperatingLimit
limit_J100_flow_range --valueVerified--> true
limit_J100_flow_range --highValue--> 19.7
limit_LZAL102 --label--> LZAL102
limit_LZAL102 --unit--> %
limit_LZAL102 --type--> OperatingLimit
limit_LZAL102 --valueVerified--> true
limit_LZAL102 --limitType--> trip
limit_LZAL102 --variable--> level
limit_LZAL102 --lowValue--> 1.0
limit_LZAL102 --note--> LSLL: emergency shutdown; protects J100 from starvation.
limit_LZAL102 --source--> REPORT 2.2; HAZOP 7.15, 11.15
limit_LZAL102 --appliesTo--> E100
HAZOP_7_01 --inElement--> HAZOP_element_7
HAZOP_7_01 --guideword--> NO
HAZOP_7_01 --consequence--> Overheat pump
HAZOP_7_01 --label--> HAZOP 7.1
HAZOP_7_01 --parameter--> FLOW
HAZOP_7_01 --safeguard--> TZAH104 (now TZAH106)
HAZOP_7_01 --itemNumber--> 1
HAZOP_7_01 --type--> HazopDeviation
HAZOP_7_01 --cause--> Isolation valve closed anywhere along line
OI11 --label--> OI11: Cause and effect (e.g. what happens to the E100 level if J100 trips) is not modelled
OI11 --itemStatus--> open
OI11 --foundBy--> S10
OI11 --about--> E100
OI11 --description--> Cause and effect (e.g. what happens to the E100 level if J100 trips) is not modelled
OI11 --resolvedBy--> Cause and effect chart, or a dynamic model
OI11 --type--> OpenItem
FI104 --label--> FI104
FI104 --measuredVariable--> flow indication
FI104 --tag--> FI104
FI104 --floor--> 1
FI104 --type--> FlowInstrument
PROC_Z102_bypass_step_01 --type--> ProcedureStep
PROC_Z102_bypass_step_01 --stepOrder--> 1
PROC_Z102_bypass_step_01 --label--> Z102 filter bypass step 1
PROC_Z102_bypass_step_01 --instruction--> Reduce J100 power by 20 % per minute until it reaches 15 %
PROC_Z102_bypass --hasProcedureStep--> PROC_Z102_bypass_step_01
SDV125 --floor--> 1
SDV125 --pipedTo--> H200a
SDV125 --gridReference--> L11
SDV125 --type--> ShutdownValve
SDV125 --feedsInto--> H200b
SDV125 --label--> SDV125
SDV125 --valveType--> shutdown (solenoid-operated)
SDV125 --pipedTo--> H200b
SDV125 --tag--> SDV125
SDV125 --note--> Route from J100 discharge to H200a/b and E100 (stripping loop). Tagged SDV125 on the P&ID; the REPORT calls it SOV125.
SDV125 --normalPosition--> open
SDV125 --feedsInto--> H200a
FT104 --feedsInto--> SDV125
```

Question: What is the grid reference of pump J100?

## Q02

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
J101b --floor--> 1
J101b --pipedTo--> PCV120b
J101b --type--> Pump
J101b --gridReference--> N16
J101b --label--> J101b rich MEA pump (duty or standby)
J101b --tag--> J101b
J101b --note--> Parallel to J101a; only one runs at a time.
J101b --feedsInto--> PCV120b
ROI03 --about--> J101b
LIC108 --controls--> J101b
CL_E101_level --hasFinalElement--> J101b
IL_E101_level_LL --tripsItem--> J101b
AOI04 --about--> J101b
PROC_J101b_startup_step_07 --operatesOn--> J101b
TT111b --monitors--> J101b
PT115b --monitors--> J101b
HAZOP_element_8 --covers--> J101b
V135b --feedsInto--> J101b
IL_E101_level_HH --tripsItem--> J101b
TT110b --monitors--> J101b
V135b --pipedTo--> J101b
AOI09 --about--> J101b
PROC_J101a_startup_step_01 --operatesOn--> J101b
PROC_J101b_startup_step_02 --operatesOn--> J101b
SIC101b --controls--> J101b
AOI02 --about--> J101b
IL_E101_level_HH --initiatedBy--> LSHH107
IL_E101_level_HH --tripsItem--> J101a
IL_E101_level_HH --label--> E101 high-high level plant shutdown (LZAH107)
IL_E101_level_HH --type--> Interlock
PROC_J101b_startup --hasProcedureStep--> PROC_J101b_startup_step_03
PROC_J101b_startup --hasProcedureStep--> PROC_J101b_startup_step_07
PROC_J101b_startup --hasProcedureStep--> PROC_J101b_startup_step_06
PROC_J101b_startup --label--> J101b start-up valve line-up
PROC_J101b_startup --hasProcedureStep--> PROC_J101b_startup_step_01
PROC_J101b_startup --type--> Procedure
PROC_J101b_startup --hasProcedureStep--> PROC_J101b_startup_step_05
PROC_J101b_startup --hasProcedureStep--> PROC_J101b_startup_step_02
PROC_J101b_startup --triggerCondition--> J101b selected as the running pump
PROC_J101b_startup --hasProcedureStep--> PROC_J101b_startup_step_04
IL_E101_level_LL --label--> E101 low-low level plant shutdown (LZAL109)
IL_E101_level_LL --initiatedBy--> LSLL109
IL_E101_level_LL --tripsItem--> J101a
IL_E101_level_LL --type--> Interlock
AbsRoute_J101b_step_19_V211 --stepIndex--> 19
AbsRoute_J101b_step_19_V211 --stepItem--> V211
AbsRoute_J101b_step_19_V211 --type--> LoopStep
AbsRoute_J101b_step_19_V211 --stepType--> inline
AbsRoute_J101b_step_19_V211 --label--> Absorber recirculation on J101b step 19: V211
AbsRoute_J101b_setting_V134b --label--> V134b in Absorber recirculation on J101b
AbsRoute_J101b_setting_V134b --type--> ValveSetting
AbsRoute_J101b_setting_V134b --requiredPosition--> open
AbsRoute_J101b_setting_V134b --valve--> V134b
AbsRoute_J101b --hasValveSetting--> AbsRoute_J101b_setting_V134b
AbsRoute_J101b_step_23_TT208 --label--> Absorber recirculation on J101b step 23: TT208
AbsRoute_J101b_step_23_TT208 --stepItem--> TT208
AbsRoute_J101b_step_23_TT208 --stepType--> tie-in
AbsRoute_J101b_step_23_TT208 --stepIndex--> 23
AbsRoute_J101b_step_23_TT208 --type--> LoopStep
AbsRoute_J101b_step_32_E101 --type--> LoopStep
AbsRoute_J101b_step_32_E101 --stepType--> inline
AbsRoute_J101b_step_32_E101 --label--> Absorber recirculation on J101b step 32: E101
AbsRoute_J101b_step_32_E101 --stepIndex--> 32
AbsRoute_J101b_step_32_E101 --stepItem--> E101
AbsRoute_J101b_setting_V144a --valve--> V144a
AbsRoute_J101b_setting_V144a --type--> ValveSetting
AbsRoute_J101b_setting_V144a --label--> V144a in Absorber recirculation on J101b
AbsRoute_J101b_setting_V144a --requiredPosition--> closed
AbsRoute_J101b --hasValveSetting--> AbsRoute_J101b_setting_V144a
PROC_J101b_startup_step_03 --type--> ProcedureStep
PROC_J101b_startup_step_03 --requiredPosition--> open
PROC_J101b_startup_step_03 --label--> J101b start-up valve line-up step 3
PROC_J101b_startup_step_03 --operatesOn--> V134b
PROC_J101b_startup_step_03 --stepOrder--> 3
PROC_J101b_startup_step_03 --instruction--> Open V134b
AbsRoute_J101b_setting_V198b --valve--> V198b
AbsRoute_J101b_setting_V198b --type--> ValveSetting
AbsRoute_J101b_setting_V198b --requiredPosition--> closed
AbsRoute_J101b_setting_V198b --label--> V198b in Absorber recirculation on J101b
AbsRoute_J101b --hasValveSetting--> AbsRoute_J101b_setting_V198b
AbsRoute_J101b_step_25_TT210 --stepIndex--> 25
AbsRoute_J101b_step_25_TT210 --label--> Absorber recirculation on J101b step 25: TT210
AbsRoute_J101b_step_25_TT210 --stepType--> tie-in
AbsRoute_J101b_step_25_TT210 --type--> LoopStep
AbsRoute_J101b_step_25_TT210 --stepItem--> TT210
AbsRoute_J101b_step_24_C200 --stepItem--> C200
AbsRoute_J101b_step_24_C200 --label--> Absorber recirculation on J101b step 24: C200
AbsRoute_J101b_step_24_C200 --type--> LoopStep
AbsRoute_J101b_step_24_C200 --stepType--> inline
AbsRoute_J101b_step_24_C200 --stepIndex--> 24
AbsRoute_J101b_setting_SDV123 --type--> ValveSetting
AbsRoute_J101b_setting_SDV123 --requiredPosition--> closed
AbsRoute_J101b_setting_SDV123 --valve--> SDV123
AbsRoute_J101b_setting_SDV123 --label--> SDV123 in Absorber recirculation on J101b
AbsRoute_J101b --hasValveSetting--> AbsRoute_J101b_setting_SDV123
LIC108 --tag--> LIC108
LIC108 --label--> E101 level controller (PV LT108)
LIC108 --type--> Controller
LIC108 --controls--> J101a
CL_E101_level --hasController--> LIC108
AbsRoute_J101b_setting_V143a --label--> V143a in Absorber recirculation on J101b
AbsRoute_J101b_setting_V143a --type--> ValveSetting
AbsRoute_J101b_setting_V143a --requiredPosition--> closed
AbsRoute_J101b_setting_V143a --valve--> V143a
AbsRoute_J101b --hasValveSetting--> AbsRoute_J101b_setting_V143a
AbsRoute_J101b_setting_V135a --requiredPosition--> closed
AbsRoute_J101b_setting_V135a --label--> V135a in Absorber recirculation on J101b
AbsRoute_J101b_setting_V135a --valve--> V135a
AbsRoute_J101b_setting_V135a --type--> ValveSetting
AbsRoute_J101b --hasValveSetting--> AbsRoute_J101b_setting_V135a
AbsRoute_J101b_step_06_B103b --stepType--> tie-in
AbsRoute_J101b_step_06_B103b --type--> LoopStep
AbsRoute_J101b_step_06_B103b --stepItem--> B103b
AbsRoute_J101b_step_06_B103b --stepIndex--> 6
AbsRoute_J101b_step_06_B103b --label--> Absorber recirculation on J101b step 6: B103b
V139b --floor--> 1
V139b --valveType--> ball
V139b --gridReference--> N16
V139b --tag--> V139b
V139b --type--> ManualValve
V139b --label--> V139b
V139b --normalPosition--> closed
V139b --note--> J101b pump area. FI02
AbsRoute_J101b_step_02_V135b --stepType--> inline
AbsRoute_J101b_step_02_V135b --stepItem--> V135b
AbsRoute_J101b_step_02_V135b --type--> LoopStep
AbsRoute_J101b_step_02_V135b --stepIndex--> 2
AbsRoute_J101b_step_02_V135b --label--> Absorber recirculation on J101b step 2: V135b
AOI02 --resolvedBy--> Plant supervisor or handover document (REPORT F.5.4.5)
AOI02 --about--> J101a
AOI02 --itemStatus--> open
AOI02 --type--> OpenItem
AOI02 --foundBy--> absorption loop build, Oct 2026
AOI02 --label--> AOI02: Which of J101a and J101b is the normal duty pump
AOI02 --description--> Which of J101a and J101b is the normal duty pump
AbsRoute_J101b_step_07_PT115b --stepItem--> PT115b
AbsRoute_J101b_step_07_PT115b --stepIndex--> 7
AbsRoute_J101b_step_07_PT115b --stepType--> tie-in
AbsRoute_J101b_step_07_PT115b --label--> Absorber recirculation on J101b step 7: PT115b
AbsRoute_J101b_step_07_PT115b --type--> LoopStep
TT110b --sensorType--> PRT
TT110b --floor--> 1
TT110b --gridReference--> N16
TT110b --tag--> TT110b
TT110b --label--> TT110b
TT110b --type--> TemperatureInstrument
TT110b --measuredVariable--> J101b temperature
TT110b --signalType--> Fieldbus
ROI03 --foundBy--> rich section build, Oct 2026
ROI03 --resolvedBy--> Plant supervisor
```

Question: Where is pump J101b located?

## Q03

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
H200a --label--> H200a electric heater
H200a --type--> ElectricHeater
H200a --feedsInto--> V403
H200a --tag--> H200a
H200a --pipedTo--> V403
H200a --floor--> 2
H200a --pipedTo--> V309
H200a --gridReference--> J10
SDV125 --pipedTo--> H200a
IL_H200a_HH --tripsItem--> H200a
SDV152 --pipedTo--> H200a
TY213a --controls--> H200a
TT212a --monitors--> H200a
OI09 --about--> H200a
limit_TSHH212a --appliesTo--> H200a
aspen_v6_1_H200a_performance --ofEquipment--> H200a
TZH213 --controls--> H200a
CL_H200a_temperature --hasFinalElement--> H200a
PROC_heater_overtemperature_step_02 --operatesOn--> H200a
TZAHH212a --controls--> H200a
OI13 --about--> H200a
PROC_heater_overtemperature_step_06 --operatesOn--> H200a
aspen_v3_H200a_performance --ofEquipment--> H200a
TIC213a --controls--> H200a
HS200a --controls--> H200a
aspen_v3_block_H200A --represents--> H200a
aspen_v6_1_block_H200A --represents--> H200a
OI01 --about--> H200a
OI06 --about--> H200a
TSHH212a --monitors--> H200a
IL_heater_outlet_H --tripsItem--> H200a
SDV125 --feedsInto--> H200a
TY213a --type--> Controller
TY213a --label--> Power converter driving H200a
TY213a --tag--> TY213a
CL_H200a_temperature --hasController--> TY213a
PROC_heater_overtemperature_step_06 --type--> ProcedureStep
PROC_heater_overtemperature_step_06 --instruction--> If both TT213 and TI213 read above 25 C, send a mechanical engineer to check H200a and H200b
PROC_heater_overtemperature_step_06 --stepOrder--> 6
PROC_heater_overtemperature_step_06 --label--> MEA entering E100 too hot (heater over-temperature) step 6
PROC_heater_overtemperature --hasProcedureStep--> PROC_heater_overtemperature_step_06
OI01 --resolvedBy--> Heater datasheet and electrical single-line diagram
OI01 --about--> H200b
OI01 --type--> OpenItem
OI01 --foundBy--> S01, S02
OI01 --itemStatus--> open
OI01 --description--> Power rating and electrical supply (breaker, contactor, panel) of H200a and H200b
OI01 --label--> OI01: Power rating and electrical supply (breaker, contactor, panel) of H200a and H200b
TT212a --sensorType--> K-type thermocouple
TT212a --signalType--> 4-20mA
TT212a --type--> TemperatureInstrument
TT212a --measuredVariable--> heater temperature
TT212a --gridReference--> J9
TT212a --floor--> 2
TT212a --label--> TT212a
TT212a --tag--> TT212a
IL_H200a_HH --initiatedBy--> TT212a
TT213 --sensorType--> PRT
TT213 --type--> TemperatureInstrument
TT213 --measuredVariable--> temperature of MEA leaving H200a/b
TT213 --label--> TT213
TT213 --gridReference--> H13
TT213 --signalType--> Profibus-PA
TT213 --tag--> TT213
TT213 --floor--> 2
PROC_stripping_loop_lineup_step_27 --operatesOn--> TT213
IL_heater_outlet_H --initiatedBy--> TT213
PROC_heater_overtemperature_step_01 --operatesOn--> TT213
limit_TT213_setpoint_commissioning --appliesTo--> TT213
PROC_heater_overtemperature_step_05 --operatesOn--> TT213
CL_H200a_temperature --hasSensor--> TT213
CL_H200b_temperature --hasSensor--> TT213
IL_H200a_HH --label--> H200a high-high temperature trip
IL_H200a_HH --type--> Interlock
IL_H200a_HH --initiatedBy--> TSHH212a
OI06 --description--> No Aspen case for the stripping loop test or the side return; loop-mode duties and loadings are unknown
OI06 --label--> OI06: No Aspen case for the stripping loop test or the side return; loop-mode duties and loadings are unknown
OI06 --about--> E100
OI06 --about--> H200b
OI06 --type--> OpenItem
OI06 --foundBy--> R20, A11
OI06 --resolvedBy--> A converged Aspen case for the loop line-up, or plant data from a loop run
OI06 --itemStatus--> open
PROC_heater_overtemperature_step_02 --label--> MEA entering E100 too hot (heater over-temperature) step 2
PROC_heater_overtemperature_step_02 --instruction--> If the set point is 25 C and the MEA temperature is still rising, manually shut off H200a
PROC_heater_overtemperature_step_02 --stepOrder--> 2
PROC_heater_overtemperature_step_02 --type--> ProcedureStep
PROC_heater_overtemperature --hasProcedureStep--> PROC_heater_overtemperature_step_02
StripperRecirculation --label--> Stripping loop only, absorber isolated, lean returned via SDV125 and H200a/b
StripperRecirculation --type--> OperatingMode
StrippingLoop --inMode--> StripperRecirculation
Route_B_top_bypass --inMode--> StripperRecirculation
Route_C_side_filter --inMode--> StripperRecirculation
Route_A_top_filter --inMode--> StripperRecirculation
Route_D_side_bypass --inMode--> StripperRecirculation
HS200a --tag--> HS200a
HS200a --label--> H200a hand switch
HS200a --type--> Controller
aspen_v3_block_H200A --status--> OK
aspen_v3_block_H200A --inCase--> case_aspen_v3
aspen_v3_block_H200A --blockId--> H200A
aspen_v3_block_H200A --aspenModel--> HEATER
aspen_v3_block_H200A --type--> AspenBlock
aspen_v3_block_H200A --label--> H200A (ABB_pilot_plant_final_3)
aspen_v3_stream_S5 --toBlock--> aspen_v3_block_H200A
aspen_v3_stream_S7 --fromBlock--> aspen_v3_block_H200A
Route_B_top_bypass_step_33_H200a --nextStep--> Route_B_top_bypass_step_36_V403
Route_B_top_bypass_step_33_H200a --label--> Route B: top return (stage 1), Z102 bypassed step 33: H200a
Route_B_top_bypass_step_33_H200a --stepItem--> H200a
Route_B_top_bypass_step_33_H200a --stepType--> inline
Route_B_top_bypass_step_33_H200a --type--> LoopStep
Route_B_top_bypass_step_33_H200a --stepIndex--> 33
Route_B_top_bypass_step_32_SDV125 --nextStep--> Route_B_top_bypass_step_33_H200a
SDV125 --floor--> 1
SDV125 --gridReference--> L11
SDV125 --type--> ShutdownValve
SDV125 --feedsInto--> H200b
SDV125 --label--> SDV125
SDV125 --valveType--> shutdown (solenoid-operated)
SDV125 --pipedTo--> H200b
SDV125 --tag--> SDV125
SDV125 --note--> Route from J100 discharge to H200a/b and E100 (stripping loop). Tagged SDV125 on the P&ID; the REPORT calls it SOV125.
SDV125 --normalPosition--> open
FT104 --feedsInto--> SDV125
FT104 --pipedTo--> SDV125
Route_C_side_filter_setting_SDV125 --valve--> SDV125
FigureOfEight_setting_SDV125 --valve--> SDV125
Route_A_top_filter_setting_SDV125 --valve--> SDV125
Route_D_side_bypass_setting_SDV125 --valve--> SDV125
PROC_figure_of_eight_lineup_step_03 --operatesOn--> SDV125
Route_B_top_bypass_setting_SDV125 --valve--> SDV125
OI09 --about--> SDV125
PROC_stripping_loop_lineup_step_22 --operatesOn--> SDV125
CL_H200a_temperature --type--> ControlLoop
CL_H200a_temperature --controlledVariable--> Temperature of MEA entering E100
CL_H200a_temperature --manipulatedVariable--> Thermal duty of H200a
CL_H200a_temperature --hasController--> TIC213a
CL_H200a_temperature --source--> SUMMARY p.190; REPORT D.4.4.a
CL_H200a_temperature --label--> Temperature of MEA entering E100, heater leg A
TIC213a --label--> Heater outlet temperature controller, leg A
TIC213a --tag--> TIC213a
TIC213a --type--> Controller
limit_TIC213a_setpoint_commissioning --appliesTo--> TIC213a
OI02 --about--> TIC213a
Route_A_top_filter_step_36_H200a --stepItem--> H200a
Route_A_top_filter_step_36_H200a --nextStep--> Route_A_top_filter_step_39_V403
Route_A_top_filter_step_36_H200a --stepIndex--> 36
Route_A_top_filter_step_36_H200a --type--> LoopStep
Route_A_top_filter_step_36_H200a --stepType--> inline
Route_A_top_filter_step_36_H200a --label--> Route A: top return (stage 1), through Z102 step 36: H200a
```

Question: On which floor and at which grid reference is heater H200a located?

## Q04

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
FCV110 --feedsInto--> H100_N_steam_in
FCV110 --pipedTo--> H100_N_steam_in
FCV110 --type--> FlowControlValve
FCV110 --normalPosition--> closed
FCV110 --note--> Steam control valve for H100, named ZS110 on site (DIFF). Closed in the stripping loop test: no steam (REPORT Fig E.1, F.5.4.3).
FCV110 --label--> FCV110
FCV110 --floor--> 1
FCV110 --gridReference--> L5
FCV110 --tag--> FCV110
FCV110 --valveType--> flow control
FT101 --pipedTo--> FCV110
FT101 --feedsInto--> FCV110
FIC100 --controls--> FCV110
CL_H100_temperature_master --hasFinalElement--> FCV110
HAZOP_element_13 --covers--> FCV110
discrepancy_FCV110_name --concerns--> FCV110
PROC_reboiler_heating_step_02 --operatesOn--> FCV110
TIC100 --controls--> FCV110
HAZOP_13_04 --concerns--> FCV110
PROC_stripping_loop_lineup_step_06 --operatesOn--> FCV110
PROC_H100_steam_bypass_step_06 --operatesOn--> FCV110
CL_H100_steam_slave --hasFinalElement--> FCV110
HAZOP_element_13 --covers--> V104
HAZOP_element_13 --covers--> TT118
HAZOP_element_13 --covers--> TT117
HAZOP_element_13 --label--> HAZOP element 13: STEAM / CONDENSATE SYSTEM to H1 (H100)
HAZOP_element_13 --covers--> V103
HAZOP_element_13 --covers--> V100
HAZOP_element_13 --covers--> H100
HAZOP_element_13 --covers--> PT101
HAZOP_element_13 --covers--> K100
HAZOP_element_13 --type--> HazopElement
HAZOP_element_13 --covers--> XV140
HAZOP_element_13 --covers--> V101
HAZOP_element_13 --source--> 27794_Plant_HAZREP, HAZOP study 6-7 May 2010, drawing 55_200_1001 issue 1. Elements 7, 8, 11 and 13 (those touching the stripping loop).
HAZOP_element_13 --covers--> V105
HAZOP_element_13 --elementNumber--> 13
HAZOP_element_13 --covers--> V102
HAZOP_element_13 --covers--> V106
HAZOP_element_13 --covers--> RV107
HAZOP_element_13 --covers--> NRV110
HAZOP_element_13 --covers--> V109
HAZOP_13_03 --inElement--> HAZOP_element_13
HAZOP_13_11 --inElement--> HAZOP_element_13
HAZOP_13_14 --inElement--> HAZOP_element_13
HAZOP_13_06 --inElement--> HAZOP_element_13
HAZOP_13_08 --inElement--> HAZOP_element_13
HAZOP_13_13 --inElement--> HAZOP_element_13
HAZOP_13_05 --inElement--> HAZOP_element_13
HAZOP_13_04 --inElement--> HAZOP_element_13
HAZOP_13_09 --inElement--> HAZOP_element_13
HAZOP_13_10 --inElement--> HAZOP_element_13
HAZOP_13_12 --inElement--> HAZOP_element_13
HAZOP_13_02 --inElement--> HAZOP_element_13
HAZOP_13_01 --inElement--> HAZOP_element_13
HAZOP_13_07 --inElement--> HAZOP_element_13
FIC100 --label--> Steam flow controller (cascade slave)
FIC100 --type--> Controller
FIC100 --tag--> FIC100
CL_H100_steam_slave --hasController--> FIC100
CL_H100_temperature_master --manipulatedVariable--> Steam flow set point for FIC100
CL_H100_temperature_master --hasSensor--> TT100
CL_H100_temperature_master --hasController--> TIC100
CL_H100_temperature_master --cascadeMasterOf--> CL_H100_steam_slave
CL_H100_temperature_master --source--> SUMMARY p.190; REPORT D.4.4.c
CL_H100_temperature_master --controlledVariable--> Temperature of MEA leaving H100 into E100
CL_H100_temperature_master --label--> Temperature of MEA leaving H100 (cascade master)
CL_H100_temperature_master --type--> ControlLoop
SteamRoute_step_10_FCV110 --stepItem--> FCV110
SteamRoute_step_10_FCV110 --stepType--> inline
SteamRoute_step_10_FCV110 --label--> Steam and condensate route to H100 step 10: FCV110
SteamRoute_step_10_FCV110 --stepIndex--> 10
SteamRoute_step_10_FCV110 --type--> LoopStep
FT101 --measuredVariable--> steam flow to H100
FT101 --sensorType--> swirl volumetric flow meter
FT101 --monitors--> H100
FT101 --floor--> 1
FT101 --label--> FT101
FT101 --tag--> FT101
FT101 --type--> FlowInstrument
FT101 --gridReference--> L5
FT101 --signalType--> Profibus-PA
CL_H100_steam_slave --hasSensor--> FT101
V102 --feedsInto--> FT101
V102 --pipedTo--> FT101
HAZOP_13_04 --type--> HazopDeviation
HAZOP_13_04 --label--> HAZOP 13.4
HAZOP_13_04 --recommendedAction--> Limit flow through PCV113 by output limit (during commissioning) to ~140kg/hr
HAZOP_13_04 --guideword--> MORE
HAZOP_13_04 --cause--> Excess demand (eg on startup)
HAZOP_13_04 --itemNumber--> 4
HAZOP_13_04 --parameter--> FLOW
HAZOP_13_04 --actionTaken--> Action complete
HAZOP_13_04 --consequence--> Excess demand on building steam supply
SteamRoute --hasStep--> SteamRoute_step_17_K100
SteamRoute --hasStep--> SteamRoute_step_15_PI101
SteamRoute --hasStep--> SteamRoute_step_21_V105
SteamRoute --hasStep--> SteamRoute_step_02_V100
SteamRoute --hasStep--> SteamRoute_step_20_V104
SteamRoute --hasStep--> SteamRoute_step_04_PI100
SteamRoute --hasStep--> SteamRoute_step_13_H100_N_condensate_out
SteamRoute --hasStep--> SteamRoute_step_01_XV140
SteamRoute --type--> Loop
SteamRoute --hasStep--> SteamRoute_step_14_TT118
SteamRoute --hasStep--> SteamRoute_step_07_FI100
SteamRoute --hasStep--> SteamRoute_step_11_TT117
SteamRoute --hasStep--> SteamRoute_step_16_RV107
SteamRoute --hasStep--> SteamRoute_step_22_NRV110
SteamRoute --hasStep--> SteamRoute_step_03_PT101
SteamRoute --note--> Building steam heats the MEA in the H100 reboiler shell and leaves as condensate through the K100 trap. FCV110 sets the steam flow (TIC100 > FIC100 cascade, stripping loop).
SteamRoute --inMode--> FigureOfEight
SteamRoute --hasStep--> SteamRoute_step_09_FT101
SteamRoute --hasStep--> SteamRoute_step_12_H100_N_steam_in
SteamRoute --hasStep--> SteamRoute_step_19_V103
SteamRoute --hasStep--> SteamRoute_step_05_V101
SteamRoute --hasStep--> SteamRoute_step_06_FT100
SteamRoute --hasStep--> SteamRoute_step_08_V102
SteamRoute --hasStep--> SteamRoute_step_10_FCV110
SteamRoute --label--> Steam and condensate route to H100
SteamRoute --hasStep--> SteamRoute_step_00_STEAM_SUPPLY
SteamRoute --hasStep--> SteamRoute_step_23_CONDENSATE_RETURN
SteamRoute --hasStep--> SteamRoute_step_18_V106
discrepancy_FCV110_name --label--> FCV110_name
discrepancy_FCV110_name --type--> PIDDiscrepancy
discrepancy_FCV110_name --source--> P_ID_Differences.pdf
discrepancy_FCV110_name --gridReference--> L5
discrepancy_FCV110_name --asBuilt--> Labelled ZS110 on site
discrepancy_FCV110_name --drawingShows--> Labelled FCV110
CL_H100_steam_slave --manipulatedVariable--> FCV110 opening
CL_H100_steam_slave --source--> SUMMARY p.190; REPORT D.4.4.c
CL_H100_steam_slave --controlledVariable--> Steam flowrate to H100
CL_H100_steam_slave --hasSensor--> FT100
CL_H100_steam_slave --type--> ControlLoop
CL_H100_steam_slave --label--> Steam flow to H100 (cascade slave)
FCV110__cit04 --label--> Citation 4 for FCV110
FCV110__cit04 --citationText--> Pilot Plant Report Fig E.1 and section F.5.4.3
FCV110__cit04 --type--> Citation
FCV110__cit04 --location--> Fig E.1 and section F.5.4.3
FCV110__cit04 --document--> SRC_REPORT
UT01 --type--> OpenItem
UT01 --about--> XV140
UT01 --resolvedBy--> Trace on the P&ID
UT01 --label--> UT01: Order along the steam line (XV140 > V100 > PT101 > V101 > FT100 > V102 > FT101 > FCV110 > H100 > K100 > V103 > V105 > NRV110) is inferred
UT01 --foundBy--> utl section build, Oct 2026
UT01 --description--> Order along the steam line (XV140 > V100 > PT101 > V101 > FT100 > V102 > FT101 > FCV110 > H100 > K100 > V103 > V105 > NRV110) is inferred
UT01 --itemStatus--> open
UT01 --about--> NRV110
UT01 --about--> V100
UT01 --about--> K100
TIC100 --type--> Controller
```

Question: What is the grid reference of the steam flow control valve FCV110?

## Q05

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
LT101 --gridReference--> K8
LT101 --signalType--> Profibus-PA
LT101 --locatedAtStage--> E100_stage_12
LT101 --monitors--> E100
LT101 --note--> Stage mapping inferred: odd Aspen stages are the gaps between packed beds where the side instruments sit; floors match REPORT.
LT101 --sensorType--> differential pressure transmitter
LT101 --type--> LevelInstrument
LT101 --floor--> 1
LT101 --label--> LT101
LT101 --tag--> LT101
LT101 --measuredVariable--> level
IL_E100_level_LL --initiatedBy--> LT101
PROC_pump_start_order_step_03 --type--> ProcedureStep
PROC_pump_start_order_step_03 --operatesOn--> J101a
PROC_pump_start_order_step_03 --instruction--> If LT101 >= LT108, start J101a/b before J100
PROC_pump_start_order_step_03 --stepOrder--> 3
PROC_pump_start_order_step_03 --label--> Order of starting J100 and J101a/b step 3
PROC_pump_start_order --hasProcedureStep--> PROC_pump_start_order_step_03
PROC_pump_start_order_step_01 --operatesOn--> LT108
PROC_pump_start_order_step_01 --stepOrder--> 1
PROC_pump_start_order_step_01 --type--> ProcedureStep
PROC_pump_start_order_step_01 --instruction--> Compare LT101 (E100) and LT108 (E101)
PROC_pump_start_order_step_01 --label--> Order of starting J100 and J101a/b step 1
PROC_pump_start_order --hasProcedureStep--> PROC_pump_start_order_step_01
LT101__cit01 --document--> SRC_PID
LT101__cit01 --location--> grid K8, E100 sump, left-hand side
LT101__cit01 --citationText--> P&ID grid K8, E100 sump, left-hand side
LT101__cit01 --label--> Citation 1 for LT101
LT101__cit01 --type--> Citation
IL_E100_level_LL --tripsItem--> J100
IL_E100_level_LL --label--> E100 low-low level shutdown (protects J100)
IL_E100_level_LL --initiatedBy--> LSLL102
IL_E100_level_LL --type--> Interlock
PROC_pump_start_order_step_02 --type--> ProcedureStep
PROC_pump_start_order_step_02 --instruction--> If LT101 < LT108, start J100 before J101a/b to avoid overfilling
PROC_pump_start_order_step_02 --label--> Order of starting J100 and J101a/b step 2
PROC_pump_start_order_step_02 --stepOrder--> 2
PROC_pump_start_order_step_02 --operatesOn--> J101a
PROC_pump_start_order --hasProcedureStep--> PROC_pump_start_order_step_02
limit_LT101_operating_window --lowValue--> 10.0
limit_LT101_operating_window --limitType--> range
limit_LT101_operating_window --label--> LT101_operating_window
limit_LT101_operating_window --unit--> %
limit_LT101_operating_window --appliesTo--> E100
limit_LT101_operating_window --highValue--> 90.0
limit_LT101_operating_window --note--> Keep LT101 between 10 % and 90 % during the stripping loop test.
limit_LT101_operating_window --type--> OperatingLimit
limit_LT101_operating_window --variable--> level
limit_LT101_operating_window --valueVerified--> true
limit_LT101_operating_window --source--> REPORT E.3.7, E.3.8
LT101__cit03 --document--> SRC_TEAM
LT101__cit03 --label--> Citation 3 for LT101
LT101__cit03 --location--> left-hand side of E100 sump
LT101__cit03 --citationText--> Team check left-hand side of E100 sump
LT101__cit03 --type--> Citation
LT101__cit02 --location--> Appendix B instrument list
LT101__cit02 --document--> SRC_REPORT
LT101__cit02 --label--> Citation 2 for LT101
LT101__cit02 --type--> Citation
LT101__cit02 --citationText--> Pilot Plant Report Appendix B instrument list
```

Question: Which communication protocol is specified for level transmitter LT101?

## Q06

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
FT108 --signalType--> 4-20mA
FT108 --type--> FlowInstrument
FT108 --pipedTo--> FT109
FT108 --feedsInto--> FT109
FT108 --sensorType--> Coriolis mass flow meter
FT108 --pipedTo--> V151
FT108 --measuredVariable--> mass flow and density of rich MEA
FT108 --tag--> FT108
FT108 --floor--> 1
FT108 --monitors--> E101
FT108 --label--> FT108
FT108 --gridReference--> N13
AOI01 --about--> FT108
V144a --pipedTo--> FT108
V144b --feedsInto--> FT108
V144b --pipedTo--> FT108
HAZOP_element_8 --covers--> FT108
V144a --feedsInto--> FT108
DI108 --measuredVariable--> density indication (from FT108)
DI108 --floor--> 1
DI108 --monitors--> E101
DI108 --label--> DI108
DI108 --type--> FlowInstrument
DI108 --tag--> DI108
V151 --type--> ManualValve
V151 --normalPosition--> open
V151 --gridReference--> M9
V151 --floor--> 1
V151 --tag--> V151
V151 --pipedTo--> C100
V151 --label--> V151
V151 --note--> On the rich line from FT108 to the C100 cold side. Other REPORT tables give grid N9 or N8.
HAZOP_element_8 --covers--> V151
FigureOfEight_setting_V151 --valve--> V151
PROC_figure_of_eight_lineup_step_01 --operatesOn--> V151
AOI01 --resolvedBy--> Team check on the full-size P&ID
AOI01 --type--> OpenItem
AOI01 --about--> FT109
AOI01 --description--> Flow direction deduced from the documents (TT209/TT210 descriptions, J101 duty); the arrangement of FT108, FT109 and V124 is inferred from the P&ID
AOI01 --itemStatus--> open
AOI01 --foundBy--> absorption loop build, Oct 2026
AOI01 --label--> AOI01: Flow direction deduced from the documents (TT209/TT210 descriptions, J101 duty); the arrangement of FT108, FT109 and V124 is inferred from the P&ID
AOI01 --about--> V124
AbsorptionLoop_step_10_FT108 --stepItem--> FT108
AbsorptionLoop_step_10_FT108 --label--> Absorption loop step 10: FT108
AbsorptionLoop_step_10_FT108 --stepType--> inline
AbsorptionLoop_step_10_FT108 --type--> LoopStep
AbsorptionLoop_step_10_FT108 --stepIndex--> 10
AbsRoute_J101b_step_10_FT108 --stepType--> inline
AbsRoute_J101b_step_10_FT108 --label--> Absorber recirculation on J101b step 10: FT108
AbsRoute_J101b_step_10_FT108 --stepIndex--> 10
AbsRoute_J101b_step_10_FT108 --type--> LoopStep
AbsRoute_J101b_step_10_FT108 --stepItem--> FT108
FT108__abscit02 --citationText--> Pilot Plant Report Appendix B instrument list; Appendix D: 'rich MEA leaving the absorber (E101) and entering C100'
FT108__abscit02 --type--> Citation
FT108__abscit02 --location--> Appendix B instrument list; Appendix D: 'rich MEA leaving the absorber (E101) and entering C100'
FT108__abscit02 --document--> SRC_REPORT
FT108__abscit02 --label--> Citation 2 for FT108 (absorption loop)
HAZOP_element_8 --covers--> V144b
HAZOP_element_8 --covers--> PCV120a
HAZOP_element_8 --covers--> PCV120b
HAZOP_element_8 --covers--> V402
HAZOP_element_8 --covers--> V134a
HAZOP_element_8 --covers--> J101a
HAZOP_element_8 --covers--> C100
HAZOP_element_8 --label--> HAZOP element 8: RICH MEA line from E101 to E100
HAZOP_element_8 --covers--> J101b
HAZOP_element_8 --covers--> SDV152
HAZOP_element_8 --covers--> V135b
HAZOP_element_8 --covers--> V150
HAZOP_element_8 --covers--> V143b
HAZOP_element_8 --covers--> V143a
HAZOP_element_8 --elementNumber--> 8
HAZOP_element_8 --covers--> V134b
HAZOP_element_8 --covers--> V403
HAZOP_element_8 --type--> HazopElement
HAZOP_element_8 --covers--> V144a
HAZOP_element_8 --source--> 27794_Plant_HAZREP, HAZOP study 6-7 May 2010, drawing 55_200_1001 issue 1. Elements 7, 8, 11 and 13 (those touching the stripping loop).
HAZOP_element_8 --covers--> V135a
HAZOP_8_03 --inElement--> HAZOP_element_8
HAZOP_8_01 --inElement--> HAZOP_element_8
HAZOP_8_06 --inElement--> HAZOP_element_8
HAZOP_8_07 --inElement--> HAZOP_element_8
HAZOP_8_09 --inElement--> HAZOP_element_8
HAZOP_8_04 --inElement--> HAZOP_element_8
HAZOP_8_05 --inElement--> HAZOP_element_8
HAZOP_8_11 --inElement--> HAZOP_element_8
HAZOP_8_02 --inElement--> HAZOP_element_8
HAZOP_8_08 --inElement--> HAZOP_element_8
HAZOP_8_10 --inElement--> HAZOP_element_8
V144b --type--> ManualValve
V144b --tag--> V144b
V144b --normalPosition--> closed
V144b --floor--> 1
V144b --valveType--> ball
V144b --gridReference--> L14
V144b --label--> V144b
V143b --feedsInto--> V144b
V143b --pipedTo--> V144b
PROC_J101b_startup_step_06 --operatesOn--> V144b
FigureOfEight_setting_V144b --valve--> V144b
AbsRoute_J101b_setting_V144b --valve--> V144b
AbsRoute_J101a_setting_V144b --valve--> V144b
PROC_figure_of_eight_lineup_step_17 --operatesOn--> V144b
V144a --label--> V144a
V144a --type--> ManualValve
V144a --tag--> V144a
V144a --normalPosition--> open
V144a --valveType--> ball
V144a --floor--> 1
V144a --gridReference--> N14
V143a --feedsInto--> V144a
PROC_figure_of_eight_lineup_step_13 --operatesOn--> V144a
AbsRoute_J101b_setting_V144a --valve--> V144a
FigureOfEight_setting_V144a --valve--> V144a
PROC_J101a_startup_step_06 --operatesOn--> V144a
AbsRoute_J101a_setting_V144a --valve--> V144a
V143a --pipedTo--> V144a
FT108__abscit01 --location--> grid N13
FT108__abscit01 --type--> Citation
FT108__abscit01 --citationText--> P&ID grid N13
FT108__abscit01 --document--> SRC_PID
FT108__abscit01 --label--> Citation 1 for FT108 (absorption loop)
AbsRoute_J101a_step_10_FT108 --stepIndex--> 10
AbsRoute_J101a_step_10_FT108 --type--> LoopStep
AbsRoute_J101a_step_10_FT108 --stepType--> inline
AbsRoute_J101a_step_10_FT108 --label--> Absorber recirculation on J101a step 10: FT108
AbsRoute_J101a_step_10_FT108 --stepItem--> FT108
FigureOfEight_step_07_FT108 --stepType--> inline
FigureOfEight_step_07_FT108 --type--> LoopStep
FigureOfEight_step_07_FT108 --label--> Figure-of-eight circulation (normal running) step 7: FT108
FigureOfEight_step_07_FT108 --stepItem--> FT108
FigureOfEight_step_07_FT108 --nextStep--> FigureOfEight_step_08_V151
FigureOfEight_step_07_FT108 --stepIndex--> 7
FigureOfEight_step_06_V144b --nextStep--> FigureOfEight_step_07_FT108
FigureOfEight_step_06_V144a --nextStep--> FigureOfEight_step_07_FT108
FT109 --pipedTo--> V124
FT109 --feedsInto--> V124
C100 --pipedTo--> SDV152
C100 --pipedTo--> V113a
C100 --feedsInto--> V113a
V112 --pipedTo--> C100
V112 --feedsInto--> C100
PCV120b --pipedTo--> V143b
PCV120b --feedsInto--> V143b
V124 --pipedTo--> V198b
V124 --feedsInto--> V119b
V124 --pipedTo--> V119b
PCV120a --feedsInto--> V143a
PCV120a --pipedTo--> V143a
```

Question: What type of flowmeter is FT108?

## Q07

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
AT400 --monitors--> E101
AT400 --measuredVariable--> CO2 in gas samples along E101
AT400 --type--> Instrument
AT400 --sensorType--> ABB gas analyser
AT400 --tag--> AT400
AT400 --label--> AT400
E101_sample_6 --sampledBy--> AT400
E101_sample_2 --sampledBy--> AT400
AOI13 --about--> AT400
E101_sample_1 --sampledBy--> AT400
E101_sample_3 --sampledBy--> AT400
E101_sample_5 --sampledBy--> AT400
E101_sample_4 --sampledBy--> AT400
E101_sample_5 --onColumn--> E101
E101_sample_5 --height_m--> 1.37
E101_sample_5 --label--> E101 gas sample point 5 (1.37 m)
E101_sample_5 --pairedWith--> TT204
E101_sample_5 --type--> SamplePoint
E101_sample_5 --sampleValve--> V205
E101_sample_5 --sampleNumber--> 5
AT400__abscit02 --label--> Citation 2 for AT400 (absorption loop)
AT400__abscit02 --location--> Fig 4.1
AT400__abscit02 --type--> Citation
AT400__abscit02 --document--> SRC_REPORT
AT400__abscit02 --citationText--> Pilot Plant Report Fig 4.1
E101_sample_1 --height_m--> 6.85
E101_sample_1 --sampleValve--> V408
E101_sample_1 --label--> E101 gas sample point 1 (6.85 m)
E101_sample_1 --type--> SamplePoint
E101_sample_1 --sampleNumber--> 1
E101_sample_1 --pairedWith--> TT413
E101_sample_1 --onColumn--> E101
E101_sample_3 --sampleNumber--> 3
E101_sample_3 --onColumn--> E101
E101_sample_3 --pairedWith--> TT305
E101_sample_3 --height_m--> 4.11
E101_sample_3 --sampleValve--> V306
E101_sample_3 --label--> E101 gas sample point 3 (4.11 m)
E101_sample_3 --type--> SamplePoint
E101_sample_4 --label--> E101 gas sample point 4 (2.74 m)
E101_sample_4 --onColumn--> E101
E101_sample_4 --sampleNumber--> 4
E101_sample_4 --sampleValve--> V207
E101_sample_4 --type--> SamplePoint
E101_sample_4 --pairedWith--> TT206
E101_sample_4 --height_m--> 2.74
E101_sample_6 --height_m--> 0.0
E101_sample_6 --onColumn--> E101
E101_sample_6 --sampleNumber--> 6
E101_sample_6 --pairedWith--> TT109
E101_sample_6 --label--> E101 gas sample point 6 (0.0 m)
E101_sample_6 --type--> SamplePoint
E101_sample_2 --label--> E101 gas sample point 2 (5.48 m)
E101_sample_2 --type--> SamplePoint
E101_sample_2 --height_m--> 5.48
E101_sample_2 --sampleNumber--> 2
E101_sample_2 --onColumn--> E101
E101_sample_2 --pairedWith--> TT307
E101_sample_2 --sampleValve--> V308
AOI13 --label--> AOI13: Sample valves for E101 samples 1 and 6 are not identified on the P&ID
AOI13 --type--> OpenItem
AOI13 --foundBy--> absorption loop build, Oct 2026
AOI13 --description--> Sample valves for E101 samples 1 and 6 are not identified on the P&ID
AOI13 --itemStatus--> open
AOI13 --resolvedBy--> Full-size P&ID or site check
AT400__abscit01 --location--> row AT400 (samples along the absorber, 'SAMPLE TO ABB GAS ANALYSER')
AT400__abscit01 --label--> Citation 1 for AT400 (absorption loop)
AT400__abscit01 --type--> Citation
AT400__abscit01 --document--> SRC_DIFF
AT400__abscit01 --citationText--> P&ID differences row AT400 (samples along the absorber, 'SAMPLE TO ABB GAS ANALYSER')
```

Question: What measurement method and signal protocol does AT400 use?

## Q08

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
aspen_v3_block_E101 --type--> AspenBlock
aspen_v3_block_E101 --aspenModel--> RADFRAC
aspen_v3_block_E101 --blockId--> E101
aspen_v3_block_E101 --status--> OK
aspen_v3_block_E101 --label--> E101 (ABB_pilot_plant_final_3)
aspen_v3_block_E101 --inCase--> case_aspen_v3
aspen_v3_stream_S8 --fromBlock--> aspen_v3_block_E101
aspen_v3_stream_1 --toBlock--> aspen_v3_block_E101
aspen_v3_stream_2 --toBlock--> aspen_v3_block_E101
aspen_v3_stream_4 --fromBlock--> aspen_v3_block_E101
LT108 --tag--> LT108
LT108 --type--> LevelInstrument
LT108 --floor--> 1
LT108 --monitors--> E101
LT108 --label--> LT108
LT108 --gridReference--> K15
LT108 --signalType--> Fieldbus
LT108 --measuredVariable--> E101 sump level
LT108 --sensorType--> differential pressure transmitter
PROC_pump_start_order_step_01 --operatesOn--> LT108
CL_E101_level --hasSensor--> LT108
aspen_v6_1_block_E101 --type--> AspenBlock
aspen_v6_1_block_E101 --aspenModel--> RADFRAC
aspen_v6_1_block_E101 --label--> E101 (ABB_pilot_plant_final_6_1_SA_validation)
aspen_v6_1_block_E101 --blockId--> E101
aspen_v6_1_block_E101 --status--> OK
aspen_v6_1_block_E101 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S8 --fromBlock--> aspen_v6_1_block_E101
aspen_v6_1_stream_2 --toBlock--> aspen_v6_1_block_E101
aspen_v6_1_stream_1 --toBlock--> aspen_v6_1_block_E101
aspen_v6_1_stream_4 --fromBlock--> aspen_v6_1_block_E101
E101 --pipedTo--> RV400
E101 --floor--> 1
E101 --note--> Lean MEA enters at the top through NRV400; rich MEA leaves from the sump to J101a/b. The air admittance valve shown on the P&ID has been removed from the plant (DIFF, E14/15).
E101 --feedsInto--> E101_N_sump_outlet
E101 --designBasis--> Packing and column designed for 2.3-2.5 bar operation on MEA and 50 kg/h CO2 (HAZOP 10.4)
E101 --feedsInto--> E101_N_gas_outlet
E101 --pipedTo--> E101_N_sump_outlet
E101 --pipedTo--> E101_N_gas_outlet
E101 --type--> AbsorptionColumn
E101 --diameter_mm--> 230.0
E101 --tag--> E101
E101 --label--> E101 absorber
HAZOP_7_10 --concerns--> E101
TT305 --monitors--> E101
PT111 --monitors--> E101
E101_sample_5 --onColumn--> E101
E101_N_gas_outlet --onEquipment--> E101
LSLL109 --monitors--> E101
TT207 --monitors--> E101
PT403 --monitors--> E101
LI108 --monitors--> E101
E101_sample_4 --onColumn--> E101
E101_N_sump_outlet --onEquipment--> E101
FT109 --monitors--> E101
E101_sample_3 --onColumn--> E101
HAZOP_9b_05 --concerns--> E101
limit_LZAL109 --appliesTo--> E101
DI108 --monitors--> E101
E101_N_gas_inlet --feedsInto--> E101
FT304 --monitors--> E101
K101_N2_recycle --bypasses--> E101
PT110 --monitors--> E101
E101_N_gas_inlet --pipedTo--> E101
HAZOP_5_08 --concerns--> E101
HAZOP_8_01 --concerns--> E101
HAZOP_8_06 --concerns--> E101
PI403 --monitors--> E101
AT400 --monitors--> E101
FT303 --monitors--> E101
TT205 --monitors--> E101
E101_N_base_inlet --onEquipment--> E101
aspen_v6_1_E101_performance --ofEquipment--> E101
TT206 --monitors--> E101
HAZOP_8_03 --concerns--> E101
E101_N_gas_inlet --onEquipment--> E101
E101_N_top_inlet --feedsInto--> E101
E101_sample_6 --onColumn--> E101
K402 --pipedTo--> E101
HAZOP_5_07 --concerns--> E101
AI300 --monitors--> E101
FI109 --monitors--> E101
FI108 --monitors--> E101
aspen_v3_vent_gas --ofEquipment--> E101
AT300 --monitors--> E101
E101_N_top_inlet --pipedTo--> E101
aspen_v6_1_feed_gas --ofEquipment--> E101
limit_PSHH117_set --appliesTo--> E101
TT109 --monitors--> E101
TT412 --monitors--> E101
HAZOP_10_03 --concerns--> E101
LSHH107 --monitors--> E101
E101_sample_2 --onColumn--> E101
limit_LZAH107 --appliesTo--> E101
HAZOP_5_06 --concerns--> E101
PSHH117 --monitors--> E101
TT413 --monitors--> E101
HAZOP_7_13 --concerns--> E101
TT107 --monitors--> E101
TT306 --monitors--> E101
E101_N_top_inlet --onEquipment--> E101
E101_sample_1 --onColumn--> E101
AOI10 --about--> E101
RV400 --protects--> E101
FT108 --monitors--> E101
TT411 --monitors--> E101
TT204 --monitors--> E101
aspen_v3_feed_gas --ofEquipment--> E101
HAZOP_element_10 --covers--> E101
HAZOP_8_11 --concerns--> E101
TT307 --monitors--> E101
TT308 --monitors--> E101
HAZOP_8_02 --concerns--> E101
aspen_v3_E101_performance --ofEquipment--> E101
PCV300 --valveType--> pressure control
PCV300 --floor--> 3
PCV300 --normalPosition--> open
PCV300 --note--> Vents lean gas from the absorber to hold the E101 pressure (PIC403). Opened in the vent stream start-up (Fig F.3), closed at shutdown.
PCV300 --pipedTo--> VENT_E101
PCV300 --label--> PCV300
PCV300 --feedsInto--> VENT_E101
PCV300 --type--> PressureControlValve
PCV300 --tag--> PCV300
PCV300 --gridReference--> G18
K402 --feedsInto--> PCV300
CL_E101_pressure --hasFinalElement--> PCV300
K402 --pipedTo--> PCV300
PIC403 --controls--> PCV300
AV01 --about--> PCV300
K101 --type--> Saturator
K101 --label--> K101 gas saturator
K101 --pipedTo--> SDV170
K101 --pipedTo--> Z103
K101 --floor--> 1
K101 --feedsInto--> E101_N_gas_inlet
K101 --pipedTo--> E101_N_gas_inlet
K101 --note--> Saturates the feed gas with water before E101; temperature held by TIC121 using C106 on the recirculating water. Grid not in the REPORT lists (near L17 to L18 on the P&ID). Not modelled in Aspen (GOI09).
K101 --pipedTo--> V126
K101 --tag--> K101
DI_CARTRIDGE --feedsInto--> K101
HAZOP_4_06 --concerns--> K101
V172 --pipedTo--> K101
J102 --pipedTo--> K101
limit_LZAL_K101 --appliesTo--> K101
HAZOP_4_07 --concerns--> K101
LT104 --monitors--> K101
HAZOP_3_05 --concerns--> K101
FEED_GAS_HEADER --feedsInto--> K101
GOI09 --about--> K101
LI106 --monitors--> K101
```

Question: At which grid reference is the absorber level transmitter LT108 located?

## Q09

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
B300 --note--> Dead-end branch (team trace). Operates at 3 bar, not the 8 bar shown near it on the P&ID; the 8 bar belongs to PCV302 (DIFF, team).
B300 --floor--> 3
B300 --type--> PulsationDampener
B300 --gridReference--> G9
B300 --tag--> B300
B300 --label--> B300 pulsation dampener on the J300 discharge
discrepancy_B300_pressure --concerns--> B300
J300 --pipedTo--> B300
limit_B300_operating --appliesTo--> B300
OverheadRefluxLoop_step_10_B300 --stepItem--> B300
OverheadRefluxLoop_step_10_B300 --label--> Stripper overhead and reflux loop step 10: B300
OverheadRefluxLoop_step_10_B300 --stepType--> tie-in
OverheadRefluxLoop_step_10_B300 --stepIndex--> 10
OverheadRefluxLoop_step_10_B300 --type--> LoopStep
B300__ovhcit02 --label--> Citation 2 for B300 (ovh)
B300__ovhcit02 --type--> Citation
B300__ovhcit02 --document--> SRC_DIFF
B300__ovhcit02 --citationText--> P&ID differences row B300 (operates at 3 bar not 8 bar, G9)
B300__ovhcit02 --location--> row B300 (operates at 3 bar not 8 bar, G9)
discrepancy_B300_pressure --drawingShows--> 8 bar shown next to B300
discrepancy_B300_pressure --gridReference--> G9
discrepancy_B300_pressure --label--> B300_pressure
discrepancy_B300_pressure --asBuilt--> B300 operates at 3 bar
discrepancy_B300_pressure --type--> PIDDiscrepancy
B300__ovhcit01 --location--> grid G9
B300__ovhcit01 --type--> Citation
B300__ovhcit01 --document--> SRC_PID
B300__ovhcit01 --label--> Citation 1 for B300 (ovh)
B300__ovhcit01 --citationText--> P&ID grid G9
J300 --gridReference--> G10
J300 --pipedTo--> PCV302
J300 --note--> Speed set by SIC300 from the K401 level (LT401, LIC401).
J300 --label--> J300 reflux pump
J300 --floor--> 3
J300 --tag--> J300
J300 --pipedTo--> RV300
J300 --type--> Pump
J300 --feedsInto--> PCV302
K401 --pipedTo--> J300
CL_K401_level --hasFinalElement--> J300
K401 --feedsInto--> J300
SIC300 --controls--> J300
LIC401 --controls--> J300
OOI04 --about--> J300
TT309 --monitors--> J300
RV301 --protects--> J300
HAZOP_element_12 --covers--> J300
TT310 --monitors--> J300
RV300 --protects--> J300
FT305 --monitors--> J300
limit_B300_operating --type--> OperatingLimit
limit_B300_operating --valueVerified--> false
limit_B300_operating --unit--> bar
limit_B300_operating --highValue--> 3.0
limit_B300_operating --limitType--> operating
limit_B300_operating --source--> DIFF row B300 (operates at 3 bar not 8 bar)
limit_B300_operating --label--> B300_operating
limit_B300_operating --variable--> pressure
B300__ovhcit03 --location--> B300 is a dead end; 8 bar is the PCV302 setting
B300__ovhcit03 --citationText--> Team check B300 is a dead end; 8 bar is the PCV302 setting
B300__ovhcit03 --label--> Citation 3 for B300 (ovh)
B300__ovhcit03 --type--> Citation
B300__ovhcit03 --document--> SRC_TEAM
K401 --pipedTo--> K401_N_gas_outlet
K401 --feedsInto--> K401_N_gas_outlet
C400 --pipedTo--> K401
C400 --feedsInto--> K401
PCV302 --feedsInto--> FT305
PCV302 --pipedTo--> FT305
PCV302 --pipedTo--> V317
```

Question: What is the actual operating pressure of B300, rather than the value shown on the P&ID?

## Q10

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
V403 --pipedTo--> V402
V403 --feedsInto--> V402
V403 --valveType--> ball
V403 --gridReference--> F8
V403 --note--> REPORT Fig B.24 gives floor 4; DIFF and REPORT Fig E.2 give floor 3.
V403 --tag--> V403
V403 --floor--> 3
V403 --type--> ManualValve
V403 --label--> V403
V403 --normalPosition--> open
Route_A_top_filter_setting_V403 --valve--> V403
H200a --feedsInto--> V403
discrepancy_V402_V403_floor --concerns--> V403
H200a --pipedTo--> V403
OOI03 --about--> V403
Route_B_top_bypass_setting_V403 --valve--> V403
PROC_switch_to_side_return_step_02 --operatesOn--> V403
Route_C_side_filter_setting_V403 --valve--> V403
Route_D_side_bypass_setting_V403 --valve--> V403
H200b --feedsInto--> V403
H200b --pipedTo--> V403
FigureOfEight_setting_V403 --valve--> V403
PROC_figure_of_eight_lineup_step_08 --operatesOn--> V403
FT305 --feedsInto--> V403
OI10 --about--> V403
HAZOP_element_8 --covers--> V403
FT305 --pipedTo--> V403
PROC_stripping_loop_lineup_step_23 --operatesOn--> V403
V402 --pipedTo--> E100_N_top_inlet
V402 --normalPosition--> open
V402 --feedsInto--> E100_N_top_inlet
V402 --valveType--> ball
V402 --gridReference--> F8
V402 --label--> V402
V402 --type--> ManualValve
V402 --note--> REPORT Fig B.24 gives floor 4; DIFF and REPORT Fig E.2 give floor 3.
V402 --tag--> V402
V402 --floor--> 3
Route_C_side_filter_setting_V402 --valve--> V402
FigureOfEight_setting_V402 --valve--> V402
Route_D_side_bypass_setting_V402 --valve--> V402
Route_A_top_filter_setting_V402 --valve--> V402
HAZOP_element_8 --covers--> V402
discrepancy_V402_V403_floor --concerns--> V402
PROC_figure_of_eight_lineup_step_09 --operatesOn--> V402
PROC_stripping_loop_lineup_step_24 --operatesOn--> V402
Route_B_top_bypass_setting_V402 --valve--> V402
PROC_switch_to_side_return_step_03 --operatesOn--> V402
H200b --pipedTo--> V309
H200b --tag--> H200b
H200b --type--> ElectricHeater
H200b --label--> H200b electric heater
H200b --floor--> 2
H200b --gridReference--> J11
TIC213b --controls--> H200b
TSHH212b --monitors--> H200b
IL_H200b_HH --tripsItem--> H200b
OI13 --about--> H200b
TZAHH212b --controls--> H200b
PROC_heater_overtemperature_step_03 --operatesOn--> H200b
aspen_v3_H200b_performance --ofEquipment--> H200b
OI01 --about--> H200b
aspen_v6_1_block_H200B --represents--> H200b
OI06 --about--> H200b
limit_TSHH212b --appliesTo--> H200b
TT212b --monitors--> H200b
IL_heater_outlet_H --tripsItem--> H200b
SDV125 --feedsInto--> H200b
aspen_v3_block_H200B --represents--> H200b
TY213b --controls--> H200b
SDV125 --pipedTo--> H200b
SDV152 --pipedTo--> H200b
OI09 --about--> H200b
aspen_v6_1_H200b_performance --ofEquipment--> H200b
TZH213 --controls--> H200b
CL_H200b_temperature --hasFinalElement--> H200b
HS200b --controls--> H200b
V402__cit02 --location--> Fig E.1/E.2 (stripping loop commissioning line-up)
V402__cit02 --type--> Citation
V402__cit02 --citationText--> Pilot Plant Report Fig E.1/E.2 (stripping loop commissioning line-up)
V402__cit02 --document--> SRC_REPORT
V402__cit02 --label--> Citation 2 for V402
Route_C_side_filter_setting_V403 --type--> ValveSetting
Route_C_side_filter_setting_V403 --label--> V403 in Route C: side return (stage 3), through Z102
Route_C_side_filter_setting_V403 --requiredPosition--> closed
Route_C_side_filter --hasValveSetting--> Route_C_side_filter_setting_V403
V402__cit03 --location--> row V402 & V403 (F8)
V402__cit03 --type--> Citation
V402__cit03 --label--> Citation 3 for V402
V402__cit03 --citationText--> P&ID differences row V402 & V403 (F8)
V402__cit03 --document--> SRC_DIFF
FigureOfEight_setting_V402 --type--> ValveSetting
FigureOfEight_setting_V402 --label--> V402 in Figure-of-eight circulation (normal running)
FigureOfEight_setting_V402 --requiredPosition--> open
FigureOfEight --hasValveSetting--> FigureOfEight_setting_V402
FT305 --label--> FT305
FT305 --tag--> FT305
FT305 --measuredVariable--> mass flow (reflux from J300)
FT305 --gridReference--> F9
FT305 --type--> FlowInstrument
FT305 --signalType--> Profibus-PA
FT305 --floor--> 3
FT305 --sensorType--> Coriolis mass flow meter
FT305 --monitors--> J300
OOI03 --about--> FT305
PCV302 --feedsInto--> FT305
PCV302 --pipedTo--> FT305
discrepancy_TT309_FT305_order --concerns--> FT305
H200a --label--> H200a electric heater
H200a --type--> ElectricHeater
H200a --tag--> H200a
H200a --floor--> 2
H200a --pipedTo--> V309
H200a --gridReference--> J10
SDV125 --pipedTo--> H200a
IL_H200a_HH --tripsItem--> H200a
SDV152 --pipedTo--> H200a
TY213a --controls--> H200a
TT212a --monitors--> H200a
OI09 --about--> H200a
limit_TSHH212a --appliesTo--> H200a
aspen_v6_1_H200a_performance --ofEquipment--> H200a
TZH213 --controls--> H200a
CL_H200a_temperature --hasFinalElement--> H200a
PROC_heater_overtemperature_step_02 --operatesOn--> H200a
TZAHH212a --controls--> H200a
OI13 --about--> H200a
PROC_heater_overtemperature_step_06 --operatesOn--> H200a
aspen_v3_H200a_performance --ofEquipment--> H200a
TIC213a --controls--> H200a
HS200a --controls--> H200a
aspen_v3_block_H200A --represents--> H200a
aspen_v6_1_block_H200A --represents--> H200a
OI01 --about--> H200a
OI06 --about--> H200a
TSHH212a --monitors--> H200a
IL_heater_outlet_H --tripsItem--> H200a
SDV125 --feedsInto--> H200a
Route_B_top_bypass_step_36_V403 --label--> Route B: top return (stage 1), Z102 bypassed step 36: V403
Route_B_top_bypass_step_36_V403 --stepType--> inline
Route_B_top_bypass_step_36_V403 --type--> LoopStep
Route_B_top_bypass_step_36_V403 --stepIndex--> 36
Route_B_top_bypass_step_36_V403 --nextStep--> Route_B_top_bypass_step_37_V402
Route_B_top_bypass_step_36_V403 --stepItem--> V403
Route_B_top_bypass_step_33_H200a --nextStep--> Route_B_top_bypass_step_36_V403
Route_B_top_bypass_step_33_H200b --nextStep--> Route_B_top_bypass_step_36_V403
PROC_figure_of_eight_lineup_step_09 --requiredPosition--> open
PROC_figure_of_eight_lineup_step_09 --type--> ProcedureStep
PROC_figure_of_eight_lineup_step_09 --stepOrder--> 9
PROC_figure_of_eight_lineup_step_09 --instruction--> Set V402 open
```

Question: On which floor are V402 and V403 physically located?

## Q11

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
PCV120b --floor--> 1
PCV120b --type--> PressureControlValve
PCV120b --pipedTo--> V143b
PCV120b --note--> Not drawn on the P&ID; as-built it sits between J101b and B103b (DIFF).
PCV120b --feedsInto--> V143b
PCV120b --valveType--> pressure control
PCV120b --label--> PCV120b
PCV120b --tag--> PCV120b
PCV120b --normalPosition--> open
PCV120b --gridReference--> L14
J101b --pipedTo--> PCV120b
discrepancy_PCV120b_missing --concerns--> PCV120b
HAZOP_element_8 --covers--> PCV120b
limit_PCV120b_set --appliesTo--> PCV120b
J101b --feedsInto--> PCV120b
limit_PCV120b_set --type--> OperatingLimit
limit_PCV120b_set --valueVerified--> false
limit_PCV120b_set --unit--> bar
limit_PCV120b_set --limitType--> setpoint
limit_PCV120b_set --highValue--> 8.0
limit_PCV120b_set --variable--> pressure
limit_PCV120b_set --label--> PCV120b_set
limit_PCV120b_set --source--> PID 'PCV SET TO 120b 8 bar'
FigureOfEight_step_04_PCV120b --stepItem--> PCV120b
FigureOfEight_step_04_PCV120b --stepType--> inline
FigureOfEight_step_04_PCV120b --nextStep--> FigureOfEight_step_05_V143b
FigureOfEight_step_04_PCV120b --type--> LoopStep
FigureOfEight_step_04_PCV120b --label--> Figure-of-eight circulation (normal running) step 4: PCV120b
FigureOfEight_step_04_PCV120b --stepIndex--> 4
FigureOfEight_step_03_J101b --nextStep--> FigureOfEight_step_04_PCV120b
PCV120b__abscit02 --citationText--> Pilot Plant Report valve list (L14, floor 1)
PCV120b__abscit02 --type--> Citation
PCV120b__abscit02 --document--> SRC_REPORT
PCV120b__abscit02 --location--> valve list (L14, floor 1)
PCV120b__abscit02 --label--> Citation 2 for PCV120b (absorption loop)
J101b --floor--> 1
J101b --type--> Pump
J101b --gridReference--> N16
J101b --label--> J101b rich MEA pump (duty or standby)
J101b --tag--> J101b
J101b --note--> Parallel to J101a; only one runs at a time.
ROI03 --about--> J101b
LIC108 --controls--> J101b
CL_E101_level --hasFinalElement--> J101b
IL_E101_level_LL --tripsItem--> J101b
AOI04 --about--> J101b
PROC_J101b_startup_step_07 --operatesOn--> J101b
TT111b --monitors--> J101b
PT115b --monitors--> J101b
HAZOP_element_8 --covers--> J101b
V135b --feedsInto--> J101b
IL_E101_level_HH --tripsItem--> J101b
TT110b --monitors--> J101b
V135b --pipedTo--> J101b
AOI09 --about--> J101b
PROC_J101a_startup_step_01 --operatesOn--> J101b
PROC_J101b_startup_step_02 --operatesOn--> J101b
SIC101b --controls--> J101b
AOI02 --about--> J101b
AbsorptionLoop_step_05_PCV120b --label--> Absorption loop step 5: PCV120b
AbsorptionLoop_step_05_PCV120b --stepItem--> PCV120b
AbsorptionLoop_step_05_PCV120b --type--> LoopStep
AbsorptionLoop_step_05_PCV120b --stepType--> inline
AbsorptionLoop_step_05_PCV120b --stepIndex--> 5
discrepancy_PCV120b_missing --drawingShows--> PCV120b not shown
discrepancy_PCV120b_missing --asBuilt--> PCV120b between J101b and B103b
discrepancy_PCV120b_missing --type--> PIDDiscrepancy
discrepancy_PCV120b_missing --gridReference--> N17
discrepancy_PCV120b_missing --label--> PCV120b_missing
HAZOP_element_8 --covers--> V144b
HAZOP_element_8 --covers--> PCV120a
HAZOP_element_8 --covers--> V402
HAZOP_element_8 --covers--> V151
HAZOP_element_8 --covers--> V134a
HAZOP_element_8 --covers--> J101a
HAZOP_element_8 --covers--> C100
HAZOP_element_8 --label--> HAZOP element 8: RICH MEA line from E101 to E100
HAZOP_element_8 --covers--> SDV152
HAZOP_element_8 --covers--> V135b
HAZOP_element_8 --covers--> V150
HAZOP_element_8 --covers--> V143b
HAZOP_element_8 --covers--> V143a
HAZOP_element_8 --elementNumber--> 8
HAZOP_element_8 --covers--> V134b
HAZOP_element_8 --covers--> V403
HAZOP_element_8 --type--> HazopElement
HAZOP_element_8 --covers--> V144a
HAZOP_element_8 --source--> 27794_Plant_HAZREP, HAZOP study 6-7 May 2010, drawing 55_200_1001 issue 1. Elements 7, 8, 11 and 13 (those touching the stripping loop).
HAZOP_element_8 --covers--> FT108
HAZOP_element_8 --covers--> V135a
HAZOP_8_03 --inElement--> HAZOP_element_8
HAZOP_8_01 --inElement--> HAZOP_element_8
HAZOP_8_06 --inElement--> HAZOP_element_8
HAZOP_8_07 --inElement--> HAZOP_element_8
HAZOP_8_09 --inElement--> HAZOP_element_8
HAZOP_8_04 --inElement--> HAZOP_element_8
HAZOP_8_05 --inElement--> HAZOP_element_8
HAZOP_8_11 --inElement--> HAZOP_element_8
HAZOP_8_02 --inElement--> HAZOP_element_8
HAZOP_8_08 --inElement--> HAZOP_element_8
HAZOP_8_10 --inElement--> HAZOP_element_8
AbsRoute_J101b_step_05_PCV120b --stepItem--> PCV120b
AbsRoute_J101b_step_05_PCV120b --stepIndex--> 5
AbsRoute_J101b_step_05_PCV120b --stepType--> inline
AbsRoute_J101b_step_05_PCV120b --type--> LoopStep
AbsRoute_J101b_step_05_PCV120b --label--> Absorber recirculation on J101b step 5: PCV120b
B103b --floor--> 1
B103b --tag--> B103b
B103b --note--> Function inferred from the P&ID symbol (same as B101 on J100). DIFF: PCV120b sits between J101b and B103b but is not drawn.
B103b --label--> B103b pulsation dampener on the J101b discharge
B103b --type--> PulsationDampener
AOI03 --about--> B103b
PCV120b__abscit01 --location--> row PCV120b (N17)
PCV120b__abscit01 --label--> Citation 1 for PCV120b (absorption loop)
PCV120b__abscit01 --type--> Citation
PCV120b__abscit01 --citationText--> P&ID differences row PCV120b (N17)
PCV120b__abscit01 --document--> SRC_DIFF
V143b --feedsInto--> V144b
V143b --pipedTo--> V144b
V144b --feedsInto--> FT108
V144b --pipedTo--> FT108
V134b --feedsInto--> V135b
V134b --pipedTo--> V135b
```

Question: Where should PCV120b be located in the actual plant?

## Q12

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
RV401 --pipedTo--> K403
RV401 --gridReference--> F7
RV401 --note--> E100 relief; discharges to knockout drum K403 (DIFF).
RV401 --protects--> E100
RV401 --type--> ReliefValve
RV401 --floor--> 4
RV401 --label--> RV401
RV401 --valveType--> relief
RV401 --normalPosition--> closed
RV401 --tag--> RV401
HAZOP_element_11 --covers--> RV401
discrepancy_K403_missing --concerns--> RV401
HAZOP_11_08 --type--> HazopDeviation
HAZOP_11_08 --recommendedAction--> Put a PSH onto the column; size RV100 for maximum filling gas feed rate
HAZOP_11_08 --inElement--> HAZOP_element_11
HAZOP_11_08 --safeguard--> RV400
HAZOP_11_08 --itemNumber--> 8
HAZOP_11_08 --actionTaken--> PSH added
HAZOP_11_08 --parameter--> PRESSURE
HAZOP_11_08 --label--> HAZOP 11.8
HAZOP_11_08 --guideword--> HIGHER
HAZOP_11_08 --cause--> Failure of pressure control system
RV400 --gridReference--> E15
RV400 --type--> ReliefValve
RV400 --valveType--> relief
RV400 --normalPosition--> closed
RV400 --note--> E101 relief valve, sized for maximum filling gas rate (HAZOP 10.8); discharges to knockout drum K403 (DIFF).
RV400 --label--> RV400
RV400 --pipedTo--> K403
RV400 --protects--> E101
RV400 --tag--> RV400
HAZOP_10_08 --concerns--> RV400
E101 --pipedTo--> RV400
HAZOP_3_02 --concerns--> RV400
AV06 --about--> RV400
HAZOP_element_10 --covers--> RV400
HAZOP_10_08 --cause--> Failure of pressure control system
HAZOP_10_08 --actionTaken--> Action completed
HAZOP_10_08 --itemNumber--> 8
HAZOP_10_08 --safeguard--> RV400
HAZOP_10_08 --recommendedAction--> Put a PSH onto the column; size RV400 for maximum filling gas feed rate
HAZOP_10_08 --inElement--> HAZOP_element_10
HAZOP_10_08 --parameter--> PRESSURE
HAZOP_10_08 --label--> HAZOP 10.8
HAZOP_10_08 --type--> HazopDeviation
HAZOP_10_08 --guideword--> HIGHER
RV401__cit02 --document--> SRC_DIFF
RV401__cit02 --location--> row K403 (E7)
RV401__cit02 --label--> Citation 2 for RV401
RV401__cit02 --citationText--> P&ID differences row K403 (E7)
RV401__cit02 --type--> Citation
AV06 --label--> AV06: RV400 set pressure and how K403 drains are not documented
AV06 --description--> RV400 set pressure and how K403 drains are not documented
AV06 --resolvedBy--> Site check or relief valve datasheet
AV06 --type--> OpenItem
AV06 --foundBy--> aov section build, Oct 2026
AV06 --itemStatus--> open
AV06 --about--> K403
RV400__abscit02 --type--> Citation
RV400__abscit02 --location--> row K403 (RV400 at E15/16)
RV400__abscit02 --document--> SRC_DIFF
RV400__abscit02 --label--> Citation 2 for RV400 (absorption loop)
RV400__abscit02 --citationText--> P&ID differences row K403 (RV400 at E15/16)
E101 --floor--> 1
E101 --note--> Lean MEA enters at the top through NRV400; rich MEA leaves from the sump to J101a/b. The air admittance valve shown on the P&ID has been removed from the plant (DIFF, E14/15).
E101 --feedsInto--> E101_N_sump_outlet
E101 --designBasis--> Packing and column designed for 2.3-2.5 bar operation on MEA and 50 kg/h CO2 (HAZOP 10.4)
E101 --feedsInto--> E101_N_gas_outlet
E101 --pipedTo--> E101_N_sump_outlet
E101 --pipedTo--> E101_N_gas_outlet
E101 --type--> AbsorptionColumn
E101 --diameter_mm--> 230.0
E101 --tag--> E101
E101 --label--> E101 absorber
HAZOP_7_10 --concerns--> E101
TT305 --monitors--> E101
PT111 --monitors--> E101
E101_sample_5 --onColumn--> E101
E101_N_gas_outlet --onEquipment--> E101
LSLL109 --monitors--> E101
TT207 --monitors--> E101
PT403 --monitors--> E101
LI108 --monitors--> E101
E101_sample_4 --onColumn--> E101
E101_N_sump_outlet --onEquipment--> E101
FT109 --monitors--> E101
E101_sample_3 --onColumn--> E101
HAZOP_9b_05 --concerns--> E101
limit_LZAL109 --appliesTo--> E101
DI108 --monitors--> E101
E101_N_gas_inlet --feedsInto--> E101
FT304 --monitors--> E101
LT108 --monitors--> E101
K101_N2_recycle --bypasses--> E101
PT110 --monitors--> E101
E101_N_gas_inlet --pipedTo--> E101
HAZOP_5_08 --concerns--> E101
HAZOP_8_01 --concerns--> E101
HAZOP_8_06 --concerns--> E101
PI403 --monitors--> E101
AT400 --monitors--> E101
FT303 --monitors--> E101
TT205 --monitors--> E101
E101_N_base_inlet --onEquipment--> E101
aspen_v6_1_E101_performance --ofEquipment--> E101
TT206 --monitors--> E101
HAZOP_8_03 --concerns--> E101
E101_N_gas_inlet --onEquipment--> E101
E101_N_top_inlet --feedsInto--> E101
E101_sample_6 --onColumn--> E101
K402 --pipedTo--> E101
HAZOP_5_07 --concerns--> E101
AI300 --monitors--> E101
FI109 --monitors--> E101
FI108 --monitors--> E101
aspen_v3_vent_gas --ofEquipment--> E101
AT300 --monitors--> E101
E101_N_top_inlet --pipedTo--> E101
aspen_v6_1_feed_gas --ofEquipment--> E101
limit_PSHH117_set --appliesTo--> E101
TT109 --monitors--> E101
TT412 --monitors--> E101
HAZOP_10_03 --concerns--> E101
LSHH107 --monitors--> E101
E101_sample_2 --onColumn--> E101
limit_LZAH107 --appliesTo--> E101
HAZOP_5_06 --concerns--> E101
PSHH117 --monitors--> E101
TT413 --monitors--> E101
HAZOP_7_13 --concerns--> E101
TT107 --monitors--> E101
TT306 --monitors--> E101
E101_N_top_inlet --onEquipment--> E101
E101_sample_1 --onColumn--> E101
AOI10 --about--> E101
FT108 --monitors--> E101
TT411 --monitors--> E101
TT204 --monitors--> E101
aspen_v3_feed_gas --ofEquipment--> E101
HAZOP_element_10 --covers--> E101
HAZOP_8_11 --concerns--> E101
TT307 --monitors--> E101
TT308 --monitors--> E101
HAZOP_8_02 --concerns--> E101
aspen_v3_E101_performance --ofEquipment--> E101
discrepancy_K403_not_on_PID --concerns--> K403
discrepancy_K403_not_on_PID --asBuilt--> K403 knockout drum on the RV400 and RV401 discharges
discrepancy_K403_not_on_PID --drawingShows--> K403 not drawn
discrepancy_K403_not_on_PID --gridReference--> E15/16
discrepancy_K403_not_on_PID --type--> PIDDiscrepancy
```

Question: Which vessel receives the relief connections from RV400 and RV401?

## Q13

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
aspen_v6_1_block_E100 --inCase--> case_aspen_v6_1
aspen_v6_1_block_E100 --statusMessage--> RATESEP CALCULATIONS FAILED TO CONVERGE.
aspen_v6_1_block_E100 --status--> ERROR
aspen_v6_1_block_E100 --represents--> E100
aspen_v6_1_block_E100 --label--> E100 (ABB_pilot_plant_final_6_1_SA_validation)
aspen_v6_1_block_E100 --type--> AspenBlock
aspen_v6_1_block_E100 --blockId--> E100
aspen_v6_1_block_E100 --aspenModel--> RADFRAC
aspen_v6_1_stream_S15 --fromBlock--> aspen_v6_1_block_E100
aspen_v6_1_stream_S23 --fromBlock--> aspen_v6_1_block_E100
aspen_v6_1_stream_S10 --toBlock--> aspen_v6_1_block_E100
aspen_v6_1_stream_S12 --fromBlock--> aspen_v6_1_block_E100
aspen_v6_1_stream_S14 --toBlock--> aspen_v6_1_block_E100
aspen_v3_block_E100 --label--> E100 (ABB_pilot_plant_final_3)
aspen_v3_block_E100 --represents--> E100
aspen_v3_block_E100 --aspenModel--> RADFRAC
aspen_v3_block_E100 --inCase--> case_aspen_v3
aspen_v3_block_E100 --status--> WARNING
aspen_v3_block_E100 --statusMessage--> FEED PRESSURE IS LOWER THAN STAGE PRESSURE.
aspen_v3_block_E100 --type--> AspenBlock
aspen_v3_block_E100 --blockId--> E100
aspen_v3_stream_S13 --fromBlock--> aspen_v3_block_E100
aspen_v3_stream_S10 --toBlock--> aspen_v3_block_E100
aspen_v3_stream_S6 --fromBlock--> aspen_v3_block_E100
aspen_v3_stream_S14 --fromBlock--> aspen_v3_block_E100
aspen_v3_stream_S24 --toBlock--> aspen_v3_block_E100
aspen_v3_block_E101 --type--> AspenBlock
aspen_v3_block_E101 --aspenModel--> RADFRAC
aspen_v3_block_E101 --blockId--> E101
aspen_v3_block_E101 --status--> OK
aspen_v3_block_E101 --label--> E101 (ABB_pilot_plant_final_3)
aspen_v3_block_E101 --inCase--> case_aspen_v3
aspen_v3_stream_S8 --fromBlock--> aspen_v3_block_E101
aspen_v3_stream_1 --toBlock--> aspen_v3_block_E101
aspen_v3_stream_2 --toBlock--> aspen_v3_block_E101
aspen_v3_stream_4 --fromBlock--> aspen_v3_block_E101
E100 --floor--> 1
E100 --hasStage--> E100_stage_12
E100 --diameter_mm--> 264.62
E100 --tag--> E100
E100 --label--> E100 stripper (desorber)
E100 --hasStage--> E100_stage_08
E100 --hasStage--> E100_stage_01
E100 --hasStage--> E100_stage_04
E100 --feedsInto--> E100_N_overhead
E100 --hasStage--> E100_stage_07
E100 --pipedTo--> E100_N_overhead
E100 --note--> Chimney tray below the bottom packed bed separates the draw-off section (stage 11) from the sump (stage 12).
E100 --hasStage--> E100_stage_02
E100 --hasStage--> E100_stage_09
E100 --feedsInto--> E100_N_sump_outlet
E100 --hasStage--> E100_stage_06
E100 --feedsInto--> E100_N_drawoff
E100 --pipedTo--> E100_N_sump_outlet
E100 --hasStage--> E100_stage_05
E100 --hasStage--> E100_stage_11
E100 --hasStage--> E100_stage_10
E100 --designBasis--> Designed for sub-atmospheric pressure (vacuum), per HAZOP element 11 item 10. Design pressure value not documented.
E100 --hasStage--> E100_stage_03
E100 --pipedTo--> E100_N_drawoff
E100 --type--> StrippingColumn
TT200 --monitors--> E100
PI401 --monitors--> E100
TT401 --monitors--> E100
PROC_reboiler_heating_step_06 --operatesOn--> E100
HAZOP_13_13 --concerns--> E100
HAZOP_11_13 --concerns--> E100
LT101 --monitors--> E100
E100_N_sump_outlet --onEquipment--> E100
LSLL102 --monitors--> E100
HAZOP_11_12 --concerns--> E100
OI06 --about--> E100
LSHH100 --monitors--> E100
aspen_v6_1_E100_performance --ofEquipment--> E100
E100_N_overhead --onEquipment--> E100
TT302 --monitors--> E100
HAZOP_7_10 --concerns--> E100
HAZOP_6_07 --concerns--> E100
HAZOP_11_15 --concerns--> E100
E100_N_top_inlet --feedsInto--> E100
PT402 --monitors--> E100
PT401 --monitors--> E100
E100_N_drawoff --onEquipment--> E100
E100_N_side_inlet --onEquipment--> E100
limit_LT101_operating_window --appliesTo--> E100
limit_LZAH100 --appliesTo--> E100
HAZOP_9b_05 --concerns--> E100
RV401 --protects--> E100
E100_N_top_inlet --pipedTo--> E100
E100_N_top_inlet --onEquipment--> E100
HAZOP_13_12 --concerns--> E100
aspen_v3_E100_performance --ofEquipment--> E100
TT301 --monitors--> E100
TT400 --monitors--> E100
HAZOP_7_15 --concerns--> E100
HAZOP_element_11 --covers--> E100
limit_LT101_low_alarm --appliesTo--> E100
TT303 --monitors--> E100
OI11 --about--> E100
limit_PSHH116_set --appliesTo--> E100
HAZOP_13_11 --concerns--> E100
E100_N_reboiler_return --feedsInto--> E100
limit_PSHH400_set --appliesTo--> E100
OI03 --about--> E100
TT103 --monitors--> E100
PSHH400 --monitors--> E100
E100_N_reboiler_return --pipedTo--> E100
HAZOP_8_01 --concerns--> E100
PT102 --monitors--> E100
PSHH116 --monitors--> E100
TT203 --monitors--> E100
limit_LZAL102 --appliesTo--> E100
TT201 --monitors--> E100
HAZOP_6_08 --concerns--> E100
TT300 --monitors--> E100
HAZOP_11_01 --concerns--> E100
E100_N_reboiler_return --onEquipment--> E100
TT202 --monitors--> E100
aspen_v6_1_block_E101 --type--> AspenBlock
aspen_v6_1_block_E101 --aspenModel--> RADFRAC
aspen_v6_1_block_E101 --label--> E101 (ABB_pilot_plant_final_6_1_SA_validation)
aspen_v6_1_block_E101 --blockId--> E101
aspen_v6_1_block_E101 --status--> OK
aspen_v6_1_block_E101 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S8 --fromBlock--> aspen_v6_1_block_E101
aspen_v6_1_stream_2 --toBlock--> aspen_v6_1_block_E101
aspen_v6_1_stream_1 --toBlock--> aspen_v6_1_block_E101
aspen_v6_1_stream_4 --fromBlock--> aspen_v6_1_block_E101
E101 --pipedTo--> RV400
E101 --floor--> 1
E101 --note--> Lean MEA enters at the top through NRV400; rich MEA leaves from the sump to J101a/b. The air admittance valve shown on the P&ID has been removed from the plant (DIFF, E14/15).
E101 --feedsInto--> E101_N_sump_outlet
E101 --designBasis--> Packing and column designed for 2.3-2.5 bar operation on MEA and 50 kg/h CO2 (HAZOP 10.4)
E101 --feedsInto--> E101_N_gas_outlet
E101 --pipedTo--> E101_N_sump_outlet
E101 --pipedTo--> E101_N_gas_outlet
E101 --type--> AbsorptionColumn
E101 --diameter_mm--> 230.0
E101 --tag--> E101
E101 --label--> E101 absorber
HAZOP_7_10 --concerns--> E101
TT305 --monitors--> E101
PT111 --monitors--> E101
E101_sample_5 --onColumn--> E101
E101_N_gas_outlet --onEquipment--> E101
LSLL109 --monitors--> E101
TT207 --monitors--> E101
PT403 --monitors--> E101
LI108 --monitors--> E101
E101_sample_4 --onColumn--> E101
```

Question: Trace the main rich MEA route from the bottom of E101 to the inlet of E100.

## Q14

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
aspen_v6_1_block_E100 --inCase--> case_aspen_v6_1
aspen_v6_1_block_E100 --statusMessage--> RATESEP CALCULATIONS FAILED TO CONVERGE.
aspen_v6_1_block_E100 --status--> ERROR
aspen_v6_1_block_E100 --represents--> E100
aspen_v6_1_block_E100 --label--> E100 (ABB_pilot_plant_final_6_1_SA_validation)
aspen_v6_1_block_E100 --type--> AspenBlock
aspen_v6_1_block_E100 --blockId--> E100
aspen_v6_1_block_E100 --aspenModel--> RADFRAC
aspen_v6_1_stream_S15 --fromBlock--> aspen_v6_1_block_E100
aspen_v6_1_stream_S23 --fromBlock--> aspen_v6_1_block_E100
aspen_v6_1_stream_S10 --toBlock--> aspen_v6_1_block_E100
aspen_v6_1_stream_S12 --fromBlock--> aspen_v6_1_block_E100
aspen_v6_1_stream_S14 --toBlock--> aspen_v6_1_block_E100
aspen_v3_block_E100 --label--> E100 (ABB_pilot_plant_final_3)
aspen_v3_block_E100 --represents--> E100
aspen_v3_block_E100 --aspenModel--> RADFRAC
aspen_v3_block_E100 --inCase--> case_aspen_v3
aspen_v3_block_E100 --status--> WARNING
aspen_v3_block_E100 --statusMessage--> FEED PRESSURE IS LOWER THAN STAGE PRESSURE.
aspen_v3_block_E100 --type--> AspenBlock
aspen_v3_block_E100 --blockId--> E100
aspen_v3_stream_S13 --fromBlock--> aspen_v3_block_E100
aspen_v3_stream_S10 --toBlock--> aspen_v3_block_E100
aspen_v3_stream_S6 --fromBlock--> aspen_v3_block_E100
aspen_v3_stream_S14 --fromBlock--> aspen_v3_block_E100
aspen_v3_stream_S24 --toBlock--> aspen_v3_block_E100
aspen_v3_block_E101 --type--> AspenBlock
aspen_v3_block_E101 --aspenModel--> RADFRAC
aspen_v3_block_E101 --blockId--> E101
aspen_v3_block_E101 --status--> OK
aspen_v3_block_E101 --label--> E101 (ABB_pilot_plant_final_3)
aspen_v3_block_E101 --inCase--> case_aspen_v3
aspen_v3_stream_S8 --fromBlock--> aspen_v3_block_E101
aspen_v3_stream_1 --toBlock--> aspen_v3_block_E101
aspen_v3_stream_2 --toBlock--> aspen_v3_block_E101
aspen_v3_stream_4 --fromBlock--> aspen_v3_block_E101
E100 --floor--> 1
E100 --hasStage--> E100_stage_12
E100 --diameter_mm--> 264.62
E100 --tag--> E100
E100 --label--> E100 stripper (desorber)
E100 --hasStage--> E100_stage_08
E100 --hasStage--> E100_stage_01
E100 --hasStage--> E100_stage_04
E100 --feedsInto--> E100_N_overhead
E100 --hasStage--> E100_stage_07
E100 --pipedTo--> E100_N_overhead
E100 --note--> Chimney tray below the bottom packed bed separates the draw-off section (stage 11) from the sump (stage 12).
E100 --hasStage--> E100_stage_02
E100 --hasStage--> E100_stage_09
E100 --feedsInto--> E100_N_sump_outlet
E100 --hasStage--> E100_stage_06
E100 --feedsInto--> E100_N_drawoff
E100 --pipedTo--> E100_N_sump_outlet
E100 --hasStage--> E100_stage_05
E100 --hasStage--> E100_stage_11
E100 --hasStage--> E100_stage_10
E100 --designBasis--> Designed for sub-atmospheric pressure (vacuum), per HAZOP element 11 item 10. Design pressure value not documented.
E100 --hasStage--> E100_stage_03
E100 --pipedTo--> E100_N_drawoff
E100 --type--> StrippingColumn
TT200 --monitors--> E100
PI401 --monitors--> E100
TT401 --monitors--> E100
PROC_reboiler_heating_step_06 --operatesOn--> E100
HAZOP_13_13 --concerns--> E100
HAZOP_11_13 --concerns--> E100
LT101 --monitors--> E100
E100_N_sump_outlet --onEquipment--> E100
LSLL102 --monitors--> E100
HAZOP_11_12 --concerns--> E100
OI06 --about--> E100
LSHH100 --monitors--> E100
aspen_v6_1_E100_performance --ofEquipment--> E100
E100_N_overhead --onEquipment--> E100
TT302 --monitors--> E100
HAZOP_7_10 --concerns--> E100
HAZOP_6_07 --concerns--> E100
HAZOP_11_15 --concerns--> E100
E100_N_top_inlet --feedsInto--> E100
PT402 --monitors--> E100
PT401 --monitors--> E100
E100_N_drawoff --onEquipment--> E100
E100_N_side_inlet --onEquipment--> E100
limit_LT101_operating_window --appliesTo--> E100
limit_LZAH100 --appliesTo--> E100
HAZOP_9b_05 --concerns--> E100
RV401 --protects--> E100
E100_N_top_inlet --pipedTo--> E100
E100_N_top_inlet --onEquipment--> E100
HAZOP_13_12 --concerns--> E100
aspen_v3_E100_performance --ofEquipment--> E100
TT301 --monitors--> E100
TT400 --monitors--> E100
HAZOP_7_15 --concerns--> E100
HAZOP_element_11 --covers--> E100
limit_LT101_low_alarm --appliesTo--> E100
TT303 --monitors--> E100
OI11 --about--> E100
limit_PSHH116_set --appliesTo--> E100
HAZOP_13_11 --concerns--> E100
E100_N_reboiler_return --feedsInto--> E100
limit_PSHH400_set --appliesTo--> E100
OI03 --about--> E100
TT103 --monitors--> E100
PSHH400 --monitors--> E100
E100_N_reboiler_return --pipedTo--> E100
HAZOP_8_01 --concerns--> E100
PT102 --monitors--> E100
PSHH116 --monitors--> E100
TT203 --monitors--> E100
limit_LZAL102 --appliesTo--> E100
TT201 --monitors--> E100
HAZOP_6_08 --concerns--> E100
TT300 --monitors--> E100
HAZOP_11_01 --concerns--> E100
E100_N_reboiler_return --onEquipment--> E100
TT202 --monitors--> E100
aspen_v6_1_block_E101 --type--> AspenBlock
aspen_v6_1_block_E101 --aspenModel--> RADFRAC
aspen_v6_1_block_E101 --label--> E101 (ABB_pilot_plant_final_6_1_SA_validation)
aspen_v6_1_block_E101 --blockId--> E101
aspen_v6_1_block_E101 --status--> OK
aspen_v6_1_block_E101 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S8 --fromBlock--> aspen_v6_1_block_E101
aspen_v6_1_stream_2 --toBlock--> aspen_v6_1_block_E101
aspen_v6_1_stream_1 --toBlock--> aspen_v6_1_block_E101
aspen_v6_1_stream_4 --fromBlock--> aspen_v6_1_block_E101
E101 --pipedTo--> RV400
E101 --floor--> 1
E101 --note--> Lean MEA enters at the top through NRV400; rich MEA leaves from the sump to J101a/b. The air admittance valve shown on the P&ID has been removed from the plant (DIFF, E14/15).
E101 --feedsInto--> E101_N_sump_outlet
E101 --designBasis--> Packing and column designed for 2.3-2.5 bar operation on MEA and 50 kg/h CO2 (HAZOP 10.4)
E101 --feedsInto--> E101_N_gas_outlet
E101 --pipedTo--> E101_N_sump_outlet
E101 --pipedTo--> E101_N_gas_outlet
E101 --type--> AbsorptionColumn
E101 --diameter_mm--> 230.0
E101 --tag--> E101
E101 --label--> E101 absorber
HAZOP_7_10 --concerns--> E101
TT305 --monitors--> E101
PT111 --monitors--> E101
E101_sample_5 --onColumn--> E101
E101_N_gas_outlet --onEquipment--> E101
LSLL109 --monitors--> E101
TT207 --monitors--> E101
PT403 --monitors--> E101
LI108 --monitors--> E101
E101_sample_4 --onColumn--> E101
```

Question: Trace the lean MEA circulation route from E100 back to E101, identifying the main heat-transfer equipment and pump.

## Q15

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
aspen_v6_1_block_C100 --represents--> C100
aspen_v6_1_block_C100 --statusMessage--> TEMPERATURE CROSSOVER DETECTED
aspen_v6_1_block_C100 --inCase--> case_aspen_v6_1
aspen_v6_1_block_C100 --status--> WARNING
aspen_v6_1_block_C100 --aspenModel--> HEATX
aspen_v6_1_block_C100 --type--> AspenBlock
aspen_v6_1_block_C100 --label--> C100 (ABB_pilot_plant_final_6_1_SA_validation)
aspen_v6_1_block_C100 --blockId--> C100
aspen_v6_1_stream_S2 --fromBlock--> aspen_v6_1_block_C100
aspen_v6_1_stream_S3BACKUP --toBlock--> aspen_v6_1_block_C100
aspen_v6_1_stream_S8 --toBlock--> aspen_v6_1_block_C100
aspen_v6_1_stream_S27 --fromBlock--> aspen_v6_1_block_C100
C100 --source--> SUMMARY p.106; REPORT section 3
C100 --note--> Hot side carries lean MEA from E100. In the stripping loop the rich (cold) side has no flow from the absorber. REPORT puts C100 efficiency at about 95 %.
C100 --floor--> 1
C100 --pipedTo--> SDV152
C100 --tag--> C100
C100 --type--> LeanRichExchanger
C100 --pipedTo--> V113a
C100 --feedsInto--> V113a
C100 --label--> C100 lean/rich interchanger (gasketed plate heat exchanger)
HAZOP_8_02 --concerns--> C100
HAZOP_7_11 --concerns--> C100
TT104 --monitors--> C100
V112 --pipedTo--> C100
HAZOP_element_8 --covers--> C100
V112 --feedsInto--> C100
PT103 --monitors--> C100
V151 --pipedTo--> C100
aspen_v3_block_C100 --represents--> C100
aspen_v6_1_C100_performance --ofEquipment--> C100
HAZOP_8_09 --concerns--> C100
TE105 --monitors--> C100
HAZOP_element_7 --covers--> C100
TT113 --monitors--> C100
aspen_v3_C100_performance --ofEquipment--> C100
TT112 --monitors--> C100
aspen_v3_block_C100 --status--> OK
aspen_v3_block_C100 --inCase--> case_aspen_v3
aspen_v3_block_C100 --type--> AspenBlock
aspen_v3_block_C100 --label--> C100 (ABB_pilot_plant_final_3)
aspen_v3_block_C100 --aspenModel--> HEATX
aspen_v3_block_C100 --blockId--> C100
aspen_v3_stream_S15 --fromBlock--> aspen_v3_block_C100
aspen_v3_stream_S3 --toBlock--> aspen_v3_block_C100
aspen_v3_stream_S8 --toBlock--> aspen_v3_block_C100
aspen_v3_stream_S2 --fromBlock--> aspen_v3_block_C100
V151 --type--> ManualValve
V151 --normalPosition--> open
V151 --gridReference--> M9
V151 --floor--> 1
V151 --tag--> V151
V151 --label--> V151
V151 --note--> On the rich line from FT108 to the C100 cold side. Other REPORT tables give grid N9 or N8.
HAZOP_element_8 --covers--> V151
FigureOfEight_setting_V151 --valve--> V151
FT108 --pipedTo--> V151
PROC_figure_of_eight_lineup_step_01 --operatesOn--> V151
HAZOP_8_02 --concerns--> LSLL109
HAZOP_8_02 --consequence--> E101 empties into E101
HAZOP_8_02 --label--> HAZOP 8.2
HAZOP_8_02 --safeguard--> See action re flow across C100.  Plant shutdown on LZAL 109
HAZOP_8_02 --guideword--> MORE
HAZOP_8_02 --itemNumber--> 2
HAZOP_8_02 --type--> HazopDeviation
HAZOP_8_02 --cause--> Faulty pump control
HAZOP_8_02 --inElement--> HAZOP_element_8
HAZOP_8_02 --parameter--> FLOW
HAZOP_8_02 --concerns--> E101
case_aspen_v6_1 --converged--> false
case_aspen_v6_1 --representsMode--> FigureOfEight
case_aspen_v6_1 --savedOn--> Thu Feb 27 15:14:32 2025
case_aspen_v6_1 --recommendedForUse--> false
case_aspen_v6_1 --aspenFile--> ABB_pilot_plant_final_6_1_SA_validation.apwz
case_aspen_v6_1 --label--> ABB_pilot_plant_final_6_1_SA_validation
case_aspen_v6_1 --aspenVersion--> 37.0
case_aspen_v6_1 --note--> Rescaled to pilot conditions with a sensitivity study for validation. Saved results did not converge: E100 RateSep failed, H100 invalid input, C100 temperature crossover, recycle opened at S3BACKUP.
case_aspen_v6_1 --type--> SimulationCase
aspen_v6_1_block_E100 --inCase--> case_aspen_v6_1
aspen_v6_1_block_C400COND --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S21 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_PURGE --inCase--> case_aspen_v6_1
aspen_v6_1_E100_stage_02 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S4 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S17 --inCase--> case_aspen_v6_1
aspen_v6_1_block_H200A --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S8 --inCase--> case_aspen_v6_1
aspen_v6_1_E100_stage_08 --inCase--> case_aspen_v6_1
aspen_v6_1_block_MIXER1 --inCase--> case_aspen_v6_1
aspen_v6_1_E100_stage_06 --inCase--> case_aspen_v6_1
aspen_v6_1_E100_stage_11 --inCase--> case_aspen_v6_1
aspen_v6_1_E100_performance --inCase--> case_aspen_v6_1
aspen_v6_1_block_C400 --inCase--> case_aspen_v6_1
aspen_v6_1_H100_performance --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S1 --inCase--> case_aspen_v6_1
aspen_v6_1_block_B2 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S16 --inCase--> case_aspen_v6_1
aspen_v6_1_H200a_performance --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S27 --inCase--> case_aspen_v6_1
aspen_v6_1_H200b_performance --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S13 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S12 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S2 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S10 --inCase--> case_aspen_v6_1
aspen_v6_1_block_C200 --inCase--> case_aspen_v6_1
aspen_v6_1_E100_stage_04 --inCase--> case_aspen_v6_1
aspen_v6_1_block_SPLITER1 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_1 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S25 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_2 --inCase--> case_aspen_v6_1
aspen_v6_1_block_E101 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S15 --inCase--> case_aspen_v6_1
aspen_v6_1_C200_performance --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S11 --inCase--> case_aspen_v6_1
aspen_v6_1_block_B1 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S26 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S5 --inCase--> case_aspen_v6_1
aspen_v6_1_E101_performance --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S23 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S31 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S14 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S28 --inCase--> case_aspen_v6_1
aspen_v6_1_E100_stage_05 --inCase--> case_aspen_v6_1
aspen_v6_1_E100_stage_09 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S7 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S3BACKUP --inCase--> case_aspen_v6_1
aspen_v6_1_C100_performance --inCase--> case_aspen_v6_1
aspen_v6_1_block_MIXER2 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_4 --inCase--> case_aspen_v6_1
aspen_v6_1_E100_stage_03 --inCase--> case_aspen_v6_1
aspen_v6_1_block_H100 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S9 --inCase--> case_aspen_v6_1
aspen_v6_1_E100_stage_07 --inCase--> case_aspen_v6_1
aspen_v6_1_E100_stage_10 --inCase--> case_aspen_v6_1
aspen_v6_1_feed_gas --inCase--> case_aspen_v6_1
aspen_v6_1_E100_stage_01 --inCase--> case_aspen_v6_1
aspen_v6_1_E100_stage_12 --inCase--> case_aspen_v6_1
aspen_v6_1_block_H200B --inCase--> case_aspen_v6_1
Route_C_side_filter_step_16_C100 --label--> Route C: side return (stage 3), through Z102 step 16: C100
Route_C_side_filter_step_16_C100 --nextStep--> Route_C_side_filter_step_18_V113a
Route_C_side_filter_step_16_C100 --stepIndex--> 16
Route_C_side_filter_step_16_C100 --stepType--> inline
Route_C_side_filter_step_16_C100 --stepItem--> C100
Route_C_side_filter_step_16_C100 --type--> LoopStep
Route_C_side_filter_step_13_V112 --nextStep--> Route_C_side_filter_step_16_C100
C100__cit01 --location--> interchanger C100, grid M8 to M9
C100__cit01 --type--> Citation
C100__cit01 --label--> Citation 1 for C100
C100__cit01 --document--> SRC_PID
C100__cit01 --citationText--> P&ID interchanger C100, grid M8 to M9
```

Question: Which process streams pass through the two sides of C100, and where do those streams originate?

## Q16

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
C200 --note--> Cools lean MEA before the absorber; cooling water flow set by FIC201 (cascade from TIC210).
C200 --type--> TrimCooler
C200 --feedsInto--> NRV400
C200 --floor--> 2
C200 --tag--> C200
C200 --label--> C200 lean MEA trim cooler (water cooled)
C200 --pipedTo--> NRV400
HAZOP_7_12 --concerns--> C200
HAZOP_10_07 --concerns--> C200
N200_bypass --toItem--> C200
TT209 --monitors--> C200
V212 --pipedTo--> C200
TI210 --monitors--> C200
V213 --feedsInto--> C200
aspen_v6_1_C200_performance --ofEquipment--> C200
TT208 --monitors--> C200
V213 --pipedTo--> C200
FI201 --monitors--> C200
FT201 --monitors--> C200
C200_N_cw_in --onEquipment--> C200
HAZOP_element_7 --covers--> C200
FI200 --monitors--> C200
aspen_v3_C200_performance --ofEquipment--> C200
TT210 --monitors--> C200
C200_N_cw_out --onEquipment--> C200
aspen_v3_block_C200 --label--> C200 (ABB_pilot_plant_final_3)
aspen_v3_block_C200 --status--> OK
aspen_v3_block_C200 --inCase--> case_aspen_v3
aspen_v3_block_C200 --blockId--> C200
aspen_v3_block_C200 --aspenModel--> HEATER
aspen_v3_block_C200 --type--> AspenBlock
aspen_v3_stream_S2 --toBlock--> aspen_v3_block_C200
aspen_v3_stream_2 --fromBlock--> aspen_v3_block_C200
C200_N_cw_out__utlcit01 --type--> Citation
C200_N_cw_out__utlcit01 --label--> Citation 1 for C200_N_cw_out (utl)
C200_N_cw_out__utlcit01 --document--> SRC_PID
C200_N_cw_out__utlcit01 --citationText--> P&ID C200
C200_N_cw_out__utlcit01 --location--> C200
C200_N_cw_in__utlcit01 --label--> Citation 1 for C200_N_cw_in (utl)
C200_N_cw_in__utlcit01 --type--> Citation
C200_N_cw_in__utlcit01 --document--> SRC_PID
C200_N_cw_in__utlcit01 --citationText--> P&ID C200
C200_N_cw_in__utlcit01 --location--> C200
aspen_v6_1_block_C200 --blockId--> C200
aspen_v6_1_block_C200 --type--> AspenBlock
aspen_v6_1_block_C200 --label--> C200 (ABB_pilot_plant_final_6_1_SA_validation)
aspen_v6_1_block_C200 --inCase--> case_aspen_v6_1
aspen_v6_1_block_C200 --status--> OK
aspen_v6_1_block_C200 --aspenModel--> HEATER
aspen_v6_1_stream_2 --fromBlock--> aspen_v6_1_block_C200
aspen_v6_1_stream_S2 --toBlock--> aspen_v6_1_block_C200
C200__abscit02 --label--> Citation 2 for C200 (absorption loop)
C200__abscit02 --type--> Citation
C200__abscit02 --document--> SRC_REPORT
C200__abscit02 --location--> section 3 (C200 is a trim cooler, second floor)
C200__abscit02 --citationText--> Pilot Plant Report section 3 (C200 is a trim cooler, second floor)
C200__abscit03 --location--> block C200
C200__abscit03 --type--> Citation
C200__abscit03 --citationText--> Aspen v3 block C200
C200__abscit03 --document--> SRC_ASPEN_V3
C200__abscit03 --label--> Citation 3 for C200 (absorption loop)
HAZOP_11_07 --label--> HAZOP 11.7
HAZOP_11_07 --cause--> Any failure of the system pressure control
HAZOP_11_07 --guideword--> HIGHER
HAZOP_11_07 --type--> HazopDeviation
HAZOP_11_07 --consequence--> Increased degradation of MEA (slight)
HAZOP_11_07 --itemNumber--> 7
HAZOP_11_07 --inElement--> HAZOP_element_11
HAZOP_11_07 --parameter--> TEMP.
HAZOP_11_07 --actionTaken--> TAH added
HAZOP_11_07 --recommendedAction--> Consider TAH on process outlet from C200
TIC210 --controls--> FCV200
TIC210 --label--> C200 outlet temperature controller (cascade master)
TIC210 --tag--> TIC210
TIC210 --type--> Controller
CL_C200_temperature --hasController--> TIC210
TT215 --signalType--> Fieldbus
TT215 --measuredVariable--> temperature near C200 (position to trace, FI05)
TT215 --floor--> 2
TT215 --sensorType--> K-type thermocouple
TT215 --gridReference--> J13
TT215 --type--> TemperatureInstrument
TT215 --label--> TT215
TT215 --tag--> TT215
AOI08 --foundBy--> absorption loop build, Oct 2026
AOI08 --itemStatus--> open
AOI08 --resolvedBy--> Site check
AOI08 --about--> FCV201
AOI08 --description--> FCV200 and FCV201 are both on the C200 cooling water line; FIC201 drives FCV200, but the role of FCV201 is not documented
AOI08 --about--> FCV200
AOI08 --type--> OpenItem
AOI08 --label--> AOI08: FCV200 and FCV201 are both on the C200 cooling water line; FIC201 drives FCV200, but the role of FCV201 is not documented
aspen_v3_stream_2 --pressure_bar--> 2.0
aspen_v3_stream_2 --moleFlow_kmol_h--> 22.9975
aspen_v3_stream_2 --massFlow_kg_h--> 552.2604
aspen_v3_stream_2 --streamId--> 2
aspen_v3_stream_2 --label--> 2 (ABB_pilot_plant_final_3)
aspen_v3_stream_2 --inCase--> case_aspen_v3
aspen_v3_stream_2 --apparentCO2_kg_h--> 31.84518
aspen_v3_stream_2 --meaMassFraction--> 0.2725138
aspen_v3_stream_2 --waterFlow_kg_h--> 369.31
aspen_v3_stream_2 --vapourFraction--> 0.0
aspen_v3_stream_2 --type--> StreamState
aspen_v3_stream_2 --toBlock--> aspen_v3_block_E101
aspen_v3_stream_2 --phase--> LIQUID
aspen_v3_stream_2 --enthalpyFlow_W--> -1905236.0
aspen_v3_stream_2 --temperature_C--> 40.0
aspen_v3_stream_2 --co2Loading_mol_mol--> 0.2936858
CL_C200_cooling_water --type--> ControlLoop
CL_C200_cooling_water --hasController--> FIC201
CL_C200_cooling_water --manipulatedVariable--> FCV200 opening
CL_C200_cooling_water --label--> Cooling water flow to C200 (cascade slave)
CL_C200_cooling_water --hasFinalElement--> FCV200
CL_C200_cooling_water --hasSensor--> FT201
CL_C200_cooling_water --controlledVariable--> Cooling water flowrate to C200
CL_C200_temperature --cascadeMasterOf--> CL_C200_cooling_water
aspen_v6_1_C200_performance --label--> C200 performance (ABB_pilot_plant_final_6_1_SA_validation)
aspen_v6_1_C200_performance --duty_kW--> 7.236044
aspen_v6_1_C200_performance --derivedBy--> build_absorption_loop.py
aspen_v6_1_C200_performance --hotInlet_C--> 70.52478
aspen_v6_1_C200_performance --note--> Lean MEA side only; Aspen models C200 as a heater block, so the cooling water side is not simulated.
aspen_v6_1_C200_performance --inCase--> case_aspen_v6_1
aspen_v6_1_C200_performance --hotOutlet_C--> 45.0
aspen_v6_1_C200_performance --type--> HeatExchangerPerformance
TT209 --sensorType--> PRT
TT209 --label--> TT209
TT209 --gridReference--> J12
TT209 --type--> TemperatureInstrument
TT209 --measuredVariable--> lean MEA entering C200
TT209 --tag--> TT209
TT209 --signalType--> Fieldbus
TT209 --floor--> 2
discrepancy_TT208_TT209_swap --concerns--> TT209
limit_TAH_C200_outlet --type--> OperatingLimit
limit_TAH_C200_outlet --unit--> C
limit_TAH_C200_outlet --limitType--> alarm
limit_TAH_C200_outlet --label--> TAH_C200_outlet
limit_TAH_C200_outlet --valueVerified--> false
limit_TAH_C200_outlet --variable--> temperature
limit_TAH_C200_outlet --source--> HAZOP element 10, item 7 (TAH added on the C200 process outlet)
limit_TAH_C200_outlet --appliesTo--> TT210
aspen_v3_C200_performance --type--> HeatExchangerPerformance
aspen_v3_C200_performance --inCase--> case_aspen_v3
aspen_v3_C200_performance --duty_kW--> 24.13058
aspen_v3_C200_performance --hotInlet_C--> 86.0
aspen_v3_C200_performance --derivedBy--> build_absorption_loop.py
aspen_v3_C200_performance --label--> C200 performance (ABB_pilot_plant_final_3)
aspen_v3_C200_performance --hotOutlet_C--> 40.0
aspen_v3_C200_performance --note--> Lean MEA side only; Aspen models C200 as a heater block, so the cooling water side is not simulated.
aspen_v3_stream_S2 --inCase--> case_aspen_v3
```

Question: Where does lean MEA flow after leaving C200, and which transmitter measures its outlet temperature?

## Q17

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
aspen_v3_block_E100 --label--> E100 (ABB_pilot_plant_final_3)
aspen_v3_block_E100 --represents--> E100
aspen_v3_block_E100 --aspenModel--> RADFRAC
aspen_v3_block_E100 --inCase--> case_aspen_v3
aspen_v3_block_E100 --status--> WARNING
aspen_v3_block_E100 --statusMessage--> FEED PRESSURE IS LOWER THAN STAGE PRESSURE.
aspen_v3_block_E100 --type--> AspenBlock
aspen_v3_block_E100 --blockId--> E100
aspen_v3_stream_S13 --fromBlock--> aspen_v3_block_E100
aspen_v3_stream_S10 --toBlock--> aspen_v3_block_E100
aspen_v3_stream_S6 --fromBlock--> aspen_v3_block_E100
aspen_v3_stream_S14 --fromBlock--> aspen_v3_block_E100
aspen_v3_stream_S24 --toBlock--> aspen_v3_block_E100
aspen_v6_1_block_E100 --inCase--> case_aspen_v6_1
aspen_v6_1_block_E100 --statusMessage--> RATESEP CALCULATIONS FAILED TO CONVERGE.
aspen_v6_1_block_E100 --status--> ERROR
aspen_v6_1_block_E100 --represents--> E100
aspen_v6_1_block_E100 --label--> E100 (ABB_pilot_plant_final_6_1_SA_validation)
aspen_v6_1_block_E100 --type--> AspenBlock
aspen_v6_1_block_E100 --blockId--> E100
aspen_v6_1_block_E100 --aspenModel--> RADFRAC
aspen_v6_1_stream_S15 --fromBlock--> aspen_v6_1_block_E100
aspen_v6_1_stream_S23 --fromBlock--> aspen_v6_1_block_E100
aspen_v6_1_stream_S10 --toBlock--> aspen_v6_1_block_E100
aspen_v6_1_stream_S12 --fromBlock--> aspen_v6_1_block_E100
aspen_v6_1_stream_S14 --toBlock--> aspen_v6_1_block_E100
E100 --floor--> 1
E100 --hasStage--> E100_stage_12
E100 --diameter_mm--> 264.62
E100 --tag--> E100
E100 --label--> E100 stripper (desorber)
E100 --hasStage--> E100_stage_08
E100 --hasStage--> E100_stage_01
E100 --hasStage--> E100_stage_04
E100 --feedsInto--> E100_N_overhead
E100 --hasStage--> E100_stage_07
E100 --pipedTo--> E100_N_overhead
E100 --note--> Chimney tray below the bottom packed bed separates the draw-off section (stage 11) from the sump (stage 12).
E100 --hasStage--> E100_stage_02
E100 --hasStage--> E100_stage_09
E100 --feedsInto--> E100_N_sump_outlet
E100 --hasStage--> E100_stage_06
E100 --feedsInto--> E100_N_drawoff
E100 --pipedTo--> E100_N_sump_outlet
E100 --hasStage--> E100_stage_05
E100 --hasStage--> E100_stage_11
E100 --hasStage--> E100_stage_10
E100 --designBasis--> Designed for sub-atmospheric pressure (vacuum), per HAZOP element 11 item 10. Design pressure value not documented.
E100 --hasStage--> E100_stage_03
E100 --pipedTo--> E100_N_drawoff
E100 --type--> StrippingColumn
TT200 --monitors--> E100
PI401 --monitors--> E100
TT401 --monitors--> E100
PROC_reboiler_heating_step_06 --operatesOn--> E100
HAZOP_13_13 --concerns--> E100
HAZOP_11_13 --concerns--> E100
LT101 --monitors--> E100
E100_N_sump_outlet --onEquipment--> E100
LSLL102 --monitors--> E100
HAZOP_11_12 --concerns--> E100
OI06 --about--> E100
LSHH100 --monitors--> E100
aspen_v6_1_E100_performance --ofEquipment--> E100
E100_N_overhead --onEquipment--> E100
TT302 --monitors--> E100
HAZOP_7_10 --concerns--> E100
HAZOP_6_07 --concerns--> E100
HAZOP_11_15 --concerns--> E100
E100_N_top_inlet --feedsInto--> E100
PT402 --monitors--> E100
PT401 --monitors--> E100
E100_N_drawoff --onEquipment--> E100
E100_N_side_inlet --onEquipment--> E100
limit_LT101_operating_window --appliesTo--> E100
limit_LZAH100 --appliesTo--> E100
HAZOP_9b_05 --concerns--> E100
RV401 --protects--> E100
E100_N_top_inlet --pipedTo--> E100
E100_N_top_inlet --onEquipment--> E100
HAZOP_13_12 --concerns--> E100
aspen_v3_E100_performance --ofEquipment--> E100
TT301 --monitors--> E100
TT400 --monitors--> E100
HAZOP_7_15 --concerns--> E100
HAZOP_element_11 --covers--> E100
limit_LT101_low_alarm --appliesTo--> E100
TT303 --monitors--> E100
OI11 --about--> E100
limit_PSHH116_set --appliesTo--> E100
HAZOP_13_11 --concerns--> E100
E100_N_reboiler_return --feedsInto--> E100
limit_PSHH400_set --appliesTo--> E100
OI03 --about--> E100
TT103 --monitors--> E100
PSHH400 --monitors--> E100
E100_N_reboiler_return --pipedTo--> E100
HAZOP_8_01 --concerns--> E100
PT102 --monitors--> E100
PSHH116 --monitors--> E100
TT203 --monitors--> E100
limit_LZAL102 --appliesTo--> E100
TT201 --monitors--> E100
HAZOP_6_08 --concerns--> E100
TT300 --monitors--> E100
HAZOP_11_01 --concerns--> E100
E100_N_reboiler_return --onEquipment--> E100
TT202 --monitors--> E100
LSHH100 --tag--> LSHH100
LSHH100 --note--> Stage mapping inferred: odd Aspen stages are the gaps between packed beds where the side instruments sit; floors match REPORT.
LSHH100 --locatedAtStage--> E100_stage_12
LSHH100 --type--> LevelInstrument
LSHH100 --measuredVariable--> level high-high switch
LSHH100 --floor--> 1
LSHH100 --label--> LSHH100
IL_E100_level_HH --initiatedBy--> LSHH100
PT402 --tag--> PT402
PT402 --monitors--> K401
PT402 --measuredVariable--> pressure after K401
PT402 --gridReference--> C16
PT402 --type--> PressureInstrument
PT402 --signalType--> Fieldbus
PT402 --floor--> 4
PT402 --sensorType--> gauge pressure transmitter
PT402 --label--> PT402
HAZOP_12_02 --concerns--> PT402
HAZOP_element_12 --covers--> PT402
CL_E100_pressure --hasSensor--> PT402
NRV106 --tag--> NRV106
NRV106 --valveType--> check
NRV106 --floor--> 1
NRV106 --note--> Near V112 at the E100 sump outlet. FI07
NRV106 --type--> CheckValve
NRV106 --label--> NRV106
NRV106 --gridReference--> M8
Route_D_side_bypass_step_38_E100 --stepIndex--> 38
Route_D_side_bypass_step_38_E100 --label--> Route D: side return (stage 3), Z102 bypassed step 38: E100
Route_D_side_bypass_step_38_E100 --stepType--> inline
Route_D_side_bypass_step_38_E100 --stepItem--> E100
Route_D_side_bypass_step_38_E100 --type--> LoopStep
Route_D_side_bypass_step_37_E100_N_side_inlet --nextStep--> Route_D_side_bypass_step_38_E100
Route_B_top_bypass_step_10_E100 --nextStep--> Route_B_top_bypass_step_11_E100_N_sump_outlet
Route_B_top_bypass_step_10_E100 --stepItem--> E100
Route_B_top_bypass_step_10_E100 --stepIndex--> 10
Route_B_top_bypass_step_10_E100 --stepType--> inline
Route_B_top_bypass_step_10_E100 --type--> LoopStep
Route_B_top_bypass_step_10_E100 --label--> Route B: top return (stage 1), Z102 bypassed step 10: E100
Route_B_top_bypass_step_09_E100_N_reboiler_return --nextStep--> Route_B_top_bypass_step_10_E100
aspen_v3_stream_S10 --temperature_C--> 89.99877
aspen_v3_stream_S10 --phase--> MIXED
```

Question: Trace the CO2-rich overhead stream from E100 through the condensation and gas recovery system.

## Q18

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
C400_N_cw_out__utlcit01 --location--> C400
C400_N_cw_out__utlcit01 --type--> Citation
C400_N_cw_out__utlcit01 --document--> SRC_PID
C400_N_cw_out__utlcit01 --citationText--> P&ID C400
C400_N_cw_out__utlcit01 --label--> Citation 1 for C400_N_cw_out (utl)
aspen_v3_block_C400 --inCase--> case_aspen_v3
aspen_v3_block_C400 --aspenModel--> HEATER
aspen_v3_block_C400 --type--> AspenBlock
aspen_v3_block_C400 --blockId--> C400
aspen_v3_block_C400 --status--> OK
aspen_v3_block_C400 --label--> C400 (ABB_pilot_plant_final_3)
aspen_v3_stream_S11 --fromBlock--> aspen_v3_block_C400
aspen_v3_stream_S13 --toBlock--> aspen_v3_block_C400
C400_N_cw_in__utlcit01 --type--> Citation
C400_N_cw_in__utlcit01 --document--> SRC_PID
C400_N_cw_in__utlcit01 --citationText--> P&ID C400
C400_N_cw_in__utlcit01 --label--> Citation 1 for C400_N_cw_in (utl)
C400_N_cw_in__utlcit01 --location--> C400
aspen_v6_1_block_C400 --aspenModel--> HEATER
aspen_v6_1_block_C400 --label--> C400 (ABB_pilot_plant_final_6_1_SA_validation)
aspen_v6_1_block_C400 --blockId--> C400
aspen_v6_1_block_C400 --inCase--> case_aspen_v6_1
aspen_v6_1_block_C400 --status--> OK
aspen_v6_1_block_C400 --type--> AspenBlock
aspen_v6_1_stream_S11 --fromBlock--> aspen_v6_1_block_C400
aspen_v6_1_stream_S15 --toBlock--> aspen_v6_1_block_C400
C400 --floor--> 4
C400 --pipedTo--> K401
C400 --type--> Condenser
C400 --label--> C400 overhead condenser (spiral heat exchanger)
C400 --tag--> C400
C400 --note--> Water-cooled; cooling water flow set by FIC402 on FCV401 (cascade from TIC410). Grid not in the REPORT lists (between C8 and E10 on the P&ID).
C400 --feedsInto--> K401
E100_N_overhead --pipedTo--> C400
OOI04 --about--> C400
HAZOP_12_07 --concerns--> C400
aspen_v3_C400_performance --ofEquipment--> C400
OOI06 --about--> C400
HAZOP_12_03 --concerns--> C400
FI402 --monitors--> C400
C400_N_cw_in --onEquipment--> C400
HAZOP_6_05 --concerns--> C400
HAZOP_6_01 --concerns--> C400
C400_N_cw_out --onEquipment--> C400
PT401 --monitors--> C400
HAZOP_element_12 --covers--> C400
TI410 --monitors--> C400
limit_TAH_C400_carryover --appliesTo--> C400
FI401 --monitors--> C400
FT402 --monitors--> C400
HAZOP_6_06 --concerns--> C400
E100_N_overhead --feedsInto--> C400
TT410 --monitors--> C400
E100_N_overhead --type--> Nozzle
E100_N_overhead --onEquipment--> E100
E100_N_overhead --label--> E100 vapour outlet at the top of the column
E100 --feedsInto--> E100_N_overhead
E100 --pipedTo--> E100_N_overhead
C400__ovhcit01 --label--> Citation 1 for C400 (ovh)
C400__ovhcit01 --type--> Citation
C400__ovhcit01 --location--> overhead line after PT401, top of the drawing
C400__ovhcit01 --document--> SRC_PID
C400__ovhcit01 --citationText--> P&ID overhead line after PT401, top of the drawing
PCV415 --pipedTo--> FCV401
PCV415 --normalPosition--> open
PCV415 --note--> Pressure regulator on the C400 cooling water stream (UT09). The valve list gives floor 3.
PCV415 --floor--> 4
PCV415 --type--> PressureControlValve
PCV415 --gridReference--> C14
PCV415 --tag--> PCV415
PCV415 --feedsInto--> FCV401
PCV415 --valveType--> pressure control
PCV415 --label--> PCV415
UT09 --about--> PCV415
V405 --feedsInto--> PCV415
V405 --pipedTo--> PCV415
TIC410 --type--> Controller
TIC410 --tag--> TIC410
TIC410 --label--> C400 gas outlet temperature controller (cascade master)
TIC410 --controls--> FCV401
CL_C400_temperature --hasController--> TIC410
OOI04 --description--> Aspen returns the reflux to the rich feed before the heaters (MIXER2), but on the P&ID it joins after them at V403/V402
OOI04 --foundBy--> ovh section build, Oct 2026
OOI04 --about--> J300
OOI04 --type--> OpenItem
OOI04 --resolvedBy--> Note for model comparison; update the Aspen flowsheet if needed
OOI04 --itemStatus--> open
OOI04 --label--> OOI04: Aspen returns the reflux to the rich feed before the heaters (MIXER2), but on the P&ID it joins after them at V403/V402
HAZOP_6_01 --actionTaken--> Pump shutdown trip added
HAZOP_6_01 --consequence--> No flow to J103
HAZOP_6_01 --concerns--> J103
HAZOP_6_01 --inElement--> HAZOP_element_6
HAZOP_6_01 --cause--> K401 / C300 (now C400) blocked
HAZOP_6_01 --guideword--> NO
HAZOP_6_01 --label--> HAZOP 6.1
HAZOP_6_01 --recommendedAction--> Consider consequences of starving J103
HAZOP_6_01 --parameter--> FLOW
HAZOP_6_01 --type--> HazopDeviation
HAZOP_6_01 --itemNumber--> 1
HAZOP_6_01 --concerns--> K401
TT410 --signalType--> Fieldbus
TT410 --measuredVariable--> temperature of CO2 leaving C400
TT410 --floor--> 4
TT410 --label--> TT410
TT410 --sensorType--> PRT
TT410 --tag--> TT410
TT410 --gridReference--> C15
TT410 --type--> TemperatureInstrument
CL_C400_temperature --hasSensor--> TT410
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_07_J300
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_14_FT305
OverheadRefluxLoop --label--> Stripper overhead and reflux loop
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_09_RV300
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_02_PT401
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_03_C400
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_10_B300
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_08_TT310
OverheadRefluxLoop --note--> Runs whenever E100 is boiling. Vapour is condensed in C400; K401 separates the condensate (returned as reflux by J300) from the CO2-rich gas (to the CO2 return, piece 7).
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_06_LT401
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_05_K401
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_17_E100_N_top_inlet
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_01_E100_N_overhead
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_15_V403
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_00_E100
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_16_V402
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_12_V317
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_13_TT309
OverheadRefluxLoop --type--> Loop
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_04_LSHH400
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_11_PCV302
OverheadRefluxLoop --inMode--> FigureOfEight
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_18_E100
C400__ovhcit03 --citationText--> P&ID differences row LSHH400 (between C400 and K401)
C400__ovhcit03 --location--> row LSHH400 (between C400 and K401)
C400__ovhcit03 --document--> SRC_DIFF
C400__ovhcit03 --label--> Citation 3 for C400 (ovh)
C400__ovhcit03 --type--> Citation
C400_N_cw_in --pipedTo--> C400_N_cw_out
C400_N_cw_in --label--> C400 cooling water inlet
C400_N_cw_in --type--> Nozzle
C400_N_cw_in --feedsInto--> C400_N_cw_out
FT402 --pipedTo--> C400_N_cw_in
FT402 --feedsInto--> C400_N_cw_in
CL_C400_cooling_water --hasFinalElement--> FCV401
CL_C400_cooling_water --controlledVariable--> Cooling water flowrate to C400
CL_C400_cooling_water --manipulatedVariable--> FCV401 opening
CL_C400_cooling_water --label--> Cooling water flow to C400 (cascade slave)
CL_C400_cooling_water --hasController--> FIC402
CL_C400_cooling_water --hasSensor--> FT402
CL_C400_cooling_water --type--> ControlLoop
```

Question: Where does liquid recovered in the condenser system return, and which pump provides the transfer?

## Q19

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
aspen_v3_block_E101 --type--> AspenBlock
aspen_v3_block_E101 --aspenModel--> RADFRAC
aspen_v3_block_E101 --blockId--> E101
aspen_v3_block_E101 --status--> OK
aspen_v3_block_E101 --label--> E101 (ABB_pilot_plant_final_3)
aspen_v3_block_E101 --inCase--> case_aspen_v3
aspen_v3_stream_S8 --fromBlock--> aspen_v3_block_E101
aspen_v3_stream_1 --toBlock--> aspen_v3_block_E101
aspen_v3_stream_2 --toBlock--> aspen_v3_block_E101
aspen_v3_stream_4 --fromBlock--> aspen_v3_block_E101
aspen_v6_1_block_E101 --type--> AspenBlock
aspen_v6_1_block_E101 --aspenModel--> RADFRAC
aspen_v6_1_block_E101 --label--> E101 (ABB_pilot_plant_final_6_1_SA_validation)
aspen_v6_1_block_E101 --blockId--> E101
aspen_v6_1_block_E101 --status--> OK
aspen_v6_1_block_E101 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S8 --fromBlock--> aspen_v6_1_block_E101
aspen_v6_1_stream_2 --toBlock--> aspen_v6_1_block_E101
aspen_v6_1_stream_1 --toBlock--> aspen_v6_1_block_E101
aspen_v6_1_stream_4 --fromBlock--> aspen_v6_1_block_E101
E101 --pipedTo--> RV400
E101 --floor--> 1
E101 --note--> Lean MEA enters at the top through NRV400; rich MEA leaves from the sump to J101a/b. The air admittance valve shown on the P&ID has been removed from the plant (DIFF, E14/15).
E101 --feedsInto--> E101_N_sump_outlet
E101 --designBasis--> Packing and column designed for 2.3-2.5 bar operation on MEA and 50 kg/h CO2 (HAZOP 10.4)
E101 --feedsInto--> E101_N_gas_outlet
E101 --pipedTo--> E101_N_sump_outlet
E101 --pipedTo--> E101_N_gas_outlet
E101 --type--> AbsorptionColumn
E101 --diameter_mm--> 230.0
E101 --tag--> E101
E101 --label--> E101 absorber
HAZOP_7_10 --concerns--> E101
TT305 --monitors--> E101
PT111 --monitors--> E101
E101_sample_5 --onColumn--> E101
E101_N_gas_outlet --onEquipment--> E101
LSLL109 --monitors--> E101
TT207 --monitors--> E101
PT403 --monitors--> E101
LI108 --monitors--> E101
E101_sample_4 --onColumn--> E101
E101_N_sump_outlet --onEquipment--> E101
FT109 --monitors--> E101
E101_sample_3 --onColumn--> E101
HAZOP_9b_05 --concerns--> E101
limit_LZAL109 --appliesTo--> E101
DI108 --monitors--> E101
E101_N_gas_inlet --feedsInto--> E101
FT304 --monitors--> E101
LT108 --monitors--> E101
K101_N2_recycle --bypasses--> E101
PT110 --monitors--> E101
E101_N_gas_inlet --pipedTo--> E101
HAZOP_5_08 --concerns--> E101
HAZOP_8_01 --concerns--> E101
HAZOP_8_06 --concerns--> E101
PI403 --monitors--> E101
AT400 --monitors--> E101
FT303 --monitors--> E101
TT205 --monitors--> E101
E101_N_base_inlet --onEquipment--> E101
aspen_v6_1_E101_performance --ofEquipment--> E101
TT206 --monitors--> E101
HAZOP_8_03 --concerns--> E101
E101_N_gas_inlet --onEquipment--> E101
E101_N_top_inlet --feedsInto--> E101
E101_sample_6 --onColumn--> E101
K402 --pipedTo--> E101
HAZOP_5_07 --concerns--> E101
AI300 --monitors--> E101
FI109 --monitors--> E101
FI108 --monitors--> E101
aspen_v3_vent_gas --ofEquipment--> E101
AT300 --monitors--> E101
E101_N_top_inlet --pipedTo--> E101
aspen_v6_1_feed_gas --ofEquipment--> E101
limit_PSHH117_set --appliesTo--> E101
TT109 --monitors--> E101
TT412 --monitors--> E101
HAZOP_10_03 --concerns--> E101
LSHH107 --monitors--> E101
E101_sample_2 --onColumn--> E101
limit_LZAH107 --appliesTo--> E101
HAZOP_5_06 --concerns--> E101
PSHH117 --monitors--> E101
TT413 --monitors--> E101
HAZOP_7_13 --concerns--> E101
TT107 --monitors--> E101
TT306 --monitors--> E101
E101_N_top_inlet --onEquipment--> E101
E101_sample_1 --onColumn--> E101
AOI10 --about--> E101
RV400 --protects--> E101
FT108 --monitors--> E101
TT411 --monitors--> E101
TT204 --monitors--> E101
aspen_v3_feed_gas --ofEquipment--> E101
HAZOP_element_10 --covers--> E101
HAZOP_8_11 --concerns--> E101
TT307 --monitors--> E101
TT308 --monitors--> E101
HAZOP_8_02 --concerns--> E101
aspen_v3_E101_performance --ofEquipment--> E101
PCV300 --valveType--> pressure control
PCV300 --floor--> 3
PCV300 --normalPosition--> open
PCV300 --note--> Vents lean gas from the absorber to hold the E101 pressure (PIC403). Opened in the vent stream start-up (Fig F.3), closed at shutdown.
PCV300 --pipedTo--> VENT_E101
PCV300 --label--> PCV300
PCV300 --feedsInto--> VENT_E101
PCV300 --type--> PressureControlValve
PCV300 --tag--> PCV300
PCV300 --gridReference--> G18
K402 --feedsInto--> PCV300
CL_E101_pressure --hasFinalElement--> PCV300
K402 --pipedTo--> PCV300
PIC403 --controls--> PCV300
AV01 --about--> PCV300
K101 --type--> Saturator
K101 --label--> K101 gas saturator
K101 --pipedTo--> SDV170
K101 --pipedTo--> Z103
K101 --floor--> 1
K101 --feedsInto--> E101_N_gas_inlet
K101 --pipedTo--> E101_N_gas_inlet
K101 --note--> Saturates the feed gas with water before E101; temperature held by TIC121 using C106 on the recirculating water. Grid not in the REPORT lists (near L17 to L18 on the P&ID). Not modelled in Aspen (GOI09).
K101 --pipedTo--> V126
K101 --tag--> K101
DI_CARTRIDGE --feedsInto--> K101
HAZOP_4_06 --concerns--> K101
V172 --pipedTo--> K101
J102 --pipedTo--> K101
limit_LZAL_K101 --appliesTo--> K101
HAZOP_4_07 --concerns--> K101
LT104 --monitors--> K101
HAZOP_3_05 --concerns--> K101
FEED_GAS_HEADER --feedsInto--> K101
GOI09 --about--> K101
LI106 --monitors--> K101
FEED_GAS_HEADER --pipedTo--> K101
limit_LAL_K101 --appliesTo--> K101
K101_N2_recycle --fromItem--> K101
limit_LZAH_K101 --appliesTo--> K101
GOI07 --about--> K101
GOI02 --about--> K101
HAZOP_element_3 --covers--> K101
HAZOP_4_02 --concerns--> K101
TI121 --monitors--> K101
C106 --pipedTo--> K101
```

Question: What is the nitrogen return path after gas leaves the top of E101?

## Q20

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
aspen_v3_block_E101 --type--> AspenBlock
aspen_v3_block_E101 --aspenModel--> RADFRAC
aspen_v3_block_E101 --blockId--> E101
aspen_v3_block_E101 --status--> OK
aspen_v3_block_E101 --label--> E101 (ABB_pilot_plant_final_3)
aspen_v3_block_E101 --inCase--> case_aspen_v3
aspen_v3_stream_S8 --fromBlock--> aspen_v3_block_E101
aspen_v3_stream_1 --toBlock--> aspen_v3_block_E101
aspen_v3_stream_2 --toBlock--> aspen_v3_block_E101
aspen_v3_stream_4 --fromBlock--> aspen_v3_block_E101
aspen_v6_1_block_E101 --type--> AspenBlock
aspen_v6_1_block_E101 --aspenModel--> RADFRAC
aspen_v6_1_block_E101 --label--> E101 (ABB_pilot_plant_final_6_1_SA_validation)
aspen_v6_1_block_E101 --blockId--> E101
aspen_v6_1_block_E101 --status--> OK
aspen_v6_1_block_E101 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S8 --fromBlock--> aspen_v6_1_block_E101
aspen_v6_1_stream_2 --toBlock--> aspen_v6_1_block_E101
aspen_v6_1_stream_1 --toBlock--> aspen_v6_1_block_E101
aspen_v6_1_stream_4 --fromBlock--> aspen_v6_1_block_E101
E101 --pipedTo--> RV400
E101 --floor--> 1
E101 --note--> Lean MEA enters at the top through NRV400; rich MEA leaves from the sump to J101a/b. The air admittance valve shown on the P&ID has been removed from the plant (DIFF, E14/15).
E101 --feedsInto--> E101_N_sump_outlet
E101 --designBasis--> Packing and column designed for 2.3-2.5 bar operation on MEA and 50 kg/h CO2 (HAZOP 10.4)
E101 --feedsInto--> E101_N_gas_outlet
E101 --pipedTo--> E101_N_sump_outlet
E101 --pipedTo--> E101_N_gas_outlet
E101 --type--> AbsorptionColumn
E101 --diameter_mm--> 230.0
E101 --tag--> E101
E101 --label--> E101 absorber
HAZOP_7_10 --concerns--> E101
TT305 --monitors--> E101
PT111 --monitors--> E101
E101_sample_5 --onColumn--> E101
E101_N_gas_outlet --onEquipment--> E101
LSLL109 --monitors--> E101
TT207 --monitors--> E101
PT403 --monitors--> E101
LI108 --monitors--> E101
E101_sample_4 --onColumn--> E101
E101_N_sump_outlet --onEquipment--> E101
FT109 --monitors--> E101
E101_sample_3 --onColumn--> E101
HAZOP_9b_05 --concerns--> E101
limit_LZAL109 --appliesTo--> E101
DI108 --monitors--> E101
E101_N_gas_inlet --feedsInto--> E101
FT304 --monitors--> E101
LT108 --monitors--> E101
K101_N2_recycle --bypasses--> E101
PT110 --monitors--> E101
E101_N_gas_inlet --pipedTo--> E101
HAZOP_5_08 --concerns--> E101
HAZOP_8_01 --concerns--> E101
HAZOP_8_06 --concerns--> E101
PI403 --monitors--> E101
AT400 --monitors--> E101
FT303 --monitors--> E101
TT205 --monitors--> E101
E101_N_base_inlet --onEquipment--> E101
aspen_v6_1_E101_performance --ofEquipment--> E101
TT206 --monitors--> E101
HAZOP_8_03 --concerns--> E101
E101_N_gas_inlet --onEquipment--> E101
E101_N_top_inlet --feedsInto--> E101
E101_sample_6 --onColumn--> E101
K402 --pipedTo--> E101
HAZOP_5_07 --concerns--> E101
AI300 --monitors--> E101
FI109 --monitors--> E101
FI108 --monitors--> E101
aspen_v3_vent_gas --ofEquipment--> E101
AT300 --monitors--> E101
E101_N_top_inlet --pipedTo--> E101
aspen_v6_1_feed_gas --ofEquipment--> E101
limit_PSHH117_set --appliesTo--> E101
TT109 --monitors--> E101
TT412 --monitors--> E101
HAZOP_10_03 --concerns--> E101
LSHH107 --monitors--> E101
E101_sample_2 --onColumn--> E101
limit_LZAH107 --appliesTo--> E101
HAZOP_5_06 --concerns--> E101
PSHH117 --monitors--> E101
TT413 --monitors--> E101
HAZOP_7_13 --concerns--> E101
TT107 --monitors--> E101
TT306 --monitors--> E101
E101_N_top_inlet --onEquipment--> E101
E101_sample_1 --onColumn--> E101
AOI10 --about--> E101
RV400 --protects--> E101
FT108 --monitors--> E101
TT411 --monitors--> E101
TT204 --monitors--> E101
aspen_v3_feed_gas --ofEquipment--> E101
HAZOP_element_10 --covers--> E101
HAZOP_8_11 --concerns--> E101
TT307 --monitors--> E101
TT308 --monitors--> E101
HAZOP_8_02 --concerns--> E101
aspen_v3_E101_performance --ofEquipment--> E101
PCV300 --valveType--> pressure control
PCV300 --floor--> 3
PCV300 --normalPosition--> open
PCV300 --note--> Vents lean gas from the absorber to hold the E101 pressure (PIC403). Opened in the vent stream start-up (Fig F.3), closed at shutdown.
PCV300 --pipedTo--> VENT_E101
PCV300 --label--> PCV300
PCV300 --feedsInto--> VENT_E101
PCV300 --type--> PressureControlValve
PCV300 --tag--> PCV300
PCV300 --gridReference--> G18
K402 --feedsInto--> PCV300
CL_E101_pressure --hasFinalElement--> PCV300
K402 --pipedTo--> PCV300
PIC403 --controls--> PCV300
AV01 --about--> PCV300
K101 --type--> Saturator
K101 --label--> K101 gas saturator
K101 --pipedTo--> SDV170
K101 --pipedTo--> Z103
K101 --floor--> 1
K101 --feedsInto--> E101_N_gas_inlet
K101 --pipedTo--> E101_N_gas_inlet
K101 --note--> Saturates the feed gas with water before E101; temperature held by TIC121 using C106 on the recirculating water. Grid not in the REPORT lists (near L17 to L18 on the P&ID). Not modelled in Aspen (GOI09).
K101 --pipedTo--> V126
K101 --tag--> K101
DI_CARTRIDGE --feedsInto--> K101
HAZOP_4_06 --concerns--> K101
V172 --pipedTo--> K101
J102 --pipedTo--> K101
limit_LZAL_K101 --appliesTo--> K101
HAZOP_4_07 --concerns--> K101
LT104 --monitors--> K101
HAZOP_3_05 --concerns--> K101
FEED_GAS_HEADER --feedsInto--> K101
GOI09 --about--> K101
LI106 --monitors--> K101
FEED_GAS_HEADER --pipedTo--> K101
limit_LAL_K101 --appliesTo--> K101
K101_N2_recycle --fromItem--> K101
limit_LZAH_K101 --appliesTo--> K101
GOI07 --about--> K101
GOI02 --about--> K101
HAZOP_element_3 --covers--> K101
HAZOP_4_02 --concerns--> K101
TI121 --monitors--> K101
C106 --pipedTo--> K101
```

Question: How do the fresh CO2 and N2 feeds reach the absorber?

## Q21

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
K101 --type--> Saturator
K101 --label--> K101 gas saturator
K101 --pipedTo--> SDV170
K101 --pipedTo--> Z103
K101 --floor--> 1
K101 --feedsInto--> E101_N_gas_inlet
K101 --pipedTo--> E101_N_gas_inlet
K101 --note--> Saturates the feed gas with water before E101; temperature held by TIC121 using C106 on the recirculating water. Grid not in the REPORT lists (near L17 to L18 on the P&ID). Not modelled in Aspen (GOI09).
K101 --pipedTo--> V126
K101 --tag--> K101
DI_CARTRIDGE --feedsInto--> K101
HAZOP_4_06 --concerns--> K101
V172 --pipedTo--> K101
J102 --pipedTo--> K101
limit_LZAL_K101 --appliesTo--> K101
HAZOP_4_07 --concerns--> K101
LT104 --monitors--> K101
HAZOP_3_05 --concerns--> K101
FEED_GAS_HEADER --feedsInto--> K101
GOI09 --about--> K101
LI106 --monitors--> K101
FEED_GAS_HEADER --pipedTo--> K101
limit_LAL_K101 --appliesTo--> K101
K101_N2_recycle --fromItem--> K101
limit_LZAH_K101 --appliesTo--> K101
GOI07 --about--> K101
GOI02 --about--> K101
HAZOP_element_3 --covers--> K101
HAZOP_4_02 --concerns--> K101
TI121 --monitors--> K101
C106 --pipedTo--> K101
K103_CO2_recycle --bypasses--> K101
TT121 --monitors--> K101
DI_CARTRIDGE --pipedTo--> K101
J102 --feedsInto--> K101
V172 --feedsInto--> K101
N2ReturnLoop --hasStep--> N2ReturnLoop_step_00_E101
N2ReturnLoop --hasStep--> N2ReturnLoop_step_02_K402
N2ReturnLoop --hasStep--> N2ReturnLoop_step_15_E101_N_gas_inlet
N2ReturnLoop --inMode--> FigureOfEight
N2ReturnLoop --hasStep--> N2ReturnLoop_step_01_E101_N_gas_outlet
N2ReturnLoop --hasStep--> N2ReturnLoop_step_05_FT303
N2ReturnLoop --hasStep--> N2ReturnLoop_step_16_E101
N2ReturnLoop --hasStep--> N2ReturnLoop_step_13_FT107
N2ReturnLoop --hasStep--> N2ReturnLoop_step_07_FT304
N2ReturnLoop --note--> N2 is not absorbed, so it is recirculated: J102 blows it from the K402 overhead back through K101 into E101. Fresh N2 and CO2 (piece 5) top it up. FCV111 recycles part of it from K101 back to K102 to set the N2 flow into E101.
N2ReturnLoop --hasStep--> N2ReturnLoop_step_03_K402_N_gas_to_return
N2ReturnLoop --hasStep--> N2ReturnLoop_step_10_V187
N2ReturnLoop --hasStep--> N2ReturnLoop_step_04_TT304
N2ReturnLoop --label--> N2 return loop (E101 > K402 > K102 > J102 > K101 > E101)
N2ReturnLoop --hasStep--> N2ReturnLoop_step_12_TT114
N2ReturnLoop --hasStep--> N2ReturnLoop_step_08_FI304
N2ReturnLoop --hasStep--> N2ReturnLoop_step_14_K101
N2ReturnLoop --hasStep--> N2ReturnLoop_step_06_FI303
N2ReturnLoop --hasStep--> N2ReturnLoop_step_09_K102
N2ReturnLoop --type--> Loop
N2ReturnLoop --hasStep--> N2ReturnLoop_step_11_J102
FCV111 --floor--> 1
FCV111 --valveType--> flow control
FCV111 --tag--> FCV111
FCV111 --pipedTo--> K102
FCV111 --label--> FCV111
FCV111 --gridReference--> K17
FCV111 --type--> FlowControlValve
FCV111 --normalPosition--> open
FCV111 --note--> Recycles N2 from K101 back to K102, reducing the recycled N2 entering E101 (REPORT D.4, Fig D.6/D.7). Controlled by FIC303/FIC304 from FT303/FT304 on the N2 recycle pipe.
FIC304 --controls--> FCV111
K101_N2_recycle --routeVia--> FCV111
SDV170 --pipedTo--> FCV111
CL_N2_to_E101 --hasFinalElement--> FCV111
FIC303 --controls--> FCV111
N2ReturnLoop_step_11_J102 --label--> N2 return loop (E101 > K402 > K102 > J102 > K101 > E101) step 11: J102
N2ReturnLoop_step_11_J102 --stepItem--> J102
N2ReturnLoop_step_11_J102 --stepIndex--> 11
N2ReturnLoop_step_11_J102 --type--> LoopStep
N2ReturnLoop_step_11_J102 --stepType--> inline
NRV100b --type--> CheckValve
NRV100b --gridReference--> Q19
NRV100b --note--> Bottom right (make-up water to K101?). FI03
NRV100b --feedsInto--> DI_CARTRIDGE
NRV100b --pipedTo--> DI_CARTRIDGE
NRV100b --valveType--> check
NRV100b --label--> NRV100b
NRV100b --tag--> NRV100b
NRV100b --floor--> 1
NRV100a --feedsInto--> NRV100b
NRV100a --pipedTo--> NRV100b
N2ReturnLoop_step_04_TT304 --stepType--> tie-in
N2ReturnLoop_step_04_TT304 --type--> LoopStep
N2ReturnLoop_step_04_TT304 --label--> N2 return loop (E101 > K402 > K102 > J102 > K101 > E101) step 4: TT304
N2ReturnLoop_step_04_TT304 --stepIndex--> 4
N2ReturnLoop_step_04_TT304 --stepItem--> TT304
TT107 --label--> TT107
TT107 --signalType--> Fieldbus
TT107 --sensorType--> PRT
TT107 --floor--> 1
TT107 --measuredVariable--> gas entering E101 (after K101)
TT107 --monitors--> E101
TT107 --type--> TemperatureInstrument
TT107 --gridReference--> K18
TT107 --tag--> TT107
HAZOP_10_03 --label--> HAZOP 10.3
HAZOP_10_03 --consequence--> Overpressure lower section of E101 and K101
HAZOP_10_03 --actionTaken--> RV added
HAZOP_10_03 --itemNumber--> 3
HAZOP_10_03 --inElement--> HAZOP_element_10
HAZOP_10_03 --parameter--> FLOW
HAZOP_10_03 --cause--> High rate of gas up column from CO2 and N2 feed system
HAZOP_10_03 --type--> HazopDeviation
HAZOP_10_03 --concerns--> E101
HAZOP_10_03 --recommendedAction--> RV at outlet to K101?
HAZOP_10_03 --guideword--> MORE
N2ReturnLoop_step_05_FT303 --stepItem--> FT303
N2ReturnLoop_step_05_FT303 --type--> LoopStep
N2ReturnLoop_step_05_FT303 --stepType--> inline
N2ReturnLoop_step_05_FT303 --label--> N2 return loop (E101 > K402 > K102 > J102 > K101 > E101) step 5: FT303
N2ReturnLoop_step_05_FT303 --stepIndex--> 5
HAZOP_4_06 --cause--> As K101
HAZOP_4_06 --parameter--> TEMP.
HAZOP_4_06 --label--> HAZOP 4.6
HAZOP_4_06 --itemNumber--> 6
HAZOP_4_06 --type--> HazopDeviation
HAZOP_4_06 --inElement--> HAZOP_element_4
HAZOP_4_06 --guideword--> HIGHER
N2ReturnLoop_step_10_V187 --stepItem--> V187
N2ReturnLoop_step_10_V187 --stepType--> branch
N2ReturnLoop_step_10_V187 --label--> N2 return loop (E101 > K402 > K102 > J102 > K101 > E101) step 10: V187
N2ReturnLoop_step_10_V187 --stepIndex--> 10
N2ReturnLoop_step_10_V187 --type--> LoopStep
GOI09 --foundBy--> gas section build, Oct 2026
GOI09 --itemStatus--> open
GOI09 --label--> GOI09: Aspen feeds the gas straight into E101 with no K101 saturator
GOI09 --description--> Aspen feeds the gas straight into E101 with no K101 saturator
GOI09 --resolvedBy--> Note for model comparison
GOI09 --type--> OpenItem
limit_LZAH_K101 --type--> OperatingLimit
limit_LZAH_K101 --variable--> level
limit_LZAH_K101 --unit--> -
limit_LZAH_K101 --limitType--> alarm
limit_LZAH_K101 --source--> HAZOP element 3, item 5 (LZAH104, now LZAH103; soft high alarm added)
limit_LZAH_K101 --valueVerified--> false
limit_LZAH_K101 --label--> LZAH_K101
SDV170 --gridReference--> K17
SDV170 --label--> SDV170
SDV170 --valveType--> shutdown (solenoid-operated)
SDV170 --tag--> SDV170
SDV170 --type--> ShutdownValve
SDV170 --floor--> 1
SDV170 --note--> On the FCV111 recycle line from K101 to K102 (P&ID shows SDV170 with HS170 next to FCV111); the REPORT lists it as SOV170.
K101_N2_recycle --routeVia--> SDV170
```

Question: How is water circulated around the gas saturator K101, and which exchanger is associated with its temperature regulation?

## Q22

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
H100 --tag--> H100
H100 --floor--> 1
H100 --source--> SUMMARY p.102
H100 --type--> SteamReboiler
H100 --feedsInto--> Q106
H100 --pipedTo--> Q106
H100 --label--> H100 vertical thermosiphon steam reboiler
FI102 --monitors--> H100
H100_N_condensate_out --onEquipment--> H100
TT100 --monitors--> H100
aspen_v3_H100_performance --ofEquipment--> H100
FT101 --monitors--> H100
HAZOP_element_13 --covers--> H100
aspen_v6_1_block_H100 --represents--> H100
TI100 --monitors--> H100
PROC_reboiler_heating_step_04 --operatesOn--> H100
DI100 --monitors--> H100
limit_H100_steam_limit --appliesTo--> H100
PI101 --monitors--> H100
PI100 --monitors--> H100
aspen_v3_block_H100REAC --represents--> H100
PT101 --monitors--> H100
FT102 --monitors--> H100
aspen_v3_block_H100HEAT --represents--> H100
TT117 --monitors--> H100
TT118 --monitors--> H100
FI100 --monitors--> H100
Q105 --pipedTo--> H100
H100_N_steam_in --onEquipment--> H100
Q105 --feedsInto--> H100
aspen_v6_1_H100_performance --ofEquipment--> H100
FT100 --monitors--> H100
HAZOP_element_11 --covers--> H100
RV107 --protects--> H100
aspen_v6_1_block_H100 --label--> H100 (ABB_pilot_plant_final_6_1_SA_validation)
aspen_v6_1_block_H100 --blockId--> H100
aspen_v6_1_block_H100 --aspenModel--> HEATX
aspen_v6_1_block_H100 --type--> AspenBlock
aspen_v6_1_block_H100 --statusMessage--> INVALID INPUT SPECIFICATIONS SEE TASC BROWSER FOR INFO.
aspen_v6_1_block_H100 --status--> ERROR
aspen_v6_1_block_H100 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S14 --fromBlock--> aspen_v6_1_block_H100
aspen_v6_1_stream_S17 --fromBlock--> aspen_v6_1_block_H100
aspen_v6_1_stream_S31 --toBlock--> aspen_v6_1_block_H100
aspen_v6_1_stream_S23 --toBlock--> aspen_v6_1_block_H100
PROC_reboiler_heating_step_01 --operatesOn--> FT100
PROC_reboiler_heating_step_01 --stepOrder--> 1
PROC_reboiler_heating_step_01 --instruction--> Check whether FT100 and FT101 show steam flowing to H100
PROC_reboiler_heating_step_01 --type--> ProcedureStep
PROC_reboiler_heating_step_01 --label--> Reboiler heating the MEA during the stripping loop test step 1
PROC_reboiler_heating --hasProcedureStep--> PROC_reboiler_heating_step_01
aspen_v6_1_stream_S14 --massFlow_kg_h--> 199.9608
aspen_v6_1_stream_S14 --co2Loading_mol_mol--> 0.638118
aspen_v6_1_stream_S14 --waterFlow_kg_h--> 156.4997
aspen_v6_1_stream_S14 --temperature_C--> 89.36771
aspen_v6_1_stream_S14 --pressure_bar--> 2.05248
aspen_v6_1_stream_S14 --type--> StreamState
aspen_v6_1_stream_S14 --label--> S14 (ABB_pilot_plant_final_6_1_SA_validation)
aspen_v6_1_stream_S14 --streamId--> S14
aspen_v6_1_stream_S14 --moleFlow_kmol_h--> 9.279221
aspen_v6_1_stream_S14 --vapourFraction--> 0.0
aspen_v6_1_stream_S14 --phase--> LIQUID
aspen_v6_1_stream_S14 --apparentCO2_kg_h--> 13.05912
aspen_v6_1_stream_S14 --meaMassFraction--> 0.1420495
aspen_v6_1_stream_S14 --enthalpyFlow_W--> -759156.0
aspen_v6_1_stream_S14 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S14 --toBlock--> aspen_v6_1_block_E100
SteamRoute_step_19_V103 --label--> Steam and condensate route to H100 step 19: V103
SteamRoute_step_19_V103 --stepItem--> V103
SteamRoute_step_19_V103 --stepType--> inline
SteamRoute_step_19_V103 --stepIndex--> 19
SteamRoute_step_19_V103 --type--> LoopStep
SteamRoute --hasStep--> SteamRoute_step_17_K100
SteamRoute --hasStep--> SteamRoute_step_15_PI101
SteamRoute --hasStep--> SteamRoute_step_21_V105
SteamRoute --hasStep--> SteamRoute_step_02_V100
SteamRoute --hasStep--> SteamRoute_step_20_V104
SteamRoute --hasStep--> SteamRoute_step_04_PI100
SteamRoute --hasStep--> SteamRoute_step_13_H100_N_condensate_out
SteamRoute --hasStep--> SteamRoute_step_01_XV140
SteamRoute --type--> Loop
SteamRoute --hasStep--> SteamRoute_step_14_TT118
SteamRoute --hasStep--> SteamRoute_step_07_FI100
SteamRoute --hasStep--> SteamRoute_step_11_TT117
SteamRoute --hasStep--> SteamRoute_step_16_RV107
SteamRoute --hasStep--> SteamRoute_step_22_NRV110
SteamRoute --hasStep--> SteamRoute_step_03_PT101
SteamRoute --note--> Building steam heats the MEA in the H100 reboiler shell and leaves as condensate through the K100 trap. FCV110 sets the steam flow (TIC100 > FIC100 cascade, stripping loop).
SteamRoute --inMode--> FigureOfEight
SteamRoute --hasStep--> SteamRoute_step_09_FT101
SteamRoute --hasStep--> SteamRoute_step_12_H100_N_steam_in
SteamRoute --hasStep--> SteamRoute_step_19_V103
SteamRoute --hasStep--> SteamRoute_step_05_V101
SteamRoute --hasStep--> SteamRoute_step_06_FT100
SteamRoute --hasStep--> SteamRoute_step_08_V102
SteamRoute --hasStep--> SteamRoute_step_10_FCV110
SteamRoute --label--> Steam and condensate route to H100
SteamRoute --hasStep--> SteamRoute_step_00_STEAM_SUPPLY
SteamRoute --hasStep--> SteamRoute_step_23_CONDENSATE_RETURN
SteamRoute --hasStep--> SteamRoute_step_18_V106
aspen_v3_H100_performance --coldInlet_C--> 116.8438
aspen_v3_H100_performance --label--> H100 performance (ABB_pilot_plant_final_3)
aspen_v3_H100_performance --coldSideDuty_kW--> 115.5427
aspen_v3_H100_performance --type--> HeatExchangerPerformance
aspen_v3_H100_performance --lmtd_K--> 32.8462
aspen_v3_H100_performance --area_m2--> 61.6081
aspen_v3_H100_performance --hotOutlet_C--> 118.2011
aspen_v3_H100_performance --derivedBy--> heat_mass_transfer.py
aspen_v3_H100_performance --minApproach_K--> 1.357255
aspen_v3_H100_performance --temperatureCross--> false
aspen_v3_H100_performance --overallU_W_m2K--> 448.1082
aspen_v3_H100_performance --hotInlet_C--> 276.85
aspen_v3_H100_performance --effectiveness--> 0.9911752
aspen_v3_H100_performance --hotSideDuty_kW--> 115.5827
aspen_v3_H100_performance --coldOutlet_C--> 119.3414
aspen_v3_H100_performance --duty_kW--> 115.5627
aspen_v3_H100_performance --energyBalanceError_pct--> 0.03452101
aspen_v3_H100_performance --ua_W_K--> 3517.69
aspen_v3_H100_performance --inCase--> case_aspen_v3
V102 --label--> V102
V102 --note--> Steam side of H100. Closed in the stripping loop test: no steam (REPORT Fig E.1).
V102 --feedsInto--> FT101
V102 --tag--> V102
V102 --pipedTo--> FT101
V102 --type--> ManualValve
V102 --normalPosition--> closed
V102 --gridReference--> L4
V102 --valveType--> ball
V102 --floor--> 1
FT100 --feedsInto--> V102
FT100 --pipedTo--> V102
PROC_stripping_loop_lineup_step_08 --operatesOn--> V102
PROC_H100_steam_bypass_step_05 --operatesOn--> V102
HAZOP_element_13 --covers--> V102
case_aspen_v6_1 --converged--> false
case_aspen_v6_1 --representsMode--> FigureOfEight
case_aspen_v6_1 --savedOn--> Thu Feb 27 15:14:32 2025
case_aspen_v6_1 --recommendedForUse--> false
case_aspen_v6_1 --aspenFile--> ABB_pilot_plant_final_6_1_SA_validation.apwz
case_aspen_v6_1 --label--> ABB_pilot_plant_final_6_1_SA_validation
case_aspen_v6_1 --aspenVersion--> 37.0
case_aspen_v6_1 --note--> Rescaled to pilot conditions with a sensitivity study for validation. Saved results did not converge: E100 RateSep failed, H100 invalid input, C100 temperature crossover, recycle opened at S3BACKUP.
case_aspen_v6_1 --type--> SimulationCase
aspen_v6_1_block_E100 --inCase--> case_aspen_v6_1
aspen_v6_1_block_C400COND --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S21 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_PURGE --inCase--> case_aspen_v6_1
aspen_v6_1_E100_stage_02 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S4 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S17 --inCase--> case_aspen_v6_1
```

Question: Which steam supply components are upstream of reboiler H100?

## Q23

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
C200 --note--> Cools lean MEA before the absorber; cooling water flow set by FIC201 (cascade from TIC210).
C200 --type--> TrimCooler
C200 --feedsInto--> NRV400
C200 --floor--> 2
C200 --tag--> C200
C200 --label--> C200 lean MEA trim cooler (water cooled)
C200 --pipedTo--> NRV400
HAZOP_7_12 --concerns--> C200
HAZOP_10_07 --concerns--> C200
N200_bypass --toItem--> C200
TT209 --monitors--> C200
V212 --pipedTo--> C200
TI210 --monitors--> C200
V213 --feedsInto--> C200
aspen_v6_1_C200_performance --ofEquipment--> C200
TT208 --monitors--> C200
V213 --pipedTo--> C200
FI201 --monitors--> C200
FT201 --monitors--> C200
C200_N_cw_in --onEquipment--> C200
HAZOP_element_7 --covers--> C200
FI200 --monitors--> C200
aspen_v3_C200_performance --ofEquipment--> C200
TT210 --monitors--> C200
C200_N_cw_out --onEquipment--> C200
aspen_v3_block_C200 --label--> C200 (ABB_pilot_plant_final_3)
aspen_v3_block_C200 --status--> OK
aspen_v3_block_C200 --inCase--> case_aspen_v3
aspen_v3_block_C200 --blockId--> C200
aspen_v3_block_C200 --aspenModel--> HEATER
aspen_v3_block_C200 --type--> AspenBlock
aspen_v3_stream_S2 --toBlock--> aspen_v3_block_C200
aspen_v3_stream_2 --fromBlock--> aspen_v3_block_C200
FI200 --floor--> 2
FI200 --tag--> FI200
FI200 --measuredVariable--> C200 cooling water flow indication (local)
FI200 --label--> FI200
FI200 --type--> FlowInstrument
FI200 --gridReference--> H11
C200_N_cw_out__utlcit01 --type--> Citation
C200_N_cw_out__utlcit01 --label--> Citation 1 for C200_N_cw_out (utl)
C200_N_cw_out__utlcit01 --document--> SRC_PID
C200_N_cw_out__utlcit01 --citationText--> P&ID C200
C200_N_cw_out__utlcit01 --location--> C200
C200_N_cw_in__utlcit01 --label--> Citation 1 for C200_N_cw_in (utl)
C200_N_cw_in__utlcit01 --type--> Citation
C200_N_cw_in__utlcit01 --document--> SRC_PID
C200_N_cw_in__utlcit01 --citationText--> P&ID C200
C200_N_cw_in__utlcit01 --location--> C200
aspen_v6_1_block_C200 --blockId--> C200
aspen_v6_1_block_C200 --type--> AspenBlock
aspen_v6_1_block_C200 --label--> C200 (ABB_pilot_plant_final_6_1_SA_validation)
aspen_v6_1_block_C200 --inCase--> case_aspen_v6_1
aspen_v6_1_block_C200 --status--> OK
aspen_v6_1_block_C200 --aspenModel--> HEATER
aspen_v6_1_stream_2 --fromBlock--> aspen_v6_1_block_C200
aspen_v6_1_stream_S2 --toBlock--> aspen_v6_1_block_C200
C200__abscit02 --label--> Citation 2 for C200 (absorption loop)
C200__abscit02 --type--> Citation
C200__abscit02 --document--> SRC_REPORT
C200__abscit02 --location--> section 3 (C200 is a trim cooler, second floor)
C200__abscit02 --citationText--> Pilot Plant Report section 3 (C200 is a trim cooler, second floor)
FI200__utlcit01 --location--> grid H11
FI200__utlcit01 --citationText--> P&ID grid H11
FI200__utlcit01 --document--> SRC_PID
FI200__utlcit01 --type--> Citation
FI200__utlcit01 --label--> Citation 1 for FI200 (utl)
C200__abscit03 --location--> block C200
C200__abscit03 --type--> Citation
C200__abscit03 --citationText--> Aspen v3 block C200
C200__abscit03 --document--> SRC_ASPEN_V3
C200__abscit03 --label--> Citation 3 for C200 (absorption loop)
HAZOP_11_07 --label--> HAZOP 11.7
HAZOP_11_07 --cause--> Any failure of the system pressure control
HAZOP_11_07 --guideword--> HIGHER
HAZOP_11_07 --type--> HazopDeviation
HAZOP_11_07 --consequence--> Increased degradation of MEA (slight)
HAZOP_11_07 --itemNumber--> 7
HAZOP_11_07 --inElement--> HAZOP_element_11
HAZOP_11_07 --parameter--> TEMP.
HAZOP_11_07 --actionTaken--> TAH added
HAZOP_11_07 --recommendedAction--> Consider TAH on process outlet from C200
TIC210 --controls--> FCV200
TIC210 --label--> C200 outlet temperature controller (cascade master)
TIC210 --tag--> TIC210
TIC210 --type--> Controller
CL_C200_temperature --hasController--> TIC210
TT215 --signalType--> Fieldbus
TT215 --measuredVariable--> temperature near C200 (position to trace, FI05)
TT215 --floor--> 2
TT215 --sensorType--> K-type thermocouple
TT215 --gridReference--> J13
TT215 --type--> TemperatureInstrument
TT215 --label--> TT215
TT215 --tag--> TT215
AOI08 --foundBy--> absorption loop build, Oct 2026
AOI08 --itemStatus--> open
AOI08 --resolvedBy--> Site check
AOI08 --about--> FCV201
AOI08 --description--> FCV200 and FCV201 are both on the C200 cooling water line; FIC201 drives FCV200, but the role of FCV201 is not documented
AOI08 --about--> FCV200
AOI08 --type--> OpenItem
AOI08 --label--> AOI08: FCV200 and FCV201 are both on the C200 cooling water line; FIC201 drives FCV200, but the role of FCV201 is not documented
aspen_v3_stream_2 --pressure_bar--> 2.0
aspen_v3_stream_2 --moleFlow_kmol_h--> 22.9975
aspen_v3_stream_2 --massFlow_kg_h--> 552.2604
aspen_v3_stream_2 --streamId--> 2
aspen_v3_stream_2 --label--> 2 (ABB_pilot_plant_final_3)
aspen_v3_stream_2 --inCase--> case_aspen_v3
aspen_v3_stream_2 --apparentCO2_kg_h--> 31.84518
aspen_v3_stream_2 --meaMassFraction--> 0.2725138
aspen_v3_stream_2 --waterFlow_kg_h--> 369.31
aspen_v3_stream_2 --vapourFraction--> 0.0
aspen_v3_stream_2 --type--> StreamState
aspen_v3_stream_2 --toBlock--> aspen_v3_block_E101
aspen_v3_stream_2 --phase--> LIQUID
aspen_v3_stream_2 --enthalpyFlow_W--> -1905236.0
aspen_v3_stream_2 --temperature_C--> 40.0
aspen_v3_stream_2 --co2Loading_mol_mol--> 0.2936858
CL_C200_cooling_water --type--> ControlLoop
CL_C200_cooling_water --hasController--> FIC201
CL_C200_cooling_water --manipulatedVariable--> FCV200 opening
CL_C200_cooling_water --label--> Cooling water flow to C200 (cascade slave)
CL_C200_cooling_water --hasFinalElement--> FCV200
CL_C200_cooling_water --hasSensor--> FT201
CL_C200_cooling_water --controlledVariable--> Cooling water flowrate to C200
CL_C200_temperature --cascadeMasterOf--> CL_C200_cooling_water
aspen_v6_1_C200_performance --label--> C200 performance (ABB_pilot_plant_final_6_1_SA_validation)
aspen_v6_1_C200_performance --duty_kW--> 7.236044
aspen_v6_1_C200_performance --derivedBy--> build_absorption_loop.py
aspen_v6_1_C200_performance --hotInlet_C--> 70.52478
aspen_v6_1_C200_performance --note--> Lean MEA side only; Aspen models C200 as a heater block, so the cooling water side is not simulated.
aspen_v6_1_C200_performance --inCase--> case_aspen_v6_1
aspen_v6_1_C200_performance --hotOutlet_C--> 45.0
aspen_v6_1_C200_performance --type--> HeatExchangerPerformance
TT209 --sensorType--> PRT
TT209 --label--> TT209
TT209 --gridReference--> J12
TT209 --type--> TemperatureInstrument
TT209 --measuredVariable--> lean MEA entering C200
TT209 --tag--> TT209
TT209 --signalType--> Fieldbus
TT209 --floor--> 2
discrepancy_TT208_TT209_swap --concerns--> TT209
limit_TAH_C200_outlet --type--> OperatingLimit
limit_TAH_C200_outlet --unit--> C
limit_TAH_C200_outlet --limitType--> alarm
limit_TAH_C200_outlet --label--> TAH_C200_outlet
limit_TAH_C200_outlet --valueVerified--> false
limit_TAH_C200_outlet --variable--> temperature
```

Question: Describe the cooling water route and associated instrumentation around C200, including the real position of FI200.

## Q24

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
C400_N_cw_out__utlcit01 --location--> C400
C400_N_cw_out__utlcit01 --type--> Citation
C400_N_cw_out__utlcit01 --document--> SRC_PID
C400_N_cw_out__utlcit01 --citationText--> P&ID C400
C400_N_cw_out__utlcit01 --label--> Citation 1 for C400_N_cw_out (utl)
aspen_v3_block_C400 --inCase--> case_aspen_v3
aspen_v3_block_C400 --aspenModel--> HEATER
aspen_v3_block_C400 --type--> AspenBlock
aspen_v3_block_C400 --blockId--> C400
aspen_v3_block_C400 --status--> OK
aspen_v3_block_C400 --label--> C400 (ABB_pilot_plant_final_3)
aspen_v3_stream_S11 --fromBlock--> aspen_v3_block_C400
aspen_v3_stream_S13 --toBlock--> aspen_v3_block_C400
C400_N_cw_in__utlcit01 --type--> Citation
C400_N_cw_in__utlcit01 --document--> SRC_PID
C400_N_cw_in__utlcit01 --citationText--> P&ID C400
C400_N_cw_in__utlcit01 --label--> Citation 1 for C400_N_cw_in (utl)
C400_N_cw_in__utlcit01 --location--> C400
aspen_v6_1_block_C400 --aspenModel--> HEATER
aspen_v6_1_block_C400 --label--> C400 (ABB_pilot_plant_final_6_1_SA_validation)
aspen_v6_1_block_C400 --blockId--> C400
aspen_v6_1_block_C400 --inCase--> case_aspen_v6_1
aspen_v6_1_block_C400 --status--> OK
aspen_v6_1_block_C400 --type--> AspenBlock
aspen_v6_1_stream_S11 --fromBlock--> aspen_v6_1_block_C400
aspen_v6_1_stream_S15 --toBlock--> aspen_v6_1_block_C400
C400 --floor--> 4
C400 --pipedTo--> K401
C400 --type--> Condenser
C400 --label--> C400 overhead condenser (spiral heat exchanger)
C400 --tag--> C400
C400 --note--> Water-cooled; cooling water flow set by FIC402 on FCV401 (cascade from TIC410). Grid not in the REPORT lists (between C8 and E10 on the P&ID).
C400 --feedsInto--> K401
E100_N_overhead --pipedTo--> C400
OOI04 --about--> C400
HAZOP_12_07 --concerns--> C400
aspen_v3_C400_performance --ofEquipment--> C400
OOI06 --about--> C400
HAZOP_12_03 --concerns--> C400
FI402 --monitors--> C400
C400_N_cw_in --onEquipment--> C400
HAZOP_6_05 --concerns--> C400
HAZOP_6_01 --concerns--> C400
C400_N_cw_out --onEquipment--> C400
PT401 --monitors--> C400
HAZOP_element_12 --covers--> C400
TI410 --monitors--> C400
limit_TAH_C400_carryover --appliesTo--> C400
FI401 --monitors--> C400
FT402 --monitors--> C400
HAZOP_6_06 --concerns--> C400
E100_N_overhead --feedsInto--> C400
TT410 --monitors--> C400
E100_N_overhead --type--> Nozzle
E100_N_overhead --onEquipment--> E100
E100_N_overhead --label--> E100 vapour outlet at the top of the column
E100 --feedsInto--> E100_N_overhead
E100 --pipedTo--> E100_N_overhead
C400__ovhcit01 --label--> Citation 1 for C400 (ovh)
C400__ovhcit01 --type--> Citation
C400__ovhcit01 --location--> overhead line after PT401, top of the drawing
C400__ovhcit01 --document--> SRC_PID
C400__ovhcit01 --citationText--> P&ID overhead line after PT401, top of the drawing
PCV415 --pipedTo--> FCV401
PCV415 --normalPosition--> open
PCV415 --note--> Pressure regulator on the C400 cooling water stream (UT09). The valve list gives floor 3.
PCV415 --floor--> 4
PCV415 --type--> PressureControlValve
PCV415 --gridReference--> C14
PCV415 --tag--> PCV415
PCV415 --feedsInto--> FCV401
PCV415 --valveType--> pressure control
PCV415 --label--> PCV415
UT09 --about--> PCV415
V405 --feedsInto--> PCV415
V405 --pipedTo--> PCV415
TIC410 --type--> Controller
TIC410 --tag--> TIC410
TIC410 --label--> C400 gas outlet temperature controller (cascade master)
TIC410 --controls--> FCV401
CL_C400_temperature --hasController--> TIC410
OOI04 --description--> Aspen returns the reflux to the rich feed before the heaters (MIXER2), but on the P&ID it joins after them at V403/V402
OOI04 --foundBy--> ovh section build, Oct 2026
OOI04 --about--> J300
OOI04 --type--> OpenItem
OOI04 --resolvedBy--> Note for model comparison; update the Aspen flowsheet if needed
OOI04 --itemStatus--> open
OOI04 --label--> OOI04: Aspen returns the reflux to the rich feed before the heaters (MIXER2), but on the P&ID it joins after them at V403/V402
HAZOP_6_01 --actionTaken--> Pump shutdown trip added
HAZOP_6_01 --consequence--> No flow to J103
HAZOP_6_01 --concerns--> J103
HAZOP_6_01 --inElement--> HAZOP_element_6
HAZOP_6_01 --cause--> K401 / C300 (now C400) blocked
HAZOP_6_01 --guideword--> NO
HAZOP_6_01 --label--> HAZOP 6.1
HAZOP_6_01 --recommendedAction--> Consider consequences of starving J103
HAZOP_6_01 --parameter--> FLOW
HAZOP_6_01 --type--> HazopDeviation
HAZOP_6_01 --itemNumber--> 1
HAZOP_6_01 --concerns--> K401
TT410 --signalType--> Fieldbus
TT410 --measuredVariable--> temperature of CO2 leaving C400
TT410 --floor--> 4
TT410 --label--> TT410
TT410 --sensorType--> PRT
TT410 --tag--> TT410
TT410 --gridReference--> C15
TT410 --type--> TemperatureInstrument
CL_C400_temperature --hasSensor--> TT410
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_07_J300
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_14_FT305
OverheadRefluxLoop --label--> Stripper overhead and reflux loop
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_09_RV300
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_02_PT401
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_03_C400
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_10_B300
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_08_TT310
OverheadRefluxLoop --note--> Runs whenever E100 is boiling. Vapour is condensed in C400; K401 separates the condensate (returned as reflux by J300) from the CO2-rich gas (to the CO2 return, piece 7).
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_06_LT401
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_05_K401
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_17_E100_N_top_inlet
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_01_E100_N_overhead
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_15_V403
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_00_E100
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_16_V402
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_12_V317
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_13_TT309
OverheadRefluxLoop --type--> Loop
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_04_LSHH400
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_11_PCV302
OverheadRefluxLoop --inMode--> FigureOfEight
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_18_E100
C400__ovhcit03 --citationText--> P&ID differences row LSHH400 (between C400 and K401)
C400__ovhcit03 --location--> row LSHH400 (between C400 and K401)
C400__ovhcit03 --document--> SRC_DIFF
C400__ovhcit03 --label--> Citation 3 for C400 (ovh)
C400__ovhcit03 --type--> Citation
C400_N_cw_in --pipedTo--> C400_N_cw_out
C400_N_cw_in --label--> C400 cooling water inlet
C400_N_cw_in --type--> Nozzle
C400_N_cw_in --feedsInto--> C400_N_cw_out
FT402 --pipedTo--> C400_N_cw_in
FT402 --feedsInto--> C400_N_cw_in
CL_C400_cooling_water --hasFinalElement--> FCV401
CL_C400_cooling_water --controlledVariable--> Cooling water flowrate to C400
CL_C400_cooling_water --manipulatedVariable--> FCV401 opening
CL_C400_cooling_water --label--> Cooling water flow to C400 (cascade slave)
CL_C400_cooling_water --hasController--> FIC402
CL_C400_cooling_water --hasSensor--> FT402
CL_C400_cooling_water --type--> ControlLoop
```

Question: Which instruments and control valve are associated with the cooling water supply to condenser C400?

## Q25

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
```

Question: Which control valve regulates the cooling water supplied to C401, and which controller operates it?

## Q26

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
aspen_v3_block_E101 --type--> AspenBlock
aspen_v3_block_E101 --aspenModel--> RADFRAC
aspen_v3_block_E101 --blockId--> E101
aspen_v3_block_E101 --status--> OK
aspen_v3_block_E101 --label--> E101 (ABB_pilot_plant_final_3)
aspen_v3_block_E101 --inCase--> case_aspen_v3
aspen_v3_stream_S8 --fromBlock--> aspen_v3_block_E101
aspen_v3_stream_1 --toBlock--> aspen_v3_block_E101
aspen_v3_stream_2 --toBlock--> aspen_v3_block_E101
aspen_v3_stream_4 --fromBlock--> aspen_v3_block_E101
aspen_v6_1_block_E101 --type--> AspenBlock
aspen_v6_1_block_E101 --aspenModel--> RADFRAC
aspen_v6_1_block_E101 --label--> E101 (ABB_pilot_plant_final_6_1_SA_validation)
aspen_v6_1_block_E101 --blockId--> E101
aspen_v6_1_block_E101 --status--> OK
aspen_v6_1_block_E101 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S8 --fromBlock--> aspen_v6_1_block_E101
aspen_v6_1_stream_2 --toBlock--> aspen_v6_1_block_E101
aspen_v6_1_stream_1 --toBlock--> aspen_v6_1_block_E101
aspen_v6_1_stream_4 --fromBlock--> aspen_v6_1_block_E101
E101 --pipedTo--> RV400
E101 --floor--> 1
E101 --note--> Lean MEA enters at the top through NRV400; rich MEA leaves from the sump to J101a/b. The air admittance valve shown on the P&ID has been removed from the plant (DIFF, E14/15).
E101 --feedsInto--> E101_N_sump_outlet
E101 --designBasis--> Packing and column designed for 2.3-2.5 bar operation on MEA and 50 kg/h CO2 (HAZOP 10.4)
E101 --feedsInto--> E101_N_gas_outlet
E101 --pipedTo--> E101_N_sump_outlet
E101 --pipedTo--> E101_N_gas_outlet
E101 --type--> AbsorptionColumn
E101 --diameter_mm--> 230.0
E101 --tag--> E101
E101 --label--> E101 absorber
HAZOP_7_10 --concerns--> E101
TT305 --monitors--> E101
PT111 --monitors--> E101
E101_sample_5 --onColumn--> E101
E101_N_gas_outlet --onEquipment--> E101
LSLL109 --monitors--> E101
TT207 --monitors--> E101
PT403 --monitors--> E101
LI108 --monitors--> E101
E101_sample_4 --onColumn--> E101
E101_N_sump_outlet --onEquipment--> E101
FT109 --monitors--> E101
E101_sample_3 --onColumn--> E101
HAZOP_9b_05 --concerns--> E101
limit_LZAL109 --appliesTo--> E101
DI108 --monitors--> E101
E101_N_gas_inlet --feedsInto--> E101
FT304 --monitors--> E101
LT108 --monitors--> E101
K101_N2_recycle --bypasses--> E101
PT110 --monitors--> E101
E101_N_gas_inlet --pipedTo--> E101
HAZOP_5_08 --concerns--> E101
HAZOP_8_01 --concerns--> E101
HAZOP_8_06 --concerns--> E101
PI403 --monitors--> E101
AT400 --monitors--> E101
FT303 --monitors--> E101
TT205 --monitors--> E101
E101_N_base_inlet --onEquipment--> E101
aspen_v6_1_E101_performance --ofEquipment--> E101
TT206 --monitors--> E101
HAZOP_8_03 --concerns--> E101
E101_N_gas_inlet --onEquipment--> E101
E101_N_top_inlet --feedsInto--> E101
E101_sample_6 --onColumn--> E101
K402 --pipedTo--> E101
HAZOP_5_07 --concerns--> E101
AI300 --monitors--> E101
FI109 --monitors--> E101
FI108 --monitors--> E101
aspen_v3_vent_gas --ofEquipment--> E101
AT300 --monitors--> E101
E101_N_top_inlet --pipedTo--> E101
aspen_v6_1_feed_gas --ofEquipment--> E101
limit_PSHH117_set --appliesTo--> E101
TT109 --monitors--> E101
TT412 --monitors--> E101
HAZOP_10_03 --concerns--> E101
LSHH107 --monitors--> E101
E101_sample_2 --onColumn--> E101
limit_LZAH107 --appliesTo--> E101
HAZOP_5_06 --concerns--> E101
PSHH117 --monitors--> E101
TT413 --monitors--> E101
HAZOP_7_13 --concerns--> E101
TT107 --monitors--> E101
TT306 --monitors--> E101
E101_N_top_inlet --onEquipment--> E101
E101_sample_1 --onColumn--> E101
AOI10 --about--> E101
RV400 --protects--> E101
FT108 --monitors--> E101
TT411 --monitors--> E101
TT204 --monitors--> E101
aspen_v3_feed_gas --ofEquipment--> E101
HAZOP_element_10 --covers--> E101
HAZOP_8_11 --concerns--> E101
TT307 --monitors--> E101
TT308 --monitors--> E101
HAZOP_8_02 --concerns--> E101
aspen_v3_E101_performance --ofEquipment--> E101
PCV300 --valveType--> pressure control
PCV300 --floor--> 3
PCV300 --normalPosition--> open
PCV300 --note--> Vents lean gas from the absorber to hold the E101 pressure (PIC403). Opened in the vent stream start-up (Fig F.3), closed at shutdown.
PCV300 --pipedTo--> VENT_E101
PCV300 --label--> PCV300
PCV300 --feedsInto--> VENT_E101
PCV300 --type--> PressureControlValve
PCV300 --tag--> PCV300
PCV300 --gridReference--> G18
K402 --feedsInto--> PCV300
CL_E101_pressure --hasFinalElement--> PCV300
K402 --pipedTo--> PCV300
PIC403 --controls--> PCV300
AV01 --about--> PCV300
K101 --type--> Saturator
K101 --label--> K101 gas saturator
K101 --pipedTo--> SDV170
K101 --pipedTo--> Z103
K101 --floor--> 1
K101 --feedsInto--> E101_N_gas_inlet
K101 --pipedTo--> E101_N_gas_inlet
K101 --note--> Saturates the feed gas with water before E101; temperature held by TIC121 using C106 on the recirculating water. Grid not in the REPORT lists (near L17 to L18 on the P&ID). Not modelled in Aspen (GOI09).
K101 --pipedTo--> V126
K101 --tag--> K101
DI_CARTRIDGE --feedsInto--> K101
HAZOP_4_06 --concerns--> K101
V172 --pipedTo--> K101
J102 --pipedTo--> K101
limit_LZAL_K101 --appliesTo--> K101
HAZOP_4_07 --concerns--> K101
LT104 --monitors--> K101
HAZOP_3_05 --concerns--> K101
FEED_GAS_HEADER --feedsInto--> K101
GOI09 --about--> K101
LI106 --monitors--> K101
FEED_GAS_HEADER --pipedTo--> K101
limit_LAL_K101 --appliesTo--> K101
K101_N2_recycle --fromItem--> K101
limit_LZAH_K101 --appliesTo--> K101
GOI07 --about--> K101
GOI02 --about--> K101
HAZOP_element_3 --covers--> K101
HAZOP_4_02 --concerns--> K101
TI121 --monitors--> K101
C106 --pipedTo--> K101
```

Question: How is gas from the absorber connected to the controlled venting system?

## Q27

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
aspen_v6_1_block_E100 --inCase--> case_aspen_v6_1
aspen_v6_1_block_E100 --statusMessage--> RATESEP CALCULATIONS FAILED TO CONVERGE.
aspen_v6_1_block_E100 --status--> ERROR
aspen_v6_1_block_E100 --represents--> E100
aspen_v6_1_block_E100 --label--> E100 (ABB_pilot_plant_final_6_1_SA_validation)
aspen_v6_1_block_E100 --type--> AspenBlock
aspen_v6_1_block_E100 --blockId--> E100
aspen_v6_1_block_E100 --aspenModel--> RADFRAC
aspen_v6_1_stream_S15 --fromBlock--> aspen_v6_1_block_E100
aspen_v6_1_stream_S23 --fromBlock--> aspen_v6_1_block_E100
aspen_v6_1_stream_S10 --toBlock--> aspen_v6_1_block_E100
aspen_v6_1_stream_S12 --fromBlock--> aspen_v6_1_block_E100
aspen_v6_1_stream_S14 --toBlock--> aspen_v6_1_block_E100
aspen_v3_block_E100 --label--> E100 (ABB_pilot_plant_final_3)
aspen_v3_block_E100 --represents--> E100
aspen_v3_block_E100 --aspenModel--> RADFRAC
aspen_v3_block_E100 --inCase--> case_aspen_v3
aspen_v3_block_E100 --status--> WARNING
aspen_v3_block_E100 --statusMessage--> FEED PRESSURE IS LOWER THAN STAGE PRESSURE.
aspen_v3_block_E100 --type--> AspenBlock
aspen_v3_block_E100 --blockId--> E100
aspen_v3_stream_S13 --fromBlock--> aspen_v3_block_E100
aspen_v3_stream_S10 --toBlock--> aspen_v3_block_E100
aspen_v3_stream_S6 --fromBlock--> aspen_v3_block_E100
aspen_v3_stream_S14 --fromBlock--> aspen_v3_block_E100
aspen_v3_stream_S24 --toBlock--> aspen_v3_block_E100
aspen_v3_block_E101 --type--> AspenBlock
aspen_v3_block_E101 --aspenModel--> RADFRAC
aspen_v3_block_E101 --blockId--> E101
aspen_v3_block_E101 --status--> OK
aspen_v3_block_E101 --label--> E101 (ABB_pilot_plant_final_3)
aspen_v3_block_E101 --inCase--> case_aspen_v3
aspen_v3_stream_S8 --fromBlock--> aspen_v3_block_E101
aspen_v3_stream_1 --toBlock--> aspen_v3_block_E101
aspen_v3_stream_2 --toBlock--> aspen_v3_block_E101
aspen_v3_stream_4 --fromBlock--> aspen_v3_block_E101
E100 --floor--> 1
E100 --hasStage--> E100_stage_12
E100 --diameter_mm--> 264.62
E100 --tag--> E100
E100 --label--> E100 stripper (desorber)
E100 --hasStage--> E100_stage_08
E100 --hasStage--> E100_stage_01
E100 --hasStage--> E100_stage_04
E100 --feedsInto--> E100_N_overhead
E100 --hasStage--> E100_stage_07
E100 --pipedTo--> E100_N_overhead
E100 --note--> Chimney tray below the bottom packed bed separates the draw-off section (stage 11) from the sump (stage 12).
E100 --hasStage--> E100_stage_02
E100 --hasStage--> E100_stage_09
E100 --feedsInto--> E100_N_sump_outlet
E100 --hasStage--> E100_stage_06
E100 --feedsInto--> E100_N_drawoff
E100 --pipedTo--> E100_N_sump_outlet
E100 --hasStage--> E100_stage_05
E100 --hasStage--> E100_stage_11
E100 --hasStage--> E100_stage_10
E100 --designBasis--> Designed for sub-atmospheric pressure (vacuum), per HAZOP element 11 item 10. Design pressure value not documented.
E100 --hasStage--> E100_stage_03
E100 --pipedTo--> E100_N_drawoff
E100 --type--> StrippingColumn
TT200 --monitors--> E100
PI401 --monitors--> E100
TT401 --monitors--> E100
PROC_reboiler_heating_step_06 --operatesOn--> E100
HAZOP_13_13 --concerns--> E100
HAZOP_11_13 --concerns--> E100
LT101 --monitors--> E100
E100_N_sump_outlet --onEquipment--> E100
LSLL102 --monitors--> E100
HAZOP_11_12 --concerns--> E100
OI06 --about--> E100
LSHH100 --monitors--> E100
aspen_v6_1_E100_performance --ofEquipment--> E100
E100_N_overhead --onEquipment--> E100
TT302 --monitors--> E100
HAZOP_7_10 --concerns--> E100
HAZOP_6_07 --concerns--> E100
HAZOP_11_15 --concerns--> E100
E100_N_top_inlet --feedsInto--> E100
PT402 --monitors--> E100
PT401 --monitors--> E100
E100_N_drawoff --onEquipment--> E100
E100_N_side_inlet --onEquipment--> E100
limit_LT101_operating_window --appliesTo--> E100
limit_LZAH100 --appliesTo--> E100
HAZOP_9b_05 --concerns--> E100
RV401 --protects--> E100
E100_N_top_inlet --pipedTo--> E100
E100_N_top_inlet --onEquipment--> E100
HAZOP_13_12 --concerns--> E100
aspen_v3_E100_performance --ofEquipment--> E100
TT301 --monitors--> E100
TT400 --monitors--> E100
HAZOP_7_15 --concerns--> E100
HAZOP_element_11 --covers--> E100
limit_LT101_low_alarm --appliesTo--> E100
TT303 --monitors--> E100
OI11 --about--> E100
limit_PSHH116_set --appliesTo--> E100
HAZOP_13_11 --concerns--> E100
E100_N_reboiler_return --feedsInto--> E100
limit_PSHH400_set --appliesTo--> E100
OI03 --about--> E100
TT103 --monitors--> E100
PSHH400 --monitors--> E100
E100_N_reboiler_return --pipedTo--> E100
HAZOP_8_01 --concerns--> E100
PT102 --monitors--> E100
PSHH116 --monitors--> E100
TT203 --monitors--> E100
limit_LZAL102 --appliesTo--> E100
TT201 --monitors--> E100
HAZOP_6_08 --concerns--> E100
TT300 --monitors--> E100
HAZOP_11_01 --concerns--> E100
E100_N_reboiler_return --onEquipment--> E100
TT202 --monitors--> E100
aspen_v6_1_block_E101 --type--> AspenBlock
aspen_v6_1_block_E101 --aspenModel--> RADFRAC
aspen_v6_1_block_E101 --label--> E101 (ABB_pilot_plant_final_6_1_SA_validation)
aspen_v6_1_block_E101 --blockId--> E101
aspen_v6_1_block_E101 --status--> OK
aspen_v6_1_block_E101 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S8 --fromBlock--> aspen_v6_1_block_E101
aspen_v6_1_stream_2 --toBlock--> aspen_v6_1_block_E101
aspen_v6_1_stream_1 --toBlock--> aspen_v6_1_block_E101
aspen_v6_1_stream_4 --fromBlock--> aspen_v6_1_block_E101
E101 --pipedTo--> RV400
E101 --floor--> 1
E101 --note--> Lean MEA enters at the top through NRV400; rich MEA leaves from the sump to J101a/b. The air admittance valve shown on the P&ID has been removed from the plant (DIFF, E14/15).
E101 --feedsInto--> E101_N_sump_outlet
E101 --designBasis--> Packing and column designed for 2.3-2.5 bar operation on MEA and 50 kg/h CO2 (HAZOP 10.4)
E101 --feedsInto--> E101_N_gas_outlet
E101 --pipedTo--> E101_N_sump_outlet
E101 --pipedTo--> E101_N_gas_outlet
E101 --type--> AbsorptionColumn
E101 --diameter_mm--> 230.0
E101 --tag--> E101
E101 --label--> E101 absorber
HAZOP_7_10 --concerns--> E101
TT305 --monitors--> E101
PT111 --monitors--> E101
E101_sample_5 --onColumn--> E101
E101_N_gas_outlet --onEquipment--> E101
LSLL109 --monitors--> E101
TT207 --monitors--> E101
PT403 --monitors--> E101
LI108 --monitors--> E101
E101_sample_4 --onColumn--> E101
```

Question: Starting with the flow measurement, which control chain adjusts lean MEA flow from E100 into E101?

## Q28

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
aspen_v3_block_E100 --label--> E100 (ABB_pilot_plant_final_3)
aspen_v3_block_E100 --represents--> E100
aspen_v3_block_E100 --aspenModel--> RADFRAC
aspen_v3_block_E100 --inCase--> case_aspen_v3
aspen_v3_block_E100 --status--> WARNING
aspen_v3_block_E100 --statusMessage--> FEED PRESSURE IS LOWER THAN STAGE PRESSURE.
aspen_v3_block_E100 --type--> AspenBlock
aspen_v3_block_E100 --blockId--> E100
aspen_v3_stream_S13 --fromBlock--> aspen_v3_block_E100
aspen_v3_stream_S10 --toBlock--> aspen_v3_block_E100
aspen_v3_stream_S6 --fromBlock--> aspen_v3_block_E100
aspen_v3_stream_S14 --fromBlock--> aspen_v3_block_E100
aspen_v3_stream_S24 --toBlock--> aspen_v3_block_E100
aspen_v6_1_block_E100 --inCase--> case_aspen_v6_1
aspen_v6_1_block_E100 --statusMessage--> RATESEP CALCULATIONS FAILED TO CONVERGE.
aspen_v6_1_block_E100 --status--> ERROR
aspen_v6_1_block_E100 --represents--> E100
aspen_v6_1_block_E100 --label--> E100 (ABB_pilot_plant_final_6_1_SA_validation)
aspen_v6_1_block_E100 --type--> AspenBlock
aspen_v6_1_block_E100 --blockId--> E100
aspen_v6_1_block_E100 --aspenModel--> RADFRAC
aspen_v6_1_stream_S15 --fromBlock--> aspen_v6_1_block_E100
aspen_v6_1_stream_S23 --fromBlock--> aspen_v6_1_block_E100
aspen_v6_1_stream_S10 --toBlock--> aspen_v6_1_block_E100
aspen_v6_1_stream_S12 --fromBlock--> aspen_v6_1_block_E100
aspen_v6_1_stream_S14 --toBlock--> aspen_v6_1_block_E100
J101b --floor--> 1
J101b --pipedTo--> PCV120b
J101b --type--> Pump
J101b --gridReference--> N16
J101b --label--> J101b rich MEA pump (duty or standby)
J101b --tag--> J101b
J101b --note--> Parallel to J101a; only one runs at a time.
J101b --feedsInto--> PCV120b
ROI03 --about--> J101b
LIC108 --controls--> J101b
CL_E101_level --hasFinalElement--> J101b
IL_E101_level_LL --tripsItem--> J101b
AOI04 --about--> J101b
PROC_J101b_startup_step_07 --operatesOn--> J101b
TT111b --monitors--> J101b
PT115b --monitors--> J101b
HAZOP_element_8 --covers--> J101b
V135b --feedsInto--> J101b
IL_E101_level_HH --tripsItem--> J101b
TT110b --monitors--> J101b
V135b --pipedTo--> J101b
AOI09 --about--> J101b
PROC_J101a_startup_step_01 --operatesOn--> J101b
PROC_J101b_startup_step_02 --operatesOn--> J101b
SIC101b --controls--> J101b
AOI02 --about--> J101b
E100 --floor--> 1
E100 --hasStage--> E100_stage_12
E100 --diameter_mm--> 264.62
E100 --tag--> E100
E100 --label--> E100 stripper (desorber)
E100 --hasStage--> E100_stage_08
E100 --hasStage--> E100_stage_01
E100 --hasStage--> E100_stage_04
E100 --feedsInto--> E100_N_overhead
E100 --hasStage--> E100_stage_07
E100 --pipedTo--> E100_N_overhead
E100 --note--> Chimney tray below the bottom packed bed separates the draw-off section (stage 11) from the sump (stage 12).
E100 --hasStage--> E100_stage_02
E100 --hasStage--> E100_stage_09
E100 --feedsInto--> E100_N_sump_outlet
E100 --hasStage--> E100_stage_06
E100 --feedsInto--> E100_N_drawoff
E100 --pipedTo--> E100_N_sump_outlet
E100 --hasStage--> E100_stage_05
E100 --hasStage--> E100_stage_11
E100 --hasStage--> E100_stage_10
E100 --designBasis--> Designed for sub-atmospheric pressure (vacuum), per HAZOP element 11 item 10. Design pressure value not documented.
E100 --hasStage--> E100_stage_03
E100 --pipedTo--> E100_N_drawoff
E100 --type--> StrippingColumn
TT200 --monitors--> E100
PI401 --monitors--> E100
TT401 --monitors--> E100
PROC_reboiler_heating_step_06 --operatesOn--> E100
HAZOP_13_13 --concerns--> E100
HAZOP_11_13 --concerns--> E100
LT101 --monitors--> E100
E100_N_sump_outlet --onEquipment--> E100
LSLL102 --monitors--> E100
HAZOP_11_12 --concerns--> E100
OI06 --about--> E100
LSHH100 --monitors--> E100
aspen_v6_1_E100_performance --ofEquipment--> E100
E100_N_overhead --onEquipment--> E100
TT302 --monitors--> E100
HAZOP_7_10 --concerns--> E100
HAZOP_6_07 --concerns--> E100
HAZOP_11_15 --concerns--> E100
E100_N_top_inlet --feedsInto--> E100
PT402 --monitors--> E100
PT401 --monitors--> E100
E100_N_drawoff --onEquipment--> E100
E100_N_side_inlet --onEquipment--> E100
limit_LT101_operating_window --appliesTo--> E100
limit_LZAH100 --appliesTo--> E100
HAZOP_9b_05 --concerns--> E100
RV401 --protects--> E100
E100_N_top_inlet --pipedTo--> E100
E100_N_top_inlet --onEquipment--> E100
HAZOP_13_12 --concerns--> E100
aspen_v3_E100_performance --ofEquipment--> E100
TT301 --monitors--> E100
TT400 --monitors--> E100
HAZOP_7_15 --concerns--> E100
HAZOP_element_11 --covers--> E100
limit_LT101_low_alarm --appliesTo--> E100
TT303 --monitors--> E100
OI11 --about--> E100
limit_PSHH116_set --appliesTo--> E100
HAZOP_13_11 --concerns--> E100
E100_N_reboiler_return --feedsInto--> E100
limit_PSHH400_set --appliesTo--> E100
OI03 --about--> E100
TT103 --monitors--> E100
PSHH400 --monitors--> E100
E100_N_reboiler_return --pipedTo--> E100
HAZOP_8_01 --concerns--> E100
PT102 --monitors--> E100
PSHH116 --monitors--> E100
TT203 --monitors--> E100
limit_LZAL102 --appliesTo--> E100
TT201 --monitors--> E100
HAZOP_6_08 --concerns--> E100
TT300 --monitors--> E100
HAZOP_11_01 --concerns--> E100
E100_N_reboiler_return --onEquipment--> E100
TT202 --monitors--> E100
LSHH100 --tag--> LSHH100
LSHH100 --note--> Stage mapping inferred: odd Aspen stages are the gaps between packed beds where the side instruments sit; floors match REPORT.
LSHH100 --locatedAtStage--> E100_stage_12
LSHH100 --type--> LevelInstrument
LSHH100 --measuredVariable--> level high-high switch
LSHH100 --floor--> 1
LSHH100 --label--> LSHH100
IL_E100_level_HH --initiatedBy--> LSHH100
IL_E101_level_HH --initiatedBy--> LSHH107
IL_E101_level_HH --tripsItem--> J101a
IL_E101_level_HH --label--> E101 high-high level plant shutdown (LZAH107)
IL_E101_level_HH --type--> Interlock
PT402 --tag--> PT402
PT402 --monitors--> K401
PT402 --measuredVariable--> pressure after K401
PT402 --gridReference--> C16
```

Question: If J101b is the active rich MEA pump, how does the system measure and adjust the flow towards E100?

## Q29

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
aspen_v3_block_E101 --type--> AspenBlock
aspen_v3_block_E101 --aspenModel--> RADFRAC
aspen_v3_block_E101 --blockId--> E101
aspen_v3_block_E101 --status--> OK
aspen_v3_block_E101 --label--> E101 (ABB_pilot_plant_final_3)
aspen_v3_block_E101 --inCase--> case_aspen_v3
aspen_v3_stream_S8 --fromBlock--> aspen_v3_block_E101
aspen_v3_stream_1 --toBlock--> aspen_v3_block_E101
aspen_v3_stream_2 --toBlock--> aspen_v3_block_E101
aspen_v3_stream_4 --fromBlock--> aspen_v3_block_E101
aspen_v6_1_block_E101 --type--> AspenBlock
aspen_v6_1_block_E101 --aspenModel--> RADFRAC
aspen_v6_1_block_E101 --label--> E101 (ABB_pilot_plant_final_6_1_SA_validation)
aspen_v6_1_block_E101 --blockId--> E101
aspen_v6_1_block_E101 --status--> OK
aspen_v6_1_block_E101 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S8 --fromBlock--> aspen_v6_1_block_E101
aspen_v6_1_stream_2 --toBlock--> aspen_v6_1_block_E101
aspen_v6_1_stream_1 --toBlock--> aspen_v6_1_block_E101
aspen_v6_1_stream_4 --fromBlock--> aspen_v6_1_block_E101
E101 --pipedTo--> RV400
E101 --floor--> 1
E101 --note--> Lean MEA enters at the top through NRV400; rich MEA leaves from the sump to J101a/b. The air admittance valve shown on the P&ID has been removed from the plant (DIFF, E14/15).
E101 --feedsInto--> E101_N_sump_outlet
E101 --designBasis--> Packing and column designed for 2.3-2.5 bar operation on MEA and 50 kg/h CO2 (HAZOP 10.4)
E101 --feedsInto--> E101_N_gas_outlet
E101 --pipedTo--> E101_N_sump_outlet
E101 --pipedTo--> E101_N_gas_outlet
E101 --type--> AbsorptionColumn
E101 --diameter_mm--> 230.0
E101 --tag--> E101
E101 --label--> E101 absorber
HAZOP_7_10 --concerns--> E101
TT305 --monitors--> E101
PT111 --monitors--> E101
E101_sample_5 --onColumn--> E101
E101_N_gas_outlet --onEquipment--> E101
LSLL109 --monitors--> E101
TT207 --monitors--> E101
PT403 --monitors--> E101
LI108 --monitors--> E101
E101_sample_4 --onColumn--> E101
E101_N_sump_outlet --onEquipment--> E101
FT109 --monitors--> E101
E101_sample_3 --onColumn--> E101
HAZOP_9b_05 --concerns--> E101
limit_LZAL109 --appliesTo--> E101
DI108 --monitors--> E101
E101_N_gas_inlet --feedsInto--> E101
FT304 --monitors--> E101
LT108 --monitors--> E101
K101_N2_recycle --bypasses--> E101
PT110 --monitors--> E101
E101_N_gas_inlet --pipedTo--> E101
HAZOP_5_08 --concerns--> E101
HAZOP_8_01 --concerns--> E101
HAZOP_8_06 --concerns--> E101
PI403 --monitors--> E101
AT400 --monitors--> E101
FT303 --monitors--> E101
TT205 --monitors--> E101
E101_N_base_inlet --onEquipment--> E101
aspen_v6_1_E101_performance --ofEquipment--> E101
TT206 --monitors--> E101
HAZOP_8_03 --concerns--> E101
E101_N_gas_inlet --onEquipment--> E101
E101_N_top_inlet --feedsInto--> E101
E101_sample_6 --onColumn--> E101
K402 --pipedTo--> E101
HAZOP_5_07 --concerns--> E101
AI300 --monitors--> E101
FI109 --monitors--> E101
FI108 --monitors--> E101
aspen_v3_vent_gas --ofEquipment--> E101
AT300 --monitors--> E101
E101_N_top_inlet --pipedTo--> E101
aspen_v6_1_feed_gas --ofEquipment--> E101
limit_PSHH117_set --appliesTo--> E101
TT109 --monitors--> E101
TT412 --monitors--> E101
HAZOP_10_03 --concerns--> E101
LSHH107 --monitors--> E101
E101_sample_2 --onColumn--> E101
limit_LZAH107 --appliesTo--> E101
HAZOP_5_06 --concerns--> E101
PSHH117 --monitors--> E101
TT413 --monitors--> E101
HAZOP_7_13 --concerns--> E101
TT107 --monitors--> E101
TT306 --monitors--> E101
E101_N_top_inlet --onEquipment--> E101
E101_sample_1 --onColumn--> E101
AOI10 --about--> E101
RV400 --protects--> E101
FT108 --monitors--> E101
TT411 --monitors--> E101
TT204 --monitors--> E101
aspen_v3_feed_gas --ofEquipment--> E101
HAZOP_element_10 --covers--> E101
HAZOP_8_11 --concerns--> E101
TT307 --monitors--> E101
TT308 --monitors--> E101
HAZOP_8_02 --concerns--> E101
aspen_v3_E101_performance --ofEquipment--> E101
PCV300 --valveType--> pressure control
PCV300 --floor--> 3
PCV300 --normalPosition--> open
PCV300 --note--> Vents lean gas from the absorber to hold the E101 pressure (PIC403). Opened in the vent stream start-up (Fig F.3), closed at shutdown.
PCV300 --pipedTo--> VENT_E101
PCV300 --label--> PCV300
PCV300 --feedsInto--> VENT_E101
PCV300 --type--> PressureControlValve
PCV300 --tag--> PCV300
PCV300 --gridReference--> G18
K402 --feedsInto--> PCV300
CL_E101_pressure --hasFinalElement--> PCV300
K402 --pipedTo--> PCV300
PIC403 --controls--> PCV300
AV01 --about--> PCV300
K101 --type--> Saturator
K101 --label--> K101 gas saturator
K101 --pipedTo--> SDV170
K101 --pipedTo--> Z103
K101 --floor--> 1
K101 --feedsInto--> E101_N_gas_inlet
K101 --pipedTo--> E101_N_gas_inlet
K101 --note--> Saturates the feed gas with water before E101; temperature held by TIC121 using C106 on the recirculating water. Grid not in the REPORT lists (near L17 to L18 on the P&ID). Not modelled in Aspen (GOI09).
K101 --pipedTo--> V126
K101 --tag--> K101
DI_CARTRIDGE --feedsInto--> K101
HAZOP_4_06 --concerns--> K101
V172 --pipedTo--> K101
J102 --pipedTo--> K101
limit_LZAL_K101 --appliesTo--> K101
HAZOP_4_07 --concerns--> K101
LT104 --monitors--> K101
HAZOP_3_05 --concerns--> K101
FEED_GAS_HEADER --feedsInto--> K101
GOI09 --about--> K101
LI106 --monitors--> K101
FEED_GAS_HEADER --pipedTo--> K101
limit_LAL_K101 --appliesTo--> K101
K101_N2_recycle --fromItem--> K101
limit_LZAH_K101 --appliesTo--> K101
GOI07 --about--> K101
GOI02 --about--> K101
HAZOP_element_3 --covers--> K101
HAZOP_4_02 --concerns--> K101
TI121 --monitors--> K101
C106 --pipedTo--> K101
```

Question: Which complete control chain responds when the lean MEA temperature entering E101 is above its set point?

## Q30

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
aspen_v6_1_block_E100 --inCase--> case_aspen_v6_1
aspen_v6_1_block_E100 --statusMessage--> RATESEP CALCULATIONS FAILED TO CONVERGE.
aspen_v6_1_block_E100 --status--> ERROR
aspen_v6_1_block_E100 --represents--> E100
aspen_v6_1_block_E100 --label--> E100 (ABB_pilot_plant_final_6_1_SA_validation)
aspen_v6_1_block_E100 --type--> AspenBlock
aspen_v6_1_block_E100 --blockId--> E100
aspen_v6_1_block_E100 --aspenModel--> RADFRAC
aspen_v6_1_stream_S15 --fromBlock--> aspen_v6_1_block_E100
aspen_v6_1_stream_S23 --fromBlock--> aspen_v6_1_block_E100
aspen_v6_1_stream_S10 --toBlock--> aspen_v6_1_block_E100
aspen_v6_1_stream_S12 --fromBlock--> aspen_v6_1_block_E100
aspen_v6_1_stream_S14 --toBlock--> aspen_v6_1_block_E100
aspen_v3_block_E100 --label--> E100 (ABB_pilot_plant_final_3)
aspen_v3_block_E100 --represents--> E100
aspen_v3_block_E100 --aspenModel--> RADFRAC
aspen_v3_block_E100 --inCase--> case_aspen_v3
aspen_v3_block_E100 --status--> WARNING
aspen_v3_block_E100 --statusMessage--> FEED PRESSURE IS LOWER THAN STAGE PRESSURE.
aspen_v3_block_E100 --type--> AspenBlock
aspen_v3_block_E100 --blockId--> E100
aspen_v3_stream_S13 --fromBlock--> aspen_v3_block_E100
aspen_v3_stream_S10 --toBlock--> aspen_v3_block_E100
aspen_v3_stream_S6 --fromBlock--> aspen_v3_block_E100
aspen_v3_stream_S14 --fromBlock--> aspen_v3_block_E100
aspen_v3_stream_S24 --toBlock--> aspen_v3_block_E100
E100 --floor--> 1
E100 --hasStage--> E100_stage_12
E100 --diameter_mm--> 264.62
E100 --tag--> E100
E100 --label--> E100 stripper (desorber)
E100 --hasStage--> E100_stage_08
E100 --hasStage--> E100_stage_01
E100 --hasStage--> E100_stage_04
E100 --feedsInto--> E100_N_overhead
E100 --hasStage--> E100_stage_07
E100 --pipedTo--> E100_N_overhead
E100 --note--> Chimney tray below the bottom packed bed separates the draw-off section (stage 11) from the sump (stage 12).
E100 --hasStage--> E100_stage_02
E100 --hasStage--> E100_stage_09
E100 --feedsInto--> E100_N_sump_outlet
E100 --hasStage--> E100_stage_06
E100 --feedsInto--> E100_N_drawoff
E100 --pipedTo--> E100_N_sump_outlet
E100 --hasStage--> E100_stage_05
E100 --hasStage--> E100_stage_11
E100 --hasStage--> E100_stage_10
E100 --designBasis--> Designed for sub-atmospheric pressure (vacuum), per HAZOP element 11 item 10. Design pressure value not documented.
E100 --hasStage--> E100_stage_03
E100 --pipedTo--> E100_N_drawoff
E100 --type--> StrippingColumn
TT200 --monitors--> E100
PI401 --monitors--> E100
TT401 --monitors--> E100
PROC_reboiler_heating_step_06 --operatesOn--> E100
HAZOP_13_13 --concerns--> E100
HAZOP_11_13 --concerns--> E100
LT101 --monitors--> E100
E100_N_sump_outlet --onEquipment--> E100
LSLL102 --monitors--> E100
HAZOP_11_12 --concerns--> E100
OI06 --about--> E100
LSHH100 --monitors--> E100
aspen_v6_1_E100_performance --ofEquipment--> E100
E100_N_overhead --onEquipment--> E100
TT302 --monitors--> E100
HAZOP_7_10 --concerns--> E100
HAZOP_6_07 --concerns--> E100
HAZOP_11_15 --concerns--> E100
E100_N_top_inlet --feedsInto--> E100
PT402 --monitors--> E100
PT401 --monitors--> E100
E100_N_drawoff --onEquipment--> E100
E100_N_side_inlet --onEquipment--> E100
limit_LT101_operating_window --appliesTo--> E100
limit_LZAH100 --appliesTo--> E100
HAZOP_9b_05 --concerns--> E100
RV401 --protects--> E100
E100_N_top_inlet --pipedTo--> E100
E100_N_top_inlet --onEquipment--> E100
HAZOP_13_12 --concerns--> E100
aspen_v3_E100_performance --ofEquipment--> E100
TT301 --monitors--> E100
TT400 --monitors--> E100
HAZOP_7_15 --concerns--> E100
HAZOP_element_11 --covers--> E100
limit_LT101_low_alarm --appliesTo--> E100
TT303 --monitors--> E100
OI11 --about--> E100
limit_PSHH116_set --appliesTo--> E100
HAZOP_13_11 --concerns--> E100
E100_N_reboiler_return --feedsInto--> E100
limit_PSHH400_set --appliesTo--> E100
OI03 --about--> E100
TT103 --monitors--> E100
PSHH400 --monitors--> E100
E100_N_reboiler_return --pipedTo--> E100
HAZOP_8_01 --concerns--> E100
PT102 --monitors--> E100
PSHH116 --monitors--> E100
TT203 --monitors--> E100
limit_LZAL102 --appliesTo--> E100
TT201 --monitors--> E100
HAZOP_6_08 --concerns--> E100
TT300 --monitors--> E100
HAZOP_11_01 --concerns--> E100
E100_N_reboiler_return --onEquipment--> E100
TT202 --monitors--> E100
H100 --tag--> H100
H100 --floor--> 1
H100 --source--> SUMMARY p.102
H100 --type--> SteamReboiler
H100 --feedsInto--> Q106
H100 --pipedTo--> Q106
H100 --label--> H100 vertical thermosiphon steam reboiler
FI102 --monitors--> H100
H100_N_condensate_out --onEquipment--> H100
TT100 --monitors--> H100
aspen_v3_H100_performance --ofEquipment--> H100
FT101 --monitors--> H100
HAZOP_element_13 --covers--> H100
aspen_v6_1_block_H100 --represents--> H100
TI100 --monitors--> H100
PROC_reboiler_heating_step_04 --operatesOn--> H100
DI100 --monitors--> H100
limit_H100_steam_limit --appliesTo--> H100
PI101 --monitors--> H100
PI100 --monitors--> H100
aspen_v3_block_H100REAC --represents--> H100
PT101 --monitors--> H100
FT102 --monitors--> H100
aspen_v3_block_H100HEAT --represents--> H100
TT117 --monitors--> H100
TT118 --monitors--> H100
FI100 --monitors--> H100
Q105 --pipedTo--> H100
H100_N_steam_in --onEquipment--> H100
Q105 --feedsInto--> H100
aspen_v6_1_H100_performance --ofEquipment--> H100
FT100 --monitors--> H100
HAZOP_element_11 --covers--> H100
RV107 --protects--> H100
aspen_v6_1_block_H100 --label--> H100 (ABB_pilot_plant_final_6_1_SA_validation)
aspen_v6_1_block_H100 --blockId--> H100
aspen_v6_1_block_H100 --aspenModel--> HEATX
aspen_v6_1_block_H100 --type--> AspenBlock
aspen_v6_1_block_H100 --statusMessage--> INVALID INPUT SPECIFICATIONS SEE TASC BROWSER FOR INFO.
aspen_v6_1_block_H100 --status--> ERROR
aspen_v6_1_block_H100 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S14 --fromBlock--> aspen_v6_1_block_H100
```

Question: Which linked instruments and controllers increase reboiler heating when the MEA temperature returning to E100 is too low?

## Q31

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
C400_N_cw_out__utlcit01 --location--> C400
C400_N_cw_out__utlcit01 --type--> Citation
C400_N_cw_out__utlcit01 --document--> SRC_PID
C400_N_cw_out__utlcit01 --citationText--> P&ID C400
C400_N_cw_out__utlcit01 --label--> Citation 1 for C400_N_cw_out (utl)
aspen_v3_block_C400 --inCase--> case_aspen_v3
aspen_v3_block_C400 --aspenModel--> HEATER
aspen_v3_block_C400 --type--> AspenBlock
aspen_v3_block_C400 --blockId--> C400
aspen_v3_block_C400 --status--> OK
aspen_v3_block_C400 --label--> C400 (ABB_pilot_plant_final_3)
aspen_v3_stream_S11 --fromBlock--> aspen_v3_block_C400
aspen_v3_stream_S13 --toBlock--> aspen_v3_block_C400
C400_N_cw_in__utlcit01 --type--> Citation
C400_N_cw_in__utlcit01 --document--> SRC_PID
C400_N_cw_in__utlcit01 --citationText--> P&ID C400
C400_N_cw_in__utlcit01 --label--> Citation 1 for C400_N_cw_in (utl)
C400_N_cw_in__utlcit01 --location--> C400
aspen_v6_1_block_C400 --aspenModel--> HEATER
aspen_v6_1_block_C400 --label--> C400 (ABB_pilot_plant_final_6_1_SA_validation)
aspen_v6_1_block_C400 --blockId--> C400
aspen_v6_1_block_C400 --inCase--> case_aspen_v6_1
aspen_v6_1_block_C400 --status--> OK
aspen_v6_1_block_C400 --type--> AspenBlock
aspen_v6_1_stream_S11 --fromBlock--> aspen_v6_1_block_C400
aspen_v6_1_stream_S15 --toBlock--> aspen_v6_1_block_C400
C400 --floor--> 4
C400 --pipedTo--> K401
C400 --type--> Condenser
C400 --label--> C400 overhead condenser (spiral heat exchanger)
C400 --tag--> C400
C400 --note--> Water-cooled; cooling water flow set by FIC402 on FCV401 (cascade from TIC410). Grid not in the REPORT lists (between C8 and E10 on the P&ID).
C400 --feedsInto--> K401
E100_N_overhead --pipedTo--> C400
OOI04 --about--> C400
HAZOP_12_07 --concerns--> C400
aspen_v3_C400_performance --ofEquipment--> C400
OOI06 --about--> C400
HAZOP_12_03 --concerns--> C400
FI402 --monitors--> C400
C400_N_cw_in --onEquipment--> C400
HAZOP_6_05 --concerns--> C400
HAZOP_6_01 --concerns--> C400
C400_N_cw_out --onEquipment--> C400
PT401 --monitors--> C400
HAZOP_element_12 --covers--> C400
TI410 --monitors--> C400
limit_TAH_C400_carryover --appliesTo--> C400
FI401 --monitors--> C400
FT402 --monitors--> C400
HAZOP_6_06 --concerns--> C400
E100_N_overhead --feedsInto--> C400
TT410 --monitors--> C400
E100_N_overhead --type--> Nozzle
E100_N_overhead --onEquipment--> E100
E100_N_overhead --label--> E100 vapour outlet at the top of the column
E100 --feedsInto--> E100_N_overhead
E100 --pipedTo--> E100_N_overhead
C400__ovhcit01 --label--> Citation 1 for C400 (ovh)
C400__ovhcit01 --type--> Citation
C400__ovhcit01 --location--> overhead line after PT401, top of the drawing
C400__ovhcit01 --document--> SRC_PID
C400__ovhcit01 --citationText--> P&ID overhead line after PT401, top of the drawing
PCV415 --pipedTo--> FCV401
PCV415 --normalPosition--> open
PCV415 --note--> Pressure regulator on the C400 cooling water stream (UT09). The valve list gives floor 3.
PCV415 --floor--> 4
PCV415 --type--> PressureControlValve
PCV415 --gridReference--> C14
PCV415 --tag--> PCV415
PCV415 --feedsInto--> FCV401
PCV415 --valveType--> pressure control
PCV415 --label--> PCV415
UT09 --about--> PCV415
V405 --feedsInto--> PCV415
V405 --pipedTo--> PCV415
TIC410 --type--> Controller
TIC410 --tag--> TIC410
TIC410 --label--> C400 gas outlet temperature controller (cascade master)
TIC410 --controls--> FCV401
CL_C400_temperature --hasController--> TIC410
OOI04 --description--> Aspen returns the reflux to the rich feed before the heaters (MIXER2), but on the P&ID it joins after them at V403/V402
OOI04 --foundBy--> ovh section build, Oct 2026
OOI04 --about--> J300
OOI04 --type--> OpenItem
OOI04 --resolvedBy--> Note for model comparison; update the Aspen flowsheet if needed
OOI04 --itemStatus--> open
OOI04 --label--> OOI04: Aspen returns the reflux to the rich feed before the heaters (MIXER2), but on the P&ID it joins after them at V403/V402
HAZOP_6_01 --actionTaken--> Pump shutdown trip added
HAZOP_6_01 --consequence--> No flow to J103
HAZOP_6_01 --concerns--> J103
HAZOP_6_01 --inElement--> HAZOP_element_6
HAZOP_6_01 --cause--> K401 / C300 (now C400) blocked
HAZOP_6_01 --guideword--> NO
HAZOP_6_01 --label--> HAZOP 6.1
HAZOP_6_01 --recommendedAction--> Consider consequences of starving J103
HAZOP_6_01 --parameter--> FLOW
HAZOP_6_01 --type--> HazopDeviation
HAZOP_6_01 --itemNumber--> 1
HAZOP_6_01 --concerns--> K401
TT410 --signalType--> Fieldbus
TT410 --measuredVariable--> temperature of CO2 leaving C400
TT410 --floor--> 4
TT410 --label--> TT410
TT410 --sensorType--> PRT
TT410 --tag--> TT410
TT410 --gridReference--> C15
TT410 --type--> TemperatureInstrument
CL_C400_temperature --hasSensor--> TT410
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_07_J300
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_14_FT305
OverheadRefluxLoop --label--> Stripper overhead and reflux loop
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_09_RV300
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_02_PT401
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_03_C400
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_10_B300
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_08_TT310
OverheadRefluxLoop --note--> Runs whenever E100 is boiling. Vapour is condensed in C400; K401 separates the condensate (returned as reflux by J300) from the CO2-rich gas (to the CO2 return, piece 7).
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_06_LT401
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_05_K401
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_17_E100_N_top_inlet
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_01_E100_N_overhead
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_15_V403
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_00_E100
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_16_V402
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_12_V317
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_13_TT309
OverheadRefluxLoop --type--> Loop
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_04_LSHH400
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_11_PCV302
OverheadRefluxLoop --inMode--> FigureOfEight
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_18_E100
C400__ovhcit03 --citationText--> P&ID differences row LSHH400 (between C400 and K401)
C400__ovhcit03 --location--> row LSHH400 (between C400 and K401)
C400__ovhcit03 --document--> SRC_DIFF
C400__ovhcit03 --label--> Citation 3 for C400 (ovh)
C400__ovhcit03 --type--> Citation
C400_N_cw_in --pipedTo--> C400_N_cw_out
C400_N_cw_in --label--> C400 cooling water inlet
C400_N_cw_in --type--> Nozzle
C400_N_cw_in --feedsInto--> C400_N_cw_out
FT402 --pipedTo--> C400_N_cw_in
FT402 --feedsInto--> C400_N_cw_in
CL_C400_cooling_water --hasFinalElement--> FCV401
CL_C400_cooling_water --controlledVariable--> Cooling water flowrate to C400
CL_C400_cooling_water --manipulatedVariable--> FCV401 opening
CL_C400_cooling_water --label--> Cooling water flow to C400 (cascade slave)
CL_C400_cooling_water --hasController--> FIC402
CL_C400_cooling_water --hasSensor--> FT402
CL_C400_cooling_water --type--> ControlLoop
```

Question: Which instruments link a high temperature in the C400 overhead cooling system to an increase in cooling water flow?

## Q32

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
aspen_v3_block_E101 --type--> AspenBlock
aspen_v3_block_E101 --aspenModel--> RADFRAC
aspen_v3_block_E101 --blockId--> E101
aspen_v3_block_E101 --status--> OK
aspen_v3_block_E101 --label--> E101 (ABB_pilot_plant_final_3)
aspen_v3_block_E101 --inCase--> case_aspen_v3
aspen_v3_stream_S8 --fromBlock--> aspen_v3_block_E101
aspen_v3_stream_1 --toBlock--> aspen_v3_block_E101
aspen_v3_stream_2 --toBlock--> aspen_v3_block_E101
aspen_v3_stream_4 --fromBlock--> aspen_v3_block_E101
aspen_v6_1_block_E101 --type--> AspenBlock
aspen_v6_1_block_E101 --aspenModel--> RADFRAC
aspen_v6_1_block_E101 --label--> E101 (ABB_pilot_plant_final_6_1_SA_validation)
aspen_v6_1_block_E101 --blockId--> E101
aspen_v6_1_block_E101 --status--> OK
aspen_v6_1_block_E101 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S8 --fromBlock--> aspen_v6_1_block_E101
aspen_v6_1_stream_2 --toBlock--> aspen_v6_1_block_E101
aspen_v6_1_stream_1 --toBlock--> aspen_v6_1_block_E101
aspen_v6_1_stream_4 --fromBlock--> aspen_v6_1_block_E101
E101 --pipedTo--> RV400
E101 --floor--> 1
E101 --note--> Lean MEA enters at the top through NRV400; rich MEA leaves from the sump to J101a/b. The air admittance valve shown on the P&ID has been removed from the plant (DIFF, E14/15).
E101 --feedsInto--> E101_N_sump_outlet
E101 --designBasis--> Packing and column designed for 2.3-2.5 bar operation on MEA and 50 kg/h CO2 (HAZOP 10.4)
E101 --feedsInto--> E101_N_gas_outlet
E101 --pipedTo--> E101_N_sump_outlet
E101 --pipedTo--> E101_N_gas_outlet
E101 --type--> AbsorptionColumn
E101 --diameter_mm--> 230.0
E101 --tag--> E101
E101 --label--> E101 absorber
HAZOP_7_10 --concerns--> E101
TT305 --monitors--> E101
PT111 --monitors--> E101
E101_sample_5 --onColumn--> E101
E101_N_gas_outlet --onEquipment--> E101
LSLL109 --monitors--> E101
TT207 --monitors--> E101
PT403 --monitors--> E101
LI108 --monitors--> E101
E101_sample_4 --onColumn--> E101
E101_N_sump_outlet --onEquipment--> E101
FT109 --monitors--> E101
E101_sample_3 --onColumn--> E101
HAZOP_9b_05 --concerns--> E101
limit_LZAL109 --appliesTo--> E101
DI108 --monitors--> E101
E101_N_gas_inlet --feedsInto--> E101
FT304 --monitors--> E101
LT108 --monitors--> E101
K101_N2_recycle --bypasses--> E101
PT110 --monitors--> E101
E101_N_gas_inlet --pipedTo--> E101
HAZOP_5_08 --concerns--> E101
HAZOP_8_01 --concerns--> E101
HAZOP_8_06 --concerns--> E101
PI403 --monitors--> E101
AT400 --monitors--> E101
FT303 --monitors--> E101
TT205 --monitors--> E101
E101_N_base_inlet --onEquipment--> E101
aspen_v6_1_E101_performance --ofEquipment--> E101
TT206 --monitors--> E101
HAZOP_8_03 --concerns--> E101
E101_N_gas_inlet --onEquipment--> E101
E101_N_top_inlet --feedsInto--> E101
E101_sample_6 --onColumn--> E101
K402 --pipedTo--> E101
HAZOP_5_07 --concerns--> E101
AI300 --monitors--> E101
FI109 --monitors--> E101
FI108 --monitors--> E101
aspen_v3_vent_gas --ofEquipment--> E101
AT300 --monitors--> E101
E101_N_top_inlet --pipedTo--> E101
aspen_v6_1_feed_gas --ofEquipment--> E101
limit_PSHH117_set --appliesTo--> E101
TT109 --monitors--> E101
TT412 --monitors--> E101
HAZOP_10_03 --concerns--> E101
LSHH107 --monitors--> E101
E101_sample_2 --onColumn--> E101
limit_LZAH107 --appliesTo--> E101
HAZOP_5_06 --concerns--> E101
PSHH117 --monitors--> E101
TT413 --monitors--> E101
HAZOP_7_13 --concerns--> E101
TT107 --monitors--> E101
TT306 --monitors--> E101
E101_N_top_inlet --onEquipment--> E101
E101_sample_1 --onColumn--> E101
AOI10 --about--> E101
RV400 --protects--> E101
FT108 --monitors--> E101
TT411 --monitors--> E101
TT204 --monitors--> E101
aspen_v3_feed_gas --ofEquipment--> E101
HAZOP_element_10 --covers--> E101
HAZOP_8_11 --concerns--> E101
TT307 --monitors--> E101
TT308 --monitors--> E101
HAZOP_8_02 --concerns--> E101
aspen_v3_E101_performance --ofEquipment--> E101
PCV300 --valveType--> pressure control
PCV300 --floor--> 3
PCV300 --normalPosition--> open
PCV300 --note--> Vents lean gas from the absorber to hold the E101 pressure (PIC403). Opened in the vent stream start-up (Fig F.3), closed at shutdown.
PCV300 --pipedTo--> VENT_E101
PCV300 --label--> PCV300
PCV300 --feedsInto--> VENT_E101
PCV300 --type--> PressureControlValve
PCV300 --tag--> PCV300
PCV300 --gridReference--> G18
K402 --feedsInto--> PCV300
CL_E101_pressure --hasFinalElement--> PCV300
K402 --pipedTo--> PCV300
PIC403 --controls--> PCV300
AV01 --about--> PCV300
K101 --type--> Saturator
K101 --label--> K101 gas saturator
K101 --pipedTo--> SDV170
K101 --pipedTo--> Z103
K101 --floor--> 1
K101 --feedsInto--> E101_N_gas_inlet
K101 --pipedTo--> E101_N_gas_inlet
K101 --note--> Saturates the feed gas with water before E101; temperature held by TIC121 using C106 on the recirculating water. Grid not in the REPORT lists (near L17 to L18 on the P&ID). Not modelled in Aspen (GOI09).
K101 --pipedTo--> V126
K101 --tag--> K101
DI_CARTRIDGE --feedsInto--> K101
HAZOP_4_06 --concerns--> K101
V172 --pipedTo--> K101
J102 --pipedTo--> K101
limit_LZAL_K101 --appliesTo--> K101
HAZOP_4_07 --concerns--> K101
LT104 --monitors--> K101
HAZOP_3_05 --concerns--> K101
FEED_GAS_HEADER --feedsInto--> K101
GOI09 --about--> K101
LI106 --monitors--> K101
FEED_GAS_HEADER --pipedTo--> K101
limit_LAL_K101 --appliesTo--> K101
K101_N2_recycle --fromItem--> K101
limit_LZAH_K101 --appliesTo--> K101
GOI07 --about--> K101
GOI02 --about--> K101
HAZOP_element_3 --covers--> K101
HAZOP_4_02 --concerns--> K101
TI121 --monitors--> K101
C106 --pipedTo--> K101
```

Question: Which measurement, controller and actuator are linked to the pressure of E101?

## Q33

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
PCV119 --type--> PressureControlValve
PCV119 --gridReference--> K19
PCV119 --label--> PCV119
PCV119 --floor--> 1
PCV119 --tag--> PCV119
PCV119 --note--> E100 pressure control valve on the overhead line (boundary of the loop).
PCV119 --pipedTo--> K103
PCV119 --pipedTo--> VENT_SYSTEM
PCV119 --valveType--> pressure control
PCV119 --normalPosition--> open
K103_CO2_recycle --routeVia--> PCV119
GR07 --about--> PCV119
CL_E100_pressure --hasFinalElement--> PCV119
PIC401 --controls--> PCV119
HAZOP_element_6 --covers--> PCV119
PIC402 --controls--> PCV119
HAZOP_6_05 --concerns--> PCV119
J103 --pipedTo--> PCV119
GR07 --type--> OpenItem
GR07 --description--> PCV119 recycles CO2 back to K103 (REPORT D.4, team trace); it is also in the vent start-up table (Fig F.3) and a vent line runs above it: does it also vent?
GR07 --label--> GR07: PCV119 recycles CO2 back to K103 (REPORT D.4, team trace); it is also in the vent start-up table (Fig F.3) and a vent line runs above it: does it also vent?
GR07 --itemStatus--> open
GR07 --resolvedBy--> Trace on the P&ID
GR07 --foundBy--> grt section build, Oct 2026
J103 --pipedTo--> SDV171
J103 --tag--> J103
J103 --feedsInto--> SDV171
J103 --note--> Compresses the CO2 from K401 and returns it into K101 via SDV171 (team trace). A shutdown trip protects it if it is starved (HAZOP 6.1).
J103 --gridReference--> M20
J103 --label--> J103 CO2 return compressor (single-stage reciprocating, air-cooled)
J103 --type--> Compressor
J103 --floor--> 1
HAZOP_6_05 --concerns--> J103
HAZOP_6_01 --concerns--> J103
TT115 --monitors--> J103
K103_CO2_recycle --fromItem--> J103
PSHH118 --monitors--> J103
FT302 --monitors--> J103
HAZOP_6_02 --concerns--> J103
limit_TRIP_J103_starved --appliesTo--> J103
K103 --feedsInto--> J103
GR05 --about--> J103
K103 --pipedTo--> J103
HAZOP_6_09 --concerns--> J103
FT301 --monitors--> J103
HAZOP_element_6 --covers--> J103
GR10 --about--> J103
HAZOP_6_06 --concerns--> J103
VN01 --about--> V409
VN01 --type--> OpenItem
VN01 --label--> VN01: Fig F.3 lists PCV119, V190, V197, V209, PCV300, V315, SDV421, V409 and V411 on the vent stream: trace each one's line to its vent outlet (V197, V209 and V411 also appear in the cooling water tables, UT07)
VN01 --resolvedBy--> Trace on the P&ID
VN01 --itemStatus--> open
VN01 --about--> V315
VN01 --foundBy--> vnt section build, Oct 2026
VN01 --description--> Fig F.3 lists PCV119, V190, V197, V209, PCV300, V315, SDV421, V409 and V411 on the vent stream: trace each one's line to its vent outlet (V197, V209 and V411 also appear in the cooling water tables, UT07)
VN01 --about--> VENT_SYSTEM
HAZOP_element_6 --covers--> K103
HAZOP_element_6 --source--> HAZOP study, 6-7 May 2010 (27794_Plant_HAZREP_1.xls)
HAZOP_element_6 --elementNumber--> 6
HAZOP_element_6 --type--> HazopElement
HAZOP_element_6 --label--> HAZOP element 6: CO2 RETURN FROM K401 to E101 via J103
HAZOP_element_6 --covers--> K401
HAZOP_element_6 --covers--> FT301
HAZOP_element_6 --covers--> FT302
HAZOP_element_6 --covers--> SDV171
HAZOP_6_02 --inElement--> HAZOP_element_6
HAZOP_6_01 --inElement--> HAZOP_element_6
HAZOP_6_03 --inElement--> HAZOP_element_6
HAZOP_6_09 --inElement--> HAZOP_element_6
HAZOP_6_06 --inElement--> HAZOP_element_6
HAZOP_6_08 --inElement--> HAZOP_element_6
HAZOP_6_04 --inElement--> HAZOP_element_6
HAZOP_6_05 --inElement--> HAZOP_element_6
HAZOP_6_07 --inElement--> HAZOP_element_6
PIC402 --label--> E100 pressure controller
PIC402 --tag--> PIC402
PIC402 --type--> Controller
CL_E100_pressure --hasController--> PIC402
K103 --type--> KnockoutDrum
K103 --note--> Protects the J103 compressor from liquid (HAZOP 6.9 'alarmed catchpot upstream of J103'). PCV119 recycles CO2 around it (REPORT D.4). Grid not in the REPORT lists (near M20).
K103 --label--> K103 alarmed catchpot on the J103 suction
K103 --pipedTo--> V185
K103 --floor--> 1
K103 --tag--> K103
GR04 --about--> K103
K103_CO2_recycle --toItem--> K103
limit_LAH_K103 --appliesTo--> K103
FT301 --feedsInto--> K103
FT301 --pipedTo--> K103
CL_E100_pressure --source--> SUMMARY p.190; REPORT D.4
CL_E100_pressure --manipulatedVariable--> PCV119 opening
CL_E100_pressure --hasController--> PIC401
CL_E100_pressure --type--> ControlLoop
CL_E100_pressure --label--> E100 pressure (boundary loop on overhead)
CL_E100_pressure --controlledVariable--> Pressure in E100
CL_E100_pressure --hasSensor--> PT402
CL_E100_pressure --hasSensor--> PT401
PCV119__cit01 --type--> Citation
PCV119__cit01 --location--> p.190 (control-loop table)
PCV119__cit01 --citationText--> Plant summary 2023-24 p.190 (control-loop table)
PCV119__cit01 --label--> Citation 1 for PCV119
PCV119__cit01 --document--> SRC_SUMMARY
RV105 --label--> RV105
RV105 --valveType--> relief
RV105 --tag--> RV105
RV105 --type--> ReliefValve
RV105 --gridReference--> K19
RV105 --normalPosition--> closed
RV105 --note--> Next to PCV119 (CO2 return / J103 area). FI07
RV105 --floor--> 1
FI07 --about--> RV105
K103_CO2_recycle --bypasses--> SDV171
K103_CO2_recycle --type--> BypassRoute
K103_CO2_recycle --normalState--> modulating
K103_CO2_recycle --label--> CO2 recycle around K103 via PCV119 (E100 pressure control)
K103_CO2_recycle --bypasses--> K101
PIC401 --label--> E100 pressure controller
PIC401 --type--> Controller
PIC401 --tag--> PIC401
HAZOP_6_05 --itemNumber--> 5
HAZOP_6_05 --actionTaken--> Action completed
HAZOP_6_05 --safeguard--> NRV104
HAZOP_6_05 --recommendedAction--> Consider control of PCV 119 on Flow (vs pressure) in light of spec. of J103
HAZOP_6_05 --concerns--> NRV104
HAZOP_6_05 --concerns--> C400
HAZOP_6_05 --cause--> Failure of NRV104 + low pressure d/s of C400
HAZOP_6_05 --guideword--> REVERSE
HAZOP_6_05 --label--> HAZOP 6.5
HAZOP_6_05 --consequence--> instable pressure control loop protecting J103
HAZOP_6_05 --parameter--> FLOW
HAZOP_6_05 --type--> HazopDeviation
V209 --pipedTo--> VENT_SYSTEM
V197 --pipedTo--> VENT_SYSTEM
V411 --pipedTo--> VENT_SYSTEM
V190 --pipedTo--> VENT_SYSTEM
V409 --pipedTo--> VENT_SYSTEM
VENT_E101 --pipedTo--> VENT_SYSTEM
SDV421 --pipedTo--> VENT_SYSTEM
V315 --pipedTo--> VENT_SYSTEM
SDV171 --feedsInto--> V172
SDV171 --pipedTo--> V172
V316 --pipedTo--> V315
PCV300 --pipedTo--> VENT_E101
PCV300 --feedsInto--> VENT_E101
V411 --feedsInto--> CW_RETURN
V411 --pipedTo--> CW_RETURN
V410 --feedsInto--> V411
V410 --pipedTo--> V411
FT302 --feedsInto--> FT301
```

Question: Which two pressure measurements can be selected to control PCV119, and where are they located?

## Q34

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
K101 --type--> Saturator
K101 --label--> K101 gas saturator
K101 --pipedTo--> SDV170
K101 --pipedTo--> Z103
K101 --floor--> 1
K101 --feedsInto--> E101_N_gas_inlet
K101 --pipedTo--> E101_N_gas_inlet
K101 --note--> Saturates the feed gas with water before E101; temperature held by TIC121 using C106 on the recirculating water. Grid not in the REPORT lists (near L17 to L18 on the P&ID). Not modelled in Aspen (GOI09).
K101 --pipedTo--> V126
K101 --tag--> K101
DI_CARTRIDGE --feedsInto--> K101
HAZOP_4_06 --concerns--> K101
V172 --pipedTo--> K101
J102 --pipedTo--> K101
limit_LZAL_K101 --appliesTo--> K101
HAZOP_4_07 --concerns--> K101
LT104 --monitors--> K101
HAZOP_3_05 --concerns--> K101
FEED_GAS_HEADER --feedsInto--> K101
GOI09 --about--> K101
LI106 --monitors--> K101
FEED_GAS_HEADER --pipedTo--> K101
limit_LAL_K101 --appliesTo--> K101
K101_N2_recycle --fromItem--> K101
limit_LZAH_K101 --appliesTo--> K101
GOI07 --about--> K101
GOI02 --about--> K101
HAZOP_element_3 --covers--> K101
HAZOP_4_02 --concerns--> K101
TI121 --monitors--> K101
C106 --pipedTo--> K101
K103_CO2_recycle --bypasses--> K101
TT121 --monitors--> K101
DI_CARTRIDGE --pipedTo--> K101
J102 --feedsInto--> K101
V172 --feedsInto--> K101
N2ReturnLoop --hasStep--> N2ReturnLoop_step_00_E101
N2ReturnLoop --hasStep--> N2ReturnLoop_step_02_K402
N2ReturnLoop --hasStep--> N2ReturnLoop_step_15_E101_N_gas_inlet
N2ReturnLoop --inMode--> FigureOfEight
N2ReturnLoop --hasStep--> N2ReturnLoop_step_01_E101_N_gas_outlet
N2ReturnLoop --hasStep--> N2ReturnLoop_step_05_FT303
N2ReturnLoop --hasStep--> N2ReturnLoop_step_16_E101
N2ReturnLoop --hasStep--> N2ReturnLoop_step_13_FT107
N2ReturnLoop --hasStep--> N2ReturnLoop_step_07_FT304
N2ReturnLoop --note--> N2 is not absorbed, so it is recirculated: J102 blows it from the K402 overhead back through K101 into E101. Fresh N2 and CO2 (piece 5) top it up. FCV111 recycles part of it from K101 back to K102 to set the N2 flow into E101.
N2ReturnLoop --hasStep--> N2ReturnLoop_step_03_K402_N_gas_to_return
N2ReturnLoop --hasStep--> N2ReturnLoop_step_10_V187
N2ReturnLoop --hasStep--> N2ReturnLoop_step_04_TT304
N2ReturnLoop --label--> N2 return loop (E101 > K402 > K102 > J102 > K101 > E101)
N2ReturnLoop --hasStep--> N2ReturnLoop_step_12_TT114
N2ReturnLoop --hasStep--> N2ReturnLoop_step_08_FI304
N2ReturnLoop --hasStep--> N2ReturnLoop_step_14_K101
N2ReturnLoop --hasStep--> N2ReturnLoop_step_06_FI303
N2ReturnLoop --hasStep--> N2ReturnLoop_step_09_K102
N2ReturnLoop --type--> Loop
N2ReturnLoop --hasStep--> N2ReturnLoop_step_11_J102
FCV111 --floor--> 1
FCV111 --valveType--> flow control
FCV111 --tag--> FCV111
FCV111 --pipedTo--> K102
FCV111 --label--> FCV111
FCV111 --gridReference--> K17
FCV111 --type--> FlowControlValve
FCV111 --normalPosition--> open
FCV111 --note--> Recycles N2 from K101 back to K102, reducing the recycled N2 entering E101 (REPORT D.4, Fig D.6/D.7). Controlled by FIC303/FIC304 from FT303/FT304 on the N2 recycle pipe.
FIC304 --controls--> FCV111
K101_N2_recycle --routeVia--> FCV111
SDV170 --pipedTo--> FCV111
CL_N2_to_E101 --hasFinalElement--> FCV111
FIC303 --controls--> FCV111
N2ReturnLoop_step_11_J102 --label--> N2 return loop (E101 > K402 > K102 > J102 > K101 > E101) step 11: J102
N2ReturnLoop_step_11_J102 --stepItem--> J102
N2ReturnLoop_step_11_J102 --stepIndex--> 11
N2ReturnLoop_step_11_J102 --type--> LoopStep
N2ReturnLoop_step_11_J102 --stepType--> inline
NRV100b --type--> CheckValve
NRV100b --gridReference--> Q19
NRV100b --note--> Bottom right (make-up water to K101?). FI03
NRV100b --feedsInto--> DI_CARTRIDGE
NRV100b --pipedTo--> DI_CARTRIDGE
NRV100b --valveType--> check
NRV100b --label--> NRV100b
NRV100b --tag--> NRV100b
NRV100b --floor--> 1
NRV100a --feedsInto--> NRV100b
NRV100a --pipedTo--> NRV100b
N2ReturnLoop_step_04_TT304 --stepType--> tie-in
N2ReturnLoop_step_04_TT304 --type--> LoopStep
N2ReturnLoop_step_04_TT304 --label--> N2 return loop (E101 > K402 > K102 > J102 > K101 > E101) step 4: TT304
N2ReturnLoop_step_04_TT304 --stepIndex--> 4
N2ReturnLoop_step_04_TT304 --stepItem--> TT304
TT107 --label--> TT107
TT107 --signalType--> Fieldbus
TT107 --sensorType--> PRT
TT107 --floor--> 1
TT107 --measuredVariable--> gas entering E101 (after K101)
TT107 --monitors--> E101
TT107 --type--> TemperatureInstrument
TT107 --gridReference--> K18
TT107 --tag--> TT107
HAZOP_10_03 --label--> HAZOP 10.3
HAZOP_10_03 --consequence--> Overpressure lower section of E101 and K101
HAZOP_10_03 --actionTaken--> RV added
HAZOP_10_03 --itemNumber--> 3
HAZOP_10_03 --inElement--> HAZOP_element_10
HAZOP_10_03 --parameter--> FLOW
HAZOP_10_03 --cause--> High rate of gas up column from CO2 and N2 feed system
HAZOP_10_03 --type--> HazopDeviation
HAZOP_10_03 --concerns--> E101
HAZOP_10_03 --recommendedAction--> RV at outlet to K101?
HAZOP_10_03 --guideword--> MORE
N2ReturnLoop_step_05_FT303 --stepItem--> FT303
N2ReturnLoop_step_05_FT303 --type--> LoopStep
N2ReturnLoop_step_05_FT303 --stepType--> inline
N2ReturnLoop_step_05_FT303 --label--> N2 return loop (E101 > K402 > K102 > J102 > K101 > E101) step 5: FT303
N2ReturnLoop_step_05_FT303 --stepIndex--> 5
HAZOP_4_06 --cause--> As K101
HAZOP_4_06 --parameter--> TEMP.
HAZOP_4_06 --label--> HAZOP 4.6
HAZOP_4_06 --itemNumber--> 6
HAZOP_4_06 --type--> HazopDeviation
HAZOP_4_06 --inElement--> HAZOP_element_4
HAZOP_4_06 --guideword--> HIGHER
N2ReturnLoop_step_10_V187 --stepItem--> V187
N2ReturnLoop_step_10_V187 --stepType--> branch
N2ReturnLoop_step_10_V187 --label--> N2 return loop (E101 > K402 > K102 > J102 > K101 > E101) step 10: V187
N2ReturnLoop_step_10_V187 --stepIndex--> 10
N2ReturnLoop_step_10_V187 --type--> LoopStep
GOI09 --foundBy--> gas section build, Oct 2026
GOI09 --itemStatus--> open
GOI09 --label--> GOI09: Aspen feeds the gas straight into E101 with no K101 saturator
GOI09 --description--> Aspen feeds the gas straight into E101 with no K101 saturator
GOI09 --resolvedBy--> Note for model comparison
GOI09 --type--> OpenItem
limit_LZAH_K101 --type--> OperatingLimit
limit_LZAH_K101 --variable--> level
limit_LZAH_K101 --unit--> -
limit_LZAH_K101 --limitType--> alarm
limit_LZAH_K101 --source--> HAZOP element 3, item 5 (LZAH104, now LZAH103; soft high alarm added)
limit_LZAH_K101 --valueVerified--> false
limit_LZAH_K101 --label--> LZAH_K101
SDV170 --gridReference--> K17
SDV170 --label--> SDV170
SDV170 --valveType--> shutdown (solenoid-operated)
SDV170 --tag--> SDV170
SDV170 --type--> ShutdownValve
SDV170 --floor--> 1
SDV170 --note--> On the FCV111 recycle line from K101 to K102 (P&ID shows SDV170 with HS170 next to FCV111); the REPORT lists it as SOV170.
K101_N2_recycle --routeVia--> SDV170
```

Question: Which instrument chain controls the fresh nitrogen feed entering K101?

## Q35

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
K101 --type--> Saturator
K101 --label--> K101 gas saturator
K101 --pipedTo--> SDV170
K101 --pipedTo--> Z103
K101 --floor--> 1
K101 --feedsInto--> E101_N_gas_inlet
K101 --pipedTo--> E101_N_gas_inlet
K101 --note--> Saturates the feed gas with water before E101; temperature held by TIC121 using C106 on the recirculating water. Grid not in the REPORT lists (near L17 to L18 on the P&ID). Not modelled in Aspen (GOI09).
K101 --pipedTo--> V126
K101 --tag--> K101
DI_CARTRIDGE --feedsInto--> K101
HAZOP_4_06 --concerns--> K101
V172 --pipedTo--> K101
J102 --pipedTo--> K101
limit_LZAL_K101 --appliesTo--> K101
HAZOP_4_07 --concerns--> K101
LT104 --monitors--> K101
HAZOP_3_05 --concerns--> K101
FEED_GAS_HEADER --feedsInto--> K101
GOI09 --about--> K101
LI106 --monitors--> K101
FEED_GAS_HEADER --pipedTo--> K101
limit_LAL_K101 --appliesTo--> K101
K101_N2_recycle --fromItem--> K101
limit_LZAH_K101 --appliesTo--> K101
GOI07 --about--> K101
GOI02 --about--> K101
HAZOP_element_3 --covers--> K101
HAZOP_4_02 --concerns--> K101
TI121 --monitors--> K101
C106 --pipedTo--> K101
K103_CO2_recycle --bypasses--> K101
TT121 --monitors--> K101
DI_CARTRIDGE --pipedTo--> K101
J102 --feedsInto--> K101
V172 --feedsInto--> K101
N2ReturnLoop --hasStep--> N2ReturnLoop_step_00_E101
N2ReturnLoop --hasStep--> N2ReturnLoop_step_02_K402
N2ReturnLoop --hasStep--> N2ReturnLoop_step_15_E101_N_gas_inlet
N2ReturnLoop --inMode--> FigureOfEight
N2ReturnLoop --hasStep--> N2ReturnLoop_step_01_E101_N_gas_outlet
N2ReturnLoop --hasStep--> N2ReturnLoop_step_05_FT303
N2ReturnLoop --hasStep--> N2ReturnLoop_step_16_E101
N2ReturnLoop --hasStep--> N2ReturnLoop_step_13_FT107
N2ReturnLoop --hasStep--> N2ReturnLoop_step_07_FT304
N2ReturnLoop --note--> N2 is not absorbed, so it is recirculated: J102 blows it from the K402 overhead back through K101 into E101. Fresh N2 and CO2 (piece 5) top it up. FCV111 recycles part of it from K101 back to K102 to set the N2 flow into E101.
N2ReturnLoop --hasStep--> N2ReturnLoop_step_03_K402_N_gas_to_return
N2ReturnLoop --hasStep--> N2ReturnLoop_step_10_V187
N2ReturnLoop --hasStep--> N2ReturnLoop_step_04_TT304
N2ReturnLoop --label--> N2 return loop (E101 > K402 > K102 > J102 > K101 > E101)
N2ReturnLoop --hasStep--> N2ReturnLoop_step_12_TT114
N2ReturnLoop --hasStep--> N2ReturnLoop_step_08_FI304
N2ReturnLoop --hasStep--> N2ReturnLoop_step_14_K101
N2ReturnLoop --hasStep--> N2ReturnLoop_step_06_FI303
N2ReturnLoop --hasStep--> N2ReturnLoop_step_09_K102
N2ReturnLoop --type--> Loop
N2ReturnLoop --hasStep--> N2ReturnLoop_step_11_J102
FCV111 --floor--> 1
FCV111 --valveType--> flow control
FCV111 --tag--> FCV111
FCV111 --pipedTo--> K102
FCV111 --label--> FCV111
FCV111 --gridReference--> K17
FCV111 --type--> FlowControlValve
FCV111 --normalPosition--> open
FCV111 --note--> Recycles N2 from K101 back to K102, reducing the recycled N2 entering E101 (REPORT D.4, Fig D.6/D.7). Controlled by FIC303/FIC304 from FT303/FT304 on the N2 recycle pipe.
FIC304 --controls--> FCV111
K101_N2_recycle --routeVia--> FCV111
SDV170 --pipedTo--> FCV111
CL_N2_to_E101 --hasFinalElement--> FCV111
FIC303 --controls--> FCV111
N2ReturnLoop_step_11_J102 --label--> N2 return loop (E101 > K402 > K102 > J102 > K101 > E101) step 11: J102
N2ReturnLoop_step_11_J102 --stepItem--> J102
N2ReturnLoop_step_11_J102 --stepIndex--> 11
N2ReturnLoop_step_11_J102 --type--> LoopStep
N2ReturnLoop_step_11_J102 --stepType--> inline
NRV100b --type--> CheckValve
NRV100b --gridReference--> Q19
NRV100b --note--> Bottom right (make-up water to K101?). FI03
NRV100b --feedsInto--> DI_CARTRIDGE
NRV100b --pipedTo--> DI_CARTRIDGE
NRV100b --valveType--> check
NRV100b --label--> NRV100b
NRV100b --tag--> NRV100b
NRV100b --floor--> 1
NRV100a --feedsInto--> NRV100b
NRV100a --pipedTo--> NRV100b
N2ReturnLoop_step_04_TT304 --stepType--> tie-in
N2ReturnLoop_step_04_TT304 --type--> LoopStep
N2ReturnLoop_step_04_TT304 --label--> N2 return loop (E101 > K402 > K102 > J102 > K101 > E101) step 4: TT304
N2ReturnLoop_step_04_TT304 --stepIndex--> 4
N2ReturnLoop_step_04_TT304 --stepItem--> TT304
TT107 --label--> TT107
TT107 --signalType--> Fieldbus
TT107 --sensorType--> PRT
TT107 --floor--> 1
TT107 --measuredVariable--> gas entering E101 (after K101)
TT107 --monitors--> E101
TT107 --type--> TemperatureInstrument
TT107 --gridReference--> K18
TT107 --tag--> TT107
HAZOP_10_03 --label--> HAZOP 10.3
HAZOP_10_03 --consequence--> Overpressure lower section of E101 and K101
HAZOP_10_03 --actionTaken--> RV added
HAZOP_10_03 --itemNumber--> 3
HAZOP_10_03 --inElement--> HAZOP_element_10
HAZOP_10_03 --parameter--> FLOW
HAZOP_10_03 --cause--> High rate of gas up column from CO2 and N2 feed system
HAZOP_10_03 --type--> HazopDeviation
HAZOP_10_03 --concerns--> E101
HAZOP_10_03 --recommendedAction--> RV at outlet to K101?
HAZOP_10_03 --guideword--> MORE
N2ReturnLoop_step_05_FT303 --stepItem--> FT303
N2ReturnLoop_step_05_FT303 --type--> LoopStep
N2ReturnLoop_step_05_FT303 --stepType--> inline
N2ReturnLoop_step_05_FT303 --label--> N2 return loop (E101 > K402 > K102 > J102 > K101 > E101) step 5: FT303
N2ReturnLoop_step_05_FT303 --stepIndex--> 5
HAZOP_4_06 --cause--> As K101
HAZOP_4_06 --parameter--> TEMP.
HAZOP_4_06 --label--> HAZOP 4.6
HAZOP_4_06 --itemNumber--> 6
HAZOP_4_06 --type--> HazopDeviation
HAZOP_4_06 --inElement--> HAZOP_element_4
HAZOP_4_06 --guideword--> HIGHER
N2ReturnLoop_step_10_V187 --stepItem--> V187
N2ReturnLoop_step_10_V187 --stepType--> branch
N2ReturnLoop_step_10_V187 --label--> N2 return loop (E101 > K402 > K102 > J102 > K101 > E101) step 10: V187
N2ReturnLoop_step_10_V187 --stepIndex--> 10
N2ReturnLoop_step_10_V187 --type--> LoopStep
GOI09 --foundBy--> gas section build, Oct 2026
GOI09 --itemStatus--> open
GOI09 --label--> GOI09: Aspen feeds the gas straight into E101 with no K101 saturator
GOI09 --description--> Aspen feeds the gas straight into E101 with no K101 saturator
GOI09 --resolvedBy--> Note for model comparison
GOI09 --type--> OpenItem
limit_LZAH_K101 --type--> OperatingLimit
limit_LZAH_K101 --variable--> level
limit_LZAH_K101 --unit--> -
limit_LZAH_K101 --limitType--> alarm
limit_LZAH_K101 --source--> HAZOP element 3, item 5 (LZAH104, now LZAH103; soft high alarm added)
limit_LZAH_K101 --valueVerified--> false
limit_LZAH_K101 --label--> LZAH_K101
SDV170 --gridReference--> K17
SDV170 --label--> SDV170
SDV170 --valveType--> shutdown (solenoid-operated)
SDV170 --tag--> SDV170
SDV170 --type--> ShutdownValve
SDV170 --floor--> 1
SDV170 --note--> On the FCV111 recycle line from K101 to K102 (P&ID shows SDV170 with HS170 next to FCV111); the REPORT lists it as SOV170.
K101_N2_recycle --routeVia--> SDV170
```

Question: Which components would be involved in correcting an excessive fresh CO2 feed concentration at K101?

## Q36

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
aspen_v3_block_E101 --type--> AspenBlock
aspen_v3_block_E101 --aspenModel--> RADFRAC
aspen_v3_block_E101 --blockId--> E101
aspen_v3_block_E101 --status--> OK
aspen_v3_block_E101 --label--> E101 (ABB_pilot_plant_final_3)
aspen_v3_block_E101 --inCase--> case_aspen_v3
aspen_v3_stream_S8 --fromBlock--> aspen_v3_block_E101
aspen_v3_stream_1 --toBlock--> aspen_v3_block_E101
aspen_v3_stream_2 --toBlock--> aspen_v3_block_E101
aspen_v3_stream_4 --fromBlock--> aspen_v3_block_E101
aspen_v6_1_block_E101 --type--> AspenBlock
aspen_v6_1_block_E101 --aspenModel--> RADFRAC
aspen_v6_1_block_E101 --label--> E101 (ABB_pilot_plant_final_6_1_SA_validation)
aspen_v6_1_block_E101 --blockId--> E101
aspen_v6_1_block_E101 --status--> OK
aspen_v6_1_block_E101 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S8 --fromBlock--> aspen_v6_1_block_E101
aspen_v6_1_stream_2 --toBlock--> aspen_v6_1_block_E101
aspen_v6_1_stream_1 --toBlock--> aspen_v6_1_block_E101
aspen_v6_1_stream_4 --fromBlock--> aspen_v6_1_block_E101
E101 --pipedTo--> RV400
E101 --floor--> 1
E101 --note--> Lean MEA enters at the top through NRV400; rich MEA leaves from the sump to J101a/b. The air admittance valve shown on the P&ID has been removed from the plant (DIFF, E14/15).
E101 --feedsInto--> E101_N_sump_outlet
E101 --designBasis--> Packing and column designed for 2.3-2.5 bar operation on MEA and 50 kg/h CO2 (HAZOP 10.4)
E101 --feedsInto--> E101_N_gas_outlet
E101 --pipedTo--> E101_N_sump_outlet
E101 --pipedTo--> E101_N_gas_outlet
E101 --type--> AbsorptionColumn
E101 --diameter_mm--> 230.0
E101 --tag--> E101
E101 --label--> E101 absorber
HAZOP_7_10 --concerns--> E101
TT305 --monitors--> E101
PT111 --monitors--> E101
E101_sample_5 --onColumn--> E101
E101_N_gas_outlet --onEquipment--> E101
LSLL109 --monitors--> E101
TT207 --monitors--> E101
PT403 --monitors--> E101
LI108 --monitors--> E101
E101_sample_4 --onColumn--> E101
E101_N_sump_outlet --onEquipment--> E101
FT109 --monitors--> E101
E101_sample_3 --onColumn--> E101
HAZOP_9b_05 --concerns--> E101
limit_LZAL109 --appliesTo--> E101
DI108 --monitors--> E101
E101_N_gas_inlet --feedsInto--> E101
FT304 --monitors--> E101
LT108 --monitors--> E101
K101_N2_recycle --bypasses--> E101
PT110 --monitors--> E101
E101_N_gas_inlet --pipedTo--> E101
HAZOP_5_08 --concerns--> E101
HAZOP_8_01 --concerns--> E101
HAZOP_8_06 --concerns--> E101
PI403 --monitors--> E101
AT400 --monitors--> E101
FT303 --monitors--> E101
TT205 --monitors--> E101
E101_N_base_inlet --onEquipment--> E101
aspen_v6_1_E101_performance --ofEquipment--> E101
TT206 --monitors--> E101
HAZOP_8_03 --concerns--> E101
E101_N_gas_inlet --onEquipment--> E101
E101_N_top_inlet --feedsInto--> E101
E101_sample_6 --onColumn--> E101
K402 --pipedTo--> E101
HAZOP_5_07 --concerns--> E101
AI300 --monitors--> E101
FI109 --monitors--> E101
FI108 --monitors--> E101
aspen_v3_vent_gas --ofEquipment--> E101
AT300 --monitors--> E101
E101_N_top_inlet --pipedTo--> E101
aspen_v6_1_feed_gas --ofEquipment--> E101
limit_PSHH117_set --appliesTo--> E101
TT109 --monitors--> E101
TT412 --monitors--> E101
HAZOP_10_03 --concerns--> E101
LSHH107 --monitors--> E101
E101_sample_2 --onColumn--> E101
limit_LZAH107 --appliesTo--> E101
HAZOP_5_06 --concerns--> E101
PSHH117 --monitors--> E101
TT413 --monitors--> E101
HAZOP_7_13 --concerns--> E101
TT107 --monitors--> E101
TT306 --monitors--> E101
E101_N_top_inlet --onEquipment--> E101
E101_sample_1 --onColumn--> E101
AOI10 --about--> E101
RV400 --protects--> E101
FT108 --monitors--> E101
TT411 --monitors--> E101
TT204 --monitors--> E101
aspen_v3_feed_gas --ofEquipment--> E101
HAZOP_element_10 --covers--> E101
HAZOP_8_11 --concerns--> E101
TT307 --monitors--> E101
TT308 --monitors--> E101
HAZOP_8_02 --concerns--> E101
aspen_v3_E101_performance --ofEquipment--> E101
PCV300 --valveType--> pressure control
PCV300 --floor--> 3
PCV300 --normalPosition--> open
PCV300 --note--> Vents lean gas from the absorber to hold the E101 pressure (PIC403). Opened in the vent stream start-up (Fig F.3), closed at shutdown.
PCV300 --pipedTo--> VENT_E101
PCV300 --label--> PCV300
PCV300 --feedsInto--> VENT_E101
PCV300 --type--> PressureControlValve
PCV300 --tag--> PCV300
PCV300 --gridReference--> G18
K402 --feedsInto--> PCV300
CL_E101_pressure --hasFinalElement--> PCV300
K402 --pipedTo--> PCV300
PIC403 --controls--> PCV300
AV01 --about--> PCV300
K101 --type--> Saturator
K101 --label--> K101 gas saturator
K101 --pipedTo--> SDV170
K101 --pipedTo--> Z103
K101 --floor--> 1
K101 --feedsInto--> E101_N_gas_inlet
K101 --pipedTo--> E101_N_gas_inlet
K101 --note--> Saturates the feed gas with water before E101; temperature held by TIC121 using C106 on the recirculating water. Grid not in the REPORT lists (near L17 to L18 on the P&ID). Not modelled in Aspen (GOI09).
K101 --pipedTo--> V126
K101 --tag--> K101
DI_CARTRIDGE --feedsInto--> K101
HAZOP_4_06 --concerns--> K101
V172 --pipedTo--> K101
J102 --pipedTo--> K101
limit_LZAL_K101 --appliesTo--> K101
HAZOP_4_07 --concerns--> K101
LT104 --monitors--> K101
HAZOP_3_05 --concerns--> K101
FEED_GAS_HEADER --feedsInto--> K101
GOI09 --about--> K101
LI106 --monitors--> K101
FEED_GAS_HEADER --pipedTo--> K101
limit_LAL_K101 --appliesTo--> K101
K101_N2_recycle --fromItem--> K101
limit_LZAH_K101 --appliesTo--> K101
GOI07 --about--> K101
GOI02 --about--> K101
HAZOP_element_3 --covers--> K101
HAZOP_4_02 --concerns--> K101
TI121 --monitors--> K101
C106 --pipedTo--> K101
```

Question: How do the nitrogen recycle flow measurements control the amount of gas returning to E101?

## Q37

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
```

Question: How is the condensate level measurement converted into a return-flow adjustment?

## Q38

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
```

Question: Which two analytical instruments allow the operator to compare rich and lean MEA condition on opposite sides of the regeneration cycle?

## Q39

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
H100 --tag--> H100
H100 --floor--> 1
H100 --source--> SUMMARY p.102
H100 --type--> SteamReboiler
H100 --feedsInto--> Q106
H100 --pipedTo--> Q106
H100 --label--> H100 vertical thermosiphon steam reboiler
FI102 --monitors--> H100
H100_N_condensate_out --onEquipment--> H100
TT100 --monitors--> H100
aspen_v3_H100_performance --ofEquipment--> H100
FT101 --monitors--> H100
HAZOP_element_13 --covers--> H100
aspen_v6_1_block_H100 --represents--> H100
TI100 --monitors--> H100
PROC_reboiler_heating_step_04 --operatesOn--> H100
DI100 --monitors--> H100
limit_H100_steam_limit --appliesTo--> H100
PI101 --monitors--> H100
PI100 --monitors--> H100
aspen_v3_block_H100REAC --represents--> H100
PT101 --monitors--> H100
FT102 --monitors--> H100
aspen_v3_block_H100HEAT --represents--> H100
TT117 --monitors--> H100
TT118 --monitors--> H100
FI100 --monitors--> H100
Q105 --pipedTo--> H100
H100_N_steam_in --onEquipment--> H100
Q105 --feedsInto--> H100
aspen_v6_1_H100_performance --ofEquipment--> H100
FT100 --monitors--> H100
HAZOP_element_11 --covers--> H100
RV107 --protects--> H100
aspen_v6_1_block_H100 --label--> H100 (ABB_pilot_plant_final_6_1_SA_validation)
aspen_v6_1_block_H100 --blockId--> H100
aspen_v6_1_block_H100 --aspenModel--> HEATX
aspen_v6_1_block_H100 --type--> AspenBlock
aspen_v6_1_block_H100 --statusMessage--> INVALID INPUT SPECIFICATIONS SEE TASC BROWSER FOR INFO.
aspen_v6_1_block_H100 --status--> ERROR
aspen_v6_1_block_H100 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S14 --fromBlock--> aspen_v6_1_block_H100
aspen_v6_1_stream_S17 --fromBlock--> aspen_v6_1_block_H100
aspen_v6_1_stream_S31 --toBlock--> aspen_v6_1_block_H100
aspen_v6_1_stream_S23 --toBlock--> aspen_v6_1_block_H100
PROC_reboiler_heating_step_01 --operatesOn--> FT100
PROC_reboiler_heating_step_01 --stepOrder--> 1
PROC_reboiler_heating_step_01 --instruction--> Check whether FT100 and FT101 show steam flowing to H100
PROC_reboiler_heating_step_01 --type--> ProcedureStep
PROC_reboiler_heating_step_01 --label--> Reboiler heating the MEA during the stripping loop test step 1
PROC_reboiler_heating --hasProcedureStep--> PROC_reboiler_heating_step_01
aspen_v6_1_stream_S14 --massFlow_kg_h--> 199.9608
aspen_v6_1_stream_S14 --co2Loading_mol_mol--> 0.638118
aspen_v6_1_stream_S14 --waterFlow_kg_h--> 156.4997
aspen_v6_1_stream_S14 --temperature_C--> 89.36771
aspen_v6_1_stream_S14 --pressure_bar--> 2.05248
aspen_v6_1_stream_S14 --type--> StreamState
aspen_v6_1_stream_S14 --label--> S14 (ABB_pilot_plant_final_6_1_SA_validation)
aspen_v6_1_stream_S14 --streamId--> S14
aspen_v6_1_stream_S14 --moleFlow_kmol_h--> 9.279221
aspen_v6_1_stream_S14 --vapourFraction--> 0.0
aspen_v6_1_stream_S14 --phase--> LIQUID
aspen_v6_1_stream_S14 --apparentCO2_kg_h--> 13.05912
aspen_v6_1_stream_S14 --meaMassFraction--> 0.1420495
aspen_v6_1_stream_S14 --enthalpyFlow_W--> -759156.0
aspen_v6_1_stream_S14 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S14 --toBlock--> aspen_v6_1_block_E100
SteamRoute_step_19_V103 --label--> Steam and condensate route to H100 step 19: V103
SteamRoute_step_19_V103 --stepItem--> V103
SteamRoute_step_19_V103 --stepType--> inline
SteamRoute_step_19_V103 --stepIndex--> 19
SteamRoute_step_19_V103 --type--> LoopStep
SteamRoute --hasStep--> SteamRoute_step_17_K100
SteamRoute --hasStep--> SteamRoute_step_15_PI101
SteamRoute --hasStep--> SteamRoute_step_21_V105
SteamRoute --hasStep--> SteamRoute_step_02_V100
SteamRoute --hasStep--> SteamRoute_step_20_V104
SteamRoute --hasStep--> SteamRoute_step_04_PI100
SteamRoute --hasStep--> SteamRoute_step_13_H100_N_condensate_out
SteamRoute --hasStep--> SteamRoute_step_01_XV140
SteamRoute --type--> Loop
SteamRoute --hasStep--> SteamRoute_step_14_TT118
SteamRoute --hasStep--> SteamRoute_step_07_FI100
SteamRoute --hasStep--> SteamRoute_step_11_TT117
SteamRoute --hasStep--> SteamRoute_step_16_RV107
SteamRoute --hasStep--> SteamRoute_step_22_NRV110
SteamRoute --hasStep--> SteamRoute_step_03_PT101
SteamRoute --note--> Building steam heats the MEA in the H100 reboiler shell and leaves as condensate through the K100 trap. FCV110 sets the steam flow (TIC100 > FIC100 cascade, stripping loop).
SteamRoute --inMode--> FigureOfEight
SteamRoute --hasStep--> SteamRoute_step_09_FT101
SteamRoute --hasStep--> SteamRoute_step_12_H100_N_steam_in
SteamRoute --hasStep--> SteamRoute_step_19_V103
SteamRoute --hasStep--> SteamRoute_step_05_V101
SteamRoute --hasStep--> SteamRoute_step_06_FT100
SteamRoute --hasStep--> SteamRoute_step_08_V102
SteamRoute --hasStep--> SteamRoute_step_10_FCV110
SteamRoute --label--> Steam and condensate route to H100
SteamRoute --hasStep--> SteamRoute_step_00_STEAM_SUPPLY
SteamRoute --hasStep--> SteamRoute_step_23_CONDENSATE_RETURN
SteamRoute --hasStep--> SteamRoute_step_18_V106
aspen_v3_H100_performance --coldInlet_C--> 116.8438
aspen_v3_H100_performance --label--> H100 performance (ABB_pilot_plant_final_3)
aspen_v3_H100_performance --coldSideDuty_kW--> 115.5427
aspen_v3_H100_performance --type--> HeatExchangerPerformance
aspen_v3_H100_performance --lmtd_K--> 32.8462
aspen_v3_H100_performance --area_m2--> 61.6081
aspen_v3_H100_performance --hotOutlet_C--> 118.2011
aspen_v3_H100_performance --derivedBy--> heat_mass_transfer.py
aspen_v3_H100_performance --minApproach_K--> 1.357255
aspen_v3_H100_performance --temperatureCross--> false
aspen_v3_H100_performance --overallU_W_m2K--> 448.1082
aspen_v3_H100_performance --hotInlet_C--> 276.85
aspen_v3_H100_performance --effectiveness--> 0.9911752
aspen_v3_H100_performance --hotSideDuty_kW--> 115.5827
aspen_v3_H100_performance --coldOutlet_C--> 119.3414
aspen_v3_H100_performance --duty_kW--> 115.5627
aspen_v3_H100_performance --energyBalanceError_pct--> 0.03452101
aspen_v3_H100_performance --ua_W_K--> 3517.69
aspen_v3_H100_performance --inCase--> case_aspen_v3
V102 --label--> V102
V102 --note--> Steam side of H100. Closed in the stripping loop test: no steam (REPORT Fig E.1).
V102 --feedsInto--> FT101
V102 --tag--> V102
V102 --pipedTo--> FT101
V102 --type--> ManualValve
V102 --normalPosition--> closed
V102 --gridReference--> L4
V102 --valveType--> ball
V102 --floor--> 1
FT100 --feedsInto--> V102
FT100 --pipedTo--> V102
PROC_stripping_loop_lineup_step_08 --operatesOn--> V102
PROC_H100_steam_bypass_step_05 --operatesOn--> V102
HAZOP_element_13 --covers--> V102
case_aspen_v6_1 --converged--> false
case_aspen_v6_1 --representsMode--> FigureOfEight
case_aspen_v6_1 --savedOn--> Thu Feb 27 15:14:32 2025
case_aspen_v6_1 --recommendedForUse--> false
case_aspen_v6_1 --aspenFile--> ABB_pilot_plant_final_6_1_SA_validation.apwz
case_aspen_v6_1 --label--> ABB_pilot_plant_final_6_1_SA_validation
case_aspen_v6_1 --aspenVersion--> 37.0
case_aspen_v6_1 --note--> Rescaled to pilot conditions with a sensitivity study for validation. Saved results did not converge: E100 RateSep failed, H100 invalid input, C100 temperature crossover, recycle opened at S3BACKUP.
case_aspen_v6_1 --type--> SimulationCase
aspen_v6_1_block_E100 --inCase--> case_aspen_v6_1
aspen_v6_1_block_C400COND --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S21 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_PURGE --inCase--> case_aspen_v6_1
aspen_v6_1_E100_stage_02 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S4 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S17 --inCase--> case_aspen_v6_1
```

Question: If H100 appears to be heating unexpectedly, which linked measurements and valves should be investigated?

## Q40

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
J101a --pipedTo--> PCV120a
J101a --note--> J101a and J101b are in parallel; only one runs at a time (SIC101a or SIC101b).
J101a --gridReference--> N15
J101a --feedsInto--> PCV120a
J101a --tag--> J101a
J101a --floor--> 1
J101a --type--> Pump
J101a --label--> J101a rich MEA pump (duty or standby)
AOI02 --about--> J101a
PROC_J101a_startup_step_02 --operatesOn--> J101a
TT110a --monitors--> J101a
TT111a --monitors--> J101a
AOI04 --about--> J101a
IL_E101_level_LL --tripsItem--> J101a
PROC_pump_start_order_step_04 --operatesOn--> J101a
HAZOP_element_8 --covers--> J101a
PROC_pump_start_order_step_03 --operatesOn--> J101a
PROC_J101b_startup_step_01 --operatesOn--> J101a
SIC101a --controls--> J101a
IL_E101_level_HH --tripsItem--> J101a
V135a --pipedTo--> J101a
PROC_pump_start_order_step_02 --operatesOn--> J101a
V135a --feedsInto--> J101a
AOI09 --about--> J101a
PROC_J101a_startup_step_07 --operatesOn--> J101a
ROI03 --about--> J101a
limit_J101_start_power --appliesTo--> J101a
PT115a --monitors--> J101a
LIC108 --controls--> J101a
CL_E101_level --hasFinalElement--> J101a
J101b --floor--> 1
J101b --pipedTo--> PCV120b
J101b --type--> Pump
J101b --gridReference--> N16
J101b --label--> J101b rich MEA pump (duty or standby)
J101b --tag--> J101b
J101b --note--> Parallel to J101a; only one runs at a time.
J101b --feedsInto--> PCV120b
ROI03 --about--> J101b
LIC108 --controls--> J101b
CL_E101_level --hasFinalElement--> J101b
IL_E101_level_LL --tripsItem--> J101b
AOI04 --about--> J101b
PROC_J101b_startup_step_07 --operatesOn--> J101b
TT111b --monitors--> J101b
PT115b --monitors--> J101b
HAZOP_element_8 --covers--> J101b
V135b --feedsInto--> J101b
IL_E101_level_HH --tripsItem--> J101b
TT110b --monitors--> J101b
V135b --pipedTo--> J101b
AOI09 --about--> J101b
PROC_J101a_startup_step_01 --operatesOn--> J101b
PROC_J101b_startup_step_02 --operatesOn--> J101b
SIC101b --controls--> J101b
AOI02 --about--> J101b
AbsRoute_J101a_step_11_FI108 --stepIndex--> 11
AbsRoute_J101a_step_11_FI108 --stepItem--> FI108
AbsRoute_J101a_step_11_FI108 --stepType--> tie-in
AbsRoute_J101a_step_11_FI108 --type--> LoopStep
AbsRoute_J101a_step_11_FI108 --label--> Absorber recirculation on J101a step 11: FI108
IL_E101_level_HH --initiatedBy--> LSHH107
IL_E101_level_HH --label--> E101 high-high level plant shutdown (LZAH107)
IL_E101_level_HH --type--> Interlock
AbsRoute_J101a_step_19_V211 --label--> Absorber recirculation on J101a step 19: V211
AbsRoute_J101a_step_19_V211 --type--> LoopStep
AbsRoute_J101a_step_19_V211 --stepType--> inline
AbsRoute_J101a_step_19_V211 --stepItem--> V211
AbsRoute_J101a_step_19_V211 --stepIndex--> 19
PROC_J101b_startup --hasProcedureStep--> PROC_J101b_startup_step_03
PROC_J101b_startup --hasProcedureStep--> PROC_J101b_startup_step_07
PROC_J101b_startup --hasProcedureStep--> PROC_J101b_startup_step_06
PROC_J101b_startup --label--> J101b start-up valve line-up
PROC_J101b_startup --hasProcedureStep--> PROC_J101b_startup_step_01
PROC_J101b_startup --type--> Procedure
PROC_J101b_startup --hasProcedureStep--> PROC_J101b_startup_step_05
PROC_J101b_startup --hasProcedureStep--> PROC_J101b_startup_step_02
PROC_J101b_startup --triggerCondition--> J101b selected as the running pump
PROC_J101b_startup --hasProcedureStep--> PROC_J101b_startup_step_04
AbsRoute_J101a_setting_V143a --label--> V143a in Absorber recirculation on J101a
AbsRoute_J101a_setting_V143a --type--> ValveSetting
AbsRoute_J101a_setting_V143a --requiredPosition--> open
AbsRoute_J101a_setting_V143a --valve--> V143a
AbsRoute_J101a --hasValveSetting--> AbsRoute_J101a_setting_V143a
PROC_J101a_startup_step_05 --operatesOn--> V143a
PROC_J101a_startup_step_05 --instruction--> Open V143a
PROC_J101a_startup_step_05 --label--> J101a start-up valve line-up step 5
PROC_J101a_startup_step_05 --requiredPosition--> open
PROC_J101a_startup_step_05 --type--> ProcedureStep
PROC_J101a_startup_step_05 --stepOrder--> 5
PROC_J101a_startup --hasProcedureStep--> PROC_J101a_startup_step_05
AbsRoute_J101b_step_19_V211 --stepIndex--> 19
AbsRoute_J101b_step_19_V211 --stepItem--> V211
AbsRoute_J101b_step_19_V211 --type--> LoopStep
AbsRoute_J101b_step_19_V211 --stepType--> inline
AbsRoute_J101b_step_19_V211 --label--> Absorber recirculation on J101b step 19: V211
AbsRoute_J101b_step_23_TT208 --label--> Absorber recirculation on J101b step 23: TT208
AbsRoute_J101b_step_23_TT208 --stepItem--> TT208
AbsRoute_J101b_step_23_TT208 --stepType--> tie-in
AbsRoute_J101b_step_23_TT208 --stepIndex--> 23
AbsRoute_J101b_step_23_TT208 --type--> LoopStep
AbsRoute_J101b_step_32_E101 --type--> LoopStep
AbsRoute_J101b_step_32_E101 --stepType--> inline
AbsRoute_J101b_step_32_E101 --label--> Absorber recirculation on J101b step 32: E101
AbsRoute_J101b_step_32_E101 --stepIndex--> 32
AbsRoute_J101b_step_32_E101 --stepItem--> E101
E101 --pipedTo--> RV400
E101 --floor--> 1
E101 --note--> Lean MEA enters at the top through NRV400; rich MEA leaves from the sump to J101a/b. The air admittance valve shown on the P&ID has been removed from the plant (DIFF, E14/15).
E101 --feedsInto--> E101_N_sump_outlet
E101 --designBasis--> Packing and column designed for 2.3-2.5 bar operation on MEA and 50 kg/h CO2 (HAZOP 10.4)
E101 --feedsInto--> E101_N_gas_outlet
E101 --pipedTo--> E101_N_sump_outlet
E101 --pipedTo--> E101_N_gas_outlet
E101 --type--> AbsorptionColumn
E101 --diameter_mm--> 230.0
E101 --tag--> E101
E101 --label--> E101 absorber
HAZOP_7_10 --concerns--> E101
TT305 --monitors--> E101
PT111 --monitors--> E101
E101_sample_5 --onColumn--> E101
E101_N_gas_outlet --onEquipment--> E101
LSLL109 --monitors--> E101
TT207 --monitors--> E101
PT403 --monitors--> E101
LI108 --monitors--> E101
E101_sample_4 --onColumn--> E101
E101_N_sump_outlet --onEquipment--> E101
FT109 --monitors--> E101
E101_sample_3 --onColumn--> E101
HAZOP_9b_05 --concerns--> E101
limit_LZAL109 --appliesTo--> E101
DI108 --monitors--> E101
E101_N_gas_inlet --feedsInto--> E101
FT304 --monitors--> E101
LT108 --monitors--> E101
K101_N2_recycle --bypasses--> E101
PT110 --monitors--> E101
E101_N_gas_inlet --pipedTo--> E101
HAZOP_5_08 --concerns--> E101
HAZOP_8_01 --concerns--> E101
HAZOP_8_06 --concerns--> E101
PI403 --monitors--> E101
AT400 --monitors--> E101
FT303 --monitors--> E101
TT205 --monitors--> E101
E101_N_base_inlet --onEquipment--> E101
aspen_v6_1_E101_performance --ofEquipment--> E101
TT206 --monitors--> E101
```

Question: If J101a fails and J101b must take over, which pump and valve changes connect the standby route into the rich MEA loop?

## Q41

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
aspen_v3_block_E101 --type--> AspenBlock
aspen_v3_block_E101 --aspenModel--> RADFRAC
aspen_v3_block_E101 --blockId--> E101
aspen_v3_block_E101 --status--> OK
aspen_v3_block_E101 --label--> E101 (ABB_pilot_plant_final_3)
aspen_v3_block_E101 --inCase--> case_aspen_v3
aspen_v3_stream_S8 --fromBlock--> aspen_v3_block_E101
aspen_v3_stream_1 --toBlock--> aspen_v3_block_E101
aspen_v3_stream_2 --toBlock--> aspen_v3_block_E101
aspen_v3_stream_4 --fromBlock--> aspen_v3_block_E101
aspen_v6_1_block_E101 --type--> AspenBlock
aspen_v6_1_block_E101 --aspenModel--> RADFRAC
aspen_v6_1_block_E101 --label--> E101 (ABB_pilot_plant_final_6_1_SA_validation)
aspen_v6_1_block_E101 --blockId--> E101
aspen_v6_1_block_E101 --status--> OK
aspen_v6_1_block_E101 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S8 --fromBlock--> aspen_v6_1_block_E101
aspen_v6_1_stream_2 --toBlock--> aspen_v6_1_block_E101
aspen_v6_1_stream_1 --toBlock--> aspen_v6_1_block_E101
aspen_v6_1_stream_4 --fromBlock--> aspen_v6_1_block_E101
E101 --pipedTo--> RV400
E101 --floor--> 1
E101 --note--> Lean MEA enters at the top through NRV400; rich MEA leaves from the sump to J101a/b. The air admittance valve shown on the P&ID has been removed from the plant (DIFF, E14/15).
E101 --feedsInto--> E101_N_sump_outlet
E101 --designBasis--> Packing and column designed for 2.3-2.5 bar operation on MEA and 50 kg/h CO2 (HAZOP 10.4)
E101 --feedsInto--> E101_N_gas_outlet
E101 --pipedTo--> E101_N_sump_outlet
E101 --pipedTo--> E101_N_gas_outlet
E101 --type--> AbsorptionColumn
E101 --diameter_mm--> 230.0
E101 --tag--> E101
E101 --label--> E101 absorber
HAZOP_7_10 --concerns--> E101
TT305 --monitors--> E101
PT111 --monitors--> E101
E101_sample_5 --onColumn--> E101
E101_N_gas_outlet --onEquipment--> E101
LSLL109 --monitors--> E101
TT207 --monitors--> E101
PT403 --monitors--> E101
LI108 --monitors--> E101
E101_sample_4 --onColumn--> E101
E101_N_sump_outlet --onEquipment--> E101
FT109 --monitors--> E101
E101_sample_3 --onColumn--> E101
HAZOP_9b_05 --concerns--> E101
limit_LZAL109 --appliesTo--> E101
DI108 --monitors--> E101
E101_N_gas_inlet --feedsInto--> E101
FT304 --monitors--> E101
LT108 --monitors--> E101
K101_N2_recycle --bypasses--> E101
PT110 --monitors--> E101
E101_N_gas_inlet --pipedTo--> E101
HAZOP_5_08 --concerns--> E101
HAZOP_8_01 --concerns--> E101
HAZOP_8_06 --concerns--> E101
PI403 --monitors--> E101
AT400 --monitors--> E101
FT303 --monitors--> E101
TT205 --monitors--> E101
E101_N_base_inlet --onEquipment--> E101
aspen_v6_1_E101_performance --ofEquipment--> E101
TT206 --monitors--> E101
HAZOP_8_03 --concerns--> E101
E101_N_gas_inlet --onEquipment--> E101
E101_N_top_inlet --feedsInto--> E101
E101_sample_6 --onColumn--> E101
K402 --pipedTo--> E101
HAZOP_5_07 --concerns--> E101
AI300 --monitors--> E101
FI109 --monitors--> E101
FI108 --monitors--> E101
aspen_v3_vent_gas --ofEquipment--> E101
AT300 --monitors--> E101
E101_N_top_inlet --pipedTo--> E101
aspen_v6_1_feed_gas --ofEquipment--> E101
limit_PSHH117_set --appliesTo--> E101
TT109 --monitors--> E101
TT412 --monitors--> E101
HAZOP_10_03 --concerns--> E101
LSHH107 --monitors--> E101
E101_sample_2 --onColumn--> E101
limit_LZAH107 --appliesTo--> E101
HAZOP_5_06 --concerns--> E101
PSHH117 --monitors--> E101
TT413 --monitors--> E101
HAZOP_7_13 --concerns--> E101
TT107 --monitors--> E101
TT306 --monitors--> E101
E101_N_top_inlet --onEquipment--> E101
E101_sample_1 --onColumn--> E101
AOI10 --about--> E101
RV400 --protects--> E101
FT108 --monitors--> E101
TT411 --monitors--> E101
TT204 --monitors--> E101
aspen_v3_feed_gas --ofEquipment--> E101
HAZOP_element_10 --covers--> E101
HAZOP_8_11 --concerns--> E101
TT307 --monitors--> E101
TT308 --monitors--> E101
HAZOP_8_02 --concerns--> E101
aspen_v3_E101_performance --ofEquipment--> E101
PCV300 --valveType--> pressure control
PCV300 --floor--> 3
PCV300 --normalPosition--> open
PCV300 --note--> Vents lean gas from the absorber to hold the E101 pressure (PIC403). Opened in the vent stream start-up (Fig F.3), closed at shutdown.
PCV300 --pipedTo--> VENT_E101
PCV300 --label--> PCV300
PCV300 --feedsInto--> VENT_E101
PCV300 --type--> PressureControlValve
PCV300 --tag--> PCV300
PCV300 --gridReference--> G18
K402 --feedsInto--> PCV300
CL_E101_pressure --hasFinalElement--> PCV300
K402 --pipedTo--> PCV300
PIC403 --controls--> PCV300
AV01 --about--> PCV300
K101 --type--> Saturator
K101 --label--> K101 gas saturator
K101 --pipedTo--> SDV170
K101 --pipedTo--> Z103
K101 --floor--> 1
K101 --feedsInto--> E101_N_gas_inlet
K101 --pipedTo--> E101_N_gas_inlet
K101 --note--> Saturates the feed gas with water before E101; temperature held by TIC121 using C106 on the recirculating water. Grid not in the REPORT lists (near L17 to L18 on the P&ID). Not modelled in Aspen (GOI09).
K101 --pipedTo--> V126
K101 --tag--> K101
DI_CARTRIDGE --feedsInto--> K101
HAZOP_4_06 --concerns--> K101
V172 --pipedTo--> K101
J102 --pipedTo--> K101
limit_LZAL_K101 --appliesTo--> K101
HAZOP_4_07 --concerns--> K101
LT104 --monitors--> K101
HAZOP_3_05 --concerns--> K101
FEED_GAS_HEADER --feedsInto--> K101
GOI09 --about--> K101
LI106 --monitors--> K101
FEED_GAS_HEADER --pipedTo--> K101
limit_LAL_K101 --appliesTo--> K101
K101_N2_recycle --fromItem--> K101
limit_LZAH_K101 --appliesTo--> K101
GOI07 --about--> K101
GOI02 --about--> K101
HAZOP_element_3 --covers--> K101
HAZOP_4_02 --concerns--> K101
TI121 --monitors--> K101
C106 --pipedTo--> K101
```

Question: How does the E101 liquid level control loop work, including its sensor and actuator?

## Q42

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
aspen_v3_block_E100 --label--> E100 (ABB_pilot_plant_final_3)
aspen_v3_block_E100 --represents--> E100
aspen_v3_block_E100 --aspenModel--> RADFRAC
aspen_v3_block_E100 --inCase--> case_aspen_v3
aspen_v3_block_E100 --status--> WARNING
aspen_v3_block_E100 --statusMessage--> FEED PRESSURE IS LOWER THAN STAGE PRESSURE.
aspen_v3_block_E100 --type--> AspenBlock
aspen_v3_block_E100 --blockId--> E100
aspen_v3_stream_S13 --fromBlock--> aspen_v3_block_E100
aspen_v3_stream_S10 --toBlock--> aspen_v3_block_E100
aspen_v3_stream_S6 --fromBlock--> aspen_v3_block_E100
aspen_v3_stream_S14 --fromBlock--> aspen_v3_block_E100
aspen_v3_stream_S24 --toBlock--> aspen_v3_block_E100
aspen_v6_1_block_E100 --inCase--> case_aspen_v6_1
aspen_v6_1_block_E100 --statusMessage--> RATESEP CALCULATIONS FAILED TO CONVERGE.
aspen_v6_1_block_E100 --status--> ERROR
aspen_v6_1_block_E100 --represents--> E100
aspen_v6_1_block_E100 --label--> E100 (ABB_pilot_plant_final_6_1_SA_validation)
aspen_v6_1_block_E100 --type--> AspenBlock
aspen_v6_1_block_E100 --blockId--> E100
aspen_v6_1_block_E100 --aspenModel--> RADFRAC
aspen_v6_1_stream_S15 --fromBlock--> aspen_v6_1_block_E100
aspen_v6_1_stream_S23 --fromBlock--> aspen_v6_1_block_E100
aspen_v6_1_stream_S10 --toBlock--> aspen_v6_1_block_E100
aspen_v6_1_stream_S12 --fromBlock--> aspen_v6_1_block_E100
aspen_v6_1_stream_S14 --toBlock--> aspen_v6_1_block_E100
E100 --floor--> 1
E100 --hasStage--> E100_stage_12
E100 --diameter_mm--> 264.62
E100 --tag--> E100
E100 --label--> E100 stripper (desorber)
E100 --hasStage--> E100_stage_08
E100 --hasStage--> E100_stage_01
E100 --hasStage--> E100_stage_04
E100 --feedsInto--> E100_N_overhead
E100 --hasStage--> E100_stage_07
E100 --pipedTo--> E100_N_overhead
E100 --note--> Chimney tray below the bottom packed bed separates the draw-off section (stage 11) from the sump (stage 12).
E100 --hasStage--> E100_stage_02
E100 --hasStage--> E100_stage_09
E100 --feedsInto--> E100_N_sump_outlet
E100 --hasStage--> E100_stage_06
E100 --feedsInto--> E100_N_drawoff
E100 --pipedTo--> E100_N_sump_outlet
E100 --hasStage--> E100_stage_05
E100 --hasStage--> E100_stage_11
E100 --hasStage--> E100_stage_10
E100 --designBasis--> Designed for sub-atmospheric pressure (vacuum), per HAZOP element 11 item 10. Design pressure value not documented.
E100 --hasStage--> E100_stage_03
E100 --pipedTo--> E100_N_drawoff
E100 --type--> StrippingColumn
TT200 --monitors--> E100
PI401 --monitors--> E100
TT401 --monitors--> E100
PROC_reboiler_heating_step_06 --operatesOn--> E100
HAZOP_13_13 --concerns--> E100
HAZOP_11_13 --concerns--> E100
LT101 --monitors--> E100
E100_N_sump_outlet --onEquipment--> E100
LSLL102 --monitors--> E100
HAZOP_11_12 --concerns--> E100
OI06 --about--> E100
LSHH100 --monitors--> E100
aspen_v6_1_E100_performance --ofEquipment--> E100
E100_N_overhead --onEquipment--> E100
TT302 --monitors--> E100
HAZOP_7_10 --concerns--> E100
HAZOP_6_07 --concerns--> E100
HAZOP_11_15 --concerns--> E100
E100_N_top_inlet --feedsInto--> E100
PT402 --monitors--> E100
PT401 --monitors--> E100
E100_N_drawoff --onEquipment--> E100
E100_N_side_inlet --onEquipment--> E100
limit_LT101_operating_window --appliesTo--> E100
limit_LZAH100 --appliesTo--> E100
HAZOP_9b_05 --concerns--> E100
RV401 --protects--> E100
E100_N_top_inlet --pipedTo--> E100
E100_N_top_inlet --onEquipment--> E100
HAZOP_13_12 --concerns--> E100
aspen_v3_E100_performance --ofEquipment--> E100
TT301 --monitors--> E100
TT400 --monitors--> E100
HAZOP_7_15 --concerns--> E100
HAZOP_element_11 --covers--> E100
limit_LT101_low_alarm --appliesTo--> E100
TT303 --monitors--> E100
OI11 --about--> E100
limit_PSHH116_set --appliesTo--> E100
HAZOP_13_11 --concerns--> E100
E100_N_reboiler_return --feedsInto--> E100
limit_PSHH400_set --appliesTo--> E100
OI03 --about--> E100
TT103 --monitors--> E100
PSHH400 --monitors--> E100
E100_N_reboiler_return --pipedTo--> E100
HAZOP_8_01 --concerns--> E100
PT102 --monitors--> E100
PSHH116 --monitors--> E100
TT203 --monitors--> E100
limit_LZAL102 --appliesTo--> E100
TT201 --monitors--> E100
HAZOP_6_08 --concerns--> E100
TT300 --monitors--> E100
HAZOP_11_01 --concerns--> E100
E100_N_reboiler_return --onEquipment--> E100
TT202 --monitors--> E100
LSHH100 --tag--> LSHH100
LSHH100 --note--> Stage mapping inferred: odd Aspen stages are the gaps between packed beds where the side instruments sit; floors match REPORT.
LSHH100 --locatedAtStage--> E100_stage_12
LSHH100 --type--> LevelInstrument
LSHH100 --measuredVariable--> level high-high switch
LSHH100 --floor--> 1
LSHH100 --label--> LSHH100
IL_E100_level_HH --initiatedBy--> LSHH100
PT402 --tag--> PT402
PT402 --monitors--> K401
PT402 --measuredVariable--> pressure after K401
PT402 --gridReference--> C16
PT402 --type--> PressureInstrument
PT402 --signalType--> Fieldbus
PT402 --floor--> 4
PT402 --sensorType--> gauge pressure transmitter
PT402 --label--> PT402
HAZOP_12_02 --concerns--> PT402
HAZOP_element_12 --covers--> PT402
CL_E100_pressure --hasSensor--> PT402
NRV106 --tag--> NRV106
NRV106 --valveType--> check
NRV106 --floor--> 1
NRV106 --note--> Near V112 at the E100 sump outlet. FI07
NRV106 --type--> CheckValve
NRV106 --label--> NRV106
NRV106 --gridReference--> M8
Route_D_side_bypass_step_38_E100 --stepIndex--> 38
Route_D_side_bypass_step_38_E100 --label--> Route D: side return (stage 3), Z102 bypassed step 38: E100
Route_D_side_bypass_step_38_E100 --stepType--> inline
Route_D_side_bypass_step_38_E100 --stepItem--> E100
Route_D_side_bypass_step_38_E100 --type--> LoopStep
Route_D_side_bypass_step_37_E100_N_side_inlet --nextStep--> Route_D_side_bypass_step_38_E100
Route_B_top_bypass_step_10_E100 --nextStep--> Route_B_top_bypass_step_11_E100_N_sump_outlet
Route_B_top_bypass_step_10_E100 --stepItem--> E100
Route_B_top_bypass_step_10_E100 --stepIndex--> 10
Route_B_top_bypass_step_10_E100 --stepType--> inline
Route_B_top_bypass_step_10_E100 --type--> LoopStep
Route_B_top_bypass_step_10_E100 --label--> Route B: top return (stage 1), Z102 bypassed step 10: E100
Route_B_top_bypass_step_09_E100_N_reboiler_return --nextStep--> Route_B_top_bypass_step_10_E100
aspen_v3_stream_S10 --temperature_C--> 89.99877
aspen_v3_stream_S10 --phase--> MIXED
```

Question: Describe the stripper pressure control loop and the alternative measurement channels.

## Q43

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
PT403 --monitors--> E101
PT403 --gridReference--> D16
PT403 --type--> PressureInstrument
PT403 --measuredVariable--> absorber (E101) pressure
PT403 --label--> PT403
PT403 --signalType--> Fieldbus
PT403 --tag--> PT403
PT403 --floor--> 4
PT403 --sensorType--> gauge pressure transmitter
CL_E101_pressure --hasSensor--> PT403
aspen_v3_block_E101 --type--> AspenBlock
aspen_v3_block_E101 --aspenModel--> RADFRAC
aspen_v3_block_E101 --blockId--> E101
aspen_v3_block_E101 --status--> OK
aspen_v3_block_E101 --label--> E101 (ABB_pilot_plant_final_3)
aspen_v3_block_E101 --inCase--> case_aspen_v3
aspen_v3_stream_S8 --fromBlock--> aspen_v3_block_E101
aspen_v3_stream_1 --toBlock--> aspen_v3_block_E101
aspen_v3_stream_2 --toBlock--> aspen_v3_block_E101
aspen_v3_stream_4 --fromBlock--> aspen_v3_block_E101
aspen_v6_1_block_E101 --type--> AspenBlock
aspen_v6_1_block_E101 --aspenModel--> RADFRAC
aspen_v6_1_block_E101 --label--> E101 (ABB_pilot_plant_final_6_1_SA_validation)
aspen_v6_1_block_E101 --blockId--> E101
aspen_v6_1_block_E101 --status--> OK
aspen_v6_1_block_E101 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S8 --fromBlock--> aspen_v6_1_block_E101
aspen_v6_1_stream_2 --toBlock--> aspen_v6_1_block_E101
aspen_v6_1_stream_1 --toBlock--> aspen_v6_1_block_E101
aspen_v6_1_stream_4 --fromBlock--> aspen_v6_1_block_E101
E101 --pipedTo--> RV400
E101 --floor--> 1
E101 --note--> Lean MEA enters at the top through NRV400; rich MEA leaves from the sump to J101a/b. The air admittance valve shown on the P&ID has been removed from the plant (DIFF, E14/15).
E101 --feedsInto--> E101_N_sump_outlet
E101 --designBasis--> Packing and column designed for 2.3-2.5 bar operation on MEA and 50 kg/h CO2 (HAZOP 10.4)
E101 --feedsInto--> E101_N_gas_outlet
E101 --pipedTo--> E101_N_sump_outlet
E101 --pipedTo--> E101_N_gas_outlet
E101 --type--> AbsorptionColumn
E101 --diameter_mm--> 230.0
E101 --tag--> E101
E101 --label--> E101 absorber
HAZOP_7_10 --concerns--> E101
TT305 --monitors--> E101
PT111 --monitors--> E101
E101_sample_5 --onColumn--> E101
E101_N_gas_outlet --onEquipment--> E101
LSLL109 --monitors--> E101
TT207 --monitors--> E101
LI108 --monitors--> E101
E101_sample_4 --onColumn--> E101
E101_N_sump_outlet --onEquipment--> E101
FT109 --monitors--> E101
E101_sample_3 --onColumn--> E101
HAZOP_9b_05 --concerns--> E101
limit_LZAL109 --appliesTo--> E101
DI108 --monitors--> E101
E101_N_gas_inlet --feedsInto--> E101
FT304 --monitors--> E101
LT108 --monitors--> E101
K101_N2_recycle --bypasses--> E101
PT110 --monitors--> E101
E101_N_gas_inlet --pipedTo--> E101
HAZOP_5_08 --concerns--> E101
HAZOP_8_01 --concerns--> E101
HAZOP_8_06 --concerns--> E101
PI403 --monitors--> E101
AT400 --monitors--> E101
FT303 --monitors--> E101
TT205 --monitors--> E101
E101_N_base_inlet --onEquipment--> E101
aspen_v6_1_E101_performance --ofEquipment--> E101
TT206 --monitors--> E101
HAZOP_8_03 --concerns--> E101
E101_N_gas_inlet --onEquipment--> E101
E101_N_top_inlet --feedsInto--> E101
E101_sample_6 --onColumn--> E101
K402 --pipedTo--> E101
HAZOP_5_07 --concerns--> E101
AI300 --monitors--> E101
FI109 --monitors--> E101
FI108 --monitors--> E101
aspen_v3_vent_gas --ofEquipment--> E101
AT300 --monitors--> E101
E101_N_top_inlet --pipedTo--> E101
aspen_v6_1_feed_gas --ofEquipment--> E101
limit_PSHH117_set --appliesTo--> E101
TT109 --monitors--> E101
TT412 --monitors--> E101
HAZOP_10_03 --concerns--> E101
LSHH107 --monitors--> E101
E101_sample_2 --onColumn--> E101
limit_LZAH107 --appliesTo--> E101
HAZOP_5_06 --concerns--> E101
PSHH117 --monitors--> E101
TT413 --monitors--> E101
HAZOP_7_13 --concerns--> E101
TT107 --monitors--> E101
TT306 --monitors--> E101
E101_N_top_inlet --onEquipment--> E101
E101_sample_1 --onColumn--> E101
AOI10 --about--> E101
RV400 --protects--> E101
FT108 --monitors--> E101
TT411 --monitors--> E101
TT204 --monitors--> E101
aspen_v3_feed_gas --ofEquipment--> E101
HAZOP_element_10 --covers--> E101
HAZOP_8_11 --concerns--> E101
TT307 --monitors--> E101
TT308 --monitors--> E101
HAZOP_8_02 --concerns--> E101
aspen_v3_E101_performance --ofEquipment--> E101
PCV300 --valveType--> pressure control
PCV300 --floor--> 3
PCV300 --normalPosition--> open
PCV300 --note--> Vents lean gas from the absorber to hold the E101 pressure (PIC403). Opened in the vent stream start-up (Fig F.3), closed at shutdown.
PCV300 --pipedTo--> VENT_E101
PCV300 --label--> PCV300
PCV300 --feedsInto--> VENT_E101
PCV300 --type--> PressureControlValve
PCV300 --tag--> PCV300
PCV300 --gridReference--> G18
K402 --feedsInto--> PCV300
CL_E101_pressure --hasFinalElement--> PCV300
K402 --pipedTo--> PCV300
PIC403 --controls--> PCV300
AV01 --about--> PCV300
K101 --type--> Saturator
K101 --label--> K101 gas saturator
K101 --pipedTo--> SDV170
K101 --pipedTo--> Z103
K101 --floor--> 1
K101 --feedsInto--> E101_N_gas_inlet
K101 --pipedTo--> E101_N_gas_inlet
K101 --note--> Saturates the feed gas with water before E101; temperature held by TIC121 using C106 on the recirculating water. Grid not in the REPORT lists (near L17 to L18 on the P&ID). Not modelled in Aspen (GOI09).
K101 --pipedTo--> V126
K101 --tag--> K101
DI_CARTRIDGE --feedsInto--> K101
HAZOP_4_06 --concerns--> K101
V172 --pipedTo--> K101
J102 --pipedTo--> K101
limit_LZAL_K101 --appliesTo--> K101
HAZOP_4_07 --concerns--> K101
LT104 --monitors--> K101
HAZOP_3_05 --concerns--> K101
FEED_GAS_HEADER --feedsInto--> K101
GOI09 --about--> K101
LI106 --monitors--> K101
FEED_GAS_HEADER --pipedTo--> K101
```

Question: What happens in the absorber pressure control loop when PT403 indicates pressure above the set point?

## Q44

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
H100 --tag--> H100
H100 --floor--> 1
H100 --source--> SUMMARY p.102
H100 --type--> SteamReboiler
H100 --feedsInto--> Q106
H100 --pipedTo--> Q106
H100 --label--> H100 vertical thermosiphon steam reboiler
FI102 --monitors--> H100
H100_N_condensate_out --onEquipment--> H100
TT100 --monitors--> H100
aspen_v3_H100_performance --ofEquipment--> H100
FT101 --monitors--> H100
HAZOP_element_13 --covers--> H100
aspen_v6_1_block_H100 --represents--> H100
TI100 --monitors--> H100
PROC_reboiler_heating_step_04 --operatesOn--> H100
DI100 --monitors--> H100
limit_H100_steam_limit --appliesTo--> H100
PI101 --monitors--> H100
PI100 --monitors--> H100
aspen_v3_block_H100REAC --represents--> H100
PT101 --monitors--> H100
FT102 --monitors--> H100
aspen_v3_block_H100HEAT --represents--> H100
TT117 --monitors--> H100
TT118 --monitors--> H100
FI100 --monitors--> H100
Q105 --pipedTo--> H100
H100_N_steam_in --onEquipment--> H100
Q105 --feedsInto--> H100
aspen_v6_1_H100_performance --ofEquipment--> H100
FT100 --monitors--> H100
HAZOP_element_11 --covers--> H100
RV107 --protects--> H100
aspen_v6_1_block_H100 --label--> H100 (ABB_pilot_plant_final_6_1_SA_validation)
aspen_v6_1_block_H100 --blockId--> H100
aspen_v6_1_block_H100 --aspenModel--> HEATX
aspen_v6_1_block_H100 --type--> AspenBlock
aspen_v6_1_block_H100 --statusMessage--> INVALID INPUT SPECIFICATIONS SEE TASC BROWSER FOR INFO.
aspen_v6_1_block_H100 --status--> ERROR
aspen_v6_1_block_H100 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S14 --fromBlock--> aspen_v6_1_block_H100
aspen_v6_1_stream_S17 --fromBlock--> aspen_v6_1_block_H100
aspen_v6_1_stream_S31 --toBlock--> aspen_v6_1_block_H100
aspen_v6_1_stream_S23 --toBlock--> aspen_v6_1_block_H100
PROC_reboiler_heating_step_01 --operatesOn--> FT100
PROC_reboiler_heating_step_01 --stepOrder--> 1
PROC_reboiler_heating_step_01 --instruction--> Check whether FT100 and FT101 show steam flowing to H100
PROC_reboiler_heating_step_01 --type--> ProcedureStep
PROC_reboiler_heating_step_01 --label--> Reboiler heating the MEA during the stripping loop test step 1
PROC_reboiler_heating --hasProcedureStep--> PROC_reboiler_heating_step_01
aspen_v6_1_stream_S14 --massFlow_kg_h--> 199.9608
aspen_v6_1_stream_S14 --co2Loading_mol_mol--> 0.638118
aspen_v6_1_stream_S14 --waterFlow_kg_h--> 156.4997
aspen_v6_1_stream_S14 --temperature_C--> 89.36771
aspen_v6_1_stream_S14 --pressure_bar--> 2.05248
aspen_v6_1_stream_S14 --type--> StreamState
aspen_v6_1_stream_S14 --label--> S14 (ABB_pilot_plant_final_6_1_SA_validation)
aspen_v6_1_stream_S14 --streamId--> S14
aspen_v6_1_stream_S14 --moleFlow_kmol_h--> 9.279221
aspen_v6_1_stream_S14 --vapourFraction--> 0.0
aspen_v6_1_stream_S14 --phase--> LIQUID
aspen_v6_1_stream_S14 --apparentCO2_kg_h--> 13.05912
aspen_v6_1_stream_S14 --meaMassFraction--> 0.1420495
aspen_v6_1_stream_S14 --enthalpyFlow_W--> -759156.0
aspen_v6_1_stream_S14 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S14 --toBlock--> aspen_v6_1_block_E100
SteamRoute_step_19_V103 --label--> Steam and condensate route to H100 step 19: V103
SteamRoute_step_19_V103 --stepItem--> V103
SteamRoute_step_19_V103 --stepType--> inline
SteamRoute_step_19_V103 --stepIndex--> 19
SteamRoute_step_19_V103 --type--> LoopStep
SteamRoute --hasStep--> SteamRoute_step_17_K100
SteamRoute --hasStep--> SteamRoute_step_15_PI101
SteamRoute --hasStep--> SteamRoute_step_21_V105
SteamRoute --hasStep--> SteamRoute_step_02_V100
SteamRoute --hasStep--> SteamRoute_step_20_V104
SteamRoute --hasStep--> SteamRoute_step_04_PI100
SteamRoute --hasStep--> SteamRoute_step_13_H100_N_condensate_out
SteamRoute --hasStep--> SteamRoute_step_01_XV140
SteamRoute --type--> Loop
SteamRoute --hasStep--> SteamRoute_step_14_TT118
SteamRoute --hasStep--> SteamRoute_step_07_FI100
SteamRoute --hasStep--> SteamRoute_step_11_TT117
SteamRoute --hasStep--> SteamRoute_step_16_RV107
SteamRoute --hasStep--> SteamRoute_step_22_NRV110
SteamRoute --hasStep--> SteamRoute_step_03_PT101
SteamRoute --note--> Building steam heats the MEA in the H100 reboiler shell and leaves as condensate through the K100 trap. FCV110 sets the steam flow (TIC100 > FIC100 cascade, stripping loop).
SteamRoute --inMode--> FigureOfEight
SteamRoute --hasStep--> SteamRoute_step_09_FT101
SteamRoute --hasStep--> SteamRoute_step_12_H100_N_steam_in
SteamRoute --hasStep--> SteamRoute_step_19_V103
SteamRoute --hasStep--> SteamRoute_step_05_V101
SteamRoute --hasStep--> SteamRoute_step_06_FT100
SteamRoute --hasStep--> SteamRoute_step_08_V102
SteamRoute --hasStep--> SteamRoute_step_10_FCV110
SteamRoute --label--> Steam and condensate route to H100
SteamRoute --hasStep--> SteamRoute_step_00_STEAM_SUPPLY
SteamRoute --hasStep--> SteamRoute_step_23_CONDENSATE_RETURN
SteamRoute --hasStep--> SteamRoute_step_18_V106
aspen_v3_H100_performance --coldInlet_C--> 116.8438
aspen_v3_H100_performance --label--> H100 performance (ABB_pilot_plant_final_3)
aspen_v3_H100_performance --coldSideDuty_kW--> 115.5427
aspen_v3_H100_performance --type--> HeatExchangerPerformance
aspen_v3_H100_performance --lmtd_K--> 32.8462
aspen_v3_H100_performance --area_m2--> 61.6081
aspen_v3_H100_performance --hotOutlet_C--> 118.2011
aspen_v3_H100_performance --derivedBy--> heat_mass_transfer.py
aspen_v3_H100_performance --minApproach_K--> 1.357255
aspen_v3_H100_performance --temperatureCross--> false
aspen_v3_H100_performance --overallU_W_m2K--> 448.1082
aspen_v3_H100_performance --hotInlet_C--> 276.85
aspen_v3_H100_performance --effectiveness--> 0.9911752
aspen_v3_H100_performance --hotSideDuty_kW--> 115.5827
aspen_v3_H100_performance --coldOutlet_C--> 119.3414
aspen_v3_H100_performance --duty_kW--> 115.5627
aspen_v3_H100_performance --energyBalanceError_pct--> 0.03452101
aspen_v3_H100_performance --ua_W_K--> 3517.69
aspen_v3_H100_performance --inCase--> case_aspen_v3
V102 --label--> V102
V102 --note--> Steam side of H100. Closed in the stripping loop test: no steam (REPORT Fig E.1).
V102 --feedsInto--> FT101
V102 --tag--> V102
V102 --pipedTo--> FT101
V102 --type--> ManualValve
V102 --normalPosition--> closed
V102 --gridReference--> L4
V102 --valveType--> ball
V102 --floor--> 1
FT100 --feedsInto--> V102
FT100 --pipedTo--> V102
PROC_stripping_loop_lineup_step_08 --operatesOn--> V102
PROC_H100_steam_bypass_step_05 --operatesOn--> V102
HAZOP_element_13 --covers--> V102
case_aspen_v6_1 --converged--> false
case_aspen_v6_1 --representsMode--> FigureOfEight
case_aspen_v6_1 --savedOn--> Thu Feb 27 15:14:32 2025
case_aspen_v6_1 --recommendedForUse--> false
case_aspen_v6_1 --aspenFile--> ABB_pilot_plant_final_6_1_SA_validation.apwz
case_aspen_v6_1 --label--> ABB_pilot_plant_final_6_1_SA_validation
case_aspen_v6_1 --aspenVersion--> 37.0
case_aspen_v6_1 --note--> Rescaled to pilot conditions with a sensitivity study for validation. Saved results did not converge: E100 RateSep failed, H100 invalid input, C100 temperature crossover, recycle opened at S3BACKUP.
case_aspen_v6_1 --type--> SimulationCase
aspen_v6_1_block_E100 --inCase--> case_aspen_v6_1
aspen_v6_1_block_C400COND --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S21 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_PURGE --inCase--> case_aspen_v6_1
aspen_v6_1_E100_stage_02 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S4 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S17 --inCase--> case_aspen_v6_1
```

Question: Explain the master and slave controllers used to regulate heating through H100.

## Q45

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
C200 --note--> Cools lean MEA before the absorber; cooling water flow set by FIC201 (cascade from TIC210).
C200 --type--> TrimCooler
C200 --feedsInto--> NRV400
C200 --floor--> 2
C200 --tag--> C200
C200 --label--> C200 lean MEA trim cooler (water cooled)
C200 --pipedTo--> NRV400
HAZOP_7_12 --concerns--> C200
HAZOP_10_07 --concerns--> C200
N200_bypass --toItem--> C200
TT209 --monitors--> C200
V212 --pipedTo--> C200
TI210 --monitors--> C200
V213 --feedsInto--> C200
aspen_v6_1_C200_performance --ofEquipment--> C200
TT208 --monitors--> C200
V213 --pipedTo--> C200
FI201 --monitors--> C200
FT201 --monitors--> C200
C200_N_cw_in --onEquipment--> C200
HAZOP_element_7 --covers--> C200
FI200 --monitors--> C200
aspen_v3_C200_performance --ofEquipment--> C200
TT210 --monitors--> C200
C200_N_cw_out --onEquipment--> C200
aspen_v3_block_C200 --label--> C200 (ABB_pilot_plant_final_3)
aspen_v3_block_C200 --status--> OK
aspen_v3_block_C200 --inCase--> case_aspen_v3
aspen_v3_block_C200 --blockId--> C200
aspen_v3_block_C200 --aspenModel--> HEATER
aspen_v3_block_C200 --type--> AspenBlock
aspen_v3_stream_S2 --toBlock--> aspen_v3_block_C200
aspen_v3_stream_2 --fromBlock--> aspen_v3_block_C200
C200_N_cw_out__utlcit01 --type--> Citation
C200_N_cw_out__utlcit01 --label--> Citation 1 for C200_N_cw_out (utl)
C200_N_cw_out__utlcit01 --document--> SRC_PID
C200_N_cw_out__utlcit01 --citationText--> P&ID C200
C200_N_cw_out__utlcit01 --location--> C200
C200_N_cw_in__utlcit01 --label--> Citation 1 for C200_N_cw_in (utl)
C200_N_cw_in__utlcit01 --type--> Citation
C200_N_cw_in__utlcit01 --document--> SRC_PID
C200_N_cw_in__utlcit01 --citationText--> P&ID C200
C200_N_cw_in__utlcit01 --location--> C200
aspen_v6_1_block_C200 --blockId--> C200
aspen_v6_1_block_C200 --type--> AspenBlock
aspen_v6_1_block_C200 --label--> C200 (ABB_pilot_plant_final_6_1_SA_validation)
aspen_v6_1_block_C200 --inCase--> case_aspen_v6_1
aspen_v6_1_block_C200 --status--> OK
aspen_v6_1_block_C200 --aspenModel--> HEATER
aspen_v6_1_stream_2 --fromBlock--> aspen_v6_1_block_C200
aspen_v6_1_stream_S2 --toBlock--> aspen_v6_1_block_C200
C200__abscit02 --label--> Citation 2 for C200 (absorption loop)
C200__abscit02 --type--> Citation
C200__abscit02 --document--> SRC_REPORT
C200__abscit02 --location--> section 3 (C200 is a trim cooler, second floor)
C200__abscit02 --citationText--> Pilot Plant Report section 3 (C200 is a trim cooler, second floor)
C200__abscit03 --location--> block C200
C200__abscit03 --type--> Citation
C200__abscit03 --citationText--> Aspen v3 block C200
C200__abscit03 --document--> SRC_ASPEN_V3
C200__abscit03 --label--> Citation 3 for C200 (absorption loop)
HAZOP_11_07 --label--> HAZOP 11.7
HAZOP_11_07 --cause--> Any failure of the system pressure control
HAZOP_11_07 --guideword--> HIGHER
HAZOP_11_07 --type--> HazopDeviation
HAZOP_11_07 --consequence--> Increased degradation of MEA (slight)
HAZOP_11_07 --itemNumber--> 7
HAZOP_11_07 --inElement--> HAZOP_element_11
HAZOP_11_07 --parameter--> TEMP.
HAZOP_11_07 --actionTaken--> TAH added
HAZOP_11_07 --recommendedAction--> Consider TAH on process outlet from C200
TIC210 --controls--> FCV200
TIC210 --label--> C200 outlet temperature controller (cascade master)
TIC210 --tag--> TIC210
TIC210 --type--> Controller
CL_C200_temperature --hasController--> TIC210
TT215 --signalType--> Fieldbus
TT215 --measuredVariable--> temperature near C200 (position to trace, FI05)
TT215 --floor--> 2
TT215 --sensorType--> K-type thermocouple
TT215 --gridReference--> J13
TT215 --type--> TemperatureInstrument
TT215 --label--> TT215
TT215 --tag--> TT215
AOI08 --foundBy--> absorption loop build, Oct 2026
AOI08 --itemStatus--> open
AOI08 --resolvedBy--> Site check
AOI08 --about--> FCV201
AOI08 --description--> FCV200 and FCV201 are both on the C200 cooling water line; FIC201 drives FCV200, but the role of FCV201 is not documented
AOI08 --about--> FCV200
AOI08 --type--> OpenItem
AOI08 --label--> AOI08: FCV200 and FCV201 are both on the C200 cooling water line; FIC201 drives FCV200, but the role of FCV201 is not documented
aspen_v3_stream_2 --pressure_bar--> 2.0
aspen_v3_stream_2 --moleFlow_kmol_h--> 22.9975
aspen_v3_stream_2 --massFlow_kg_h--> 552.2604
aspen_v3_stream_2 --streamId--> 2
aspen_v3_stream_2 --label--> 2 (ABB_pilot_plant_final_3)
aspen_v3_stream_2 --inCase--> case_aspen_v3
aspen_v3_stream_2 --apparentCO2_kg_h--> 31.84518
aspen_v3_stream_2 --meaMassFraction--> 0.2725138
aspen_v3_stream_2 --waterFlow_kg_h--> 369.31
aspen_v3_stream_2 --vapourFraction--> 0.0
aspen_v3_stream_2 --type--> StreamState
aspen_v3_stream_2 --toBlock--> aspen_v3_block_E101
aspen_v3_stream_2 --phase--> LIQUID
aspen_v3_stream_2 --enthalpyFlow_W--> -1905236.0
aspen_v3_stream_2 --temperature_C--> 40.0
aspen_v3_stream_2 --co2Loading_mol_mol--> 0.2936858
CL_C200_cooling_water --type--> ControlLoop
CL_C200_cooling_water --hasController--> FIC201
CL_C200_cooling_water --manipulatedVariable--> FCV200 opening
CL_C200_cooling_water --label--> Cooling water flow to C200 (cascade slave)
CL_C200_cooling_water --hasFinalElement--> FCV200
CL_C200_cooling_water --hasSensor--> FT201
CL_C200_cooling_water --controlledVariable--> Cooling water flowrate to C200
CL_C200_temperature --cascadeMasterOf--> CL_C200_cooling_water
aspen_v6_1_C200_performance --label--> C200 performance (ABB_pilot_plant_final_6_1_SA_validation)
aspen_v6_1_C200_performance --duty_kW--> 7.236044
aspen_v6_1_C200_performance --derivedBy--> build_absorption_loop.py
aspen_v6_1_C200_performance --hotInlet_C--> 70.52478
aspen_v6_1_C200_performance --note--> Lean MEA side only; Aspen models C200 as a heater block, so the cooling water side is not simulated.
aspen_v6_1_C200_performance --inCase--> case_aspen_v6_1
aspen_v6_1_C200_performance --hotOutlet_C--> 45.0
aspen_v6_1_C200_performance --type--> HeatExchangerPerformance
TT209 --sensorType--> PRT
TT209 --label--> TT209
TT209 --gridReference--> J12
TT209 --type--> TemperatureInstrument
TT209 --measuredVariable--> lean MEA entering C200
TT209 --tag--> TT209
TT209 --signalType--> Fieldbus
TT209 --floor--> 2
discrepancy_TT208_TT209_swap --concerns--> TT209
limit_TAH_C200_outlet --type--> OperatingLimit
limit_TAH_C200_outlet --unit--> C
limit_TAH_C200_outlet --limitType--> alarm
limit_TAH_C200_outlet --label--> TAH_C200_outlet
limit_TAH_C200_outlet --valueVerified--> false
limit_TAH_C200_outlet --variable--> temperature
limit_TAH_C200_outlet --source--> HAZOP element 10, item 7 (TAH added on the C200 process outlet)
limit_TAH_C200_outlet --appliesTo--> TT210
aspen_v3_C200_performance --type--> HeatExchangerPerformance
aspen_v3_C200_performance --inCase--> case_aspen_v3
aspen_v3_C200_performance --duty_kW--> 24.13058
aspen_v3_C200_performance --hotInlet_C--> 86.0
aspen_v3_C200_performance --derivedBy--> build_absorption_loop.py
aspen_v3_C200_performance --label--> C200 performance (ABB_pilot_plant_final_3)
aspen_v3_C200_performance --hotOutlet_C--> 40.0
aspen_v3_C200_performance --note--> Lean MEA side only; Aspen models C200 as a heater block, so the cooling water side is not simulated.
aspen_v3_stream_S2 --inCase--> case_aspen_v3
```

Question: How does the cascade control system maintain the lean MEA temperature after C200?

## Q46

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
C400_N_cw_out__utlcit01 --location--> C400
C400_N_cw_out__utlcit01 --type--> Citation
C400_N_cw_out__utlcit01 --document--> SRC_PID
C400_N_cw_out__utlcit01 --citationText--> P&ID C400
C400_N_cw_out__utlcit01 --label--> Citation 1 for C400_N_cw_out (utl)
aspen_v3_block_C400 --inCase--> case_aspen_v3
aspen_v3_block_C400 --aspenModel--> HEATER
aspen_v3_block_C400 --type--> AspenBlock
aspen_v3_block_C400 --blockId--> C400
aspen_v3_block_C400 --status--> OK
aspen_v3_block_C400 --label--> C400 (ABB_pilot_plant_final_3)
aspen_v3_stream_S11 --fromBlock--> aspen_v3_block_C400
aspen_v3_stream_S13 --toBlock--> aspen_v3_block_C400
C400_N_cw_in__utlcit01 --type--> Citation
C400_N_cw_in__utlcit01 --document--> SRC_PID
C400_N_cw_in__utlcit01 --citationText--> P&ID C400
C400_N_cw_in__utlcit01 --label--> Citation 1 for C400_N_cw_in (utl)
C400_N_cw_in__utlcit01 --location--> C400
aspen_v6_1_block_C400 --aspenModel--> HEATER
aspen_v6_1_block_C400 --label--> C400 (ABB_pilot_plant_final_6_1_SA_validation)
aspen_v6_1_block_C400 --blockId--> C400
aspen_v6_1_block_C400 --inCase--> case_aspen_v6_1
aspen_v6_1_block_C400 --status--> OK
aspen_v6_1_block_C400 --type--> AspenBlock
aspen_v6_1_stream_S11 --fromBlock--> aspen_v6_1_block_C400
aspen_v6_1_stream_S15 --toBlock--> aspen_v6_1_block_C400
C400 --floor--> 4
C400 --pipedTo--> K401
C400 --type--> Condenser
C400 --label--> C400 overhead condenser (spiral heat exchanger)
C400 --tag--> C400
C400 --note--> Water-cooled; cooling water flow set by FIC402 on FCV401 (cascade from TIC410). Grid not in the REPORT lists (between C8 and E10 on the P&ID).
C400 --feedsInto--> K401
E100_N_overhead --pipedTo--> C400
OOI04 --about--> C400
HAZOP_12_07 --concerns--> C400
aspen_v3_C400_performance --ofEquipment--> C400
OOI06 --about--> C400
HAZOP_12_03 --concerns--> C400
FI402 --monitors--> C400
C400_N_cw_in --onEquipment--> C400
HAZOP_6_05 --concerns--> C400
HAZOP_6_01 --concerns--> C400
C400_N_cw_out --onEquipment--> C400
PT401 --monitors--> C400
HAZOP_element_12 --covers--> C400
TI410 --monitors--> C400
limit_TAH_C400_carryover --appliesTo--> C400
FI401 --monitors--> C400
FT402 --monitors--> C400
HAZOP_6_06 --concerns--> C400
E100_N_overhead --feedsInto--> C400
TT410 --monitors--> C400
E100_N_overhead --type--> Nozzle
E100_N_overhead --onEquipment--> E100
E100_N_overhead --label--> E100 vapour outlet at the top of the column
E100 --feedsInto--> E100_N_overhead
E100 --pipedTo--> E100_N_overhead
C400__ovhcit01 --label--> Citation 1 for C400 (ovh)
C400__ovhcit01 --type--> Citation
C400__ovhcit01 --location--> overhead line after PT401, top of the drawing
C400__ovhcit01 --document--> SRC_PID
C400__ovhcit01 --citationText--> P&ID overhead line after PT401, top of the drawing
PCV415 --pipedTo--> FCV401
PCV415 --normalPosition--> open
PCV415 --note--> Pressure regulator on the C400 cooling water stream (UT09). The valve list gives floor 3.
PCV415 --floor--> 4
PCV415 --type--> PressureControlValve
PCV415 --gridReference--> C14
PCV415 --tag--> PCV415
PCV415 --feedsInto--> FCV401
PCV415 --valveType--> pressure control
PCV415 --label--> PCV415
UT09 --about--> PCV415
V405 --feedsInto--> PCV415
V405 --pipedTo--> PCV415
TIC410 --type--> Controller
TIC410 --tag--> TIC410
TIC410 --label--> C400 gas outlet temperature controller (cascade master)
TIC410 --controls--> FCV401
CL_C400_temperature --hasController--> TIC410
OOI04 --description--> Aspen returns the reflux to the rich feed before the heaters (MIXER2), but on the P&ID it joins after them at V403/V402
OOI04 --foundBy--> ovh section build, Oct 2026
OOI04 --about--> J300
OOI04 --type--> OpenItem
OOI04 --resolvedBy--> Note for model comparison; update the Aspen flowsheet if needed
OOI04 --itemStatus--> open
OOI04 --label--> OOI04: Aspen returns the reflux to the rich feed before the heaters (MIXER2), but on the P&ID it joins after them at V403/V402
HAZOP_6_01 --actionTaken--> Pump shutdown trip added
HAZOP_6_01 --consequence--> No flow to J103
HAZOP_6_01 --concerns--> J103
HAZOP_6_01 --inElement--> HAZOP_element_6
HAZOP_6_01 --cause--> K401 / C300 (now C400) blocked
HAZOP_6_01 --guideword--> NO
HAZOP_6_01 --label--> HAZOP 6.1
HAZOP_6_01 --recommendedAction--> Consider consequences of starving J103
HAZOP_6_01 --parameter--> FLOW
HAZOP_6_01 --type--> HazopDeviation
HAZOP_6_01 --itemNumber--> 1
HAZOP_6_01 --concerns--> K401
TT410 --signalType--> Fieldbus
TT410 --measuredVariable--> temperature of CO2 leaving C400
TT410 --floor--> 4
TT410 --label--> TT410
TT410 --sensorType--> PRT
TT410 --tag--> TT410
TT410 --gridReference--> C15
TT410 --type--> TemperatureInstrument
CL_C400_temperature --hasSensor--> TT410
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_07_J300
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_14_FT305
OverheadRefluxLoop --label--> Stripper overhead and reflux loop
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_09_RV300
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_02_PT401
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_03_C400
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_10_B300
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_08_TT310
OverheadRefluxLoop --note--> Runs whenever E100 is boiling. Vapour is condensed in C400; K401 separates the condensate (returned as reflux by J300) from the CO2-rich gas (to the CO2 return, piece 7).
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_06_LT401
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_05_K401
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_17_E100_N_top_inlet
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_01_E100_N_overhead
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_15_V403
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_00_E100
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_16_V402
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_12_V317
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_13_TT309
OverheadRefluxLoop --type--> Loop
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_04_LSHH400
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_11_PCV302
OverheadRefluxLoop --inMode--> FigureOfEight
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_18_E100
C400__ovhcit03 --citationText--> P&ID differences row LSHH400 (between C400 and K401)
C400__ovhcit03 --location--> row LSHH400 (between C400 and K401)
C400__ovhcit03 --document--> SRC_DIFF
C400__ovhcit03 --label--> Citation 3 for C400 (ovh)
C400__ovhcit03 --type--> Citation
C400_N_cw_in --pipedTo--> C400_N_cw_out
C400_N_cw_in --label--> C400 cooling water inlet
C400_N_cw_in --type--> Nozzle
C400_N_cw_in --feedsInto--> C400_N_cw_out
FT402 --pipedTo--> C400_N_cw_in
FT402 --feedsInto--> C400_N_cw_in
CL_C400_cooling_water --hasFinalElement--> FCV401
CL_C400_cooling_water --controlledVariable--> Cooling water flowrate to C400
CL_C400_cooling_water --manipulatedVariable--> FCV401 opening
CL_C400_cooling_water --label--> Cooling water flow to C400 (cascade slave)
CL_C400_cooling_water --hasController--> FIC402
CL_C400_cooling_water --hasSensor--> FT402
CL_C400_cooling_water --type--> ControlLoop
```

Question: What are the master sensor, slave flow measurement and final actuator for the C400 cooling control system?

## Q47

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
C106 --note--> Cools the K101 recirculating water; cooling water flow set by FIC106 on FCV102 (cascade from TIC121).
C106 --label--> C106 saturator water cooler
C106 --pipedTo--> NRV111
C106 --tag--> C106
C106 --type--> TrimCooler
C106 --floor--> 1
C106 --pipedTo--> K101
HAZOP_element_4 --covers--> C106
C106_N_cw_in --onEquipment--> C106
TT119 --monitors--> C106
FT106 --monitors--> C106
C106_N_cw_out --onEquipment--> C106
GOI03 --about--> C106
J104 --pipedTo--> C106
FI106 --monitors--> C106
C106_N_cw_in__utlcit01 --document--> SRC_PID
C106_N_cw_in__utlcit01 --citationText--> P&ID C106
C106_N_cw_in__utlcit01 --label--> Citation 1 for C106_N_cw_in (utl)
C106_N_cw_in__utlcit01 --type--> Citation
C106_N_cw_in__utlcit01 --location--> C106
C106_N_cw_out__utlcit01 --location--> C106
C106_N_cw_out__utlcit01 --type--> Citation
C106_N_cw_out__utlcit01 --document--> SRC_PID
C106_N_cw_out__utlcit01 --label--> Citation 1 for C106_N_cw_out (utl)
C106_N_cw_out__utlcit01 --citationText--> P&ID C106
K101 --type--> Saturator
K101 --label--> K101 gas saturator
K101 --pipedTo--> SDV170
K101 --pipedTo--> Z103
K101 --floor--> 1
K101 --feedsInto--> E101_N_gas_inlet
K101 --pipedTo--> E101_N_gas_inlet
K101 --note--> Saturates the feed gas with water before E101; temperature held by TIC121 using C106 on the recirculating water. Grid not in the REPORT lists (near L17 to L18 on the P&ID). Not modelled in Aspen (GOI09).
K101 --pipedTo--> V126
K101 --tag--> K101
DI_CARTRIDGE --feedsInto--> K101
HAZOP_4_06 --concerns--> K101
V172 --pipedTo--> K101
J102 --pipedTo--> K101
limit_LZAL_K101 --appliesTo--> K101
HAZOP_4_07 --concerns--> K101
LT104 --monitors--> K101
HAZOP_3_05 --concerns--> K101
FEED_GAS_HEADER --feedsInto--> K101
GOI09 --about--> K101
LI106 --monitors--> K101
FEED_GAS_HEADER --pipedTo--> K101
limit_LAL_K101 --appliesTo--> K101
K101_N2_recycle --fromItem--> K101
limit_LZAH_K101 --appliesTo--> K101
GOI07 --about--> K101
GOI02 --about--> K101
HAZOP_element_3 --covers--> K101
HAZOP_4_02 --concerns--> K101
TI121 --monitors--> K101
K103_CO2_recycle --bypasses--> K101
TT121 --monitors--> K101
DI_CARTRIDGE --pipedTo--> K101
J102 --feedsInto--> K101
V172 --feedsInto--> K101
N2ReturnLoop --hasStep--> N2ReturnLoop_step_00_E101
N2ReturnLoop --hasStep--> N2ReturnLoop_step_02_K402
N2ReturnLoop --hasStep--> N2ReturnLoop_step_15_E101_N_gas_inlet
N2ReturnLoop --inMode--> FigureOfEight
N2ReturnLoop --hasStep--> N2ReturnLoop_step_01_E101_N_gas_outlet
N2ReturnLoop --hasStep--> N2ReturnLoop_step_05_FT303
N2ReturnLoop --hasStep--> N2ReturnLoop_step_16_E101
N2ReturnLoop --hasStep--> N2ReturnLoop_step_13_FT107
N2ReturnLoop --hasStep--> N2ReturnLoop_step_07_FT304
N2ReturnLoop --note--> N2 is not absorbed, so it is recirculated: J102 blows it from the K402 overhead back through K101 into E101. Fresh N2 and CO2 (piece 5) top it up. FCV111 recycles part of it from K101 back to K102 to set the N2 flow into E101.
N2ReturnLoop --hasStep--> N2ReturnLoop_step_03_K402_N_gas_to_return
N2ReturnLoop --hasStep--> N2ReturnLoop_step_10_V187
N2ReturnLoop --hasStep--> N2ReturnLoop_step_04_TT304
N2ReturnLoop --label--> N2 return loop (E101 > K402 > K102 > J102 > K101 > E101)
N2ReturnLoop --hasStep--> N2ReturnLoop_step_12_TT114
N2ReturnLoop --hasStep--> N2ReturnLoop_step_08_FI304
N2ReturnLoop --hasStep--> N2ReturnLoop_step_14_K101
N2ReturnLoop --hasStep--> N2ReturnLoop_step_06_FI303
N2ReturnLoop --hasStep--> N2ReturnLoop_step_09_K102
N2ReturnLoop --type--> Loop
N2ReturnLoop --hasStep--> N2ReturnLoop_step_11_J102
FCV111 --floor--> 1
FCV111 --valveType--> flow control
FCV111 --tag--> FCV111
FCV111 --pipedTo--> K102
FCV111 --label--> FCV111
FCV111 --gridReference--> K17
FCV111 --type--> FlowControlValve
FCV111 --normalPosition--> open
FCV111 --note--> Recycles N2 from K101 back to K102, reducing the recycled N2 entering E101 (REPORT D.4, Fig D.6/D.7). Controlled by FIC303/FIC304 from FT303/FT304 on the N2 recycle pipe.
FIC304 --controls--> FCV111
K101_N2_recycle --routeVia--> FCV111
SDV170 --pipedTo--> FCV111
CL_N2_to_E101 --hasFinalElement--> FCV111
FIC303 --controls--> FCV111
N2ReturnLoop_step_11_J102 --label--> N2 return loop (E101 > K402 > K102 > J102 > K101 > E101) step 11: J102
N2ReturnLoop_step_11_J102 --stepItem--> J102
N2ReturnLoop_step_11_J102 --stepIndex--> 11
N2ReturnLoop_step_11_J102 --type--> LoopStep
N2ReturnLoop_step_11_J102 --stepType--> inline
NRV100b --type--> CheckValve
NRV100b --gridReference--> Q19
NRV100b --note--> Bottom right (make-up water to K101?). FI03
NRV100b --feedsInto--> DI_CARTRIDGE
NRV100b --pipedTo--> DI_CARTRIDGE
NRV100b --valveType--> check
NRV100b --label--> NRV100b
NRV100b --tag--> NRV100b
NRV100b --floor--> 1
NRV100a --feedsInto--> NRV100b
NRV100a --pipedTo--> NRV100b
N2ReturnLoop_step_04_TT304 --stepType--> tie-in
N2ReturnLoop_step_04_TT304 --type--> LoopStep
N2ReturnLoop_step_04_TT304 --label--> N2 return loop (E101 > K402 > K102 > J102 > K101 > E101) step 4: TT304
N2ReturnLoop_step_04_TT304 --stepIndex--> 4
N2ReturnLoop_step_04_TT304 --stepItem--> TT304
TT107 --label--> TT107
TT107 --signalType--> Fieldbus
TT107 --sensorType--> PRT
TT107 --floor--> 1
TT107 --measuredVariable--> gas entering E101 (after K101)
TT107 --monitors--> E101
TT107 --type--> TemperatureInstrument
TT107 --gridReference--> K18
TT107 --tag--> TT107
HAZOP_10_03 --label--> HAZOP 10.3
HAZOP_10_03 --consequence--> Overpressure lower section of E101 and K101
HAZOP_10_03 --actionTaken--> RV added
HAZOP_10_03 --itemNumber--> 3
HAZOP_10_03 --inElement--> HAZOP_element_10
HAZOP_10_03 --parameter--> FLOW
HAZOP_10_03 --cause--> High rate of gas up column from CO2 and N2 feed system
HAZOP_10_03 --type--> HazopDeviation
HAZOP_10_03 --concerns--> E101
HAZOP_10_03 --recommendedAction--> RV at outlet to K101?
HAZOP_10_03 --guideword--> MORE
FT106 --measuredVariable--> cooling water flow to C106
FT106 --sensorType--> electromagnetic volumetric flow meter
FT106 --feedsInto--> C106_N_cw_in
FT106 --gridReference--> R16
FT106 --label--> FT106
FT106 --pipedTo--> C106_N_cw_in
FT106 --type--> FlowInstrument
FT106 --signalType--> 4-20mA
FT106 --floor--> 1
FT106 --tag--> FT106
FCV102 --feedsInto--> FT106
FCV102 --pipedTo--> FT106
CL_C106_cooling_water --hasSensor--> FT106
V136 --note--> On the C106 cooling water return ('COOLING WATER TO DWG' on the P&ID).
```

Question: How is the temperature of water entering K101 regulated using C106?

## Q48

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
C400_N_cw_out__utlcit01 --location--> C400
C400_N_cw_out__utlcit01 --type--> Citation
C400_N_cw_out__utlcit01 --document--> SRC_PID
C400_N_cw_out__utlcit01 --citationText--> P&ID C400
C400_N_cw_out__utlcit01 --label--> Citation 1 for C400_N_cw_out (utl)
aspen_v3_block_C400 --inCase--> case_aspen_v3
aspen_v3_block_C400 --aspenModel--> HEATER
aspen_v3_block_C400 --type--> AspenBlock
aspen_v3_block_C400 --blockId--> C400
aspen_v3_block_C400 --status--> OK
aspen_v3_block_C400 --label--> C400 (ABB_pilot_plant_final_3)
aspen_v3_stream_S11 --fromBlock--> aspen_v3_block_C400
aspen_v3_stream_S13 --toBlock--> aspen_v3_block_C400
C400_N_cw_in__utlcit01 --type--> Citation
C400_N_cw_in__utlcit01 --document--> SRC_PID
C400_N_cw_in__utlcit01 --citationText--> P&ID C400
C400_N_cw_in__utlcit01 --label--> Citation 1 for C400_N_cw_in (utl)
C400_N_cw_in__utlcit01 --location--> C400
aspen_v6_1_block_C400 --aspenModel--> HEATER
aspen_v6_1_block_C400 --label--> C400 (ABB_pilot_plant_final_6_1_SA_validation)
aspen_v6_1_block_C400 --blockId--> C400
aspen_v6_1_block_C400 --inCase--> case_aspen_v6_1
aspen_v6_1_block_C400 --status--> OK
aspen_v6_1_block_C400 --type--> AspenBlock
aspen_v6_1_stream_S11 --fromBlock--> aspen_v6_1_block_C400
aspen_v6_1_stream_S15 --toBlock--> aspen_v6_1_block_C400
C400 --floor--> 4
C400 --pipedTo--> K401
C400 --type--> Condenser
C400 --label--> C400 overhead condenser (spiral heat exchanger)
C400 --tag--> C400
C400 --note--> Water-cooled; cooling water flow set by FIC402 on FCV401 (cascade from TIC410). Grid not in the REPORT lists (between C8 and E10 on the P&ID).
C400 --feedsInto--> K401
E100_N_overhead --pipedTo--> C400
OOI04 --about--> C400
HAZOP_12_07 --concerns--> C400
aspen_v3_C400_performance --ofEquipment--> C400
OOI06 --about--> C400
HAZOP_12_03 --concerns--> C400
FI402 --monitors--> C400
C400_N_cw_in --onEquipment--> C400
HAZOP_6_05 --concerns--> C400
HAZOP_6_01 --concerns--> C400
C400_N_cw_out --onEquipment--> C400
PT401 --monitors--> C400
HAZOP_element_12 --covers--> C400
TI410 --monitors--> C400
limit_TAH_C400_carryover --appliesTo--> C400
FI401 --monitors--> C400
FT402 --monitors--> C400
HAZOP_6_06 --concerns--> C400
E100_N_overhead --feedsInto--> C400
TT410 --monitors--> C400
E100_N_overhead --type--> Nozzle
E100_N_overhead --onEquipment--> E100
E100_N_overhead --label--> E100 vapour outlet at the top of the column
E100 --feedsInto--> E100_N_overhead
E100 --pipedTo--> E100_N_overhead
C400__ovhcit01 --label--> Citation 1 for C400 (ovh)
C400__ovhcit01 --type--> Citation
C400__ovhcit01 --location--> overhead line after PT401, top of the drawing
C400__ovhcit01 --document--> SRC_PID
C400__ovhcit01 --citationText--> P&ID overhead line after PT401, top of the drawing
PCV415 --pipedTo--> FCV401
PCV415 --normalPosition--> open
PCV415 --note--> Pressure regulator on the C400 cooling water stream (UT09). The valve list gives floor 3.
PCV415 --floor--> 4
PCV415 --type--> PressureControlValve
PCV415 --gridReference--> C14
PCV415 --tag--> PCV415
PCV415 --feedsInto--> FCV401
PCV415 --valveType--> pressure control
PCV415 --label--> PCV415
UT09 --about--> PCV415
V405 --feedsInto--> PCV415
V405 --pipedTo--> PCV415
TIC410 --type--> Controller
TIC410 --tag--> TIC410
TIC410 --label--> C400 gas outlet temperature controller (cascade master)
TIC410 --controls--> FCV401
CL_C400_temperature --hasController--> TIC410
OOI04 --description--> Aspen returns the reflux to the rich feed before the heaters (MIXER2), but on the P&ID it joins after them at V403/V402
OOI04 --foundBy--> ovh section build, Oct 2026
OOI04 --about--> J300
OOI04 --type--> OpenItem
OOI04 --resolvedBy--> Note for model comparison; update the Aspen flowsheet if needed
OOI04 --itemStatus--> open
OOI04 --label--> OOI04: Aspen returns the reflux to the rich feed before the heaters (MIXER2), but on the P&ID it joins after them at V403/V402
HAZOP_6_01 --actionTaken--> Pump shutdown trip added
HAZOP_6_01 --consequence--> No flow to J103
HAZOP_6_01 --concerns--> J103
HAZOP_6_01 --inElement--> HAZOP_element_6
HAZOP_6_01 --cause--> K401 / C300 (now C400) blocked
HAZOP_6_01 --guideword--> NO
HAZOP_6_01 --label--> HAZOP 6.1
HAZOP_6_01 --recommendedAction--> Consider consequences of starving J103
HAZOP_6_01 --parameter--> FLOW
HAZOP_6_01 --type--> HazopDeviation
HAZOP_6_01 --itemNumber--> 1
HAZOP_6_01 --concerns--> K401
TT410 --signalType--> Fieldbus
TT410 --measuredVariable--> temperature of CO2 leaving C400
TT410 --floor--> 4
TT410 --label--> TT410
TT410 --sensorType--> PRT
TT410 --tag--> TT410
TT410 --gridReference--> C15
TT410 --type--> TemperatureInstrument
CL_C400_temperature --hasSensor--> TT410
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_07_J300
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_14_FT305
OverheadRefluxLoop --label--> Stripper overhead and reflux loop
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_09_RV300
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_02_PT401
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_03_C400
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_10_B300
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_08_TT310
OverheadRefluxLoop --note--> Runs whenever E100 is boiling. Vapour is condensed in C400; K401 separates the condensate (returned as reflux by J300) from the CO2-rich gas (to the CO2 return, piece 7).
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_06_LT401
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_05_K401
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_17_E100_N_top_inlet
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_01_E100_N_overhead
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_15_V403
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_00_E100
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_16_V402
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_12_V317
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_13_TT309
OverheadRefluxLoop --type--> Loop
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_04_LSHH400
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_11_PCV302
OverheadRefluxLoop --inMode--> FigureOfEight
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_18_E100
C400__ovhcit03 --citationText--> P&ID differences row LSHH400 (between C400 and K401)
C400__ovhcit03 --location--> row LSHH400 (between C400 and K401)
C400__ovhcit03 --document--> SRC_DIFF
C400__ovhcit03 --label--> Citation 3 for C400 (ovh)
C400__ovhcit03 --type--> Citation
C400_N_cw_in --pipedTo--> C400_N_cw_out
C400_N_cw_in --label--> C400 cooling water inlet
C400_N_cw_in --type--> Nozzle
C400_N_cw_in --feedsInto--> C400_N_cw_out
FT402 --pipedTo--> C400_N_cw_in
FT402 --feedsInto--> C400_N_cw_in
CL_C400_cooling_water --hasFinalElement--> FCV401
CL_C400_cooling_water --controlledVariable--> Cooling water flowrate to C400
CL_C400_cooling_water --manipulatedVariable--> FCV401 opening
CL_C400_cooling_water --label--> Cooling water flow to C400 (cascade slave)
CL_C400_cooling_water --hasController--> FIC402
CL_C400_cooling_water --hasSensor--> FT402
CL_C400_cooling_water --type--> ControlLoop
```

Question: Which controller maintains the condensate level in C400 and how is its output implemented?

## Q49

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
aspen_v3_block_E101 --type--> AspenBlock
aspen_v3_block_E101 --aspenModel--> RADFRAC
aspen_v3_block_E101 --blockId--> E101
aspen_v3_block_E101 --status--> OK
aspen_v3_block_E101 --label--> E101 (ABB_pilot_plant_final_3)
aspen_v3_block_E101 --inCase--> case_aspen_v3
aspen_v3_stream_S8 --fromBlock--> aspen_v3_block_E101
aspen_v3_stream_1 --toBlock--> aspen_v3_block_E101
aspen_v3_stream_2 --toBlock--> aspen_v3_block_E101
aspen_v3_stream_4 --fromBlock--> aspen_v3_block_E101
aspen_v6_1_block_E101 --type--> AspenBlock
aspen_v6_1_block_E101 --aspenModel--> RADFRAC
aspen_v6_1_block_E101 --label--> E101 (ABB_pilot_plant_final_6_1_SA_validation)
aspen_v6_1_block_E101 --blockId--> E101
aspen_v6_1_block_E101 --status--> OK
aspen_v6_1_block_E101 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S8 --fromBlock--> aspen_v6_1_block_E101
aspen_v6_1_stream_2 --toBlock--> aspen_v6_1_block_E101
aspen_v6_1_stream_1 --toBlock--> aspen_v6_1_block_E101
aspen_v6_1_stream_4 --fromBlock--> aspen_v6_1_block_E101
E101 --pipedTo--> RV400
E101 --floor--> 1
E101 --note--> Lean MEA enters at the top through NRV400; rich MEA leaves from the sump to J101a/b. The air admittance valve shown on the P&ID has been removed from the plant (DIFF, E14/15).
E101 --feedsInto--> E101_N_sump_outlet
E101 --designBasis--> Packing and column designed for 2.3-2.5 bar operation on MEA and 50 kg/h CO2 (HAZOP 10.4)
E101 --feedsInto--> E101_N_gas_outlet
E101 --pipedTo--> E101_N_sump_outlet
E101 --pipedTo--> E101_N_gas_outlet
E101 --type--> AbsorptionColumn
E101 --diameter_mm--> 230.0
E101 --tag--> E101
E101 --label--> E101 absorber
HAZOP_7_10 --concerns--> E101
TT305 --monitors--> E101
PT111 --monitors--> E101
E101_sample_5 --onColumn--> E101
E101_N_gas_outlet --onEquipment--> E101
LSLL109 --monitors--> E101
TT207 --monitors--> E101
PT403 --monitors--> E101
LI108 --monitors--> E101
E101_sample_4 --onColumn--> E101
E101_N_sump_outlet --onEquipment--> E101
FT109 --monitors--> E101
E101_sample_3 --onColumn--> E101
HAZOP_9b_05 --concerns--> E101
limit_LZAL109 --appliesTo--> E101
DI108 --monitors--> E101
E101_N_gas_inlet --feedsInto--> E101
FT304 --monitors--> E101
LT108 --monitors--> E101
K101_N2_recycle --bypasses--> E101
PT110 --monitors--> E101
E101_N_gas_inlet --pipedTo--> E101
HAZOP_5_08 --concerns--> E101
HAZOP_8_01 --concerns--> E101
HAZOP_8_06 --concerns--> E101
PI403 --monitors--> E101
AT400 --monitors--> E101
FT303 --monitors--> E101
TT205 --monitors--> E101
E101_N_base_inlet --onEquipment--> E101
aspen_v6_1_E101_performance --ofEquipment--> E101
TT206 --monitors--> E101
HAZOP_8_03 --concerns--> E101
E101_N_gas_inlet --onEquipment--> E101
E101_N_top_inlet --feedsInto--> E101
E101_sample_6 --onColumn--> E101
K402 --pipedTo--> E101
HAZOP_5_07 --concerns--> E101
AI300 --monitors--> E101
FI109 --monitors--> E101
FI108 --monitors--> E101
aspen_v3_vent_gas --ofEquipment--> E101
AT300 --monitors--> E101
E101_N_top_inlet --pipedTo--> E101
aspen_v6_1_feed_gas --ofEquipment--> E101
limit_PSHH117_set --appliesTo--> E101
TT109 --monitors--> E101
TT412 --monitors--> E101
HAZOP_10_03 --concerns--> E101
LSHH107 --monitors--> E101
E101_sample_2 --onColumn--> E101
limit_LZAH107 --appliesTo--> E101
HAZOP_5_06 --concerns--> E101
PSHH117 --monitors--> E101
TT413 --monitors--> E101
HAZOP_7_13 --concerns--> E101
TT107 --monitors--> E101
TT306 --monitors--> E101
E101_N_top_inlet --onEquipment--> E101
E101_sample_1 --onColumn--> E101
AOI10 --about--> E101
RV400 --protects--> E101
FT108 --monitors--> E101
TT411 --monitors--> E101
TT204 --monitors--> E101
aspen_v3_feed_gas --ofEquipment--> E101
HAZOP_element_10 --covers--> E101
HAZOP_8_11 --concerns--> E101
TT307 --monitors--> E101
TT308 --monitors--> E101
HAZOP_8_02 --concerns--> E101
aspen_v3_E101_performance --ofEquipment--> E101
PCV300 --valveType--> pressure control
PCV300 --floor--> 3
PCV300 --normalPosition--> open
PCV300 --note--> Vents lean gas from the absorber to hold the E101 pressure (PIC403). Opened in the vent stream start-up (Fig F.3), closed at shutdown.
PCV300 --pipedTo--> VENT_E101
PCV300 --label--> PCV300
PCV300 --feedsInto--> VENT_E101
PCV300 --type--> PressureControlValve
PCV300 --tag--> PCV300
PCV300 --gridReference--> G18
K402 --feedsInto--> PCV300
CL_E101_pressure --hasFinalElement--> PCV300
K402 --pipedTo--> PCV300
PIC403 --controls--> PCV300
AV01 --about--> PCV300
K101 --type--> Saturator
K101 --label--> K101 gas saturator
K101 --pipedTo--> SDV170
K101 --pipedTo--> Z103
K101 --floor--> 1
K101 --feedsInto--> E101_N_gas_inlet
K101 --pipedTo--> E101_N_gas_inlet
K101 --note--> Saturates the feed gas with water before E101; temperature held by TIC121 using C106 on the recirculating water. Grid not in the REPORT lists (near L17 to L18 on the P&ID). Not modelled in Aspen (GOI09).
K101 --pipedTo--> V126
K101 --tag--> K101
DI_CARTRIDGE --feedsInto--> K101
HAZOP_4_06 --concerns--> K101
V172 --pipedTo--> K101
J102 --pipedTo--> K101
limit_LZAL_K101 --appliesTo--> K101
HAZOP_4_07 --concerns--> K101
LT104 --monitors--> K101
HAZOP_3_05 --concerns--> K101
FEED_GAS_HEADER --feedsInto--> K101
GOI09 --about--> K101
LI106 --monitors--> K101
FEED_GAS_HEADER --pipedTo--> K101
limit_LAL_K101 --appliesTo--> K101
K101_N2_recycle --fromItem--> K101
limit_LZAH_K101 --appliesTo--> K101
GOI07 --about--> K101
GOI02 --about--> K101
HAZOP_element_3 --covers--> K101
HAZOP_4_02 --concerns--> K101
TI121 --monitors--> K101
C106 --pipedTo--> K101
```

Question: How does the control system regulate nitrogen return flow towards the absorber?

## Q50

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
H200b --pipedTo--> V309
H200b --tag--> H200b
H200b --type--> ElectricHeater
H200b --feedsInto--> V403
H200b --pipedTo--> V403
H200b --label--> H200b electric heater
H200b --floor--> 2
H200b --gridReference--> J11
TIC213b --controls--> H200b
TSHH212b --monitors--> H200b
IL_H200b_HH --tripsItem--> H200b
OI13 --about--> H200b
TZAHH212b --controls--> H200b
PROC_heater_overtemperature_step_03 --operatesOn--> H200b
aspen_v3_H200b_performance --ofEquipment--> H200b
OI01 --about--> H200b
aspen_v6_1_block_H200B --represents--> H200b
OI06 --about--> H200b
limit_TSHH212b --appliesTo--> H200b
TT212b --monitors--> H200b
IL_heater_outlet_H --tripsItem--> H200b
SDV125 --feedsInto--> H200b
aspen_v3_block_H200B --represents--> H200b
TY213b --controls--> H200b
SDV125 --pipedTo--> H200b
SDV152 --pipedTo--> H200b
OI09 --about--> H200b
aspen_v6_1_H200b_performance --ofEquipment--> H200b
TZH213 --controls--> H200b
CL_H200b_temperature --hasFinalElement--> H200b
HS200b --controls--> H200b
H200a --label--> H200a electric heater
H200a --type--> ElectricHeater
H200a --feedsInto--> V403
H200a --tag--> H200a
H200a --pipedTo--> V403
H200a --floor--> 2
H200a --pipedTo--> V309
H200a --gridReference--> J10
SDV125 --pipedTo--> H200a
IL_H200a_HH --tripsItem--> H200a
SDV152 --pipedTo--> H200a
TY213a --controls--> H200a
TT212a --monitors--> H200a
OI09 --about--> H200a
limit_TSHH212a --appliesTo--> H200a
aspen_v6_1_H200a_performance --ofEquipment--> H200a
TZH213 --controls--> H200a
CL_H200a_temperature --hasFinalElement--> H200a
PROC_heater_overtemperature_step_02 --operatesOn--> H200a
TZAHH212a --controls--> H200a
OI13 --about--> H200a
PROC_heater_overtemperature_step_06 --operatesOn--> H200a
aspen_v3_H200a_performance --ofEquipment--> H200a
TIC213a --controls--> H200a
HS200a --controls--> H200a
aspen_v3_block_H200A --represents--> H200a
aspen_v6_1_block_H200A --represents--> H200a
OI01 --about--> H200a
OI06 --about--> H200a
TSHH212a --monitors--> H200a
IL_heater_outlet_H --tripsItem--> H200a
SDV125 --feedsInto--> H200a
Route_B_top_bypass_step_33_H200b --stepItem--> H200b
Route_B_top_bypass_step_33_H200b --stepIndex--> 33
Route_B_top_bypass_step_33_H200b --nextStep--> Route_B_top_bypass_step_36_V403
Route_B_top_bypass_step_33_H200b --label--> Route B: top return (stage 1), Z102 bypassed step 33: H200b
Route_B_top_bypass_step_33_H200b --type--> LoopStep
Route_B_top_bypass_step_33_H200b --stepType--> inline
Route_B_top_bypass_step_32_SDV125 --nextStep--> Route_B_top_bypass_step_33_H200b
IL_H200a_HH --label--> H200a high-high temperature trip
IL_H200a_HH --type--> Interlock
IL_H200a_HH --initiatedBy--> TSHH212a
IL_H200a_HH --initiatedBy--> TT212a
OI06 --description--> No Aspen case for the stripping loop test or the side return; loop-mode duties and loadings are unknown
OI06 --label--> OI06: No Aspen case for the stripping loop test or the side return; loop-mode duties and loadings are unknown
OI06 --about--> E100
OI06 --type--> OpenItem
OI06 --foundBy--> R20, A11
OI06 --resolvedBy--> A converged Aspen case for the loop line-up, or plant data from a loop run
OI06 --itemStatus--> open
PROC_heater_overtemperature_step_02 --label--> MEA entering E100 too hot (heater over-temperature) step 2
PROC_heater_overtemperature_step_02 --instruction--> If the set point is 25 C and the MEA temperature is still rising, manually shut off H200a
PROC_heater_overtemperature_step_02 --stepOrder--> 2
PROC_heater_overtemperature_step_02 --type--> ProcedureStep
PROC_heater_overtemperature --hasProcedureStep--> PROC_heater_overtemperature_step_02
StripperRecirculation --label--> Stripping loop only, absorber isolated, lean returned via SDV125 and H200a/b
StripperRecirculation --type--> OperatingMode
StrippingLoop --inMode--> StripperRecirculation
Route_B_top_bypass --inMode--> StripperRecirculation
Route_C_side_filter --inMode--> StripperRecirculation
Route_A_top_filter --inMode--> StripperRecirculation
Route_D_side_bypass --inMode--> StripperRecirculation
StrippingLoop_step_36_H200b --stepItem--> H200b
StrippingLoop_step_36_H200b --label--> Stripping loop step 36: H200b
StrippingLoop_step_36_H200b --stepIndex--> 36
StrippingLoop_step_36_H200b --type--> LoopStep
StrippingLoop_step_36_H200b --stepType--> inline
limit_TSHH212b --note--> Setpoint not on drawing.
limit_TSHH212b --unit--> C
limit_TSHH212b --type--> OperatingLimit
limit_TSHH212b --limitType--> trip
limit_TSHH212b --variable--> temperature
limit_TSHH212b --valueVerified--> true
limit_TSHH212b --source--> P&ID
limit_TSHH212b --label--> TSHH212b
TT212b --gridReference--> J10
TT212b --type--> TemperatureInstrument
TT212b --floor--> 2
TT212b --tag--> TT212b
TT212b --label--> TT212b
TT212b --sensorType--> K-type thermocouple
TT212b --measuredVariable--> heater temperature
TT212b --signalType--> 4-20mA
IL_H200b_HH --initiatedBy--> TT212b
H200b__cit01 --type--> Citation
H200b__cit01 --citationText--> P&ID heater control section (grids J9 to J11)
H200b__cit01 --label--> Citation 1 for H200b
H200b__cit01 --document--> SRC_PID
H200b__cit01 --location--> heater control section (grids J9 to J11)
Route_B_top_bypass_step_33_H200a --nextStep--> Route_B_top_bypass_step_36_V403
Route_B_top_bypass_step_33_H200a --label--> Route B: top return (stage 1), Z102 bypassed step 33: H200a
Route_B_top_bypass_step_33_H200a --stepItem--> H200a
Route_B_top_bypass_step_33_H200a --stepType--> inline
Route_B_top_bypass_step_33_H200a --type--> LoopStep
Route_B_top_bypass_step_33_H200a --stepIndex--> 33
Route_B_top_bypass_step_32_SDV125 --nextStep--> Route_B_top_bypass_step_33_H200a
SDV125 --floor--> 1
SDV125 --gridReference--> L11
SDV125 --type--> ShutdownValve
SDV125 --label--> SDV125
SDV125 --valveType--> shutdown (solenoid-operated)
SDV125 --tag--> SDV125
SDV125 --note--> Route from J100 discharge to H200a/b and E100 (stripping loop). Tagged SDV125 on the P&ID; the REPORT calls it SOV125.
SDV125 --normalPosition--> open
FT104 --feedsInto--> SDV125
FT104 --pipedTo--> SDV125
Route_C_side_filter_setting_SDV125 --valve--> SDV125
FigureOfEight_setting_SDV125 --valve--> SDV125
Route_A_top_filter_setting_SDV125 --valve--> SDV125
Route_D_side_bypass_setting_SDV125 --valve--> SDV125
PROC_figure_of_eight_lineup_step_03 --operatesOn--> SDV125
Route_B_top_bypass_setting_SDV125 --valve--> SDV125
OI09 --about--> SDV125
PROC_stripping_loop_lineup_step_22 --operatesOn--> SDV125
CL_H200a_temperature --type--> ControlLoop
CL_H200a_temperature --controlledVariable--> Temperature of MEA entering E100
CL_H200a_temperature --manipulatedVariable--> Thermal duty of H200a
CL_H200a_temperature --hasController--> TIC213a
CL_H200a_temperature --source--> SUMMARY p.190; REPORT D.4.4.a
```

Question: Which sensor and controllers determine the heating duties of H200a and H200b?

## Q51

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
aspen_v3_block_E101 --type--> AspenBlock
aspen_v3_block_E101 --aspenModel--> RADFRAC
aspen_v3_block_E101 --blockId--> E101
aspen_v3_block_E101 --status--> OK
aspen_v3_block_E101 --label--> E101 (ABB_pilot_plant_final_3)
aspen_v3_block_E101 --inCase--> case_aspen_v3
aspen_v3_stream_S8 --fromBlock--> aspen_v3_block_E101
aspen_v3_stream_1 --toBlock--> aspen_v3_block_E101
aspen_v3_stream_2 --toBlock--> aspen_v3_block_E101
aspen_v3_stream_4 --fromBlock--> aspen_v3_block_E101
aspen_v6_1_block_E101 --type--> AspenBlock
aspen_v6_1_block_E101 --aspenModel--> RADFRAC
aspen_v6_1_block_E101 --label--> E101 (ABB_pilot_plant_final_6_1_SA_validation)
aspen_v6_1_block_E101 --blockId--> E101
aspen_v6_1_block_E101 --status--> OK
aspen_v6_1_block_E101 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S8 --fromBlock--> aspen_v6_1_block_E101
aspen_v6_1_stream_2 --toBlock--> aspen_v6_1_block_E101
aspen_v6_1_stream_1 --toBlock--> aspen_v6_1_block_E101
aspen_v6_1_stream_4 --fromBlock--> aspen_v6_1_block_E101
E101 --pipedTo--> RV400
E101 --floor--> 1
E101 --note--> Lean MEA enters at the top through NRV400; rich MEA leaves from the sump to J101a/b. The air admittance valve shown on the P&ID has been removed from the plant (DIFF, E14/15).
E101 --feedsInto--> E101_N_sump_outlet
E101 --designBasis--> Packing and column designed for 2.3-2.5 bar operation on MEA and 50 kg/h CO2 (HAZOP 10.4)
E101 --feedsInto--> E101_N_gas_outlet
E101 --pipedTo--> E101_N_sump_outlet
E101 --pipedTo--> E101_N_gas_outlet
E101 --type--> AbsorptionColumn
E101 --diameter_mm--> 230.0
E101 --tag--> E101
E101 --label--> E101 absorber
HAZOP_7_10 --concerns--> E101
TT305 --monitors--> E101
PT111 --monitors--> E101
E101_sample_5 --onColumn--> E101
E101_N_gas_outlet --onEquipment--> E101
LSLL109 --monitors--> E101
TT207 --monitors--> E101
PT403 --monitors--> E101
LI108 --monitors--> E101
E101_sample_4 --onColumn--> E101
E101_N_sump_outlet --onEquipment--> E101
FT109 --monitors--> E101
E101_sample_3 --onColumn--> E101
HAZOP_9b_05 --concerns--> E101
limit_LZAL109 --appliesTo--> E101
DI108 --monitors--> E101
E101_N_gas_inlet --feedsInto--> E101
FT304 --monitors--> E101
LT108 --monitors--> E101
K101_N2_recycle --bypasses--> E101
PT110 --monitors--> E101
E101_N_gas_inlet --pipedTo--> E101
HAZOP_5_08 --concerns--> E101
HAZOP_8_01 --concerns--> E101
HAZOP_8_06 --concerns--> E101
PI403 --monitors--> E101
AT400 --monitors--> E101
FT303 --monitors--> E101
TT205 --monitors--> E101
E101_N_base_inlet --onEquipment--> E101
aspen_v6_1_E101_performance --ofEquipment--> E101
TT206 --monitors--> E101
HAZOP_8_03 --concerns--> E101
E101_N_gas_inlet --onEquipment--> E101
E101_N_top_inlet --feedsInto--> E101
E101_sample_6 --onColumn--> E101
K402 --pipedTo--> E101
HAZOP_5_07 --concerns--> E101
AI300 --monitors--> E101
FI109 --monitors--> E101
FI108 --monitors--> E101
aspen_v3_vent_gas --ofEquipment--> E101
AT300 --monitors--> E101
E101_N_top_inlet --pipedTo--> E101
aspen_v6_1_feed_gas --ofEquipment--> E101
limit_PSHH117_set --appliesTo--> E101
TT109 --monitors--> E101
TT412 --monitors--> E101
HAZOP_10_03 --concerns--> E101
LSHH107 --monitors--> E101
E101_sample_2 --onColumn--> E101
limit_LZAH107 --appliesTo--> E101
HAZOP_5_06 --concerns--> E101
PSHH117 --monitors--> E101
TT413 --monitors--> E101
HAZOP_7_13 --concerns--> E101
TT107 --monitors--> E101
TT306 --monitors--> E101
E101_N_top_inlet --onEquipment--> E101
E101_sample_1 --onColumn--> E101
AOI10 --about--> E101
RV400 --protects--> E101
FT108 --monitors--> E101
TT411 --monitors--> E101
TT204 --monitors--> E101
aspen_v3_feed_gas --ofEquipment--> E101
HAZOP_element_10 --covers--> E101
HAZOP_8_11 --concerns--> E101
TT307 --monitors--> E101
TT308 --monitors--> E101
HAZOP_8_02 --concerns--> E101
aspen_v3_E101_performance --ofEquipment--> E101
PCV300 --valveType--> pressure control
PCV300 --floor--> 3
PCV300 --normalPosition--> open
PCV300 --note--> Vents lean gas from the absorber to hold the E101 pressure (PIC403). Opened in the vent stream start-up (Fig F.3), closed at shutdown.
PCV300 --pipedTo--> VENT_E101
PCV300 --label--> PCV300
PCV300 --feedsInto--> VENT_E101
PCV300 --type--> PressureControlValve
PCV300 --tag--> PCV300
PCV300 --gridReference--> G18
K402 --feedsInto--> PCV300
CL_E101_pressure --hasFinalElement--> PCV300
K402 --pipedTo--> PCV300
PIC403 --controls--> PCV300
AV01 --about--> PCV300
K101 --type--> Saturator
K101 --label--> K101 gas saturator
K101 --pipedTo--> SDV170
K101 --pipedTo--> Z103
K101 --floor--> 1
K101 --feedsInto--> E101_N_gas_inlet
K101 --pipedTo--> E101_N_gas_inlet
K101 --note--> Saturates the feed gas with water before E101; temperature held by TIC121 using C106 on the recirculating water. Grid not in the REPORT lists (near L17 to L18 on the P&ID). Not modelled in Aspen (GOI09).
K101 --pipedTo--> V126
K101 --tag--> K101
DI_CARTRIDGE --feedsInto--> K101
HAZOP_4_06 --concerns--> K101
V172 --pipedTo--> K101
J102 --pipedTo--> K101
limit_LZAL_K101 --appliesTo--> K101
HAZOP_4_07 --concerns--> K101
LT104 --monitors--> K101
HAZOP_3_05 --concerns--> K101
FEED_GAS_HEADER --feedsInto--> K101
GOI09 --about--> K101
LI106 --monitors--> K101
FEED_GAS_HEADER --pipedTo--> K101
limit_LAL_K101 --appliesTo--> K101
K101_N2_recycle --fromItem--> K101
limit_LZAH_K101 --appliesTo--> K101
GOI07 --about--> K101
GOI02 --about--> K101
HAZOP_element_3 --covers--> K101
HAZOP_4_02 --concerns--> K101
TI121 --monitors--> K101
C106 --pipedTo--> K101
```

Question: If the CO2 concentration in gas leaving the top of E101 increases unexpectedly, what plant changes could explain it?

## Q52

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
aspen_v6_1_block_C100 --represents--> C100
aspen_v6_1_block_C100 --statusMessage--> TEMPERATURE CROSSOVER DETECTED
aspen_v6_1_block_C100 --inCase--> case_aspen_v6_1
aspen_v6_1_block_C100 --status--> WARNING
aspen_v6_1_block_C100 --aspenModel--> HEATX
aspen_v6_1_block_C100 --type--> AspenBlock
aspen_v6_1_block_C100 --label--> C100 (ABB_pilot_plant_final_6_1_SA_validation)
aspen_v6_1_block_C100 --blockId--> C100
aspen_v6_1_stream_S2 --fromBlock--> aspen_v6_1_block_C100
aspen_v6_1_stream_S3BACKUP --toBlock--> aspen_v6_1_block_C100
aspen_v6_1_stream_S8 --toBlock--> aspen_v6_1_block_C100
aspen_v6_1_stream_S27 --fromBlock--> aspen_v6_1_block_C100
C100 --source--> SUMMARY p.106; REPORT section 3
C100 --note--> Hot side carries lean MEA from E100. In the stripping loop the rich (cold) side has no flow from the absorber. REPORT puts C100 efficiency at about 95 %.
C100 --floor--> 1
C100 --pipedTo--> SDV152
C100 --tag--> C100
C100 --type--> LeanRichExchanger
C100 --pipedTo--> V113a
C100 --feedsInto--> V113a
C100 --label--> C100 lean/rich interchanger (gasketed plate heat exchanger)
HAZOP_8_02 --concerns--> C100
HAZOP_7_11 --concerns--> C100
TT104 --monitors--> C100
V112 --pipedTo--> C100
HAZOP_element_8 --covers--> C100
V112 --feedsInto--> C100
PT103 --monitors--> C100
V151 --pipedTo--> C100
aspen_v3_block_C100 --represents--> C100
aspen_v6_1_C100_performance --ofEquipment--> C100
HAZOP_8_09 --concerns--> C100
TE105 --monitors--> C100
HAZOP_element_7 --covers--> C100
TT113 --monitors--> C100
aspen_v3_C100_performance --ofEquipment--> C100
TT112 --monitors--> C100
aspen_v3_block_C100 --status--> OK
aspen_v3_block_C100 --inCase--> case_aspen_v3
aspen_v3_block_C100 --type--> AspenBlock
aspen_v3_block_C100 --label--> C100 (ABB_pilot_plant_final_3)
aspen_v3_block_C100 --aspenModel--> HEATX
aspen_v3_block_C100 --blockId--> C100
aspen_v3_stream_S15 --fromBlock--> aspen_v3_block_C100
aspen_v3_stream_S3 --toBlock--> aspen_v3_block_C100
aspen_v3_stream_S8 --toBlock--> aspen_v3_block_C100
aspen_v3_stream_S2 --fromBlock--> aspen_v3_block_C100
V151 --type--> ManualValve
V151 --normalPosition--> open
V151 --gridReference--> M9
V151 --floor--> 1
V151 --tag--> V151
V151 --label--> V151
V151 --note--> On the rich line from FT108 to the C100 cold side. Other REPORT tables give grid N9 or N8.
HAZOP_element_8 --covers--> V151
FigureOfEight_setting_V151 --valve--> V151
FT108 --pipedTo--> V151
PROC_figure_of_eight_lineup_step_01 --operatesOn--> V151
HAZOP_8_02 --concerns--> LSLL109
HAZOP_8_02 --consequence--> E101 empties into E101
HAZOP_8_02 --label--> HAZOP 8.2
HAZOP_8_02 --safeguard--> See action re flow across C100.  Plant shutdown on LZAL 109
HAZOP_8_02 --guideword--> MORE
HAZOP_8_02 --itemNumber--> 2
HAZOP_8_02 --type--> HazopDeviation
HAZOP_8_02 --cause--> Faulty pump control
HAZOP_8_02 --inElement--> HAZOP_element_8
HAZOP_8_02 --parameter--> FLOW
HAZOP_8_02 --concerns--> E101
case_aspen_v6_1 --converged--> false
case_aspen_v6_1 --representsMode--> FigureOfEight
case_aspen_v6_1 --savedOn--> Thu Feb 27 15:14:32 2025
case_aspen_v6_1 --recommendedForUse--> false
case_aspen_v6_1 --aspenFile--> ABB_pilot_plant_final_6_1_SA_validation.apwz
case_aspen_v6_1 --label--> ABB_pilot_plant_final_6_1_SA_validation
case_aspen_v6_1 --aspenVersion--> 37.0
case_aspen_v6_1 --note--> Rescaled to pilot conditions with a sensitivity study for validation. Saved results did not converge: E100 RateSep failed, H100 invalid input, C100 temperature crossover, recycle opened at S3BACKUP.
case_aspen_v6_1 --type--> SimulationCase
aspen_v6_1_block_E100 --inCase--> case_aspen_v6_1
aspen_v6_1_block_C400COND --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S21 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_PURGE --inCase--> case_aspen_v6_1
aspen_v6_1_E100_stage_02 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S4 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S17 --inCase--> case_aspen_v6_1
aspen_v6_1_block_H200A --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S8 --inCase--> case_aspen_v6_1
aspen_v6_1_E100_stage_08 --inCase--> case_aspen_v6_1
aspen_v6_1_block_MIXER1 --inCase--> case_aspen_v6_1
aspen_v6_1_E100_stage_06 --inCase--> case_aspen_v6_1
aspen_v6_1_E100_stage_11 --inCase--> case_aspen_v6_1
aspen_v6_1_E100_performance --inCase--> case_aspen_v6_1
aspen_v6_1_block_C400 --inCase--> case_aspen_v6_1
aspen_v6_1_H100_performance --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S1 --inCase--> case_aspen_v6_1
aspen_v6_1_block_B2 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S16 --inCase--> case_aspen_v6_1
aspen_v6_1_H200a_performance --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S27 --inCase--> case_aspen_v6_1
aspen_v6_1_H200b_performance --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S13 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S12 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S2 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S10 --inCase--> case_aspen_v6_1
aspen_v6_1_block_C200 --inCase--> case_aspen_v6_1
aspen_v6_1_E100_stage_04 --inCase--> case_aspen_v6_1
aspen_v6_1_block_SPLITER1 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_1 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S25 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_2 --inCase--> case_aspen_v6_1
aspen_v6_1_block_E101 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S15 --inCase--> case_aspen_v6_1
aspen_v6_1_C200_performance --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S11 --inCase--> case_aspen_v6_1
aspen_v6_1_block_B1 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S26 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S5 --inCase--> case_aspen_v6_1
aspen_v6_1_E101_performance --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S23 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S31 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S14 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S28 --inCase--> case_aspen_v6_1
aspen_v6_1_E100_stage_05 --inCase--> case_aspen_v6_1
aspen_v6_1_E100_stage_09 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S7 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S3BACKUP --inCase--> case_aspen_v6_1
aspen_v6_1_C100_performance --inCase--> case_aspen_v6_1
aspen_v6_1_block_MIXER2 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_4 --inCase--> case_aspen_v6_1
aspen_v6_1_E100_stage_03 --inCase--> case_aspen_v6_1
aspen_v6_1_block_H100 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S9 --inCase--> case_aspen_v6_1
aspen_v6_1_E100_stage_07 --inCase--> case_aspen_v6_1
aspen_v6_1_E100_stage_10 --inCase--> case_aspen_v6_1
aspen_v6_1_feed_gas --inCase--> case_aspen_v6_1
aspen_v6_1_E100_stage_01 --inCase--> case_aspen_v6_1
aspen_v6_1_E100_stage_12 --inCase--> case_aspen_v6_1
aspen_v6_1_block_H200B --inCase--> case_aspen_v6_1
Route_C_side_filter_step_16_C100 --label--> Route C: side return (stage 3), through Z102 step 16: C100
Route_C_side_filter_step_16_C100 --nextStep--> Route_C_side_filter_step_18_V113a
Route_C_side_filter_step_16_C100 --stepIndex--> 16
Route_C_side_filter_step_16_C100 --stepType--> inline
Route_C_side_filter_step_16_C100 --stepItem--> C100
Route_C_side_filter_step_16_C100 --type--> LoopStep
Route_C_side_filter_step_13_V112 --nextStep--> Route_C_side_filter_step_16_C100
C100__cit01 --location--> interchanger C100, grid M8 to M9
C100__cit01 --type--> Citation
C100__cit01 --label--> Citation 1 for C100
C100__cit01 --document--> SRC_PID
C100__cit01 --citationText--> P&ID interchanger C100, grid M8 to M9
```

Question: If lean MEA leaving C100 is unusually hot, what could be wrong with the rich MEA side of the exchanger?

## Q53

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
aspen_v3_block_E101 --type--> AspenBlock
aspen_v3_block_E101 --aspenModel--> RADFRAC
aspen_v3_block_E101 --blockId--> E101
aspen_v3_block_E101 --status--> OK
aspen_v3_block_E101 --label--> E101 (ABB_pilot_plant_final_3)
aspen_v3_block_E101 --inCase--> case_aspen_v3
aspen_v3_stream_S8 --fromBlock--> aspen_v3_block_E101
aspen_v3_stream_1 --toBlock--> aspen_v3_block_E101
aspen_v3_stream_2 --toBlock--> aspen_v3_block_E101
aspen_v3_stream_4 --fromBlock--> aspen_v3_block_E101
aspen_v6_1_block_E101 --type--> AspenBlock
aspen_v6_1_block_E101 --aspenModel--> RADFRAC
aspen_v6_1_block_E101 --label--> E101 (ABB_pilot_plant_final_6_1_SA_validation)
aspen_v6_1_block_E101 --blockId--> E101
aspen_v6_1_block_E101 --status--> OK
aspen_v6_1_block_E101 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S8 --fromBlock--> aspen_v6_1_block_E101
aspen_v6_1_stream_2 --toBlock--> aspen_v6_1_block_E101
aspen_v6_1_stream_1 --toBlock--> aspen_v6_1_block_E101
aspen_v6_1_stream_4 --fromBlock--> aspen_v6_1_block_E101
TT210 --type--> TemperatureInstrument
TT210 --signalType--> Fieldbus
TT210 --label--> TT210
TT210 --floor--> 2
TT210 --tag--> TT210
TT210 --gridReference--> J14
TT210 --sensorType--> PRT
TT210 --monitors--> C200
TT210 --measuredVariable--> lean MEA leaving C200 (entering E101)
CL_C200_temperature --hasSensor--> TT210
AOI15 --about--> TT210
limit_TAH_C200_outlet --appliesTo--> TT210
E101 --pipedTo--> RV400
E101 --floor--> 1
E101 --note--> Lean MEA enters at the top through NRV400; rich MEA leaves from the sump to J101a/b. The air admittance valve shown on the P&ID has been removed from the plant (DIFF, E14/15).
E101 --feedsInto--> E101_N_sump_outlet
E101 --designBasis--> Packing and column designed for 2.3-2.5 bar operation on MEA and 50 kg/h CO2 (HAZOP 10.4)
E101 --feedsInto--> E101_N_gas_outlet
E101 --pipedTo--> E101_N_sump_outlet
E101 --pipedTo--> E101_N_gas_outlet
E101 --type--> AbsorptionColumn
E101 --diameter_mm--> 230.0
E101 --tag--> E101
E101 --label--> E101 absorber
HAZOP_7_10 --concerns--> E101
TT305 --monitors--> E101
PT111 --monitors--> E101
E101_sample_5 --onColumn--> E101
E101_N_gas_outlet --onEquipment--> E101
LSLL109 --monitors--> E101
TT207 --monitors--> E101
PT403 --monitors--> E101
LI108 --monitors--> E101
E101_sample_4 --onColumn--> E101
E101_N_sump_outlet --onEquipment--> E101
FT109 --monitors--> E101
E101_sample_3 --onColumn--> E101
HAZOP_9b_05 --concerns--> E101
limit_LZAL109 --appliesTo--> E101
DI108 --monitors--> E101
E101_N_gas_inlet --feedsInto--> E101
FT304 --monitors--> E101
LT108 --monitors--> E101
K101_N2_recycle --bypasses--> E101
PT110 --monitors--> E101
E101_N_gas_inlet --pipedTo--> E101
HAZOP_5_08 --concerns--> E101
HAZOP_8_01 --concerns--> E101
HAZOP_8_06 --concerns--> E101
PI403 --monitors--> E101
AT400 --monitors--> E101
FT303 --monitors--> E101
TT205 --monitors--> E101
E101_N_base_inlet --onEquipment--> E101
aspen_v6_1_E101_performance --ofEquipment--> E101
TT206 --monitors--> E101
HAZOP_8_03 --concerns--> E101
E101_N_gas_inlet --onEquipment--> E101
E101_N_top_inlet --feedsInto--> E101
E101_sample_6 --onColumn--> E101
K402 --pipedTo--> E101
HAZOP_5_07 --concerns--> E101
AI300 --monitors--> E101
FI109 --monitors--> E101
FI108 --monitors--> E101
aspen_v3_vent_gas --ofEquipment--> E101
AT300 --monitors--> E101
E101_N_top_inlet --pipedTo--> E101
aspen_v6_1_feed_gas --ofEquipment--> E101
limit_PSHH117_set --appliesTo--> E101
TT109 --monitors--> E101
TT412 --monitors--> E101
HAZOP_10_03 --concerns--> E101
LSHH107 --monitors--> E101
E101_sample_2 --onColumn--> E101
limit_LZAH107 --appliesTo--> E101
HAZOP_5_06 --concerns--> E101
PSHH117 --monitors--> E101
TT413 --monitors--> E101
HAZOP_7_13 --concerns--> E101
TT107 --monitors--> E101
TT306 --monitors--> E101
E101_N_top_inlet --onEquipment--> E101
E101_sample_1 --onColumn--> E101
AOI10 --about--> E101
RV400 --protects--> E101
FT108 --monitors--> E101
TT411 --monitors--> E101
TT204 --monitors--> E101
aspen_v3_feed_gas --ofEquipment--> E101
HAZOP_element_10 --covers--> E101
HAZOP_8_11 --concerns--> E101
TT307 --monitors--> E101
TT308 --monitors--> E101
HAZOP_8_02 --concerns--> E101
aspen_v3_E101_performance --ofEquipment--> E101
PCV300 --valveType--> pressure control
PCV300 --floor--> 3
PCV300 --normalPosition--> open
PCV300 --note--> Vents lean gas from the absorber to hold the E101 pressure (PIC403). Opened in the vent stream start-up (Fig F.3), closed at shutdown.
PCV300 --pipedTo--> VENT_E101
PCV300 --label--> PCV300
PCV300 --feedsInto--> VENT_E101
PCV300 --type--> PressureControlValve
PCV300 --tag--> PCV300
PCV300 --gridReference--> G18
K402 --feedsInto--> PCV300
CL_E101_pressure --hasFinalElement--> PCV300
K402 --pipedTo--> PCV300
PIC403 --controls--> PCV300
AV01 --about--> PCV300
K101 --type--> Saturator
K101 --label--> K101 gas saturator
K101 --pipedTo--> SDV170
K101 --pipedTo--> Z103
K101 --floor--> 1
K101 --feedsInto--> E101_N_gas_inlet
K101 --pipedTo--> E101_N_gas_inlet
K101 --note--> Saturates the feed gas with water before E101; temperature held by TIC121 using C106 on the recirculating water. Grid not in the REPORT lists (near L17 to L18 on the P&ID). Not modelled in Aspen (GOI09).
K101 --pipedTo--> V126
K101 --tag--> K101
DI_CARTRIDGE --feedsInto--> K101
HAZOP_4_06 --concerns--> K101
V172 --pipedTo--> K101
J102 --pipedTo--> K101
limit_LZAL_K101 --appliesTo--> K101
HAZOP_4_07 --concerns--> K101
LT104 --monitors--> K101
HAZOP_3_05 --concerns--> K101
FEED_GAS_HEADER --feedsInto--> K101
```

Question: TT210 shows the MEA entering E101 is too hot. What could cause this, and how would it affect absorption?

## Q54

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
TT213 --sensorType--> PRT
TT213 --type--> TemperatureInstrument
TT213 --measuredVariable--> temperature of MEA leaving H200a/b
TT213 --label--> TT213
TT213 --gridReference--> H13
TT213 --signalType--> Profibus-PA
TT213 --tag--> TT213
TT213 --floor--> 2
PROC_stripping_loop_lineup_step_27 --operatesOn--> TT213
IL_heater_outlet_H --initiatedBy--> TT213
PROC_heater_overtemperature_step_01 --operatesOn--> TT213
limit_TT213_setpoint_commissioning --appliesTo--> TT213
PROC_heater_overtemperature_step_05 --operatesOn--> TT213
CL_H200a_temperature --hasSensor--> TT213
CL_H200b_temperature --hasSensor--> TT213
TT213__cit02 --type--> Citation
TT213__cit02 --label--> Citation 2 for TT213
TT213__cit02 --document--> SRC_REPORT
TT213__cit02 --location--> Appendix B instrument list
TT213__cit02 --citationText--> Pilot Plant Report Appendix B instrument list
FigureOfEight_step_14_TT213 --stepItem--> TT213
FigureOfEight_step_14_TT213 --stepType--> tie-in
FigureOfEight_step_14_TT213 --type--> LoopStep
FigureOfEight_step_14_TT213 --stepIndex--> 14
FigureOfEight_step_14_TT213 --label--> Figure-of-eight circulation (normal running) step 14: TT213
PROC_heater_overtemperature_step_06 --type--> ProcedureStep
PROC_heater_overtemperature_step_06 --instruction--> If both TT213 and TI213 read above 25 C, send a mechanical engineer to check H200a and H200b
PROC_heater_overtemperature_step_06 --operatesOn--> H200a
PROC_heater_overtemperature_step_06 --stepOrder--> 6
PROC_heater_overtemperature_step_06 --label--> MEA entering E100 too hot (heater over-temperature) step 6
PROC_heater_overtemperature --hasProcedureStep--> PROC_heater_overtemperature_step_06
Route_D_side_bypass_step_34_TT213 --label--> Route D: side return (stage 3), Z102 bypassed step 34: TT213
Route_D_side_bypass_step_34_TT213 --stepIndex--> 34
Route_D_side_bypass_step_34_TT213 --stepType--> tie-in
Route_D_side_bypass_step_34_TT213 --type--> LoopStep
Route_D_side_bypass_step_34_TT213 --stepItem--> TT213
CL_H200a_temperature --hasFinalElement--> H200a
CL_H200a_temperature --type--> ControlLoop
CL_H200a_temperature --controlledVariable--> Temperature of MEA entering E100
CL_H200a_temperature --manipulatedVariable--> Thermal duty of H200a
CL_H200a_temperature --hasController--> TIC213a
CL_H200a_temperature --source--> SUMMARY p.190; REPORT D.4.4.a
CL_H200a_temperature --label--> Temperature of MEA entering E100, heater leg A
CL_H200a_temperature --hasController--> TY213a
PROC_heater_overtemperature_step_05 --type--> ProcedureStep
PROC_heater_overtemperature_step_05 --instruction--> If TI213 does not match TT213, follow emergency procedure E.3.12
PROC_heater_overtemperature_step_05 --stepOrder--> 5
PROC_heater_overtemperature_step_05 --label--> MEA entering E100 too hot (heater over-temperature) step 5
PROC_heater_overtemperature --hasProcedureStep--> PROC_heater_overtemperature_step_05
TT213__cit01 --label--> Citation 1 for TT213
TT213__cit01 --type--> Citation
TT213__cit01 --document--> SRC_PID
TT213__cit01 --location--> grid H13
TT213__cit01 --citationText--> P&ID grid H13
StrippingLoop_step_37_TT213 --stepItem--> TT213
StrippingLoop_step_37_TT213 --stepType--> tie-in
StrippingLoop_step_37_TT213 --type--> LoopStep
StrippingLoop_step_37_TT213 --label--> Stripping loop step 37: TT213
StrippingLoop_step_37_TT213 --stepIndex--> 37
Route_A_top_filter_step_37_TT213 --stepType--> tie-in
Route_A_top_filter_step_37_TT213 --stepIndex--> 37
Route_A_top_filter_step_37_TT213 --stepItem--> TT213
Route_A_top_filter_step_37_TT213 --type--> LoopStep
Route_A_top_filter_step_37_TT213 --label--> Route A: top return (stage 1), through Z102 step 37: TT213
PROC_heater_overtemperature_step_04 --label--> MEA entering E100 too hot (heater over-temperature) step 4
PROC_heater_overtemperature_step_04 --operatesOn--> TI213
PROC_heater_overtemperature_step_04 --stepOrder--> 4
PROC_heater_overtemperature_step_04 --instruction--> If TT213 still reads above 25 C, send an operator to check TI213
PROC_heater_overtemperature_step_04 --type--> ProcedureStep
PROC_heater_overtemperature --hasProcedureStep--> PROC_heater_overtemperature_step_04
CL_H200b_temperature --label--> Temperature of MEA entering E100, heater leg B
CL_H200b_temperature --manipulatedVariable--> Thermal duty of H200b
CL_H200b_temperature --hasController--> TIC213b
CL_H200b_temperature --controlledVariable--> Temperature of MEA entering E100
CL_H200b_temperature --type--> ControlLoop
CL_H200b_temperature --source--> SUMMARY p.190; REPORT D.4.4.a
CL_H200b_temperature --hasController--> TY213b
CL_H200b_temperature --hasFinalElement--> H200b
limit_TT213_setpoint_commissioning --type--> OperatingLimit
limit_TT213_setpoint_commissioning --source--> REPORT E.2.1.9
limit_TT213_setpoint_commissioning --limitType--> setpoint
limit_TT213_setpoint_commissioning --note--> Heaters effectively off during the commissioning test.
limit_TT213_setpoint_commissioning --unit--> C
limit_TT213_setpoint_commissioning --label--> TT213_setpoint_commissioning
limit_TT213_setpoint_commissioning --variable--> temperature
limit_TT213_setpoint_commissioning --valueVerified--> true
limit_TT213_setpoint_commissioning --highValue--> 25.0
PROC_stripping_loop_lineup_step_27 --stepOrder--> 27
PROC_stripping_loop_lineup_step_27 --type--> ProcedureStep
PROC_stripping_loop_lineup_step_27 --instruction--> Set heater outlet temperature set point to 25 C (read on TT213)
PROC_stripping_loop_lineup_step_27 --label--> Stripping loop line-up (commissioning test start-up) step 27
PROC_stripping_loop_lineup --hasProcedureStep--> PROC_stripping_loop_lineup_step_27
PROC_heater_overtemperature_step_01 --instruction--> Check the heater set point in the control room is 25 C; if not, set it to 25 C
PROC_heater_overtemperature_step_01 --label--> MEA entering E100 too hot (heater over-temperature) step 1
PROC_heater_overtemperature_step_01 --type--> ProcedureStep
PROC_heater_overtemperature_step_01 --stepOrder--> 1
PROC_heater_overtemperature --hasProcedureStep--> PROC_heater_overtemperature_step_01
PROC_heater_overtemperature --type--> Procedure
PROC_heater_overtemperature --source--> REPORT E.3.4
PROC_heater_overtemperature --label--> MEA entering E100 too hot (heater over-temperature)
PROC_heater_overtemperature --hasProcedureStep--> PROC_heater_overtemperature_step_02
PROC_heater_overtemperature --hasProcedureStep--> PROC_heater_overtemperature_step_03
PROC_heater_overtemperature --triggerCondition--> TT213 reads above the expected room temperature during the stripping loop test (set point 25 C)
IL_heater_outlet_H --type--> Interlock
IL_heater_outlet_H --label--> Heater outlet high temperature (TZH213)
IL_heater_outlet_H --tripsItem--> H200b
IL_heater_outlet_H --tripsItem--> H200a
Route_C_side_filter_step_37_TT213 --stepIndex--> 37
Route_C_side_filter_step_37_TT213 --type--> LoopStep
Route_C_side_filter_step_37_TT213 --label--> Route C: side return (stage 3), through Z102 step 37: TT213
Route_C_side_filter_step_37_TT213 --stepItem--> TT213
Route_C_side_filter_step_37_TT213 --stepType--> tie-in
Route_B_top_bypass_step_34_TT213 --stepIndex--> 34
Route_B_top_bypass_step_34_TT213 --stepItem--> TT213
Route_B_top_bypass_step_34_TT213 --stepType--> tie-in
Route_B_top_bypass_step_34_TT213 --type--> LoopStep
Route_B_top_bypass_step_34_TT213 --label--> Route B: top return (stage 1), Z102 bypassed step 34: TT213
```

Question: If TT213 is below the required rich MEA feed temperature, what might be happening in the pre-heater system?

## Q55

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
aspen_v3_block_E100 --label--> E100 (ABB_pilot_plant_final_3)
aspen_v3_block_E100 --represents--> E100
aspen_v3_block_E100 --aspenModel--> RADFRAC
aspen_v3_block_E100 --inCase--> case_aspen_v3
aspen_v3_block_E100 --status--> WARNING
aspen_v3_block_E100 --statusMessage--> FEED PRESSURE IS LOWER THAN STAGE PRESSURE.
aspen_v3_block_E100 --type--> AspenBlock
aspen_v3_block_E100 --blockId--> E100
aspen_v3_stream_S13 --fromBlock--> aspen_v3_block_E100
aspen_v3_stream_S10 --toBlock--> aspen_v3_block_E100
aspen_v3_stream_S6 --fromBlock--> aspen_v3_block_E100
aspen_v3_stream_S14 --fromBlock--> aspen_v3_block_E100
aspen_v3_stream_S24 --toBlock--> aspen_v3_block_E100
aspen_v6_1_block_E100 --inCase--> case_aspen_v6_1
aspen_v6_1_block_E100 --statusMessage--> RATESEP CALCULATIONS FAILED TO CONVERGE.
aspen_v6_1_block_E100 --status--> ERROR
aspen_v6_1_block_E100 --represents--> E100
aspen_v6_1_block_E100 --label--> E100 (ABB_pilot_plant_final_6_1_SA_validation)
aspen_v6_1_block_E100 --type--> AspenBlock
aspen_v6_1_block_E100 --blockId--> E100
aspen_v6_1_block_E100 --aspenModel--> RADFRAC
aspen_v6_1_stream_S15 --fromBlock--> aspen_v6_1_block_E100
aspen_v6_1_stream_S23 --fromBlock--> aspen_v6_1_block_E100
aspen_v6_1_stream_S10 --toBlock--> aspen_v6_1_block_E100
aspen_v6_1_stream_S12 --fromBlock--> aspen_v6_1_block_E100
aspen_v6_1_stream_S14 --toBlock--> aspen_v6_1_block_E100
E100 --floor--> 1
E100 --hasStage--> E100_stage_12
E100 --diameter_mm--> 264.62
E100 --tag--> E100
E100 --label--> E100 stripper (desorber)
E100 --hasStage--> E100_stage_08
E100 --hasStage--> E100_stage_01
E100 --hasStage--> E100_stage_04
E100 --feedsInto--> E100_N_overhead
E100 --hasStage--> E100_stage_07
E100 --pipedTo--> E100_N_overhead
E100 --note--> Chimney tray below the bottom packed bed separates the draw-off section (stage 11) from the sump (stage 12).
E100 --hasStage--> E100_stage_02
E100 --hasStage--> E100_stage_09
E100 --feedsInto--> E100_N_sump_outlet
E100 --hasStage--> E100_stage_06
E100 --feedsInto--> E100_N_drawoff
E100 --pipedTo--> E100_N_sump_outlet
E100 --hasStage--> E100_stage_05
E100 --hasStage--> E100_stage_11
E100 --hasStage--> E100_stage_10
E100 --designBasis--> Designed for sub-atmospheric pressure (vacuum), per HAZOP element 11 item 10. Design pressure value not documented.
E100 --hasStage--> E100_stage_03
E100 --pipedTo--> E100_N_drawoff
E100 --type--> StrippingColumn
TT200 --monitors--> E100
PI401 --monitors--> E100
TT401 --monitors--> E100
PROC_reboiler_heating_step_06 --operatesOn--> E100
HAZOP_13_13 --concerns--> E100
HAZOP_11_13 --concerns--> E100
LT101 --monitors--> E100
E100_N_sump_outlet --onEquipment--> E100
LSLL102 --monitors--> E100
HAZOP_11_12 --concerns--> E100
OI06 --about--> E100
LSHH100 --monitors--> E100
aspen_v6_1_E100_performance --ofEquipment--> E100
E100_N_overhead --onEquipment--> E100
TT302 --monitors--> E100
HAZOP_7_10 --concerns--> E100
HAZOP_6_07 --concerns--> E100
HAZOP_11_15 --concerns--> E100
E100_N_top_inlet --feedsInto--> E100
PT402 --monitors--> E100
PT401 --monitors--> E100
E100_N_drawoff --onEquipment--> E100
E100_N_side_inlet --onEquipment--> E100
limit_LT101_operating_window --appliesTo--> E100
limit_LZAH100 --appliesTo--> E100
HAZOP_9b_05 --concerns--> E100
RV401 --protects--> E100
E100_N_top_inlet --pipedTo--> E100
E100_N_top_inlet --onEquipment--> E100
HAZOP_13_12 --concerns--> E100
aspen_v3_E100_performance --ofEquipment--> E100
TT301 --monitors--> E100
TT400 --monitors--> E100
HAZOP_7_15 --concerns--> E100
HAZOP_element_11 --covers--> E100
limit_LT101_low_alarm --appliesTo--> E100
TT303 --monitors--> E100
OI11 --about--> E100
limit_PSHH116_set --appliesTo--> E100
HAZOP_13_11 --concerns--> E100
E100_N_reboiler_return --feedsInto--> E100
limit_PSHH400_set --appliesTo--> E100
OI03 --about--> E100
TT103 --monitors--> E100
PSHH400 --monitors--> E100
E100_N_reboiler_return --pipedTo--> E100
HAZOP_8_01 --concerns--> E100
PT102 --monitors--> E100
PSHH116 --monitors--> E100
TT203 --monitors--> E100
limit_LZAL102 --appliesTo--> E100
TT201 --monitors--> E100
HAZOP_6_08 --concerns--> E100
TT300 --monitors--> E100
HAZOP_11_01 --concerns--> E100
E100_N_reboiler_return --onEquipment--> E100
TT202 --monitors--> E100
LSHH100 --tag--> LSHH100
LSHH100 --note--> Stage mapping inferred: odd Aspen stages are the gaps between packed beds where the side instruments sit; floors match REPORT.
LSHH100 --locatedAtStage--> E100_stage_12
LSHH100 --type--> LevelInstrument
LSHH100 --measuredVariable--> level high-high switch
LSHH100 --floor--> 1
LSHH100 --label--> LSHH100
IL_E100_level_HH --initiatedBy--> LSHH100
PT402 --tag--> PT402
PT402 --monitors--> K401
PT402 --measuredVariable--> pressure after K401
PT402 --gridReference--> C16
PT402 --type--> PressureInstrument
PT402 --signalType--> Fieldbus
PT402 --floor--> 4
PT402 --sensorType--> gauge pressure transmitter
PT402 --label--> PT402
HAZOP_12_02 --concerns--> PT402
HAZOP_element_12 --covers--> PT402
CL_E100_pressure --hasSensor--> PT402
NRV106 --tag--> NRV106
NRV106 --valveType--> check
NRV106 --floor--> 1
NRV106 --note--> Near V112 at the E100 sump outlet. FI07
NRV106 --type--> CheckValve
NRV106 --label--> NRV106
NRV106 --gridReference--> M8
Route_D_side_bypass_step_38_E100 --stepIndex--> 38
Route_D_side_bypass_step_38_E100 --label--> Route D: side return (stage 3), Z102 bypassed step 38: E100
Route_D_side_bypass_step_38_E100 --stepType--> inline
Route_D_side_bypass_step_38_E100 --stepItem--> E100
Route_D_side_bypass_step_38_E100 --type--> LoopStep
Route_D_side_bypass_step_37_E100_N_side_inlet --nextStep--> Route_D_side_bypass_step_38_E100
Route_B_top_bypass_step_10_E100 --nextStep--> Route_B_top_bypass_step_11_E100_N_sump_outlet
Route_B_top_bypass_step_10_E100 --stepItem--> E100
Route_B_top_bypass_step_10_E100 --stepIndex--> 10
Route_B_top_bypass_step_10_E100 --stepType--> inline
Route_B_top_bypass_step_10_E100 --type--> LoopStep
Route_B_top_bypass_step_10_E100 --label--> Route B: top return (stage 1), Z102 bypassed step 10: E100
Route_B_top_bypass_step_09_E100_N_reboiler_return --nextStep--> Route_B_top_bypass_step_10_E100
aspen_v3_stream_S10 --temperature_C--> 89.99877
aspen_v3_stream_S10 --phase--> MIXED
```

Question: The temperature and pressure in E100 are both rising. What heating-system faults could explain this?

## Q56

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
aspen_v6_1_block_E100 --inCase--> case_aspen_v6_1
aspen_v6_1_block_E100 --statusMessage--> RATESEP CALCULATIONS FAILED TO CONVERGE.
aspen_v6_1_block_E100 --status--> ERROR
aspen_v6_1_block_E100 --represents--> E100
aspen_v6_1_block_E100 --label--> E100 (ABB_pilot_plant_final_6_1_SA_validation)
aspen_v6_1_block_E100 --type--> AspenBlock
aspen_v6_1_block_E100 --blockId--> E100
aspen_v6_1_block_E100 --aspenModel--> RADFRAC
aspen_v6_1_stream_S15 --fromBlock--> aspen_v6_1_block_E100
aspen_v6_1_stream_S23 --fromBlock--> aspen_v6_1_block_E100
aspen_v6_1_stream_S10 --toBlock--> aspen_v6_1_block_E100
aspen_v6_1_stream_S12 --fromBlock--> aspen_v6_1_block_E100
aspen_v6_1_stream_S14 --toBlock--> aspen_v6_1_block_E100
aspen_v3_block_E100 --label--> E100 (ABB_pilot_plant_final_3)
aspen_v3_block_E100 --represents--> E100
aspen_v3_block_E100 --aspenModel--> RADFRAC
aspen_v3_block_E100 --inCase--> case_aspen_v3
aspen_v3_block_E100 --status--> WARNING
aspen_v3_block_E100 --statusMessage--> FEED PRESSURE IS LOWER THAN STAGE PRESSURE.
aspen_v3_block_E100 --type--> AspenBlock
aspen_v3_block_E100 --blockId--> E100
aspen_v3_stream_S13 --fromBlock--> aspen_v3_block_E100
aspen_v3_stream_S10 --toBlock--> aspen_v3_block_E100
aspen_v3_stream_S6 --fromBlock--> aspen_v3_block_E100
aspen_v3_stream_S14 --fromBlock--> aspen_v3_block_E100
aspen_v3_stream_S24 --toBlock--> aspen_v3_block_E100
E100 --floor--> 1
E100 --hasStage--> E100_stage_12
E100 --diameter_mm--> 264.62
E100 --tag--> E100
E100 --label--> E100 stripper (desorber)
E100 --hasStage--> E100_stage_08
E100 --hasStage--> E100_stage_01
E100 --hasStage--> E100_stage_04
E100 --feedsInto--> E100_N_overhead
E100 --hasStage--> E100_stage_07
E100 --pipedTo--> E100_N_overhead
E100 --note--> Chimney tray below the bottom packed bed separates the draw-off section (stage 11) from the sump (stage 12).
E100 --hasStage--> E100_stage_02
E100 --hasStage--> E100_stage_09
E100 --feedsInto--> E100_N_sump_outlet
E100 --hasStage--> E100_stage_06
E100 --feedsInto--> E100_N_drawoff
E100 --pipedTo--> E100_N_sump_outlet
E100 --hasStage--> E100_stage_05
E100 --hasStage--> E100_stage_11
E100 --hasStage--> E100_stage_10
E100 --designBasis--> Designed for sub-atmospheric pressure (vacuum), per HAZOP element 11 item 10. Design pressure value not documented.
E100 --hasStage--> E100_stage_03
E100 --pipedTo--> E100_N_drawoff
E100 --type--> StrippingColumn
TT200 --monitors--> E100
PI401 --monitors--> E100
TT401 --monitors--> E100
PROC_reboiler_heating_step_06 --operatesOn--> E100
HAZOP_13_13 --concerns--> E100
HAZOP_11_13 --concerns--> E100
LT101 --monitors--> E100
E100_N_sump_outlet --onEquipment--> E100
LSLL102 --monitors--> E100
HAZOP_11_12 --concerns--> E100
OI06 --about--> E100
LSHH100 --monitors--> E100
aspen_v6_1_E100_performance --ofEquipment--> E100
E100_N_overhead --onEquipment--> E100
TT302 --monitors--> E100
HAZOP_7_10 --concerns--> E100
HAZOP_6_07 --concerns--> E100
HAZOP_11_15 --concerns--> E100
E100_N_top_inlet --feedsInto--> E100
PT402 --monitors--> E100
PT401 --monitors--> E100
E100_N_drawoff --onEquipment--> E100
E100_N_side_inlet --onEquipment--> E100
limit_LT101_operating_window --appliesTo--> E100
limit_LZAH100 --appliesTo--> E100
HAZOP_9b_05 --concerns--> E100
RV401 --protects--> E100
E100_N_top_inlet --pipedTo--> E100
E100_N_top_inlet --onEquipment--> E100
HAZOP_13_12 --concerns--> E100
aspen_v3_E100_performance --ofEquipment--> E100
TT301 --monitors--> E100
TT400 --monitors--> E100
HAZOP_7_15 --concerns--> E100
HAZOP_element_11 --covers--> E100
limit_LT101_low_alarm --appliesTo--> E100
TT303 --monitors--> E100
OI11 --about--> E100
limit_PSHH116_set --appliesTo--> E100
HAZOP_13_11 --concerns--> E100
E100_N_reboiler_return --feedsInto--> E100
limit_PSHH400_set --appliesTo--> E100
OI03 --about--> E100
TT103 --monitors--> E100
PSHH400 --monitors--> E100
E100_N_reboiler_return --pipedTo--> E100
HAZOP_8_01 --concerns--> E100
PT102 --monitors--> E100
PSHH116 --monitors--> E100
TT203 --monitors--> E100
limit_LZAL102 --appliesTo--> E100
TT201 --monitors--> E100
HAZOP_6_08 --concerns--> E100
TT300 --monitors--> E100
HAZOP_11_01 --concerns--> E100
E100_N_reboiler_return --onEquipment--> E100
TT202 --monitors--> E100
H100 --tag--> H100
H100 --floor--> 1
H100 --source--> SUMMARY p.102
H100 --type--> SteamReboiler
H100 --feedsInto--> Q106
H100 --pipedTo--> Q106
H100 --label--> H100 vertical thermosiphon steam reboiler
FI102 --monitors--> H100
H100_N_condensate_out --onEquipment--> H100
TT100 --monitors--> H100
aspen_v3_H100_performance --ofEquipment--> H100
FT101 --monitors--> H100
HAZOP_element_13 --covers--> H100
aspen_v6_1_block_H100 --represents--> H100
TI100 --monitors--> H100
PROC_reboiler_heating_step_04 --operatesOn--> H100
DI100 --monitors--> H100
limit_H100_steam_limit --appliesTo--> H100
PI101 --monitors--> H100
PI100 --monitors--> H100
aspen_v3_block_H100REAC --represents--> H100
PT101 --monitors--> H100
FT102 --monitors--> H100
aspen_v3_block_H100HEAT --represents--> H100
TT117 --monitors--> H100
TT118 --monitors--> H100
FI100 --monitors--> H100
Q105 --pipedTo--> H100
H100_N_steam_in --onEquipment--> H100
Q105 --feedsInto--> H100
aspen_v6_1_H100_performance --ofEquipment--> H100
FT100 --monitors--> H100
HAZOP_element_11 --covers--> H100
RV107 --protects--> H100
aspen_v6_1_block_H100 --label--> H100 (ABB_pilot_plant_final_6_1_SA_validation)
aspen_v6_1_block_H100 --blockId--> H100
aspen_v6_1_block_H100 --aspenModel--> HEATX
aspen_v6_1_block_H100 --type--> AspenBlock
aspen_v6_1_block_H100 --statusMessage--> INVALID INPUT SPECIFICATIONS SEE TASC BROWSER FOR INFO.
aspen_v6_1_block_H100 --status--> ERROR
aspen_v6_1_block_H100 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S14 --fromBlock--> aspen_v6_1_block_H100
```

Question: What happens to E100 regeneration if the steam supply to H100 is lost?

## Q57

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
C400_N_cw_out__utlcit01 --location--> C400
C400_N_cw_out__utlcit01 --type--> Citation
C400_N_cw_out__utlcit01 --document--> SRC_PID
C400_N_cw_out__utlcit01 --citationText--> P&ID C400
C400_N_cw_out__utlcit01 --label--> Citation 1 for C400_N_cw_out (utl)
aspen_v3_block_C400 --inCase--> case_aspen_v3
aspen_v3_block_C400 --aspenModel--> HEATER
aspen_v3_block_C400 --type--> AspenBlock
aspen_v3_block_C400 --blockId--> C400
aspen_v3_block_C400 --status--> OK
aspen_v3_block_C400 --label--> C400 (ABB_pilot_plant_final_3)
aspen_v3_stream_S11 --fromBlock--> aspen_v3_block_C400
aspen_v3_stream_S13 --toBlock--> aspen_v3_block_C400
C400_N_cw_in__utlcit01 --type--> Citation
C400_N_cw_in__utlcit01 --document--> SRC_PID
C400_N_cw_in__utlcit01 --citationText--> P&ID C400
C400_N_cw_in__utlcit01 --label--> Citation 1 for C400_N_cw_in (utl)
C400_N_cw_in__utlcit01 --location--> C400
aspen_v6_1_block_C400 --aspenModel--> HEATER
aspen_v6_1_block_C400 --label--> C400 (ABB_pilot_plant_final_6_1_SA_validation)
aspen_v6_1_block_C400 --blockId--> C400
aspen_v6_1_block_C400 --inCase--> case_aspen_v6_1
aspen_v6_1_block_C400 --status--> OK
aspen_v6_1_block_C400 --type--> AspenBlock
aspen_v6_1_stream_S11 --fromBlock--> aspen_v6_1_block_C400
aspen_v6_1_stream_S15 --toBlock--> aspen_v6_1_block_C400
C400 --floor--> 4
C400 --pipedTo--> K401
C400 --type--> Condenser
C400 --label--> C400 overhead condenser (spiral heat exchanger)
C400 --tag--> C400
C400 --note--> Water-cooled; cooling water flow set by FIC402 on FCV401 (cascade from TIC410). Grid not in the REPORT lists (between C8 and E10 on the P&ID).
C400 --feedsInto--> K401
E100_N_overhead --pipedTo--> C400
OOI04 --about--> C400
HAZOP_12_07 --concerns--> C400
aspen_v3_C400_performance --ofEquipment--> C400
OOI06 --about--> C400
HAZOP_12_03 --concerns--> C400
FI402 --monitors--> C400
C400_N_cw_in --onEquipment--> C400
HAZOP_6_05 --concerns--> C400
HAZOP_6_01 --concerns--> C400
C400_N_cw_out --onEquipment--> C400
PT401 --monitors--> C400
HAZOP_element_12 --covers--> C400
TI410 --monitors--> C400
limit_TAH_C400_carryover --appliesTo--> C400
FI401 --monitors--> C400
FT402 --monitors--> C400
HAZOP_6_06 --concerns--> C400
E100_N_overhead --feedsInto--> C400
TT410 --monitors--> C400
E100_N_overhead --type--> Nozzle
E100_N_overhead --onEquipment--> E100
E100_N_overhead --label--> E100 vapour outlet at the top of the column
E100 --feedsInto--> E100_N_overhead
E100 --pipedTo--> E100_N_overhead
C400__ovhcit01 --label--> Citation 1 for C400 (ovh)
C400__ovhcit01 --type--> Citation
C400__ovhcit01 --location--> overhead line after PT401, top of the drawing
C400__ovhcit01 --document--> SRC_PID
C400__ovhcit01 --citationText--> P&ID overhead line after PT401, top of the drawing
PCV415 --pipedTo--> FCV401
PCV415 --normalPosition--> open
PCV415 --note--> Pressure regulator on the C400 cooling water stream (UT09). The valve list gives floor 3.
PCV415 --floor--> 4
PCV415 --type--> PressureControlValve
PCV415 --gridReference--> C14
PCV415 --tag--> PCV415
PCV415 --feedsInto--> FCV401
PCV415 --valveType--> pressure control
PCV415 --label--> PCV415
UT09 --about--> PCV415
V405 --feedsInto--> PCV415
V405 --pipedTo--> PCV415
TIC410 --type--> Controller
TIC410 --tag--> TIC410
TIC410 --label--> C400 gas outlet temperature controller (cascade master)
TIC410 --controls--> FCV401
CL_C400_temperature --hasController--> TIC410
OOI04 --description--> Aspen returns the reflux to the rich feed before the heaters (MIXER2), but on the P&ID it joins after them at V403/V402
OOI04 --foundBy--> ovh section build, Oct 2026
OOI04 --about--> J300
OOI04 --type--> OpenItem
OOI04 --resolvedBy--> Note for model comparison; update the Aspen flowsheet if needed
OOI04 --itemStatus--> open
OOI04 --label--> OOI04: Aspen returns the reflux to the rich feed before the heaters (MIXER2), but on the P&ID it joins after them at V403/V402
HAZOP_6_01 --actionTaken--> Pump shutdown trip added
HAZOP_6_01 --consequence--> No flow to J103
HAZOP_6_01 --concerns--> J103
HAZOP_6_01 --inElement--> HAZOP_element_6
HAZOP_6_01 --cause--> K401 / C300 (now C400) blocked
HAZOP_6_01 --guideword--> NO
HAZOP_6_01 --label--> HAZOP 6.1
HAZOP_6_01 --recommendedAction--> Consider consequences of starving J103
HAZOP_6_01 --parameter--> FLOW
HAZOP_6_01 --type--> HazopDeviation
HAZOP_6_01 --itemNumber--> 1
HAZOP_6_01 --concerns--> K401
TT410 --signalType--> Fieldbus
TT410 --measuredVariable--> temperature of CO2 leaving C400
TT410 --floor--> 4
TT410 --label--> TT410
TT410 --sensorType--> PRT
TT410 --tag--> TT410
TT410 --gridReference--> C15
TT410 --type--> TemperatureInstrument
CL_C400_temperature --hasSensor--> TT410
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_07_J300
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_14_FT305
OverheadRefluxLoop --label--> Stripper overhead and reflux loop
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_09_RV300
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_02_PT401
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_03_C400
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_10_B300
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_08_TT310
OverheadRefluxLoop --note--> Runs whenever E100 is boiling. Vapour is condensed in C400; K401 separates the condensate (returned as reflux by J300) from the CO2-rich gas (to the CO2 return, piece 7).
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_06_LT401
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_05_K401
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_17_E100_N_top_inlet
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_01_E100_N_overhead
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_15_V403
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_00_E100
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_16_V402
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_12_V317
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_13_TT309
OverheadRefluxLoop --type--> Loop
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_04_LSHH400
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_11_PCV302
OverheadRefluxLoop --inMode--> FigureOfEight
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_18_E100
C400__ovhcit03 --citationText--> P&ID differences row LSHH400 (between C400 and K401)
C400__ovhcit03 --location--> row LSHH400 (between C400 and K401)
C400__ovhcit03 --document--> SRC_DIFF
C400__ovhcit03 --label--> Citation 3 for C400 (ovh)
C400__ovhcit03 --type--> Citation
C400_N_cw_in --pipedTo--> C400_N_cw_out
C400_N_cw_in --label--> C400 cooling water inlet
C400_N_cw_in --type--> Nozzle
C400_N_cw_in --feedsInto--> C400_N_cw_out
FT402 --pipedTo--> C400_N_cw_in
FT402 --feedsInto--> C400_N_cw_in
CL_C400_cooling_water --hasFinalElement--> FCV401
CL_C400_cooling_water --controlledVariable--> Cooling water flowrate to C400
CL_C400_cooling_water --manipulatedVariable--> FCV401 opening
CL_C400_cooling_water --label--> Cooling water flow to C400 (cascade slave)
CL_C400_cooling_water --hasController--> FIC402
CL_C400_cooling_water --hasSensor--> FT402
CL_C400_cooling_water --type--> ControlLoop
```

Question: If cooling water flow through C400 falls significantly, what could happen to the CO2 return system?

## Q58

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
K401 --tag--> K401
K401 --pipedTo--> J300
K401 --feedsInto--> J300
K401 --type--> KnockoutDrum
K401 --floor--> 4
K401 --pipedTo--> K401_N_gas_outlet
K401 --note--> The vessel with the hatched demister symbol between C400 and J300. Its label is not legible on the team's P&ID copy; the SUMMARY and DIFF call it K401. The 2010 HAZOP mentions both K400 and K401 (OOI01). Modelled in Aspen as the flash block C400COND.
K401 --feedsInto--> K401_N_gas_outlet
K401 --label--> K401 knockout drum with demister
OOI01 --about--> K401
PT402 --monitors--> K401
C400 --pipedTo--> K401
LT401 --monitors--> K401
HAZOP_12_08 --concerns--> K401
PI402 --monitors--> K401
HAZOP_element_6 --covers--> K401
aspen_v3_K401_performance --ofEquipment--> K401
OOI05 --about--> K401
HAZOP_12_02 --concerns--> K401
LSHH400 --monitors--> K401
K401_N_gas_outlet --onEquipment--> K401
HAZOP_12_09 --concerns--> K401
OOI06 --about--> K401
HAZOP_element_12 --covers--> K401
C400 --feedsInto--> K401
limit_PDAH_K401_demister --appliesTo--> K401
HAZOP_6_01 --concerns--> K401
LSHH400 --measuredVariable--> level high-high switch on the overhead (C400 to K401)
LSHH400 --gridReference--> E10
LSHH400 --label--> LSHH400
LSHH400 --type--> LevelInstrument
LSHH400 --tag--> LSHH400
LSHH400 --floor--> 4
discrepancy_LSHH400_location --concerns--> LSHH400
limit_LZAH_K401 --appliesTo--> LSHH400
OOI05 --about--> LSHH400
HAZOP_element_12 --covers--> LSHH400
K401_N_gas_outlet --pipedTo--> NRV401
K401_N_gas_outlet --feedsInto--> NRV401
K401_N_gas_outlet --type--> Nozzle
K401_N_gas_outlet --label--> K401 gas outlet to the CO2 return (piece 7)
NRV401 --normalPosition--> open
NRV401 --gridReference--> D18
NRV401 --floor--> 4
NRV401 --feedsInto--> FT302
NRV401 --pipedTo--> FT302
NRV401 --type--> CheckValve
NRV401 --label--> NRV401
NRV401 --tag--> NRV401
NRV401 --note--> Non-return valve on the top floor on the CO2 line from K401 (position to trace, GR05).
NRV401 --valveType--> check
GR05 --about--> NRV401
J103 --pipedTo--> SDV171
J103 --tag--> J103
J103 --feedsInto--> SDV171
J103 --note--> Compresses the CO2 from K401 and returns it into K101 via SDV171 (team trace). A shutdown trip protects it if it is starved (HAZOP 6.1).
J103 --gridReference--> M20
J103 --label--> J103 CO2 return compressor (single-stage reciprocating, air-cooled)
J103 --type--> Compressor
J103 --floor--> 1
J103 --pipedTo--> PCV119
HAZOP_6_05 --concerns--> J103
HAZOP_6_01 --concerns--> J103
TT115 --monitors--> J103
K103_CO2_recycle --fromItem--> J103
PSHH118 --monitors--> J103
FT302 --monitors--> J103
HAZOP_6_02 --concerns--> J103
limit_TRIP_J103_starved --appliesTo--> J103
K103 --feedsInto--> J103
GR05 --about--> J103
K103 --pipedTo--> J103
HAZOP_6_09 --concerns--> J103
FT301 --monitors--> J103
HAZOP_element_6 --covers--> J103
GR10 --about--> J103
HAZOP_6_06 --concerns--> J103
PT402 --tag--> PT402
PT402 --measuredVariable--> pressure after K401
PT402 --gridReference--> C16
PT402 --type--> PressureInstrument
PT402 --monitors--> E100
PT402 --signalType--> Fieldbus
PT402 --floor--> 4
PT402 --sensorType--> gauge pressure transmitter
PT402 --label--> PT402
HAZOP_12_02 --concerns--> PT402
HAZOP_element_12 --covers--> PT402
CL_E100_pressure --hasSensor--> PT402
HAZOP_12_09 --inElement--> HAZOP_element_12
HAZOP_12_09 --recommendedAction--> put LAL on K400
HAZOP_12_09 --actionTaken--> LAL added
HAZOP_12_09 --itemNumber--> 9
HAZOP_12_09 --parameter--> LEVEL
HAZOP_12_09 --cause--> control valve open too much
HAZOP_12_09 --consequence--> Backflow through FCV402 - bypass cooler
HAZOP_12_09 --guideword--> LOWER
HAZOP_12_09 --type--> HazopDeviation
HAZOP_12_09 --label--> HAZOP 12.9
GR05 --description--> Order on the CO2 line from K401 (NRV401 > FT302 > FT301 > K103) is inferred; DIFF says FT301/FT302 are in the reverse order to the P&ID
GR05 --type--> OpenItem
GR05 --foundBy--> grt section build, Oct 2026
GR05 --resolvedBy--> Trace on the P&ID
GR05 --label--> GR05: Order on the CO2 line from K401 (NRV401 > FT302 > FT301 > K103) is inferred; DIFF says FT301/FT302 are in the reverse order to the P&ID
GR05 --itemStatus--> open
HAZOP_element_12 --covers--> LT401
HAZOP_element_12 --elementNumber--> 12
HAZOP_element_12 --covers--> C400
HAZOP_element_12 --covers--> PT401
HAZOP_element_12 --source--> HAZOP study, 6-7 May 2010 (27794_Plant_HAZREP_1.xls)
HAZOP_element_12 --type--> HazopElement
HAZOP_element_12 --covers--> J300
HAZOP_element_12 --covers--> FT402
HAZOP_element_12 --label--> HAZOP element 12: OVERHEADS to C300 (400)
HAZOP_12_01 --inElement--> HAZOP_element_12
HAZOP_12_08 --inElement--> HAZOP_element_12
HAZOP_12_06 --inElement--> HAZOP_element_12
HAZOP_12_05 --inElement--> HAZOP_element_12
HAZOP_12_02 --inElement--> HAZOP_element_12
HAZOP_12_10 --inElement--> HAZOP_element_12
HAZOP_12_04 --inElement--> HAZOP_element_12
HAZOP_12_07 --inElement--> HAZOP_element_12
HAZOP_12_03 --inElement--> HAZOP_element_12
HAZOP_6_01 --actionTaken--> Pump shutdown trip added
HAZOP_6_01 --consequence--> No flow to J103
HAZOP_6_01 --inElement--> HAZOP_element_6
HAZOP_6_01 --cause--> K401 / C300 (now C400) blocked
HAZOP_6_01 --guideword--> NO
HAZOP_6_01 --concerns--> C400
HAZOP_6_01 --label--> HAZOP 6.1
HAZOP_6_01 --recommendedAction--> Consider consequences of starving J103
HAZOP_6_01 --parameter--> FLOW
HAZOP_6_01 --type--> HazopDeviation
HAZOP_6_01 --itemNumber--> 1
LT401 --sensorType--> differential pressure transmitter
LT401 --floor--> 4
LT401 --type--> LevelInstrument
LT401 --signalType--> 4-20mA
LT401 --measuredVariable--> liquid level in K401 (control table: 'liquid level in condenser C400')
LT401 --label--> LT401
LT401 --tag--> LT401
LT401 --gridReference--> F10
CL_K401_level --hasSensor--> LT401
OOI05 --about--> LT401
limit_LAL_K401 --appliesTo--> LT401
discrepancy_LSHH400_location --asBuilt--> LSHH400 between C400 and K401
discrepancy_LSHH400_location --drawingShows--> LSHH400 drawn elsewhere
discrepancy_LSHH400_location --gridReference--> E10
discrepancy_LSHH400_location --type--> PIDDiscrepancy
discrepancy_LSHH400_location --label--> LSHH400_location
```

Question: What would happen if the demister in K401 became blocked?

## Q59

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
J103 --pipedTo--> SDV171
J103 --tag--> J103
J103 --feedsInto--> SDV171
J103 --note--> Compresses the CO2 from K401 and returns it into K101 via SDV171 (team trace). A shutdown trip protects it if it is starved (HAZOP 6.1).
J103 --gridReference--> M20
J103 --label--> J103 CO2 return compressor (single-stage reciprocating, air-cooled)
J103 --type--> Compressor
J103 --floor--> 1
J103 --pipedTo--> PCV119
HAZOP_6_05 --concerns--> J103
HAZOP_6_01 --concerns--> J103
TT115 --monitors--> J103
K103_CO2_recycle --fromItem--> J103
PSHH118 --monitors--> J103
FT302 --monitors--> J103
HAZOP_6_02 --concerns--> J103
limit_TRIP_J103_starved --appliesTo--> J103
K103 --feedsInto--> J103
GR05 --about--> J103
K103 --pipedTo--> J103
HAZOP_6_09 --concerns--> J103
FT301 --monitors--> J103
HAZOP_element_6 --covers--> J103
GR10 --about--> J103
HAZOP_6_06 --concerns--> J103
J103__grtcit01 --citationText--> P&ID grid M20
J103__grtcit01 --location--> grid M20
J103__grtcit01 --type--> Citation
J103__grtcit01 --document--> SRC_PID
J103__grtcit01 --label--> Citation 1 for J103 (grt)
Compressor --type--> Class
Compressor --subClassOf--> Equipment
Compressor --comment--> Gas compressor (J103 is a single-stage reciprocating, air-cooled compressor).
HAZOP_6_09 --consequence--> Damage to J103
HAZOP_6_09 --guideword--> INCORRECT
HAZOP_6_09 --type--> HazopDeviation
HAZOP_6_09 --parameter--> COMPOSITION
HAZOP_6_09 --inElement--> HAZOP_element_6
HAZOP_6_09 --safeguard--> separator & demister pad
HAZOP_6_09 --label--> HAZOP 6.9
HAZOP_6_09 --itemNumber--> 9
HAZOP_6_09 --cause--> Excess water carryover
HAZOP_6_09 --recommendedAction--> As above; consider alarmed catchpot upstream of J103
HAZOP_6_09 --actionTaken--> Alarm added
TT115 --floor--> 1
TT115 --label--> TT115
TT115 --type--> TemperatureInstrument
TT115 --signalType--> 4-20mA
TT115 --gridReference--> M20
TT115 --measuredVariable--> J103 temperature
TT115 --sensorType--> K-type thermocouple
TT115 --tag--> TT115
GR05 --description--> Order on the CO2 line from K401 (NRV401 > FT302 > FT301 > K103) is inferred; DIFF says FT301/FT302 are in the reverse order to the P&ID
GR05 --type--> OpenItem
GR05 --about--> NRV401
GR05 --foundBy--> grt section build, Oct 2026
GR05 --resolvedBy--> Trace on the P&ID
GR05 --label--> GR05: Order on the CO2 line from K401 (NRV401 > FT302 > FT301 > K103) is inferred; DIFF says FT301/FT302 are in the reverse order to the P&ID
GR05 --itemStatus--> open
limit_LAH_K103 --type--> OperatingLimit
limit_LAH_K103 --variable--> level
limit_LAH_K103 --source--> HAZOP element 6, item 9 (alarmed catchpot upstream of J103; alarm added)
limit_LAH_K103 --unit--> -
limit_LAH_K103 --appliesTo--> K103
limit_LAH_K103 --limitType--> alarm
limit_LAH_K103 --label--> LAH_K103
limit_LAH_K103 --valueVerified--> false
limit_TRIP_J103_starved --label--> TRIP_J103_starved
limit_TRIP_J103_starved --type--> OperatingLimit
limit_TRIP_J103_starved --limitType--> trip
limit_TRIP_J103_starved --source--> HAZOP element 6, item 1 (pump shutdown trip added)
limit_TRIP_J103_starved --unit--> -
limit_TRIP_J103_starved --valueVerified--> false
limit_TRIP_J103_starved --variable--> suction flow
RV105 --label--> RV105
RV105 --valveType--> relief
RV105 --tag--> RV105
RV105 --type--> ReliefValve
RV105 --gridReference--> K19
RV105 --normalPosition--> closed
RV105 --note--> Next to PCV119 (CO2 return / J103 area). FI07
RV105 --floor--> 1
FI07 --about--> RV105
HAZOP_6_01 --actionTaken--> Pump shutdown trip added
HAZOP_6_01 --consequence--> No flow to J103
HAZOP_6_01 --inElement--> HAZOP_element_6
HAZOP_6_01 --cause--> K401 / C300 (now C400) blocked
HAZOP_6_01 --guideword--> NO
HAZOP_6_01 --concerns--> C400
HAZOP_6_01 --label--> HAZOP 6.1
HAZOP_6_01 --recommendedAction--> Consider consequences of starving J103
HAZOP_6_01 --parameter--> FLOW
HAZOP_6_01 --type--> HazopDeviation
HAZOP_6_01 --itemNumber--> 1
HAZOP_6_01 --concerns--> K401
GR10 --description--> Aspen treats the gas as once-through (no N2 or CO2 recycle), so recycle flows are not simulated
GR10 --label--> GR10: Aspen treats the gas as once-through (no N2 or CO2 recycle), so recycle flows are not simulated
GR10 --about--> J102
GR10 --foundBy--> grt section build, Oct 2026
GR10 --type--> OpenItem
GR10 --resolvedBy--> Note for model comparison
GR10 --itemStatus--> open
V185 --tag--> V185
V185 --normalPosition--> closed
V185 --floor--> 1
V185 --note--> Locked ball valve at J103/K103 (drain); the REPORT gives M20 and M21.
V185 --valveType--> ball
V185 --hasLockingHandle--> true
V185 --type--> ManualValve
V185 --gridReference--> M20
V185 --label--> V185
K103 --pipedTo--> V185
HAZOP_6_06 --itemNumber--> 6
HAZOP_6_06 --recommendedAction--> Put an appropriate alarm around C300 to warn of vapour carryover
HAZOP_6_06 --consequence--> Vapour carryover to J103; damage to J103
HAZOP_6_06 --actionTaken--> Alarm added
HAZOP_6_06 --type--> HazopDeviation
HAZOP_6_06 --guideword--> HIGHER
HAZOP_6_06 --cause--> C300 (C400) not working
HAZOP_6_06 --inElement--> HAZOP_element_6
HAZOP_6_06 --label--> HAZOP 6.6
HAZOP_6_06 --safeguard--> Temp & flow indicators on C300 water throughput
HAZOP_6_06 --parameter--> TEMP.
HAZOP_6_06 --concerns--> C400
FT302 --feedsInto--> FT301
FT302 --measuredVariable--> CO2 return flow (K401 to J103)
FT302 --type--> FlowInstrument
FT302 --signalType--> Profibus-DP
FT302 --gridReference--> G18
FT302 --sensorType--> thermal mass flow meter
FT302 --label--> FT302
FT302 --tag--> FT302
FT302 --floor--> 3
FT302 --pipedTo--> FT301
NRV401 --feedsInto--> FT302
NRV401 --pipedTo--> FT302
HAZOP_element_6 --covers--> FT302
discrepancy_FT301_FT302_order --concerns--> FT302
SDV171 --gridReference--> L19
SDV171 --floor--> 1
SDV171 --note--> On the CO2 return from J103 into K101 (team trace). The REPORT lists it as SOV171 (closed at start, open in operation).
SDV171 --label--> SDV171
SDV171 --feedsInto--> V172
SDV171 --type--> ShutdownValve
SDV171 --tag--> SDV171
SDV171 --pipedTo--> V172
SDV171 --normalPosition--> open
SDV171 --valveType--> shutdown (solenoid-operated)
K103_CO2_recycle --bypasses--> SDV171
HAZOP_element_6 --covers--> SDV171
```

Question: What would be the process consequences if compressor J103 stopped circulating CO2?

## Q60

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
J102 --floor--> 1
J102 --pipedTo--> K101
J102 --tag--> J102
J102 --note--> Blows the recycled N2 from K102 into K101 only (team trace). HAZOP 5.2 (2010) mentions combined spillback and speed control; no spillback is drawn now.
J102 --label--> J102 lobe blower (N2 return)
J102 --type--> Blower
J102 --gridReference--> L17
J102 --feedsInto--> K101
HAZOP_5_01 --concerns--> J102
HAZOP_5_02 --concerns--> J102
K102 --pipedTo--> J102
K102 --feedsInto--> J102
FI304 --monitors--> J102
GR10 --about--> J102
GR01 --about--> J102
HAZOP_5_09 --concerns--> J102
FT107 --monitors--> J102
TT114 --monitors--> J102
TT304 --monitors--> J102
HAZOP_element_5 --covers--> J102
HAZOP_5_04 --concerns--> J102
FI303 --monitors--> J102
aspen_v3_block_E101 --type--> AspenBlock
aspen_v3_block_E101 --aspenModel--> RADFRAC
aspen_v3_block_E101 --blockId--> E101
aspen_v3_block_E101 --status--> OK
aspen_v3_block_E101 --label--> E101 (ABB_pilot_plant_final_3)
aspen_v3_block_E101 --inCase--> case_aspen_v3
aspen_v3_stream_S8 --fromBlock--> aspen_v3_block_E101
aspen_v3_stream_1 --toBlock--> aspen_v3_block_E101
aspen_v3_stream_2 --toBlock--> aspen_v3_block_E101
aspen_v3_stream_4 --fromBlock--> aspen_v3_block_E101
aspen_v6_1_block_E101 --type--> AspenBlock
aspen_v6_1_block_E101 --aspenModel--> RADFRAC
aspen_v6_1_block_E101 --label--> E101 (ABB_pilot_plant_final_6_1_SA_validation)
aspen_v6_1_block_E101 --blockId--> E101
aspen_v6_1_block_E101 --status--> OK
aspen_v6_1_block_E101 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S8 --fromBlock--> aspen_v6_1_block_E101
aspen_v6_1_stream_2 --toBlock--> aspen_v6_1_block_E101
aspen_v6_1_stream_1 --toBlock--> aspen_v6_1_block_E101
aspen_v6_1_stream_4 --fromBlock--> aspen_v6_1_block_E101
E101 --pipedTo--> RV400
E101 --floor--> 1
E101 --note--> Lean MEA enters at the top through NRV400; rich MEA leaves from the sump to J101a/b. The air admittance valve shown on the P&ID has been removed from the plant (DIFF, E14/15).
E101 --feedsInto--> E101_N_sump_outlet
E101 --designBasis--> Packing and column designed for 2.3-2.5 bar operation on MEA and 50 kg/h CO2 (HAZOP 10.4)
E101 --feedsInto--> E101_N_gas_outlet
E101 --pipedTo--> E101_N_sump_outlet
E101 --pipedTo--> E101_N_gas_outlet
E101 --type--> AbsorptionColumn
E101 --diameter_mm--> 230.0
E101 --tag--> E101
E101 --label--> E101 absorber
HAZOP_7_10 --concerns--> E101
TT305 --monitors--> E101
PT111 --monitors--> E101
E101_sample_5 --onColumn--> E101
E101_N_gas_outlet --onEquipment--> E101
LSLL109 --monitors--> E101
TT207 --monitors--> E101
PT403 --monitors--> E101
LI108 --monitors--> E101
E101_sample_4 --onColumn--> E101
E101_N_sump_outlet --onEquipment--> E101
FT109 --monitors--> E101
E101_sample_3 --onColumn--> E101
HAZOP_9b_05 --concerns--> E101
limit_LZAL109 --appliesTo--> E101
DI108 --monitors--> E101
E101_N_gas_inlet --feedsInto--> E101
FT304 --monitors--> E101
LT108 --monitors--> E101
K101_N2_recycle --bypasses--> E101
PT110 --monitors--> E101
E101_N_gas_inlet --pipedTo--> E101
HAZOP_5_08 --concerns--> E101
HAZOP_8_01 --concerns--> E101
HAZOP_8_06 --concerns--> E101
PI403 --monitors--> E101
AT400 --monitors--> E101
FT303 --monitors--> E101
TT205 --monitors--> E101
E101_N_base_inlet --onEquipment--> E101
aspen_v6_1_E101_performance --ofEquipment--> E101
TT206 --monitors--> E101
HAZOP_8_03 --concerns--> E101
E101_N_gas_inlet --onEquipment--> E101
E101_N_top_inlet --feedsInto--> E101
E101_sample_6 --onColumn--> E101
K402 --pipedTo--> E101
HAZOP_5_07 --concerns--> E101
AI300 --monitors--> E101
FI109 --monitors--> E101
FI108 --monitors--> E101
aspen_v3_vent_gas --ofEquipment--> E101
AT300 --monitors--> E101
E101_N_top_inlet --pipedTo--> E101
aspen_v6_1_feed_gas --ofEquipment--> E101
limit_PSHH117_set --appliesTo--> E101
TT109 --monitors--> E101
TT412 --monitors--> E101
HAZOP_10_03 --concerns--> E101
LSHH107 --monitors--> E101
E101_sample_2 --onColumn--> E101
limit_LZAH107 --appliesTo--> E101
HAZOP_5_06 --concerns--> E101
PSHH117 --monitors--> E101
TT413 --monitors--> E101
HAZOP_7_13 --concerns--> E101
TT107 --monitors--> E101
TT306 --monitors--> E101
E101_N_top_inlet --onEquipment--> E101
E101_sample_1 --onColumn--> E101
AOI10 --about--> E101
RV400 --protects--> E101
FT108 --monitors--> E101
TT411 --monitors--> E101
TT204 --monitors--> E101
aspen_v3_feed_gas --ofEquipment--> E101
HAZOP_element_10 --covers--> E101
HAZOP_8_11 --concerns--> E101
TT307 --monitors--> E101
TT308 --monitors--> E101
HAZOP_8_02 --concerns--> E101
aspen_v3_E101_performance --ofEquipment--> E101
PCV300 --valveType--> pressure control
PCV300 --floor--> 3
PCV300 --normalPosition--> open
PCV300 --note--> Vents lean gas from the absorber to hold the E101 pressure (PIC403). Opened in the vent stream start-up (Fig F.3), closed at shutdown.
PCV300 --pipedTo--> VENT_E101
PCV300 --label--> PCV300
PCV300 --feedsInto--> VENT_E101
PCV300 --type--> PressureControlValve
PCV300 --tag--> PCV300
PCV300 --gridReference--> G18
K402 --feedsInto--> PCV300
CL_E101_pressure --hasFinalElement--> PCV300
K402 --pipedTo--> PCV300
PIC403 --controls--> PCV300
AV01 --about--> PCV300
K101 --type--> Saturator
K101 --label--> K101 gas saturator
K101 --pipedTo--> SDV170
K101 --pipedTo--> Z103
K101 --floor--> 1
K101 --feedsInto--> E101_N_gas_inlet
K101 --pipedTo--> E101_N_gas_inlet
K101 --note--> Saturates the feed gas with water before E101; temperature held by TIC121 using C106 on the recirculating water. Grid not in the REPORT lists (near L17 to L18 on the P&ID). Not modelled in Aspen (GOI09).
K101 --pipedTo--> V126
```

Question: If J102 fails during normal operation, what happens to gas circulation through E101?

## Q61

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
PCV300 --valveType--> pressure control
PCV300 --floor--> 3
PCV300 --normalPosition--> open
PCV300 --note--> Vents lean gas from the absorber to hold the E101 pressure (PIC403). Opened in the vent stream start-up (Fig F.3), closed at shutdown.
PCV300 --pipedTo--> VENT_E101
PCV300 --label--> PCV300
PCV300 --feedsInto--> VENT_E101
PCV300 --type--> PressureControlValve
PCV300 --tag--> PCV300
PCV300 --gridReference--> G18
K402 --feedsInto--> PCV300
CL_E101_pressure --hasFinalElement--> PCV300
K402 --pipedTo--> PCV300
PIC403 --controls--> PCV300
AV01 --about--> PCV300
aspen_v3_block_E101 --type--> AspenBlock
aspen_v3_block_E101 --aspenModel--> RADFRAC
aspen_v3_block_E101 --blockId--> E101
aspen_v3_block_E101 --status--> OK
aspen_v3_block_E101 --label--> E101 (ABB_pilot_plant_final_3)
aspen_v3_block_E101 --inCase--> case_aspen_v3
aspen_v3_stream_S8 --fromBlock--> aspen_v3_block_E101
aspen_v3_stream_1 --toBlock--> aspen_v3_block_E101
aspen_v3_stream_2 --toBlock--> aspen_v3_block_E101
aspen_v3_stream_4 --fromBlock--> aspen_v3_block_E101
aspen_v6_1_block_E101 --type--> AspenBlock
aspen_v6_1_block_E101 --aspenModel--> RADFRAC
aspen_v6_1_block_E101 --label--> E101 (ABB_pilot_plant_final_6_1_SA_validation)
aspen_v6_1_block_E101 --blockId--> E101
aspen_v6_1_block_E101 --status--> OK
aspen_v6_1_block_E101 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S8 --fromBlock--> aspen_v6_1_block_E101
aspen_v6_1_stream_2 --toBlock--> aspen_v6_1_block_E101
aspen_v6_1_stream_1 --toBlock--> aspen_v6_1_block_E101
aspen_v6_1_stream_4 --fromBlock--> aspen_v6_1_block_E101
E101 --pipedTo--> RV400
E101 --floor--> 1
E101 --note--> Lean MEA enters at the top through NRV400; rich MEA leaves from the sump to J101a/b. The air admittance valve shown on the P&ID has been removed from the plant (DIFF, E14/15).
E101 --feedsInto--> E101_N_sump_outlet
E101 --designBasis--> Packing and column designed for 2.3-2.5 bar operation on MEA and 50 kg/h CO2 (HAZOP 10.4)
E101 --feedsInto--> E101_N_gas_outlet
E101 --pipedTo--> E101_N_sump_outlet
E101 --pipedTo--> E101_N_gas_outlet
E101 --type--> AbsorptionColumn
E101 --diameter_mm--> 230.0
E101 --tag--> E101
E101 --label--> E101 absorber
HAZOP_7_10 --concerns--> E101
TT305 --monitors--> E101
PT111 --monitors--> E101
E101_sample_5 --onColumn--> E101
E101_N_gas_outlet --onEquipment--> E101
LSLL109 --monitors--> E101
TT207 --monitors--> E101
PT403 --monitors--> E101
LI108 --monitors--> E101
E101_sample_4 --onColumn--> E101
E101_N_sump_outlet --onEquipment--> E101
FT109 --monitors--> E101
E101_sample_3 --onColumn--> E101
HAZOP_9b_05 --concerns--> E101
limit_LZAL109 --appliesTo--> E101
DI108 --monitors--> E101
E101_N_gas_inlet --feedsInto--> E101
FT304 --monitors--> E101
LT108 --monitors--> E101
K101_N2_recycle --bypasses--> E101
PT110 --monitors--> E101
E101_N_gas_inlet --pipedTo--> E101
HAZOP_5_08 --concerns--> E101
HAZOP_8_01 --concerns--> E101
HAZOP_8_06 --concerns--> E101
PI403 --monitors--> E101
AT400 --monitors--> E101
FT303 --monitors--> E101
TT205 --monitors--> E101
E101_N_base_inlet --onEquipment--> E101
aspen_v6_1_E101_performance --ofEquipment--> E101
TT206 --monitors--> E101
HAZOP_8_03 --concerns--> E101
E101_N_gas_inlet --onEquipment--> E101
E101_N_top_inlet --feedsInto--> E101
E101_sample_6 --onColumn--> E101
K402 --pipedTo--> E101
HAZOP_5_07 --concerns--> E101
AI300 --monitors--> E101
FI109 --monitors--> E101
FI108 --monitors--> E101
aspen_v3_vent_gas --ofEquipment--> E101
AT300 --monitors--> E101
E101_N_top_inlet --pipedTo--> E101
aspen_v6_1_feed_gas --ofEquipment--> E101
limit_PSHH117_set --appliesTo--> E101
TT109 --monitors--> E101
TT412 --monitors--> E101
HAZOP_10_03 --concerns--> E101
LSHH107 --monitors--> E101
E101_sample_2 --onColumn--> E101
limit_LZAH107 --appliesTo--> E101
HAZOP_5_06 --concerns--> E101
PSHH117 --monitors--> E101
TT413 --monitors--> E101
HAZOP_7_13 --concerns--> E101
TT107 --monitors--> E101
TT306 --monitors--> E101
E101_N_top_inlet --onEquipment--> E101
E101_sample_1 --onColumn--> E101
AOI10 --about--> E101
RV400 --protects--> E101
FT108 --monitors--> E101
TT411 --monitors--> E101
TT204 --monitors--> E101
aspen_v3_feed_gas --ofEquipment--> E101
HAZOP_element_10 --covers--> E101
HAZOP_8_11 --concerns--> E101
TT307 --monitors--> E101
TT308 --monitors--> E101
HAZOP_8_02 --concerns--> E101
aspen_v3_E101_performance --ofEquipment--> E101
K101 --type--> Saturator
K101 --label--> K101 gas saturator
K101 --pipedTo--> SDV170
K101 --pipedTo--> Z103
K101 --floor--> 1
K101 --feedsInto--> E101_N_gas_inlet
K101 --pipedTo--> E101_N_gas_inlet
K101 --note--> Saturates the feed gas with water before E101; temperature held by TIC121 using C106 on the recirculating water. Grid not in the REPORT lists (near L17 to L18 on the P&ID). Not modelled in Aspen (GOI09).
K101 --pipedTo--> V126
K101 --tag--> K101
DI_CARTRIDGE --feedsInto--> K101
HAZOP_4_06 --concerns--> K101
V172 --pipedTo--> K101
J102 --pipedTo--> K101
limit_LZAL_K101 --appliesTo--> K101
HAZOP_4_07 --concerns--> K101
LT104 --monitors--> K101
HAZOP_3_05 --concerns--> K101
FEED_GAS_HEADER --feedsInto--> K101
GOI09 --about--> K101
LI106 --monitors--> K101
FEED_GAS_HEADER --pipedTo--> K101
limit_LAL_K101 --appliesTo--> K101
K101_N2_recycle --fromItem--> K101
limit_LZAH_K101 --appliesTo--> K101
GOI07 --about--> K101
GOI02 --about--> K101
HAZOP_element_3 --covers--> K101
HAZOP_4_02 --concerns--> K101
TI121 --monitors--> K101
C106 --pipedTo--> K101
```

Question: What could happen if PCV300 remained excessively closed while gas continued entering E101?

## Q62

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
PCV119 --type--> PressureControlValve
PCV119 --gridReference--> K19
PCV119 --label--> PCV119
PCV119 --floor--> 1
PCV119 --tag--> PCV119
PCV119 --note--> E100 pressure control valve on the overhead line (boundary of the loop).
PCV119 --pipedTo--> K103
PCV119 --pipedTo--> VENT_SYSTEM
PCV119 --valveType--> pressure control
PCV119 --normalPosition--> open
K103_CO2_recycle --routeVia--> PCV119
GR07 --about--> PCV119
CL_E100_pressure --hasFinalElement--> PCV119
PIC401 --controls--> PCV119
HAZOP_element_6 --covers--> PCV119
PIC402 --controls--> PCV119
HAZOP_6_05 --concerns--> PCV119
J103 --pipedTo--> PCV119
aspen_v3_block_E100 --label--> E100 (ABB_pilot_plant_final_3)
aspen_v3_block_E100 --represents--> E100
aspen_v3_block_E100 --aspenModel--> RADFRAC
aspen_v3_block_E100 --inCase--> case_aspen_v3
aspen_v3_block_E100 --status--> WARNING
aspen_v3_block_E100 --statusMessage--> FEED PRESSURE IS LOWER THAN STAGE PRESSURE.
aspen_v3_block_E100 --type--> AspenBlock
aspen_v3_block_E100 --blockId--> E100
aspen_v3_stream_S13 --fromBlock--> aspen_v3_block_E100
aspen_v3_stream_S10 --toBlock--> aspen_v3_block_E100
aspen_v3_stream_S6 --fromBlock--> aspen_v3_block_E100
aspen_v3_stream_S14 --fromBlock--> aspen_v3_block_E100
aspen_v3_stream_S24 --toBlock--> aspen_v3_block_E100
aspen_v6_1_block_E100 --inCase--> case_aspen_v6_1
aspen_v6_1_block_E100 --statusMessage--> RATESEP CALCULATIONS FAILED TO CONVERGE.
aspen_v6_1_block_E100 --status--> ERROR
aspen_v6_1_block_E100 --represents--> E100
aspen_v6_1_block_E100 --label--> E100 (ABB_pilot_plant_final_6_1_SA_validation)
aspen_v6_1_block_E100 --type--> AspenBlock
aspen_v6_1_block_E100 --blockId--> E100
aspen_v6_1_block_E100 --aspenModel--> RADFRAC
aspen_v6_1_stream_S15 --fromBlock--> aspen_v6_1_block_E100
aspen_v6_1_stream_S23 --fromBlock--> aspen_v6_1_block_E100
aspen_v6_1_stream_S10 --toBlock--> aspen_v6_1_block_E100
aspen_v6_1_stream_S12 --fromBlock--> aspen_v6_1_block_E100
aspen_v6_1_stream_S14 --toBlock--> aspen_v6_1_block_E100
E100 --floor--> 1
E100 --hasStage--> E100_stage_12
E100 --diameter_mm--> 264.62
E100 --tag--> E100
E100 --label--> E100 stripper (desorber)
E100 --hasStage--> E100_stage_08
E100 --hasStage--> E100_stage_01
E100 --hasStage--> E100_stage_04
E100 --feedsInto--> E100_N_overhead
E100 --hasStage--> E100_stage_07
E100 --pipedTo--> E100_N_overhead
E100 --note--> Chimney tray below the bottom packed bed separates the draw-off section (stage 11) from the sump (stage 12).
E100 --hasStage--> E100_stage_02
E100 --hasStage--> E100_stage_09
E100 --feedsInto--> E100_N_sump_outlet
E100 --hasStage--> E100_stage_06
E100 --feedsInto--> E100_N_drawoff
E100 --pipedTo--> E100_N_sump_outlet
E100 --hasStage--> E100_stage_05
E100 --hasStage--> E100_stage_11
E100 --hasStage--> E100_stage_10
E100 --designBasis--> Designed for sub-atmospheric pressure (vacuum), per HAZOP element 11 item 10. Design pressure value not documented.
E100 --hasStage--> E100_stage_03
E100 --pipedTo--> E100_N_drawoff
E100 --type--> StrippingColumn
TT200 --monitors--> E100
PI401 --monitors--> E100
TT401 --monitors--> E100
PROC_reboiler_heating_step_06 --operatesOn--> E100
HAZOP_13_13 --concerns--> E100
HAZOP_11_13 --concerns--> E100
LT101 --monitors--> E100
E100_N_sump_outlet --onEquipment--> E100
LSLL102 --monitors--> E100
HAZOP_11_12 --concerns--> E100
OI06 --about--> E100
LSHH100 --monitors--> E100
aspen_v6_1_E100_performance --ofEquipment--> E100
E100_N_overhead --onEquipment--> E100
TT302 --monitors--> E100
HAZOP_7_10 --concerns--> E100
HAZOP_6_07 --concerns--> E100
HAZOP_11_15 --concerns--> E100
E100_N_top_inlet --feedsInto--> E100
PT402 --monitors--> E100
PT401 --monitors--> E100
E100_N_drawoff --onEquipment--> E100
E100_N_side_inlet --onEquipment--> E100
limit_LT101_operating_window --appliesTo--> E100
limit_LZAH100 --appliesTo--> E100
HAZOP_9b_05 --concerns--> E100
RV401 --protects--> E100
E100_N_top_inlet --pipedTo--> E100
E100_N_top_inlet --onEquipment--> E100
HAZOP_13_12 --concerns--> E100
aspen_v3_E100_performance --ofEquipment--> E100
TT301 --monitors--> E100
TT400 --monitors--> E100
HAZOP_7_15 --concerns--> E100
HAZOP_element_11 --covers--> E100
limit_LT101_low_alarm --appliesTo--> E100
TT303 --monitors--> E100
OI11 --about--> E100
limit_PSHH116_set --appliesTo--> E100
HAZOP_13_11 --concerns--> E100
E100_N_reboiler_return --feedsInto--> E100
limit_PSHH400_set --appliesTo--> E100
OI03 --about--> E100
TT103 --monitors--> E100
PSHH400 --monitors--> E100
E100_N_reboiler_return --pipedTo--> E100
HAZOP_8_01 --concerns--> E100
PT102 --monitors--> E100
PSHH116 --monitors--> E100
TT203 --monitors--> E100
limit_LZAL102 --appliesTo--> E100
TT201 --monitors--> E100
HAZOP_6_08 --concerns--> E100
TT300 --monitors--> E100
HAZOP_11_01 --concerns--> E100
E100_N_reboiler_return --onEquipment--> E100
TT202 --monitors--> E100
LSHH100 --tag--> LSHH100
LSHH100 --note--> Stage mapping inferred: odd Aspen stages are the gaps between packed beds where the side instruments sit; floors match REPORT.
LSHH100 --locatedAtStage--> E100_stage_12
LSHH100 --type--> LevelInstrument
LSHH100 --measuredVariable--> level high-high switch
LSHH100 --floor--> 1
LSHH100 --label--> LSHH100
IL_E100_level_HH --initiatedBy--> LSHH100
PT402 --tag--> PT402
PT402 --monitors--> K401
PT402 --measuredVariable--> pressure after K401
PT402 --gridReference--> C16
PT402 --type--> PressureInstrument
PT402 --signalType--> Fieldbus
PT402 --floor--> 4
PT402 --sensorType--> gauge pressure transmitter
PT402 --label--> PT402
HAZOP_12_02 --concerns--> PT402
HAZOP_element_12 --covers--> PT402
CL_E100_pressure --hasSensor--> PT402
NRV106 --tag--> NRV106
NRV106 --valveType--> check
NRV106 --floor--> 1
NRV106 --note--> Near V112 at the E100 sump outlet. FI07
```

Question: What are the consequences if PCV119 cannot respond to increasing stripper pressure?

## Q63

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
aspen_v3_block_E101 --type--> AspenBlock
aspen_v3_block_E101 --aspenModel--> RADFRAC
aspen_v3_block_E101 --blockId--> E101
aspen_v3_block_E101 --status--> OK
aspen_v3_block_E101 --label--> E101 (ABB_pilot_plant_final_3)
aspen_v3_block_E101 --inCase--> case_aspen_v3
aspen_v3_stream_S8 --fromBlock--> aspen_v3_block_E101
aspen_v3_stream_1 --toBlock--> aspen_v3_block_E101
aspen_v3_stream_2 --toBlock--> aspen_v3_block_E101
aspen_v3_stream_4 --fromBlock--> aspen_v3_block_E101
aspen_v6_1_block_E101 --type--> AspenBlock
aspen_v6_1_block_E101 --aspenModel--> RADFRAC
aspen_v6_1_block_E101 --label--> E101 (ABB_pilot_plant_final_6_1_SA_validation)
aspen_v6_1_block_E101 --blockId--> E101
aspen_v6_1_block_E101 --status--> OK
aspen_v6_1_block_E101 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S8 --fromBlock--> aspen_v6_1_block_E101
aspen_v6_1_stream_2 --toBlock--> aspen_v6_1_block_E101
aspen_v6_1_stream_1 --toBlock--> aspen_v6_1_block_E101
aspen_v6_1_stream_4 --fromBlock--> aspen_v6_1_block_E101
E101 --pipedTo--> RV400
E101 --floor--> 1
E101 --note--> Lean MEA enters at the top through NRV400; rich MEA leaves from the sump to J101a/b. The air admittance valve shown on the P&ID has been removed from the plant (DIFF, E14/15).
E101 --feedsInto--> E101_N_sump_outlet
E101 --designBasis--> Packing and column designed for 2.3-2.5 bar operation on MEA and 50 kg/h CO2 (HAZOP 10.4)
E101 --feedsInto--> E101_N_gas_outlet
E101 --pipedTo--> E101_N_sump_outlet
E101 --pipedTo--> E101_N_gas_outlet
E101 --type--> AbsorptionColumn
E101 --diameter_mm--> 230.0
E101 --tag--> E101
E101 --label--> E101 absorber
HAZOP_7_10 --concerns--> E101
TT305 --monitors--> E101
PT111 --monitors--> E101
E101_sample_5 --onColumn--> E101
E101_N_gas_outlet --onEquipment--> E101
LSLL109 --monitors--> E101
TT207 --monitors--> E101
PT403 --monitors--> E101
LI108 --monitors--> E101
E101_sample_4 --onColumn--> E101
E101_N_sump_outlet --onEquipment--> E101
FT109 --monitors--> E101
E101_sample_3 --onColumn--> E101
HAZOP_9b_05 --concerns--> E101
limit_LZAL109 --appliesTo--> E101
DI108 --monitors--> E101
E101_N_gas_inlet --feedsInto--> E101
FT304 --monitors--> E101
LT108 --monitors--> E101
K101_N2_recycle --bypasses--> E101
PT110 --monitors--> E101
E101_N_gas_inlet --pipedTo--> E101
HAZOP_5_08 --concerns--> E101
HAZOP_8_01 --concerns--> E101
HAZOP_8_06 --concerns--> E101
PI403 --monitors--> E101
AT400 --monitors--> E101
FT303 --monitors--> E101
TT205 --monitors--> E101
E101_N_base_inlet --onEquipment--> E101
aspen_v6_1_E101_performance --ofEquipment--> E101
TT206 --monitors--> E101
HAZOP_8_03 --concerns--> E101
E101_N_gas_inlet --onEquipment--> E101
E101_N_top_inlet --feedsInto--> E101
E101_sample_6 --onColumn--> E101
K402 --pipedTo--> E101
HAZOP_5_07 --concerns--> E101
AI300 --monitors--> E101
FI109 --monitors--> E101
FI108 --monitors--> E101
aspen_v3_vent_gas --ofEquipment--> E101
AT300 --monitors--> E101
E101_N_top_inlet --pipedTo--> E101
aspen_v6_1_feed_gas --ofEquipment--> E101
limit_PSHH117_set --appliesTo--> E101
TT109 --monitors--> E101
TT412 --monitors--> E101
HAZOP_10_03 --concerns--> E101
LSHH107 --monitors--> E101
E101_sample_2 --onColumn--> E101
limit_LZAH107 --appliesTo--> E101
HAZOP_5_06 --concerns--> E101
PSHH117 --monitors--> E101
TT413 --monitors--> E101
HAZOP_7_13 --concerns--> E101
TT107 --monitors--> E101
TT306 --monitors--> E101
E101_N_top_inlet --onEquipment--> E101
E101_sample_1 --onColumn--> E101
AOI10 --about--> E101
RV400 --protects--> E101
FT108 --monitors--> E101
TT411 --monitors--> E101
TT204 --monitors--> E101
aspen_v3_feed_gas --ofEquipment--> E101
HAZOP_element_10 --covers--> E101
HAZOP_8_11 --concerns--> E101
TT307 --monitors--> E101
TT308 --monitors--> E101
HAZOP_8_02 --concerns--> E101
aspen_v3_E101_performance --ofEquipment--> E101
PCV300 --valveType--> pressure control
PCV300 --floor--> 3
PCV300 --normalPosition--> open
PCV300 --note--> Vents lean gas from the absorber to hold the E101 pressure (PIC403). Opened in the vent stream start-up (Fig F.3), closed at shutdown.
PCV300 --pipedTo--> VENT_E101
PCV300 --label--> PCV300
PCV300 --feedsInto--> VENT_E101
PCV300 --type--> PressureControlValve
PCV300 --tag--> PCV300
PCV300 --gridReference--> G18
K402 --feedsInto--> PCV300
CL_E101_pressure --hasFinalElement--> PCV300
K402 --pipedTo--> PCV300
PIC403 --controls--> PCV300
AV01 --about--> PCV300
K101 --type--> Saturator
K101 --label--> K101 gas saturator
K101 --pipedTo--> SDV170
K101 --pipedTo--> Z103
K101 --floor--> 1
K101 --feedsInto--> E101_N_gas_inlet
K101 --pipedTo--> E101_N_gas_inlet
K101 --note--> Saturates the feed gas with water before E101; temperature held by TIC121 using C106 on the recirculating water. Grid not in the REPORT lists (near L17 to L18 on the P&ID). Not modelled in Aspen (GOI09).
K101 --pipedTo--> V126
K101 --tag--> K101
DI_CARTRIDGE --feedsInto--> K101
HAZOP_4_06 --concerns--> K101
V172 --pipedTo--> K101
J102 --pipedTo--> K101
limit_LZAL_K101 --appliesTo--> K101
HAZOP_4_07 --concerns--> K101
LT104 --monitors--> K101
HAZOP_3_05 --concerns--> K101
FEED_GAS_HEADER --feedsInto--> K101
GOI09 --about--> K101
LI106 --monitors--> K101
FEED_GAS_HEADER --pipedTo--> K101
limit_LAL_K101 --appliesTo--> K101
K101_N2_recycle --fromItem--> K101
limit_LZAH_K101 --appliesTo--> K101
GOI07 --about--> K101
GOI02 --about--> K101
HAZOP_element_3 --covers--> K101
HAZOP_4_02 --concerns--> K101
TI121 --monitors--> K101
C106 --pipedTo--> K101
```

Question: If the liquid level in E101 rises rapidly, how could the two MEA transfer pumps be responsible?

## Q64

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
aspen_v3_block_E100 --label--> E100 (ABB_pilot_plant_final_3)
aspen_v3_block_E100 --represents--> E100
aspen_v3_block_E100 --aspenModel--> RADFRAC
aspen_v3_block_E100 --inCase--> case_aspen_v3
aspen_v3_block_E100 --status--> WARNING
aspen_v3_block_E100 --statusMessage--> FEED PRESSURE IS LOWER THAN STAGE PRESSURE.
aspen_v3_block_E100 --type--> AspenBlock
aspen_v3_block_E100 --blockId--> E100
aspen_v3_stream_S13 --fromBlock--> aspen_v3_block_E100
aspen_v3_stream_S10 --toBlock--> aspen_v3_block_E100
aspen_v3_stream_S6 --fromBlock--> aspen_v3_block_E100
aspen_v3_stream_S14 --fromBlock--> aspen_v3_block_E100
aspen_v3_stream_S24 --toBlock--> aspen_v3_block_E100
aspen_v6_1_block_E100 --inCase--> case_aspen_v6_1
aspen_v6_1_block_E100 --statusMessage--> RATESEP CALCULATIONS FAILED TO CONVERGE.
aspen_v6_1_block_E100 --status--> ERROR
aspen_v6_1_block_E100 --represents--> E100
aspen_v6_1_block_E100 --label--> E100 (ABB_pilot_plant_final_6_1_SA_validation)
aspen_v6_1_block_E100 --type--> AspenBlock
aspen_v6_1_block_E100 --blockId--> E100
aspen_v6_1_block_E100 --aspenModel--> RADFRAC
aspen_v6_1_stream_S15 --fromBlock--> aspen_v6_1_block_E100
aspen_v6_1_stream_S23 --fromBlock--> aspen_v6_1_block_E100
aspen_v6_1_stream_S10 --toBlock--> aspen_v6_1_block_E100
aspen_v6_1_stream_S12 --fromBlock--> aspen_v6_1_block_E100
aspen_v6_1_stream_S14 --toBlock--> aspen_v6_1_block_E100
E100 --floor--> 1
E100 --hasStage--> E100_stage_12
E100 --diameter_mm--> 264.62
E100 --tag--> E100
E100 --label--> E100 stripper (desorber)
E100 --hasStage--> E100_stage_08
E100 --hasStage--> E100_stage_01
E100 --hasStage--> E100_stage_04
E100 --feedsInto--> E100_N_overhead
E100 --hasStage--> E100_stage_07
E100 --pipedTo--> E100_N_overhead
E100 --note--> Chimney tray below the bottom packed bed separates the draw-off section (stage 11) from the sump (stage 12).
E100 --hasStage--> E100_stage_02
E100 --hasStage--> E100_stage_09
E100 --feedsInto--> E100_N_sump_outlet
E100 --hasStage--> E100_stage_06
E100 --feedsInto--> E100_N_drawoff
E100 --pipedTo--> E100_N_sump_outlet
E100 --hasStage--> E100_stage_05
E100 --hasStage--> E100_stage_11
E100 --hasStage--> E100_stage_10
E100 --designBasis--> Designed for sub-atmospheric pressure (vacuum), per HAZOP element 11 item 10. Design pressure value not documented.
E100 --hasStage--> E100_stage_03
E100 --pipedTo--> E100_N_drawoff
E100 --type--> StrippingColumn
TT200 --monitors--> E100
PI401 --monitors--> E100
TT401 --monitors--> E100
PROC_reboiler_heating_step_06 --operatesOn--> E100
HAZOP_13_13 --concerns--> E100
HAZOP_11_13 --concerns--> E100
LT101 --monitors--> E100
E100_N_sump_outlet --onEquipment--> E100
LSLL102 --monitors--> E100
HAZOP_11_12 --concerns--> E100
OI06 --about--> E100
LSHH100 --monitors--> E100
aspen_v6_1_E100_performance --ofEquipment--> E100
E100_N_overhead --onEquipment--> E100
TT302 --monitors--> E100
HAZOP_7_10 --concerns--> E100
HAZOP_6_07 --concerns--> E100
HAZOP_11_15 --concerns--> E100
E100_N_top_inlet --feedsInto--> E100
PT402 --monitors--> E100
PT401 --monitors--> E100
E100_N_drawoff --onEquipment--> E100
E100_N_side_inlet --onEquipment--> E100
limit_LT101_operating_window --appliesTo--> E100
limit_LZAH100 --appliesTo--> E100
HAZOP_9b_05 --concerns--> E100
RV401 --protects--> E100
E100_N_top_inlet --pipedTo--> E100
E100_N_top_inlet --onEquipment--> E100
HAZOP_13_12 --concerns--> E100
aspen_v3_E100_performance --ofEquipment--> E100
TT301 --monitors--> E100
TT400 --monitors--> E100
HAZOP_7_15 --concerns--> E100
HAZOP_element_11 --covers--> E100
limit_LT101_low_alarm --appliesTo--> E100
TT303 --monitors--> E100
OI11 --about--> E100
limit_PSHH116_set --appliesTo--> E100
HAZOP_13_11 --concerns--> E100
E100_N_reboiler_return --feedsInto--> E100
limit_PSHH400_set --appliesTo--> E100
OI03 --about--> E100
TT103 --monitors--> E100
PSHH400 --monitors--> E100
E100_N_reboiler_return --pipedTo--> E100
HAZOP_8_01 --concerns--> E100
PT102 --monitors--> E100
PSHH116 --monitors--> E100
TT203 --monitors--> E100
limit_LZAL102 --appliesTo--> E100
TT201 --monitors--> E100
HAZOP_6_08 --concerns--> E100
TT300 --monitors--> E100
HAZOP_11_01 --concerns--> E100
E100_N_reboiler_return --onEquipment--> E100
TT202 --monitors--> E100
LSHH100 --tag--> LSHH100
LSHH100 --note--> Stage mapping inferred: odd Aspen stages are the gaps between packed beds where the side instruments sit; floors match REPORT.
LSHH100 --locatedAtStage--> E100_stage_12
LSHH100 --type--> LevelInstrument
LSHH100 --measuredVariable--> level high-high switch
LSHH100 --floor--> 1
LSHH100 --label--> LSHH100
IL_E100_level_HH --initiatedBy--> LSHH100
PT402 --tag--> PT402
PT402 --monitors--> K401
PT402 --measuredVariable--> pressure after K401
PT402 --gridReference--> C16
PT402 --type--> PressureInstrument
PT402 --signalType--> Fieldbus
PT402 --floor--> 4
PT402 --sensorType--> gauge pressure transmitter
PT402 --label--> PT402
HAZOP_12_02 --concerns--> PT402
HAZOP_element_12 --covers--> PT402
CL_E100_pressure --hasSensor--> PT402
NRV106 --tag--> NRV106
NRV106 --valveType--> check
NRV106 --floor--> 1
NRV106 --note--> Near V112 at the E100 sump outlet. FI07
NRV106 --type--> CheckValve
NRV106 --label--> NRV106
NRV106 --gridReference--> M8
Route_D_side_bypass_step_38_E100 --stepIndex--> 38
Route_D_side_bypass_step_38_E100 --label--> Route D: side return (stage 3), Z102 bypassed step 38: E100
Route_D_side_bypass_step_38_E100 --stepType--> inline
Route_D_side_bypass_step_38_E100 --stepItem--> E100
Route_D_side_bypass_step_38_E100 --type--> LoopStep
Route_D_side_bypass_step_37_E100_N_side_inlet --nextStep--> Route_D_side_bypass_step_38_E100
Route_B_top_bypass_step_10_E100 --nextStep--> Route_B_top_bypass_step_11_E100_N_sump_outlet
Route_B_top_bypass_step_10_E100 --stepItem--> E100
Route_B_top_bypass_step_10_E100 --stepIndex--> 10
Route_B_top_bypass_step_10_E100 --stepType--> inline
Route_B_top_bypass_step_10_E100 --type--> LoopStep
Route_B_top_bypass_step_10_E100 --label--> Route B: top return (stage 1), Z102 bypassed step 10: E100
Route_B_top_bypass_step_09_E100_N_reboiler_return --nextStep--> Route_B_top_bypass_step_10_E100
aspen_v3_stream_S10 --temperature_C--> 89.99877
aspen_v3_stream_S10 --phase--> MIXED
```

Question: If the level in E100 rises while rich MEA is being transferred, what imbalance should be investigated?

## Q65

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
J100 --floor--> 1
J100 --gridReference--> M10
J100 --note--> Speed set by SIC100. HAZOP 7.11 refers to diaphragm changes.
J100 --feedsInto--> PCV122
J100 --type--> Pump
J100 --label--> J100 lean MEA pump
J100 --pipedTo--> PCV122
J100 --pipedTo--> RV101
J100 --tag--> J100
FI103 --monitors--> J100
PROC_Z102_bypass_step_01 --operatesOn--> J100
V113b --feedsInto--> J100
PROC_stripping_loop_lineup_step_28 --operatesOn--> J100
CL_J100_flow --hasFinalElement--> J100
FI104 --monitors--> J100
IL_E100_level_LL --tripsItem--> J100
HAZOP_7_14 --concerns--> J100
TT106 --monitors--> J100
V113b --pipedTo--> J100
HAZOP_7_01 --concerns--> J100
HAZOP_11_12 --concerns--> J100
HS100 --controls--> J100
FT103 --monitors--> J100
HAZOP_element_7 --covers--> J100
limit_J100_power_range --appliesTo--> J100
FIC104 --controls--> J100
HAZOP_11_13 --concerns--> J100
FT104 --monitors--> J100
limit_J100_cavitation --appliesTo--> J100
HAZOP_7_11 --concerns--> J100
PROC_Z102_bypass_step_05 --operatesOn--> J100
PT104 --monitors--> J100
limit_J100_flow_range --appliesTo--> J100
OI11 --about--> J100
PROC_stripping_loop_lineup_step_01 --operatesOn--> J100
RV101 --protects--> J100
FIC103 --controls--> J100
IL_E100_level_HH --tripsItem--> J100
SIC100 --controls--> J100
limit_TZAH106 --appliesTo--> J100
HAZOP_7_15 --concerns--> J100
HAZOP_7_02 --concerns--> J100
LT101 --gridReference--> K8
LT101 --signalType--> Profibus-PA
LT101 --locatedAtStage--> E100_stage_12
LT101 --monitors--> E100
LT101 --note--> Stage mapping inferred: odd Aspen stages are the gaps between packed beds where the side instruments sit; floors match REPORT.
LT101 --sensorType--> differential pressure transmitter
LT101 --type--> LevelInstrument
LT101 --floor--> 1
LT101 --label--> LT101
LT101 --tag--> LT101
LT101 --measuredVariable--> level
IL_E100_level_LL --initiatedBy--> LT101
StrippingLoop_step_20_J100 --stepIndex--> 20
StrippingLoop_step_20_J100 --stepType--> inline
StrippingLoop_step_20_J100 --label--> Stripping loop step 20: J100
StrippingLoop_step_20_J100 --stepItem--> J100
StrippingLoop_step_20_J100 --type--> LoopStep
PROC_pump_start_order_step_01 --operatesOn--> LT108
PROC_pump_start_order_step_01 --stepOrder--> 1
PROC_pump_start_order_step_01 --type--> ProcedureStep
PROC_pump_start_order_step_01 --instruction--> Compare LT101 (E100) and LT108 (E101)
PROC_pump_start_order_step_01 --label--> Order of starting J100 and J101a/b step 1
PROC_pump_start_order --hasProcedureStep--> PROC_pump_start_order_step_01
HAZOP_7_14 --concerns--> RV101
HAZOP_7_14 --parameter--> PRESSURE
HAZOP_7_14 --label--> HAZOP 7.14
HAZOP_7_14 --guideword--> HIGHER
HAZOP_7_14 --type--> HazopDeviation
HAZOP_7_14 --cause--> Isolation d/s of J100
HAZOP_7_14 --safeguard--> RV101
HAZOP_7_14 --itemNumber--> 14
HAZOP_7_14 --inElement--> HAZOP_element_7
PROC_Z102_bypass_step_05 --type--> ProcedureStep
PROC_Z102_bypass_step_05 --label--> Z102 filter bypass step 5
PROC_Z102_bypass_step_05 --instruction--> Return J100 to the previous steady-state power
PROC_Z102_bypass_step_05 --stepOrder--> 5
PROC_Z102_bypass --hasProcedureStep--> PROC_Z102_bypass_step_05
Route_B_top_bypass_step_20_J100 --label--> Route B: top return (stage 1), Z102 bypassed step 20: J100
Route_B_top_bypass_step_20_J100 --stepType--> inline
Route_B_top_bypass_step_20_J100 --stepIndex--> 20
Route_B_top_bypass_step_20_J100 --type--> LoopStep
Route_B_top_bypass_step_20_J100 --nextStep--> Route_B_top_bypass_step_24_PCV122
Route_B_top_bypass_step_20_J100 --stepItem--> J100
Route_B_top_bypass_step_19_V113b --nextStep--> Route_B_top_bypass_step_20_J100
SIC100 --tag--> SIC100
SIC100 --type--> Controller
SIC100 --label--> J100 speed controller
CL_J100_flow --hasController--> SIC100
TT106 --gridReference--> L10
TT106 --sensorType--> PRT
TT106 --signalType--> 4-20mA
TT106 --floor--> 1
TT106 --type--> TemperatureInstrument
TT106 --label--> TT106
TT106 --measuredVariable--> temperature
TT106 --tag--> TT106
J100__cit02 --citationText--> Pilot Plant Report section 2.5 (pump trials)
J100__cit02 --document--> SRC_REPORT
J100__cit02 --location--> section 2.5 (pump trials)
J100__cit02 --label--> Citation 2 for J100
J100__cit02 --type--> Citation
limit_J100_flow_range --label--> J100_flow_range
limit_J100_flow_range --limitType--> range
limit_J100_flow_range --unit--> L/min
limit_J100_flow_range --lowValue--> 10.79
limit_J100_flow_range --note--> P&ID design range. In the commissioning test J100 delivered 272 to 1051 kg/h (about 4.5 to 17.5 L/min), so it ran below this range at low pump power.
limit_J100_flow_range --variable--> volumetric flow
limit_J100_flow_range --source--> P&ID; TEAM confirmed on full-size P&ID; REPORT Fig E.4
limit_J100_flow_range --type--> OperatingLimit
limit_J100_flow_range --valueVerified--> true
limit_J100_flow_range --highValue--> 19.7
limit_LZAL102 --label--> LZAL102
limit_LZAL102 --unit--> %
limit_LZAL102 --type--> OperatingLimit
limit_LZAL102 --valueVerified--> true
limit_LZAL102 --limitType--> trip
limit_LZAL102 --variable--> level
limit_LZAL102 --lowValue--> 1.0
limit_LZAL102 --note--> LSLL: emergency shutdown; protects J100 from starvation.
limit_LZAL102 --source--> REPORT 2.2; HAZOP 7.15, 11.15
limit_LZAL102 --appliesTo--> E100
HAZOP_7_01 --inElement--> HAZOP_element_7
HAZOP_7_01 --guideword--> NO
HAZOP_7_01 --consequence--> Overheat pump
HAZOP_7_01 --label--> HAZOP 7.1
HAZOP_7_01 --parameter--> FLOW
HAZOP_7_01 --safeguard--> TZAH104 (now TZAH106)
HAZOP_7_01 --itemNumber--> 1
HAZOP_7_01 --type--> HazopDeviation
HAZOP_7_01 --cause--> Isolation valve closed anywhere along line
OI11 --label--> OI11: Cause and effect (e.g. what happens to the E100 level if J100 trips) is not modelled
OI11 --itemStatus--> open
OI11 --foundBy--> S10
OI11 --about--> E100
OI11 --description--> Cause and effect (e.g. what happens to the E100 level if J100 trips) is not modelled
OI11 --resolvedBy--> Cause and effect chart, or a dynamic model
OI11 --type--> OpenItem
FI104 --label--> FI104
FI104 --measuredVariable--> flow indication
FI104 --tag--> FI104
FI104 --floor--> 1
FI104 --type--> FlowInstrument
PROC_Z102_bypass_step_01 --type--> ProcedureStep
PROC_Z102_bypass_step_01 --stepOrder--> 1
PROC_Z102_bypass_step_01 --label--> Z102 filter bypass step 1
PROC_Z102_bypass_step_01 --instruction--> Reduce J100 power by 20 % per minute until it reaches 15 %
PROC_Z102_bypass --hasProcedureStep--> PROC_Z102_bypass_step_01
SDV125 --floor--> 1
```

Question: Why might LT101 fall rapidly when J100 speed increases, and what could happen to the pump?

## Q66

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
Z102 --pipedTo--> V117b
Z102 --feedsInto--> V117b
Z102 --label--> Z102 MEA filter
Z102 --type--> Filter
Z102 --floor--> 1
Z102 --tag--> Z102
Z102 --filterRating_um--> 50.0
Z102_bypass --bypasses--> Z102
PDT105 --monitors--> Z102
V117a --pipedTo--> Z102
V117a --feedsInto--> Z102
HAZOP_7_03 --concerns--> Z102
OI08 --about--> Z102
limit_PDT105_blocked_filter --appliesTo--> Z102
HAZOP_element_7 --covers--> Z102
V120 --bypasses--> Z102
PROC_Z102_bypass_step_06 --operatesOn--> Z102
PROC_Z102_bypass --hasProcedureStep--> PROC_Z102_bypass_step_02
PROC_Z102_bypass --triggerCondition--> PDT105 at or above 0.45 bar (Z102 blocked)
PROC_Z102_bypass --hasProcedureStep--> PROC_Z102_bypass_step_05
PROC_Z102_bypass --hasProcedureStep--> PROC_Z102_bypass_step_04
PROC_Z102_bypass --type--> Procedure
PROC_Z102_bypass --hasProcedureStep--> PROC_Z102_bypass_step_03
PROC_Z102_bypass --label--> Z102 filter bypass
PROC_Z102_bypass --hasProcedureStep--> PROC_Z102_bypass_step_06
PROC_Z102_bypass --source--> REPORT E.3.6 and Fig F.21
PROC_Z102_bypass --hasProcedureStep--> PROC_Z102_bypass_step_01
Z102_bypass --activatedBy--> PROC_Z102_bypass
PROC_Z102_bypass_step_04 --instruction--> Manually close V117b
PROC_Z102_bypass_step_04 --stepOrder--> 4
PROC_Z102_bypass_step_04 --requiredPosition--> closed
PROC_Z102_bypass_step_04 --type--> ProcedureStep
PROC_Z102_bypass_step_04 --operatesOn--> V117b
PROC_Z102_bypass_step_04 --label--> Z102 filter bypass step 4
Route_D_side_bypass_step_11_E100_N_sump_outlet --stepType--> inline
Route_D_side_bypass_step_11_E100_N_sump_outlet --label--> Route D: side return (stage 3), Z102 bypassed step 11: E100_N_sump_outlet
Route_D_side_bypass_step_11_E100_N_sump_outlet --type--> LoopStep
Route_D_side_bypass_step_11_E100_N_sump_outlet --nextStep--> Route_D_side_bypass_step_12_V110
Route_D_side_bypass_step_11_E100_N_sump_outlet --stepItem--> E100_N_sump_outlet
Route_D_side_bypass_step_11_E100_N_sump_outlet --stepIndex--> 11
Route_D_side_bypass_step_10_E100 --nextStep--> Route_D_side_bypass_step_11_E100_N_sump_outlet
Z102__cit01 --type--> Citation
Z102__cit01 --location--> grid M11
Z102__cit01 --document--> SRC_PID
Z102__cit01 --label--> Citation 1 for Z102
Z102__cit01 --citationText--> P&ID grid M11
Route_C_side_filter_step_34_FI104 --label--> Route C: side return (stage 3), through Z102 step 34: FI104
Route_C_side_filter_step_34_FI104 --stepItem--> FI104
Route_C_side_filter_step_34_FI104 --stepIndex--> 34
Route_C_side_filter_step_34_FI104 --stepType--> tie-in
Route_C_side_filter_step_34_FI104 --type--> LoopStep
Route_B_top_bypass_step_20_J100 --label--> Route B: top return (stage 1), Z102 bypassed step 20: J100
Route_B_top_bypass_step_20_J100 --stepType--> inline
Route_B_top_bypass_step_20_J100 --stepIndex--> 20
Route_B_top_bypass_step_20_J100 --type--> LoopStep
Route_B_top_bypass_step_20_J100 --nextStep--> Route_B_top_bypass_step_24_PCV122
Route_B_top_bypass_step_20_J100 --stepItem--> J100
Route_B_top_bypass_step_19_V113b --nextStep--> Route_B_top_bypass_step_20_J100
Route_B_top_bypass --hasStep--> Route_B_top_bypass_step_25_V116
Route_B_top_bypass --hasStep--> Route_B_top_bypass_step_22_B101
Route_B_top_bypass --hasStep--> Route_B_top_bypass_step_15_PT103
Route_B_top_bypass --hasStep--> Route_B_top_bypass_step_07_TI100
Route_B_top_bypass --hasValveSetting--> Route_B_top_bypass_setting_V309
Route_B_top_bypass --hasStep--> Route_B_top_bypass_step_14_TT104
Route_B_top_bypass --hasStep--> Route_B_top_bypass_step_18_V113a
Route_B_top_bypass --hasStep--> Route_B_top_bypass_step_28_FT103
Route_B_top_bypass --hasStep--> Route_B_top_bypass_step_33_H200a
Route_B_top_bypass --hasStep--> Route_B_top_bypass_step_36_V403
Route_B_top_bypass --label--> Route B: top return (stage 1), Z102 bypassed
Route_B_top_bypass --hasStep--> Route_B_top_bypass_step_03_DI100
Route_B_top_bypass --inMode--> StripperRecirculation
Route_B_top_bypass --hasValveSetting--> Route_B_top_bypass_setting_V302
Route_B_top_bypass --hasValveSetting--> Route_B_top_bypass_setting_SDV125
Route_B_top_bypass --hasStep--> Route_B_top_bypass_step_20_J100
Route_B_top_bypass --hasStep--> Route_B_top_bypass_step_02_FI102
Route_B_top_bypass --hasStep--> Route_B_top_bypass_step_38_E100_N_top_inlet
Route_B_top_bypass --hasStep--> Route_B_top_bypass_step_31_FI104
Route_B_top_bypass --hasStep--> Route_B_top_bypass_step_09_E100_N_reboiler_return
Route_B_top_bypass --hasValveSetting--> Route_B_top_bypass_setting_V403
Route_B_top_bypass --hasStep--> Route_B_top_bypass_step_00_E100_N_drawoff
Route_B_top_bypass --hasStep--> Route_B_top_bypass_step_11_E100_N_sump_outlet
Route_B_top_bypass --hasStep--> Route_B_top_bypass_step_19_V113b
Route_B_top_bypass --hasValveSetting--> Route_B_top_bypass_setting_V318
Route_B_top_bypass --type--> RouteScenario
Route_B_top_bypass --hasStep--> Route_B_top_bypass_step_06_TT100
Route_B_top_bypass --returnsToStage--> E100_stage_01
Route_B_top_bypass --hasStep--> Route_B_top_bypass_step_30_FT104
Route_B_top_bypass --hasStep--> Route_B_top_bypass_step_26_V120
Route_B_top_bypass --hasStep--> Route_B_top_bypass_step_10_E100
Route_B_top_bypass --hasStep--> Route_B_top_bypass_step_32_SDV125
Route_B_top_bypass --hasStep--> Route_B_top_bypass_step_05_H100
Route_B_top_bypass --returnPoint--> top (stage 1)
Route_B_top_bypass --usesFilter--> false
Route_B_top_bypass --hasStep--> Route_B_top_bypass_step_16_C100
Route_B_top_bypass --hasValveSetting--> Route_B_top_bypass_setting_V120
Route_B_top_bypass --hasStep--> Route_B_top_bypass_step_27_V121
Route_B_top_bypass --hasStep--> Route_B_top_bypass_step_34_TT213
Route_B_top_bypass --hasStep--> Route_B_top_bypass_step_21_TT106
Route_B_top_bypass --hasStep--> Route_B_top_bypass_step_33_H200b
Route_B_top_bypass --hasValveSetting--> Route_B_top_bypass_setting_V117b
Route_B_top_bypass --hasStep--> Route_B_top_bypass_step_35_TI213
Route_B_top_bypass --hasStep--> Route_B_top_bypass_step_08_Q106
Route_B_top_bypass --hasStep--> Route_B_top_bypass_step_17_TE105
Route_B_top_bypass --hasValveSetting--> Route_B_top_bypass_setting_V117a
Route_B_top_bypass --hasStep--> Route_B_top_bypass_step_29_FI103
Route_B_top_bypass --hasStep--> Route_B_top_bypass_step_01_FT102
Route_B_top_bypass --hasStep--> Route_B_top_bypass_step_13_V112
Route_B_top_bypass --hasStep--> Route_B_top_bypass_step_23_PT104
Route_B_top_bypass --hasStep--> Route_B_top_bypass_step_37_V402
Route_B_top_bypass --hasStep--> Route_B_top_bypass_step_04_Q105
Route_B_top_bypass --hasValveSetting--> Route_B_top_bypass_setting_V402
Route_B_top_bypass --hasValveSetting--> Route_B_top_bypass_setting_SDV123
Route_B_top_bypass --isNormalRoute--> false
Route_B_top_bypass --variantOf--> StrippingLoop
Route_B_top_bypass --hasStep--> Route_B_top_bypass_step_39_E100
Route_B_top_bypass --hasStep--> Route_B_top_bypass_step_24_PCV122
Route_B_top_bypass --hasStep--> Route_B_top_bypass_step_12_V110
Route_B_top_bypass --note--> Used when PDT105 reaches 0.45 bar (Z102 blocked).
Route_B_top_bypass_step_01_FT102 --stepIndex--> 1
Route_B_top_bypass_step_01_FT102 --stepItem--> FT102
Route_B_top_bypass_step_01_FT102 --stepType--> inline
Route_B_top_bypass_step_01_FT102 --label--> Route B: top return (stage 1), Z102 bypassed step 1: FT102
Route_B_top_bypass_step_01_FT102 --type--> LoopStep
Route_B_top_bypass_step_01_FT102 --nextStep--> Route_B_top_bypass_step_04_Q105
Route_B_top_bypass_step_00_E100_N_drawoff --nextStep--> Route_B_top_bypass_step_01_FT102
Route_C_side_filter_step_30_V121 --type--> LoopStep
Route_C_side_filter_step_30_V121 --stepType--> inline
Route_C_side_filter_step_30_V121 --stepItem--> V121
Route_C_side_filter_step_30_V121 --nextStep--> Route_C_side_filter_step_31_FT103
Route_C_side_filter_step_30_V121 --stepIndex--> 30
Route_C_side_filter_step_30_V121 --label--> Route C: side return (stage 3), through Z102 step 30: V121
Route_C_side_filter_step_29_V117b --nextStep--> Route_C_side_filter_step_30_V121
Route_A_top_filter_setting_V302 --label--> V302 in Route A: top return (stage 1), through Z102
Route_A_top_filter_setting_V302 --valve--> V302
Route_A_top_filter_setting_V302 --type--> ValveSetting
Route_A_top_filter_setting_V302 --requiredPosition--> closed
Route_A_top_filter --hasValveSetting--> Route_A_top_filter_setting_V302
Route_B_top_bypass_step_36_V403 --label--> Route B: top return (stage 1), Z102 bypassed step 36: V403
Route_B_top_bypass_step_36_V403 --stepType--> inline
Route_B_top_bypass_step_36_V403 --type--> LoopStep
Route_B_top_bypass_step_36_V403 --stepIndex--> 36
Route_B_top_bypass_step_36_V403 --nextStep--> Route_B_top_bypass_step_37_V402
Route_B_top_bypass_step_36_V403 --stepItem--> V403
Route_B_top_bypass_step_33_H200a --nextStep--> Route_B_top_bypass_step_36_V403
Route_B_top_bypass_step_33_H200b --nextStep--> Route_B_top_bypass_step_36_V403
Route_D_side_bypass_step_38_E100 --stepIndex--> 38
Route_D_side_bypass_step_38_E100 --label--> Route D: side return (stage 3), Z102 bypassed step 38: E100
Route_D_side_bypass_step_38_E100 --stepType--> inline
Route_D_side_bypass_step_38_E100 --stepItem--> E100
Route_D_side_bypass_step_38_E100 --type--> LoopStep
```

Question: What could explain a high differential-pressure reading across Z102, and how does it affect lean MEA circulation?

## Q67

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
K101 --type--> Saturator
K101 --label--> K101 gas saturator
K101 --pipedTo--> SDV170
K101 --pipedTo--> Z103
K101 --floor--> 1
K101 --feedsInto--> E101_N_gas_inlet
K101 --pipedTo--> E101_N_gas_inlet
K101 --note--> Saturates the feed gas with water before E101; temperature held by TIC121 using C106 on the recirculating water. Grid not in the REPORT lists (near L17 to L18 on the P&ID). Not modelled in Aspen (GOI09).
K101 --pipedTo--> V126
K101 --tag--> K101
DI_CARTRIDGE --feedsInto--> K101
HAZOP_4_06 --concerns--> K101
V172 --pipedTo--> K101
J102 --pipedTo--> K101
limit_LZAL_K101 --appliesTo--> K101
HAZOP_4_07 --concerns--> K101
LT104 --monitors--> K101
HAZOP_3_05 --concerns--> K101
FEED_GAS_HEADER --feedsInto--> K101
GOI09 --about--> K101
LI106 --monitors--> K101
FEED_GAS_HEADER --pipedTo--> K101
limit_LAL_K101 --appliesTo--> K101
K101_N2_recycle --fromItem--> K101
limit_LZAH_K101 --appliesTo--> K101
GOI07 --about--> K101
GOI02 --about--> K101
HAZOP_element_3 --covers--> K101
HAZOP_4_02 --concerns--> K101
TI121 --monitors--> K101
C106 --pipedTo--> K101
K103_CO2_recycle --bypasses--> K101
TT121 --monitors--> K101
DI_CARTRIDGE --pipedTo--> K101
J102 --feedsInto--> K101
V172 --feedsInto--> K101
J104 --pipedTo--> RV102
J104 --note--> Recirculates water over K101 (HAZOP element 4). A filter was added on its inlet (HAZOP 4.3).
J104 --label--> J104 K101 water recirculation pump
J104 --floor--> 1
J104 --gridReference--> O18
J104 --tag--> J104
J104 --type--> Pump
J104 --pipedTo--> C106
HAZOP_element_4 --covers--> J104
RV102 --protects--> J104
HAZOP_3_07 --concerns--> J104
FT110 --monitors--> J104
GOI07 --about--> J104
Z103 --pipedTo--> J104
N2ReturnLoop --hasStep--> N2ReturnLoop_step_00_E101
N2ReturnLoop --hasStep--> N2ReturnLoop_step_02_K402
N2ReturnLoop --hasStep--> N2ReturnLoop_step_15_E101_N_gas_inlet
N2ReturnLoop --inMode--> FigureOfEight
N2ReturnLoop --hasStep--> N2ReturnLoop_step_01_E101_N_gas_outlet
N2ReturnLoop --hasStep--> N2ReturnLoop_step_05_FT303
N2ReturnLoop --hasStep--> N2ReturnLoop_step_16_E101
N2ReturnLoop --hasStep--> N2ReturnLoop_step_13_FT107
N2ReturnLoop --hasStep--> N2ReturnLoop_step_07_FT304
N2ReturnLoop --note--> N2 is not absorbed, so it is recirculated: J102 blows it from the K402 overhead back through K101 into E101. Fresh N2 and CO2 (piece 5) top it up. FCV111 recycles part of it from K101 back to K102 to set the N2 flow into E101.
N2ReturnLoop --hasStep--> N2ReturnLoop_step_03_K402_N_gas_to_return
N2ReturnLoop --hasStep--> N2ReturnLoop_step_10_V187
N2ReturnLoop --hasStep--> N2ReturnLoop_step_04_TT304
N2ReturnLoop --label--> N2 return loop (E101 > K402 > K102 > J102 > K101 > E101)
N2ReturnLoop --hasStep--> N2ReturnLoop_step_12_TT114
N2ReturnLoop --hasStep--> N2ReturnLoop_step_08_FI304
N2ReturnLoop --hasStep--> N2ReturnLoop_step_14_K101
N2ReturnLoop --hasStep--> N2ReturnLoop_step_06_FI303
N2ReturnLoop --hasStep--> N2ReturnLoop_step_09_K102
N2ReturnLoop --type--> Loop
N2ReturnLoop --hasStep--> N2ReturnLoop_step_11_J102
FCV111 --floor--> 1
FCV111 --valveType--> flow control
FCV111 --tag--> FCV111
FCV111 --pipedTo--> K102
FCV111 --label--> FCV111
FCV111 --gridReference--> K17
FCV111 --type--> FlowControlValve
FCV111 --normalPosition--> open
FCV111 --note--> Recycles N2 from K101 back to K102, reducing the recycled N2 entering E101 (REPORT D.4, Fig D.6/D.7). Controlled by FIC303/FIC304 from FT303/FT304 on the N2 recycle pipe.
FIC304 --controls--> FCV111
K101_N2_recycle --routeVia--> FCV111
SDV170 --pipedTo--> FCV111
CL_N2_to_E101 --hasFinalElement--> FCV111
FIC303 --controls--> FCV111
N2ReturnLoop_step_11_J102 --label--> N2 return loop (E101 > K402 > K102 > J102 > K101 > E101) step 11: J102
N2ReturnLoop_step_11_J102 --stepItem--> J102
N2ReturnLoop_step_11_J102 --stepIndex--> 11
N2ReturnLoop_step_11_J102 --type--> LoopStep
N2ReturnLoop_step_11_J102 --stepType--> inline
NRV100b --type--> CheckValve
NRV100b --gridReference--> Q19
NRV100b --note--> Bottom right (make-up water to K101?). FI03
NRV100b --feedsInto--> DI_CARTRIDGE
NRV100b --pipedTo--> DI_CARTRIDGE
NRV100b --valveType--> check
NRV100b --label--> NRV100b
NRV100b --tag--> NRV100b
NRV100b --floor--> 1
NRV100a --feedsInto--> NRV100b
NRV100a --pipedTo--> NRV100b
N2ReturnLoop_step_04_TT304 --stepType--> tie-in
N2ReturnLoop_step_04_TT304 --type--> LoopStep
N2ReturnLoop_step_04_TT304 --label--> N2 return loop (E101 > K402 > K102 > J102 > K101 > E101) step 4: TT304
N2ReturnLoop_step_04_TT304 --stepIndex--> 4
N2ReturnLoop_step_04_TT304 --stepItem--> TT304
TT107 --label--> TT107
TT107 --signalType--> Fieldbus
TT107 --sensorType--> PRT
TT107 --floor--> 1
TT107 --measuredVariable--> gas entering E101 (after K101)
TT107 --monitors--> E101
TT107 --type--> TemperatureInstrument
TT107 --gridReference--> K18
TT107 --tag--> TT107
HAZOP_10_03 --label--> HAZOP 10.3
HAZOP_10_03 --consequence--> Overpressure lower section of E101 and K101
HAZOP_10_03 --actionTaken--> RV added
HAZOP_10_03 --itemNumber--> 3
HAZOP_10_03 --inElement--> HAZOP_element_10
HAZOP_10_03 --parameter--> FLOW
HAZOP_10_03 --cause--> High rate of gas up column from CO2 and N2 feed system
HAZOP_10_03 --type--> HazopDeviation
HAZOP_10_03 --concerns--> E101
HAZOP_10_03 --recommendedAction--> RV at outlet to K101?
HAZOP_10_03 --guideword--> MORE
N2ReturnLoop_step_05_FT303 --stepItem--> FT303
N2ReturnLoop_step_05_FT303 --type--> LoopStep
N2ReturnLoop_step_05_FT303 --stepType--> inline
N2ReturnLoop_step_05_FT303 --label--> N2 return loop (E101 > K402 > K102 > J102 > K101 > E101) step 5: FT303
N2ReturnLoop_step_05_FT303 --stepIndex--> 5
HAZOP_4_06 --cause--> As K101
HAZOP_4_06 --parameter--> TEMP.
HAZOP_4_06 --label--> HAZOP 4.6
HAZOP_4_06 --itemNumber--> 6
HAZOP_4_06 --type--> HazopDeviation
HAZOP_4_06 --inElement--> HAZOP_element_4
HAZOP_4_06 --guideword--> HIGHER
N2ReturnLoop_step_10_V187 --stepItem--> V187
N2ReturnLoop_step_10_V187 --stepType--> branch
N2ReturnLoop_step_10_V187 --label--> N2 return loop (E101 > K402 > K102 > J102 > K101 > E101) step 10: V187
N2ReturnLoop_step_10_V187 --stepIndex--> 10
N2ReturnLoop_step_10_V187 --type--> LoopStep
GOI09 --foundBy--> gas section build, Oct 2026
GOI09 --itemStatus--> open
GOI09 --label--> GOI09: Aspen feeds the gas straight into E101 with no K101 saturator
GOI09 --description--> Aspen feeds the gas straight into E101 with no K101 saturator
GOI09 --resolvedBy--> Note for model comparison
GOI09 --type--> OpenItem
limit_LZAH_K101 --type--> OperatingLimit
```

Question: If J104 stops circulating water around K101, what happens to the gas feed preparation?

## Q68

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
FCV105 --floor--> 1
FCV105 --label--> FCV105
FCV105 --tag--> FCV105
FCV105 --feedsInto--> NRV101
FCV105 --note--> CO2 mass flow controller (FIC105); the 2010 HAZOP calls it FCV106.
FCV105 --pipedTo--> NRV101
FCV105 --normalPosition--> open
FCV105 --type--> FlowControlValve
FCV105 --gridReference--> K21
FCV105 --valveType--> flow control (mass flow controller)
CL_CO2_feed --hasFinalElement--> FCV105
FT105 --monitors--> FCV105
FIC105 --controls--> FCV105
GOI04 --about--> FCV105
GOI01 --about--> FCV105
FT105 --feedsInto--> FCV105
HAZOP_1_06 --concerns--> FCV105
FT105 --pipedTo--> FCV105
HAZOP_element_1 --covers--> FCV105
HAZOP_1_03 --concerns--> FCV105
HAZOP_element_1 --covers--> NRV101
HAZOP_element_1 --elementNumber--> 1
HAZOP_element_1 --covers--> V128
HAZOP_element_1 --covers--> RV103
HAZOP_element_1 --source--> HAZOP study, 6-7 May 2010 (27794_Plant_HAZREP_1.xls)
HAZOP_element_1 --label--> HAZOP element 1: CO2 FEED (V128 to tee)
HAZOP_element_1 --type--> HazopElement
HAZOP_element_1 --covers--> PCV116
HAZOP_1_04 --inElement--> HAZOP_element_1
HAZOP_1_01 --inElement--> HAZOP_element_1
HAZOP_1_05 --inElement--> HAZOP_element_1
HAZOP_1_06 --inElement--> HAZOP_element_1
HAZOP_1_07 --inElement--> HAZOP_element_1
HAZOP_1_08 --inElement--> HAZOP_element_1
HAZOP_1_03 --inElement--> HAZOP_element_1
HAZOP_1_11 --inElement--> HAZOP_element_1
HAZOP_1_02 --inElement--> HAZOP_element_1
CL_CO2_feed --label--> CO2 feed rate (CO2 concentration into the plant)
CL_CO2_feed --type--> ControlLoop
CL_CO2_feed --manipulatedVariable--> FCV105 opening
CL_CO2_feed --hasController--> FIC105
CL_CO2_feed --hasSensor--> FT105
CL_CO2_feed --controlledVariable--> CO2 feed rate
HAZOP_1_03 --type--> HazopDeviation
HAZOP_1_03 --safeguard--> Detectable by analysis
HAZOP_1_03 --guideword--> MORE
HAZOP_1_03 --itemNumber--> 3
HAZOP_1_03 --consequence--> Wrong composition in plant
HAZOP_1_03 --label--> HAZOP 1.3
HAZOP_1_03 --cause--> FCV 106 (now FCV105) jammed open
HAZOP_1_03 --parameter--> FLOW
HAZOP_1_06 --consequence--> CO2 liquifying / solidifying
HAZOP_1_06 --cause--> Excess flow
HAZOP_1_06 --label--> HAZOP 1.6
HAZOP_1_06 --itemNumber--> 6
HAZOP_1_06 --type--> HazopDeviation
HAZOP_1_06 --guideword--> LOWER
HAZOP_1_06 --parameter--> TEMP.
HAZOP_1_06 --recommendedAction--> Consider min operating safe temp of FCV106 (now FCV105)
HAZOP_1_06 --actionTaken--> Action completed
HAZOP_1_06 --safeguard--> none
FCV105__gascit04 --citationText--> HAZOP 2010 element 1, items 3 and 6 ('FCV 106 (now FCV105)')
FCV105__gascit04 --document--> SRC_HAZOP
FCV105__gascit04 --type--> Citation
FCV105__gascit04 --location--> element 1, items 3 and 6 ('FCV 106 (now FCV105)')
FCV105__gascit04 --label--> Citation 4 for FCV105 (gas)
FT105 --label--> FT105
FT105 --sensorType--> thermal mass flow meter
FT105 --tag--> FT105
FT105 --gridReference--> K21
FT105 --floor--> 1
FT105 --measuredVariable--> CO2 feed mass flow
FT105 --type--> FlowInstrument
FT105 --signalType--> 4-20mA
PCV116 --pipedTo--> FT105
PCV116 --feedsInto--> FT105
FIC105 --tag--> FIC105
FIC105 --type--> Controller
FIC105 --label--> CO2 feed flow controller (sets the CO2 concentration into the plant)
FCV105__gascit03 --label--> Citation 3 for FCV105 (gas)
FCV105__gascit03 --type--> Citation
FCV105__gascit03 --citationText--> Plant summary 2023-24 p.190 (FCV105 / FT105 / FIC105)
FCV105__gascit03 --location--> p.190 (FCV105 / FT105 / FIC105)
FCV105__gascit03 --document--> SRC_SUMMARY
GOI04 --description--> Tag renumbering since 2010: HAZOP FCV106 = FCV105 (CO2) and FCV107 = FCV106 (N2), but the SUMMARY uses FCV116/FIC116 for N2 and FIC106 for C106 cooling water
GOI04 --type--> OpenItem
GOI04 --label--> GOI04: Tag renumbering since 2010: HAZOP FCV106 = FCV105 (CO2) and FCV107 = FCV106 (N2), but the SUMMARY uses FCV116/FIC116 for N2 and FIC106 for C106 cooling water
GOI04 --resolvedBy--> Instrument index or site check
GOI04 --itemStatus--> open
GOI04 --foundBy--> gas section build, Oct 2026
GOI04 --about--> FCV116
GasFeedRoute_step_04_FCV105 --type--> LoopStep
GasFeedRoute_step_04_FCV105 --label--> Feed gas route (CO2 and N2 supplies to E101) step 4: FCV105
GasFeedRoute_step_04_FCV105 --stepItem--> FCV105
GasFeedRoute_step_04_FCV105 --stepIndex--> 4
GasFeedRoute_step_04_FCV105 --stepType--> inline
FCV105__gascit02 --document--> SRC_REPORT
FCV105__gascit02 --citationText--> Pilot Plant Report valve lists (FCV105, K21, floor 1)
FCV105__gascit02 --location--> valve lists (FCV105, K21, floor 1)
FCV105__gascit02 --type--> Citation
FCV105__gascit02 --label--> Citation 2 for FCV105 (gas)
FCV105__gascit01 --label--> Citation 1 for FCV105 (gas)
FCV105__gascit01 --location--> grid K21
FCV105__gascit01 --citationText--> P&ID grid K21
FCV105__gascit01 --document--> SRC_PID
FCV105__gascit01 --type--> Citation
GOI01 --about--> FCV116
GOI01 --type--> OpenItem
GOI01 --resolvedBy--> Trace on the P&ID
GOI01 --description--> Order of items on each supply line (regulator, flow meter, mass flow controller, non-return valve)
GOI01 --foundBy--> gas section build, Oct 2026
GOI01 --label--> GOI01: Order of items on each supply line (regulator, flow meter, mass flow controller, non-return valve)
GOI01 --itemStatus--> open
NRV101 --pipedTo--> FEED_GAS_HEADER
NRV101 --feedsInto--> FEED_GAS_HEADER
PCV116 --pipedTo--> RV103
V128 --feedsInto--> PCV116
V128 --pipedTo--> PCV116
FEED_GAS_HEADER --feedsInto--> K101
FEED_GAS_HEADER --pipedTo--> K101
NRV102 --pipedTo--> FEED_GAS_HEADER
NRV102 --feedsInto--> FEED_GAS_HEADER
```

Question: What would happen if FCV105 became stuck open during CO2 feed operation?

## Q69

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
aspen_v3_block_E100 --label--> E100 (ABB_pilot_plant_final_3)
aspen_v3_block_E100 --represents--> E100
aspen_v3_block_E100 --aspenModel--> RADFRAC
aspen_v3_block_E100 --inCase--> case_aspen_v3
aspen_v3_block_E100 --status--> WARNING
aspen_v3_block_E100 --statusMessage--> FEED PRESSURE IS LOWER THAN STAGE PRESSURE.
aspen_v3_block_E100 --type--> AspenBlock
aspen_v3_block_E100 --blockId--> E100
aspen_v3_stream_S13 --fromBlock--> aspen_v3_block_E100
aspen_v3_stream_S10 --toBlock--> aspen_v3_block_E100
aspen_v3_stream_S6 --fromBlock--> aspen_v3_block_E100
aspen_v3_stream_S14 --fromBlock--> aspen_v3_block_E100
aspen_v3_stream_S24 --toBlock--> aspen_v3_block_E100
aspen_v6_1_block_E100 --inCase--> case_aspen_v6_1
aspen_v6_1_block_E100 --statusMessage--> RATESEP CALCULATIONS FAILED TO CONVERGE.
aspen_v6_1_block_E100 --status--> ERROR
aspen_v6_1_block_E100 --represents--> E100
aspen_v6_1_block_E100 --label--> E100 (ABB_pilot_plant_final_6_1_SA_validation)
aspen_v6_1_block_E100 --type--> AspenBlock
aspen_v6_1_block_E100 --blockId--> E100
aspen_v6_1_block_E100 --aspenModel--> RADFRAC
aspen_v6_1_stream_S15 --fromBlock--> aspen_v6_1_block_E100
aspen_v6_1_stream_S23 --fromBlock--> aspen_v6_1_block_E100
aspen_v6_1_stream_S10 --toBlock--> aspen_v6_1_block_E100
aspen_v6_1_stream_S12 --fromBlock--> aspen_v6_1_block_E100
aspen_v6_1_stream_S14 --toBlock--> aspen_v6_1_block_E100
E100 --floor--> 1
E100 --hasStage--> E100_stage_12
E100 --diameter_mm--> 264.62
E100 --tag--> E100
E100 --label--> E100 stripper (desorber)
E100 --hasStage--> E100_stage_08
E100 --hasStage--> E100_stage_01
E100 --hasStage--> E100_stage_04
E100 --feedsInto--> E100_N_overhead
E100 --hasStage--> E100_stage_07
E100 --pipedTo--> E100_N_overhead
E100 --note--> Chimney tray below the bottom packed bed separates the draw-off section (stage 11) from the sump (stage 12).
E100 --hasStage--> E100_stage_02
E100 --hasStage--> E100_stage_09
E100 --feedsInto--> E100_N_sump_outlet
E100 --hasStage--> E100_stage_06
E100 --feedsInto--> E100_N_drawoff
E100 --pipedTo--> E100_N_sump_outlet
E100 --hasStage--> E100_stage_05
E100 --hasStage--> E100_stage_11
E100 --hasStage--> E100_stage_10
E100 --designBasis--> Designed for sub-atmospheric pressure (vacuum), per HAZOP element 11 item 10. Design pressure value not documented.
E100 --hasStage--> E100_stage_03
E100 --pipedTo--> E100_N_drawoff
E100 --type--> StrippingColumn
TT200 --monitors--> E100
PI401 --monitors--> E100
TT401 --monitors--> E100
PROC_reboiler_heating_step_06 --operatesOn--> E100
HAZOP_13_13 --concerns--> E100
HAZOP_11_13 --concerns--> E100
LT101 --monitors--> E100
E100_N_sump_outlet --onEquipment--> E100
LSLL102 --monitors--> E100
HAZOP_11_12 --concerns--> E100
OI06 --about--> E100
LSHH100 --monitors--> E100
aspen_v6_1_E100_performance --ofEquipment--> E100
E100_N_overhead --onEquipment--> E100
TT302 --monitors--> E100
HAZOP_7_10 --concerns--> E100
HAZOP_6_07 --concerns--> E100
HAZOP_11_15 --concerns--> E100
E100_N_top_inlet --feedsInto--> E100
PT402 --monitors--> E100
PT401 --monitors--> E100
E100_N_drawoff --onEquipment--> E100
E100_N_side_inlet --onEquipment--> E100
limit_LT101_operating_window --appliesTo--> E100
limit_LZAH100 --appliesTo--> E100
HAZOP_9b_05 --concerns--> E100
RV401 --protects--> E100
E100_N_top_inlet --pipedTo--> E100
E100_N_top_inlet --onEquipment--> E100
HAZOP_13_12 --concerns--> E100
aspen_v3_E100_performance --ofEquipment--> E100
TT301 --monitors--> E100
TT400 --monitors--> E100
HAZOP_7_15 --concerns--> E100
HAZOP_element_11 --covers--> E100
limit_LT101_low_alarm --appliesTo--> E100
TT303 --monitors--> E100
OI11 --about--> E100
limit_PSHH116_set --appliesTo--> E100
HAZOP_13_11 --concerns--> E100
E100_N_reboiler_return --feedsInto--> E100
limit_PSHH400_set --appliesTo--> E100
OI03 --about--> E100
TT103 --monitors--> E100
PSHH400 --monitors--> E100
E100_N_reboiler_return --pipedTo--> E100
HAZOP_8_01 --concerns--> E100
PT102 --monitors--> E100
PSHH116 --monitors--> E100
TT203 --monitors--> E100
limit_LZAL102 --appliesTo--> E100
TT201 --monitors--> E100
HAZOP_6_08 --concerns--> E100
TT300 --monitors--> E100
HAZOP_11_01 --concerns--> E100
E100_N_reboiler_return --onEquipment--> E100
TT202 --monitors--> E100
LSHH100 --tag--> LSHH100
LSHH100 --note--> Stage mapping inferred: odd Aspen stages are the gaps between packed beds where the side instruments sit; floors match REPORT.
LSHH100 --locatedAtStage--> E100_stage_12
LSHH100 --type--> LevelInstrument
LSHH100 --measuredVariable--> level high-high switch
LSHH100 --floor--> 1
LSHH100 --label--> LSHH100
IL_E100_level_HH --initiatedBy--> LSHH100
PT402 --tag--> PT402
PT402 --monitors--> K401
PT402 --measuredVariable--> pressure after K401
PT402 --gridReference--> C16
PT402 --type--> PressureInstrument
PT402 --signalType--> Fieldbus
PT402 --floor--> 4
PT402 --sensorType--> gauge pressure transmitter
PT402 --label--> PT402
HAZOP_12_02 --concerns--> PT402
HAZOP_element_12 --covers--> PT402
CL_E100_pressure --hasSensor--> PT402
NRV106 --tag--> NRV106
NRV106 --valveType--> check
NRV106 --floor--> 1
NRV106 --note--> Near V112 at the E100 sump outlet. FI07
NRV106 --type--> CheckValve
NRV106 --label--> NRV106
NRV106 --gridReference--> M8
Route_D_side_bypass_step_38_E100 --stepIndex--> 38
Route_D_side_bypass_step_38_E100 --label--> Route D: side return (stage 3), Z102 bypassed step 38: E100
Route_D_side_bypass_step_38_E100 --stepType--> inline
Route_D_side_bypass_step_38_E100 --stepItem--> E100
Route_D_side_bypass_step_38_E100 --type--> LoopStep
Route_D_side_bypass_step_37_E100_N_side_inlet --nextStep--> Route_D_side_bypass_step_38_E100
Route_B_top_bypass_step_10_E100 --nextStep--> Route_B_top_bypass_step_11_E100_N_sump_outlet
Route_B_top_bypass_step_10_E100 --stepItem--> E100
Route_B_top_bypass_step_10_E100 --stepIndex--> 10
Route_B_top_bypass_step_10_E100 --stepType--> inline
Route_B_top_bypass_step_10_E100 --type--> LoopStep
Route_B_top_bypass_step_10_E100 --label--> Route B: top return (stage 1), Z102 bypassed step 10: E100
Route_B_top_bypass_step_09_E100_N_reboiler_return --nextStep--> Route_B_top_bypass_step_10_E100
aspen_v3_stream_S10 --temperature_C--> 89.99877
aspen_v3_stream_S10 --phase--> MIXED
```

Question: Pressure in E100 is approaching the high-pressure shutdown condition. What protects the stripper and what should the operator do?

## Q70

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
aspen_v3_block_E101 --type--> AspenBlock
aspen_v3_block_E101 --aspenModel--> RADFRAC
aspen_v3_block_E101 --blockId--> E101
aspen_v3_block_E101 --status--> OK
aspen_v3_block_E101 --label--> E101 (ABB_pilot_plant_final_3)
aspen_v3_block_E101 --inCase--> case_aspen_v3
aspen_v3_stream_S8 --fromBlock--> aspen_v3_block_E101
aspen_v3_stream_1 --toBlock--> aspen_v3_block_E101
aspen_v3_stream_2 --toBlock--> aspen_v3_block_E101
aspen_v3_stream_4 --fromBlock--> aspen_v3_block_E101
aspen_v6_1_block_E101 --type--> AspenBlock
aspen_v6_1_block_E101 --aspenModel--> RADFRAC
aspen_v6_1_block_E101 --label--> E101 (ABB_pilot_plant_final_6_1_SA_validation)
aspen_v6_1_block_E101 --blockId--> E101
aspen_v6_1_block_E101 --status--> OK
aspen_v6_1_block_E101 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S8 --fromBlock--> aspen_v6_1_block_E101
aspen_v6_1_stream_2 --toBlock--> aspen_v6_1_block_E101
aspen_v6_1_stream_1 --toBlock--> aspen_v6_1_block_E101
aspen_v6_1_stream_4 --fromBlock--> aspen_v6_1_block_E101
E101 --pipedTo--> RV400
E101 --floor--> 1
E101 --note--> Lean MEA enters at the top through NRV400; rich MEA leaves from the sump to J101a/b. The air admittance valve shown on the P&ID has been removed from the plant (DIFF, E14/15).
E101 --feedsInto--> E101_N_sump_outlet
E101 --designBasis--> Packing and column designed for 2.3-2.5 bar operation on MEA and 50 kg/h CO2 (HAZOP 10.4)
E101 --feedsInto--> E101_N_gas_outlet
E101 --pipedTo--> E101_N_sump_outlet
E101 --pipedTo--> E101_N_gas_outlet
E101 --type--> AbsorptionColumn
E101 --diameter_mm--> 230.0
E101 --tag--> E101
E101 --label--> E101 absorber
HAZOP_7_10 --concerns--> E101
TT305 --monitors--> E101
PT111 --monitors--> E101
E101_sample_5 --onColumn--> E101
E101_N_gas_outlet --onEquipment--> E101
LSLL109 --monitors--> E101
TT207 --monitors--> E101
PT403 --monitors--> E101
LI108 --monitors--> E101
E101_sample_4 --onColumn--> E101
E101_N_sump_outlet --onEquipment--> E101
FT109 --monitors--> E101
E101_sample_3 --onColumn--> E101
HAZOP_9b_05 --concerns--> E101
limit_LZAL109 --appliesTo--> E101
DI108 --monitors--> E101
E101_N_gas_inlet --feedsInto--> E101
FT304 --monitors--> E101
LT108 --monitors--> E101
K101_N2_recycle --bypasses--> E101
PT110 --monitors--> E101
E101_N_gas_inlet --pipedTo--> E101
HAZOP_5_08 --concerns--> E101
HAZOP_8_01 --concerns--> E101
HAZOP_8_06 --concerns--> E101
PI403 --monitors--> E101
AT400 --monitors--> E101
FT303 --monitors--> E101
TT205 --monitors--> E101
E101_N_base_inlet --onEquipment--> E101
aspen_v6_1_E101_performance --ofEquipment--> E101
TT206 --monitors--> E101
HAZOP_8_03 --concerns--> E101
E101_N_gas_inlet --onEquipment--> E101
E101_N_top_inlet --feedsInto--> E101
E101_sample_6 --onColumn--> E101
K402 --pipedTo--> E101
HAZOP_5_07 --concerns--> E101
AI300 --monitors--> E101
FI109 --monitors--> E101
FI108 --monitors--> E101
aspen_v3_vent_gas --ofEquipment--> E101
AT300 --monitors--> E101
E101_N_top_inlet --pipedTo--> E101
aspen_v6_1_feed_gas --ofEquipment--> E101
limit_PSHH117_set --appliesTo--> E101
TT109 --monitors--> E101
TT412 --monitors--> E101
HAZOP_10_03 --concerns--> E101
LSHH107 --monitors--> E101
E101_sample_2 --onColumn--> E101
limit_LZAH107 --appliesTo--> E101
HAZOP_5_06 --concerns--> E101
PSHH117 --monitors--> E101
TT413 --monitors--> E101
HAZOP_7_13 --concerns--> E101
TT107 --monitors--> E101
TT306 --monitors--> E101
E101_N_top_inlet --onEquipment--> E101
E101_sample_1 --onColumn--> E101
AOI10 --about--> E101
RV400 --protects--> E101
FT108 --monitors--> E101
TT411 --monitors--> E101
TT204 --monitors--> E101
aspen_v3_feed_gas --ofEquipment--> E101
HAZOP_element_10 --covers--> E101
HAZOP_8_11 --concerns--> E101
TT307 --monitors--> E101
TT308 --monitors--> E101
HAZOP_8_02 --concerns--> E101
aspen_v3_E101_performance --ofEquipment--> E101
PCV300 --valveType--> pressure control
PCV300 --floor--> 3
PCV300 --normalPosition--> open
PCV300 --note--> Vents lean gas from the absorber to hold the E101 pressure (PIC403). Opened in the vent stream start-up (Fig F.3), closed at shutdown.
PCV300 --pipedTo--> VENT_E101
PCV300 --label--> PCV300
PCV300 --feedsInto--> VENT_E101
PCV300 --type--> PressureControlValve
PCV300 --tag--> PCV300
PCV300 --gridReference--> G18
K402 --feedsInto--> PCV300
CL_E101_pressure --hasFinalElement--> PCV300
K402 --pipedTo--> PCV300
PIC403 --controls--> PCV300
AV01 --about--> PCV300
K101 --type--> Saturator
K101 --label--> K101 gas saturator
K101 --pipedTo--> SDV170
K101 --pipedTo--> Z103
K101 --floor--> 1
K101 --feedsInto--> E101_N_gas_inlet
K101 --pipedTo--> E101_N_gas_inlet
K101 --note--> Saturates the feed gas with water before E101; temperature held by TIC121 using C106 on the recirculating water. Grid not in the REPORT lists (near L17 to L18 on the P&ID). Not modelled in Aspen (GOI09).
K101 --pipedTo--> V126
K101 --tag--> K101
DI_CARTRIDGE --feedsInto--> K101
HAZOP_4_06 --concerns--> K101
V172 --pipedTo--> K101
J102 --pipedTo--> K101
limit_LZAL_K101 --appliesTo--> K101
HAZOP_4_07 --concerns--> K101
LT104 --monitors--> K101
HAZOP_3_05 --concerns--> K101
FEED_GAS_HEADER --feedsInto--> K101
GOI09 --about--> K101
LI106 --monitors--> K101
FEED_GAS_HEADER --pipedTo--> K101
limit_LAL_K101 --appliesTo--> K101
K101_N2_recycle --fromItem--> K101
limit_LZAH_K101 --appliesTo--> K101
GOI07 --about--> K101
GOI02 --about--> K101
HAZOP_element_3 --covers--> K101
HAZOP_4_02 --concerns--> K101
TI121 --monitors--> K101
C106 --pipedTo--> K101
```

Question: The pressure in E101 is rising above its normal controlled value. Which safeguards apply and what actions are required?

## Q71

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
LT101 --gridReference--> K8
LT101 --signalType--> Profibus-PA
LT101 --locatedAtStage--> E100_stage_12
LT101 --monitors--> E100
LT101 --note--> Stage mapping inferred: odd Aspen stages are the gaps between packed beds where the side instruments sit; floors match REPORT.
LT101 --sensorType--> differential pressure transmitter
LT101 --type--> LevelInstrument
LT101 --floor--> 1
LT101 --label--> LT101
LT101 --tag--> LT101
LT101 --measuredVariable--> level
IL_E100_level_LL --initiatedBy--> LT101
PROC_pump_start_order_step_03 --type--> ProcedureStep
PROC_pump_start_order_step_03 --operatesOn--> J101a
PROC_pump_start_order_step_03 --instruction--> If LT101 >= LT108, start J101a/b before J100
PROC_pump_start_order_step_03 --stepOrder--> 3
PROC_pump_start_order_step_03 --label--> Order of starting J100 and J101a/b step 3
PROC_pump_start_order --hasProcedureStep--> PROC_pump_start_order_step_03
PROC_pump_start_order_step_01 --operatesOn--> LT108
PROC_pump_start_order_step_01 --stepOrder--> 1
PROC_pump_start_order_step_01 --type--> ProcedureStep
PROC_pump_start_order_step_01 --instruction--> Compare LT101 (E100) and LT108 (E101)
PROC_pump_start_order_step_01 --label--> Order of starting J100 and J101a/b step 1
PROC_pump_start_order --hasProcedureStep--> PROC_pump_start_order_step_01
LT101__cit01 --document--> SRC_PID
LT101__cit01 --location--> grid K8, E100 sump, left-hand side
LT101__cit01 --citationText--> P&ID grid K8, E100 sump, left-hand side
LT101__cit01 --label--> Citation 1 for LT101
LT101__cit01 --type--> Citation
IL_E100_level_LL --tripsItem--> J100
IL_E100_level_LL --label--> E100 low-low level shutdown (protects J100)
IL_E100_level_LL --initiatedBy--> LSLL102
IL_E100_level_LL --type--> Interlock
PROC_pump_start_order_step_02 --type--> ProcedureStep
PROC_pump_start_order_step_02 --instruction--> If LT101 < LT108, start J100 before J101a/b to avoid overfilling
PROC_pump_start_order_step_02 --label--> Order of starting J100 and J101a/b step 2
PROC_pump_start_order_step_02 --stepOrder--> 2
PROC_pump_start_order_step_02 --operatesOn--> J101a
PROC_pump_start_order --hasProcedureStep--> PROC_pump_start_order_step_02
limit_LT101_operating_window --lowValue--> 10.0
limit_LT101_operating_window --limitType--> range
limit_LT101_operating_window --label--> LT101_operating_window
limit_LT101_operating_window --unit--> %
limit_LT101_operating_window --appliesTo--> E100
limit_LT101_operating_window --highValue--> 90.0
limit_LT101_operating_window --note--> Keep LT101 between 10 % and 90 % during the stripping loop test.
limit_LT101_operating_window --type--> OperatingLimit
limit_LT101_operating_window --variable--> level
limit_LT101_operating_window --valueVerified--> true
limit_LT101_operating_window --source--> REPORT E.3.7, E.3.8
LT101__cit03 --document--> SRC_TEAM
LT101__cit03 --label--> Citation 3 for LT101
LT101__cit03 --location--> left-hand side of E100 sump
LT101__cit03 --citationText--> Team check left-hand side of E100 sump
LT101__cit03 --type--> Citation
LT101__cit02 --location--> Appendix B instrument list
LT101__cit02 --document--> SRC_REPORT
LT101__cit02 --label--> Citation 2 for LT101
LT101__cit02 --type--> Citation
LT101__cit02 --citationText--> Pilot Plant Report Appendix B instrument list
```

Question: LT101 falls below 5% during full plant operation. What is the required response, and what happens if it falls below 1%?

## Q72

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
LT101 --gridReference--> K8
LT101 --signalType--> Profibus-PA
LT101 --locatedAtStage--> E100_stage_12
LT101 --monitors--> E100
LT101 --note--> Stage mapping inferred: odd Aspen stages are the gaps between packed beds where the side instruments sit; floors match REPORT.
LT101 --sensorType--> differential pressure transmitter
LT101 --type--> LevelInstrument
LT101 --floor--> 1
LT101 --label--> LT101
LT101 --tag--> LT101
LT101 --measuredVariable--> level
IL_E100_level_LL --initiatedBy--> LT101
PROC_pump_start_order_step_03 --type--> ProcedureStep
PROC_pump_start_order_step_03 --operatesOn--> J101a
PROC_pump_start_order_step_03 --instruction--> If LT101 >= LT108, start J101a/b before J100
PROC_pump_start_order_step_03 --stepOrder--> 3
PROC_pump_start_order_step_03 --label--> Order of starting J100 and J101a/b step 3
PROC_pump_start_order --hasProcedureStep--> PROC_pump_start_order_step_03
PROC_pump_start_order_step_01 --operatesOn--> LT108
PROC_pump_start_order_step_01 --stepOrder--> 1
PROC_pump_start_order_step_01 --type--> ProcedureStep
PROC_pump_start_order_step_01 --instruction--> Compare LT101 (E100) and LT108 (E101)
PROC_pump_start_order_step_01 --label--> Order of starting J100 and J101a/b step 1
PROC_pump_start_order --hasProcedureStep--> PROC_pump_start_order_step_01
LT101__cit01 --document--> SRC_PID
LT101__cit01 --location--> grid K8, E100 sump, left-hand side
LT101__cit01 --citationText--> P&ID grid K8, E100 sump, left-hand side
LT101__cit01 --label--> Citation 1 for LT101
LT101__cit01 --type--> Citation
IL_E100_level_LL --tripsItem--> J100
IL_E100_level_LL --label--> E100 low-low level shutdown (protects J100)
IL_E100_level_LL --initiatedBy--> LSLL102
IL_E100_level_LL --type--> Interlock
PROC_pump_start_order_step_02 --type--> ProcedureStep
PROC_pump_start_order_step_02 --instruction--> If LT101 < LT108, start J100 before J101a/b to avoid overfilling
PROC_pump_start_order_step_02 --label--> Order of starting J100 and J101a/b step 2
PROC_pump_start_order_step_02 --stepOrder--> 2
PROC_pump_start_order_step_02 --operatesOn--> J101a
PROC_pump_start_order --hasProcedureStep--> PROC_pump_start_order_step_02
limit_LT101_operating_window --lowValue--> 10.0
limit_LT101_operating_window --limitType--> range
limit_LT101_operating_window --label--> LT101_operating_window
limit_LT101_operating_window --unit--> %
limit_LT101_operating_window --appliesTo--> E100
limit_LT101_operating_window --highValue--> 90.0
limit_LT101_operating_window --note--> Keep LT101 between 10 % and 90 % during the stripping loop test.
limit_LT101_operating_window --type--> OperatingLimit
limit_LT101_operating_window --variable--> level
limit_LT101_operating_window --valueVerified--> true
limit_LT101_operating_window --source--> REPORT E.3.7, E.3.8
LT101__cit03 --document--> SRC_TEAM
LT101__cit03 --label--> Citation 3 for LT101
LT101__cit03 --location--> left-hand side of E100 sump
LT101__cit03 --citationText--> Team check left-hand side of E100 sump
LT101__cit03 --type--> Citation
LT101__cit02 --location--> Appendix B instrument list
LT101__cit02 --document--> SRC_REPORT
LT101__cit02 --label--> Citation 2 for LT101
LT101__cit02 --type--> Citation
LT101__cit02 --citationText--> Pilot Plant Report Appendix B instrument list
```

Question: LT101 rises above 85% during normal operation. What adjustments are specified, and what is the high-high response?

## Q73

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
aspen_v3_block_E101 --type--> AspenBlock
aspen_v3_block_E101 --aspenModel--> RADFRAC
aspen_v3_block_E101 --blockId--> E101
aspen_v3_block_E101 --status--> OK
aspen_v3_block_E101 --label--> E101 (ABB_pilot_plant_final_3)
aspen_v3_block_E101 --inCase--> case_aspen_v3
aspen_v3_stream_S8 --fromBlock--> aspen_v3_block_E101
aspen_v3_stream_1 --toBlock--> aspen_v3_block_E101
aspen_v3_stream_2 --toBlock--> aspen_v3_block_E101
aspen_v3_stream_4 --fromBlock--> aspen_v3_block_E101
LT108 --tag--> LT108
LT108 --type--> LevelInstrument
LT108 --floor--> 1
LT108 --monitors--> E101
LT108 --label--> LT108
LT108 --gridReference--> K15
LT108 --signalType--> Fieldbus
LT108 --measuredVariable--> E101 sump level
LT108 --sensorType--> differential pressure transmitter
PROC_pump_start_order_step_01 --operatesOn--> LT108
CL_E101_level --hasSensor--> LT108
aspen_v6_1_block_E101 --type--> AspenBlock
aspen_v6_1_block_E101 --aspenModel--> RADFRAC
aspen_v6_1_block_E101 --label--> E101 (ABB_pilot_plant_final_6_1_SA_validation)
aspen_v6_1_block_E101 --blockId--> E101
aspen_v6_1_block_E101 --status--> OK
aspen_v6_1_block_E101 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S8 --fromBlock--> aspen_v6_1_block_E101
aspen_v6_1_stream_2 --toBlock--> aspen_v6_1_block_E101
aspen_v6_1_stream_1 --toBlock--> aspen_v6_1_block_E101
aspen_v6_1_stream_4 --fromBlock--> aspen_v6_1_block_E101
E101 --pipedTo--> RV400
E101 --floor--> 1
E101 --note--> Lean MEA enters at the top through NRV400; rich MEA leaves from the sump to J101a/b. The air admittance valve shown on the P&ID has been removed from the plant (DIFF, E14/15).
E101 --feedsInto--> E101_N_sump_outlet
E101 --designBasis--> Packing and column designed for 2.3-2.5 bar operation on MEA and 50 kg/h CO2 (HAZOP 10.4)
E101 --feedsInto--> E101_N_gas_outlet
E101 --pipedTo--> E101_N_sump_outlet
E101 --pipedTo--> E101_N_gas_outlet
E101 --type--> AbsorptionColumn
E101 --diameter_mm--> 230.0
E101 --tag--> E101
E101 --label--> E101 absorber
HAZOP_7_10 --concerns--> E101
TT305 --monitors--> E101
PT111 --monitors--> E101
E101_sample_5 --onColumn--> E101
E101_N_gas_outlet --onEquipment--> E101
LSLL109 --monitors--> E101
TT207 --monitors--> E101
PT403 --monitors--> E101
LI108 --monitors--> E101
E101_sample_4 --onColumn--> E101
E101_N_sump_outlet --onEquipment--> E101
FT109 --monitors--> E101
E101_sample_3 --onColumn--> E101
HAZOP_9b_05 --concerns--> E101
limit_LZAL109 --appliesTo--> E101
DI108 --monitors--> E101
E101_N_gas_inlet --feedsInto--> E101
FT304 --monitors--> E101
K101_N2_recycle --bypasses--> E101
PT110 --monitors--> E101
E101_N_gas_inlet --pipedTo--> E101
HAZOP_5_08 --concerns--> E101
HAZOP_8_01 --concerns--> E101
HAZOP_8_06 --concerns--> E101
PI403 --monitors--> E101
AT400 --monitors--> E101
FT303 --monitors--> E101
TT205 --monitors--> E101
E101_N_base_inlet --onEquipment--> E101
aspen_v6_1_E101_performance --ofEquipment--> E101
TT206 --monitors--> E101
HAZOP_8_03 --concerns--> E101
E101_N_gas_inlet --onEquipment--> E101
E101_N_top_inlet --feedsInto--> E101
E101_sample_6 --onColumn--> E101
K402 --pipedTo--> E101
HAZOP_5_07 --concerns--> E101
AI300 --monitors--> E101
FI109 --monitors--> E101
FI108 --monitors--> E101
aspen_v3_vent_gas --ofEquipment--> E101
AT300 --monitors--> E101
E101_N_top_inlet --pipedTo--> E101
aspen_v6_1_feed_gas --ofEquipment--> E101
limit_PSHH117_set --appliesTo--> E101
TT109 --monitors--> E101
TT412 --monitors--> E101
HAZOP_10_03 --concerns--> E101
LSHH107 --monitors--> E101
E101_sample_2 --onColumn--> E101
limit_LZAH107 --appliesTo--> E101
HAZOP_5_06 --concerns--> E101
PSHH117 --monitors--> E101
TT413 --monitors--> E101
HAZOP_7_13 --concerns--> E101
TT107 --monitors--> E101
TT306 --monitors--> E101
E101_N_top_inlet --onEquipment--> E101
E101_sample_1 --onColumn--> E101
AOI10 --about--> E101
RV400 --protects--> E101
FT108 --monitors--> E101
TT411 --monitors--> E101
TT204 --monitors--> E101
aspen_v3_feed_gas --ofEquipment--> E101
HAZOP_element_10 --covers--> E101
HAZOP_8_11 --concerns--> E101
TT307 --monitors--> E101
TT308 --monitors--> E101
HAZOP_8_02 --concerns--> E101
aspen_v3_E101_performance --ofEquipment--> E101
PCV300 --valveType--> pressure control
PCV300 --floor--> 3
PCV300 --normalPosition--> open
PCV300 --note--> Vents lean gas from the absorber to hold the E101 pressure (PIC403). Opened in the vent stream start-up (Fig F.3), closed at shutdown.
PCV300 --pipedTo--> VENT_E101
PCV300 --label--> PCV300
PCV300 --feedsInto--> VENT_E101
PCV300 --type--> PressureControlValve
PCV300 --tag--> PCV300
PCV300 --gridReference--> G18
K402 --feedsInto--> PCV300
CL_E101_pressure --hasFinalElement--> PCV300
K402 --pipedTo--> PCV300
PIC403 --controls--> PCV300
AV01 --about--> PCV300
K101 --type--> Saturator
K101 --label--> K101 gas saturator
K101 --pipedTo--> SDV170
K101 --pipedTo--> Z103
K101 --floor--> 1
K101 --feedsInto--> E101_N_gas_inlet
K101 --pipedTo--> E101_N_gas_inlet
K101 --note--> Saturates the feed gas with water before E101; temperature held by TIC121 using C106 on the recirculating water. Grid not in the REPORT lists (near L17 to L18 on the P&ID). Not modelled in Aspen (GOI09).
K101 --pipedTo--> V126
K101 --tag--> K101
DI_CARTRIDGE --feedsInto--> K101
HAZOP_4_06 --concerns--> K101
V172 --pipedTo--> K101
J102 --pipedTo--> K101
limit_LZAL_K101 --appliesTo--> K101
HAZOP_4_07 --concerns--> K101
LT104 --monitors--> K101
HAZOP_3_05 --concerns--> K101
FEED_GAS_HEADER --feedsInto--> K101
GOI09 --about--> K101
LI106 --monitors--> K101
```

Question: The level in E101 falls below 5% on LT108. What must the operator do?

## Q74

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
aspen_v3_block_E101 --type--> AspenBlock
aspen_v3_block_E101 --aspenModel--> RADFRAC
aspen_v3_block_E101 --blockId--> E101
aspen_v3_block_E101 --status--> OK
aspen_v3_block_E101 --label--> E101 (ABB_pilot_plant_final_3)
aspen_v3_block_E101 --inCase--> case_aspen_v3
aspen_v3_stream_S8 --fromBlock--> aspen_v3_block_E101
aspen_v3_stream_1 --toBlock--> aspen_v3_block_E101
aspen_v3_stream_2 --toBlock--> aspen_v3_block_E101
aspen_v3_stream_4 --fromBlock--> aspen_v3_block_E101
LT108 --tag--> LT108
LT108 --type--> LevelInstrument
LT108 --floor--> 1
LT108 --monitors--> E101
LT108 --label--> LT108
LT108 --gridReference--> K15
LT108 --signalType--> Fieldbus
LT108 --measuredVariable--> E101 sump level
LT108 --sensorType--> differential pressure transmitter
PROC_pump_start_order_step_01 --operatesOn--> LT108
CL_E101_level --hasSensor--> LT108
aspen_v6_1_block_E101 --type--> AspenBlock
aspen_v6_1_block_E101 --aspenModel--> RADFRAC
aspen_v6_1_block_E101 --label--> E101 (ABB_pilot_plant_final_6_1_SA_validation)
aspen_v6_1_block_E101 --blockId--> E101
aspen_v6_1_block_E101 --status--> OK
aspen_v6_1_block_E101 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S8 --fromBlock--> aspen_v6_1_block_E101
aspen_v6_1_stream_2 --toBlock--> aspen_v6_1_block_E101
aspen_v6_1_stream_1 --toBlock--> aspen_v6_1_block_E101
aspen_v6_1_stream_4 --fromBlock--> aspen_v6_1_block_E101
E101 --pipedTo--> RV400
E101 --floor--> 1
E101 --note--> Lean MEA enters at the top through NRV400; rich MEA leaves from the sump to J101a/b. The air admittance valve shown on the P&ID has been removed from the plant (DIFF, E14/15).
E101 --feedsInto--> E101_N_sump_outlet
E101 --designBasis--> Packing and column designed for 2.3-2.5 bar operation on MEA and 50 kg/h CO2 (HAZOP 10.4)
E101 --feedsInto--> E101_N_gas_outlet
E101 --pipedTo--> E101_N_sump_outlet
E101 --pipedTo--> E101_N_gas_outlet
E101 --type--> AbsorptionColumn
E101 --diameter_mm--> 230.0
E101 --tag--> E101
E101 --label--> E101 absorber
HAZOP_7_10 --concerns--> E101
TT305 --monitors--> E101
PT111 --monitors--> E101
E101_sample_5 --onColumn--> E101
E101_N_gas_outlet --onEquipment--> E101
LSLL109 --monitors--> E101
TT207 --monitors--> E101
PT403 --monitors--> E101
LI108 --monitors--> E101
E101_sample_4 --onColumn--> E101
E101_N_sump_outlet --onEquipment--> E101
FT109 --monitors--> E101
E101_sample_3 --onColumn--> E101
HAZOP_9b_05 --concerns--> E101
limit_LZAL109 --appliesTo--> E101
DI108 --monitors--> E101
E101_N_gas_inlet --feedsInto--> E101
FT304 --monitors--> E101
K101_N2_recycle --bypasses--> E101
PT110 --monitors--> E101
E101_N_gas_inlet --pipedTo--> E101
HAZOP_5_08 --concerns--> E101
HAZOP_8_01 --concerns--> E101
HAZOP_8_06 --concerns--> E101
PI403 --monitors--> E101
AT400 --monitors--> E101
FT303 --monitors--> E101
TT205 --monitors--> E101
E101_N_base_inlet --onEquipment--> E101
aspen_v6_1_E101_performance --ofEquipment--> E101
TT206 --monitors--> E101
HAZOP_8_03 --concerns--> E101
E101_N_gas_inlet --onEquipment--> E101
E101_N_top_inlet --feedsInto--> E101
E101_sample_6 --onColumn--> E101
K402 --pipedTo--> E101
HAZOP_5_07 --concerns--> E101
AI300 --monitors--> E101
FI109 --monitors--> E101
FI108 --monitors--> E101
aspen_v3_vent_gas --ofEquipment--> E101
AT300 --monitors--> E101
E101_N_top_inlet --pipedTo--> E101
aspen_v6_1_feed_gas --ofEquipment--> E101
limit_PSHH117_set --appliesTo--> E101
TT109 --monitors--> E101
TT412 --monitors--> E101
HAZOP_10_03 --concerns--> E101
LSHH107 --monitors--> E101
E101_sample_2 --onColumn--> E101
limit_LZAH107 --appliesTo--> E101
HAZOP_5_06 --concerns--> E101
PSHH117 --monitors--> E101
TT413 --monitors--> E101
HAZOP_7_13 --concerns--> E101
TT107 --monitors--> E101
TT306 --monitors--> E101
E101_N_top_inlet --onEquipment--> E101
E101_sample_1 --onColumn--> E101
AOI10 --about--> E101
RV400 --protects--> E101
FT108 --monitors--> E101
TT411 --monitors--> E101
TT204 --monitors--> E101
aspen_v3_feed_gas --ofEquipment--> E101
HAZOP_element_10 --covers--> E101
HAZOP_8_11 --concerns--> E101
TT307 --monitors--> E101
TT308 --monitors--> E101
HAZOP_8_02 --concerns--> E101
aspen_v3_E101_performance --ofEquipment--> E101
PCV300 --valveType--> pressure control
PCV300 --floor--> 3
PCV300 --normalPosition--> open
PCV300 --note--> Vents lean gas from the absorber to hold the E101 pressure (PIC403). Opened in the vent stream start-up (Fig F.3), closed at shutdown.
PCV300 --pipedTo--> VENT_E101
PCV300 --label--> PCV300
PCV300 --feedsInto--> VENT_E101
PCV300 --type--> PressureControlValve
PCV300 --tag--> PCV300
PCV300 --gridReference--> G18
K402 --feedsInto--> PCV300
CL_E101_pressure --hasFinalElement--> PCV300
K402 --pipedTo--> PCV300
PIC403 --controls--> PCV300
AV01 --about--> PCV300
K101 --type--> Saturator
K101 --label--> K101 gas saturator
K101 --pipedTo--> SDV170
K101 --pipedTo--> Z103
K101 --floor--> 1
K101 --feedsInto--> E101_N_gas_inlet
K101 --pipedTo--> E101_N_gas_inlet
K101 --note--> Saturates the feed gas with water before E101; temperature held by TIC121 using C106 on the recirculating water. Grid not in the REPORT lists (near L17 to L18 on the P&ID). Not modelled in Aspen (GOI09).
K101 --pipedTo--> V126
K101 --tag--> K101
DI_CARTRIDGE --feedsInto--> K101
HAZOP_4_06 --concerns--> K101
V172 --pipedTo--> K101
J102 --pipedTo--> K101
limit_LZAL_K101 --appliesTo--> K101
HAZOP_4_07 --concerns--> K101
LT104 --monitors--> K101
HAZOP_3_05 --concerns--> K101
FEED_GAS_HEADER --feedsInto--> K101
GOI09 --about--> K101
LI106 --monitors--> K101
```

Question: LT108 indicates the absorber level is above 85%. Which immediate process adjustments are specified?

## Q75

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
C400_N_cw_out__utlcit01 --location--> C400
C400_N_cw_out__utlcit01 --type--> Citation
C400_N_cw_out__utlcit01 --document--> SRC_PID
C400_N_cw_out__utlcit01 --citationText--> P&ID C400
C400_N_cw_out__utlcit01 --label--> Citation 1 for C400_N_cw_out (utl)
aspen_v3_block_C400 --inCase--> case_aspen_v3
aspen_v3_block_C400 --aspenModel--> HEATER
aspen_v3_block_C400 --type--> AspenBlock
aspen_v3_block_C400 --blockId--> C400
aspen_v3_block_C400 --status--> OK
aspen_v3_block_C400 --label--> C400 (ABB_pilot_plant_final_3)
aspen_v3_stream_S11 --fromBlock--> aspen_v3_block_C400
aspen_v3_stream_S13 --toBlock--> aspen_v3_block_C400
LT401 --sensorType--> differential pressure transmitter
LT401 --floor--> 4
LT401 --type--> LevelInstrument
LT401 --monitors--> K401
LT401 --signalType--> 4-20mA
LT401 --measuredVariable--> liquid level in K401 (control table: 'liquid level in condenser C400')
LT401 --label--> LT401
LT401 --tag--> LT401
LT401 --gridReference--> F10
CL_K401_level --hasSensor--> LT401
HAZOP_element_12 --covers--> LT401
OOI05 --about--> LT401
limit_LAL_K401 --appliesTo--> LT401
C400_N_cw_in__utlcit01 --type--> Citation
C400_N_cw_in__utlcit01 --document--> SRC_PID
C400_N_cw_in__utlcit01 --citationText--> P&ID C400
C400_N_cw_in__utlcit01 --label--> Citation 1 for C400_N_cw_in (utl)
C400_N_cw_in__utlcit01 --location--> C400
aspen_v6_1_block_C400 --aspenModel--> HEATER
aspen_v6_1_block_C400 --label--> C400 (ABB_pilot_plant_final_6_1_SA_validation)
aspen_v6_1_block_C400 --blockId--> C400
aspen_v6_1_block_C400 --inCase--> case_aspen_v6_1
aspen_v6_1_block_C400 --status--> OK
aspen_v6_1_block_C400 --type--> AspenBlock
aspen_v6_1_stream_S11 --fromBlock--> aspen_v6_1_block_C400
aspen_v6_1_stream_S15 --toBlock--> aspen_v6_1_block_C400
C400 --floor--> 4
C400 --pipedTo--> K401
C400 --type--> Condenser
C400 --label--> C400 overhead condenser (spiral heat exchanger)
C400 --tag--> C400
C400 --note--> Water-cooled; cooling water flow set by FIC402 on FCV401 (cascade from TIC410). Grid not in the REPORT lists (between C8 and E10 on the P&ID).
C400 --feedsInto--> K401
E100_N_overhead --pipedTo--> C400
OOI04 --about--> C400
HAZOP_12_07 --concerns--> C400
aspen_v3_C400_performance --ofEquipment--> C400
OOI06 --about--> C400
HAZOP_12_03 --concerns--> C400
FI402 --monitors--> C400
C400_N_cw_in --onEquipment--> C400
HAZOP_6_05 --concerns--> C400
HAZOP_6_01 --concerns--> C400
C400_N_cw_out --onEquipment--> C400
PT401 --monitors--> C400
HAZOP_element_12 --covers--> C400
TI410 --monitors--> C400
limit_TAH_C400_carryover --appliesTo--> C400
FI401 --monitors--> C400
FT402 --monitors--> C400
HAZOP_6_06 --concerns--> C400
E100_N_overhead --feedsInto--> C400
TT410 --monitors--> C400
E100_N_overhead --type--> Nozzle
E100_N_overhead --onEquipment--> E100
E100_N_overhead --label--> E100 vapour outlet at the top of the column
E100 --feedsInto--> E100_N_overhead
E100 --pipedTo--> E100_N_overhead
C400__ovhcit01 --label--> Citation 1 for C400 (ovh)
C400__ovhcit01 --type--> Citation
C400__ovhcit01 --location--> overhead line after PT401, top of the drawing
C400__ovhcit01 --document--> SRC_PID
C400__ovhcit01 --citationText--> P&ID overhead line after PT401, top of the drawing
PCV415 --pipedTo--> FCV401
PCV415 --normalPosition--> open
PCV415 --note--> Pressure regulator on the C400 cooling water stream (UT09). The valve list gives floor 3.
PCV415 --floor--> 4
PCV415 --type--> PressureControlValve
PCV415 --gridReference--> C14
PCV415 --tag--> PCV415
PCV415 --feedsInto--> FCV401
PCV415 --valveType--> pressure control
PCV415 --label--> PCV415
UT09 --about--> PCV415
V405 --feedsInto--> PCV415
V405 --pipedTo--> PCV415
OverheadRefluxLoop_step_06_LT401 --stepIndex--> 6
OverheadRefluxLoop_step_06_LT401 --label--> Stripper overhead and reflux loop step 6: LT401
OverheadRefluxLoop_step_06_LT401 --stepItem--> LT401
OverheadRefluxLoop_step_06_LT401 --stepType--> tie-in
OverheadRefluxLoop_step_06_LT401 --type--> LoopStep
TIC410 --type--> Controller
TIC410 --tag--> TIC410
TIC410 --label--> C400 gas outlet temperature controller (cascade master)
TIC410 --controls--> FCV401
CL_C400_temperature --hasController--> TIC410
OOI04 --description--> Aspen returns the reflux to the rich feed before the heaters (MIXER2), but on the P&ID it joins after them at V403/V402
OOI04 --foundBy--> ovh section build, Oct 2026
OOI04 --about--> J300
OOI04 --type--> OpenItem
OOI04 --resolvedBy--> Note for model comparison; update the Aspen flowsheet if needed
OOI04 --itemStatus--> open
OOI04 --label--> OOI04: Aspen returns the reflux to the rich feed before the heaters (MIXER2), but on the P&ID it joins after them at V403/V402
HAZOP_6_01 --actionTaken--> Pump shutdown trip added
HAZOP_6_01 --consequence--> No flow to J103
HAZOP_6_01 --concerns--> J103
HAZOP_6_01 --inElement--> HAZOP_element_6
HAZOP_6_01 --cause--> K401 / C300 (now C400) blocked
HAZOP_6_01 --guideword--> NO
HAZOP_6_01 --label--> HAZOP 6.1
HAZOP_6_01 --recommendedAction--> Consider consequences of starving J103
HAZOP_6_01 --parameter--> FLOW
HAZOP_6_01 --type--> HazopDeviation
HAZOP_6_01 --itemNumber--> 1
HAZOP_6_01 --concerns--> K401
TT410 --signalType--> Fieldbus
TT410 --measuredVariable--> temperature of CO2 leaving C400
TT410 --floor--> 4
TT410 --label--> TT410
TT410 --sensorType--> PRT
TT410 --tag--> TT410
TT410 --gridReference--> C15
TT410 --type--> TemperatureInstrument
CL_C400_temperature --hasSensor--> TT410
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_07_J300
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_14_FT305
OverheadRefluxLoop --label--> Stripper overhead and reflux loop
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_09_RV300
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_02_PT401
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_03_C400
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_10_B300
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_08_TT310
OverheadRefluxLoop --note--> Runs whenever E100 is boiling. Vapour is condensed in C400; K401 separates the condensate (returned as reflux by J300) from the CO2-rich gas (to the CO2 return, piece 7).
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_06_LT401
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_05_K401
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_17_E100_N_top_inlet
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_01_E100_N_overhead
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_15_V403
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_00_E100
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_16_V402
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_12_V317
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_13_TT309
OverheadRefluxLoop --type--> Loop
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_04_LSHH400
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_11_PCV302
OverheadRefluxLoop --inMode--> FigureOfEight
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_18_E100
```

Question: LT401 shows the liquid level in C400 has fallen below 5%. What is the correct response?

## Q76

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
C400_N_cw_out__utlcit01 --location--> C400
C400_N_cw_out__utlcit01 --type--> Citation
C400_N_cw_out__utlcit01 --document--> SRC_PID
C400_N_cw_out__utlcit01 --citationText--> P&ID C400
C400_N_cw_out__utlcit01 --label--> Citation 1 for C400_N_cw_out (utl)
aspen_v3_block_C400 --inCase--> case_aspen_v3
aspen_v3_block_C400 --aspenModel--> HEATER
aspen_v3_block_C400 --type--> AspenBlock
aspen_v3_block_C400 --blockId--> C400
aspen_v3_block_C400 --status--> OK
aspen_v3_block_C400 --label--> C400 (ABB_pilot_plant_final_3)
aspen_v3_stream_S11 --fromBlock--> aspen_v3_block_C400
aspen_v3_stream_S13 --toBlock--> aspen_v3_block_C400
C400_N_cw_in__utlcit01 --type--> Citation
C400_N_cw_in__utlcit01 --document--> SRC_PID
C400_N_cw_in__utlcit01 --citationText--> P&ID C400
C400_N_cw_in__utlcit01 --label--> Citation 1 for C400_N_cw_in (utl)
C400_N_cw_in__utlcit01 --location--> C400
aspen_v6_1_block_C400 --aspenModel--> HEATER
aspen_v6_1_block_C400 --label--> C400 (ABB_pilot_plant_final_6_1_SA_validation)
aspen_v6_1_block_C400 --blockId--> C400
aspen_v6_1_block_C400 --inCase--> case_aspen_v6_1
aspen_v6_1_block_C400 --status--> OK
aspen_v6_1_block_C400 --type--> AspenBlock
aspen_v6_1_stream_S11 --fromBlock--> aspen_v6_1_block_C400
aspen_v6_1_stream_S15 --toBlock--> aspen_v6_1_block_C400
C400 --floor--> 4
C400 --pipedTo--> K401
C400 --type--> Condenser
C400 --label--> C400 overhead condenser (spiral heat exchanger)
C400 --tag--> C400
C400 --note--> Water-cooled; cooling water flow set by FIC402 on FCV401 (cascade from TIC410). Grid not in the REPORT lists (between C8 and E10 on the P&ID).
C400 --feedsInto--> K401
E100_N_overhead --pipedTo--> C400
OOI04 --about--> C400
HAZOP_12_07 --concerns--> C400
aspen_v3_C400_performance --ofEquipment--> C400
OOI06 --about--> C400
HAZOP_12_03 --concerns--> C400
FI402 --monitors--> C400
C400_N_cw_in --onEquipment--> C400
HAZOP_6_05 --concerns--> C400
HAZOP_6_01 --concerns--> C400
C400_N_cw_out --onEquipment--> C400
PT401 --monitors--> C400
HAZOP_element_12 --covers--> C400
TI410 --monitors--> C400
limit_TAH_C400_carryover --appliesTo--> C400
FI401 --monitors--> C400
FT402 --monitors--> C400
HAZOP_6_06 --concerns--> C400
E100_N_overhead --feedsInto--> C400
TT410 --monitors--> C400
E100_N_overhead --type--> Nozzle
E100_N_overhead --onEquipment--> E100
E100_N_overhead --label--> E100 vapour outlet at the top of the column
E100 --feedsInto--> E100_N_overhead
E100 --pipedTo--> E100_N_overhead
C400__ovhcit01 --label--> Citation 1 for C400 (ovh)
C400__ovhcit01 --type--> Citation
C400__ovhcit01 --location--> overhead line after PT401, top of the drawing
C400__ovhcit01 --document--> SRC_PID
C400__ovhcit01 --citationText--> P&ID overhead line after PT401, top of the drawing
PCV415 --pipedTo--> FCV401
PCV415 --normalPosition--> open
PCV415 --note--> Pressure regulator on the C400 cooling water stream (UT09). The valve list gives floor 3.
PCV415 --floor--> 4
PCV415 --type--> PressureControlValve
PCV415 --gridReference--> C14
PCV415 --tag--> PCV415
PCV415 --feedsInto--> FCV401
PCV415 --valveType--> pressure control
PCV415 --label--> PCV415
UT09 --about--> PCV415
V405 --feedsInto--> PCV415
V405 --pipedTo--> PCV415
TIC410 --type--> Controller
TIC410 --tag--> TIC410
TIC410 --label--> C400 gas outlet temperature controller (cascade master)
TIC410 --controls--> FCV401
CL_C400_temperature --hasController--> TIC410
OOI04 --description--> Aspen returns the reflux to the rich feed before the heaters (MIXER2), but on the P&ID it joins after them at V403/V402
OOI04 --foundBy--> ovh section build, Oct 2026
OOI04 --about--> J300
OOI04 --type--> OpenItem
OOI04 --resolvedBy--> Note for model comparison; update the Aspen flowsheet if needed
OOI04 --itemStatus--> open
OOI04 --label--> OOI04: Aspen returns the reflux to the rich feed before the heaters (MIXER2), but on the P&ID it joins after them at V403/V402
HAZOP_6_01 --actionTaken--> Pump shutdown trip added
HAZOP_6_01 --consequence--> No flow to J103
HAZOP_6_01 --concerns--> J103
HAZOP_6_01 --inElement--> HAZOP_element_6
HAZOP_6_01 --cause--> K401 / C300 (now C400) blocked
HAZOP_6_01 --guideword--> NO
HAZOP_6_01 --label--> HAZOP 6.1
HAZOP_6_01 --recommendedAction--> Consider consequences of starving J103
HAZOP_6_01 --parameter--> FLOW
HAZOP_6_01 --type--> HazopDeviation
HAZOP_6_01 --itemNumber--> 1
HAZOP_6_01 --concerns--> K401
TT410 --signalType--> Fieldbus
TT410 --measuredVariable--> temperature of CO2 leaving C400
TT410 --floor--> 4
TT410 --label--> TT410
TT410 --sensorType--> PRT
TT410 --tag--> TT410
TT410 --gridReference--> C15
TT410 --type--> TemperatureInstrument
CL_C400_temperature --hasSensor--> TT410
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_07_J300
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_14_FT305
OverheadRefluxLoop --label--> Stripper overhead and reflux loop
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_09_RV300
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_02_PT401
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_03_C400
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_10_B300
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_08_TT310
OverheadRefluxLoop --note--> Runs whenever E100 is boiling. Vapour is condensed in C400; K401 separates the condensate (returned as reflux by J300) from the CO2-rich gas (to the CO2 return, piece 7).
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_06_LT401
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_05_K401
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_17_E100_N_top_inlet
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_01_E100_N_overhead
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_15_V403
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_00_E100
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_16_V402
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_12_V317
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_13_TT309
OverheadRefluxLoop --type--> Loop
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_04_LSHH400
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_11_PCV302
OverheadRefluxLoop --inMode--> FigureOfEight
OverheadRefluxLoop --hasStep--> OverheadRefluxLoop_step_18_E100
C400__ovhcit03 --citationText--> P&ID differences row LSHH400 (between C400 and K401)
C400__ovhcit03 --location--> row LSHH400 (between C400 and K401)
C400__ovhcit03 --document--> SRC_DIFF
C400__ovhcit03 --label--> Citation 3 for C400 (ovh)
C400__ovhcit03 --type--> Citation
C400_N_cw_in --pipedTo--> C400_N_cw_out
C400_N_cw_in --label--> C400 cooling water inlet
C400_N_cw_in --type--> Nozzle
C400_N_cw_in --feedsInto--> C400_N_cw_out
FT402 --pipedTo--> C400_N_cw_in
FT402 --feedsInto--> C400_N_cw_in
CL_C400_cooling_water --hasFinalElement--> FCV401
CL_C400_cooling_water --controlledVariable--> Cooling water flowrate to C400
CL_C400_cooling_water --manipulatedVariable--> FCV401 opening
CL_C400_cooling_water --label--> Cooling water flow to C400 (cascade slave)
CL_C400_cooling_water --hasController--> FIC402
CL_C400_cooling_water --hasSensor--> FT402
CL_C400_cooling_water --type--> ControlLoop
```

Question: The liquid level in C400 rises above 85%. What should be done before the high-high condition is reached?

## Q77

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
J102 --floor--> 1
J102 --pipedTo--> K101
J102 --tag--> J102
J102 --note--> Blows the recycled N2 from K102 into K101 only (team trace). HAZOP 5.2 (2010) mentions combined spillback and speed control; no spillback is drawn now.
J102 --label--> J102 lobe blower (N2 return)
J102 --type--> Blower
J102 --gridReference--> L17
J102 --feedsInto--> K101
HAZOP_5_01 --concerns--> J102
HAZOP_5_02 --concerns--> J102
K102 --pipedTo--> J102
K102 --feedsInto--> J102
FI304 --monitors--> J102
GR10 --about--> J102
GR01 --about--> J102
HAZOP_5_09 --concerns--> J102
FT107 --monitors--> J102
TT114 --monitors--> J102
TT304 --monitors--> J102
HAZOP_element_5 --covers--> J102
HAZOP_5_04 --concerns--> J102
FI303 --monitors--> J102
K402 --feedsInto--> PCV300
K402 --pipedTo--> PCV300
K402 --feedsInto--> K402_N_gas_to_return
K402 --pipedTo--> K402_N_gas_to_return
K402 --label--> K402 cyclone separator on the E101 overhead
K402 --note--> Removes liquid carried over from E101 (demister pad; oversized liquid return to E101, HAZOP 5.9). A tuning-fork liquid level switch and trip were added downstream of it (HAZOP 10.1). Grid not in the REPORT lists.
K402 --type--> CycloneSeparator
K402 --pipedTo--> E101
K402 --floor--> 4
K402 --tag--> K402
AV01 --about--> K402
GR02 --about--> K402
HAZOP_5_09 --concerns--> K402
HAZOP_10_05 --concerns--> K402
E101_N_gas_outlet --feedsInto--> K402
HAZOP_element_5 --covers--> K402
AV08 --about--> K402
FT300 --monitors--> K402
E101_N_gas_outlet --pipedTo--> K402
K402_N_gas_to_return --onEquipment--> K402
HAZOP_10_01 --concerns--> K402
N2ReturnLoop --hasStep--> N2ReturnLoop_step_00_E101
N2ReturnLoop --hasStep--> N2ReturnLoop_step_02_K402
N2ReturnLoop --hasStep--> N2ReturnLoop_step_15_E101_N_gas_inlet
N2ReturnLoop --inMode--> FigureOfEight
N2ReturnLoop --hasStep--> N2ReturnLoop_step_01_E101_N_gas_outlet
N2ReturnLoop --hasStep--> N2ReturnLoop_step_05_FT303
N2ReturnLoop --hasStep--> N2ReturnLoop_step_16_E101
N2ReturnLoop --hasStep--> N2ReturnLoop_step_13_FT107
N2ReturnLoop --hasStep--> N2ReturnLoop_step_07_FT304
N2ReturnLoop --note--> N2 is not absorbed, so it is recirculated: J102 blows it from the K402 overhead back through K101 into E101. Fresh N2 and CO2 (piece 5) top it up. FCV111 recycles part of it from K101 back to K102 to set the N2 flow into E101.
N2ReturnLoop --hasStep--> N2ReturnLoop_step_03_K402_N_gas_to_return
N2ReturnLoop --hasStep--> N2ReturnLoop_step_10_V187
N2ReturnLoop --hasStep--> N2ReturnLoop_step_04_TT304
N2ReturnLoop --label--> N2 return loop (E101 > K402 > K102 > J102 > K101 > E101)
N2ReturnLoop --hasStep--> N2ReturnLoop_step_12_TT114
N2ReturnLoop --hasStep--> N2ReturnLoop_step_08_FI304
N2ReturnLoop --hasStep--> N2ReturnLoop_step_14_K101
N2ReturnLoop --hasStep--> N2ReturnLoop_step_06_FI303
N2ReturnLoop --hasStep--> N2ReturnLoop_step_09_K102
N2ReturnLoop --type--> Loop
N2ReturnLoop --hasStep--> N2ReturnLoop_step_11_J102
AV01 --label--> AV01: The order of items on the E101 overhead line, and where the gas splits between the vent (PCV300) and the N2 return (J102, piece 7)
AV01 --resolvedBy--> Trace on the P&ID
AV01 --foundBy--> aov section build, Oct 2026
AV01 --itemStatus--> open
AV01 --description--> The order of items on the E101 overhead line, and where the gas splits between the vent (PCV300) and the N2 return (J102, piece 7)
AV01 --about--> PCV300
AV01 --type--> OpenItem
J102__grtcit01 --label--> Citation 1 for J102 (grt)
J102__grtcit01 --document--> SRC_PID
J102__grtcit01 --citationText--> P&ID grid L17
J102__grtcit01 --location--> grid L17
J102__grtcit01 --type--> Citation
N2ReturnLoop_step_11_J102 --label--> N2 return loop (E101 > K402 > K102 > J102 > K101 > E101) step 11: J102
N2ReturnLoop_step_11_J102 --stepItem--> J102
N2ReturnLoop_step_11_J102 --stepIndex--> 11
N2ReturnLoop_step_11_J102 --type--> LoopStep
N2ReturnLoop_step_11_J102 --stepType--> inline
N2ReturnLoop_step_04_TT304 --stepType--> tie-in
N2ReturnLoop_step_04_TT304 --type--> LoopStep
N2ReturnLoop_step_04_TT304 --label--> N2 return loop (E101 > K402 > K102 > J102 > K101 > E101) step 4: TT304
N2ReturnLoop_step_04_TT304 --stepIndex--> 4
N2ReturnLoop_step_04_TT304 --stepItem--> TT304
FT107 --sensorType--> variable area volumetric flow meter
FT107 --label--> FT107
FT107 --measuredVariable--> flow at J102 (position to trace)
FT107 --signalType--> 4-20mA
FT107 --tag--> FT107
FT107 --floor--> 1
FT107 --gridReference--> L17
FT107 --type--> FlowInstrument
N2ReturnLoop_step_05_FT303 --stepItem--> FT303
N2ReturnLoop_step_05_FT303 --type--> LoopStep
N2ReturnLoop_step_05_FT303 --stepType--> inline
N2ReturnLoop_step_05_FT303 --label--> N2 return loop (E101 > K402 > K102 > J102 > K101 > E101) step 5: FT303
N2ReturnLoop_step_05_FT303 --stepIndex--> 5
TT114 --label--> TT114
TT114 --tag--> TT114
TT114 --sensorType--> K-type thermocouple
TT114 --signalType--> 4-20mA
TT114 --floor--> 1
TT114 --gridReference--> L17
TT114 --type--> TemperatureInstrument
TT114 --measuredVariable--> J102 temperature
N2ReturnLoop_step_13_FT107 --label--> N2 return loop (E101 > K402 > K102 > J102 > K101 > E101) step 13: FT107
N2ReturnLoop_step_13_FT107 --stepIndex--> 13
N2ReturnLoop_step_13_FT107 --type--> LoopStep
N2ReturnLoop_step_13_FT107 --stepItem--> FT107
N2ReturnLoop_step_13_FT107 --stepType--> tie-in
HAZOP_10_01 --parameter--> FLOW
HAZOP_10_01 --itemNumber--> 1
HAZOP_10_01 --safeguard--> Low fluid inventory in system
HAZOP_10_01 --actionTaken--> Action completed
HAZOP_10_01 --guideword--> NO
HAZOP_10_01 --cause--> Blockage in the packing / trays / redistributors
HAZOP_10_01 --recommendedAction--> Tuning fork liquid level detection & trip downstream of K402 cyclone.
HAZOP_10_01 --label--> HAZOP 10.1
HAZOP_10_01 --inElement--> HAZOP_element_10
HAZOP_10_01 --consequence--> Flowrate down column < inlet flowrate .: accumulation of liquid.  Worst scenario - liquid into inlet of blower J102 depending on height of blocked plane (i.e. liquid space above vs plant liquid inventory)
HAZOP_10_01 --type--> HazopDeviation
GR01 --about--> K102
GR01 --foundBy--> grt section build, Oct 2026
GR01 --type--> OpenItem
GR01 --resolvedBy--> Trace on the P&ID
GR01 --label--> GR01: Exact order of TT114 and FT107 around J102
GR01 --description--> Exact order of TT114 and FT107 around J102
GR01 --itemStatus--> open
N2ReturnLoop_step_16_E101 --type--> LoopStep
N2ReturnLoop_step_16_E101 --stepType--> inline
N2ReturnLoop_step_16_E101 --label--> N2 return loop (E101 > K402 > K102 > J102 > K101 > E101) step 16: E101
N2ReturnLoop_step_16_E101 --stepItem--> E101
N2ReturnLoop_step_16_E101 --stepIndex--> 16
Blower --subClassOf--> Equipment
Blower --type--> Class
Blower --comment--> Low-pressure gas mover (J102 is a lobe blower).
N2ReturnLoop_step_10_V187 --stepItem--> V187
N2ReturnLoop_step_10_V187 --stepType--> branch
N2ReturnLoop_step_10_V187 --label--> N2 return loop (E101 > K402 > K102 > J102 > K101 > E101) step 10: V187
N2ReturnLoop_step_10_V187 --stepIndex--> 10
N2ReturnLoop_step_10_V187 --type--> LoopStep
HAZOP_10_05 --guideword--> MISDIRECTED
HAZOP_10_05 --inElement--> HAZOP_element_10
HAZOP_10_05 --parameter--> FLOW
HAZOP_10_05 --type--> HazopDeviation
HAZOP_10_05 --consequence--> Blockage in column
HAZOP_10_05 --itemNumber--> 5
HAZOP_10_05 --actionTaken--> Action completed
```

Question: A gas leak is suspected in the nitrogen return pipe between K402 and J102. What precautions and emergency actions are required?

## Q78

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
H100 --tag--> H100
H100 --floor--> 1
H100 --source--> SUMMARY p.102
H100 --type--> SteamReboiler
H100 --feedsInto--> Q106
H100 --pipedTo--> Q106
H100 --label--> H100 vertical thermosiphon steam reboiler
FI102 --monitors--> H100
H100_N_condensate_out --onEquipment--> H100
TT100 --monitors--> H100
aspen_v3_H100_performance --ofEquipment--> H100
FT101 --monitors--> H100
HAZOP_element_13 --covers--> H100
aspen_v6_1_block_H100 --represents--> H100
TI100 --monitors--> H100
PROC_reboiler_heating_step_04 --operatesOn--> H100
DI100 --monitors--> H100
limit_H100_steam_limit --appliesTo--> H100
PI101 --monitors--> H100
PI100 --monitors--> H100
aspen_v3_block_H100REAC --represents--> H100
PT101 --monitors--> H100
FT102 --monitors--> H100
aspen_v3_block_H100HEAT --represents--> H100
TT117 --monitors--> H100
TT118 --monitors--> H100
FI100 --monitors--> H100
Q105 --pipedTo--> H100
H100_N_steam_in --onEquipment--> H100
Q105 --feedsInto--> H100
aspen_v6_1_H100_performance --ofEquipment--> H100
FT100 --monitors--> H100
HAZOP_element_11 --covers--> H100
RV107 --protects--> H100
aspen_v6_1_block_H100 --label--> H100 (ABB_pilot_plant_final_6_1_SA_validation)
aspen_v6_1_block_H100 --blockId--> H100
aspen_v6_1_block_H100 --aspenModel--> HEATX
aspen_v6_1_block_H100 --type--> AspenBlock
aspen_v6_1_block_H100 --statusMessage--> INVALID INPUT SPECIFICATIONS SEE TASC BROWSER FOR INFO.
aspen_v6_1_block_H100 --status--> ERROR
aspen_v6_1_block_H100 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S14 --fromBlock--> aspen_v6_1_block_H100
aspen_v6_1_stream_S17 --fromBlock--> aspen_v6_1_block_H100
aspen_v6_1_stream_S31 --toBlock--> aspen_v6_1_block_H100
aspen_v6_1_stream_S23 --toBlock--> aspen_v6_1_block_H100
PROC_reboiler_heating_step_01 --operatesOn--> FT100
PROC_reboiler_heating_step_01 --stepOrder--> 1
PROC_reboiler_heating_step_01 --instruction--> Check whether FT100 and FT101 show steam flowing to H100
PROC_reboiler_heating_step_01 --type--> ProcedureStep
PROC_reboiler_heating_step_01 --label--> Reboiler heating the MEA during the stripping loop test step 1
PROC_reboiler_heating --hasProcedureStep--> PROC_reboiler_heating_step_01
aspen_v6_1_stream_S14 --massFlow_kg_h--> 199.9608
aspen_v6_1_stream_S14 --co2Loading_mol_mol--> 0.638118
aspen_v6_1_stream_S14 --waterFlow_kg_h--> 156.4997
aspen_v6_1_stream_S14 --temperature_C--> 89.36771
aspen_v6_1_stream_S14 --pressure_bar--> 2.05248
aspen_v6_1_stream_S14 --type--> StreamState
aspen_v6_1_stream_S14 --label--> S14 (ABB_pilot_plant_final_6_1_SA_validation)
aspen_v6_1_stream_S14 --streamId--> S14
aspen_v6_1_stream_S14 --moleFlow_kmol_h--> 9.279221
aspen_v6_1_stream_S14 --vapourFraction--> 0.0
aspen_v6_1_stream_S14 --phase--> LIQUID
aspen_v6_1_stream_S14 --apparentCO2_kg_h--> 13.05912
aspen_v6_1_stream_S14 --meaMassFraction--> 0.1420495
aspen_v6_1_stream_S14 --enthalpyFlow_W--> -759156.0
aspen_v6_1_stream_S14 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S14 --toBlock--> aspen_v6_1_block_E100
SteamRoute_step_19_V103 --label--> Steam and condensate route to H100 step 19: V103
SteamRoute_step_19_V103 --stepItem--> V103
SteamRoute_step_19_V103 --stepType--> inline
SteamRoute_step_19_V103 --stepIndex--> 19
SteamRoute_step_19_V103 --type--> LoopStep
SteamRoute --hasStep--> SteamRoute_step_17_K100
SteamRoute --hasStep--> SteamRoute_step_15_PI101
SteamRoute --hasStep--> SteamRoute_step_21_V105
SteamRoute --hasStep--> SteamRoute_step_02_V100
SteamRoute --hasStep--> SteamRoute_step_20_V104
SteamRoute --hasStep--> SteamRoute_step_04_PI100
SteamRoute --hasStep--> SteamRoute_step_13_H100_N_condensate_out
SteamRoute --hasStep--> SteamRoute_step_01_XV140
SteamRoute --type--> Loop
SteamRoute --hasStep--> SteamRoute_step_14_TT118
SteamRoute --hasStep--> SteamRoute_step_07_FI100
SteamRoute --hasStep--> SteamRoute_step_11_TT117
SteamRoute --hasStep--> SteamRoute_step_16_RV107
SteamRoute --hasStep--> SteamRoute_step_22_NRV110
SteamRoute --hasStep--> SteamRoute_step_03_PT101
SteamRoute --note--> Building steam heats the MEA in the H100 reboiler shell and leaves as condensate through the K100 trap. FCV110 sets the steam flow (TIC100 > FIC100 cascade, stripping loop).
SteamRoute --inMode--> FigureOfEight
SteamRoute --hasStep--> SteamRoute_step_09_FT101
SteamRoute --hasStep--> SteamRoute_step_12_H100_N_steam_in
SteamRoute --hasStep--> SteamRoute_step_19_V103
SteamRoute --hasStep--> SteamRoute_step_05_V101
SteamRoute --hasStep--> SteamRoute_step_06_FT100
SteamRoute --hasStep--> SteamRoute_step_08_V102
SteamRoute --hasStep--> SteamRoute_step_10_FCV110
SteamRoute --label--> Steam and condensate route to H100
SteamRoute --hasStep--> SteamRoute_step_00_STEAM_SUPPLY
SteamRoute --hasStep--> SteamRoute_step_23_CONDENSATE_RETURN
SteamRoute --hasStep--> SteamRoute_step_18_V106
aspen_v3_H100_performance --coldInlet_C--> 116.8438
aspen_v3_H100_performance --label--> H100 performance (ABB_pilot_plant_final_3)
aspen_v3_H100_performance --coldSideDuty_kW--> 115.5427
aspen_v3_H100_performance --type--> HeatExchangerPerformance
aspen_v3_H100_performance --lmtd_K--> 32.8462
aspen_v3_H100_performance --area_m2--> 61.6081
aspen_v3_H100_performance --hotOutlet_C--> 118.2011
aspen_v3_H100_performance --derivedBy--> heat_mass_transfer.py
aspen_v3_H100_performance --minApproach_K--> 1.357255
aspen_v3_H100_performance --temperatureCross--> false
aspen_v3_H100_performance --overallU_W_m2K--> 448.1082
aspen_v3_H100_performance --hotInlet_C--> 276.85
aspen_v3_H100_performance --effectiveness--> 0.9911752
aspen_v3_H100_performance --hotSideDuty_kW--> 115.5827
aspen_v3_H100_performance --coldOutlet_C--> 119.3414
aspen_v3_H100_performance --duty_kW--> 115.5627
aspen_v3_H100_performance --energyBalanceError_pct--> 0.03452101
aspen_v3_H100_performance --ua_W_K--> 3517.69
aspen_v3_H100_performance --inCase--> case_aspen_v3
V102 --label--> V102
V102 --note--> Steam side of H100. Closed in the stripping loop test: no steam (REPORT Fig E.1).
V102 --feedsInto--> FT101
V102 --tag--> V102
V102 --pipedTo--> FT101
V102 --type--> ManualValve
V102 --normalPosition--> closed
V102 --gridReference--> L4
V102 --valveType--> ball
V102 --floor--> 1
FT100 --feedsInto--> V102
FT100 --pipedTo--> V102
PROC_stripping_loop_lineup_step_08 --operatesOn--> V102
PROC_H100_steam_bypass_step_05 --operatesOn--> V102
HAZOP_element_13 --covers--> V102
case_aspen_v6_1 --converged--> false
case_aspen_v6_1 --representsMode--> FigureOfEight
case_aspen_v6_1 --savedOn--> Thu Feb 27 15:14:32 2025
case_aspen_v6_1 --recommendedForUse--> false
case_aspen_v6_1 --aspenFile--> ABB_pilot_plant_final_6_1_SA_validation.apwz
case_aspen_v6_1 --label--> ABB_pilot_plant_final_6_1_SA_validation
case_aspen_v6_1 --aspenVersion--> 37.0
case_aspen_v6_1 --note--> Rescaled to pilot conditions with a sensitivity study for validation. Saved results did not converge: E100 RateSep failed, H100 invalid input, C100 temperature crossover, recycle opened at S3BACKUP.
case_aspen_v6_1 --type--> SimulationCase
aspen_v6_1_block_E100 --inCase--> case_aspen_v6_1
aspen_v6_1_block_C400COND --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S21 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_PURGE --inCase--> case_aspen_v6_1
aspen_v6_1_E100_stage_02 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S4 --inCase--> case_aspen_v6_1
aspen_v6_1_stream_S17 --inCase--> case_aspen_v6_1
```

Question: Temperature and pressure around H100 rise sharply and a blockage is suspected. What is the documented bypass procedure?

## Q79

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
K101 --type--> Saturator
K101 --label--> K101 gas saturator
K101 --pipedTo--> SDV170
K101 --pipedTo--> Z103
K101 --floor--> 1
K101 --feedsInto--> E101_N_gas_inlet
K101 --pipedTo--> E101_N_gas_inlet
K101 --note--> Saturates the feed gas with water before E101; temperature held by TIC121 using C106 on the recirculating water. Grid not in the REPORT lists (near L17 to L18 on the P&ID). Not modelled in Aspen (GOI09).
K101 --pipedTo--> V126
K101 --tag--> K101
DI_CARTRIDGE --feedsInto--> K101
HAZOP_4_06 --concerns--> K101
V172 --pipedTo--> K101
J102 --pipedTo--> K101
limit_LZAL_K101 --appliesTo--> K101
HAZOP_4_07 --concerns--> K101
LT104 --monitors--> K101
HAZOP_3_05 --concerns--> K101
FEED_GAS_HEADER --feedsInto--> K101
GOI09 --about--> K101
LI106 --monitors--> K101
FEED_GAS_HEADER --pipedTo--> K101
limit_LAL_K101 --appliesTo--> K101
K101_N2_recycle --fromItem--> K101
limit_LZAH_K101 --appliesTo--> K101
GOI07 --about--> K101
GOI02 --about--> K101
HAZOP_element_3 --covers--> K101
HAZOP_4_02 --concerns--> K101
TI121 --monitors--> K101
C106 --pipedTo--> K101
K103_CO2_recycle --bypasses--> K101
TT121 --monitors--> K101
DI_CARTRIDGE --pipedTo--> K101
J102 --feedsInto--> K101
V172 --feedsInto--> K101
N2ReturnLoop --hasStep--> N2ReturnLoop_step_00_E101
N2ReturnLoop --hasStep--> N2ReturnLoop_step_02_K402
N2ReturnLoop --hasStep--> N2ReturnLoop_step_15_E101_N_gas_inlet
N2ReturnLoop --inMode--> FigureOfEight
N2ReturnLoop --hasStep--> N2ReturnLoop_step_01_E101_N_gas_outlet
N2ReturnLoop --hasStep--> N2ReturnLoop_step_05_FT303
N2ReturnLoop --hasStep--> N2ReturnLoop_step_16_E101
N2ReturnLoop --hasStep--> N2ReturnLoop_step_13_FT107
N2ReturnLoop --hasStep--> N2ReturnLoop_step_07_FT304
N2ReturnLoop --note--> N2 is not absorbed, so it is recirculated: J102 blows it from the K402 overhead back through K101 into E101. Fresh N2 and CO2 (piece 5) top it up. FCV111 recycles part of it from K101 back to K102 to set the N2 flow into E101.
N2ReturnLoop --hasStep--> N2ReturnLoop_step_03_K402_N_gas_to_return
N2ReturnLoop --hasStep--> N2ReturnLoop_step_10_V187
N2ReturnLoop --hasStep--> N2ReturnLoop_step_04_TT304
N2ReturnLoop --label--> N2 return loop (E101 > K402 > K102 > J102 > K101 > E101)
N2ReturnLoop --hasStep--> N2ReturnLoop_step_12_TT114
N2ReturnLoop --hasStep--> N2ReturnLoop_step_08_FI304
N2ReturnLoop --hasStep--> N2ReturnLoop_step_14_K101
N2ReturnLoop --hasStep--> N2ReturnLoop_step_06_FI303
N2ReturnLoop --hasStep--> N2ReturnLoop_step_09_K102
N2ReturnLoop --type--> Loop
N2ReturnLoop --hasStep--> N2ReturnLoop_step_11_J102
FCV111 --floor--> 1
FCV111 --valveType--> flow control
FCV111 --tag--> FCV111
FCV111 --pipedTo--> K102
FCV111 --label--> FCV111
FCV111 --gridReference--> K17
FCV111 --type--> FlowControlValve
FCV111 --normalPosition--> open
FCV111 --note--> Recycles N2 from K101 back to K102, reducing the recycled N2 entering E101 (REPORT D.4, Fig D.6/D.7). Controlled by FIC303/FIC304 from FT303/FT304 on the N2 recycle pipe.
FIC304 --controls--> FCV111
K101_N2_recycle --routeVia--> FCV111
SDV170 --pipedTo--> FCV111
CL_N2_to_E101 --hasFinalElement--> FCV111
FIC303 --controls--> FCV111
N2ReturnLoop_step_11_J102 --label--> N2 return loop (E101 > K402 > K102 > J102 > K101 > E101) step 11: J102
N2ReturnLoop_step_11_J102 --stepItem--> J102
N2ReturnLoop_step_11_J102 --stepIndex--> 11
N2ReturnLoop_step_11_J102 --type--> LoopStep
N2ReturnLoop_step_11_J102 --stepType--> inline
NRV100b --type--> CheckValve
NRV100b --gridReference--> Q19
NRV100b --note--> Bottom right (make-up water to K101?). FI03
NRV100b --feedsInto--> DI_CARTRIDGE
NRV100b --pipedTo--> DI_CARTRIDGE
NRV100b --valveType--> check
NRV100b --label--> NRV100b
NRV100b --tag--> NRV100b
NRV100b --floor--> 1
NRV100a --feedsInto--> NRV100b
NRV100a --pipedTo--> NRV100b
N2ReturnLoop_step_04_TT304 --stepType--> tie-in
N2ReturnLoop_step_04_TT304 --type--> LoopStep
N2ReturnLoop_step_04_TT304 --label--> N2 return loop (E101 > K402 > K102 > J102 > K101 > E101) step 4: TT304
N2ReturnLoop_step_04_TT304 --stepIndex--> 4
N2ReturnLoop_step_04_TT304 --stepItem--> TT304
TT107 --label--> TT107
TT107 --signalType--> Fieldbus
TT107 --sensorType--> PRT
TT107 --floor--> 1
TT107 --measuredVariable--> gas entering E101 (after K101)
TT107 --monitors--> E101
TT107 --type--> TemperatureInstrument
TT107 --gridReference--> K18
TT107 --tag--> TT107
HAZOP_10_03 --label--> HAZOP 10.3
HAZOP_10_03 --consequence--> Overpressure lower section of E101 and K101
HAZOP_10_03 --actionTaken--> RV added
HAZOP_10_03 --itemNumber--> 3
HAZOP_10_03 --inElement--> HAZOP_element_10
HAZOP_10_03 --parameter--> FLOW
HAZOP_10_03 --cause--> High rate of gas up column from CO2 and N2 feed system
HAZOP_10_03 --type--> HazopDeviation
HAZOP_10_03 --concerns--> E101
HAZOP_10_03 --recommendedAction--> RV at outlet to K101?
HAZOP_10_03 --guideword--> MORE
N2ReturnLoop_step_05_FT303 --stepItem--> FT303
N2ReturnLoop_step_05_FT303 --type--> LoopStep
N2ReturnLoop_step_05_FT303 --stepType--> inline
N2ReturnLoop_step_05_FT303 --label--> N2 return loop (E101 > K402 > K102 > J102 > K101 > E101) step 5: FT303
N2ReturnLoop_step_05_FT303 --stepIndex--> 5
HAZOP_4_06 --cause--> As K101
HAZOP_4_06 --parameter--> TEMP.
HAZOP_4_06 --label--> HAZOP 4.6
HAZOP_4_06 --itemNumber--> 6
HAZOP_4_06 --type--> HazopDeviation
HAZOP_4_06 --inElement--> HAZOP_element_4
HAZOP_4_06 --guideword--> HIGHER
N2ReturnLoop_step_10_V187 --stepItem--> V187
N2ReturnLoop_step_10_V187 --stepType--> branch
N2ReturnLoop_step_10_V187 --label--> N2 return loop (E101 > K402 > K102 > J102 > K101 > E101) step 10: V187
N2ReturnLoop_step_10_V187 --stepIndex--> 10
N2ReturnLoop_step_10_V187 --type--> LoopStep
GOI09 --foundBy--> gas section build, Oct 2026
GOI09 --itemStatus--> open
GOI09 --label--> GOI09: Aspen feeds the gas straight into E101 with no K101 saturator
GOI09 --description--> Aspen feeds the gas straight into E101 with no K101 saturator
GOI09 --resolvedBy--> Note for model comparison
GOI09 --type--> OpenItem
limit_LZAH_K101 --type--> OperatingLimit
limit_LZAH_K101 --variable--> level
limit_LZAH_K101 --unit--> -
limit_LZAH_K101 --limitType--> alarm
limit_LZAH_K101 --source--> HAZOP element 3, item 5 (LZAH104, now LZAH103; soft high alarm added)
limit_LZAH_K101 --valueVerified--> false
limit_LZAH_K101 --label--> LZAH_K101
SDV170 --gridReference--> K17
SDV170 --label--> SDV170
SDV170 --valveType--> shutdown (solenoid-operated)
SDV170 --tag--> SDV170
SDV170 --type--> ShutdownValve
SDV170 --floor--> 1
SDV170 --note--> On the FCV111 recycle line from K101 to K102 (P&ID shows SDV170 with HS170 next to FCV111); the REPORT lists it as SOV170.
K101_N2_recycle --routeVia--> SDV170
```

Question: A significant nitrogen or carbon dioxide release occurs near the gas mixing system K101. What safeguards and operator actions apply?

## Q80

Answer the question using ONLY the facts below from the plant knowledge graph. Cite the facts you use. If the facts are not enough, say what is missing.

Facts:
```
J105 --note--> Speed-controlled with limited maximum flow (HAZOP 9a.4); check valves downstream (9a.6); thermal trip (9b.1); dry-run protection (9a.3); stopped by the liquid flow switch at the manual vent V138 (9a.7).
J105 --gridReference--> N4
J105 --label--> J105 MEA filling / draining pump
J105 --floor--> 1
J105 --feedsInto--> FILL_DRAIN_HEADER
J105 --type--> Pump
J105 --pipedTo--> FILL_DRAIN_HEADER
J105 --tag--> J105
HAZOP_9a_11 --concerns--> J105
HAZOP_element_9b --covers--> J105
MS03 --about--> J105
limit_TRIP_J105_dry_run --appliesTo--> J105
F100 --pipedTo--> J105
HAZOP_9b_04 --concerns--> J105
F100 --feedsInto--> J105
limit_TRIP_J105_thermal --appliesTo--> J105
TT116 --monitors--> J105
limit_TRIP_J105_liquid_at_vent --appliesTo--> J105
HAZOP_9a_07 --concerns--> J105
HAZOP_9a_01 --concerns--> J105
HAZOP_element_9a --covers--> J105
MS02 --about--> J105
MS04 --description--> Role of PCV126 on the J105 discharge (spillback or back-pressure)
MS04 --foundBy--> mea section build, Oct 2026
MS04 --label--> MS04: Role of PCV126 on the J105 discharge (spillback or back-pressure)
MS04 --type--> OpenItem
MS04 --itemStatus--> open
MS04 --resolvedBy--> Trace on the P&ID
MS04 --about--> PCV126
J105__meacit03 --document--> SRC_HAZOP
J105__meacit03 --type--> Citation
J105__meacit03 --citationText--> HAZOP 2010 element 9a, items 1 to 7; element 9b, items 1, 2 and 4
J105__meacit03 --label--> Citation 3 for J105 (mea)
J105__meacit03 --location--> element 9a, items 1 to 7; element 9b, items 1, 2 and 4
MS05 --resolvedBy--> Full-size P&ID
MS05 --itemStatus--> open
MS05 --foundBy--> mea section build, Oct 2026
MS05 --about--> V138
MS05 --description--> V138 (manual vent 'valve N') and the liquid flow switch that stops J105 are not in the REPORT lists
MS05 --type--> OpenItem
MS05 --label--> MS05: V138 (manual vent 'valve N') and the liquid flow switch that stops J105 are not in the REPORT lists
HAZOP_element_9b --elementNumber--> 9b
HAZOP_element_9b --type--> HazopElement
HAZOP_element_9b --covers--> V147a
HAZOP_element_9b --covers--> V146a
HAZOP_element_9b --covers--> R100
HAZOP_element_9b --label--> HAZOP element 9b: FILLING / EMPTYING Line - DRAINING
HAZOP_element_9b --source--> HAZOP study, 6-7 May 2010 (27794_Plant_HAZREP_1.xls)
HAZOP_element_9b --covers--> V146b
HAZOP_element_9b --covers--> V147b
HAZOP_9b_02 --inElement--> HAZOP_element_9b
HAZOP_9b_03 --inElement--> HAZOP_element_9b
HAZOP_9b_06 --inElement--> HAZOP_element_9b
HAZOP_9b_04 --inElement--> HAZOP_element_9b
HAZOP_9b_05 --inElement--> HAZOP_element_9b
HAZOP_9b_01 --inElement--> HAZOP_element_9b
V138 --valveType--> manual vent
V138 --floor--> 1
V138 --label--> V138
V138 --note--> Manual vent ('valve N') on the filling line; a liquid flow switch on its right-hand side stops J105 (HAZOP 9a.7, 9b.4). Not in the REPORT lists (MS05).
V138 --tag--> V138
V138 --type--> ManualValve
HAZOP_element_9a --covers--> V138
HAZOP_9b_04 --concerns--> V138
HAZOP_9a_07 --concerns--> V138
MEAFillRoute_step_02_TT116 --stepIndex--> 2
MEAFillRoute_step_02_TT116 --stepItem--> TT116
MEAFillRoute_step_02_TT116 --label--> MEA filling route (feed tank > J105 > fill/drain header) step 2: TT116
MEAFillRoute_step_02_TT116 --stepType--> tie-in
MEAFillRoute_step_02_TT116 --type--> LoopStep
J105__meacit01 --location--> grid N4
J105__meacit01 --type--> Citation
J105__meacit01 --document--> SRC_PID
J105__meacit01 --label--> Citation 1 for J105 (mea)
J105__meacit01 --citationText--> P&ID grid N4
HAZOP_9a_11 --cause--> Wrong tank is attached to J105
HAZOP_9a_11 --label--> HAZOP 9a.11
HAZOP_9a_11 --itemNumber--> 11
HAZOP_9a_11 --type--> HazopDeviation
HAZOP_9a_11 --guideword--> INCORRECT
HAZOP_9a_11 --parameter--> COMPOSITION
HAZOP_9a_11 --inElement--> HAZOP_element_9a
HAZOP_9a_11 --safeguard--> SOP
NRV104 --tag--> NRV104
NRV104 --note--> On the N2 line to the long horizontal line towards the J105 filling system (team trace, P&ID label). The 2010 HAZOP put NRV104 on the CO2 return (6.3/6.5); tags were renumbered after 2010 (GR11).
NRV104 --gridReference--> O18
NRV104 --floor--> 1
NRV104 --type--> CheckValve
NRV104 --valveType--> check
NRV104 --label--> NRV104
NRV104 --normalPosition--> open
HAZOP_6_05 --concerns--> NRV104
HAZOP_6_03 --concerns--> NRV104
GR11 --about--> NRV104
N2_PURGE_HEADER --pipedTo--> NRV104
MS09 --about--> R100
MS09 --description--> HAZOP note M26: the area around B100 (now F100/R100) was not covered by the 2010 HAZOP
MS09 --label--> MS09: HAZOP note M26: the area around B100 (now F100/R100) was not covered by the 2010 HAZOP
MS09 --itemStatus--> open
MS09 --about--> F100
MS09 --resolvedBy--> Note
MS09 --foundBy--> mea section build, Oct 2026
MS09 --type--> OpenItem
FILL_DRAIN_HEADER --label--> MEA fill / drain header (long horizontal line along the bottom of the drawing)
FILL_DRAIN_HEADER --pipedTo--> V122
FILL_DRAIN_HEADER --tag--> FILL_DRAIN_HEADER
FILL_DRAIN_HEADER --note--> Untagged. Connects J105 and the tanks to the plant drains and fill points (MS07, MS08).
FILL_DRAIN_HEADER --pipedTo--> R100
FILL_DRAIN_HEADER --type--> PipeSegment
FILL_DRAIN_HEADER --floor--> 1
FILL_DRAIN_HEADER --pipedTo--> V115
V126 --pipedTo--> FILL_DRAIN_HEADER
MS07 --about--> FILL_DRAIN_HEADER
V168 --pipedTo--> FILL_DRAIN_HEADER
V147a --pipedTo--> FILL_DRAIN_HEADER
V167 --pipedTo--> FILL_DRAIN_HEADER
V146a --pipedTo--> FILL_DRAIN_HEADER
V148 --pipedTo--> FILL_DRAIN_HEADER
V149 --pipedTo--> FILL_DRAIN_HEADER
V147b --pipedTo--> FILL_DRAIN_HEADER
HAZOP_element_9a --covers--> FILL_DRAIN_HEADER
MS08 --about--> FILL_DRAIN_HEADER
V160 --pipedTo--> FILL_DRAIN_HEADER
V153 --pipedTo--> FILL_DRAIN_HEADER
V154 --pipedTo--> FILL_DRAIN_HEADER
V155 --pipedTo--> FILL_DRAIN_HEADER
V146b --pipedTo--> FILL_DRAIN_HEADER
J105__meacit02 --label--> Citation 2 for J105 (mea)
J105__meacit02 --type--> Citation
J105__meacit02 --document--> SRC_REPORT
J105__meacit02 --citationText--> Pilot Plant Report pump list (J105, floor 1, N4)
J105__meacit02 --location--> pump list (J105, floor 1, N4)
TT116 --signalType--> 4-20mA
TT116 --type--> TemperatureInstrument
TT116 --measuredVariable--> MEA temperature at J105
TT116 --sensorType--> PRT
TT116 --label--> TT116
TT116 --tag--> TT116
TT116 --floor--> 1
TT116 --gridReference--> N5
F100 --floor--> 1
F100 --note--> Feed tank for filling the plant (HAZOP M9 'one feed, one receiver'; low-level trip M17). DIFF: the R100 and F100 labels are swapped on the P&ID (N2 and N3), so this is the tank drawn as R100 (MS01).
F100 --type--> StorageTank
F100 --tag--> F100
F100 --label--> F100 MEA feed tank
F100 --gridReference--> N2
PI112 --monitors--> F100
discrepancy_R100_F100_labels --concerns--> F100
NRV107 --feedsInto--> F100
MS06 --about--> F100
```

Question: During MEA filling, the storage or supply vessel B100 becomes empty while J105 is running. What hazards and protective actions are identified?
