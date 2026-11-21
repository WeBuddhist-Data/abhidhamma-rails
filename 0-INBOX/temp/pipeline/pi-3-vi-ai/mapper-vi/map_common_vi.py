"""Shared helpers and tables for the pi-3 (Dhātukathā) Pāli->Vietnamese keyword maps (pi-3-vi-ai/mapper-vi/).

Importing this module writes nothing (sys.dont_write_bytecode is set before the pi-2 / pi-1 modules are loaded, so no
bytecode lands in their folders, and none of their build functions is called).

    import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
    from map_common_vi import *

Main pieces
- read_keywords(part) / read_vietnamese(part) / read_pali(part)    pi-3 paths (segments end with ^id)
- present(value, text)        the pi-1 presence check (re-exported through pi-2: literal, NFC, case-insensitive,
                              word-bounded; " … " parts in order, " / " alternatives (all present); variant brackets
                              removed first)
- CORE, MATRIX, SATI_BARE, lc, NDE, GAP, pi1_value, pi1_map_values    re-exported from pi-2 map_common_vi.py
- pi2_value(kw, kws, text)    the whole approved pi-2 table chain without its segment rules (pi-2 map_18_vi.py
                              _base_value: T18 -> T23 -> T17 … T45 -> KH -> the pi-1 chain); KeyError if none
- pi2_map_values(kw)          Counter of the values the approved pi-2 Vietnamese map gives a keyword
- KD                          the pi-3 table settled on the sample (preamble, 1-uddeso, 2-pathamanayo); later parts
                              extend it in their own script ({**KD, ...}), never here
- value(kw, kws, table=None, text=None)
                              table -> KD -> segment rules of the pi-3 frame (context3) -> " / " alternatives ->
                              counts -> «X saṅgahito» -> «X dhammā» -> pi2_value
- build_part(part, resolver)  writes <part>.mapped.md; stops on an unmapped keyword; refuses ", " in a value
- verify(part, allowed=None)  the brief's structural check + the presence check; `allowed` = {(id, kw): reason}
- prior_hashes()              sha256 of every pi-1 / pi-2 *.mapped.md (check_parts_vi.py compares before / after)
"""
import hashlib
import importlib.util
import pathlib
import re
import sys
import unicodedata
from collections import Counter

sys.dont_write_bytecode = True

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
PIPE = ROOT / "0-INBOX" / "temp" / "pipeline"
PI1_DIR = PIPE / "pi-1-vi-ai" / "mapper-vi"
PI2_DIR = PIPE / "pi-2-vi-ai" / "mapper-vi"
VI_DIR = ROOT / "AI_translation" / "vietnamese" / "pi-3-vietnamese-plain-zeroshot_split_chapters"
PI_DIR = ROOT / "AI_translation" / "pali" / "pi-3_split_chapters"
PI2_MAP = ROOT / "AI_translation" / "vietnamese" / "pi-2-keywords-by-reference-pali-vietnamese-plain.md"


def prior_hashes():
    """sha256 of every pi-1 / pi-2 mapped file (the approved outputs this module must never rewrite)."""
    out = {}
    for d in (PI1_DIR, PI2_DIR):
        for f in sorted(d.glob("*.mapped.md")):
            out[str(f)] = hashlib.sha256(f.read_bytes()).hexdigest()
    return out


# ---------------------------------------------------------------------------- pi-2 / pi-1 modules (read-only)
def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


P2 = _load("pi2_map_common_vi", PI2_DIR / "map_common_vi.py")

# The pi-2 part scripts do `from map_common_vi import ...` with the pi-2 folder on sys.path. This file has the same
# name, so the pi-2 module is put under that name while they load, then everything is restored.
_saved_mod = sys.modules.get("map_common_vi")
_saved_path = list(sys.path)
sys.modules["map_common_vi"] = P2
try:
    P2_18 = _load("pi2_map_18_vi", PI2_DIR / "map_18_vi.py")
finally:
    sys.path[:] = _saved_path
    if _saved_mod is not None:
        sys.modules["map_common_vi"] = _saved_mod
    else:
        sys.modules.pop("map_common_vi", None)

