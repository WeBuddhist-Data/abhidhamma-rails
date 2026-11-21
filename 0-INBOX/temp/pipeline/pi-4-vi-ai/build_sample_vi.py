# -*- coding: utf-8 -*-
"""pi-4 (Puggalapaññatti) Vietnamese zero-shot SAMPLE builder: preamble, 1-matika.md, 2-ekakapuggalapannatti.md.

Fixed formula strings are module constants. Chapter agents (ch3-11) import this module and use the person
names, frames, headings and closers VERBATIM:

    import sys; sys.path.insert(0, r"D:\\Work\\OpenPecha\\abhidhamma-rails\\0-INBOX\\temp\\pipeline\\pi-4-vi-ai")
    import build_sample_vi as S
    S.q(S.NAME["kodhano"]); S.close(S.NAME["kodhano"]); S.CHAPTER_HEADING[3]; S.NIDDESA_CLOSER[2] ...

Importing does not write anything; run  python -I -X utf8 build_sample_vi.py  to rebuild the three files.
At build time every string claimed from pi-1 / pi-2 / pi-3 (CROSS_BOOK) is asserted to occur in those rails files.
Names are stored lowercase (except proper words); at the start of a list item or sentence the first letter is
capitalised with cap(), nothing else changes.
"""
import pathlib
import re
import unicodedata

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
PALI_DIR = ROOT / "AI_translation/pali/pi-4_split_chapters"
OUT_DIR = ROOT / "AI_translation/vietnamese/pi-4-vietnamese-plain-zeroshot_split_chapters"
RAILS_DIR = {b: ROOT / f"AI_translation/vietnamese/pi-{b}-vietnamese-plain-rails_split_chapters" for b in (1, 2, 3)}


def cap(s):
    return s[:1].upper() + s[1:]


# ---------------------------------------------------------------- book frame
HOMAGE = "Kính lễ Đức Thế Tôn, bậc A-la-hán, bậc Tự Giác Ngộ Hoàn Toàn"          # pi-1/2/3 ^T-1
PITAKA = "Tạng Vi Diệu Pháp"                                                      # pi-1/2/3 ^0
BOOK_TITLE = "Định danh các hạng người"                                           # new (Puggalapaññattipāḷi)
BOOK_TITLE_ALTERNATIVES = ("Mô tả các hạng người", "Phân định các hạng người")
PANNATTI = "sự định danh"          # paññatti, designation sense (pi-1 «khái niệm» is the 'concept' sense)
PUGGALA = "người"                  # puggala (core term)
PUGGALA_TYPES = "hạng người"       # puggalā counted as types: «Hai hạng người –», «các hạng người»
MATIKA_END = "Ma trận của bộ “Định danh các hạng người” đã hoàn tất."           # Puggalapaññattimātikā niṭṭhitā.
BOOK_END = "Bộ “Định danh các hạng người” đã hoàn tất."                         # Puggalapaññattipakaraṇaṃ niṭṭhitaṃ. (ch11)

# ---------------------------------------------------------------- headings and closers
NUM = {1: "một", 2: "hai", 3: "ba", 4: "bốn", 5: "năm", 6: "sáu", 7: "bảy", 8: "tám", 9: "chín", 10: "mười"}
MATIKA = "Ma trận"                                                                  # Mātikā (pi-1)
UDDESA_HEADING = {n: f"Phần nêu đề mục theo nhóm {NUM[n]}" for n in NUM}          # Ekakauddeso … Dasakauddeso
NIDDESO = "Phần giải thích"                                                         # ### Niddeso
CHAPTER_HEADING = {n + 1: f"Định danh các hạng người theo nhóm {NUM[n]}" for n in NUM}  # ch2 Ekaka… ch11 Dasaka-puggalapaññatti
MATIKA_GROUP_CLOSER = {n: f"Phân loại theo nhóm {NUM[n]}." for n in NUM}           # Ekakaṃ. … Dasakaṃ. (pi-1)
NIDDESA_CLOSER = {n: f"Giải thích phân loại theo nhóm {NUM[n]}." for n in NUM}     # Ekakaniddeso. … Dasakaniddeso. (pi-1/pi-2)
GROUP_OPENER = {n: f"{cap(NUM[n])} hạng người –" for n in range(2, 11)}            # Dve / Tayo … Dasa puggalā –
TYPES_COUNT = {n: f"{cap(NUM[n])} hạng người" for n in range(2, 11)}              # «Ba hạng người giống như …»

# ---------------------------------------------------------------- frames
DESIGNATION_Q = "Sự định danh về {x} bao quát đến mức nào?"                       # Kittāvatā X-ānaṃ X-paññatti?
DESIGNATION_A = "Bao quát {n} – {items}; sự định danh về {x} bao quát đến mức ấy."  # Yāvatā N – …; ettāvatā …
DEF_Q = "Thế nào là {name}?"                       # Katamo ca puggalo X?
IDHEKACCO = "Ở đời này, có người"                  # Idhekacco (puggalo) (pi-1 ^1-1351 …)
ATTHEKACCO = "có người"                            # Atthekacco puggalo (pi-2 «có người hành thiền»)
DEF_CLOSE = "– người này được gọi là “{name}”."     # – ayaṃ vuccati puggalo "X".
DEF_CLOSE_NODASH = "Người này được gọi là “{name}”."  # Ayaṃ vuccati puggalo "X". (no dash in the Pāli)
DEF_CLOSE_PL = "– những người này được gọi là “{name}”."  # – ime vuccanti puggalā "X".
TATTHA_Q = "Ở đây, {x} là gì?"                     # Tattha katamo/katamā/katamaṃ X? (pi-1 / pi-2)
THING_CLOSE = "– đó được gọi là {x}."              # – ayaṃ / idaṃ vuccati X (noun, no quotes in the Pāli; pi-1)
SAMANNAGATO = "được trang bị"                      # samannāgato (pi-2); for āvaraṇa / bad states pi-2 uses «mang»
TINNO = "đã vượt qua, đã đến bờ bên kia, đứng trên đất liền"   # tiṇṇo pāraṅgato thale tiṭṭhati
DITTHEVA_DHAMME = "ngay trong đời này"             # diṭṭheva dhamme (pi-2)
DUKKHASSANTAKARO = "người đi đến tận cùng của khổ đau"   # dukkhassantakaro; dukkhassantaṃ karoti = «đi đến tận cùng của khổ đau»


def q(name):
    return DEF_Q.format(name=name)


def close(name, dash=True):
    return DEF_CLOSE.format(name=name) if dash else DEF_CLOSE_NODASH.format(name=name)


def close_pl(name):
    return DEF_CLOSE_PL.format(name=name)


def designation(x, n, items):
    return DESIGNATION_Q.format(x=x) + " " + DESIGNATION_A.format(x=x, n=n, items=items)


