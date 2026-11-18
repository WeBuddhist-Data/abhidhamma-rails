"""Pāli->Vietnamese keyword map for pi-1 part 5-atthakathakandam (Aṭṭhakathākaṇḍaṃ: the matrix items explained
by the classes of mind, ^1-4-0 … ^1-1616).

usage: python -I -X utf8 map_5_vi.py                 (writes 5-atthakathakandam.mapped.md and verifies it)
       python -I -X utf8 map_5_vi.py dump [miss]     (prints every distinct keyword=value with count and the first
                                                      segments; with «miss» only the presence misses; writes nothing)

Importing this file writes nothing. It imports map_4-02_4-03_vi.py (and through it map_4-01_vi.py,
map_3-02_3-03_vi.py, map_2-05_3-01_vi.py, map_2-04_vi.py, map_2-02_2-03_vi.py); none of them rewrites its output
on import.
Resolution order per keyword:
  OVERRIDES[bid][kw] -> SAME (segments whose Pāli and keywords equal an earlier mapped segment: that line's values)
  -> context5() (segment rules of this part) -> ADD5 -> the 4-02/4-03 tables (_val: ADD402, then the 4-01
  _value: ADD401, MATRIX, «dhammā X», the 3-02/3-03 value(), T05) -> ch2_value(T05);
  a «dhammā X» value not found contiguous becomes «hiện tượng … X» (as 4-01).
The earlier parts' segment rules (their context() functions) are NOT applied: they key on keyword sets of other
chapters; every value used here is listed by `dump` and was checked against the segments.
Conventions: vi-map-conventions.md and the earlier notes-map-*.md; new: notes-map-5.md.
"""
import importlib.util
import pathlib
import sys
from collections import Counter

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from map_common_vi import (CORE, GAP, NDE, build_part, ch2_value, lc, present,  # noqa: E402
                           read_keywords, read_vietnamese, verify)

_spec = importlib.util.spec_from_file_location("map_4_02_4_03_vi", HERE / "map_4-02_4-03_vi.py")
_p402 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_p402)          # import only: its __main__ block does not run
_p401 = _p402._p401
T05 = _p401.T05

PART = "5-atthakathakandam"

# ---------------------------------------------------------------------------------------------- fixed phrases
_KHONG_XD = "không xác định về mặt đạo đức"
_DITG = "sự mắc kẹt trong các quan điểm"
_KVK = "quả của nghiệp và chức năng"         # vipākato ca kiriyato ca «(thiện, quả của nghiệp và chức năng)»
_NUM = {"ekaka": "một", "duka": "hai", "tika": "ba", "catukka": "bốn", "pañcaka": "năm"}


def _jh(a, b, where):
    """<a><b>-jjhānā: «<a> tầng thiền <where> theo phương pháp chia bốn và <b> tầng thiền theo phương pháp chia năm»"""
    return (f"{_NUM[a]} tầng thiền {where} theo phương pháp chia bốn và {_NUM[b]} tầng thiền "
            f"theo phương pháp chia năm")


