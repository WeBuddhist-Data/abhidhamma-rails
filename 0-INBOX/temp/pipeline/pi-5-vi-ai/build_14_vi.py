# -*- coding: utf-8 -*-
"""pi-5 (Kathāvatthu) Vietnamese zero-shot, chapter 14: 14-chatthavaggo.md (Chaṭṭhavaggo, ^5-14-0 … ^5-470),
the ten kathā (53)-(62) of the sixth vagga (asaṅkhata / sanidassana) and its uddāna.

Imports the approved sample builder (build_sample_vi, read-only) for every debate frame and the finished
chapter builders build_4_vi / build_9_vi / build_12_vi (read-only, importing writes nothing) for the path names,
the vagga close and arahattamagga, so every repeat is byte-identical with those chapters. Every string claimed
from the pi-1..4 Vietnamese rails is asserted to occur there, every string taken from a finished pi-5 chapter
is asserted to occur in that chapter's output; the sample's per-line checks (IDs, dashes, quotes, NFC,
foreign letters) are run against the Pāli. Every Pāli sentence keeps its own sentence.

run:  python -I -B -X utf8 build_14_vi.py
"""
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai")
import build_sample_vi as B  # noqa: E402
import build_4_vi as C4      # noqa: E402  (sotāpatti- / sakadāgāmi- / anāgāmimagga)
import build_9_vi as C9      # noqa: E402  (vagga close: Tassuddānaṃ –)
import build_12_vi as C12    # noqa: E402  (arahattamagga)

NAME = "14-chatthavaggo.md"
Q, q, NANU, AM, cap = B.Q, B.q, B.NANU, B.AMANTA, B.cap
NH, NHP = B.NA_HEVAM, B.NA_HEVAM_PE
NVQ, TENA_HI = B.NA_VATTABBAM_Q, B.TENA_HI
VAR = B.VAR
NUM = B.NUM
VAGGA6 = B.VAGGA[6]                                       # Chaṭṭhavaggo = «Chương thứ sáu» (terms file)
K, E = B.KATHA.format, B.KATHA_END.format

# ================================================================ asaṅkhata frame (pi-1 core, ch10)
ASK = "không do điều kiện tạo thành"                       # asaṅkhata (pi-1 core)
SK = "do điều kiện tạo thành"                              # saṅkhata
ASK_N = f"điều {ASK}"                                     # asaṅkhataṃ (noun; ch10 «điều không do điều kiện tạo thành»)
SK_N = f"điều {SK}"
NIB = "Niết-bàn"


def a(x):
    return f"{x} {ASK}"


def s(x):
    return f"{x} {SK}"


def tena_hi_lc(x):
    """…pe… tena hi Xti. (after …pe…: lowercase)"""
    return f"vậy thì {x}."


REFUGE = f"là {NIB}, nơi che chở, nơi ẩn náu, nơi nương tựa, nơi đến cuối cùng, điều bất biến, điều bất tử"
# nibbānaṃ tāṇaṃ leṇaṃ saraṇaṃ parāyanaṃ accutaṃ amataṃ (ch10 tāṇa … amata)


def n_ask(n):
    """dve / pañca … asaṅkhatāni (bare thesis «có hai X», ch10)"""
    return f"có {n} {ASK_N}"


def refuges(n):
    """dve tāṇāni dve leṇāni … dve nibbānāni (ch10 ^5-353, here unabridged)"""
    return (f"có {n} nơi che chở, {n} nơi ẩn náu, {n} nơi nương tựa, {n} nơi đến cuối cùng, {n} điều bất biến, "
            f"{n} điều bất tử, {n} {NIB}")


def gap(n):
    """atthi dvinnaṃ nibbānānaṃ uccanīcatā … antarikā vā (ch10 ^5-353)"""
    return (f"giữa {n} {NIB} có sự cao thấp, sự thấp kém và ưu việt, sự hơn kém, hoặc ranh giới, hoặc sự phân "
            "chia, hoặc đường vạch, hoặc khoảng cách")


def refuges_pe(n):
    """dve tāṇāni…pe… antarikā vā"""
    return f"có {n} nơi che chở… hoặc khoảng cách"


def two_close(x, first_cap=False):
    """^5-448 pattern after the thesis X: X asaṅkhataṃ, nibbānaṃ asaṅkhatanti? … antarikā vāti?"""
    head = Q if first_cap else q
    return (f"{head(f'{a(x)}, {a(NIB)}')} {AM} {Q(n_ask('hai'))} {NHP} {q(n_ask('hai'))} {AM} "
            f"{Q(refuges_pe('hai'))} {NHP}")


# ================================================================ (53) Niyāma
NY = "sự cố định"                                         # niyāma (terms file heading; okkamati niyāmaṃ pi-2, pi-4)
KX1 = NY                                                  # Niyāmakathā = «Bàn về sự cố định» (terms file)
MG = "con đường"
MG_SO, MG_SA, MG_AN, MG_AR = C4.SOTAPATTIMAGGA, C4.SAKADAGAMIMAGGA, C4.ANAGAMIMAGGA, C12.MG_AR
NY_SO, NY_SA, NY_AN, NY_AR = (m.replace(MG, NY, 1) for m in (MG_SO, MG_SA, MG_AN, MG_AR))
# sotāpatti- / sakadāgāmi- / anāgāmi- / arahattaniyāmo = «sự cố định vào dòng / trở lại một lần / không trở lại /
# A-la-hán» (built from the magga names)
NY_MI = f"{NY} theo hướng sai lầm"                        # micchattaniyāmo (pi-1 micchattaniyatā «cố định theo hướng sai lầm»)
NY_SM = f"{NY} theo hướng đúng đắn"                       # sammattaniyāmo (pi-1)
ANIYATO = "trở thành không cố định"                       # aniyato hoti (pi-1 aniyatā «không cố định»)
VERBS = ("đạt được, làm sinh khởi, làm phát khởi, làm khởi lên, làm dấy lên, làm hình thành, làm hình thành trọn "
         "vẹn, làm sinh ra, làm sinh ra trọn vẹn")
