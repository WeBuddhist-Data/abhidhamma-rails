"""kwstats.py [ch …]: distinct keywords with use counts (all chapters when none given)."""
import sys, re, pathlib, collections
D = pathlib.Path(__file__).resolve().parents[1]
chs = sys.argv[1:] or sorted(p.name[:-12] for p in D.glob("*.keywords.md"))
c = collections.Counter(); seg = collections.Counter()
for ch in chs:
    for l in (D / f"{ch}.keywords.md").read_text(encoding="utf-8").splitlines():
        ks = [k.strip() for k in l.split("] ", 1)[1].split(", ")]
        c.update(ks); seg.update(set(ks))
print(len(c), sum(c.values()))
for k, n in c.most_common():
    print(n, seg[k], k)
