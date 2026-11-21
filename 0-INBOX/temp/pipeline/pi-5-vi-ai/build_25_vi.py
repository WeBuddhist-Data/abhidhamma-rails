# -*- coding: utf-8 -*-
"""pi-5 (Kathāvatthu) Vietnamese zero-shot, chapter 25: 25-sattarasamavaggo.md (Sattarasamavaggo, ^5-25-0 … ^5-801),
the eleven kathā (166)-(176) of the seventeenth vagga and its uddāna (no fifty-group close in this file).

Imports the approved sample builder (build_sample_vi, read-only) for every debate frame and the finished chapter
builders build_10 / build_12 / build_15 / build_20 / build_21 (read-only; importing writes nothing) for strings shared
with those chapters, so every repeat is byte-identical. Every string claimed from the pi-1..4 Vietnamese rails is
asserted to occur there, every string taken from a finished pi-5 chapter is asserted to occur in that chapter's
output; the sample's per-line checks (IDs, dashes, quotes, NFC, foreign letters) are run against the Pāli.
Every Pāli sentence keeps its own Vietnamese sentence.

run:  python -I -B -X utf8 build_25_vi.py
"""
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai")
import build_sample_vi as B  # noqa: E402
import build_10_vi as C10    # noqa: E402  (Tassuddānaṃ –, CRIMES)
import build_12_vi as C12    # noqa: E402  (poison, CIVARA)
import build_15_vi as C15    # noqa: E402  (hanci_no / hanci_yes / nanu_l, GIL, VIP)
import build_20_vi as C20    # noqa: E402  (nāhaṃ, bhikkhave, sañcetanikānaṃ … sutta)
import build_21_vi as C21    # noqa: E402  (cīvaraṃ dadeyya … cetiyaṃ abhidakkhiṇaṃ kareyya)

NAME = "25-sattarasamavaggo.md"
Q, q, NANU, AM, cap, chain = B.Q, B.q, B.NANU, B.AMANTA, B.cap, B.chain
NH, NHP = B.NA_HEVAM, B.NA_HEVAM_PE
NVQ, TENA_HI, ATTHEVA, NANU_VUTTAM = B.NA_VATTABBAM_Q, B.TENA_HI, B.ATTHEVA, B.NANU_VUTTAM
VAR, SPELL = B.VAR, B.SPELL
K, E = B.KATHA.format, B.KATHA_END.format
VAGGA17 = B.VAGGA[17]                                     # Sattarasamavaggo = «Chương thứ mười bảy» (terms file)
TASSUDDANAM = C10.TASSUDDANAM                             # Tassuddānaṃ – (coordinator: byte for byte)
hanci_no, hanci_yes, nanu_l = C15.hanci_no, C15.hanci_yes, C15.nanu_l
NATTHI = "Không có."                                      # Natthi. (answer, ch11 / ch12 / ch22)
GIL = C15.GIL                                             # gilānapaccayabhesajjaparikkhāra (pi-2, ch10, ch15)
CIV = C12.CIVARA                                          # cīvara «y phục»
VIP = C15.VIP                                             # kammavipāka «quả của nghiệp» (pi-1, ch15)
ANICCA = B.ANICCA                                         # anicca … vipariṇāmadhamma (pi-1, pi-2)

# ================================================================ (166) Arahato puññūpacaya
AR = "bậc A-la-hán"
PU, APU = "sự tích lũy phước", "sự tích lũy điều không phải phước"   # puññūpacaya (terms file) / apuñña (ch18)
T1, T1A = f"{AR} có {PU}", f"{AR} có {APU}"               # atthi arahato (a)puññūpacayo (ch10 «bậc A-la-hán có X»)
N1, N1A = f"{AR} không có {PU}", f"{AR} không có {APU}"
SV = [("sự tạo tác thuộc về phước", "tạo tác"), ("sự tạo tác dẫn đến trạng thái bất động", "tạo tác")]
# puññābhisaṅkhāra / āneñjābhisaṅkhāra (pi-2 ^2 paṭiccasamuppāda); abhisaṅkharoti «tạo tác» (ch23)
KAMMA9 = ["cõi tái sinh", "sự hiện hữu", "quyền uy", f"quyền thống trị [{SPELL} (?): ādhipaccasaṃvattanikaṃ]",
          "của cải lớn", "đoàn tùy tùng lớn", "sự vinh hiển cõi trời", "sự vinh hiển cõi người"]
# gati- (sample) bhava- (pi-2) issariya- / adhipacca- (ch10, ch15) mahābhoga- (pi-4 mahābhoga «của cải lớn»)
# mahāparivāra- (pi-2 parivāra «đoàn tùy tùng») deva- / manussasobhagyasaṃvattaniyaṃ kammaṃ karoti (new)
ABHI = ", ".join([f"{v} {n}" for n, v in SV] + [f"làm nghiệp dẫn đến {x}" for x in KAMMA9])
ST1 = "không tích lũy cũng không giảm trừ, mà đứng vững sau khi đã giảm trừ"   # nevācināti … (ch2 ^5-?)
ST2 = "không dứt bỏ cũng không bám víu, mà đứng vững sau khi đã dứt bỏ"        # neva pajahati … (ch2)
ST3 = "không phân tán cũng không gom tụ, mà đứng vững sau khi đã phân tán"     # neva visineti … (ch2)
ST4 = "không dập tắt cũng không nhen nhóm, mà đứng vững sau khi đã dập tắt"    # neva vidhūpeti … (ch2)
VERBS6 = ["dứt bỏ", "bám víu", "phân tán", "gom tụ", "dập tắt", "nhen nhóm"]   # pajahati … sandhūpeti (ch2)
DANA = f"{AR} có thể thực hiện sự bố thí"                 # arahā dānaṃ dadeyya (ch21 frame)
GIFTS = C21.GIFTS.replace("(Pī.)", "(?)")                 # cīvaraṃ dadeyya … abhidakkhiṇaṃ [padakkhiṇaṃ (?)] kareyya
PAD = f"{AR} {C21.PAD}"                                   # arahā cetiyaṃ abhidakkhiṇaṃ kareyya

