# r1 reviewer helper (console only): per-segment polarity counts, name consistency, typography.
import re, sys, os
ROOT = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation'
P = os.path.join(ROOT, 'pali', 'pi-4_split_chapters')
V = os.path.join(ROOT, 'vietnamese', 'pi-4-vietnamese-plain-rails_split_chapters')
FILES = ['preamble.md', '1-matika.md', '2-ekakapuggalapannatti.md']

def segs(path):
    out, cur = [], []
    for l in open(path, encoding='utf-8').read().split('\n'):
        if not l.strip():
            if cur:
                out.append(cur); cur = []
            continue
        cur.append(l)
    if cur:
        out.append(cur)
    return out

def bid(seg):
    m = re.search(r'\^([\w-]+)\s*$', seg[-1])
    return m.group(1) if m else '?'

PNEG = re.compile(r"(?<![\wāīūṃṅñṭḍṇḷ])(na|no|neva|nevasekkha\w*|natthi|nappajānāti|nārabhati|ananu\w*|apariyo\w*)(?![\wāīūṃṅñṭḍṇḷ])|\b(a|an)(?=[a-zāīūṃṅñṭḍṇḷ]{3,})", re.I)
VNEG = re.compile(r'\b(không|chưa|chẳng)\b', re.I)

def pneg_count(s):
    # rough: count na/no/neva tokens
    return len(re.findall(r"(?<![^\s\[\(,;–\"])(na|no|neva|nappajānāti|nārabhati)(?=[\s,;.])", s))

for f in FILES:
    ps, vs = segs(os.path.join(P, f)), segs(os.path.join(V, f))
    print('#####', f, len(ps), len(vs))
    for p, v in zip(ps, vs):
        b = bid(p)
        if bid(v) != b:
            print('ID MISMATCH', b, bid(v))
        if len(p) != len(v):
            print('LINECOUNT', b, len(p), len(v))
        for i, (pl, vl) in enumerate(zip(p, v)):
            pn = pneg_count(pl)
            vn = len(VNEG.findall(vl))
            # typography
            issues = []
            if '….' in vl or '...' in vl:
                issues.append('ellipsis')
            if '"' in vl:
                issues.append('straight quote')
            if re.search(r'\s[.,;:?!]', vl.replace(' –', '').replace('– ', '')):
                issues.append('space before punct')
            if vl.count('–') != pl.count('–'):
                issues.append('dash count')
            if pl.rstrip().split(' ^')[0].endswith('?') != vl.rstrip().split(' ^')[0].endswith('?'):
                issues.append('qmark end')
            # bracket count
            if pl.count('[') != vl.count('['):
                issues.append('bracket count %d/%d' % (pl.count('['), vl.count('[')))
            # Latin words with Pali diacritics outside brackets
            outside = re.sub(r'\[[^\]]*\]', '', vl)
            lat = re.findall(r'\b\w*[āīūṃṅñṭḍṇḷ]\w*\b', outside)
            if lat:
                issues.append('pali outside brackets: ' + ','.join(lat))
            if os.environ.get('R1ALL') or issues or (pn != vn and os.environ.get('R1NEG')):
                print(f'{b} L{i}: Pneg={pn} Vneg={vn} {issues}')