# ---------------------------------------------------------------- person names (every matrix person type)
EKAKA = [  # matrix ^4-M-7, in order; ch2 defines them
    ("samayavimutto", "người được giải thoát theo thời điểm"),
    ("asamayavimutto", "người được giải thoát không theo thời điểm"),
    ("kuppadhammo", "người có thể bị lay chuyển"),
    ("akuppadhammo", "người không thể bị lay chuyển"),
    ("parihānadhammo", "người có thể bị sa sút"),
    ("aparihānadhammo", "người không thể bị sa sút"),
    ("cetanābhabbo", "người có khả năng giữ vững nhờ chủ ý"),
    ("anurakkhaṇābhabbo", "người có khả năng giữ vững nhờ sự gìn giữ"),
    ("puthujjano", "người phàm phu"),
    ("gotrabhū", "người chuyển đổi dòng dõi"),
    ("bhayūparato", "người kiêng tránh vì sợ hãi"),
    ("abhayūparato", "người kiêng tránh không vì sợ hãi"),
    ("bhabbāgamano", "người có khả năng tiến bước"),
    ("abhabbāgamano", "người không có khả năng tiến bước"),
    ("niyato", "người có hướng đi cố định"),
    ("aniyato", "người có hướng đi không cố định"),
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
    ("ekabījī", "người chỉ còn một hạt giống"),
    ("sakadāgāmī", "bậc trở lại một lần"),
    ("anāgāmī", "bậc không trở lại"),
    ("antarāparinibbāyī", "bậc nhập Niết-bàn trọn vẹn trong khoảng giữa"),
    ("upahaccaparinibbāyī", "bậc nhập Niết-bàn trọn vẹn khi gần mạng chung"),
    ("asaṅkhāraparinibbāyī", "bậc nhập Niết-bàn trọn vẹn không có sự thúc đẩy"),
    ("sasaṅkhāraparinibbāyī", "bậc nhập Niết-bàn trọn vẹn có sự thúc đẩy"),
    ("uddhaṃsotoakaniṭṭhagāmī", "bậc ngược dòng đi đến cõi Sắc Cứu Cánh"),
    ("sotāpanno", "bậc vào dòng"),
    ("sotāpattiphalasacchikiriyāya paṭipanno", "người đang thực hành để tự mình chứng nghiệm thành quả vào dòng"),
    ("sakadāgāmī", "bậc trở lại một lần"),
    ("sakadāgāmiphalasacchikiriyāya paṭipanno", "người đang thực hành để tự mình chứng nghiệm thành quả trở lại một lần"),
    ("anāgāmī", "bậc không trở lại"),
    ("anāgāmiphalasacchikiriyāya paṭipanno", "người đang thực hành để tự mình chứng nghiệm thành quả không trở lại"),
    ("arahā", "bậc A-la-hán"),
    ("arahattaphalasacchikiriyāya paṭipanno", "người đang thực hành để tự mình chứng nghiệm thành quả A-la-hán"),
]
EKAKA_VARIANT = {29: " [dị bản (Sī.): paccekabuddho]", 54: " [dị bản (Sī.): arahattāya]"}

# plural forms used in the definitions' quotes (ime vuccanti puggalā "…", "sekkhā")
PLURAL = {
    "abhabbāgamanā": "những người không có khả năng tiến bước",
    "bhabbāgamanā": "những người có khả năng tiến bước",
    "sekkhā": "những người còn đang tu học",
}

DUKA = [  # matrix ^4-M-8; ch3 defines them. tuple = pair «A và B.», str = whole item
    ("kodhano", "người giận dữ", "upanāhī", "người ôm hận"),
    ("makkhī", "người gièm pha", "paḷāsī", "người ganh đua"),
    ("issukī", "người ganh tị", "maccharī", "người keo kiệt"),
    ("saṭho", "người gian xảo", "māyāvī", "người xảo trá"),
    ("ahiriko", "người không biết hổ thẹn", "anottappī", "người không biết ghê sợ tội lỗi"),
    ("dubbaco", "người khó dạy bảo", "pāpamitto", "người kết bạn với người xấu"),
    ("indriyesu aguttadvāro", "người không phòng hộ cửa các giác quan",
     "bhojane amattaññū", "người không biết tiết độ trong ăn uống"),
    ("muṭṭhassati", "người mất tỉnh thức", "asampajāno", "người thiếu hiểu biết rõ ràng"),
    ("sīlavipanno", "người suy đồi về giới hạnh", "diṭṭhivipanno", "người suy đồi về quan điểm"),
    ("ajjhattasaṃyojano", "người có xiềng xích ở nơi bản thân",
     "bahiddhāsaṃyojano", "người có xiềng xích ở bên ngoài bản thân"),
    ("akkodhano", "người không giận dữ", "anupanāhī", "người không ôm hận"),
    ("amakkhī", "người không gièm pha", "apaḷāsī", "người không ganh đua"),
    ("anissukī", "người không ganh tị", "amaccharī", "người không keo kiệt"),
    ("asaṭho", "người không gian xảo", "amāyāvī", "người không xảo trá"),
    ("hirimā", "người biết hổ thẹn", "ottappī", "người biết ghê sợ tội lỗi"),
    ("suvaco", "người dễ dạy bảo", "kalyāṇamitto", "người kết bạn với người tốt"),
    ("indriyesu guttadvāro", "người phòng hộ cửa các giác quan",
     "bhojane mattaññū", "người biết tiết độ trong ăn uống"),
    ("upaṭṭhitassati", "người có sự tỉnh thức được thiết lập", "sampajāno", "người có hiểu biết rõ ràng"),
    ("sīlasampanno", "người thành tựu về giới hạnh", "diṭṭhisampanno", "người thành tựu về quan điểm"),
    "Hai hạng người khó tìm gặp trong thế gian.",
    "Hai hạng người khó làm cho thỏa mãn.",
    "Hai hạng người dễ làm cho thỏa mãn.",
    "Các ô nhiễm của hai hạng người tăng trưởng.",
    "Các ô nhiễm của hai hạng người không tăng trưởng.",
    ("hīnādhimutto", "người có chí hướng thấp kém", "paṇītādhimutto", "người có chí hướng ưu việt"),
    ("titto", "người đã thỏa mãn", "tappetā", "người làm cho người khác thỏa mãn"),
]
DUKA_VARIANT = {2: " [khác chính tả (Syā., Ka.): palāsī]"}

