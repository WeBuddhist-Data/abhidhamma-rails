"""pi-5 Kathāvatthu, Vietnamese RAILS (plain audience): chapter 23, Pannarasamavaggo (^5-23-0 … ^5-742): eleven
kathās (145-155) with the repeated "Pannarasamavaggo" sub-headings, the vagga close, the uddāna and the third
fifty-group close (Tatiyo paṇṇāsako. / Tassuddānaṃ – / its uddāna; frame set in ch13, the Tassuddānaṃ rule of ch18).

Builds AI_translation/vietnamese/pi-5-vietnamese-plain-rails_split_chapters/23-pannarasamavaggo.md from the fixed
strings below, importing the approved sample builder READ-ONLY (frames Q, q, NANU, hanci, hanci_neg, na_vattabbam,
tena_hi, tena_hi_na, katha, katha_end, var_sp …). Strings taken from pi-1 … pi-4 rails are asserted there (REUSED23);
strings shared with the finished pi-5 rails chapters are asserted in those chapter files (SHARED).
The per-line dash / quote / NFC / id checks of S.check_against_pali run before writing.
New recurring strings: notes-rails-23.md.

usage: python -I -X utf8 -B build_rails_23_vi.py          (writes the chapter and the adherence copy rails\\adh-23\\)
       python -I -X utf8 -B build_rails_23_vi.py --find <regex> [max] [chars]   (look up finished pi-5 rails chapters)
"""
import pathlib
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai\rails")
import build_rails_sample_vi as S  # noqa: E402

NAME = "23-pannarasamavaggo.md"
Q, q, NANU, PE, YES, NO, NO_PE = S.Q, S.q, S.NANU, S.PE, S.YES, S.NO, S.NO_PE
cap, RE, CIT = S.cap, S.RE, S.CIT
ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
FINISHED = ["1-puggalakatha.md", "2-parihanikatha.md", "3-brahmacariyakatha.md", "4-jahatikatha.md",
            "5-sabbamatthitikatha.md", "6-atitakkhandhadikatha.md", "7-ekaccam-atthitikatha.md",
            "8-satipatthanakatha.md", "9-hevatthikatha.md", "10-dutiyavaggo.md", "11-tatiyavaggo.md",
            "12-catutthavaggo.md", "13-pancamavaggo.md", "14-chatthavaggo.md", "15-sattamavaggo.md",
            "16-atthamavaggo.md", "17-navamavaggo.md", "18-dasamavaggo.md"]


def nanu_l(x):                      # nanu Xti? (after …pe…, lower case; ch15)
    return f"chẳng phải {x} sao?"


# ---------------------------------------------------------------------------------------------------------------
# Shared vocabulary (termbase; pi-1 … pi-4; finished pi-5 chapters)
# ---------------------------------------------------------------------------------------------------------------
BH = "Này các tỳ-khưu"                                                  # bhikkhave (sample)
NO_HAVE = "Không có."                                                   # Natthi. (ch12, ch14)
ATTH_L = "có bài kinh như vậy thật không?"                              # "…"ti – attheva suttantoti? (ch14)
MAGGO = ("Có phải đó là con đường, thành quả, Niết-bàn, con đường vào dòng, thành quả vào dòng" + PE
         + " chi phần giác ngộ không?")                                 # Maggo phalaṃ nibbānaṃ, … bojjhaṅgoti? (ch11)
LW, LU = "thuộc thế gian", "vượt thế gian"                              # lokiya / lokuttara (termbase, ch10)
ANAS = "không phải là đối tượng của ô nhiễm"                            # anāsava (termbase, ch12)
SAS = "là đối tượng của ô nhiễm"                                        # sāsava (termbase, ch11)
FIVE = f"có phải đó là cảm giác{PE} tri giác{PE} các tạo tác{PE} thức không?"
#   vedanā…pe… saññā…pe… saṅkhārā…pe… viññāṇanti? (also with plain "…"); bare predicate «đó là» (ch11, ch18)
RUPA = Q("đó là vật chất")                                              # Rūpanti?
LIST5 = ["niềm tin", "sự tinh tấn", "sự tỉnh thức", "sự định tâm", "trí tuệ"]   # saddhā … paññā (ch17)
SPV = ", ".join(LIST5)
P5 = ["sự tiếp xúc", "cảm giác", "tri giác", "chủ ý", "tâm"]           # phasso vedanā saññā cetanā cittaṃ (ch17)

# ---------------------------------------------------------------------------------------------------------------
# Headings, kathā names, vagga close, fifty-group close
# ---------------------------------------------------------------------------------------------------------------
VAGGA = "Chương thứ mười lăm"                                           # Pannarasamavaggo (termbase)
KATHA = {1: "tính chất làm điều kiện", 2: "điều kiện lẫn nhau", 3: "thời gian",
         4: "khoảnh khắc, chốc lát và thời khắc", 5: "ô nhiễm", 6: "sự lão hóa và sự chết",
         7: "tri giác và cảm giác", 8: "lần thứ hai về tri giác và cảm giác",
         9: "lần thứ ba về tri giác và cảm giác", 10: "việc hướng đến cõi chúng sinh Vô Tưởng",
         11: "sự tích lũy nghiệp"}
#   Paccayatā- (termbase paccayatā), Aññamaññapaccaya- (termbase heading), Addhā-, Khaṇalayamuhutta- (termbase khaṇa,
#   laya, muhutta), Āsava-, Jarāmaraṇa-, Saññāvedayita- / Dutiya- / Tatiyasaññāvedayitakathā (termbase headings «Bàn
#   (lần thứ hai / ba) về tri giác và cảm giác»), Asaññasattupika- (termbase phrase), Kammūpacayakathā (termbase)


