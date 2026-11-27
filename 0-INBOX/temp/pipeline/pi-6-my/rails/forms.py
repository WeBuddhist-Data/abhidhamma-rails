"""Inspection helper (read only): for each missed keyword, the Burmese forms in its segments that start with a given
stem (the first chunk of the term). usage: forms.py <adherence report> [--rails]"""
import collections, pathlib, re, sys, unicodedata
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(HERE)); sys.dont_write_bytecode = True
import adherence_my as A  # noqa: E402
N = lambda s: unicodedata.normalize("NFC", s)
B = A.segments(ROOT / ("AI_translation/burmese/pi-6-burmese-plain-rails_split_chapters" if "--rails" in sys.argv else
                       "AI_translation/burmese/pi-6-burmese-plain-zeroshot_split_chapters"))
g = collections.defaultdict(list)
for l in open(sys.argv[1], encoding="utf-8"):
    f = N(l).strip().split("\t")
    if len(f) == 3 and f[0][:1].isdigit():
        g[(f[1], f[2])].append(f[0])
for (kw, t), ids in sorted(g.items(), key=lambda x: -len(x[1])):
    words = t.split()
    key = words[-1][:6] if len(words) else t
    pre = " ".join(words[:-1])
    c = collections.Counter()
    for i in ids:
        for m in re.finditer(r"(\S+ ){0,3}" + re.escape(key) + r"\S*", B[i]):
            c[m.group(0)] += 1
    print(f"=== {kw} ×{len(ids)} «{t}»")
    for k, v in c.most_common(12):
        print(f"   {v:4d}  {k}")
