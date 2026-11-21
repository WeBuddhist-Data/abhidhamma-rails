"""Build the Pāli->Vietnamese keyword map for pi-5 (Kathāvatthu) chapter 18: 18-dasamavaggo.

usage: python -I -X utf8 -B map_18_vi.py                    (writes 18-dasamavaggo.mapped.md and verifies it)
       python -I -X utf8 -B map_18_vi.py show lo hi [miss]   (segments lo..hi with every pair; writes nothing)
       python -I -X utf8 -B map_18_vi.py ctx bid word ...    (Vietnamese around each word in segment bid)

Importing this module builds nothing (check_parts_vi.py imports it for ALLOWED).
Resolution order per keyword: OVERRIDES[bid][kw] -> context18 (segment rules) -> T18 -> map_5_vi.subject_predicate
-> value5(kw, kws, PRIOR, text) of map_sample_vi, where PRIOR = the finished chapter tables (T2 … T15, as map_10_vi /
map_15_vi) under T18.
Conventions: pi-1 … pi-4 vi-map-conventions*.md + notes-map-*.md, vi-map-conventions-pi5.md, map-coordinator-rules.md;
new values in notes-map-18.md.
"""
import pathlib
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai\mapper-vi")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_vi import (NDE, GAP, build_part, editorial_text, en_ru, join, lc, pick, present,  # noqa: E402
                           read_keywords, read_vietnamese, verify)
from map_sample_vi import FORMULAS, KV, context5, value5  # noqa: E402,F401
import map_2_vi  # noqa: E402
import map_3_vi  # noqa: E402
import map_4_vi  # noqa: E402
import map_5_vi  # noqa: E402
import map_6_vi  # noqa: E402
import map_7_vi  # noqa: E402
import map_8_vi  # noqa: E402
import map_9_vi  # noqa: E402
import map_10_vi  # noqa: E402
import map_11_vi  # noqa: E402
import map_12_vi  # noqa: E402
import map_13_vi  # noqa: E402
import map_14_vi  # noqa: E402
import map_15_vi  # noqa: E402

PART = "18-dasamavaggo"

_YT = "yếu tố đồng hành với tâm"                   # cetasika (T15)
_VT = "vận hành theo"                              # anuparivatti (pi-1 MATRIX cittānuparivattino)
_SH = "có nguyên nhân từ sự thọ trì"               # samādānahetuka
_NC = "người có được"                              # samaṅgī / samaṅgissa (map_13)
_TT = "thuộc thế gian"                             # lokiya (pi-1)
_VTG = "vượt thế gian"                             # lokuttara (pi-1)
_LĐT = "làm đối tượng"                             # X ārabbha «lấy X làm đối tượng»

