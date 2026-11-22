import re, sys, os
# Console-only comparison of answer types (ours vs reference). Writes nothing.
ROOT = r'D:\Work\OpenPecha\abhidhamma-rails'
V = os.path.join(ROOT, 'AI_translation', 'vietnamese', 'pi-6-vietnamese-plain-rails_split_chapters')
TS = os.path.join(ROOT, '1-SOURCES', 'Translations', 'Vietnamese', 'vi-6-tinh_su.md')
FILES = ['3-06-ayatanayamaka.md', '4-dhatuyamaka.md', '5-01-saccayamaka.md', '5-02-saccayamaka.md',
         '5-03-saccayamaka.md', '6-01-sankharayamaka.md', '6-02-sankharayamaka.md', '7-01-anusayayamaka.md']

def segs(lines):
    d = {}; cur = []
    for l in lines:
        if not l.strip() or l.startswith('![['):
            continue
        cur.append(l)
        m = re.search(r'\^([\d-]+)\s*$', l)
        if m:
            d[m.group(1)] = cur; cur = []
    return d

def ours_types(text):
    t = re.sub(r'\[[^\]]*\]', '', text)
    out = []
    for q in re.split(r'\?', t)[1:]:
        q = q.strip()
        if q.startswith('Đúng vậy'):
            out.append('Y')
        elif re.match(r'Không có\b', q) and len(q) < 14:
            out.append('X')
        elif re.match(r'Không\.', q):
            out.append('N')
        elif q.startswith(('…', '(')) or not q or re.match(r'^\(?[a-zđ]\)', q):
            out.append('-')
        else:
            out.append('P')
    return out

def ts_types(text):
    t = re.sub(r'\[[^\]]*\]', '', text)
    out = []
    for q in re.split(r'\?', t)[1:]:
        q = q.strip()
        if re.match(r'(Phải rồi|Phải\.|Đúng vậy|Đúng)', q):
            out.append('Y')
        elif re.match(r'Không có\.', q):
            out.append('X')
        elif re.match(r'(Không phải|Không\.)', q):
            out.append('N')
        elif not q or q.startswith(('…', '(', 'Hay là', 'Hay')) or re.match(r'^\d+\.', q):
            out.append('-')
        else:
            out.append('P')
    return out

def norm(seq):
    return [x for x in seq if x != '-']

with open(TS, encoding='utf-8') as f:
    tsd = segs([l.rstrip('\n') for l in f])
show = os.environ.get('R2SHOW')
for fn in FILES:
    with open(os.path.join(V, fn), encoding='utf-8') as f:
        od = segs([l.rstrip('\n') for l in f])
    miss = []; diff = 0
    for k, v in od.items():
        if k not in tsd:
            miss.append(k); continue
        a = norm(ours_types(' '.join(v))); b = norm(ts_types(' '.join(tsd[k])))
        if a != b:
            diff += 1
            print('DIFF', fn, k, ''.join(a), '|', ''.join(b))
            if show and k in show.split(','):
                print('  O:', ' / '.join(v))
                print('  T:', ' / '.join(tsd[k]))
    print('FILE', fn, 'segments', len(od), 'missing-in-ref', len(miss), ' '.join(miss[:30]), 'diff', diff)
