"""r2 reviewer: list Pali-looking tokens outside [...] brackets, and quote/period patterns (console only).
usage: python -I -X utf8 r2_latin.py <vi_ch.md>
"""
import re, sys
t = open(sys.argv[1], encoding='utf-8').read()
nob = re.sub(r'\[[^\]]*\]', '', t)
pali = re.findall(r'\b\w*[āīūṃṅñṭḍṇḷ]\w*\b', nob)
print('pali-like tokens outside brackets:', sorted(set(pali)))
for m in re.finditer(r'[?!]” [A-ZĐ]', t):
    ln = t.count('\n', 0, m.start()) + 1
    print('quote-end without period, line', ln, repr(t[m.start()-30:m.end()+10]))
for m in re.finditer(r'”[!?]', t):
    ln = t.count('\n', 0, m.start()) + 1
    print('punct after quote, line', ln, repr(t[m.start()-30:m.end()+5]))
for m in re.finditer(r'\?\s', t):
    pass
qs = re.findall(r'([^.?!”]*\?)', t)
bad = [q.strip() for q in qs if not re.search(r'\b(gì|nào|ai|sao|bao giờ|không|vì sao|những ai|là gì)\b', q)]
print('questions without question word:', bad[:10])
