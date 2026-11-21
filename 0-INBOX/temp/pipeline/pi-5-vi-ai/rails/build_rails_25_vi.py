"""pi-5 Kathāvatthu, Vietnamese RAILS (plain audience): chapter 25, Sattarasamavaggo (^5-25-0 … ^5-801): eleven
kathās (166-176) with the repeated "Sattarasamavaggo" sub-headings, the vagga close and the uddāna.

Builds AI_translation/vietnamese/pi-5-vietnamese-plain-rails_split_chapters/25-sattarasamavaggo.md from the fixed
strings below, importing the approved sample builder READ-ONLY (frames Q, q, NANU, hanci, hanci_neg, na_vattabbam,
tena_hi, tena_hi_na, neu, katha, katha_end, var, var_sp …). Strings taken from pi-1 … pi-4 rails are asserted there
(REUSED25); strings shared with the finished pi-5 rails chapters 1-20 are asserted in those chapter files (SHARED).
The per-line dash / quote / NFC / id checks of S.check_against_pali run before writing.
New recurring strings: notes-rails-25.md.

usage: python -I -X utf8 -B build_rails_25_vi.py          (writes the chapter and the adherence copy rails\\adh-25\\)
"""
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai\rails")
import build_rails_sample_vi as S  # noqa: E402

NAME = "25-sattarasamavaggo.md"
Q, q, NANU, PE, YES, NO, NO_PE = S.Q, S.q, S.NANU, S.PE, S.YES, S.NO, S.NO_PE
hanci, hanci_neg, na_vattabbam = S.hanci, S.hanci_neg, S.na_vattabbam
cap = S.cap
CIT = S.CIT


def nanu_l(x):                      # nanu Xti? (after …pe…, lower case)
    return f"chẳng phải {x} sao?"


# ---------------------------------------------------------------------------------------------------------------
# Shared vocabulary (termbase; pi-1 … pi-4; finished pi-5 chapters)
# ---------------------------------------------------------------------------------------------------------------
BH = "Này các tỳ-khưu"                                                  # bhikkhave (sample)
ARH = S.PN["arahā"]                                                     # bậc A-la-hán (pi-4)
SG = "Tăng đoàn"                                                        # saṅgho (sample / termbase)
VAGGA = "Chương thứ mười bảy"                                           # Sattarasamavaggo (termbase)
TASSUDDANAM = "Tóm tắt của chương này –"                               # Tassuddānaṃ – (ch9)
C_SN, C_MN = CIT["saṃ. ni."], CIT["ma. ni."]
C_VV = "Chuyện Thiên Cung"                                              # vi. va. (new)
C_SU = CIT["su. ni."]
C_MV = "Đại Phẩm"                                                       # mahāva. (ch2 / ch10)

# gifts (ch13 / ch15; same order as ch21)
CIV, PIN, SEN, GIL = "y phục", "đồ ăn khất thực", "chỗ ở", "thuốc men và vật dụng chữa bệnh"
KHA, BHO, PAN = "món ăn cứng", "món ăn mềm", "nước uống"
DANA = "thực hiện sự bố thí"                                            # dānaṃ deti / dadeyya (ch15; termbase)
AR = "làm cho phần cúng dường được thành tựu"                           # dakkhiṇaṃ ārādhenti (termbase)

# Kathā 1
PU, APU = "sự tích lũy phước", "sự tích lũy điều không phải phước"     # puññūpacayo / apuññūpacayo (termbase)
T1, T1N = f"{ARH} có {PU}", f"{ARH} không có {PU}"
A1, A1N = f"{ARH} có {APU}", f"{ARH} không có {APU}"
PUB = "sự tạo tác thuộc về phước"                                       # puññābhisaṅkhāro (pi-2)
ANE = "sự tạo tác dẫn đến trạng thái bất động"                          # āneñjābhisaṅkhāro (pi-2)
ADHI_V = S.var_sp("?", "ādhipaccasaṃvattanikaṃ")
DEEDS = ["cõi tái sinh", "sự hiện hữu", "quyền uy", "quyền thống trị" + ADHI_V, "tài sản lớn", "đoàn tùy tùng lớn",
         "sự vinh hiển giữa chư thiên", "sự vinh hiển giữa loài người"]
#   gati- bhava- issariya- adhipacca- mahābhoga- mahāparivāra- devasobhagya- manussasobhagyasaṃvattaniyaṃ kammaṃ
AC = f"{ARH} không tích lũy cũng không giảm trừ, đứng vững sau khi đã giảm trừ"   # nevācināti … (ch2 frame)
PAJ = "không dứt bỏ cũng không bám víu, đứng vững sau khi đã dứt bỏ"          # (ch2)
VIS = "không phân tán cũng không gom tụ, đứng vững sau khi đã phân tán"         # (ch2)
VID = "không dập tắt cũng không nhen nhóm, đứng vững sau khi đã dập tắt"        # (ch2)
CET = "bảo tháp"                                                        # cetiyaṃ (termbase)
ABHID = f"đi nhiễu quanh {CET} theo chiều bên phải"                      # cetiyaṃ abhidakkhiṇaṃ kareyya (termbase)
GIFT_ARH = (f"cho {CIV}{PE} cho {PIN}{PE} cho {SEN}{PE} cho {GIL}{PE} cho {KHA}{PE} cho {BHO}{PE} cho {PAN}{PE} "
            f"đảnh lễ {CET}{PE} dâng vòng hoa lên {CET}{PE} dâng hương thơm{PE} dâng dầu thoa{PE} "
            f"{ABHID}{S.var('?', 'padakkhiṇaṃ')}")

