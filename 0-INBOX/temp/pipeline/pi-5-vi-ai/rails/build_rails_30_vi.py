"""pi-5 Kathāvatthu, Vietnamese RAILS (plain audience): chapter 30, Bāvīsatimavaggo (^5-30-0 … ^5-907): ten
kathās (208-217) with the repeated "Bāvīsatimavaggo" sub-headings, the vagga close and the uddāna.

Builds AI_translation/vietnamese/pi-5-vietnamese-plain-rails_split_chapters/30-bavisatimavaggo.md from the fixed
strings below, importing the approved sample builder READ-ONLY (frames Q, q, NANU, hanci, hanci_neg, na_vattabbam,
tena_hi, tena_hi_na, katha, katha_end, var …). Strings taken from pi-1 … pi-4 rails are asserted there
(REUSED30); strings shared with the finished pi-5 rails chapters 1-25 are asserted in those chapter files (SHARED).
The per-line dash / quote / NFC / id checks of S.check_against_pali run before writing.
New recurring strings: notes-rails-30.md.

usage: python -I -X utf8 -B build_rails_30_vi.py          (writes the chapter and the adherence copy rails\\adh-30\\)
"""
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai\rails")
import build_rails_sample_vi as S  # noqa: E402

NAME = "30-bavisatimavaggo.md"
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
BH_L = "này các tỳ-khưu"                                                # bhikkhave inside a running quote
AV = "Này các hiền giả"                                                 # āvuso (ch10)
AV_L = "này các hiền giả"
ARH = S.PN["arahā"]                                                     # bậc A-la-hán (pi-4)
VAGGA = "Chương thứ hai mươi hai"                                       # Bāvīsatimavaggo (termbase)
TASSUDDANAM = "Tóm tắt của chương này –"                               # Tassuddānaṃ – (ch9)
C_AN, C_MN = CIT["a. ni."], CIT["ma. ni."]
C_DN = "Trường Bộ Kinh"                                                 # dī. ni. (ch8, ch10)
SARI = "Chẳng phải tôn giả Xá-lợi-phất đã nói thế này sao –"            # Nanu āyasmā sāriputto etadavoca – (ch11)

# Kathā 1
T1 = "có sự nhập Niết-bàn trọn vẹn mà chưa dứt bỏ một xiềng xích nào đó"   # atthi kiñci saṃyojanaṃ appahāya parinibbānaṃ
T1B = (f"có sự nhập Niết-bàn trọn vẹn mà chưa dứt bỏ một quan điểm về tự ngã nào đó{PE} "
       "mà chưa dứt bỏ sự không biết ghê sợ tội lỗi")                   # atthi kiñci sakkāyadiṭṭhiṃ appahāya…pe… anottappaṃ appahāya parinibbānaṃ
SARAGO = f"{ARH} có tham đắm{PE} có phiền não"                          # arahā sarāgo…pe… sakileso
NIRAGO = f"{ARH} không có tham đắm{PE} không còn phiền não"             # arahā nirāgo…pe… nikkileso (termbase; ch19)
BV = f"{ARH} biết tất cả phạm vi của Đức Phật"                          # arahā sabbaṃ buddhavisayaṃ jānāti

# Kathā 2
T2 = f"{ARH} nhập Niết-bàn trọn vẹn với tâm thiện"                      # arahā kusalacitto parinibbāyati
PUB = "sự tạo tác thuộc về phước"                                       # puññābhisaṅkhāro (pi-2; ch25)
ANE = "sự tạo tác dẫn đến trạng thái bất động"                          # āneñjābhisaṅkhāro (pi-2; ch25)
DEEDS = ["cõi tái sinh", "sự hiện hữu", "quyền uy", "quyền thống trị", "tài sản lớn", "đoàn tùy tùng lớn",
         "sự vinh hiển giữa chư thiên", "sự vinh hiển giữa loài người"]   # (ch25)
