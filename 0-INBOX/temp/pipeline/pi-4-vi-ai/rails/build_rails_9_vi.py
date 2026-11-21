"""pi-4 Puggalapaññatti, Vietnamese RAILS (plain audience): chapter 9 Aṭṭhakapuggalapaññatti (^4-1-8-0, ^4-207).

Builds AI_translation/vietnamese/pi-4-vietnamese-plain-rails_split_chapters/9-atthakapuggalapannatti.md from fixed
strings, importing the approved sample constants (build_rails_sample_vi as S: NAME, headings, closers).
The question uses the approved aṭṭhaka matrix names (^4-M-14) and the answer the ekaka names of the eight noble
persons (^4-M-7, S.NAME), so identical Pāli gives byte-identical Vietnamese. No atthekacco name occurs here.
At build time: every string marked (pi-2) is asserted to occur in the approved pi-2 Vietnamese rails; strings taken
from the finished pi-4 chapters (matrix, ch4, ch5) are asserted to occur there; every person name used is asserted
to be a value of S.NAME; block IDs and per-segment line counts are checked against the Pāli chapter.
Termbase: AI_translation/vietnamese/pi-4-pali-vietnamese-termbase-plain.md (+ pi-4-vi-ai/termbase/APPROVED.md).
New recurring strings: notes-rails-9.md.

usage: python -I -X utf8 build_rails_9_vi.py
"""
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-4-vi-ai\rails")
import build_rails_sample_vi as S  # noqa: E402  (import writes nothing)

ROOT = S.ROOT
SRC = ROOT / "AI_translation/pali/pi-4_split_chapters/9-atthakapuggalapannatti.md"
OUT = S.OUT_DIR / "9-atthakapuggalapannatti.md"
USED_NAMES = []


def N(k):
    v = S.NAME[k]
    USED_NAMES.append(v)
    return v


# ---------------------------------------------------------------------------------------------------------------
# Fixed strings (new ones are listed in notes-rails-9.md)
# ---------------------------------------------------------------------------------------------------------------
TATTHA_Q = "Ở đây, {} là những ai?"          # Tattha katame X? (ch4, ch5)
IME = "đây là {}"                              # ime X (ch4 «Ime tayo satthāro.» = «Đây là ba bậc đạo sư.»)
ARAHATTAYA = " [dị bản (Syā., Ka.): arahattāya; Tăng Chi Bộ Kinh 8.59]"
#   [arahattāya (syā. ka.) a. ni. 8.59]   (matrix ^4-M-7 «[dị bản (Sī.): arahattāya]»; «Tăng Chi Bộ Kinh» pi-2;
#   note layout «[…: word; Tăng Chi Bộ Kinh N.N]» as ch5 ^4-160)

# Strings taken unchanged from the approved pi-2 rails (asserted)
REUSED = [
    ("a. ni. (citation)", "Tăng Chi Bộ Kinh", "2"),
]
# Strings taken from the finished pi-4 chapters (asserted in those files)
PI4 = [
    ("1-matika.md", "[dị bản (Sī.): arahattāya]"),
    ("1-matika.md", "Bốn hạng người có được con đường, bốn hạng người có được thành quả."),
    ("4-tikapuggalapannatti.md", "Ở đây, ba bậc đạo sư là những ai?"),
    ("4-tikapuggalapannatti.md", "Đây là ba bậc đạo sư."),
    ("5-catukkapuggalapannatti.md", "[khác chính tả (Syā., Ka.): āmavaṇṇī; Tăng Chi Bộ Kinh 4.105]"),
]


def seg(*lines):
    return "\n".join(lines)


def build():
    magga = N("cattāro maggasamaṅgino")             # bốn hạng người có được con đường
    phala = N("cattāro phalasamaṅgino puggalā")     # bốn hạng người có được thành quả
    q = TATTHA_Q.format(f"{magga}, {phala}")
    pairs = [
        (N("sotāpanno"), N("sotāpattiphalasacchikiriyāya paṭipanno")),
        (N("sakadāgāmī"), N("sakadāgāmiphalasacchikiriyāya paṭipanno")),
        (N("anāgāmī"), N("anāgāmiphalasacchikiriyāya paṭipanno")),
        (N("arahā"), N("arahattaphalasacchikiriyāya paṭipanno") + ARAHATTAYA),
    ]
    answer = "; ".join(f"{a}, {b}" for a, b in pairs)
    answer = S.cap(answer) + "; " + IME.format(magga) + ", " + IME.format(phala) + "."
    line1 = q + " " + answer
    return [seg(S.H_CHAPTER[8] + " ^4-1-8-0"), seg(line1, S.CLOSER_CHAPTER[8] + " ^4-207")]


# ---------------------------------------------------------------------------------------------------------------
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")


def structure(text):
    out, n = [], 0
    for line in text.splitlines():
        if not line.strip():
            continue
        n += 1
        m = ID.search(line)
        if m:
            out.append((m.group(1), n))
            n = 0
    return out


def nfc_lower(s):
    return unicodedata.normalize("NFC", s).lower()


def check_reused():
    texts = {b: nfc_lower("\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md"))))
             for b, d in S.RAILS.items()}
    bad = [(p, v, b) for p, v, b in REUSED if nfc_lower(v) not in texts[b]]
    assert not bad, "reused strings not found in their rails: " + repr(bad)
    bad = [(f, v) for f, v in PI4 if unicodedata.normalize("NFC", v)
           not in unicodedata.normalize("NFC", (S.OUT_DIR / f).read_text(encoding="utf-8"))]
    assert not bad, "pi-4 strings not found in their chapters: " + repr(bad)


def main():
    check_reused()
    segs = build()
    names = set(S.NAME.values())
    assert all(n in names for n in USED_NAMES)
    text = unicodedata.normalize("NFC", "\n\n".join(segs) + "\n")
    assert "\n\n\n" not in text and "—" not in text and "–" not in text and ":-" not in text and "…." not in text
    src = SRC.read_text(encoding="utf-8")
    assert structure(src) == structure(text), (structure(src), structure(text))
    OUT.write_text(text, encoding="utf-8", newline="\n")
    print("wrote", OUT, len(structure(text)), "segments")


if __name__ == "__main__":
    main()
