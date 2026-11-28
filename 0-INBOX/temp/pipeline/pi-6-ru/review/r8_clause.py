"""r8: clause-level check of answer sentences: split at 'no ca' / ', но ' and compare members, tense, polarity per clause.
For 'Xñca ... Yñca ...' sentences compare the polarity of each half (Russian 'и (не) ..., и (не) ...' / 'ни ..., ни ...')."""
import re, sys
sys.path.insert(0, r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-ru\review')
from r8_check import FILES, load, p_members, r_members, p_tense, r_tense

PNEG = r'\bna\b|\bnuppajj|\bnappaj|\bnanirujjh'
def pn(s): return len(re.findall(PNEG, s))
def rn(s):
    s = re.sub(r'не связанн\w*', '', s)
    return len(re.findall(r'(?<![а-яё])(не|ни)(?![а-яё])', s, re.I))
dd = lambda t: [x for k, x in enumerate(t) if k == 0 or t[k - 1] != x]

bad = 0; n = 0
for f in FILES:
    p, r = load(f)
    for i, (a, b) in enumerate(zip(p, r)):
        if not a.strip() or a.startswith('#'): continue
        a2 = re.sub(r'\s*\^[\w-]+\s*$', '', a); b2 = re.sub(r'\s*\^[\w-]+\s*$', '', b)
        ps = re.split(r'(?<=[.?])\s+', a2); rs = re.split(r'(?<=[.?])\s+', b2)
        if len(ps) != len(rs): continue
        for x, y in zip(ps, rs):
            if x.endswith('?') or x.startswith('('): continue
            if re.search(r'\bno ca\b', x):
                n += 1
                px = re.split(r',?\s*\bno ca\b', x); ry = re.split(r', но ', y)
                if len(px) != 2 or len(ry) != 2:
                    bad += 1; print('SPLIT', f, i + 1, x[:60], '|', y[:60]); continue
                # first clause: same polarity; second clause: inverted
                e1, e2 = pn(px[0]), 1 - pn(px[1])
                g1, g2 = rn(ry[0]), rn(ry[1])
                m1 = p_members(px[0]) == r_members(ry[0]) and p_members(px[1]) == r_members(ry[1])
                t1 = dd(p_tense(px[0])) == dd(r_tense(ry[0])) and dd(p_tense(px[1])) == dd(r_tense(ry[1]))
                if (e1, e2) != (g1, g2) or not m1 or not t1:
                    bad += 1
                    print('NOCA', f, i + 1, (e1, e2), (g1, g2), 'mem' if not m1 else '', 'tense' if not t1 else '', '|', y[:150])
            elif re.search(r'ñca\b', x):
                n += 1
                halves = re.split(r'(?=\b\w+ñca\b)', x)
                halves = [h for h in halves if re.search(r'ñca\b', h)]
                if len(halves) != 2:
                    continue
                pol = [pn(h) for h in halves]
                # Russian: 'и не ..., и не ...' / 'ни ..., ни' / 'и ..., и ...'
                if re.search(r'(?<![а-яё])ни (?:[^,]+), ни ', y):
                    rpol = [1, 1]
                else:
                    ms = list(re.finditer(r'(?<![а-яё])и (не )?(?=(?:возни|разви|разов|устран|осуществ|полностью|понима|понял|поймёт|поймут))', y))
                    rpol = [1 if mm.group(1) else 0 for mm in ms[-2:]] if len(ms) >= 2 else None
                mem = p_members(x) == r_members(y)
                if rpol != pol or not mem:
                    bad += 1; print('BOTH', f, i + 1, pol, rpol, '' if mem else 'mem', '|', y[-160:])
print('clauses', n, 'flags', bad)
