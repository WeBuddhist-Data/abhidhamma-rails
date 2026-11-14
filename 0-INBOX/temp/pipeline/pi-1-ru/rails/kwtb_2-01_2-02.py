"""Helper for 2-01/2-02: distinct keywords of the segments after ^1-57 (2-01) and of 2-02,
with their full termbase entries. Writes kwtb-2-01_2-02.txt next to this file.
usage: python -I -X utf8 kwtb_2-01_2-02.py"""
import re
from pathlib import Path

ROOT = Path(r"D:\Work\OpenPecha\abhidhamma-rails")
PALI = ROOT / "AI_translation" / "pali" / "pi-1_split_chapters"
KW = ROOT / "AI_translation" / "pali" / "pi-1-keywords-by-reference-pali-plain.md"
TB = ROOT / "AI_translation" / "russian" / "pi-1-pali-russian-termbase-plain.md"
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")

ids = []
for f in ("2-01-cittuppadakandam.md", "2-02-cittuppadakandam.md"):
    for line in (PALI / f).read_text(encoding="utf-8").splitlines():
        m = ID.search(line)
        if m:
            ids.append(m.group(1))
want = set(ids[ids.index("1-57") + 1:])
tb = {}
for line in TB.read_text(encoding="utf-8").splitlines():
    if ": {" in line:
        k, v = line.split(": {", 1)
        tb[k] = v.rstrip("}")
seen = {}
for line in KW.read_text(encoding="utf-8").splitlines():
    m = re.match(r"\[([^\]]+)\] (.*)", line)
    if not m or m.group(1) not in want:
        continue
    for k in m.group(2).split(", "):
        seen.setdefault(k, m.group(1))
out = [f"{k} [{sid}]: {tb.get(k, '??')}" for k, sid in seen.items()]
(Path(__file__).parent / "kwtb-2-01_2-02.txt").write_text("\n".join(out) + "\n", encoding="utf-8")
print(len(out), "keywords")