T18 = {
    # ---- headings «Chương thứ mười»; «(95) 1. Bàn về sự chấm dứt» … «(105) 11. Bàn về việc cho rằng sự không biểu lộ
    # là sự phạm giới»; closers «Phần bàn về … đã hoàn tất.» (kathā / niṭṭhitā: FORMULAS)
    "dasamavaggo": "Chương thứ mười",              # heading and «Chương thứ mười.» (as map_14 / map_15)
    "dasama": "thứ mười",
    "ābhoga": "sự chú hướng",                      # Sābhogātikathā «Bàn về việc cho rằng có sự chú hướng»
    "ābhogaṃ": "sự chú hướng", "ābhogā": "sự chú hướng",   # sābhoga- «có sự chú hướng» / anābhogā «không có sự chú
    "ābhogo": "sự chú hướng",                      # hướng» (positive part)
    "samādāna": "sự thọ trì", "hetu": "nguyên nhân",
    "samādānahetu": "sự thọ trì làm nguyên nhân",  # Samādānahetukathā «Bàn về sự thọ trì làm nguyên nhân»
    "samādānahetukaṃ": _SH,                        # «giới hạnh có nguyên nhân từ sự thọ trì tăng trưởng»
    "samādānahetukaṃ vaḍḍhati": _SH + " tăng trưởng",   # (extraction of Samādānahetukaṃ sīlaṃ vaḍḍhati)
    "samādānahetukaṃ sīlaṃ": "giới hạnh " + _SH,   # head noun first (5-604 uddāna)
    "viññatti sīlaṃ": "sự biểu lộ là giới hạnh", "viññattisīlaṃ": "sự biểu lộ là giới hạnh",   # inner «là» kept
    "aviññatti": "sự không biểu lộ",               # own a- kept
    "dussilya": "sự phạm giới", "dussilyaṃ": "sự phạm giới",
    "sīlya": "giới",                               # of dussilya «sự phạm giới» (positive part: the word for sīla)
    "anuparivatti": _VT, "anuparivattī": _VT,      # cittānuparivattī «vận hành theo tâm»
    "sīlaṃ cittānuparivattī": "giới hạnh " + _VT + " tâm",
    "sīlaṃ na cittānuparivattī": "giới hạnh không " + _VT + " tâm",
    "sammāsamādhi cittānuparivattī": "định tâm đúng đắn " + _VT + " tâm",
    "cetasika": _YT, "cetasikaṃ": _YT, "cetasikā": _YT,   # acetasika- «không phải là yếu tố …» (positive part)
    "sīlaṃ cetasikaṃ": "giới hạnh là " + _YT,
    # ---- 5-571 / 5-572 «khi năm khối tìm cầu sự tái sinh chưa chấm dứt, năm khối mang tính chức năng sinh khởi …
    # sự tụ hợp của mười khối … người đã chết tu tập con đường, người đã qua đời tu tập con đường»
    "upapattesiye": "tìm cầu sự tái sinh",
    "khandhā uppajjanti": "khối" + GAP + "sinh khởi",   # «năm khối mang tính chức năng sinh khởi» (subject first)
    "uppajjanti": "sinh khởi",                     # (T15 «xuất hiện» is another text; T10 «sinh khởi»)
    "dasannaṃ": "mười",                            # keyword with its numeral keeps it (pi-3)
    "niruddhe": "chấm dứt",                        # aniruddhe «chưa chấm dứt» (positive part), «đã sinh khởi rồi chấm dứt»
                                                   # (T14); «đã chấm dứt» by override where the text says so
    "mato": "người đã chết", "kālaṅkato": "người đã qua đời",   # T15 kālaṅkatā
    # ---- 5-573 … 5-575 «vật chất của người có được con đường là con đường … có đối tượng, nó có sự hướng đến, sự chú
    # hướng, sự lưu ý, sự chú tâm, chủ ý, sự mong ước, sự mong cầu»
    "maggasamaṅgissa": _NC + " con đường", "maggasamaṅgī": _NC + " con đường",   # head noun first
    "samaṅgī": _NC, "samaṅgissa": _NC,
    "cakkhuviññāṇasamaṅgissa": _NC + " thức qua mắt",
    "maggasamaṅgī samannāgato": _NC + " con đường được trang bị",
    "ārammaṇaṃ": "có đối tượng", "ārammaṇā": "có đối tượng",   # sārammaṇa / anārammaṇa «(không) có đối tượng»;
                                                   # uppannārammaṇā «có đối tượng đã sinh khởi» (notes-map-15)
    # ---- 5-576 «năm loại thức có chỗ dựa đã sinh khởi, có đối tượng đã sinh khởi … có chỗ dựa đã sinh ra trước …
    # có chỗ dựa thuộc phần bên trong, có đối tượng thuộc phần bên ngoài, có chỗ dựa chưa tan rã … có chỗ dựa khác
    # nhau … không trải nghiệm phạm vi hoạt động của nhau, không sinh khởi khi không có sự lưu ý, không sinh khởi khi
    # không chú tâm, không sinh khởi liền mạch, … không sinh khởi liền sau nhau … không có sự chú hướng»
    "vatthukā": "có chỗ dựa",
    "purejāta": "đã sinh ra trước",
    "bāhira": "thuộc phần bên ngoài",              # as ajjhattika «thuộc phần bên trong» (pi-1 bāhirā)
    "visayaṃ": "phạm vi hoạt động",                # gocaravisayaṃ «phạm vi hoạt động» (the compound as a whole)
    "samannāhārā": "sự lưu ý",                     # of asamannāhārā «khi không có sự lưu ý» (positive part)
    "manasikārā": "chú tâm",                       # of amanasikārā «khi không chú tâm» (positive part, as written)
    "samanantarā": "liền sau",                     # aññamaññassa samanantarā «liền sau nhau» («nhau» = aññamañña)
    "samanantarā uppajjanti": "sinh khởi liền sau",   # Vietnamese order («không sinh khởi liền sau nhau»)
    # ---- 5-577 … 5-586 «thức qua mắt lấy sự trống rỗng làm đối tượng mà sinh khởi … tùy thuộc vào mắt và sự trống
    # rỗng, sinh khởi thức qua mắt … lấy sự tiếp xúc làm đối tượng … lấy vật xúc chạm làm đối tượng»
    "viññāṇa": "loại thức", "viññāṇā": "loại thức",   # pañcaviññāṇa «năm loại thức» (the text's classifier, pi-1
                                                      # «loại dưỡng chất»)
    "suññataṃ": "sự trống rỗng",
    "ārabbha": "lấy" + GAP + _LĐT,
    "ārabbha uppajjati": "lấy" + GAP + _LĐT + " mà sinh khởi",   # inner «mà» kept
    "suññataṃ ārabbha": "lấy sự trống rỗng " + _LĐT,             # Vietnamese order
    "phassaṃ ārabbha": "lấy sự tiếp xúc " + _LĐT,
    "phoṭṭhabbaṃ ārabbha": "lấy vật xúc chạm " + _LĐT,
    "cakkhuviññāṇaṃ uppajjati": "thức qua mắt" + GAP + "sinh khởi",   # subject first (coordinator rule)
    "manoviññāṇaṃ uppajjati": "ý thức" + GAP + "sinh khởi",
    "paṭicca": "tùy thuộc vào",                    # «tùy thuộc vào mắt và sự trống rỗng» (map_14 context14)
    "cakkhuviññāṇaṃ sābhogaṃ": "thức qua mắt có sự chú hướng",
    # 5-579 sutta «vị tỳ-khưu khi thấy hình sắc bằng mắt thì không nắm giữ dấu hiệu tổng quát, không nắm giữ các chi
    # tiết… khi nghe âm thanh bằng tai… khi ngửi mùi bằng mũi… khi nếm vị bằng lưỡi… khi chạm vật xúc chạm bằng thân»
    "anubyañjana": "chi tiết",                     # «các chi tiết» («các» dropped)
    "gandhaṃ": "mùi",                              # (T15 «hương thơm» is the gift list)
    "sutvā": "khi nghe", "ghāyitvā": "khi ngửi", "sāyitvā": "khi nếm", "phusitvā": "khi chạm",   # the text's «khi»
    # ---- 5-587 / 5-588 «người có được con đường được trang bị hai giới hạnh … sự tiếp xúc thuộc thế gian … giới
    # hạnh thuộc thế gian và vượt thế gian … lời nói đúng đắn thuộc thế gian … là người phàm phu»
    "lokiyena": _TT, "lokiyāya": _TT, "lokuttarena": _VTG, "lokuttarāya": _VTG,
    "lokiyena lokuttarena": _TT + " và " + _VTG, "lokiyāya lokuttarāya": _TT + " và " + _VTG,   # inner «và» kept
    "lokiyena vīriyena": "sự tinh tấn " + _TT, "lokiyāya saddhāya": "niềm tin " + _TT,
    "lokiyāya paññāya": "trí tuệ " + _TT,
    "lokiyāya samannāgato": "được trang bị" + GAP + _TT,   # «được trang bị lời nói đúng đắn thuộc thế gian»
    # 5-589 «người phạm giới, có giới hạnh bị sứt mẻ, có giới hạnh bị cắt đứt»
    "khaṇḍa": "bị sứt mẻ",
    # ---- 5-590 … 5-594 «… có kết quả đáng mong muốn … có kết quả, có quả trổ … khi giới hạnh đã sinh khởi rồi chấm
    # dứt, thì trở thành người phạm giới … Vậy thì giới hạnh không phải là …»
    "phalaṃ": "kết quả",                           # iṭṭhaphalaṃ / saphalaṃ «có kết quả …» (map_10 with dāna, KV)
    "uppajjitvā": "đã sinh khởi rồi",              # as T14 uppajja (the text's «đã»; map_10 «sinh khởi rồi» where the
                                                   # text has no «đã»)
    "tena hi sīlaṃ": "Vậy thì giới hạnh",          # as T15 tena hi puññaṃ
    # ---- 5-598 «tăng trưởng như dây leo … như đám cỏ lau»; 5-599 «đối với người đã thọ trì giới hạnh rồi khởi lên sự
    # hướng tâm đến dục lạc … giáo pháp của người hiền thiện ở xa kẻ không hiền thiện»
    "samādiyitvā": "đã thọ trì" + GAP + "rồi",     # gerund «đã thọ trì … rồi» (as T14 uppajja «… rồi»)
    "vitakkentassa": "khởi lên",                   # T15 vitakketi (the «người» stands before «đã thọ trì»)
    "asabbhi": "kẻ không hiền thiện",              # as T15 asataṃ (own a- kept)
    # 5-600 verse «… đứng vững trong Giáo Pháp, thành tựu về giới hạnh, những người ấy đi đến cõi trời»
    "dhamma": "Giáo Pháp",                         # dhammaṭṭhā «đứng vững trong Giáo Pháp»
    "vana": "rừng",
    # ---- 5-601 «sự kiềm chế việc sát hại sinh mạng … sự đảnh lễ là giới hạnh, sự đứng dậy chào đón …, sự chắp tay …,
    # sự kính cẩn đúng phép …, việc mang đến chỗ ngồi …, … chỗ nằm …, … nước rửa chân …, … miếng chà chân …, việc chà
    # lưng khi tắm là giới hạnh»
    "abhivādanaṃ": "sự đảnh lễ", "paccuṭṭhānaṃ": "sự đứng dậy chào đón",
    "añjalikammaṃ": "sự chắp tay", "añjali": "chắp tay",
    "kammaṃ": NDE,                                 # añjalikammaṃ / sāmīcikammaṃ: no word of its own («sự» belongs to the
                                                   # whole compound)
    "sāmīci": "kính cẩn đúng phép",
    "abhihāro": "việc mang đến", "seyyā": "chỗ nằm", "pāda": "chân",
    "pādakathalikā": "miếng chà chân",
    "nhāne": "tắm",                                # «khi tắm»: the locative frame «khi» dropped (as «trong» / «ở»)
    "parikammaṃ": "việc chà",                      # piṭṭhiparikammaṃ «việc chà lưng»
    "vādā": "việc nói", "vādo": "việc nói",        # musāvādā / musāvādo «việc nói dối» (T15 vādaṃ)
    "ādānā": "việc lấy",                           # adinnādānā «việc lấy của không được cho» (T15 ādānaṃ)
    # ---- 5-603 «đối với người đã thọ trì nghiệp xấu ác rồi thực hiện sự bố thí, cả phước và điều không phải phước,
    # cả hai đều tăng trưởng»; 5-604 «Chẳng phải đã thọ trì nghiệp xấu ác sao?»
    "pāpa": "xấu ác",                              # pāpakammaṃ «nghiệp xấu ác» (KV pāpakāni)
    "dadantassa": "thực hiện",                     # dānaṃ dadantassa «thực hiện sự bố thí» (T15 deti)
    "apuññaṃ": "điều không phải phước",            # own a- kept; the text's «điều»
    "samādinno": "đã thọ trì",
    # ---- 5-604 uddānas «Chương thứ mười. Tóm tắt của chương này – …» «Nhóm năm mươi thứ hai. … Sự cố định, sự gộp
    # vào, cõi tái sinh, lợi ích, và sự chấm dứt [dị bản …]»
    "ānisaṃsa": "lợi ích",
    "atthi": "có",                                 # pañcaviññāṇasamaṅgissa atthi maggabhāvanā «… có sự tu tập con đường»
                                                   # (existential «có», sample)
    "saṅgaha": "sự gộp vào",
}

