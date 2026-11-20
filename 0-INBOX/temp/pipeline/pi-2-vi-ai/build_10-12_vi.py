# -*- coding: utf-8 -*-
"""pi-2 Vibhaṅga, Vietnamese plain zero-shot: chapters 10 (Bojjhaṅga), 11 (Maggaṅga), 12 (Jhāna).

usage: python -I -X utf8 build_10-12_vi.py
Writes AI_translation\\vietnamese\\pi-2-vietnamese-plain-zeroshot_split_chapters\\10-bojjhangavibhango.md,
11-maggangavibhango.md and 12-jhanavibhango.md (only when run as a script; importing writes nothing).

Imports build_ch1_sample_vi (S), build_1_vi (B), build_2-3_vi (T), build_4-5_vi (F), build_6_vi (G) and
build_7-9_vi (H) and reuses their strings (nothing of theirs is rewritten; T's item tables are extended in memory
only). pi-1 strings (awakening-factor names, path-factor definitions ^1-297 … ^1-304, the jhāna formulas, the
rūpāvacara / arūpāvacara / lokuttara / kiriya openings and their result clauses, the definitions of pīti, passaddhi,
sati, paññā, vitakka, vicāra, saññā, the hindrances, ākāsa, sense restraint and moderation in food) are copied from
the reviewed pi-1 Vietnamese rails and asserted; composed jhāna openings are checked against every pi-1 opening the
composer can parse. The ch. 11 Suttanta definitions with the ch. 4 Pāli take the ch. 4 strings (asserted).
Unknown Pāli raises KeyError (nothing is guessed).
"""
import importlib
import os
import re
import sys

HERE = r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-vi-ai"
sys.path.insert(0, HERE)
import build_ch1_sample_vi as S  # noqa: E402
import build_1_vi as B  # noqa: E402
T = importlib.import_module("build_2-3_vi")
F = importlib.import_module("build_4-5_vi")
G = importlib.import_module("build_6_vi")
H = importlib.import_module("build_7-9_vi")

DASH = S.DASH
cap, low = S.cap, S.low
pi1, between, repl = T.pi1, T.between, T.repl
called = T.called
in_pi1 = G.in_pi1
TATTHA = S.TATTHA                                   # Ở đây,
IDHA, BHIKKHU = F.IDHA, F.BHIKKHU                   # Ở đời này / vị tỳ-khưu [pi-1]
WHAT = G.WHAT                                       # Điều mà là
TENA = cap(G.TENA)                                  # Vì thế nên mới nói rằng [ch6]
SLIPS = []
PI1_PALI_DIR = os.path.join(S.ROOT, r"AI_translation\pali\pi-1_split_chapters")
_PI1P = {}


def pi1_pali(bid):
    """pi-1 Pāli line by block ID (variant brackets removed)."""
    if not _PI1P:
        for fn in sorted(os.listdir(PI1_PALI_DIR)):
            if fn.endswith(".md"):
                for line in open(os.path.join(PI1_PALI_DIR, fn), encoding="utf-8").read().split("\n"):
                    m = S.ID.search(line)
                    if m:
                        _PI1P[m.group(1)[1:]] = re.sub(r" \[[^\]]*\]", "", S.ID.sub("", line))
    return _PI1P[bid]


def qq(name):
    """question with the name in “…” (names that contain «là», as ch4 «Ở đây, “…” là gì?»)"""
    return f"{TATTHA} “{name}” là gì?"


def q(name):
    return f"{TATTHA} {name} là gì?"


# ================================================================ 1. names
BJ = {k: "chi phần giác ngộ là " + v for k, v in H.BOJJH.items()}          # [pi-1; upekkhā by pattern, ch7]
BJ_P = {k + "sambojjhaṅgo": k for k in H.BOJJH}
BJ_ORDER = list(H.BOJJH)
SATTA_BJ = "bảy chi phần giác ngộ"                                         # satta bojjhaṅgā [new; pi-1 words]
FN = F.FNAME                                                               # path factors [pi-1 ^1-297 … ^1-304]
PATH_ORDER = list(FN)
MAGGA8, MAGGA5 = F.MAGGA8, F.MAGGA5                                        # [pi-1]
ARIYA8 = "con đường cao quý gồm tám chi phần"                             # [ch4]
ORD = {"paṭhamaṃ": "thứ nhất", "dutiyaṃ": "thứ hai", "tatiyaṃ": "thứ ba", "catutthaṃ": "thứ tư",
       "pañcamaṃ": "thứ năm"}                                              # [pi-1]
JH = {k: "tầng thiền " + v for k, v in ORD.items()}                        # paṭhamaṃ jhānaṃ … [pi-1]
for _v in JH.values():
    in_pi1("chứng nhập và an trú " + _v)
NANGA = {"pañc": "năm", "catur": "bốn", "tiv": "ba", "duv": "hai"}         # Xaṅgikaṃ jhānaṃ = tầng thiền gồm X chi phần
for _v in NANGA.values():
    in_pi1(f"tầng thiền gồm {_v} chi phần")
JF = {"vitakko": "sự hướng tâm", "vicāro": "sự duy trì tâm", "pīti": "sự hân hoan", "sukhaṃ": "hạnh phúc",
      "cittassekaggatā": "sự nhất tâm", "upekkhā": "sự bình thản"}         # jhāna factors [pi-1 ^1-83]
assert cap(", ".join(JF[k] for k in ("vitakko", "vicāro", "pīti", "sukhaṃ", "cittassekaggatā"))) in pi1("1-83")
NAME = {}   # Pāli name (questions / answers) -> (Vietnamese, quote in questions)
for _k, _v in BJ.items():
    NAME[_k + "sambojjhaṅgo"] = (_v, True)
for _k, _v in FN.items():
    NAME[_k] = (_v, False)
NAME.update({"satta bojjhaṅgā": (SATTA_BJ, False), "aṭṭhaṅgiko maggo": (MAGGA8, False),
             "pañcaṅgiko maggo": (MAGGA5, False)})
for _k, _v in JH.items():
    NAME[_k + " jhānaṃ"] = (_v, False)
NAME["vīriyasambojjhaṅgaṃ [viriyasambojjhaṅgaṃ (sī. syā.)]"] = (BJ["vīriya"], True)


def question(p):
    vi, quote = NAME[p]
    return qq(vi) if quote else q(vi)


def answer_called(p, quoted):
    return called(NAME[p][0], quoted)


# ================================================================ 2. pi-1 bodies
UPEKKHA4 = "sự bình thản, sự giữ bình thản, sự bình thản trọn vẹn, sự cân bằng của tâm"   # [new; upekkhā pi-1]
PITI = between(pi1("1-9"), "Điều mà vào lúc ấy là ", f" {DASH} đó là")                     # [pi-1 ^1-9]
assert between(pi1("1-285"), "Điều mà vào lúc ấy là ", f" {DASH} đó là") == PITI + ", " + BJ["pīti"]
PITI_BJ_VAR = repl(PITI, "sự phấn chấn,", "sự phấn chấn [khác chính tả (Sī.): odaggaṃ; dha. sa. 9],") + ", " + BJ["pīti"]
_PAS = between(pi1("1-40"), "Điều mà vào lúc ấy là ", f" {DASH} đó là")
for _a in (" [khác chính tả (Sī., Syā.): paṭippassaddhi]", " [khác chính tả (Sī., Syā.): paṭippassambhanā]",
           " [khác chính tả (Sī., Syā.): paṭippassambhitattaṃ]"):
    _PAS = repl(_PAS, _a, "")
PASSADDHI_BJ = repl(_PAS, "khối tri giác và khối tạo tác", "khối tri giác, khối tạo tác và khối thức") + ", " + BJ["passaddhi"]
SATI_FULL = F.SATI                                                         # [pi-1 ^1-14]
SATI_PE = H.SATI_PE                                                        # sati anussati…pe… sammāsati
SATI_PE3 = F.pe_cut(F.SATI, 3, "tỉnh thức đúng đắn")                       # sati anussati paṭissati…pe… sammāsati
PANNA_FULL = between(pi1("1-16"), "Điều mà vào lúc ấy là ", f" {DASH} đó là")   # [pi-1 ^1-16]
PANNA_PE = F.PANNA                                                         # paññā pajānanā…pe… … sammādiṭṭhi
VITAKKA7 = T.VITAKKA7                                                      # [pi-1 ^1-7]
VITAKKA_PE = F.pe_cut(VITAKKA7, 2, "tư duy đúng đắn")
VICARA = between(pi1("1-8"), "Điều mà vào lúc ấy là ", f" {DASH} đó là")   # [pi-1 ^1-8]
VICARA_ANU = repl(VICARA, "sự chuyển động của tâm, ", "sự chuyển động của tâm, sự chuyển động tiếp nối, ")   # anucāro (as written)
SANNA3 = between(pi1("1-61"), "Điều mà vào lúc ấy là ", f" {DASH} đó là")   # saññā sañjānanā sañjānitattaṃ [pi-1]
assert SANNA3 == "tri giác, sự nhận ra, trạng thái đã nhận ra", SANNA3
SAMADHI_PE1 = F.pe_cut(F.SAMADHI, 1, "định tâm đúng đắn")                  # cittassa ṭhiti…pe… sammāsamādhi [pi-1 ^1-1367]
assert WHAT + SAMADHI_PE1 in pi1("1-1367")
VIRIYA_PE = H.VIRIYA_PE                                                    # [pi-1 ^1-1366]
assert WHAT + VIRIYA_PE in pi1("1-1366")
SADDHA4 = G.SADDHA4
CITTA_PE = H.CITTA_PE                                                      # cittaṃ mano mānasaṃ…pe… tajjāmanoviññāṇadhātu
RAGA_PE = F.pe_cut(G.RAGA, 2, "sự say đắm của tâm")                       # rāgo sārāgo…pe… cittassa sārāgo
DOSA_FULL = between(pi1("1-1160"), "Điều mà thuộc loại như vậy là ", f" {DASH} đó được gọi là")   # [pi-1 ^1-1160]
DOSA_VAR = repl(DOSA_FULL, "trạng thái khởi sân,", "trạng thái khởi sân [khác chính tả (Syā.): dūsanā dūsitattaṃ],")
DOSA_PE = f"{G.DOSA_HEAD}… {G.DOSA_TAIL}"                                  # cittassa āghāto…pe… anattamanatā cittassa
THINA = between(pi1("1-1162"), "Điều mà là ", f" {DASH} đó được gọi là")   # [pi-1 ^1-1162; pi-2 akalyatā]
THINA_VAR = repl(THINA, "trạng thái khởi uể oải của tâm",
                 "trạng thái khởi uể oải [khác chính tả (Sī., Syā.): thīyanā thīyitattaṃ] của tâm")
MIDDHA = between(pi1("1-1163"), "Điều mà là ", f" {DASH} đó được gọi là")  # [pi-1 ^1-1163; pi-2 suppaṃ … suppitattaṃ]
UDDHACCA = between(pi1("1-1165"), "Điều mà là ", f" {DASH} đó được gọi là")   # [pi-1 ^1-1165]
assert UDDHACCA == G.UDDH
_K = pi1("1-1166")
KUKKUCCA_A = between(_K, "là gì? ", ". Điều mà")                           # Akappiye kappiyasaññitā … [pi-1 ^1-1166]
KUKKUCCA_B = between(_K, "Điều mà thuộc loại như vậy là ", f" {DASH} đó được gọi là")
VICI = G.VICI                                                              # [pi-1 2-04]
_vi = VICI.split(", ")
VICI_SHORT = ", ".join(_vi[:3] + _vi[-2:])                                  # kaṅkhā … kaṅkhāyitattaṃ chambhitattaṃ … manovilekho
AKASA = between(pi1("1-637"), "? ", f" {DASH} vật chất này")               # [pi-1 ^1-637]
FEEL = G.FEEL                                                              # [pi-1 ^1-3, ^1-152, ^1-415, ^1-445, ^1-558]
CITTA_CETASIKA = "tâm và các yếu tố đồng hành với tâm"                     # cittacetasikā dhammā [pi-1 ^1-1029]
in_pi1(cap(CITTA_CETASIKA))
EXCEPT_IN = "sinh khởi trong đó"                                           # etthuppannaṃ X ṭhapetvā [pi-1 ^1-1387 …]
in_pi1("ngoại trừ cảm giác dễ chịu sinh khởi trong đó", "ngoại trừ sự hướng tâm và sự duy trì tâm sinh khởi trong đó")
for _bid, _key in (("1-298", "takko vitakko saṅkappo appanā byappanā cetaso abhiniropanā sammāsaṅkappo maggaṅgaṃ "
                             "maggapariyāpannaṃ"),
                   ("1-299", "catūhi vacīduccaritehi ārati virati paṭivirati veramaṇī akiriyā akaraṇaṃ anajjhāpatti "
                             "velāanatikkamo setughāto sammāvācā maggaṅgaṃ maggapariyāpannaṃ"),
                   ("1-300", "tīhi kāyaduccaritehi ārati virati paṭivirati veramaṇī akiriyā akaraṇaṃ anajjhāpatti "
                             "velāanatikkamo setughāto sammākammanto maggaṅgaṃ maggapariyāpannaṃ"),
                   ("1-301", "micchāājīvā ārati virati paṭivirati veramaṇī akiriyā akaraṇaṃ anajjhāpatti "
                             "velāanatikkamo setughāto sammāājīvo maggaṅgaṃ maggapariyāpannaṃ"),
                   ("1-304", "cittassa ṭhiti saṇṭhiti avaṭṭhiti avisāhāro avikkhepo avisāhaṭamānasatā samatho "
                             "samādhindriyaṃ samādhibalaṃ sammāsamādhi samādhisambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ")):
    assert "tasmiṃ samaye " + _key + " " + DASH in pi1_pali(_bid), _bid

