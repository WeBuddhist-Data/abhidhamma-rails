"""Pāli->Vietnamese keyword map for pi-1 part 2-04-cittuppadakandam.

usage: python -I -X utf8 map_2-04_vi.py   (writes 2-04-cittuppadakandam.mapped.md and verifies it)

Importing this file writes nothing.
Resolution order per keyword: OVERRIDES[bid][kw] -> context() -> the 2-02/2-03 context() ->
T (= the 2-02/2-03 table + ADD) via ch2_value.
Conventions: vi-map-conventions.md (approved sample), notes-map-2-02_2-03.md; new decisions: notes-map-2-04.md.
"""
import importlib.util
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from map_common_vi import GAP, build_part, ch2_value, lc, verify  # noqa: E402

_spec = importlib.util.spec_from_file_location("map_2_02_2_03_vi", HERE / "map_2-02_2-03_vi.py")
_prev = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_prev)          # import only: its __main__ block does not run

PART = "2-04-cittuppadakandam"

# New keys only (keys that already exist in the earlier tables are changed per segment below, never here).
ADD = {
    # ---------------------------------------------------------------- headings and colophons
    "akusalāni": "bất thiện",                           # «Mười hai loại tâm bất thiện» (citta implied)
    "dvādasa": "mười hai", "akusalacittāni": "loại tâm bất thiện",
    "abyākata": "không xác định về mặt đạo đức",
    "abyākatavipāko": "quả của nghiệp không xác định về mặt đạo đức",   # «Quả của nghiệp, không xác định …»
    "vipāka": "quả của nghiệp", "vipākā": "quả của nghiệp", "vipākāni": "quả của nghiệp",
    "kusalavipāka": "quả của nghiệp thiện", "kusalavipākā": "quả của nghiệp thiện",
    "kusalavipākāni": "quả của nghiệp thiện",
    "viññāṇāni": "loại thức",
    "vipākapañcaviññāṇāni": "năm loại thức là quả của nghiệp",
    "vipākāni pañcaviññāṇāni": "năm loại thức là quả của nghiệp",
    "manodhātu": "yếu tố ý",
    "vipākamanodhātu": "yếu tố ý là quả của nghiệp", "vipākā manodhātu": "yếu tố ý là quả của nghiệp",
    "vipākamanoviññāṇadhātu": "yếu tố ý thức là quả của nghiệp",
    "vipākā manoviññāṇadhātu": "yếu tố ý thức là quả của nghiệp",
    "vipākā upekkhāsahagatā manoviññāṇadhātu":
        "yếu tố ý thức là quả của nghiệp" + GAP + "có sự bình thản đi kèm",
    "sahagatā": "đi kèm", "somanassasahagatā": "có niềm vui đi kèm",
    "upekkhāsahagatā": "có sự bình thản đi kèm",
    "mahāvipākā": "quả nghiệp lớn",
    # ---------------------------------------------------------------- the unwholesome frame
    "akusalā": "bất thiện", "akusala": "bất thiện", "dhammā akusalā": "hiện tượng bất thiện",
    "akusalaṃ cittaṃ": "tâm bất thiện", "cittaṃ uppannaṃ": "tâm" + GAP + "sinh khởi",
    "dhammārammaṇaṃ": "đối tượng của ý", "dhammārammaṇā": "đối tượng của ý",
    "diṭṭhigata": "sự mắc kẹt trong các quan điểm",
    "diṭṭhigatavippayuttaṃ": "không gắn liền với sự mắc kẹt trong các quan điểm",
    "domanassasahagataṃ": "có nỗi buồn đi kèm", "domanassa": "nỗi buồn", "paṭigha": "sự ác cảm",
    # ---------------------------------------------------------------- unwholesome factors
    "micchādiṭṭhi": "quan điểm sai lầm", "micchāsaṅkappo": "tư duy sai lầm",
    "micchāvāyāmo": "nỗ lực sai lầm", "micchāsamādhi": "định tâm sai lầm",
    "ahirika": "không biết hổ thẹn", "ahirikaṃ": "sự không biết hổ thẹn",
    "ahirikabalaṃ": "sức mạnh không biết hổ thẹn",
    "anottappa": "không biết ghê sợ tội lỗi", "anottappaṃ": "sự không biết ghê sợ tội lỗi",
    "anottappabalaṃ": "sức mạnh không biết ghê sợ tội lỗi",
    "ottappitabbena": "điều đáng ghê sợ",
    "lobho": "sự tham lam", "abhijjhā": "sự thèm muốn", "moho": "sự si mê",
    "doso": "sự sân hận", "byāpādo": "sự ác ý", "vicikicchā": "sự hoài nghi",
    "uddhaccaṃ": "sự xao động",
    "tivaṅgiko": "gồm ba chi phần", "duvaṅgiko": "gồm hai chi phần", "hetu": "gốc rễ",
    # ---------------------------------------------------------------- the diṭṭhi string (1-381, 1-392)
    "diṭṭhigataṃ": "sự mắc kẹt trong các quan điểm", "gahanaṃ": "rừng rậm", "kantāro": "hoang mạc",
    "visūkāyikaṃ": "sự quanh co", "vipphanditaṃ": "sự dao động", "saṃyojanaṃ": "xiềng xích",
    "diṭṭhisaṃyojanaṃ": "xiềng xích quan điểm", "gāho": "sự nắm giữ", "patiṭṭhāho": "sự bám chặt",
    "abhiniveso": "sự cố chấp", "parāmāso": "sự hiểu sai lệch", "kummaggo": "con đường lệch lạc",
    "patho": "lối đi", "micchāpatho": "lối đi sai lầm", "micchattaṃ": "sự sai lầm",
    "tittha": "học thuyết ngoại đạo",                   # of titthāyatanaṃ «nền tảng của các học thuyết ngoại đạo»
    "vipariyāsa": "điều đảo ngược", "vipariyāsaggāho": "sự nắm giữ điều đảo ngược",
    # ---------------------------------------------------------------- the lobha string (1-389, 1-391)
    "sārāgo": "sự say đắm", "akusalamūlaṃ": "gốc rễ bất thiện",
    # ---------------------------------------------------------------- the moha string (1-390)
    "aññāṇaṃ": "sự không biết", "ñāṇaṃ": "biết",        # fragment of aññāṇaṃ
    "dassanaṃ": "thấy",                                 # of adassanaṃ «sự không thấy»
    "anabhisamayo": "sự không thấu hiểu",
    "anubodho": "hiểu ra",                              # of ananubodho «sự không hiểu ra»
    "sambodho": "tỉnh ngộ",                             # of asambodho «sự không tỉnh ngộ»
    "appaṭivedho": "sự không thấu triệt", "asaṃgāhanā": "sự không nắm bắt",
    "pariyogāhanā": "đi sâu",                           # of apariyogāhanā «sự không đi sâu»
    "samapekkhanā": "xem xét",                          # of asamapekkhanā «sự không xem xét»
    "paccavekkhanā": "xem xét lại",                     # of apaccavekkhanā «sự không xem xét lại»
    "paccakkhakammaṃ": "tự mình thấy rõ",               # of apaccakkhakammaṃ «sự không tự mình thấy rõ»
    "dummejjhaṃ": "sự ngu muội", "bālyaṃ": "sự khờ dại",
    "pamoho": "sự mê muội", "sammoho": "sự mê lầm", "avijjā": "vô minh",
    "ogho": "dòng lũ", "yogo": "ách", "anusayo": "khuynh hướng tiềm ẩn",
    "pariyuṭṭhānaṃ": "sự ám ảnh", "laṅgī": "then cài",
    # ---------------------------------------------------------------- painful mental feeling (1-415 … 1-417)
    "cetasikaṃ dukkhaṃ": "sự khó chịu trong tâm", "dukkhā vedanā": "cảm giác" + GAP + "khó chịu",
    # ---------------------------------------------------------------- the dosa string (1-418, 1-419)
    "dussitattaṃ": "trạng thái khởi sân", "byāpatti": "sự thù hằn", "byāpajjanā": "sự khởi thù hằn",
    "virodho": "sự chống đối", "paṭivirodho": "sự đối nghịch", "caṇḍikkaṃ": "sự hung dữ",
    "asuropo": "sự thô lỗ", "anattamanatā": "sự không hài lòng",
    # ---------------------------------------------------------------- the vicikicchā string (1-425)
    "kaṅkhā": "sự nghi ngờ", "kaṅkhāyanā": "sự khởi nghi ngờ", "vimati": "sự phân vân",
    "dveḷhakaṃ": "sự lưỡng lự", "dvedhā": "ngã ba",     # dvedhāpatho «sự đứng trước ngã ba đường»
    "saṃsayo": "sự ngờ vực", "anekaṃsaggāho": "sự không nắm giữ được điều chắc chắn",
    "ekaṃsa": "điều chắc chắn",                         # of anekaṃsa-
    "āsappanā": "sự chần chừ", "parisappanā": "sự do dự", "thambhitattaṃ": "trạng thái cứng đờ",
    "vilekho": "sự giằng xé",                           # manovilekho «sự giằng xé trong ý»
    # ---------------------------------------------------------------- the uddhacca string (1-429)
    "avūpasamo": "sự không lắng xuống", "vikkhepo": "sự tán loạn", "bhantattaṃ": "trạng thái rối loạn",
    # ---------------------------------------------------------------- results of wholesome action
    "kusalassa": "thiện", "kusalassa kammassa": "nghiệp thiện",
    "katattā": "đã được tạo", "upacitattā": "tích lũy",   # «đã được tạo và tích lũy»
    "kāmāvacarassa": "thuộc cõi dục lạc", "avacarassa": "thuộc cõi",
    "rūpāvacarassa": "thuộc cõi hình sắc", "arūpāvacarassa": "thuộc cõi không hình sắc",
    "abyākatā": "không xác định về mặt đạo đức",
    "dhammā abyākatā": "hiện tượng không xác định về mặt đạo đức",
    "abyākatamūlaṃ": "gốc rễ không xác định về mặt đạo đức",
    "cakkhuviññāṇaṃ": "thức qua mắt", "cakkhuviññāṇa": "thức qua mắt",
    "cakkhuviññāṇadhātu": "yếu tố thức qua mắt",
    "sotaviññāṇaṃ": "thức qua tai", "ghānaviññāṇaṃ": "thức qua mũi", "jivhāviññāṇaṃ": "thức qua lưỡi",
    "kāyaviññāṇaṃ": "thức qua thân", "kāyaviññāṇa": "thức qua thân",
    "kāyaviññāṇadhātu": "yếu tố thức qua thân",
    "sukhasahagataṃ": "có hạnh phúc đi kèm",
    "kāyikaṃ": "nơi thân",                              # «sự khoan khoái nơi thân» (as cetasikaṃ = trong tâm)
    "kāyasamphassajaṃ": "sinh từ sự tiếp xúc của thân", "kāyasamphassajā": "sinh từ sự tiếp xúc của thân",
    "uppannā": "sinh khởi", "dhātu uppannā": "yếu tố" + GAP + "sinh khởi",
    "ārammaṇā": "đối tượng",
    "sampayuttā": "gắn liền", "vippayuttā": "không gắn liền",
    "ñāṇavippayuttā": "không gắn liền với hiểu biết",
    "asaññā": "không tri giác",                         # of nevasaññānāsaññā «… không phải không tri giác»
}
T = {**_prev.T, **ADD}
assert not set(ADD) & set(_prev.T), set(ADD) & set(_prev.T)

