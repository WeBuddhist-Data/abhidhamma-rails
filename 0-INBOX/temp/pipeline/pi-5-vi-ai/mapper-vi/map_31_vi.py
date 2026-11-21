"""Build the Pāli->Vietnamese keyword map for pi-5 (Kathāvatthu) chapter 31: 31-tevisatimavaggo.

usage: python -I -X utf8 -B map_31_vi.py                    (writes 31-tevisatimavaggo.mapped.md and verifies it)
       python -I -X utf8 -B map_31_vi.py show lo hi [miss]   (segments lo..hi with every pair, English | Russian and
                                                             the finished chapters' values where they differ; writes
                                                             nothing)
       python -I -X utf8 -B map_31_vi.py dump [miss]         (every distinct keyword=value; writes nothing)
       python -I -X utf8 -B map_31_vi.py look kw ...         (finished chapter tables, pi-1 … pi-4 map values)
       python -I -X utf8 -B map_31_vi.py mlook kw ...        (values in the finished pi-5 mapped files)

Importing this module builds nothing (check_parts_vi.py imports it for ALLOWED).
Resolution order per keyword: OVERRIDES[bid][kw] -> context31 (segment rules of this chapter) -> T31 -> context5 ->
the finished chapter tables T29, T27, T26, T25, T24 … T2 (latest first; a value counts only where it stands in this
segment, as map_27_vi / map_29_vi; chapters 28 and 30 are mapped at the same time and not used) ->
map_5_vi.subject_predicate (coordinator rule) -> value5(kw, kws, T31, text) of map_sample_vi (FORMULAS -> KV -> two-word
composition -> the pi-4 chain).
Conventions: pi-1 … pi-4 vi-map-conventions*.md + notes-map-*.md, vi-map-conventions-pi5.md, map-coordinator-rules.md;
book-end values as the pi-4 map's colophon (pakaraṇaṃ = Bộ, niṭṭhitaṃ = đã hoàn tất); new values in notes-map-31.md.
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

PART = "31-tevisatimavaggo"

_HT = "được hình thành trọn vẹn"                   # parinipphanna (positive part of aparinipphanna «không …»)

T31 = {
    # ---- headings «Chương thứ hai mươi ba» (repeated before every discussion), «(218) 1. Bàn về cùng một ý định» …
    # «(226) 9. Bàn về những gì không được hình thành trọn vẹn»; closers «Phần bàn về … đã hoàn tất.»
    "tevīsatimavaggo": "Chương thứ hai mươi ba",   # heading and «Chương thứ hai mươi ba.» (as map_27 / map_29)
    "tevīsatima": "thứ hai mươi ba",
    "eka": "cùng một",                             # ekādhippāya «cùng một ý định» (the text's «cùng» carries 'shared')
    "ekādhippāya": "cùng một ý định", "ekādhippāyena": "cùng một ý định",   # instrumental «với» = frame
    "adhippāya": "ý định", "adhippāyena": "ý định",   # T29 adhippāya
    "vaṇṇa": "hình dạng", "vaṇṇena": "hình dạng",  # «trong hình dạng của các bậc A-la-hán» («trong» = case frame)
    "arahanta": "bậc A-la-hán", "arahantānaṃ": "bậc A-la-hán",   # leading «các» dropped
    "arahantavaṇṇa": "hình dạng của các bậc A-la-hán",   # head noun first, inner «của các» kept
    "arahantānaṃ vaṇṇena": "hình dạng của các bậc A-la-hán",
    "kārikā": "làm theo",                          # «vì làm theo ý muốn nhờ quyền uy» (heading «việc làm theo»: override)
    "issariyakāmakārikādikathā": "Bàn về việc làm theo ý muốn nhờ quyền uy và các mục khác",
    "issariyakāmakārikākathā": "Bàn về việc làm theo ý muốn nhờ quyền uy",
    "patirūpa": "tương tự",                        # «tương tự sự sân hận» (heading «cái tương tự»: override)
    "patirūpako": "tương tự", "cittapatirūpakaṃ": "tương tự tâm",
    "patirūpakathā": "Bàn về cái tương tự",        # the text's «cái» (as animittaṃ «cái không có dấu hiệu», T27)
    "nipphanna": "được hình thành",                # member of aparinipphanna (pari = trọn vẹn)
    "parinipphanna": _HT, "parinipphannaṃ": _HT,   # (as map_19 / map_23 parinipphannaṃ)
    "dukkhaṃ parinipphannaṃ": "khổ đau" + GAP + _HT,   # «chỉ khổ đau mới được …» («chỉ … mới» = ññeva)
    # ---- 5-908 / 5-909 «được phép hưởng thụ hành vi dâm dục … người không phải sa-môn … sát hại sinh mạng, …, nói
    # dối, nói lời chia rẽ, nói lời thô ác, nói lời phù phiếm, đột nhập nhà, cướp bóc, cướp một ngôi nhà, mai phục bên
    # đường, đi lại với vợ người khác, cướp phá làng, cướp phá thị trấn» (verbs as map_10 / map_25 -eyya forms)
    "methuno": "dâm dục", "methuno dhammo": "hành vi dâm dục",   # (as methunaṃ dhammaṃ, finished maps)
    "dhammo": "hành vi", "dhammaṃ": "hành vi",     # member of methuno dhammo / methunaṃ dhammaṃ
    "paṭisevitabbo": "được phép hưởng thụ",        # gerundive keeps its modal (as vattabbe = nên nói)
    "paṭisevanti": "hưởng thụ",
    "assamaṇena": "người không phải sa-môn",       # agent noun keeps its head noun, own a- kept
    "abhikkhunā": "người không phải tỳ-khưu",
    "pārājikena": "người phạm tội bị trục xuất",
    "mūlena": "gốc",                               # chinnamūlena «bị cắt đứt tận gốc»
    "pāṇo": "sinh mạng",                           # (as pāṇaṃ)
    "hantabbo": "được phép sát hại",               # the modal stands once, with the first verb of the list
    "hananti": "sát hại", "pāṇaṃ hananti": "sát hại sinh mạng",   # (as pāṇaṃ haneyya, map_10)
    "bhaṇitabbā": "nói", "bhaṇanti": "nói",        # (as bhaṇeyya)
    "palapitabbaṃ": "nói lời", "palapanti": "nói lời",   # (as palapeyya)
    "sandhi": "nhà",
    "cheditabbo": "đột nhập", "chindanti": "đột nhập",   # (as chindeyya)
    "hātabbaṃ": NDE, "haranti": NDE,               # nillopaṃ harati «cướp bóc»: one word, given to nillopaṃ
    "ekāgārikaṃ kātabbaṃ": "cướp một ngôi nhà", "ekāgārikaṃ karonti": "cướp một ngôi nhà",   # (as … kareyya)
    "ṭhātabbaṃ": "mai phục", "tiṭṭhanti": "mai phục",   # (as tiṭṭheyya)
    "dāro": "vợ",                                  # (as dāraṃ)
    "ghātako": "cướp phá",                         # gāmaghātako «cướp phá làng» (as ghātakaṃ, map_25)
    "amanussā": "chúng sinh không phải loài người",   # head noun kept, own a- kept
    # ---- 5-910 … 5-914 «Bồ-tát vì làm theo ý muốn nhờ quyền uy mà đi đến nơi đọa lạc … nhập vào bào thai … đã làm
    # những việc khổ hạnh khó làm … đã chấp nhận “thế gian là trường tồn” … đã tôn xưng một bậc đạo sư khác»
    "roruvaṃ": "địa ngục Khiếu Hoán",              # classifier kept (as pi-4 «cõi Sắc Cứu Cánh»)
    "gabbhaseyyaṃ": "bào thai",
    "okkamati": "nhập vào",
    "bodhisatto okkamati": "Bồ-tát" + GAP + "nhập vào",
    "iddhimā": "có thần thông",
    "vīmaṃsa": "sự thẩm xét",                      # vīmaṃsiddhipādo «… bằng sự thẩm xét»
    "dukkarakārikaṃ": "việc khổ hạnh khó làm",     # (as dukkarakāriyaṃ, map_12; «những» dropped)
    "bodhisatto akāsi": "Bồ-tát" + GAP + "đã làm",
    "bodhisatto dukkarakārikaṃ akāsi": "Bồ-tát" + GAP + "đã làm những việc khổ hạnh khó làm",   # inner «những» kept
    "bodhisatto uddisi": "Bồ-tát" + GAP + "đã tôn xưng",
    "paccāgacchi": "đã chấp nhận",
    "hoti": "còn tồn tại",                         # «Như Lai còn tồn tại sau khi chết» (as map_22)
    # ---- 5-918 closing verses «Nhóm nửa năm mươi nhỏ. … Điều mới, sự nhập Niết-bàn, cùng một ý định. … Nghiền nát
    # các học thuyết của người khác, được thiết lập vững chắc trên gốc rễ là kinh; Soi sáng giáo thuyết của bậc đạo sư,
    # trong bộ “Các vấn đề tranh luận”. Gồm ba mươi lăm phần tụng đọc. Bộ “Các vấn đề tranh luận” đã hoàn tất.»
    "aḍḍhapaṇṇāsako": "Nhóm nửa năm mươi",         # (paṇṇāsako = Nhóm năm mươi, map_23)
    "nibbuti": "sự nhập Niết-bàn",
    "maddanā": "Nghiền nát", "pavāda": "học thuyết",
    "mūla": "gốc rễ",                              # suttamūla «gốc rễ là kinh» (as map_23 mūlaṃ)
    "samāhitā": "được thiết lập vững chắc",
    "ujjotanā": "Soi sáng",
    "samaye": "giáo thuyết",                       # satthusamaye «giáo thuyết của bậc đạo sư» (not samaye = lúc)
    "pakaraṇe": "Bộ",                              # the pi-4 colophon (pakaraṇaṃ = Bộ): «trong bộ …», «Bộ “…” …»
    "pañcattiṃsa": "ba mươi lăm",
    "bhāṇavāraṃ": "phần tụng đọc",                 # pi-1 «Phần tụng đọc» (bhāṇa = tụng đọc, vāro = phần)
}

OVERRIDES = {
    "5-31-3-1-0": {"kārikā": "việc làm theo"},     # heading «Bàn về việc làm theo ý muốn nhờ quyền uy …»
    "5-31-4-1-0": {"patirūpa": "cái tương tự"},    # heading «Bàn về cái tương tự»
}

ALLOWED = {
}

_USED = [29, 27, 26, 25] + list(range(24, 1, -1))   # latest first; 28 / 30 are in progress elsewhere


def _tables():
    """[(chapter, table)] of the finished chapters, latest first."""
    out = []
    for n in _USED:
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


def context31(kw, k, kws, text):
    """Segment rules of this chapter (k: lower-cased keyword). None = no rule."""
    if k == "eka":                                 # «cùng một ý định» (ekādhippāya) / «cướp một ngôi nhà» (ekāgārikaṃ)
        return "cùng một" if present("cùng một", text) else "một"
    return None


def resolver():
    vi = read_vietnamese(PART)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        text = vi.get(bid, "")
        k = lc(kw)
        v = context31(kw, k, kws, text)
        if v is not None:
            return v
        if k in T31:
            return T31[k]
        v = context5(kw, k, kws, text)
        if v is not None:
            return v
        for n, t in _TABLES:                        # the finished chapters (latest first) where their value stands in
            if k in t and (t[k] == NDE or present(t[k], text)):   # this segment
                return t[k]
        if " " in kw:
            v = map_5_vi.subject_predicate(kw, kws, text)
            if v:
                return v
        return value5(kw, kws, T31, text)
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
                src = " [T31]" if lc(kw) in T31 else (" [prior]" if p else "")
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
