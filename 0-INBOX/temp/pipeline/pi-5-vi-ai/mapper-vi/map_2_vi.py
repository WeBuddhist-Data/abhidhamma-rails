"""Build the pi-5 (Kathāvatthu) Pāli->Vietnamese keyword map for chapter 2: 2-parihanikatha (Parihānikathā).

usage: python -I -X utf8 -B map_2_vi.py                 (writes 2-parihanikatha.mapped.md and verifies it)
       python -I -X utf8 -B map_2_vi.py dump [miss]     (every distinct keyword=value; writes nothing)

Importing this module builds nothing (check_parts_vi.py imports it for ALLOWED).
Resolution order per keyword: OVERRIDES[bid][kw] -> context2 (segment rules of this chapter) -> value5(kw, kws, T2,
text) from map_sample_vi (T2 -> context5 -> FORMULAS -> KV -> two-word composition -> the pi-4 chain).
Conventions: pi-1 … pi-4 vi-map-conventions*.md + notes-map-*.md, vi-map-conventions-pi5.md; new values in
notes-map-2.md.
"""
import pathlib
import sys
from collections import Counter

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_vi import GAP, NDE, build_part, lc, pick, present, read_keywords, read_vietnamese, verify  # noqa: E402
from map_sample_vi import value5  # noqa: E402

PART = "2-parihanikatha"

_ARA = "bậc A-la-hán"
_ANA = "bậc không trở lại"
_SAK = "bậc trở lại một lần"
_SOT = "bậc vào dòng"
_SVT = "được giải thoát theo từng thời điểm"

