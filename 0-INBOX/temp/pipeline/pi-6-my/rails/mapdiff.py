"""Inspection helper (read only): (keyword, keyword-map form) pairs whose form is none of the keyword's termbase terms,
with counts and ids. usage: mapdiff.py"""
import collections, pathlib, re, sys, unicodedata
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(HERE)); sys.dont_write_bytecode = True
import adherence_my as A  # noqa: E402
N = lambda s: unicodedata.normalize("NFC", s)
tb = A.parse_termbase(ROOT / "AI_translation/burmese/pi-6-pali-burmese-termbase-plain.md")
c = collections.defaultdict(list)
for l in open(ROOT / "AI_translation/burmese/pi-6-keywords-by-reference-pali-burmese-plain.md", encoding="utf-8"):
    m = re.match(r"^\[([^\]]+)\] (.*)$", N(l.strip()))
    if not m: continue
    for x in m.group(2).split(", "):
        if "=" in x:
            k, v = x.split("=", 1)
            t = tb.get(k.lower())
            if t is None: c[(k, v, "NO TB")].append(m.group(1))
            elif v not in t: c[(k, v, " | ".join(t))].append(m.group(1))
for (k, v, t), ids in sorted(c.items(), key=lambda x: -len(x[1])):
    print(f"{len(ids):4d}\t{k}\tmap «{v}»\tTB «{t}»\t{' '.join(ids[:6])}")
