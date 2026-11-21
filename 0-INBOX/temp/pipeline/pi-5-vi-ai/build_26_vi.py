# -*- coding: utf-8 -*-
"""pi-5 (Kathāvatthu) Vietnamese zero-shot, chapter 26: 26-attharasamavaggo.md (Aṭṭhārasamavaggo, ^5-26-0 … ^5-827),
the nine kathā (177)-(185) of the eighteenth vagga and its uddāna.

Imports the approved sample builder (build_sample_vi, read-only) for every debate frame and the finished chapter
builders build_10 / build_11 / build_12 / build_15 / build_17 / build_22 (read-only; importing writes nothing) for
strings shared with those chapters, so every repeat is byte-identical. Every string claimed from the pi-1..4
Vietnamese rails is asserted to occur there, every string taken from a finished pi-5 chapter is asserted to occur in
that chapter's output; the sample's per-line checks (IDs, dashes, quotes, NFC, foreign letters) are run against the
Pāli. Every Pāli sentence keeps its own Vietnamese sentence.

run:  python -I -B -X utf8 build_26_vi.py
      python -I -B -X utf8 build_26_vi.py --find <regex> [maxhits] [maxchars]   (look up finished pi-5 chapters)
"""
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai")
import build_sample_vi as B  # noqa: E402
import build_10_vi as C10    # noqa: E402  (Tassuddānaṃ –, samāpanno, jhāna names, kaṇṭaka frames, ifq / tail)
import build_11_vi as C11    # noqa: E402  (jino satthā … dhammappaṭisaraṇo)
import build_12_vi as C12    # noqa: E402  (arahattamaggena … jahati, tiṇṇaṃ saṃyojanānaṃ pahānaṃ …, paths, fruits)
import build_15_vi as C15    # noqa: E402  (hanci_no / nanu_l, dvinnaṃ phassānaṃ…pe… samodhānaṃ)
import build_17_vi as C17    # noqa: E402  (three samādhis, āvaṭṭanā…pe… paṇidhi)
import build_22_vi as C22    # noqa: E402  (yā … uppādāya āvaṭṭanā …, anāvaṭṭentassa uppajjati …, mettā … upekkhā)

NAME = "26-attharasamavaggo.md"
Q, q, NANU, AM, cap, chain = B.Q, B.q, B.NANU, B.AMANTA, B.cap, B.chain
NH, NHP = B.NA_HEVAM, B.NA_HEVAM_PE
NVQ, TENA_HI, ATTHEVA, NANU_VUTTAM = B.NA_VATTABBAM_Q, B.TENA_HI, B.ATTHEVA, B.NANU_VUTTAM
NO_CA_VATA = B.NO_CA_VATA
VAR = B.VAR
K, E = B.KATHA.format, B.KATHA_END.format
VAGGA18 = B.VAGGA[18]                                     # Aṭṭhārasamavaggo = «Chương thứ mười tám» (terms file)
TASSUDDANAM = C10.TASSUDDANAM                             # Tassuddānaṃ – (coordinator: byte for byte)
hanci_no, nanu_l = C15.hanci_no, C15.nanu_l               # Hañci P, no ca vata re vattabbe – "Q"ti. / …pe… nanu Xti?
hanci = B.hanci                                           # Hañci P, tena vata re vattabbe – "Q"ti.

# ================================================================ kathā names (headings and closing lines)
KX = {1: "thế giới loài người",                           # Manussalokakathā (terms file, pi-2)
      2: "việc thuyết giảng Giáo Pháp",                   # Dhammadesanākathā (dhammadesanā pi-4, ch11)
      3: "lòng trắc ẩn",                                  # Karuṇākathā (karuṇā pi-1, ch22)
      4: "các loại hương thơm",                           # Gandhajātikathā (gandha «hương thơm» pi-4, ch21)
      5: "một con đường",                                 # Ekamaggakathā
      6: "sự chuyển từ tầng thiền sang tầng thiền",       # Jhānasaṅkantikathā (jhānā jhānaṃ saṅkamati)
      7: "tầng thiền trung gian",                         # Jhānantarikakathā (aṭṭhakathā: jhānantariko samādhi)
      8: "việc cho rằng nghe âm thanh",                   # Saddaṃ suṇātītikathā (as written, no samāpanno)
      9: "việc cho rằng thấy hình sắc bằng mắt"}          # Cakkhunā rūpaṃ passatītikathā (pi-2 cakkhunā rūpaṃ disvā)


def heads(n):
    """#### Aṭṭhārasamavaggo ^5-26-n-0 / ##### (176+n) n. <title> ^5-26-n-1-0"""
    return [(4, VAGGA18, f"5-26-{n}-0"), (5, f"({176 + n}) {n}. {K(x=KX[n])}", f"5-26-{n}-1-0")]


BHAG = C12.BHAG                                           # bhagavā «Đức Thế Tôn»
BB = "Đức Phật, Đức Thế Tôn"                              # buddho bhagavā (ch3, ch10)

# ================================================================ (177) Manussaloka
T1 = f"{BB} đã sống ở thế giới loài người"                # buddho bhagavā manussaloke aṭṭhāsi (manussaloka pi-2)
BV = ("những bảo tháp, khu vườn, tịnh xá, làng, thị trấn, thành phố, đất nước, xứ sở nơi Đức Phật đã cư trú")
# buddhavutthāni cetiyāni ārāmavihāragāmanigamanagarāni raṭṭhāni janapadāni (cetiya ch21; ārāma «vườn» ch18;
# gāma / nigama / nagara / janapada ch5; raṭṭha «đất nước» sample; janapada «xứ sở» pi-2)
LUMB = ("Đức Thế Tôn đã sinh ra tại Lâm-tỳ-ni, đã giác ngộ hoàn toàn dưới gốc cây Bồ-đề, Đức Thế Tôn đã chuyển "
        "bánh xe Giáo Pháp tại Ba-la-nại")               # (ch3 ^5-274 wording)
