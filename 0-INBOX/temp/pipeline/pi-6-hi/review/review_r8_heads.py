import sys, re
sys.path.insert(0, r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-hi\review')
from review_r8_check import load, FILES
for f in FILES:
    P, H = load(f)
    for i,(p,h) in enumerate(zip(P,H)):
        if p.startswith('#') or 'iṭṭhit' in p or (len(p) < 60 and not p.startswith('(') and not p.lower().startswith('yassa') and not p.lower().startswith('yattha')):
            print(f, i+1, '|', p, '|', h)
