"""Build the Pāli->Vietnamese keyword map for pi-5 (Kathāvatthu) chapter 24: 24-solasamavaggo.

usage: python -I -X utf8 -B map_24_vi.py                    (writes 24-solasamavaggo.mapped.md and verifies it)
       python -I -X utf8 -B map_24_vi.py show lo hi [miss]   (segments lo..hi with every pair, English | Russian and
                                                             the finished chapters' values where they differ; writes
                                                             nothing)
       python -I -X utf8 -B map_24_vi.py dump [miss]         (every distinct keyword=value; writes nothing)
       python -I -X utf8 -B map_24_vi.py look kw ...         (finished chapter tables, pi-1 … pi-4 map values)

Importing this module builds nothing (check_parts_vi.py imports it for ALLOWED).
Resolution order per keyword: OVERRIDES[bid][kw] -> context24 (segment rules of this chapter) -> T24 -> context5 ->
the finished chapter tables T21 … T2 (latest first; a value counts only where it stands in this segment, as map_21_vi)
-> map_5_vi.subject_predicate (coordinator rule) -> value5(kw, kws, T24, text) of map_sample_vi (FORMULAS -> KV ->
two-word composition -> the pi-4 chain).
Conventions: pi-1 … pi-4 vi-map-conventions*.md + notes-map-*.md, vi-map-conventions-pi5.md, map-coordinator-rules.md;
new values in notes-map-24.md.
"""
import importlib
import pathlib
import sys
from collections import Counter

sys.dont_write_bytecode = True
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai\mapper-vi")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_vi import (NDE, GAP, build_part, en_ru, join, lc, pick, present, read_keywords,  # noqa: E402,F401
                           read_vietnamese, verify)
from map_sample_vi import FORMULAS, KV, context5, value5  # noqa: E402,F401

PART = "24-solasamavaggo"

_MN = "một người"                                  # paro (the subject «Có phải một người … không?»)
_TC = "tìm cầu"
_TT = "sự thành tựu thiền"
_TS = "sự tái sinh"
_AT = "an trú trong hạnh phúc"
_DT = "ngay trong đời này"
_CH = "cõi hình sắc"
_CKH = "cõi không hình sắc"
_TD = "sự tham đắm"