# paṭilabhanti uppādenti samuppādenti uṭṭhāpenti samuṭṭhāpenti nibbattenti abhinibbattenti janenti sañjanenti


def some(first, obj):
    """Atthi keci X okkamanti / samāpajjanti paṭilabhanti … sañjanentīti?"""
    return Q(f"có những người {first}, {VERBS} {obj}")


# ================================================================ (54) Paṭiccasamuppāda
PSU = "sự sinh khởi tùy thuộc vào điều kiện"              # paṭiccasamuppāda (pi-1 core)
KX2 = PSU
PS_A = "vô minh làm điều kiện cho các sự tạo tác"         # avijjāpaccayā saṅkhārā (pi-2 ^2-225, clause)
PS_S = "các sự tạo tác làm điều kiện cho thức"            # saṅkhārapaccayā viññāṇaṃ
PS_B = "sự hiện hữu làm điều kiện cho sự sinh"            # bhavapaccayā jāti
PS_J = "sự sinh làm điều kiện cho sự lão hóa và sự chết"  # jātipaccayā jarāmaraṇaṃ
AVJ = "vô minh"
SUB_A = "các sự tạo tác do vô minh làm điều kiện"         # avijjāpaccayā saṅkhārā (as subject of asaṅkhatā)
SUB_S = "thức do các sự tạo tác làm điều kiện"            # saṅkhārapaccayā viññāṇaṃ (subject)
SUB_N = "phần tinh thần và vật chất do thức làm điều kiện"   # viññāṇapaccayā nāmarūpaṃ (subject; nāmarūpa pi-2)
SUB_J = "sự lão hóa và sự chết do sự sinh làm điều kiện"  # jātipaccayā jarāmaraṇaṃ (subject)
IDAPP = "quy luật tùy thuộc vào điều kiện"                # idappaccayatā (pi-1 ^1-1008)
DT = "sự ổn định của các hiện tượng, tính cố định của các hiện tượng"   # dhammaṭṭhitatā dhammaniyāmatā
NHULAI = "các Như Lai"                                    # tathāgatānaṃ (Như Lai pi-2)
UPPADA = f"Dù {NHULAI} xuất hiện hay {NHULAI} không xuất hiện, yếu tố ấy vẫn đứng vững"
# uppādā vā tathāgatānaṃ anuppādā vā tathāgatānaṃ ṭhitāva sā dhātu
TBH = "này các tỳ-khưu"
SUTTA_PS = (
    f"{B.NANU_VUTTAM} “Này các tỳ-khưu, {PS_J}. {UPPADA}, {DT}, {IDAPP}. Như Lai giác ngộ, thấu hiểu điều ấy. "
    "Sau khi giác ngộ, sau khi thấu hiểu, nói ra, thuyết giảng, công bố, thiết lập, mở bày, phân tích, làm cho rõ "
    f"ràng. Và nói ‘Hãy thấy’ – {TBH}, {PS_J}. Này các tỳ-khưu, {PS_B}… {TBH}, {PS_A}. {UPPADA}… và nói "
    f"‘hãy thấy’ – {TBH}, {PS_A}. Như vậy, {TBH}, điều mà, ở đây, là tính đúng như thật, tính không sai lệch, tính "
    f"không khác đi, {IDAPP} – {TBH}, đó được gọi là {PSU}” [Tương Ưng Bộ Kinh 2.20].")
# abhisambujjhati «giác ngộ» (pi-4), abhisameti «thấu hiểu» (ch10 abhisamaya), deseti «thuyết giảng» (pi-4);
# tathatā avitathatā anaññathatā as the sample's tathavādī avitathavādī anaññathavādī; yā tatra … – ayaṃ vuccati
# as pi-1 «Điều mà, ở đây, là … – đó được gọi là …»


def where(clause):
    """X-ti yā tattha dhammaṭṭhitatā dhammaniyāmatā"""
    return f"trong việc {clause}, {DT} ở đây"


# ================================================================ (55) Sacca
KX3 = "các sự thật"                                       # Saccakathā (sacca «sự thật» core)
CS = "bốn sự thật"                                        # cattāri saccāni
DS, SS, NS_, MS = ("sự thật về khổ đau", "sự thật về sự phát sinh", "sự thật về sự chấm dứt",
                   "sự thật về con đường")                # dukkha- / samudaya- / nirodha- / maggasaccaṃ (ch10)
