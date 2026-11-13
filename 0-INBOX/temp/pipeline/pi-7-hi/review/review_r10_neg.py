import os, sys, re, collections
sys.path.insert(0, os.path.dirname(__file__))
from review_r10_align import pairs, IDRE
from review_r10_check import pneg, hneg, ptoks, strip_id

def psplit(s):
    s = re.sub(r"\([^)]*\)", lambda m: m.group(0).replace('.', '§'), s)
    return [x for x in re.split(r"(?<=[.;])\s+|\s+–\s+|…pe…|…", s) if x.strip()]
def hsplit(s):
    s = re.sub(r"\([^)]*\)", lambda m: m.group(0).replace('।', '§'), s)
    return [x for x in re.split(r"(?<=[।;?])\s+|\s+–\s+|…", s) if x.strip()]

pat = collections.Counter()
rows = []
unaligned = []
for f, pl, hl in pairs():
    for i, (a, b) in enumerate(zip(pl, hl), 1):
        a0, b0 = strip_id(a), strip_id(b)
        if pneg(a0) == hneg(b0):
            continue
        ps, hs = psplit(a0), hsplit(b0)
        if len(ps) != len(hs):
            unaligned.append((f, i, pneg(a0), hneg(b0), len(ps), len(hs)))
            continue
        for x, y in zip(ps, hs):
            if pneg(x) != hneg(y):
                rows.append((f, i, pneg(x), hneg(y), x.strip(), y.strip()))
                # pattern: neg tokens
                key = ' '.join(t for t in ptoks(x) if t.startswith(('na', 'no')) and t not in ('nava',))
                pat[(pneg(x) - hneg(y))] += 1
out = os.path.join(os.path.dirname(__file__), 'review_r10_neg_out.txt')
with open(out, 'w', encoding='utf-8') as o:
    o.write(f'rows {len(rows)} unaligned {len(unaligned)} {pat}\n')
    for r in unaligned:
        o.write('UNALIGNED ' + repr(r) + '\n')
    for f, i, p, h, x, y in rows:
        o.write(f'[{f[:4]}:{i}] {p}/{h}\n  P: {x}\n  H: {y}\n')
print(out, len(rows), len(unaligned), pat)
