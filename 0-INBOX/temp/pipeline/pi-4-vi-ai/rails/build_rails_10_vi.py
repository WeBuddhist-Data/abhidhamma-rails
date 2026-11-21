"""pi-4 Puggalapaññatti, Vietnamese RAILS (plain audience): chapter 10 Navakapuggalapaññatti (^4-1-9-0, ^4-208).

Builds AI_translation/vietnamese/pi-4-vietnamese-plain-rails_split_chapters/10-navakapuggalapannatti.md from fixed
strings, importing the approved sample constants (build_rails_sample_vi as S: NAME, frames, headings, closers).
The nine definitions repeat ch2 ^4-22 .. ^4-30 with ch10 punctuation (commas, no dash, no quotes):
  - sammāsambuddho / paccekasambuddho: «Ở đời này, có người» + the chakka matrix clause (^4-M-12, S.CHAKKA) without
    its leading «có người » (identical Pāli: «…, tattha ca sabbaññutaṃ pāpuṇāti balesu ca vasībhāvaṃ»), as ch7;
  - ubhatobhāga- / paññāvimutto / kāyasakkhī: S.VIMOKKHA + «, và » + S.DISVA_* (ch4 ^4-95 comma form);
  - diṭṭhippatto / saddhāvimutto: the …pe… truths string of ch5 + the ch4 ^4-96/97 comma form;
  - dhammānusārī / saddhānusārī: the ch2 ^4-29/30 strings;
  - «Ayaṃ vuccati puggalo X.» (no dash, no quotes) = «Người này được gọi là X.» (ch5 ^4-171/172, ^4-188).
At build time: every (pi-2) string is asserted in the approved pi-2 rails; strings taken from the finished pi-4
chapters (2, 4, 5, 7) are asserted there; every person name is a value of S.NAME; block IDs and per-segment line
counts are checked against the Pāli chapter.
Termbase: AI_translation/vietnamese/pi-4-pali-vietnamese-termbase-plain.md (+ pi-4-vi-ai/termbase/APPROVED.md).
New recurring strings: notes-rails-10.md.

usage: python -I -X utf8 build_rails_10_vi.py
"""
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-4-vi-ai\rails")
import build_rails_sample_vi as S  # noqa: E402  (import writes nothing)

ROOT = S.ROOT
SRC = ROOT / "AI_translation/pali/pi-4_split_chapters/10-navakapuggalapannatti.md"
OUT = S.OUT_DIR / "10-navakapuggalapannatti.md"
USED_NAMES = []


def N(k):
    v = S.NAME[k]
    USED_NAMES.append(v)
    return v


def tail(k):
    """A chakka matrix clause without «có người » (the frame «Ở đời này, có người» supplies it here)."""
    v = N(k)
    assert v.startswith("có người "), v
    return v[len("có người "):]


# ---------------------------------------------------------------------------------------------------------------
# Fixed strings
# ---------------------------------------------------------------------------------------------------------------
K1 = "… abhisambujjhati, tattha ca sabbaññutaṃ pāpuṇāti balesu ca vasībhāvaṃ"
K2 = "… abhisambujjhati, na ca tattha sabbaññutaṃ pāpuṇāti na ca balesu vasībhāvaṃ"


def called(name):                    # Ayaṃ vuccati puggalo X.   (no dash, no quotes)
    return f"Người này được gọi là {name}."


TRUTHS_PE = ("hiểu rõ đúng như thật: “Đây là khổ đau”… hiểu rõ đúng như thật: "
             "“Đây là cách thực hành dẫn đến sự chấm dứt khổ đau”")
