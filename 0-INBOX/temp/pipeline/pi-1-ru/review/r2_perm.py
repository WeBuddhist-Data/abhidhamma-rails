import re
base = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation'
files = ['2-03-cittuppadakandam.md', '2-04-cittuppadakandam.md', '2-05-cittuppadakandam.md']
P_PAT = [('dukkhapaṭipad', 'D'), ('sukhapaṭipad', 'S'), ('dandhābhiññ', 'd'), ('khippābhiññ', 'k'),
         ('suññat', 'E'), ('animitt', 'N'), ('appaṇihit', 'A'), ('chandādhipatey', 'c'), ('vīriyādhipatey', 'v'),
         ('cittādhipatey', 'm'), ('vīmaṃsādhipatey', 'i'), ('kusalaṃ…', 'K'), ('vipāko', 'V'),
         ('somanassasahagat', '+'), ('upekkhāsahagat', '0'), ('domanassasahagat', '-'), ('sukhasahagat', 'b+'), ('dukkhasahagat', 'b-'),
         ('ñāṇasampayutt', 'J'), ('ñāṇavippayutt', 'j'), ('diṭṭhigatasampayutt', 'W'), ('diṭṭhigatavippayutt', 'w'), ('sasaṅkhārena', 's'),
         ('akusal', 'U'), ('kusal', 'G'), ('abyākat', 'X')]
R_PAT = [('трудным способом', 'D'), ('лёгким способом', 'S'), ('медленным высшим', 'd'), ('быстрым высшим', 'k'),
         ('пустое', 'E'), ('пустот', 'E'), ('не имеющее признаков', 'N'), ('свобод\\w+ от устремлений', 'A'), ('преобладанием желания', 'c'),
         ('преобладанием усердия', 'v'), ('преобладанием ума', 'm'), ('преобладанием пытливости', 'i'), ('\\(благой ум\\)', 'K'), ('\\(результат действий\\)', 'V'),
         ('сопровождаем\\w+ радостью', '+'), ('сопровождаем\\w+ невозмутимостью', '0'), ('сопровождаем\\w+ унынием', '-'), ('сопровождаем\\w+ счастьем', 'b+'), ('сопровождаем\\w+ болью', 'b-'),
         ('(?<!не )связанн\\w+ со знанием', 'J'), ('не связанн\\w+ со знанием', 'j'), ('(?<!не )связанн\\w+ с приверженностью', 'W'), ('не связанн\\w+ с приверженностью', 'w'), ('с побуждением', 's'),
         ('неблаг', 'U'), ('(?<!не)благ', 'G'), ('неопределённ', 'X')]
def seq(s, pats):
    hits = []
    for pat, code in pats:
        for m in re.finditer(pat, s):
            hits.append((m.start(), code))
    hits.sort()
    # drop overlapping (kusal inside akusal)
    out, last = [], -10
    for pos, code in hits:
        if pos <= last + 1 and code in ('G',):
            continue
        out.append(code); last = pos
    return out
for f in files:
    P = open(base + r'\pali\pi-1_split_chapters\\' + f, encoding='utf-8').read().split('\n')
    R = open(base + r'\russian\pi-1-russian-plain-rails_split_chapters\\' + f, encoding='utf-8').read().split('\n')
    for i, (p, r) in enumerate(zip(P, R)):
        if not p.strip():
            continue
        p2 = re.sub(r'akusal', 'Ū', p)
        sp = seq(p2.replace('Ū', 'akusal'), P_PAT)
        sp = [c for c in sp]
        # fix: 'kusal' also matches inside 'akusal'; remove a G immediately following U at same word
        q = []
        for c in sp:
            q.append(c)
        sr = seq(r, R_PAT)
        a = ''.join(x for x in sp if x not in 'GUX')
        b = ''.join(x for x in sr if x not in 'GUX')
        if a != b:
            idm = re.search(r'\^([\w-]+)', p)
            print(f[:4], i + 1, idm.group(1) if idm else '', a, '|', b)