# ---------------------------------------------------------------------------- chapter-2 values
T2 = {
    # ---- headings «Bàn về sự suy thoái», «Sự suy thoái xét theo lập luận», «… xét qua đối chiếu các bậc thánh»,
    # «… xét qua chứng cứ từ kinh»
    "parihāni": "sự suy thoái",
    "yutti": "lập luận",
    "vāda": NDE,                                   # Vādayutti «lập luận»: vāda has no word of its own
    "saṃsandana": "đối chiếu",                     # (5-264 saṃsandanaṃ «Sự đối chiếu» = FORMULAS)
    "ariya": "bậc thánh", "puggala": "bậc",        # «các bậc thánh» (pi-4: ariya = bậc thánh where only ariyapuggala;
                                                   # puggalo = bậc where the segment has no «người»)
    "sādhana": "chứng cứ",
    # ---- the ariya persons and their fruits («bậc A-la-hán sa sút khỏi trạng thái A-la-hán»)
    "arahattā": "trạng thái A-la-hán",             # ablative «khỏi» = frame (vietnamese-style: arahatta = the state …)
    "arahato": _ARA, "arahatā": _ARA,              # «của bậc A-la-hán», «bậc A-la-hán đã thấy khổ đau»
    "anāgāmissa": _ANA, "anāgāminā": _ANA,
    "sakadāgāmissa": _SAK, "sakadāgāminā": _SAK,
    "sotāpannassa": _SOT, "sotāpannena": _SOT,
    "phalā": "thành quả", "phalehi": "thành quả",  # «bốn thành quả», members of X-phalā (pi-4 phala)
    "anāgāmiphalā": "thành quả không trở lại", "sakadāgāmiphalā": "thành quả trở lại một lần",
    "sotāpattiphalā": "thành quả vào dòng",
    "anāgāmiphale": "thành quả không trở lại", "sakadāgāmiphale": "thành quả trở lại một lần",
    "sotāpattiphale": "thành quả vào dòng",        # «Trong thành quả …» (locative «trong» = frame)
    # ---- sa sút / suy thoái
    "parihāyamāno": "khi sa sút",                  # participle keeps «khi» (sample vediyamāno)
    "parihīno": "bị sa sút",                       # «bị sa sút khỏi địa vị phú hộ»
    "parihīne": "mất đi",                          # satasahasse parihīne «khi mất đi một trăm nghìn» (loc. abs.,
                                                   # «khi» dropped as sample uppanne / niruddhe)
    "parihāyituṃ": "sa sút",                       # bhabbo … parihāyituṃ «có khả năng sa sút»
    "parihānāya": "sự suy thoái",                  # «dẫn đến sự suy thoái»
    "arahā parihāyamāno": _ARA + " khi sa sút",    # «bậc A-la-hán, khi sa sút» (comma dropped)
    "anāgāmī parihāyamāno": _ANA + " khi sa sút", "sakadāgāmī parihāyamāno": _SAK + " khi sa sút",
    "sotāpanno parihāyamāno": _SOT + " khi sa sút",
    "arahanto parihāyanti": _ARA + GAP + "sa sút",  # «tất cả các bậc A-la-hán đều sa sút»
    # ---- 5-239 the rich man «một phú hộ giữ địa vị phú hộ nhờ có bốn trăm nghìn»
    "seṭṭhī": "phú hộ", "seṭṭhittaṃ": "địa vị phú hộ", "kārento": "giữ",
    "sata": "trăm", "sahassehi": "nghìn", "sāpateyyā": "tài sản",
    # ---- 5-241 «đứng vững ở đâu? Trong thành quả … đứng vững trong địa vị của người phàm phu … ngay sau thành quả
    # vào dòng, vị ấy tự mình chứng nghiệm chính trạng thái A-la-hán»
    "saṇṭhāti": "đứng vững", "puthujjana": "người phàm phu", "puthu": "phàm phu", "jana": "người",
    "anantarā": "ngay sau",                        # eva: context2
    "sacchikaroti": "tự mình chứng nghiệm",
    # ---- 5-242 … «phiền não của ai đã được dứt bỏ nhiều hơn»
    "pahīnā": "đã được dứt bỏ", "pahīno": "đã được dứt bỏ",
    "bahutarā kilesā pahīnā": "phiền não" + GAP + "đã được dứt bỏ nhiều hơn",
    # ---- 5-244 … «sự tu tập các chi phần giác ngộ của ai vượt trội hơn»
    "adhimattā": "vượt trội hơn",
    "adhimattā bojjhaṅgabhāvanā": "sự tu tập các chi phần giác ngộ" + GAP + "vượt trội hơn",
    "bojjha": "giác ngộ", "aṅga": "chi phần", "pāda": "nền tảng", "indriya": "năng lực", "bala": "sức mạnh",
    "balā": "sức mạnh",
    # ---- 5-251 … «sự tham đắm dẫn đến cõi khổ», «sự tham đắm dục lạc ở dạng thô», «ác ý ở dạng nhỏ nhiệm»
    "apāya": "cõi khổ", "gamanīyo": "dẫn đến",
    "oḷāriko": "ở dạng thô", "oḷāriko byāpādo": "ác ý ở dạng thô",   # Vietnamese order (pi-2 oḷārika)
    "aṇu": "nhỏ nhiệm",                            # aṇusahagato «ở dạng nhỏ nhiệm» (member)
    "ottappaṃ": "biết ghê sợ tội lỗi",             # fragment of anottappaṃ «sự không biết ghê sợ tội lỗi» (pi-1)
    "māno": "sự kiêu mạn", "māna": "kiêu mạn",     # «sự kiêu mạn đã được dứt bỏ» / «khuynh hướng tiềm ẩn kiêu mạn»
    # ---- 5-260 «đã được dứt bỏ, đã bị cắt đứt tận gốc, đã bị làm cho như cây thốt nốt bị chặt ngọn, đã bị làm cho
    # không còn hiện hữu, có bản chất không nảy sinh trong tương lai … để dứt bỏ sự tham đắm, bậc A-la-hán đã tu tập
    # con đường»
    "mūlo": "gốc", "tāla": "cây thốt nốt", "vatthu": "ngọn",   # tālāvatthukato «như cây thốt nốt bị chặt ngọn»
    "anabhāvaṅkato": "đã bị làm cho không còn hiện hữu",
    "uppāda": "nảy sinh",                          # fragment of anuppāda «không nảy sinh» (positive part)
    "pahānāya": "dứt bỏ",                          # «để dứt bỏ» (pi-4: dative «để» = frame)
    "rāgappahānāya": "dứt bỏ sự tham đắm", "dosappahānāya": "dứt bỏ sự sân hận",
    "anottappapahānāya": "dứt bỏ sự không biết ghê sợ tội lỗi",
    "arahato bhāvito": _ARA + " đã tu tập",        # «bậc A-la-hán đã tu tập con đường» (passive rendered active)
    "bojjhaṅgā bhāvitā": "đã tu tập các chi phần giác ngộ",
    "paṭṭhānā": "sự thiết lập", "padhānā": "nỗ lực",
    # ---- 5-261 the arahant formula
    "vīta": "đã lìa", "vītadoso": "đã lìa sân hận", "vītamoho": "đã lìa si mê",
    "kata": "đã làm xong",                         # katakaraṇīyo «đã làm xong việc cần làm»
    "ohita": "đã đặt" + GAP + "xuống", "bhāro": "gánh nặng",   # «đã đặt gánh nặng xuống»
    "attho": "mục đích",                           # anuppattasadattho «đã đạt đến mục đích của chính mình»
    "pari": "hoàn toàn", "khīṇa": "đã diệt tận",   # parikkhīṇa- «đã diệt tận hoàn toàn»
    "saṃyojano": "xiềng xích",
    "aññā": "hiểu biết trọn vẹn",                  # sammadaññāvimutto «được giải thoát nhờ hiểu biết trọn vẹn»
    "ukkhitta": "đã nhấc bỏ", "paligho": "thanh chắn",
    "saṅkiṇṇa": "đã lấp", "parikho": "hào",
    "abbūḷha": "đã nhổ", "esiko": "cột trụ",
    "aggaḷo": "then cửa",                          # niraggaḷo «đã tháo then cửa»
    "ariyo": "bậc thánh",
    "panna": "đã hạ", "dhajo": "ngọn cờ",          # pannaddhajo «đã hạ ngọn cờ» (pannabhāro «đã buông bỏ gánh nặng»)
    "visaññutto": "đã thoát khỏi trói buộc",
    "su": "trọn vẹn", "vijita": "đã chiến thắng", "vijayo": "chiến thắng",   # suvijitavijayo «đã chiến thắng trọn vẹn»
    "pariññātaṃ": "đã được hiểu biết trọn vẹn",
    "sacchikato": "đã được tự mình chứng nghiệm",
    "nirodho sacchikato": "sự chấm dứt đã được tự mình chứng nghiệm",
    "abhiññeyyaṃ": "điều cần được hiểu biết trực tiếp",
    "sacchikātabbaṃ": "điều cần được tự mình chứng nghiệm",
    # ---- 5-262 / 5-263 «bậc A-la-hán được giải thoát theo từng thời điểm …»
    "samaya": "thời điểm",                         # pi-4 member
    "samayavimutto": _SVT, "samayavimuttassa": _SVT,
    "samayavimutto arahā": _ARA + " " + _SVT, "samayavimuttassa arahato": _ARA + " " + _SVT,
    "samayavimutto parihāyati": _SVT + " sa sút",
    "vimutto na parihāyati": "được giải thoát" + GAP + "không sa sút",
    "vimuttassa bhāvito": "được giải thoát" + GAP + "đã tu tập",
    # ---- 5-264 «trưởng lão Xá-lợi-phất … trưởng lão Đại Bàn-đặc đã sa sút»
    "thero": "trưởng lão",
    "sāriputto thero": "trưởng lão Xá-lợi-phất", "sāriputto thero parihāyittha": "trưởng lão Xá-lợi-phất đã sa sút",
    "sāriputto parihāyittha": "Xá-lợi-phất đã sa sút",
    "mahāpanthako thero": "trưởng lão Đại Bàn-đặc",
    "mahāpanthako thero parihāyittha": "trưởng lão Đại Bàn-đặc đã sa sút",
    "mahāpanthako parihāyittha": "Đại Bàn-đặc đã sa sút",
    "ādayo": "chỗ khác",                           # variant label «Trung Bộ Kinh 1.202 và các chỗ khác» («các» dropped)
    # ---- 5-265 verses «Quả thật, các cách thực hành cao và thấp đã được bậc sa-môn công bố; Người ta không đi đến
    # bờ bên kia hai lần, nhưng điều này cũng không được xem là chỉ một lần» [Kinh Tập 719] … «Người đã lìa khao khát,
    # không còn nắm giữ, không có việc gì cần làm; … dòng lũ và cạm bẫy đã được nhổ bỏ»
    "samaṇena": "bậc sa-môn", "pakāsitā": "đã được" + GAP + "công bố",
    "pāraṃ": "bờ bên kia", "diguṇaṃ": "hai lần", "ekaguṇaṃ": "một lần", "mutaṃ": "được xem là",
    "sutta": "kinh",                               # Suttasādhana «chứng cứ từ kinh»; suttanipāte «Kinh Tập»
    "taṇho": "khao khát", "ādāno": "nắm giữ",      # anādāno «không còn nắm giữ» (positive part)
    "vijjati": "có",                               # na vijjati «không có» (the verb's own word)
    "pāso": "cạm bẫy", "samūhato": "đã được nhổ bỏ",
    # ---- 5-266 verses «Với vị tỳ-khưu ấy, đã được giải thoát đúng đắn, có tâm an tịnh; Không có sự bồi đắp thêm cho
    # điều đã làm … Như tảng đá liền một khối, không bị gió lay động; … các vật xúc chạm … không làm rung động bậc như
    # vậy; Tâm vị ấy vững vàng, được giải thoát, và vị ấy quán sát sự suy tàn của nó»
    "paticayo": "sự bồi đắp thêm", "katassa": "điều đã làm",
    "santa": "an tịnh", "cittassa": "tâm", "bhikkhuno": "vị tỳ-khưu",
    "selo": "tảng đá", "ghano": "liền một khối", "vātena": "gió", "samīrati": "lay động",
    "phassā": "vật xúc chạm", "tādino": "bậc như vậy", "pavedhenti": "làm rung động",
    "ṭhitaṃ": "vững vàng", "vippamuttaṃ": "được giải thoát", "vayaṃ": "sự suy tàn", "anupassati": "quán sát",
    # ---- 5-267 «năm hiện tượng này dẫn đến sự suy thoái của vị tỳ-khưu được giải thoát theo từng thời điểm … Sự ưa
    # thích công việc, sự ưa thích nói chuyện, sự ưa thích ngủ nghỉ … không xem xét lại tâm»
    "kamma": "công việc", "bhassa": "nói chuyện", "niddā": "ngủ nghỉ", "ārāmatā": "sự ưa thích",
    "paccavekkhati": "xem xét lại",
    "vimuttassa bhikkhuno": "vị tỳ-khưu được giải thoát",
    "samayavimuttassa bhikkhuno": "vị tỳ-khưu " + _SVT,
    "kāmarāgapariyuṭṭhānaṃ": "sự ám ảnh của tham đắm dục lạc",
    # ---- 5-268 «bị cái gì ám ảnh mà sa sút? … Sự ám ảnh sinh khởi tùy thuộc vào cái gì? … tích lũy … giảm trừ …
    # dứt bỏ … bám víu … phân tán … gom tụ … dập tắt … nhen nhóm … mà đứng vững sau khi đã giảm trừ»
    "pariyuṭṭhito": "bị" + GAP + "ám ảnh",
    "pariyuṭṭhito parihāyati": "bị" + GAP + "ám ảnh mà sa sút",
    "paṭicca uppajjati": "sinh khởi tùy thuộc vào", "paṭicca": "tùy thuộc vào", "uppajjati": "sinh khởi",
    "paṭigha": "ác cảm", "bhavarāga": "tham đắm hiện hữu", "kāmarāga": "tham đắm dục lạc",
    "rāga": "sự tham đắm", "dosa": "sự sân hận", "moha": "sự si mê",   # «bị sự tham đắm / sân hận / si mê ám ảnh»
    "ācinati": "tích lũy", "apacinati": "giảm trừ", "apacinitvā": "sau khi đã giảm trừ",
    "pajahati": "dứt bỏ", "pajahitvā": "sau khi đã dứt bỏ", "upādiyati": "bám víu",
    "visineti": "phân tán", "visinitvā": "sau khi đã phân tán", "ussineti": "gom tụ",
    "vidhūpeti": "dập tắt", "sandhūpeti": "nhen nhóm",
    "ṭhito": "đứng vững",
}


