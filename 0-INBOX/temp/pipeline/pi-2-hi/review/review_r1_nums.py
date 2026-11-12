import re, sys
exec(open(r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-hi\review\review_r1_align.py', encoding='utf-8').read().split("mode = sys.argv")[0])
PN = {'eka': 'एक', 'du': 'दो', 'ti': 'तीन', 'catub': 'चार', 'pañca': 'पाँच', 'chab': 'छह', 'satta': 'सात', 'aṭṭha': 'आठ', 'nava': 'नौ', 'dasa': 'दस', 'ekādasa': 'ग्यारह', 'bahu': 'अनेक'}
for i, (p, h) in enumerate(zip(pl, hl), 1):
    a = [PN.get(x.lower(), '?' + x) for x in re.findall(r'(\w+?)vidhena', p)]
    b = re.findall(r'(\S+) प्रकार से', h)
    if a != b: print(i, pid(p), a, b)
# other number words
NW = r'\b(eka|eko|ekaṃ|dve|dvi|tayo|tīṇi|tisso|cattāro|cattāri|catasso|pañca|cha|satta|aṭṭha|nava|dasa)\b'
HW = r'(एक|दो|तीन|चार|पाँच|छह|सात|आठ|नौ|दस|ग्यारह)'
for i, (p, h) in enumerate(zip(pl, hl), 1):
    a = len(re.findall(NW, p, re.I)); b = len(re.findall(HW, h))
    if a != b and i > 62: print('NUMW', i, pid(p), a, b)