DK, SAM, NIR = "khổ đau", "sự phát sinh", "sự chấm dứt"   # dukkhaṃ / samudayo / nirodho
KD = ("khổ đau nơi thân, khổ đau trong tâm, sự sầu muộn, sự than khóc, khổ đau, nỗi buồn và sự tuyệt vọng")
# kāyikaṃ dukkhaṃ cetasikaṃ dukkhaṃ sokaparidevadukkhadomanassaupāyāsā: the argument turns on dukkha, so
# «khổ đau» throughout (coordinator rule); pi-1 / pi-2 have «sự khó chịu» for this dukkha (report)
TANHA3 = "khao khát dục lạc, khao khát được hiện hữu, khao khát không còn hiện hữu"   # (pi-2 ^2-203)
SD_PE = f"{B.SAMMA[0]}… {B.SAMMA[-1]}"                     # sammādiṭṭhi…pe… sammāsamādhi (pi-2)
TATHA = "đúng như thật, không sai lệch, không khác đi"     # tathāni avitathāni anaññathāni
THIS = "điều này đúng như thật, điều này không sai lệch, điều này không khác đi"   # tathametaṃ avitathametaṃ …
SUTTA_SC = (
    f"{B.NANU_VUTTAM} “Này các tỳ-khưu, bốn điều này {TATHA}! Bốn điều nào? ‘Đây là khổ đau’, {TBH}, {THIS}… "
    "‘đây là sự phát sinh của khổ đau’… ‘đây là sự chấm dứt khổ đau’… ‘đây là cách thực hành dẫn đến sự chấm dứt "
    f"khổ đau’, {THIS}. Này các tỳ-khưu, bốn điều này {TATHA}” [Tương Ưng Bộ Kinh 5.1090].")
# dukkhasamudayo / dukkhanirodho / dukkhanirodhagāminī paṭipadā (pi-2 ^2-189)

# ================================================================ (56) Āruppa
KX4 = "các trạng thái không hình sắc"                     # Āruppakathā (arūpa «không hình sắc» pi-1, pi-2)
ARU4 = "bốn trạng thái không hình sắc"                    # cattāro āruppā
AKA = "lĩnh vực không gian vô tận"                        # ākāsānañcāyatanaṃ (pi-2, ch10)
BHAVA7 = ("là sự hiện hữu, cõi tái sinh, nơi cư trú của chúng sinh, vòng luân hồi, cách sinh, chỗ trú của thức, "
          "sự có được sự tồn tại cá nhân")
# bhavo gati sattāvāso saṃsāro yoni viññāṇaṭṭhiti attabhāvapaṭilābho (gati «cõi tái sinh» pi-4; attabhāva
# «sự tồn tại cá nhân» pi-1; paṭilābha «sự có được» pi-2)
UPAGA = "đi đến"                                          # -ūpaga (kamma and sattā: one word)
LIFE5 = "chúng sinh sinh ra, già đi, qua đời, chết đi, tái sinh"   # sattā jāyanti jīyanti mīyanti cavanti upapajjanti
FOURK = f"có {B.VEDANA}, {B.SANNA}, {B.SANKHARA}, {B.VINNANA}"   # atthi vedanā saññā saṅkhārā viññāṇaṃ
CATU = "là sự hiện hữu gồm bốn khối"                      # catuvokārabhavo (pi-2)
ANEJA = f"Đức Thế Tôn đã nói rằng {ARU4} là bất động"     # cattāro āruppā anejā vuttā bhagavatā (ch10 frame;
#                                                           āneñja «trạng thái bất động» pi-2)

# ================================================================ (57) Nirodhasamāpatti
NSA = "thành tựu thiền chấm dứt"                          # nirodhasamāpatti (pi-2 «thành tựu thiền chấm dứt tri giác …»)
KX5 = NSA
VS, KS, CSK = "sự tạo tác bằng lời nói", "sự tạo tác bằng thân", "sự tạo tác bằng tâm"   # (pi-2 ^2-226, ch10)
VUT_ING = "đối với người đang xuất khỏi"                  # vuṭṭhahantassa (vuṭṭhāna «sự xuất khỏi» pi-2)
VUT_ED = "người đã xuất khỏi"                             # vuṭṭhitaṃ / vuṭṭhitassa
PH3 = "sự tiếp xúc trống rỗng, sự tiếp xúc không có dấu hiệu, sự tiếp xúc không mong cầu"
# suññato phasso, animitto phasso, appaṇihito phasso (suñña «trống rỗng», animitta «không có dấu hiệu» terms;
# appaṇihita «không mong cầu» pi-1)
VIVEKA = "tâm nghiêng về sự tách biệt, hướng về sự tách biệt, xuôi về sự tách biệt"
# vivekaninnaṃ cittaṃ hoti vivekapoṇaṃ vivekapabbhāraṃ (viveka «sự tách biệt» pi-1)

# ================================================================ (58) Ākāsa
AK = "không gian"                                         # ākāso (pi-1 ākāsadhātu «yếu tố không gian»)
KX6 = AK
ANAK = f"cái không phải {AK}"                             # anākāso (ch10 «cái không phải con đường»)


def space_acts(var=""):
    """pakkhino gacchanti, … iddhiṃ [sattiṃ (?)] khipanti, usuṃ khipanti"""
    return ("các loài chim di chuyển, mặt trăng và mặt trời di chuyển, các vì sao di chuyển, biến hóa thần thông, "
            "cử động cánh tay, cử động bàn tay, ném cục đất, ném cây chùy, "
            f"ném thần thông{var}, ném mũi tên")


def make(x, y):
    """X Y karonti"""
    return f"làm cho {x} trở thành {y}"


