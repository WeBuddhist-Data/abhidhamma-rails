"""dev_g5.py: g5 diagnostics (read-only on the vault; writes nothing): unmapped keywords and stem-fallback values of
the g5 chapters with the segment's Pāli / Burmese, under the current map_g5 tables."""
import sys, re, pathlib, collections
sys.dont_write_bytecode = True
D = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(D))
import map7_rules as R
import map_g5 as G
M = G.mapper()
mode = sys.argv[1] if len(sys.argv) > 1 else "all"
un = collections.defaultdict(list)
st = collections.defaultdict(list)
for ch in G.CHAPTERS:
    my, pa = R.burmese(ch), R.pali(ch)
    for sid, kws in R.keyword_rows(ch):
        for kw in kws:
            try:
                v = M.lookup(ch, sid, kw, pa.get(sid, ""), my[sid])
            except KeyError:
                un[kw].append((ch, sid))
                continue
            if M.SRC.get((sid, kw)) == "stem":
                st[(kw, v)].append((ch, sid))
def ctx(ch, sid, kw, n=500):
    p = R.pali(ch).get(sid, ""); b = R.burmese(ch).get(sid, "")
    i = R.low(p).find(R.low(kw)[:max(4, len(kw)-3)])
    return p[max(0, i-200):i+300], b
if mode in ("all", "un"):
    print("UNMAPPED", sum(len(x) for x in un.values()), "uses", len(un), "keywords")
    for kw, locs in sorted(un.items(), key=lambda x: -len(x[1])):
        print(f"## {kw} ({len(locs)}): " + " ".join(f"{c[:4]}^{s}" for c, s in locs[:8]))
        if "-v" in sys.argv:
            c, s = locs[0]
            p, b = ctx(c, s, kw)
            print("   PI:", p.replace("\n", " ")[:500]); print("   MY:", b.replace("\n", " ")[:900])
if mode in ("all", "st"):
    print("STEM", sum(len(x) for x in st.values()), "uses", len(st), "pairs")
    for (kw, v), locs in sorted(st.items(), key=lambda x: -len(x[1])):
        print(f"## {kw} = {v} ({len(locs)}): " + " ".join(f"{c[:4]}^{s}" for c, s in locs[:8]))
        if "-v" in sys.argv:
            c, s = locs[0]
            p, b = ctx(c, s, kw)
            print("   PI:", p.replace("\n", " ")[:500]); print("   MY:", b.replace("\n", " ")[:900])