PRIOR = {**map_7_vi.T7, **map_6_vi.T6, **map_5_vi.T5, **map_4_vi.T4, **map_2_vi.T2, **map_3_vi.T3,
         **map_8_vi.T8, **map_9_vi.T9, **map_10_vi.T10, **map_11_vi.T11, **map_12_vi.T12, **map_13_vi.T13,
         **map_14_vi.T14, **map_15_vi.T15, **T18}


def context18(kw, k, kws, text):
    """Segment rules of this chapter (k: lower-cased keyword). None = no rule."""
    s = set(lc(x) for x in kws)
    if k in ("samādhi", "samādhinā", "samādhīhi", "sati", "satiyā", "satīhi"):   # the factor «sự định tâm» / «sự
        bare = "định tâm" if k.startswith("samādh") else "tỉnh thức"            # tỉnh thức» (T15) / only inside
        if s & {"sammā", "sammāsamādhi cittānuparivattī"}:                     # «… đúng đắn» (path segments:
            return bare                                                       # pi-1 SATI_BARE)
        return pick(text, "sự " + bare, bare)
    if k == "rūpaṃ":               # the aggregate «vật chất» / the visible object «hình sắc» (sutta 5-579 …)
        return pick(text, "vật chất", "hình sắc")
    if k == "rūpa" and "rūpāyatanaṃ" in s:         # rūpāyatanaṃ «lĩnh vực hình sắc»
        return "hình sắc"
    if k == "cakkhuviññāṇaṃ kusalaṃ":              # «thức qua mắt là thiện» (5-581) / «thức qua mắt vừa là thiện vừa
        return pick(text, "thức qua mắt là thiện", "thức qua mắt vừa là thiện")   # là bất thiện» (5-582)
    if k == "manoviññāṇaṃ kusalaṃ":
        return pick(text, "ý thức là thiện", "ý thức vừa là thiện")
    return None


