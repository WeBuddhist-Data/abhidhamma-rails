"""Debug helper for build_rails_2-04_2-08.py: translate given Pāli lines of a file (by block id) and print them.
usage: python -I -B -X utf8 debug_2-04_2-08.py <file prefix> <block id> [--norm]"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
B = __import__("build_rails_2-04_2-08")

B.build_res()
pref, bid = sys.argv[1], sys.argv[2]
name = [f for f in B.FILES if f.startswith(pref)][0]
T = B.Triad(name)
lines = open(os.path.join(B.PALI_DIR, name), encoding="utf-8").read().split("\n")
seg = []
for ln in lines:
    if not ln.strip():
        seg = []
        continue
    seg.append(ln)
    m = B.ID_RE.search(ln)
    if m and m.group(1) == bid:
        for s in seg:
            mm = B.ID_RE.search(s)
            body = s[: mm.start()] if mm else s.rstrip()
            if "--norm" in sys.argv:
                print("N:", T.normalize(B.S.lower_initials(body)))
            print("H:", B.translate_line(body, T))
        break
