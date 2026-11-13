import re, sys, collections
sys.path.insert(0, r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-hi\review')
from review_r8_check import load, FILES, HITEM
from review_r8_order import sents

ITEMP = r'(?<![\w])(cakkhu|sot|ghān|man|itth|puris|jīvit|somanass|domanass|upekkh|saddh|paññ|anaññātaññassāmīt|aññātāv|aññ)(?:indriy|ndriy|andriy)'
seen = collections.OrderedDict()
for f in FILES:
    P, H = load(f)
    for i, (p, h) in enumerate(zip(P, H)):
        if p.startswith('#') or p.startswith('(') or re.match(r'(?i)y(assa|attha|o) ', p):
            continue
        sp, sh = sents(p, 0), sents(h, 1)
        if len(sp) != len(sh):
            continue
        for a, b in zip(sp, sh):
            m1 = re.search(ITEMP, a, re.I)
            m2 = re.search(HITEM, b)
            ca = a[:m1.start()] if m1 else a
            cb = b[:m2.start()] if m2 else b
            ca = re.sub(r'\b(tesaṃ|tāsaṃ|tattha)\b', '', ca).strip()
            cb = re.sub(r'(वहाँ)', '', cb).strip()
            key = (ca, cb)
            if key not in seen:
                seen[key] = '%s L%d' % (f, i + 1)
for (a, b), loc in seen.items():
    print(loc, '|', a, '\n        |', b)
print(len(seen))
