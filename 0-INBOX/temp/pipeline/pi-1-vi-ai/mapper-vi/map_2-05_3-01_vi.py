"""Pāli->Vietnamese keyword maps for pi-1 parts 2-05-cittuppadakandam and 3-01-rupakandam.

usage: python -I -X utf8 map_2-05_3-01_vi.py [PART ...]   (writes <part>.mapped.md and verifies it)

Importing this file writes nothing (it imports map_2-04_vi.py, which imports map_2-02_2-03_vi.py; neither
rewrites its output on import).
Resolution order per keyword:
  2-05: OVERRIDES[bid][kw] -> context05() (-> the 2-04 / 2-02-2-03 context()) -> T05 (= 2-04 table + ADD05)
        via ch2_value
  3-01: OVERRIDES[bid][kw] -> ADD301 (= PRED301 + MEVA + headings) -> MATRIX -> T05 via ch2_value
PRED301 holds the matter predicates for reuse by 3-02 / 3-03 (import this file with importlib).
Conventions: vi-map-conventions.md, notes-map-2-02_2-03.md, notes-map-2-04.md; new: notes-map-2-05_3-01.md.
"""
import importlib.util
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from map_common_vi import GAP, MATRIX, NDE, SATI_BARE, build_part, ch2_value, lc, verify  # noqa: E402

_spec = importlib.util.spec_from_file_location("map_2_04_vi", HERE / "map_2-04_vi.py")
_p204 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_p204)          # import only: its __main__ block does not run

PARTS = ["2-05-cittuppadakandam", "3-01-rupakandam"]

