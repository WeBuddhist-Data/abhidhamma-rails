"""List unmapped keywords of the given files with one Pāli snippet each (no files written).

usage: python -I -B -X utf8 unm_2-02_2-08_hi.py <file> …
"""
import sys, pathlib, re, collections, importlib.util
sys.dont_write_bytecode = True
HERE_ = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE_))
from map_sample_hi import *  # noqa
_sp = importlib.util.spec_from_file_location("m0208", HERE_ / "map_2-02_2-08_hi.py")
_m = importlib.util.module_from_spec(_sp); _sp.loader.exec_module(_m)
table = {**PI7, **_m.T}
seen = collections.OrderedDict()
for f in sys.argv[1:]:
    hi, pa = read_hindi(f), read_pali(f)
    ovr = _m.OVR_ALL.get(f, {})
    for bid, kws in read_keywords(f):
        for kw in kws:
            if kw in ovr.get(bid, {}):
                continue
            try:
                pi7_value(kw, kws, table, pa.get(bid), hi.get(bid))
            except KeyError:
                if kw not in seen:
                    p = pa.get(bid, "")
                    m = re.search(re.escape(kw[:max(4, len(kw) - 2)]), p, re.I)
                    sn = p[max(0, m.start() - 60): m.end() + 60].replace("\n", " ") if m else p[:120]
                    seen[kw] = [f[:4], bid, 0, sn]
                seen[kw][2] += 1
for kw, (f, bid, c, sn) in seen.items():
    print(f"{kw} | {f} {bid} x{c} | {sn}")
