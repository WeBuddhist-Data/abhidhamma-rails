"""Build the Pāli->Vietnamese keyword map for pi-5 (Kathāvatthu) chapter 26: 26-attharasamavaggo.

usage: python -I -X utf8 -B map_26_vi.py                    (writes 26-attharasamavaggo.mapped.md and verifies it)
       python -I -X utf8 -B map_26_vi.py show lo hi [miss]   (segments lo..hi with every pair, English | Russian and
                                                             the finished chapters' values where they differ; writes
                                                             nothing)
       python -I -X utf8 -B map_26_vi.py dump [miss]         (every distinct keyword=value; writes nothing)
       python -I -X utf8 -B map_26_vi.py look kw ...         (finished chapter tables, pi-1 … pi-4 map values)
       python -I -X utf8 -B map_26_vi.py mlook kw ...        (values in the finished pi-5 mapped files)

Importing this module builds nothing (check_parts_vi.py imports it for ALLOWED).
Resolution order per keyword: OVERRIDES[bid][kw] -> context26 (segment rules of this chapter) -> T26 -> context5 ->
the finished chapter tables T24 … T2 (latest first; a value counts only where it stands in this segment, as map_24_vi)
-> map_5_vi.subject_predicate (coordinator rule) -> value5(kw, kws, T26, text) of map_sample_vi (FORMULAS -> KV ->
two-word composition -> the pi-4 chain).
Conventions: pi-1 … pi-4 vi-map-conventions*.md + notes-map-*.md, vi-map-conventions-pi5.md, map-coordinator-rules.md;
new values in notes-map-26.md.
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

PART = "26-attharasamavaggo"

_NT = "người đang nhập thành tựu thiền"            # samāpanno «người đang nhập thành tựu thiền nghe âm thanh» (T19 / T21)
_DT = "đã được" + GAP + "thuyết giảng"             # desito «Giáo Pháp đã được Đức Phật, Đức Thế Tôn thuyết giảng»

T26 = {
    # ---- headings «Chương thứ mười tám» (repeated before every discussion), «(177) 1. Bàn về thế giới loài người» …
    # «(185) 9. Bàn về việc cho rằng thấy hình sắc bằng mắt»; closers «Phần bàn về … đã hoàn tất.»
    "aṭṭhārasamavaggo": "Chương thứ mười tám",     # as map_24 soḷasamavaggo
    "aṭṭhārasama": "thứ mười tám",
    "manussaloka": "thế giới loài người", "manussaloke": "thế giới loài người",
    "jāti": "loại",                                # Gandhajātikathā «Bàn về các loại hương thơm» (KV jāte «loại»)
    "gandhajāti": "loại hương thơm", "gandhajāte": "loại hương thơm",   # «các loại hương thơm (khác)» («các» dropped)
    "gandha": "hương thơm", "gandhena": "hương thơm",                    # T10 / T12 (T15 «mùi» another text)
    "saṅkanti": "sự chuyển", "saṅkantikathā": "Bàn về sự chuyển",       # «Bàn về sự chuyển từ tầng thiền sang …»
    "saṅkamati": "chuyển",
    "antarika": "trung gian", "antarikā": "trung gian",                 # T10 / T14 «khoảng cách» another text
    "jhānantarika": "tầng thiền trung gian", "jhānantarikā": "tầng thiền trung gian",
    # ---- 5-802 / 5-803 «Chẳng phải có những bảo tháp, khu vườn, tịnh xá, làng, thị trấn, thành phố, đất nước, xứ sở
    # nơi Đức Phật đã cư trú sao? … Đức Thế Tôn đã sinh ra tại Lâm-tỳ-ni, đã giác ngộ hoàn toàn dưới gốc cây Bồ-đề,
    # Đức Thế Tôn đã chuyển bánh xe Giáo Pháp tại Ba-la-nại, tại bảo tháp Cha-pa-la, sự tạo tác của tuổi thọ đã được
    # buông bỏ …» and the five sutta openings «Này các tỳ-khưu, một thời Ta trú tại …»
    "aṭṭhāsi": "đã sống",                          # manussaloke aṭṭhāsi «đã sống ở thế giới loài người»
    "buddhavutthāni": "nơi Đức Phật đã cư trú", "vutthāni": "đã cư trú",
    "cetiyāni": "bảo tháp", "cetiye": "bảo tháp",  # «các / những» dropped
    "ārāma": "khu vườn", "ārāme": "khu vườn", "vihāra": "tịnh xá",   # ārāmavihāra… «khu vườn, tịnh xá, …»
    "nagarāni": "thành phố", "raṭṭhāni": "đất nước",                 # KV raṭṭhaṃ
    "jāto": "đã sinh ra",                          # KV / pi-1 (T17 «sinh» is sahajāto); bhagavā jāto «Đức Thế Tôn đã
                                                   # sinh ra»
    "bhagavatā pavattitaṃ": "Đức Thế Tôn đã chuyển",
    "dhammacakkaṃ pavattitaṃ": "đã chuyển bánh xe Giáo Pháp",   # Vietnamese order
    "ossaṭṭho": "đã được buông bỏ",
    "samayaṃ": "thời",                             # ekamidāhaṃ samayaṃ «một thời» (eka no keyword: numeral dropped)
    "viharāmi": "trú",                             # «Ta trú tại …»
    "subhaga": "Su-bha-ga", "vane": "rừng",        # first subhagavane «trong rừng Su-bha-ga»; CROSSCHECK veḷuvane
                                                   # «Trúc Lâm», jetavane «rừng Kỳ-đà», mahāvane «Đại Lâm»
    "sāla": "cây sa-la", "rāja": "chúa",           # sālarājamūle «dưới gốc cây sa-la chúa» (mūle = gốc)
    "nigrodhe": "cây đa", "ajapāla": "người chăn dê",   # ajapālanigrodhe «tại cây đa của người chăn dê»
    "veḷu": "Trúc",                                # veḷuvane «trong Trúc Lâm» (split Sino-Vietnamese, as KV mahāpathavī)
    "kaḷandaka": "sóc", "nivāpe": "nơi cho" + GAP + "ăn",   # kaḷandakanivāpe «nơi cho sóc ăn»
    "jeta": "Kỳ-đà",
    "mahāvane": "Đại Lâm",
    "kūṭāgāra": "có mái nhọn", "sālāyaṃ": "giảng đường",    # kūṭāgārasālāya «tại giảng đường có mái nhọn»
    "saṃvaḍḍho": "đã lớn lên", "abhibhuyya": "vượt lên trên",
    "tena hi buddho": "Vậy thì Đức Phật", "tena hi buddhassa": "Vậy thì Đức Phật",   # «Vậy thì Đức Phật, Đức Thế
    "tena hi dhammo": "Vậy thì Giáo Pháp",                                         # Tôn …» / «Vậy thì Giáo Pháp …»
    "anupalitto": "không bị" + GAP + "làm vấy bẩn",   # «không bị thế gian làm vấy bẩn» (T12 «không bị vấy bẩn» another
                                                     # text)
    # ---- 5-804 … 5-806 «Giáo Pháp đã được Đức Phật, Đức Thế Tôn thuyết giảng … Được hóa thân thuyết giảng … tôn giả
    # A-nan … Ta cũng có thể thuyết giảng Giáo Pháp một cách tóm tắt … những người hiểu được thì khó tìm» / AN 3.126
    "dhammo": "Giáo Pháp",                         # as written (T15 «giáo pháp» is satañca dhammo)
    "desito": _DT, "dhammo desito": "Giáo Pháp " + _DT,
    "abhinimmitena": "hóa thân",
    "āyasmatā": "tôn giả", "āyasmatā ānandena": "tôn giả A-nan",
    "saṃkhittena": "một cách tóm tắt", "vitthārena": "một cách chi tiết",
    "deseyyaṃ": "thuyết giảng",                    # optative: «có thể» is frame (coordinator rule)
    "dhammaṃ deseyyaṃ": "thuyết giảng Giáo Pháp",
    "aññātāro": "người hiểu được",                 # «những» dropped
    "dullabhā": "khó tìm",
    "desemi": "thuyết giảng", "dhammaṃ desemi": "thuyết giảng Giáo Pháp",
    "abhiññāya": "sau khi đã hiểu biết trực tiếp",  # as written (T4 / T12 other texts)
    "abhiññāya dhammaṃ": "Giáo Pháp sau khi đã hiểu biết trực tiếp",   # Vietnamese order
    "pāṭihāriyaṃ": "sức thuyết phục",              # of appāṭihāriyaṃ «không có sức thuyết phục» (positive part)
    "karaṇīyo": "điều nên làm",                    # «lời khuyên dạy là điều nên làm» (the text's predicate noun)
    "ovādo": "lời khuyên dạy", "anusāsanī": "lời giáo huấn",
    "alaṃ": "đủ", "tuṭṭhiyā": "thỏa mãn", "attamanatāya": "hài lòng",   # «đủ để các ông thỏa mãn …» («để» frame)
    "somanassāya": "niềm vui",                     # «đủ để các ông có niềm vui» («để … có» frame)
    "akkhāto": "được" + GAP + "thuyết giảng",      # svākkhāto «được khéo thuyết giảng»
    "suppaṭipanno saṅgho": "Tăng đoàn thực hành tốt đẹp",
    "veyyākaraṇasmiṃ": "lời giải đáp",
    "bhaññamāne": "khi" + GAP + "đang được nói ra",   # participle keeps «khi» (coordinator rule)
    "akampitthā": "đã rung chuyển",
    # ---- 5-807 / 5-808 «… lòng từ ái … niềm vui đồng cảm… sự bình thản … Đức Thế Tôn là người có lòng trắc ẩn, người
    # mang lại lợi ích cho thế gian, người thương xót thế gian, người hành động vì sự tốt đẹp của thế gian … đã nhập
    # thành tựu thiền của lòng trắc ẩn lớn»
    "kāruṇiko": "người có lòng trắc ẩn", "bhagavā kāruṇiko": "Đức Thế Tôn là người có lòng trắc ẩn",   # inner «là»
    "hito": "người mang lại lợi ích", "caro": "người hành động",   # lokahito / lokatthacaro (head noun kept)
    "mahākaruṇā": "lòng trắc ẩn lớn",
    "mahākaruṇāsamāpattiṃ": "thành tựu thiền của lòng trắc ẩn lớn",   # head noun before its genitive
    "samāpajji": "đã nhập", "bhagavā samāpajji": "Đức Thế Tôn đã nhập",
    "samāpattiṃ samāpajji": "đã nhập thành tựu thiền",   # Vietnamese order
    # ---- 5-809 «phân và nước tiểu … vượt trội hẳn các loại hương thơm khác … Đức Thế Tôn là người ăn hương thơm …
    # ăn cơm và cháo … dùng … để tắm, để thoa, để xoa lên người, cất giữ trong giỏ, đặt vào hộp, bày ra ở chợ»
    "bhagavā bhuñjati": "Đức Thế Tôn ăn",
    "adhiggaṇhāti": "vượt trội",                  # ativiya «hẳn» no keyword
    "bhojī": "người ăn", "bhagavā gandhabhojī": "Đức Thế Tôn là người ăn hương thơm",   # inner «là» kept
    "odana": "cơm", "kummāsaṃ": "cháo",
    "nhāyanti": "tắm", "vilimpanti": "thoa", "ucchādenti": "xoa lên người",   # «để» = purpose frame
    "peḷāya": "giỏ", "paṭisāmenti": "cất giữ", "karaṇḍāya": "hộp", "nikkhipanti": "đặt vào",
    "pasārenti": "bày ra",
    # ---- 5-810 … 5-812 «… bằng một con đường cao quý … sự tham đắm dục lạc … con đường vào dòng đã được Đức Thế Tôn
    # tu tập … các đệ tử … bằng bốn con đường cao quý … đạt được điều chưa đạt được, tự mình chứng nghiệm điều chưa tự
    # mình chứng nghiệm»
    "rāgaṃ": "sự tham đắm",                        # member of kāmarāgaṃ «sự tham đắm dục lạc» (T3 / T4 / T12 / T21)
    "ariyamaggena": "con đường cao quý",
    "maggehi": "con đường",
    "bhāvito": "đã được" + GAP + "tu tập", "bhagavatā bhāvito": "đã được Đức Thế Tôn tu tập",   # Vietnamese order
    "maggo bhāvito": "con đường" + GAP + "đã được" + GAP + "tu tập",
    "adhigacchanti": "đạt được",
    "sacchikataṃ": "tự mình chứng nghiệm",         # of asacchikataṃ «điều chưa tự mình chứng nghiệm» (positive part)
    # ---- 5-813 … 5-816 «… có sự hướng tâm và sự duy trì tâm … vị tỳ-khưu hoàn toàn tách khỏi các dục lạc…»
    "vitakkaṃ vicāraṃ": "sự hướng tâm và sự duy trì tâm",   # savitakkaṃ savicāraṃ (inner «và» kept)
    # ---- 5-819 … 5-822 «định tâm không có sự hướng tâm, chỉ có sự duy trì tâm là tầng thiền trung gian …»
    "samādhi": "định tâm",                         # as written (first everywhere; CROSSCHECK 5-822 «ba sự định tâm»)
    # ---- 5-823 … 5-825 «người đang nhập thành tựu thiền nghe âm thanh … âm thanh là cái gai của tầng thiền thứ
    # nhất … hơi thở vào và hơi thở ra là cái gai … tri giác và cảm giác là cái gai»
    "samāpanno": _NT,
    "samāpanno suṇāti": _NT + " nghe", "samāpanno saddaṃ suṇāti": _NT + " nghe âm thanh",
    "saddo": "âm thanh",                           # «âm thanh là cái gai» (T19 NDE is another text)
    "kaṇṭako": "cái gai",
    "assāsapassāso": "hơi thở vào và hơi thở ra",
    "saññā vedanā": "tri giác và cảm giác",        # saññā ca vedanā ca (inner «và» kept)
}

OVERRIDES = {
    "5-816": {"eva": "hoàn toàn"},                 # first: vivicceva «hoàn toàn tách khỏi» (as map_21 5-673);
                                                   # CROSSCHECK «thật» (Attheva suttanto)
    "5-825": {"vitakko vicāro": "sự hướng tâm sự duy trì tâm"},   # first: vitakko vicāro kaṇṭako «sự hướng tâm, sự duy
                                                   # trì tâm là cái gai» (comma dropped); later vitakkavicārā «… và …»
    "5-826": {"rūpaṃ": "hình sắc",                 # first: Cakkhunā rūpaṃ passati «thấy hình sắc bằng mắt»; CROSSCHECK
                                                   # «vật chất» (rūpena rūpaṃ paṭivijānāti)
              "Rūpena rūpaṃ": "hình sắc bằng vật chất"},   # first: Rūpena rūpaṃ passati «thấy hình sắc bằng vật chất»
                                                   # (Vietnamese order, inner «bằng» kept)
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


def context26(kw, k, kws, text):
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
        v = context26(kw, k, kws, text)
        if v is not None:
            return v
        if k in T26:
            return T26[k]
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
        return value5(kw, kws, T26, text)
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
                src = " [T26]" if lc(kw) in T26 else (" [prior]" if p else "")
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
