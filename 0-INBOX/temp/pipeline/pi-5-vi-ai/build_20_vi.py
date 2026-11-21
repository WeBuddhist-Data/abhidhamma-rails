# -*- coding: utf-8 -*-
"""pi-5 (Kathāvatthu) Vietnamese zero-shot, chapter 20: 20-dvadasamavaggo.md (Dvādasamavaggo, ^5-20-0 … ^5-653),
the ten kathā (116)-(125) of the twelfth vagga and its uddāna.

Imports the approved sample builder (build_sample_vi, read-only) for every debate frame and the finished chapter
builders build_2_vi / build_4_vi / build_9_vi / build_12_vi / build_15_vi (read-only, importing writes nothing)
for persons, the vagga close and the vedaniya / sampayutta / āvaṭṭanā lists, so every repeat is byte-identical
with those chapters. Every string claimed from the pi-1..4 Vietnamese rails is asserted to occur there, every
string taken from a finished pi-5 chapter is asserted to occur in that chapter's output; the sample's per-line
checks (IDs, dashes, quotes, NFC, foreign letters) are run against the Pāli.

run:  python -I -B -X utf8 build_20_vi.py
"""
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai")
import build_sample_vi as B  # noqa: E402
import build_2_vi as C2      # noqa: E402
import build_4_vi as C4      # noqa: E402
import build_9_vi as C9      # noqa: E402  (vagga close: Tassuddānaṃ –)
import build_12_vi as C12    # noqa: E402
import build_15_vi as C15    # noqa: E402  (sukhavedaniya … paṇidhi lists, ch15 ^5-492 / ^5-495)

NAME = "20-dvadasamavaggo.md"
Q, q, NANU, AM, cap, chain = B.Q, B.q, B.NANU, B.AMANTA, B.cap, B.chain
NH, NHP = B.NA_HEVAM, B.NA_HEVAM_PE
NVQ, TENA_HI, TENA_HI_NA = B.NA_VATTABBAM_Q, B.TENA_HI, B.TENA_HI_NA
VAR, SPELL = B.VAR, B.SPELL
hanci_no, hanci_yes, nanu_l = C15.hanci_no, C15.hanci_yes, C15.nanu_l
VAGGA12 = B.VAGGA[12]                                     # Dvādasamavaggo = «Chương thứ mười hai» (terms file)
K = B.KATHA.format
E = B.KATHA_END.format


def heads(n, num, title):
    """#### Dvādasamavaggo ^5-20-n-0 / ##### (num) n. <title> ^5-20-n-1-0"""
    return [(4, VAGGA12, f"5-20-{n}-0"), (5, f"({num}) {n}. {title}", f"5-20-{n}-1-0")]


# ================================================================ (116) Saṃvaro kammaṃ
SAM, ASAM = "sự phòng hộ", "sự không phòng hộ"            # saṃvara / asaṃvara (ch11, terms file ch20)
KAMMA = "nghiệp"                                          # kamma (pi-1)
KX1 = f"việc cho rằng {SAM} là {KAMMA}"                  # Saṃvaro kammantikathā (terms file)
IND = {"cakkhu": B.INDRIYA[0], "sota": B.INDRIYA[1], "ghāna": B.INDRIYA[2], "jivhā": B.INDRIYA[3],
       "kāya": B.INDRIYA[4], "mano": B.INDRIYA[5]}       # cakkhundriya … manindriya (pi-2)
DOOR_K = {"cakkhu": "nghiệp bằng mắt", "jivhā": "nghiệp bằng lưỡi", "kāya": "nghiệp bằng thân",
          "mano": "nghiệp bằng ý"}                        # cakkhu- / jivhā- (new) / kāya- / manokamma (pi-1, ch14, ch16)


def sv(d, neg=False):
    """cakkhundriyasaṃvaro / cakkhundriyaasaṃvaro"""
    return f"{ASAM if neg else SAM} {IND[d]}"


def svk(d, neg=False):
    """cakkhundriyasaṃvaro cakkhukammaṃ"""
    return f"{sv(d, neg)} là {DOOR_K[d]}"


def samvara_seg(neg):
    """^5-630 / ^5-631 (three lines each)"""
    pe = chain([sv(x, neg) for x in ("sota", "ghāna", "jivhā")])
    first = Q(f"{ASAM if neg else SAM} là {KAMMA}")
    rest = q(f"{pe}… {svk('kāya', neg)}")
    return (
        f"{first} {AM} {Q(svk('cakkhu', neg))} {NHP} {rest} {NHP}",
        f"{Q(svk('kāya', neg))} {AM} {Q(svk('cakkhu', neg))} {NHP} {q(svk('kāya', neg))} {AM} "
        f"{Q(chain([sv('sota', neg), sv('ghāna', neg), svk('jivhā', neg)]))} {NHP} {q(svk('mano', neg))} {NHP}",
        f"{Q(svk('mano', neg))} {AM} {Q(svk('cakkhu', neg))} {NHP} {q(svk('mano', neg))} {AM} "
        f"{Q(chain([sv('sota', neg), sv('ghāna', neg), sv('jivhā', neg), svk('kāya', neg)]))} {NHP}")


