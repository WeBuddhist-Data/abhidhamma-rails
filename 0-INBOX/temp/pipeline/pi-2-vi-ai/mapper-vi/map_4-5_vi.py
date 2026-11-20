"""Build the Pāli->Vietnamese keyword maps for pi-2 parts 4-saccavibhango and 5-indriyavibhango.

usage: python -I -X utf8 map_4-5_vi.py              (writes the two <part>.mapped.md and verifies them)
       python -I -X utf8 map_4-5_vi.py dump PART [miss]   (every distinct keyword=value with count and first
                                                           segments; with «miss» only presence misses; writes nothing)

Resolution order per keyword: OVERRIDES[bid][kw] -> context() (segment rules) -> T45 (this script's table)
-> map_common_vi.value(): KH (pi-2 table) -> the approved pi-1 chain (pi1_value).
Conventions: pi-1 vi-map-conventions.md + notes-map-*.md, vi-map-conventions-pi2.md, notes-map-2-3.md,
notes-map-4-5.md.
"""
import pathlib
import sys
from collections import Counter

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_vi import (GAP, NDE, build_part, lc, present, read_keywords,  # noqa: E402
                           read_vietnamese, value, verify)

PARTS = ["4-saccavibhango", "5-indriyavibhango"]

_KX = "không xác định về mặt đạo đức"

_SKL = "sự sầu muộn sự than khóc sự khó chịu nỗi buồn và sự tuyệt vọng"     # commas dropped
_SAS = "mà là đối tượng của ô nhiễm"

