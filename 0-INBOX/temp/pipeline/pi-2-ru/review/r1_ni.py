import sys, re
from collections import Counter
sys.path.insert(0, r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-ru\review')
from r1_align import load
c = Counter()
for ch in ['1-khandhavibhango.md', '2-ayatanavibhango.md', '3-dhatuvibhango.md']:
    p, r, pt, rt = load(ch)
    for m in re.finditer(r'(\S+\s+\S+\s+)?\bни\b[^,;.]*,\s*ни\b[^,;.]*', rt):
        s = m.group(0)
        if re.search(r'\b(не|нельзя|нет)\b', s):
            continue
        c[s.strip()] += 1
for k, v in c.most_common():
    print(v, k)