AB = F.ABHI_BODY
BODY = {   # definition body (after Yo / Yā / Yaṃ or after "yo / yā tasmiṃ samaye") -> Vietnamese (after «Điều mà là»)
    "sati anussati…pe… sammāsati satisambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ":
        AB["Yā sati anussati…pe… sammāsati satisambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ"],
    "sati anussati sammāsati satisambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ": H.SATI_LOK,
    "paññā pajānanā…pe… amoho dhammavicayo sammādiṭṭhi dhammavicayasambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ":
        AB["Yā paññā pajānanā…pe… amoho dhammavicayo sammādiṭṭhi dhammavicayasambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ"],
    "cetasiko vīriyārambho…pe… sammāvāyāmo vīriyasambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ":
        AB["Yo cetasiko vīriyārambho…pe… sammāvāyāmo vīriyasambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ"],
    ("pīti pāmojjaṃ āmodanā pamodanā hāso pahāso vitti odagyaṃ [odaggaṃ (sī.) dha. sa. 9] attamanatā cittassa "
     "pītisambojjhaṅgo"): PITI_BJ_VAR,
    ("vedanākkhandhassa saññākkhandhassa saṅkhārakkhandhassa viññāṇakkhandhassa passaddhi paṭippassaddhi passambhanā "
     "paṭippassambhanā paṭippassambhitattaṃ passaddhisambojjhaṅgo"): PASSADDHI_BJ,
    "cittassa ṭhiti…pe… sammāsamādhi samādhisambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ":
        AB["Yā cittassa ṭhiti…pe… sammāsamādhi samādhisambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ"],
    "upekkhā upekkhanā ajjhupekkhanā majjhattatā cittassa upekkhāsambojjhaṅgo": UPEKKHA4 + ", " + BJ["upekkhā"],
    "takko vitakko saṅkappo appanā byappanā cetaso abhiniropanā sammāsaṅkappo maggaṅgaṃ maggapariyāpannaṃ": F._SS,
    "takko vitakko…pe… sammāsaṅkappo maggaṅgaṃ maggapariyāpannaṃ":
        AB["Yo takko vitakko…pe… sammāsaṅkappo maggaṅgaṃ maggapariyāpannaṃ"],
    ("catūhi vacīduccaritehi ārati virati paṭivirati veramaṇī akiriyā akaraṇaṃ anajjhāpatti velāanatikkamo setughāto "
     "sammāvācā maggaṅgaṃ maggapariyāpannaṃ"): F._SV,
    ("tīhi kāyaduccaritehi ārati virati paṭivirati veramaṇī akiriyā akaraṇaṃ anajjhāpatti velāanatikkamo setughāto "
     "sammākammanto maggaṅgaṃ maggapariyāpannaṃ"): F._SK,
    ("micchāājīvā ārati virati paṭivirati veramaṇī akiriyā akaraṇaṃ anajjhāpatti velāanatikkamo setughāto "
     "sammāājīvo maggaṅgaṃ maggapariyāpannaṃ"): F._SA,
    ("cittassa ṭhiti saṇṭhiti avaṭṭhiti avisāhāro avikkhepo avisāhaṭamānasatā samatho samādhindriyaṃ samādhibalaṃ "
     "sammāsamādhi samādhisambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ"): F._SM,
}
assert F._SM.endswith(BJ["samādhi"] + ", chi phần của con đường, nằm trong con đường")

# ================================================================ 3. jhāna openings (composer checked against pi-1)
PI1_OPEN, PI1_TAS = G.PI1_OPEN, G.PI1_TASSEVA
MOT = "một người "
_r1 = PI1_OPEN["rūpūpapattiyā maggaṃ bhāveti vivicceva kāmehi…pe… paṭhamaṃ jhānaṃ upasampajja viharati pathavīkasiṇaṃ"]
_l1 = PI1_OPEN[H.LOKP]
_k1 = PI1_OPEN["rūpāvacaraṃ jhānaṃ bhāveti kiriyaṃ neva kusalaṃ nākusalaṃ na ca kammavipākaṃ diṭṭhadhammasukhavihāraṃ "
               "vivicceva kāmehi…pe… paṭhamaṃ jhānaṃ upasampajja viharati pathavīkasiṇaṃ"]
START_VI = {"vivicceva kāmehi": "hoàn toàn tách khỏi các dục lạc",
            "vitakkavicārānaṃ vūpasamā": "nhờ sự hướng tâm và sự duy trì tâm lắng xuống",
            "pītiyā ca virāgā": "nhờ sự hân hoan phai nhạt",
            "sukhassa ca pahānā": "nhờ dứt bỏ sự dễ chịu"}                     # [pi-1 openings]
PREFIX = {   # Pāli opening prefix -> Vietnamese (after «Vào lúc »), from the pi-1 first-jhāna openings
    "rūpūpapattiyā maggaṃ bhāveti ": _r1[:_r1.index(START_VI["vivicceva kāmehi"])],
    "lokuttaraṃ jhānaṃ bhāveti niyyānikaṃ apacayagāmiṃ diṭṭhigatānaṃ pahānāya paṭhamāya bhūmiyā pattiyā ":
        _l1[:_l1.index(START_VI["vivicceva kāmehi"])],
    "rūpāvacaraṃ jhānaṃ bhāveti kiriyaṃ neva kusalaṃ nākusalaṃ na ca kammavipākaṃ diṭṭhadhammasukhavihāraṃ ":
        _k1[:_k1.index(START_VI["vivicceva kāmehi"])],
}
SUFFIX = {" pathavīkasiṇaṃ": ", " + G.EARTH,
          " dukkhapaṭipadaṃ dandhābhiññaṃ": ", với cách thực hành khó khăn và sự hiểu biết trực tiếp chậm chạp",
          " dukkhapaṭipadaṃ dandhābhiññaṃ suññataṃ": ", với cách thực hành khó khăn và sự hiểu biết trực tiếp chậm chạp"
                                                     + G.SUNNA}
FULL_BODY = {   # bodies without …pe… not in the pi-1 openings
    ("vivicceva kāmehi vivicca akusalehi dhammehi avitakkaṃ vicāramattaṃ vivekajaṃ pītisukhaṃ dutiyaṃ jhānaṃ "
     "upasampajja viharati"):
        "hoàn toàn tách khỏi các dục lạc, tách khỏi các hiện tượng bất thiện, chứng nhập và an trú tầng thiền thứ hai, "
        "không có sự hướng tâm, chỉ có sự duy trì tâm, có sự hân hoan và hạnh phúc sinh từ sự tách biệt",   # [pi-1 pieces]
}
in_pi1("chứng nhập và an trú tầng thiền thứ hai, không có sự hướng tâm, chỉ có sự duy trì tâm",
       "có sự hân hoan và hạnh phúc sinh từ sự tách biệt")
JBODY = re.compile(r"^(vivicceva kāmehi|vitakkavicārānaṃ vūpasamā|pītiyā ca virāgā|sukhassa ca pahānā)…pe… "
                   r"((?:\w+ jhānaṃ…pe… )*)(\w+) jhānaṃ upasampajja viharati$")


def jbody(b):
    if b in FULL_BODY:
        return FULL_BODY[b]
    m = JBODY.match(b)
    if not m:
        raise KeyError("jhāna body: " + b[:80])
    mids = [ORD[x.split(" ")[0]] for x in m.group(2).split("…pe… ") if x]
    out = START_VI[m.group(1)] + "… " + "".join(f"tầng thiền {x}… " for x in mids)
    return out + "chứng nhập và an trú " + JH[m.group(3)]


def split_suffix(p):
    for suf in sorted(SUFFIX, key=len, reverse=True):
        if p.endswith(suf):
            return p[:-len(suf)], SUFFIX[suf]
    return p, ""


def jopen(p):
    """opening after "yasmiṃ samaye" -> Vietnamese after «Vào lúc » (pi-1 when identical)."""
    if p in PI1_OPEN:
        return PI1_OPEN[p]
    for pre, pre_vi in PREFIX.items():
        if p.startswith(pre):
            body, suf = split_suffix(p[len(pre):])
            return pre_vi + jbody(body) + suf
    raise KeyError("opening: " + p[:80])


RESULT = {"rūpāvacarassa kusalassa kammassa katattā upacitattā vipākaṃ ":
          "là quả của chính nghiệp thiện thuộc cõi hình sắc ấy đã được tạo và tích lũy",
          "lokuttarassa kusalassa jhānassa katattā bhāvitattā vipākaṃ ":
          "là quả của chính tầng thiền thiện vượt thế gian ấy đã được tạo và tu tập"}   # [pi-1 ^1-499, ^1-505]
for _v in RESULT.values():
    in_pi1(_v)


def jtas(p):
    """result clause after "Tasseva" -> «Còn khi một người …, là quả của …» (pi-1 when identical)."""
    if p in PI1_TAS or p + " suññataṃ" in PI1_TAS:
        return G.tasseva(p)
    for pre, res in RESULT.items():
        if p.startswith(pre):
            body, suf = split_suffix(p[len(pre):])
            return f"Còn khi {MOT}{jbody(body)}{suf}, {res}"
    raise KeyError("Tasseva: " + p[:80])


def check_openings():
    """the composer reproduces every pi-1 opening / result clause it can parse."""
    n = 0
    for table, fn, pres in ((PI1_OPEN, jopen, PREFIX), (PI1_TAS, jtas, RESULT)):
        for p, v in table.items():
            for pre in pres:
                if p.startswith(pre):
                    body, suf = split_suffix(p[len(pre):])
                    if body in FULL_BODY or JBODY.match(body):
                        if (suf or not p.endswith("aṃ")) and "[" not in p:
                            c = (PREFIX[pre] + jbody(body) + suf) if pres is PREFIX else \
                                f"Còn khi {MOT}{jbody(body)}{suf}, {RESULT[pre]}"
                            assert c == v, (p[:90], c[:150], v[:150])
                            n += 1
    assert n >= 8, n
    return n


# ================================================================ 4. Abhidhammabhājanīya sentences
CONTACT = F.CONTACT_TO                                  # sự tiếp xúc… có sự không tán loạn [pi-1]
YAM = H.YAM_SAMAYE                                      # thì điều mà vào lúc ấy là
JF_LIST = re.compile(r"^(pañc|catur|tiv|duv)aṅgikaṃ jhānaṃ hoti( –)? (.+)$")


def factors(s):
    """'vitakko, vicāro, …' (or without commas, ^2-629) -> «sự hướng tâm, …»"""
    parts = s.split(", ") if ", " in s else re.findall(r"cittassekaggatā|\w+", s)
    if ", " not in s:
        SLIPS.append("commas missing: " + s)
    return ", ".join(JF[x] for x in parts)


def tasmim_tail(r):
    """the text after ", tasmiṃ samaye " -> «thì vào lúc ấy …»"""
    if r == "phasso hoti…pe… avikkhepo hoti":
        return f"thì vào lúc ấy có {CONTACT}"
    m = re.match(r"^satta bojjhaṅgā honti – (\w+)…pe… (\w+)$", r)
    if m:
        return f"thì vào lúc ấy có {SATTA_BJ} {DASH} {BJ[BJ_P[m.group(1)]]}… {BJ[BJ_P[m.group(2)]]}"
    if r + "." in F.PATH_TAIL:
        return "thì vào lúc ấy có " + F.PATH_TAIL[r + "."][:-1]
    m = JF_LIST.match(r)
    if m:
        sep = f" {DASH} " if m.group(2) else ": "
        if not m.group(2):
            SLIPS.append("dash missing: " + r[:40])
        return f"thì vào lúc ấy có tầng thiền gồm {NANGA[m.group(1)]} chi phần{sep}{factors(m.group(3))}"
    raise KeyError("tasmiṃ samaye: " + r[:80])


ANS = re.compile(r'^(.+) – (?:ayaṃ|idaṃ) vuccati ("?)([^"]+)("?)$')


def ya_tail(r):
    """'<body> – ayaṃ vuccati "X"' after "yā tasmiṃ samaye" -> «thì điều mà vào lúc ấy là … – đó được gọi là “X”»"""
    m = ANS.match(r)
    if not m:
        raise KeyError("yā tail: " + r[:80])
    body, q1, name, q2 = m.groups()
    assert q1 == q2
    return f"{YAM} {BODY[body]} {DASH} {answer_called(name, bool(q1))}"


YO_PHASSA = "phasso hoti…pe… avikkhepo hoti – ime dhammā kusalā"
YO_PHASSA_VI = f"thì những gì có vào lúc ấy, sự tiếp xúc… sự không tán loạn {DASH} những hiện tượng này là thiện"   # [new]
OPEN_RE = re.compile(r"^Idha bhikkhu yasmiṃ samaye (.+?), (tasmiṃ|yā tasmiṃ|yo tasmiṃ) samaye (.+)\.$")
TAS_RE = re.compile(r"^Tasseva (.+?), (tasmiṃ|yā tasmiṃ) samaye (.+)\.$")
AVA = {"sattahi bojjhaṅgehi": SATTA_BJ, "aṭṭhaṅgikena maggena": MAGGA8, "pañcaṅgikena maggena": MAGGA5,
       "sammādiṭṭhiyā": FN["sammādiṭṭhi"], "sammāsaṅkappena": FN["sammāsaṅkappo"], "sammāvāyāmena": FN["sammāvāyāmo"],
       "sammāsatiyā": FN["sammāsati"], "sammāsamādhinā": FN["sammāsamādhi"]}
for _k in BJ_ORDER:
    AVA[_k + "sambojjhaṅga"] = BJ[_k]
AVA["jhāna"] = "tầng thiền"                                                 # jhānasampayuttā [new]
SENT = {
    "Ime dhammā kusalā.": "Những hiện tượng này là thiện.",                 # [pi-1]
}


def avasesa(s):
    """'Avasesā dhammā X sampayuttā(…pe… avasesā dhammā Y sampayuttā)…' -> «Các hiện tượng còn lại gắn liền với X…»"""
    out = []
    for piece in re.split(r"…pe… ", s):
        m = re.match(r"^[Aa]vasesā dhammā (.+?) ?sampayuttā$", piece)
        if not m:
            raise KeyError("avasesā: " + piece)
        out.append(f"các hiện tượng còn lại gắn liền với {AVA[m.group(1)]}")
    return cap("… ".join(out))


def sentence(s):
    if s in SENT:
        return SENT[s]
    m = re.match(r"^Tattha katam(?:o|ā|aṃ|e) (.+)\?$", s)
    if m:
        return question(m.group(1))
    m = OPEN_RE.match(s)
    if m:
        op, kind, r = m.groups()
        head = f"{IDHA}, vào lúc {BHIKKHU} {jopen(op)[len(MOT):]}, "
        assert jopen(op).startswith(MOT)
        if kind == "tasmiṃ":
            return head + tasmim_tail(r) + "."
        if kind == "yā tasmiṃ":
            return head + ya_tail(r) + "."
        assert r == YO_PHASSA, r
        return head + YO_PHASSA_VI + "."
    m = TAS_RE.match(s)
    if m:
        op, kind, r = m.groups()
        return jtas(op) + ", " + (tasmim_tail(r) if kind == "tasmiṃ" else ya_tail(r)) + "."
    m = re.match(r"^(?:Yo|Yā|Yaṃ) (.+?)(…pe…)?\.$", s)
    if m:
        return WHAT + ya_tail(m.group(1))[len(YAM) + 1:] + ("…" if m.group(2) else ".")
    m = re.match(r'^(?:Ayaṃ|Idaṃ) vuccati ("?)([^"]+)("?)\.$|^Ime vuccanti ("?)([^"]+)("?)\.$', s)
    if m:
        name = m.group(2) or m.group(5)
        return cap(answer_called(name, bool(m.group(1) or m.group(4)))) + "."
    if s.startswith("Avasesā dhammā"):
        tail = ""
        if s.endswith("…pe…."):
            s, tail = s[:-len("…pe….")] + ".", "…"
        if s.endswith("ti."):                                               # ^2-637 "jhānasampayuttāti." (closing ti)
            SLIPS.append("closing ti: " + s[-30:])
            s = s[:-3] + "."
        return avasesa(s[:-1]) + (tail or ".")
    raise KeyError("sentence: " + s[:120])