# ================================================================ (167) Natthi arahato akālamaccu
AKM = "cái chết không đúng lúc"                          # akālamaccu (kāla «lúc» sample kālavādī «nói đúng lúc»)
T2, T2A = f"{AR} không có {AKM}", f"{AR} có {AKM}"
AG, NAG = f"có kẻ giết {AR}", f"không có kẻ giết {AR}"    # arahantaghātaka (ch3, ch10 KILLERS)
VOR = "tước đoạt mạng sống"                               # jīvitā voropeti (pi-2, ch20)
VOR_A = f"{VOR} của một {AR}"                             # arahantaṃ jīvitā voropeti (pi-2 ^2 ṭhānāṭhāna, ch20)
LV = "khi còn sự sống, còn phần còn lại của sự sống"      # sati jīvite jīvitāvasese (ch19)
DV = "khi không còn sự sống, không còn phần còn lại của sự sống"   # asati jīvite jīvitāvasese (ch19)
BODY = f"thân của {AR}"
POI = C12.poison(BODY)                                    # arahato kāye visaṃ kameyya … (ch12)
NPOI = f"chất độc không thể tác động lên {BODY}, dao kiếm không thể tác động, lửa không thể tác động"   # (ch23)
NAHAM = (C20.NAHAM.replace("khi chưa được cảm nhận, và", "khi chưa được cảm nhận; và")
         .replace(" [dị bản (Tăng Chi Bộ Kinh 10.17): upapajjaṃ]", "").replace(" [Tăng Chi Bộ Kinh 10.217]!", ""))
# ch20 ^5-? wording; here "vadāmi; tañca kho" (semicolon) and upapajjaṃ in the text (no variant, no citation)

# ================================================================ (168) Sabbamidaṃ kammato
T3 = "tất cả điều này đều do nghiệp"                      # sabbamidaṃ kammato
PK = "tất cả điều này đều có nguyên nhân là những gì đã làm trước đây"   # sabbamidaṃ pubbekatahetu
KV = f"tất cả điều này đều do {VIP}"                      # sabbamidaṃ kammavipākato
BYV = f"do {VIP} mà"                                      # kammavipākena
PANA = "việc sát hại sinh mạng"                           # pāṇātipāta (pi-2)
SAPH, APH = "có kết quả", "không có kết quả"              # saphala (sample) / aphala (ch18)
CR = C10.CRIMES                                           # pāṇaṃ haneyya … nigamaghātaṃ kareyya (ch10)
DEEDS = chain([f"có thể {x}" for x in CR[1:]])            # adinnaṃ ādiyeyya…pe… nigamaghātakaṃ kareyya
GIVE4 = chain(["có thể thực hiện sự bố thí"] + [f"có thể cho {x}" for x in (CIV, "đồ ăn khất thực", "chỗ ở", GIL)])
VV = f"[{SPELL} (Pī., Ka., Trung Bộ Kinh 2.460): vattati; {VAR} (?): vattate]"
VERSE3 = [f"“Do nghiệp mà thế gian vận hành {VV}, do nghiệp mà muôn loài vận hành {VV};",
          "Chúng sinh bị nghiệp ràng buộc, như chốt trục của cỗ xe đang chạy [Trung Bộ Kinh 2.460; Kinh Tập 659].",
          "“Do nghiệp mà người ta được danh tiếng, lời khen ngợi,",
          "Do nghiệp mà bị mất mát, bị giết hại và bị giam cầm;",
          "Biết rằng nghiệp ấy tạo nên sự khác biệt,",
          "Tại sao lại nói ở thế gian rằng không có nghiệp”."]
# Kammunā vattatī loko … / Kammena kittiṃ labhate pasaṃsaṃ … ("." after "ti" kept)

# ================================================================ (169) Indriyabaddha
IB = "những gì gắn kết với các năng lực"                  # indriyabaddha (pi-1 anindriyabaddha «không gắn kết với …»)
AIB = "những gì không gắn kết với các năng lực"
T4 = f"chỉ {IB} mới là khổ đau"                           # indriyabaddhaññeva dukkhaṃ
AP3 = "vô thường, do điều kiện tạo thành, sinh khởi tùy thuộc vào điều kiện… có bản chất biến đổi"
AP2 = "vô thường, do điều kiện tạo thành… có bản chất biến đổi"
NOTE = "[cặp câu hỏi này phải đứng trước cặp câu hỏi trước đó]"   # [idaṃ-pucchādvayena purimapucchādvayassa purato bhavitabbaṃ]
YAD = "cái gì vô thường thì cái ấy là khổ đau"            # yadaniccaṃ taṃ dukkhaṃ (ch10)
CIT = "[Tương Ưng Bộ Kinh 3.15]"
VY = f"Đức Thế Tôn đã nói rằng {YAD} {CIT} –"             # yadaniccaṃ taṃ dukkhaṃ [saṃ. ni. 3.15] vuttaṃ bhagavatā –
DK_IB, DK_AIB = "khổ đau gắn kết với các năng lực", "khổ đau không gắn kết với các năng lực"
BRV = "đời sống tu hành trong sạch được sống dưới sự hướng dẫn của Đức Thế Tôn để hiểu biết trọn vẹn"
# pariññāya bhagavati brahmacariyaṃ vussati (brahmacariya pi-1; pariññā ch9)
NOAGAIN = "đã được hiểu biết trọn vẹn, không sinh khởi trở lại"   # pariññātaṃ na puna uppajjati

