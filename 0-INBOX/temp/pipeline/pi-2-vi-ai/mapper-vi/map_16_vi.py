"""Build the Pāli->Vietnamese keyword map for pi-2 part 16-nanavibhango.

usage: python -I -X utf8 map_16_vi.py                    (writes 16-nanavibhango.mapped.md and verifies it)
       python -I -X utf8 map_16_vi.py dump PART [miss]   (every distinct keyword=value with count and first
                                                         segments; with «miss» only presence misses; writes nothing)

Resolution order per keyword: OVERRIDES[bid][kw] -> context() (segment rules, incl. the «X paññā» rule)
-> T16 (this script's table) -> T1315 (map_13-15_vi.py) -> T1012 -> T79 -> T45 -> map_common_vi.value(): KH
(pi-2 table) -> the approved pi-1 chain; context() falls back to map_13-15_vi.context() (and through it
map_10-12_vi.context()).
Conventions: pi-1 vi-map-conventions.md + notes-map-*.md, vi-map-conventions-pi2.md, notes-map-2-3.md …
notes-map-13-15.md, notes-map-16.md.
"""
import importlib.util
import pathlib
import re
import sys
from collections import Counter

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from map_common_vi import (GAP, NDE, build_part, lc, pi1_map_values, present,  # noqa: E402
                           read_keywords, read_vietnamese, value, verify)


def _imp(name, fn):
    spec = importlib.util.spec_from_file_location(name, HERE / fn)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)          # import only: the earlier scripts build nothing unless run as a script
    return mod


M1315 = _imp("map_1315_vi", "map_13-15_vi.py")
T45, T79, T1012, T1315, context1315 = M1315.T45, M1315.T79, M1315.T1012, M1315.T1315, M1315.context

PARTS = ["16-nanavibhango"]

_KX = "không xác định về mặt đạo đức"
_NV = "chỗ dựa của sự hiểu biết"
_TT = "trí tuệ"
_KN = "sự hiểu biết"
_NUM = {"ekaka": "một", "duka": "đôi", "tika": "ba", "catukka": "bốn", "pañcaka": "năm", "chakka": "sáu",
        "sattaka": "bảy", "aṭṭhaka": "tám", "navaka": "chín", "dasaka": "mười"}
_NUMG = {"ekaka": "một", "duka": "hai", "tika": "ba", "catukka": "bốn", "pañcaka": "năm", "chakka": "sáu",
         "sattaka": "bảy", "aṭṭhaka": "tám", "navaka": "chín", "dasaka": "mười"}
# locatives «trong …» (build_16_vi LOCN / AV)
LOCN = {"kusalābyākate": "tâm thiện và " + _KX, "kusale": "tâm thiện", "vipāke": "quả của nghiệp",
        "kiriyābyākate": "tâm mang tính chức năng " + _KX}

