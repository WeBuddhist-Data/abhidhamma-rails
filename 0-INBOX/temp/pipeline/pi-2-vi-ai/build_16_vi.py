# -*- coding: utf-8 -*-
"""pi-2 Vibhaṅga, Vietnamese plain zero-shot: chapter 16 (Ñāṇavibhaṅga).

usage: python -I -X utf8 build_16_vi.py [--dry]
Writes AI_translation\\vietnamese\\pi-2-vietnamese-plain-zeroshot_split_chapters\\16-nanavibhango.md (only when run
as a script without --dry; importing writes nothing).

Imports build_13-15_vi (Y) and through it X, S, B, T, F, G, H; B's item tables get a few feminine surfaces and new
items in memory only, nothing of theirs is rewritten. pi-1 strings (the rūpa one-fold list and its "-meva" list,
^1-1373 knowledge names, ^1-1371 "atthi dinnaṃ …", the diṭṭhāsava view list, ^1-1344 / ^1-1371 / ^1-1326 frames,
the ten kilesavatthu, ^1-1380, ^1-248 / ^1-204, ^1-181 …, ^1-1386 bhūmi words) are copied from the pi-1 Vietnamese
rails and asserted; ch4 / ch6 / ch7 / ch12 / ch15 strings are imported or asserted in their outputs. Lists and the
duka / tika expositions are parsed; the remaining lines are hand lines checked by their Pāli start and end.
"""
import importlib
import os
import re
import sys

HERE = r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-vi-ai"
sys.path.insert(0, HERE)
Y = importlib.import_module("build_13-15_vi")
X = Y.X
S, B, T, F, G, H = Y.S, Y.B, Y.T, Y.F, Y.G, Y.H

DASH = S.DASH
cap, low = S.cap, S.low
in_pi1, between = G.in_pi1, T.between
called, q, qq = T.called, X.q, X.qq
TATTHA, IDHA, BHIKKHU = X.TATTHA, X.IDHA, X.BHIKKHU
SLIPS = []
FN = "16-nanavibhango.md"
PI1_P = os.path.join(S.ROOT, r"AI_translation\pali\pi-1_split_chapters")
PI1_V = os.path.join(S.ROOT, r"AI_translation\vietnamese\pi-1-vietnamese-plain-rails_split_chapters")


def nonempty(path):
    return [x for x in open(path, encoding="utf-8").read().split("\n") if x.strip()]


def pi1_pair(fn, pali_start):
    """pi-1 (Pāli, Vietnamese) non-empty line whose Pāli starts with pali_start (block ID removed)."""
    pl, vl = nonempty(os.path.join(PI1_P, fn)), nonempty(os.path.join(PI1_V, fn))
    assert len(pl) == len(vl), fn
    hits = [(S.ID.sub("", p).rstrip(), S.ID.sub("", v).rstrip()) for p, v in zip(pl, vl) if p.startswith(pali_start)]
    assert hits, pali_start
    return hits[0]


def vi_out(fn):
    return open(os.path.join(S.VI_DIR, fn), encoding="utf-8").read()


def in_out(fn, *parts):
    txt = vi_out(fn)
    for p in parts:
        assert p in txt, (fn, p[:80])


def pali_out(fn):
    return [S.ID.sub("", x).rstrip() for x in nonempty(os.path.join(S.PALI_DIR, fn))]


# ================================================================ 1. core words
PANNA = F.PANNA                                     # paññā pajānanā…pe… amoho dhammavicayo sammādiṭṭhi [pi-1 ^1-16 cut]
TP = "điều mà, ở đây, là " + PANNA                  # yā tattha paññā … [pi-1 ^1-1344]
EP = "điều mà thuộc loại như vậy là " + PANNA       # yā evarūpā paññā … [pi-1 ^1-1371]
in_pi1(TP, EP, "Điều mà sinh khởi liên quan đến quá khứ là quan điểm")   # [pi-1 ^1-1326 frame]


def ar(x):
    """X ārabbha yā uppajjati paññā pajānanā…pe… [pi-1 ^1-1326 frame]"""
    return f"Điều mà sinh khởi liên quan đến {x} là {PANNA}"


def gen(x):
    """<participle>-assa yā uppajjati paññā …"""
    return f"Điều mà sinh khởi ở {x} là {PANNA}"


TRI = "trí tuệ"                                     # paññā [pi-1 core]
KNOW = "sự hiểu biết"                               # ñāṇa [ch4 / ch15]
VAT = "chỗ dựa"                                     # vatthu [pi-1 ^1-? rūpa «chỗ dựa», kilesavatthu]
NV = "chỗ dựa của sự hiểu biết"                     # ñāṇavatthu [new]
FIVE = "năm loại thức"                              # pañca viññāṇā [pi-1 ^1-454 «Năm loại thức»]
in_pi1("Năm loại thức là quả của nghiệp thiện", "là chỗ dựa của sự tiếp xúc của mắt")
NUMV = {"eka": 1, "du": 2, "ti": 3, "catub": 4, "pañca": 5, "chab": 6, "satta": 7, "aṭṭha": 8, "nava": 9, "dasa": 10}


def frame_open(n):
    return f"Phân loại {NV} theo nhóm {S.NUM[n]}"   # [B.frame_open words; sample class_open]


def frame_close(n):
    return f"Như vậy là phân loại {NV} theo nhóm {S.NUM[n]}."


# loci: "trong …" [pi-1 ^1-1384 / ^1-1386 «Tâm thiện thuộc bốn cõi», «Quả của nghiệp thuộc bốn cõi», «tâm mang tính
# chức năng không xác định về mặt đạo đức thuộc ba cõi»]
_, _V1386 = pi1_pair("5-atthakathakandam.md", "Katame dhammā abyākatā? Catūsu bhūmīsu vipāko")
assert "Quả của nghiệp thuộc bốn cõi; tâm mang tính chức năng không xác định về mặt đạo đức thuộc ba cõi" in _V1386
in_pi1("Tâm thiện thuộc bốn cõi")
BH = {"tīsu": "thuộc ba cõi", "catūsu": "thuộc bốn cõi"}
LOCN = {"kusalābyākate": "tâm thiện và không xác định về mặt đạo đức", "kusale": "tâm thiện",
        "vipāke": "quả của nghiệp", "kiriyābyākate": "tâm mang tính chức năng không xác định về mặt đạo đức"}
AV = {"kāmāvacara": "thuộc cõi dục lạc", "rūpāvacara": "thuộc cõi hình sắc", "arūpāvacara": "thuộc cõi không hình sắc",
      "rūpāvacarārūpāvacara": "thuộc cõi hình sắc và cõi không hình sắc"}   # [pi-1]
MAGGA4, PHALA4 = "bốn con đường", "bốn thành quả"                         # [pi-1 magga / phala]
in_pi1("Bốn con đường")
LOC_RE = re.compile(r"(tīsu|catūsu) bhūmīsu (kusalābyākate|kusale|vipāke|kiriyābyākate)|catūsu maggesu|catūsu phalesu|"
                    r"tīsu phalesu|(kāmāvacara|rūpāvacarārūpāvacara|rūpāvacara|arūpāvacara)"
                    r"(kusalābyākate|kusale)|catūsu maggesu, catūsu phalesu|dvīsu jhānesu|tīsu jhānesu")


def loc1(m):
    t = m.group(0)
    if m.group(1):
        return f"trong {LOCN[m.group(2)]} {BH[m.group(1)]}"
    if m.group(3):
        return f"trong {LOCN[m.group(4)]} {AV[m.group(3)]}"
    return {"catūsu maggesu": f"trong {MAGGA4}", "catūsu phalesu": f"trong {PHALA4}",
            "tīsu phalesu": "trong ba thành quả", "dvīsu jhānesu": "trong hai tầng thiền",
            "tīsu jhānesu": "trong ba tầng thiền"}[t]


def loc(p):
    """sequence of locatives -> «trong …, trong …»"""
    p = p.replace("catūsu maggesu, catūsu phalesu", "catūsu maggesu catūsu phalesu")
    parts, pos = [], 0
    for m in LOC_RE.finditer(p):
        assert p[pos:m.start()].strip() == "", (p, pos)
        parts.append(loc1(m))
        pos = m.end()
    assert p[pos:].strip() == "", p
    return ", ".join(parts)


# ================================================================ 2. matrix items (B tables, extended in memory)
for _s, _k in (("ācayagāminī", "acaya"), ("apacayagāminī", "apacaya"),
               ("nevācayagāmināpacayagāminī", "nevacaya"), ("maggādhipatinī", "maggadhipati"),
               ("uppādinī", "uppadi")):
    B.SURF[_s] = _k                                  # feminine surfaces (paññā), same items
EXTRA = {   # new paññā / ñāṇa attributes [new unless marked]
    "atthajāpikā": "tạo ra lợi ích", "jāpitatthā": "có lợi ích đã được tạo ra",
    "cintāmayā": "được tạo nên từ sự suy tư", "sutamayā": "được tạo nên từ sự lắng nghe",
    "bhāvanāmayā": "được tạo nên từ sự tu tập", "dānamayā": "được tạo nên từ sự bố thí",
    "sīlamayā": "được tạo nên từ giới hạnh",                                 # [ch6 dānamayā … bhāvanāmayā]
    "adhisīle": "trong giới hạnh cao thượng", "adhicitte": "trong tâm cao thượng",
    "adhipaññāya": "trong trí tuệ cao thượng",
    "hānabhāginī": "thuộc về phía suy giảm", "ṭhitibhāginī": "thuộc về phía duy trì",
    "visesabhāginī": "thuộc về phía thăng tiến", "nibbedhabhāginī": "thuộc về phía xuyên thấu",
}
in_out("6-paticcasamuppadavibhango.md", "được tạo nên từ sự bố thí, được tạo nên từ giới hạnh, được tạo nên từ sự tu tập")
PATIPADA = {"dukkhapaṭipadā dandhābhiññā": "với cách thực hành khó khăn và sự hiểu biết trực tiếp chậm chạp",
            "dukkhapaṭipadā khippābhiññā": "với cách thực hành khó khăn và sự hiểu biết trực tiếp nhanh chóng",
            "sukhapaṭipadā dandhābhiññā": "với cách thực hành dễ dàng và sự hiểu biết trực tiếp chậm chạp",
            "sukhapaṭipadā khippābhiññā": "với cách thực hành dễ dàng và sự hiểu biết trực tiếp nhanh chóng"}   # [pi-1]
ARAM = {"parittā parittārammaṇā": "hạn hẹp và có đối tượng hạn hẹp",
        "parittā appamāṇārammaṇā": "hạn hẹp và có đối tượng không thể đo lường",
        "appamāṇā parittārammaṇā": "không thể đo lường và có đối tượng hạn hẹp",
        "appamāṇā appamāṇārammaṇā": "không thể đo lường và có đối tượng không thể đo lường"}   # [pi-1 ^1-181 …]
in_pi1(*PATIPADA.values(), *ARAM.values())
EXTRA.update(PATIPADA)
EXTRA.update(ARAM)
MA = ("là ", "không phải là ")


def attr(x):
    """Pāli attribute of paññā -> Vietnamese predicate (B item string, one per item)"""
    x = low(x)
    x2 = re.sub(r"^(\w+)vippayuttā (\w+)$", r"\1vippayutta\2", x)   # two words (all pi-2 ch16 clusters) = the compound
    if x2 in EXTRA:
        return EXTRA[x2]
    return B.P(B.SURF[x2])


def pn(x):
    """X paññā -> «trí tuệ (mà) X» («mà» before a «là …» item, ch4 restrictive attribute)"""
    p = attr(x)
    return f"{TRI} {'mà ' if p.startswith(MA) else ''}{p}"


def atthi(x):
    return f"có loại {attr(x)}"                     # atthi X [ch1 «có loại»]


SAMP = {"vitakka": "sự hướng tâm", "vicāra": "sự duy trì tâm", "pīti": "sự hân hoan", "sukha": "hạnh phúc",
        "upekkhā": "sự bình thản", "vitakkavicāra": "sự hướng tâm và sự duy trì tâm"}   # [pi-1]


def subj(s):
    """subject of a duka / tika exposition clause (without "paññā") -> «trí tuệ …»"""
    s0 = low(s)
    m = re.match(r"^(\w+?)(sampayuttā|vippayuttā)$", s0)
    if m:
        return f"{TRI} {'gắn liền với' if m.group(2) == 'sampayuttā' else 'không gắn liền với'} {SAMP[m.group(1)]}"
    if s0 == "vitakkavippayuttā vicārasampayuttā":
        return f"{TRI} không gắn liền với {SAMP['vitakka']}, gắn liền với {SAMP['vicāra']}"
    if s0 == "sabbāpi tatrupāyā":
        return "mọi trí tuệ về phương cách cho việc ấy"
    if s0.startswith("upariṭṭhimā"):
        return f"{TRI} trong thành quả A-la-hán cao nhất{VAR_UPARI}"
    return f"{TRI} {loc(s0)}"


VAR_UPARI = " [khác chính tả (Syā.): upariṭṭhime; (Ka.): upariṭṭhimaṃ]"
in_pi1("Thành quả A-la-hán cao nhất", "con đường A-la-hán cao nhất")


def clause(c):
    """'<subject> paññā <attr> paññā' -> «trí tuệ … là trí tuệ …»"""
    m = re.match(r"^(.+?) paññā (.+?) paññā$", c)
    assert m, c
    return f"{subj(m.group(1))} là {pn(m.group(2))}"


def lab(t):
    """(1. Ka) / (Kha) / (Ga) / (Gha) / (Kha-gha) -> (1. a) / (b) / (c) / (d) / (b-d); rest of the line"""
    m = re.match(r"^\((\d+(?:-\d+)?)?(?:\. )?(Ka|Kha|Ga|Gha|Kha-gha)?\) (.*)$", t)
    if not m:
        return "", t
    num, ka, rest = m.groups()
    kv = {"Ka": "a", "Kha": "b", "Ga": "c", "Gha": "d", "Kha-gha": "b-d"}.get(ka)
    inner = ". ".join(x for x in (num, kv) if x)
    return f"({inner}) ", rest


def case(vi, pali_rest):
    return cap(vi) if pali_rest[:1].isupper() else low(vi)


# ================================================================ 3. pi-1 one-fold lists (rūpa ^1-584 and its "-meva" list)
_P1 = [x for x in pali_out("1-khandhavibhango.md") if "Ekavidhena rūpakkhandho – sabbaṃ rūpaṃ na hetu" in x][0]
_P1 = between(_P1, "sabbaṃ rūpaṃ ", ". Evaṃ ekavidhena").replace("uppannaṃ, chahi", "uppannaṃ chahi").split(", ")
_V1 = S.RUPA_EKAVIDHA[len("Toàn bộ vật chất "):].split("; ")
assert len(_P1) == len(_V1), (len(_P1), len(_V1))
RUPA1 = dict(zip(_P1, _V1))
_PM, _VM = pi1_pair("3-01-rupakandam.md", "Sabbaṃ rūpaṃ na hetumeva")
_PM = _PM[len("Sabbaṃ rūpaṃ "):-1].split(", ")
_VM = _VM[len("Toàn bộ vật chất "):-1].split("; ")
assert len(_PM) == len(_VM), (len(_PM), len(_VM))
MEVA = dict(zip(_PM, _VM))
MEVA["nevācayagāmināpacayagāmimeva"] = MEVA["neva ācayagāmi na apacayagāmimeva"]
CHAC = "chắc chắn "


def ekaka_item(x):
    """masc. pl. item of the ñāṇa one-fold matrix -> the rūpa-list string (pi-1) or the B item"""
    n = {"na hetū": "na hetu", "nevācayagāmināpacayagāmino": "nevācayagāmināpacayagāmī"}.get(x, re.sub(r"ā$", "aṃ", x))
    if n in RUPA1:
        return RUPA1[n]
    return B.P(B.SURF[x])


def meva_item(x):
    if x in MEVA:
        return MEVA[x]
    if x == "uppannaṃ manoviññāṇaviññeyyameva":
        v = MEVA["uppannaṃ chahi viññāṇehi viññeyyameva"]
        assert "sáu loại thức" in v
        return v.replace("sáu loại thức", "ý thức")
    base = x[:-len("meva")]
    surf = {"arūpa": "arūpā", "sārammaṇa": "sārammaṇā", "vipāka": "vipāko",
            "upādinnupādāniya": "upādinnupādāniyo"}[base]
    return CHAC + B.P(B.SURF[surf])