# ================================================================ (170) Ṭhapetvā ariyamaggaṃ
MG = "con đường cao quý"                                  # ariyamagga (pi-1)
T5 = f"ngoại trừ {MG}, các tạo tác còn lại là khổ đau"    # ṭhapetvā ariyamaggaṃ avasesā saṅkhārā dukkhā
DS = "sự phát sinh của khổ đau"                           # dukkhasamudaya (pi-2, ch21)
DPN = "cách thực hành dẫn đến sự chấm dứt khổ đau"        # dukkhanirodhagāminī paṭipadā (ch10, ch14)
FOUR = f"khổ đau, {DS}, sự chấm dứt khổ đau, {DPN}"
V4 = f"Đức Thế Tôn đã nói rằng có bốn sự thật cao quý – {FOUR}"   # (ch16 «Đức Thế Tôn đã nói rằng có … –»)
ARS = "chỉ có ba sự thật cao quý"                         # tīṇeva ariyasaccāni
SA_DPN = f"nó là {DPN}"                                   # sā dukkhanirodhagāminī paṭipadā

# ================================================================ (171)-(175) saṅgha / buddha
SG, DK = "Tăng đoàn", "phần cúng dường"                   # saṅgha (sample) / dakkhiṇā (ch15)
QUALS = ["xứng đáng được dâng lễ vật", "xứng đáng được tiếp đãi", "xứng đáng nhận phần cúng dường",
         "xứng đáng được chắp tay cung kính", "là ruộng phước vô thượng của thế gian"]
# āhuneyyo pāhuneyyo dakkhiṇeyyo añjalikaraṇīyo anuttaraṃ puññakkhettaṃ lokassa (new)
QUAL = ", ".join(QUALS)
QUAL_PE = f"{QUALS[0]}… {QUALS[-1]}"                      # āhuneyyo…pe… anuttaraṃ puññakkhettaṃ lokassa
PU8 = f"Đức Thế Tôn đã nói rằng bốn đôi người, tám hạng người {QUALS[2]}"
# cattāro purisayugā aṭṭha purisapuggalā dakkhiṇeyyā vuttā bhagavatā (sample ^5-206)
T6 = f"{SG} nhận {DK}"                                    # saṅgho dakkhiṇaṃ paṭiggaṇhāti
T7 = f"{SG} làm thanh tịnh {DK}"                          # saṅgho dakkhiṇaṃ visodheti
T8 = f"{SG} ăn, uống, nhai, nếm"                          # saṅgho bhuñjati pivati khādati sāyati (sāyati «nếm» pi-1)
VC = "vật cúng dường"                                     # dinnaṃ (ch10 ^5 "tesu dinnaṃ mahapphalaṃ")
T9 = f"{VC} cho {SG} có quả lớn"                          # saṅghassa dinnaṃ mahapphalaṃ (mahapphala ch10, ch15)
T10 = f"{VC} cho Đức Phật có quả lớn"                     # buddhassa dinnaṃ mahapphalaṃ
GIVE = f"có một số người thực hiện sự bố thí cho {SG}"    # atthi keci saṅghassa dānaṃ denti (ch15 dānaṃ deti)
GIVE7 = f"có một số người cho {SG} " + chain([CIV] + [f"cho {x}" for x in ("đồ ăn khất thực", "chỗ ở", GIL,
                                                                          "món ăn cứng", "món ăn mềm", "nước uống")])
GIVE_W = f"có một số người cho {SG} nước uống"
ARA = f"làm cho {DK} được thành tựu"                      # dakkhiṇaṃ ārādhenti (aṭṭhakathā: sampādenti)
G2 = f"có một số người, sau khi thực hiện sự bố thí cho {SG}, {ARA}"
G2L = (f"có một số người, sau khi cho {SG} "
       + chain([CIV] + [f"sau khi cho {x}" for x in ("đồ ăn khất thực", "chỗ ở", GIL, "món ăn cứng", "món ăn mềm",
                                                      "nước uống")]) + f", {ARA}")
G2W = f"có một số người, sau khi cho {SG} nước uống, {ARA}"
VERSE6 = ["“Như lửa nhận lễ vật, như đất nhận cơn mưa từ đám mây lớn;",
          f"{SG} thành tựu định tâm, nhận {DK}”."]
