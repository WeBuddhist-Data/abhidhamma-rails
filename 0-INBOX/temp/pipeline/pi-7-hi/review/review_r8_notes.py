import re, sys
sys.path.insert(0, r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\review')
from review_r8_common import load
p, h, ids = load()
seen = set()
skip = {'cakkaṃ', 'saṃkhittaṃ', 'cakkaṃ, saṃkhittaṃ', 'yāva asaññasattā', 'mūlaṃ kātabbaṃ.', 'mūlaṃ pucchitabbaṃ.', 'paṭiccasadisā', 'paṭiccasadisaṃ', 'sabbattha nava'}
for i, (a, b) in enumerate(zip(p, h)):
    if a.startswith('#'):
        continue
    pa = re.findall(r'\(([^()]*[a-zā][^()]*)\)', a)
    hb = re.findall(r'\(([^()]*[\u0900-\u097F][^()]*)\)', b)
    if len(pa) != len(hb):
        print('MISMATCH', i + 1, pa, hb); continue
    for x, y in zip(pa, hb):
        k = x.strip().lower()
        if k in skip or k in seen:
            continue
        seen.add(k)
        print(f'{i+1}| {x} || {y}')