# ==================================================================== 2-05
# New keys only (keys already in the earlier tables are changed per segment in context05 / OVERRIDES).
ADD05 = {
    # ---------------------------------------------------------------- headings and closing lines
    "suddhikaappaṇihitaṃ": "sự không mong cầu đơn thuần",
    "adhipateyya": "làm yếu tố chủ đạo",
    "suññatā": "sự trống rỗng",                     # Chandādhipateyyasuddhikasuññatā «Sự trống rỗng đơn thuần …»
    "abyākataṃ": "loại không xác định về mặt đạo đức",   # «Loại không xác định …» (classifier kept, as parittāni)
    "vipākaabyākataṃ": "loại không xác định về mặt đạo đức là quả của nghiệp",
    "kiriyāabyākataṃ": "loại không xác định về mặt đạo đức mang tính chức năng",
    "kiriyā abyākatā": "loại không xác định về mặt đạo đức mang tính chức năng",  # «Các loại …, mang tính chức năng»
    "vipākā abyākatā": "quả của nghiệp không xác định về mặt đạo đức",  # «Các quả của nghiệp, không xác định …»
    "hetuka": "có gốc rễ", "hetukā": "có gốc rễ",   # Ahetuka «không có gốc rễ» (fragment) / Sahetuka «có gốc rễ»
    "kiriyāmano": "ý mang tính chức năng", "kiriyā mano": "ý mang tính chức năng",
    "kiriyāmanodhātu": "yếu tố ý mang tính chức năng", "kiriyā manodhātu": "yếu tố ý mang tính chức năng",
    "kiriyāmanoviññāṇa": "ý thức mang tính chức năng", "kiriyā manoviññāṇa": "ý thức mang tính chức năng",
    "kiriyāmanoviññāṇadhātu": "yếu tố ý thức mang tính chức năng",
    "kiriyā manoviññāṇadhātu": "yếu tố ý thức mang tính chức năng",
    "dhātusomanassasahagatā": "yếu tố" + GAP + "có niềm vui đi kèm",
    "dhātu somanassasahagatā": "yếu tố" + GAP + "có niềm vui đi kèm",
    "manoviññāṇadhātusomanassasahagatā": "yếu tố ý thức" + GAP + "có niềm vui đi kèm",
    "manoviññāṇadhātu somanassasahagatā": "yếu tố ý thức" + GAP + "có niềm vui đi kèm",
    "dhātuupekkhāsahagatā": "yếu tố" + GAP + "có sự bình thản đi kèm",
    "dhātu upekkhāsahagatā": "yếu tố" + GAP + "có sự bình thản đi kèm",
    "manoviññāṇadhātuupekkhāsahagatā": "yếu tố ý thức" + GAP + "có sự bình thản đi kèm",
    "manoviññāṇadhātu upekkhāsahagatā": "yếu tố ý thức" + GAP + "có sự bình thản đi kèm",
    "niṭṭhitaṃ": "đã hoàn tất",
    # ---------------------------------------------------------------- world-transcending results
    "bhāvitattā": "tu tập",                         # «đã được tạo và tu tập» (katattā = đã được tạo)
    "kusalassa jhānassa": "tầng thiền thiện",
    "lokuttarassa kusalassa": "thiện vượt thế gian",
    "lokuttarassa kusalassa jhānassa": "tầng thiền thiện vượt thế gian",
    "animittaṃ": "tính chất không có dấu hiệu",     # qualifier, as suññataṃ / appaṇihitaṃ
    # «…nti kusalaṃ / …nti vipāko»: the quotation -nti has no word of its own
    "suññatanti": "tính chất trống rỗng", "animittanti": "tính chất không có dấu hiệu",
    "appaṇihitanti": "tính chất không mong cầu",
    "abhiññanti": "sự hiểu biết trực tiếp", "dandhābhiññanti": "sự hiểu biết trực tiếp chậm chạp",
    "adhipateyyanti": "làm yếu tố chủ đạo",
    "aññātāvī": "người đã hiểu biết trọn vẹn",
    # ---------------------------------------------------------------- results of the unwholesome
    "dukkhindriyaṃ": "năng lực khó chịu",
    "akusalassa": "bất thiện", "akusalassa kammassa": "nghiệp bất thiện",
    "kāyasamphassa": "sự tiếp xúc của thân", "samphassa": "sự tiếp xúc",
    # ---------------------------------------------------------------- functional minds
    "kammavipākā": "quả của nghiệp", "kammavipākaṃ": "quả của nghiệp",
    "kusalā nākusalā": "không phải thiện không phải bất thiện",     # neva kusalā nākusalā
    "kusalaṃ nākusalaṃ": "không phải thiện không phải bất thiện",
    "akusalaṃ": "bất thiện",
    "kiriyaṃ": "mang tính chức năng",
    "vihāraṃ": "an trú",                            # diṭṭhadhammasukhavihāraṃ «nhằm an trú trong hạnh phúc …»
    "jhānaṃ bhāveti": "tu tập tầng thiền",
    "rūpāvacaraṃ": "thuộc cõi hình sắc", "arūpāvacaraṃ": "thuộc cõi không hình sắc",
}
T05 = {**_p204.T, **ADD05}
assert not set(ADD05) & set(_p204.T), set(ADD05) & set(_p204.T)

OVERRIDES = {
    # ---- 2-05 headings / closing lines where a body-qualifier word is the heading noun
    "1-1-8-2-0": {"suññataṃ": "sự trống rỗng"},       # «Sự trống rỗng đơn thuần»
    "1-1-8-4-0": {"appaṇihitaṃ": "sự không mong cầu"},  # «Sự không mong cầu đơn thuần»
    "1-513": {"suññataṃ": "sự trống rỗng"},           # closing «Sự trống rỗng đơn thuần.»
    "1-1-10-2-0": {"Kiriyāmano": "ý" + GAP + "mang tính chức năng"},   # «Yếu tố ý thức mang tính chức năng»
    "1-1-10-3-0": {"Kiriyāmano": "ý" + GAP + "mang tính chức năng"},
    "1-573": {"Kiriyā mano": "ý" + GAP + "mang tính chức năng"},
    "1-575": {"Kiriyā mano": "ý" + GAP + "mang tính chức năng"},
    "1-559": {"dukkhaṃ": "sự đau khổ"},               # the dukkha heading «sự đau khổ là gì?» (2-04 1-416)
}
# «Tâm chức năng …» (headings and closing lines Sahetuka-/Rūpāvacara-/Arūpāvacarakiriyā): «tâm» is implied
for _b in ("1-1-10-4-0", "1-1-10-5-0", "1-1-10-6-0", "1-578", "1-582"):
    OVERRIDES.setdefault(_b, {})["kiriyā"] = "chức năng"
