"""Show Pāli, Hindi and keywords (with the current values) for segments.
usage: python -I -B -X utf8 show_3-02_3-06_hi.py <file> id1 id2 ...      (max chars per text: env-free, 1500)
       python -I -B -X utf8 show_3-02_3-06_hi.py <file> --kw keyword [n]   (segments with that keyword)
"""
import sys, pathlib; sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import *  # noqa
import importlib.util  # noqa
_sp = importlib.util.spec_from_file_location("m3", pathlib.Path(__file__).resolve().parent / "map_3-02_3-06_hi.py")
M = importlib.util.module_from_spec(_sp); _sp.loader.exec_module(M)

f = sys.argv[1]
hi, pa = read_hindi(f), read_pali(f)
kwd = dict(read_keywords(f))
args = sys.argv[2:]
NOPA = "--nopa" in args
args = [a for a in args if a != "--nopa"]
if args and args[0] == "--kw":
    n = int(args[2]) if len(args) > 2 else 3
    ids = [b for b, k in kwd.items() if args[1] in k][:n]
else:
    ids = args
tab = {**PI7, **M.T}
for b in ids:
    print("=" * 8, b)
    if not NOPA:
        print("PA:", (pa.get(b) or "")[:2500])
    print("HI:", (hi.get(b) or "")[:2500])
    out = []
    for kw in kwd.get(b, []):
        o = M.OVR.get(f, {}).get(b, {})
        try:
            v = o[kw] if kw in o else pi7_value(kw, kwd[b], tab, pa.get(b), hi.get(b))[0]
        except KeyError:
            v = "???"
        out.append(f"{kw}={v}")
    print("KW:", ", ".join(out))
