"""Shared helpers and tables for the pi-2 (Vibhaṅga) Pāli->Vietnamese keyword maps (pi-2-vi-ai/mapper-vi/).

Importing this module writes nothing (no output file, no bytecode: sys.dont_write_bytecode is set before the
pi-1 modules are loaded, so nothing lands in the pi-1 __pycache__ either).

    import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
    from map_common_vi import *

Main pieces
- read_keywords(part) / read_vietnamese(part) / read_pali(part)    pi-2 paths (segments end with ^id)
- present(value, text)          the pi-1 presence check (literal, NFC, case-insensitive, word-bounded; " … " parts
                                in order, " / " alternatives; variant brackets removed)
- CORE, CH2, ch2_value, MATRIX, SATI_BARE, lc, NDE, GAP     re-exported from pi-1 map_common_vi.py (read-only)
- pi1_value(kw, kws)            the whole approved pi-1 resolver chain without its segment rules
                                (pi-1 map_5_vi.py: ADD5 -> 4-02/4-03 _val (ADD402, ADD401, MATRIX, RUPA, ADD301 ...)
                                -> ch2_value(T05)); KeyError if pi-1 has no value
- KH                            the pi-2 table settled on the sample (preamble, 1-khandhavibhango); later parts
                                extend it in their own script ({**KH, ...}), never here
- value(kw, kws, table=None)    table -> KH -> pi1_value
- pi1_map_values(kw)            Counter of the values the approved pi-1 Vietnamese map gives a keyword
- build_part(part, resolver)    writes <part>.mapped.md; stops on an unmapped keyword; refuses ", " in a value
- verify(part, allowed=None)    the brief's structural check + the presence check; `allowed` = {(id, kw): reason}
                                presence exceptions (printed with their reason, not counted as misses)
"""
import importlib.util
import pathlib
import sys
import unicodedata
from collections import Counter

sys.dont_write_bytecode = True

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
PI1_DIR = ROOT / "0-INBOX" / "temp" / "pipeline" / "pi-1-vi-ai" / "mapper-vi"
VI_DIR = ROOT / "AI_translation" / "vietnamese" / "pi-2-vietnamese-plain-zeroshot_split_chapters"
PI_DIR = ROOT / "AI_translation" / "pali" / "pi-2_split_chapters"
PI1_MAP = ROOT / "AI_translation" / "vietnamese" / "pi-1-keywords-by-reference-pali-vietnamese-plain.md"


# ---------------------------------------------------------------------------- pi-1 modules (read-only)
def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


P1 = _load("pi1_map_common_vi", PI1_DIR / "map_common_vi.py")

# The pi-1 part scripts do `from map_common_vi import ...` with the pi-1 folder on sys.path. This file has the same
# name, so the pi-1 module is put under that name while they load, then everything is restored.
_saved_mod = sys.modules.get("map_common_vi")
_saved_path = list(sys.path)
sys.modules["map_common_vi"] = P1
try:
    P1_5 = _load("pi1_map_5_vi", PI1_DIR / "map_5_vi.py")
finally:
    sys.path[:] = _saved_path
    if _saved_mod is not None:
        sys.modules["map_common_vi"] = _saved_mod
    else:
        sys.modules.pop("map_common_vi", None)

present, lc, NDE, GAP = P1.present, P1.lc, P1.NDE, P1.GAP
CORE, CH2, MATRIX, SATI_BARE, ch2_value = P1.CORE, P1.CH2, P1.MATRIX, P1.SATI_BARE, P1.ch2_value
ADD5, T05 = P1_5.ADD5, P1_5.T05


def pi1_value(kw, kws):
    """The approved pi-1 value of a keyword (tables only; pi-1 segment rules are not applied)."""
    k = lc(kw)
    if k in ADD5:
        return ADD5[k]
    try:
        return P1_5._p402._val(k)
    except KeyError:
        return ch2_value(kw, kws, T05)


# ---------------------------------------------------------------------------- reading (pi-2 paths)
def read_keywords(part):
    out = []
    for line in (HERE / f"{part}.keywords.md").read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        bid, rest = line.split("] ", 1)
        out.append((bid[1:], [k.strip() for k in rest.split(", ")]))
    return out


def read_vietnamese(part):
    return P1._segments(VI_DIR / f"{part}.md")


def read_pali(part):
    return P1._segments(PI_DIR / f"{part}.md")


_PI1_MAP_CACHE = {}


def pi1_map_values(kw):
    """Counter of the values the approved pi-1 Vietnamese keyword map gives `kw` (exact keyword)."""
    if not _PI1_MAP_CACHE:
        for line in PI1_MAP.read_text(encoding="utf-8").splitlines():
            if "] " not in line:
                continue
            for pair in line.split("] ", 1)[1].split(", "):
                if "=" in pair:
                    k, v = pair.split("=", 1)
                    _PI1_MAP_CACHE.setdefault(k, Counter())[v] += 1
    return _PI1_MAP_CACHE.get(kw, Counter())


