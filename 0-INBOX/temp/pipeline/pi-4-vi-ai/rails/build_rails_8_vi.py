"""pi-4 Puggalapaññatti, Vietnamese RAILS (plain audience): chapter 8 Sattakapuggalapaññatti (^4-1-7-0, ^4-203 .. ^4-206).

Builds AI_translation/vietnamese/pi-4-vietnamese-plain-rails_split_chapters/8-sattakapuggalapannatti.md from fixed
strings, importing the approved sample constants (build_rails_sample_vi as S: NAME, frames, headings, closers).
Every repeat is one constant, so identical Pāli gives byte-identical Vietnamese.
At build time: every string marked (pi-2) is asserted to occur in the approved pi-2 Vietnamese rails; strings taken
from the finished pi-4 chapters (ch2, ch4, ch7) are asserted to occur there; every person name used is asserted to be
a value of S.NAME; block IDs and per-segment line counts are checked against the Pāli chapter.
Termbase: AI_translation/vietnamese/pi-4-pali-vietnamese-termbase-plain.md (+ pi-4-vi-ai/termbase/APPROVED.md).
New recurring strings: notes-rails-8.md.

usage: python -I -X utf8 build_rails_8_vi.py
"""
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-4-vi-ai\rails")
import build_rails_sample_vi as S  # noqa: E402  (import writes nothing)

ROOT = S.ROOT
SRC = ROOT / "AI_translation/pali/pi-4_split_chapters/8-sattakapuggalapannatti.md"
OUT = S.OUT_DIR / "8-sattakapuggalapannatti.md"
USED_NAMES = []

cap = S.cap
I = S.IDHEKACCO                                   # Idhekacco puggalo = Ở đời này, có người


def N(k):
    v = S.NAME[k]
    USED_NAMES.append(v)
    return v


def bare_close(name):
    """Ayaṃ vuccati puggalo X. (no dash, no quotes in the Pāli: brief «Người này được gọi là X.»)"""
    return f"Người này được gọi là {name}."


# ---------------------------------------------------------------------------------------------------------------
# Fixed strings (new ones are listed in notes-rails-8.md)
# ---------------------------------------------------------------------------------------------------------------
# the water simile: matrix names ^4-M-13 (S.NAME keys)
K_NIMUGGO = "sakiṃ nimuggo nimuggova hoti"
K_NIMUJJATI = "ummujjitvā nimujjati"
K_THITO = "ummujjitvā ṭhito hoti"
K_VIPASSATI = "ummujjitvā vipassati viloketi"
K_PATARATI = "ummujjitvā patarati"
K_GADHA = "ummujjitvā paṭigādhappatto hoti"       # the definition spells patigādhappatto (termbase: same rendering)
K_TINNO = "ummujjitvā tiṇṇo hoti pāraṅgato thale tiṭṭhati brāhmaṇo"

KALAKA = f"{I} mang các hiện tượng bất thiện hoàn toàn đen tối."
#   Idhekacco puggalo samannāgato hoti ekantakāḷakehi akusalehi dhammehi.   (samannāgata «mang» for bad states)

KUSALA = "trong các hiện tượng thiện"                                       # kusalesu dhammesu
SADHU = "tốt thay"                                                          # sāhu / sādhu
N_SAHU = " [khác chính tả (Sī., Syā.): sāhu, cũng vậy ở cả ba chỗ]"          # [sāhu (sī. syā.) evaṃ tīsu ṭhānesupi]
N_VIRIYA = " [khác chính tả (Sī., Syā.): viriyaṃ]"                           # [viriyaṃ (sī. syā.)]
FACULTIES = ["niềm tin", "sự biết hổ thẹn", "sự biết ghê sợ tội lỗi", "sự tinh tấn", "trí tuệ"]
#   saddhā, hirī, ottappaṃ, vīriyaṃ, paññā


def good_quote(notes=False):
    """"sāhu saddhā kusalesu dhammesu, sādhu hirī …, sādhu paññā kusalesu dhammesū"ti"""
    parts = []
    for i, f in enumerate(FACULTIES):
        head = SADHU
        if notes and i == 1:
            head += N_SAHU
        fac = f
        if notes and i == 3:
            fac += N_VIRIYA
        parts.append(f"{head} {fac} {KUSALA}")
    return "“" + cap(", ".join(parts)) + "”"


