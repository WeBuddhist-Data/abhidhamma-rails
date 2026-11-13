import re, sys, collections
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-hi\review")
from review_r3_pairs import load
from review_r3_struct import FILES

pat = sys.argv[1]
n = int(sys.argv[2]) if len(sys.argv) > 2 else 2
c = collections.Counter()
for fn in FILES:
    p, h = load(fn)
    for l in h:
        for m in re.finditer(pat + r"((?:\s*\S+){%d})" % n, l):
            c[m.group(0)] += 1
for w, k in c.most_common():
    print(k, w)
