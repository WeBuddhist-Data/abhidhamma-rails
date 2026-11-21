"""r4: answer-sequence check per line (A = yes, N = should not be said, X = no / natthi). Console only."""
import re
import sys

BASE = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation"
PDIR = BASE + r"\pali\pi-5_split_chapters"
VDIR = BASE + r"\vietnamese\pi-5-vietnamese-plain-rails_split_chapters"


def nonempty(p):
    with open(p, encoding="utf-8") as f:
        return [l for l in f.read().split("\n") if l.strip()]


def pseq(s):
    s = re.sub(r"\[[^\]]*\]", "", s)
    out = []
    for m in re.finditer(r"āmantā|na hevaṃ vattabbe|\? natthi\b", s, re.I):
        t = m.group(0).lower()
        out.append("A" if t.startswith("ām") else ("N" if t.startswith("na") else "X"))
    return "".join(out)


def vseq(s):
    s = re.sub(r"\[[^\]]*\]", "", s)
    out = []
    for m in re.finditer(r"đúng vậy|không nên nói như vậy|\? không có\b", s, re.I):
        t = m.group(0).lower()
        out.append("A" if t.startswith("đú") else ("N" if t.startswith("không") else "X"))
    return "".join(out)


for ch in sys.argv[1:]:
    pl, vl = nonempty(PDIR + "\\" + ch), nonempty(VDIR + "\\" + ch)
    bad = 0
    for i, (p, v) in enumerate(zip(pl, vl)):
        a, b = pseq(p), vseq(v)
        if a != b:
            bad += 1
            print(ch, "L%d" % (i + 1), a, b)
    print(ch, "lines", len(pl), "sequence mismatches", bad)
