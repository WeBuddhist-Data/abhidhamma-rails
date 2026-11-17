import re, os
BASE = r'D:\Work\OpenPecha\abhidhamma-rails'
P = os.path.join(BASE, r'AI_translation\pali\pi-2_split_chapters')
R = os.path.join(BASE, r'AI_translation\russian\pi-2-russian-plain-rails_split_chapters')
FILES = ['13-appamannavibhango.md', '14-sikkhapadavibhango.md', '15-patisambhidavibhango.md', '16-nanavibhango.md']
NUMW = {'catasso': 'четыр', 'tisso': 'три', 'dve': 'два', 'pañca': 'пят', 'cattāri': 'четыр', 'dasa': 'десят', 'aṭṭha': 'восем', 'nava': 'девят', 'satta': 'сем'}
for fn in FILES:
    pl = open(os.path.join(P, fn), encoding='utf-8').read().split('\n')
    rl = open(os.path.join(R, fn), encoding='utf-8').read().split('\n')
    for i, (a, b) in enumerate(zip(pl, rl), 1):
        a2 = re.sub(r'\[[^\]]*\]', '', a); b2 = re.sub(r'\[[^\]]*\]', '', b)
        s = len(re.findall(r'\bsiyā\b', a2, re.I)); n = len(re.findall(r'\bиногда\b', b2, re.I))
        if s != n:
            print(fn[:2], i, 'siya', s, 'иногда', n)
        # ordinals
        for pw, rw in [('paṭham', 'перв'), ('dutiy', 'втор'), ('tatiy', 'трет'), ('catutth', 'четвёрт'), ('pañcam', 'пят'), ('chaṭṭh', 'шест'), ('sattam', 'седьм'), ('aṭṭham', 'восьм')]:
            ca = len(re.findall(pw, a2, re.I)); cb = len(re.findall(rw, b2, re.I))
            if ca != cb and ca:
                print(fn[:2], i, 'ordinal', pw, ca, rw, cb)
        # kusala/akusala
        ka = len(re.findall(r'(?<![a-zā])kusal', a2, re.I)); aka = len(re.findall(r'akusal', a2, re.I))
        kb = len(re.findall(r'(?<![а-яё])благ', b2, re.I)); akb = len(re.findall(r'неблаг', b2, re.I))
        if ka != kb or aka != akb:
            print(fn[:2], i, 'kusala', ka, kb, 'akusala', aka, akb)
        sa = len(re.findall(r'sampayutt', a2)); va = len(re.findall(r'vippayutt', a2))
        nv = len(re.findall(r'не связан', b2))
        if va != nv:
            print(fn[:2], i, 'vippayutta', va, 'не связан', nv)
