"""Build the Pāli->Vietnamese keyword map for pi-5 (Kathāvatthu) chapter 19: 19-ekadasamavaggo.

usage: python -I -X utf8 -B map_19_vi.py                    (writes 19-ekadasamavaggo.mapped.md and verifies it)
       python -I -X utf8 -B map_19_vi.py show lo hi [miss]   (segments lo..hi with every pair; writes nothing)
       python -I -X utf8 -B map_19_vi.py ctx bid word ...    (Vietnamese around each word in segment bid)
       python -I -X utf8 -B map_19_vi.py look kw ...         (values in the finished pi-5 mapped files)

Importing this module builds nothing (check_parts_vi.py imports it for ALLOWED).
Resolution order per keyword: OVERRIDES[bid][kw] -> context19 (segment rules) -> T19 -> map_5_vi.subject_predicate
-> value5(kw, kws, PRIOR, text) of map_sample_vi, where PRIOR = the finished chapter tables (T2 … T15, T18, as
map_18_vi) under T19.
Conventions: pi-1 … pi-4 vi-map-conventions*.md + notes-map-*.md, vi-map-conventions-pi5.md, map-coordinator-rules.md;
new values in notes-map-19.md.
"""
import pathlib
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai\mapper-vi")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_vi import (NDE, GAP, build_part, editorial_text, en_ru, join, lc, pick, present,  # noqa: E402
                           read_keywords, read_vietnamese, verify)
from map_sample_vi import FORMULAS, KV, context5, value5  # noqa: E402,F401
import map_5_vi  # noqa: E402
import map_18_vi  # noqa: E402

PART = "19-ekadasamavaggo"

_KT = "khuynh hướng tiềm ẩn"                        # anusaya (earlier chapters)
_KG = "không gắn liền với tâm"                     # cittavippayutta
_SM = "sức mạnh thần thông"                        # iddhibala
_HT = "được hình thành trọn vẹn"                   # parinipphanna
_LT = "sự liên tục của tâm"                        # cittasantati

