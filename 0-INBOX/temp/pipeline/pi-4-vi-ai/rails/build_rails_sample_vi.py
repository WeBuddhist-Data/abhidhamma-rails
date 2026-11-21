"""pi-4 Puggalapaññatti, Vietnamese RAILS (plain audience): SAMPLE builder.

Builds AI_translation/vietnamese/pi-4-vietnamese-plain-rails_split_chapters/
    preamble.md, 1-matika.md, 2-ekakapuggalapannatti.md
and 0-INBOX/temp/pipeline/pi-4-vi-ai/rails/vi-rails-formulas.md
from the fixed strings below. Chapter agents (ch3-11) import the constants:

    import sys; sys.path.insert(0, r"D:\\Work\\OpenPecha\\abhidhamma-rails\\0-INBOX\\temp\\pipeline\\pi-4-vi-ai\\rails")
    from build_rails_sample_vi import NAME, cap, q_katamo, close_dash, ...

Importing writes nothing (outputs only under __main__). At build time every string marked (pi-1) / (pi-2) / (pi-3)
is asserted to occur in that book's approved Vietnamese rails.
Termbase: AI_translation/vietnamese/pi-4-pali-vietnamese-termbase-plain.md (+ pi-4-vi-ai/termbase/APPROVED.md).
Style: 0-INBOX/temp/pipeline/vietnamese-style.md.

usage: python -I -X utf8 build_rails_sample_vi.py
"""
import pathlib
import sys
import unicodedata

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
OUT_DIR = ROOT / "AI_translation/vietnamese/pi-4-vietnamese-plain-rails_split_chapters"
FORMULAS_MD = ROOT / "0-INBOX/temp/pipeline/pi-4-vi-ai/rails/vi-rails-formulas.md"
RAILS = {b: ROOT / f"AI_translation/vietnamese/pi-{b}-vietnamese-plain-rails_split_chapters" for b in "123"}


def cap(s):
    """Capitalise the first letter (sentence start / matrix item)."""
    return s[:1].upper() + s[1:]


# ---------------------------------------------------------------------------------------------------------------
# Book frame and headings (user-approved 2026-11-20, verbatim)
# ---------------------------------------------------------------------------------------------------------------
HOMAGE = "Kính lễ Đức Thế Tôn, bậc A-la-hán, bậc Tự Giác Ngộ Hoàn Toàn"            # (pi-1)
H_ABHI = "# Tạng Vi Diệu Pháp"                                                    # (pi-1)
H_BOOK = "## Định danh các hạng người"
BOOK_TITLE = "Định danh các hạng người"           # mid-sentence: “Định danh các hạng người”
COLOPHON = "Bộ “Định danh các hạng người” đã hoàn tất."
H_MATIKA = "### Ma trận"                                                          # (pi-1)
H_NIDDESO = "### Phần giải thích"

NUM = {1: "một", 2: "hai", 3: "ba", 4: "bốn", 5: "năm", 6: "sáu", 7: "bảy", 8: "tám", 9: "chín", 10: "mười"}
GROUP_PALI = {1: "Ekaka", 2: "Duka", 3: "Tika", 4: "Catukka", 5: "Pañcaka", 6: "Chakka", 7: "Sattaka",
              8: "Aṭṭhaka", 9: "Navaka", 10: "Dasaka"}
H_UDDESO = {n: f"#### Phần nêu đề mục theo nhóm {NUM[n]}" for n in NUM}           # Ekakauddeso … Dasakauddeso
CLOSER_MATRIX = {n: f"Phân loại theo nhóm {NUM[n]}." for n in NUM}               # Ekakaṃ. … Dasakaṃ.
H_CHAPTER = {n: f"#### Định danh các hạng người theo nhóm {NUM[n]}" for n in NUM}  # Ekakapuggalapaññatti …
CLOSER_CHAPTER = {n: f"Giải thích phân loại theo nhóm {NUM[n]}." for n in NUM}    # Ekakaniddeso. …
GROUP_OPEN = {n: f"{cap(NUM[n])} hạng người –" for n in range(2, 11)}             # Dve puggalā – … Dasa puggalā –
MATIKA_END = "Ma trận của “Định danh các hạng người” đã hoàn tất."               # Puggalapaññattimātikā niṭṭhitā.

# ---------------------------------------------------------------------------------------------------------------
# Sentence frames (user-approved frames; the rest proposed here, binding for ch3-11)
# ---------------------------------------------------------------------------------------------------------------
IDHEKACCO = "Ở đời này, có người"          # Idhekacco puggalo
ATTHEKACCO = "có người"                    # Atthekacco puggalo (capitalise at line start)


def q_katamo(name):                        # Katamo ca puggalo X?
    return f"Thế nào là {name}?"


def close_dash(name):                      # – ayaṃ vuccati puggalo "X".
    return f"– người này được gọi là “{name}”."


def close_sentence(name):                  # Ayaṃ vuccati puggalo "X". (no dash in the Pāli)
    return f"Người này được gọi là “{name}”."


def close_dash_pl(name):                   # – ime vuccanti puggalā "X".
    return f"– những người này được gọi là “{name}”."


def q_kathanca(name):                      # Kathañca puggalo X hoti?
    return f"Người như thế nào là {name}?"


def evam(name):                            # Evaṃ puggalo X hoti.
    return f"Như vậy là {name}."


def kittavata(x):                          # Kittāvatā X-ānaṃ X-paññatti?
    return f"Sự định danh về {x} bao quát đến mức nào?"


def yavata_ettavata(x, listing):           # Yāvatā …; ettāvatā X-ānaṃ X-paññatti.
    return f"Bao quát {listing}; sự định danh về {x} bao quát đến mức ấy."


def ca_ca(a, b):                           # X ca, Y ca.
    return f"{cap(a)} và {b}."


# designations (matrix ^4-M-1 .. ^4-M-7)
DESIG = {"khandha": "các khối", "āyatana": "các lĩnh vực nhận biết", "dhātu": "các yếu tố",
         "sacca": "các sự thật", "indriya": "các năng lực", "puggala": "các hạng người"}
PANNATTI = {k: f"sự định danh về {v}" for k, v in DESIG.items()}                 # khandhapaññatti …

# lists (matrix ^4-M-2 .. ^4-M-6)
KHANDHA_LIST = "khối vật chất, khối cảm giác, khối tri giác, khối tạo tác, khối thức"            # (pi-2)
AYATANA_LIST = ("lĩnh vực mắt, lĩnh vực hình sắc, lĩnh vực tai, lĩnh vực âm thanh, lĩnh vực mũi, lĩnh vực mùi, "
                "lĩnh vực lưỡi, lĩnh vực vị, lĩnh vực thân, lĩnh vực vật xúc chạm, lĩnh vực ý, "
                "lĩnh vực đối tượng của ý")                                                       # (pi-1)
DHATU_LIST = ("yếu tố mắt, yếu tố hình sắc, yếu tố thức qua mắt, yếu tố tai, yếu tố âm thanh, yếu tố thức qua tai, "
              "yếu tố mũi, yếu tố mùi, yếu tố thức qua mũi, yếu tố lưỡi, yếu tố vị, yếu tố thức qua lưỡi, "
              "yếu tố thân, yếu tố vật xúc chạm, yếu tố thức qua thân, yếu tố ý, yếu tố đối tượng của ý, "
              "yếu tố ý thức")                                                                     # (pi-2)
SACCA_LIST = "sự thật về khổ đau, sự thật về sự phát sinh, sự thật về sự chấm dứt, sự thật về con đường"
INDRIYA_TAIL = ("năng lực tai, năng lực mũi, năng lực lưỡi, năng lực thân, năng lực ý, năng lực nữ tính, "
                "năng lực nam tính, năng lực sống, năng lực dễ chịu, năng lực khó chịu, năng lực niềm vui, "
                "năng lực nỗi buồn, năng lực bình thản, năng lực niềm tin, năng lực tinh tấn, năng lực tỉnh thức, "
                "năng lực định tâm, năng lực trí tuệ, năng lực biết được điều chưa từng biết, "
                "năng lực hiểu biết trọn vẹn, năng lực của người đã hiểu biết trọn vẹn")             # (pi-2)
INDRIYA_LIST = "năng lực mắt, " + INDRIYA_TAIL
COUNT = {"khandha": "năm khối", "āyatana": "mười hai lĩnh vực nhận biết", "dhātu": "mười tám yếu tố",
         "sacca": "bốn sự thật", "indriya": "hai mươi hai năng lực"}                               # (pi-3)

# ---------------------------------------------------------------------------------------------------------------
# Fixed strings of the ekaka definitions (ch2), reusable later
# ---------------------------------------------------------------------------------------------------------------
KALENA_SAMAYENA = "thỉnh thoảng, theo từng thời điểm"          # kālena kālaṃ samayena samayaṃ
VIMOKKHA = "chạm đến tám sự giải thoát bằng thân rồi an trú"   # aṭṭha vimokkhe kāyena phusitvā viharati
NA_HEVA_KHO = "quả thật không"                                 # na heva kho
DISVA_EKACCE = "nhờ thấy bằng trí tuệ, một số ô nhiễm của người ấy được diệt tận"   # paññāya cassa disvā ekacce āsavā parikkhīṇā honti
DISVA_SABBE = "nhờ thấy bằng trí tuệ, các ô nhiễm của người ấy được diệt tận"        # paññāya cassa disvā āsavā parikkhīṇā honti
SABBEPI = "Tất cả các bậc thánh, xét về sự giải thoát cao quý, đều {}."             # Sabbepi ariyapuggalā ariye vimokkhe X-ā.
LABHI = ("Ở đời này, có người có được các thành tựu thiền đi kèm với hình sắc hoặc đi kèm với không hình sắc.")
#   Idhekacco puggalo lābhī hoti rūpasahagatānaṃ vā arūpasahagatānaṃ vā samāpattīnaṃ.
NA_NIKAMA = ("Người ấy quả thật không có được chúng theo ý muốn, không có được chúng mà không khó khăn, "
             "không có được chúng mà không vất vả; người ấy không chứng nhập và xuất khỏi ở nơi nào mình muốn, "
             "thành tựu thiền nào mình muốn, bao lâu mình muốn.")
#   So ca kho na nikāmalābhī hoti na akicchalābhī na akasiralābhī; na yatthicchakaṃ yadicchakaṃ yāvaticchakaṃ
#   samāpajjatipi vuṭṭhātipi.
NIKAMA = ("Người ấy quả thật có được chúng theo ý muốn, có được chúng mà không khó khăn, "
          "có được chúng mà không vất vả; người ấy chứng nhập và xuất khỏi ở nơi nào mình muốn, "
          "thành tựu thiền nào mình muốn, bao lâu mình muốn.")
THANA = "Quả thật, đây là điều có thể xảy ra, rằng"           # Ṭhānaṃ kho panetaṃ vijjati, yaṃ
ATTHANA = "Đây là điều không thể xảy ra, không có cơ hội, rằng"  # Aṭṭhānametaṃ anavakāso yaṃ   (pi-2)
KUPPEYYUM = "do sự buông thả, các thành tựu thiền ấy của người ấy bị lay chuyển"   # tassa puggalassa pamādamāgamma tā samāpattiyo kuppeyyuṃ
PARIHAYEYYA = "do sự buông thả, người ấy sa sút khỏi các thành tựu thiền ấy"       # so puggalo pamādamāgamma tāhi samāpattīhi parihāyeyya
NA_PARIHAYATI = "người ấy không sa sút khỏi các thành tựu thiền ấy"                 # na parihāyati tāhi samāpattīhi
PARIHAYATI = "người ấy sa sút khỏi các thành tựu thiền ấy"                         # parihāyati tāhi samāpattīhi
AVARANA_NEG = ("mang sự ngăn che do nghiệp, mang sự ngăn che do phiền não, mang sự ngăn che do quả của nghiệp, "
               "không có niềm tin, không có ý muốn, kém trí tuệ")                                        # (pi-2)
