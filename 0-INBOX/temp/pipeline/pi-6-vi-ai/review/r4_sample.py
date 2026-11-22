import sys, re
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai\review")
from r4_common import pairs
terms = sys.argv[1].split(",")
k = int(sys.argv[2]) if len(sys.argv) > 2 else 2
files = sys.argv[3].split(",") if len(sys.argv) > 3 else None
seen = {t: 0 for t in terms}
for f, n, sid, p, v in pairs(files):
    for t in terms:
        if re.search(t, p, re.I) and seen[t] < k:
            seen[t] += 1
            print(f"[{t}] {f}:{n} {sid}\n  P: {p.strip()}\n  V: {v.strip()}")
