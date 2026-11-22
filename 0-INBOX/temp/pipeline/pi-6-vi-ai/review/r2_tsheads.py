import re, sys, os
# Console-only: compare counts of head terms per segment between ours and the reference. Writes nothing.
ROOT = r'D:\Work\OpenPecha\abhidhamma-rails'
V = os.path.join(ROOT, 'AI_translation', 'vietnamese', 'pi-6-vietnamese-plain-rails_split_chapters')
TS = os.path.join(ROOT, '1-SOURCES', 'Translations', 'Vietnamese', 'vi-6-tinh_su.md')
FILES = ['3-06-ayatanayamaka.md', '4-dhatuyamaka.md', '5-01-saccayamaka.md', '5-02-saccayamaka.md',
         '5-03-saccayamaka.md', '6-01-sankharayamaka.md', '6-02-sankharayamaka.md', '7-01-anusayayamaka.md']
TERMS = [  # (name, ours regex, ref regex)
    ('arahant', r'a-la-hán', r'la-? ?hán'),
    ('puthujjana', r'phàm phu', r'phàm phu'),
    ('asaññasatta', r'vô tưởng', r'vô tưởng'),
    ('suddhavasa', r'tịnh cư', r'tịnh cư'),
    ('uppadakkhana', r'khoảnh khắc sinh khởi', r'sát-? ?na sanh'),
    ('bhangakkhana', r'khoảnh khắc tan rã', r'sát-? ?na diệt'),
    ('nirodhasamapanna', r'thiền chấm dứt', r'(thiền|nhập) diệt'),
    ('apayika', r'cõi khổ', r'khổ cảnh|đọa xứ|cõi khổ|ác đạo'),
]
def segs(lines):
    d = {}; cur = []
    for l in lines:
        if not l.strip() or l.startswith('![['):
            continue
        cur.append(l)
        m = re.search(r'\^([\d-]+)\s*$', l)
        if m:
            d[m.group(1)] = ' '.join(cur).lower(); cur = []
    return d
with open(TS, encoding='utf-8') as f:
    tsd = segs([l.rstrip('\n') for l in f])
for fn in FILES:
    with open(os.path.join(V, fn), encoding='utf-8') as f:
        od = segs([l.rstrip('\n') for l in f])
    for k, v in od.items():
        if k not in tsd:
            continue
        t = tsd[k]
        d = []
        for name, a, b in TERMS:
            na, nb = len(re.findall(a, v)), len(re.findall(b, t))
            if na != nb:
                d.append('%s %d/%d' % (name, na, nb))
        if d:
            print(fn, k, '; '.join(d))
