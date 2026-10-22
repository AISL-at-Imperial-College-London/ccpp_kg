"""Write every plant-item fact in the KG as a plain claim, for independent checking.
Usage (from the repo root):  python stripping_loop/export_claims.py
Output: stripping_loop/claims.md (numbered claims, grouped by item, with the KG's cited sources)
"""
import pathlib
from collections import defaultdict

from rdflib import Graph

HERE = pathlib.Path(__file__).resolve().parent
NS = "http://imperial.ac.uk/ccpp#"
g = Graph()
g.parse(HERE.parent / "ontology" / "ccpp_ontology.ttl")
g.parse(HERE / "stripping_loop.ttl")

PRE = f"PREFIX ccpp: <{NS}>\nPREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>\n"
SKIP = {"tag", "citedIn", "note", "label", "type", "hasStage"}

facts = defaultdict(list)
for item, tag, prop, val in g.query(PRE + """
    SELECT ?i ?tag ?p ?v WHERE {
      ?i a/rdfs:subClassOf* ccpp:PlantItem ; ccpp:tag ?tag ; ?p ?v .
    }"""):
    name = str(prop).split("#")[-1]
    if name in SKIP:
        continue
    value = str(val).replace(NS, "")
    facts[str(tag)].append(f"{name} = {value}")

cls = {str(t): str(c).split("#")[-1] for t, c in g.query(PRE + """
    SELECT ?tag ?c WHERE { ?i ccpp:tag ?tag ; a ?c . FILTER(STRSTARTS(STR(?c), STR(ccpp:))) }""")}
cites = defaultdict(list)
for tag, text in g.query(PRE + "SELECT ?tag ?t WHERE { ?i ccpp:tag ?tag ; ccpp:citedIn/ccpp:citationText ?t }"):
    cites[str(tag)].append(str(text))
order = defaultdict(list)
for tag, idx in g.query(PRE + """
    SELECT ?tag ?idx WHERE { ccpp:StrippingLoop ccpp:hasStep ?s . ?s ccpp:stepItem/ccpp:tag ?tag ; ccpp:stepIndex ?idx }"""):
    order[str(tag)].append(int(idx))

lines = ["# Stripping loop KG: claims for independent verification", ""]
n = 0
for tag in sorted(facts):
    lines += ["", f"## {tag} ({cls.get(tag, 'item')})", ""]
    if tag in order:
        n += 1
        lines.append(f"{n}. {tag} is step {', '.join(map(str, sorted(order[tag])))} of the stripping loop route.")
    for f in sorted(set(facts[tag])):
        n += 1
        lines.append(f"{n}. {tag}: {f}")
    lines.append(f"   - KG sources: {'; '.join(sorted(set(cites[tag]))) or 'none'}")
route = [str(t) for t, in g.query(PRE + """
    SELECT ?name WHERE { ccpp:StrippingLoop ccpp:hasStep ?s . ?s ccpp:stepIndex ?i ; ccpp:stepType "inline" ; ccpp:stepItem ?x .
      OPTIONAL { ?x ccpp:tag ?t } OPTIONAL { ?x rdfs:label ?l } BIND(COALESCE(?t, ?l) AS ?name) } ORDER BY ?i""")]
lines = lines[:2] + ["## Loop route (inline items in flow order)", "", " > ".join(route), ""] + lines[2:]
(HERE / "claims.md").write_text("\n".join(lines) + "\n")
print(f"Wrote {n} claims to {HERE / 'claims.md'}")
