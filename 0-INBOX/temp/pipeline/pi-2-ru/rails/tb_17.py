"""Termbase entries for every keyword of chapter 17 (^2-832 … ^2-977 and ^2-U1 … ^2-U72), written to tb-17.txt.
usage: python -I -X utf8 tb_17.py
"""
import pathlib
import re

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
KW = ROOT / "AI_translation" / "pali" / "pi-2-keywords-by-reference-pali-plain.md"
TB = ROOT / "AI_translation" / "russian" / "pi-2-pali-russian-termbase-plain.md"
OUT = ROOT / "0-INBOX" / "temp" / "pipeline" / "pi-2-ru" / "rails" / "tb-17.txt"

idx = {}
for ln in TB.read_text(encoding="utf-8").splitlines():
    if ": {" in ln:
        idx.setdefault(ln.split(": {", 1)[0], []).append(ln)

words = []
for ln in KW.read_text(encoding="utf-8").splitlines():
    m = re.match(r"\[2-(U?)(\d+)\] (.*)$", ln)
    if m and (m.group(1) == "U" and int(m.group(2)) <= 72 or not m.group(1) and 832 <= int(m.group(2)) <= 977):
        for w in m.group(3).split(", "):
            w = w.strip()
            if w and w not in words:
                words.append(w)
out = []
for w in sorted(words, key=str.lower):
    out += idx.get(w, [f"--- {w}: NOT FOUND"])
OUT.write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")
print(len(words), "keywords;", sum(1 for w in words if w not in idx), "not found")
