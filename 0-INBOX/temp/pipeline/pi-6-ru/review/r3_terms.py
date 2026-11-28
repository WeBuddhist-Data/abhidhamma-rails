"""Count person/plane/moment terms per line, Pali vs Russian; print mismatches."""
import sys, re
from collections import Counter
P = 'AI_translation/pali/pi-6_split_chapters/'
R = 'AI_translation/russian/pi-6-russian-plain-rails_split_chapters/'
files = sys.argv[1].split(',')
show = sys.argv[2].split(',') if len(sys.argv) > 2 else None
T = [
    ('asañña', r'asaññasatt', r'без восприятия'),
    ('arupa', r'arūp', r'без форм'),
    ('rupavac', r'(?<!a)(?<![a-z])rūpāvacar', r'(?<!без )(?:мир\w*|существ\w*) форм'),
    ('kama', r'kāmāvacar', r'чувственных желаний'),
    ('suddha', r'suddhāvās', r'Чист\w* обител'),
    ('pacchimabh', r'pacchimabhavik', r'в последний раз'),
    ('arahant', r'arahant', r'архат'),
    ('aggamagga', r'aggamagg', r'высш\w+ пут'),
    ('aggaphala', r'aggaphal', r'высш\w+ плод'),
    ('puthujjana', r'puthujjan', r'обычн\w+ люд'),
    ('apaya', r'(?<![a-z])[aā]pāy', r'низш\w+ мир'),
    ('nirodhasam', r'nirodhasamāpann', r'достижени\w+ прекращения'),
    ('catuvok', r'catuvokār', r'четырьмя составляющими'),
    ('pancavok', r'pañcavokār', r'пятью составляющими'),
    ('upapajjant', r'upapajjant', r'перерожда'),
    ('cavant', r'cavant', r'умира'),
    ('pavatte', r'pavatte', r'в течение жизни'),
    ('uppadakk', r'uppādakkhaṇ', r'момент\w* возникновения'),
    ('bhangakk', r'bhaṅgakkhaṇ', r'момент\w* распада'),
    ('vattamane', r'vattamān', r'присутствует'),
    ('tanhavipp', r'taṇhāvippayutt', r'не связанн\w+ с жаждой'),
    ('maggavipp', r'maggavippayutt', r'не связанн\w+ с путём'),
    ('pacchimacitt', r'pacchimacitt', r'последн\w+ ум'),
    ('upapatticitt', r'upapatticitt', r'ум\w* перерождения'),
    ('dutiyecitte', r'dutiye citte', r'втор\w+ ум'),
    ('abhisamet', r'(?<![a-z])[Aa]bhisametāv', r'(?<!не )постиг'),
    ('anabhisamet', r'[Aa]nabhisametāv', r'не постиг'),
    ('assasa', r'assāsapassās', r'вдох'),
    ('avitakka', r'avitakkaavicār', r'без направленной мысли'),
    ('savitakka', r'savitakkasavicār', r'с направленной мыслью'),
    ('jhana1', r'paṭhamajjhān', r'перв\w+ медитативн|перв\w+(?:,| и) (?:во |в )?втор'),
    ('jhana4', r'catutthajjhān', r'четвёрт'),
    ('patilabh', r'paṭilabhissanti', r'обретут|обретёт'),
    ('itaresam', r'itaresaṃ|avases', r'остальн'),
    ('sabbesam', r'[Ss]abbesaṃ', r'(?<![а-яё])всех'),
    ('anantara', r'anantarā', r'сразу после'),
    ('phala', r'(?<![a-z])phal', r'(?<![а-яё])плод'),
    ('nirodhasamapann_samapannanam', r'(?<![a-z])samāpannānaṃ', r'вошедш'),
]
def cnt(s, rx):
    s = re.sub(r'\[[^\]]*\]', '', s)
    return len(re.findall(rx, s, re.I if rx.startswith('(?<!без') else 0))
tot = Counter()
for f in files:
    pl = open(P + f, encoding='utf-8').read().split('\n')
    rl = open(R + f, encoding='utf-8').read().split('\n')
    for i, (p, r) in enumerate(zip(pl, rl), 1):
        if not p.strip() or p.startswith('#'):
            continue
        bad = []
        for name, pr, rr in T:
            a = len(re.findall(pr, re.sub(r'\[[^\]]*\]', '', p), re.I))
            b = len(re.findall(rr, re.sub(r'\[[^\]]*\]', '', r), re.I))
            if a != b:
                bad.append(f'{name}:{a}/{b}')
                tot[name] += 1
        if bad and (not show or any(b.split(':')[0] in show for b in bad)):
            print(f'{f}:{i} ' + ' '.join(bad))
print(tot)