# ================================================================ 4. reused strings from pi-1 / earlier chapters
_, _V1373 = pi1_pair("4-03-nikkhepakandam.md", "Tattha katamā diṭṭhivisuddhi?")
KN4 = between(_V1373, "là gì? ", ".").split(", ")                          # [pi-1 ^1-1373]
KAMMASSAKA, SACCANU, MAGGASAM, PHALASAM = KN4
assert KAMMASSAKA == "Hiểu biết rằng nghiệp là tài sản của chính mình", KN4
KAMMASSAKA = low(KAMMASSAKA)
DHAMMASAM = MAGGASAM.replace("con đường", "Giáo Pháp")                     # Dhammasamaṅgissa (as written) [new]
_, _V1371 = pi1_pair("4-03-nikkhepakandam.md", "Tattha katamā diṭṭhisampadā?")
ATTHI_DINNA = between(_V1371, "là gì? ", "; điều mà thuộc loại")           # “Có sự bố thí, … rồi tuyên bố” [pi-1 ^1-1371]
assert ATTHI_DINNA.startswith("“Có sự bố thí") and ATTHI_DINNA.endswith("tuyên bố”"), ATTHI_DINNA
_, _VDA = pi1_pair("4-01-nikkhepakandam.md", "Tattha katamo diṭṭhāsavo?")
VIEWS10 = between(_VDA, "là gì? ", "; điều mà")                            # “Thế gian là trường tồn”, hoặc … [pi-1]
assert VIEWS10.startswith("“Thế gian là trường tồn”") and VIEWS10.endswith("sau khi chết”"), VIEWS10
_, _VKV = pi1_pair("5-atthakathakandam.md", "Katame dhammā kilesā? Dasa kilesavatthūni")
KILESA10 = between(_VKV, "là phiền não? ", ". Sự tham lam sinh khởi")      # Mười chỗ dựa của phiền não – … [pi-1]
assert KILESA10.startswith("Mười chỗ dựa của phiền não " + DASH), KILESA10
_, _V1380 = pi1_pair("4-03-nikkhepakandam.md", "Vijjāti")
for _w in ("sự nhớ lại các đời sống trước", "sự chết và sự tái sinh của chúng sinh", "sự diệt tận các ô nhiễm"):
    assert "hiểu biết về " + _w in _V1380, _w                              # [pi-1 ^1-1380]
PUBBE, CUTU, KHAYA = "sự nhớ lại các đời sống trước", "sự chết và sự tái sinh của chúng sinh", "sự diệt tận các ô nhiễm"
_, _V1344 = pi1_pair("4-03-nikkhepakandam.md", "Tattha katamā ṭhānakusalatā?")
assert "là điều kiện cho sự sinh khởi" in _V1344 and "thì đó là điều có thể xảy ra" in _V1344   # [pi-1 ^1-1344]
TH, ATH = "điều có thể xảy ra", "điều không thể xảy ra"                  # ṭhāna / aṭṭhāna [pi-1 ^1-1344 / ^1-1345]
in_pi1(ATH)
in_pi1("có hình sắc, thấy những hình sắc", "không có tri giác về hình sắc ở nơi bản thân, thấy ở bên ngoài bản thân "
       "những hình sắc")                                                    # [pi-1 ^1-248 / ^1-204]
in_pi1("khuynh hướng tiềm ẩn vô minh", "xiềng xích tham đắm dục lạc", "xiềng xích tham đắm hiện hữu",
       "đã tự mình hiểu biết trực tiếp, chứng nghiệm", "bậc Tự Giác Ngộ Hoàn Toàn", "Như Lai", "Tăng đoàn",
       "sự không xem xét lại", "sự hợp nhất của tâm", "sự không thấu triệt",
       "quy luật tùy thuộc vào điều kiện và các hiện tượng sinh khởi tùy thuộc vào điều kiện")
DUKKHA4 = ("sự hiểu biết về khổ đau, sự hiểu biết về sự phát sinh của khổ đau, sự hiểu biết về sự chấm dứt khổ đau, "
           "sự hiểu biết về cách thực hành dẫn đến sự chấm dứt khổ đau")   # [ch4]
in_out("4-saccavibhango.md", cap(DUKKHA4), "Điều gì trong thế gian là điều đáng yêu, là điều khoan khoái, thì ở đó,")
TRUTH = {"dukkha": "khổ đau", "dukkhasamudaya": "sự phát sinh của khổ đau", "dukkhanirodha": "sự chấm dứt khổ đau",
         "dukkhanirodhagāminī": "cách thực hành dẫn đến sự chấm dứt khổ đau"}   # [ch4]
_CH7 = vi_out("7-satipatthanavibhango.md")
CITTA16 = ("hoặc hiểu rõ tâm có tham đắm là “tâm có tham đắm”" +
           between(_CH7, "hoặc hiểu rõ tâm có tham đắm là “tâm có tham đắm”", "“tâm không được giải thoát”")
           + "“tâm không được giải thoát”")                                 # [ch7 ^2-365]
_P7 = [x for x in pali_out("7-satipatthanavibhango.md") if "ajjhattabahiddhā citte cittānupassī viharati? Idha" in x][0]
CITTA16_P = between(_P7, "Idha bhikkhu ", ". Evaṃ bhikkhu")                # same Pāli asserted below
JHANA4 = "Bốn tầng thiền " + DASH + " tầng thiền thứ nhất, tầng thiền thứ hai, tầng thiền thứ ba và tầng thiền thứ tư"
in_out("12-jhanavibhango.md", JHANA4 + ".", "gần gũi, lui tới, thường xuyên lui tới hầu cận")   # [ch12]
in_out("9-iddhipadavibhango.md", "tu tập, làm đi làm lại")
ABHISANKH = ("sự tạo tác thuộc về phước", "sự tạo tác không thuộc về phước", "sự tạo tác dẫn đến trạng thái bất động")
in_out("6-paticcasamuppadavibhango.md", *ABHISANKH)                         # [ch6]
LINK = G.N                                                                  # dependent-origination names [pi-1 / ch6]
in_pi1("sự sinh làm điều kiện cho sự lão hóa và sự chết", "Vô minh làm điều kiện cho các sự tạo tác")
in_pi1("thấy những hình sắc")
RUPA3 = X.RUPA3                                                             # sabbaso rūpasaññānaṃ … amanasikārā [ch12]
THOUGHT, AYAT = X.THOUGHT, X.NAMES_AYAT
PS, NIR, PAT, KN = Y.PS, Y.NIR, Y.PAT, Y.KN                                 # [ch15]


def kn(x):
    return f"{KN} {x}"


# ================================================================ 5. ñāṇa names and other new strings
NAMES = {   # X ñāṇaṃ -> «sự hiểu biết …» [new; «sự hiểu biết về X» = ch4 / ch15]
    "dhamme": kn("Giáo Pháp"), "anvaye": "sự hiểu biết bằng suy diễn", "pariye": "sự hiểu biết bao quát tâm",
    "sammuti": "sự hiểu biết theo quy ước", "paracitte": kn("tâm người khác"),
    "iddhividhe": kn("các loại thần thông"), "sotadhātuvisuddhiyā": kn("sự trong sạch của yếu tố tai"),
    "pubbenivāsānussatiyā": kn(PUBBE), "sattānaṃ cutūpapāte": kn(CUTU), "āsavānaṃ khaye": kn(KHAYA),
    "paccavekkhaṇā": "sự hiểu biết xem xét lại",
}
VAR_PARIYE = " [dị bản (tất cả các ấn bản): paricce; xem “Trường Bộ Kinh”]"
VAR_SAMMUTI = " [khác chính tả (Syā.): sammatiñāṇaṃ; xem “Trường Bộ Kinh”]"
DA = {"jāti": "sự sinh", "bhava": "sự hiện hữu", "upādāna": "sự bám víu", "taṇhā": "khao khát", "vedanā": "cảm giác",
      "phassa": "sự tiếp xúc", "saḷāyatana": "sáu lĩnh vực nhận biết", "nāmarūpa": "phần tinh thần và vật chất",
      "viññāṇa": "thức", "saṅkhāra": "các sự tạo tác", "jarāmaraṇa": "sự lão hóa và sự chết", "avijjā": "vô minh"}
for _k, _p in (("jāti", "jāti"), ("bhava", "bhavo"), ("upādāna", "upādānaṃ"), ("taṇhā", "taṇhā"), ("vedanā", "vedanā"),
               ("phassa", "phasso"), ("saḷāyatana", "saḷāyatanaṃ"), ("nāmarūpa", "nāmarūpaṃ"), ("viññāṇa", "viññāṇaṃ"),
               ("saṅkhāra", "saṅkhārā"), ("jarāmaraṇa", "jarāmaraṇaṃ"), ("avijjā", "avijjā")):
    assert LINK[_p] == DA[_k], _k
DA_ORDER = ["jāti", "bhava", "upādāna", "taṇhā", "vedanā", "phassa", "saḷāyatana", "nāmarūpa", "viññāṇa"]


def four(n):
    """X-e, X-samudaye, X-nirodhe, X-nirodhagāminiyā paṭipadāya ñāṇaṃ [ch15 four_truths without paṭisambhidā]"""
    return [kn(n), kn("sự phát sinh của " + n), kn("sự chấm dứt " + n), kn("cách thực hành dẫn đến sự chấm dứt " + n)]


assert ", ".join(four("khổ đau")) == DUKKHA4

ACAYA = {"ācayāya no apacayāya": "dẫn đến sự tích lũy chứ không dẫn đến sự giảm trừ",
         "apacayāya no ācayāya": "dẫn đến sự giảm trừ chứ không dẫn đến sự tích lũy",
         "ācayāya ceva apacayāya ca": "vừa dẫn đến sự tích lũy vừa dẫn đến sự giảm trừ",
         "nevācayāya no apacayāya": "không dẫn đến sự tích lũy cũng không dẫn đến sự giảm trừ",
         "neva ācayāya no apacayāya": "không dẫn đến sự tích lũy cũng không dẫn đến sự giảm trừ",
         "nibbidāya no paṭivedhāya": "dẫn đến sự nhàm chán chứ không dẫn đến sự thấu triệt",
         "paṭivedhāya no nibbidāya": "dẫn đến sự thấu triệt chứ không dẫn đến sự nhàm chán",
         "nibbidāya ceva paṭivedhāya ca": "vừa dẫn đến sự nhàm chán vừa dẫn đến sự thấu triệt",
         "neva nibbidāya no paṭivedhāya": "không dẫn đến sự nhàm chán cũng không dẫn đến sự thấu triệt"}   # [new]
in_pi1("dẫn đến sự tích lũy", "không dẫn đến sự tích lũy cũng không dẫn đến sự giảm trừ")
KOSALLA = {"āya": "sự khéo léo về sự tăng tiến", "apāya": "sự khéo léo về sự suy thoái",
           "upāya": "sự khéo léo về phương cách"}                          # [new; kosalla pi-1 «sự khéo léo»]
SAMADHI5 = "định tâm đúng đắn gồm năm chi phần"
SAMADHI5N = "định tâm đúng đắn gồm năm sự hiểu biết"
ABHINNA6 = "sáu loại hiểu biết trực tiếp"                                  # chasu abhiññāsu [pi-1 abhiññā]
NV77 = "bảy mươi bảy " + NV
SAMAP9 = "chín sự chứng đạt an trú tuần tự"                                # anupubbavihārasamāpatti [ch12 samāpatti]
NIRODHA_SAMAP = "sự chứng đạt chấm dứt tri giác và cảm giác"
MP = f"trong {MAGGA4}, trong {PHALA4}"
JH_SAMAP = ["sự chứng đạt tầng thiền thứ nhất", "sự chứng đạt tầng thiền thứ hai", "sự chứng đạt tầng thiền thứ ba",
            "sự chứng đạt tầng thiền thứ tư"] + [f"sự chứng đạt {AYAT[k]}" for k in
                                               ("ākāsānañcāyatana", "viññāṇañcāyatana", "ākiñcaññāyatana",
                                                "nevasaññānāsaññāyatana")]

# ten powers
TB = "sức mạnh Như Lai"
NL = "Như Lai"
BALA_ACTS = ("tuyên bố vị trí của bậc dẫn đầu, rống tiếng rống sư tử giữa các hội chúng, chuyển bánh xe cao thượng")
EQUIP = f"mà khi được trang bị những sức mạnh ấy, {NL} {BALA_ACTS}"
BALA = [
    f"{TH} là {TH} và {ATH} là {ATH}",
    "quả của các nghiệp đã thực hiện thuộc quá khứ, tương lai và hiện tại, theo hoàn cảnh, theo nguyên nhân",
    "cách thực hành dẫn đến mọi nơi",
    "thế gian có nhiều yếu tố, có các yếu tố khác nhau",
    "sự khác nhau về chí hướng của chúng sinh",
    "mức độ cao thấp của các năng lực nơi những chúng sinh khác, những người khác",
    "sự vẩn đục, sự trong sạch và sự xuất khỏi của các tầng thiền, các sự giải thoát, các định tâm và các sự chứng đạt",
    PUBBE, CUTU, KHAYA,
]
BALA7Q = "sự vẩn đục và sự trong sạch của các tầng thiền, các sự giải thoát, các định tâm và các sự chứng đạt"
VAR_LOKA = " [khác chính tả (Syā.): anekadhātuṃ nānādhātuṃ lokaṃ; ma. ni. 1.148]"


def bala_name(b):
    return f"sự hiểu biết đúng như thật của {NL} về {b}"


def bala_q(b):
    n = bala_name(b)
    return qq(n) if " là " in n else q(n)


def bala_line(i):
    """(i) Idha / Puna caparaṃ tathāgato X yathābhūtaṃ pajānāti. Yampi … brahmacakkaṃ pavatteti."""
    b = BALA[i]
    b1 = b + VAR_LOKA if i == 3 else b
    head = f"{IDHA}, {NL}" if i == 0 else f"Lại nữa, {NL}"
    return (f"({i + 1}) {head} hiểu rõ đúng như thật {b1}. Việc {NL} hiểu rõ đúng như thật {b}, điều này cũng là một "
            f"{TB} của {NL}, nhờ dựa vào sức mạnh ấy mà {NL} {BALA_ACTS}.")


def neg(x):
    return f"Việc {x} là {ATH}, không có cơ hội; điều đó không thể xảy ra"


def pos(x):
    return f"Nhưng việc {x} là {TH}; điều đó có thể xảy ra"


def knows(x, first=False):
    return f"{IDHA}, {NL} hiểu rõ rằng “{x}”." if first else f"Ngài hiểu rõ rằng “{x}”."


SAMPANNA, PUTHU = "một người thành tựu về quan điểm", "một người phàm"   # diṭṭhisampanno puggalo / puthujjano [new]
in_pi1("sự thành tựu về quan điểm")
GOOD = "cõi tốt lành, thế giới cõi trời"                                  # sugatiṃ saggaṃ lokaṃ [new]
BAD3 = "cõi khổ, cõi xấu, nơi đọa lạc, địa ngục"                         # apāyaṃ duggatiṃ vinipātaṃ nirayaṃ [new]
DEATH = "sau khi thân tan rã, sau khi chết"                               # kāyassa bhedā paraṃ maraṇā [new]
DES = "đáng mong muốn, đáng yêu mến, đáng ưa thích"                       # iṭṭha kanta manāpa [sample]
UNDES = "không đáng mong muốn, không đáng yêu mến, không đáng ưa thích"
assert DES in open(os.path.join(HERE, "ch1-sample.md"), encoding="utf-8").read()
CON = {"kāya": "bằng thân", "vacī": "bằng lời nói", "mano": "bằng ý"}
DUC = {k: f"hành vi xấu {v}" for k, v in CON.items()}                     # X-duccarita [pi-1 ^1-300 words]
SUC = {k: f"hành vi tốt {v}" for k, v in CON.items()}
in_pi1("hành vi xấu bằng thân")


def ripen(src, good):
    return f"{src} sinh ra quả {DES if good else UNDES}"


def rebirth(who, good):
    return f"người có {who}, do nguyên nhân ấy, do điều kiện ấy, {DEATH}, tái sinh vào {GOOD if good else BAD3}"


