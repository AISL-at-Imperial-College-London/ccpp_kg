"""Print every citation for one item in the KG.
Usage (from the repo root):  python stripping_loop/show_sources.py Z102
"""
import pathlib
import sys

from rdflib import Graph

HERE = pathlib.Path(__file__).resolve().parent
g = Graph()
g.parse(HERE.parent / "ontology" / "ccpp_ontology.ttl")
g.parse(HERE / "stripping_loop.ttl")

tag = sys.argv[1] if len(sys.argv) > 1 else "Z102"
q = f"""
PREFIX ccpp: <http://imperial.ac.uk/ccpp#>
SELECT ?text WHERE {{ ccpp:{tag} ccpp:citedIn/ccpp:citationText ?text }} ORDER BY ?text
"""
rows = list(g.query(q))
print(f"Sources for {tag}:")
for (text,) in rows:
    print("  -", text)
if not rows:
    print("  (none found: check the tag spelling)")

total = list(g.query("PREFIX ccpp: <http://imperial.ac.uk/ccpp#> "
                     "SELECT (COUNT(?c) AS ?n) WHERE { ?c a ccpp:Citation }"))[0][0]
print(f"\nTotal citations in the KG: {total}")
