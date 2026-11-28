import re
BASE = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation'
FILES = ['6-02-sankharayamaka.md', '7-01-anusayayamaka.md', '7-02-anusayayamaka.md',
         '7-03-anusayayamaka.md', '7-04-anusayayamaka.md', '7-05-anusayayamaka.md']
LAB = {'Ka': 'а', 'Kha': 'б', 'Ga': 'в', 'Gha': 'г', 'Ṅa': 'д', 'Ca': 'е'}
ANS = {'Āmantā': 'Да', 'No': 'Нет', 'Natthi': 'Такого нет'}
n = 0
for f in FILES:
    p = open(BASE + '\\pali\\pi-6_split_chapters\\' + f, encoding='utf-8').read().split('\n')
    r = open(BASE + '\\russian\\pi-6-russian-plain-rails_split_chapters\\' + f, encoding='utf-8').read().split('\n')
    for i, (a, b) in enumerate(zip(p, r), 1):
        a2 = a.lstrip('# '); b2 = b.lstrip('# ')
        m = re.match(r'\((\w+)\)', a2)
        if m and m.group(1) in LAB:
            if not b2.startswith('(' + LAB[m.group(1)] + ')'):
                n += 1; print(f, i, 'LABEL', a2[:20], b2[:20])
            a2 = a2[m.end():].strip(); b2 = re.sub(r'^\(\w\)\s*', '', b2)
        vp = bool(re.match(r'(?i)(yassa|yo|yattha|yato) vā pana', a2))
        if vp != b2.startswith('А '):
            n += 1; print(f, i, 'VAPANA', a2[:40], '|', b2[:40])
        # answers after '?'
        pa = re.findall(r'\?\s*(Āmantā|No|Natthi)\b', a)
        ra = re.findall(r'\?\s*(Да|Нет|Такого нет)\b', b)
        if [ANS[x] for x in pa] != ra:
            n += 1; print(f, i, 'ANSWER', pa, ra)
print('issues', n)