KUSI = f"{BHAG} đã nhập Niết-bàn trọn vẹn tại Câu-thi-na"   # kusinārāyaṃ bhagavā parinibbuto (parinibbuta pi-4)
LIFE = f"{LUMB}, tại bảo tháp Cha-pa-la, sự tạo tác của tuổi thọ đã được buông bỏ, {KUSI}"
# … cāpāle cetiye āyusaṅkhāro ossaṭṭho, kusinārāyaṃ bhagavā parinibbuto (saṅkhāra «tạo tác» pi-2)
LIFE_PE = f"{LUMB.split(', đã giác ngộ')[0]}… {KUSI}"     # bhagavā lumbiniyā jāto…pe… kusinārāyaṃ bhagavā parinibbuto
EKAM = "Này các tỳ-khưu, một thời Ta trú tại"             # ekamidāhaṃ, bhikkhave, samayaṃ … viharāmi (bhikkhave ch6)
SUTTA_PLACES = (
    f"“{EKAM} Úc-ca-tha, trong rừng Su-bha-ga, dưới gốc cây sa-la chúa” [Trường Bộ Kinh 2.91]; "
    f"“{EKAM} Ưu-lâu-tần-loa, tại cây đa của người chăn dê, khi vừa mới giác ngộ hoàn toàn” [Tăng Chi Bộ Kinh 4.21]; "
    f"“{EKAM} Vương Xá, trong Trúc Lâm, nơi cho sóc ăn” [Trường Bộ Kinh 2.180]; "
    f"“{EKAM} Xá-vệ, trong rừng Kỳ-đà, tại khu vườn của ông Cấp Cô Độc”; "
    f"“{EKAM} Tỳ-xá-ly, trong Đại Lâm, tại giảng đường có mái nhọn” [Trường Bộ Kinh 3.11]!")
# ukkaṭṭhāyaṃ … subhagavane sālarājamūle / uruvelāyaṃ … ajapālanigrodhe paṭhamābhisambuddho / rājagahe … veḷuvane
# kaḷandakanivāpe / sāvatthiyaṃ … jetavane anāthapiṇḍikassa ārāme / vesāliyaṃ … mahāvane kūṭāgārasālāya
# (Sāvatthī «Xá-vệ» ch3; abhisambuddha ch3; ārāma «khu vườn» as BV; other names new)
LOKE = (f"{BHAG} đã sinh ra ở thế gian, đã lớn lên ở thế gian, sống vượt lên trên thế gian, không bị thế gian làm "
        "vấy bẩn")                                        # loke jāto, loke saṃvaḍḍho, lokaṃ abhibhuyya viharati
#                                                           anupalitto lokena (anupalitta «không bị vấy bẩn» ch12)

# ================================================================ (178) Dhammadesanā
T2 = f"Giáo Pháp đã được {BB} thuyết giảng"               # buddhena bhagavatā dhammo desito (deseti pi-4)
EPI = C11.EPI                                             # jino satthā … dhammappaṭisaraṇo (ch11; ch13 differs)
ABH = "hóa thân"                                          # abhinimmita (aṭṭhakathā: abhinimmitaṃ pesesi)
ANANDA = "tôn giả A-nan"                                  # āyasmā ānando (sample, ch13)
SARI = ("“Này Xá-lợi-phất, Ta cũng có thể thuyết giảng Giáo Pháp một cách tóm tắt; này Xá-lợi-phất, Ta cũng có thể "
        "thuyết giảng Giáo Pháp một cách chi tiết; này Xá-lợi-phất, Ta cũng có thể thuyết giảng Giáo Pháp vừa tóm tắt "
        "vừa chi tiết; và những người hiểu được thì khó tìm” [Tăng Chi Bộ Kinh 3.33, trong Kinh Xá-lợi-phất]!")
# saṃkhittenapi kho ahaṃ, sāriputta, dhammaṃ deseyyaṃ; … aññātāro ca dullabhā (Xá-lợi-phất ch2, ch11)
AB, SN, SP = ("sau khi đã hiểu biết trực tiếp, không phải khi chưa hiểu biết trực tiếp", "có căn cứ, không phải không có "
              "căn cứ", "có sức thuyết phục, không phải không có sức thuyết phục")
# abhiññāya … no anabhiññāya (abhiññā «hiểu biết trực tiếp» pi-2) / sanidānaṃ … no anidānaṃ / sappāṭihāriyaṃ …
GOTAMAKA = (
    f"“‘Này các tỳ-khưu, Ta thuyết giảng Giáo Pháp {AB}; này các tỳ-khưu, Ta thuyết giảng Giáo Pháp {SN}; này các "
    f"tỳ-khưu, Ta thuyết giảng Giáo Pháp {SP}; này các tỳ-khưu, đối với Ta [{VAR} (Sī., Pī., Ka.): yañcassa], người "
    f"thuyết giảng Giáo Pháp {AB}, thuyết giảng Giáo Pháp {SN}, thuyết giảng Giáo Pháp {SP}, thì lời khuyên dạy là "
    "điều nên làm, lời giáo huấn là điều nên làm; và này các tỳ-khưu, thật đủ để các ông thỏa mãn, đủ để các ông hài "
    "lòng, đủ để các ông có niềm vui – Đức Thế Tôn là bậc Tự Giác Ngộ Hoàn Toàn, Giáo Pháp được khéo thuyết giảng, "
    "Tăng đoàn thực hành tốt đẹp’. Và khi lời giải đáp này đang được nói ra, mười nghìn thế giới đã rung chuyển” "
    "[Tăng Chi Bộ Kinh 3.126]!")
