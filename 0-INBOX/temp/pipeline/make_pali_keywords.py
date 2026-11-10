"""Derive the Pāli-only keyword file from the English keyword map (non-English pipeline skips keyword extraction).

usage: python -I -X utf8 make_pali_keywords.py <book number>
in:  AI_translation/english/pi-N-keywords-by-reference-pali-english-plain.md   ([id] pali=english, …)
out: AI_translation/pali/pi-N-keywords-by-reference-pali-plain.md               ([id] pali, …)
Refuses to overwrite an existing output file.
"""
import pathlib, sys

B = pathlib.Path(__file__).resolve().parents[3]  # repo root (was a fixed Windows path)
n = sys.argv[1]
src = B / f"AI_translation/english/pi-{n}-keywords-by-reference-pali-english-plain.md"
out = B / f"AI_translation/pali/pi-{n}-keywords-by-reference-pali-plain.md"
if out.exists():
    sys.exit(f"{out.name} already exists, not touching it")
rows = []
for line in src.read_text(encoding="utf-8-sig").splitlines():
    if not line.strip():
        continue
    i, body = line.split("] ", 1)
    rows.append(f"{i}] " + ", ".join(p.split("=", 1)[0] for p in body.split(", ")))
out.write_text("\n".join(rows) + "\n", encoding="utf-8", newline="\n")
print(out.name, len(rows), "lines")
