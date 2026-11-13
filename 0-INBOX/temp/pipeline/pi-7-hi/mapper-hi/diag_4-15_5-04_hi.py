"""Diagnostics for 4-15 … 5-04 (my files): unmapped keywords, fallback-sourced values, presence misses.
usage: python -I -B -X utf8 diag_4-15_5-04_hi.py <file> [missing|fallback|miss|all]
Uses the T / OVR of map_4-15_5-04_hi.py (loaded by path, its __main__ does not run).
"""
import sys, pathlib, collections, importlib.util
sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from map_sample_hi import *  # noqa
from map_sample_hi import read_keywords, read_hindi, read_pali, lc, NDE

spec = importlib.util.spec_from_file_location("m41504", HERE / "map_4-15_5-04_hi.py")
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

f = sys.argv[1]
mode = sys.argv[2] if len(sys.argv) > 2 else "all"
table = {**PI7, **m.T, **m.FT.get(f, {})}
ovr = m.OVR.get(f, {})
log = {}
res = make_resolver(f, table, ovr, log)
hi = read_hindi(f)
missing = collections.Counter()
misses = []
for bid, kws in read_keywords(f):
    for kw in kws:
        try:
            v = res(bid, kw, kws)
        except KeyError:
            missing[kw] += 1
            continue
        if v != NDE and not present(v, hi.get(bid)):
            misses.append((bid, kw, v))
if mode in ("missing", "all"):
    print("MISSING", len(missing))
    for k, c in sorted(missing.items(), key=lambda x: lc(x[0])):
        print("  ", k, c)
if mode in ("fallback", "all"):
    print("FALLBACK")
    by = collections.defaultdict(list)
    for (kw, v), c in log.items():
        by[kw].append((v, dict(c)))
    for kw in sorted(by, key=lc):
        if all(set(c) <= {"table", "override"} for _, c in by[kw]):
            continue
        print("  ", kw, "->", "; ".join(f"{v} {c}" for v, c in by[kw]))
if mode in ("miss", "all"):
    print("PRESENCE MISSES", len(misses))
    for x in misses[:300]:
        print("  ", *x)
