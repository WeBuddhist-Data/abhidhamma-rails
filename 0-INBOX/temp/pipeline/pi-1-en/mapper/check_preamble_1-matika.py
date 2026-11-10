"""Pali-presence check for preamble / 1-matika maps.

usage: python -I -X utf8 check_preamble_1-matika.py [chapter ...]
For each `pali=english` pair (pali != "(no direct equivalent)"; " / " splits alternatives) checks
that the Pali value occurs (case-sensitive substring) in that segment's Pali, with variant brackets
"[...]", the (Ka)/(Kha)/(Ga) labels, heading marks and the ^id removed. Misses whose value minus its
final vowel (or with its initial a/i/u lengthened) does occur are labelled SANDHI: a compound
member written in its own form where the text fuses two vowels at the joint.
Also counts (no direct equivalent) and cut values (substring but not a whole word).
"""
import pathlib, re, sys

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


def check(ch):
    segs = segments(ch)
    nde = cuts = total = 0
    misses = []
    for line in (HERE / f"{ch}.mapped.md").read_text(encoding="utf-8").splitlines():
        bid, rest = line.split("] ", 1)
        bid = bid[1:]
        text = segs[bid]
        words = set(re.findall(r"[^\s.,;:]+", text))
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
                long_initial = {"a": "ā", "i": "ī", "u": "ū"}.get(alt[0], alt[0]) + alt[1:]
                kind = "SANDHI" if alt[:-1] in text or long_initial in text else "MISSING"
                misses.append((kind, bid, alt, eng))
    print(f"{ch}: pairs {total}, nde {nde}, cut values (substring of a longer word) {cuts}, "
          f"not present {len(misses)}")
    for x in misses:
        print("   ", *x)


if __name__ == "__main__":
    for ch in sys.argv[1:] or ["preamble", "1-matika"]:
        check(ch)