present, lc, NDE, GAP = P2.present, P2.lc, P2.NDE, P2.GAP
CORE, MATRIX, SATI_BARE = P2.CORE, P2.MATRIX, P2.SATI_BARE
pi1_value, pi1_map_values, KH = P2.pi1_value, P2.pi1_map_values, P2.KH


def pi2_value(kw, kws, text=None):
    """The approved pi-2 value of a keyword (tables only; pi-2 segment rules are not applied)."""
    return P2_18._base_value(kw, kws, text or "")


_PI2_MAP_CACHE = {}


def pi2_map_values(kw):
    """Counter of the values the approved pi-2 Vietnamese keyword map gives `kw` (exact keyword)."""
    if not _PI2_MAP_CACHE:
        for line in PI2_MAP.read_text(encoding="utf-8").splitlines():
            if "] " not in line:
                continue
            for pair in line.split("] ", 1)[1].split(", "):
                if "=" in pair:
                    k, v = pair.split("=", 1)
                    _PI2_MAP_CACHE.setdefault(k, Counter())[v] += 1
    return _PI2_MAP_CACHE.get(kw, Counter())


# ---------------------------------------------------------------------------- reading (pi-3 paths)
def read_keywords(part):
    out = []
    for line in (HERE / f"{part}.keywords.md").read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        bid, rest = line.split("] ", 1)
        out.append((bid[1:], [k.strip() for k in rest.split(", ")]))
    return out


def read_vietnamese(part):
    return P2.P1._segments(VI_DIR / f"{part}.md")


def read_pali(part):
    return P2.P1._segments(PI_DIR / f"{part}.md")


# ---------------------------------------------------------------------------- the pi-3 table (sample)
_KX = "không xác định về mặt đạo đức"
_INCL, _EXCL = "được gộp vào", "không được gộp vào"
_ASX = "điều không do điều kiện tạo thành"

# numbers: stem -> Vietnamese numeral (B.NUM of build_sample_vi.py / vi-zeroshot-terms.md §7)
NUM = {
    "eka": "một", "dvi": "hai", "ti": "ba", "catu": "bốn", "pañca": "năm", "cha": "sáu", "satta": "bảy",
    "aṭṭha": "tám", "nava": "chín", "dasa": "mười", "ekādasa": "mười một", "dvādasa": "mười hai",
    "terasa": "mười ba", "cuddasa": "mười bốn", "pannarasa": "mười lăm", "soḷasa": "mười sáu",
    "sattarasa": "mười bảy", "aṭṭhārasa": "mười tám", "bāvīsati": "hai mươi hai",
}
# instrumental count words (ekena / ekāya / dvīhi … aṭṭhārasahi) -> numeral
NUM_INS = {"ekena": "một", "ekāya": "một", "dvīhi": "hai", "tīhi": "ba", "catūhi": "bốn", "pañcahi": "năm",
           "chahi": "sáu", "sattahi": "bảy", "aṭṭhahi": "tám", "navahi": "chín", "dasahi": "mười",
           "ekādasahi": "mười một", "dvādasahi": "mười hai", "terasahi": "mười ba", "cuddasahi": "mười bốn",
           "pannarasahi": "mười lăm", "soḷasahi": "mười sáu", "sattarasahi": "mười bảy", "aṭṭhārasahi": "mười tám"}
# N-āyatanehi forms (ekenāyatanena, dvīhāyatanehi … dvādasāyatanehi)
NUM_AY = {"ekenāyatanena": "một"}
for _ins, _n in NUM_INS.items():
    if _ins.endswith("hi") and _ins not in ("ekena", "ekāya"):
        NUM_AY[_ins[:-1] + "āyatanehi"] = _n          # dasahi -> dasahāyatanehi, dvīhi -> dvīhāyatanehi
NUM_AY["catūhāyatanehi"] = "bốn"
NUM_AY["dvādasāyatanehi"] = "mười hai"