T19 = {
    # ---- headings «Chương thứ mười một»; «(106-108) 1-3. Bàn về cả ba loại khuynh hướng tiềm ẩn», «Bàn về hiểu
    # biết», «Bàn về việc cho rằng hiểu biết không gắn liền với tâm», «Bàn về việc nói rằng đây là khổ đau», «Bàn về
    # sức mạnh thần thông», «Bàn về sự định tâm», «Bàn về sự ổn định của các hiện tượng», «Bàn về tính vô thường»
    "ekādasamavaggo": "Chương thứ mười một",       # heading and «Chương thứ mười một.» (as T18 dasamavaggo)
    "ekādasama": "thứ mười một",
    "anusaya": _KT,                                # Tissopi anusayakathā «… cả ba loại khuynh hướng tiềm ẩn»
    "vippayutta": "không gắn liền",
    "ñāṇaṃ cittavippayutta": "hiểu biết " + _KG,   # heading and «“hiểu biết không gắn liền với tâm”» (5-617)
    "iddhibala": _SM, "iddhibalena": _SM, "balena": "sức mạnh",
    # ---- 5-605 … 5-613 «khuynh hướng tiềm ẩn ác cảm / kiêu mạn / tham đắm hiện hữu …; sự ác cảm, sự ám ảnh của ác
    # cảm, xiềng xích ác cảm …; dòng lũ vô minh, ách vô minh» (members = the compound's form, pi-1)
    "paṭigha": "ác cảm", "māna": "kiêu mạn",       # not «sự …»: the text has only «… ác cảm / kiêu mạn» in 5-607, 5-611
    "rāga": "tham đắm",                            # first: Kāmarāgānusayo «khuynh hướng tiềm ẩn tham đắm dục lạc»
    "bhava": "hiện hữu",                           # bhavarāga «tham đắm hiện hữu»
    "yogo": "ách",                                 # avijjāyogo / kāmayogo «ách vô minh / ách dục lạc» (pi-1 ách)
    "paṭighapariyuṭṭhānaṃ": "sự ám ảnh của ác cảm", "mānapariyuṭṭhānaṃ": "sự ám ảnh của kiêu mạn",
    "bhavarāgapariyuṭṭhānaṃ": "sự ám ảnh của tham đắm hiện hữu",
    # 5-606 / 5-608 / 5-613 «khi tâm thiện hay không xác định về mặt đạo đức đang diễn ra, người phàm phu nên gọi là
    # “có khuynh hướng tiềm ẩn” … có gốc rễ nhờ gốc rễ ấy … vậy thì sự tham đắm không xác định về mặt đạo đức»
    "tena hi rāgo": "Vậy thì sự tham đắm",         # as T18 tena hi sīlaṃ
    "vattamāne": "đang diễn ra",                   # locative absolute: the frame «khi» dropped (as T18 niruddhe, nhāne)
    "citte vattamāne": "tâm" + GAP + "đang diễn ra",   # «tâm thiện hay không xác định … đang diễn ra»
    "hetunā": "gốc rễ",                            # tena hetunā «nhờ gốc rễ ấy» (instrumental frame «nhờ» dropped)
    # 5-609 … 5-612 «Thuộc về khối nào? Thuộc về khối tạo tác … khối tạo tác một phần gắn liền với tâm, một phần không
    # gắn liền với tâm»
    "kāmarāgānusayo cittavippayutto": _KT + " tham đắm dục lạc " + _KG,
    "avijjānusayo cittavippayutto": _KT + " vô minh " + _KG,
    "saṅkhārakkhandho cittavippayutto": "khối tạo tác " + _KG,
    "saññākkhandho cittavippayutto": "khối tri giác " + _KG,
    "ekadeso": "một phần",
    "saṅkhārakkhandho ekadeso": "khối tạo tác một phần",
    "cittasampayutto ekadeso": "gắn liền với tâm một phần",   # extraction artefact (…cittasampayutto ekadeso
                                                              # cittavippayutto): the adjacent words, comma dropped (pi-3)
    "ekadeso cittavippayutto": "một phần " + _KG,
    # ---- 5-614 / 5-615 «khi sự không biết đã mất đi, khi tâm không gắn liền với hiểu biết đang diễn ra … khi sự tham
    # đắm / sự sân hận / sự si mê / phiền não đã mất đi … nhờ hiểu biết thuộc quá khứ, … đã chấm dứt, đã mất đi, đã an
    # tịnh»
    "aññāṇe": "sự không biết", "ñāṇe": "biết",     # ñāṇe: fragment of aññāṇe (positive part)
    "vigate": "đã mất đi",                         # frame «khi» dropped (locative absolute)
    "rāge": "sự tham đắm", "dose": "sự sân hận", "mohe": "sự si mê",
    "ñāṇavippayutte vattamāne": "không gắn liền với hiểu biết đang diễn ra",
    "atītena ñāṇena": "hiểu biết thuộc quá khứ", "niruddhena": "đã chấm dứt", "paṭipassaddhena": "đã an tịnh",
    # ---- 5-617 «bậc A-la-hán có được thức qua mắt nên gọi là “người có trí tuệ” không [có vẻ là câu hỏi của người
    # theo học thuyết của chúng ta]»
    "paññavā": "người có trí tuệ",
    "viya": "có vẻ là", "dissati": NDE,            # viya dissati «có vẻ là»: one Vietnamese phrase (Russian: viya «похоже
                                                   # на», dissati no direct equivalent)
    # ---- 5-618 … 5-620 «khi nói lời “đây là khổ đau”, hiểu biết “đây là khổ đau” khởi lên … “vật chất là vô thường”
    # … cả về “i”, cả về “dam”, cả về “du”, cả về “kham”»
    "pavattati": "khởi lên",                       # (T15 «chảy xuôi» is another text)
    "bhāsato": "khi nói", "vācaṃ bhāsato": "khi nói lời",   # participle keeps «khi» (first rendering; «nói lời … mà»
    "vācaṃ": "lời",                                         # in the rebuttal lines; CROSSCHECK)
    "viññāṇaṃ aniccaṃ": "thức là vô thường", "rūpaṃ aniccaṃ": "vật chất là vô thường",   # inner «là» kept
    "kha": "kham",                                 # the syllable «“kham”»
    # ---- 5-621 … 5-624 «người được trang bị sức mạnh thần thông có thể tồn tại suốt một kiếp … sự có được sự tồn tại
    # cá nhân … khi còn sự sống, còn phần còn lại của sự sống … có thể dùng thần thông mà giữ cho sự tiếp xúc đã sinh
    # khởi đừng chấm dứt … các chúng sinh có bản chất phải sinh đừng sinh ra»
    "attabhāvappaṭilābho": "sự có được sự tồn tại cá nhân", "bhāva": "sự tồn tại",   # attabhāva (T-tables)
    "tiṭṭheyya": "tồn tại",                        # optative: the bare verb, «có thể» is frame (coordinator rule)
    "iddhibalena tiṭṭheyya": _SM + GAP + "tồn tại",   # «sức mạnh thần thông có thể tồn tại» (extraction artefact)
    "avasese": "phần còn lại", "avasesaṃ": "phần còn lại",   # kappāvasesaṃ «phần còn lại của kiếp»
    "jīvitāvasese": "phần còn lại của sự sống",    # head noun first
    "mā": "đừng",
    "nirujjhi": "chấm dứt", "jāyiṃsu": "sinh ra", "jīriṃsu": "lão hóa", "byādhiyiṃsu": "bệnh", "mīyiṃsu": "chết",
    "jīrī": "lão hóa", "byādhiyī": "bệnh", "mīyī": "chết",
    "byādhi": "bệnh",                              # byādhidhamma «có bản chất phải bệnh» (member)
    "iddhiyā paggahetuṃ": "thần thông mà giữ cho",   # «dùng thần thông mà giữ cho» (instrumental frame «dùng» dropped;
                                                     # inner «mà» kept, as T18 ārabbha uppajjati)
    # 5-623 «Bất cứ ai, này A-nan, có bốn nền tảng thần thông được tu tập, được làm đi làm lại, được biến thành cỗ xe,
    # được biến thành nền tảng, được thiết lập vững chắc, được làm cho quen thuộc, được khởi sự đúng đắn, thì người ấy,
    # nếu muốn, có thể tồn tại suốt một kiếp hoặc phần còn lại của kiếp»
    "yassa kassaci": "bất cứ ai",
    "bhāvitā": "được tu tập", "bahulīkatā": "được làm đi làm lại",
    "bhāvitā bahulīkatā": "được tu tập được làm đi làm lại",   # comma dropped (pi-1)
    "yānīkatā": "được biến thành cỗ xe", "anuṭṭhitā": "được thiết lập vững chắc",
    "paricitā": "được làm cho quen thuộc", "samāraddhā": "được khởi sự", "su": "đúng đắn",   # susamāraddhā
    "ākaṅkhamāno": "nếu muốn",                     # the participle with the text's «nếu» (as «khi»)
    # 5-624 AN 4.182 «không có người bảo đảm nào, dù là sa-môn hoặc bà-la-môn hoặc vị trời hoặc Ma vương hoặc Phạm
    # thiên hoặc bất cứ ai trong thế gian … những nghiệp xấu ác đã làm trước đây, là đối tượng của phiền não, đưa đến sự
    # hiện hữu mới, đầy lo âu, có quả trổ khó chịu, dẫn đến sự sinh, sự lão hóa và sự chết trong tương lai»
    "pāṭibhogo": "người bảo đảm", "māro vā brahmā": "Ma vương hoặc Phạm thiên",
    "katāni": "đã làm", "saṃkilesikāni": "đối tượng của phiền não",   # predicate «là» dropped (pi-1 saṃkilesikā)
    "ponobbhavikāni": "đưa đến sự hiện hữu mới", "bhavikāni": "đưa đến sự hiện hữu",
    "sadarāni": "đầy lo âu", "darāni": "lo âu",
    "jarāmaraṇiyāni": "sự lão hóa và sự chết",     # member of jātijarāmaraṇiyāni «dẫn đến sự sinh, sự lão hóa và sự chết»
    "dukkhavipākāni jātijarāmaraṇiyāni": "có quả trổ khó chịu dẫn đến sự sinh sự lão hóa và sự chết",   # commas dropped
    # ---- 5-625 / 5-626 «sự liên tục của tâm là sự định tâm … sự định tâm kéo dài trong khoảnh khắc của một tâm …
    # người có được thức qua mắt là người đang nhập thành tựu thiền … Ta, này các hiền giả Ni-kiền-tử, có thể không lay
    # động thân, không nói ra lời, suốt bảy ngày đêm sống cảm nhận hạnh phúc thuần nhất»
    "cittasantati": _LT, "cittasantati samādhi": _LT + " là sự định tâm",   # inner «là» kept
    "khaṇiko": "kéo dài trong khoảnh khắc",
    "cittakkhaṇiko": "kéo dài trong khoảnh khắc của" + GAP + "tâm",
    "ekacittakkhaṇiko": "kéo dài trong khoảnh khắc của một tâm",
    "samāpanno": "người đang nhập thành tựu thiền",   # the text's predicate noun (pi-1 samāpannassa «người đã chứng
                                                       # nhập» is another text)
    "rāgasahagatacittasamaṅgī": "người có được tâm có sự tham đắm đi kèm",
    "pahomi": "có thể", "iñjamāno": "lay động",    # of aniñjamāno «không lay động» (positive part)
    "bhāsamāno": "nói ra",                         # of abhāsamāno «không nói ra» (positive part, no «khi» in the text)
    "rattindivāni": "ngày đêm", "ekanta": "thuần nhất", "viharituṃ": "sống",
    "paṭisaṃvedī": "cảm nhận",                     # «sống cảm nhận hạnh phúc»: no head noun in the text (pi-2 / pi-4)
    # ---- 5-627 / 5-628 «sự ổn định của các hiện tượng được hình thành trọn vẹn … sự ổn định của sự ổn định ấy …
    # đối với từng cái như vậy, không có sự đi đến tận cùng của khổ đau, không có sự cắt đứt vòng luân chuyển, không có
    # sự nhập Niết-bàn trọn vẹn không còn bám víu»
    "parinipphannā": _HT, "parinipphannaṃ": _HT, "nipphannā": "được hình thành", "nipphannaṃ": "được hình thành",
    "ṭhitatā parinipphannā": "sự ổn định" + GAP + _HT,   # «sự ổn định (của sự ổn định ấy) được hình thành trọn vẹn»
    "dhammaṭṭhitatā parinipphannā": "sự ổn định của các hiện tượng " + _HT,
    "rūpassa parinipphannā": "vật chất " + _HT,    # extraction artefacts of Rūpassa / viññāṇassa ṭhitatā
    "viññāṇassa parinipphannā": "thức " + _HT,     # parinipphannā «sự ổn định của vật chất / thức được hình thành …»
    "jarā parinipphannā": "sự lão hóa " + _HT, "maraṇaṃ parinipphannaṃ": "sự chết " + _HT,
    "aniccatā parinipphannā": "tính vô thường " + _HT,
    "viññāṇaṃ parinipphannaṃ": "thức " + _HT,
    "tāya tāyeva": "từng cái như vậy",             # (sample tassa tasseva «từng người như vậy»; frame «đối với» dropped)
    "dukkhassantakiriyā": "sự đi đến tận cùng của khổ đau",   # KV dukkhassa antakiriyā
    "vaṭṭa": "vòng luân chuyển",                   # vaṭṭupacchedo (KV; T15 «vòng xoay» is another text)
    "saṅkhārānaṃ": "tạo tác",                      # «các tạo tác» («các» dropped)
    # ---- 5-629 «… có sự tan rã của vật chất, có sự biến mất» and the uddāna «… hiểu biết khởi lên nơi âm thanh
    # [dị bản (Sī.): yattha saddo; (?): yathāsaddaṃ] …»
    "bhedo": "sự tan rã",                          # (T10 «sự phát ra» is another text)
    "yattha": "nơi", "sadde": "âm thanh",
    "saddo": NDE,                                  # only in the variant bracket [dị bản (Sī.): yattha saddo]
}