# sati occurs only inside «sự thiết lập tỉnh thức» (as 2-03 1-357 / 1-360)
for _b in ("1-528", "1-552"):
    OVERRIDES.setdefault(_b, {})["sati"] = SATI_BARE


def context05(bid, k, s):
    """2-05 rules for keys whose earlier-table value is another sense. None = no rule."""
    if k == "kiriyā":                                     # functional (2-03 table: «làm» of akiriyā)
        return "mang tính chức năng"
    if k == "sukha" and "vihāraṃ" in s:                    # diṭṭhadhammasukhavihāraṃ «an trú trong hạnh phúc»
        return "hạnh phúc"
    if k == "dukkha" and "dukkhindriyaṃ" in s:             # dukkhindriyaṃ «năng lực khó chịu»
        return "khó chịu"
    if k == "dukkhaṃ" and "dukkhā vedanā" in s:            # bodily feeling string «sự khó chịu nơi thân»
        return "khó chịu"
    return _p204.context(bid, k, s)


def resolver_for(part):
    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        s = set(lc(x) for x in kws)
        if part.startswith("2-05"):
            v = context05(bid, lc(kw), s)
            if v is not None:
                return v
            return ch2_value(kw, kws, T05)
        return resolve301(bid, kw, kws, s)
    return resolve


