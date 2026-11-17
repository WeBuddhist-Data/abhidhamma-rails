import sys, re
from collections import defaultdict
sys.path.insert(0, r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-ru\review')
from r1_align import load

ch = sys.argv[1]
p, r, pt, rt = load(ch)
m = defaultdict(lambda: defaultdict(list))
mism = []


def norm_p(s):
    s = re.sub(r'\^[\w-]+\s*$', '', s)
    s = re.sub(r'…pe…\.?', ' ', s)
    s = re.sub(r'[.,;]', ' ', s)
    return ' '.join(s.split())


def norm_r(s):
    s = re.sub(r'\^[\w-]+\s*$', '', s)
    s = s.replace('…', ' ')
    s = re.sub(r'[.;]', ' ', s)
    s = s.strip(' ,')
    return ' '.join(s.split()).strip(' ,')


for (pid, pl), (rid, rl) in zip(p, r):
    for a, b in zip(pl, rl):
        if '–' not in a:
            continue
        pa = a.split('–', 1)[1]
        rb = b.split('–', 1)[1] if '–' in b else ''
        pa = re.split(r'Evaṃ ', pa)[0]
        rb = re.split(r'Такова ', rb)[0]
        pi = [norm_p(x) for x in re.split(r'\batthi\b', pa, flags=re.I) if norm_p(x)]
        ri = [norm_r(x) for x in re.split(r'\b[Бб]ывает\b', rb) if norm_r(x)]
        if 'atthi' not in pa:
            continue
        if len(pi) != len(ri):
            mism.append((pid, len(pi), len(ri), a[:80]))
            continue
        for x, y in zip(pi, ri):
            m[x][y].append(pid)

for x, d in sorted(m.items()):
    if len(d) > 1:
        print('INCONSIST', x)
        for y, ids in d.items():
            print('    ', y, ids[:6], len(ids))
for t in mism:
    print('COUNTMISMATCH', t)
if len(sys.argv) > 2:
    for x, d in sorted(m.items()):
        for y in d:
            print(x, '=>', y)

