import re, sys, collections
sys.path.insert(0, r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\review')
from review_r8_common import load
p, h, ids = load()
PH = [
    (r'mūlaṃ kātabbaṃ', 'मूल वाक्य बनाना चाहिए'),
    (r'mūlaṃ pucchitabbaṃ', 'मूल वाक्य पूछना चाहिए'),
    (r'\banulomaṃ\.', 'सकारात्मक क्रम।'),
    (r'\bpaccanīyaṃ\.', 'नकारात्मक क्रम।'),
    (r'anulomapaccanīyaṃ\.', 'सकारात्मक-नकारात्मक क्रम।'),
    (r'paccanīyānulomaṃ\.', 'नकारात्मक-सकारात्मक क्रम।'),
    (r'paṭiccasadis', 'निर्भरता के खंड के समान'),
    (r'ninnānākaraṇ|ninnānaṃ|ninnānā\b', 'बिना किसी अंतर के'),
    (r'niṭṭhitaṃ', 'समाप्त'),
    (r'\bcakkaṃ', 'चक्र'),
    (r'saṃkhittaṃ', 'संक्षिप्त'),
    (r'sahajātā\b|sahajātaṃ\b|sahajāto\b', 'सह-उत्पत्ति'),
    (r'nānākkhaṇik', 'भिन्न क्षण'),
    (r'pakatūpanissay', 'स्वाभाविक प्रबल आश्रय'),
    (r'ārammaṇūpanissay', 'विषय रूपी प्रबल आश्रय'),
    (r'anantarūpanissay', 'निकटता रूपी प्रबल आश्रय'),
    (r'ārammaṇādhipati', 'विषय रूपी प्रधानता'),
    (r'sahajātādhipati', 'सह-उत्पत्ति रूपी प्रधानता'),
    (r'ārammaṇapurejāt', 'विषय रूपी पूर्व-उत्पत्ति'),
    (r'vatthupurejāt', 'आधार रूपी पूर्व-उत्पत्ति'),
    (r'ghaṭan', 'संयोजन'),
    (r'āmasan', 'उल्लेख'),
    (r'gaṇan', 'गणना'),
    (r'\bpañh', 'प्रश्न'),
]
for pk, hk in PH:
    tot = [0, 0]; bad = []
    for i, (a, b) in enumerate(zip(p, h)):
        if a.startswith('#'):
            continue
        x = len(re.findall(pk, a.lower())); y = b.count(hk)
        tot[0] += x; tot[1] += y
        if x != y:
            bad.append(f'{i+1}:{x}/{y}')
    print(pk, tot, ' '.join(bad[:40]))
