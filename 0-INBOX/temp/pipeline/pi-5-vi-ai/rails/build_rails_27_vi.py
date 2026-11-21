"""pi-5 Kathāvatthu, Vietnamese RAILS (plain audience): chapter 27, Ekūnavīsatimavaggo (^5-27-0 … ^5-856): eight
kathās (186-193) with the repeated "Ekūnavīsatimavaggo" sub-headings, the vagga close and the uddāna.

Builds AI_translation/vietnamese/pi-5-vietnamese-plain-rails_split_chapters/27-ekunavisatimavaggo.md from the fixed
strings below, importing the approved sample builder READ-ONLY (frames Q, q, NANU, hanci, hanci_neg, na_vattabbam,
tena_hi, katha, katha_end, katva, var …). Strings taken from pi-1 … pi-4 rails are asserted there (REUSED27);
strings shared with the finished pi-5 rails chapters are asserted in those chapter files (SHARED).
The per-line dash / quote / NFC / id checks of S.check_against_pali run before writing.
New recurring strings: notes-rails-27.md.

usage: python -I -X utf8 -B build_rails_27_vi.py          (writes the chapter and the adherence copy rails\\adh-27\\)
       python -I -X utf8 -B build_rails_27_vi.py --find <regex> [max] [chars]   (finished pi-5 rails chapters)
       python -I -X utf8 -B build_rails_27_vi.py --tb                          (keywords of this chapter + termbase)
       python -I -X utf8 -B build_rails_27_vi.py --word <regex>                (grep termbase headwords)
"""
import pathlib
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai\rails")
import build_rails_sample_vi as S  # noqa: E402

NAME = "27-ekunavisatimavaggo.md"
Q, q, NANU, PE, YES, NO, NO_PE = S.Q, S.q, S.NANU, S.PE, S.YES, S.NO, S.NO_PE
cap, RE, CIT = S.cap, S.RE, S.CIT
ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
TB = ROOT / "AI_translation/vietnamese/pi-5-pali-vietnamese-termbase-plain.md"
KW = ROOT / "AI_translation/pali/pi-5-keywords-by-reference-pali-plain.md"
FINISHED = ["1-puggalakatha.md", "2-parihanikatha.md", "3-brahmacariyakatha.md", "4-jahatikatha.md",
            "5-sabbamatthitikatha.md", "6-atitakkhandhadikatha.md", "7-ekaccam-atthitikatha.md",
            "8-satipatthanakatha.md", "9-hevatthikatha.md", "10-dutiyavaggo.md", "11-tatiyavaggo.md",
            "12-catutthavaggo.md", "13-pancamavaggo.md", "14-chatthavaggo.md", "15-sattamavaggo.md",
            "16-atthamavaggo.md", "17-navamavaggo.md", "18-dasamavaggo.md", "19-ekadasamavaggo.md",
            "20-dvadasamavaggo.md", "21-terasamavaggo.md", "22-cuddasamavaggo.md", "23-pannarasamavaggo.md"]


def nanu_l(x):                      # nanu Xti? (after …pe…, lower case; ch15)
    return f"chẳng phải {x} sao?"


# ---------------------------------------------------------------------------------------------------------------
# Headings, kathā names, vagga close
# ---------------------------------------------------------------------------------------------------------------
VAGGA = "Chương thứ mười chín"                                          # Ekūnavīsatimavaggo (termbase)
KATHA = {1: "sự dứt bỏ phiền não", 2: "sự trống rỗng", 3: "thành quả của đời sống sa-môn", 4: "sự đạt đến",
         5: "tính đúng như thật", 6: "điều thiện", 7: "sự cố định hoàn toàn", 8: "các năng lực"}
#   Kilesajahana- (termbase kilesa, jahana), Suññatā-, Sāmaññaphala-, Patti-, Tathatā-, Kusala- («điều» as ch21
#   Kusalapaṭilābhakathā, ch22 Abyākatakathā), Accantaniyāma- (termbase accantaniyāma), Indriyakathā
TASSUDDANAM = "Tóm tắt của chương này –"                               # Tassuddānaṃ – (ch9)

# ---------------------------------------------------------------------------------------------------------------
# Shared vocabulary (termbase; pi-1 … pi-4; finished pi-5 chapters)
# ---------------------------------------------------------------------------------------------------------------
BH = "Này các tỳ-khưu"                                                  # bhikkhave (sample)
ASK = "không do điều kiện tạo thành"                                    # asaṅkhato / -ṃ / -ā (termbase, ch14)
SK = "do điều kiện tạo thành"                                           # saṅkhato / -ṃ (termbase, ch14)
ASKT = f"điều {ASK}"                                                    # asaṅkhatāni (noun; ch14)
NIB = "Niết-bàn"                                                        # nibbānaṃ
NIB_LIST = ("đó là Niết-bàn, nơi che chở, nơi ẩn náu, nơi nương tựa, nơi đến cuối cùng, điều bất biến, "
            "điều bất tử")                                              # Nibbānaṃ tāṇaṃ … amataṃ (ch14)
