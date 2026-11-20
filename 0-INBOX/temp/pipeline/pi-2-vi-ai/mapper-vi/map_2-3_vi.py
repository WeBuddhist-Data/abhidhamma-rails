"""Build the Pāli->Vietnamese keyword maps for pi-2 parts 2-ayatanavibhango and 3-dhatuvibhango.

usage: python -I -X utf8 map_2-3_vi.py              (writes the two <part>.mapped.md and verifies them)
       python -I -X utf8 map_2-3_vi.py dump PART [miss]   (every distinct keyword=value with count and first
                                                           segments; with «miss» only presence misses; writes nothing)

Resolution order per keyword: OVERRIDES[bid][kw] -> context() (segment rules) -> T23 (this script's table)
-> map_common_vi.value(): KH (pi-2 table) -> the approved pi-1 chain (pi1_value).
Conventions: pi-1 vi-map-conventions.md + notes-map-*.md, vi-map-conventions-pi2.md, notes-map-2-3.md.
"""
import pathlib
import sys
from collections import Counter

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_vi import (GAP, NDE, build_part, lc, present, read_keywords,  # noqa: E402
                           read_vietnamese, value, verify)

PARTS = ["2-ayatanavibhango", "3-dhatuvibhango"]

_KX = "không xác định về mặt đạo đức"

