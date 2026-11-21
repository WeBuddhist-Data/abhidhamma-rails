"""Build the Pāli->Vietnamese keyword map for pi-5 (Kathāvatthu) chapter 29: 29-ekavisatimavaggo.

usage: python -I -X utf8 -B map_29_vi.py                    (writes 29-ekavisatimavaggo.mapped.md and verifies it)
       python -I -X utf8 -B map_29_vi.py show lo hi [miss]   (segments lo..hi with every pair, English | Russian and
                                                             the finished chapters' values where they differ; writes
                                                             nothing)
       python -I -X utf8 -B map_29_vi.py dump [miss]         (every distinct keyword=value; writes nothing)
       python -I -X utf8 -B map_29_vi.py look kw ...         (finished chapter tables, pi-1 … pi-4 map values)
       python -I -X utf8 -B map_29_vi.py mlook kw ...        (values in the finished pi-5 mapped files)

Importing this module builds nothing (check_parts_vi.py imports it for ALLOWED).
Resolution order per keyword: OVERRIDES[bid][kw] -> context29 (segment rules of this chapter) -> T29 -> context5 ->
the finished chapter tables T27, T26, T24 … T2 (latest first; a value counts only where it stands in this segment, as
map_24_vi / map_27_vi; chapters 25 and 28 are mapped at the same time and not used) -> map_5_vi.subject_predicate
(coordinator rule) -> value5(kw, kws, T29, text) of map_sample_vi (FORMULAS -> KV -> two-word composition -> the pi-4
chain).
Conventions: pi-1 … pi-4 vi-map-conventions*.md + notes-map-*.md, vi-map-conventions-pi5.md, map-coordinator-rules.md;
new values in notes-map-29.md.
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

PART = "29-ekavisatimavaggo"

T29 = {
    # ---- headings «Chương thứ hai mươi mốt» (repeated before every discussion), «(200) 1. Bàn về giáo huấn» …
    # «(207) 8. Bàn về nghiệp»; closers «Phần bàn về … đã hoàn tất.» (kathā / niṭṭhitā: FORMULAS)
    "ekavīsatimavaggo": "Chương thứ hai mươi mốt",  # heading and «Chương thứ hai mươi mốt.» (as map_24 / map_27)
    "ekavīsatima": "thứ hai mươi mốt",
    "iddhikathā": "Bàn về thần thông",             # heading and closer «Phần bàn về thần thông …» (as Kammakathā)
    "dhammakathā": "Bàn về các hiện tượng",        # inner «các» kept (as Kāmakathā «Bàn về các dục lạc»)
    # ---- 5-878 Sāsanakathā «giáo huấn đã được làm mới … làm mới lại giáo huấn của Như Lai»
    "sāsana": "giáo huấn", "sāsanaṃ": "giáo huấn",   # (as sāsane, finished map)
    "puna": "lại",                                 # «làm mới lại» (navaṃ = mới; T10 «lại»)
    # ---- 5-879 / 5-880 Avivittakathā «người phàm phu không tách khỏi các hiện tượng thuộc ba cõi»
    "vivitta": "tách khỏi", "vivitto": "tách khỏi",   # of avivitta(-o) «không tách khỏi»: the positive part
    "tedhātukehi": "thuộc ba cõi",
    "kammehi": "nghiệp",
    "puthujjano avivitto": "người phàm phu không tách khỏi",   # own a- kept
    "rūpadhātuarūpadhātūpagaṃ kammaṃ": "nghiệp đi đến cõi hình sắc và cõi không hình sắc",   # head noun first
    "arūpa": "không hình sắc",                     # member (dhātu = cõi; T15 / T16)
    "pariññātaṃ": "đã được" + GAP + "hiểu biết trọn vẹn",   # «đã được người phàm phu hiểu biết trọn vẹn»
    # ---- 5-881 / 5-882 Saṃyojanakathā «có sự đạt đến trạng thái A-la-hán khi chưa dứt bỏ xiềng xích nào đó»
    "kiñci saṃyojanaṃ pahāya": "dứt bỏ xiềng xích nào đó",   # of appahāya: positive part, Vietnamese order
    "appahāya arahattappatti": "sự đạt đến trạng thái A-la-hán khi chưa dứt bỏ",
    "arahattappatti": "sự đạt đến trạng thái A-la-hán",
    "arahatta": "trạng thái A-la-hán",             # the text's «trạng thái» (T12 / T3)
    "makkho": "gièm pha", "paḷāso": "ganh đua", "upāyāso": "tuyệt vọng",   # «có gièm pha …» (of samakkho …)
    "nirāgo": "không có tham đắm", "niddoso": "không có sân hận", "nimmoho": "không có si mê",   # own ni- kept
    "arahā nirāgo": "bậc A-la-hán không có tham đắm",
    "visayaṃ": "phạm vi",                          # buddhavisayaṃ «phạm vi của Đức Phật»
    # ---- 5-883 / 5-884 Iddhikathā «có thần thông theo ý định của chư Phật hay của các đệ tử»
    "adhippāya": "ý định",
    "adhippāyaiddhi": "thần thông theo ý định", "adhippāyiddhi": "thần thông theo ý định",
    "buddhānaṃ": "chư Phật",                       # the text's «chư» kept (as devā = chư thiên)
    "buddhānaṃ vā sāvakānaṃ": "chư Phật hay của các đệ tử",
    "paṇṇā": "lá", "pupphā": "hoa", "phalikā": "quả",   # «cây luôn có lá / hoa / quả»
    "nicca": "luôn",                               # niccapaṇṇā …
    "niccaṃ": "luôn",                              # CROSSCHECK: first niccaṃ juṇhaṃ «luôn có ánh trăng»; then
                                                   # «vật chất thường còn» (Rūpaṃ niccaṃ)
    "juṇhaṃ": "ánh trăng", "khemaṃ": "an ổn", "subhikkhaṃ": "no đủ", "suvatthi": "an lành",
    "jāti": "sinh", "jarā": "lão hóa", "maraṇa": "chết",   # «có bản chất phải sinh / lão hóa / chết» (T19)
    "samādhi": "sự định tâm",                      # the text's «sự»
    "pana": "quả thật",                            # suvaṇṇo ca pana āsi «và nó quả thật đã là vàng»
    "māgadhassa": "xứ Ma-kiệt-đà",                 # classifier «xứ» kept (pi-4 xứ Ca-thi)
    "pāsādaṃ": "cung điện",
    "pilindavaccho": "Pi-lin-đa-vác-cha",
    "seniyassa": "Seniya", "seniyassa bimbisārassa": "Seniya Tần-bà-sa-la",
    "adhimucci": "đã dứt khoát hướng tâm",
    # ---- 5-885 Buddhakathā «giữa chư Phật với chư Phật có sự thấp kém và vượt trội … xét về sự làm chủ … xét về
    # sự hiểu biết và thấy rõ về sự toàn tri»
    "buddhānaṃ hīnātirekatā": "chư Phật" + GAP + "sự thấp kém và vượt trội",
    "atireka": "vượt trội",
    "vasibhāva": "sự làm chủ",
    "sabbaññuta": "sự toàn tri",
    "ñāṇa": "hiểu biết",
    # ---- 5-886 Sabbadisākathā «chư Phật tồn tại ở tất cả các phương … Đức Phật tồn tại ở phương đông …»
    "buddhā": "chư Phật",
    "buddho tiṭṭhati": "Đức Phật tồn tại", "buddhā tiṭṭhanti": "chư Phật tồn tại",
    "tiṭṭhanti": "tồn tại",
    "disāya": "phương",
    "puratthimāya": "đông", "dakkhiṇāya": "nam", "uttarāya": "bắc",   # disāya = phương
    "jacco": "thuộc giai cấp", "gotto": "thuộc họ",   # kiṃjacco / kiṃgotto «thuộc giai cấp nào, thuộc họ nào»
    "nāmā": "tên",                                 # kinnāmā … «… tên gì»
    "upaṭṭhāko": "người thị giả",                  # agent noun keeps its head noun
    "kīdisaṃ": "như thế nào",
    "pattaṃ": "bình bát",
    "dhāreti": "mặc",                              # CROSSCHECK: first «mặc y phục», then «mang bình bát»
    "nagare": "thành phố", "raṭṭhe": "vương quốc",
    "rājike": "Thiên Vương",                       # cātumahārājike «cõi Tứ Đại Thiên Vương» (map 10 rājikānaṃ)
    "tusite": "Đâu Suất",                          # map 10 tusitānaṃ
    "ratiyā": "Lạc",                               # nimmānaratiyā «cõi Hóa Lạc» (nimmāna = Hóa)
    "para": "Tha",                                 # paranimmitavasavattiyā «cõi Tha Hóa Tự Tại» (map 10)
    "vattiyā": "Tự Tại",                           # map 10 vattīnaṃ
    # ---- 5-887 … 5-891 Dhammakathā / Kammakathā «tất cả các hiện tượng / nghiệp đều cố định … ba nhóm – nhóm cố
    # định theo hướng sai lầm …» [Liệt kê các hiện tượng, ma trận bộ ba 15]
    "niyato rāsi": "nhóm cố định",                 # Vietnamese order (micchattaniyato rāsi «nhóm cố định …»)
    "rāsī": "nhóm",
    "dha": "Liệt kê các hiện tượng",               # dha. sa. = Dhammasaṅgaṇī (citation = the Vietnamese title)
    "tika": "bộ ba",                               # tikamātikā «ma trận bộ ba»
    "kammā": "nghiệp",
    "kammā niyatā": "nghiệp" + GAP + "cố định",    # «các nghiệp đều cố định» (as dhammā niyatā)
    "vedanīyaṃ": "được cảm nhận",                  # (as vedaniyaṃ, finished maps)
    "upapajja": "khi tái sinh",                    # «được cảm nhận khi tái sinh»
    "aparāpariya": "trong các đời kế tiếp",        # «được cảm nhận trong các đời kế tiếp» (inner «các» kept;
                                                   # as diṭṭhadhamma «ngay trong đời này»)
    "diṭṭhadhammavedanīyaṃ niyataṃ": "được cảm nhận ngay trong đời này cố định",
    "aparāpariyavedanīyaṃ niyataṃ": "được cảm nhận trong các đời kế tiếp cố định",
}

OVERRIDES = {
    "5-29-5-1-0": {"buddha": "chư Phật"},          # heading «Bàn về chư Phật» (elsewhere buddha = Đức Phật)
}

ALLOWED = {
}

_USED = [27, 26] + list(range(24, 1, -1))       # latest first; 25 / 28 are in progress elsewhere


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


def context29(kw, k, kws, text):
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
        v = context29(kw, k, kws, text)
        if v is not None:
            return v
        if k in T29:
            return T29[k]
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
        return value5(kw, kws, T29, text)
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
                src = " [T29]" if lc(kw) in T29 else (" [prior]" if p else "")
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
             "23-pannarasamavaggo", "24-solasamavaggo", "26-attharasamavaggo", "27-ekunavisatimavaggo"]


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
