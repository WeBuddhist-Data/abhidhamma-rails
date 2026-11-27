"""g1 helper: uses whose final value (map_g1) differs from the module-only value, per keyword."""
import sys, pathlib, collections
sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE))
import map7_rules as R
import map_g1 as G
M0 = R.Mapper(stem=R.make_stem([R.FRAME, R.STOCK, R.LEXW]))
c = collections.Counter()
for ch in G.G1:
    a = M0.map_chapter(ch)[0]
    b = (HERE / f"{ch}.mapped.md").read_text(encoding="utf-8").splitlines()
    for x, y in zip(a, b):
        for p, q in zip(x.split("] ", 1)[1].split(", "), y.split("] ", 1)[1].split(", ")):
            if p != q:
                c[(ch, p, q.split("=", 1)[1])] += 1
for (ch, p, q), n in sorted(c.items()):
    print(f"{ch}\t{p}\t-> {q}\t{n}")
print("total", sum(c.values()))
