"""Pali-presence check for the 3-02 / 3-03 maps (same as check_preamble_1-matika.py, with two more
sandhi kinds recognised).

usage: python -I -X utf8 check_3-02_3-03.py [chapter ...]
Every `pali=english` value (each side of " / ") must be a case-sensitive substring of the segment's
Pali (variant brackets, labels, heading marks and ^id removed). A miss is labelled SANDHI when the
value is a compound member written in its own form and the text fuses it at the joint:
  - final vowel lost or merged (upādiṇṇa in upādiṇṇupādāniyaṃ, itthi in itthindriyaṃ),
  - initial vowel lengthened (āyatana-),
  - initial vowel elided after the preceding member (indriyaṃ in cakkhundriyaṃ),
  - initial v doubled to bb after a numeral (vidhena in catubbidhena, chabbidhena).
Anything else is MISSING (an error).
"""
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
PALI = ROOT / "AI_translation" / "pali" / "pi-1_split_chapters"
NDE = "(no direct equivalent)"
ID = re.compile(r"\s*\^([0-9A-Za-z-]+)\s*$")


def segments(ch):
    segs, buf = {}, []
    for line in (PALI / f"{ch}.md").read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        mm = ID.search(line)
        buf.append(line[:mm.start()] if mm else line)
        if mm:
            t = " ".join(buf)
            t = re.sub(r"\[[^\]]*\]", " ", t)
            t = re.sub(r"\((Ka|Kha|Ga)\)", " ", t)
            t = re.sub(r"^#+\s*|\s#+\s", " ", t)
            segs[mm.group(1)] = re.sub(r"\s+", " ", t).strip()
            buf = []
    return segs


def sandhi(alt, text):
    long_initial = {"a": "ā", "i": "ī", "u": "ū"}.get(alt[0], alt[0]) + alt[1:]
    return (alt[:-1] in text or long_initial in text
            or (alt[0] in "aiu" and len(alt) > 4 and alt[1:] in text)
            or (alt[0] == "v" and "bb" + alt[1:] in text))


def check(ch):
    segs = segments(ch)
    nde = cuts = total = 0
    misses = []
    for line in (HERE / f"{ch}.mapped.md").read_text(encoding="utf-8").splitlines():
        bid, rest = line.split("] ", 1)
        bid = bid[1:]
        text = segs[bid]
        words = set(re.findall(r"[^\s.,;:?–]+", text))
        for pair in rest.split(", "):
            total += 1
            pali, eng = pair.rsplit("=", 1)
            if pali == NDE:
                nde += 1
                continue
            for alt in pali.split(" / "):
                if alt in text:
                    if " " not in alt and alt not in words:
                        cuts += 1
                    continue
                misses.append(("SANDHI" if sandhi(alt, text) else "MISSING", bid, alt, eng))
    kinds = {}
    for kind, bid, alt, eng in misses:
        kinds.setdefault((kind, alt), []).append(bid)
    print(f"{ch}: pairs {total}, nde {nde}, cut values (substring of a longer word) {cuts}, "
          f"not present {len(misses)} (SANDHI {sum(1 for x in misses if x[0] == 'SANDHI')}, "
          f"MISSING {sum(1 for x in misses if x[0] == 'MISSING')})")
    for (kind, alt), ids in sorted(kinds.items()):
        print(f"    {kind} {alt}  x{len(ids)}  e.g. {ids[0]}")


if __name__ == "__main__":
    for ch in sys.argv[1:] or ["3-02-rupakandam", "3-03-rupakandam"]:
        check(ch)
