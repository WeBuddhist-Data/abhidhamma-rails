import re, sys, os, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from review_r4_struct_lib import *

L = r'(?<![a-zāīūṃṅñṭḍṇḷ])'
V = 'वाल[ीेा]'
ITEMS = {
    '2-09': ([('hīn', 'H'), ('majjhim', 'M'), ('paṇīt', 'P')],
             [('हीन', 'H'), ('मध्यम', 'M'), ('उत्तम', 'P')]),
    '2-10': ([('micchattaniyat', 'M'), ('sammattaniyat', 'S'), ('aniyat', 'A')],
             [('ग़लत दिशा में निश्चित', 'M'), ('सही दिशा में निश्चित', 'S'), ('अनिश्चित', 'A')]),
    '2-11': ([('maggārammaṇ', 'R'), ('maggahetuk', 'H'), ('maggādhipat', 'A')],
             [('मार्ग को विषय बनाने ' + V, 'R'), ('मार्ग को मूल बनाने ' + V, 'H'), ('मार्ग की प्रधानता ' + V, 'A')]),
    '2-12': ([('anuppann', 'N'), ('uppann', 'U'), ('uppād', 'D')],
             [('उत्पन्न न हु[ईएआ]', 'N'), ('उत्पन्न हो चुक[ीेा]', 'U'), ('उत्पन्न होने ' + V, 'D')]),
    '2-13': ([('atīt', 'T'), ('anāgat', 'N'), ('paccuppann', 'P')],
             [('अतीत', 'T'), ('भविष्य', 'N'), ('वर्तमान', 'P')]),
    '2-14': ([('atītārammaṇ', 'TR'), ('anāgatārammaṇ', 'NR'), ('paccuppannārammaṇ', 'PR'),
              ('atīt', 'T'), ('anāgat', 'N'), ('paccuppann', 'P')],
             [('अतीत के विषय', 'TR'), ('भविष्य के विषय', 'NR'), ('वर्तमान के विषय', 'PR'),
              ('अतीत', 'T'), ('भविष्य', 'N'), ('वर्तमान', 'P')]),
    '2-15': ([('ajjhatt', 'A'), ('bahiddh', 'B')],
             [('स्वयं से संबंधित', 'A'), ('दूसरों से संबंधित', 'B')]),
    '2-16': ([('ajjhattārammaṇ', 'AR'), ('bahiddhārammaṇ', 'BR'), ('ajjhatt', 'A'), ('bahiddh', 'B')],
             [('स्वयं से संबंधित विषय', 'AR'), ('दूसरों से संबंधित विषय', 'BR'),
              ('स्वयं से संबंधित', 'A'), ('दूसरों से संबंधित', 'B')]),
    '2-17': ([('sanidassanasappaṭigh', 'S'), ('anidassanasappaṭigh', 'A'), ('anidassanaappaṭigh', 'N')],
             [('दिखाई देने ' + V + ' और टकराव ' + V, 'S'), ('दिखाई न देने ' + V + ' पर टकराव ' + V, 'A'),
              ('दिखाई न देने ' + V + ' और टकराव से रहित', 'N')]),
}

def seq(s, pats, latin):
    res = []
    for pat, code in pats:
        rx = (L + pat) if latin else pat
        for m in re.finditer(rx, s, re.I):
            res.append((m.start(), m.end(), code))
    res.sort(key=lambda x: (x[0], -(x[1] - x[0])))
    out = []; last = -1
    for st, en, c in res:
        if st < last:
            continue
        out.append(c); last = en
    return out

def head(p, latin):
    # head of line: up to first ' – ' or '. ' or '…'
    m = re.split(r' – |\. |…|\(', p, 1)
    return m[0]

if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else 'all'
    tot = 0
    for f in FILES:
        pp, hp = ITEMS[f[:4]]
        P = nonempty(load(os.path.join(PA, f)))
        H = nonempty(load(os.path.join(HI, f)))
        for n, ((_, p), (_, h)) in enumerate(zip(P, H), 1):
            if p.startswith('#'):
                continue
            a = seq(head(p, True), pp, True); b = seq(head(h, False), hp, False)
            fa = seq(p, pp, True); fb = seq(h, hp, False)
            bad_head = a != b
            bad_all = collections.Counter(fa) != collections.Counter(fb)
            if bad_head or bad_all:
                tot += 1
                print(f[:4], n, 'HEAD' if bad_head else '', 'ALL' if bad_all else '')
                if bad_head:
                    print('  Ph', a); print('  Hh', b)
                if bad_all:
                    ca, cb = collections.Counter(fa), collections.Counter(fb)
                    print('  P-H', dict(ca - cb), ' H-P', dict(cb - ca))
    print('TOTAL', tot)
