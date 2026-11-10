"""Pali-presence check for the 4-01 / 4-02 maps (same rules as check_preamble_1-matika.py).

usage: python -I -X utf8 check_4-01_4-02.py [chapter ...]
Every Pali value (each side of " / ", not "(no direct equivalent)") must be a case-sensitive substring of
the segment's Pali with variant brackets and heading marks removed. Values are also tried against the text
with "," and ";" removed (spans the map writes without the comma, e.g. "vacīkammaṃ manokammaṃ"): PUNCT.
Misses where the value minus its last letter, or with its first vowel lengthened, occurs are SANDHI
(a compound member written in its own form, conventions 1.4); "vata" written for the -bbata of
sīlabbata is SANDHI too. Anything else is MISSING.
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
            t = re.sub(r"^#+\s*|\s#+\s", " ", t)
            segs[mm.group(1)] = re.sub(r"\s+", " ", t).strip()
            buf = []
    return segs


def check(ch):
    segs = segments(ch)
    nde = cuts = total = punct = 0
    misses, cases = [], []
    for line in (HERE / f"{ch}.mapped.md").read_text(encoding="utf-8").splitlines():
        bid, rest = line.split("] ", 1)
        bid = bid[1:]
        text = segs[bid]
        flat = re.sub(r"\s+", " ", re.sub(r"[,;]", "", text))
        words = set(re.findall(r"[^\s.,;:?–]+", text))
        for pair in rest.split(", "):
            total += 1
            pali, eng = pair.rsplit("=", 1)
            if pali == NDE:
                nde += 1
                continue
            for alt in pali.split(" / "):
                # first-occurrence capitalisation hint: the stem occurs first with the other case
                stem = alt[:-1] if len(alt) > 3 else alt
                other = (alt[0].upper() if alt[0].islower() else alt[0].lower()) + stem[1:]
                po, ps = text.find(other), text.find(stem)
                if po != -1 and (ps == -1 or po < ps):
                    cases.append((bid, alt, eng))
                if alt in text:
                    if " " not in alt and alt not in words:
                        cuts += 1
                    continue
                if alt in flat:
                    punct += 1
                    continue
                long_initial = {"a": "ā", "i": "ī", "u": "ū"}.get(alt[0], alt[0]) + alt[1:]
                sandhi = (alt[:-1] in text or long_initial in text or long_initial[:-1] in text
                          or (alt == "vata" and "sīlabbat" in text))
                misses.append(("SANDHI" if sandhi else "MISSING", bid, alt, eng))
    n_s = sum(1 for x in misses if x[0] == "SANDHI")
    print(f"{ch}: pairs {total}, nde {nde}, cut values (substring of a longer word) {cuts}, "
          f"spans matched without punctuation {punct}, SANDHI {n_s}, MISSING {len(misses) - n_s}")
    for x in misses:
        if x[0] == "MISSING" or "-v" in sys.argv:
            print("   ", *x)
    if "-c" in sys.argv:
        for x in cases:
            print("    CASE?", *x)


if __name__ == "__main__":
    for ch in [a for a in sys.argv[1:] if not a.startswith("-")] or ["4-01-nikkhepakandam", "4-02-nikkhepakandam"]:
        check(ch)
