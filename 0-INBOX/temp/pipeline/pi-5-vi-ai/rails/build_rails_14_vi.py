"""pi-5 Kathāvatthu, Vietnamese RAILS (plain audience): chapter 14, Chaṭṭhavaggo (^5-14-0 … ^5-470): ten kathās
(53-62) with the repeated "Chaṭṭhavaggo" sub-headings, the vagga close and the uddāna.

Builds AI_translation/vietnamese/pi-5-vietnamese-plain-rails_split_chapters/14-chatthavaggo.md from the fixed
strings below, importing the approved sample builder READ-ONLY (frames Q, q, NANU, hanci, hanci_neg, na_vattabbam,
tena_hi, katha, katha_end, vaggo, var …). Strings taken from pi-1 … pi-4 rails are asserted there (REUSED14);
strings shared with the finished pi-5 rails chapters (sample, ch4, ch9-ch12) are asserted in those chapter files
(SHARED). The per-line dash / quote / NFC / id checks of S.check_against_pali run before writing.
New recurring strings: notes-rails-14.md.

usage: python -I -X utf8 -B build_rails_14_vi.py          (writes the chapter and the adherence copy rails\\adh-14\\)
"""
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai\rails")
import build_rails_sample_vi as S  # noqa: E402

NAME = "14-chatthavaggo.md"
Q, q, NANU, PE, YES, NO_PE = S.Q, S.q, S.NANU, S.PE, S.YES, S.NO_PE
cap, RE, CIT = S.cap, S.RE, S.CIT

# ---------------------------------------------------------------------------------------------------------------
# Core words (termbase; pi-1 / pi-2; ch10)
# ---------------------------------------------------------------------------------------------------------------
ASK = "không do điều kiện tạo thành"                 # asaṅkhato / asaṅkhataṃ / asaṅkhatā (termbase, sample)
SK = "do điều kiện tạo thành"                         # saṅkhato (termbase, sample)
ASKT = f"điều {ASK}"                                 # asaṅkhataṃ (noun; termbase)
SKT = f"điều {SK}"                                   # saṅkhataṃ (noun)
NIB = "Niết-bàn"                                      # nibbānaṃ
NIB_LIST = ("đó là Niết-bàn, nơi che chở, nơi ẩn náu, nơi nương tựa, nơi đến cuối cùng, điều bất biến, "
            "điều bất tử")                            # Nibbānaṃ tāṇaṃ leṇaṃ saraṇaṃ parāyanaṃ accutaṃ amataṃ (termbase)
NIY = "sự cố định"                                    # niyāmo (termbase; ch12 Niyāmokkantikathā)
NIY_SO, NIY_SA = "sự cố định vào dòng", "sự cố định trở lại một lần"
NIY_AN, NIY_AR = "sự cố định không trở lại", "sự cố định A-la-hán"     # (termbase phrases)
NIY_MI = "sự cố định theo hướng sai lầm"              # micchattaniyāmo (pi-1 «cố định theo hướng sai lầm»)
NIY_SAM = "sự cố định theo hướng đúng đắn"            # sammattaniyāmo (pi-1 «cố định theo hướng đúng đắn»)
MAG = "con đường"                                     # maggo
M_SO, M_AR = "con đường vào dòng", "con đường A-la-hán"                # sotāpattimaggo / arahattamaggo (termbase)
PS = "sự sinh khởi tùy thuộc vào điều kiện"           # paṭiccasamuppādo (termbase, pi-1)
AVIJ = "vô minh"                                      # avijjā
L_AV = "vô minh làm điều kiện cho các sự tạo tác"     # avijjāpaccayā saṅkhārā (pi-2)
L_SK = "các sự tạo tác làm điều kiện cho thức"        # saṅkhārapaccayā viññāṇaṃ (pi-2)
L_BH = "sự hiện hữu làm điều kiện cho sự sinh"        # bhavapaccayā jāti (pi-2)
L_JA = "sự sinh làm điều kiện cho sự lão hóa và sự chết"   # jātipaccayā jarāmaraṇaṃ (pi-2)
LINKS = ["các sự tạo tác do vô minh làm điều kiện", "thức do các sự tạo tác làm điều kiện",
         "phần tinh thần và vật chất do thức làm điều kiện", "sự lão hóa và sự chết do sự sinh làm điều kiện"]
