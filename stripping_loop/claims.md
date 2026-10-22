# Stripping loop KG: claims for independent verification

## Loop route (inline items in flow order)

E100 draw-off nozzle below TT103 (chimney tray, to H100) > FT102 > Q105 > H100 > Q106 > E100 sump return nozzle from H100 (below chimney tray) > E100 > E100 sump outlet nozzle (to V110) > V110 > V112 > C100 > V113a > V113b > J100 > PCV122 > V116 > V117a > Z102 > V117b > V121 > FT103 > FT104 > SDV125 > H200a > H200b > V403 > V402 > E100 top inlet nozzle after V402 (above top packed bed) > E100


## B101 (PulsationDampener)

1. B101 is step 22 of the stripping loop route.
2. B101: floor = 1
   - KG sources: P&ID differences row PT104 & B101 (M10); P&ID grid M10; Team check order TT106 > B101 > PT104 > PCV122 > V116 confirmed

## C100 (LeanRichExchanger)

3. C100 is step 16 of the stripping loop route.
4. C100: feedsInto = V113a
5. C100: floor = 1
6. C100: pipedTo = V113a
7. C100: source = SUMMARY p.106; REPORT section 3
   - KG sources: Aspen v3 block C100; P&ID interchanger C100, grid M8 to M9; Pilot Plant Report section 3; Plant summary 2023-24 p.106

## DI100 (FlowInstrument)

8. DI100 is step 3 of the stripping loop route.
9. DI100: floor = 1
10. DI100: measuredVariable = density indication (from FT102)
11. DI100: monitors = H100
   - KG sources: P&ID on FT102, grid M6; Team check tag is DI100, not DE100

## E100 (StrippingColumn)

12. E100 is step 10, 42 of the stripping loop route.
13. E100: designBasis = Designed for sub-atmospheric pressure (vacuum), per HAZOP element 11 item 10. Design pressure value not documented.
14. E100: diameter_mm = 264.62
15. E100: feedsInto = E100_N_drawoff
16. E100: feedsInto = E100_N_sump_outlet
17. E100: floor = 1
18. E100: pipedTo = E100_N_drawoff
19. E100: pipedTo = E100_N_sump_outlet
   - KG sources: Aspen v3 block E100 (RadFrac internals); HAZOP 2010 element 11, item 10 (designed for sub-atmospheric pressure); P&ID column E100, grids F7 to K8

## FCV110 (FlowControlValve)

20. FCV110: floor = 1
21. FCV110: gridReference = L5
22. FCV110: normalPosition = closed
23. FCV110: valveType = flow control
   - KG sources: P&ID differences row FCV110 (L5); P&ID grid L5; Pilot Plant Report Fig E.1 and section F.5.4.3; Plant summary 2023-24 p.190 (control-loop table)

## FI102 (FlowInstrument)

24. FI102 is step 2 of the stripping loop route.
25. FI102: floor = 1
26. FI102: gridReference = M6
27. FI102: measuredVariable = mass flow indication
28. FI102: monitors = H100
   - KG sources: P&ID grid M6; Pilot Plant Report Appendix B instrument list (M6, floor 1)

## FI103 (FlowInstrument)

29. FI103 is step 32 of the stripping loop route.
30. FI103: floor = 1
31. FI103: measuredVariable = flow indication
32. FI103: monitors = J100
   - KG sources: P&ID grid L12; Pilot Plant Report Appendix B instrument list (M12, floor 1)

## FI104 (FlowInstrument)

33. FI104 is step 34 of the stripping loop route.
34. FI104: floor = 1
35. FI104: measuredVariable = flow indication
36. FI104: monitors = J100
   - KG sources: P&ID grid L12; Pilot Plant Report Appendix B instrument list (M12, floor 1)

## FIC100 (Controller)

37. FIC100: controls = FCV110
   - KG sources: Plant summary 2023-24 p.190 (control-loop table)

## FIC103 (Controller)

38. FIC103: controls = J100
   - KG sources: P&ID below J100, grid M10; Plant summary 2023-24 p.190 (control-loop table); Team check J100 motor M > SIC100 > HS100 > FIC103

## FIC104 (Controller)

39. FIC104: controls = J100
   - KG sources: Plant summary 2023-24 p.190 (control-loop table)

## FT100 (FlowInstrument)

40. FT100: floor = 1
41. FT100: gridReference = L4
42. FT100: measuredVariable = steam flow to H100
43. FT100: monitors = H100
44. FT100: sensorType = orifice flow meter
45. FT100: signalType = Profibus-PA
   - KG sources: P&ID grid L4; Pilot Plant Report Appendix B instrument list

