"""Scan 4-01: for a keyword, the distinct Pāli contexts (prev word + kw + next word) in segments listing it.
usage: python -I -B -X utf8 scan_4-01_hi.py kw"""
import sys, pathlib, re, collections; sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import read_keywords, read_pali

F = "4-01-kilesagocchaka"
kw = sys.argv[1]
pa = read_pali(F)
c = collections.Counter()
ex = {}
for bid, kws in read_keywords(F):
    if kw in kws:
        for m in re.finditer(r"(\S+) " + re.escape(kw) + r"(?!\w)(\S*)", pa.get(bid, "")):
            k = (m.group(1), m.group(2))
            c[k] += 1
            ex.setdefault(k, bid)
for k, n in c.most_common():
    print(n, k, ex[k])
