"""Pāli->Vietnamese keyword maps for pi-1 parts 3-02-rupakandam and 3-03-rupakandam (Rūpavibhatti, pairs … elevens).

usage: python -I -X utf8 map_3-02_3-03_vi.py [PART ...]   (writes <part>.mapped.md and verifies it)
       python -I -X utf8 map_3-02_3-03_vi.py dump PART     (prints every distinct keyword=value with its count; writes nothing)

Importing this file writes nothing (it imports map_2-05_3-01_vi.py, which imports map_2-04_vi.py and
map_2-02_2-03_vi.py; none of them rewrites its output on import).
Resolution order per keyword:
  context() -> RUPA (new keys and the 3-02/3-03 readings) -> «rūpaṃ X» / «rūpassa na X» / two-term rules
  -> ADD301 (= PRED301 + MEVA + 3-01 headings) -> MATRIX -> T05 via ch2_value
Answer frame (harmonise pass): «Vật chất nào <pred>? … – vật chất này <pred>.»; the predicate keeps the
PRED301 value (frame «Vật chất nào», «vật chất này», the predicate «là» and the «không (phải là)» of a
na / no item dropped).
Conventions: vi-map-conventions.md and the earlier notes-map-*.md; new: notes-map-3-02_3-03.md.
"""
import importlib.util
import pathlib
import sys
from collections import Counter

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from map_common_vi import (GAP, MATRIX, NDE, build_part, ch2_value, lc, read_keywords,  # noqa: E402
                           read_vietnamese, verify)

_spec = importlib.util.spec_from_file_location("map_2_05_3_01_vi", HERE / "map_2-05_3-01_vi.py")
_p301 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_p301)          # import only: its __main__ block does not run
PRED301, ADD301, T05 = _p301.PRED301, _p301.ADD301, _p301.T05

PARTS = ["3-02-rupakandam", "3-03-rupakandam"]

# ---------------------------------------------------------------- sense organs and their objects (all case forms)
ORGAN = {"cakkhu": "mắt", "sota": "tai", "ghāna": "mũi", "jivhā": "lưỡi", "kāya": "thân"}
_ORGAN_FORMS = {"cakkhu": ["cakkhuṃ", "cakkhumhi", "cakkhunā"], "sota": ["sotaṃ", "sotamhi", "sotena"],
                "ghāna": ["ghānaṃ", "ghānamhi", "ghānena"], "jivhā": ["jivhaṃ", "jivhāya"],
                "kāya": ["kāyaṃ", "kāyamhi", "kāyena", "kāyo", "kāyassa"]}
OBJ = {"rūpa": "hình sắc", "sadda": "âm thanh", "gandha": "mùi", "rasa": "vị", "phoṭṭhabba": "vật xúc chạm"}
_OBJ_FORMS = {"rūpa": ["rūpamhi"], "sadda": ["saddaṃ", "saddo", "saddamhi"],
              "gandha": ["gandhaṃ", "gandho", "gandhamhi"], "rasa": ["rasaṃ", "raso", "rasamhi"],
              "phoṭṭhabba": ["phoṭṭhabbaṃ", "phoṭṭhabbo", "phoṭṭhabbamhi"]}

RUPA = {}
for _o, _vi in ORGAN.items():
    RUPA[_o] = _vi
    for _f in _ORGAN_FORMS[_o]:
        RUPA[_f] = _vi
    _st = "jivhā" if _o == "jivhā" else _o
    RUPA[f"{_st}samphasso"] = f"sự tiếp xúc của {_vi}"
    RUPA[f"{_st}samphassajā"] = f"sinh từ sự tiếp xúc của {_vi}"
    RUPA[f"{_st}samphassajā vedanā"] = f"cảm giác sinh từ sự tiếp xúc của {_vi}"
    RUPA[f"{_st}samphassajāya"] = f"sinh từ sự tiếp xúc của {_vi}"
    RUPA[f"{_st}samphassajāya vedanāya"] = f"cảm giác sinh từ sự tiếp xúc của {_vi}"
    RUPA[f"{_st}viññāṇaṃ"] = f"thức qua {_vi}"
    RUPA[_ORGAN_FORMS[_o][0] + " nissāya"] = _vi + GAP + "dựa vào"   # yaṃ cakkhuṃ nissāya «mắt mà dựa vào nó»
