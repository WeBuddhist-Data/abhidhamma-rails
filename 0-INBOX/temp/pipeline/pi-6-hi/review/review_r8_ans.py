import sys, re
sys.path.insert(0, r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-hi\review')
from review_r8_check import load, FILES
for f in FILES:
    P, H = load(f)
    for i,(p,h) in enumerate(zip(P,H)):
        a = len(re.findall(r'\?\s*No\.', p)); b = len(re.findall(r'\?\s*नहीं।', h))
        c = len(re.findall(r'\?\s*(Uppajj\w+|Parij\w+|Pajah\w+|Bhāv\w+|Sacchi\w+)\.', p)); d2 = len(re.findall(r'\?\s*(उत्पन्न|पूरी तरह|छोड़|अभ्यास|साक्षात्कार)[^?।]*।', h))
        if a != b or c != d2:
            print(f, i+1, a, b, c, d2, '|', p[-80:], '|', h[-80:])
