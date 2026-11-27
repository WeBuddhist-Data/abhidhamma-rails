"""usage: diff3.py [--tsv OUT] — every value that differs between work/phase2-mapped/*.mapped.md and the current
*.mapped.md: chapter, segment, keyword, old, new (and the SRC of the new value if a map log is given)"""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
D = HERE.parent
rows = []
for f in sorted((HERE / "phase2-mapped").glob("*.mapped.md")):
    old = f.read_text(encoding="utf-8").splitlines()
    new = (D / f.name).read_text(encoding="utf-8").splitlines()
    assert len(old) == len(new), f.name
    for a, b in zip(old, new):
        sa, ra = a.split("] ", 1)
        sb, rb = b.split("] ", 1)
        assert sa == sb
        ka, kb = ra.split(", "), rb.split(", ")
        assert len(ka) == len(kb), sa
        for x, y in zip(ka, kb):
            k1, v1 = x.split("=", 1)
            k2, v2 = y.split("=", 1)
            assert k1 == k2
            if v1 != v2:
                rows.append((f.name.split(".")[0], sa[1:], k1, v1, v2))
for r in rows:
    print("\t".join(r))
print("changes", len(rows), file=sys.stderr)
