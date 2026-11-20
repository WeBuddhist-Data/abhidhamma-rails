"""Build the Pāli->Vietnamese keyword maps for pi-2 parts 13-appamannavibhango, 14-sikkhapadavibhango and
15-patisambhidavibhango.

usage: python -I -X utf8 map_13-15_vi.py                    (writes the three <part>.mapped.md and verifies them)
       python -I -X utf8 map_13-15_vi.py dump PART [miss]   (every distinct keyword=value with count and first
                                                            segments; with «miss» only presence misses; writes nothing)

Resolution order per keyword: OVERRIDES[bid][kw] -> context() (segment rules) -> T1315 (this script's table)
-> T1012 (map_10-12_vi.py) -> T79 (map_7-9_vi.py) -> T45 (map_4-5_vi.py) -> map_common_vi.value(): KH (pi-2 table)
-> the approved pi-1 chain.
Conventions: pi-1 vi-map-conventions.md + notes-map-*.md, vi-map-conventions-pi2.md, notes-map-2-3.md,
notes-map-4-5.md, notes-map-6.md, notes-map-7-9.md, notes-map-10-12.md, notes-map-13-15.md.
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


M1012 = _imp("map_1012_vi", "map_10-12_vi.py")
T45, T79, T1012, context1012 = M1012.T45, M1012.T79, M1012.T1012, M1012.context
M6 = _imp("map_6_vi", "map_6_vi.py")       # the mind-type openings (ch. 6): OBJ, prio(), selected T6 values
OBJ, prio = M6.OBJ, M6.prio

PARTS = ["13-appamannavibhango", "14-sikkhapadavibhango", "15-patisambhidavibhango"]

_KX = "không xác định về mặt đạo đức"
_AP = "trạng thái không thể đo lường"
_PS = "hiểu biết thông suốt"
_LPS = "loại hiểu biết thông suốt"
_SURA = "việc dùng rượu nấu rượu men và chất gây say dẫn đến sự buông thả"      # comma dropped
_BV = {"mettā": "lòng từ ái", "karuṇā": "lòng trắc ẩn", "muditā": "niềm vui đồng cảm", "upekkhā": "sự bình thản"}

T1315 = {
    # ================================================================ ch. 13 (Appamaññā)
    "appamaññā": _AP, "appamaññāyo": _AP, "appamaññānaṃ": _AP,
    "metti": "lòng từ ái", "mettāyanā": "sự khởi lòng từ ái", "mettāyitattaṃ": "trạng thái khởi lòng từ ái",
    "karuṇāyanā": "sự khởi lòng trắc ẩn", "karuṇāyitattaṃ": "trạng thái khởi lòng trắc ẩn",
    "muditāyanā": "sự khởi niềm vui đồng cảm", "muditāyitattaṃ": "trạng thái khởi niềm vui đồng cảm",
    "upekkhāyanā": "sự khởi bình thản", "upekkhāyitattaṃ": "trạng thái khởi bình thản",
    "vimutti": "sự giải thoát", "cetovimutti": "sự giải thoát của tâm", "ceto": "tâm",
    "sattesu": "chúng sinh",
    # the dwelling formula «an trú sau khi lan tỏa khắp một phương với tâm có X đi kèm»
    "sahagatena": "đi kèm", "cetasā": "tâm",
    "disaṃ": "phương", "ekaṃ disaṃ pharitvā": "sau khi lan tỏa khắp một phương",
    "pharitvā": "sau khi lan tỏa khắp", "pharitvā viharati": "an trú sau khi lan tỏa khắp",
    "pharati": "lan tỏa khắp", "adhimuccitvā": "sau khi quyết định",
    "pharitvā adhimuccitvā": "sau khi lan tỏa khắp sau khi quyết định",          # comma dropped
    "tathā": "cũng vậy", "tathā catutthaṃ": "cũng vậy phương thứ tư", "catutthaṃ disaṃ": "phương thứ tư",
    "tiriyaṃ": "chiều ngang", "sabbadhi": "khắp mọi nơi", "sabbattatāya": "đối với tất cả như đối với chính mình",
    "sabbāvantaṃ": "toàn thể", "sabbāvantaṃ lokaṃ": "toàn thể thế gian", "sabbāvantaṃ loka": "toàn thể thế gian",
    "vipulena": "rộng rãi", "mahaggatena": "rộng lớn", "appamāṇena": "không thể đo lường",
    "averena": "không thù địch", "abyāpajjena": "không thù hằn",
    "vipulaṃ": "rộng rãi", "mahaggataṃ": "rộng lớn", "appamāṇaṃ": "không thể đo lường",
    "avero": "không thù địch", "abyāpajjo": "không thù hằn",
    # the simile
    "puggalaṃ": "người", "piyaṃ": "đáng yêu quý", "manāpaṃ": "đáng ưa thích", "amanāpaṃ": "không đáng ưa thích",
    "disvā": "thấy", "mettāyeyya": "khởi lòng từ ái", "karuṇāyeyya": "khởi lòng trắc ẩn", "mudito": "vui mừng",
    "upekkhako": "bình thản", "duggataṃ": "khốn khổ", "durūpetaṃ": "bất hạnh",
    # ^2-644 «Một phương»
    "puratthimaṃ": "đông", "pacchimaṃ": "tây", "uttaraṃ": "bắc", "dakkhiṇaṃ": "nam", "vidisaṃ": "phương trung gian",
    "puratthimaṃ vā disaṃ": "hoặc phương đông", "pacchimaṃ vā disaṃ": "hoặc phương tây",
    "uttaraṃ vā disaṃ": "hoặc phương bắc", "dakkhiṇaṃ vā disaṃ": "hoặc phương nam",
    # ^2-646 «An trú»: the iriyati string (meditative context)
    "iriyati": "vận động", "vattati": "tiến triển", "pāleti": "gìn giữ", "yapeti": "tiếp diễn", "yāpeti": "kéo dài",
    "carati": "đi lại",
    # ^2-648 «Đây là cách nói bao hàm tất cả»
    "pariyādāya": "bao hàm tất cả", "vacana": "cách nói",
    # the citta string (^2-643)
    "tajjā": "tương ứng", "paṇḍaraṃ": "sự sáng ngời", "hadayaṃ": "tấm lòng", "mānasaṃ": "tâm trí",
    "manāyatanaṃ": "lĩnh vực ý", "manindriyaṃ": "năng lực ý", "jātaṃ": "sinh",          # sahajātaṃ «cùng sinh»
    "tena": "vì thế",
    # Abhidhamma (^2-684 …)
    "avasesā": "còn lại", "avasesā dhammā": "hiện tượng còn lại", "āvacarassa": "thuộc cõi",
    "ākusalaṃ": "bất thiện", "ākusalā": "bất thiện",                     # of nākusalaṃ «không phải bất thiện»
    "neva kusalā nākusalā": "không phải thiện không phải bất thiện",     # comma dropped (as ch. 12)
    # ================================================================ ch. 14 (Sikkhāpada)
    "sikkhāpada": "điều tu học", "sikkhāpadaṃ": "điều tu học", "sikkhāpadāni": "điều tu học",
    "sikkhāpadānaṃ": "điều tu học", "pada": "điều", "padaṃ": "điều", "padāni": "điều", "padānaṃ": "điều",
    "sikkhā": "tu học",                                                    # member; «sự tu học»: context
    "veramaṇī sikkhāpadaṃ": "điều tu học về sự kiềm chế",
    "surāmerayamajjapamādaṭṭhānā veramaṇī": "sự kiềm chế " + _SURA,
    "surā": "rượu nấu", "meraya": "rượu men", "majja": "chất gây say", "pamāda": "sự buông thả",
    "ṭṭhānā": "dẫn đến",                                                  # pamādaṭṭhānā «dẫn đến sự buông thả»
    "pāṇātipātā": "việc sát hại sinh mạng", "ātipātā": "sát hại", "musāvādā": "việc nói dối", "musā": "dối",
    "vādā": "nói", "ādānā": "lấy", "micchācārā": "hành vi sai trái", "kāmesu": "dục lạc",
    # the abstention string (pi-1 ^1-299)
    "akaraṇaṃ": "sự không làm", "akiriyā": "sự không thực hiện", "anajjhāpatti": "sự không rơi vào lỗi vi phạm",
    "anatikkamo": "sự không vượt quá", "velā": "giới hạn", "setu": "cây cầu", "ghāto": "sự phá bỏ",
    "sañcetayitattaṃ": "trạng thái đã cố ý", "cetanāya": "chủ ý",
    "kāmāvacare": "thuộc cõi dục lạc", "āvacare": "thuộc cõi",            # slip for kāmāvacaraṃ (^2-711)
    "kusalāyeva": "chỉ là thiện",
    # ================================================================ ch. 15 (Paṭisambhidā)
    "paṭisambhidā": _LPS, "paṭisambhidānaṃ": _LPS, "paṭisambhidā aniyatā": _LPS + " không cố định",
    "atthapaṭisambhidā": _PS + " về ý nghĩa", "dhammapaṭisambhidā": _PS + " về các hiện tượng",
    "niruttipaṭisambhidā": _PS + " về cách diễn đạt", "paṭibhānapaṭisambhidā": _PS + " về tài ứng đáp",
    "attha": "ý nghĩa", "atthe": "ý nghĩa", "atthaṃ": "ý nghĩa", "dhamma": "hiện tượng", "dhamme": "hiện tượng",
    "nirutti": "cách diễn đạt", "niruttiyā": "cách diễn đạt", "paṭibhāna": "tài ứng đáp",
    "ñāṇaṃ": "sự hiểu biết", "ñāṇesu": "sự hiểu biết", "ābhilāpe": "lời diễn tả",
    "paññatti": "khái niệm", "dhammānaṃ paññatti": "khái niệm về những hiện tượng",
    "jotakānī": "làm sáng tỏ", "idamatthajotakānī": "làm sáng tỏ ý nghĩa này",
    "ñāṇāni idamatthajotakānī": "sự hiểu biết này làm sáng tỏ ý nghĩa này",
    "jānāti": "biết",
    # vāra headings
    "vāro": "mục", "saṅgaha": "tổng hợp", "saṅgahavāro": "mục tổng hợp", "sacca": "sự thật",
    "saccavāro": "mục về các sự thật", "dhammavāro": "mục về các hiện tượng", "paṭicca": "tùy thuộc vào điều kiện",
    "samuppāda": "sự sinh khởi", "samuppādavāro": "mục về sự sinh khởi", "pariyatti": "việc học hỏi Giáo Pháp",
    "pariyattivāro": "mục về việc học hỏi Giáo Pháp", "kusala": "thiện", "akusala": "bất thiện",
    "kiriya": "chức năng",
    # Sacca / Hetu / Dhamma / Paṭiccasamuppāda vāra
    "dukkhe": "khổ đau", "samudaye": "sự phát sinh", "dukkhasamudaye": "sự phát sinh của khổ đau",
    "nirodhe": "sự chấm dứt", "dukkhanirodhe": "sự chấm dứt khổ đau",
    "hetumhi": "nguyên nhân", "phale": "quả",
    "ye": "nào", "jātā": "đã sinh", "sañjātā": "đã sinh ra", "nibbattā": "đã phát khởi", "pātubhūtā": "đã xuất hiện",
    "jarā": "sự lão hóa", "maraṇe": "sự chết", "jarāmaraṇe": "sự lão hóa và sự chết",
    "jarāmaraṇe ñāṇaṃ": "sự hiểu biết về sự lão hóa và sự chết",
    "jarāmaraṇanirodhe": "sự chấm dứt sự lão hóa và sự chết",
    "jātiyā": "sự sinh", "bhave": "sự hiện hữu", "upādāne": "sự bám víu", "taṇhāya": "khao khát",
    "vedanāya": "cảm giác", "phasse": "sự tiếp xúc", "āyatane": "lĩnh vực nhận biết", "nāma": "phần tinh thần",
    "rūpe": "vật chất", "nāmarūpe": "phần tinh thần và vật chất", "viññāṇe": "thức",
    "viññāṇe ñāṇaṃ": "sự hiểu biết về thức", "saṅkhāresu": "sự tạo tác",
    "saṅkhāresu ñāṇaṃ": "sự hiểu biết về các sự tạo tác", "saṅkhāranirodhe": "sự chấm dứt các sự tạo tác",
    # Pariyatti vāra (^2-724)
    "dhammaṃ": "Giáo Pháp",                                              # dhammaṃ jānāti «biết Giáo Pháp»
    "suttaṃ": "kinh", "geyyaṃ": "văn xuôi xen kệ", "veyyākaraṇaṃ": "lời giải thích", "gāthaṃ": "kệ",
    "udānaṃ": "lời cảm hứng", "itivuttakaṃ": "lời đã được nói như vậy", "jātakaṃ": "chuyện tiền thân",
    "abbhutadhammaṃ": "chuyện kỳ diệu chưa từng có", "abbhuta": "kỳ diệu chưa từng có", "vedallaṃ": "lời vấn đáp",
    "bhāsitassa": "lời đã được nói",
    # Abhidhamma vāras
    "vipākaṃ": "quả", "vipākā": "quả", "dhātu uppannā": "yếu tố" + GAP + "sinh khởi",
    "uppajjati": "sinh khởi", "uppajjanti": "sinh khởi", "cittuppādesu": "loại tâm",
    "uppādesu": "loại",                                                    # of cittuppādesu «loại tâm» (pi-1 «loại»)
    "sampayuttesu": "gắn liền", "kusalato": "thiện", "kiriyato": "mang tính chức năng",
    "kāmāvacara": "thuộc cõi dục lạc", "maggesu": "con đường", "phalesu": "thành quả",
    # ================================================================ mind-type / jhāna openings (ch. 6 / pi-1)
    "sasaṅkhārena": "có sự thúc đẩy",                                     # uppannaṃ / uppannā: context
    "apacayagāminī": "dẫn đến sự giảm trừ", "apaṭighā": "không có tính va chạm",
    "anidassanaapaṭighā": "không thấy được và không có tính va chạm",      # ^2-749 slip, rendered as meant
    "yaṃ yaṃ": "bất cứ thứ gì", "yaṃ yaṃ vā panārabbha": "hoặc lấy bất cứ thứ gì làm đối tượng",
    "ye vā pana": "hoặc" + GAP + "bất cứ" + GAP + "nào", "samuppannā": "sinh khởi",
    "chandādhipateyyaṃ": "lấy ý muốn làm yếu tố chủ đạo",
    "vīmaṃsādhipateyyaṃ": "lấy sự thẩm xét làm yếu tố chủ đạo",
    "ūpapattiyā maggaṃ": "con đường dẫn đến tái sinh", "diṭṭhigata": "sự mắc kẹt trong các quan điểm",
    "kāmāvacarassa kusalassa": "thiện thuộc cõi dục lạc", "akusalassa": "bất thiện",
    "nevasaññānāsaññāyatanasaññāsahagataṃ":
        "có tri giác về lĩnh vực không phải tri giác cũng không phải không tri giác đi kèm",
    "suññataṃ": "tính chất trống rỗng", "bhāvitattā": "tu tập",
    "paṭigha": "sự ác cảm", "vicikicchā": "sự hoài nghi", "uddhacca": "sự xao động", "domanassa": "nỗi buồn",
}
for _x, _v in _BV.items():
    T1315[_x] = _v
    T1315[f"{_x}sahagatena"] = f"có {_v} đi kèm"
    T1315[f"{_x}sahagataṃ"] = f"có {_v} đi kèm"
    T1315[f"{_x}sahagatena cetasā"] = f"tâm có {_v} đi kèm"              # «với tâm có X đi kèm» («với» frame)
    T1315[f"{_x}cetovimutti"] = f"sự giải thoát của tâm nhờ {_v}"
for _x, _v in (("pāṇātipātā", "việc sát hại sinh mạng"), ("adinnādānā", "việc lấy của không được cho"),
               ("kāmesumicchācārā", "hành vi sai trái trong các dục lạc"), ("musāvādā", "việc nói dối"),
               ("surāmerayamajjapamādaṭṭhānā", _SURA)):
    T1315[f"{_x} veramaṇī"] = f"sự kiềm chế {_v}"


def context(bid, kw, k, s, text, kws):
    """Segment rules (k: lower-cased keyword, s: lower-cased keyword set, kws: raw keywords). None = no rule."""
    if k == "sikkhā" and "dhammā sikkhā" in s:      # «Những hiện tượng này là sự tu học»
        return "sự tu học"
    if k == "dhammā sikkhā":
        return "hiện tượng" + GAP + "sự tu học"
    if k in ("uppannaṃ", "uppannā"):  # mind-type opening «Vào lúc tâm … sinh khởi» (ch. 6) / Pañhā «đã sinh khởi»
        return "sinh khởi" if "samaye" in s else "đã sinh khởi"
    if k == "uttaraṃ":        # ^2-644 «phương bắc» / lokuttaraṃ «vượt thế gian»
        return "bắc" if "dakkhiṇaṃ" in s else "vượt"
    if k == "dukkha":         # dukkhapaṭipadaṃ «cách thực hành khó khăn» (ch. 6 rule)
        return prio(["khổ đau", "khó khăn"], text)
    if k in ("sukhaṃ", "dukkhaṃ") and "kāyaviññāṇaṃ" in s:   # body consciousness «có sự dễ chịu / khó chịu»
        return "sự dễ chịu" if k == "sukhaṃ" else "sự khó chịu"
    if k == "sukhasahagataṃ" and "kāyaviññāṇaṃ" in s:
        return "có sự dễ chịu đi kèm"
    m = re.match(r"^(rūp|sadd|gandh|ras|phoṭṭhabb|dhamm)ārammaṇ(?:aṃ|ā)$", k)
    if m:                     # «có đối tượng là hình sắc… hay đối tượng của ý» (ch. 6 rule)
        o = OBJ[m.group(1)]
        return prio([f"có đối tượng là {o}", f"có đối tượng là{GAP}{o}"], text)
    if k in ("ārammaṇaṃ", "ārammaṇā") and s & _OBJ_KWS:
        return "đối tượng"    # member of rūpārammaṇaṃ … (ch. 6 / pi-1)
    if k in ("dhammā kusalā", "dhammā akusalā", "dhammā abyākatā"):   # «Những hiện tượng này là …»
        a = {"dhammā kusalā": "thiện", "dhammā akusalā": "bất thiện", "dhammā abyākatā": _KX}[k]
        return prio([f"hiện tượng {a}", f"hiện tượng{GAP}{a}"], text)
    return context1012(bid, kw, k, s, text, kws)


_OBJ_KWS = {f"{o}ārammaṇ{e}" for o in OBJ for e in ("aṃ", "ā")}


OVERRIDES = {
    # fragment of -vipākadhammadhammā (as ^2-170, ^2-217, ^2-388, ^2-484)
    "2-701": {"dhammā": NDE},
    "2-716": {"dhammā": NDE},
    "2-749": {"dhammā": NDE},
    # heading «Mục về nguyên nhân» (Hetuvāro; the matrix hetu stays «gốc rễ»)
    "2-15-1-3-0": {"Hetu": "nguyên nhân"},
}


def resolver_for(part):
    vi = read_vietnamese(part)
    table = {**T45, **T79, **T1012, **T1315}

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        k = lc(kw)
        s = set(lc(x) for x in kws)
        text = vi.get(bid, "")
        v = context(bid, kw, k, s, text, kws)
        if v is not None:
            return v
        return value(kw, kws, table, text)
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
        dump(sys.argv[2], len(sys.argv) > 3)
    else:
        for p in PARTS:
            build_part(p, resolver_for(p))
            verify(p)
