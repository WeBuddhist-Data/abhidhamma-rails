import sys, re, collections
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai\review")
from r4_common import pairs
c = collections.Counter()
for f, n, sid, p, v in pairs():
    for w in re.findall(r"[a-zāīūṃṅñṭḍṇḷ]+", p.lower()):
        if w.startswith(("a", "n")):
            c[w] += 1
for w, k in sorted(c.items()):
    print(k, w)
