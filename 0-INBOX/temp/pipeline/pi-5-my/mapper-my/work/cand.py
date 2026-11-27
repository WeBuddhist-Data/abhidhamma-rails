"""candidate Burmese n-grams for a keyword: present in most of its segments, rare elsewhere (scratch helper)."""
import sys, pathlib, re, collections, math
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
import map5_rules as R
segs = {}
kwsegs = collections.defaultdict(set)
for ch in R.CHAPTERS:
    my = R.burmese(ch)
    for sid, kws in R.keyword_rows(ch):
        segs[(ch, sid)] = my.get(sid, "")
        for k in kws:
            kwsegs[k].add((ch, sid))
def grams(t):
    toks = re.sub(r"[“”‘’\[\]()၊။…–]", " ", t).split()
    out = set()
    for n in (1, 2, 3):
        for i in range(len(toks) - n + 1):
            out.add(" ".join(toks[i:i+n]))
    return out
G = {k: grams(v) for k, v in segs.items()}
df = collections.Counter()
for g in G.values():
    df.update(g)
N = len(G)
for kw in sys.argv[1:]:
    S = kwsegs[kw]
    c = collections.Counter()
    for s in S:
        c.update(G[s])
    sc = sorted(((c[g] / len(S)) * math.log(N / df[g]), g, c[g]) for g in c if c[g] >= max(1, len(S) * 0.5))
    print(kw, len(S), " | ".join(f"{g} ({n})" for _, g, n in sc[::-1][:8]))