#   avijjāpaccayā saṅkhārā / saṅkhārapaccayā viññāṇaṃ / viññāṇapaccayā nāmarūpaṃ / jātipaccayā jarāmaraṇaṃ
#   (as subjects of "… asaṅkhatā / saṅkhatā"; termbase Avijjāpaccayā asaṅkhatā «do vô minh làm điều kiện …»)
IDAPP = "quy luật tùy thuộc vào điều kiện"            # idappaccayatā (termbase, pi-1)
DTN = "sự ổn định của các hiện tượng, tính cố định của các hiện tượng"   # dhammaṭṭhitatā dhammaniyāmatā (termbase)
DS, SS = "sự thật về khổ đau", "sự thật về sự phát sinh"                # dukkhasaccaṃ / samudayasaccaṃ (termbase, ch10)
NS, MS = "sự thật về sự chấm dứt", "sự thật về con đường"               # nirodhasaccaṃ / maggasaccaṃ (ch10)
DUK, SAM, NIR = "khổ đau", "sự phát sinh", "sự chấm dứt"                 # dukkhaṃ / samudayo / nirodho (termbase)
SOKA5 = "sự sầu muộn, sự than khóc, sự khó chịu, nỗi buồn và sự tuyệt vọng"   # sokaparideva… (pi-1, ch10)
DUK_L = f"sự khó chịu nơi thân, sự khó chịu trong tâm, {SOKA5}"          # kāyikaṃ dukkhaṃ cetasikaṃ dukkhaṃ … (ch10)
TAN = "khao khát dục lạc, khao khát được hiện hữu, khao khát không còn hiện hữu"   # kāma- / bhava- / vibhavataṇhā (pi-2)
SAMMA_PE = f"{S.SAMMA[0]}{PE} {S.SAMMA[-1]}"          # sammādiṭṭhi…pe… sammāsamādhi (pi-1)
SACCA4 = ["đây là khổ đau", "đây là sự phát sinh của khổ đau", "đây là sự chấm dứt khổ đau",
          "đây là cách thực hành dẫn đến sự chấm dứt khổ đau"]           # idaṃ dukkhaṃ … (pi-2, ch10)
AK = "lĩnh vực không gian vô tận"                      # ākāsānañcāyatana (pi-1, ch11)
BHAVO7 = ("sự hiện hữu, cõi tái sinh, nơi cư trú của chúng sinh, vòng luân hồi, cách sinh, chỗ trú của thức, "
          "sự có được sự tồn tại cá nhân")             # bhavo gati sattāvāso saṃsāro yoni viññāṇaṭṭhiti attabhāvapaṭilābho (ch11)
BORN = "sinh ra, già đi, qua đời, chết đi, tái sinh"   # jāyanti jīyanti mīyanti cavanti upapajjanti (termbase)
CATU = "sự hiện hữu gồm bốn khối"                      # catuvokārabhavo (pi-2)
ARU = "bốn trạng thái không hình sắc"                  # cattāro āruppā (termbase āruppā)
VR = "Đức Thế Tôn đã nói rằng"                         # … vuttā bhagavatā (ch4)
NSAM = "thành tựu thiền chấm dứt"                      # nirodhasamāpatti (termbase)
SANKH = {"v": "sự tạo tác bằng lời nói", "k": "sự tạo tác bằng thân", "c": "sự tạo tác bằng tâm"}   # (pi-2)
AKASA = "không gian"                                   # ākāso (termbase)
ANAK = "điều không phải là không gian"                 # anākāsaṃ / anākāso
VERBS = ("có được, làm sinh khởi, làm phát khởi, làm khởi lên, làm dấy lên, làm hình thành, làm hình thành trọn vẹn, "
         "làm sinh ra, làm sinh ra trọn vẹn nó")
#   paṭilabhanti uppādenti samuppādenti uṭṭhāpenti samuṭṭhāpenti nibbattenti abhinibbattenti janenti sañjanenti
RUPA_L = ("đó là hình sắc, là lĩnh vực hình sắc, là yếu tố hình sắc, là màu xanh, màu vàng, màu đỏ, màu trắng, "
          "được nhận biết bằng mắt, va chạm vào mắt, đi vào tầm của mắt")   # Rūpaṃ rūpāyatanaṃ … āgacchati (sample ^5-214)
RUPA_S = f"đó là hình sắc, là lĩnh vực hình sắc, là yếu tố hình sắc{PE} đi vào tầm của mắt"
EYE_R = "tùy thuộc vào mắt và các hình sắc, sinh khởi thức qua mắt"   # cakkhuñca paṭicca rūpe ca uppajjati … (pi-2)
NO_HAVE = "Không có."                                  # Natthi. (ch12)
ATTH = S.ATTHEVA                                       # Attheva suttantoti?  «Có bài kinh như vậy thật không?»
ATTH_L = "có bài kinh như vậy thật không?"             # "…"nti – attheva suttantoti?
PD, AP, TE, VA = "yếu tố đất", "yếu tố nước", "yếu tố lửa", "yếu tố gió"   # pathavī- / āpo- / tejo- / vāyodhātu (termbase)
CI = "năng lực mắt"                                    # cakkhundriyaṃ (pi-2)
KK = "nghiệp bằng thân"                                # kāyakammaṃ (termbase)
WALK6 = ("ai đó đang đi tới, đang đi lui, đang nhìn thẳng, đang nhìn quanh, đang co lại, đang duỗi ra")
#   abhikkamantaṃ paṭikkamantaṃ ālokentaṃ vilokentaṃ samiñjentaṃ pasārentaṃ (termbase; pi-2 «đi lui», «nhìn quanh»)


def a(x):                             # X asaṅkhato
    return f"{x} {ASK}"


def s(x):                             # X saṅkhato
    return f"{x} {SK}"