for _o, _vi in OBJ.items():
    RUPA[_o] = _vi
    for _f in _OBJ_FORMS[_o]:
        RUPA[_f] = _vi

# ---------------------------------------------------------------- verbs: tense words kept (as uppannā / uppādino)
for _past, _pres, _fut, _vi in (("suṇi", "suṇāti", "suṇissati", "nghe"), ("ghāyi", "ghāyati", "ghāyissati", "ngửi"),
                                ("sāyi", "sāyati", "sāyissati", "nếm"), ("phusi", "phusati", "phusissati", "chạm"),
                                ("paṭihaññi", "paṭihaññati", "paṭihaññissati", "va chạm"),
                                ("uppajji", "uppajjati", "uppajjissati", "sinh khởi")):
    RUPA.update({_past: "đã " + _vi, _pres: "đang " + _vi, _fut: "sẽ " + _vi})

_NS = "không thấy được nhưng có tính va chạm"
RUPA.update({
    # ---------------------------------------------------------------- qualities (^1-M1-22)
    "anidassano": "không thấy được", "anidassanena": "không thấy được", "anidassanamhi": "không thấy được",
    "sappaṭigho": "có tính va chạm", "sappaṭighena": "có tính va chạm", "sappaṭighamhi": "có tính va chạm",
    "sanidassanamhi": "thấy được",
    "anidassano sappaṭigho": _NS, "anidassanaṃ sappaṭighaṃ": _NS, "anidassanamhi sappaṭighamhi": _NS,
    "anidassanena sappaṭighena": _NS, "anidassanasappaṭighaṃ": _NS,
    "sanidassanaṃ sappaṭighaṃ": "thấy được và có tính va chạm",
    "sappaṭighaṃ paṭihaññi": "có tính va chạm đã va chạm",   # «…, vốn … có tính va chạm, đã va chạm» (comma dropped)
    "sappaṭigho paṭihaññi": "có tính va chạm đã va chạm",
    # ---------------------------------------------------------------- sense-organ definitions
    "pasādo": "chất nhạy cảm", "upādāya pasādo": "chất nhạy cảm phái sinh từ",
    "attabhāva": "sự tồn tại cá nhân",
    "bhūtānaṃ": "yếu tố", "bhūtehi": "yếu tố", "mahābhūtānaṃ": "yếu tố cơ bản", "mahābhūtehi": "yếu tố cơ bản",
    "dvārā": "cánh cửa", "samuddo": "đại dương", "khettaṃ": "cánh đồng", "nettaṃ": "cái dẫn đường",
    "nayanaṃ": "cái chỉ lối", "tīraṃ": "bờ", "suñño": "trống rỗng", "gāmo": "ngôi làng",
    "suñño gāmo": "ngôi làng trống rỗng",
    "nissāya": "dựa vào", "ārammaṇo": "lấy" + GAP + "làm đối tượng",   # rūpārammaṇo «lấy hình sắc / nó làm đối tượng»
    # ---------------------------------------------------------------- visible form (^1-616)
    "vaṇṇa": "màu sắc", "nibhā": "dáng vẻ", "vaṇṇanibhā": "màu sắc và dáng vẻ",
    "upādāya vaṇṇanibhā": "màu sắc và dáng vẻ phái sinh từ",
    "maṇisaṅkhamuttāveḷuriyassa vaṇṇanibhā": "màu sắc và dáng vẻ của ngọc quý vỏ ốc ngọc trai và ngọc lưu ly",
    "jātarūparajatassa vaṇṇanibhā": "màu sắc và dáng vẻ của vàng và bạc",
    "nīlaṃ": "màu xanh", "pītakaṃ": "màu vàng", "lohitakaṃ": "màu đỏ", "odātaṃ": "màu trắng",
    "kāḷakaṃ": "màu đen", "mañjiṭṭhakaṃ": "màu đỏ thẫm", "hari": "màu xanh lục", "harivaṇṇaṃ": "màu ánh lục",
    "ambaṅkuravaṇṇaṃ": "màu chồi xoài", "amba": "xoài", "aṅkura": "chồi",
    "vaṭṭaṃ": "tròn", "parimaṇḍalaṃ": "tròn trịa", "caturaṃsaṃ": "bốn góc", "chaḷaṃsaṃ": "sáu góc",
    "aṭṭhaṃsaṃ": "tám góc", "soḷasaṃsaṃ": "mười sáu góc",
    "chāyā": "bóng râm", "ātapo": "nắng", "āloko": "ánh sáng", "andhakāro": "bóng tối", "abbhā": "mây",
    "mahikā": "sương mù", "dhūmo": "khói", "rajo": "bụi",
    "canda": "trăng", "sūriya": "mặt trời", "maṇḍalassa": "vầng",   # candamaṇḍala / sūriyamaṇḍala «vầng …»
    "ādāsa": "gương", "tārakarūpānaṃ": "vì sao",
    "maṇi": "ngọc quý", "saṅkha": "vỏ ốc", "muttā": "ngọc trai", "veḷuriyassa": "ngọc lưu ly", "rajatassa": "bạc",
    # ---------------------------------------------------------------- sound (^1-620)
    "bheri": "trống lớn", "mudiṅga": "trống cơm", "paṇava": "trống con", "gīta": "hát", "vādita": "nhạc cụ",
    "samma": "chũm chọe", "pāṇi": "vỗ tay", "vāta": "gió", "udaka": "nước", "manussa": "người",
    "amanussa": "loài không phải người",            # «tiếng của những loài không phải người» («những» dropped)
    "sattānaṃ": "chúng sinh", "dhātūnaṃ": "vật", "sannighāta": "va đập",
    "bherisaddo": "tiếng trống lớn", "mudiṅgasaddo": "tiếng trống cơm", "saṅkhasaddo": "tiếng tù và",
    "paṇavasaddo": "tiếng trống con", "gītasaddo": "tiếng hát", "vāditasaddo": "tiếng nhạc cụ",
    "sammasaddo": "tiếng chũm chọe", "pāṇisaddo": "tiếng vỗ tay", "nigghosasaddo": "tiếng ồn ào",
    "dhātūnaṃ sannighātasaddo": "tiếng va đập của các vật", "vātasaddo": "tiếng gió",
    "udakasaddo": "tiếng nước", "manussasaddo": "tiếng người",
    "amanussasaddo": "tiếng của những loài không phải người",
    # ---------------------------------------------------------------- smell and taste (^1-624, ^1-628)
    "mūla": "rễ cây", "sāra": "lõi cây", "taca": "vỏ cây", "patta": "lá", "puppha": "hoa", "phala": "trái cây",
    "khandha": "thân cây", "āmaka": "tanh", "vissa": "ôi thiu",
    "mūlagandho": "mùi rễ cây", "sāragandho": "mùi lõi cây", "tacagandho": "mùi vỏ cây",
    "pattagandho": "mùi lá", "pupphagandho": "mùi hoa", "phalagandho": "mùi trái cây",
    "āmakagandho": "mùi tanh", "vissagandho": "mùi ôi thiu", "sugandho": "mùi thơm", "duggandho": "mùi hôi",
    "mūlaraso": "vị rễ cây", "khandharaso": "vị thân cây", "tacaraso": "vị vỏ cây", "pattaraso": "vị lá",
    "puppharaso": "vị hoa", "phalaraso": "vị trái cây",
    "ambilaṃ": "vị chua", "madhuraṃ": "vị ngọt", "tittakaṃ": "vị đắng", "kaṭukaṃ": "vị cay",
    "loṇikaṃ": "vị mặn", "khārikaṃ": "vị kiềm", "lambilaṃ": "vị chua nhẹ", "kasāvo": "vị chát",
    "sādu": "vị ngon",
    # ---------------------------------------------------------------- tangible (^1-647), elements (^1-967 …)
    "kakkhaḷaṃ": "cái cứng", "mudukaṃ": "cái mềm", "saṇhaṃ": "cái mịn", "pharusaṃ": "cái thô ráp",
    "garukaṃ": "cái nặng", "lahukaṃ": "cái nhẹ",
    "sukha": "dễ chịu", "dukkha": "khó chịu",      # sukhasamphassaṃ «cái có tiếp xúc dễ chịu» (as 3-01 1-590)
    "samphasso": "tiếp xúc", "manāpiyo": "dễ ưa", "amanāpiyo": "không dễ ưa",
    "pathavī": "đất", "khara": "rắn", "kakkhaḷattaṃ": "sự cứng",
    "gataṃ": "điều được xem là",                    # -gata «điều được xem là …»
    "sineho": "chất ẩm", "bandhanattaṃ": "tính kết dính", "bandhanattaṃ rūpassa": "tính kết dính của vật chất",
    "usmā": "hơi ấm", "usumaṃ": "hơi nóng", "thambhitattaṃ": "trạng thái căng cứng",
    # ---------------------------------------------------------------- faculties, intimation, space
    "itthiyā": "người nữ", "purisassa": "người nam", "liṅgaṃ": "hình tướng", "nimittaṃ": "dấu hiệu",
    "kuttaṃ": "cử chỉ", "ākappo": "dáng điệu",
    "rūpīnaṃ dhammānaṃ": "hiện tượng thuộc vật chất",
    "kusalacittassa": "tâm thiện", "akusalacittassa": "tâm bất thiện",
    "abhikkamantassa": "đi tới", "paṭikkamantassa": "đi lui", "ālokentassa": "nhìn thẳng",
    "vilokentassa": "nhìn sang bên", "samiñjentassa": "co lại", "pasārentassa": "duỗi ra",
    "thambhanā": "sự căng cứng", "santhambhitattaṃ": "trạng thái căng cứng toàn diện",
    "viññāpanā": "sự làm cho biết",
    "vācā": "lời nói", "girā": "lời lẽ", "byappatho": "cách nói", "udīraṇaṃ": "sự thốt ra",
    "ghoso": "tiếng nói", "dhoso": "tiếng nói",     # ^1-850 «dhoso» = ghoso (spelling slip)
    "ghosakammaṃ": "sự phát ra tiếng nói",
    "aghaṃ": "khoảng không", "vivaro": "kẽ hở", "asamphuṭṭhaṃ": "điều không bị" + GAP + "chạm đến",
    # ---------------------------------------------------------------- qualities, growth, ageing, impermanence
    "lahupariṇāmatā": "sự chuyển đổi nhanh nhẹn", "avitthanatā": "sự không trì trệ",
    "akathinatā": "sự không cứng nhắc",
    "ācayo": "sự tích lũy", "āyatanānaṃ": "lĩnh vực nhận biết",
    "jīraṇatā": "sự hao mòn", "khaṇḍiccaṃ": "răng gãy rụng", "pāliccaṃ": "tóc bạc", "valittacatā": "da nhăn nheo",
    "āyuno": "tuổi thọ", "saṃhāni": "sự suy giảm", "indriyānaṃ": "năng lực", "paripāko": "sự chín muồi",
    "khayo": "sự hủy diệt", "vayo": "sự suy tàn", "bhedo": "sự tan rã", "paribhedo": "sự tan rã hoàn toàn",
    "antaradhānaṃ": "sự biến mất",
    # ---------------------------------------------------------------- food (^1-645)
    "odano": "cơm", "kummāso": "cháo", "sattu": "bột rang", "maccho": "cá", "maṃsaṃ": "thịt",
    "khīraṃ": "sữa", "dadhi": "sữa đông", "sappi": "bơ lỏng", "navanītaṃ": "bơ tươi", "madhu": "mật ong",
    "phāṇitaṃ": "mật mía",
    "mukha": "miệng", "āsiyaṃ": "đưa vào", "danta": "răng", "vikhādanaṃ": "nhai", "gala": "cổ họng",
    "ajjhoharaṇīyaṃ": "nuốt", "kucchi": "bụng", "vitthambhanaṃ": "làm căng đầy",
    "ojāya": "tinh chất nuôi dưỡng", "yāpenti": "duy trì mạng sống",
    # ---------------------------------------------------------------- classification predicates
    "kammassa katattā": "do nghiệp đã được tạo",    # «sinh ra do nghiệp đã được tạo» («sinh ra» added)
    "kammassa": "nghiệp",
    "cittajaṃ": "sinh từ tâm",
    "bāhiraṃ sappaṭighaṃ": "thuộc phần bên ngoài và có tính va chạm",
    "bāhiraṃ appaṭighaṃ": "thuộc phần bên ngoài và không có tính va chạm",
    "upādā sappaṭighaṃ": "phái sinh và có tính va chạm",
    "upādā appaṭighaṃ": "phái sinh và không có tính va chạm",       # also no upādā appaṭighaṃ (1-893)
    "upādiṇṇaṃ sappaṭighaṃ": "do nghiệp tạo ra và có tính va chạm",
    "upādiṇṇaṃ appaṭighaṃ": "do nghiệp tạo ra và không có tính va chạm",
    "viññeyyaṃ": "có thể nhận biết",                 # as 3-01 1-588 … 1-590
    "manasā": "ý", "viññātaṃ rūpaṃ": "vật chất được" + GAP + "nhận biết",   # «vật chất được ý nhận biết»
    "āyatanaṃ cakkhuviññeyyaṃ rūpaṃ": "lĩnh vực" + GAP + "là vật chất mà mắt có thể nhận biết",
    "āyatanaṃ manodhātuviññeyyaṃ rūpaṃ": "lĩnh vực" + GAP + "là vật chất mà yếu tố ý có thể nhận biết",
    "rūpaṃ manoviññeyyaṃ rūpaṃ": "vật chất là vật chất mà ý có thể nhận biết",
    "rūpaṃ manoviññāṇadhātuviññeyyaṃ rūpaṃ": "vật chất là vật chất mà yếu tố ý thức có thể nhận biết",
    # ---------------------------------------------------------------- headings and closing lines
    "duka": "phân loại theo nhóm hai",              # Dukaniddeso «Giải thích phân loại theo nhóm hai» (as 3-01 Dukaṃ)
    "kaṇḍe": "phần",                                # Rūpakaṇḍe «của phần về vật chất»
    "aṭṭhama": "thứ tám",
})