# ovāda / anusāsanī / tuṭṭhi / attamanatā (attamana «hài lòng» ch3) / somanassa «niềm vui» (pi-1) / svākkhāto dhammo,
# suppaṭipanno saṅgho / veyyākaraṇa / dasasahassilokadhātu «mười nghìn thế giới» (ch10)

# ================================================================ (179) Karuṇā
METTA, KARUNA, MUDITA, UPEKKHA = C22.METTA, C22.KARUNA, C22.MUDITA, C22.UPEKKHA   # (pi-1, pi-2, ch22)


def has(x, neg=False):
    """(n)atthi buddhassa bhagavato X"""
    return f"{BB} {'không ' if neg else ''}có {x}"


T3 = has(KARUNA, True)                                    # natthi buddhassa bhagavato karuṇā
KAR4 = f"{BHAG} là người có lòng trắc ẩn, người mang lại lợi ích cho thế gian, người thương xót thế gian, người hành " \
       "động vì sự tốt đẹp của thế gian"
# kāruṇiko lokahito lokānukampako lokatthacaro (sample ^5-230 lokānukampāya «vì lòng thương xót thế gian»,
# atthāya «vì sự tốt đẹp», hita «lợi ích»)
MKS = f"{BHAG} đã nhập thành tựu thiền của lòng trắc ẩn lớn"   # mahākaruṇāsamāpattiṃ samāpajji (samāpatti pi-2)

# ================================================================ (180) Gandhajāti
T4 = f"phân và nước tiểu của {BB} vượt trội hẳn các loại hương thơm khác"
# buddhassa bhagavato uccārapassāvo ativiya aññe gandhajāte adhiggaṇhāti (uccārapassāva ch10)
ODANA = f"{BHAG} ăn cơm và cháo"                          # bhagavā odanakummāsaṃ bhuñjati (pi-1 ^1-742 «Cơm, cháo»)
USE = (f"có những người dùng phân và nước tiểu của {BB} để tắm, để thoa, để xoa lên người "
       f"[{VAR} (Sī., Pī., Ka.): uccārenti], cất giữ trong giỏ, đặt vào hộp, bày ra ở chợ, và dùng hương thơm ấy làm "
       "những việc cần đến hương thơm")
# atthi keci … nhāyanti vilimpanti ucchādenti … peḷāya paṭisāmenti karaṇḍāya nikkhipanti āpaṇe pasārenti, tena ca
# gandhena gandhakaraṇīyaṃ karonti

# ================================================================ (181) Ekamagga
FR4 = f"bốn {C12.SAMANNA}"                                # cattāri sāmaññaphalāni (pi-1, ch4, ch12)
T5 = f"tự mình chứng nghiệm {FR4} bằng một con đường cao quý"   # ekena ariyamaggena … sacchikaroti (ch4, ch10)
T5S = f"tự mình chứng nghiệm {FR4} bằng bốn con đường cao quý"  # catūhi ariyamaggehi … sacchikaronti
FOUR_PE = C15.TWO_PE.replace("hai sự tiếp xúc… hai tâm", "bốn sự tiếp xúc… bốn tri giác")
# catunnaṃ phassānaṃ…pe… catunnaṃ saññānaṃ samodhānaṃ hoti (ch4 / ch15 pattern)
assert FOUR_PE == "có sự tụ hợp của bốn sự tiếp xúc… bốn tri giác"
MG_SO, MG_SA, MG_AN, MG_AR = C12.MG_SO, C12.MG_SA, C12.MG_AN, C12.MG_AR
AM3, AMO, AMA = C12.am(C12.THREE), C12.am(C12.OLARIKA), C12.am(C12.ANU)   # arahattamaggena … jahati (ch12)
VB_SO, VB_SA, VB_AN = C12.VB_SO, C12.VB_SA, C12.VB_AN     # tiṇṇaṃ saṃyojanānaṃ pahānaṃ sotāpattiphalaṃ … (ch12)
SEE = ("các đệ tử thấy điều mà Đức Phật, Đức Thế Tôn chưa thấy, đạt được điều chưa đạt được, tự mình chứng nghiệm "
       "điều chưa tự mình chứng nghiệm")
# sāvakā buddhassa bhagavato adiṭṭhaṃ dakkhanti anadhigataṃ adhigacchanti asacchikataṃ sacchikaronti (ch13 adiṭṭha …)


def bhavita(x):
    """bhagavatā X bhāvito"""
    return f"{x} đã được {BHAG} tu tập"


# ================================================================ (182) Jhānasaṅkanti
J = C10.J                                                 # tầng thiền thứ nhất … thứ tư (pi-1)
T6 = "chuyển từ tầng thiền sang tầng thiền"               # jhānā jhānaṃ saṅkamati


def sk(a, b):
    """A-ā jhānā B-ṃ jhānaṃ saṅkamati"""
    return f"chuyển từ {J[a]} sang {J[b]}"


ya, arise, nvq_c = C22.ya, C22.arise, C22.nvq_c           # (ch22 frames, byte-identical)
VK = C10.VK                                               # vitakkavicārā «sự hướng tâm và sự duy trì tâm» (pi-1)
VKA = f"có {VK}"                                          # savitakkaṃ savicāraṃ (pi-1 ^1-160)
PITI = "sự hân hoan"                                      # pīti (pi-1, ch10)


def ad(x, obj):
    """X-ṃ jhānaṃ OBJ ādīnavato manasikaroto uppajjati (ādīnavato «là sự nguy hại» ch17)"""
    return f"{x} sinh khởi nơi người chú tâm đến {obj} là sự nguy hại"


def same(a, b):
    """taññeva A-ṃ jhānaṃ taṃ B-ṃ jhānaṃ (ch5 «chính X ấy là Y ấy»)"""
    return f"chính {J[a]} ấy là {J[b]} ấy"


