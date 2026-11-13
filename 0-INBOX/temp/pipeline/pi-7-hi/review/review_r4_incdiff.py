import re, sys, os, difflib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from review_r4_struct_lib import *
from review_r4_items import ITEMS
from review_r4_tmpl import norm_p, norm_h

data = {}
for f in FILES:
    pp, hp = ITEMS[f[:4]]
    P = nonempty(load(os.path.join(PA, f)))
    H = nonempty(load(os.path.join(HI, f)))
    for n, ((_, p), (_, h)) in enumerate(zip(P, H), 1):
        data['%s:%d' % (f[:4], n)] = (norm_p(p, pp), norm_h(h, hp))
pairs = [x.split('/') for x in sys.argv[1:]]
for a, b in pairs:
    ha = data[a][1].split(); hb = data[b][1].split()
    print('==', a, 'vs', b, '| P:', data[a][0][:120])
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, ha, hb).get_opcodes():
        if op != 'equal':
            print('   ', op, ' '.join(ha[i1:i2]), ' ==> ', ' '.join(hb[j1:j2]))
