import os, sys, re
sys.path.insert(0, os.path.dirname(__file__))
from review_r10_align import pairs
# usage: review_r10_show.py "5-03:6,7 5-04:12" [maxlen]
spec = {}
for part in sys.argv[1].split():
    f, ls = part.split(':')
    spec.setdefault(f, set()).update(int(x) for x in ls.split(','))
mx = int(sys.argv[2]) if len(sys.argv) > 2 else 10**6
out = os.path.join(os.path.dirname(__file__), 'review_r10_show_out.txt')
with open(out, 'w', encoding='utf-8') as o:
    for f, pl, hl in pairs():
        for k, ls in spec.items():
            if f.startswith(k):
                for i in sorted(ls):
                    a, b = pl[i-1], hl[i-1]
                    o.write(f'[{f[:4]}:{i}] P: {a[:mx]}\n[{f[:4]}:{i}] H: {b[:mx]}\n')
                    if '  ' in b:
                        j = b.index('  '); o.write('   DOUBLESPACE at: ' + repr(b[max(0,j-40):j+20]) + '\n')
print(out)
