"""pi-5 Kathāvatthu, Vietnamese RAILS (plain audience): chapter 15, Sattamavaggo (^5-15-0 … ^5-502): ten kathās
(63-72) with the repeated "Sattamavaggo" sub-headings, the vagga close and the uddāna.

Builds AI_translation/vietnamese/pi-5-vietnamese-plain-rails_split_chapters/15-sattamavaggo.md from the fixed
strings below, importing the approved sample builder READ-ONLY (frames Q, q, NANU, hanci, hanci_neg,
na_vattabbam, tena_hi, tena_hi_na, katha, katha_end, vaggo, var, var_sp …). Strings taken from pi-1 … pi-4 rails are
asserted there (REUSED15); strings shared with the finished pi-5 rails chapters are asserted in those chapter files
(SHARED). The per-line dash / quote / NFC / id checks of S.check_against_pali run before writing.
New recurring strings: notes-rails-15.md.

usage: python -I -X utf8 -B build_rails_15_vi.py          (writes the chapter and the adherence copy rails\\adh-15\\)
"""
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai\rails")
import build_rails_sample_vi as S  # noqa: E402

NAME = "15-sattamavaggo.md"
Q, q, NANU, PE, YES, NO, NO_PE = S.Q, S.q, S.NANU, S.PE, S.YES, S.NO, S.NO_PE
cap = S.cap
CIT = S.CIT
A = S.A


def nanu_l(x):                      # nanu Xti? (after …pe…, lower case)
    return f"chẳng phải {x} sao?"


def tena_hi_na_l(x):                # tena hi na vattabbaṃ – "X"ti. (after …pe…, lower case)
    return f"vậy thì không nên nói – “{x}”."


# ---------------------------------------------------------------------------------------------------------------
# Shared vocabulary (termbase; pi-1 … pi-4; finished pi-5 chapters)
# ---------------------------------------------------------------------------------------------------------------
BH, bh = "Này các tỳ-khưu", "này các tỳ-khưu"                         # bhikkhave (sample)
K_RUPA, K_VED, K_SAN, K_SANKH, K_VIN = ("khối vật chất", "khối cảm giác", "khối tri giác", "khối tạo tác",
                                        "khối thức")                  # (pi-2; sample)
SUKHA_V, DUKKHA_V, UPEKKHA_V = ("cảm giác dễ chịu", "cảm giác khó chịu",
                                "cảm giác không khó chịu cũng không dễ chịu")   # (pi-2; sample)
LIST10 = ["sự tiếp xúc", "cảm giác", "tri giác", "chủ ý", "tâm", "niềm tin", "sự tinh tấn", "sự tỉnh thức",
          "sự định tâm", "trí tuệ"]                                     # phasso … paññā (ch4 / ch12)
RDM = ["sự tham đắm", "sự sân hận", "sự si mê"]                         # rāgo doso moho (ch2)
ANOT = "sự không biết ghê sợ tội lỗi"                                   # anottappaṃ (ch2)
CET_D = "yếu tố đồng hành với tâm"                                      # cetasika (termbase)
CD = f"hiện tượng là {CET_D}"                                           # cetasiko dhammo
DANA = "sự bố thí"                                                      # dānaṃ (termbase)
GIVE_D = "thực hiện sự bố thí"                                          # dānaṃ deti (termbase dentaṃ «thực hiện»)
GIL = "thuốc men và vật dụng chữa bệnh"                                 # gilānapaccayabhesajjaparikkhāro (pi-2)
ISK = S.SAPHALA_K.split(", ", 2)[2]                                     # iṭṭhaphalaṃ … sukhavipākaṃ (sample)
ANI = S.SAPHALA_A.split(", ", 2)[2]                                     # aniṭṭhaphalaṃ … dukkhavipākaṃ (sample)
VR = "Đức Thế Tôn đã nói rằng"                                          # … vuttaṃ bhagavatā (no quote; ch4)
PG = "có thể bị nhấc lên và bị đè xuống, có thể bị cắt và bị đập vỡ"   # paggahaniggahupago chedanabhedanupago (ch5)
KV = "quả của nghiệp"                                                   # kammavipāko (termbase; sample ch1)
VIP = "quả"                                                             # vipāko (termbase Vipāko atthi; sample ch1)
CV = "người làm vua chuyển luân"                                        # cakkavattisatto (termbase; ch12)
SO, SA, AN, AR = ("thành quả vào dòng", "thành quả trở lại một lần", "thành quả không trở lại",
                  "thành quả A-la-hán")                                 # sotāpatti- … arahattaphalaṃ (ch2 / ch12)
AS = "vị đệ tử của bậc thánh"                                           # ariyasāvako (pi-2)
SURA = "việc dùng rượu nấu, rượu men và chất gây say dẫn đến sự buông thả"   # surāmeraya… (pi-2)
ESESE = S.KAYA_K.split(", thì ", 1)[1]                                  # esese ekaṭṭhe same samabhāge tajjāte (sample)
CONJ7 = ("đi kèm, cùng sinh, hòa lẫn, có cùng một sự sinh khởi, có cùng một sự chấm dứt, có cùng một chỗ dựa, "
         "có cùng một đối tượng")
#   sahagatā sahajātā saṃsaṭṭhā ekuppādā ekanirodhā ekavatthukā ekārammaṇā
CONJ8 = ("đi kèm, cùng sinh, hòa lẫn, gắn liền, có cùng một sự sinh khởi, có cùng một sự chấm dứt, "
         "có cùng một chỗ dựa, có cùng một đối tượng")
#   sahagatā sahajātā saṃsaṭṭhā sampayuttā ekuppādā ekanirodhā ekavatthukā ekārammaṇā

# ---------------------------------------------------------------------------------------------------------------
# Theses, kathā names, vagga close
# ---------------------------------------------------------------------------------------------------------------
VAGGA = S.vaggo(7)                                                     # Sattamavaggo «Chương thứ bảy» (termbase)
NATTHI_S = "không có hiện tượng nào được gộp vào bất kỳ hiện tượng nào"  # natthi keci dhammā kehici dhammehi saṅgahitā
ATTHI_S = "có những hiện tượng được gộp vào những hiện tượng nào đó"     # atthi keci dhammā kehici dhammehi saṅgahitā
NATTHI_P = "không có hiện tượng nào gắn liền với bất kỳ hiện tượng nào"  # … sampayuttā
NATTHI_C = f"không có hiện tượng nào là {CET_D}"                        # natthi cetasiko dhammo
ATTHI_C = f"có {CD}"                                                    # atthi cetasiko dhammo
T4 = f"{CD} là {DANA}"                                                  # cetasiko dhammo dānaṃ
DEY = "vật để bố thí"                                                   # deyyadhammo (termbase)
T4B = f"{DEY} là {DANA}"                                                # deyyadhammo dānaṃ
PM = "phước phát sinh từ sự thọ hưởng"                                  # paribhogamayaṃ puññaṃ (termbase)
T5 = f"{PM} tăng trưởng"                                                # paribhogamayaṃ puññaṃ vaḍḍhati
ITO = "nhờ những gì được cho từ đây mà ở đó họ duy trì sự sống"         # ito dinnena tattha yāpenti
PK = f"đất là {KV}"                                                     # pathavī kammavipāko (termbase)
JM = "sự lão hóa và sự chết"                                            # jarāmaraṇaṃ (termbase)
T8 = f"{JM} là {VIP}"                                                   # jarāmaraṇaṃ vipāko
NAV = "không có quả của các hiện tượng cao quý"                         # natthi ariyadhammavipāko
VD = "hiện tượng có khả năng sinh ra quả"                               # vipākadhammadhammo (termbase)
T10 = f"{VIP} là {VD}"                                                  # vipāko vipākadhammadhammo
KATHA = {1: "những gì được gộp vào", 2: "những gì gắn liền", 3: CET_D, 4: DANA, 5: PM,
         6: "những gì được cho từ đây", 7: f"việc {PK}", 8: f"việc {T8}", 9: "quả của các hiện tượng cao quý",
         10: f"việc {T10}"}
