"""Probe for 2-02..2-08: unmapped keywords, fallback values, presence misses (no files written).

usage: python -I -B -X utf8 probe_2-02_2-08_hi.py <file> [<file> …]
"""
import sys, pathlib, collections
sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import *  # noqa
import importlib.util
_sp = importlib.util.spec_from_file_location("m0208", pathlib.Path(__file__).resolve().parent / "map_2-02_2-08_hi.py")
_m = importlib.util.module_from_spec(_sp); _sp.loader.exec_module(_m)
T, OVR_ALL = _m.T, _m.OVR_ALL

for f in sys.argv[1:]:
    hi, pa = read_hindi(f), read_pali(f)
    table = {**PI7, **T}
    ovr = OVR_ALL.get(f, {})
    unm = collections.Counter()
    fb = collections.defaultdict(collections.Counter)
    miss = collections.defaultdict(list)
    for bid, kws in read_keywords(f):
        text = hi.get(bid)
        for kw in kws:
            o = ovr.get(bid, {})
            if kw in o:
                v, src = o[kw], "override"
            else:
                try:
                    v, src = pi7_value(kw, kws, table, pa.get(bid), text)
                except KeyError:
                    unm[kw] += 1
                    continue
            if src not in ("table", "heading", "override"):
                fb[(kw, v, src)][bid] += 1
            if v != NDE and not present(v, text):
                miss[(kw, v)].append(bid)
    print("=" * 10, f)
    print("UNMAPPED", len(unm))
    for k, c in sorted(unm.items(), key=lambda x: lc(x[0])):
        print("  ", k, c)
    print("FALLBACK", len(fb))
    for (k, v, s), c in sorted(fb.items(), key=lambda x: lc(x[0][0])):
        print("  ", k, "=", v, s, sum(c.values()), list(c)[:4])
    print("MISS", len(miss))
    for (k, v), b in sorted(miss.items(), key=lambda x: lc(x[0][0])):
        print("  ", k, "=", v, len(b), b[:6])
