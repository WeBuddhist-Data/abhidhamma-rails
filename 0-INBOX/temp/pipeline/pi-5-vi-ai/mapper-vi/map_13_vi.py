"""Build the Pāli->Vietnamese keyword map for pi-5 (Kathāvatthu) chapter 13: 13-pancamavaggo.

usage: python -I -X utf8 -B map_13_vi.py                  (writes 13-pancamavaggo.mapped.md and verifies it)
       python -I -X utf8 -B map_13_vi.py show lo hi [miss] (segments lo..hi with every pair, the values of the finished
                                                           chapters' tables and English | Russian; writes nothing)

Importing this module builds nothing (check_parts_vi.py imports it for ALLOWED).
Resolution order per keyword: OVERRIDES[bid][kw] -> context13 (segment rules of this chapter) -> value5(kw, kws, T13,
text) of map_sample_vi (T13 -> context5 -> FORMULAS -> KV -> two-word composition -> the pi-4 chain).
Conventions: pi-1 … pi-4 vi-map-conventions*.md + notes-map-*.md, vi-map-conventions-pi5.md, map-coordinator-rules.md;
new values in notes-map-13.md.
"""
import importlib
import pathlib
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai\mapper-vi")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_vi import (NDE, GAP, build_part, en_ru, join, lc, pick, present, read_keywords,  # noqa: E402
                           read_vietnamese, verify)
from map_sample_vi import FORMULAS, KV, context5, value5  # noqa: E402,F401

PART = "13-pancamavaggo"

_HB = "hiểu biết"
_GT = "hiểu biết về sự giải thoát"             # vimuttiñāṇaṃ
_AS = "thuộc về người đã hoàn tất tu học"      # asekha (pi-1 MATRIX asekkhā)
_CT = "bao quát tâm"                           # cetopariyāye «hiểu biết bao quát tâm»
_TS = "hiểu biết thông suốt"                   # paṭisambhidā
_QU = "hiểu biết theo quy ước"                 # sammutiñāṇaṃ
_SL = "điều sai lệch"                          # viparīte «hiểu biết về điều sai lệch»
_ND = "người đang nhập"                        # samāpannassa «người đang nhập thành tựu thiền …»
_TC = "tự mình chứng nghiệm thành quả"         # X-phalasacchikiriyāya
_CO = "người có được thành quả"                # X-phalasamaṅgissa
_DT = "có" + GAP + "làm đối tượng"             # X-ārammaṇaṃ «chỉ có X làm đối tượng»