AC = f"{ARH} không tích lũy cũng không giảm trừ, đứng vững sau khi đã giảm trừ"   # (ch2 / ch25)
PAJ = "không dứt bỏ cũng không bám víu, đứng vững sau khi đã dứt bỏ"          # (ch2)
VIS = "không phân tán cũng không gom tụ, đứng vững sau khi đã phân tán"         # (ch2)
VID = "không dập tắt cũng không nhen nhóm, đứng vững sau khi đã dập tắt"        # (ch2)
UPS = f"{ARH}, có sự tỉnh thức được thiết lập, tỉnh thức và hiểu biết rõ ràng, nhập Niết-bàn trọn vẹn"
#   arahā upaṭṭhitassati sato sampajāno parinibbāyati (upaṭṭhitassati pi-4; sato sampajāno pi-2)

# Kathā 3
STAND = f"{ARH} nhập Niết-bàn trọn vẹn khi đang đứng vững trong"        # arahā … ṭhito parinibbāyati (termbase)
T3 = f"{STAND} trạng thái bất động"                                     # āneñje
PAK = f"{STAND} tâm bình thường"                                        # pakaticitte
KIR = f"{STAND} tâm mang tính chức năng"                                # kiriyamaye citte
VIP = f"{STAND} tâm thuộc quả của nghiệp"                               # vipākacitte (sibling of vipākābyākate)
KIRA = f"{STAND} tâm không xác định về mặt đạo đức mang tính chức năng"  # kiriyābyākate citte (pi-1; ch19)
VIPA = f"{STAND} tâm không xác định về mặt đạo đức thuộc quả của nghiệp"  # vipākābyākate citte (ch20)
CJ = "Đức Thế Tôn, sau khi xuất khỏi tầng thiền thứ tư, liền sau đó đã nhập Niết-bàn trọn vẹn"
#   bhagavā catutthajjhānā vuṭṭhahitvā samanantarā parinibbuto (tầng thiền thứ tư pi-1)

# Kathās 4-5
GB = "khi đang nằm trong bào thai"                                      # gabbhaseyyāya (termbase)
SP = "người đang nằm mơ"                                                # supinagatassa (termbase)
DA = "sự thấu hiểu Giáo Pháp"                                           # dhammābhisamayo (pi-4; ch4)
AP = "sự đạt đến trạng thái A-la-hán"                                   # arahattappatti (termbase)
T4 = f"{GB} có {DA}"
SLEEP = "người đang ngủ, buông thả, mất tỉnh thức, không hiểu biết rõ ràng"
#   suttassa pamattassa muṭṭhassatissa asampajānassa (muṭṭhassati asampajāno ch11)
CAUSES = ["việc thuyết giảng Giáo Pháp", "việc nghe Giáo Pháp", "việc đàm luận Giáo Pháp", "việc hỏi han",
          "việc thọ trì giới hạnh", "sự phòng hộ cửa các giác quan", "sự biết tiết độ trong ăn uống",
          "sự chuyên tâm thực hành việc thức canh vào đầu đêm và cuối đêm"]
#   dhammadesanā (ch11), dhammassavanaṃ, dhammasākacchā, paripucchā, sīlasamādānaṃ, indriyesu guttadvāratā (pi-1),
#   bhojane mattaññutā (pi-1), pubbarattāpararattaṃ jāgariyānuyogo (pi-2)
TWO = ("có hai điều kiện cho sự sinh khởi của quan điểm đúng đắn – tiếng nói từ người khác, "
       "và sự chú tâm đúng cách")                                       # dve paccayā sammādiṭṭhiyā uppādāya – …

# Kathā 6
T6 = f"tất cả tâm của {SP} đều không xác định về mặt đạo đức"           # sabbaṃ supinagatassa cittaṃ abyākataṃ
DR = "trong giấc mơ có thể"                                             # supinantena … -eyya
EVIL = ("lấy của không được cho", "nói dối", "nói lời chia rẽ", "nói lời thô ác", "nói lời phù phiếm", "đột nhập nhà",
        "cướp bóc", "cướp một ngôi nhà", "mai phục bên đường", "đi lại với vợ người khác", "cướp phá làng",
        "cướp phá thị trấn")                                            # (ch10 / ch25)
