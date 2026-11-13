import sys
sys.path.insert(0, r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\review')
from review_r8_common import load
p, h, ids = load()
# usage: lines.py 35,374,... [maxchars]
mx = int(sys.argv[2]) if len(sys.argv) > 2 else 100000
for n in map(int, sys.argv[1].split(',')):
    print(f'--- {n} [{ids[n-1]}]')
    print('P:', p[n - 1][:mx])
    print('H:', h[n - 1][:mx])
