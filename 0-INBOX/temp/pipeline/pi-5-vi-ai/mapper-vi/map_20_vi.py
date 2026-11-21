"""Build the Pāli->Vietnamese keyword map for pi-5 (Kathāvatthu) chapter 20: 20-dvadasamavaggo.

usage: python -I -X utf8 -B map_20_vi.py                    (writes 20-dvadasamavaggo.mapped.md and verifies it)
       python -I -X utf8 -B map_20_vi.py show lo hi [miss]   (segments lo..hi with every pair; writes nothing)
       python -I -X utf8 -B map_20_vi.py dump [miss]         (every distinct keyword=value; writes nothing)
       python -I -X utf8 -B map_20_vi.py prior kw ...        (the finished chapters' table values; writes nothing)

Importing this module builds nothing (check_parts_vi.py imports it for ALLOWED).
Resolution order per keyword: OVERRIDES[bid][kw] -> context20 (segment rules) -> T20 -> map_5_vi.subject_predicate ->
value5(kw, kws, PRIOR, text) of map_sample_vi, where PRIOR = the finished chapter tables (T2 … T16, T18; as map_16_vi /
map_18_vi) under T20.
Conventions: pi-1 … pi-4 vi-map-conventions*.md + notes-map-*.md, vi-map-conventions-pi5.md, map-coordinator-rules.md;
new values in notes-map-20.md.
"""
import importlib
import pathlib
import sys
from collections import Counter

sys.dont_write_bytecode = True
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai\mapper-vi")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_vi import (NDE, GAP, build_part, en_ru, lc, pick, present, read_keywords,  # noqa: E402
                           read_vietnamese, verify)
from map_sample_vi import FORMULAS, KV, context5, value5  # noqa: E402,F401
import map_5_vi  # noqa: E402

PART = "20-dvadasamavaggo"

_PH = "sự phòng hộ"                                # saṃvaro
_KPH = "sự không phòng hộ"                         # asaṃvaro (own a- kept)
_CĐ = "được cố định"                               # niyato «được cố định vào trạng thái …»
_CĐV = _CĐ + " vào trạng thái "                    # X-tāniyato
_GĐ = "đi từ gia đình này sang gia đình khác"      # kolaṅkola
_TS7 = "tái sinh tối đa bảy lần"                   # sattakkhattuparama
_TTQ = "thành tựu về quan điểm"                    # diṭṭhisampanna (puggalo «người» is its own keyword)
_ĐDB = "đã được dứt bỏ"                            # pahīnā
_HH7 = "ở lần hiện hữu thứ bảy"                    # sattamabhavika


def _ind(sense, organ, neg=False):
    """«sự (không) phòng hộ năng lực X là nghiệp bằng X» (inner «là» kept)."""
    return (_KPH if neg else _PH) + " năng lực " + sense + " là nghiệp bằng " + organ