CIV, PIN, SEN, GIL = "y phục", "đồ ăn khất thực", "chỗ ở", "thuốc men và vật dụng chữa bệnh"
KHA, BHO, PAN = "món ăn cứng", "món ăn mềm", "nước uống"
CET = "bảo tháp"
ABHID = f"đi nhiễu quanh {CET} theo chiều bên phải"                      # (ch21 / ch25)
METH = "hưởng thụ hành vi dâm dục"                                      # methunaṃ dhammaṃ paṭiseveyya (ch10)
ASUCI = f"chất bất tịnh của {SP} có thể thoát ra"                       # supinagatassa asuci mucceyya
ABBO = f"Đức Thế Tôn đã nói rằng tâm của {SP} là không được tính đến"   # supinagatassa cittaṃ abbohāriyaṃ vuttaṃ bhagavatā

# Kathā 7
APT = "tính chất làm điều kiện thực hành"                               # āsevanapaccayatā (termbase)
T7 = f"không có bất cứ {APT} nào"                                       # natthi kāci āsevanapaccayatā
T7P = f"có {APT} nào đó"                                                # atthi kāci āsevanapaccayatā
ASB = "khi được thực hành, được tu tập, được làm đi làm lại"            # āsevito bhāvito bahulīkato (pi-2)
HELL = "dẫn đến địa ngục, dẫn đến cõi súc sinh, dẫn đến cõi ngạ quỷ"     # niraya-, tiracchānayoni-, pettivisaya-
AMATA = ("thâm nhập vào điều bất tử, lấy điều bất tử làm nơi đến cuối cùng, "
         "lấy điều bất tử làm điểm kết thúc")                           # amatogadhā hoti amataparāyanā amatapariyosānā
PAT_K = "việc sát hại sinh mạng"                                        # pāṇātipāto (termbase)
ADIN = "việc lấy của không được cho"                                    # adinnādānaṃ (pi-2)
KAMA = "hành vi sai trái trong các dục lạc"                             # kāmesumicchācāro (pi-2)
MUSA = "việc nói dối"                                                   # musāvādo (pi-2)
PIS = "lời nói chia rẽ"                                                 # pisuṇā vācā (pi-2)
PHA = "lời nói thô ác"                                                  # pharusā vācā (pi-2)
SAM = "việc nói lời phù phiếm"                                          # samphappalāpo (pi-2)
SURA = "việc uống rượu nấu và rượu men"                                 # surāmerayapānaṃ


def lv(x, y):                       # yo sabbalahuso X-assa vipāko manussabhūtassa Y-saṃvattaniko hoti
    return f"quả nhẹ nhất của {x}, đối với người sinh làm người, dẫn đến {y}"


# Kathā 8
T8 = "tất cả các hiện tượng đều kéo dài trong khoảnh khắc của một tâm"  # ekacittakkhaṇikā sabbe dhammā (ch19)
NATURE = ["đại địa", "đại dương", "núi Tu-di, vua của các ngọn núi", "nước", "lửa", "gió"]   # (sample)
TINA = "cỏ, gỗ và cây rừng"                                             # (sample)
NICCA = "thường còn, bền vững, trường tồn, không có bản chất biến đổi"   # niccā dhuvā sassatā avipariṇāmadhammā (sample)
SAHA_C = "lĩnh vực mắt cùng sinh với thức qua mắt"                      # cakkhāyatanaṃ cakkhuviññāṇena sahajātaṃ
SAHA_K = "lĩnh vực thân cùng sinh với thức qua thân"                    # kāyāyatanaṃ kāyaviññāṇena sahajātaṃ
VIBH = "phần thức tương ứng"                                            # tajjassa viññāṇabhāgassa
NOT_YET = f"thì chưa có sự xuất hiện của {VIBH}"                         # neva tāva tajjassa viññāṇabhāgassa pātubhāvo hoti
THEN = f"thì như vậy có sự xuất hiện của {VIBH}"                         # evaṃ tajjassa viññāṇabhāgassa pātubhāvo hoti