## FT101 (FlowInstrument)

46. FT101: floor = 1
47. FT101: gridReference = L5
48. FT101: measuredVariable = steam flow to H100
49. FT101: monitors = H100
50. FT101: sensorType = swirl volumetric flow meter
51. FT101: signalType = Profibus-PA
   - KG sources: P&ID grid L5; Pilot Plant Report Appendix B instrument list

## FT102 (FlowInstrument)

52. FT102 is step 1 of the stripping loop route.
53. FT102: feedsInto = Q105
54. FT102: floor = 1
55. FT102: gridReference = M6
56. FT102: measuredVariable = mass flow, density and temperature
57. FT102: monitors = H100
58. FT102: pipedTo = Q105
59. FT102: sensorType = Coriolis mass flow meter
60. FT102: signalType = Profibus-PA
   - KG sources: P&ID grid M6; Pilot Plant Report Appendix B instrument list

## FT103 (FlowInstrument)

61. FT103 is step 31 of the stripping loop route.
62. FT103: feedsInto = FT104
63. FT103: floor = 1
64. FT103: gridReference = L12
65. FT103: measuredVariable = volumetric flow
66. FT103: monitors = J100
67. FT103: pipedTo = FT104
68. FT103: sensorType = electromagnetic volumetric flow meter
69. FT103: signalType = 4-20mA
   - KG sources: P&ID grid L12; Pilot Plant Report Appendix B instrument list; Team check flow V121 > FT103 > FT104

## FT104 (FlowInstrument)

70. FT104 is step 33 of the stripping loop route.
71. FT104: feedsInto = SDV125
72. FT104: floor = 1
73. FT104: gridReference = L12
74. FT104: measuredVariable = volumetric flow
75. FT104: monitors = J100
76. FT104: pipedTo = SDV123
77. FT104: pipedTo = SDV125
78. FT104: sensorType = swirl volumetric flow meter
79. FT104: signalType = Fieldbus
   - KG sources: P&ID grid L12; Pilot Plant Report Appendix B instrument list; Team check flow V121 > FT103 > FT104

## FT305 (FlowInstrument)

80. FT305: floor = 3
81. FT305: gridReference = F9
82. FT305: measuredVariable = mass flow (reflux from J300)
83. FT305: sensorType = Coriolis mass flow meter
84. FT305: signalType = Profibus-PA
   - KG sources: P&ID grid F9; Pilot Plant Report Appendix B instrument list

## H100 (SteamReboiler)

85. H100 is step 5 of the stripping loop route.
86. H100: feedsInto = Q106
87. H100: floor = 1
88. H100: pipedTo = Q106
89. H100: source = SUMMARY p.102
   - KG sources: Aspen v3 blocks H100REAC and H100HEAT; P&ID reboiler H100, near grid L6; Plant summary 2023-24 p.102

## H200a (ElectricHeater)

90. H200a is step 36 of the stripping loop route.
91. H200a: feedsInto = V403
92. H200a: floor = 2
93. H200a: gridReference = J10
94. H200a: pipedTo = V309
95. H200a: pipedTo = V403
   - KG sources: P&ID heater control section (grids J9 to J11); Pilot Plant Report start-up tables, heater H200a (J10, floor 2)

## H200b (ElectricHeater)

96. H200b is step 36 of the stripping loop route.
97. H200b: feedsInto = V403
98. H200b: floor = 2
99. H200b: gridReference = J11
100. H200b: pipedTo = V309
101. H200b: pipedTo = V403
   - KG sources: P&ID heater control section (grids J9 to J11); Pilot Plant Report start-up tables, heater H200b (J11, floor 2)

## HS100 (Controller)

102. HS100: controls = J100
   - KG sources: Original P&ID 2010 J100 controls; P&ID below J100, grid M10; Team check J100 motor M > SIC100 > HS100 > FIC103

## HS200a (Controller)

103. HS200a: controls = H200a
   - KG sources: P&ID heater control section (grids J9 to J11)

## HS200b (Controller)

104. HS200b: controls = H200b
   - KG sources: P&ID heater control section (grids J9 to J11)

## J100 (Pump)

105. J100 is step 20 of the stripping loop route.
106. J100: feedsInto = PCV122
107. J100: floor = 1
108. J100: gridReference = M10
109. J100: pipedTo = PCV122
110. J100: pipedTo = RV101
   - KG sources: P&ID grid M10; Pilot Plant Report section 2.5 (pump trials)

## LSHH100 (LevelInstrument)

111. LSHH100: floor = 1
112. LSHH100: locatedAtStage = E100_stage_12
113. LSHH100: measuredVariable = level high-high switch
114. LSHH100: monitors = E100
   - KG sources: P&ID E100 sump, left-hand side; Team check left-hand side of E100 sump