def context(bid, kw, k, s, text):
    """Segment rules (k: lower-cased keyword, s: lower-cased keyword set). None = no rule."""
    if kw in ("Yo", "Yā", "Yaṃ"):                   # opening relative: «Điều có ở …»; no word where the
        return "điều" if "điều có" in text.lower() else NDE   # Vietnamese starts with the item (gata strings, «… đó là …»)
    if kw in ("yo", "yaṃ"):                         # yo / yaṃ vā panaññampi atthi «hoặc bất cứ … nào khác»
        return "bất cứ" + GAP + "nào"
    if k == "saṅkha" and "bheri" in s:              # sound list «tiếng tù và»
        return "tù và"
    if k == "bhedo" and "vācā" in s:                # vacībhedo «sự phát thành lời»
        return "sự phát thành"
    if k == "hetukaṃ" and "cittajaṃ" in s:          # cittahetukaṃ «có tâm làm gốc rễ»
        return "có" + GAP + "làm gốc rễ"
    if k == "viññātaṃ" and "manasā" in s:           # «vật chất được ý nhận biết»
        return "được" + GAP + "nhận biết"
    return None


def value(k):
    """Table value of a lower-cased keyword (no segment rules)."""
    if k in RUPA:
        return RUPA[k]
    if k.startswith("rūpassa na "):                 # «không phải là sự nhẹ nhàng của vật chất»
        return "không phải là " + value("rūpassa " + k[len("rūpassa na "):])
    if k.startswith("rūpaṃ "):                      # «Vật chất nào có tính va chạm …»
        return "vật chất" + GAP + value(k[len("rūpaṃ "):])
    for table in (ADD301, MATRIX):
        if k in table:
            return table[k]
    raise KeyError(k)


def resolver_for(part):
    vi = read_vietnamese(part)

    def resolve(bid, kw, kws):
        k = lc(kw)
        s = set(lc(x) for x in kws)
        v = context(bid, kw, k, s, vi.get(bid, ""))
        if v is not None:
            return v
        try:
            return value(k)
        except KeyError:
            return ch2_value(kw, kws, T05)
    return resolve


def dump(part):
    res = resolver_for(part)
    c = Counter()
    for bid, kws in read_keywords(part):
        for kw in kws:
            try:
                c[(kw, res(bid, kw, kws))] += 1
            except KeyError:
                c[(kw, "???")] += 1
    for (kw, v), n in sorted(c.items()):
        print(f"{kw}={v}  [{n}]")


if __name__ == "__main__":
    if sys.argv[1:2] == ["dump"]:
        dump(sys.argv[2])
    else:
        for p in (sys.argv[1:] or PARTS):
            build_part(p, resolver_for(p))
            verify(p)