def unit(a, obj, qual, end_pe):
    """^5-813 l.2-5 / ^5-814 / ^5-815"""
    b = a + 1
    t = sk(a, b)
    yy = ya(J[a], J[b])
    no = f"Nếu {arise(J[b], False)}, {NO_CA_VATA} “{t}”" + ("…" if end_pe else ".")
    return (f"{Q(t)} {AM} {Q(yy)} {NHP}",
            f"{nvq_c(t, yy)} {AM} {Q(arise(J[b], True))} {NHP} {nanu_l(arise(J[b], False))} {AM} {no}",
            f"{Q(t)} {AM} {Q(ad(J[a], obj))} {AM} {Q(ad(J[b], obj))} {NHP}",
            f"{Q(f'{J[a]} {qual}')} {AM} {Q(f'{J[b]} {qual}')} {NHP} {q(t)} {AM} {Q(same(a, b))} {NHP}")


JH_SUTTA = ("“Này các tỳ-khưu, ở đây, vị tỳ-khưu hoàn toàn tách khỏi các dục lạc… chứng nhập và an trú tầng thiền "
            "thứ tư” [Tăng Chi Bộ Kinh 2.13; 4.163]!")   # idha, bhikkhave, bhikkhu vivicceva kāmehi…pe… (ch21)

# ================================================================ (183) Jhānantarikā
JI = "tầng thiền trung gian"                              # jhānantarikā (aṭṭhakathā: avitakko vicāramatto samādhi
#                                                           jhānantariko)
T7 = f"có {JI}"                                           # atthi jhānantarikā
S1, S2, S3 = C17.S1, C17.S2, C17.S3                       # three samādhis (pi-1, pi-2, ch17)
S2J, S2N = f"{S2} là {JI}", f"{S2} không phải là {JI}"    # avitakko vicāramatto samādhi (na) jhānantarikā


def btw(a, b, yes=True):
    """A-assa ca jhānassa B-assa ca jhānassa antare (n)atthi jhānantarikā"""
    return f"giữa {J[a]} và {J[b]} {'có' if yes else 'không có'} {JI}"


def sj(s, yes=True):
    return f"{s} là {JI}" if yes else f"{s} không phải là {JI}"


PAT = "thuộc hiện tại"                                    # paṭuppanna = paccuppanna (aṭṭhakathā; ch5 «thuộc quá khứ»)
TWO_J = f"giữa hai tầng thiền {PAT}"                      # dvinnaṃ jhānānaṃ paṭuppannānamantare
VATT = (f"khi {S2} đang diễn ra, {J[0]} đã chấm dứt, {J[1]} {PAT}")
# avitakke vicāramatte samādhimhi vattamāne paṭhamaṃ jhānaṃ niruddhaṃ dutiyaṃ jhānaṃ paṭuppannaṃ
BS3 = C17.BS3                                             # tayo samādhī vuttā bhagavatā – … (ch17)
BS3_PE = f"Đức Thế Tôn đã nói đến ba sự định tâm – định tâm có sự hướng tâm… không có sự duy trì tâm"
# tayo samādhī vuttā bhagavatā – savitakko…pe… avicāro samādhi
assert BS3.startswith(BS3_PE.split("…")[0]) and BS3.endswith(BS3_PE.split("…")[1])

# ================================================================ (184) Saddaṃ suṇāti
SAM = C10.SAM                                             # samāpanno «người đang nhập thành tựu thiền» (ch10)
T8 = f"{SAM} nghe âm thanh"                               # samāpanno saddaṃ suṇāti
SENSE = (f"{SAM} thấy hình sắc bằng mắt… bằng tai… bằng mũi… bằng lưỡi… chạm vật xúc chạm bằng thân")
# samāpanno cakkhunā rūpaṃ passati…pe… sotena…pe… ghānena…pe… jivhāya…pe… kāyena phoṭṭhabbaṃ phusati (pi-2 ^2 indriya)
SOT = "người có được thức qua tai"                        # sotaviññāṇasamaṅgī (ch17 samaṅgī «có được»; pi-2 thức qua tai)
MANO = "định tâm thuộc về người có được ý thức"           # samādhi manoviññāṇasamaṅgissa (manoviññāṇa «ý thức» pi-2)
MS = f"{MANO}, {SOT} nghe âm thanh"
TWO_PE = C15.TWO_PE                                       # dvinnaṃ phassānaṃ…pe… dvinnaṃ cittānaṃ samodhānaṃ (ch15)
kt, ifq, tail, sam = C10.kt, C10.ifq, C10.tail, C10.sam   # (ch10 frames)
KT = C10.KT                                               # kaṇṭako «cái gai»
KT1 = kt("âm thanh", J[0])                                # paṭhamassa jhānassa saddo kaṇṭako vutto bhagavatā (ch10)
KT2 = kt("sự hướng tâm, sự duy trì tâm", J[1])            # dutiyassa jhānassa vitakko vicāro kaṇṭako vutto bhagavatā
ARU, NIRS, SV = C10.ARU, C10.NIRS, C10.SV                 # arūpa āyatanas, saññāvedayitanirodha (pi-2, ch10)
KTS = ("Đức Thế Tôn đã nói rằng "
       + chain([f"{PITI} là {KT} của {J[2]}", f"hơi thở vào và hơi thở ra là {KT} của {J[3]}",
                f"đối với {sam(ARU[0])}, tri giác về hình sắc là {KT}",
                f"đối với {sam(ARU[1])}, tri giác về {ARU[0]} là {KT}",
                f"đối với {sam(ARU[2])}, tri giác về {ARU[1]} là {KT}",
                f"đối với {sam(ARU[3])}, tri giác về {ARU[2]} là {KT}",
                f"đối với {sam(NIRS)}, {SV} là {KT}"]))
