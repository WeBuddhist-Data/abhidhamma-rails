import re
BASE = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation'
FILES = ['6-02-sankharayamaka.md', '7-01-anusayayamaka.md', '7-02-anusayayamaka.md',
         '7-03-anusayayamaka.md', '7-04-anusayayamaka.md', '7-05-anusayayamaka.md']
PL = r'(в мире без форм|в мире форм|в мире чувственных желаний|в двух видах чувства|в трёх видах чувства|в болезненном чувстве)'
for f in FILES:
    p = open(BASE + '\\pali\\pi-6_split_chapters\\' + f, encoding='utf-8').read()
    t = open(BASE + '\\russian\\pi-6-russian-plain-rails_split_chapters\\' + f, encoding='utf-8').read()
    if '\r' in t: print(f, 'CR')
    if '\n\n\n' in t: print(f, 'double blank')
    pl, rl = p.split('\n'), t.split('\n')
    for i, (a, l) in enumerate(zip(pl, rl), 1):
        for m in re.finditer(PL + r', (там|не|и) ', l):
            print(f, i, 'COMMA', l[max(0, m.start() - 40):m.end() + 20])
        if re.search(r'\bли\b', l): print(f, i, 'LI')
        if re.search(r'[A-Za-zāīūṃṅñṭḍṇḷ]{3,}', re.sub(r'\^[\w-]+', '', l)): print(f, i, 'LATIN', l[:120])
        if '—' in l: print(f, i, 'EMDASH')
        if '  ' in l: print(f, i, 'DOUBLESPACE')
        if l.strip() and not l.startswith('#'):
            body = re.sub(r'\s*\^[\w-]+$', '', l)
            pb = re.sub(r'\s*\^[\w-]+$', '', a)
            if body[-1] not in '.?…)' and not body.startswith('Почтение'):
                print(f, i, 'END', body[-30:])
            # question/statement count
            if pb.count('?') != body.count('?'):
                print(f, i, 'QCOUNT', pb.count('?'), body.count('?'))
            if pb.count('…pe…') != body.count('…'):
                print(f, i, 'PECOUNT', pb.count('…pe…'), body.count('…'))
            if pb.count('(') != body.count('('):
                print(f, i, 'PAREN', pb.count('('), body.count('('))