PRIOR = {**map_18_vi.PRIOR, **T19}


def context19(kw, k, kws, text):
    """Segment rules of this chapter (k: lower-cased keyword). None = no rule."""
    if k == "rūpaṃ":               # the aggregate «vật chất» (T14 «hình sắc» is the visible object)
        return pick(text, "vật chất", "hình sắc")
    if k == "dhamma":              # dhammaṭṭhitatā «sự ổn định của các hiện tượng» (T18 «Giáo Pháp» is another text)
        return pick(text, "hiện tượng", "Giáo Pháp")
    if k in ("samaṅgī", "cakkhuviññāṇasamaṅgī"):   # «người có được thức qua mắt» (5-626, T18) / «bậc A-la-hán có được
        tail = "" if k == "samaṅgī" else " thức qua mắt"   # thức qua mắt» (5-617: no «người»)
        return pick(text, "người có được" + tail, "có được" + tail)
    return None


OVERRIDES = {
    "5-622": {"jarā": "lão hóa", "jāti": "sinh", "maraṇa": "chết"},   # X-dhammā sattā «chúng sinh có bản chất phải
                                                                     # lão hóa / sinh / chết» (members, no «sự»)
    "5-624": {"jarā": "lão hóa",                   # first jarādhammo «điều có bản chất phải lão hóa»; CROSSCHECK «sự lão
                                                   # hóa» (jātijarāmaraṇiyāni)
              "maraṇa": "chết",                    # first maraṇadhammo «… phải chết»; CROSSCHECK «sự chết»
              "koci": "nào",                       # first natthi koci pāṭibhogo «không có người bảo đảm nào»; CROSSCHECK
                                                   # koci vā lokasmiṃ «bất cứ ai trong thế gian»
              "dukkha": "khó chịu"},               # dukkhavipākāni «có quả trổ khó chịu»
    "5-626": {"rāga": "sự tham đắm"},              # rāgasahagata «có sự tham đắm đi kèm» (the only rāga here)
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
        v = context19(kw, k, kws, text)
        if v is not None:
            return v
        if k in T19:
            return T19[k]
        if k not in PRIOR:
            v = map_5_vi.subject_predicate(kw, kws, text)
            if v:
                return v
        return value5(kw, kws, PRIOR, text)
    return resolve


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
                print(f"   {kw}={v}  [ru:{e[1]}]{flag}")


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
             "14-chatthavaggo", "15-sattamavaggo", "18-dasamavaggo"]


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