# ---------------------------------------------------------------------------- the pi-2 table (sample)
_KX = "không xác định về mặt đạo đức"
_SAMP = "người đã chứng nhập"
_AGG = {"rūpa": "vật chất", "vedanā": "cảm giác", "saññā": "tri giác", "saṅkhāra": "tạo tác", "viññāṇa": "thức"}

KH = {
    # ---- preamble and headings
    "vibhaṅga": "Phân tích các hiện tượng", "vibhaṅgapāḷi": "Phân tích các hiện tượng", "pāḷi": NDE,
    "vibhaṅgo": "phân tích", "khandha": "khối",                     # Khandhavibhaṅgo «Phân tích các khối»
    "suttanta": "kinh", "bhājanīyaṃ": "phân tích", "abhidhamma": "Vi Diệu Pháp",
    "pañhā": "hỏi đáp", "pañhāpucchakaṃ": "phần hỏi đáp",          # «Phần hỏi đáp»
    "tikaṃ": "bộ ba", "dukaṃ": "bộ đôi", "niṭṭhito": "đã hoàn tất",
    # ---- aggregates (pi-1 khandha = khối; the matter aggregate = khối vật chất)
    "khandho": "khối", "khandhā": "khối", "khandhānaṃ": "khối",
    "rūpakkhandho": "khối vật chất", "vedanākkhandho": "khối cảm giác", "saññākkhandho": "khối tri giác",
    "saṅkhārakkhandho": "khối tạo tác", "viññāṇakkhandho": "khối thức",
    **_AGG,
    "rūpaṃ": "vật chất", "viññāṇaṃ": "thức", "saṅkhārā": "sự tạo tác", "vedanāhi": "cảm giác",
    "saññāhi": "tri giác",
    # ---- definition frames
    "tattha": "ở đây", "vuccati": "được gọi là", "vuccanti": "được gọi là",
    "yaṃ kiñci": "bất cứ … nào", "yā kāci": "bất cứ … nào", "ye keci": "bất cứ … nào",
    # «khi gom tất cả lại làm một và thu tóm lại»: gom = abhisaññūhitvā, tất cả lại làm một = tadekajjhaṃ
    "tadekajjhaṃ": "tất cả lại làm một", "abhisaññūhitvā": "gom",
    "abhisaṅkhipitvā": "thu tóm lại",
    # ---- time, self, coarse/subtle, inferior/superior
    "atītaṃ": "thuộc quá khứ", "anāgataṃ": "thuộc tương lai", "paccuppannaṃ": "thuộc hiện tại",
    "atītā": "thuộc quá khứ", "anāgatā": "thuộc tương lai", "paccuppannā": "thuộc hiện tại",
    "niruddhaṃ": "đã chấm dứt", "niruddhā": "đã chấm dứt", "vigataṃ": "đã mất đi", "vigatā": "đã mất đi",
    "vipariṇataṃ": "đã biến đổi", "vipariṇatā": "đã biến đổi",
    "abbhatthaṅgataṃ": "đã biến mất hoàn toàn", "abbhatthaṅgatā": "đã biến mất hoàn toàn",
    "uppajjitvā": "sau khi sinh khởi", "atītaṃsena": "phần thuộc quá khứ",
    "saṅgahitaṃ": "được gộp vào", "saṅgahitā": "được gộp vào",
    "atītaṃsena saṅgahitaṃ": "được gộp vào phần thuộc quá khứ",
    "atītaṃsena saṅgahitā": "được gộp vào phần thuộc quá khứ",
    "jātaṃ": "đã sinh ra", "jātā": "đã sinh ra", "nibbattaṃ": "đã phát sinh", "nibbattā": "đã phát sinh",
    "abhinibbattaṃ": "đã phát sinh rõ rệt", "abhinibbattā": "đã phát sinh rõ rệt",
    "pātubhūtaṃ": "đã hiện ra", "pātubhūtā": "đã hiện ra", "uppannaṃ": "đã sinh khởi", "uppannā": "đã sinh khởi",
    "uṭṭhitaṃ": "đã trỗi dậy", "uṭṭhitā": "đã trỗi dậy",
    "samuṭṭhitaṃ": "đã trỗi dậy trọn vẹn", "samuṭṭhitā": "đã trỗi dậy trọn vẹn",
    "ajjhattaṃ": "ở nơi bản thân", "paccattaṃ": "riêng từng người", "pāṭipuggalikaṃ": "thuộc về cá nhân",
    "pāṭipuggalikā": "thuộc về cá nhân", "parapuggalānaṃ": "người khác",   # «từng»: tesaṃ tesaṃ (no keyword)
    "oḷārikaṃ": "ở dạng thô", "oḷārikā": "ở dạng thô", "sukhumaṃ": "ở dạng vi tế", "sukhumā": "ở dạng vi tế",
    "hīnaṃ": "thấp kém", "hīnā": "thấp kém", "paṇītaṃ": "ưu việt", "paṇītā": "ưu việt",
    "upādāyupādāya": "so với", "daṭṭhabbaṃ": "nên được xem là", "daṭṭhabbā": "nên được xem là",
    "samāpannassa": _SAMP,
    # ---- matter (pi-1 values)
    "upādāya": "phái sinh từ", "upādāyarūpaṃ": "vật chất phái sinh từ", "bhūtā": "yếu tố",
    "mahābhūtā": "yếu tố cơ bản",
    # ---- feelings in the comparison paragraphs
    "sukhā": "dễ chịu", "dukkhā": "khó chịu", "adukkhamasukhā": "không khó chịu cũng không dễ chịu",
    "sukhā vedanā": "cảm giác dễ chịu", "dukkhā vedanā": "cảm giác khó chịu",
    "sukhadukkhā": "dễ chịu và khó chịu", "sukhadukkhāhi": "dễ chịu và khó chịu",
    "dukkhāhi vedanāhi": "cảm giác" + GAP + "khó chịu",                  # of sukhadukkhāhi «các cảm giác dễ chịu và khó chịu»
    "kusalā": "thiện", "akusalā": "bất thiện", "abyākatā": _KX,
    "kusalaṃ": "thiện", "akusalaṃ": "bất thiện", "abyākataṃ": _KX,
    "kusalābyākatā": "thiện và " + _KX, "akusalābyākatā": "bất thiện và " + _KX,
    "kusalākusalā": "thiện và bất thiện",
    "sāsavā": "là đối tượng của ô nhiễm", "anāsavā": "không phải là đối tượng của ô nhiễm",
    "sāsavaṃ": "là đối tượng của ô nhiễm", "anāsavaṃ": "không phải là đối tượng của ô nhiễm",
    "āsavā": "ô nhiễm", "āsavaṃ": "ô nhiễm",
    "sampayuttā": "gắn liền", "sampayuttaṃ": "gắn liền",
    "vedanāya": "cảm giác", "sukhāya": "dễ chịu", "dukkhāya": "khó chịu",
    "adukkhamasukhāya": "không khó chịu cũng không dễ chịu",
    "sukhāya vedanāya": "cảm giác dễ chịu", "dukkhāya vedanāya": "cảm giác khó chịu",
    # ---- classification frames (Abhidhammabhājanīya): «Phân loại khối X theo nhóm N»
    "vidhena": "theo nhóm",
    "ekavidhena": "theo nhóm một", "duvidhena": "theo nhóm hai", "tividhena": "theo nhóm ba",
    "catubbidhena": "theo nhóm bốn", "pañcavidhena": "theo nhóm năm", "chabbidhena": "theo nhóm sáu",
    "sattavidhena": "theo nhóm bảy", "aṭṭhavidhena": "theo nhóm tám", "navavidhena": "theo nhóm chín",
    "dasavidhena": "theo nhóm mười", "ekādasavidhena": "theo nhóm mười một",
    "catuvīsatividhena": "theo nhóm hai mươi bốn", "tiṃsavidhena": "theo nhóm ba mươi",
    "tiṃsatividhena": "theo nhóm ba mươi", "bahuvidhena": "theo nhiều nhóm",
    "duka": "bộ đôi", "tika": "bộ ba", "mūlakaṃ": "dựa trên",
    "ubhato": "cả hai phía", "vaḍḍhakaṃ": "mở rộng",
}
for _x, _v in (("rūpa", "vật chất"), ("vedanā", "cảm giác"), ("saññā", "tri giác"), ("saṅkhāra", "tạo tác"),
               ("viññāṇa", "thức")):
    KH[f"dasavidhena {_x}kkhandho"] = f"khối {_v} theo nhóm mười"