T16 = {
    # ================================================================ headings and frames
    "ñāṇa": "sự hiểu biết", "ñāṇaṃ": _KN, "ñāṇesu": _KN, "ñāṇavatthu": _NV, "vatthu": "chỗ dựa",
    "vatthūni": "chỗ dựa", "mātikā": "ma trận", "niddeso": "giải thích", "vibhaṅgo": "phân tích",
    "chakkamātikā": "ma trận bộ sáu", "dasakamātikā": "ma trận bộ mười", "niṭṭhito": "đã hoàn tất",
    "paññā": _TT, "sattasattati": "bảy mươi bảy", "dasa": "mười", "dasa kilesavatthūni": "mười chỗ dựa của phiền não",
    "kilesavatthūni": "chỗ dựa của phiền não", "kilesa": "phiền não", "tattha": "ở đây",
    # ================================================================ 2-751 / 2-761 … 2-766 (onefold)
    "viññāṇā": "loại thức", "kappeti": "thực hiện", "uppajjanti": "sinh khởi", "uppanna": "đã sinh khởi",
    "uppannārammaṇā": "có đối tượng đã sinh khởi", "samāpajjati": "chứng nhập", "cavati": "chết",
    "amanasikārā": "không có sự chú tâm", "asamannāhārā": "không có sự lưu ý",
    "manasikāro": "sự chú tâm", "samannāhāro": "sự lưu ý", "ābhogo": "sự chú hướng", "āvaṭṭanā": "sự hướng đến",
    "anābhogā": "không có sự chú hướng", "kāyakammaṃ": "nghiệp bằng thân", "vacīkammaṃ": "nghiệp bằng lời nói",
    "paṭivijānāti": "nhận biết rõ", "nānā": "khác nhau", "supinaṃ": "nằm mơ", "supati": "ngủ",
    "paṭibujjhati": "thức dậy", "vuṭṭhāti": "xuất khỏi", "aññatra": "ngoại trừ", "paccanubhonti": "trải nghiệm",
    "paccanubhoti": "trải nghiệm", "gocara": "phạm vi hoạt động", "gocaravisayaṃ": "phạm vi hoạt động",
    "gocaravisayaṃ paccanubhontī": "trải nghiệm phạm vi hoạt động",
    "abhinipāta": "sự va chạm", "āpāta": "sự hiện ra", "samanantarā": "liền sau",
    "ajjhattika": "thuộc phần bên trong", "ajjhattikā": "thuộc phần bên trong", "bāhirā": "thuộc phần bên ngoài",
    "ajjhattikavatthukā": "có chỗ dựa thuộc phần bên trong", "vatthukā": "có chỗ dựa",
    "bāhirārammaṇā": "có đối tượng thuộc phần bên ngoài", "purejātārammaṇā": "có đối tượng đã sinh ra trước",
    "asambhinna": "chưa tan rã", "asambhinnasmiṃ": "chưa tan rã", "uppannasmiṃ": "đã sinh khởi",
    "ārammaṇe": "đối tượng", "aññaṃ": "khác", "vibhāvanā": "làm sáng tỏ", "yāthāvaka": "đúng như thật",
    "vibhāvanā paññā": "trí tuệ làm sáng tỏ", "iriyāpathaṃ": "tư thế", "abbokiṇṇā": "liền mạch",
    "apubbaṃ": "không trước", "acarimaṃ": "không sau", "paṭṭhapeti": "khởi lập", "dhammaṃ": "hiện tượng",
    "kusalākusalaṃ": "thiện hay bất thiện", "kusalākusalaṃ dhammaṃ": "hiện tượng thiện hay bất thiện",
    "ākusalaṃ": "bất thiện", "acetasikā": "không phải là yếu tố đồng hành với tâm",
    "āsekkhā": "thuộc về người đã hoàn tất tu học", "āsekkha": "thuộc về người đã hoàn tất tu học",
    "sekkha": "thuộc về người còn đang tu học", "sekkhā": "thuộc về người còn đang tu học",
    "asekkhā": "thuộc về người đã hoàn tất tu học",
    "manasikarontassa": "người đang chú tâm", "samannāharantassa": "người đang lưu ý", "khaṇe": "khoảnh khắc",
    "ekakkhaṇe": "cùng một khoảnh khắc", "paṭipāṭiyā": "theo thứ tự lần lượt",
    "kāyaviññāṇassa uppannasamanantarā": "ngay liền sau khi thức qua thân sinh khởi",
    "cakkhuviññāṇassa uppannasamanantarā": "ngay liền sau khi thức qua mắt sinh khởi",
    "kāyaviññāṇaṃ na uppajjati": "thức qua thân không sinh khởi",
    "cakkhuviññāṇaṃ na uppajjati": "thức qua mắt không sinh khởi",
    "kāyaviññāṇaṃ na paccanubhoti": "thức qua thân không trải nghiệm",
    "cakkhuviññāṇaṃ na paccanubhoti": "thức qua mắt không trải nghiệm",
    "kāyaviññāṇassa gocaravisayaṃ": "phạm vi hoạt động của thức qua thân",
    "cakkhuviññāṇassa gocaravisayaṃ": "phạm vi hoạt động của thức qua mắt",
    "kāyaviññāṇassa": "thức qua thân", "cakkhuviññāṇassa": "thức qua mắt", "sotaviññāṇassa": "thức qua tai",
    "ghānaviññāṇassa": "thức qua mũi", "jivhāviññāṇassa": "thức qua lưỡi",
    "mano": "ý", "manodhātuyā": "yếu tố ý", "dhātuyā": "yếu tố", "gamanaṃ": "đi", "nisajjaṃ": "ngồi",
    "seyyaṃ": "nằm", "ekakaṃ": "phân loại theo nhóm một", "dukaṃ": "phân loại theo nhóm hai",
    "tikaṃ": "phân loại theo nhóm ba", "catukkaṃ": "phân loại theo nhóm bốn", "pañcakaṃ": "phân loại theo nhóm năm",
    "chakkaṃ": "phân loại theo nhóm sáu", "sattakaṃ": "phân loại theo nhóm bảy", "aṭṭhakaṃ": "phân loại theo nhóm tám",
    "navakaṃ": "phân loại theo nhóm chín", "dasakaṃ": "phân loại theo nhóm mười",
    "manoviññāṇa": "ý thức", "jarā": "sự lão hóa",
    # ================================================================ matrix predicates (bare; «là» frame dropped)
    "sāsavā": "đối tượng của ô nhiễm", "anāsavā": "không phải là đối tượng của ô nhiễm",
    "pahātabbā": "cần dứt bỏ", "upādāniyā": "đối tượng của sự bám víu", "saṃyojaniyā": "đối tượng của xiềng xích",
    "ganthaniyā": "đối tượng của nút thắt", "oghaniyā": "đối tượng của dòng lũ", "yoganiyā": "đối tượng của ách",
    "nīvaraṇiyā": "đối tượng của chướng ngại", "saṃkilesikā": "đối tượng của phiền não",
    "parāmaṭṭhā": "bị sự hiểu sai lệch nắm giữ", "sahagatā": "đi kèm", "pītisahagatā": "có sự hân hoan đi kèm",
    "sukhasahagatā": "có hạnh phúc đi kèm", "upekkhāsahagatā": "có sự bình thản đi kèm", "ācaya": "sự tích lũy",
    "āpacaya": "sự giảm trừ", "apacaya": "sự giảm trừ", "hetukā": "có gốc rễ", "hetū": "gốc rễ",
    "saṅkhatā": "do điều kiện tạo thành", "vippayuttā": "không gắn liền", "sampayuttā": "gắn liền",
    "vicārā": "sự duy trì tâm", "vitakkā": "sự hướng tâm", "vitakka": "sự hướng tâm", "vicāra": "sự duy trì tâm",
    "rūpāvacarā": "thuộc cõi hình sắc", "arūpāvacarā": "thuộc cõi không hình sắc",
    "kāmāvacarā": "thuộc cõi dục lạc", "āvacarā": "thuộc cõi", "parittā": "hạn hẹp", "mahaggatā": "rộng lớn",
    "appamāṇā": "không thể đo lường", "bhāvanāya": "sự tu tập", "dassanena": "sự thấy chân lý",
    "mattā": "chỉ có", "abyākatā": _KX, "ārammaṇā": "có đối tượng", "apariyāpannā": "không nằm trong các cõi tồn tại",
    "asaṃkiliṭṭha": "không bị phiền não làm vẩn đục", "aniyatā": "không cố định", "niyatā": "cố định",
    "lokiyā": "thuộc thế gian", "uttarā": "vượt", "na": "không", "upādāna": "sự bám víu", "parāmāsa": "sự hiểu sai lệch",
    "āsava": "ô nhiễm", "upādānavippayuttā": "không gắn liền với sự bám víu",
    "parāmāsavippayuttā": "không gắn liền với sự hiểu sai lệch", "upekkhā": "sự bình thản", "pīti": "sự hân hoan",
    "sukha": "hạnh phúc", "viññeyyā": "có thể nhận biết", "kenaci": "một loại thức nào đó",
    "niyyānikā": "dẫn đến giải thoát", "sauttarā": "còn có điều cao hơn", "anuttarā": "không có điều gì cao hơn",
    "attha": "lợi ích", "jāpikā": "tạo ra", "jāpita": "đã được tạo ra", "uppādinī": "sẽ sinh khởi",
    "uppannā": "đã sinh khởi", "anuppannā": "chưa sinh khởi", "ādhipatinī": "lấy … làm yếu tố chủ đạo",
    "ācayagāminī": "dẫn đến sự tích lũy", "apacayagāminī": "dẫn đến sự giảm trừ", "magga": "con đường",
    "vipākadhammadhammā": "có khả năng sinh ra quả", "dhammā": NDE,       # fragment of -vipākadhammadhammā
    "mahaggatārammaṇā": "có đối tượng rộng lớn", "parittārammaṇā": "có đối tượng hạn hẹp",
    "appamāṇārammaṇā": "có đối tượng không thể đo lường", "atītārammaṇā": "có đối tượng thuộc quá khứ",
    "anāgatārammaṇā": "có đối tượng thuộc tương lai", "paccuppannārammaṇā": "có đối tượng thuộc hiện tại",
    "ajjhattā": "ở nơi bản thân", "bahiddhā": "ở bên ngoài bản thân",
    "ajjhattabahiddhā": "ở nơi bản thân và ở bên ngoài bản thân", "ajjhattārammaṇā": "có đối tượng ở nơi bản thân",
    "bahiddhārammaṇā": "có đối tượng ở bên ngoài bản thân",
    # ================================================================ 2-753 / 2-768 … 2-771 (threefold)
    "dāna": "sự bố thí", "dānaṃ": "sự bố thí", "suta": "sự lắng nghe", "cintā": "sự suy tư", "bhāvanā": "sự tu tập",
    "sīla": "giới hạnh", "sīlaṃ": "giới hạnh", "sīle": "giới hạnh", "citte": "tâm",
    "adhipaññāya": "trí tuệ cao thượng", "upāya": "phương cách", "kosallaṃ": "sự khéo léo",
    "ādhigaccha": "nhờ",                                                        # dānādhigaccha «nhờ sự bố thí» (as written)
    "yoga": "sự khéo léo", "vihitesu": "được tạo dựng", "ṭṭhānesu": "lĩnh vực", "vijjā": "học thuật",
    "āyatanesu": "ngành", "sippāyatanesu": "ngành thủ công", "kammassakataṃ": "nghiệp là tài sản của chính mình",
    "saccānulomikaṃ": "thuận theo sự thật", "anulomikaṃ": "thuận theo", "ānulomikaṃ": "thuận theo",
    "anulomikā": "thuận theo", "khantiṃ": "sự chấp nhận", "khanti": "sự chấp nhận", "diṭṭhiṃ": "quan điểm",
    "ruciṃ": "sự ưa thích", "ruci": "sự ưa thích", "mudiṃ": "sự tán thành", "pekkhaṃ": "sự xem xét",
    "pekkhā": "sự xem xét", "nijjhāna": "suy ngẫm", "dhamma": "hiện tượng", "sutvā": "nghe",
    "paṭilabhati": "đạt được", "evarūpiṃ": "thuộc loại như vậy", "yaṃ": "mà", "anicca": "vô thường",
    "rūpaṃ": "vật chất", "vedanā": "cảm giác", "saññā": "tri giác", "saṅkhārā": "sự tạo tác", "viññāṇaṃ": "thức",
    "samāpannassa": "người đã chứng nhập", "samāpannassa paññā": "trí tuệ của người đã chứng nhập",
    "pātimokkha": "bộ giới luật căn bản", "saṃvaraṃ": "sự thu thúc", "saṃvarantassa": "người đang thu thúc",
    "samāpattiṃ": "sự chứng đạt", "samāpajjantassa": "người đang chứng nhập", "ārūpāvacara": "cõi không hình sắc",
    "rūpāvacarārūpāvacarasamāpattiṃ": "sự chứng đạt thuộc cõi hình sắc và cõi không hình sắc",
    "pahīyanti": "được dứt bỏ", "manasikaroto": "chú tâm", "tatrupāyā": "phương cách cho việc ấy",
    "nirujjhanti": "chấm dứt", "vepullāya": "sự lớn mạnh", "pāripūriyā": "sự hoàn thiện",
    "kusalā": "thiện", "akusalā": "bất thiện", "kusalā dhammā": "hiện tượng thiện", "akusalā dhammā": "hiện tượng bất thiện",
    "kiriyābyākate": LOCN["kiriyābyākate"], "ābyākate": _KX, "kusale": "tâm thiện",
    "kusalābyākate": LOCN["kusalābyākate"], "bhūmīsu": "cõi", "maggesu": "con đường", "phalesu": "thành quả",
    "phale": "thành quả", "arahatta": "A-la-hán", "upariṭṭhimā": "cao nhất",
    "rūpāvacarārūpāvacarakusalābyākate": "tâm thiện và " + _KX + " thuộc cõi hình sắc và cõi không hình sắc",
    "rūpāvacarārūpāvacarakusale": "tâm thiện thuộc cõi hình sắc và cõi không hình sắc",
    "kāmāvacara": "thuộc cõi dục lạc", "āvacara": "thuộc cõi",
    "vitakkavicāra": "sự hướng tâm và sự duy trì tâm",
    "ārabbha": "liên quan đến", "uppajjati": "sinh khởi", "vicayo": "sự tìm hiểu",
    "dhammavicayo": "sự tìm hiểu các hiện tượng", "amoho": "sự không si mê", "sammā": "đúng đắn",
    "pajānanā": "sự hiểu rõ", "diṭṭhi": "quan điểm", "sammādiṭṭhi": "quan điểm đúng đắn",
    "paritte": "hạn hẹp", "mahaggate": "rộng lớn", "appamāṇe": "không thể đo lường", "dhamme": "hiện tượng",
    "ariya": "cao quý", "maggaṃ": "con đường", "adhipatiṃ": "yếu tố chủ đạo", "vattabbā": "nên nói",
    "ajjhatte": "ở nơi bản thân", "ajjhatte dhamme": "hiện tượng ở nơi bản thân", "ajjhatta": "ở nơi bản thân",
    "bahiddhādhamme": "hiện tượng ở bên ngoài bản thân",
    # ================================================================ fourfold (2-754, 2-793 … 2-803)
    "ācayāya": "dẫn đến sự tích lũy", "apacayāya": "dẫn đến sự giảm trừ", "nibbidāya": "dẫn đến sự nhàm chán",
    "paṭivedhāya": "dẫn đến sự thấu triệt", "paññā ācayāya": "trí tuệ dẫn đến sự tích lũy",
    "paññā apacayāya": "trí tuệ dẫn đến sự giảm trừ", "paññā nibbidāya": "trí tuệ dẫn đến sự nhàm chán",
    "jarāmaraṇe": "sự lão hóa và sự chết", "jarāmaraṇe ñāṇaṃ": "sự hiểu biết về sự lão hóa và sự chết",
    "paṭisambhidā": "loại hiểu biết thông suốt", "jātiyā": "sự sinh", "nibbedha": "xuyên thấu", "nirodhe": "sự chấm dứt",
    "jarāmaraṇanirodhe": "sự chấm dứt sự lão hóa và sự chết", "saṅkhāranirodhe": "sự chấm dứt các sự tạo tác",
    "dukkhanirodhe": "sự chấm dứt khổ đau", "upādāne": "sự bám víu", "viññāṇe": "thức", "phasse": "sự tiếp xúc",
    "sammuti": "quy ước", "taṇhāya": "khao khát", "maraṇe": "sự chết", "visesa": "thăng tiến",
    "pariye": "bao quát tâm", "samaṅgissa": "người có được", "bhave": "sự hiện hữu", "vedanāya": "cảm giác",
    "rūpe": "vật chất", "saṅkhāresu": "sự tạo tác", "phala": "thành quả", "anvaye": "suy diễn",
    "anvaye ñāṇaṃ": "sự hiểu biết bằng suy diễn", "pariye ñāṇaṃ": "sự hiểu biết bao quát tâm",
    "viññāṇe ñāṇaṃ": "sự hiểu biết về thức", "saṅkhāresu ñāṇaṃ": "sự hiểu biết về các sự tạo tác",
    "viññāṇepetaṃ ñāṇaṃ": "cũng là sự hiểu biết về thức",
    "nāma": "phần tinh thần", "nāmarūpe": "phần tinh thần và vật chất", "paṭipadā": "cách thực hành",
    "ārammaṇāni": "đối tượng", "samudaye": "sự phát sinh", "dukkhasamudaye": "sự phát sinh của khổ đau",
    "samudaya": "sự phát sinh", "nirodha": "sự chấm dứt", "āyatane": "lĩnh vực nhận biết",
    "nibbedhabhāginī": "thuộc về phía xuyên thấu", "hānabhāginī": "thuộc về phía suy giảm",
    "visesabhāginī": "thuộc về phía thăng tiến", "ṭhitibhāginī": "thuộc về phía duy trì", "ṭhiti": "duy trì",
    "dukkhe": "khổ đau", "kammānaṃ": "nghiệp", "samaṇa": "sa-môn", "samaṇā": "sa-môn", "ṭhapetvā": "ngoại trừ",
    "dukkaṭānaṃ": "làm xấu", "sukata": "làm tốt", "sattā": "chúng sinh", "brāhmaṇā": "bà-la-môn",
    "sammaggatā": "đã đi đúng đắn", "pavedentī": "tuyên bố", "abhiññā": "hiểu biết trực tiếp", "pitā": "cha",
    "mātā": "mẹ", "phalaṃ": "quả", "evarūpā": "thuộc loại như vậy", "paṭipannā": "thực hành",
    "sacchikatvā": "chứng nghiệm", "opapātikā": "hóa sinh", "hutaṃ": "cúng dường", "sayaṃ": "tự mình", "yā": "điều",
    "kusalā paññā": "trí tuệ thiện",
    "sattānaṃ": "chúng sinh", "nirodhaṃ": "sự chấm dứt", "dukkhanirodhaṃ": "sự chấm dứt khổ đau",
    "samudayaṃ": "sự phát sinh", "dukkhasamudayaṃ": "sự phát sinh của khổ đau", "dukkhaṃ": "khổ đau",
    "abbhaññaṃsu": "đã hiểu biết trực tiếp", "dukkhaṃ abbhaññaṃsu": "đã hiểu biết trực tiếp khổ đau",
    "abhijānissanti": "sẽ hiểu biết trực tiếp", "nayaṃ": "suy ra", "neti": "suy ra", "paricca": "bao quát",
    "ñātena": "đã được biết", "viditena": "đã được hiểu", "pariyogāḷhena": "đã được thâm nhập",
    "ceto": "tâm", "bhikkhu": "vị tỳ-khưu", "puggalānaṃ": "người", "avasesā": "còn lại",
    "avasesā paññā": "trí tuệ còn lại", "ye hi keci": "bất cứ … nào", "pajānāti": "hiểu rõ", "cittaṃ": "tâm",
    "kāmāvacarakusalābyākate paññā": "trí tuệ trong tâm thiện và " + _KX + " thuộc cõi dục lạc",
    "hoti": NDE,                                                                 # ^2-798 «… vītarāgo hoti»
    "abhiññāyo": "loại hiểu biết trực tiếp", "vītarāgo": "lìa tham đắm", "paṭivijjhati": "thấu triệt",
    "kāmesu": "dục lạc", "saccāni": "sự thật",
    # ^2-799
    "avitakka": "không có sự hướng tâm", "jhānassa": "tầng thiền", "nibbidāsahagatā": "có sự nhàm chán đi kèm",
    "pītisukhasahagatā": "có sự hân hoan và hạnh phúc đi kèm", "manasikārā": "sự chú tâm",
    "kāmasahagatā saññāmanasikārā": "tri giác và sự chú tâm có dục lạc đi kèm", "samudācaranti": "khởi lên",
    "anudhammatā": "phù hợp", "ūpasañhitā": "liên quan đến", "virāgūpasañhitā": "liên quan đến sự phai nhạt",
    "viññāṇañcāyatanassa": "lĩnh vực thức vô tận", "nibbidā": "sự nhàm chán", "āyatana": "lĩnh vực",
    "ākāsānañcāyatanassa": "lĩnh vực không gian vô tận", "ākiñcaññāyatanassa": "lĩnh vực không có gì cả",
    "rūpa": "hình sắc", "catutthassa jhānassa": "tầng thiền thứ tư", "lābhiṃ": "người đã đạt được",
    "ānañcāyatana": "lĩnh vực" + GAP + "vô tận", "pītisukha": "sự hân hoan và hạnh phúc", "sati": "sự tỉnh thức",
    "tadanudhammatā sati": "sự tỉnh thức phù hợp với điều ấy",
    "adukkhamasukha": "không khó chịu cũng không dễ chịu",
    "nevasaññānāsaññāyatanasahagatā": "có lĩnh vực không phải tri giác cũng không phải không tri giác đi kèm",
    "saññāmanasikārā": "tri giác và sự chú tâm", "kāma": "dục lạc", "santiṭṭhati": "đứng vững",
    "tadanudhammatā sati santiṭṭhati": "sự tỉnh thức phù hợp với điều ấy đứng vững",
    # ^2-800 (ch15 values)
    "ābhilāpe": "lời diễn tả", "nirutti": "cách diễn đạt", "atthe": "ý nghĩa", "paṭibhāna": "tài ứng đáp",
    # ^2-801 / ^2-802
    "samādhiṃ": "định tâm", "dukkha": "khó khăn", "dukkhapaṭipadā": "cách thực hành khó khăn", "kasirena": "vất vả",
    "kicchena": "khó nhọc", "ābhiññā": "sự hiểu biết trực tiếp", "sukhapaṭipadā": "cách thực hành dễ dàng",
    "abhijānantassa": "hiểu biết trực tiếp", "uppādentassa": "làm sinh khởi",
    "khippābhiññā": "sự hiểu biết trực tiếp nhanh chóng", "dandhābhiññā": "sự hiểu biết trực tiếp chậm chạp",
    "khippaṃ": "nhanh chóng", "dandhaṃ": "chậm chạp",
    "dukkhapaṭipadā khippābhiññā": "cách thực hành khó khăn và sự hiểu biết trực tiếp nhanh chóng",
    "dukkhapaṭipadā dandhābhiññā": "cách thực hành khó khăn và sự hiểu biết trực tiếp chậm chạp",
    "samādhissa": "định tâm", "nikāma": "theo ý muốn", "lābhissa": "người" + GAP + "đạt được",
    "ārammaṇaṃ": "đối tượng", "pharantassa": "lan tỏa", "vipulaṃ": "rộng rãi",
    # ^2-803
    "saṅkhāranirodhaṃ": "sự chấm dứt các sự tạo tác", "saṅkhāre": "sự tạo tác",
    # ^2-804 / 2-805 / 2-806
    "jhānesu": "tầng thiền", "ādhigato": "đạt đến", "samādhi": "định tâm", "dibba": "thiên", "cakkhu": "nhãn",
    "sasaṅkhāra": "có sự thúc đẩy", "vuṭṭhahāmī": "xuất khỏi", "vuṭṭhitassa": "người đã xuất khỏi",
    "samāpajjāmi": "chứng nhập", "pañcaṅgiko": "gồm năm chi phần", "pañcañāṇiko": "gồm năm sự hiểu biết",
    "niggayha": "sự kiềm chế", "ñāṇaṃ uppajjati": "sự hiểu biết sinh khởi", "āloka": "ánh sáng",
    "sasaṅkhāraniggayhavāritagato": "đạt được nhờ sự kiềm chế và ngăn chặn có sự thúc đẩy",
    "sato": "với sự tỉnh thức", "ariyo": "cao quý", "laddho": "đạt được", "paccattaññeva": "ngay nơi tự thân",
    "paracitte": "tâm người khác", "santo": "an tịnh", "akāpurisasevito": "được những người không hèn kém thực hành",
    "pharaṇatā": "sự lan tỏa", "sukho": "hạnh phúc", "sevito": "thực hành", "paṇīto": "ưu việt",
    "paccavekkhaṇā": "sự xem xét lại", "paccavekkhaṇāñāṇaṃ": "sự hiểu biết xem xét lại", "nimittaṃ": "dấu hiệu",
    "vārita": "ngăn chặn", "paṭippassaddha": "sự lắng dịu hoàn toàn",
    "ekodibhāvādhigato": "đạt đến sự hợp nhất của tâm", "nirāmiso": "không có tính trần tục",
    "cutūpapāte": "sự chết và sự tái sinh", "khaye": "sự diệt tận", "abhiññāsu": "loại hiểu biết trực tiếp",
    "sota": "tai", "sotadhātu": "yếu tố tai", "dhātu": "yếu tố", "vidhe": "loại",
    "pubbenivāsānussatiyā": "sự nhớ lại các đời sống trước", "āsavānaṃ": "ô nhiễm", "iddhi": "thần thông",
    "visuddhiyā": "sự trong sạch", "ūpapāte": "sự tái sinh", "ānussatiyā": "sự nhớ lại",
    "jarāmaraṇa": "sự lão hóa và sự chết", "virāga": "phai nhạt", "jāti": "sự sinh",
    "paccayā": "làm điều kiện", "jātipaccayā": "sự sinh làm điều kiện",
    "upādānapaccayā": "sự bám víu làm điều kiện", "viññāṇa": "thức", "viññāṇapaccayā": "thức làm điều kiện",
    "phassa": "sự tiếp xúc", "phassapaccayā": "sự tiếp xúc làm điều kiện", "taṇhā": "khao khát",
    "taṇhāpaccayā": "khao khát làm điều kiện", "maraṇa": "sự chết", "khaya": "diệt tận", "bhava": "sự hiện hữu",
    "bhavapaccayā": "sự hiện hữu làm điều kiện", "vedanāpaccayā": "cảm giác làm điều kiện",
    "ṭṭhiti": "tính ổn định", "nāmarūpapaccayā": "phần tinh thần và vật chất làm điều kiện",
    "saṅkhārapaccayā": "các sự tạo tác làm điều kiện", "avijjā": "vô minh", "avijjāpaccayā": "vô minh làm điều kiện",
    "tampi": "điều đó cũng", "nāmarūpa": "phần tinh thần và vật chất",
    "saḷāyatanapaccayā": "sáu lĩnh vực nhận biết làm điều kiện", "vaya": "suy tàn",
    # ^2-807 / 2-808
    "anāgāmi": "không trở lại", "sakadāgāmi": "trở lại một lần", "magge": "con đường", "sotāpatti": "vào dòng",
    "jhāna": "tầng thiền", "samāpattiyā": "sự chứng đạt", "samāpattīsu": "sự chứng đạt",
    "viññāṇañcāyatanasamāpattiyā": "sự chứng đạt lĩnh vực thức vô tận", "vihāra": "an trú",
    "vedayita": "cảm giác", "ākāsānañcāyatana": "lĩnh vực không gian vô tận",
    "ākiñcaññāyatanasamāpattiyā": "sự chứng đạt lĩnh vực không có gì cả", "catutthajjhāna": "tầng thiền thứ tư",
    "ākāsānañcāyatanasamāpattiyā": "sự chứng đạt lĩnh vực không gian vô tận",
    "nevasaññānāsaññāyatanasamāpattiyā":
        "sự chứng đạt lĩnh vực không phải tri giác cũng không phải không tri giác",
    "anupubba": "tuần tự",
    # ================================================================ ten powers (2-760, 2-809 … 2-831)
    "parisāsu": "hội chúng", "samāpattīnaṃ": "sự chứng đạt", "cutūpapātaṃ": "sự chết và sự tái sinh",
    "āsabhaṃ": "bậc dẫn đầu", "hetuso": "theo nguyên nhân", "ṭhānaso": "theo hoàn cảnh", "paṭijānāti": "tuyên bố",
    "ṭhānaṃ paṭijānāti": "tuyên bố vị trí", "vodānaṃ": "sự trong sạch", "saṃkilesaṃ": "sự vẩn đục",
    "khayaṃ": "sự diệt tận", "vuṭṭhānaṃ": "sự xuất khỏi", "samannāgato": "được trang bị", "sabbattha": "mọi nơi",
    "indriya": "năng lực", "aṭṭhānato": "điều không thể xảy ra", "ādhimuttikataṃ": "chí hướng",
    "gāminiṃ": "dẫn đến", "vimokkha": "sự giải thoát", "sīha": "sư tử",
    "pubbenivāsānussatiṃ": "sự nhớ lại các đời sống trước", "parapuggalānaṃ": "người khác", "ṭhānaṃ": "vị trí",
    "balaṃ": "sức mạnh", "balaṃ āgamma tathāgato": "nhờ dựa vào sức mạnh ấy mà Như Lai",
    "yathābhūtaṃ": "đúng như thật", "ūpapātaṃ": "sự tái sinh", "ānussatiṃ": "sự nhớ lại", "āgamma": "nhờ dựa vào",
    "nādaṃ": "tiếng rống", "nadati": "rống", "sīhanādaṃ nadati": "rống tiếng rống sư tử", "pavatteti": "chuyển",
    "brahmacakkaṃ pavatteti": "chuyển bánh xe cao thượng", "tathāgato": "Như Lai",
    "tathāgatabalāni": "sức mạnh Như Lai", "samādānānaṃ": "đã thực hiện",
    "kammasamādānānaṃ": "nghiệp đã thực hiện", "cakkaṃ": "bánh xe", "brahmacakkaṃ": "bánh xe cao thượng",
    # ^2-809
    "sampanno": "thành tựu", "diṭṭhisampanno": "thành tựu về quan điểm", "upādāya": "tùy thuộc vào",
    "uddiseyya": "tôn" + GAP + "làm", "manāpo": "đáng ưa thích", "manāpo vipāko": "quả" + GAP + "đáng ưa thích",
    "arahaṃ": "bậc A-la-hán", "arahanto": "bậc A-la-hán", "uppajjeyyuṃ": "xuất hiện",
    "sambuddho": "Tự Giác Ngộ", "sammāsambuddho": "Tự Giác Ngộ Hoàn Toàn",
    "sammāsambuddhā": "Tự Giác Ngộ Hoàn Toàn", "duggatiṃ": "cõi xấu", "lohitaṃ": "máu", "kāya": "thân",
    "kāyasucarita": "hành vi tốt bằng thân", "kāyaduccarita": "hành vi xấu bằng thân", "kāyassa": "thân",
    "paraṃ maraṇā": "sau khi chết", "bhedā": "tan rã", "anavakāso": "không có cơ hội", "sucarita": "hành vi tốt",
    "maraṇā": "chết", "voropeyya": "tước đoạt", "kanto": "đáng yêu mến", "gatiṃ": "cõi",
    "amanāpo": "không đáng ưa thích", "amanāpo vipāko": "quả" + GAP + "không đáng ưa thích",
    "aṭṭhamaṃ": "thứ tám", "kareyya": "giữ", "bhavaṃ": "lần hiện hữu", "pitaraṃ": "cha", "saṅkhāraṃ": "sự tạo tác",
    "sugatiṃ": "cõi tốt lành", "manosucarita": "hành vi tốt bằng ý", "vacīsucarita": "hành vi tốt bằng lời nói",
    "paduṭṭhena": "độc ác", "saggaṃ": "cõi trời", "saggaṃ lokaṃ": "thế giới cõi trời", "nirayaṃ": "địa ngục",
    "aṭṭhānametaṃ": "điều không thể xảy ra", "rājā": "vua", "rājāno": "vua", "jīvitā": "mạng sống",
    "puriso": "người nam", "manoduccarita": "hành vi xấu bằng ý", "cittena": "tâm", "duccarita": "hành vi xấu",
    "mātaraṃ": "mẹ", "saṅghaṃ": "Tăng đoàn", "puthujjano": "người phàm", "niccato": "thường hằng",
    "puggalo": "người", "diṭṭhisampanno puggalo": "người thành tựu về quan điểm", "vinipātaṃ": "nơi đọa lạc",
    "sukhato": "hạnh phúc", "nibbatteyya": "tạo ra", "upapajjeyya": "tái sinh", "sakkattaṃ": "địa vị Đế Thích",
    "atthato": "tự ngã",                                                       # ^2-809 slip for attato, as meant
    "uppādeyya": "làm cho" + GAP + "chảy", "satthāraṃ": "bậc đạo sư", "akanto": "không đáng yêu mến",
    "aniṭṭho": "không đáng mong muốn", "vacī": "lời nói", "vacīduccarita": "hành vi xấu bằng lời nói",
    "ye ye": "nào", "cakkavattī": "chuyển luân", "iṭṭho": "đáng mong muốn", "itthī": "người nữ",
    "lokadhātuyā": "thế giới", "hetū ": "nguyên nhân",
    # ^2-810
    "kammasamādānāni": "nghiệp" + GAP + "đã thực hiện", "vipaccanti": "trổ quả", "paṭibāḷhāni": "ngăn trở",
    "upadhi": "thân thể", "gati": "cõi tái sinh", "payoga": "sự nỗ lực", "pāpakāni": "xấu ác",
    "pāpakāni kammasamādānāni": "nghiệp xấu ác đã thực hiện", "sampatti": "sự thuận lợi",
    "kalyāṇāni kammasamādānāni": "nghiệp tốt đẹp đã thực hiện", "samādānāni": "đã thực hiện",
    "vipattiṃ": "sự bất lợi",
    # ^2-811 / 2-812
    "tiracchāna": "súc sinh", "yoni": "loài", "petti": "ngạ quỷ", "deva": "trời", "niraya": "địa ngục",
    "manussa": "người", "gāmī": "dẫn đến", "maggo": "con đường", "visaya": "cõi", "khandha": "khối",
    "nānattaṃ": "sự khác nhau",
    # ^2-813 … 2-827
    "payirupāsanti": "thường xuyên lui tới hầu cận", "payirupāsiṃsu": "đã thường xuyên lui tới hầu cận",
    "bhajanti": "lui tới", "bhajiṃsu": "đã lui tới", "ādhimuttikā": "có chí hướng", "sevanti": "gần gũi",
    "seviṃsu": "đã gần gũi", "sevissanti": "sẽ gần gũi", "hīnādhimuttikā": "có chí hướng thấp kém",
    "paṇītādhimuttikā": "có chí hướng ưu việt",
    "dvākāre": "có phẩm chất xấu", "bhabbābhabbe": "có khả năng và không có khả năng", "ākāre": "phẩm chất",
    "caritaṃ": "tính hạnh", "āsayaṃ": "thiên hướng", "mudindriye": "có các năng lực non yếu",
    "rajakkhe": "bụi trong mắt", "suviññāpaye": "dễ hướng dẫn", "akkhe": "mắt", "indriye": "năng lực",
    "svākāre": "có phẩm chất tốt", "duviññāpaye": "khó hướng dẫn", "ābhabbe": "không có khả năng",
    "adhimuttiṃ": "chí hướng", "viññāpaye": "hướng dẫn", "tikkhindriye": "có các năng lực sắc bén",
    "anusayaṃ": "khuynh hướng tiềm ẩn",
    "samuppannesu": "sinh khởi", "anupagamma": "không đi đến", "sarīra": "thân thể",
    "paccayatā": "quy luật tùy thuộc vào điều kiện", "paṭicca": "tùy thuộc vào điều kiện", "āsayo": "thiên hướng",
    "sassato": "trường tồn", "ante": "cực đoan", "antavā": "hữu hạn", "paṭiladdhā": "đã đạt được",
    "anantavā": "vô hạn", "vibhava": "sự không còn hiện hữu", "sannissitā": "nương tựa", "jīvaṃ": "linh hồn",
    "idappaccayatā": "quy luật tùy thuộc vào điều kiện", "hoti tathāgato": "Như Lai còn tồn tại",
    "dhammesu": "hiện tượng", "bhavadiṭṭhi": "quan điểm về sự hiện hữu",
    "vibhavadiṭṭhi": "quan điểm về sự không còn hiện hữu",
    "sātarūpaṃ": "điều khoan khoái", "paṭighānusayo": "khuynh hướng tiềm ẩn ác cảm", "māno": "sự kiêu mạn",
    "piyarūpaṃ": "điều đáng yêu", "appiyarūpaṃ": "điều không đáng yêu", "vicikicchā": "sự hoài nghi",
    "ānupatitā": "đi theo", "anuseti": "nằm sẵn", "rāgānusayo": "khuynh hướng tiềm ẩn tham đắm",
    "ekaṭṭho": "cùng hiện diện", "ānusayā": "khuynh hướng tiềm ẩn", "anusayo": "khuynh hướng tiềm ẩn",
    "tadekaṭṭho": "cùng hiện diện với nó", "asātarūpaṃ": "điều không khoan khoái",
    "apuññābhisaṅkhāro": "sự tạo tác không thuộc về phước", "ābhisaṅkhāro": "sự tạo tác",
    "āneñjābhisaṅkhāro": "sự tạo tác dẫn đến trạng thái bất động", "paritta": "nhỏ",
    "puññābhisaṅkhāro": "sự tạo tác thuộc về phước", "bhūmako": "thuộc cấp độ", "adhimutti": "chí hướng",
    "bahulīkatāni": "được làm đi làm lại", "moho": "sự si mê", "bhāvitāni": "được tu tập",
    "anottappaṃ": "sự không biết ghê sợ tội lỗi", "thinaṃ": "sự uể oải", "rajakkhā": "bụi trong mắt",
    "akkhā": "mắt", "lobho": "sự tham lam", "doso": "sự sân hận", "ussadagatāni": "trở nên nổi trội",
    "āsevitāni": "được thực hành", "uddhaccaṃ": "sự xao động", "ahirikaṃ": "sự không biết hổ thẹn",
    "abahulīkatāni": "không được làm đi làm lại", "abhāvitāni": "không được tu tập",
    "anussadagatāni": "không trở nên nổi trội", "anāsevitāni": "không được thực hành",
    "samādhindriyaṃ": "năng lực định tâm", "saddhindriyaṃ": "năng lực niềm tin", "mudindriyā": "có các năng lực non yếu",
    "indriyāni": "năng lực", "indriyaṃ": "năng lực", "vīriyindriyaṃ": "năng lực tinh tấn",
    "satindriyaṃ": "năng lực tỉnh thức", "paññindriyaṃ": "năng lực trí tuệ", "tikkhindriyā": "có các năng lực sắc bén",
    "dvākārā": "có phẩm chất xấu", "ākārā": "phẩm chất", "caritā": "tính hạnh", "āsayā": "thiên hướng",
    "pāpa": "xấu ác", "indriyā": "năng lực", "svākārā": "có phẩm chất tốt",
    "kalyāṇacaritā": "có tính hạnh tốt đẹp", "kalyāṇādhimuttikā": "có chí hướng tốt đẹp",
    "suviññāpayā": "dễ hướng dẫn", "duviññāpayā": "khó hướng dẫn", "viññāpayā": "hướng dẫn",
    "assaddhā": "không có niềm tin", "niyāmaṃ": "sự cố định", "kilesāvaraṇena": "sự ngăn che do phiền não",
    "acchandikā": "không có ý muốn", "okkamituṃ": "bước vào", "abhabbā": "không có khả năng",
    "āvaraṇena": "sự ngăn che", "kammāvaraṇena": "sự ngăn che do nghiệp", "samannāgatā": "mang",
    "āvaraṇena samannāgatā": "mang sự ngăn che", "sammattaṃ": "sự đúng đắn", "kusalesu": "thiện",
    "kusalesu dhammesu": "hiện tượng thiện", "duppaññā": "trí tuệ kém", "bhabbā": "có khả năng",
    "saddhā": "có niềm tin", "chandikā": "có ý muốn",
    # ^2-828
    "jhānaṃ": "tầng thiền", "jhānāni": "tầng thiền", "samāpatti": "sự chứng đạt",
    "samādhismiṃ samāpatti": "sự chứng đạt trong định tâm", "subhanteva": "đẹp", "samatikkamma": "vượt qua",
    "vodāna": "sự trong sạch", "sabbaso": "hoàn toàn", "samādhismiṃ samādhi": "định tâm trong định tâm",
    "samādhī": "định tâm", "saṃkilesa": "sự vẩn đục", "atthaṅgamā": "biến mất", "nānatta": "sự đa dạng",
    "viharati": "an trú", "aṭṭhamo": "thứ tám", "vuṭṭhāna": "sự xuất khỏi", "vuṭṭhānampi": "sự xuất khỏi",
    "upasampajja": "chứng nhập", "upasampajja viharati": "chứng nhập và an trú",
    "khippaṃ samāpajjati": "chứng nhập nhanh", "dandhaṃ samāpajjati": "chứng nhập chậm", "vicāro": "sự duy trì tâm",
    "vipatti": "sự thất bại", "āyatanaṃ": "lĩnh vực", "ākāsānañcāyatanaṃ": "lĩnh vực không gian vô tận",
    "ākiñcaññāyatanaṃ": "lĩnh vực không có gì cả", "pañcamo": "thứ năm", "rūpāni": "hình sắc",
    "catutthaṃ jhānaṃ": "tầng thiền thứ tư", "ananto": "vô tận", "viññāṇañcāyatanaṃ": "lĩnh vực thức vô tận",
    "ajjhattaṃ": "ở nơi bản thân", "vimokkho": "sự giải thoát", "vimokkhā": "sự giải thoát",
    "jhāyī": "người hành thiền",
    "nevasaññānāsaññāyatanaṃ": "lĩnh vực không phải tri giác cũng không phải không tri giác",
    "natthi kiñci": "không có gì cả", "saññī": "có tri giác", "saññānaṃ": "tri giác",
    "nānattasaññānaṃ": "tri giác về sự đa dạng", "rūpasaññānaṃ": "tri giác về hình sắc",
    "paṭighasaññānaṃ": "tri giác về sự va chạm", "rūpī": "có hình sắc", "paṭigha": "sự va chạm",
    "adhimutto": "quyết định", "sattamo": "thứ bảy", "hānabhāgiyo": "thuộc về phía suy giảm",
    "visesabhāgiyo": "thuộc về phía thăng tiến", "chaṭṭho": "thứ sáu", "kusalo": "khéo léo", "ākāso": "không gian",
    "pacceti": "cho rằng", "samānaṃ": "vốn là",
    # ^2-829
    "vaṇṇo": "dung mạo", "udapādiṃ": "đã sinh ra", "sākāraṃ": "với các nét đặc trưng", "cuto": "chết",
    "jātiṃ": "đời", "jātiyo": "đời", "gotto": "dòng họ", "amutra": "ở nơi kia", "kappe": "kiếp thế giới",
    "vivaṭṭa": "hình thành", "paṭisaṃvedī": "cảm nhận", "paññāsampi": "năm mươi", "āhāro": "thức ăn",
    "cattālīsampi": "bốn mươi", "satampi": "một trăm", "āyu": "tuổi thọ", "pubbenivāsaṃ": "đời sống trước",
    "anekavihitaṃ": "nhiều" + GAP + "theo nhiều cách", "nāmo": "tên", "ūpapanno": "tái sinh",
    "ānussati": "sự nhớ lại", "anussarati": "nhớ lại", "pariyanto": "đến mức", "dasapi": "mười",
    "dasapi jātiyo": "mười đời", "tiṃsampi": "ba mươi", "sahassampi": "một nghìn", "vīsampi": "hai mươi",
    "saṃvaṭṭa": "tan hoại",
    # ^2-830
    "yathākammūpage": "đi theo nghiệp của mình", "cavamāne": "đang chết đi", "suvaṇṇe": "đẹp đẽ",
    "kāyasucaritena": "hành vi tốt bằng thân", "kāyaduccaritena": "hành vi xấu bằng thân",
    "sucaritena": "hành vi tốt", "dibbena": "thiên", "cakkhunā": "nhãn", "ūpage": "đi theo",
    "sugate": "cõi tốt lành", "manosucaritena": "hành vi tốt bằng ý", "vacīsucaritena": "hành vi tốt bằng lời nói",
    "mānusakena": "người", "vata": "quả thật", "hīne": "thấp kém", "manoduccaritena": "hành vi xấu bằng ý",
    "duccaritena": "hành vi xấu", "ariyānaṃ": "bậc thánh", "visuddhena": "thanh tịnh", "upapannā": "đã tái sinh",
    "paṇīte": "ưu việt", "upavādakā": "phỉ báng", "atikkanta": "vượt quá", "dubbaṇṇe": "xấu xí",
    "samādānā": "thực hiện", "duggate": "cõi xấu", "vacīduccaritena": "hành vi xấu bằng lời nói",
    "micchā": "sai lầm", "micchādiṭṭhikā": "có quan điểm sai lầm",
    # ^2-831
    "viharatī": "an trú", "upasampajja viharatī": "chứng nhập và an trú", "vimuttiṃ": "sự giải thoát",
    "cetovimuttiṃ": "sự giải thoát của tâm", "diṭṭheva dhamme": "ngay trong đời này",
    "anāsavaṃ": "không còn ô nhiễm",
    # ^2-761 «chắc chắn …» (pi-1 3-01 "-meva" values: the separate na / no stays outside the value)
    "acetasikameva": "chắc chắn không phải là yếu tố đồng hành với tâm", "aniyatameva": "chắc chắn không cố định",
    "arūpameva": "chắc chắn phi vật chất", "hetumeva": "chắc chắn" + GAP + "gốc rễ",
    "vicārameva": "chắc chắn" + GAP + "sự duy trì tâm", "ābhibhūtameva": "chắc chắn bị" + GAP + "chế ngự",
    "āvacarameva": "chắc chắn thuộc cõi",
    # ^2-796 the ch7 ^2-365 mind list (quoted «“tâm …”»)
    "sarāgaṃ": "có tham đắm", "sadosaṃ": "có sân hận", "samohaṃ": "có si mê", "saṃkhittaṃ": "co rút",
    "vikkhittaṃ": "tán loạn", "mahaggataṃ": "rộng lớn", "amahaggataṃ": "không rộng lớn",
    "sauttaraṃ": "còn có điều cao hơn", "anuttaraṃ": "không có điều gì cao hơn", "asamāhitaṃ": "không được định tâm",
    "vimuttaṃ": "được giải thoát", "avimuttaṃ": "không được giải thoát",
    # ^2-767
    "arahato": "vị A-la-hán", "uppannāya": "đã sinh khởi",
}
for _x, _v in (("sarāgaṃ", "có tham đắm"), ("vītarāgaṃ", "đã lìa tham đắm"), ("sadosaṃ", "có sân hận"),
               ("vītadosaṃ", "đã lìa sân hận"), ("samohaṃ", "có si mê"), ("vītamohaṃ", "đã lìa si mê"),
               ("saṃkhittaṃ", "co rút"), ("vikkhittaṃ", "tán loạn"), ("mahaggataṃ", "rộng lớn"),
               ("amahaggataṃ", "không rộng lớn"), ("sauttaraṃ", "còn có điều cao hơn"),
               ("anuttaraṃ", "không có điều gì cao hơn"), ("samāhitaṃ", "được định tâm"),
               ("asamāhitaṃ", "không được định tâm"), ("vimuttaṃ", "được giải thoát"),
               ("avimuttaṃ", "không được giải thoát")):
    T16[f"{_x} citta"] = f"tâm {_v}"                                       # «“tâm có tham đắm”»