T45 = {
    # ================================================================ ch. 4 (Saccavibhaṅga)
    # ---- the truths (dukkha as the truth = khổ đau; bodily pain = khó chịu by segment, see context())
    "sacca": "sự thật", "saccaṃ": "sự thật", "saccā": "sự thật", "saccāni": "sự thật", "saccānaṃ": "sự thật",
    "ariya": "cao quý", "ariyasaccaṃ": "sự thật cao quý", "ariyasaccāni": "sự thật cao quý",
    "ariyasaccānaṃ": "sự thật cao quý",
    "dukkha": "khổ đau", "dukkhaṃ": "khổ đau", "dukkhaṃ ariyasaccaṃ": "sự thật cao quý về khổ đau",
    "dukkhasaccaṃ": "sự thật về khổ đau",
    "samudaya": "sự phát sinh", "samudayaṃ": "sự phát sinh", "samudayo": "sự phát sinh", "samudaye": "sự phát sinh",
    "dukkhasamudayaṃ": "sự phát sinh của khổ đau", "dukkhasamudayo": "sự phát sinh của khổ đau",
    "dukkhasamudaye": "sự phát sinh của khổ đau",
    "dukkhanirodha": "sự chấm dứt khổ đau", "dukkhanirodhaṃ": "sự chấm dứt khổ đau",
    "dukkhanirodho": "sự chấm dứt khổ đau",
    "magga": "con đường",
    # ---- 2-190 … 2-202 (suffering)
    "jātipi": "sự sinh", "jarāpi": "sự lão hóa", "maraṇampi": "sự chết", "upāyāsāpi": "sự tuyệt vọng",  # pi: «cũng» frame
    "sokaparidevadukkhadomanassupāyāsāpi": _SKL, "sokaparidevadukkhadomanassupāyāsā": _SKL,
    "soka": "sự sầu muộn", "parideva": "sự than khóc",
    "appiyehi": "những gì mình không yêu quý", "piyehi": "những gì mình yêu quý",   # «những gì»: pronoun, kept
    "vippayogo": "xa lìa", "dukkho": "khổ đau", "labhati": "đạt được", "picchaṃ": "điều mình mong cầu",
    "saṃkhittena": "nói tóm lại", "upādāna": "sự bám víu",
    "jāti": "sự sinh", "sañjāti": "sự sinh ra", "okkanti": "sự nhập thai", "abhinibbatti": "sự hình thành",
    "pātubhāvo": "sự xuất hiện", "paṭilābho": "sự có được", "nikāye": "loài", "nikāyā": "loài",  # sattanikāye «loài chúng sinh»
    "jarā": "sự lão hóa", "vali": "nhăn nheo", "taca": "da",                     # valittacatā «da nhăn nheo»
    "cuti": "sự lìa khỏi", "cavanatā": "trạng thái lìa khỏi", "maccu": "sự tử vong", "maraṇaṃ": "sự chết",
    "kālakiriyā": "sự qua đời", "kaḷevarassa": "thân xác", "nikkhepo": "sự bỏ lại", "upacchedo": "sự cắt đứt",
    "jīvitindriya": "năng lực sống", "jīvitindriyassupacchedo": "sự cắt đứt năng lực sống",
    "ñāti": "người thân", "bhoga": "tài sản", "roga": "bệnh tật", "byasanena": "tổn hại",
    "phuṭṭhassa": "gặp phải", "byasanena vā phuṭṭhassa": "hoặc gặp phải tổn hại",
    "samannāgatassa": "vướng phải", "dhammena": "điều",                         # dukkhadhammena «điều khổ đau»
    "soko": "sự sầu muộn", "socanā": "sự buồn rầu", "anto": "bên trong", "antoparisoko": "nỗi sầu thấm sâu bên trong",
    "parijjhāyanā": "sự héo hon", "domanassaṃ": "nỗi buồn", "sallaṃ": "mũi tên",
    "ādevo": "sự kêu khóc", "paridevo": "sự than khóc", "ādevanā": "hành động kêu khóc", "vācā": "lời nói",
    "palāpo": "lời lảm nhảm", "vippalāpo": "lời lảm nhảm không ngớt", "lālappo": "sự rên rỉ",
    "āyāso": "sự phiền muộn", "upāyāso": "sự tuyệt vọng",
    "cetasikaṃ asātaṃ": "sự bứt rứt trong tâm", "cetosamphassa": "sự tiếp xúc của tâm",
    "dukkhaṃ vedayitaṃ": "cảm nhận" + GAP + "khó chịu", "dukkhā vedanā": "cảm giác" + GAP + "khó chịu",
    "yassa": "người nào", "ye vā panassa": "hoặc" + GAP + "những người" + GAP + "cho người ấy",
    "aniṭṭhā": "không đáng mong muốn", "akantā": "không đáng yêu mến", "amanāpā": "không đáng ưa thích",
    "iṭṭhā": "đáng mong muốn", "kantā": "đáng yêu mến", "manāpā": "đáng ưa thích",
    "kāmā": "mong", "anattha": "không lợi ích", "ahita": "không tốt lành", "aphāsuka": "không thoải mái",
    "ayogakkhemakāmā": "mong điều không an ổn", "phāsuka": "thoải mái", "yogakkhema": "an ổn",
    "samāgamo": "sự gần gũi", "samodhānaṃ": "sự tụ hợp", "missībhāvo": "sự hòa lẫn",
    "asamāgamo": "sự không gần gũi", "asamodhānaṃ": "sự không tụ hợp", "amissībhāvo": "sự không hòa lẫn",
    "mātā": "mẹ", "pitā": "cha", "bhātā": "anh em trai", "bhaginī": "chị em gái", "mittā": "bạn bè",
    "amaccā": "đồng sự", "ñātī": "bà con", "sālohitā": "người ruột thịt",
    "icchā": "mong muốn", "icchāya": "sự mong muốn", "pattabbaṃ": "đạt được", "byādhi": "bệnh",
    "maraṇa": "chết", "upāyāsā": "sự tuyệt vọng",
    "seyyathidaṃ": "cụ thể là",
    "rūpupādānakkhandho": "khối vật chất làm đối tượng cho sự bám víu",
    "vedanupādānakkhandho": "khối cảm giác làm đối tượng cho sự bám víu",
    "saññupādānakkhandho": "khối tri giác làm đối tượng cho sự bám víu",
    "saṅkhārupādānakkhandho": "khối tạo tác làm đối tượng cho sự bám víu",
    "viññāṇupādānakkhandho": "khối thức làm đối tượng cho sự bám víu",
    # ---- 2-203 / 2-204 (arising and cessation)
    "ponobhavikā": "dẫn đến sự hiện hữu mới", "nandi": "thích thú", "rāga": "sự tham đắm",
    "ābhinandinī": "tìm vui thích",
    "kāmataṇhā": "khao khát dục lạc", "bhavataṇhā": "khao khát được hiện hữu",
    "vibhavataṇhā": "khao khát không còn hiện hữu", "bhava": "được hiện hữu", "vibhava": "không còn hiện hữu",
    "phoṭṭhabbataṇhā": "khao khát vật xúc chạm",
    "piyarūpaṃ": "điều đáng yêu", "sātarūpaṃ": "điều khoan khoái", "nivisati": "bám rễ",
    "taṇhā uppajjamānā uppajjati": "khao khát" + GAP + "khi sinh khởi thì sinh khởi",
    "taṇhā pahīyamānā pahīyati": "khao khát" + GAP + "khi được dứt bỏ thì được dứt bỏ",
    "pahīyati": "được dứt bỏ", "nirujjhati": "chấm dứt",
    "cakkhuṃ": "mắt", "sotaṃ": "tai", "ghānaṃ": "mũi", "jivhā": "lưỡi", "kāyo": "thân", "mano": "ý",
    "manosamphasso": "sự tiếp xúc của ý",
    "asesa": "không còn dư sót", "virāga": "sự phai nhạt", "cāgo": "sự xả bỏ", "paṭinissaggo": "sự buông bỏ",
    "mutti": "sự giải thoát", "anālayo": "sự không còn bám chấp",
    # ---- 2-205 (the path, Suttanta)
    "aṭṭhaṅgiko maggo": "con đường gồm tám chi phần", "pañcaṅgiko maggo": "con đường gồm năm chi phần",
    "ñāṇaṃ": "sự hiểu biết", "nekkhamma": "sự từ bỏ", "abyāpāda": "sự không ác ý", "avihiṃsā": "sự không hãm hại",
    "musā": "nói dối", "musāvādā": "việc nói dối", "pisuṇāya": "chia rẽ", "pharusāya": "thô ác",
    "samphappalāpā": "việc nói lời phù phiếm",
    "pāṇātipātā": "việc sát hại sinh mạng", "ātipātā": "sát hại", "ādānā": "lấy",   # adinnādānā «việc lấy của …»
    "micchācārā": "hành vi sai trái", "kāmesu": "dục lạc",     # «hành vi sai trái trong các dục lạc» (harmonise-log)
    "sāvako": "vị đệ tử", "pahāya": "sau khi dứt bỏ", "kappeti": "nuôi sống",
    "chandaṃ janeti": "khởi lên ý muốn", "uppādāya": "được sinh khởi",
    "kāye": "thân", "kāye kāyānupassī": "thân" + GAP + "quán sát thân",
    "kāyānupassī viharati": "sống quán sát thân", "ānupassī": "quán sát", "vedanāsu": "cảm giác",
    "dhammesu": "hiện tượng", "ātāpī": "nhiệt tâm", "satimā": "có sự tỉnh thức", "vineyya": "sau khi chế ngự",
    "viveka": "sự tách biệt", "pītisukhaṃ": "sự hân hoan và hạnh phúc",
    "savitakkaṃ savicāraṃ": "có sự hướng tâm và sự duy trì tâm",
    "vitakkavicārānaṃ vūpasamā": "sự hướng tâm và sự duy trì tâm lắng xuống",
    "sukhavihārī": "an trú trong hạnh phúc", "sukhaṃ": "hạnh phúc",
    # ---- 2-206 … 2-214 (Abhidhammabhājanīya)
    "uttaraṃ": "vượt",                                             # lokuttaraṃ «vượt thế gian»
    "apacayagāmiṃ": "dẫn đến sự giảm trừ", "ābhiññaṃ": "sự hiểu biết trực tiếp",
    "dukkhapaṭipadaṃ dandhābhiññaṃ": "cách thực hành khó khăn và sự hiểu biết trực tiếp chậm chạp",
    "pahānaṃ": "sự dứt bỏ", "taṇhāya": "khao khát", "taṇhāya pahānaṃ": "sự dứt bỏ khao khát",
    "avasesā ca kilesā": "phiền não còn lại", "avasesā ca akusalā": "bất thiện còn lại",
    "avasesā dhammā": "hiện tượng còn lại", "akusalā dhammā": "hiện tượng bất thiện",
    "sāsavāni": "đối tượng của ô nhiễm",
    "kusalamūlāni sāsavāni": "gốc rễ thiện " + _SAS, "mūlāni sāsavāni": "gốc rễ" + GAP + _SAS,
    "sāsavā kusalā dhammā": "hiện tượng thiện" + GAP + _SAS,
    "sāsavā kusalākusalānaṃ dhammānaṃ": "hiện tượng thiện và bất thiện " + _SAS,
    "kusalākusalānaṃ": "thiện và bất thiện", "dhammānaṃ": "hiện tượng",
    "kusalākusalānaṃ dhammānaṃ vipākā": "quả của các hiện tượng thiện và bất thiện",
    "neva kusalā nākusalā": "không phải thiện không phải bất thiện",               # comma dropped
    "kāyaduccaritehi": "hành vi xấu bằng thân", "vacīduccaritehi": "hành vi xấu bằng lời nói",
    "akiriyā": "sự không làm", "akaraṇaṃ": "sự không thực hiện", "anajjhāpatti": "sự không rơi vào lỗi vi phạm",
    "anatikkamo": "sự không vượt quá",                             # velāanatikkamo «sự không vượt quá giới hạn»
    "dhammavicayasambojjhaṅgo": "chi phần giác ngộ là sự tìm hiểu các hiện tượng",
    "satisambojjhaṅgo": "chi phần giác ngộ là sự tỉnh thức",
    # ---- Pañhāpucchaka
    "saccā araṇā": "sự thật không có xung đột", "saccāni appaṭighā": "sự thật không có tính va chạm",
    "āsekkhā": "thuộc về người đã hoàn tất tu học", "arūpāni": "phi vật chất",
    "asaṅkhataṃ": "không do điều kiện tạo thành",
    "upādānañceva upādānasampayuttañca": "vừa là sự bám víu vừa gắn liền với sự bám víu",
    # ================================================================ ch. 5 (Indriyavibhaṅga)
    "bāvīsatindriyāni": "hai mươi hai năng lực", "bāvīsatīnaṃ": "hai mươi hai",       # numerals kept (notes-map-2-3)
    "bāvīsatīnaṃ indriyānaṃ": "hai mươi hai năng lực",
    "aññātāvindriyaṃ": "năng lực của người đã hiểu biết trọn vẹn",
    "rūpajīvitindriyaṃ": "năng lực sống thuộc vật chất", "arūpajīvitindriyaṃ": "năng lực sống phi vật chất",
    "rūpīnaṃ": "thuộc vật chất",                                    # «những hiện tượng thuộc vật chất ấy»
    "jīvitaṃ": "sự sống",                                           # jīvita string (pi-1)
    "itthattaṃ": "trạng thái nữ tính", "purisattaṃ": "trạng thái nam tính",
    "dhura": "gánh",                                                # anikkhittadhuratā «sự không buông bỏ gánh»
    "anikkhitta": "không buông bỏ",                                 # keeps its a- («sự không buông bỏ ý muốn»)
    "asithilaparakkamatā": "sự xông pha không lơi lỏng",
    "apilāpanatā": "sự không hời hợt", "asammussanatā": "sự không quên lãng",
    "ñātānaṃ": "đã được biết", "viditānaṃ": "đã được nhận biết", "sacchikatānaṃ": "đã được tự mình chứng nghiệm",
    "sacchikiriyāya": "tự mình chứng nghiệm",
    "suñño": "trống rỗng", "gāmopeso": "ngôi làng",                 # «đây là ngôi làng trống rỗng» (as ^2-3)
    "nevavipākanavipākadhammadhammā": "không phải là quả của nghiệp cũng không có khả năng sinh ra quả",
    "indriyā": "năng lực", "indriyā siyā": "năng lực đôi khi", "indriyā sappaṭighā": "năng lực có tính va chạm",
    "indriyā hetū": "năng lực là gốc rễ",                           # «Bốn năng lực là gốc rễ» (inner «là» kept)
    "no": "không",                                                  # «Không phải là ô nhiễm»
    "upādānā": "sự bám víu", "vicārā": "sự duy trì tâm", "vitakkā": "sự hướng tâm",
    "gantho ceva ganthasampayutta": "vừa là nút thắt vừa gắn liền với nút thắt",   # quote closed early (slip)
}
for _n, _v in (("das", "mười"), ("ekādas", "mười một"), ("dvādas", "mười hai"), ("teras", "mười ba"),
               ("cuddas", "mười bốn"), ("pannaras", "mười lăm"), ("soḷas", "mười sáu"),
               ("sattaras", "mười bảy"), ("aṭṭhāras", "mười tám"), ("ekavīsat", "hai mươi mốt")):
    T45[f"{_n}indriyā"] = f"{_v} năng lực"                          # «Mười một năng lực …» (counted subjects)
