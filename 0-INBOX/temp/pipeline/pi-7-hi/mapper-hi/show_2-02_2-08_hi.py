"""Show Pāli, Hindi, keywords (and mapped line if any) for ids, or for segments whose keywords contain a word.

usage: python -I -B -X utf8 show_2-02_2-08_hi.py <file> id … | <file> --kw word [--max N] [--short]
"""
import sys, pathlib
sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import *  # noqa

f = sys.argv[1]
args = sys.argv[2:]
hi, pa = read_hindi(f), read_pali(f)
kw = dict(read_keywords(f))
mp = {}
mf = HERE / f"{f}.mapped.md"
if mf.exists():
    for l in mf.read_text(encoding="utf-8").splitlines():
        b, _, r = l.partition("] ")
        mp[b[1:]] = r
mx = 9999
short = "--short" in args
if "--max" in args:
    mx = int(args[args.index("--max") + 1])
if args and args[0] == "--kw":
    w = args[1]
    ids = [b for b, ks in kw.items() if any(lc(k) == lc(w) for k in ks)][:mx]
else:
    ids = [a for a in args if not a.startswith("--") and not a.isdigit()]


def ctx(t, w, n=160):
    i = t.find(w)
    return t[max(0, i - n): i + n] if i >= 0 else t[:2 * n]


for b in ids:
    print("####", b)
    if short and args[0] == "--kw":
        print("PA:", ctx(pa.get(b, ""), args[1][:6]))
        print("HI:", hi.get(b, "")[:600])
    else:
        print("PA:", pa.get(b))
        print("HI:", hi.get(b))
        print("KW:", ", ".join(kw.get(b, [])))
        if b in mp:
            print("MP:", mp[b])
