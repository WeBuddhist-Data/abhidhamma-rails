"""Line-level item counts: Pāli term occurrences vs Vietnamese rendering occurrences on the aligned line.

usage: python -I -X utf8 count_items_vi.py [--bak]
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vi_common
from vi_common import PARTS, pairs, VAR

ITEMS = [
    (r"sammāvāyām|sammappadhān", "nỗ lực đúng đắn"),
    (r"sammāsati", "tỉnh thức đúng đắn"),
    (r"sammāsamādh", "định tâm đúng đắn"),
    (r"sammādiṭṭh", "quan điểm đúng đắn"),
    (r"vīriyabal|viriyabal", "sức mạnh tinh tấn"),
    (r"satibal", "sức mạnh tỉnh thức"),
    (r"samādhibal", "sức mạnh định tâm"),
    (r"paññābal", "sức mạnh trí tuệ"),
    (r"vīriyindriy|viriyindriy", "năng lực tinh tấn"),
    (r"satindriy", "năng lực tỉnh thức"),
    (r"samādhindriy", "năng lực định tâm"),
    (r"paññindriy", "năng lực trí tuệ"),
    (r"maggaṅgaṃ", "chi phần của con đường"),
    (r"maggapariyāpann|maggariyāpann", "nằm trong con đường"),
]

if "--bak" in sys.argv:
    vi_common.CUR["vdir"] = vi_common.BAK
n = 0
for part in PARTS:
    for k, (p, v) in enumerate(pairs(part)):
        pc, vc = VAR.sub("", p), VAR.sub("", v)
        for rp, rv in ITEMS:
            a, b = len(re.findall(rp, pc)), vc.lower().count(rv)
            if a != b:
                n += 1
                print(f"{part} line {k + 1}: {rp} x{a} vs «{rv}» x{b}")
print("count mismatches:", n)
