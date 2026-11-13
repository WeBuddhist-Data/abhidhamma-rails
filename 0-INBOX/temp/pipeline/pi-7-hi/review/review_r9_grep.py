import os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
from review_r9_common import *
# usage: review_r9_grep.py <regex-on-pali> [maxn] [--h regex on hindi]
pat = re.compile(sys.argv[1])
maxn = int(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2].isdigit() else 10
hpat = None
if '--h' in sys.argv:
    hpat = re.compile(sys.argv[sys.argv.index('--h') + 1])
n = 0
for f, sid, ne, p, h, pid, hid in pairs():
    if pat.search(p) and (hpat is None or hpat.search(h)):
        n += 1
        if n <= maxn:
            print('==', f, ne, sid)
            print('P:', p)
            print('H:', h)
print('total', n)
