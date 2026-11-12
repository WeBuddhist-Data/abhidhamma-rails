import re
base = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation'
ch = '6-paticcasamuppadavibhango'
P = [l for l in open(base + r'\pali\pi-2_split_chapters\%s.md' % ch, encoding='utf-8').read().split('\n') if l.strip()]
H = [l for l in open(base + r'\hindi\pi-2-hindi-plain-rails_split_chapters\%s.md' % ch, encoding='utf-8').read().split('\n') if l.strip()]
pmap = [('kusalamūla', 'KM'), ('akusalamūla', 'AM'), ('avijjā', 'A'), ('saṅkhāra', 'S'), ('viññāṇa', 'V'), ('nāmarūpa', 'NR'), ('nāma', 'N'),
        ('chaṭṭhāyatana', 'C6'), ('saḷāyatana', 'S6'), ('phassa', 'P'), ('vedanā', 'VE'), ('taṇhā', 'T'), ('upādāna', 'U'),
        ('adhimokkha', 'AD'), ('pasāda', 'PA'), ('paṭigha', 'PT'), ('vicikicchā', 'VI'), ('uddhacca', 'UD'), ('bhava', 'B'), ('jāti', 'J')]
hmap = [('हानिकर मूलों', 'AM'), ('हितकर मूलों', 'KM'), ('अज्ञान', 'A'), ('मानसिक रचनाओं', 'S'), ('चेतना', 'V'), ('मानसिक पक्ष और भौतिक रूप', 'NR'), ('मानसिक पक्ष', 'N'),
        ('छठे इंद्रिय-क्षेत्र', 'C6'), ('छह इंद्रिय-क्षेत्रों', 'S6'), ('संपर्क', 'P'), ('अनुभूति', 'VE'), ('तृष्णा', 'T'), ('आसक्ति', 'U'),
        ('निश्चय', 'AD'), ('आस्था', 'PA'), ('चिढ़', 'PT'), ('संशय', 'VI'), ('बेचैनी', 'UD'), ('अस्तित्व', 'B'), ('जन्म', 'J')]
def pcodes(s):
    out = []
    for m in re.finditer(r'(\w+?)paccayā(pi)?\b', s):
        w = m.group(1)
        for k, c in pmap:
            if w == k or w == k[:-1] or w.startswith(k) and len(w) - len(k) <= 1:
                out.append(c + ('*' if m.group(2) else '')); break
        else:
            out.append('?' + w)
    return out
def hcodes(s):
    out = []
    for m in re.finditer(r'([\u0900-\u097F\- ]+?) के कारण( भी)?', s):
        w = m.group(1).strip()
        # take the longest suffix that matches
        for k, c in hmap:
            if w.endswith(k):
                out.append(c + ('*' if m.group(2) else '')); break
        else:
            out.append('?' + w[-15:])
    return out
n = 0
for i, (p, h) in enumerate(zip(P, H), 1):
    a, b = pcodes(p), hcodes(h)
    if a != b:
        n += 1
        print(i, p[-12:].strip(), '\n P', a, '\n H', b)
print('mismatches', n)