P809 = " ".join([
    knows(neg(f"{SAMPANNA} xem bất cứ sự tạo tác nào là thường hằng"), True),
    knows(pos(f"{PUTHU} xem bất cứ sự tạo tác nào là thường hằng")),
    knows(neg(f"{SAMPANNA} xem bất cứ sự tạo tác nào là hạnh phúc")),
    knows(pos(f"{PUTHU} xem bất cứ sự tạo tác nào là hạnh phúc")),
    knows(neg(f"{SAMPANNA} xem bất cứ hiện tượng nào là tự ngã")),      # atthato as meant (attato), reported
    knows(pos(f"{PUTHU} xem bất cứ hiện tượng nào là tự ngã")),
    knows(neg(f"{SAMPANNA} tước đoạt mạng sống của mẹ")),
    knows(pos(f"{PUTHU} tước đoạt mạng sống của mẹ")),
])
P809_2 = " ".join([
    knows(neg(f"{SAMPANNA} tước đoạt mạng sống của cha… tước đoạt mạng sống của một vị A-la-hán… với tâm độc ác làm "
              f"cho {NL} chảy máu… chia rẽ Tăng đoàn… tôn người khác làm bậc đạo sư… tạo ra lần hiện hữu thứ tám")),
    knows(pos(f"{PUTHU} tạo ra lần hiện hữu thứ tám")),
])
BUDDHA2 = "hai bậc A-la-hán, Tự Giác Ngộ Hoàn Toàn"
VAR_CAKKA = " [khác chính tả (Sī., Syā.): cakkavatti]"
P809_3 = " ".join([
    knows(neg(f"{BUDDHA2} xuất hiện trong cùng một thế giới, không trước không sau")),
    knows(pos("một bậc A-la-hán, Tự Giác Ngộ Hoàn Toàn xuất hiện trong một thế giới")),
    knows(neg(f"hai vị vua chuyển luân{VAR_CAKKA} xuất hiện trong cùng một thế giới, không trước không sau")),
    knows(pos("một vị vua chuyển luân xuất hiện trong một thế giới")),
])
STATUS = "giữ địa vị Đế Thích, giữ địa vị Ma vương, giữ địa vị Phạm thiên"   # sakkattaṃ … brahmattaṃ kareyya [new]
P809_4 = " ".join([
    knows(neg("người nữ trở thành bậc A-la-hán, Tự Giác Ngộ Hoàn Toàn")),
    knows(pos("người nam trở thành bậc A-la-hán, Tự Giác Ngộ Hoàn Toàn")),
    knows(neg("người nữ trở thành vua chuyển luân")),
    knows(pos("người nam trở thành vua chuyển luân")),
    knows(neg(f"người nữ {STATUS}")),
    knows(pos(f"người nam {STATUS}")),
])
P809_5 = " ".join([
    knows(neg(ripen(DUC["kāya"], True))),
    knows(pos(ripen(DUC["kāya"], False))),
    knows(neg(f"{DUC['vacī']}… việc {ripen(DUC['mano'], True)}")),
    knows(pos(f"{DUC['vacī']}… việc {ripen(DUC['mano'], False)}")),
])
P809_6 = " ".join([
    knows(neg(ripen(SUC["kāya"], False))),
    knows(pos(ripen(SUC["kāya"], True))),
    knows(neg(f"{SUC['vacī']}… việc {ripen(SUC['mano'], False)}")),
    knows(pos(f"{SUC['vacī']}… việc {ripen(SUC['mano'], True)}")),
])
P809_7 = " ".join([
    knows(neg(rebirth(DUC["kāya"], True))),
    knows(pos(rebirth(DUC["kāya"], False))),
    knows(neg(f"người có {DUC['vacī']}… người có {DUC['mano']}, do nguyên nhân ấy, do điều kiện ấy, {DEATH}, tái sinh "
              f"vào {GOOD}")),
    knows(pos(f"người có {DUC['vacī']}… người có {DUC['mano']}, do nguyên nhân ấy, do điều kiện ấy, {DEATH}, tái sinh "
              f"vào {BAD3}")),
])
CAUSE = (f"“Những hiện tượng nào là nguyên nhân, là điều kiện của những hiện tượng nào, thì tùy thuộc vào đó, đó là "
         f"{TH}; những hiện tượng nào không phải là nguyên nhân, không phải là điều kiện của những hiện tượng nào, thì "
         f"tùy thuộc vào đó, đó là {ATH}”.")                              # [pi-1 ^1-1344 / ^1-1345 words; upādāya new]
P809_8 = " ".join([
    knows(neg(rebirth(SUC["kāya"], False))),
    knows(pos(rebirth(SUC["kāya"], True))),
    knows(neg(f"người có {SUC['vacī']}… người có {SUC['mano']}, do nguyên nhân ấy, do điều kiện ấy, {DEATH}, tái sinh "
              f"vào {BAD3}")),
    knows(pos(f"người có {SUC['vacī']}… người có {SUC['mano']}, do nguyên nhân ấy, do điều kiện ấy, {DEATH}, tái sinh "
              f"vào {GOOD}")),
    CAUSE,
    f"{cap(TP)} {DASH} đây là {bala_name(BALA[0])}.",
])


GATI = {"gati": "cõi tái sinh", "upadhi": "thân thể", "kāla": "thời điểm", "payoga": "sự nỗ lực"}   # [new]
G4 = ["gati", "upadhi", "kāla", "payoga"]


def k810(bad, sampatti, blocked):
    kind = "xấu ác" if bad else "tốt đẹp"
    out = []
    for g in G4:
        cond = f"sự {'thuận lợi' if sampatti else 'bất lợi'} về {GATI[g]}"
        if blocked:
            out.append(f"Có một số nghiệp {kind} đã thực hiện bị {cond} ngăn trở nên không trổ quả.")
        else:
            out.append(f"Có một số nghiệp {kind} đã thực hiện trổ quả nhờ dựa vào {cond}.")
    return " ".join(out)


DHI = {"hīna": "những chúng sinh có chí hướng thấp kém", "paṇīta": "những chúng sinh có chí hướng ưu việt"}   # [new]
SEV = {"pres": "gần gũi, lui tới, thường xuyên lui tới hầu cận",
       "past": "đã gần gũi, đã lui tới, đã thường xuyên lui tới hầu cận",
       "fut": "sẽ gần gũi, sẽ lui tới, sẽ thường xuyên lui tới hầu cận"}   # [ch12 words]


EXIST = (f"Có {DHI['hīna']}, có {DHI['paṇīta']}.")
SEV_PRES = f"{cap(DHI['hīna'])} {SEV['pres']} {DHI['hīna']}. {cap(DHI['paṇīta'])} {SEV['pres']} {DHI['paṇīta']}."
SEV_PAST_C = f"cả trong thời quá khứ, {DHI['hīna']} {SEV['past']} {DHI['hīna']}, {DHI['paṇīta']} {SEV['past']} {DHI['paṇīta']}"
SEV_FUT_C = f"cả trong thời tương lai, {DHI['hīna']} {SEV['fut']} {DHI['hīna']}, {DHI['paṇīta']} {SEV['fut']} {DHI['paṇīta']}"
SEV_PAST_S = f"cả trong thời quá khứ, {DHI['hīna']} {SEV['past']} {DHI['hīna']}. {cap(DHI['paṇīta'])} {SEV['past']} {DHI['paṇīta']}"
SEV_FUT_S = f"cả trong thời tương lai, {DHI['hīna']} {SEV['fut']} {DHI['hīna']}. {cap(DHI['paṇīta'])} {SEV['fut']} {DHI['paṇīta']}"

ASAYA, ANUSAYA, CARITA, ADHIMUTTI = "thiên hướng", "khuynh hướng tiềm ẩn", "tính hạnh", "chí hướng"   # [new; anusaya pi-1]
ANU7 = ["tham đắm dục lạc", "ác cảm", "kiêu mạn", "quan điểm", "hoài nghi", "tham đắm hiện hữu", "vô minh"]   # [pi-1 words]
TYPES = {"apparajakkha": "ít bụi trong mắt", "mahārajakkha": "nhiều bụi trong mắt",
         "tikkhindriya": "có các năng lực sắc bén", "mudindriya": "có các năng lực non yếu",
         "svākāra": "có phẩm chất tốt", "dvākāra": "có phẩm chất xấu", "suviññāpaya": "dễ hướng dẫn",
         "duviññāpaya": "khó hướng dẫn", "bhabba": "có khả năng", "abhabba": "không có khả năng"}   # [new]


def beings(t):
    return f"những chúng sinh {TYPES[t]}"


def who(t):
    return f"{cap(beings(t))} là những ai?"


DONE4 = "được thực hành, được tu tập, được làm đi làm lại, trở nên nổi trội"   # āsevita … ussadagata [ch7 / ch12 words]
NOT4 = "không được thực hành, không được tu tập, không được làm đi làm lại, không trở nên nổi trội"
IND5 = "Năm năng lực " + DASH + " " + T.listing(["năng lực niềm tin", "năng lực tinh tấn", "năng lực tỉnh thức",
                                                  "năng lực định tâm", "năng lực trí tuệ"])   # [pi-1 / ch5 names]
in_out("5-indriyavibhango.md", "năng lực niềm tin, năng lực tinh tấn")
AVARANA = {"kamma": "sự ngăn che do nghiệp", "kilesa": "sự ngăn che do phiền não", "vipāka": "sự ngăn che do quả của nghiệp"}
NIYAMA = "bước vào sự cố định, tức sự đúng đắn trong các hiện tượng thiện"   # niyāmaṃ okkamituṃ … sammattaṃ [new]

# jhāna / vimokkha / samādhi / samāpatti (^2-828)
JHAYI = "người hành thiền"
VIM = "sự giải thoát"                                                      # vimokkha [new]
ORD8 = ["thứ nhất", "thứ hai", "thứ ba", "thứ tư", "thứ năm", "thứ sáu", "thứ bảy", "thứ tám"]
SAM3 = ("Ba loại định tâm " + DASH + " định tâm có sự hướng tâm và sự duy trì tâm; định tâm không có sự hướng tâm, chỉ "
        "có sự duy trì tâm; và định tâm không có sự hướng tâm cũng không có sự duy trì tâm")   # [B item words]
SAMAP9_LIST = T.listing(JH_SAMAP + [NIRODHA_SAMAP])

# Ekaka exposition helpers
VINN = dict(zip(("cakkhu", "sota", "ghāna", "jivhā", "kāya"), S.VINNANA6.split(", ")[:5]))   # thức qua mắt … [pi-1]
GOCARA = "phạm vi hoạt động"


def gocara(a, b, first_cap):
    s = f"{GOCARA} của {VINN[a]} thì {VINN[b]} không trải nghiệm, {GOCARA} của {VINN[b]} thì {VINN[a]} cũng không trải nghiệm"
    return cap(s) if first_cap else s


def samanant(a, b, first_cap):
    s = (f"ngay liền sau khi {VINN[a]} sinh khởi, {VINN[b]} không sinh khởi, ngay liền sau khi {VINN[b]} sinh khởi, "
         f"{VINN[a]} cũng không sinh khởi")
    return cap(s) if first_cap else s


EK = {   # the onefold statements (3) … (27) [new]
    "Purejātavatthukā purejātārammaṇā": "có chỗ dựa đã sinh ra trước, có đối tượng đã sinh ra trước",
    "Ajjhattikavatthukā bāhirārammaṇā": "có chỗ dựa thuộc phần bên trong, có đối tượng thuộc phần bên ngoài",
    "Asambhinnavatthukā asambhinnārammaṇā": "có chỗ dựa chưa tan rã, có đối tượng chưa tan rã",
    "Nānāvatthukā nānārammaṇā": "có chỗ dựa khác nhau, có đối tượng khác nhau",
    "Uppannavatthukā uppannārammaṇā": "có chỗ dựa đã sinh khởi, có đối tượng đã sinh khởi",
    "Na aññamaññassa gocaravisayaṃ paccanubhonti": f"không trải nghiệm {GOCARA} của nhau",
    "Na asamannāhārā uppajjanti": "không sinh khởi khi không có sự lưu ý",
    "Na amanasikārā uppajjanti": "không sinh khởi khi không có sự chú tâm",
    "Na abbokiṇṇā uppajjanti": "không sinh khởi liền mạch",
    "Na apubbaṃ acarimaṃ uppajjanti": "không sinh khởi không trước không sau",
    "Na aññamaññassa samanantarā uppajjanti": "không sinh khởi ngay liền sau nhau",
    "Pañca viññāṇā anābhogā": f"{FIVE} không có sự chú hướng",
}
BY5, AFTER5 = f"bằng {FIVE}, người ta", f"ngay cả liền sau {FIVE}, người ta cũng"
AFTER5_MD = f"bằng cả yếu tố ý sinh liền sau {FIVE}, người ta cũng"         # samanantarā manodhātuyāpi [new]
ACT = {   # predicates after Pañcahi viññāṇehi / samanantarāpi
    "na kañci dhammaṃ paṭivijānāti": "không nhận biết rõ bất cứ hiện tượng nào",
    "na kañci iriyāpathaṃ kappeti": "không thực hiện bất cứ tư thế nào",
    "na kāyakammaṃ na vacīkammaṃ paṭṭhapeti": "không khởi lập nghiệp bằng thân hay nghiệp bằng lời nói",
    "na kusalākusalaṃ dhammaṃ samādiyati": "không thọ trì hiện tượng thiện hay bất thiện",
    "na samāpajjati na vuṭṭhāti": "không chứng nhập, không xuất khỏi",
    "na cavati na uppajjati": "không chết, không tái sinh",
    "na supati na paṭibujjhati na supinaṃ passati": "không ngủ, không thức dậy, không nằm mơ",
}
POSTURE = "hoặc đi, hoặc đứng, hoặc ngồi, hoặc nằm"                       # gamanaṃ vā ṭhānaṃ vā nisajjaṃ vā seyyaṃ vā
YATHAVA = f"{TRI} làm sáng tỏ sự vật đúng như thật"                        # yāthāvakavatthuvibhāvanā paññā [new]
VAR_KINCI = " [khác chính tả (Sī., Ka.): kiñci]"
ABHINIPATA = "ngoại trừ sự va chạm đơn thuần"
APATA = "ngoại trừ sự hiện ra đơn thuần"


def ek_stmt(t):
    """(13) … (27) statements of the onefold matrix (no final stop)"""
    if t in EK:
        return cap(EK[t])
    if t.startswith("Pañcahi viññāṇehi na kañci [kiñci (sī. ka.)] dhammaṃ paṭivijānāti aññatra abhinipātamattā"):
        return f"{cap(BY5)} {ACT['na kañci dhammaṃ paṭivijānāti']}{VAR_KINCI}, {ABHINIPATA}"
    m = re.match(r"^Pañcahi viññāṇehi (.+)$", t)
    if m:
        return f"{cap(BY5)} {ACT[m.group(1)]}"
    m = re.match(r"^Pañcannaṃ viññāṇānaṃ samanantarāpi (.+?)(, yāthāvakavatthuvibhāvanā paññā)?$", t)
    if m:
        return f"{cap(AFTER5)} {ACT[m.group(1)]}" + (f", {YATHAVA}" if m.group(2) else "")
    raise KeyError("ekaka statement: " + t)


GOCARA_P = ("Na aññamaññassa gocaravisayaṃ paccanubhontīti cakkhuviññāṇassa gocaravisayaṃ sotaviññāṇaṃ na "
            "paccanubhoti, sotaviññāṇassa gocaravisayampi cakkhuviññāṇaṃ na paccanubhoti. Cakkhuviññāṇassa "
            "gocaravisayaṃ ghānaviññāṇaṃ na paccanubhoti, ghānaviññāṇassa gocaravisayampi cakkhuviññāṇaṃ na "
            "paccanubhoti. Cakkhuviññāṇassa gocaravisayaṃ jivhāviññāṇaṃ na paccanubhoti, jivhāviññāṇassa "
            "gocaravisayampi cakkhuviññāṇaṃ na paccanubhoti. Cakkhuviññāṇassa gocaravisayaṃ kāyaviññāṇaṃ na "
            "paccanubhoti, kāyaviññāṇassa gocaravisayampi cakkhuviññāṇaṃ na paccanubhoti. Sotaviññāṇassa…pe… "
            "ghānaviññāṇassa…pe… jivhāviññāṇassa…pe… kāyaviññāṇassa gocaravisayaṃ cakkhuviññāṇaṃ na paccanubhoti, "
            "cakkhuviññāṇassa gocaravisayampi kāyaviññāṇaṃ na paccanubhoti. Kāyaviññāṇassa gocaravisayaṃ "
            "sotaviññāṇaṃ na paccanubhoti, sotaviññāṇassa gocaravisayampi kāyaviññāṇaṃ na paccanubhoti. "
            "Kāyaviññāṇassa gocaravisayaṃ ghānaviññāṇaṃ na paccanubhoti, ghānaviññāṇassa gocaravisayampi "
            "kāyaviññāṇaṃ na paccanubhoti. Kāyaviññāṇassa gocaravisayaṃ jivhāviññāṇaṃ na paccanubhoti, "
            "jivhāviññāṇassa gocaravisayampi kāyaviññāṇaṃ na paccanubhoti.")


