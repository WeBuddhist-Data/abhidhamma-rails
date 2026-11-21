"""Build the Pāli->Vietnamese keyword map for pi-5 (Kathāvatthu) chapter 17: 17-navamavaggo.

usage: python -I -X utf8 -B map_17_vi.py                    (writes 17-navamavaggo.mapped.md and verifies it)
       python -I -X utf8 -B map_17_vi.py show lo hi [miss]   (segments lo..hi with every pair, English | Russian and
                                                             the finished chapters' values where they differ; writes
                                                             nothing)
       python -I -X utf8 -B map_17_vi.py dump [miss]         (every distinct keyword=value; writes nothing)

Importing this module builds nothing (check_parts_vi.py imports it for ALLOWED).
Resolution order per keyword: OVERRIDES[bid][kw] -> context17 (segment rules of this chapter) -> T17 -> context5 ->
the finished chapter tables T14 … T2 (latest first; a value counts only where it stands in this segment, so the
chapter-specific values of other segments do not leak in) -> value5(kw, kws, T17, text) of map_sample_vi (FORMULAS ->
KV -> two-word composition -> the pi-4 chain).
Conventions: pi-1 … pi-4 vi-map-conventions*.md + notes-map-*.md, vi-map-conventions-pi5.md, map-coordinator-rules.md;
new values in notes-map-17.md.
"""
import importlib
import pathlib
import sys
from collections import Counter

sys.dont_write_bytecode = True
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai\mapper-vi")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_vi import (NDE, GAP, build_part, en_ru, join, lc, pick, present, read_keywords,  # noqa: E402
                           read_vietnamese, verify)
from map_sample_vi import FORMULAS, KV, context5, value5  # noqa: E402,F401

PART = "17-navamavaggo"

_DBT = "điều bất tử"                                 # amata (T14 amataṃ; the text always writes «điều bất tử»)
_LDT = "lấy" + GAP + "làm đối tượng"               # -ārammaṇaṃ «xiềng xích lấy điều bất tử làm đối tượng» (T11)
_KLDT = "khi " + _LDT                               # ārabbha «… sinh khởi khi lấy X làm đối tượng» (gerund, «khi» kept)
_ĐT = "đối tượng"                                   # ārammaṇa of sa- / anārammaṇa (keyword without sa- / an-)
_KTT = "khuynh hướng tiềm ẩn"                       # anusaya (T10)
_KTD = "khối tạo tác"
_NBT = "nghiệp bằng thân"                           # kāyakamma (T14)
_LT = "sự lan tỏa"                                  # vipphāro
_LTHT = "sự lan tỏa của sự hướng tâm"               # vitakkavipphāro
_CHT = "có sự hướng tâm đi theo"                    # vitakkānupatita(ṃ)
_TQK = "thuộc quá khứ"
_TTL = "thuộc tương lai"
_THT = "thuộc hiện tại"