def heading_k(k):                   # «Bàn về X» / «Bàn lần thứ hai về X»
    x = KATHA[k]
    return f"Bàn {x}" if x.startswith("lần") else S.katha(x)


def end_k(k):                       # «Phần bàn về X đã hoàn tất.» / «Phần bàn lần thứ hai về X đã hoàn tất.»
    x = KATHA[k]
    return f"Phần bàn {x} đã hoàn tất." if x.startswith("lần") else S.katha_end(x)


TASSUDDANAM = "Tóm tắt của chương này –"                               # Tassuddānaṃ – (ch9; after the vagga close)
TATIYO = "Nhóm năm mươi thứ ba."                                        # Tatiyo paṇṇāsako. (ch13 frame)
TASS50 = "Tóm tắt của nhóm này –"                                       # Tassuddānaṃ – after a fifty-group close (ch18)

# ---- theses ---------------------------------------------------------------------------------------------------
T1 = "tính chất làm điều kiện được xác định riêng biệt"                 # paccayatā vavatthitā (termbase)
T3 = "thời gian được hình thành trọn vẹn"                               # addhā parinipphanno (termbase)
T4 = "thời khắc được hình thành trọn vẹn"                               # muhuttaṃ parinipphannaṃ
T5 = f"bốn ô nhiễm {ANAS}"                                              # cattāro āsavā anāsavā
T6 = f"sự lão hóa và sự chết của các hiện tượng {LU} là {LU}"            # lokuttarānaṃ dhammānaṃ jarāmaraṇaṃ lokuttaraṃ
NS = "thành tựu thiền chấm dứt tri giác và cảm giác"                    # saññāvedayitanirodhasamāpatti (termbase)
T7 = f"{NS} là {LU}"                                                    # … lokuttarā (termbase phrase)
T8 = f"{NS} {LW}"                                                       # … lokiyā
SN = "người đang nhập sự chấm dứt tri giác và cảm giác"                 # saññāvedayitanirodhaṃ samāpanno (termbase, ch10)
T9 = f"{SN} có thể qua đời"                                             # … kālaṃ kareyya (termbase kālaṃ kareyya)
T9N = f"{SN} không thể qua đời"                                         # … na kālaṃ kareyya
UPIKA = "hướng đến cõi chúng sinh Vô Tưởng"                             # asaññasattupikā (termbase)
T10 = f"{NS} {UPIKA}"                                                   # saññāvedayitanirodhasamāpatti asaññasattupikā
KU = "sự tích lũy nghiệp"                                               # kammūpacayo (termbase)
T11 = S.anna("nghiệp", KU)                                              # aññaṃ kammaṃ añño kammūpacayo (sample frame)

UDDANA = (f"{cap(T1)}, sự sinh khởi tùy thuộc vào điều kiện, {KATHA[3]}, {KATHA[4]}, {T5}, {T6}, {T7}, {T8}, {T9}, "
          f"chính con đường ấy hướng đến sự tái sinh vào cõi chúng sinh Vô Tưởng, {T11}.")
#   Paccayatā vavatthitā, paṭiccasamuppādo (termbase), addhā, khaṇo layo muhuttaṃ, …, sveva maggo
#   asaññasattupapattiyā, aññaṃ kammaṃ añño kammūpacayoti.
UDD50 = "Các khuynh hướng tiềm ẩn, sự thu thúc, kiếp, gốc rễ, và được xác định riêng biệt."
#   Anusayā (ch19 Tissopi anusayakathā; termbase anusaya), saṃvaro (ch20 Saṃvaro kammantikathā; APPROVED «sự thu
#   thúc»), kappo (ch21 Kappaṭṭhakathā; termbase «kiếp»), mūlañca (ch22; termbase mūla «gốc rễ»), vavatthitāti (here)

# ---- conditions (paccaya; termbase / APPROVED) ----------------------------------------------------------------
PC = {"hetu": "điều kiện gốc rễ", "adhipati": "điều kiện chủ đạo", "sahajāta": "điều kiện cùng sinh",
      "indriya": "điều kiện năng lực", "magga": "điều kiện con đường", "āhāra": "điều kiện dưỡng chất",
      "ārammaṇa": "điều kiện đối tượng", "anantara": "điều kiện kế cận", "āsevana": "điều kiện thực hành",
      "samanantara": "điều kiện kế cận liền ngay"}


def pp(*names):                     # X-paccayena paccayo, Y-paccayena paccayo
    return ", ".join(f"làm điều kiện bằng {PC[n]}" for n in names)


SAHA = "các hiện tượng cùng sinh"                                       # sahajātānaṃ dhammānaṃ (termbase)
ADH = {"chanda": "ý muốn chủ đạo", "vīriya": "tinh tấn chủ đạo", "citta": "tâm chủ đạo",
       "vīmaṃsā": "sự thẩm xét chủ đạo"}
#   chanda- / vīriya- / citta- / vīmaṃsādhipati (termbase phrases «… chi phối», aligned to APPROVED adhipati
#   «yếu tố chủ đạo»: see notes)


def dom(x, extra=""):               # X-ādhipati sahajātānaṃ dhammānaṃ adhipati(, tañca Y)
    return f"{ADH[x]} là yếu tố chủ đạo đối với {SAHA}" + (f", và nó là {extra}" if extra else "")


def nanu_h(p, *names):              # Nanu P? Āmantā. Hañci P, tena vata re vattabbe – "…"ti.
    return f"{NANU(p)} {YES} {S.hanci(p, pp(*names))}"