#   Saṅgahita-, Sampayutta-, Cetasika-, Paribhogamayapuñña- (termbase headings), Dāna-, Itodinna-,
#   Pathavī kammavipākoti-, Jarāmaraṇaṃ vipākoti-, Ariyadhammavipāka-, Vipāko vipākadhammadhammotikathā
TASSUDDANAM = "Tóm tắt của chương này –"                               # Tassuddānaṃ – (ch9)
UDDANA = (f"Sự gộp vào, những gì gắn liền, {CD}, {DANA} là {CET_D}, {T5}, {ITO}, {PK}, {T8}, {NAV}, {T10}.")
#   Saṅgaho, sampayutto, cetasiko dhammo, cetasikaṃ dānaṃ, paribhogamayaṃ puññaṃ vaḍḍhati, ito dinnena tattha
#   yāpenti, pathavī kammavipāko, jarāmaraṇaṃ vipāko, natthi ariyadhammavipāko, vipāko vipākadhammadhammoti.

REUSED15 = [  # (Pāli, Vietnamese, book)
    ("Cakkhusamphassajā saññā", "tri giác sinh từ sự tiếp xúc của mắt", "2"),
    ("sotasamphassajā saññā", "tri giác sinh từ sự tiếp xúc của tai", "2"),
    ("rūpakkhandha … (aggregate names)", "khối vật chất, khối cảm giác, khối tri giác, khối tạo tác, khối thức", "2"),
    ("kusalākusale dhamme", "các hiện tượng thiện và bất thiện", "4"),
    ("sāvajjānavajje dhamme", "các hiện tượng có lỗi và không có lỗi", "4"),
    ("hīnappaṇīte dhamme", "các hiện tượng thấp kém và ưu việt", "4"),
    ("kaṇhasukkasappaṭibhāge dhamme", "các hiện tượng đen tối và trong sáng cùng với các mặt đối lập của chúng", "4"),
    ("āvaṭṭanā ābhogo samannāhāro manasikāro", "sự hướng đến, sự chú hướng, sự lưu ý", "2"),
    ("kāmavitakko, byāpādavitakko, vihiṃsāvitakko",
     "Sự hướng tâm đến dục lạc, sự hướng tâm đến ác ý, sự hướng tâm đến sự hãm hại", "2"),
    ("sukhāya vedanāya sampayuttā", "gắn liền với cảm giác dễ chịu", "1"),
    ("adukkhamasukhāya vedanāya sampayuttā", "gắn liền với cảm giác không khó chịu cũng không dễ chịu", "1"),
    ("sārammaṇā", "có đối tượng", "1"),
    ("ācayagāmino", "dẫn đến sự tích lũy", "1"),
    ("apacayagāmino", "dẫn đến sự giảm trừ", "1"),
    ("appamāṇā", "không thể đo lường", "1"),
    ("Idhekacco", "Ở đời này, có người", "1"),
    ("Idha ariyasāvako … pahāya", f"Ở đây, {AS}, sau khi dứt bỏ", "2"),
    ("pāṇātipātā paṭivirato hoti", "kiêng tránh việc sát hại sinh mạng", "4"),
    ("adinnādānā", "việc lấy của không được cho", "2"),
    ("kāmesumicchācārā", "hành vi sai trái trong các dục lạc", "2"),
    ("musāvādā", "việc nói dối", "2"),
    ("surāmerayamajjapamādaṭṭhānā", SURA, "2"),
    ("sappuriso", "người chân chính", "4"),
    ("anattā", "không phải là tự ngã", "2"),
    ("cīvarapiṇḍapātasenāsanagilānapaccayabhesajjaparikkhāra",
     "y phục, đồ ăn khất thực, chỗ ở, thuốc men và vật dụng chữa bệnh", "2"),
    ("dī. ni. (citation)", "Trường Bộ Kinh", "2"),
]

SHARED = [  # (Pāli, Vietnamese, finished pi-5 rails chapter)
    ("kammavipāko", KV, "1-puggalakatha.md"),
    ("Vipāko atthi", "quả tồn tại", "1-puggalakatha.md"),
    ("Añño karoti añño paṭisaṃvedeti", "một người làm, một người khác cảm nhận", "1-puggalakatha.md"),
    ("Tassa tasseva natthi dukkhassa antakiriyā …", S.TASSA_TASSEVA, "1-puggalakatha.md"),
    ("esese ekaṭṭhe same samabhāge tajjāte", ESESE, "1-puggalakatha.md"),
    ("[… (?)]", "[dị bản (?): ", "1-puggalakatha.md"),
    ("rāgo / doso / moho / anottappaṃ", "sự si mê đã được dứt bỏ", "2-parihanikatha.md"),
    ("anottappaṃ", ANOT, "2-parihanikatha.md"),
    ("sotāpattiphala / sakadāgāmiphala …", SA, "2-parihanikatha.md"),
    ("khu. pā. (citation)", "Tiểu Tụng", "3-brahmacariyakatha.md"),
    ("tiṇṇaṃ phassānaṃ … paññānaṃ samodhānaṃ hoti", "có sự tụ hợp của ba sự tiếp xúc, ba cảm giác, ba tri giác, "
     "ba chủ ý, ba tâm, ba niềm tin, ba sự tinh tấn, ba sự tỉnh thức, ba sự định tâm, ba trí tuệ", "4-jahatikatha.md"),
    ("… vuttaṃ bhagavatā (no quote)", VR, "4-jahatikatha.md"),
    ("paggahaniggahupago chedanabhedanupago", PG, "5-sabbamatthitikatha.md"),
    ("sammukhībhāvo", "sự cùng hiện diện đối mặt nhau", "5-sabbamatthitikatha.md"),
    ("aṭṭhakathā oloketabbā", "cần tham khảo Chú giải", "5-sabbamatthitikatha.md"),
    ("dī. ni. (citation)", "Trường Bộ Kinh", "8-satipatthanakatha.md"),
    ("Tassuddānaṃ –", TASSUDDANAM, "9-hevatthikatha.md"),
    ("Lokuttaraṃ", "vượt thế gian", "10-dutiyavaggo.md"),
    ("Dvinnaṃ phassānaṃ dvinnaṃ cittānaṃ samodhānaṃ hoti", "có sự tụ hợp của hai sự tiếp xúc, hai tâm",
     "11-tatiyavaggo.md"),
    ("Kāmāvacaraṃ / rūpāvacaraṃ", "thuộc cõi dục lạc rồi trở thành thuộc cõi hình sắc", "11-tatiyavaggo.md"),
    ("rāgasahagataṃ rāgasahajātaṃ rāgasaṃsaṭṭhaṃ rāgasampayuttaṃ",
     "đi kèm, cùng sinh với tham đắm, hòa lẫn với tham đắm, gắn liền với tham đắm", "11-tatiyavaggo.md"),
    ("pāṇātipāto", "việc sát hại sinh mạng", "11-tatiyavaggo.md"),
    ("Pañcimāni, bhikkhave, X! Katamāni pañca?", "Năm năng lực nào?", "11-tatiyavaggo.md"),
    ("piṇḍapātaṃ deti, senāsanaṃ deti, gilānapaccayabhesajjaparikkhāraṃ deti",
     f"đồ ăn khất thực, cho chỗ ở, cho {GIL}", "12-catutthavaggo.md"),
    ("cakkavattisatto", CV, "12-catutthavaggo.md"),
    ("apacayagāmī", "dẫn đến sự giảm trừ", "12-catutthavaggo.md"),
    ("arahattaphalaṃ", AR, "12-catutthavaggo.md"),
    ("Yathā A, evamevaṃ Bti?", "Có phải cũng như", "12-catutthavaggo.md"),
    ("evamevaṃ", "cũng y như vậy", "12-catutthavaggo.md"),
]