T13 = {
    # ---- headings «(43) 1. Bàn về sự giải thoát» … «(52) 10. Bàn về hiểu biết về thành quả»; closers «Phần bàn về …
    # đã hoàn tất.» (kathā = Bàn về, niṭṭhitā = đã hoàn tất, vaggo = chương, pañcama = thứ năm: FORMULAS / KV)
    "vimuttikathā": "Bàn về sự giải thoát", "vimutti": "sự giải thoát",   # T11
    "ñāṇa": _HB, "ñāṇaṃ": _HB,                     # «hiểu biết» (no «sự»; T5 / T11)
    "asekha": _AS, "asekhaṃ": _AS,
    "sekha": NDE,                                  # 5-13-2-1-0: fragment of Asekha- with no «còn đang tu học» in the
                                                   # heading (pi-1 ^1-1024 sekkhā)
    "sekhaṃ": "còn đang tu học",                   # fragment of asekhaṃ: the positive Vietnamese, as the segment has it
                                                   # in «người còn đang tu học» (pi-1 ^1-1025 sekkhā)
    "sekhassa": "người còn đang tu học",           # the person (pi-4 names with their head noun)
    "viparīta": _SL, "viparīte": _SL,              # the text's «điều» kept (sample saṅkhataṃ «cái …»)
    "viparītaṃ": "sai lệch",                       # viparītaṃ hoti «thì trở thành sai lệch»
    "niyāma": "sự cố định",                        # niyāmagamanāya «để đi đến sự cố định» / of aniyāma- (positive part)
    "paṭisambhidā": _TS,                           # (pi-2 «loại hiểu biết thông suốt»: the text has no «loại» here)
    "sammuti": "quy ước", "sammutiṃ": "quy ước",   # pi-2; «theo quy ước», «biết quy ước», «sự thật quy ước»
    "sammutiñāṇa": _QU, "sammutiñāṇaṃ": _QU,
    "anāgatañāṇakathā": "Bàn về hiểu biết về tương lai",
    "paṭuppannañāṇakathā": "Bàn về hiểu biết về hiện tại",
    "phalañāṇakathā": "Bàn về hiểu biết về thành quả",
    "phala": "thành quả", "phale": "thành quả",
    # ---- 5-418 … 5-420 «hiểu biết về sự giải thoát được giải thoát … hiểu biết xem xét lại … người chuyển đổi dòng
    # dõi … người đang thực hành để tự mình chứng nghiệm thành quả vào dòng … hiểu biết của bậc vào dòng, hiểu biết của
    # người đã đạt đến thành quả vào dòng, đã có được, đã chứng đắc, đã tự mình chứng nghiệm … người có được thành quả
    # vào dòng … và nó là hiểu biết của người đã đạt đến thành quả»
    "vimuttiñāṇaṃ": _GT, "vimuttiñāṇaṃ vimuttaṃ": _GT + " được giải thoát",
    "paccavekkhaṇa": "xem xét lại",                # notes-map-2 paccavekkhati
    "arahato": "bậc A-la-hán", "arahā": "bậc A-la-hán",   # notes-map-2 / notes-map-5
    "sotāpannassa": "bậc vào dòng", "sakadāgāmissa": "bậc trở lại một lần", "anāgāmissa": "bậc không trở lại",
    "pattassa": "đã đạt đến",                      # «người đã đạt đến …» (T3 X-phalappatto «đã đạt đến …»)
    "paṭiladdhassa": "đã có được", "sacchikatassa": "đã tự mình chứng nghiệm",   # T3 paṭiladdho / sacchikato
    "adhigatassa sacchikatassa": "đã chứng đắc đã tự mình chứng nghiệm",          # comma dropped (T3 / T11)
    "arahattaṃ sacchikatassa": "trạng thái A-la-hán" + GAP + "đã tự mình chứng nghiệm",
    "sotāpattiphalaṃ sacchikatassa": "thành quả vào dòng" + GAP + "đã tự mình chứng nghiệm",
    "phalaṃ pattassa": "đã đạt đến thành quả",     # «người đã đạt đến thành quả» (Vietnamese order)
    "sotāpattiphala": "thành quả vào dòng", "sakadāgāmiphala": "thành quả trở lại một lần",
    "anāgāmiphala": "thành quả không trở lại", "arahattaphala": "thành quả A-la-hán",   # T3 / T11
    "arahattasacchikiriyāya": "tự mình chứng nghiệm trạng thái A-la-hán",              # T3 / T11
    "sotāpattiphalasacchikiriyāya vimuttaṃ": _TC + " vào dòng được giải thoát",
    "sakadāgāmiphalasacchikiriyāya vimuttaṃ": _TC + " trở lại một lần được giải thoát",
    "anāgāmiphalasacchikiriyāya vimuttaṃ": _TC + " không trở lại được giải thoát",
    "samaṅgissa": "người có được",                 # pi-1 / pi-2 («người có được thành quả …»)
    "sotāpattiphalasamaṅgissa": _CO + " vào dòng",
    "sotāpattiphalasamaṅgissa puggalassa": _CO + " vào dòng",   # the name with its head noun renders both words
                                                                # (T11 aṭṭhamakassa puggalassa)
    "sotāpattiphalasamaṅgissa vimuttaṃ": _CO + " vào dòng được giải thoát",
    "sakadāgāmiphalasamaṅgissa vimuttaṃ": _CO + " trở lại một lần được giải thoát",
    "anāgāmiphalasamaṅgissa vimuttaṃ": _CO + " không trở lại được giải thoát",
    "arahattaphalasamaṅgissa vimuttaṃ": _CO + " A-la-hán được giải thoát",
    # ---- 5-421 … 5-423 «người còn đang tu học biết, thấy hiện tượng thuộc về người đã hoàn tất tu học, chứng nhập và
    # an trú trong điều đã thấy, đã biết, đã tự mình chứng nghiệm, chạm đến bằng thân rồi an trú … điều chưa thấy, chưa
    # biết, chưa tự mình chứng nghiệm … người chuyển đổi dòng dõi có hiểu biết về con đường vào dòng … tôn giả A-nan …
    # trưởng lão Xá-lợi-phất»
    "viharati": "an trú", "phusitvā": "chạm đến", "phusitvā viharati": "chạm đến" + GAP + "an trú",   # T3 / T11
    "viditaṃ": "đã biết", "sacchikataṃ": "đã tự mình chứng nghiệm",
    "aviditaṃ": "chưa biết", "asacchikataṃ": "chưa tự mình chứng nghiệm", "adiṭṭhaṃ": "chưa thấy",   # own a- kept
    "sotāpattimagge": "con đường vào dòng",
    "arahatte ñāṇaṃ": "hiểu biết về trạng thái A-la-hán",
    "sotāpattiphalasacchikiriyāya ñāṇaṃ atthi": _TC + " vào dòng có hiểu biết",   # atthi «có» (map_5 «X ñāṇaṃ atthi»)
    "sāriputto thero": "trưởng lão Xá-lợi-phất",   # notes-map-2 «trưởng lão X»
    # ---- 5-424 … 5-427 «người đang nhập thành tựu thiền với đề mục bao trùm là đất có hiểu biết về điều sai lệch …
    # sự đảo ngược rằng thường còn đối với điều vô thường … hạnh phúc đối với điều khổ đau … tự ngã đối với điều không
    # phải tự ngã … đẹp đối với điều không đẹp … bậc A-la-hán có thể nhập … sự đảo ngược về tri giác, sự đảo ngược về
    # tâm, sự đảo ngược về quan điểm … đối với người nhập thành tựu thiền …, tất cả đều là đất … có ai đó nhập vào đất»
    "samāpattiṃ": "thành tựu thiền",               # pi-1 samāpatti / pi-4 samāpattīnaṃ
    "samāpannassa": _ND,
    "samāpattiṃ samāpannassa": _ND + " thành tựu thiền",
    "viparīte ñāṇaṃ": _HB + " về " + _SL,
    "vipariyeso": "sự đảo ngược",
    "dukkhe": "điều khổ đau",                      # «đối với điều khổ đau» (as Anicce / asubhe «điều …»)
    "niccaṃ": "thường còn", "subhaṃ": "đẹp",
    "samāpajjeyya": "có thể nhập", "samāpajjantassa": "người nhập", "samāpajjati": "nhập",
    "sabbā": "tất cả",                             # sabbeva pathavī «tất cả đều là đất»
    # ---- 5-428 … 5-431 «người không cố định có hiểu biết để đi đến sự cố định … các sự thiết lập tỉnh thức… các nỗ
    # lực đúng đắn… các nền tảng thần thông… các năng lực… các sức mạnh… các chi phần giác ngộ … người này sẽ bước vào
    # sự cố định theo hướng đúng đắn, người này có khả năng thấu hiểu Giáo Pháp»
    "niyatassa": "cố định",                        # of Aniyatassa «người không cố định» (positive part; the standalone
                                                   # Niyatassa is its own keyword, 5-428)
    "niyatassa atthi ñāṇaṃ": "cố định có hiểu biết",
    "gamanāya": "đi đến",                          # «để» frame dropped (pi-2 pahānāya)
    "bojjha": "giác ngộ", "balā": "sức mạnh", "pādā": "nền tảng",   # notes-map-2 / T11
    "okkamissati": "sẽ bước vào", "sammattaniyāmaṃ okkamissati": "sẽ bước vào sự cố định theo hướng đúng đắn",
    "bhabbo": "có khả năng", "abhisametuṃ": "thấu hiểu",            # pi-4 bhabba; notes-map-4 abhisamenti
    # ---- 5-432 / 5-433 «tất cả hiểu biết là hiểu biết thông suốt … bất cứ ai biết quy ước, tất cả những người ấy đều
    # đã đạt đến hiểu biết thông suốt … hiểu biết bao quát tâm … biết tâm người khác … đề mục bao trùm màu vàng … lĩnh
    # vực không gian vô tận … người đang thực hiện sự bố thí… người đang cho y phục… đồ ăn khất thực… chỗ ở… thuốc men
    # và vật dụng chữa bệnh có trí tuệ, trí tuệ ấy là hiểu biết thông suốt»
    "pattā": "đã đạt đến", "paṭisambhidāpattā": "đã đạt đến " + _TS,
    "jānanti": "biết",
    "pariyāye": "bao quát", "cetopariyāye": _CT,   # ceto = tâm (pi chain)
    "cetopariyāye ñāṇaṃ": _HB + " " + _CT,         # head noun first («hiểu biết bao quát tâm»)
    "ākāsānañca": "không gian vô tận",             # T11
    "nevasaññānāsaññā": "không phải tri giác cũng không phải không tri giác",   # T11
    "pīta": "màu vàng",
    "dānaṃ": "sự bố thí",                          # «thực hiện sự bố thí» (pi-2 Dānaṃ)
    "dadantassa": "người đang cho",                # 5-432: override (first rendering «người đang thực hiện»)
    "cīvaraṃ": "y phục", "piṇḍapātaṃ": "đồ ăn khất thực",
    # ---- 5-434 … 5-438 «hiểu biết theo quy ước chỉ có sự thật làm đối tượng, không có điều khác làm đối tượng …
    # thuộc về sự thật quy ước … nhờ hiểu biết ấy mà hiểu biết trọn vẹn khổ đau, dứt bỏ sự phát sinh, tự mình chứng
    # nghiệm sự chấm dứt, tu tập con đường … hiểu rõ “tâm có tham đắm là tâm có tham đắm” … tâm co rút… tâm được định
    # tâm… hiểu biết về đối tượng là sự tiếp xúc nên được gọi là – “hiểu biết bao quát tâm” … hiểu biết bao quát sự
    # tiếp xúc»
    "ārammaṇaṃ": _DT,                              # X-ārammaṇaṃ «có X làm đối tượng» (T11 «lấy … làm» where the text says
                                                   # so); context13: «đối tượng» in «là đối tượng của» (5-441)
    "sammutisaccamhi": "sự thật quy ước",          # «thuộc về sự thật quy ước» (locative frame dropped)
    "sammutiñāṇaṃ saccārammaṇaṃ": _QU + GAP + "có sự thật làm đối tượng",   # «chỉ» = eva skipped
    "cetopariyāye cittārammaṇaṃ": _CT + GAP + "có tâm làm đối tượng",
    "parijānāti": "hiểu biết trọn vẹn", "dukkhaṃ parijānāti": "hiểu biết trọn vẹn khổ đau",   # T5
    "pajahati": "dứt bỏ", "sacchikaroti": "tự mình chứng nghiệm",   # T5 (the text has «tự mình»)
    "saṃkhittaṃ": "co rút",                        # pi-2 (FORMULAS «Tóm lược» is the section label)
    "samāhitaṃ": "được định tâm",                  # pi-2
    "vīta": "đã lìa", "vītarāgaṃ": "đã lìa tham đắm", "vītadosaṃ": "đã lìa sân hận", "vītamohaṃ": "đã lìa si mê",
    "rāgaṃ": "tham đắm", "dosaṃ": "sân hận", "mohaṃ": "si mê",       # of sarāgaṃ … (T11)
    "sarāgaṃ cittaṃ": "tâm có tham đắm", "sadosaṃ cittaṃ": "tâm có sân hận", "samohaṃ cittaṃ": "tâm có si mê",
    "vītarāgaṃ cittaṃ": "tâm đã lìa tham đắm", "avimuttaṃ cittaṃ": "tâm không được giải thoát",   # head noun first
    "phassapariyāye ñāṇaṃ": _HB + " bao quát sự tiếp xúc",
    "anottappapariyāye ñāṇaṃ": _HB + " bao quát sự không biết ghê sợ tội lỗi",
    "anottappa": "sự không biết ghê sợ tội lỗi",   # the text writes «sự» (notes-map-5 anottappī)
    "rāga": "sự tham đắm", "dosa": "sự sân hận", "moha": "sự si mê",   # «đối tượng là sự tham đắm …» (notes-map-2)
    "ārammaṇe": "đối tượng",                       # Phassārammaṇe «về đối tượng là sự tiếp xúc»
    # ---- 5-439 «biết tương lai xét theo gốc rễ, … xét theo nguyên nhân, … căn nguyên, … sự hình thành, … khởi nguồn,
    # … nguồn gốc, … dưỡng chất, … đối tượng, … điều kiện, … sự phát sinh … biết tính chất làm điều kiện nguyên nhân của
    # tương lai, … đối tượng, … chi phối, … kế cận, … kế cận liền ngay»
    "mūlato": "xét theo gốc rễ", "hetuto": "xét theo nguyên nhân", "nidānato": "xét theo căn nguyên",
    "sambhavato": "xét theo sự hình thành", "samuṭṭhānato": "xét theo nguồn gốc", "āhārato": "xét theo dưỡng chất",
    "ārammaṇato": "xét theo đối tượng", "paccayato": "xét theo điều kiện", "samudayato": "xét theo sự phát sinh",
    # (-to with «xét theo», pi-3 khandhato)
    "hetupaccayataṃ": "tính chất làm điều kiện nguyên nhân", "ārammaṇapaccayataṃ": "tính chất làm điều kiện đối tượng",
    "adhipatipaccayataṃ": "tính chất làm điều kiện chi phối", "anantarapaccayataṃ": "tính chất làm điều kiện kế cận",
    "adhipati": "chi phối", "anantara": "kế cận", "samanantara": "kế cận liền ngay",
    # ---- 5-440 sutta «Này A-nan, thành Ba-liên-phất sẽ gặp ba hiểm họa – hoặc từ lửa, hoặc từ nước, hoặc từ sự chia rẽ
    # lẫn nhau»
    "bhavissanti": "sẽ gặp", "antarāyā": "hiểm họa",
    "aggito": "lửa", "udakato": "nước",            # ablative frame «từ» dropped (notes-map-2 arahattā «khỏi»)
    "mithubhedā": "sự chia rẽ lẫn nhau", "mithu": "lẫn nhau",
    # ---- 5-441 «nhờ hiểu biết ấy mà biết hiểu biết ấy … hiểu biết ấy là đối tượng của hiểu biết ấy … dùng sự tiếp xúc
    # ấy mà chạm sự tiếp xúc ấy, dùng cảm giác ấy mà cảm nhận …, … mà nhận ra …, … mà cố ý với …, … mà duy trì tâm trên
    # …, … mà hân hoan với …, … mà ghi nhớ …, … mà hiểu rõ …, dùng thanh kiếm ấy mà chặt …, cái rìu … đẽo, cái rìu nhỏ,
    # cái bào, cây kim … khâu, đầu ngón tay … chạm vào, chóp mũi, đỉnh đầu, phân … rửa, nước tiểu, nước bọt, mủ, máu»
    "ñāṇaṃ ārammaṇaṃ": _HB + GAP + "là đối tượng",   # «hiểu biết ấy là đối tượng của …» (inner «là», sample aññā
                                                      # vedanā «cảm giác … là khác»)
    "paccuppanne": NDE,                            # only in the bracket [khác chính tả (Sī., Syā.): paccuppanne]
    "vedeti": "cảm nhận", "sañjānāti": "nhận ra", "ceteti": "cố ý", "vicāreti": "duy trì tâm",
    "piyāyati": "hân hoan", "sarati": "ghi nhớ", "satiṃ": "sự tỉnh thức",   # the text writes «sự tỉnh thức ấy»
    "khaggaṃ": "thanh kiếm", "pharasuṃ": "cái rìu", "kudhāriṃ": "cái rìu nhỏ", "vāsiṃ": "cái bào",
    "tacchati": "đẽo", "sūciṃ": "cây kim", "sibbeti": "khâu",
    "aṅgulaggaṃ": "đầu ngón tay", "nāsika": "mũi", "aggaṃ": "chóp",   # nāsikaggaṃ «chóp mũi» (aṅgulaggaṃ is its own
                                                                      # keyword)
    "matthakaṃ": "đỉnh đầu", "gūthaṃ": "phân", "kheḷaṃ": "nước bọt", "pubbaṃ": "mủ", "lohitaṃ": "máu",
    "dhovati": "rửa",
    # ---- 5-442 «khi tất cả các tạo tác đã được thấy là vô thường, hiểu biết ấy cũng đã được thấy là vô thường»
    "aniccato": "là vô thường",                    # -to «as» with its «là» (sample saccato «như là sự thật»)
    # ---- 5-443 (the Buddha epithets and the path string = T11 values) «đệ tử mô tả sự phân định của thành quả …
    # mức độ cao thấp của các thành quả, … của các năng lực, … của các hạng người … sự định danh về các khối, … các lĩnh
    # vực nhận biết, … các yếu tố, … các sự thật, … các năng lực, … các hạng người»
    "sāvakassa": "đệ tử", "sāvakassa ñāṇaṃ atthi": "đệ tử có hiểu biết",   # T11 sāvaka («vị» not in the text)
    "kataṃ": "sự phân định", "paññāpeti": "mô tả",
    "indriya": "năng lực", "puggala": "hạng người",   # pi-4 puggalapaññatti «sự định danh về các hạng người»
    "jino": "bậc chiến thắng", "sabbaññū": "bậc toàn tri", "sabbadassāvī": "bậc thấy tất cả",
    "sāmī": "làm chủ", "paṭisaraṇo": "chỗ nương tựa",
    "uppādetā": "người làm sinh khởi", "sañjanetā": "người làm sinh thành", "akkhātā": "người tuyên thuyết",
    "uppannassa": "sinh khởi", "sañjātassa": "sinh thành",   # of an- / asañ- (positive part)
    "aññū": "biết", "vidū": "hiểu", "kovido": "thông thạo",
    # ---- 5-444 uddāna «Tóm tắt của chương này – … Nhóm năm mươi lớn. Tóm tắt của nhóm năm mươi này nữa – Sự được tìm
    # thấy của chúng sinh, người đưa đến, sức mạnh, người tại gia là bậc A-la-hán, và sự giải thoát là thứ năm.»
    "uddānaṃ": "Tóm tắt",                          # map_9 / T11
    "paṇṇāsako": "Nhóm năm mươi",                  # Mahāpaṇṇāsako «Nhóm năm mươi lớn»
    "upaladdhiṃ": "Sự được tìm thấy",              # Sattupaladdhiṃ (line-initial capital kept, map_9 Upalabbho)
    "upaharato": "người đưa đến", "gihissa": "người tại gia", "balaṃ": "sức mạnh",
}

