"""pi-5 Kathāvatthu, Vietnamese RAILS (plain audience): chapter 31, Tevīsatimavaggo (^5-31-0 … ^5-918), the LAST
chapter of the book: nine kathās (218-226) with the repeated "Tevīsatimavaggo" sub-headings, the vagga close and
uddāna, the close of the small half-fifty (Khuddako aḍḍhapaṇṇāsako. / Tassuddānaṃ – / its uddāna; frame of ch13,
Tassuddānaṃ rule of ch18), the summary of the fifty-groups (Paṇṇāsakuddānaṃ –, three verse lines), the count of
recitation portions and the book colophon (built like pi-4's «Bộ “Định danh các hạng người” đã hoàn tất.»).

Builds AI_translation/vietnamese/pi-5-vietnamese-plain-rails_split_chapters/31-tevisatimavaggo.md from the fixed
strings below, importing the approved sample builder READ-ONLY. Strings taken from pi-1 … pi-4 rails are asserted
there (REUSED31); strings shared with the finished pi-5 rails chapters are asserted in those chapter files (SHARED).
The per-line dash / quote / NFC / id checks of S.check_against_pali run before writing.
New recurring strings: notes-rails-31.md.

usage: python -I -X utf8 -B build_rails_31_vi.py          (writes the chapter and the adherence copy rails\\adh-31\\)
       python -I -X utf8 -B build_rails_31_vi.py --find <regex> [max] [chars]   (look up finished pi-5 rails chapters)
       python -I -X utf8 -B build_rails_31_vi.py --tb | --word <regex>          (termbase lookups)
"""
import pathlib
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai\rails")
import build_rails_sample_vi as S  # noqa: E402

NAME = "31-tevisatimavaggo.md"
Q, q, NANU, PE, YES, NO, NO_PE = S.Q, S.q, S.NANU, S.PE, S.YES, S.NO, S.NO_PE
cap = S.cap
ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
TB = ROOT / "AI_translation/vietnamese/pi-5-pali-vietnamese-termbase-plain.md"
KW = ROOT / "AI_translation/pali/pi-5-keywords-by-reference-pali-plain.md"
PDIR = S.PALI_DIR
VDIR = S.OUT_DIR


def nanu_l(x):                      # nanu Xti? (after …pe…, lower case; ch15)
    return f"chẳng phải {x} sao?"


# ---------------------------------------------------------------------------------------------------------------
# Headings, kathā names, vagga close, half-fifty close, summary of the fifties, colophon
# ---------------------------------------------------------------------------------------------------------------
VAGGA = "Chương thứ hai mươi ba"                                        # Tevīsatimavaggo (termbase)
KATHA = {1: "cùng một ý định",                                          # Ekādhippāya- (termbase ekādhippāya)
         2: "hình dạng của các bậc A-la-hán",                           # Arahantavaṇṇa- (termbase arahantavaṇṇa)
         3: "việc làm theo ý muốn nhờ quyền uy và các mục khác",        # Issariyakāmakārikādikathā (termbase heading)
         "3e": "việc làm theo ý muốn nhờ quyền uy",                     # Issariyakāmakārikākathā niṭṭhitā (termbase)
         4: "cái tương tự",                                             # Patirūpakathā (termbase heading)
         5: "cái không được hình thành trọn vẹn"}                       # Aparinipphanna- (termbase parinipphanna)
