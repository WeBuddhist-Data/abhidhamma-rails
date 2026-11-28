"""Write the pi-6 keyword lines of the G3 segments (3-01 … 3-06 Āyatanayamaka) to kw-G3.md
(so termbase_adherence.py counts only these chapters).

usage: python -I -X utf8 -B kw_subset_G3.py
"""
import pathlib
import re

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
KW = ROOT / "AI_translation" / "pali" / "pi-6-keywords-by-reference-pali-plain.md"
RU = ROOT / "AI_translation" / "russian" / "pi-6-russian-plain-rails_split_chapters"
OUT = ROOT / "0-INBOX" / "temp" / "pipeline" / "pi-6-ru" / "rails" / "kw-G3.md"
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")

ids = {m.group(1) for ch in (f"3-0{i}-ayatanayamaka.md" for i in range(1, 7))
       for ln in (RU / ch).read_text(encoding="utf-8").splitlines() if (m := ID.search(ln))}
keep = [ln for ln in KW.read_text(encoding="utf-8").splitlines() if ln[1:].split("] ", 1)[0] in ids]
OUT.write_text("\n".join(keep) + "\n", encoding="utf-8", newline="\n")
print(len(ids), "segments;", len(keep), "keyword lines")
