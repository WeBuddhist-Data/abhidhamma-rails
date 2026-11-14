import re
base = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation'
files = ['2-03-cittuppadakandam.md', '2-04-cittuppadakandam.md', '2-05-cittuppadakandam.md']
for f in files:
    P = open(base + r'\pali\pi-1_split_chapters\\' + f, encoding='utf-8').read().split('\n')
    R = open(base + r'\russian\pi-1-russian-plain-rails_split_chapters\\' + f, encoding='utf-8').read().split('\n')
    for p, r in zip(P, R):
        idm = re.search(r'\^([\w-]+)\s*$', p)
        sid = idm.group(1) if idm else '?'
        # hoti/honti enumerations vs есть
        hp = len(re.findall(r'\bhon?ti\b', p)) - len(re.findall(r'\bhoti\?', p))
        # remove the 'hoti' in 'X hoti.' closing "– ayaṃ tasmiṃ samaye X hoti" and "uppannaṃ hoti"
        hp -= len(re.findall(r'samaye \S+ hoti\b', p)) - len(re.findall(r'^Katam\S+ tasmiṃ samaye \S+ hoti\?', p))
        hp -= len(re.findall(r'uppann\S+ hoti', p))
        er = len(re.findall(r'\bесть\b', r))
        if hp != er:
            print(sid, 'hoti', hp, 'есть', er)
        # Saṅkhārakkhandha list: tokens before ';' vs commas
        m = re.match(r'Katamo tasmiṃ samaye saṅkhārakkhandho hoti\? (.*?);', p)
        if m:
            np_ = len(m.group(1).split())
            mr = re.match(r'Что такое совокупность формирующих факторов в это время\? (.*?);', r)
            nr = len(mr.group(1).split(',')) if mr else -1
            print(sid, 'sankhara list', np_, nr)
        # definitions: Yo/Ya/Yam tasmim samaye ... –
        m = re.search(r'\? (?:Yo|Yā|Yaṃ) tasmiṃ samaye (.*?) – ', p)
        mr = re.search(r'То, что в это время есть (.*?), – это', r)
        if m and mr:
            toks = m.group(1).split()
            # merge known two-word items
            s = ' '.join(toks)
            for two in ['cittassa ṭhiti', 'anattamanatā cittassa', 'thambhitattaṃ cittassa', 'cittassa uddhaccaṃ', 'cetaso vikkhepo', 'bhantattaṃ cittassa',
                        'cetaso abhiniropanā', 'cittassa anusandhānatā', 'attamanatā cittassa', 'lobho akusalamūlaṃ', 'moho akusalamūlaṃ', 'alobho kusalamūlaṃ', 'adoso kusalamūlaṃ',
                        'cetasiko vīriyārambho', 'cetasikaṃ sātaṃ', 'cetasikaṃ sukhaṃ', 'cetasikaṃ asātaṃ', 'cetasikaṃ dukkhaṃ', 'kāyikaṃ sātaṃ', 'kāyikaṃ sukhaṃ', 'kāyikaṃ asātaṃ', 'kāyikaṃ dukkhaṃ']:
                s = s.replace(two, two.replace(' ', '_'))
            n1 = len(s.split())
            n2 = len(mr.group(1).split(','))
            if n1 != n2:
                print(sid, 'def items', n1, n2, '|', s[:120])
