# -*- coding: utf-8 -*-
"""pi-5 (Kathāvatthu) Vietnamese zero-shot, chapter 23: 23-pannarasamavaggo.md (Pannarasamavaggo, ^5-23-0 … ^5-742),
the eleven kathā (145)-(155) of the fifteenth vagga, its uddāna, the close of the third fifty-group and its uddāna.

Imports the approved sample builder (build_sample_vi, read-only) for every debate frame and the finished chapter
builders build_2_vi / build_4_vi / build_9_vi / build_12_vi / build_14_vi / build_15_vi (read-only, importing writes
nothing) for persons, paths and fruits, the path / fruit / Niết-bàn list, the poison formula, the dependent-origination
clauses and the vagga close, so every repeat is byte-identical with those chapters. The condition names follow ch13
(build_13_vi PC: hetu- / ārammaṇa- / adhipati- / anantara- / samanantarapaccaya). Every string claimed from the
pi-1..4 Vietnamese rails is asserted to occur there, every string taken from a finished pi-5 chapter is asserted to
occur in that chapter's output; the sample's per-line checks (IDs, dashes, quotes, NFC, foreign letters) are run
against the Pāli. Every Pāli sentence keeps its own sentence.

run:  python -I -B -X utf8 build_23_vi.py
"""
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai")
import build_sample_vi as B  # noqa: E402
import build_2_vi as C2      # noqa: E402  (persons, fruits, DEV6, kilesa words)
import build_4_vi as C4      # noqa: E402  (path names, anāsava / sāsava)
import build_9_vi as C9      # noqa: E402  (vagga close: Tassuddānaṃ –)
import build_12_vi as C12    # noqa: E402  (path / fruit / Niết-bàn list, poison formula, L10 list)
import build_13_vi as C13    # noqa: E402  (condition names PC)
import build_15_vi as C15    # noqa: E402  (hanci_no / hanci_yes / nanu_l, vipāka, jarāmaraṇa)

NAME = "23-pannarasamavaggo.md"
Q, q, NANU, AM, cap, chain = B.Q, B.q, B.NANU, B.AMANTA, B.cap, B.chain
NH, NHP = B.NA_HEVAM, B.NA_HEVAM_PE
NVQ, TENA_HI, TENA_HI_NA = B.NA_VATTABBAM_Q, B.TENA_HI, B.TENA_HI_NA
NANU_VUTTAM, ATTHEVA = B.NANU_VUTTAM, B.ATTHEVA
SPELL = B.SPELL
hanci_no, hanci_yes, nanu_l = C15.hanci_no, C15.hanci_yes, C15.nanu_l
VAGGA15 = B.VAGGA[15]                                     # Pannarasamavaggo = «Chương thứ mười lăm» (terms file)
K = B.KATHA.format
E = B.KATHA_END.format
NATTHI = "Không có."                                      # Natthi. (answer, ch11 / ch12)


def heads(n, num, title):
    """#### Pannarasamavaggo ^5-23-n-0 / ##### (num) n. <title> ^5-23-n-1-0"""
    return [(4, VAGGA15, f"5-23-{n}-0"), (5, f"({num}) {n}. {title}", f"5-23-{n}-1-0")]


def navq_open(x):
    """Na vattabbaṃ – "X…ti? with the Pāli's quote left open (ch10 ^5-396 precedent)"""
    return f"Có phải không nên nói – “{x} không?"


# ================================================================ (145) Paccayatā
PACCAYATA = "tính chất làm điều kiện"                     # paccayatā (terms file heading (145); ch13 PC)
VAV = "được xác định riêng biệt"                          # vavatthita (pi-2 vavatthapeti «xác định»)
T1 = f"{PACCAYATA} {VAV}"                                 # paccayatā vavatthitā
PN = {k: C13.PC[i][len("tính chất làm "):] for i, k in enumerate(("hetu", "ārammaṇa", "adhipati", "anantara",
                                                                    "samanantara"))}
# hetu- / ārammaṇa- / adhipati- / anantara- / samanantarapaccaya = «điều kiện nguyên nhân / đối tượng / chi phối /
# kế cận / kế cận liền ngay» (ch13 PC, byte for byte after «tính chất làm»)
PN.update({"sahajāta": "điều kiện cùng sinh",             # sahajātapaccaya (sahajāta «cùng sinh» ch15, ch17)
           "indriya": "điều kiện năng lực",               # indriyapaccaya (indriya «năng lực» core)
           "magga": "điều kiện con đường",                # maggapaccaya (magga «con đường» core)
           "āhāra": "điều kiện dưỡng chất",               # āhārapaccaya (āhāra «dưỡng chất» pi-2, ch13)
           "āsevana": "điều kiện thực hành"})             # āsevanapaccaya (āsevanā «sự thực hành» pi-1 ^1-1361)


def pp(k):
    """X-paccayena paccayo (hoti)"""
    return f"làm điều kiện theo {PN[k]}"


def pq(a, b):
    """"A-paccayena paccayo, B-paccayena paccayo" (quoted)"""
    return f"{pp(a)}, {pp(b)}"


VIM, CHANDA, VIRIYA, CITTA = "sự thẩm xét", "ý muốn", "tinh tấn", "tâm"   # vīmaṃsā / chanda / vīriya / citta (pi-1)
HETU = "nguyên nhân"                                      # hetu (the word of hetupaccaya, ch13; pi-1 core «gốc rễ»: for review)
ADH = "yếu tố chi phối"                                   # adhipati (the word of adhipatipaccaya, ch13)
SAHA = "các hiện tượng cùng sinh"                         # sahajātā dhammā (ch15 sahajāta)


