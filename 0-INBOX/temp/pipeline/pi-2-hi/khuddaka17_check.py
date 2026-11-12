# -*- coding: utf-8 -*-
"""Extra checks for chapter 17: Latin words outside brackets (ignoring block IDs), CR, double blanks,
forbidden words, ':-', em dash."""
import re, sys
p = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi\pi-2-hindi-plain-zeroshot_split_chapters\17-khuddakavatthuvibhango.md"
t = open(p, encoding="utf-8", newline="").read()
errs = []
for n, line in enumerate(t.split("\n"), 1):
    s = re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", line)
    s = re.sub(r"\[[^\]]*\]", "", s)
    for w in re.findall(r"[A-Za-zĀ-ž\u1E00-\u1EFF]+", s):
        errs.append((n, w))
    for bad in ("धर्म", "seed", "—", ":-"):
        if bad in line:
            errs.append((n, bad))
if "\r" in t:
    errs.append("CR")
if "\n\n\n" in t:
    errs.append("double blank")
print("extra checks", "OK" if not errs else errs[:20])
