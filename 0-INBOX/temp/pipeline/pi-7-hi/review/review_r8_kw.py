import re, sys, collections
sys.path.insert(0, r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\review')
from review_r8_common import load
p, h, ids = load()
KW = [
    (r'khandh', 'समूह'),
    (r'cittasamuṭṭhān', 'मन से उत्पन्न'),
    (r'kaṭattā', 'किए गए कर्म से उत्पन्न'),
    (r'paṭisandhi', 'पुनर्जन्म'),
    (r'vatth(?:u|uṃ|uñca|ū)\b', 'आधार'),
    (r'mahābhūt', 'महाभूत'),
    (r'\blobh', 'लोभ'),
    (r'\bmoh', 'मोह'),
    (r'diṭṭhi', 'दृष्टि'),
    (r'\bth[iī]n', 'आलस्य'),
    (r'uddhacc', 'बेचैनी'),
    (r'ahirik', 'निर्लज्जता'),
    (r'anottapp', 'बुराई के प्रति निडरता'),
    (r'\bdos', 'द्वेष'),
    (r'vicikicch', 'संशय'),
    (r'cetanā', 'इरादा'),
    (r'asaññasatt', 'पहचान-रहित'),
    (r'ahetuk', 'मूल से रहित'),
    (r'\barūpe\b', 'अभौतिक लोक में'),
    (r'vipāk', 'कर्म-फल'),
    (r'āvajjan', 'मोड़'),
    (r'domanass', 'उदासी'),
    (r'\brāg', 'राग'),
    (r'\bmān(?:o|aṃ|assa)\b', 'अहंकार'),
    (r'\bsaddh', 'श्रद्धा'),
    (r'\bsīl', 'सदाचार'),
    (r'\bpaññ', 'प्रज्ञा'),
    (r'senāsan', 'निवास-स्थान'),
    (r'gotrabhu', 'गोत्र-परिवर्तन'),
    (r'vodān', 'शुद्धि'),
    (r'āhārasamuṭṭhān', 'आहार से उत्पन्न'),
    (r'utusamuṭṭhān', 'तापमान से उत्पन्न'),
    (r'pavatt', 'जीवन-काल'),
    (r'\bpīti|\bpītiṃ|\bpītiyā', 'उल्लास'),
    (r'\bvitakk', 'आरंभिक विचार'),
    (r'\bvicār', 'सतत विचार'),
    (r'\bsukh', 'सुख'),
    (r'\bdukkh', 'दुःख'),
    (r'upekkh', 'समभाव'),
    (r'\bmagg', 'मार्ग'),
    (r'phal', 'फल'),
    (r'jhān', 'ध्यान'),
    (r'\bcakkh', 'आँख'),
    (r'abhinandati', 'आनंद'),
    (r'assādeti', 'रस'),
    (r'paccavekkh', 'पुनः विचार'),
    (r'garuṃ', 'महत्व'),
    (r'aniccato', 'अनित्य'),
    (r'\bariy', 'आर्य'),
    (r'sekkh', 'सीखने'),
    (r'puthujjan', 'सामान्य'),
    (r'kusal', 'हितकर'),
    (r'akusal', 'हानिकर'),
    (r'sampayuttak', 'जुड़े'),
    (r'purimā', 'पहले'),
    (r'pacchimā', 'बाद'),
    (r'vuṭṭhān', 'बाहर आ'),
    (r'kabaḷīkār', 'आहार'),
    (r'jīvitindriy', 'जीवन'),
    (r'\bnirodh', 'निरोध'),
    (r'nevasaññ', 'न-संज्ञा'),
    (r'ākiñcaññ', 'आकिंचन्य'),
    (r'viññāṇañc', 'चेतना'),
    (r'ākāsānañc', 'आकाश'),
    (r'\bdān', 'दान'),
    (r'uposath', 'उपवास'),
    (r'nibbān', 'निर्वाण'),
    (r'cetopariy', 'मन'),
    (r'iddhividh', 'ऋद्धि'),
    (r'pubbenivās', 'पूर्व'),
    (r'yathākammūpag', 'कर्म'),
    (r'anāgataṃs', 'भविष्य'),
    (r'sotadhāt', 'कान'),
    (r'dibb', 'दिव्य'),
]
res = collections.defaultdict(list)
for i, (a, b) in enumerate(zip(p, h)):
    if a.startswith('#'):
        continue
    A = re.sub(r'\{[^}]*\}', '', a).lower()
    B = re.sub(r'\[[^\]]*\]', '', b)
    for pk, hk in KW:
        na = len(re.findall(pk, A)); nb = B.count(hk)
        if na != nb:
            res[pk].append((i + 1, na, nb))
for pk, v in res.items():
    print('==', pk, len(v), ' '.join(f'{l}:{x}/{y}' for l, x, y in v[:80]))
