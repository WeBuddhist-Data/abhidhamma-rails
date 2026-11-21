"""pi-4 Puggalapaññatti, Vietnamese RAILS (plain audience): chapter 7 Chakkapuggalapaññatti (^4-1-6-0, ^4-202).

Builds AI_translation/vietnamese/pi-4-vietnamese-plain-rails_split_chapters/7-chakkapuggalapannatti.md from fixed
strings, importing the approved sample constants (build_rails_sample_vi as S: NAME, frames, headings, closers).
The six clauses are the approved matrix names of the chakka (^4-M-12, S.NAME) without their leading «có người »
(the Pāli here has «yvāyaṃ puggalo», no atthekacco), so identical Pāli gives byte-identical Vietnamese.
At build time: every string marked (pi-2) is asserted to occur in the approved pi-2 Vietnamese rails; strings taken
from the finished pi-4 chapters (matrix, ch4) are asserted to occur there; every person name used is asserted to be
a value of S.NAME; block IDs and per-segment line counts are checked against the Pāli chapter.
Termbase: AI_translation/vietnamese/pi-4-pali-vietnamese-termbase-plain.md (+ pi-4-vi-ai/termbase/APPROVED.md).
New recurring strings: notes-rails-7.md.

usage: python -I -X utf8 build_rails_7_vi.py
"""
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-4-vi-ai\rails")
import build_rails_sample_vi as S  # noqa: E402  (import writes nothing)

ROOT = S.ROOT
SRC = ROOT / "AI_translation/pali/pi-4_split_chapters/7-chakkapuggalapannatti.md"
OUT = S.OUT_DIR / "7-chakkapuggalapannatti.md"
USED_NAMES = []


def N(k):
    v = S.NAME[k]
    USED_NAMES.append(v)
    return v


def tail(k):
    """The predicate of an atthekacco matrix name: NAME without «có người » (coordinator rule: the definition's
    Pāli has «yvāyaṃ puggalo», no atthi / ekacco, so «có» is dropped; «người» comes from «người nào»)."""
    v = N(k)
    assert v.startswith("có người "), v
    return v[len("có người "):]


# ---------------------------------------------------------------------------------------------------------------
# Fixed strings (new ones are listed in notes-rails-7.md)
# ---------------------------------------------------------------------------------------------------------------
TATRA = "Trong số đó, người nào {}, thì cần hiểu người ấy là {}."
#   Tatra yvāyaṃ puggalo …, X tena daṭṭhabbo / daṭṭhabbā.   (ch4 ^4-130/131 «Trong số đó, bậc đạo sư nào …, thì cần
#   hiểu bậc đạo sư ấy là …» with «người» for puggalo)

# the six matrix clauses (S.CHAKKA keys)
K1 = "… abhisambujjhati, tattha ca sabbaññutaṃ pāpuṇāti balesu ca vasībhāvaṃ"
K2 = "… abhisambujjhati, na ca tattha sabbaññutaṃ pāpuṇāti na ca balesu vasībhāvaṃ"
K3 = "… anabhisambujjhati, diṭṭhe ceva dhamme dukkhassantakaro hoti sāvakapāramiñca pāpuṇāti"
K4 = "… anabhisambujjhati, diṭṭheva dhamme dukkhassantakaro hoti, na ca sāvakapāramiṃ pāpuṇāti"
K5 = "… anabhisambujjhati, na ca diṭṭheva dhamme dukkhassantakaro hoti, anāgāmī hoti anāgantā itthattaṃ"
K6 = "… anabhisambujjhati, na ca diṭṭheva dhamme dukkhassantakaro hoti, āgāmī hoti āgantā itthattaṃ"

KHOI = f"trở thành người {S.DUKKHASSANTA}"                         # dukkhassantakaro hoti
N_KAROTI = " [dị bản (Sī.): dukkhassantaṃ karoti, cũng vậy ở các chỗ sau]"
#   [dukkhassantaṃ karoti (sī.) evamuparipi]   («cũng vậy ở các chỗ sau» = evamuparipi, pi-2)
AGAMI_M = "mà trở thành người còn trở lại, người sẽ trở lại đời này"  # āgāmī hoti āgantā itthattaṃ (matrix)
AGANTA = "mà là người sẽ trở lại đời này"                            # āgantā itthattaṃ (ch7: no «āgāmī hoti»)
SARIPUTTA = "Xá-lợi-phất và Mục-kiền-liên"                           # sāriputtamoggallānā (not in the termbase)
AVASESA = "các bậc A-la-hán còn lại"                                 # avasesā arahantā
SOTA_SAKA = "bậc vào dòng và bậc trở lại một lần"                    # sotāpannasakadāgāmino (ch4 ^4-110/127)

# Strings taken unchanged from the approved pi-2 rails (asserted)
REUSED = [
    ("evamuparipi (variant note)", "cũng vậy ở các chỗ sau", "2"),
    ("diṭṭheva dhamme", S.DITTHE_DHAMME, "2"),
]
# Strings taken from the finished pi-4 chapters (asserted in those files)
PI4 = [
    ("1-matika.md", "người sẽ trở lại đời này"),
    ("4-tikapuggalapannatti.md", "Bậc vào dòng và bậc trở lại một lần"),
    ("4-tikapuggalapannatti.md", "Trong số đó, bậc đạo sư nào"),
    ("4-tikapuggalapannatti.md", "thì cần hiểu bậc đạo sư ấy là"),
]


def seg(*lines):
    return "\n".join(lines)


def build():
    c1 = tail(K1)
    c2 = tail(K2)
    c3 = tail(K3).replace(KHOI, KHOI + N_KAROTI, 1)
    assert c3 != tail(K3)
    c4 = tail(K4)
    c5 = tail(K5)
    c6 = tail(K6)
    assert c6.endswith(AGAMI_M)
    c6 = c6[:-len(AGAMI_M)] + AGANTA
    lines = [
        TATRA.format(c1, N("sammāsambuddho")),
        TATRA.format(c2, N("paccekasambuddho")),
        TATRA.format(c3, SARIPUTTA),
        TATRA.format(c4, AVASESA),
        TATRA.format(c5, N("anāgāmī")),
        TATRA.format(c6, SOTA_SAKA),
        S.CLOSER_CHAPTER[6] + " ^4-202",
    ]
    return [seg(S.H_CHAPTER[6] + " ^4-1-6-0"), seg(*lines)]


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
    assert "\n\n\n" not in text and "—" not in text and ":-" not in text and "…." not in text
    src = SRC.read_text(encoding="utf-8")
    assert structure(src) == structure(text), (structure(src), structure(text))
    OUT.write_text(text, encoding="utf-8", newline="\n")
    print("wrote", OUT, len(structure(text)), "segments")


if __name__ == "__main__":
    main()