for _sg, _stem, _n in (("āsavo ceva", "āsava", "ô nhiễm"), ("saṃyojanañceva", "saṃyojana", "xiềng xích"),
                       ("nīvaraṇañceva", "nīvaraṇa", "chướng ngại"), ("kileso ceva", "kilesa", "phiền não")):
    T45[f"{_sg} {_stem}sampayuttañcā"] = f"vừa là {_n} vừa gắn liền với {_n}"   # «…ñcā"ti» spelling of ch. 5
# «X ceva X-sampayuttañca» (singular subject forms; as map_2-3_vi.py)
for _sg, _stem, _n in (("hetu ceva", "hetu", "gốc rễ"), ("āsavo ceva", "āsava", "ô nhiễm"),
                       ("saṃyojanañceva", "saṃyojana", "xiềng xích"), ("gantho ceva", "gantha", "nút thắt"),
                       ("nīvaraṇañceva", "nīvaraṇa", "chướng ngại"), ("kileso ceva", "kilesa", "phiền não"),
                       ("upādānañceva", "upādāna", "sự bám víu")):
    for _e in ("ttañca", "ttā"):
        T45[f"{_sg} {_stem}sampayu{_e}"] = f"vừa là {_n} vừa gắn liền với {_n}"

OVERRIDES = {
    "2-190": {"dukkha": "sự khó chịu"},                         # member of sokaparidevadukkha… (bodily pain)
    "2-196": {"dukkhaṃ": "khó chịu", "dukkhā": "khó chịu"},     # bodily pain (as ch. 3 ^2-180)
    "2-197": {"dukkhaṃ": "khó chịu", "dukkhā": "khó chịu", "cetasikaṃ": "trong tâm"},
    "2-201": {"uppajjati": "khởi lên", "Jarā": "già", "dukkha": "sự khó chịu"},   # jarādhammānaṃ «phải già»
    "2-202": {"dukkhā": "khổ đau"},                             # pañcupādānakkhandhā dukkhā «… là khổ đau»
    "2-203": {"Yaṃ": "điều", "rūpaṃ": "điều", "dhammā": "đối tượng của ý"},       # piya-/sātarūpaṃ «điều …»
    "2-204": {"Yaṃ": "điều", "rūpaṃ": "điều", "dhammā": "đối tượng của ý"},
    "2-205": {"viharati": "sống", "aṭṭhaṅgiko maggo": "con đường" + GAP + "gồm tám chi phần"},   # «… cao quý gồm …»
    "2-217": {"dhammā": NDE},                                   # fragment of -vipākadhammadhammā (as ^2-170)
    "2-218": {"rūpaṃ": "thuộc vật chất", "cetasikaṃ": "yếu tố đồng hành với tâm"},
    # ch. 5: feeling strings (as ch. 3 ^2-180), the vīriya string (pi-1 «sự nỗ lực»); ṭhiti: «sự ổn định» (vīriya
    # and samādhi strings; the jīvita string's «sự tồn tại» is the third occurrence, see notes-map-4-5.md)
    "2-220": {"dukkhaṃ": "khó chịu", "sukhaṃ": "dễ chịu", "sukhā vedanā": "cảm giác" + GAP + "dễ chịu",
              "cetasikaṃ": "trong tâm", "vāyāmo": "sự nỗ lực", "ṭhiti": "sự ổn định"},
    "2-223": {"dhammā": NDE},                                   # fragment of -vipākadhammadhammā (as ^2-170)
    "2-224": {"rūpā": "thuộc vật chất", "cetasikaṃ": "yếu tố đồng hành với tâm"},   # «Bảy năng lực thuộc vật chất»
}


