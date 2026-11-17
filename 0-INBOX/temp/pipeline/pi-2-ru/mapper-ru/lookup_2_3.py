"""Values of given keywords in the approved maps, with example ids. usage: python -I -X utf8 lookup_2_3.py kw ..."""
import collections
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
MAPS = sorted((ROOT / "AI_translation" / "russian").glob("pi-*-keywords-by-reference-pali-russian-plain.md"))
MAPS += [HERE / "1-khandhavibhango.mapped.md"]
lc = lambda s: s[:1].lower() + s[1:]
want = {lc(a) for a in sys.argv[1:]}
hits = {k: collections.defaultdict(list) for k in want}
for m in MAPS:
    tag = m.name.split("-keywords")[0].replace(".mapped.md", "")
    for line in m.read_text(encoding="utf-8").splitlines():
        if "] " not in line:
            continue
        bid, rest = line.split("] ", 1)
        for pair in rest.split(", "):
            if "=" not in pair:
                continue
            k, v = pair.split("=", 1)
            if lc(k) in hits:
                hits[lc(k)][f"{tag}:{v}"].append(bid[1:])
for k in sys.argv[1:]:
    h = hits[lc(k)]
    print(k + ": " + (" | ".join(f"{v} ({len(ids)}; {','.join(ids[:3])})" for v, ids in
                                 sorted(h.items(), key=lambda x: -len(x[1]))[:6]) or "-"))