# New keys and the readings of this part (this table precedes the earlier tables).
ADD5 = {
    # ---------------------------------------------------------------- headings and closing lines
    "aṭṭhakathā": "giải thích",                          # Aṭṭhakathākaṇḍaṃ «Phần giải thích»
    "atthuddhāro": "giải thích ý nghĩa",                 # «Giải thích ý nghĩa các bộ ba / đôi»; «Phần giải thích ý nghĩa …»
    "niṭṭhito": "đã hoàn tất",
    # ---------------------------------------------------------------- planes and classes of mind
    "bhūmīsu": "cõi",                                    # catūsu / tīsu bhūmīsu «thuộc bốn / ba cõi»
    "kusalaṃ": "thiện", "akusalaṃ": "bất thiện",         # «tâm thiện / bất thiện …» («tâm» implied, as 2-04 akusalāni)
    "kusalesu": "thiện", "akusalesu": "bất thiện",       # «trong tâm thiện …», sabbākusalesu «trong toàn bộ tâm bất thiện»
    "kusalato": "thiện", "akusalato": "bất thiện",       # «bốn loại tâm thiện …», «(thiện, …)»
    "kusalassa": "thiện", "akusalassa": "bất thiện",     # «quả của nghiệp thiện / bất thiện»
    "akusalacitta": "tâm bất thiện",                     # Dvādasa akusalacittuppādā «Mười hai loại tâm bất thiện»
    "akusala": "bất thiện", "kusala": "thiện",
    "kiriyato": "chức năng",                             # «loại tâm chức năng», «(… và chức năng)»
    "kiriyesu": "chức năng",                             # tīsu bhūmīsu kiriyesu «trong tâm chức năng thuộc ba cõi»
    "kiriya": "mang tính chức năng",                     # kiriyahetu «gốc rễ mang tính chức năng»
    "kiriyābyākataṃ": "chức năng " + _KHONG_XD,          # «tâm chức năng không xác định về mặt đạo đức»
    "abyākataṃ": _KHONG_XD, "abyākatā": _KHONG_XD, "abyākata": _KHONG_XD,
    "vipākato": "quả của nghiệp",                        # «loại quả của nghiệp thiện …», «(thiện, quả của nghiệp …)»
    "vipākato ca kiriyato": _KVK,
    "kusalato ca vipākato": "thiện và quả của nghiệp",   # «(thiện và quả của nghiệp)» of the world-transcending absorptions
    "vipāka": "quả của nghiệp",                          # vipākahetu «gốc rễ là quả của nghiệp»
    "uppādā": "loại", "uppādo": "loại", "uppāde": "loại", "uppādesu": "loại",   # member of cittuppāda «loại tâm»
    "cittuppādā": "loại tâm", "cittuppādo": "loại tâm", "cittuppāde": "loại tâm", "cittuppādesu": "loại tâm",
    "citta": "tâm",
    "sahagatacitta": "tâm" + GAP + "đi kèm",             # -sahagatacittuppādā «loại tâm có X đi kèm»
    "sahagato citta": "tâm" + GAP + "đi kèm", "sahagatesu citta": "tâm" + GAP + "đi kèm",
    "vippayuttacitta": "tâm" + GAP + "không gắn liền",   # ñāṇavippayuttacittuppādā «loại tâm … không gắn liền với hiểu biết»
    "vippayutte citta": "tâm" + GAP + "không gắn liền",
    "ahetuke citta": "tâm" + GAP + "không có gốc rễ",    # kāmāvacarakiriyato ahetuke cittuppāde «các loại tâm chức năng … không có gốc rễ»
    "sabbaṃ": "toàn bộ",                                 # sabbaṃ akusalaṃ «toàn bộ tâm bất thiện»
    "avasesaṃ": "còn lại", "avasesaṃ akusalaṃ": "bất thiện còn lại",   # «tâm bất thiện còn lại»
    "kāmāvacarassa": "thuộc cõi dục lạc", "avacarassa": "thuộc cõi",
    "kāmāvacara": "thuộc cõi dục lạc", "kāmāvacaraṃ": "thuộc cõi dục lạc", "avacara": "thuộc cõi",
    "avacaraṃ": "thuộc cõi", "rūpāvacara": "thuộc cõi hình sắc", "rūpāvacaraṃ": "thuộc cõi hình sắc",
    "kāma": "dục lạc", "rūpa": "hình sắc", "arūpa": "không hình sắc",
    "dvādasa": "mười hai", "ekādasa": "mười một", "dasa": "mười",
    # accompanied / associated
    "sahagata": "đi kèm", "sahagatā": "đi kèm", "sahagato": "đi kèm", "sahagataṃ": "đi kèm", "sahagatesu": "đi kèm",
    "somanassa": "niềm vui", "upekkhā": "sự bình thản", "domanassa": "nỗi buồn",
    "lobha": "sự tham lam", "vicikicchā": "sự hoài nghi", "uddhacca": "sự xao động",
    "somanassasahagata": "có niềm vui đi kèm", "somanassasahagatā": "có niềm vui đi kèm",
    "upekkhāsahagata": "có sự bình thản đi kèm", "upekkhāsahagatā": "có sự bình thản đi kèm",
    "domanassasahagata": "có nỗi buồn đi kèm", "domanassasahagatesu": "có nỗi buồn đi kèm",
    "lobhasahagata": "có sự tham lam đi kèm", "lobhasahagatesu": "có sự tham lam đi kèm",
    "vicikicchāsahagato": "có sự hoài nghi đi kèm", "vicikicchāsahagataṃ": "có sự hoài nghi đi kèm",
    "vicikicchāsahagatesu": "có sự hoài nghi đi kèm",
    "uddhaccasahagato": "có sự xao động đi kèm", "uddhaccasahagataṃ": "có sự xao động đi kèm",
    "uddhaccasahagatesu": "có sự xao động đi kèm",
    "pītisahagatā": "có sự hân hoan đi kèm", "sukhasahagatā": "có hạnh phúc đi kèm",
    "pīti": "sự hân hoan", "sukha": "hạnh phúc",
    "dukkha": "sự đau khổ",                              # dukkhasahagataṃ kāyaviññāṇaṃ «thức qua thân có sự đau khổ đi kèm»
    "kāyaviññāṇaṃ": "thức qua thân",
    "sampayutta": "gắn liền", "sampayuttā": "gắn liền", "sampayutte": "gắn liền", "sampayutto": "gắn liền",
    "vippayutta": "không gắn liền", "vippayuttā": "không gắn liền", "vippayutte": "không gắn liền",
    "ñāṇa": "hiểu biết", "ñāṇavippayutta": "không gắn liền với hiểu biết",
    "ñāṇavippayutte": "không gắn liền với hiểu biết",
    "diṭṭhigata": _DITG,
    "diṭṭhigatavippayutta": "không gắn liền với " + _DITG, "diṭṭhigatavippayuttā": "không gắn liền với " + _DITG,
    "vippayuttalobha": "sự tham lam" + GAP + "không gắn liền",   # «có sự tham lam đi kèm và không gắn liền với …»
    "vippayuttā lobha": "sự tham lam" + GAP + "không gắn liền",
    "moho": "sự si mê", "mohaṃ": "sự si mê",
    "sahagato moho": "sự si mê" + GAP + "đi kèm",        # «sự si mê có sự hoài nghi / xao động đi kèm»
    "sahagataṃ mohaṃ": "sự si mê" + GAP + "đi kèm",
    "sahagataṃ uddhaccasahagataṃ mohaṃ": "sự si mê có sự xao động đi kèm",
    "sasaṅkhārikesu": "có sự thúc đẩy",                  # sasaṅkhārikesu akusalesu «các loại tâm bất thiện có sự thúc đẩy»
    # arising
    "uppannaṃ": "sinh khởi", "uppanne": "sinh khởi", "uppanno": "sinh khởi",   # etthuppanna X «X sinh khởi trong đó»
    "uppajjati": "sinh khởi", "uppajjanti": "sinh khởi",
    "uppanne vitakkavicāre": "sự hướng tâm và sự duy trì tâm sinh khởi",
    "uppannaṃ vicāraṃ": "sự duy trì tâm sinh khởi", "uppannaṃ vitakkaṃ": "sự hướng tâm sinh khởi",
    "uppanno ca vicāro": "sự duy trì tâm sinh khởi", "uppanne hetū": "gốc rễ sinh khởi",
    "sahajāto": "cùng sinh khởi",                        # vitakkasahajāto «cùng sinh khởi với sự hướng tâm»
    "ekato": "cùng", "hetū ekato uppajjanti": "gốc rễ cùng sinh khởi",   # «hai hoặc ba gốc rễ cùng sinh khởi»
    "ṭhapetvā": "ngoại trừ",
    "siyā": "đôi khi",
    # na vattabbā (the 4-02 frame «không nên nói rằng nó / chúng “…”»; na is not a keyword)
    "vattabbā": "nên nói", "vattabbo": "nên nói", "vattabbaṃ": "nên nói",
    "vattabbo savitakkasavicāro": "nên nói" + GAP + "có sự hướng tâm và sự duy trì tâm",
    "vattabbaṃ pītisahagatanti": "nên nói" + GAP + "có sự hân hoan đi kèm",
    "vattabbā parittārammaṇā": "nên nói" + GAP + "có đối tượng hạn hẹp",
    "vattabbā maggārammaṇā": "nên nói" + GAP + "lấy con đường làm đối tượng",
    "vattabbā anuppannā": "nên nói" + GAP + "chưa sinh khởi",
    "vattabbā atītārammaṇā": "nên nói" + GAP + "có đối tượng thuộc quá khứ",
    "vattabbaṃ ajjhattārammaṇanti": "nên nói" + GAP + "có đối tượng thuộc về bản thân",
    "savitakkasavicāro": "có sự hướng tâm và sự duy trì tâm",
    # ---------------------------------------------------------------- absorptions
    "jhānaṃ": "tầng thiền", "jhānā": "tầng thiền", "jhāne": "tầng thiền", "jhānassa": "tầng thiền",
    "catutthaṃ jhānaṃ": "tầng thiền thứ tư", "catutthassa jhānassa": "tầng thiền thứ tư",
    "lokuttara": "vượt thế gian", "lokuttaraṃ": "vượt thế gian",
    "lokuttaraṃ catutthaṃ jhānaṃ": "tầng thiền thứ tư vượt thế gian",
    "lokuttaraṃ paṭhamaṃ jhānaṃ": "tầng thiền thứ nhất vượt thế gian",
    "lokuttarapañcakanaye dutiyaṃ jhānaṃ": "tầng thiền thứ hai vượt thế gian theo phương pháp chia năm",
    "pañcaka": "chia năm", "naye": "phương pháp", "pañcakanaye": "theo phương pháp chia năm",
    "āruppā": "tầng thiền không hình sắc",               # cattāro āruppā «bốn tầng thiền không hình sắc»
    "arūpāvacarā": "thuộc cõi không hình sắc",           # cattāro arūpāvacarā «bốn loại tâm thuộc cõi không hình sắc»
    "viññāṇañcāyatanaṃ": "lĩnh vực thức vô tận", "ānañcāyatanaṃ": "lĩnh vực" + GAP + "vô tận",
    "ānañca": "vô tận", "ākāsa": "không gian", "ākiñcañña": "không có gì cả",
    "asaññā": "không tri giác", "saññā": "tri giác",     # of nevasaññānāsaññāyatanaṃ (2-04)
    # ---------------------------------------------------------------- minds without roots, mind elements
    "viññāṇāni": "loại thức", "pañcaviññāṇāni": "năm loại thức",   # dvepañcaviññāṇāni «hai nhóm năm loại thức»
    "dhātu": "yếu tố", "dhātuyo": "yếu tố", "mano": "ý",
    "manodhātu": "yếu tố ý", "manodhātuyo": "yếu tố ý",
    "manoviññāṇa": "ý thức", "manoviññāṇadhātu": "yếu tố ý thức",
    "hetuka": "có gốc rễ",                               # of ahetuka «không có gốc rễ» (positive part, 2-05)
    "kiriyāmano": "ý mang tính chức năng", "kiriyāmanodhātu": "yếu tố ý mang tính chức năng",
    "kiriyāhetukamanoviññāṇa": "ý thức mang tính chức năng không có gốc rễ",            # commas dropped
    "kiriyāhetukamanoviññāṇadhātu": "yếu tố ý thức mang tính chức năng không có gốc rễ",
    "dhātu upekkhāsahagatā": "yếu tố" + GAP + "có sự bình thản đi kèm",
    "manoviññāṇadhātu upekkhāsahagatā": "yếu tố ý thức" + GAP + "có sự bình thản đi kèm",
    # ---------------------------------------------------------------- roots
    "kusalahetu": "gốc rễ thiện", "kusalahetū": "gốc rễ thiện", "akusalahetū": "gốc rễ bất thiện",
    "abyākatahetū": "gốc rễ " + _KHONG_XD,
    "vipākahetu": "gốc rễ là quả của nghiệp", "kiriyahetu": "gốc rễ mang tính chức năng",
    "alobho": "sự không tham lam", "adoso": "sự không sân hận", "amoho": "sự không si mê",
    "lobho": "sự tham lam", "doso": "sự sân hận",
    "hetu": "gốc rễ", "hetū": "gốc rễ",
    # ---------------------------------------------------------------- paths, fruits, material form, nibbāna
    "rūpañca": "vật chất", "rūpañca nibbānañca": "vật chất và Niết-bàn",
    "rūpaṃ": "vật chất", "rūpaṃ nibbānañca": "vật chất" + GAP + "và Niết-bàn",   # «vật chất còn lại và Niết-bàn»
    "nibbānañca anārammaṇā": "Niết-bàn không có đối tượng",
    "sāmaññaphalāni nibbānañca": "thành quả của đời sống sa-môn và Niết-bàn",
    "indriyabaddharūpañca nibbānañca": "vật chất" + GAP + "gắn kết với các năng lực và Niết-bàn",   # of anindriya…
    "baddha": "gắn kết", "indriya": "năng lực",          # anindriyabaddha «không gắn kết với các năng lực»
    "ariya": "cao quý",                                  # cattāro ariyamaggā «bốn con đường cao quý»
    "sekkha": "thuộc về người còn đang tu học",          # nevasekkhanāsekkhā
    "kammassa": "nghiệp", "kammassa katattā": "do nghiệp đã được tạo",
    "avasesañca": "còn lại", "avasesañca rūpaṃ": "vật chất còn lại",
    "kāya": "thân",                                      # kāyaviññatti, kāyagantho (CH2 «thân tinh thần» is the six pairs)
    # ---------------------------------------------------------------- triads (items not in MATRIX as worded here)
    "atītā": "thuộc quá khứ", "anāgatā": "thuộc tương lai", "paccuppannā": "thuộc hiện tại",
    "niyogā": "nhất thiết",                              # Niyogā anāgatārammaṇā natthi «… nhất thiết có đối tượng …»
    "dhammā nevācayagāmināpacayagāmino": "hiện tượng không dẫn đến sự tích lũy cũng không dẫn đến sự giảm trừ",
    "kenaci": "một loại thức nào đó",
    "dhammā kenaci viññeyyā": "hiện tượng" + GAP + "một loại thức nào đó có thể nhận biết",
    "dhammā": "hiện tượng",
    "niyatā": "cố định",                                 # also the positive part of aniyatā «không cố định»
    # ---------------------------------------------------------------- defilement groups
    "āsava": "ô nhiễm", "saṃyojana": "xiềng xích", "gantha": "nút thắt", "nīvaraṇa": "chướng ngại",
    "upādāna": "sự bám víu", "kilesa": "phiền não", "parāmāsa": "sự hiểu sai lệch",
    "āsavā": "ô nhiễm", "āsavo": "ô nhiễm", "saṃyojanā": "xiềng xích", "saṃyojanaṃ": "xiềng xích",
    "ganthā": "nút thắt", "gantho": "nút thắt", "nīvaraṇā": "chướng ngại", "nīvaraṇaṃ": "chướng ngại",
    "upādānā": "sự bám víu", "kilesā": "phiền não",
    "parāmāso": "sự hiểu sai lệch", "parāmāsā": "sự hiểu sai lệch", "parāmāsaṃ": "sự hiểu sai lệch",
    "oghā": "dòng lũ", "yogā": "ách",
    # «Teva / Tāneva X X ceva Y ca» = «Chính những X ấy vừa là X …»
    "saṃyojanāni saṃyojanā": "xiềng xích" + GAP + "xiềng xích",
    "nīvaraṇāni nīvaraṇā": "chướng ngại" + GAP + "chướng ngại",
    "upādānāni upādānā": "sự bám víu" + GAP + "sự bám víu",
    "kilesā kilesā": "phiền não" + GAP + "phiền não",
    "bhava": "hiện hữu",                                 # bhavāsavo «ô nhiễm hiện hữu», bhavarāga «tham đắm hiện hữu»
    "avijjā": "vô minh", "diṭṭhi": "quan điểm",
    "rāgasaṃyojanaṃ": "xiềng xích tham đắm",            # of kāma- / bhavarāgasaṃyojanaṃ
    "parāmāsasaṃyojanaṃ": "xiềng xích hiểu sai lệch",   # of sīlabbataparāmāsasaṃyojanaṃ
    "diṭṭhisaṃyojanaṃ": "xiềng xích quan điểm",
    "abhiniveso": "sự cố chấp", "abhiniveso kāyagantho": "nút thắt của thân bằng sự cố chấp",
    "parāmāso kāyagantho": "nút thắt của thân bằng sự hiểu sai lệch",
    "abhijjhākāyagantho": "nút thắt của thân bằng sự thèm muốn",
    "abhijjhā": "sự thèm muốn", "byāpādo": "sự ác ý",
    "chanda": "ý muốn",                                  # kāmacchandanīvaraṇaṃ «chướng ngại ý muốn dục lạc»
    "diṭṭhiparāmāso": "sự hiểu sai lệch dưới dạng quan điểm",
    "māno": "sự kiêu mạn", "uddhaccaṃ": "sự xao động", "ahirikaṃ": "sự không biết hổ thẹn",
    "anottappaṃ": "sự không biết ghê sợ tội lỗi", "vatthūni": "chỗ dựa",
    # ---------------------------------------------------------------- great intermediate pairs
    "cittā": "tâm", "cetasikā": "đồng hành với tâm",     # the matrix adjective (4-02 rule: no cittacetasikā here)
    "cittañca": "tâm", "khandho": "khối", "vedanā": "cảm giác",
    "samuṭṭhānā": "do" + GAP + "sinh ra", "samuṭṭhāna": "do" + GAP + "sinh ra",
    "saṃsaṭṭha": "hòa lẫn", "saṃsaṭṭhā": "hòa lẫn",
    "kāyaviññatti": "sự biểu lộ bằng thân", "vacīviññatti": "sự biểu lộ bằng lời nói",
    "viññatti": "sự biểu lộ", "vacī": "lời nói",
    "cittajaṃ": "sinh từ tâm", "hetukaṃ": "có" + GAP + "làm gốc rễ",   # cittahetukaṃ «có tâm làm gốc rễ» (3-02)
    "yaṃ": "bất cứ" + GAP + "nào",                       # yaṃ vā panaññampi atthi rūpaṃ (3-02)
    "upādāya": "phái sinh từ", "upādāya rūpaṃ": "vật chất phái sinh từ",
    "bhūtā": "yếu tố", "mahābhūtā": "yếu tố cơ bản",
}
for _a, _b in (("tika", "catukka"), ("tika", "tika"), ("duka", "tika"), ("duka", "duka"), ("ekaka", "duka")):
    ADD5[f"lokuttara{_a}{_b}jjhānā"] = _jh(_a, _b, "vượt thế gian")