KD = {
    # ---- preamble / book
    "dhātukathā": "Thảo luận về các yếu tố", "dhātukathāya": "Thảo luận về các yếu tố",
    "dhātukathāpāḷi": "Thảo luận về các yếu tố", "pāḷi": NDE,
    "kathā": "thảo luận", "sambuddha": "bậc Tự Giác Ngộ",
    "dhammasaṅgaṇī": "Liệt kê các hiện tượng", "saṅgaṇī": "liệt kê", "sabbā": "toàn bộ",
    # ---- matrices and method words (1-uddeso)
    "uddeso": "phần nêu đề mục", "naya": "phương pháp", "nayo": "phương pháp", "mātikā": "ma trận",
    "nayamātikā": "ma trận các phương pháp", "abbhantara": "bên trong", "abbhantaramātikā": "ma trận bên trong",
    "nayamukha": "lối vào các phương pháp", "nayamukhamātikā": "ma trận lối vào các phương pháp",
    "lakkhaṇa": "đặc tính", "lakkhaṇamātikā": "ma trận các đặc tính",
    "bāhira": "bên ngoài", "bāhiramātikā": "ma trận bên ngoài",
    "saṅgaho": "sự gộp vào", "asaṅgaho": "sự không gộp vào", "saṅgaha": "sự gộp vào",
    "asaṅgaha": "sự không gộp vào", "saṅgaho asaṅgaho": "sự gộp vào và sự không gộp vào",
    "saṅgahāsaṅgaha": "sự gộp vào và sự không gộp vào",
    "sampayogo": "sự gắn liền", "vippayogo": "sự không gắn liền",
    "sampayogo vippayogo": "sự gắn liền và sự không gắn liền",
    "sabhāgo": "cùng loại", "visabhāgo": "khác loại", "bhāga": "loại",
    "niddeso": "giải thích", "padaniddeso": "giải thích đề mục", "pada": "đề mục",
    # ---- the inclusion frame (2-pathamanayo …)
    "katihi": "bao nhiêu", "katihāyatanehi": "bao nhiêu lĩnh vực nhận biết",
    "khandho": "khối", "khandhā": "khối", "khandhehi": "khối", "khandhena": "khối",
    "khandhato": "xét theo khối",                         # asaṅkhataṃ khandhato ṭhapetvā «xét theo khối thì ngoại trừ …»
    "āyatanehi": "lĩnh vực nhận biết", "āyatanena": "lĩnh vực nhận biết", "āyatana": "lĩnh vực nhận biết",
    "āyatanāni": "lĩnh vực nhận biết",
    "dhātūhi": "yếu tố", "dhātuyā": "yếu tố", "dhātuyo": "yếu tố", "dhātu": "yếu tố",
    "saṅgahito": _INCL, "saṅgahitā": _INCL, "saṅgahitaṃ": _INCL, "saṅgahitāni": _INCL,
    "asaṅgahito": _EXCL, "asaṅgahitā": _EXCL, "asaṅgahitaṃ": _EXCL, "asaṅgahitāni": _EXCL,
    "sampayuttaṃ": "gắn liền", "vippayuttaṃ": "không gắn liền",
    "sampayuttā": "gắn liền", "vippayuttā": "không gắn liền",
    "ṭhapetvā": "ngoại trừ", "asaṅkhataṃ": _ASX, "asaṅkhataṃ ṭhapetvā": "ngoại trừ " + _ASX,
    "na kehici": "không có" + GAP + "nào", "na kāhici": "không có" + GAP + "nào",   # «Không có khối nào …»
    "natthi": "không có",                                 # «… sampayuttoti? Natthi.» «Không có.» (ch6)
    # relative frame of methods 2-14 (seen in 3-dutiyanayo / 8-sattamanayo): «Đối với X, những hiện tượng nào …
    # được gộp vào theo cách gộp vào khối …, thì những hiện tượng đó …»; leading «những» dropped as «các»
    "ye dhammā": "hiện tượng nào", "te dhammā": "hiện tượng đó", "tehi dhammehi": "hiện tượng ấy",
    "saṅgahena": "theo cách gộp vào", "khandhasaṅgahena": "theo cách gộp vào khối",
    "āyatanasaṅgahena": "theo cách gộp vào lĩnh vực nhận biết", "dhātusaṅgahena": "theo cách gộp vào yếu tố",
    "khandha": "khối", "punareva": "rồi lại",
    # round labels «(Phần xét …)»
    "ekamūlakaṃ": "phần xét từng mục một", "dukamūlakaṃ": "phần xét từng nhóm hai",
    "tikamūlakaṃ": "phần xét từng nhóm ba", "catukkamūlakaṃ": "phần xét từng nhóm bốn",
    "pañcakaṃ": "phần xét cả năm", "catukkaṃ": "phần xét cả bốn", "dvādasakaṃ": "phần xét cả mười hai",
    "aṭṭhārasakaṃ": "phần xét cả mười tám",
    "eka": "từng mục một", "duka": "từng nhóm hai", "tika": "từng nhóm ba", "catukka": "từng nhóm bốn",
    "mūlakaṃ": "phần xét",
    # ---- section headings
    "āyatanaṃ": "lĩnh vực nhận biết",               # heading «Các lĩnh vực nhận biết»; member of X-āyatanaṃ: context3
    "saccaṃ": "sự thật", "saccāni": "sự thật", "indriyaṃ": "năng lực", "indriyāni": "năng lực",
    "paṭicca": "tùy thuộc vào điều kiện", "samuppāda": "sự sinh khởi", "samuppādo": "sự sinh khởi",
    "ādi": "mục khác",                                # «… và các mục khác»
    "tikaṃ": "bộ ba", "dukaṃ": "bộ đôi",
    # ---- the members (vi-zeroshot-terms.md §8, pi-1 / pi-2 words)
    "pañcakkhandhā": "năm khối", "dvādasāyatanāni": "mười hai lĩnh vực nhận biết",
    "aṭṭhārasa dhātuyo": "mười tám yếu tố", "cattāri saccāni": "bốn sự thật",
    "bāvīsatindriyāni": "hai mươi hai năng lực",
    "cakkhu": "mắt", "sota": "tai", "ghāna": "mũi", "jivhā": "lưỡi", "kāya": "thân", "mana": "ý", "mano": "ý",
    "sadda": "âm thanh", "gandha": "mùi", "rasa": "vị", "phoṭṭhabba": "vật xúc chạm",
    "arūpa": "không hình sắc",
    "cakkhāyatanaṃ": "lĩnh vực mắt", "sotāyatanaṃ": "lĩnh vực tai", "ghānāyatanaṃ": "lĩnh vực mũi",
    "jivhāyatanaṃ": "lĩnh vực lưỡi", "kāyāyatanaṃ": "lĩnh vực thân", "rūpāyatanaṃ": "lĩnh vực hình sắc",
    "saddāyatanaṃ": "lĩnh vực âm thanh", "gandhāyatanaṃ": "lĩnh vực mùi", "rasāyatanaṃ": "lĩnh vực vị",
    "phoṭṭhabbāyatanaṃ": "lĩnh vực vật xúc chạm", "manāyatanaṃ": "lĩnh vực ý",
    "dhammāyatanaṃ": "lĩnh vực đối tượng của ý",
    "cakkhudhātu": "yếu tố mắt", "sotadhātu": "yếu tố tai", "ghānadhātu": "yếu tố mũi",
    "jivhādhātu": "yếu tố lưỡi", "kāyadhātu": "yếu tố thân", "rūpadhātu": "yếu tố hình sắc",
    "saddadhātu": "yếu tố âm thanh", "gandhadhātu": "yếu tố mùi", "rasadhātu": "yếu tố vị",
    "phoṭṭhabbadhātu": "yếu tố vật xúc chạm", "dhammadhātu": "yếu tố đối tượng của ý",
    "cakkhuviññāṇa": "thức qua mắt", "sotaviññāṇa": "thức qua tai", "ghānaviññāṇa": "thức qua mũi",
    "jivhāviññāṇa": "thức qua lưỡi", "kāyaviññāṇa": "thức qua thân", "manoviññāṇa": "ý thức",
    "cakkhuviññāṇadhātu": "yếu tố thức qua mắt", "sotaviññāṇadhātu": "yếu tố thức qua tai",
    "ghānaviññāṇadhātu": "yếu tố thức qua mũi", "jivhāviññāṇadhātu": "yếu tố thức qua lưỡi",
    "kāyaviññāṇadhātu": "yếu tố thức qua thân", "manodhātu": "yếu tố ý", "manoviññāṇadhātu": "yếu tố ý thức",
    "dukkhasaccaṃ": "sự thật về khổ đau", "samudayasaccaṃ": "sự thật về sự phát sinh",
    "nirodhasaccaṃ": "sự thật về sự chấm dứt", "maggasaccaṃ": "sự thật về con đường",
    "samudaya": "sự phát sinh", "nirodha": "sự chấm dứt", "magga": "con đường",
    "cakkhundriyaṃ": "năng lực mắt", "manindriyaṃ": "năng lực ý",
    "itthi": "nữ tính", "purisa": "nam tính", "jīvita": "sống",
    "saddhā": "niềm tin", "samādhi": "định tâm", "paññā": "trí tuệ", "somanassa": "niềm vui",
    "domanassa": "nỗi buồn",
    # anaññātaññassāmītindriyaṃ «năng lực biết được điều chưa từng biết»: aññāta = biết (approved pi-1 map value)
    "ñassāmi": "biết được", "aññāta": "biết",
    "aññā": "hiểu biết trọn vẹn", "aññātāvī": "người đã hiểu biết trọn vẹn",
    "avijjā": "vô minh", "paccayā": "làm điều kiện cho", "saṅkhārā": "sự tạo tác",
    "viññāṇaṃ": "thức", "nāmarūpaṃ": "phần tinh thần và vật chất", "nāmarūpa": "phần tinh thần và vật chất",
    "phasso": "sự tiếp xúc", "vedanā": "cảm giác", "taṇhā": "khao khát", "upādānaṃ": "sự bám víu",
    "bhavo": "sự hiện hữu", "upapatti": "tái sinh", "kāma": "dục lạc", "vokāra": "gồm" + GAP + "khối",
    "nāsaññā": "không phải không có tri giác",
    "jāti": "sự sinh", "jarā": "sự lão hóa", "maraṇaṃ": "sự chết",
    "soko": "sự sầu muộn", "paridevo": "sự than khóc", "dukkhaṃ": "sự khó chịu", "domanassaṃ": "nỗi buồn",
    "upāyāso": "sự tuyệt vọng", "upaṭṭhānaṃ": "sự thiết lập", "upaṭṭhānā": "sự thiết lập",
    "padhānaṃ": "nỗ lực", "padhānā": "nỗ lực", "sammā": "đúng đắn",
    "iddhi": "thần thông", "pādā": "nền tảng", "jhānaṃ": "tầng thiền", "jhānāni": "tầng thiền",
    "appamaññā": "trạng thái không thể đo lường", "appamaññāyo": "trạng thái không thể đo lường",
    "balāni": "sức mạnh", "bodhi": "giác ngộ", "aṅgā": "chi phần", "ariyo": "cao quý",
    "aṭṭhaṅgiko": "gồm tám chi phần", "maggo": "con đường", "cetanā": "chủ ý", "manasikāro": "sự chú tâm",
    "cittaṃ": "tâm", "citta": "tâm", "cittā": "tâm", "dhammā": "hiện tượng",
    # ---- triad / dyad names (pi-1 MATRIX words as the text writes them)
    "kusalā": "thiện", "akusalā": "bất thiện", "abyākatā": _KX,
    "pahātabbā": "cần dứt bỏ", "bhāvanāya pahātabbā": "cần dứt bỏ bằng sự tu tập",
    "dassanena pahātabbā": "cần dứt bỏ bằng sự thấy chân lý",
    "dassanena": "sự thấy chân lý", "bhāvanāya": "sự tu tập",
    "gāmino": "dẫn đến", "sekkha": "thuộc về người còn đang tu học",
    "mahaggata": "rộng lớn", "appamāṇa": "không thể đo lường", "paritta": "hạn hẹp",
    "adhipatino": "lấy" + GAP + "làm yếu tố chủ đạo",
    "saṃkiliṭṭha": "bị phiền não làm vẩn đục", "asaṃkiliṭṭha": "không bị phiền não làm vẩn đục",
    "upādinna": "do nghiệp tạo ra", "upādinnā": "do nghiệp tạo ra",
    "savitakka": "có sự hướng tâm", "avitakka": "không có sự hướng tâm",
    "vitakka": "sự hướng tâm", "vitakkā": "sự hướng tâm", "vicāra": "sự duy trì tâm", "vicārā": "sự duy trì tâm",
    "pīti": "sự hân hoan", "sahagatā": "đi kèm",
    "sahagatā dhammā": "hiện tượng có" + GAP + "đi kèm",          # approved pi-1 value («có X đi kèm»)
    "na sahagatā dhammā": "hiện tượng không có" + GAP + "đi kèm",
    "avacarā": "thuộc cõi", "raṇā": "xung đột",
    "sanidassana": "thấy được", "anidassana": "không thấy được", "paṭighā": "có tính va chạm",
    "upādā": "phái sinh", "cetasikā": "yếu tố đồng hành với tâm",
    "samuṭṭhānā": "do" + GAP + "sinh ra", "anuparivattino": "vận hành theo",
    "cittānuparivattino": "vận hành theo tâm", "citta anuparivattino": "vận hành theo tâm",
    "saṃsaṭṭha": "hòa lẫn", "visaṃsaṭṭhā": "không hòa lẫn",
    "hetū": "gốc rễ", "āsava": "ô nhiễm", "kilesā": "phiền não", "kilesa": "phiền não",
    "upādānā": "sự bám víu", "parāmāsā": "sự hiểu sai lệch", "parāmāsa": "sự hiểu sai lệch",
    "saṃyojanā": "xiềng xích", "ganthā": "nút thắt", "oghā": "dòng lũ", "yogā": "ách", "nīvaraṇā": "chướng ngại",
    "viññeyyā": "có thể nhận biết",
    # ---- the variant bracket of ^3-112 (vibha. dukapañhāpucchakepi): its label is translated, but present()
    # removes brackets; values listed as presence exceptions by the part script
    "pañhā": "hỏi đáp", "pucchake": "phần hỏi đáp",
}
for _n, _v in NUM.items():
    KD.setdefault(_n, _v)
