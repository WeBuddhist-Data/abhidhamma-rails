"""KWIC for 3-02..3-06: for each keyword, the segments where it is listed: Pāli context (±W chars) and the
Hindi parentheticals / short Hindi, plus the current value.
usage: python -I -B -X utf8 kwic_3-02_3-06_hi.py <file|all> n kw1 kw2 ...
"""
import sys, re, pathlib; sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import *  # noqa
import importlib.util  # noqa
_sp = importlib.util.spec_from_file_location("m3", pathlib.Path(__file__).resolve().parent / "map_3-02_3-06_hi.py")
M = importlib.util.module_from_spec(_sp); _sp.loader.exec_module(M)

files = M.FILES if sys.argv[1] == "all" else [sys.argv[1]]
n = int(sys.argv[2])
W = 90
tab = {**PI7, **M.T}
for kw in sys.argv[3:]:
    print("#" * 6, kw)
    shown = 0
    for f in files:
        hi, pa = read_hindi(f), read_pali(f)
        for bid, kws in read_keywords(f):
            if kw not in kws or shown >= n:
                continue
            shown += 1
            p = pa.get(bid, "")
            m = re.search(re.escape(kw), p) or re.search(re.escape(kw), p, re.I)
            pc = p[max(0, m.start() - W): m.end() + W] if m else p[:2 * W]
            h = hi.get(bid, "")
            par = re.findall(r"\([^()]{6,}\)", h)
            hs = h if len(h) < 400 else " || ".join(par) or h[-300:]
            o = M.OVR.get(f, {}).get(bid, {})
            try:
                v = o[kw] if kw in o else pi7_value(kw, kws, tab, pa.get(bid), hi.get(bid))[0]
            except KeyError:
                v = "???"
            print(f"  [{f[:4]} {bid}] PA: …{pc.replace(chr(10), ' / ')}…")
            print(f"      HI: {hs.replace(chr(10), ' / ')}")
            print(f"      = {v}  {'OK' if present(v, h) else 'MISS'}")