# ================================================================ (59)-(62) sanidassana
SAN = "thấy được"                                         # sanidassana (pi-1 «thấy được và có tính va chạm»)
KX7 = f"việc cho rằng {AK} {SAN}"                         # Ākāso sanidassanotikathā
EARTH, WATER, FIRE, WIND = "yếu tố đất", "yếu tố nước", "yếu tố lửa", "yếu tố gió"   # (pi-1, pi-2)
KX8 = f"việc cho rằng {EARTH} {SAN} và các mục khác"      # Pathavīdhātu sanidassanātiādikathā (ādi: terms file)
EYEF = B.INDRIYA[0]                                       # cakkhundriyaṃ = «năng lực mắt»
KX9 = f"việc cho rằng {EYEF} {SAN} và các mục khác"       # Cakkhundriyaṃ sanidassanantiādikathā
KK = "nghiệp bằng thân"                                   # kāyakammaṃ (pi-1 ^1-985)
KX10 = f"việc cho rằng {KK} {SAN}"                        # Kāyakammaṃ sanidassanantikathā
RUPA_EYE = ("là hình sắc, lĩnh vực hình sắc, yếu tố hình sắc, màu xanh, màu vàng, màu đỏ, màu trắng, được nhận "
            "biết bằng mắt, va chạm vào mắt, đi vào tầm của mắt")
# rūpaṃ rūpāyatanaṃ rūpadhātu nīlaṃ … cakkhussa āpāthaṃ āgacchati (pi-1 colours; ch10 «được nhận biết bằng tai,
# va chạm vào tai, đi vào tầm của tai»)
RUPA_EYE_PE = "là hình sắc, lĩnh vực hình sắc, yếu tố hình sắc… đi vào tầm của mắt"
SUTTA_EYE = "tùy thuộc vào mắt và các hình sắc, sinh khởi thức qua mắt"   # cakkhuñca paṭicca rūpe ca … (pi-2)
CITE_EYE = "[Trung Bộ Kinh 1.400; 3.421; Tương Ưng Bộ Kinh 4.60]"
ATTHEVA_IN = "có bài kinh như vậy thật"                   # attheva suttanto (inside a sentence, ch10)


def eye_with(x):
    """cakkhuñca paṭicca X-ñca uppajjati cakkhuviññāṇaṃ"""
    return f"tùy thuộc vào mắt và {x}, sinh khởi thức qua mắt"


def eye_seg(x, var="", cite=""):
    """the three lines X sanidassano … no ca vata re vattabbe – "cakkhuñca paṭicca X-ñca …"nti."""
    th = f"{x} {SAN}"
    first = f"{Q(th)} {AM} {Q(RUPA_EYE if x != EYEF else RUPA_EYE_PE)} {NHP}"
    second = f"{Q(th)} {AM} {Q(eye_with(x))} {NHP}"
    third = (f"{Q(eye_with(x))} {AM} “{cap(eye_with(x))}” – {ATTHEVA_IN}{var} không? Không có. "
             f"“{cap(SUTTA_EYE)}”{cite} – {B.ATTHEVA[0].lower()}{B.ATTHEVA[1:]} {AM} "
             f"Nếu “{SUTTA_EYE}” – {ATTHEVA_IN}, {B.NO_CA_VATA} “{eye_with(x)}”.")
    return first, second, third


def see(what, th, end="."):
    """Nanu passati X-nti? Āmantā. Hañci passati X, tena vata re vattabbe – "Y"ti."""
    return f"{NVQ(th)} {AM} {NANU(f'thấy {what}')} {AM} Nếu thấy {what}, {B.TENA_VATA} “{th}”{end}"


SEE_AK = "khoảng giữa hai cái cây, khoảng giữa hai cây cột, lỗ khóa, lỗ cửa sổ"
# dvinnaṃ rukkhānaṃ antaraṃ, dvinnaṃ thambhānaṃ antaraṃ, tāḷacchiddaṃ vātapānacchiddaṃ
MOVE6 = "người đang đi tới, đang đi lui, đang nhìn thẳng, đang nhìn quanh, đang co lại, đang duỗi ra"
# abhikkamantaṃ paṭikkamantaṃ ālokentaṃ vilokentaṃ samiñjentaṃ pasārentaṃ (pi-2 «khi đi tới, khi đi lui …»)
PASSASI = f" [{VAR} (Sī., Syā., Ka.): passasi, cũng vậy ở các chỗ sau]"   # [passasi (sī. syā. ka.) evamuparipi] (ch2)

# ================================================================ vagga close (ch9 frame)
UDDANA = (f"{cap(a(NY))}, {a(PSU)}, {a(CS)}, {a(ARU4)}, {a(NSA)}, {a(AK)}, {AK} {SAN}, bốn yếu tố cơ bản, "
          f"năm năng lực, {KK} cũng vậy.")
# Niyamo [= niyāmo] asaṅkhato, paṭiccasamuppādo asaṅkhato, cattāri saccāni asaṅkhatāni, cattāro āruppā asaṅkhatā,
# nirodhasamāpatti asaṅkhatā, ākāso asaṅkhato, ākāso sanidassano, cattāro mahābhūtā («bốn yếu tố cơ bản» pi-1),
# pañcindriyāni, tatheva kāyakammanti.


def heads(n, num, title):
    """#### Chaṭṭhavaggo ^5-14-n-0 / ##### (num) n. <title> ^5-14-n-1-0"""
    return [(4, VAGGA6, f"5-14-{n}-0"), (5, f"({num}) {n}. {K(x=title)}", f"5-14-{n}-1-0")]


