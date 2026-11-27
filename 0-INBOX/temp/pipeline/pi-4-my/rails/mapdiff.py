"""Inspection helper (read only): keyword-map values that are not the termbase term, with their segment ids."""
import collections, pathlib, re, sys, unicodedata
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(HERE)); sys.dont_write_bytecode = True
import adherence_my as A  # noqa
N = lambda s: unicodedata.normalize("NFC", s)
tb = A.parse_termbase(ROOT / "AI_translation/burmese/pi-4-pali-burmese-termbase-plain.md")
d = collections.defaultdict(list)
for l in open(ROOT / "AI_translation/burmese/pi-4-keywords-by-reference-pali-burmese-plain.md", encoding="utf-8"):
    m = re.match(r"^\[([^\]]+)\] (.*)$", N(l.strip()))
    if not m: continue
    for x in m.group(2).split(", "):
        if "=" not in x: continue
        k, v = x.split("=", 1)
        t = tb.get(k.lower())
        if t is not None and v not in t:
            d[(k, v, " | ".join(t))].append(m.group(1))
for (k, v, t), ids in sorted(d.items(), key=lambda x: x[0][0].lower()):
    print(f"{k}\t«{v}» → «{t}»\t{' '.join(ids)}")
