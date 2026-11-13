import sys, re
sys.path.insert(0, r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\review')
from review_r7_common import *

praw, pl = load(P)
hraw, hl = load(H)
S = segs(pl)
D = dyad_of(pl)

W = r'(?<![\wāīūṃṅñṭḍṇḷ])'
E_ = r'[\wāīūṃṅñṭḍṇḷ]*'
# Pali: list of (regex, pol)
PI = {
 'Sārammaṇadukaṃ': [(W + 'sārammaṇ' + E_, 1), (W + 'anārammaṇ' + E_, 0)],
 'Cittadukaṃ': [(W + r'citt(?:aṃ|o|assa|añca|ā|a|e|ānaṃ)(?![\wāīūṃṅñṭḍṇḷ])', 1), (W + r'nocitt(?:aṃ|o|assa|añca|ā|a|e|ānaṃ)(?![\wāīūṃṅñṭḍṇḷ])', 0)],
 'Cetasikadukaṃ': [(W + 'cetasik' + E_, 1), (W + 'acetasik' + E_, 0)],
 'Cittasampayuttadukaṃ': [(W + 'cittasampayutt' + E_, 1), (W + 'cittavippayutt' + E_, 0)],
 'Cittasaṃsaṭṭhadukaṃ': [(W + 'cittasaṃsaṭṭh' + E_, 1), (W + 'cittavisaṃsaṭṭh' + E_, 0)],
 'Cittasamuṭṭhānadukaṃ': [(W + 'cittasamuṭṭhān' + E_, 1), (W + 'nocittasamuṭṭhān' + E_, 0)],
 'Cittasahabhūdukaṃ': [(W + 'cittasahabh' + E_, 1), (W + 'nocittasahabh' + E_, 0)],
 'Cittānuparivattidukaṃ': [(W + 'cittānuparivatt' + E_, 1), (W + 'nocittānuparivatt' + E_, 0)],
 'Cittasaṃsaṭṭhasamuṭṭhānadukaṃ': [(W + 'cittasaṃsaṭṭhasamuṭṭhān' + E_, 1), (W + 'nocittasaṃsaṭṭhasamuṭṭhān' + E_, 0)],
 'Cittasaṃsaṭṭhasamuṭṭhānasahabhūdukaṃ': [(W + 'cittasaṃsaṭṭhasamuṭṭhānasahabh' + E_, 1), (W + 'nocittasaṃsaṭṭhasamuṭṭhānasahabh' + E_, 0)],
 'Cittasaṃsaṭṭhasamuṭṭhānānuparivattidukaṃ': [(W + 'cittasaṃsaṭṭhasamuṭṭhānānuparivatt' + E_, 1), (W + 'nocittasaṃsaṭṭhasamuṭṭhānānuparivatt' + E_, 0)],
 'Ajjhattikadukaṃ': [(W + 'ajjhattik' + E_, 1), (W + 'bāhir' + E_, 0)],
 'Upādādukaṃ': [(W + r'upādā(?![\wāīūṃṅñṭḍṇḷ])', 1), (W + r'noupādā(?![\wāīūṃṅñṭḍṇḷ])', 0)],
 'Upādinnadukaṃ': [(W + 'upādinn' + E_, 1), (W + 'anupādinn' + E_, 0)],
}
NEGTAIL = re.compile(r'^ न (होने|करने) वाल')
# Hindi: (core regex, special-neg regex or None)
HI = {
 'Sārammaṇadukaṃ': (r'विषय वाल[ीेा]', r'विषय से रहित'),
 'Cittadukaṃ': (r'मन रूपी', None),
 'Cetasikadukaṃ': (r'मन (?:की|के|का) सहचर', None),
 'Cittasampayuttadukaṃ': (r'मन से जुड़[ीेा]', r'मन से अलग'),
 'Cittasaṃsaṭṭhadukaṃ': (r'मन से घुल[ीेा]-मिल[ीेा]', None),
 'Cittasamuṭṭhānadukaṃ': (r'मन से उत्पन्न', None),
 'Cittasahabhūdukaṃ': (r'मन के साथ-साथ(?: होने वाल)?', None),
 'Cittānuparivattidukaṃ': (r'मन का अनुसरण(?: करने वाल)?', None),
 'Cittasaṃsaṭṭhasamuṭṭhānadukaṃ': (r'मन से घुल[ीेा]-मिल[ीेा] और मन से उत्पन्न', None),
 'Cittasaṃsaṭṭhasamuṭṭhānasahabhūdukaṃ': (r'मन से घुल[ीेा]-मिल[ीेा],? मन से उत्पन्न और मन के साथ-साथ(?: होने वाल)?', None),
 'Cittasaṃsaṭṭhasamuṭṭhānānuparivattidukaṃ': (r'मन से घुल[ीेा]-मिल[ीेा],? मन से उत्पन्न और मन का अनुसरण(?: करने वाल)?', None),
 'Ajjhattikadukaṃ': (r'आंतरिक', r'बाह्य'),
 'Upādādukaṃ': (r'व्युत्पन्न', None),
 'Upādinnadukaṃ': (r'कर्म से उत्पन्न', None),
}

def head(t, hindi=False):
    t = IDRE.sub('', t)
    return re.split(r' – |…|\(|\. |\.$|।|;', t)[0]

def pitems(t, d):
    out = []
    for rx, pol in PI[d]:
        for m in re.finditer(rx, t, flags=re.I):
            out.append((m.start(), pol))
    return [p for _, p in sorted(out)]

def hitems(t, d):
    core, sneg = HI[d]
    out = []
    for m in re.finditer(core, t):
        tail = t[m.end():]
        pol = 0 if NEGTAIL.match(tail) or re.match(r'^ न (होने|करने) वाल', ' ' + tail.lstrip()) and tail.startswith(' न') else 1
        out.append((m.start(), pol))
    if sneg:
        for m in re.finditer(sneg, t):
            out.append((m.start(), 0))
    return [p for _, p in sorted(out)]

FULL = '-full' in sys.argv
checked = 0
for ((n, i, p), sid), (_, _, h) in zip(S, hl):
    if p.startswith('#') or 'dhamm' not in p.lower():
        continue
    d = D[n]
    if d not in PI:
        continue
    ph, hh = head(p), head(h, True)
    if 'dhamm' not in ph.lower():
        continue
    if FULL:
        if d == 'Cittadukaṃ': continue
        ph = IDRE.sub('', p); hh = IDRE.sub('', h)
        hh = re.sub(r'व्युत्पन्न भौतिक रूप', 'X', hh); hh = re.sub(r'किए गए कर्म से उत्पन्न', 'X', hh)
    checked += 1
    a, b = pitems(ph, d), hitems(hh, d)
    if a != b:
        print('ITEM', n, sid, d, a, b)
        print('   P', ph)
        print('   H', hh)
print('checked', checked)