def adh(x):
    """X-ādhipati sahajātānaṃ dhammānaṃ adhipati"""
    return f"{x} chi phối là {ADH} của {SAHA}"


AND_IND = "và nó là năng lực"                             # tañca indriyaṃ (ch13 «và nó là»)
AND_MAG = "và nó là chi phần của con đường"               # tañca maggaṅgaṃ (maggaṅga pi-1 ^1-283)
AND_AHA = "và nó là dưỡng chất"                           # so ca āhāro
ARIYA = ("sự xem xét lại sinh khởi sau khi trân trọng hiện tượng cao quý, và nó là đối tượng")
# ariyaṃ dhammaṃ garuṃ katvā uppajjati paccavekkhaṇā, tañcārammaṇaṃ (paccavekkhaṇā pi-1 apaccavekkhaṇā; garuṃ katvā
# pi-4 «sự trân trọng»; ariyadhamma «hiện tượng cao quý» ch15)
KIRIYA = "không xác định về mặt đạo đức mang tính chức năng"   # kiriyābyākata (pi-1 ^1-1068, ch20 KIRA)


def prior(kind):
    """purimā purimā X dhammā pacchimānaṃ pacchimānaṃ X-ānaṃ dhammānaṃ anantarapaccayena paccayo, sā ca āsevanā"""
    return (f"từng hiện tượng {kind} trước làm điều kiện cho từng hiện tượng {kind} sau theo {PN['anantara']}, "
            "và nó là sự thực hành")


# ================================================================ (146) Aññamaññapaccaya
KX2 = "điều kiện lẫn nhau"                                # Aññamaññapaccayakathā
AV, SK = "vô minh", "các sự tạo tác"                      # avijjā / saṅkhārā (pi-2 ^2-225 plural)
SK1 = "sự tạo tác"                                        # saṅkhārena (singular, pi-2 Abhidhammabhājaniya)
TA, UP = "khao khát", "sự bám víu"                        # taṇhā / upādānaṃ (core, pi-2)


def cond(a, b, api=False):
    """A-paccayā B (A làm điều kiện cho B); A-paccayāpi B = A cũng làm điều kiện cho B (pi-2 ^2 Abhidhamma)"""
    return f"{a} {'cũng ' if api else ''}làm điều kiện cho {b}"


ONLY_AV = f"chỉ {cond(AV, SK)}"                           # avijjāpaccayāva saṅkhārā (aṭṭhakathā: avijjāva … paccayo)
ONLY_TA = f"chỉ {cond(TA, UP)}"                           # taṇhāpaccayāva upādānaṃ
REV_AV = cond(SK, AV, True)                               # saṅkhārapaccayāpi avijjā
REV_TA = cond(UP, TA, True)                               # upādānapaccayāpi taṇhā
BOTH_AV = f"{cond(AV, SK, True)}, {REV_AV}"               # avijjāpaccayāpi saṅkhārā, saṅkhārapaccayāpi avijjā
BOTH_TA = f"{cond(TA, UP, True)}, {REV_TA}"               # taṇhāpaccayāpi upādānaṃ, upādānapaccayāpi taṇhā
JM = C15.JM                                               # jarāmaraṇa = «sự lão hóa và sự chết» (pi-2, ch15)
S_JATI = f"“Này các tỳ-khưu, {cond(JM, 'sự sinh')}, {cond('sự sinh', 'sự hiện hữu')}”"
# "Jarāmaraṇapaccayā, bhikkhave, jāti, jātipaccayā bhavo"ti (vocative fronted as ch14)
NR = "phần tinh thần và vật chất"                         # nāmarūpa (pi-2)
S_NAMA = (f"“Này các tỳ-khưu, {cond('thức', NR)}, {cond(NR, 'thức', True)}” "
          "[Trường Bộ Kinh 2.58, nhưng hơi khác một chút]")
# "Viññāṇapaccayā, bhikkhave, nāmarūpaṃ, nāmarūpapaccayāpi viññāṇa"nti [dī. ni. 2.58, thokaṃ pana visadisaṃ]
SUTTA_Q = "– có bài kinh như vậy thật không?"            # "X" – attheva suttantoti? (ch14)


def only_line(only, rev):
    return f"{only}, không nên nói – “{rev}”"


# ================================================================ (147) Addhā / (148) Khaṇa laya muhutta
ADDHA = "thời gian"                                       # addhā (aṭṭhakathā: kālasaṅkhāto addhā)
PARI = "được hình thành trọn vẹn"                         # parinipphanna (ch19)
TT = {"a": "quá khứ", "f": "tương lai", "p": "hiện tại"}  # atīta / anāgata / paccuppanna (ch5, ch17)
KH5 = f"{B.RUPA}, {B.VEDANA}, {B.SANNA}, {B.SANKHARA}, {B.VINNANA}"   # rūpaṃ vedanā saññā saṅkhārā viññāṇaṃ (pi-2)


def addha(t=None):
    return f"{ADDHA} {TT[t]}" if t else ADDHA


def rupa_chain():
    """Rūpanti? Na hevaṃ vattabbe…pe… vedanā…pe… saññā…pe… saṅkhārā…pe… viññāṇanti? Na hevaṃ vattabbe…pe…"""
    return (f"{Q(f'là {B.RUPA}')} {NHP} {B.VEDANA}… {B.SANNA}… {B.SANKHARA}… {q(f'là {B.VINNANA}')} {NHP}")


COUNTS = [("năm khối", "mười lăm"), ("mười hai lĩnh vực nhận biết", "ba mươi sáu"),
          ("mười tám yếu tố", "năm mươi bốn"), ("hai mươi hai năng lực", "sáu mươi sáu")]
