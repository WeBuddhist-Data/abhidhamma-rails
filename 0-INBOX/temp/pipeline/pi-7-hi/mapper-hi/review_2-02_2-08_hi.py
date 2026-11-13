"""Review the mapped files: every distinct kw=value with count and first ids (multi-valued keywords marked *).

usage: python -I -B -X utf8 review_2-02_2-08_hi.py <file> … [--multi]
"""
import sys, pathlib, collections
sys.dont_write_bytecode = True
HERE_ = pathlib.Path(__file__).resolve().parent
multi = "--multi" in sys.argv
args = sys.argv[1:]
base = []
if "--base" in args:
    i = args.index("--base")
    base, args = args[i + 1:], args[:i]


def load(f):
    d = collections.defaultdict(lambda: collections.defaultdict(list))
    for l in (HERE_ / f"{f}.mapped.md").read_text(encoding="utf-8").splitlines():
        b, _, r = l.partition("] ")
        if not r:
            continue
        for p in r.split(", "):
            k, v = p.split("=", 1)
            d[k][v].append(b[1:])
    return d


known = set()
for bf in base:
    for k, vs in load(bf).items():
        for v in vs:
            known.add((k.lower(), v))
for f in [a for a in args if not a.startswith("--")]:
    d = load(f)
    print("=" * 10, f)
    for k in sorted(d, key=lambda x: x.lower()):
        vs = d[k]
        if multi and len(vs) < 2:
            continue
        if all((k.lower(), v) in known for v in vs):
            continue
        star = "*" if len(vs) > 1 else " "
        print(star, k, " | ".join(f"{v} x{len(ids)} {sorted(set(ids))[:3]}" for v, ids in vs.items()))