# Kathā 2
T2, T2P = f"{ARH} không có cái chết không đúng lúc", f"{ARH} có cái chết không đúng lúc"   # akālamaccu (termbase)
KG = "kẻ giết bậc A-la-hán"                                             # arahantaghātako (ch3)
SATI = "khi có sự sống, có phần còn lại của sự sống"                    # sati jīvite jīvitāvasese (ch19)
ASATI = "khi không có sự sống, không có phần còn lại của sự sống"       # asati … (ch19)
VOR = "tước đoạt mạng sống"                                             # jīvitā voropeti (pi-2; ch20)
POIS = f"chất độc có thể tác động lên thân của {ARH}, dao kiếm có thể tác động, lửa có thể tác động"   # (ch12)
NPOIS = (f"chất độc không thể tác động lên thân của {ARH}, dao kiếm không thể tác động, "
         "lửa không thể tác động")
SUT_K = (f"“{BH}, Ta không nói rằng có sự chấm dứt của các nghiệp có chủ ý đã làm, đã được tích lũy, khi chúng "
         f"chưa được cảm nhận; và điều ấy là {S.DITTHE}, hoặc trong lần tái sinh kế tiếp, hoặc trong một lượt khác "
         "về sau”.")
#   nāhaṃ, bhikkhave, sañcetanikānaṃ kammānaṃ katānaṃ upacitānaṃ appaṭisaṃveditvā byantībhāvaṃ vadāmi; tañca kho
#   diṭṭheva dhamme upapajjaṃ vā apare vā pariyāye (ch20 ^5-635 wording)

# Kathā 3
T3 = "tất cả điều này đều do nghiệp"                                    # sabbamidaṃ kammato (kammato termbase)
KV = "do quả của nghiệp"                                                # kammavipākato / kammavipākena (termbase)
T3V = f"tất cả điều này đều {KV}"
EVIL = ("lấy của không được cho", "nói dối", "nói lời chia rẽ", "nói lời thô ác", "nói lời phù phiếm", "đột nhập nhà",
        "cướp bóc", "cướp một ngôi nhà", "mai phục bên đường", "đi lại với vợ người khác", "cướp phá làng",
        "cướp phá thị trấn")                                            # (ch10 aññāṇakathā list)
VAR_VT = " [khác chính tả (Pī., Ka., Trung Bộ Kinh 2.460): vattati; dị bản (?): vattate]"
#   [vattati (pī. ka., ma. ni. 2.460), vattate (?)]

# Kathā 4
IB, AIB = "điều gắn kết với các năng lực", "điều không gắn kết với các năng lực"   # (an)indriyabaddhaṃ (pi-1)
T4 = f"chỉ {IB} mới là khổ đau"                                          # indriyabaddhaññeva dukkhaṃ
AN1 = "vô thường, do điều kiện tạo thành, sinh khởi tùy thuộc vào điều kiện… có bản chất biến đổi"
AN2 = "vô thường, do điều kiện tạo thành… có bản chất biến đổi"
NOTE4 = " [cặp câu hỏi này nên đứng trước cặp câu hỏi trước đó]"
#   [idaṃ-pucchādvayena purimapucchādvayassa purato bhavitabbaṃ]
YAD = "cái gì vô thường thì cái ấy là khổ đau"                          # yadaniccaṃ taṃ dukkhaṃ (ch10)
C315 = f" [{C_SN} 3.15]"
IBD, AIBD = "khổ đau gắn kết với các năng lực", "khổ đau không gắn kết với các năng lực"   # (an)indriyabaddhaṃ dukkhaṃ
BRV = "đời sống tu hành trong sạch được sống theo Đức Thế Tôn"           # bhagavati brahmacariyaṃ vussati

# Kathā 5
T5 = "ngoại trừ con đường cao quý, các tạo tác còn lại là khổ đau"
DS = "sự phát sinh của khổ đau"                                         # dukkhasamudayo (ch10)
PAT = "cách thực hành dẫn đến sự chấm dứt khổ đau"                      # dukkhanirodhagāminī paṭipadā (ch10)
AS4 = f"khổ đau, {DS}, sự chấm dứt khổ đau, {PAT}"
CA4 = f"Đức Thế Tôn đã nói về bốn sự thật cao quý – {AS4}"
TINE = "chỉ có ba sự thật cao quý"
MG = "con đường cao quý"

# Kathās 6-9: worthiness of the Order
WORTHY = ("xứng đáng được dâng lễ vật, xứng đáng được tiếp đãi, xứng đáng nhận phần cúng dường, "
          "xứng đáng được chắp tay cung kính, là ruộng phước không có điều gì cao hơn cho thế gian")