BOTH1 = f"cả {SAM} lẫn {ASAM} đều là {KAMMA}"            # saṃvaropi asaṃvaropi kammaṃ
SEE = "khi thấy hình sắc bằng mắt thì nắm giữ dấu hiệu tổng quát"      # cakkhunā rūpaṃ disvā nimittaggāhī hoti (pi-1)
NOSEE = "thì không nắm giữ dấu hiệu tổng quát"                           # na nimittaggāhī hoti (pi-1 ^1-1354)
HEAR = "khi nghe âm thanh bằng tai"                                      # sotena saddaṃ sutvā (pi-1)
KNOW = "khi nhận biết đối tượng của ý bằng ý thì nắm giữ dấu hiệu tổng quát"   # manasā dhammaṃ viññāya … (pi-1)
NIMITTA = (f"“Này các tỳ-khưu, ở đây, vị tỳ-khưu {SEE}… {NOSEE}, {HEAR}… {KNOW}… {NOSEE}”!")
# idha, bhikkhave, bhikkhu … (ch15 «Này Kê-vát-ta, ở đây, vị tỳ-khưu»)

# ================================================================ (117) Kamma
KX2 = KAMMA                                               # Kammakathā = «Bàn về nghiệp»
SAV, ASAV = "có quả", "không có quả"                      # savipāka / avipāka (ch7, ch15)
TH2 = f"tất cả {KAMMA} đều {SAV}"                         # sabbaṃ kammaṃ savipākaṃ
ALLC = f"tất cả chủ ý đều {SAV}"                          # sabbā cetanā savipākā (cetanā «chủ ý» core)
VIPA = "không xác định về mặt đạo đức thuộc quả của nghiệp"   # vipākābyākata (abyākata pi-1; vipāka «quả của nghiệp» pi-1)
KIRA = "không xác định về mặt đạo đức mang tính chức năng"    # kiriyābyākata (pi-1 ^1-1068)
PL = {"k": "thuộc cõi dục lạc", "r": "thuộc cõi hình sắc", "a": "thuộc cõi không hình sắc",
      "ap": "không nằm trong các cõi tồn tại"}           # kāmāvacara … apariyāpanna (pi-1, ch11, ch15, ch16)


def cet(kind, *planes):
    """(kāmāvacarā …) vipākābyākatā / kiriyābyākatā cetanā"""
    pl = "".join(f"{PL[p]}, " for p in planes)
    return f"chủ ý {pl}{kind}"


def sv_(x):
    return f"{x} {SAV}"


def av_(x):
    return f"{x} {ASAV}"


NAHAM = ("“Này các tỳ-khưu, Ta không nói đến sự chấm dứt của các nghiệp có chủ ý đã được tạo, đã được tích lũy khi "
         "chưa được cảm nhận, và điều ấy ngay trong đời này, hoặc trong lần tái sinh kế tiếp "
         "[dị bản (Tăng Chi Bộ Kinh 10.17): upapajjaṃ], hoặc trong một lượt khác về sau” "
         "[Tăng Chi Bộ Kinh 10.217]!")
# nāhaṃ, bhikkhave, sañcetanikānaṃ kammānaṃ katānaṃ upacitānaṃ appaṭisaṃviditvā byantibhāvaṃ vadāmi, tañca kho
# diṭṭheva dhamme upapajje vā apare vā pariyāye (sañcetanika «có chủ ý» ch16; katattā upacitattā «đã được tạo và
# tích lũy» pi-1; diṭṭheva dhamme «ngay trong đời này» pi-4; upapajjati «tái sinh» coordinator)

# ================================================================ (118) Saddo vipāko / (119) Saḷāyatana
VIP = C15.VIP                                             # vipāko = «quả của nghiệp» (pi-1, ch15)
KX3 = f"việc cho rằng âm thanh là {VIP}"                  # Saddo vipākotikathā (ch15 Jarāmaraṇaṃ vipākotikathā frame)
TH3 = f"âm thanh là {VIP}"                                # saddo vipāko (sadda «âm thanh» pi-2)
PH = f"sự tiếp xúc là {VIP}, sự tiếp xúc"                 # phasso vipāko, phasso … (ch15)
VED, SAR, ANAR = C15.VED, C15.SAR, C15.ANAR
POS, ATT = C15.POS, C15.att                               # the full list and «nó (không) có sự hướng đến …» (ch15)
POS_PE = C15.POS_PE                                       # sukhavedaniyo dukkhavedaniyo…pe… sārammaṇo (ch15)
NEG_PE = C15.NEG_PE                                       # na sukhavedaniyo na dukkhavedaniyo…pe… anārammaṇo (ch15)
POS_PE1 = f"{VED[0]}… {SAR}"                              # sukhavedaniyo…pe… sārammaṇo
NEG_PE1 = f"không {VED[0]}… {ANAR}"                       # na sukhavedaniyo…pe… anārammaṇo
ATT_P, ATT_N = ATT(pe=True), ATT(neg=True, pe=True)       # atthi / natthi tassa āvaṭṭanā…pe… paṇidhi
BRAHMA = ("“Người ấy, do nghiệp ấy đã được tạo, đã được tích lũy, đã được tăng thêm, đã được mở rộng, có giọng nói "
          "như Phạm Thiên, nói như chim ca-lăng-tần-già” [trong Trường Bộ Kinh]!")