# names of the Tika … Dasaka lists (key = Pāli as the definition question names it)
TIKA_NAMES = {
    "nirāso": "người không mong cầu", "āsaṃso": "người có mong cầu", "vigatāso": "người đã lìa mong cầu",
    "gūthabhāṇī": "người nói lời như phân", "pupphabhāṇī": "người nói lời như hoa",
    "madhubhāṇī": "người nói lời như mật",
    "arukūpamacitto": "người có tâm giống như vết thương lở loét",
    "vijjūpamacitto": "người có tâm giống như tia chớp", "vajirūpamacitto": "người có tâm giống như kim cương",
    "andho": "người mù", "ekacakkhu": "người một mắt", "dvicakkhu": "người hai mắt",
    "avakujjapañño": "người có trí tuệ úp ngược", "ucchaṅgapañño": "người có trí tuệ như vạt áo",
    "puthupañño": "người có trí tuệ rộng lớn",
    "pāsāṇalekhūpamo": "người giống như đường vạch trên đá",
    "pathavilekhūpamo": "người giống như đường vạch trên đất",
    "udakalekhūpamo": "người giống như đường vạch trên nước",
    "suppameyyo": "người dễ đo lường", "duppameyyo": "người khó đo lường", "appameyyo": "người không thể đo lường",
}
CATUKKA_NAMES = {
    "asappuriso": "người không chân chính",
    "asappurisena asappurisataro": "người không chân chính hơn cả người không chân chính",
    "sappuriso": "người chân chính", "sappurisena sappurisataro": "người chân chính hơn cả người chân chính",
    "pāpo": "người xấu", "pāpena pāpataro": "người xấu hơn cả người xấu",
    "kalyāṇo": "người tốt", "kalyāṇena kalyāṇataro": "người tốt hơn cả người tốt",
    "pāpadhammo": "người có phẩm chất xấu",
    "pāpadhammena pāpadhammataro": "người có phẩm chất xấu hơn cả người có phẩm chất xấu",
    "kalyāṇadhammo": "người có phẩm chất tốt",
    "kalyāṇadhammena kalyāṇadhammataro": "người có phẩm chất tốt hơn cả người có phẩm chất tốt",
    "sāvajjo": "người có lỗi", "vajjabahulo": "người nhiều lỗi", "appavajjo": "người ít lỗi",
    "anavajjo": "người không có lỗi",
    "ugghaṭitaññū": "người hiểu ngay khi vừa được nêu ra",
    "vipañcitaññū": "người hiểu khi được giải thích chi tiết",
    "neyyo": "người cần được dẫn dắt", "padaparamo": "người chỉ dừng lại ở câu chữ",
    "yuttappaṭibhāno no muttappaṭibhāno": "người có tài ứng đáp xác đáng nhưng không lưu loát",
    "muttappaṭibhāno no yuttappaṭibhāno": "người có tài ứng đáp lưu loát nhưng không xác đáng",
    "yuttappaṭibhāno ca muttappaṭibhāno ca": "người có tài ứng đáp vừa xác đáng vừa lưu loát",
    "neva yuttappaṭibhāno no muttappaṭibhāno": "người có tài ứng đáp không xác đáng cũng không lưu loát",
    "uṭṭhānaphalūpajīvī no puññaphalūpajīvī":
        "người sống nhờ thành quả của công sức chứ không nhờ thành quả của phước",
    "puññaphalūpajīvī no uṭṭhānaphalūpajīvī":
        "người sống nhờ thành quả của phước chứ không nhờ thành quả của công sức",
    "uṭṭhānaphalūpajīvī ca puññaphalūpajīvī ca":
        "người sống nhờ cả thành quả của công sức lẫn thành quả của phước",
    "neva uṭṭhānaphalūpajīvī no puññaphalūpajīvī":
        "người không sống nhờ thành quả của công sức cũng không nhờ thành quả của phước",
    "tamo tamaparāyano": "người trong bóng tối hướng đến bóng tối",
    "tamo jotiparāyano": "người trong bóng tối hướng đến ánh sáng",
    "joti tamaparāyano": "người trong ánh sáng hướng đến bóng tối",
    "joti jotiparāyano": "người trong ánh sáng hướng đến ánh sáng",
    "oṇatoṇato": "người đang ở thấp và đi xuống thấp", "oṇatuṇṇato": "người đang ở thấp và đi lên cao",
    "uṇṇatoṇato": "người đang ở cao và đi xuống thấp", "uṇṇatuṇṇato": "người đang ở cao và đi lên cao",
    "rūpappamāṇo rūpappasanno": "người lấy hình sắc làm thước đo, có lòng tin trong sáng nhờ hình sắc",
    "ghosappamāṇo ghosappasanno": "người lấy tiếng tăm làm thước đo, có lòng tin trong sáng nhờ tiếng tăm",
    "lūkhappamāṇo lūkhappasanno": "người lấy sự đạm bạc làm thước đo, có lòng tin trong sáng nhờ sự đạm bạc",
    "dhammappamāṇo dhammappasanno": "người lấy Giáo Pháp làm thước đo, có lòng tin trong sáng nhờ Giáo Pháp",
    "sarāgo": "người có tham đắm", "sadoso": "người có sân hận", "samoho": "người có si mê",
    "samāno": "người có kiêu mạn",
    "anusotagāmī": "người đi xuôi dòng", "paṭisotagāmī": "người đi ngược dòng", "ṭhitatto": "người đứng vững",
    "tiṇṇo pāraṅgato thale tiṭṭhati brāhmaṇo": "bà-la-môn " + TINNO,
    "appassuto sutena anupapanno": "người ít học hỏi và không thành tựu nhờ điều đã học",
    "appassuto sutena upapanno": "người ít học hỏi nhưng thành tựu nhờ điều đã học",
    "bahussuto sutena anupapanno": "người học hỏi nhiều nhưng không thành tựu nhờ điều đã học",
    "bahussuto sutena upapanno": "người học hỏi nhiều và thành tựu nhờ điều đã học",
    "samaṇamacalo": "sa-môn bất động", "samaṇapadumo": "sa-môn như hoa sen hồng",
    "samaṇapuṇḍarīko": "sa-môn như hoa sen trắng", "samaṇesu samaṇasukhumālo": "sa-môn tinh tế giữa các sa-môn",
}
PANCAKA_NAMES = {
    "datvā avajānāti": "người cho rồi lại khinh thường", "saṃvāsena avajānāti": "người khinh thường vì sống chung",
    "ādheyyamukho": "người cả tin", "lolo": "người không kiên định", "mando momūho": "người chậm hiểu và mê muội",
    "piṇḍapātiko": "người chỉ ăn thức ăn khất thực",
    "khalupacchābhattiko": "người không nhận thức ăn dâng sau bữa",
    "ekāsaniko": "người chỉ ăn một lần ngồi", "paṃsukūliko": "người mặc y may từ vải bỏ đi",
    "tecīvariko": "người chỉ dùng ba y", "āraññiko": "người sống trong rừng",
    "rukkhamūliko": "người sống dưới gốc cây", "abbhokāsiko": "người sống ngoài trời",
    "nesajjiko": "người chỉ ngồi, không nằm", "yathāsanthatiko": "người ở bất cứ chỗ nào được chỉ định",
    "sosāniko": "người sống ở bãi tha ma",
}
SIMILE = {  # X-ūpamā puggalā = «N hạng người giống như X»
    "gilāna": "người bệnh", "potthaka": "vải gai thô", "kāsikavattha": "vải xứ Ca-thi",
    "valāhaka": "mây mưa", "mūsika": "chuột", "amba": "quả xoài", "kumbha": "cái chum",
    "udakarahada": "hồ nước", "balībadda": "bò đực", "āsīvisa": "rắn độc", "rukkha": "cây",
    "yodhājīva": "chiến binh", "udaka": "người ở dưới nước",
}
SATTAKA_UDAKA = [  # ^4-M-13 (1) seven persons compared to water
    "người chìm một lần thì chìm hẳn", "người trồi lên rồi lại chìm", "người trồi lên rồi đứng yên",
    "người trồi lên rồi quan sát, nhìn quanh", "người trồi lên rồi bơi qua",
    "người trồi lên rồi đến được chỗ chân chạm đáy",
    "người trồi lên rồi " + TINNO + ", là bà-la-môn",
]
MAGGASAMANGI = "người có được con đường"      # maggasamaṅgī (pi-1 ^1-1373)
PHALASAMANGI = "người có được thành quả"      # phalasamaṅgī (pi-1 ^1-1373)

NAME = {}
for _p, _v in EKAKA:
    NAME[_p] = _v
for _it in DUKA:
    if isinstance(_it, tuple):
        NAME[_it[0]], NAME[_it[2]] = _it[1], _it[3]
for _d in (TIKA_NAMES, CATUKKA_NAMES, PANCAKA_NAMES):
    NAME.update(_d)
NAME["uddhaṃsoto akaniṭṭhagāmī"] = NAME["uddhaṃsotoakaniṭṭhagāmī"]   # ch2 spelling with a space


def names(*keys):
    return ", ".join(NAME[k] for k in keys)


# ---------------------------------------------------------------- recurring clauses (ch1 / ch2)
KHANDHA_LIST = "khối vật chất, khối cảm giác, khối tri giác, khối tạo tác, khối thức"            # pi-2 ^2-1
AYATANA_LIST = ("lĩnh vực mắt, lĩnh vực hình sắc, lĩnh vực tai, lĩnh vực âm thanh, lĩnh vực mũi, lĩnh vực mùi, "
                "lĩnh vực lưỡi, lĩnh vực vị, lĩnh vực thân, lĩnh vực vật xúc chạm, lĩnh vực ý, "
                "lĩnh vực đối tượng của ý")                                                     # pi-1 ^1-1342
DHATU_LIST = ("yếu tố mắt, yếu tố hình sắc, yếu tố thức qua mắt, yếu tố tai, yếu tố âm thanh, yếu tố thức qua tai, "
              "yếu tố mũi, yếu tố mùi, yếu tố thức qua mũi, yếu tố lưỡi, yếu tố vị, yếu tố thức qua lưỡi, "
              "yếu tố thân, yếu tố vật xúc chạm, yếu tố thức qua thân, yếu tố ý, yếu tố đối tượng của ý, "
              "yếu tố ý thức")                                                                  # pi-2 ^2-183
SACCA_LIST = ("sự thật về khổ đau, sự thật về sự phát sinh, sự thật về sự chấm dứt, "
              "sự thật về con đường")                                                           # pi-2 ^2-982
INDRIYA_LIST = ("năng lực mắt, năng lực tai, năng lực mũi, năng lực lưỡi, năng lực thân, năng lực ý, "
                "năng lực nữ tính, năng lực nam tính, năng lực sống, năng lực dễ chịu, năng lực khó chịu, "
                "năng lực niềm vui, năng lực nỗi buồn, năng lực bình thản, năng lực niềm tin, "
                "năng lực tinh tấn, năng lực tỉnh thức, năng lực định tâm, năng lực trí tuệ, "
                "năng lực biết được điều chưa từng biết, năng lực hiểu biết trọn vẹn, "
                "năng lực của người đã hiểu biết trọn vẹn")                                     # pi-2 ^2-221

