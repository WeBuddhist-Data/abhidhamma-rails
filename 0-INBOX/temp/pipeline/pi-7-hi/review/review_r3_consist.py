import re, os, sys
from collections import Counter, defaultdict
B = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation'
FILES = ['2-01-vitakkattika.md', '2-02-pitittika.md', '2-03-dassanenapahatabbattika.md',
         '2-04-dassanenapahatabbahetukattika.md', '2-05-acayagamittika.md', '2-06-sekkhattika.md',
         '2-07-parittattika.md', '2-08-parittarammanattika.md']

def load(path):
    with open(path, encoding='utf-8') as f:
        return [l for l in f.read().split('\n') if l.strip()]

P, H = [], []
for f in FILES:
    p = load(os.path.join(B, 'pali', 'pi-7_split_chapters', f)); h = load(os.path.join(B, 'hindi', 'pi-7-hindi-plain-rails_split_chapters', f))
    P += [(f, i + 1, x) for i, x in enumerate(p)]; H += [x for x in h]

# For each Pali key phrase: list Hindi candidates; count lines containing pali phrase and which candidates appear
CHECKS = {
 'sahajāto (vāra)': (r'dhammaṃ sahajāto', ['के साथ जन्म लेकर', 'के साथ उत्पन्न होकर', 'सह-उत्पन्न', 'के साथ उत्पन्न']),
 'saṃsaṭṭho': (r'saṃsaṭṭho', ['घुल-मिल', 'मिश्रित', 'संसृष्ट']),
 'sampayutto (vāra)': (r'dhammaṃ sampayutto', ['से जुड़कर', 'से जुड़ी होकर', 'से जुड़े होकर', 'से संयुक्त']),
 'nissāya': (r'dhammaṃ nissāya', ['पर आश्रित होकर', 'का आश्रय लेकर', 'के आश्रय से', 'पर आश्रित']),
 'taṃ ārabbha': (r'taṃ ārabbha', ['उसे विषय बनाकर', 'उन्हें विषय बनाकर', 'उसको विषय बनाकर']),
 'garuṃ katvā': (r'garuṃ katvā', ['महत्व देकर', 'महत्त्व देकर', 'प्रधान बनाकर']),
 'paccavekkh': (r'paccavekkh', ['पुनः विचार', 'पुनरावलोकन', 'समीक्षा']),
 'assādeti': (r'assād', ['रस ले', 'आस्वाद']),
 'abhinand': (r'abhinand', ['आनंद ले', 'अभिनंदन', 'प्रसन्न']),
 'bhavaṅga': (r'bhavaṅg', ['जीवन-धारा', 'भवंग']),
 'phalasamāpatti': (r'phalasamāpatti', ['फल की ध्यान-अवस्था', 'फल-समापत्ति', 'फल की प्राप्ति']),
 'cuticitta': (r'cuticitt', ['मृत्यु का मन', 'मृत्यु के मन', 'मृत्यु-चित्त', 'च्युति']),
 'upapatticitta': (r'upapatticitt', ['जन्म के मन', 'जन्म का मन', 'उत्पत्ति']),
 'vuṭṭhāna': (r'vuṭṭhān', ['बाहर आने', 'उठने']),
 'anuloma (example)': (r'(?<![a-z])anulom(?:aṃ|añca)\s(?!\()', ['अनुरूपता', 'अनुलोम']),
 'gotrabhu': (r'gotrabhu', ['गोत्र-परिवर्तन', 'गोत्रभू']),
 'vodāna': (r'vodān', ['शुद्धि']),
 'parikamma': (r'parikamm', ['प्रारंभिक तैयारी', 'परिकर्म']),
 'domanassa': (r'domanass', ['उदासी', 'दौर्मनस्य', 'दुःख']),
 'arahā': (r'arah[āa]', ['अर्हत्', 'अर्हंत', 'अरहंत']),
 'puthujjana': (r'puthujjan', ['साधारण व्यक्ति', 'पृथग्जन', 'सामान्य']),
 'cetanā': (r'cetanā', ['इरादा', 'संकल्प', 'चेतना']),
 'vipassati': (r'vipass', ['अंतर्दृष्टि से देख', 'अंतर्दृष्टि']),
 'sekkhā (persons)': (r'Sekkhā|sekkhā', ['सीखने के चरण वाले', 'सीखने वाले']),
 'sīla': (r'(?<![a-z])sīl', ['सदाचार', 'शील']),
 'utu': (r'(?<![a-z])utu', ['तापमान', 'ऋतु', 'मौसम']),
 'bāhira': (r'bāhir', ['बाह्य', 'बाहरी']),
 'asaññasatta': (r'asaññasatt', ['पहचान-रहित', 'असंज्ञ']),
 'kabaḷīkāra': (r'kabaḷīkār', ['कौर-कौर', 'ग्रास']),
 'kilesa': (r'kiles', ['मन के क्लेश', 'क्लेश']),
 'nānākkhaṇikā': (r'nānākkhaṇik', ['भिन्न क्षण', 'भिन्न-क्षण', 'अलग क्षण']),
 'pacchājāta (label)': (r'Pacchājātā\b|pacchājātā\b|pacchājātaṃ', ['पश्चात्-उत्पत्ति', 'बाद में उत्पन्न']),
 'purejātassa imassa kāyassa': (r'purejātassa imassa kāyassa', ['पहले उत्पन्न इस शरीर', 'पहले उत्पन्न हुए इस शरीर']),
 'ninnānaṃ': (r'ninnān', ['बिना किसी अंतर']),
 'saṃkhittaṃ': (r'saṃkhitt', ['संक्षिप्त']),
 'sadisaṃ': (r'sadis', ['के समान', 'जैसा', 'जैसे']),
 'ghaṭanā': (r'ghaṭan', ['संयोजन', 'मेल']),
 'mūlake': (r'mūlake', ['से शुरू होने वाली शृंखला', 'मूल वाले']),
 'tadārammaṇatā': (r'tadārammaṇ', ['उसी विषय को लेकर']),
 'āvajjanā': (r'āvajjan', ['मन को विषय की ओर मोड़']),
 'cittasamaṅgissa': (r'cittasamaṅg', ['मन से युक्त व्यक्ति']),
 'pakatūpanissayo': (r'pakatūpanissay', ['स्वाभाविक प्रबल आश्रय']),
 'upanissāya': (r'upanissāya', ['के प्रबल आश्रय से']),
 'vatthu': (r'vatthu', ['आधार']),
}
for name, (pp, cands) in CHECKS.items():
    cnt = Counter(); lines = 0; miss = []
    for (f, i, p), h in zip(P, H):
        if re.search(pp, p):
            lines += 1
            got = [c for c in cands if c in h]
            for c in got: cnt[c] += 1
            if not got:
                miss.append(f'{f[:4]}:{i}')
    print(f'{name}: lines={lines} {dict(cnt)} miss={miss[:12]}{"..." if len(miss)>12 else ""} ({len(miss)})')
