"""Build the Pāli->Vietnamese keyword map for pi-5 (Kathāvatthu) chapter 27: 27-ekunavisatimavaggo.

usage: python -I -X utf8 -B map_27_vi.py                    (writes 27-ekunavisatimavaggo.mapped.md and verifies it)
       python -I -X utf8 -B map_27_vi.py show lo hi [miss]   (segments lo..hi with every pair, English | Russian and
                                                             the finished chapters' values where they differ; writes
                                                             nothing)
       python -I -X utf8 -B map_27_vi.py dump [miss]         (every distinct keyword=value; writes nothing)
       python -I -X utf8 -B map_27_vi.py look kw ...         (finished chapter tables, pi-1 … pi-4 map values)
       python -I -X utf8 -B map_27_vi.py mlook kw ...        (values in the finished pi-5 mapped files)

Importing this module builds nothing (check_parts_vi.py imports it for ALLOWED).
Resolution order per keyword: OVERRIDES[bid][kw] -> context27 (segment rules of this chapter) -> T27 -> context5 ->
the finished chapter tables T24 … T2 (latest first; a value counts only where it stands in this segment, as map_24_vi)
-> map_5_vi.subject_predicate (coordinator rule) -> value5(kw, kws, T27, text) of map_sample_vi (FORMULAS -> KV ->
two-word composition -> the pi-4 chain).
Conventions: pi-1 … pi-4 vi-map-conventions*.md + notes-map-*.md, vi-map-conventions-pi5.md, map-coordinator-rules.md;
new values in notes-map-27.md.
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

PART = "27-ekunavisatimavaggo"

_KĐK = "không do điều kiện tạo thành"               # asaṅkhata (predicate)
_TQ = "thành quả"
_CĐ = "con đường"
_YN = "yếu tố Niết-bàn"

T27 = {
    # ---- headings «Chương thứ mười chín» (repeated before every discussion), «(186) 1. Bàn về sự dứt bỏ phiền não» …
    # «(193) 8. Bàn về các năng lực»; closers «Phần bàn về … đã hoàn tất.» (kathā / niṭṭhitā: FORMULAS)
    "ekūnavīsatimavaggo": "Chương thứ mười chín",  # heading and «Chương thứ mười chín.» (as map_24 soḷasamavaggo)
    "ekūnavīsatima": "thứ mười chín",
    "jahana": "sự dứt bỏ",                         # Kilesajahanakathā «Bàn về sự dứt bỏ phiền não»
    "accanta": "hoàn toàn",                        # «sự cố định hoàn toàn» (T10 «tuyệt đối» another text)
    "accantaniyāma": "sự cố định hoàn toàn",       # Accantaniyāmakathā
    "accantaniyāmatā": "tính cố định hoàn toàn",   # «có tính cố định hoàn toàn»
    # ---- 5-828 / 5-829 «làm chấm dứt điều đã chấm dứt, làm mất đi điều đã mất đi, làm diệt tận điều đã bị diệt tận,
    # làm biến mất điều đã biến mất, làm biến mất hoàn toàn …» / «làm cho điều chưa sinh ra không sinh ra, làm cho điều
    # chưa sinh thành không sinh thành, … không phát sinh, … không hiện ra»
    "nirodheti": "làm chấm dứt",
    "khīṇaṃ": "đã bị diệt tận", "khepeti": "làm diệt tận",
    "atthaṅgameti": "làm biến mất", "abbhatthaṅgameti": "làm biến mất hoàn toàn",
    "ajaneti": "làm cho" + GAP + "không sinh ra",  # own a- kept («không»); causative «làm cho» as nirodheti «làm …»
    "asañjaneti": "làm cho" + GAP + "không sinh thành",
    "anibbatteti": "làm cho" + GAP + "không phát sinh",
    "apātubhāveti": "làm cho" + GAP + "không hiện ra",
    "sañjātaṃ": "sinh thành",                      # of asañjātaṃ «chưa sinh thành» (positive part; T17)
    # ---- 5-830 «người đã tham đắm dứt bỏ sự tham đắm … Này các tỳ-khưu, bầu trời và mặt đất …» (T21 same quote)
    "rāgaṃ": "sự tham đắm", "dosaṃ": "sự sân hận", "mohaṃ": "sự si mê",   # the text's «sự» (T21 / T24)
    "pathavī": "mặt đất",                          # T21 (context5 «đất» would cut the text's word)
    # ---- 5-832 … 5-834 «sự trống rỗng nằm trong khối tạo tác … cái không có dấu hiệu … cái không mong cầu … các tạo
    # tác này trống rỗng tự ngã hay những gì thuộc về tự ngã» [Trung Bộ Kinh 3.69, trong Kinh Thích Hợp Với Trạng
    # Thái Bất Động]
    "animittaṃ": "cái không có dấu hiệu",          # the text's «cái» (as KV / context5 «cái do điều kiện tạo thành»)
    "appaṇihito": "cái không mong cầu",
    "suññatā saṅkhārakkhandhapariyāpannā": "sự trống rỗng nằm trong khối tạo tác",
    "rūpakkhandhassa": "khối vật chất",
    "rūpakkhandhassa saṅkhārakkhandhapariyāpannā": "khối vật chất nằm trong khối tạo tác",   # «sự trống rỗng của
    "saṅkhārakkhandhassa rūpakkhandhapariyāpannā": "khối tạo tác nằm trong khối vật chất",   # khối X nằm trong …»
    "suññaṃ": "trống rỗng",
    "āneñja": "Trạng Thái Bất Động",               # āneñjasappāye «Kinh Thích Hợp Với Trạng Thái Bất Động» (capitals)
    # ---- 5-835 … 5-843 «thành quả của đời sống sa-môn không do điều kiện tạo thành … nơi che chở, nơi ẩn náu, nơi
    # nương tựa, nơi đến cuối cùng, điều bất biến, điều bất tử … hai điều không do điều kiện tạo thành»
    "parāyaṇaṃ": "nơi đến cuối cùng",
    "asaṅkhatāni": "điều " + _KĐK,                 # «hai / năm / chín / sáu điều …» (as map_14)
    "sāmaññaphalaṃ asaṅkhataṃ": _TQ + " của đời sống sa-môn " + _KĐK,
    "sotāpattiphalaṃ asaṅkhataṃ": _TQ + " vào dòng " + _KĐK,
    "arahattaphalaṃ asaṅkhataṃ": _TQ + " A-la-hán " + _KĐK,
    "cīvarassa": "y phục", "piṇḍapātassa": "đồ ăn khất thực", "senāsanassa": "chỗ ở",   # T21 (-aṃ forms)
    "parikkhārassa": "vật dụng",
    "cīvarassa asaṅkhatā": "y phục " + _KĐK,       # Cīvarassa patti asaṅkhatā «sự đạt đến y phục …» (adjacent)
    "gilānapaccayabhesajjaparikkhārassa asaṅkhatā": "thuốc men và vật dụng chữa bệnh " + _KĐK,
    "vitthāretabbaṃ": "nên được trình bày chi tiết",   # (evaṃ sabbaṃ vitthāretabbaṃ) «(tất cả nên được …)»
    "sotāpattimaggassa": _CĐ + " vào dòng", "sotāpattiphalassa": _TQ + " vào dòng",
    "sotāpattimaggassa asaṅkhatā": _CĐ + " vào dòng " + _KĐK,
    "arahattaphalassa asaṅkhatā": _TQ + " A-la-hán " + _KĐK,
    "sabbadhammānaṃ asaṅkhatā": "tất cả các hiện tượng " + _KĐK,   # «tính đúng như thật của tất cả các hiện tượng
                                                   # không do …» (adjacent; inner «các» kept)
    "rūpatā": "tính chất vật chất", "saṅkhāratā": "tính chất tạo tác",
    "rūpatā asaṅkhatā": "tính chất vật chất " + _KĐK,
    "viññāṇatā asaṅkhatā": "tính chất thức " + _KĐK,
    # ---- 5-844 … 5-846 «yếu tố Niết-bàn là thiện … có đối tượng, nó có sự hướng đến… sự mong cầu»
    "nibbānadhātu": _YN,
    "nibbānadhātu kusalā": _YN + " là thiện",      # inner «là» kept
    "ārammaṇo": "có đối tượng",                    # sārammaṇo / anārammaṇo (T24)
    # ---- 5-847 … 5-852 «kẻ giết mẹ … đối với người cố định vào quan điểm về sự trường tồn, quan điểm về sự đoạn diệt
    # có thể sinh khởi … bằng con đường bất thiện» / AN 7.15 «có người mang các hiện tượng bất thiện hoàn toàn đen tối,
    # người ấy một lần chìm thì chìm luôn … trồi lên rồi lại chìm … trồi lên rồi nhìn thấy rõ, nhìn quanh …»
    "uppajjeyya": "sinh khởi",                     # optative: the bare verb («có thể» = frame)
    "akusalena maggena": _CĐ + " bất thiện",       # Vietnamese order
    "sassatadiṭṭhiyā": "quan điểm về sự trường tồn", "ucchedadiṭṭhiyā": "quan điểm về sự đoạn diệt",
    "niyatassa puggalassa": "người cố định",       # Vietnamese order
    "samannāgato": "mang",                         # «có người mang các hiện tượng …» («có» = Idhekacco)
    "kho": NDE,                                    # only in the bracket [dị bản (…): evaṃ kho bhikkhave puggalo]
    "sabbakālaṃ": "vào mọi lúc",                   # adverb keeps its preposition (KV sabbadā)
    "nimujjati": "chìm", "vipassati": "nhìn thấy rõ",
    # ---- 5-853 … 5-855 «có sự tinh tấn thuộc thế gian …»
    "lokiyaṃ vīriyaṃ": "sự tinh tấn thuộc thế gian",   # the text's «sự»
    # ---- 5-856 MN 1.283 «khi quan sát thế gian bằng con mắt của Đức Phật, Ta đã thấy các chúng sinh có ít bụi trong
    # mắt, có nhiều bụi trong mắt, có các năng lực sắc bén, có các năng lực non yếu, có phẩm chất tốt, dễ hướng dẫn,
    # một số sống thấy sự đáng sợ của thế gian khác và của lỗi lầm» [Trung Bộ Kinh 1.283; ở đó cũng thấy các từ như
    # “dvākāre duviññāpaye”]
    "addasaṃ": "đã thấy", "volokento": "khi quan sát",   # participle keeps «khi»
    "cakkhunā": "con mắt",                         # buddhacakkhunā «bằng con mắt của Đức Phật» (the text's «con»)
    "raja": "bụi", "tikkha": "sắc bén", "mudu": "non yếu",
    "viharante": "sống", "dassāvino": "thấy", "bhaya": "sự đáng sợ", "vajja": "lỗi lầm",
    "lokiyāni": "thuộc thế gian",
    "dvākāre": NDE, "duviññāpaye": NDE,            # only in Pāli inside the editorial bracket (sample 5-112 rule)
    "dissanti": "thấy", "padāni": "từ",            # editorial bracket «ở đó cũng thấy các từ như …» («các» dropped)
}

OVERRIDES = {
}

ALLOWED = {
}


def _tables():
    """[(chapter, table)] of the finished chapters (2 … 24)."""
    out = []
    for n in range(2, 25):
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


def context27(kw, k, kws, text):
    """Segment rules of this chapter (k: lower-cased keyword). None = no rule."""
    return None


def resolver():
    vi = read_vietnamese(PART)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        text = vi.get(bid, "")
        k = lc(kw)
        v = context27(kw, k, kws, text)
        if v is not None:
            return v
        if k in T27:
            return T27[k]
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
        return value5(kw, kws, T27, text)
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
                src = " [T27]" if lc(kw) in T27 else (" [prior]" if p else "")
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
             "23-pannarasamavaggo", "24-solasamavaggo"]


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