#   "idaṃ dukkha"nti yathābhūtaṃ pajānāti…pe… "ayaṃ dukkhanirodhagāminī paṭipadā"ti yathābhūtaṃ pajānāti  (ch5)
assert TRUTHS_PE.startswith(S.TRUTHS.split(", hiểu rõ")[0]) and TRUTHS_PE.endswith(S.TRUTHS.split(", ")[-1])
TATHAGATA_LC = "v" + S.TATHAGATA[1:-1]   # , tathāgatappaveditā cassa dhammā paññāya vodiṭṭhā honti vocaritā,  (ch4)
NO_CA_KHO = f"nhưng quả thật không như ở {S.NAME['diṭṭhippatto']}"   # no ca kho yathā diṭṭhippattassa  (ch2, ch4)


def anusari(x):                      # Yassa puggalassa sotāpatti…paṭipannassa X-indriyaṃ adhimattaṃ hoti, … bhāveti.
    return (f"Người nào, khi đang thực hành để tự mình chứng nghiệm thành quả vào dòng, có năng lực {x} vượt trội, "
            f"tu tập con đường cao quý được {x} dẫn dắt, có {x} đi trước.")


def phale(a, b):                     # Sotāpatti…paṭipanno puggalo A, phale ṭhito B(ti).
    return f"{S.cap(N('sotāpattiphalasacchikiriyāya paṭipanno'))} là {a}, {N('phaleṭhito')} là {b}."


# Strings taken unchanged from the approved pi-2 rails (asserted)
REUSED = [
    ("yathābhūtaṃ pajānāti", "hiểu rõ đúng như thật", "2"),
    ("dukkhanirodhagāminī paṭipadā", "cách thực hành dẫn đến sự chấm dứt khổ đau", "2"),
    ("Tathāgata", "Như Lai", "2"),
]
# Strings taken from the finished pi-4 chapters (asserted in those files)
PI4 = [
    ("2-ekakapuggalapannatti.md", "Người nào, khi đang thực hành để tự mình chứng nghiệm thành quả vào dòng, có năng "
     "lực trí tuệ vượt trội, tu tập con đường cao quý được trí tuệ dẫn dắt, có trí tuệ đi trước"),
    ("2-ekakapuggalapannatti.md", "Người nào, khi đang thực hành để tự mình chứng nghiệm thành quả vào dòng, có năng "
     "lực niềm tin vượt trội, tu tập con đường cao quý được niềm tin dẫn dắt, có niềm tin đi trước"),
    ("2-ekakapuggalapannatti.md", "Người đang thực hành để tự mình chứng nghiệm thành quả vào dòng là người đi theo "
     "Giáo Pháp, người đã đứng vững trong thành quả là người đạt đến quan điểm."),
    ("2-ekakapuggalapannatti.md", "Người đang thực hành để tự mình chứng nghiệm thành quả vào dòng là người đi theo "
     "niềm tin, người đã đứng vững trong thành quả là người được giải thoát nhờ niềm tin."),
    ("2-ekakapuggalapannatti.md", "Ở đời này, có người quả thật không chạm đến tám sự giải thoát bằng thân rồi an trú"),
    ("4-tikapuggalapannatti.md", "Ở đời này, có người chạm đến tám sự giải thoát bằng thân rồi an trú, và nhờ thấy "
     "bằng trí tuệ, một số ô nhiễm của người ấy được diệt tận"),
    ("4-tikapuggalapannatti.md", "“Đây là cách thực hành dẫn đến sự chấm dứt khổ đau”, và Giáo Pháp do Như Lai tuyên "
     "bố được người ấy thấy rõ và thông suốt bằng trí tuệ, và nhờ thấy bằng trí tuệ, một số ô nhiễm của người ấy "
     "được diệt tận"),
    ("4-tikapuggalapannatti.md", "một số ô nhiễm của người ấy được diệt tận, nhưng quả thật không như ở người đạt đến "
     "quan điểm"),
    ("5-catukkapuggalapannatti.md", TRUTHS_PE),
    ("7-chakkapuggalapannatti.md", "người nào tự mình giác ngộ các sự thật trong những điều chưa từng được nghe trước "
     "đây, và trong đó đạt đến sự toàn tri, và sự làm chủ đối với các sức mạnh"),
    ("7-chakkapuggalapannatti.md", "người nào tự mình giác ngộ các sự thật trong những điều chưa từng được nghe trước "
     "đây, và trong đó không đạt đến sự toàn tri, và không đạt đến sự làm chủ đối với các sức mạnh"),
]