def lemma(lem_vi, rest_vi):
    return f"“{cap(lem_vi)}”: {rest_vi}."


def ek_expo(t):
    """the onefold exposition lines (^2-762 … ^2-766)"""
    m = re.match(r"^(Pañca viññāṇā )?(\w+)vatthukā, (\w+)ārammaṇāti (.+)\.$", t)
    if m:
        key = f"{cap(m.group(2))}vatthukā {m.group(3)}ārammaṇā"
        lv = (FIVE + " " if m.group(1) else "") + EK[key]
        rest = m.group(4)
        if rest.startswith("uppannasmiṃ"):
            r = "chúng sinh khởi khi chỗ dựa đã sinh khởi, đối tượng đã sinh khởi"
        elif rest.startswith("purejātasmiṃ"):
            r = "chúng sinh khởi khi chỗ dựa đã sinh ra trước, đối tượng đã sinh ra trước"
        elif rest.startswith("asambhinnasmiṃ"):
            r = "chúng sinh khởi khi chỗ dựa chưa tan rã, đối tượng chưa tan rã"
        elif rest == "pañcannaṃ viññāṇānaṃ vatthu ajjhattikā ārammaṇā bāhirā":
            r = f"chỗ dựa của {FIVE} thuộc phần bên trong, các đối tượng thuộc phần bên ngoài"
        elif rest.startswith("aññaṃ cakkhuviññāṇassa"):
            assert rest == ", ".join(f"aññaṃ {d}viññāṇassa vatthu ca ārammaṇañca" for d in VINN), rest
            r = ", ".join(f"chỗ dựa và đối tượng của {VINN[d]} là khác" for d in VINN)
        else:
            raise KeyError(rest)
        return lemma(lv, r)
    if t.startswith("Na aññamaññassa gocaravisayaṃ paccanubhontīti "):
        assert t == GOCARA_P, t
        s1 = ". ".join(gocara("cakkhu", b, True) for b in ("sota", "ghāna", "jivhā", "kāya"))
        mid = (f"{GOCARA} của {VINN['sota']}… của {VINN['ghāna']}… của {VINN['jivhā']}… của {VINN['kāya']} thì "
               f"{VINN['cakkhu']} không trải nghiệm, {GOCARA} của {VINN['cakkhu']} thì {VINN['kāya']} cũng không trải "
               "nghiệm")
        s3 = ". ".join(cap(f"{GOCARA} của {VINN['kāya']} thì {VINN[b]} không trải nghiệm, {GOCARA} của {VINN[b]} thì "
                           f"{VINN['kāya']} cũng không trải nghiệm") for b in ("sota", "ghāna", "jivhā"))
        return f"“{cap(EK['Na aññamaññassa gocaravisayaṃ paccanubhonti'])}”: {low(s1)}. {cap(mid)}. {s3}."
    if t.startswith("Pañca viññāṇā na hetumeva, "):
        items = t[len("Pañca viññāṇā "):-1].split(", ")
        return f"{cap(FIVE)} " + "; ".join(meva_item(x) for x in items) + "."
    if t.startswith("Na aññamaññassa samanantarā uppajjantīti "):
        exp = (GOCARA_P.replace("Na aññamaññassa gocaravisayaṃ paccanubhontīti", "Na aññamaññassa samanantarā "
                                "uppajjantīti").replace("gocaravisayampi ", "uppannasamanantarāpi ")
               .replace("gocaravisayaṃ ", "uppannasamanantarā ").replace("na paccanubhoti", "na uppajjati"))
        assert t == exp, t
        s1 = ". ".join(samanant("cakkhu", b, True) for b in ("sota", "ghāna", "jivhā", "kāya"))
        mid = (f"ngay liền sau khi {VINN['sota']}… {VINN['ghāna']}… {VINN['jivhā']}… {VINN['kāya']} sinh khởi, "
               f"{VINN['cakkhu']} không sinh khởi, ngay liền sau khi {VINN['cakkhu']} sinh khởi, {VINN['kāya']} cũng "
               "không sinh khởi")
        s3 = ". ".join(cap(f"ngay liền sau khi {VINN['kāya']} sinh khởi, {VINN[b]} không sinh khởi, ngay liền sau khi "
                           f"{VINN[b]} sinh khởi, {VINN['kāya']} cũng không sinh khởi") for b in ("sota", "ghāna", "jivhā"))
        assert exp.count("na uppajjati") == 16 and "Sotaviññāṇassa…pe… ghānaviññāṇassa…pe… jivhāviññāṇassa…pe… " \
            "kāyaviññāṇassa uppannasamanantarā cakkhuviññāṇaṃ na uppajjati" in exp
        return f"“{cap(EK['Na aññamaññassa samanantarā uppajjanti'])}”: {low(s1)}. {cap(mid)}. {s3}."
    simple = {
        "Na asamannāhārā uppajjantīti samannāharantassa uppajjanti.":
            lemma(EK["Na asamannāhārā uppajjanti"], "chúng sinh khởi ở người đang lưu ý"),
        "Na amanasikārā uppajjantīti manasikarontassa uppajjanti.":
            lemma(EK["Na amanasikārā uppajjanti"], "chúng sinh khởi ở người đang chú tâm"),
        "Na abbokiṇṇā uppajjantīti na paṭipāṭiyā uppajjanti.":
            lemma(EK["Na abbokiṇṇā uppajjanti"], "chúng không sinh khởi theo thứ tự lần lượt"),
        "Na apubbaṃ acarimaṃ uppajjantīti na ekakkhaṇe uppajjanti.":
            lemma(EK["Na apubbaṃ acarimaṃ uppajjanti"], "chúng không sinh khởi trong cùng một khoảnh khắc"),
        ("Pañca viññāṇā anābhogāti pañcannaṃ viññāṇānaṃ natthi āvaṭṭanā vā ābhogo vā samannāhāro vā manasikāro "
         "vā."): lemma(EK["Pañca viññāṇā anābhogā"], f"ở {FIVE} không có sự hướng đến, hay sự chú hướng, hay sự lưu ý, "
                                                    "hay sự chú tâm"),
        "Aññatra abhinipātamattāti aññatra āpātamattā.": lemma(ABHINIPATA, APATA),
        "Evaṃ yāthāvakavatthuvibhāvanā paññā.": f"Như vậy là {YATHAVA}.",
    }
    if t in simple:
        return simple[t]
    m = re.match(r"^Pañcahi viññāṇehi (.+?)ti pañcahi viññāṇehi (.+?)( – gamanaṃ vā ṭhānaṃ vā nisajjaṃ vā seyyaṃ vā)?\.$", t)
    if m:
        a = m.group(1)
        a = a[:-1] + a[-1:] if not a.endswith("ī") else a[:-1] + "i"
        assert a == m.group(2), (a, m.group(2))
        v = f"{BY5} {ACT[a]}"
        return lemma(v, v + (f" {DASH} {POSTURE}" if m.group(3) else ""))
    m = re.match(r"^Pañcannaṃ viññāṇānaṃ samanantarāpi (.+?)ti pañcannaṃ viññāṇānaṃ samanantarā manodhātuyāpi (.+?)"
                 r"( – gamanaṃ vā ṭhānaṃ vā nisajjaṃ vā seyyaṃ vā)?\.( Evaṃ yāthāvakavatthuvibhāvanā paññā\.)?$", t)
    if m:
        a = m.group(1)
        a = a[:-1] + "i" if a.endswith("ī") else a
        assert a == m.group(2), (a, m.group(2))
        out = lemma(f"{AFTER5} {ACT[a]}", f"{AFTER5_MD} {ACT[a]}" + (f" {DASH} {POSTURE}" if m.group(3) else ""))
        if m.group(4):
            out += f" Như vậy là {YATHAVA}."
        return out
    raise KeyError("ekaka exposition: " + t[:80])


# ================================================================ 6. the matrix lists (ekaka … dasaka)
LABELS = {
    "### Ñāṇavibhaṅgo": "### " + S.CHAPTER_TITLES[16],
    "Ñāṇavibhaṅgo niṭṭhito.": S.CHAPTER_CLOSING.format(title=S.CHAPTER_TITLES[16]),
    "#### Mātikā": "#### Ma trận",                                          # [pi-1 rūpakaṇḍa]
}
GROUP = {"Ekaka": 1, "Duka": 2, "Tika": 3, "Catukka": 4, "Pañcaka": 5, "Chakka": 6, "Sattaka": 7, "Aṭṭhaka": 8,
         "Navaka": 9, "Dasaka": 10}
BO = {1: "bộ một", 2: "bộ đôi", 3: "bộ ba", 4: "bộ bốn", 5: "bộ năm", 6: "bộ sáu", 7: "bộ bảy", 8: "bộ tám",
      9: "bộ chín", 10: "bộ mười"}                                          # Tika- / Dukamātikā [pi-1 «Ma trận bộ ba / đôi»]
in_pi1("#### Ma trận bộ ba", "#### Ma trận bộ đôi", "##### Giải thích phân loại theo nhóm một",
       "Phân loại theo nhóm bốn.")
for _g, _n in GROUP.items():
    LABELS[f"#### {_g}mātikā"] = f"#### Ma trận {BO[_n]}"
    LABELS[f"##### {_g}niddeso"] = f"##### Giải thích phân loại theo nhóm {S.NUM[_n]}"   # [pi-1 ^1-2-3-1-0 …]
    LABELS[f"{_g}ṃ."] = f"Phân loại theo nhóm {S.NUM[_n]}."              # Ekakaṃ. … [pi-1 rūpakaṇḍa ^1-584 …]
FRAME_RE = re.compile(r"^(Evaṃ )?(\w+?)[vb]idhena ñāṇavatthu( –|\.)?(.*)$")


def matika_list(body):
    """'(n) …' items of the duka / tika matrix"""
    m = re.match(r"^(.+?) paññā atthi (.+)$", body)
    if m:
        subj_p = m.group(1)
        subs = [pn(x) for x in subj_p.split(" paññā ")]
        items = m.group(2).split(", atthi ")
        return f"{cap(', '.join(subs))}: " + ", ".join(atthi(x) for x in items)
    if body.startswith("Atthi "):
        return cap(", ".join(atthi(x) for x in body[len("Atthi "):].split(", atthi ")))
    if body.endswith(" paññā") and "ñāṇaṃ" not in body:
        return cap(", ".join(pn(x[:-len(" paññā")]) for x in body.split(", ")))
    raise KeyError("matrix item: " + body)


CATUKKA_M = {   # catukkamātikā (1) … (12-21)
    "Kammassakatañāṇaṃ, saccānulomikaṃ ñāṇaṃ, maggasamaṅgissa ñāṇaṃ, phalasamaṅgissa ñāṇaṃ":
        cap(", ".join((KAMMASSAKA, SACCANU, MAGGASAM, PHALASAM))),
    "Dukkhe ñāṇaṃ, dukkhasamudaye ñāṇaṃ, dukkhanirodhe ñāṇaṃ, dukkhanirodhagāminiyā paṭipadāya ñāṇaṃ": cap(DUKKHA4),
    ("Dhamme ñāṇaṃ, anvaye ñāṇaṃ, pariye [paricce (sabbattha) passa dīghanikāye] ñāṇaṃ, sammutiñāṇaṃ [sammatiñāṇaṃ "
     "(syā.) passa dīghanikāye]"):
        cap(f"{NAMES['dhamme']}, {NAMES['anvaye']}, {NAMES['pariye']}{VAR_PARIYE}, {NAMES['sammuti']}{VAR_SAMMUTI}"),
    ("Atthi paññā ācayāya no apacayāya, atthi paññā apacayāya no ācayāya, atthi paññā ācayāya ceva apacayāya ca, "
     "atthi paññā nevācayāya no apacayāya"):
        cap(", ".join(f"có {TRI} {ACAYA[k]}" for k in (
            "ācayāya no apacayāya", "apacayāya no ācayāya", "ācayāya ceva apacayāya ca", "nevācayāya no apacayāya"))),
    ("Atthi paññā nibbidāya no paṭivedhāya, atthi paññā paṭivedhāya no nibbidāya, atthi paññā nibbidāya ceva "
     "paṭivedhāya ca, atthi paññā neva nibbidāya no paṭivedhāya"):
        cap(", ".join(f"có {TRI} {ACAYA[k]}" for k in ("nibbidāya no paṭivedhāya", "paṭivedhāya no nibbidāya",
                                                        "nibbidāya ceva paṭivedhāya ca",
                                                        "neva nibbidāya no paṭivedhāya"))),
    "Hānabhāginī paññā, ṭhitibhāginī paññā, visesabhāginī paññā, nibbedhabhāginī paññā":
        cap(", ".join(pn(x) for x in ("hānabhāginī", "ṭhitibhāginī", "visesabhāginī", "nibbedhabhāginī"))),
    "Catasso paṭisambhidā": f"Bốn {Y.PS_UNIT}",
    "Catasso paṭipadā": "Bốn cách thực hành",
    "Cattāri ārammaṇāni": "Bốn đối tượng",
    ("Jarāmaraṇe ñāṇaṃ, jarāmaraṇasamudaye ñāṇaṃ, jarāmaraṇanirodhe ñāṇaṃ, jarāmaraṇanirodhagāminiyā paṭipadāya "
     "ñāṇaṃ"): cap(", ".join(four(DA["jarāmaraṇa"]))),
}
DA_TAIL = ", ".join(four(DA["saṅkhāra"]))
P754_1221 = (cap("… ".join(kn(DA[k]) for k in DA_ORDER)) + "… " + DA_TAIL + ". " + frame_close(4))
OTHER_M = {
    "Pañcaṅgiko sammāsamādhi (2) pañcañāṇiko sammāsamādhi": f"{cap(SAMADHI5)} (2) {SAMADHI5N}",
    "Chasu abhiññāsu paññā": cap(f"{TRI} trong {ABHINNA6}"),
    "Sattasattati ñāṇavatthūni": cap(NV77),
    "Catūsu maggesu, catūsu phalesu paññā": cap(f"{TRI} {MP}"),
    "Navasu anupubbavihārasamāpattīsu paññā": cap(f"{TRI} trong {SAMAP9}"),
}


