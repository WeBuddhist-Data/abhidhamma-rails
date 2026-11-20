"""Scratch: where the nāma / rūpa members (Tattha katamaṃ rūpaṃ? / vuccati "rūpaṃ" / Atthi nāmaṃ, atthi rūpaṃ /
idañca rūpaṃ) occur in pi-2 and how the Vietnamese renders them.

usage: python -I -X utf8 probe_namarupa_vi.py [--bak]
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vi_common
from vi_common import PARTS, pairs

if "--bak" in sys.argv:
    vi_common.CUR["vdir"] = vi_common.BAK
PP = [r"Tattha katamaṃ rūpaṃ\?", r'vuccati "rūpaṃ"', r"Atthi nāmaṃ, atthi rūpaṃ", r"idañca rūpaṃ"]
VV = ["Ở đây, vật chất là gì?", "đó được gọi là “vật chất”", "Có phần tinh thần, có vật chất", "đây là vật chất",
      "Ở đây, phần vật chất là gì?", "đó được gọi là “phần vật chất”", "Có phần tinh thần, có phần vật chất",
      "đây là phần vật chất"]
tot = [0] * len(PP)
for part in PARTS:
    for k, (p, v) in enumerate(pairs(part)):
        a = [len(re.findall(x, p)) for x in PP]
        if any(a):
            b = [v.count(x) for x in VV]
            tot = [x + y for x, y in zip(tot, a)]
            print(part[:3], k + 1, "P", a, "V old", b[:4], "new", b[4:], "| nāma in line:", "nāmaṃ" in p)
print("Pāli totals", tot)