# «X paññā»: attributes whose Vietnamese is not a plain matrix predicate (build_16_vi EXTRA)
PANNA_ATTR = {
    "atthajāpikā": "tạo ra lợi ích", "jāpitatthā": "có lợi ích đã được tạo ra",
    "cintāmayā": "được tạo nên từ sự suy tư", "sutamayā": "được tạo nên từ sự lắng nghe",
    "bhāvanāmayā": "được tạo nên từ sự tu tập", "dānamayā": "được tạo nên từ sự bố thí",
    "sīlamayā": "được tạo nên từ giới hạnh", "adhisīle": "trong giới hạnh cao thượng",
    "adhicitte": "trong tâm cao thượng", "adhipaññāya": "trong trí tuệ cao thượng",
    "hānabhāginī": "thuộc về phía suy giảm", "ṭhitibhāginī": "thuộc về phía duy trì",
    "visesabhāginī": "thuộc về phía thăng tiến", "nibbedhabhāginī": "thuộc về phía xuyên thấu",
    "dukkhapaṭipadā dandhābhiññā": "với cách thực hành khó khăn và sự hiểu biết trực tiếp chậm chạp",
    "dukkhapaṭipadā khippābhiññā": "với cách thực hành khó khăn và sự hiểu biết trực tiếp nhanh chóng",
    "sukhapaṭipadā dandhābhiññā": "với cách thực hành dễ dàng và sự hiểu biết trực tiếp chậm chạp",
    "sukhapaṭipadā khippābhiññā": "với cách thực hành dễ dàng và sự hiểu biết trực tiếp nhanh chóng",
    "parittā parittārammaṇā": "hạn hẹp và có đối tượng hạn hẹp",
    "parittā appamāṇārammaṇā": "hạn hẹp và có đối tượng không thể đo lường",
    "appamāṇā parittārammaṇā": "không thể đo lường và có đối tượng hạn hẹp",
    "appamāṇā appamāṇārammaṇā": "không thể đo lường và có đối tượng không thể đo lường",
    "vitakkasampayuttā": "gắn liền với sự hướng tâm", "vicārasampayuttā": "gắn liền với sự duy trì tâm",
    "pītisampayuttā": "gắn liền với sự hân hoan", "sukhasampayuttā": "gắn liền với hạnh phúc",
    "upekkhāsampayuttā": "gắn liền với sự bình thản",
    "vitakkavicārasampayuttā": "gắn liền với sự hướng tâm và sự duy trì tâm",
    "vitakkavicāravippayuttā": "không gắn liền với sự hướng tâm và sự duy trì tâm",
    "vitakkavippayuttā vicārasampayuttā": "không gắn liền với sự hướng tâm gắn liền với sự duy trì tâm",
    "kusalā": "thiện", "avasesā": "còn lại", "vibhāvanā": "làm sáng tỏ",
    "uppannā": "đã sinh khởi", "anuppannā": "chưa sinh khởi", "uppādinī": "sẽ sinh khởi",
    "atītā": "thuộc quá khứ", "anāgatā": "thuộc tương lai", "paccuppannā": "thuộc hiện tại",
    "niyatā": "cố định", "aniyatā": "không cố định", "mahaggatā": "rộng lớn",
    "na pītisahagatā": "không có sự hân hoan đi kèm",
}
LOC_RE = re.compile(r"^(bhūmīsu) (kusalābyākate|kusale|vipāke|kiriyābyākate)$|^(maggesu|phalesu)$")