T23 = {
    # ---- Suttantabhājanīya of ch. 2 (the twelve bases)
    "dvādasāyatanāni": "mười hai lĩnh vực nhận biết",      # numeral inside the keyword: kept (as the Russian map)
    "aniccaṃ": "vô thường", "dukkhaṃ": "khổ đau", "anattā": "không phải là tự ngã",
    "vipariṇāmadhammaṃ": "có bản chất biến đổi",
    # ---- the sense-organ bodies (pi-1 ^1-596 words, as this text writes them)
    "paṇḍara": "sự sáng ngời", "khetta": "cánh đồng", "netta": "cái dẫn đường", "tīra": "bờ",
    "samuddo": "đại dương",
    "cakkhundriya": "năng lực mắt", "sotindriya": "năng lực tai", "ghānindriya": "năng lực mũi",
    "jivhindriya": "năng lực lưỡi", "jīvhindriya": "năng lực lưỡi",      # ^2-159 spelling slip, as meant
    "kāyindriya": "năng lực thân",
    "anidassanāya sappaṭighāya": "không thấy được nhưng có tính va chạm", "sappaṭighāya": "có tính va chạm",
    "sappaṭigha": "có tính va chạm",
    # ---- visible form, sound, smell, taste (ch. 2 ^2-162 … 165)
    "rūpa": "hình sắc",                                   # stem of rūpāyatana / rūpadhātu
    "vaṇṇanibhā": "ánh màu", "vaṇṇa": "màu", "nibhā": "ánh",
    "mutta": "ngọc trai", "caturassaṃ": "bốn góc",
    "dhātūnaṃ": "vật",                                    # dhātūnaṃ sannighātasaddo «tiếng va đập của các vật»
    "nigghosa": "ồn ào", "āma": "tanh", "phala": "trái cây", "khandha": "thân cây",
    "lambikaṃ": "vị chua nhẹ", "asādu": "vị không ngon",
    # ---- Abhidhammabhājanīya
    "rāga": "tham đắm", "dosa": "sân hận", "moha": "si mê",
    "arūpaṃ": "phi vật chất", "asaṅkhataṃ": "không do điều kiện tạo thành",
    "acetasikā": "không phải là yếu tố đồng hành với tâm", "cetasikaṃ": "yếu tố đồng hành với tâm",
    "nevavipākanavipākadhammadhammā": "không phải là quả của nghiệp cũng không có khả năng sinh ra quả",
    # ---- ch. 3: the six elements (pi-1 ^1-967 … 970, ^1-726, ^1-637 words)
    "dhātudvayaṃ": "yếu tố" + GAP + "có hai loại", "dvayaṃ": "có hai loại",   # «Yếu tố đất có hai loại»
    "seyyathidaṃ": "cụ thể là", "aññampi": "khác",
    "kharigataṃ": "điều được xem là rắn", "āpogataṃ": "điều được xem là nước",
    "sinehagataṃ": "điều được xem là chất ẩm", "sineho": "chất ẩm", "rūpassa": "vật chất",
    "tejogataṃ": "điều được xem là lửa", "usmāgataṃ": "điều được xem là hơi ấm",
    "usumagataṃ": "điều được xem là hơi nóng", "vāyogataṃ": "điều được xem là gió",
    "thambhitattaṃ": "trạng thái căng cứng", "ākāso": "không gian",
    "ākāsagataṃ": "điều được xem là không gian", "aghagataṃ": "điều được xem là khoảng không",
    "vivaragataṃ": "điều được xem là kẽ hở",
    # earth (internal / external)
    "kesā": "tóc", "lomā": "lông", "nakhā": "móng", "dantā": "răng", "taco": "da", "nhāru": "gân",
    "aṭṭhi": "xương", "miñjaṃ": "tủy xương", "vakkaṃ": "thận", "hadayaṃ": "tim", "yakanaṃ": "gan",
    "kilomakaṃ": "màng hoành", "pihakaṃ": "lá lách", "papphāsaṃ": "phổi", "antaṃ": "ruột",
    "antaguṇaṃ": "màng ruột", "udariyaṃ": "thức ăn trong dạ dày", "karīsaṃ": "phân",
    "ayo": "sắt", "lohaṃ": "đồng", "tipu": "thiếc", "sajjhaṃ": "bạc", "veḷuriyo": "ngọc lưu ly",
    "saṅkho": "vỏ ốc", "silā": "đá", "pavāḷaṃ": "san hô", "rajataṃ": "đồng tiền",   # harmonise D7
    "lohitaṅko": "hồng ngọc", "masāragallaṃ": "ngọc mắt mèo", "tiṇaṃ": "cỏ", "kaṭṭhaṃ": "gỗ",
    "sakkharā": "sỏi", "kaṭhalaṃ": "mảnh sành", "bhūmi": "đất", "pāsāṇo": "đá tảng", "pabbato": "núi",
    # water
    "pittaṃ": "mật", "semhaṃ": "đờm", "pubbo": "mủ", "lohitaṃ": "máu", "sedo": "mồ hôi", "medo": "mỡ",
    "assu": "nước mắt", "vasā": "mỡ lỏng", "kheḷo": "nước bọt", "siṅghāṇikā": "nước mũi",
    "lasikā": "dịch khớp", "muttaṃ": "nước tiểu",
    "bhummāni": "trên mặt đất", "udakāni": "nước", "antalikkhāni": "trên bầu trời",
    # fire
    "santappati": "ấm lên", "jīrīyati": "già đi", "pariḍayhati": "nóng rực",
    "asita": "đã ăn", "pīta": "đã uống", "khāyita": "đã nhai", "sāyitaṃ": "đã nếm",
    "pariṇāmaṃ gacchati": "được tiêu hóa", "sammā": "đúng cách",              # ^2-175 «được tiêu hóa đúng cách»
    "kaṭṭhaggi": "lửa củi", "palālaggi": "lửa rơm", "tiṇaggi": "lửa cỏ", "gomayaggi": "lửa phân bò",
    "thusaggi": "lửa trấu", "saṅkāraggi": "lửa rác", "indaggi": "lửa sét", "sannicaya": "đống",
    # wind
    "uddhaṅgamā": "đi lên", "adhogamā": "đi xuống", "gamā": "đi", "vātā": "gió",
    "kucchisayā": "trong bụng", "koṭṭhāsayā": "trong ruột", "aṅgamaṅgānusārino": "chạy khắp các chi",
    "ānusārino": "chạy khắp", "satthaka": "dao cắt", "khuraka": "dao cạo", "uppalaka": "kim châm",
    "assāso": "hơi thở vào", "puratthimā": "đông", "sarajā": "có bụi", "arajā": "không bụi",
    "sītā": "lạnh", "uṇhā": "nóng", "kāḷa": "bão", "verambha": "trên tầng cao",
    "pakkha": "cánh chim", "supaṇṇa": "chim thần Ga-ru-đa", "tālavaṇṭa": "quạt lá cọ", "vidhūpana": "quạt tay",
    # space
    "kaṇṇa": "tai", "nāsa": "mũi", "mukha": "miệng", "dvāraṃ": "cửa", "ajjhoharati": "được nuốt vào",
    "santiṭṭhati": "nằm lại", "nikkhamati": "thoát ra", "maṃsa": "thịt", "lohitehi": "máu",
    # ---- ch. 3: the second and third sixes
    "upekkhā": "bình thản", "sukha": "dễ chịu", "dukkha": "khó chịu",     # «yếu tố bình thản / dễ chịu / khó chịu»
    "sukhaṃ": "dễ chịu",                                                 # feeling string (pi-1 ^1-445)
    "dukkhaṃ vedayitaṃ": "cảm nhận" + GAP + "khó chịu", "sukhaṃ vedayitaṃ": "cảm nhận" + GAP + "dễ chịu",
    "dukkhā vedanā": "cảm giác" + GAP + "khó chịu", "sukhā vedanā": "cảm giác" + GAP + "dễ chịu",
    "cetasikaṃ asātaṃ": "sự bứt rứt trong tâm", "cetosamphassa": "sự tiếp xúc của tâm",
    "apariyogāhaṇā": "sự không đi sâu", "asaṅgāhaṇā": "sự không nắm bắt", "ānusayo": "khuynh hướng tiềm ẩn",
    "kāma": "dục lạc", "byāpāda": "ác ý", "vihiṃsā": "hãm hại", "nekkhamma": "từ bỏ",
    "abyāpāda": "không ác ý", "avihiṃsā": "không hãm hại",
    "paṭisaṃyutto": "liên quan đến", "kāmapaṭisaṃyutto": "liên quan đến dục lạc",
    "byappanā": "sự gắn tâm chặt chẽ", "nirayaṃ": "địa ngục", "uparito": "ở bên trên",
    "vasavattī deve": "chư thiên" + GAP + "Tự Tại", "yaṃ": "điều",          # «những điều trong khoảng giữa ấy»
    "dasasu": "mười", "vatthūsu": "chỗ dựa",                               # harmonise D5 «mười chỗ dựa của …»
    "manopadoso": "sự sân hận dữ dội của ý", "asuropo": "sự nói năng cộc cằn", "dussanā": "sự khởi sân",
    "pāṇinā": "tay", "leḍḍunā": "cục đất", "daṇḍena": "gậy", "satthena": "vũ khí", "rajjuyā": "dây thừng",
    "aññataraññatarena": "thứ này hay thứ khác", "sattesu": "chúng sinh", "viheṭheti": "quấy hại",
    "heṭhanā": "sự quấy hại", "viheṭhanā": "sự quấy hại nặng nề", "hiṃsanā": "sự làm hại",
    "vihiṃsanā": "sự hãm hại", "rosanā": "sự làm khổ", "parūpaghāto": "sự gây hại cho người khác",
    "ūpaghāto": "sự gây hại",
    "karuṇāyitattaṃ": "trạng thái khởi lòng trắc ẩn", "cetovimutti": "sự giải thoát của tâm",
    "mettācetovimutti": "sự giải thoát của tâm nhờ lòng từ ái",
    "karuṇācetovimutti": "sự giải thoát của tâm nhờ lòng trắc ẩn",
    # ---- ch. 3 Abhidhammabhājanīya
    "uppajjati cittaṃ": "sinh khởi tâm", "samannāhāro": "sự lưu ý", "samanantarā": "ngay sau khi",
    "niruddha": "chấm dứt", "dhātuyā": "yếu tố", "dhamme": "đối tượng của ý", "dhammesu": "hiện tượng",
    "rūpe": "hình sắc", "sadde": "âm thanh", "gandhe": "mùi", "rase": "vị", "phoṭṭhabbe": "vật xúc chạm",
    "gāmopeso": "ngôi làng", "vā pana": "hoặc",
    # ---- Pañhāpucchaka
    "cittā": "tâm",                                                      # «Bảy yếu tố là tâm»
}
_NUM = {"ekādasa": "mười một", "dvādasa": "mười hai", "dasa": "mười", "nava": "chín", "pañca": "năm",
        "soḷasa": "mười sáu", "sattarasa": "mười bảy", "pannarasa": "mười lăm", "aṭṭhārasa": "mười tám"}