# tatiyassa jhānassa pīti kaṇṭako…pe… catutthassa jhānassa assāsapassāso kaṇṭako … ākāsānañcāyatanaṃ samāpannassa
# rūpasaññā kaṇṭako… … saññā ca vedanā ca kaṇṭako vutto bhagavatā (vutto bhagavatā once: «Đức Thế Tôn đã nói rằng»
# once; ch10 ^5-332 wording of each item)

# ================================================================ (185) Cakkhunā rūpaṃ passati
EYE = "thấy hình sắc bằng mắt"                            # cakkhunā rūpaṃ passati (pi-2 cakkhunā rūpaṃ disvā)
FIVE_PE = ("nghe âm thanh bằng tai… ngửi mùi bằng mũi… nếm vị bằng lưỡi… chạm vật xúc chạm bằng thân")   # (pi-2)
BODY = "chạm vật xúc chạm bằng thân"                      # kāyena phoṭṭhabbaṃ phusati (pi-2)
RU = B.RUPA                                               # rūpa (matter) «vật chất»: the eye / body (aṭṭhakathā)
R_SEE = f"thấy hình sắc bằng {RU}"                        # rūpena rūpaṃ passati (object: rūpāyatana, sample split)
R_KNOW = f"nhận biết rõ hình sắc bằng {RU}"               # rūpena rūpaṃ paṭivijānāti (paṭivijānāti pi-2), eye lines
R_TOUCH = f"chạm {RU} bằng {RU}"                          # rūpena rūpaṃ phusati (object: the tangible, matter)
R_KNOW_B = f"nhận biết rõ {RU} bằng {RU}"                 # rūpena rūpaṃ paṭivijānāti, body lines (reported)
R_MANO = f"{RU} là ý thức"                                # rūpaṃ manoviññāṇaṃ
AVP = C17.AVP                                             # āvaṭṭanā…pe… paṇidhi (ch17)


def org(x, neg=False):
    """(n)atthi X-ssa āvaṭṭanā…pe… paṇidhi"""
    return f"{x} {'không ' if neg else ''}có {AVP}"


def org_lines(organ, thesis):
    """…pe… X-ena … phusatīti? Āmantā. Atthi X-ssa āvaṭṭanā…? … nanu natthi …? … Hañci natthi …"""
    return (f"{q(thesis)} {AM} {Q(org(organ))} {NHP} {nanu_l(org(organ, True))} {AM} "
            f"Nếu {org(organ, True)}, {NO_CA_VATA} “{thesis}”")


# ================================================================ uddāna
UDD = (f"{T1}, {T2}, {T3}, {T4}, {T5}, {T6}, {T7}, {T8}, {EYE}, {BODY}.")
# Buddho bhagavā manussaloke aṭṭhāsi, … cakkhunā rūpaṃ passati [no comma] kāyena phoṭṭhabbaṃ phusati.


