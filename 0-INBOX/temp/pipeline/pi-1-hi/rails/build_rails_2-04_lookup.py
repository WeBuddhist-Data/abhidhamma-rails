"""Termbase lookup for chapter 2-04: every token and multi-word key that occurs in the Pāli."""
import pathlib
import re
import sys

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
P = ROOT / "AI_translation" / "pali" / "pi-1_split_chapters" / "2-04-cittuppadakandam.md"
TB = ROOT / "AI_translation" / "hindi" / "pi-1-pali-hindi-termbase-plain.md"
text = P.read_text(encoding="utf-8")
# drop block ids
body = re.sub(r"\^[0-9A-Za-z-]+", " ", text)
low = body.lower()
tokens = set(re.findall(r"[a-zāīūṃṅñṭḍṇḷ]+", low))
tb = {}
for line in TB.read_text(encoding="utf-8").splitlines():
    m = re.match(r"^(.+?): \{(.*)\}\s*$", line)
    if m:
        tb[m.group(1).strip().lower()] = m.group(2)
out = []
missing = []
for t in sorted(tokens):
    if t in tb:
        out.append(f"{t}: {tb[t]}")
    else:
        missing.append(t)
multi = [k for k in tb if " " in k and k in low]
out.append("\n=== MULTI-WORD ===")
for k in sorted(multi):
    out.append(f"{k}: {tb[k]}")
out.append("\n=== NO ENTRY ===")
out.append(" ".join(missing))
target = pathlib.Path(sys.argv[1])
target.write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")
print(len(tokens), "tokens", len(tokens) - len(missing), "with entries", len(missing), "without", len(multi), "multi")