# ---- predicates of the «có loại X» / «đôi khi X» lines (Abhidhammabhājanīya, Pañhāpucchaka). Pāli gives them in
# the masculine / feminine / neuter / plural of the subject; Vietnamese has one form. Value form as pi-1 MATRIX:
# no frame («có loại», «đôi khi», predicate «là»); «X-niyo» bare = «đối tượng của X» (leading «là» dropped).
def _forms(stem, v, endings=("o", "ā", "aṃ", "e")):
    for e in endings:
        KH[stem + e] = v


_PRED = {
    # stem (without the ending) -> value
    "kusal": "thiện", "akusal": "bất thiện", "abyākat": _KX,
    "sahetuk": "có gốc rễ", "ahetuk": "không có gốc rễ", "hetuk": "có gốc rễ",
    "hetusampayutt": "gắn liền với gốc rễ", "hetuvippayutt": "không gắn liền với gốc rễ",
    "sampayutt": "gắn liền", "vippayutt": "không gắn liền",
    "phassasampayutt": "gắn liền với sự tiếp xúc", "cittasampayutt": "gắn liền với tâm",
    "sukhindriyasampayutt": "gắn liền với năng lực dễ chịu",
    "kāmāvacar": "thuộc cõi dục lạc", "rūpāvacar": "thuộc cõi hình sắc", "arūpāvacar": "thuộc cõi không hình sắc",
    "āvacar": "thuộc cõi", "pariyāpann": "nằm trong các cõi tồn tại",
    "apariyāpann": "không nằm trong các cõi tồn tại",
    "vipāk": "quả của nghiệp", "vipākadhammadhamm": "có khả năng sinh ra quả",
    "upādinnupādāniy": "do nghiệp tạo ra và là đối tượng của sự bám víu",
    "anupādinnupādāniy": "không do nghiệp tạo ra nhưng là đối tượng của sự bám víu",
    "upādinn": "do nghiệp tạo ra", "anupādinn": "không do nghiệp tạo ra",
    "saṃkiliṭṭhasaṃkilesik": "bị phiền não làm vẩn đục và là đối tượng của phiền não",
    "asaṃkiliṭṭhasaṃkilesik": "không bị phiền não làm vẩn đục nhưng là đối tượng của phiền não",
    "asaṃkiliṭṭhaasaṃkilesik": "không bị phiền não làm vẩn đục và không phải là đối tượng của phiền não",
    "saṃkiliṭṭh": "bị phiền não làm vẩn đục", "asaṃkiliṭṭh": "không bị phiền não làm vẩn đục",
    "savitakkasavicār": "có sự hướng tâm và sự duy trì tâm",
    "avitakkavicāramatt": "không có sự hướng tâm chỉ có sự duy trì tâm",       # comma dropped
    "avitakkaavicār": "không có sự hướng tâm cũng không có sự duy trì tâm",
    "savitakk": "có sự hướng tâm", "avitakk": "không có sự hướng tâm",
    "savicār": "có sự duy trì tâm", "avicār": "không có sự duy trì tâm",
    "vitakk": "sự hướng tâm", "vicār": "sự duy trì tâm",
    "pītisahagat": "có sự hân hoan đi kèm", "sukhasahagat": "có hạnh phúc đi kèm",
    "upekkhāsahagat": "có sự bình thản đi kèm", "sahagat": "đi kèm",
    "pahātabb": "cần dứt bỏ", "pahātabbahetuk": "có gốc rễ cần dứt bỏ",
    "sekkh": "thuộc về người còn đang tu học", "asekkh": "thuộc về người đã hoàn tất tu học",
    "paritt": "hạn hẹp", "mahaggat": "rộng lớn", "appamāṇ": "không thể đo lường",
    "parittārammaṇ": "có đối tượng hạn hẹp", "mahaggatārammaṇ": "có đối tượng rộng lớn",
    "appamāṇārammaṇ": "có đối tượng không thể đo lường",
    "hīn": "thấp kém", "majjhim": "trung bình", "paṇīt": "ưu việt",
    "micchattaniyat": "cố định theo hướng sai lầm", "sammattaniyat": "cố định theo hướng đúng đắn",
    "niyat": "cố định", "aniyat": "không cố định",
    "uppann": "đã sinh khởi", "anuppann": "chưa sinh khởi",
    "atīt": "thuộc quá khứ", "anāgat": "thuộc tương lai", "paccuppann": "thuộc hiện tại",
    "atītārammaṇ": "có đối tượng thuộc quá khứ", "anāgatārammaṇ": "có đối tượng thuộc tương lai",
    "paccuppannārammaṇ": "có đối tượng thuộc hiện tại",
    "ajjhatt": "ở nơi bản thân", "bahiddh": "ở bên ngoài bản thân",
    "ajjhattabahiddh": "ở nơi bản thân và ở bên ngoài bản thân",
    "ajjhattārammaṇ": "có đối tượng ở nơi bản thân", "bahiddhārammaṇ": "có đối tượng ở bên ngoài bản thân",
    "ajjhattabahiddhārammaṇ": "có đối tượng ở nơi bản thân và ở bên ngoài bản thân",
    "anārammaṇ": "không có đối tượng", "sārammaṇ": "có đối tượng",
    "lokiy": "thuộc thế gian", "lokuttar": "vượt thế gian",
    "sauttar": "còn có điều cao hơn", "anuttar": "không có điều gì cao hơn",
    "saraṇ": "có xung đột", "araṇ": "không có xung đột",
    "niyyānik": "dẫn đến giải thoát", "aniyyānik": "không dẫn đến giải thoát",
    "parāmaṭṭh": "bị sự hiểu sai lệch nắm giữ", "aparāmaṭṭh": "không bị sự hiểu sai lệch nắm giữ",
    "saṃkilesik": "đối tượng của phiền não", "asaṃkilesik": "không phải là đối tượng của phiền não",
    "sappītik": "có sự hân hoan", "appītik": "không có sự hân hoan",
    "sanidassanasappaṭigh": "thấy được và có tính va chạm",
    "anidassanasappaṭigh": "không thấy được nhưng có tính va chạm",
    "anidassanaappaṭigh": "không thấy được và không có tính va chạm",
    "sanidassan": "thấy được", "anidassan": "không thấy được",
    "sappaṭigh": "có tính va chạm", "appaṭigh": "không có tính va chạm",
    "ajjhattik": "thuộc phần bên trong", "bāhir": "thuộc phần bên ngoài",
    "cittasaṃsaṭṭh": "hòa lẫn với tâm", "saṃsaṭṭh": "hòa lẫn",
}
for _s, _v in _PRED.items():
    _forms(_s, _v)

