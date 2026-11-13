import sys, re
sys.path.insert(0, r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\review')
from review_r7_common import *

praw, pl = load(P)
hraw, hl = load(H)
withE = '-e' in sys.argv
if withE:
    eraw, el = load(E)
for a in sys.argv[1:]:
    if a == '-e':
        continue
    if '-' in a:
        x, y = map(int, a.split('-'))
        rng = range(x, y + 1)
    else:
        rng = [int(a)]
    for n in rng:
        print(f'[{n}] P:', pl[n-1][2])
        print(f'[{n}] H:', hl[n-1][2])
        if withE:
            print(f'[{n}] E:', el[n-1][2])
        print()