for _n, _v in _NUM.items():
    T23[_n] = _v
    T23[f"{_n} dhātuyo"] = f"{_v} yếu tố"
T23.update({"dvādasannaṃ": "mười hai", "dvādasannaṃ āyatanānaṃ": "mười hai lĩnh vực nhận biết",
            "dasāyatanā": "mười lĩnh vực", "ekādasāyatanā": "mười một lĩnh vực"})
for _x, _v in (("rūpa", "vật chất"), ("vedanā", "cảm giác"), ("saññā", "tri giác"), ("saṅkhāra", "tạo tác"),
               ("viññāṇa", "thức")):
    T23[f"bahuvidhena {_x}kkhandho"] = f"khối {_v} theo nhiều nhóm"
for _org, _v in (("cakkhu", "mắt"), ("sota", "tai"), ("ghāna", "mũi"), ("jivhā", "lưỡi"), ("kāya", "thân")):
    T23[f"{_org}viññāṇadhātu"] = f"yếu tố thức qua {_v}"
for _s, _v in (("sukha", "dễ chịu"), ("dukkha", "khó chịu"), ("somanassa", "niềm vui"), ("domanassa", "nỗi buồn"),
               ("upekkhā", "bình thản"), ("avijjā", "vô minh"), ("kāma", "dục lạc"), ("byāpāda", "ác ý"),
               ("vihiṃsā", "hãm hại"), ("nekkhamma", "từ bỏ"), ("abyāpāda", "không ác ý"),
               ("avihiṃsā", "không hãm hại")):
    T23[f"{_s}dhātu"] = f"yếu tố {_v}"