T20 = {
    # ---- headings «Chương thứ mười hai»; «(116) 1. Bàn về việc cho rằng sự phòng hộ là nghiệp» … «(125) 10. Bàn về
    # người ở lần hiện hữu thứ bảy»; closers «Phần bàn về … đã hoàn tất.» (kathā / niṭṭhitā: FORMULAS)
    "dvādasamavaggo": "Chương thứ mười hai",       # heading and «Chương thứ mười hai.» (as map_16 / map_18)
    "dvādasama": "thứ mười hai",
    "kammakathā": "Bàn về nghiệp",
    "saḷāyatana": "sáu lĩnh vực nhận biết", "saḷāyatanaṃ": "sáu lĩnh vực nhận biết",   # saḷ- «sáu» is part of the
                                                   # keyword (numeral kept with its keyword, pi-3)
    "kolaṅkola": _GĐ,                              # member (Kolaṅkolakathā, kolaṅkolapuggalo: «người» = puggalo)
    "kolaṅkolatāniyato": _CĐV + _GĐ,
    "sattakkhattuparamatāniyato": _CĐV + _TS7,
    "ekabījitāniyato": _CĐV + "có một hạt giống",
    "niyato": _CĐ,                                 # (pi-4 «có hướng đi cố định» is another text)
    "niyamo": "sự cố định", "niyamena": "sự cố định",   # «bằng sự cố định …» (instrumental frame «bằng» dropped)
    "niyāmaṃ okkamanti": "bước vào sự cố định",    # sotāpattiniyāmaṃ okkamanti «bước vào sự cố định vào dòng»
    "bhavika": "ở lần hiện hữu", "bhavikassa": "ở lần hiện hữu",   # members of sattamabhavika
    "sattamabhavika": _HH7,                        # heading member («Bàn về người ở lần hiện hữu thứ bảy»: as kolaṅkola)
    "sattamabhavikassa": "người " + _HH7,          # uddāna «đối với người ở lần hiện hữu thứ bảy cũng vậy» (the person)
    "voropana": "việc tước đoạt", "jīvitā voropana": "việc tước đoạt mạng sống",   # Vietnamese order
    "voropanakathā": "Bàn về việc tước đoạt",
    "du": "xấu", "gati": "cõi",                    # duggati «cõi xấu» (T16 du «hôi» is duggandho)
    "duggatikathā": "Bàn về cõi xấu",
    "kathāyaṃ": "bàn về", "duggatikathāyaṃ": "bàn về cõi xấu",   # editorial «trong phần bàn về cõi xấu này» (as kathā)
    # ---- 5-630 / 5-631 «Có phải sự phòng hộ năng lực mắt là nghiệp bằng mắt không?»
    "cakkhukammaṃ": "nghiệp bằng mắt", "jivhākammaṃ": "nghiệp bằng lưỡi",   # as kāyakammaṃ / manokammaṃ
    "manindriya": "năng lực ý",
    "saṃvaro kammaṃ": _PH + " là nghiệp",          # inner «là» kept (^5-631 fragment of Asaṃvaro: override)
    "cakkhundriyasaṃvaro cakkhukammaṃ": _ind("mắt", "mắt"),
    "kāyindriyasaṃvaro kāyakammaṃ": _ind("thân", "thân"),
    "jivhindriyasaṃvaro jivhākammaṃ": _ind("lưỡi", "lưỡi"),
    "manindriyasaṃvaro manokammaṃ": _ind("ý", "ý"),
    "cakkhundriyaasaṃvaro cakkhukammaṃ": _ind("mắt", "mắt", True),
    "kāyindriyaasaṃvaro kāyakammaṃ": _ind("thân", "thân", True),
    "jivhindriyaasaṃvaro jivhākammaṃ": _ind("lưỡi", "lưỡi", True),
    "manindriyaasaṃvaro manokammaṃ": _ind("ý", "ý", True),
    # 5-632 sense-door sutta «vị tỳ-khưu khi thấy hình sắc bằng mắt … khi nghe âm thanh bằng tai… khi nhận biết đối
    # tượng của ý bằng ý» (the text's «khi», as T18 sutvā)
    "disvā": "khi thấy", "viññāya": "khi nhận biết",
    "eva": "thật",                                 # Attheva suttanto (5-635 / 5-649 first occurrence: overrides)
    # ---- 5-633 / 5-634 «chủ ý không xác định về mặt đạo đức thuộc quả của nghiệp / mang tính chức năng»
    "vipākābyākatā": "không xác định về mặt đạo đức thuộc quả của nghiệp",
    "kiriyābyākatā": "không xác định về mặt đạo đức mang tính chức năng",
    # 5-635 sutta «Ta không nói đến sự chấm dứt của các nghiệp có chủ ý đã được tạo, đã được tích lũy khi chưa được cảm
    # nhận, và điều ấy ngay trong đời này, hoặc trong lần tái sinh kế tiếp …, hoặc trong một lượt khác về sau»
    "sañcetanikānaṃ": "có chủ ý",
    "katānaṃ": "đã được tạo",                      # (KV «đã làm» is 5-78)
    "upacitānaṃ": "đã được tích lũy",
    "paṭisaṃviditvā": "khi" + GAP + "được cảm nhận",   # of appaṭisaṃviditvā «khi chưa được cảm nhận» (positive part;
                                                   # the gerund keeps «khi», as T16 bhijjamāne «khi … đang tan rã»)
    "upapajje": "lần tái sinh kế tiếp", "pariyāye": "lượt",
    # ---- 5-636 … 5-639 «được cảm nhận là dễ chịu, … có đối tượng; nó có sự hướng đến …»
    "vedaniyo": "được cảm nhận",                   # as T16 vedaniyaṃ
    "sukhavedaniyo": "được cảm nhận là dễ chịu", "dukkhavedaniyo": "được cảm nhận là khó chịu",
    "dukkha": "khó chịu",                          # dukkhavedaniyo / dukkhāya vedanāya (feeling)
    "ārammaṇo": "có đối tượng",                    # of sārammaṇo / anārammaṇo (as T16 / T18 ārammaṇaṃ)
    # 5-637 «do nghiệp ấy đã được tạo, đã được tích lũy, đã được tăng thêm, đã được mở rộng, có giọng nói như Phạm
    # Thiên, nói như chim ca-lăng-tần-già» [trong Trường Bộ Kinh]
    "katattā": "đã được tạo", "upacitattā": "đã được tích lũy", "ussannattā": "đã được tăng thêm",
    "vipulattā": "đã được mở rộng",
    "saro": "giọng nói",                           # brahmassaro «có giọng nói như Phạm Thiên»
    "karavika": "chim ca-lăng-tần-già", "bhāṇī": "nói",   # (pi-4 «nói lời» is gūthabhāṇī …)
    "dīghanikāye": "Trường Bộ Kinh",
    # 5-640 «sáu lĩnh vực nhận biết sinh khởi do nghiệp đã được tạo»
    "uppannaṃ": "sinh khởi",
    # ---- 5-641 … 5-645 Sattakkhattuparamakathā «mẹ bị tước đoạt mạng sống … máu của Như Lai bị làm cho chảy với tâm
    # độc ác… Tăng đoàn bị chia rẽ … không có khả năng thấu hiểu Giáo Pháp trong khoảng giữa … các sự thiết lập tỉnh
    # thức… các chi phần giác ngộ … bằng sự cố định trở lại một lần … bước vào sự cố định vào dòng»
    "abhabbo": "không có khả năng",                # own a- kept (pi-4 abhabba)
    "cittena uppāditaṃ": "bị làm cho chảy với tâm",   # Vietnamese order, inner «với» kept (coordinator rule)
    "saṅgho bhinno": "Tăng đoàn bị chia rẽ",       # subject first
    "sati": "tỉnh thức",                           # satipaṭṭhānā «sự thiết lập tỉnh thức» (pi-1 SATI_BARE)
    # ---- 5-648 / 5-649 Jīvitā voropanakathā «người thành tựu về quan điểm có thể cố ý tước đoạt mạng sống của sinh
    # vật … của mẹ … của một bậc A-la-hán… với tâm độc ác làm cho máu của Như Lai chảy… chia rẽ Tăng đoàn … thiếu kính
    # trọng / kính trọng đối với Bậc Đạo Sư … Giáo Pháp … Tăng đoàn … sự tu học»
    "diṭṭhisampanno puggalo": "người " + _TTQ, "diṭṭhisampannassa puggalassa": "người " + _TTQ,   # head noun first
    "sampannassa": "thành tựu",                    # as sampanno (T12 / T15)
    "sañcicca": "cố ý", "sañcicca voropeyya": "cố ý tước đoạt",
    "voropeyya": "tước đoạt",                      # optative: the bare verb («có thể» = frame, coordinator rule)
    "pāṇaṃ": "sinh vật",                           # «mạng sống của sinh vật» (T10 / T15 «sinh mạng» is another text)
    "pāṇaṃ voropeyya": "tước đoạt" + GAP + "sinh vật",
    "diṭṭhisampanno sañcicca": _TTQ + GAP + "cố ý",                    # «người thành tựu về quan điểm có thể cố ý»
    "diṭṭhisampanno sañcicca voropeyya": _TTQ + GAP + "cố ý tước đoạt",
    "mātaraṃ jīvitā": "mạng sống của mẹ",          # head noun before its genitive, inner «của» kept
    "arahantaṃ": "bậc A-la-hán",
    "uppādeyya": "làm cho" + GAP + "chảy",         # «làm cho máu của Như Lai chảy» (T10 / T12 «làm phát sinh» elsewhere)
    "cittena uppādeyya": "tâm" + GAP + "làm cho" + GAP + "chảy",
    "saṅghaṃ bhindeyya": "chia rẽ Tăng đoàn",
    "gāravo": "kính trọng",                        # of agāravo «thiếu kính trọng» (positive part)
    "sagāravo": "kính trọng",                      # «kính trọng đối với …» (sa- has no word of its own)
    # 5-649 «có thể đại tiện lên, có thể tiểu tiện lên, có thể khạc nhổ lên bảo tháp của Đức Phật, có thể đi vòng
    # quanh bảo tháp của Đức Phật về phía bên trái» (the locative «lên» dropped, as «trong» / «ở»)
    "ohadeyya": "đại tiện", "omutteyya": "tiểu tiện", "niṭṭhubheyya": "khạc nhổ",
    "thūpe": "bảo tháp", "apabyāmato": "về phía bên trái", "kareyya": "đi vòng quanh",
    # sutta «ví như đại dương có bản chất ổn định, không tràn qua bờ; cũng vậy, … điều tu học nào Ta đã đặt ra cho
    # các đệ tử, các đệ tử của Ta không vi phạm điều ấy, dù vì mạng sống»
    "ṭhita": "ổn định", "dhammo": "bản chất",      # ṭhitadhammo «có bản chất ổn định»
    "velaṃ": "bờ", "ativattati": "tràn qua",       # of nātivattati «không tràn qua» (na separate)
    "yaṃ": "nào",                                  # yaṃ … sikkhāpadaṃ «điều tu học nào» (KV yampidaṃ «nào»)
    "sikkhā": "tu học",                            # sikkhāpadaṃ «điều tu học» (padaṃ = điều); «sự tu học» = sikkhāya
    "paññattaṃ": "đã đặt ra", "atikkamanti": "vi phạm",
    "hetu": "vì",                                  # jīvitahetupi «dù vì mạng sống»
    # ---- 5-650 … 5-653 Duggatikathā «đối với người thành tựu về quan điểm, cõi xấu đã được dứt bỏ … có thể tham đắm
    # các hình sắc ở cõi khổ … với người nữ không phải loài người, với con vật cái thuộc loài súc sinh, với thiếu nữ
    # loài rồng … có thể tái sinh vào địa ngục… vào cõi súc sinh… vào cõi ngạ quỷ»
    "diṭṭhisampannassa pahīnā": _TTQ + GAP + _ĐDB,
    "diṭṭhisampannassa pahīnā duggati": _TTQ + GAP + "cõi xấu " + _ĐDB,
    "diṭṭhisampanno rajjeyya": _TTQ + GAP + "tham đắm",
    "rajjeyya": "tham đắm", "rūpe rajjeyya": "tham đắm các hình sắc",   # Vietnamese order, inner «các» kept (pi-1)
    "āpāyike": "ở cõi khổ",                        # as KV āpāyikaṃ
    "amanussa": "không phải loài người",           # amanussitthiyā «người nữ không phải loài người»
    "tiracchānagata": "loài súc sinh",             # tiracchānagatitthiyā «con vật cái thuộc loài súc sinh» (KV tiracchānagato)
    "kaññāya": "thiếu nữ",                         # nāgakaññāya «thiếu nữ loài rồng»
    "tiracchānayoniṃ": "cõi súc sinh", "yoniṃ": "cõi",   # as T16 tiracchānayoni (yoni «cõi» there)
    "dissanti": "dường như",                       # editorial «… dường như nên được hiểu là …»
}