def context(bid, kw, k, s, text):
    """Segment rules (k: lower-cased keyword, s: lower-cased keyword set). None = no rule."""
    if k in ("ārammaṇo", "ārammaṇā", "ārammaṇaṃ"):
        return "có đối tượng" if present("có đối tượng", text) else "lấy" + GAP + "làm đối tượng"
    if k in ("hetuko", "hetukā", "hetukaṃ"):
        return "có gốc rễ" if present("có gốc rễ", text) else "lấy" + GAP + "làm gốc rễ"
    if k == "sati":           # the factor «sự tỉnh thức»; only inside «tỉnh thức đúng đắn»: SATI_BARE
        return "sự tỉnh thức" if present("sự tỉnh thức", text) else "tỉnh thức"
    if k == "viharati":       # «an trú» (jhāna formula); «sống» where the text has only «sống»
        return "an trú" if present("an trú", text) else "sống"
    return None


def resolver_for(part):
    vi = read_vietnamese(part)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        k = lc(kw)
        s = set(lc(x) for x in kws)
        text = vi.get(bid, "")
        v = context(bid, kw, k, s, text)
        if v is not None:
            return v
        return value(kw, kws, T45, text)
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
        print(f"{kw}={v}  [{n}] {where[(kw, v)][:5]}" + (f"  MISS {m}" if m else ""))


if __name__ == "__main__":
    if sys.argv[1:2] == ["dump"]:
        dump(sys.argv[2], len(sys.argv) > 3)
    else:
        for p in PARTS:
            build_part(p, resolver_for(p))
            verify(p)