# pañcakkhandhā / dvādasāyatanāni / aṭṭhārasa dhātuyo / bāvīsatindriyāni; pannarasa … chasaṭṭhi (ch17 ^5-569)
S3 = ("“Này các tỳ-khưu, có ba chủ đề bàn luận này! Ba điều nào? Này các tỳ-khưu, hoặc người ta có thể bàn luận về "
      f"{addha('a')} – ‘trong {addha('a')} đã là như vậy’; này các tỳ-khưu, hoặc người ta có thể bàn luận về "
      f"{addha('f')} – ‘trong {addha('f')} sẽ là như vậy’; này các tỳ-khưu, hoặc người ta có thể bàn luận về "
      f"{addha('p')} bây giờ – ‘bây giờ, trong hiện tại là như vậy’. Này các tỳ-khưu, đây là ba chủ đề bàn luận”")
# tīṇimāni, bhikkhave, kathāvatthūni! Katamāni tīṇi? Atītaṃ vā, bhikkhave, addhānaṃ ārabbha kathaṃ katheyya – ‘evaṃ
# ahosi atītamaddhāna’nti; … Imāni kho, bhikkhave, tīṇi kathāvatthūnī (Katamāni pañca? «Năm điều nào?» ch15)
KH, LA, MU = "khoảnh khắc", "chốc lát", "thời khắc"       # khaṇa (ch10 uppādakkhaṇa) / laya / muhutta
KX4 = f"{KH}, {LA}, {MU}"                                 # Khaṇalayamuhuttakathā

# ================================================================ (149) Āsava / (150) Jarāmaraṇa
ASAVA = "ô nhiễm"                                         # āsava (core)
ANS, SAS = C4.POS[4], C4.NEG[4]                           # anāsava / sāsava «không phải là / là đối tượng của ô nhiễm»
T5 = f"bốn {ASAVA} {ANS}"                                 # cattāro āsavā anāsavā
MPN = f"là {C12.L40_PE}"                                  # Maggo phalaṃ nibbānaṃ, sotāpattimaggo sotāpattiphalaṃ…pe… bojjhaṅgo (ch10, ch12)
OTHER = f"có những {ASAVA} khác mà bằng các {ASAVA} ấy, những {ASAVA} kia {SAS}"
# atthaññeva āsavā yehi āsavehi te āsavā sāsavā honti (ch20 «mà bằng … ấy»)
LT, LK = "vượt thế gian", "thuộc thế gian"                # lokuttara / lokiya (pi-1)
T6 = f"{JM} của các hiện tượng {LT} là {LT}"              # lokuttarānaṃ dhammānaṃ jarāmaraṇaṃ lokuttaraṃ
MG = {"so": C4.SOTAPATTIMAGGA, "sa": C4.SAKADAGAMIMAGGA, "an": C4.ANAGAMIMAGGA, "ar": C12.MG_AR}
FR = {"so": C2.FRUIT[C2.SO], "sa": C2.FRUIT[C2.SA], "an": C2.FRUIT[C2.AN], "ar": C12.FR_AR}
DEV6, SING6 = C2.DEV6, C12.SING6


def jm(x, y=None):
    """X-assa jarāmaraṇaṃ X (sotāpattimaggassa jarāmaraṇaṃ sotāpattimaggo)"""
    return f"{JM} của {x} là {y or x}"


# ================================================================ (151)-(153) Saññāvedayita
SVN = "thành tựu thiền chấm dứt tri giác và cảm giác"    # saññāvedayitanirodhasamāpatti (pi-2 ^2 ñāṇavibhaṅga)
SVP = "người đang nhập sự chấm dứt tri giác và cảm giác"  # saññāvedayitanirodhaṃ samāpanno (pi-2; ch16 nirodhaṃ samāpanna)
KX7 = "tri giác và cảm giác"                              # Saññāvedayitakathā (as written; vedayita «cảm giác» pi-2)
T7, T8 = f"{SVN} là {LT}", f"{SVN} là {LK}"              # … lokuttarā / lokiyā
PL = {"k": "thuộc cõi dục lạc", "r": "thuộc cõi hình sắc", "a": "thuộc cõi không hình sắc"}
# kāmāvacarā / rūpāvacarā / arūpāvacarā (pi-1, ch15, ch20)
T9 = f"{SVP} có thể qua đời"                              # … kālaṃ kareyya (kālakiriyā «sự qua đời» pi-2; ch20 «có thể»)
T9N = f"{SVP} không thể qua đời"                          # … na kālaṃ kareyya
MR = ", ".join(f"{x} lúc lâm chung" for x in ("sự tiếp xúc", "cảm giác", "tri giác", "chủ ý", "tâm"))
# māraṇantiyo phasso, māraṇantiyā vedanā … māraṇantiyaṃ cittaṃ
PV = "sự tiếp xúc, cảm giác, tri giác, chủ ý, tâm"        # phasso vedanā saññā cetanā cittaṃ (core)
NO_P, NO_V, NO_C = "người không có sự tiếp xúc", "người không có cảm giác", "người không có tâm"   # aphassaka …
HAS_P, HAS_C = "người có sự tiếp xúc", "người có tâm"     # saphassaka / sacittaka (ch11 saphassa «có sự tiếp xúc»)
BODY = f"thân của {SVP}"                                  # saññāvedayitanirodhaṃ samāpannassa kāye
POISON = C12.poison(BODY)                                 # visaṃ kameyya, satthaṃ kameyya, aggi kameyya (ch5, ch12)
NPOISON = (f"chất độc không thể tác động lên {BODY}, dao kiếm không thể tác động, lửa không thể tác động")
NY = "sự cố định"                                         # niyāma (ch13, ch14)
CS = "người có được thức qua mắt"                         # cakkhuviññāṇasamaṅgī (ch18)


