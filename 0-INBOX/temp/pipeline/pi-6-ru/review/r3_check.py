"""Per-line automated checks: verb tense sequence, negation counts, answers, members."""
import sys, re
P = 'AI_translation/pali/pi-6_split_chapters/'
R = 'AI_translation/russian/pi-6-russian-plain-rails_split_chapters/'
files = sys.argv[1].split(',')
only = sys.argv[2].split(',') if len(sys.argv) > 2 else None

# Pali finite verbs (uppajj / nirujjh) -> tense
PV = re.compile(r"(?<![a-zāīūṃ])(n?uppajj|nirujjh)(at[iī]|ant[iī]|itth[aā]|iṃsu|issat[iī]|issant[iī])")
def ptense(s):
    out = []
    for m in PV.finditer(s):
        lem = 'U' if 'uppajj' in m.group(1) else 'N'
        e = m.group(2)[:-1]
        t = 'P' if e in ('at', 'ant') else 'A' if e in ('itth', 'iṃs') else 'F'
        out.append(lem + t)
    return out
RV = [
    (re.compile(r'возника(?:ет|ют)\b'), 'UP'),
    (re.compile(r'возникал[аои]?\b'), 'UA'),
    (re.compile(r'возникн(?:ет|ут)\b'), 'UF'),
    (re.compile(r'прекраща(?:ется|ются)\b'), 'NP'),
    (re.compile(r'прекращал(?:ся|ась|ось|ись)\b'), 'NA'),
    (re.compile(r'прекрат(?:ится|ятся)\b'), 'NF'),
]
def rtense(s):
    hits = []
    for rx, t in RV:
        for m in rx.finditer(s):
            hits.append((m.start(), t))
    return [t for _, t in sorted(hits)]

def pneg(s):
    s2 = re.sub(r'\[[^\]]*\]', '', s)
    s2 = re.sub(r'\?\s*No\.', '?', s2)
    n = len(re.findall(r"\b(?:na|no|neva|nuppajj\w*)\b", s2, re.I))
    n += len(re.findall(r"\bnuppajj", s2))  # nuppajjati counted once more? no
    return n
def rneg(s):
    s2 = re.sub(r'\[[^\]]*\]', '', s)
    s2 = re.sub(r'\?\s*Нет\.', '?', s2)
    return len(re.findall(r'(?<![а-яё])(?:не|ни|нет)(?![а-яё])', s2, re.I))

def ans(s, kind):
    if kind == 'P':
        return re.findall(r'Āmantā|\bNo\b\.|Natthi', s)
    return re.findall(r'Да\b|Нет\.|Такого нет', s)

for f in files:
    pl = open(P + f, encoding='utf-8').read().split('\n')
    rl = open(R + f, encoding='utf-8').read().split('\n')
    for i, (p, r) in enumerate(zip(pl, rl), 1):
        if not p.strip() or p.startswith('#'):
            continue
        probs = []
        pt, rt = ptense(re.sub(r'\[[^\]]*\]', '', p)), rtense(re.sub(r'\[[^\]]*\]', '', r))
        import itertools
        cp=[k for k,_ in itertools.groupby(pt)]; cr=[k for k,_ in itertools.groupby(rt)]
        if (not only or 'T' in only) and cp != cr:
            probs.append(f'TENSE P={"".join(pt)} R={"".join(rt)}')
        a1 = ['Y' if x == 'Āmantā' else 'N' if x.startswith('No') else 'X' for x in ans(p, 'P')]
        a2 = ['Y' if x == 'Да' else 'N' if x.startswith('Нет') else 'X' for x in ans(r, 'R')]
        if (not only or 'A' in only) and a1 != a2:
            probs.append(f'ANS {a1} {a2}')
        if probs:
            print(f'{f}:{i} ' + ' | '.join(probs))
            if not only or 'v' in only:
                print('  P', p[:400]); print('  R', r[:400])
