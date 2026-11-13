import re, sys
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-hi\review")
from review_r3_pairs import load
from review_r3_struct import FILES
from review_r3_check import ITEMS_H, HV

MASC = {"होता", "हुआ", "होगा", "होते", "हुए", "होंगे"}
FEM = {"होती", "हुई", "होगी", "होतीं", "हुईं", "होंगी"}
G = {"D": "m", "S": "m", "N": "m", "M": "m", "K": "f", "V": "f", "C": "f"}
rx = "|".join("(%s)" % a for a, b in ITEMS_H)

for fn in FILES:
    p, h = load(fn)
    for i, b in enumerate(h, 1):
        b2 = re.sub(r"\[[^\]]*\]", "", b)
        its = [(m.start(), [ITEMS_H[k][1] for k in range(len(ITEMS_H)) if m.group(k + 1)][0]) for m in re.finditer(rx, b2)]
        for m in HV.finditer(b2):
            prev = [c for pos, c in its if pos < m.start()]
            if not prev: continue
            g = G[prev[-1]]
            v = m.group(3)
            if (g == "m" and v not in MASC) or (g == "f" and v not in FEM):
                print(fn[:4], i, prev[-1], m.group(0), "|", b2[max(0, m.start() - 60):m.end() + 10])
        # other gender-bearing words after item: भी/नहीं ... है; check 'हुआ था' vs 'हुई थी' pairing
        for m in re.finditer(r"(हुआ|हुई|हुए) (था|थी|थे)", b2):
            if (m.group(1), m.group(2)) not in (("हुआ", "था"), ("हुई", "थी"), ("हुए", "थे")):
                print(fn[:4], i, "AUX", m.group(0))
