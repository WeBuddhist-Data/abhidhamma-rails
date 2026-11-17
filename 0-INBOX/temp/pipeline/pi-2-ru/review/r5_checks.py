import re
R = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation\russian\pi-2-russian-plain-rails_split_chapters\17-khuddakavatthuvibhango.md'
P = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation\pali\pi-2_split_chapters\17-khuddakavatthuvibhango.md'
rt = open(R, encoding='utf-8').read()
pt = open(P, encoding='utf-8').read()
rl = [l for l in rt.split('\n') if l.strip()]
pl = [l for l in pt.split('\n') if l.strip()]

def bid(l):
    m = re.search(r'\^([0-9A-Za-z-]+)\s*$', l)
    return m.group(1) if m else ''

print('em dash count', rt.count('—'), 'double blank', rt.count('\n\n\n'), 'CR', rt.count('\r'))
for i, l in enumerate(rl):
    body = re.sub(r'\[[^\]]*\]', '', l)
    body = re.sub(r'\^[0-9A-Za-z-]+\s*$', '', body)
    lat = re.findall(r'[A-Za-zĀāĪīŪūṄṅÑñṬṭḌḍṆṇḶḷṂṃ]{2,}', body)
    if lat:
        print('LATIN', i, lat[:5])
    if re.search(r'\bли\b', l):
        print('LI', i, l[:80])
    if l.rstrip().endswith(('?', '.', '»', '!')) is False and not l.startswith('#') and not bid(l):
        print('END?', i, l[-40:])
    if '  ' in l:
        print('DOUBLESPACE', i)
    # question/statement end parity with Pali
    pe = re.sub(r'\s*\^[0-9A-Za-z-]+\s*$', '', pl[i]).rstrip()
    re_ = re.sub(r'\s*\^[0-9A-Za-z-]+\s*$', '', l).rstrip()
    if not l.startswith('#') and pe[-1:] != re_[-1:]:
        print('ENDDIFF', i, repr(pe[-25:]), '|', repr(re_[-25:]))
# counts of selected strings
for s in ['неповреждённа', 'неповреждённая', 'Здесь некий', 'Вот человек', 'положения тела', 'манер', 'красот', 'внешност', 'хотение', 'Кто такие']:
    print(s, rt.count(s))
# number words in Pali vs Russian per line
pn = {'eka':1,'dve':2,'dvi':2,'tīṇi':3,'tayo':3,'tisso':3,'cattāro':4,'cattāri':4,'catasso':4,'pañca':5,'cha':6,'satta':7,'aṭṭha':8,'nava':9,'dasa':10,'aṭṭhārasa':18,'chattiṃsa':36,'soḷasa':16,'dvāsaṭṭhi':62}
rn = {'два':2,'две':2,'три':3,'четыре':4,'пять':5,'шесть':6,'семь':7,'восемь':8,'девять':9,'десять':10,'восемнадцать':18,'тридцать':36,'шестнадцать':16,'шестьдесят':62,'сто':108}
from collections import Counter
for i, (a, b) in enumerate(zip(pl, rl)):
    ca = Counter(pn[w] for w in re.findall(r"[a-zA-Zāīūṃṅñṭḍṇḷ]+", a.lower()) if w in pn)
    if 'aṭṭhataṇhāvicaritasataṃ' in a or 'taṇhāvicaritasataṃ' in a: ca[108] += 1
    cb = Counter(rn[w] for w in re.findall(r"[а-яё]+", b.lower()) if w in rn)
    if ca != cb:
        print('NUM', i, bid(a) or bid(b), dict(ca), dict(cb))
