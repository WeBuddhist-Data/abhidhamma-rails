"""Context of keywords: Pāli snippet around the word, and Hindi snippets around guessed Hindi strings.

usage: python -I -B -X utf8 ctx_2-02_2-08_hi.py <file> <kw> [hindi-guess …] [--n N] [--w W]
  prints, for the first N segments whose keywords contain kw: the Pāli snippet(s) and, per guess,
  the Hindi snippet(s); without a guess, the first W*2 chars of the Hindi.
"""
import sys, pathlib, re
sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import *  # noqa

f, kw = sys.argv[1], sys.argv[2]
rest = sys.argv[3:]
n, w = 3, 110
if "--n" in rest:
    n = int(rest[rest.index("--n") + 1]); rest = [x for x in rest if x not in ("--n", str(n))]
if "--w" in rest:
    w = int(rest[rest.index("--w") + 1]); rest = [x for x in rest if x not in ("--w", str(w))]
hi, pa = read_hindi(f), read_pali(f)
ids = [b for b, ks in read_keywords(f) if kw in ks]
print(kw, "segments:", len(ids), ids[:12])
stem = kw[:max(4, len(kw) - 3)]
for b in ids[:n]:
    print("##", b)
    p = pa.get(b, "")
    for m in list(re.finditer(re.escape(stem), p, re.I))[:3]:
        print("  PA:", p[max(0, m.start() - w): m.end() + w].replace("\n", " "))
    h = hi.get(b, "")
    if not rest:
        print("  HI:", h[: 2 * w].replace("\n", " "))
    for g in rest:
        ms = list(re.finditer(re.escape(g), h))
        print("  HI[%s] x%d" % (g, len(ms)))
        for m in ms[:2]:
            print("     ", h[max(0, m.start() - w): m.end() + w].replace("\n", " "))