## LSLL102 (LevelInstrument)

115. LSLL102: floor = 1
116. LSLL102: locatedAtStage = E100_stage_12
117. LSLL102: measuredVariable = level low-low switch
118. LSLL102: monitors = E100
   - KG sources: P&ID E100 sump, left-hand side; Team check left-hand side of E100 sump

## LT101 (LevelInstrument)

119. LT101: floor = 1
120. LT101: gridReference = K8
121. LT101: locatedAtStage = E100_stage_12
122. LT101: measuredVariable = level
123. LT101: monitors = E100
124. LT101: sensorType = differential pressure transmitter
125. LT101: signalType = Profibus-PA
   - KG sources: P&ID grid K8, E100 sump, left-hand side; Pilot Plant Report Appendix B instrument list; Team check left-hand side of E100 sump

## PCV119 (PressureControlValve)

126. PCV119: floor = 1
127. PCV119: gridReference = K19
128. PCV119: normalPosition = open
129. PCV119: valveType = pressure control
   - KG sources: Plant summary 2023-24 p.190 (control-loop table)

## PCV122 (PressureControlValve)

130. PCV122 is step 24 of the stripping loop route.
131. PCV122: feedsInto = V116
132. PCV122: floor = 1
133. PCV122: gridReference = M10
134. PCV122: normalPosition = open
135. PCV122: pipedTo = V116
136. PCV122: valveType = pressure control
   - KG sources: P&ID grid M10, after B101, set to 8 bar; Team check order TT106 > B101 > PT104 > PCV122 > V116 confirmed

## PDT105 (DifferentialPressureInstrument)

137. PDT105 is step 28 of the stripping loop route.
138. PDT105: floor = 1
139. PDT105: gridReference = M11
140. PDT105: measuredVariable = differential pressure across Z102
141. PDT105: monitors = Z102
142. PDT105: sensorType = differential pressure transmitter
143. PDT105: signalType = Profibus-PA
   - KG sources: P&ID grid M11; Pilot Plant Report Appendix B instrument list

## PIC401 (Controller)

144. PIC401: controls = PCV119
   - KG sources: Plant summary 2023-24 p.190 (control-loop table)

## PIC402 (Controller)

145. PIC402: controls = PCV119
   - KG sources: Plant summary 2023-24 p.190 (control-loop table)

## PSHH116 (PressureInstrument)

146. PSHH116: floor = 1
147. PSHH116: locatedAtStage = E100_stage_11
148. PSHH116: measuredVariable = pressure high-high switch
149. PSHH116: monitors = E100
   - KG sources: HAZOP 2010 recommendation M4 (PSH on E100 trips the plant at 2 barg); P&ID E100 base, right-hand side; Team check right-hand side of E100

## PSHH400 (PressureInstrument)

150. PSHH400: floor = 4
151. PSHH400: locatedAtStage = E100_stage_01
152. PSHH400: measuredPhase = vapour
153. PSHH400: measuredVariable = pressure high-high switch
154. PSHH400: monitors = E100
   - KG sources: HAZOP 2010 recommendation M4 (PSH on E100 trips the plant at 2 barg); P&ID E100 top, grid F7

## PT102 (PressureInstrument)

155. PT102: floor = 1
156. PT102: gridReference = K8
157. PT102: locatedAtStage = E100_stage_12
158. PT102: measuredVariable = pressure
159. PT102: monitors = E100
160. PT102: sensorType = gauge pressure transmitter
161. PT102: signalType = Profibus-PA
   - KG sources: P&ID grid K8, E100 sump, left-hand side; Pilot Plant Report Appendix B instrument list; Team check left-hand side of E100 sump

## PT103 (PressureInstrument)

162. PT103 is step 15 of the stripping loop route.
163. PT103: floor = 1
164. PT103: gridReference = M8
165. PT103: measuredVariable = pressure
166. PT103: monitors = C100
167. PT103: sensorType = gauge pressure transmitter
168. PT103: signalType = Profibus-PA
   - KG sources: P&ID grid M8, on the lean line near TT104 before C100; Pilot Plant Report Appendix B instrument list; Team check on the lean line from the E100 sump, near TT104, entering C100

## PT104 (PressureInstrument)

169. PT104 is step 23 of the stripping loop route.
170. PT104: floor = 1
171. PT104: gridReference = L10
172. PT104: measuredVariable = pressure
173. PT104: monitors = J100
174. PT104: sensorType = gauge pressure transmitter
175. PT104: signalType = Profibus-PA
   - KG sources: P&ID differences row PT104 & B101 (M10); P&ID grid L10; Pilot Plant Report Appendix B instrument list; Team check order TT106 > B101 > PT104 > PCV122 > V116 confirmed