FIXES = [   # (Pāli as written, as meant): punctuation / spelling only (reported)
    ("ākiñcāyatanaṃ upasampajja", "ākiñcaññāyatanaṃ upasampajja"),          # ^2-508 spelling
]
NOSPACE = H.NOSPACE_PE
SPLIT = H.SPLIT


def abhi_line(t):
    for a, b in FIXES:
        if a in t:
            SLIPS.append(f"{a!r} -> {b!r}")
            t = t.replace(a, b)
    if NOSPACE.search(t):
        t = NOSPACE.sub("…pe…", t)
    return " ".join(sentence(s) for s in SPLIT.split(t))


# ================================================================ 5. Pañhāpucchaka
P = B.P
NV0 = H.NV0                                    # không nên nói rằng (no dash, as the Pāli)
QT = H.QT
T.item("savitakka_savicara_2", ["savitakkaṃ savicāraṃ"], P("savitakkasavicara"))   # two words (ch. 12)
T.CANON[T.canon("savitakkaṃ savicāraṃ")] = "savitakka_savicara_2"
ETTHA = {"sukhaṃ vedanaṃ": "cảm giác dễ chịu", "adukkhamasukhaṃ vedanaṃ": "cảm giác không khó chịu cũng không dễ chịu",
         "vitakkavicāre": "sự hướng tâm và sự duy trì tâm", "pītiṃ": "sự hân hoan", "sukhaṃ": "hạnh phúc",
         "upekkhaṃ": "sự bình thản", "vitakkaṃ": "sự hướng tâm", "vicāraṃ": "sự duy trì tâm"}   # [pi-1 ^1-1387 …]
for _v in ETTHA.values():
    in_pi1(f"ngoại trừ {_v} sinh khởi trong đó")
QFIXES = [   # punctuation slips in the Pāli (reported)
    ("Anāsavā āsavavippayuttā.", "Anāsavā, āsavavippayuttā."),                         # ^2-485 comma
    ("maggahetukantipi maggādhipatītipi", "maggahetukantipi, maggādhipatītipi"),         # ^2-640 comma
    ("paccuppannāramaṇantipi", "paccuppannārammaṇantipi"),                               # ^2-640 spelling
    ('"āsavā ceva āsavasampayuttā cāti"pi', '"āsavā ceva āsavasampayuttā cā"tipi'),        # ^2-641 quote
    ("āsavavippayuttā sāsavā", "āsavavippayuttasāsavā"),                                 # ^2-641 two words
    ("āsavavippayuttā anāsavā", "āsavavippayuttaanāsavā"),
    ("Araṇāti.", "Araṇā."), ("araṇāti.", "araṇā."),                                       # closing ti of the questions
]


def bare(x, n):
    x = x + ("ṃ" if n else "")
    x = re.sub(r" cā$", " ca", x)
    return T.ITEMS[T.key_of(x)]["p"]


class QV:
    def __init__(self, subjects, single):
        self.subjects, self.single = subjects, single
        self.rx = re.compile(r"^(" + "|".join(map(re.escape, sorted(subjects, key=len, reverse=True))) + r") (.+)$")

    def chunk(self, c, state, first):
        subj, one = "", False
        m = self.rx.match(c)
        if m:
            subj, one, c = self.subjects[m.group(1)], m.group(1) in self.single, m.group(2)
        elif first:
            c = low(c)
        m = re.match(r"^" + DASH + r" etthuppann(?:aṃ|e) (.+?) ṭhapetvā (.+)$", c)
        if m:
            state["nv"] = False
            return f"{subj} {DASH} ngoại trừ {ETTHA[m.group(1)]} {EXCEPT_IN}, {T.pred_vi(m.group(2), {})}"
        assert DASH not in c, c
        m = re.match(r"^(siyā )?na vattabb(?:o|ā|aṃ) (.+)$", c)
        if m:
            qm = B.QUOTE_RE.match(m.group(2))
            if qm:
                vi = f"{NV0} {T.quoted(qm.group(1), qm.group(2), {})}"
            else:
                qm = QT.match(m.group(2))
                vi = f"{NV0} {bare(qm.group(1), qm.group(2))}"
            if m.group(1):
                vi = f"{B.SOMETIMES} {vi}"
            state["nv"] = True
        elif c.endswith("tipi") and (state.get("nv") or first):
            qm = B.QUOTE_RE.match(c)
            x = T.quoted(qm.group(1), qm.group(2), {}) if qm else bare(*QT.match(c).groups()[:2])
            if state.get("nv"):
                vi = f"{B.OR} {x}"
            else:   # ^2-485 "Āsavā ceva āsavasampayuttā cātipi, …" without "na vattabbā" (as written, reported)
                SLIPS.append("na vattabbā missing: " + c)
                vi = f"rằng {x}"
            state["nv"] = True
        else:
            if c.startswith("siyā "):
                vi = f"{B.SOMETIMES} {T.pred_vi(c[5:], {})}"
            else:
                vi = T.pred_vi(c, {})
                if state.get("nv"):
                    vi = "mà " + vi
            state["nv"] = False
        if not subj:
            return vi
        if (one and not vi.startswith("là ")) or vi.startswith(NV0):
            vi = f"{S.THI} {vi}"
        return f"{subj} {vi}"

    def line(self, t):
        for a, b in QFIXES:
            if a in t:
                SLIPS.append(f"{a!r} -> {b!r}")
                t = t.replace(a, b)
        out = []
        for sent in re.split(r"(?<=\.) (?=[A-ZĀ])", t):
            assert sent.endswith("."), sent[-40:]
            parts = re.split(r"(, |; |\x01 ?)", sent[:-1].replace("…pe…", B.PE))
            state, vi = {}, []
            for i, x in enumerate(parts):
                if i % 2:
                    vi.append(B.sep_vi(x))
                    if x.startswith(B.PE) or x == "; ":
                        state["nv"] = False
                else:
                    vi.append(self.chunk(x, state, i == 0))
            out.append(cap("".join(vi)) + ".")
        return " ".join(out)


def _qn(name):
    return f"“{name}”"


SUBJ10 = {"Pītisambojjhaṅgo": cap(_qn(BJ["pīti"])), "Dhammavicayasambojjhaṅgo": cap(_qn(BJ["dhammavicaya"])),
          "dhammavicayasambojjhaṅgo": _qn(BJ["dhammavicaya"]),
          "Cha bojjhaṅgā": "Sáu chi phần giác ngộ", "cha bojjhaṅgā": "sáu chi phần giác ngộ"}
SUBJ10["Pītisambojjhaṅgo"] = "“" + cap(BJ["pīti"]) + "”"
SUBJ10["Dhammavicayasambojjhaṅgo"] = "“" + cap(BJ["dhammavicaya"]) + "”"
SINGLE10 = {"Pītisambojjhaṅgo", "Dhammavicayasambojjhaṅgo", "dhammavicayasambojjhaṅgo"}
SUBJ11 = {"Sammāsaṅkappo": cap(FN["sammāsaṅkappo"]), "Sammādiṭṭhi": cap(FN["sammādiṭṭhi"]),
          "sammādiṭṭhi": FN["sammādiṭṭhi"], "Satta maggaṅgā": "Bảy chi phần của con đường",
          "satta maggaṅgā": "bảy chi phần của con đường"}                     # maggaṅga [pi-1 «chi phần của con đường»]
SINGLE11 = {"Sammāsaṅkappo", "Sammādiṭṭhi", "sammādiṭṭhi"}
SUBJ12 = {"Tīṇi jhānāni": "Ba tầng thiền", "tīṇi jhānāni": "ba tầng thiền", "Dve jhānāni": "Hai tầng thiền",
          "dve jhānāni": "hai tầng thiền", "Paṭhamaṃ jhānaṃ": cap(JH["paṭhamaṃ"]),
          "Catutthaṃ jhānaṃ": cap(JH["catutthaṃ"]), "catutthaṃ jhānaṃ": JH["catutthaṃ"]}
SINGLE12 = {"Paṭhamaṃ jhānaṃ", "Catutthaṃ jhānaṃ", "catutthaṃ jhānaṃ"}
QQ = {10: QV(SUBJ10, SINGLE10), 11: QV(SUBJ11, SINGLE11), 12: QV(SUBJ12, SINGLE12)}

# ================================================================ 6. Suttantabhājanīya: shared strings
NISSITA = ("dựa trên sự tách biệt, dựa trên sự phai nhạt, dựa trên sự chấm dứt, "
           "hướng đến sự buông xả")              # vivekanissitaṃ virāganissitaṃ nirodhanissitaṃ vossaggapariṇāmiṃ [new]
LEADS = "dẫn đến sự hiểu biết trực tiếp, đến sự giác ngộ hoàn toàn, đến Niết-bàn"   # abhiññāya sambodhāya nibbānāya [new]
J1, J2, J3, J4 = F.J1, F.J2, F.J3, F.J4                                    # [pi-1 jhāna formula, via ch4]
J2V = repl(J2, ", chứng nhập", ", vị ấy chứng nhập")
J3V = repl(J3, "phai nhạt, an trú", "phai nhạt, vị ấy an trú")
J4V = repl(J4, ", chứng nhập", ", vị ấy chứng nhập")
J3V_NODASH = repl(J3V, f"người ấy {DASH} “", "người ấy: “")               # no dash in the Pāli (ch. 11)
assert F.JHANA4 == f"{IDHA}, {BHIKKHU} {J1}. {cap(J2V)}. {cap(J3V)}. {cap(J4V)}."
JHANA_SC = f"{IDHA}, {BHIKKHU} {J1}; {J2V}; {J3V_NODASH}; {J4V}"            # ch. 11: ";" between the jhānas
NAMES_AYAT = {"ākāsānañcāyatana": "lĩnh vực không gian vô tận", "viññāṇañcāyatana": "lĩnh vực thức vô tận",
              "ākiñcaññāyatana": "lĩnh vực không có gì cả",
              "nevasaññānāsaññāyatana": "lĩnh vực không phải tri giác cũng không phải không tri giác"}   # [pi-1]
for _v in NAMES_AYAT.values():
    in_pi1(f"có tri giác về {_v} đi kèm")
RUPA3 = ("nhờ hoàn toàn vượt qua các tri giác về hình sắc, nhờ các tri giác về sự va chạm biến mất, "
         "nhờ không chú tâm đến các tri giác về sự đa dạng")                # [pi-1 ^1-265]
in_pi1(RUPA3)
BEYOND = {k: f"hoàn toàn vượt qua {v}" for k, v in NAMES_AYAT.items()}     # sabbaso Xṃ samatikkamma [pi-1 ^1-266]
in_pi1(BEYOND["ākāsānañcāyatana"], BEYOND["viññāṇañcāyatana"], BEYOND["ākiñcaññāyatana"])
THOUGHT = {"ananto ākāso": "Không gian là vô tận", "anantaṃ viññāṇa": "Thức là vô tận",
           "natthi kiñcī": "Không có gì cả"}                                 # [new]
ENTER = "vị ấy chứng nhập và an trú "
FORMLESS = (f"{RUPA3}, với ý nghĩ “{THOUGHT['ananto ākāso']}”, {ENTER}{NAMES_AYAT['ākāsānañcāyatana']}; "
            f"{BEYOND['ākāsānañcāyatana']}, với ý nghĩ “{THOUGHT['anantaṃ viññāṇa']}”, {ENTER}"
            f"{NAMES_AYAT['viññāṇañcāyatana']}; {BEYOND['viññāṇañcāyatana']}, với ý nghĩ “{THOUGHT['natthi kiñcī']}”, "
            f"{ENTER}{NAMES_AYAT['ākiñcaññāyatana']}; {BEYOND['ākiñcaññāyatana']}, {ENTER}"
            f"{NAMES_AYAT['nevasaññānāsaññāyatana']}")
# hindrances, conduct, abandoning
SANTA = H.VINITA[H.VINITA.index("đã lắng yên"):-1]       # santā honti samitā … byantīkatā [ch7 VINITA words]
assert SANTA.startswith("đã lắng yên, đã được làm lắng dịu, đã lắng dịu hoàn toàn, đã biến mất") and \
    SANTA.endswith("đã bị làm cho tiêu tan"), SANTA
CATTA = ("đã được xả bỏ, đã được nhả ra, đã được thả ra, đã được dứt bỏ, đã được buông bỏ, "
         "đã được dứt bỏ và buông bỏ")             # cattattā vantattā muttattā pahīnattā paṭinissaṭṭhattā … [new]
SODHETI = ("làm trong sạch hẳn, làm trong sạch hoàn toàn, làm cho thoát khỏi, làm cho thoát hẳn, "
           "làm cho thoát hoàn toàn")             # (sodheti) visodheti parisodheti moceti vimoceti parimoceti [new]
PARISODH = "làm trong sạch hoàn toàn tâm khỏi"     # X-ā cittaṃ parisodheti [new]
JATA = "đã sinh, đã sinh ra, đã phát khởi, đã hình thành, đã xuất hiện"   # jātā honti sañjātā nibbattā … [ch6 words]
ATIKKANTO = "đã vượt qua, đã vượt khỏi, đã vượt qua hoàn toàn"              # atikkanto hoti vītikkanto samatikkanto
LABHA = H.IDDHI_DEF[H.IDDHI_DEF.index("sự đạt được"):-1]                     # lābho … upasampadā [ch9]
assert LABHA == ("sự đạt được, sự có được, sự đạt đến, sự đạt đến trọn vẹn, sự chạm, sự tự mình chứng nghiệm, "
                 "sự chứng nhập"), LABHA
UPETO, UPETO_PE = H.UPETO, H.UPETO_PE
UPETO_PE2 = "vị ấy là người có được, có được trọn vẹn… " + H.EQUIPPED      # upeto hoti samupeto…pe… samannāgato
IRIYATI = low(H.SENT["Iriyati vattati pāleti yapeti yāpeti carati viharati."])[:-1]   # vị ấy vận động, …, sống
IRIYATI_JH = IRIYATI[:-len("sống")] + "an trú"                              # jhāna context: viharati = «an trú» [pi-1]
SAMAPANNA3 = ("của người đã chứng nhập {}, hoặc của người đã tái sinh vào đó, hoặc của người an trú trong hạnh "
              "phúc ngay trong đời này")      # X samāpannassa vā upapannassa vā diṭṭhadhammasukhavihārissa vā [new]