WORTHY_PE = "xứng đáng được dâng lễ vật… là ruộng phước không có điều gì cao hơn cho thế gian"
P8 = "Đức Thế Tôn đã nói rằng bốn đôi người, tám hạng người xứng đáng nhận phần cúng dường"   # (ch1; ch15 «đã nói rằng»)
T6 = f"{SG} nhận phần cúng dường"
T7 = f"{SG} làm thanh tịnh phần cúng dường"
T8 = f"{SG} ăn, uống, nhai, nếm"
T9 = f"điều được bố thí cho {SG} có quả lớn"                             # saṅghassa dinnaṃ mahapphalaṃ (ch10 «có quả lớn»)
T10 = "điều được bố thí cho Đức Phật có quả lớn"
NV = "việc không nên nói rằng"                                          # Na vattabbaṃ …-kathā
BJ = "bữa ăn theo nhóm, bữa ăn thay thế, bữa ăn còn dư, bữa ăn không còn dư"
DRINKS = ["nước xoài", "nước trái trâm", "nước chuối có hạt", "nước chuối không hạt", "nước hoa ma-đu-ca",
          "nước nho", "nước củ súng", "nước trái pha-ru-sa-ca"]           # (termbase)
VAR_MADHU = f" [dị bản (Sī., Syā., Kaṃ., Pī.): madhupānaṃ; nhưng cần xem {C_MV} 300]"
#   [madhupānaṃ (sī. syā. kaṃ. pī.) mahāva. 300 pana passitabbaṃ]
DRV = ", ".join(DRINKS[:5]) + "," + VAR_MADHU + " " + ", ".join(DRINKS[5:])
DR = ", ".join(DRINKS)

# Kathā 10
DV = "loài hai chân"
EP = (f"bậc hàng đầu của {DV}, bậc tối thắng của {DV}, bậc dẫn đầu của {DV}, bậc tối thượng của {DV}, "
      f"bậc ưu việt nhất của {DV}, bậc không ai sánh bằng, bậc ngang bằng với những bậc không ai sánh bằng, "
      "bậc không ai ngang hàng, bậc không ai tương tự, bậc không ai sánh ngang")
#   dvipadānaṃ aggo … seṭṭho … pamokkho … uttamo … pavaro asamo asamasamo appaṭisamo appaṭibhāgo appaṭipuggalo
SAMA = "ai hoàn toàn ngang bằng với Đức Phật – về giới hạnh, về định tâm, về trí tuệ"   # buddhena samasamo – …

# Kathā 11
T11 = "sự bố thí được thanh tịnh chỉ từ phía người bố thí, không phải từ phía người nhận"
KARAKO = ("một người là người tạo cho người khác, sự dễ chịu và sự khó chịu do người khác làm ra, một người làm, "
          "một người khác cảm nhận")                                    # Añño aññassa kārako … (ch15)
SUT_A = ("“Này A-nan, có bốn sự thanh tịnh này của phần cúng dường! Bốn sự thanh tịnh nào? Này A-nan, có phần "
         "cúng dường được thanh tịnh từ phía người bố thí, không phải từ phía người nhận; này A-nan, có phần cúng "
         "dường được thanh tịnh từ phía người nhận, không phải từ phía người bố thí; này A-nan, có phần cúng dường "
         "được thanh tịnh cả từ phía người bố thí lẫn từ phía người nhận; này A-nan, có phần cúng dường không được "
         "thanh tịnh từ phía người bố thí, cũng không từ phía người nhận. Này A-nan, đây là bốn sự thanh tịnh của "
         f"phần cúng dường” [{C_MN} 3.381].")

KATHA = {1: f"{PU} của {ARH}", 2: f"việc {T2}", 3: f"việc {T3}", 4: IB, 5: f"việc ngoại trừ {MG}",
         6: f"{NV} {T6}", 7: f"{NV} {T7}", 8: f"{NV} {SG} ăn", 9: f"{NV} {T9}", 10: f"{NV} {T10}",
         11: "sự thanh tịnh của phần cúng dường"}
KATHA_END1 = f"việc {T1}"            # Atthi arahato puññūpacayotikathā (the close differs from the heading)
UDDANA = (f"{cap(T1)}, {T2}, {T3}, {T4}, {T5}, {T6}, {T7}, {T8}, {T9}, có sự bố thí vì sự thanh tịnh"
          f"{S.var('Syā.', 'visujjhatīti')}.")
#   Atthi arahato puññūpacayo, …, saṅghassa dinnaṃ mahapphalaṃ, atthi dānaṃ visuddhiyāti [visujjhatīti (syā.)].

REUSED25 = [  # (Pāli, Vietnamese, book)
    ("puññābhisaṅkhāro", "Sự tạo tác thuộc về phước", "2"),
    ("āneñjābhisaṅkhāro", "sự tạo tác dẫn đến trạng thái bất động", "2"),
    ("anindriyabaddha-", "không gắn kết với các năng lực", "1"),
    ("arahā", ARH, "4"),
]