## PT401 (PressureInstrument)

176. PT401: floor = 4
177. PT401: gridReference = C8
178. PT401: measuredVariable = E100 overhead pressure
179. PT401: monitors = E100
180. PT401: sensorType = gauge pressure transmitter
181. PT401: signalType = Profibus-PA
   - KG sources: P&ID grid C8; Pilot Plant Report Appendix B instrument list

## PT402 (PressureInstrument)

182. PT402: floor = 4
183. PT402: gridReference = C16
184. PT402: measuredVariable = pressure after K401
185. PT402: monitors = E100
186. PT402: sensorType = gauge pressure transmitter
187. PT402: signalType = Fieldbus
   - KG sources: P&ID grid C16; Pilot Plant Report Appendix B instrument list

## Q105 (PipeSegment)

188. Q105 is step 4 of the stripping loop route.
189. Q105: feedsInto = H100
190. Q105: pipedTo = H100
   - KG sources: P&ID line Q105, near grid M6; Team check reboiler circuit trace

## Q106 (PipeSegment)

191. Q106 is step 8 of the stripping loop route.
192. Q106: feedsInto = E100_N_reboiler_return
193. Q106: pipedTo = E100_N_reboiler_return
   - KG sources: P&ID line Q106, grids L6 to L7; Team check Q106 returns from H100 to E100

## RV101 (ReliefValve)

194. RV101: floor = 1
195. RV101: gridReference = L10
196. RV101: normalPosition = closed
197. RV101: protects = J100
198. RV101: valveType = relief
   - KG sources: HAZOP 2010 element 7, item 14; P&ID grid L10

## RV401 (ReliefValve)

199. RV401: floor = 4
200. RV401: gridReference = F7
201. RV401: normalPosition = closed
202. RV401: protects = E100
203. RV401: valveType = relief
   - KG sources: P&ID differences row K403 (E7); P&ID grid F7

## SDV123 (ShutdownValve)

204. SDV123: floor = 1
205. SDV123: gridReference = L9
206. SDV123: normalPosition = closed
207. SDV123: valveType = shutdown (solenoid-operated)
   - KG sources: P&ID grid L9, tagged SDV123; Pilot Plant Report Fig E.1/E.2 (stripping loop commissioning line-up) (listed as SOV123)

## SDV125 (ShutdownValve)

208. SDV125 is step 35 of the stripping loop route.
209. SDV125: feedsInto = H200a
210. SDV125: feedsInto = H200b
211. SDV125: floor = 1
212. SDV125: gridReference = L11
213. SDV125: normalPosition = open
214. SDV125: pipedTo = H200a
215. SDV125: pipedTo = H200b
216. SDV125: valveType = shutdown (solenoid-operated)
   - KG sources: P&ID grid L11, tagged SDV125; Pilot Plant Report Fig E.1/E.2 (stripping loop commissioning line-up) (listed as SOV125); Team check tag is SDV125 on the P&ID

## SIC100 (Controller)

217. SIC100: controls = J100
   - KG sources: Original P&ID 2010 J100 controls; P&ID below J100, grid M10; Plant summary 2023-24 p.190 (control-loop table); Team check J100 motor M > SIC100 > HS100 > FIC103

## TE105 (TemperatureInstrument)

218. TE105 is step 17 of the stripping loop route.
219. TE105: floor = 1
220. TE105: gridReference = M9
221. TE105: measuredVariable = temperature
222. TE105: monitors = C100
223. TE105: sensorType = PRT
224. TE105: signalType = Profibus-PA
   - KG sources: P&ID grid M9 (tagged TE105); Pilot Plant Report Appendix B lists it as TT105; Appendix D calls it TE105

## TI100 (TemperatureInstrument)

225. TI100 is step 7 of the stripping loop route.
226. TI100: floor = 1
227. TI100: gridReference = K6
228. TI100: measuredVariable = temperature indication
229. TI100: monitors = H100
   - KG sources: P&ID grid K6; Pilot Plant Report Appendix B instrument list (K6, floor 1)

## TI213 (TemperatureInstrument)

230. TI213 is step 38 of the stripping loop route.
231. TI213: floor = 2
232. TI213: gridReference = H10
233. TI213: measuredVariable = temperature indication
   - KG sources: P&ID heater control section; Pilot Plant Report Appendix B instrument list (H10, floor 2) and section E.3.4.1

## TIC100 (Controller)

234. TIC100: controls = FCV110
   - KG sources: Plant summary 2023-24 p.190 (control-loop table)