_FINISHED = (7, 6, 5, 4, 2, 3, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18)
PRIOR = {}
for _n in _FINISHED:
    PRIOR.update(getattr(importlib.import_module(f"map_{_n}_vi"), f"T{_n}", {}))
PRIOR.update(T20)


def context20(kw, k, kws, text):
    """Segment rules of this chapter (k: lower-cased keyword). None = no rule."""
    return None


OVERRIDES = {
    "5-631": {"saṃvaro kammaṃ": "sự" + GAP + "phòng hộ là nghiệp"},   # of Asaṃvaro kammaṃ «sự không phòng hộ là
                                                   # nghiệp» (positive part, as map_16 rūpino dhammā «hiện tượng … vật chất»)
    "5-635": {"eva": "ngay"},                      # first: diṭṭheva dhamme «ngay trong đời này» (CROSSCHECK; later Attheva
                                                   # suttanto «thật»)
    "5-641": {"dhammaṃ": "Giáo Pháp"},             # abhisametuṃ dhammaṃ «thấu hiểu Giáo Pháp» (5-632 «đối tượng của ý»)
    "5-648": {"dhamme": "Giáo Pháp"},              # «đối với Giáo Pháp» (5-635 diṭṭheva dhamme «đời»)
    "5-649": {"eva": "cũng"},                      # first: evameva kho «cũng vậy» (CROSSCHECK; later Attheva suttanto «thật»)
}