in_pi1("để an trú trong hạnh phúc ngay trong đời này")
LIVE, ABIDE = "sống", "an trú"                                             # viharatī (lemma)
SIT = {   # sampajānakārī situations [new]
    "abhikkante paṭikkante": "khi đi tới, khi đi lui", "ālokite vilokite": "khi nhìn thẳng, khi nhìn quanh",
    "samiñjite pasārite": "khi co tay chân, khi duỗi tay chân",
    "saṅghāṭipattacīvaradhāraṇe": "khi mang y ngoài, bát và y",
    "asite pīte khāyite sāyite": "khi ăn, khi uống, khi nhai, khi nếm",
    "uccārapassāvakamme": "khi đại tiện, tiểu tiện",
    "gate ṭhite nisinne sutte jāgarite bhāsite tuṇhībhāve": "khi đi, khi đứng, khi ngồi, khi ngủ, khi thức, khi nói, khi im lặng"}
SK = "hành động với sự hiểu biết rõ ràng"                                  # sampajānakārī hoti [new]
SSK = "hành động với sự tỉnh thức và hiểu biết rõ ràng"                     # sato sampajānakārī hoti [new]
SS = "với sự tỉnh thức và hiểu biết rõ ràng"                                # sato sampajāno (abhikkamati …) [new]
VAR_SAMMINJ = " [khác chính tả (Sī., Syā.): sammiñjite]"
SITS = list(SIT)


def sk_list(var=False):
    """So abhikkante paṭikkante sampajānakārī hoti, … (all seven)"""
    out = []
    for k in SITS:
        v = SIT[k]
        if var and k == "samiñjite pasārite":
            v = v.replace("khi co tay chân,", "khi co tay chân" + VAR_SAMMINJ + ",")
        out.append(f"{SK} {v}")
    return "; ".join(out)


SS_ACTS = ["đi tới", "đi lui", "nhìn thẳng", "nhìn quanh", "co tay chân", "duỗi tay chân"]   # abhikkamati … pasāreti


def ss_answer(last_sato=True):
    """sato sampajāno abhikkamati, …, sato sampajānakārī hoti, … tuṇhībhāve (sato) sampajānakārī hoti"""
    a = ", ".join(f"{x} {SS}" for x in SS_ACTS)
    rest = [SSK] + [f"{SSK} {SIT[k]}" for k in SITS[3:]]
    if not last_sato:
        rest[-1] = f"{SK} {SIT[SITS[-1]]}"
    return f"{a}; " + "; ".join(rest)


# Suttanta key phrases (lemma = the same words as in the opening paragraph ^2-508) [new unless marked]
PATIMOKKHA = "bộ giới luật căn bản"                                         # pātimokkha
L = {
    "patimokkha": f"được thu thúc bằng sự thu thúc theo {PATIMOKKHA}",      # pātimokkhasaṃvarasaṃvuto
    "acaragocara": "đầy đủ hạnh kiểm đúng đắn và nơi lui tới thích hợp",    # ācāragocarasampanno
    "anumatta": "thấy sự nguy hiểm trong những lỗi nhỏ nhặt",               # aṇumattesu vajjesu bhayadassāvī
    "sikkha": "thọ trì và tu học các điều tu học",                         # samādāya sikkhati sikkhāpadesu
    "indriya": "phòng hộ cửa các giác quan",                               # indriyesu guttadvāro [pi-1 ^1-1354]
    "bhojana": "biết tiết độ trong ăn uống",                                # bhojane mattaññū [pi-1 ^1-1355]
    "jagariya": "chuyên tâm thực hành việc thức canh vào đầu đêm và cuối đêm",   # pubbarattāpararattaṃ jāgariy…
    "bodhi": "chuyên tâm tu tập các hiện tượng hỗ trợ cho sự giác ngộ",    # bodhipakkhikānaṃ … bhāvanānuyogamanuyutto
    "vivitta_bhajati": "lui tới chỗ ở thanh vắng",                          # vivittaṃ senāsanaṃ bhajati
    "gato": "đi đến rừng, hoặc đi đến gốc cây, hoặc đi đến ngôi nhà trống",
    "nisidati": "ngồi xuống, xếp chân kiết già", "uju": "giữ thân ngay thẳng",
    "parimukha": "thiết lập sự tỉnh thức trước mặt",
    "abhijjha": "sau khi dứt bỏ sự thèm muốn đối với thế gian", "vigatabhijjha": "với tâm đã lìa sự thèm muốn",
    "abhijjhaya": f"{PARISODH} sự thèm muốn",
    "byapada": "sau khi dứt bỏ ác ý và sự sân hận dữ dội", "abyapanna": "có tâm không ác ý",
    "byapadapadosa": f"{PARISODH} ác ý và sự sân hận dữ dội",
    "thina": "sau khi dứt bỏ sự uể oải và đờ đẫn", "vigatathina": "đã lìa sự uể oải và đờ đẫn",
    "aloka": "có tri giác về ánh sáng", "sato": "tỉnh thức và hiểu biết rõ ràng",
    "thinamiddha": f"{PARISODH} sự uể oải và đờ đẫn",
    "uddhacca": "sau khi dứt bỏ sự xao động và hối tiếc", "anuddhato": "không xao động",
    "vupasanta": "có tâm đã lắng dịu hoàn toàn", "vupasanta_full": "có tâm đã lắng dịu hoàn toàn ở nơi bản thân",
    "uddhaccakukkucca": f"{PARISODH} sự xao động và hối tiếc",
    "vicikiccha": "sau khi dứt bỏ sự hoài nghi", "tinna": "đã vượt qua sự hoài nghi",
    "akathamkathi": "không còn băn khoăn về các hiện tượng thiện", "vicikicchaya": f"{PARISODH} sự hoài nghi",
    "pancanivarana": "sau khi dứt bỏ năm chướng ngại này", "upakkilesa": "những thứ làm vẩn đục tâm",
    "dubbali": "làm suy yếu trí tuệ",
}
in_pi1("sự phòng hộ cửa các giác quan", "sự biết tiết độ trong ăn uống", "có sự trong sáng ở nơi bản thân",
       "sự tỉnh thức hoàn toàn trong sạch nhờ sự bình thản")
J1_LEMMA = J1[:J1.index(", chứng nhập")]          # hoàn toàn tách khỏi các dục lạc, tách khỏi các hiện tượng bất thiện
LJ = {   # jhāna-formula lemmas = the pi-1 words of the formula
    "vivicca": J1_LEMMA, "savitakka": P("savitakkasavicara"), "vivekaja": "sinh từ sự tách biệt",
    "pitisukha": "sự hân hoan và hạnh phúc", "vitakkavicara": "nhờ sự hướng tâm và sự duy trì tâm lắng xuống",
    "ajjhatta": "ở nơi bản thân", "sampasadana": "sự trong sáng", "ekodi": "sự hợp nhất của tâm",
    "avitakka": P("avitakkaavicara"), "samadhija": "sinh từ định tâm", "pitiya": "nhờ sự hân hoan phai nhạt",
    "upekkhako": "bình thản", "sato_ca": "tỉnh thức và hiểu biết rõ ràng",
    "sukhanca": "cảm nhận hạnh phúc bằng thân", "ariya": "là trạng thái mà nhờ đó các bậc thánh mô tả",
    "usv": "Người bình thản, có sự tỉnh thức, an trú trong hạnh phúc",
    "sukhassa": "nhờ dứt bỏ sự dễ chịu và dứt bỏ sự khó chịu",
    "pubbeva": "nhờ niềm vui và nỗi buồn đã biến mất từ trước", "adm": S.ADM,
    "upekkhasati": "có sự tỉnh thức hoàn toàn trong sạch nhờ sự bình thản",
    "rupasanna": "nhờ hoàn toàn vượt qua các tri giác về hình sắc",
    "patigha": "nhờ các tri giác về sự va chạm biến mất",
    "nanatta": "nhờ không chú tâm đến các tri giác về sự đa dạng",
}
for _k in ("vivicca", "savitakka", "vivekaja", "pitisukha", "vitakkavicara", "sampasadana", "ekodi", "avitakka",
           "samadhija", "pitiya", "sato_ca", "sukhanca", "ariya", "usv", "sukhassa", "pubbeva", "upekkhasati"):
    assert LJ[_k] in (J1 + J2 + J3 + J4), _k
for _k in ("rupasanna", "patigha", "nanatta"):
    assert LJ[_k] in RUPA3


def lem(x):
    return f"“{cap(x)}”"


def tena(x):
    return f"{TENA} “{x}”."


def qa(name, body, quoted=True):
    """Tattha katamo X? Yo … – ayaṃ vuccati "X"."""
    return f"{q(name)} {WHAT}{body} {DASH} {called(name, quoted)}."


def qpe(name):
    """Tattha katamaṃ X…pe… idaṃ vuccati "X"."""
    return f"{TATTHA} {name} là gì… {called(name)}."


def sodheti(what):
    """Idaṃ cittaṃ imāya / imamhā X sodheti … parimoceti."""
    return f"Vị ấy làm trong sạch tâm này khỏi {what} này, {SODHETI}."


def citta_qa():
    return qa("tâm", CITTA_PE)


def viharati_pe(abide):
    w = ABIDE if abide else LIVE
    return f"{lem(w)}… {low(TENA)} “{w}”."


def viharati_full(abide):
    w = ABIDE if abide else LIVE
    return f"{lem(w)}: {IRIYATI_JH if abide else IRIYATI}. {tena(w)}"


def upasampajja(obj):
    return f"{lem('chứng nhập')}: điều mà đối với {obj} là {LABHA}."


GANANA_VAR = " [khác chính tả (Syā.): gaṇanānupubbato; cũng vậy ở các chỗ sau]"
SUKHA_J = FEEL["somanassa"]                     # Yaṃ cetasikaṃ sātaṃ … (sukha as a jhāna factor = «hạnh phúc») [pi-1 ^1-3]
SATI_Q = qa("sự tỉnh thức", SATI_PE)            # Tattha katamā sati? Yā sati anussati…pe… sammāsati – …
SAMP_Q = qa("sự hiểu biết rõ ràng", PANNA_PE)   # Tattha katamaṃ sampajaññaṃ? Yā paññā pajānanā…pe… – …
UPEK_Q = qa("sự bình thản", UPEKKHA4)
PITI_Q = qa("sự hân hoan", PITI)
SUKHA_Q = qa("hạnh phúc", SUKHA_J)
VITAKKA_Q = qa("sự hướng tâm", VITAKKA7)
VITAKKA_Q_PE = qa("sự hướng tâm", VITAKKA_PE)
ABHIJJHA_Q = qa("sự thèm muốn", RAGA_PE)
BYAPADA_Q_PE = qa("ác ý", DOSA_PE)
PADOSA = ("Điều gì là ác ý thì điều ấy là sự sân hận dữ dội, điều gì là sự sân hận dữ dội thì điều ấy là ác ý.")
THINA_Q = qa("sự uể oải", THINA_VAR)
MIDDHA_Q = qa("sự đờ đẫn", MIDDHA)
UDDHACCA_Q = qa("sự xao động", UDDHACCA)
STEM = {"abhijjha": "sự thèm muốn", "byapada": "ác ý và sự sân hận dữ dội", "thina": "sự uể oải và đờ đẫn",
        "uddhacca": "sự xao động và hối tiếc", "vicikiccha": "sự hoài nghi"}
FIVE_P = "sự thèm muốn"


def santa(subject):
    return f"{subject} {SANTA}."


def iti_upeto(a, b, pe=True):
    return f"Như vậy, với {a} này và với {b} này, {UPETO_PE if pe else UPETO}."


# ================================================================ 7. hand lines (Suttanta), in order
HAND10 = [
    ("Tattha katamo satisambojjhaṅgo? Idha bhikkhu satimā hoti",
     f"{qq(BJ['sati'])} {IDHA}, {BHIKKHU} có sự tỉnh thức, được trang bị sự tỉnh thức và sự khôn ngoan tột bậc, "
     f"là người nhớ được, nhớ lại được cả những việc đã làm từ lâu, cả những lời đã nói từ lâu {DASH} "
     f"{called(BJ['sati'])}."),
    ("So tathā sato viharanto",
     f"Vị ấy, khi sống tỉnh thức như vậy, dùng trí tuệ tìm hiểu, xem xét, thẩm xét toàn diện hiện tượng ấy {DASH} "
     f"{called(BJ['dhammavicaya'])}."),
    ("Tassa taṃ dhammaṃ paññāya pavicinato",
     f"Ở vị ấy, khi dùng trí tuệ tìm hiểu, xem xét, thẩm xét toàn diện hiện tượng ấy, sự tinh tấn được khởi động, "
     f"không chùng xuống {DASH} {called(BJ['vīriya'])}."),
    ("Āraddhavīriyassa uppajjati",
     f"Ở người đã khởi động tinh tấn, sự hân hoan không có tính trần tục sinh khởi {DASH} {called(BJ['pīti'])}."),
    ("Pītimanassa kāyopi passambhati",
     f"Ở người có tâm hân hoan, thân cũng lắng dịu, tâm cũng lắng dịu {DASH} {called(BJ['passaddhi'])}."),
    ("Passaddhakāyassa sukhino",
     f"Ở người có thân đã lắng dịu, có hạnh phúc, tâm đi vào định tâm {DASH} {called(BJ['samādhi'])}."),
    ("So tathā samāhitaṃ cittaṃ",
     f"Vị ấy là người khéo léo nhìn với sự bình thản trọn vẹn đối với tâm đã được định tâm như vậy {DASH} "
     f"{called(BJ['upekkhā'])}."),
]
YADAPI = [   # (key, first a, first b, a, b)
    ("sati", "sự tỉnh thức đối với các hiện tượng ở nơi bản thân", "sự tỉnh thức đối với các hiện tượng ở bên ngoài bản thân"),
    ("dhammavicaya", "sự tìm hiểu kỹ đối với các hiện tượng ở nơi bản thân",
     "sự tìm hiểu kỹ đối với các hiện tượng ở bên ngoài bản thân"),
    ("vīriya", "sự tinh tấn nơi thân", "sự tinh tấn trong tâm"),
    ("pīti", "sự hân hoan " + P("savitakkasavicara"), "sự hân hoan " + P("avitakkaavicara")),
    ("passaddhi", "sự an tịnh của thân tinh thần", "sự an tịnh của tâm"),
    ("samādhi", "định tâm " + P("savitakkasavicara"), "định tâm " + P("avitakkaavicara")),
    ("upekkhā", "sự bình thản đối với các hiện tượng ở nơi bản thân",
     "sự bình thản đối với các hiện tượng ở bên ngoài bản thân"),
]
in_pi1("sự an tịnh của thân tinh thần", "sự an tịnh của tâm", "sự tìm hiểu kỹ", "nơi thân", "trong tâm")
_PREF = {"sati": "Tattha katamo satisambojjhaṅgo? Atthi", "dhammavicaya": "Tattha katamo dhammavicayasambojjhaṅgo?",
         "vīriya": "Tattha katamo vīriyasambojjhaṅgo?", "pīti": "Tattha katamo pītisambojjhaṅgo?",
         "passaddhi": "Tattha katamo passaddhisambojjhaṅgo?", "samādhi": "Tattha katamo samādhisambojjhaṅgo?",
         "upekkhā": "Tattha katamo upekkhāsambojjhaṅgo?"}