def context2(kw, k, kws, text):
    """Segment rules of this chapter (k: lower-cased keyword). None = no rule."""
    s = set(lc(x) for x in kws)
    if k in ("rāgo", "doso", "moho"):  # «sự tham đắm …» / only «đã lìa tham đắm …» (vīta-, 5-261)
        noun = {"rāgo": "tham đắm", "doso": "sân hận", "moho": "si mê"}[k]
        return pick(text, "sự " + noun, noun)
    if k == "bhāvito":                 # «đã tu tập con đường» / «con đường đã được tu tập» (5-261)
        return pick(text, "đã tu tập", "đã được tu tập")
    if k == "maggo bhāvito":
        return pick(text, "đã tu tập con đường", "con đường đã được tu tập")
    if k == "vimuttassa":              # «… đã được giải thoát đúng đắn» (5-266) / «được giải thoát theo từng …»
        return pick(text, "đã được giải thoát đúng đắn") and "đã được giải thoát" or "được giải thoát"
    if k == "bhava":                   # «xiềng xích của sự hiện hữu» / «tham đắm hiện hữu»
        return pick(text, "sự hiện hữu", "hiện hữu")
    if k == "eva":                     # Attheva suttantoti «… thật không?» (context5) / arahattaṃyeva «chính trạng
        return "thật" if "suttanto" in s else "chính"   # thái A-la-hán» (5-241)
    if k == "vata":                  # sīlabbata «nghi thức» / tena vata re «chắc chắn»
        if "sīlabbata" in s and not present("chắc chắn", text):
            return "nghi thức"
        return "chắc chắn"
    return None


