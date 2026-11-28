import sys, re
P = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation\pali\pi-6_split_chapters\\'
R = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation\russian\pi-6-russian-plain-rails_split_chapters\\'
ch = sys.argv[1]
pl = open(P + ch, encoding='utf-8').read().split('\n')
rl = open(R + ch, encoding='utf-8').read().split('\n')

PITEMS = [('anaññātaññassāmīt', 'познания непознанного'), ('aññātāv', 'обладателя окончательного знания'),
          ('aññ', 'окончательного знания'), ('cakkhu', 'глаза'), ('cakkh', 'глаза'), ('sot', 'уха'), ('ghān', 'носа'),
          ('jivh', 'языка'), ('kāy', 'тела'), ('man', 'ума'), ('itth', 'женственности'), ('puris', 'мужественности'),
          ('jīvit', 'жизненная'), ('sukh', 'удовольствия'), ('dukkh', 'боли'), ('somanass', 'радости'),
          ('domanass', 'уныния'), ('upekkh', 'невозмутимости'), ('saddh', 'веры'), ('vīriy', 'усердия'),
          ('sat', 'осознанности'), ('samādh', 'сосредоточения'), ('paññ', 'мудрости')]

def pitem(stem):
    for k, v in PITEMS:
        if stem == k:
            return v
    return '?' + stem

def pali_seq(s):
    out = []
    for m in re.finditer(r'(no ca \w+ (?:tattha )?)?(\w+?)(?:ndriya|indriya)(?:ṃ|ñca|ñceva|nti)?\s+(?:…pe…\s*)?(na uppajjat|nuppajjat|uppajjat)', s):
        neg = m.group(3) != 'uppajjat'
        if m.group(1):
            neg = not neg
        out.append((pitem(m.group(2)), neg))
    return out

RNAMES = 'обладателя окончательного знания|окончательного знания|познания непознанного|глаза|уха|носа|языка|тела|ума|женственности|мужественности|удовольствия|боли|радости|уныния|невозмутимости|веры|усердия|осознанности|сосредоточения|мудрости'
RITEM = re.compile(r'способность (' + RNAMES + r')|(жизненная) способность')

def rus_seq(s):
    out = []
    prev = 0
    lastneg = None
    for m in RITEM.finditer(s):
        name = m.group(1) or m.group(2)
        ctx = s[prev:m.start()]
        # context since previous item
        if re.search(r'не возникает', ctx):
            neg = True
        elif re.search(r'(^|[\s,])ни $', ctx) or ctx.endswith('ни '):
            neg = True
        elif 'возникает' in ctx:
            neg = False
        else:
            neg = None
        prev = m.end()
        if neg is None:
            continue  # item not tied to verb (e.g. '…')
        out.append((name, neg))
    return out

bad = 0
n = 0
for i, (a, b) in enumerate(zip(pl, rl)):
    if not a.strip() or a.startswith('#'):
        continue
    n += 1
    ps = pali_seq(a)
    rs = rus_seq(b)
    flag = ps != rs
    for w in ['возникал', 'возникнет', 'прекра']:
        if w in b:
            flag = True
    if ('upapajj' in a) != ('перерожда' in b):
        flag = True
    if ('cavant' in a) != ('умира' in b):
        flag = True
    if flag:
        bad += 1
        print(i + 1, ps)
        print(i + 1, rs)
        print('  P:', a[:400])
        print('  R:', b[:400])
print('lines', n, 'flagged', bad)
