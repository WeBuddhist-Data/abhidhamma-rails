"""Build the Pāli->Vietnamese keyword map for pi-2 part 18-dhammahadayavibhango.

usage: python -I -X utf8 map_18_vi.py                    (writes 18-dhammahadayavibhango.mapped.md and verifies it)
       python -I -X utf8 map_18_vi.py dump PART [miss]   (every distinct keyword=value; writes nothing)
       python -I -X utf8 map_18_vi.py show PART lo hi [all] [pali]   (segments with misses; writes nothing)

Resolution order per keyword: OVERRIDES[bid][kw] -> context18() (segment rules) -> T18 (this script's table)
-> T23 (map_2-3_vi.py) -> the map_17_vi.py resolver (context17 -> T17 -> context16 -> T16 -> context1315 -> T1315
-> T1012 -> T79 -> T45 -> map_common_vi.value(): KH -> the approved pi-1 chain).
Conventions: pi-1 vi-map-conventions.md + notes-map-*.md, vi-map-conventions-pi2.md, notes-map-2-3.md …
notes-map-17.md, notes-map-18.md.
"""
import importlib.util
import pathlib
import sys
from collections import Counter

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from map_common_vi import (GAP, NDE, build_part, lc, pi1_map_values, present,  # noqa: E402
                           read_keywords, read_pali, read_vietnamese, value, verify)


def _imp(name, fn):
    spec = importlib.util.spec_from_file_location(name, HERE / fn)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)          # import only: the earlier scripts build nothing unless run as a script
    return mod


M17 = _imp("map_17_vi", "map_17_vi.py")
M23 = _imp("map_2_3_vi", "map_2-3_vi.py")
T23 = M23.T23

PARTS = ["18-dhammahadayavibhango"]

_KX = "không xác định về mặt đạo đức"
_UPA = "sinh vào lĩnh vực"                      # X-āyatanūpaga «(chư thiên) sinh vào lĩnh vực X»

