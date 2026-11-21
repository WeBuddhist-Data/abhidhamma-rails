"""pi-5 Kathāvatthu, Vietnamese RAILS (plain audience): chapter 10 (10-dutiyavaggo.md, ^5-10-0 … ^5-353).

Builds AI_translation/vietnamese/pi-5-vietnamese-plain-rails_split_chapters/10-dutiyavaggo.md from fixed strings.
Imports the approved sample builder READ-ONLY (frames, constants, per-line checks) and the finished chapter-2 and
chapter-3 builders READ-ONLY (their fixed strings for identical Pāli; importing writes nothing). Every string marked
(pi-1) … (pi-4) is asserted to occur in that book's approved Vietnamese rails; ch2 / ch3 strings are asserted in the
finished chapter files. New recurring strings: notes-rails-10.md.

usage: python -I -X utf8 -B build_rails_10_vi.py            (build + checks + adherence copy rails/adh-10/)
       python -I -X utf8 -B build_rails_10_vi.py --lookup   (termbase entries for this chapter's keywords)
"""
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai\rails")
import build_rails_sample_vi as S  # noqa: E402
import build_rails_2_vi as C2  # noqa: E402
import build_rails_3_vi as C3  # noqa: E402

TB = S.ROOT / "AI_translation/vietnamese/pi-5-pali-vietnamese-termbase-plain.md"
KW = S.ROOT / "AI_translation/pali/pi-5-keywords-by-reference-pali-plain.md"
NAME = "10-dutiyavaggo.md"
CH9 = "9-hevatthikatha.md"

YES, NO, NO_PE, PE = S.YES, S.NO, S.NO_PE, S.PE
Q, q, cap, NANU = S.Q, S.q, S.cap, S.NANU
hanci, hanci_neg, neu = S.hanci, S.hanci_neg, S.neu
NANU_VUTTAM, ATTHEVA = S.NANU_VUTTAM, S.ATTHEVA
tena_hi, tena_hi_na, na_vattabbam = S.tena_hi, S.tena_hi_na, S.na_vattabbam
var, var_sp, CIT = S.var, S.var_sp, S.CIT
katha, katha_end = S.katha, S.katha_end

# ---------------------------------------------------------------------------------------------------------------
# Strings reused from the finished chapters 2 and 3 (identical Pāli; asserted in their chapter files)
# ---------------------------------------------------------------------------------------------------------------
RAGA, DOSA, MOHA, ANOT = C2.RAGA, C2.DOSA, C2.MOHA, C2.ANOT
AR_KIL = C2.AR_KIL                                   # doso … anottappaṃ (pi-1 names)
PAHINA, MAGGA, BOJJ, BHAV = C2.PAHINA, C2.MAGGA, C2.BOJJ, C2.BHAV
UCCH = C2.UCCH                                       # ucchinnamūlo tālāvatthukato anabhāvaṅkato āyatiṃ anuppādadhammo
EPI, EPI3, FOUR, TASKS, LAST = C2.EPI, C2.EPI3, C2.FOUR, C2.TASKS, C2.LAST
KAMA7 = C2.KAMA7                                     # rāgo kāmarāgo … kāmacchandanīvaraṇaṃ
ab_list, pahana = C2.ab_list, C2.pahana
EPI_L, TASKS_L = EPI.split(", "), TASKS.split(", ")
assert len(EPI_L) == 17 and len(TASKS_L) == 5
RATANA, DHP = C3.RATANA, C3.DHP                      # Sahāvassa … (verse), Anupubbena medhāvī … (verse)
DC_BODY = C3.DHAMMACAKKHU.split(" [trong")[0]       # yasmiṃ, bhikkhave, samaye … sīlabbataparāmāso"
P_SOTA, P_SAKA, P_ANAG, P_ARA = C3.P_SOTA, C3.P_SAKA, C3.P_ANAG, C3.P_ARA
TAD, DASS, kim = C3.TAD, C3.DASS, C3.kim
SAKKAYA, VICI, SILAB = C3.SAKKAYA, C3.VICI, C3.SILAB
SATTAKKHATTU, KOLANKOLO, EKABIJI = C3.SATTAKKHATTU, C3.KOLANKOLO, C3.EKABIJI
ANTARA, UPAHACCA, ASANKHARA, SASANKHARA, UDDHAMSOTO = (C3.ANTARA, C3.UPAHACCA, C3.ASANKHARA, C3.SASANKHARA,
                                                        C3.UDDHAMSOTO)
RUPARAGA, AK_G, ARIYAKANTA, BP, ODARIKA = C3.RUPARAGA, C3.AK_G, C3.ARIYAKANTA, C3.BP, C3.ODARIKA
CH2_STR = [KAMA7, UCCH, EPI, FOUR, TASKS]
CH3_STR = RATANA[:5] + DHP + [DC_BODY, P_SOTA, P_SAKA, P_ANAG, P_ARA, TAD, AK_G]

# ---------------------------------------------------------------------------------------------------------------
# Strings taken unchanged from the approved pi-1 … pi-4 Vietnamese rails (asserted at build time)
# ---------------------------------------------------------------------------------------------------------------
PUTH = "người phàm phu"                                                                            # (pi-1)
AVIJ_PI1 = "vô minh, dòng lũ vô minh, ách vô minh, khuynh hướng tiềm ẩn vô minh, sự ám ảnh của vô minh"  # (pi-1)
IDAPP = "quy luật tùy thuộc vào điều kiện và các hiện tượng sinh khởi tùy thuộc vào điều kiện"      # (pi-1)
EIGHT = ["Bậc Đạo Sư", "Giáo Pháp", "Tăng đoàn", "sự tu học", "quá khứ", "tương lai", "quá khứ và tương lai",
         IDAPP]                                                                                    # (pi-1 ^1-1008)
SOKA5 = "sự sầu muộn, sự than khóc, sự khó chịu, nỗi buồn và sự tuyệt vọng"                        # (pi-1)
JATI8 = "sự sinh, sự lão hóa, sự chết, " + SOKA5                                                  # (ch4)
ASITA = "đã ăn, đã uống, đã nhai, đã nếm"                                                          # (pi-2)
CPS = "y phục, đồ ăn khất thực, chỗ ở, thuốc men và vật dụng chữa bệnh"                            # (pi-2)
GOLD = "vàng và bạc"                                                                               # jātarūparajata (pi-1)
PANDAKA = "người ái nam ái nữ"                                                                     # (pi-2)
SUKHA3 = "dễ chịu, hoặc khó chịu, hoặc không khó chịu cũng không dễ chịu"                          # (pi-2)
DUKKHA_CH = "cách thực hành dẫn đến sự chấm dứt khổ đau"                                          # (pi-1)
ASAVAKHAYA = "sự diệt tận các ô nhiễm"                                                             # (pi-1)
BRAHMALOKA = "cõi Phạm Thiên"                                                                      # (pi-1)
J1, J2, J3, J4 = ("tầng thiền thứ nhất", "tầng thiền thứ hai", "tầng thiền thứ ba", "tầng thiền thứ tư")  # (pi-1)
KASINA = ["đề mục bao trùm là đất", "đề mục bao trùm là nước", "đề mục bao trùm là lửa", "đề mục bao trùm là gió",
          "đề mục bao trùm màu xanh", "đề mục bao trùm màu vàng", "đề mục bao trùm màu đỏ",
          "đề mục bao trùm màu trắng"]                                                             # (pi-1)
AKASA, VINNANAÑCA, AKINCA, NEVASA = ("lĩnh vực không gian vô tận", "lĩnh vực thức vô tận", "lĩnh vực không có gì cả",
                                     "lĩnh vực không phải tri giác cũng không phải không tri giác")  # (pi-2)
DEVAS = ["Tứ Đại Thiên Vương", "Ba Mươi Ba", "Dạ Ma", "Đâu Suất", "Hóa Lạc", "Tha Hóa Tự Tại", "Phạm Chúng",
         "Phạm Phụ", "Đại Phạm", "Thiểu Quang", "Vô Lượng Quang", "Quang Âm", "Thiểu Tịnh", "Vô Lượng Tịnh",
         "Biến Tịnh", "Quảng Quả", "Vô Phiền", "Vô Nhiệt", "Thiện Hiện", "Thiện Kiến", "Sắc Cứu Cánh"]  # (pi-2)
AKASA_DEVA = f"chư thiên sinh vào {AKASA}"                                                         # (pi-2)
THIRD_KAPPA, HALF_KAPPA = "một phần ba của kiếp", "nửa kiếp"                                       # (pi-2)
DN = "Trường Bộ Kinh"                                                                              # dī. ni. (pi-2)
WALK = ["đi tới", "đi lui", "nhìn thẳng", "nhìn quanh"]                                            # (pi-2)
REUSED = ([(PUTH, "1"), (AVIJ_PI1, "1"), (IDAPP, "1"), (SOKA5, "1"), ("sự sinh, sự lão hóa", "1"), (ASITA, "2"),
           (CPS, "2"),
           (GOLD, "1"), (PANDAKA, "2"), (SUKHA3, "2"), (DUKKHA_CH, "1"), (ASAVAKHAYA, "1"), (BRAHMALOKA, "1"),
           (J1, "1"), (J2, "1"), (J3, "1"), (J4, "1"), (AKASA, "2"), (VINNANAÑCA, "2"), (AKINCA, "2"), (NEVASA, "2"),
           (AKASA_DEVA, "2"), (THIRD_KAPPA, "2"), (HALF_KAPPA, "2"), (DN, "2")]
          + [(f"về {x}", "1") for x in EIGHT] + [(f"với {k}", "1") for k in KASINA]
          + [(f"chư thiên {d}", "2") for d in DEVAS] + [(w, "2") for w in WALK])

# ---------------------------------------------------------------------------------------------------------------
# Headings and kathā names (termbase headwords; notes-rails-10.md)
# ---------------------------------------------------------------------------------------------------------------
VAGGA = S.vaggo(2)                                   # Dutiyavaggo = Chương thứ hai
N_PARU = "việc người khác đưa đến"                   # Parūpahāra (upahāra «việc … đưa đến», para «người khác»)
N_ANNA = "sự không biết"                             # Aññāṇa
N_KANKHA = "sự nghi ngờ"                             # Kaṅkhā
N_PARAV = "việc được người khác giảng giải"          # Paravitāraṇa (vitāraṇa «việc được … giảng giải»)
N_VACI = "sự phát ra lời nói"                        # Vacībheda
N_DUKKHA = "việc nêu lên khổ đau"                    # Dukkhāhāra (āhāra «việc nêu lên»)
N_CITTA = "sự duy trì của tâm"                       # Cittaṭṭhiti
N_KUKKU = "tro nóng"                                 # Kukkuḷa
N_ANUP = "sự thấu hiểu tuần tự"                      # Anupubbābhisamaya
N_VOHARA = "lời nói"                                 # Vohāra
N_NIRODHA = "sự chấm dứt"                            # Nirodha (termbase Nirodhakathā «Bàn về sự chấm dứt»)
TASSUDDANAM = "Tóm tắt của chương này –"             # Tassuddānaṃ – (APPROVED; ch9 string used if ch9 is finished)
UDDANA = [f"{cap(N_PARU)}, {N_ANNA}, {N_KANKHA}, {N_PARAV};",
          f"{cap(N_VACI)}, {N_DUKKHA}, {N_CITTA} và {N_KUKKU};",
          f"{cap(N_ANUP)}, {N_VOHARA} và {N_NIRODHA}."]

# ---------------------------------------------------------------------------------------------------------------
# Core words of this chapter
# ---------------------------------------------------------------------------------------------------------------
AR = S.PN["arahā"]                                   # bậc A-la-hán (pi-4)
TASSA = "người ấy"                                   # tassa (person)
ASUCI = "sự xuất tinh bất tịnh"                      # asuci sukkavissaṭṭhi (termbase)
VIMATI = "sự phân vân"                               # vimati (termbase; pi-1)
AVIJ7 = f"{AVIJ_PI1}, xiềng xích vô minh, chướng ngại vô minh"
#   avijjā avijjogho avijjāyogo avijjānusayo avijjāpariyuṭṭhānaṃ avijjāsaṃyojanaṃ avijjānīvaraṇaṃ
VIC4 = "sự hoài nghi, sự ám ảnh của hoài nghi, xiềng xích hoài nghi, chướng ngại hoài nghi"
#   vicikicchā vicikicchāpariyuṭṭhānaṃ vicikicchāsaṃyojanaṃ vicikicchānīvaraṇaṃ
KAMA7_PE = "sự tham đắm, sự tham đắm dục lạc, sự ám ảnh của tham đắm dục lạc" + PE + " chướng ngại ý muốn dục lạc"
SAD = f"{AR} thông thạo các hiện tượng của mình"      # sadhammakusala arahā (termbase)
PAR = f"{AR} thông thạo các hiện tượng của người khác"   # paradhammakusala arahā (para «người khác»)
FRUITS4 = "thành quả vào dòng, hoặc thành quả trở lại một lần, hoặc thành quả không trở lại, hoặc trạng thái A-la-hán"
#   sotāpattiphalaṃ vā sakadāgāmiphalaṃ vā anāgāmiphalaṃ vā arahattaṃ vā
NAMES3 = ["tên và họ của người nữ và người nam", "đường đúng và đường sai", f"tên của {S.TINA}"]
#   itthipurisānaṃ nāmagottaṃ, maggāmaggaṃ, tiṇakaṭṭhavanappatīnaṃ nāmaṃ


def has(who, x, neg=False):          # atthi / natthi <who-gen> X
    return f"{who} {'không có' if neg else 'có'} {x}"


def eight(x, mode="full"):           # satthari X, dhamme X … idappaccayatāpaṭiccasamuppannesu dhammesu X
    items = [f"{x} về {y}" for y in EIGHT]
    if mode == "full":
        return ", ".join(items)
    if mode == "pe1":                # satthari X…pe… last
        return f"{items[0]}{PE} {items[-1]}"
    if mode == "pe2":                # satthari X, dhamme X…pe… last
        return f"{items[0]}, {items[1]}{PE} {items[-1]}"
    if mode == "pe3":                # satthari X, dhamme X, saṅghe X…pe… last
        return f"{items[0]}, {items[1]}, {items[2]}{PE} {items[-1]}"
    raise ValueError(mode)