def seg(*lines):
    return "\n".join(lines)


def build():
    IDH = S.IDHEKACCO
    vim = f"{IDH} {S.VIMOKKHA}"                               # Idhekacco puggalo aṭṭha vimokkhe … viharati
    na_vim = f"{IDH} {S.NA_HEVA_KHO} {S.VIMOKKHA}"            # Idhekacco puggalo na heva kho aṭṭha vimokkhe …
    ditthi_body = f"{IDH} {TRUTHS_PE}, {TATHAGATA_LC}, và {S.DISVA_EKACCE}"
    nm = {k: N(k) for k in ("sammāsambuddho", "paccekasambuddho", "ubhatobhāgavimutto", "paññāvimutto",
                            "kāyasakkhī", "diṭṭhippatto", "saddhāvimutto", "dhammānusārī", "saddhānusārī")}

    def d(k, body):
        return f"{S.q_katamo(nm[k])} {body} {called(nm[k])}"

    lines = [
        d("sammāsambuddho", f"{IDH} {tail(K1)}."),
        d("paccekasambuddho", f"{IDH} {tail(K2)}."),
        d("ubhatobhāgavimutto", f"{vim}, và {S.DISVA_SABBE}."),       # viharati paññāya … (comma missing in Pāli)
        d("paññāvimutto", f"{na_vim}, và {S.DISVA_SABBE}."),
        d("kāyasakkhī", f"{vim}, và {S.DISVA_EKACCE}."),
        d("diṭṭhippatto", f"{ditthi_body}."),
        d("saddhāvimutto", f"{ditthi_body}, {NO_CA_KHO}."),
        d("dhammānusārī", anusari("trí tuệ")) + " " + phale(nm["dhammānusārī"], nm["diṭṭhippatto"]),
        d("saddhānusārī", anusari("niềm tin")) + " " + phale(nm["saddhānusārī"], nm["saddhāvimutto"]),
        S.CLOSER_CHAPTER[9] + " ^4-208",
    ]
    return [seg(S.H_CHAPTER[9] + " ^4-1-9-0"), seg(*lines)]


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


def nfc(s):
    return unicodedata.normalize("NFC", s)


def check_reused():
    texts = {b: nfc("\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md")))).lower()
             for b, d in S.RAILS.items()}
    bad = [(p, v, b) for p, v, b in REUSED if nfc(v).lower() not in texts[b]]
    assert not bad, "reused strings not found in their rails: " + repr(bad)
    bad = [(f, v) for f, v in PI4 if nfc(v) not in nfc((S.OUT_DIR / f).read_text(encoding="utf-8"))]
    assert not bad, "pi-4 strings not found in their chapters: " + repr(bad)


def main():
    check_reused()
    segs = build()
    names = set(S.NAME.values())
    assert all(n in names for n in USED_NAMES)
    text = nfc("\n\n".join(segs) + "\n")
    assert "\n\n\n" not in text and "—" not in text and ":-" not in text and "…." not in text
    assert text.count("“") == text.count("“Đây") == 4         # names unquoted, as in the Pāli
    for p in PI4[:9]:                                         # the reused chapter strings really are in the output
        assert nfc(p[1]) in text, p
    for p in PI4[9:]:                                         # ch7 «người nào» + clause = «có người» + clause here
        assert "có " + nfc(p[1]) .replace("người nào ", "người ", 1) in text, p
    src = SRC.read_text(encoding="utf-8")
    assert structure(src) == structure(text), (structure(src), structure(text))
    OUT.write_text(text, encoding="utf-8", newline="\n")
    print("wrote", OUT, len(structure(text)), "segments")


if __name__ == "__main__":
    main()