T18 = {
    # ================================================================ headings
    "hadaya": "cốt lõi",                                             # «Phân tích cốt lõi của các hiện tượng»
    "vāro": "mục", "sabba": "tất cả", "saṅgāhika": "bao gồm",       # «Mục bao gồm tất cả»
    "uppattānuppattivāro": "Mục về những gì sinh khởi và không sinh khởi", "ānuppatti": "không sinh khởi",
    "dassanavāro": "mục trình bày", "dassana": "trình bày",
    "antara": "sự khác biệt",                                        # Bhūmantara- «sự khác biệt giữa các cõi»
    "bhūmantaradassanavāro": "Mục trình bày sự khác biệt giữa các cõi",
    "uppādaka": "tạo ra sự tái sinh", "uppādakakamma": "nghiệp tạo ra sự tái sinh",
    "uppādakakammaṃ": "nghiệp tạo ra sự tái sinh",
    # āyuppamāṇa: the Vietnamese fuses āyu + pamāṇa into «tuổi thọ» (as pi-1 cittassekaggatā / ekaggatā)
    "āyu": "tuổi thọ", "pamāṇa": "tuổi thọ", "pamāṇaṃ": "tuổi thọ",
    "āyuppamāṇa": "tuổi thọ", "āyuppamāṇaṃ": "tuổi thọ",
    "abhiññeyyādivāro": "Mục về những gì cần được hiểu biết trực tiếp và các điều khác",
    "sārammaṇānārammaṇavāro": "Mục về những gì có đối tượng và không có đối tượng", "ārammaṇa": "đối tượng",
    "diṭṭhasutādidassanavāro": "Mục trình bày những gì được thấy được nghe và các điều khác",   # comma dropped
    "tikādidassanavāro": "Mục trình bày các bộ ba và các bộ khác",
    "tikaṃ": "bộ ba", "dukaṃ": "bộ đôi", "vipākattikaṃ": "Bộ ba về quả của nghiệp",
    "upādinna": "do nghiệp tạo ra", "lokiya": "thế gian",               # «Bộ ba về những gì do nghiệp tạo ra»
    # ---- the planes (kāmadhātu here is the plane «cõi dục lạc», unlike ch3's «yếu tố dục lạc»)
    "kāmadhātu": "cõi dục lạc", "kāmadhātuyā": "cõi dục lạc", "arūpadhātu": "cõi không hình sắc",
    "arūpadhātuyā": "cõi không hình sắc", "rūpadhātuyā": "cõi hình sắc", "dhātuyā": "cõi",
    "apariyāpannaṃ": "phần không nằm trong các cõi tồn tại",
    "dhātuyo kāmadhātupariyāpannā": "yếu tố nằm trong cõi dục lạc",
    "dhātuyo pariyāpannā": "yếu tố nằm trong các cõi tồn tại",
    "asañña": "Vô Tưởng", "sattā": "chúng sinh",                    # «Chúng sinh Vô Tưởng»
    # ================================================================ counted units (Sabbasaṅgāhika …)
    "phassā": "loại tiếp xúc", "phasso": "loại tiếp xúc", "samphasso": "sự tiếp xúc",
    "āhāro": "dưỡng chất", "kabaḷīkārāhāro": "thức ăn trong vai trò dưỡng chất",
    "phassāhāro": "sự tiếp xúc trong vai trò dưỡng chất",
    "manosañcetanāhāro": "chủ ý của ý trong vai trò dưỡng chất", "viññāṇāhāro": "thức trong vai trò dưỡng chất",
    "āyatanāni": "lĩnh vực nhận biết", "āyatanānaṃ": "lĩnh vực nhận biết",
    "ekādasāyatanāni": "mười một lĩnh vực nhận biết", "dasāyatanāni": "mười lĩnh vực nhận biết",
    "cuddasindriyāni": "mười bốn năng lực", "terasindriyāni": "mười ba năng lực",
    "dvādasindriyāni": "mười hai năng lực", "ekādasindriyāni": "mười một năng lực",
    "dasindriyāni": "mười năng lực", "bāvīsatindriyā": "hai mươi hai năng lực", "terasa": "mười ba",
    "cakkhu": "mắt", "dukkha": "khổ đau",                             # Dukkhasaccaṃ «sự thật về khổ đau»
    "akusalahetu": "gốc rễ bất thiện", "vipākato": "quả",             # pi-1 ^1-1068
    "kiriyābyākatesu": _KX + " mang tính chức năng",
    "manodhātusamphasso": "sự tiếp xúc của yếu tố ý", "manodhātusamphassa": "sự tiếp xúc của yếu tố ý",
    "manodhātusamphassajā": "sinh từ sự tiếp xúc của yếu tố ý",
    "manoviññāṇadhātusamphassajā": "sinh từ sự tiếp xúc của yếu tố ý thức",
    "dhātūnaṃ": "yếu tố", "khandha": "khối",
    # ================================================================ Dhammadassanavāra (rebirth moment)
    "upapattikkhaṇe": "vào khoảnh khắc tái sinh", "upapatti": "tái sinh", "khaṇe": "khoảnh khắc",
    "pātubhavanti": "xuất hiện", "pātubhavati": "xuất hiện",
    "tiracchānagatānaṃ": "loài súc sinh", "sattānaṃ": "chúng sinh", "jaccandhānaṃ": "mù bẩm sinh",
    "badhirānaṃ": "điếc",                               # of jaccabadhirānaṃ / jaccandhabadhirānaṃ
    "asurānaṃ": "a-tu-la", "paripuṇṇāyatanānaṃ": "có đầy đủ các lĩnh vực nhận biết",
    "kappikānaṃ": "kiếp",                               # of paṭhamakappikānaṃ «ở thời kỳ đầu của kiếp»
    "petānaṃ": "ngạ quỷ", "devānaṃ": "chư thiên", "nerayikānaṃ": "chúng sinh địa ngục",
    "manussānaṃ": "loài người", "opapātikānaṃ": "hóa sinh",
    "opapātikānaṃ tiracchānagatānaṃ": "loài súc sinh hóa sinh", "opapātikānaṃ asurānaṃ": "a-tu-la hóa sinh",
    "opapātikānaṃ petānaṃ": "ngạ quỷ hóa sinh", "kāmāvacarānaṃ": "thuộc cõi dục lạc", "āvacarānaṃ": "thuộc cõi",
    "gabbhaseyyakānaṃ": "sinh ra từ bào thai",
    "sampayuttānaṃ": "gắn liền", "vippayuttānaṃ": "không gắn liền", "ñāṇa": "hiểu biết",
    "ñāṇavippayuttānaṃ": "không gắn liền với hiểu biết", "sahetukānaṃ": "có gốc rễ",
    "napuṃsakānaṃ": "không có giới tính", "avasesānaṃ": "còn lại",
    "asaññasattānaṃ": "Vô Tưởng", "asaññasattānaṃ devānaṃ": "chư thiên Vô Tưởng",
    "aphassakā": "không có sự tiếp xúc", "avedanakā": "không có cảm giác", "acetanakā": "không có chủ ý",
    "acittakā": "không có tâm", "anāhārā": "không có dưỡng chất", "asaññakā": "không có tri giác",
    # ================================================================ Bhūmantaradassanavāra (2-1020)
    "akaniṭṭhe deve": "chư thiên Sắc Cứu Cánh", "paranimmitavasavattī": "Tha Hóa Tự Tại",
    "paranimmitavasavattī deve": "chư thiên Tha Hóa Tự Tại", "āyatanūpage": _UPA,
    "ākāsānañcāyatanūpage": _UPA + " không gian vô tận",
    "nevasaññānāsaññāyatanūpage": _UPA + " không phải tri giác cũng không phải không tri giác",
    "antare": "khoảng giữa", "pariyantaṃ": "giới hạn", "deve antokaritvā": "bao gồm cả chư thiên",
    "kusalākusalabyākatā": "thiện bất thiện và " + _KX,              # comma dropped
    "kāmāvacarā dhammā": "hiện tượng thuộc cõi dục lạc", "maggā": "con đường", "phalāni": "thành quả",
    "sāsavā": "đối tượng của ô nhiễm",
    # ================================================================ Uppādakakamma (2-1021)
    "devā": "chư thiên", "deviyo": "hoàng hậu", "kumārā": "hoàng tử", "rājāno": "vua", "sammuti": "quy ước",
    "visuddhi": "sự trong sạch", "mahārājike": "Đại Thiên Vương", "mahārājikānaṃ": "Đại Thiên Vương",
    "tadupari": "trở lên", "arahanto": "vị A-la-hán", "dānaṃ": "bố thí", "sīlaṃ": "giới hạnh",
    "samādiyitvā": "thọ trì", "uposatha": "ngày trai giới", "katvā": "thực hiện", "upapajjanti": "tái sinh",
    "khattiya": "người quý tộc", "brāhmaṇa": "bà-la-môn", "gahapati": "gia chủ", "mahāsālānaṃ": "giàu có",
    # god names: Sino-Vietnamese, members = their syllables (as ch3 nimmita = Hóa, vasavattī = Tự Tại)
    "tāvatiṃsānaṃ": "Ba Mươi Ba", "yāmānaṃ devānaṃ": "chư thiên Dạ Ma", "tusitānaṃ": "Đâu Suất",
    "tusitānaṃ devānaṃ": "chư thiên Đâu Suất", "nimmāna": "Hóa", "ratīnaṃ": "Lạc",
    "nimmānaratīnaṃ devānaṃ": "chư thiên Hóa Lạc", "paranimmitavasavattīnaṃ": "Tha Hóa Tự Tại",
    "paranimmitavasavattīnaṃ devānaṃ": "chư thiên Tha Hóa Tự Tại", "vasavattīnaṃ": "Tự Tại",
    "brahmānaṃ devānaṃ": "chư thiên" + GAP + "Phạm",                 # of mahābrahmānaṃ devānaṃ
    "mahābrahmānaṃ": "Đại Phạm", "mahābrahmānaṃ devānaṃ": "chư thiên Đại Phạm",
    "pārisajjānaṃ": "Chúng", "purohitānaṃ": "Phụ",                   # brahmapārisajja / -purohita
    "appamāṇābhānaṃ": "Vô Lượng Quang", "ābhānaṃ": "Quang", "ābhassarānaṃ": "Quang Âm",
    "subhānaṃ": "Tịnh", "kiṇhānaṃ": "Biến", "appamāṇa": "Vô Lượng",   # parittasubha / appamāṇasubha / subhakiṇha
    "vehapphalānaṃ": "Quảng Quả", "vehapphalānaṃ devānaṃ": "chư thiên Quảng Quả",
    "avihānaṃ": "Vô Phiền", "avihānaṃ devānaṃ": "chư thiên Vô Phiền",
    "atappānaṃ": "Vô Nhiệt", "atappānaṃ devānaṃ": "chư thiên Vô Nhiệt",
    "sudassānaṃ": "Thiện Hiện", "sudassānaṃ devānaṃ": "chư thiên Thiện Hiện",
    "sudassīnaṃ devānaṃ": "chư thiên Thiện Kiến", "akaniṭṭhānaṃ devānaṃ": "chư thiên Sắc Cứu Cánh",
    "āyatanūpagānaṃ": _UPA, "ākāsānañcāyatanūpagānaṃ": _UPA + " không gian vô tận",
    "viññāṇañcāyatanūpagānaṃ": _UPA + " thức vô tận", "ākiñcaññāyatanūpagānaṃ": _UPA + " không có gì cả",
    "nevasaññānāsaññāyatanūpagānaṃ": _UPA + " không phải tri giác cũng không phải không tri giác",
    # ================================================================ Āyuppamāṇa (2-1022 … 2-1028)
    "sataṃ": "một trăm", "mānusakāni": "của loài người", "mānusakaṃ vassasataṃ": "một trăm năm của loài người",
    "paññāsa": "năm mươi", "vassāni": "năm", "vassasatāni": "trăm năm", "satāni": "trăm",
    "rattindivo": "một ngày một đêm", "rattiyo": "đêm", "rattiyo māso": "đêm" + GAP + "một tháng",
    "tiṃsa": "ba mươi", "māso": "một tháng", "saṃvaccharo": "một năm",
    "dvādasamāsiyo saṃvaccharo": "mười hai tháng" + GAP + "một năm", "dibbāni": "cõi trời",
    "sahassaṃ": "một nghìn", "sahassāni": "nghìn",
    "manussānaṃ gaṇanāya": "theo cách tính của loài người", "gaṇanāya": "theo cách tính",
    "samiddhino": "có đầy đủ", "saṅkhāto": "tính gộp làm một", "pakāsitāti": "đã được công bố",
    # verse totals computed into Vietnamese numerals (as the Russian map: koṭiyo = millions, aṭṭhavīsa = 280)
    "koṭiyo": "triệu", "aṭṭhavīsañca": "hai trăm tám mươi",
    "jhānaṃ": "tầng thiền", "bhāvetvā": "sau khi tu tập", "kappassa": "kiếp", "kappā": "kiếp",
    "parittaṃ": "ở mức hạn hẹp", "majjhimaṃ": "ở mức trung bình", "paṇītaṃ": "ở mức ưu việt",
    "catusaṭṭhi": "sáu mươi bốn", "bāttiṃsa": "ba mươi hai", "nānattatā": "sự khác biệt",
    "abhinīhāra": "sự định hướng", "kappasahassāni": "nghìn kiếp", "kappasahassaṃ": "một nghìn kiếp",
    "caturāsīti": "tám mươi bốn", "cattārīsa": "bốn mươi", "saṭṭhi": "sáu mươi", "vīsati": "hai mươi",
    # ---- the verses (2-1029)
    "punāgacchanti": "trở lại", "parinibbanti": "nhập Niết-bàn trọn vẹn", "cavanti": "chết đi",
    "nipakā": "khôn ngoan", "gatiṃ": "cõi tái sinh", "bhāventi": "tu tập", "bhāvayitvā": "sau khi tu tập",
    "saṅkhayā": "cạn kiệt", "pariññāya": "sau khi hiểu biết trọn vẹn", "gatā": "đi đến", "uttamaṃ": "tối thượng",
    "dīghāyukā": "sống lâu", "ukkhittā": "được" + GAP + "nâng lên", "āsave": "ô nhiễm", "puñña": "phước",
    "bhavaggatampi": "đỉnh cao của sự hiện hữu", "nibbānogadhagāminaṃ": "dẫn sâu vào Niết-bàn",
    "tejena": "uy lực", "suciṃ": "trong sạch", "mokkhāya": "để giải thoát khỏi", "mahesinā": "bậc Đại Hiền",
    "āyusaṅkhayā": "khi tuổi thọ cạn kiệt", "nipuṇā": "tinh tế", "anāsavāti": "không còn ô nhiễm",
    "tasmā": "vì thế", "cintakā": "biết suy xét", "koci": "nào", "dhīrā": "người trí",
    "jarā": "sự lão hóa", "maraṇa": "sự chết",
    # ================================================================ Abhiññeyyādi / Sārammaṇa / Diṭṭhasutādi
    "abhiññeyyā": "cần được hiểu biết trực tiếp", "abhiññeyyo": "cần được hiểu biết trực tiếp",
    "pariññeyyā": "cần được hiểu biết trọn vẹn", "pariññeyyo": "cần được hiểu biết trọn vẹn",
    "pahātabbā": "cần được dứt bỏ", "pahātabbo": "cần được dứt bỏ",
    "bhāvetabbā": "cần được tu tập", "bhāvetabbo": "cần được tu tập",
    "sacchikātabbā": "cần được tự mình chứng nghiệm", "sacchikātabbo": "cần được tự mình chứng nghiệm",
    "sārammaṇā": "có đối tượng", "rūpā": "thuộc vật chất",          # «bao nhiêu khối thuộc vật chất» (ch5 ^2-224)
    "sārammaṇārammaṇā": "lấy những gì có đối tượng làm đối tượng",
    "anārammaṇārammaṇā": "lấy những gì không có đối tượng làm đối tượng",
    "sutā": "được nghe", "suto": "được nghe", "mutā": "được cảm nhận", "muto": "được cảm nhận",
    "viññātā": "được nhận biết", "viññāto": "được nhận biết",
    "nevavipākanavipākadhammadhammo": "không phải là quả của nghiệp cũng không có khả năng sinh ra quả",
    # ================================================================ uddāna and colophons (2-1044)
    "abhiññā": "cần được hiểu biết trực tiếp", "aṭṭhārasannaṃ": "mười tám",
    "aṭṭhārasannaṃ dhātūnaṃ": "mười tám yếu tố",
    "vibhaṅgapakaraṇaṃ": "Bộ Phân tích các hiện tượng", "pakaraṇaṃ": "Bộ",   # «Bộ “Phân tích các hiện tượng”»
}
for _n, _nv in (("vedanā", "cảm giác"), ("saññā", "tri giác"), ("cetanā", "chủ ý")):
    T18[f"manoviññāṇadhātusamphassajā {_n}"] = f"{_nv} sinh từ sự tiếp xúc của yếu tố ý thức"

