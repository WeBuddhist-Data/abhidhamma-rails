"""r5: anusaya line-pair checks: members, planes, persons, verb polarity, answers."""
import re, sys, collections
P = 'AI_translation/pali/pi-6_split_chapters/'
R = 'AI_translation/russian/pi-6-russian-plain-rails_split_chapters/'
FILES = ['7-06-anusayayamaka', '7-07-anusayayamaka', '7-08-anusayayamaka', '7-09-anusayayamaka',
         '7-10-anusayayamaka', '7-11-anusayayamaka']
if len(sys.argv) > 1: FILES = sys.argv[1].split(',')
show = 'v' in (sys.argv[2] if len(sys.argv) > 2 else '')

PM = [('kāmarāg', 'K'), ('paṭigh', 'P'), ('mān', 'M'), ('diṭṭh', 'D'), ('vicikicch', 'V'), ('bhavarāg', 'B'), ('avijj', 'A')]
PMRX = re.compile(r'(kāmarāg|paṭigh|mān|diṭṭh|vicikicch|bhavarāg|avijj)ānusay', re.I)
RM = [('к страсти к существованию', 'B'), ('к чувственной страсти', 'K'), ('к неприязни', 'P'), ('к самомнению', 'M'),
      ('к воззрениям', 'D'), ('к колебанию', 'V'), ('к неведению', 'A')]
RMRX = re.compile('|'.join(re.escape(a) for a, _ in RM))
RMD = dict(RM)
PMD = {a.lower(): b for a, b in PM}

def pmem(s): return [PMD[m.group(1).lower()] for m in PMRX.finditer(s)]
def rmem(s): return [RMD[m.group(0)] for m in RMRX.finditer(s)]

# planes
PPL = re.compile(r'(\bna\s+)?(arūpadhātu\w*|rūpadhātu\w*|kāmadhātu\w*|dukkhāya vedanāya|dvīsu vedanāsu|tīsu vedanāsu|apariyāpanne|sabbattha)', re.I)
def ppl(s):
    out = []
    for m in PPL.finditer(s):
        w = m.group(2).lower()
        t = 'AD' if w.startswith('arūp') else 'RD' if w.startswith('rūp') else 'KD' if w.startswith('kām') else \
            'DV' if w.startswith('dukkh') else '2V' if w.startswith('dvī') else '3V' if w.startswith('tīs') else \
            'AP' if w.startswith('apar') else 'ALL'
        if 'mūlak' in w: continue
        out.append(('~' if m.group(1) else '') + t)
    return out
RPL = re.compile(r'(не\s+)?(?:в|из|во)?\s*(мир\w*\s+без\s+форм|мир\w*\s+форм|мир\w*\s+чувственных\s+желаний|болезненн\w+\s+чувств\w*|двух\s+видах\s+чувства|трёх\s+видах\s+чувства|не\s+принадлежит\s+к\s+кругам|нигде|везде|во\s+всех)', re.I)
def rpl(s):
    out = []
    for m in RPL.finditer(s):
        w = m.group(2).lower()
        t = 'AD' if 'без форм' in w else 'RD' if 'форм' in w else 'KD' if 'желаний' in w else 'DV' if 'болезн' in w else \
            '2V' if 'двух' in w else '3V' if 'трёх' in w else 'AP' if 'принадлежит' in w else 'ALL'
        out.append(('~' if m.group(1) else '') + t)
    return out

# persons
PPE = [(r'aggamaggasamaṅg\w*', 'AGG'), (r'anāgāmimaggasamaṅg\w*', 'ANM'), (r'aṭṭhamak\w*', 'ATT'),
       (r'dvinnaṃ maggasamaṅgīna\w*', '2MS'), (r'anāgāmi(?!magg)\w*', 'ANA'), (r'arah\w*', 'ARH'),
       (r'puthujjan\w*', 'PUT'), (r'dvinnaṃ puggalānaṃ', '2P'), (r'tiṇṇaṃ puggalānaṃ', '3P'),
       (r'catunnaṃ puggalānaṃ', '4P'), (r'pañcannaṃ puggalānaṃ', '5P'), (r'sveva puggalo|tasseva puggalassa|tesaññeva puggalānaṃ', 'SAME'),
       (r'avasesā puggalā|avasesānaṃ puggalānaṃ', 'REST'), (r'sabbesaṃ|sabbe', 'ALLP')]
PPERX = re.compile('|'.join('(?P<g%s>%s)' % (t, r) for r, t in PPE), re.I)
RPE = [(r'высш\w+\s+пут\w+', 'AGG'), (r'пут\w+\s+невозвращения', 'ANM'), (r'восьмой\s+ступени', 'ATT'),
       (r'двух\s+обладающих\s+путём', '2MS'), (r'невозвращающ\w*', 'ANA'), (r'архат\w*', 'ARH'),
       (r'обычн\w+\s+человек\w*', 'PUT'), (r'двух\s+личност\w*', '2P'), (r'трёх\s+личност\w*', '3P'),
       (r'четырёх\s+личност\w*', '4P'), (r'пяти\s+личност\w*', '5P'), (r'(?:эта|этой|этих|у этой|этого)\s+же\s+\w+', 'SAME'),
       (r'остальн\w+\s+личност\w*', 'REST'), (r'\bвсех\b|\bвсе\b', 'ALLP')]
