import re, sys, collections
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-hi\review")
from review_r3_pairs import load
from review_r3_struct import FILES

c = collections.Counter()
for fn in FILES:
    p, h = load(fn)
    for l in p:
        l = re.sub(r"\^[0-9-]+", "", l)
        for w in re.findall(r"[A-Za-zāīūṃṅñṭḍṇḷĀĪŪṬḌṆṄÑṂ]+", l):
            c[w.lower()] += 1
for w, n in sorted(c.items()):
    print(w, n, end="; ")