## TIC213a (Controller)

235. TIC213a: controls = H200a
   - KG sources: P&ID heater control section (grids J9 to J11); Plant summary 2023-24 p.190 (control-loop table)

## TIC213b (Controller)

236. TIC213b: controls = H200b
   - KG sources: P&ID heater control section (grids J9 to J11); Plant summary 2023-24 p.190 (control-loop table)

## TSHH212a (TemperatureInstrument)

237. TSHH212a: floor = 2
238. TSHH212a: measuredVariable = temperature high-high switch
239. TSHH212a: monitors = H200a
   - KG sources: P&ID heater control section (grids J9 to J11)

## TSHH212b (TemperatureInstrument)

240. TSHH212b: floor = 2
241. TSHH212b: measuredVariable = temperature high-high switch
242. TSHH212b: monitors = H200b
   - KG sources: P&ID heater control section (grids J9 to J11)

## TT100 (TemperatureInstrument)

243. TT100 is step 6 of the stripping loop route.
244. TT100: floor = 1
245. TT100: gridReference = L6
246. TT100: measuredVariable = temperature of MEA leaving H100
247. TT100: monitors = H100
248. TT100: sensorType = PRT
249. TT100: signalType = Profibus-PA
   - KG sources: P&ID on line Q106, grid L6; Pilot Plant Report Appendix B instrument list; Team check TT100 confirmed on Q106

## TT103 (TemperatureInstrument)

250. TT103: floor = 1
251. TT103: gridReference = J7
252. TT103: locatedAtStage = E100_stage_11
253. TT103: measuredVariable = temperature
254. TT103: monitors = E100
255. TT103: sensorType = PRT
256. TT103: signalType = Profibus-PA
   - KG sources: P&ID grid J7, left-hand side of E100; Pilot Plant Report Appendix B instrument list; Team check left-hand side of E100

## TT104 (TemperatureInstrument)

257. TT104 is step 14 of the stripping loop route.
258. TT104: floor = 1
259. TT104: gridReference = M8
260. TT104: measuredVariable = temperature
261. TT104: monitors = C100
262. TT104: sensorType = PRT
263. TT104: signalType = Profibus-PA
   - KG sources: P&ID grid M8; Pilot Plant Report Appendix B instrument list; Team check next to PT103 on the lean line entering C100

## TT106 (TemperatureInstrument)

264. TT106 is step 21 of the stripping loop route.
265. TT106: floor = 1
266. TT106: gridReference = L10
267. TT106: measuredVariable = temperature
268. TT106: monitors = J100
269. TT106: sensorType = PRT
270. TT106: signalType = 4-20mA
   - KG sources: P&ID grid L10; Pilot Plant Report Appendix B instrument list; Team check TT106 confirmed at J100

## TT200 (TemperatureInstrument)

271. TT200: floor = 2
272. TT200: gridReference = J7
273. TT200: locatedAtStage = E100_stage_09
274. TT200: measuredPhase = liquid
275. TT200: measuredVariable = temperature
276. TT200: monitors = E100
277. TT200: sensorType = PRT
278. TT200: signalType = Profibus-PA
   - KG sources: P&ID grid J7; Pilot Plant Report Appendix B instrument list; Team check liquid measurement confirmed on full-size P&ID

## TT201 (TemperatureInstrument)

279. TT201: floor = 2
280. TT201: gridReference = J7
281. TT201: locatedAtStage = E100_stage_09
282. TT201: measuredPhase = vapour
283. TT201: measuredVariable = temperature
284. TT201: monitors = E100
285. TT201: sensorType = PRT
286. TT201: signalType = Profibus-PA
   - KG sources: P&ID column E100, grid J7 (tag hidden under marker 7); Pilot Plant Report Appendix B instrument list

## TT202 (TemperatureInstrument)

287. TT202: floor = 2
288. TT202: gridReference = H7
289. TT202: locatedAtStage = E100_stage_07
290. TT202: measuredPhase = liquid
291. TT202: measuredVariable = temperature
292. TT202: monitors = E100
293. TT202: sensorType = PRT
294. TT202: signalType = 4-20mA
   - KG sources: P&ID grid H7; Pilot Plant Report Appendix B instrument list; Team check liquid measurement confirmed on full-size P&ID

## TT203 (TemperatureInstrument)

295. TT203: floor = 2
296. TT203: gridReference = H7
297. TT203: locatedAtStage = E100_stage_07
298. TT203: measuredPhase = vapour
299. TT203: measuredVariable = temperature
300. TT203: monitors = E100
301. TT203: sensorType = PRT
302. TT203: signalType = 4-20mA
   - KG sources: P&ID grid H7; Pilot Plant Report Appendix B instrument list; Team check vapour measurement confirmed on full-size P&ID