AVARANA_POS = ("không mang sự ngăn che do nghiệp, không mang sự ngăn che do phiền não, "
               "không mang sự ngăn che do quả của nghiệp, có niềm tin, có ý muốn, có trí tuệ")             # (pi-2)
NIYAMA = "có khả năng bước vào sự cố định, tức sự đúng đắn trong các hiện tượng thiện"                     # (pi-2)
ANANUSSUTA = "tự mình giác ngộ các sự thật trong những điều chưa từng được nghe trước đây"
#   pubbe ananussutesu dhammesu sāmaṃ saccāni abhisambujjhati (negative: «không tự mình giác ngộ …»)
SABBANNUTA = "và trong đó đạt đến sự toàn tri, và sự làm chủ đối với các sức mạnh"
#   tattha ca sabbaññutaṃ pāpuṇāti, balesu ca vasībhāvaṃ
NA_SABBANNUTA = "và trong đó không đạt đến sự toàn tri, và không đạt đến sự làm chủ đối với các sức mạnh"
#   na ca tattha sabbaññutaṃ pāpuṇāti, na ca balesu vasībhāvaṃ
TRUTHS = ("hiểu rõ đúng như thật: “Đây là khổ đau”, hiểu rõ đúng như thật: “Đây là sự phát sinh của khổ đau”, "
          "hiểu rõ đúng như thật: “Đây là sự chấm dứt khổ đau”, hiểu rõ đúng như thật: "
          "“Đây là cách thực hành dẫn đến sự chấm dứt khổ đau”")
#   "idaṃ dukkha"nti yathābhūtaṃ pajānāti, … "ayaṃ dukkhanirodhagāminī paṭipadā"ti yathābhūtaṃ pajānāti
TATHAGATA = "Và Giáo Pháp do Như Lai tuyên bố được người ấy thấy rõ và thông suốt bằng trí tuệ."
#   Tathāgatappaveditā cassa dhammā paññāya vodiṭṭhā honti vocaritā.
SOTAPANNA_INTRO = ("Ở đời này, có người nhờ diệt tận hoàn toàn ba xiềng xích mà trở thành bậc vào dòng, "
                   "không thể bị rơi vào nơi đọa lạc, có hướng đi cố định, hướng đến sự giác ngộ trọn vẹn")
#   Idhekacco puggalo tiṇṇaṃ saṃyojanānaṃ parikkhayā sotāpanno hoti avinipātadhammo niyato sambodhiparāyano
DUKKHASSANTA = "đi đến tận cùng của khổ đau"                  # dukkhassantaṃ karoti
ANAGAMI_INTRO = ("Ở đời này, có người nhờ diệt tận hoàn toàn năm xiềng xích thuộc phần thấp mà được hóa sinh, "
                 "nhập Niết-bàn trọn vẹn tại đó, không còn quay trở lại từ thế gian ấy")
#   Idhekacco puggalo pañcannaṃ orambhāgiyānaṃ saṃyojanānaṃ parikkhayā opapātiko hoti, tattha parinibbāyī
#   anāvattidhammo tasmā lokā
UPARI = "làm phát sinh con đường cao quý để dứt bỏ các xiềng xích cao hơn"
#   ariyamaggaṃ sañjaneti upariṭṭhimānaṃ saṃyojanānaṃ pahānāya
PATIPANNO_DEF = "Người đang thực hành để {} là người đang thực hành để tự mình chứng nghiệm thành quả {}."
#   X-pahānāya / X-tanubhāvāya paṭipanno puggalo Y-phalasacchikiriyāya paṭipanno.
YASSA_PAHINA = "Người nào có {} đã được dứt bỏ"                # Yassa puggalassa X pahīnā(ni)
TANU = "làm suy yếu sự tham đắm dục lạc và ác ý"                                                   # (pi-1, with «để»)
ANAVASESA_KAMA = "dứt bỏ sự tham đắm dục lạc và ác ý không còn sót lại"                            # (pi-1, with «để»)
ANAVASESA_ARAHATTA = ("dứt bỏ sự tham đắm cõi hình sắc, sự tham đắm cõi không hình sắc, sự kiêu mạn, "
                      "sự xao động và vô minh không còn sót lại")                                    # (pi-1, with «để»)
KAMA_BYAPADA = "sự tham đắm dục lạc và ác ý"
ARAHATTA_FIVE = "sự tham đắm cõi hình sắc, sự tham đắm cõi không hình sắc, sự kiêu mạn, sự xao động và vô minh"
DITTHE_DHAMME = "ngay trong đời này"                            # diṭṭheva dhamme / diṭṭhe ceva dhamme   (pi-2)
PAPAKA_AKUSALA = "các hiện tượng xấu ác bất thiện"              # pāpakā akusalā dhammā   (pi-1)
CETOVIMUTTI = "sự giải thoát của tâm, sự giải thoát nhờ trí tuệ"                                   # (pi-2)
TINNO = "vị bà-la-môn đã vượt qua, đã đến bờ bên kia, đứng trên đất liền"
#   tiṇṇo pāraṅgato thale tiṭṭhati brāhmaṇo

# ---------------------------------------------------------------------------------------------------------------
# Person-type names: NAME[pali] (lower-case citation form; cap() at a line start). Chapters 3-11 use them verbatim
# in the definition question, in the quoted name and wherever the type is named.
# ---------------------------------------------------------------------------------------------------------------
EKAKA = [
    ("samayavimutto", "người được giải thoát theo từng thời điểm"),
    ("asamayavimutto", "người được giải thoát không theo từng thời điểm"),
    ("kuppadhammo", "người có thể bị lay chuyển"),
    ("akuppadhammo", "người không thể bị lay chuyển"),
    ("parihānadhammo", "người có thể bị sa sút"),
    ("aparihānadhammo", "người không thể bị sa sút"),
    ("cetanābhabbo", "người có khả năng không sa sút nhờ chủ ý"),
    ("anurakkhaṇābhabbo", "người có khả năng không sa sút nhờ sự gìn giữ"),
    ("puthujjano", "người phàm phu"),
    ("gotrabhū", "người chuyển đổi dòng dõi"),
    ("bhayūparato", "người kiêng tránh vì sợ hãi"),
    ("abhayūparato", "người kiêng tránh không vì sợ hãi"),
    ("bhabbāgamano", "người có khả năng tiến bước"),
    ("abhabbāgamano", "người không có khả năng tiến bước"),
    ("niyato", "người có hướng đi cố định"),
    ("aniyato", "người không có hướng đi cố định"),
    ("paṭipannako", "người đang thực hành"),
    ("phaleṭhito", "người đã đứng vững trong thành quả"),
    ("samasīsī", "người có hai sự kết thúc cùng lúc"),
    ("ṭhitakappī", "người khiến kiếp dừng lại"),
    ("ariyo", "bậc thánh"),
    ("anariyo", "người không phải bậc thánh"),
    ("sekkho", "người còn đang tu học"),
    ("asekkho", "người đã hoàn tất tu học"),
    ("nevasekkhanāsekkho", "người không phải còn đang tu học cũng không phải đã hoàn tất tu học"),
    ("tevijjo", "người có ba loại hiểu biết chân thật"),
    ("chaḷabhiñño", "người có sáu loại hiểu biết trực tiếp"),
    ("sammāsambuddho", "bậc Tự Giác Ngộ Hoàn Toàn"),
    ("paccekasambuddho", "bậc Độc Giác"),
    ("ubhatobhāgavimutto", "người được giải thoát theo cả hai cách"),
    ("paññāvimutto", "người được giải thoát nhờ trí tuệ"),
    ("kāyasakkhī", "người chứng nghiệm bằng thân"),
    ("diṭṭhippatto", "người đạt đến quan điểm"),
    ("saddhāvimutto", "người được giải thoát nhờ niềm tin"),
    ("dhammānusārī", "người đi theo Giáo Pháp"),
    ("saddhānusārī", "người đi theo niềm tin"),
    ("sattakkhattuparamo", "người tái sinh tối đa bảy lần"),
    ("kolaṅkolo", "người đi từ gia đình này sang gia đình khác"),
    ("ekabījī", "người có một hạt giống"),
    ("sakadāgāmī", "bậc trở lại một lần"),
    ("anāgāmī", "bậc không trở lại"),
    ("antarāparinibbāyī", "người nhập Niết-bàn trọn vẹn trong khoảng giữa"),
    ("upahaccaparinibbāyī", "người nhập Niết-bàn trọn vẹn khi gần mạng chung"),
    ("asaṅkhāraparinibbāyī", "người nhập Niết-bàn trọn vẹn không có sự thúc đẩy"),
    ("sasaṅkhāraparinibbāyī", "người nhập Niết-bàn trọn vẹn có sự thúc đẩy"),
    ("uddhaṃsotoakaniṭṭhagāmī", "người ngược dòng đi đến cõi Sắc Cứu Cánh"),
    ("sotāpanno", "bậc vào dòng"),
    ("sotāpattiphalasacchikiriyāya paṭipanno", "người đang thực hành để tự mình chứng nghiệm thành quả vào dòng"),
    ("sakadāgāmī#2", "bậc trở lại một lần"),
    ("sakadāgāmiphalasacchikiriyāya paṭipanno",
     "người đang thực hành để tự mình chứng nghiệm thành quả trở lại một lần"),
    ("anāgāmī#2", "bậc không trở lại"),
    ("anāgāmiphalasacchikiriyāya paṭipanno", "người đang thực hành để tự mình chứng nghiệm thành quả không trở lại"),
    ("arahā", "bậc A-la-hán"),
    ("arahattaphalasacchikiriyāya paṭipanno", "người đang thực hành để tự mình chứng nghiệm thành quả A-la-hán"),
]

DUKA = [  # (matrix line, [(pali, name), …])
    (1, [("kodhano", "người giận dữ"), ("upanāhī", "người ôm hận")]),
    (2, [("makkhī", "người gièm pha"), ("paḷāsī", "người ganh đua")]),
    (3, [("issukī", "người ganh tị"), ("maccharī", "người keo kiệt")]),
    (4, [("saṭho", "người gian trá"), ("māyāvī", "người xảo trá")]),
    (5, [("ahiriko", "người không biết hổ thẹn"), ("anottappī", "người không biết ghê sợ tội lỗi")]),
    (6, [("dubbaco", "người khó dạy bảo"), ("pāpamitto", "người kết bạn với người xấu")]),
    (7, [("indriyesu aguttadvāro", "người không phòng hộ cửa các giác quan"),
         ("bhojane amattaññū", "người không biết tiết độ trong ăn uống")]),
    (8, [("muṭṭhassati", "người mất tỉnh thức"), ("asampajāno", "người không hiểu biết rõ ràng")]),
    (9, [("sīlavipanno", "người suy đồi về giới hạnh"), ("diṭṭhivipanno", "người suy đồi về quan điểm")]),
    (10, [("ajjhattasaṃyojano", "người có xiềng xích ở nơi bản thân"),
          ("bahiddhāsaṃyojano", "người có xiềng xích ở bên ngoài bản thân")]),
    (11, [("akkodhano", "người không giận dữ"), ("anupanāhī", "người không ôm hận")]),
    (12, [("amakkhī", "người không gièm pha"), ("apaḷāsī", "người không ganh đua")]),
    (13, [("anissukī", "người không ganh tị"), ("amaccharī", "người không keo kiệt")]),
    (14, [("asaṭho", "người không gian trá"), ("amāyāvī", "người không xảo trá")]),
    (15, [("hirimā", "người biết hổ thẹn"), ("ottappī", "người biết ghê sợ tội lỗi")]),
    (16, [("suvaco", "người dễ dạy bảo"), ("kalyāṇamitto", "người kết bạn với người tốt")]),
    (17, [("indriyesu guttadvāro", "người phòng hộ cửa các giác quan"),
          ("bhojane mattaññū", "người biết tiết độ trong ăn uống")]),
    (18, [("upaṭṭhitassati", "người có sự tỉnh thức được thiết lập"), ("sampajāno", "người hiểu biết rõ ràng")]),
    (19, [("sīlasampanno", "người thành tựu về giới hạnh"), ("diṭṭhisampanno", "người thành tựu về quan điểm")]),
    (20, [("dve puggalā dullabhā lokasmiṃ", "hai hạng người khó tìm gặp trên thế gian")]),
    (21, [("dve puggalā duttappayā", "hai hạng người khó làm cho thỏa mãn")]),
    (22, [("dve puggalā sutappayā", "hai hạng người dễ làm cho thỏa mãn")]),
    (23, [("dvinnaṃ puggalānaṃ āsavā vaḍḍhanti", "ô nhiễm của hai hạng người tăng trưởng")]),
    (24, [("dvinnaṃ puggalānaṃ āsavā na vaḍḍhanti", "ô nhiễm của hai hạng người không tăng trưởng")]),
    (25, [("hīnādhimutto", "người có chí hướng thấp kém"), ("paṇītādhimutto", "người có chí hướng ưu việt")]),
    (26, [("titto", "người đã thỏa mãn"), ("tappetā", "người làm cho người khác thỏa mãn")]),
]