VIMOKKHA = "dùng thân chạm đến tám sự giải thoát rồi an trú"        # aṭṭha vimokkhe kāyena phusitvā viharati
NA_HEVA_KHO = "quả thật không"                                      # na heva kho
PANNAYA_SOME = "và nhờ thấy bằng trí tuệ, một số ô nhiễm của người ấy được diệt tận"   # paññāya cassa disvā ekacce āsavā parikkhīṇā honti
PANNAYA_ALL = "và nhờ thấy bằng trí tuệ, các ô nhiễm của người ấy được diệt tận"       # … āsavā parikkhīṇā honti
SAMAPATTI_LABHI = ("có được các thành tựu thiền đi kèm với hình sắc "
                   "hoặc đi kèm với không hình sắc")                # lābhī hoti rūpasahagatānaṃ vā arūpasahagatānaṃ vā samāpattīnaṃ
NIKAMA_NEG = ("Nhưng người ấy không có được chúng theo ý muốn, không có được chúng một cách không khó khăn, "
              "không có được chúng một cách không vất vả; không chứng nhập và cũng không xuất khỏi chúng "
              "ở nơi nào mình muốn, thành tựu thiền nào mình muốn, lâu chừng nào mình muốn.")
NIKAMA_POS = ("Và người ấy có được chúng theo ý muốn, có được chúng một cách không khó khăn, "
              "có được chúng một cách không vất vả; chứng nhập và cũng xuất khỏi chúng "
              "ở nơi nào mình muốn, thành tựu thiền nào mình muốn, lâu chừng nào mình muốn.")
THANA = "Nhưng đây là điều có thể xảy ra, rằng"                     # Ṭhānaṃ kho panetaṃ vijjati, yaṃ (pi-2 ^2-… «Ṭhānañca kho etaṃ vijjati yaṃ»)
ATTHANA = "Đây là điều không thể xảy ra, không có cơ hội, rằng"     # Aṭṭhānametaṃ anavakāso yaṃ (pi-2)
ARIYE_VIMOKKHE = "Tất cả các bậc thánh, xét về sự giải thoát cao quý, đều là {pl}."   # Sabbepi ariyapuggalā ariye vimokkhe X-ā.
SACCA_PAJANATI = ("hiểu rõ đúng như thật: “Đây là khổ đau”, hiểu rõ đúng như thật: “Đây là sự phát sinh của khổ đau”, "
                  "hiểu rõ đúng như thật: “Đây là sự chấm dứt khổ đau”, hiểu rõ đúng như thật: "
                  "“Đây là cách thực hành dẫn đến sự chấm dứt khổ đau”.")
TATHAGATA_DHAMMA = "Giáo Pháp do Như Lai tuyên bố đã được người ấy thấy rõ và thông suốt bằng trí tuệ."
ANANUSSUTA = "tự mình giác ngộ các sự thật trong những điều chưa từng được nghe trước đây"  # pubbe ananussutesu dhammesu sāmaṃ saccāni abhisambujjhati
NA_ANANUSSUTA = "không tự mình giác ngộ các sự thật trong những điều chưa từng được nghe trước đây"
SABBANNUTA = "đạt đến sự toàn tri"
VASIBHAVA = "sự làm chủ đối với các sức mạnh"
SOTAPANNA_BASE = ("Ở đời này, có người, nhờ diệt tận hoàn toàn ba xiềng xích, là bậc vào dòng, "
                  "không còn phải rơi vào nơi đọa lạc, có hướng đi cố định, hướng đến sự giác ngộ trọn vẹn")
ANAGAMI_BASE = ("Ở đời này, có người, nhờ diệt tận hoàn toàn năm xiềng xích thuộc phần thấp, được hóa sinh, "
                "nhập Niết-bàn trọn vẹn ở đó, không còn quay trở lại từ thế giới ấy.")
UPARITTHIMA = "làm phát sinh con đường cao quý để dứt bỏ các xiềng xích cao hơn"   # ariyamaggaṃ sañjaneti upariṭṭhimānaṃ saṃyojanānaṃ pahānāya
PATIPANNO_FOR = "người đang thực hành để tự mình chứng nghiệm thành quả {x}"       # X-phalasacchikiriyāya paṭipanno
KAMARAGA_TANU = "để làm suy yếu sự tham đắm dục lạc và ác ý"                       # pi-1
KAMARAGA_PAHANA = "để dứt bỏ sự tham đắm dục lạc và ác ý không còn sót lại"         # pi-1
UDDHAM_PAHANA = ("để dứt bỏ sự tham đắm cõi hình sắc, sự tham đắm cõi không hình sắc, "
                 "sự kiêu mạn, sự xao động và vô minh không còn sót lại")             # pi-1
AVARANA_NEG = ("mang sự ngăn che do nghiệp, mang sự ngăn che do phiền não, "
               "mang sự ngăn che do quả của nghiệp, không có niềm tin, không có ý muốn, kém trí tuệ")  # pi-2 ^2-826
AVARANA_POS = ("không mang sự ngăn che do nghiệp, không mang sự ngăn che do phiền não, "
               "không mang sự ngăn che do quả của nghiệp, có niềm tin, có ý muốn, có trí tuệ")      # pi-2 ^2-827
NIYAMA = "có khả năng bước vào sự cố định, tức sự đúng đắn trong các hiện tượng thiện"           # pi-2
NA_NIYAMA = "không có khả năng bước vào sự cố định, tức sự đúng đắn trong các hiện tượng thiện"  # pi-2

# Cross-book strings: asserted at build time to occur in the reviewed rails of that book.
CROSS_BOOK = [
    (1, HOMAGE), (1, "# " + PITAKA), (1, "### " + MATIKA), (1, "Phần nêu đề mục"),
    (1, "Phân loại theo nhóm một."), (1, "Phân loại theo nhóm mười."), (1, "Giải thích phân loại theo nhóm một"),
    (2, "Giải thích phân loại theo nhóm mười"), (1, "Ma trận đã hoàn tất."), (1, "Bộ “Liệt kê các hiện tượng” đã hoàn tất."),
    (2, "Năm khối – " + KHANDHA_LIST), (1, "Mười hai lĩnh vực nhận biết – " + AYATANA_LIST),
    (2, "Mười tám yếu tố – " + DHATU_LIST), (2, cap(SACCA_LIST)),(2, "Hai mươi hai năng lực – " + INDRIYA_LIST),
    (3, "bốn sự thật"), (3, "hai mươi hai năng lực"), (3, "mười tám yếu tố"),
    (1, IDHEKACCO), (2, "có người hành thiền"), (1, "người phàm phu"), (1, "Ba xiềng xích"),
    (2, "Năm xiềng xích thuộc phần thấp"), (2, "tám sự giải thoát"), (2, "thành tựu thiền"),
    (2, "chứng nhập thành tựu thiền"), (2, "xuất khỏi thành tựu thiền"), (2, ATTHANA), (2, THANA),
    (2, "sự buông thả"), (2, AVARANA_NEG), (2, AVARANA_POS), (2, NA_NIYAMA), (2, NIYAMA),
    (1, KAMARAGA_TANU), (1, KAMARAGA_PAHANA), (1, UDDHAM_PAHANA), (2, "hiểu rõ đúng như thật"),
    (2, "sự phát sinh của khổ đau"), (2, "cách thực hành dẫn đến sự chấm dứt khổ đau"),
    (2, "thành quả vào dòng"), (2, "thành quả trở lại một lần"), (2, "thành quả không trở lại"),
    (2, "thành quả A-la-hán"), (1, MAGGASAMANGI), (1, PHALASAMANGI), (1, "con đường cao quý"),
    (1, "sự diệt tận các ô nhiễm"), (2, "sự giải thoát của tâm"), (2, "sáu loại hiểu biết trực tiếp"),
    (1, "ba loại hiểu biết chân thật"), (2, "người còn đang tu học"), (2, "người đã hoàn tất tu học"),
    (1, "tự mình chứng nghiệm"), (1, "có sự thúc đẩy"), (2, "nhập Niết-bàn trọn vẹn"), (1, "chúng sinh hóa sinh"),
    (2, "nơi đọa lạc"), (2, "chư thiên"), (2, "loài người"), (2, "Tuổi thọ"), (1, "Năm nghiệp có quả không gián đoạn"),
    (1, "quan điểm sai lầm cố định"), (2, "người giữ giới"), (2, "người không biết hổ thẹn"),
    (2, "người không biết ghê sợ tội lỗi"), (2, "người mất tỉnh thức"), (2, "người có sự tỉnh thức được thiết lập"),
    (2, "người thành tựu về quan điểm"), (2, "Sự giận dữ và sự ôm hận"), (2, "sự gièm pha và sự ganh đua"),
    (2, "sự ganh tị và sự keo kiệt"), (2, "sự xảo trá và sự gian xảo"), (1, "Sự khó dạy bảo"),
    (1, "Sự kết bạn với người xấu"), (1, "Sự kết bạn với người tốt"), (1, "Sự không phòng hộ cửa các giác quan"),
    (1, "Sự không biết tiết độ trong ăn uống"), (1, "Sự thiếu hiểu biết rõ ràng"), (1, "Sự suy đồi về giới hạnh"),
    (1, "Sự thành tựu về giới hạnh"), (2, "xiềng xích ở nơi bản thân"), (2, "xiềng xích ở bên ngoài bản thân"),
    (2, "chí hướng thấp kém"), (2, "chí hướng ưu việt"), (1, "giống như tia chớp"), (1, "giống như kim cương"),
    (1, "người chân chính"), (2, "bậc đạo sư"), (2, "gần gũi, kết giao, thân cận"), (2, "lòng tin trong sáng"),
    (2, "ít học hỏi"), (1, "học hỏi nhiều"), (1, "sa-môn"), (1, "bà-la-môn"), (2, DITTHEVA_DHAMME),
    (2, "Tăng Chi Bộ Kinh"), (1, "các hiện tượng xấu ác bất thiện"), (2, "sự hiểu biết trực tiếp"),
    (2, "sức mạnh"), (2, "Như Lai"), (1, "Sự tĩnh lặng"), (1, "Sự thấu suốt"), (1, "ở nơi bản thân"),
    (2, "thuộc về phước"), (1, "thế gian"), (1, "sự tham đắm"), (1, "sân hận"), (1, "si mê"), (1, "sự kiêu mạn"),
    (2, "tài ứng đáp"), (2, "trí tuệ thuộc về người còn đang tu học"), (1, "hiểu biết chân thật"),
    (2, "không thể đo lường"), (1, "dục lạc"), (1, "khao khát được hiện hữu"), (2, "có khả năng"),
    (1, "Năng lực trí tuệ".lower()), (2, "năng lực niềm tin"), (2, "Phạm Chúng"),
]