def matrix_line(t):
    m = FRAME_RE.match(t)
    if m:
        ev, nk, d, rest = m.groups()
        n = NUMV[low(nk)]
        if ev:
            assert d == "." and not rest, t
            return frame_close(n)
        if t.startswith("Ekavidhena ñāṇavatthu – pañca viññāṇā "):
            items = rest[len(" pañca viññāṇā "):].rstrip(",").split(", ")
            return f"{frame_open(1)} {DASH} {FIVE} " + "; ".join(ekaka_item(x) for x in items) + ";"
        if t.startswith("Dasavidhena ñāṇavatthu – dasa tathāgatassa"):
            assert t == ("Dasavidhena ñāṇavatthu – dasa tathāgatassa tathāgatabalāni yehi balehi samannāgato tathāgato "
                         "āsabhaṃ ṭhānaṃ paṭijānāti, parisāsu sīhanādaṃ nadati, brahmacakkaṃ pavatteti. Katamāni dasa?"), t
            return f"{frame_open(10)} {DASH} mười {TB} của {NL} {EQUIP}. Mười điều đó là gì?"
        assert d == " –" and not rest, t
        return f"{frame_open(n)} {DASH}"
    if t == "Uppannavatthukā uppannārammaṇā,":
        return cap(EK["Uppannavatthukā uppannārammaṇā"]) + ";"
    m = re.match(r"^\((\d+(?:-\d+)?)\) (.+)$", t)
    if not m:
        raise KeyError("matrix line: " + t[:80])
    num, body = m.groups()
    pre = f"({num}) "
    if body.startswith("Jātiyā ñāṇaṃ…pe… bhave ñāṇaṃ"):
        exp = ("Jātiyā ñāṇaṃ…pe… bhave ñāṇaṃ…pe… upādāne ñāṇaṃ…pe… taṇhāya ñāṇaṃ…pe… vedanāya ñāṇaṃ…pe… phasse "
               "ñāṇaṃ…pe… saḷāyatane ñāṇaṃ…pe… nāmarūpe ñāṇaṃ…pe… viññāṇe ñāṇaṃ…pe… saṅkhāresu ñāṇaṃ, saṅkhārasamudaye "
               "ñāṇaṃ, saṅkhāranirodhe ñāṇaṃ, saṅkhāranirodhagāminiyā paṭipadāya ñāṇaṃ. Evaṃ catubbidhena ñāṇavatthu.")
        assert body == exp, body
        return pre + P754_1221
    if body in CATUKKA_M:
        return pre + CATUKKA_M[body]
    if body in OTHER_M:
        return pre + OTHER_M[body]
    if body in EK or body.startswith(("Pañcahi viññāṇehi", "Pañcannaṃ viññāṇānaṃ samanantarāpi")):
        return pre + ek_stmt(body)
    if body.startswith(("Idha tathāgato", "Puna caparaṃ tathāgato")):
        i = int(num) - 1
        return bala_check(i, body)
    if body in ("Adhisīle paññā, adhicitte paññā, adhipaññāya paññā",):
        return pre + cap(", ".join(pn(x) for x in ("adhisīle", "adhicitte", "adhipaññāya")))
    if body == "Āyakosallaṃ, apāyakosallaṃ, upāyakosallaṃ":
        return pre + cap(", ".join(KOSALLA[k] for k in ("āya", "apāya", "upāya")))
    return pre + matika_list(body)


_BALA_P = ["ṭhānañca ṭhānato aṭṭhānañca aṭṭhānato",
           "atītānāgatapaccuppannānaṃ kammasamādānānaṃ ṭhānaso hetuso vipākaṃ",
           "sabbatthagāminiṃ paṭipadaṃ",
           "anekadhātu nānādhātulokaṃ",
           "sattānaṃ nānādhimuttikataṃ",
           "parasattānaṃ parapuggalānaṃ indriyaparopariyattaṃ",
           "jhānavimokkhasamādhisamāpattīnaṃ saṃkilesaṃ vodānaṃ vuṭṭhānaṃ",
           "pubbenivāsānussatiṃ",
           "sattānaṃ cutūpapātaṃ",
           "āsavānaṃ khayaṃ"]
_BALA_TAIL = ("idampi tathāgatassa tathāgatabalaṃ hoti, yaṃ balaṃ āgamma tathāgato āsabhaṃ ṭhānaṃ paṭijānāti, parisāsu "
              "sīhanādaṃ nadati, brahmacakkaṃ pavatteti.")


def bala_check(i, body):
    head = "Idha tathāgato" if i == 0 else "Puna caparaṃ tathāgato"
    obj = _BALA_P[i]
    obj1 = obj + " [anekadhātuṃ nānādhātuṃ lokaṃ (syā.) ma. ni. 1.148]" if i == 3 else obj
    exp = (f"{head} {obj1} yathābhūtaṃ pajānāti. Yampi tathāgato {obj} yathābhūtaṃ pajānāti, {_BALA_TAIL}")
    if i == 9:
        exp += (" Imāni dasa tathāgatassa tathāgatabalāni, yehi balehi samannāgato tathāgato āsabhaṃ ṭhānaṃ "
                "paṭijānāti, parisāsu sīhanādaṃ nadati, brahmacakkaṃ pavatteti.")
    assert body == exp, (i, body[-150:])
    vi = bala_line(i)
    if i == 9:
        vi += f" Đây là mười {TB} của {NL}, {EQUIP}."
    return vi


# ================================================================ 7. the duka / tika / catukka expositions
def duka_line(t):
    """'(n) A paññā X paññā, B paññā Y paññā.' (ch16 duka exposition, tika (5) … (11))"""
    pre, rest = lab(t)
    assert rest.endswith("."), rest
    body = rest[:-1]
    special = {
        "Sabbāva paññā kenaci viññeyyā, kenaci na viññeyyā":
            f"mọi {TRI} đều {B.ITEMS['kenaci']['s']}, {B.ITEMS['kenaci_na']['s']}",
        ("Kāmāvacarakusalābyākate paññā kāmāvacarā paññā, rūpāvacarā paññā arūpāvacarā paññā, apariyāpannā paññā na "
         "kāmāvacarā paññā"):
            f"{subj('kāmāvacarakusalābyākate')} là {pn('kāmāvacarā')}, {pn('rūpāvacarā')}, {pn('arūpāvacarā')}, "
            f"{pn('apariyāpannā')} là {pn('na kāmāvacarā')}",
        ("Rūpāvacarakusalābyākate paññā rūpāvacarā paññā, kāmāvacarā paññā arūpāvacarā paññā apariyāpannā paññā na "
         "rūpāvacarā paññā"):
            f"{subj('rūpāvacarakusalābyākate')} là {pn('rūpāvacarā')}, {pn('kāmāvacarā')}, {pn('arūpāvacarā')}, "
            f"{pn('apariyāpannā')} là {pn('na rūpāvacarā')}",
        ("Arūpāvacarakusalābyākate paññā arūpāvacarā paññā, kāmāvacarā paññā rūpāvacarā paññā apariyāpannā paññā na "
         "arūpāvacarā paññā"):
            f"{subj('arūpāvacarakusalābyākate')} là {pn('arūpāvacarā')}, {pn('kāmāvacarā')}, {pn('rūpāvacarā')}, "
            f"{pn('apariyāpannā')} là {pn('na arūpāvacarā')}",
    }
    if body in special:
        if body.startswith(("Kāmāvacarakusalābyākate paññā kāmāvacarā", "Rūpāvacarakusalābyākate paññā rūpāvacarā",
                            "Arūpāvacarakusalābyākate")):
            SLIPS.append(f"^2-767 {pre.strip()} 'X paññā Y paññā' without comma between subjects (punctuation; commas "
                         "added)")
        vi = special[body]
    else:
        vi = ", ".join(clause(c) for c in split_top(body))
    return pre + case(vi, rest) + "."


def split_top(body):
    return re.split(r", (?![^\[]*\])", body)


def is_duka(t):
    pre, rest = lab(t)
    if not pre or not rest.endswith(".") or "?" in rest or "ārabbha" in rest or "ñāṇaṃ" in rest:
        return False
    body = rest[:-1]
    return bool(re.match(r"^(.+?) paññā (.+?) paññā$", split_top(body)[0])) or body.startswith("Sabbāva paññā kenaci")


# ================================================================ 8. hand lines (checked by Pāli start / end)
def qa_ar(name, obj, quoted=True):
    """Tattha katamā X? Y ārabbha yā uppajjati paññā … – ayaṃ vuccati "X"."""
    return f"{q(name)} {ar(obj)} {DASH} {called(name, quoted)}."


def qa_gen(name, who_, quoted=True):
    return f"{q(name)} {gen(who_)} {DASH} {called(name, quoted)}."


def lowq(s):
    """lowercase «Ở đây» after a (Ka)/(Kha) label (the Pāli has 'tattha')"""
    return low(s)


YOGA = "được tạo dựng nhờ sự khéo léo"                                     # yogavihita [new]
FIELDS = (f"hoặc trong các ngành nghề {YOGA}, hoặc trong các ngành thủ công {YOGA}, hoặc trong các lĩnh vực học thuật "
          f"{YOGA}")                                                         # kammāyatana / sippāyatana / vijjāṭṭhāna
KHANTI6 = ("sự chấp nhận thuận theo, quan điểm, sự ưa thích, sự tán thành, sự xem xét, sự chấp nhận các hiện tượng sau "
           "khi suy ngẫm")                                                  # anulomikā khanti … dhammanijjhānakkhanti [new]
RUPA_ANICCA = ("hoặc rằng vật chất là vô thường, hoặc rằng cảm giác… tri giác… các sự tạo tác… thức là vô thường")


def cinta(heard):
    how = "nhờ nghe từ người khác" if heard else "khi không nghe từ người khác"
    return (f"{cap(FIELDS)}, hoặc đối với việc nghiệp là tài sản của chính mình, hoặc đối với điều thuận theo sự thật, "
            f"{RUPA_ANICCA}, thì {KHANTI6} thuộc loại như vậy mà người ta đạt được {how}")


HAND = []


def hand(start, end, vi):
    HAND.append((start, end, vi))


# --- duka (35)
hand("(35) Tattha katamā atthajāpikā paññā?", "", f"(35) {q(pn('atthajāpikā'))}")
_ARA = "của vị A-la-hán"
hand("Catūsu bhūmīsu kusale arahato abhiññaṃ", "",
     f"{cap(TRI)} trong tâm thiện thuộc bốn cõi, trong tâm mang tính chức năng không xác định về mặt đạo đức {_ARA} "
     f"đang làm sinh khởi sự hiểu biết trực tiếp, đang làm sinh khởi sự chứng đạt, là {pn('atthajāpikā')}, {TRI} trong "
     f"quả của nghiệp thuộc bốn cõi, trong tâm mang tính chức năng không xác định về mặt đạo đức {_ARA} khi sự hiểu biết "
     f"trực tiếp đã sinh khởi, khi sự chứng đạt đã sinh khởi, là {pn('jāpitatthā')}.")
# --- tika exposition
NAME_C = {"cintā": pn("cintāmayā"), "suta": pn("sutamayā"), "dāna": pn("dānamayā"), "sīla": pn("sīlamayā"),
          "adhisīla": pn("adhisīle"), "adhicitta": pn("adhicitte"), "adhipaññā": pn("adhipaññāya")}
hand("(1. Ka) tattha katamā cintāmayā paññā?", "", f"(1. a) {lowq(q(NAME_C['cintā']))}")
hand("Yogavihitesu vā kammāyatanesu", 'parato assutvā paṭilabhati – ayaṃ vuccati "cintāmayā paññā".',
     f"{cinta(False)} {DASH} {called(NAME_C['cintā'])}.")
hand("(Kha) tattha katamā sutamayā paññā? Yogavihitesu", 'parato sutvā paṭilabhati – ayaṃ vuccati "sutamayā paññā".',
     f"(b) {lowq(q(NAME_C['suta']))} {cinta(True)} {DASH} {called(NAME_C['suta'])}.")
_BHAV = f"mọi {TRI} của người đã chứng nhập đều là {pn('bhāvanāmayā')}."     # sabbāpi samāpannassa paññā … [new]
hand("(Ga) sabbāpi samāpannassa paññā bhāvanāmayā paññā.", "", f"(c) {_BHAV}")
hand("(2. Ka) tattha katamā dānamayā paññā?", '"dānamayā paññā".',
     f"(2. a) {lowq(q(NAME_C['dāna']))} {ar('sự bố thí, nhờ sự bố thí,')} {DASH} {called(NAME_C['dāna'])}.")
hand("(Kha) tattha katamā sīlamayā paññā?", '"sīlamayā paññā".',
     f"(b) {lowq(q(NAME_C['sīla']))} {ar('giới hạnh, nhờ giới hạnh,')} {DASH} {called(NAME_C['sīla'])}.")
hand("(Ga) sabbāpi samāpannassa paññā bhāvanāmayā paññā.", "", f"(c) {_BHAV}")
hand("(3. Ka) tattha katamā adhisīle paññā?", '"adhisīle paññā".',
     f"(3. a) {lowq(q(NAME_C['adhisīla']))} {gen('người đang thu thúc bằng sự thu thúc theo bộ giới luật căn bản')} "
     f"{DASH} {called(NAME_C['adhisīla'])}.")
hand("(Kha) tattha katamā adhicitte paññā?", '"adhicitte paññā".',
     f"(b) {lowq(q(NAME_C['adhicitta']))} {gen('người đang chứng nhập sự chứng đạt thuộc cõi hình sắc và cõi không hình sắc')} "
     f"{DASH} {called(NAME_C['adhicitta'])}.")
hand("(Ga) tattha katamā adhipaññāya paññā?", '"adhipaññāya paññā".',
     f"(c) {lowq(q(NAME_C['adhipaññā']))} {cap(TRI)} {MP} {DASH} {called(NAME_C['adhipaññā'])}.")
GROW = "dẫn đến sự tăng trưởng, sự lớn mạnh, sự tu tập, sự hoàn thiện"   # [pi-1 ^1-1377 / ch8 words]
GROW2 = "dẫn đến sự tăng trưởng, sự lớn mạnh"
MANAS = "Khi người ta chú tâm đến những hiện tượng này"
hand("(4. Ka) tattha katamaṃ āyakosallaṃ?", '"āyakosallaṃ".',
     f"(4. a) {lowq(q(KOSALLA['āya']))} “{MANAS}, các hiện tượng bất thiện chưa sinh khởi không sinh khởi, và các hiện "
     f"tượng bất thiện đã sinh khởi được dứt bỏ. Hoặc khi người ta chú tâm đến những hiện tượng này, các hiện tượng thiện "
     f"chưa sinh khởi sinh khởi, và các hiện tượng thiện đã sinh khởi {GROW}” {DASH} {TP} {DASH} "
     f"{called(KOSALLA['āya'])}.")
hand("(Kha) tattha katamaṃ apāyakosallaṃ?", '"apāyakosallaṃ".',
     f"(b) {lowq(q(KOSALLA['apāya']))} “{MANAS}, các hiện tượng thiện chưa sinh khởi không sinh khởi, và các hiện tượng "
     f"thiện đã sinh khởi chấm dứt. Hoặc khi người ta chú tâm đến những hiện tượng này, các hiện tượng bất thiện chưa sinh "
     f"khởi sinh khởi, và các hiện tượng bất thiện đã sinh khởi {GROW2}” {DASH} {TP} {DASH} "
     f"{called(KOSALLA['apāya'])}.")
hand("(Ga) sabbāpi tatrupāyā paññā upāyakosallaṃ.", "",
     f"(c) mọi {TRI} về phương cách cho việc ấy đều là {KOSALLA['upāya']}.")
for _k, _o, _n in (("parittārammaṇā", "các hiện tượng hạn hẹp", "12. Ka"),
                   ("mahaggatārammaṇā", "các hiện tượng rộng lớn", "Kha"),
                   ("appamāṇārammaṇā", "các hiện tượng không thể đo lường", "Ga")):
    _lab = {"12. Ka": "12. a", "Kha": "b", "Ga": "c"}[_n]
    hand(f"({_n}) tattha katamā {_k} paññā?", f'"{_k} paññā".',
         f"({_lab}) {lowq(q(pn(_k)))} {ar(_o)} {DASH} {called(pn(_k))}.")
hand("(13. Ka) tattha katamā maggārammaṇā paññā?", '"maggārammaṇā paññā".',
     f"(13. a) {lowq(q(pn('maggārammaṇā')))} {ar('con đường cao quý')} {DASH} {called(pn('maggārammaṇā'))}.")
hand("(Kha) catūsu maggesu paññā maggahetukā paññā.", "", None)   # duka form
hand("(Ga) tattha katamā maggādhipatinī paññā?", '"maggādhipatinī paññā".',
     f"(c) {lowq(q(pn('maggādhipatinī')))} Điều mà sinh khởi sau khi lấy con đường cao quý làm yếu tố chủ đạo là "
     f"{PANNA} {DASH} {called(pn('maggādhipatinī'))}.")
hand("(14) Catūsu bhūmīsu vipāke paññā siyā uppannā", "na vattabbā uppādinīti.",
     f"(14) {cap(subj('catūsu bhūmīsu vipāke'))} đôi khi {attr('uppannā')}, đôi khi {attr('uppādinī')}, không nên nói "
     f"rằng {attr('anuppannā')}. {cap(subj('catūsu bhūmīsu kusale tīsu bhūmīsu kiriyābyākate'))} đôi khi "
     f"{attr('uppannā')}, đôi khi {attr('anuppannā')}, không nên nói rằng {attr('uppādinī')}.")