# Segments whose Pāli and keywords equal an earlier mapped segment: the earlier line's values (checked equal).
SAME_SRC = {"1-1414": ("4-01-nikkhepakandam", "1-1023"), "1-1415": ("4-01-nikkhepakandam", "1-1024"),
            "1-1547": ("4-02-nikkhepakandam", "1-1213"), "1-1548": ("4-02-nikkhepakandam", "1-1214"),
            "1-1549": ("4-02-nikkhepakandam", "1-1215"), "1-1602": ("4-02-nikkhepakandam", "1-1288"),
            "1-1604": ("4-02-nikkhepakandam", "1-1290"), "1-1606": ("4-02-nikkhepakandam", "1-1292")}


def _load_same():
    out = {}
    mine = dict(read_keywords(PART))
    for bid, (part, src) in SAME_SRC.items():
        lines = (HERE / f"{part}.mapped.md").read_text(encoding="utf-8").splitlines()
        line = next(l for l in lines if l.startswith(f"[{src}] "))
        pairs = [p.split("=", 1) for p in line.split("] ", 1)[1].split(", ")]
        assert [k for k, _ in pairs] == mine[bid], (bid, src)
        out[bid] = dict(pairs)
    return out


# Per-segment readings (the Vietnamese of THAT segment words the keyword differently).
OVERRIDES = {
    # «mười một loại quả của nghiệp thiện …»: the only cittuppādā of the segment has no «tâm»
    "1-1399": {"citta": NDE, "cittuppādā": "loại"},
    "1-1589": {"citta": NDE, "cittuppādā": "loại"},
    "1-1591": {"citta": NDE, "cittuppādā": "loại"},
    "1-1412": {"caya": NDE},                             # fragment of apacaya «sự giảm trừ» (as 2-03, 4-01)
    # maggārammaṇā / maggahetukā «lấy con đường làm đối tượng / gốc rễ» (as 4-01 ^1-1038 / ^1-1039)
    "1-1429": {"ārammaṇā": "lấy" + GAP + "làm đối tượng", "hetukā": "lấy" + GAP + "làm gốc rễ"},
    # fetter / hindrance stems without «sự» (4-01 ^1-1118, 4-02 ^1-1158)
    "1-1477": {"paṭigha": "ác cảm", "māna": "kiêu mạn", "vicikicchā": "hoài nghi", "issā": "ganh tị",
               "rāga": "tham đắm", "kāmarāga": "tham đắm dục lạc", "parāmāsa": "hiểu sai lệch"},
    "1-1503": {"vicikicchā": "hoài nghi", "uddhacca": "xao động"},
    # closing line «Bộ sách “Liệt kê các hiện tượng” đã hoàn tất.» (the title: CORE)
    "1-1616": {"Dhammasaṅgaṇī": CORE["dhammasaṅgaṇī"], "saṅgaṇī": CORE["saṅgaṇī"], "Dhamma": CORE["dhamma"]},
}


