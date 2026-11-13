"""Count being/place/moment chunks per line in Pali vs Hindi."""
import re, os, sys, unicodedata
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from review_r7_pairs import load
from review_r7_abstract import FILES

B = r'(?<![A-Za-zāīūṃṅñṭḍṇḷ])'
T = [
    ('upapajjant', B + r'upapajjant', r'जन्म लेने वाल'),
    ('cavant', B + r'cavant', r'मरने वाल'),
    ('upapajjitvā', r'upapajjitvā', r'जन्म लेकर'),
    ('parinibbāy', r'parinibbāyissanti', r'पूर्ण निर्वाण पाएँग'),
    ('na itthī', B + r'na itthīnaṃ', r'स्त्रियों से भिन्न'),
    ('itthī/yo', B + r'itth(īnaṃ|iyo)', r'स्त्रियों|स्त्रियाँ'),
    ('na purisa', B + r'na purisānaṃ', r'पुरुषों से भिन्न'),
    ('purisā/naṃ', B + r'puris(ānaṃ|ā)(?![A-Za-zāīūṃ])', r'पुरुषों|(?<=जो )पुरुष(?= इसी)'),
    ('asañña', B + r'asaññasatt', r'पहचान-रहित'),
    ('sacakkhuk', B + r'sacakkhuk', r'आँख वाल'),
    ('acakkhuk', B + r'acakkhuk', r'आँख से रहित'),
    ('saghānak', B + r'saghānak', r'नाक वाल'),
    ('aghānak', B + r'aghānak', r'नाक से रहित'),
    ('sasotak', B + r'sasotak', r'कान वाल'),
    ('asotak', B + r'asotak', r'कान से रहित'),
    ('sacittak', B + r'sacittak', r'मन वाल'),
    ('acittak', B + r'acittak', r'मन से रहित'),
    ('sahetuk', B + r'sahetuk', r'मूल वाल'),
    ('ahetuk', B + r'ahetuk', r'मूल से रहित'),
    ('pacchimabhavik', r'pacchimabhavik', r'अंतिम जन्म वाल'),
    ('rūpāvacar', B + r'rūpāvacar', r'(?<!अ)(?<!अ\S)सूक्ष्म भौतिक लोक|(?<=या )अभौतिक'),  # placeholder adjusted below
    ('arūpa', B + r'arūp', r'अभौतिक लोक'),
    ('kāmāvacar', B + r'kāmāvacar', r'इंद्रिय-सुखों के लोक'),
    ('pañcavokār', r'pañcavokār', r'पाँच समूहों'),
    ('catuvokār', r'catuvokār', r'चार (या पाँच )?समूहों'),
    ('suddhāvās', r'suddhāvās', r'शुद्ध निवास'),
    ('nirodhasamāpann', r'nirodhasamāpann', r'समाप्ति'),
    ('pacchimacittasamaṅgī', r'pacchimacittasamaṅgī', r'अंतिम मन से युक्त'),
    ('bhaṅgakkhaṇe', r'bhaṅgakkhaṇe', r'भंग होने के क्षण'),
    ('uppādakkhaṇe', r'uppādakkhaṇe', r'उत्पन्न होने के क्षण'),
    ('pavatte', r'pavatte', r'जीवन के दौरान'),
    ('vinā', B + r'vinā', r'के बिना'),
    ('sampayutt', r'sampayutt', r'से जुड़'),
    ('vippayutt', r'vippayutt', r'से अलग'),
    ('sabbesaṃ', B + r'sabbesaṃ', r'सभी'),
    ('itaresaṃ', B + r'itaresaṃ', r'बाकी'),
    ('eteneva', r'eteneva bhāvena', r'इसी लिंग में'),
    ('anantarā', r'anantarā', r'के ठीक बाद'),
    ('upapatticitt', r'upapatticitt', r'जन्म के मन'),
    ('dutiye citte', r'dutiye citte vattamāne', r'दूसरे मन के चलते समय'),
    ('ñāṇa', 'ñāṇa', r'ज्ञान से'),
    ('somanassena', r'somanassena', r'प्रसन्नता के (साथ|बिना)'),
    ('upekkhāya', r'upekkhāya', r'समभाव के (साथ|बिना)'),
]
idre = re.compile(r'\s*\^(6-[\d-]+)\s*$')

def cnt_rupa_h(h):
    # 'सूक्ष्म भौतिक लोक' occurrences (not preceded by अ since अभौतिक differs) + 'सूक्ष्म भौतिक लोक या अभौतिक' counts once each
    return len(re.findall(r'सूक्ष्म भौतिक', h))

def cnt_arupa_h(h):
    return len(re.findall(r'अभौतिक', h))

def cnt_arupa_p(p):
    return len(re.findall(B + r'arūp', p, re.I))

out = []
for fn in FILES:
    pl, hl = load(fn)
    for i, (p, h) in enumerate(zip(pl, hl), 1):
        if p.startswith('#'):
            continue
        p = unicodedata.normalize('NFC', idre.sub('', p))
        h = idre.sub('', h)
        diffs = []
        for name, pre, hre in T:
            if name == 'rūpāvacar':
                pc, hc = len(re.findall(pre, p, re.I)), cnt_rupa_h(h)
            elif name == 'arūpa':
                pc, hc = cnt_arupa_p(p), cnt_arupa_h(h)
            else:
                pc, hc = len(re.findall(pre, p, re.I)), len(re.findall(hre, h))
            if name == 'itthī/yo':
                pc -= len(re.findall(B + r'na itthīnaṃ', p, re.I)) * 0
            if pc != hc:
                diffs.append(f'{name}:{pc}/{hc}')
        if diffs:
            out.append((fn, i, diffs))
for fn, i, d in out:
    print(fn[:5], i, ' '.join(d))
print(len(out))
