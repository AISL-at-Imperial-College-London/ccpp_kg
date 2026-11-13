"""
Register a new source document the same way the existing sections do, without needing to know the builder's internals.

It reads an already-built section (.ttl) to find how a citation points at the HAZOP source and what class that source
node has, then returns an ITEMS entry for the new document in the same form.
Use in a data file:   ITEMS.update(source_item("CE", "Cause and effect matrix, Rev 5 (06/10/2011, final for construction)"))
"""
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent


def _pattern():
    texts = {p: p.read_text() for p in ROOT.glob("*/*.ttl") if p.parent.name not in ("ccpp", "ontology")}
    local = None
    for text in texts.values():                                   # how does a citation point at the HAZOP document?
        m = re.search(r"ccpp:\w*[Ss]ource\w*\s+ccpp:(\w*HAZOP\w*?)\s*[;.,]", text)
        if m and not re.search(r"HAZOP_(\d|element)", m.group(1)):
            local = m.group(1); break
    if local is None:
        raise SystemExit("new_sources: could not find how citations point at the HAZOP source. "
                         "Run:  grep -m3 -n 'HAZOP' overhead/overhead.ttl   and send the output.")
    prefix, suffix = local.split("HAZOP")
    cls = None
    for text in texts.values():                                   # what class is that source node?
        m = re.search(r"^ccpp:" + re.escape(local) + r"\s+a\s+ccpp:(\w+)", text, re.M)
        if m:
            cls = m.group(1); break
    if cls is None:
        raise SystemExit(f"new_sources: found the source node ccpp:{local} but not its class. "
                         f"Run:  grep -rn -m2 '^ccpp:{local} ' */*.ttl   and send the output.")
    return prefix, suffix, cls


def source_item(key, title):
    prefix, suffix, cls = _pattern()
    return {prefix + key + suffix: dict(cls=cls, label=title, note="Source document added for the KG A+ improvements (received from the plant, Nov 2026).",
                                        cite=[("DERIVED", "source document register")])}


if __name__ == "__main__":
    print("source nodes look like: ccpp:%sHAZOP%s, class ccpp:%s" % _pattern())