NIB_PE = f"đó là Niết-bàn{PE} điều bất tử"                              # Nibbānaṃ…pe… amataṃ
NIB_PE2 = f"đó là Niết-bàn{PE} điều bất biến, điều bất tử"              # Nibbānaṃ…pe… accutaṃ amataṃ
LW, LU = "thuộc thế gian", "vượt thế gian"                              # lokiya / lokuttara (termbase, ch10, ch23)
KIL = "các phiền não"                                                   # kilese (termbase, ch3)
SK_KH = "khối tạo tác"                                                  # saṅkhārakkhandha (termbase, pi-2)
PARI = "nằm trong"                                                      # pariyāpanna (APPROVED)
SUN = "sự trống rỗng"                                                   # suññatā (termbase, ch11)
ANIM, APP = "cái không có dấu hiệu", "cái không mong cầu"               # animittaṃ / appaṇihito (termbase, ch11)
SPH = "thành quả của đời sống sa-môn"                                   # sāmaññaphalaṃ (termbase, ch4)
SAM = "đời sống sa-môn"                                                 # sāmaññaṃ
PATTI = "sự đạt đến"                                                    # patti (termbase)
TATH = "tính đúng như thật của tất cả các hiện tượng"                   # sabbadhammānaṃ tathatā (termbase tathatā)
NDH = "yếu tố Niết-bàn"                                                 # nibbānadhātu (termbase)
NDH_K = f"{NDH} là thiện"                                               # nibbānadhātu kusalā (termbase phrase)
ACC = "tính cố định hoàn toàn"                                          # accantaniyāmatā (termbase)
PUTH = "người phàm phu"                                                 # puthujjanassa (termbase)
T_ACC = f"{PUTH} có {ACC}"                                              # atthi puthujjanassa accantaniyāmatā
ACCP = "người cố định hoàn toàn"                                        # accantaniyatassa puggalassa (niyatassa puggalassa)
VIC = "sự hoài nghi"                                                    # vicikicchā (termbase)
SD, UD = "quan điểm về sự trường tồn", "quan điểm về sự đoạn diệt"      # sassata- / ucchedadiṭṭhi (termbase)
AKM = "con đường bất thiện"                                             # akusalo maggo (termbase Akusalena maggena)
NIY_POS = (f"dẫn đến giải thoát, dẫn đến sự diệt tận, dẫn đến sự giác ngộ, không phải là đối tượng của ô nhiễm{PE} "
           f"không phải là đối tượng của phiền não")                    # niyyāniko … anāsavo…pe… asaṃkilesiko (ch4)
NIY_NEG = f"không dẫn đến giải thoát{PE} là đối tượng của phiền não"    # aniyyāniko…pe… saṃkilesiko (ch4)
AV = f"nó có sự hướng đến{PE} sự mong cầu"                              # atthi tāya / tassa āvaṭṭanā…pe… paṇidhi (ch15)
AVN = f"nó không có sự hướng đến{PE} sự mong cầu"                       # natthi tāya / tassa āvaṭṭanā…pe… paṇidhi (ch15)
SAR, ANR = "có đối tượng", "không có đối tượng"                         # sārammaṇa / anārammaṇa (termbase, ch15)
LIST5 = ["niềm tin", "sự tinh tấn", "sự tỉnh thức", "sự định tâm", "trí tuệ"]   # saddhā … paññā (ch17, ch23)
ROOTS = ["sự không tham lam", "sự không sân hận", "sự không si mê"]     # alobho / adoso / amoho (termbase)


def a(x):                             # X asaṅkhato
    return f"{x} {ASK}"


def s(x):                             # X saṅkhato
    return f"{x} {SK}"


def n_ask(n):                         # N asaṅkhatāni (ch14)
    return f"có {n} {ASKT}"


def refuges_pe(n):                    # N tāṇāni…pe… antarikā vā (ch14)
    return f"có {n} nơi che chở{PE} hoặc khoảng cách"


def block(first, x, nib=NIB_LIST, n="hai", lower=False):
    """X asaṅkhato? Āmantā. Nibbānaṃ … amatanti? … X asaṅkhato, nibbānaṃ asaṅkhatanti? Āmantā. Dve asaṅkhatānīti?
    … dve asaṅkhatānīti? Āmantā. Dve tāṇāni…pe… antarikā vāti? Na hevaṃ vattabbe…pe… (ch14 two_block)."""
    head = q(first) if lower else Q(first)
    return (f"{head} {YES} {Q(nib)} {NO_PE} {q(f'{x}, {a(NIB)}')} {YES} {Q(n_ask(n))} {NO_PE} "
            f"{q(n_ask(n))} {YES} {Q(refuges_pe(n))} {NO_PE}")


def count_tail(first, n):             # X…, nibbānaṃ asaṅkhatanti? Āmantā. N asaṅkhatānīti? … N tāṇāni…pe… antarikā vāti?
    return (f"{Q(first)} {YES} {Q(n_ask(n))} {NO_PE} {q(n_ask(n))} {YES} {Q(refuges_pe(n))} {NO_PE}")


AGG5 = f"vật chất{PE} cảm giác{PE} tri giác{PE} các tạo tác{PE} thức"   # rūpaṃ… vedanā… saññā… saṅkhārā… viññāṇaṃ

# ---- Kilesajahana -------------------------------------------------------------------------------------------------
J_PAST, J_FUT, J_NOW = (f"dứt bỏ {KIL} thuộc quá khứ", f"dứt bỏ {KIL} thuộc tương lai",
                        f"dứt bỏ {KIL} thuộc hiện tại")                 # atīte / anāgate / paccuppanne kilese jahati
J_ALL = f"{J_PAST}, {J_FUT}, {J_NOW}"
PAST_V = ("làm chấm dứt cái đã chấm dứt, làm mất đi cái đã mất đi, làm diệt tận cái đã bị diệt tận, "
          "làm biến mất cái đã biến mất, làm biến mất hoàn toàn cái đã biến mất hoàn toàn")
#   Niruddhaṃ nirodheti, vigataṃ vigameti, khīṇaṃ khepeti, atthaṅgataṃ atthaṅgameti, abbhatthaṅgataṃ abbhatthaṅgameti
#   (termbase; participles as ch5 «đã chấm dứt, đã mất đi, … đã biến mất, đã biến mất hoàn toàn»)
FUT_V = ("làm cho cái chưa sinh ra không sinh ra, làm cho cái chưa sinh thành không sinh thành, "
         "làm cho cái chưa phát sinh không phát sinh, làm cho cái chưa hiện ra không hiện ra")
#   Ajātaṃ ajaneti, asañjātaṃ asañjaneti, anibbattaṃ anibbatteti, apātubhūtaṃ apātubhāveti (termbase; ch5 participles)
RATTO = ("Có phải người đã tham đắm dứt bỏ sự tham đắm, người đã sân hận dứt bỏ sự sân hận, người đã si mê dứt bỏ "
         "sự si mê, người đã bị phiền não làm ô nhiễm dứt bỏ các phiền não không? Không nên nói như vậy… có phải bằng "
         "sự tham đắm mà dứt bỏ sự tham đắm, bằng sự sân hận mà dứt bỏ sự sân hận, bằng sự si mê mà dứt bỏ sự si mê, "
         "bằng các phiền não mà dứt bỏ các phiền não không? Không nên nói như vậy…")   # (ch21 ^5-665 line 1, verbatim)
