import sys, re
sys.path.insert(0, r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\review')
from review_r7_common import *
from collections import Counter

praw, pl = load(P)
hraw, hl = load(H)
S = segs(pl)
W = r'(?<![\wāīūṃṅñṭḍṇḷ])'
PAIRS = [
 ('khandha', W + r'khandh', r'समूह'),
 ('mahabhuta', r'mahābhūt', r'महाभूत'),
 ('cittasamutthana', r'citta(?:saṃsaṭṭha)?samuṭṭhān', r'मन से उत्पन्न'),
 ('katatta', r'kaṭattā', r'किए गए कर्म से उत्पन्न'),
 ('upadarupa', r'upādārūp', r'व्युत्पन्न भौतिक रूप'),
 ('patisandhi', r'paṭisandhi', r'पुनर्जन्म'),
 ('vatthu', W + r'vatth', r'आधार'),
 ('ahetuka', r'ahetuk', r'मूल से रहित'),
 ('asannasatta', r'asaññasatt', r'पहचान-रहित'),
 ('moha', W + r'moh', r'मोह'),
 ('vicikiccha', r'vicikicch', r'संशय'),
 ('uddhacca', r'uddhacc', r'बेचैनी'),
 ('cakkhu', W + r'cakkh', r'आँख'),
 ('kaya', W + r'kāy(?!ik)', r'शरीर'),
 ('aharasam', r'āhārasamuṭṭhān', r'आहार से उत्पन्न'),
 ('utusam', r'utusamuṭṭhān', r'तापमान से उत्पन्न'),
 ('kabalikara', r'kabaḷīkār', r'कौर-कौर'),
 ('jivitindriya', r'jīvitindriy', r'जीवन-क्षमता'),
 ('cetana', W + r'cetan', r'इराद'),
 ('nibbana', r'nibbān', r'निर्वाण'),
 ('sampayuttaka', r'sampayuttak', r'जुड़े हुए'),
 ('avajjana', r'āvajjan', r'मोड़'),
 ('vipaka', r'vipāk', r'कर्म-फल'),
 ('ajjhattika', r'ajjhattik', r'आंतरिक'),
 ('bahira', W + r'bāhir', r'बाह्य'),
 ('domanassa', r'domanass', r'उदासी'),
 ('raga', W + r'rāg', r'राग'),
 ('ditthi', W + r'diṭṭh', r'दृष्टि'),
 ('jhana', r'jhān', r'ध्यान'),
 ('magga', W + r'magg', r'मार्ग'),
 ('phala', W + r'phal', r'(?<!कर्म-)फल'),
 ('gotrabhu', r'gotrabh', r'गोत्र-परिवर्तन'),
 ('pacchajata', r'pacchājāt', r'पश्चात्-उत्पत्ति|बाद में उत्पन्न'),
 ('purejata', r'purejāt', r'पूर्व-उत्पत्ति|पहले उत्पन्न'),
 ('sahajata', r'sahajāt', r'सह-उत्पत्ति'),
 ('nanakkhanika', r'nānākkhaṇik', r'भिन्न क्षण'),
 ('upanissaya', r'upanissay|upanissāya', r'प्रबल आश्रय'),
 ('saddha', W + r'saddh', r'श्रद्धा'),
 ('panna', W + r'paññ', r'प्रज्ञा'),
 ('sila', W + r'sīl', r'सदाचार'),
 ('dana', W + r'dān', r'दान'),
 ('kilesa', r'kiles', r'क्लेश'),
 ('iddhividha', r'iddhividh', r'अलौकिक'),
 ('cetopariya', r'cetopariy', r'दूसरों के मन'),
 ('pubbenivasa', r'pubbenivās', r'पूर्व जन्म'),
 ('anagatamsa', r'anāgataṃs', r'भविष्य'),
 ('yathakammupaga', r'yathākammūpag', r'कर्मों के अनुसार'),
 ('sota', W + r'sot|saddaṃ', r'कान|ध्वनि'),
 ('rupayatana', r'rūpāyatan', r'दृश्य रूप का'),
 ('photthabba', r'phoṭṭhabb', r'स्पर्श'),
 ('akasananca', r'ākāsānañc', r'अनंत आकाश'),
 ('akincanna', r'ākiñcaññ', r'कुछ भी न होने'),
 ('nevasanna', r'nevasaññ', r'न पहचान न अ-पहचान'),
 ('vinnananca', r'viññāṇañc', r'अनंत चेतना'),
 ('utu', W + r'utu', r'तापमान'),
 ('bhojana', r'bhojan', r'भोजन'),
 ('senasana', r'senāsan', r'निवास-स्थान'),
 ('sankha', r'saṅgh', r'संघ'),
 ('pana', W + r'pāṇ', r'जीव की हत्या'),
 ('nirodha', r'nirodh', r'निरोध'),
 ('sukha', r'sukh', r'सुख'),
 ('dukkha', W + r'dukkh', r'दुःख'),
 ('anuloma', r'anulom', r'अनुरूपता|सकारात्मक'),
 ('vodana', r'vodān', r'शुद्धि'),
 ('vutthana', r'vuṭṭhān', r'बाहर आने'),
 ('manodhatu', r'manodhāt', r'मन के तत्व|मन का तत्व'),
 ('manovinnanadhatu', r'manoviññāṇadhāt', r'मन की चेतना के तत्व|मन की चेतना का तत्व'),
 ('hadaya', r'hadaya', r'हृदय'),
 ('itthindriya', r'itthindriy', r'स्त्री'),
 ('purisindriya', r'purisindriy', r'पुरुष'),
 ('sadda', W + r'sadd(?!h)', r'ध्वनि'),
 ('sankhitta', r'saṃkhitt', r'संक्षिप्त'),
 ('ninnanakarana', r'ninnānākaraṇ', r'बिना किसी अंतर'),
]

res = Counter()
for ((n, i, p), sid), (_, _, h) in zip(S, hl):
    if p.startswith('#'):
        continue
    pt = IDRE.sub('', p); ht = IDRE.sub('', h)
    for name, prx, hrx in PAIRS:
        a = len(re.findall(prx, pt, flags=re.I)); b = len(re.findall(hrx, ht))
        if a != b:
            res[name] += 1
            if name in sys.argv[1:] or 'all' in sys.argv[1:]:
                print(name, n, sid, a, b)
print(res.most_common())
