"""Inventory of headings, notes and counting lines in 5-05..5-12 (read-only helper)."""
import re, sys, os, collections
ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
PALI = os.path.join(ROOT, "AI_translation", "pali", "pi-7_split_chapters")
FILES = ["5-05-paccaniya-dukatika.md", "5-06-paccaniya-tikaduka.md", "5-07-paccaniya-tikatika.md",
         "5-08-paccaniya-dukaduka.md", "5-09-anulomapaccaniya-tika.md", "5-10-anulomapaccaniya-duka.md",
         "5-11-anulomapaccaniya-dukatika.md", "5-12-anulomapaccaniya-tikaduka.md"]
what = sys.argv[1]
heads, notes, braces = collections.Counter(), collections.Counter(), collections.Counter()
for f in FILES:
    for ln in open(os.path.join(PALI, f), encoding="utf-8").read().split("\n"):
        ln = re.sub(r" \^[0-9A-Za-z-]+\s*$", "", ln)
        if ln.startswith("#"):
            heads[re.sub(r"^#+ ", "", ln)] += 1
            continue
        for m in re.finditer(r"\(([^()]*[^\d().][^()]*)\)", ln):
            notes[m.group(1)] += 1
        for m in re.finditer(r"\{[^}]*\}", ln):
            braces[m.group(0)] += 1
d = {"heads": heads, "notes": notes, "braces": braces}[what]
for k, v in sorted(d.items()):
    print(v, k)