# ---------------------------------------------------------------- chapter texts (non-empty lines, IDs added by the builder)
def preamble():
    return [HOMAGE, "# " + PITAKA, "## " + BOOK_TITLE]


def matika():
    L = ["### " + MATIKA, "#### " + UDDESA_HEADING[1],
         "Sáu sự định danh – sự định danh về các khối, sự định danh về các lĩnh vực nhận biết, "
         "sự định danh về các yếu tố, sự định danh về các sự thật, sự định danh về các năng lực, "
         "sự định danh về các hạng người.",
         designation("các khối", "năm khối", KHANDHA_LIST),
         designation("các lĩnh vực nhận biết", "mười hai lĩnh vực nhận biết", AYATANA_LIST),
         designation("các yếu tố", "mười tám yếu tố", DHATU_LIST),
         designation("các sự thật", "bốn sự thật", SACCA_LIST),
         designation("các năng lực", "hai mươi hai năng lực", INDRIYA_LIST),
         DESIGNATION_Q.format(x="các hạng người")]
    for i, (_, v) in enumerate(EKAKA, 1):
        L.append(f"({i}) {cap(v)}{EKAKA_VARIANT.get(i, '')}")
    L.append(MATIKA_GROUP_CLOSER[1])

    L += ["#### " + UDDESA_HEADING[2], GROUP_OPENER[2]]
    for i, it in enumerate(DUKA, 1):
        if isinstance(it, tuple):
            L.append(f"({i}) {cap(it[1])} và {it[3]}{DUKA_VARIANT.get(i, '')}.")
        else:
            L.append(f"({i}) {it}")
    L.append(MATIKA_GROUP_CLOSER[2])

    sim = lambda n, k: f"{TYPES_COUNT[n]} giống như {SIMILE[k]}"
    L += ["#### " + UDDESA_HEADING[3], GROUP_OPENER[3]]
    sev = "đáng gần gũi, đáng kết giao, đáng thân cận"
    nsev = "không đáng gần gũi, không đáng kết giao, không đáng thân cận"
    tika = [
        cap(names("nirāso", "āsaṃso", "vigatāso")) + ".",
        sim(3, "gilāna") + ".",
        cap(names("kāyasakkhī", "diṭṭhippatto", "saddhāvimutto")) + ".",
        cap(names("gūthabhāṇī", "pupphabhāṇī", "madhubhāṇī")) + ".",
        cap(names("arukūpamacitto", "vijjūpamacitto", "vajirūpamacitto")) + ".",
        cap(names("andho", "ekacakkhu", "dvicakkhu")) + ".",
        f"{cap(NAME['avakujjapañño'])}, {NAME['ucchaṅgapañño']} [khác chính tả (Syā.): uccaṅgupañño], "
        f"{NAME['puthupañño']}.",
        "Có người chưa lìa tham đắm đối với các dục lạc và các sự hiện hữu, có người đã lìa tham đắm đối với "
        "các dục lạc nhưng chưa lìa tham đắm đối với các sự hiện hữu, có người đã lìa tham đắm đối với cả "
        "các dục lạc và các sự hiện hữu.",
        cap(names("pāsāṇalekhūpamo", "pathavilekhūpamo", "udakalekhūpamo")) + ".",
        sim(3, "potthaka") + ".",
        sim(3, "kāsikavattha") + ".",
        cap(names("suppameyyo", "duppameyyo", "appameyyo")) + ".",
        f"Có người {nsev}, có người {sev}, có người {sev} với lòng tôn kính và trân trọng "
        "[khác chính tả (Sī.): garukatvā].",
        f"Có người đáng ghê tránh, {nsev}, có người đáng được nhìn với sự bình thản, {nsev}; có người {sev}.",
        "Có người thực hành trọn vẹn các giới hạnh [khác chính tả (Syā.): paripūrīkārī], thực hành định tâm ở "
        "mức độ nhất định, thực hành trí tuệ ở mức độ nhất định; có người thực hành trọn vẹn các giới hạnh, "
        "thực hành trọn vẹn định tâm, thực hành trí tuệ ở mức độ nhất định; có người thực hành trọn vẹn các "
        "giới hạnh, thực hành trọn vẹn định tâm và thực hành trọn vẹn trí tuệ.",
        "Ba bậc đạo sư.",
        "Lại có ba bậc đạo sư khác.",
    ]
    L += [f"({i}) {t}" for i, t in enumerate(tika, 1)]
    L.append(MATIKA_GROUP_CLOSER[3])

    L += ["#### " + UDDESA_HEADING[4], GROUP_OPENER[4]]
    praise_blame = "nói lời khen ngợi người đáng chê trách"
    blame_praise = "nói lời chê trách người đáng khen ngợi"
    blame_blame = "nói lời chê trách người đáng chê trách"
    praise_praise = "nói lời khen ngợi người đáng khen ngợi"
    trust_no = "bày tỏ lòng tin trong sáng ở nơi không đáng có lòng tin trong sáng"
    distrust_yes = "bày tỏ sự thiếu lòng tin trong sáng ở nơi đáng có lòng tin trong sáng"
    distrust_no = "bày tỏ sự thiếu lòng tin trong sáng ở nơi không đáng có lòng tin trong sáng"
    trust_yes = "bày tỏ lòng tin trong sáng ở nơi đáng có lòng tin trong sáng"
    nv = "không xem xét, không tìm hiểu thấu đáo mà"
    av = "xem xét, tìm hiểu thấu đáo rồi"
    btk = "đúng sự thật, chính xác, đúng lúc"
    catukka = [
        cap(names("asappuriso", "asappurisena asappurisataro", "sappuriso", "sappurisena sappurisataro")) + ".",
        cap(names("pāpo", "pāpena pāpataro", "kalyāṇo", "kalyāṇena kalyāṇataro")) + ".",
        cap(names("pāpadhammo", "pāpadhammena pāpadhammataro", "kalyāṇadhammo",
                  "kalyāṇadhammena kalyāṇadhammataro")) + ".",
        f"{cap(NAME['sāvajjo'])}, {NAME['vajjabahulo']}, {NAME['appavajjo']} "
        f"[dị bản (Syā., Ka.): appasāvajjo; Tăng Chi Bộ Kinh 4.135], {NAME['anavajjo']}.",
        f"{cap(NAME['ugghaṭitaññū'])}, {NAME['vipañcitaññū']} "
        f"[khác chính tả (Sī.): vipacitaññū; Tăng Chi Bộ Kinh 4.133], {NAME['neyyo']}, {NAME['padaparamo']}.",
        cap(names("yuttappaṭibhāno no muttappaṭibhāno", "muttappaṭibhāno no yuttappaṭibhāno",
                  "yuttappaṭibhāno ca muttappaṭibhāno ca", "neva yuttappaṭibhāno no muttappaṭibhāno")) + ".",
        "Bốn hạng người thuyết giảng Giáo Pháp.",
        sim(4, "valāhaka") + ".",
        sim(4, "mūsika") + ".",
        sim(4, "amba") + ".",
        sim(4, "kumbha") + ".",
        sim(4, "udakarahada") + ".",
        sim(4, "balībadda") + " [khác chính tả (Sī.): balibaddūpamā].",
        sim(4, "āsīvisa") + ".",
        f"Có người {nv} {praise_blame}, có người {nv} {blame_praise}, có người {nv} {trust_no}, "
        f"có người {nv} {distrust_yes}.",
        f"Có người {av} {blame_blame}, có người {av} {praise_praise}, có người {av} {distrust_no}, "
        f"có người {av} {trust_yes}.",
        f"Có người {blame_blame}, {btk}, nhưng không {praise_praise}, {btk}; "
        f"có người {praise_praise}, {btk}, nhưng không {blame_blame}, {btk}; "
        f"có người vừa {blame_blame}, {btk}; vừa {praise_praise}, {btk}, "
        f"có người không {blame_blame}, {btk}, cũng không {praise_praise}, {btk}.",
        cap(names("uṭṭhānaphalūpajīvī no puññaphalūpajīvī", "puññaphalūpajīvī no uṭṭhānaphalūpajīvī",
                  "uṭṭhānaphalūpajīvī ca puññaphalūpajīvī ca", "neva uṭṭhānaphalūpajīvī no puññaphalūpajīvī")) + ".",
        cap(names("tamo tamaparāyano", "tamo jotiparāyano", "joti tamaparāyano", "joti jotiparāyano")) + ".",
        cap(names("oṇatoṇato", "oṇatuṇṇato", "uṇṇatoṇato", "uṇṇatuṇṇato")) + ".",
        sim(4, "rukkha") + ".",
        cap(names("rūpappamāṇo rūpappasanno", "ghosappamāṇo ghosappasanno")) + ".",
        cap(names("lūkhappamāṇo lūkhappasanno", "dhammappamāṇo dhammappasanno")) + ".",
        "Có người thực hành vì lợi ích của bản thân, không vì lợi ích của người khác; có người thực hành vì lợi "
        "ích của người khác, không vì lợi ích của bản thân; có người thực hành vì lợi ích của bản thân và vì lợi "
        "ích của người khác; có người không thực hành vì lợi ích của bản thân cũng không vì lợi ích của người khác.",
        "Có người tự hành hạ bản thân, chuyên tâm thực hành việc hành hạ bản thân; có người hành hạ người khác, "
        "chuyên tâm thực hành việc hành hạ người khác; có người vừa tự hành hạ bản thân, chuyên tâm thực hành "
        "việc hành hạ bản thân, vừa hành hạ người khác, chuyên tâm thực hành việc hành hạ người khác; có người "
        "không tự hành hạ bản thân, không chuyên tâm thực hành việc hành hạ bản thân, không hành hạ người khác, "
        "không chuyên tâm thực hành việc hành hạ người khác. Người ấy, không tự hành hạ bản thân, không hành hạ "
        f"người khác, {DITTHEVA_DHAMME} sống không còn đói khát, đã lắng dịu, đã trở nên mát mẻ "
        "[khác chính tả (Sī., Ka.): sītibhūto], cảm nhận hạnh phúc, với bản thân đã trở nên cao thượng.",
        cap(names("sarāgo", "sadoso", "samoho", "samāno")) + ".",
        "Có người có được sự tĩnh lặng của tâm ở nơi bản thân, không có được sự thấu suốt các hiện tượng nhờ trí "
        "tuệ cao thượng; có người có được sự thấu suốt các hiện tượng nhờ trí tuệ cao thượng, không có được sự "
        "tĩnh lặng của tâm ở nơi bản thân; có người có được sự tĩnh lặng của tâm ở nơi bản thân và có được sự "
        "thấu suốt các hiện tượng nhờ trí tuệ cao thượng; có người không có được sự tĩnh lặng của tâm ở nơi bản "
        "thân, cũng không có được sự thấu suốt các hiện tượng nhờ trí tuệ cao thượng.",
        f"{cap(names('anusotagāmī', 'paṭisotagāmī', 'ṭhitatto'))}, bà-la-môn đã vượt qua, đã đến bờ bên kia "
        "[khác chính tả (Sī., Syā.): pāragato], đứng trên đất liền.",
        cap(names("appassuto sutena anupapanno", "appassuto sutena upapanno", "bahussuto sutena anupapanno",
                  "bahussuto sutena upapanno")) + ".",
        cap(names("samaṇamacalo", "samaṇapadumo", "samaṇapuṇḍarīko", "samaṇesu samaṇasukhumālo")) + ".",
    ]
    L += [f"({i}) {t}" for i, t in enumerate(catukka, 1)]
    L.append(MATIKA_GROUP_CLOSER[4])

    L += ["#### " + UDDESA_HEADING[5], GROUP_OPENER[5]]
    liber = ("hiểu rõ đúng như thật sự giải thoát của tâm, sự giải thoát nhờ trí tuệ ấy, nơi mà các hiện tượng "
             "xấu ác bất thiện đã sinh khởi nơi người ấy chấm dứt không còn dư sót")
    pancaka = [
        f"Có người phạm lỗi [khác chính tả (Sī., Syā.): ārambhati] và ăn năn, không {liber}. "
        f"Có người phạm lỗi nhưng không ăn năn, không {liber}. "
        f"Có người không phạm lỗi nhưng ăn năn, không {liber}. "
        f"Có người không phạm lỗi và không ăn năn, không {liber}. "
        f"Có người không phạm lỗi và không ăn năn, {liber}.",
        cap(names("datvā avajānāti", "saṃvāsena avajānāti", "ādheyyamukho", "lolo", "mando momūho")) + ".",
        sim(5, "yodhājīva") + ".",
    ]
    for k in ("piṇḍapātiko", "khalupacchābhattiko", "ekāsaniko", "paṃsukūliko", "tecīvariko", "āraññiko",
              "rukkhamūliko", "abbhokāsiko", "nesajjiko", "yathāsanthatiko", "sosāniko"):
        pancaka.append(f"Năm hạng {NAME[k]}.")
    L += [f"({i}) {t}" for i, t in enumerate(pancaka, 1)]
    L.append(MATIKA_GROUP_CLOSER[5])

    L += ["#### " + UDDESA_HEADING[6], GROUP_OPENER[6]]
    L.append(
        f"(1) Có người {ANANUSSUTA}, và ở đó {SABBANNUTA} và {VASIBHAVA} [dị bản (Pī.): phalesu]. "
        f"Có người {ANANUSSUTA}, nhưng ở đó không {SABBANNUTA}, cũng không đạt đến {VASIBHAVA}. "
        f"Có người {NA_ANANUSSUTA}, nhưng {DITTHEVA_DHAMME} là {DUKKHASSANTAKARO} và đạt đến sự toàn hảo của "
        "hàng đệ tử. "
        f"Có người {NA_ANANUSSUTA}, {DITTHEVA_DHAMME} là {DUKKHASSANTAKARO}, nhưng không đạt đến sự toàn hảo "
        "của hàng đệ tử. "
        f"Có người {NA_ANANUSSUTA}, và {DITTHEVA_DHAMME} không phải {DUKKHASSANTAKARO}, mà là "
        f"{NAME['anāgāmī']}, không còn trở lại [dị bản (Syā., Ka.): anāgantvā; Tăng Chi Bộ Kinh 4.171] "
        "trạng thái này. "
        f"Có người {NA_ANANUSSUTA}, và {DITTHEVA_DHAMME} không phải {DUKKHASSANTAKARO}, mà là người còn trở lại "
        "[dị bản (Syā., Ka.): sotāpannasakadāgāmī], còn trở lại trạng thái này.")
    L.append(MATIKA_GROUP_CLOSER[6])

    L += ["#### " + UDDESA_HEADING[7], GROUP_OPENER[7]]
    L.append(f"(1) {sim(7, 'udaka')}. {cap(', '.join(SATTAKA_UDAKA))}.")
    L.append("(2) " + cap(names("ubhatobhāgavimutto", "paññāvimutto", "kāyasakkhī", "diṭṭhippatto",
                                "saddhāvimutto", "dhammānusārī", "saddhānusārī")) + ".")
    L.append(MATIKA_GROUP_CLOSER[7])

    L += ["#### " + UDDESA_HEADING[8], GROUP_OPENER[8],
          f"(1) Bốn {MAGGASAMANGI}, bốn {PHALASAMANGI}.", MATIKA_GROUP_CLOSER[8]]
    L += ["#### " + UDDESA_HEADING[9], GROUP_OPENER[9],
          "(1) " + cap(names("sammāsambuddho", "paccekasambuddho", "ubhatobhāgavimutto", "paññāvimutto",
                             "kāyasakkhī", "diṭṭhippatto", "saddhāvimutto", "dhammānusārī", "saddhānusārī")) + ".",
          MATIKA_GROUP_CLOSER[9]]
    L += ["#### " + UDDESA_HEADING[10], GROUP_OPENER[10],
          "(1) Năm người đạt đến đích ngay ở đây, năm người đạt đến đích sau khi rời khỏi nơi đây.",
          MATIKA_GROUP_CLOSER[10], MATIKA_END]
    return L