# defilement clusters (pi-1 MATRIX nouns)
for _stem, _noun, _niya in (("āsava", "ô nhiễm", "sāsava"), ("saṃyojana", "xiềng xích", "saṃyojaniya"),
                            ("gantha", "nút thắt", "ganthaniya"), ("ogha", "dòng lũ", "oghaniya"),
                            ("yoga", "ách", "yoganiya"), ("nīvaraṇa", "chướng ngại", "nīvaraṇiya"),
                            ("upādāna", "sự bám víu", "upādāniya"), ("kilesa", "phiền não", "saṃkilesika"),
                            ("parāmāsa", "sự hiểu sai lệch", "parāmaṭṭha")):
    _neg = {"sāsava": "anāsava", "saṃkilesika": "asaṃkilesika", "parāmaṭṭha": "aparāmaṭṭha",
            "upādāniya": "anupādāniya"}.get(_niya, ("an" if _niya[0] in "āaeiouō" else "a") + _niya)
    if _stem == "parāmāsa":
        _pos, _negv = "bị sự hiểu sai lệch nắm giữ", "không bị sự hiểu sai lệch nắm giữ"
        _join_pos, _join_neg = f"nhưng {_pos}", f"và {_negv}"
    else:
        _pos, _negv = f"đối tượng của {_noun}", f"không phải là đối tượng của {_noun}"
        _join_pos, _join_neg = f"nhưng là {_pos}", f"và {_negv}"
    KH[_stem] = _noun
    _forms(_niya[:-1], _pos)                                   # sāsavo / sāsavā / sāsavaṃ
    _forms(_neg[:-1], _negv)
    _forms(f"{_stem}sampayutt", f"gắn liền với {_noun}")
    _forms(f"{_stem}vippayutt", f"không gắn liền với {_noun}")
    _forms(f"{_stem}vippayutta{_niya[:-1]}", f"không gắn liền với {_noun} {_join_pos}")
    _forms(f"{_stem}vippayutta{_neg[:-1]}", f"không gắn liền với {_noun} {_join_neg}")

