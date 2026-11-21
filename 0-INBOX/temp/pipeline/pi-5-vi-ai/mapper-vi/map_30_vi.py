"""Build the Pāli->Vietnamese keyword map for pi-5 (Kathāvatthu) chapter 30: 30-bavisatimavaggo.

usage: python -I -X utf8 -B map_30_vi.py                    (writes 30-bavisatimavaggo.mapped.md and verifies it)
       python -I -X utf8 -B map_30_vi.py show lo hi [miss]   (segments lo..hi with every pair, English | Russian and
                                                             the finished chapters' values where they differ; writes
                                                             nothing)
       python -I -X utf8 -B map_30_vi.py dump [miss]         (every distinct keyword=value; writes nothing)
       python -I -X utf8 -B map_30_vi.py look kw ...         (finished chapter tables, pi-1 … pi-4 map values)
       python -I -X utf8 -B map_30_vi.py mlook kw ...        (values in the finished pi-5 mapped files)

Importing this module builds nothing (check_parts_vi.py imports it for ALLOWED).
Resolution order per keyword: OVERRIDES[bid][kw] -> context30 (segment rules of this chapter) -> T30 -> context5 ->
the finished chapter tables T29, T27 … T2 (latest first; a value counts only where it stands in this segment, as map_24_vi /
map_27_vi) -> map_5_vi.subject_predicate (coordinator rule) -> value5(kw, kws, T30, text) of map_sample_vi (FORMULAS ->
KV -> two-word composition -> the pi-4 chain).
Conventions: pi-1 … pi-4 vi-map-conventions*.md + notes-map-*.md, vi-map-conventions-pi5.md, map-coordinator-rules.md;
new values in notes-map-30.md.
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

PART = "30-bavisatimavaggo"

_PN = "sự nhập Niết-bàn trọn vẹn"
_NPN = "nhập Niết-bàn trọn vẹn"
_A = "bậc A-la-hán"
_KXĐ = "không xác định về mặt đạo đức"
_TC = "tính chất làm điều kiện"
_KK = "kéo dài trong khoảnh khắc"
_ND = "người đang nằm mơ"

T30 = {
    # ---- headings «Chương thứ hai mươi hai» (repeated before every discussion), «(208) 1. Bàn về sự nhập Niết-bàn
    # trọn vẹn» … «(217) 10. Bàn về những gì kéo dài trong khoảnh khắc»; closers «Phần bàn về … đã hoàn tất.»
    "bāvīsatimavaggo": "Chương thứ hai mươi hai",  # heading and «Chương thứ hai mươi hai.» (as map_27 / map_29)
    "bāvīsatima": "thứ hai mươi hai",
    "parinibbāna": _PN,
    "parinibbānakathā": "Bàn về " + _PN,           # as T26 saṅkantikathā «Bàn về sự chuyển»
    "kusalacitta": "tâm thiện",
    "āneñja": "trạng thái bất động",               # T25 (T27 «Trạng Thái Bất Động» is the sutta title)
    "abhisamayakathā": "Bàn về sự thấu hiểu",      # Dhammābhisamayakathā «Bàn về sự thấu hiểu Giáo Pháp»
    "āsevana": "thực hành",                        # «điều kiện thực hành»
    "āsevanapaccaya": "điều kiện thực hành",
    "āsevanapaccayakathā": "Bàn về điều kiện thực hành",
    "āsevanapaccayatā": _TC + " thực hành",
    "paccayatā": _TC,                              # T23
    "khaṇika": _KK,                                # Khaṇikakathā «Bàn về những gì kéo dài trong khoảnh khắc»
    "khaṇikā": _KK,                                # member of (eka)cittakkhaṇikā
    "cittakkhaṇikā": _KK + " của" + GAP + "tâm",   # «… trong khoảnh khắc của một tâm» (eka «một» between)
    "ekacittakkhaṇikā": _KK + " của một tâm",
    # ---- 5-892 / 5-893 «có sự nhập Niết-bàn trọn vẹn mà chưa dứt bỏ một xiềng xích nào đó … bậc A-la-hán có tham
    # đắm… có phiền não … biết toàn bộ phạm vi của Đức Phật»
    "kiñci saṃyojanaṃ pahāya": "dứt bỏ một xiềng xích nào đó",   # positive part of appahāya (T29, the text's «một»)
    "appahāya parinibbānaṃ": _PN + " mà chưa dứt bỏ",           # Vietnamese order, inner «mà» kept (coordinator)
    "nirāgo": "không có tham đắm",                 # own nir- kept (T29)
    "arahā nirāgo": _A + " không có tham đắm",
    "visayaṃ": "phạm vi",                          # T29 (buddhavisayaṃ «phạm vi của Đức Phật»)
    # ---- 5-894 «bậc A-la-hán nhập Niết-bàn trọn vẹn trong khi tạo tác sự tạo tác thuộc về phước… làm nghiệp dẫn
    # đến cõi tái sinh… trong khi tích lũy, giảm trừ, dứt bỏ, bám víu, phân tán, gom tụ, dập tắt, nhen nhóm»
    "kusalacitto": "tâm thiện",                    # «với tâm thiện» («với» = frame, as «bằng» of cakkhunā)
    "citto": "tâm",
    "arahā parinibbāyati": _A + " " + _NPN,        # subject first (coordinator rule)
    "abhisaṅkharonto": "trong khi tạo tác",        # participles keep «trong khi» (map_4); first rendering
    "karonto": "trong khi" + GAP + "làm",          # one «trong khi» for the whole list (as T3 cutassa «khi … chết»)
    "kammaṃ karonto": "trong khi" + GAP + "làm nghiệp",
    "ācinanto": "trong khi tích lũy",
    "apacinanto": "trong khi" + GAP + "giảm trừ", "pajahanto": "trong khi" + GAP + "dứt bỏ",
    "upādiyanto": "trong khi" + GAP + "bám víu", "visinento": "trong khi" + GAP + "phân tán",
    "ussinento": "trong khi" + GAP + "gom tụ", "vidhūpento": "trong khi" + GAP + "dập tắt",
    "sandhūpento": "trong khi" + GAP + "nhen nhóm",
    "manussa": "cõi người",                        # manussasobhagya «sự vinh hiển cõi người» (T25; context30)
    # ---- 5-895 «khi có sự tỉnh thức được thiết lập, tỉnh thức và hiểu biết rõ ràng»
    "sati": "sự tỉnh thức",                        # upaṭṭhitassati (the text's «sự»)
    # ---- 5-896 «khi đang đứng vững trong trạng thái bất động … trong tâm bình thường … trong tâm mang tính chức
    # năng … trong tâm không xác định về mặt đạo đức thuộc quả của nghiệp … sau khi xuất khỏi tầng thiền thứ tư,
    # liền sau đó đã nhập Niết-bàn trọn vẹn»
    "āneñje": "trạng thái bất động",
    "ṭhito parinibbāyati": _NPN + " khi đang đứng vững",   # Vietnamese order
    "pakaticitte": "tâm bình thường",
    "kiriyamaye": "mang tính chức năng",
    "kiriyābyākate": _KXĐ + " mang tính chức năng",
    "vipākābyākate": _KXĐ + " thuộc quả của nghiệp",
    "catutthajjhānā": "tầng thiền thứ tư",
    "vuṭṭhahitvā": "sau khi xuất khỏi",
    "samanantarā": "liền sau đó",                  # the text's «đó» (adverb, «immediately after»)
    "samanantarā parinibbuto": "liền sau đó đã nhập Niết-bàn trọn vẹn",
    # ---- 5-897 … 5-900 «khi nằm trong bào thai có sự thấu hiểu Giáo Pháp … việc thuyết giảng Giáo Pháp, việc nghe
    # Giáo Pháp, việc đàm luận Giáo Pháp, việc hỏi han, việc thọ trì giới hạnh, … sự chuyên tâm thực hành việc thức
    # canh vào đầu đêm và cuối đêm … người đang ngủ, buông thả, mất tỉnh thức, không hiểu biết rõ ràng»
    "gabbha": "bào thai",
    "seyyāya": "nằm",                              # gabbhaseyyāya «khi nằm trong bào thai» («khi» = the frame of the
                                                   # noun, as «trong» of Supinantena)
    "savanaṃ": "việc nghe", "sākacchā": "việc đàm luận", "paripucchā": "việc hỏi han",
    "samādānaṃ": "việc thọ trì",
    "jāgariya": "việc thức canh", "anuyogo": "sự chuyên tâm thực hành",   # jāgariyānuyogo (not the heading «Chất vấn»)
    "ratta": "đêm",                                # pubbarattāpararattaṃ «vào đầu đêm và cuối đêm» (first)
    "suttassa": "người đang ngủ",                  # head noun «người» of the list (pi-4 / sample rule)
    "pamattassa": "buông thả",
    "muṭṭhassatissa": "mất tỉnh thức",             # T11 muṭṭhassati
    "sampajānassa": "hiểu biết rõ ràng",           # of asampajānassa «không hiểu biết rõ ràng» (positive part)
    "arahatta": "trạng thái A-la-hán",             # T29 / style rule
    "arahattappatti": "sự đạt đến trạng thái A-la-hán",
    "supinagatassa": _ND,
    # ---- 5-901 / 5-902 «tất cả tâm của người đang nằm mơ là không xác định về mặt đạo đức … trong giấc mơ có thể
    # sát hại sinh mạng … có thể hưởng thụ hành vi dâm dục, đồ bất tịnh của người đang nằm mơ có thể thoát ra»
    "supinagatassa abyākataṃ": _ND + " là " + _KXĐ,   # inner «là» kept
    "supinantena": "giấc mơ",                      # «trong giấc mơ» (locative frame «trong» dropped)
    "mucceyya": "thoát ra",                        # optative: the bare verb («có thể» = frame)
    "kareyya": "đi nhiễu quanh",                   # as T21 / map 25 (same list; ekāgārikaṃ kareyya «cướp …» has its
                                                   # own keyword)
    # ---- 5-903 … 5-905 AN 8.40 «Việc sát hại sinh mạng, này các tỳ-khưu, khi được thực hành, được tu tập, được làm
    # đi làm lại, thì dẫn đến địa ngục, dẫn đến cõi súc sinh, dẫn đến cõi ngạ quỷ, quả nhẹ nhất của việc sát hại
    # sinh mạng, đối với người sinh làm người, là dẫn đến tuổi thọ ngắn …»
    "āsevito": "khi được thực hành", "āsevitā": "khi được thực hành",   # participle keeps «khi»
    "bhāvito": "được tu tập", "bahulīkato": "được làm đi làm lại",
    "bhāvito bahulīkato": "được tu tập được làm đi làm lại",   # comma dropped (as bhāvitā bahulīkatā)
    "saṃvattanikā": "dẫn đến",
    "nirayasaṃvattaniko": "dẫn đến địa ngục", "nirayasaṃvattanikā": "dẫn đến địa ngục",
    "yoni": "cõi",                                 # tiracchānayoni «cõi súc sinh» (T16)
    "sabbalahuso": "nhẹ nhất", "sabbalahuso vipāko": "quả nhẹ nhất",   # Vietnamese order
    "bhūtassa": "sinh làm",                        # manussabhūtassa «người sinh làm người» (context30: manussa)
    "micchācārassa": "hành vi sai trái",           # kāmesumicchācārassa «hành vi sai trái trong các dục lạc»
    "sapatta": "sự thù địch", "vera": "oán hận",   # sapattavera «sự thù địch và oán hận»
    "vādassa": "việc nói",                         # musāvādassa «việc nói dối»
    "abbhūta": "điều không có thật", "abbhakkhāna": "sự vu khống",   # abbhūtabbhakkhāna «sự vu khống điều không có
                                                   # thật» (own a- kept)
    "mittehi": "bạn bè", "bhedana": "sự chia lìa", # mittehi bhedana «sự chia lìa với bạn bè»
    "amanāpa": "không dễ ưa",                      # amanāpasadda «âm thanh không dễ ưa» (own a- kept)
    "palāpassa": "việc nói lời",                   # samphappalāpassa «việc nói lời phù phiếm»
    "ādeyya": "được tin nhận",                     # of anādeyyavācā «lời nói không được tin nhận» (positive part)
    "vācā": "lời nói",
    "pānaṃ": "việc uống",                          # surāmerayapānaṃ «việc uống rượu nấu và rượu men»
    "ummattaka": "sự điên loạn",
    "ogadhā": "thâm nhập vào",                     # amatogadhā «thâm nhập vào điều bất tử»
    "parāyanā": "lấy" + GAP + "làm nơi đến cuối cùng",   # amataparāyanā «lấy điều bất tử làm nơi đến cuối cùng»
    "pariyosānā": "lấy" + GAP + "làm điểm kết thúc",     # (pi-1 ārammaṇā «lấy … làm đối tượng»)
    # ---- 5-906 «lĩnh vực mắt cùng sinh với thức qua mắt … Mắt thuộc phần bên trong, này các hiền giả, không bị hư
    # hoại, … và không có sự lưu ý tương ứng, thì vẫn chưa có sự xuất hiện của phần thức tương ứng»
    "cakkhuviññāṇena": "thức qua mắt", "kāyaviññāṇena": "thức qua thân",
    "tajjo": "tương ứng", "bhāgassa": "phần",
    "aparibhinnaṃ": "không bị hư hoại",            # own a- kept
    # ---- 5-907 «… thường còn, bền vững, trường tồn, có bản chất không biến đổi»
    "niccā": "thường còn", "dhuvā": "bền vững",
}

OVERRIDES = {
    "5-901": {"dhammaṃ": "hành vi"},               # methunaṃ dhammaṃ «hành vi dâm dục» (member)
}

ALLOWED = {
}


def _tables():
    """[(chapter, table)] of the finished chapters (2 … 27, 29; 28 / 31 are mapped at the same time)."""
    out = []
    for n in list(range(2, 28)) + [29]:
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


def context30(kw, k, kws, text):
    """Segment rules of this chapter (k: lower-cased keyword). None = no rule."""
    if k == "ṭhito":               # «khi đang đứng vững trong …» (5-896, 5-907) / «mà đứng vững sau khi …» (5-894)
        return pick(text, "khi đang đứng vững", "đứng vững")
    if k == "manussa":             # manussasobhagya «sự vinh hiển cõi người» / manussabhūtassa «người sinh làm người»
        return pick(text, "cõi người") or "người"
    return None


def resolver():
    vi = read_vietnamese(PART)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        text = vi.get(bid, "")
        k = lc(kw)
        v = context30(kw, k, kws, text)
        if v is not None:
            return v
        if k in T30:
            return T30[k]
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
        return value5(kw, kws, T30, text)
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
                src = " [T30]" if lc(kw) in T30 else (" [prior]" if p else "")
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
             "19-ekadasamavaggo", "20-dvadasamavaggo", "21-terasamavaggo", "22-cuddasamavaggo",
             "23-pannarasamavaggo", "24-solasamavaggo", "25-sattarasamavaggo", "26-attharasamavaggo",
             "27-ekunavisatimavaggo", "29-ekavisatimavaggo"]


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