SHARED = [  # (Pāli, Vietnamese, finished pi-5 rails chapter)
    ("cattāro purisayugā aṭṭha purisapuggalā", "bốn đôi người, tám hạng người", "1-puggalakatha.md"),
    ("samasamo", "hoàn toàn ngang bằng với", "1-puggalakatha.md"),
    ("… bhagavantaṃ etadavoca –", "đã nói với Đức Thế Tôn điều này sao –", "1-puggalakatha.md"),
    ("Arahā ācinatīti?", f"Có phải {ARH} tích lũy không?", "2-parihanikatha.md"),
    ("Arahā apacinatīti?", f"Có phải {ARH} giảm trừ không?", "2-parihanikatha.md"),
    ("Arahā sandhūpetīti?", f"Có phải {ARH} nhen nhóm không?", "2-parihanikatha.md"),
    ("neva pajahati na upādiyati pajahitvā ṭhito", PAJ, "2-parihanikatha.md"),
    ("neva visineti na ussineti visinitvā ṭhito", VIS, "2-parihanikatha.md"),
    ("neva vidhūpeti na sandhūpeti vidhūpetvā ṭhito", VID, "2-parihanikatha.md"),
    ("arahantaghātakā", KG, "3-brahmacariyakatha.md"),
    ("Tassuddānaṃ –", TASSUDDANAM, "9-hevatthikatha.md"),
    ("pāṇaṃ haneyya, adinnaṃ ādiyeyya, … nigamaghātaṃ kareyya", "có thể sát hại sinh mạng, " + ", ".join(EVIL),
     "10-dutiyavaggo.md"),
    ("yadaniccaṃ taṃ dukkhaṃ", YAD, "10-dutiyavaggo.md"),
    ("dukkhasamudayo … dukkhanirodhagāminī paṭipadā", f"{DS}’ – đối với", "10-dutiyavaggo.md"),
    ("dukkhanirodhagāminī paṭipadā", PAT, "10-dutiyavaggo.md"),
    ("tesu dinnaṃ mahapphalaṃ", "điều được bố thí cho họ có quả lớn", "10-dutiyavaggo.md"),
    ("mahāva. (citation)", C_MV, "10-dutiyavaggo.md"),
    ("arahato kāye visaṃ kameyya, satthaṃ kameyya, aggi kameyya", POIS, "12-catutthavaggo.md"),
    ("brahmacariyaṃ", "đời sống tu hành trong sạch", "12-catutthavaggo.md"),
    ("gilānapaccayabhesajjaparikkhāraṃ dadantassa", f"người đang cho {GIL}", "13-pancamavaggo.md"),
    ("issariya- / adhipaccasaṃvattaniyaṃ kammaṃ", "nghiệp dẫn đến quyền uy, nghiệp dẫn đến quyền thống trị",
     "15-sattamavaggo.md"),
    ("dāyako dānaṃ deti", f"người bố thí {DANA}", "15-sattamavaggo.md"),
    ("dānaṃ iṭṭhaphalaṃ vuttaṃ bhagavatā", "Đức Thế Tôn đã nói rằng", "15-sattamavaggo.md"),
    ("ito khādanīyaṃ / bhojanīyaṃ / pānīyaṃ denti", f"cho {KHA}, từ đây người ta cho {BHO}, từ đây người ta cho {PAN}",
     "15-sattamavaggo.md"),
    ("Cīvaraṃ … / piṇḍapāto senāsanaṃ gilānapaccayabhesajjaparikkhāro", f"{PIN}, {SEN}, {GIL}",
     "15-sattamavaggo.md"),
    ("Añño aññassa kārako …", KARAKO, "15-sattamavaggo.md"),
    ("Yathā X, evamevaṃ Y", "cũng y như vậy", "15-sattamavaggo.md"),
    ("sati jīvite jīvitāvasese", SATI, "19-ekadasamavaggo.md"),
    ("asati jīvite jīvitāvasese", ASATI, "19-ekadasamavaggo.md"),
    ("nāhaṃ, bhikkhave, sañcetanikānaṃ … upacitānaṃ appaṭisaṃviditvā byantibhāvaṃ vadāmi",
     "Ta không nói rằng có sự chấm dứt của các nghiệp có chủ ý đã làm, đã được tích lũy, khi chúng chưa được cảm nhận",
     "20-dvadasamavaggo.md"),
    ("upapajje vā apare vā pariyāye", "hoặc trong lần tái sinh kế tiếp", "20-dvadasamavaggo.md"),
    ("apare vā pariyāye", "hoặc trong một lượt khác về sau", "20-dvadasamavaggo.md"),
    ("arahantaṃ jīvitā voropeyya", f"{VOR} của {ARH}", "20-dvadasamavaggo.md"),
    ("diṭṭhisampanno", "thành tựu về", "20-dvadasamavaggo.md"),
    ("Xti-kathā", "Bàn về việc ", "20-dvadasamavaggo.md"),
]


def check_strings():
    texts = {b: unicodedata.normalize("NFC", "\n".join(p.read_text(encoding="utf-8")
                                                       for p in sorted(d.glob("*.md")))).lower()
             for b, d in S.RAILS.items()}
    bad = [(p, v, b) for p, v, b in REUSED25 if unicodedata.normalize("NFC", v).lower() not in texts[b]]
    assert not bad, "reused strings not found in their rails: " + repr(bad)
    bad = []
    for p, v, f in SHARED:
        t = unicodedata.normalize("NFC", (S.OUT_DIR / f).read_text(encoding="utf-8"))
        if unicodedata.normalize("NFC", v) not in t:
            bad.append((p, v, f))
    assert not bad, "shared strings not found in their chapters: " + repr(bad)