RAGA_C = "Có phải sự tham đắm gắn liền với tâm, con đường gắn liền với tâm không?"   # (ch21)
TWO_C = "Có phải có sự tụ hợp của hai tâm không?"                       # Dvinnaṃ cittānaṃ samodhānaṃ hotīti? (ch10, ch15)
RAGA_K = "Có phải sự tham đắm là bất thiện, con đường là thiện không?"  # (ch21, lower case there)
KUSALA_DH = ("các hiện tượng thiện và bất thiện, có lỗi và không có lỗi, thấp kém và ưu việt, đen tối và trong sáng "
             "cùng với các mặt đối lập của chúng đi đến chỗ cùng hiện diện đối mặt nhau")   # (ch15, ch18, ch21)
VIDURA = ("Có phải các hiện tượng thiện và bất thiện, có lỗi và không có lỗi, thấp kém và ưu việt, đen tối và trong "
          "sáng cùng với các mặt đối lập của chúng đi đến chỗ cùng hiện diện đối mặt nhau không? Đúng vậy. Chẳng phải "
          "Đức Thế Tôn đã nói thế này sao – “Này các tỳ-khưu, có bốn điều rất xa cách nhau này! Bốn điều nào? Này các "
          "tỳ-khưu, bầu trời và mặt đất – đây là điều rất xa cách nhau thứ nhất… vì vậy, bản chất của người hiền thiện "
          "ở xa kẻ không hiền thiện”. Có bài kinh như vậy thật không? Đúng vậy. Vậy thì không nên nói – “các hiện tượng "
          "thiện và bất thiện… đi đến chỗ cùng hiện diện đối mặt nhau”.")   # (ch21 ^5-665 line 3, identical Pāli)

# ---- Suññatā ------------------------------------------------------------------------------------------------------
T_SUN = f"{SUN} {PARI} {SK_KH}"                                         # suññatā saṅkhārakkhandhapariyāpannā (termbase)
NEG8 = ("không vô thường, không do điều kiện tạo thành, không sinh khởi tùy thuộc vào điều kiện, không có bản chất "
        "diệt tận, không có bản chất suy tàn, không có bản chất phai nhạt, không có bản chất chấm dứt, không có bản "
        "chất biến đổi")                                                # na anicco na saṅkhato … na vipariṇāmadhammo
KH = {"r": "khối vật chất", "v": "khối cảm giác", "s": "khối tri giác", "n": "khối thức"}   # (pi-2 khandha names)


def sun_of(k):                        # X-kkhandhassa suññatā
    return f"{SUN} của {KH[k] if k in KH else SK_KH}"


def nv(subj, pred):                   # X na vattabbā – "Y"ti? (ch11 «đối với X, không nên nói – “Y”»)
    return f"có phải đối với {subj}, không nên nói – “{pred}” không?"


SUTTA_SUN = (f"“{BH}, các tạo tác này trống rỗng tự ngã hay những gì thuộc về tự ngã” "
             f"[{CIT['ma. ni.']} 3.69, trong kinh Thích Hợp Với Trạng Thái Bất Động]!")
#   "suññamidaṃ, bhikkhave, saṅkhārā attena vā attaniyena vā"ti [ma. ni. 3.69 āneñjasappāye]! (sample «trống rỗng
#   tự ngã hay những gì thuộc về tự ngã»; ch16 «…, trong kinh …»)

# ---- Sāmaññaphala / Patti / Tathatā -------------------------------------------------------------------------------
SO_P, SA_P, AN_P, AR_P = ("thành quả vào dòng", "thành quả trở lại một lần", "thành quả không trở lại",
                          "thành quả A-la-hán")                         # (termbase, pi-4 names)
SO_M, SA_M, AN_M, AR_M = ("con đường vào dòng", "con đường trở lại một lần", "con đường không trở lại",
                          "con đường A-la-hán")                         # (termbase)
REQ = ["y phục", "đồ ăn khất thực", "chỗ ở", "thuốc men và vật dụng chữa bệnh"]   # cīvara … parikkhāra (pi-2)
JH = ["tầng thiền thứ nhất", "tầng thiền thứ hai", "tầng thiền thứ ba", "tầng thiền thứ tư",
      "lĩnh vực không gian vô tận", "lĩnh vực thức vô tận", "lĩnh vực không có gì cả",
      "lĩnh vực không phải tri giác cũng không phải không tri giác",
      SO_M, SO_P, SA_M, SA_P, AN_M, AN_P, AR_M, AR_P]                   # (pi-1)
EVAM = "(tất cả nên được trình bày chi tiết như vậy)"                  # (evaṃ sabbaṃ vitthāretabbaṃ) (termbase)


def pt(x):                            # X-assa patti
    return f"{PATTI} {x}"


def ta(x):                            # X-assa X-tā
    return f"tính chất {x}"


# ---- Accantaniyāma ------------------------------------------------------------------------------------------------
KILLERS = ["kẻ giết mẹ", "kẻ giết cha", "kẻ giết bậc A-la-hán", "kẻ làm chảy máu", "kẻ chia rẽ Tăng đoàn"]   # (ch10)
FIXED = "được cố định hoàn toàn"                                         # accantaniyato (ch23 «được cố định»)
NIM = "Ở đời này, này các tỳ-khưu, có người mang các hiện tượng bất thiện hoàn toàn đen tối, người ấy"
#   idha, bhikkhave, ekacco puggalo samannāgato hoti ekantakāḷakehi akusalehi dhammehi, so (pi-4 «Ở đời này, có
#   người mang các hiện tượng bất thiện hoàn toàn đen tối»)
SAKIM = "một lần chìm thì chìm luôn"                                    # sakiṃ nimuggo nimuggova hoti (pi-4)
UM1 = "trồi lên rồi lại chìm"                                            # ummujjitvā nimujjati (pi-4)
UM2 = ("trồi lên rồi đứng yên, trồi lên rồi nhìn thấy rõ, nhìn quanh, trồi lên rồi bơi qua, trồi lên rồi đạt đến "
       "chỗ chân chạm đáy")                                              # ummujjitvā ṭhito hoti … patigādhappatto hoti (pi-4)