def build():
    d = B.Doc()
    d.head(3, VAGGA18, "5-26-0")
    # ------------------------------------------------------------ (177) Manussaloka
    d.head(4, f"(177) 1. {K(x=KX[1])}", "5-26-1-0")
    d.seg("5-802",
          f"{NVQ(T1)} {AM} {NANU(f'có {BV}')} {AM} {hanci(f'có {BV}', T1)}",
          f"{NVQ(T1)} {AM} {NANU(LIFE)} {AM} {hanci(LIFE_PE, T1)}",
          f"{NVQ(T1)} {AM} {NANU_VUTTAM} {SUTTA_PLACES} {ATTHEVA} {AM} {TENA_HI(T1)}")
    d.seg("5-803",
          f"{Q(T1)} {AM} {NANU(f'{LOKE} [Tăng Chi Bộ Kinh 4.36]')} {AM} {hanci_no(LOKE, T1)}",
          E(x=KX[1]))
    # ------------------------------------------------------------ (178) Dhammadesanā
    for lv, t, sid in heads(2):
        d.head(lv, t, sid)
    d.seg("5-804",
          f"{NVQ(T2)} {AM} Được ai thuyết giảng? Được {ABH} thuyết giảng. {Q(f'{ABH} là {EPI}')} {NHP}",
          f"{NVQ(T2)} {AM} Được ai thuyết giảng? Được {ANANDA} thuyết giảng. {Q(f'{ANANDA} là {EPI}')} {NHP}")
    d.seg("5-805",
          f"{NVQ(T2)} {AM} {NANU_VUTTAM} {SARI} {ATTHEVA} {AM} {TENA_HI(T2)}")
    d.seg("5-806",
          f"{NVQ(T2)} {AM} {NANU_VUTTAM} {GOTAMAKA} {ATTHEVA} {AM} {TENA_HI(T2)}",
          E(x=KX[2]))
    # ------------------------------------------------------------ (179) Karuṇā
    for lv, t, sid in heads(3):
        d.head(lv, t, sid)
    d.seg("5-807",
          f"{Q(T3)} {AM} {Q(has(METTA, True))} {NHP} {q(T3)} {AM} {Q(has(f'{MUDITA}… {UPEKKHA}', True))} {NHP}",
          f"{Q(has(METTA))} {AM} {Q(has(KARUNA))} {NHP} {q(has(f'{MUDITA}… {UPEKKHA}'))} {AM} {Q(has(KARUNA))} "
          f"{NHP}",
          f"{Q(T3)} {AM} {Q(f'{BHAG} là người không có lòng trắc ẩn')} {NHP} {nanu_l(KAR4)} {AM} "
          f"Nếu {KAR4}, {NO_CA_VATA} “{T3}”…",
          f"{Q(T3)} {AM} {NANU(MKS)} {AM} {hanci_no(MKS, T3)}")
    d.seg("5-808",
          f"{Q(has(KARUNA))} {AM} {Q(f'{BHAG} có tham đắm')} {NH} {TENA_HI(T3)}",
          E(x=KX[3]))
    # ------------------------------------------------------------ (180) Gandhajāti
    for lv, t, sid in heads(4):
        d.head(lv, t, sid)
    d.seg("5-809",
          f"{Q(T4)} {AM} {Q(f'{BHAG} là người ăn hương thơm')} {NHP} {nanu_l(ODANA)} {AM} {hanci_no(ODANA, T4)}",
          f"{Q(T4)} {AM} {Q(USE)} {NHP}",
          E(x=KX[4]))
    # ------------------------------------------------------------ (181) Ekamagga
    for lv, t, sid in heads(5):
        d.head(lv, t, sid)
    d.seg("5-810",
          f"{Q(T5)} {AM} {Q(FOUR_PE)} {NHP} {q(T5)} {AM} {Q(f'bằng {MG_SO}')} {NHP} "
          f"{q(f'bằng {MG_SA}… bằng {MG_AN}')} {NHP}",
          f"Bằng con đường nào? Bằng {MG_AR}. {Q(AM3)} {NHP} {q(AM3)} {AM} {NANU(VB_SO)} {AM} {hanci_no(VB_SO, AM3)}",
          f"{Q(AMO)} {NHP} {q(AMO)} {AM} {NANU(VB_SA)} {AM} {hanci_no(VB_SA, AMO)}",
          f"{Q(AMA)} {NHP} {q(AMA)} {AM} {NANU(VB_AN)} {AM} {hanci_no(VB_AN, AMA)}")
    d.seg("5-811",
          f"{NVQ(T5)} {AM} {Q(bhavita(MG_SO))} {AM} {Q(f'{BHAG} là {C12.SO}')} {NHP} "
          f"{q(bhavita(f'{MG_SA}… {MG_AN}'))} {AM} {Q(f'{BHAG} là {C12.AN}')} {NHP}")
    d.seg("5-812",
          f"{Q(f'{BHAG} {T5}, các đệ tử {T5S}')} {AM} {Q(SEE)} {NHP}",
          E(x=KX[5]))
    # ------------------------------------------------------------ (182) Jhānasaṅkanti
    for lv, t, sid in heads(6):
        d.head(lv, t, sid)
    d.seg("5-813",
          f"{Q(T6)} {AM} {Q(sk(0, 2))} {NHP} {q(T6)} {AM} {Q(sk(1, 3))} {NHP}",
          *unit(0, "các dục lạc", VKA, True))
    d.seg("5-814", *unit(1, VK, f"có {PITI}", False))
    d.seg("5-815", *unit(2, PITI, "có hạnh phúc đi kèm", False))
    d.seg("5-816",
          f"{NVQ(T6)} {AM} {NANU_VUTTAM} {JH_SUTTA} {ATTHEVA} {AM} {TENA_HI(T6)}",
          E(x=KX[6]))
    # ------------------------------------------------------------ (183) Jhānantarikā
    for lv, t, sid in heads(7):
        d.head(lv, t, sid)
    d.seg("5-817",
          f"{Q(T7)} {AM} {Q('có sự tiếp xúc trung gian… có tri giác trung gian')} {NHP}",
          f"{Q(T7)} {AM} {Q(btw(1, 2))} {NHP}",
          f"{Q(T7)} {AM} {Q(btw(2, 3))} {NHP}",
          f"{Q(btw(1, 2, False))} {AM} {hanci_no(btw(1, 2, False), T7)}",
          f"{Q(btw(2, 3, False))} {AM} {hanci_no(btw(2, 3, False), T7)}")
    d.seg("5-818",
          f"{Q(btw(0, 1))} {AM} {Q(btw(1, 2))} {NHP}",
          f"{Q(btw(0, 1))} {AM} {Q(btw(2, 3))} {NHP}",
          f"{Q(btw(1, 2, False))} {AM} {Q(btw(0, 1, False))} {NHP}",
          f"{Q(btw(2, 3, False))} {AM} {Q(btw(0, 1, False))} {NHP}")
    d.seg("5-819",
          f"{Q(sj(S2))} {AM} {Q(sj(S1))} {NHP}",
          f"{Q(sj(S2))} {AM} {Q(sj(S3))} {NHP}",
          f"{Q(sj(S1, False))} {AM} {Q(sj(S2, False))} {NHP}",
          f"{Q(sj(S3, False))} {AM} {Q(sj(S2, False))} {NHP}")
    d.seg("5-820",
          f"{Q(f'{TWO_J} có {S2}')} {AM} {NANU(VATT)} {AM} Nếu {VATT}, {NO_CA_VATA} “{TWO_J}, {S2J}.")
    d.seg("5-821",
          f"{Q(S2N)} {AM} {Q(f'{S2} là {J[0]}… là {J[1]}… là {J[2]}… là {J[3]}')} {NH} {TENA_HI(S2J)}")
    d.seg("5-822",
          f"{Q(S2J)} {AM} {NANU(f'{BS3} [Trường Bộ Kinh 3.305, 353]')} {AM} {hanci_no(BS3_PE, S2J)}",
          E(x=KX[7]))
    # ------------------------------------------------------------ (184) Saddaṃ suṇāti
    for lv, t, sid in heads(8):
        d.head(lv, t, sid)
    d.seg("5-823",
          f"{Q(T8)} {AM} {Q(SENSE)} {NHP}",
          f"{Q(T8)} {AM} {Q(f'{SOT} là {SAM}')} {NH} {NANU(MANO)} {AM} {hanci_no(MANO, T8)}",
          f"{Q(MS)} {AM} {hanci_no(MS, T8)} {Q(MS)} {AM} {Q(TWO_PE)} {NHP}")
    d.seg("5-824", f"{NVQ(T8)} {AM} {NANU(KT1)} {AM} {C10.hanci(KT1, T8)}")
    d.seg("5-825",
          f"{ifq(KT1, T8)} {AM} {Q(f'{KT2}, {tail(VK)}')} {NHP}",
          f"{ifq(KT1, T8)} {AM} {Q(f'{KTS}, {tail(SV)}')} {NHP}",
          E(x=KX[8]))
    # ------------------------------------------------------------ (185) Cakkhunā rūpaṃ passati
    for lv, t, sid in heads(9):
        d.head(lv, t, sid)
    d.seg("5-826",
          f"{Q(EYE)} {AM} {Q(R_SEE)} {NHP} {q(R_SEE)} {AM} {Q(R_KNOW)} {NHP} {q(R_KNOW)} {AM} {Q(R_MANO)} {NHP} "
          f"{org_lines('mắt', EYE)}.",
          f"Có phải {FIVE_PE} không? {AM} {Q(R_TOUCH)} {NHP}",
          f"{Q(R_TOUCH)} {AM} {Q(R_KNOW_B)} {NHP} {q(R_KNOW_B)} {AM} {Q(R_MANO)} {NHP} {org_lines('thân', BODY)}…")
    d.seg("5-827",
          f"Có phải không nên nói – “{EYE}”… “{BODY}” không? {AM} {NANU_VUTTAM} “Này các tỳ-khưu, ở đây, vị tỳ-khưu "
          f"{EYE}… {BODY}” [Trung Bộ Kinh 1.349; Tăng Chi Bộ Kinh 4.37 (cần xem Chú giải)]! {ATTHEVA} {AM} "
          f"{TENA_HI(f'{EYE}… {BODY}')}",
          E(x=KX[9]),
          f"{VAGGA18}.",
          TASSUDDANAM,
          cap(UDD))
    return d.text()


