"""Heading segments with keywords and current resolution. usage: heads_1-03_2-01_hi.py <file> [all]"""
import sys, pathlib, importlib.util
sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import read_keywords, read_hindi, read_pali, pi7_value, PI7

_p = pathlib.Path(__file__).resolve().parent / "map_1-03_2-01_hi.py"
T, OVRS = {}, {}
if _p.exists():
    _s = importlib.util.spec_from_file_location("map_1_03_2_01_hi", _p)
    M = importlib.util.module_from_spec(_s)
    _s.loader.exec_module(M)
    T, OVRS = M.T, M.OVRS
f = sys.argv[1]
hi, pa = read_hindi(f), read_pali(f)
table = {**PI7, **T}
seen = set()
for bid, kws in read_keywords(f):
    p = pa.get(bid) or ""
    if not p.startswith("#"):
        continue
    out = []
    for kw in kws:
        o = OVRS.get(f, {}).get(bid, {})
        if kw in o:
            out.append(f"{kw}={o[kw]}[ovr]")
            continue
        try:
            v, s = pi7_value(kw, kws, table, p, hi.get(bid))
            out.append(f"{kw}={v}[{s}]")
        except KeyError:
            out.append(f"{kw}=???")
    if "all" not in sys.argv and all(x.endswith("[heading]") for x in out):
        continue
    key = (p.lstrip("#").strip(), tuple(out))
    if key in seen and "all" not in sys.argv:
        continue
    seen.add(key)
    print(bid, "|", p.lstrip("#").strip(), "|", (hi.get(bid) or "").lstrip("#").strip(), "|", ", ".join(out))
