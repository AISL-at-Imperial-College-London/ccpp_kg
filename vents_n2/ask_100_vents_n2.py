"""
Ask the vents, N2 header and make-up water KG (piece 11) 47 questions whose expected answers come from the
documents (the team then traces and checks it on the P&ID), not from the KG. Piece 11 links to items in other
sections, so the questions run on the joined full plant.
Run from the repo root (after ccpp/build_full_plant.py):   python vents_n2/ask_100_vents_n2.py
Output: vents_n2/hundred_results_vents_n2.md
"""
import collections
import pathlib
import sys

from rdflib import Graph

HERE = pathlib.Path(__file__).resolve().parent
NS = "http://imperial.ac.uk/ccpp#"
PRE = f"PREFIX ccpp: <{NS}>\nPREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>\n"
g = Graph()
g.parse(HERE.parent / "ontology" / "ccpp_ontology.ttl")
g.parse(HERE.parent / "ccpp" / "full_plant.ttl")


def T(x): return f"ccpp:{x}"
def ALL(*trip): return "ASK { " + " ".join(f"{T(s)} {T(p)} {T(o)} ." for s, p, o in trip) + " }"
def OUT(s, p): return f"SELECT ?t WHERE {{ {T(s)} {T(p)} ?x . ?x ccpp:tag ?t }}"
def PATH(a, p, b): return f"ASK {{ {T(a)} {T(p)}+ {T(b)} }}"
def DIRECT(a, p, b): return f"ASK {{ {T(a)} {T(p)} {T(b)} }}"
def VAL(s, p): return f"SELECT ?v WHERE {{ {T(s)} {T(p)} ?v }}"
def CONTAINS(s, p, text): return f"ASK {{ {T(s)} {T(p)} ?v . FILTER(CONTAINS(STR(?v), \"{text}\")) }}"
def INSTEP(loop, item): return f"ASK {{ {T(loop)} ccpp:hasStep/ccpp:stepItem {T(item)} }}"
def CLSP(c, prefix): return (f"SELECT DISTINCT ?t WHERE {{ ?x a/rdfs:subClassOf* {T(c)} ; ccpp:tag ?t ; ccpp:citedIn ?c . "
                             f"FILTER(CONTAINS(STR(?c), \"__{prefix}cit\")) }}")
def CNTOI(prefix): return f"SELECT (COUNT(?o) AS ?n) WHERE {{ ?o a ccpp:OpenItem ; ccpp:foundBy \"{prefix} section build, Oct 2026\" }}"


