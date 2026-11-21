"""Build the Pāli->Vietnamese keyword map for pi-5 (Kathāvatthu) chapter 21: 21-terasamavaggo.

usage: python -I -X utf8 -B map_21_vi.py                    (writes 21-terasamavaggo.mapped.md and verifies it)
       python -I -X utf8 -B map_21_vi.py show lo hi [miss]   (segments lo..hi with every pair, English | Russian and
                                                             the finished chapters' values where they differ; writes
                                                             nothing)
       python -I -X utf8 -B map_21_vi.py dump [miss]         (every distinct keyword=value; writes nothing)
       python -I -X utf8 -B map_21_vi.py look kw ...         (finished chapter tables, pi-1 … pi-4 map values)

Importing this module builds nothing (check_parts_vi.py imports it for ALLOWED).
Resolution order per keyword: OVERRIDES[bid][kw] -> context21 (segment rules of this chapter) -> T21 -> context5 ->
the finished chapter tables T18 … T2 (latest first; a value counts only where it stands in this segment, as map_17_vi)
-> map_5_vi.subject_predicate (coordinator rule) -> value5(kw, kws, T21, text) of map_sample_vi (FORMULAS -> KV ->
two-word composition -> the pi-4 chain).
Conventions: pi-1 … pi-4 vi-map-conventions*.md + notes-map-*.md, vi-map-conventions-pi5.md, map-coordinator-rules.md;
new values in notes-map-21.md.
"""
import importlib
import pathlib
import sys
from collections import Counter

sys.dont_write_bytecode = True
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai\mapper-vi")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_vi import (NDE, GAP, build_part, en_ru, join, lc, pick, present, read_keywords,  # noqa: E402
                           read_vietnamese, verify)
from map_sample_vi import FORMULAS, KV, context5, value5  # noqa: E402,F401

PART = "21-terasamavaggo"

_KP = "người tồn tại suốt một kiếp"                 # kappaṭṭho (agent noun with its head noun)
_NA = "người đã tiến hành nghiệp có quả không gián đoạn"   # anantarāpayutto puggalo
_NC = "người cố định"                              # niyato
_NB = "người bị ngăn che"                          # nivuto
_ND = "người đang hiện diện đối mặt"               # sammukhībhūto
_NT = "người đang nhập thành tựu thiền"            # samāpanno (ch 7)
_KD = "khao khát đối tượng của ý"                  # dhammataṇhā
_KX = "không xác định về mặt đạo đức"
_LDT = "lấy" + GAP + "làm đối tượng"