def emerges(notes=False):
    """Idhekacco puggalo ummujjati "…"ti."""
    return f"{I} trồi lên với ý nghĩ: {good_quote(notes)}."


DECLINES = "không đứng yên, không tăng trưởng mà chỉ suy giảm"   # neva tiṭṭhati no vaḍḍhati hāyatiyeva
STEADY = "không suy giảm, không tăng trưởng mà đứng yên"         # neva hāyati no vaḍḍhati ṭhitā / ṭhitaṃ hoti


def each_faculty(pred):
    """Tassa sā saddhā …, tassa sā hirī …, tassa taṃ ottappaṃ …, tassa taṃ vīriyaṃ …, tassa sā paññā …."""
    return cap("; ".join(f"{f} ấy của người ấy {pred}" for f in FACULTIES)) + "."


SOTAPANNA = "Người ấy " + S.SOTAPANNA_INTRO[len(I) + 1:] + "."
#   So tiṇṇaṃ saṃyojanānaṃ parikkhayā sotāpanno hoti avinipātadhammo niyato sambodhiparāyano.   (ch2)
KHOI = f"trở thành người {S.DUKKHASSANTA}"                       # dukkhassantakaro hoti   (ch7)
SAKADAGAMI = (f"Người ấy nhờ diệt tận hoàn toàn ba xiềng xích và nhờ sự suy yếu của tham đắm, sân hận và si mê mà "
              f"trở thành {N('sakadāgāmī')}, và sau khi trở lại thế gian này chỉ một lần, {KHOI}.")
#   So tiṇṇaṃ saṃyojanānaṃ parikkhayā rāgadosamohānaṃ tanuttā sakadāgāmī hoti sakideva imaṃ lokaṃ āgantvā
#   dukkhassantakaro hoti.   (ch2 ^4-34 with dukkhassantakaro hoti)
ANAGAMI = "Người ấy " + S.ANAGAMI_INTRO[len(I) + 1:] + "."
#   So pañcannaṃ orambhāgiyānaṃ saṃyojanānaṃ parikkhayā opapātiko hoti tattha parinibbāyī anāvattidhammo tasmā lokā.
KHAYA = "nhờ sự diệt tận các ô nhiễm"                                                         # āsavānaṃ khayā   (pi-2)
ARAHATTA_REST = ("ngay trong đời này tự mình hiểu biết trực tiếp, chứng nghiệm, chứng nhập và an trú "
                 f"{S.CETOVIMUTTI}, không còn ô nhiễm")                                        # (pi-2, ch4)
#   anāsavaṃ cetovimuttiṃ paññāvimuttiṃ diṭṭheva dhamme sayaṃ abhiññā sacchikatvā upasampajja viharati
ARAHANT = f"Người ấy, {KHAYA}, {ARAHATTA_REST}."                  # So āsavānaṃ khayā … viharati.

# Strings taken unchanged from the approved pi-2 rails (asserted)
REUSED = [
    ("āsavānaṃ khayā", KHAYA, "2"),
    ("anāsavaṃ cetovimuttiṃ paññāvimuttiṃ diṭṭheva dhamme sayaṃ abhiññā sacchikatvā upasampajja viharati",
     ARAHATTA_REST, "2"),
    ("diṭṭheva dhamme", S.DITTHE_DHAMME, "2"),
    ("cetovimuttiṃ paññāvimuttiṃ", S.CETOVIMUTTI, "2"),
]
# Strings taken from the finished pi-4 chapters (asserted in those files)
PI4 = [
    ("2-ekakapuggalapannatti.md", S.SOTAPANNA_INTRO[len(I) + 1:]),
    ("2-ekakapuggalapannatti.md", S.ANAGAMI_INTRO[len(I) + 1:]),
    ("2-ekakapuggalapannatti.md", "nhờ diệt tận hoàn toàn ba xiềng xích và nhờ sự suy yếu của tham đắm, sân hận và si mê "
                                  "mà trở thành bậc trở lại một lần, và sau khi trở lại thế gian này chỉ một lần,"),
    ("2-ekakapuggalapannatti.md", f"{I} {S.VIMOKKHA}"),
    ("2-ekakapuggalapannatti.md", "có năng lực niềm tin vượt trội, tu tập con đường cao quý được niềm tin dẫn dắt, "
                                  "có niềm tin đi trước"),
    ("2-ekakapuggalapannatti.md", "Người đang thực hành để tự mình chứng nghiệm thành quả vào dòng là người đi theo "
                                  "niềm tin, người đã đứng vững trong thành quả là người được giải thoát nhờ niềm tin."),
    ("4-tikapuggalapannatti.md", f"{KHAYA}, {ARAHATTA_REST}"),
    ("4-tikapuggalapannatti.md", f"{S.VIMOKKHA}, và {S.DISVA_EKACCE}"),
    ("7-chakkapuggalapannatti.md", KHOI),
]