# per-segment choices (read from the segments)
OVERRIDES = {
    "5-262": {"āmantā": "Đúng vậy"},   # first occurrence «( ) [(āmantā) (Ka.)]», but the segment answers «Đúng vậy.»
                                       # elsewhere (5-112 had no other answer: NDE there)
}

# presence-check exceptions: (id, keyword) -> reason
ALLOWED = {}


def resolve(bid, kw, kws, _vi={}):
    if not _vi:
        _vi.update(read_vietnamese(PART))
    ov = OVERRIDES.get(bid, {})
    if kw in ov:
        return ov[kw]
    text = _vi.get(bid, "")
    v = context2(kw, lc(kw), kws, text)
    if v is not None:
        return v
    return value5(kw, kws, T2, text)


def dump(only_miss=False):
    vi = read_vietnamese(PART)
    c, miss, where = Counter(), Counter(), {}
    for bid, kws in read_keywords(PART):
        for kw in kws:
            try:
                v = resolve(bid, kw, kws)
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
        print(f"{kw}={v}  [{n}] {where[(kw, v)][:4]}" + (f"  MISS {m}" if m else ""))
    print("distinct", len(c), "miss-pairs", len(miss), "miss-total", sum(miss.values()))


if __name__ == "__main__":
    if sys.argv[1:2] == ["dump"]:
        dump(sys.argv[2:3] == ["miss"])
    else:
        build_part(PART, resolve)
        verify(PART, ALLOWED)