KH.update({
    "hetu": "gốc rễ", "hetū": "gốc rễ", "āsavo": "ô nhiễm", "āsavā": "ô nhiễm",
    "phassa": "sự tiếp xúc", "samphassa": "sự tiếp xúc", "samphassajā": "sinh từ sự tiếp xúc",
    "paccayā": "do … làm điều kiện",                                   # «do sự tiếp xúc của mắt làm điều kiện»
    "ācaya": "sự tích lũy", "apacaya": "sự giảm trừ", "āpacaya": "sự giảm trừ",
    "ācayagāmī": "dẫn đến sự tích lũy", "apacayagāmī": "dẫn đến sự giảm trừ", "gāmī": "dẫn đến",
    "ācayagāmino": "dẫn đến sự tích lũy", "apacayagāmino": "dẫn đến sự giảm trừ",
    "uppādī": "sẽ sinh khởi", "uppādino": "sẽ sinh khởi",
    "ādhipati": "lấy … làm yếu tố chủ đạo", "ādhipatino": "lấy … làm yếu tố chủ đạo",
    "magga": "con đường", "micchatta": "hướng sai lầm", "sammatta": "hướng đúng đắn",
    "dassanena": "sự thấy chân lý", "bhāvanāya": "sự tu tập",
    "kenaci": "một loại thức nào đó", "viññeyyo": "có thể nhận biết", "viññeyyā": "có thể nhận biết",
    "kenaci viññeyyo": "một loại thức nào đó có thể nhận biết",
    "kenaci na viññeyyo": "một loại thức nào đó không thể nhận biết",
    "uttaro": "vượt", "uttarā": "vượt",                                # member of lokuttaro (pi-1 uttarā)
    "pīti": "sự hân hoan", "sukha": "hạnh phúc", "upekkhā": "sự bình thản",
    "na pītisahagato": "không có sự hân hoan đi kèm", "na kāmāvacaro": "không thuộc cõi dục lạc",
    "siyā": "đôi khi", "na": "không", "vattabbo": "nên nói", "vattabbā": "nên nói",
    # sense-contact and consciousness strings
    "cakkhusamphassa": "sự tiếp xúc của mắt", "sotasamphassa": "sự tiếp xúc của tai",
    "ghānasamphassa": "sự tiếp xúc của mũi", "jivhāsamphassa": "sự tiếp xúc của lưỡi",
    "kāyasamphassa": "sự tiếp xúc của thân", "manosamphassa": "sự tiếp xúc của ý",
    "cakkhusamphassajā": "sinh từ sự tiếp xúc của mắt", "sotasamphassajā": "sinh từ sự tiếp xúc của tai",
    "ghānasamphassajā": "sinh từ sự tiếp xúc của mũi", "jivhāsamphassajā": "sinh từ sự tiếp xúc của lưỡi",
    "kāyasamphassajā": "sinh từ sự tiếp xúc của thân", "manosamphassajā": "sinh từ sự tiếp xúc của ý",
    "paṭighasamphassa": "sự tiếp xúc có va chạm", "paṭighasamphassajā": "sinh từ sự tiếp xúc có va chạm",
    "adhivacanasamphassa": "sự tiếp xúc qua tên gọi",
    "adhivacanasamphassajā": "sinh từ sự tiếp xúc qua tên gọi",
    "cakkhuviññāṇaṃ": "thức qua mắt", "sotaviññāṇaṃ": "thức qua tai", "ghānaviññāṇaṃ": "thức qua mũi",
    "jivhāviññāṇaṃ": "thức qua lưỡi", "kāyaviññāṇaṃ": "thức qua thân", "manoviññāṇaṃ": "ý thức",
    "mano": "ý", "manodhātu": "yếu tố ý", "manoviññāṇa": "ý thức", "manoviññāṇadhātu": "yếu tố ý thức",
    "dhātu": "yếu tố", "viññāṇadhātu": "yếu tố" + GAP + "thức",       # member of manoviññāṇadhātu-
    "indriyaṃ": "năng lực", "indriya": "năng lực",
    "sukhindriyaṃ": "năng lực dễ chịu", "dukkhindriyaṃ": "năng lực khó chịu",
    "somanassindriyaṃ": "năng lực niềm vui", "domanassindriyaṃ": "năng lực nỗi buồn",
    "upekkhindriyaṃ": "năng lực bình thản", "sukhindriya": "năng lực dễ chịu",
    "dukkhindriya": "năng lực khó chịu", "somanassindriya": "năng lực niềm vui",
    "domanassindriya": "năng lực nỗi buồn", "upekkhindriya": "năng lực bình thản",
    "cetanā": "chủ ý", "citta": "tâm", "cittaṃ": "tâm",
})
for _org, _v in (("cakkhu", "mắt"), ("sota", "tai"), ("ghāna", "mũi"), ("jivhā", "lưỡi"), ("kāya", "thân"),
                 ("mano", "ý")):
    for _n, _nv in (("vedanā", "cảm giác"), ("saññā", "tri giác"), ("cetanā", "chủ ý")):
        KH[f"{_org}samphassajā {_n}"] = f"{_nv} sinh từ sự tiếp xúc của {_v}"


