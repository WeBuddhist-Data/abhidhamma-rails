import os, sys, re, collections
sys.path.insert(0, os.path.dirname(__file__))
from review_r10_align import pairs
from review_r10_check import pneg, ptoks, strip_id
from review_r10_neg import psplit, hsplit

INNER = [r"(?<![a-zāīūṃ])(?:na|no)*anupādinn(?!upādān|aanupādān)", r"(?<![a-zāīūṃ])(?:na|no)*acetasik", r"(?<![a-zāīūṃ])(?:na|no)*asaṃkiliṭṭh", r"(?<![a-zāīūṃ])(?:na|no)*sauttar"]
def pneg2(s):
    n = pneg(s)
    low = s.lower()
    for r in INNER:
        n += len(re.findall(r, low))
    # 'na uppajjati' verb negation
    n -= len(re.findall(r"\bna uppajj", low))
    return n
def hneg2(s):
    n = len(re.findall(r"(?<!\S)न होने वाल", s))
    n += len(re.findall(r"न छोड़ी जाने वाल|न छोड़े जाने वाल|न जानी जा सकने वाल|मूलों से रहित", s))
    return n
rows = []
for f, pl, hl in pairs():
    for i, (a, b) in enumerate(zip(pl, hl), 1):
        a0, b0 = strip_id(a), strip_id(b)
        if pneg2(a0) == hneg2(b0):
            continue
        ps, hs = psplit(a0), hsplit(b0)
        if len(ps) != len(hs):
            rows.append((f[:4], i, pneg2(a0), hneg2(b0), a0, b0)); continue
        for x, y in zip(ps, hs):
            if pneg2(x) != hneg2(y):
                rows.append((f[:4], i, pneg2(x), hneg2(y), x.strip(), y.strip()))
out = os.path.join(os.path.dirname(__file__), 'review_r10_neg3_out.txt')
with open(out, 'w', encoding='utf-8') as o:
    for f, i, p, h, x, y in rows:
        o.write(f'[{f}:{i}] {p}/{h}\n  P: {x[:900]}\n  H: {y[:1200]}\n')
print(out, len(rows))