def niy(who, neg=False):
    """(n)atthi so niyāmo yena niyāmena niyato X na kālaṃ kareyya"""
    return f"{'không có' if neg else 'có'} {NY} mà do được cố định bằng {NY} ấy, {who} không thể qua đời"


# ================================================================ (154) Asaññasattupika
ASS = "hướng đến cõi chúng sinh Vô Tưởng"                 # asaññasattupika (ch11 / ch16 «chúng sinh Vô Tưởng»)
KX10 = f"điều {ASS}"                                      # Asaññasattupikakathā
T10 = f"{SVN} {ASS}"
KM = ("sự không tham lam, tức gốc rễ thiện, sự không sân hận, tức gốc rễ thiện, sự không si mê, tức gốc rễ thiện, "
      "niềm tin, sự tinh tấn, sự tỉnh thức, sự định tâm, trí tuệ")
# alobho kusalamūlaṃ … saddhā vīriyaṃ sati samādhi paññā (pi-1 ^1-32 «sự không tham lam, tức gốc rễ thiện»; ch12 list)
KM_PE = "sự không tham lam, tức gốc rễ thiện, sự không sân hận, tức gốc rễ thiện… trí tuệ"
BHAV = "tu tập con đường"                                 # maggabhāvanā (ch18 «sự tu tập con đường»; ch3 maggaṃ bhāveti)
IDHA = "ở đây cũng không có tri giác, ở đó cũng không có tri giác"   # idhāpi asaññī tatrāpi asaññī (ch11 asañña)

# ================================================================ (155) Kammūpacaya
KAMMA = "nghiệp"                                          # kamma (pi-1)
KU = "sự tích lũy nghiệp"                                 # kammūpacaya (upacita «tích lũy» pi-1)
T11 = f"{KAMMA} là khác, {KU} là khác"                    # aññaṃ kammaṃ añño kammūpacayo (terms file «X là khác, Y là khác»)
L11 = C12.L10 + [C2.R]                                    # phassa … paññā (ch12 L10), rāga (ch2)
VIP = C15.VIP                                             # vipāko / kammavipāko = «quả của nghiệp» (pi-1, ch15)


def upa(x):
    """X-ūpacaya = «sự tích lũy X» (a leading «sự» of X dropped)"""
    return f"sự tích lũy {x[len('sự '):] if x.startswith('sự ') else x}"


def other(x):
    return f"{x} là khác, {upa(x)} là khác"


KU_SA = f"{KU} cùng sinh với nghiệp"                      # kammūpacayo kammena sahajāto


def ved(kind, f):
    """X-ena kammena … Y-āya vedanāya sampayuttena kammena sahajāto kammūpacayo Y-āya vedanāya sampayutto"""
    return f"{KU} cùng sinh với nghiệp gắn liền với cảm giác {f} là gắn liền với cảm giác {f}"


ADUK = "không khó chịu cũng không dễ chịu"                # adukkhamasukha (pi-1)


def ved_line(kind):
    first = f"{KU} cùng sinh với nghiệp {kind} là {kind}"
    return (f"{Q(first)} {AM} {Q(ved(kind, 'dễ chịu'))} {NHP} cảm giác khó chịu… {q(ved(kind, ADUK))} {NHP}")


def kc(x, rest):
    """X cittena sahajāto, …"""
    return f"{x} cùng sinh với tâm, {rest}"


BREAK = "khi tâm đang tan rã thì"                         # cittaṃ bhijjamānaṃ (ch16 «khi … đang tan rã, thì tan rã»)
IN_K = f"{KU} ở trong nghiệp"                             # kammamhi kammūpacayo
FROM_K = f"{IN_K}, từ {KU}, {VIP} phát sinh"              # …, kammūpacayato vipāko nibbattati (nibbattati ch19)
SAB = "vừa gây hại vừa không gây hại"                     # sabyābajjhampi abyābajjhampi
SUTTA_P = (
    f"“Này Pun-na, ở đây, có người tạo tác sự tạo tác bằng thân {SAB} [{SPELL} (Ka.): sabyāpajjhampi "
    f"abyāpajjhampi; cần xem Trung Bộ Kinh 2.81], tạo tác sự tạo tác bằng lời nói {SAB}… tạo tác sự tạo tác bằng ý, "
    f"người ấy, sau khi tạo tác sự tạo tác bằng thân {SAB}, sự tạo tác bằng lời nói {SAB}… sự tạo tác bằng ý, thì "
    f"tái sinh vào một thế giới {SAB}. Khi người ấy đã tái sinh vào thế giới {SAB}, các sự tiếp xúc {SAB} chạm đến "
    f"người ấy. Người ấy, khi bị các sự tiếp xúc {SAB} chạm đến, cảm nhận cảm giác {SAB}, xen lẫn dễ chịu và khó "
    "chịu, ví như loài người, một số vị trời và một số chúng sinh ở cõi đọa lạc. Này Pun-na, như vậy, từ chúng sinh "
    "mà có sự tái sinh của chúng sinh, người ta làm điều gì thì do điều ấy mà tái sinh, khi đã tái sinh thì các sự "
    "tiếp xúc chạm đến người ấy. Này Pun-na, vì vậy Ta nói ‘chúng sinh là người thừa kế của nghiệp’” "
    "[Trung Bộ Kinh 2.81]")
# idha, puṇṇa, ekacco sabyābajjhampi abyābajjhampi [sabyāpajjhampi abyāpajjhampi (ka.) ma. ni. 2.81 passitabbaṃ]
# kāyasaṅkhāraṃ abhisaṅkharoti … Evampāhaṃ, puṇṇa, ‘kammadāyādā sattā’ti vadāmī (kāya- / vacīsaṅkhāra pi-2;
# upapajjati «tái sinh» coordinator; vokiṇṇasukhadukkha: feeling sense «dễ chịu / khó chịu» pi-1; passitabbaṃ
# «cần xem» ch10, ch17)

