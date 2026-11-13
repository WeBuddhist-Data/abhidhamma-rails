"""Abstract faculty names in aligned Pali/Hindi lines and group by Pali template."""
import re, os, sys
from collections import defaultdict, OrderedDict
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from review_r7_pairs import load

FILES = [f'10-0{i}-indriyayamaka.md' for i in range(1, 8)]

# key, pali full stem, pali bare regex, hindi bare
ITEMS = [
    ('cak', 'cakkhundriy', r'cakkhu[ṃū]?', 'आँख'),
    ('sot', 'sotindriy', r'sota[ṃn]?', 'कान'),
    ('ghā', 'ghānindriy', r'ghāna[ṃn]?', 'नाक'),
    ('jiv', 'jivhindriy', r'jivhā?', 'जीभ'),
    ('kāy', 'kāyindriy', r'kāy[oaṃ]', 'शरीर'),
    ('man', 'manindriy', r'man[oa]', 'मन'),
    ('itt', 'itthindriy', r'itth[iī]', 'स्त्री'),
    ('pur', 'purisindriy', r'puris[oa]', 'पुरुष'),
    ('jīv', 'jīvitindriy', r'jīvita[ṃn]?', 'जीवन'),
    ('suk', 'sukhindriy', r'sukha[ṃn]?', 'सुख'),
    ('duk', 'dukkhindriy', r'dukkha[ṃn]?', 'दुःख'),
    ('som', 'somanassindriy', r'somanassa[ṃn]?', 'प्रसन्नता'),
    ('dom', 'domanassindriy', r'domanassa[ṃn]?', 'उदासी'),
    ('upe', 'upekkhindriy', r'upekkhā?', 'समभाव'),
    ('sad', 'saddhindriy', r'saddhā', 'श्रद्धा'),
    ('vīr', 'vīriyindriy', r'vīriya[ṃn]?', 'उत्साह'),
    ('sat', 'satindriy', r'sat[iī]', 'सजगता'),
    ('sam', 'samādhindriy', r'samādh[iī]', 'एकाग्रता'),
    ('paa', 'paññindriy', r'paññā', 'प्रज्ञा'),
    ('ana', 'anaññātaññassāmītindriy', r'anaññāta[ñ]+[aā]ssāmīti', '“जो अब तक नहीं जाना उसे मैं जान लूँगा”'),
    ('aññ', 'aññindriy', r'añña[ṃn]', 'पूर्ण ज्ञान'),
    ('ātā', 'aññātāvindriy', r'aññātāvī', 'पूर्ण ज्ञान पा चुका व्यक्ति'),
]
HFULL = {k: ('जीवन-क्षमता' if k == 'jīv' else ('पूर्ण ज्ञान पा चुके की क्षमता' if k == 'ātā' else hb + ' की क्षमता')) for k, _, _, hb in ITEMS}
HFULL['itt'] = 'स्त्रीत्व की क्षमता'
HFULL['pur'] = 'पुरुषत्व की क्षमता'
PL = r'[A-Za-zāīūṃṅñṭḍṇḷ]'
DV = r'[ऀ-ॿ]'
idre = re.compile(r'\s*\^(6-[\d-]+)\s*$')

def p_tokens(line, bare=True):
    toks = []
    for k, stem, bre, hb in ITEMS:
        for m in re.finditer(rf'(?<!{PL}){stem}{PL}*', line, re.I):
            toks.append((m.start(), m.end(), 'F', k))
    if bare:
        for k, stem, bre, hb in ITEMS:
            for m in re.finditer(rf'(?<!{PL})(?:{bre})(?:ñca|ñceva|ti|nti|ceva|ñ)?(?!{PL})', line, re.I):
                toks.append((m.start(), m.end(), 'B', k))
    toks.sort()
    # drop overlaps
    out, last = [], -1
    for t in toks:
        if t[0] >= last:
            out.append(t); last = t[1]
    return out

def h_tokens(line):
    toks = []
    for k, _, _, hb in ITEMS:
        full = HFULL[k]
        for m in re.finditer(rf'(?<!{DV}){re.escape(full)}(?:एँ|ओं)?', line):
            toks.append((m.start(), m.end(), 'F', k))
    for k, _, _, hb in sorted(ITEMS, key=lambda x: -len(x[3])):
        for m in re.finditer(rf'(?<!{DV}){re.escape(hb)}(?!{DV})', line):
            toks.append((m.start(), m.end(), 'B', k))
    toks.sort(key=lambda t: (t[0], -(t[1] - t[0])))
    out, last = [], -1
    for t in toks:
        if t[0] >= last:
            out.append(t); last = t[1]
    return out

def abstract(line, toks, mapping):
    s, pos = [], 0
    for a, b, kind, k in toks:
        s.append(line[pos:a])
        if k not in mapping:
            mapping[k] = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[len(mapping)] if len(mapping) < 26 else '?'
        s.append(f'<{kind}{mapping[k]}>')
        pos = b
    s.append(line[pos:])
    return ''.join(s)

def rows(files=FILES):
    for fn in files:
        pl, hl = load(fn)
        for i, (p, h) in enumerate(zip(pl, hl), 1):
            pid = idre.search(p)
            pb, hb = idre.sub('', p), idre.sub('', h)
            mapping = OrderedDict()
            ap = abstract(pb, p_tokens(pb), mapping)
            pk = set(mapping)
            ah = abstract(hb, h_tokens(hb), mapping)
            extra = set(mapping) - pk
            yield fn, i, pid.group(1) if pid else '', pb, hb, ap, ah, extra

if __name__ == '__main__':
    groups = defaultdict(lambda: defaultdict(list))
    mism = []
    for fn, i, pid, pb, hb, ap, ah, extra in rows():
        groups[ap][ah].append((fn, i))
        if extra:
            mism.append((fn, i, extra))
    print('templates', len(groups), 'lines', sum(len(v2) for v in groups.values() for v2 in v.values()))
    print('lines with Hindi items not in Pali:', len(mism))
    for m in mism[:40]:
        print('  EXTRA', m)
    multi = {k: v for k, v in groups.items() if len(v) > 1}
    print('templates with >1 Hindi variant:', len(multi))
    mode = sys.argv[1] if len(sys.argv) > 1 else ''
    if mode == 'multi':
        for k, v in multi.items():
            print('=' * 10)
            print('P:', k)
            for ah, locs in sorted(v.items(), key=lambda x: -len(x[1])):
                print(f'  [{len(locs)}] {locs[:4]} H: {ah}')
    if mode == 'uniq':
        lo, hi = int(sys.argv[2]), int(sys.argv[3])
        for n, (k, v) in enumerate(groups.items()):
            if lo <= n < hi:
                ah, locs = max(v.items(), key=lambda x: len(x[1]))
                print(f'#{n} [{sum(len(x) for x in v.values())}] {locs[0]}')
                print('  P:', k)
                print('  H:', ah)