T21 = {
    # ---- headings «Chương thứ mười ba» (repeated before every discussion), «(126) 1. Bàn về người tồn tại suốt một
    # kiếp» … «(135) 10. Bàn về việc cho rằng khao khát đối tượng của ý không phải là sự phát sinh của khổ đau»;
    # closers «Phần bàn về … đã hoàn tất.» (kathā / niṭṭhitā: FORMULAS); 5-685 «Chương thứ mười ba. Tóm tắt …»
    "terasamavaggo": "Chương thứ mười ba",          # as map_17 navamavaggo
    "terasama": "thứ mười ba",
    "ṭha": "tồn tại", "ṭho": "tồn tại",            # member of kappaṭṭha(-kathā) «người tồn tại suốt một kiếp» (no head
                                                   # noun for a member, pi-4); 5-657 first kappaṭṭho (not adhammaṭṭho)
    "kusalapaṭilābhakathā": "Bàn về sự có được điều thiện",
    "paṭilābha": "sự có được",
    "payutta": "đã tiến hành", "payutto": "đã tiến hành",   # Anantarāpayutto «người đã tiến hành nghiệp …»; 5-662
                                                   # «Chẳng phải đã tiến hành nghiệp ấy sao?»
    "anantarā": "nghiệp có quả không gián đoạn",   # the member (anantariya kamma; «nghiệp» stands for it in the heading)
    "anantarāpayutto puggalo": _NA,                # Vietnamese order (head noun first)
    "nivuta": _NB, "nivuto": _NB,                  # agent noun with its head noun (pi-4 names)
    "sammukhībhūta": _ND, "sammukhībhūto": _ND,
    "samāpanno": _NT,                              # context21: «đã rơi vào» in the sutta of 5-675
    "assādeti": "thỏa thích", "samāpanno assādeti": _NT + " thỏa thích",
    "asāta": "điều không khoan khoái",             # own a- kept; the text's «điều» (asātarāgo «sự tham đắm điều không
                                                   # khoan khoái»)
    "dhammataṇhā": _KD,
    "dhammataṇhā abyākatā": _KD + " là " + _KX,    # inner «là» kept
    "dhammataṇhā akusalā": _KD + " là bất thiện",
    # ---- 5-654 … 5-657 «Có phải người tồn tại suốt một kiếp có thể tồn tại suốt một kiếp không? … kiếp hình thành
    # và Đức Phật xuất hiện trong thế gian … người tồn tại suốt một kiếp qua đời … Khi kiếp đang bị thiêu đốt, … Đi
    # khi đã chết, hay đi qua không trung? … nghiệp khiến tồn tại suốt một kiếp chín muồi trong các đời kế tiếp …»
    "kappaṭṭho tiṭṭheyya": _KP + GAP + "tồn tại",  # optative: «có thể» is frame (coordinator rule)
    "kappaṭṭho dadeyya": _KP + GAP + "thực hiện",  # first «… có thể thực hiện sự bố thí»
    "kālaṃ karoti": "qua đời",
    "ḍayhante": "khi" + GAP + "đang bị thiêu đốt",   # loc. abs. participle keeps «khi» (T17 vattamāne)
    "mato": "khi đã chết",                         # «Đi khi đã chết» (participle keeps «khi»; T18 «người đã chết»
                                                   # is another text)
    "vehāsaṃ": "không trung",
    "vepakkaṃ": "chín muồi",                       # aparāpariyavepakkaṃ «chín muồi trong các đời kế tiếp»
    "paṭiññā": "lời khẳng định",                   # in the translated note of the variant bracket (ALLOWED)
    "vādissa": "người theo học thuyết",            # paravādissa (FORMULAS vādī; ALLOWED)
    "navama": "thứ chín",                          # navamapantiyaṃ «dòng thứ chín» (T17; ALLOWED)
    "bhāvito": "đã tu tập",
    # verse 5-657 «Kẻ chia rẽ Tăng đoàn thuộc cõi khổ, thuộc địa ngục, là người tồn tại suốt một kiếp; Ưa thích bè
    # phái, đứng trên điều phi pháp, rơi khỏi điều an ổn; Sau khi chia rẽ Tăng đoàn đang hòa hợp, bị nung đốt trong
    # địa ngục suốt một kiếp»
    "āpāyiko": "thuộc cõi khổ", "nerayiko": "thuộc địa ngục",
    "rato": "ưa thích", "vagga": "bè phái",
    "khemā": "an ổn",                              # yogakkhemā «điều an ổn» («điều» belongs to the whole compound)
    "yoga": NDE,                                   # yogakkhemā: no word of its own (as T18 kammaṃ)
    "padhaṃsati": "rơi khỏi", "samaggaṃ": "đang hòa hợp", "paccati": "bị nung đốt",
    # ---- 5-658 / 5-659 «… có thể cho y phục… đồ ăn khất thực… chỗ ở… thuốc men và vật dụng chữa bệnh… món ăn cứng…
    # món ăn mềm… nước uống… có thể đảnh lễ bảo tháp… có thể dâng vòng hoa lên bảo tháp… hương thơm… dầu thoa… có
    # thể đi nhiễu quanh bảo tháp theo chiều bên phải … không thể có được tâm thiện … tâm thiện của sự xuất khỏi»
    "gilāna": "chữa bệnh",                         # map_10 (gilānapaccaya «chữa bệnh»)
    "vandeyya": "đảnh lễ", "cetiyaṃ": "bảo tháp",
    "abhidakkhiṇaṃ": "theo chiều bên phải", "kareyya": "đi nhiễu quanh",   # abhidakkhiṇaṃ kareyya
    "paṭilabheyya": "có được",                     # optative: the bare verb («không thể» = na + frame)
    "kusalaṃ paṭilabheyya": "có được" + GAP + "thiện",   # Vietnamese order («có được tâm thiện»)
    # ---- 5-660 … 5-662 «Chẳng phải nghiệp ấy đã được tiến hành, sự hối tiếc đã được làm sinh khởi, sự ân hận đã
    # được làm sinh ra sao? … không có khả năng bước vào … mẹ bị tước đoạt mạng sống … máu của Như Lai bị làm cho chảy
    # với tâm độc ác… Tăng đoàn bị chia rẽ … sau khi rút lại nghiệp ấy, xua tan sự hối tiếc, dẹp bỏ sự ân hận»
    "payuttaṃ": "đã được tiến hành",
    "kukkuccaṃ": "sự hối tiếc", "vippaṭisāriyaṃ": "sự ân hận",
    "janitaṃ": "đã được làm sinh ra",
    "okkameyya": "bước vào",                       # optative: the bare verb
    "niyāmaṃ okkameyya": "bước vào sự cố định",
    "abhabbo": "không có khả năng",                # own a- kept (pi-4 abhabba)
    "cittena uppāditaṃ": "bị làm cho chảy với tâm",   # inner «với» kept (coordinator rule)
    "saṅgho bhinno": "Tăng đoàn bị chia rẽ",
    "paṭisaṃharitvā": "sau khi rút lại",           # gerund «sau khi» (map 4); one «sau khi» for the series
    "paṭivinodetvā": "xua tan", "paṭivinetvā": "dẹp bỏ",
    # ---- 5-663 / 5-664 «người cố định theo hướng sai lầm bước vào sự cố định theo hướng đúng đắn … trước đó tu tập
    # con đường rồi sau đó bước vào sự cố định … Bồ-tát có khả năng không thấu hiểu Giáo Pháp trong đời ấy»
    "niyato": _NC,                                 # «người cố định» (pi-4 «người có hướng đi cố định» is another text)
    "niyato okkamati": _NC + " bước vào",
    "micchattaniyato": _NC + " theo hướng sai lầm", "sammattaniyato": _NC + " theo hướng đúng đắn",
    "bhāvetvā": "tu tập" + GAP + "rồi",            # «tu tập con đường rồi sau đó» (as T18 samādiyitvā «… rồi»)
    "maggaṃ bhāvetvā": "tu tập con đường rồi",
    "pacchā": "sau đó",
    "jātiyā": "đời",                               # tāya jātiyā «trong đời ấy»
    # ---- 5-665 … 5-670 «người đã tham đắm dứt bỏ sự tham đắm, người đã sân hận dứt bỏ sự sân hận, người đã si mê
    # dứt bỏ sự si mê, người đã bị phiền não làm ô nhiễm dứt bỏ các phiền não … dùng sự tham đắm mà dứt bỏ …»
    "ratto": "người đã tham đắm", "duṭṭho": "người đã sân hận", "mūḷho": "người đã si mê",
    "kiliṭṭho": "người đã bị phiền não làm ô nhiễm",
    "rāgaṃ": "sự tham đắm", "dosaṃ": "sự sân hận", "mohaṃ": "sự si mê",   # T12
    "rāgaṃ jahati": "dứt bỏ sự tham đắm",          # verb before its object, as the text («người đã tham đắm dứt bỏ»
                                                   # joins Ratto, not rāgaṃ)
    "kilese jahati": "dứt bỏ các phiền não",       # inner «các» kept (pi-1)
    "saṃyojanaṃ jahati": "dứt bỏ xiềng xích",
    "nivuto jahati": _NB + " dứt bỏ",              # subject + predicate (coordinator rule)
    "pathavī": "mặt đất",                          # Nabhañca pathavī ca «bầu trời và mặt đất» (map_18 override)
    # ---- 5-671 … 5-673 «người đang nhập thành tựu thiền thỏa thích, sự ưa thích tầng thiền lấy tầng thiền làm đối
    # tượng … dùng sự hướng tâm ấy mà hướng tâm đến … vị ấy thỏa thích với nó, ham muốn nó, và nhờ nó mà đạt đến sự
    # hài lòng»
    "jhānanikanti": "sự ưa thích tầng thiền", "nikanti": "sự ưa thích",
    "ārammaṇā": _LDT,                              # jhānārammaṇā (T11)
    "vitakkena": "sự hướng tâm",
    "nikāmeti": "ham muốn", "āpajjati": "đạt đến", "vittiṃ": "sự hài lòng",
    # ---- 5-674 / 5-675 «chúng sinh hoan hỷ với khổ đau, có những người mong ước, ước ao, tìm kiếm, truy tìm, tìm
    # cầu khổ đau … khuynh hướng tiềm ẩn tham đắm nằm sẵn trong cảm giác khó chịu … Người ấy, đã rơi vào sự thuận
    # theo và sự chống đối như vậy, … hoan hỷ với cảm giác ấy, tán thán nó» [… trong Kinh Lớn về Sự Diệt Tận Khao Khát]
    "abhinandino": "hoan hỷ",
    "patthenti": "mong ước", "esanti": "tìm kiếm", "gavesanti": "truy tìm", "pariyesanti": "tìm cầu",
    "sukhāya": "dễ chịu", "sukhāya vedanāya": "cảm giác dễ chịu",   # the feeling (KV «hạnh phúc» is the dative
                                                                  # «vì hạnh phúc»)
    "anurodha": "sự thuận theo", "virodhaṃ": "sự chống đối",
    "abhivadati": "tán thán",
    "mahā": "Lớn", "saṅkhaye": "Sự Diệt Tận",      # sutta title as written (capitals kept, as KV itivu)
    # ---- 5-676 … 5-684 «khao khát hình sắc… khao khát âm thanh… khao khát mùi… khao khát vị… khao khát vật xúc
    # chạm … Đức Thế Tôn đã nói rằng khao khát là bất thiện … rằng sự tham lam là bất thiện, khao khát đối tượng của ý
    # là sự tham lam … khao khát dẫn đến sự hiện hữu mới, đi kèm với sự thích thú và tham đắm, tìm vui thích chỗ này
    # chỗ kia»
    "rūpataṇhā": "khao khát hình sắc", "saddataṇhā": "khao khát âm thanh", "gandhataṇhā": "khao khát mùi",
    "rasataṇhā": "khao khát vị",
    "taṇhā vuttā": "đã nói rằng khao khát", "taṇhā vutto": "đã nói rằng khao khát",   # Vietnamese order, inner
    "lobho vutto": "đã nói rằng sự tham lam",      # «rằng» kept (coordinator rule)
    "vutto bhagavatā": "Đức Thế Tôn đã nói",       # FORMULAS vuttaṃ bhagavatā
    "abhinandinī": "tìm vui thích",                # tatratatrābhinandinī
    "pono": "mới", "bhavikā": "dẫn đến sự hiện hữu",   # ponobbhavikā «dẫn đến sự hiện hữu mới»
}