RPERX = re.compile('|'.join('(?P<g%s>%s)' % (t, r) for r, t in RPE), re.I)
def pper(s): return [m.lastgroup[1:] for m in PPERX.finditer(s)]
def rper(s): return [m.lastgroup[1:] for m in RPERX.finditer(s)]

# verb polarity
PV = re.compile(r'(\bna\s+)?\b(nappajah\w*|pajah\w*|parijān\w*|appahīn\w*|pahīn\w*|nānuse\w*|anuse\w*|nuppajj\w*|uppajj\w*|upapajj\w*)', re.I)
def ppol(s):
    s = re.sub(r'na vattabb\w* "[^"]*"ti vā "[^"]*"ti vā', 'NV', s)
    out = []
    last = 0
    for m in PV.finditer(s):
        flip = re.search(r'(?<![a-z])no ca(?![a-z])', s[last:m.start()]) is not None
        _unused = re.search(r"no ca", s[last:m.start()]) is not None
        last = m.end()
        w = m.group(2).lower()
        cls = 'PJ' if 'pajah' in w else 'PR' if 'parij' in w else 'PH' if 'pahīn' in w else 'AN' if 'nuse' in w else 'UP' if w.startswith(('upapajj',)) else 'UJ'
        neg = bool(m.group(1)) or w.startswith(('napp', 'appah', 'nānus', 'nupp'))
        if flip: neg = not neg
        out.append(('~' if neg else '') + cls)
    return out
RV = re.compile(r'(\bне\s+)?\b(устраня\w*|устранен\w*|устранён\w*|понима\w*|залега\w*|возника\w*|перерожда\w*)', re.I)
def rpol(s):
    s = re.sub(r'[Нн]е следует говорить ни «[^»]*», ни «[^»]*»', 'NV', s)
    ms = list(RV.finditer(s))
    out = []
    for i, m in enumerate(ms):
        w = m.group(2).lower()
        cls = 'PJ' if w.startswith('устраня') else 'PH' if w.startswith('устран') else 'PR' if 'понима' in w else 'AN' if 'залега' in w else 'UP' if 'перерожд' in w else 'UJ'
        neg = bool(m.group(1))
        end = ms[i + 1].start() if i + 1 < len(ms) else len(s)
        seg = s[m.end():end]
        seg = re.split(r'[.;?]', seg)[0]
        k = len(re.findall(r'(?<![а-яё])ни(?![а-яё])', seg, re.I))
        n = k if (neg and k >= 2) else 1
        out += [('~' if neg else '') + cls] * n
    return out

def pans(s): return ['Y' if a == 'Āmantā' else 'N' if a == 'No' else 'X' for a in re.findall(r'Āmantā|\bNo\b(?=\.)|\bNatthi\b', s)]
def rans(s): return ['Y' if a == 'Да' else 'N' if a == 'Нет' else 'X' for a in re.findall(r'(?<![а-яё])Да(?![а-яё])|Нет(?=\.)|Такого нет', s)]

cnt = collections.Counter()
for f in FILES:
    pl = open(P + f + '.md', encoding='utf-8').read().split('\n')
    rl = open(R + f + '.md', encoding='utf-8').read().split('\n')
    for i, (p, r) in enumerate(zip(pl, rl), 1):
        if not p.strip() or p.startswith('#'): continue
        probs = []
        a, b = pmem(p), rmem(r)
        if sorted(a) != sorted(b): probs.append('MEM %s|%s' % (''.join(a), ''.join(b)))
        elif a != b: probs.append('MEMORD %s|%s' % (''.join(a), ''.join(b)))
        a, b = ppl(p), rpl(r)
        if a != b: probs.append('PL %s|%s' % (','.join(a), ','.join(b)))
        a, b = pper(p), rper(r)
        if a != b: probs.append('PER %s|%s' % (','.join(a), ','.join(b)))
        import itertools
        a = [k for k, _ in itertools.groupby(ppol(p))]; b = [k for k, _ in itertools.groupby(rpol(r))]
        if a != b: probs.append('POL %s|%s' % (','.join(a), ','.join(b)))
        a, b = pans(p), rans(r)
        if a != b: probs.append('ANS %s|%s' % (a, b))
        for x in probs: cnt[x.split()[0]] += 1
        if probs:
            print('%s:%d %s' % (f, i, ' || '.join(probs)))
            if show: print('  P', p[:600]); print('  R', r[:800])
print(cnt)