UM_END = "trồi lên rồi đạt đến chỗ chân chạm đáy"
A715 = f"{CIT['a. ni.']} 7.15"
SUT_NIM = f"“{NIM} {SAKIM}”"

# ---- Indriya ------------------------------------------------------------------------------------------------------
IND = {"saddhā": "năng lực niềm tin", "vīriya": "năng lực tinh tấn", "sati": "năng lực tỉnh thức",
       "samādhi": "năng lực định tâm", "paññā": "năng lực trí tuệ", "mano": "năng lực ý",
       "somanassa": "năng lực niềm vui", "jīvita": "năng lực sống"}     # (pi-2)
PL = {"saddhā": "niềm tin", "vīriya": "sự tinh tấn", "sati": "sự tỉnh thức", "samādhi": "sự định tâm",
      "paññā": "trí tuệ", "mano": "ý", "somanassa": "niềm vui", "jīvita": "sự sống"}   # (termbase; ch23 LIST5)
EX, NEX = "tồn tại", "không tồn tại"                                    # atthi / natthi (termbase; coordinator rule)


def ex(k, w=LW, faculty=False, neg=False):   # (n)atthi lokiyā saddhā / lokiyaṃ saddhindriyaṃ
    return f"{(IND if faculty else PL)[k]} {w} {NEX if neg else EX}"


def pair(k, w=LW, neg2=False, k1=None):      # atthi lokiyā X, (n)atthi lokiyaṃ X-indriyaṃ
    return f"{ex(k1 or k, w)}, {ex(k, w, True, neg2)}"


PANCA = f"năm năng lực {LW}"                                            # lokiyāni pañcindriyāni (ch14 «năm năng lực»)
SUT_IND = (f"“{BH}, khi quan sát thế gian bằng mắt của Đức Phật, Ta đã thấy các chúng sinh có ít bụi trong mắt, "
           f"có nhiều bụi trong mắt, có các năng lực sắc bén, có các năng lực non yếu, có phẩm chất tốt, dễ hướng dẫn, "
           f"và một số sống thấy sự đáng sợ nơi thế gian khác và nơi lỗi lầm” "
           f"[{CIT['ma. ni.']} 1.283, ở đó cũng thấy các từ như “dvākāre duviññāpaye”]!")
#   "addasaṃ kho ahaṃ, bhikkhave, buddhacakkhunā lokaṃ volokento satte apparajakkhe mahārajakkhe, tikkhindriye
#   mudindriye, svākāre, suviññāpaye, appekacce paralokavajjabhayadassāvino viharante"ti [ma. ni. 1.283 tattha
#   "dvākāre duviññāpaye" iccādīnipi padāni dissanti]! (pi-2 ^2-814 wording for the qualities)

UDDANA = (f"{cap(J_ALL)}, {T_SUN}, {a(SPH)}, {a(PATTI)}, {a(TATH)}, {NDH_K}, {T_ACC}, {PANCA} {NEX}.")
#   Atīte kilese jahati anāgate … paccuppanne kilese jahati, suññatā …, natthi lokiyāni pañcindriyānīti.

REUSED27 = [  # (Pāli, Vietnamese, book)
    ("Sakiṃ nimuggo nimuggova hoti", SAKIM, "4"), ("ummujjitvā nimujjati", UM1, "4"),
] + [("ummujjitvā ṭhito hoti, … paṭigādhappatto hoti (one by one)", x, "4") for x in UM2.split(", trồi")[0:1]] + [
    ("ummujjitvā vipassati viloketi", "trồi lên rồi nhìn thấy rõ, nhìn quanh", "4"),
    ("ummujjitvā patarati", "trồi lên rồi bơi qua", "4"), ("ummujjitvā paṭigādhappatto hoti", UM_END, "4"),
    ("Idhekacco puggalo samannāgato hoti ekantakāḷakehi akusalehi dhammehi",
     "có người mang các hiện tượng bất thiện hoàn toàn đen tối", "4"),
    ("apparajakkhe mahārajakkhe tikkhindriye mudindriye svākāre",
     "có ít bụi trong mắt, có nhiều bụi trong mắt, có các năng lực sắc bén, có các năng lực non yếu, có phẩm chất tốt",
     "2"),
    ("suviññāpaye", "dễ hướng dẫn", "2"),
    ("cīvarapiṇḍapātasenāsanagilānapaccayabhesajjaparikkhāra", ", ".join(REQ), "2"),
    ("ākāsānañcāyatana", JH[4], "1"), ("viññāṇañcāyatana", JH[5], "1"), ("ākiñcaññāyatana", JH[6], "1"),
    ("nevasaññānāsaññāyatana", JH[7], "1"), ("catutthaṃ jhānaṃ", JH[3], "1"),
    ("saṅkhārakkhandha", SK_KH, "2"),
] + [(f"{k}indriya", v, "2") for k, v in IND.items() if k not in ("saddhā", "vīriya", "paññā", "mano", "jīvita")] + [
    ("saddhindriya", IND["saddhā"], "2"), ("vīriyindriya", IND["vīriya"], "2"), ("paññindriya", IND["paññā"], "2"),
    ("manindriya", IND["mano"], "2"), ("jīvitindriya", IND["jīvita"], "2"),
]

