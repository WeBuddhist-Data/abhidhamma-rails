import re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from review_r4_struct_lib import *

MASC = ['समूह', 'आधार', 'तापमान', 'भोजन', 'निवास-स्थान', 'राग', 'मोह', 'इरादा', 'इरादे', 'मार्ग', 'फल',
        'शरीर', 'कान', 'महाभूत', 'सदाचार', 'मूल', 'मन', 'द्वेष', 'अहंकार', 'संशय', 'भौतिक रूप', 'दृश्य रूप',
        'स्वाद', 'स्पर्श', 'गंध', 'ध्वनि', 'त्याग', 'कर्म', 'इंद्रिय-क्षेत्र', 'जल तत्व', 'पुनर्जन्म']
FEM = ['परिघटना', 'परिघटनाएँ', 'परिघटनाओं', 'प्रधानता', 'आँख', 'जीभ', 'नाक', 'श्रद्धा', 'प्रज्ञा', 'दृष्टि',
       'चेतना', 'उदासी', 'बेचैनी', 'कामना', 'क्षमता', 'ध्यान-अवस्था', 'जीवन-क्षमता']
# feminine adjective endings directly before masculine noun
adjf = r'(?:वाली|चुकी|हुई|की|होने वाली|अतीत की|निश्चित)'
rx1 = re.compile(r'(\S*(?:वाली|चुकी|हुई)) (' + '|'.join(re.escape(m) for m in MASC) + r')(?=[\s,।…)?]|$)')
rx2 = re.compile(r'(\S*(?:वाला|वाले|चुका|चुके|हुआ|हुए)) (' + '|'.join(re.escape(m) for m in FEM) + r')(?=[\s,।…)?]|$)')
# genitive की/के before masculine/feminine in 2-13 style items
rx3 = re.compile(r'(?:अतीत|भविष्य|वर्तमान) (की) (' + '|'.join(re.escape(m) for m in MASC) + r')(?=[\s,।…)?]|$)')
rx4 = re.compile(r'(?:अतीत|भविष्य|वर्तमान) (का|के) (' + '|'.join(re.escape(m) for m in FEM) + r')(?=[\s,।…)?]|$)')
# verb agreement: परिघटना ... होता है / परिघटनाएँ होती है
rx5 = re.compile(r'परिघटना,? [^।–]*?(?:के लिए|के रूप में) कारण होता है')
rx6 = re.compile(r'परिघटनाएँ[^।–]*? उत्पन्न होती है(?!ं)')
rx7 = re.compile(r'परिघटना [^।–]*? उत्पन्न होती हैं')
for f in FILES:
    H = nonempty(load(os.path.join(HI, f)))
    for n, (_, h) in enumerate(H, 1):
        for rx, tag in ((rx1, 'F-adj+M-noun'), (rx2, 'M-adj+F-noun'), (rx3, 'की+M'), (rx4, 'का/के+F'), (rx5, 'परिघटना..होता'), (rx6, 'परिघटनाएँ..होती है'), (rx7, 'परिघटना..होती हैं')):
            for m in rx.finditer(h):
                s = max(0, m.start() - 30)
                print(f[:4], n, tag, '|', h[s:m.end() + 15])