def attr_value(a, table):
    """Bare Vietnamese predicate of a paññā attribute (matrix value; two-word clusters = the compound)."""
    a = lc(a)
    if a in PANNA_ATTR:
        return PANNA_ATTR[a]
    a2 = re.sub(r"^(\w+)vippayuttā (\w+)$", r"\1vippayutta\2", a)
    return value(a2, [a2], table)


def panna(k, table, text):
    """«X paññā» -> «trí tuệ (mà / mà là) X» as the segment writes it; locatives -> «trí tuệ trong … »."""
    a = k[:-len(" paññā")]
    m = LOC_RE.match(a)
    if m:
        if m.group(1):
            loc = f"trong {LOCN[m.group(2)]} thuộc{GAP}cõi"
        else:
            loc = "trong" + GAP + {"maggesu": "con đường", "phalesu": "thành quả"}[m.group(3)]
        cands = [f"{_TT} {loc}", _TT + GAP + loc]
        if m.group(3) == "phalesu":   # always after «trí tuệ trong bốn con đường,»: the second «trong»
            cands.reverse()
    else:
        b = attr_value(a, table)
        cands = [f"{_TT} {b}", f"{_TT} mà là {b}", f"{_TT} mà {b}"]
    for c in cands:
        if present(c, text):
            return c
    return cands[0]