# ---- dependent origination (pi-2 6-paticcasamuppadavibhango) -----------------------------------------------------
AV_S = "vô minh làm điều kiện cho các sự tạo tác"                       # avijjāpaccayā saṅkhārā (pi-2)
AV_ONLY = "chỉ có vô minh làm điều kiện cho các sự tạo tác"             # avijjāpaccayāva saṅkhārā
S_AV = "sự tạo tác cũng làm điều kiện cho vô minh"                      # saṅkhārapaccayāpi avijjā (pi-2)
AV_S_API = "vô minh cũng làm điều kiện cho các sự tạo tác"              # avijjāpaccayāpi saṅkhārā
TA_U = "khao khát làm điều kiện cho sự bám víu"                         # taṇhāpaccayā upādānaṃ (pi-2)
TA_ONLY = f"chỉ có {TA_U}"                                              # taṇhāpaccayāva upādānaṃ
U_TA = "sự bám víu cũng làm điều kiện cho khao khát"                    # upādānapaccayāpi taṇhā (pi-2)
TA_U_API = "khao khát cũng làm điều kiện cho sự bám víu"                # taṇhāpaccayāpi upādānaṃ
VN = ("thức làm điều kiện cho phần tinh thần và vật chất, phần tinh thần và vật chất cũng làm điều kiện cho "
      "thức")                                                           # viññāṇapaccayā … nāmarūpapaccayāpi viññāṇaṃ (pi-2)
JM = "sự lão hóa và sự chết làm điều kiện cho sự sinh, sự sinh làm điều kiện cho sự hiện hữu"
#   jarāmaraṇapaccayā … jāti, jātipaccayā bhavo (pi-2 pieces, reversed as written)

# ---- the three-topics sutta (a. ni. 3.68) ----------------------------------------------------------------------
TOPICS = (f"“{BH}, có ba chủ đề bàn luận này! Ba chủ đề nào? "
          f"{BH}, hoặc người ta có thể lấy thời gian quá khứ làm đối tượng mà bàn luận – ‘thời gian quá khứ đã là như "
          f"vậy’; {BH.lower()}, hoặc người ta có thể lấy thời gian tương lai làm đối tượng mà bàn luận – ‘thời gian "
          f"tương lai sẽ là như vậy’; {BH.lower()}, hoặc người ta có thể lấy thời gian hiện tại bây giờ làm đối tượng mà "
          f"bàn luận – ‘bây giờ, hiện tại là như vậy’. {BH}, đây là ba chủ đề bàn luận”")
#   tīṇimāni, bhikkhave, kathāvatthūni! Katamāni tīṇi? Atītaṃ vā, bhikkhave, addhānaṃ ārabbha kathaṃ katheyya –
#   ‘evaṃ ahosi atītamaddhāna’nti; … Imāni kho, bhikkhave, tīṇi kathāvatthūnī"ti (frame of ch11 «có ba loại mắt này!
#   Ba loại mắt nào? … đây là ba loại mắt»; ārabbha termbase «lấy … làm đối tượng»)

# ---- the Puṇṇa sutta (ma. ni. 2.81) ----------------------------------------------------------------------------
PUNNA = "Phú-lâu-na"                                                    # Puṇṇa (not in the termbase; see notes)
SA = "vừa gây hại vừa không gây hại"                                    # sabyābajjhampi abyābajjhampi (termbase)
KS, VS, MS = "sự tạo tác bằng thân", "sự tạo tác bằng lời nói", "sự tạo tác bằng ý"   # kāya- / vacī- / manosaṅkhāraṃ
VAR_P = (S.var_sp("Ka.", "sabyāpajjhampi abyāpajjhampi")[:-1] + f"; {CIT['ma. ni.']} 2.81, cần xem]")
#   [sabyāpajjhampi abyāpajjhampi (ka.) ma. ni. 2.81 passitabbaṃ] (ch17 «…, cần xem» for passitabbaṃ)
PUNNA_SUT = (f"“Ở đây, này {PUNNA}, có người tạo tác {KS} {SA}{VAR_P}, tạo tác {VS} {SA}{PE} {MS}; người ấy, "
             f"sau khi tạo tác {KS} {SA}, sau khi tạo tác {VS} {SA}{PE} {MS}, tái sinh vào thế gian {SA}. "
             f"Khi người ấy đã tái sinh vào thế gian {SA}, những sự tiếp xúc {SA} chạm đến người ấy. "
             f"Khi bị những sự tiếp xúc {SA} chạm đến, người ấy cảm nhận cảm giác {SA}, có sự dễ chịu và sự khó chịu "
             f"xen lẫn, ví như loài người, một số chư thiên và một số chúng sinh ở cõi đọa lạc. "
             f"Như vậy, này {PUNNA}, sự tái sinh của một sinh thể là do chính sinh thể ấy: người ta làm điều gì thì do "
             f"điều ấy mà tái sinh; khi người ấy đã tái sinh, những sự tiếp xúc chạm đến người ấy. "
             f"Này {PUNNA}, cũng như vậy, Ta nói ‘chúng sinh là người thừa kế của nghiệp’”")
#   idha, puṇṇa, ekacco sabyābajjhampi abyābajjhampi kāyasaṅkhāraṃ abhisaṅkharoti, … vokiṇṇasukhadukkhaṃ, seyyathāpi
#   manussā ekacce ca devā ekacce ca vinipātikā. Iti kho, puṇṇa, bhūtā bhūtassa upapatti hoti, yaṃ karoti tena
#   upapajjati, upapannametaṃ phassā phusanti. Evampāhaṃ, puṇṇa, ‘kammadāyādā sattā’ti vadāmī"ti