TASSUDDANAM = "Tóm tắt của chương này –"                               # Tassuddānaṃ – (ch9; after the vagga close)
KHUDDAKO = "Nhóm nửa năm mươi nhỏ."                                     # Khuddako aḍḍhapaṇṇāsako. (termbase aḍḍhapaṇṇāsako; ch13 frame)
TASS50 = "Tóm tắt của nhóm này –"                                       # Tassuddānaṃ – after a fifty-group close (ch18)
UDD50 = "Mới, sự nhập Niết-bàn, cùng một ý định."                       # Navaṃ, nibbuti, ekādhippāyoti.
PANNASA_UDD = "Tóm tắt của các nhóm năm mươi –"                         # Paṇṇāsakuddānaṃ –
MAHA50 = "Nhóm năm mươi lớn"                                            # Mahāpaṇṇāsako. (ch13) for "Mahā-"
VERSE = [
    f"{MAHA50}, sự cố định, các khuynh hướng tiềm ẩn, sự chế ngự, với nhóm nửa năm mươi nhỏ là thứ năm;",
    #   Mahāniyāmo, anusayā, niggaho, khuddakapañcamo; (niyāma ch18, anusayā ch23, niggaho ch28 fifty-uddānas;
    #   "…pañcamo" as ch13 «với sự giải thoát là thứ năm»)
    "Nghiền nát các học thuyết của người khác, được thiết lập vững chắc trên gốc rễ của kinh;",
    #   Parappavādamaddanā, suttamūlasamāhitā; (termbase maddanā, para, pavāda, sutta, mūla, samāhitā)
    "Soi sáng giáo thuyết của bậc đạo sư, trong Bộ “Các vấn đề tranh luận”.",
    #   Ujjotanā satthusamaye, kathāvatthupakaraṇeti. (termbase Ujjotanā, samaye, satthāraṃ, pakaraṇe, kathāvatthu)
]
BHANAVARA = "Ba mươi lăm phần tụng đọc"                                 # Pañcattiṃsabhāṇavāraṃ (no full stop, as written)
COLOPHON = "Bộ “Các vấn đề tranh luận” đã hoàn tất."                   # Kathāvatthupakaraṇaṃ niṭṭhitaṃ. (pi-4 frame)

# ---- shared vocabulary -----------------------------------------------------------------------------------------
EKA = "với cùng một ý định"                                             # ekādhippāyena
METHUNA = "hưởng thụ hành vi dâm dục"                                   # methunaṃ dhammaṃ paṭisevati (ch10)
CRIMES = ["sát hại sinh mạng", "lấy của không được cho", "nói dối", "nói lời chia rẽ", "nói lời thô ác",
          "nói lời phù phiếm", "đột nhập nhà", "cướp bóc", "cướp một ngôi nhà", "mai phục bên đường",
          "đi lại với vợ người khác", "cướp phá làng", "cướp phá thị trấn"]   # pāṇaṃ hanati … nigamaghātakaṃ karoti (ch10)
AMAN = "những chúng sinh không phải loài người, trong hình dạng của các bậc A-la-hán,"
#   arahantānaṃ vaṇṇena amanussā (termbase amanussā, arahantānaṃ vaṇṇena)
BS = "Bồ-tát, do việc làm theo ý muốn nhờ quyền uy,"                    # bodhisatto issariyakāmakārikāhetu
VINI = "đi đến nơi đọa lạc"                                             # vinipātaṃ gacchati (termbase; ch11 «nơi đọa lạc»)
GABBHA = "nhập vào bào thai"                                            # gabbhaseyyaṃ okkamati (termbase)
DUKKARA = "đã làm những việc khổ hạnh khó làm"                          # dukkarakārikaṃ akāsi (termbase phrase)
APARA = "đã làm khổ hạnh khác"                                          # aparantapaṃ akāsi (ch12)
VAR_APARA = " [dị bản (Tương Ưng Bộ Kinh 1.137): amaraṃ tapaṃ]"        # [amaraṃ tapaṃ (saṃ. ni. 1.137)] (ch12)
SATTHA = "đã tôn xưng một vị khác làm bậc đạo sư"                       # aññaṃ satthāraṃ uddisi (ch12)
HELLS = ["địa ngục", "địa ngục Đẳng Hoạt", "địa ngục Hắc Thằng", "địa ngục Viêm Nhiệt", "địa ngục Đại Viêm Nhiệt",
         "địa ngục Chúng Hợp", "địa ngục Khiếu Hoán", "địa ngục Vô Gián"]
#   nirayaṃ, sañjīvaṃ, kālasuttaṃ, tāpanaṃ, mahātāpanaṃ, saṅghātakaṃ, roruvaṃ (termbase «địa ngục Khiếu Hoán»), avīciṃ
VAR_HELL = S.var("Sī., Syā., Kaṃ., Pī.", "patāpanaṃ")                    # [patāpanaṃ (sī. syā. kaṃ. pī.)]
VIEWS = ["Thế gian là trường tồn", "Thế gian không trường tồn", "Thế gian là hữu hạn", "Thế gian là vô hạn",
         "Linh hồn và thân thể là một", "Linh hồn là khác, thân thể là khác", "Như Lai còn tồn tại sau khi chết",
         "Như Lai không còn tồn tại sau khi chết", "Như Lai vừa còn tồn tại vừa không còn tồn tại sau khi chết",
         "Như Lai không phải còn tồn tại cũng không phải không còn tồn tại sau khi chết"]   # (pi-1; ch22)
