"""Inspection helper (not part of the checks): group the adherence misses by which loose variant of the term occurs."""
import collections, pathlib, re, sys, unicodedata
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(HERE)); sys.dont_write_bytecode = True
import adherence_my as A
N = lambda s: unicodedata.normalize("NFC", s)
Z = A.segments(ROOT / (sys.argv[2] if len(sys.argv) > 2 else "AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters"))
VAR = [("ရမည့်", "ရမည်"), ("ဟူသော အကြောင်းကြောင့်", ""), ("ကြွင်းကျန်", "ကြွင်း")]
c = collections.Counter()
ex = {}
for l in open(sys.argv[1], encoding="utf-8"):
    f = N(l).strip().split("\t")
    if len(f) != 3 or not f[0][:1].isdigit():
        continue
    i, kw, terms = f
    t = Z[i]
    how = "none"
    for o, n in VAR:
        if any(o in x and A.occurs(x.replace(o, n), t) for x in terms.split(" | ")):
            how = f"{o}->{n}"
            break
    c[(kw, how)] += 1
    ex.setdefault((kw, how), i)
for (kw, how), n in sorted(c.items(), key=lambda x: (x[0][1], -x[1])):
    print(n, kw, how, ex[(kw, how)])