REUSED23 = [  # (Pāli, Vietnamese, book)
    ("Avijjāpaccayā saṅkhārā", AV_S, "2"),
    ("saṅkhārapaccayāpi avijjā", S_AV, "2"),
    ("taṇhāpaccayā upādānaṃ, upādānapaccayāpi taṇhā", f"{TA_U}, {U_TA}", "2"),
    ("viññāṇapaccayā nāmarūpaṃ, nāmarūpapaccayāpi viññāṇaṃ", VN, "2"),
    ("jātipaccayā", "sự sinh làm điều kiện cho", "2"), ("bhavapaccayā jāti", "sự hiện hữu làm điều kiện cho sự sinh", "2"),
    ("jarāmaraṇaṃ", "sự lão hóa và sự chết", "2"),
    ("chandādhipateyyaṃ", "lấy ý muốn làm yếu tố chủ đạo", "1"),
    ("vīriyādhipateyyaṃ", "lấy tinh tấn làm yếu tố chủ đạo", "1"),
    ("maggaṅgaṃ", "chi phần của con đường", "1"),
    ("kiriyābyākatesu dhammesu", "hiện tượng không xác định về mặt đạo đức mang tính chức năng", "1"),
    ("moho akusalamūlaṃ", "sự si mê, tức gốc rễ bất thiện", "1"),
    ("apaccavekkhaṇā", "sự không xem xét lại", "1"),
    ("Arūpāvacarā paññā", "thuộc cõi không hình sắc", "2"),
    ("garuṃ katvā", "trân trọng", "4"),
]

SHARED = [  # (Pāli, Vietnamese, finished pi-5 rails chapter)
    ("Tassuddānaṃ –", TASSUDDANAM, "9-hevatthikatha.md"),
    ("Tassuddānaṃ – (after Dutiyo paṇṇāsako.)", TASS50, "18-dasamavaggo.md"),
    ("Dutiyo paṇṇāsako.", "Nhóm năm mươi thứ hai.", "18-dasamavaggo.md"),
    ("Maggo phalaṃ nibbānaṃ, sotāpattimaggo sotāpattiphalaṃ…pe… bojjhaṅgoti?", MAGGO, "11-tatiyavaggo.md"),
    ("anāsavanti", ANAS, "12-catutthavaggo.md"),
    ("sāsavaṃ", SAS, "11-tatiyavaggo.md"),
    ("rāgasahajātaṃ", "cùng sinh với tham đắm", "11-tatiyavaggo.md"),
    ("lokiya / lokuttara", "tầng thiền thứ nhất vượt thế gian", "10-dutiyavaggo.md"),
    ("lokiya", f"tầng thiền thứ nhất {LW}", "10-dutiyavaggo.md"),
    ("saññāvedayitanirodhaṃ samāpannassa", SN, "10-dutiyavaggo.md"),
    ("arahattamaggo arahattaphalaṃ, satipaṭṭhānaṃ … bojjhaṅgo",
     "con đường A-la-hán, thành quả A-la-hán, sự thiết lập tỉnh thức, nỗ lực đúng đắn, nền tảng thần thông, năng lực, "
     "sức mạnh, chi phần giác ngộ", "10-dutiyavaggo.md"),
    ("satipaṭṭhānā…pe… sammappadhānā… iddhipādā… indriyā… balā… bojjhaṅgā",
     "các sự thiết lập tỉnh thức… đã tu tập các nỗ lực đúng đắn… đã tu tập các nền tảng thần thông… đã tu tập các năng "
     "lực… đã tu tập các sức mạnh… đã tu tập các chi phần giác ngộ", "2-parihanikatha.md"),
    ('"…"nti – attheva suttantoti? Natthi.', f"” – {ATTH_L} {NO_HAVE}", "14-chatthavaggo.md"),
    ("[… thokaṃ pana visadisaṃ]", ", nhưng hơi khác một chút]", "16-atthamavaggo.md"),
    ("[… passitabbaṃ]", ", cần xem]", "17-navamavaggo.md"),
    ("dī. ni.", "Trường Bộ Kinh", "8-satipatthanakatha.md"),
    ("Nanu vuttaṃ bhagavatā – \"idha, kevaṭṭa,", "Chẳng phải Đức Thế Tôn đã nói thế này sao – “Ở đây, này",
     "15-sattamavaggo.md"),
    ("tīṇimāni, bhikkhave, cakkhūni! Katamāni tīṇi?", "Này các tỳ-khưu, có ba loại mắt này! Ba loại mắt nào?",
     "11-tatiyavaggo.md"),
    ("…ti, āmantā.", "không, đúng vậy.", "5-sabbamatthitikatha.md"),
    ("saññā cetanā cittaṃ saddhā vīriyaṃ sati samādhi paññā rāgo",
     "tri giác, chủ ý, tâm, niềm tin, sự tinh tấn, sự tỉnh thức, sự định tâm, trí tuệ, sự tham đắm", "17-navamavaggo.md"),
    ("anottappaṃ", "sự không biết ghê sợ tội lỗi", "17-navamavaggo.md"),
    ("Kālaṃ karoti", "qua đời", "3-brahmacariyakatha.md"),
]


