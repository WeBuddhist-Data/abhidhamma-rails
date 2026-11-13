import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from review_r4_struct_lib import *
# usage: review_r4_show.py <fileprefix> <n1,n2,...|a-b> [maxchars]
f = [x for x in FILES if x.startswith(sys.argv[1])][0]
P = nonempty(load(os.path.join(PA, f)))
H = nonempty(load(os.path.join(HI, f)))
sel = []
for part in sys.argv[2].split(','):
    if '-' in part:
        a, b = part.split('-'); sel += list(range(int(a), int(b) + 1))
    else:
        sel.append(int(part))
mx = int(sys.argv[3]) if len(sys.argv) > 3 else 100000
for n in sel:
    if 1 <= n <= len(P):
        print('[%d] P: %s' % (n, P[n - 1][1][:mx]))
        print('[%d] H: %s' % (n, H[n - 1][1][:mx]))
        print()
