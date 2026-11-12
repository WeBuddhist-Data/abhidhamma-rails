import re, io, sys, collections
base = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation'
ch = sys.argv[1]
lo = int(sys.argv[2]) if len(sys.argv) > 2 else 1
hi = int(sys.argv[3]) if len(sys.argv) > 3 else 9999
P = [l for l in io.open(base + r'\pali\pi-2_split_chapters\\' + ch, encoding='utf8').read().split('\n') if l.strip()]
H = [l for l in io.open(base + r'\hindi\pi-2-hindi-plain-rails_split_chapters\\' + ch, encoding='utf8').read().split('\n') if l.strip()]

# Pali number stems (order matters: longest first)
pnum = [
 ('caturāsīti', 84), ('catusaṭṭhi', 64), ('bāttiṃsa', 32), ('bāvīsati', 22), ('aṭṭhavīsa', 28), ('aṭṭhārasa', 18), ('sattarasa', 17), ('soḷasa', 16),
 ('pannarasa', 15), ('cuddasa', 14), ('terasa', 13), ('dvādasa', 12), ('ekādasa', 11), ('cattārīsa', 40), ('vīsati', 20),
 ('saṭṭhi', 60), ('paññāsa', 50), ('navuti', 90), ('tiṃsa', 30),
 ('dasa', 10), ('nava', 9), ('aṭṭha', 8), ('satta', 7), ('cha', 6), ('pañca', 5),
 ('cattāro', 4), ('catasso', 4), ('cattāri', 4), ('catu', 4), ('tayo', 3), ('tīṇi', 3), ('tisso', 3), ('tīṇ', 3),
 ('dve', 2), ('dv', 2), ('eko', 1), ('ekā', 1), ('ekaṃ', 1), ('eka', 1),
]
hnum = {'एक': 1, 'दो': 2, 'तीन': 3, 'चार': 4, 'पाँच': 5, 'छह': 6, 'सात': 7, 'आठ': 8, 'नौ': 9, 'दस': 10, 'ग्यारह': 11, 'बारह': 12,
        'तेरह': 13, 'चौदह': 14, 'पंद्रह': 15, 'सोलह': 16, 'सत्रह': 17, 'अठारह': 18, 'बाईस': 22, 'बीस': 20, 'चालीस': 40, 'साठ': 60,
        'चौरासी': 84, 'चौंसठ': 64, 'बत्तीस': 32, 'अट्ठाईस': 28, 'पचास': 50, 'नब्बे': 90, 'तीस': 30, 'सौ': 100, 'हज़ार': 1000, 'लाख': 100000}

def pal_nums(s):
    s = re.sub(r'\[[^\]]*\]', '', s)
    out = []
    for w in re.findall(r"[a-zA-Zāīūṃṅñṭḍṇḷ]+", s):
        wl = w.lower()
        if wl in ('sattā', 'sattānaṃ', 'satte', 'sattāti'):  # beings
            continue
        for stem, n in pnum:
            st = stem[:-1] if (stem.endswith('a') and len(stem) > 4 and stem not in ('satta','aṭṭha','pañca')) else stem
            if wl.startswith(st) and not (st != stem and wl.startswith(stem) is False and wl[len(st):len(st)+1] not in ('ā','i','ī','u')):
                # avoid false hits
                if stem == 'eka' and not re.match(r'eka(ṃ|ā|o|dasa|ssa|kkhaṇe)?$', wl) and not wl.startswith('ekādasa'):
                    break
                if stem in ('dv',) and not re.match(r'dv(e|āyatan|indriy|ādasa)', wl):
                    break
                if stem == 'satta' and wl.startswith('sattamo'):
                    break
                if stem == 'catu' and not re.match(r'catu(ttha|rāsīti|saṭṭhi)', wl):
                    break
                if stem == 'aṭṭha' and wl.startswith('aṭṭhamo'):
                    break
                if stem == 'nava' and not re.match(r'nav(a|indriy|āyatan)', wl):
                    break
                out.append(n)
                break
    return out

def hin_nums(s):
    s = re.sub(r'\[[^\]]*\]', '', s)
    return [hnum[w] for w in re.findall(r'[\u0900-\u097F]+', s) if w in hnum]

for i, (a, b) in enumerate(zip(P, H), 1):
    if i < lo or i > hi:
        continue
    fl = []
    pn = sorted(pal_nums(a)); hn = sorted(hin_nums(b))
    if collections.Counter(pn) != collections.Counter(hn):
        fl.append(f'NUM P{pn} H{hn}')
    sp = len(re.findall(r'\bsiyā\b', a, re.I)); sh = b.count('कभी')
    if sp != sh: fl.append(f'SIYA {sp}/{sh}')
    vp = len(re.findall(r'vattabb', a)); vh = len(re.findall(r'नहीं कहा जा सकता|नहीं कहे जा सकते|नहीं कही जा सकती|नहीं कहा जा सकता', b))
    if vp != vh: fl.append(f'VATTABBA {vp}/{vh}')
    kp = len(re.findall(r'(?<![a-zāīū])kusal', a, re.I)); ap = len(re.findall(r'akusal', a, re.I)); bp = len(re.findall(r'abyākat', a, re.I))
    kh = b.count('हितकर'); ah = b.count('हानिकर'); bh = b.count('अनिर्धारित')
    if (kp, ap, bp) != (kh, ah, bh): fl.append(f'KAB P{(kp,ap,bp)} H{(kh,ah,bh)}')
    # negation rough
    npn = len(re.findall(r'\b(na|no|neva)\b', a))
    nh = len(re.findall(r'(?<![\u0900-\u097F])(न|नहीं)(?![\u0900-\u097F])', b))
    if npn != nh: fl.append(f'NEG {npn}/{nh}')
    if fl:
        print(i, ' | '.join(fl))