def check_strings():
    texts = {b: unicodedata.normalize("NFC", "\n".join(p.read_text(encoding="utf-8")
                                                       for p in sorted(d.glob("*.md")))).lower()
             for b, d in S.RAILS.items()}
    bad = [(p, v, b) for p, v, b in REUSED23 if unicodedata.normalize("NFC", v).lower() not in texts[b]]
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

    def sub(k, n):                  # #### Pannarasamavaggo / ##### (n) k. X-kathā
        heading(f"5-23-{k}-0", 4, VAGGA)
        heading(f"5-23-{k}-1-0", 5, f"({n}) {k}. {heading_k(k)}")

    heading("5-23-0", 3, VAGGA)

    # ---- (145) 1. Paccayatākathā ----------------------------------------------------------------------------------
    heading("5-23-1-0", 4, f"(145) 1. {heading_k(1)}")
    VH = "sự thẩm xét là gốc rễ, và nó là yếu tố chủ đạo"               # vīmaṃsā hetu, so ca adhipati
    add("5-711",
        f"{Q(T1)} {YES} {nanu_h(VH, 'hetu', 'adhipati')}",
        nanu_h(dom("chanda"), "adhipati", "sahajāta"))
    add("5-712",
        nanu_h(dom("vīriya"), "adhipati", "sahajāta"),
        nanu_h(dom("vīriya", "năng lực"), "adhipati", "indriya"),
        nanu_h(dom("vīriya", "chi phần của con đường"), "adhipati", "magga"))
    add("5-713",
        nanu_h(dom("citta"), "adhipati", "sahajāta"),
        nanu_h(dom("citta", "dưỡng chất"), "adhipati", "āhāra"),
        nanu_h(dom("citta", "năng lực"), "adhipati", "indriya"))
    add("5-714",
        nanu_h(dom("vīmaṃsā"), "adhipati", "sahajāta"),
        nanu_h(dom("vīmaṃsā", "năng lực"), "adhipati", "indriya"),
        nanu_h(dom("vīmaṃsā", "chi phần của con đường"), "adhipati", "magga"))
    add("5-715",
        nanu_h("sự xem xét lại sinh khởi sau khi lấy hiện tượng cao quý làm điều trân trọng, và nó là đối tượng",
               "adhipati", "ārammaṇa"))

    def seq(kind):                  # purimā purimā X dhammā pacchimānaṃ pacchimānaṃ X-ānaṃ dhammānaṃ anantara…, sā ca āsevanā
        return (f"các hiện tượng {kind} trước, trước nữa làm điều kiện bằng {PC['anantara']} cho các hiện tượng {kind} "
                f"sau, sau nữa, và nó là sự thực hành")

    KB = "không xác định về mặt đạo đức mang tính chức năng"            # kiriyābyākatā (termbase)
    add("5-716", *[nanu_h(seq(k), "anantara", "āsevana") for k in ("thiện", "bất thiện", KB)])
    add("5-717",
        f"{S.na_vattabbam(T1)} {YES} Có phải {pp('hetu', 'ārammaṇa', 'anantara', 'samanantara')} không? {NO} "
        f"{S.tena_hi(T1)}",
        end_k(1))

    # ---- (146) 2. Aññamaññapaccayakathā ---------------------------------------------------------------------------
    sub(2, 146)

    def only(a, b):                 # X-paccayāva Y, na vattabbaṃ – "Y-paccayāpi X"ti
        return f"{a}, không nên nói – “{b}”"

    add("5-718",
        f"Có phải {only(AV_ONLY, S_AV)} không? {YES} {NANU('vô minh cùng sinh với sự tạo tác')} {YES} "
        f"{S.hanci('vô minh cùng sinh với sự tạo tác', f'{AV_S_API}, {S_AV}')}",
        f"Có phải {only(TA_ONLY, U_TA)} không? {YES} {NANU('khao khát cùng sinh với sự bám víu')} {YES} "
        f"{S.hanci('khao khát cùng sinh với sự bám víu', f'{TA_U_API}, {U_TA}')}")
    add("5-719",
        f"“{BH}, {JM}” – {ATTH_L} {NO_HAVE} Vậy thì {only(AV_ONLY, S_AV)}. {cap(only(TA_ONLY, U_TA))}.",
        f"“{BH}, {VN}” [Trường Bộ Kinh 2.58, nhưng hơi khác một chút] – {ATTH_L} {YES} "
        f"Vậy thì {AV_S_API}, {S_AV}; {TA_U_API}, {U_TA}.",
        end_k(2))

    # ---- (147) 3. Addhākathā --------------------------------------------------------------------------------------
    sub(3, 147)
    TQ, TT, TH = "thời gian quá khứ", "thời gian tương lai", "thời gian hiện tại"   # atīto / anāgato / paccuppanno addhā

    def five(thesis, lower=False):  # X parinipphannoti? Āmantā. Rūpanti? Na hevaṃ vattabbe…pe… vedanā…pe… viññāṇanti?
        return f"{(q if lower else Q)(thesis)} {YES} {RUPA} {NO_PE} {FIVE} {NO_PE}"

    AG = ["vật chất", "cảm giác", "tri giác", "các tạo tác", "thức"]

    def agg(when, t):               # Atītaṃ rūpaṃ vedanā … viññāṇaṃ atīto addhāti?
        return f"{', '.join(AG)} thuộc {when} là {t}"

    def groups(n, what, total):     # Atītā X atīto addhā, anāgatā X anāgato addhā, paccuppannā X …? N addhāti?
        x = f"{n} {what}"
        return (f"{Q(f'{x} thuộc quá khứ là {TQ}, {x} thuộc tương lai là {TT}, {x} thuộc hiện tại là {TH}')} {YES} "
                f"{Q(f'có {total} thời gian')} {NO_PE}")

    add("5-720",
        " ".join([five(T3), five(f"{TQ} được hình thành trọn vẹn", True),
                  five(f"{TT} được hình thành trọn vẹn", True), five(f"{TH} được hình thành trọn vẹn", True)]),
        f"{Q(agg('quá khứ', TQ))} {YES} {Q(f'có năm {TQ}')} {NO_PE} {q(agg('tương lai', TT))} {YES} "
        f"{Q(f'có năm {TT}')} {NO_PE} {q(agg('hiện tại', TH))} {YES} {Q(f'có năm {TH}')} {NO_PE}",
        groups("năm", "khối", "mười lăm"),
        groups("mười hai", "lĩnh vực nhận biết", "ba mươi sáu"),
        groups("mười tám", "yếu tố", "năm mươi bốn"),
        groups("hai mươi hai", "năng lực", "sáu mươi sáu"))
    add("5-721",
        f"{S.na_vattabbam(T3)} {YES} {S.NANU_VUTTAM} {TOPICS} [{CIT['a. ni.']} 3.68; Trường Bộ Kinh 3.305]. "
        f"{S.ATTHEVA} {YES} {S.tena_hi(T3)}",
        end_k(3))

    # ---- (148) 4. Khaṇalayamuhuttakathā ---------------------------------------------------------------------------
    sub(4, 148)
    T4A = ("khoảnh khắc được hình thành trọn vẹn, chốc lát được hình thành trọn vẹn, thời khắc được hình thành trọn "
           "vẹn")                                                       # khaṇo … layo … muhuttaṃ parinipphannaṃ
    add("5-722", five(T4A))
    add("5-723",
        f"{S.na_vattabbam(T4)} {YES} {S.NANU_VUTTAM} {TOPICS}. {S.ATTHEVA} {YES} {S.tena_hi(T4)}",
        end_k(4))

    # ---- (149) 5. Āsavakathā --------------------------------------------------------------------------------------
    sub(5, 149)
    add("5-724", f"{Q(T5)} {YES} {MAGGO} {NO_PE}")
    OTHER = f"thật có những ô nhiễm khác, mà do những ô nhiễm ấy, các ô nhiễm kia {SAS}"
    #   atthaññeva āsavā yehi āsavehi te āsavā sāsavā honti (eva «thật», termbase)
    add("5-725", f"{S.na_vattabbam(T5)} {YES} {Q(OTHER)} {NO} {S.tena_hi(T5)}", end_k(5))

    # ---- (150) 6. Jarāmaraṇakathā ---------------------------------------------------------------------------------
    sub(6, 150)

    def jm(x, y):                   # X-assa jarāmaraṇaṃ Y
        return f"sự lão hóa và sự chết của {x} là {y}"

    SM, SP = "con đường vào dòng", "thành quả vào dòng"
    AM, AP = "con đường A-la-hán", "thành quả A-la-hán"
    MID = [f"của {x}" for x in ("con đường trở lại một lần", "thành quả trở lại một lần", "con đường không trở lại",
                                "thành quả không trở lại")]
    BOJ = [f"của {x}" for x in ("các sự thiết lập tỉnh thức", "các nỗ lực đúng đắn", "các nền tảng thần thông",
                                "các năng lực", "các sức mạnh")]
    add("5-726",
        f"{Q(T6)} {YES} {MAGGO} {NO_PE} {q(jm(SM, SM))} {NO_PE} {q(jm(SM, SM))} {YES} {Q(jm(SP, SP))} {NO_PE} "
        f"có phải sự lão hóa và sự chết {f'{PE} '.join(MID + [f'của {AM}'])} là {AM} không? {NO_PE} "
        f"{q(jm(AM, AM))} {YES} {Q(jm(AP, AP))} {NO_PE} "
        f"có phải sự lão hóa và sự chết {f'{PE} '.join(BOJ + ['của các chi phần giác ngộ'])} là chi phần giác ngộ "
        f"không? {NO_PE}")
    add("5-727",
        f"{S.na_vattabbam(T6)} {YES} {Q(f'nó {LW}')} {NO} {S.tena_hi(f'nó {LU}')}",
        end_k(6))

    # ---- (151) 7. Saññāvedayitakathā ------------------------------------------------------------------------------
    sub(7, 151)
    add("5-728", f"{Q(T7)} {YES} {MAGGO} {NO_PE}")
    add("5-729",
        f"{S.na_vattabbam(T7)} {YES} {Q(f'nó {LW}')} {NO} {S.tena_hi(f'nó {LU}')}",
        end_k(7))

    # ---- (152) 8. Dutiyasaññāvedayitakathā ------------------------------------------------------------------------
    sub(8, 152)
    SPH = ["cõi dục lạc", "cõi hình sắc", "cõi không hình sắc"]          # kāma- / rūpa- / arūpāvacarā (termbase)
    add("5-730",
        f"{five(T8)} " + " ".join(f"{q(f'nó thuộc {x}')} {NO_PE}" for x in SPH))
    add("5-731",
        f"{S.na_vattabbam(T8)} {YES} {Q(f'nó {LU}')} {NO} {S.tena_hi(f'nó {LW}')}",
        end_k(8))

    # ---- (153) 9. Tatiyasaññāvedayitakathā ------------------------------------------------------------------------
    sub(9, 153)
    MR = ", ".join(f"{x} lúc lâm chung" for x in P5)                    # māraṇantiyo phasso … māraṇantiyaṃ cittaṃ
    PV5 = ", ".join(P5)                                                 # phasso vedanā saññā cetanā cittaṃ
    WHO_N = ["người không có sự tiếp xúc", "người không có cảm giác"]   # aphassakassa, avedanakassa
    DEATH = "có sự qua đời"                                             # kālaṃ kiriyā (termbase kālaṃ kareyya «qua đời»)

    def seqd(pos_items, last, pred):  # A-assa P, B-assa P…pe… Z-assa P
        return f"{', '.join(f'{x} {pred}' for x in pos_items)}{PE} {last} {pred}" if pos_items[1:] else \
            f"{pos_items[0]} {pred}{PE} {last} {pred}"

    NEG_D = seqd(WHO_N, "người không có tâm", DEATH)
    POS_D = seqd(["người có sự tiếp xúc"], "người có tâm", DEATH)
    BODY = (f"chất độc có thể tác động vào thân của {SN}, dao kiếm có thể tác động, lửa có thể tác động")
    BODY_N = (f"chất độc không thể tác động vào thân của {SN}, dao kiếm không thể tác động, lửa không thể tác động")
    #   kāye visaṃ (na) kameyya, satthaṃ (na) kameyya, aggi (na) kameyya (termbase kameyya «tác động»)
    add("5-732",
        f"{Q(T9)} {YES} {Q(f'{SN} có {MR}')} {NO_PE} {q(f'{SN} không có {MR}')} {YES} "
        f"{S.hanci_neg(f'{SN} không có {MR}', T9)}",
        f"{Q(T9)} {YES} {Q(f'{SN} có {PV5}')} {NO_PE} {q(f'{SN} không có {PV5}')} {YES} {Q(NEG_D)} {NO_PE} "
        f"{nanu_l(POS_D)} {YES} {S.hanci_neg(POS_D, T9)}",
        f"{Q(T9)} {YES} {Q(BODY)} {NO_PE} {q(BODY_N)} {YES} {S.hanci_neg(BODY_N, T9)}",
        f"{Q(T9)} {YES} {Q(BODY)} {YES} {Q('người ấy không phải là người đang nhập sự chấm dứt')} {NO_PE}")

    def niy(x, neg=False):          # (n)atthi so niyāmo yena niyāmena niyato X na kālaṃ kareyya
        return f"{'không ' if neg else ''}có sự cố định ấy, mà bởi sự cố định ấy, {x} được cố định, không thể qua đời"

    add("5-733", f"{Q(T9N)} {YES} {Q(niy(SN))} {NO_HAVE} {S.hanci_neg(niy(SN, True), T9N)}")
    CV = "người có được thức qua mắt"                                   # cakkhuviññāṇasamaṅgī (termbase)
    CVN = f"{CV} không thể qua đời"
    add("5-734", f"{Q(CVN)} {YES} {Q(niy(CV))} {NO_HAVE} {S.hanci_neg(niy(CV, True), CVN)}", end_k(9))

    # ---- (154) 10. Asaññasattupikakathā ---------------------------------------------------------------------------
    sub(10, 154)
    ROOTS = ["sự không tham lam, tức gốc rễ thiện", "sự không sân hận, tức gốc rễ thiện",
             "sự không si mê, tức gốc rễ thiện"]                        # alobho kusalamūlaṃ … (pi-1 «…, tức gốc rễ …»)
    R_FULL = f"{', '.join(ROOTS)}, {SPV}"
    R_PE = f"{ROOTS[0]}, {ROOTS[1]}{PE} trí tuệ"
    MB = "có sự tu tập con đường"                                       # maggabhāvanā (ch18 «có sự tu tập con đường»)
    add("5-735",
        f"{Q(T10)} {YES} {Q(f'{SN} có {R_FULL}')} {NO_PE} {q(f'{SN} không có {R_PE}')} {YES} "
        f"{S.hanci_neg(f'{SN} không có {R_FULL}', T10)}",
        f"{Q(T10)} {YES} {Q(f'{SN} có {PV5}')} {NO_PE} {q(f'{SN} không có {PV5}')} {YES} "
        f"{Q(seqd(['người không có sự tiếp xúc'], 'người không có tâm', MB))} {NO_PE} "
        f"{nanu_l(seqd(['người có sự tiếp xúc'], 'người có tâm', MB))} {YES} "
        f"{S.hanci_neg(seqd(['người có sự tiếp xúc'], 'người có tâm', MB), T10)}",
        f"{Q(T10)} {YES} "
        f"{Q(f'bất cứ ai nhập sự chấm dứt tri giác và cảm giác, tất cả những người ấy đều {UPIKA}')} {NO_PE}")
    HERE = "ở đây cũng là người không có tri giác, ở đó cũng là người không có tri giác"   # idhāpi asaññī tatrāpi asaññī
    add("5-736",
        f"{S.na_vattabbam(T10)} {YES} {NANU(HERE)} {YES} {S.hanci(HERE, T10)}",
        end_k(10))

    # ---- (155) 11. Kammūpacayakathā -------------------------------------------------------------------------------
    sub(11, 155)
    PAIRS = [("sự tiếp xúc", "sự tích lũy sự tiếp xúc"), ("cảm giác", "sự tích lũy cảm giác"),
             ("tri giác", "sự tích lũy tri giác"), ("chủ ý", "sự tích lũy chủ ý"), ("tâm", "sự tích lũy tâm"),
             ("niềm tin", "sự tích lũy niềm tin"), ("sự tinh tấn", "sự tích lũy sự tinh tấn"),
             ("sự tỉnh thức", "sự tích lũy sự tỉnh thức"), ("sự định tâm", "sự tích lũy sự định tâm"),
             ("trí tuệ", "sự tích lũy trí tuệ"), ("sự tham đắm", "sự tích lũy sự tham đắm")]
    #   añño phasso, añño phassūpacayo; … añño rāgo, añño rāgūpacayo (termbase saññūpacayo «sự tích lũy tri giác»)
    LAST = S.anna("sự không biết ghê sợ tội lỗi", "sự tích lũy sự không biết ghê sợ tội lỗi")
    add("5-737",
        f"{Q(T11)} {YES} Có phải {'; '.join(S.anna(a, b) for a, b in PAIRS)}{PE} {LAST} không? {NO_PE}")
    KS1 = f"{KU} cùng sinh với nghiệp"                                  # kammūpacayo kammena sahajāto

    def kk(kind):                   # K-ena kammena sahajāto kammūpacayo K-o
        return f"{KU} cùng sinh với nghiệp {kind} là {kind}"

    def fe(v):                      # X-āya vedanāya sampayuttena kammena sahajāto kammūpacayo X-āya vedanāya sampayutto
        return f"{KU} cùng sinh với nghiệp gắn liền với cảm giác {v} thì gắn liền với cảm giác {v}"

    NEU = "không khó chịu cũng không dễ chịu"                           # adukkhamasukhā (termbase)
    FEEL = f"{Q(fe('dễ chịu'))} {NO_PE} cảm giác khó chịu{PE} {q(fe(NEU))} {NO_PE}"
    add("5-738",
        f"{Q(T11)} {YES} {Q(KS1)} {NO_PE}",
        f"Có phải {KS1} không, đúng vậy. Có phải {kk('thiện')} không, không nên nói như vậy…",
        f"{Q(kk('thiện'))} {YES} {FEEL}")
    add("5-739",
        f"{Q(KS1)} {YES} {Q(kk('bất thiện'))} {NO_PE}",
        f"{Q(kk('bất thiện'))} {YES} {FEEL}")

    def kc(x, pred):                # X cittena sahajātaṃ, X pred
        return f"{x} cùng sinh với tâm, {x} {pred}"

    def br(x, neg=False):           # X cittena sahajātaṃ, cittaṃ bhijjamānaṃ X (na) bhijjati
        return f"{x} cùng sinh với tâm, khi tâm đang tan rã thì {x} {'không ' if neg else ''}tan rã"

    SAR, ANR = "có đối tượng", "không có đối tượng"                     # sārammaṇa / anārammaṇa (termbase)
    add("5-740",
        f"{Q(kc('nghiệp', SAR))} {YES} {Q(kc(KU, SAR))} {NO_PE} {q(kc(KU, ANR))} {YES} {Q(kc('nghiệp', ANR))} {NO_PE}",
        f"{Q(br('nghiệp'))} {YES} {Q(br(KU))} {NO_PE}",
        f"{Q(br(KU, True))} {YES} {Q(br('nghiệp', True))} {NO_PE}")
    IN = f"{KU} ở trong nghiệp"                                         # kammamhi kammūpacayo
    VIP = f"{IN}, từ {KU} mà quả trổ phát sinh"                         # … kammūpacayato vipāko nibbattati
    add("5-741",
        f"{Q(IN)} {YES} {Q(f'chính nghiệp ấy là {KU} ấy')} {NO_PE}",
        f"{Q(VIP)} {YES} {Q(f'chính nghiệp ấy là {KU} ấy, là quả của nghiệp ấy')} {NO_PE}",
        f"{Q(f'{VIP}, quả trổ {SAR}')} {YES} {Q(f'{KU} {SAR}')} {NO_PE} {q(f'{KU} {ANR}')} {YES} "
        f"{Q(f'quả trổ {ANR}')} {NO_PE}")
    add("5-742",
        f"Có phải {T11} không, đúng vậy. {S.NANU_VUTTAM} {PUNNA_SUT} [{CIT['ma. ni.']} 2.81]. {S.ATTHEVA} {YES} "
        f"{S.tena_hi_na(T11)}",
        end_k(11),
        f"{VAGGA}.",
        TASSUDDANAM,
        UDDANA,
        TATIYO,
        TASS50,
        UDD50)
    return segs