for _ins, _v in NUM_INS.items():
    KD[_ins] = _v
    KD[f"{_ins} dhātūhi"] = f"{_v} yếu tố"
    KD[f"{_ins} khandhehi"] = f"{_v} khối"
for _ay, _v in NUM_AY.items():
    KD[_ay] = f"{_v} lĩnh vực nhận biết"

_NEG = {"na": "không", "no": "không phải", "neva": "không"}
# «X saṅgahito», «dhammā asaṅgahitā», «dhammā vippayuttā» …: subject + predicate as the segment writes them
_TAIL = {}
for _e in ("o", "ā", "aṃ", "āni"):
    _TAIL["saṅgahit" + _e], _TAIL["asaṅgahit" + _e] = _INCL, _EXCL
for _e in ("o", "ā", "aṃ"):
    _TAIL["sampayutt" + _e], _TAIL["vippayutt" + _e] = "gắn liền", "không gắn liền"
_AY_COUNT = re.compile(r"^āyatanehi (\w+)$")


def _join(a, b, text):
    """«a b» where the segment has it contiguous, else «a … b»."""
    v = f"{a} {b}"
    if text is None or present(v, text):
        return v
    return a + GAP + b


def context3(kw, k, kws, text):
    """Segment rules of the pi-3 frame (k: lower-cased keyword). None = no rule."""
    s = set(lc(x) for x in kws)
    if k in ("sukha",):            # «năng lực dễ chịu» / «có hạnh phúc đi kèm»
        return "hạnh phúc" if present("hạnh phúc", text) else "dễ chịu"
    if k in ("dukkha",):           # «sự thật về khổ đau» / «năng lực khó chịu», «không khó chịu …»
        return "khổ đau" if present("khổ đau", text) else "khó chịu"
    if k == "upekkhā":             # «có sự bình thản đi kèm» / «năng lực bình thản» (pi-1 SATI_BARE pattern)
        return "sự bình thản" if present("sự bình thản", text) else "bình thản"
    if k == "sati":                # «sự tỉnh thức» / bare «tỉnh thức» inside «sự thiết lập tỉnh thức», «năng lực …»
        return "sự tỉnh thức" if present("sự tỉnh thức", text) else "tỉnh thức"
    if k == "rūpa":                # rūpakkhandho «khối vật chất» / rūpāyatana, rūpadhātu, rūpabhava «hình sắc»
        return "hình sắc" if present("hình sắc", text) else "vật chất"
    if k == "saññā":               # bhava list «sự hiện hữu có tri giác» (pi-2 notes-map-6) / the factor «tri giác»
        return "có tri giác" if "bhavo" in s else "tri giác"
    if k == "dhamma":              # dhammāyatana / dhammadhātu «đối tượng của ý» / dhammasaṅgaṇī «hiện tượng»
        return "đối tượng của ý" if present("đối tượng của ý", text) else "hiện tượng"
    if k == "saṅkhāra":            # saṅkhārakkhandho «khối tạo tác» / saṅkhārapaccayā «các sự tạo tác …»
        return "tạo tác" if present("khối tạo tác", text) else "sự tạo tác"
    if k == "āyatanaṃ":            # member of a named X-āyatanaṃ «lĩnh vực mắt» / saḷāyatanaṃ, heading
        named = any(x != k and x.endswith("āyatanaṃ") and " " not in x for x in s)
        return "lĩnh vực" if named else "lĩnh vực nhận biết"
    if k in ("hetukā",):           # «có gốc rễ» / only maggahetukā: «lấy … làm gốc rễ» (pi-2 rule)
        return "có gốc rễ" if present("có gốc rễ", text) else "lấy" + GAP + "làm gốc rễ"
    if k in ("ārammaṇā",):         # «có đối tượng» / only maggārammaṇā: «lấy … làm đối tượng»
        return "có đối tượng" if present("có đối tượng", text) else "lấy" + GAP + "làm đối tượng"
    if k in ("uppannā",):          # «đã sinh khởi» / fragment of anuppannā «chưa sinh khởi»
        return "đã sinh khởi" if present("đã sinh khởi", text) else "sinh khởi"
    if k in ("sampayuttaṃ", "vippayuttaṃ", "saṅgahitaṃ", "asaṅgahitaṃ"):
        base = {"sampayuttaṃ": "gắn liền", "vippayuttaṃ": "không gắn liền", "saṅgahitaṃ": _INCL,
                "asaṅgahitaṃ": _EXCL}[k]
        return "điều " + base if present("điều " + base, text) else base   # method terms «điều …» (Nayamātikā)
    return None


