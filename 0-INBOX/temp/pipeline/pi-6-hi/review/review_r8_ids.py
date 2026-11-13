import sys, re
sys.path.insert(0, r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-hi\review')
from review_r8_check import load
def idof(f, ln):
    P, H = load(f)
    for j in range(ln-1, len(P)):
        m = re.search(r'\^([\w-]+)\s*$', P[j])
        if m: return m.group(1)
for f, ln in [('10-08',218),('10-08',264),('10-12',73),('10-12',76),('10-12',82),('10-12',184),('10-12',188),('10-12',196),('10-12',322),('10-13',162),('10-13',163),('10-13',145),('10-13',369),('10-13',266),('10-13',336),('10-10',124),('10-11',89),('10-13',384)]:
    print(f, ln, idof(f, ln))
