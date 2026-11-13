import os, re, sys
from collections import Counter, defaultdict
sys.path.insert(0, os.path.dirname(__file__))
from review_r9_common import *

PNUM = {'ekaṃ': 1, 'eko': 1, 'dve': 2, 'tīṇi': 3, 'tayo': 3, 'cattāri': 4, 'cattāro': 4, 'pañca': 5, 'cha': 6, 'satta': 7,
        'aṭṭha': 8, 'nava': 9, 'dasa': 10, 'ekādasa': 11, 'dvādasa': 12, 'terasa': 13, 'cuddasa': 14,
        'pannarasa': 15, 'paṇṇarasa': 15, 'soḷasa': 16, 'sattarasa': 17, 'aṭṭhārasa': 18, 'ekūnavīsati': 19,
        'vīsati': 20, 'ekavīsati': 21, 'bāvīsati': 22, 'dvāvīsati': 22, 'tevīsati': 23}
HNUM = {'एक': 1, 'दो': 2, 'तीन': 3, 'चार': 4, 'पाँच': 5, 'छह': 6, 'सात': 7, 'आठ': 8, 'नौ': 9, 'दस': 10,
        'ग्यारह': 11, 'बारह': 12, 'तेरह': 13, 'चौदह': 14, 'पंद्रह': 15, 'सोलह': 16, 'सत्रह': 17, 'अठारह': 18,
        'उन्नीस': 19, 'बीस': 20, 'इक्कीस': 21, 'बाईस': 22, 'तेईस': 23}
for k, v in {'ekavīsa': 21, 'ekavīsati': 21, 'dvāvīsa': 22, 'bāvīsa': 22, 'tevīsa': 23, 'catuvīsa': 24, 'pañcavīsa': 25,
              'chabbīsa': 26, 'sattavīsa': 27, 'aṭṭhavīsa': 28, 'ekūnatiṃsa': 29, 'tiṃsa': 30, 'ekatiṃsa': 31,
              'dvattiṃsa': 32, 'battiṃsa': 32, 'tettiṃsa': 33, 'catuttiṃsa': 34, 'pañcatiṃsa': 35, 'chattiṃsa': 36,
              'sattatiṃsa': 37, 'aṭṭhatiṃsa': 38, 'cattālīsa': 40, 'ekūnavīsa': 19, 'vīsa': 20}.items():
    PNUM[k] = v
for k, v in {'चौबीस': 24, 'पच्चीस': 25, 'छब्बीस': 26, 'सत्ताईस': 27, 'अट्ठाईस': 28, 'उनतीस': 29, 'तीस': 30,
              'इकतीस': 31, 'बत्तीस': 32, 'तैंतीस': 33, 'चौंतीस': 34, 'पैंतीस': 35, 'छत्तीस': 36, 'सैंतीस': 37,
              'अड़तीस': 38, 'चालीस': 40}.items():
    HNUM[k] = v
PL = r'a-zA-Zāīūṃṅñṭḍṇḷ'
PNUMRE = re.compile(r'(?<![%s])(%s)(?![%s])' % (PL, '|'.join(sorted(PNUM, key=len, reverse=True)), PL))
DV = 'ऀ-ॣ०-ॿ'
HNUMRE = re.compile(r'(?<![%s])(%s)(?![%s])(?! (?:का|के) वर्गीकरण| क्रम)' % (DV, '|'.join(sorted(HNUM, key=len, reverse=True)), DV))

CONDS = [('hetu', 'hetuyā', 'मूल'), ('ārammaṇa', 'ārammaṇe', 'विषय'), ('adhipati', 'adhipatiyā', 'प्रधानता'),
         ('anantara', 'anantare', 'निकटता'), ('samanantara', 'samanantare', 'पूर्ण निकटता'),
         ('sahajāta', 'sahajāte', 'सह-उत्पत्ति'), ('aññamañña', 'aññamaññe', 'परस्पर'), ('nissaya', 'nissaye', 'आश्रय'),
         ('upanissaya', 'upanissaye', 'प्रबल आश्रय'), ('purejāta', 'purejāte', 'पूर्व-उत्पत्ति'),
         ('pacchājāta', 'pacchājāte', 'पश्चात्-उत्पत्ति'), ('āsevana', 'āsevane', 'पुनरावृत्ति'), ('kamma', 'kamme', 'कर्म'),
         ('vipāka', 'vipāke', 'कर्म-फल'), ('āhāra', 'āhāre', 'आहार'), ('indriya', 'indriye', 'क्षमता'), ('jhāna', 'jhāne', 'ध्यान'),
         ('magga', 'magge', 'मार्ग'), ('sampayutta', 'sampayutte', 'जुड़ाव'), ('vippayutta', 'vippayutte', 'अलगाव'),
         ('atthi', 'atthiyā', 'उपस्थिति'), ('natthi', 'natthiyā', 'अनुपस्थिति'), ('vigata', 'vigate', 'विलीनता'),
         ('avigata', 'avigate', 'अविलीनता')]