def eye(av, inner, outer, come, att=None):
    """[yato ca kho,] āvuso, ajjhattika… aparibhinna hoti, bāhirā ca … (na) āpāthaṃ āgacchanti[, no ca / ca tajjo
    samannāhāro hoti]; att None = the clause is cut by …pe… after "no ca" (rendered «, và không»)."""
    head = (f"{av}, {'khi nào' if att is True else 'nếu'} {inner} thuộc phần bên trong không bị hư hoại, "
            f"các {outer} thuộc phần bên ngoài {'đi vào tầm' if come else 'không đi vào tầm'}")
    if att is None:
        return head + ", và không"
    return head + f", và {'có' if att else 'không có'} sự lưu ý tương ứng"


KATHA = {1: "sự nhập Niết-bàn trọn vẹn", 2: "tâm thiện", 3: "trạng thái bất động", 4: DA,
         6: "điều không xác định về mặt đạo đức", 7: "điều kiện thực hành", 8: "việc kéo dài trong khoảnh khắc"}
TISSOPI = "Cả ba phần bàn"                                              # Tissopi(…)kathā (ch19)
UDDANA = (f"{cap(T1)}, {T2}, {T3}, {T4}, {GB} có {AP}, {SP} có {DA}, {SP} có {AP}, {T6}, {T7}, {T8}.")

REUSED30 = [  # (Pāli, Vietnamese, book)
    ("puññābhisaṅkhāro", PUB, "2"),
    ("āneñjābhisaṅkhāro", ANE, "2"),
    ("arahā", ARH, "4"),
    ("upaṭṭhitassati", "có sự tỉnh thức được thiết lập", "4"),
    ("sato sampajāno", "tỉnh thức và hiểu biết rõ ràng", "2"),
    ("catutthajjhāna", "tầng thiền thứ tư", "1"),
    ("kiriyābyākata", "không xác định về mặt đạo đức mang tính chức năng", "1"),
    ("dhammābhisamayo", DA, "4"),
    ("paripucchato", "hỏi han", "4"),
    ("indriyesu guttadvāratā", "sự phòng hộ cửa các giác quan", "1"),
    ("bhojane mattaññutā", "sự biết tiết độ trong ăn uống", "1"),
    ("pubbarattāpararattaṃ jāgariyānuyoga-", "chuyên tâm thực hành việc thức canh vào đầu đêm và cuối đêm", "2"),
    ("sīlaṃ samādiyitvā", "thọ trì giới hạnh", "2"),
    ("yoniso manasikaroto", "chú tâm đúng cách", "4"),
    ("āsevitāni bhāvitāni bahulīkatāni", "được thực hành, được tu tập, được làm đi làm lại", "2"),
    ("pāṇātipātā / adinnādānā / kāmesumicchācārā veramaṇī",
     f"sự kiềm chế {PAT_K}, sự kiềm chế {ADIN}, sự kiềm chế {KAMA}", "2"),
    ("musāvādo, pisuṇā vācā, pharusā vācā, samphappalāpo", f"{MUSA}, {PIS}, {PHA}, {SAM}", "2"),
    ("bhogabyasanaṃ", "sự tổn hại về tài sản", "2"),
    ("ajjhattika / bāhira", "thuộc phần bên trong", "2"),
    ("bāhirārammaṇā", "thuộc phần bên ngoài", "2"),
]

