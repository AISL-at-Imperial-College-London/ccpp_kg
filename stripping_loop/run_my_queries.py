"""Run your own questions against the KG and compare them with answers you wrote first.

Each file in stripping_loop/my_queries/ is a SPARQL query with two comment lines at the top:
    # Q: plain-English question
    # EXPECT: answer1, answer2      (order does not matter; leave empty to just see the answer)
Usage (from the repo root):  python stripping_loop/run_my_queries.py
"""
import pathlib

from rdflib import Graph

HERE = pathlib.Path(__file__).resolve().parent
NS = "http://imperial.ac.uk/ccpp#"
g = Graph()
g.parse(HERE.parent / "ontology" / "ccpp_ontology.ttl")
g.parse(HERE / "stripping_loop.ttl")

PREFIXES = f"PREFIX ccpp: <{NS}>\nPREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>\n"


def norm(x):
    """Compare numbers as numbers (8 == 8.0) and everything else as exact text."""
    x = str(x).strip().replace(NS, "")
    try:
        return repr(float(x))
    except ValueError:
        return x


passed = failed = 0
for f in sorted((HERE / "my_queries").glob("*.rq")):
    text = f.read_text()
    lines = text.splitlines()
    question = next((l[4:].strip() for l in lines if l.startswith("# Q:")), f.stem)
    expect = next((l[9:].strip() for l in lines if l.startswith("# EXPECT:")), "")
    query = text if "PREFIX ccpp:" in text else PREFIXES + text
    print(f"\n[{f.stem}] {question}")
    try:
        res = g.query(query)
    except Exception as e:  # noqa: BLE001
        print(f"    ERROR in the query: {e}")
        failed += 1
        continue
    if res.type == "ASK":
        got = {str(res.askAnswer).lower()}
        print(f"    {res.askAnswer}")
    else:
        rows = list(res)
        got = {norm(r[0]) for r in rows if r[0] is not None}
        for r in rows:
            print("    " + " | ".join("" if v is None else str(v).replace(NS, "") for v in r))
        if not rows:
            print("    (no rows)")
    if expect:
        expected = {norm(x) for x in expect.split(",") if x.strip()}
        if got == expected:
            passed += 1
            print("    PASS (matches your expected answer)")
        else:
            failed += 1
            print(f"    FAIL  expected {sorted(expected)}  got {sorted(got)}")

print(f"\n{passed} passed, {failed} failed")
