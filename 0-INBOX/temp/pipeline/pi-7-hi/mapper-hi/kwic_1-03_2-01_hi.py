"""KWIC: for each keyword, the first N segments that list it, with the aligned Pāli / Hindi sentence(s).
usage: kwic_1-03_2-01_hi.py <file> <N> kw [kw …]
"""
import sys, pathlib, re
sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import read_keywords, read_hindi, read_pali

f, n = sys.argv[1], int(sys.argv[2])
hi, pa = read_hindi(f), read_pali(f)
kwl = read_keywords(f)


def sents(t, hindi):
    t = t.replace("\n", " ")
    pat = r"(?<=[।?])\s+|(?<=\(\d\))\s+|(?<=\(\d\d\))\s+" if hindi else r"(?<=[.?])\s+(?=[A-ZĀĪŪṆṬḌ(])|(?<=\(\d\))\s+|(?<=\(\d\d\))\s+"
    return [s for s in re.split(pat, t) if s.strip()]


for kw in sys.argv[3:]:
    c = 0
    print("#####", kw)
    for bid, kws in kwl:
        if kw not in kws:
            continue
        c += 1
        if c > n:
            break
        p, h = pa.get(bid, ""), hi.get(bid, "")
        ps, hs = sents(p, False), sents(h, True)
        base = re.sub(r"(ti|ñca|pi)$", "", kw)
        if len(ps) == len(hs):
            idx = [i for i, s in enumerate(ps) if base in s or base.lower() in s.lower()]
            for i in idx[:2]:
                print(f"[{bid}] P: {ps[i][:400]}")
                print(f"[{bid}] H: {hs[i][:400]}")
        else:
            print(f"[{bid}] (unaligned {len(ps)}/{len(hs)}) P: {p[:300]}")
            print(f"[{bid}] H: {h[:500]}")
