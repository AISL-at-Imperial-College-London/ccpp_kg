"""Run every query and save the answers, with the sources for each tag, to one file.
Usage (from the repo root):  python stripping_loop/export_answers.py
Output: stripping_loop/query_answers.md
"""
import pathlib

from rdflib import Graph

HERE = pathlib.Path(__file__).resolve().parent
g = Graph()
g.parse(HERE.parent / "ontology" / "ccpp_ontology.ttl")
g.parse(HERE / "stripping_loop.ttl")

# Look up every tag's citations once
cites = {}
for tag, text in g.query("""
    PREFIX ccpp: <http://imperial.ac.uk/ccpp#>
    SELECT ?tag ?text WHERE { ?i ccpp:tag ?tag ; ccpp:citedIn/ccpp:citationText ?text }"""):
    cites.setdefault(str(tag), []).append(str(text))

lines = ["# Stripping loop KG: query answers with sources", ""]
for q in sorted((HERE / "queries").glob("*.rq")):
    text = q.read_text()
    question = text.splitlines()[0].lstrip("# ")
    lines += ["", f"## {q.stem}", "", f"**{question}**", ""]
    res = g.query(text)
    if res.type == "ASK":
        lines.append(f"- Answer: {res.askAnswer}")
        continue
    names = [str(v) for v in res.vars]
    rows = list(res)
    if not rows:
        lines.append("- (no rows)")
    for row in rows:
        vals = ["" if row[v] is None else str(row[v]) for v in res.vars]
        lines.append("- " + " | ".join(f"{k} = {v}" for k, v in zip(names, vals)))
        srcs = sorted({s for v in vals for s in cites.get(v, [])})
        if srcs:
            lines.append("  - Sources: " + "; ".join(srcs))

out = HERE / "query_answers.md"
out.write_text("\n".join(lines) + "\n")
print(f"Wrote {out} ({len(lines)} lines)")