ACCEPT = "đã chấp nhận"                                                 # paccāgacchi (termbase)
NO_HAVE = "Không có."                                                   # Natthi. (ch12, ch14)
ATTH_L = "có bài kinh như vậy thật không?"                              # "…"ti – attheva suttantoti? (ch14)


def sutta_frame(x):                 # X? Āmantā. "X"ti – attheva suttantoti? Natthi. Hañci "x"ti – nattheva suttanto, …
    return (f"{Q(x)} {YES} “{cap(x)}” – {ATTH_L} {NO_HAVE} Nếu “{x}” – không có bài kinh như vậy thật, "
            f"thì {S.RE}, chắc chắn không nên nói – “{x}”.")


# ---- look-alikes (patirūpa) --------------------------------------------------------------------------------------
def pati(x):                        # atthi na X X-patirūpako
    return f"có cái không phải là {x} nhưng tương tự {x}"


P10 = ["sự tiếp xúc", "cảm giác", "tri giác", "chủ ý", "tâm", "niềm tin", "sự tinh tấn", "sự tỉnh thức",
       "sự định tâm", "trí tuệ"]                                         # phasso … paññā (ch17, ch23)
DMK = ["sự sân hận", "sự si mê", "phiền não"]                           # doso, moho, kileso (termbase)
LUST = "sự tham đắm"                                                    # rāgo (termbase)

# ---- not fully produced (aparinipphanna) -----------------------------------------------------------------------
APN = "không được hình thành trọn vẹn"                                  # aparinipphanna (termbase parinipphanna)
PN = "được hình thành trọn vẹn"
ANICCA_L = S.ANICCA.split(", ")                                         # aniccaṃ … vipariṇāmadhammaṃ (sample)
NEG = ", ".join(f"không {x}" for x in ANICCA_L)                         # na aniccaṃ na saṅkhataṃ … (negated list)
DUKKHA_ONLY = "chỉ khổ đau mới được hình thành trọn vẹn"               # dukkhaññeva parinipphannaṃ (ch25 «chỉ … mới»)
YAD = "cái gì vô thường thì cái ấy là khổ đau"                          # yadaniccaṃ taṃ dukkhaṃ (ch10, ch25)
CIT315 = " [Tương Ưng Bộ Kinh 3.15]"
AV = S.ANNATAVI                                                         # aññātāvindriyaṃ (pi-2)


def full(x):                        # X aniccaṃ saṅkhataṃ … vipariṇāmadhammaṃ
    return f"{x} là {S.ANICCA}"


def short(x):                       # X aniccaṃ saṅkhataṃ…pe… vipariṇāmadhammaṃ
    return f"{x} là {ANICCA_L[0]}, {ANICCA_L[1]}{PE} {ANICCA_L[-1]}"


def yad_line(x, cit="", pe=False):  # Dukkhaññeva …? Āmantā. Nanu yadaniccaṃ … – "X anicca"nti? Āmantā. Hañci …
    p = f"{YAD}, Đức Thế Tôn đã nói – «{x} là vô thường»"
    h = S.hanci_neg(p, DUKKHA_ONLY)
    return (f"{Q(DUKKHA_ONLY)} {YES} Chẳng phải {YAD}{cit}, Đức Thế Tôn đã nói – “{x} là vô thường” sao? {YES} "
            + (h[:-1] + PE if pe else h))


UDDANA = (f"{cap(EKA)} thì được phép {METHUNA}, {AMAN} {METHUNA}, {BS} {VINI}, {GABBHA}, {DUKKARA}, {APARA}, "
          f"{SATTHA}, {', '.join(pati(x) for x in [LUST] + DMK)}, vật chất {APN}, {AV} {APN}.")