OVERRIDES = {
    "5-419": {"arahatta": "A-la-hán"},             # first rendering «thành quả A-la-hán» (CROSSCHECK: also «trạng thái
    "5-420": {"arahatta": "A-la-hán"},             # A-la-hán» in Arahattasacchikiriyāya)
    "5-428": {"Niyatassa atthi ñāṇaṃ": "người cố định có hiểu biết"},   # the standalone Niyatassa («người cố định»)
    "5-432": {"dadantassa": "người đang thực hiện"},   # first rendering: dānaṃ dadantassa «người đang thực hiện sự bố
                                                       # thí» (CROSSCHECK: then «người đang cho»)
    "5-437": {"vattabbaṃ ñāṇaṃ": _HB + GAP + "nên được gọi là",   # «hiểu biết về đối tượng là sự tiếp xúc nên được
              "vattabbaṃ cetopariyāye ñāṇaṃ": "nên được gọi là " + _HB + " " + _CT},   # gọi là – “hiểu biết bao quát tâm”»
}

ALLOWED = {}


def context13(kw, k, kws, text):
    """Segment rules of this chapter (k: lower-cased keyword). None = no rule."""
    s = set(lc(x) for x in kws)
    if k == "eva":                 # Attheva suttantoti «… thật không?» (context5) / X-ārammaṇaññeva «chỉ có X làm đối
        return "thật" if "suttanto" in s else "chỉ"   # tượng»
    if k == "arahatta":            # «trạng thái A-la-hán» (T3) / «thành quả A-la-hán» (5-419, 5-420: overrides)
        return pick(text, "trạng thái A-la-hán", "A-la-hán")
    if k == "ārammaṇaṃ" and not present("làm đối tượng", text):   # «hiểu biết ấy là đối tượng của …» (5-441)
        return "đối tượng"
    if k in T13:
        return None
    return None


