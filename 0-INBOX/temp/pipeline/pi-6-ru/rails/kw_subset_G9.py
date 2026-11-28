"""Write the pi-6 keyword lines of the 9-01 / 9-02 / 9-03 (Dhammayamaka) segments to kw-G9.md (so
termbase_adherence.py counts only G9's chapters). usage: python -I -X utf8 -B kw_subset_G9.py
"""
import pathlib
import re

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
KW = ROOT / "AI_translation" / "pali" / "pi-6-keywords-by-reference-pali-plain.md"
RU = ROOT / "AI_translation" / "russian" / "pi-6-russian-plain-rails_split_chapters"
OUT = ROOT / "0-INBOX" / "temp" / "pipeline" / "pi-6-ru" / "rails" / "kw-G9.md"
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")

ids = set()
for ch in ("9-01-dhammayamaka.md", "9-02-dhammayamaka.md", "9-03-dhammayamaka.md"):
    ids |= {m.group(1) for ln in (RU / ch).read_text(encoding="utf-8").splitlines() if (m := ID.search(ln))}
keep = [ln for ln in KW.read_text(encoding="utf-8").splitlines() if ln[1:].split("] ", 1)[0] in ids]
OUT.write_text("\n".join(keep) + "\n", encoding="utf-8", newline="\n")
print(len(ids), "segments;", len(keep), "keyword lines")
