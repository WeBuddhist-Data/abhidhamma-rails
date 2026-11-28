"""Compare effective (tense, polarity) of finite verbs per line, Pali vs Russian.
Pali: neg if preceded by 'na' or form nuppajj-; flipped if the clause begins with 'no ca'.
Russian: neg if preceded by 'не'."""
import sys, re, itertools
P = 'AI_translation/pali/pi-6_split_chapters/'
R = 'AI_translation/russian/pi-6-russian-plain-rails_split_chapters/'
files = sys.argv[1].split(',')
verbose = len(sys.argv) > 2
PV = re.compile(r"(?<![a-zāīūṃ])(n?uppajj|nirujjh|n?anuset|pajah|parijān|bhāve|sacchikaro)(at[iī]|ant[iī]|itth[aā]|iṃsu|issat[iī]|issant[iī]|i)?", re.I)
def pal(s):
    s = re.sub(r'\[[^\]]*\]', '', s)
    out = []
    for m in PV.finditer(s):
        if m.group(2) is None and not m.group(1).startswith(('pajah', 'parij')):
            pass
        e = (m.group(2) or 'at')[:-1] if m.group(2) else 'at'
        t = 'P' if e in ('at', 'ant', '') else 'A' if e in ('itth', 'iṃs') else 'F'
        pre = s[:m.start()]
        neg = m.group(1).lower().startswith('n') and not m.group(1).lower().startswith('nirujjh')
        if re.search(r'\bna\s*$', pre):
            neg = True
        clause = re.split(r'[,.?;]', pre)[-1]
        if re.match(r'\s*no ca\b', clause):
            neg = not neg
        out.append(t + ('-' if neg else '+'))
    return out
RV = [
    (r'возника(?:ет|ют)', 'P'), (r'возникал[аои]?', 'A'), (r'возникн(?:ет|ут)', 'F'),
    (r'прекраща(?:ется|ются)', 'P'), (r'прекращал(?:ся|ась|ось|ись)', 'A'), (r'прекрат(?:ится|ятся)', 'F'),
]
RX = re.compile('(?<![а-яё])(' + '|'.join(r for r, _ in RV) + ')(?![а-яё])')
def rus(s):
    s = re.sub(r'\[[^\]]*\]', '', s)
    out = []
    for m in RX.finditer(s):
        w = m.group(1)
        t = next(t for r, t in RV if re.fullmatch(r, w))
        neg = bool(re.search(r'(?<![а-яё])не\s+$', s[:m.start()]))
        out.append(t + ('-' if neg else '+'))
    return out
n = 0
for f in files:
    pl = open(P + f, encoding='utf-8').read().split('\n')
    rl = open(R + f, encoding='utf-8').read().split('\n')
    for i, (p, r) in enumerate(zip(pl, rl), 1):
        if not p.strip() or p.startswith('#'):
            continue
        a = [k for k, _ in itertools.groupby(pal(p))]
        b = [k for k, _ in itertools.groupby(rus(r))]
        if a != b:
            n += 1
            print(f'{f}:{i} P={" ".join(a)} R={" ".join(b)}')
            if verbose:
                print('  P', p); print('  R', r)
print('mismatches', n)
