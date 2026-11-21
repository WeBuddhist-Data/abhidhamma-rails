"""Build the Pāli->Vietnamese keyword map for pi-5 (Kathāvatthu) chapter 23: 23-pannarasamavaggo.

usage: python -I -X utf8 -B map_23_vi.py                    (writes 23-pannarasamavaggo.mapped.md and verifies it)
       python -I -X utf8 -B map_23_vi.py show lo hi [miss]   (segments lo..hi with every pair, English | Russian and
                                                             the finished chapters' values where they differ; writes
                                                             nothing)
       python -I -X utf8 -B map_23_vi.py dump [miss]         (every distinct keyword=value; writes nothing)
       python -I -X utf8 -B map_23_vi.py look kw ...         (finished chapter tables, KV, FORMULAS, pi-1 … pi-4 maps)

Importing this module builds nothing (check_parts_vi.py imports it for ALLOWED).
Resolution order per keyword: OVERRIDES[bid][kw] -> context23 (segment rules of this chapter) -> T23 -> context5 ->
the finished chapter tables T20 … T2 (latest first; a value counts only where it stands in this segment, as map_17_vi)
-> value5(kw, kws, T23, text) of map_sample_vi (FORMULAS -> KV -> two-word composition -> the pi-4 chain).
Conventions: pi-1 … pi-4 vi-map-conventions*.md + notes-map-*.md, vi-map-conventions-pi5.md, map-coordinator-rules.md;
condition names (paccaya) as map_13_vi; new values in notes-map-23.md.
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

PART = "23-pannarasamavaggo"

_TCLĐK = "tính chất làm điều kiện"                 # paccayatā (map_13 X-paccayataṃ «tính chất làm điều kiện X»)
_ĐK = "điều kiện "                                  # X-paccayena «làm điều kiện theo điều kiện X» (frame «theo» dropped)
_XĐ = "được xác định riêng biệt"                    # vavatthitā
_HT = "được hình thành trọn vẹn"                    # parinipphanna (T19)
_TG = "thời gian"                                   # addhā
_TVCG = "tri giác và cảm giác"                      # saññāvedayita
_CDTV = "chấm dứt " + _TVCG                         # saññāvedayitanirodha (member of …nirodhasamāpatti)
_SCD = "sự " + _CDTV                                # saññāvedayitanirodhaṃ «người đang nhập sự chấm dứt …»
_TTCD = "thành tựu thiền " + _CDTV                  # saññāvedayitanirodhasamāpatti
_ND = "người đang nhập"                             # samāpanno / samāpannassa (map_13 samāpannassa)
_QĐ = "qua đời"                                     # kālaṃ kareyya (optative: the bare verb, «có thể» = frame)
_VT = "cõi chúng sinh Vô Tưởng"                     # asaññasatta (the text's «cõi» kept)
_HĐ = "hướng đến"                                   # upika / upikā
_TL = "sự tích lũy"                                 # upacaya / upacayo
_TLN = _TL + " nghiệp"                              # kammūpacaya(-o)
_GH = "gây hại"                                     # sabyābajjhaṃ (sa- has no word of its own: «vừa gây hại»)
_KGH = "không gây hại"                              # abyābajjhaṃ (own a- kept)
_STT = "sự tạo tác bằng "                           # kāya- / vacī- / manosaṅkhāraṃ

T23 = {
    # ---- headings «Chương thứ mười lăm»; «(145) 1. Bàn về tính chất làm điều kiện» … «(155) 11. Bàn về sự tích lũy
    # nghiệp»; closers «Phần bàn về … đã hoàn tất.» (kathā = Bàn về, niṭṭhitā = đã hoàn tất: FORMULAS)
    "pannarasamavaggo": "Chương thứ mười lăm",     # heading and «Chương thứ mười lăm.» (as map_18 / map_19 / map_20)
    "pannarasama": "thứ mười lăm",
    "paccayatā": _TCLĐK,                           # (T10 / T14 «quy luật tùy thuộc vào điều kiện» is idappaccayatā)
    "paccaya": "điều kiện",                        # Aññamaññapaccaya «điều kiện lẫn nhau» (KV «dựa vào» is aparappaccaya)
    "aññamañña": "lẫn nhau", "aññamaññapaccaya": "điều kiện lẫn nhau",
    "aññamaññapaccayakathā": "Bàn về điều kiện lẫn nhau",
    "khaṇa": "khoảnh khắc", "laya": "chốc lát", "muhutta": "thời khắc",   # Khaṇalayamuhutta «khoảnh khắc, chốc lát,
    "khaṇo": "khoảnh khắc", "layo": "chốc lát", "muhuttaṃ": "thời khắc",  # thời khắc» (T10 muhuttaṃ «chốc chốc» is
                                                                          # another text)
    "saññāvedayita": _TVCG, "vedayita": "cảm giác",
    "saññāvedayitakathā": "Bàn về " + _TVCG,
    "dutiyasaññāvedayitakathā": "Bàn lần thứ hai về " + _TVCG,   # «Bàn lần thứ hai về …» (dutiya has no keyword)
    "tatiyasaññāvedayitakathā": "Bàn lần thứ ba về " + _TVCG,
    "saññāvedayitakathā niṭṭhitā": "Bàn về " + _TVCG + " đã hoàn tất",   # closer «Phần bàn về … đã hoàn tất.»
    "dutiyasaññāvedayitakathā niṭṭhitā": "Bàn lần thứ hai về " + _TVCG + " đã hoàn tất",
    "tatiyasaññāvedayitakathā niṭṭhitā": "Bàn lần thứ ba về " + _TVCG + " đã hoàn tất",
    "satta": "chúng sinh", "sañña": "Tưởng",       # of asaññasatta «chúng sinh Vô Tưởng» (positive part, T16)
    "upika": _HĐ, "upikā": _HĐ,                    # Asaññasattupikakathā «Bàn về điều hướng đến cõi chúng sinh Vô Tưởng»
    "upacaya": _TL, "upacayo": _TL, "kammūpacaya": _TLN, "kammūpacayo": _TLN,
    # ---- 5-711 … 5-714 «Chẳng phải ý muốn chi phối là yếu tố chi phối của các hiện tượng cùng sinh sao? … làm điều
    # kiện theo điều kiện chi phối, làm điều kiện theo điều kiện cùng sinh … năng lực … con đường … dưỡng chất»
    "paccayo": "làm điều kiện",
    "hetupaccayena": _ĐK + "nguyên nhân", "adhipatipaccayena": _ĐK + "chi phối",   # map_13 condition names
    "sahajātapaccayena": _ĐK + "cùng sinh", "indriyapaccayena": _ĐK + "năng lực", "maggapaccayena": _ĐK + "con đường",
    "ārammaṇapaccayena": _ĐK + "đối tượng", "anantarapaccayena": _ĐK + "kế cận",
    "āsevanapaccayena": _ĐK + "thực hành",
    "sahajāta": "cùng sinh", "jātānaṃ": "sinh",    # of sahajātānaṃ (T17 jātā / jātaṃ «sinh»)
    "sahajātānaṃ dhammānaṃ": "hiện tượng cùng sinh",
    "vavatthitā": _XĐ,
    "chandādhipati adhipati": "ý muốn chi phối là yếu tố chi phối",      # extraction artefacts: the adjacent words with
    "vīriyādhipati adhipati": "tinh tấn chi phối là yếu tố chi phối",    # the inner «là» (sample rule)
    "cittādhipati adhipati": "tâm chi phối là yếu tố chi phối",
    "vīmaṃsādhipati adhipati": "sự thẩm xét chi phối là yếu tố chi phối",
    "magga": "con đường",                          # maggaṅgaṃ «chi phần của con đường» / maggabhāvanā «tu tập con đường»
    # ---- 5-715 «sự xem xét lại sinh khởi sau khi trân trọng hiện tượng cao quý, và nó là đối tượng»
    "garuṃ": "trân trọng",
    "katvā": "sau khi",                            # garuṃ katvā «sau khi trân trọng»: the gerund's «sau khi» (map 4 / 5)
    "paccavekkhaṇā": "sự xem xét lại",             # the noun with its «sự» (T13 Paccavekkhaṇa- «xem xét lại» is a member)
    # ---- 5-716 «từng hiện tượng thiện trước làm điều kiện cho từng hiện tượng thiện sau theo điều kiện kế cận, và nó
    # là sự thực hành»
    "purimā": "trước",
    "kiriyābyākatā dhammā": "hiện tượng không xác định về mặt đạo đức mang tính chức năng",
    "dhammā paccayo": "hiện tượng" + GAP + "làm điều kiện",
    # ---- 5-718 / 5-719 «chỉ vô minh làm điều kiện cho các sự tạo tác … các sự tạo tác cũng làm điều kiện cho vô minh …
    # vô minh cùng sinh với sự tạo tác … sự lão hóa và sự chết làm điều kiện cho sự sinh» (T14 paccayā chain)
    "taṇhāpaccayā": "khao khát làm điều kiện cho",
    "upādānapaccayā": "sự bám víu" + GAP + "làm điều kiện cho",   # «sự bám víu cũng làm điều kiện cho khao khát»
    "saṅkhārapaccayā": "sự tạo tác" + GAP + "làm điều kiện cho",  # «các sự tạo tác cũng làm điều kiện cho vô minh»
    "jātā": "sinh",                                # of sahajātā «cùng sinh với …»
    # ---- 5-720 / 5-721 «thời gian được hình thành trọn vẹn … thời gian quá khứ … có ba chủ đề bàn luận này … hoặc
    # người ta có thể bàn luận về thời gian quá khứ»
    "addhā": _TG, "addhā parinipphanno": _TG + " " + _HT,
    "atīto addhā": _TG + " quá khứ", "anāgato addhā": _TG + " tương lai", "paccuppanno addhā": _TG + " hiện tại",
    "atītaṃ addhānaṃ": _TG + " quá khứ", "anāgataṃ addhānaṃ": _TG + " tương lai",
    "paccuppannaṃ addhānaṃ": _TG + " hiện tại",
    "nipphanno": "được hình thành", "parinipphanno": _HT,   # as T19 nipphannā / parinipphannā
    "vatthūni": "chủ đề", "kathāvatthūni": "chủ đề bàn luận",
    "katheyya": "bàn luận",                        # optative: the bare verb («có thể» = frame, coordinator rule)
    # ---- 5-726 / 5-727 «sự lão hóa và sự chết của các hiện tượng vượt thế gian … của thành quả trở lại một lần …»
    "lokuttarānaṃ": "vượt thế gian",
    "arahattaphalassa": "thành quả A-la-hán", "anāgāmiphalassa": "thành quả không trở lại",
    "sakadāgāmiphalassa": "thành quả trở lại một lần",
    "arahattamaggassa": "con đường A-la-hán", "anāgāmimaggassa": "con đường không trở lại",
    "sakadāgāmimaggassa": "con đường trở lại một lần",
    "balānaṃ": "sức mạnh",
    # ---- 5-728 … 5-731 «thành tựu thiền chấm dứt tri giác và cảm giác là vượt thế gian»
    "nirodha": "chấm dứt", "saññāvedayitanirodha": _CDTV,
    "saññāvedayitanirodhasamāpatti lokuttarā": _TTCD + " là vượt thế gian",   # inner «là» kept (sample)
    # ---- 5-732 … 5-734 «người đang nhập sự chấm dứt tri giác và cảm giác có thể qua đời … có sự tiếp xúc lúc lâm
    # chung … chất độc có thể tác động lên thân của …, dao kiếm …, lửa … sự cố định mà do được cố định bằng sự cố định
    # ấy … người có được thức qua mắt»
    "nirodhaṃ": "sự chấm dứt", "saññāvedayitanirodhaṃ": _SCD,
    "samāpanno": _ND, "samāpannassa": _ND,
    "nirodhaṃ samāpanno": _ND + " sự chấm dứt", "nirodhaṃ samāpannassa": _ND + " sự chấm dứt",
    "kālaṃ kareyya": _QĐ,
    "saññāvedayitanirodhaṃ kālaṃ kareyya": _SCD + GAP + _QĐ,   # «… sự chấm dứt tri giác và cảm giác có thể qua đời»
    "saññāvedayitanirodhaṃ phasso": _SCD + GAP + "sự tiếp xúc",   # «… có sự tiếp xúc» (existential «có» = frame)
    "māraṇa": "lâm chung", "māraṇantiyo": "lúc lâm chung",
    "kameyya": "tác động",                         # optative: the bare verb
    "kāye": "thân",                                # «lên thân của …» (locative frame «lên» dropped, as T20 thūpe)
    "samaṅgī": "người có được", "cakkhuviññāṇasamaṅgī": "người có được thức qua mắt",   # as context19
    # ---- 5-735 / 5-736 «thành tựu thiền chấm dứt tri giác và cảm giác hướng đến cõi chúng sinh Vô Tưởng … sự không
    # tham lam, tức gốc rễ thiện … niềm tin, sự tinh tấn, sự tỉnh thức, sự định tâm, trí tuệ … tu tập con đường … bất
    # cứ ai nhập …»
    "saññāvedayitanirodhasamāpatti asaññasattupikā": _TTCD + " " + _HĐ + " " + _VT,
    "samādhi": "sự định tâm", "sati": "sự tỉnh thức",   # the factors (context23: «tỉnh thức» inside «sự thiết lập
                                                        # tỉnh thức», 5-726)
    "mūlaṃ": "gốc rễ",                             # kusalamūlaṃ «gốc rễ thiện»; uddāna mūlañca «gốc rễ» (T12 «gốc» is
                                                   # another text)
    "samāpajjanti": "nhập",
    # ---- 5-737 … 5-741 «nghiệp là khác, sự tích lũy nghiệp là khác … sự tích lũy tri giác … sự tích lũy nghiệp cùng
    # sinh với nghiệp thiện là thiện … gắn liền với cảm giác dễ chịu … khi tâm đang tan rã thì nghiệp tan rã … từ sự
    # tích lũy nghiệp, quả của nghiệp phát sinh»
    "saññūpacayo": _TL + " tri giác",
    "aññā vedanā": "cảm giác là khác",             # contiguous here («cảm giác là khác»; KV «cảm giác … là khác» is
                                                   # aññā sukhā vedanā)
    "kammūpacayo sahajāto": _TLN + " cùng sinh",
    "kammaṃ sahajātaṃ": "nghiệp cùng sinh",
    "jāto": "sinh", "jātaṃ": "sinh",               # of sahajāto / sahajātaṃ «cùng sinh» (T17)
    "kusalena kammena": "nghiệp thiện", "akusalena kammena": "nghiệp bất thiện",   # head noun first
    "kusalena kammena kusalo": "nghiệp thiện là thiện",   # inner «là» kept
    "kammena kusalo": "nghiệp" + GAP + "thiện",    # extraction artefact (kammena … kusalo): the predicate «thiện» of
    "kammena akusalo": "nghiệp" + GAP + "bất thiện",   # «nghiệp thiện là thiện» («là» = predicate frame)
    "sampayuttena": "gắn liền",                    # «nghiệp gắn liền với cảm giác …» (governing «với» dropped, pi-3)
    "sukhāya": "dễ chịu",                          # the feeling (KV «hạnh phúc» is 5-230)
    "bhijjamānaṃ": "khi" + GAP + "đang tan rã",    # loc. abs. participle keeps «khi» (T16 bhijjamāne)
    "cittaṃ bhijjamānaṃ": "khi tâm đang tan rã",
    "nibbattati": "phát sinh",
    # ---- 5-742 sutta MN 57 «Này Pun-na, ở đây, có người tạo tác sự tạo tác bằng thân vừa gây hại vừa không gây hại …
    # sau khi tạo tác … thì tái sinh vào một thế giới … các sự tiếp xúc … chạm đến người ấy … khi bị các sự tiếp xúc …
    # chạm đến, cảm nhận cảm giác …, xen lẫn dễ chịu và khó chịu, ví như loài người, một số vị trời và một số chúng sinh
    # ở cõi đọa lạc … chúng sinh là người thừa kế của nghiệp»; uddāna «… kiếp, gốc rễ, và điều được xác định riêng biệt»
    "kāyasaṅkhāraṃ": _STT + "thân", "vacīsaṅkhāraṃ": _STT + "lời nói", "manosaṅkhāraṃ": _STT + "ý",
    "saṅkhāraṃ": "sự tạo tác", "kāya": "thân", "vacī": "lời nói", "mano": "ý",
    "abhisaṅkharoti": "tạo tác", "abhisaṅkharitvā": "sau khi tạo tác",   # gerund «sau khi» (map 4 / 5)
    "sabyābajjhaṃ": _GH, "abyābajjhaṃ": _KGH,
    "sabyābajjhaṃ abyābajjhaṃ": "vừa " + _GH + " vừa " + _KGH,   # -pi … -pi «vừa … vừa …» (inner words kept)
    "phuṭṭho": "khi bị" + GAP + "chạm đến",        # phuṭṭho samāno «khi bị các sự tiếp xúc … chạm đến» (participle
                                                   # keeps «khi»)
    "vokiṇṇa": "xen lẫn",                          # vokiṇṇasukhadukkhaṃ «xen lẫn dễ chịu và khó chịu»
    "sukha": "dễ chịu", "dukkhaṃ": "khó chịu", "sukhadukkhaṃ": "dễ chịu và khó chịu",   # no «sự» here (context5
                                                                                       # «sự dễ chịu …» elsewhere)
    "seyyathāpi": "ví như",
    "vinipātikā": "chúng sinh ở cõi đọa lạc",      # the beings with their head noun (as KV nerayiko)
    "kamma": "nghiệp",                             # kammadāyādā «người thừa kế của nghiệp»
    "kappo": "kiếp",                               # uddāna (T18 / pi-4 kappa «kiếp»)
    "paṭicca": "tùy thuộc vào điều kiện",          # paṭiccasamuppādo «sự sinh khởi tùy thuộc vào điều kiện» (pi-1)
    "upapattiyā": "tái sinh",                      # asaññasattupapattiyā «để tái sinh vào …» («để» frame dropped)
    "maggo": "con đường",
}

OVERRIDES = {
}

ALLOWED = {}


def _tables():
    """[(chapter, table)] of the finished chapters (2 … 20)."""
    out = []
    for n in range(2, 21):
        try:
            m = importlib.import_module(f"map_{n}_vi")
        except Exception:      # noqa: BLE001
            continue
        t = getattr(m, f"T{n}", None)
        if t:
            out.append((n, t))
    return out


_TABLES = _tables()


def context23(kw, k, kws, text):
    """Segment rules of this chapter (k: lower-cased keyword). None = no rule."""
    if k == "kathā" and not present("bàn về", text):   # «Bàn lần thứ hai / thứ ba về …» (5-23-8-1-0, 5-731,
        return "Bàn" + GAP + "về"                      # 5-23-9-1-0, 5-734)
    if k == "adhipati":            # the predicate noun «… là yếu tố chi phối» (5-711 … 5-714) / adhipatipaccayena
        return pick(text, "yếu tố chi phối", "chi phối")   # «điều kiện chi phối» only (5-715)
    if k == "ārammaṇaṃ":           # sārammaṇaṃ «nghiệp có đối tượng» (5-740) / «nó là đối tượng» (5-715)
        return pick(text, "có đối tượng", "đối tượng")
    if k == "sati":                # the factor «sự tỉnh thức» / «sự thiết lập tỉnh thức» (5-726; pi-1 SATI_BARE)
        return pick(text, "sự tỉnh thức", "tỉnh thức")
    return None


def resolver():
    vi = read_vietnamese(PART)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        text = vi.get(bid, "")
        k = lc(kw)
        v = context23(kw, k, kws, text)
        if v is not None:
            return v
        if k in T23:
            return T23[k]
        v = context5(kw, k, kws, text)
        if v is not None:
            return v
        for n, t in reversed(_TABLES):             # the finished chapters (latest first) where their value stands in
            if k in t and (t[k] == NDE or present(t[k], text)):   # this segment
                return t[k]
        return value5(kw, kws, T23, text)
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
                src = " [T23]" if lc(kw) in T23 else (" [prior]" if p else "")
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
                print("   ", name, dict(v.most_common(4)))


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