H2C = {h: s for s, l, h in CONDS}
P2C = {}
for s, l, h in CONDS:
    P2C[l] = s
    for suf in ['paccayā', 'paccayena', 'paccayo', 'paccayaṃ', 'paccayādi']:
        P2C[s + suf] = s
P2C_heads = {s: s for s, l, h in CONDS}
alts = sorted(P2C, key=len, reverse=True)
PCRE = re.compile(r'(?<![%s])(no|na)?(%s)(?![%s])' % (PL, '|'.join(alts), PL))
PCRE_HY = re.compile(r'(?<![%s])(no|na)?(%s)(?=-)' % (PL, '|'.join(sorted(P2C_heads, key=len, reverse=True))))
HCRE = re.compile(r'(?<![%s])(%s)-कारण( के अभाव| के बिना| का अभाव)?' % (DV, '|'.join(sorted(H2C, key=len, reverse=True))))


def pconds(t):
    t = t.lower().replace('*', '')
    out = []
    for m in re.finditer(PCRE.pattern + '|' + PCRE_HY.pattern, t):
        if m.group(2):
            out.append((m.start(), P2C[m.group(2)], bool(m.group(1))))
        else:
            out.append((m.start(), m.group(4), bool(m.group(3))))
    out.sort()
    return [(c, n) for _, c, n in out]


def hconds(t):
    return [(H2C[m.group(1)], bool(m.group(2))) for m in HCRE.finditer(t)]


def pnums(t):
    return [PNUM[m.group(1)] for m in PNUMRE.finditer(t.lower())]


def hnums(t):
    return [HNUM[m.group(1)] for m in HNUMRE.finditer(t)]


issues = []
nseg = 0
nlines = 0
for f, sid, ne, p, h, pid, hid in pairs():
    nlines += 1
    if pid:
        nseg += 1
    if pid != hid:
        issues.append((f, sid, ne, 'IDMISMATCH', pid, hid))
    if pconds(p) != hconds(h):
        issues.append((f, sid, ne, 'COND', pconds(p), hconds(h)))
    if pnums(p) != hnums(h):
        issues.append((f, sid, ne, 'NUM', pnums(p), hnums(h)))
    pm = re.findall(r'\((\d+)\)', p)
    hm = re.findall(r'\((\d+)\)', h)
    if pm != hm:
        issues.append((f, sid, ne, 'MARK', pm, hm))
    pe = p.replace('…pe…', '…').count('…')
    if pe != h.count('…'):
        issues.append((f, sid, ne, 'ELLIPSIS', pe, h.count('…')))
    pd = p.count('–') + p.count('—')
    if pd != h.count('–') or '—' in h:
        issues.append((f, sid, ne, 'DASH', pd, h.count('–')))
    if re.search(r'["\'‘’]', h):
        issues.append((f, sid, ne, 'QUOTE', '', h))
    if p.count('“') != h.count('“') or p.count('”') != h.count('”'):
        issues.append((f, sid, ne, 'CURLYQ', p.count('“'), h.count('“')))
    # latin outside brackets
    hh = re.sub(r'\[[^\]]*\]', '', h)
    if re.search(r'[A-Za-zāīūṃṅñṭḍṇḷ]', hh):
        issues.append((f, sid, ne, 'LATIN', '', h))
    # sentence punctuation
    if not p.lstrip().startswith('#'):
        pp = re.sub(r'^\d+(-\d+)*\.\s', '', p)
        pdots = pp.count('.')
        hd = h.count('।')
        if pdots != hd or p.count('?') != h.count('?') or '.' in re.sub(r'^\d+(-\d+)*\.\s', '', h):
            issues.append((f, sid, ne, 'PUNCT', (pdots, p.count('?')), (hd, h.count('?'))))
        pend = p.rstrip()[-1:]
        hend = h.rstrip()[-1:]
        mp = {'.': '।', '?': '?', ')': ')', ']': ']', '…': '…', ':': ':', ',': ','}
        if mp.get(pend, pend) != hend:
            issues.append((f, sid, ne, 'END', pend, hend))
    else:
        if not h.lstrip().startswith('#') or p.count('#') != h.count('#') or p.count('*') != h.count('*'):
            issues.append((f, sid, ne, 'HEAD', p, h))

for f in FILES:
    for d in (PDIR, HDIR):
        t = load(os.path.join(d, f))
        if '\n\n\n' in t:
            issues.append((f, None, 0, 'DOUBLEBLANK', d[-30:], ''))
c = Counter(i[3] for i in issues)
print('lines', nlines, 'segments', nseg, dict(c))
for i in issues:
    print(i)
