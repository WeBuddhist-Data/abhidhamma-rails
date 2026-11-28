"""Write the pi-6 keyword lines of the segments present in the Russian rails split folder to kw-sample.md
(so termbase_adherence.py counts only the translated chapters).

usage: python -I -X utf8 -B kw_subset.py
"""
import pathlib
import re

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
KW = ROOT / "AI_translation" / "pali" / "pi-6-keywords-by-reference-pali-plain.md"
RU = ROOT / "AI_translation" / "russian" / "pi-6-russian-plain-rails_split_chapters"
OUT = ROOT / "0-INBOX" / "temp" / "pipeline" / "pi-6-ru" / "rails" / "kw-sample.md"
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")

ids = {m.group(1) for p in RU.glob("*.md") for ln in p.read_text(encoding="utf-8").splitlines() if (m := ID.search(ln))}
keep = [ln for ln in KW.read_text(encoding="utf-8").splitlines() if ln[1:].split("] ", 1)[0] in ids]
OUT.write_text("\n".join(keep) + "\n", encoding="utf-8", newline="\n")
print(len(ids), "segments;", len(keep), "keyword lines")