TIKA = [
    (1, [("nirāso", "người không có mong cầu"), ("āsaṃso", "người có mong cầu"),
         ("vigatāso", "người đã lìa mong cầu")]),
    (2, [("tayo gilānūpamā puggalā", "ba hạng người giống như người bệnh")]),
    (3, [("kāyasakkhī", None), ("diṭṭhippatto", None), ("saddhāvimutto", None)]),
    (4, [("gūthabhāṇī", "người nói lời như phân"), ("pupphabhāṇī", "người nói lời như hoa"),
         ("madhubhāṇī", "người nói lời như mật")]),
    (5, [("arukūpamacitto puggalo", "người có tâm giống như vết thương lở loét"),
         ("vijjūpamacitto puggalo", "người có tâm giống như tia chớp"),
         ("vajirūpamacitto puggalo", "người có tâm giống như kim cương")]),
    (6, [("andho", "người mù"), ("ekacakkhu", "người một mắt"), ("dvicakkhu", "người hai mắt")]),
    (7, [("avakujjapañño puggalo", "người có trí tuệ úp ngược"),
         ("ucchaṅgapañño puggalo", "người có trí tuệ như vạt áo"),
         ("puthupañño puggalo", "người có trí tuệ rộng lớn")]),
    (8, [("kāmesu ca bhavesu ca avītarāgo",
          "có người chưa lìa tham đắm đối với các dục lạc và đối với các sự hiện hữu"),
         ("kāmesu vītarāgo bhavesu avītarāgo",
          "có người đã lìa tham đắm đối với các dục lạc nhưng chưa lìa tham đắm đối với các sự hiện hữu"),
         ("kāmesu ca bhavesu ca vītarāgo",
          "có người đã lìa tham đắm đối với cả các dục lạc lẫn các sự hiện hữu")]),
    (9, [("pāsāṇalekhūpamo puggalo", "người giống như đường vạch trên đá"),
         ("pathavilekhūpamo puggalo", "người giống như đường vạch trên đất"),
         ("udakalekhūpamo puggalo", "người giống như đường vạch trên nước")]),
    (10, [("tayo potthakūpamā puggalā", "ba hạng người giống như vải gai thô")]),
    (11, [("tayo kāsikavatthūpamā puggalā", "ba hạng người giống như vải xứ Ca-thi")]),
    (12, [("suppameyyo", "người dễ đo lường"), ("duppameyyo", "người khó đo lường"),
          ("appameyyo", "người không thể đo lường")]),
    (13, [("na sevitabbo na bhajitabbo na payirupāsitabbo",
           "có người không đáng gần gũi, không đáng kết giao, không đáng thân cận"),
          ("sevitabbo bhajitabbo payirupāsitabbo", "có người đáng gần gũi, đáng kết giao, đáng thân cận"),
          ("sakkatvā garuṃ katvā sevitabbo bhajitabbo payirupāsitabbo",
           "có người đáng gần gũi, đáng kết giao, đáng thân cận với lòng tôn kính và sự trân trọng")]),
    (14, [("jigucchitabbo na sevitabbo na bhajitabbo na payirupāsitabbo",
           "có người đáng ghê tránh, không đáng gần gũi, không đáng kết giao, không đáng thân cận"),
          ("ajjhupekkhitabbo na sevitabbo na bhajitabbo na payirupāsitabbo",
           "có người đáng được nhìn với sự bình thản, không đáng gần gũi, không đáng kết giao, không đáng thân cận"),
          ("sevitabbo bhajitabbo payirupāsitabbo#14", "có người đáng gần gũi, đáng kết giao, đáng thân cận")]),
    (15, [("sīlesu paripūrakārī, samādhismiṃ mattaso kārī, paññāya mattaso kārī",
           "có người thực hành trọn vẹn các giới hạnh, thực hành ở mức vừa phải về định tâm, "
           "thực hành ở mức vừa phải về trí tuệ"),
          ("sīlesu ca paripūrakārī, samādhismiñca paripūrakārī, paññāya mattaso kārī",
           "có người vừa thực hành trọn vẹn các giới hạnh, vừa thực hành trọn vẹn về định tâm, "
           "nhưng thực hành ở mức vừa phải về trí tuệ"),
          ("sīlesu ca paripūrakārī, samādhismiñca paripūrakārī, paññāya ca paripūrakārī",
           "có người vừa thực hành trọn vẹn các giới hạnh, vừa thực hành trọn vẹn về định tâm, "
           "vừa thực hành trọn vẹn về trí tuệ")]),
    (16, [("tayo satthāro", "ba bậc đạo sư")]),
    (17, [("aparepi tayo satthāro", "lại có ba bậc đạo sư khác")]),
]

_NA_ANU = "không xem xét, không tìm hiểu thấu đáo mà"   # ananuvicca apariyogāhetvā
_ANU = "sau khi xem xét, tìm hiểu thấu đáo thì"          # anuvicca pariyogāhetvā
VANNA_OK = "nói lời khen ngợi người đáng khen ngợi"      # vaṇṇārahassa vaṇṇaṃ bhāsitā hoti
AVANNA_OK = "nói lời chê trách người đáng chê trách"     # avaṇṇārahassa avaṇṇaṃ bhāsitā hoti
VANNA_BAD = "nói lời khen ngợi người đáng chê trách"     # avaṇṇārahassa vaṇṇaṃ bhāsitā hoti
AVANNA_BAD = "nói lời chê trách người đáng khen ngợi"    # vaṇṇārahassa avaṇṇaṃ bhāsitā hoti
PASADA_OK = "bày tỏ lòng tin trong sáng ở nơi đáng có lòng tin trong sáng"               # pasādanīye ṭhāne pasādaṃ upadaṃsitā hoti
PASADA_BAD = "bày tỏ lòng tin trong sáng ở nơi không đáng có lòng tin trong sáng"        # appasādanīye ṭhāne pasādaṃ …
APPASADA_OK = "bày tỏ sự thiếu lòng tin trong sáng ở nơi không đáng có lòng tin trong sáng"  # appasādanīye ṭhāne appasādaṃ …
APPASADA_BAD = "bày tỏ sự thiếu lòng tin trong sáng ở nơi đáng có lòng tin trong sáng"   # pasādanīye ṭhāne appasādaṃ …
BTK = "một cách đúng sự thật, chính xác, đúng lúc"      # bhūtaṃ tacchaṃ kālena
_ATTA = "vì lợi ích của bản thân"                       # attahitāya
_PARA = "vì lợi ích của người khác"                     # parahitāya
_TAPA_A = "tự hành hạ bản thân, chuyên tâm thực hành việc hành hạ bản thân"   # attantapo … attaparitāpanānuyogamanuyutto
_TAPA_P = "hành hạ người khác, chuyên tâm thực hành việc hành hạ người khác"  # parantapo … paraparitāpanānuyogamanuyutto
_SAMATHA = "sự tĩnh lặng của tâm ở nơi bản thân"        # ajjhattaṃ cetosamathassa
_VIPASSANA = "sự thấu suốt các hiện tượng nhờ trí tuệ cao thượng"   # adhipaññādhammavipassanāya