P = "vnt"
L = "N2HeaderRoute"
VENTS = ["PCV119", "V190", "V197", "V209", "V315", "SDV421", "V409", "V411"]
Q = [(f"V{i:02d}", "Vents", f"Is {v} on the vent stream (Fig F.3) to the vent system?", DIRECT(v, "pipedTo", "VENT_SYSTEM"), ["true"]) for i, v in enumerate(VENTS, 1)]
Q += [
 ("V09","Vents","Does the absorber vent (after PCV300) discharge to the vent system?", DIRECT("VENT_E101","pipedTo","VENT_SYSTEM"), ["true"]),
 ("V10","Vents","Can gas from the top of E101 reach the vent system through PCV300?", PATH("E101_N_gas_outlet","pipedTo","VENT_SYSTEM"), ["true"]),
 ("V11","Vents","Is the vent system a vent connection?", CLSP("VentConnection",P), ["VENT_SYSTEM"]),
 ("V12","Vents","Do the relief valves RV400 and RV401 still discharge to K403?", ALL(("RV400","pipedTo","K403"),("RV401","pipedTo","K403")), ["true"]),
 ("K01","K403","What grid is K403 at (report colour P&ID)?", VAL("K403","gridReference"), ["B11"]),
 ("K02","K403","Does the K403 note cite the report colour P&ID?", CONTAINS("K403","note","colour P&ID"), ["true"]),
 ("K03","K403","Is open item VN03 about where K403 drains?", ALL(("VN03","about","K403")), ["true"]),
 ("N01","N2 header","What comes after PCV117 on the N2 header branch?", DIRECT("PCV117","feedsInto","NRV109"), ["true"]),
 ("N02","N2 header","Does NRV109 feed the N2 header?", DIRECT("NRV109","feedsInto","N2_PURGE_HEADER"), ["true"]),
 ("N03","N2 header","Does the header feed both tank check valves?", ALL(("N2_PURGE_HEADER","feedsInto","NRV107"),("N2_PURGE_HEADER","feedsInto","NRV108")), ["true"]),
 ("N04","N2 header","Does NRV107 feed F100 (left tank)?", DIRECT("NRV107","feedsInto","F100"), ["true"]),
 ("N05","N2 header","Does NRV108 feed R100 (right tank)?", DIRECT("NRV108","feedsInto","R100"), ["true"]),
 ("N06","N2 header","Does N2 from the supply reach both tanks?", ALL(("NRV107","feedsInto","F100"),("NRV108","feedsInto","R100")), ["true"]),
 ("N07","N2 header","Can N2 from the supply reach F100?", PATH("N2_SUPPLY","feedsInto","F100"), ["true"]),
 ("N08","N2 header","Can N2 from the header reach the E100 MEA side (it must not)?", PATH("N2_PURGE_HEADER","feedsInto","E100"), ["false"]),
 ("N09","N2 header","Is NRV104 on the N2 header (team trace)?", DIRECT("N2_PURGE_HEADER","pipedTo","NRV104"), ["true"]),
 ("N10","N2 header","Does the N2 header route include PI114?", INSTEP(L,"PI114"), ["true"]),
 ("N11","N2 header","Does the N2 header route start at the N2 supply?", INSTEP(L,"N2_SUPPLY"), ["true"]),
 ("N12","N2 header","Is the N2 header a pipe segment?", CLSP("PipeSegment",P), ["N2_PURGE_HEADER"]),
 ("N13","N2 header","Does PCV117 still feed PCV115 (the feed line is unchanged)?", DIRECT("PCV117","feedsInto","PCV115"), ["true"]),
 ("W01","Make-up water","What does the make-up water supply feed first?", OUT("MAKEUP_WATER_SUPPLY","feedsInto"), ["NRV100a"]),
 ("W02","Make-up water","What does NRV100a feed?", OUT("NRV100a","feedsInto"), ["NRV100b"]),
 ("W03","Make-up water","Is the deionising cartridge after the NRVs (HAZOP 4.8)?", DIRECT("NRV100b","feedsInto","DI_CARTRIDGE"), ["true"]),
 ("W04","Make-up water","Does the deionising cartridge feed K101?", DIRECT("DI_CARTRIDGE","feedsInto","K101"), ["true"]),
 ("W05","Make-up water","Does make-up water reach K101?", PATH("MAKEUP_WATER_SUPPLY","feedsInto","K101"), ["true"]),
 ("W06","Make-up water","What grid is the make-up water supply at?", VAL("MAKEUP_WATER_SUPPLY","gridReference"), ["Q18"]),
 ("W07","Make-up water","Which supply connection does this piece add?", CLSP("SupplyConnection",P), ["MAKEUP_WATER_SUPPLY"]),
 ("W08","Make-up water","Which filter does this piece add?", CLSP("Filter",P), ["DI_CARTRIDGE"]),
 ("W09","Make-up water","Does HAZOP 4.8 concern the deionising cartridge?", ALL(("HAZOP_4_08","concerns","DI_CARTRIDGE")), ["true"]),
 ("W10","Make-up water","Was a deionising cartridge added (HAZOP 4.8)?", CONTAINS("HAZOP_4_08","actionTaken","Deionising cartridge added"), ["true"]),
 ("W11","Make-up water","Can make-up water reach E101 through K101?", PATH("MAKEUP_WATER_SUPPLY","feedsInto","E101"), ["true"]),
 ("O01","Open items","How many open items does this piece hold?", CNTOI(P), ["6"]),
 ("O02","Open items","Is VN01 about the vent system?", ALL(("VN01","about","VENT_SYSTEM")), ["true"]),
 ("O03","Open items","Is VN06 about the make-up water?", ALL(("VN06","about","MAKEUP_WATER_SUPPLY")), ["true"]),
 ("O04","Open items","Is VN05 about the N2 header?", ALL(("VN05","about","N2_PURGE_HEADER")), ["true"]),
 ("X01","Join","Does the N2 header route use the N2 supply and V127 from piece 5?", ALL(("N2_SUPPLY","feedsInto","V127"),("V127","feedsInto","PCV117")), ["true"]),
 ("X02","Join","Is the MEA filling route unchanged (F100 still feeds J105)?", DIRECT("F100","feedsInto","J105"), ["true"]),
 ("X03","Join","Is the CO2 recycle round K103 unchanged (PCV119 to K103)?", DIRECT("PCV119","pipedTo","K103"), ["true"]),
 ("X04","Join","Is the K101 water loop unchanged (Z103 to J104)?", DIRECT("Z103","pipedTo","J104"), ["true"]),
]


def norm(x):
    x = str(x).strip().replace(NS, "")
    try:
        return repr(float(x))
    except ValueError:
        return x


results = []
for qid, cat, question, sparql, expect in Q:
    try:
        res = g.query(PRE + sparql)
        rows = [[str(res.askAnswer).lower()]] if res.type == "ASK" else [
            ["" if v is None else str(v).replace(NS, "") for v in r] for r in res]
        err = None
    except Exception as e:  # noqa: BLE001
        rows, err = [], str(e)
    got = {norm(r[0]) for r in rows if r and r[0] != ""}
    status = "QUERY ERROR" if err else ("PASS" if got == {norm(x) for x in expect} else "FAIL")
    results.append((qid, cat, question, expect, rows, status, err))

count = collections.Counter(r[5] for r in results)
lines = ["# Vents and N2 KG: question run", "", f"PASS {count['PASS']}, FAIL {count['FAIL']}, QUERY ERROR {count['QUERY ERROR']}", ""]
for qid, cat, question, expect, rows, status, err in results:
    lines += [f"## {qid} [{cat}] {status}", "", f"**{question}**", "", f"- Expected: {', '.join(expect)}"]
    lines += [f"- Error: {err}"] if err else [f"- KG: {', '.join(r[0] for r in rows) or '(no rows)'}"]
    lines.append("")
(HERE / "hundred_results_vents_n2.md").write_text("\n".join(lines))
for qid, cat, question, expect, rows, status, err in results:
    if status != "PASS":
        print(f"[{qid}] {status} {question}\n      expected: {expect}\n      got: {[r[0] for r in rows]} {err or ''}")
print(f"\nPASS {count['PASS']}, FAIL {count['FAIL']}, QUERY ERROR {count['QUERY ERROR']}  (details in vents_n2/hundred_results_vents_n2.md)")
sys.exit(1 if count["FAIL"] or count["QUERY ERROR"] else 0)