## TT212a (TemperatureInstrument)

303. TT212a: floor = 2
304. TT212a: gridReference = J9
305. TT212a: measuredVariable = heater temperature
306. TT212a: monitors = H200a
307. TT212a: sensorType = K-type thermocouple
308. TT212a: signalType = 4-20mA
   - KG sources: P&ID grid J9; Pilot Plant Report Appendix B instrument list

## TT212b (TemperatureInstrument)

309. TT212b: floor = 2
310. TT212b: gridReference = J10
311. TT212b: measuredVariable = heater temperature
312. TT212b: monitors = H200b
313. TT212b: sensorType = K-type thermocouple
314. TT212b: signalType = 4-20mA
   - KG sources: P&ID grid J10; Pilot Plant Report Appendix B instrument list

## TT213 (TemperatureInstrument)

315. TT213 is step 37 of the stripping loop route.
316. TT213: floor = 2
317. TT213: gridReference = H13
318. TT213: measuredVariable = temperature of MEA leaving H200a/b
319. TT213: sensorType = PRT
320. TT213: signalType = Profibus-PA
   - KG sources: P&ID grid H13; Pilot Plant Report Appendix B instrument list

## TT300 (TemperatureInstrument)

321. TT300: floor = 3
322. TT300: gridReference = G7
323. TT300: locatedAtStage = E100_stage_05
324. TT300: measuredPhase = liquid
325. TT300: measuredVariable = temperature
326. TT300: monitors = E100
327. TT300: sensorType = PRT
328. TT300: signalType = 4-20mA
   - KG sources: P&ID grid G7; Pilot Plant Report Appendix B instrument list; Team check liquid measurement confirmed on full-size P&ID

## TT301 (TemperatureInstrument)

329. TT301: floor = 3
330. TT301: gridReference = G7
331. TT301: locatedAtStage = E100_stage_05
332. TT301: measuredPhase = vapour
333. TT301: measuredVariable = temperature
334. TT301: monitors = E100
335. TT301: sensorType = PRT
336. TT301: signalType = 4-20mA
   - KG sources: P&ID grid G7; Pilot Plant Report Appendix B instrument list; Team check vapour measurement confirmed on full-size P&ID

## TT302 (TemperatureInstrument)

337. TT302: floor = 3
338. TT302: gridReference = G7
339. TT302: locatedAtStage = E100_stage_03
340. TT302: measuredPhase = liquid
341. TT302: measuredVariable = temperature
342. TT302: monitors = E100
343. TT302: sensorType = PRT
344. TT302: signalType = Profibus-PA
   - KG sources: P&ID grid G7; Pilot Plant Report Appendix B instrument list; Team check liquid measurement confirmed on full-size P&ID

## TT303 (TemperatureInstrument)

345. TT303: floor = 3
346. TT303: gridReference = G7
347. TT303: locatedAtStage = E100_stage_03
348. TT303: measuredPhase = vapour
349. TT303: measuredVariable = temperature
350. TT303: monitors = E100
351. TT303: sensorType = PRT
352. TT303: signalType = Profibus-PA
   - KG sources: P&ID column E100, grid G7 (tag hidden under marker 6); Pilot Plant Report Appendix B instrument list

## TT309 (TemperatureInstrument)

353. TT309: floor = 3
354. TT309: gridReference = F9
355. TT309: measuredVariable = temperature (reflux from J300)
356. TT309: sensorType = PRT
357. TT309: signalType = Profibus-PA
   - KG sources: P&ID grid F9; Pilot Plant Report Appendix B instrument list

## TT400 (TemperatureInstrument)

358. TT400: floor = 4
359. TT400: gridReference = F7
360. TT400: locatedAtStage = E100_stage_01
361. TT400: measuredPhase = liquid
362. TT400: measuredVariable = temperature
363. TT400: monitors = E100
364. TT400: sensorType = PRT
365. TT400: signalType = Profibus-PA
   - KG sources: P&ID grid F7; Pilot Plant Report Appendix B instrument list; Team check liquid measurement confirmed on full-size P&ID

## TT401 (TemperatureInstrument)

366. TT401: floor = 4
367. TT401: gridReference = F7
368. TT401: locatedAtStage = E100_stage_01
369. TT401: measuredPhase = vapour
370. TT401: measuredVariable = temperature
371. TT401: monitors = E100
372. TT401: sensorType = PRT
373. TT401: signalType = Profibus-PA
   - KG sources: P&ID grid F7; Pilot Plant Report Appendix B instrument list; Team check vapour measurement confirmed on full-size P&ID