def build():
    d = B.Doc()
    d.head(3, VAGGA6, "5-14-0")
    # ------------------------------------------------------------ (53) Niyāma
    d.head(4, f"(53) 1. {K(x=KX1)}", "5-14-1-0")
    d.seg("5-445",
          f"{Q(a(NY))} {AM} {Q(REFUGE)} {NHP}",
          f"{Q(f'{a(NY)}, {a(NIB)}')} {AM} {Q(n_ask('hai'))} {NHP}",
          f"{Q(n_ask('hai'))} {AM} {Q(refuges('hai'))} {NHP}",
          f"{Q(f'có hai {NIB}')} {AM} {Q(gap('hai'))} {NHP}",
          f"{Q(a(NY))} {AM} {some('bước vào', NY)} {AM} {some('bước vào', ASK_N)} {NHP}")
    d.seg("5-446",
          f"{Q(a(NY))} {AM} {Q(a(MG))} {NHP}",
          f"{Q(s(MG))} {AM} {Q(s(NY))} {NHP}",
          f"{Q(a(NY_SO))} {AM} {Q(a(MG_SO))} {NHP}",
          f"{Q(s(MG_SO))} {AM} {Q(s(NY_SO))} {NHP}",
          f"Có phải {NY_SA}… {NY_AN}… {a(NY_AR)} không? {AM} {Q(a(MG_AR))} {NHP} {q(s(MG_AR))} {AM} "
          f"{Q(s(NY_AR))} {NHP}",
          f"Có phải {a(NY_SO)}… {a(NY_AR)}, {a(NIB)} không? {AM} {Q(n_ask('năm'))} {NHP} {q(n_ask('năm'))} {AM} "
          f"{Q(refuges_pe('năm'))} {NHP}",
          f"{Q(a(NY))} {AM} {Q(a(NY_MI))} {NHP} {q(s(NY_MI))} {AM} {Q(s(NY_SM))} {NHP}")
    d.seg("5-447",
          f"{NVQ(a(NY))} {AM} {Q(f'khi {NY} đã sinh khởi rồi chấm dứt, thì {ANIYATO}')} {NHP} {TENA_HI(a(NY))} "
          f"{Q(f'khi {NY_MI} đã sinh khởi rồi chấm dứt, thì {ANIYATO}')} {NHP} {tena_hi_lc(a(NY_MI))}",
          E(x=KX1))
    # ------------------------------------------------------------ (54) Paṭiccasamuppāda
    for lv, t, sid in heads(2, 54, KX2):
        d.head(lv, t, sid)
    d.seg("5-448",
          f"{Q(a(PSU))} {AM} {Q(REFUGE)} {NHP} {q(f'{a(PSU)}, {a(NIB)}')} {AM} {Q(n_ask('hai'))} {NHP} "
          f"{q(n_ask('hai'))} {AM} {Q(refuges('hai'))} {NHP} {q(f'có hai {NIB}')} {AM} {Q(gap('hai'))} {NHP}")
    chain449 = []
    for sub in (AVJ, SUB_A, SUB_S, SUB_N, SUB_J):
        chain449.append(f"{q(a(PSU))} {AM} {Q(a(sub))} {NHP} {q(s(sub))} {AM} {Q(s(PSU))} {NHP}")
    l449 = " ".join(chain449)
    l449 = "C" + l449[1:]                                  # first question capitalised
    d.seg("5-449", l449)
    d.seg("5-450",
          f"{NVQ(a(PSU))} {AM} {SUTTA_PS} {B.ATTHEVA} {AM} {TENA_HI(a(PSU))}")
    d.seg("5-451",
          f"{Q(f'{where(PS_A)} {ASK}, {a(NIB)}')} {AM} {Q(n_ask('hai'))} {NHP} {q(n_ask('hai'))} {AM} "
          f"{Q(refuges_pe('hai'))} {NHP}",
          f"{Q(f'{where(PS_A)} {ASK}, {where(PS_S)} {ASK}, {a(NIB)}')} {AM} {Q(n_ask('ba'))} {NHP} "
          f"{Q(n_ask('ba'))} {AM} {Q(refuges_pe('ba'))} {NHP}",
          f"{Q(f'{where(PS_A)} {ASK}, {where(PS_S)} {ASK}… {where(PS_J)} {ASK}, {a(NIB)}')} {AM} "
          f"{Q(n_ask('mười hai'))} {NHP} {q(n_ask('mười hai'))} {AM} "
          f"{Q('có mười hai nơi che chở, mười hai nơi ẩn náu… hoặc khoảng cách')} {NHP}",
          E(x=KX2))
    # ------------------------------------------------------------ (55) Sacca
    for lv, t, sid in heads(3, 55, KX3):
        d.head(lv, t, sid)
    d.seg("5-452",
          f"{Q(a(CS))} {AM} {Q(refuges('bốn'))} {NHP} {q(f'có bốn {NIB}')} {AM} {Q(gap('bốn'))} {NHP}",
          f"{Q(a(DS))} {AM} {Q(a(DK))} {NHP} {q(a(DS))} {AM} {Q(a(KD))} {NHP} {q(a(SS))} {AM} {Q(a(SAM))} "
          f"{NHP} {q(a(SS))} {AM} {Q(a(TANHA3))} {NHP} {q(a(MS))} {AM} {Q(a(MG))} {NHP} {q(a(MS))} {AM} "
          f"{Q(a(SD_PE))} {NHP}",
          f"{Q(s(DK))} {AM} {Q(s(DS))} {NHP} {q(s(KD))} {AM} {Q(s(DS))} {NHP} {q(s(SAM))} {AM} {Q(s(SS))} "
          f"{NHP} {q(s(TANHA3))} {AM} {Q(s(SS))} {NHP} {q(s(MG))} {AM} {Q(s(MS))} {NHP} {q(s(SD_PE))} {AM} "
          f"{Q(s(MS))} {NHP}")
    nn_a = f"{a(NS_)}, {a(NIR)}"                         # nirodhasaccaṃ asaṅkhataṃ, nirodho asaṅkhato
    nn_s = f"{a(NS_)}, {s(NIR)}"                         # nirodhasaccaṃ asaṅkhataṃ, nirodho saṅkhato
    d.seg("5-453",
          f"{Q(nn_a)} {AM} {Q(f'{a(DS)}, {a(DK)}')} {NHP} {q(nn_a)} {AM} {Q(f'{a(SS)}, {a(SAM)}')} {NHP} "
          f"{q(nn_a)} {AM} {Q(f'{a(MS)}, {a(MG)}')} {NHP}",
          f"{Q(f'{a(DS)}, {s(DK)}')} {AM} {Q(nn_s)} {NHP} {q(f'{a(SS)}, {s(SAM)}')} {AM} {Q(nn_s)} {NHP} "
          f"{q(f'{a(MS)}, {s(MG)}')} {AM} {Q(nn_s)} {NHP}")
    d.seg("5-454",
          f"{NVQ(a(CS))} {AM} {SUTTA_SC} {B.ATTHEVA} {AM} {TENA_HI(a(CS))}",
          E(x=KX3))
    # ------------------------------------------------------------ (56) Āruppa
    for lv, t, sid in heads(4, 56, KX4):
        d.head(lv, t, sid)
    in_aka, in_ask = f"trong {AKA}", f"trong {ASK_N}"
    d.seg("5-455",
          f"{Q(a(AKA))} {AM} {Q(REFUGE)} {NHP} {two_close(AKA)}",
          f"{Q(a(AKA))} {AM} {Q(f'{AKA} {BHAVA7}')} {AM} {Q(f'{ASK_N} {BHAVA7}')} {NHP}",
          f"{Q(f'có nghiệp {UPAGA} {AKA}')} {AM} {Q(f'có nghiệp {UPAGA} {ASK_N}')} {NHP} "
          f"{q(f'có chúng sinh {UPAGA} {AKA}')} {AM} {Q(f'có chúng sinh {UPAGA} {ASK_N}')} {NHP}",
          f"{Q(f'{in_aka}, {LIFE5}')} {AM} {Q(f'{in_ask}, {LIFE5}')} {NHP} {q(f'{in_aka} {FOURK}')} {AM} "
          f"{Q(f'{in_ask} {FOURK}')} {NHP} {q(f'{AKA} {CATU}')} {AM} {Q(f'{ASK_N} {CATU}')} {NHP}")
    d.seg("5-456",
          f"{NVQ(a(ARU4))} {AM} {NANU(ANEJA)} {AM} Nếu {ANEJA}, {B.TENA_VATA[:-2]} “{a(ARU4)}”.",
          E(x=KX4))
    # ------------------------------------------------------------ (57) Nirodhasamāpatti
    for lv, t, sid in heads(5, 57, KX5):
        d.head(lv, t, sid)
    d.seg("5-457",
          f"{Q(a(NSA))} {AM} {Q(REFUGE)} {NHP} {two_close(NSA)}",
          f"{Q(a(NSA))} {AM} {some('nhập', 'sự chấm dứt')} {AM} {some('nhập', ASK_N)} {NHP}")

    att_n = "người đang nhập sự chấm dứt"
    att_a = f"người đang nhập {ASK_N}"
    d.seg("5-458",
          f"{Q('từ sự chấm dứt, sự trong sạch, sự xuất khỏi được nhận ra')} {AM} "
          f"{Q(f'từ {ASK_N}, sự trong sạch, sự xuất khỏi được nhận ra')} {NHP} "
          f"{q(f'đối với {att_n}, trước tiên {VS} chấm dứt, sau đó {KS}, sau đó {CSK}')} {AM} "
          f"{Q(f'đối với {att_a}, trước tiên {VS} chấm dứt, sau đó {KS}, sau đó {CSK}')} {NHP} "
          f"{q(f'{VUT_ING} sự chấm dứt, trước tiên {CSK} sinh khởi, sau đó {KS}, sau đó {VS}')} {AM} "
          f"{Q(f'{VUT_ING} {ASK_N}, trước tiên {CSK} sinh khởi, sau đó {KS}, sau đó {VS}')} {NHP}",
          f"{Q(f'ba sự tiếp xúc chạm đến {VUT_ED} sự chấm dứt – {PH3}')} {AM} "
          f"{Q(f'ba sự tiếp xúc chạm đến {VUT_ED} {ASK_N} – {PH3}')} {NHP}",
          f"{Q(f'đối với {VUT_ED} sự chấm dứt, {VIVEKA}')} {AM} {Q(f'đối với {VUT_ED} {ASK_N}, {VIVEKA}')} {NHP}")
    d.seg("5-459",
          f"{NVQ(a(NSA))} {AM} {Q(SK)} {NHP} {tena_hi_lc(a(NSA))}",
          E(x=KX5))
    # ------------------------------------------------------------ (58) Ākāsa
    for lv, t, sid in heads(6, 58, KX6):
        d.head(lv, t, sid)
    d.seg("5-460",
          f"{Q(a(AK))} {AM} {Q(REFUGE)} {NHP} {q(f'{a(AK)}, {a(NIB)}')} {AM} {Q(n_ask('hai'))} {NHP} "
          f"{Q(n_ask('hai'))} {AM} {Q(refuges_pe('hai'))} {NHP}",
          f"{Q(a(AK))} {AM} {Q(f'có những người {make(ANAK, AK)}')} {AM} "
          f"{Q(f'có những người {make(SK_N, ASK_N)}')} {NHP} {q(f'có những người {make(AK, ANAK)}')} {AM} "
          f"{Q(f'có những người {make(ASK_N, SK_N)}')} {NHP}",
          f"{Q(f'trong {AK}, ' + space_acts(f' [{VAR} (?): sattiṃ]'))} {AM} "
          f"{Q(f'trong {ASK_N}, ' + space_acts())} {NHP}")
    d.seg("5-461",
          f"{Q(f'bao quanh {AK} mà làm nhà, làm kho')} {AM} {Q(f'bao quanh {ASK_N} mà làm nhà, làm kho')} {NHP}",
          f"{Q(f'khi giếng đang được đào, {ANAK} trở thành {AK}')} {AM} {Q(f'{SK_N} trở thành {ASK_N}')} {NHP}",
          f"{Q(f'khi giếng trống đang được lấp đầy, khi kho trống đang được lấp đầy, khi chum trống đang được lấp đầy, {AK} biến mất')} "
          f"{AM} {Q(f'{ASK_N} biến mất')} {NHP}")
    d.seg("5-462",
          f"{NVQ(a(AK))} {AM} {Q(s(AK))} {NHP} {tena_hi_lc(a(AK))}",
          E(x=KX6))
    # ------------------------------------------------------------ (59) Ākāso sanidassano
    for lv, t, sid in heads(7, 59, KX7):
        d.head(lv, t, sid)
    d.seg("5-463", *eye_seg(AK, var=f" [{VAR} (?): atthi]", cite=f" {CITE_EYE}"))
    d.seg("5-464",
          see(SEE_AK, f"{AK} {SAN}"),
          E(x=KX7))
    # ------------------------------------------------------------ (60) Pathavīdhātu sanidassanā
    for lv, t, sid in heads(8, 60, KX8):
        d.head(lv, t, sid)
    d.seg("5-465", *eye_seg(EARTH))
    th_e, th_w, th_f, th_a = (f"{x} {SAN}" for x in (EARTH, WATER, FIRE, WIND))
    d.seg("5-466",
          f"{NVQ(th_e)} {AM} {NANU('thấy mặt đất, tảng đá, ngọn núi')} {AM} Nếu thấy{PASSASI} mặt đất, tảng đá, "
          f"ngọn núi, {B.TENA_VATA} “{th_e}”…",
          f"{NVQ(th_w)} {AM} {NANU('thấy nước')} {AM} Nếu thấy nước, {B.TENA_VATA} “{th_w}…",
          f"Có phải không nên nói – {th_f} không? {AM} {NANU('thấy lửa đang cháy')} {AM} Nếu thấy lửa đang cháy, "
          f"{B.TENA_VATA} “{th_f}”…",
          see("những cái cây đang bị gió lay động", th_a, end="…"),
          E(x=KX8))
    # ------------------------------------------------------------ (61) Cakkhundriyaṃ sanidassanaṃ
    for lv, t, sid in heads(9, 61, KX9):
        d.head(lv, t, sid)
    d.seg("5-467", *eye_seg(EYEF))
    d.seg("5-468",
          see("mắt, tai, mũi, lưỡi, thân", f"năm năng lực {SAN}", end="…"),
          E(x=KX9))
    # ------------------------------------------------------------ (62) Kāyakammaṃ sanidassanaṃ
    for lv, t, sid in heads(10, 62, KX10):
        d.head(lv, t, sid)
    d.seg("5-469", *eye_seg(KK))
    d.seg("5-470",
          see(MOVE6, f"{KK} {SAN}"),
          E(x=KX10),
          f"{VAGGA6}.",
          C9.TASSUDDANAM,
          UDDANA)
    return d.text()


