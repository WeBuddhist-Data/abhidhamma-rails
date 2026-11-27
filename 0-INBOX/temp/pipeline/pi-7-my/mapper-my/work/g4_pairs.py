"""g4_pairs.py: the distinct keyword / value / source triples of the g4 chapters (read-only helper)."""
import sys, pathlib, collections
sys.dont_write_bytecode = True
D = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(D))
import map7_rules as R
import map_g4 as G
M = G.mapper()
c = collections.Counter(); ex = {}
for ch in G.CHAPTERS:
    lines, *_ = M.map_chapter(ch)
    for l in lines:
        sid, rest = l[1:].split("] ", 1)
        for kv in rest.split(", "):
            k, v = kv.split("=", 1)
            s = (M.SRC.get((sid, k)) or "?")
            c[(s.split(":")[-1], k, v)] += 1; ex.setdefault((s.split(":")[-1], k, v), f"{ch[:4]} {sid}")
L = [f"{s}\t{k}\t{v}\t{n}\t{ex[(s,k,v)]}" for (s, k, v), n in sorted(c.items(), key=lambda x: (x[0][0], R.low(x[0][1])))]
(D / "work" / "g4-pairs.tsv").write_text("\n".join(L) + "\n", encoding="utf-8")
print(len(L), collections.Counter(x[0] for x in c).most_common())