# so tassa kammassa katattā upacitattā ussannattā vipulattā brahmassaro hoti karavikabhāṇī [dīghanikāye]
# (katattā upacitattā pi-1; brahma «Phạm Thiên» pi-1; aṅguttaranikāye «trong Tăng Chi Bộ Kinh» ch3 pattern)
SALA = "sáu lĩnh vực nhận biết"                           # saḷāyatana (pi-2)
KX4 = SALA                                                # Saḷāyatanakathā
AY = {k: B.AYATANA[i] for i, k in enumerate(("cakkhu", "sota", "ghāna", "jivhā", "kāya"))}   # (pi-2)
UPP = f"{SALA} sinh khởi do nghiệp đã được tạo"           # saḷāyatanaṃ kammassa katattā uppannaṃ (pi-1 katattā)


def vp(x):
    return f"{x} là {VIP}"


def two_lines(x, ph_neg):
    """lines 2-3 of the vedaniya argument for a subject x (^5-636 / ^5-638)"""
    xx = f"{vp(x)}, {x}"
    l2 = f"Có phải {PH} {POS_PE1}, {ATT_P} không? {AM} Có phải {xx} {POS_PE1}, {ATT_P} không? {NHP}"
    l3 = f"Có phải {xx} {NEG_PE1}, {ATT_N} không? {AM} Có phải {PH} {ph_neg}, {ATT_N} không? {NHP}"
    return l2, l3


# ================================================================ (120)-(122) Sattakkhattuparama, Kolaṅkola, Ekabījī
SK7, KOL, EKB = "người tái sinh tối đa bảy lần", "người đi từ gia đình này sang gia đình khác", "người có một hạt giống"
# sattakkhattuparamo / kolaṅkolo / ekabījī puggalo (pi-4, ch3, ch12)


def fixed(p, plural=False):
    """X puggalo X-tāniyato = «X được cố định vào trạng thái …» (niyata «cố định» pi-1, ch13; -tā = trạng thái)"""
    return f"{'tất cả những người ấy đều' if plural else p} được cố định vào trạng thái {p[len('người '):]}"


TH5 = fixed(SK7)
KILLED = ["mẹ bị tước đoạt mạng sống", "cha bị tước đoạt mạng sống", "bậc A-la-hán bị tước đoạt mạng sống",
          "máu của Như Lai bị làm cho chảy với tâm độc ác", "Tăng đoàn bị chia rẽ"]
# mātā jīvitā voropitā … saṅgho bhinno (pi-2 ^2-U55, there with hoti)
KILLED_Q = Q(chain(KILLED))
ABH = "không có khả năng thấu hiểu Giáo Pháp trong khoảng giữa"   # abhabbo antarā dhammaṃ abhisametuṃ
# (bhabbo dhammaṃ abhisametuṃ «có khả năng thấu hiểu Giáo Pháp» ch13; abhabbo «không có khả năng» ch3; antarā ch16)
NY = "sự cố định"                                         # niyamo (= niyāmo, ch14 Niyamo [= niyāmo]; terms file)
NY_SO, NY_SA, NY_AN, NY_AR = (m.replace("con đường", NY, 1) for m in
                              (C4.SOTAPATTIMAGGA, C4.SAKADAGAMIMAGGA, C4.ANAGAMIMAGGA, C12.MG_AR))   # (ch14)
DEV6 = C2.DEV6                                            # satipaṭṭhānā … bojjhaṅgā (ch2, pi-3)


def yena(p):
    """so niyamo yena niyamena X"""
    return f"{NY} mà bằng {NY} ấy {fixed(p)}"


def yehi(p, items):
    """te satipaṭṭhānā… bojjhaṅgā yehi bojjhaṅgehi X"""
    return f"{items} mà bằng {DEV6[-1]} ấy {fixed(p)}"


def short(p):
    """Na vattabbaṃ – "X"ti? Āmantā. Nanu so X-oti? Āmantā. Hañci so X-o, tena vata re vattabbe – "X"ti."""
    nanu = f"người ấy là {p}"
    return f"{NVQ(fixed(p))} {AM} {NANU(nanu)} {AM} {hanci_yes(nanu, fixed(p))}"


# ================================================================ (123) Jīvitā voropana
DS = "người thành tựu về quan điểm"                       # diṭṭhisampanno puggalo (pi-2, pi-4)
KX8 = "việc tước đoạt mạng sống"                          # Jīvitā voropanakathā (jīvitā voropeti pi-2)
TH8 = f"{DS} có thể cố ý tước đoạt mạng sống của sinh vật"   # … sañcicca pāṇaṃ jīvitā voropeyya (pāṇa, sañcicca new)
KILL = ["tước đoạt mạng sống của mẹ", "tước đoạt mạng sống của cha", "tước đoạt mạng sống của một bậc A-la-hán",
        "với tâm độc ác làm cho máu của Như Lai chảy", "chia rẽ Tăng đoàn"]
