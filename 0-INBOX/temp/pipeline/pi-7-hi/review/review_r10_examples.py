import os, sys, re
sys.path.insert(0, os.path.dirname(__file__))
from review_r10_align import pairs
from review_r10_check import strip_id
PAIRS = [
 ('khandh', 'समूह'), ('mahābhūt', 'महाभूत'), ('samuṭṭhān', 'मन से उत्पन्न'), ('kaṭattā', 'किए गए कर्म'),
 ('upādā(?!n)', 'व्युत्पन्न'), ('paṭisandhi', 'पुनर्जन्म'), ('vatthu', 'आधार'), ('kiriy', 'क्रिया'),
 ('moh', 'मोह'), ('vicikicch', 'संशय'), ('uddhacc', 'बेचैनी'), ('pavatt', 'जीवन-'),
 ('sukh', 'सुख'), ('dukkh', 'दुःख'), ('pīti', 'उल्लास'), ('upekkh', 'समभाव'),
 ('sanidassan', 'दिखाई देने'), ('anidassan', 'दिखाई न देने'), ('sappaṭigh', 'टकराव वाल'), ('appaṭigh', 'टकराव से रहित'),
 ('lokiy', 'लौकिक'), ('lokuttar', 'लोकोत्तर'), ('saraṇ', 'संघर्ष वाल'), ('araṇ', 'संघर्ष से रहित'),
 ('vitakk', 'आरंभिक विचार'), ('vicār', 'सतत विचार'), ('sahetuk', 'मूल वाल'), ('ahetuk', 'मूल से रहित'),
 ('atīt', 'अतीत'), ('anāgat', 'भविष्य'), ('paccuppann', 'वर्तमान'), ('ajjhatt', 'स्वयं से संबंधित'), ('bahiddh', 'दूसर'),
 ('paritt', 'सीमित'), ('mahaggat', 'उन्नत'), ('appamāṇ', 'असीम'), ('hīn', 'हीन'), ('majjhim', 'मध्यम'), ('paṇīt', 'उत्तम'),
 ('kāmāvacar', 'इंद्रिय-सुख'), ('arūpāvacar', 'अभौतिक लोक'), ('sekkh', 'सीख'), ('dassanen', 'सत्य-दर्शन'), ('bhāvanā', 'अभ्यास'),
 ('āsav', 'मन के मैल'), ('kiles|kiliṭṭh', 'क्लेश'), ('saññojan', 'बंधन'), ('ganth', 'गाँठ'), ('nīvaraṇ', 'बाधा'), ('upādān', 'आसक्ति'),
 ('niyyānik', 'मुक्ति'), ('cetasik', 'सहचर'), ('upādinn', 'कर्म से उत्पन्न'), ('magg', 'मार्ग'),
]
def cnt(rx, s):
    return len(re.findall(rx, s))
out = os.path.join(os.path.dirname(__file__), 'review_r10_examples_out.txt')
n = 0
with open(out, 'w', encoding='utf-8') as o:
    for f, pl, hl in pairs():
        for i, (a, b) in enumerate(zip(pl, hl), 1):
            if a.startswith('#'):
                continue
            a0, b0 = strip_id(a).lower(), strip_id(b)
            a0 = re.sub(r"\{[^}]*\}", "", a0); b0 = re.sub(r"\[[^\]]*\]", "", b0)
            bad = []
            for p, h in PAIRS:
                if p in ('sukh', 'dukkh'):
                    x = cnt(p, a0); y = cnt(r'(?<!इंद्रिय-)' + h, b0)
                elif p in ('saraṇ',):
                    x = cnt(r"saraṇ", a0); y = cnt(h, b0)
                elif p == 'araṇ':
                    x = cnt(r"(?<![s])araṇ", a0); y = cnt(h, b0)
                elif p == 'sanidassan':
                    x = cnt(r"(?<![a-zāī])(?:na|no)*sanidassan", a0); y = cnt(h, b0)
                elif p == 'anidassan':
                    x = cnt(r"(?<![a-zāī])(?:na|no)*anidassan", a0); y = cnt(h, b0)
                elif p == 'sappaṭigh':
                    x = cnt(r"sappaṭigh", a0); y = cnt(h, b0)
                elif p == 'appaṭigh':
                    x = cnt(r"(?<!s)appaṭigh", a0); y = cnt(h, b0)
                elif p == 'sahetuk':
                    x = cnt(r"sahetuk", a0); y = cnt(h, b0)
                elif p == 'ahetuk':
                    x = cnt(r"(?<![a-zāī])(?:na|no)*ahetuk", a0); y = cnt(h, b0)
                elif p == 'vicār':
                    x = cnt(p, a0) ; y = cnt(h, b0)
                else:
                    x = cnt(p, a0); y = cnt(h, b0)
                if x != y:
                    bad.append(f'{p}:{x}/{y}')
            if bad:
                n += 1
                o.write(f'[{f[:4]}:{i}] ' + ' '.join(bad) + '\n')
print(out, n)