# Āhutiṃ jātavedova, mahāmeghaṃva medanī; / Saṅgho samādhisampanno, paṭiggaṇhāti dakkhiṇa"nti.
# (āhuti «lễ vật» as āhuneyya; mahāmegha = the rain, aṭṭhakathā; samādhisampanna pi-4 «thành tựu về định tâm»)
MP = "con đường {v}, thành quả {v}"                       # maggo V-ti, phalaṃ V-ti (ch12 con đường / thành quả)
BH = (f"có một số người tổ chức bữa ăn cho {SG}, tổ chức bữa ăn cho các vị được chỉ định, tổ chức việc dâng cháo")
# saṅghabhattāni / uddesabhattāni / yāgupānāni karonti (yāgu «cháo» sample)
GB = "bữa ăn theo nhóm, bữa ăn thay thế, bữa ăn với thức ăn còn dư, bữa ăn với thức ăn không còn dư"
# gaṇabhojanaṃ paramparabhojanaṃ atirittabhojanaṃ anatirittabhojanaṃ
DR = ["nước xoài", "nước trái trâm", "nước chuối có hạt", "nước chuối không hạt", "nước hoa ma-đu-ca", "nước nho",
      "nước củ súng", "nước trái pha-ru-sa-ca"]
# ambapānaṃ jambu- coca- moca- madhuka- muddika- sāluka- phārusakapānaṃ
DRV = (", ".join(DR[:5]) + f", [{VAR} (Sī., Syā., Kaṃ., Pī.): madhupānaṃ; nhưng cần xem Đại Phẩm 300] "
       + ", ".join(DR[5:]))
EIGHT = "Đức Thế Tôn đã nói rằng có tám loại thức uống – "  # aṭṭha pānāni vuttāni bhagavatā –
GOT = (f"“Này Kiều-đàm-di, hãy dâng cho {SG}, khi bà đã dâng cho {SG}, thì cả Ta sẽ được tôn kính, và cả {SG} nữa” "
       "[Trung Bộ Kinh 3.376]")
# saṅghe, gotami, dehi, saṅghe te dinne ahañceva pūjito bhavissāmi saṅgho cā (Gotamī = Kiều-đàm-di, new)
SAKKA = "Chẳng phải Sakka, vua của chư thiên, đã nói với Đức Thế Tôn thế này sao –"   # (sample etadavoca frame)
SAC = "“Đối với những con người đang tế lễ, những chúng sinh mong cầu phước;"
VERSE9 = [SAC,
          f"Đang tạo phước còn chấp trước, {VC} ở đâu có quả lớn.",
          "“Bốn bậc đang thực hành, và bốn bậc đã đứng vững nơi thành quả;",
          f"Đó là {SG} ngay thẳng, an định trong trí tuệ và giới hạnh.",
          SAC,
          f"Đang tạo phước còn chấp trước, {VC} nơi {SG} có quả lớn” [Tương Ưng Bộ Kinh 1.262; Chuyện Thiên Cung "
          "642, 751].",
          f"“Thật vậy, {SG} này bao la, rộng lớn,",
          "Không thể đo lường, như nước của đại dương;",
          f"Thật vậy, họ là những đệ tử tối thắng của bậc anh hùng giữa loài người [{VAR} (Ka.): narasīhasāvakā],",
          "Những người đem lại ánh sáng, họ tuyên thuyết Giáo Pháp.",
          "“Đối với họ, đó là điều được cho tốt đẹp, được dâng tốt đẹp, được tế lễ tốt đẹp,",
          f"Những ai thực hiện sự bố thí hướng về {SG};",
          f"{cap(DK)} ấy đã đến với {SG}, được đặt vững chắc,",
          "Có quả lớn, được các bậc hiểu biết thế gian tán thán.",
          "“Nhớ lại sự tế lễ như vậy,",
          f"Những ai tràn đầy niềm hoan hỷ, đi lại [{VAR} (Sī., Ka.): viharanti] trong thế gian;",
          "Sau khi loại bỏ vết nhơ keo kiệt cùng với gốc rễ,",
          "Không bị chê trách, họ đi đến nơi chốn cõi trời” [Chuyện Thiên Cung 645, 754]."]
# opadhika «còn chấp trước» (ch10 upadhi); paṭipanna / phale ṭhita (pi-4); mahaggata «rộng lớn» (pi-1);
# lokavidū «bậc hiểu biết thế gian» (pi-4); yajati / yañña «tế lễ»; vi. va. = Chuyện Thiên Cung (new)
DV2 = "giữa loài hai chân"                               # dvipadānaṃ
BQ = (f"Đức Thế Tôn là bậc đứng đầu {DV2}, bậc tối thắng {DV2}, bậc dẫn đầu {DV2}, bậc tối thượng {DV2}, bậc ưu việt "
      f"nhất {DV2}, bậc không ai sánh bằng, bậc ngang bằng với những bậc không ai sánh bằng, bậc không có ai ngang "
      "hàng, bậc không có ai tương tự, bậc không có người đối địch")
# aggo seṭṭho pamokkho uttamo pavaro asamo asamasamo appaṭisamo appaṭibhāgo appaṭipuggalo (commas rendered)
SS = "có ai đó hoàn toàn ngang bằng với Đức Phật – về giới hạnh, định tâm, trí tuệ"   # samasama (sample)
NSS = "không có ai hoàn toàn ngang bằng với Đức Phật – về giới hạnh, định tâm, trí tuệ"
VERSE10 = ["“Không ở thế gian này, cũng không ở thế gian khác,",
           "Có ai tối thắng hơn hay ngang bằng với Đức Phật;",
           f"Bậc đã đạt đến vị trí đứng đầu giữa những bậc {QUALS[0]},",
           "Cho những người cầu phước, mong tìm quả bao la” [Chuyện Thiên Cung 1047]."]