# ================================================================ cross-book asserts (pi-1..4 rails)
CROSS = [
    ("không do điều kiện tạo thành", 1), ("do điều kiện tạo thành", 1), ("cố định theo hướng sai lầm", 1),
    ("cố định theo hướng đúng đắn", 1), ("không cố định", 1), ("bước vào sự cố định", 2), ("bước vào sự cố định", 4),
    ("sự sinh khởi tùy thuộc vào điều kiện", 1), (PS_A, 2), (PS_S, 2), (PS_B, 2), (PS_J, 2),
    ("thức làm điều kiện cho phần tinh thần và vật chất", 2), (IDAPP, 1), ("Như Lai", 2), ("tự mình giác ngộ", 4),
    ("việc thuyết giảng Giáo Pháp", 4), ("Điều mà, ở đây, là", 1), ("đó được gọi là", 2), ("vô minh", 1),
    ("sự thật cao quý về sự phát sinh của khổ đau", 2), ("sự thật cao quý về sự chấm dứt khổ đau", 2),
    ("cách thực hành dẫn đến sự chấm dứt khổ đau", 2), ("Đây là", 2),
    ("sự sầu muộn, sự than khóc", 2), ("nỗi buồn và sự tuyệt vọng", 2), ("nơi thân", 1), ("trong tâm", 1),
    (TANHA3, 2), ("quan điểm đúng đắn", 2), ("định tâm đúng đắn", 2),
    ("không hình sắc", 1), (AKA, 2), ("sự hiện hữu", 2), ("chúng sinh", 2),
    ("sự tồn tại cá nhân", 1), ("sự có được", 2), ("tái sinh", 2), ("đang chết đi, đang tái sinh", 2),
    ("sự hiện hữu gồm bốn khối", 2), ("trạng thái bất động", 2),
    ("thành tựu thiền chấm dứt tri giác và cảm giác", 2), ("sự trong sạch, sự xuất khỏi", 2),
    ("sự tạo tác bằng thân, sự tạo tác bằng lời nói, sự tạo tác bằng tâm", 2), ("không mong cầu", 1),
    ("sự tách biệt", 1), ("trống rỗng", 1), ("không có dấu hiệu", 1),
    ("yếu tố không gian", 1), ("cục đất", 2), ("cái chum", 4), ("thần thông", 1),
    ("thấy được và có tính va chạm", 1), ("màu xanh, màu vàng, màu đỏ, màu trắng", 1),
    ("Tùy thuộc vào mắt và các hình sắc, sinh khởi", 2), ("thức qua mắt", 2),
    ("yếu tố đất, yếu tố nước, yếu tố lửa, yếu tố gió", 2), ("bốn yếu tố cơ bản", 1),
    ("nghiệp bằng thân", 1), ("khi đi tới, khi đi lui", 2), ("khi nhìn thẳng, khi nhìn quanh", 2),
    ("Trung Bộ Kinh", 4), ("năng lực mắt", 2),
]
# ================================================================ finished pi-5 chapters (zero-shot outputs)
PI5 = [
    ("có hai nơi che chở… hai nơi ẩn náu… hai nơi nương tựa… hai nơi đến cuối cùng… hai điều bất biến… hai điều "
     "bất tử… hai Niết-bàn", "10-dutiyavaggo.md"),
    (f"Có phải có hai {NIB} không? Đúng vậy. Có phải {gap('hai')} không? Không nên nói như vậy…", "10-dutiyavaggo.md"),
    (DS, "10-dutiyavaggo.md"), (SS, "10-dutiyavaggo.md"), (NS_, "10-dutiyavaggo.md"), (MS, "10-dutiyavaggo.md"),
    ("được nhận biết bằng tai, va chạm vào tai, đi vào tầm của tai", "10-dutiyavaggo.md"),
    ("cái không phải con đường", "10-dutiyavaggo.md"), ("điều không do điều kiện tạo thành", "10-dutiyavaggo.md"),
    ("lĩnh vực không gian vô tận", "10-dutiyavaggo.md"), (VS, "10-dutiyavaggo.md"),
    ("Đức Thế Tôn đã nói rằng", "10-dutiyavaggo.md"),
    ("Không có.", "12-catutthavaggo.md"), (MG_AR, "12-catutthavaggo.md"), ("bước vào sự cố định", "12-catutthavaggo.md"),
    (MG_SO, "4-jahatikatha.md"), (MG_SA, "4-jahatikatha.md"), (MG_AN, "4-jahatikatha.md"),
    ("Tóm tắt của chương này –", "9-hevatthikatha.md"), ("cũng vậy ở các chỗ sau", "2-parihanikatha.md"),
    ("Tương Ưng Bộ Kinh", "5-sabbamatthitikatha.md"), ("thấu hiểu", "10-dutiyavaggo.md"),
    ("[dị bản (?): ", "10-dutiyavaggo.md"),
    ("cõi tái sinh", "1-puggalakatha.md"), ("được nhận ra", "1-puggalakatha.md"),
]


