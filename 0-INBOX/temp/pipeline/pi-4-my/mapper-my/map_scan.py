"""Book-wide scan of the pi-4 Burmese keyword mapping: every keyword with more than one value.
usage: python3 -I -X utf8 harmonise_map_scan.py [out.tsv] [--detail out.txt] [--dir DIR]
Prints: keyword <TAB> n values <TAB> value (count; chapters) | ...   (first letter case-insensitive, as the tables)
--detail writes every value with its segment IDs."""
import sys, pathlib, collections

HERE = pathlib.Path(__file__).resolve().parent
args = sys.argv[1:]
d = HERE
detail = None
if "--dir" in args:
    i = args.index("--dir"); d = pathlib.Path(args[i + 1]); del args[i:i + 2]
if "--detail" in args:
    i = args.index("--detail"); detail = pathlib.Path(args[i + 1]); del args[i:i + 2]
ORDER = ["preamble"] + [str(i) for i in range(1, 12)]


def short(name):
    return name.split("-", 1)[0].split(".", 1)[0]


vals = collections.defaultdict(lambda: collections.defaultdict(collections.Counter))
segs = collections.defaultdict(lambda: collections.defaultdict(list))
for f in sorted(d.glob("*.mapped.md")):
    ch = short(f.name)
    for l in f.read_text(encoding="utf-8").splitlines():
        sid, rest = l.split("] ", 1)
        for kv in rest.split(", "):
            k, v = kv.split("=", 1)
            kk = k[:1].lower() + k[1:]
            vals[kk][v][ch] += 1
            segs[kk][v].append(sid[1:])
rows, det = [], []
for k in sorted(vals, key=lambda x: (x.lower(), x)):
    if len(vals[k]) > 1:
        parts = []
        det.append(f"== {k}")
        for v, chs in sorted(vals[k].items(), key=lambda x: -sum(x[1].values())):
            parts.append(f"{v} ({sum(chs.values())}; " + " ".join(c for c in ORDER if c in chs) + ")")
            det.append(f"   {v}\t{len(segs[k][v])}\t" + " ".join(segs[k][v][:40]))
        rows.append(f"{k}\t{len(vals[k])}\t" + " | ".join(parts))
out = "\n".join(rows) + "\n"
if args:
    pathlib.Path(args[0]).write_text(out, encoding="utf-8")
if detail:
    detail.write_text("\n".join(det) + "\n", encoding="utf-8")
print(f"keywords {len(vals)} | with >1 value {len(rows)}")
if not args:
    print(out)