def ekaka():
    N = NAME
    vim = VIMOKKHA
    L = ["### " + NIDDESO, "#### " + CHAPTER_HEADING[2]]
    L.append(f"{q(N['samayavimutto'])} {IDHEKACCO} theo từng lúc, theo từng thời điểm, dùng thân chạm đến "
             "[khác chính tả (Sī., Pī.): phassitvā] tám sự giải thoát rồi an trú, "
             f"{PANNAYA_SOME} {close(N['samayavimutto'])}")
    L.append(f"{q(N['asamayavimutto'])} {IDHEKACCO} {NA_HEVA_KHO} theo từng lúc, theo từng thời điểm, {vim}, "
             f"{PANNAYA_ALL} {close(N['asamayavimutto'])} "
             + ARIYE_VIMOKKHE.format(pl="những người được giải thoát không theo thời điểm"))
    for key, neg, tail in (
        ("kuppadhammo", True, f"{THANA} do sự buông thả, các thành tựu thiền ấy của người ấy có thể bị lay chuyển"),
        ("akuppadhammo", False, f"{ATTHANA} do sự buông thả, các thành tựu thiền ấy của người ấy có thể bị lay chuyển"),
        ("parihānadhammo", True, f"{THANA} do sự buông thả, người ấy có thể sa sút khỏi các thành tựu thiền ấy"),
        ("aparihānadhammo", False, f"{ATTHANA} do sự buông thả, người ấy có thể sa sút khỏi các thành tựu thiền ấy"),
        ("cetanābhabbo", True, "Nếu người ấy luôn hướng chủ ý đến chúng, người ấy không sa sút khỏi các thành tựu "
                               "thiền ấy. Nếu không luôn hướng chủ ý đến chúng, người ấy sa sút khỏi các thành tựu "
                               "thiền ấy"),
        ("anurakkhaṇābhabbo", True, "Nếu người ấy gìn giữ chúng, người ấy không sa sút khỏi các thành tựu thiền ấy. "
                                    "Nếu không gìn giữ chúng, người ấy sa sút khỏi các thành tựu thiền ấy"),
    ):
        line = f"{q(N[key])} {IDHEKACCO} {SAMAPATTI_LABHI}. {NIKAMA_NEG if neg else NIKAMA_POS} {tail} {close(N[key])}"
        if key == "akuppadhammo":
            line += " " + ARIYE_VIMOKKHE.format(pl="những người không thể bị lay chuyển")
        if key == "aparihānadhammo":
            line += " " + ARIYE_VIMOKKHE.format(pl="những người không thể bị sa sút")
        L.append(line)
    L.append(f"{q(N['puthujjano'])} Người mà ba xiềng xích chưa được dứt bỏ; và người ấy cũng không thực hành để "
             f"dứt bỏ các hiện tượng ấy {close(N['puthujjano'])}")
    L.append(f"{q(N['gotrabhū'])} Người {SAMANNAGATO} những hiện tượng mà ngay sau chúng có sự đi vào của hiện "
             f"tượng cao quý {close(N['gotrabhū'])}")
    L.append(f"{q(N['bhayūparato'])} Bảy {N['sekkho']} và những {N['puthujjano']} giữ giới là "
             f"những {N['bhayūparato']}. {cap(N['arahā'])} là {N['abhayūparato']}.")
    L.append(f"{q(N['abhabbāgamano'])} Những người nào {AVARANA_NEG}, đần độn, {NA_NIYAMA} "
             f"{close_pl(PLURAL['abhabbāgamanā'])}")
    L.append(f"{q(N['bhabbāgamano'])} Những người nào {AVARANA_POS} [khác chính tả (Sī.): paññavantā], "
             f"không đần độn, {NIYAMA} {close_pl(PLURAL['bhabbāgamanā'])}")
    L.append(f"{q(N['niyato'])} Năm người phạm nghiệp có quả không gián đoạn, những người có quan điểm sai lầm cố "
             f"định, và tám bậc thánh là những {N['niyato']}. Những người còn lại là những {N['aniyato']}.")
    L.append(f"{q(N['paṭipannako'])} Bốn {MAGGASAMANGI} là những {N['paṭipannako']}, bốn {PHALASAMANGI} là "
             f"những {N['phaleṭhito']}.")
    L.append(f"{q(N['samasīsī'])} Người mà sự kết thúc các ô nhiễm và sự kết thúc mạng sống xảy ra không trước "
             f"không sau {close(N['samasīsī'])}")
    L.append(f"{q(N['ṭhitakappī'])} Giả sử người này đang thực hành để tự mình chứng nghiệm thành quả vào dòng, "
             "và đó là lúc kiếp bị thiêu hủy, thì kiếp sẽ không bị thiêu hủy chừng nào người này chưa tự mình "
             f"chứng nghiệm thành quả vào dòng. {close(N['ṭhitakappī'], dash=False)} Tất cả những "
             f"{MAGGASAMANGI} đều là những {N['ṭhitakappī']}.")
    L.append(f"{q(N['ariyo'])} Tám bậc thánh là những {N['ariyo']}. Những người còn lại là những {N['anariyo']}.")
    L.append(f"{q(N['sekkho'])} Bốn {MAGGASAMANGI} và ba {PHALASAMANGI} là “{PLURAL['sekkhā']}”. "
             f"{cap(N['arahā'])} là {N['asekkho']}. Những người còn lại là những {N['nevasekkhanāsekkho']}.")
    L.append(f"{q(N['tevijjo'])} Người {SAMANNAGATO} ba loại hiểu biết chân thật là “{N['tevijjo']}”.")
    L.append(f"{q(N['chaḷabhiñño'])} Người {SAMANNAGATO} sáu loại hiểu biết trực tiếp là “{N['chaḷabhiñño']}”.")
    L.append(f"{q(N['sammāsambuddho'])} {IDHEKACCO} {ANANUSSUTA}; và ở đó {SABBANNUTA}, và {VASIBHAVA} "
             f"{close(N['sammāsambuddho'])}")
    L.append(f"{q(N['paccekasambuddho'])} {IDHEKACCO} {ANANUSSUTA}; nhưng ở đó không {SABBANNUTA}, cũng không "
             f"đạt đến {VASIBHAVA} {close(N['paccekasambuddho'])}")
    L.append(f"{q(N['ubhatobhāgavimutto'])} {IDHEKACCO} {vim}; {PANNAYA_ALL} {close(N['ubhatobhāgavimutto'])}")
    L.append(f"{q(N['paññāvimutto'])} {IDHEKACCO} {NA_HEVA_KHO} {vim}; {PANNAYA_ALL}. "
             f"{close(N['paññāvimutto'], dash=False)}")
    L.append(f"{q(N['kāyasakkhī'])} {IDHEKACCO} {vim}; {PANNAYA_SOME}. {close(N['kāyasakkhī'], dash=False)}")
    L.append(f"{q(N['diṭṭhippatto'])} {IDHEKACCO} {SACCA_PAJANATI} {TATHAGATA_DHAMMA} "
             f"{cap(PANNAYA_SOME)} {close(N['diṭṭhippatto'])}")
    L.append(f"{q(N['saddhāvimutto'])} {IDHEKACCO} {SACCA_PAJANATI} {TATHAGATA_DHAMMA} "
             f"{cap(PANNAYA_SOME)}, nhưng không được như ở {N['diṭṭhippatto']} {close(N['saddhāvimutto'])}")
    sota = PATIPANNO_FOR.format(x="vào dòng")
    for key, ind, lead in (("dhammānusārī", "trí tuệ", "trí tuệ"), ("saddhānusārī", "niềm tin", "niềm tin")):
        res = "diṭṭhippatto" if key == "dhammānusārī" else "saddhāvimutto"
        L.append(f"{q(N[key])} {cap(sota)}, có năng lực {ind} vượt trội, tu tập con đường cao quý do {lead} dẫn "
                 f"dắt, có {lead} đi trước {close(N[key])} {cap(sota)} là {N[key]}; khi đã đứng vững trong "
                 f"thành quả, người ấy là {N[res]}.")
    L.append(f"{q(N['sattakkhattuparamo'])} {SOTAPANNA_BASE} [khác chính tả (Sī., Ka.): sambodhiparāyaṇo]. "
             "Người ấy, sau khi trôi lăn, luân chuyển giữa chư thiên và loài người bảy lần, thì đi đến tận cùng "
             f"của khổ đau {close(N['sattakkhattuparamo'])}")
    L.append(f"{q(N['kolaṅkolo'])} {SOTAPANNA_BASE}. Người ấy, sau khi trôi lăn, luân chuyển qua hai hoặc ba gia "
             f"đình, thì đi đến tận cùng của khổ đau {close(N['kolaṅkolo'])}")
    L.append(f"{q(N['ekabījī'])} {SOTAPANNA_BASE}. Người ấy, sau khi tạo ra chỉ một lần hiện hữu làm người, thì "
             f"đi đến tận cùng của khổ đau {close(N['ekabījī'])}")
    L.append(f"{q(N['sakadāgāmī'])} {IDHEKACCO}, nhờ diệt tận hoàn toàn ba xiềng xích và nhờ sự suy yếu của tham "
             f"đắm, sân hận và si mê, là {N['sakadāgāmī']}, chỉ trở lại thế gian này một lần rồi đi đến tận cùng "
             f"của khổ đau {close(N['sakadāgāmī'])}")
    ana = ANAGAMI_BASE[:-1]
    L.append(f"{q(N['anāgāmī'])} {ana} {close(N['anāgāmī'])}")
    L.append(f"{q(N['antarāparinibbāyī'])} {ANAGAMI_BASE} Người ấy, hoặc ngay sau khi tái sinh, hoặc khi chưa "
             f"đến giữa tuổi thọ, {UPARITTHIMA} {close(N['antarāparinibbāyī'])}")
    L.append(f"{q(N['upahaccaparinibbāyī'])} {ANAGAMI_BASE} Người ấy, sau khi đã qua giữa tuổi thọ, hoặc khi "
             f"gần mạng chung [khác chính tả (Ka.): kālaṃ kiriyaṃ], {UPARITTHIMA} "
             f"{close(N['upahaccaparinibbāyī'])}")
    L.append(f"{q(N['asaṅkhāraparinibbāyī'])} {ANAGAMI_BASE} Người ấy, không có sự thúc đẩy, {UPARITTHIMA} "
             f"{close(N['asaṅkhāraparinibbāyī'])}")
    L.append(f"{q(N['sasaṅkhāraparinibbāyī'])} {ANAGAMI_BASE} Người ấy, có sự thúc đẩy, {UPARITTHIMA} "
             f"{close(N['sasaṅkhāraparinibbāyī'])}")
    up = N["uddhaṃsoto akaniṭṭhagāmī"]
    L.append(f"{q(up)} {ANAGAMI_BASE} Người ấy chết từ cõi Vô Phiền thì đến cõi Vô Nhiệt, chết từ cõi Vô Nhiệt "
             "thì đến cõi Thiện Hiện, chết từ cõi Thiện Hiện thì đến cõi Thiện Kiến, chết từ cõi Thiện Kiến thì "
             f"đến cõi Sắc Cứu Cánh; ở cõi Sắc Cứu Cánh, người ấy {UPARITTHIMA} {close(up)}")
    L.append(f"Thế nào là {N['sotāpanno']} và {sota}? Người đang thực hành để dứt bỏ ba xiềng xích là {sota}. "
             f"Người mà ba xiềng xích đã được dứt bỏ {close(N['sotāpanno'])}")
    L.append(f"Người đang thực hành {KAMARAGA_TANU} là {PATIPANNO_FOR.format(x='trở lại một lần')}. Người mà sự "
             f"tham đắm dục lạc và ác ý đã suy yếu {close(N['sakadāgāmī'])}")
    L.append(f"Người đang thực hành {KAMARAGA_PAHANA} là {PATIPANNO_FOR.format(x='không trở lại')}. Người mà sự "
             f"tham đắm dục lạc và ác ý đã được dứt bỏ không còn sót lại {close(N['anāgāmī'])}")
    L.append(f"Người đang thực hành {UDDHAM_PAHANA} là {PATIPANNO_FOR.format(x='A-la-hán')}. Người mà sự tham "
             "đắm cõi hình sắc, sự tham đắm cõi không hình sắc, sự kiêu mạn, sự xao động, vô minh đã được dứt bỏ "
             f"không còn sót lại {close(N['arahā'])}")
    L.append(NIDDESA_CLOSER[1])
    return L


