import re, sys, collections
sys.path.insert(0, r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\review')
from review_r8_common import load
p, h, ids = load()
R = {
    'Kilesadukaṃ': (r'\bnokiles', r'(?<![a-zāīūṃṅñṭḍṇḷ])kiles', r'मन के क्लेश रूपी न होने', r'मन के क्लेश(?! रूपी न होने)'),
    'Saṃkiliṭṭhadukaṃ': (r'asaṃkiliṭṭh', r'(?<![a])saṃkiliṭṭh', r'क्लेशों से मलिन न होने', r'क्लेशों से मलिन(?! न होने)'),
    'Dassanenapahātabbadukaṃ': (r'nadassanena', r'(?<!na)dassanena', r'सत्य-दर्शन से न छोड़', r'सत्य-दर्शन से छोड़'),
    'Bhāvanāyapahātabbadukaṃ': (r'nabhāvanāya', r'(?<!na)bhāvanāya', r'मानसिक अभ्यास से न छोड़', r'मानसिक अभ्यास से छोड़'),
    'Dassanenapahātabbahetukadukaṃ': (r'nadassanena pahātabbahetuk', r'(?<!na)dassanena pahātabbahetuk', r'सत्य-दर्शन से छोड़े जाने वाले मूलों से रहित', r'सत्य-दर्शन से छोड़े जाने वाले मूलों वाल'),
    'Bhāvanāyapahātabbahetukadukaṃ': (r'nabhāvanāya pahātabbahetuk', r'(?<!na)bhāvanāya pahātabbahetuk', r'मानसिक अभ्यास से छोड़े जाने वाले मूलों से रहित', r'मानसिक अभ्यास से छोड़े जाने वाले मूलों वाल'),
    'Savitakkadukaṃ': (r'\bavitakk', r'\bsavitakk', r'आरंभिक विचार से रहित', r'आरंभिक विचार वाल'),
    'Savicāradukaṃ': (r'\bavicār', r'\bsavicār', r'सतत विचार से रहित', r'सतत विचार वाल'),
    'Sappītikadukaṃ': (r'\bappītik', r'\bsappītik', r'उल्लास से रहित', r'उल्लास वाल'),
    'Pītisahagatadukaṃ': (r'napītisahagat', r'(?<!na)pītisahagat', r'उल्लास के साथ न होने', r'उल्लास के साथ होने'),
    'Sukhasahagatadukaṃ': (r'nasukhasahagat', r'(?<!na)sukhasahagat', r'सुख के साथ न होने', r'सुख के साथ होने'),
    'Upekkhāsahagatadukaṃ': (r'naupekkhāsahagat', r'(?<!na)upekkhāsahagat', r'समभाव के साथ न होने', r'समभाव के साथ होने'),
    'Kāmāvacaradukaṃ': (r'nakāmāvacar', r'(?<!na)kāmāvacar', r'इंद्रिय-सुखों के लोक से संबंधित न होने', r'इंद्रिय-सुखों के लोक से संबंधित(?! न होने)'),
    'Rūpāvacaradukaṃ': (r'narūpāvacar', r'(?<![na])rūpāvacar', r'सूक्ष्म भौतिक लोक से संबंधित न होने', r'सूक्ष्म भौतिक लोक से संबंधित(?! न होने)'),
    'Arūpāvacaradukaṃ': (r'naarūpāvacar', r'(?<![na])arūpāvacar', r'अभौतिक लोक से संबंधित न होने', r'अभौतिक लोक से संबंधित(?! न होने)'),
    'Niyyānikadukaṃ': (r'aniyyānik', r'(?<!a)niyyānik', r'मुक्ति की ओर न ले जाने', r'मुक्ति की ओर ले जाने'),
    'Niyatadukaṃ': (r'aniyat', r'(?<!a)niyat', r'अनिश्चित', r'(?<!अ)निश्चित'),
    'Saraṇadukaṃ': (r'(?<![a-zāīūṃṅñṭḍṇḷ])araṇ', r'(?<![a-zāīūṃṅñṭḍṇḷ])saraṇ', r'संघर्ष से रहित', r'संघर्ष वाल'),
}
dyad = None
out = collections.defaultdict(list)
for i, (a, b) in enumerate(zip(p, h)):
    if a.startswith('#') and 'dukaṃ' in a and not a.startswith('#######'):
        dyad = a.split(' ')[1]; continue
    if a.startswith('#') or dyad not in R:
        continue
    pn, pp_, hn, hp = R[dyad]
    A = a.lower()
    c = (len(re.findall(pn, A)), len(re.findall(pp_, A)), len(re.findall(hn, b)), len(re.findall(hp, b)))
    if c[0] != c[2] or c[1] != c[3]:
        out[dyad].append((i + 1, c))
for d, v in out.items():
    print(d, len(v), ' '.join(f'{l}:{c}' for l, c in v))
