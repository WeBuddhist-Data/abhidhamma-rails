import re, sys, os, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from review_r4_struct_lib import *

m = collections.defaultdict(lambda: collections.defaultdict(list))
short = collections.defaultdict(lambda: collections.defaultdict(list))
for f in FILES:
    P = nonempty(load(os.path.join(PA, f)))
    H = nonempty(load(os.path.join(HI, f)))
    for n, ((_, p), (_, h)) in enumerate(zip(P, H), 1):
        pp = re.sub(r'\s*\^\S+\s*$', '', p).strip()
        hh = re.sub(r'\s*\^\S+\s*$', '', h).strip()
        if p.startswith('#'):
            k = re.sub(r'^#+\s*', '', pp)
            m[k][re.sub(r'^#+\s*', '', hh)].append('%s:%d' % (f[:4], n))
        elif len(pp) < 60 and not re.search(r'\d', pp):
            short[pp][hh].append('%s:%d' % (f[:4], n))
for k in sorted(m):
    for v, locs in m[k].items():
        print('H', k, '=>', v, '  ', ' '.join(locs[:4]), '(+%d)' % (len(locs) - 4) if len(locs) > 4 else '')
print()
for k in sorted(short):
    for v, locs in short[k].items():
        print('S', k, '=>', v, '  ', ' '.join(locs[:4]), '(+%d)' % (len(locs) - 4) if len(locs) > 4 else '')
