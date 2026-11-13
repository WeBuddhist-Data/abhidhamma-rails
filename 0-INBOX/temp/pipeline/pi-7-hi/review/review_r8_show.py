import re, sys
sys.path.insert(0, r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\review')
from review_r8_common import load
p, h, ids = load()
# usage: show.py a-b [maxchars]  (1-based non-empty line numbers)
a, b = map(int, sys.argv[1].split('-'))
mx = int(sys.argv[2]) if len(sys.argv) > 2 else 100000
for i in range(a - 1, b):
    print(f'P{i+1}: {p[i][:mx]}')
    print(f'H{i+1}: {h[i][:mx]}')
