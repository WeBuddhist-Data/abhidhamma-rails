"""Context helper for map_2-09_3-01_hi.py: for each keyword, its first N segments in a file:
Pāli window, English map value, prior pi-1..6 Hindi values, Hindi window (proportional position).
usage: python -I -B -X utf8 ctx_2-09_3-01_hi.py <file> <N> kw1 kw2 …   (kw '*' = whole segment ids follow: @id)
"""
import collections
import pathlib
import re
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import read_keywords, read_hindi, read_pali, prior, ROOT, lc  # noqa: E402

EN = ROOT / "AI_translation" / "english" / "pi-7-keywords-by-reference-pali-english-plain.md"
_en = {}
for line in EN.read_text(encoding="utf-8").splitlines():
    if "] " in line:
        bid, rest = line.split("] ", 1)
        _en[bid[1:]] = rest.split(", ")

f, n = sys.argv[1], int(sys.argv[2])
kwl = read_keywords(f)
hi, pa = read_hindi(f), read_pali(f)
for kw in sys.argv[3:]:
    if kw.startswith("@"):
        bid = kw[1:]
        print("#####", bid)
        print("PA:", pa.get(bid))
        print("HI:", hi.get(bid))
        print("EN:", ", ".join(_en.get(bid, [])))
        continue
    only = None
    if "@" in kw:
        kw, only = kw.split("@", 1)
    pr = prior(kw)
    print("=" * 30, kw, "| prior:", {b: dict(c.most_common(3)) for b, c in pr.items()})
    shown = 0
    for bid, kws in kwl:
        if kw not in kws or shown >= n or (only and bid != only):
            continue
        shown += 1
        p, h = pa.get(bid, ""), hi.get(bid, "")
        i = p.find(kw)
        if i < 0:
            i = p.lower().find(kw.lower())
        en = [x for x in _en.get(bid, []) if x.split("=", 1)[0] == kw]
        j = int(len(h) * max(i, 0) / max(len(p), 1))
        print(f"--- {bid} EN: {en[:2]}")
        print("   PA:", p[max(0, i - 70): i + 90].replace("\n", " "))
        print("   HI:", h[max(0, j - 160): j + 200].replace("\n", " "))