hand("(15) Sabbāva paññā siyā atītā", "",
     f"(15) Mọi {TRI} đôi khi {attr('atītā')}, đôi khi {attr('anāgatā')}, đôi khi {attr('paccuppannā')}.")
for _k, _o, _n in (("atītārammaṇā", "các hiện tượng thuộc quá khứ", "16. Ka"),
                   ("anāgatārammaṇā", "các hiện tượng thuộc tương lai", "Kha"),
                   ("paccuppannārammaṇā", "các hiện tượng thuộc hiện tại", "Ga")):
    _lab = {"16. Ka": "16. a", "Kha": "b", "Ga": "c"}[_n]
    hand(f"({_n}) tattha katamā {_k} paññā?", f'"{_k} paññā".',
         f"({_lab}) {lowq(q(pn(_k)))} {ar(_o)} {DASH} {called(pn(_k))}.")
hand("(17) Sabbāva paññā siyā ajjhattā", "",
     f"(17) Mọi {TRI} đôi khi {attr('ajjhattā')}, đôi khi {attr('bahiddhā')}, đôi khi {attr('ajjhattabahiddhā')}.")
for _k, _o, _n in (("ajjhattārammaṇā", "các hiện tượng ở nơi bản thân", "18. Ka"),
                   ("bahiddhārammaṇā", "các hiện tượng ở bên ngoài bản thân", "Kha"),
                   ("ajjhattabahiddhārammaṇā", "các hiện tượng ở nơi bản thân và ở bên ngoài bản thân", "Ga")):
    _lab = {"18. Ka": "18. a", "Kha": "b", "Ga": "c"}[_n]
    hand(f"({_n}) tattha katamā {_k} paññā?", f'"{_k} paññā".',
         f"({_lab}) {lowq(q(pn(_k)))} {ar(_o)} {DASH} {called(pn(_k))}.")
hand("Evaṃ tividhena ñāṇavatthu.", "", None)   # frame
# --- catukka exposition
KQ = qq(KAMMASSAKA)
hand("(1. Ka) tattha katamaṃ kammassakatañāṇaṃ?", "sabbāpi sāsavā kusalā paññā kammassakatañāṇaṃ.",
     f"(1. a) {low(KQ)} {ATTHI_DINNA} {DASH} {EP} {DASH} {called(KAMMASSAKA)}. Ngoại trừ {SACCANU}, mọi {TRI} thiện mà "
     f"là đối tượng của ô nhiễm đều là {KAMMASSAKA}.")
hand("(Kha) tattha katamaṃ saccānulomikaṃ ñāṇaṃ?", '"saccānulomikaṃ ñāṇaṃ".',
     f"(b) {low(q(SACCANU))} “Vật chất là vô thường”, hoặc cảm giác… tri giác… các sự tạo tác…, hoặc “Thức là vô "
     f"thường”, điều mà thuộc loại như vậy là {KHANTI6} {DASH} {called(SACCANU)}.")
hand("(Ga) catūsu maggesu paññā maggasamaṅgissa ñāṇaṃ.", "", f"(c) {TRI} trong {MAGGA4} là {MAGGASAM}.")
hand("(Gha) catūsu phalesu paññā phalasamaṅgissa ñāṇaṃ.", "", f"(d) {TRI} trong {PHALA4} là {PHALASAM}.")


def also(names):
    return ", ".join(f"cũng là {n}" for n in names)


hand("(2) Maggasamaṅgissa ñāṇaṃ dukkhepetaṃ ñāṇaṃ", "dukkhanirodhagāminiyā paṭipadāyapetaṃ ñāṇaṃ.",
     f"(2) {cap(MAGGASAM)} thì {also(four('khổ đau'))}.")
hand("(Ka) tattha katamaṃ dukkhe ñāṇaṃ?", '"dukkhe ñāṇaṃ".',
     f"(a) {low(q(kn('khổ đau')))} {ar('khổ đau')} {DASH} {called(kn('khổ đau'))}.")
hand("(Kha-gha) dukkhasamudayaṃ ārabbha…pe…", '"dukkhanirodhagāminiyā paṭipadāya ñāṇaṃ".',
     f"(b-d) điều mà sinh khởi liên quan đến {TRUTH['dukkhasamudaya']}… liên quan đến {TRUTH['dukkhanirodha']}… liên "
     f"quan đến {TRUTH['dukkhanirodhagāminī']} là {PANNA} {DASH} {called(kn(TRUTH['dukkhanirodhagāminī']))}.")
hand("(3) Kāmāvacarakusalābyākate paññā kāmāvacarā paññā, rūpāvacara", "", None)   # duka form
hand("(4. Ka) tattha katamaṃ dhamme ñāṇaṃ?", "",
     f"(4. a) {low(q(NAMES['dhamme']))} {cap(TRI)} {MP} là {NAMES['dhamme']}.")
_ABB = {"past": "đã hiểu biết trực tiếp", "fut": "sẽ hiểu biết trực tiếp"}


def infer(t):
    tense = _ABB[t]
    when = "trong thời quá khứ" if t == "past" else "trong thời tương lai"
    var = " [khác chính tả (Syā.): abbhaññiṃsu; cũng vậy ở các chỗ sau]" if t == "past" else ""
    objs = list(TRUTH.values())
    a = f"Bất cứ sa-môn hay bà-la-môn nào {when} {tense} {objs[0]}{var}, " + ", ".join(f"{tense} {o}" for o in objs[1:])
    b = ", ".join(f"thì họ {tense} chính {objs[0]} này" if i == 0 else f"{tense} chính {o} này"
                  for i, o in enumerate(objs))
    return f"{a}, {b}"


hand("(Kha) so iminā dhammena ñātena", '"anvaye ñāṇaṃ".',
     f"(b) nhờ Giáo Pháp này đã được biết, đã được thấy, đã được đạt đến, đã được hiểu, đã được thâm nhập, vị ấy suy ra "
     f"cho quá khứ và tương lai. “{infer('past')}. {infer('fut')}” {DASH} {TP} {DASH} {called(NAMES['anvaye'])}.")
_CITTA_P = CITTA16_P
hand("(Ga) tattha katamaṃ pariye ñāṇaṃ?", '"pariye ñāṇaṃ".',
     f"(c) {low(q(NAMES['pariye']))} {IDHA}, {BHIKKHU} dùng tâm mình bao quát tâm của những chúng sinh khác, những "
     f"người khác mà hiểu rõ. Vị ấy {CITTA16} {DASH} {TP} {DASH} {called(NAMES['pariye'])}.")
hand("(Gha) ṭhapetvā dhamme ñāṇaṃ", "avasesā paññā sammutiñāṇaṃ.",
     f"(d) ngoại trừ {NAMES['dhamme']}, {NAMES['anvaye']}, {NAMES['pariye']}, {TRI} còn lại là {NAMES['sammuti']}.")
_AC = {k: f"{TRI} {v}" for k, v in ACAYA.items()}
hand("(5. Ka) tattha katamā paññā ācayāya no apacayāya?", "",
     f"(5. a) {low(q(_AC['ācayāya no apacayāya']))} {cap(TRI)} trong tâm thiện {AV['kāmāvacara']} "
     f"{ACAYA['ācayāya no apacayāya']}.")
hand("(Kha) catūsu maggesu paññā apacayāya no ācayāya.", "",
     f"(b) {TRI} trong {MAGGA4} {ACAYA['apacayāya no ācayāya']}.")
hand("(Ga) rūpāvacarārūpāvacarakusale paññā ācayāya ceva apacayāya ca.", "",
     f"(c) {TRI} trong tâm thiện {AV['rūpāvacarārūpāvacara']} {ACAYA['ācayāya ceva apacayāya ca']}.")
hand("(Gha) avasesā paññā neva ācayāya no apacayāya.", "", f"(d) {TRI} còn lại {ACAYA['neva ācayāya no apacayāya']}.")
hand("(6. Ka) tattha katamā paññā nibbidāya no paṭivedhāya?", '"paññā nibbidāya no paṭivedhāya".',
     f"(6. a) {low(q(_AC['nibbidāya no paṭivedhāya']))} {cap(TRI)} mà nhờ đó người ta lìa tham đắm đối với các dục lạc, "
     f"nhưng không thấu triệt các loại hiểu biết trực tiếp, cũng không thấu triệt các sự thật {DASH} "
     f"{called(_AC['nibbidāya no paṭivedhāya'])}.")
hand("(Kha) sveva paññāya kāmesu vītarāgo samāno", '"paññā paṭivedhāya no nibbidāya".',
     f"(b) chính người ấy, nhờ trí tuệ, đã lìa tham đắm đối với các dục lạc, thấu triệt các loại hiểu biết trực tiếp, "
     f"nhưng không thấu triệt các sự thật {DASH} {called(_AC['paṭivedhāya no nibbidāya'])}.")
hand("(Ga) catūsu maggesu paññā nibbidāya ceva paṭivedhāya ca.", "",
     f"(c) {TRI} trong {MAGGA4} {ACAYA['nibbidāya ceva paṭivedhāya ca']}.")
hand("(Gha) avasesā paññā neva nibbidāya no paṭivedhāya.", "",
     f"(d) {TRI} còn lại {ACAYA['neva nibbidāya no paṭivedhāya']}.")
SM = "các tri giác và sự chú tâm"                                          # saññāmanasikārā [pi-1 words]
SAH = {"kāma": "dục lạc", "avitakka": "trạng thái không có sự hướng tâm", "nibbidā": "sự nhàm chán",
       "vitakka": "sự hướng tâm", "upekkhā": "sự bình thản", "pītisukha": "sự hân hoan và hạnh phúc",
       "adukkhamasukha": "trạng thái không khó chịu cũng không dễ chịu", "rūpa": "hình sắc",
       "ākāsānañcāyatana": AYAT["ākāsānañcāyatana"], "viññāṇañcāyatana": AYAT["viññāṇañcāyatana"],
       "ākiñcaññāyatana": AYAT["ākiñcaññāyatana"], "nevasaññānāsaññāyatana": AYAT["nevasaññānāsaññāyatana"]}


def hana(x):
    return f"{SM} có {SAH[x]} đi kèm khởi lên, thì đó là {pn('hānabhāginī')}"


THITI = f"sự tỉnh thức phù hợp với điều ấy đứng vững, thì đó là {pn('ṭhitibhāginī')}"   # tadanudhammatā sati santiṭṭhati


def visesa(x):
    return f"{SM} có {SAH[x]} đi kèm khởi lên, thì đó là {pn('visesabhāginī')}"


NIBB = (f"{SM} có {SAH['nibbidā']} đi kèm khởi lên, thì đó là {TRI} liên quan đến sự phai nhạt, "
        f"{attr('nibbedhabhāginī')}")
GAIN = {"dutiya": "tầng thiền thứ hai", "tatiya": "tầng thiền thứ ba", "catuttha": "tầng thiền thứ tư",
        "ākāsānañcāyatana": AYAT["ākāsānañcāyatana"], "viññāṇañcāyatana": AYAT["viññāṇañcāyatana"],
        "ākiñcaññāyatana": AYAT["ākiñcaññāyatana"]}
_SEQ = [("dutiya", "vitakka", "upekkhā"), ("tatiya", "pītisukha", "adukkhamasukha"),
        ("catuttha", "upekkhā", "ākāsānañcāyatana"), ("ākāsānañcāyatana", "rūpa", "viññāṇañcāyatana"),
        ("viññāṇañcāyatana", "ākāsānañcāyatana", "ākiñcaññāyatana"),
        ("ākiñcaññāyatana", "viññāṇañcāyatana", "nevasaññānāsaññāyatana")]
hand("(7. Ka) tattha katamā hānabhāginī paññā?", "",
     f"(7. a) {low(q(pn('hānabhāginī')))} Ở người đã đạt được tầng thiền thứ nhất, {hana('kāma')}.")
hand("(Kha) tadanudhammatā sati santiṭṭhati ṭhitibhāginī paññā.", "", f"(b) {THITI}.")
hand("(Ga) avitakkasahagatā saññāmanasikārā samudācaranti visesabhāginī paññā.", "", f"(c) {visesa('avitakka')}.")
hand("(Gha) nibbidāsahagatā saññāmanasikārā samudācaranti virāgūpasañhitā nibbedhabhāginī paññā. Dutiyassa",
     "virāgūpasañhitā nibbedhabhāginī paññā.",
     f"(d) {NIBB}. " + " ".join(f"Ở người đã đạt được {GAIN[g]}, {hana(h)}. {cap(THITI)}. {cap(visesa(v))}. {cap(NIBB)}."
                               for g, h, v in _SEQ))
hand("(8) Tattha katamā catasso paṭisambhidā?", "Imā catasso paṭisambhidā.",
     f"(8) {q('bốn ' + Y.PS_UNIT)} {cap(', '.join(PS[k] for k in Y.PS_ORDER))}. "
     f"{cap(Y.kn('ý nghĩa', 'attha'))}, {Y.kn('các hiện tượng', 'dhamma')}, {NIR}, {PAT}. "
     f"Đây là bốn {Y.PS_UNIT}.")
in_out("15-patisambhidavibhango.md", f"{cap(Y.kn('ý nghĩa', 'attha'))}, {Y.kn('các hiện tượng', 'dhamma')}, {NIR}, {PAT}.")
_PP = list(PATIPADA)
_PDO = {"dukkhapaṭipadā dandhābhiññā": ("một cách khó nhọc, vất vả", "chậm chạp"),
        "dukkhapaṭipadā khippābhiññā": ("một cách khó nhọc, vất vả", "nhanh chóng"),
        "sukhapaṭipadā dandhābhiññā": ("một cách không khó nhọc, không vất vả", "chậm chạp"),
        "sukhapaṭipadā khippābhiññā": ("một cách không khó nhọc, không vất vả", "nhanh chóng")}


def pp_def(k):
    how, speed = _PDO[k]
    return (f"{q(pn(k))} {gen(f'người làm sinh khởi định tâm {how}, hiểu biết trực tiếp trạng thái ấy một cách {speed}')} "
            f"{DASH} {called(pn(k))}.")


hand("(9) Tattha katamā catasso paṭipadā?", "",
     f"(9) {q('bốn cách thực hành')} {cap(', '.join(pn(k) for k in _PP))}.")
hand("(Ka) tattha katamā dukkhapaṭipadā dandhābhiññā paññā?", "", f"(a) {low(pp_def(_PP[0]))}")
hand("(Kha) tattha katamā dukkhapaṭipadā khippābhiññā paññā?", "", f"(b) {low(pp_def(_PP[1]))}")
hand("(Ga) tattha katamā sukhapaṭipadā dandhābhiññā paññā?", "", f"(c) {low(pp_def(_PP[2]))}")
hand("(Gha) tattha katamā sukhapaṭipadā khippābhiññā paññā?", "Imā catasso paṭipadā.",
     f"(d) {low(pp_def(_PP[3]))} Đây là bốn cách thực hành.")
_AR = list(ARAM)
_ADO = {"parittā parittārammaṇā": ("không đạt được định tâm theo ý muốn", "nhỏ hẹp"),
        "parittā appamāṇārammaṇā": ("không đạt được định tâm theo ý muốn", "rộng rãi"),
        "appamāṇā parittārammaṇā": ("đạt được định tâm theo ý muốn", "nhỏ hẹp"),
        "appamāṇā appamāṇārammaṇā": ("đạt được định tâm theo ý muốn", "rộng rãi")}


def ar_def(k):
    a, b = _ADO[k]
    return f"{q(pn(k))} {gen(f'người {a}, lan tỏa đến đối tượng {b}')} {DASH} {called(pn(k))}."


hand("(10) Tattha katamāni cattāri ārammaṇāni?", "", f"(10) {q('bốn đối tượng')} {cap(', '.join(pn(k) for k in _AR))}.")
hand("(Ka) tattha katamā parittā parittārammaṇā paññā?", "", f"(a) {low(ar_def(_AR[0]))}")
hand("(Kha) tattha katamā parittā appamāṇārammaṇā paññā?", "", f"(b) {low(ar_def(_AR[1]))}")
hand("(Ga) tattha katamā appamāṇā parittārammaṇā paññā?", "", f"(c) {low(ar_def(_AR[2]))}")
hand("(Gha) tattha katamā appamāṇā appamāṇārammaṇā paññā?", "Imāni cattāri ārammaṇāni.",
     f"(d) {low(ar_def(_AR[3]))} Đây là bốn đối tượng.")
