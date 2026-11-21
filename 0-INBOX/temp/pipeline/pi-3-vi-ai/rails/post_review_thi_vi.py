"""User approval 2026-11-20 ("Approve, then merge", extra 2): add «thì» where a dependent-origination link name
(«… do X làm điều kiện», decision 4) stands directly before the main verb, so «điều kiện gắn liền / được gộp»
is not read as one phrase. Same rule as the «thì» before verbs elsewhere. Applied to ch7 ^3-240-243 (the
approved spot) and ch2 ^3-62-65 (identical shape). Appends to review-fixes-log.tsv.
"""
import pathlib, re

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
V = ROOT / "AI_translation/vietnamese/pi-3-vietnamese-plain-rails_split_chapters"
LOG = ROOT / "0-INBOX/temp/pipeline/pi-3-vi-ai/rails/review-fixes-log.tsv"
PAT = re.compile(r"làm điều kiện (gắn liền|được gộp)")
EXPECT = {"2-pathamanayo.md": 4, "7-chatthanayo.md": 4}

rows = []
for name, n in EXPECT.items():
    p = V / name
    lines = p.read_text(encoding="utf-8").split("\n")
    hits = 0
    for i, l in enumerate(lines):
        if PAT.search(l):
            new = PAT.sub(r"làm điều kiện thì \1", l)
            sid = re.search(r"\^([0-9-]+)\s*$", l)
            rows.append(f"{name}\t{sid.group(1) if sid else '?'}\tlàm điều kiện <verb>\tlàm điều kiện thì <verb>\tuser extra 2")
            hits += len(PAT.findall(l))
            lines[i] = new
    assert hits == n, (name, hits)
    p.write_text("\n".join(lines), encoding="utf-8", newline="\n")
with open(LOG, "a", encoding="utf-8", newline="\n") as f:
    f.write("\n".join(rows) + "\n")
print("changed", len(rows), "lines")
