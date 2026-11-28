import sys, re
P = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation\pali\pi-6_split_chapters\\'
R = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation\russian\pi-6-russian-plain-rails_split_chapters\\'
ch = sys.argv[1]
pl = open(P + ch, encoding='utf-8').read().split('\n')
rl = open(R + ch, encoding='utf-8').read().split('\n')
# (pali regex, russian regex)
T = [
    (r'\bsacakkhuk', r'с глазом'), (r'\bacakkhuk', r'без глаза'),
    (r'\bsasotak', r'с ухом'), (r'\basotak', r'без уха'),
    (r'\bsaghānak', r'с носом'), (r'\baghānak', r'без носа'),
    (r'\bna itthīnaṃ', r'не женщиной'), (r'(?<!na )\bitthīnaṃ', r'(?<!не )женщиной'),
    (r'\bna purisānaṃ', r'не мужчиной'), (r'(?<!na )\bpurisānaṃ', r'(?<!не )мужчиной'),
    (r'\bvinā somanassena', r'без радости'), (r'(?<!vinā )\bsomanassena', r'(?<!связанного )с радостью'),
    (r'\bvinā upekkhāya', r'без невозмутимости'), (r'(?<!vinā )\bupekkhāya', r'(?<!связанного )с невозмутимостью'),
    (r'\bsahetuk', r'с корнями'), (r'\bahetuk', r'без корней'),
    (r'\bñāṇasampayuttānaṃ', r'(?<!связанного )со знанием'), (r'\bñāṇavippayuttānaṃ', r'без знания'),
    (r'\bsacittak', r'с умом'), (r'\bacittak', r'без ума'),
    (r'upapajjant', r'перерожда'), (r'cavant', r'умира'), (r'\buppajjantīnaṃ', r'XXX'),
    (r'sabbesaṃ', r'(?i)у всех'),
    (r'pavatte', r'(?i)в течение жизни'), (r'bhaṅgakkhaṇe', r'момент распада'), (r'uppādakkhaṇe', r'момент возникновения'),
    (r'nirodhasamāpann', r'достижение прекращения'), (r'asaññasatt', r'существ\w* без восприятия'),
    (r'(?<!ū)arūp', r'мир\w* без форм'), (r'rūpāvacar', r'мир\w* форм(?! )|мир\w* форм[.,? ]'), (r'kāmāvacar', r'чувственных желаний'),
    (r'pañcavokār', r'пяти'), (r'catuvokār', r'четыр'),
    (r'sampayutta(?=\w*cittassa)', r'(?<!не )связанного'),
    (r'vippayutta(?=\w*cittassa)', r'не связанного'),
    (r'āmantā', r'Да[.…]'), (r'\bno\.', r'Нет\.'), (r'natthi', r'Такого нет'),
    (r'yattha', r'(?i)где'), (r'\byassa\b', r'(?i)у кого'),
    (r'\bvā pana\b', r'(?i)\bа '),
]
bad = 0
for i, (a, b) in enumerate(zip(pl, rl)):
    if not a.strip() or a.startswith('#') or 'uppajj' not in a:
        continue
    al = a.lower()
    diffs = []
    for pr, rr in T:
        ca = len(re.findall(pr, al))
        cb = len(re.findall(rr, b))
        if pr == r'(?<!ū)arūp':
            ca = len(re.findall(r'(?<![ūr])arūp', al))
        if pr == r'rūpāvacar':
            ca = len(re.findall(r'(?<!a)rūpāvacar', al))
        if ca != cb:
            diffs.append((pr, ca, cb))
    if diffs:
        bad += 1
        print(i + 1, diffs)
        if len(sys.argv) > 2:
            print('  P:', a); print('  R:', b)
print('flagged', bad)
