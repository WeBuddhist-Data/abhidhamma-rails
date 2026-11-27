"""usage: kwvals.py KW [KW…] — values of the keywords in all *.mapped.md (count; segments)"""
import sys, pathlib, collections
d = pathlib.Path(__file__).resolve().parent.parent
want = set(sys.argv[1:])
vals = collections.defaultdict(lambda: collections.defaultdict(list))
for f in sorted(d.glob("*.mapped.md")):
    for l in f.read_text(encoding="utf-8").splitlines():
        sid, rest = l.split("] ", 1)
        for kv in rest.split(", "):
            k, v = kv.split("=", 1)
            if k in want:
                vals[k][v].append(sid[1:])
for k in sys.argv[1:]:
    for v, s in vals[k].items():
        print(k, "|", v, "|", len(s), " ".join(s[:12]))