SHARED = [  # (Pāli, Vietnamese, finished pi-5 rails chapter)
    ("Tassuddānaṃ –", TASSUDDANAM, "9-hevatthikatha.md"),
    ("Ratto rāgaṃ jahati … kilesehi kilese jahatīti? Na hevaṃ vattabbe…pe….", RATTO, "21-terasamavaggo.md"),
    ("Rāgo cittasampayutto, maggo cittasampayuttoti?", RAGA_C, "21-terasamavaggo.md"),
    ("rāgo akusalo, maggo kusaloti?", RAGA_K[8:], "21-terasamavaggo.md"),
    ("Kusalākusalā … āgacchantīti? Āmantā. Nanu vuttaṃ … kusalākusalā…pe… āgacchantī\"ti.", VIDURA,
     "21-terasamavaggo.md"),
    ("kusalākusalā sāvajjānavajjā … āgacchanti", KUSALA_DH, "18-dasamavaggo.md"),
    ("dvinnaṃ … cittānaṃ samodhānaṃ", "Có phải có sự tụ hợp của hai", "10-dutiyavaggo.md"),
    ("dvinnaṃ cittānaṃ samodhānaṃ", "hai tâm không?", "10-dutiyavaggo.md"),
    ("atītaṃ niruddhaṃ vigataṃ … atthaṅgataṃ abbhatthaṅgataṃ",
     "quá khứ đã chấm dứt, đã mất đi, đã biến đổi, đã biến mất, đã biến mất hoàn toàn", "5-sabbamatthitikatha.md"),
    ("anāgataṃ ajātaṃ abhūtaṃ asañjātaṃ anibbattaṃ … apātubhūtaṃ",
     "tương lai chưa sinh ra, chưa trở thành, chưa sinh thành, chưa phát sinh, chưa phát sinh rõ rệt, chưa hiện ra",
     "5-sabbamatthitikatha.md"),
    ("atītaṃ atthi", "quá khứ tồn tại", "5-sabbamatthitikatha.md"),
    ("kilese jahati", "dứt bỏ các phiền não", "3-brahmacariyakatha.md"),
    ("suññatā / animitta / appaṇihita", f"cái không có dấu hiệu… có đối tượng là {APP}", "11-tatiyavaggo.md"),
    ("X na vattabbaṃ – \"Y\"nti?", "Có phải đối với các sự thiết lập tỉnh thức cao quý, không nên nói – “",
     "11-tatiyavaggo.md"),
    ("suññaṃ attena vā attaniyena vā", "trống rỗng tự ngã hay những gì thuộc về tự ngã", "1-puggalakatha.md"),
    ("[a. ni. 6.63 nibbedhikasutte]", f"[{CIT['a. ni.']} 6.63, trong kinh Thấu Triệt]", "16-atthamavaggo.md"),
    ("Nibbānaṃ tāṇaṃ leṇaṃ saraṇaṃ parāyanaṃ accutaṃ amatanti?", Q(NIB_LIST), "14-chatthavaggo.md"),
    ("Dve asaṅkhatānīti?", Q(n_ask("hai")), "14-chatthavaggo.md"),
    ("Dve tāṇāni…pe… antarikā vāti?", Q(refuges_pe("hai")), "14-chatthavaggo.md"),
    ("Pañca tāṇāni…pe… antarikā vāti?", Q(refuges_pe("năm")), "14-chatthavaggo.md"),
    ("pañcindriyāni (uddāna)", "năm năng lực", "14-chatthavaggo.md"),
    ("sotāpattimaggo asaṅkhato", a(SO_M), "14-chatthavaggo.md"),
    ("thành quả của đời sống sa-môn", "ba thành quả của đời sống sa-môn", "4-jahatikatha.md"),
    ("Katamena maggenāti?", "Bằng con đường nào?", "4-jahatikatha.md"),
    ("niyyāniko khayagāmī bodhagāmī", "dẫn đến giải thoát, dẫn đến sự diệt tận, dẫn đến sự giác ngộ",
     "4-jahatikatha.md"),
    ("anāsavo…pe… asaṃkilesiyo", "không phải là đối tượng của ô nhiễm… không phải là đối tượng của phiền não",
     "4-jahatikatha.md"),
    ("aniyyāniko … saṃkilesiyo", "không dẫn đến giải thoát", "4-jahatikatha.md"),
    ("…pe… saṃkilesiyo", "là đối tượng của phiền não", "4-jahatikatha.md"),
    ("sārammaṇā; atthi tāya āvaṭṭanā…pe… paṇidhīti?", f"{SAR}; {AV} không?", "15-sattamavaggo.md"),
    ("anārammaṇā; natthi tāya āvaṭṭanā…pe… paṇidhi", f"{ANR}; {AVN}", "15-sattamavaggo.md"),
    ("mātughātako … saṅghabhedako", f"{KILLERS[0]} tu tập con đường{PE} {f'{PE} '.join(KILLERS[1:])}",
     "10-dutiyavaggo.md"),
    ("saddhā vīriyaṃ sati samādhi paññā", ", ".join(LIST5), "17-navamavaggo.md"),
    ("pahīnā", "đã được dứt bỏ", "12-catutthavaggo.md"),
    ("Kusalapaṭilābhakathā", "Bàn về sự có được điều thiện", "21-terasamavaggo.md"),
    ("Vuttaṃ bhagavatā – \"…\"ti katvā teneva kāraṇena", "Có phải vì cho rằng Đức Thế Tôn đã nói – “",
     "1-puggalakatha.md"),
    ("sotāpattiphalaṃ", SO_P, "4-jahatikatha.md"),
    ("lokiyaṃ jhānaṃ", f"tầng thiền thứ nhất {LW}", "10-dutiyavaggo.md"),
    ("lokuttaraṃ jhānaṃ", f"tầng thiền thứ nhất {LU}", "10-dutiyavaggo.md"),
]


