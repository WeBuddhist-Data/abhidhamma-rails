import re
P = 'D:\\Work\\OpenPecha\\abhidhamma-rails\\AI_translation\\pali\\pi-2_split_chapters\\'
R = 'D:\\Work\\OpenPecha\\abhidhamma-rails\\AI_translation\\russian\\pi-2-russian-plain-rails_split_chapters\\'
ch = '6-paticcasamuppadavibhango.md'
instr = {'avijjā': 'неведением', 'saṅkhāra': 'формирующим фактором', 'viññāṇa': 'сознанием', 'nāmarūpa': 'умственным и материальной формой',
         'nāma': 'умственным', 'chaṭṭhāyatana': 'шестой сферой восприятия', 'saḷāyatana': 'шестью сферами восприятия', 'phassa': 'контактом',
         'vedanā': 'чувством', 'taṇhā': 'жаждой', 'upādāna': 'цеплянием', 'bhava': 'существованием', 'jāti': 'рождением',
         'adhimokkha': 'решимостью', 'pasāda': 'ясной верой', 'paṭigha': 'неприязнью', 'vicikicchā': 'колебанием', 'uddhacca': 'беспокойством',
         'kusalamūla': 'благими корнями', 'akusalamūla': 'неблагими корнями'}
nom = {'saṅkhāro': 'формирующий фактор', 'saṅkhārā': 'формирующие факторы', 'viññāṇaṃ': 'сознание', 'nāmarūpaṃ': 'умственное и материальная форма',
       'nāmaṃ': 'умственное', 'chaṭṭhāyatanaṃ': 'шестая сфера восприятия', 'saḷāyatanaṃ': 'шесть сфер восприятия', 'phasso': 'контакт',
       'vedanā': 'чувство', 'taṇhā': 'жажда', 'upādānaṃ': 'цепляние', 'bhavo': 'существование', 'jāti': 'рождение', 'jarāmaraṇaṃ': 'старение и смерть',
       'avijjā': 'неведение', 'adhimokkho': 'решимость', 'pasādo': 'ясная вера', 'paṭighaṃ': 'неприязнь', 'vicikicchā': 'колебание', 'uddhaccaṃ': 'беспокойство'}
pl = [l for l in open(P + ch, encoding='utf-8').read().split('\n') if l.strip()]
rl = [l for l in open(R + ch, encoding='utf-8').read().split('\n') if l.strip()]
n = 0
for i, (p, r) in enumerate(zip(pl, rl)):
    if 'Tattha' in p[:8] or p.startswith('#'):
        continue
    pp = re.findall(r'(\w+?)paccayā(?:pi)? (\w+)', p)
    if not pp: continue
    exp = []
    for c, res in pp:
        c = c[0].lower() + c[1:]
        if c not in instr or res not in nom:
            continue
        exp.append((instr[c], nom[res]))
    got = []
    for cl in re.split(r'[,;.:]', r):
        m = re.search(r'(?:^|\s)((?:[а-яё]+ ){0,3}?(?:неведением|формирующим фактором|формирующими факторами|сознанием|умственным и материальной формой|умственным|шестой сферой восприятия|шестью сферами восприятия|контактом|чувством|жаждой|цеплянием|существованием|рождением|решимостью|ясной верой|неприязнью|колебанием|беспокойством|неблагими корнями|благими корнями)) (?:тоже )?обусловлен[аоы]? (?:и возникают )?(.+)$', cl.strip())
        if m:
            cond = m.group(1)
            for k in ['а ', 'в это время ', 'время ']:
                if cond.startswith(k): cond = cond[len(k):]
            cond = cond.replace('это ', '')
            res = m.group(2).strip()
            got.append((cond.strip(), res))
    # compare
    ok = len(exp) == len(got)
    if ok:
        for (a, b), (c, d) in zip(exp, got):
            if not c.endswith(a) or not (d == b or d.startswith(b)):
                ok = False
    n += 1
    if not ok:
        print(i, 'EXP', exp); print(i, 'GOT', got); print()
print('chain lines checked', n)
