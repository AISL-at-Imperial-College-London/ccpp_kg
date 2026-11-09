"""
Ask a knowledge graph a set of third-party questions and measure how well its evidence supports each answer.

Works on any RDF knowledge graph (it does not depend on our ontology), so the same questions, code and scoring can be
used for every KG in the comparison.

Run from the repo root:
    python tools/test_kg_questions.py questions.json ccpp/full_plant.ttl ontology/ccpp_ontology.ttl --name KG_A
Outputs (in results/):
    <name>_results.md        score table by category, then every question with its evidence
    <name>_answer_prompts.md one prompt per question (evidence + question) to paste into an LLM for a grounded answer
"""
import json
import pathlib
import re
import sys
from collections import defaultdict

# common names -> tags (applied identically to every KG)
ALIASES = {"absorber": "E101", "stripper": "E100", "desorber": "E100", "reboiler": "H100", "condenser": "C400",
           "cross exchanger": "C100", "lean/rich": "C100", "trim cooler": "C200", "saturator": "K101", "knockout": "K401",
           "cyclone": "K402", "reflux pump": "J300", "blower": "J102", "compressor": "J103", "electric heater": "H200a"}
FLOW_WORDS = ("feed", "pipe", "flow", "next", "connect", "stream", "upstream", "downstream", "route")
TAG = re.compile(r"\b([A-Z]{1,4}\d{3}[a-z]?)\b")


def local(x):
    x = str(x)
    return re.split(r"[#/]", x)[-1] if x.startswith("http") else x


def load(paths):
    from rdflib import Graph, Literal
    g = Graph()
    for p in paths:
        g.parse(p)
    return [(str(s), str(p), str(o), isinstance(o, Literal)) for s, p, o in g]


class KG:
    def __init__(self, triples):
        self.out, self.inn = defaultdict(list), defaultdict(list)
        self.byname, self.mentions = defaultdict(set), defaultdict(set)
        for s, p, o, lit in triples:
            self.out[s].append((p, o, lit))
            if not lit:
                self.inn[o].append((p, s))
            self.byname[local(s)].add(s)
            if lit:
                if TAG.fullmatch(o.strip() or "-"):
                    self.byname[o.strip()].add(s)
                elif local(p) not in ("tag", "location", "citationText"):
                    for t in set(TAG.findall(o)):           # nodes whose text mentions the tag (HAZOP rows, loops, notes)
                        self.mentions[t].add(s)

    def seeds(self, question):
        q = question.lower()
        tags = set(TAG.findall(question)) | {t for w, t in ALIASES.items() if w in q}
        return tags, {n for t in tags for n in self.byname.get(t, ())}

    def describe(self, node, lines, seen):
        for p, o, lit in self.out[node]:
            if local(p) in ("citedIn",):
                continue
            line = f"{local(node)} --{local(p)}--> {o if lit else local(o)}"
            if line not in seen:
                seen.add(line); lines.append(line)

    def evidence(self, question, flow_depth=3, max_lines=400):
        tags, seeds = self.seeds(question)
        lines, seen = [], set()
        ctx = {n for t in tags for n in self.mentions.get(t, ())} - seeds
        for n in seeds:
            self.describe(n, lines, seen)
            for p, s in self.inn[n]:                      # things that point at the item: HAZOP rows, loops, limits, open items, instruments
                if local(p) in ("citedIn", "stepItem"):
                    continue
                line = f"{local(s)} --{local(p)}--> {local(n)}"
                if line not in seen:
                    seen.add(line); lines.append(line)
                ctx.add(s)
        for c in ctx:                                     # one more hop: the content of those context nodes
            self.describe(c, lines, seen)
            for p, s in self.inn[c]:                      # and what points at them (limits on instruments, controllers on valves)
                if local(p) not in ("citedIn", "stepItem", "hasStep"):
                    line = f"{local(s)} --{local(p)}--> {local(c)}"
                    if line not in seen:
                        seen.add(line); lines.append(line)
        frontier = set(seeds)                             # flow neighbourhood, both directions, for cause and effect
        for _ in range(flow_depth):
            nxt = set()
            for n in frontier:
                for p, o, lit in self.out[n]:
                    if not lit and any(w in local(p).lower() for w in FLOW_WORDS):
                        line = f"{local(n)} --{local(p)}--> {local(o)}"
                        if line not in seen:
                            seen.add(line); lines.append(line)
                        nxt.add(o)
                for p, s in self.inn[n]:
                    if any(w in local(p).lower() for w in FLOW_WORDS):
                        line = f"{local(s)} --{local(p)}--> {local(n)}"
                        if line not in seen:
                            seen.add(line); lines.append(line)
                        nxt.add(s)
            frontier = nxt - frontier
        return tags, lines[:max_lines]


