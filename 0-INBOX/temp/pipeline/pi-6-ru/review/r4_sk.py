"""r4: 6-02 saṅkhāra checks.
mode concepts: per line compare counts of person/time concept words (Pāli vs Russian)
mode skel: unique verb/member/polarity skeleton pairs per sentence
"""
import re, sys, collections
BASE = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation'
F = '6-02-sankharayamaka.md'
p = open(BASE + '\\pali\\pi-6_split_chapters\\' + F, encoding='utf-8').read().split('\n')
r = open(BASE + '\\russian\\pi-6-russian-plain-rails_split_chapters\\' + F, encoding='utf-8').read().split('\n')

CONC = [
    ('uppādakkhaṇe', r'в момент возникновения'),
    ('bhaṅgakkhaṇe', r'в момент распада'),
    ('pacchimacitt', r'последн\w+ ум'),
    ('anantarā', r'сразу после'),
    ('asaññasatt', r'без восприятия'),
    ('nirodhasamāpann', r'достижение прекращения'),
    ('(?<!a)rūpāvacar', r'(?<!без )форм\b'),
    ('arūpāvacar', r'без форм'),
    ('kāmāvacar', r'чувственных желаний'),
    ('itaresaṃ', r'остальн'),
    ('paṭhamajjhān', r'первое'), ('dutiyajjhān', r'второе'), ('tatiyajjhān', r'третье'), ('catutthajjhān', r'четвёртое'),
    ('samāpannānaṃ', r'вошедших'),
    ('assāsapassās', r'вдохов и выдохов'),
    ('vitakk', r'направленн'),
    ('suddhāvās', r'Чистых обител'),
    ('pacchimabhavik', r'последней жизнью'),
    ('parinibbāy', r'окончательного угасания'),
    ('sabbesaṃ', r'[Уу] всех'),
    ('tesaṃyeva', r'у них же'),
    ('bhūmiyaṃ', r'на уровне'),
    ('vattamāne', r'присутствует'),
    ('upapajj', r'перерожд|переродив'),
]

def concepts():
    n = 0
    for i, (a, b) in enumerate(zip(p, r), 1):
        if not a.strip() or a.startswith('#'):
            continue
        for pp, rr in CONC:
            c1 = len(re.findall(pp, a, flags=re.I)); c2 = len(re.findall(rr, b, flags=re.I))
            if pp == 'samāpannānaṃ':
                c1 -= len(re.findall('nirodhasamāpannānaṃ', a, flags=re.I))
                c2 -= len(re.findall('вошедших в медитативное достижение', b))
            if c1 != c2:
                n += 1
                print(i, pp, c1, c2)
    print('concept mismatches', n)

VERB_P = [(r'\bnuppajjat[iī]|\bna uppajjat[iī]', 'neg U0'), (r'\bnuppajjitth[aā]', 'neg U1'), (r'\bnuppajjissat[iī]', 'neg U2'),
          (r'\buppajjat[iī]', 'U0'), (r'\buppajjitth[aā]', 'U1'), (r'\buppajjissat[iī]', 'U2'),
          (r'\bna nirujjhat[iī]', 'neg N0'), (r'\bna nirujjhitth[aā]', 'neg N1'), (r'\bna nirujjhissat[iī]', 'neg N2'),
          (r'\bnirujjhat[iī]', 'N0'), (r'\bnirujjhitth[aā]', 'N1'), (r'\bnirujjhissat[iī]', 'N2'),
          (r'\bparijānāt[iī]', 'P0'), (r'\bupapajj\w+', 'UPAP'), (r'\bparinibbāyissanti', 'PNB')]
VERB_R = [(r'\bне возникает', 'neg U0'), (r'\bне возникал\w*', 'neg U1'), (r'\bне возникнет', 'neg U2'),
          (r'\bвозникает', 'U0'), (r'\bвозникал\w*', 'U1'), (r'\bвозникнет', 'U2'),
          (r'\bне прекращается', 'neg N0'), (r'\bне прекращался', 'neg N1'), (r'\bне прекратится', 'neg N2'),
          (r'\bпрекращается', 'N0'), (r'\bпрекращался', 'N1'), (r'\bпрекратится', 'N2'),
          (r'\bпонимает', 'P0'), (r'\bперерожд\w+|\bпереродив\w+', 'UPAP'), (r'\bдостигнет окончательного', 'PNB')]

def skel(s, table, mem):
    out = []
    pat = '|'.join('(?P<g%d>%s)' % (i, x) for i, (x, _) in enumerate(table))
    toks = []
    for m in re.finditer(pat, s, flags=re.I):
        for i, (_, t) in enumerate(table):
            if m.group('g%d' % i):
                toks.append((m.start(), t))
    for m in re.finditer(mem, s, flags=re.I):
        toks.append((m.start(), 'M'))
    for m in re.finditer(r'\bno ca\b|, но\b', s):
        toks.append((m.start(), 'BUT'))
    for m in re.finditer(r'\bни\b', s):
        toks.append((m.start(), 'ni'))
    for m in re.finditer(r'[?.]', s):
        toks.append((m.start(), m.group(0)))
    toks.sort()
    return ' '.join(t for _, t in toks)

MEM_P = r'(kāya|vacī|citta)saṅkhār\w*'
MEM_R = r'телесн\w+ формирующ\w+ фактор\w*|речев\w+ формирующ\w+ фактор\w*|формирующ\w+ фактор\w* ума'

def tense_seq(s, table):
    pat = '|'.join('(?P<g%d>%s)' % (i, x) for i, (x, _) in enumerate(table))
    seq = []
    for m in re.finditer(pat, s, flags=re.I):
        for i, (_, t) in enumerate(table):
            if m.group('g%d' % i):
                t = t.replace('neg ', '')
                if not seq or seq[-1] != t:
                    seq.append(t)
    return seq

def skelmode():
    d = collections.defaultdict(collections.Counter); first = {}
    bad = 0
    for i, (a, b) in enumerate(zip(p, r), 1):
        if not a.strip() or a.startswith('#'):
            continue
        t1 = tense_seq(a, VERB_P); t2 = tense_seq(b, VERB_R)
        if t1 != t2:
            bad += 1; print('TENSE', i, t1, t2)
        ps = re.split(r'(?<=[.?])\s+', re.sub(r'\s*\^[\w-]+$', '', a))
        rs = re.split(r'(?<=[.?])\s+', re.sub(r'\s*\^[\w-]+$', '', b))
        if len(ps) != len(rs):
            print('SENT', i); continue
        for x, y in zip(ps, rs):
            kx = skel(x, VERB_P, MEM_P); ky = skel(y, VERB_R, MEM_R)
            d[kx][ky] += 1; first.setdefault((kx, ky), i)
    print('tense mismatches', bad)
    for x in sorted(d, key=lambda k: -sum(d[k].values())):
        if len(d[x]) > 1 or True:
            print('P', sum(d[x].values()), x)
            for y, n in d[x].most_common():
                print('   R', n, first[(x, y)], y)

if sys.argv[1] == 'concepts':
    concepts()
else:
    skelmode()
