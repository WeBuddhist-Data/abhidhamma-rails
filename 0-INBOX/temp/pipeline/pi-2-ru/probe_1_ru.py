# -*- coding: utf-8 -*-
"""Probe for build_1_ru.py: compare the saññā / saṅkhāra / viññāṇa Abhidhammabhājanīya blocks with the vedanā block."""
import difflib, re, sys
P = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\pali\pi-2_split_chapters\1-khandhavibhango.md"
L = open(P, encoding="utf-8").read().split("\n")
# 0-based ranges of the sections (file lines 120..251, 252..392, 393..532, 533..671)
secs = {"vedana": (119, 251), "sanna": (251, 392), "sankhara": (392, 532), "vinnana": (532, 671)}
def norm(lines, name):
    out = []
    for l in lines:
        l = re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", l)
        l = l.replace(name, "X")
        out.append(l)
    return out
names = {"vedana": "vedanā", "sanna": "saññā", "sankhara": "saṅkhāra", "vinnana": "viññāṇa"}
base = norm(L[slice(*secs["vedana"])], "vedanā")
for k in ("sanna", "sankhara", "vinnana"):
    other = norm(L[slice(*secs[k])], names[k])
    print("=" * 30, k)
    for d in difflib.unified_diff(base, other, lineterm="", n=0):
        print(d[:2000])