T24 = {
    # ---- headings «Chương thứ mười sáu» (repeated before every discussion), «(156) 1. Bàn về sự chế ngự» … «(165) 10.
    # Bàn về những gì nằm trong cõi hình sắc và cõi không hình sắc»; closers «Phần bàn về … đã hoàn tất.»
    "soḷasamavaggo": "Chương thứ mười sáu",         # as map_17 navamavaggo / map_21 terasamavaggo
    "soḷasama": "thứ mười sáu",
    "niggahakathā": "Bàn về sự chế ngự",
    "niggaha": "sự chế ngự", "niggaho": "sự chế ngự",   # restraint of the mind (not the FORMULAS rebuttal «sự bác bỏ»,
                                                       # absent from this chapter); uddāna Cittaniggaho «Sự chế ngự tâm»
    "paggahakathā": "Bàn về sự nâng lên",
    "paggaha": "sự nâng lên",
    "paggaho": "sự nâng" + GAP + "lên",            # uddāna cittapaggaho «sự nâng tâm lên»
    "sukhānuppadānakathā": "Bàn về việc trao sự dễ chịu",
    "anuppadāna": "việc trao", "anuppadānaṃ": "việc trao",
    "sukhānuppadāna": "việc trao sự dễ chịu", "sukhānuppadānaṃ": "việc trao sự dễ chịu",
    "adhigayha": "bằng cách nắm gộp lại",
    "manasikāra": "sự chú tâm", "manasikāro": "sự chú tâm",
    "hetu": "gốc rễ",                              # Rūpaṃ hetūtikathā «… vật chất là gốc rễ» (pi-1 / pi-2; T10 / T18
                                                   # «nguyên nhân», T20 «vì» are other texts)
    "rūpaṃ hetu": "vật chất là gốc rễ",            # inner «là» kept
    "rūpārūpadhātupariyāpannakathā": "Bàn về những gì nằm trong " + _CH + " và " + _CKH,
    "rūpārūpadhātu": _CH + " và " + _CKH,
    "pariyāpanna": "nằm trong", "pariyāpanno": "nằm trong",
    # ---- 5-743 … 5-746 «Có phải một người chế ngự tâm của người khác “đừng tham đắm”, “đừng sân hận”, “đừng si mê”,
    # “đừng bị phiền não làm ô nhiễm” không? … sự tiếp xúc đã sinh khởi của người khác “đừng chấm dứt” … một người vì
    # lợi ích của người khác mà dứt bỏ … một người là người làm cho một người khác, sự dễ chịu, sự khó chịu do người
    # khác làm ra, một người làm, một người khác cảm nhận» / «nâng tâm của người khác lên … làm sinh khởi cho người khác
    # sự không tham lam, gốc rễ thiện …»
    "paro": _MN,
    "niggaṇhāti": "chế ngự", "paro niggaṇhāti": _MN + " chế ngự",
    "parassa niggaṇhāti": "chế ngự" + GAP + "người khác",   # «chế ngự tâm của người khác» (Vietnamese order)
    "paggaṇhāti": "nâng" + GAP + "lên", "paro paggaṇhāti": _MN + " nâng" + GAP + "lên",
    "parassa paggaṇhāti": "nâng" + GAP + "người khác lên",  # «nâng tâm của người khác lên»
    "paro pajahati": _MN + GAP + "dứt bỏ", "paro bhāveti": _MN + GAP + "tu tập",   # «một người vì lợi ích … mà …»
    "rajji": "tham đắm", "dussi": "sân hận", "muyhi": "si mê",   # mā rajji «đừng tham đắm» (mā = đừng, T19)
    "kilissi": "bị phiền não làm ô nhiễm",          # mā kilissī «đừng bị phiền não làm ô nhiễm» (T21 kiliṭṭho)
    "samādhi": "sự định tâm", "samādhiṃ": "sự định tâm",   # the factors as the text writes them here (T15 / T16)
    "sukhaṃ": "sự dễ chịu",                        # «sự dễ chịu, sự khó chịu do người khác làm ra», «trao sự dễ chịu»
    "sukhaṃ dukkhaṃ": "sự dễ chịu sự khó chịu",    # «sự dễ chịu, sự khó chịu» (comma dropped, pi-1)
    "paraṅkataṃ dukkhaṃ": "sự khó chịu do người khác làm ra",   # Vietnamese order (T15 parakataṃ sukhadukkhaṃ)
    "kataṃ": "làm",                                # verse Attanāva kataṃ pāpaṃ «Điều ác do chính mình làm»
    "akataṃ": "không làm",                         # own a- kept
    "pāpaṃ": "điều ác",                            # the text's «điều» kept (T21 asāta)
    "attanā": "chính mình",                        # «chính mình bị ô nhiễm», «chính mình được trong sạch»
    "visujjhati": "được trong sạch", "suddhi": "trong sạch", "asuddhi": "không trong sạch",
    "paccattaṃ": "việc riêng của mỗi người",       # «là việc riêng của mỗi người»
    "visodhaye": "làm cho" + GAP + "trong sạch",   # optative: «có thể» is frame («không ai có thể làm cho người khác
                                                   # trong sạch»)
    "bhūtā": "đã đạt được",                        # vasībhūtā «đã đạt được sự làm chủ» (5-744 / 5-746; T14 «yếu tố»
                                                   # is mahābhūtā, context24)
    "pattā": "đã đạt được",                        # balappattā «đã đạt được sức mạnh» (T13 «đã đạt đến» another text)
    "vasī": "sự làm chủ",
    "alobhaṃ": "sự không tham lam", "adosaṃ": "sự không sân hận", "amohaṃ": "sự không si mê",
    "mūlaṃ": "gốc rễ",                             # kusalamūlaṃ «gốc rễ thiện» (pi-1; T12 «gốc» another text)
    "janeti": "làm sinh khởi",
    # ---- 5-747 / 5-748 «trao cho người khác sự dễ chịu của chính mình, trao sự dễ chịu của những người khác …» /
    # «tôn giả Ưu-đà-di đã nói … Đức Thế Tôn quả thật đã loại bỏ cho chúng ta nhiều hiện tượng khó chịu, … đã mang lại
    # cho chúng ta nhiều hiện tượng dễ chịu … [Trung Bộ Kinh 2.148, trong Kinh Ví Dụ Chim Cút]»
    "anuppadeti": "trao", "sukhaṃ anuppadeti": "trao sự dễ chịu",
    "paro anuppadeti": _MN + " trao", "paro sukhaṃ anuppadeti": _MN + " trao sự dễ chịu",
    "aññesaṃ": "người khác",                       # «của những người khác» («những» dropped)
    "apahattā": "đã loại bỏ", "upahattā": "đã mang lại",
    "laṭukika": "Chim Cút", "upame": "Ví Dụ",      # laṭukikopame «Kinh Ví Dụ Chim Cút» (capitals as written, T21)
    # ---- 5-749 … 5-753 «Có phải chú tâm bằng cách nắm gộp lại không? … dùng tâm ấy mà hiểu rõ tâm ấy … dùng sự tiếp
    # xúc ấy mà chạm sự tiếp xúc ấy … trong khi chú tâm đến quá khứ là “quá khứ” … sự tụ hợp của hai sự tiếp xúc …» and
    # Dhp 277-279 «Khi nhờ trí tuệ mà thấy rằng tất cả các tạo tác đều vô thường; Thì nhàm chán khổ đau, đây là con
    # đường đến sự thanh tịnh … tất cả các hiện tượng đều không phải là tự ngã»
    "manasi karoti": "chú tâm",                    # notes-map-17 («đến» dropped)
    "manasikaronto": "trong khi chú tâm",          # participle keeps «trong khi» (coordinator rule)
    "phassena": "sự tiếp xúc", "vicārena": "sự duy trì tâm", "pītiyā": "sự hân hoan", "satiyā": "sự tỉnh thức",
    "nibbindati": "nhàm chán", "visuddhiyā": "sự thanh tịnh",   # «đến» = the dative frame
    "dukkhe": "khổ đau", "paññāya": "trí tuệ",     # «nhờ trí tuệ mà thấy» («nhờ» = the instrumental frame)
    "attā": "tự ngã",                              # of anattā «không phải là tự ngã» (positive part)
    # ---- 5-754 … 5-759 «vật chất là gốc rễ … có đối tượng, nó có sự hướng đến… sự mong cầu … các yếu tố cơ bản là
    # gốc rễ mà các vật chất phái sinh dựa vào» / «vật chất có gốc rễ … nhờ gốc rễ không tham lam … vật chất có điều kiện»
    "upādāyarūpānaṃ": "vật chất phái sinh",        # «các» dropped
    "upādāya": "phái sinh",                        # first: upādāyarūpānaṃ; CROSSCHECK «dựa vào» (upādāyahetu)
    "alobha": "không tham lam", "adosa": "không sân hận", "amoha": "không si mê",   # X-hetunā «nhờ gốc rễ X»
    "lobha": "tham lam", "dosa": "sân hận", "moha": "si mê",
    "hetunā": "gốc rễ",                            # T19
    "hetuko": "có gốc rễ",
    "māno": "sự kiêu mạn", "vicikicchā": "sự hoài nghi", "thinaṃ": "sự uể oải", "uddhaccaṃ": "sự xao động",
    "ahirikaṃ": "sự không biết hổ thẹn",
    # ---- 5-760 … 5-764 «vật chất là thiện / bất thiện … nghiệp bằng thân, nghiệp bằng lời nói vừa là thiện vừa là bất
    # thiện»
    "kāya": "thân", "vacī": "lời nói", "kāyakammaṃ": "nghiệp bằng thân", "vacīkammaṃ": "nghiệp bằng lời nói",
    # ---- 5-765 / 5-766 «vật chất được cảm nhận là dễ chịu … gắn liền với cảm giác dễ chịu … gắn liền với sự tiếp xúc
    # … gắn liền với tâm»
    "adukkhamasukhāya": "không khó chịu cũng không dễ chịu",
    # ---- 5-767 «tâm và các yếu tố đồng hành với tâm sinh khởi do nghiệp đã được tạo là quả của nghiệp»
    "uppannā": "sinh khởi",                        # no «đã» in the text
    # ---- 5-768 … 5-774 «tìm cầu sự thành tựu thiền, tìm cầu sự tái sinh, an trú trong hạnh phúc ngay trong đời này, đi
    # kèm với tâm tìm cầu sự thành tựu thiền, với tâm tìm cầu sự tái sinh, với tâm an trú trong hạnh phúc ngay trong
    # đời này, cùng sinh, hòa lẫn, gắn liền, có cùng sự sinh khởi, có cùng sự chấm dứt, có cùng chỗ dựa, có cùng đối
    # tượng»
    "esiyaṃ": _TC, "esiyo": _TC,
    "samāpatti": _TT,                              # the text's «sự» (T14 «thành tựu thiền» another text)
    "upapatti": _TS,                               # T12
    "samāpattesiyaṃ": _TC + " " + _TT, "samāpattesiyo": _TC + " " + _TT,
    "upapattesiyaṃ": _TC + " " + _TS, "upapattesiyo": _TC + " " + _TS,
    "samāpattesiyena cittena": "tâm " + _TC + " " + _TT,   # head noun first (T12 upapattesiyena cittena)
    "diṭṭhadhammasukhavihārena cittena": "tâm " + _AT + " " + _DT,
    "diṭṭhadhamma": _DT, "sukhavihāraṃ": _AT, "sukhavihāro": _AT,   # pi-2
    "vihāraṃ": "an trú", "vihāro": "an trú",
    "sahagataṃ": "đi kèm", "sahagato": "đi kèm",
    "saha": "cùng",                                # sahajātaṃ «cùng sinh» (T17); CROSSCHECK sahagataṃ «đi kèm» (first,
                                                   # no word of its own for saha)
    "jātaṃ": "sinh", "jāto": "sinh",               # T17
    "saṃsaṭṭhaṃ": "hòa lẫn", "saṃsaṭṭho": "hòa lẫn",
    "sampayuttaṃ": "gắn liền", "sampayutto": "gắn liền",
    "uppādaṃ": "sự sinh khởi", "uppādo": "sự sinh khởi",   # ekuppādaṃ «có cùng sự sinh khởi» (the text's «sự»; eka
                                                   # «cùng» no keyword, as T15 uppādā)
    "nirodhaṃ": "sự chấm dứt", "nirodho": "sự chấm dứt",
    "rūpaṃ rūpāvacaraṃ": "vật chất thuộc " + _CH, "rūpaṃ arūpāvacaraṃ": "vật chất thuộc " + _CKH,
    "katattā rūpaṃ": "đã được tạo vật chất",       # «… đã được tạo, vật chất thuộc cõi dục lạc» (adjacent, comma
                                                   # dropped, pi-3)
    "kāmāvacara": "thuộc cõi dục lạc",
    "rāgo": _TD,
    "rūparāgo rūpadhātupariyāpanno": _TD + " " + _CH + " nằm trong " + _CH,
    "arūparāgo arūpadhātupariyāpanno": _TD + " " + _CKH + " nằm trong " + _CKH,
    "kāmarāgo kāmadhātupariyāpanno": _TD + " dục lạc nằm trong cõi dục lạc",
    "saddarāgo saddadhātupariyāpanno": _TD + " âm thanh nằm trong yếu tố âm thanh",
    "phoṭṭhabbarāgo phoṭṭhabbadhātupariyāpanno": _TD + " vật xúc chạm nằm trong yếu tố vật xúc chạm",
    "saddarāgo": _TD + " âm thanh", "gandharāgo": _TD + " mùi", "rasarāgo": _TD + " vị",
    "phoṭṭhabbarāgo": _TD + " vật xúc chạm", "kāmarāgo": _TD + " dục lạc",
    "saddadhātu": "yếu tố âm thanh",               # the text's «yếu tố» (rūpadhātu «cõi hình sắc»)
    "rūpadhātu": _CH, "arūpadhātu": _CKH, "kāmadhātu": "cõi dục lạc",
    "sadda": "âm thanh", "rasa": "vị", "phoṭṭhabba": "vật xúc chạm", "kāma": "dục lạc",
    "kilesā": "phiền não",                         # «tất cả các phiền não» («các» dropped)
    "dhātu": "cõi",                                # first rūpadhātu / arūpadhātu «cõi …» (T16); CROSSCHECK 5-772 / 5-774
                                                   # saddadhātu «yếu tố âm thanh»
}