SHARED = [  # (Pāli, Vietnamese, finished pi-5 rails chapter)
    ("niccā dhuvā sassatā avipariṇāmadhammā", NICCA, "1-puggalakatha.md"),
    ("sabbe dhammā anattā", "tất cả các hiện tượng đều", "1-puggalakatha.md"),
    ("cakkhussa āpāthaṃ āgacchati", "đi vào tầm", "1-puggalakatha.md"),
    ("mahāpathavī … tiṇakaṭṭhavanappatayo", f"{NATURE[2]} được tìm thấy… {NATURE[3]}", "1-puggalakatha.md"),
    ("Arahā ācinatīti?", f"Có phải {ARH} tích lũy không?", "2-parihanikatha.md"),
    ("nevācinati na apacinati apacinitvā ṭhito", AC, "2-parihanikatha.md"),
    ("neva pajahati na upādiyati pajahitvā ṭhito", PAJ, "2-parihanikatha.md"),
    ("neva visineti na ussineti visinitvā ṭhito", VIS, "2-parihanikatha.md"),
    ("Sakkāyadiṭṭhi", "quan điểm về tự ngã", "2-parihanikatha.md"),
    ("sarāgo", f"{ARH} có tham đắm", "5-sabbamatthitikatha.md"),
    ("anottappaṃ", "sự không biết ghê sợ tội lỗi", "5-sabbamatthitikatha.md"),
    ("satipaṭṭhānā [dī. ni. …]", C_DN, "8-satipatthanakatha.md"),
    ("Tassuddānaṃ –", TASSUDDANAM, "9-hevatthikatha.md"),
    ("pāṇaṃ haneyya, adinnaṃ ādiyeyya, … nigamaghātaṃ kareyya", "có thể sát hại sinh mạng, " + ", ".join(EVIL),
     "10-dutiyavaggo.md"),
    ("methunaṃ dhammaṃ paṭiseveyya", f"có thể {METH}", "10-dutiyavaggo.md"),
    ("āvuso", AV, "10-dutiyavaggo.md"),
    ("dhammadesanā", "việc thuyết giảng Giáo Pháp", "11-tatiyavaggo.md"),
    ("muṭṭhassati asampajāno", "mất tỉnh thức, không hiểu biết rõ ràng", "11-tatiyavaggo.md"),
    ("Nanu āyasmā sāriputto etadavoca –", SARI, "11-tatiyavaggo.md"),
    ("tiracchānayoni, pettivisayo", "cõi súc sinh, cõi ngạ quỷ", "16-atthamavaggo.md"),
    ("dānaṃ iṭṭhaphalaṃ vuttaṃ bhagavatā", "Đức Thế Tôn đã nói rằng", "15-sattamavaggo.md"),
    ("Tissopi anusayakathā", TISSOPI, "19-ekadasamavaggo.md"),
    ("Ekacittakkhaṇiko samādhī", "kéo dài trong khoảnh khắc của một tâm", "19-ekadasamavaggo.md"),
    ("nikkileso", "không còn phiền não", "19-ekadasamavaggo.md"),
    ("kiriyābyākatā", "không xác định về mặt đạo đức mang tính chức năng", "20-dvadasamavaggo.md"),
    ("vipākābyākatā", "không xác định về mặt đạo đức thuộc quả của nghiệp", "20-dvadasamavaggo.md"),
    ("dānaṃ dadeyya", "có thể thực hiện sự bố thí", "21-terasamavaggo.md"),
    ("cīvaraṃ dadeyya … cetiyaṃ abhidakkhiṇaṃ kareyya",
     f"cho {CIV}{PE} cho {PIN}{PE} cho {SEN}{PE} cho {GIL}", "25-sattarasamavaggo.md"),
    ("cetiyaṃ vandeyya… cetiye mālaṃ… gandhaṃ… vilepanaṃ āropeyya…pe… abhidakkhiṇaṃ",
     f"đảnh lễ {CET}{PE} dâng vòng hoa lên {CET}{PE} dâng hương thơm{PE} dâng dầu thoa{PE} {ABHID}",
     "25-sattarasamavaggo.md"),
    ("khādanīyaṃ … bhojanīyaṃ … pānīyaṃ", f"cho {KHA}{PE} cho {BHO}{PE} cho {PAN}", "25-sattarasamavaggo.md"),
    ("puññābhisaṅkhāraṃ abhisaṅkharoti, āneñjābhisaṅkhāraṃ …",
     f"tạo tác {PUB}, tạo tác {ANE}, làm nghiệp dẫn đến {DEEDS[0]}, làm nghiệp dẫn đến {DEEDS[1]}",
     "25-sattarasamavaggo.md"),
    ("mahābhoga- … manussasobhagyasaṃvattaniyaṃ kammaṃ",
     ", ".join(f"làm nghiệp dẫn đến {d}" for d in DEEDS[4:]), "25-sattarasamavaggo.md"),
    ("neva vidhūpeti na sandhūpeti vidhūpetvā ṭhito", f"{PAJ}, {VIS}, {VID}", "25-sattarasamavaggo.md"),
    ("Abyākatakathā", S.katha(KATHA[6]), "22-cuddasamavaggo.md"),
    ("āsevanapaccayena", "điều kiện thực hành", "23-pannarasamavaggo.md"),
]