# ================================================================ cross-book asserts (pi-1..4 rails)
CROSS = [
    ("thế giới loài người", 2), ("nhập Niết-bàn trọn vẹn", 4), ("Ngài thuyết giảng Giáo Pháp", 4),
    ("việc thuyết giảng Giáo Pháp", 4), ("hiểu biết trực tiếp", 2), ("bậc Tự Giác Ngộ Hoàn Toàn", 4),
    ("Tăng đoàn", 2), ("niềm vui", 1), ("xứ sở", 2), ("tạo tác", 2), ("Cơm, cháo", 1), ("thành tựu thiền", 2),
    ("con đường vào dòng", 2), ("con đường trở lại một lần", 2), ("con đường không trở lại", 2),
    ("con đường A-la-hán", 2), ("bậc vào dòng", 4), ("bậc không trở lại", 4), ("thành quả của đời sống sa-môn", 1),
    ("tầng thiền thứ nhất", 1), ("có sự hướng tâm và sự duy trì tâm", 1), ("Các hiện tượng có hạnh phúc đi kèm", 1),
    ("hoàn toàn tách khỏi các dục lạc", 1), ("chứng nhập và an trú tầng thiền thứ nhất", 1),
    (S2, 2), (S3, 2), ("định tâm có sự hướng tâm và sự duy trì tâm", 2), ("lĩnh vực không gian vô tận", 2),
    ("lĩnh vực thức vô tận", 2), ("lĩnh vực không có gì cả", 2),
    ("lĩnh vực không phải tri giác cũng không phải không tri giác", 2), ("sự chấm dứt tri giác và cảm giác", 2),
    ("các tri giác về hình sắc", 2), ("thức qua tai", 2), ("ý thức", 2), ("nhận biết rõ", 2),
    ("thấy hình sắc bằng mắt", 2), ("nghe âm thanh bằng tai", 2), ("ngửi mùi bằng mũi", 2),
    ("nếm vị bằng lưỡi", 2), ("chạm vật xúc chạm bằng thân", 2), ("sự hân hoan", 1), ("vật chất", 2),
]
# ================================================================ finished pi-5 chapters (zero-shot outputs)
PI5 = [
    (LUMB, "3-brahmacariyakatha.md"), ("Xá-vệ", "3-brahmacariyakatha.md"), ("Đức Phật, Đức Thế Tôn",
                                                                          "3-brahmacariyakatha.md"),
    ("giác ngộ hoàn toàn", "3-brahmacariyakatha.md"), ("bảo tháp", "21-terasamavaggo.md"),
    ("đất nước", "1-puggalakatha.md"), ("làng", "5-sabbamatthitikatha.md"), ("thị trấn", "5-sabbamatthitikatha.md"),
    ("thành phố", "5-sabbamatthitikatha.md"), ("vườn cây", "18-dasamavaggo.md"),
    ("Này các tỳ-khưu", "6-atitakkhandhadikatha.md"), ("Trường Bộ Kinh", "17-navamavaggo.md"),
    ("Không bị vấy bẩn", "12-catutthavaggo.md"), (EPI, "11-tatiyavaggo.md"), ("tôn giả A-nan", "1-puggalakatha.md"),
    ("tôn giả Xá-lợi-phất", "11-tatiyavaggo.md"), ("trong Kinh Ví Dụ Chim Cút", "24-solasamavaggo.md"),
    ("mười nghìn thế giới", "10-dutiyavaggo.md"), ("hài lòng", "3-brahmacariyakatha.md"),
    (f"{METTA}", "22-cuddasamavaggo.md"), (KARUNA, "22-cuddasamavaggo.md"), (MUDITA, "22-cuddasamavaggo.md"),
    (UPEKKHA, "22-cuddasamavaggo.md"), ("vì lòng thương xót thế gian", "1-puggalakatha.md"),
    ("vì sự tốt đẹp, lợi ích", "1-puggalakatha.md"), ("nhập thành tựu thiền", "10-dutiyavaggo.md"),
    ("có tham đắm", "5-sabbamatthitikatha.md"), ("phân và nước tiểu", "10-dutiyavaggo.md"),
    (f"tự mình chứng nghiệm ba {C12.SAMANNA}", "4-jahatikatha.md"), ("con đường cao quý", "4-jahatikatha.md"),
    ("có sự tụ hợp của ba sự tiếp xúc", "4-jahatikatha.md"), ("Có phải bằng con đường vào dòng không?",
                                                             "4-jahatikatha.md"),
    (AM3, "12-catutthavaggo.md"), (AMO, "12-catutthavaggo.md"), (AMA, "12-catutthavaggo.md"),
    (VB_SO, "12-catutthavaggo.md"), (VB_SA, "12-catutthavaggo.md"), (VB_AN, "12-catutthavaggo.md"),
    ("đã được tu tập", "12-catutthavaggo.md"), ("đệ tử", "11-tatiyavaggo.md"),
    ("chưa thấy, chưa biết, chưa tự mình chứng nghiệm", "13-pancamavaggo.md"),
    (ya("điều bất thiện", "điều thiện"), "22-cuddasamavaggo.md"),
    (f"{nvq_c('gốc rễ bất thiện nối kết với gốc rễ thiện', ya('điều bất thiện', 'điều thiện'))} {AM}",
     "22-cuddasamavaggo.md"),
    ("sinh khởi nơi người không hướng đến", "22-cuddasamavaggo.md"),
    ("chẳng phải điều thiện sinh khởi nơi người hướng đến… sinh khởi nơi người mong cầu sao?",
     "22-cuddasamavaggo.md"),
    ("là sự nguy hại", "17-navamavaggo.md"), ("chú tâm đến các tạo tác", "17-navamavaggo.md"),
    ("có sự hân hoan", "10-dutiyavaggo.md"), ("chính tương lai ấy là hiện tại ấy", "5-sabbamatthitikatha.md"),
    ("thuộc quá khứ", "5-sabbamatthitikatha.md"),
    ("Này các tỳ-khưu, ở đây, vị tỳ-khưu hoàn toàn tách khỏi các dục lạc", "21-terasamavaggo.md"),
    ("chứng nhập và an trú tầng thiền thứ tư", "21-terasamavaggo.md"),
    (f"Chẳng phải {BS3} [Trường Bộ Kinh 3.305, 353] sao?", "17-navamavaggo.md"),
    (f"Chẳng phải có {S2} sao?", "17-navamavaggo.md"),
    (f"{ifq(KT1, f'{SAM} có sự phát ra lời nói')} {AM}", "10-dutiyavaggo.md"),
    (f"Nếu {KT1}, {B.TENA_VATA}", "10-dutiyavaggo.md"), ("người ấy có tri giác và cảm giác không?",
                                                         "10-dutiyavaggo.md"),
    (f"đối với {sam(ARU[0])}, tri giác về hình sắc là {KT}", "10-dutiyavaggo.md"),
    ("hơi thở vào và hơi thở ra là cái gai của tầng thiền thứ tư", "10-dutiyavaggo.md"),
    ("có được thức qua mắt", "17-navamavaggo.md"), (TWO_PE, "15-sattamavaggo.md"), (AVP, "17-navamavaggo.md"),
    ("(cần xem Chú giải)", "15-sattamavaggo.md"), (TASSUDDANAM, "10-dutiyavaggo.md"),
    ("thuyết giảng", "11-tatiyavaggo.md"),
]


