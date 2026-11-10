"""Pali-presence check for 5-atthakathakandam.mapped.md (same test as check_preamble_1-matika.py).

usage: python -I -X utf8 check_5-atthakathakandam.py
Every value (each side of " / ") must be a case-sensitive substring of the segment's Pali (variant
brackets, labels, heading marks removed). Misses are classified:
  PUNCT   the value is present once the commas / dashes inside the stretch are ignored
          (", " is the map separator, so a stretch is written without them)
  ENCL    present once the enclitic -ti / -pi of a "...tipi" quotation is restored
  SANDHI  a compound member written in its own form where the text fuses / doubles letters at the
          joint (final vowel changed, initial a/i/u lengthened, doubled consonant: v -> bb, kh -> kkh)
  MISSING anything else (an error)
"""
import pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
CH = "5-atthakathakandam"
PALI = ROOT / "AI_translation" / "pali" / "pi-1_split_chapters" / f"{CH}.md"
NDE = "(no direct equivalent)"
ID = re.compile(r"\s*\^([0-9A-Za-z-]+)\s*$")


def segments():
    segs, buf = {}, []
    for line in PALI.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        mm = ID.search(line)
        buf.append(line[:mm.start()] if mm else line)
        if mm:
            t = " ".join(buf)
            t = re.sub(r"\s*\[[^\]]*\]", "", t)
            t = re.sub(r"\((Ka|Kha|Ga)\)", " ", t)
            t = re.sub(r"^#+\s*|\s#+\s", " ", t)
            segs[mm.group(1)] = re.sub(r"\s+", " ", t).strip()
            buf = []
    return segs


def loose(s):
    return re.sub(r"\s+", " ", re.sub(r"[,–;?]", " ", s)).strip()


def sandhi(alt, text):
    if alt[:-1] in text:
        return True
    long_initial = {"a": "ā", "i": "ī", "u": "ū"}.get(alt[0], alt[0]) + alt[1:]
    if long_initial in text or long_initial[:-1] in text:
        return True
    if alt[0] == "v" and ("bb" + alt[1:] in text or "bb" + alt[1:-1] in text):
        return True
    if alt[:2] == "kh" and "k" + alt in text:
        return True
    if alt.startswith("jhān") and "j" + alt in text:
        return True
    return False


def check():
    segs = segments()
    nde = total = 0
    kinds = {}
    for line in (HERE / f"{CH}.mapped.md").read_text(encoding="utf-8").splitlines():
        bid, rest = line.split("] ", 1)
        bid = bid[1:]
        text = segs[bid]
        lt = loose(text)
        for pair in rest.split(", "):
            total += 1
            pali, eng = pair.rsplit("=", 1)
            if pali == NDE:
                nde += 1
                continue
            for alt in pali.split(" / "):
                if alt in text:
                    continue
                if alt in lt:
                    kind = "PUNCT"
                elif re.search(re.escape(alt).replace(r"\ ", r"\w* ") + r"(?:ti|tipi|nti|ntipi)?(?!\w)", lt) or \
                        any(w + "ti" in lt or w + "tipi" in lt for w in [alt.split()[-1]]):
                    kind = "ENCL"
                elif sandhi(alt, text) or all(sandhi(w, text) or w in text for w in alt.split()):
                    kind = "SANDHI"
                else:
                    kind = "MISSING"
                kinds.setdefault(kind, []).append((bid, alt, eng))
    print(f"{CH}: pairs {total}, nde {nde}, not literal: " +
          ", ".join(f"{k} {len(v)}" for k, v in sorted(kinds.items())))
    for k in ("MISSING", "SANDHI", "ENCL", "PUNCT"):
        seen = {}
        for bid, alt, eng in kinds.get(k, []):
            seen.setdefault(alt, []).append(bid)
        for alt, bids in seen.items():
            print(f"   {k:8} {alt!r} ({len(bids)}x, e.g. {bids[0]})")


if __name__ == "__main__":
    check()
