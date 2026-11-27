"""Which sentences / clauses / words of the pi-4 sample Pāli also occur in pi-1 / pi-2 / pi-3 Pāli? (read only, scratch)

usage: python3 -I -X utf8 overlap.py [sent|clause|word] [chapter ...]
"""
import pathlib
import re
import sys
from collections import Counter

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
ID_RE = re.compile(r" ?\^[0-9A-Za-z-]+\s*$")
mode = sys.argv[1] if len(sys.argv) > 1 else "sent"
chs = sys.argv[2:] or ["1-matika.md", "2-ekakapuggalapannatti.md"]

corp = []
for b in "123":
    for f in sorted((ROOT / f"AI_translation/pali/pi-{b}_split_chapters").glob("*.md")):
        corp.append(re.sub(r"\s*\[[^\]]*\]", "", f.read_text(encoding="utf-8-sig")))
CORP = "\n".join(corp)
CORPL = CORP.lower()


def units(line):
    line = re.sub(r"\s*\[[^\]]*\]", "", ID_RE.sub("", line)).strip()
    line = re.sub(r"^#+ |^\(\d+\) ", "", line)
    if mode == "sent":
        return [s for s in re.split(r"(?<=[.?;])\s+| – ", line) if s]
    if mode == "clause":
        return [s for s in re.split(r"(?<=[.?;,])\s+| – ", line) if s]
    return re.findall(r"[^\W\d_]+", line)


seen = Counter()
for ch in chs:
    for line in (ROOT / "AI_translation/pali/pi-4_split_chapters" / ch).read_text(encoding="utf-8-sig").splitlines():
        for u in units(line):
            k = u.strip().rstrip(".?;,").strip()
            if len(k) < 4 or k in seen:
                seen[k] += 1
                continue
            seen[k] += 1
            n = CORPL.count(k.lower())
            if n:
                print(f"{n:5d}  {k}")