# ================================================================ vagga close and the third fifty-group
UDDANA = (f"{cap(T1)}, sự sinh khởi tùy thuộc vào điều kiện, {ADDHA}, {KX4}, {T5}, {T6}, {T7}, {T8}, {T9}, "
          f"chính điều ấy là con đường để tái sinh vào cõi chúng sinh Vô Tưởng, {T11}.")
# Paccayatā vavatthitā, paṭiccasamuppādo, addhā, khaṇo layo muhuttaṃ, cattāro āsavā anāsavā, lokuttarānaṃ dhammānaṃ
# jarāmaraṇaṃ lokuttarā, saññāvedayitanirodhasamāpatti lokuttarā, … lokiyā, saññāvedayitanirodhaṃ samāpanno kālaṃ
# kareyya, sveva maggo asaññasattupapattiyā, aññaṃ kammaṃ añño kammūpacayoti. (paṭiccasamuppāda pi-1 core, ch14)
TATIYO_PANNASAKO = "Nhóm năm mươi thứ ba."                # Tatiyo paṇṇāsako. (coordinator «Dutiyo paṇṇāsako.» pattern)
UDDANA50 = f"Các khuynh hướng tiềm ẩn, sự phòng hộ, kiếp, gốc rễ, và điều {VAV}."
# Anusayā, saṃvaro, kappo, mūlañca vavatthitāti. (first kathā of vaggas 11-15: anusaya ch19, saṃvara ch20, kappa
# core «kiếp», kusalamūla «gốc rễ» ch22 / pi-1, vavatthitā this chapter; ca = và, as ch18)