KH.update({
    # ---- Suttantabhājanīya: the hīna / paṇīta and near / far words
    "uññātaṃ": "bị coi thường", "avaññātaṃ": "bị xem nhẹ", "hīḷitaṃ": "bị chê bai", "paribhūtaṃ": "bị khinh miệt",
    "acittīkataṃ": "không được quý trọng", "cittīkataṃ": "được quý trọng",
    "hīnamataṃ": "được xem là thấp kém", "paṇītamataṃ": "được xem là ưu việt",
    "hīnasammataṃ": "được công nhận là thấp kém", "paṇītasammataṃ": "được công nhận là ưu việt",
    "iṭṭhaṃ": "đáng mong muốn", "kantaṃ": "đáng yêu mến", "manāpaṃ": "đáng ưa thích",
    "aniṭṭhaṃ": "không đáng mong muốn", "akantaṃ": "không đáng yêu mến", "amanāpaṃ": "không đáng ưa thích",
    "rūpā": "hình sắc", "saddā": "âm thanh", "gandhā": "mùi", "rasā": "vị", "phoṭṭhabbā": "vật xúc chạm",
    "āsanne": "gần kề", "upakaṭṭhe": "cận kề", "dūre": "ở xa", "santike": "ở gần",
    "yaṃ vā panaññampi": "hoặc" + GAP + "bất cứ" + GAP + "nào khác",   # «hoặc còn có bất cứ vật chất nào khác»
    "āyatanaṃ": "lĩnh vực",                                              # member: cakkhāyatanaṃ «lĩnh vực mắt»
    "cakkhāyatanaṃ": "lĩnh vực mắt", "phoṭṭhabbāyatanaṃ": "lĩnh vực vật xúc chạm",
    "kabaḷīkāro": "thức ăn", "āhāro": "dưỡng chất", "kabaḷīkāro āhāro": "thức ăn trong vai trò dưỡng chất",
    # ---- the ekaka list of matter (pi-1 ^1-584 values; the negation of a na / no item belongs to the item)
    "jarābhibhūtaṃ": "bị sự lão hóa chế ngự", "ābhibhūtaṃ": "bị" + GAP + "chế ngự", "abhibhūtaṃ": "bị" + GAP + "chế ngự",
    "acetasikaṃ": "không phải là yếu tố đồng hành với tâm", "cetasikā": "yếu tố đồng hành với tâm",
    "mattaṃ": "chỉ có", "mattā": "chỉ có", "matto": "chỉ có",            # of avitakkavicāramatta-
    "saha": "cùng", "sahabhu": "cùng tồn tại", "sahabhuno": "cùng tồn tại", "sahabhū": "cùng tồn tại",
    "ānuparivatti": "vận hành theo", "ānuparivattino": "vận hành theo", "anuparivatti": "vận hành theo",
    "sappaccayaṃ": "có điều kiện", "sappaccayā": "có điều kiện", "saṅkhataṃ": "do điều kiện tạo thành",
    "saṅkhatā": "do điều kiện tạo thành",
    "āsekkhaṃ": "thuộc về người đã hoàn tất tu học",                    # of nevasekkhanāsekkhaṃ
    "samphassaṃ": "tiếp xúc",                                            # «có loại khi tiếp xúc thì dễ chịu»
    "cakkhundriyaṃ": "năng lực mắt", "sotindriyaṃ": "năng lực tai", "ghānindriyaṃ": "năng lực mũi",
    "jivhindriyaṃ": "năng lực lưỡi", "kāyindriyaṃ": "năng lực thân",
    "cakkhuviññeyyaṃ": "mắt có thể nhận biết", "sotaviññeyyaṃ": "tai có thể nhận biết",   # «vật chất mà X có thể…»
    "ghānaviññeyyaṃ": "mũi có thể nhận biết", "jivhāviññeyyaṃ": "lưỡi có thể nhận biết",
    "kāyaviññeyyaṃ": "thân có thể nhận biết", "manoviññeyyaṃ": "ý có thể nhận biết",
    "vibhattaṃ": "đã phân tích",                                         # (Yathā rūpakaṇḍe vibhattaṃ …)
    "tike": "bộ ba", "tikā": "bộ ba", "vitthāro": "đã được trình bày chi tiết",   # (Yathā kusalattike vitthāro …)
    "arūpā": "phi vật chất",                                             # «Bốn khối phi vật chất»
    "cittaṃ": "tâm",
    "viññeyyaṃ rūpaṃ": "vật chất mà" + GAP + "có thể nhận biết",        # pi-1 3-01 ^1-588
    "vuccanti saṅkhārā": "được gọi là các sự tạo tác",                    # «đó được gọi là các sự tạo tác …»
    "sampayuttāhi": "gắn liền", "kusalābyākatāhi": "thiện và " + _KX, "akusalābyākatāhi": "bất thiện và " + _KX,
    "kusalākusalāhi": "thiện và bất thiện",
    "ābyākatāhi saññāhi": "tri giác" + GAP + _KX,                          # fragment of kusalābyākatāhi saññāhi
    "ābyākatāhi vedanāhi": "cảm giác" + GAP + _KX,
    # ---- Pañhāpucchaka
    "khandhā siyā": "khối đôi khi",
    "vedanāya sampayuttā": "gắn liền với cảm giác",
})
for _e in ("o", "ā", "aṃ"):
    KH[f"vedanāya sampayutt{_e}"] = "gắn liền với cảm giác"
    KH[f"dukkhāya vedanāya sampayutt{_e}"] = "gắn liền với cảm giác khó chịu"
    KH[f"sukhāya vedanāya sampayutt{_e}"] = "gắn liền với cảm giác dễ chịu"
    KH[f"adukkhamasukhāya vedanāya sampayutt{_e}"] = "gắn liền với cảm giác không khó chịu cũng không dễ chịu"