def check_strings():
    texts = {b: unicodedata.normalize("NFC", "\n".join(p.read_text(encoding="utf-8")
                                                       for p in sorted(d.glob("*.md")))).lower()
             for b, d in S.RAILS.items()}
    bad = [(p, v, b) for p, v, b in REUSED15 if unicodedata.normalize("NFC", v).lower() not in texts[b]]
    assert not bad, "reused strings not found in their rails: " + repr(bad)
    bad = []
    for p, v, f in SHARED:
        t = unicodedata.normalize("NFC", (S.OUT_DIR / f).read_text(encoding="utf-8"))
        if unicodedata.normalize("NFC", v) not in t:
            bad.append((p, v, f))
    assert not bad, "shared strings not found in their chapters: " + repr(bad)


# ---------------------------------------------------------------------------------------------------------------
# Small frames
# ---------------------------------------------------------------------------------------------------------------
def gan(x, k, var="", capfirst=True):  # X katamakkhandhagaṇanaṃ gacchatīti? K-gaṇanaṃ gacchatīti. Hañci …
    head = cap(x) if capfirst else x
    return (f"{head} được tính vào khối nào{var}? Được tính vào {k}. "
            f"{S.hanci(f'{x} được tính vào {k}', f'{x} được gộp vào {k}')}")


def sj(a, b):                       # A B-ena sahajāto
    return f"{a} cùng sinh với {b}"


def sp(a, b):                       # A B-ena sampayutto
    return f"{a} gắn liền với {b}"


def kv(x, y, var=""):               # X-ena sahajātāti katvā Y-sikāti?
    return f"Có phải vì cho rằng cùng sinh với {x}, nên là yếu tố đồng hành với {y}{var} không?"


def lab(x):                         # labbhā X paresaṃ dātuṃ
    return f"có thể cho người khác {x}"


def vr(x):                          # dānaṃ iṭṭhaphalaṃ vuttaṃ bhagavatā, X
    return f"{VR} {DANA} có kết quả đáng mong muốn, {x}"


# Feelings / conjunction / attention lists of kathās 7-8
VED3 = ["được cảm nhận là dễ chịu", "được cảm nhận là khó chịu",
        "được cảm nhận là không khó chịu cũng không dễ chịu"]          # sukha- / dukkha- / adukkhamasukhavedaniya
SAMP8 = [f"gắn liền với {SUKHA_V}", f"gắn liền với {DUKKHA_V}", f"gắn liền với {UPEKKHA_V}",
         "gắn liền với sự tiếp xúc", "gắn liền với cảm giác", "gắn liền với tri giác", "gắn liền với chủ ý",
         "gắn liền với tâm"]                                            # sukhāya vedanāya sampayutta … cittena sampayutta
AV7 = ["sự hướng đến", "sự chú hướng", "sự lưu ý", "sự chú tâm", "chủ ý", "sự mong ước", "sự mong cầu"]
#   āvaṭṭanā ābhogo samannāhāro manasikāro cetanā patthanā paṇidhi
POS_FULL = ", ".join(VED3 + SAMP8 + ["có đối tượng"])
NEG_FULL = ", ".join(["không " + x for x in VED3 + SAMP8] + ["không có đối tượng"])
POS_PE = (", ".join(VED3) + f", {SAMP8[0]}, với {DUKKHA_V}{PE} " + ", ".join(SAMP8[2:]) + ", có đối tượng")
#   sukhavedaniyo … sukhāya vedanāya sampayutto dukkhāya…pe… adukkhamasukhāya … sārammaṇo
POS_SH = f"{VED3[0]}, {VED3[1]}{PE} có đối tượng"                       # sukhavedaniyo dukkhavedaniyo…pe… sārammaṇo
NEG_SH = f"không {VED3[0]}, không {VED3[1]}{PE} không có đối tượng"     # na sukhavedaniyo na dukkhavedaniyo…pe… anārammaṇo
AVF = ", ".join(AV7)
AVS = f"{AV7[0]}{PE} {AV7[-1]}"                                         # āvaṭṭanā…pe… paṇidhi


