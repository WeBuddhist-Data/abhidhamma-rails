import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from r4_lib import *
from collections import Counter

# compare number multisets: ours (Vietnamese number words) vs Tinh Su (digits + words); in-memory only
W = {'một': 1, 'hai': 2, 'ba': 3, 'bốn': 4, 'năm': 5, 'sáu': 6, 'bảy': 7, 'tám': 8, 'chín': 9, 'mười': 10,
     'mười một': 11, 'mười hai': 12, 'mười tám': 18, 'tứ': 4, 'tam': 3, 'nhị': 2, 'ngũ': 5, 'lục': 6, 'thập': 10}


def nums_vi(s, ts=False):
    s = re.sub(r'\[.*?\]', '', s).lower()
    s = re.sub(r'\s\^\S+$', '', s)
    out = [int(x) for x in re.findall(r'\b\d+\b', s) if not ts or int(x) < 100]
    for k in sorted(W, key=len, reverse=True):
        if not ts and k in ('tứ', 'tam', 'nhị', 'ngũ', 'lục', 'thập'):
            continue
        pat = r'(?<!\w)' + k + r'(?!\w)'
        # skip ordinals "thứ hai", and "năm" as year? none here; skip 'chia bốn/năm' method names
        for m in re.finditer(pat, s):
            pre = s[max(0, m.start() - 6):m.start()]
            if 'thứ ' in pre or 'chia ' in pre:
                continue
            if k == 'một' and re.match(r'\s*(loại thức nào|cách)', s[m.end():]):
                continue
            out.append(W[k])
        s = re.sub(pat, ' ', s)
    return Counter(out)


f = sys.argv[1]
ts = ts_dict()
V = segs(os.path.join(VI, f))
for sid, vl in V:
    if not sid or sid not in ts:
        continue
    a = nums_vi(' '.join(vl))
    b = nums_vi(ts[sid], ts=True)
    if a != b:
        print(sid, 'ours', dict(a), '| TS', dict(b))
