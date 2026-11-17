import sys, re
sys.path.insert(0, r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-ru\review')
from r1_align import load

NUM = [('ekavidhena', 'по одному'), ('duvidhena', 'на два вида'), ('tividhena', 'на три вида'),
       ('catubbidhena', 'на четыре вида'), ('pañcavidhena', 'на пять видов'), ('chabbidhena', 'на шесть видов'),
       ('sattavidhena', 'на семь видов'), ('aṭṭhavidhena', 'на восемь видов'), ('navavidhena', 'на девять видов'),
       ('dasavidhena', 'на десять видов'), ('ekādasavidhena', 'на одиннадцать видов'),
       ('catuvīsatividhena', 'на двадцать четыре вида'), ('tiṃsavidhena', 'на тридцать видов'),
       ('tiṃsatividhena', 'на тридцать видов'), ('bahuvidhena', 'на многие виды')]
# count words
CW = {'eka': 'одн', 'dve': 'дв', 'tayo': 'тр', 'tīṇi': 'тр', 'cattāro': 'четыр', 'cattāri': 'четыр', 'pañca': 'пят',
      'cha': 'шест', 'satta': 'сем', 'aṭṭha': 'восем', 'nava': 'девят', 'dasa': 'десят', 'ekādasa': 'одиннадцат',
      'dvādasa': 'двенадцат', 'soḷasa': 'шестнадцат', 'aṭṭhārasa': 'восемнадцат', 'sattarasa': 'семнадцат',
      'ekaṃ': 'одн', 'dvādasāyatanāni': 'двенадцат', 'aṭṭhārasa': 'восемнадцат'}
for ch in sys.argv[1:]:
    p, r, pt, rt = load(ch)
    for (pid, pl), (rid, rl) in zip(p, r):
        for a, b in zip(pl, rl):
            al = a.lower()
            bl = b.lower()
            for pw, rw in NUM:
                ca = len(re.findall(r'\b' + pw + r'\b', al))
                cb = bl.count(rw)
                if pw == 'tiṃsavidhena' or pw == 'tiṃsatividhena':
                    continue
                if ca != cb and not (pw == 'ekavidhena'):
                    print('NUM', pid, pw, ca, cb)
            # cardinal words
            for pw, rw in CW.items():
                ca = len(re.findall(r'(?<![\wāīūṃṅñṭḍṇḷ])' + pw + r'(?![\wāīūṃṅñṭḍṇḷ])', al))
                cb = len(re.findall(r'(?<!\w)' + rw + r'\w*', bl))
                if ca and ca > cb:
                    print('CARD', pid, pw, ca, rw, cb)
