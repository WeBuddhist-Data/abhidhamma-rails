import re, sys
sys.path.insert(0, r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\review')
from review_r8_common import load
p, h, ids = load()
n = 0
for i, a in enumerate(p):
    if a.startswith('#') and re.search(r'dukaṃ \^', a) and not a.startswith('#######'):
        print('=' * 20, i + 1, a)
        k = 0
        j = i + 1
        while j < len(p) and k < 3:
            if not p[j].startswith('#'):
                print('P', j + 1, p[j].split(' – ')[0][:200])
                print('H', j + 1, h[j].split(' – ')[0][:300])
                k += 1
            j += 1
