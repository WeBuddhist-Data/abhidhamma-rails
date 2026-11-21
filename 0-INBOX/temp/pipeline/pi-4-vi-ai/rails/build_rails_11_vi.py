"""pi-4 Puggalapaññatti, Vietnamese RAILS (plain audience): chapter 11 Dasakapuggalapaññatti (^4-1-10-0, ^4-209).

Builds AI_translation/vietnamese/pi-4-vietnamese-plain-rails_split_chapters/11-dasakapuggalapannatti.md from fixed
strings, importing the approved sample constants (build_rails_sample_vi as S: NAME, DESIG, headings, closers,
COLOPHON). The two questions use the approved dasaka matrix names (^4-M-16, S.NAME) and the answers the ekaka names
of the nine person types (^4-M-7, S.NAME), so identical Pāli gives byte-identical Vietnamese. No atthekacco name
occurs here (the coordinator's «có người» rule has nothing to apply to).
At build time: every string marked (pi-2) is asserted to occur in the approved pi-2 Vietnamese rails; strings taken
from the finished pi-4 chapters (matrix, ch7, ch9) are asserted to occur there; every person name used is asserted
to be a value of S.NAME; block IDs, per-segment line counts and per-line dash counts are checked against the Pāli.
Termbase: AI_translation/vietnamese/pi-4-pali-vietnamese-termbase-plain.md (+ pi-4-vi-ai/termbase/APPROVED.md).
New recurring strings: notes-rails-11.md.

usage: python -I -X utf8 build_rails_11_vi.py
"""
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-4-vi-ai\rails")
import build_rails_sample_vi as S  # noqa: E402  (import writes nothing)

ROOT = S.ROOT
SRC = ROOT / "AI_translation/pali/pi-4_split_chapters/11-dasakapuggalapannatti.md"
OUT = S.OUT_DIR / "11-dasakapuggalapannatti.md"
USED_NAMES = []


def N(k):
    v = S.NAME[k]
    USED_NAMES.append(v)
    return v


# ---------------------------------------------------------------------------------------------------------------
# Fixed strings (new ones are listed in notes-rails-11.md)
# ---------------------------------------------------------------------------------------------------------------
KATAMESAM = "{} là những ai?"                  # Katamesaṃ pañcannaṃ X? (question about persons, brief / formulas)
IMESAM = "đây là {}"                           # imesaṃ pañcannaṃ X (after «–»; ch9 «ime X» = «đây là X»)
YO_ARAHA = f"và người nào {S.DITTHE_DHAMME} là {{}}"
#   yo ca diṭṭheva dhamme arahā   («ngay trong đời này» pi-2; «người nào» as ch7 «người nào» / formulas «Yassa
#   puggalassa» = «Người nào»; arahā = S.NAME «bậc A-la-hán»; «là» added for grammar, no «hoti» in the Pāli)
ETTAVATA = S.cap(f"sự định danh về {S.DESIG['puggala']} bao quát đến mức ấy.")
#   Ettāvatā puggalānaṃ puggalapaññattīti.   (matrix frame «…; sự định danh về {X} bao quát đến mức ấy.», ^4-M-2..6)

# Strings taken unchanged from the approved pi-2 rails (asserted)
REUSED = [
    ("diṭṭheva dhamme", S.DITTHE_DHAMME, "2"),
]
# Strings taken from the finished pi-4 chapters (asserted in those files)
PI4 = [
    ("1-matika.md", "Năm hạng người đạt đến đích ở đời này, năm hạng người đạt đến đích sau khi rời khỏi đời này."),
    ("1-matika.md", "sự định danh về các yếu tố bao quát đến mức ấy."),
    ("1-matika.md", "Sự định danh về các hạng người bao quát đến mức nào?"),
    ("1-matika.md", S.MATIKA_END),
    ("9-atthakapuggalapannatti.md", "; đây là bốn hạng người có được con đường, đây là bốn hạng người"),
    ("7-chakkapuggalapannatti.md", "Trong số đó, người nào"),
]


def seg(*lines):
    return "\n".join(lines)


def build():
    idha = N("pañcannaṃ idha niṭṭhā")                # năm hạng người đạt đến đích ở đời này
    vihaya = N("pañcannaṃ idha vihāya niṭṭhā")        # năm hạng người đạt đến đích sau khi rời khỏi đời này
    first = [N("sattakkhattuparamo"), N("kolaṅkolo"), N("ekabījī"), N("sakadāgāmī")]
    l1 = (S.cap(KATAMESAM.format(idha)) + " "
          + S.cap(", ".join(first)) + " " + YO_ARAHA.format(N("arahā"))
          + " – " + IMESAM.format(idha) + ".")
    second = [N("antarāparinibbāyī"), N("upahaccaparinibbāyī"), N("asaṅkhāraparinibbāyī"),
              N("sasaṅkhāraparinibbāyī"),
              N("uddhaṃsotoakaniṭṭhagāmī")]  # Pāli «uddhaṃsotassa akaniṭṭhagāmino» (two words, one person type)
    l2 = (S.cap(KATAMESAM.format(vihaya)) + " "
          + S.cap(", ".join(second))
          + " – " + IMESAM.format(vihaya) + ".")
    lines = [l1, l2, ETTAVATA, S.CLOSER_CHAPTER[10], S.COLOPHON + " ^4-209"]
    return [seg(S.H_CHAPTER[10] + " ^4-1-10-0"), seg(*lines)]


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


def dashes(text):
    return [line.count("–") + line.count("—") for line in text.splitlines() if line.strip()]


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
    assert "\n\n\n" not in text and "—" not in text and ":-" not in text and "…." not in text and "\r" not in text
    assert "là là" not in text and "được được" not in text
    src = SRC.read_text(encoding="utf-8")
    assert structure(src) == structure(text), (structure(src), structure(text))
    assert dashes(src) == dashes(text), (dashes(src), dashes(text))
    OUT.write_text(text, encoding="utf-8", newline="\n")
    print("wrote", OUT, len(structure(text)), "segments")


if __name__ == "__main__":
    main()
