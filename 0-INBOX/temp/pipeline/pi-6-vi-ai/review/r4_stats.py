import sys, re, collections
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai\review")
from r4_common import pairs, IDRE
lines = 0
ids = set()
heads = 0
for f, n, sid, p, v in pairs():
    lines += 1
    m = IDRE.search(p)
    if m:
        ids.add(m.group(1))
        if p.startswith("#"):
            heads += 1
print("non-empty lines", lines, "ids", len(ids), "heading ids", heads, "content ids", len(ids) - heads)
