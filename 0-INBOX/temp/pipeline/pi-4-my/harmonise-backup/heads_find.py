"""Exact line lookup in the FINAL pi-1 / pi-2 / pi-3 Burmese: for each Pāli text given, every final Burmese of a line
whose Pāli (without #, block ID and final «.») equals it. Read only.

usage: python3 -I -X utf8 heads_find.py TEXT [TEXT ...]
"""
import re
import sys

sys.argv.append("--noop")
import pathlib
import unicodedata

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
ID_RE = re.compile(r" (\^[0-9A-Za-z-]+)\s*$")


def blocks(text):
    res, cur = {}, []
    for line in text.splitlines():
        if not line.strip():
            continue
        cur.append(line)
        m = ID_RE.search(line)
        if m:
            res[m.group(1)] = cur
            cur = []
    return res


def norm(s):
    s = ID_RE.sub("", s)
    s = re.sub(r"^#+ ", "", s).strip()
    return s.rstrip(".").rstrip("။").strip()


want = [a for a in sys.argv[1:] if a != "--noop"]
found = {w: {} for w in want}
for b in "123":
    pdir = ROOT / f"AI_translation/pali/pi-{b}_split_chapters"
    bdir = ROOT / f"AI_translation/burmese/pi-{b}-burmese-plain-rails_split_chapters"
    for f in sorted(pdir.glob("*.md")):
        bf = bdir / f.name
        if not bf.exists():
            continue
        pb = blocks(f.read_text(encoding="utf-8-sig"))
        bb = blocks(unicodedata.normalize("NFC", bf.read_text(encoding="utf-8-sig")))
        for k, pl in pb.items():
            for i, p in enumerate(pl):
                n = norm(p)
                for w in want:
                    if n.lower() == w.lower():
                        my = bb[k][i]
                        found[w].setdefault(my, []).append(f"pi-{b} {k}")
for w in want:
    print(f"{w}:")
    for my, ks in found[w].items():
        print(f"   {my}   [{len(ks)}: {', '.join(ks[:3])}]")