REUSED31 = [  # (Pāli, Vietnamese, book)
    ("sassato lokoti vā, asassato lokoti vā …", "“Thế gian là trường tồn”, hoặc “Thế gian không trường tồn”", "1"),
    ("antavā / anantavā loko", "“Thế gian là hữu hạn”, hoặc “Thế gian là vô hạn”", "1"),
    ("taṃ jīvaṃ taṃ sarīraṃ / aññaṃ …", "“Linh hồn và thân thể là một”, hoặc “Linh hồn là khác, thân thể là khác”", "1"),
    ("hoti / na hoti tathāgato paraṃ maraṇā",
     "“Như Lai còn tồn tại sau khi chết”, hoặc “Như Lai không còn tồn tại sau khi chết”", "1"),
    ("hoti ca na ca hoti / neva hoti na na hoti tathāgato paraṃ maraṇā",
     "“Như Lai vừa còn tồn tại vừa không còn tồn tại sau khi chết”, hoặc “Như Lai không phải còn tồn tại cũng không "
     "phải không còn tồn tại sau khi chết”", "1"),
    ("Puggalapaññattipakaraṇaṃ niṭṭhitaṃ.", "Bộ “Định danh các hạng người” đã hoàn tất.", "4"),
    ("aññātāvindriya", AV, "2"),
]

SHARED = [  # (Pāli, Vietnamese, finished pi-5 rails chapter)
    ("Tassuddānaṃ –", TASSUDDANAM, "9-hevatthikatha.md"),
    ("Mahāpaṇṇāsako.", MAHA50 + ".", "13-pancamavaggo.md"),
    ("vimuttipañcamanti", "với sự giải thoát là thứ năm", "13-pancamavaggo.md"),
    ("Tassuddānaṃ – (after Dutiyo paṇṇāsako.)", f"Nhóm năm mươi thứ hai.\n{TASS50}\nSự cố định, ", "18-dasamavaggo.md"),
    ("Tatiyo paṇṇāsako. … Anusayā", f"Nhóm năm mươi thứ ba.\n{TASS50}\nCác khuynh hướng tiềm ẩn, ",
     "23-pannarasamavaggo.md"),
    ("Catuttho paṇṇāsako. … Niggaho (ch28, being finished at the same time)",
     f"Nhóm năm mươi thứ tư.\n{TASS50}\nSự chế ngự, ", "28-visatimavaggo.md"),
    ("methunaṃ dhammaṃ paṭiseveyya", METHUNA, "10-dutiyavaggo.md"),
    ("pāṇaṃ haneyya … nigamaghātaṃ kareyya", ", ".join(CRIMES), "10-dutiyavaggo.md"),
    ("vinipātaṃ", "nơi đọa lạc", "11-tatiyavaggo.md"),
    ("Bodhisatto aparantapaṃ [amaraṃ tapaṃ (saṃ. ni. 1.137)] akāsi, aññaṃ satthāraṃ uddisīti?",
     f"Có phải Bồ-tát {APARA}{VAR_APARA}, {SATTHA} không?", "12-catutthavaggo.md"),
    ('"…"nti – attheva suttantoti? Natthi.', f"” – {ATTH_L} {NO_HAVE}", "14-chatthavaggo.md"),
    ('Hañci "…"nti – attheva suttanto, no ca vata re vattabbe –',
     "” – có bài kinh như vậy thật, thì này bạn, chắc chắn không nên nói – “", "14-chatthavaggo.md"),
    ("nirayaṃ upapajjeyya, tiracchānayoniṃ upapajjeyya", "có thể tái sinh vào địa ngục, tái sinh vào cõi súc sinh",
     "20-dvadasamavaggo.md"),
    ("Kappaṭṭho iddhimāti? Na hevaṃ vattabbe…pe…", f"có thần thông không? {NO_PE}", "21-terasamavaggo.md"),
    ("chandiddhipādo … vīmaṃsiddhipādo", "đã tu tập nền tảng thần thông bằng ý muốn, đã tu tập nền tảng thần thông "
     "bằng tinh tấn, đã tu tập nền tảng thần thông bằng tâm, đã tu tập nền tảng thần thông bằng sự thẩm xét",
     "21-terasamavaggo.md"),
    ("'sassato loko'ti … (Vaccha sutta)", "‘Thế gian là trường tồn’, này Vác-cha", "22-cuddasamavaggo.md"),
    ("Nanu yadaniccaṃ taṃ dukkhaṃ [saṃ. ni. 3.15] vuttaṃ bhagavatā – \"",
     f"Chẳng phải {YAD}{CIT315}, Đức Thế Tôn đã nói – “", "25-sattarasamavaggo.md"),
    ("Hañci yadaniccaṃ taṃ dukkhaṃ", f"Nếu {YAD}", "25-sattarasamavaggo.md"),
    ("Indriyabaddhaññeva dukkhanti?", "Có phải chỉ điều gắn kết với các năng lực mới là khổ đau không?",
     "25-sattarasamavaggo.md"),
    ("saññā cetanā cittaṃ saddhā vīriyaṃ sati samādhi paññā rāgo",
     "tri giác, chủ ý, tâm, niềm tin, sự tinh tấn, sự tỉnh thức, sự định tâm, trí tuệ, sự tham đắm", "17-navamavaggo.md"),
    ("phasso", "sự tiếp xúc", "23-pannarasamavaggo.md"),
]