def prio(cands, text):
    for c in cands:
        if present(c, text):
            return c
    return cands[0]


def context(bid, kw, k, s, text, kws, table):
    """Segment rules (k: lower-cased keyword, s: lower-cased keyword set). None = no rule."""
    m = re.match(r"^(ekaka|duka|tika|catukka|pañcaka|chakka|sattaka|aṭṭhaka|navaka|dasaka)$", k)
    if m:                     # «Ma trận bộ N» / «Giải thích phân loại theo nhóm N»
        return f"phân loại theo nhóm {_NUMG[k]}" if "niddeso" in s else f"bộ {_NUM[k]}"
    if k.endswith(" paññā") and k != "samāpannassa paññā" and k not in table:
        return panna(k, table, text)
    if k == "dhamme":         # «sự hiểu biết về Giáo Pháp» (catukka 4) / «các hiện tượng …»
        return prio(["hiện tượng", "Giáo Pháp"], text) if "dhamme ñāṇaṃ" not in s else "Giáo Pháp"
    if k == "ñāṇaṃ":          # pi-1 ^1-1373 names «hiểu biết …» (no «sự») where the segment has no «sự hiểu biết»
        return prio([_KN, "hiểu biết"], text)
    if k == "uppajjati":      # «không chết, không tái sinh» (na cavati na uppajjati)
        return prio(["sinh khởi", "tái sinh"], text)
    if k == "hetukā":         # only maggahetukā: «lấy con đường làm gốc rễ»
        return prio(["có gốc rễ", "lấy" + GAP + "làm gốc rễ"], text)
    if k == "ārammaṇā":       # «có đối tượng» / «lấy … làm đối tượng» / ^2-762 the noun «các đối tượng»
        if bid == "2-762":
            return "đối tượng"
        return prio(["có đối tượng", "lấy" + GAP + "làm đối tượng"], text)
    if k in ("khippaṃ", "dandhaṃ"):   # ^2-801 «một cách nhanh chóng / chậm chạp», ^2-828 «nhanh / chậm»
        return prio([{"khippaṃ": "nhanh chóng", "dandhaṃ": "chậm chạp"}[k],
                     {"khippaṃ": "nhanh", "dandhaṃ": "chậm"}[k]], text)
    if k == "mattā":          # avitakkavicāramattā «chỉ có» / abhinipātamattā «đơn thuần»
        return prio(["chỉ có", "đơn thuần"], text)
    if k == "sukha":          # factor «hạnh phúc» / ^2-801 sukhapaṭipadā «dễ dàng» / ^2-829 «sự dễ chịu»
        return prio(["hạnh phúc", "dễ dàng", "sự dễ chịu"], text)
    if k == "dukkha":         # ^2-801 «khó khăn» / ^2-829 «sự khó chịu»
        return prio(["khó khăn", "sự khó chịu"], text)
    if k == "ṭhānaṃ":         # «vị trí của bậc dẫn đầu» / ^2-766 «đứng»
        return prio(["vị trí", "đứng"], text)
    if k == "samannāgatā":    # ^2-826/827 «mang sự ngăn che» / ^2-830 «có hành vi …»
        return prio(["mang", "có"], text)
    if k == "dhamma":         # dhammavicayo «các hiện tượng» / ^2-803 Dhammasamaṅgissa «Giáo Pháp»
        if kw == "Dhamma":
            return "Giáo Pháp"
        return "hiện tượng"
    if k == "nibbatteyya":    # «tạo ra lần hiện hữu thứ tám» / «sinh ra quả»
        return prio(["tạo ra", "sinh ra"], text)
    if k == "paccavekkhaṇā":  # ^2-804 «dấu hiệu của sự xem xét lại» / ^2-808 «sự hiểu biết xem xét lại»
        return prio(["sự xem xét lại", "xem xét lại"], text)
    if k == "dhammā":         # fragment of -vipākadhammadhammā (as ^2-701 …) / ^2-771 «các hiện tượng»
        return NDE if "vipākadhammadhammā" in s else "hiện tượng"
    if k == "samudaya":       # «sự phát sinh của …»
        return "sự phát sinh"
    if k in PRIO:
        return prio(PRIO[k], text)
    return None