# mātaraṃ … arahantaṃ jīvitā voropeyya, (pa)duṭṭhena cittena tathāgatassa lohitaṃ uppādeyya, saṅghaṃ bhindeyya
# (pi-2 ^2 ṭhānāṭhāna: «tước đoạt mạng sống của cha… của một bậc A-la-hán…», kept with its «một»)
SATTHA, DHA, SAN, SIK = "Bậc Đạo Sư", "Giáo Pháp", "Tăng đoàn", "sự tu học"   # satthā / dhamma / saṅgha / sikkhā (pi-1)
AGA, SAGA = "thiếu kính trọng", "kính trọng"              # agāravo / sagāravo (pi-2 agārava, pi-1 sagāravatā)
THUPA = "bảo tháp của Đức Phật"                           # buddhathūpa
OHA = (f"có thể đại tiện lên, có thể tiểu tiện lên, có thể khạc nhổ lên {THUPA}, có thể đi vòng quanh {THUPA} về "
       f"phía bên trái [{VAR} (Sī., Ka.): asabyākato]")
# buddhathūpe ohadeyya omutteyya niṭṭhubheyya buddhathūpe apabyāmato [asabyākato (sī. ka.)] kareyya
SEA = ("“Này các tỳ-khưu, ví như đại dương có bản chất ổn định, không tràn qua bờ; cũng vậy, này các tỳ-khưu, điều "
       "tu học nào Ta đã đặt ra cho các đệ tử, các đệ tử của Ta không vi phạm điều ấy, dù vì mạng sống” "
       "[Tiểu Phẩm 385; Tăng Chi Bộ Kinh 8.20; Kinh Phật Tự Thuyết 45]!")
# seyyathāpi, bhikkhave, mahāsamuddo ṭhitadhammo velaṃ nātivattati; evameva kho, bhikkhave, yaṃ mayā sāvakānaṃ
# sikkhāpadaṃ paññattaṃ taṃ mama sāvakā jīvitahetupi nātikkamanti (ch10 ^5-346 «ví như đại dương …; cũng vậy, này
# các tỳ-khưu,»; sikkhāpada «điều tu học» pi-2; sāvaka «đệ tử» ch4)

# ================================================================ (124) Duggati / (125) Sattamabhavika
DUG = "cõi xấu"                                           # duggati (pi-2)
KX9 = DUG
AR = C2.AR
PAH = C2.PAHINA                                           # pahīnā = «đã được dứt bỏ» (ch2, pi-2)


def dug(who):
    """X-assa (puggalassa) pahīnā duggati (ch11 / ch12 «đối với X, … đã được dứt bỏ»)"""
    return f"đối với {who}, {DUG} {PAH}"


TH9 = dug(DS)
APA = "ở cõi khổ"                                         # āpāyika (sample āpāyikaṃ dukkhaṃ «khổ đau ở cõi khổ»)
RUPE = f"tham đắm các hình sắc {APA}"                     # āpāyike rūpe rajjeyya (rajjati «tham đắm» ch11)
SENSES_PE = f"tham đắm các âm thanh {APA}… các mùi… các vị… các vật xúc chạm"   # āpāyike sadde… gandhe… rase… phoṭṭhabbe
SEX = ("hưởng thụ hành vi dâm dục với người nữ không phải loài người, với con vật cái thuộc loài súc sinh, với "
       "thiếu nữ loài rồng")                              # amanussitthiyā tiracchānagatitthiyā nāgakaññāya methunaṃ … (ch12)
ANIM = ["nhận dê và cừu", "nhận gà và heo", "nhận voi, bò, ngựa đực và ngựa cái"]   # (ch12, pi-4)
BIRD = "nhận chim đa đa, chim cút, chim công và chim trĩ"   # tittiravaṭṭakamorakapiñjaraṃ (ch12)
BIRD_V = f"{BIRD} [{SPELL} (Syā., Kaṃ., Pī.): … kapiñjalaṃ]"   # (ch12 GIHI_LIST)


def can(x, neg=False):
    return f"{'không thể' if neg else 'có thể'} {x}"


def full_list(neg=False, var=False):
    """āpāyike sadde…pe… gandhe… rase… phoṭṭhabbe…pe… amanussitthiyā … paṭiggaṇheyya… tittira… paṭiggaṇheyya"""
    head = f"{can(SENSES_PE, neg)}… {can(SEX, neg)}, {', '.join(can(a, neg) for a in ANIM)}"
    return f"{head}… {can(BIRD_V if var else BIRD, neg)}"


