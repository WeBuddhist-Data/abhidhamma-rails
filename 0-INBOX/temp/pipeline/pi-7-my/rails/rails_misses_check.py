"""(copy of pi-6-my/rails/rails_misses_check.py, unchanged) Every adherence miss left in the rails must be a known INFLECTION / ARTEFACT / CONTEXT row of adherence-classified.tsv
(same id and keyword); no GENUINE or unknown miss may remain.
usage: rails_misses_check.py <adherence-rails.txt> <adherence-classified.tsv>"""
import collections
import sys
import unicodedata

adh, tsv = sys.argv[1:3]
N = lambda s: unicodedata.normalize("NFC", s)
cls = {}
for l in open(tsv, encoding="utf-8"):
    f = N(l).rstrip("\n").split("\t")
    if f[0] != "id":
        cls[(f[0], f[1])] = f[4]
c, bad, left = collections.Counter(), [], set()
for l in open(adh, encoding="utf-8"):
    f = N(l).strip().split("\t")
    if len(f) != 3 or not f[0][:1].isdigit():
        continue
    key = (f[0], f[1])
    left.add(key)
    k = cls.get(key, "UNKNOWN")
    c[k] += 1
    if k not in ("INFLECTION", "ARTEFACT", "CONTEXT"):
        bad.append(f"{k} {key[0]} {key[1]}")
fixed = sum(1 for k, v in cls.items() if v == "GENUINE" and k not in left)
gone = sum(1 for k, v in cls.items() if v != "GENUINE" and k not in left)
print("misses left: " + ", ".join(f"{k} {v}" for k, v in sorted(c.items()))
      + f"; GENUINE fixed {fixed}; INFLECTION/ARTEFACT/CONTEXT rows no longer listed {gone}; GENUINE or unknown left {len(bad)}")
print("\n".join(bad))
sys.exit(1 if bad else 0)