# ==================================================================== 3-01 (Rūpakaṇḍa: Uddesa, Mātikā, Ekakaniddesa)
# PRED301: the matter predicates, value form = the predicate without its frame («Có loại vật chất …»,
# «Vật chất nào … thì …», the predicate «là», the negation «không (phải là)» of a «na / no» item).
# Matrix items keep the MATRIX value (map_common_vi.py); 3-02 / 3-03 reuse this table as it stands.
PRED301 = {
    # ---- matrix predicates (same values as MATRIX, neuter singular)
    "upādā": MATRIX["upādā"],                               # phái sinh (no upādā «không phải là phái sinh»)
    "upādiṇṇaṃ": MATRIX["upādiṇṇa"],                         # do nghiệp tạo ra
    "upādiṇṇupādāniyaṃ": MATRIX["upādiṇṇupādāniyā"],
    "anupādiṇṇupādāniyaṃ": MATRIX["anupādiṇṇupādāniyā"],
    "upādāniyaṃ": MATRIX["upādāniyā"],                       # đối tượng của sự bám víu
    "sanidassanaṃ": MATRIX["sanidassana"], "anidassanaṃ": MATRIX["anidassana"],
    "anidassana": MATRIX["anidassana"],
    "sappaṭighaṃ": MATRIX["sappaṭighā"], "appaṭighaṃ": "không có tính va chạm",
    "anidassanaappaṭighaṃ": "không thấy được và không có tính va chạm",
    "samuṭṭhānaṃ": MATRIX["samuṭṭhāna"], "cittasamuṭṭhānaṃ": MATRIX["cittasamuṭṭhānā"],
    "cittasahabhu": MATRIX["cittasahabhuno"],
    "anuparivatti": MATRIX["anuparivattino"], "cittānuparivatti": MATRIX["cittānuparivattino"],
    "ajjhattikaṃ": MATRIX["ajjhattikā"], "bāhiraṃ": MATRIX["bāhirā"],
    # ---- new predicates of the matter chapter
    "indriyaṃ": "năng lực",                                  # là năng lực / không phải là năng lực
    "mahābhūtaṃ": "yếu tố cơ bản", "mahābhūtā": "yếu tố cơ bản",
    "bhūtaṃ": "yếu tố", "bhūtā": "yếu tố",                   # member: bhūta yếu tố + mahā cơ bản
    "viññatti": "sự biểu lộ",
    "kāyaviññatti": "sự biểu lộ bằng thân", "vacīviññatti": "sự biểu lộ bằng lời nói",
    "oḷārikaṃ": "ở dạng thô", "sukhumaṃ": "ở dạng vi tế",
    "ārammaṇaṃ": "đối tượng",                                # là đối tượng của … (anārammaṇaṃ: see OVERRIDES)
    # sense bases, elements, faculties
    "cakkhu": "mắt", "sota": "tai", "ghāna": "mũi", "jivhā": "lưỡi", "kāya": "thân",
    "cakkhāyatanaṃ": "lĩnh vực mắt", "sotāyatanaṃ": "lĩnh vực tai", "ghānāyatanaṃ": "lĩnh vực mũi",
    "jivhāyatanaṃ": "lĩnh vực lưỡi", "kāyāyatanaṃ": "lĩnh vực thân",
    "rūpāyatanaṃ": "lĩnh vực hình sắc", "saddāyatanaṃ": "lĩnh vực âm thanh",
    "gandhāyatanaṃ": "lĩnh vực mùi", "rasāyatanaṃ": "lĩnh vực vị",
    "phoṭṭhabbāyatanaṃ": "lĩnh vực vật xúc chạm",
    "dhammāyatana": "lĩnh vực đối tượng của ý",
    "cakkhudhātu": "yếu tố mắt", "sotadhātu": "yếu tố tai", "ghānadhātu": "yếu tố mũi",
    "jivhādhātu": "yếu tố lưỡi", "kāyadhātu": "yếu tố thân",
    "rūpadhātu": "yếu tố hình sắc", "saddadhātu": "yếu tố âm thanh", "gandhadhātu": "yếu tố mùi",
    "rasadhātu": "yếu tố vị", "phoṭṭhabbadhātu": "yếu tố vật xúc chạm",
    "pathavīdhātu": "yếu tố đất", "āpodhātu": "yếu tố nước", "tejodhātu": "yếu tố lửa",
    "vāyodhātu": "yếu tố gió", "ākāsadhātu": "yếu tố không gian",
    "itthi": "nữ tính", "purisa": "nam tính",
    "itthindriyaṃ": "năng lực nữ tính", "purisindriyaṃ": "năng lực nam tính",
    # «là chỗ dựa cho / là đối tượng của» X
    "cakkhusamphassassa": "sự tiếp xúc của mắt", "sotasamphassassa": "sự tiếp xúc của tai",
    "ghānasamphassassa": "sự tiếp xúc của mũi", "jivhāsamphassassa": "sự tiếp xúc của lưỡi",
    "kāyasamphassassa": "sự tiếp xúc của thân",
    "samphassajāya": "sinh từ sự tiếp xúc", "kāyasamphassajāya": "sinh từ sự tiếp xúc của thân",
    "vedanāya": "cảm giác", "samphassajāya vedanāya": "cảm giác sinh từ sự tiếp xúc",
    "saññāya": "tri giác", "cetanāya": "chủ ý",
    "cakkhuviññāṇassa": "thức qua mắt", "kāyaviññāṇassa": "thức qua thân",
    # qualities of matter (rūpassa X = «X của vật chất»)
    "lahutā": "sự nhẹ nhàng", "rūpassa lahutā": "sự nhẹ nhàng của vật chất",
    "mudutā": "sự mềm mại", "rūpassa mudutā": "sự mềm mại của vật chất",
    "kammaññatā": "sự dễ vận dụng", "rūpassa kammaññatā": "sự dễ vận dụng của vật chất",
    "rūpassa upacayo": "sự tăng trưởng của vật chất",
    "santati": "sự liên tục", "rūpassa santati": "sự liên tục của vật chất",
    "jaratā": "sự lão hóa", "rūpassa jaratā": "sự lão hóa của vật chất",
    "aniccatā": "tính vô thường", "rūpassa aniccatā": "tính vô thường của vật chất",
    "kabaḷīkāro": "thức ăn", "āhāro": "dưỡng chất",
    "kabaḷīkāro āhāro": "thức ăn trong vai trò dưỡng chất",
    # Ekaka list (^1-584): matrix items, without «là», negation of a fragment dropped
    "pahātabbaṃ": MATRIX["pahātabbā"], "sahagataṃ": "đi kèm",
    "pītisahagataṃ": MATRIX["pītisahagatā"], "sukhasahagataṃ": MATRIX["sukhasahagatā"],
    "upekkhāsahagataṃ": MATRIX["upekkhāsahagatā"],
    "asekkhaṃ": MATRIX["asekkhā"], "sekkha": MATRIX["sekkhā"],
    "saṅkhataṃ": MATRIX["saṅkhatā"], "saṃkilesikaṃ": MATRIX["saṃkilesikā"],
    "vippayuttaṃ": "không gắn liền", "cittavippayuttaṃ": MATRIX["cittavippayuttā"],
    "cetasikaṃ": MATRIX["cetasikā"],                         # of acetasikaṃ «không đồng hành với tâm»
    "sāsavaṃ": MATRIX["sāsavā"], "āsavaṃ": MATRIX["āsava"],
    "saṃyojaniyaṃ": MATRIX["saṃyojaniyā"], "ganthaniyaṃ": MATRIX["ganthaniyā"],
    "oghaniyaṃ": MATRIX["oghaniyā"], "yoganiyaṃ": MATRIX["yoganiyā"],
    "nīvaraṇiyaṃ": MATRIX["nīvaraṇiyā"], "parāmaṭṭhaṃ": MATRIX["parāmaṭṭhā"],
    "abyākataṃ": MATRIX["abyākatā"],
    "rūpāvacaraṃ": MATRIX["rūpāvacarā"], "arūpāvacaraṃ": MATRIX["arūpāvacarā"],
    "kāmāvacaraṃ": MATRIX["kāmāvacarā"], "avacaraṃ": MATRIX["avacarā"],
    "niyataṃ": MATRIX["niyatā"],                             # of aniyataṃ «không cố định»
    "niyyānikaṃ": MATRIX["niyyānikā"],                       # of aniyyānikaṃ
    "apariyāpannaṃ": "không nằm trong các cõi tồn tại",      # no apariyāpannaṃ «không thuộc về các hiện tượng …»
    "parittaṃ": MATRIX["paritta"], "lokiyaṃ": MATRIX["lokiyā"],
    "hetukaṃ": MATRIX["hetukā"], "gāmi": "dẫn đến",
    "uppannaṃ": MATRIX["uppannā"],                           # đã sinh khởi
    "aniccaṃ": "vô thường",                                  # là vô thường
    "jarā": "sự lão hóa", "abhibhūtaṃ": "bị" + GAP + "chế ngự",   # jarābhibhūtaṃ «bị sự lão hóa chế ngự»
    "viññeyyaṃ": "có thể được" + GAP + "nhận biết",          # «có thể được sáu loại thức nhận biết»
    "viññāṇehi": "loại thức",
    "upādāya": "phái sinh từ", "upādāya rūpaṃ": "vật chất phái sinh từ",
}
# -meva (^1-594): «chắc chắn» + the predicate; « … » where a negation of the item stands between
_MEVA_NEG = {"pahātabba": "pahātabbaṃ", "sahagata": "sahagataṃ", "upekkhāsahagata": "upekkhāsahagataṃ",
             "sukhasahagata": "sukhasahagataṃ", "pītisahagata": "pītisahagataṃ", "asekkha": "asekkhaṃ",
             "cetasika": "cetasikaṃ", "rūpāvacara": "rūpāvacaraṃ", "arūpāvacara": "arūpāvacaraṃ",
             "niyata": "niyataṃ", "niyyānika": "niyyānikaṃ", "ārammaṇa": "ārammaṇaṃ",
             "hetuka": "hetukaṃ", "apariyāpanna": "apariyāpannaṃ", "āsava": "āsavaṃ",
             "abhibhūta": "abhibhūtaṃ", "viññeyya": "viññeyyaṃ"}
