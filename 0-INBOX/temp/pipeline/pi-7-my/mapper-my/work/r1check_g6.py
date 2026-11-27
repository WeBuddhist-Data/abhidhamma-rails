"""r1check_g6.py: R1 check over the g6 output: a «-ñca / -ñceva / -ca / -pi / -ti» keyword whose value differs from
the value the mapper gives its base form in the same segment."""
import sys, pathlib, collections
sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
import map_g6 as G
import map7_rules as R
M = G.mapper()
out = collections.Counter()
for ch in G.G6:
    my, pa = R.burmese(ch), R.pali(ch)
    G._M["ch"] = ch
    for sid, kws in R.keyword_rows(ch):
        for kw in kws:
            b = R.base_forms(kw)
            if not b:
                continue
            try:
                v = M.lookup(ch, sid, kw, pa.get(sid, ""), my[sid])
            except KeyError:
                continue
            for x in b:
                try:
                    bv = R.finish(M._lookup(ch, "__chk__", x, pa.get(sid, ""), my[sid]))
                except KeyError:
                    continue
                if bv != v:
                    out[(kw, v, x, bv, M.SRC.get((sid, kw)))] += 1
                    out[("@where", kw, ch, sid)] += 0
                break
for k, n in sorted(out.items(), key=lambda x: str(x[0])):
    if k[0] != "@where":
        print(n, k)