# ---------------------------------------------------------------------------------------------------------------
# Verses (one Vietnamese line per Pāli line)
# ---------------------------------------------------------------------------------------------------------------
V785 = [
    f"“Thế gian vận hành{VAR_VT} do nghiệp, muôn loài vận hành{VAR_VT} do nghiệp;",
    f"Chúng sinh bị nghiệp ràng buộc, như chốt trục của cỗ xe đang chạy [{C_MN} 2.460; {C_SU} 659].",
    "“Do nghiệp mà được danh tiếng, lời khen ngợi,",
    "Do nghiệp mà bị mất mát, bị giết hại và bị giam cầm;",
    "Sau khi biết nghiệp ấy tạo nên sự khác nhau,",
    "Tại sao lại nói trong thế gian rằng không có nghiệp”.",
]
#   Kammunā vattatī loko, kammunā vattatī pajā; / Kammanibandhanā sattā, rathassāṇīva yāyato.
#   Kammena kittiṃ labhate pasaṃsaṃ, / Kammena jāniñca vadhañca bandhaṃ; / Taṃ kammaṃ nānākaraṇaṃ viditvā, /
#   Kasmā vade natthi kammanti loke"ti.   (Pāli "." kept after the rhetorical question)

V791 = [
    "“Như lửa với lễ vật, như đất với đám mây lớn;",
    f"{SG} thành tựu về định tâm, nhận phần cúng dường”.",
]
#   Āhutiṃ jātavedova, mahāmeghaṃva medanī; / Saṅgho samādhisampanno, paṭiggaṇhāti dakkhiṇa"nti.

YAJ = "“Đối với loài người đang tế lễ, đối với chúng sinh mong cầu phước;"   # Yajamānānaṃ manussānaṃ, … pāṇinaṃ;
KAR = "Đang làm phước còn chấp trước"                                    # Karotaṃ opadhikaṃ puññaṃ
V798 = [
    YAJ,
    f"{KAR}, điều được bố thí ở đâu có quả lớn”.",                        # kattha dinnaṃ mahapphalanti. (close supplied)
    "“Bốn bậc đang thực hành, và bốn bậc đã đứng vững nơi thành quả;",
    "Đó là Tăng đoàn ngay thẳng, an định trong trí tuệ và giới hạnh.",
    YAJ[1:],                                                             # stanza continues the answer (see notes)
    f"{KAR}, {T9}” [{C_SN} 1.262; {C_VV} 642, 751].",
    "“Quả thật, Tăng đoàn này bao la, rộng lớn,",
    "Không thể đo lường như nước của đại dương;",
    f"Quả thật, đây là những đệ tử tối thắng của bậc anh hùng giữa loài người{S.var('Ka.', 'narasīhasāvakā')},",
    "Những người đem lại ánh sáng, họ tuyên thuyết Giáo Pháp.",
    "“Đối với những người ấy, điều đã cho là khéo được bố thí, khéo được dâng, khéo được tế lễ,",
    "Những người thực hiện sự bố thí hướng về Tăng đoàn;",
    "Phần cúng dường ấy đã đến Tăng đoàn, được thiết lập vững chắc,",
    "Có quả lớn, được các bậc hiểu biết thế gian tán thán.",
    "“Nhớ lại sự tế lễ như vậy,",
    f"Những ai tràn đầy niềm hoan hỷ đi lại{S.var('Sī., Ka.', 'viharanti')} trong thế gian;",
    "Sau khi loại bỏ cấu uế của sự keo kiệt cùng với gốc rễ,",
    f"Không bị chê trách, họ đi đến nơi chốn cõi trời” [{C_VV} 645, 754].",
]