_MEVA_POS = {"upādāniya": "upādāniyaṃ", "saṅkhata": "saṅkhataṃ", "saṃkilesika": "saṃkilesikaṃ",
             "vippayutta": "vippayuttaṃ", "cittavippayutta": "cittavippayuttaṃ",
             "saṃyojaniya": "saṃyojaniyaṃ", "oghaniya": "oghaniyaṃ", "nīvaraṇiya": "nīvaraṇiyaṃ",
             "ganthaniya": "ganthaniyaṃ", "yoganiya": "yoganiyaṃ", "sāsava": "sāsavaṃ",
             "parāmaṭṭha": "parāmaṭṭhaṃ", "kāmāvacara": "kāmāvacaraṃ", "avacara": "avacaraṃ",
             "lokiya": "lokiyaṃ"}
_LA = {"upādāniya", "saṃkilesika", "saṃyojaniya", "oghaniya", "nīvaraṇiya", "ganthaniya", "yoganiya",
       "sāsava"}                                             # «chắc chắn là đối tượng của …»
MEVA = {}
for _s, _k in _MEVA_POS.items():
    MEVA[_s + "meva"] = "chắc chắn " + ("là " if _s in _LA else "") + PRED301[_k]
for _s, _k in _MEVA_NEG.items():                         # «chắc chắn không (phải là / có) …»
    MEVA[_s + "meva"] = "chắc chắn" + GAP + PRED301[_k]
