"""Audit for 1-03/1-04/1-05/2-01: each keyword, its values and their sources (PI7 + chapter T + OVR),
skipping unmapped. usage: python -I -B -X utf8 audit_1-03_2-01_hi.py <file> [fallback|all]
"""
import sys, pathlib, collections, importlib.util
sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import read_keywords, read_hindi, read_pali, pi7_value, PI7, lc

_p = pathlib.Path(__file__).resolve().parent / "map_1-03_2-01_hi.py"
T, OVRS = {}, {}
if _p.exists():
    _s = importlib.util.spec_from_file_location("map_1_03_2_01_hi", _p)
    M = importlib.util.module_from_spec(_s)
    _s.loader.exec_module(M)
    T, OVRS = M.T, M.OVRS
f = sys.argv[1]
only_fb = (sys.argv[2] if len(sys.argv) > 2 else "fallback") == "fallback"
table = {**PI7, **T}
ovr = OVRS.get(f, {})
hi, pa = read_hindi(f), read_pali(f)
log = collections.defaultdict(collections.Counter)
ex = {}
for bid, kws in read_keywords(f):
    for kw in kws:
        if kw in ovr.get(bid, {}):
            v, s = ovr[bid][kw], "override"
        else:
            try:
                v, s = pi7_value(kw, kws, table, pa.get(bid), hi.get(bid))
            except KeyError:
                continue
        log[kw][(v, s)] += 1
        ex.setdefault((kw, v), bid)
for kw in sorted(log, key=lc):
    vals = log[kw]
    if only_fb and all(s in ("table", "heading", "override") for (v, s) in vals):
        continue
    print(kw, "->", "; ".join(f"{v} [{s} {c} e.g. {ex[(kw, v)]}]" for (v, s), c in vals.items()))
