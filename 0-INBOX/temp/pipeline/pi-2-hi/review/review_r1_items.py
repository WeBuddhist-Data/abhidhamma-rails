import re, sys
from collections import defaultdict
exec(open(r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-hi\review\review_r1_align.py', encoding='utf-8').read().split("mode = sys.argv")[0])

def pitems(l):
    l = idre.sub('', l)
    l = l.split('–', 1)[1] if '–' in l else l
    l = re.split(r'Evaṃ \w+ ', l)[0]
    parts = re.split(r'\b[Aa]tthi\b', l)[1:]
    return [re.sub(r'[\s,.;…pe]+$', '', p.replace('…pe…', '')).strip(' ,.;') for p in parts]

def hitems(l):
    l = idre.sub('', l)
    l = l.split('–', 1)[1] if '–' in l else l
    l = l.split('इस तरह')[0]
    parts = re.split(r'(?:^|(?<=[\s,;।…]))कुछ ', l)[1:]
    return [p.strip(' ,;।…') for p in parts]

mapping = defaultdict(lambda: defaultdict(list))
start = int(sys.argv[1]) if len(sys.argv) > 1 else 63
end = int(sys.argv[2]) if len(sys.argv) > 2 else 510
for i in range(start - 1, end):
    p, h = pl[i], hl[i]
    if 'atthi' not in p.lower(): continue
    a, b = pitems(p), hitems(h)
    if len(a) != len(b):
        print(f'COUNT {i+1} {pid(p)}: P{len(a)} H{len(b)}')
        continue
    for x, y in zip(a, b):
        y = re.sub(r'\s+(है|हैं)$', '', y)
        mapping[x][y].append(i + 1)
for k, v in mapping.items():
    if len(v) > 1:
        print('INCONS', k)
        for y, ls in v.items(): print('    ', y, ls[:8], len(ls))
if '-dump' in sys.argv:
    for k, v in mapping.items():
        print(k, '=>', ' || '.join(v.keys()))