# per-segment choices (read from the segments)
OVERRIDES = {
    "2-1023": {"sabba": "mọi"},                                  # sabbakāmasamiddhino «có đầy đủ mọi dục lạc»
    "2-1034": {"ārammaṇā": "lấy" + GAP + "làm đối tượng"},       # outer member of sārammaṇārammaṇā
    "2-1035": {"ārammaṇā": "lấy" + GAP + "làm đối tượng"},
    "2-1044": {"sārammaṇā": "mục về đối tượng"},                 # uddāna «hai mục về đối tượng»
    "2-1017": {"rūpa": "vật chất"},                              # rūpakkhandho / rūpajīvitindriyaṃ (also rūpāyatana)
    "2-18-10-0": {"ādi": "bộ khác"},                             # «các bộ ba và các bộ khác»
}
_RUPA_PLANE = {"2-18-2-2-0", "2-18-3-2-0", "2-18-4-2-0", "2-993", "2-1015"}   # capital Rūpa of Rūpadhātu(yā)
_AYATANA_COUNTED = {"2-993", "2-1020"}                           # āyatanā = «lĩnh vực nhận biết» there


def context18(bid, kw, k, s, text, kws):
    """Segment rules (k: lower-cased keyword, s: lower-cased keyword set). None = no rule."""
    if k == "rūpa":
        if kw[0].isupper():                       # sentence-initial: Rūpakkhandho / Rūpadhātuyā
            return "hình sắc" if bid in _RUPA_PLANE else "vật chất"
        return "hình sắc"                         # rūpāyatana / rūpadhātu / kāmarūpagati
    if k == "rūpadhātu":                          # the element «yếu tố hình sắc» / the plane «cõi hình sắc»
        return "yếu tố hình sắc" if present("yếu tố hình sắc", text) else "cõi hình sắc"
    if k == "dhātu":                              # element «yếu tố»; only the plane in the segment: «cõi»
        return "yếu tố" if present("yếu tố", text) else "cõi"
    if k in ("vedanā", "saññā", "cetanā"):        # counted «loại cảm giác / tri giác / chủ ý»
        base = {"vedanā": "cảm giác", "saññā": "tri giác", "cetanā": "chủ ý"}[k]
        return "loại " + base if present("loại " + base, text) else base
    if k in ("cittāni", "cittā", "cittaṃ", "cittānaṃ"):
        return "loại tâm" if present("loại tâm", text) else "tâm"
    if k == "viññāṇadhātu":                       # as map_2-3_vi.py
        return "yếu tố thức" if present("yếu tố thức", text) else "yếu tố" + GAP + "thức"
    if k == "āyatanā":
        return "lĩnh vực nhận biết" if bid in _AYATANA_COUNTED else "lĩnh vực"
    if k == "ādi":
        return "điều khác"                        # «… và các điều khác»
    if k.startswith("upapattikkhaṇe ") and k not in T18:
        rest = kw.split(" ", 1)[1]
        return "vào khoảnh khắc tái sinh " + _base_value(rest, kws, text)
    return None