def check_cross():
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(dd.glob("*.md")))
             for b, dd in B.RAILS_DIR.items()}
    missing = [(st, f"pi-{b}") for st, b in CROSS if st not in texts[b]]
    missing += [(st, f) for st, f in PI5 if st not in (B.OUT_DIR / f).read_text(encoding="utf-8")]
    for st, w in missing:
        print(f"CROSS MISSING in {w}: {st}")
    assert not missing, f"{len(missing)} cross strings not found"
    print(f"ch14 cross asserts: {len(CROSS)} pi-1..4 strings, {len(PI5)} pi-5 chapter strings found")


def main():
    B.check_cross_book()
    check_cross()
    text = unicodedata.normalize("NFC", build())
    pali = (B.PALI_DIR / NAME).read_text(encoding="utf-8")
    probs, repaired = B.check_lines(pali, text, NAME)
    for p in probs:
        print("PROBLEM", p)
    assert not probs, f"{len(probs)} line problems"
    assert "\r" not in text and "\n\n\n" not in text and "—" not in text and "chánh niệm" not in text
    with open(B.OUT_DIR / NAME, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(f"wrote {NAME}: {len([ln for ln in text.splitlines() if ln.strip()])} lines; "
          f"odd closing order repaired: {len(repaired)}; line checks: OK")


if __name__ == "__main__":
    main()
