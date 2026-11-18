"""Pāli->Vietnamese keyword maps for pi-1 parts 2-02-cittuppadakandam and 2-03-cittuppadakandam.

usage: python -I -X utf8 map_2-02_2-03_vi.py [PART ...]   (writes <part>.mapped.md and verifies it)

Importing this file writes nothing.
Resolution order per keyword: OVERRIDES[bid][kw] -> context() -> T (= CH2 + ADD) via ch2_value.
Conventions: vi-map-conventions.md (approved sample); new decisions: notes-map-2-02_2-03.md.
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_vi import CH2, GAP, NDE, SATI_BARE, build_part, ch2_value, lc, verify  # noqa: E402

PARTS = ["2-02-cittuppadakandam", "2-03-cittuppadakandam"]

ADD = {
    # ================================================================ 2-02
    # ---------------------------------------------------------------- headings and colophons
    "rūpāvacara": "thuộc cõi hình sắc", "arūpāvacara": "thuộc cõi không hình sắc",
    "arūpa": "không hình sắc",
    "catukka": "chia bốn", "catukkanayo": "phương pháp chia bốn",
    "pañcaka": "chia năm", "pañcakanayo": "phương pháp chia năm", "nayo": "phương pháp",
    "paṭipadā": "cách thực hành", "ārammaṇāni": "loại đối tượng",
    "soḷasakkhattukaṃ": "phân tích theo mười sáu cách",
    "soḷasakkhattukāni": "phân tích theo mười sáu cách",
    "aṭṭhakkhattukaṃ": "phân tích theo tám cách",
    "abhibhāyatanāni": "lĩnh vực chế ngự", "abhibhu": "chế ngự",
    "vimokkhāni": "sự giải thoát", "vihāra": "nơi an trú", "brahma": "cao thượng",
    "jhānāni": "tầng thiền", "asubha": "sự không đẹp đẽ", "bhūmaka": "cõi",
    # ---------------------------------------------------------------- the absorption formulas
    "upapattiyā": "tái sinh", "maggaṃ": "con đường",
    "upapattiyā maggaṃ": "con đường dẫn đến tái sinh",
    "bhāveti": "tu tập", "maggaṃ bhāveti": "tu tập con đường",
    "upasampajja": "chứng nhập", "viharati": "an trú", "upasampajja viharati": "chứng nhập và an trú",
    "kasiṇaṃ": "đề mục bao trùm", "pathavī": "đất", "āpo": "nước", "tejo": "lửa", "vāyo": "gió",
    "nīla": "màu xanh", "pīta": "màu vàng", "lohita": "màu đỏ", "odāta": "màu trắng",
    "vivicceva": "hoàn toàn tách khỏi", "kāmehi": "dục lạc",
    "vivicceva kāmehi": "hoàn toàn tách khỏi các dục lạc",
    "akusalehi": "bất thiện", "akusalehi dhammehi": "hiện tượng bất thiện",
    "vitakkaṃ": "sự hướng tâm", "vicāraṃ": "sự duy trì tâm", "vitakka": "sự hướng tâm",
    "vicāra": "sự duy trì tâm", "vicārānaṃ": "sự duy trì tâm",
    "vivekajaṃ": "sinh từ sự tách biệt", "samādhijaṃ": "sinh từ định tâm",
    "vūpasamā": "lắng xuống", "ajjhattaṃ": "bên trong", "sampasādanaṃ": "sự trong sáng",
    "ekodibhāvaṃ": "sự hợp nhất",
    "tivaṅgikaṃ": "gồm ba chi phần", "duvaṅgikaṃ": "gồm hai chi phần",
    "duvaṅgikaṃ jhānaṃ": "tầng thiền gồm hai chi phần",
    "pītiyā": "sự hân hoan", "virāgā": "phai nhạt", "upekkhako": "bình thản",
    "upekkhako ca viharati": "an trú bình thản", "sato": "tỉnh thức",
    "sampajāno": "hiểu biết rõ ràng", "sukhañca": "hạnh phúc", "kāyena": "thân",
    "paṭisaṃvedeti": "cảm nhận", "ariyā": "bậc thánh", "ācikkhanti": "mô tả",
    "pahānā": "dứt bỏ", "sukhassa": "sự dễ chịu", "sukhassa ca pahānā": "dứt bỏ sự dễ chịu",
    "dukkhassa": "sự khó chịu", "dukkha": "khó chịu", "atthaṅgamā": "biến mất",
    "domanassānaṃ": "nỗi buồn", "pārisuddhiṃ": "hoàn toàn trong sạch",
    "catutthaṃ jhānaṃ": "tầng thiền thứ tư",
    # ---------------------------------------------------------------- modes of practice, objects
    "paṭipadaṃ": "cách thực hành", "dukkhapaṭipadaṃ": "cách thực hành khó khăn",
    "sukha": "dễ dàng", "sukhapaṭipadaṃ": "cách thực hành dễ dàng",
    "abhiññaṃ": "sự hiểu biết trực tiếp", "dandha": "chậm chạp",
    "dandhābhiññaṃ": "sự hiểu biết trực tiếp chậm chạp", "khippa": "nhanh chóng",
    "khippābhiññaṃ": "sự hiểu biết trực tiếp nhanh chóng",
    "paṭipadaṃ dandha": "cách thực hành" + GAP + "chậm chạp",
    "paṭipadaṃ khippa": "cách thực hành" + GAP + "nhanh chóng",
    "parittaṃ": "hạn hẹp", "paritta": "hạn hẹp", "parittārammaṇaṃ": "có đối tượng hạn hẹp",
    "appamāṇaṃ": "không thể đo lường", "appamāṇa": "không thể đo lường",
    "appamāṇārammaṇaṃ": "có đối tượng không thể đo lường",
    # ---------------------------------------------------------------- spheres of mastery, liberations
    "parittāni": "loại hạn hẹp", "appamāṇāni": "loại không thể đo lường",
    "ajjhattaṃ arūpa": "không" + GAP + "hình sắc nơi bản thân",
    "rūpāni": "hình sắc", "saññī": "có tri giác", "rūpasaññī": "có tri giác về hình sắc",
    "bahiddhā": "ở bên ngoài bản thân", "abhibhuyya": "chế ngự", "jānāmi": "biết",
    "passāmīti": "thấy",
    "suvaṇṇa": "màu đẹp", "dubbaṇṇāni": "màu xấu",
    "nīlāni": "loại xanh", "pītāni": "loại vàng", "lohitakāni": "loại đỏ", "odātāni": "loại trắng",
    "vaṇṇāni": "màu", "nidassanāni": "trông", "nibhāsāni": "tỏa ánh",
    "rūpī": "có hình sắc", "subhanti": "đẹp đẽ",
    # ---------------------------------------------------------------- sublime abidings, the unattractive
    "mettāsahagataṃ": "có lòng từ ái đi kèm", "mettā": "lòng từ ái",
    "karuṇā": "lòng trắc ẩn", "muditā": "niềm vui đồng cảm",
    "uddhumātaka": "xác chết trương phình", "vinīlaka": "xác chết bầm tím",
    "vipubbaka": "xác chết mưng mủ", "vicchiddaka": "xác chết bị cắt đứt",
    "vikkhāyitaka": "xác chết bị thú vật ăn dở", "vikkhittaka": "xác chết bị vương vãi",
    "hata": "bị chặt", "lohitaka": "xác chết đẫm máu", "puḷavaka": "xác chết đầy giòi",
    "aṭṭhika": "bộ xương",
    # ---------------------------------------------------------------- the formless absorptions
    "sabbaso": "hoàn toàn", "samatikkamā": "vượt qua", "samatikkamma": "vượt qua",
    "saññānaṃ": "tri giác", "nānatta": "sự đa dạng",
    "manasikārā": "chú tâm",                               # of amanasikārā «không chú tâm»
    "ākāsa": "không gian", "ānañca": "vô tận",
    "ānañcāyatana": "lĩnh vực" + GAP + "vô tận", "ānañcāyatanaṃ": "lĩnh vực" + GAP + "vô tận",
    "viññāṇañca": "thức vô tận", "viññāṇañcāyatanaṃ": "lĩnh vực thức vô tận",
    "ākiñcañña": "không có gì cả", "nāsaññā": "không phải không tri giác",
    # ---------------------------------------------------------------- level and dominant factor
    "hīnaṃ": "thấp kém", "majjhimaṃ": "trung bình", "paṇītaṃ": "ưu việt",
    "chanda": "ý muốn", "adhipateyyaṃ": "làm yếu tố chủ đạo", "vīmaṃsā": "sự thẩm xét",
    # ================================================================ 2-03 (supramundane)
    # ---------------------------------------------------------------- headings and colophons
    "lokuttara": "vượt thế gian", "lokuttarakusalaṃ": "tâm thiện vượt thế gian",
    "suddhika": "đơn thuần", "suddhikapaṭipadā": "cách thực hành đơn thuần",
    "suññata": "sự trống rỗng", "mūlaka": "dựa trên", "mūlakapaṭipadā": "cách thực hành dựa trên",
    "appaṇihita": "sự không mong cầu", "vīsati": "hai mươi", "nayā": "phương pháp",
    "adhipati": "yếu tố chủ đạo",
    "lokuttaraṃ cittaṃ": "tâm vượt thế gian",
    # qualifiers of the absorption (headings «Sự trống rỗng» / «Sự không mong cầu»: see resolver)
    "suññataṃ": "tính chất trống rỗng", "appaṇihitaṃ": "tính chất không mong cầu",
    # ---------------------------------------------------------------- the opening sentence
    "lokuttaraṃ": "vượt thế gian", "lokuttaraṃ jhānaṃ": "tầng thiền vượt thế gian",
    "lokuttaraṃ jhānaṃ bhāveti": "tu tập tầng thiền vượt thế gian",
    "niyyānikaṃ": "dẫn đến giải thoát", "gāmiṃ": "dẫn đến", "apacaya": "sự giảm trừ",
    "caya": NDE,                                   # fragment of apacaya: «sự giảm trừ» is one word
    "niyyānikaṃ apacayagāmiṃ": "dẫn đến giải thoát và dẫn đến sự giảm trừ",
    "diṭṭhigatānaṃ": "sự mắc kẹt trong các quan điểm", "pahānāya": "dứt bỏ",
    "diṭṭhigatānaṃ pahānāya": "dứt bỏ sự mắc kẹt trong các quan điểm",
    "bhūmiyā": "giai đoạn", "pattiyā": "đạt đến",
    "eva": "hoàn toàn", "vivicca": "tách khỏi",     # vivicceva split: «hoàn toàn tách khỏi»
    # ---------------------------------------------------------------- the higher paths
    "aññindriyaṃ": "năng lực hiểu biết trọn vẹn", "aññā": "hiểu biết trọn vẹn",
    "rāga": "sự tham đắm", "kāmarāga": "sự tham đắm dục lạc", "byāpādānaṃ": "ác ý",
    "tanubhāvāya": "làm suy yếu",
    "avasesa": "còn sót lại",                       # of anavasesa «không còn sót lại»
    "māna": "sự kiêu mạn", "uddhacca": "sự xao động", "avijjāya": "vô minh",
    # ---------------------------------------------------------------- new factors and strings
    "anaññātaññassāmītindriyaṃ": "năng lực biết được điều chưa từng biết",
    "aññāta": "biết",                               # of anaññāta «chưa từng biết»
    "sacchikiriyāya": "tự mình chứng nghiệm", "sacchikatānaṃ": "được tự mình chứng nghiệm",
    "viditānaṃ": "được nhận biết", "ñātānaṃ": "được biết",
    "vācā": "lời nói", "vacī": "lời nói", "ājīvo": "sinh kế", "micchā": "sai lầm",
    "duccaritehi": "hành vi xấu",
    "ārati": "sự tránh xa", "virati": "sự kiêng tránh", "paṭivirati": "sự kiêng tránh hoàn toàn",
    "veramaṇī": "sự kiềm chế",
    "kiriyā": "làm", "karaṇaṃ": "thực hiện",        # of akiriyā / akaraṇaṃ «sự không làm / thực hiện»
    "ajjhāpatti": "rơi vào lỗi vi phạm",            # of anajjhāpatti
    "velā": "giới hạn", "atikkamo": "vượt quá",     # velāanatikkamo «sự không vượt quá giới hạn»
    "setu": "cây cầu", "ghāto": "sự phá bỏ",
    "samaye": "vào lúc ấy",
    "micchāājīvā ārati": "sự tránh xa sinh kế sai lầm",   # samaye X -> «vào lúc ấy … X» (ch2_value)
    "magga": "con đường", "aṅgaṃ": "chi phần", "maggaṅgaṃ": "chi phần của con đường",
    "sambojjhaṅgo": "chi phần giác ngộ", "samādhisambojjhaṅgo": "chi phần giác ngộ là định tâm",
    "vīriyasambojjhaṅgo": "chi phần giác ngộ là sự tinh tấn",
    "vicayasambojjhaṅgo": "chi phần giác ngộ là sự tìm hiểu",
    "aṭṭhaṅgiko": "gồm tám chi phần",
    # ---------------------------------------------------------------- the twenty great methods
    "maggaṃ": "con đường", "paṭṭhānaṃ": "sự thiết lập", "padhānaṃ": "nỗ lực", "iddhi": "thần thông",
    "bojjhaṅgaṃ": "chi phần giác ngộ", "saccaṃ": "sự thật", "samathaṃ": "sự tĩnh lặng",
    "khandhaṃ": "khối", "āyatanaṃ": "lĩnh vực nhận biết", "dhātuṃ": "yếu tố", "āhāraṃ": "dưỡng chất",
    "phassaṃ": "sự tiếp xúc", "vedanaṃ": "cảm giác", "saññaṃ": "tri giác", "cetanaṃ": "chủ ý",
    "ādhipateyyaṃ": "làm yếu tố chủ đạo",
}
# lokuttaraṃ X = «X vượt thế gian»; lokuttaraṃ X bhāveti = «tu tập X vượt thế gian»
_TWENTY = {"maggaṃ": "con đường", "satipaṭṭhānaṃ": "sự thiết lập tỉnh thức",
           "iddhipādaṃ": "nền tảng thần thông", "indriyaṃ": "năng lực", "balaṃ": "sức mạnh",
           "bojjhaṅgaṃ": "chi phần giác ngộ", "saccaṃ": "sự thật", "samathaṃ": "sự tĩnh lặng",
           "dhammaṃ": "hiện tượng", "khandhaṃ": "khối", "āyatanaṃ": "lĩnh vực nhận biết",
           "dhātuṃ": "yếu tố", "āhāraṃ": "dưỡng chất", "phassaṃ": "sự tiếp xúc", "vedanaṃ": "cảm giác",
           "saññaṃ": "tri giác", "cetanaṃ": "chủ ý", "cittaṃ": "tâm"}
for _p, _v in _TWENTY.items():
    ADD[f"lokuttaraṃ {_p}"] = f"{_v} vượt thế gian"
    ADD[f"lokuttaraṃ {_p} bhāveti"] = f"tu tập {_v} vượt thế gian"
T = {**CH2, **ADD}

OVERRIDES = {
    # ---- 2-02
    "1-1-2-7-0": {"parittāni": "hạn hẹp"},     # heading «Các lĩnh vực chế ngự hạn hẹp» (no «loại»)
    "1-165": {"sukhaṃ": "dễ chịu"},            # sukhaṃ of adukkhamasukhaṃ; no «hạnh phúc» in 1-165
    # ---- 2-03
    "1-286": {"sukhaṃ": "hạnh phúc"},          # the sukha heading «hạnh phúc là gì?» (as 2-01 1-10 / 1-87)
    "1-300": {"kāya": "thân"},                # tīhi kāyaduccaritehi «ba loại hành vi xấu bằng thân»
    "1-357": {"sati": SATI_BARE},              # only inside «sự thiết lập tỉnh thức»
    "1-360": {"sati": SATI_BARE},
}
# capitalised headings / colophons, distinct from the lower-case qualifier in the body
CAPS = {"Suññataṃ": "sự trống rỗng", "Appaṇihitaṃ": "sự không mong cầu"}
# 2-02: sati occurs only inside «năng lực tỉnh thức» (and sato / satimā «tỉnh thức»); 1-165 keeps
# «sự tỉnh thức» («có sự tỉnh thức hoàn toàn trong sạch nhờ sự bình thản»).
for _n in (161, 162, 163, 164, 166, 168, 169, 170, 171, 172, 173, 174, 175):
    OVERRIDES.setdefault(f"1-{_n}", {})["sati"] = SATI_BARE


def context(bid, k, s):
    """Context rules (k: lower-cased keyword, s: lower-cased keyword set). None = no rule."""
    if k in ("rūpa", "arūpa") and "rāga" in s:            # rūparāga / arūparāga (1-363)
        return "cõi hình sắc" if k == "rūpa" else "cõi không hình sắc"
    if k == "rūpa":
        if bid.startswith("1-1-"):                         # headings Rūpāvacarakusalaṃ
            return "hình sắc"
        if "arūpa" in s:                                   # rūpasaññānaṃ «các tri giác về hình sắc»
            return "hình sắc"
        if "upapattiyā" in s:                              # rūpūpapattiyā «tái sinh vào cõi hình sắc»
            return "cõi hình sắc"
    if k == "arūpa" and not bid.startswith("1-1-") and "upapattiyā" in s:
        return "cõi không hình sắc"                        # arūpūpapattiyā
    if k == "ajjhattaṃ" and "ajjhattaṃ arūpa" in s:        # ajjhattaṃ arūpasaññī «… nơi bản thân»
        return "nơi bản thân"
    if k == "dukkha" and "dukkhapaṭipadaṃ" in s:           # «cách thực hành khó khăn»
        return "khó khăn"
    if k == "āyatanāni" and "abhibhāyatanāni" in s:        # «các lĩnh vực chế ngự»
        return "lĩnh vực"
    return None


def resolver_for(part):
    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        if kw in CAPS:
            return CAPS[kw]
        s = set(lc(x) for x in kws)
        v = context(bid, lc(kw), s)
        if v is not None:
            return v
        return ch2_value(kw, kws, T)
    return resolve


if __name__ == "__main__":
    for p in (sys.argv[1:] or PARTS):
        build_part(p, resolver_for(p))
        verify(p)
