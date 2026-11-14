import re, os
from collections import Counter
base = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation'
R = os.path.join(base, 'russian', 'pi-1-russian-plain-rails_split_chapters')
files = ['4-01-nikkhepakandam.md', '4-02-nikkhepakandam.md', '4-03-nikkhepakandam.md', '5-atthakathakandam.md']
c = Counter()
for fn in files:
    with open(os.path.join(R, fn), encoding='utf-8') as f:
        for l in f:
            if not l.strip():
                continue
            m = re.search(r'\^([\w-]+)\s*$', l); i = m.group(1) if m else '?'
            for mm in re.finditer(r'(.{0,45}),\s–\sэто', l):
                c[mm.group(1)[-30:]] += 1
for k, v in c.most_common():
    print(v, '|', k)
