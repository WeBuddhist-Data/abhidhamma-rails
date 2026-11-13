"""Split AI_translation/pali/pi-6-keywords-by-reference-pali-plain.md into per-part keyword files for the Hindi mapper.

out: 0-INBOX/temp/pipeline/pi-6-hi/mapper-hi/<part>.keywords.md (lines in file order; every line assigned exactly once)
"""
import pathlib, re, sys

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
SRC = ROOT / "AI_translation/pali/pi-6-keywords-by-reference-pali-plain.md"
PALI = ROOT / "AI_translation/pali/pi-6_split_chapters"
OUT = ROOT / "0-INBOX/temp/pipeline/pi-6-hi/mapper-hi"
OUT.mkdir(exist_ok=True)
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")

owner = {}
for p in sorted(PALI.glob("*.md")):
    for line in p.read_text(encoding="utf-8-sig").splitlines():
        m = ID.search(line)
        if m:
            owner[m.group(1)] = p.stem
by_part, missing = {}, []
for line in SRC.read_text(encoding="utf-8-sig").splitlines():
    if not line.strip():
        continue
    sid = line[1:line.index("]")]
    part = owner.get(sid)
    if part is None:
        missing.append(sid)
        continue
    by_part.setdefault(part, []).append(line)
if missing:
    sys.exit(f"ids not in the Pāli parts: {missing[:10]}")
total = 0
for part, lines in by_part.items():
    (OUT / f"{part}.keywords.md").write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    total += len(lines)
    print(part, len(lines))
print("total", total)
