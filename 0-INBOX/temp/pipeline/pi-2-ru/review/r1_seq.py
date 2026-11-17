import sys, re
sys.path.insert(0, r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-ru\review')
from r1_align import load
# sequence of sentence subjects: number words / named items, Pali vs Russian
PN = [('ekādasa', 11), ('dvādasa', 12), ('pannarasa', 15), ('soḷasa', 16), ('sattarasa', 17), ('aṭṭhārasa', 18),
      ('dve', 2), ('dv', 2), ('tayo', 3), ('tisso', 3), ('cattāro', 4), ('pañca', 5), ('cha', 6), ('satta', 7),
      ('aṭṭha', 8), ('nava', 9), ('dasa', 10)]
RN = [('Одиннадцать', 11), ('Двенадцать', 12), ('Пятнадцать', 15), ('Шестнадцать', 16), ('Семнадцать', 17),
      ('Восемнадцать', 18), ('Две', 2), ('Два', 2), ('Три', 3), ('Четыре', 4), ('Пять', 5), ('Шесть', 6),
      ('Семь', 7), ('Восемь', 8), ('Девять', 9), ('Десять', 10)]


def pseq(s):
    out = []
    for sent in re.split(r'(?<=[.;])\s+', s):
        w = sent.strip().split(' ')[0].lower()
        hit = False
        for k, v in [('dvādasāyatan', 12), ('ekādasāyatan', 11), ('dasāyatan', 10), ('navāyatan', 9),
                     ('chāyatan', 6), ('pañcāyatan', 5), ('dvāyatan', 2)]:
            if w.startswith(k):
                out.append(v); hit = True; break
        if hit:
            continue
        if w == 'pañcakkhandhā':
            out.append(5); continue
        for k, v in PN:
            if w == k or (w.startswith(k) and w.endswith(('āyatanā', 'āyatanāni', 'dhātuyo'))) :
                out.append(v); break
    return out


def rseq(s):
    out = []
    for sent in re.split(r'(?<=[.;])\s+', s):
        w = sent.strip().split(' ')[0]
        for k, v in RN:
            if w == k:
                out.append(v); break
    return out


for ch in sys.argv[1:]:
    p, r, pt, rt = load(ch)
    for (pid, pl), (rid, rl) in zip(p, r):
        for a, b in zip(pl, rl):
            x, y = pseq(a), rseq(b)
            if x != y:
                print(pid, x, y)
    print(ch, 'done')
