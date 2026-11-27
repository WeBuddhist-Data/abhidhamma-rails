"""Book-wide scan of the pi-1 Burmese keyword mapping: every keyword with more than one value.
usage: python3 -I -X utf8 harmonise_map_scan.py [out.tsv] [--dir DIR]
Prints: keyword <TAB> n values <TAB> value (count; chapters) | ..."""
import sys, pathlib, collections

HERE = pathlib.Path(__file__).resolve().parent
args = sys.argv[1:]
d = HERE
if "--dir" in args:
    i = args.index("--dir")
    d = pathlib.Path(args[i + 1])
    del args[i:i + 2]
ORDER = ["preamble", "1-matika", "2-01", "2-02", "2-03", "2-04", "2-05", "3-01", "3-02", "3-03",
         "4-01", "4-02", "4-03", "5"]


def short(name):
    for o in ORDER:
        if name.startswith(o):
            return o
    return name


vals = collections.defaultdict(lambda: collections.defaultdict(collections.Counter))
for f in sorted(d.glob("*.mapped.md")):
    ch = short(f.name)
    for l in f.read_text(encoding="utf-8").splitlines():
        sid, rest = l.split("] ", 1)
        for kv in rest.split(", "):
            k, v = kv.split("=", 1)
            vals[k[:1].lower() + k[1:]][v][ch] += 1  # first letter case-insensitive, as the tables
rows = []
for k in sorted(vals, key=lambda x: (x.lower(), x)):
    if len(vals[k]) > 1:
        parts = []
        for v, chs in sorted(vals[k].items(), key=lambda x: -sum(x[1].values())):
            parts.append(f"{v} ({sum(chs.values())}; " + " ".join(c for c in ORDER if c in chs) + ")")
        rows.append(f"{k}\t{len(vals[k])}\t" + " | ".join(parts))
out = "\n".join(rows) + "\n"
if args:
    pathlib.Path(args[0]).write_text(out, encoding="utf-8")
print(f"keywords {len(vals)} | with >1 value {len(rows)}")
if not args:
    print(out)
