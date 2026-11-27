"""Book-wide scan of the pi-7 Burmese keyword mapping (model: pi-6-my/mapper-my/work/map_scan.py, copied, not
imported): every keyword with more than one value (first letter case-insensitive, as the tables).
usage: python3 -I -X utf8 work/map_scan.py [out.tsv] [--detail out.txt] [--dir DIR]"""
import sys, pathlib, collections
HERE = pathlib.Path(__file__).resolve().parent.parent
args = sys.argv[1:]
d, detail = HERE, None
if "--dir" in args:
    i = args.index("--dir"); d = pathlib.Path(args[i + 1]); del args[i:i + 2]
if "--detail" in args:
    i = args.index("--detail"); detail = pathlib.Path(args[i + 1]); del args[i:i + 2]
sys.path.insert(0, str(HERE)); sys.dont_write_bytecode = True
import map7_rules as R


def short(c):
    return c if c == "preamble" else "-".join(c.split("-")[:2])


ORDER = [short(c) for c in R.chapters()]
vals = collections.defaultdict(lambda: collections.defaultdict(collections.Counter))
segs = collections.defaultdict(lambda: collections.defaultdict(list))
for c in R.chapters():
    for l in (d / f"{c}.mapped.md").read_text(encoding="utf-8").splitlines():
        sid, rest = l.split("] ", 1)
        for kv in rest.split(", "):
            k, v = kv.split("=", 1)
            kk = R.low(k)
            vals[kk][v][short(c)] += 1
            segs[kk][v].append(sid[1:])
rows, det = [], []
for k in sorted(vals, key=lambda x: (x.lower(), x)):
    if len(vals[k]) > 1:
        parts = []
        det.append(f"== {k}")
        for v, chs in sorted(vals[k].items(), key=lambda x: (-sum(x[1].values()), x[0])):
            parts.append(f"{v} ({sum(chs.values())}; " + " ".join(c for c in ORDER if c in chs) + ")")
            det.append(f"   {v}\t{len(segs[k][v])}\t" + " ".join(segs[k][v][:40]))
        rows.append(f"{k}\t{len(vals[k])}\t" + " | ".join(parts))
out = "\n".join(rows) + "\n"
if args:
    pathlib.Path(args[0]).write_text(out, encoding="utf-8")
if detail:
    detail.write_text("\n".join(det) + "\n", encoding="utf-8")
print(f"keywords {len(vals)} | with >1 value {len(rows)} | uses {sum(sum(sum(c.values()) for c in v.values()) for v in vals.values())}")