OVERRIDES = {
    "5-572": {"niruddhe": "đã chấm dứt"},          # «khi năm khối tìm cầu sự tái sinh đã chấm dứt» (KV)
    "5-589": {"niruddhe": "đã chấm dứt"},          # «khi giới hạnh thuộc thế gian đã chấm dứt»
    "5-599": {"pathavī": "mặt đất"},               # Nabhañca pathavī ca «bầu trời và mặt đất» (map_15 ^5-485)
    "5-603": {"pathavī": "mặt đất"},
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
        v = context18(kw, k, kws, text)
        if v is not None:
            return v
        if k in T18:
            return T18[k]
        if k not in PRIOR:
            v = map_5_vi.subject_predicate(kw, kws, text)
            if v:
                return v
        return value5(kw, kws, PRIOR, text)
    return resolve


def _prior_values(k):
    out = {}
    for n, m in ((2, map_2_vi), (3, map_3_vi), (4, map_4_vi), (5, map_5_vi), (6, map_6_vi), (7, map_7_vi),
                 (8, map_8_vi), (9, map_9_vi), (10, map_10_vi), (11, map_11_vi), (12, map_12_vi), (13, map_13_vi),
                 (14, map_14_vi), (15, map_15_vi)):
        t = getattr(m, f"T{n}", {})
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
                p = _prior_values(lc(kw))
                ps = (" T:" + str(sorted(set(x for x in p.values() if x != v)))) if p and any(
                    x != v for x in p.values()) else ""
                print(f"   {kw}={v}  [ru:{e[1]}]{ps}{flag}")


def ctx(bid, words, width=60):
    t = editorial_text(read_vietnamese(PART).get(bid, ""))
    low = t.lower()
    for w in words:
        pos = low.find(w.lower())
        n = 0
        while pos >= 0 and n < 3:
            print(f"[{w}] …{t[max(0, pos - width):pos + len(w) + width]}…".replace("\n", " / "))
            pos = low.find(w.lower(), pos + 1)
            n += 1
        if n == 0:
            print(f"[{w}] (absent)")


_FINISHED = ["preamble", "1-puggalakatha", "2-parihanikatha", "3-brahmacariyakatha", "4-jahatikatha",
             "5-sabbamatthitikatha", "6-atitakkhandhadikatha", "7-ekaccam-atthitikatha", "8-satipatthanakatha",
             "9-hevatthikatha", "10-dutiyavaggo", "11-tatiyavaggo", "12-catutthavaggo", "13-pancamavaggo",
             "14-chatthavaggo", "15-sattamavaggo"]


def look(words):
    """values of each keyword in the finished pi-5 mapped files (named one by one; reference only)."""
    from collections import Counter
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
            bid, _, rest = line.partition("] ")
            for pair in rest.split(", "):
                kw, _, v = pair.partition("=")
                if lc(kw) in found:
                    found[lc(kw)][(v, part.split("-")[0])] += 1
    for k, c in found.items():
        print(want[k], dict(c.most_common(8)))


if __name__ == "__main__":
    if sys.argv[1:2] == ["look"]:
        look(sys.argv[2:])
    elif sys.argv[1:2] == ["show"]:
        show(int(sys.argv[2]), int(sys.argv[3]), "miss" in sys.argv[4:])
    elif sys.argv[1:2] == ["ctx"]:
        ctx(sys.argv[2], sys.argv[3:])
    else:
        build_part(PART, resolver())
        verify(PART, ALLOWED)
