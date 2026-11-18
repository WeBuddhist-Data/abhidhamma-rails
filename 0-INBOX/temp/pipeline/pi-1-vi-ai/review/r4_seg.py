import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from r4_lib import *
# usage: r4_seg.py [ts] [ru] [en] id1 id2 ...
flags = [a for a in sys.argv[1:] if a in ('ts', 'ru', 'nopi')]
ids = [a for a in sys.argv[1:] if a not in flags]
P, V, R = {}, {}, {}
for f in FILES + ['1-matika.md']:
    P.update(seg_dict(os.path.join(PI, f)))
    V.update(seg_dict(os.path.join(VI, f)))
    if 'ru' in flags:
        R.update(seg_dict(os.path.join(RU, f)))
ts = ts_dict() if 'ts' in flags else {}
for i in ids:
    print('==', i)
    if 'nopi' not in flags:
        for l in P.get(i, ['<none>']): print('P:', strip_id(l))
    for l in V.get(i, ['<none>']): print('V:', strip_id(l))
    if 'ts' in flags: print('T:', strip_id(ts.get(i, '<none>')))
    if 'ru' in flags:
        for l in R.get(i, ['<none>']): print('R:', strip_id(l))