for _k, _a, _b in YADAPI:
    _fa, _fb = _a, _b
    if _k == "passaddhi":
        _fa += " [khác chính tả (Syā., Ka.): kāyappassaddhi]"
        _fb += " [khác chính tả (Syā., Ka.): cittappassaddhi]"
    HAND10.append((_PREF[_k], f"{qq(BJ[_k])} Có {_fa}, có {_fb}. {cap(_a)} cũng là “{BJ[_k]}”, {LEADS}. "
                              f"{cap(_b)} cũng là “{BJ[_k]}”, {LEADS}."))
HAND10.append(("Tattha katamo satisambojjhaṅgo? Idha bhikkhu satisambojjhaṅgaṃ bhāveti",
               f"{qq(BJ['sati'])} {IDHA}, {BHIKKHU} tu tập {BJ['sati']}, {NISSITA}; "
               + "… ".join(f"tu tập {BJ[k]}" for k in BJ_ORDER[1:]) + f", {NISSITA}."))


def check_ch4_same():
    """the ch. 11 Suttanta definitions of sammādiṭṭhi … sammāājīvo have the ch. 4 Pāli (so the ch. 4 Vietnamese)."""
    p4 = open(os.path.join(S.PALI_DIR, "4-saccavibhango.md"), encoding="utf-8").read().split("\n")
    p11 = open(os.path.join(S.PALI_DIR, "11-maggangavibhango.md"), encoding="utf-8").read().split("\n")
    out = []
    for pre in ("Tattha katamā sammādiṭṭhi? Dukkhe ñāṇaṃ", "Tattha katamo sammāsaṅkappo? Nekkhammasaṅkappo",
                "Tattha katamā sammāvācā? Musāvādā", "Tattha katamo sammākammanto? Pāṇātipātā",
                "Tattha katamo sammāājīvo? Idha ariyasāvako"):
        a = [x for x in p4 if x.startswith(pre)]
        b = [x for x in p11 if x.startswith(pre)]
        assert len(a) == len(b) == 1 and a[0] == b[0], pre
        out.append((pre, [v for p, v in F.HAND4 if p == pre][0]))
    return out


HAND11 = check_ch4_same() + [
    ("Tattha katamo sammāvāyāmo? Idha bhikkhu anuppannānaṃ",
     f"{q(FN['sammāvāyāmo'])} {IDHA}, {BHIKKHU} {H.EFF_ALL} {DASH} {called(FN['sammāvāyāmo'])}."),
    ("Tattha katamā sammāsati? Idha bhikkhu kāye",
     f"{q(FN['sammāsati'])} {IDHA}, {BHIKKHU}, " + "; ".join(f"{H.anup(a)}, {F.SATI_TAIL}" for a in H.ASPECTS)
     + f" {DASH} {called(FN['sammāsati'])}."),
    ("Tattha katamo sammāsamādhi? Idha bhikkhu vivicceva",
     f"{q(FN['sammāsamādhi'])} {JHANA_SC} {DASH} {called(FN['sammāsamādhi'])}."),
    ("Tattha katamā sammādiṭṭhi? Idha bhikkhu sammādiṭṭhiṃ bhāveti",
     f"{q(FN['sammādiṭṭhi'])} {IDHA}, {BHIKKHU} tu tập {FN['sammādiṭṭhi']}, {NISSITA}; "
     + "… ".join(f"tu tập {FN[k]}" for k in PATH_ORDER[1:]) + f", {NISSITA}."),
]
assert H.EFF_ALL in pi1("1-1377") or "; ".join(H.EFF) == H.EFF_ALL

# ch. 12: the opening paragraph ^2-508
SENASANA9 = "rừng, gốc cây, núi, khe núi, hang núi, bãi tha ma, rừng sâu, khoảng trời trống, đống rơm"
P508 = (
    f"{IDHA}, {BHIKKHU} sống {L['patimokkha']}, {L['acaragocara']}, {L['anumatta']}, {L['sikkha']}, "
    f"{L['indriya']}, {L['bhojana']}, {L['jagariya']}, với sự liên tục và sự khôn ngoan, {L['bodhi']}. "
    f"Vị ấy {sk_list(True)}. "
    f"Vị ấy {L['vivitta_bhajati']}: {SENASANA9}, ít tiếng động, ít ồn ào, vắng hơi người, kín đáo với người đời "
    f"[khác chính tả (Sī., Syā.): manussarāhaseyyakaṃ], thích hợp cho sự độc cư. "
    f"Vị ấy, {L['gato']}, {L['nisidati']}, {L['uju']}, {L['parimukha']}. "
    f"Vị ấy, {L['abhijjha']}, sống {L['vigatabhijjha']}, {L['abhijjhaya']}. "
    f"{cap(L['byapada'])}, vị ấy sống {L['abyapanna']}, thương xót và mong điều lợi ích cho tất cả chúng sinh và "
    f"muôn loài, {L['byapadapadosa']}. "
    f"{cap(L['thina'])}, vị ấy sống {L['vigatathina']}, {L['aloka']}, {L['sato']}, {L['thinamiddha']}. "
    f"{cap(L['uddhacca'])}, vị ấy sống {L['anuddhato']}, {L['vupasanta_full']}, {L['uddhaccakukkucca']}. "
    f"{cap(L['vicikiccha'])}, vị ấy sống {L['tinna']}, {L['akathamkathi']}, {L['vicikicchaya']}. "
    f"Vị ấy, {L['pancanivarana']}, là {L['upakkilesa']}, {L['dubbali']}, {J1}; {J2V}; {J3V}; {J4V}; {FORMLESS}.")

BHIKKHU_DEF = ("tỳ-khưu theo danh xưng, tỳ-khưu theo sự tự xưng, tỳ-khưu vì đi khất thực, tỳ-khưu vì là người khất "
               "thực, tỳ-khưu vì đã chấp nhận đời sống khất thực, tỳ-khưu vì mặc y may từ những mảnh vải vụn, tỳ-khưu vì "
               "phá vỡ các hiện tượng xấu ác bất thiện, tỳ-khưu vì đã phá vỡ các hiện tượng xấu ác bất thiện, tỳ-khưu do đã "
               "dứt bỏ một phần các phiền não, tỳ-khưu do đã dứt bỏ toàn bộ các phiền não, tỳ-khưu còn đang tu học, "
               "tỳ-khưu đã hoàn tất tu học, tỳ-khưu không phải còn đang tu học cũng không phải đã hoàn tất tu học, tỳ-khưu "
               "hàng đầu, tỳ-khưu hiền thiện, tỳ-khưu tinh túy, tỳ-khưu cốt lõi, tỳ-khưu đã được thọ giới đầy đủ bởi Tăng "
               "đoàn hòa hợp, bằng một tăng sự gồm một lời đề nghị và ba lần tuyên bố, không thể bị hủy bỏ, xứng đáng "
               "được duy trì")   # [new]
in_pi1("Tăng đoàn")
VITIKKAMA3 = "sự vi phạm bằng thân, sự vi phạm bằng lời nói, sự vi phạm bằng thân và lời nói"   # [pi-1 ^1-1368]
AVITIKKAMA3 = "sự không vi phạm bằng thân, sự không vi phạm bằng lời nói, sự không vi phạm bằng thân và lời nói"
in_pi1(VITIKKAMA3, AVITIKKAMA3)
ACARA, ANACARA = "hạnh kiểm đúng đắn", "hạnh kiểm sai trái"                 # ācāro / anācāro [new]
GOCARA, AGOCARA = "nơi lui tới thích hợp", "nơi lui tới không thích hợp"    # gocaro / agocaro [new]
GIFTS = ["việc biếu tre", "việc biếu lá", "việc biếu hoa", "việc biếu trái cây", "việc biếu đồ tắm",
         "việc biếu cây chà răng", "lời nịnh bợ", "lời nửa thật nửa giả", "việc chăm bẵm con trẻ",
         "việc chạy việc vặt"]                                               # veḷudāna … jaṅghapesanika [new]
VAR_MUGGA = " [khác chính tả (Sī.): muggasuppatāya]"
WRONG_LIFE = "sinh kế sai lầm này hay sinh kế sai lầm khác bị các Đức Phật chê trách"   # aññataraññatarena … micchāājīvena
in_pi1("sinh kế sai lầm")
_g = [f"bằng {x}" + (VAR_MUGGA if x == "lời nửa thật nửa giả" else "") for x in GIFTS]
ANACARA_LIFE = (f"{T.IDHEKACCO} nuôi sống bản thân {_g[0]}, " + ", ".join(f"hoặc {x}" for x in _g[1:])
                + f", hoặc bằng {WRONG_LIFE}")
ACARA_LIFE = (f"{T.IDHEKACCO} không nuôi sống bản thân {GIFTS[0] and 'bằng ' + GIFTS[0]}, "
              + ", ".join(f"không bằng {x}" for x in GIFTS[1:]) + f", không bằng {WRONG_LIFE}")
RESORTS = ["nhà kỹ nữ", "nhà góa phụ", "nhà thiếu nữ lớn tuổi chưa chồng", "nhà người ái nam ái nữ",
           "chỗ ở của tỳ-khưu-ni", "quán rượu"]                              # vesiyā … pānāgāra-gocaro [new]
KINGS = ("với vua chúa, với các quan đại thần, với các đạo sĩ ngoại đạo, với các đệ tử của đạo sĩ ngoại đạo, "
         "bằng sự giao du không thích đáng")
FOUR_ASSEMBLY = "các tỳ-khưu, các tỳ-khưu-ni, các nam cư sĩ, các nữ cư sĩ"
FAM_BAD = ("hoặc có những gia đình không có niềm tin, không có lòng tin trong sáng, không như giếng nước cho người "
           "cần, hay mắng nhiếc và lăng mạ, mong điều không lợi ích, mong điều không tốt lành, mong điều không thoải "
           f"mái, mong điều không an ổn cho {FOUR_ASSEMBLY}, người ấy gần gũi, lui tới, thường xuyên lui tới hầu cận "
           "những gia đình như thế")
FAM_GOOD = ("hoặc có những gia đình có niềm tin, có lòng tin trong sáng, như giếng nước cho người cần, rực sáng bởi "
            "y cà-sa, có gió của các bậc ẩn sĩ thổi qua lại, mong điều lợi ích, mong điều tốt lành, mong điều thoải "
            f"mái, mong điều an ổn cho {FOUR_ASSEMBLY}, người ấy gần gũi, lui tới, thường xuyên lui tới hầu cận "
            "những gia đình như thế")
assert "mong điều không lợi ích, mong điều không tốt lành, mong điều không thoải mái, mong điều không an ổn" in \
    [v for p, v in F.HAND4 if p == "Tattha katamo appiyehi sampayogo dukkho?"][0]
AGOCARA_LINE = (f"{q(AGOCARA)} {T.IDHEKACCO} lui tới {RESORTS[0]}, " + ", ".join(f"hoặc lui tới {x}" for x in RESORTS[1:])
                + f", sống giao du {KINGS}; {FAM_BAD} {DASH} {called(AGOCARA)}.")
GOCARA_LINE = (f"{q(GOCARA)} {T.IDHEKACCO} không lui tới {RESORTS[0]}, "
               + ", ".join(f"không lui tới {x}" for x in RESORTS[1:])
               + f", sống không giao du {KINGS}; {FAM_GOOD} {DASH} {called(GOCARA)}. "
               + iti_upeto(ACARA, GOCARA) + " " + tena(L["acaragocara"]))
_S1352 = pi1("1-1352")
SENSE_BAD = between(_S1352, "là gì? ", f" {DASH} đó được gọi là")          # [pi-1 ^1-1352]
SENSE_GOOD = between(pi1("1-1354"), "là gì? ", f" {DASH} đó được gọi là")   # [pi-1 ^1-1354]
FOOD_BAD = between(pi1("1-1353"), "là gì? ", f" {DASH} đó được gọi là")
FOOD_GOOD = between(pi1("1-1355"), "là gì? ", f" {DASH} đó được gọi là")
AGUTTA = "sự không phòng hộ cửa các giác quan"
GUTTA = "sự phòng hộ cửa các giác quan"
AMATTA = "sự không biết tiết độ trong ăn uống"
MATTA = "sự biết tiết độ trong ăn uống"
for _x in (AGUTTA, GUTTA, AMATTA, MATTA):
    in_pi1(f"{_x} là gì?")
SENSE_GOOD_SLIP = SENSE_GOOD   # ^2-517 "Ñatvādhikaraṇamenaṃ" = Yatvādhikaraṇamenaṃ (spelling, as meant)


def check_pi1_conduct():
    """^2-517 / ^2-518 have the pi-1 ^1-1352 … ^1-1355 Pāli (quotes, sandhi and ^2-517 Ñatvā- aside)."""
    p12 = open(os.path.join(S.PALI_DIR, "12-jhanavibhango.md"), encoding="utf-8").read()

    def norm(x):
        return re.sub(r'["\s,–]|ti\b', "", x.replace("nānubyañjana", "naanubyañjana").replace("Ñatvā", "Yatvā")
                      .replace("phāsu vihāro", "phāsuvihāro"))
    for bid in ("1-1352", "1-1353", "1-1354", "1-1355"):
        body = between(pi1_pali(bid), "? ", " – ayaṃ vuccati")
        assert norm(body) in norm(p12), bid


FIVE_HIND = "Ý muốn dục lạc, ác ý, sự uể oải, sự đờ đẫn, sự xao động, sự hối tiếc, sự hoài nghi"   # [pi-1 names]
in_pi1("sự uể oải", "sự đờ đẫn", "sự hối tiếc")
KAMA6 = ("Ý muốn là dục lạc, sự tham đắm là dục lạc, ý muốn và sự tham đắm là dục lạc, tư duy là dục lạc, "
         "sự tham đắm là dục lạc, sự tham đắm do tư duy là dục lạc")    # Chando kāmo, … saṅkapparāgo kāmo [new]

