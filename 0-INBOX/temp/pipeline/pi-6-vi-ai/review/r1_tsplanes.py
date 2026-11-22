import sys, re
from collections import Counter
sys.path.insert(0, 'D:/Work/OpenPecha/abhidhamma-rails/0-INBOX/temp/pipeline/pi-6-vi-ai/review')
from r1_check import load, PDIR, FILES
from r1_ts import load_ts

# console-only: compare per-segment counts of plane / person words, Pali vs reference
PAIRS = [
    ('suddhāvās', r'tịnh cư'),
    ('asaññasatt', r'vô tư ?ởng'),
    ('arūp(?!ak)', r'vô sắc'),
    ('pañcavokār', r'ngũ u ?ẩn'),
    ('catuvokār', r'tứ u ?ẩn'),
    ('kāmāvacar', r'dục giới'),
    ('(?<!a)rūpāvacar', r'sắc giới'),
    ('pacchimabhavik', r'kiếp chót|kiếp cuối'),
    ('sacakkhuk', r'hữu nhãn'),
    ('acakkhuk', r'vô nhãn'),
    ('sacittak', r'hữu tâm'),
    ('acittak', r'vô tâm'),
]
files = sys.argv[1:] or FILES
T = load_ts()
n = 0
for f in files:
    P, _ = load(PDIR + f)
    for sid, pl in P.items():
        if sid not in T or pl[0].startswith('#'):
            continue
        pt = ' '.join(pl).lower()
        tt = ' '.join(T[sid]).lower()
        d = []
        for pr, tr in PAIRS:
            a = len(re.findall(pr, pt))
            b = len(re.findall(tr, tt))
            if a != b:
                d.append('%s %d/%d' % (pr[:10], a, b))
        if d:
            n += 1
            print(f[:4], sid, '; '.join(d))
print('segments with differences:', n)