## TY213a (Controller)

374. TY213a: controls = H200a
   - KG sources: P&ID heater control section (grids J9 to J11)

## TY213b (Controller)

375. TY213b: controls = H200b
   - KG sources: P&ID heater control section (grids J9 to J11)

## TZAHH212a (Controller)

376. TZAHH212a: controls = H200a
   - KG sources: P&ID heater control section (grids J9 to J11)

## TZAHH212b (Controller)

377. TZAHH212b: controls = H200b
   - KG sources: P&ID heater control section (grids J9 to J11)

## TZH213 (Controller)

378. TZH213: controls = H200a
379. TZH213: controls = H200b
   - KG sources: P&ID heater control section (grids J9 to J11)

## V101 (ManualValve)

380. V101: floor = 1
381. V101: gridReference = L4
382. V101: normalPosition = closed
383. V101: valveType = ball
   - KG sources: Pilot Plant Report Fig E.1 and Fig F.23

## V102 (ManualValve)

384. V102: floor = 1
385. V102: gridReference = L4
386. V102: normalPosition = closed
387. V102: valveType = ball
   - KG sources: Pilot Plant Report Fig E.1 and Fig F.23

## V105 (ManualValve)

388. V105: floor = 1
389. V105: gridReference = M4
390. V105: normalPosition = closed
391. V105: valveType = ball
   - KG sources: Pilot Plant Report Fig E.1 and Fig F.23

## V106 (ManualValve)

392. V106: floor = 1
393. V106: gridReference = M3
394. V106: normalPosition = closed
395. V106: valveType = ball
   - KG sources: Pilot Plant Report Fig E.1 and Fig F.23

## V109 (ManualValve)

396. V109: floor = 1
397. V109: normalPosition = closed
398. V109: valveType = ball
   - KG sources: Pilot Plant Report Fig E.1 and Fig F.23

## V110 (ManualValve)

399. V110 is step 12 of the stripping loop route.
400. V110: feedsInto = V112
401. V110: floor = 1
402. V110: gridReference = L7
403. V110: normalPosition = open
404. V110: pipedTo = V112
405. V110: valveType = ball
   - KG sources: P&ID grid L7; Pilot Plant Report Fig E.1/E.2 (stripping loop commissioning line-up); Team check first valve after the sump outlet; ball valve per valve schedule

## V112 (CheckValve)

406. V112 is step 13 of the stripping loop route.
407. V112: feedsInto = C100
408. V112: floor = 1
409. V112: gridReference = M8
410. V112: normalPosition = open
411. V112: pipedTo = C100
412. V112: valveType = check
   - KG sources: P&ID grid M8; Pilot Plant Report Fig E.1/E.2 (stripping loop commissioning line-up); Team check check valve per valve schedule

## V113a (CheckValve)

413. V113a is step 18 of the stripping loop route.
414. V113a: feedsInto = V113b
415. V113a: floor = 1
416. V113a: gridReference = M9
417. V113a: normalPosition = open
418. V113a: pipedTo = V113b
419. V113a: valveType = check
   - KG sources: P&ID grid M9; Pilot Plant Report Fig E.1/E.2 (stripping loop commissioning line-up); Team check check valve per valve schedule

## V113b (ManualValve)

420. V113b is step 19 of the stripping loop route.
421. V113b: feedsInto = J100
422. V113b: floor = 1
423. V113b: gridReference = M10
424. V113b: normalPosition = open
425. V113b: pipedTo = J100
426. V113b: valveType = ball
   - KG sources: P&ID grid M10; Pilot Plant Report Fig E.1/E.2 (stripping loop commissioning line-up); Team check ball valve per valve schedule

## V116 (ManualValve)

427. V116 is step 25 of the stripping loop route.
428. V116: feedsInto = V117a
429. V116: floor = 1
430. V116: gridReference = M11
431. V116: normalPosition = open
432. V116: pipedTo = V117a
433. V116: pipedTo = V120
434. V116: valveType = ball
   - KG sources: P&ID grid M11; Pilot Plant Report Fig E.1/E.2 (stripping loop commissioning line-up)

## V117a (ManualValve)

435. V117a is step 26 of the stripping loop route.
436. V117a: feedsInto = Z102
437. V117a: floor = 1
438. V117a: gridReference = M11
439. V117a: normalPosition = open
440. V117a: pipedTo = Z102
441. V117a: valveType = ball
   - KG sources: P&ID grid M11; Pilot Plant Report Fig E.1/E.2 (stripping loop commissioning line-up) and Fig F.21

## V117b (ManualValve)

