import sys
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai\review")
from r4_common import pairs, IDRE
# headings + id mismatch check + editorial notes
for f, n, sid, p, v in pairs():
    mp = IDRE.search(p); mv = IDRE.search(v)
    if (mp and not mv) or (mv and not mp) or (mp and mv and mp.group(1) != mv.group(1)):
        print("IDMISMATCH", f, n, mp and mp.group(1), mv and mv.group(1))
    if p.startswith("#") or "[" in p or "[" in v:
        print(f"{f}:{n} | {p.strip()} || {v.strip()}")