PRIO = {   # same Pāli, the segment's own Vietnamese (first candidate present in the segment)
    "hetū": ["gốc rễ", "nguyên nhân"],                       # ^2-809 «là nguyên nhân, là điều kiện»
    "nirodha": ["sự chấm dứt", "chấm dứt"],                  # ^2-806 «có bản chất phải chấm dứt», ^2-808
    "rūpa": ["hình sắc", "vật chất"],                        # ^2-806 nāmarūpa «phần tinh thần và vật chất»
    "sampatti": ["sự thuận lợi", "sự thành công"],           # ^2-828 «sự thành công / sự thất bại»
    "bhava": ["sự hiện hữu", "hiện hữu"],                    # ^2-816 bhavarāgānusayo «tham đắm hiện hữu»
    "amanasikārā": ["không có sự chú tâm", "không chú tâm"],  # ^2-828 «nhờ không chú tâm đến»
    "bahiddhārammaṇā": ["có đối tượng ở bên ngoài bản thân", "có đối tượng" + GAP + "ở bên ngoài bản thân"],
    "samāhitaṃ": ["được định tâm"],
    "āyatana": ["lĩnh vực nhận biết", "lĩnh vực"],         # saḷāyatana «sáu lĩnh vực nhận biết» / ākāsānañcāyatana …
}


