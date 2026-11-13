import os, sys, re, collections
sys.path.insert(0, os.path.dirname(__file__))
from review_r10_align import pairs
from review_r10_check import pneg, hneg, ptoks, strip_id, PCOND
from review_r10_neg import psplit, hsplit

def stem(t):
    t = re.sub(r"(ñceva|ñca|ṃ|ssa|o|ā|a|ū|u|ī|i|e)$", "", t)
    return t
groups = collections.defaultdict(list)
for f, pl, hl in pairs():
    for i, (a, b) in enumerate(zip(pl, hl), 1):
        a0, b0 = strip_id(a), strip_id(b)
        ps, hs = psplit(a0), hsplit(b0)
        if len(ps) != len(hs):
            continue
        for x, y in zip(ps, hs):
            d = pneg(x) - hneg(y)
            if d == 0:
                continue
            toks = [t for t in ptoks(x) if (t.startswith(('na', 'no', 'a', 'sa')) and not PCOND.fullmatch(t)
                    and t not in ('nava', 'abyākataṃ', 'abyākato', 'abyākatassa', 'akusalaṃ', 'akusalo', 'akusalassa', 'abyākatañca', 'akusalañca', 'ārammaṇapaccayena'))]
            key = (tuple(sorted(set(stem(t) for t in toks))), d)
            groups[key].append((f[:4], i, x.strip(), y.strip()))
out = os.path.join(os.path.dirname(__file__), 'review_r10_neg2_out.txt')
with open(out, 'w', encoding='utf-8') as o:
    for key, v in sorted(groups.items(), key=lambda kv: -len(kv[1])):
        o.write(f'## {len(v)} delta={key[1]} {key[0]}\n   ids: ' + ' '.join(f'{a}:{b}' for a, b, _, _ in v[:40]) + '\n')
        f, i, x, y = v[0]
        o.write(f'   P: {x[:700]}\n   H: {y[:900]}\n')
print(out, len(groups))