HAND12 = [
    ("Idha bhikkhu pātimokkhasaṃvarasaṃvuto", P508),
    ('"Idhā"ti',
     f"{lem('ở đời này')}: trong quan điểm này, trong sự chấp nhận này, trong sự ưa thích này, trong sự tiếp nhận này, "
     "trong Giáo Pháp này, trong Giới Luật này, trong Giáo Pháp và Giới Luật này, trong lời dạy này, trong đời sống "
     f"tu hành trong sạch này, trong giáo huấn của Bậc Đạo Sư này. {tena('ở đời này')}"),
    ('"Bhikkhū"ti', f"{lem('tỳ-khưu')}: {BHIKKHU_DEF}."),
    ('"Pātimokkha"nti',
     f"{lem(PATIMOKKHA)}: giới hạnh, nền tảng, khởi đầu, sự thực hành, sự tự chế, sự thu thúc, sự giải thoát, điều "
     f"đứng đầu để thành tựu các hiện tượng thiện. {lem('sự thu thúc')}. {cap(AVITIKKAMA3)}. {lem('được thu thúc')}. "
     f"Với sự thu thúc theo {PATIMOKKHA} này, {UPETO}. {tena(L['patimokkha'])}"),
    ('"Viharatī"ti iriyati', viharati_full(False)),
    ('"Ācāragocarasampanno"ti', f"{lem(L['acaragocara'])}: có {ACARA}, có {ANACARA}."),
    ("Tattha katamo anācāro?",
     f"{q(ANACARA)} {cap(VITIKKAMA3)} {DASH} {called(ANACARA)}. Mọi sự phạm giới đều là {ANACARA}. "
     f"{ANACARA_LIFE} {DASH} {called(ANACARA)}."),
    ("Tattha katamo ācāro?",
     f"{q(ACARA)} {cap(AVITIKKAMA3)} {DASH} {called(ACARA)}. Mọi sự thu thúc theo giới hạnh đều là {ACARA}. "
     f"{ACARA_LIFE} {DASH} {called(ACARA)}."),
    ('"Gocaro"ti', f"{lem(GOCARA)}: có {GOCARA}, có {AGOCARA}."),
    ("Tattha katamo agocaro?", AGOCARA_LINE),
    ("Tattha katamo gocaro?", GOCARA_LINE),
    ('"Aṇumattesu',
     f"{lem(L['anumatta'])}: ở đây, những lỗi nhỏ nhặt là gì? Những lỗi nào nhỏ, nhỏ bé, nhẹ, được xem là nhẹ, cần "
     "được xử lý bằng sự tự chế, cần được xử lý bằng sự thu thúc, cần được xử lý bằng sự khởi tâm, gắn liền với sự "
     f"chú tâm {DASH} {called('những lỗi nhỏ nhặt')}. Như vậy, đối với những lỗi nhỏ nhặt này, vị ấy là người thấy "
     f"lỗi, thấy sự nguy hiểm, thấy sự tai hại và thấy lối thoát. {tena(L['anumatta'])}"),
    ('"Samādāya',
     f"{lem(L['sikkha'])}: ở đây, sự tu học là gì? Bốn sự tu học {DASH} sự tu học của tỳ-khưu dành cho các tỳ-khưu, "
     "sự tu học của tỳ-khưu-ni dành cho các tỳ-khưu-ni, sự tu học của nam cư sĩ dành cho các nam cư sĩ, sự tu học "
     f"của nữ cư sĩ dành cho các nữ cư sĩ. {cap(called('các sự tu học'))}. Như vậy, vị ấy thọ trì và thực hành các "
     "sự tu học này một cách toàn bộ, về mọi mặt, trọn vẹn, không thiếu sót, không sót lại gì. "
     f"{tena(L['sikkha'])}"),
    ('"Indriyesu guttadvāro"ti', f"{lem(L['indriya'])}: có {GUTTA}, có sự không phòng hộ cửa."),
    ("Tattha katamā indriyesu aguttadvāratā?", f"{q(AGUTTA)} {SENSE_BAD} {DASH} {called(AGUTTA)}."),
    ("Tattha katamā indriyesu guttadvāratā?",
     f"{q(GUTTA)} {SENSE_GOOD_SLIP} {DASH} {called(GUTTA)}. Với {GUTTA} này, {UPETO_PE2}. {tena(L['indriya'])}"),
    ('"Bhojane mattaññū"ti', f"{lem(L['bhojana'])}: có {MATTA}, có {AMATTA}."),
    ("Tattha katamā bhojane amattaññutā?", f"{q(AMATTA)} {FOOD_BAD} {DASH} {called(AMATTA)}."),
    ("Tattha katamā bhojane mattaññutā?",
     f"{q(MATTA)} {FOOD_GOOD} {DASH} {called(MATTA)}. Với {MATTA} này, {UPETO_PE}. {tena(L['bhojana'])}"),
    ("Kathañca bhikkhu pubbarattāpararattaṃ",
     f"Và {BHIKKHU} {L['jagariya']} như thế nào? {IDHA}, {BHIKKHU} vào ban ngày, bằng đi kinh hành và ngồi, "
     f"{PARISODH} các hiện tượng gây chướng ngại; vào canh đầu của đêm, bằng đi kinh hành và ngồi, {PARISODH} các "
     "hiện tượng gây chướng ngại; vào canh giữa của đêm, nằm nghiêng bên phải theo tư thế sư tử, đặt chân này lên "
     "chân kia [dị bản (Syā.): pādena pādaṃ], tỉnh thức và hiểu biết rõ ràng, sau khi chú tâm đến tri giác về việc "
     f"thức dậy; vào canh cuối của đêm, sau khi thức dậy, bằng đi kinh hành và ngồi, {PARISODH} các hiện tượng gây "
     f"chướng ngại. Như vậy, {BHIKKHU} {L['jagariya']}."),
    ('"Sātacca"nti.', f"{lem('sự liên tục')}. {WHAT}{VIRIYA_PE}."),
    ('"Nepakka"nti.', f"{lem('sự khôn ngoan')}. {WHAT}{PANNA_PE}."),
    ('"Bodhipakkhikānaṃ',
     f"{lem(L['bodhi'])}. {q('các hiện tượng hỗ trợ cho sự giác ngộ')} {cap(SATTA_BJ)} {DASH} "
     + T.listing([BJ[k] for k in BJ_ORDER]) + f". {cap(called('các hiện tượng hỗ trợ cho sự giác ngộ'))}. "
     "Như vậy, vị ấy thực hành những hiện tượng hỗ trợ cho sự giác ngộ ấy, tu tập, làm đi làm lại. "
     f"{tena(L['bodhi'])}"),
    ("Kathañca bhikkhu abhikkante",
     f"Và {BHIKKHU} " + sk_list() + f" như thế nào? {IDHA}, {BHIKKHU} {ss_answer()}."),
    ("Tattha katamā sati? Yā sati anussati paṭissati sati", qa("sự tỉnh thức", SATI_FULL)),
    ('"Sampajāno"ti',
     f"{lem('hiểu biết rõ ràng')}: ở đây, sự hiểu biết rõ ràng là gì? {WHAT}{PANNA_FULL} {DASH} "
     f"{called('sự hiểu biết rõ ràng')}. {iti_upeto('sự tỉnh thức', 'sự hiểu biết rõ ràng')} "
     f"Như vậy, {BHIKKHU} {ss_answer(last_sato=False)}."),
    ('"Vivitta"nti',
     f"{lem('thanh vắng')}: chỗ ở dù ở gần, nhưng không bị người tại gia và người xuất gia chen chúc. Vì thế nơi ấy "
     "thanh vắng. Chỗ ở dù ở xa, nhưng không bị người tại gia và người xuất gia chen chúc. Vì thế nơi ấy thanh vắng."),
    ('"Senāsana"nti',
     f"{lem('chỗ ở')}: giường cũng là chỗ ở, ghế cũng là chỗ ở, nệm cũng là chỗ ở, gối [khác chính tả (Sī., Syā.): "
     "bimbohanampi] cũng là chỗ ở, tịnh xá cũng là chỗ ở, nhà một mái cũng là chỗ ở, lâu đài cũng là chỗ ở, tháp "
     "canh cũng là chỗ ở, nhà mái tròn cũng là chỗ ở, động đá cũng là chỗ ở, hang cũng là chỗ ở, gốc cây cũng là "
     "chỗ ở, bụi tre cũng là chỗ ở. Hoặc bất cứ nơi nào các tỳ-khưu lui về, tất cả nơi ấy đều là chỗ ở."),
    ('"Vivittaṃ senāsanaṃ bhajatī"ti',
     f"{lem(L['vivitta_bhajati'])}: vị ấy lui tới chỗ ở thanh vắng này, lui tới thường xuyên, gần gũi, gần gũi "
     f"thường xuyên, gần gũi trọn vẹn. {tena(L['vivitta_bhajati'])}"),
    ('"Arañña"nti', f"{lem('rừng')}: sau khi đi ra ngoài cột trụ ở cổng làng, tất cả nơi ấy đều là rừng."),
    ('"Rukkhamūla"nti',
     f"{lem('gốc cây')}: gốc cây chính là gốc cây. Núi chính là núi. Khe núi chính là khe núi. Hang núi chính là "
     "hang núi. Bãi tha ma chính là bãi tha ma. Khoảng trời trống chính là khoảng trời trống. Đống rơm chính là "
     "đống rơm."),
    ('"Vanapattha"nti dūrā',
     " ".join(f"{lem('rừng sâu')}: đây là tên gọi của những chỗ ở {x}." for x in (
         "xa xôi", "trong lùm rừng", "đáng sợ [khác chính tả (Sī., Syā.): bhiṃsanakānametaṃ]", "làm sởn tóc gáy",
         "ở vùng biên", "không có người qua lại", "khó chịu đựng"))),
    ('"Appasadda"nti',
     f"{lem('ít tiếng động')}: chỗ ở dù ở gần, nhưng không bị người tại gia và người xuất gia chen chúc. Vì thế nơi "
     "ấy ít tiếng động. Chỗ ở dù ở xa, nhưng không bị người tại gia và người xuất gia chen chúc. Vì thế nơi ấy ít "
     "tiếng động."),
    ('"Appanigghosa"nti',
     f"{lem('ít ồn ào')}: nơi nào ít tiếng động thì chính nơi ấy ít ồn ào. Nơi nào ít ồn ào thì chính nơi ấy vắng "
     "hơi người. Nơi nào vắng hơi người thì chính nơi ấy kín đáo với người đời. Nơi nào kín đáo với người đời thì "
     "chính nơi ấy thích hợp cho sự độc cư."),
    ('"Araññagato',
     f"{lem(L['gato'])}: vị ấy là người đã đi đến rừng, hoặc đã đi đến gốc cây, hoặc đã đi đến ngôi nhà trống."),
    ('"Nisīdati', f"{lem(L['nisidati'])}: vị ấy đã ngồi, xếp chân kiết già."),
    ('"Ujuṃ', f"{lem(L['uju'])}: thân ngay thẳng, được giữ vững, được đặt đúng cách."),
    ('"Parimukhaṃ',
     f"{lem(L['parimukha'])}: {low(qa('sự tỉnh thức', SATI_PE3))} Sự tỉnh thức này được thiết lập, được thiết lập "
     f"vững chắc nơi chóp mũi hoặc nơi vùng miệng. {tena(L['parimukha'])}"),
    ('"Abhijjhaṃ loke pahāyā"ti', f"{lem(L['abhijjha'])}: {low(ABHIJJHA_Q)}"),
    ("Tattha katamo loko?",
     f"{q('thế gian')} Năm khối {F.UPK} là thế gian {DASH} {called('thế gian')}. Sự thèm muốn này đối với thế gian "
     f"này {SANTA}. {tena(L['abhijjha'])}"),
    ('"Vigatābhijjhena',
     f"{lem(L['vigatabhijjha'])}: {low(citta_qa())} Tâm này đã lìa sự thèm muốn. {tena(L['vigatabhijjha'])}"),
    ('"Viharatī"ti iriyati', viharati_full(False)),
    ('"Abhijjhāya cittaṃ parisodhetī"ti', f"{lem(L['abhijjhaya'])}: {low(ABHIJJHA_Q)}"),
    ("Tattha katamaṃ cittaṃ? Yaṃ cittaṃ", f"{citta_qa()} {sodheti('sự thèm muốn')} {tena(L['abhijjhaya'])}"),
    ('"Byāpādapadosaṃ pahāyā"ti', f"{lem(L['byapada'])}: có ác ý, có sự sân hận dữ dội."),
    ("Tattha katamo byāpādo? Yo cittassa āghāto paṭighāto", qa("ác ý", DOSA_VAR)),
    ("Tattha katamo padoso? Yo byāpādo so padoso, yo padoso so byāpādo. Iti",
     f"{q('sự sân hận dữ dội')} {PADOSA} Như vậy, ác ý này và sự sân hận dữ dội này {SANTA}. {tena(L['byapada'])}"),
    ('"Abyāpannacitto"ti',
     f"{lem(L['abyapanna'])}: {low(citta_qa())} Tâm này không có ác ý. {tena(L['abyapanna'])}"),
    ('"Viharatī"ti', viharati_pe(False)),
    ('"Byāpādapadosā cittaṃ parisodhetī"ti', f"{lem(L['byapadapadosa'])}. Có ác ý, có sự sân hận dữ dội."),
    ("Tattha katamo byāpādo? Yo cittassa āghāto…pe…", qa("ác ý", DOSA_PE)),
    ("Tattha katamo padoso?", f"{q('sự sân hận dữ dội')} {PADOSA}"),
    ("Tattha katamaṃ cittaṃ? Yaṃ cittaṃ",
     f"{citta_qa()} {sodheti('ác ý và sự sân hận dữ dội')} {tena(L['byapadapadosa'])}"),
    ('"Thinamiddhaṃ pahāyā"ti', f"{lem(L['thina'])}: có sự uể oải [khác chính tả (Sī., Syā.): thīnaṃ], có sự đờ đẫn."),
    ("Tattha katamaṃ thinaṃ? Yā cittassa", THINA_Q),
    ("Tattha katamaṃ middhaṃ? Yā kāyassa",
     f"{MIDDHA_Q} Như vậy, sự uể oải này và sự đờ đẫn này {SANTA}. {tena(L['thina'])}"),
    ('"Vigatathinamiddho"ti.',
     f"{lem(L['vigatathina'])}. Vì sự uể oải và đờ đẫn ấy {CATTA}. {tena(L['vigatathina'])}"),
    ('"Viharatī"ti', viharati_pe(False)),
    ('"Ālokasaññī"ti.',
     f"{lem(L['aloka'])}. {qa('tri giác', SANNA3)} Tri giác này sáng sủa, được khai mở, trong sạch, sáng tỏ. "
     f"{tena(L['aloka'])}"),
    ('"Sato sampajāno"ti.', f"{lem(L['sato'])}. {SATI_Q}"),
    ("Tattha katamaṃ sampajaññaṃ? Yā paññā pajānanā…pe…",
     f"{SAMP_Q} {iti_upeto('sự tỉnh thức', 'sự hiểu biết rõ ràng')} {tena(L['sato'])}"),
    ('"Thinamiddhā cittaṃ parisodhetī"ti.', f"{lem(L['thinamiddha'])}. Có sự uể oải, có sự đờ đẫn."),
    ("Tattha katamaṃ thinaṃ…pe…", qpe("sự uể oải")),
    ("Tattha katamaṃ middhaṃ…pe…", qpe("sự đờ đẫn")),
    ("Tattha katamaṃ cittaṃ…pe…", f"{qpe('tâm')} {sodheti('sự uể oải và đờ đẫn')} {tena(L['thinamiddha'])}"),
    ('"Uddhaccakukkuccaṃ pahāyā"ti', f"{lem(L['uddhacca'])}: có sự xao động, có sự hối tiếc."),
    ("Tattha katamaṃ uddhaccaṃ?", UDDHACCA_Q),
    ("Tattha katamaṃ kukkuccaṃ? Akappiye",
     f"{q('sự hối tiếc')} {KUKKUCCA_A}, điều mà thuộc loại như vậy là {KUKKUCCA_B} {DASH} {called('sự hối tiếc')}. "
     f"Như vậy, sự xao động này và sự hối tiếc này {SANTA}. {tena(L['uddhacca'])}"),
    ('"Anuddhato"ti',
     f"{lem(L['anuddhato'])}: vì sự xao động và hối tiếc ấy {CATTA}. {tena(L['anuddhato'])}"),
    ('"Viharatī"ti', viharati_pe(False)),
    ('"Vūpasantacitto"ti.',
     f"{lem(L['vupasanta'])}. {citta_qa()} Tâm này ở nơi bản thân đã lắng yên, đã được làm lắng dịu, đã lắng dịu "
     f"hoàn toàn. {tena(L['vupasanta_full'])}"),
    ('"Uddhaccakukkuccā cittaṃ parisodhetī"ti', f"{lem(L['uddhaccakukkucca'])}: có sự xao động, có sự hối tiếc."),
    ("Tattha katamaṃ uddhaccaṃ?", UDDHACCA_Q),
    ("Tattha katamaṃ kukkuccaṃ…pe…", qpe("sự hối tiếc")),
    ("Tattha katamaṃ cittaṃ…pe…", f"{qpe('tâm')} {sodheti('sự xao động và hối tiếc')} {tena(L['uddhaccakukkucca'])}"),
    ('"Vicikicchaṃ pahāyā"ti',
     f"{lem(L['vicikiccha'])}: {low(qa('sự hoài nghi', VICI))} Sự hoài nghi này {SANTA}. {tena(L['vicikiccha'])}"),
    ('"Tiṇṇavicikiccho"ti',
     f"{lem(L['tinna'])}: vị ấy đã vượt qua sự hoài nghi này, đã vượt lên, đã vượt thoát, đã sang bờ bên kia, "
     f"đã đến được bờ bên kia. {tena(L['tinna'])}"),
    ('"Akathaṃkathī',
     f"{lem(L['akathamkathi'])}: đối với các hiện tượng thiện, vị ấy không nghi ngờ, không hoài nghi bằng sự hoài "
     f"nghi này; là người không còn băn khoăn, hết băn khoăn, lìa băn khoăn. {tena(L['akathamkathi'])}"),
    ('"Vicikicchāya cittaṃ parisodhetī"ti', f"{lem(L['vicikicchaya'])}: {low(qa('sự hoài nghi', VICI_SHORT))}"),
    ("Tattha katamaṃ cittaṃ? Yaṃ cittaṃ", f"{citta_qa()} {sodheti('sự hoài nghi')} {tena(L['vicikicchaya'])}"),
    ('"Ime pañca nīvaraṇe pahāyā"ti',
     f"{lem(L['pancanivarana'])}: năm chướng ngại này {SANTA}. {tena(L['pancanivarana'])}"),
    ('"Cetaso upakkilese"ti', f"{lem(L['upakkilesa'])}: năm chướng ngại này là những thứ làm vẩn đục tâm."),
    ('"Paññāya dubbalīkaraṇe"ti',
     f"{lem(L['dubbali'])}: do năm chướng ngại này mà trí tuệ chưa sinh khởi thì không sinh khởi, và trí tuệ đã sinh "
     f"khởi thì chấm dứt. {tena(L['dubbali'])}"),
    ('"Vivicceva kāmehi vivicca akusalehi dhammehī"ti',
     f"{lem(LJ['vivicca'])}: ở đây, các dục lạc là gì? {KAMA6} {DASH} {called('các dục lạc')}."),
    ("Tattha katame akusalā dhammā?",
     f"{q('các hiện tượng bất thiện')} {FIVE_HIND} {DASH} {called('các hiện tượng bất thiện')}. Như vậy, vị ấy tách "
     f"khỏi các dục lạc này và các hiện tượng bất thiện này. {tena(LJ['vivicca'])}"),
    ('"Savitakkaṃ savicāra"nti', f"{lem(LJ['savitakka'])}: có sự hướng tâm, có sự duy trì tâm."),
    ("Tattha katamo vitakko? Yo takko vitakko saṅkappo", VITAKKA_Q),
    ("Tattha katamo vicāro? Yo cāro vicāro",
     f"{qa('sự duy trì tâm', VICARA, quoted=False)} {iti_upeto('sự hướng tâm', 'sự duy trì tâm')} "
     f"{tena(LJ['savitakka'])}"),
    ('"Vivekaja"nti',
     f"{lem(LJ['vivekaja'])}: sự hướng tâm, sự duy trì tâm, sự hân hoan, hạnh phúc, sự nhất tâm {DASH} những điều ấy "
     f"{JATA} trong sự tách biệt này. {tena(LJ['vivekaja'])}"),
    ('"Pītisukha"nti', f"{lem(LJ['pitisukha'])}: có sự hân hoan, có hạnh phúc."),
    ("Tattha katamā pīti? Yā pīti", PITI_Q),
    ("Tattha katamaṃ sukhaṃ? Yaṃ cetasikaṃ",
     f"{SUKHA_Q} Hạnh phúc này có sự hân hoan này đi kèm, cùng sinh với nó, hòa lẫn với nó, gắn liền với nó. "
     f"{tena(LJ['pitisukha'])}"),
    ('"Paṭhama"nti', None),   # filled below (variant)
    ('"Jhāna"nti vitakko', f"{lem('tầng thiền')}: sự hướng tâm, sự duy trì tâm, sự hân hoan, hạnh phúc, sự nhất tâm."),
    ('"Upasampajjā"ti yo paṭhamassa', upasampajja(JH["paṭhamaṃ"])),
    ('"Viharatī"ti', viharati_pe(True)),
    ('"Vitakkavicārānaṃ vūpasamā"ti', f"{lem(LJ['vitakkavicara'])}: có sự hướng tâm, có sự duy trì tâm."),
    ("Tattha katamo vitakko? Yo takko vitakko…pe…", VITAKKA_Q_PE),
    ("Tattha katamo vicāro? Yo cāro vicāro anuvicāro",
     f"{qa('sự duy trì tâm', VICARA)} Như vậy, sự hướng tâm này và sự duy trì tâm này {SANTA}. "
     f"{tena(LJ['vitakkavicara'])}"),
    ('"Ajjhatta"nti', f"{lem(LJ['ajjhatta'])}: điều mà ở nơi bản thân, riêng từng người."),
    ('"Sampasādana"nti', f"{lem(LJ['sampasadana'])}: điều mà là {SADDHA4}."),
    ('"Cetaso ekodibhāva"nti', f"{lem(LJ['ekodi'])}: điều mà là {SAMADHI_PE1}."),
    ('"Avitakkaṃ avicāra"nti', f"{lem(LJ['avitakka'])}: có sự hướng tâm, có sự duy trì tâm."),
    ("Tattha katamo vitakko? Yo takko vitakko…pe…", VITAKKA_Q_PE),
    ("Tattha katamo vicāro? Yo cāro anucāro",
     f"{qa('sự duy trì tâm', VICARA_ANU)} Như vậy, sự hướng tâm này và sự duy trì tâm này {SANTA}. "
     f"{tena(LJ['avitakka'])}"),
    ('"Samādhija"nti',
     f"{lem(LJ['samadhija'])}: sự trong sáng, sự hân hoan và hạnh phúc {DASH} những điều ấy {JATA} trong định tâm "
     f"này. {tena(LJ['samadhija'])}"),
    ('"Pītisukha"nti', f"{lem(LJ['pitisukha'])}: có sự hân hoan, có hạnh phúc."),
    ("Tattha katamā pīti…pe…", qpe("sự hân hoan")),
    ("Tattha katamaṃ sukhaṃ…pe…",
     f"{qpe('hạnh phúc')} Hạnh phúc này có sự hân hoan này đi kèm, cùng sinh với nó, hòa lẫn với nó, gắn liền với "
     f"nó. {tena(LJ['pitisukha'])}"),
    ('"Dutiya"nti', None),
    ('"Jhāna"nti sampasādo', f"{lem('tầng thiền')}: sự trong sáng, sự hân hoan và hạnh phúc, sự nhất tâm."),
    ('"Upasampajjā"ti yo dutiyassa', upasampajja(JH["dutiyaṃ"])),
    ('"Viharatī"ti', viharati_pe(True)),
    ('"Pītiyā ca virāgā"ti',
     f"{lem(LJ['pitiya'])}: {low(PITI_Q)} Sự hân hoan này {SANTA}. {tena(LJ['pitiya'])}"),
    ('"Upekkhako"ti',
     f"{lem(LJ['upekkhako'])}: {low(UPEK_Q)} Với sự bình thản này, {UPETO_PE}. {tena(LJ['upekkhako'])}"),
    ('"Viharatī"ti', viharati_pe(True)),
    ('"Sato ca sampajāno"ti', f"{lem(LJ['sato_ca'])}: {low(SATI_Q)}"),
    ("Tattha katamaṃ sampajaññaṃ?",
     f"{SAMP_Q} {iti_upeto('sự tỉnh thức', 'sự hiểu biết rõ ràng')} {tena(LJ['sato_ca'])}"),
    ('"Sukhañca kāyena paṭisaṃvedetī"ti', f"{lem(LJ['sukhanca'])}: {low(SUKHA_Q)}"),
    ("Tattha katamo kāyo?",
     f"{q('thân')} {cap(S.AGG['sanna']['khandha'])}, {S.AGG['sankhara']['khandha']}, "
     f"{S.AGG['vinnana']['khandha']} {DASH} {called('thân')}. Vị ấy cảm nhận hạnh phúc này bằng thân này. "
     f"{tena(LJ['sukhanca'])}"),
    ('"Yaṃ taṃ ariyā ācikkhantī"ti',
     f"{lem(LJ['ariya'])}: ở đây, các bậc thánh là ai? Các Đức Phật và các đệ tử của Đức Phật được gọi là các bậc "
     "thánh. Các vị ấy mô tả, thuyết giảng, trình bày [khác chính tả (Sī., Syā.): paññāpenti], xác lập, khai mở, "
     f"phân tích, làm sáng tỏ, công bố điều này. {tena(LJ['ariya'])}"),
    ('"Upekkhako satimā sukhavihārī"ti', f"{lem(LJ['usv'])}: {low(UPEK_Q)}"),
    ("Tattha katamā sati? Yā sati anussati…pe…", SATI_Q),
    ("Tattha katamaṃ sukhaṃ? Yaṃ cetasikaṃ",
     f"{SUKHA_Q} Như vậy, được trang bị sự bình thản này, sự tỉnh thức này và hạnh phúc này, {IRIYATI_JH}. "
     f"{tena(LJ['usv'])}"),
    ('"Tatiya"nti', None),
    ('"Jhāna"nti upekkhā, sati, sampajaññaṃ',
     f"{lem('tầng thiền')}: sự bình thản, sự tỉnh thức, sự hiểu biết rõ ràng, hạnh phúc, sự nhất tâm."),
    ('"Upasampajjā"ti yo tatiyassa', upasampajja(JH["tatiyaṃ"])),
    ('"Viharatī"ti', viharati_pe(True)),
    ('"Sukhassa ca pahānā dukkhassa ca pahānā"ti', f"{lem(LJ['sukhassa'])}: có sự dễ chịu, có sự khó chịu."),
    ("Tattha katamaṃ sukhaṃ? Yaṃ kāyikaṃ", qa("sự dễ chịu", FEEL["sukha"])),
    ("Tattha katamaṃ dukkhaṃ?",
     f"{qa('sự khó chịu', FEEL['dukkha'])} Như vậy, sự dễ chịu này và sự khó chịu này {SANTA}. "
     f"{tena(LJ['sukhassa'])}"),
    ('"Pubbeva somanassadomanassānaṃ atthaṅgamā"ti', f"{lem(LJ['pubbeva'])}: có niềm vui, có nỗi buồn."),
    ("Tattha katamaṃ somanassaṃ?", qa("niềm vui", FEEL["somanassa"])),
    ("Tattha katamaṃ domanassaṃ?",
     f"{qa('nỗi buồn', FEEL['domanassa'])} Như vậy, niềm vui này và nỗi buồn này từ trước {SANTA}. "
     f"{tena(LJ['pubbeva'])}"),
    ('"Adukkhamasukha"nti', f"{lem(LJ['adm'])}: điều mà là {FEEL['upekkha']}. {tena(LJ['adm'])}"),
    ('"Upekkhāsatipārisuddhi"nti', f"{lem(LJ['upekkhasati'])}: {low(UPEK_Q)}"),
    ("Tattha katamā sati? Yā sati anussati…pe…",
     f"{SATI_Q} Sự tỉnh thức này nhờ sự bình thản này mà được khai mở, trong sạch, sáng tỏ. "
     f"{tena(LJ['upekkhasati'])}"),
    ('"Catuttha"nti', None),
    ('"Jhāna"nti upekkhā, sati, cittassekaggatā', f"{lem('tầng thiền')}: sự bình thản, sự tỉnh thức, sự nhất tâm."),
    ('"Upasampajjā"ti yo catutthassa', upasampajja(JH["catutthaṃ"])),
    ('"Viharatī"ti', viharati_pe(True)),
    ('"Sabbaso rūpasaññānaṃ',
     f"{lem(LJ['rupasanna'])}: ở đây, tri giác về hình sắc là gì? {cap(SANNA3)} "
     + SAMAPANNA3.format("sự chứng đạt thuộc cõi hình sắc")
     + f" {DASH} {called('các tri giác về hình sắc')}. Vị ấy {ATIKKANTO} các tri giác về hình sắc này. "
     f"{tena(LJ['rupasanna'])}"),
    ('"Paṭighasaññānaṃ',
     f"{lem(LJ['patigha'])}: ở đây, tri giác về sự va chạm là gì? Tri giác về hình sắc, tri giác về âm thanh… "
     f"tri giác về vật xúc chạm {DASH} {called('các tri giác về sự va chạm', False)}. Các tri giác về sự va chạm "
     f"này {SANTA}. {tena(LJ['patigha'])}"),
    ('"Nānattasaññānaṃ',
     f"{lem(LJ['nanatta'])}: ở đây, tri giác về sự đa dạng là gì? {cap(SANNA3)} của người chưa chứng nhập, có yếu tố "
     f"ý hoặc có yếu tố ý thức {DASH} {called('các tri giác về sự đa dạng')}. Vị ấy không chú tâm đến các tri giác về "
     f"sự đa dạng này. {tena(LJ['nanatta'])}"),
    ('"Ananto ākāso"ti',
     f"{lem(THOUGHT['ananto ākāso'])}: {low(qa('không gian', AKASA[0].lower() + AKASA[1:]))} Vị ấy đặt tâm, đặt "
     f"tâm vững chắc vào không gian ấy, lan tỏa vô tận. {tena(low(THOUGHT['ananto ākāso']))}"),
]
for _x in ("tri giác về hình sắc", "tri giác về âm thanh", "tri giác về vật xúc chạm"):
    assert _x in F.SUBJ4.values(), _x