T17 = {
    # ---- headings «Chương thứ chín», «(84) 1. Bàn về người thấy lợi ích» … «(94) 11. Bàn về sự được trang bị quá
    # khứ và tương lai»; closers «Phần bàn về … đã hoàn tất.» (kathā = Bàn về, niṭṭhitā = đã hoàn tất: FORMULAS)
    "navamavaggo": "Chương thứ chín",              # heading and «Chương thứ chín.» (as map_12 / map_14)
    "navama": "thứ chín",                          # member (pi-3 navama «thứ chín»)
    "vaggo": "chương",
    "ānisaṃsa": "lợi ích",
    "dassāvī": "người thấy",                       # agent noun with its head noun (ānisaṃsadassāvī «người thấy lợi ích»)
    "amata": _DBT, "amataṃ": _DBT,
    "ārammaṇa": _ĐT,                               # heading members (amatārammaṇa «đối tượng là điều bất tử»,
                                                   # sārammaṇa «có đối tượng», anārammaṇa «không có đối tượng»)
    "anusayā": _KTT, "anusayo": _KTT,
    "ñāṇaṃ": "hiểu biết",
    "atītānāgata": "thuộc quá khứ và tương lai",   # the attribute (heading «đối tượng thuộc quá khứ và tương lai»)
    "atītānāgataṃ": "quá khứ và tương lai",        # the noun («quá khứ và tương lai không tồn tại», 5-561)
    "anāgatārammaṇa": "đối tượng thuộc" + GAP + "tương lai",   # fragment of atītānāgatārammaṇa (head noun first)
    "vitakkānupatita": "điều " + _CHT,             # heading / closer noun «điều có sự hướng tâm đi theo» (the text's
                                                   # «điều» kept, as map_13 viparīta)
    "vitakkānupatitaṃ": _CHT, "anupatitaṃ": "đi theo", "anupatita": "đi theo",
    "vitakka": "sự hướng tâm",
    "vipphāra": "lan tỏa", "vitakkavipphāra": "lan tỏa của sự hướng tâm",   # heading «âm thanh lan tỏa của …»
    "vipphāro": _LT, "vitakkavipphāro": _LTHT,
    "sadda": "âm thanh", "saddo": "âm thanh",
    "yathā": "tùy theo",                           # na yathācittassa «không tùy theo tâm»
    "cittassa": "tâm", "vācā": "lời nói",
    "kāya": "thân", "kāyakamma": _NBT, "kāyakammaṃ": _NBT,
    "samannāgata": "sự được trang bị",             # T12 (heading «Bàn về sự được trang bị …»)
    "samannāgato": "được trang bị",                # pi-2 / pi-4 / T12
    # ---- 5-547 «đối với người chú tâm đến các tạo tác là vô thường, các xiềng xích được dứt bỏ … là khổ đau… là bệnh
    # tật… là ung nhọt… là mũi tên… là điều bất hạnh… là sự đau ốm… là cái xa lạ… là cái tan rã… là tai họa… là tai
    # ương… là điều đáng sợ… là tai nạn… là cái dao động… là cái dễ vỡ… là cái không bền vững… là cái không phải nơi
    # che chở… là cái không phải nơi ẩn náu… là cái không phải nơi nương tựa… là cái không trở thành nơi nương tựa…
    # là cái rỗng không… là cái hư rỗng… là cái trống rỗng… không phải là tự ngã… là sự nguy hại… là có bản chất biến
    # đổi … vừa chú tâm đến …, vừa là người thấy lợi ích nơi Niết-bàn … sự tụ hợp của hai sự tiếp xúc… hai tâm»
    # -to adverbs keep their «là» and the text's classifier (T10 / T13 aniccato «là vô thường»)
    "aniccato": "là vô thường", "dukkhato": "là khổ đau", "rogato": "là bệnh tật", "gaṇḍato": "là ung nhọt",
    "sallato": "là mũi tên", "aghato": "là điều bất hạnh", "ābādhato": "là sự đau ốm", "parato": "là cái xa lạ",
    "palokato": "là cái tan rã", "ītito": "là tai họa", "upaddavato": "là tai ương", "bhayato": "là điều đáng sợ",
    "upasaggato": "là tai nạn", "calato": "là cái dao động", "pabhaṅguto": "là cái dễ vỡ",
    "dhuvato": "là cái" + GAP + "bền vững",        # of addhuvato «là cái không bền vững» (positive part)
    "tāṇato": "là cái" + GAP + "nơi che chở",      # of atāṇato «là cái không phải nơi che chở»
    "leṇato": "là cái" + GAP + "nơi ẩn náu",       # of aleṇato
    "saraṇato": "là cái" + GAP + "nơi nương tựa",  # of asaraṇato (first; asaraṇībhūtato «không trở thành …»)
    "rittato": "là cái rỗng không", "tucchato": "là cái hư rỗng", "suññato": "là cái trống rỗng",
    "attato": "là tự ngã",                         # of anattato «không phải là tự ngã» (positive part)
    "ādīnavato": "là sự nguy hại", "vipariṇāmadhammato": "là có bản chất biến đổi",
    "manasikaroto": "người chú tâm",               # «đối với người chú tâm đến …» (sample paṭijānantaṃ «người …»)
    "manasi karoti": "chú tâm",                    # «vừa chú tâm đến …» («đến» = the governing preposition, dropped)
    "pahīyanti": "được dứt bỏ", "pahānaṃ": "sự dứt bỏ",
    "saṃyojanā pahīyanti": "xiềng xích được dứt bỏ",   # T12
    "saṃyojanānaṃ": "xiềng xích", "saṃyojanā": "xiềng xích", "saṃyojanaṃ": "xiềng xích",
    "samodhānaṃ": "sự tụ hợp", "phassānaṃ": "sự tiếp xúc", "cittānaṃ": "tâm",   # T10
    # ---- 5-548 sutta «tỳ-khưu sống quán sát hạnh phúc nơi Niết-bàn, có tri giác về hạnh phúc, cảm nhận hạnh phúc,
    # thường xuyên, liên tục, liền mạch, dùng tâm mà dứt khoát hướng đến, dùng trí tuệ mà đi sâu vào»
    "bhikkhu": "tỳ-khưu",                          # the text has no «vị» here
    "viharati": "sống", "anupassī": "quán sát", "sukhānupassī viharati": "sống quán sát hạnh phúc",
    "sukha": "hạnh phúc", "saññī": "có tri giác",  # sukhasaññī «có tri giác về hạnh phúc»
    "paṭisaṃvedī": "cảm nhận",                     # sukhapaṭisaṃvedī «cảm nhận hạnh phúc» (no «người» in the text)
    "satataṃ": "thường xuyên", "samitaṃ": "liên tục", "abbokiṇṇaṃ": "liền mạch",   # T12
    "cetasā": "tâm", "paññāya": "trí tuệ",
    "adhimuccamāno": "dứt khoát hướng đến",        # participles: no «khi» in the text
    "pariyogāhamāno": "đi sâu vào",
    # ---- 5-549 / 5-550 «Có phải sự tham đắm sinh khởi khi lấy điều bất tử làm đối tượng không? … điều bất tử là đối
    # tượng của xiềng xích, là đối tượng của nút thắt, … bị sự hiểu sai lệch nắm giữ, … khơi dậy sự tham đắm, hấp
    # dẫn, đáng ham muốn, làm say đắm, trói buộc, làm mê mẩn … khơi dậy sự sân hận, khơi dậy sự phẫn nộ, khơi dậy sự
    # ác cảm … khơi dậy sự si mê, tạo ra sự không biết, làm cho không có mắt, làm chấm dứt trí tuệ, thuộc về phía gây
    # phiền não, không dẫn đến Niết-bàn»
    "ārabbha": _KLDT,
    "uppajjati": "sinh khởi", "uppajjanti": "sinh khởi",
    "ārabbha uppajjati": "sinh khởi " + _KLDT, "ārabbha uppajjanti": "sinh khởi " + _KLDT,
    "rūpaṃ ārabbha": "khi lấy vật chất làm đối tượng",
    "rāgo": "sự tham đắm", "doso": "sự sân hận", "moho": "sự si mê",
    "rāgo uppajjati": "sự tham đắm sinh khởi", "doso uppajjati": "sự sân hận sinh khởi",
    "moho uppajjati": "sự si mê sinh khởi", "saṃyojanā uppajjanti": "xiềng xích sinh khởi",
    "saṃyojaniyaṃ": "đối tượng của xiềng xích", "ganthaniyaṃ": "đối tượng của nút thắt",   # pi-1 X-niyā (bare
    "oghaniyaṃ": "đối tượng của dòng lũ", "yoganiyaṃ": "đối tượng của ách",                # adjective, leading «là»
    "nīvaraṇiyaṃ": "đối tượng của chướng ngại", "upādāniyaṃ": "đối tượng của sự bám víu",  # dropped)
    "saṃkilesiyaṃ": "đối tượng của phiền não", "parāmaṭṭhaṃ": "bị sự hiểu sai lệch nắm giữ",
    "rūpaṃ saṃyojaniyaṃ": "vật chất là đối tượng của xiềng xích",   # inner «là» kept
    "rajaniyaṃ": "hấp dẫn", "kamaniyaṃ": "đáng ham muốn", "madaniyaṃ": "làm say đắm",       # T10 (-nīyo)
    "bandhaniyaṃ": "trói buộc", "mucchaniyaṃ": "làm mê mẩn",
    "dosaṭṭhāniyaṃ": "khơi dậy sự sân hận", "kopaṭṭhāniyaṃ": "khơi dậy sự phẫn nộ",
    "mohaṭṭhāniyaṃ": "khơi dậy sự si mê",
    "kopa": "sự phẫn nộ", "paṭigha": "sự ác cảm",  # members (Paṭighānusayo «… ác cảm»: context17)
    "aññāṇa": "sự không biết", "ñāṇa": "biết",     # of aññāṇakaraṇaṃ «tạo ra sự không biết» (T10 context rule)
    "karaṇaṃ": "tạo ra",                           # first aññāṇakaraṇaṃ (T10 karaṇo; acakkhukaraṇaṃ «làm cho»)
    "acakkhukaraṇaṃ": "làm cho không có mắt",
    "paññā": "trí tuệ", "nirodhiyaṃ": "làm chấm dứt",
    "vighāta": "gây phiền não", "pakkhiyaṃ": "thuộc về phía",
    "saṃvattaniyaṃ": "dẫn đến",                    # of anibbānasaṃvattaniyaṃ «không dẫn đến Niết-bàn» (positive part)
    # ---- 5-551 sutta «Nhận ra Niết-bàn như là Niết-bàn, sau khi nhận ra …, tưởng tượng về Niết-bàn, tưởng tượng
    # trong Niết-bàn, tưởng tượng từ Niết-bàn, tưởng tượng Niết-bàn là của tôi, hoan hỷ với Niết-bàn»
    "sañjānāti": "nhận ra", "sañjānitvā": "sau khi nhận ra",   # gerund «sau khi» (map 4)
    "maññati": "tưởng tượng", "me": "của tôi",     # (FORMULAS tava «của bạn»)
    "abhinandati": "hoan hỷ",
    # ---- 5-552 «có sự hướng đến, sự chú hướng, sự lưu ý, sự chú tâm, chủ ý, sự mong ước, sự mong cầu … cảm giác…
    # tri giác, chủ ý, tâm, niềm tin, sự tinh tấn, sự tỉnh thức, sự định tâm, trí tuệ, sự tham đắm, … quan điểm, sự
    # hoài nghi, sự uể oải, sự xao động, sự không biết hổ thẹn… sự không biết ghê sợ tội lỗi»
    "āvaṭṭanā": "sự hướng đến", "ābhogo": "sự chú hướng", "samannāhāro": "sự lưu ý",   # pi-2
    "manasikāro": "sự chú tâm", "cetanā": "chủ ý", "patthanā": "sự mong ước", "paṇidhi": "sự mong cầu",
    "phasso": "sự tiếp xúc", "vedanā": "cảm giác", "saññā": "tri giác", "cittaṃ": "tâm", "citta": "tâm",
    "saddhā": "niềm tin", "sati": "sự tỉnh thức", "māno": "sự kiêu mạn", "diṭṭhi": "quan điểm",
    "thinaṃ": "sự uể oải", "uddhaccaṃ": "sự xao động", "ahirikaṃ": "sự không biết hổ thẹn",
    "anottappaṃ": "sự không biết ghê sợ tội lỗi",
    "ottappaṃ": "biết ghê sợ tội lỗi",             # of anottappaṃ (positive part, notes-map-5)
    "rūpaṃ": "vật chất",                           # the aggregate (context5)
    # ---- 5-553 «Chẳng phải vật chất có điều kiện sao?»
    "sappaccayaṃ": "có điều kiện", "rūpaṃ sappaccayaṃ": "vật chất có điều kiện",
    # ---- 5-554 / 5-555 / 5-557 «khuynh hướng tiềm ẩn tham đắm dục lạc không có đối tượng … sự tham đắm dục lạc, sự
    # ám ảnh của tham đắm dục lạc, xiềng xích tham đắm dục lạc, dòng lũ dục lạc, ách dục lạc, chướng ngại ý muốn dục
    # lạc … Thuộc về khối nào? Thuộc về khối tạo tác … nằm trong khối tạo tác … khối tạo tác một phần có đối tượng,
    # một phần không có đối tượng … khuynh hướng tiềm ẩn ác cảm, … kiêu mạn, … quan điểm, … hoài nghi, … tham đắm hiện
    # hữu, … vô minh»
    "ārammaṇā": _ĐT, "ārammaṇo": _ĐT,              # of sārammaṇo / anārammaṇo (positive part)
    "khandha": "khối",                             # Katamakkhandhapariyāpanno «Thuộc về khối nào»
    "saṅkhārakkhandha": _KTD,                      # saṅkhārakkhandhapariyāpanno «nằm trong khối tạo tác»
    "saṅkhārakkhandho ekadeso": _KTD + " một phần",
    "ekadeso": "một phần",                         # (T3 / T7 ekadesaṃ)
    "ārammaṇo ekadeso": _ĐT + " một phần",         # «một phần có đối tượng, một phần …» (comma dropped, pi-3)
    "saṅkhāra": "tạo tác",                         # khối tạo tác (pi-1; not T12 «sự thúc đẩy»)
    "vedanākkhandho": "khối cảm giác", "saññākkhandho": "khối tri giác", "viññāṇakkhandho": "khối thức",
    "viññāṇa": "thức",
    "kāmarāgānusayo": _KTT + " tham đắm dục lạc",
    "kāmarāga": "tham đắm dục lạc", "kāma": "dục lạc", "rāga": "tham đắm",   # (context17: «sự tham đắm» 5-562)
    "kāmarāgapariyuṭṭhānaṃ": "sự ám ảnh của tham đắm dục lạc", "pariyuṭṭhānaṃ": "sự ám ảnh",
    "kāmacchanda": "ý muốn dục lạc", "chanda": "ý muốn",
    "kāmacchandanīvaraṇaṃ": "chướng ngại ý muốn dục lạc", "nīvaraṇaṃ": "chướng ngại",
    "yogo": "ách", "ogho": "dòng lũ",              # kāmayogo «ách dục lạc», kāmogho «dòng lũ dục lạc» (T10)
    "cakkhu": "mắt", "cakkhāyatanaṃ": "lĩnh vực mắt",
    "phoṭṭhabba": "vật xúc chạm", "phoṭṭhabbāyatanaṃ": "lĩnh vực vật xúc chạm",
    "paṭighānusayo": _KTT + " ác cảm", "mānānusayo": _KTT + " kiêu mạn", "diṭṭhānusayo": _KTT + " quan điểm",
    "vicikicchānusayo": _KTT + " hoài nghi", "bhavarāgānusayo": _KTT + " tham đắm hiện hữu",
    "avijjānusayo": _KTT + " vô minh",
    "māna": "kiêu mạn", "bhava": "hiện hữu", "bhavarāga": "tham đắm hiện hữu",   # members of the anusaya names
    "avijjā": "vô minh", "avijjogho": "dòng lũ vô minh", "avijjāyogo": "ách vô minh",   # T10
    "avijjāpariyuṭṭhānaṃ": "sự ám ảnh của vô minh", "avijjāsaṃyojanaṃ": "xiềng xích vô minh",
    "avijjānīvaraṇaṃ": "chướng ngại vô minh",
    # ---- 5-556 «khi tâm thiện hay không xác định về mặt đạo đức đang diễn ra, người phàm phu nên gọi là có khuynh
    # hướng tiềm ẩn … Vậy thì sự tham đắm không có đối tượng.»
    "tena hi": "Vậy thì", "tena hi rāgo": "Vậy thì sự tham đắm",
    "kusala": "thiện", "abyākate": "không xác định về mặt đạo đức",
    "citte": "tâm", "abyākate citte": "tâm" + GAP + "không xác định về mặt đạo đức",
    "vattamāne": "khi" + GAP + "đang diễn ra",     # loc. abs. participle keeps «khi» (T14 khaññamāne)
    "citte vattamāne": "khi tâm" + GAP + "đang diễn ra",
    "puthujjano": "người phàm phu", "puthu": "phàm phu", "jano": "người",
    # ---- 5-557 «trí tuệ, năng lực trí tuệ, sức mạnh trí tuệ, quan điểm đúng đắn, chi phần giác ngộ là sự tìm hiểu
    # các hiện tượng»
    "paññindriyaṃ": "năng lực trí tuệ", "indriyaṃ": "năng lực", "balaṃ": "sức mạnh",
    "sambojjhaṅgo": "chi phần giác ngộ", "sambojjha": "giác ngộ", "aṅgo": "chi phần",
    "dhammavicaya": "sự tìm hiểu các hiện tượng",  # inner «các» kept (pi-1 dhammavicayo)
    # ---- 5-558 «bậc A-la-hán có được thức qua mắt nên gọi là người có hiểu biết … người có trí tuệ»
    "arahā": "bậc A-la-hán", "cakkhuviññāṇa": "thức qua mắt",
    "samaṅgī": "có được", "cakkhuviññāṇasamaṅgī": "có được thức qua mắt",   # Vietnamese order (pi-1 samaṅgī)
    "paññavā": "người có trí tuệ",
    # ---- 5-559 … 5-561 «tâm có đối tượng thuộc quá khứ không có đối tượng … Hoặc nếu không có đối tượng … là sai …
    # khi lấy quá khứ làm đối tượng, có sự hướng đến… sự mong cầu»
    "atītārammaṇaṃ": "có đối tượng " + _TQK,       # bahuvrīhi keeps «có» (pi-2 X-ārammaṇo «có đối tượng X»)
    "anāgatārammaṇaṃ": "có đối tượng " + _TTL, "paccuppannārammaṇaṃ": "có đối tượng " + _THT,
    "vā pana": "Hoặc",                             # Hañci vā pana «Hoặc nếu» («nếu» = hañci, no keyword)
    "ārabbha paṇidhi": _KLDT + GAP + "sự mong cầu",
    "atthi": "tồn tại",                            # of natthi «không tồn tại» (5-561; positive part)
    # ---- 5-562 «tất cả tâm đều có sự hướng tâm đi theo … có sự duy trì tâm đi theo, có sự hân hoan đi theo, có hạnh
    # phúc đi theo, có khổ đau đi theo, có niềm vui đi theo, có nỗi buồn đi theo, có sự bình thản đi theo, … có sự
    # không biết ghê sợ tội lỗi đi theo … định tâm không có sự hướng tâm, chỉ có sự duy trì tâm … Đức Thế Tôn đã nói
    # đến ba sự định tâm – định tâm có sự hướng tâm và sự duy trì tâm, …»
    "sabbaṃ": "tất cả",                            # notes-map-5
    "cittaṃ vitakkānupatitaṃ": "tâm" + GAP + _CHT,   # «tâm đều có …» («đều» between)
    "vicāra": "sự duy trì tâm", "pīti": "sự hân hoan", "dukkha": "khổ đau", "somanassa": "niềm vui",
    "domanassa": "nỗi buồn", "upekkhā": "sự bình thản",
    "ottappa": "biết ghê sợ tội lỗi",              # of anottappānupatitaṃ (positive part)
    "anottappa": "sự không biết ghê sợ tội lỗi", "dosa": "sự sân hận",
    "samādhi": "định tâm",                         # «có định tâm …» (5-552 «sự định tâm»: context17)
    "avitakko samādhi": "định tâm không có sự hướng tâm",   # head noun first
    "vitakko vicāro": "sự hướng tâm và sự duy trì tâm",   # of savitakko savicāro (inner «và» kept)
    "vuttā": "đã nói", "vuttā bhagavatā": "Đức Thế Tôn đã nói",   # T14
    # ---- 5-563 «trong mọi trường hợp khi hướng tâm, duy trì tâm, sự lan tỏa của sự hướng tâm là âm thanh … khi tiếp
    # xúc, sự lan tỏa của sự tiếp xúc … khi cảm nhận … khi nhận ra … khi cố ý … khi suy nghĩ … khi nhớ … khi hiểu rõ …
    # âm thanh lan tỏa của sự hướng tâm được nhận biết bằng tai, va chạm vào tai, đi vào tầm của tai»
    "sabbaso": "trong mọi trường hợp",             # adverb keeps its preposition (Sabbattha «ở mọi nơi»)
    "vitakkayato": "khi hướng tâm",                # participles keep «khi»; one «khi» stands for the pair
    "vicārayato": "duy trì tâm",
    "vitakkayato vicārayato": "khi hướng tâm duy trì tâm",   # comma dropped (pi-1)
    "phusayato": "khi tiếp xúc", "vedayato": "khi cảm nhận", "sañjānato": "khi nhận ra",
    "cetayato": "khi cố ý", "sarato": "khi nhớ", "pajānato": "khi hiểu rõ",
    "phassa": "sự tiếp xúc",                       # phassavipphāro «sự lan tỏa của sự tiếp xúc»
    "vitakkavipphāro saddo": _LTHT + " là âm thanh",   # first «sự lan tỏa … là âm thanh» (inner «là» kept);
                                                   # CROSSCHECK «âm thanh lan tỏa của sự hướng tâm»
    "viññeyyo": "được nhận biết", "sota": "tai", "paṭihaññati": "va chạm",   # sotaviññeyyo, sotasmiṃ paṭihaññati
    # ---- 5-564 … 5-567 «lời nói của người không có sự tiếp xúc, … của người có cảm giác, … tri giác, … chủ ý, … tâm
    # … lời nói của người không hướng đến … của người không có sự chú hướng … của người không mong cầu … lời nói do tâm
    # sinh ra, cùng sinh với tâm, sinh khởi cùng một lúc với tâm … người muốn phát biểu thì phát biểu, người muốn kể
    # thì kể, người muốn trò chuyện thì trò chuyện, người muốn nói thì nói … có ai đó nghĩ “tôi sẽ phát biểu điều
    # này” rồi phát biểu điều khác …»
    "phassakassa": "người có sự tiếp xúc",         # -aka «người có X» (of a- / sa-X-akassa; «không» = a-)
    "vedanakassa": "người có cảm giác", "saññakassa": "người có tri giác", "cetanakassa": "người có chủ ý",
    "āvaṭṭentassa": "người hướng đến", "ābhogassa": "người có sự chú hướng",
    "paṇidahantassa": "người mong cầu",
    "samuṭṭhānā": "do" + GAP + "sinh ra", "samuṭṭhānaṃ": "do" + GAP + "sinh ra",   # pi-1 / pi-2
    "kāyakammaṃ cittasamuṭṭhānaṃ": _NBT + " do tâm sinh ra",
    "jātā": "sinh", "jātaṃ": "sinh",               # of sahajātā «cùng sinh với tâm»
    "saha": "cùng",                                # pi-2 (sahajātā «cùng sinh», saha ekuppādā «cùng một lúc»)
    "uppādā": "sinh khởi", "uppādaṃ": "sinh khởi",   # of ekuppādā «sinh khởi cùng một lúc»
    "bhaṇati": "phát biểu", "katheti": "kể", "ālapati": "trò chuyện", "voharati": "nói",
    "kāmo": "muốn",                                # bhaṇitukāmo «người muốn phát biểu» («người» stands for -tu-kāma)
    "kathessāmi": "sẽ kể", "ālapissāmi": "sẽ trò chuyện", "voharissāmi": "sẽ nói",
    "koci": "ai đó",                               # KV
    "aññaṃ": "điều này",                           # first «“tôi sẽ phát biểu điều này” rồi phát biểu điều khác»;
                                                   # CROSSCHECK «điều khác»
    "abhikkamati": "đi tới", "āloketi": "nhìn thẳng", "samiñjeti": "co lại", "pasāreti": "duỗi ra",
    "gacchati": "đi đến", "pasāressāmi": "sẽ duỗi",
    "aññatra": "chỗ này",                          # first «“tôi sẽ đi đến chỗ này” rồi đi đến chỗ khác»;
                                                   # CROSSCHECK «chỗ khác»
    # ---- 5-568 «quá khứ đã chấm dứt, đã mất đi, đã biến đổi, đã biến mất, đã biến mất hoàn toàn … tương lai chưa
    # sinh ra, chưa trở thành, chưa sinh thành, chưa phát sinh, chưa phát sinh rõ rệt, chưa hiện ra»
    "niruddhaṃ": "đã chấm dứt", "vigataṃ": "đã mất đi", "vipariṇataṃ": "đã biến đổi",   # T7 / pi-2
    "atthaṅgataṃ": "đã biến mất", "abbhatthaṅgataṃ": "đã biến mất hoàn toàn",
    "atītaṃ niruddhaṃ": "quá khứ đã chấm dứt",     # notes-map-5
    "ajātaṃ": "chưa sinh ra",                      # own a- kept
    "sañjātaṃ": "sinh thành", "nibbattaṃ": "phát sinh",   # of asañjātaṃ / anibbattaṃ / anabhinibbattaṃ /
    "abhinibbattaṃ": "phát sinh rõ rệt", "pātubhūtaṃ": "hiện ra",   # apātubhūtaṃ «chưa …» (positive part; the
                                                   # text has no «đã» here, unlike T7)
    # ---- 5-569 «được trang bị khối vật chất thuộc quá khứ … ba khối vật chất … năm khối thuộc quá khứ … mười lăm
    # khối … lĩnh vực mắt thuộc quá khứ … mười hai lĩnh vực nhận biết … ba mươi sáu lĩnh vực nhận biết … yếu tố mắt
    # … mười tám yếu tố … năm mươi bốn yếu tố … năng lực mắt … hai mươi hai năng lực … sáu mươi sáu năng lực»
    "rūpakkhandhena": "khối vật chất", "rūpa": "vật chất", "khandhena": "khối", "khandhehi": "khối",
    "atītehi khandhehi": "khối " + _TQK,
    "cakkhāyatanena": "lĩnh vực mắt", "atītena cakkhāyatanena": "lĩnh vực mắt " + _TQK,
    "anāgatena cakkhāyatanena": "lĩnh vực mắt " + _TTL, "paccuppannena cakkhāyatanena": "lĩnh vực mắt " + _THT,
    "āyatanehi": "lĩnh vực nhận biết", "dhātuyā": "yếu tố", "dhātūhi": "yếu tố", "cakkhudhātuyā": "yếu tố mắt",
    "cakkhundriyena": "năng lực mắt", "indriyehi": "năng lực", "indriyena": "năng lực",
    "pannarasahi": "mười lăm", "dvādasahi": "mười hai", "aṭṭhārasahi": "mười tám", "bāvīsati": "hai mươi hai",
    "chattiṃsa": "ba mươi sáu", "catupaññāsa": "năm mươi bốn", "chasaṭṭhi": "sáu mươi sáu",   # notes-map-5
    # ---- 5-570 «có người tu thiền với tám sự giải thoát, đạt được bốn tầng thiền theo ý muốn, đạt được chín thành tựu
    # thiền an trú tuần tự … Chương thứ chín. Tóm tắt của chương này – … các khuynh hướng tiềm ẩn không có đối tượng,
    # cũng vậy, hiểu biết …»
    "vimokkha": "sự giải thoát", "jhāyī": "người tu thiền", "jhānānaṃ": "tầng thiền",
    "lābhī": "đạt được",                           # nikāmalābhī «đạt được … theo ý muốn» (pi-4 «có được» where written)
    "samāpattīnaṃ": "thành tựu thiền", "vihāra": "an trú", "anupubba": "tuần tự",
    "evamevaṃ": "cũng vậy",                        # T12
    "uddānaṃ": "Tóm tắt",
}