def check_cross():
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(dd.glob("*.md")))
             for b, dd in B.RAILS_DIR.items()}
    missing = [(s, f"pi-{b}") for s, b in CROSS if s not in texts[b]]
    cache = {}
    for s, f in PI5:
        if f not in cache:
            cache[f] = (B.OUT_DIR / f).read_text(encoding="utf-8")
        if s not in cache[f]:
            missing.append((s, f))
    for s, w in missing:
        print(f"CROSS MISSING in {w}: {s}")
    assert not missing, f"{len(missing)} cross strings not found"
    print(f"ch26 cross asserts: {len(CROSS)} pi-1..4 strings, {len(PI5)} pi-5 chapter strings found")


# ================================================================ lookup helper (finished pi-5 chapters only)
DONE = ["1-puggalakatha.md", "2-parihanikatha.md", "3-brahmacariyakatha.md", "4-jahatikatha.md",
        "5-sabbamatthitikatha.md", "6-atitakkhandhadikatha.md", "7-ekaccam-atthitikatha.md",
        "8-satipatthanakatha.md", "9-hevatthikatha.md", "10-dutiyavaggo.md", "11-tatiyavaggo.md",
        "12-catutthavaggo.md", "13-pancamavaggo.md", "14-chatthavaggo.md", "15-sattamavaggo.md",
        "16-atthamavaggo.md", "17-navamavaggo.md", "18-dasamavaggo.md", "19-ekadasamavaggo.md",
        "20-dvadasamavaggo.md", "21-terasamavaggo.md", "22-cuddasamavaggo.md", "23-pannarasamavaggo.md",
        "24-solasamavaggo.md"]


def find(pat, maxhits=6, maxc=700):
    rx = re.compile(pat)
    hits = 0
    for n in DONE:
        pl = [x for x in (B.PALI_DIR / n).read_text(encoding="utf-8").splitlines() if x.strip()]
        vl = [x for x in (B.OUT_DIR / n).read_text(encoding="utf-8").splitlines() if x.strip()]
        for i, ln in enumerate(pl):
            m = rx.search(ln)
            if not m:
                continue
            s = max(0, m.start() - 100)
            print(f"[{n} line {i + 1}]")
            print("  PI:", ln[s:s + 300])
            print("  VI:", vl[i][:maxc] if i < len(vl) else "<missing>")
            hits += 1
            if hits >= maxhits:
                return


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
    if len(sys.argv) > 2 and sys.argv[1] == "--find":
        find(sys.argv[2], *(int(a) for a in sys.argv[3:]))
    else:
        main()