CATUKKA = [
    (1, [("asappuriso", "người không chân chính"),
         ("asappurisena asappurisataro", "người không chân chính hơn cả người không chân chính"),
         ("sappuriso", "người chân chính"), ("sappurisena sappurisataro", "người chân chính hơn cả người chân chính")]),
    (2, [("pāpo", "người xấu"), ("pāpena pāpataro", "người xấu hơn cả người xấu"), ("kalyāṇo", "người tốt"),
         ("kalyāṇena kalyāṇataro", "người tốt hơn cả người tốt")]),
    (3, [("pāpadhammo", "người có phẩm chất xấu"),
         ("pāpadhammena pāpadhammataro", "người có phẩm chất xấu hơn cả người có phẩm chất xấu"),
         ("kalyāṇadhammo", "người có phẩm chất tốt"),
         ("kalyāṇadhammena kalyāṇadhammataro", "người có phẩm chất tốt hơn cả người có phẩm chất tốt")]),
    (4, [("sāvajjo", "người có lỗi"), ("vajjabahulo", "người có nhiều lỗi"), ("appavajjo", "người ít lỗi"),
         ("anavajjo", "người không có lỗi")]),
    (5, [("ugghaṭitaññū", "người biết ngay khi vừa được nêu ra"),
         ("vipañcitaññū", "người biết khi được giải thích chi tiết"), ("neyyo", "người cần được dẫn dắt"),
         ("padaparamo", "người chỉ dừng lại ở câu chữ")]),
    (6, [("yuttappaṭibhāno, no muttappaṭibhāno",
          "người có tài ứng đáp xác đáng nhưng không có tài ứng đáp lưu loát"),
         ("muttappaṭibhāno, no yuttappaṭibhāno",
          "người có tài ứng đáp lưu loát nhưng không có tài ứng đáp xác đáng"),
         ("yuttappaṭibhāno ca muttappaṭibhāno ca", "người vừa có tài ứng đáp xác đáng vừa có tài ứng đáp lưu loát"),
         ("neva yuttappaṭibhāno no muttappaṭibhāno",
          "người không có tài ứng đáp xác đáng cũng không có tài ứng đáp lưu loát")]),
    (7, [("cattāro dhammakathikā puggalā", "bốn hạng người thuyết giảng Giáo Pháp")]),
    (8, [("cattāro valāhakūpamā puggalā", "bốn hạng người giống như đám mây mưa")]),
    (9, [("cattāro mūsikūpamā puggalā", "bốn hạng người giống như con chuột")]),
    (10, [("cattāro ambūpamā puggalā", "bốn hạng người giống như quả xoài")]),
    (11, [("cattāro kumbhūpamā puggalā", "bốn hạng người giống như cái chum")]),
    (12, [("cattāro udakarahadūpamā puggalā", "bốn hạng người giống như hồ nước")]),
    (13, [("cattāro balībaddūpamā puggalā", "bốn hạng người giống như con bò đực")]),
    (14, [("cattāro āsīvisūpamā puggalā", "bốn hạng người giống như con rắn độc")]),
    (15, [("ananuvicca apariyogāhetvā avaṇṇārahassa vaṇṇaṃ bhāsitā hoti", f"có người {_NA_ANU} {VANNA_BAD}"),
          ("ananuvicca apariyogāhetvā vaṇṇārahassa avaṇṇaṃ bhāsitā hoti", f"có người {_NA_ANU} {AVANNA_BAD}"),
          ("ananuvicca apariyogāhetvā appasādanīye ṭhāne pasādaṃ upadaṃsitā hoti", f"có người {_NA_ANU} {PASADA_BAD}"),
          ("ananuvicca apariyogāhetvā pasādanīye ṭhāne appasādaṃ upadaṃsitā hoti",
           f"có người {_NA_ANU} {APPASADA_BAD}")]),
    (16, [("anuvicca pariyogāhetvā avaṇṇārahassa avaṇṇaṃ bhāsitā hoti", f"có người {_ANU} {AVANNA_OK}"),
          ("anuvicca pariyogāhetvā vaṇṇārahassa vaṇṇaṃ bhāsitā hoti", f"có người {_ANU} {VANNA_OK}"),
          ("anuvicca pariyogāhetvā appasādanīye ṭhāne appasādaṃ upadaṃsitā hoti", f"có người {_ANU} {APPASADA_OK}"),
          ("anuvicca pariyogāhetvā pasādanīye ṭhāne pasādaṃ upadaṃsitā hoti", f"có người {_ANU} {PASADA_OK}")]),
    (17, [("avaṇṇārahassa avaṇṇaṃ bhāsitā hoti bhūtaṃ tacchaṃ kālena, no ca kho vaṇṇārahassa vaṇṇaṃ …",
           f"có người {AVANNA_OK} {BTK}, nhưng quả thật không {VANNA_OK} {BTK}"),
          ("vaṇṇārahassa vaṇṇaṃ bhāsitā hoti bhūtaṃ tacchaṃ kālena, no ca kho avaṇṇārahassa avaṇṇaṃ …",
           f"có người {VANNA_OK} {BTK}, nhưng quả thật không {AVANNA_OK} {BTK}"),
          ("avaṇṇārahassa ca avaṇṇaṃ … ; vaṇṇārahassa ca vaṇṇaṃ …",
           f"có người vừa {AVANNA_OK} {BTK}; vừa {VANNA_OK} {BTK}"),
          ("neva avaṇṇārahassa avaṇṇaṃ … no ca vaṇṇārahassa vaṇṇaṃ …",
           f"có người không {AVANNA_OK} {BTK}, cũng không {VANNA_OK} {BTK}")]),
    (18, [("uṭṭhānaphalūpajīvī no puññaphalūpajīvī",
           "người sống nhờ thành quả của công sức chứ không sống nhờ thành quả của phước"),
          ("puññaphalūpajīvī no uṭṭhānaphalūpajīvī",
           "người sống nhờ thành quả của phước chứ không sống nhờ thành quả của công sức"),
          ("uṭṭhānaphalūpajīvī ca puññaphalūpajīvī ca",
           "người sống nhờ cả thành quả của công sức lẫn thành quả của phước"),
          ("neva uṭṭhānaphalūpajīvī no puññaphalūpajīvī",
           "người không sống nhờ thành quả của công sức cũng không sống nhờ thành quả của phước")]),
    (19, [("tamo tamaparāyano", "người trong bóng tối hướng đến bóng tối"),
          ("tamo jotiparāyano", "người trong bóng tối hướng đến ánh sáng"),
          ("joti tamaparāyano", "người trong ánh sáng hướng đến bóng tối"),
          ("joti jotiparāyano", "người trong ánh sáng hướng đến ánh sáng")]),
    (20, [("oṇatoṇato", "người đang ở thấp và đi xuống thấp"), ("oṇatuṇṇato", "người đang ở thấp và đi lên cao"),
          ("uṇṇatoṇato", "người đang ở cao và đi xuống thấp"), ("uṇṇatuṇṇato", "người đang ở cao và đi lên cao")]),
    (21, [("cattāro rukkhūpamā puggalā", "bốn hạng người giống như cái cây")]),
    (22, [("rūpappamāṇo", "người lấy hình sắc làm thước đo"),
          ("rūpappasanno", "người có lòng tin trong sáng nơi hình sắc"),
          ("ghosappamāṇo", "người lấy tiếng tăm làm thước đo"),
          ("ghosappasanno", "người có lòng tin trong sáng nơi tiếng tăm")]),
    (23, [("lūkhappamāṇo", "người lấy sự đạm bạc làm thước đo"),
          ("lūkhappasanno", "người có lòng tin trong sáng nơi sự đạm bạc"),
          ("dhammappamāṇo", "người lấy Giáo Pháp làm thước đo"),
          ("dhammappasanno", "người có lòng tin trong sáng nơi Giáo Pháp")]),
    (24, [("attahitāya paṭipanno hoti, no parahitāya", f"có người thực hành {_ATTA}, không {_PARA}"),
          ("parahitāya paṭipanno hoti, no attahitāya", f"có người thực hành {_PARA}, không {_ATTA}"),
          ("attahitāya ceva paṭipanno hoti parahitāya ca", f"có người thực hành {_ATTA} và cả {_PARA}"),
          ("neva attahitāya paṭipanno hoti no parahitāya", f"có người không thực hành {_ATTA}, cũng không {_PARA}")]),
    (25, [("attantapo hoti attaparitāpanānuyogamanuyutto", f"có người {_TAPA_A}"),
          ("parantapo hoti paraparitāpanānuyogamanuyutto", f"có người {_TAPA_P}"),
          ("attantapo ca … parantapo ca …", f"có người vừa {_TAPA_A}, vừa {_TAPA_P}"),
          ("neva attantapo … na parantapo …",
           "có người không tự hành hạ bản thân, không chuyên tâm thực hành việc hành hạ bản thân, "
           "không hành hạ người khác, không chuyên tâm thực hành việc hành hạ người khác")]),
    (26, [("sarāgo", "người có tham đắm"), ("sadoso", "người có sân hận"), ("samoho", "người có si mê"),
          ("samāno", "người có kiêu mạn")]),
    (27, [("lābhī … cetosamathassa, na lābhī … vipassanāya", f"có người có được {_SAMATHA}, nhưng không có được {_VIPASSANA}"),
          ("lābhī … vipassanāya, na lābhī … cetosamathassa", f"có người có được {_VIPASSANA}, nhưng không có được {_SAMATHA}"),
          ("lābhī ceva … cetosamathassa, lābhī ca … vipassanāya", f"có người vừa có được {_SAMATHA}, vừa có được {_VIPASSANA}"),
          ("neva lābhī … cetosamathassa, na lābhī … vipassanāya",
           f"có người không có được {_SAMATHA}, cũng không có được {_VIPASSANA}")]),
    (28, [("anusotagāmī puggalo", "người đi xuôi dòng"), ("paṭisotagāmī puggalo", "người đi ngược dòng"),
          ("ṭhitatto puggalo", "người đứng vững"), ("tiṇṇo pāraṅgato thale tiṭṭhati brāhmaṇo", TINNO)]),
    (29, [("appassuto sutena anupapanno", "người học hỏi ít và không thành tựu nhờ điều đã học"),
          ("appassuto sutena upapanno", "người học hỏi ít nhưng thành tựu nhờ điều đã học"),
          ("bahussuto sutena anupapanno", "người học hỏi nhiều nhưng không thành tựu nhờ điều đã học"),
          ("bahussuto sutena upapanno", "người học hỏi nhiều và thành tựu nhờ điều đã học")]),
    (30, [("samaṇamacalo", "vị sa-môn bất động"), ("samaṇapadumo", "vị sa-môn như hoa sen hồng"),
          ("samaṇapuṇḍarīko", "vị sa-môn như hoa sen trắng"),
          ("samaṇesu samaṇasukhumālo", "vị sa-môn tinh tế giữa các sa-môn")]),
]

_PANCA_TAIL = (f"{{}} hiểu rõ đúng như thật {CETOVIMUTTI} ấy, trong đó {PAPAKA_AKUSALA} "
               "đã sinh khởi của người ấy chấm dứt không còn dư sót")
#   tañca cetovimuttiṃ paññāvimuttiṃ yathābhūtaṃ (na)ppajānāti, yatthassa te uppannā pāpakā akusalā dhammā
#   aparisesā nirujjhanti   ({} = «và không» / «và»)
PANCAKA = [
    (1, [("ārabhati ca vippaṭisārī ca hoti … nappajānāti",
          "có người vừa phạm lỗi vừa ăn năn, " + _PANCA_TAIL.format("và không")),
         ("ārabhati na vippaṭisārī ca hoti … nappajānāti",
          "có người phạm lỗi nhưng không ăn năn, " + _PANCA_TAIL.format("và không")),
         ("nārabhati vippaṭisārī ca hoti … nappajānāti",
          "có người không phạm lỗi nhưng ăn năn, " + _PANCA_TAIL.format("và không")),
         ("nārabhati na vippaṭisārī hoti … nappajānāti",
          "có người không phạm lỗi, không ăn năn, " + _PANCA_TAIL.format("và không")),
         ("nārabhati na vippaṭisārī hoti … pajānāti",
          "có người không phạm lỗi, không ăn năn, " + _PANCA_TAIL.format("và"))]),
    (2, [("datvā avajānāti", "người cho rồi khinh thường"), ("saṃvāsena avajānāti", "người khinh thường vì sống chung"),
         ("ādheyyamukho hoti", "người cả tin"), ("lolo hoti", "người không kiên định"),
         ("mando momūho hoti", "người chậm hiểu, mê muội")]),
    (3, [("pañca yodhājīvūpamā puggalā", "năm hạng người giống như chiến binh")]),
    (4, [("pañca piṇḍapātikā", "năm hạng người chỉ ăn thức ăn khất thực")]),
    (5, [("pañca khalupacchābhattikā", "năm hạng người không nhận thức ăn dâng sau bữa")]),
    (6, [("pañca ekāsanikā", "năm hạng người chỉ ăn trong một lần ngồi")]),
    (7, [("pañca paṃsukūlikā", "năm hạng người mặc y may từ vải bỏ đi")]),
    (8, [("pañca tecīvarikā", "năm hạng người chỉ dùng ba y")]),
    (9, [("pañca āraññikā", "năm hạng người sống trong rừng")]),
    (10, [("pañca rukkhamūlikā", "năm hạng người sống dưới gốc cây")]),
    (11, [("pañca abbhokāsikā", "năm hạng người sống ngoài trời")]),
    (12, [("pañca nesajjikā", "năm hạng người chỉ ngồi không nằm")]),
    (13, [("pañca yathāsanthatikā", "năm hạng người ở bất cứ chỗ nào được chỉ định")]),
    (14, [("pañca sosānikā", "năm hạng người sống ở bãi tha ma")]),
]

CHAKKA = [
    (1, [("… abhisambujjhati, tattha ca sabbaññutaṃ pāpuṇāti balesu ca vasībhāvaṃ",
          f"có người {ANANUSSUTA}, {SABBANNUTA}"),
         ("… abhisambujjhati, na ca tattha sabbaññutaṃ pāpuṇāti na ca balesu vasībhāvaṃ",
          f"có người {ANANUSSUTA}, {NA_SABBANNUTA}"),
         ("… anabhisambujjhati, diṭṭhe ceva dhamme dukkhassantakaro hoti sāvakapāramiñca pāpuṇāti",
          f"có người không {ANANUSSUTA}, nhưng {DITTHE_DHAMME} trở thành người {DUKKHASSANTA}, "
          "và đạt đến sự toàn hảo của hàng đệ tử"),
         ("… anabhisambujjhati, diṭṭheva dhamme dukkhassantakaro hoti, na ca sāvakapāramiṃ pāpuṇāti",
          f"có người không {ANANUSSUTA}, nhưng {DITTHE_DHAMME} trở thành người {DUKKHASSANTA}, "
          "và không đạt đến sự toàn hảo của hàng đệ tử"),
         ("… anabhisambujjhati, na ca diṭṭheva dhamme dukkhassantakaro hoti, anāgāmī hoti anāgantā itthattaṃ",
          f"có người không {ANANUSSUTA}, và không trở thành người {DUKKHASSANTA} {DITTHE_DHAMME}, "
          "mà trở thành bậc không trở lại, người không trở lại đời này"),
         ("… anabhisambujjhati, na ca diṭṭheva dhamme dukkhassantakaro hoti, āgāmī hoti āgantā itthattaṃ",
          f"có người không {ANANUSSUTA}, và không trở thành người {DUKKHASSANTA} {DITTHE_DHAMME}, "
          "mà trở thành người còn trở lại, người sẽ trở lại đời này")]),
]