def check_strings():
    texts = {b: unicodedata.normalize("NFC", "\n".join(p.read_text(encoding="utf-8")
                                                       for p in sorted(d.glob("*.md")))).lower()
             for b, d in S.RAILS.items()}
    bad = [(p, v, b) for p, v, b in REUSED27 if unicodedata.normalize("NFC", v).lower() not in texts[b]]
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
        lines = [unicodedata.normalize("NFC", x) for x in lines]
        lines[-1] = lines[-1] + f" ^{i}"
        segs.append(lines)

    def heading(i, level, text):
        add(i, "#" * level + " " + text)

    def sub(k, n):                  # #### Ekūnavīsatimavaggo / ##### (n) k. X-kathā
        heading(f"5-27-{k}-0", 4, VAGGA)
        heading(f"5-27-{k}-1-0", 5, f"({n}) {k}. {S.katha(KATHA[k])}")

    heading("5-27-0", 3, VAGGA)

    # ---- (186) 1. Kilesajahanakathā -----------------------------------------------------------------------------
    heading("5-27-1-0", 4, f"(186) 1. {S.katha(KATHA[1])}")
    add("5-828",
        f"{Q(J_PAST)} {YES} {Q(PAST_V)} {NO_PE} {q(J_PAST)} {YES} {NANU('quá khứ đã chấm dứt')} {YES} "
        f"{S.hanci_neg('quá khứ đã chấm dứt', J_PAST)} {Q(J_PAST)} {YES} {NANU('quá khứ không tồn tại')} {YES} "
        f"{S.hanci_neg('quá khứ không tồn tại', J_PAST)}")
    add("5-829",
        f"{Q(J_FUT)} {YES} {Q(FUT_V)} {NO_PE} {q(J_FUT)} {YES} {NANU('tương lai chưa sinh ra')} {YES} "
        f"{S.hanci_neg('tương lai chưa sinh ra', J_FUT)} {Q(J_FUT)} {YES} {NANU('tương lai không tồn tại')} {YES} "
        f"{S.hanci_neg('tương lai không tồn tại', J_FUT)}")
    add("5-830",
        f"{Q(J_NOW)} {YES} {RATTO}",
        f"{RAGA_C} {YES} {TWO_C} {NO_PE}",
        f"{RAGA_K} {YES} {Q(KUSALA_DH)} {NO_PE}",
        VIDURA)
    add("5-831",
        f"{S.na_vattabbam(J_ALL)} {YES} {Q(f'không có ai dứt bỏ {KIL}')} {NO_PE} vậy thì {J_ALL}.",
        S.katha_end(KATHA[1]))

    # ---- (187) 2. Suññatākathā ----------------------------------------------------------------------------------
    sub(2, 187)
    add("5-832",
        f"{Q(T_SUN)} {YES} {Q(f'{ANIM} {PARI} {SK_KH}')} {NO_PE} {q(T_SUN)} {YES} {Q(f'{APP} {PARI} {SK_KH}')} "
        f"{NO_PE} {nv(ANIM, f'{PARI} {SK_KH}')} {YES} {cap(nv(SUN, f'{PARI} {SK_KH}'))} {NO_PE} "
        f"{nv(APP, f'{PARI} {SK_KH}')} {YES} {cap(nv(SUN, f'{PARI} {SK_KH}'))} {NO_PE}",
        f"{Q(T_SUN)} {YES} {Q(f'{SK_KH} {NEG8}')} {NO_PE} {nanu_l(f'{SK_KH} {S.ANICCA}')} {YES} "
        f"{S.hanci_neg(f'{SK_KH} vô thường{PE} có bản chất biến đổi', T_SUN)}")
    S_R, S_S, S_N = sun_of("r"), sun_of("sk"), sun_of("n")         # rūpa- / saṅkhāra- / viññāṇakkhandhassa suññatā
    IN_SK, IN_R, IN_N = f"{PARI} {SK_KH}", f"{PARI} {KH['r']}", f"{PARI} {KH['n']}"
    IN_VSN = f"{PARI} {KH['v']}{PE} {PARI} {KH['s']}{PE} {IN_N}"
    add("5-833",
        f"{Q(f'{S_R} {IN_SK}')} {YES} {Q(f'{S_S} {IN_R}')} {NO_PE} "
        f"có phải {sun_of('v')}{PE} của {KH['s']}{PE} của {KH['n']} {IN_SK} không? {YES} "
        f"{Q(f'{S_S} {IN_N}')} {NO_PE}",
        f"{cap(nv(S_S, IN_R))} {YES} {cap(nv(S_R, IN_SK))} {NO_PE} {nv(S_S, IN_VSN)} {YES} "
        f"{cap(nv(S_N, IN_SK))} {NO_PE}")
    add("5-834",
        f"{S.na_vattabbam(T_SUN)} {YES} {S.NANU_VUTTAM} {SUTTA_SUN} {S.ATTHEVA} {YES} {S.tena_hi(T_SUN)}",
        S.katha_end(KATHA[2]))

    # ---- (188) 3. Sāmaññaphalakathā -----------------------------------------------------------------------------
    sub(3, 188)
    add("5-835", block(a(SPH), a(SPH)))
    add("5-836",
        f"{Q(a(SPH))} {YES} {Q(a(SAM))} {NO_PE} {q(s(SAM))} {YES} {Q(s(SPH))} {NO_PE}",
        f"{Q(a(SO_P))} {YES} {Q(a(SO_M))} {NO_PE} {q(s(SO_M))} {YES} {Q(s(SO_P))} {NO_PE}",
        f"Có phải {SA_P}{PE} {AN_P}{PE} {a(AR_P)} không? {YES} {Q(a(AR_M))} {NO_PE} {q(s(AR_M))} {YES} "
        f"{Q(s(AR_P))} {NO_PE}",
        count_tail(f"{a(SO_P)}, {SA_P}{PE} {AN_P}{PE} {a(AR_P)}, {a(NIB)}", "năm"),
        S.katha_end(KATHA[3]))

    # ---- (189) 4. Pattikathā ------------------------------------------------------------------------------------
    sub(4, 189)
    add("5-837", block(a(PATTI), a(PATTI)))
    l1 = (block(a(pt(REQ[0])), a(pt(REQ[0])), nib=NIB_PE) + " "
          + block(f"{pt(REQ[1])}{PE} {REQ[2]}{PE} {a(REQ[3])}", a(pt(REQ[3])), nib=NIB_PE2, lower=True))
    add("5-838",
        l1,
        count_tail(f"{a(pt(REQ[0]))}{PE} {REQ[1]}{PE} {REQ[2]}{PE} {a(pt(REQ[3]))}, {a(NIB)}", "năm"))
    first = f"{a(pt(JH[0]))} {EVAM} " + f"{PE} ".join(JH[1:-1]) + f"{PE} {a(pt(JH[-1]))}"
    add("5-839",
        block(first, a(pt(JH[-1])), nib=NIB_PE2),
        count_tail(f"{PE} ".join(a(pt(x)) for x in (SO_M, SO_P, AR_M, AR_P)) + f"{PE} {a(NIB)}", "chín"))
    add("5-840",
        f"{S.na_vattabbam(a(PATTI))} {YES} {Q(f'{PATTI} là {AGG5}')} {NO} {S.tena_hi(a(PATTI))}",
        S.katha_end(KATHA[4]))

    # ---- (190) 5. Tathatākathā ----------------------------------------------------------------------------------
    sub(5, 190)
    add("5-841", block(a(TATH), a(TATH), nib=NIB_PE))
    R = f"{ta('vật chất')} của vật chất, chẳng phải {ta('vật chất')}"   # Rūpassa rūpatā, nanu rūpatā
    V = f"{ta('thức')} của thức, chẳng phải {ta('thức')}"               # viññāṇassa viññāṇatā, nanu viññāṇatā
    MID = [f"{ta('cảm giác')} của cảm giác, chẳng phải {ta('cảm giác')}",
           f"{ta('tri giác')} của tri giác, chẳng phải {ta('tri giác')}",
           f"{ta('tạo tác')} của các tạo tác, chẳng phải {ta('tạo tác')}"]
    add("5-842",
        f"{cap(R)} {ASK} sao? {YES} {Q(NIB_PE)} {NO_PE} {R} {ASK}, {a(NIB)} sao? {YES} {Q(n_ask('hai'))} {NO_PE} "
        f"{q(n_ask('hai'))} {YES} {Q(refuges_pe('hai'))} {NO_PE}",
        f"{cap(MID[0])}{PE} {MID[1]}{PE} {MID[2]}{PE} {V} {ASK} sao? {YES} {Q(NIB_PE)} {NO_PE}",
        f"{cap(R)}{PE} {V} {ASK}, {a(NIB)} sao? {YES} {Q(n_ask('sáu'))} {NO_PE} {q(n_ask('sáu'))} {YES} "
        f"{Q(refuges_pe('sáu'))} {NO_PE}")
    add("5-843",
        f"{S.na_vattabbam(a(TATH))} {YES} {Q(f'{TATH} là {AGG5}')} {NO} {S.tena_hi(a(TATH))}",
        S.katha_end(KATHA[5]))

    # ---- (191) 6. Kusalakathā -----------------------------------------------------------------------------------
    sub(6, 191)
    add("5-844",
        f"{Q(NDH_K)} {YES} {Q(f'nó {SAR}, {AV}')} {NO_PE} {nanu_l(f'nó {ANR}, {AVN}')} {YES} "
        f"{S.hanci_neg(f'nó {ANR}, {AVN}', NDH_K)}")
    POS = f"là thiện, {SAR}, {AV}"
    NEG = f"là thiện, {ANR}, {AVN}"
    OTHERS = f"{ROOTS[1]} là thiện{PE} {ROOTS[2]} là thiện{PE} " + f"{PE} ".join(LIST5[:4]) + f"{PE} {LIST5[4]}"
    add("5-845",
        f"{Q(f'{ROOTS[0]} {POS}')} {YES} {Q(f'{NDH} {POS}')} {NO_PE} {q(f'{OTHERS} {POS}')} {YES} "
        f"{Q(f'{NDH} {POS}')} {NO_PE}",
        f"{Q(f'{NDH} {NEG}')} {YES} {Q(f'{ROOTS[0]} {NEG}')} {NO_PE} {q(f'{NDH} {NEG}')} {YES} "
        f"{Q(f'{OTHERS} {NEG}')} {NO_PE}")
    add("5-846",
        f"{S.na_vattabbam(NDH_K)} {YES} {NANU(f'{NDH} không có lỗi')} {YES} {S.hanci(f'{NDH} không có lỗi', NDH_K)}",
        S.katha_end(KATHA[6]))

    # ---- (192) 7. Accantaniyāmakathā ----------------------------------------------------------------------------
    sub(7, 192)
    add("5-847",
        f"{Q(T_ACC)} {YES} Có phải {KILLERS[0]} {FIXED}, {f'{PE} '.join(KILLERS[1:])} {FIXED} không? {NO_PE}")

    def path_lines(doubt, who):
        """^5-848 / 849 / 850: X uppajjeyyāti? … Pahīnāti? … Katamena maggenāti? …"""
        up = f"{doubt} có thể sinh khởi nơi {who}"
        nup = f"{doubt} không thể sinh khởi nơi {who}"
        l1 = f"{Q(up)} {YES} {S.hanci_neg(up, T_ACC)}"
        l2 = (f"{Q(nup)} {YES} {Q('nó đã được dứt bỏ')} {NO_PE} {q('nó đã được dứt bỏ')} {YES} "
              f"{Q(f'bằng {SO_M}')} {NO_PE} có phải bằng {SA_M}{PE} {AN_M}{PE} {AR_M} không? {NO_PE}")
        return l1, l2, f"{doubt} nơi {who} đã được dứt bỏ bằng {AKM}"

    KAT = f"Bằng con đường nào? Bằng {AKM}."                           # Katamena maggenāti? Akusalena maggena(ti).
    l1, l2, quoted = path_lines(VIC, ACCP)
    add("5-848",
        f"{Q(T_ACC)} {YES} {l1}",
        l2,
        f"{KAT} {Q(f'{AKM} {NIY_POS}')} {NO_PE} {nanu_l(f'{AKM} {NIY_NEG}')} {YES} "
        f"{S.hanci_neg(f'{AKM} {NIY_NEG}', quoted)}")
    for i, (d1, d2) in (("5-849", (UD, SD)), ("5-850", (SD, UD))):
        l1, l2, quoted = path_lines(d1, f"người cố định theo {d2}")
        add(i, l1, l2, f"{KAT} {cap(AKM)}{PE} thì {RE}, chắc chắn không nên nói – “{quoted}”.")
    add("5-851",
        f"{S.na_vattabbam(T_ACC)} {YES} {S.NANU_VUTTAM} “{NIM} {S.var(A715, 'evaṃ kho bhikkhave puggalo')[1:]} "
        f"{SAKIM}” [{A715}]! {S.ATTHEVA} {YES} {S.tena_hi(T_ACC)}")
    KV = f"vì cho rằng {S.VUTTAM} {SUT_NIM}"
    add("5-852",
        f"{S.katva(f'{S.VUTTAM} {SUT_NIM}', T_ACC)} {YES} {S.VUTTAM} “Ở đời này, này các tỳ-khưu, có người {UM1}” "
        f"[{A715}]! {S.ATTHEVA} {YES} {Q(f'vào mọi lúc đều {UM1}')} {NO_PE}",
        f"Có phải {KV} – và vì lý do ấy, {T_ACC} không? {YES} {S.VUTTAM} “Ở đời này, này các tỳ-khưu, có người {UM2}” "
        f"[{A715}]! {S.ATTHEVA} {YES} {Q(f'vào mọi lúc đều {UM_END}')} {NO_PE}",
        S.katha_end(KATHA[7]))

    # ---- (193) 8. Indriyakathā ----------------------------------------------------------------------------------
    sub(8, 193)
    F3 = f"{PE} ".join(IND[k] for k in ("sati", "samādhi", "paññā"))   # satindriyaṃ…pe… paññindriyaṃ
    P3 = f"{PE} ".join(PL[k] for k in ("sati", "samādhi", "paññā"))     # sati…pe… paññā
    add("5-853",
        f"{Q(ex('saddhā', faculty=True, neg=True))} {YES} {Q(ex('saddhā', neg=True))} {NO_PE} "
        f"có phải {IND['vīriya']} {LW}{PE} {F3} {NEX} không? {YES} "
        f"{Q(ex('paññā', neg=True))} {NO_PE}",
        f"{Q(ex('saddhā'))} {YES} {Q(ex('saddhā', faculty=True))} {NO_PE} "
        f"có phải {PL['vīriya']} {LW}{PE} {P3} {EX} không? {YES} "
        f"{Q(ex('paññā', faculty=True))} {NO_PE}",
        f"{Q(pair('mano'))} {YES} {Q(pair('saddhā'))} {NO_PE} {q(pair('mano'))} {YES} {Q(pair('paññā'))} {NO_PE}",
        f"Có phải {pair('somanassa')}{PE} {pair('jīvita')} không? {YES} {Q(pair('saddhā'))} {NO_PE} "
        f"{q(pair('jīvita'))} {YES} {Q(pair('paññā'))} {NO_PE}")
    add("5-854",
        f"{Q(pair('saddhā', neg2=True))} {YES} {Q(pair('mano', neg2=True))} {NO_PE} {q(pair('paññā', neg2=True))} "
        f"{YES} {Q(pair('mano', neg2=True))} {NO_PE}",
        f"{Q(pair('saddhā', neg2=True))} {YES} Có phải {pair('somanassa', neg2=True)}{PE} "
        f"{pair('jīvita', neg2=True)} không? {NO_PE} {q(pair('paññā', neg2=True))} {YES} "
        f"Có phải {pair('mano', neg2=True)}{PE} {pair('jīvita', neg2=True)} không? {NO_PE}")
    add("5-855",
        f"{Q(pair('saddhā', LU))} {YES} {Q(pair('saddhā'))} {NO_PE} có phải {ex('vīriya', LU)}{PE} "
        f"{pair('paññā', LU)} không? {YES} {Q(pair('paññā'))} {NO_PE}",
        f"{Q(pair('saddhā', neg2=True))} {YES} {Q(pair('saddhā', LU, neg2=True))} {NO_PE} có phải "
        f"{ex('vīriya')}{PE} {pair('paññā', neg2=True)} không? {YES} {Q(pair('paññā', LU, neg2=True))} {NO_PE}")
    add("5-856",
        f"{Q(f'{PANCA} {NEX}')} {YES} {S.NANU_VUTTAM} {SUT_IND} {S.ATTHEVA} {YES} {S.tena_hi(f'{PANCA} {EX}')}",
        S.katha_end(KATHA[8]),
        f"{VAGGA}.",
        TASSUDDANAM,
        UDDANA)
    return segs