def score(key_items, lines):
    text = "\n".join(lines).lower()
    found = [k for k in key_items if re.search(r"(?<![a-z0-9])" + re.escape(k.lower()) + r"(?![a-z0-9])", text)]
    return found, (len(found) / len(key_items) if key_items else 0.0)


def run(questions, kg, name, outdir=pathlib.Path("results")):
    outdir.mkdir(exist_ok=True)
    by_cat = defaultdict(list)
    detail, prompts = [], []
    for q in questions:
        tags, lines = kg.evidence(q["question"])
        found, s = score(q.get("key_items", []), lines)
        status = "SUPPORTED" if s >= 0.8 else "PARTIAL" if s >= 0.4 else "NOT SUPPORTED"
        by_cat[q.get("category", "other")].append((s, status))
        missing = [k for k in q.get("key_items", []) if k not in found]
        detail += [f"## {q['id']} [{q.get('category','')}] {status} ({s:.0%})", "", f"**{q['question']}**", "",
                   f"- Expected: {q.get('expected_answer','')}", f"- Source: {q.get('source','')}",
                   f"- Key items found: {', '.join(found) or 'none'}", f"- Key items missing: {', '.join(missing) or 'none'}",
                   f"- Evidence lines: {len(lines)}", ""]
        prompts += [f"## {q['id']}", "", "Answer the question using ONLY the facts below from the plant knowledge graph. "
                    "Cite the facts you use. If the facts are not enough, say what is missing.", "", "Facts:", "```",
                    *lines[:150], "```", "", f"Question: {q['question']}", ""]
    rows = ["| Category | Questions | Supported | Partial | Not supported | Mean key-item recall |", "|---|---|---|---|---|---|"]
    allv = []
    for cat, v in sorted(by_cat.items()):
        allv += v
        rows.append(f"| {cat} | {len(v)} | {sum(x[1]=='SUPPORTED' for x in v)} | {sum(x[1]=='PARTIAL' for x in v)} | "
                    f"{sum(x[1]=='NOT SUPPORTED' for x in v)} | {sum(x[0] for x in v)/len(v):.0%} |")
    rows.append(f"| **All** | {len(allv)} | {sum(x[1]=='SUPPORTED' for x in allv)} | {sum(x[1]=='PARTIAL' for x in allv)} | "
                f"{sum(x[1]=='NOT SUPPORTED' for x in allv)} | {sum(x[0] for x in allv)/max(len(allv),1):.0%} |")
    (outdir / f"{name}_results.md").write_text("\n".join([f"# {name}: third-party question test", ""] + rows + [""] + detail))
    (outdir / f"{name}_answer_prompts.md").write_text("\n".join(prompts))
    print("\n".join(rows))
    print(f"\nDetails: {outdir / (name + '_results.md')}\nAnswer prompts: {outdir / (name + '_answer_prompts.md')}")


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    name = sys.argv[sys.argv.index("--name") + 1] if "--name" in sys.argv else "KG"
    args = [a for a in args if a != name]
    questions = json.loads(pathlib.Path(args[0]).read_text())
    run(questions, KG(load(args[1:])), name)