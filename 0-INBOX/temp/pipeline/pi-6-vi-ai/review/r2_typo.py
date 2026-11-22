import re, os, collections
ROOT = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation'
P = os.path.join(ROOT, 'pali', 'pi-6_split_chapters')
V = os.path.join(ROOT, 'vietnamese', 'pi-6-vietnamese-plain-rails_split_chapters')
FILES = ['3-06-ayatanayamaka.md', '4-dhatuyamaka.md', '5-01-saccayamaka.md', '5-02-saccayamaka.md',
         '5-03-saccayamaka.md', '6-01-sankharayamaka.md', '6-02-sankharayamaka.md', '7-01-anusayayamaka.md']

def lines(path):
    with open(path, encoding='utf-8') as f:
        return [l.rstrip('\n') for l in f if l.strip()]

CHK = [
    ('4dots', r'…\.'), ('dblspace', r'\S  +\S'), ('spcomma', r' [,.;?]'), ('dots3', r'\.\.\.'),
    ('noqword', r'(?<!không)(?<!chưa)(?<!chăng)(?<!nào)(?<!đâu)\?'), ('lower-after-dot', r'\. [a-zđàáảãạâăèéêìíòóôơùúưỳý]'),
    ('cap-after-ellipsis', r'…\s?[A-ZĐ]'), ('trail', r'[^.?)…\]”:]\s*\^[\d-]+$'), ('trail2', r'[^.?)…\]”:]$'),
    ('comma-thi', r',\s*thì ở[^,]*,\s*thì'), ('vanhung', r'nhưng.*nhưng'), ('khongco-van', r'không có [^,.]*vẫn'),
]
c = collections.Counter(); ex = collections.defaultdict(list)
for fn in FILES:
    pl = lines(os.path.join(P, fn)); vl = lines(os.path.join(V, fn))
    for i, (a, b) in enumerate(zip(pl, vl)):
        if b.startswith('#'):
            continue
        bb = re.sub(r'\[[^\]]*\]', '', b)
        for name, rx in CHK:
            for m in re.finditer(rx, bb):
                c[name] += 1
                if len(ex[name]) < 6:
                    s = max(0, m.start() - 50)
                    ex[name].append('%s L%d: %s' % (fn, i, bb[s:m.end() + 30]))
for k, v in c.items():
    print(k, v)
    for e in ex[k]:
        print('   ', e)