ALLOWED = {
}


def resolver():
    vi = read_vietnamese(PART)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        k = lc(kw)
        text = vi.get(bid, "")
        v = context20(kw, k, kws, text)
        if v is not None:
            return v
        if k in T20:
            return T20[k]
        if k not in PRIOR:
            v = map_5_vi.subject_predicate(kw, kws, text)
            if v:
                return v
        return value5(kw, kws, PRIOR, text)
    return resolve


def _prior_all(k):
    out = {}
    for n in _FINISHED:
        t = getattr(importlib.import_module(f"map_{n}_vi"), f"T{n}", {})
        if k in t:
            out[n] = t[k]
    return out


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
                p = _prior_all(lc(kw))
                ps = (" T:" + str(p)) if p and any(x != v for x in p.values()) else ""
                print(f"   {kw}={v}  [en:{e[0]} | ru:{e[1]}]{ps}{flag}")


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


if __name__ == "__main__":
    if sys.argv[1:2] == ["show"]:
        show(int(sys.argv[2]), int(sys.argv[3]), "miss" in sys.argv[4:])
    elif sys.argv[1:2] == ["dump"]:
        dump(sys.argv[2:3] == ["miss"])
    elif sys.argv[1:2] == ["prior"]:      # the finished chapters' table values of each keyword
        for _k in sys.argv[2:]:
            print(_k, _prior_all(lc(_k)), "KV:", KV.get(lc(_k)), "F:", FORMULAS.get(lc(_k)))
    else:
        build_part(PART, resolver())
        verify(PART, ALLOWED)
