"""r5: citta chapter: verb tense/polarity sequence, answers, person/moment tokens per line."""
import re, sys, itertools, collections
P = 'AI_translation/pali/pi-6_split_chapters/8-cittayamaka.md'
R = 'AI_translation/russian/pi-6-russian-plain-rails_split_chapters/8-cittayamaka.md'
show = len(sys.argv) > 1

PV = re.compile(r"(?<![a-zāīūṃ])(uppajj|nirujjh|uppann|niruddh)(atī|ati|itthā|ittha|issatī|issati|amān\w*|añ\w*|aṃ|an\w*|ā|o)(?:ti)?(?![a-zāīūṃ])")
def ptoks(s):
    out = []
    last = 0
    for m in PV.finditer(s):
        pre = s[last:m.start()]
        last = m.end()
        stem, e = m.group(1), m.group(2)
        lem = 'U' if stem in ('uppajj', 'uppann') else 'N'
        if stem in ('uppann', 'niruddh'): t = 'pp'
        elif e.startswith('amān'): t = 'prp'
        elif e.startswith('at'): t = 'P'
        elif e.startswith('itth'): t = 'A'
        elif e.startswith('iss'): t = 'F'
        else: t = '?' + e
        neg = re.search(r'(?<![a-zāīūṃ])(?:na|ceva na|na ca)\s*$', pre.strip() + ' ') is not None or re.search(r'(?<![a-zāīūṃ])na\s+(?:ceva\s+|ca\s+)?$', pre) is not None
        if re.search(r'(?<![a-z])no ca(?![a-z])', pre): neg = not neg
        out.append(('~' if neg else '') + lem + t)
    return out
RV = [
    (r'возника(?:ет|ют)', 'UP'), (r'возникал[аои]?', 'UA'), (r'возникн(?:ет|ут)', 'UF'),
    (r'прекраща(?:ется|ются)', 'NP'), (r'прекращал(?:ся|ась|ось|ись)', 'NA'), (r'прекрат(?:ится|ятся)', 'NF'),
    (r'возникающ\w*', 'Uprp'), (r'прекращающ\w*', 'Nprp'), (r'возникш\w*', 'Upp'), (r'прекративш\w*', 'Npp'),
]
RVX = re.compile('|'.join('(?P<g%d>(?<![а-яё])%s(?![а-яё]))' % (i, r) for i, (r, t) in enumerate(RV)))
def rtoks(s):
    out = []
    ms = list(RVX.finditer(s))
    last = 0
    for i, m in enumerate(ms):
        pre = s[last:m.start()]
        last = m.end()
        t = RV[int(m.lastgroup[1:])][1]
        neg = re.search(r'(?<![а-яё])(?:не|ни)(?:\s+(?:является|являются|был\w*|будет))?\s+$', pre) is not None
        out.append(('~' if neg else '') + t)
    return out

def pans(s):
    m = re.search(r'\?\s*(Āmantā|No|Natthi|\w+)\.', s)
    return m.group(1) if m else None
def rans(s):
    m = re.search(r'\?\s*([А-ЯЁа-яё ]+)\.', s)
    return m.group(1) if m else None
AMAP = {'Āmantā': 'Да', 'No': 'Нет', 'Natthi': 'Такого нет', 'Uppajjittha': 'Возникал', 'Nirujjhittha': 'Прекращался',
        'Uppajjissati': 'Возникнет', 'Nirujjhissati': 'Прекратится', 'Nirujjhati': 'Прекращается', 'Uppajjati': 'Возникает'}

PT = [(r'pacchimacitt', 'LAST'), (r'nirodhasamāpann', 'NS'), (r'asaññasatt', 'AS'), (r'uppādakkhaṇ', 'UK'),
      (r'bhaṅgakkhaṇ', 'BK'), (r'itaresaṃ', 'OTH'), (r'(?<![a-zāīūṃ])atīt', 'PAST'), (r'anāgat', 'FUT'), (r'paccuppann', 'PRES'),
      (r'arūp', 'ARU'), (r'pañcavokār', 'PV')]
RT = [(r'последн', 'LAST'), (r'достижение прекращения', 'NS'), (r'без восприятия', 'AS'), (r'момент\w* возникновения', 'UK'),
      (r'момент\w* распада', 'BK'), (r'остальн', 'OTH'), (r'прошл', 'PAST'), (r'будущ', 'FUT'), (r'настоящ', 'PRES'),
      (r'без форм', 'ARU'), (r'пят\w+ совокупност', 'PV')]
def tok(s, T):
    rx = re.compile('|'.join('(?P<g%d>%s)' % (i, r) for i, (r, t) in enumerate(T)), re.I)
    return [T[int(m.lastgroup[1:])][1] for m in rx.finditer(s)]

pl = open(P, encoding='utf-8').read().split('\n')
rl = open(R, encoding='utf-8').read().split('\n')
cnt = collections.Counter()
for i, (p, r) in enumerate(zip(pl, rl), 1):
    if not p.strip() or p.startswith('#'): continue
    probs = []
    a = [k for k, _ in itertools.groupby(ptoks(p))]
    b = [k for k, _ in itertools.groupby(rtoks(r))]
    if a != b: probs.append('VERB %s | %s' % (','.join(a), ','.join(b)))
    pa, ra = pans(p), rans(r)
    if pa and AMAP.get(pa) != ra: probs.append('ANS %s|%s' % (pa, ra))
    if not pa and ra and ra in AMAP.values(): probs.append('ANS %s|%s' % (pa, ra))
    x, y = sorted(tok(p, PT)), sorted(tok(r, RT))
    if x != y: probs.append('TOK %s | %s' % (','.join(x), ','.join(y)))
    for q in probs: cnt[q.split()[0]] += 1
    if probs:
        print('%d %s' % (i, ' || '.join(probs)))
        if show: print('  P', p[:500]); print('  R', r[:600])
print(cnt)
