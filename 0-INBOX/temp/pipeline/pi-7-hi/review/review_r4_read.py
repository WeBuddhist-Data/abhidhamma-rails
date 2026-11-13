import re, sys, os, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from review_r4_struct_lib import *
from review_r4_items import ITEMS
from review_r4_tmpl import norm_p

# print unique-template, non-count, non-trivial lines of one file
pref = sys.argv[1]
lo = int(sys.argv[2]) if len(sys.argv) > 2 else 1
hi = int(sys.argv[3]) if len(sys.argv) > 3 else 10 ** 6
seen = set()
for f in FILES:
    pp, hp = ITEMS[f[:4]]
    P = nonempty(load(os.path.join(PA, f)))
    H = nonempty(load(os.path.join(HI, f)))
    for n, ((_, p), (_, h)) in enumerate(zip(P, H), 1):
        if p.startswith('#'):
            continue
        k = norm_p(p, pp)
        first = k not in seen
        seen.add(k)
        if not f.startswith(pref) or not first or n < lo or n > hi:
            continue
        if re.match(r'^(Na|No)?[Hh]etu(yā|paccayā)? ', p) and ('gaṇetabb' in p or re.search(r'(ārammaṇe|naārammaṇe|adhipatiyā) \w+', p)):
            continue
        if re.search(r'paccayena paccayo(… \w+paccayena paccayo)+\. \(\d\)', p) and ' – ' not in p:
            continue
        if len(p) < 70:
            continue
        # strip the trailing ID for brevity
        print('[%d] P: %s' % (n, re.sub(r'\s*\^\S+$', '', p)))
        print('[%d] H: %s' % (n, re.sub(r'\s*\^\S+$', '', h)))
        print()