OVERRIDES = {
    "5-657": {"dhamma": "pháp"},                   # adhammaṭṭho «đứng trên điều phi pháp» (positive part)
    "5-673": {"eva": "hoàn toàn"},                 # first: vivicceva «hoàn toàn tách khỏi»; CROSSCHECK «thật» (Attheva
                                                   # suttanto)
    "5-675": {"taṇhā": "Khao Khát"},               # only mahātaṇhāsaṅkhaye «Kinh Lớn về Sự Diệt Tận Khao Khát»
}

_NOTE = ("is in the translated note after the colon of the variant bracket [dị bản (?): vehāsaṃ gacchatīti; vì đây "
         "chỉ là lời khẳng định của người theo học thuyết khác, như ở dòng thứ chín của Các vấn đề tranh luận "
         "621-623], which present() strips")
ALLOWED = {
    ("5-656", "paṭiññā"): "«lời khẳng định» (paṭiññāyeva) " + _NOTE,
    ("5-656", "vādissa"): "«người theo học thuyết khác» (paravādissa) " + _NOTE,
    ("5-656", "navama"): "«dòng thứ chín» (navamapantiyaṃ) " + _NOTE,
}


def _tables():
    """[(chapter, table)] of the finished chapters (2 … 18)."""
    out = []
    for n in range(2, 19):
        try:
            m = importlib.import_module(f"map_{n}_vi")
        except Exception:      # noqa: BLE001
            continue
        t = getattr(m, f"T{n}", None)
        if t:
            out.append((n, t))
    return out


