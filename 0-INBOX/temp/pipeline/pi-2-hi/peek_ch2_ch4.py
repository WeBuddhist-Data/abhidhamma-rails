# -*- coding: utf-8 -*-
"""Helper (read-only): show short context around a pattern in another Hindi chapter, for consistency checks."""
import re, sys
D = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi\pi-2-hindi-plain-zeroshot_split_chapters"
name, pat = sys.argv[1], sys.argv[2]
w = int(sys.argv[3]) if len(sys.argv) > 3 else 80
txt = open(f"{D}\\{name}", encoding="utf-8").read()
seen = set()
for m in re.finditer(pat, txt):
    s = txt[max(0, m.start() - w): m.end() + w].replace("\n", " / ")
    if s not in seen:
        seen.add(s)
        print("…" + s + "…")
    if len(seen) >= 4:
        break