def pah_groups(who, groups):        # who-ssa X-ppahānāya Y bhāvito…pe… (several groups joined by …)
    out = []
    for xs, ys in groups:
        out.append(f"{PE} ".join(f"để dứt bỏ {x}" for x in xs) + ", " + f"{PE} ".join(f"đã tu tập {y}" for y in ys))
    return f"{who}, " + f"{PE} ".join(out)


def epi_last(who, extra=""):        # who vītarāgo vītadoso vītamoho (katakaraṇīyo)…pe… sacchikātabbaṃ sacchikataṃ
    return f"{who} {EPI3}{extra}{PE} {LAST}"


def nanu_full(who):                 # Nanu arahā vītarāgo … sacchikātabbaṃ sacchikatanti?
    return f"{who} {EPI}, {FOUR}, {TASKS}"


# ---------------------------------------------------------------------------------------------------------------
# The four parallel kathās on the arahant (asuci / aññāṇa / kaṅkhā / paravitāraṇā): shared line builders
# ---------------------------------------------------------------------------------------------------------------
def nanu_raga(T):                   # T? Āmantā. Nanu arahato rāgo pahīno … ? Āmantā. Hañci …, no ca vata re …
    P = f"{RAGA} của {AR} {PAHINA}, {UCCH}"
    return f"{Q(T)} {YES} {NANU(P)} {YES} {hanci_neg(P, T)}"


def nanu_kil(T, items):             # … Nanu arahato doso pahīno…pe… anottappaṃ pahīnaṃ ucchinnamūlaṃ …
    P = ab_list(items, AR) + ", " + UCCH
    return f"{Q(T)} {YES} {NANU(P)} {YES} {hanci_neg(f'{ANOT} của {AR} {PAHINA}, {UCCH}', T)}"


def nanu_pah(T, groups, last_x):    # … Nanu arahato X-ppahānāya … bhāvitāti? … Hañci arahato last_x-ppahānāya bojjhaṅgā …
    return (f"{Q(T)} {YES} {NANU(pah_groups(AR, groups))} {YES} "
            f"{hanci_neg(pahana(AR, last_x, [BOJJ]), T)}")


def sad_open(X):                    # Atthi arahato X? Sadhammakusalassa … atthi X, paradhammakusalassa … natthi X. …
    return (f"{Q(has(AR, X))} {cap(has(SAD, X))}, {has(PAR, X, True)}. {Q(has(SAD, X))} {YES} "
            f"{Q(has(PAR, X))} {NO_PE}")


def sad_l2(X):
    return f"{Q(has(PAR, X, True))} {YES} {Q(has(SAD, X, True))} {NO_PE}"


def pair(a, b, X, neg, end=NO_PE):  # a …, atthi tassa X? Āmantā. b …, atthi tassa X? Na hevaṃ vattabbe…pe….
    t = has(TASSA, X, neg)
    return f"{Q(f'{a}, {t}')} {YES} {Q(f'{b}, {t}')} {end}"


def raga1(who):
    return ab_list([RAGA], who)


def kil3(who, first=None):          # who-ssa doso pahīno…pe… moho pahīno…pe… anottappaṃ pahīnaṃ
    return ab_list(first or [DOSA, MOHA, ANOT], who)


def anot1(who):
    return ab_list([ANOT], who)


G_RAGA = ([RAGA], [MAGGA, BOJJ])
G_DMA = ([DOSA, MOHA, ANOT], [MAGGA, BOJJ])


# ---------------------------------------------------------------------------------------------------------------
# Suttas of the four kathās
# ---------------------------------------------------------------------------------------------------------------
JAN_HEAD = ("Này các tỳ-khưu, Ta nói rằng sự diệt tận các ô nhiễm là dành cho người biết{v}, cho người thấy, không "
            "phải cho người không biết, không phải cho người không thấy")
#   jānatohaṃ, bhikkhave, passato āsavānaṃ khayaṃ vadāmi, no ajānato no apassato
JAN_V = var_sp("Sī.", "jānatāhaṃ").replace("]", "; (Syā., Pī., Ka.): jānatvāhaṃ]")
JAN_Q = (f"Và này các tỳ-khưu, đối với người biết điều gì, người thấy điều gì, thì có {ASAVAKHAYA}?")
#   Kiñca, bhikkhave, jānato kiṃ passato āsavānaṃ khayo hoti?
JP = f"đối với người biết, người thấy, thì có {ASAVAKHAYA}"            # jānato passato āsavānaṃ khayo hoti
EVAM = f"này các tỳ-khưu, đối với người biết như vậy, người thấy như vậy, thì có {ASAVAKHAYA}"
#   evaṃ kho, bhikkhave, jānato evaṃ passato āsavānaṃ khayo hoti
ITI = ["vật chất là như vậy", "sự phát sinh của vật chất là như vậy", "sự biến mất của vật chất là như vậy",
       "cảm giác là như vậy", "tri giác là như vậy", "các tạo tác là như vậy", "thức là như vậy",
       "sự phát sinh của thức là như vậy", "sự biến mất của thức là như vậy"]
#   iti rūpaṃ, iti rūpassa samudayo, iti rūpassa atthaṅgamo, iti vedanā … iti viññāṇassa atthaṅgamo
SACCA4 = ["đây là khổ đau", "đây là sự phát sinh của khổ đau", "đây là sự chấm dứt khổ đau", f"đây là {DUKKHA_CH}"]
#   idaṃ dukkhaṃ / ayaṃ dukkhasamudayo / ayaṃ dukkhanirodho / ayaṃ dukkhanirodhagāminī paṭipadā
SABBA_N = ("Này các tỳ-khưu, người không hiểu biết trực tiếp, không hiểu biết trọn vẹn, không làm phai nhạt, "
           "không dứt bỏ tất cả, thì không có khả năng đi đến sự diệt tận khổ đau")
SABBA_P = ("và này các tỳ-khưu, người hiểu biết trực tiếp, hiểu biết trọn vẹn, làm phai nhạt, dứt bỏ tất cả, "
           "thì có khả năng đi đến sự diệt tận khổ đau")
#   sabbaṃ, bhikkhave, anabhijānaṃ aparijānaṃ avirājayaṃ appajahaṃ abhabbo dukkhakkhayāya, sabbañca kho … bhabbo …


def jan_sutta1(bang, v="", cit=""):  # jānatohaṃ … ‘Iti rūpaṃ … atthaṅgamo’ti – evaṃ kho …
    return (f"“{JAN_HEAD.format(v=v)}{bang} {JAN_Q} ‘{cap(', '.join(ITI[:3]))}, {ITI[3]}{PE} {ITI[4]}{PE} "
            f"{ITI[5]}{PE} {', '.join(ITI[6:])}’ – {EVAM}”{cit}.")


def jan_sutta1_short():             # … ‘Iti rūpaṃ’…pe… ‘iti viññāṇassa atthaṅgamo’ti – evaṃ kho …
    return (f"“{JAN_HEAD.format(v='')}! {JAN_Q} ‘{cap(ITI[0])}’{PE} ‘{ITI[-1]}’ – {EVAM}”.")


def jan_sutta2(cit=""):             # … ‘Idaṃ dukkha’nti – bhikkhave, jānato passato … Evaṃ kho …
    return (f"“{JAN_HEAD.format(v='')}. {JAN_Q} ‘{cap(SACCA4[0])}’ – này các tỳ-khưu, {JP}, ‘{SACCA4[1]}’ – {JP}, "
            f"‘{SACCA4[2]}’ – {JP}, ‘{SACCA4[3]}’ – {JP}. {cap(EVAM)}”{cit}.")


def jan_sutta2_k():                 # kaṅkhā: … ‘Idaṃ dukkha’nti, bhikkhave…pe… ‘…paṭipadā’ti jānato passato …
    return (f"“{JAN_HEAD.format(v='')}! {JAN_Q} ‘{cap(SACCA4[0])}’, này các tỳ-khưu{PE} ‘{SACCA4[3]}’, {JP}. "
            f"{cap(EVAM)}”.")


def jan_sutta2_p():                 # paravitāraṇā: … ‘ayaṃ dukkhasamudayo’ti…pe… ‘ayaṃ dukkhanirodho’ti…pe… …
    return (f"“{JAN_HEAD.format(v='')}! {JAN_Q} ‘{cap(SACCA4[0])}’ – này các tỳ-khưu, {JP}, ‘{SACCA4[1]}’{PE} "
            f"‘{SACCA4[2]}’{PE} ‘{SACCA4[3]}’ – {JP}. {cap(EVAM)}”.")


def sabba(sep, cit=""):
    return f"“{SABBA_N}{sep} {SABBA_P}”{cit}!"


RATANA_LAST = "Không có khả năng làm sáu trọng tội”."                # Chaccābhiṭhānāni abhabba kātu"nti.
RATANA6 = RATANA[:5] + [RATANA_LAST]
RATANA_SHORT = f"“{RATANA[0][1].lower()}{RATANA[0][2:-1]}{PE} {RATANA_LAST[0].lower()}{RATANA_LAST[1:-2]}”."
#   "sahāvassa dassanasampadāya …pe… chaccābhiṭhānāni abhabba kātu"nti.


def dc(end):                        # yasmiṃ, bhikkhave, samaye … sīlabbataparāmāso"ti. / !
    return f"{DC_BODY}{end}"


def nanu_sutta(T, body):            # T? Āmantā. Nanu vuttaṃ bhagavatā – "…". Attheva suttantoti? Āmantā. Tena hi …
    return f"{Q(T)} {YES} {NANU_VUTTAM} {body} {ATTHEVA} {YES} {tena_hi_na(T)}"


def names_line(T, verb_pos, verb_q):
    """Na vattabbaṃ – "T"ti? Āmantā. Nanu arahā … na jāneyya / kaṅkheyya …? Āmantā. Hañci …, tena vata re …"""
    P = verb_pos
    return f"{na_vattabbam(T)} {YES} {NANU(P)} {YES} {hanci(P, T)}", verb_q


