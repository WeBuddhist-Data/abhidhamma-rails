import sys, re
from collections import Counter
sys.path.insert(0, r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-ru\review')
from r1_align import load
c1 = Counter(); c2 = Counter()
for ch in ['1-khandhavibhango.md', '2-ayatanavibhango.md', '3-dhatuvibhango.md']:
    p, r, pt, rt = load(ch)
    for m in re.finditer(r'(\S+ \S+),? – это', rt):
        s = m.group(0)
        key = ('C ' if ', –' in s else 'N ') + m.group(1)
        c1[key] += 1
for k, v in sorted(c1.items()):
    print(v, k)