def ayatana_lines(key, nxt):
    """"X"nti … cittacetasikā dhammā / "Upasampajjā"ti / "Viharatī"ti…pe… / "Sabbaso X samatikkammā"ti …"""
    n = NAMES_AYAT[key]
    out = [(f'"{nxt[0]}"nti', f"{lem(n)}: {CITTA_CETASIKA} {SAMAPANNA3.format(n)}."),
           (f'"Upasampajjā"ti yo {nxt[1]}', upasampajja(n)),
           ('"Viharatī"ti', viharati_pe(True))]
    return out


HAND12 += ayatana_lines("ākāsānañcāyatana", ("Ākāsānañcāyatana", "ākāsānañcāyatanassa"))
HAND12 += [
    ('"Sabbaso ākāsānañcāyatanaṃ samatikkammā"ti',
     f"{lem(BEYOND['ākāsānañcāyatana'])}: vị ấy {ATIKKANTO} {NAMES_AYAT['ākāsānañcāyatana']} này. "
     f"{tena(BEYOND['ākāsānañcāyatana'])}"),
    ('"Anantaṃ viññāṇa"nti',
     f"{lem(THOUGHT['anantaṃ viññāṇa'])}: vị ấy chú tâm đến chính không gian ấy đã được thức chạm đến, lan tỏa vô tận. "
     f"{tena(low(THOUGHT['anantaṃ viññāṇa']))}"),
]
HAND12 += ayatana_lines("viññāṇañcāyatana", ("Viññāṇañcāyatana", "viññāṇañcāyatanassa"))
HAND12 += [
    ('"Sabbaso viññāṇañcāyatanaṃ',
     f"{lem(BEYOND['viññāṇañcāyatana'])}: vị ấy {ATIKKANTO} {NAMES_AYAT['viññāṇañcāyatana']} này. "
     f"{tena(BEYOND['viññāṇañcāyatana'])}"),
    ('"Natthi kiñcī"ti',
     f"{lem(THOUGHT['natthi kiñcī'])}: vị ấy tu tập, làm cho tan biến, làm cho biến mất chính thức ấy, thấy rằng "
     f"“{THOUGHT['natthi kiñcī']}”. {tena(low(THOUGHT['natthi kiñcī']))}"),
]
HAND12 += ayatana_lines("ākiñcaññāyatana", ("Ākiñcaññāyatana", "ākiñcaññāyatanassa"))
NEVASANNI = "không phải có tri giác cũng không phải không có tri giác"     # nevasaññīnāsaññī [new; ch6 pattern]
HAND12 += [
    ('"Sabbaso ākiñcaññāyatanaṃ',
     f"{lem(BEYOND['ākiñcaññāyatana'])}: vị ấy {ATIKKANTO} {NAMES_AYAT['ākiñcaññāyatana']} này. "
     f"{tena(BEYOND['ākiñcaññāyatana'])}"),
    ('"Nevasaññīnāsaññī"ti',
     f"{lem(NEVASANNI)}: vị ấy chú tâm đến chính {NAMES_AYAT['ākiñcaññāyatana']} ấy như là điều an tịnh, tu tập sự "
     f"chứng đạt còn sót lại các sự tạo tác. {TENA} “{NEVASANNI}” [đoạn văn này không có trong ma trận, nhưng có "
     "trong phần giải thích ở tất cả các bản chép tay]."),
]
HAND12 += ayatana_lines("nevasaññānāsaññāyatana", ("Nevasaññānāsaññāyatana", "nevasaññānāsaññāyatanassa"))[:2]
HAND12 += [('"Viharatī"ti iriyati', viharati_full(True))]


