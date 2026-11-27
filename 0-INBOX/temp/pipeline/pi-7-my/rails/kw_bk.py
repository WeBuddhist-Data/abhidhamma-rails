"""Inspection helper: count Burmese renderings around a Pāli phrase. usage: kw_bk.py <pāli regex> <burmese regex> [--bk]"""
import collections, pathlib, re, sys, unicodedata
HERE = pathlib.Path(__file__).resolve().parent; ROOT = HERE.parents[4]
N = lambda s: unicodedata.normalize("NFC", s)
PD = ROOT / "AI_translation/pali/pi-7_split_chapters"
BD = HERE.parent / "review/fix-backup/rails-text"
prx, brx = re.compile(N(sys.argv[1])), re.compile(N(sys.argv[2]))
c = collections.Counter(); where = collections.defaultdict(list)
for p in sorted(PD.glob("*.md")):
    pl = N(p.read_text(encoding="utf-8-sig")).split("\n"); bl = N((BD / p.name).read_text(encoding="utf-8")).split("\n")
    for k, (a, b) in enumerate(zip(pl, bl), 1):
        n = len(prx.findall(a))
        if n:
            ms = brx.findall(b)
            key = (n, tuple(sorted(collections.Counter(ms).items())))
            c[key] += 1; where[key].append(f"{p.name[:4]}:{k}")
for k, v in c.most_common():
    print(v, k, where[k][:6])
