"""pairs_g6.py: distinct keyword = value pairs of the g6 chapters as map_g6.py gives them (nothing written but
work/pairs-g6.txt): uses, source, first segment."""
import sys, pathlib, collections
sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
import map_g6 as G
import map7_rules as R
M = G.mapper()
pairs, src, first = collections.Counter(), {}, {}
for ch in G.G6:
    lines, problems, unmapped, nne = G.map_chapter(M, ch)
    for l in lines:
        sid, rest = l[1:].split("] ", 1)
        for kv in rest.split(", "):
            k, v = kv.split("=", 1)
            pairs[(k, v)] += 1
            src.setdefault((k, v), M.SRC.get((sid, k)) or "?")
            first.setdefault((k, v), f"{ch} {sid}")
with open(HERE / "work/pairs-g6.txt", "w", encoding="utf-8") as f:
    for (k, v), n in sorted(pairs.items(), key=lambda x: (R.low(x[0][0]), x[0][1])):
        f.write(f"{k}\t{v}\t{n}\t{src[(k, v)]}\t{first[(k, v)]}\n")
print(len(pairs), "pairs")