NOTE = (f"[theo Chú giải, đây là dấu hiệu câu hỏi của {B.PARAVADI}. Tuy vậy, câu hỏi này dường như là của "
        f"{B.SAKAVADI}, còn các câu hỏi trước trong phần bàn về {DUG} này dường như nên được hiểu là của {B.PARAVADI}]")
# [aṭṭhakathānulomaṃ paravādīpucchālakkhaṇaṃ. tathāpāyaṃ pucchā sakavādissa, purimāyo ca imissaṃ duggatikathāyaṃ
# paravādissāti gahetabbā viya dissanti] (paravādīpucchālakkhaṇaṃ «dấu hiệu câu hỏi của …» ch10; aṭṭhakathā pi-4)
RE = ["địa ngục", "cõi súc sinh", "cõi ngạ quỷ"]           # niraya / tiracchānayoni / pettivisaya (pi-2, ch16)


def reborn(r):
    return f"có thể tái sinh vào {r}"                     # upapajjeyya (pi-2 «tái sinh vào … địa ngục»)


S7 = "người ở lần hiện hữu thứ bảy"                       # sattamabhaviko puggalo (pi-2 «lần hiện hữu thứ tám»)
KX10 = S7

# ================================================================ vagga close
UDDANA = (f"{cap(SAM)} là {KAMMA}, {ASAM} cũng vậy, {TH2}, {TH3}, {SALA} là {VIP}, {TH5}, {fixed(KOL)}, "
          f"{fixed(EKB)}, {TH8}, {TH9}, đối với {S7} cũng vậy.")
# Saṃvaro kammaṃ tatheva asaṃvaro, sabbakammaṃ savipākaṃ, saddo vipāko, saḷāyatanaṃ vipāko, sattakkhattuparamo
# puggalo sattakkhattuparamatāniyato, kolaṅkolapuggalo kolaṅkolatāniyato, ekabījī puggalo ekabījitāniyato,
# diṭṭhisampanno puggalo sañcicca pāṇaṃ jīvitā voropeyya, diṭṭhisampannassa puggalassa pahīnā duggati, tatheva
# sattamabhavikassāti. (tatheva «… cũng vậy» ch14 / ch17)