# ---------------------------------------------------------------- build
ID_RE = re.compile(r"\s*(\^[0-9A-Za-z-]+)\s*$")


def assemble(pali_name, vi_lines):
    src = (PALI_DIR / pali_name).read_text(encoding="utf-8").splitlines()
    out, k = [], 0
    for ln in src:
        if not ln.strip():
            out.append("")
            continue
        assert k < len(vi_lines), f"{pali_name}: too few Vietnamese lines"
        v = vi_lines[k]
        k += 1
        ph = re.match(r"#+ ", ln)
        assert (ph.group(0) if ph else "") == (re.match(r"#+ ", v).group(0) if re.match(r"#+ ", v) else ""), \
            f"{pali_name}: heading level differs at {ln[:40]!r} / {v[:40]!r}"
        m = ID_RE.search(ln)
        out.append(v + (" " + m.group(1) if m else ""))
    assert k == len(vi_lines), f"{pali_name}: {len(vi_lines) - k} extra Vietnamese lines"
    text = unicodedata.normalize("NFC", "\n".join(out).rstrip("\n") + "\n")
    return text


def check_cross_book():
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md"))) for b, d in RAILS_DIR.items()}
    missing = [(b, s) for b, s in CROSS_BOOK if s not in texts[b]]
    assert not missing, "cross-book strings not found: " + repr(missing)
    return len(CROSS_BOOK)


def main():
    n = check_cross_book()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    m = matika()
    e = ekaka()
    for name, lines in (("preamble.md", preamble()), ("1-matika.md", m), ("2-ekakapuggalapannatti.md", e)):
        (OUT_DIR / name).write_bytes(assemble(name, lines).encode("utf-8"))
    # every Ekaka matrix name is the question and the quoted name of its definition
    ch2 = (OUT_DIR / "2-ekakapuggalapannatti.md").read_text(encoding="utf-8")
    for p, v in EKAKA:
        assert v in ch2, p
    for p in ("samayavimutto", "kuppadhammo", "puthujjano", "sammāsambuddho", "kāyasakkhī", "arahā"):
        assert f"“{NAME[p]}”" in ch2, p
    print(f"OK: cross-book strings {n}; wrote preamble.md, 1-matika.md ({len(m)} lines), "
          f"2-ekakapuggalapannatti.md ({len(e)} lines) to {OUT_DIR}")


if __name__ == "__main__":
    main()