OVERRIDES = {
}

ALLOWED = {}


def _tables():
    """[(chapter, table)] of the finished chapters (2 … 14)."""
    out = []
    for n in range(2, 15):
        try:
            m = importlib.import_module(f"map_{n}_vi")
        except Exception:      # noqa: BLE001
            continue
        t = getattr(m, f"T{n}", None)
        if t:
            out.append((n, t))
    return out


_TABLES = _tables()
PRIOR = {}
for _n, _t in _TABLES:
    PRIOR.update(_t)
TABLE = {**PRIOR, **T17}


def context17(kw, k, kws, text):
    """Segment rules of this chapter (k: lower-cased keyword). None = no rule."""
    s = set(lc(x) for x in kws)
    if k == "ārammaṇaṃ":           # amatārammaṇaṃ «lấy điều bất tử làm đối tượng» (5-549, 5-551, 5-570: first) / of
        if "amata" in s:                           # sārammaṇaṃ / anārammaṇaṃ «(không) có đối tượng»
            return _LDT
        return _ĐT
    if k == "rāga":                # kāmarāga- / bhavarāgānusayo «tham đắm» / rāgānupatitaṃ «có sự tham đắm đi theo»
        return "sự tham đắm" if "vitakkānupatita" in s else "tham đắm"
    if k == "paṭigha":             # paṭighaṭṭhāniyaṃ «khơi dậy sự ác cảm» / Paṭighānusayo «khuynh hướng tiềm ẩn ác cảm»
        return "ác cảm" if "paṭighānusayo" in s else "sự ác cảm"
    if k == "vicikicchā":          # the list «sự hoài nghi» (5-552) / vicikicchānusayo «… hoài nghi» (5-555)
        return "hoài nghi" if "vicikicchānusayo" in s else "sự hoài nghi"
    if k == "samādhi":             # the list «sự định tâm» (5-552) / «định tâm không có sự hướng tâm …» (5-562)
        return "sự định tâm" if "patthanā" in s else "định tâm"
    if k == "anāgatārammaṇaṃ":     # «có đối tượng thuộc tương lai» / fragment of atītānāgatārammaṇaṃ «có đối tượng
        if "atītānāgataṃ" in s or "atītānāgata" in s or "vitakkānupatitaṃ" in s:   # thuộc quá khứ và tương lai»
            return "có đối tượng thuộc" + GAP + "tương lai"
        return "có đối tượng " + _TTL
    if k == "pasāreti":            # «người muốn duỗi ra thì duỗi ra» (5-566) / «rồi duỗi cái khác» (5-567)
        return pick(text, "duỗi ra", "duỗi")
    return None