def build():
    d = B.Doc()
    d.head(3, VAGGA15, "5-23-0")
    # ------------------------------------------------------------ (145) Paccayatā
    d.head(4, f"(145) 1. {K(x=PACCAYATA)}", "5-23-1-0")
    vh = f"{VIM} là {HETU}, và nó là {ADH}"
    d.seg("5-711",
          f"{Q(T1)} {AM} {NANU(vh)} {AM} {hanci_yes(vh, pq('hetu', 'adhipati'))}",
          f"{NANU(adh(CHANDA))} {AM} {hanci_yes(adh(CHANDA), pq('adhipati', 'sahajāta'))}")

    def adh_seg(sid, x, extras):
        lines = [f"{NANU(adh(x))} {AM} {hanci_yes(adh(x), pq('adhipati', 'sahajāta'))}"]
        for extra, k in extras:
            p = f"{adh(x)}, {extra}"
            lines.append(f"{NANU(p)} {AM} {hanci_yes(p, pq('adhipati', k))}")
        d.seg(sid, *lines)

    adh_seg("5-712", VIRIYA, [(AND_IND, "indriya"), (AND_MAG, "magga")])
    adh_seg("5-713", CITTA, [(AND_AHA, "āhāra"), (AND_IND, "indriya")])
    adh_seg("5-714", VIM, [(AND_IND, "indriya"), (AND_MAG, "magga")])
    d.seg("5-715", f"{NANU(ARIYA)} {AM} {hanci_yes(ARIYA, pq('adhipati', 'ārammaṇa'))}")
    d.seg("5-716", *(f"{NANU(prior(k))} {AM} {hanci_yes(prior(k), pq('anantara', 'āsevana'))}"
                     for k in ("thiện", "bất thiện", KIRIYA)))
    d.seg("5-717",
          f"{NVQ(T1)} {AM} {Q(', '.join(pp(k) for k in ('hetu', 'ārammaṇa', 'anantara', 'samanantara')))} {NH} "
          f"{TENA_HI(T1)}",
          E(x=PACCAYATA))
    # ------------------------------------------------------------ (146) Aññamaññapaccaya
    for lv, t, sid in heads(2, 146, K(x=KX2)):
        d.head(lv, t, sid)
    na = f"{AV} cùng sinh với {SK1}"
    nt = f"{TA} cùng sinh với {UP}"
    d.seg("5-718",
          f"{Q(only_line(ONLY_AV, REV_AV))} {AM} {NANU(na)} {AM} {hanci_yes(na, BOTH_AV)}",
          f"{Q(only_line(ONLY_TA, REV_TA))} {AM} {NANU(nt)} {AM} "
          f"{hanci_yes(nt, BOTH_TA)}")
    d.seg("5-719",
          f"{S_JATI} {SUTTA_Q} {NATTHI} {TENA_HI(only_line(ONLY_AV, REV_AV))} {cap(only_line(ONLY_TA, REV_TA))}.",
          f"{S_NAMA} {SUTTA_Q} {AM} Vậy thì {BOTH_AV}; {BOTH_TA}.",
          E(x=KX2))
    # ------------------------------------------------------------ (147) Addhā
    for lv, t, sid in heads(3, 147, K(x=ADDHA)):
        d.head(lv, t, sid)
    l1 = [f"{Q(f'{addha()} {PARI}')} {AM} {rupa_chain()}"]
    for t in ("a", "f", "p"):
        l1.append(f"{q(f'{addha(t)} {PARI}')} {AM} {rupa_chain()}")
    l2 = []
    for i, t in enumerate(("a", "f", "p")):
        l2.append(f"{(Q if i == 0 else q)(f'{KH5} thuộc {TT[t]} là {addha(t)}')} {AM} "
                  f"{Q(f'có năm {addha(t)}')} {NHP}")
    lines = [" ".join(l1), " ".join(l2)]
    for items, total in COUNTS:
        x = ", ".join(f"{items} thuộc {TT[t]} là {addha(t)}" for t in ("a", "f", "p"))
        lines.append(f"{Q(x)} {AM} {Q(f'có {total} {ADDHA}')} {NHP}")
    d.seg("5-720", *lines)
    t3 = f"{ADDHA} {PARI}"
    d.seg("5-721",
          f"{navq_open(t3)} {AM} {NANU_VUTTAM} {S3} [Tăng Chi Bộ Kinh 3.68; Trường Bộ Kinh 3.305]. {ATTHEVA} {AM} "
          f"{TENA_HI(t3)}",
          E(x=ADDHA))
    # ------------------------------------------------------------ (148) Khaṇa laya muhutta
    for lv, t, sid in heads(4, 148, K(x=KX4)):
        d.head(lv, t, sid)
    d.seg("5-722",
          f"{Q(f'{KH} {PARI}, {LA} {PARI}, {MU} {PARI}')} {AM} {Q(f'là {B.RUPA}')} {NHP} {B.VEDANA}… {B.SANNA}… "
          f"{B.SANKHARA}… {q(f'là {B.VINNANA}')} {NHP}")
    t4 = f"{MU} {PARI}"
    d.seg("5-723",
          f"{navq_open(t4)} {AM} {NANU_VUTTAM} {S3}. {ATTHEVA} {AM} {TENA_HI(t4)}",
          E(x=KX4))
    # ------------------------------------------------------------ (149) Āsava
    for lv, t, sid in heads(5, 149, K(x=f"các {ASAVA}")):
        d.head(lv, t, sid)
    d.seg("5-724", f"{Q(T5)} {AM} {Q(MPN)} {NHP}")
    d.seg("5-725",
          f"{navq_open(T5)} {AM} {Q(OTHER)} {NH} {TENA_HI(T5)}",
          E(x=f"các {ASAVA}"))
    # ------------------------------------------------------------ (150) Jarāmaraṇa
    for lv, t, sid in heads(6, 150, K(x=JM)):
        d.head(lv, t, sid)
    devs = "… ".join(f"của {x}" for x in DEV6[:5])
    d.seg("5-726",
          f"{Q(T6)} {AM} {Q(MPN)} {NHP} {q(jm(MG['so']))} {NHP} {q(jm(MG['so']))} {AM} {Q(jm(FR['so']))} {NHP} "
          f"của {MG['sa']}… của {FR['sa']}… của {MG['an']}… của {FR['an']}… {q(jm(MG['ar']))} {NHP} "
          f"{q(jm(MG['ar']))} {AM} {Q(jm(FR['ar']))} {NHP} {devs}… {q(jm(DEV6[5], SING6[5]))} {NHP}")
    d.seg("5-727",
          f"{navq_open(T6)} {AM} {Q(f'là {LK}')} {NH} {TENA_HI(f'là {LT}')}",
          E(x=JM))
    # ------------------------------------------------------------ (151) Saññāvedayita
    for lv, t, sid in heads(7, 151, K(x=KX7)):
        d.head(lv, t, sid)
    d.seg("5-728", f"{Q(T7)} {AM} {Q(MPN)} {NHP}")
    d.seg("5-729",
          f"{navq_open(T7)} {AM} {Q(f'là {LK}')} {NH} {TENA_HI(f'là {LT}')}",
          E(x=KX7))
    # ------------------------------------------------------------ (152) Dutiyasaññāvedayita
    k8 = f"lần thứ hai về {KX7}"
    for lv, t, sid in heads(8, 152, f"Bàn {k8}"):
        d.head(lv, t, sid)
    d.seg("5-730",
          f"{Q(T8)} {AM} {Q(f'là {B.RUPA}')} {NHP} {B.VEDANA}… {B.SANNA}… {B.SANKHARA}… {q(f'là {B.VINNANA}')} {NHP} "
          + " ".join(f"{q('là ' + PL[k])} {NHP}" for k in ("k", "r", "a")))
    d.seg("5-731",
          f"{navq_open(T8)} {AM} {Q(f'là {LT}')} {NH} {TENA_HI(f'là {LK}')}",
          f"Phần bàn {k8} đã hoàn tất.")
    # ------------------------------------------------------------ (153) Tatiyasaññāvedayita
    k9 = f"lần thứ ba về {KX7}"
    for lv, t, sid in heads(9, 153, f"Bàn {k9}"):
        d.head(lv, t, sid)
    no_mr = f"{SVP} không có {MR}"
    no_pv = f"{SVP} không có {PV}"
    has_die = f"{HAS_P} qua đời… {HAS_C} qua đời"
    d.seg("5-732",
          f"{Q(T9)} {AM} {Q(f'{SVP} có {MR}')} {NHP} {q(no_mr)} {AM} {hanci_no(no_mr, T9)}",
          f"{Q(T9)} {AM} {Q(f'{SVP} có {PV}')} {NHP} {q(no_pv)} {AM} "
          f"{Q(f'{NO_P} qua đời, {NO_V} qua đời… {NO_C} qua đời')} {NHP} {nanu_l(has_die)} {AM} "
          f"{hanci_no(has_die, T9)}",
          f"{Q(T9)} {AM} {Q(POISON)} {NHP} {q(NPOISON)} {AM} {hanci_no(NPOISON, T9)}",
          f"{Q(T9)} {AM} {Q(POISON)} {AM} {Q('không phải là người đang nhập sự chấm dứt')} {NHP}")
    d.seg("5-733",
          f"{Q(T9N)} {AM} {Q(niy(SVP))} {NATTHI} Nếu {niy(SVP, True)}, {B.NO_CA_VATA} “{T9N}.")
    cs_n = f"{CS} không thể qua đời"
    d.seg("5-734",
          f"{Q(cs_n)} {AM} {Q(niy(CS))} {NATTHI} {hanci_no(niy(CS, True), cs_n)}",
          f"Phần bàn {k9} đã hoàn tất.")
    # ------------------------------------------------------------ (154) Asaññasattupika
    for lv, t, sid in heads(10, 154, K(x=KX10)):
        d.head(lv, t, sid)
    bh_has = f"{HAS_P} {BHAV}… {HAS_C} {BHAV}"
    d.seg("5-735",
          f"{Q(T10)} {AM} {Q(f'{SVP} có {KM}')} {NHP} {q(f'{SVP} không có {KM_PE}')} {AM} "
          f"{hanci_no(f'{SVP} không có {KM}', T10)}",
          f"{Q(T10)} {AM} {Q(f'{SVP} có {PV}')} {NHP} {q(no_pv)} {AM} {Q(f'{NO_P} {BHAV}… {NO_C} {BHAV}')} {NHP} "
          f"{nanu_l(bh_has)} {AM} {hanci_no(bh_has, T10)}",
          f"{Q(T10)} {AM} "
          f"{Q(f'bất cứ ai nhập sự chấm dứt tri giác và cảm giác, tất cả những người ấy đều {ASS}')} {NHP}")
    d.seg("5-736",
          f"{NVQ(T10)} {AM} {NANU(IDHA)} {AM} {hanci_yes(IDHA, T10)}",
          E(x=KX10))
    # ------------------------------------------------------------ (155) Kammūpacaya
    for lv, t, sid in heads(11, 155, K(x=KU)):
        d.head(lv, t, sid)
    pairs = "; ".join(other(x) for x in L11)
    d.seg("5-737",
          f"{Q(T11)} {AM} {Q(f'{pairs}… {other(C2.AO)}')} {NHP}")
    d.seg("5-738",
          f"{Q(T11)} {AM} {Q(KU_SA)} {NHP}",
          f"Có phải {KU_SA} không, đúng vậy. Có phải {KU} cùng sinh với nghiệp thiện là thiện không, "
          f"không nên nói như vậy…",
          ved_line("thiện"))
    d.seg("5-739",
          f"{Q(KU_SA)} {AM} {Q(f'{KU} cùng sinh với nghiệp bất thiện là bất thiện')} {NHP}",
          ved_line("bất thiện"))
    d.seg("5-740",
          f"{Q(kc(KAMMA, f'{KAMMA} có đối tượng'))} {AM} {Q(kc(KU, f'{KU} có đối tượng'))} {NHP} "
          f"{q(kc(KU, f'{KU} không có đối tượng'))} {AM} {Q(kc(KAMMA, f'{KAMMA} không có đối tượng'))} {NHP}",
          f"{Q(kc(KAMMA, f'{BREAK} {KAMMA} tan rã'))} {AM} {Q(kc(KU, f'{BREAK} {KU} tan rã'))} {NHP}",
          f"{Q(kc(KU, f'{BREAK} {KU} không tan rã'))} {AM} {Q(kc(KAMMA, f'{BREAK} {KAMMA} không tan rã'))} {NHP}")
    d.seg("5-741",
          f"{Q(IN_K)} {AM} {Q(f'chính {KAMMA} ấy là {KU} ấy')} {NHP}",
          f"{Q(FROM_K)} {AM} {Q(f'chính {KAMMA} ấy là {KU} ấy, là {VIP} ấy')} {NHP}",
          f"{Q(f'{FROM_K}, {VIP} có đối tượng')} {AM} {Q(f'{KU} có đối tượng')} {NHP} "
          f"{q(f'{KU} không có đối tượng')} {AM} {Q(f'{VIP} không có đối tượng')} {NHP}")
    d.seg("5-742",
          f"Có phải {T11} không, đúng vậy. {NANU_VUTTAM} {SUTTA_P}. {ATTHEVA} {AM} {TENA_HI_NA(T11)}",
          E(x=KU),
          f"{VAGGA15}.",
          C9.TASSUDDANAM,
          UDDANA,
          TATIYO_PANNASAKO,
          C9.TASSUDDANAM,
          UDDANA50)
    return d.text()


