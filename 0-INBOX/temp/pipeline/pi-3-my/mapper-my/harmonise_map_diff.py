"""Read-only: values changed by the map-harmonise pass (current *.mapped.md against harmonise-backup/mapped/).
usage: python3 -I -X utf8 harmonise_map_diff.py [--all]   (--all: every changed pair; default: grouped counts)"""
import sys, pathlib, collections

HERE = pathlib.Path(__file__).resolve().parent
per_ch, groups, rows = collections.Counter(), collections.Counter(), []
for f in sorted(HERE.glob("*.mapped.md"), key=lambda p: (p.name != "preamble.mapped.md", int(p.name.split("-")[0]) if p.name[0].isdigit() else 0)):
    old = (HERE / "harmonise-backup/mapped" / f.name).read_text(encoding="utf-8").splitlines()
    new = f.read_text(encoding="utf-8").splitlines()
    assert [l.split("] ")[0] for l in old] == [l.split("] ")[0] for l in new]
    ch = f.name.split(".")[0]
    per_ch[ch] += 0
    for a, b in zip(old, new):
        sid = a.split("] ")[0][1:]
        pa = a.split("] ", 1)[1].split(", ")
        pb = b.split("] ", 1)[1].split(", ")
        assert [x.split("=", 1)[0] for x in pa] == [x.split("=", 1)[0] for x in pb]
        for x, y in zip(pa, pb):
            if x != y:
                k, v0 = x.split("=", 1)
                v1 = y.split("=", 1)[1]
                per_ch[ch] += 1
                groups[(ch, k, v0, v1)] += 1
                rows.append(f"{ch}\t{sid}\t{k}\t{v0}\t->\t{v1}")
print("values changed:", sum(per_ch.values()), "|", " · ".join(f"{c}: {n}" for c, n in per_ch.items()))
for (ch, k, v0, v1), n in groups.items():
    print(f"  {ch}\t{k}\t«{v0}» -> «{v1}»\t{n}")
if "--all" in sys.argv:
    print("\n".join(rows))