def find(pat, mx=4, mc=700):
    pdir = ROOT / "AI_translation/pali/pi-5_split_chapters"
    vdir = ROOT / "AI_translation/vietnamese/pi-5-vietnamese-plain-rails_split_chapters"
    rx, h = re.compile(pat), 0
    for n in FINISHED:
        pl = [x for x in (pdir / n).read_text(encoding="utf-8").splitlines() if x.strip()]
        vl = [x for x in (vdir / n).read_text(encoding="utf-8").splitlines() if x.strip()]
        for i, ln in enumerate(pl):
            m = rx.search(ln)
            if m:
                s = max(0, m.start() - 100)
                print(f"[{n} line {i + 1}]\n  PI: {ln[s:s + 400]}\n  VI: {vl[i][:mc]}")
                h += 1
                if h >= mx:
                    return


def main():
    check_strings()
    S.check_reused()
    segs = build()
    S.check_against_pali(NAME, segs)
    text = unicodedata.normalize("NFC", "\n\n".join("\n".join(s) for s in segs) + "\n")
    assert "\n\n\n" not in text and "\r" not in text
    (S.OUT_DIR / NAME).write_text(text, encoding="utf-8", newline="\n")
    print("wrote", S.OUT_DIR / NAME)
    adh = S.FORMULAS_MD.parent / "adh-23"           # byte-identical copy for termbase_adherence_vi.py
    adh.mkdir(exist_ok=True)
    (adh / NAME).write_text(text, encoding="utf-8", newline="\n")
    print("wrote", adh / NAME)


if __name__ == "__main__":
    if sys.argv[1:2] == ["--find"]:
        a = sys.argv[2:]
        find(a[0], int(a[1]) if len(a) > 1 else 4, int(a[2]) if len(a) > 2 else 700)
    else:
        main()