def resolver():
    vi = read_vietnamese(PART)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        text = vi.get(bid, "")
        k = lc(kw)
        v = context17(kw, k, kws, text)
        if v is not None:
            return v
        if k in T17:
            return T17[k]
        v = context5(kw, k, kws, text)
        if v is not None:
            return v
        for n, t in reversed(_TABLES):             # the finished chapters (latest first) where their value stands in
            if k in t and (t[k] == NDE or present(t[k], text)):   # this segment
                return t[k]
        return value5(kw, kws, T17, text)
    return resolve


def _prior_values(k):
    return {n: t[k] for n, t in _TABLES if k in t}


def show(lo, hi, only_miss=False):
    res = resolver()
    vi = read_vietnamese(PART)
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
                p = _prior_values(lc(kw))
                ps = (" T:" + str(p)) if p and any(x != v for x in p.values()) else ""
                src = " [T17]" if lc(kw) in T17 else (" [prior]" if p else "")
                print(f"   {kw}={v}{src}  [en:{e[0]} | ru:{e[1]}]{ps}{flag}")


def dump(only_miss=False):
    res = resolver()
    vi = read_vietnamese(PART)
    c, miss, where = Counter(), Counter(), {}
    for bid, kws in read_keywords(PART):
        for kw in kws:
            try:
                v = res(bid, kw, kws)
            except KeyError:
                v = "???"
            c[(kw, v)] += 1
            where.setdefault((kw, v), []).append(bid)
            if v == "???" or (v != NDE and not present(v, vi.get(bid, ""))):
                miss[(kw, v)] += 1
    for (kw, v), n in sorted(c.items()):
        m = miss.get((kw, v), 0)
        if only_miss and not m:
            continue
        print(f"{kw}={v}  [{n}] {where[(kw, v)][:5]}" + (f"  MISS {m}" if m else ""))
    print("distinct", len(c), "miss-pairs", len(miss), "miss-total", sum(miss.values()))


def look(words):
    """Values of the finished chapter tables and of the pi-1 … pi-4 maps (reference only)."""
    from map_common_vi import pi1_map_values, pi2_map_values, pi3_map_values, pi4_map_values
    for w in words:
        k = lc(w)
        print(w, "T:", _prior_values(k), "KV:", KV.get(k), "F:", FORMULAS.get(k))
        for name, f in (("pi1", pi1_map_values), ("pi2", pi2_map_values), ("pi3", pi3_map_values),
                        ("pi4", pi4_map_values)):
            try:
                v = f(w)
            except Exception:  # noqa: BLE001
                v = None
            if v:
                print("   ", name, v)


if __name__ == "__main__":
    if sys.argv[1:2] == ["look"]:
        look(sys.argv[2:])
    elif sys.argv[1:2] == ["show"]:
        show(int(sys.argv[2]), int(sys.argv[3]), "miss" in sys.argv[4:])
    elif sys.argv[1:2] == ["dump"]:
        dump(sys.argv[2:3] == ["miss"])
    else:
        build_part(PART, resolver())
        verify(PART, ALLOWED)
