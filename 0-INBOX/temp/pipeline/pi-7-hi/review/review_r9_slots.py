import os, re, sys, json
from collections import defaultdict, Counter
sys.path.insert(0, os.path.dirname(__file__))
from review_r9_common import *

PR1 = re.compile(r'^(.+?)(?: dhammaṃ)? paṭicca(?:…pe…)?\s+(.+?) dhamm(o|ā) uppajja(ti|nti)')
PR2 = re.compile(r'^(.+?) dhamm(o|ā) (.+?) dhammassa \S+paccayena paccayo')
HR1 = re.compile(r'^(.+?) परिघटना(?:ओं)? पर निर्भर होकर(?:…)?\s+(.+?) (परिघटनाएँ|परिघटना) \S+-कारण .*?उत्पन्न होती (हैं|है)')
HR2 = re.compile(r'^(.+?) (परिघटना|परिघटनाएँ), (.+?) परिघटना(?:ओं)? के लिए \S+(?: \S+)?-कारण के रूप में कारण होती (हैं|है)')
HR1b = re.compile(r'^(.+?) परिघटना(?:ओं)? पर निर्भर होकर')

END = re.compile(r'(assa|ussa|issa|aṃ|uṃ|iṃ|o|ā|ū|ī|u|i|a|e)$')
PART = {'ca', 'ceva'}


def pstem(slot):
    s = slot.lower().replace('…pe…', ' ')
    toks = []
    for w in s.split():
        w = w.strip(',.')
        if w in PART:
            toks.append('^' if w == 'ceva' else '&')
            continue
        if w.endswith('ñceva'):
            w = w[:-5]; amp = '^'
        elif w.endswith('ñca'):
            w = w[:-3]; amp = '&'
        else:
            amp = None
        w = END.sub('', w)
        toks.append(w)
        if amp:
            toks.append(amp)
    return ' '.join(toks)


def hnorm(s):
    s = re.sub(r'परिघटना(एँ|ओं)?', '', s)
    s = re.sub(r'\s+', ' ', s).strip(' ,')
    s = s.replace(' और', ' और')
    s = re.sub(r'\s+,', ',', s)
    return s


def split_sent(t, lang):
    if lang == 'p':
        return [x for x in re.split(r'(?<=[.?])\s+|(?<=\))\s+(?=[A-ZĀ])', t) if x.strip()]
    return [x for x in re.split(r'(?<=[।?])\s+|(?<=\))\s+(?=[^\s(])', t) if x.strip()]


slots = []  # (f, ne, sid, kind, pkey, hval, praw, hraw)
fails = []
for f, sid, ne, p, h, pid, hid in pairs():
    if p.lstrip().startswith('#') or p.lstrip().startswith('('):
        continue
    ps = split_sent(re.sub(r'dhammadhamm', 'dhamma dhamm', p), 'p')
    hs = split_sent(h, 'h')
    pm = [(PR1.match(x), PR2.match(x)) for x in ps]
    hm = [(HR1.match(x), HR2.match(x)) for x in hs]
    pf = [(i, 'R1' if a else 'R2' if b else None) for i, (a, b) in enumerate(pm) if a or b]
    hf = [(i, 'R1' if a else 'R2' if b else None) for i, (a, b) in enumerate(hm) if a or b]
    if [k for _, k in pf] != [k for _, k in hf]:
        fails.append((f, ne, sid, [k for _, k in pf], [k for _, k in hf], p, h))
        continue
    for (pi, k), (hi, _) in zip(pf, hf):
        a, b = pm[pi]
        c, d = hm[hi]
        if k == 'R1':
            slots.append((f, ne, sid, 'acc', pstem(a.group(1)), hnorm(c.group(1)), a.group(1), c.group(1)))
            slots.append((f, ne, sid, 'nom', pstem(a.group(2)), hnorm(c.group(2)), a.group(2), c.group(2)))
            if (a.group(3) == 'ā') != (c.group(3) == 'परिघटनाएँ') or (a.group(4) == 'nti') != (c.group(4) == 'हैं'):
                fails.append((f, ne, sid, 'NUMBER-AGREE', '', ps[pi], hs[hi]))
        else:
            slots.append((f, ne, sid, 'nom', pstem(b.group(1)), hnorm(d.group(1)), b.group(1), d.group(1)))
            slots.append((f, ne, sid, 'gen', pstem(b.group(3)), hnorm(d.group(3)), b.group(3), d.group(3)))
            if (b.group(2) == 'ā') != (d.group(2) == 'परिघटनाएँ') or (b.group(2) == 'ā') != (d.group(4) == 'हैं'):
                fails.append((f, ne, sid, 'NUMBER-AGREE', '', ps[pi], hs[hi]))

json.dump(slots, open(os.path.join(os.path.dirname(__file__), 'review_r9_slots.json'), 'w', encoding='utf-8'), ensure_ascii=False)
print('slots', len(slots), 'fails', len(fails))
for x in fails:
    print(x[:5])
    print('  P:', x[5][:400])
    print('  H:', x[6][:400])