# ---------------------------------------------------------------------------------------------------------------
# The chapter
# ---------------------------------------------------------------------------------------------------------------
def build_ch10(tassuddanam):
    segs = []

    def add(i, *lines):
        lines = list(lines)
        lines[-1] = lines[-1] + f" ^{i}"
        segs.append(lines)

    def head(i, level, text):
        add(i, "#" * level + " " + text)

    head("5-10-0", 3, VAGGA)

    # ==== (10) 1. Parūpahārakathā ==================================================================================
    head("5-10-1-0", 4, f"(10) 1. {katha(N_PARU)}")
    T = has(AR, ASUCI)                                      # atthi arahato asuci sukkavissaṭṭhi
    TP, TA = has(PUTH, ASUCI), T
    MARA = "các vị thiên thuộc nhóm Ma vương"               # mārakāyikā devatā (termbase)
    MDU = f"{MARA} đưa {ASUCI} đến {AR}"                    # mārakāyikā devatā arahato asuciṃ sukkavissaṭṭhiṃ upasaṃharanti
    add("5-307",
        f"{Q(T)} {YES} {Q(has(AR, KAMA7))} {NO_PE}",
        f"{Q(has(AR, KAMA7, True))} {YES} {hanci_neg(has(AR, KAMA7, True), T)}",
        f"{Q(f'{TP}, {has(TASSA, KAMA7)}')} {YES} {Q(f'{TA}, {has(TASSA, KAMA7_PE)}')} {NO_PE}",
        f"{Q(f'{TA}, {has(TASSA, KAMA7_PE, True)}')} {YES} {Q(f'{TP}, {has(TASSA, KAMA7_PE, True)}')} {NO_PE}",
        f"{Q(T)} {YES} Theo nghĩa nào? Bởi vì {MDU}.",
        f"{Q(MDU)} {YES} {Q(has(MARA, ASUCI))} {NO_PE}",
        f"{Q(has(MARA, ASUCI, True))} {YES} {hanci_neg(has(MARA, ASUCI, True), MDU)}",
        f"{Q(MDU)} {YES} Có phải {MARA} đưa {ASUCI} của chính mình đến, đưa {ASUCI} của người khác đến, đưa "
        f"{ASUCI} của {TASSA} đến không? {NO_PE}",
        f"{Q(f'{MARA} không đưa {ASUCI} của chính mình, cũng không của người khác, cũng không của {TASSA} đến')} {YES} "
        f"{hanci_neg(f'{MARA} không đưa {ASUCI} của chính mình, cũng không của người khác, cũng không của {TASSA} đến', MDU)}",
        f"{Q(MDU)} {YES} {Q('đưa đến qua các lỗ chân lông')} {NO_PE}")

    VIM_PE = eight(VIMATI, "pe1")
    add("5-308",
        f"{Q(MDU)} {YES} Vì lý do gì? Bởi vì chúng tôi sẽ khiến vị ấy rơi vào {VIMATI}. {Q(has(AR, VIMATI))} {NO_PE}",
        f"{Q(has(AR, VIMATI))} {YES} {Q(has(AR, eight(VIMATI)))} {NO_PE}",
        f"{Q(has(AR, eight(VIMATI), True))} {YES} {hanci_neg(has(AR, VIM_PE, True), has(AR, VIMATI))}",
        f"{Q(f'{has(PUTH, VIMATI)}, {has(TASSA, VIM_PE)}')} {YES} {Q(f'{has(AR, VIMATI)}, {has(TASSA, VIM_PE)}')} "
        f"{NO_PE}",
        f"{Q(f'{has(AR, VIMATI)}, {has(TASSA, VIM_PE, True)}')} {YES} "
        f"{Q(f'{has(PUTH, VIMATI)}, {has(TASSA, VIM_PE, True)}')} {NO_PE}",
        f"{Q(T)} {YES} {cap(ASUCI)} của {AR} là thứ tiết ra từ cái gì? Là thứ tiết ra từ những gì {ASITA}. "
        f"{Q(f'{ASUCI} của {AR} là thứ tiết ra từ những gì {ASITA}')} {YES} "
        f"{Q(f'bất cứ ai ăn, uống, nhai, nếm, thì tất cả những người ấy đều có {ASUCI}')} {NO_PE}",
        f"{Q(f'bất cứ ai ăn, uống, nhai, nếm, thì tất cả những người ấy đều có {ASUCI}')} {YES} "
        f"{Q(f'trẻ em ăn, uống, nhai, nếm, trẻ em có {ASUCI}')} {NO}",
        f"{Q(f'những {PANDAKA} ăn, uống, nhai, nếm, những {PANDAKA} có {ASUCI}')} {NO_PE}",
        f"{Q(f'chư thiên ăn, uống, nhai, nếm, các vị thiên có {ASUCI}')} {NO_PE}")

    NIS = f"{ASUCI} của {AR} là thứ tiết ra từ những gì {ASITA}"
    UCC = f"phân và nước tiểu của {AR} là thứ tiết ra từ những gì {ASITA}"
    add("5-309",
        f"{Q(NIS)} {YES} {Q('nó có chỗ chứa')} {NO_PE}",
        f"{Q(f'{UCC}, nó có chỗ chứa')} {YES} {Q(f'{NIS}, nó có chỗ chứa')} {NO_PE}",
        f"{Q(f'{NIS}, nó không có chỗ chứa')} {YES} {Q(f'{UCC}, nó không có chỗ chứa')} {NO_PE}")

    SEX = ["hưởng thụ hành vi dâm dục", "làm phát sinh sự dâm dục", "sống trên chiếc giường chật chội vì con cái",
           "thụ hưởng gỗ đàn hương xứ Ca-thi", "mang vòng hoa, hương thơm và dầu thoa", f"nhận {GOLD}"]
    #   methunaṃ dhammaṃ paṭiseveyya, methunaṃ uppādeyya, puttasambādhasayanaṃ ajjhāvaseyya, kāsikacandanaṃ
    #   paccanubhaveyya, mālāgandhavilepanaṃ dhāreyya, jātarūparajataṃ sādiyeyya
    SEX_V = [SEX[0], SEX[1] + var("Sī., Syā.", "methunaṃ dhammaṃ uppādeyya")] + SEX[2:]
    pos = "có thể " + ", ".join(SEX)
    negs = "không thể " + ", ".join(SEX)
    add("5-310",
        f"{Q(T)} {YES} Có phải {AR} có thể {', '.join(SEX_V)} không? {NO}",
        f"{Q(f'{TP}, {PUTH} {pos}')} {YES} {Q(f'{TA}, {AR} {pos}')} {NO_PE}",
        f"{Q(f'{TA}, nhưng {AR} {negs}')} {YES} {Q(f'{TP}, nhưng {PUTH} {negs}')} {NO}",
        nanu_raga(T),
        nanu_kil(T, AR_KIL[1:]))

    add("5-311",
        f"{Q(T)} {YES} {NANU(pahana(AR, RAGA, [MAGGA]))} {YES} {hanci_neg(pahana(AR, RAGA, [MAGGA]), T)}",
        f"{Q(T)} {YES} {NANU(pahana(AR, RAGA, BHAV))} {YES} {hanci_neg(pahana(AR, RAGA, [BOJJ]), T)}",
        nanu_pah(T, [G_DMA], ANOT),
        f"{Q(T)} {YES} {NANU(nanu_full(AR))} {YES} {hanci_neg(epi_last(AR, ', đã làm xong việc cần làm'), T)}")

    X = ASUCI
    G_ALL = [G_RAGA, G_DMA]
    add("5-312",
        sad_open(X), sad_l2(X),
        pair(raga1(SAD), raga1(PAR), X, False),
        pair(kil3(SAD), anot1(PAR), X, False),
        pair(pah_groups(SAD, G_ALL), pahana(PAR, ANOT, [BOJJ]), X, False),
        pair(epi_last(SAD), epi_last(PAR), X, False),
        pair(raga1(PAR), raga1(SAD), X, True),
        pair(kil3(PAR), anot1(SAD), X, True),
        pair(pah_groups(PAR, G_ALL), pahana(SAD, ANOT, [BOJJ]), X, True),
        pair(epi_last(PAR), epi_last(SAD), X, True))

    T_UP = has(AR, N_PARU)                                    # atthi arahato parūpahāro
    UPA = f"người khác có thể đưa {CPS} đến {AR}"             # arahato cīvara… pare upasaṃhareyyuṃ
    NIDDA = (f"“Này các tỳ-khưu, những vị tỳ-khưu là {PUTH} nào{var('Sī.', 'ye keci')} thành tựu giới hạnh, tỉnh "
             "thức, hiểu biết rõ ràng mà bước vào giấc ngủ, thì chất bất tịnh của họ không thoát ra. Này các tỳ-khưu, "
             "ngay cả những ẩn sĩ bên ngoài đã lìa tham đắm đối với các dục lạc, thì chất bất tịnh của họ cũng không "
             "thoát ra. Này các tỳ-khưu, đây là điều không thể xảy ra, không có cơ hội, rằng chất bất tịnh của "
             f"{AR} có thể thoát ra” [{C2.MAHAVA} 353, tương đồng về ý nghĩa; {CIT['a. ni.']} 5.210, cần xem].")
    add("5-313",
        f"{Q(T)} {YES} {NANU_VUTTAM} {NIDDA} {ATTHEVA} {YES} {tena_hi_na(T)}",
        f"{na_vattabbam(T_UP)} {YES} {NANU(UPA)} {YES} {hanci(UPA, T_UP)}",
        f"{neu(UPA, T_UP)} {YES} {Q(f'người khác có thể đưa {FRUITS4} đến {AR}')} {NO_PE}",
        katha_end(N_PARU))

    # ==== (11) 2. Aññāṇakathā ======================================================================================
    head("5-10-2-0", 4, VAGGA)
    head("5-10-2-1-0", 5, f"(11) 2. {katha(N_ANNA)}")
    X = N_ANNA
    T = has(AR, X)
    TP = has(PUTH, X)
    AV = f"bị {N_ANNA} chi phối"                              # aññāṇapakato (termbase)
    ROB = ["sát hại sinh mạng", "lấy của không được cho", "nói dối", "nói lời chia rẽ", "nói lời thô ác",
           "nói lời phù phiếm", "đột nhập nhà", "cướp bóc", "cướp một ngôi nhà", "mai phục bên đường",
           "đi lại với vợ người khác", "cướp phá làng", "cướp phá thị trấn"]
    #   pāṇaṃ haneyya, adinnaṃ ādiyeyya, musā bhaṇeyya, pisuṇaṃ bhaṇeyya, pharusaṃ bhaṇeyya, samphaṃ palapeyya,
    #   sandhiṃ chindeyya, nillopaṃ hareyya, ekāgāriyaṃ kareyya, paripanthe tiṭṭheyya, paradāraṃ gaccheyya,
    #   gāmaghātaṃ kareyya, nigamaghātaṃ kareyya
    ROB3 = f"{ROB[0]}, {ROB[1]}, {ROB[2]}{PE} {ROB[-2]}, {ROB[-1]}"
    ROB2 = f"{ROB[0]}, {ROB[1]}{PE} {ROB[-2]}, {ROB[-1]}"
    add("5-314",
        f"{Q(T)} {YES} {Q(has(AR, AVIJ7))} {NO} {Q(has(AR, AVIJ7, True))} {YES} {hanci_neg(has(AR, AVIJ7, True), T)}",
        f"{Q(f'{TP}, {has(TASSA, AVIJ7)}')} {YES} {Q(f'{T}, {has(TASSA, AVIJ7)}')} {NO}",
        f"{Q(f'{T}, {has(TASSA, AVIJ7, True)}')} {YES} {Q(f'{TP}, {has(TASSA, AVIJ7, True)}')} {NO}",
        f"{Q(T)} {YES} Có phải {AR}, {AV}, có thể {', '.join(ROB)} không? {NO}",
        f"{Q(f'{TP}, {PUTH}, {AV}, có thể {ROB3}')} {YES} {Q(f'{T}, {AR}, {AV}, có thể {ROB2}')} {NO}",
        f"{Q(f'{T}, nhưng {AR}, {AV}, không thể {ROB2}')} {YES} {Q(f'{TP}, nhưng {PUTH}, {AV}, không thể {ROB2}')} {NO}",
        f"{Q(T)} {YES} {Q(has(AR, eight(X)))} {NO}",
        f"{Q(has(AR, eight(X), True))} {YES} {hanci_neg(has(AR, eight(X, 'pe3'), True), T)}",
        f"{Q(f'{TP}, {has(TASSA, eight(X, 'pe3'))}')} {YES} {Q(f'{T}, {has(TASSA, eight(X, 'pe3'))}')} {NO}",
        f"{Q(f'{T}, {has(TASSA, eight(X, 'pe3'), True)}')} {YES} {Q(f'{TP}, {has(TASSA, eight(X, 'pe3'), True)}')} "
        f"{NO}")

    add("5-315",
        nanu_raga(T),
        nanu_kil(T, [DOSA, MOHA, ANOT]),
        f"{Q(T)} {YES} {NANU(pahana(AR, RAGA, [MAGGA, BOJJ]))} {YES} {hanci_neg(pahana(AR, RAGA, [BOJJ]), T)}",
        nanu_pah(T, [G_DMA], ANOT),
        f"{Q(T)} {YES} {NANU(epi_last(AR))} {YES} {hanci_neg(f'{AR} đã lìa tham đắm{PE} {LAST}', T)}")

    add("5-316",
        sad_open(X), sad_l2(X),
        pair(raga1(SAD), raga1(PAR), X, False),
        pair(kil3(SAD), anot1(PAR), X, False),
        pair(pahana(SAD, RAGA, [MAGGA, BOJJ]), pahana(PAR, RAGA, [BOJJ]), X, False),
        pair(pah_groups(SAD, [G_DMA]), pahana(PAR, ANOT, [BOJJ]), X, False),
        pair(epi_last(SAD), epi_last(PAR), X, False),
        pair(raga1(PAR), raga1(SAD), X, True),
        pair(kil3(PAR), anot1(SAD), X, True),
        pair(f"{PAR}, để dứt bỏ {RAGA}, đã tu tập {MAGGA}{PE} đã tu tập {BOJJ}{PE} để dứt bỏ {DOSA}, để dứt bỏ "
             f"{MOHA}{PE} để dứt bỏ {ANOT}, đã tu tập {MAGGA}{PE} đã tu tập {BOJJ}", pahana(SAD, ANOT, [BOJJ]), X,
             True),
        pair(epi_last(PAR), epi_last(SAD), X, True))

    CIT_JAN1 = f" [{CIT['saṃ. ni.']} 3.101; {CIT['itivu.']} 102; {CIT['saṃ. ni.']} 5.1095]"
    CIT_JAN2 = f" [{CIT['saṃ. ni.']} 5.1095]"
    CIT_SAB = f" [{CIT['saṃ. ni.']} 4.26; {CIT['itivu.']} 7, cũng trong {CIT['itivu.']}]"
    names_pos = ", ".join(f"có thể không biết {x}" for x in NAMES3)
    add("5-317",
        nanu_sutta(T, jan_sutta1(".", JAN_V, CIT_JAN1)),
        nanu_sutta(T, jan_sutta2(CIT_JAN2)),
        nanu_sutta(T, sabba(",", CIT_SAB)),
        f"{Q(T)} {YES} {NANU_VUTTAM}",
        *RATANA6,
        f"{ATTHEVA} {YES} {tena_hi_na(T)}",
        nanu_sutta(T, dc(".")),
        f"{na_vattabbam(T)} {YES} {NANU(f'{AR} {names_pos}')} {YES} {hanci(f'{AR} {names_pos}', T)}",
        f"{neu(f'{AR} {names_pos}', T)} {YES} {Q(f'{AR} có thể không biết {FRUITS4}')} {NO_PE}",
        katha_end(N_ANNA))

    # ==== (12) 3. Kaṅkhākathā ======================================================================================
    head("5-10-3-0", 4, VAGGA)
    head("5-10-4-0", 4, f"(12) 3. {katha(N_KANKHA)}")
    X = N_KANKHA
    T = has(AR, X)
    TP = has(PUTH, X)
    add("5-318",
        f"{Q(T)} {YES} {Q(has(AR, VIC4))} {NO_PE}",
        f"{Q(has(AR, VIC4, True))} {YES} {hanci_neg(has(AR, VIC4, True), T)}",
        f"{Q(f'{TP}, {has(TASSA, VIC4)}')} {YES} {Q(f'{T}, {has(TASSA, VIC4)}')} {NO_PE}",
        f"{Q(f'{T}, {has(TASSA, VIC4, True)}')} {YES} {Q(f'{TP}, {has(TASSA, VIC4, True)}')} {NO_PE}",
        f"{Q(T)} {YES} {Q(has(AR, eight(X)))} {NO}",
        f"{Q(has(AR, eight(X, 'pe2'), True))} {YES} {hanci_neg(has(AR, eight(X, 'pe2'), True), T)}",
        f"{Q(f'{TP}, {has(TASSA, eight(X, 'pe2'))}')} {YES} {Q(f'{T}, {has(TASSA, eight(X, 'pe2'))}')} {NO}",
        f"{Q(f'{T}, {has(TASSA, eight(X, 'pe2'), True)}')} {YES} {Q(f'{TP}, {has(TASSA, eight(X, 'pe2'), True)}')} "
        f"{NO}")

    BIG = (f"{kil3(AR)}{PE} để dứt bỏ {RAGA}, đã tu tập {MAGGA}{PE} đã tu tập {BOJJ}{PE} để dứt bỏ {DOSA}{PE} "
           f"để dứt bỏ {ANOT}, đã tu tập {MAGGA}{PE} đã tu tập {BOJJ}; chẳng phải {epi_last(AR)}")
    #   arahato doso pahīno…pe… moho…pe… anottappaṃ pahīnaṃ…pe… rāgappahānāya maggo bhāvito…pe… bojjhaṅgā bhāvitā…pe…
    #   dosappahānāya…pe… anottappapahānāya maggo bhāvito…pe… bojjhaṅgā bhāvitā; nanu arahā vītarāgo …
    add("5-319",
        nanu_raga(T),
        f"{Q(T)} {YES} {NANU(BIG)} {YES} {hanci_neg(epi_last(AR), T)}")

    def big_sad(who):               # who-ssa doso…pe… (all groups)…pe… who vītarāgo …
        return (f"{kil3(who)}{PE} để dứt bỏ {RAGA}, đã tu tập {MAGGA}{PE} đã tu tập {BOJJ}{PE} để dứt bỏ {DOSA}"
                f"{PE} để dứt bỏ {MOHA}{PE} để dứt bỏ {ANOT}, đã tu tập {MAGGA}{PE} đã tu tập {BOJJ}{PE} "
                f"{epi_last(who)}")

    t_has, t_not = has(TASSA, X), has(TASSA, X, True)
    add("5-320",
        sad_open(X), sad_l2(X),
        pair(raga1(SAD), raga1(PAR), X, False),
        f"{Q(f'{big_sad(SAD)}, {t_has}')} {YES} {Q(f'{epi_last(PAR)}, {t_has}')} {NO_PE} "
        f"{q(f'{raga1(PAR)}, {t_not}')} {YES} {Q(f'{raga1(SAD)}, {t_not}')} {NO_PE}",
        f"{Q(f'{big_sad(PAR)}, {t_not}')} {YES} {Q(f'{epi_last(SAD)}, {t_not}')} {NO_PE}")

    names_k = ", ".join(f"có thể nghi ngờ về {x}" for x in NAMES3)
    V1 = ["“Khi các hiện tượng thật sự xuất hiện,",
          "Nơi vị bà-la-môn nhiệt tâm đang thiền định;",
          f"Thì mọi {N_KANKHA} của vị ấy đều tan biến,"]
    #   Yadā have pātubhavanti dhammā, / Ātāpino jhāyato brāhmaṇassa; / Athassa kaṅkhā vapayanti sabbā,
    VERSES = V1 + ["Vì vị ấy hiểu rõ hiện tượng cùng với nguyên nhân của nó."] + V1 + [
        "Vì vị ấy đã biết sự diệt tận của các điều kiện."] + V1[:2] + [
        "Vị ấy đứng vững, xua tan đạo quân của Ma vương,",
        f"Như mặt trời{var_sp('Sī., Syā., Kaṃ., Pī.', 'suriyova')} chiếu sáng bầu trời "
        f"[{C2.MAHAVA} 3; Kinh Phật Tự Thuyết 3].",
        f"“Bất cứ {N_KANKHA} nào, ở đời này hay ở đời sau,",
        "Thuộc về mình hay thuộc về người khác;",
        f"Những người thiền định{var('Kinh Phật Tự Thuyết', 'ye jhāyino')} dứt bỏ tất cả những điều ấy,",
        "Những người nhiệt tâm, sống đời sống tu hành trong sạch [Kinh Phật Tự Thuyết 47, cũng trong Kinh Phật Tự "
        "Thuyết].",
        f"“Những ai đã vượt qua {N_KANKHA}, giữa các chúng sinh còn {N_KANKHA};",
        "Không còn ngờ vực, đã thoát khỏi trói buộc, điều được bố thí cho họ có quả lớn.",
        "“Ở đây, sự công bố Giáo Pháp là như thế,",
        "Ở đó, không vị đệ tử nào nghi ngờ điều gì;",
        "Bậc đã vượt qua dòng lũ" + var_sp("Sī., Ka.", "nitiṇṇaoghaṃ").replace("]", "; (Syā., Kaṃ.): nittiṇṇaoghaṃ]")
        + ", đã cắt đứt sự hoài nghi,",
        f"Chúng ta đảnh lễ Đức Phật, bậc Chiến Thắng, bậc chúa tể của loài người” [{DN} 2.354]."]
    assert len(VERSES) == 22
    add("5-321",
        nanu_sutta(T, jan_sutta1_short()),
        nanu_sutta(T, jan_sutta2_k()),
        nanu_sutta(T, sabba(";")),
        nanu_sutta(T, RATANA_SHORT),
        nanu_sutta(T, dc("!")),
        f"{Q(T)} {YES} {NANU_VUTTAM}",
        *VERSES,
        f"{ATTHEVA} {YES} {tena_hi_na(T)}",
        f"{na_vattabbam(T)} {YES} {NANU(f'{AR} {names_k}')} {YES} {hanci(f'{AR} {names_k}', T, ';')}",
        f"{neu(f'{AR} {names_k}', T)} {YES} {Q(f'{AR} có thể nghi ngờ về {FRUITS4}')} {NO_PE}",
        katha_end(N_KANKHA))

    # ==== (13) 4. Paravitāraṇakathā ================================================================================
    head("5-10-5-0", 4, VAGGA)
    head("5-10-5-1-0", 5, f"(13) 4. {katha(N_PARAV)}")
    X = N_PARAV
    T = has(AR, X)
    TP = has(PUTH, X)
    DEP = ("phải được người khác dẫn dắt, phải tin vào người khác, phải dựa vào người khác, bị lệ thuộc vào người "
           "khác, không biết, không thấy, mê mờ, không hiểu biết rõ ràng")
    #   paraneyyo parapattiyo parapaccayo parapaṭibaddhabhū, na jānāti na passati sammūḷho asampajāno
    IND = ("không phải được người khác dẫn dắt, không phải tin vào người khác, không phải dựa vào người khác, không "
           "bị lệ thuộc vào người khác, biết, thấy, không mê mờ, hiểu biết rõ ràng")
    #   na paraneyyo na parapattiyo na parapaccayo na parapaṭibaddhabhū, jānāti passati asammūḷho sampajāno
    E3 = eight(X, "pe2")
    add("5-322",
        f"{Q(T)} {YES} {Q(f'{AR} {DEP}')} {NO_PE}",
        f"{NANU(f'{AR} {IND}')} {YES} {hanci_neg(f'{AR} {IND}', T)}",
        f"{Q(f'{TP}, và {TASSA} {DEP}')} {YES} {Q(f'{T}, và {TASSA} {DEP}')} {NO_PE}",
        f"{Q(f'{T}, và {TASSA} {IND}')} {YES} {Q(f'{TP}, và {TASSA} {IND}')} {NO_PE}",
        f"{Q(T)} {YES} {Q(has(AR, eight(X)))} {NO_PE}",
        f"{Q(has(AR, E3, True))} {YES} {hanci_neg(has(AR, E3, True), T)}",
        f"{Q(f'{TP}, {has(TASSA, E3)}')} {YES} {Q(f'{T}, {has(TASSA, E3)}')} {NO_PE}",
        f"{Q(f'{T}, {has(TASSA, E3, True)}')} {YES} {Q(f'{TP}, {has(TASSA, E3, True)}')} {NO_PE}")

    BIG_P = (f"{kil3(AR)}, {UCCH}{PE} để dứt bỏ {RAGA}, đã tu tập {MAGGA}{PE} đã tu tập {BOJJ}{PE} để dứt bỏ {DOSA}{PE} "
             f"để dứt bỏ {ANOT}, đã tu tập {MAGGA}{PE} đã tu tập {BOJJ}{PE} chẳng phải {epi_last(AR)}")
    add("5-323",
        nanu_raga(T),
        f"{Q(T)} {YES} {NANU(BIG_P)} {YES} {hanci_neg(f'{AR} {EPI3}, {LAST}', T)}")

    def big_p(who, kil):            # paravitāraṇā variant (no mohappahānāya)
        return (f"{kil}{PE} để dứt bỏ {RAGA}, đã tu tập {MAGGA}{PE} đã tu tập {BOJJ}{PE} để dứt bỏ {DOSA}{PE} "
                f"để dứt bỏ {ANOT}, đã tu tập {MAGGA}{PE} đã tu tập {BOJJ}{PE} {epi_last(who)}")

    t_has, t_not = has(TASSA, X), has(TASSA, X, True)
    KIL_PAR = f"{DOSA} của {PAR} {PAHINA}, {MOHA} {PAHINA}{PE} {ANOT} {PAHINA}"     # doso pahīno, moho pahīno…pe…
    add("5-324",
        sad_open(X), sad_l2(X),
        pair(raga1(SAD), raga1(PAR), X, False, NO),
        f"{Q(f'{big_p(SAD, kil3(SAD))}, {t_has}')} {YES} {Q(f'{epi_last(PAR)}, {t_has}')} {NO_PE}",
        pair(raga1(PAR), raga1(SAD), X, True, NO),
        f"{Q(f'{big_p(PAR, KIL_PAR)}, {t_not}')} {YES} {Q(f'{epi_last(SAD)}, {t_not}')} {NO_PE}")

    DHOTAKA = [f"“Ta không có khả năng{var('Sī., Syā., Ka.', 'gamissāmi').replace(']', '; (Pī.): samīhāmi]')} giải thoát",
               f"Bất cứ ai{var('Ka.', 'kiñci')} còn băn khoăn ở thế gian, này Đô-ta-ca;",
               "Và khi hiểu biết trực tiếp Giáo Pháp tối thượng,",
               f"Như vậy ông sẽ vượt qua dòng lũ này” [{CIT['su. ni.']} 1070, trong {CIT['su. ni.']}; "
               f"{CIT['cūḷani.']} 33, phần giải thích câu hỏi của thanh niên Đô-ta-ca]."]
    #   Nāhaṃ sahissāmi pamocanāya, / Kathaṅkathiṃ dhotaka kañci loke; / Dhammañca seṭṭhaṃ abhijānamāno, /
    #   Evaṃ tuvaṃ oghamimaṃ taresī
    vit = [f"người khác có thể giảng giải cho {AR} về {NAMES3[0]}"] + [
        f"người khác có thể giảng giải về {x}" for x in NAMES3[1:]]
    VIT = ", ".join(vit)
    add("5-325",
        nanu_sutta(T, jan_sutta1_short()),
        nanu_sutta(T, jan_sutta2_p()),
        nanu_sutta(T, sabba(";")),
        nanu_sutta(T, RATANA_SHORT),
        nanu_sutta(T, dc("!")),
        f"{Q(T)} {YES} {NANU_VUTTAM}",
        *DHOTAKA,
        f"{ATTHEVA} {YES} {tena_hi_na(T)}",
        f"{na_vattabbam(T)} {YES} {NANU(VIT)} {YES} {hanci(VIT, T)}",
        f"{neu(VIT, T)} {YES} {Q(f'người khác có thể giảng giải cho {AR} về {FRUITS4}')} {NO_PE}",
        katha_end(N_PARAV))

    # ==== (14) 5. Vacībhedakathā ===================================================================================
    head("5-10-6-0", 4, VAGGA)
    head("5-10-6-1-0", 5, f"(14) 5. {katha(N_VACI)}")
    SAM = "người đang nhập"                                   # samāpannassa (termbase)
    SAMS = "những người đang nhập"                            # samāpannānaṃ
    T = has(SAM, N_VACI)                                      # samāpannassa atthi vacībhedo
    KB = "sự phát ra cử động thân"                            # kāyabhedo (termbase)
    add("5-326",
        f"{Q(T)} {YES} {Q(f'{SAMS} có {N_VACI} ở mọi nơi')} {NO_PE}",
        f"{Q(T)} {YES} {Q(f'{SAMS} có {N_VACI} vào mọi lúc')} {NO_PE}",
        f"{Q(T)} {YES} {Q(f'tất cả {SAMS} đều có {N_VACI}')} {NO_PE}",
        f"{Q(T)} {YES} {Q(f'trong mọi thành tựu thiền đều có {N_VACI}')} {NO_PE}",
        f"{Q(T)} {YES} {Q(has(SAM, KB))} {NO_PE}",
        f"{Q(has(SAM, KB, True))} {YES} {Q(has(SAM, N_VACI, True))} {NO_PE}",
        f"{Q(f'{SAM} có lời nói, có {N_VACI}')} {YES} {Q(f'{SAM} có thân, có {KB}')} {NO_PE}",
        f"{Q(f'{SAM} có thân, không có {KB}')} {YES} {Q(f'{SAM} có lời nói, không có {N_VACI}')} {NO_PE}")

    def jv(x, neg=False):           # Xti jānanto (na ca) Xti vācaṃ bhāsati
        return f"trong khi biết rằng đó là {x}, {'nhưng không' if neg else 'thì'} nói ra lời rằng đó là {x}"

    DUK, SAMU, NIRO, MAG = "khổ đau", "sự phát sinh", "sự chấm dứt", "con đường"
    add("5-327",
        *[f"{Q(jv(DUK))} {YES} {Q(jv(x))} {NO_PE}" for x in (SAMU, NIRO, MAG)],
        *[f"{Q(jv(x, True))} {YES} {Q(jv(DUK, True))} {NO_PE}" for x in (SAMU, NIRO, MAG)])

    NS = "hiểu biết có phạm vi là sự thật, tai có phạm vi là âm thanh"   # ñāṇaṃ saccagocaraṃ, sotaṃ saddagocaraṃ
    add("5-328",
        f"{Q(T)} {YES} Hiểu biết có phạm vi là gì? Hiểu biết có phạm vi là sự thật. {Q('tai có phạm vi là sự thật')} "
        f"{NO_PE}",
        f"{Q(T)} {YES} Tai có phạm vi là gì? Tai có phạm vi là âm thanh. {Q('hiểu biết có phạm vi là âm thanh')} {NO}",
        f"{Q(f'{T}, {NS}')} {YES} {hanci_neg(NS, T)}",
        f"{Q(f'{T}, {NS}')} {YES} "
        f"{Q('có sự tụ hợp của hai sự tiếp xúc, hai cảm giác, hai tri giác, hai chủ ý, hai tâm')} {NO}")

    K_ARU = KASINA[1:] + [AKASA, VINNANAÑCA, AKINCA, NEVASA]
    KS = f"{PE} ".join(K_ARU)
    P_K = f"{SAM} thành tựu thiền với {KASINA[0]}"            # pathavīkasiṇaṃ samāpattiṃ samāpannassa
    LS = f"{SAM} thành tựu thiền thuộc thế gian"              # lokiyasamāpattiṃ / lokiyaṃ samāpattiṃ samāpannassa

    def lj(j, kind="thuộc thế gian"):
        return f"{SAM} {j} {kind}"

    def ljs(js, kind="thuộc thế gian"):     # lokiyaṃ dutiyaṃ jhānaṃ… tatiyaṃ jhānaṃ… catutthaṃ jhānaṃ
        return f"{SAM} {f'{PE} '.join(js)} {kind}"

    add("5-329",
        f"{Q(T)} {YES} {Q(has(P_K, N_VACI))} {NO}",
        f"{Q(T)} {YES} {Q(has(f'{SAM} {KS}', N_VACI))} {NO_PE}",
        f"{Q(has(P_K, N_VACI, True))} {YES} {hanci_neg(has(P_K, N_VACI, True), T)}",
        f"{Q(has(f'{SAM} {KS}', N_VACI, True))} {YES} {hanci_neg(has(f'{SAM} {NEVASA}', N_VACI, True), T)}",
        f"{Q(T)} {YES} {Q(has(LS, N_VACI))} {NO_PE}",
        f"{Q(T)} {YES} {Q(has(lj(J1), N_VACI))} {NO_PE} {Q(T)} {YES} {Q(has(ljs([J2, J3, J4]), N_VACI))} {NO_PE}",
        f"{Q(has(LS, N_VACI, True))} {YES} {hanci_neg(has(LS, N_VACI, True), T)}",
        f"{Q(has(lj(J1), N_VACI, True))} {YES} {hanci_neg(has(lj(J1), N_VACI, True), T)}",
        f"{Q(has(ljs([J2, J3, J4]), N_VACI, True))} {YES} {hanci_neg(has(lj(J4), N_VACI, True), T)}")

    LU = "vượt thế gian"
    add("5-330",
        f"{Q(has(lj(J1, LU), N_VACI))} {YES} {Q(has(lj(J1), N_VACI))} {NO_PE}",
        f"{Q(has(lj(J1, LU), N_VACI))} {YES} {Q(has(ljs([J2, J3, J4]), N_VACI))} {NO_PE}",
        f"{Q(has(lj(J1), N_VACI, True))} {YES} {Q(has(lj(J1, LU), N_VACI, True))} {NO_PE}",
        f"{Q(has(ljs([J2, J3, J4]), N_VACI, True))} {YES} {Q(has(lj(J1, LU), N_VACI, True))} {NO_PE}")
    add("5-331",
        f"{Q(has(lj(J1, LU), N_VACI))} {YES} {Q(has(lj(J2, LU), N_VACI))} {NO_PE}",
        f"{Q(has(lj(J1, LU), N_VACI))} {YES} {Q(has(ljs([J3, J4], LU), N_VACI))} {NO_PE}",
        f"{Q(has(lj(J2, LU), N_VACI, True))} {YES} {Q(has(lj(J1, LU), N_VACI, True))} {NO_PE}",
        f"{Q(has(ljs([J2, J3, J4], LU), N_VACI, True))} {YES} {Q(has(lj(J1, LU), N_VACI, True))} {NO_PE}")

    VV = "sự hướng tâm và sự duy trì tâm"                     # vitakkavicārā (termbase)
    J1VV = f"{SAM} {J1} có {VV}"                               # paṭhamaṃ jhānaṃ samāpannassa atthi vitakkavicārā
    SAID_VS = f"Đức Thế Tôn đã nói rằng {VV} là các sự tạo tác bằng lời nói"   # vitakkavicārā vacīsaṅkhārā vuttā bhagavatā
    SAID_VT = "Đức Thế Tôn đã nói rằng lời nói do sự hướng tâm sinh ra"        # vitakkasamuṭṭhānā vācā vuttā bhagavatā
    SAID_ST = "Đức Thế Tôn đã nói rằng lời nói do tri giác sinh ra"           # saññāsamuṭṭhānā vācā vuttā bhagavatā
    V_EV = var("Syā.", "atthi vitakkavicārā, cũng vậy ở các chỗ sau")
    KJ = f"{PE} ".join(f"với {k}" for k in KASINA[1:])
    VS_Q, VS_H = f"{SAID_VS} – “{J1VV}”", f"{SAID_VS} – “{J1VV},”"
    VT_Q, VT_H = f"{SAID_VT} – “{J1VV}”", f"{SAID_VT} – “{J1VV},”"
    ST_Q = f"{SAID_ST} – “{SAM} {J2} có tri giác, {has(TASSA, VV)}”"
    add("5-332",
        f"{na_vattabbam(T)} {YES} {NANU(VS_Q)} {YES} {hanci(VS_H, T, '')}",
        f"Có phải nếu {SAID_VS} – “{J1VV}”{V_EV}, thì {has(TASSA, N_VACI)} không? {YES} "
        f"{Q(f'{SAM} {J1} với {KASINA[0]} có {VV}, {has(TASSA, N_VACI)}')} {NO_PE}",
        f"{neu(VS_Q, has(TASSA, N_VACI))} {YES} "
        f"{Q(f'{SAM} {J1} {KJ} có {VV}, {has(TASSA, N_VACI)}')} {NO_PE}",
        f"{na_vattabbam(T)} {YES} {NANU(VT_Q)} {YES} {hanci(VT_H, T, '')}",
        f"{neu(VT_Q, has(TASSA, N_VACI))} {YES} {Q(ST_Q)} {NO_PE}",
        f"{neu(VT_Q, has(TASSA, N_VACI))} {YES} "
        f"{Q(f'{SAID_ST} – {SAM} {J3}{PE} {J4}{PE} {AKASA}{PE} {VINNANAÑCA}{PE} {AKINCA} có tri giác, {has(TASSA, VV)}')} "
        f"{NO_PE}")

    def nir(who, what, pl=False):   # X samāpannassa Y niruddhā hoti / honti
        return f"đối với {SAM} {who}, {what} đã chấm dứt"

    C259 = f" [{CIT['saṃ. ni.']} 4.259, 263]"
    VN = nir(J1, "lời nói")                                    # paṭhamaṃ jhānaṃ samāpannassa vācā niruddhā hoti
    NIR9 = ", ".join([nir(J3, "sự hân hoan"), nir(J4, "hơi thở vào và hơi thở ra"),
                      nir(AKASA, "tri giác về hình sắc"), nir(VINNANAÑCA, f"tri giác về {AKASA}"),
                      nir(AKINCA, f"tri giác về {VINNANAÑCA}"), nir(NEVASA, f"tri giác về {AKINCA}"),
                      nir("sự chấm dứt tri giác và cảm giác", "tri giác và cảm giác")])
    SV = "tri giác và cảm giác"                                # saññā ca vedanā ca
    KAN = "cái gai"                                            # kaṇḍako / kaṇṭako (termbase)
    K_V = var_sp("Syā.", "kaṇṭako").replace("]", f"; {CIT['a. ni.']} 10.72]")

    def kan(who, what, cit=""):     # X-ssa jhānassa Y kaṇṭako vutto bhagavatā
        return f"Đức Thế Tôn đã nói rằng đối với {who}, {what} là {KAN}{cit}"

    AN72 = f" [{CIT['a. ni.']} 10.72]"
    KAN_LIST = f"{PE} ".join([
        kan(J2, VV), kan(J3, "sự hân hoan"), kan(J4, "hơi thở vào và hơi thở ra", AN72),
        kan(f"{SAM} {AKASA}", "tri giác về hình sắc"), kan(f"{SAM} {VINNANAÑCA}", f"tri giác về {AKASA}"),
        kan(f"{SAM} {AKINCA}", f"tri giác về {VINNANAÑCA}"), kan(f"{SAM} {NEVASA}", f"tri giác về {AKINCA}"),
        kan(f"{SAM} sự chấm dứt tri giác và cảm giác", SV, AN72)])
    KAN1 = kan(J1, "âm thanh")
    SIKHI = (f"“Này A-nan, vị đệ tử tên là A-tỳ-phù của Đức Thế Tôn Thi-khí, {AR}, bậc Tự Giác Ngộ Hoàn Toàn, "
             f"đứng vững ở {BRAHMALOKA}, đã làm cho mười nghìn thế giới nghe biết bằng giọng nói –")
    #   sikhissa, ānanda, bhagavato arahato sammāsambuddhassa abhibhū nāma sāvako brahmaloke ṭhito
    #   dasasahassilokadhātuṃ sarena viññāpesi –
    ABHIBHU = ["‘Hãy khởi sự, hãy tiến bước, hãy chuyên chú vào giáo huấn của Đức Phật;",
               "Hãy đánh tan đạo quân của Thần Chết, như voi phá ngôi nhà lau sậy.",
               "‘Ai sống không buông lung"
               + var_sp("Sī., Syā., Kaṃ.", "vihessati").replace("]", "; (Ka.): viharissati]")
               + " trong Giáo Pháp và Giới Luật này;",
               f"Sau khi dứt bỏ vòng luân hồi của sự sinh, sẽ làm nên tận cùng của khổ đau’” "
               f"[{CIT['a. ni.']} 1, trong Chương Bộ Ba; {CIT['saṃ. ni.']} 1.285]."]
    add("5-333",
        f"{Q(T)} {YES} Chẳng phải “{VN}”{C259} sao! {ATTHEVA} {YES} {hanci_neg(f'«{VN}», có bài kinh như vậy thật', T)}",
        f"Có phải “{VN}”{C259}, có bài kinh như vậy thật, {has(TASSA, N_VACI)} không? {YES} "
        f"Có phải “{nir(J2, VV)}”{C259}, có bài kinh như vậy thật, {has(TASSA, VV)} không? {NO_PE}",
        f"Có phải “{VN}”{C259}, có bài kinh như vậy thật, {has(TASSA, N_VACI)} không? {YES} "
        f"Có phải “{NIR9}” [{CIT['saṃ. ni.']} 4.259, 263; {CIT['a. ni.']} 9.31; {DN} 3.344], có bài kinh như vậy thật, "
        f"{has(TASSA, SV)} không? {NO_PE}",
        f"{na_vattabbam(T)} {YES} Chẳng phải Đức Thế Tôn đã nói rằng đối với {J1}, âm thanh là {KAN}{K_V} sao "
        f"[{CIT['a. ni.']} 10.72, câu hỏi dựa vào Kinh Cái Gai]? {YES} "
        f"{hanci(f'Đức Thế Tôn đã nói rằng đối với {J1}, âm thanh là {KAN}', T)}",
        f"{neu(KAN1, T)} {YES} Có phải {KAN_LIST}, {has(TASSA, SV)} không? {NO_PE}",
        f"{na_vattabbam(T)} {YES} {NANU_VUTTAM} {SIKHI}",
        *ABHIBHU,
        f"{ATTHEVA} {YES} {tena_hi(T)}",
        katha_end(N_VACI))

    # ==== (15) 6. Dukkhāhārakathā ==================================================================================
    head("5-10-7-0", 4, VAGGA)
    head("5-10-7-1-0", 5, f"(15) 6. {katha(N_DUKKHA)}")
    SAY = "nói ra lời rằng đó là khổ đau"                      # dukkhanti vācaṃ bhāsati / bhāsanti
    ALL = f"bất cứ ai {SAY}, thì tất cả những người ấy đều tu tập con đường"
    BALA = f"những {PUTH} ngu si"                              # bālaputhujjanā
    KILLERS = (f"kẻ giết mẹ{PE} kẻ giết cha{PE} kẻ giết bậc A-la-hán{PE} kẻ làm chảy máu"
               f"{var('Sī., Ka.', 'lohituppādako; nhưng ở các chỗ khác chỉ thấy ruhiruppādako')}{PE} kẻ chia rẽ Tăng đoàn")
    add("5-334",
        f"{Q(f'{N_DUKKHA} là chi phần của con đường, nằm trong con đường')} {YES} {Q(ALL)} {NO}",
        f"{Q(ALL)} {YES} {Q(f'{BALA} {SAY}, {BALA} tu tập con đường')} {NO} "
        f"{Q(f'{KILLERS} {SAY}, kẻ chia rẽ Tăng đoàn tu tập con đường')} {NO_PE}",
        katha_end(N_DUKKHA))

    # ==== (16) 7. Cittaṭṭhitikathā =================================================================================
    head("5-10-8-0", 4, VAGGA)
    head("5-10-8-1-0", 5, f"(16) 7. {katha(N_CITTA)}")
    ONE = "một tâm"                                            # ekaṃ cittaṃ (termbase)

    def dur(x):
        return f"duy trì suốt {x}"                             # X tiṭṭhati (tiṭṭhati «duy trì»)

    TC = f"{ONE} {dur('một ngày')}"                            # ekaṃ cittaṃ divasaṃ tiṭṭhati
    UPP, VAY = "khoảnh khắc sinh khởi", "khoảnh khắc suy tàn"
    D3 = ["bốn ngày", "tám ngày", "mười ngày", "hai mươi ngày", "một tháng", "hai tháng", "bốn tháng", "tám tháng",
          "mười tháng", "một năm", "hai năm", "bốn năm", "tám năm", "mười năm", "hai mươi năm", "ba mươi năm",
          "bốn mươi năm", "năm mươi năm", "một trăm năm", "hai trăm năm", "bốn trăm năm", "năm trăm năm",
          "một nghìn năm", "hai nghìn năm", "bốn nghìn năm", "tám nghìn năm", "mười sáu nghìn năm", "một kiếp",
          "hai kiếp", "bốn kiếp", "tám kiếp", "mười sáu kiếp", "ba mươi hai kiếp", "sáu mươi bốn kiếp", "năm trăm kiếp",
          "hàng nghìn kiếp", "hai nghìn kiếp", "bốn nghìn kiếp", "tám nghìn kiếp", "mười sáu nghìn kiếp",
          "hai mươi nghìn kiếp", "bốn mươi nghìn kiếp", "sáu mươi nghìn kiếp", "tám mươi bốn nghìn kiếp"]
    assert len(D3) == 44
    LH = "những hiện tượng ấy thay đổi nhanh hơn tâm"          # te dhammā cittena lahuparivattā
    MONKEY = ("“Này các tỳ-khưu, cũng như con khỉ đi lang thang trong rừng, trong khu rừng rậm, nắm lấy một cành cây, "
              "buông cành ấy ra rồi nắm lấy cành khác, buông cành ấy ra rồi nắm lấy cành khác; cũng y như vậy, này các "
              f"tỳ-khưu, cái được gọi là tâm{var(CIT['bahūsu'], 'yadidaṃ')}, là ý, là thức, cái ấy, suốt đêm và ngày, "
              f"sinh khởi là cái này, chấm dứt là cái khác” [{CIT['saṃ. ni.']} 2.61].")
    LAHU = ("“Này các tỳ-khưu, Ta không thấy một hiện tượng nào khác thay đổi nhanh như tâm này. Này các tỳ-khưu, tâm "
            f"thay đổi nhanh đến mức ngay cả một ví dụ cũng không dễ đưa ra” [{CIT['a. ni.']} 1.48].")
    add("5-335",
        f"{Q(TC)} {YES} {Q(f'nửa ngày là {UPP}, nửa ngày là {VAY}')} {NO}",
        f"{Q(f'{ONE} {dur("hai ngày")}')} {YES} {Q(f'một ngày là {UPP}, một ngày là {VAY}')} {NO}",
        f"Có phải {ONE} {f'{PE} '.join(dur(x) for x in D3)} không? {YES} "
        f"{Q(f'bốn mươi hai nghìn kiếp là {UPP}, bốn mươi hai nghìn kiếp là {VAY}')} {NO}",
        f"{Q(TC)} {YES} {Q('có những hiện tượng khác, trong một ngày, sinh khởi rồi chấm dứt nhiều lần')} {YES} "
        f"{Q(LH)} {NO}",
        f"{Q(LH)} {YES} {NANU_VUTTAM} {LAHU} {ATTHEVA} {YES} {tena_hi_na(LH)}",
        f"{Q(LH)} {YES} {NANU_VUTTAM} {MONKEY} {ATTHEVA} {YES} {tena_hi_na(LH)}")

    def yeneva(a, b):               # yeneva cittena a, teneva cittena b
        return f"với chính tâm nào mà {a}, cũng với chính tâm ấy mà {b}"

    SENSE = ["thấy hình sắc bằng mắt", "nghe âm thanh bằng tai", "ngửi mùi bằng mũi", "nếm vị bằng lưỡi",
             "chạm vào vật xúc chạm bằng thân", "nhận biết đối tượng của ý bằng ý"]
    #   cakkhunā rūpaṃ passati, sotena saddaṃ suṇāti, ghānena gandhaṃ ghāyati, jivhāya rasaṃ sāyati,
    #   kāyena phoṭṭhabbaṃ phusati, manasā dhammaṃ vijānāti
    CITTAS = (["thức qua tai", "thức qua mũi", "thức qua lưỡi", "thức qua thân", "tâm bất thiện"]
              + [f"đi kèm với {x}" for x in AR_KIL[:-1]] + [f"tâm đi kèm với {AR_KIL[-1]}"])
    SN = SENSE
    L336_2 = (f"{yeneva(SN[0], SN[1])}{PE} {SN[2]}{PE} {SN[3]}{PE} {SN[4]}{PE} {SN[5]}{PE} "
              f"{yeneva(SN[5], SN[0])}{PE} {SN[1]}{PE} {SN[2]}{PE} {SN[3]}{PE} {SN[4]}")
    A, P_, AL, VI = WALK
    W = [(A, P_), (P_, A), (AL, VI), (VI, AL), ("co lại", "duỗi ra"), ("duỗi ra", "co lại")]
    add("5-336",
        f"{Q(TC)} {YES} {Q(f'thức qua mắt {dur("một ngày")}')} {NO} Có phải {f'{PE} '.join(CITTAS)} {dur('một ngày')} không? {NO_PE}",
        f"{Q(TC)} {YES} {Q(L336_2)} {NO_PE}",
        f"{Q(TC)} {YES} {Q('; '.join(yeneva(a, b) for a, b in W))} {NO_PE}")

    YT = "duy trì suốt tuổi thọ"                               # yāvatāyukaṃ tiṭṭhati
    AK1 = f"đối với {AKASA_DEVA}, {ONE} {YT}"
    DEVA_L = f"{PE} ".join(f"chư thiên {d}" for d in DEVAS)
    L4 = [f"tuổi thọ của chư thiên {DEVAS[0]} là năm trăm năm, đối với chư thiên {DEVAS[0]}, {ONE} {dur('năm trăm năm')}"]
    L4 += [dur(x) for x in ["một nghìn năm", "hai nghìn năm", "bốn nghìn năm", "tám nghìn năm", "mười sáu nghìn năm",
                            THIRD_KAPPA, HALF_KAPPA, "một kiếp", "hai kiếp", "bốn kiếp", "tám kiếp", "mười sáu kiếp",
                            "ba mươi hai kiếp", "sáu mươi bốn kiếp", "năm trăm kiếp", "một nghìn kiếp",
                            "hai nghìn kiếp", "bốn nghìn kiếp", "tám nghìn kiếp"]]
    L4 += [f"tuổi thọ của chư thiên {DEVAS[-1]} là mười sáu nghìn kiếp, đối với chư thiên {DEVAS[-1]}, {ONE} "
           f"{dur('mười sáu nghìn kiếp')}"]
    AK20 = (f"tuổi thọ của {AKASA_DEVA} là hai mươi nghìn kiếp, đối với {AKASA_DEVA}, {ONE} "
            f"{dur('hai mươi nghìn kiếp')}")
    add("5-337",
        f"{Q(AK1)} {YES} {Q(f'đối với loài người, {ONE} {YT}')} {NO}",
        f"{Q(AK1)} {YES} Có phải đối với {DEVA_L}, {ONE} {YT} không? {NO}",
        f"{Q(AK20)} {YES} "
        f"{Q(f'tuổi thọ của loài người là một trăm năm, đối với loài người, {ONE} {dur("một trăm năm")}')} {NO}",
        f"{Q(AK20)} {YES} Có phải {f'{PE} '.join(L4)} không? {NO}",
        f"{Q(f'tâm của {AKASA_DEVA} sinh khởi từng thời khắc, chấm dứt từng thời khắc')} {YES} "
        f"{Q(f'{AKASA_DEVA} chết đi từng thời khắc, sinh khởi từng thời khắc')} {NO}",
        f"{Q(AK1)} {YES} {Q(f'{AKASA_DEVA}, {yeneva("sinh khởi", "chết đi")}')} {NO_PE}",
        katha_end(N_CITTA))

    # ==== (17) 8. Kukkuḷakathā =====================================================================================
    head("5-10-9-0", 4, VAGGA)
    head("5-10-9-1-0", 5, f"(17) 8. {katha(N_KUKKU)}")
    T = f"tất cả các tạo tác, không trừ ra phần nào, đều là {N_KUKKU}"    # sabbe saṅkhārā anodhiṃ katvā kukkuḷā
    SUKHA = ["cảm giác dễ chịu", "sự dễ chịu nơi thân", "sự dễ chịu trong tâm", "hạnh phúc cõi trời", "hạnh phúc cõi người",
             "hạnh phúc của lợi lộc", "hạnh phúc của sự được kính trọng", "hạnh phúc của xe cộ",
             "hạnh phúc của giường nằm", "hạnh phúc của quyền uy", "hạnh phúc của quyền thống trị",
             "hạnh phúc của người tại gia", "hạnh phúc của đời sống sa-môn", "hạnh phúc là đối tượng của ô nhiễm",
             "hạnh phúc không phải là đối tượng của ô nhiễm", "hạnh phúc có chấp trước", "hạnh phúc không còn chấp trước",
             "hạnh phúc có tính trần tục", "hạnh phúc không có tính trần tục", "hạnh phúc có sự hân hoan",
             "hạnh phúc không có sự hân hoan", "hạnh phúc của tầng thiền", "hạnh phúc của sự giải thoát",
             "hạnh phúc của dục lạc", "hạnh phúc của sự từ bỏ", "hạnh phúc của sự tách biệt", "hạnh phúc của sự lắng dịu",
             "hạnh phúc của sự giác ngộ"]
    #   sukhā vedanā, kāyikaṃ sukhaṃ, cetasikaṃ sukhaṃ, dibbaṃ sukhaṃ, mānusakaṃ sukhaṃ, lābhasukhaṃ, sakkārasukhaṃ,
    #   yānasukhaṃ, sayanasukhaṃ, issariyasukhaṃ, ādhipaccasukhaṃ, gihisukhaṃ, sāmaññasukhaṃ, sāsavaṃ sukhaṃ,
    #   anāsavaṃ sukhaṃ, upadhisukhaṃ, nirūpadhisukhaṃ, sāmisaṃ sukhaṃ, nirāmisaṃ sukhaṃ, sappītikaṃ sukhaṃ,
    #   nippītikaṃ sukhaṃ, jhānasukhaṃ, vimuttisukhaṃ, kāmasukhaṃ, nekkhammasukhaṃ, vivekasukhaṃ, upasamasukhaṃ,
    #   sambodhasukhaṃ
    assert len(SUKHA) == 28
    DUKKHA_L = f"cảm giác khó chịu, sự khó chịu nơi thân, sự khó chịu trong tâm, {SOKA5}"
    #   dukkhā vedanā kāyikaṃ dukkhaṃ cetasikaṃ dukkhaṃ sokaparidevadukkhadomanassaupāyāsā
    BURN = "đang bốc cháy"                                     # ādittaṃ / ādittā / āditto
    KENA = (f"Bốc cháy bởi cái gì? Ta nói rằng ‘bốc cháy bởi lửa tham đắm, lửa sân hận, lửa si mê, bốc cháy bởi "
            f"{JATI8}’.")
    #   Kena ādittaṃ? ‘Rāgagginā dosagginā mohagginā ādittaṃ, jātiyā … upāyāsehi āditta’nti vadāmi.
    VED = f"cảm nhận nào{{v}} sinh khởi do sự tiếp xúc của {{x}} làm điều kiện, dù {SUKHA3}, cảm nhận ấy cũng {BURN}"
    ADITTA = (f"“Này các tỳ-khưu, tất cả đều {BURN}! Và này các tỳ-khưu, tất cả cái gì {BURN}? Này các tỳ-khưu, "
              f"mắt {BURN}, các hình sắc {BURN}, thức qua mắt {BURN}, sự tiếp xúc của mắt {BURN}; "
              + VED.format(v=var(CIT['saṃ. ni.'] + " 4.28", "yampidaṃ"), x="mắt") + f". {KENA} "
              f"Tai {BURN}, các âm thanh {BURN}{PE} mũi {BURN}, các mùi {BURN}{PE} lưỡi {BURN}, các vị {BURN}{PE} "
              f"thân {BURN}, các vật xúc chạm {BURN}{PE} ý {BURN}, các đối tượng của ý {BURN}, ý thức {BURN}, "
              f"sự tiếp xúc của ý {BURN}; " + VED.format(v="", x="ý") + f". {KENA[:-1]}” "
              f"[{C2.MAHAVA} 54; {CIT['saṃ. ni.']} 4.28].")
    TH_V1 = var("Sī., Syā.", "tena hi").replace("]", "; (Ka.): tena hi na vattabbaṃ]")
    GUNA = ("“Này các tỳ-khưu, có năm loại dục lạc này! Năm loại nào? Các hình sắc được nhận biết bằng mắt, đáng "
            "mong muốn, đáng yêu mến, đáng ưa thích, có vẻ đáng yêu, gắn liền với dục lạc, hấp dẫn; các âm thanh được "
            f"nhận biết bằng tai{PE} các mùi được nhận biết bằng mũi{PE} các vị được nhận biết bằng lưỡi{PE} các vật "
            "xúc chạm được nhận biết bằng thân, đáng mong muốn, đáng yêu mến, đáng ưa thích, có vẻ đáng yêu, gắn liền "
            "với dục lạc, hấp dẫn. Này các tỳ-khưu, đây là năm loại dục lạc” "
            f"[{CIT['ma. ni.']} 1.166; {CIT['saṃ. ni.']} 4.268].")

    def phassa(place, neg):         # cha phassāyatanikā nāma nirayā / saggā
        a, b = ("không ", "") if neg else ("", "không ")
        trio = (f"chỉ {{v}} điều có vẻ {a}đáng mong muốn, không {{v}} điều có vẻ {b}đáng mong muốn; chỉ {{v}} điều có "
                f"vẻ {a}đáng yêu mến, không {{v}} điều có vẻ {b}đáng yêu mến; chỉ {{v}} điều có vẻ {a}đáng ưa thích, "
                f"không {{v}} điều có vẻ {b}đáng ưa thích")
        v1 = var(CIT['bahūsu'], 'paṭividdho') if neg else ""
        return ("“Này các tỳ-khưu, đó là lợi lộc cho các ông, này các tỳ-khưu, các ông đã khéo được lợi, các ông đã có "
                f"được{v1} thời cơ để sống đời sống tu hành trong sạch! Này các tỳ-khưu, Ta đã thấy {place} có tên là sáu "
                "lĩnh vực tiếp xúc. Ở đó, dù thấy bất cứ hình sắc nào bằng mắt, thì " + trio.format(v="thấy") + ". "
                f"Dù nghe bất cứ âm thanh nào bằng tai{PE} ngửi mùi bằng mũi{PE} nếm vị bằng lưỡi{PE} chạm vào vật "
                "xúc chạm bằng thân… nhận biết đối tượng của ý bằng ý, thì " + trio.format(v="nhận biết") + "” "
                f"[{CIT['saṃ. ni.']} 4.135].")

    ANICCA_P = ("«cái gì vô thường thì cái ấy là khổ đau [" + CIT['saṃ. ni.'] + " 3.15],» Đức Thế Tôn đã nói, "
                "«tất cả các tạo tác đều vô thường» [" + CIT['dha. pa.'] + " 277; " + CIT['ma. ni.'] + " 1.356]")
    ANICCA_H = "«cái gì vô thường thì cái ấy là khổ đau,» Đức Thế Tôn đã nói, «tất cả các tạo tác đều vô thường,»"
    BAD = S.SAPHALA_A.split(", ", 2)[2]          # aniṭṭhaphalaṃ … dukkhavipākaṃ
    GOOD = S.SAPHALA_K.split(", ", 2)[2]         # iṭṭhaphalaṃ … sukhavipākaṃ
    MERIT4 = f"giới hạnh{PE} sự hành trì ngày trai giới{PE} sự tu tập{PE} đời sống tu hành trong sạch"
    SUKHO = ["“Sự tách biệt là hạnh phúc cho người biết đủ, đã nghe Giáo Pháp và thấy rõ;",
             "Không ác ý là hạnh phúc ở đời, sự chế ngự đối với các loài hữu tình.",
             "“Sự lìa tham là hạnh phúc ở đời, sự vượt qua các dục lạc;",
             f"Sự điều phục kiêu mạn về bản ngã, đó quả thật là hạnh phúc tối thượng "
             f"[{C2.MAHAVA} 5; Kinh Phật Tự Thuyết 11, và trong Kinh Phật Tự Thuyết].",
             "“Hạnh phúc ấy đạt được nhờ hạnh phúc, đó chính là hạnh phúc hoàn toàn;",
             "Ba hiểu biết chân thật đã được chứng đạt, đó quả thật là hạnh phúc tối thượng”."]
    #   Sukho viveko tuṭṭhassa, sutadhammassa passato; / Abyāpajjaṃ sukhaṃ loke, pāṇabhūtesu saṃyamo. / Sukhā
    #   virāgatā loke, kāmānaṃ samatikkamo; / Asmimānassa yo vinayo, etaṃ ve paramaṃ sukhaṃ. / Taṃ sukhena sukhaṃ
    #   pattaṃ, accantasukhameva taṃ; / Tisso vijjā anuppattā, etaṃ ve paramaṃ sukhaṃ
    add("5-338",
        f"{Q(T)} {YES} {NANU(f'có {', '.join(SUKHA)}')} {YES} "
        f"{hanci_neg(f'có {SUKHA[0]}{PE} {SUKHA[-1]}', T)}",
        f"{Q(T)} {YES} {Q(f'tất cả các tạo tác đều là {DUKKHA_L}')} {NO}",
        f"{na_vattabbam(T)} {YES} {NANU_VUTTAM} {ADITTA} {ATTHEVA} {YES} Vậy thì nên nói{TH_V1} – “{T}”.",
        f"{Q(T)} {YES} {NANU_VUTTAM} {GUNA} {ATTHEVA} {YES} {tena_hi_na(T)}",
        f"{na_vattabbam(T)} {YES} {NANU_VUTTAM} {phassa('các địa ngục', True)} {ATTHEVA} {YES} "
        f"Vậy thì nên nói{var('Syā., Ka.', 'tena hi na vattabbaṃ')} – “{T}”.",
        f"{Q(T)} {YES} {NANU_VUTTAM} {phassa('các cõi trời', False)} {ATTHEVA} {YES} {tena_hi_na(T)}",
        f"{na_vattabbam(T)} {YES} {NANU(S.rq(ANICCA_P, 0))} {YES} {hanci(ANICCA_H, T, '')}",
        f"{Q(T)} {YES} {Q(f'sự bố thí {BAD}')} {NO}",
        f"{Q(f'{MERIT4} {BAD}')} {NO}",
        f"{NANU(f'sự bố thí {GOOD}')} {YES} {hanci_neg(f'sự bố thí {GOOD}', T)}",
        f"{NANU(f'{MERIT4} {GOOD}')} {YES} {hanci_neg(f'đời sống tu hành trong sạch {GOOD}', T)}",
        f"{Q(T)} {YES} {NANU_VUTTAM}",
        *SUKHO,
        f"{ATTHEVA} {YES} {tena_hi_na(T)}",
        katha_end(N_KUKKU))

    # ==== (18) 9. Anupubbābhisamayakathā ===========================================================================
    head("5-10-10-0", 4, VAGGA)
    head("5-10-10-1-0", 5, f"(18) 9. {katha(N_ANUP)}")
    T = f"có {N_ANUP}"                                         # anupubbābhisamayo (thesis)
    STAGES = [("vào dòng", "thành quả vào dòng"), ("trở lại một lần", "thành quả trở lại một lần"),
              ("không trở lại", "thành quả không trở lại"), ("A-la-hán", "thành quả A-la-hán")]
    add("5-339", *[f"{Q(T)} {YES} {Q(f'dần dần tu tập con đường {m}')} {NO} {Q(f'dần dần tu tập con đường {m}')} {YES} "
                   f"{Q(f'dần dần tự mình chứng nghiệm {f}')} {NO}" for m, f in STAGES])

    C4 = "một phần tư"                                         # catubhāgaṃ (termbase)
    ATT4 = ("đã có được, đã chứng đắc, đã tự mình chứng nghiệm, chứng nhập và an trú, chạm đến bằng thân rồi an trú, "
            f"{C4} không chạm đến bằng thân rồi an trú")
    #   paṭiladdho adhigato sacchikato upasampajja viharati, kāyena phusitvā viharati, catubhāgaṃ na kāyena …

    def head4(x, fruit):
        return f"{C4} là {x}, {C4} không phải là {x}, {C4} đã đạt đến {fruit}, {ATT4}"

    def jah4(items):
        return f"Dứt bỏ {C4} {', '.join(items)}, {TAD}."

    SO, SA, AN = S.PN["sotāpanno"], S.PN["sakadāgāmī"], S.PN["anāgāmī"]
    SO_TAIL = (f"{C4} là {SATTAKKHATTU}, {KOLANKOLO}, {EKABIJI}, được trang bị niềm tin trong sáng không lay chuyển nơi "
               f"Đức Phật, nơi Giáo Pháp{PE} nơi Tăng đoàn{PE} {ARIYAKANTA}, {C4} không có {AK_G}")
    SO_Q = f"Có phải {head4(SO, 'thành quả vào dòng')}, {SO_TAIL} không?"
    REST = f"Bằng việc thấy {DASS['samudaya']}{PE} bằng việc thấy {DASS['nirodha']}{PE} bằng việc thấy {DASS['magga']}, dứt bỏ cái gì?"
    add("5-340",
        f"{kim('dukkha', P_SOTA)} {jah4([SAKKAYA, VICI, SILAB])} {SO_Q} {NO}",
        f"{REST} {jah4([SAKKAYA, VICI, SILAB])} {SO_Q} {NO_PE}")

    KR_OL, BY_OL = f"sự tham đắm dục lạc {ODARIKA}", f"ác ý {ODARIKA}"
    SA_Q = f"Có phải {head4(SA, 'thành quả trở lại một lần')} không?"
    add("5-341",
        f"{kim('dukkha', P_SAKA)} {jah4([KR_OL, BY_OL])} {SA_Q} {NO_PE} {REST[0].lower()}{REST[1:]} "
        f"{jah4([KR_OL, BY_OL])} {SA_Q} {NO_PE}")

    KR_AN, BY_AN = "sự tham đắm dục lạc ở dạng nhỏ nhiệm", "ác ý ở dạng nhỏ nhiệm"
    AN_T = f"{C4} là {ANTARA}{PE} {UPAHACCA}{PE} {ASANKHARA}{PE} {SASANKHARA}{PE} {UDDHAMSOTO}"
    add("5-342",
        f"{kim('dukkha', P_ANAG)} {jah4([KR_AN, BY_AN])} Có phải {head4(AN, 'thành quả không trở lại')}, {AN_T}, "
        f"{C4} không phải là người theo dòng đi lên, không phải là người đi đến cõi Sắc Cứu Cánh không? {NO_PE}",
        f"{REST} {jah4([KR_AN, BY_AN])} Có phải {head4(AN, 'thành quả không trở lại')}, {AN_T}, "
        f"{C4} không phải là {UDDHAMSOTO} không? {NO_PE}")

    RR = RUPARAGA.split(", ") + ["vô minh"]                    # rūparāgaṃ, arūparāgaṃ, mānaṃ, uddhaccaṃ, avijjaṃ
    EPI_PE = f"{PE} ".join(EPI_L[:3]) + f"{PE} " + ", ".join(EPI_L[3:])
    TASKS_PE = ", ".join(TASKS_L[:4]) + f"{PE} {TASKS_L[4]}"
    AR_Q = (f"Có phải {head4(AR, 'trạng thái A-la-hán')}, {C4} {EPI_PE}, {FOUR}, {TASKS_PE}, {C4} điều cần được tự "
            f"mình chứng nghiệm chưa được tự mình chứng nghiệm không?")
    REST_AR = (f"Bằng việc thấy {DASS['samudaya']}{PE} bằng việc thấy {DASS['nirodha']}{PE} bằng việc thấy "
               f"{DASS['magga']}, dứt bỏ cái gì?")
    add("5-343",
        f"{kim('dukkha', P_ARA)} {jah4(RR)} {AR_Q} {NO_PE}",
        f"{REST_AR} {jah4(RR)} {AR_Q} {NO_PE}")

    PATI = "nên gọi là người đang thực hành"                  # paṭipannakoti vattabbo
    PATI_Q = "nên gọi là “người đang thực hành”"              # "paṭipannako"ti vattabbo
    PHALE = "nên gọi là người đứng vững nơi thành quả"        # phale ṭhitoti vattabbo
    NAV = f"không nên nói – “{PHALE}”"                       # na vattabbaṃ – "phale ṭhitoti vattabbo"ti

    def dk(x, pati=PATI):
        return f"trong khi thấy {x}, {pati}"

    def sn(x, tail=PHALE):
        return f"khi {x} đã được thấy, {tail}"

    SN_PE = f"trong khi thấy {SAMU}{PE} trong khi thấy {NIRO}"
    NOTE_S = "[dấu hiệu câu hỏi của người theo học thuyết của chúng ta]"   # [sakavādīpucchālakkhaṇaṃ]
    NOTE_P = "[dấu hiệu câu hỏi của người theo học thuyết khác]"           # [paravādīpucchālakkhaṇaṃ]
    PS = cap(P_SOTA)
    add("5-344",
        f"Có phải {P_SOTA}, {dk(DUK)} không? {YES} {Q(sn(DUK))} {NO} Có phải {SN_PE}, {PATI} không? {YES} "
        f"{Q(sn(NIRO))} {NO}",
        f"Có phải {P_SOTA}, {dk(MAG)}, {sn(MAG)} không? {YES} {Q(f'{dk(DUK)}, {sn(DUK)}')} {NO_PE} "
        f"{q(f'{dk(MAG)}, {sn(MAG)}')} {YES} Có phải {SN_PE}, {PATI}, {sn(NIRO)} không? {NO_PE}",
        f"Có phải {P_SOTA}, {dk(DUK)}, {sn(DUK, NAV)} không? {YES} {Q(f'{dk(MAG)}, {sn(MAG, NAV)}')} {NO_PE} "
        f"có phải trong khi thấy {SAMU}{PE} trong khi thấy {NIRO}, {PATI}, {sn(NIRO, NAV)} không? {YES} "
        f"{Q(f'{dk(MAG, PATI_Q)}, {sn(MAG, NAV)}')} {NO_PE}",
        f"{NOTE_S} Có phải {P_SOTA}, {dk(DUK)}, {sn(DUK, NAV)} không? {YES} {Q('việc thấy khổ đau là vô ích')} {NO_PE} "
        f"có phải trong khi thấy {SAMU}{PE} trong khi thấy {NIRO}, {PATI}, {sn(NIRO, NAV)} không? {YES} "
        f"{Q('việc thấy sự chấm dứt là vô ích')} {NO_PE}")
    assert PS

    def seen_as(x, y, pl=False):
        return f"khi {x} đã được thấy là vô thường, {y} đã được thấy là vô thường"

    NUM = [("bốn", "bốn"), ("tám", "tám"), ("mười hai", "mười hai"), ("bốn mươi bốn", "bốn mươi bốn"),
           ("bảy mươi bảy", "bảy mươi bảy")]
    L6 = []
    for k, (a, b) in enumerate(NUM):
        qq = Q if k == 0 else q
        L6.append(f"{qq(f'tự mình chứng nghiệm thành quả vào dòng bằng {a} hiểu biết')} {YES} "
                  f"{Q(f'có {b} thành quả vào dòng')} {NO_PE}")
    add("5-345",
        f"{NOTE_P} {Q('khi khổ đau đã được thấy, bốn sự thật đã được thấy')} {YES} "
        f"{Q('sự thật về khổ đau là bốn sự thật')} {NO_PE}",
        f"{NOTE_S} {Q(seen_as('khối vật chất', 'năm khối'))} {YES} {Q('khối vật chất là năm khối')} {NO_PE}",
        f"{NOTE_S} {Q(seen_as(S.A['cakkhāyatana'], 'mười hai lĩnh vực nhận biết'))} {YES} "
        f"{Q(S.A['cakkhāyatana'] + ' là mười hai lĩnh vực nhận biết')} {NO_PE}",
        f"{NOTE_S} {Q(seen_as(S.D['cakkhudhātu'], 'mười tám yếu tố'))} {YES} "
        f"{Q(S.D['cakkhudhātu'] + ' là mười tám yếu tố')} {NO_PE}",
        f"{NOTE_S} {Q(seen_as(S.I['cakkhundriya'], 'hai mươi hai năng lực'))} {YES} "
        f"{Q(S.I['cakkhundriya'] + ' là hai mươi hai năng lực')} {NO_PE}",
        f"{NOTE_S} " + " ".join(L6))

    OCEAN = ("“Này các tỳ-khưu, cũng như đại dương thấp xuống tuần tự, nghiêng xuống tuần tự, dốc xuống tuần tự, "
             "không đột ngột là vực thẳm; cũng y như vậy, này các tỳ-khưu, trong Giáo Pháp và Giới Luật này, có sự tu "
             "học tuần tự, việc làm tuần tự, cách thực hành tuần tự, không đột ngột là sự thấu triệt hiểu biết trọn vẹn” "
             f"[Tiểu Phẩm 385; {CIT['a. ni.']} 8.20; Kinh Phật Tự Thuyết 45, và trong Kinh Phật Tự Thuyết].")
    SEE = [("khổ đau", ["sự phát sinh của khổ đau", "sự chấm dứt khổ đau", DUKKHA_CH]),
           ("sự phát sinh của khổ đau", ["khổ đau", "sự chấm dứt khổ đau", DUKKHA_CH]),
           ("sự chấm dứt khổ đau", ["khổ đau", "sự phát sinh của khổ đau", DUKKHA_CH]),
           (DUKKHA_CH, ["khổ đau", "sự phát sinh của khổ đau", "sự chấm dứt khổ đau"])]
    SEE_T = "; ".join(f"ai thấy {a} thì người ấy cũng thấy {b[0]}, cũng thấy {b[1]}, cũng thấy {b[2]}" for a, b in SEE)
    GAVAM = ("Chẳng phải tôn giả trưởng lão Kiều-phạm-ba-đề đã nói với các tỳ-khưu thế này sao – “Này các hiền giả, "
             "điều này tôi đã được nghe trực tiếp từ Đức Thế Tôn, đã được lĩnh hội trực tiếp – ‘Này các tỳ-khưu, "
             f"{SEE_T}’” [{CIT['saṃ. ni.']} 5.1100]!")
    add("5-346",
        f"{na_vattabbam(T)} {YES} {NANU_VUTTAM} {OCEAN} {ATTHEVA} {YES} {tena_hi(T)}",
        f"{na_vattabbam(T)} {YES} {NANU_VUTTAM}",
        *DHP,
        f"{ATTHEVA} {YES} {tena_hi(T)}",
        f"{Q(T)} {YES} {GAVAM} {ATTHEVA} {YES} {tena_hi_na(T)}",
        f"{Q(T)} {YES} {NANU_VUTTAM}",
        *RATANA6,
        f"{ATTHEVA} {YES} {tena_hi_na(T)}",
        nanu_sutta(T, dc("!")),
        katha_end(N_ANUP))

    # ==== (19) 10. Vohārakathā =====================================================================================
    head("5-10-11-0", 4, VAGGA)
    head("5-10-11-1-0", 5, f"(19) 10. {katha(N_VOHARA)}")
    BV = f"lời nói của {BP}"                                   # buddhassa bhagavato vohāro
    T = f"{BV} vượt thế gian"                                  # buddhassa bhagavato vohāro lokuttaro
    LO, LK = "vượt thế gian", "thuộc thế gian"
    add("5-347",
        f"{Q(T)} {YES} Có phải va chạm vào tai {LO}, không phải vào tai {LK}; người ta nhận biết rõ bằng thức {LO}, "
        f"không phải bằng thức {LK}; các đệ tử nhận biết rõ, không phải những {PUTH} không? {NO_PE}",
        f"{NANU(f'{BV} va chạm vào tai {LK}')} {YES} {hanci_neg(f'{BV} va chạm vào tai {LK}', T)}",
        f"{NANU(f'người ta nhận biết rõ {BV} bằng thức {LK}')} {YES} "
        f"{hanci_neg(f'người ta nhận biết rõ {BV} bằng thức {LK}', T)}",
        f"{NANU(f'những {PUTH} nhận biết rõ {BV}')} {YES} {hanci_neg(f'những {PUTH} nhận biết rõ {BV}', T)}")

    LUD = "hiện tượng vượt thế gian"                           # lokuttaro dhammo (termbase)
    EAR_P = "được nhận biết bằng tai, va chạm vào tai, đi vào tầm của tai"
    EAR_N = "không được nhận biết bằng tai, không va chạm vào tai, không đi vào tầm của tai"
    add("5-348",
        f"{Q(T)} {YES} Có phải là con đường, thành quả, Niết-bàn, con đường vào dòng, thành quả vào dòng, con đường trở "
        "lại một lần, thành quả trở lại một lần, con đường không trở lại, thành quả không trở lại, con đường A-la-hán, "
        "thành quả A-la-hán, sự thiết lập tỉnh thức, nỗ lực đúng đắn, nền tảng thần thông, năng lực, sức mạnh, chi phần "
        f"giác ngộ không? {NO_PE}",
        f"{Q(T)} {YES} {Q(f'có ai đó nghe {BV}')} {YES} {Q(f'{LUD} {EAR_P}')} {NO_PE}",
        f"{NANU(f'{LUD} {EAR_N}')} {YES} {hanci_neg(f'{LUD} {EAR_N}', T)}")

    R_P = "khơi dậy sự tham đắm, hấp dẫn, đáng ham muốn, làm say đắm, trói buộc, làm mê mẩn"
    R_N = ("không khơi dậy sự tham đắm, không hấp dẫn, không đáng ham muốn, không làm say đắm, không trói buộc, không "
           "làm mê mẩn")
    D_P = "khơi dậy sự sân hận, khơi dậy sự phẫn nộ, khơi dậy ác cảm"
    D_N = "không khơi dậy sự sân hận, không khơi dậy sự phẫn nộ, không khơi dậy ác cảm"
    M_P = ("khơi dậy sự si mê, tạo ra sự không biết, tạo ra sự không có mắt, làm chấm dứt trí tuệ, thuộc về phía gây "
           "phiền não, không dẫn đến Niết-bàn")
    M_N = ("không khơi dậy sự si mê, không tạo ra sự không biết, không tạo ra sự không có mắt, làm tăng trưởng trí tuệ, "
           "thuộc về phía không gây phiền não, dẫn đến Niết-bàn")
    L349 = []
    for verb, p, n in (("tham đắm vào", R_P, R_N), ("sân hận với", D_P, D_N), ("si mê đối với", M_P, M_N)):
        L349.append(f"{Q(T)} {YES} {Q(f'có ai đó có thể {verb} {BV}')} {YES} {Q(f'{LUD} {p}')} {NO_PE}")
        L349.append(f"{NANU(f'{LUD} {n}')} {YES} {hanci_neg(f'{LUD} {n}', T)}")
    add("5-349", *L349)

    HEAR = f"bất cứ ai nghe {BV}, thì tất cả những người ấy đều tu tập con đường"
    K2 = f"kẻ giết mẹ tu tập con đường{PE} kẻ giết cha{PE} kẻ giết bậc A-la-hán{PE} kẻ làm chảy máu{PE} kẻ chia rẽ Tăng đoàn"
    add("5-350",
        f"{Q(T)} {YES} {Q(HEAR)} {NO_PE}",
        f"{Q(HEAR)} {YES} {Q(f'{BALA} nghe {BV}, {BALA} tu tập con đường')} {NO_PE} "
        f"{q(f'{K2} nghe {BV}, kẻ chia rẽ Tăng đoàn tu tập con đường')} {NO_PE}")

    BOTH = f"cả hiện tượng {LK} lẫn hiện tượng {LO}"         # lokiyampi lokuttarampi dhammaṃ
    add("5-351",
        f"{Q('có thể dùng cây gậy bằng vàng để chỉ ra cả đống thóc lẫn đống vàng')} {YES} "
        f"Cũng vậy, Đức Thế Tôn, bằng lời nói {LO}, nói về {BOTH}.",
        f"{Q('có thể dùng cây gậy bằng gỗ thầu dầu để chỉ ra cả đống thóc lẫn đống vàng')} {YES} "
        f"Cũng vậy, Đức Thế Tôn, bằng lời nói {LK}, nói về {BOTH}.")

    def vh(a, b):                   # a-ṃ voharantassa b hoti
        return f"khi nói về {a}, thì là {b}"

    T2 = f"{BV}, khi nói về điều {LK}, thì {LK}, khi nói về điều {LO}, thì {LO}"
    #   buddhassa bhagavato vohāro lokiyaṃ voharantassa lokiyo hoti, lokuttaraṃ voharantassa lokuttaro hoti
    PAIRS = [("con đường", "con đường"), ("đường sai", "đường sai"), ("thành quả", "thành quả"),
             ("điều không phải thành quả", "điều không phải thành quả"), ("Niết-bàn", "Niết-bàn"),
             ("điều không phải Niết-bàn", "điều không phải Niết-bàn"),
             ("điều do điều kiện tạo thành", "điều do điều kiện tạo thành"),
             ("điều không do điều kiện tạo thành", "điều không do điều kiện tạo thành"), ("vật chất", "vật chất"),
             ("điều phi vật chất", "điều phi vật chất"), ("cảm giác", "cảm giác"),
             ("điều không phải cảm giác", "điều không phải cảm giác"), ("tri giác", "tri giác"),
             ("điều không phải tri giác", "điều không phải tri giác"), ("các tạo tác", "các tạo tác"),
             ("những điều không phải tạo tác", "những điều không phải tạo tác"), ("thức", "thức"),
             ("điều không phải thức", "điều không phải thức")]
    add("5-352",
        f"{Q(T2)} {YES} Có phải khi nói về điều {LK}, thì va chạm vào tai {LK}, khi nói về điều {LO}, thì va chạm vào "
        f"tai {LO}; khi nói về điều {LK}, thì người ta nhận biết rõ bằng thức {LK}, khi nói về điều {LO}, thì người ta "
        f"nhận biết rõ bằng thức {LO}; khi nói về điều {LK}, thì những {PUTH} nhận biết rõ, khi nói về điều {LO}, thì "
        f"các đệ tử nhận biết rõ không? {NO_PE}",
        f"{na_vattabbam(T2)} {YES} {NANU(f'Đức Thế Tôn nói về {BOTH}')} {YES} "
        f"{hanci(f'Đức Thế Tôn nói về {BOTH}', T2)}",
        f"{Q(T2)} {YES} {Q(', '.join(vh(a, b) for a, b in PAIRS))} {NO_PE}",
        katha_end(N_VOHARA))

    # ==== (20) 11. Nirodhakathā ====================================================================================
    head("5-10-12-0", 4, VAGGA)
    head("5-10-12-1-0", 5, f"(20) 11. {katha(N_NIRODHA)}")
    T = f"có hai {N_NIRODHA}"                                  # dve nirodhā
    NS2 = "có hai sự thật về sự chấm dứt"                      # dve nirodhasaccāni
    L1 = (f"{Q(T)} {YES} {Q('có hai sự chấm dứt khổ đau')} {NO_PE} {q('có hai sự chấm dứt khổ đau')} {YES} "
          f"{Q(NS2)} {NO_PE} " + " ".join(f"{q(NS2)} {YES} {Q(f'có hai sự thật về {x}')} {NO_PE}"
                                          for x in ("khổ đau", "sự phát sinh", "con đường")))
    REF = f"có hai nơi che chở{PE} hai nơi ẩn náu{PE} hai nơi nương tựa{PE} hai nơi đến cuối cùng{PE} hai điều bất biến{PE} hai điều bất tử{PE} hai Niết-bàn"
    APP = "các tạo tác đã chấm dứt không do suy xét"           # appaṭisaṅkhāniruddhā saṅkhārā
    PAT = "các tạo tác đã chấm dứt do suy xét"                 # paṭisaṅkhāniruddhā saṅkhārā
    N1 = f"người ta do suy xét làm chấm dứt {APP}"             # appaṭisaṅkhāniruddhe saṅkhāre paṭisaṅkhā nirodhenti
    N2 = f"{APP} cũng bị phá vỡ hoàn toàn, {PAT} cũng bị phá vỡ hoàn toàn"
    ARIYA = "đã chấm dứt nhờ dựa vào con đường cao quý"        # ariyamaggaṃ āgamma niruddhā
    add("5-353",
        L1,
        f"{Q(NS2)} {YES} {Q(REF)} {NO_PE}",
        f"{Q('có hai Niết-bàn')} {YES} {Q('giữa hai Niết-bàn có sự cao thấp, sự thấp kém và ưu việt, sự hơn kém, hoặc ranh giới, hoặc sự phân chia, hoặc đường vạch, hoặc khoảng cách')} {NO_PE}",
        f"{Q(T)} {YES} {NANU(N1)} {YES} {hanci_neg(N1, T)}",
        f"{na_vattabbam(T)} {YES} {NANU(N2)} {YES} {hanci(N2, T)}",
        f"{Q(T)} {YES} Có phải {PAT} cũng{var('?', 'paṭisaṅkhāniruddhā')} {ARIYA} không? {YES} "
        f"{Q(f'{APP} {ARIYA}')} {NO_PE}",
        f"{Q(T)} {YES} {Q(f'{PAT} không sinh khởi lại')} {YES} {Q(f'{APP} không sinh khởi lại')} {NO_PE} "
        f"vậy thì không nên nói – “{T}”.",
        katha_end(N_NIRODHA),
        VAGGA + ".",
        tassuddanam,
        *UDDANA)
    return segs