# ================================================================ (176) Dakkhiṇāvisuddhi
DY, PT = "người bố thí", "người nhận"                     # dāyaka / paṭiggāhaka (ch15)
T11 = f"sự bố thí được thanh tịnh chỉ từ phía {DY}, không phải từ phía {PT}"   # dāyakatova dānaṃ visujjhati, no …
RQ = f"có một số {PT} {QUAL}"                             # atthi keci paṭiggāhakā āhuneyyā …
SO3 = f"có một số người, sau khi thực hiện sự bố thí cho bậc vào dòng, {ARA}"   # sotāpanne (pi-4)
AK = ("một người là người làm cho một người khác, sự dễ chịu và sự khó chịu do người khác làm ra, một người làm, "
      "một người khác cảm nhận")
# añño aññassa kārako (ch15, ch24), parakataṃ sukhadukkhaṃ (sample ^5-173 paraṅkataṃ sukhadukkhaṃ), añño karoti …
AN = "Này A-nan"                                          # ānanda (terms file)
an = "này A-nan"


def dv(how):
    return f"có {DK} {how}"


SUTTA11 = (f"“{AN}, có bốn sự thanh tịnh của {DK} này! Bốn điều nào? {AN}, "
           f"{dv(f'được thanh tịnh từ phía {DY}, không phải từ phía {PT}')}; {an}, "
           f"{dv(f'được thanh tịnh từ phía {PT}, không phải từ phía {DY}')}; {an}, "
           f"{dv(f'được thanh tịnh cả từ phía {DY} lẫn từ phía {PT}')}; {an}, "
           f"{dv(f'không được thanh tịnh từ phía {DY}, cũng không từ phía {PT}')}. "
           f"{AN}, đây là bốn sự thanh tịnh của {DK}” [Trung Bộ Kinh 3.381]")

# ================================================================ kathā names (headings and closing lines)
KX = {1: f"{PU} của {AR}",                                # Arahato puññūpacayakathā (terms file)
      2: f"việc cho rằng {T2}",                           # Natthi arahato akālamaccūtikathā
      3: f"việc cho rằng {T3}",                           # Sabbamidaṃ kammatotikathā
      4: IB,                                              # Indriyabaddhakathā (ch15 «những gì …»)
      5: f"việc cho rằng ngoại trừ {MG}",                 # Ṭhapetvā ariyamaggantikathā (as written, ch11 Ariyantikathā)
      6: f"việc cho rằng không nên nói {T6}",             # Na vattabbaṃ saṅgho dakkhiṇaṃ paṭiggaṇhātītikathā
      7: f"việc cho rằng không nên nói {T7}",
      8: f"việc cho rằng không nên nói {SG} ăn",          # Na vattabbaṃ saṅgho bhuñjatītikathā
      9: f"việc cho rằng không nên nói {T9}",             # … saṅghassadinnaṃ / saṅghassa dinnaṃ (one wording)
      10: f"việc cho rằng không nên nói {T10}",
      11: f"sự thanh tịnh của {DK}"}                      # Dakkhiṇāvisuddhikathā
END1 = E(x=f"việc cho rằng {T1}")                         # Atthi arahato puññūpacayotikathā niṭṭhitā. (as written)


def heads(n):
    """#### Sattarasamavaggo ^5-25-n-0 / ##### (165+n) n. <title> ^5-25-n-1-0"""
    return [(4, VAGGA17, f"5-25-{n}-0"), (5, f"({165 + n}) {n}. {K(x=KX[n])}", f"5-25-{n}-1-0")]


UDDANA = (f"{cap(T1)}, {T2}, {T3}, {T4}, {T5}, {T6}, {T7}, {T8}, {T9}, có sự bố thí vì sự thanh tịnh "
          f"[{VAR} (Syā.): visujjhatīti].")
# Atthi arahato puññūpacayo, … saṅghassa dinnaṃ mahapphalaṃ, atthi dānaṃ visuddhiyāti [visujjhatīti (syā.)]


