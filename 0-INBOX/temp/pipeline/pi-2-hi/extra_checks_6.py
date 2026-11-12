# -*- coding: utf-8 -*-
"""Extra checks for chapter 6 Hindi: Latin outside variant brackets, quote balance, double blanks, CR, banned words.
usage: python -I -X utf8 extra_checks_6.py
"""
import re
P = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi\pi-2-hindi-plain-zeroshot_split_chapters\6-paticcasamuppadavibhango.md"
t = open(P, encoding="utf-8", newline="").read()
bad = 0
for n, line in enumerate(t.split("\n"), 1):
    s = re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", line)
    s = re.sub(r"\s*\[[^\]]*\]", "", s)
    if re.search(r"[A-Za-zĀ-ž]", s):
        print("latin", n, s[:80]); bad += 1
    if s.count("“") != s.count("”"):
        print("quotes", n); bad += 1
    if re.search(r"\bseed|unseeded|:-|—", line):
        print("banned", n); bad += 1
    if "  " in s:
        print("double space", n); bad += 1
print("CR" if "\r" in t else "no CR", "| double blank" if "\n\n\n" in t else "| no double blank", "| bad", bad)