# «X ceva Y-sampayutto» = «vừa là X vừa gắn liền với X» (as pi-1 «vừa là X vừa …»)
for _stem, _n, _sg, _pl in (("hetu", "gốc rễ", "hetu ceva", "hetū ceva"),
                            ("āsava", "ô nhiễm", "āsavo ceva", "āsavā ceva"),
                            ("saṃyojana", "xiềng xích", "saṃyojanañceva", "saṃyojanā ceva"),
                            ("gantha", "nút thắt", "gantho ceva", "ganthā ceva"),
                            ("ogha", "dòng lũ", "ogho ceva", "oghā ceva"),
                            ("yoga", "ách", "yogo ceva", "yogā ceva"),
                            ("nīvaraṇa", "chướng ngại", "nīvaraṇañceva", "nīvaraṇā ceva"),
                            ("upādāna", "sự bám víu", "upādānañceva", "upādānā ceva"),
                            ("kilesa", "phiền não", "kileso ceva", "kilesā ceva")):
    KH[f"{_sg} {_stem}sampayutto"] = f"vừa là {_n} vừa gắn liền với {_n}"
    KH[f"{_pl} {_stem}sampayuttā"] = f"vừa là {_n} vừa gắn liền với {_n}"

# noun + attribute keywords («vedanā atītā», «Sāsavā saññā», «rūpaṃ oḷārikaṃ» …): «<noun> <attribute>» as the
# text writes it (attribute after the noun; an inner «là» kept: «cảm giác là đối tượng của ô nhiễm»)
NOUNS = {"vedanā": "cảm giác", "vedanāhi": "cảm giác", "saññā": "tri giác", "saññāhi": "tri giác",
         "saṅkhārā": "sự tạo tác", "viññāṇaṃ": "thức", "rūpaṃ": "vật chất"}