def check_strings():
    texts = {b: unicodedata.normalize("NFC", "\n".join(p.read_text(encoding="utf-8")
                                                       for p in sorted(d.glob("*.md")))).lower()
             for b, d in S.RAILS.items()}
    bad = [(p, v, b) for p, v, b in REUSED31 if unicodedata.normalize("NFC", v).lower() not in texts[b]]
    assert not bad, "reused strings not found in their rails: " + repr(bad)
    bad = []
    for p, v, f in SHARED:
        t = unicodedata.normalize("NFC", (VDIR / f).read_text(encoding="utf-8"))
        if unicodedata.normalize("NFC", v) not in t:
            bad.append((p, v, f))
    assert not bad, "shared strings not found in their chapters: " + repr(bad)


# ---------------------------------------------------------------------------------------------------------------
# The chapter
# ---------------------------------------------------------------------------------------------------------------
def build():
    segs = []

    def add(i, *lines):
        lines = [unicodedata.normalize("NFC", x) for x in lines]
        lines[-1] = lines[-1] + f" ^{i}"
        segs.append(lines)

    def heading(i, level, text):
        add(i, "#" * level + " " + text)

    heading("5-31-0", 3, VAGGA)

    # ---- (218) 1. Ekādhippāyakathā --------------------------------------------------------------------------------
    heading("5-31-1-0", 4, f"(218) 1. {S.katha(KATHA[1])}")
    T1 = f"{EKA} thì được phép {METHUNA}"                               # ekādhippāyena methuno dhammo paṭisevitabbo
    BECOME = ", ".join(f"phải trở thành {x}" for x in ("người không phải sa-môn", "người không phải tỳ-khưu",
                                                       "người bị cắt đứt gốc", "người phạm tội bị trục xuất"))
    #   assamaṇena hotabbaṃ, abhikkhunā hotabbaṃ, chinnamūlena hotabbaṃ pārājikena hotabbaṃ
    ALL_CRIMES = ", ".join(CRIMES)
    add("5-908",
        f"{Q(T1)} {YES} {Q(f'{EKA} thì {BECOME}')} {NO_PE} {q(T1)} {YES} "
        f"{Q(EKA + ' thì được phép ' + ALL_CRIMES)} {NO_PE}",
        S.katha_end(KATHA[1]))

    # ---- (219) 2. Arahantavaṇṇakathā ------------------------------------------------------------------------------
    heading("5-31-2-0", 4, VAGGA)
    heading("5-31-2-1-0", 5, f"(219) 2. {S.katha(KATHA[2])}")
    MID = ", ".join(CRIMES[1:-1])
    add("5-909",
        f"{Q(f'{AMAN} {METHUNA}')} {YES} {Q(f'{AMAN} {CRIMES[0]}{PE} {MID}{PE} {CRIMES[-1]}')} {NO_PE}",
        S.katha_end(KATHA[2]))

    # ---- (220-4) 3-7. Issariyakāmakārikādikathā -------------------------------------------------------------------
    heading("5-31-3-0", 4, VAGGA)
    heading("5-31-3-1-0", 5, f"(220-4) 3-7. {S.katha(KATHA[3])}")
    GO = [f"đi đến {h}" for h in HELLS]
    GO[4] += VAR_HELL
    GO_LIST = ", ".join(GO[:-1]) + f"{PE} {GO[-1]}"
    add("5-910",
        f"{Q(f'{BS} {VINI}')} {YES} {Q(f'{BS} {GO_LIST}')} {NO_PE}",
        sutta_frame(f"{BS} {VINI}"))
    IDDHI = (f"Bồ-tát đã tu tập nền tảng thần thông bằng ý muốn{PE} nền tảng thần thông bằng tinh tấn{PE} "
             f"nền tảng thần thông bằng tâm{PE} đã tu tập nền tảng thần thông bằng sự thẩm xét")
    #   bodhisattena chandiddhipādo bhāvito…pe… vīriyiddhipādo…pe… cittiddhipādo…pe… vīmaṃsiddhipādo bhāvito
    add("5-911",
        f"{Q(f'{BS} {GABBHA}')} {YES} "
        f"{Q(f'{BS} có thể tái sinh vào địa ngục, tái sinh vào cõi súc sinh')} {NO_PE}",
        f"{Q(f'{BS} {GABBHA}')} {YES} {Q('Bồ-tát có thần thông')} {NO_PE} {q('Bồ-tát có thần thông')} {YES} "
        f"{Q(IDDHI)} {NO_PE}",
        sutta_frame(f"{BS} {GABBHA}"))
    V = [f"“{v}”" for v in VIEWS]
    ALL_VIEWS = f"{ACCEPT} {V[0]}, {V[1]}{PE} {(PE + ' ').join(V[2:-1])}{PE} {ACCEPT} {V[-1]}"
    #   "sassato loko"ti paccāgacchi, "asassato loko"ti…pe… "antavā…"ti…pe… … "neva hoti …"ti paccāgacchi
    #   (the Pāli's stray space in "sarīra"nti … is rendered as meant)
    add("5-912",
        f"{Q(f'{BS} {DUKKARA}')} {YES} {Q(f'{BS} {ALL_VIEWS}')} {NO_PE}",
        sutta_frame(f"{BS} {DUKKARA}"))
    add("5-913",
        f"{Q(f'{BS} {APARA}{VAR_APARA}, {SATTHA}')} {YES} "
        f"{Q(f'{BS} {ACCEPT} {V[0]}{PE} {ACCEPT} {V[-1]}')} {NO_PE}")
    add("5-914",
        sutta_frame(f"{BS} {SATTHA}"),
        S.katha_end(KATHA["3e"]))

    # ---- (225) 8. Patirūpakathā -----------------------------------------------------------------------------------
    heading("5-31-4-0", 4, VAGGA)
    heading("5-31-4-1-0", 5, f"(225) 8. {S.katha(KATHA[4])}")
    REST = f"{pati(P10[0])}{PE} {pati(P10[-1])}"
    ALL10 = ", ".join(pati(x) for x in P10)
    ALL3 = ", ".join(pati(x) for x in DMK)
    add("5-915",
        f"{Q(pati(LUST))} {YES} {Q(ALL10)} {NO_PE}")
    add("5-916",
        f"{Q(ALL3)} {YES} {Q(REST)} {NO_PE}",
        S.katha_end(KATHA[4]))

    # ---- (226) 9. Aparinipphannakathā -----------------------------------------------------------------------------
    heading("5-31-5-0", 4, VAGGA)
    heading("5-31-5-1-0", 5, f"(226) 9. {S.katha(KATHA[5])}")
    R = "vật chất"
    add("5-917",
        f"{Q(f'{R} {APN}')} {YES} {Q(f'{R} {NEG}')} {NO_PE} {nanu_l(full(R))} {YES} "
        f"{S.hanci_neg(short(R), f'{R} {APN}')}",
        yad_line(R, CIT315, pe=True))
    FIRST = (f"{S.VEDANA}{PE} {S.SANNA}{PE} {S.SANKHARA}{PE} {S.VINNANA}{PE} {S.A['cakkhāyatana']}{PE} "
             f"{S.A['dhammāyatana']}{PE} {S.D['cakkhudhātu']}{PE} {S.D['dhammadhātu']}{PE} "
             f"{S.I['cakkhundriya']}{PE} {AV}")
    #   Vedanā …pe… saññā… saṅkhārā… viññāṇaṃ… cakkhāyatanaṃ…pe… dhammāyatanaṃ… cakkhudhātu… dhammadhātu…
    #   cakkhundriyaṃ…pe… aññātāvindriyaṃ
    NEG_PE = f"không {ANICCA_L[0]}{PE} không {ANICCA_L[-1]}"            # na aniccaṃ…pe… na vipariṇāmadhammaṃ
    add("5-918",
        f"{Q(f'{FIRST} {APN}')} {YES} {Q(f'{AV} {NEG_PE}')} {NO_PE} {nanu_l(short(AV))} {YES} "
        f"{S.hanci_neg(full(AV), f'{AV} {APN}')}",
        yad_line(AV),
        S.katha_end(KATHA[5]),
        f"{VAGGA}.",
        TASSUDDANAM,
        UDDANA,
        KHUDDAKO,
        TASS50,
        UDD50,
        PANNASA_UDD,
        *VERSE,
        BHANAVARA,
        COLOPHON)
    return segs


