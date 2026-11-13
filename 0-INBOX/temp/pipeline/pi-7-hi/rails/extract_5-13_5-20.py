"""List heading bodies and parenthetical notes of 5-13..5-20 (helper for build_rails_5-13_5-20.py)."""
import os
import re
import sys

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
PALI = os.path.join(ROOT, "AI_translation", "pali", "pi-7_split_chapters")
FILES = ["5-13-anulomapaccaniya-tikatika.md", "5-14-anulomapaccaniya-dukaduka.md", "5-15-paccaniyanuloma-tika.md",
         "5-16-paccaniyanuloma-duka.md", "5-17-paccaniyanuloma-dukatika.md", "5-18-paccaniyanuloma-tikaduka.md",
         "5-19-paccaniyanuloma-tikatika.md", "5-20-paccaniyanuloma-dukaduka.md"]
what = sys.argv[1]
seen = {}
for f in FILES:
    for ln in open(os.path.join(PALI, f), encoding="utf-8"):
        ln = re.sub(r" \^[0-9A-Za-z-]+\s*$", "", ln.rstrip("\n"))
        if what == "head" and ln.startswith("#"):
            b = re.sub(r"^#+ \*?(?:(?:\d+-)*\d+\. )?", "", ln).rstrip("*")
            seen.setdefault(b, f[:4])
        if what == "note" and not ln.startswith("#"):
            for m in re.finditer(r"\(([^()]*[^\d().][^()]*)\)", ln):
                seen.setdefault(m.group(1), f[:4])
        if what == "brace":
            for m in re.finditer(r"\{[^}]*\}", ln):
                seen.setdefault(m.group(0), f[:4])
for k, v in seen.items():
    print(v, k)