def build():
    d = B.Doc()
    d.head(3, VAGGA12, "5-20-0")
    # ------------------------------------------------------------ (116) Saṃvaro kammaṃ
    d.head(4, f"(116) 1. {K(x=KX1)}", "5-20-1-0")
    d.seg("5-630", *samvara_seg(False))
    d.seg("5-631", *samvara_seg(True))
    d.seg("5-632",
          f"{NVQ(BOTH1)} {AM} {B.NANU_VUTTAM} {NIMITTA} {B.ATTHEVA} {AM} {TENA_HI(BOTH1)}",
          E(x=KX1))
    # ------------------------------------------------------------ (117) Kamma
    for lv, t, sid in heads(2, 117, K(x=KX2)):
        d.head(lv, t, sid)
    d.seg("5-633",
          f"{Q(TH2)} {AM} {Q(ALLC)} {NHP} {q(ALLC)} {AM} {Q(sv_(cet(VIPA)))} {NHP} {q(ALLC)} {AM} "
          f"{Q(sv_(cet(KIRA)))} {NHP}",
          f"{Q(ALLC)} {AM} {Q(sv_(cet(VIPA, 'k')))} {NHP} {q(ALLC)} {AM} {Q(sv_(cet(VIPA, 'r', 'a', 'ap')))} {NHP}",
          f"{Q(ALLC)} {AM} {Q(sv_(cet(KIRA, 'k')))} {NHP} {q(ALLC)} {AM} {Q(sv_(cet(KIRA, 'r', 'a')))} {NHP}")
    d.seg("5-634",
          f"{Q(av_(cet(VIPA)))} {AM} {hanci_no(av_(cet(VIPA)), ALLC)}",
          f"{Q(av_(cet(KIRA)))} {AM} {hanci_no(av_(cet(KIRA)), ALLC)}",
          f"{Q(av_(cet(VIPA, 'k', 'r', 'a', 'ap')))} {AM} {hanci_no(av_(cet(VIPA, 'ap')), ALLC)}",
          f"{Q(av_(cet(KIRA, 'k', 'r', 'a')))} {AM} {hanci_no(av_(cet(KIRA, 'a')), ALLC)}")
    d.seg("5-635",
          f"{NVQ(TH2)} {AM} {B.NANU_VUTTAM} {NAHAM} {B.ATTHEVA} {AM} {TENA_HI(TH2)}",
          E(x=KX2))
    # ------------------------------------------------------------ (118) Saddo vipāko
    for lv, t, sid in heads(3, 118, K(x=KX3)):
        d.head(lv, t, sid)
    l1 = (f"{Q(TH3)} {AM} Có phải {POS}; {ATT()} không? {NHP} {nanu_l(f'{NEG_PE}, {ATT_N}')} {AM} "
          f"{hanci_no(f'{NEG_PE1}, {ATT_N}', TH3)}")
    d.seg("5-636", l1, *two_lines("âm thanh", NEG_PE))
    d.seg("5-637",
          f"{NVQ(TH3)} {AM} {B.NANU_VUTTAM} {BRAHMA} {B.ATTHEVA} {AM} {TENA_HI(TH3)}",
          E(x=KX3))
    # ------------------------------------------------------------ (119) Saḷāyatana
    for lv, t, sid in heads(4, 119, K(x=KX4)):
        d.head(lv, t, sid)
    eye = AY["cakkhu"]
    l1 = (f"{Q(vp(eye))} {AM} Có phải {POS_PE}, {ATT_P} không? {NHP} {nanu_l(f'{NEG_PE1}, {ATT_N}')} {AM} "
          f"{hanci_no(f'{NEG_PE1}, {ATT_N}', vp(eye))[:-1]}…")
    d.seg("5-638", l1, *two_lines(eye, NEG_PE1))
    body = AY["kāya"]
    bx = f"{vp(body)}, {body}"
    d.seg("5-639",
          f"Có phải {chain([AY['sota'], AY['ghāna'], AY['jivhā'], vp(body)])} không? {AM} "
          f"Có phải {POS_PE1}, {ATT_P} không? {NHP} {nanu_l(f'{NEG_PE1}, {ATT_N}')} {AM} "
          f"{hanci_no(f'{NEG_PE1}, {ATT_N}', vp(body))}",
          f"Có phải {PH} {POS_PE1}, {ATT_P} không? {AM} Có phải {bx} {POS_PE1}, {ATT_P} không? {NHP} "
          f"có phải {bx} {NEG_PE1}, {ATT_N} không? {AM} Có phải {PH} {NEG_PE1}, {ATT_N} không? {NHP}")
    d.seg("5-640",
          f"{NVQ(vp(SALA))} {AM} {NANU(UPP)} {AM} {hanci_yes(UPP, vp(SALA))}",
          E(x=KX4))
    # ------------------------------------------------------------ (120) Sattakkhattuparama
    for lv, t, sid in heads(5, 120, K(x=SK7)):
        d.head(lv, t, sid)
    d.seg("5-641",
          f"{Q(TH5)} {AM} {KILLED_Q} {NHP}",
          f"{Q(TH5)} {AM} {Q(ABH)} {NHP} {Q(ABH)} {AM} {KILLED_Q} {NHP}")
    items = chain(DEV6)
    d.seg("5-642",
          f"{Q(TH5)} {AM} {Q(f'có {yena(SK7)}')} {NHP} {q(f'có {yehi(SK7, items)}')} {NHP}")
    items2 = f"{DEV6[0]}… {DEV6[-1]}"
    d.seg("5-643",
          f"{Q(f'không có {yena(SK7)}')} {AM} {hanci_no(f'không có {yena(SK7)}', TH5)}",
          f"{Q(f'không có {yehi(SK7, items2)}')} {AM} {hanci_no(f'không có {yehi(SK7, DEV6[-1])}', TH5)}")
    d.seg("5-644",
          f"{Q(TH5)} {AM} {Q(f'bằng {NY_SA}')} {NHP} {q(f'bằng {NY_AN}')} {NHP} {q(f'bằng {NY_AR}')} {NHP}",
          f"Bằng {NY} nào? Bằng {NY_SO}. {Q(TH5)} {AM} "
          f"{Q(f'bất cứ ai bước vào {NY_SO}, {fixed(SK7, plural=True)}')} {NHP}")
    nanu5 = f"người ấy là {SK7}"
    d.seg("5-645",
          f"{NVQ(TH5)} {AM} {NANU(nanu5)} {AM} {hanci_yes(nanu5, TH5)}",
          E(x=SK7))
    # ------------------------------------------------------------ (121) Kolaṅkola / (122) Ekabījī
    for lv, t, sid in heads(6, 121, K(x=KOL)):
        d.head(lv, t, sid)
    d.seg("5-646", short(KOL), E(x=KOL))
    for lv, t, sid in heads(7, 122, K(x=EKB)):
        d.head(lv, t, sid)
    d.seg("5-647", short(EKB), E(x=EKB))
    # ------------------------------------------------------------ (123) Jīvitā voropana
    for lv, t, sid in heads(8, 123, K(x=KX8)):
        d.head(lv, t, sid)
    kill = f"{DS} có thể cố ý {chain(KILL)}"
    d.seg("5-648",
          f"{Q(TH8)} {AM} {Q(kill)} {NHP}",
          f"{Q(TH8)} {AM} {Q(f'{DS} {AGA} đối với {SATTHA}')} {NHP} "
          f"có phải {AGA} đối với {DHA}… đối với {SAN}… đối với {SIK} không? {NHP}",
          f"{NANU(f'{DS} {SAGA} đối với {SATTHA}')} {AM} {hanci_no(f'{DS} {SAGA} đối với {SATTHA}', TH8)} "
          f"{NANU(f'{DS} {SAGA} đối với {DHA}… đối với {SAN}… đối với {SIK}')} {AM} "
          f"{hanci_no(f'{DS} {SAGA} đối với {SIK}', TH8)}")
    d.seg("5-649",
          f"{Q(f'{DS} {AGA} đối với {SATTHA}')} {AM} {Q(f'{DS} {OHA}')} {NHP}",
          f"{Q(TH8)} {AM} {B.NANU_VUTTAM} {SEA} {B.ATTHEVA} {AM} {TENA_HI_NA(TH8)}",
          E(x=KX8))
    # ------------------------------------------------------------ (124) Duggati
    for lv, t, sid in heads(9, 124, K(x=KX9)):
        d.head(lv, t, sid)
    ds_r = f"{DS} {can(RUPE)}"
    ds_b = f"{DS} {can(BIRD)}"
    d.seg("5-650",
          f"{Q(TH9)} {AM} {Q(ds_r)} {AM} {hanci_no(ds_r, TH9)}",
          f"{Q(TH9)} {AM} {Q(f'{DS} {full_list(var=True)}')} {AM} {hanci_no(ds_b, TH9)}")
    ar_r, ar_b = f"{dug(AR)}, {AR} {can(RUPE)}", f"{dug(AR)}, {AR} {can(BIRD)}"
    neg_list = full_list(neg=True)
    d.seg("5-651",
          f"{Q(f'{TH9}, {ds_r}')} {AM} {Q(ar_r)} {NHP} "
          f"{q(f'{TH9}, {DS} {can(SENSES_PE)}… {can(BIRD)}')} {AM} {Q(ar_b)} {NHP}",
          f"{Q(f'{dug(AR)}, nhưng {AR} {can(RUPE, True)}')} {AM} {Q(f'{TH9}, nhưng {DS} {can(RUPE, True)}')} {NHP} "
          f"{q(f'{dug(AR)}, nhưng {AR} {neg_list}')} {AM} {Q(f'{TH9}, nhưng {DS} {can(BIRD, True)}')} {NHP}")
    d.seg("5-652",
          f"{NOTE} {NVQ(TH9)} {AM} Có phải {DS} {reborn(RE[0])}… {reborn(RE[1])}… {reborn(RE[2])} không? {NH} "
          f"{TENA_HI(TH9)}",
          E(x=KX9))
    # ------------------------------------------------------------ (125) Sattamabhavika
    for lv, t, sid in heads(10, 125, K(x=KX10)):
        d.head(lv, t, sid)
    d.seg("5-653",
          f"Có phải không nên nói “{dug(S7)}” không? {AM} "
          f"Có phải {S7} {', '.join(reborn(r) for r in RE)} không? {NH} {TENA_HI(dug(S7))}",
          E(x=KX10),
          f"{VAGGA12}.",
          C9.TASSUDDANAM,
          UDDANA)
    return d.text()