# ---------------------------------------------------------------------------------------------------------------
# Checks and writer (S's per-line checks; quote balance also allows a verse stanza re-opening with ‘ inside an open
# ‘…’ quote, as the Pāli does in ^5-333, where only the last stanza closes)
# ---------------------------------------------------------------------------------------------------------------
def quotes_ok(text):
    lines = text.split("\n")
    body = []
    for k, ln in enumerate(lines):
        prev = "\n".join(body)
        if k and ln.startswith("“") and prev.count("“") > prev.count("”"):
            ln = ln[1:]
        elif k and ln.startswith("‘") and prev.count("‘") > prev.count("’"):
            ln = ln[1:]
        body.append(ln)
    b = "\n".join(body)
    return b.count("“") == b.count("”") and b.count("‘") == b.count("’")


def check_against_pali(name, segs):
    orig = S.quotes_ok
    try:
        S.quotes_ok = quotes_ok
        S.check_against_pali(name, segs)
    finally:
        S.quotes_ok = orig


def write(name, segs):
    check_against_pali(name, segs)
    text = unicodedata.normalize("NFC", "\n\n".join("\n".join(s) for s in segs) + "\n")
    assert "\n\n\n" not in text and "\r" not in text and "«" not in text and "»" not in text
    assert "là là" not in text and "được được" not in text
    (S.OUT_DIR / name).write_text(text, encoding="utf-8", newline="\n")
    print("wrote", S.OUT_DIR / name)
    adh = S.ROOT / "0-INBOX/temp/pipeline/pi-5-vi-ai/rails/adh-10"      # termbase-adherence copy (byte-identical)
    adh.mkdir(exist_ok=True)
    (adh / name).write_bytes((S.OUT_DIR / name).read_bytes())
    print("wrote", adh / name)