def vis(x):                           # X sanidassano (termbase «thấy được»)
    return f"{x} thấy được"


def n_ask(n):                         # N asaṅkhatāni
    return f"có {n} {ASKT}"


def refuges(n):                       # N tāṇāni N leṇāni … N nibbānāni
    return (f"có {n} nơi che chở, {n} nơi ẩn náu, {n} nơi nương tựa, {n} nơi đến cuối cùng, {n} điều bất biến, "
            f"{n} điều bất tử, {n} Niết-bàn")


def refuges_pe(n, two=False):         # N tāṇāni (N leṇāni)…pe… antarikā vā
    return f"có {n} nơi che chở" + (f", {n} nơi ẩn náu" if two else "") + f"{PE} hoặc khoảng cách"


def nibb(n):                          # N nibbānāni
    return f"có {n} Niết-bàn"


def gap(n):                           # atthi N-nnaṃ nibbānānaṃ uccanīcatā … antarikā vā (ch10)
    return (f"giữa {n} Niết-bàn có sự cao thấp, sự thấp kém và ưu việt, sự hơn kém, hoặc ranh giới, "
            f"hoặc sự phân chia, hoặc đường vạch, hoặc khoảng cách")


def okk(verb_obj):                    # atthi keci X okkamanti / samāpajjanti paṭilabhanti … sañjanenti
    return f"có ai đó {verb_obj}, {VERBS}"


def cease(x):                         # X-e uppajja niruddhe aniyato hoti
    return f"khi {x} đã sinh khởi rồi đã chấm dứt, thì người ta trở thành không cố định"


def dt(link):                         # L-ti yā tattha dhammaṭṭhitatā dhammaniyāmatā asaṅkhatā
    return f"trong việc {link}, {DTN} ở đó {ASK}"


def eye(x):                           # cakkhuñca paṭicca X-ñca uppajjati cakkhuviññāṇaṃ (pi-2 frame)
    return f"tùy thuộc vào mắt và {x}, sinh khởi thức qua mắt"


def two_block(x, cap2=False):         # X asaṅkhato … nibbānaṃ … dve asaṅkhatāni … dve tāṇāni…pe… antarikā vā
    third = Q(n_ask("hai")) if cap2 else q(n_ask("hai"))
    return (f"{Q(a(x))} {YES} {Q(NIB_LIST)} {NO_PE} {q(f'{a(x)}, {a(NIB)}')} {YES} {Q(n_ask('hai'))} {NO_PE} "
            f"{third} {YES} {Q(refuges_pe('hai'))} {NO_PE}")


def visible(i_rupa, i_eye, i_sutta, x, short=False, v="", cit=""):
    """The three lines of an 'X sanidassano' refutation (^5-463, 465, 467, 469)."""
    l1 = f"{Q(vis(x))} {YES} {Q(RUPA_S if short else RUPA_L)} {NO_PE}"
    l2 = f"{Q(vis(x))} {YES} {Q(eye(x))} {NO_PE}"
    att = f"có{v} bài kinh như vậy thật không?"
    l3 = (f"{Q(eye(x))} {YES} “{cap(eye(x))}” – {att} {NO_HAVE} “{cap(EYE_R)}”{cit} – {ATTH_L} {YES} "
          f"Nếu “{EYE_R}” – có bài kinh như vậy thật, thì {RE}, chắc chắn không nên nói – “{eye(x)}”.")
    return l1, l2, l3


def seen(x, what, v="", pe=False, tail=True):
    """Na vattabbaṃ – "X sanidassano"ti? … Nanu passati Y-nti? … Hañci passati Y, tena vata re vattabbe – "X"ti."""
    h = S.hanci(f"người ta thấy{v} {what}", vis(x))
    if pe:
        h = h[:-1] + PE
    return f"{S.na_vattabbam(vis(x))} {YES} {NANU(f'người ta thấy {what}')} {YES} {h}"


# ---------------------------------------------------------------------------------------------------------------
# Headings, kathā names, vagga close
# ---------------------------------------------------------------------------------------------------------------
VAGGA = S.vaggo(6)                                     # Chaṭṭhavaggo «Chương thứ sáu» (termbase)
KATHA = {1: NIY, 2: PS, 3: "các sự thật", 4: "các trạng thái không hình sắc", 5: NSAM, 6: AKASA,
         7: f"việc {vis(AKASA)}", 8: f"việc {vis(PD)} và các mục khác", 9: f"việc {vis(CI)} và các mục khác",
         10: f"việc {vis(KK)}"}
#   Niyāma-, Paṭiccasamuppāda-, Sacca-, Āruppa-, Nirodhasamāpatti-, Ākāsakathā, Ākāso sanidassanoti-,
#   Pathavīdhātu sanidassanātiādi-, Cakkhundriyaṃ sanidassanantiādi-, Kāyakammaṃ sanidassanantikathā
TASSUDDANAM = "Tóm tắt của chương này –"               # Tassuddānaṃ – (ch9)
UDDANA = (f"{cap(a(NIY))}, {a(PS)}, {a('bốn sự thật')}, {a(ARU)}, {a(NSAM)}, {a(AKASA)}, {vis(AKASA)}, "
          f"bốn yếu tố cơ bản, năm năng lực, cũng vậy với {KK}.")
