"""g4_ruled.py: the chunks of the g4 table / ctx values matched by an ending rule (read-only helper)."""
import sys, pathlib, collections
sys.dont_write_bytecode = True
D = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(D))
import map7_rules as R
import map_g4 as G
keys = {R.low(k) for k in G.G4} | {R.low(k) for t in G.CTX.values() for k in t}
c = collections.Counter(); ex = {}
for ch in G.CHAPTERS:
    for sid, k, chunk, r in R.verify_file(ch)[4]:
        if R.low(k) in keys:
            c[(k, chunk, r)] += 1; ex.setdefault((k, chunk, r), sid)
for (k, chunk, r), n in sorted(c.items()):
    print(f"{k}\t«{chunk}»\t{r}\t{n}\t{ex[(k, chunk, r)]}")
