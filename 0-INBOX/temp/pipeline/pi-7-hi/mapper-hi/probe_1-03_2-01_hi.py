"""Probe for 1-03/1-04/1-05/2-01: unmapped keywords (with counts) and presence misses using PI7 + the
chapter table T from map_1-03_2-01_hi.py (if importable). Writes nothing.
usage: python -I -B -X utf8 probe_1-03_2-01_hi.py <file> [unmapped|miss|both]
"""
import sys, pathlib, collections
sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import *  # noqa
from map_sample_hi import read_keywords, read_hindi, read_pali, pi7_value, present, PI7

import importlib.util
_p = pathlib.Path(__file__).resolve().parent / "map_1-03_2-01_hi.py"
if _p.exists():
    _s = importlib.util.spec_from_file_location("map_1_03_2_01_hi", _p)
    M = importlib.util.module_from_spec(_s)
    _s.loader.exec_module(M)
    T, OVRS = M.T, M.OVRS
else:
    T, OVRS = {}, {}

f = sys.argv[1]
mode = sys.argv[2] if len(sys.argv) > 2 else "both"
table = {**PI7, **T}
ovr = OVRS.get(f, {})
hi, pa = read_hindi(f), read_pali(f)
unm = collections.Counter()
unm_ex = {}
miss = collections.defaultdict(list)
for bid, kws in read_keywords(f):
    for kw in kws:
        o = ovr.get(bid, {})
        if kw in o:
            v = o[kw]
        else:
            try:
                v, src = pi7_value(kw, kws, table, pa.get(bid), hi.get(bid))
            except KeyError:
                unm[kw] += 1
                unm_ex.setdefault(kw, bid)
                continue
        if not present(v, hi.get(bid)):
            miss[(kw, v)].append(bid)
if mode in ("unmapped", "both"):
    print("UNMAPPED", len(unm))
    for k, c in unm.most_common():
        print(f"  {k}\t{c}\t{unm_ex[k]}")
if mode in ("miss", "both"):
    print("MISSES", sum(len(v) for v in miss.values()))
    for (k, v), ids in sorted(miss.items(), key=lambda x: -len(x[1])):
        print(f"  {k}={v}\t{len(ids)}\t{' '.join(ids[:6])}")