# ================================================================ cross-book asserts (pi-1..4 rails)
CROSS = [
    (SEE, 1), (NOSEE, 1), ("K" + HEAR[1:] + "…", 1), (KNOW, 1), ("sự phòng hộ", 1), ("năng lực mắt", 2), ("năng lực ý", 2),
    ("nghiệp bằng thân", 1), ("nghiệp bằng ý", 1), ("không xác định về mặt đạo đức mang tính chức năng", 1),
    ("không xác định về mặt đạo đức", 1), ("quả của nghiệp", 1), ("thuộc cõi dục lạc", 1), ("thuộc cõi hình sắc", 1),
    ("thuộc cõi không hình sắc", 1), ("không nằm trong các cõi tồn tại", 1), ("đã được tạo và tích lũy", 1),
    ("ngay trong đời này", 4), ("Phạm Thiên", 1), (SALA, 2), ("lĩnh vực thân", 2), ("sinh khởi", 1),
    ("người tái sinh tối đa bảy lần", 4), ("người đi từ gia đình này sang gia đình khác", 4),
    ("người có một hạt giống", 4), ("cố định", 1), ("lần hiện hữu thứ tám", 2),
    ("Mẹ bị tước đoạt mạng sống, cha bị tước đoạt mạng sống, bậc A-la-hán bị tước đoạt mạng sống, máu của Như Lai "
     "bị làm cho chảy với tâm độc ác, Tăng đoàn bị chia rẽ", 2),
    ("tước đoạt mạng sống của cha… tước đoạt mạng sống của một bậc A-la-hán… với tâm độc ác làm cho máu của Như Lai "
     "chảy… chia rẽ Tăng đoàn", 2),
    (DS, 2), (DS, 4), ("thiếu kính trọng", 2), ("đối với Bậc Đạo Sư", 2),
    ("đối với Giáo Pháp", 2), ("đối với Tăng đoàn", 2), ("đối với sự tu học", 2), ("sự kính trọng", 1),
    ("điều tu học", 2), ("cõi xấu", 2), ("cõi khổ", 2), ("tái sinh vào cõi khổ", 2), ("địa ngục", 2),
    ("cõi súc sinh", 2), ("cõi ngạ quỷ", 2), ("loài súc sinh", 2), ("dê và cừu", 4), ("gà và heo", 4),
    ("voi, bò, ngựa đực và ngựa cái", 4), ("hưởng thụ hành vi dâm dục", 4), ("đại dương", 1), ("Chú giải", 4),
    ("Như Lai", 2), ("bước vào sự cố định", 4),
]
# ================================================================ finished pi-5 chapters (zero-shot outputs)
PI5 = [
    ("sự không phòng hộ", "11-tatiyavaggo.md"), ("sự phòng hộ", "11-tatiyavaggo.md"),
    ("không có quả", "7-ekaccam-atthitikatha.md"), ("có quả", "15-sattamavaggo.md"),
    ("nghiệp bằng thân", "14-chatthavaggo.md"), ("nghiệp bằng ý", "16-atthamavaggo.md"),
    ("nghiệp có chủ ý", "16-atthamavaggo.md"), ("Bàn về việc cho rằng sự lão hóa và sự chết là quả của nghiệp",
                                                "15-sattamavaggo.md"),
    (f"{POS}; {ATT()} không?", "15-sattamavaggo.md"), (f"chẳng phải {NEG_PE}", "15-sattamavaggo.md"),
    (f"sự tiếp xúc là quả của nghiệp, sự tiếp xúc {VED[0]}", "15-sattamavaggo.md"), (ATT_N, "15-sattamavaggo.md"),
    (ATT_P, "15-sattamavaggo.md"), ("Tóm tắt của chương này –", "9-hevatthikatha.md"),
    ("trong Tăng Chi Bộ Kinh", "3-brahmacariyakatha.md"),
    (SK7 + ", " + KOL + ", " + EKB, "3-brahmacariyakatha.md"), ("không có khả năng", "3-brahmacariyakatha.md"),
    ("có khả năng thấu hiểu Giáo Pháp", "13-pancamavaggo.md"), ("trong khoảng giữa", "16-atthamavaggo.md"),
    (NY_SO, "14-chatthavaggo.md"), (NY_SA, "14-chatthavaggo.md"), (NY_AN, "14-chatthavaggo.md"),
    (NY_AR, "14-chatthavaggo.md"), ("Bằng con đường nào?", "4-jahatikatha.md"),
    ("bất cứ ai thấu hiểu Giáo Pháp, tất cả những người ấy", "4-jahatikatha.md"),
    (DEV6[0], "2-parihanikatha.md"),
    (DEV6[-1], "2-parihanikatha.md"), ("bước vào sự cố định", "12-catutthavaggo.md"),
    ("có thể hưởng thụ hành vi dâm dục", "12-catutthavaggo.md"),
    ("có thể nhận dê và cừu, có thể nhận gà và heo, có thể nhận voi, bò, ngựa đực và ngựa cái, có thể nhận chim đa "
     "đa, chim cút, chim công và chim trĩ [khác chính tả (Syā., Kaṃ., Pī.): … kapiñjalaṃ]", "12-catutthavaggo.md"),
    ("“Này các tỳ-khưu, ví như đại dương", "10-dutiyavaggo.md"), ("; cũng vậy, này các tỳ-khưu,", "10-dutiyavaggo.md"),
    ("[Tiểu Phẩm 385; Tăng Chi Bộ Kinh 8.20; Kinh Phật Tự Thuyết 45", "10-dutiyavaggo.md"),
    ("dấu hiệu câu hỏi của người theo học thuyết khác", "10-dutiyavaggo.md"),
    ("ở đây, vị tỳ-khưu", "15-sattamavaggo.md"), ("Này các tỳ-khưu, Ta không", "10-dutiyavaggo.md"),
    ("đã được dứt bỏ", "2-parihanikatha.md"), ("khổ đau ở cõi khổ", "1-puggalakatha.md"),
    ("tham đắm", "11-tatiyavaggo.md"), ("cõi súc sinh, cõi ngạ quỷ", "16-atthamavaggo.md"),
    ("thuộc cõi dục lạc", "15-sattamavaggo.md"), ("không nằm trong các cõi tồn tại", "16-atthamavaggo.md"),
    ("[dị bản (Trung Bộ Kinh 3.300)", "16-atthamavaggo.md"), ("Trường Bộ Kinh", "8-satipatthanakatha.md"),
    ("nghĩ “tôi sẽ", "17-navamavaggo.md"), ("cũng vậy.", "14-chatthavaggo.md"),
    ("Phần bàn về việc cho rằng", "15-sattamavaggo.md"), ("người cố định", "13-pancamavaggo.md"),
]


def check_cross():
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(dd.glob("*.md")))
             for b, dd in B.RAILS_DIR.items()}
    missing = [(s, f"pi-{b}") for s, b in CROSS if s not in texts[b]]
    missing += [(s, f) for s, f in PI5 if s not in (B.OUT_DIR / f).read_text(encoding="utf-8")]
    for s, w in missing:
        print(f"CROSS MISSING in {w}: {s}")
    assert not missing, f"{len(missing)} cross strings not found"
    print(f"ch20 cross asserts: {len(CROSS)} pi-1..4 strings, {len(PI5)} pi-5 chapter strings found")


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