# ================================================================ cross-book asserts (pi-1..4 rails)
CROSS = [
    (cond(AV, SK), 2), (REV_AV.replace("các sự tạo tác", "sự tạo tác"), 2), (f"{cond(TA, UP)}, {REV_TA}", 2),
    (f"{cond('thức', NR)}, {cond(NR, 'thức', True)}", 2), (JM, 2), ("sự sinh", 2), ("sự hiện hữu", 2),
    (VIM, 1), (CHANDA, 1), ("chi phần của con đường", 1), ("xem xét lại", 1), ("dưỡng chất", 2),
    ("trân trọng", 4), (KIRIYA, 1), ("sự thực hành, sự tu tập, sự làm đi làm lại", 1), ("xác định", 2),
    (SVN, 2), ("sự chấm dứt tri giác và cảm giác", 2), ("chư thiên Vô Tưởng", 2), ("sự qua đời", 2),
    ("sự không tham lam, tức gốc rễ thiện", 1), ("sự không sân hận", 1), ("sự không si mê", 1),
    ("sự tạo tác bằng thân", 2), ("sự tạo tác bằng lời nói", 2), ("đã được tạo và tích lũy", 1),
    ("sự sinh khởi tùy thuộc vào điều kiện", 1), ("kiếp", 2), ("khuynh hướng tiềm ẩn", 2), ("sự phòng hộ", 1),
    ("gốc rễ thiện", 1), (LT, 1), (LK, 1), (PL["k"], 1), (PL["r"], 1), (PL["a"], 1), (ADUK, 1),
    ("gắn liền với cảm giác dễ chịu", 1), ("quả của nghiệp", 1), ("không xác định về mặt đạo đức", 1),
    ("phần tinh thần và vật chất", 2), ("khao khát", 2), ("sự bám víu", 2), ("vô minh", 1),
    ("năng lực", 2), ("ý muốn", 1), ("tinh tấn", 1), ("Trường Bộ Kinh", 4), ("Tăng Chi Bộ Kinh", 4),
    ("Trung Bộ Kinh", 4), ("tái sinh vào", 2), ("thế giới", 2), ("vị trời", 2), ("loài người", 2),
]
# ================================================================ finished pi-5 chapters (zero-shot outputs)
PI5 = [
    (f"Có phải {MPN} không? {NHP}", "12-catutthavaggo.md"), (ANS, "12-catutthavaggo.md"),
    (C12.poison("thân của bậc A-la-hán"), "12-catutthavaggo.md"), ("con đường A-la-hán", "12-catutthavaggo.md"),
    ("thành quả A-la-hán", "12-catutthavaggo.md"), ("Không có.", "12-catutthavaggo.md"),
    (C13.PC[0], "13-pancamavaggo.md"), (C13.PC[1], "13-pancamavaggo.md"), (C13.PC[2], "13-pancamavaggo.md"),
    (C13.PC[3], "13-pancamavaggo.md"), (C13.PC[4], "13-pancamavaggo.md"), ("và nó là", "13-pancamavaggo.md"),
    ("Bàn về sự sinh khởi tùy thuộc vào điều kiện", "14-chatthavaggo.md"), ("” – có bài kinh như vậy thật không? Không có.",
                                                                       "14-chatthavaggo.md"),
    ("Này các tỳ-khưu, sự sinh làm điều kiện cho sự lão hóa và sự chết", "14-chatthavaggo.md"),
    ("sự lão hóa và sự chết của", "15-sattamavaggo.md"), ("quả của nghiệp", "15-sattamavaggo.md"),
    ("cùng sinh với", "15-sattamavaggo.md"), ("hiện tượng cao quý", "15-sattamavaggo.md"),
    ("Năm điều nào?", "15-sattamavaggo.md"), ("người đang nhập sự chấm dứt", "16-atthamavaggo.md"),
    ("cõi chúng sinh Vô Tưởng", "16-atthamavaggo.md"), ("nhưng hơi khác một chút", "16-atthamavaggo.md"),
    ("đang tan rã, thì tan rã", "16-atthamavaggo.md"), ("tan rã", "16-atthamavaggo.md"),
    ("năm khối thuộc quá khứ", "17-navamavaggo.md"), ("mười hai lĩnh vực nhận biết thuộc quá khứ", "17-navamavaggo.md"),
    ("mười tám yếu tố thuộc quá khứ", "17-navamavaggo.md"), ("hai mươi hai năng lực thuộc quá khứ", "17-navamavaggo.md"),
    ("sáu mươi sáu năng lực", "17-navamavaggo.md"), ("năm mươi bốn yếu tố", "17-navamavaggo.md"),
    ("ba mươi sáu lĩnh vực nhận biết", "17-navamavaggo.md"), ("mười lăm khối", "17-navamavaggo.md"),
    (CS, "18-dasamavaggo.md"), ("Nhóm năm mươi thứ hai.", "18-dasamavaggo.md"), ("sự tu tập con đường", "18-dasamavaggo.md"),
    ("được hình thành trọn vẹn", "19-ekadasamavaggo.md"), ("khuynh hướng tiềm ẩn", "19-ekadasamavaggo.md"),
    ("sự phòng hộ", "20-dvadasamavaggo.md"), ("mà bằng sự cố định ấy", "20-dvadasamavaggo.md"),
    ("có thể tái sinh vào", "20-dvadasamavaggo.md"), ("chúng sinh Vô Tưởng", "11-tatiyavaggo.md"),
    ("không có tri giác", "11-tatiyavaggo.md"), ("có sự tiếp xúc", "11-tatiyavaggo.md"),
    ("Có phải không nên nói – “lời nói của Đức Phật, Đức Thế Tôn khi nói về điều thuộc thế gian thì thuộc thế gian, "
     "khi nói về điều vượt thế gian thì vượt thế gian không?", "10-dutiyavaggo.md"),
    ("khoảnh khắc", "10-dutiyavaggo.md"), ("vật chất thuộc quá khứ", "5-sabbamatthitikatha.md"),
    (C9.TASSUDDANAM, "9-hevatthikatha.md"), ("cần xem", "10-dutiyavaggo.md"), ("hiện tại", "13-pancamavaggo.md"),
    ("bất cứ ai", "10-dutiyavaggo.md"), ("tất cả những người ấy đều", "10-dutiyavaggo.md"),
    ("người không có", "11-tatiyavaggo.md"),
]


def check_cross():
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(dd.glob("*.md")))
             for b, dd in B.RAILS_DIR.items()}
    missing = [(s, f"pi-{b}") for s, b in CROSS if s not in texts[b]]
    missing += [(s, f) for s, f in PI5 if s not in (B.OUT_DIR / f).read_text(encoding="utf-8")]
    for s, w in missing:
        print(f"CROSS MISSING in {w}: {s}")
    assert not missing, f"{len(missing)} cross strings not found"
    print(f"ch23 cross asserts: {len(CROSS)} pi-1..4 strings, {len(PI5)} pi-5 chapter strings found")


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
    print(f"wrote {NAME}: {len([l for l in text.splitlines() if l.strip()])} lines; "
          f"odd closing order repaired: {len(repaired)}; line checks: OK")


if __name__ == "__main__":
    main()
