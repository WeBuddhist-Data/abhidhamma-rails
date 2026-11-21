import os, re
VI = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation\vietnamese\pi-5-vietnamese-plain-rails_split_chapters'
FILES = ['23-pannarasamavaggo', '24-solasamavaggo', '25-sattarasamavaggo', '26-attharasamavaggo',
         '27-ekunavisatimavaggo', '28-visatimavaggo', '29-ekavisatimavaggo', '30-bavisatimavaggo',
         '31-tevisatimavaggo']
pat = re.compile(r'\S*[āīūṃṅñṭḍṇḷ]\S*')
for f in FILES:
    for n, l in enumerate(open(os.path.join(VI, f + '.md'), encoding='utf-8'), 1):
        s = re.sub(r'\[[^\]]*\]', '', l)
        hits = pat.findall(s)
        if hits:
            print(f, n, hits[:6])
        for q in ['  ', ' ,', ' .', '..', '“ ', ' ”']:
            if q in l.rstrip('\n'):
                print(f, n, 'spacing', repr(q))
