import re
P = 'D:\\Work\\OpenPecha\\abhidhamma-rails\\AI_translation\\pali\\pi-2_split_chapters\\'
R = 'D:\\Work\\OpenPecha\\abhidhamma-rails\\AI_translation\\russian\\pi-2-russian-plain-rails_split_chapters\\'
pnum = [('Ekavīsat', 21), ('Bāvīsat', 22), ('Sattaras', 17), ('Soḷas', 16), ('Pannaras', 15), ('Cuddas', 14), ('Teras', 13), ('Dvādas', 12),
        ('Ekādas', 11), ('Aṭṭhāras', 18), ('Das', 10), ('Nav', 9), ('Aṭṭh', 8), ('Satt', 7), ('Cha ', 6), ('Pañc', 5), ('Cattār', 4), ('Catunn', 4),
        ('Tīṇ', 3), ('Dv', 2), ('Dve ', 2)]
rnum = [('Двадцать одна', 21), ('Двадцать две', 22), ('Двадцати двух', 22), ('Семнадцать', 17), ('Шестнадцать', 16), ('Пятнадцать', 15), ('Четырнадцать', 14),
        ('Тринадцать', 13), ('Двенадцать', 12), ('Одиннадцать', 11), ('Восемнадцать', 18), ('Десять', 10), ('Девять', 9), ('Восемь', 8),
        ('Семь', 7), ('Шесть', 6), ('Пять', 5), ('Четыре', 4), ('четырёх', 4), ('Три', 3), ('Две', 2)]
def pval(s):
    s = s.strip()
    for k, v in pnum:
        if s.startswith(k): return v
    return None
def rval(s):
    s = s.strip()
    for k, v in rnum:
        if s.startswith(k): return v
    return None
for ch in ['4-saccavibhango.md', '5-indriyavibhango.md']:
    pl = [l for l in open(P + ch, encoding='utf-8').read().split('\n') if l.strip()]
    rl = [l for l in open(R + ch, encoding='utf-8').read().split('\n') if l.strip()]
    for i, (p, r) in enumerate(zip(pl, rl)):
        ps = [x for x in re.split(r'(?<=[.?;])\s+', p) if x.strip()]
        rs = [x for x in re.split(r'(?<=[.?;])\s+', r) if x.strip()]
        pv = [pval(x) for x in ps]; rv = [rval(x) for x in rs]
        pv = [x for x in pv if x]; rv = [x for x in rv if x]
        if pv != rv:
            print(ch, i, 'P', pv); print(ch, i, 'R', rv)
        # subject-type check: which sacca / indriya leads each sentence
        if ch.startswith('4'):
            pk = [re.match(r'(Samudaya|Magga|Nirodha|Dukkha)sacc', x.strip()) for x in ps]
            rk = [re.match(r'Истин[ау] о (возникновении|пути|прекращении|страдании)', x.strip()) for x in rs]
            m = {'Samudaya': 'возникновении', 'Magga': 'пути', 'Nirodha': 'прекращении', 'Dukkha': 'страдании'}
            a = [m[x.group(1)] for x in pk if x]; b = [x.group(1) for x in rk if x]
            if a != b: print(ch, i, 'SACCA', a, b)