#   Niyamo asaṅkhato, paṭiccasamuppādo asaṅkhato, cattāri saccāni asaṅkhatāni, cattāro āruppā asaṅkhatā,
#   nirodhasamāpatti asaṅkhatā, ākāso asaṅkhato, ākāso sanidassano, cattāro mahābhūtā, pañcindriyāni,
#   tatheva kāyakammanti.

REUSED14 = [  # (Pāli, Vietnamese, book)
    ("avijjāpaccayā saṅkhārā", L_AV, "2"), ("saṅkhārapaccayā viññāṇaṃ", L_SK, "2"),
    ("viññāṇapaccayā nāmarūpaṃ", "thức làm điều kiện cho phần tinh thần và vật chất", "2"),
    ("bhavapaccayā jāti", L_BH, "2"), ("jātipaccayā jarāmaraṇaṃ", L_JA, "2"),
    ("sokaparidevadukkhadomanassupāyāsā", SOKA5, "1"),
    ("kāmataṇhā, bhavataṇhā, vibhavataṇhā", TAN, "2"),
    ("kāyasaṅkhāro", SANKH["k"], "2"), ("vacīsaṅkhāro", SANKH["v"], "2"), ("cittasaṅkhāro", SANKH["c"], "2"),
    ("micchattaniyatā", "cố định theo hướng sai lầm", "1"), ("sammattaniyatā", "cố định theo hướng đúng đắn", "1"),
    ("ākāsānañcāyatana", AK, "1"), ("catuvokārabhavo", CATU, "2"),
    ("cakkhuñca paṭicca rūpe ca uppajjati", "tùy thuộc vào mắt và các hình sắc, sinh khởi", "2"),
    ("cattāro mahābhūtā", "bốn yếu tố cơ bản", "1"), ("idappaccayatā", IDAPP, "1"),
    ("nīlaṃ pītakaṃ lohitakaṃ odātaṃ", "màu xanh, màu vàng, màu đỏ, màu trắng", "1"),
    ("dukkhaṃ, dukkhasamudayo, dukkhanirodho, dukkhanirodhagāminī paṭipadā",
     "khổ đau, sự phát sinh của khổ đau, sự chấm dứt khổ đau, cách thực hành dẫn đến sự chấm dứt khổ đau", "2"),
    ("abhikkante paṭikkante … ālokite vilokite", "khi đi tới, khi đi lui", "2"),
    ("ālokite vilokite", "khi nhìn thẳng, khi nhìn quanh", "2"),
    ("sanidassana", "thấy được", "1"), ("paṭiccasamuppāda", PS, "1"),
]

SHARED = [  # (Pāli, Vietnamese, finished pi-5 rails chapter)
    ("atthi dvinnaṃ nibbānānaṃ uccanīcatā … antarikā vā", gap("hai"), "10-dutiyavaggo.md"),
    ("dve nibbānāni", nibb("hai"), "10-dutiyavaggo.md"),
    ("dve tāṇāni…pe… dve amatāni", "có hai nơi che chở… hai nơi ẩn náu… hai nơi nương tựa… hai nơi đến cuối cùng… "
     "hai điều bất biến… hai điều bất tử… hai Niết-bàn", "10-dutiyavaggo.md"),
    ("dve nirodhasaccāni", "có hai sự thật về sự chấm dứt", "10-dutiyavaggo.md"),
    ("dve dukkhasaccāni / samudayasaccāni / maggasaccāni", "có hai sự thật về khổ đau", "10-dutiyavaggo.md"),
    ("dve samudayasaccāni", "có hai sự thật về sự phát sinh", "10-dutiyavaggo.md"),
    ("dve maggasaccāni", "có hai sự thật về con đường", "10-dutiyavaggo.md"),
    ("dukkhā vedanā kāyikaṃ dukkhaṃ cetasikaṃ dukkhaṃ sokaparideva…", DUK_L, "10-dutiyavaggo.md"),
    ("vacīsaṅkhārā", "các sự tạo tác bằng lời nói", "10-dutiyavaggo.md"),
    ("Atthi keci …ti?", "Có phải có ai đó", "10-dutiyavaggo.md"),
    ("Chaṭṭhavaggo / Dutiyavaggo … (S.vaggo)", "Chương thứ hai", "10-dutiyavaggo.md"),
    ("Rūpaṃ rūpāyatanaṃ rūpadhātu … cakkhussa āpāthaṃ āgacchati",
     "là hình sắc, là lĩnh vực hình sắc, là yếu tố hình sắc, là màu xanh, màu vàng, màu đỏ, màu trắng, được nhận "
     "biết bằng mắt, va chạm vào mắt, đi vào tầm của mắt", "1-puggalakatha.md"),
    ("bhavo gati sattāvāso saṃsāro yoni … attabhāvapaṭilābho",
     "cõi tái sinh, nơi cư trú của chúng sinh, vòng luân hồi, cách sinh", "11-tatiyavaggo.md"),
    ("attabhāvapaṭilābho", "sự có được sự tồn tại cá nhân", "11-tatiyavaggo.md"),
    ("ākāsānañcāyatana", AK, "11-tatiyavaggo.md"),
    ("Natthi.", NO_HAVE, "12-catutthavaggo.md"),
    ("Niyāmokkantikathā", "Bàn về việc bước vào sự cố định", "12-catutthavaggo.md"),
    ("Nanu … vuttaṃ bhagavatāti?", f"Chẳng phải {VR}", "4-jahatikatha.md"),
    ("Tassuddānaṃ –", TASSUDDANAM, "9-hevatthikatha.md"),
]


