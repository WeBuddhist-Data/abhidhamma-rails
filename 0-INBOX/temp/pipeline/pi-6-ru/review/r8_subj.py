"""r8: map Pāli answer-subject phrases (persons / planes / moments) to Russian ones.
Pāli subject = text of each answer sentence (or of the part after 'no ca' is ignored) before the first
'tesaṃ' / 'tattha' / indriya; Russian subject = text before the first 'там' / verb / 'не' / 'и возни' / indriya.
"""
import re, sys, collections
sys.path.insert(0, r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-ru\review')
from r8_check import FILES, load, P_RE, R_RE

def p_subj(s):
    m = re.search(r'\b(tesaṃ|tattha|te)\b|' + P_RE.pattern, s)
    return s[:m.start()].strip() if m else None

def r_subj(s):
    m = re.search(r'(?<![а-яё])(там|не(?! связанн)|ни|и возни|и не|и разов|и разви|и устран|и осуществ|и полностью|и понима|возни(?!кновени)\w*|развива\w*|разовь\w*|устраня\w*|устранил\w*|устранит\w*|осуществ\w*|понима\w*|понял\w*|поймёт|поймут|полностью)(?![а-яё])|' + R_RE.pattern, s, re.I)
    return s[:m.start()].strip(' ,') if m else None

def main():
    d = collections.defaultdict(collections.Counter); first = {}
    for f in FILES:
        p, r = load(f)
        for i, (a, b) in enumerate(zip(p, r)):
            if not a.strip() or a.startswith('#') or a.rstrip().endswith('?') or '?' in a and a.index('?') > len(a) - 15:
                continue
            a2 = re.sub(r'\s*\^[\w-]+\s*$', '', a); b2 = re.sub(r'\s*\^[\w-]+\s*$', '', b)
            ps = re.split(r'(?<=[.?])\s+', a2); rs = re.split(r'(?<=[.?])\s+', b2)
            if len(ps) != len(rs):
                continue
            for x, y in zip(ps, rs):
                if x.endswith('?') or x.startswith('(') or re.match(r'(Yassa|Yattha|Yo)\b', x):
                    continue
                sx = p_subj(x); sy = r_subj(y)
                if sx is None: continue
                d[sx][sy] += 1; first.setdefault((sx, sy), '%s:%d' % (f[:5], i + 1))
    for x in sorted(d, key=lambda k: -sum(d[k].values())):
        print('P', sum(d[x].values()), x)
        for y, c in d[x].most_common():
            print('   R', c, first[(x, y)], y)

main()