_JM = DA["jarāmaraṇa"]
hand("(11) Maggasamaṅgissa ñāṇaṃ jarāmaraṇepetaṃ ñāṇaṃ", "", f"(11) {cap(MAGGASAM)} thì {also(four(_JM))}.")
hand("(Ka) tattha katamaṃ jarāmaraṇe ñāṇaṃ?", "", f"(a) {low(q(kn(_JM)))} {ar(_JM)} {DASH} {called(kn(_JM))}.")
hand("(Kha-gha) jarāmaraṇasamudayaṃ ārabbha…pe…", "",
     f"(b-d) điều mà sinh khởi liên quan đến sự phát sinh của {_JM}… liên quan đến sự chấm dứt {_JM}… liên quan đến "
     f"cách thực hành dẫn đến sự chấm dứt {_JM} là {PANNA} {DASH} {called(four(_JM)[3])}.")
_SK = DA["saṅkhāra"]
hand("(12-21) Dhammasamaṅgissa ñāṇaṃ jātiyāpetaṃ ñāṇaṃ", "",
     f"(12-21) {cap(DHAMMASAM)} thì " + "… ".join(f"cũng là {kn(DA[k])}" for k in DA_ORDER) + "… "
     + also(four(_SK)) + ".")
hand("Tattha katamaṃ saṅkhāresu ñāṇaṃ?", "", f"{q(kn(_SK))} {ar(_SK)} {DASH} {called(kn(_SK))}.")
hand("Saṅkhārasamudayaṃ ārabbha…pe…", "Evaṃ catubbidhena ñāṇavatthu.",
     f"Điều mà sinh khởi liên quan đến sự phát sinh của {_SK}… liên quan đến sự chấm dứt {_SK}… liên quan đến cách "
     f"thực hành dẫn đến sự chấm dứt {_SK} là {PANNA} {DASH} {called(four(_SK)[3])}. {frame_close(4)}")
# --- pañcaka … navaka
FIVE_SAM = ["sự lan tỏa của sự hân hoan", "sự lan tỏa của hạnh phúc", "sự lan tỏa của tâm", "sự lan tỏa của ánh sáng",
            "dấu hiệu của sự xem xét lại"]                                  # [new; paccavekkhaṇā pi-1]
hand("(1) Tattha katamo pañcaṅgiko sammāsamādhi?", "Ayaṃ vuccati pañcaṅgiko sammāsamādhi.",
     f"(1) {q(SAMADHI5)} {cap(', '.join(FIVE_SAM))}. {cap(TRI)} trong hai tầng thiền là {FIVE_SAM[0]}. {cap(TRI)} trong "
     f"ba tầng thiền là {FIVE_SAM[1]}. {cap(NAMES['paracitte'])} là {FIVE_SAM[2]}. Thiên nhãn là {FIVE_SAM[3]}. "
     f"{cap(NAMES['paccavekkhaṇā'])} của người đã xuất khỏi định tâm này hay định tâm kia là {FIVE_SAM[4]}. "
     f"{cap(called(SAMADHI5, False))}.")
_KN5 = "Sự hiểu biết sinh khởi ngay nơi tự thân rằng"                     # paccattaññeva ñāṇaṃ uppajjati [new]
hand("(2) Tattha katamo pañcañāṇiko sammāsamādhi?", "Evaṃ pañcavidhena ñāṇavatthu.",
     f"(2) {q(SAMADHI5N)} {_KN5} “Định tâm này vừa là hạnh phúc trong hiện tại, vừa có quả là hạnh phúc trong tương "
     f"lai”. {_KN5} “Định tâm này là cao quý, không có tính trần tục”. {_KN5} “Định tâm này được những người không "
     f"hèn kém thực hành”. {_KN5} “Định tâm này an tịnh, ưu việt, đạt được nhờ sự lắng dịu hoàn toàn, đạt đến sự hợp "
     f"nhất của tâm, không phải đạt được nhờ sự kiềm chế và ngăn chặn có sự thúc đẩy”. {_KN5} “Còn tôi, tôi chứng nhập "
     f"định tâm này với sự tỉnh thức, tôi xuất khỏi với sự tỉnh thức”. Đây là {SAMADHI5N}. {frame_close(5)}")
hand("Tattha katamā chasu abhiññāsu paññā?", "Evaṃ chabbidhena ñāṇavatthu.",
     f"{q(TRI + ' trong ' + ABHINNA6)} " + cap(", ".join(NAMES[k] for k in (
         "iddhividhe", "sotadhātuvisuddhiyā", "paracitte", "pubbenivāsānussatiyā", "sattānaṃ cutūpapāte",
         "āsavānaṃ khaye"))) + f" {DASH} đây là {TRI} trong {ABHINNA6}. {frame_close(6)}")


def chain(a, b):
    return f"{DA[a]} làm điều kiện cho {DA[b]}"


def ninth(a, b, full):
    """the six knowledges of one link; full = the first / last link written out"""
    asati = f"khi không có {DA[a]} thì không có {DA[b]}"
    items = [f"sự hiểu biết rằng {chain(a, b)}", f"sự hiểu biết rằng {asati}",
             f"sự hiểu biết rằng cả trong thời quá khứ, {chain(a, b)}", f"sự hiểu biết rằng {asati}",
             f"sự hiểu biết rằng cả trong thời tương lai, {chain(a, b)}", f"sự hiểu biết rằng {asati}"]
    return ", ".join(items)


STHITI = ("sự hiểu biết rằng ngay cả sự hiểu biết về tính ổn định của các hiện tượng mà vị ấy có, điều đó cũng có bản "
          "chất phải diệt tận, có bản chất phải suy tàn, có bản chất phải phai nhạt, có bản chất phải chấm dứt")   # [new]
_CH = [("bhava", "jāti"), ("upādāna", "bhava"), ("taṇhā", "upādāna"), ("vedanā", "taṇhā"), ("phassa", "vedanā"),
       ("saḷāyatana", "phassa"), ("nāmarūpa", "saḷāyatana"), ("viññāṇa", "nāmarūpa"), ("saṅkhāra", "viññāṇa")]
hand("Tattha katamāni sattasattati ñāṇavatthūni?", "Evaṃ sattavidhena ñāṇavatthu.",
     f"{q(NV77)} {cap(ninth('jāti', 'jarāmaraṇa', True))}. {cap(STHITI)}; "
     + "… ".join(f"sự hiểu biết rằng {chain(a, b)}" for a, b in _CH) + "… "
     + f"{ninth('avijjā', 'saṅkhāra', True)}. {cap(STHITI)}. Đây là {NV77}. {frame_close(7)}")
_MP8 = [("con đường", "vào dòng"), ("thành quả", "vào dòng"), ("con đường", "trở lại một lần"),
        ("thành quả", "trở lại một lần"), ("con đường", "không trở lại"), ("thành quả", "không trở lại"),
        ("con đường", "A-la-hán"), ("thành quả", "A-la-hán")]              # [new; core sotāpanna «bậc vào dòng»]
hand("Tattha katamā catūsu maggesu catūsu phalesu paññā?", "Evaṃ aṭṭhavidhena ñāṇavatthu.",
     f"{q(TRI + ' ' + MP)} " + cap(", ".join(f"{TRI} trong {a} {b}" for a, b in _MP8))
     + f" {DASH} đây là {TRI} {MP}. {frame_close(8)}")
hand("Tattha katamā navasu anupubbavihārasamāpattīsu paññā?", "Evaṃ navavidhena ñāṇavatthu.",
     f"{q(TRI + ' trong ' + SAMAP9)} " + cap(", ".join(f"{TRI} trong {x}" for x in JH_SAMAP))
     + f", {NAMES['paccavekkhaṇā']} của người đã xuất khỏi {NIRODHA_SAMAP} {DASH} đây là {TRI} trong {SAMAP9}. "
     + frame_close(9))
# --- dasaka exposition
WHAT_T = f"{cap(TP)} {DASH} đây là "
hand("(1) Tattha katamaṃ tathāgatassa ṭhānañca ṭhānato", "",
     f"(1) {bala_q(BALA[0])} {P809}")
hand("Aṭṭhānametaṃ anavakāso yaṃ diṭṭhisampanno puggalo pitaraṃ", "", P809_2)
hand('"Aṭṭhānametaṃ anavakāso yaṃ ekissā lokadhātuyā dve arahanto', "", P809_3)
hand('"Aṭṭhānametaṃ anavakāso yaṃ itthī arahaṃ', "", P809_4)
hand('"Aṭṭhānametaṃ anavakāso yaṃ kāyaduccaritassa iṭṭho', "", P809_5)
hand('"Aṭṭhānametaṃ anavakāso yaṃ kāyasucaritassa aniṭṭho', "", P809_6)
hand('"Aṭṭhānametaṃ anavakāso yaṃ kāyaduccaritasamaṅgī', "", P809_7)
hand('"Aṭṭhānametaṃ anavakāso yaṃ kāyasucaritasamaṅgī', "", P809_8)
hand("(2) Tattha katamaṃ tathāgatassa atītānāgatapaccuppannānaṃ", "payogasampattipaṭibāḷhāni na vipaccanti.",
     f"(2) {bala_q(BALA[1])} {IDHA}, {NL} hiểu rõ {DASH} “{k810(True, True, True)}")
hand('"Atthekaccāni pāpakāni kammasamādānāni gativipattiṃ', "", f"“{k810(True, False, False)}")
hand('"Atthekaccāni kalyāṇāni kammasamādānāni gativipattipaṭibāḷhāni', "", f"“{k810(False, False, True)}")
_K4 = k810(False, True, False)
hand('"Atthekaccāni kalyāṇāni kammasamādānāni gatisampattiṃ', "",
     f"“{_K4[:-1]}”. {WHAT_T}{bala_name(BALA[1])}.")
hand("(3) Tattha katamaṃ tathāgatassa sabbatthagāminiṃ", "",
     f"(3) {bala_q(BALA[2])} {IDHA}, {NL} hiểu rõ rằng “Đây là con đường, đây là cách thực hành dẫn đến địa ngục” "
     f"[khác chính tả (Syā.): nirayagāminīti], hiểu rõ rằng “Đây là con đường, đây là cách thực hành dẫn đến loài súc "
     f"sinh” [dị bản (Syā.): tiracchānagāminīti; cũng vậy ở các chỗ sau. Nên tham khảo sách chú giải], hiểu rõ rằng “Đây "
     f"là con đường, đây là cách thực hành dẫn đến cõi ngạ quỷ”, hiểu rõ rằng “Đây là con đường, đây là cách thực hành "
     f"dẫn đến cõi người”, hiểu rõ rằng “Đây là con đường, đây là cách thực hành dẫn đến cõi trời”, hiểu rõ rằng “Đây "
     f"là con đường, đây là cách thực hành dẫn đến Niết-bàn”. {WHAT_T}{bala_name(BALA[2])}.")
hand("(4) Tattha katamaṃ tathāgatassa anekadhātunānādhātulokaṃ", "",
     f"(4) {bala_q(BALA[3])} {IDHA}, {NL} hiểu rõ sự khác nhau của các khối, hiểu rõ sự khác nhau của các lĩnh vực "
     f"nhận biết, hiểu rõ sự khác nhau của các yếu tố, hiểu rõ sự khác nhau của {BALA[3]}. {WHAT_T}{bala_name(BALA[3])}.")
hand("(5) Tattha katamaṃ tathāgatassa sattānaṃ nānādhimuttikataṃ", "",
     f"(5) {bala_q(BALA[4])} {IDHA}, {NL} hiểu rõ {DASH} “{EXIST} {SEV_PRES}")
hand('"Atītampi addhānaṃ hīnādhimuttikā', "", f"“{cap(SEV_PAST_C)}.")
hand('"Anāgatampi addhānaṃ hīnādhimuttikā', "", f"“{cap(SEV_FUT_C)}”. {WHAT_T}{bala_name(BALA[4])}.")
hand("(6) Tattha katamaṃ tathāgatassa parasattānaṃ", "",
     f"(6) {bala_q(BALA[5])} {IDHA}, {NL} hiểu rõ {ASAYA} của chúng sinh, hiểu rõ {ANUSAYA}, hiểu rõ {CARITA}, hiểu rõ "
     f"{ADHIMUTTI}, hiểu rõ những chúng sinh " + ", ".join(TYPES[k] for k in (
         "apparajakkha", "mahārajakkha", "tikkhindriya", "mudindriya", "svākāra", "dvākāra", "suviññāpaya",
         "duviññāpaya")) + f", {TYPES['bhabba']} và {TYPES['abhabba']}.")
hand("Katamo ca sattānaṃ āsayo?", "Ayaṃ sattānaṃ āsayo.",
     f"Và {ASAYA} của chúng sinh là gì? {VIEWS10}; như vậy, chúng sinh hoặc nương tựa vào quan điểm về sự hiện hữu, "
     f"hoặc nương tựa vào quan điểm về sự không còn hiện hữu. Hoặc, không đi đến hai cực đoan này, người ta đã đạt được "
     f"sự chấp nhận thuận theo đối với quy luật tùy thuộc vào điều kiện và các hiện tượng sinh khởi tùy thuộc vào điều "
     f"kiện, tức sự hiểu biết đúng như thật. Đây là {ASAYA} của chúng sinh.")
hand("Katamo ca sattānaṃ anusayo?", "Ayaṃ sattānaṃ anusayo.",
     f"Và {ANUSAYA} của chúng sinh là gì? Bảy {ANUSAYA} {DASH} "
     + T.listing([f"{ANUSAYA} {x}" for x in ANU7]) + ". Điều gì trong thế gian là điều đáng yêu, là điều khoan khoái, "
     f"thì ở đó, {ANUSAYA} tham đắm của chúng sinh nằm sẵn. Điều gì trong thế gian là điều không đáng yêu, là điều "
     f"không khoan khoái, thì ở đó, {ANUSAYA} ác cảm của chúng sinh nằm sẵn. Như vậy, trong hai hiện tượng này có "
     f"vô minh đi theo. Sự kiêu mạn, quan điểm và sự hoài nghi cùng hiện diện với nó cần được nhận biết. Đây là "
     f"{ANUSAYA} của chúng sinh.")
hand("Katamañca sattānaṃ caritaṃ?", "",
     f"Và {CARITA} của chúng sinh là gì? {cap(', '.join(ABHISANKH))}, thuộc cấp độ nhỏ hoặc thuộc cấp độ lớn {DASH} "
     f"đây là {CARITA} của chúng sinh.")
hand("Katamā ca sattānaṃ adhimutti?", "", f"Và {ADHIMUTTI} của chúng sinh là gì? {EXIST} {SEV_PRES}")
hand("Atītampi addhānaṃ hīnādhimuttikā sattā", "", f"{cap(SEV_PAST_S)}.")
hand("Anāgatampi addhānaṃ hīnādhimuttikā sattā", "Ayaṃ sattānaṃ adhimutti.",
     f"{cap(SEV_FUT_S)}. Đây là {ADHIMUTTI} của chúng sinh.")
hand("Katame te sattā mahārajakkhā?", "",
     f"{who('mahārajakkha')} {KILESA10}. Những chúng sinh nào mà mười chỗ dựa của phiền não này {DONE4}, thì đó là "
     f"{beings('mahārajakkha')}.")
hand("Katame te sattā apparajakkhā?", "",
     f"{who('apparajakkha')} Những chúng sinh nào mà mười chỗ dựa của phiền não này {NOT4}, thì đó là "
     f"{beings('apparajakkha')}.")
hand("Katame te sattā mudindriyā?", "",
     f"{who('mudindriya')} {IND5}. Những chúng sinh nào mà năm năng lực này {NOT4}, thì đó là {beings('mudindriya')}.")
hand("Katame te sattā tikkhindriyā?", "",
     f"{who('tikkhindriya')} Những chúng sinh nào mà năm năng lực này {DONE4}, thì đó là {beings('tikkhindriya')}.")