def seg(*lines):
    return "\n".join(lines)


def build():
    qk, ev = S.q_kathanca, S.evam
    water = [
        f"{qk(N(K_NIMUGGO))} {KALAKA} {ev(N(K_NIMUGGO))}",
        f"{qk(N(K_NIMUJJATI))} {emerges(notes=True)} {each_faculty(DECLINES)} {ev(N(K_NIMUJJATI))}",
        f"{qk(N(K_THITO))} {emerges()} {each_faculty(STEADY)} {ev(N(K_THITO))}",
        f"{qk(N(K_VIPASSATI))} {emerges()} {SOTAPANNA} {ev(N(K_VIPASSATI))}",
        f"{qk(N(K_PATARATI))} {emerges()} {SAKADAGAMI} {ev(N(K_PATARATI))}",
        f"{qk(N(K_GADHA))} {emerges()} {ANAGAMI} {ev(N(K_GADHA))}",
        f"{qk(N(K_TINNO))} {emerges()} {ARAHANT} {ev(N(K_TINNO))} ^4-203",
    ]
    ubh = N("ubhatobhāgavimutto")
    l204 = (f"{S.q_katamo(ubh)} {I} {S.VIMOKKHA}, và {S.DISVA_SABBE}. {bare_close(ubh)} ^4-204")
    #   Idhekacco puggalo aṭṭha vimokkhe kāyena phusitvā viharati paññāya cassa disvā āsavā parikkhīṇā honti.
    #   Ayaṃ vuccati puggalo ubhatobhāgavimutto.   (no punctuation before paññāya: «, và» as ch4 ^4-95)
    l205 = ("Thế nào là " + "… ".join(N(k) for k in ("paññāvimutto", "kāyasakkhī", "diṭṭhippatto", "saddhāvimutto",
                                                      "dhammānusārī")) + "… ^4-205")
    #   Katamo ca puggalo paññāvimutto…pe… kāyasakkhī… diṭṭhippatto… saddhāvimutto… dhammānusārī ….
    #   (…pe… = «…»; the closing « …." = «…» as pi-3 4-catutthanayo; never «….»)
    sa = N("saddhānusārī")
    l206 = (f"{S.q_katamo(sa)} Người nào, khi {N('sotāpattiphalasacchikiriyāya paṭipanno')[len('người '):]}, "
            "có năng lực niềm tin vượt trội, tu tập con đường cao quý được niềm tin dẫn dắt, có niềm tin đi trước. "
            f"{bare_close(sa)} {cap(N('sotāpattiphalasacchikiriyāya paṭipanno'))} là {sa}, "
            f"người đã đứng vững trong thành quả là {N('saddhāvimutto')}.")
    #   Yassa puggalassa sotāpattiphalasacchikiriyāya paṭipannassa saddhindriyaṃ adhimattaṃ hoti, saddhāvāhiṃ
    #   saddhāpubbaṅgamaṃ ariyamaggaṃ bhāveti. Ayaṃ vuccati puggalo saddhānusārī. Sotāpattiphalasacchikiriyāya
    #   paṭipanno puggalo saddhānusārī, phale ṭhito saddhāvimuttoti.   (ch2 ^4-30; closing «ti» not rendered)
    return [seg(S.H_CHAPTER[7] + " ^4-1-7-0"), seg(*water), seg(l204), seg(l205),
            seg(l206, S.CLOSER_CHAPTER[7] + " ^4-206")]


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
