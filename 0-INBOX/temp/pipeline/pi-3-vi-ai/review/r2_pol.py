# r2 helper: polarity check for ch7 answers (console only).
import re, os
P = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation\pali\pi-3_split_chapters\7-chatthanayo.md'
V = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation\vietnamese\pi-3-vietnamese-plain-rails_split_chapters\7-chatthanayo.md'
def segs(path):
    out, buf = [], []
    for line in open(path, encoding='utf-8').read().split('\n'):
        if line.strip(): buf.append(line)
        m = re.search(r'\^(3-\d+)\s*$', line)
        if m: out.append((m.group(1), buf[0] if buf else '')); buf = []
    return out
NUM = r'(?:một|hai|ba|bốn|sáu|bảy|mười)\b'
for (i, p), (j, v) in zip(segs(P), segs(V)):
    # sequence of answer polarity in Pali: S / V for count-bearing answers, kS / kV for kehici
    pa = []
    for m in re.finditer(r'(kehici )?(sampayutt|vippayutt)\w*', p):
        pre = p[max(0, m.start() - 25):m.start()]
        if re.search(r'(dhātūhi|dhātuyā|khandhehi|khandhena|āyatanehi|āyatanena) $', pre) or m.group(1):
            pa.append(('k' if m.group(1) else '') + m.group(2)[0].upper())
    va = []
    for m in re.finditer(r'(không )?gắn liền với (một số hiện tượng thuộc )?' + NUM, v, re.I):
        va.append(('k' if m.group(2) else '') + ('V' if m.group(1) else 'S'))
    if pa != va:
        print(i, 'P', pa, 'V', va)
print('done')