_TABLES = _tables()
import map_5_vi  # noqa: E402


def context21(kw, k, kws, text):
    """Segment rules of this chapter (k: lower-cased keyword). None = no rule."""
    s = set(lc(x) for x in kws)
    if k == "uppāditaṃ":           # lohitaṃ uppāditaṃ «máu … bị làm cho chảy» (5-661) / kukkuccaṃ uppāditaṃ «sự hối
        return pick(text, "bị làm cho chảy", "đã được làm sinh khởi")   # tiếc đã được làm sinh khởi» (5-660)
    if k == "rāga":                # asātarāga «sự tham đắm điều không khoan khoái» / nandīrāga «sự thích thú và tham đắm»
        return pick(text, "sự tham đắm", "tham đắm")
    if k == "rūpa" and "rūpataṇhā" in s:           # Rūpataṇhā «khao khát hình sắc»
        return "hình sắc"
    if k == "kusala" and "paṭilābha" in s:         # heading «Bàn về sự có được điều thiện» (the text's «điều»)
        return "điều thiện"
    if k == "samāpanno" and "anurodha" in s:       # anurodhavirodhaṃ samāpanno «đã rơi vào sự thuận theo và …»
        return "đã rơi vào"
    if k == "dhammataṇhā lobho":   # «khao khát đối tượng của ý là sự tham lam» / «khao khát đối tượng của ý, sự tham
        return pick(text, _KD + " là sự tham lam", _KD + " sự tham lam")   # lam, …» (comma dropped, pi-1)
    return None