# ---------------------------------------------------------------------------------------------------------------
# Lookup helpers
# ---------------------------------------------------------------------------------------------------------------
def termbase():
    tb = {}
    for ln in TB.read_text(encoding="utf-8").splitlines():
        if ": {" in ln:
            tb[ln.split(": {", 1)[0]] = ln
    return tb


def tb_chapter():
    tb = termbase()
    tbl = {k.lower(): v for k, v in tb.items()}
    ids = {"5-31-0"} | {f"5-{n}" for n in range(908, 919)}
    seen = set()
    for line in KW.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        i, body = line.split("] ", 1)
        i = i[1:]
        if not (i.startswith("5-31-") or i in ids):
            continue
        for k in body.split(", "):
            for kk in k.split(" / "):
                if kk.lower() in seen:
                    continue
                seen.add(kk.lower())
                e = tb.get(kk) or tbl.get(kk.lower())
                print(f"[{i}] {e if e else kk + ': <NOT IN TERMBASE>'}")


def finished():
    out = []
    for p in PDIR.glob("*.md"):
        m = re.match(r"(\d+)-", p.name)
        if m and 1 <= int(m.group(1)) <= 26:
            out.append(p.name)
    return sorted(out, key=lambda n: int(n.split("-")[0]))


def find(pat, mx=4, mc=700):
    rx, h = re.compile(pat), 0
    for n in finished():
        pl = [x for x in (PDIR / n).read_text(encoding="utf-8").splitlines() if x.strip()]
        vl = [x for x in (VDIR / n).read_text(encoding="utf-8").splitlines() if x.strip()]
        for i, ln in enumerate(pl):
            m = rx.search(ln)
            if m:
                s = max(0, m.start() - 100)
                print(f"[{n} line {i + 1}]\n  PI: {ln[s:s + 400]}\n  VI: {vl[i][:mc]}")
                h += 1
                if h >= mx:
                    return


def main():
    check_strings()
    S.check_reused()
    segs = build()
    S.check_against_pali(NAME, segs)
    text = unicodedata.normalize("NFC", "\n\n".join("\n".join(s) for s in segs) + "\n")
    assert "\n\n\n" not in text and "\r" not in text
    (VDIR / NAME).write_text(text, encoding="utf-8", newline="\n")
    print("wrote", VDIR / NAME)
    adh = S.FORMULAS_MD.parent / "adh-31"           # byte-identical copy for termbase_adherence_vi.py
    adh.mkdir(exist_ok=True)
    (adh / NAME).write_text(text, encoding="utf-8", newline="\n")
    print("wrote", adh / NAME)


if __name__ == "__main__":
    if sys.argv[1:2] == ["--find"]:
        a = sys.argv[2:]
        find(a[0], int(a[1]) if len(a) > 1 else 4, int(a[2]) if len(a) > 2 else 700)
    elif sys.argv[1:2] == ["--tb"]:
        tb_chapter()
    elif sys.argv[1:2] == ["--word"]:
        pat = re.compile(sys.argv[2], re.I)
        for h, ln in termbase().items():
            if pat.search(h):
                print(ln)
    else:
        main()
