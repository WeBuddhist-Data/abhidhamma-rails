import re, sys, os
ROOT = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation'
P = os.path.join(ROOT, 'pali', 'pi-6_split_chapters')
V = os.path.join(ROOT, 'vietnamese', 'pi-6-vietnamese-plain-rails_split_chapters')
FILES = ['3-06-ayatanayamaka.md', '4-dhatuyamaka.md', '5-01-saccayamaka.md', '5-02-saccayamaka.md',
         '5-03-saccayamaka.md', '6-01-sankharayamaka.md', '6-02-sankharayamaka.md', '7-01-anusayayamaka.md']

def lines(path):
    with open(path, encoding='utf-8') as f:
        return [l.rstrip('\n') for l in f if l.strip()]

# usage: r2_ids.py <viet-regex|-> [pali-regex|-] [print]
vre = None if sys.argv[1] == '-' else re.compile(sys.argv[1])
pre = None if len(sys.argv) < 3 or sys.argv[2] == '-' else re.compile(sys.argv[2])
pr = len(sys.argv) > 3
for fn in FILES:
    pl = lines(os.path.join(P, fn)); vl = lines(os.path.join(V, fn))
    # assign each line the id of the segment it ends in
    segid = [None] * len(pl)
    pend = []
    for i, l in enumerate(pl):
        pend.append(i)
        m = re.search(r'\^([\d-]+)\s*$', l)
        if m:
            for j in pend:
                segid[j] = m.group(1)
            pend = []
    hits = []
    for i, (a, b) in enumerate(zip(pl, vl)):
        if (vre is None or vre.search(b)) and (pre is None or pre.search(a)):
            hits.append(segid[i])
            if pr:
                print('--', fn, segid[i], 'L%d' % i); print('  P:', a); print('  V:', b)
    if hits:
        u = []
        for h in hits:
            if h not in u:
                u.append(h)
        print(fn, len(hits), ' '.join(str(x) for x in u))