442. V117b is step 29 of the stripping loop route.
443. V117b: feedsInto = V121
444. V117b: floor = 1
445. V117b: gridReference = M11
446. V117b: normalPosition = open
447. V117b: pipedTo = V121
448. V117b: valveType = ball
   - KG sources: P&ID grid M11; Pilot Plant Report Fig E.1/E.2 (stripping loop commissioning line-up) and Fig F.21; Team check order Z102 > V117b > V121

## V120 (ManualValve)

449. V120: bypasses = Z102
450. V120: floor = 1
451. V120: gridReference = L11
452. V120: normalPosition = closed
453. V120: pipedTo = V121
454. V120: valveType = ball
   - KG sources: P&ID grid L11; Pilot Plant Report Fig F.21 (Z102 bypass) and Fig E.1/E.2 (stripping loop commissioning line-up)

## V121 (ManualValve)

455. V121 is step 30 of the stripping loop route.
456. V121: feedsInto = FT103
457. V121: floor = 1
458. V121: gridReference = M11
459. V121: normalPosition = open
460. V121: pipedTo = FT103
461. V121: valveType = ball
   - KG sources: P&ID grid M11; Pilot Plant Report Fig E.1/E.2 (stripping loop commissioning line-up); Team check order Z102 > V117b > V121

## V217 (ManualValve)

462. V217: floor = 3
463. V217: gridReference = G14
464. V217: normalPosition = open
465. V217: valveType = ball
   - KG sources: Pilot Plant Report Fig E.2 (opened for the commissioning test; floor 3, grid G14); Pilot Plant Report lean MEA valve list (floor 2, grid G14, normally closed) and start-up tables (ball, grid H14)

## V302 (ManualValve)

466. V302: floor = 3
467. V302: gridReference = G8
468. V302: normalPosition = closed
469. V302: valveType = needle
   - KG sources: P&ID grid G8, on E100 at the side-return gap; Pilot Plant Report Fig E.1 and start-up tables (needle valve, floor 3)

## V309 (ManualValve)

470. V309: floor = 3
471. V309: gridReference = H10
472. V309: normalPosition = closed
473. V309: pipedTo = E100_N_side_inlet
474. V309: valveType = ball
   - KG sources: P&ID grid H10, branch from the heater return line to the E100 side inlet; Pilot Plant Report Fig E.1 (closed in the commissioning line-up) and Fig F.7 (grid G10); Team check side return to E100 between V318 and V302

## V315 (ManualValve)

475. V315: floor = 3
476. V315: gridReference = G10
477. V315: normalPosition = closed
478. V315: valveType = ball
   - KG sources: P&ID grid G10; Pilot Plant Report Fig E.1/E.2 (stripping loop commissioning line-up); Team check grid confirmed

## V316 (ManualValve)

479. V316: floor = 3
480. V316: gridReference = G10
481. V316: normalPosition = closed
482. V316: pipedTo = V315
483. V316: valveType = ball
   - KG sources: P&ID grid G10; Pilot Plant Report Fig E.1/E.2 (stripping loop commissioning line-up); Team check grid confirmed

## V318 (ManualValve)

484. V318: floor = 3
485. V318: gridReference = G8
486. V318: normalPosition = closed
487. V318: valveType = ball
   - KG sources: P&ID grid G8, on E100 at the side-return gap; Pilot Plant Report Fig E.1 and start-up tables (ball valve, floor 3)

## V402 (ManualValve)

488. V402 is step 40 of the stripping loop route.
489. V402: feedsInto = E100_N_top_inlet
490. V402: floor = 3
491. V402: gridReference = F8
492. V402: normalPosition = open
493. V402: pipedTo = E100_N_top_inlet
494. V402: valveType = ball
   - KG sources: P&ID differences row V402 & V403 (F8); P&ID grid F8; Pilot Plant Report Fig E.1/E.2 (stripping loop commissioning line-up)

## V403 (ManualValve)

495. V403 is step 39 of the stripping loop route.
496. V403: feedsInto = V402
497. V403: floor = 3
498. V403: gridReference = F8
499. V403: normalPosition = open
500. V403: pipedTo = V402
501. V403: valveType = ball
   - KG sources: P&ID differences row V402 & V403 (F8); P&ID grid F8; Pilot Plant Report Fig E.1/E.2 (stripping loop commissioning line-up)

## Z102 (Filter)

502. Z102 is step 27 of the stripping loop route.
503. Z102: feedsInto = V117b
504. Z102: filterRating_um = 50.0
505. Z102: floor = 1
506. Z102: pipedTo = V117b
   - KG sources: P&ID grid M11; Pilot Plant Report section E.3.6 and Fig F.21