def build():
    d = B.Doc()
    d.head(3, VAGGA17, "5-25-0")
    # ------------------------------------------------------------ (166) Arahato puññūpacaya
    d.head(4, f"(166) 1. {K(x=KX[1])}", "5-25-1-0")
    d.seg("5-776", f"{Q(T1)} {AM} {Q(T1A)} {NHP} {q(N1A)} {AM} {Q(N1)} {NHP}")
    d.seg("5-777", f"{Q(T1)} {AM} {Q(f'{AR} {ABHI}')} {NHP}")
    d.seg("5-778",
          f"{Q(T1)} {AM} {Q(f'{AR} tích lũy')} {NHP} {q(f'{AR} giảm trừ')} {NHP} "
          f"{q(chain([f'{AR} {v}' for v in VERBS6]))} {NHP} {nanu_l(f'{AR} {ST1}')} {AM} "
          f"{hanci_no(f'{AR} {ST1}', T1)}",
          f"{NANU(f'{AR} {ST2}, {ST3}, {ST4}')} {AM} {hanci_no(f'{AR} {ST4}', T1)}")
    d.seg("5-779",
          f"{Q(N1)} {AM} {Q(DANA)} {AM} {hanci_no(DANA, N1)}",
          f"{Q(f'{AR} {GIFTS}')} {AM} {hanci_no(PAD, N1)}",
          END1)
    # ------------------------------------------------------------ (167) Natthi arahato akālamaccu
    for lv, t, sid in heads(2):
        d.head(lv, t, sid)
    d.seg("5-780",
          f"{Q(T2)} {AM} {Q(NAG)} {NHP} {q(AG)} {AM} {Q(T2A)} {NHP} {q(T2)} {AM} "
          f"Người nào {VOR_A}, thì {VOR} {LV}, hay {VOR} {DV}? {cap(VOR)} {LV}. {hanci_no(f'{VOR} {LV}', T2)} "
          f"Có phải nếu {VOR} {DV}, thì {NAG} không? {NHP}")
    d.seg("5-781",
          f"{Q(T2)} {AM} {Q(NPOI)} {NHP} {nanu_l(POI)} {AM} {hanci_no(POI, T2)}",
          f"{Q(NPOI)} {AM} {Q(NAG)} {NHP}")
    d.seg("5-782",
          f"{Q(T2A)} {AM} {NANU_VUTTAM} {NAHAM}. {ATTHEVA} {AM} {TENA_HI(T2)}",
          E(x=KX[2]))
    # ------------------------------------------------------------ (168) Sabbamidaṃ kammato
    for lv, t, sid in heads(3):
        d.head(lv, t, sid)
    d.seg("5-783", f"{Q(T3)} {AM} {Q('nghiệp cũng do nghiệp')} {NHP} {q(T3)} {AM} {Q(PK)} {NHP} {q(T3)} {AM} "
                   f"{Q(KV)} {NHP}")
    d.seg("5-784",
          f"{Q(KV)} {AM} {Q(f'{BYV} có thể {CR[0]}')} {AM} {Q(f'{PANA} {SAPH}')} {AM} {Q(f'{VIP} {SAPH}')} {NHP} "
          f"{q(f'{VIP} {APH}')} {AM} {Q(f'{PANA} {APH}')} {NHP}",
          f"{Q(f'{BYV} {DEEDS}… {BYV} {GIVE4}')} {AM} {Q(f'{GIL} {SAPH}')} {AM} {Q(f'{VIP} {SAPH}')} {NHP} "
          f"{q(f'{VIP} {APH}')} {AM} {Q(f'{GIL} {APH}')} {NHP}")
    d.seg("5-785",
          f"{NVQ(T3)} {AM} {NANU_VUTTAM}",
          *VERSE3,
          f"{ATTHEVA} {AM} Vậy thì “{T3}”.",
          E(x=KX[3]))
    # ------------------------------------------------------------ (169) Indriyabaddha
    for lv, t, sid in heads(4):
        d.head(lv, t, sid)
    d.seg("5-786",
          f"{Q(T4)} {AM} {Q(f'chỉ {IB} mới là {ANICCA}')} {NHP} {nanu_l(f'{AIB} là {ANICCA}')} {AM} "
          f"{hanci_no(f'{AIB} là {ANICCA}', T4)}",
          f"{Q(f'{AIB} là {AP3}, và nó không phải là khổ đau')} {AM} "
          f"{Q(f'{IB} là {AP2}, và nó không phải là khổ đau')} {NHP}",
          f"Có phải {IB} là {AP2}, và nó là khổ đau {NOTE} không? {AM} "
          f"Có phải {AIB} là {AP2}, và nó là khổ đau {NOTE} không? {NHP}")
    d.seg("5-787",
          f"{Q(T4)} {AM} Chẳng phải {VY} “{AIB} là vô thường” sao? {AM} "
          f"Nếu {VY} {AIB} là vô thường, {B.NO_CA_VATA} “{T4}”.")
    d.seg("5-788",
          f"{NVQ(T4)} {AM} Có phải giống như {BRV} {DK_IB}, cũng vậy, {BRV} {DK_AIB} không? {NHP} "
          f"có phải giống như {DK_IB}, {NOAGAIN}, cũng vậy, {DK_AIB}, {NOAGAIN} không? {NH} {TENA_HI(T4)}",
          E(x=KX[4]))
    # ------------------------------------------------------------ (170) Ṭhapetvā ariyamaggaṃ
    for lv, t, sid in heads(5):
        d.head(lv, t, sid)
    ds_too = f"{DS} cũng là khổ đau"
    d.seg("5-789",
          f"{Q(T5)} {AM} {Q(ds_too)} {NHP} {q(ds_too)} {AM} {Q(ARS)} {NHP} {q(ARS)} {AM} Chẳng phải {V4} sao? "
          f"{AM} {hanci_no(V4, ARS, sep=';')}",
          f"{Q(ds_too)} {AM} Theo nghĩa nào? Theo nghĩa vô thường. {Q(f'{MG} là vô thường')} {AM} "
          f"{Q(f'{MG} là khổ đau')} {NHP}",
          f"{Q(f'{MG} là vô thường, và nó không phải là khổ đau')} {AM} "
          f"{Q(f'{DS} là vô thường, và nó không phải là khổ đau')} {NHP} {q(f'{DS} là vô thường, và nó là khổ đau')} "
          f"{AM} {Q(f'{MG} là vô thường, và nó là khổ đau')} {NHP}")
    d.seg("5-790",
          f"{NVQ(T5)} {AM} {NANU(SA_DPN)} {AM} {hanci_yes(SA_DPN, T5)}",
          E(x=KX[5]))
    # ------------------------------------------------------------ (171) saṅgho dakkhiṇaṃ paṭiggaṇhāti
    for lv, t, sid in heads(6):
        d.head(lv, t, sid)
    d.seg("5-791",
          f"{NVQ(T6)} {AM} {NANU(f'{SG} {QUAL}')} {AM} {hanci_yes(f'{SG} {QUAL}', T6)}",
          f"{NVQ(T6)} {AM} {NANU(PU8)} {AM} {hanci_yes(PU8, T6)}",
          f"{NVQ(T6)} {AM} {NANU(GIVE)} {AM} {hanci_yes(GIVE, T6)} {NANU(GIVE7)} {AM} {hanci_yes(GIVE_W, T6)}",
          f"{NVQ(T6)} {AM} {NANU_VUTTAM}",
          *VERSE6,
          f"{ATTHEVA} {AM} {TENA_HI(T6)}")
    d.seg("5-792",
          f"{Q(T6)} {AM} {Q(MP.format(v='nhận'))} {NHP}",
          E(x=KX[6]))
    # ------------------------------------------------------------ (172) saṅgho dakkhiṇaṃ visodheti
    for lv, t, sid in heads(7):
        d.head(lv, t, sid)
    d.seg("5-793",
          f"{NVQ(T7)} {AM} {NANU(f'{SG} {QUAL}')} {AM} {hanci_yes(f'{SG} {QUAL_PE}', T7)}",
          f"{NVQ(T7)} {AM} {NANU(PU8)} {AM} {hanci_yes(PU8, T7)}",
          f"{NVQ(T7)} {AM} {NANU(G2)} {AM} {hanci_yes(G2, T7)}",
          f"{NANU(G2L)} {AM} {hanci_yes(G2W, T7)}")
    d.seg("5-794",
          f"{Q(T7)} {AM} {Q(MP.format(v='làm thanh tịnh'))} {NHP}",
          E(x=KX[7]))
    # ------------------------------------------------------------ (173) saṅgho bhuñjati
    for lv, t, sid in heads(8):
        d.head(lv, t, sid)
    d.seg("5-795",
          f"{NVQ(T8)} {AM} {NANU(BH)} {AM} {hanci_yes(BH, T8)}",
          f"{NVQ(T8)} {AM} Chẳng phải Đức Thế Tôn đã nói – “{GB}” sao? {AM} "
          f"Nếu Đức Thế Tôn đã nói – “{GB}”, {B.TENA_VATA} “{T8}”.",
          f"{NVQ(T8)} {AM} Chẳng phải {EIGHT}{DRV} sao? {AM} {hanci_yes(EIGHT + ', '.join(DR), T8)}")
    d.seg("5-796",
          f"{Q(T8)} {AM} {Q(MP.format(v='ăn, uống, nhai, nếm'))} {NHP}",
          E(x=KX[8]))
    # ------------------------------------------------------------ (174) saṅghassa dinnaṃ mahapphalaṃ
    for lv, t, sid in heads(9):
        d.head(lv, t, sid)
    d.seg("5-797",
          f"{NVQ(T9)} {AM} {NANU(f'{SG} {QUAL}')} {AM} {hanci_yes(f'{SG} {QUAL_PE}', T9)}",
          f"{NVQ(T9)} {AM} {NANU(PU8)} {AM} {hanci_yes(PU8, T9)}")
    d.seg("5-798",
          f"{NVQ(T9)} {AM} {NANU_VUTTAM} {GOT}. {ATTHEVA} {AM} {TENA_HI(T9)}",
          f"{NVQ(T9)} {AM} {SAKKA}",
          *VERSE9,
          f"{ATTHEVA} {AM} {TENA_HI(T9)}",
          E(x=KX[9]))
    # ------------------------------------------------------------ (175) buddhassa dinnaṃ mahapphalaṃ
    for lv, t, sid in heads(10):
        d.head(lv, t, sid)
    d.seg("5-799",
          f"{NVQ(T10)} {AM} {NANU(BQ)} {AM} {hanci_yes(BQ, T10)}",
          f"{NVQ(T10)} {AM} {Q(SS)} {NATTHI} {hanci_yes(NSS, T10)}",
          f"{NVQ(T10)} {AM} {NANU_VUTTAM}",
          *VERSE10,
          f"{ATTHEVA} {AM} {TENA_HI(T10)}",
          E(x=KX[10]))
    # ------------------------------------------------------------ (176) Dakkhiṇāvisuddhi
    for lv, t, sid in heads(11):
        d.head(lv, t, sid)
    d.seg("5-800",
          f"{Q(T11)} {AM} {NANU(RQ)} {AM} {hanci_no(RQ, T11)}",
          f"{Q(T11)} {AM} {NANU(PU8)} {AM} {hanci_no(PU8, T11)}",
          f"{Q(T11)} {AM} {NANU(SO3)} {AM} {hanci_no(SO3, T11)}",
          f"Chẳng phải có một số người, sau khi thực hiện sự bố thí cho bậc trở lại một lần… cho bậc không trở "
          f"lại… cho {AR}, {ARA} sao? {AM} "
          f"{hanci_no(f'có một số người, sau khi thực hiện sự bố thí cho {AR}, {ARA}', T11)}")
    d.seg("5-801",
          f"{Q(f'sự bố thí được thanh tịnh từ phía {PT}')} {AM} {Q(AK)} {NHP}",
          f"{Q(T11)} {AM} {NANU_VUTTAM} {SUTTA11}. {ATTHEVA} {AM} {B.TENA_HI_NA(T11)}",
          E(x=KX[11]),
          f"{VAGGA17}.",
          TASSUDDANAM,
          UDDANA)
    return d.text()