for _s, _v in (("tejo", "lửa"), ("vāyo", "gió"), ("ākāsa", "không gian"), ("pathavī", "đất"), ("āpo", "nước")):
    for _side, _sv in (("ajjhattikā", "thuộc phần bên trong"), ("bāhirā", "thuộc phần bên ngoài")):
        T23[f"{_side} {_s}"] = f"{_v} {_sv}"
        T23[f"{_side} {_s}dhātu"] = f"yếu tố {_v} {_sv}"
# «X ceva X-sampayuttañca / -ttā» (singular subject forms of the pi-2 KH entries)
for _sg, _stem, _n in (("hetu ceva", "hetu", "gốc rễ"), ("āsavo ceva", "āsava", "ô nhiễm"),
                       ("saṃyojanañceva", "saṃyojana", "xiềng xích"), ("gantho ceva", "gantha", "nút thắt"),
                       ("nīvaraṇañceva", "nīvaraṇa", "chướng ngại"), ("kileso ceva", "kilesa", "phiền não")):
    for _e in ("ttañca", "ttā"):
        T23[f"{_sg} {_stem}sampayu{_e}"] = f"vừa là {_n} vừa gắn liền với {_n}"

# Pañhāpucchaka subject + predicate: «<N> lĩnh vực / yếu tố <predicate>»
_SUBJ = {"āyatanā": "lĩnh vực", "dhātuyo": "yếu tố", "dasāyatanā": "mười lĩnh vực"}

OVERRIDES = {
    # «có loại có sự dễ chịu / sự khó chịu đi kèm» (body-consciousness context, notes-2-3)
    "2-161": {"sukha": "sự dễ chịu", "dukkha": "sự khó chịu"},
    "2-154": {"Dhammā": "đối tượng của ý"},            # «Các đối tượng của ý là vô thường …»
    "2-156": {"rūpaṃ": "hình sắc"},                    # «hình sắc thấy được và có tính va chạm»
    "2-162": {"rūpaṃ": "hình sắc"},                     # «Hình sắc là ánh màu …»
    "2-163": {"saṅkha": "tù và"},                       # «tiếng tù và»
    "2-170": {"dhammā": NDE, "sukha": "hạnh phúc", "upekkhā": "sự bình thản"},   # -dhammadhammā: no word
    "2-171": {"sukha": "hạnh phúc", "upekkhā": "sự bình thản", "rūpā": "thuộc vật chất"},
    "2-174": {"raso": "nhựa"},                         # mūlaraso «nhựa rễ cây»
    "2-176": {"parittā": "nhẹ"},                       # parittā vātā «gió nhẹ»
    "2-180": {"cetasikaṃ": "trong tâm", "dukkhaṃ": "khó chịu"},   # feeling strings (pi-1 ^1-433 / ^1-445)
    "2-182": {"khandha": "khối", "sammā": "đúng đắn", "rūpā": "vật chất"},   # «tức vật chất, cảm giác …»
    "2-184": {"hadayaṃ": "tấm lòng", "uppajjitvā": "đã sinh khởi", "paṭicca": "tùy thuộc vào"},
    "2-187": {"dhammā": NDE, "sukha": "hạnh phúc", "upekkhā": "sự bình thản"},
    "2-188": {"sukha": "hạnh phúc", "upekkhā": "sự bình thản", "rūpā": "thuộc vật chất"},
}


def context(bid, kw, k, s, text):
    """Segment rules (k: lower-cased keyword, s: lower-cased keyword set). None = no rule."""
    if k in ("ārammaṇo", "ārammaṇā"):
        return "có đối tượng" if present("có đối tượng", text) else "lấy" + GAP + "làm đối tượng"
    if k in ("hetuko", "hetukā"):
        return "có gốc rễ" if present("có gốc rễ", text) else "lấy" + GAP + "làm gốc rễ"
    if k in ("yaṃ vā pana", "yo vā pana"):   # «hoặc còn có bất cứ điều gì khác» / «… bất cứ hình sắc nào khác»
        return ("hoặc" + GAP + "bất cứ điều gì" if present("bất cứ điều gì", text)
                else "hoặc" + GAP + "bất cứ" + GAP + "nào")
    if k == "viññāṇadhātu":   # «yếu tố thức» (also inside «yếu tố thức qua mắt»); only manoviññāṇadhātu: «yếu tố … thức»
        return "yếu tố thức" if present("yếu tố thức", text) else "yếu tố" + GAP + "thức"
    if k == "āyatanā" and bid in ("2-170", "2-171"):   # «Mười một lĩnh vực …» (counted subject)
        return "lĩnh vực"
    head, _, rest = k.partition(" ")
    if head in _SUBJ and rest and k not in T23:
        return _SUBJ[head] + " " + value(rest, [rest], T23, text)
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
        return value(kw, kws, T23, text)
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
