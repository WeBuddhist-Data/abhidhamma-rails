import os, sys, re
sys.path.insert(0, os.path.dirname(__file__))
from review_r10_align import pairs
from review_r10_check import ptoks, strip_id, PCOND, PNUM
from review_r10_neg import psplit, hsplit

INNER = re.compile(r"^(?:na|no)*(anupādinn(?!upādān|aanupādān)|acetasik|asaṃkiliṭṭh|sauttar|cittavisaṃsaṭṭh)")
LEX = {'nava', 'natthi', 'natthiyā', 'nayena', 'nayo', 'nanu', 'nāma'}
def pseq(s):
    toks = ptoks(s)
    seq = []
    carry = 0
    for i, t in enumerate(toks):
        if t in ('na', 'no'):
            carry += 1; continue
        if t in ('nana', 'nano'):
            carry += 2; continue
        if t in LEX or t in PNUM or PCOND.fullmatch(t) or t in ('uppajjati', 'uppajjanti', 'labbhati', 'dissanti', 'vattabbaṃ', 'sadisaṃ'):
            carry = 0; continue
        if t.startswith('nabhāvanāy') and i > 0 and toks[i-1].endswith('nevadassanena'):
            continue
        n = carry; carry = 0
        u = t
        while (u.startswith('na') or u.startswith('no')) and len(u) > 4:
            n += 1; u = u[2:]
        if INNER.match(t):
            n += 1
        if n:
            seq.append(n)
    return seq
HRUN = re.compile(r"(?:मूलों से रहित|न छोड़ी जाने वाल\S*|न छोड़े जाने वाल\S*|न जानी जा सकने वाल\S*|(?<!\S)न होने वाल\S*)((?: न होने वाल\S*)*)")
def hseq(s):
    return [1 + m.group(1).count('न होने वाल') for m in HRUN.finditer(s)]

rows = []
for f, pl, hl in pairs():
    for i, (a, b) in enumerate(zip(pl, hl), 1):
        a0, b0 = strip_id(a), strip_id(b)
        if a.startswith('#'):
            continue
        ps, hs = psplit(a0), hsplit(b0)
        if len(ps) != len(hs):
            if pseq(a0) != hseq(b0):
                rows.append((f[:4], i, pseq(a0), hseq(b0), a0, b0))
            continue
        for x, y in zip(ps, hs):
            if pseq(x) != hseq(y):
                rows.append((f[:4], i, pseq(x), hseq(y), x.strip(), y.strip()))
out = os.path.join(os.path.dirname(__file__), 'review_r10_negseq_out.txt')
with open(out, 'w', encoding='utf-8') as o:
    for f, i, p, h, x, y in rows:
        o.write(f'[{f}:{i}] {p} / {h}\n  P: {x[:900]}\n  H: {y[:1200]}\n')
print(out, len(rows))