# ---------------------------------------------------------------------------------------------------------------
# The chapter
# ---------------------------------------------------------------------------------------------------------------
def build():
    segs = []

    def add(i, *lines):
        lines = list(lines)
        lines[-1] = lines[-1] + f" ^{i}"
        segs.append(lines)

    def heading(i, level, text):
        add(i, "#" * level + " " + text)

    heading("5-15-0", 3, VAGGA)

    # ---- (63) 1. Saṅgahitakathā ---------------------------------------------------------------------------------
    heading("5-15-1-0", 4, f"(63) 1. {S.katha(KATHA[1])}")
    GANANA = "có những hiện tượng được tính vào, được kể vào, nằm trong những hiện tượng nào đó"
    #   atthi keci dhammā kehici dhammehi gaṇanaṃ gacchanti uddesaṃ gacchanti pariyāpannā
    SANNA = [f"tri giác sinh từ sự tiếp xúc của {x}" for x in ("mắt", "tai", "ý")]
    CETANA = [f"chủ ý sinh từ sự tiếp xúc của {x}" for x in ("mắt", "ý")]
    add("5-471",
        f"Có phải {NATTHI_S}{S.var_sp('Pī.', 'saṅgahītāti')} không? {YES} {NANU(GANANA)} {YES} "
        f"{S.hanci_neg(GANANA, NATTHI_S)}",
        gan(A["cakkhāyatana"], K_RUPA, S.var_sp("Sī., Pī., Ka.", "katamaṃ khandhagaṇanaṃ")) + " "
        + f"{cap(A['sotāyatana'])}{PE} {A['ghānāyatana']}{PE} {A['jivhāyatana']}{PE} "
        + gan(A["kāyāyatana"], K_RUPA, capfirst=False),
        f"{cap(A['rūpāyatana'])}{PE} {A['saddāyatana']}{PE} {A['gandhāyatana']}{PE} {A['rasāyatana']}{PE} "
        + gan(A["phoṭṭhabbāyatana"], K_RUPA, capfirst=False),
        gan(SUKHA_V, K_VED) + f" {cap(DUKKHA_V)}{PE} " + gan(UPEKKHA_V, K_VED, capfirst=False),
        gan(SANNA[0], K_SAN) + f" {cap(SANNA[1])}{PE} " + gan(SANNA[2], K_SAN, capfirst=False),
        f"{cap(CETANA[0])}{PE} " + gan(CETANA[1], K_SANKH, capfirst=False),
        f"Thức qua mắt{PE} " + gan("ý thức", K_VIN, capfirst=False))
    YS = ("hai con bò đực được gộp vào bằng dây thừng hay bằng dây ách, đồ ăn khất thực được gộp vào bằng túi treo, "
          "con chó được gộp vào bằng dây xích")
    #   dāmena vā yottena vā dve balibaddā saṅgahitā, sikkāya piṇḍapāto saṅgahito, sā gaddulena saṅgahito
    NOTE_SV = " [lời của người theo học thuyết của chúng ta (cần xem Chú giải)]"   # [sakavādivacanaṃ (aṭṭhakathā passitabbā)]
    add("5-472",
        f"Có phải cũng như {YS}; cũng y như vậy, những hiện tượng ấy được gộp vào những hiện tượng ấy{NOTE_SV} "
        f"không? {S.hanci(YS, ATTHI_S)[:-1]}{NOTE_SV}.",
        S.katha_end(KATHA[1]))

    # ---- (64) 2. Sampayuttakathā --------------------------------------------------------------------------------
    heading("5-15-2-0", 4, VAGGA)
    heading("5-15-2-1-0", 5, f"(64) 2. {S.katha(KATHA[2])}")
    SAHA2 = f"có những hiện tượng {CONJ7} với những hiện tượng nào đó"
    add("5-473",
        f"{Q(NATTHI_P)} {YES} {NANU(SAHA2)} {YES} {S.hanci_neg(SAHA2, NATTHI_P)}",
        f"{Q(sj(K_VED, K_SAN))} {YES} {S.hanci(sj(K_VED, K_SAN), sp(K_VED, K_SAN))}",
        f"Có phải {K_VED} cùng sinh với {K_SANKH}{PE} với {K_VIN} không? {YES} "
        f"{S.hanci(sj(K_VED, K_VIN), sp(K_VED, K_VIN))}",
        f"Có phải {K_SAN}{PE} {K_SANKH}{PE} {K_VIN} cùng sinh với {K_VED}{PE} với {K_SAN}{PE} với {K_SANKH} không? "
        f"{YES} {S.hanci(sj(K_VIN, K_SANKH), sp(K_VIN, K_SANKH))}")
    add("5-474",
        "Có phải cũng như dầu thấm vào, thâm nhập vào hạt mè, nước ép thấm vào, thâm nhập vào cây mía; cũng y như "
        f"vậy, những hiện tượng ấy thấm vào, thâm nhập vào những hiện tượng ấy không? {NO_PE}",
        S.katha_end(KATHA[2]))

    # ---- (65) 3. Cetasikakathā ----------------------------------------------------------------------------------
    heading("5-15-3-0", 4, VAGGA)
    heading("5-15-3-1-0", 5, f"(65) 3. {S.katha(KATHA[3])}")
    SAHA3 = f"có những hiện tượng {CONJ8} với tâm"
    F11 = LIST10[1:4] + LIST10[5:] + RDM                                 # vedanā … paññā, rāgo, doso, moho
    PH = LIST10[0]
    add("5-475",
        f"{Q(NATTHI_C)} {YES} {NANU(SAHA3)} {YES} {S.hanci_neg(SAHA3, NATTHI_C)}",
        f"{Q(sj(PH, 'tâm'))} {YES} {S.hanci(sj(PH, 'tâm'), f'{PH} là {CET_D}')} "
        f"Có phải {f'{PE} '.join(F11)}{PE} {ANOT} cùng sinh với tâm không? {YES} "
        f"{S.hanci(sj(ANOT, 'tâm'), f'{ANOT} là {CET_D}')}")
    add("5-476",
        f"{kv('tâm', 'tâm')} {YES} {kv(PH, PH, S.var('Pī., Chú giải', 'phassikāti'))} {YES} {kv('tâm', 'tâm')} {YES} "
        f"Có phải vì cho rằng cùng sinh với {f'{PE} với '.join(F11)}{PE} với {ANOT}, nên là yếu tố đồng hành với "
        f"{ANOT}{S.var('?', 'anottappikāti')} không? {YES}")
    add("5-477",
        f"{Q(NATTHI_C)} {YES} {S.NANU_VUTTAM}",
        f"“Vì tâm này và các hiện tượng là {CET_D},",
        "Đối với người đã hiểu rõ, chúng không phải là tự ngã;",
        "Sau khi biết điều thấp kém và ưu việt nơi cả hai ấy,",
        "Người thấy đúng đắn đã biết chúng có bản chất tan rã”.",
        f"{S.ATTHEVA} {YES} {S.tena_hi(ATTHI_C)}",
        f"{Q(NATTHI_C)} {YES} {S.NANU_VUTTAM} “Ở đây, này Kê-vát-ta, vị tỳ-khưu chỉ ra cả tâm của các chúng sinh "
        f"khác, của những người khác, chỉ ra cả {CET_D}, chỉ ra cả điều được hướng tâm đến, chỉ ra cả điều được duy "
        f"trì tâm vào – ‘ý của bạn như thế này, ý của bạn như thế kia, tâm của bạn như vậy’” "
        f"[Trường Bộ Kinh 1.485]. {S.ATTHEVA} {YES} {S.tena_hi(ATTHI_C)}",
        S.katha_end(KATHA[3]))

    # ---- (66) 4. Dānakathā --------------------------------------------------------------------------------------
    heading("5-15-4-0", 4, VAGGA)
    heading("5-15-4-1-0", 5, f"(66) 4. {S.katha(KATHA[4])}")
    F8 = LIST10[1:4] + LIST10[5:]                                        # vedanā … paññā (no cittaṃ)
    add("5-478",
        f"{Q(T4)} {YES} {Q(lab(CD))} {NO_PE} {q(lab(CD))} {YES} {Q(lab(PH))} {NO_PE} "
        f"{q(lab(f'{PE} '.join(F8)))} {NO_PE}")
    NOTE_UP = (" [giống với câu hỏi của người theo học thuyết khác sẽ được nói ở phần sau, "
               "cần tham khảo Chú giải]")
    #   [upari vuccamānāya paravādīpucchāya sadisā, aṭṭhakathā oloketabbā]
    REQ3 = f"đồ ăn khất thực, chỗ ở, {GIL}"
    add("5-479",
        f"{S.na_vattabbam(T4)} {YES} {Q(f'{DANA} {ANI}')} {NO_PE} {nanu_l(f'{DANA} {ISK}')} {YES} "
        f"{S.hanci(f'{DANA} {ISK}', T4)}",
        f"Có phải {vr(f'y phục là {DANA}')}{NOTE_UP} không? {YES} {Q(f'y phục {ISK}')} {NO_PE} "
        f"{q(vr(f'{REQ3} là {DANA}'))} {YES} {Q(f'{GIL} {ISK}')} {NO_PE}")
    QUAL = ("được biết là bậc nhất, được biết là lâu đời, được biết là thuộc dòng truyền thống, cổ xưa, không lẫn lộn, "
            "trước đây chưa từng lẫn lộn, hiện không bị lẫn lộn, sẽ không bị lẫn lộn, không bị các sa-môn, bà-la-môn "
            "có trí phản đối")
    #   aggaññāni rattaññāni vaṃsaññāni porāṇāni asaṅkiṇṇāni asaṅkiṇṇapubbāni, na saṅkiyanti na saṅkiyissanti,
    #   appaṭikuṭṭhāni samaṇehi brāhmaṇehi viññūhi
    GIVE = "cho vô lượng chúng sinh sự không sợ hãi, cho sự không thù địch, cho sự không gây hại"
    DATVA = ("Sau khi cho vô lượng chúng sinh sự không sợ hãi, sau khi cho sự không thù địch, sau khi cho sự không "
             "gây hại, vị ấy trở thành người có phần trong sự không sợ hãi vô lượng, sự không thù địch vô lượng, "
             "sự không gây hại vô lượng.")
    #   Aparimāṇānaṃ sattānaṃ abhayaṃ datvā … abyābajjhassa bhāgī hoti.
    SUT8 = (f"“{BH}, có năm {DANA} này, là những {DANA} lớn, {QUAL}! Năm {DANA} nào? "
            f"Ở đây, {bh}, {AS}, sau khi dứt bỏ việc sát hại sinh mạng, kiêng tránh việc sát hại sinh mạng. "
            f"{BH}, khi kiêng tránh việc sát hại sinh mạng, {AS} {GIVE}{S.var_sp('Syā., Ka.', 'abyāpajjhaṃ')}. "
            f"{DATVA} {BH}, đây là {DANA} thứ nhất, là {DANA} lớn, {QUAL}. "
            f"Lại nữa, {bh}, {AS}, sau khi dứt bỏ việc lấy của không được cho{PE} sau khi dứt bỏ hành vi sai trái "
            f"trong các dục lạc{PE} sau khi dứt bỏ việc nói dối{PE} sau khi dứt bỏ {SURA}, kiêng tránh {SURA}. "
            f"{BH}, khi kiêng tránh {SURA}, {AS} {GIVE}. {DATVA} {BH}, đây là {DANA} thứ năm, là {DANA} lớn, {QUAL}. "
            f"{BH}, đây chính là năm {DANA}, là những {DANA} lớn, {QUAL}” [{CIT['a. ni.']} 8.39].")
    add("5-480",
        f"{S.na_vattabbam(T4)} {YES} {S.NANU_VUTTAM}",
        f"“Niềm tin, sự biết hổ thẹn và {DANA} thiện,",
        "Những hiện tượng này được người chân chính noi theo;",
        "Vì người ta nói đây là con đường thuộc cõi trời,",
        f"Vì nhờ con đường này mà đi đến thế giới chư thiên” [{CIT['a. ni.']} 8.32].",
        f"{S.ATTHEVA} {YES} {S.tena_hi(T4)}",
        f"{S.na_vattabbam(T4)} {YES} {S.NANU_VUTTAM} {SUT8} {S.ATTHEVA} {YES} {S.tena_hi(T4)}")
    add("5-481",
        f"{S.na_vattabbam(T4B)} {YES} {S.NANU_VUTTAM} “Ở đời này, có người cho thức ăn, cho thức uống, cho vải, "
        f"cho xe cộ, cho vòng hoa, cho hương thơm, cho dầu thoa, cho giường nằm, cho chỗ ở, cho đèn đuốc” "
        f"[{CIT['saṃ. ni.']} 3.362-391, hơi khác một chút]! {S.ATTHEVA} {YES} {S.tena_hi(T4B)}")
    add("5-482",
        f"{Q(T4B)} {YES} {Q(f'{DEY} {ISK}')} {NO_PE} {q(vr(f'y phục là {DANA}'))} {YES} {Q(f'y phục {ISK}')} "
        f"{NO_PE} {q(vr(f'đồ ăn khất thực là {DANA}{PE} chỗ ở là {DANA}{PE} {GIL} là {DANA}'))} {YES} "
        f"{Q(f'{GIL} {ISK}')} {NO_PE} {tena_hi_na_l(T4B)}",
        S.katha_end(KATHA[4]))

    # ---- (67) 5. Paribhogamayapuññakathā ------------------------------------------------------------------------
    heading("5-15-5-0", 4, VAGGA)
    heading("5-15-5-1-0", 5, f"(67) 5. {S.katha(KATHA[5])}")
    GROW = [f"{x} tăng trưởng" for x in LIST10]
    GROW[0] = "sự tiếp xúc phát sinh từ sự thọ hưởng tăng trưởng"     # paribhogamayo phasso vaḍḍhati
    PLANTS = ", ".join(f"tăng trưởng như {x}" for x in ("dây leo", "dây quấn", "cây", "cỏ", "đống cỏ lau"))
    #   latā / māluvā / rukkho / tiṇaṃ / muñjapuñjo viya vaḍḍhati
    add("5-483",
        f"{Q(T5)} {YES} {Q(', '.join(GROW))} {NO_PE}",
        f"{Q(T5)} {YES} {Q(PLANTS)} {NO_PE}")
    POSP = ["người hướng đến", "người chú hướng", "người lưu ý", "người chú tâm", "người khởi chủ ý",
            "người mong ước", "người mong cầu"]                         # āvaṭṭentassa … paṇidahantassa (termbase)
    NEGP = [x.replace("người ", "người không ", 1) for x in POSP]
    VAR_AV = S.var_sp("Sī., Pī., Ka.", "anāvaṭṭantassa")[:-1] + "; dị bản (Syā.): anāvajjhantassa]"

    def chain(lst, first_var=""):   # X-assa hoti… Y-assa hoti… …
        items = [f"có nơi {x}" for x in lst]
        items[0] = f"phước {items[0]}{first_var}"
        return f"{PE} ".join(items)

    NEG_CH, POS_CH = chain(NEGP, VAR_AV), chain(POSP)
    GAVE = f"người bố thí, sau khi {GIVE_D},"
    add("5-484",
        f"{Q(T5)} {YES} Có phải {GAVE} không lưu ý, mà có phước không? {YES} {Q(NEG_CH)} {NO_PE} "
        f"{nanu_l(POS_CH)} {YES} {S.hanci_neg(POS_CH, T5)}")
    VIT = (f"{GAVE} khởi lên sự hướng tâm đến dục lạc, khởi lên sự hướng tâm đến ác ý, khởi lên sự hướng tâm đến sự "
           f"hãm hại,")                                                   # kāmavitakkaṃ vitakketi … (pi-2 names)
    TWO = f"có sự tụ hợp của hai sự tiếp xúc{PE} hai tâm"
    KUS = ("các hiện tượng thiện và bất thiện, có lỗi và không có lỗi, thấp kém và ưu việt, đen tối và trong sáng cùng "
           "với các mặt đối lập của chúng đi đến chỗ cùng hiện diện đối mặt nhau")
    #   kusalākusalā sāvajjānavajjā hīnapaṇītā kaṇhasukkasappaṭibhāgā dhammā sammukhībhāvaṃ āgacchanti (pi-4, termbase)
    FAR = "điều rất xa cách nhau"                                        # suvidūravidūraṃ
    SUT4 = (f"“{BH}, có bốn {FAR} này! Bốn điều nào? {BH}, bầu trời và mặt đất – đây là {FAR} thứ nhất. "
            f"{BH}, bờ bên này của biển và bờ bên kia – đây là {FAR} thứ hai. "
            f"{BH}, nơi mặt trời mọc lên và nơi nó lặn xuống – đây là {FAR} thứ ba. "
            f"{BH}, bản chất của người hiền thiện và bản chất của kẻ không hiền thiện – đây là {FAR} thứ tư. "
            f"{BH}, đây chính là bốn {FAR}.")
    add("5-485",
        f"{Q(T5)} {YES} Có phải {VIT} mà có phước không? {YES} {Q(TWO)} {NO_PE} {q(TWO)} {YES} {Q(KUS)} {NO_PE} "
        f"{q(KUS)} {YES} {S.NANU_VUTTAM} {SUT4}",
        "“Bầu trời ở xa, mặt đất ở xa,",
        "Bờ bên kia của biển, người ta nói là xa;",
        "Và nơi mặt trời mọc lên,",
        "Và nơi đấng tạo ra vầng sáng lặn xuống.",
        "“Người ta nói quả thật còn xa hơn thế,",
        "Là bản chất của người hiền thiện và bản chất của kẻ không hiền thiện;",
        "Sự gặp gỡ người hiền thiện không bị hao mòn,",
        "Dù kéo dài bao lâu, vẫn y như thế.",
        f"“Vì sự gặp gỡ kẻ không hiền thiện nhanh chóng tan biến{S.var(CIT['bahūsu'], 'khippaṃhaveti')};",
        f"Vì vậy, bản chất của người hiền thiện ở xa kẻ không hiền thiện” [{CIT['a. ni.']} 4.47].",
        f"{S.ATTHEVA} {YES} {S.tena_hi_na(KUS)}")
    TAIL = ("dòng chảy của điều thiện, dưỡng chất của hạnh phúc, thuộc về cõi trời, có quả trổ dễ chịu, "
            "dẫn đến cõi trời")
    #   kusalābhisandā sukhassāhārā sovaggikā sukhavipākā saggasaṃvattanikā
    SAMV = "đưa đến điều đáng mong muốn, đáng yêu mến, đáng ưa thích, đến lợi ích, đến hạnh phúc"
    #   iṭṭhāya kantāya manāpāya hitāya sukhāya saṃvattati
    CS = "định tâm không thể đo lường của tâm"                            # appamāṇaṃ cetosamādhiṃ
    UP = f"chứng nhập và an trú {CS}, thì dòng chảy của phước nơi người ấy là không thể đo lường, {TAIL}, {SAMV}."
    SUTP = (f"“{BH}, bốn dòng chảy của phước này, {TAIL}, {SAMV}! Bốn dòng chảy nào? "
            f"{BH}, khi vị tỳ-khưu thọ hưởng y phục của người nào mà {UP} "
            f"{BH}, khi vị tỳ-khưu thọ hưởng đồ ăn khất thực của người nào{PE} thọ hưởng chỗ ở{PE} thọ hưởng {GIL} "
            f"mà {UP} {BH}, đây chính là bốn dòng chảy của phước, {TAIL}, {SAMV}” [{CIT['a. ni.']} 4.51].")
    add("5-486",
        f"{S.na_vattabbam(T5)} {YES} {S.NANU_VUTTAM}",
        "“Những người trồng vườn cây, trồng rừng, những người làm cầu;",
        "Những ai cho trạm nước uống, giếng nước và chỗ trú ngụ.",
        "“Đối với họ, cả ngày lẫn đêm, phước luôn luôn tăng trưởng;",
        f"Đứng vững trong Giáo Pháp, thành tựu giới hạnh, những người ấy đi đến cõi trời” [{CIT['saṃ. ni.']} 1.47].",
        f"{S.ATTHEVA} {YES} {S.tena_hi(T5)}",
        f"{S.na_vattabbam(T5)} {YES} {S.NANU_VUTTAM} {SUTP} {S.ATTHEVA} {YES} {S.tena_hi(T5)}")
    RC = (f"người bố thí {GIVE_D}, người nhận, sau khi nhận, không thọ hưởng, vứt bỏ, cho đi, mà có phước")
    #   dāyako dānaṃ deti, paṭiggāhako paṭiggahetvā na paribhuñjati chaḍḍeti vissajjeti, hoti puññaṃ
    LOSS = (f"người bố thí {GIVE_D}, khi người nhận đã nhận, hoặc vua chúa lấy đi, hoặc kẻ trộm lấy đi, hoặc lửa "
            f"thiêu đốt, hoặc nước cuốn trôi, hoặc những người thừa kế không ưa thích lấy đi, mà có phước")
    add("5-487",
        f"{Q(T5)} {YES} {Q(RC)} {YES} {S.hanci_neg(RC, T5, sep=';')}",
        f"{Q(T5)} {YES} {Q(LOSS)} {YES} {S.hanci_neg(LOSS, T5, sep=';')}",
        S.katha_end(KATHA[5]))

    # ---- (68) 6. Itodinnakathā ----------------------------------------------------------------------------------
    heading("5-15-6-0", 4, VAGGA)
    heading("5-15-6-1-0", 5, f"(68) 6. {S.katha(KATHA[6])}")
    FROM = ", ".join(f"từ đây người ta cho {x}" for x in ("đồ ăn khất thực", "chỗ ở", GIL, "món ăn cứng",
                                                         "món ăn mềm", "nước uống"))
    add("5-488",
        f"{Q(ITO)} {YES} Có phải từ đây người ta cho y phục, ở đó họ thọ hưởng y phục ấy không? {NO_PE} "
        f"{q(f'{FROM}; ở đó họ thọ hưởng nước uống ấy')} {NO_PE}",
        f"{Q(ITO)} {YES} Có phải một người là người tạo cho người khác, sự dễ chịu và sự khó chịu do người khác làm "
        f"ra, một người làm, một người khác cảm nhận không? {NO_PE}")
    PETA = (f"các ngạ quỷ tùy hỷ với người đang {GIVE_D} vì lợi ích của chính họ, làm cho tâm trong sáng, "
            f"làm sinh khởi sự hân hoan, có được niềm vui")
    add("5-489", f"{S.na_vattabbam(ITO)} {YES} {NANU(PETA)} {YES} {S.hanci(PETA, ITO, sep=';')}")
    GIVEN = "Cũng y như vậy, những gì được cho từ đây đem lại lợi ích cho các ngạ quỷ."
    add("5-490",
        f"{S.na_vattabbam(ITO)} {YES} {S.NANU_VUTTAM}",
        "“Nước mưa rơi xuống chỗ cao, chảy xuôi theo chỗ trũng;",
        GIVEN,
        "“Như những dòng sông đầy, làm đầy biển cả;",
        GIVEN,
        "“Vì ở đó không có việc cày cấy, nơi ấy không có việc chăn bò;",
        f"Không có việc buôn bán như thế, việc mua bán bằng vàng{S.var_sp('Sī., Pī.', 'kayakkayaṃ')};",
        "Nhờ những gì được cho từ đây, các ngạ quỷ, những người đã qua đời, duy trì sự sống ở nơi ấy” "
        "[Tiểu Tụng 7.6; Ngạ Quỷ Sự 19].",
        f"{S.ATTHEVA} {YES} {S.tena_hi(ITO)}")
    BHATO = "hoặc, được nuôi dưỡng, nó sẽ nuôi dưỡng chúng ta, hoặc nó sẽ làm công việc cho chúng ta"
    #   Bhaṭo vā no bharissati, kiccaṃ vā no karissati
    WISH = "thấy rõ năm lý do này, cha mẹ mong muốn người con trai sinh ra trong gia đình"
    WANT = "những người sáng suốt mong muốn người con trai"                # puttaṃ icchanti paṇḍitā
    add("5-491",
        f"{S.na_vattabbam(ITO)} {YES} {S.NANU_VUTTAM} “{BH}, {WISH}! Năm lý do nào? {cap(BHATO)}, dòng dõi gia "
        f"đình sẽ duy trì lâu dài, nó sẽ tiếp nhận gia tài, hoặc nữa, nó sẽ dâng phần cúng dường cho các ngạ quỷ, "
        f"những người đã qua đời – {bh}, {WISH}”.",
        f"“Thấy rõ năm lý do, {WANT};",
        f"{cap(BHATO)}.",
        "“Dòng dõi gia đình sẽ kéo dài lâu, nó tiếp nhận gia tài;",
        "Hoặc nữa, cho các ngạ quỷ, nó sẽ dâng phần cúng dường.",
        f"“Thấy rõ những lý do này, {WANT};",
        "Vì vậy, những người hiền thiện, những người chân chính, biết ơn, ghi nhớ ơn,",
        "“Nuôi dưỡng cha mẹ, nhớ lại những gì đã được làm trước đây;",
        "Làm các công việc cho họ, như đối với những người đã làm ơn trước đây.",
        "“Làm theo lời khuyên dạy, nuôi dưỡng người đã nuôi dưỡng mình, không làm suy tàn dòng dõi gia đình;",
        f"Có niềm tin, thành tựu giới hạnh, người con trai trở thành người đáng được khen ngợi” "
        f"[{CIT['a. ni.']} 5.31].",
        f"{S.ATTHEVA} {YES} {S.tena_hi(ITO)}",
        S.katha_end(KATHA[6]))

    # ---- (69) 7. Pathavī kammavipākotikathā ---------------------------------------------------------------------
    heading("5-15-7-0", 4, VAGGA)
    heading("5-15-7-1-0", 5, f"(69) 7. {S.katha(KATHA[7])}")
    AVF_V = f"{AV7[0]}{S.var('Syā., Kaṃ.', 'āvajjanā')}, " + ", ".join(AV7[1:])
    NEG_IF = f"nó {NEG_SH}; nó không có {AVS}"
    PH_K, PT_K = f"sự tiếp xúc là {KV}, sự tiếp xúc", f"{PK}, đất"   # phasso kammavipāko, phasso … / pathavī …
    BUY = "có thể mua, bán, cầm cố, thu gom, chọn lựa"                  # labbhā ketuṃ vikketuṃ āṭhapetuṃ ocinituṃ vicinituṃ
    add("5-492",
        f"{Q(PK)} {YES} Có phải nó {POS_FULL}; nó có {AVF_V} không? {NO_PE} "
        f"{nanu_l(f'nó {NEG_FULL}; nó không có {AVF}')} {YES} {S.hanci_neg(NEG_IF, PK)}",
        f"Có phải {PH_K} {POS_PE}; nó có {AVS} không? {YES} Có phải {PT_K} {POS_PE}; nó có {AVF} không? {NO_PE} "
        f"{q(f'{PT_K} {NEG_SH}; nó không có {AVS}')} {YES} Có phải {PH_K} {NEG_SH}; nó không có {AVS} không? {NO_PE}",
        f"{Q(PK)} {YES} {Q(f'đất {PG}')} {YES} {Q(f'{KV} {PG}')} {NO_PE}",
        f"{Q(f'{BUY} đất')} {YES} {Q(f'{BUY} {KV}')} {NO_PE}")
    COM = f"{KV} là thứ chung cho người khác"                            # kammavipāko paresaṃ sādhāraṇo
    L10 = ", ".join(LIST10)                                              # phassaṃ vedanaṃ … paññaṃ
    add("5-493",
        f"{Q('đất là thứ chung cho người khác')} {YES} {Q(COM)} {NO_PE}",
        f"{Q(COM)} {YES} {S.NANU_VUTTAM}",
        "“Là kho báu không chung cho người khác, kẻ trộm không lấy đi được;",
        "Con người hãy làm các việc phước, nếu thực hành hành vi tốt đẹp” "
        "[Tiểu Tụng 8.9 trong Tiểu Tụng, hơi khác một chút].",
        f"{S.ATTHEVA} {YES} {S.tena_hi_na(COM)}",
        f"{Q(PK)} {YES} {Q('trước tiên đất hình thành, sau đó chúng sinh sinh khởi')} {YES} "
        f"{Q(f'trước tiên {VIP} sinh khởi, sau đó người ta tạo nghiệp để có được {VIP}')} {NO_PE}",
        f"{Q(f'đất là {KV} của tất cả chúng sinh')} {YES} {Q('tất cả chúng sinh thọ hưởng đất')} {NO_PE} "
        f"{q('tất cả chúng sinh thọ hưởng đất')} {YES} "
        f"{Q('có những người nhập Niết-bàn trọn vẹn mà không thọ hưởng đất')} {YES} "
        f"{Q(f'có những người nhập Niết-bàn trọn vẹn mà chưa làm diệt tận {KV}')} {NO_PE}",
        f"{Q(f'đất là {KV} của {CV}')} {YES} {Q('các chúng sinh khác thọ hưởng đất')} {YES} "
        f"{Q(f'các chúng sinh khác thọ hưởng {KV} của {CV}')} {NO_PE} "
        f"{q(f'các chúng sinh khác thọ hưởng {KV} của {CV}')} {YES} "
        f"{Q(f'các chúng sinh khác thọ hưởng {L10} của {CV}')} {NO_PE}")
    ISS = "có nghiệp dẫn đến quyền uy, nghiệp dẫn đến quyền thống trị"  # issariya- / adhipaccasaṃvattaniyaṃ kammaṃ
    add("5-494",
        f"{S.na_vattabbam(PK)} {YES} {NANU(ISS)} {YES} {S.hanci(ISS, PK)}",
        S.katha_end(KATHA[7]))

    # ---- (70) 8. Jarāmaraṇaṃ vipākotikathā ----------------------------------------------------------------------
    heading("5-15-8-0", 4, VAGGA)
    heading("5-15-8-1-0", 5, f"(70) 8. {S.katha(KATHA[8])}")
    PH_V, JM_V = f"sự tiếp xúc là {VIP}, sự tiếp xúc", f"{T8}, {JM}"
    add("5-495",
        f"{Q(T8)} {YES} Có phải nó {POS_FULL}; nó có {AVF} không? {NO_PE} {nanu_l(NEG_IF)} {YES} "
        f"{S.hanci_neg(NEG_IF, T8)}",
        f"Có phải {PH_V} {POS_SH}; nó có {AVS} không? {YES} Có phải {JM_V} {POS_SH}; nó có {AVS} không? {NO_PE}",
        f"Có phải {JM_V} {NEG_SH}; nó không có {AVS} không? {YES} Có phải {PH_V} {NEG_SH}; nó không có {AVS} không? "
        f"{NO_PE}")

    def of(k):
        return f"của các hiện tượng {k}"

    def l_is(a, b):                 # A-ānaṃ dhammānaṃ jarāmaraṇaṃ, B-ānaṃ dhammānaṃ vipākoti?
        return f"Có phải {JM} {of(a)} là {VIP} {of(b)} không?"

    def l_na(a, b):                 # A-ānaṃ … jarāmaraṇaṃ, na vattabbaṃ – "B-ānaṃ dhammānaṃ vipāko"ti?
        return f"Có phải đối với {JM} {of(a)}, không nên nói – “{VIP} {of(b)}” không?"

    K_, AK_, KA_ = "thiện", "bất thiện", "thiện và bất thiện"
    add("5-496", *[f"{f(a, b)} {YES} {f(c, d)} {NO_PE}" for f, a, b, c, d in (
        (l_is, AK_, AK_, K_, K_), (l_na, K_, K_, AK_, AK_), (l_is, K_, AK_, AK_, K_),
        (l_na, AK_, K_, K_, AK_), (l_is, KA_, AK_, KA_, K_), (l_na, KA_, K_, KA_, AK_))])
    DUB = "có nghiệp dẫn đến sự xấu xí, nghiệp dẫn đến tuổi thọ ngắn"   # dubbaṇṇa- / appāyukasaṃvattaniyaṃ kammaṃ
    add("5-497",
        f"{S.na_vattabbam(T8)} {YES} {NANU(DUB)} {YES} {S.hanci(DUB, T8)}",
        S.katha_end(KATHA[8]))

    # ---- (71) 9. Ariyadhammavipākakathā -------------------------------------------------------------------------
    heading("5-15-9-0", 4, VAGGA)
    heading("5-15-9-1-0", 5, f"(71) 9. {S.katha(KATHA[9])}")
    MAH = "đời sống sa-môn có quả lớn, đời sống bà-la-môn có quả lớn"   # mahapphalaṃ sāmaññaṃ mahapphalaṃ brahmaññaṃ
    DF, SF, BF = "quả của sự bố thí", "quả của giới hạnh", "quả của sự tu tập"   # dāna- / sīla- / bhāvanāphalaṃ

    def nv(x):
        return f"{x} không phải là {VIP}"

    def iv(x):
        return f"{x} là {VIP}"

    SAANAR = f"{SA}{PE} {AN}{PE} {AR}"
    SB = f"{SF}{PE} {BF}"
    add("5-498",
        f"{Q(NAV)} {YES} {NANU(MAH)} {YES} {S.hanci_neg(MAH, NAV)}",
        f"{Q(NAV)} {YES} {NANU(f'có {SO}')} {YES} {S.hanci_neg(f'có {SO}', NAV)} {NANU(f'có {SAANAR}')} {YES} "
        f"{S.hanci_neg(f'có {AR}', NAV)}",
        f"{Q(nv(SO))} {YES} {Q(nv(DF))} {NO_PE} {q(nv(SO))} {YES} {Q(nv(SB))} {NO_PE}",
        f"{Q(nv(SAANAR))} {YES} {Q(nv(DF))} {NO_PE} {q(nv(AR))} {YES} {Q(nv(SB))} {NO_PE} {q(iv(DF))} {YES} "
        f"{Q(iv(SO))} {NO_PE}",
        f"{Q(iv(DF))} {YES} {Q(iv(SAANAR))} {NO_PE} {q(iv(SB))} {YES} {Q(iv(SO))} {NO_PE} {q(iv(BF))} {YES} "
        f"{Q(iv(SAANAR))} {NO_PE}")
    KK, RK, AK, LK = ("điều thiện thuộc cõi dục lạc", "điều thiện thuộc cõi hình sắc",
                      "điều thiện thuộc cõi không hình sắc", "điều thiện vượt thế gian")   # (termbase)
    RA_FULL = f"{RK}{PE} {AK}"                                           # rūpāvacaraṃ kusalaṃ…pe… arūpāvacaraṃ kusalaṃ
    RA_SHORT = f"{RK}{PE} thuộc cõi không hình sắc"                      # rūpāvacaraṃ…pe… arūpāvacaraṃ kusalaṃ
    SV, AVP = "có quả trổ", "không có quả trổ"                           # savipākaṃ / avipākaṃ
    SAC, SAP = "có quả trổ dẫn đến sự tích lũy", "có quả trổ dẫn đến sự giảm trừ"   # savipākaṃ ācaya- / apacayagāmī
    add("5-499",
        f"{Q(f'{KK} {SV}')} {YES} {Q(f'{LK} {SV}')} {NO_PE} {q(f'{RA_FULL} {SV}')} {YES} {Q(f'{LK} {SV}')} {NO_PE}",
        f"{Q(f'{LK} {AVP}')} {YES} {Q(f'{KK} {AVP}')} {NO_PE} {q(f'{LK} {AVP}')} {YES} {Q(f'{RA_SHORT} {AVP}')} "
        f"{NO_PE}")
    add("5-500",
        f"{Q(f'{KK} {SAC}')} {YES} {Q(f'{LK} {SAC}')} {NO_PE} {q(f'{RA_SHORT} {SAC}')} {YES} {Q(f'{LK} {SAC}')} "
        f"{NO_PE}",
        f"{Q(f'{LK} {SAP}')} {YES} {Q(f'{KK} {SAP}')} {NO_PE} {Q(f'{LK} {SAP}')} {YES} {Q(f'{RA_SHORT} {SAP}')} "
        f"{NO_PE}",
        S.katha_end(KATHA[9]))

    # ---- (72) 10. Vipāko vipākadhammadhammotikathā --------------------------------------------------------------
    heading("5-15-10-0", 4, VAGGA)
    heading("5-15-10-1-0", 5, f"(72) 10. {S.katha(KATHA[10])}")
    TS10 = f"{VIP} của nó là {VD}"                                        # tassa vipāko vipākadhammadhammo
    add("5-501",
        f"{Q(T10)} {YES} {Q(TS10)} {NO_PE} {q(TS10)} {YES} {Q(S.TASSA_TASSEVA)} {NO_PE}",
        f"{Q(T10)} {YES} Có phải gọi là {VIP} hay gọi là {VD}, gọi là {VD} hay gọi là {VIP}, thì {ESESE} không? "
        f"{NO_PE}",
        f"{Q(T10)} {YES} Có phải {VIP} và {VD}, {VD} và {VIP}, {CONJ8} không? {NO_PE}",
        f"{Q(T10)} {YES} "
        f"{Q(f'chính cái bất thiện ấy là {VIP} của cái bất thiện, chính cái thiện ấy là {VIP} của cái thiện')} "
        f"{NO_PE}",
        f"{Q(T10)} {YES} Có phải bằng chính tâm nào mà giết hại sinh mạng, thì bằng chính tâm ấy bị nung đốt trong "
        f"địa ngục, bằng chính tâm nào mà {GIVE_D}, thì bằng chính tâm ấy vui hưởng trên cõi trời không? {NO_PE}")
    AGG = f"bốn khối phi vật chất là {VIP}, là điều kiện lẫn nhau"       # vipākā cattāro khandhā arūpino aññamaññapaccayā
    add("5-502",
        f"{S.na_vattabbam(T10)} {YES} {NANU(AGG)} {YES} {S.hanci(AGG, T10)}",
        S.katha_end(KATHA[10]),
        f"{VAGGA}.",
        TASSUDDANAM,
        UDDANA)
    return segs


def main():
    check_strings()
    S.check_reused()
    segs = build()
    S.check_against_pali(NAME, segs)
    text = unicodedata.normalize("NFC", "\n\n".join("\n".join(s) for s in segs) + "\n")
    assert "\n\n\n" not in text and "\r" not in text
    (S.OUT_DIR / NAME).write_text(text, encoding="utf-8", newline="\n")
    print("wrote", S.OUT_DIR / NAME)
    adh = S.FORMULAS_MD.parent / "adh-15"           # byte-identical copy for termbase_adherence_vi.py
    adh.mkdir(exist_ok=True)
    (adh / NAME).write_text(text, encoding="utf-8", newline="\n")
    print("wrote", adh / NAME)


if __name__ == "__main__":
    main()
