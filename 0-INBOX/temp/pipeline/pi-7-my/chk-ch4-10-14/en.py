"""Read-only: the Pāli lines of 4-10 … 4-14 matching a regex, with the aligned English zero-shot line (meaning only)."""
import re
import sys
import pathlib

R = pathlib.Path(__file__).resolve().parents[5] / "AI_translation"
rx = re.compile(sys.argv[1])
for n in ["4-10-dukatika-sarammanaduka.md", "4-11-dukatika-upadanaduka.md", "4-12-dukatika-kilesaduka.md",
          "4-13-dukatika-dassanenapahatabbaduka.md", "4-14-dukatika-saranaduka.md"]:
    pl = [l for l in (R / "pali/pi-7_split_chapters" / n).read_text(encoding="utf-8-sig").splitlines() if l.strip()]
    ef = R / "english/pi-7-english-plain-zeroshot_split_chapters" / n
    el = [l for l in ef.read_text(encoding="utf-8-sig").splitlines() if l.strip()] if ef.exists() else []
    for i, l in enumerate(pl):
        if rx.search(l):
            print(f"[{n[:4]}:{i + 1}] PI: {l[:600]}\n   EN: {el[i][:900] if i < len(el) else '-'}")