def _fill_nth():
    for i, (p, v) in enumerate(HAND12):
        if v is None:
            o = {'"Paṭhama"nti': "paṭhamaṃ", '"Dutiya"nti': "dutiyaṃ", '"Tatiya"nti': "tatiyaṃ",
                 '"Catuttha"nti': "catutthaṃ"}[p]
            w = ORD[o]
            var = GANANA_VAR if o == "paṭhamaṃ" else ""
            sep = ", vị ấy" if o == "catutthaṃ" else ". Vị ấy"            # ^2-598 comma (as written)
            HAND12[i] = (p, f"{lem(w)}: {w} theo thứ tự đếm{var}{sep} chứng nhập điều này {w}, nên gọi là {w}.")


_fill_nth()

# ================================================================ 8. labels
SEC = S.SECTION_TITLES
LABELS = {}
for _k, _v in SEC.items():
    LABELS["#### " + _k] = "#### " + _v
    LABELS[_k + "."] = _v + "."
LABELS["##### Tikaṃ"] = B.LABELS["##### Tikaṃ"]
LABELS["##### Dukaṃ"] = B.LABELS["##### Dukaṃ"]
for _n, _p in ((10, "Bojjhaṅgavibhaṅgo"), (11, "Maggaṅgavibhaṅgo"), (12, "Jhānavibhaṅgo")):
    LABELS["### " + _p] = "### " + S.CHAPTER_TITLES[_n]
    LABELS[_p + " niṭṭhito."] = S.CHAPTER_CLOSING.format(title=S.CHAPTER_TITLES[_n])
HEAD12 = {"Mātikā": G.HEAD["Mātikā"],
          "Rūpāvacarakusalaṃ": "Tâm thiện thuộc cõi hình sắc", "Arūpāvacarakusalaṃ": "Tâm thiện thuộc cõi không hình sắc",
          "Lokuttarakusalaṃ": "Tâm thiện vượt thế gian",
          "Rūpāvacaravipākā": "Quả của nghiệp thuộc cõi hình sắc",
          "Arūpāvacaravipākā": "Quả của nghiệp thuộc cõi không hình sắc",
          "Lokuttaravipākā": "Quả của nghiệp vượt thế gian",
          "Rūpārūpāvacarakiriyā": "Tâm mang tính chức năng thuộc cõi hình sắc và cõi không hình sắc"}   # [pi-1 headings]
for _k, _v in HEAD12.items():
    LABELS["##### " + _k] = "##### " + _v
    if _k != "Rūpārūpāvacarakiriyā":
        in_pi1(_v)
in_pi1("Tâm mang tính chức năng thuộc cõi hình sắc", "Tâm mang tính chức năng thuộc cõi không hình sắc")
LABELS["Catukkaṃ."] = "Phương pháp chia bốn."                               # [pi-1 Catukkanayo ^1-166]
LABELS["Pañcakaṃ."] = "Phương pháp chia năm."                               # [pi-1 Pañcakanayo ^1-175]
in_pi1(LABELS["Catukkaṃ."], LABELS["Pañcakaṃ."])
_BJ_PALI = ", ".join(k + "sambojjhaṅgo" for k in BJ_ORDER)
LABELS[f"Satta bojjhaṅgā – {_BJ_PALI}."] = f"{cap(SATTA_BJ)} {DASH} " + T.listing([BJ[k] for k in BJ_ORDER]) + "."
LABELS["Satta bojjhaṅgā – satisambojjhaṅgo…pe… upekkhāsambojjhaṅgo."] = \
    f"{cap(SATTA_BJ)} {DASH} {BJ['sati']}… {BJ['upekkhā']}."
_P8 = "sammādiṭṭhi, sammāsaṅkappo, sammāvācā, sammākammanto, sammāājīvo, sammāvāyāmo, sammāsati, sammāsamādhi"
LABELS[f"Ariyo aṭṭhaṅgiko maggo, seyyathidaṃ – {_P8}."] = f"{cap(ARIYA8)}, cụ thể là {DASH} {F.PATH8}."
assert f"{ARIYA8}, cụ thể là {DASH} {F.PATH8}" in [v for p, v in F.HAND4 if p.startswith("Tattha katamaṃ dukkhanirodhagāminī")][0]
LABELS[f"Aṭṭhaṅgiko maggo – {_P8}."] = f"{cap(MAGGA8)} {DASH} {F.PATH8}."
LABELS["Aṭṭhaṅgiko maggo – sammādiṭṭhi…pe… sammāsamādhi."] = \
    f"{cap(MAGGA8)} {DASH} {FN['sammādiṭṭhi']}… {FN['sammāsamādhi']}."
LABELS["Pañcaṅgiko maggo – sammādiṭṭhi, sammāsaṅkappo, sammāvāyāmo, sammāsati, sammāsamādhi."] = \
    f"{cap(MAGGA5)} {DASH} {F.PATH5}."
LABELS["Cattāri jhānāni – paṭhamaṃ jhānaṃ, dutiyaṃ jhānaṃ, tatiyaṃ jhānaṃ, catutthaṃ jhānaṃ."] = \
    f"Bốn tầng thiền {DASH} " + T.listing([JH[k] for k in ("paṭhamaṃ", "dutiyaṃ", "tatiyaṃ", "catutthaṃ")]) + "."
LABELS[("Cattāri jhānāni – idha bhikkhu vivicceva kāmehi vivicca akusalehi dhammehi savitakkaṃ savicāraṃ vivekajaṃ "
        "pītisukhaṃ paṭhamaṃ jhānaṃ upasampajja viharati…pe… vitakkavicārānaṃ vūpasamā ajjhattaṃ sampasādanaṃ cetaso "
        "ekodibhāvaṃ avitakkaṃ avicāraṃ samādhijaṃ pītisukhaṃ dutiyaṃ jhānaṃ upasampajja viharati…pe… pītiyā ca "
        "virāgā upekkhako ca viharati sato ca sampajāno sukhañca kāyena paṭisaṃvedeti, yaṃ taṃ ariyā ācikkhanti – "
        "\"upekkhako satimā sukhavihārī\"ti tatiyaṃ jhānaṃ upasampajja viharati…pe… sukhassa ca pahānā dukkhassa ca "
        "pahānā pubbeva somanassadomanassānaṃ atthaṅgamā adukkhamasukhaṃ upekkhāsatipārisuddhiṃ catutthaṃ jhānaṃ "
        "upasampajja viharati.")] = (f"Bốn tầng thiền {DASH} {low(IDHA)}, {BHIKKHU} {J1}… {J2V}… {J3V}… {J4V}.")
for _pa, _tot, _unit in (("Sattannaṃ bojjhaṅgānaṃ", SATTA_BJ, "chi phần giác ngộ"),
                         ("Aṭṭhannaṃ maggaṅgānaṃ", "tám chi phần của con đường", "chi phần của con đường"),
                         ("Catunnaṃ jhānānaṃ", "bốn tầng thiền", "tầng thiền")):
    LABELS[f"{_pa} kati kusalā, kati akusalā, kati abyākatā…pe… kati saraṇā, kati araṇā?"] = T.question_q(_tot, _unit)

# ================================================================ 9. build
CHAPTERS = (("10-bojjhangavibhango.md", 10, HAND10), ("11-maggangavibhango.md", 11, HAND11),
            ("12-jhanavibhango.md", 12, HAND12))


def translate(pali_lines, ch, hand):
    hand = list(hand)
    out, section = [], "sutta"
    for pl in pali_lines:
        if not pl.strip():
            out.append("")
            continue
        m = S.ID.search(pl)
        t = S.ID.sub("", pl).rstrip()
        if NOSPACE.search(t):
            SLIPS.append("space before …pe…: " + t[max(0, NOSPACE.search(t).start() - 25):][:45])
        if t.startswith("#### "):
            section = {"Suttantabhājanīyaṃ": "sutta", "Abhidhammabhājanīyaṃ": "abhi", "Pañhāpucchakaṃ": "q"}[t[5:]]
        if t in LABELS:
            vi = LABELS[t]
        elif section == "sutta" and hand and t.startswith(hand[0][0]):
            vi = hand.pop(0)[1]
        elif section == "q":
            vi = QQ[ch].line(t)
        else:
            vi = abhi_line(t)
        assert pl.count(DASH) + pl.count("—") == vi.count(DASH) and "—" not in vi, ("dash count", t[:70], vi[:90])
        for bad in ("là là", "  ", "….", '"', " ,", " .", ":-", "thì thì", "\x01", " ;", ";;", ",,", "chánh niệm",
                    "..", ", ,", "None"):
            assert bad not in vi, (bad, vi[:160])
        out.append(vi + (" " + m.group(1) if m else ""))
    assert not hand, [h[0] for h in hand]
    return out


HAND_SLIPS = [   # slips inside hand lines (rendered as meant: spelling / punctuation only; or kept as written)
    "^2-508 'ākiñcāyatanaṃ' -> 'ākiñcaññāyatanaṃ' (spelling, as meant)",
    "^2-517 'Ñatvādhikaraṇamenaṃ' -> 'Yatvādhikaraṇamenaṃ' (spelling, as meant; pi-1 ^1-1354 Vietnamese)",
    "^2-518 '\"bhojane amattaññutā\"ti.' (closing ti dropped, punctuation)",
    "^2-523 '…sampajānakārī hotīti.' (closing ti dropped, punctuation); bare 'sato sampajānakārī hoti' after "
    "'pasāreti' kept as written",
    "^2-525 last clause 'tuṇhībhāve sampajānakārī hoti' without 'sato' (as written)",
    "^2-545 'Atthi byāpādo atthi padoso.' (comma added)",
    "^2-560 short vicikicchā list without …pe… (as written)",
    "^2-564 'rāgo kāmo' twice (as written); ^2-565 'ayaṃ vuccati vicāro' and ^2-603 'imā vuccanti paṭighasaññāyo' "
    "unquoted (as written); ^2-576 'anucāro' (only here) and 'santā hoti' with two subjects (as written)",
    "^2-598 comma instead of a full stop (as written)",
    "^2-615 'taṃyeva viññāṇaṃ bhāveti vibhāveti antarabhāveti' (bhāveti as written, «tu tập»)",
]


def build():
    SLIPS.extend(HAND_SLIPS)
    n = check_openings()
    check_pi1_conduct()
    res = {}
    for fn, ch, hand in CHAPTERS:
        pali = open(os.path.join(S.PALI_DIR, fn), encoding="utf-8").read().rstrip("\n").split("\n")
        res[os.path.join(S.VI_DIR, fn)] = translate(pali, ch, hand)
    return res, n


def main():
    res, n = build()
    for path, lines in res.items():
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write("\n".join(lines).rstrip("\n") + "\n")
        print("OK:", path, "|", len([l for l in lines if l.strip()]), "non-empty lines")
    print("pi-1 openings / result clauses recomposed:", n)
    for s in sorted(set(SLIPS)):
        print("slip:", s)


if __name__ == "__main__":
    main()
