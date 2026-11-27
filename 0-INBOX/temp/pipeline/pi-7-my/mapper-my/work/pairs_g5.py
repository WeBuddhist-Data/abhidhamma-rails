"""pairs_g5.py [src-prefix …]: every distinct (keyword, value, source) of the g5 chapters with uses (read-only)."""
import sys, pathlib, collections
sys.dont_write_bytecode = True
D = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(D))
import map7_rules as R
import map_g5 as G
M = G.mapper()
c = collections.Counter(); loc = {}
for ch in G.CHAPTERS:
    my, pa = R.burmese(ch), R.pali(ch)
    for sid, kws in R.keyword_rows(ch):
        for kw in kws:
            try:
                v = M.lookup(ch, sid, kw, pa.get(sid, ""), my[sid])
            except KeyError:
                v = "?"
            s = (M.SRC.get((sid, kw)) or "?")
            c[(kw, v, s)] += 1
            loc.setdefault((kw, v, s), f"{ch[:4]}^{sid}")
skip = set(a for a in sys.argv[1:] if a.startswith("-"))
for (kw, v, s), n in sorted(c.items(), key=lambda x: (x[0][2].split(":")[-1], R.low(x[0][0]))):
    if any(s.split(":")[-1].startswith(x[1:]) for x in skip):
        continue
    print(f"{s}\t{kw}\t{v}\t{n}\t{loc[(kw, v, s)]}")
print("pairs", len(c))
