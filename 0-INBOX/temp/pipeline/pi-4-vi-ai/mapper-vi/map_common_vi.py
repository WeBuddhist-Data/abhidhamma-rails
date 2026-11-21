"""Shared helpers and tables for the pi-4 (Puggalapaññatti) Pāli->Vietnamese keyword maps (pi-4-vi-ai/mapper-vi/).

Importing this module writes nothing: sys.dont_write_bytecode is set before the pi-3 (and through it the pi-2 / pi-1)
modules are loaded, none of their build functions is called, and the pi-3 part scripts are loaded under private names
and removed from sys.modules again (check_parts_vi.py hashes every pi-1 / pi-2 / pi-3 *.mapped.md before and after).

    import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
    from map_common_vi import *

Main pieces
- read_keywords(part) / read_vietnamese(part) / read_pali(part)    pi-4 paths; a segment = the lines up to and
                              including the line that ends with ^id (headings without a blank line between them are
                              separate segments)
- present(value, text)        the pi-1 presence check (literal, NFC, case-insensitive, word-bounded; " … " parts in
                              order, " / " alternatives; variant brackets removed first)
- CORE, MATRIX, SATI_BARE, KH, KD, lc, NDE, GAP, pi1_value, pi2_value, context3    re-exported from pi-3
- pi3_value(kw, kws, text)    the whole approved pi-3 table chain without its segment overrides (pi-3 map_15_vi.py
                              _value: T15 (= T3 + T11 + T09 …) -> context3 -> KD -> pi-2 chain -> pi-1 chain)
- pi1_map_values / pi2_map_values / pi3_map_values(kw)    Counter of the values the approved Vietnamese maps give
- en_ru(bid)                  {kw: (english, russian)} of the pi-4 English / Russian maps (meaning cross-check only)
- PG                          the pi-4 table settled on the sample (preamble, 1-matika, 2-ekakapuggalapannatti); later
                              parts extend it in their own script ({**PG, ...}), never here
- NAMES                       person-type names (matrix order) as the translation writes them
- context4(kw, k, kws, text)  segment rules of the pi-4 frame (None = no rule)
- value(kw, kws, table=None, text=None)
                              table -> context4 -> PG -> pi3_value (context3 -> KD -> pi-2 -> pi-1)
- build_part(part, resolver)  writes <part>.mapped.md; stops on an unmapped keyword; refuses ", " in a value
- verify(part, allowed=None)  the brief's structural check + the presence check; `allowed` = {(id, kw): reason}
- prior_hashes()              sha256 of every pi-1 / pi-2 / pi-3 *.mapped.md
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
PI3_DIR = PIPE / "pi-3-vi-ai" / "mapper-vi"
VI_DIR = ROOT / "AI_translation" / "vietnamese" / "pi-4-vietnamese-plain-zeroshot_split_chapters"
PI_DIR = ROOT / "AI_translation" / "pali" / "pi-4_split_chapters"
MAPS = {n: ROOT / "AI_translation" / "vietnamese" / f"pi-{n}-keywords-by-reference-pali-vietnamese-plain.md"
        for n in (1, 2, 3)}
EN_MAP = ROOT / "AI_translation" / "english" / "pi-4-keywords-by-reference-pali-english-plain.md"
RU_MAP = ROOT / "AI_translation" / "russian" / "pi-4-keywords-by-reference-pali-russian-plain.md"


def prior_hashes():
    """sha256 of every pi-1 / pi-2 / pi-3 mapped file (approved outputs this module must never rewrite)."""
    out = {}
    for d in (PI1_DIR, PI2_DIR, PI3_DIR):
        for f in sorted(d.glob("*.mapped.md")):
            out[str(f)] = hashlib.sha256(f.read_bytes()).hexdigest()
    return out


# ---------------------------------------------------------------------------- pi-3 modules (read-only)
def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


_PI3_NAMES = ("map_common_vi", "map_sample_vi") + tuple(f"map_{n}_vi" for n in range(3, 16))
_saved_mods = {n: sys.modules.get(n) for n in _PI3_NAMES}
_saved_path = list(sys.path)
try:
    P3 = _load("pi3_map_common_vi", PI3_DIR / "map_common_vi.py")
    # the pi-3 part scripts do `from map_common_vi import ...` / `import map_N_vi` with the pi-3 folder on sys.path
    for _n in _PI3_NAMES:
        sys.modules.pop(_n, None)
    sys.modules["map_common_vi"] = P3
    sys.path.insert(0, str(PI3_DIR))
    P3_15 = _load("pi3_map_15_vi", PI3_DIR / "map_15_vi.py")
finally:
    sys.path[:] = _saved_path
    for _n in _PI3_NAMES:
        if _saved_mods[_n] is not None:
            sys.modules[_n] = _saved_mods[_n]
        else:
            sys.modules.pop(_n, None)

present, lc, NDE, GAP = P3.present, P3.lc, P3.NDE, P3.GAP
CORE, MATRIX, SATI_BARE, KH, KD = P3.CORE, P3.MATRIX, P3.SATI_BARE, P3.KH, P3.KD
pi1_value, pi2_value, context3 = P3.pi1_value, P3.pi2_value, P3.context3
pi3_common_value = P3.value


def pi3_value(kw, kws, text=None):
    """The approved pi-3 value of a keyword (tables of the finished pi-3 chain; pi-3 segment overrides not applied)."""
    return P3_15._value(kw, kws, text or "")


_MAP_CACHE = {}


def _map_values(n, kw):
    if n not in _MAP_CACHE:
        c = {}
        for line in MAPS[n].read_text(encoding="utf-8").splitlines():
            if "] " not in line:
                continue
            for pair in line.split("] ", 1)[1].split(", "):
                if "=" in pair:
                    k, v = pair.split("=", 1)
                    c.setdefault(k, Counter())[v] += 1
        _MAP_CACHE[n] = c
    return _MAP_CACHE[n].get(kw, Counter())


def pi1_map_values(kw):
    return _map_values(1, kw)


def pi2_map_values(kw):
    return _map_values(2, kw)


def pi3_map_values(kw):
    return _map_values(3, kw)


_ENRU = {}


def en_ru(bid):
    """{kw: (english, russian)} for one block of the pi-4 English / Russian maps (meaning cross-check only)."""
    if not _ENRU:
        for lang, path in (("en", EN_MAP), ("ru", RU_MAP)):
            for line in path.read_text(encoding="utf-8").splitlines():
                if not line.startswith("[") or "] " not in line:
                    continue
                b, rest = line.split("] ", 1)
                d = _ENRU.setdefault(b[1:], {})
                for pair in rest.split(", "):
                    if "=" in pair:
                        k, v = pair.split("=", 1)
                        d.setdefault(k, ["", ""])[0 if lang == "en" else 1] = v
    return _ENRU.get(bid, {})


# ---------------------------------------------------------------------------- reading (pi-4 paths)
def read_keywords(part):
    out = []
    for line in (HERE / f"{part}.keywords.md").read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        bid, rest = line.split("] ", 1)
        out.append((bid[1:], [k.strip() for k in rest.split(", ")]))
    return out


_ID = re.compile(r"\s*\^([0-9A-Za-z-]+)\s*$")


def segments(path):
    """{id: text}: the non-empty lines up to and including the line that ends with ^id."""
    segs, buf = {}, []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        m = _ID.search(line)
        if m:
            buf.append(line[: m.start()])
            segs[m.group(1)] = "\n".join(buf).strip()
            buf = []
        else:
            buf.append(line)
    return segs


def read_vietnamese(part):
    return segments(VI_DIR / f"{part}.md")


def read_pali(part):
    return segments(PI_DIR / f"{part}.md")


# ---------------------------------------------------------------------------- the pi-4 table (sample)
_KX = "không xác định về mặt đạo đức"

# person-type names as the translation writes them (matrix ^4-M-7 … ^4-M-15, definitions ch2 …; without the leading
# «Người» capital: the value is case-insensitive). Key = the Pāli name keyword (lower-case first letter).
NAMES = {
    # ---- ekaka (^4-M-7, ch2)
    "samayavimutto": "người được giải thoát theo thời điểm",
    "asamayavimutto": "người được giải thoát không theo thời điểm",
    "kuppadhammo": "người có thể bị lay chuyển", "akuppadhammo": "người không thể bị lay chuyển",
    "parihānadhammo": "người có thể bị sa sút", "aparihānadhammo": "người không thể bị sa sút",
    "cetanābhabbo": "người có khả năng giữ vững nhờ chủ ý",
    "anurakkhaṇābhabbo": "người có khả năng giữ vững nhờ sự gìn giữ",
    "puthujjano": "người phàm phu", "gotrabhū": "người chuyển đổi dòng dõi",
    "bhayūparato": "người kiêng tránh vì sợ hãi", "abhayūparato": "người kiêng tránh không vì sợ hãi",
    "bhabbāgamano": "người có khả năng tiến bước", "abhabbāgamano": "người không có khả năng tiến bước",
    "niyato": "người có hướng đi cố định", "aniyato": "người có hướng đi không cố định",
    "paṭipannako": "người đang thực hành", "phaleṭhito": "người đã đứng vững trong thành quả",
    "samasīsī": "người có hai sự kết thúc cùng lúc", "ṭhitakappī": "người khiến kiếp dừng lại",
    "ariyo": "bậc thánh", "anariyo": "người không phải bậc thánh",
    "sekkho": "người còn đang tu học", "asekkho": "người đã hoàn tất tu học",
    "nevasekkhanāsekkho": "người không phải còn đang tu học cũng không phải đã hoàn tất tu học",
    "tevijjo": "người có ba loại hiểu biết chân thật", "chaḷabhiñño": "người có sáu loại hiểu biết trực tiếp",
    "sammāsambuddho": "bậc Tự Giác Ngộ Hoàn Toàn", "paccekasambuddho": "bậc Độc Giác",
    "ubhatobhāgavimutto": "người được giải thoát theo cả hai cách",
    "paññāvimutto": "người được giải thoát nhờ trí tuệ", "kāyasakkhī": "người chứng nghiệm bằng thân",
    "diṭṭhippatto": "người đạt đến quan điểm", "saddhāvimutto": "người được giải thoát nhờ niềm tin",
    "dhammānusārī": "người đi theo Giáo Pháp", "saddhānusārī": "người đi theo niềm tin",
    "sattakkhattuparamo": "người tái sinh tối đa bảy lần",
    "kolaṅkolo": "người đi từ gia đình này sang gia đình khác", "ekabījī": "người chỉ còn một hạt giống",
    "sakadāgāmī": "bậc trở lại một lần", "anāgāmī": "bậc không trở lại",
    "antarāparinibbāyī": "bậc nhập Niết-bàn trọn vẹn trong khoảng giữa",
    "upahaccaparinibbāyī": "bậc nhập Niết-bàn trọn vẹn khi gần mạng chung",
    "asaṅkhāraparinibbāyī": "bậc nhập Niết-bàn trọn vẹn không có sự thúc đẩy",
    "sasaṅkhāraparinibbāyī": "bậc nhập Niết-bàn trọn vẹn có sự thúc đẩy",
    "uddhaṃsotoakaniṭṭhagāmī": "bậc ngược dòng đi đến cõi Sắc Cứu Cánh",
    "uddhaṃsoto akaniṭṭhagāmī": "bậc ngược dòng đi đến cõi Sắc Cứu Cánh",
    "sotāpanno": "bậc vào dòng", "arahā": "bậc A-la-hán",
    # ---- duka (^4-M-8, ch3)
    "kodhano": "người giận dữ", "upanāhī": "người ôm hận", "makkhī": "người gièm pha", "paḷāsī": "người ganh đua",
    "issukī": "người ganh tị", "maccharī": "người keo kiệt", "saṭho": "người gian xảo", "māyāvī": "người xảo trá",
    "ahiriko": "người không biết hổ thẹn", "anottappī": "người không biết ghê sợ tội lỗi",
    "dubbaco": "người khó dạy bảo", "pāpamitto": "người kết bạn với người xấu",
    "muṭṭhassati": "người mất tỉnh thức", "asampajāno": "người thiếu hiểu biết rõ ràng",
    "sīlavipanno": "người suy đồi về giới hạnh", "diṭṭhivipanno": "người suy đồi về quan điểm",
    "ajjhattasaṃyojano": "người có xiềng xích ở nơi bản thân",
    "bahiddhāsaṃyojano": "người có xiềng xích ở bên ngoài bản thân",
    "akkodhano": "người không giận dữ", "anupanāhī": "người không ôm hận", "amakkhī": "người không gièm pha",
    "apaḷāsī": "người không ganh đua", "anissukī": "người không ganh tị", "amaccharī": "người không keo kiệt",
    "asaṭho": "người không gian xảo", "amāyāvī": "người không xảo trá", "hirimā": "người biết hổ thẹn",
    "ottappī": "người biết ghê sợ tội lỗi", "suvaco": "người dễ dạy bảo", "kalyāṇamitto": "người kết bạn với người tốt",
    "upaṭṭhitassati": "người có sự tỉnh thức được thiết lập", "sampajāno": "người có hiểu biết rõ ràng",
    "sīlasampanno": "người thành tựu về giới hạnh", "diṭṭhisampanno": "người thành tựu về quan điểm",
    "hīnādhimutto": "người có chí hướng thấp kém", "paṇītādhimutto": "người có chí hướng ưu việt",
    "titto": "người đã thỏa mãn", "tappetā": "người làm cho người khác thỏa mãn",
    # ---- tika (^4-M-9, ch4)
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
    # ---- catukka (^4-M-10, ch5)
    "asappuriso": "người không chân chính", "sappuriso": "người chân chính",
    "pāpo": "người xấu", "kalyāṇo": "người tốt",
    "pāpadhammo": "người có phẩm chất xấu", "kalyāṇadhammo": "người có phẩm chất tốt",
    "sāvajjo": "người có lỗi", "vajjabahulo": "người nhiều lỗi", "appavajjo": "người ít lỗi",
    "anavajjo": "người không có lỗi",
    "ugghaṭitaññū": "người hiểu ngay khi vừa được nêu ra", "vipañcitaññū": "người hiểu khi được giải thích chi tiết",
    "neyyo": "người cần được dẫn dắt", "padaparamo": "người chỉ dừng lại ở câu chữ",
    "sarāgo": "người có tham đắm", "sadoso": "người có sân hận", "samoho": "người có si mê",
    "samāno": "người có kiêu mạn",
    "anusotagāmī": "người đi xuôi dòng", "paṭisotagāmī": "người đi ngược dòng", "ṭhitatto": "người đứng vững",
    "samaṇamacalo": "sa-môn bất động", "samaṇapadumo": "sa-môn như hoa sen hồng",
    "samaṇapuṇḍarīko": "sa-môn như hoa sen trắng",
    # ---- pañcaka (^4-M-11, ch6): singular names; the plural «N hạng người X» items are in PG
    "ādheyyamukho": "người cả tin", "lolo": "người không kiên định",
    "piṇḍapātiko": "người chỉ ăn thức ăn khất thực", "paṃsukūliko": "người mặc y may từ vải bỏ đi",
    "āraññiko": "người sống trong rừng", "abbhokāsiko": "người sống ngoài trời",
    "nesajjiko": "người chỉ ngồi không nằm", "sosāniko": "người sống ở bãi tha ma",
}

PG = {
    # ---- book frame (preamble, 1-matika headings and colophon)
    "puggalapaññatti": "Định danh các hạng người", "puggalapaññattipāḷi": "Định danh các hạng người",
    "pāḷi": NDE,
    "paññatti": "sự định danh",              # designation (pi-1 MATRIX «khái niệm» is the 'concept' sense)
    "paññattiyo": "sự định danh",
    "puggala": "hạng người",                 # stem of the title / of X-paññatti lists: «các hạng người»
    "puggalānaṃ": "hạng người",              # Kittāvatā puggalānaṃ … «về các hạng người»; dvinnaṃ puggalānaṃ
    "puggalā": "hạng người",                 # counted types «Hai hạng người –»; context4: «người» in definitions
    "puggalo": "người",
    "mātikā": "ma trận", "uddeso": "phần nêu đề mục", "niddeso": "phần giải thích",
    "niṭṭhitā": "đã hoàn tất",
    # group words: heading «Phần nêu đề mục theo nhóm N», closer «Phân loại theo nhóm N.»
    "ekaka": "nhóm một", "duka": "nhóm hai", "tika": "nhóm ba", "catukka": "nhóm bốn", "pañcaka": "nhóm năm",
    "chakka": "nhóm sáu", "sattaka": "nhóm bảy", "aṭṭhaka": "nhóm tám", "navaka": "nhóm chín", "dasaka": "nhóm mười",
    "ekakaṃ": "phân loại theo nhóm một", "dukaṃ": "phân loại theo nhóm hai", "tikaṃ": "phân loại theo nhóm ba",
    "catukkaṃ": "phân loại theo nhóm bốn", "pañcakaṃ": "phân loại theo nhóm năm",
    "chakkaṃ": "phân loại theo nhóm sáu", "sattakaṃ": "phân loại theo nhóm bảy",
    "aṭṭhakaṃ": "phân loại theo nhóm tám", "navakaṃ": "phân loại theo nhóm chín",
    "dasakaṃ": "phân loại theo nhóm mười",
    # ---- the designation question (^4-M-2 … ^4-M-6): «Sự định danh về các X bao quát đến mức nào? Bao quát N X – …;
    # sự định danh về các X bao quát đến mức ấy.»
    "kittāvatā": "bao quát đến mức nào", "yāvatā": "bao quát", "ettāvatā": "bao quát đến mức ấy",
    "khandhānaṃ": "khối", "āyatanānaṃ": "lĩnh vực nhận biết", "dhātūnaṃ": "yếu tố", "saccānaṃ": "sự thật",
    "indriyānaṃ": "năng lực",
    "khandha": "khối", "āyatana": "lĩnh vực nhận biết", "dhātu": "yếu tố", "sacca": "sự thật", "indriya": "năng lực",
    # ---- definition frame (ch2 …): «Thế nào là X? Ở đời này, có người … – người này được gọi là “X”.»
    "katamo": "thế nào", "katamo puggalo": "thế nào là người",
    "vuccati puggalo": "người" + GAP + "được gọi là",          # «người này được gọi là» (ayaṃ «này» skipped)
    "vuccanti puggalā": "người" + GAP + "được gọi là",        # «những người này được gọi là»
    "vuccati": "được gọi là", "vuccanti": "được gọi là",
    "samannāgato": "được trang bị", "samannāgato puggalo": "người được trang bị",
    "aṭṭhānaṃ": "điều không thể xảy ra",                     # Aṭṭhānametaṃ anavakāso «Đây là điều không thể xảy ra»
    "hoti": NDE,                                             # pi-1 rule; «xảy ra» etc. by override where written
    # ---- persons, groups
    "ariyapuggalā": "bậc thánh", "ariyo": "bậc thánh",
    "avasesā": "còn lại", "avasesā puggalā": "người còn lại",
    "samaṅgino": "có được", "samaṅgino puggalā": "người có được",
    "puggalo lābhī": "người có được", "lābhī": "có được", "lābhī samāpattīnaṃ": "có được các thành tựu thiền",
    "puggalo viharati": "người" + GAP + "an trú", "puggalo pajānāti": "người hiểu rõ",
    "puggalo paripūrakārī": "người thực hành trọn vẹn", "puggalo attantapo": "người tự hành hạ bản thân",
    "puggalo paṭipanno": "người thực hành", "paṭipanno puggalo": "người đang thực hành",
    "puggalassa paṭipannassa": "người đang thực hành",
    "citto puggalo": "người có tâm", "pañño puggalo": "người có trí tuệ", "ṭhitatto puggalo": "người đứng vững",
    "puggalā dullabhā": "hạng người khó tìm gặp", "puggalānaṃ āsavā": "ô nhiễm của" + GAP + "hạng người",
    "dhammakathikā puggalā": "hạng người thuyết giảng Giáo Pháp", "dasa puggalā": "mười hạng người",
    "jano": "người", "janā": "người", "puriso": "người",
    # ---- members of the ekaka names (^4-M-7, ch2)
    "samaya": "thời điểm", "samayena": "theo từng thời điểm", "vimutto": "được giải thoát",
    "vimokkhe": "sự giải thoát", "kuppa": "lay chuyển",
    "akuppa": "không" + GAP + "lay chuyển",                    # own a- kept; «thể bị» = dhammo
    "dhammo": "thể bị",                                      # X-dhammo «có thể bị X» / «không thể bị X» (context4)
    "parihāna": "sa sút", "parihāyati": "sa sút", "cetanā": "chủ ý", "bhabba": "có khả năng",
    "abhabba": "không có khả năng", "anurakkhaṇā": "sự gìn giữ", "anurakkhati": "gìn giữ",
    "anusañceteti": "luôn hướng chủ ý đến",
    "puthu": "phàm phu", "gotra": "dòng dõi", "bhū": "chuyển đổi", "bhaya": "sợ hãi",
    "uparato": "kiêng tránh", "uparatā": "kiêng tránh", "āgamano": "tiến bước",
    "phala": "thành quả", "ṭhito": "đã đứng vững", "ṭhitā": "đã đứng vững",
    "sama": "cùng lúc", "sīsī": "có hai sự kết thúc", "ṭhita": "dừng lại", "kappī": "kiếp",
    "ariya": "cao quý",                                      # ariye vimokkhe / ariyamaggaṃ (context4: «bậc thánh»)
    "vijjo": "hiểu biết chân thật", "abhiñño": "hiểu biết trực tiếp",
    "sammā": "Hoàn Toàn", "sambuddho": "bậc Tự Giác Ngộ", "pacceka": "Độc",
    "paccekabuddho": NDE,                                    # only inside the variant bracket [paccekabuddho (sī.)]
    "bhāga": "cách", "patto": "đạt đến", "pattassa": "đạt đến", "anusārī": "đi theo",
    "khattuṃ": "lần", "kola": "gia đình", "eka": "một", "bījī": "hạt giống",
    "parinibbāyī": "nhập Niết-bàn trọn vẹn", "antarā": "trong khoảng giữa", "upahacca": "khi gần mạng chung",
    "uddhaṃsoto": "ngược dòng", "akaniṭṭha": "cõi Sắc Cứu Cánh", "gāmī": "đi đến",
    "sotāpatti": "vào dòng", "sotāpattiphala": "thành quả vào dòng",
    "sakadāgāmi": "trở lại một lần", "anāgāmi": "không trở lại", "arahatta": "A-la-hán",
    "paṭipanno": "đang thực hành", "paṭipannassa": "đang thực hành",
    "sacchikiriyāya": "tự mình chứng nghiệm",               # pi-1 (no «để», as pahānāya = dứt bỏ)
    "phalasacchikiriyāya": "tự mình chứng nghiệm thành quả",
    "sacchikiriyāya paṭipanno": "đang thực hành để tự mình chứng nghiệm",
    "sacchikiriyāya paṭipannassa": "đang thực hành để tự mình chứng nghiệm",
    "sacchikaroti": "tự mình chứng nghiệm",
    # ---- members of the duka names (^4-M-8)
    "hiriko": "biết hổ thẹn", "vaco": "dạy bảo", "pāpa": "người xấu", "mitto": "kết bạn",
    "dvāro": "cửa", "gutta": "phòng hộ", "guttadvāro": "phòng hộ cửa", "indriyesu": "giác quan",
    "matta": "tiết độ", "ññū": "biết", "bhojane mattaññū": "biết tiết độ trong ăn uống",
    "upaṭṭhita": "được thiết lập", "vipanno": "suy đồi", "sampanno": "thành tựu", "saṃyojano": "xiềng xích",
    "adhimutto": "có chí hướng", "paṇīta": "ưu việt", "dullabhā": "khó tìm gặp", "tappayā": "làm cho thỏa mãn",
    "vaḍḍhanti": "tăng trưởng",
    # ---- members of the tika items (^4-M-9)
    "āso": "mong cầu", "vigata": "đã lìa", "gilāna": "người bệnh", "upamā": "giống như",
    "gūtha": "phân", "puppha": "hoa", "madhu": "mật", "bhāṇī": "nói lời",
    "aruka": "vết thương lở loét", "citto": "có tâm", "vijju": "tia chớp", "vajira": "kim cương",
    "avakujja": "úp ngược", "ucchaṅga": "vạt áo", "pañño": "có trí tuệ",
    "vītarāgo": "đã lìa tham đắm", "kāmesu": "dục lạc", "bhavesu": "sự hiện hữu",
    "pāsāṇa": "đá", "pathavi": "đất", "udaka": "nước", "lekhā": "đường vạch",
    "potthaka": "vải gai thô", "kāsika": "xứ Ca-thi", "kāsikavattha": "vải xứ Ca-thi", "pameyyo": "đo lường",
    "sevitabbo": "đáng gần gũi", "bhajitabbo": "đáng kết giao", "payirupāsitabbo": "đáng thân cận",
    "sakkatvā": "lòng tôn kính", "garuṃ katvā": "trân trọng",
    "jigucchitabbo": "đáng ghê tránh", "ajjhupekkhitabbo": "đáng được nhìn với sự bình thản",
    "sīlesu": "giới hạnh", "paripūrakārī": "thực hành trọn vẹn",
    "sīlesu paripūrakārī": "thực hành trọn vẹn các giới hạnh", "kārī": "thực hành",
    "samādhismiṃ": "định tâm", "samādhismiṃ paññāya": "định tâm" + GAP + "trí tuệ", "satthāro": "bậc đạo sư",
    # ---- members of the catukka items (^4-M-10)
    "asappurisataro": "người không chân chính hơn", "dhammakathikā": "thuyết giảng Giáo Pháp",
    "kathikā": "thuyết giảng", "vajja": "lỗi", "ugghaṭita": "ngay khi vừa được nêu ra",
    "vipañcita": "được giải thích chi tiết", "pada": "câu chữ",
    "yutta": "xác đáng", "mutta": "lưu loát", "paṭibhāno": "có tài ứng đáp",
    "valāhaka": "mây mưa", "mūsika": "chuột", "amba": "quả xoài", "kumbha": "cái chum",
    "udakarahada": "hồ nước", "balībadda": "bò đực", "āsīvisa": "rắn độc", "rukkha": "cây",
    "anuvicca": "xem xét", "pariyogāhetvā": "tìm hiểu thấu đáo", "arahassa": "đáng",
    "avaṇṇārahassa": "người đáng chê trách", "vaṇṇārahassa": "người đáng khen ngợi", "vaṇṇa": "khen ngợi",
    "vaṇṇaṃ bhāsitā": "nói lời khen ngợi", "avaṇṇaṃ bhāsitā": "nói lời chê trách",
    "upadaṃsitā": "bày tỏ", "pasādaṃ upadaṃsitā": "bày tỏ lòng tin trong sáng",
    "appasādaṃ": "sự thiếu lòng tin trong sáng",
    "pasādanīye ṭhāne pasādaṃ": "lòng tin trong sáng ở nơi đáng có lòng tin trong sáng",
    "bhūtaṃ": "đúng sự thật", "tacchaṃ": "chính xác",
    "uṭṭhāna": "công sức", "puñña": "phước", "upajīvī": "sống nhờ",
    "tamo": "bóng tối", "joti": "ánh sáng", "parāyano": "hướng đến", "oṇato": "ở thấp",
    "pamāṇo": "lấy" + GAP + "làm thước đo", "ghosa": "tiếng tăm", "lūkha": "sự đạm bạc",
    "pasanno": "có lòng tin trong sáng",
    "atta": "bản thân", "attanā": "với bản thân", "para": "người khác",
    "attantapo": "tự hành hạ bản thân", "tapo": "hành hạ", "paritāpana": "việc hành hạ",
    "anuyoga": "thực hành", "paritāpanānuyoga": "thực hành việc hành hạ", "anuyutto": "chuyên tâm",
    "nicchāto": "không còn đói khát", "chāto": "đói khát", "nibbuto": "đã lắng dịu",
    "sītībhūto": "đã trở nên mát mẻ", "paṭisaṃvedī": "cảm nhận", "brahma": "cao thượng",
    "rāgo": "tham đắm", "doso": "sân hận", "moho": "si mê", "māno": "kiêu mạn",
    "samathassa": "sự tĩnh lặng", "cetosamathassa": "sự tĩnh lặng của tâm", "vipassanāya": "sự thấu suốt",
    "dhammavipassanāya": "sự thấu suốt các hiện tượng", "adhipaññā": "trí tuệ cao thượng",
    "adhipaññādhamma": "hiện tượng nhờ trí tuệ cao thượng",
    "tiṇṇo": "đã vượt qua", "pāraṅgato": "đã đến bờ bên kia", "thale": "đất liền", "tiṭṭhati": "đứng",
    "brāhmaṇo": "bà-la-môn", "suto": "học hỏi", "sutena": "điều đã học", "upapanno": "thành tựu",
    "sutena upapanno": "thành tựu nhờ điều đã học",
    "samaṇa": "sa-môn", "samaṇesu": "sa-môn", "acalo": "bất động", "padumo": "hoa sen hồng",
    "puṇḍarīko": "hoa sen trắng", "sukhumālo": "tinh tế",
    # ---- members of the pañcaka items (^4-M-11): plural names «N hạng người X» = «hạng người X»
    "ārabhati": "phạm lỗi", "vippaṭisārī": "ăn năn", "cetovimuttiṃ": "sự giải thoát của tâm",
    "paññāvimuttiṃ": "sự giải thoát nhờ trí tuệ", "vimuttiṃ": "sự giải thoát", "yathā": "đúng như",
    "parisesā": "dư sót", "nirujjhanti": "chấm dứt",
    "datvā": "cho", "avajānāti": "khinh thường", "saṃvāsena": "sống chung",
    "mando": "người chậm hiểu", "momūho": "mê muội", "yodhājīva": "chiến binh",
    "piṇḍapātikā": "hạng người chỉ ăn thức ăn khất thực", "piṇḍa": "thức ăn khất thực",
    "khalu": "không nhận", "bhattikā": "thức ăn dâng sau bữa",
    "āsanikā": "chỉ ăn" + GAP + "ngồi",                       # ekāsanikā «chỉ ăn một lần ngồi» (eka not a keyword)
    "paṃsukūlikā": "hạng người mặc y may từ vải bỏ đi",
    "cīvarikā": "chỉ dùng" + GAP + "y",                       # tecīvarikā «chỉ dùng ba y» (te- not a keyword)
    "āraññikā": "hạng người sống trong rừng", "mūlikā": "sống dưới gốc",
    "abbhokāsikā": "hạng người sống ngoài trời", "nesajjikā": "hạng người chỉ ngồi không nằm",
    "santhatikā": "ở bất cứ chỗ nào được chỉ định", "sosānikā": "hạng người sống ở bãi tha ma",
    # ---- chakka (^4-M-12, ch2 ^4-22 / ^4-23)
    "sabbaññutaṃ": "sự toàn tri", "pāpuṇāti": "đạt đến", "abhisambujjhati": "giác ngộ", "sāmaṃ": "tự mình",
    "anussutesu": "được nghe", "dhammesu": "điều", "ananussutesu dhammesu": "điều chưa từng được nghe",
    "vasībhāvaṃ": "sự làm chủ", "balesu": "sức mạnh", "saccāni": "sự thật",
    "diṭṭhe dhamme": "trong đời này", "dukkhassantakaro": "người đi đến tận cùng của khổ đau",
    "dukkhassa": "khổ đau", "karo": "đi đến", "sāvaka": "hàng đệ tử", "pāramiṃ": "sự toàn hảo",
    "āgantā": "trở lại", "āgāmī": "người còn trở lại",
    "phalesu": NDE,                                          # only inside the variant bracket [phalesu (pī.)]
    # ---- sattaka (^4-M-13), dasaka (^4-M-16)
    "sakiṃ": "một lần", "nimuggo": "chìm", "ummujjitvā": "trồi lên", "viloketi": "nhìn quanh",
    "patarati": "bơi qua", "paṭigādha": "chỗ chân chạm đáy",
    "niṭṭhā": "đích", "vihāya": "sau khi rời khỏi",
    # ---- the ekaka definitions (ch2)
    "pamādaṃ": "sự buông thả", "kiccha": "khó khăn", "kasira": "vất vả", "samāpattīnaṃ": "thành tựu thiền",
    "sahagatānaṃ": "đi kèm", "rūpasahagatānaṃ": "đi kèm với hình sắc",
    "yatthicchakaṃ": "ở nơi nào mình muốn", "yadicchakaṃ": "thành tựu thiền nào mình muốn",
    "icchakaṃ": "mình muốn", "na": "không",
    "phusitvā": "chạm đến", "parikkhīṇā": "được diệt tận", "paññāya": "trí tuệ",
    "saṃyojanāni": "xiềng xích", "pahīnāni": "đã được dứt bỏ", "pahīnā": "đã được dứt bỏ",
    "avakkanti": "sự đi vào", "samanantarā": "ngay sau", "sekkhā": "người còn đang tu học",
    "sīlavanto": "giữ giới", "kamma": "nghiệp", "eḷā": "đần độn", "duppaññā": "kém trí tuệ",
    "chandikā": "có ý muốn", "ānantarikā": "phạm nghiệp có quả không gián đoạn", "diṭṭhikā": "có quan điểm",
    "micchādiṭṭhikā": "có quan điểm sai lầm", "uḍḍayhana": "bị thiêu hủy",
    "nirodho": "sự chấm dứt", "dukkhanirodho": "sự chấm dứt khổ đau", "vodiṭṭhā": "thấy rõ",
    "vocaritā": "thông suốt", "gāminī paṭipadā": "cách thực hành dẫn đến", "paveditā": "tuyên bố",
    "paveditā dhammā": "Giáo Pháp" + GAP + "tuyên bố", "dhammā": "Giáo Pháp",
    "vāhiṃ": "dẫn dắt", "adhimattaṃ": "vượt trội",
    "sambodhi": "sự giác ngộ trọn vẹn", "parikkhayā": "diệt tận hoàn toàn",
    "dukkhassantaṃ": "tận cùng của khổ đau", "saṃyojanānaṃ": "xiềng xích", "deve": "chư thiên",
    "mānuse": "loài người", "vinipātadhammo": "phải rơi vào nơi đọa lạc", "sandhāvitvā": "sau khi trôi lăn",
    "saṃsaritvā": "luân chuyển", "mānusakaṃ": "làm người", "nibbattetvā": "sau khi tạo ra",
    "āgantvā": "trở lại", "mohānaṃ": "si mê", "tanuttā": "sự suy yếu",
    "orambhāgiyānaṃ saṃyojanānaṃ": "xiềng xích thuộc phần thấp", "opapātiko": "được hóa sinh",
    "āvatti": "quay trở lại", "āvattidhammo": "quay trở lại",
    "sañjaneti": "làm phát sinh", "upariṭṭhimānaṃ saṃyojanānaṃ": "xiềng xích cao hơn",
    "vemajjhaṃ": "giữa", "pattaṃ": "đến", "atikkamitvā": "sau khi đã qua", "kālakiriyaṃ": "mạng chung",
    "avihā": "cõi Vô Phiền", "atappaṃ": "cõi Vô Nhiệt", "sudassaṃ": "cõi Thiện Hiện", "cuto": "chết",
    "tanubhūtā": "đã suy yếu",
}
for _x, _v in (("khandhānaṃ", "khối"), ("āyatanānaṃ", "lĩnh vực nhận biết"), ("dhātūnaṃ", "yếu tố"),
               ("saccānaṃ", "sự thật"), ("indriyānaṃ", "năng lực"), ("puggalānaṃ", "hạng người")):
    PG[f"kittāvatā {_x}"] = f"{_v} bao quát đến mức nào"      # «Sự định danh về các X bao quát đến mức nào?»
    PG[f"ettāvatā {_x}"] = f"{_v} bao quát đến mức ấy"
PG.update({k: v for k, v in NAMES.items() if k not in PG})

_GROUP = {"ekaka": "một", "duka": "hai", "tika": "ba", "catukka": "bốn", "pañcaka": "năm", "chakka": "sáu",
          "sattaka": "bảy", "aṭṭhaka": "tám", "navaka": "chín", "dasaka": "mười"}


def context4(kw, k, kws, text):
    """Segment rules of the pi-4 frame (k: lower-cased keyword). None = no rule."""
    s = set(lc(x) for x in kws)
    if k == "puggalā":             # «Hai hạng người –», «các hạng người» / definitions «những người …»
        return "hạng người" if present("hạng người", text) else "người"
    if k == "puggalo" and not present("người", text) and present("bậc", text):
        return "bậc"
    if k == "katamo puggalo":      # «Thế nào là người …?» / «Thế nào là bậc …?» (noble types)
        return "thế nào là người" if present("thế nào là người", text) else "thế nào là bậc"
    if k in _GROUP:                # heading «… theo nhóm N» / closer «Giải thích phân loại theo nhóm N.»
        full = "phân loại theo nhóm " + _GROUP[k]
        return full if present(full, text) else "nhóm " + _GROUP[k]
    if k == "niddeso":             # heading «Phần giải thích» / closer «Giải thích phân loại …» (pi-1 / pi-2 / pi-3)
        return "phần giải thích" if present("phần giải thích", text) else "giải thích"
    if k == "paññatti":            # «sự định danh» / title stem «Định danh các hạng người»
        return "sự định danh" if present("sự định danh", text) else "định danh"
    if k == "puggalapaññatti":     # «sự định danh về các hạng người» / the title
        v = "sự định danh về các hạng người"
        return v if present(v, text) else "Định danh các hạng người"
    if k == "dhamma":              # dhammāyatana / dhammadhātu / dhammānusārī, dhammakathikā … / hiện tượng
        for v in ("đối tượng của ý", "Giáo Pháp"):
            if present(v, text):
                return v
        return "hiện tượng"
    if k == "dhammo":              # X-dhammo: «thể bị» (kuppa / parihāna), «phẩm chất» (pāpa / kalyāṇa),
        if s & {"pāpadhammo", "kalyāṇadhammo"}:          # «phải» (avinipāta), none (anāvatti «không còn quay
            return "phẩm chất"                             # trở lại»)
        if "vinipātadhammo" in s:
            return "phải"
        if "āvattidhammo" in s:
            return NDE
        return "thể bị"
    if k in ("rāga", "rāgo"):      # «sự tham đắm dục lạc» / «tham đắm, sân hận và si mê», «chưa lìa tham đắm»
        return "sự tham đắm" if present("sự tham đắm", text) else "tham đắm"
    if k == "saṅkhāra" and present("sự thúc đẩy", text):  # asaṅkhāra / sasaṅkhāra-parinibbāyī (pi-1 sasaṅkhārena)
        return "sự thúc đẩy"
    if k == "ariya":               # ariye vimokkhe, ariyamaggaṃ, ariyadhammassa «cao quý» / only ariyapuggalā
        return "cao quý" if present("cao quý", text) else "bậc thánh"
    if k == "sammā" and "sammāsambuddho" in s:
        return "Hoàn Toàn"
    if k == "sambuddho":           # «bậc Tự Giác Ngộ (Hoàn Toàn)» / only paccekasambuddho «bậc Độc Giác»
        return "bậc Tự Giác Ngộ" if present("bậc Tự Giác Ngộ", text) else "bậc" + GAP + "Giác"
    if k in ("paṭipanno", "paṭipannassa"):                # «đang thực hành» / «thực hành để dứt bỏ», «có người thực
        return "đang thực hành" if present("đang thực hành", text) else "thực hành"   # hành vì lợi ích …»
    if k == "saddhā":              # saddhā / assaddhā (adjective) «có niềm tin» (pi-1 / pi-2) / the faculty «niềm tin»
        return "có niềm tin" if s & {"chandikā", "paññavanto", "duppaññā"} else "niềm tin"
    if k == "niyato" and "parāyano" in s:                  # avinipātadhammo niyato sambodhiparāyano (adjective)
        return "có hướng đi cố định"
    if k == "jīvita" and present("mạng sống", text):      # jīvitapariyādāna «sự kết thúc mạng sống» (pi-1 mạng sống)
        return "mạng sống"
    return None


def value(kw, kws, table=None, text=None):
    """table -> context4 -> PG -> the pi-3 chain (T15 … -> context3 -> KD -> pi-2 -> pi-1)."""
    k = lc(kw)
    t = text or ""
    if table and k in table:
        return table[k]
    v = context4(kw, k, kws, t)
    if v is not None:
        return v
    if k in PG:
        return PG[k]
    return pi3_value(kw, kws, t)


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
