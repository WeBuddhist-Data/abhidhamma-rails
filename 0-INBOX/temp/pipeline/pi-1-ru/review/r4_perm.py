import re, os
base = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation'
P = os.path.join(base, 'pali', 'pi-1_split_chapters', '4-02-nikkhepakandam.md')
R = os.path.join(base, 'russian', 'pi-1-russian-plain-rails_split_chapters', '4-02-nikkhepakandam.md')
pl = [l for l in open(P, encoding='utf-8') if '^1-1257' in l][0]
rl = [l for l in open(R, encoding='utf-8') if '^1-1257' in l][0]
pk = {'lobh': 'L', 'dos': 'D', 'moh': 'M', 'mān': 'Ma', 'diṭṭh': 'Di', 'vicikicch': 'V', 'thin': 'T', 'uddhacc': 'U', 'ahirik': 'A', 'anottapp': 'O'}
rk = {'жадност': 'L', 'злоб': 'D', 'заблуждени': 'M', 'самомнени': 'Ma', 'воззрени': 'Di', 'колебани': 'V', 'вялост': 'T', 'беспокойств': 'U', 'бессовестност': 'A', 'отсутстви': 'O'}
def key(w, d):
    for k, v in d.items():
        if w.startswith(k):
            return v
    return '?' + w
body = pl.split('?', 1)[1]
pp = re.findall(r'(\w+) (\w+) kileso ceva', body)
ppk = [(key(a, pk), key(b, pk)) for a, b in pp]
rbody = rl.split('?', 1)[1]
rp = re.findall(r'(?:^|, )\s*([а-яё ]+?) по отношению к ([а-яё ]+?) является омрачением', rbody, flags=re.I)
def rkey(s):
    s = s.strip().lower()
    if s.startswith('отсутств'):
        return 'O'
    return key(s, rk)
rpk = [(rkey(a), rkey(b)) for a, b in rp]
print(len(ppk), len(rpk))
for i, (x, y) in enumerate(zip(ppk, rpk)):
    if x != y:
        print(i, x, y)