def _base_value(kw, kws, text):
    k = lc(kw)
    if k in T18:
        return T18[k]
    if k in T23:
        return T23[k]
    return value(kw, kws, {**M17.T45, **M17.T79, **M17.T1012, **M17.T1315, **M17.T16, **M17.T17}, text)


def resolver_for(part):
    vi = read_vietnamese(part)
    base = M17.resolver_for(part)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        k = lc(kw)
        s = set(lc(x) for x in kws)
        text = vi.get(bid, "")
        v = context18(bid, kw, k, s, text, kws)
        if v is not None:
            return v
        if k in T18:
            return T18[k]
        if k in T23:
            return T23[k]
        return base(bid, kw, kws)
    return resolve


_PRIOR = {}


def prior(kw):
    """Counter of the values the earlier pi-2 mapped files give `kw` (exact keyword)."""
    if not _PRIOR:
        for f in sorted(HERE.glob("*.mapped.md")):
            if f.name.startswith("18-"):
                continue
            for line in f.read_text(encoding="utf-8").splitlines():
                if "] " not in line:
                    continue
                for pair in line.split("] ", 1)[1].split(", "):
                    if "=" in pair:
                        a, b = pair.split("=", 1)
                        _PRIOR.setdefault(a, Counter())[b] += 1
    return _PRIOR.get(kw, Counter())


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
            if v == "???" or (v != NDE and not present(v, vi.get(bid, ""))):
                miss[(kw, v)] += 1
    for (kw, v), n in sorted(c.items()):
        m = miss.get((kw, v), 0)
        if only_miss and not m:
            continue
        pr = [x for x, _ in prior(kw).most_common(3) if x != v]
        print(f"{kw}={v}  [{n}] {where[(kw, v)][:4]}" + (f"  prior:{pr}" if pr else "")
              + (f"  MISS {m}" if m else ""))
    print("distinct", len(c), "miss-pairs", len(miss), "miss-total", sum(miss.values()))


def show(part, lo=0, hi=10 ** 6, all_kw=False, pali=False):
    res = resolver_for(part)
    vi = read_vietnamese(part)
    pi = read_pali(part) if pali else {}
    for i, (bid, kws) in enumerate(read_keywords(part)):
        if not lo <= i < hi:
            continue
        text = vi.get(bid, "")
        out, nm = [], 0
        for kw in kws:
            try:
                v = res(bid, kw, kws)
            except KeyError:
                v = "???"
            m = v == "???" or (v != NDE and not present(v, text))
            nm += m
            if m or all_kw:
                out.append(("!!" if m else "") + f"{kw}={v}")
        if nm or all_kw:
            if pali:
                print(f"-- PI {pi.get(bid, '')}")
            print(f"== {i} [{bid}]")
            print("   " + " | ".join(out))


if __name__ == "__main__":
    if sys.argv[1:2] == ["show"]:
        show(sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), "all" in sys.argv[5:], "pali" in sys.argv[5:])
    elif sys.argv[1:2] == ["dump"]:
        dump(sys.argv[2], sys.argv[3:4] == ["miss"])
    else:
        for p in PARTS:
            build_part(p, resolver_for(p))
            verify(p)