OVERRIDES = {
    "1-374": {"sukhaṃ": "hạnh phúc"},          # the sukha heading «hạnh phúc là gì?» (as 2-01 1-10 / 1-87)
    "1-478": {"sukhaṃ": "hạnh phúc"},
    "1-416": {"dukkhaṃ": "sự đau khổ"},        # the dukkha heading «sự đau khổ là gì?» (same rule)
    "1-390": {"sampajaññaṃ": "hiểu biết rõ ràng"},   # of asampajaññaṃ «sự thiếu hiểu biết rõ ràng» (1-M2-129)
    "1-425": {"patho": "đường"},               # dvedhāpatho «sự đứng trước ngã ba đường»
    "1-430": {"cittāni": "loại tâm"},          # colophon «Mười hai loại tâm bất thiện» (2-01: «Tám tâm …»)
    "1-443": {"sukha": "hạnh phúc"},           # sukhasahagataṃ «có hạnh phúc đi kèm»
    "1-445": {"sukhaṃ": "dễ chịu"},            # kāyikaṃ sukhaṃ «sự dễ chịu nơi thân»
    "1-452": {"sukhaṃ": "dễ chịu", "sukha": "dễ chịu"},   # «năng lực dễ chịu», «sự dễ chịu nơi thân»
}
# upekkhā occurs only inside «năng lực bình thản» (the upekkhindriya headings; as 2-01 1-154)
for _b in ("1-407", "1-440", "1-466", "1-495"):
    OVERRIDES.setdefault(_b, {})["upekkhā"] = "bình thản"


def context(bid, k, s):
    """Context rules for 2-04 (k: lower-cased keyword, s: lower-cased keyword set). None = no rule."""
    if k == "dukkhaṃ":                                   # factor «sự đau khổ» / feeling string «khó chịu»
        return "khó chịu" if "cetasikaṃ dukkhaṃ" in s else "sự đau khổ"
    # the positive lobha / dosa strings keep «sự» (the earlier tables hold the fragments of a-lobha / a-dosa)
    if k == "lubbhanā" and "alobho" not in s:
        return "sự khởi lòng tham"
    if k == "sārajjanā" and "alobho" not in s:
        return "sự bị cuốn hút"
    if k == "dussanā" and "adoso" not in s:
        return "sự khởi sân"
    return _prev.context(bid, k, s)


def resolve(bid, kw, kws):
    ov = OVERRIDES.get(bid, {})
    if kw in ov:
        return ov[kw]
    s = set(lc(x) for x in kws)
    v = context(bid, lc(kw), s)
    if v is not None:
        return v
    return ch2_value(kw, kws, T)


if __name__ == "__main__":
    build_part(PART, resolve)
    verify(PART)
