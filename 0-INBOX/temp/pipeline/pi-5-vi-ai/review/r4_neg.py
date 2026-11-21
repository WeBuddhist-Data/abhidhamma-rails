"""r4: crude per-line negation count, Pali vs Vietnamese, frames removed (console only)."""
import re
import sys

BASE = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation"
PDIR = BASE + r"\pali\pi-5_split_chapters"
VDIR = BASE + r"\vietnamese\pi-5-vietnamese-plain-rails_split_chapters"


def nonempty(p):
    with open(p, encoding="utf-8") as f:
        return [l for l in f.read().split("\n") if l.strip()]


def pneg(s):
    s = re.sub(r"\[[^\]]*\]", "", s).lower()
    s = re.sub(r"na hevaṃ vattabbe", "", s)
    s = re.sub(r"no ca vata re vattabbe|no vata re vattabbe", "", s)
    s = re.sub(r"tena hi na vattabba", "", s)
    s = re.sub(r"\bna vattabbaṃ", "", s)  # counted separately
    n = len(re.findall(r"\bna\b|\bnatthi|\bno\b|\bnāti|\bneva\b|\bmā\b", s))
    return n


def vneg(s):
    s = re.sub(r"\[[^\]]*\]", "", s).lower()
    s = s.replace("không nên nói như vậy", "")
    s = s.replace("chắc chắn không nên nói", "")
    s = s.replace("vậy thì không nên nói", "")
    s = re.sub(r"có phải không nên nói", "", s)
    s = re.sub(r"không nên được gọi là", "", s)
    s = re.sub(r"không\s*[”’]?\s*\?", "?", s)  # question-final
    s = s.replace("chẳng phải", "")
    s = s.replace("không có.", "")  # Natthi answer counted below
    return len(re.findall(r"\bkhông\b|\bchưa\b|\bchẳng\b|\bđừng\b", s))


for ch in sys.argv[1:]:
    pl, vl = nonempty(PDIR + "\\" + ch), nonempty(VDIR + "\\" + ch)
    for i, (p, v) in enumerate(zip(pl, vl)):
        a, b = pneg(p), vneg(v)
        if b < a:
            print(ch, "L%d" % (i + 1), "P-neg %d V-neg %d" % (a, b), re.search(r"\^\S+\s*$", p) and re.search(r"\^\S+\s*$", p).group(0) or "")