def check_strings():
    texts = {b: unicodedata.normalize("NFC", "\n".join(p.read_text(encoding="utf-8")
                                                       for p in sorted(d.glob("*.md")))).lower()
             for b, d in S.RAILS.items()}
    bad = [(p, v, b) for p, v, b in REUSED30 if unicodedata.normalize("NFC", v).lower() not in texts[b]]
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

    heading("5-30-0", 3, VAGGA)

    # ---- (208) 1. Parinibbānakathā ------------------------------------------------------------------------------
    heading("5-30-1-0", 4, f"(208) 1. {S.katha(KATHA[1])}")
    add("5-892",
        f"{Q(T1)} {YES} {Q(T1B)} {NO_PE}",
        f"{Q(T1)} {YES} {Q(SARAGO)} {NO_PE} {nanu_l(NIRAGO)} {YES} {hanci_neg(NIRAGO, T1)}")
    add("5-893",
        f"{na_vattabbam(T1)} {YES} {Q(BV)} {NO} {S.tena_hi(T1)}",
        S.katha_end(KATHA[1]))

    # ---- (209) 2. Kusalacittakathā ------------------------------------------------------------------------------
    heading("5-30-2-0", 4, VAGGA)
    heading("5-30-2-1-0", 5, f"(209) 2. {S.katha(KATHA[2])}")
    acts = [f"trong khi tạo tác {PUB}", f"trong khi tạo tác {ANE}"] + [
        f"trong khi làm nghiệp dẫn đến {d}" for d in DEEDS]
    AC_ALL = "trong khi tích lũy, giảm trừ, dứt bỏ, bám víu, phân tán, gom tụ, dập tắt, nhen nhóm"
    #   ācinanto apacinanto pajahanto upādiyanto visinento ussinento vidhūpento sandhūpento (termbase)
    add("5-894",
        f"{Q(T2)} {YES} Có phải {ARH}, {(PE + ' ').join(acts)}, nhập Niết-bàn trọn vẹn không? {NO_PE}",
        f"{Q(T2)} {YES} Có phải {ARH}, {AC_ALL}, nhập Niết-bàn trọn vẹn không? {NO_PE} {nanu_l(AC)} {YES} "
        f"{hanci_neg(AC, T2)} Chẳng phải {ARH} {PAJ}, {VIS}; chẳng phải {ARH} {VID} sao? {YES} "
        f"{hanci_neg(f'{ARH} {VID}', T2)}")
    add("5-895",
        f"{na_vattabbam(T2)} {YES} {NANU(UPS)} {YES} {hanci(UPS, T2)}",
        S.katha_end(KATHA[2]))

    # ---- (210) 3. Āneñjakathā -----------------------------------------------------------------------------------
    heading("5-30-3-0", 4, VAGGA)
    heading("5-30-3-1-0", 5, f"(210) 3. {S.katha(KATHA[3])}")
    add("5-896",
        f"{Q(T3)} {YES} {NANU(PAK)} {YES} {hanci_neg(PAK, T3)}",
        f"{Q(T3)} {YES} {Q(KIR)} {NO_PE} {nanu_l(VIP)} {YES} {hanci_neg(VIP, T3)}",
        f"{Q(T3)} {YES} {Q(KIRA)} {NO_PE} {nanu_l(VIPA)} {YES} {hanci_neg(VIPA, T3)}",
        f"{Q(T3)} {YES} {NANU(f'{CJ} [{C_DN} 2.219]')} {YES} {hanci_neg(CJ, T3)}",
        S.katha_end(KATHA[3]))

    # ---- (211) 4. Dhammābhisamayakathā --------------------------------------------------------------------------
    heading("5-30-4-0", 4, VAGGA)
    heading("5-30-4-1-0", 5, f"(211) 4. {S.katha(KATHA[4])}")
    NO_C = f"{GB} không có {CAUSES[0]}, {CAUSES[1]}{PE} {CAUSES[-1]}"
    add("5-897",
        f"{Q(T4)} {YES} {Q(f'{GB} có ' + ', '.join(CAUSES))} {NO_PE} {q(NO_C)} {YES} {hanci_neg(NO_C, T4)}",
        f"{Q(T4)} {YES} {NANU(TWO)} {YES} {hanci_neg(TWO, T4)}",
        f"{Q(T4)} {YES} {Q(f'{SLEEP} có {DA}')} {NO_PE}",
        S.katha_end(KATHA[4]))

    # ---- (212-4) 5-7. Tissopikathā ------------------------------------------------------------------------------
    heading("5-30-5-0", 4, VAGGA)
    heading("5-30-5-1-0", 5, f"(212-4) 5-7. {TISSOPI}")
    add("5-898", f"{Q(f'{GB} có {AP}')} {YES} {Q(f'{SLEEP} có {AP}')} {NO_PE}")
    add("5-899", f"{Q(f'{SP} có {DA}')} {YES} {Q(f'{SLEEP} có {DA}')} {NO_PE}")
    add("5-900",
        f"{Q(f'{SP} có {AP}')} {YES} {Q(f'{SLEEP} có {AP}')} {NO_PE}",
        f"{TISSOPI} đã hoàn tất.")

    # ---- (215) 8. Abyākatakathā ---------------------------------------------------------------------------------
    heading("5-30-6-0", 4, VAGGA)
    heading("5-30-6-1-0", 5, f"(215) 8. {S.katha(KATHA[6])}")
    KILL = f"{DR} sát hại sinh mạng"
    LIST = (f"{DR} {EVIL[0]}{PE} " + ", ".join(EVIL[1:]) + f", {DR} {METH}, {ASUCI}, {DR} thực hiện sự bố thí, "
            f"cho {CIV}, cho {PIN}, cho {SEN}, cho {GIL}, cho {KHA}, cho {BHO}, cho {PAN}, đảnh lễ {CET}, "
            f"dâng vòng hoa lên {CET}, dâng hương thơm, dâng dầu thoa{PE} {ABHID}")
    add("5-901",
        f"{Q(T6)} {YES} {Q(KILL)} {YES} {hanci_neg(KILL, T6)}",
        f"{Q(LIST)} {YES} {hanci_neg(f'{DR} {ABHID}', T6)}")
    add("5-902",
        f"{na_vattabbam(T6)} {YES} {NANU(ABBO)} {YES} {hanci(ABBO, T6)}",
        S.katha_end(KATHA[6]))

    # ---- (216) 9. Āsevanapaccayakathā ---------------------------------------------------------------------------
    heading("5-30-7-0", 4, VAGGA)
    heading("5-30-7-1-0", 5, f"(216) 9. {S.katha(KATHA[7])}")

    def sutta(quote, end):
        return f"{Q(T7)} {YES} {S.NANU_VUTTAM} “{quote}”{end} {S.ATTHEVA} {YES} {S.tena_hi(T7P)}"

    SU1 = f"{BH}, {PAT_K}, {ASB}, {HELL}, {lv(PAT_K, 'tuổi thọ ngắn')}"
    SU2 = (f"{BH}, {ADIN}, {ASB}, {HELL}, {lv(ADIN, 'sự tổn hại về tài sản')}{PE} "
           f"{lv(KAMA, 'sự thù địch và oán hận')}{PE} {lv(MUSA, 'sự vu khống điều không có thật')}{PE} "
           f"{lv(PIS, 'sự chia lìa với bạn bè')}{PE} {lv(PHA, 'âm thanh không đáng ưa thích')}{PE} "
           f"{lv(SAM, 'lời nói không được tin nhận')}, {BH_L}, {SURA}, khi được thực hành{PE} "
           f"{lv(SURA, 'sự điên loạn')}")
    add("5-903",
        sutta(SU1, f" [{C_AN} 8.40]."),
        sutta(SU2, f" [{C_AN} 8.40]!"))
    add("5-904",
        sutta(f"{BH}, quan điểm sai lầm, {ASB}, {HELL}", "."),
        sutta(f"Tư duy sai lầm{PE} {BH_L}, định tâm sai lầm, khi được thực hành, được tu tập{PE} "
              "dẫn đến cõi ngạ quỷ", "!"))
    add("5-905",
        sutta(f"{BH}, quan điểm đúng đắn, {ASB}, {AMATA}", "!"),
        sutta(f"{BH}, tư duy đúng đắn, {ASB}{PE} {BH_L}, định tâm đúng đắn, {ASB}, {AMATA}", "."),
        S.katha_end(KATHA[7]))

    # ---- (217) 10. Khaṇikakathā ---------------------------------------------------------------------------------
    heading("5-30-8-0", 4, VAGGA)
    heading("5-30-8-1-0", 5, f"(217) 10. {S.katha(KATHA[8])}")
    ST = "đứng vững"                                                     # saṇṭhāti / saṇṭhahanti (termbase)
    NAT = ", ".join(f"{n} {ST}" for n in NATURE) + f", {TINA} {ST}"
    EYE = (f"“{eye(AV, 'mắt', 'hình sắc', False, False)}, {NOT_YET}{S.var(CIT['bahūsu'], 'viññāṇabhāvassa')}. "
           f"{eye(AV, 'mắt', 'hình sắc', True, False)}, {NOT_YET}. "
           f"{eye(AV, 'mắt', 'hình sắc', True, True)}, {THEN}” [{C_MN} 1.306]!")
    BODY = (f"“{eye(AV, 'thân', 'vật xúc chạm', False)}{PE} "
            f"{eye(AV_L, 'thân', 'vật xúc chạm', True)}{PE} "
            f"{eye(AV_L, 'thân', 'vật xúc chạm', True, True)}, {THEN}” [{C_MN} 1.306]!")
    add("5-906",
        f"{Q(T8)} {YES} Có phải trong một tâm, {NAT} không? {NO_PE}",
        f"{Q(T8)} {YES} {Q(SAHA_C)} {NO_PE} {q(SAHA_C)} {YES} {SARI} {EYE} {S.ATTHEVA} {YES} "
        f"{S.tena_hi_na(SAHA_C)}",
        f"Có phải lĩnh vực tai{PE} lĩnh vực mũi{PE} lĩnh vực lưỡi{PE} {SAHA_K} không? {NO_PE} {q(SAHA_K)} {YES} "
        f"{SARI} {BODY} {S.ATTHEVA} {YES} {S.tena_hi_na(SAHA_K)}")
    add("5-907",
        f"{na_vattabbam(T8)} {YES} {Q(f'tất cả các hiện tượng đều {NICCA}')} {NO} {S.tena_hi(T8)}",
        S.katha_end(KATHA[8]),
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
    adh = S.FORMULAS_MD.parent / "adh-30"           # byte-identical copy for termbase_adherence_vi.py
    adh.mkdir(exist_ok=True)
    (adh / NAME).write_text(text, encoding="utf-8", newline="\n")
    print("wrote", adh / NAME)


if __name__ == "__main__":
    main()