MEVA.update({
    "ārammaṇameva": "chắc chắn" + GAP + "có đối tượng",     # of anārammaṇameva «chắc chắn không có đối tượng»
    "abhibhūtameva": "chắc chắn bị" + GAP + "chế ngự",       # «chắc chắn bị sự lão hóa chế ngự»
    "viññeyyameva": "chắc chắn có thể được" + GAP + "nhận biết",
    "abyākatameva": "chắc chắn là không xác định về mặt đạo đức",
    "parittameva": "chắc chắn là hạn hẹp", "aniccameva": "chắc chắn là vô thường",
})

ADD301 = {
    **PRED301, **MEVA,
    # ---- headings and closing lines
    "rūpa": "vật chất", "rūpaṃ": "vật chất",                 # rūpa (matter); hình sắc in rūpāvacarā (1-583)
    "uddeso": "phần nêu đề mục", "vibhatti": "phân tích", "niddeso": "giải thích",
    "dukaṃ": "phân loại theo nhóm hai",                      # MATRIX «bộ đôi»; the heading words it so here
    "dasakaṃ": "phân loại theo nhóm mười", "ekādasakaṃ": "phân loại theo nhóm mười một",
    "dasa": "mười", "ekādasa": "mười một",
    "saṅgaho": "phân loại", "rūpasaṅgaho": "phân loại vật chất",
    "vidhena": "theo nhóm",                                  # <N>vidhena «theo nhóm <N>»
    "catubbidhena": "theo nhóm bốn", "chabbidhena": "theo nhóm sáu",
    "eva": "chắc chắn", "tattha": "ở đây",
    # ---- Uddesa (^1-583)
    "kiriyā": "mang tính chức năng",
    "asaṅkhatā ca dhātu": "yếu tố không do điều kiện tạo thành",
    # ---- lists
    "viññeyyaṃ rūpaṃ": "vật chất mà" + GAP + "có thể nhận biết",   # «vật chất mà mắt có thể nhận biết»
    "rūpaṃ sappaṭighaṃ": "vật chất có tính va chạm",
    "rūpaṃ cittasamuṭṭhānaṃ": "vật chất do tâm sinh ra",
    "rūpaṃ cittasahabhu": "vật chất cùng tồn tại với tâm",
    "rūpaṃ cittānuparivatti": "vật chất vận hành theo tâm",
    "sutaṃ": "được nghe", "mutaṃ": "được cảm nhận", "viññātaṃ": "được nhận biết",
    "samphassaṃ": "tiếp xúc",                                # «có loại tiếp xúc dễ chịu / khó chịu»
}

OVERRIDES.update({
    "1-583": {"rūpa": "hình sắc"},                           # rūpāvacarā «thuộc cõi hình sắc»
    "1-584": {"ārammaṇaṃ": "có đối tượng"},                  # of anārammaṇaṃ «không có đối tượng» (MATRIX ārammaṇā)
    "1-586": {"rūpaṃ sappaṭighaṃ": "vật chất" + GAP + "có tính va chạm"},   # «Vật chất nào có tính va chạm thì …»
    "1-588": {"viññeyyaṃ": "có thể nhận biết"},
    "1-589": {"viññeyyaṃ": "có thể nhận biết"},
    "1-590": {"viññeyyaṃ": "có thể nhận biết", "sukha": "dễ chịu", "dukkha": "khó chịu"},
})


def resolve301(bid, kw, kws, s):
    k = lc(kw)
    for table in (ADD301, MATRIX):
        if k in table:
            return table[k]
    return ch2_value(kw, kws, T05)


if __name__ == "__main__":
    for p in (sys.argv[1:] or PARTS):
        build_part(p, resolver_for(p))
        verify(p)