def context5(bid, k, s, text):
    """Segment rules of this part (k: lower-cased keyword, s: lower-cased keyword set). None = no rule."""
    if k == "kiriyā":                                    # «tâm chức năng …» beside kiriyābyākataṃ;
        return "chức năng" if "kiriyābyākataṃ" in s else "mang tính chức năng"   # else kiriyāmanodhātu / -hetuka…
    if k == "yañca":                                     # «và loại vật chất …»; «; loại vật chất …» after a «;» list
        return "và loại" if present("và loại", text) else "loại"
    if k == "pahātabbahetukā":                           # «không có gốc rễ cần dứt bỏ …» / «có gốc rễ không cần dứt bỏ …»
        return "có gốc rễ cần dứt bỏ" if present("có gốc rễ cần dứt bỏ", text) else "có gốc rễ" + GAP + "cần dứt bỏ"
    return None


def resolver_for(part):
    vi = read_vietnamese(part)
    same = _load_same()

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        if bid in same:
            return same[bid][kw]
        k = lc(kw)
        s = set(lc(x) for x in kws)
        text = vi.get(bid, "")
        v = context5(bid, k, s, text)
        if v is not None:
            return v
        if k in ADD5:
            return ADD5[k]
        try:
            v = _p402._val(k)
        except KeyError:
            return ch2_value(kw, kws, T05)
        if k.startswith("dhammā ") and v.startswith("hiện tượng ") and not present(v, text):
            v = "hiện tượng" + GAP + v[len("hiện tượng "):]
        return v
    return resolve


def dump(part, only_miss=False):
    res = resolver_for(part)
    vi = read_vietnamese(part)
    c, miss, where = Counter(), Counter(), {}
    for bid, kws in read_keywords(part):
        for kw in kws:
            try:
                v = res(bid, kw, kws)
            except KeyError:
                v = "???"
            c[(kw, v)] += 1
            where.setdefault((kw, v), []).append(bid)
            if v == "???" or not present(v, vi.get(bid, "")):
                miss[(kw, v)] += 1
    for (kw, v), n in sorted(c.items()):
        m = miss.get((kw, v), 0)
        if only_miss and not m:
            continue
        print(f"{kw}={v}  [{n}] {where[(kw, v)][:4]}" + (f"  MISS {m}" if m else ""))


if __name__ == "__main__":
    if sys.argv[1:2] == ["dump"]:
        dump(PART, len(sys.argv) > 2)
    else:
        build_part(PART, resolver_for(PART))
        verify(PART)