def resolver():
    vi = read_vietnamese(PART)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        text = vi.get(bid, "")
        v = context13(kw, lc(kw), kws, text)
        if v is not None:
            return v
        return value5(kw, kws, T13, text)
    return resolve


def _prior():
    """{kw: {chapter: value}} of the finished chapters' tables (reference only)."""
    out = {}
    for n in (2, 3, 4, 5, 6, 7, 8, 9, 11):
        try:
            m = importlib.import_module(f"map_{n}_vi")
        except Exception:      # noqa: BLE001
            continue
        for k, v in getattr(m, f"T{n}", {}).items():
            out.setdefault(k, {})[n] = v
    return out


def show(lo, hi, only_miss=False):
    res = resolver()
    vi = read_vietnamese(PART)
    pr = _prior()
    for i, (bid, kws) in enumerate(read_keywords(PART)):
        if lo <= i < hi:
            print(f"== {i} [{bid}]")
            er = en_ru(bid)
            for kw in kws:
                try:
                    v = res(bid, kw, kws)
                except KeyError:
                    v = "???"
                flag = "" if v == NDE or (v != "???" and present(v, vi.get(bid, ""))) else " <<MISS"
                if only_miss and not flag:
                    continue
                e = er.get(kw, ["", ""])
                p = pr.get(lc(kw))
                ps = (" T:" + str(p)) if p and any(x != v for x in p.values()) else ""
                print(f"   {kw}={v}  [en:{e[0]} | ru:{e[1]}]{ps}{flag}")


if __name__ == "__main__":
    if sys.argv[1:2] == ["show"]:
        show(int(sys.argv[2]), int(sys.argv[3]), "miss" in sys.argv[4:])
    else:
        build_part(PART, resolver())
        verify(PART, ALLOWED)
