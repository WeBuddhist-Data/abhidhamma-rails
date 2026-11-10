"""Pāli-only keyword file for pi-1, from the Pāli=English map (same shape as pi-3…pi-5 in AI_translation/pali/).

Per line: take the Pāli side of each pair, split " / " joins into separate words, drop "(no direct equivalent)",
drop duplicates within the line (first occurrence kept, order kept). Line count and order = the map.
Refuses to overwrite an existing output.
"""
import pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parents[4]
SRC = ROOT / "AI_translation/english/pi-1-keywords-by-reference-pali-english-plain.md"
OUT = ROOT / "AI_translation/pali/pi-1-keywords-by-reference-pali-plain.md"
if OUT.exists():
    sys.exit(f"{OUT.name} already exists, not touching it")
rows, empty = [], []
for line in SRC.read_text(encoding="utf-8-sig").splitlines():
    if not line.strip():
        continue
    i, body = line.split("] ", 1)
    seen, keep = set(), []
    for p in body.split(", "):
        pali = p.rsplit("=", 1)[0]
        for w in pali.split(" / "):
            w = w.strip()
            if w and w != "(no direct equivalent)" and w not in seen:
                seen.add(w)
                keep.append(w)
    if not keep:
        empty.append(i[1:])
    rows.append(f"{i}] " + ", ".join(keep))
OUT.write_text("\n".join(rows) + "\n", encoding="utf-8", newline="\n")
print(OUT.name, len(rows), "lines; lines with no Pāli keyword:", empty)