OVERRIDES = {
    "5-748": {"vata": "quả thật",                  # bahūnaṃ vata no bhagavā «Đức Thế Tôn quả thật …» (no «vata re»)
              "sukha": "dễ chịu",                  # first sukhadhammānaṃ «hiện tượng dễ chịu»; CROSSCHECK «sự dễ chịu»
                                                   # (Sukhānuppadānakathā)
              "dukkha": "khó chịu"},               # dukkhadhammānaṃ «hiện tượng khó chịu»
    "5-764": {"rūpaṃ kusalaṃ": "vật chất" + GAP + "thiện"},   # rūpaṃ kusalampi akusalampi «vật chất vừa là thiện vừa
                                                   # là bất thiện» (T16, as 5-775; «vật chất là thiện» only in the closer)
}

ALLOWED = {
}


def _tables():
    """[(chapter, table)] of the finished chapters (2 … 21)."""
    out = []
    for n in range(2, 22):
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


def context24(kw, k, kws, text):
    """Segment rules of this chapter (k: lower-cased keyword). None = no rule."""
    s = set(lc(x) for x in kws)
    if k == "sukha":               # Sukhānuppadāna «việc trao sự dễ chịu» / sukhavedaniyaṃ «… dễ chịu» /
        return pick(text, "sự dễ chịu", "dễ chịu", "hạnh phúc")   # diṭṭhadhammasukhavihāra «an trú trong hạnh phúc»
    if k == "rūpa":                # first rūparāgo «sự tham đắm cõi hình sắc» (pi-4) / rūpārūpadhātu (dhātu = cõi)
        return _CH if any(x.startswith("rūparāgo") for x in s) else "hình sắc"
    if k == "arūpa":               # first arūparāgo «sự tham đắm cõi không hình sắc» / arūpāvacara (pi-1)
        return _CKH if any(x.startswith("arūparāgo") for x in s) else "không hình sắc"
    if k in ("ārammaṇaṃ", "ārammaṇo"):             # sārammaṇaṃ / anārammaṇaṃ «có đối tượng» (T16 / T18 / T20) /
        return pick(text, "có đối tượng", "đối tượng")   # ekārammaṇaṃ «có cùng đối tượng», «là đối tượng của tâm ấy»
    if k in ("rūpaṃ kusalaṃ", "rūpaṃ akusalaṃ", "vacīkammaṃ kusalaṃ"):   # «vật chất là thiện» / «vật chất vừa là
        head = "nghiệp bằng lời nói" if k.startswith("vacī") else "vật chất"   # thiện vừa là bất thiện» (T16: «vừa»
        pred = "bất thiện" if "akusalaṃ" in k else "thiện"                   # skipped)
        return pick(text, head + " là " + pred, head + GAP + pred)
    if k == "sati":                # the factor as the text writes it («sự tỉnh thức đã sinh khởi» first in 5-743;
        return pick(text, "sự tỉnh thức", "tỉnh thức")   # CROSSCHECK «sự thiết lập tỉnh thức»)
    if k == "bhūtā" and "mahābhūtā" in s:          # mahābhūtā «các yếu tố cơ bản» (T14) / vasībhūtā «đã đạt được»
        return "yếu tố"
    return None


