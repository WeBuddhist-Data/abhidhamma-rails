"""For each keyword: the first N segments where it occurs, Pāli and Hindi first sentence (compact).
usage: python -I -B -X utf8 kwctx_4-15_5-04_hi.py <file> [-n N] kw [kw …]
"""
import sys, pathlib, re
sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from map_sample_hi import read_keywords, read_hindi, read_pali

args = sys.argv[1:]
f = args.pop(0)
n = 1
if args and args[0] == "-n":
    n = int(args[1]); args = args[2:]
pa, hi = read_pali(f), read_hindi(f)
kws = read_keywords(f)


def first(t, kw=None):
    if t is None:
        return None
    sents = re.split(r"(?<=[.।?])\s+", t)
    if kw:
        for s in sents:
            if kw.lower() in s.lower():
                return s[:400]
    return sents[0][:400]


for kw in args:
    c = 0
    for bid, ks in kws:
        if kw in ks:
            p = first(pa.get(bid), kw)
            # Hindi sentence with the same index as the Pāli sentence
            ps = re.split(r"(?<=[.।?])\s+", pa.get(bid) or "")
            hs = re.split(r"(?<=[.।?])\s+", hi.get(bid) or "")
            idx = next((i for i, s in enumerate(ps) if kw.lower() in s.lower()), 0)
            h = hs[idx][:400] if idx < len(hs) else (hs[0][:400] if hs else None)
            print(f"[{kw}] {bid}\n  PA: {p}\n  HI: {h}")
            c += 1
            if c >= n:
                break
