"""Probe for part 2-04: how the approved pi-3/4/5 Russian maps (and the pi-1 English map) rendered given keywords.

usage: python -I -X utf8 probe_2-04_prior_ru.py kw1 kw2 ...
"""
import collections
import pathlib
import re
import sys

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation")
FILES = [ROOT / "russian" / f"pi-{n}-keywords-by-reference-pali-russian-plain.md" for n in (3, 4, 5)]
EN = ROOT / "english" / "pi-1-keywords-by-reference-pali-english-plain.md"

texts = {f.name[:4]: f.read_text(encoding="utf-8") for f in FILES if f.exists()}
en = EN.read_text(encoding="utf-8")
for kw in sys.argv[1:]:
    pat = re.compile(r"(?:\] |, )" + re.escape(kw) + r"=([^,\n]+)")
    out = []
    for name, t in texts.items():
        c = collections.Counter(m.group(1) for m in pat.finditer(t))
        if c:
            out.append(f"{name}: " + "; ".join(f"{v} x{n}" for v, n in c.most_common(4)))
    c = collections.Counter(m.group(1) for m in pat.finditer(en))
    if c:
        out.append("en: " + "; ".join(f"{v} x{n}" for v, n in c.most_common(3)))
    print(kw, "->", " | ".join(out) if out else "-")