SATTAKA = [
    (1, [("satta udakūpamā puggalā", "bảy hạng người giống như người ở trong nước"),
         ("sakiṃ nimuggo nimuggova hoti", "người một lần chìm thì chìm luôn"),
         ("ummujjitvā nimujjati", "người trồi lên rồi lại chìm"),
         ("ummujjitvā ṭhito hoti", "người trồi lên rồi đứng yên"),
         ("ummujjitvā vipassati viloketi", "người trồi lên rồi nhìn thấy rõ, nhìn quanh"),
         ("ummujjitvā patarati", "người trồi lên rồi bơi qua"),
         ("ummujjitvā paṭigādhappatto hoti", "người trồi lên rồi đạt đến chỗ chân chạm đáy"),
         ("ummujjitvā tiṇṇo hoti pāraṅgato thale tiṭṭhati brāhmaṇo", "người trồi lên rồi trở thành " + TINNO)]),
    (2, [(k, None) for k in ("ubhatobhāgavimutto", "paññāvimutto", "kāyasakkhī", "diṭṭhippatto", "saddhāvimutto",
                             "dhammānusārī", "saddhānusārī")]),
]
AṬṬHAKA = [(1, [("cattāro maggasamaṅgino", "bốn hạng người có được con đường"),
                ("cattāro phalasamaṅgino puggalā", "bốn hạng người có được thành quả")])]
NAVAKA = [(1, [(k, None) for k in ("sammāsambuddho", "paccekasambuddho", "ubhatobhāgavimutto", "paññāvimutto",
                                    "kāyasakkhī", "diṭṭhippatto", "saddhāvimutto", "dhammānusārī", "saddhānusārī")])]
DASAKA = [(1, [("pañcannaṃ idha niṭṭhā", "năm hạng người đạt đến đích ở đời này"),
               ("pañcannaṃ idha vihāya niṭṭhā", "năm hạng người đạt đến đích sau khi rời khỏi đời này")])]

NAME = {}
for _k, _v in EKAKA:
    NAME.setdefault(_k.split("#")[0], _v)
for _grp in (DUKA, TIKA, CATUKKA, PANCAKA, CHAKKA, SATTAKA, AṬṬHAKA, NAVAKA, DASAKA):
    for _n, _items in _grp:
        for _k, _v in _items:
            if _v is not None:
                NAME.setdefault(_k.split("#")[0], _v)
for _grp in (TIKA, SATTAKA, NAVAKA):
    for _n, _items in _grp:
        for _k, _v in _items:
            if _v is None:
                assert _k in NAME, _k

# ---------------------------------------------------------------------------------------------------------------
# Strings taken unchanged from the approved pi-1 / pi-2 / pi-3 Vietnamese rails (asserted at build time)
# ---------------------------------------------------------------------------------------------------------------
REUSED = [  # (Pāli, Vietnamese, book)
    ("Namo tassa bhagavato arahato sammāsambuddhassa", HOMAGE, "1"),
    ("# Abhidhammapiṭake", H_ABHI, "1"),
    ("### Mātikā", H_MATIKA, "1"),
    ("rūpakkhandho, vedanākkhandho, saññākkhandho, saṅkhārakkhandho, viññāṇakkhandho", KHANDHA_LIST, "2"),
    ("cakkhāyatanaṃ, rūpāyatanaṃ, … manāyatanaṃ, dhammāyatanaṃ", AYATANA_LIST, "1"),
    ("cakkhudhātu, rūpadhātu, cakkhuviññāṇadhātu, … manodhātu, dhammadhātu, manoviññāṇadhātu", DHATU_LIST, "2"),
    ("(cakkhundriyaṃ,) sotindriyaṃ, … aññindriyaṃ, aññātāvindriyaṃ", INDRIYA_TAIL, "2"),
    ("dukkhasaccaṃ", "sự thật về khổ đau", "2"),
    ("samudayasaccaṃ", "sự thật về sự phát sinh", "2"),
    ("pañcakkhandhā (counted)", "năm khối", "3"),
    ("dvādasāyatanāni (counted)", "mười hai lĩnh vực nhận biết", "3"),
    ("aṭṭhārasa dhātuyo (counted)", "mười tám yếu tố", "3"),
    ("cattāri saccāni (counted)", "bốn sự thật", "3"),
    ("bāvīsatindriyāni (counted)", "hai mươi hai năng lực", "3"),
    ("Aṭṭhānametaṃ anavakāso yaṃ", ATTHANA, "2"),
    ("(Ṭhānañca kho) etaṃ vijjati yaṃ", "đây là điều có thể xảy ra, rằng", "2"),
    ("kammāvaraṇena samannāgatā … assaddhā acchandikā duppaññā", AVARANA_NEG, "2"),
    ("na kammāvaraṇena samannāgatā … saddhā chandikā paññavanto", AVARANA_POS, "2"),
    ("bhabbā niyāmaṃ okkamituṃ kusalesu dhammesu sammattaṃ", NIYAMA, "2"),
    ("kāmarāgabyāpādānaṃ tanubhāvāya", "để " + TANU, "1"),
    ("kāmarāgabyāpādānaṃ anavasesappahānāya", "để " + ANAVASESA_KAMA, "1"),
    ("rūparāgaarūparāgamānauddhaccaavijjāya anavasesappahānāya", "để " + ANAVASESA_ARAHATTA, "1"),
    ("pāpakā akusalā dhammā", PAPAKA_AKUSALA, "1"),
    ("cetovimuttiṃ paññāvimuttiṃ", CETOVIMUTTI, "2"),
    ("dukkhasamudayo", "sự phát sinh của khổ đau", "2"),
    ("dukkhanirodhagāminī paṭipadā", "cách thực hành dẫn đến sự chấm dứt khổ đau", "2"),
    ("yathābhūtaṃ pajānāti", "hiểu rõ đúng như thật", "2"),
    ("apubbaṃ acarimaṃ", "không trước không sau", "2"),
    ("diṭṭheva dhamme", DITTHE_DHAMME, "2"),
    ("puthujjano", "người phàm phu", "1"),
    ("ariyadhamma", "Giáo Pháp cao quý", "1"),
    ("kammāni ānantarikāni", "nghiệp có quả không gián đoạn", "1"),
    ("micchādiṭṭhi niyatā", "quan điểm sai lầm cố định", "1"),
    ("sekkha (person)", "người còn đang tu học", "1"),
    ("asekkha (person)", "người đã hoàn tất tu học", "1"),
    ("Tathāgata", "Như Lai", "2"),
    ("sudassī (Pure Abode)", "Thiện Kiến", "2"),
    ("a. ni. (citation)", "Tăng Chi Bộ Kinh", "2"),
    ("Idhekacco puggalo", IDHEKACCO, "1"),
]

# ---------------------------------------------------------------------------------------------------------------
# Builders
# ---------------------------------------------------------------------------------------------------------------


def seg(*lines):
    return "\n".join(lines)


def build_preamble():
    return [seg(HOMAGE + " ^T-1"), seg(H_ABHI + " ^0"), seg(H_BOOK + " ^4-0")]


def _items_line(n, items, sep=", ", end="."):
    names = [v if v is not None else NAME[k] for k, v in items]
    return f"({n}) " + cap(sep.join(names)) + end


def build_matika():
    S = [seg(H_MATIKA + " ^4-M-0"), seg(H_UDDESO[1] + " ^4-M-1-0")]
    S.append(seg("Có sáu sự định danh – " + ", ".join(PANNATTI[k] for k in DESIG) + ". ^4-M-1"))
    lists = [("khandha", KHANDHA_LIST, "^4-M-2"), ("āyatana", AYATANA_LIST, "^4-M-3"), ("dhātu", DHATU_LIST, "^4-M-4"),
             ("sacca", SACCA_LIST, "^4-M-5"), ("indriya", INDRIYA_LIST, "^4-M-6")]
    for k, lst, bid in lists:
        S.append(seg(cap(kittavata(DESIG[k])) + " " + yavata_ettavata(DESIG[k], f"{COUNT[k]} – {lst}") + " " + bid))
    # ^4-M-7: ekaka list
    lines = [cap(kittavata(DESIG["puggala"]))]
    for i, (k, v) in enumerate(EKAKA, 1):
        t = f"({i}) " + cap(v)
        if k == "paccekasambuddho":
            t += " [dị bản (Sī.): paccekabuddho]"
        if k == "arahattaphalasacchikiriyāya paṭipanno":
            t += " [dị bản (Sī.): arahattāya]"
        lines.append(t)
    lines.append(CLOSER_MATRIX[1] + " ^4-M-7")
    S.append(seg(*lines))

    # ^4-M-8: duka
    S.append(seg(H_UDDESO[2] + " ^4-M-2-0"))
    lines = [GROUP_OPEN[2]]
    for n, items in DUKA:
        if len(items) == 2:
            a, b = items[0][1], items[1][1]
            if n == 2:
                b += " [khác chính tả (Syā., Ka.): palāsī]"
            lines.append(f"({n}) " + ca_ca(a, b))
        else:
            lines.append(f"({n}) " + cap(items[0][1]) + ".")
    lines.append(CLOSER_MATRIX[2] + " ^4-M-8")
    S.append(seg(*lines))

    # ^4-M-9: tika
    S.append(seg(H_UDDESO[3] + " ^4-M-3-0"))
    lines = [GROUP_OPEN[3]]
    for n, items in TIKA:
        names = [v if v is not None else NAME[k] for k, v in items]
        if n == 7:
            names[1] += " [khác chính tả (Syā.): uccaṅgupañño]"
        if n == 13:
            names[2] += " [khác chính tả (Sī.): garukatvā]"
        if n == 14:
            line = f"({n}) " + cap(names[0]) + ", " + names[1] + "; " + names[2] + "."
        elif n == 15:
            first = names[0].replace("các giới hạnh,", "các giới hạnh [khác chính tả (Syā.): paripūrīkārī],", 1)
            line = f"({n}) " + cap(first) + "; " + names[1] + "; " + names[2] + "."
        else:
            line = f"({n}) " + cap(", ".join(names)) + "."
        lines.append(line)
    lines.append(CLOSER_MATRIX[3] + " ^4-M-9")
    S.append(seg(*lines))

    # ^4-M-10: catukka
    S.append(seg(H_UDDESO[4] + " ^4-M-4-0"))
    lines = [GROUP_OPEN[4]]
    for n, items in CATUKKA:
        names = [v for k, v in items]
        if n == 4:
            names[2] += " [dị bản (Syā., Ka.): appasāvajjo; Tăng Chi Bộ Kinh 4.135]"
        if n == 5:
            names[1] += " [khác chính tả (Sī.): vipacitaññū; Tăng Chi Bộ Kinh 4.133]"
        if n == 13:
            names[0] += " [khác chính tả (Sī.): balibaddūpamā]"
        if n == 28:
            names[3] = names[3].replace("bờ bên kia,", "bờ bên kia [khác chính tả (Sī., Syā.): pāragato],", 1)
        if n in (17,):
            line = (f"({n}) " + cap(names[0]) + "; " + names[1] + "; " + names[2] + ", " + names[3] + ".")
        elif n in (24, 27):
            line = f"({n}) " + cap("; ".join(names)) + "."
        elif n == 25:
            line = (f"({n}) " + cap("; ".join(names)) + ". " + CATUKKA_25_SO)
        else:
            line = f"({n}) " + cap(", ".join(names)) + "."
        lines.append(line)
    lines.append(CLOSER_MATRIX[4] + " ^4-M-10")
    S.append(seg(*lines))

    # ^4-M-11: pañcaka
    S.append(seg(H_UDDESO[5] + " ^4-M-5-0"))
    lines = [GROUP_OPEN[5]]
    for n, items in PANCAKA:
        names = [v for k, v in items]
        if n == 1:
            first = names[0].replace("vừa phạm lỗi", "vừa phạm lỗi [khác chính tả (Sī., Syā.): ārambhati]", 1)
            sents = [cap(first)] + [cap(x) for x in names[1:]]
            line = f"({n}) " + ". ".join(sents) + "."
        else:
            line = f"({n}) " + cap(", ".join(names)) + "."
        lines.append(line)
    lines.append(CLOSER_MATRIX[5] + " ^4-M-11")
    S.append(seg(*lines))

    # ^4-M-12: chakka
    S.append(seg(H_UDDESO[6] + " ^4-M-6-0"))
    names = [v for k, v in CHAKKA[0][1]]
    names[0] = names[0] + " [dị bản (Pī.): phalesu]"
    names[4] = names[4].replace("người không trở lại đời này",
                                "người không trở lại [dị bản (Syā., Ka.): anāgantvā; Tăng Chi Bộ Kinh 4.171] đời này", 1)
    names[5] = names[5].replace("người còn trở lại,", "người còn trở lại [dị bản (Syā., Ka.): sotāpannasakadāgāmī],", 1)
    S.append(seg(GROUP_OPEN[6], "(1) " + ". ".join(cap(x) for x in names) + ".", CLOSER_MATRIX[6] + " ^4-M-12"))

    # ^4-M-13: sattaka
    S.append(seg(H_UDDESO[7] + " ^4-M-7-0"))
    w = [v for k, v in SATTAKA[0][1]]
    l1 = "(1) " + cap(w[0]) + ". " + cap(", ".join(w[1:])) + "."
    S.append(seg(GROUP_OPEN[7], l1, _items_line(2, SATTAKA[1][1]), CLOSER_MATRIX[7] + " ^4-M-13"))

    # ^4-M-14 .. ^4-M-16
    S.append(seg(H_UDDESO[8] + " ^4-M-8-0"))
    S.append(seg(GROUP_OPEN[8], _items_line(1, AṬṬHAKA[0][1]), CLOSER_MATRIX[8] + " ^4-M-14"))
    S.append(seg(H_UDDESO[9] + " ^4-M-9-0"))
    S.append(seg(GROUP_OPEN[9], _items_line(1, NAVAKA[0][1]), CLOSER_MATRIX[9] + " ^4-M-15"))
    S.append(seg(H_UDDESO[10] + " ^4-M-10-0"))
    S.append(seg(GROUP_OPEN[10], _items_line(1, DASAKA[0][1]), CLOSER_MATRIX[10], MATIKA_END + " ^4-M-16"))
    return S


