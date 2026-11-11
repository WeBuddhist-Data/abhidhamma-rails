"""Termbase lookup for chapters 2-01 (after ^1-57) and 2-02: every Pāli word and n-gram that has an entry."""
import pathlib
import re

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
PALI = ROOT / "AI_translation" / "pali" / "pi-1_split_chapters"
TB = ROOT / "AI_translation" / "hindi" / "pi-1-pali-hindi-termbase-plain.md"
OUT = ROOT / "0-INBOX" / "temp" / "pipeline" / "pi-1-hi" / "rails" / "build_rails_2-01_2-02_lookup.txt"

t1 = (PALI / "2-01-cittuppadakandam.md").read_text(encoding="utf-8")
t1 = t1[t1.index("##### Koṭṭhāsavāro"):]
t2 = (PALI / "2-02-cittuppadakandam.md").read_text(encoding="utf-8")
text = re.sub(r"\^[0-9A-Za-z-]+", " ", t1 + "\n" + t2)
text = re.sub(r"\[[^\]]*\]", " ", text)
words = re.findall(r"[^\W\d_]+", text)
grams = set()
for n in (1, 2, 3, 4):
    for i in range(len(words) - n + 1):
        grams.add(" ".join(w.lower() for w in words[i:i + n]))

tb = {}
for line in TB.read_text(encoding="utf-8").splitlines():
    k = line.split(": {", 1)[0]
    tb[k.lower()] = line

hits = sorted(k for k in tb if k in grams)
missing = sorted({w.lower() for w in words} - set(tb))
OUT.write_text("\n".join(tb[k] for k in hits) + "\n\n=== NO ENTRY ===\n" + ", ".join(missing) + "\n", encoding="utf-8")
print(len(tb), len(hits), len(missing))
