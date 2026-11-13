import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from review_r5_common import *

for fn in FILES:
    P, H = pairs(fn)
    print("=====", fn, len(P), len(H))
    # blank-line structure
    for i, (a, b) in enumerate(zip(P, H), 1):
        if (a.strip() == "") != (b.strip() == ""):
            print("BLANK MISMATCH line", i)
    # double blank lines in Hindi
    for i in range(1, len(H)):
        if H[i].strip() == "" and H[i-1].strip() == "" and i < len(H)-1:
            print("DOUBLE BLANK at", i+1)
    ps = segments(P); hs = segments(H)
    print("segments", len(ps), len(hs))
    for (pid, pl), (hid, hl) in zip(ps, hs):
        if pid != hid or len(pl) != len(hl):
            print("SEG MISMATCH", pid, hid, len(pl), len(hl))
    # headings
    if "-h" in sys.argv:
        for i, (a, b) in enumerate(zip(P, H), 1):
            if a.startswith("#"):
                print(i, a, " || ", b)
