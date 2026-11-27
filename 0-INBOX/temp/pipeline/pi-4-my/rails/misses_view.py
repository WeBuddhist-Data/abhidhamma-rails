"""Inspection helper (read only): each adherence miss with the keyword-map form, the termbase senses and the Pāli /
zero-shot segment.  usage: misses_view.py <adherence report> [keyword-regex]"""
import pathlib
import re
import sys
import unicodedata

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(HERE))
sys.dont_write_bytecode = True
import adherence_my as A  # noqa: E402

N = lambda s: unicodedata.normalize("NFC", s)  # noqa: E731
KMAP = ROOT / "AI_translation/burmese/pi-4-keywords-by-reference-pali-burmese-plain.md"
TB = ROOT / "AI_translation/burmese/pi-4-pali-burmese-termbase-plain.md"
P = A.segments(ROOT / "AI_translation/pali/pi-4_split_chapters")
Z = A.segments(ROOT / "AI_translation/burmese/pi-4-burmese-plain-zeroshot_split_chapters")
kv = {}
for l in open(KMAP, encoding="utf-8"):
    m = re.match(r"^\[([^\]]+)\] (.*)$", N(l.strip()))
    if m:
        for x in m.group(2).split(", "):
            if "=" in x:
                k, v = x.split("=", 1)
                kv[(m.group(1), k)] = v
tbl = {}
for l in open(TB, encoding="utf-8"):
    m = re.match(r"^(.*?): \{(.*)\}\s*$", N(l.rstrip("\n")))
    if m:
        tbl[m.group(1).lower()] = m.group(2)
rx = re.compile(sys.argv[2]) if len(sys.argv) > 2 else None
for l in open(sys.argv[1], encoding="utf-8"):
    f = N(l).strip().split("\t")
    if len(f) != 3 or not f[0][:1].isdigit():
        continue
    i, kw, t = f
    if rx and not rx.fullmatch(kw):
        continue
    print(f"=== {i} {kw}  map=«{kv.get((i, kw))}»  TB: {tbl.get(kw.lower())}")
    if "--seg" in sys.argv:
        print("   P:", P[i][:600])
        print("   Z:", Z[i][:900])