def check_reused():
    texts = {}
    for b, d in S.RAILS.items():
        texts[b] = unicodedata.normalize(
            "NFC", "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md")))).lower()
    bad = [(v, b) for v, b in REUSED if unicodedata.normalize("NFC", v).lower() not in texts[b]]
    assert not bad, "reused strings not found in their rails: " + repr(bad)
    for fn, strs in (("2-parihanikatha.md", CH2_STR), ("3-brahmacariyakatha.md", CH3_STR),
                     ("4-jahatikatha.md", [JATI8])):
        t = unicodedata.normalize("NFC", (S.OUT_DIR / fn).read_text(encoding="utf-8")).lower()
        bad = [v for v in strs if v.lower() not in t]
        assert not bad, f"strings not found in {fn}: " + repr(bad)


def tassuddanam():
    """The fixed "Tassuddānaṃ –" string: chapter 9's, byte for byte, if chapter 9 is finished; else the default."""
    out = S.OUT_DIR / CH9
    if not out.exists():
        print("chapter 9 not finished: Tassuddānaṃ – =", TASSUDDANAM)
        return TASSUDDANAM
    pl = [x for x in (S.PALI_DIR / CH9).read_text(encoding="utf-8").splitlines() if x.strip()]
    vl = [x for x in out.read_text(encoding="utf-8").splitlines() if x.strip()]
    s = vl[pl.index("Tassuddānaṃ –")]
    print("chapter 9 finished: Tassuddānaṃ – =", s)
    return s


def lookup():
    tb = {}
    for ln in TB.read_text(encoding="utf-8").splitlines():
        if ": {" in ln:
            tb[ln.split(": {", 1)[0]] = ln
    tbl = {k.lower(): v for k, v in tb.items()}
    seen = set()
    for line in KW.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        i, body = line.split("] ", 1)
        i = i[1:]
        ok = i.startswith("5-10-") or (re.fullmatch(r"5-\d+", i) and 307 <= int(i[2:]) <= 353)
        if not ok:
            continue
        for k in body.split(", "):
            for kk in k.split(" / "):
                if kk.lower() in seen:
                    continue
                seen.add(kk.lower())
                e = tb.get(kk) or tbl.get(kk.lower())
                print(f"[{i}] {e if e else kk + ': <NOT IN TERMBASE>'}")


def main():
    S.check_reused()
    check_reused()
    write(NAME, build_ch10(tassuddanam()))


if __name__ == "__main__":
    if "--lookup" in sys.argv:
        lookup()
    else:
        main()
