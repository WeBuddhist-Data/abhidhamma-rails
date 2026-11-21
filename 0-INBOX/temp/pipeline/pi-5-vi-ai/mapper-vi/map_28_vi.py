"""Build the Pāli->Vietnamese keyword map for pi-5 (Kathāvatthu) chapter 28: 28-visatimavaggo.

usage: python -I -X utf8 -B map_28_vi.py                    (writes 28-visatimavaggo.mapped.md and verifies it)
       python -I -X utf8 -B map_28_vi.py show lo hi [miss]   (segments lo..hi with every pair, English | Russian and
                                                             the finished chapters' values where they differ; writes
                                                             nothing)
       python -I -X utf8 -B map_28_vi.py dump [miss]         (every distinct keyword=value; writes nothing)
       python -I -X utf8 -B map_28_vi.py look kw ...         (finished chapter tables, pi-1 … pi-4 map values)
       python -I -X utf8 -B map_28_vi.py mlook kw ...        (values in the finished pi-5 mapped files)

Importing this module builds nothing (check_parts_vi.py imports it for ALLOWED).
Resolution order per keyword: OVERRIDES[bid][kw] -> context28 (segment rules of this chapter) -> T28 -> context5 ->
the finished chapter tables T27, T24 … T2 (latest first; a value counts only where it stands in this segment, as
map_24_vi / map_27_vi) -> map_5_vi.subject_predicate (coordinator rule) -> value5(kw, kws, T28, text) of map_sample_vi
(FORMULAS -> KV -> two-word composition -> the pi-4 chain).
Conventions: pi-1 … pi-4 vi-map-conventions*.md + notes-map-*.md, vi-map-conventions-pi5.md, map-coordinator-rules.md;
new values in notes-map-28.md.
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

PART = "28-visatimavaggo"

_AN = "người tạo nghiệp có quả không gián đoạn"     # ānantariko (agent noun with its head noun)
_KCG = "kẻ canh giữ"                               # pāla / pālā
_NP = _KCG + " địa ngục"                           # nirayapālā («những kẻ canh giữ địa ngục»: «những» dropped)
_DS = "với tri giác rằng đó là Giáo Pháp"          # dhammasaññī (inner «rằng đó là» kept, coordinator rule)
_SB = "kẻ chia rẽ Tăng đoàn"                       # saṅghabhedako
_TCP = "gồm tám chi phần cao quý"                  # ariyo aṭṭhaṅgiko (Vietnamese order)
_CĐ = "con đường"

T28 = {
    # ---- headings «Chương thứ hai mươi» (repeated before every discussion), «(194) 1. Bàn về việc không cố ý» …
    # «(199) 6. Bàn về hiểu biết»; closers «Phần bàn về … đã hoàn tất.» (kathā / niṭṭhitā: FORMULAS)
    "vīsatimavaggo": "Chương thứ hai mươi",        # heading and «Chương thứ hai mươi.» (as map_27)
    "vīsatima": "thứ hai mươi",
    "asañcicca": "việc không cố ý",                # heading / closer Asañciccakathā (own a- kept; the text's «việc»);
                                                   # the adverb Asañcicca: context28
    "ñāṇa": "hiểu biết",                           # Ñāṇakathā «Bàn về hiểu biết» (T17 «biết» is another compound)
    "ñāṇakathā": "Bàn về hiểu biết",
    "nirayapālakathā": "Bàn về những " + _NP,      # inner «những» kept (as T24 «Bàn về những gì …»)
    "nirayapāla": _NP, "pāla": _KCG, "pālā": _KCG, "nirayapālā": _NP,
    # ---- 5-857 / 5-858 «người không cố ý tước đoạt mạng sống của mẹ trở thành người tạo nghiệp có quả không gián
    # đoạn … người không cố ý sát hại sinh mạng trở thành người sát hại sinh mạng … nói dối trở thành người nói dối»
    "ānantariko": _AN,
    "voropetvā": "tước đoạt",                      # gerund: no «sau khi» in the text
    "mātaraṃ voropetvā": "tước đoạt" + GAP + "mẹ",   # as T20 pāṇaṃ voropeyya
    "asañcicca voropetvā": "không cố ý tước đoạt",   # as T20 sañcicca voropeyya
    "asañcicca hantvā": "không cố ý sát hại",
    "hantvā": "sát hại",
    "atipātī": "người sát hại",                    # pāṇātipātī «người sát hại sinh mạng» (agent noun, head noun kept)
    "vādī": "người nói",                           # musāvādī «người nói dối» (not the speaker-note «người theo học thuyết»)
    "bhaṇitvā": "nói",                             # musā bhaṇitvā «nói dối»
    # ---- 5-859 «kẻ giết mẹ / cha / bậc A-la-hán là người tạo nghiệp …, kẻ làm chảy máu là …» (members as map_10)
    "mātughātako": "kẻ giết mẹ", "pitughātako": "kẻ giết cha", "ruhiruppādako": "kẻ làm chảy máu",
    # ---- 5-860 … 5-862 «kẻ chia rẽ Tăng đoàn với tri giác rằng đó là Giáo Pháp là người tạo nghiệp …»; «… không thể
    # cứu chữa»; verse as T21
    "saṅghabhedako": _SB, "saṅghabhedakā": _SB,    # «tất cả những kẻ chia rẽ Tăng đoàn» («những» dropped)
    "dhammasaññī": _DS,
    "saññī": "với tri giác",                       # -ī «with perception» keeps its «với» (as pi-1 saññī «có tri giác»)
    "dhammasaññī saṅghabhedako": _SB + " " + _DS,  # Vietnamese order
    "dhammasaññī ānantariko": _DS + " là " + _AN,  # inner «là» kept
    "atekiccho": "không thể cứu chữa",             # own a- kept
    # ---- 5-863 … 5-865 «người phàm phu không có trí tuệ … có thể nhập tầng thiền thứ nhất … có thể thực hiện sự bố
    # thí… có thể cho y phục …»
    "puthujjanassa paññā": "người phàm phu" + GAP + "trí tuệ",   # «người phàm phu không có / có trí tuệ» («có» frame)
    "samāpajjeyya": "nhập",                        # optative: the bare verb (coordinator rule; T13 «có thể nhập»)
    "puthujjano samāpajjeyya": "người phàm phu" + GAP + "nhập",
    "puthujjano dadeyya": "người phàm phu" + GAP + "thực hiện",  # first dānaṃ dadeyya «có thể thực hiện sự bố thí»
                                                   # (T21 kappaṭṭho dadeyya); CROSSCHECK «có thể cho y phục»
    # ---- 5-866 / 5-867 «trong các địa ngục có các hình phạt, và có những người thi hành hình phạt … giữa loài người»;
    # verse «Không phải Tỳ-xá-phù, cũng không phải vua của loài ngạ quỷ, Soma, Yama … Chính các nghiệp của mình đánh
    # đập ở đó, người bị đẩy đi khỏi đây …»
    "nirayesu": "địa ngục",                        # «trong các địa ngục» (frame «trong các» dropped)
    "kammakāraṇā": "hình phạt",
    "paṇunnaṃ": "bị đẩy đi", "somo": "Soma", "yamo": "Yama", "hananti": "đánh đập",
    # ---- 5-868 MN 3.250 «những kẻ canh giữ địa ngục bắt người ấy chịu hình phạt gọi là sự trói buộc năm cách – chúng
    # đóng một cây cọc sắt nung đỏ vào một bàn tay … vào một bàn chân … vào giữa ngực; … cảm giác khó chịu, dữ dội, cay
    # đắng … đặt người ấy nằm xuống rồi đẽo bằng búa … dựng người ấy chân lên trên, đầu xuống dưới rồi đẽo bằng rìu …
    # buộc người ấy vào xe rồi bắt chạy tới, chạy lui trên mặt đất đang bốc cháy, rực lửa, cháy sáng … bắt người ấy
    # leo lên và leo xuống một ngọn núi than hồng lớn … ném vào một vạc đồng nung nóng … bị nấu sôi sùng sục bọt … có
    # lúc đi ngang … ném người ấy vào đại địa ngục» and the verses «Có bốn góc, có bốn cửa, được phân chia, được đo theo
    # từng phần; Có tường sắt bao quanh, được che phủ bằng sắt. Nền của nó làm bằng sắt, rực cháy, đầy sức nóng; Tỏa
    # ra khắp mọi phía một trăm do-tuần, luôn luôn tồn tại»
    "kārenti": "bắt" + GAP + "chịu", "nirayapālā kārenti": _NP + " bắt" + GAP + "chịu",
    "kāraṇaṃ": "hình phạt", "pañcavidha": "năm cách",
    "tattaṃ": "nung đỏ", "ayokhīlaṃ": "cây cọc sắt",   # the text's classifier «cây» kept («một» = numeral frame)
    "tattaṃ ayokhīlaṃ": "cây cọc sắt nung đỏ",     # Vietnamese order
    "hatthe": "bàn tay", "pāde": "bàn chân",       # «vào một bàn tay / bàn chân»
    "gamenti": "đóng", "majjhe": "giữa", "urasmiṃ": "ngực",
    "tibbā": "dữ dội", "kaṭukā": "cay đắng",
    "saṃvesetvā": "đặt" + GAP + "nằm xuống", "nirayapālā saṃvesetvā": _NP + " đặt" + GAP + "nằm xuống",
    "kuṭhārīhi": "búa", "vāsīhi": "rìu", "tacchanti": "đẽo",   # «đẽo bằng búa / rìu» (instrumental «bằng» frame)
    "nirayapālā ṭhapetvā": _NP + " dựng",          # «dựng người ấy chân lên trên, đầu xuống dưới»
    "pādaṃ": "chân", "siraṃ": "đầu",               # uddhampādaṃ adhosiraṃ «chân lên trên, đầu xuống dưới»
    "rathe": "xe", "yojetvā": "buộc", "nirayapālā yojetvā": _NP + " buộc",
    "ādittāya": "đang bốc cháy", "pathaviyā": "mặt đất", "sampajjalitāya": "rực lửa", "sajotibhūtāya": "cháy sáng",
    "paccāsārenti": "chạy lui",                    # sārentipi paccāsārentipi «bắt chạy tới, chạy lui»
    "aṅgāra": "than hồng",                         # aṅgārapabbataṃ «ngọn núi than hồng»
    "āropenti": "bắt" + GAP + "leo lên",           # causative «bắt người ấy leo lên» (as kārenti)
    "loha": "đồng", "kumbhiyā": "vạc",             # lohakumbhiyā «một vạc đồng»
    "pakkhipanti": "ném", "nirayapālā pakkhipanti": _NP + " ném",
    "pheṇa": "bọt", "uddehakaṃ": "sùng sục",       # pheṇuddehakaṃ paccati «bị nấu sôi sùng sục bọt»
    "tiriyaṃ": "ngang",                            # tiriyaṃ gacchati «đi ngang»
    "mahāniraye": "đại địa ngục",
    "kaṇṇo": "góc", "vibhatto": "được phân chia", "bhāgaso": "theo từng phần", "mito": "được đo",
    "pākāra": "tường", "pariyanto": "bao quanh", "paṭikujjito": "được che phủ",
    "bhūmi": "nền",                                # Tassa ayomayā bhūmi «Nền của nó» (T-value «mặt đất» is pathaviyā)
    "tejasā": "sức nóng", "yojana": "do-tuần",
    "pharitvā": "tỏa ra",                          # gerund: no «sau khi» in the text
    "tiṭṭhati": "tồn tại", "sabbadā": "luôn luôn",   # «luôn luôn tồn tại» (KV «vào mọi lúc» another text)
    "sabbattha": "tất cả các bản",                 # only the variant label «[khác chính tả (tất cả các bản): …]»
    # ---- 5-869 … 5-871 «giữa chư thiên có loài súc sinh … thế giới chư thiên là cõi súc sinh … sâu bọ, châu chấu,
    # muỗi, ruồi, rắn, bọ cạp, rết, giun đất … con voi chúa tên là Ê-ra-va-na, cỗ xe cõi trời được thắng một nghìn con
    # … những người giữ voi, những người giữ ngựa, những người cung cấp cỏ, những người huấn luyện, những người nấu
    # thức ăn»
    "tiracchānagatā": "loài súc sinh",             # as KV tiracchānagato
    "tiracchānayonī": "cõi súc sinh", "yonī": "cõi",   # as T20 tiracchānayoniṃ
    "kīṭā": "sâu bọ", "paṭaṅgā": "châu chấu", "makasā": "muỗi", "ahī": "rắn", "vicchikā": "bọ cạp",
    "satapadī": "rết", "gaṇḍuppādā": "giun đất",
    "hatthināgo": "con voi chúa",                  # the text's classifier «con» kept
    "sahassa": "nghìn",                            # as sataṃ «trăm» («một» = numeral frame)
    "yuttaṃ": "được thắng", "yānaṃ": "cỗ xe",
    "bandhā": "người giữ", "yāvasikā": "người cung cấp cỏ", "bhattakārakā": "người nấu thức ăn",
    # ---- 5-872 … 5-875 «con đường gồm năm / tám chi phần … Tối thắng trong các con đường là con đường gồm tám chi
    # phần, trong các sự thật là bốn câu; Tối thắng trong các hiện tượng là sự lìa tham, và giữa loài hai chân là bậc
    # có mắt» / «Ngay từ trước, nghiệp bằng thân … đã hoàn toàn thanh tịnh; … con đường gồm tám chi phần cao quý này …
    # đi đến sự viên mãn của sự tu tập» / DN 2.214 «trong Giáo Pháp và Giới Luật nào … Các học thuyết của người khác
    # trống rỗng, không có các sa-môn khác»
    "tena hi maggo": "Vậy thì " + _CĐ,
    "maggānaṃ": _CĐ, "seṭṭho": "tối thắng", "padā": "câu", "virāgo": "sự lìa tham",
    "dvipadānaṃ": "loài hai chân",                 # the text's classifier «loài» (as tiracchānagatā)
    "pubbe": "từ trước",                           # pubbeva «Ngay từ trước» (eva = ngay: OVERRIDES)
    "parisuddho": "thanh tịnh",                    # suparisuddho «đã hoàn toàn thanh tịnh»
    "pāripūriṃ": "sự viên mãn",                    # bhāvanāpāripūriṃ «sự viên mãn của sự tu tập»
    "ariyo": "cao quý",                            # pi-4 ariya «cao quý» (T2 «bậc thánh» is ariyapuggala)
    "ariyo aṭṭhaṅgiko": _TCP, "ariyo aṭṭhaṅgiko maggo": _CĐ + " " + _TCP,
    "ariyo maggo": _CĐ + GAP + "cao quý",
    "samaṇo upalabbhati": "sa-môn" + GAP + "được tìm thấy",   # subject first («sa-môn cũng (không) được tìm thấy»)
    "samaṇebhi": "sa-môn", "pavādā": "học thuyết", "suññā": "trống rỗng",
    "subhadda": "Subhadda", "yasmiṃ": "nào",       # yasmiṃ … dhammavinaye «trong Giáo Pháp và Giới Luật nào»
    # ---- 5-876 / 5-877 «hiểu biết có mười hai chủ đề là vượt thế gian … mười hai hiểu biết vượt thế gian … mười hai
    # con đường vào dòng» / SN 5.1081 «trong những điều chưa từng được nghe trước đây, con mắt đã khởi lên …»
    "vatthukaṃ": "có" + GAP + "chủ đề",            # numeral dropped (as pi-3 vokāra «gồm … khối»)
    "dvādasavatthukaṃ": "có mười hai chủ đề",
    "dvādasavatthukaṃ ñāṇaṃ": "hiểu biết có mười hai chủ đề",   # head noun first
    "lokuttarañāṇāni": "hiểu biết vượt thế gian",
    "dvādasa sotāpattimaggā": "mười hai " + _CĐ + " vào dòng",
    "dhammesu": "điều",                            # ananussutesu dhammesu «những điều chưa từng được nghe» (pi-4)
    "cakkhuṃ": "con mắt",                          # the text's classifier (T3 / T10 same quote)
    "dukkhasamudayo": NDE,                         # only in the bracket [khác chính tả (…): dukkhasamudayo]
    # ---- uddāna «Sự chế ngự, sự tích lũy phước, đã sống, với quá khứ, và kẻ giết mẹ.»
    "puññasañcayo": "sự tích lũy phước", "sañcayo": "sự tích lũy",
    "aṭṭhāsi": "đã sống",
}

OVERRIDES = {
    "5-868": {"karonti": NDE},                     # only in the bracket [dị bản (Trung Bộ Kinh 3.250; …): karonti]
    "5-874": {"eva": "ngay"},                      # first: pubbeva «Ngay từ trước»; CROSSCHECK Attheva «thật»
    "5-875": {"eva": "chính"},                     # first: Idheva «chính ở đây»; CROSSCHECK Attheva «thật»
}

ALLOWED = {
}

_DONE = list(range(2, 28)) + [29]                  # finished chapters (30 / 31 are being mapped at the same time)


def _tables():
    """[(chapter, table)] of the finished chapters (2 … 27, 29)."""
    out = []
    for n in _DONE:
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


def context28(kw, k, kws, text):
    """Segment rules of this chapter (k: lower-cased keyword). None = no rule."""
    s = set(lc(x) for x in kws)
    if k == "asañcicca":           # heading / closer «việc không cố ý» / the adverb «người không cố ý tước đoạt …»
        return pick(text, "việc không cố ý", "không cố ý")
    if k == "tiracchāna":          # member of tiracchānayonī / -gatā «súc sinh» / heading «Bàn về loài súc sinh»
        return "súc sinh" if "tiracchānayonī" in s else "loài súc sinh"
    if k == "kāraṇikā":            # 5-866 «người thi hành hình phạt» / 5-871 «người huấn luyện»
        return pick(text, "người thi hành hình phạt", "người huấn luyện")
    if k == "paccati":             # 5-868 «bị nấu sôi» / verse 5-862 «bị nung đốt» (T21)
        return pick(text, "bị nấu sôi", "bị nung đốt")
    return None


def resolver():
    vi = read_vietnamese(PART)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        text = vi.get(bid, "")
        k = lc(kw)
        v = context28(kw, k, kws, text)
        if v is not None:
            return v
        if k in T28:
            return T28[k]
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
        return value5(kw, kws, T28, text)
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
                src = " [T28]" if lc(kw) in T28 else (" [prior]" if p else "")
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
