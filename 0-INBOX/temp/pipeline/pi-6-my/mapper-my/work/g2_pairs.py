"""read-only helper (g2): distinct keyword = value pairs of a mapped group chapter with uses, source and one sid."""
import sys, pathlib, collections
HERE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE))
import map6_rules as R
import map_g2 as G
M = G.mapper()
for ch in sys.argv[1:]:
    lines, problems, unmapped, nne = M.map_chapter(ch)
    c = collections.Counter(); ex = {}; src = {}
    for l in lines:
        sid, rest = l[1:].split("] ", 1)
        for kv in rest.split(", "):
            k, v = kv.split("=", 1)
            c[(k, v)] += 1; ex.setdefault((k, v), sid); src.setdefault((k, v), M.SRC.get((sid, k), "?"))
    print(f"== {ch} pairs {len(c)}")
    for (k, v), n in sorted(c.items(), key=lambda x: (R.low(x[0][0]), x[0][1])):
        print(f"{k} = {v} | {n} | {src[(k, v)]} | ^{ex[(k, v)]}")