def resolver():
    vi = read_vietnamese(PART)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        text = vi.get(bid, "")
        k = lc(kw)
        v = context21(kw, k, kws, text)
        if v is not None:
            return v
        if k in T21:
            return T21[k]
        v = context5(kw, k, kws, text)
        if v is not None:
            return v
        for n, t in reversed(_TABLES):             # the finished chapters (latest first) where their value stands in
            if k in t and (t[k] == NDE or present(t[k], text)):   # this segment
                return t[k]
        if " " in kw:
            v = map_5_vi.subject_predicate(kw, kws, text)
            if v:
                return v
        return value5(kw, kws, T21, text)
    return resolve


def _prior_values(k):
    return {n: t[k] for n, t in _TABLES if k in t}


def show(lo, hi, only_miss=False):
    res = resolver()
    vi = read_vietnamese(PART)
    for i, (bid, kws) in enumerate(read_keywords(PART)):
        if lo <= i < hi:
            print(f"== {i} [{bid}]")
            er = en_ru(bid)
            for kw in kws:
                try:
                    v = res(bid, kw, kws)
                except KeyError:
                    v = "???"
                flag = "" if v == NDE or (v != "???" and present(v, vi.get(bid, ""))) else " <<MISS"
                if only_miss and not flag:
                    continue
                e = er.get(kw, ["", ""])
                p = _prior_values(lc(kw))
                ps = (" T:" + str(p)) if p and any(x != v for x in p.values()) else ""
                src = " [T21]" if lc(kw) in T21 else (" [prior]" if p else "")
                print(f"   {kw}={v}{src}  [en:{e[0]} | ru:{e[1]}]{ps}{flag}")


def dump(only_miss=False):
    res = resolver()
    vi = read_vietnamese(PART)
    c, miss, where = Counter(), Counter(), {}
    for bid, kws in read_keywords(PART):
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
    print("distinct", len(c), "miss-pairs", len(miss), "miss-total", sum(miss.values()))


def look(words):
    """Values of the finished chapter tables and of the pi-1 … pi-4 maps (reference only)."""
    from map_common_vi import pi1_map_values, pi2_map_values, pi3_map_values, pi4_map_values
    for w in words:
        k = lc(w)
        print(w, "T:", _prior_values(k), "KV:", KV.get(k), "F:", FORMULAS.get(k))
        for name, f in (("pi1", pi1_map_values), ("pi2", pi2_map_values), ("pi3", pi3_map_values),
                        ("pi4", pi4_map_values)):
            try:
                v = f(w)
            except Exception:  # noqa: BLE001
                v = None
            if v:
                print("   ", name, v)


if __name__ == "__main__":
    if sys.argv[1:2] == ["look"]:
        look(sys.argv[2:])
    elif sys.argv[1:2] == ["show"]:
        show(int(sys.argv[2]), int(sys.argv[3]), "miss" in sys.argv[4:])
    elif sys.argv[1:2] == ["dump"]:
        dump(sys.argv[2:3] == ["miss"])
    else:
        build_part(PART, resolver())
        verify(PART, ALLOWED)
