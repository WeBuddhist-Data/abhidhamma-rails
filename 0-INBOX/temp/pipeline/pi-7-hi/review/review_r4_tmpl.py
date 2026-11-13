import re, sys, os, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from review_r4_struct_lib import *
from review_r4_items import ITEMS, L

def norm_p(s, pats):
    s = re.sub(r'\s*\^\S+\s*$', '', s)
    for pat, code in pats:
        s = re.sub(L + pat + r'[a-zāīūṃṅñṭḍṇḷ]*', '<X>', s, flags=re.I)
    s = re.sub(r'\(\d+\)', '(n)', s)
    return s

def norm_h(s, pats):
    s = re.sub(r'\s*\^\S+\s*$', '', s)
    for pat, code in pats:
        s = re.sub(pat, '<X>', s)
    s = re.sub(r'\(\d+\)', '(n)', s)
    return s

seen = {}
out = []
incons = []
only = sys.argv[1] if len(sys.argv) > 1 else ''
for f in FILES:
    pp, hp = ITEMS[f[:4]]
    P = nonempty(load(os.path.join(PA, f)))
    H = nonempty(load(os.path.join(HI, f)))
    for n, ((_, p), (_, h)) in enumerate(zip(P, H), 1):
        if p.startswith('#'):
            continue
        kp = norm_p(p, pp); kh = norm_h(h, hp)
        if kp in seen:
            if seen[kp][0] != kh:
                incons.append((f[:4], n, seen[kp][1]))
            continue
        seen[kp] = (kh, '%s:%d' % (f[:4], n))
        if not only or f.startswith(only):
            out.append('%s:%d' % (f[:4], n))
print('unique', len(seen))
print('inconsistent same-template', len(incons))
for x in incons:
    print('  INC', x)
print('UNIQUE_LINES', ' '.join(out))
