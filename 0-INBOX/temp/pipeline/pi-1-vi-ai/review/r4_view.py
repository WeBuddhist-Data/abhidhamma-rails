import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from r4_lib import *

# usage: r4_view.py <file> <start_index> <end_index> [ts] [ru]
f = sys.argv[1]
a, b = int(sys.argv[2]), int(sys.argv[3])
flags = sys.argv[4:]
P = segs(os.path.join(PI, f))
V = segs(os.path.join(VI, f))
ts = ts_dict() if 'ts' in flags else {}
ru = seg_dict(os.path.join(RU, f)) if 'ru' in flags else {}
for i in range(a, min(b, len(P))):
    sid, pl = P[i]
    vl = V[i][1]
    print(f'=== [{i}] {sid}')
    if 'nopi' not in flags:
        for l in pl:
            print('P:', strip_id(l))
    for l in vl:
        print('V:', strip_id(l))
    if 'ts' in flags:
        print('T:', strip_id(ts.get(sid, '<none>')))
    if 'ru' in flags:
        for l in ru.get(sid, ['<none>']):
            print('R:', strip_id(l))