hand("Katame te sattā dvākārā?", "",
     f"{who('dvākāra')} Những chúng sinh nào có {ASAYA} xấu ác, có {ANUSAYA} xấu ác, có {CARITA} xấu ác, có {ADHIMUTTI} "
     f"xấu ác, {TYPES['mahārajakkha']}, {TYPES['mudindriya']}, thì đó là {beings('dvākāra')}.")
hand("Katame te sattā svākārā?", "",
     f"{who('svākāra')} Những chúng sinh nào có {ASAYA} tốt đẹp, có {CARITA} tốt đẹp, có {ADHIMUTTI} tốt đẹp, "
     f"{TYPES['apparajakkha']}, {TYPES['tikkhindriya']}, thì đó là {beings('svākāra')}.")
hand("Katame te sattā duviññāpayā?", "",
     f"{who('duviññāpaya')} Và những chúng sinh nào {TYPES['dvākāra']}, chính những chúng sinh ấy là "
     f"{beings('duviññāpaya')}. Và những chúng sinh nào {TYPES['svākāra']}, chính những chúng sinh ấy là "
     f"{beings('suviññāpaya')}.")
hand("Katame te sattā abhabbā?", "",
     f"{who('abhabba')} Những chúng sinh nào mang {AVARANA['kamma']}, mang {AVARANA['kilesa']}, mang "
     f"{AVARANA['vipāka']}, không có niềm tin, không có ý muốn, trí tuệ kém, {TYPES['abhabba']} {NIYAMA}, thì đó là "
     f"{beings('abhabba')}.")
hand("Katame te sattā bhabbā?", "",
     f"{who('bhabba')} Những chúng sinh nào không mang {AVARANA['kamma']}, không mang {AVARANA['kilesa']}, không mang "
     f"{AVARANA['vipāka']}, có niềm tin, có ý muốn, có trí tuệ, {TYPES['bhabba']} {NIYAMA}, thì đó là "
     f"{beings('bhabba')}. {WHAT_T}{bala_name(BALA[5])}.")
SAMP_VIP = {"sampatti": "sự thành công", "vipatti": "sự thất bại"}          # [new]
hand("(7) Tattha katamaṃ tathāgatassa jhānavimokkhasamādhisamāpattīnaṃ", "ime cattāro jhāyī.",
     f"(7) {bala_q(BALA7Q)} “{cap(JHAYI)}”. Bốn {JHAYI}. Có {JHAYI} cho rằng điều vốn là {SAMP_VIP['sampatti']} là "
     f"{SAMP_VIP['vipatti']} [khác chính tả (Ka.): sampattiyeva], có {JHAYI} cho rằng điều vốn là "
     f"{SAMP_VIP['vipatti']} [khác chính tả (Ka.): vipattiyeva] là {SAMP_VIP['sampatti']}, có {JHAYI} cho rằng điều vốn "
     f"là {SAMP_VIP['sampatti']} là {SAMP_VIP['sampatti']}, có {JHAYI} cho rằng điều vốn là {SAMP_VIP['vipatti']} là "
     f"{SAMP_VIP['vipatti']} {DASH} đây là bốn {JHAYI}.")
hand("Aparepi cattāro jhāyī. Atthekacco jhāyī dandhaṃ", "",
     f"Thêm bốn {JHAYI} khác. Có {JHAYI} chứng nhập chậm, xuất khỏi nhanh, có {JHAYI} chứng nhập nhanh, xuất khỏi chậm, "
     f"có {JHAYI} chứng nhập chậm, xuất khỏi chậm, có {JHAYI} chứng nhập nhanh, xuất khỏi nhanh {DASH} đây là bốn "
     f"{JHAYI}.")
_SK1, _SK2 = "khéo léo về định tâm trong định tâm", "khéo léo về sự chứng đạt trong định tâm"   # [new]
hand("Aparepi cattāro jhāyī. Atthekacco jhāyī samādhismiṃ", "",
     f"Thêm bốn {JHAYI} khác. Có {JHAYI} {_SK1}, nhưng không {_SK2}; có {JHAYI} {_SK2}, nhưng không {_SK1}; có "
     f"{JHAYI} vừa {_SK1}, vừa {_SK2}; có {JHAYI} không {_SK1}, cũng không {_SK2} {DASH} đây là bốn {JHAYI}.")
hand('"Jhāna"nti. Cattāri jhānāni', "", f"“Tầng thiền”. {JHANA4}.")
hand('"Vimokkho"ti. Aṭṭha vimokkhā.', "",
     f"“{cap(VIM)}”. Tám {VIM}. Có hình sắc, thấy những hình sắc {DASH} đây là {VIM} {ORD8[0]}.")
hand("Ajjhattaṃ arūpasaññī bahiddhā rūpāni passati", "",
     f"Không có tri giác về hình sắc ở nơi bản thân, thấy ở bên ngoài bản thân những hình sắc {DASH} đây là {VIM} "
     f"{ORD8[1]}.")
hand("Subhanteva adhimutto hoti", "", f"Quyết định rằng “đẹp” {DASH} đây là {VIM} {ORD8[2]}.")
hand("Sabbaso rūpasaññānaṃ samatikkamā", "",
     f"{cap(RUPA3)}, với ý nghĩ “{THOUGHT['ananto ākāso']}”, chứng nhập và an trú {AYAT['ākāsānañcāyatana']} {DASH} đây "
     f"là {VIM} {ORD8[3]}.")
hand("Sabbaso ākāsānañcāyatanaṃ samatikkamma", "",
     f"{cap(X.BEYOND['ākāsānañcāyatana'])}, với ý nghĩ “{THOUGHT['anantaṃ viññāṇa']}”, chứng nhập và an trú "
     f"{AYAT['viññāṇañcāyatana']} {DASH} đây là {VIM} {ORD8[4]}.")
hand("Sabbaso viññāṇañcāyatanaṃ samatikkamma", "",
     f"{cap(X.BEYOND['viññāṇañcāyatana'])}, với ý nghĩ “{THOUGHT['natthi kiñcī']}”, chứng nhập và an trú "
     f"{AYAT['ākiñcaññāyatana']} {DASH} đây là {VIM} {ORD8[5]}.")
hand("Sabbaso ākiñcaññāyatanaṃ samatikkamma", "",
     f"{cap(X.BEYOND['ākiñcaññāyatana'])}, chứng nhập và an trú {AYAT['nevasaññānāsaññāyatana']} {DASH} đây là {VIM} "
     f"{ORD8[6]}.")
hand("Sabbaso nevasaññānāsaññāyatanaṃ samatikkamma", "",
     f"{cap(X.BEYOND['nevasaññānāsaññāyatana'])}, chứng nhập và an trú sự chấm dứt tri giác và cảm giác {DASH} đây là "
     f"{VIM} {ORD8[7]}.")
hand('"Samādhī"ti. Tayo samādhī', "", f"“Định tâm”. {SAM3}.")
hand('"Samāpattī"ti. Nava anupubbavihārasamāpattiyo', "",
     f"“Sự chứng đạt”. {cap(SAMAP9)} {DASH} {SAMAP9_LIST}.")
hand('"Saṃkilesa"nti hānabhāgiyo dhammo.', "",
     f"“Sự vẩn đục”: hiện tượng thuộc về phía suy giảm. “Sự trong sạch”: hiện tượng thuộc về phía thăng tiến. “Sự xuất "
     f"khỏi”. Sự trong sạch cũng là sự xuất khỏi, sự xuất khỏi định tâm này hay định tâm kia cũng là sự xuất khỏi. "
     f"{WHAT_T}{bala_name(BALA[6])}.")
_LIVES = ", ".join(f"{n} đời" for n in ("một", "hai", "ba", "bốn", "năm", "mười", "hai mươi", "ba mươi", "bốn mươi",
                                         "năm mươi", "một trăm", "một nghìn", "một trăm nghìn"))
_KAPPA = ("nhiều kiếp thế giới tan hoại, nhiều kiếp thế giới hình thành, nhiều kiếp thế giới tan hoại và hình thành")
_SUCH = ("có tên như vậy, dòng họ như vậy, dung mạo như vậy, thức ăn như vậy, cảm nhận sự dễ chịu và sự khó chịu như "
         "vậy, tuổi thọ đến mức như vậy")
hand("(8) Tattha katamaṃ tathāgatassa pubbenivāsānussati", "",
     f"(8) {bala_q(PUBBE)} {IDHA}, {NL} nhớ lại nhiều đời sống trước theo nhiều cách, cụ thể là {DASH} {_LIVES}, "
     f"{_KAPPA}: “Ở nơi kia, tôi đã {_SUCH}; chết từ nơi ấy, tôi đã sinh ra ở nơi kia; ở nơi ấy, tôi cũng đã {_SUCH}; "
     f"chết từ nơi ấy, tôi đã tái sinh ở đây”. Như vậy, Ngài nhớ lại nhiều đời sống trước theo nhiều cách, với các nét "
     f"đặc trưng và các chi tiết. {WHAT_T}{bala_name(PUBBE)}.")
_EYE = "bằng thiên nhãn thanh tịnh, vượt quá mắt người"                     # dibbena cakkhunā … [new]
_SEE = ("thấy chúng sinh đang chết đi, đang tái sinh, thấp kém, ưu việt, đẹp đẽ, xấu xí, ở cõi tốt lành, ở cõi xấu, hiểu "
        "rõ chúng sinh đi theo nghiệp của mình")


def conduct(good):
    w = SUC if good else DUC
    rev = "không phỉ báng" if good else "phỉ báng"
    vw = "đúng đắn" if good else "sai lầm"
    return (f"có {w['kāya']}, có {w['vacī']}, có {w['mano']}, {rev} các bậc thánh, có quan điểm {vw}, thực hiện những "
            f"nghiệp do quan điểm {vw}")


hand("(9) Tattha katamaṃ tathāgatassa sattānaṃ cutūpapātaṃ", "",
     f"(9) {bala_q(CUTU)} {IDHA}, {NL}, {_EYE}, {_SEE} {DASH} “Quả thật, những chúng sinh đáng kính này "
     f"{conduct(False)}. {cap(DEATH)}, họ đã tái sinh vào {BAD3}. Hoặc những chúng sinh đáng kính này {conduct(True)}. "
     f"{cap(DEATH)}, họ đã tái sinh vào {GOOD}”. Như vậy, {_EYE}, Ngài {_SEE}. {WHAT_T}{bala_name(CUTU)}.")
hand("(10) Tattha katamaṃ tathāgatassa āsavānaṃ khayaṃ", "",
     f"(10) {bala_q(KHAYA)} {IDHA}, nhờ {KHAYA}, {NL} ngay trong đời này tự mình hiểu biết trực tiếp, chứng nghiệm, "
     f"chứng nhập và an trú sự giải thoát của tâm và sự giải thoát nhờ trí tuệ, không còn ô nhiễm. "
     f"{WHAT_T}{bala_name(KHAYA)}.")



# ================================================================ 9. translate
def translate(pali_lines):
    hand_q = list(HAND)
    out, in_matrix = [], True
    for pl in pali_lines:
        if not pl.strip():
            out.append("")
            continue
        m = S.ID.search(pl)
        t = S.ID.sub("", pl).rstrip()
        if t == "#### Mātikā":
            in_matrix = False
        vi = None
        if t in LABELS:
            vi = LABELS[t]
        elif hand_q and t.startswith(hand_q[0][0]) and (not hand_q[0][1] or t.endswith(hand_q[0][1])):
            vi = hand_q.pop(0)[2]
        if vi is None:
            if in_matrix or FRAME_RE.match(t):
                vi = matrix_line(t)
            elif is_duka(t):
                vi = duka_line(t)
            else:
                try:
                    vi = ek_expo(t)
                except KeyError:
                    raise KeyError("unmatched: " + t[:90] + " | next hand: " + (hand_q[0][0] if hand_q else ""))
        assert pl.count(DASH) + pl.count("—") == vi.count(DASH), ("dash count", t[:70], vi[:160])
        for bad in BAD:
            assert bad not in vi, (bad, vi[:200])
        assert not PALI_LETTERS.search(re.sub(r"\[[^\]]*\]", "", vi)), ("Pāli letters", vi[:200])
        out.append(vi + (" " + m.group(1) if m else ""))
    assert not hand_q, [h[0][:50] for h in hand_q]
    return out


BAD = ("là là", "  ", "….", '"', " ,", " .", ":-", "thì thì", "\x01", " ;", ";;", ",,", "chánh niệm", "..", ", ,",
       "None", "—", "pe…", "“ ", " ”", "( ", " )")
PALI_LETTERS = re.compile(r"[āīūṃṅñṭḍṇḷ]")
FIXES = [   # (Pāli as written, as meant): spelling / punctuation only (reported)
    ("atthi anuppādinnupādāniyā, atthi anuppādinnaanupādāniyā", "atthi anupādinnupādāniyā, atthi anupādinnaanupādāniyā"),
    ("Atthi ajjhatā,", "Atthi ajjhattā,"),
    ("pajānanā …pe…", "pajānanā…pe…"),
    ("vacīsucaritasamaṅgī …pe…", "vacīsucaritasamaṅgī…pe…"),
]


def build():
    pali = open(os.path.join(S.PALI_DIR, FN), encoding="utf-8").read().rstrip("\n").split("\n")
    fixed = []
    for line in pali:
        for a, b in FIXES:
            if a in line:
                SLIPS.append(f"{a!r} -> {b!r}")
                line = line.replace(a, b)
        fixed.append(line)
    # hand lines whose Pāli we did not parse word by word: the ch7 mind list must equal ours
    _p796 = [x for x in fixed if x.startswith("(Ga) tattha katamaṃ pariye ñāṇaṃ?")][0]
    assert ". " + cap(CITTA16_P)[:-1] + "īti – yā tattha" in _p796, "pariye list differs from ch7"
    for a, b in ((" atthi pītisahagatā, atthi sukhasahagatā", None),):
        pass
    return translate(fixed)


HAND_SLIPS = [
    "^2-751 the onefold matrix list has no '(1)'/'(2)' numbers (the numbering starts at (3)): kept as written",
    "^2-753 (51) 'Pītisahagatā paññā sukhasahagatā paññā atthi …' (comma missing between the two subjects): comma added",
    "^2-769 'dānādhigaccha' / 'sīlādhigaccha' (odd form; perhaps -adhigamma): rendered «nhờ sự bố thí / nhờ giới hạnh»",
    "^2-799 'lābhiṃ' (accusative where a genitive is expected): no effect in Vietnamese («Ở người đã đạt được …»)",
    "^2-803 (12-21) 'Dhammasamaṅgissa ñāṇaṃ' (the parallels (2), (11) have Maggasamaṅgissa): as written "
    "«hiểu biết của người có được Giáo Pháp»",
    "^2-803 closing quote missing after 'saṅkhāranirodhagāminiyā paṭipadāya ñāṇaṃ' (punctuation; added)",
    "^2-804 opening quote missing before 'So kho panāhaṃ' (punctuation; added)",
    "^2-809 line 2 opening quote missing before 'Aṭṭhānametaṃ' (punctuation; added)",
    "^2-809 'kañci dhammaṃ atthato upagaccheyya' (= attato, one-letter spelling slip): rendered as meant «là tự ngã»",
    "^2-815 closing quote missing after '\"hoti tathāgato paraṃ maraṇā' (punctuation; added)",
    "^2-824 the svākārā list has no 'kalyāṇānusayā' item (dvākārā has pāpānusayā): as written",
    "^2-828 the question omits 'vuṭṭhānaṃ' (the answer and the matrix have it): as written",
    "^2-829 'pubbenivāsānussati' (stem form) in the question and the answer: no effect",
    "^2-828 '[sampattiyeva (ka.)]' identical to the text word: variant kept as written",
    "closing 'ti' dropped: ^2-796 'pajānātīti', ^2-811 'pajānātīti', ^2-812 'pajānātīti', ^2-827 'bhabbāti', "
    "^2-829 'anussaratīti', ^2-830 'pajānātīti', ^2-831 'viharatīti', 'ñāṇanti'",
]


def main():
    lines = build()
    dry = "--dry" in sys.argv
    path = os.path.join(S.VI_DIR, FN)
    if not dry:
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write("\n".join(lines).rstrip("\n") + "\n")
    print("OK:" if not dry else "DRY:", path, "|", len([x for x in lines if x.strip()]), "non-empty lines")
    for s in sorted(set(SLIPS + HAND_SLIPS)):
        print("slip:", s)


if __name__ == "__main__":
    main()
