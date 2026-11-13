import os, sys, re, collections
sys.path.insert(0, os.path.dirname(__file__))
from review_r10_align import pairs, IDRE
# unique heading pairs (Pali text without id/number -> set of Hindi renderings)
m = collections.OrderedDict()
for f, pl, hl in pairs():
    for i, (a, b) in enumerate(zip(pl, hl), 1):
        if a.startswith('#') or 'niṭṭhit' in a:
            pa = re.sub(r"^#+\s*", "", IDRE.sub('', a)).strip()
            hb = re.sub(r"^#+\s*", "", IDRE.sub('', b)).strip()
            pa2 = re.sub(r"^[\d\-\.\s]+", "", pa).strip('* ')
            hb2 = re.sub(r"^[\d\-\.\s]+", "", hb).strip('* ')
            numa = re.match(r"^\*?([\d\-\.\s]*)", pa).group(1).strip()
            numb = re.match(r"^\*?([\d\-\.\s]*)", hb).group(1).strip()
            key = pa2
            m.setdefault(key, collections.Counter())[hb2] += 1
            if numa != numb:
                print('NUMDIFF', f, i, pa, '|', hb)
out = os.path.join(os.path.dirname(__file__), 'review_r10_heads_out.txt')
with open(out, 'w', encoding='utf-8') as o:
    for k, v in m.items():
        o.write(f'{k} => ' + ' || '.join(f'{h} ({c})' for h, c in v.items()) + '\n')
print(out, len(m))