def termbase():
    tb = {}
    for ln in TB.read_text(encoding="utf-8").splitlines():
        if ": {" in ln:
            tb[ln.split(": {", 1)[0]] = ln
    return tb


def tb_chapter():
    tb = termbase()
    tbl = {k.lower(): v for k, v in tb.items()}
    seen = set()
    for line in KW.read_text(encoding="utf-8").splitlines():
        if not line.strip() or "] " not in line:
            continue
        i, body = line.split("] ", 1)
        i = i[1:]
        m = re.fullmatch(r"5-(\d+)", i)
        if not (i.startswith("5-27-") or (m and 828 <= int(m.group(1)) <= 856)):
            continue
        for k in body.split(", "):
            for kk in k.split(" / "):
                if kk.lower() in seen:
                    continue
                seen.add(kk.lower())
                e = tb.get(kk) or tbl.get(kk.lower())
                print(f"[{i}] {e if e else kk + ': <NOT IN TERMBASE>'}")


def find(pat, mx=4, mc=700):
    pdir = ROOT / "AI_translation/pali/pi-5_split_chapters"
    rx, h = re.compile(pat), 0
    for n in FINISHED:
        pl = [x for x in (pdir / n).read_text(encoding="utf-8").splitlines() if x.strip()]
        vl = [x for x in (S.OUT_DIR / n).read_text(encoding="utf-8").splitlines() if x.strip()]
        for i, ln in enumerate(pl):
            m = rx.search(ln)
            if m:
                s_ = max(0, m.start() - 100)
                print(f"[{n} line {i + 1}]\n  PI: {ln[s_:s_ + 400]}\n  VI: {vl[i][:mc]}")
                h += 1
                if h >= mx:
                    return


def main():
    check_strings()
    S.check_reused()
    segs = build()
    S.check_against_pali(NAME, segs)
    text = unicodedata.normalize("NFC", "\n\n".join("\n".join(x) for x in segs) + "\n")
    assert "\n\n\n" not in text and "\r" not in text
    (S.OUT_DIR / NAME).write_text(text, encoding="utf-8", newline="\n")
    print("wrote", S.OUT_DIR / NAME)
    adh = S.FORMULAS_MD.parent / "adh-27"           # byte-identical copy for termbase_adherence_vi.py
    adh.mkdir(exist_ok=True)
    (adh / NAME).write_text(text, encoding="utf-8", newline="\n")
    print("wrote", adh / NAME)


if __name__ == "__main__":
    a_ = sys.argv[1:]
    if a_[:1] == ["--find"]:
        find(a_[1], int(a_[2]) if len(a_) > 2 else 4, int(a_[3]) if len(a_) > 3 else 700)
    elif a_[:1] == ["--tb"]:
        tb_chapter()
    elif a_[:1] == ["--word"]:
        rx_ = re.compile(a_[1], re.I)
        for h_, ln_ in termbase().items():
            if rx_.search(h_):
                print(ln_)
    else:
        main()
