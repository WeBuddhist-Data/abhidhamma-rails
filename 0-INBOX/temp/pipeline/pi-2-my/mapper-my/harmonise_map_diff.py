"""Values changed by the map-harmonise pass: harmonise-backup/mapped/*.mapped.md (before) vs *.mapped.md (now).
usage: python3 -I -X utf8 harmonise_map_diff.py [-v]   (-v lists every change)"""
import sys, pathlib, collections
HERE = pathlib.Path(__file__).resolve().parent
B = HERE / "harmonise-backup/mapped"
per_ch, pairs = collections.Counter(), collections.Counter()
for f in sorted(HERE.glob("*.mapped.md"), key=lambda p: (p.name.split("-")[0] != "preamble", int(p.name.split("-")[0]) if p.name[0].isdigit() else 0)):
    a = (B / f.name).read_text(encoding="utf-8").splitlines()
    b = f.read_text(encoding="utf-8").splitlines()
    assert len(a) == len(b)
    for x, y in zip(a, b):
        if x == y:
            continue
        sx, rx = x.split("] ", 1); sy, ry = y.split("] ", 1)
        assert sx == sy
        for p, q in zip(rx.split(", "), ry.split(", ")):
            if p != q:
                k = p.split("=", 1)[0]
                per_ch[f.name.split(".")[0]] += 1
                pairs[(k[:1].lower() + k[1:], p.split("=", 1)[1], q.split("=", 1)[1])] += 1
                if "-v" in sys.argv:
                    print(f"{sx[1:]:12} {k}: {p.split('=', 1)[1]} -> {q.split('=', 1)[1]}")
print("changed values per chapter:", dict(per_ch), "total", sum(per_ch.values()))
for (k, o, n), c in sorted(pairs.items()):
    print(f"  {c:3}  {k}: {o} -> {n}")
