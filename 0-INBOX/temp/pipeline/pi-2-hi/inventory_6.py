# -*- coding: utf-8 -*-
"""Inventory of sentence types in chapter 6 (helper for build_6-paticcasamuppadavibhango_hi.py)."""
import re, collections
P = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\pali\pi-2_split_chapters\6-paticcasamuppadavibhango.md"
ID = re.compile(r"\s*\^[0-9A-Za-z-]+\s*$")
c = collections.Counter()
opens = collections.Counter()
for line in open(P, encoding="utf-8"):
    line = ID.sub("", line.rstrip("\n"))
    if not line.strip() or line.startswith("#"):
        continue
    for s in re.split(r"(?<=[?.])\s+", line):
        if "tasmiṃ samaye" in s.lower():
            head, _, _ = s.partition(", tasmiṃ samaye ")
            opens[head] += 1
            continue
        s2 = re.sub(r"^Tattha katam\S+ ", "Q ", s)
        c[s2] += 1
for k, v in sorted(opens.items()):
    print(v, "OPEN", k)
print("-----")
for k, v in sorted(c.items()):
    print(v, k)