def check_strings():
    texts = {b: unicodedata.normalize("NFC", "\n".join(p.read_text(encoding="utf-8")
                                                       for p in sorted(d.glob("*.md")))).lower()
             for b, d in S.RAILS.items()}
    bad = [(p, v, b) for p, v, b in REUSED14 if unicodedata.normalize("NFC", v).lower() not in texts[b]]
    assert not bad, "reused strings not found in their rails: " + repr(bad)
    bad = []
    for p, v, f in SHARED:
        t = unicodedata.normalize("NFC", (S.OUT_DIR / f).read_text(encoding="utf-8"))
        if unicodedata.normalize("NFC", v) not in t:
            bad.append((p, v, f))
    assert not bad, "shared strings not found in their chapters: " + repr(bad)


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

    heading("5-14-0", 3, VAGGA)

    # ---- (53) 1. Niyāmakathā ----------------------------------------------------------------------------------
    heading("5-14-1-0", 4, f"(53) 1. {S.katha(KATHA[1])}")
    add("5-445",
        f"{Q(a(NIY))} {YES} {Q(NIB_LIST)} {NO_PE}",
        f"{Q(f'{a(NIY)}, {a(NIB)}')} {YES} {Q(n_ask('hai'))} {NO_PE}",
        f"{Q(n_ask('hai'))} {YES} {Q(refuges('hai'))} {NO_PE}",
        f"{Q(nibb('hai'))} {YES} {Q(gap('hai'))} {NO_PE}",
        f"{Q(a(NIY))} {YES} {Q(okk(f'bước vào {NIY}'))} {YES} {Q(okk(f'bước vào {ASKT}'))} {NO_PE}")
    add("5-446",
        f"{Q(a(NIY))} {YES} {Q(a(MAG))} {NO_PE}",
        f"{Q(s(MAG))} {YES} {Q(s(NIY))} {NO_PE}",
        f"{Q(a(NIY_SO))} {YES} {Q(a(M_SO))} {NO_PE}",
        f"{Q(s(M_SO))} {YES} {Q(s(NIY_SO))} {NO_PE}",
        f"Có phải {NIY_SA}{PE} {NIY_AN}{PE} {a(NIY_AR)} không? {YES} {Q(a(M_AR))} {NO_PE} "
        f"{q(s(M_AR))} {YES} {Q(s(NIY_AR))} {NO_PE}",
        f"Có phải {a(NIY_SO)}{PE} {a(NIY_AR)}, {a(NIB)} không? {YES} {Q(n_ask('năm'))} {NO_PE} "
        f"{q(n_ask('năm'))} {YES} {Q(refuges_pe('năm'))} {NO_PE}",
        f"{Q(a(NIY))} {YES} {Q(a(NIY_MI))} {NO_PE} {q(s(NIY_MI))} {YES} {Q(s(NIY_SAM))} {NO_PE}")
    add("5-447",
        f"{S.na_vattabbam(a(NIY))} {YES} {Q(cease(NIY))} {NO_PE} {S.tena_hi(a(NIY))} "
        f"{Q(cease(NIY_MI))} {NO_PE} vậy thì {a(NIY_MI)}.",
        S.katha_end(KATHA[1]))

    # ---- (54) 2. Paṭiccasamuppādakathā ------------------------------------------------------------------------
    heading("5-14-2-0", 4, VAGGA)
    heading("5-14-2-1-0", 5, f"(54) 2. {S.katha(KATHA[2])}")
    add("5-448",
        f"{Q(a(PS))} {YES} {Q(NIB_LIST)} {NO_PE} {q(f'{a(PS)}, {a(NIB)}')} {YES} {Q(n_ask('hai'))} {NO_PE} "
        f"{q(n_ask('hai'))} {YES} {Q(refuges('hai'))} {NO_PE} {q(nibb('hai'))} {YES} {Q(gap('hai'))} {NO_PE}")
    l449 = [f"{Q(a(PS))} {YES} {Q(a(AVIJ))} {NO_PE} {q(s(AVIJ))} {YES} {Q(s(PS))} {NO_PE}"]
    for x in LINKS:
        l449.append(f"{q(a(PS))} {YES} {Q(a(x))} {NO_PE} {q(s(x))} {YES} {Q(s(PS))} {NO_PE}")
    add("5-449", " ".join(l449))
    UPP = ("Dù có sự sinh khởi của các Như Lai hay không có sự sinh khởi của các Như Lai, "
           "yếu tố ấy vẫn đã đứng vững")
    #   Uppādā vā tathāgatānaṃ anuppādā vā tathāgatānaṃ ṭhitāva sā dhātu
    SUT1 = (f"{S.NANU_VUTTAM} “này các tỳ-khưu, {L_JA}. {UPP}, {DTN}, {IDAPP}. Như Lai giác ngộ, thấu hiểu điều ấy. "
            f"Sau khi giác ngộ, sau khi thấu hiểu, Ngài nói ra, thuyết giảng, đề ra, thiết lập, mở bày, phân tích, "
            f"làm cho rõ ràng. Và Ngài nói ‘hãy thấy’ – này các tỳ-khưu, {L_JA}. Này các tỳ-khưu, {L_BH}{PE} "
            f"này các tỳ-khưu, {L_AV}. {UPP}{PE} và Ngài nói ‘hãy thấy’ – này các tỳ-khưu, {L_AV}. "
            f"Như vậy, này các tỳ-khưu, tính đúng như thật, tính không sai lệch, tính không khác đi, {IDAPP} ở đây – "
            f"này các tỳ-khưu, điều này được gọi là {PS}” [{CIT['saṃ. ni.']} 2.20].")
    add("5-450", f"{S.na_vattabbam(a(PS))} {YES} {SUT1} {ATTH} {YES} {S.tena_hi(a(PS))}")
    add("5-451",
        f"Có phải {dt(L_AV)}, {a(NIB)} không? {YES} {Q(n_ask('hai'))} {NO_PE} {q(n_ask('hai'))} {YES} "
        f"{Q(refuges_pe('hai'))} {NO_PE}",
        f"Có phải {dt(L_AV)}, {dt(L_SK)}, {a(NIB)} không? {YES} {Q(n_ask('ba'))} {NO_PE} {Q(n_ask('ba'))} {YES} "
        f"{Q(refuges_pe('ba'))} {NO_PE}",
        f"Có phải {dt(L_AV)}, {dt(L_SK)}{PE} {dt(L_JA)}, {a(NIB)} không? {YES} {Q(n_ask('mười hai'))} {NO_PE} "
        f"{q(n_ask('mười hai'))} {YES} {Q(refuges_pe('mười hai', two=True))} {NO_PE}",
        S.katha_end(KATHA[2]))

    # ---- (55) 3. Saccakathā -----------------------------------------------------------------------------------
    heading("5-14-3-0", 4, VAGGA)
    heading("5-14-3-1-0", 5, f"(55) 3. {S.katha(KATHA[3])}")
    S4 = "bốn sự thật"                                           # cattāri saccāni
    add("5-452",
        f"{Q(a(S4))} {YES} {Q(refuges('bốn'))} {NO_PE} {q(nibb('bốn'))} {YES} {Q(gap('bốn'))} {NO_PE}",
        f"{Q(a(DS))} {YES} {Q(a(DUK))} {NO_PE} {q(a(DS))} {YES} {Q(a(DUK_L))} {NO_PE} "
        f"{q(a(SS))} {YES} {Q(a(SAM))} {NO_PE} {q(a(SS))} {YES} {Q(a(TAN))} {NO_PE} "
        f"{q(a(MS))} {YES} {Q(a(MAG))} {NO_PE} {q(a(MS))} {YES} {Q(a(SAMMA_PE))} {NO_PE}",
        f"{Q(s(DUK))} {YES} {Q(s(DS))} {NO_PE} {q(s(DUK_L))} {YES} {Q(s(DS))} {NO_PE} "
        f"{q(s(SAM))} {YES} {Q(s(SS))} {NO_PE} {q(s(TAN))} {YES} {Q(s(SS))} {NO_PE} "
        f"{q(s(MAG))} {YES} {Q(s(MS))} {NO_PE} {q(s(SAMMA_PE))} {YES} {Q(s(MS))} {NO_PE}")

    def pair(t, x, neg=False):        # T-saccaṃ asaṅkhataṃ, X asaṅkhato / saṅkhato
        return f"{a(t)}, {s(x) if neg else a(x)}"

    NP = pair(NS, NIR)
    add("5-453",
        f"{Q(NP)} {YES} {Q(pair(DS, DUK))} {NO_PE} {q(NP)} {YES} {Q(pair(SS, SAM))} {NO_PE} "
        f"{q(NP)} {YES} {Q(pair(MS, MAG))} {NO_PE}",
        f"{Q(pair(DS, DUK, True))} {YES} {Q(pair(NS, NIR, True))} {NO_PE} "
        f"{q(pair(SS, SAM, True))} {YES} {Q(pair(NS, NIR, True))} {NO_PE} "
        f"{q(pair(MS, MAG, True))} {YES} {Q(pair(NS, NIR, True))} {NO_PE}")
    TAT = "điều này là đúng như thật, điều này là không sai lệch, điều này là không khác đi"
    #   tathametaṃ avitathametaṃ anaññathametaṃ
    T3 = "đúng như thật, không sai lệch, không khác đi"           # tathāni avitathāni anaññathāni
    SUT2 = (f"{S.NANU_VUTTAM} “này các tỳ-khưu, có bốn điều này là {T3}! Bốn điều nào? ‘{cap(SACCA4[0])}’, "
            f"này các tỳ-khưu, {TAT}{PE} ‘{SACCA4[1]}’{PE} ‘{SACCA4[2]}’{PE} ‘{SACCA4[3]}’, {TAT}. "
            f"Này các tỳ-khưu, bốn điều này là {T3}” [{CIT['saṃ. ni.']} 5.1090].")
    add("5-454",
        f"{S.na_vattabbam(a(S4))} {YES} {SUT2} {ATTH} {YES} {S.tena_hi(a(S4))}",
        S.katha_end(KATHA[3]))

    # ---- (56) 4. Āruppakathā ----------------------------------------------------------------------------------
    heading("5-14-4-0", 4, VAGGA)
    heading("5-14-4-1-0", 5, f"(56) 4. {S.katha(KATHA[4])}")
    add("5-455",
        two_block(AK),
        f"{Q(a(AK))} {YES} {Q(f'{AK} là {BHAVO7}')} {YES} {Q(f'{ASKT} là {BHAVO7}')} {NO_PE}",
        f"{Q(f'có nghiệp đi đến {AK}')} {YES} {Q(f'có nghiệp đi đến {ASKT}')} {NO_PE} "
        f"{q(f'có chúng sinh đi đến {AK}')} {YES} {Q(f'có chúng sinh đi đến {ASKT}')} {NO_PE}",
        f"{Q(f'ở {AK}, chúng sinh {BORN}')} {YES} {Q(f'ở {ASKT}, chúng sinh {BORN}')} {NO_PE} "
        f"{q(f'ở {AK} có cảm giác, tri giác, các tạo tác, thức')} {YES} "
        f"{Q(f'ở {ASKT} có cảm giác, tri giác, các tạo tác, thức')} {NO_PE} "
        f"{q(f'{AK} là {CATU}')} {YES} {Q(f'{ASKT} là {CATU}')} {NO_PE}")
    V4 = f"{VR} {ARU} là bất động"                              # cattāro āruppā anejā vuttā bhagavatā
    add("5-456",
        f"{S.na_vattabbam(a(ARU))} {YES} {NANU(V4)} {YES} Nếu {V4}, thì {RE}, chắc chắn nên nói “{a(ARU)}”.",
        S.katha_end(KATHA[4]))

    # ---- (57) 5. Nirodhasamāpattikathā ------------------------------------------------------------------------
    heading("5-14-5-0", 4, VAGGA)
    heading("5-14-5-1-0", 5, f"(57) 5. {S.katha(KATHA[5])}")
    add("5-457",
        two_block(NSAM),
        f"{Q(a(NSAM))} {YES} {Q(okk(f'nhập {NIR}'))} {YES} {Q(okk(f'nhập {ASKT}'))} {NO_PE}")

    def order(x, rise=False):         # X samāpajjantassa / X-ā vuṭṭhahantassa paṭhamaṃ nirujjhati / uppajjati …
        if rise:
            return (f"đối với người đang xuất khỏi {x}, trước tiên {SANKH['c']} sinh khởi, rồi đến {SANKH['k']}, "
                    f"rồi đến {SANKH['v']}")
        return (f"đối với người nhập {x}, trước tiên {SANKH['v']} chấm dứt, rồi đến {SANKH['k']}, "
                f"rồi đến {SANKH['c']}")

    PH3 = "sự tiếp xúc trống rỗng, sự tiếp xúc không có dấu hiệu, sự tiếp xúc không mong cầu"
    #   suññato phasso, animitto phasso, appaṇihito phasso
    VIV = "tâm nghiêng về sự tách biệt, hướng về sự tách biệt, xuôi về sự tách biệt"
    #   vivekaninnaṃ cittaṃ hoti vivekapoṇaṃ vivekapabbhāraṃ
    add("5-458",
        f"{Q(f'sự trong sạch, sự xuất khỏi {NIR} được nhận ra')} {YES} "
        f"{Q(f'sự trong sạch, sự xuất khỏi {ASKT} được nhận ra')} {NO_PE} "
        f"{q(order(NIR))} {YES} {Q(order(ASKT))} {NO_PE} {q(order(NIR, True))} {YES} {Q(order(ASKT, True))} {NO_PE}",
        f"{Q(f'ba sự tiếp xúc chạm đến người đã xuất khỏi {NIR} – {PH3}')} {YES} "
        f"{Q(f'ba sự tiếp xúc chạm đến người đã xuất khỏi {ASKT} – {PH3}')} {NO_PE}",
        f"{Q(f'đối với người đã xuất khỏi {NIR}, {VIV}')} {YES} {Q(f'đối với người đã xuất khỏi {ASKT}, {VIV}')} "
        f"{NO_PE}")
    add("5-459",
        f"{S.na_vattabbam(a(NSAM))} {YES} {Q(SK)} {NO_PE} vậy thì {a(NSAM)}.",
        S.katha_end(KATHA[5]))

    # ---- (58) 6. Ākāsakathā -----------------------------------------------------------------------------------
    heading("5-14-6-0", 4, VAGGA)
    heading("5-14-6-1-0", 5, f"(58) 6. {S.katha(KATHA[6])}")

    def mk(x, y):                     # X-ṃ Y-ṃ karonti
        return f"có ai đó làm cho {x} trở thành {y}"

    def moves(v=""):                  # pakkhino gacchanti … usuṃ khipanti
        return (f"loài chim đi, mặt trăng và mặt trời đi, các vì sao đi, người ta biến hóa thần thông, "
                f"cử động cánh tay, cử động bàn tay, ném cục đất, ném cây chùy, ném thần thông{v}, ném mũi tên")

    add("5-460",
        two_block(AKASA, cap2=True),
        f"{Q(a(AKASA))} {YES} {Q(mk(ANAK, AKASA))} {YES} {Q(mk(SKT, ASKT))} {NO_PE} "
        f"{q(mk(AKASA, ANAK))} {YES} {Q(mk(ASKT, SKT))} {NO_PE}",
        f"{Q(f'trong {AKASA}, ' + moves(S.var('?', 'sattiṃ')))} {YES} {Q(f'trong {ASKT}, ' + moves())} {NO_PE}")
    add("5-461",
        f"{Q(f'sau khi bao quanh {AKASA}, người ta làm nhà, làm kho')} {YES} "
        f"{Q(f'sau khi bao quanh {ASKT}, người ta làm nhà, làm kho')} {NO_PE}",
        f"{Q(f'khi cái giếng đang được đào, {ANAK} trở thành {AKASA}')} {YES} {Q(f'{SKT} trở thành {ASKT}')} {NO_PE}",
        f"{Q(f'khi cái giếng trống đang được lấp đầy, khi cái kho trống đang được lấp đầy, khi cái chum trống đang được lấp đầy, {AKASA} biến mất')} "
        f"{YES} {Q(f'{ASKT} biến mất')} {NO_PE}")
    add("5-462",
        f"{S.na_vattabbam(a(AKASA))} {YES} {Q(s(AKASA))} {NO_PE} vậy thì {a(AKASA)}.",
        S.katha_end(KATHA[6]))

    # ---- (59) 7. Ākāso sanidassanotikathā ---------------------------------------------------------------------
    heading("5-14-7-0", 4, VAGGA)
    heading("5-14-7-1-0", 5, f"(59) 7. {S.katha(KATHA[7])}")
    add("5-463", *visible(1, 2, 3, AKASA, v=S.var("?", "atthi"),
                          cit=f" [{CIT['ma. ni.']} 1.400; 3.421; {CIT['saṃ. ni.']} 4.60]"))
    SEE = "khoảng giữa hai cái cây, khoảng giữa hai cây cột, lỗ khóa, lỗ cửa sổ"
    #   dvinnaṃ rukkhānaṃ antaraṃ, dvinnaṃ thambhānaṃ antaraṃ, tāḷacchiddaṃ vātapānacchiddaṃ
    add("5-464", seen(AKASA, SEE), S.katha_end(KATHA[7]))

    # ---- (60) 8. Pathavīdhātu sanidassanātiādikathā -----------------------------------------------------------
    heading("5-14-8-0", 4, VAGGA)
    heading("5-14-8-1-0", 5, f"(60) 8. {S.katha(KATHA[8])}")
    add("5-465", *visible(1, 2, 3, PD))
    add("5-466",
        seen(PD, "mặt đất, tảng đá, ngọn núi", v=S.var("Sī., Syā., Ka.", "passasi, cũng vậy ở các chỗ sau"), pe=True),
        seen(AP, "nước", pe=True),
        seen(TE, "lửa đang cháy", pe=True),
        seen(VA, "những cái cây đang bị gió lay động", pe=True),
        S.katha_end(KATHA[8]))

    # ---- (61) 9. Cakkhundriyaṃ sanidassanantiādikathā ---------------------------------------------------------
    heading("5-14-9-0", 4, VAGGA)
    heading("5-14-9-1-0", 5, f"(61) 9. {S.katha(KATHA[9])}")
    add("5-467", *visible(1, 2, 3, CI, short=True))
    add("5-468", seen("năm năng lực", "mắt, tai, mũi, lưỡi, thân", pe=True), S.katha_end(KATHA[9]))

    # ---- (62) 10. Kāyakammaṃ sanidassanantikathā --------------------------------------------------------------
    heading("5-14-10-0", 4, VAGGA)
    heading("5-14-10-1-0", 5, f"(62) 10. {S.katha(KATHA[10])}")
    add("5-469", *visible(1, 2, 3, KK))
    add("5-470",
        seen(KK, WALK6),
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
    adh = S.FORMULAS_MD.parent / "adh-14"           # byte-identical copy for termbase_adherence_vi.py
    adh.mkdir(exist_ok=True)
    (adh / NAME).write_text(text, encoding="utf-8", newline="\n")
    print("wrote", adh / NAME)


if __name__ == "__main__":
    main()