V799 = [
    "“Không ở thế gian này, cũng không ở thế gian khác,",
    "Có ai tối thắng hơn hay ngang bằng với Đức Phật;",
    "Ngài là bậc đã đạt đến vị trí đứng đầu giữa những bậc xứng đáng được dâng lễ vật,",
    f"Đối với những người cầu phước, mong tìm quả bao la” [{C_VV} 1047].",
]


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

    heading("5-25-0", 3, VAGGA)

    # ---- (166) 1. Arahato puññūpacayakathā ----------------------------------------------------------------------
    heading("5-25-1-0", 4, f"(166) 1. {S.katha(KATHA[1])}")
    add("5-776", f"{Q(T1)} {YES} {Q(A1)} {NO_PE} {q(A1N)} {YES} {Q(T1N)} {NO_PE}")
    add("5-777",
        f"{Q(T1)} {YES} Có phải {ARH} tạo tác {PUB}, tạo tác {ANE}, "
        + ", ".join(f"làm nghiệp dẫn đến {d}" for d in DEEDS) + f" không? {NO_PE}")
    add("5-778",
        f"{Q(T1)} {YES} Có phải {ARH} tích lũy không? {NO_PE} có phải {ARH} giảm trừ không? {NO_PE} "
        f"có phải {ARH} dứt bỏ{PE} {ARH} bám víu{PE} {ARH} phân tán{PE} {ARH} gom tụ{PE} {ARH} dập tắt{PE} "
        f"{ARH} nhen nhóm không? {NO_PE} {nanu_l(AC)} {YES} {hanci_neg(AC, T1)}",
        f"{NANU(f'{ARH} {PAJ}, {VIS}, {VID}')} {YES} {hanci_neg(f'{ARH} {VID}', T1)}")
    GIVE = f"{ARH} có thể {DANA}"
    add("5-779",
        f"{Q(T1N)} {YES} {Q(GIVE)} {YES} {hanci_neg(GIVE, T1N)}",
        f"{Q(f'{ARH} có thể {GIFT_ARH}')} {YES} {hanci_neg(f'{ARH} có thể {ABHID}', T1N)}",
        S.katha_end(KATHA_END1))

    # ---- (167) 2. Natthi arahato akālamaccūtikathā --------------------------------------------------------------
    heading("5-25-2-0", 4, VAGGA)
    heading("5-25-2-1-0", 5, f"(167) 2. {S.katha(KATHA[2])}")
    add("5-780",
        f"{Q(T2)} {YES} {Q(f'không có {KG}')} {NO_PE} {q(f'có {KG}')} {YES} {Q(T2P)} {NO_PE} {q(T2)} {YES} "
        f"Ai {VOR} của {ARH} thì {VOR} {SATI}, hay {VOR} {ASATI}? {cap(VOR)} {SATI}. "
        f"{hanci_neg(f'{VOR} {SATI}', T2)} {S.neu(f'{VOR} {ASATI}', f'không có {KG}')} {NO_PE}")
    add("5-781",
        f"{Q(T2)} {YES} {Q(NPOIS)} {NO_PE} {nanu_l(POIS)} {YES} {hanci_neg(POIS, T2)}",
        f"{Q(NPOIS)} {YES} {Q(f'không có {KG}')} {NO_PE}")
    add("5-782",
        f"{Q(T2P)} {YES} {S.NANU_VUTTAM} {SUT_K} {S.ATTHEVA} {YES} {S.tena_hi(T2)}",
        S.katha_end(KATHA[2]))

    # ---- (168) 3. Sabbamidaṃ kammatotikathā ---------------------------------------------------------------------
    heading("5-25-3-0", 4, VAGGA)
    heading("5-25-3-1-0", 5, f"(168) 3. {S.katha(KATHA[3])}")
    add("5-783",
        f"{Q(T3)} {YES} {Q('nghiệp cũng do nghiệp')} {NO_PE} {q(T3)} {YES} "
        f"{Q('tất cả điều này đều do nguyên nhân là những gì đã làm trước đây')} {NO_PE} {q(T3)} {YES} "
        f"{Q(T3V)} {NO_PE}")
    PAT_K = "việc sát hại sinh mạng"                                     # pāṇātipāto (termbase)
    KVP = "quả của nghiệp"                                               # kammavipāko (termbase)
    add("5-784",
        f"{Q(T3V)} {YES} Có phải {KV} mà có thể sát hại sinh mạng không? {YES} {Q(f'{PAT_K} có kết quả')} {YES} "
        f"{Q(f'{KVP} có kết quả')} {NO_PE} {q(f'{KVP} không có kết quả')} {YES} "
        f"{Q(f'{PAT_K} không có kết quả')} {NO_PE}",
        f"Có phải {KV} mà có thể {(PE + ' ').join(EVIL)}{PE} {KV} mà có thể {DANA}{PE} cho {CIV}{PE} cho {PIN}{PE} "
        f"cho {SEN}{PE} cho {GIL} không? {YES} {Q(f'{GIL} có kết quả')} {YES} {Q(f'{KVP} có kết quả')} {NO_PE} "
        f"{q(f'{KVP} không có kết quả')} {YES} {Q(f'{GIL} không có kết quả')} {NO_PE}")
    add("5-785",
        f"{na_vattabbam(T3)} {YES} {S.NANU_VUTTAM}",
        *V785,
        f"{S.ATTHEVA} {YES} Vậy thì “{T3}”.",
        S.katha_end(KATHA[3]))

    # ---- (169) 4. Indriyabaddhakathā ----------------------------------------------------------------------------
    heading("5-25-4-0", 4, VAGGA)
    heading("5-25-4-1-0", 5, f"(169) 4. {S.katha(KATHA[4])}")
    AIB_A = f"{AIB} là {S.ANICCA}"
    add("5-786",
        f"{Q(T4)} {YES} {Q(f'chỉ {IB} mới là {S.ANICCA}')} {NO_PE} {nanu_l(AIB_A)} {YES} {hanci_neg(AIB_A, T4)}",
        f"{Q(f'{AIB} là {AN1}, và điều ấy không phải là khổ đau')} {YES} "
        f"{Q(f'{IB} là {AN2}, và điều ấy không phải là khổ đau')} {NO_PE}",
        f"Có phải {IB} là {AN2}, và điều ấy là khổ đau{NOTE4} không? {YES} "
        f"Có phải {AIB} là {AN2}, và điều ấy là khổ đau{NOTE4} không? {NO_PE}")
    add("5-787",
        f"{Q(T4)} {YES} Chẳng phải {YAD}{C315}, Đức Thế Tôn đã nói – “{AIB} là vô thường” sao? {YES} "
        f"{hanci_neg(f'{YAD}{C315}, Đức Thế Tôn đã nói – {AIB} là vô thường', T4)}")
    add("5-788",
        f"{na_vattabbam(T4)} {YES} Có phải cũng như {BRV} để hiểu biết trọn vẹn {IBD}, cũng y như vậy, {BRV} để "
        f"hiểu biết trọn vẹn {AIBD} không? {NO_PE} có phải cũng như {IBD}, khi đã được hiểu biết trọn vẹn, không "
        f"sinh khởi lại, cũng y như vậy, {AIBD}, khi đã được hiểu biết trọn vẹn, không sinh khởi lại không? {NO} "
        f"{S.tena_hi(T4)}",
        S.katha_end(KATHA[4]))

    # ---- (170) 5. Ṭhapetvā ariyamaggantikathā -------------------------------------------------------------------
    heading("5-25-5-0", 4, VAGGA)
    heading("5-25-5-1-0", 5, f"(170) 5. {S.katha(KATHA[5])}")
    DSD = f"{DS} cũng là khổ đau"
    add("5-789",
        f"{Q(T5)} {YES} {Q(DSD)} {NO_PE} {q(DSD)} {YES} {Q(TINE)} {NO_PE} {q(TINE)} {YES} {NANU(CA4)} {YES} "
        f"{hanci_neg(CA4, TINE, sep=';')}",
        f"{Q(DSD)} {YES} Theo nghĩa nào? Theo nghĩa vô thường. {Q(f'{MG} là vô thường')} {YES} "
        f"{Q(f'{MG} là khổ đau')} {NO_PE}",
        f"{Q(f'{MG} là vô thường, và nó không phải là khổ đau')} {YES} "
        f"{Q(f'{DS} là vô thường, và nó không phải là khổ đau')} {NO_PE} "
        f"{q(f'{DS} là vô thường, và nó là khổ đau')} {YES} {Q(f'{MG} là vô thường, và nó là khổ đau')} {NO_PE}")
    SA = f"đó là {PAT}"
    add("5-790",
        f"{na_vattabbam(T5)} {YES} {NANU(SA)} {YES} {hanci(SA, T5)}",
        S.katha_end(KATHA[5]))

    # ---- (171) 6. … paṭiggaṇhāti; (172) 7. … visodheti ----------------------------------------------------------
    def worthy(t, pe):
        return [f"{na_vattabbam(t)} {YES} {NANU(f'{SG} {WORTHY}')} {YES} "
                f"{hanci(f'{SG} {WORTHY_PE if pe else WORTHY}', t)}",
                f"{na_vattabbam(t)} {YES} {NANU(P8)} {YES} {hanci(P8, t)}"]

    heading("5-25-6-0", 4, VAGGA)
    heading("5-25-6-1-0", 5, f"(171) 6. {S.katha(KATHA[6])}")
    D6 = f"có những người {DANA} cho {SG}"
    G6 = (f"có những người cho {SG} {CIV}{PE} cho {PIN}{PE} cho {SEN}{PE} cho {GIL}{PE} cho {KHA}{PE} cho {BHO}{PE} "
          f"cho {PAN}")
    add("5-791",
        *worthy(T6, False),
        f"{na_vattabbam(T6)} {YES} {NANU(D6)} {YES} {hanci(D6, T6)} {NANU(G6)} {YES} "
        f"{hanci(f'có những người cho {SG} {PAN}', T6)}",
        f"{na_vattabbam(T6)} {YES} {S.NANU_VUTTAM}",
        *V791,
        f"{S.ATTHEVA} {YES} {S.tena_hi(T6)}")
    add("5-792",
        f"{Q(T6)} {YES} {Q('con đường nhận, thành quả nhận')} {NO_PE}",
        S.katha_end(KATHA[6]))

    heading("5-25-7-0", 4, VAGGA)
    heading("5-25-7-1-0", 5, f"(172) 7. {S.katha(KATHA[7])}")
    D7 = f"có những người, sau khi {DANA} cho {SG}, {AR}"
    G7 = (f"có những người, sau khi cho {SG} {CIV}{PE} sau khi cho {PIN}{PE} sau khi cho {SEN}{PE} sau khi cho {GIL}"
          f"{PE} sau khi cho {KHA}{PE} sau khi cho {BHO}{PE} sau khi cho {PAN}, {AR}")
    add("5-793",
        *worthy(T7, True),
        f"{na_vattabbam(T7)} {YES} {NANU(D7)} {YES} {hanci(D7, T7)}",
        f"{NANU(G7)} {YES} {hanci(f'có những người, sau khi cho {SG} {PAN}, {AR}', T7)}")
    add("5-794",
        f"{Q(T7)} {YES} {Q('con đường làm thanh tịnh, thành quả làm thanh tịnh')} {NO_PE}",
        S.katha_end(KATHA[7]))

    # ---- (173) 8. Na vattabbaṃ saṅgho bhuñjatītikathā -----------------------------------------------------------
    heading("5-25-8-0", 4, VAGGA)
    heading("5-25-8-1-0", 5, f"(173) 8. {S.katha(KATHA[8])}")
    B8 = (f"có những người tổ chức bữa ăn cho {SG}, tổ chức bữa ăn cho các vị được chỉ định, "
          "tổ chức các buổi uống cháo")
    #   saṅghabhattāni karonti, uddesabhattāni karonti, yāgupānāni karonti
    add("5-795",
        f"{na_vattabbam(T8)} {YES} {NANU(B8)} {YES} {hanci(B8, T8)}",
        f"{na_vattabbam(T8)} {YES} {S.NANU_VUTTAM} “{BJ}”? {YES} {hanci(f'Đức Thế Tôn đã nói – «{BJ}»', T8)}",
        f"{na_vattabbam(T8)} {YES} {NANU(f'Đức Thế Tôn đã nói về tám loại thức uống – {DRV}')} {YES} "
        f"{hanci(f'Đức Thế Tôn đã nói về tám loại thức uống – {DR}', T8)}")
    add("5-796",
        f"{Q(T8)} {YES} {Q('con đường ăn, uống, nhai, nếm, thành quả ăn, uống, nhai, nếm')} {NO_PE}",
        S.katha_end(KATHA[8]))

    # ---- (174) 9. Na vattabbaṃ saṅghassadinnaṃ mahapphalantikathā -----------------------------------------------
    heading("5-25-9-0", 4, VAGGA)
    heading("5-25-9-1-0", 5, f"(174) 9. {S.katha(KATHA[9])}")
    add("5-797", *worthy(T9, True))
    SUT_G = (f"“Này Kiều-đàm-di, hãy bố thí cho {SG}, khi bà bố thí cho {SG}, thì chính Ta cũng sẽ được tôn kính, "
             f"và cả {SG}” [{C_MN} 3.376].")
    #   saṅghe, gotami, dehi, saṅghe te dinne ahañceva pūjito bhavissāmi saṅgho cā"ti [ma. ni. 3.376]
    add("5-798",
        f"{na_vattabbam(T9)} {YES} {S.NANU_VUTTAM} {SUT_G} {S.ATTHEVA} {YES} {S.tena_hi(T9)}",
        f"{na_vattabbam(T9)} {YES} Chẳng phải Sakka, vua của chư thiên, đã nói với Đức Thế Tôn điều này sao –",
        *V798,
        f"{S.ATTHEVA} {YES} {S.tena_hi(T9)}",
        S.katha_end(KATHA[9]))

    # ---- (175) 10. Na vattabbaṃ buddhassadinnaṃ mahapphalantikathā ----------------------------------------------
    heading("5-25-10-0", 4, VAGGA)
    heading("5-25-10-1-0", 5, f"(175) 10. {S.katha(KATHA[10])}")
    add("5-799",
        f"{na_vattabbam(T10)} {YES} {NANU(f'Đức Thế Tôn là {EP}')} {YES} {hanci(f'Đức Thế Tôn là {EP}', T10)}",
        f"{na_vattabbam(T10)} {YES} Có phải có {SAMA.replace('ai ', 'ai đó ', 1)} không? Không có. {hanci(f'không có {SAMA}', T10)}",
        f"{na_vattabbam(T10)} {YES} {S.NANU_VUTTAM}",
        *V799,
        f"{S.ATTHEVA} {YES} {S.tena_hi(T10)}",
        S.katha_end(KATHA[10]))

    # ---- (176) 11. Dakkhiṇāvisuddhikathā ------------------------------------------------------------------------
    heading("5-25-11-0", 4, VAGGA)
    heading("5-25-11-1-0", 5, f"(176) 11. {S.katha(KATHA[11])}")
    W11 = f"có những người nhận {WORTHY}"
    SOT = f"có những người, sau khi {DANA} cho {S.PN['sotāpanno']}, {AR}"
    ALL4 = (f"có những người, sau khi {DANA} cho {S.PN['sakadāgāmī']}{PE} cho {S.PN['anāgāmī']}{PE} cho {ARH}, "
            f"{AR}")
    add("5-800",
        f"{Q(T11)} {YES} {NANU(W11)} {YES} {hanci_neg(W11, T11)}",
        f"{Q(T11)} {YES} {NANU(P8)} {YES} {hanci_neg(P8, T11)}",
        f"{Q(T11)} {YES} {NANU(SOT)} {YES} {hanci_neg(SOT, T11)}",
        f"{NANU(ALL4)} {YES} {hanci_neg(f'có những người, sau khi {DANA} cho {ARH}, {AR}', T11)}")
    add("5-801",
        f"{Q('sự bố thí được thanh tịnh từ phía người nhận')} {YES} {Q(KARAKO)} {NO_PE}",
        f"{Q(T11)} {YES} {S.NANU_VUTTAM} {SUT_A} {S.ATTHEVA} {YES} {S.tena_hi_na(T11)}",
        S.katha_end(KATHA[11]),
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
    adh = S.FORMULAS_MD.parent / "adh-25"           # byte-identical copy for termbase_adherence_vi.py
    adh.mkdir(exist_ok=True)
    (adh / NAME).write_text(text, encoding="utf-8", newline="\n")
    print("wrote", adh / NAME)


if __name__ == "__main__":
    main()
