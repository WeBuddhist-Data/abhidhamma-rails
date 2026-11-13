import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from review_r4_struct_lib import *

# args: prefix:n (nonempty line) or prefix:pN (physical line)
for arg in sys.argv[1:]:
    pref, n = arg.split(':')
    f = [x for x in FILES if x.startswith(pref)][0]
    P = nonempty(load(os.path.join(PA, f)))
    if n.startswith('p'):
        phys = int(n[1:])
        idx = [i for i, (pl, _) in enumerate(P) if pl == phys][0]
    else:
        idx = int(n) - 1
    sid = None
    for j in range(idx, len(P)):
        m = re.search(r'\^(\S+)\s*$', P[j][1])
        if m:
            sid = m.group(1); break
    print(arg, '-> nonempty', idx + 1, 'ID', sid)
