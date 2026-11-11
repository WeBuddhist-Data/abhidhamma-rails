"""Prepare per-chapter inputs for the pi-2 English→Pāli keyword mapping.

usage: python -I -X utf8 prep_mapper.py
From the extractor output (Keyword_extractor/output/pi-2-english-plain-zeroshot-by-reference.md) and the
zero-shot English (AI_translation/english/pi-2-english-plain-zeroshot.md), writes into mapper/:
  <ch>.keywords.md  [id] kw1, kw2, …   (lines in Pāli order, only IDs that have keywords)
  <ch>.en.md        the English segments of that chapter (same ^ids)
Chapters and their IDs come from AI_translation/pali/pi-2_split_chapters/<ch>.md.
"""
import pathlib, re

B = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
OUT = pathlib.Path(__file__).parent / "mapper"
OUT.mkdir(exist_ok=True)
ID = re.compile(r"\s\^([0-9A-Za-z-]+)\s*$")
KW = re.compile(r"^\[([^\]]+)\]\s*(.*)$")

kw = {}
for l in (B / "AI_translation/skills/scripts/Keyword_extractor/output/pi-2-english-plain-zeroshot-by-reference.md").read_text(encoding="utf-8").splitlines():
    m = KW.match(l)
    if m:
        kw[m.group(1)] = m.group(2)

en_t = (B / "AI_translation/english/pi-2-english-plain-zeroshot.md").read_text(encoding="utf-8").replace("\r\n", "\n")
_fm = re.match(r"---\n.*?\n---\n", en_t, re.S)
en_t = en_t[_fm.end():] if _fm else en_t
en_seg, buf = {}, []
for l in en_t.split("\n"):
    if not l.strip() or l.startswith("![["):
        continue
    buf.append(l)
    m = ID.search(l)
    if m:
        en_seg[m.group(1)] = buf; buf = []

sdir = B / "AI_translation/pali/pi-2_split_chapters"
chs = sorted(sdir.glob("*.md"), key=lambda p: -1 if p.stem == "preamble" else int(p.stem.split("-")[0]))
used, total_lines = set(), 0
for p in chs:
    ids = [m.group(1) for l in p.read_text(encoding="utf-8").splitlines() if (m := ID.search(l))]
    rows = [f"[{i}] {kw[i]}" for i in ids if i in kw]
    used |= {i for i in ids if i in kw}
    (OUT / f"{p.stem}.keywords.md").write_text("\n".join(rows) + "\n", encoding="utf-8", newline="\n")
    (OUT / f"{p.stem}.en.md").write_text("\n\n".join("\n".join(en_seg[i]) for i in ids) + "\n", encoding="utf-8", newline="\n")
    n_kw = sum(len(kw[i].split(", ")) for i in ids if i in kw)
    total_lines += len(rows)
    print(f"{p.stem:32} ids {len(ids):4}  keyword lines {len(rows):4}  keywords {n_kw:5}")
print("keyword IDs not placed in any chapter:", sorted(set(kw) - used))
print("total keyword lines", total_lines, "of", len(kw))