OVERRIDES = {
    "2-16-0": {"Ñāṇa": "loại hiểu biết"},              # «Phân tích các loại hiểu biết» (title stem, as ch15)
    "2-751": {"uppajjati": "tái sinh"},                 # only in «na cavati na uppajjati» («không chết, không tái sinh»)
    "2-754": {"Dhamme": "Giáo Pháp"},                   # «sự hiểu biết về Giáo Pháp» (catukka 4)
    "2-796": {"dhamme": "Giáo Pháp"},                   # dhamme ñāṇaṃ «sự hiểu biết về Giáo Pháp»
    "2-815": {"hoti": "còn tồn tại"},                   # «Như Lai còn tồn tại sau khi chết»
    "2-765": {"uppanna": "sinh khởi"},              # uppannasamanantarā «ngay liền sau khi … sinh khởi»
    "2-816": {"Yaṃ": "điều", "rūpaṃ": "điều"},          # «Điều gì trong thế gian là điều đáng yêu» (as ch4)
}


def resolver_for(part):
    vi = read_vietnamese(part)
    table = {**T45, **T79, **T1012, **T1315, **T16}

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        k = lc(kw)
        s = set(lc(x) for x in kws)
        text = vi.get(bid, "")
        v = context(bid, kw, k, s, text, kws, table)
        if v is not None:
            return v
        if k in T16:
            return T16[k]
        v = context1315(bid, kw, k, s, text, kws)
        if v is not None:
            return v
        return value(kw, kws, table, text)
    return resolve


def dump(part, only_miss=False, only_fallback=False):
    res = resolver_for(part)
    vi = read_vietnamese(part)
    c, miss, where = Counter(), Counter(), {}
    for bid, kws in read_keywords(part):
        for kw in kws:
            if only_fallback and (lc(kw) in T16 or lc(kw) in PRIO or lc(kw).endswith(" paññā")
                                  or kw in OVERRIDES.get(bid, {})):
                continue
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
        p1 = pi1_map_values(kw).most_common(1)
        p1 = p1[0][0] if p1 else ""
        print(f"{kw}={v}  [{n}] {where[(kw, v)][:4]}" + (f"  pi1:{p1}" if p1 and p1 != v else "")
              + (f"  MISS {m}" if m else ""))


if __name__ == "__main__":
    if sys.argv[1:2] == ["dump"]:
        dump(sys.argv[2], sys.argv[3:4] == ["miss"], sys.argv[3:4] == ["fallback"])
    else:
        for p in PARTS:
            build_part(p, resolver_for(p))
            verify(p)
