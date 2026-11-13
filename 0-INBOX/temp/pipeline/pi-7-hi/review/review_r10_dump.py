import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from review_r10_align import pairs
# usage: review_r10_dump.py <fileprefix> [start] [end]
pref = sys.argv[1]
s = int(sys.argv[2]) if len(sys.argv) > 2 else 1
e = int(sys.argv[3]) if len(sys.argv) > 3 else 10**9
out = os.path.join(os.path.dirname(__file__), 'review_r10_dump_out.txt')
with open(out, 'w', encoding='utf-8') as o:
    for f, pl, hl in pairs():
        if not f.startswith(pref):
            continue
        for i, (a, b) in enumerate(zip(pl, hl), 1):
            if s <= i <= e:
                o.write(f'{i} P: {a}\n{i} H: {b}\n')
print(out)