def resolver():
    vi = read_vietnamese(PART)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        text = vi.get(bid, "")
        k = lc(kw)
        v = context24(kw, k, kws, text)
        if v is not None:
            return v
        if k in T24:
            return T24[k]
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
        return value5(kw, kws, T24, text)
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
                src = " [T24]" if lc(kw) in T24 else (" [prior]" if p else "")
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


_FINISHED = ["preamble", "1-puggalakatha", "2-parihanikatha", "3-brahmacariyakatha", "4-jahatikatha",
             "5-sabbamatthitikatha", "6-atitakkhandhadikatha", "7-ekaccam-atthitikatha", "8-satipatthanakatha",
             "9-hevatthikatha", "10-dutiyavaggo", "11-tatiyavaggo", "12-catutthavaggo", "13-pancamavaggo",
             "14-chatthavaggo", "15-sattamavaggo", "16-atthamavaggo", "17-navamavaggo", "18-dasamavaggo",
             "19-ekadasamavaggo", "20-dvadasamavaggo", "21-terasamavaggo"]


def mlook(words):
    """values of each keyword in the finished pi-5 mapped files (named one by one; reference only)."""
    here = pathlib.Path(__file__).resolve().parent
    want = {lc(w): w for w in words}
    found = {k: Counter() for k in want}
    for part in _FINISHED:
        f = here / f"{part}.mapped.md"
        if not f.exists():
            continue
        for line in f.read_text(encoding="utf-8").split("\n"):
            if not line.startswith("["):
                continue
            _, _, rest = line.partition("] ")
            for pair in rest.split(", "):
                kw, _, v = pair.partition("=")
                if lc(kw) in found:
                    found[lc(kw)][(v, part.split("-")[0])] += 1
    for k, c in found.items():
        print(want[k], dict(c.most_common(10)))


if __name__ == "__main__":
    if sys.argv[1:2] == ["mlook"]:
        mlook(sys.argv[2:])
    elif sys.argv[1:2] == ["look"]:
        look(sys.argv[2:])
    elif sys.argv[1:2] == ["show"]:
        show(int(sys.argv[2]), int(sys.argv[3]), "miss" in sys.argv[4:])
    elif sys.argv[1:2] == ["dump"]:
        dump(sys.argv[2:3] == ["miss"])
    else:
        build_part(PART, resolver())
        verify(PART, ALLOWED)