_IN_PHRASE = {"sāsav": "là đối tượng của ô nhiễm"}


def _attr(word, table=None):
    for stem, v in _IN_PHRASE.items():
        if word.startswith(stem) and len(word) - len(stem) <= 3:
            return v
    if table and word in table:
        return table[word]
    if word in KH:
        return KH[word]
    try:
        return pi1_value(word, [word])
    except KeyError:
        return None


def noun_attr(k, table=None, text=None):
    """«<noun> <attr>» / «<attr> <noun>» -> «<noun vi> <attr vi>» (with " … " between them where the segment `text`
    does not have them contiguous, e.g. «cảm giác thấp kém và ưu việt»), or None."""
    parts = k.split(" ")
    if len(parts) != 2:
        return None
    a, b = parts
    if a in NOUNS and b not in NOUNS:
        n, at = NOUNS[a], _attr(b, table)
    elif b in NOUNS and a not in NOUNS:
        n, at = NOUNS[b], _attr(a, table)
    else:
        return None
    if at is None:
        return None
    v = f"{n} {at}"
    if text is not None and not present(v, text):
        v = n + GAP + at
    return v


KHANDHA_NAMES = {"rūpakkhandho": "khối vật chất", "vedanākkhandho": "khối cảm giác", "saññākkhandho": "khối tri giác",
                 "saṅkhārakkhandho": "khối tạo tác", "viññāṇakkhandho": "khối thức", "khandhā": "khối"}


def value(kw, kws, table=None, text=None):
    """table -> KH -> «vuccati(/vuccanti) X» -> noun + attribute -> «<aggregate> <predicate>» -> pi-1 chain.
    `text` (the segment's Vietnamese) only decides contiguous vs « … » in the noun + attribute rule."""
    k = lc(kw)
    if table and k in table:
        return table[k]
    if k in KH:
        return KH[k]
    for frame in ("vuccati ", "vuccanti "):
        if k.startswith(frame):
            return "được gọi là " + value(k[len(frame):], kws, table, text)
    v = noun_attr(k, table, text)
    if v is not None:
        return v
    head, _, rest = k.partition(" ")
    if head in KHANDHA_NAMES and rest:
        return KHANDHA_NAMES[head] + " " + value(rest, kws, table, text)
    return pi1_value(kw, kws)


# ---------------------------------------------------------------------------- build and verify
def build_part(part, resolver):
    """resolver(bid, kw, kws) -> Vietnamese value. Stops on an unmapped keyword."""
    lines, missing = [], []
    for bid, kws in read_keywords(part):
        pairs = []
        for kw in kws:
            try:
                v = resolver(bid, kw, kws)
            except KeyError:
                missing.append((bid, kw))
                v = "???"
            v = unicodedata.normalize("NFC", v)
            assert ", " not in v, (bid, kw, v)
            pairs.append(f"{kw}={v}")
        lines.append(f"[{bid}] " + ", ".join(pairs))
    if missing:
        raise SystemExit(f"{part}: unmapped keywords: {missing}")
    (HERE / f"{part}.mapped.md").write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    return len(lines)


def verify(part, allowed=None, show=50):
    allowed = allowed or {}
    a = [l.split("] ", 1) for l in (HERE / f"{part}.keywords.md").read_text(encoding="utf-8").splitlines()]
    b = [l.split("] ", 1) for l in (HERE / f"{part}.mapped.md").read_text(encoding="utf-8").splitlines()]
    assert [x[0] for x in a] == [x[0] for x in b]
    bad = [i for (i, x), (_, y) in zip(a, b)
           if [k.strip() for k in x.split(", ")] != [k.split("=", 1)[0] for k in y.split(", ")]]
    vi = read_vietnamese(part)
    nde, miss, exc = 0, [], []
    for bid, rest in b:
        bid = bid[1:]
        text = vi.get(bid)
        for pair in rest.split(", "):
            kw, v = pair.split("=", 1)
            if v == NDE:
                nde += 1
            elif text is None or not present(v, text):
                (exc if (bid, kw) in allowed else miss).append((bid, kw, v))
    print(part, "lines", len(a), "bad", bad, "| no-direct-equivalent", nde, "| presence misses", len(miss),
          "| listed exceptions", len(exc))
    for m in miss[:show]:
        print("   MISS", *m)
    for e in exc:
        print("   EXCEPTION", *e, "--", allowed[(e[0], e[1])])
    return bad, nde, miss
