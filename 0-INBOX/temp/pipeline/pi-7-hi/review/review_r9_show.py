import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from review_r9_common import *
# usage: review_r9_show.py <fileprefix>:<ne>[-<ne2>] ...  [--en]
want = []
en = '--en' in sys.argv
for a in sys.argv[1:]:
    if a.startswith('--'):
        continue
    fp, rng = a.split(':')
    if '-' in rng:
        a1, a2 = rng.split('-')
    else:
        a1 = a2 = rng
    want.append((fp, int(a1), int(a2)))
for fp, a1, a2 in want:
    f = [x for x in FILES if x.startswith(fp)][0]
    P = lines_nonempty(load(os.path.join(PDIR, f)))
    H = lines_nonempty(load(os.path.join(HDIR, f)))
    E = lines_nonempty(load(os.path.join(EDIR, f))) if en else None
    for i in range(a1 - 1, a2):
        print('==', f, P[i][0])
        print('P:', P[i][2])
        print('H:', H[i][2])
        if en:
            print('E:', E[i][2])