CATUKKA_25_SO = ("Người ấy không tự hành hạ bản thân, không hành hạ người khác, " + DITTHE_DHAMME
                 + " không còn đói khát, đã lắng dịu, đã trở nên mát mẻ [khác chính tả (Sī., Ka.): sītibhūto], "
                 "cảm nhận hạnh phúc, sống với bản thân đã trở nên cao thượng.")
#   So anattantapo aparantapo diṭṭheva dhamme nicchāto nibbuto sītībhūto sukhappaṭisaṃvedī brahmabhūtena attanā viharati.


def N(k):
    return NAME[k]


def build_ekaka():
    q, cd, cs = q_katamo, close_dash, close_sentence
    S = [seg(H_NIDDESO + " ^4-1-0"), seg(H_CHAPTER[1] + " ^4-1-1-0")]
    a = []
    a.append((f"{q(N('samayavimutto'))} {IDHEKACCO} {KALENA_SAMAYENA}, "
              + VIMOKKHA.replace("chạm đến", "chạm đến [khác chính tả (Sī., Pī.): phassitvā]", 1)
              + f", và {DISVA_EKACCE} {cd(N('samayavimutto'))}", "^4-1"))
    a.append((f"{q(N('asamayavimutto'))} {IDHEKACCO} {NA_HEVA_KHO} {KALENA_SAMAYENA}, {VIMOKKHA}, "
              f"và {DISVA_SABBE} {cd(N('asamayavimutto'))} "
              + SABBEPI.format("được giải thoát không theo từng thời điểm"), "^4-2"))
    a.append((f"{q(N('kuppadhammo'))} {LABHI} {NA_NIKAMA} {THANA} {KUPPEYYUM} {cd(N('kuppadhammo'))}", "^4-3"))
    a.append((f"{q(N('akuppadhammo'))} {LABHI} {NIKAMA} {ATTHANA} {KUPPEYYUM} {cd(N('akuppadhammo'))} "
              + SABBEPI.format("không thể bị lay chuyển"), "^4-4"))
    a.append((f"{q(N('parihānadhammo'))} {LABHI} {NA_NIKAMA} {THANA} {PARIHAYEYYA} {cd(N('parihānadhammo'))}",
              "^4-5"))
    a.append((f"{q(N('aparihānadhammo'))} {LABHI} {NIKAMA} {ATTHANA} {PARIHAYEYYA} {cd(N('aparihānadhammo'))} "
              + SABBEPI.format("không thể bị sa sút"), "^4-6"))
    a.append((f"{q(N('cetanābhabbo'))} {LABHI} {NA_NIKAMA} Nếu người ấy luôn hướng chủ ý đến chúng, {NA_PARIHAYATI}. "
              f"Nếu người ấy không luôn hướng chủ ý đến chúng, {PARIHAYATI} {cd(N('cetanābhabbo'))}", "^4-7"))
    a.append((f"{q(N('anurakkhaṇābhabbo'))} {LABHI} {NA_NIKAMA} Nếu người ấy gìn giữ chúng, {NA_PARIHAYATI}. "
              f"Nếu người ấy không gìn giữ chúng, {PARIHAYATI} {cd(N('anurakkhaṇābhabbo'))}", "^4-8"))
    a.append((f"{q(N('puthujjano'))} Người nào có ba xiềng xích chưa được dứt bỏ; và cũng không thực hành để dứt bỏ "
              f"các hiện tượng ấy {cd(N('puthujjano'))}", "^4-9"))
    a.append((f"{q(N('gotrabhū'))} Người được trang bị những hiện tượng mà liền sau chúng xảy ra sự đi vào "
              f"Giáo Pháp cao quý {cd(N('gotrabhū'))}", "^4-10"))
    a.append((f"{q(N('bhayūparato'))} Bảy người còn đang tu học và những người phàm phu giữ giới đều kiêng tránh "
              "vì sợ hãi. Bậc A-la-hán kiêng tránh không vì sợ hãi.", "^4-11"))
    a.append((f"{q(N('abhabbāgamano'))} Những người nào {AVARANA_NEG}, đần độn, không {NIYAMA} "
              f"{close_dash_pl(N('abhabbāgamano'))}", "^4-12"))
    a.append((f"{q(N('bhabbāgamano'))} Những người nào "
              + AVARANA_POS.replace("có trí tuệ", "có trí tuệ [khác chính tả (Sī.): paññavantā]", 1)
              + f", không đần độn, {NIYAMA} {close_dash_pl(N('bhabbāgamano'))}", "^4-13"))
    a.append((f"{q(N('niyato'))} Năm hạng người phạm nghiệp có quả không gián đoạn, những người có quan điểm sai lầm "
              "cố định và tám bậc thánh đều có hướng đi cố định. Những người còn lại không có hướng đi cố định.",
              "^4-14"))
    a.append((f"{q(N('paṭipannako'))} Bốn hạng người có được con đường là những người đang thực hành, bốn hạng người "
              "có được thành quả là những người đã đứng vững trong thành quả.", "^4-15"))
    a.append((f"{q(N('samasīsī'))} Người nào mà sự cạn kiệt các ô nhiễm và sự cạn kiệt sự sống xảy ra không trước "
              f"không sau {cd(N('samasīsī'))}", "^4-16"))
    a.append((f"{q(N('ṭhitakappī'))} Nếu người này đang thực hành để tự mình chứng nghiệm thành quả vào dòng, và đã "
              "đến lúc kiếp bị thiêu hủy, thì kiếp sẽ chưa bị thiêu hủy chừng nào người này chưa tự mình chứng nghiệm "
              f"thành quả vào dòng. {cs(N('ṭhitakappī'))} Tất cả những người có được con đường đều là "
              f"{N('ṭhitakappī')}.", "^4-17"))
    a.append((f"{q(N('ariyo'))} Tám bậc thánh là bậc thánh. Những người còn lại không phải là bậc thánh.", "^4-18"))
    a.append((f"{q(N('sekkho'))} Bốn hạng người có được con đường và ba hạng người có được thành quả là "
              f"“{N('sekkho')}”. Bậc A-la-hán là {N('asekkho')}. Những người còn lại không phải còn đang tu học cũng "
              "không phải đã hoàn tất tu học.", "^4-19"))
    a.append((f"{q(N('tevijjo'))} Người được trang bị ba loại hiểu biết chân thật là “{N('tevijjo')}”.", "^4-20"))
    a.append((f"{q(N('chaḷabhiñño'))} Người được trang bị sáu loại hiểu biết trực tiếp là “{N('chaḷabhiñño')}”.",
              "^4-21"))
    a.append((f"{q(N('sammāsambuddho'))} {IDHEKACCO} {ANANUSSUTA}; {SABBANNUTA} {cd(N('sammāsambuddho'))}",
              "^4-22"))
    a.append((f"{q(N('paccekasambuddho'))} {IDHEKACCO} {ANANUSSUTA}; {NA_SABBANNUTA} "
              f"{cd(N('paccekasambuddho'))}", "^4-23"))
    a.append((f"{q(N('ubhatobhāgavimutto'))} {IDHEKACCO} {VIMOKKHA}; và {DISVA_SABBE} "
              f"{cd(N('ubhatobhāgavimutto'))}", "^4-24"))
    a.append((f"{q(N('paññāvimutto'))} {IDHEKACCO} {NA_HEVA_KHO} {VIMOKKHA}; và {DISVA_SABBE}. "
              f"{cs(N('paññāvimutto'))}", "^4-25"))
    a.append((f"{q(N('kāyasakkhī'))} {IDHEKACCO} {VIMOKKHA}; và {DISVA_EKACCE}. {cs(N('kāyasakkhī'))}", "^4-26"))
    a.append((f"{q(N('diṭṭhippatto'))} {IDHEKACCO} {TRUTHS}. {TATHAGATA} {cap('và ' + DISVA_EKACCE)} "
              f"{cd(N('diṭṭhippatto'))}", "^4-27"))
    a.append((f"{q(N('saddhāvimutto'))} {IDHEKACCO} {TRUTHS}. {TATHAGATA} {cap('và ' + DISVA_EKACCE)}, "
              f"nhưng quả thật không như ở {N('diṭṭhippatto')} {cd(N('saddhāvimutto'))}", "^4-28"))
    for key, fac, idb, fruit in (("dhammānusārī", "trí tuệ", "^4-29", "diṭṭhippatto"),
                                 ("saddhānusārī", "niềm tin", "^4-30", "saddhāvimutto")):
        a.append((f"{q(N(key))} Người nào, khi {N('sotāpattiphalasacchikiriyāya paṭipanno')[6:]}, có năng lực {fac} "
                  f"vượt trội, tu tập con đường cao quý được {fac} dẫn dắt, có {fac} đi trước {cd(N(key))} "
                  f"{cap(N('sotāpattiphalasacchikiriyāya paṭipanno'))} là {N(key)}, người đã đứng vững trong thành quả "
                  f"là {N(fruit)}.", idb))
    a.append((f"{q(N('sattakkhattuparamo'))} {SOTAPANNA_INTRO} [khác chính tả (Sī., Ka.): sambodhiparāyaṇo]. "
              f"Người ấy, sau khi trôi lăn và luân chuyển bảy lần giữa chư thiên và loài người, {DUKKHASSANTA} "
              f"{cd(N('sattakkhattuparamo'))}", "^4-31"))
    a.append((f"{q(N('kolaṅkolo'))} {SOTAPANNA_INTRO}. Người ấy, sau khi trôi lăn và luân chuyển qua hai hoặc ba "
              f"gia đình, {DUKKHASSANTA} {cd(N('kolaṅkolo'))}", "^4-32"))
    a.append((f"{q(N('ekabījī'))} {SOTAPANNA_INTRO}. Người ấy, sau khi tạo ra chỉ một lần hiện hữu làm người, "
              f"{DUKKHASSANTA} {cd(N('ekabījī'))}", "^4-33"))
    a.append((f"{q(N('sakadāgāmī'))} {IDHEKACCO} nhờ diệt tận hoàn toàn ba xiềng xích và nhờ sự suy yếu của tham đắm, "
              f"sân hận và si mê mà trở thành {N('sakadāgāmī')}, và sau khi trở lại thế gian này chỉ một lần, "
              f"người ấy {DUKKHASSANTA} {cd(N('sakadāgāmī'))}", "^4-34"))
    a.append((f"{q(N('anāgāmī'))} {ANAGAMI_INTRO} {cd(N('anāgāmī'))}", "^4-35"))
    a.append((f"{q(N('antarāparinibbāyī'))} {ANAGAMI_INTRO}. Người ấy, hoặc liền sau khi tái sinh, hoặc khi chưa đến "
              f"giữa tuổi thọ, {UPARI} {cd(N('antarāparinibbāyī'))}", "^4-36"))
    a.append((f"{q(N('upahaccaparinibbāyī'))} {ANAGAMI_INTRO}. Người ấy, sau khi đã qua giữa tuổi thọ, hoặc khi gần "
              f"mạng chung [khác chính tả (Ka.): kālaṃ kiriyaṃ], {UPARI} {cd(N('upahaccaparinibbāyī'))}", "^4-37"))
    a.append((f"{q(N('asaṅkhāraparinibbāyī'))} {ANAGAMI_INTRO}. Người ấy, không có sự thúc đẩy, {UPARI} "
              f"{cd(N('asaṅkhāraparinibbāyī'))}", "^4-38"))
    a.append((f"{q(N('sasaṅkhāraparinibbāyī'))} {ANAGAMI_INTRO}. Người ấy, có sự thúc đẩy, {UPARI} "
              f"{cd(N('sasaṅkhāraparinibbāyī'))}", "^4-39"))
    a.append((f"{q(N('uddhaṃsotoakaniṭṭhagāmī'))} {ANAGAMI_INTRO}. Người ấy chết ở cõi Vô Phiền thì đi đến cõi Vô Nhiệt, "
              "chết ở cõi Vô Nhiệt thì đi đến cõi Thiện Hiện, chết ở cõi Thiện Hiện thì đi đến cõi Thiện Kiến, chết ở "
              "cõi Thiện Kiến thì đi đến cõi Sắc Cứu Cánh; tại cõi Sắc Cứu Cánh, người ấy "
              f"{UPARI} {cd(N('uddhaṃsotoakaniṭṭhagāmī'))}", "^4-40"))
    a.append((f"Thế nào là {N('sotāpanno')} và {N('sotāpattiphalasacchikiriyāya paṭipanno')}? "
              + PATIPANNO_DEF.format("dứt bỏ ba xiềng xích", "vào dòng") + " "
              + YASSA_PAHINA.format("ba xiềng xích") + f" {cd(N('sotāpanno'))}", "^4-41"))
    a.append((PATIPANNO_DEF.format(TANU, "trở lại một lần") + f" Người nào có {KAMA_BYAPADA} đã suy yếu "
              f"{cd(N('sakadāgāmī'))}", "^4-42"))
    a.append((PATIPANNO_DEF.format(ANAVASESA_KAMA, "không trở lại") + " "
              + YASSA_PAHINA.format(KAMA_BYAPADA) + f" không còn sót lại {cd(N('anāgāmī'))}", "^4-43"))
    S += [seg(t + " " + i) for t, i in a]
    S.append(seg(PATIPANNO_DEF.format(ANAVASESA_ARAHATTA, "A-la-hán") + " "
                 + YASSA_PAHINA.format(ARAHATTA_FIVE) + f" không còn sót lại {cd(N('arahā'))}",
                 CLOSER_CHAPTER[1] + " ^4-44"))
    return S