# ================================================================ cross-book asserts (pi-1..4 rails)
CROSS = [
    ("Sự tạo tác thuộc về phước", 2), ("sự tạo tác dẫn đến trạng thái bất động", 2),
    ("không gắn kết với các năng lực", 1), ("tước đoạt mạng sống của một bậc A-la-hán", 2),
    ("đoàn tùy tùng", 2), ("có của cải lớn", 4), ("con đường cao quý", 1), ("rộng lớn", 1),
    ("bậc hiểu biết thế gian", 4), ("thành tựu về định tâm", 4), ("sự hiện hữu", 2), ("hạng người", 4),
    ("Trung Bộ Kinh", 4), ("Tăng Chi Bộ Kinh", 4), ("sự phát sinh của khổ đau", 2), ("hiểu biết trọn vẹn", 2),
    ("vòng hoa, hương thơm, dầu thoa", 4), ("việc sát hại sinh mạng", 2), ("bậc vào dòng", 4),
    ("bậc trở lại một lần", 4), ("bậc không trở lại", 4), ("nếm", 1), ("đời sống tu hành trong sạch", 1),
]
# ================================================================ finished pi-5 chapters (zero-shot outputs)
PI5 = [
    (f"Có phải {AR} tích lũy không? {NH} Có phải {AR} giảm trừ không?", "2-parihanikatha.md"),
    (f"{AR} {ST1}", "2-parihanikatha.md"), (f"{AR} {ST2}", "2-parihanikatha.md"),
    (f"{AR} {ST3}", "2-parihanikatha.md"), (f"{AR} {ST4}", "2-parihanikatha.md"),
    ("kẻ giết bậc A-la-hán", "3-brahmacariyakatha.md"), ("theo nghĩa nào", "3-brahmacariyakatha.md"),
    (TASSUDDANAM, "9-hevatthikatha.md"), (", ".join(CR), "10-dutiyavaggo.md"),
    (f"“{YAD}", "10-dutiyavaggo.md"), ("vật cúng dường cho họ có quả lớn", "10-dutiyavaggo.md"),
    ("sự chấm dứt khổ đau", "10-dutiyavaggo.md"), (DPN, "10-dutiyavaggo.md"), ("còn chấp trước", "10-dutiyavaggo.md"),
    (f"Có phải {AR} có sự không biết không?", "10-dutiyavaggo.md"), ("quyền uy", "10-dutiyavaggo.md"),
    (POI, "12-catutthavaggo.md"), ("con đường", "12-catutthavaggo.md"), ("thành quả", "12-catutthavaggo.md"),
    ("sự thật cao quý", "12-catutthavaggo.md"), ("Đại Phẩm 15", "12-catutthavaggo.md"),
    ("người bố thí thực hiện sự bố thí", "15-sattamavaggo.md"), ("người nhận", "15-sattamavaggo.md"),
    ("phần cúng dường", "15-sattamavaggo.md"), ("nghiệp dẫn đến quyền uy, nghiệp dẫn đến quyền thống trị",
                                               "15-sattamavaggo.md"),
    ("món ăn cứng", "15-sattamavaggo.md"), ("Bốn điều nào?", "15-sattamavaggo.md"),
    ("Có phải một người là người làm cho một người khác", "15-sattamavaggo.md"), ("có quả lớn", "15-sattamavaggo.md"),
    ("Này các tỳ-khưu, đây là bốn điều rất xa cách nhau.", "15-sattamavaggo.md"),
    ("Đức Thế Tôn đã nói rằng có năm cõi tái sinh –", "16-atthamavaggo.md"), ("không có kết quả", "18-dasamavaggo.md"),
    ("điều không phải phước", "18-dasamavaggo.md"), (LV, "19-ekadasamavaggo.md"), (DV, "19-ekadasamavaggo.md"),
    ("nghiệp có chủ ý", "20-dvadasamavaggo.md"), ("tước đoạt mạng sống của một bậc A-la-hán", "20-dvadasamavaggo.md"),
    (C21.GIFTS, "21-terasamavaggo.md"), (f"có thể thực hiện sự bố thí", "21-terasamavaggo.md"),
    (DS, "21-terasamavaggo.md"), (NATTHI, "22-cuddasamavaggo.md"),
    ("chất độc không thể tác động lên", "23-pannarasamavaggo.md"), ("tạo tác sự tạo tác bằng thân", "23-pannarasamavaggo.md"),
    (AK.split(", sự dễ chịu")[0], "24-solasamavaggo.md"),
    ("sự dễ chịu và sự khó chịu do người khác làm ra", "1-puggalakatha.md"), ("bốn đôi người, tám hạng người",
                                                                           "1-puggalakatha.md"),
    ("hoàn toàn ngang bằng", "1-puggalakatha.md"), ("Có phải có ai đó", "1-puggalakatha.md"), ("cháo", "1-puggalakatha.md"),
    ("và nó không phải là", "8-satipatthanakatha.md"), ("thế gian khác", "1-puggalakatha.md"),
]


def check_cross():
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(dd.glob("*.md")))
             for b, dd in B.RAILS_DIR.items()}
    missing = [(st, f"pi-{b}") for st, b in CROSS if st not in texts[b]]
    missing += [(st, f) for st, f in PI5 if st not in (B.OUT_DIR / f).read_text(encoding="utf-8")]
    for st, w in missing:
        print(f"CROSS MISSING in {w}: {st}")
    assert not missing, f"{len(missing)} cross strings not found"
    assert NAHAM != C20.NAHAM and "upapajjaṃ" not in NAHAM and "; và điều ấy" in NAHAM, "NAHAM derivation"
    assert "(?)" in GIFTS and GIFTS != C21.GIFTS, "GIFTS derivation"
    print(f"ch25 cross asserts: {len(CROSS)} pi-1..4 strings, {len(PI5)} pi-5 chapter strings found")


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