def value(kw, kws, table=None, text=None):
    """table -> KD -> context3 -> alternatives -> counts -> «X saṅgahito» -> «X dhammā» -> the pi-2 / pi-1 chain.
    `text` (the segment's Vietnamese) decides the context rules and contiguous vs « … »."""
    k = lc(kw)
    t = text or ""
    if table and k in table:
        return table[k]
    v = context3(kw, k, kws, t)
    if v is not None:
        return v
    if k in KD:
        return KD[k]
    if k in KH:                                            # exact pi-2 table entry («sukhāya vedanāya sampayuttā» …)
        return KH[k]
    if " / " in k:                                         # «āyatanāni / pādā»: alternatives, each mapped
        return " / ".join(value(p, kws, table, text) for p in kw.split(" / "))
    m = _AY_COUNT.match(k)
    if m and m.group(1) in NUM_INS:                        # «āyatanehi sattarasahi»: adjacent words of the count line
        return _join("lĩnh vực nhận biết", NUM_INS[m.group(1)], text)
    parts = k.split(" ")
    if len(parts) >= 2 and parts[-1] in _TAIL:             # «Cakkhāyatanaṃ saṅgahitaṃ», «dhātu saṅgahitā» …
        hv = value(kw.rsplit(" ", 1)[0], kws, table, text)
        return _join(hv, _TAIL[parts[-1]], text)
    if len(parts) >= 2 and parts[-1] == "dhammā":         # «Kusalā dhammā», «na sahagatā dhammā» …
        neg = ""
        body = parts[:-1]
        if body[0] in _NEG and len(body) > 1:
            neg, body = _NEG[body[0]], body[1:]
        xv = value(" ".join(body), kws, table, text)
        head = "hiện tượng" + (" " + neg if neg else "")
        for cand in (f"{head} {xv}", f"{head} là {xv}" if xv.startswith("đối tượng") else None):
            if cand and (text is None or present(cand, text)):
                return cand
        return head + GAP + xv
    try:
        return pi2_value(kw, kws, text)
    except KeyError:
        pass
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
    a = [l.split("] ", 1) for l in (HERE / f"{part}.keywords.md").read_text(encoding="utf-8").splitlines() if l.strip()]
    b = [l.split("] ", 1) for l in (HERE / f"{part}.mapped.md").read_text(encoding="utf-8").splitlines() if l.strip()]
    assert [x[0] for x in a] == [x[0] for x in b], part
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