# ---------------------------------------------------------------------------------------------------------------
# Formula list (written to vi-rails-formulas.md)
# ---------------------------------------------------------------------------------------------------------------
def formulas():
    reused = {vi: b for _, vi, b in REUSED}

    def mark(vi):
        for s, b in reused.items():
            if s == vi:
                return f" (pi-{b})"
        return ""

    out = ["# pi-4 Puggalapaññatti: Vietnamese rails sentence formulas and person-type names (binding for ch3-11)", "",
           "Format: Pāli = tiếng Việt, one per line; (pi-1) / (pi-2) / (pi-3) = taken unchanged from that book's "
           "approved Vietnamese rails (asserted by the builder). Generated by build_rails_sample_vi.py: import its "
           "constants (NAME, frames, headings, closers) rather than retyping. Termbase: "
           "AI_translation/vietnamese/pi-4-pali-vietnamese-termbase-plain.md (+ pi-4-vi-ai/termbase/APPROVED.md). "
           "Style: 0-INBOX/temp/pipeline/vietnamese-style.md.", "",
           "## Book frame and headings", ""]
    F = [("Namo tassa bhagavato arahato sammāsambuddhassa", HOMAGE), ("# Abhidhammapiṭake", H_ABHI),
         ("## Puggalapaññattipāḷi", H_BOOK), ("Puggalapaññatti (book title mid-sentence)", "“" + BOOK_TITLE + "”"),
         ("Colophon (end of ch11)", COLOPHON), ("### Mātikā", H_MATIKA), ("### Niddeso", H_NIDDESO)]
    for n in NUM:
        F.append((f"#### {GROUP_PALI[n]}uddeso", H_UDDESO[n]))
    for n in NUM:
        F.append((f"{GROUP_PALI[n]}ṃ. (matrix group closer)".replace("aṃ.", "aṃ."), CLOSER_MATRIX[n]))
    for n in NUM:
        F.append((f"#### {GROUP_PALI[n]}puggalapaññatti", H_CHAPTER[n]))
    for n in NUM:
        F.append((f"{GROUP_PALI[n]}niddeso. (chapter closer)", CLOSER_CHAPTER[n]))
    for n in range(2, 11):
        F.append((["", "", "Dve", "Tayo", "Cattāro", "Pañca", "Cha", "Satta", "Aṭṭha", "Nava", "Dasa"][n]
                  + " puggalā – (group opener)", GROUP_OPEN[n]))
    F.append(("Puggalapaññattimātikā niṭṭhitā.", MATIKA_END))
    out += [f"{p} = {v}{mark(v)}" for p, v in F]
    out += ["", "## Sentence frames", ""]
    F = [("Kittāvatā X-ānaṃ X-paññatti?", kittavata("{X}")),
         ("Yāvatā N X – …; ettāvatā X-ānaṃ X-paññatti.", yavata_ettavata("{X}", "{N X} – …")),
         ("X (designation): khandha / āyatana / dhātu / sacca / indriya / puggala", " / ".join(DESIG.values())),
         ("X-paññatti (list member, ^4-M-1)", "sự định danh về {X}"),
         ("Cha paññattiyo – …", "Có sáu sự định danh – …"),
         ("Katamo ca puggalo X?", q_katamo("{X}")),
         ("Idhekacco puggalo …", IDHEKACCO + " …"),
         ("Atthekacco puggalo … (matrix clauses, definitions)", "có người … (Có người … at a line start)"),
         ("– ayaṃ vuccati puggalo “X”.", close_dash("{X}")),
         ("Ayaṃ vuccati puggalo “X”. (no dash in the Pāli)", close_sentence("{X}")),
         ("– ime vuccanti puggalā “X”.", close_dash_pl("{X}")),
         ("Kathañca puggalo X hoti?", q_kathanca("{X}")),
         ("Evaṃ puggalo X hoti.", evam("{X}")),
         ("questions about persons / about things", "… là những ai? / … là gì?"),
         ("puggalā (counted: dve / tayo … puggalā; dvinnaṃ puggalānaṃ)", "hạng người"),
         ("Yassa puggalassa …", "Người nào …"),
         ("Ye te puggalā …", "Những người nào …"),
         ("Avasesā puggalā", "Những người còn lại"),
         ("X ca, Y ca. (matrix pair)", "X và Y."),
         ("Sabbepi ariyapuggalā ariye vimokkhe X-ā.", SABBEPI.format("X")),
         ("So …", "Người ấy …"),
         ("tassa puggalassa / so puggalo", "của người ấy / người ấy"),
         ("ayaṃ puggalo (ṭhitakappī)", "người này")]
    out += [f"{p} = {v}{mark(v)}" for p, v in F]
    out += ["", "## Matrix lists (^4-M-1 .. ^4-M-6)", ""]
    F = [("pañcakkhandhā / dvādasāyatanāni / aṭṭhārasa dhātuyo / cattāri saccāni / bāvīsatindriyāni (counted)",
          " / ".join(COUNT.values())),
         ("rūpakkhandho, vedanākkhandho, saññākkhandho, saṅkhārakkhandho, viññāṇakkhandho", KHANDHA_LIST),
         ("cakkhāyatanaṃ … dhammāyatanaṃ", AYATANA_LIST),
         ("cakkhudhātu … manoviññāṇadhātu", DHATU_LIST),
         ("dukkhasaccaṃ, samudayasaccaṃ, nirodhasaccaṃ, maggasaccaṃ", SACCA_LIST),
         ("cakkhundriyaṃ … aññātāvindriyaṃ", INDRIYA_LIST)]
    for p, v in F:
        m = mark(v)
        if not m and v == INDRIYA_LIST:
            m = " (pi-2, from «năng lực tai»; «năng lực mắt» (pi-2) heads it)"
        if not m and v == SACCA_LIST:
            m = " (items «sự thật về khổ đau», «sự thật về sự phát sinh» (pi-2); all four as pi-3 formulas)"
        if not m and v == " / ".join(COUNT.values()):
            m = " (pi-3)"
        out.append(f"{p} = {v}{m}")
    out += ["", "## Fixed strings of the definitions (ch2; reuse wherever the Pāli repeats)", ""]
    F = [("kālena kālaṃ samayena samayaṃ", KALENA_SAMAYENA),
         ("aṭṭha vimokkhe kāyena phusitvā viharati", VIMOKKHA),
         ("na heva kho …", NA_HEVA_KHO + " …"),
         ("paññāya cassa disvā ekacce āsavā parikkhīṇā honti", DISVA_EKACCE),
         ("paññāya cassa disvā āsavā parikkhīṇā honti", DISVA_SABBE),
         ("Idhekacco puggalo lābhī hoti rūpasahagatānaṃ vā arūpasahagatānaṃ vā samāpattīnaṃ.", LABHI),
         ("So ca kho na nikāmalābhī hoti na akicchalābhī na akasiralābhī; na yatthicchakaṃ yadicchakaṃ "
          "yāvaticchakaṃ samāpajjatipi vuṭṭhātipi.", NA_NIKAMA),
         ("So ca kho nikāmalābhī hoti akicchalābhī akasiralābhī; yatthicchakaṃ yadicchakaṃ yāvaticchakaṃ "
          "samāpajjatipi vuṭṭhātipi.", NIKAMA),
         ("Ṭhānaṃ kho panetaṃ vijjati, yaṃ …", THANA + " …"),
         ("Aṭṭhānametaṃ anavakāso yaṃ …", ATTHANA + " …"),
         ("tassa puggalassa pamādamāgamma tā samāpattiyo kuppeyyuṃ", KUPPEYYUM),
         ("so puggalo pamādamāgamma tāhi samāpattīhi parihāyeyya", PARIHAYEYYA),
         ("(na) parihāyati tāhi samāpattīhi", NA_PARIHAYATI + " / " + PARIHAYATI),
         ("Sace (na) anusañceteti, …", "Nếu người ấy (không) luôn hướng chủ ý đến chúng, …"),
         ("Sace (na) anurakkhati, …", "Nếu người ấy (không) gìn giữ chúng, …"),
         ("kammāvaraṇena samannāgatā, kilesāvaraṇena …, vipākāvaraṇena …, assaddhā acchandikā duppaññā",
          AVARANA_NEG),
         ("na kammāvaraṇena samannāgatā, … saddhā chandikā paññavanto", AVARANA_POS),
         ("eḷā / aneḷā", "đần độn / không đần độn"),
         ("(a)bhabbā niyāmaṃ okkamituṃ kusalesu dhammesu sammattaṃ", "(không) " + NIYAMA),
         ("pubbe ananussutesu dhammesu sāmaṃ saccāni (an)abhisambujjhati", "(không) " + ANANUSSUTA),
         ("tattha ca sabbaññutaṃ pāpuṇāti, balesu ca vasībhāvaṃ", SABBANNUTA),
         ("na ca tattha sabbaññutaṃ pāpuṇāti, na ca balesu vasībhāvaṃ", NA_SABBANNUTA),
         ("\"idaṃ dukkha\"nti yathābhūtaṃ pajānāti, … paṭipadā\"ti yathābhūtaṃ pajānāti", TRUTHS),
         ("Tathāgatappaveditā cassa dhammā paññāya vodiṭṭhā honti vocaritā.", TATHAGATA),
         ("no ca kho yathā diṭṭhippattassa", "nhưng quả thật không như ở " + NAME["diṭṭhippatto"]),
         ("paññāvāhiṃ paññāpubbaṅgamaṃ ariyamaggaṃ bhāveti",
          "tu tập con đường cao quý được trí tuệ dẫn dắt, có trí tuệ đi trước"),
         ("X phale ṭhito Y", "người đã đứng vững trong thành quả là Y"),
         ("tiṇṇaṃ saṃyojanānaṃ parikkhayā sotāpanno hoti avinipātadhammo niyato sambodhiparāyano",
          SOTAPANNA_INTRO.replace(IDHEKACCO + " ", "")),
         ("sattakkhattuṃ deve ca mānuse ca sandhāvitvā saṃsaritvā",
          "sau khi trôi lăn và luân chuyển bảy lần giữa chư thiên và loài người"),
         ("dukkhassantaṃ karoti", DUKKHASSANTA),
         ("dukkhassantakaro hoti", "trở thành người " + DUKKHASSANTA),
         ("rāgadosamohānaṃ tanuttā", "nhờ sự suy yếu của tham đắm, sân hận và si mê"),
         ("sakideva imaṃ lokaṃ āgantvā", "sau khi trở lại thế gian này chỉ một lần"),
         ("pañcannaṃ orambhāgiyānaṃ saṃyojanānaṃ parikkhayā opapātiko hoti, tattha parinibbāyī anāvattidhammo "
          "tasmā lokā", ANAGAMI_INTRO.replace(IDHEKACCO + " ", "")),
         ("ariyamaggaṃ sañjaneti upariṭṭhimānaṃ saṃyojanānaṃ pahānāya", UPARI),
         ("upapannaṃ vā samanantarā appattaṃ vā vemajjhaṃ āyuppamāṇaṃ",
          "hoặc liền sau khi tái sinh, hoặc khi chưa đến giữa tuổi thọ"),
         ("atikkamitvā vemajjhaṃ āyuppamāṇaṃ upahacca vā kālakiriyaṃ",
          "sau khi đã qua giữa tuổi thọ, hoặc khi gần mạng chung"),
         ("asaṅkhārena / sasaṅkhārena", "không có sự thúc đẩy / có sự thúc đẩy"),
         ("avihā / atappā / sudassā / sudassī / akaniṭṭha", "cõi Vô Phiền / cõi Vô Nhiệt / cõi Thiện Hiện / "
          "cõi Thiện Kiến (pi-2 «Thiện Kiến») / cõi Sắc Cứu Cánh"),
         ("X cuto Y gacchati", "chết ở X thì đi đến Y"),
         ("X-pahānāya paṭipanno puggalo Y-phalasacchikiriyāya paṭipanno.", PATIPANNO_DEF.format("X", "Y")),
         ("Yassa puggalassa X pahīnā(ni)", YASSA_PAHINA.format("X")),
         ("tīṇi saṃyojanāni (ap)pahīnāni", "ba xiềng xích đã được dứt bỏ / chưa được dứt bỏ"),
         ("kāmarāgabyāpādānaṃ tanubhāvāya", "để " + TANU),
         ("kāmarāgabyāpādānaṃ anavasesappahānāya", "để " + ANAVASESA_KAMA),
         ("rūparāgaarūparāgamānauddhaccaavijjāya anavasesappahānāya", "để " + ANAVASESA_ARAHATTA),
         ("kāmarāgabyāpādā tanubhūtā / anavasesā pahīnā",
          KAMA_BYAPADA + " đã suy yếu / đã được dứt bỏ không còn sót lại"),
         ("apubbaṃ acarimaṃ", "không trước không sau"),
         ("āsavapariyādānañca … jīvitapariyādānañca", "sự cạn kiệt các ô nhiễm và sự cạn kiệt sự sống"),
         ("Pañca puggalā ānantarikā", "Năm hạng người phạm nghiệp có quả không gián đoạn"),
         ("micchādiṭṭhikā niyatā", "những người có quan điểm sai lầm cố định"),
         ("maggasamaṅgino / phalasamaṅgino puggalā", "những (hạng) người có được con đường / có được thành quả"),
         ("Tīhi vijjāhi / Chahi abhiññāhi samannāgato puggalo",
          "Người được trang bị ba loại hiểu biết chân thật / sáu loại hiểu biết trực tiếp"),
         ("diṭṭheva dhamme / diṭṭhe ceva dhamme", DITTHE_DHAMME),
         ("pāpakā akusalā dhammā", PAPAKA_AKUSALA),
         ("cetovimuttiṃ paññāvimuttiṃ", CETOVIMUTTI),
         ("tiṇṇo pāraṅgato thale tiṭṭhati brāhmaṇo", TINNO),
         ("bhūtaṃ tacchaṃ kālena", BTK),
         ("ananuvicca apariyogāhetvā / anuvicca pariyogāhetvā", _NA_ANU + " / " + _ANU),
         ("vaṇṇārahassa vaṇṇaṃ / avaṇṇārahassa avaṇṇaṃ bhāsitā hoti", VANNA_OK + " / " + AVANNA_OK),
         ("avaṇṇārahassa vaṇṇaṃ / vaṇṇārahassa avaṇṇaṃ bhāsitā hoti", VANNA_BAD + " / " + AVANNA_BAD),
         ("pasādanīye / appasādanīye ṭhāne pasādaṃ upadaṃsitā hoti", PASADA_OK + " / " + PASADA_BAD),
         ("appasādanīye / pasādanīye ṭhāne appasādaṃ upadaṃsitā hoti", APPASADA_OK + " / " + APPASADA_BAD),
         ("attahitāya / parahitāya", _ATTA + " / " + _PARA),
         ("ajjhattaṃ cetosamathassa / adhipaññādhammavipassanāya", _SAMATHA + " / " + _VIPASSANA),
         ("a. ni. N.N (citation in a variant note)", "Tăng Chi Bộ Kinh N.N"),
         ("…pe…", "… (same spot; never «….»)"),
         ("[word (sī. syā.)] spelling only", "[khác chính tả (Sī., Syā.): word]"),
         ("[word (sī.)] other word", "[dị bản (Sī.): word]"),
         ("– (Pāli dash)", "– (same spot, same count; never added)")]
    for p, v in F:
        out.append(f"{p} = {v}{mark(v)}")
    out += ["", "## Person-type names of the matrix (NAME[pali]; use verbatim in ch3-11: matrix, «Thế nào là X?», "
            "quoted “X”)", ""]
    for title, grp in (("Ekaka (^4-M-7)", None), ("Duka (^4-M-8)", DUKA), ("Tika (^4-M-9)", TIKA),
                       ("Catukka (^4-M-10)", CATUKKA), ("Pañcaka (^4-M-11)", PANCAKA), ("Chakka (^4-M-12)", CHAKKA),
                       ("Sattaka (^4-M-13)", SATTAKA), ("Aṭṭhaka (^4-M-14)", AṬṬHAKA), ("Navaka (^4-M-15)", NAVAKA),
                       ("Dasaka (^4-M-16)", DASAKA)):
        out += [f"### {title}", ""]
        if grp is None:
            for i, (k, v) in enumerate(EKAKA, 1):
                out.append(f"({i}) {k.split('#')[0]} = {v}{mark(v)}")
        else:
            for n, items in grp:
                for k, v in items:
                    v = v if v is not None else NAME[k]
                    k = k.split("#")[0]
                    if k.startswith(("na ", "sevitabbo", "sakkatvā", "jigucchitabbo", "ajjhupekkhitabbo", "sīlesu",
                                     "kāmesu", "ananuvicca", "anuvicca", "avaṇṇārahassa", "vaṇṇārahassa", "neva ",
                                     "attahitāya", "parahitāya", "attantapo", "parantapo", "lābhī", "ārabhati",
                                     "nārabhati", "…")):
                        k = "atthekacco puggalo " + k
                    out.append(f"({n}) {k} = {v}{mark(v)}")
        out.append("")
    out += ["Head nouns: «người» by default; «bậc» for ariyo, the four fruit holders (sotāpanno, sakadāgāmī, anāgāmī, "
            "arahā) and the two Buddhas (termbase); samaṇa types «vị sa-môn»; counted types «N hạng người»; "
            "«có người …» for the atthekacco clauses (capitalised at a line start, unchanged in the quoted name).",
            "Variant notes kept with the names in the matrix: paḷāsī [khác chính tả (Syā., Ka.): palāsī]; "
            "paccekasambuddho [dị bản (Sī.): paccekabuddho]; ucchaṅgapañño [khác chính tả (Syā.): uccaṅgupañño]; "
            "vipañcitaññū [khác chính tả (Sī.): vipacitaññū; Tăng Chi Bộ Kinh 4.133]; appavajjo [dị bản (Syā., Ka.): "
            "appasāvajjo; Tăng Chi Bộ Kinh 4.135]; balībaddūpamā [khác chính tả (Sī.): balibaddūpamā].", ""]
    return "\n".join(out)


# ---------------------------------------------------------------------------------------------------------------
def check_reused():
    texts = {}
    for b, d in RAILS.items():
        texts[b] = unicodedata.normalize("NFC", "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md"))))
    # case-insensitive: a reused string may stand at a sentence start in one book and mid-sentence in the other
    bad = [(p, v, b) for p, v, b in REUSED if unicodedata.normalize("NFC", v).lower() not in texts[b].lower()]
    assert not bad, "reused strings not found in their rails: " + repr(bad)


def write(path, segs):
    text = unicodedata.normalize("NFC", "\n\n".join(segs) + "\n")
    assert "\n\n\n" not in text and "—" not in text and ":-" not in text and "…." not in text, path
    path.write_text(text, encoding="utf-8", newline="\n")
    print("wrote", path)


def main():
    check_reused()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    write(OUT_DIR / "preamble.md", build_preamble())
    write(OUT_DIR / "1-matika.md", build_matika())
    write(OUT_DIR / "2-ekakapuggalapannatti.md", build_ekaka())
    FORMULAS_MD.write_text(unicodedata.normalize("NFC", formulas()), encoding="utf-8", newline="\n")
    print("wrote", FORMULAS_MD)


if __name__ == "__main__":
    main()
