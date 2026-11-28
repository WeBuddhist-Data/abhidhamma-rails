"""r5: sentence templates (members/planes/persons masked), Pāli template -> Russian variants."""
import re, sys, collections
P = 'AI_translation/pali/pi-6_split_chapters/'
R = 'AI_translation/russian/pi-6-russian-plain-rails_split_chapters/'
FILES = sys.argv[1].split(',')
mode = sys.argv[2] if len(sys.argv) > 2 else 'multi'

def pmask(s):
    s = re.sub(r'\^[\w-]+', '', s)
    s = re.sub(r'(kāmarāg|paṭigh|mān|diṭṭh|vicikicch|bhavarāg|avijj)ānusay(\w*)', r'M\2', s, flags=re.I)
    s = re.sub(r'(?:\bna\s+)?(?:arūpadhātu|rūpadhātu|kāmadhātu)\w*|dukkhāya vedanāya|dvīsu vedanāsu|tīsu vedanāsu|apariyāpanne', 'L', s, flags=re.I)
    s = re.sub(r'L(?:\s+L)+', 'L', s)
    s = re.sub(r'\b(?:Aggamaggasamaṅg|Anāgāmimaggasamaṅg|Aṭṭhamak|Anāgāmi|Arah|Puthujjan)\w*', 'PER', s, flags=re.I)
    s = re.sub(r'\b(?:Dvinnaṃ|Tiṇṇaṃ|Catunnaṃ|Pañcannaṃ)\b', 'N', s, flags=re.I)
    s = re.sub(r'M(\w*)(?:\s+(?:ca\s+)?M\1)+', r'M\1+', s)
    s = re.sub(r'Mo ca(?:\s+Mo ca)+', 'Mo ca+', s)
    return s.strip()
RMEM = r'(?:к страсти к существованию|к чувственной страсти|к неприязни|к самомнению|к воззрениям|к колебанию|к неведению)'
def rmask(s):
    s = re.sub(r'\^[\w-]+', '', s)
    s = re.sub(RMEM, 'M', s)
    s = re.sub(r'M(?:(?:, | и |, ни |, и )M)+', 'M+', s)
    s = re.sub(r'(?:(?:не )?(?:в|из|во) )?мир\w* (?:без форм|форм|чувственных желаний)|(?:в )?болезненном чувстве|(?:в )?(?:двух|трёх) видах чувства|(?:в )?том, что не принадлежит к кругам существования', 'L', s)
    s = re.sub(r'L(?:(?:, | и |, и )L)+', 'L', s)
    s = re.sub(r'L L', 'L', s)
    s = re.sub(r'(?:Обладающ\w+|обладающ\w+) (?:высшим путём|путём невозвращения)|[Лл]ичност\w+ восьмой ступени|невозвращающ\w+|архат\w*|обычн\w+ человек\w*', 'PER', s)
    s = re.sub(r'(?<![а-яё])(?:двух|трёх|четырёх|пяти)(?![а-яё])', 'N', s, flags=re.I)
    return s.strip()

def sents(s, lang):
    parts = re.split(r'(?<=[.?;])\s+', s)
    return [x for x in parts if x.strip()]

m = collections.defaultdict(collections.Counter)
where = collections.defaultdict(list)
mis = 0
for f in FILES:
    pl = open(P + f + '.md', encoding='utf-8').read().split('\n')
    rl = open(R + f + '.md', encoding='utf-8').read().split('\n')
    for i, (p, r) in enumerate(zip(pl, rl), 1):
        if not p.strip() or p.startswith('#'): continue
        ps, rs = sents(p, 'p'), sents(r, 'r')
        if len(ps) != len(rs):
            mis += 1
            ps, rs = [p], [r]
        for a, b in zip(ps, rs):
            ta, tb = pmask(a), rmask(b)
            m[ta][tb] += 1
            where[(ta, tb)].append('%s:%d' % (f[:4], i))
print('sentence-count mismatches', mis, 'pali templates', len(m))
for ta, c in sorted(m.items(), key=lambda x: -sum(x[1].values())):
    if mode == 'multi' and len(c) < 2: continue
    print('P:', ta[:300])
    for tb, n in c.most_common():
        print('   %4d R: %s   [%s]' % (n, tb[:400], ' '.join(where[(ta, tb)][:4])))
