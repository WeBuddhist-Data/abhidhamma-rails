"""Build the Vietnamese plain zero-shot of pi-1 parts 4-02 and 4-03 (Nikkhepakaṇḍa: summary of the flood, yoke,
hindrance, misapprehension groups, long intermediate pairs, clinging, defilement and closing pairs, and of the
discourse pairs; ^1-3-2-6-0 … ^1-1383).

usage: python -I -X utf8 build_4-02_4-03_vi.py      (checks, then writes both parts)

Importing this file does NOT build anything.
Method: build_4-01_vi (G) is imported unchanged, and through it build_matika_vi (M), build_ch2_01_sample_vi (C),
build_3-01_vi (R), build_3-02_3-03_vi (X) and the 2-0x builders (B, D, E, F). Segment-level translation with fixed
formula strings (structure as ../pi-1-ru/build_4-02_4-03_ru.py). Every matrix item, question and answer comes from
M.QUESTION / M.ANSWER / M.BARE / M.PRED; the 4-01 frames (QB, TQ, TA, NO_X, NIYA, AMONG_*, VIPP_SAS, BHUMI …),
lists (spheres, aggregates, «toàn bộ vật chất», paths) and strings (lobha, dosa, moha, diṭṭhi, kaṅkhā, kāma, bhava,
māna, sakkāya, sīlabbata) are reused, never retyped. Where a 4-02 segment has the same Pāli words as a 4-01 one,
the Vietnamese is asserted equal to the 4-01 Vietnamese. Per line the build asserts the Pāli count of «–», «?»,
«[» and «…pe…» (= «…»).
"""
import importlib, pathlib, re, sys, unicodedata

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
G = importlib.import_module("build_4-01_vi")   # importing does not write
M, C, R, X = G.M, G.C, G.R, G.X
B, D, E, F = G.B, G.D, G.E, G.F

PARTS = ("4-02-nikkhepakandam.md", "4-03-nikkhepakandam.md")
PALI_DIR, OUT_DIR = B.PALI_DIR, B.OUT_DIR
TERMS = HERE / "vi-zeroshot-terms.md"
DASH, ELL = G.DASH, G.ELL
cap, P2, Q, QB, ANS, TQ, TA = G.cap, G.P2, G.Q, G.QB, G.ANS, G.TQ, G.TA
DH = M.DH

# =========================================================================================
# 0. The 4-01 Vietnamese of segments whose Pāli words recur here
# =========================================================================================
V401 = dict(G.SEGMENTS)
P401 = dict(G.pali_segments())


def body401(bid):
    """the answer body of a 4-01 'Katame dhammā X? <body> – ime dhammā X.' segment"""
    v = V401[bid][0]
    return v.split("? ", 1)[1].rsplit(f" {DASH} đây là ", 1)[0]


def words(s):
    """Pāli words only (punctuation ignored), for 'same Pāli' assertions"""
    return re.findall(r"[^\W\d_]+", s.replace("…pe…", " PE ").lower())


# =========================================================================================
# 1. Headings and closing lines (headings verbatim from vi-zeroshot-terms.md)
# =========================================================================================
HEAD = {"#### Suttantikadukanikkhepaṃ": "#### Tóm lược các bộ đôi theo kinh"}
GROUP_HEAD = {
    "##### Oghagocchakaṃ": M.GROUPS["1-M-2-6-0"][0],
    "##### Yogagocchakaṃ": M.GROUPS["1-M-2-7-0"][0],
    "##### Nīvaraṇagocchakaṃ": M.GROUPS["1-M-2-8-0"][0],
    "##### Parāmāsagocchakaṃ": M.GROUPS["1-M-2-9-0"][0],
    "##### Mahantaradukaṃ": M.GROUPS["1-M-2-10-0"][0],
    "##### Upādānagocchakaṃ": M.GROUPS["1-M-2-11-0"][0],
    "##### Kilesagocchakaṃ": M.GROUPS["1-M-2-12-0"][0],
    "##### Piṭṭhidukaṃ": M.GROUPS["1-M-2-13-0"][0],
}
HEAD.update(GROUP_HEAD)
# «Nikkhepakaṇḍe dutiyabhāṇavāro.» (terms file), «Abhidhammadukaṃ.» (terms file), «Nikkhepakaṇḍaṃ niṭṭhitaṃ.»
# (terms-file pattern «<phần> đã hoàn tất.»)
END_BHANA2 = G.END_BHANA1.replace("thứ nhất", "thứ hai")
END_ABHI = "Các bộ đôi theo Vi Diệu Pháp."
END_KANDA = cap(G._KANDA) + " đã hoàn tất."
assert END_KANDA == "Phần tóm lược đã hoàn tất."
CLOSING = {"Nikkhepakaṇḍe dutiyabhāṇavāro. (proposed)": END_BHANA2, "Abhidhammadukaṃ. (proposed)": END_ABHI}


def check_headings():
    terms, lines = {}, {}
    for line in TERMS.read_text(encoding="utf-8").splitlines():
        m = re.fullmatch(r"(#+ .+?) = (#+ .+)", line)
        if m:
            terms.setdefault(m.group(1), m.group(2))
        m = re.fullmatch(r"([^#].+?) = (.+)", line)
        if m:
            lines.setdefault(m.group(1), m.group(2))
    for p, v in HEAD.items():
        assert terms[p] == v, (p, terms.get(p), v)
    for p, v in CLOSING.items():
        assert lines[p] == v, (p, lines.get(p), v)
    assert lines["<X>kaṇḍaṃ niṭṭhitaṃ. (proposed)"].startswith("<phần> đã hoàn tất.")
    return len(HEAD) + len(CLOSING)


# =========================================================================================
# 2. Lists and frames (4-01)
# =========================================================================================
K3, KA, KAB, VIP, SAS = G.K3, G.KA, G.KAB, G.VIP, G.SAS
SPH3, SPH4, SPHERE, TL = G.SPH3, G.SPH4, G.SPHERE, G.TL
KHN, KH4, KH4P, KH5P = G.KHN, G.KH4, G.KH4P, G.KH5P
KH4P_SP = f"{KHN['vedanākkhandho']} {ELL} {KHN['viññāṇakkhandho']}"   # stray space before «…pe…», mirrored
KH3V = ", ".join(KHN[k] for k in ("vedanākkhandho", "saññākkhandho", "saṅkhārakkhandho"))
SABBA, ASD, LEFT, THOSE = G.SABBA, G.ASD, G.LEFT, G.THOSE
MAGGA, PHALA, MAGGA3, MAGGA4 = G.MAGGA, G.PHALA, G.MAGGA3, G.MAGGA4
SAMP_N, SAMP_1, KAMMA3, TADEK = G.SAMP_N, G.SAMP_1, G.KAMMA3, G.TADEK
YO, EVA, EXCEPT = G.YO, G.EVA, G.EXCEPT
TAM = C.N["cittaṃ"]                                    # tâm
ALL_RF_ASD = f"{cap(R.ALL_RF)} và {ASD}"               # sabbañca rūpaṃ, asaṅkhatā ca dhātu (opening a list)
REST_RF = f"và {R.RF} còn lại"                          # avasesañca rūpaṃ
assert ASD == "yếu tố không do điều kiện tạo thành" and R.MAHA4 == "bốn yếu tố cơ bản"


def NO_X(key, kh=KH4P):
    """'Te dhamme ṭhapetvā avasesā kusalākusalābyākatā … apariyāpannā; vedanākkhandho…pe…; sabbañca rūpaṃ …'"""
    return QB(key, f"{G.TE_TH} {K3} {LEFT}, {SPH4}, {TL} {kh}; {SABBA}")


assert NO_X(P2(14, "b")) == G.NO_X(P2(14, "b"))


def VIPP_SAS_KAB(key):
    """'Tehi dhammehi ye dhammā vippayuttā sāsavā kusalābyākatā dhammā …; rūpakkhandho…pe…'"""
    return QB(key, f"{cap(KAB)}, không gắn liền với {THOSE}, {SAS}, {SPH3}, {TL} {KH5P}")


def SAMP(key):
    return QB(key, f"{G.REL_SAMP}, {TL} {KH4P}")


def VIPP(key):
    return QB(key, f"{G.REL_VIPP}, {TL} {KH4P}; {SABBA}")


def AMONG(key, rel):
    """'Tehi dhammehi ye dhammā <rel>, te dhamme ṭhapetvā vedanākkhandho…pe… viññāṇakkhandho'"""
    return QB(key, f"Trong số những hiện tượng {rel}, ngoại trừ {THOSE}, {KH4P}")


assert AMONG(P2(18, "b"), f"gắn liền với {THOSE}") == QB(P2(18, "b"), f"{G.AMONG_SAMP} {KH4P}")


def AMONG_REST(key, rel):
    """'Tehi dhammehi ye dhammā <rel>, te dhamme ṭhapetvā avasesā sāsavā kusalākusalābyākatā …; rūpakkhandho…pe…'"""
    return QB(key, f"Trong số những hiện tượng {rel}, ngoại trừ {THOSE}, {K3} {LEFT}, {SAS}, {SPH3}, {TL} {KH5P}")


assert AMONG_REST(P2(17, "b"), f"là đối tượng của {THOSE}") == G.AMONG_NIYA_SEG(P2(17, "b"))


def both_list(pali_line, nom, ins, x):
    """'A B-ena x-ñceva x-sampayuttañca, …' = «A vừa là x vừa gắn liền với B, …» (4-01 _both), in the Pāli order"""
    body = pali_line.split("? ", 1)[1].split(f" {DASH} ime dhammā", 1)[0]
    out = []
    for item in body.split(", "):
        a, b = item.split(" ")[:2]
        out.append(G._both(nom[a[0].lower() + a[1:]], x, ins[b]))
    return cap(", ".join(out))


# =========================================================================================
# 3. Names
# =========================================================================================
OGHA_N, YOGA_N, NIV_N, UPA_N, KILESA_N = "dòng lũ", "ách", "chướng ngại", "sự bám víu", "phiền não"
for n, x in ((32, OGHA_N), (38, YOGA_N), (44, NIV_N), (69, UPA_N), (75, KILESA_N)):
    assert M.PRED[P2(n, "a")] == f"là {x}", n
PARA = M.PARA                                                   # sự hiểu sai lệch
# hindrances: «chướng ngại X» (as «xiềng xích X», 4-01: the bare noun after the class word)
KAMACCHANDA = G._desire(G.KAMA, "")[0]                          # kāmacchanda = ý muốn dục lạc (S_KAMA)
assert G.S_KAMA.startswith(KAMACCHANDA + ", ")
THINA, MIDDHA = "sự uể oải", "sự đờ đẫn"                         # thina / middha
UDDHACCA = E.NEW_NAMES["uddhaccaṃ"]                              # sự xao động
KUKKUCCA = "sự hối tiếc"                                         # kukkucca (kept apart from uddhacca)
VICI = G.VICI                                                    # sự hoài nghi
BYAPADA = E.NEW_NAMES["byāpādo"]                                 # sự ác ý
AVIJJA = M.BARE[P2(110, "a")]                                    # vô minh
bare = lambda s: s.removeprefix("sự ")   # noqa: E731
NIV = {
    "kāmacchandanīvaraṇaṃ": f"{NIV_N} {KAMACCHANDA}",
    "byāpādanīvaraṇaṃ": f"{NIV_N} {bare(BYAPADA)}",
    "thinamiddhanīvaraṇaṃ": f"{NIV_N} {bare(THINA)} và {bare(MIDDHA)}",
    "uddhaccakukkuccanīvaraṇaṃ": f"{NIV_N} {bare(UDDHACCA)} và {bare(KUKKUCCA)}",
    "vicikicchānīvaraṇaṃ": f"{NIV_N} {bare(VICI)}",
    "avijjānīvaraṇaṃ": f"{NIV_N} {AVIJJA}",
    "uddhaccanīvaraṇaṃ": f"{NIV_N} {bare(UDDHACCA)}",
    "kukkuccanīvaraṇaṃ": f"{NIV_N} {bare(KUKKUCCA)}",
}
assert G.FETTER("vicikicchā") == "xiềng xích hoài nghi" and NIV["vicikicchānīvaraṇaṃ"] == "chướng ngại hoài nghi"
NIV_INS = {k.replace("nīvaraṇaṃ", "nīvaraṇena"): v for k, v in NIV.items()}
SIX_NIV = [NIV[k] for k in ("kāmacchandanīvaraṇaṃ", "byāpādanīvaraṇaṃ", "thinamiddhanīvaraṇaṃ",
                            "uddhaccakukkuccanīvaraṇaṃ", "vicikicchānīvaraṇaṃ", "avijjānīvaraṇaṃ")]
# misapprehension
DP = f"{PARA} dưới dạng quan điểm"                             # diṭṭhiparāmāsa
# clinging: «sự bám víu vào X»
SELFDOC = f"học thuyết về {G.SELF}"                              # attavāda
UPA = {
    "kāmupādānaṃ": f"{UPA_N} vào {G.KAMA}",
    "diṭṭhupādānaṃ": f"{UPA_N} vào quan điểm",
    "sīlabbatupādānaṃ": f"{UPA_N} vào giới hạnh và nghi thức",
    "attavādupādānaṃ": f"{UPA_N} vào {SELFDOC}",
}
assert G.SILA_N.endswith("giới hạnh và nghi thức")
UPA_INS = {k.replace("upādānaṃ", "upādānena"): v for k, v in UPA.items()}
# defilements (2-04 / 4-01 names)
LOBHA, DOSA, MOHA = G.ROOTS_A
MANA = G.MANA_N                                                  # sự kiêu mạn
DITTHI = E.W_DITTHI[0]                                           # quan điểm
AHIRIKA, ANOTTAPPA = E.NEW_NAMES["ahirikaṃ"], E.NEW_NAMES["anottappaṃ"]
assert (AHIRIKA, ANOTTAPPA) == (M.BARE[P2(115, "a")], M.BARE[P2(115, "b")])
KIL = {"lobho": LOBHA, "doso": DOSA, "moho": MOHA, "māno": MANA, "diṭṭhi": DITTHI, "vicikicchā": VICI,
       "thinaṃ": THINA, "uddhaccaṃ": UDDHACCA, "ahirikaṃ": AHIRIKA, "anottappaṃ": ANOTTAPPA}
KIL_INS = {"lobhena": LOBHA, "dosena": DOSA, "mohena": MOHA, "mānena": MANA, "diṭṭhiyā": DITTHI,
           "vicikicchāya": VICI, "thinena": THINA, "uddhaccena": UDDHACCA, "ahirikena": AHIRIKA,
           "anottappena": ANOTTAPPA}
VATTHU = "chỗ dựa"                                               # vatthu (3-01)

# =========================================================================================
# 4. Strings
# =========================================================================================
# thina / middha (akallatā = sự không khỏe khoắn; akammaññatā = sự không dễ vận dụng, sample kammaññatā;
# kāya- = của thân tinh thần, sample)
DE_VAN_DUNG = C.WL["kammaññatā"][0]                              # sự dễ vận dụng
UNFIT = "sự không khỏe khoắn"
S_THINA = ", ".join([f"{UNFIT} {C.CITTA_N}", f"sự không {DE_VAN_DUNG[3:]}", "sự chùng xuống",
                     "sự chùng xuống hoàn toàn", "sự co rút", "sự khởi co rút", "trạng thái khởi co rút", THINA,
                     "sự khởi uể oải", f"trạng thái khởi uể oải {C.CITTA_N}"])
S_MIDDHA = ", ".join([f"{UNFIT} {C.KAYA_N}", f"sự không {DE_VAN_DUNG[3:]}", "sự bao phủ", "sự bao phủ hoàn toàn",
                      "sự bế tắc bên trong", MIDDHA, "giấc ngủ", "sự gà gật", "giấc ngủ", "sự ngủ",
                      "trạng thái đã ngủ"])
assert len(S_THINA.split(", ")) == 10 and len(S_MIDDHA.split(", ")) == 11
S_UDDHACCA = ", ".join(E.W_UDDHACCA)
KUKKUCCA_OPEN = ("Tri giác điều không được phép là được phép, tri giác điều được phép là không được phép, "
                 "tri giác điều không đáng chê trách là đáng chê trách, tri giác điều đáng chê trách là "
                 "không đáng chê trách")
assert C.N["saññā"] == "tri giác"
S_KUKKUCCA = ", ".join([KUKKUCCA, "sự khởi hối tiếc", "trạng thái khởi hối tiếc", f"sự ân hận {C.CITTA_N}",
                        E.W_VICIKICCHA[-1]])                     # manovilekho = sự giằng xé trong ý (2-04)
ITI = "Như vậy, cả {a} này lẫn {b} này"                         # iti idañca A, idañca B


def BOTH_THESE(a, b):
    return ITI.format(a=a, b=b)


# moha / diṭṭhi / vicikicchā / dosa / lobha / kāma / bhava (4-01)
S_MOHA, ANNANA4, S_DITTHI, S_KANKHA = G.S_MOHA, G.ANNANA4, G.S_DITTHI, G.S_KANKHA
TEN_VIEWS, ALL_WRONG = G.TEN_VIEWS, G.ALL_WRONG
DITTHI_ABBR = f"{E.W_DITTHI[0]}, {E.W_DITTHI[1]}{ELL} {E.W_DITTHI[-1]}"     # diṭṭhi diṭṭhigataṃ…pe… vipariyāsaggāho
MOHA_ABBR = f"{E.W_MOHA[0]}, {E.W_MOHA[1]}{ELL} {', '.join(E.W_MOHA[-3:])}"  # aññāṇaṃ adassanaṃ…pe… akusalamūlaṃ
VICI_FIRST = G.VICI_OPEN.split(", ")[0]                                      # Satthari kaṅkhati vicikicchati
KANKHA_LAST = ", ".join(E.W_VICIKICCHA[-2:])                                 # thambhitattaṃ cittassa manovilekho
assert G.VICI_OPEN.startswith(VICI_FIRST + ", ") and S_KANKHA.endswith(KANKHA_LAST)
BHAVA_ABBR = f"{G.BHAVESU} {G._BH[0]}{ELL} {G._BH[-1]}"                     # Yo bhavesu bhavachando…pe… bhavajjhosānaṃ
# māna without the variant bracket and with «; yo evarūpo» (^1-1239)
MANA_PLAIN = re.sub(r" \[[^\]]*\]", "", G.MANA).replace(f". {cap(EVA)} ", f"; {EVA} ", 1)
assert MANA_PLAIN.count(";") == 1 and "[" not in MANA_PLAIN
# identity view with the four aggregates abbreviated («Vedanaṃ…pe… saññaṃ…pe… saṅkhāre…pe… viññāṇaṃ …»)
_HEAD_SAKK = G.SAKKAYA_OPEN.split(" Người ấy ", 1)[0]
assert _HEAD_SAKK.endswith(G._SAKK[0])
SAKKAYA_ABBR = (f"{_HEAD_SAKK} Người ấy xem " + f"{ELL} ".join(G._AGGS[1:5]) + " "
                + G._SAKK[4].removeprefix(f"xem {G._AGGS[4]} "))
assert SAKKAYA_ABBR.count(ELL) == 3 and SAKKAYA_ABBR.endswith(G._SAKK[4].split(" là ", 1)[1])
# natthi dinnaṃ / atthi dinnaṃ
_LOKA = "thế giới"   # loka (as the ten views)


def _dinnam(yes):
    has = "có" if yes else "không có"
    return (f"“{cap(has)} bố thí, {has} tế lễ, {has} cúng dường, {has} quả và kết quả của các nghiệp đã làm tốt "
            f"hay làm xấu, {has} {_LOKA} này, {has} {_LOKA} khác, {has} mẹ, {has} cha, {has} chúng sinh hóa sinh, "
            f"{has} ở đời các sa-môn và bà-la-môn đi đúng đường{{V}}, thực hành đúng đắn, là những người sau khi "
            f"tự mình hiểu biết trực tiếp và tự mình chứng nghiệm {_LOKA} này và {_LOKA} khác thì tuyên bố về chúng”")


NATTHI = _dinnam(False).replace("{V}", "")
NATTHI_V = _dinnam(False).replace("{V}", M.V("p", "Ka.", "samaggatā"))
ATTHI = _dinnam(True).replace("{V}", "")
# abbreviated sample strings
WP = C.WL["paññā"]
PANNA_ABBR = f"{WP[0]}, {WP[1]}{ELL} {', '.join(WP[-3:])}"   # paññā pajānanā…pe… amoho dhammavicayo sammādiṭṭhi
assert PANNA_ABBR == "trí tuệ, sự hiểu rõ… sự không si mê, sự tìm hiểu các hiện tượng, quan điểm đúng đắn"
SAMADHI_ABBR = f"{C.WL['cittassa'][0]}{ELL} {C.WL['cittassa'][-1]}"   # cittassa ṭhiti…pe… sammāsamādhi
VIRIYA_ABBR = f"{C.WL['cetasiko'][0]}{ELL} {C.WL['cetasiko'][-1]}"   # cetasiko vīriyārambho…pe… sammāvāyāmo
SHAME = "Việc"   # Yaṃ (na) hirīyati … / ottappati … (the sample's SHAME frame without «vào lúc ấy»)
assert C.SHAME("hirī", "S").split("? ", 1)[1].startswith(f"{SHAME} vào lúc ấy S")
# mental and material (4-03)
SAMPAJ = M.BARE[P2(130, "b")]
assert SAMPAJ == C.N["sampajaññaṃ"]
ASEVANA = "sự thực hành, sự tu tập, sự làm đi làm lại"     # āsevanā bhāvanā bahulīkammaṃ (bhāvanā = sự tu tập)
assert M.DEV == "sự tu tập"
IN_CASE = "Bất cứ điều gì trong trường hợp ấy là"          # yā tattha S
KAYIKA = ["bằng thân", "bằng lời nói", "bằng thân và lời nói"]   # kāyiko / vācasiko / kāyikavācasiko


def TRANSGR(neg):
    w = "sự không vi phạm" if neg else "sự vi phạm"
    return cap(YO) + " " + ", ".join(f"{w} {k}" for k in KAYIKA)


SILA_SAMVARA = "sự thu thúc theo giới hạnh"                 # sīlasaṃvara (saṃvara = sự thu thúc)


# =========================================================================================
# 5. 4-02
# =========================================================================================
def build_402(P):
    S = []

    def add(bid, *lines):
        S.append((bid, list(lines)))

    # --- floods, yokes (abbreviated) ---
    add("1-3-2-6-0", GROUP_HEAD["##### Oghagocchakaṃ"])
    add("1-1156", f"{Q(P2(32, 'a'))} Bốn {OGHA_N}{ELL} {M.ANSWER(P2(37, 'a'))}")
    add("1-3-2-7-0", GROUP_HEAD["##### Yogagocchakaṃ"])
    add("1-1157", f"{Q(P2(38, 'a'))} Bốn {YOGA_N}{ELL} {M.ANSWER(P2(43, 'a'))}")

    # --- hindrances ---
    add("1-3-2-8-0", GROUP_HEAD["##### Nīvaraṇagocchakaṃ"])
    k = P2(44, "a")
    add("1-1158", f"{Q(k)} Sáu {NIV_N}{M.V('p', 'Syā.', 'nīvaraṇāni')} {DASH} " + ", ".join(SIX_NIV) + ".")
    n = NIV["kāmacchandanīvaraṇaṃ"]
    add("1-1159", f"{TQ(n)} {G.KAMESU} {G.S_KAMA} {TA(n)}")
    # the Pāli has «;» after «caratīti …» and «carissatīti …» here (commas at ^1-1066): one Vietnamese formula
    n = NIV["byāpādanīvaraṇaṃ"]
    add("1-1160", f"{TQ(n)} {G.DOSA_OPEN} {cap(EVA)} {G.S_DOSA} {TA(n)}")
    n = NIV["thinamiddhanīvaraṇaṃ"]
    add("1-1161", f"{TQ(n)} Có {THINA}, có {MIDDHA}.")
    add("1-1162", f"{TQ(THINA)} {YO} {S_THINA} {TA(THINA)}")
    add("1-1163", f"{TQ(MIDDHA)} {YO} {S_MIDDHA} {TA(MIDDHA)} {BOTH_THESE(THINA, MIDDHA)} {TA(n)}")
    n = NIV["uddhaccakukkuccanīvaraṇaṃ"]
    add("1-1164", f"{TQ(n)} Có {UDDHACCA}, có {KUKKUCCA}.")
    add("1-1165", f"{TQ(UDDHACCA)} {YO} {S_UDDHACCA} {TA(UDDHACCA)}")
    add("1-1166", f"{TQ(KUKKUCCA)} {KUKKUCCA_OPEN}. {cap(EVA)} {S_KUKKUCCA} {TA(KUKKUCCA)} "
                  f"{BOTH_THESE(UDDHACCA, KUKKUCCA)} {TA(n)}")
    n = NIV["vicikicchānīvaraṇaṃ"]
    add("1-1167", f"{TQ(n)} {G.VICI_OPEN}. {cap(EVA)} {S_KANKHA} {TA(n)}")
    # «aññāṇaṃः yaṃ»: Devanāgarī visarga where a punctuation mark belongs; «;» (as 4-01 ^1-1106)
    n = NIV["avijjānīvaraṇaṃ"]
    add("1-1168", f"{TQ(n)} {cap(ANNANA4)}; {EVA} {S_MOHA} {TA(n)}", cap(M.ANSWER(k)))
    add("1-1169", NO_X(P2(44, "b")))
    add("1-1170", G.NIYA(P2(45, "a")))
    add("1-1171", QB(P2(45, "b"), MAGGA3))
    add("1-1172", SAMP(P2(46, "a")))
    add("1-1173", VIPP(P2(46, "b")))
    add("1-1174", G.SAME(NIV_N, P2(47, "a")))
    add("1-1175", AMONG_REST(P2(47, "b"), f"là đối tượng của {THOSE}"))
    add("1-1176", QB(P2(48, "a"), both_list(P["1-1176"][0], NIV, NIV_INS, NIV_N)))
    add("1-1177", AMONG(P2(48, "b"), f"gắn liền với {THOSE}"))
    add("1-1178", VIPP_SAS_KAB(P2(49, "a")))       # kusalābyākatā (as written)
    add("1-1179", QB(P2(49, "b"), MAGGA3))

    # --- misapprehension ---
    add("1-3-2-9-0", GROUP_HEAD["##### Parāmāsagocchakaṃ"])
    k = P2(50, "a")
    add("1-1180", f"{Q(k)} {cap(DP)}.")
    add("1-1181", f"{TQ(DP)} {TEN_VIEWS}; {EVA} {S_DITTHI} {TA(DP)} {cap(ALL_WRONG)} {DP}.", cap(M.ANSWER(k)))
    add("1-1182", NO_X(P2(50, "b")))
    add("1-1183", G.NIYA(P2(51, "a")))
    add("1-1184", QB(P2(51, "b"), MAGGA3))
    add("1-1185", SAMP(P2(52, "a")))
    add("1-1186", VIPP(P2(52, "b")))
    add("1-1187", f"{Q(P2(53, 'a'))} Chính {PARA} ấy {M.PRED[P2(53, 'a')]}.")
    add("1-1188", AMONG_REST(P2(53, "b"), f"bị {THOSE} nắm giữ"))
    add("1-1189", G.VIPP_SAS(P2(54, "a")))         # kusalākusalābyākatā (as written)
    add("1-1190", QB(P2(54, "b"), MAGGA3))

    # --- long intermediate pairs ---
    add("1-3-2-10-0", GROUP_HEAD["##### Mahantaradukaṃ"])
    add("1-1191", QB(P2(55, "a"), cap(KH4)))
    add("1-1192", QB(P2(55, "b"), ALL_RF_ASD))
    VIN7 = [E.EYE, E.EAR, E.NOSE, E.TONGUE, E.BODY, B.NAME["manodhātu"], B.NAME["manoviññāṇadhātu"]]
    add("1-1193", QB(P2(56, "a"), cap(", ".join(VIN7))))
    add("1-1194", QB(P2(56, "b"), f"{cap(KH3V)}; {SABBA}"))
    add("1-1195", QB(P2(57, "a"), cap(KH3V)))
    add("1-1196", QB(P2(57, "b"), f"{cap(TAM)}; {SABBA}"))
    add("1-1197", QB(P2(58, "a"), cap(KH3V)))

    def not_said(a, b):
        """'Cittaṃ na vattabbaṃ – A-ntipi, B-ntipi.'"""
        return f"Về {TAM}, không nên nói {DASH} rằng nó “{a}”, cũng không nên nói rằng nó “{b}”."

    add("1-1198", QB(P2(58, "b"), ALL_RF_ASD) + " " + not_said(M.PRED[P2(58, "a")], M.PRED[P2(58, "b")]))
    add("1-1199", QB(P2(59, "a"), cap(KH3V)))
    add("1-1200", QB(P2(59, "b"), ALL_RF_ASD) + " " + not_said(M.PRED[P2(59, "a")], M.PRED[P2(59, "b")]))
    VINNATTI2 = f"{R.N['kāyaviññatti']}, {R.N['vacīviññatti']}"
    CITTAJA = (f"{X.ANY_OTHER} {X.QUALS['cittajaṃ cittahetukaṃ cittasamuṭṭhānaṃ']}: "
               + ", ".join(X.ITEMS[i] for i in ("rūpāyatanaṃ", "saddāyatanaṃ", "gandhāyatanaṃ", "rasāyatanaṃ",
                                                "phoṭṭhabbāyatanaṃ", "ākāsadhātu", "āpodhātu", "rūpassa lahutā",
                                                "rūpassa mudutā", "rūpassa kammaññatā", "rūpassa upacayo",
                                                "rūpassa santati", "kabaḷīkāro āhāro")))
    assert f"{cap(VINNATTI2)}, {CITTAJA} {DASH} " in (OUT_DIR / "3-02-rupakandam.md").read_text(encoding="utf-8")
    add("1-1201", QB(P2(60, "a"), f"{cap(KH3V)}; {VINNATTI2}; {CITTAJA}"))
    TAM_REST = f"{cap(TAM)}; {REST_RF}; và {ASD}"     # cittañca, avasesañca rūpaṃ, asaṅkhatā ca dhātu
    TAM_ALL = f"{cap(TAM)}; {SABBA}"                  # cittañca, sabbañca rūpaṃ, asaṅkhatā ca dhātu
    add("1-1202", QB(P2(60, "b"), TAM_REST))
    add("1-1203", QB(P2(61, "a"), f"{cap(KH3V)}, {VINNATTI2}"))
    add("1-1204", QB(P2(61, "b"), TAM_REST))
    add("1-1205", QB(P2(62, "a"), f"{cap(KH3V)}, {VINNATTI2}"))
    add("1-1206", QB(P2(62, "b"), TAM_REST))
    for bid, nn in (("1-1207", 63), ("1-1209", 64), ("1-1211", 65)):
        add(bid, QB(P2(nn, "a"), cap(KH3V)))
        add(f"1-{int(bid.split('-')[1]) + 1}", QB(P2(nn, "b"), TAM_ALL))
    add("1-1213", QB(P2(66, "a"), f"{cap(R.N['cakkhāyatanaṃ'])}{ELL} {B.NAME['manāyatanaṃ']}"))
    add("1-1214", QB(P2(66, "b"), f"{cap(R.N['rūpāyatanaṃ'])}{ELL} {B.NAME['dhammāyatanaṃ']}"))
    add("1-1215", QB(P2(67, "a"), f"{cap(R.N['cakkhāyatanaṃ'])}{ELL} {R.N['kabaḷīkāro āhāro']}"))
    add("1-1216", QB(P2(67, "b"), f"{cap(KH4)}, {R.MAHA4} và {ASD}"))
    b994 = f"{cap(VIP)}, {SAS}, {SPH3}, {TL} {KH4P}; {G.KATATTA}"
    assert b994 == body401("1-994")
    add("1-1217", QB(P2(68, "a"), b994))
    b995 = f"{cap(KA)}, {SAS}, {SPH3}, {TL} {KH4P}; {G.KIRIYA}; {G.NA_KATATTA}"
    assert b995 == body401("1-995")
    add("1-1218", QB(P2(68, "b"), f"{b995}; {MAGGA3[0].lower()}{MAGGA3[1:]}"))

    # --- clinging ---
    add("1-3-2-11-0", GROUP_HEAD["##### Upādānagocchakaṃ"])
    k = P2(69, "a")
    add("1-1219", f"{Q(k)} Bốn {UPA_N} {DASH} " + ", ".join(UPA.values())
        + M.V("s", "Sī.", "kāmūpādānaṃ diṭṭhūpādānaṃ sīlabbatūpādānaṃ attavādūpādānaṃ") + ".")
    n = UPA["kāmupādānaṃ"]
    add("1-1220", f"{TQ(n)} {G.KAMESU} {G.S_KAMA} {TA(n)}")
    n = UPA["diṭṭhupādānaṃ"]
    add("1-1221", f"{TQ(n)} {NATTHI_V} {DASH} {EVA} {S_DITTHI} {TA(n)} "
                  f"Ngoại trừ {UPA['sīlabbatupādānaṃ']} cùng {UPA['attavādupādānaṃ']}, {ALL_WRONG} {n}.")
    n = UPA["sīlabbatupādānaṃ"]
    add("1-1222", f"{TQ(n)} {G.SILA_OPEN} {DASH} {EVA} {S_DITTHI} {TA(n)}")
    n = UPA["attavādupādānaṃ"]
    add("1-1223", f"{TQ(n)} {SAKKAYA_ABBR} {cap(EVA)} {S_DITTHI} {TA(n)}", cap(M.ANSWER(k)))
    add("1-1224", NO_X(P2(69, "b")))
    add("1-1225", G.NIYA(P2(70, "a")))
    add("1-1226", QB(P2(70, "b"), MAGGA3))
    add("1-1227", SAMP(P2(71, "a")))
    add("1-1228", VIPP(P2(71, "b")))
    add("1-1229", G.SAME(UPA_N, P2(72, "a")))
    add("1-1230", AMONG_REST(P2(72, "b"), f"là đối tượng của {THOSE}"))
    add("1-1231", QB(P2(73, "a"), both_list(P["1-1231"][0], UPA, UPA_INS, UPA_N)))
    add("1-1232", AMONG(P2(73, "b"), f"gắn liền với {THOSE}"))
    add("1-1233", G.VIPP_SAS(P2(74, "a")))
    add("1-1234", QB(P2(74, "b"), MAGGA3), END_BHANA2)

    # --- defilements ---
    add("1-3-2-12-0", GROUP_HEAD["##### Kilesagocchakaṃ"])
    k = P2(75, "a")
    add("1-1235", f"{Q(k)} Mười {VATTHU} của {KILESA_N} {DASH} " + ", ".join(KIL.values()) + ".")
    add("1-1236", f"{TQ(LOBHA)} {YO} {G.S_LOBHA} {TA(LOBHA)}")
    add("1-1237", V401["1-1066"][0])
    add("1-1238", f"{TQ(MOHA)} {cap(ANNANA4)}. {cap(EVA)} {S_MOHA} {TA(MOHA)}")
    add("1-1239", f"{TQ(MANA)} {MANA_PLAIN} {TA(MANA)}")
    add("1-1240", f"{TQ(DITTHI)} {TEN_VIEWS}; {EVA} {S_DITTHI} {TA(DITTHI)} {cap(ALL_WRONG)} {DITTHI}.")
    add("1-1241", f"{TQ(VICI)} {G.VICI_OPEN}; {EVA} {S_KANKHA} {TA(VICI)}")
    add("1-1242", f"{TQ(THINA)} {YO} {S_THINA} {TA(THINA)}")
    add("1-1243", f"{TQ(UDDHACCA)} {YO} {S_UDDHACCA} {TA(UDDHACCA)}")
    add("1-1244", f"{TQ(AHIRIKA)} {SHAME} {E.S_AHIRIKA} {TA(AHIRIKA)}")
    add("1-1245", f"{TQ(ANOTTAPPA)} {SHAME} {E.S_ANOTTAPPA} {TA(ANOTTAPPA)}", cap(M.ANSWER(k)))
    add("1-1246", NO_X(P2(75, "b"), KH4P_SP))
    add("1-1247", G.NIYA(P2(76, "a")))
    add("1-1248", QB(P2(76, "b"), MAGGA3))
    add("1-1249", QB(P2(77, "a"), G.AKUS_BLOCK))
    b1012 = f"{cap(KAB)}, {SPH4}, {TL} {KH4P}; {SABBA}"
    assert b1012 == body401("1-1012")
    add("1-1250", QB(P2(77, "b"), b1012))
    add("1-1251", SAMP(P2(78, "a")))
    add("1-1252", VIPP(P2(78, "b")))
    add("1-1253", G.SAME(KILESA_N, P2(79, "a")))
    add("1-1254", AMONG_REST(P2(79, "b"), f"là đối tượng của {THOSE}"))
    add("1-1255", G.SAME(KILESA_N, P2(80, "a")))
    add("1-1256", AMONG(P2(80, "b"), f"bị {THOSE} làm vẩn đục"))
    add("1-1257", QB(P2(81, "a"), both_list(P["1-1257"][0], KIL, KIL_INS, KILESA_N)))
    add("1-1258", AMONG(P2(81, "b"), f"gắn liền với {THOSE}"))
    add("1-1259", VIPP_SAS_KAB(P2(82, "a")))       # kusalābyākatā (as written)
    add("1-1260", QB(P2(82, "b"), MAGGA3))

    # --- closing pairs ---
    add("1-3-2-13-0", GROUP_HEAD["##### Piṭṭhidukaṃ"])
    SAKK_SEG = f"{TQ(G.SAKKAYA)} {SAKKAYA_ABBR} {cap(EVA)} {DITTHI_ABBR} {TA(G.SAKKAYA)}"
    VICI_SEG = f"{TQ(VICI)} {VICI_FIRST}{ELL} {KANKHA_LAST} {TA(VICI)}"
    SILA_SEG = f"{TQ(G.SILA_N)} {G.SILA_OPEN} {DASH} {EVA} {DITTHI_ABBR} {TA(G.SILA_N)}"
    assert Q(P2(83, "a")) == Q(G.T(8, "a")) and Q(P2(85, "a")) == Q(G.T(9, "a")) and Q(P2(86, "a")) == Q(G.T(9, "b"))
    add("1-1261", V401["1-1006"][0])
    add("1-1262", SAKK_SEG)
    add("1-1263", VICI_SEG)
    add("1-1264", f"{SILA_SEG} {V401['1-1010'][0]}")
    add("1-1265", NO_X(P2(83, "b")))
    b1011 = f"{G.AVASESA}; {TADEK}; {SAMP_N} {KH4P}; {KAMMA3}"
    assert b1011 == body401("1-1011")
    add("1-1266", QB(P2(84, "a"), b1011))
    add("1-1267", NO_X(P2(84, "b"), KH4P_SP))
    add("1-1268", V401["1-1013"][0])
    add("1-1269", SAKK_SEG)
    add("1-1270", VICI_SEG)
    add("1-1271", f"{SILA_SEG} {V401['1-1017'][0]}")
    add("1-1272", NO_X(P2(85, "b")))
    add("1-1273", V401["1-1018"][0])
    add("1-1274", NO_X(P2(86, "b")))
    PITI, SUKHA, UPEKKHA, VIT, VIC = G.PITI, G.SUKHA, G.UPEKKHA, G.VIT, G.VIC
    BH = G.BHUMI
    ALL4 = ("kāma", "rūpa", "arūpa", "apar")
    not_lvl = lambda x: f"khác với cấp độ có {x}"   # noqa: E731  (Na X-bhūmiyaṃ)

    def with_(key, level, spheres, factor, samp, aggs):
        """'X-bhūmiyaṃ …, Y ṭhapetvā, taṃsampayutto … – ime dhammā …'"""
        return QB(key, f"{BH(level, *spheres)}, {EXCEPT} {factor}; {samp} {aggs}")

    def without(key, level, spheres, factor):
        """'(Na) A-X-bhūmiyaṃ …; vedanākkhandho…pe…; Y ca, sabbañca rūpaṃ, … – ime dhammā …'"""
        return QB(key, f"{BH(level, *spheres)}; {KH4P}; và {factor}; {SABBA}")

    add("1-1275", with_(P2(87, "a"), M.PRED[P2(87, "a")], ("kāma", "rūpa", "apar"), VIT, SAMP_1, KH4P))
    add("1-1276", without(P2(87, "b"), M.PRED[P2(87, "b")], ALL4, VIT))
    add("1-1277", with_(P2(88, "a"), M.PRED[P2(88, "a")], ("kāma", "rūpa", "apar"), VIC, SAMP_1, KH4))
    add("1-1278", without(P2(88, "b"), M.PRED[P2(88, "b")], ALL4, VIC))
    add("1-1279", with_(P2(89, "a"), M.PRED[P2(89, "a")], ("kāma", "rūpa", "apar"), PITI, SAMP_1, KH4P))
    add("1-1280", without(P2(89, "b"), M.PRED[P2(89, "b")], ALL4, PITI))
    assert body401("1-1003") == with_(P2(90, "a"), "có " + PITI, ("kāma", "rūpa", "apar"), PITI, SAMP_1,
                                      KH4P).split("? ", 1)[1].rsplit(f" {DASH} đây là ", 1)[0]
    add("1-1281", with_(P2(90, "a"), "có " + PITI, ("kāma", "rūpa", "apar"), PITI, SAMP_1, KH4P))
    add("1-1282", without(P2(90, "b"), not_lvl(PITI), ALL4, PITI))
    add("1-1283", V401["1-1004"][0])
    add("1-1284", without(P2(91, "b"), not_lvl(SUKHA), ALL4, SUKHA))
    add("1-1285", V401["1-1005"][0])
    add("1-1286", without(P2(92, "b"), not_lvl(UPEKKHA), ("kāma", "rūpa", "apar"), UPEKKHA))
    assert Q(P2(91, "a")) == Q(G.T(7, "b")) and Q(P2(92, "a")) == Q(G.T(7, "c"))
    # the sphere definitions
    LOWER, UPPER = "làm giới hạn bên dưới", "ở bên trên"
    WITHIN = "lưu chuyển trong khoảng giữa ấy và nằm trong khoảng ấy"   # etthāvacarā ettha pariyāpannā
    THEN_K = f"thì các khối, các yếu tố, các lĩnh vực nhận biết {WITHIN}"   # khandhadhātu āyatanā
    THEN_C = f"thì tâm và các yếu tố đồng hành với tâm {WITHIN}"            # cittacetasikā dhammā
    WHO = ("ở người đã chứng nhập, hoặc ở người đã tái sinh vào đó, hoặc ở người an trú trong hạnh phúc ngay "
           "trong đời này{V}")   # samāpannassa vā upapannassa vā diṭṭhadhammasukhavihārissa vā
    assert F.SUKHAVIHARA_V.endswith("an trú trong hạnh phúc ngay trong đời này")
    add("1-1287", QB(P2(93, "a"), "Lấy địa ngục Vô Gián " + LOWER + ", và tính gộp cả chư thiên Tha Hóa Tự Tại"
                     + M.V("s", "Sī., Ka.", "paranimmitavasavattideve") + f" {UPPER}, {THEN_K}, {TL} {G.FIVE}"))
    add("1-1288", QB(P2(93, "b"), cap(", ".join(SPHERE[s] for s in ("rūpa", "arūpa", "apar")))))
    add("1-1289", QB(P2(94, "a"), "Lấy cõi Phạm Thiên " + LOWER + ", và tính gộp cả chư thiên Sắc Cứu Cánh"
                     + M.V("s", "Sī., Ka.", "akaniṭṭhadeve") + f" {UPPER}, {THEN_C}, "
                     + WHO.replace("{V}", M.V("s", "Ka.", "diṭṭhadhammasukhavihārassa"))))
    add("1-1290", QB(P2(94, "b"), cap(", ".join(SPHERE[s] for s in ("kāma", "arūpa", "apar")))))
    ARUPA_GODS = "chư thiên đã đạt đến {}"
    add("1-1291", QB(P2(95, "a"), "Lấy " + ARUPA_GODS.format(AKASA) + f" {LOWER}, và tính gộp cả "
                     + ARUPA_GODS.format(NEVA) + f" {UPPER}, {THEN_C}, " + WHO.replace("{V}", "")))
    add("1-1292", QB(P2(95, "b"), cap(", ".join(SPHERE[s] for s in ("kāma", "rūpa", "apar")))))
    add("1-1293", G.NIYA(P2(96, "a")))
    add("1-1294", QB(P2(96, "b"), f"Các {MAGGA}, các {PHALA} của {MAGGA}, và {ASD}"))
    add("1-1295", QB(P2(97, "a"), MAGGA4))
    add("1-1296", NO_X(P2(97, "b")))
    add("1-1297", QB(P2(98, "a"), f"Năm nghiệp có quả không gián đoạn, và {G.WRONG_VIEW} cố định, "
                                  f"{MAGGA4[0].lower()}{MAGGA4[1:]}"))
    assert body401("1-1035") == f"Năm nghiệp có quả không gián đoạn, và {G.WRONG_VIEW} cố định"
    add("1-1298", NO_X(P2(98, "b")))
    add("1-1299", G.NIYA(P2(99, "a")))
    add("1-1300", QB(P2(99, "b"), MAGGA3))
    # «Tīṇi akusalamūlāni lobho, doso, moho» has no dash here (^1-1249 has one): a colon
    add("1-1301", QB(P2(100, "a"), G.AKUS_BLOCK.replace(f" {DASH} ", ": ", 1)))
    add("1-1302", QB(P2(100, "b"), b1012), END_ABHI)
    return S


# names of the immaterial spheres (2-02 notes): ākāsānañcāyatana / nevasaññānāsaññāyatana
AKASA = "lĩnh vực không gian vô tận"
NEVA = "lĩnh vực không phải tri giác cũng không phải không tri giác"
_SPH_TEXT = (OUT_DIR / "2-02-cittuppadakandam.md").read_text(encoding="utf-8")
assert AKASA in _SPH_TEXT and NEVA in _SPH_TEXT


# =========================================================================================
# 6. 4-03
# =========================================================================================
def build_403(P):
    S = []

    def add(bid, *lines):
        S.append((bid, list(lines)))

    def every(key, kind):
        """'Sabbepi (a)kusalā dhammā X.'"""
        return f"Tất cả {DH} {G.K[kind]} đều {M.PRED[key]}."

    def called(nn, letter, body):
        """'Tattha katamo X? <body> – ayaṃ vuccati X.' with X = the matrix noun ^1-M2-nn"""
        x = M.BARE[P2(nn, letter)]
        return f"{TQ(x)} {body} {TA(x)}"

    AHIRI_ANOTT = cap(f"{AHIRIKA} và {ANOTTAPPA}")
    HIRI_OTT = cap(f"{C.N['hirī']} và {C.N['ottappaṃ']}")
    assert (C.N["hirī"], C.N["ottappaṃ"]) == (M.BARE[P2(116, "a")], M.BARE[P2(116, "b")])
    BAD = "hành vi xấu"     # duccarita (2-03)
    GOOD_ = "hành vi tốt"   # sucarita
    NAMING = ("Bất cứ điều gì là sự định danh, danh xưng chung, khái niệm, cách gọi thông thường, tên, sự đặt tên, "
              "danh hiệu, cách diễn đạt, dấu hiệu ngôn từ, lời diễn tả dành cho hiện tượng này hay hiện tượng kia")
    assert "khái niệm" in M.BARE[P2(108, "a")] and "cách diễn đạt" in M.BARE[P2(107, "a")]

    add("1-3-3-0", HEAD["#### Suttantikadukanikkhepaṃ"])
    add("1-1303", QB(P2(101, "a"), f"Những hiện tượng gắn liền với {M.BARE[P2(141, 'a')]}"))
    add("1-1304", QB(P2(101, "b"), f"Những hiện tượng gắn liền với {AVIJJA}"))
    add("1-1305", QB(P2(102, "a"), f"{cap(WP[0])} trong ba {G.ARIYAMAGGA} thấp hơn"))
    add("1-1306", QB(P2(102, "b"), f"{cap(WP[0])} trong {MAGGA} cao nhất, {TL} {MAGGA} A-la-hán"))
    assert "thành quả A-la-hán" in body401("1-1024")
    add("1-1307", QB(P2(103, "a"), AHIRI_ANOTT) + " " + every(P2(103, "a"), "akusala"))
    add("1-1308", QB(P2(103, "b"), HIRI_OTT) + " " + every(P2(103, "b"), "kusala"))
    add("1-1309", QB(P2(104, "a"), AHIRI_ANOTT) + " " + every(P2(104, "a"), "akusala"))
    # the Pāli answer ends with «?» («ime dhammā sukkā?»): kept
    add("1-1310", QB(P2(104, "b"), HIRI_OTT)[:-1] + "? " + every(P2(104, "b"), "kusala"))
    add("1-1311", QB(P2(105, "a"), cap(", ".join(f"{BAD} {k}" for k in ("bằng thân", "bằng lời nói", "bằng ý"))))
        + " " + every(P2(105, "a"), "akusala"))
    add("1-1312", QB(P2(105, "b"), cap(", ".join(f"{GOOD_} {k}" for k in ("bằng thân", "bằng lời nói", "bằng ý"))))
        + " " + every(P2(105, "b"), "kusala"))
    for bid, nn in (("1-1313", 106), ("1-1314", 107), ("1-1315", 108)):
        add(bid, QB(P2(nn, "a"), NAMING) + f" Tất cả {DH} đều {M.PRED[P2(nn, 'b')]}.")
    add("1-1316", called(109, "a", f"{cap(KH4)} và {ASD}"))
    assert G.MAHA == body401("1-1097")
    add("1-1317", called(109, "b", G.MAHA))
    add("1-1318", called(110, "a", f"{YO} {MOHA_ABBR}"))
    add("1-1319", called(110, "b", BHAVA_ABBR))
    SELF_WORLD = f"{cap(G.SELF)} và {_LOKA}"
    for bid, nn, letter, view in (("1-1320", 111, "a", "sẽ tồn tại"), ("1-1321", 111, "b", "sẽ không tồn tại"),
                                  ("1-1322", 112, "a", "là trường tồn"), ("1-1323", 112, "b", "sẽ bị đoạn diệt"),
                                  ("1-1324", 113, "a", "là hữu hạn"), ("1-1325", 113, "b", "là vô hạn")):
        add(bid, called(nn, letter, f"“{SELF_WORLD} {view}”, {EVA} {DITTHI_ABBR}"))
    assert G.VIEWS[0].endswith(" là trường tồn") and G.VIEWS[2].endswith(" là hữu hạn")
    assert "đoạn diệt" in M.BARE[P2(112, "b")]
    add("1-1326", called(114, "a", f"Điều sinh khởi liên quan đến quá khứ, {TL} {DITTHI_ABBR}"))
    add("1-1327", called(114, "b", f"Điều sinh khởi liên quan đến tương lai, {TL} {DITTHI_ABBR}"))
    add("1-1328", called(115, "a", f"{SHAME} {E.S_AHIRIKA}"))
    add("1-1329", called(115, "b", f"{SHAME} {E.S_ANOTTAPPA}"))
    add("1-1330", called(116, "a", f"{SHAME} {C.S_HIRI}"))
    add("1-1331", called(116, "b", f"{SHAME} {C.S_OTTAPPA}"))
    TOLD = "Khi được nhắc nhở đúng theo Giáo Pháp, bất cứ điều gì là"   # sahadhammike vuccamāne
    add("1-1332", called(117, "a", f"{TOLD} sự khó bảo, tính khó bảo, {M.BARE[P2(117, 'a')]}, sự tiếp nhận "
                                   "một cách ngang trái, sự thích thú với việc làm trái, sự thiếu tôn trọng, thái độ "
                                   "thiếu tôn trọng, sự thiếu kính trọng, sự không vâng lời"))
    SEVANA = ("thì bất cứ điều gì là sự giao du với họ, sự thường xuyên giao du, sự giao du mật thiết, sự gần gũi, "
              "sự gần gũi mật thiết, sự gắn bó, sự gắn bó mật thiết, sự nghiêng về phía họ")
    add("1-1333", called(117, "b", "Có những người không có niềm tin, phạm giới, ít học hỏi, keo kiệt, kém trí tuệ, "
                                   + SEVANA))
    add("1-1334", called(118, "a", f"{TOLD} sự dễ bảo, tính dễ bảo, {M.BARE[P2(118, 'a')]}, sự tiếp nhận không "
                                   "ngang trái, sự không thích thú với việc làm trái, sự kính trọng, sự tôn trọng, "
                                   "thái độ tôn trọng, sự vâng lời"))
    add("1-1335", called(118, "b", "Có những người có niềm tin, giữ giới, học hỏi nhiều, rộng lượng, có trí tuệ, "
                                   + SEVANA))
    APATTI = "lỗi vi phạm"
    SAMAP = "thành tựu thiền"
    assert APATTI in M.BARE[P2(119, "a")] and SAMAP in M.BARE[P2(120, "a")]

    def skill(about):
        """'Yā tāsaṃ X-ānaṃ X-kusalatā paññā pajānanā…pe… sammādiṭṭhi'"""
        return f"{YO} sự thành thạo về {about}, {TL} {PANNA_ABBR}"

    add("1-1336", called(119, "a", f"Năm nhóm {APATTI} là các {APATTI}, bảy nhóm {APATTI} cũng là các {APATTI}. "
                                   + cap(skill(f"các {APATTI} ấy"))))
    add("1-1337", called(119, "b", cap(skill(f"việc ra khỏi các {APATTI} ấy"))))
    T6 = [M.PRED[G.T(6, l)] for l in "abc"]
    add("1-1338", called(120, "a", "; ".join(f"có {SAMAP} {t}" for t in T6).replace("có", "Có", 1) + ". "
                                   + cap(skill(f"các {SAMAP} ấy"))))
    add("1-1339", called(120, "b", cap(skill(f"việc xuất khỏi các {SAMAP} ấy"))))
    DHATU18 = []
    for s in ("cakkhu", "sota", "ghāna", "jivhā", "kāya"):
        o = {"cakkhu": "rūpa", "sota": "sadda", "ghāna": "gandha", "jivhā": "rasa", "kāya": "phoṭṭhabba"}[s]
        DHATU18 += [R.N[f"{s}dhātu"], R.N[f"{o}dhātu"], f"yếu tố {R.VINNANA[s]}"]
    DHATU18 += [B.NAME["manodhātu"], B.NAME["dhammadhātu"], B.NAME["manoviññāṇadhātu"]]
    assert DHATU18[2] == E.NEW_NAMES["cakkhuviññāṇadhātu"] and DHATU18[14] == E.NEW_NAMES["kāyaviññāṇadhātu"]
    add("1-1340", called(121, "a", "Mười tám yếu tố: " + ", ".join(DHATU18) + ". " + cap(skill("các yếu tố ấy"))))
    add("1-1341", called(121, "b", cap(skill("sự chú tâm đến các yếu tố ấy"))))
    AY12 = []
    for s, o in (("cakkhāyatanaṃ", "rūpāyatanaṃ"), ("sotāyatanaṃ", "saddāyatanaṃ"), ("ghānāyatanaṃ", "gandhāyatanaṃ"),
                 ("jivhāyatanaṃ", "rasāyatanaṃ"), ("kāyāyatanaṃ", "phoṭṭhabbāyatanaṃ")):
        AY12 += [R.N[s], R.N[o]]
    AY12 += [B.NAME["manāyatanaṃ"], B.NAME["dhammāyatanaṃ"]]
    add("1-1342", called(122, "a", f"Mười hai lĩnh vực nhận biết {DASH} " + ", ".join(AY12) + ". "
                                   + cap(skill("các lĩnh vực nhận biết ấy"))))
    NAMA, RUPA_N = M.BARE[P2(109, "a")], M.BARE[P2(109, "b")]
    CHAIN = [AVIJJA, "các sự tạo tác", "thức", f"{NAMA} và {RUPA_N}", "sáu lĩnh vực nhận biết", C.N["phasso"],
             C.N["vedanā"], "khao khát", UPA_N, "sự hiện hữu", "sự sinh", "già và chết"]
    PS = (cap(", ".join(f"{a} làm điều kiện cho {b}" for a, b in zip(CHAIN, CHAIN[1:])))
          + "; sự sầu muộn, sự than khóc, sự đau khổ, nỗi buồn và sự tuyệt vọng sinh khởi; như vậy là "
            "sự phát sinh của toàn bộ khối khổ đau này.")
    add("1-1343", called(122, "b", f"{PS} {IN_CASE} {PANNA_ABBR}"))
    CAUSE = "nguyên nhân, là điều kiện"   # hetū paccayā (general sense here)
    add("1-1344", called(123, "a", f"Những hiện tượng nào là {CAUSE} cho sự sinh khởi"
                                   f"{M.V('p', 'Sī., Ka.', 'upādāya')} của những hiện tượng nào, thì đó là điều có "
                                   f"thể xảy ra; {IN_CASE[0].lower()}{IN_CASE[1:]} {PANNA_ABBR}"))
    add("1-1345", called(123, "b", "Những hiện tượng nào không phải là nguyên nhân, không phải là điều kiện cho sự "
                                   "sinh khởi của những hiện tượng nào, thì đó là điều không thể xảy ra; "
                                   f"{IN_CASE[0].lower()}{IN_CASE[1:]} {PANNA_ABBR}"))
    assert "điều có thể xảy ra" in M.BARE[P2(123, "a")] and "điều không thể xảy ra" in M.BARE[P2(123, "b")]
    add("1-1346", called(124, "a", f"{YO} tính ngay thật, " + ", ".join(C.WL["ujutā"][2:])))
    add("1-1347", called(124, "b", f"{YO} {C.S_MUDUTA}, sự khiêm nhường của tâm"))
    add("1-1348", called(125, "a", f"{YO} {M.BARE[P2(125, 'a')]}, sự bao dung, sự chịu đựng, sự không hung dữ, "
                                   f"sự không thô lỗ, {C.WL['pīti'][-1]}"))
    assert E.W_DOSA[8:10] == ["sự hung dữ", "sự thô lỗ"]
    for bid, nn, letter, neg, every_ in (("1-1349", 125, "b", True, SILA_SAMVARA),
                                         ("1-1368", 135, "a", False, "sự phạm giới"),
                                         ("1-1370", 136, "a", True, SILA_SAMVARA),
                                         ("1-1372", 137, "a", True, SILA_SAMVARA)):
        x = M.BARE[P2(nn, letter)]
        S.append((bid, [called(nn, letter, TRANSGR(neg)) + f" Mọi {every_} đều là {x}."]))
    add("1-1350", called(126, "a", "Từ bỏ lời nói thô cộc, cay nghiệt, làm người khác đau lòng, xúc phạm người khác, "
                                   "gần với sự giận dữ, không đưa đến định tâm, người ấy nói lời nói không có lỗi, êm "
                                   "tai, dễ mến, thấm vào lòng, lịch sự, được nhiều người yêu mến, được nhiều người ưa "
                                   f"thích; {IN_CASE[0].lower()}{IN_CASE[1:]} sự nói lời dịu dàng, sự nói lời hòa nhã, "
                                   "sự nói lời không thô ác"))
    assert C.N["samādhindriyaṃ"].endswith("định tâm") and G.S_DOSA.count("sự giận dữ") == 1
    PS_N = M.BARE[P2(126, "b")]
    GIFT = "vật phẩm"   # āmisa (kept apart from rūpa = vật chất)
    add("1-1351", called(126, "b", f"Có hai loại {bare(PS_N)} {DASH} {PS_N} bằng {GIFT} và {PS_N} bằng Giáo Pháp. "
                                   f"Ở đời này, có người niềm nở tiếp đón bằng {GIFT} hoặc bằng Giáo Pháp"))

    def doors(guard):
        no = "" if guard else "không "
        grasp = "không nắm giữ dấu hiệu tổng quát, không nắm giữ các chi tiết" if guard else \
            "nắm giữ dấu hiệu tổng quát, nắm giữ các chi tiết"

        def why(org):
            fac = R.N["cakkhundriyaṃ"] if org == "mắt" else B.NAME["manindriyaṃ"]
            so = "nên" if guard else "vậy mà"
            return (f"Vì nếu sống mà để {fac} không được thu thúc thì sự thèm muốn, nỗi buồn và các hiện tượng "
                    f"xấu ác, bất thiện có thể tràn vào người ấy, {so} người ấy {no}thực hành để thu thúc năng lực "
                    f"ấy, {no}bảo vệ {fac}, {no}thực hiện sự thu thúc nơi {fac}.")
        return (f"Ở đời này, có người khi thấy hình sắc bằng mắt thì {grasp}. {why('mắt')} "
                f"Khi nghe âm thanh bằng tai{ELL} khi ngửi mùi bằng mũi{ELL} khi nếm vị bằng lưỡi{ELL} khi chạm "
                f"vật xúc chạm bằng thân{ELL} khi nhận biết đối tượng của ý bằng ý thì {grasp}. {why('ý')}")

    assert B.NAME["manindriyaṃ"] == "năng lực ý" and R.N["cakkhundriyaṃ"] == "năng lực mắt"
    add("1-1352", called(127, "a", f"{doors(False)} {YO} sự không canh giữ, sự không bảo vệ, sự không che chở, "
                                   "sự không thu thúc của sáu năng lực này"))
    add("1-1353", called(127, "b", "Ở đời này, có người ăn thức ăn mà không suy xét, không đúng cách, để vui đùa, "
                                   "để say sưa, để trang điểm, để làm đẹp. "
                                   f"{IN_CASE} sự không biết đủ, sự không biết tiết độ, sự không suy xét trong ăn uống"))
    add("1-1354", called(128, "a", f"{doors(True)} {YO} sự canh giữ, sự bảo vệ, sự che chở, sự thu thúc của sáu "
                                   "năng lực này"))
    add("1-1355", called(128, "b", f"Ở đời này, có người ăn thức ăn có suy xét, đúng cách {DASH} không phải để vui "
                                   "đùa, không phải để say sưa, không phải để trang điểm, không phải để làm đẹp, mà "
                                   "chỉ để thân này tồn tại và kéo dài, để chấm dứt sự bức bách, để hỗ trợ đời sống "
                                   "tu hành trong sạch, với ý nghĩ: “Như vậy ta sẽ chấm dứt cảm giác cũ và không "
                                   "làm sinh khởi cảm giác mới, và ta sẽ có sự duy trì mạng sống, sự không có lỗi "
                                   f"và sự an trú thoải mái”. {IN_CASE} sự biết đủ, sự biết tiết độ, sự suy xét "
                                   "trong ăn uống"))
    assert "không đúng cách" not in M.BARE[P2(139, "b")] and "đúng cách" in M.BARE[P2(139, "b")]
    WS = C.WL["sati"]
    MUTTHA = [w.replace("sự ", "sự không ", 1) for w in WS[:6]] + ["sự hời hợt", "sự quên lãng"]
    assert WS[6:8] == ["sự không hời hợt", "sự không quên lãng"]
    add("1-1356", called(129, "a", f"{YO} {', '.join(MUTTHA)}"))
    add("1-1357", called(129, "b", f"{YO} {MOHA_ABBR}"))
    add("1-1358", called(130, "a", f"{YO} {C.S_SATI}"))
    add("1-1359", called(130, "b", f"{YO} {PANNA_ABBR}"))
    add("1-1360", called(131, "a", f"{YO} {PANNA_ABBR}"))
    add("1-1361", called(131, "b", f"{YO} {ASEVANA} {DH} thiện")
        + f" Cả bảy chi phần giác ngộ cũng là {M.BARE[P2(131, 'b')]}.")
    add("1-1362", called(132, "a", f"{YO} {SAMADHI_ABBR}"))
    add("1-1363", called(132, "b", f"{YO} {PANNA_ABBR}"))
    add("1-1364", called(133, "a", f"{YO} {SAMADHI_ABBR}"))
    add("1-1365", called(133, "b", f"{YO} {VIRIYA_ABBR}"))
    add("1-1366", called(134, "a", f"{YO} {VIRIYA_ABBR}"))
    add("1-1367", called(134, "b", f"{YO} {SAMADHI_ABBR}"))
    # «pavedentītiः yā»: Devanāgarī visarga where a punctuation mark belongs; «;»
    add("1-1369", called(135, "b", f"{NATTHI}; {EVA} {DITTHI_ABBR}") + f" {cap(ALL_WRONG)} {M.BARE[P2(135, 'b')]}.")
    add("1-1371", called(136, "b", f"{ATTHI}; {EVA} {PANNA_ABBR}")
        + f" Mọi {C.N['sammādiṭṭhi']} đều là {M.BARE[P2(136, 'b')]}.")
    add("1-1373", f"{TQ(M.BARE[P2(137, 'b')])} Hiểu biết rằng nghiệp là tài sản của chính mình, hiểu biết thuận theo "
                  "các sự thật, hiểu biết của người có được con đường, hiểu biết của người có được thành quả.")
    assert G.ARIYA.startswith("Ở người có được ")

    def gloss(text, body):
        """'"X"ti – …' = «“X” – nghĩa là …»"""
        return f"“{cap(text)}” {DASH} nghĩa là {body}"

    add("1-1374", gloss(M.BARE[P2(138, "a")], PANNA_ABBR + "."))
    add("1-1375", gloss(M.BARE[P2(138, "b")], VIRIYA_ABBR + "."))
    add("1-1376", gloss("sự xúc động", "nỗi sợ sinh, nỗi sợ già, nỗi sợ bệnh, nỗi sợ chết.") + " "
        + f"“Điều đáng xúc động”{M.V('s', 'Sī.', 'saṃvejanīyaṃ')} {DASH} nghĩa là sinh, già, bệnh, chết.")
    assert M.BARE[P2(139, "a")] == "sự xúc động trước những điều đáng xúc động"
    EFFORT = "khởi lên ý muốn, nỗ lực, khởi động tinh tấn, nâng tâm lên, ra sức nỗ lực"
    BADS, GOODS = f"{DH} xấu ác, bất thiện", f"{DH} thiện"
    assert f"để {BADS} xảy ra nơi mình" in C.S_HIRI
    add("1-1377", gloss(M.BARE[P2(139, "b")],
                        f"ở đời này, vị tỳ-khưu {EFFORT} để {BADS} chưa sinh khởi không sinh khởi; {EFFORT} để dứt bỏ "
                        f"{BADS} đã sinh khởi; {EFFORT} để {GOODS} chưa sinh khởi được sinh khởi; {EFFORT} để "
                        f"{GOODS} đã sinh khởi được duy trì, không bị mai một, được tăng trưởng, được lớn mạnh, "
                        "được tu tập và được hoàn thiện."))
    add("1-1378", gloss(M.BARE[P2(140, "a")], f"sự mong muốn nhiều hơn nữa của người không tự mãn với việc tu tập "
                                               f"{GOODS}."))
    add("1-1379", gloss(M.BARE[P2(140, "b")], "sự làm một cách chu đáo, sự làm một cách liên tục, sự làm một cách "
                                               f"bền bỉ, sự hành xử không chùng xuống, {C.WL['cetasiko'][10]}, "
                                               f"{C.WL['cetasiko'][11]}, {ASEVANA} trong việc tu tập {GOODS}."))
    assert (C.WL["cetasiko"][10], C.WL["cetasiko"][11]) == ("sự không buông bỏ ý muốn", "sự không buông gánh")
    VIJJA = M.BARE[P2(141, "a")]
    KHAYA = M.BARE[P2(142, "a")].removeprefix("hiểu biết về ")    # sự diệt tận
    add("1-1380", gloss(VIJJA, f"ba loại {VIJJA} {DASH} hiểu biết về sự nhớ lại các đời sống trước là {VIJJA}, "
                               f"hiểu biết về sự chết và tái sinh của chúng sinh là {VIJJA}, hiểu biết về {KHAYA} "
                               f"các {G.ASAVA_N} là {VIJJA}."))
    VIM = M.BARE[P2(141, "b")]
    add("1-1381", gloss(VIM, f"hai loại giải thoát {DASH} sự thoát ly của tâm{M.V('p', 'Sī., Syā.', 'cittassa ca')}, "
                             "và Niết-bàn."))
    add("1-1382", gloss(M.BARE[P2(142, "a")], "hiểu biết của người có được con đường."))
    add("1-1383", gloss(M.BARE[P2(142, "b")], "hiểu biết của người có được thành quả."), END_KANDA)
    order = [b for b, _ in P.items()]
    S.sort(key=lambda s: order.index(s[0]))
    return S


# =========================================================================================
# 7. Build and checks
# =========================================================================================
def pali_segments(part):
    segs, buf = [], []
    for line in (PALI_DIR / part).read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        m = G.ID.search(line)
        if m:
            buf.append(line[:m.start()])
            segs.append((m.group(1), buf))
            buf = []
        else:
            buf.append(line)
    assert not buf, "trailing lines without id"
    return segs


def same_pali_checks(P):
    """segments reused from 4-01 must have the same Pāli words"""
    for new, old in (("1-1237", "1-1066"), ("1-1261", "1-1006"), ("1-1268", "1-1013"), ("1-1273", "1-1018"),
                     ("1-1283", "1-1004"), ("1-1285", "1-1005")):
        a = words(P[new][0].split("? ", 1)[1])
        b = words(P401[old][0].split("? ", 1)[1])
        assert a == b, (new, old)
    for new, old in (("1-1264", "1-1010"), ("1-1271", "1-1017")):
        tail = P[new][0].split("sīlabbataparāmāso. ", 1)[1]
        assert words(tail) == words(P401[old][0]), (new, old)
    # the same definition bodies (Pāli words, brackets and punctuation ignored) as the 4-01 segments whose
    # Vietnamese formula is used; only the defined name differs
    def body_p(line):
        # «patiṭṭhāho» in the diṭṭhi string = 2-04 / 4-01 «paṭiggāho» («sự bám chặt», 4-01 notes)
        line = re.sub(r" \[[^\]]*\]", "", line).split("? ", 1)[1].replace("patiṭṭhāho", "paṭiggāho")
        return words(re.split(rf" {DASH} (?:ayaṃ|idaṃ) vuccati | {DASH} ime dhammā ", line)[0])

    for new, old in (("1-1159", "1-1103"), ("1-1220", "1-1103"), ("1-1236", "1-1141"), ("1-1167", "1-1008"),
                     ("1-1241", "1-1123"), ("1-1238", "1-1067"), ("1-1168", "1-1106"), ("1-1181", "1-1105"),
                     ("1-1240", "1-1105"), ("1-1239", "1-1121"), ("1-1160", "1-1066"), ("1-1249", "1-997"),
                     ("1-1250", "1-1012"), ("1-1302", "1-1012"), ("1-1266", "1-1011"), ("1-1217", "1-994"),
                     ("1-1222", "1-1009"), ("1-1223", "1-1007"), ("1-1281", "1-1003"), ("1-1297", "1-1035")):
        a, b = body_p(P[new][0]), body_p(P401[old][0])
        if new == "1-1223":   # four aggregates abbreviated with …pe…
            a, b = a[:a.index("vedanaṃ")], b[:b.index("vedanaṃ")]
        if new == "1-1297":   # «micchādiṭṭhi niyatā» (two words) for «micchādiṭṭhiniyatā»; + the four paths
            a, b = a[:5], b[:5]
        if new == "1-1222":   # 4-01 quotes the slogan (‘…’ti); here «suddhīti»
            a, b = a[:8], b[:8]
        assert a == b, (new, old, [(x, y) for x, y in zip(a, b) if x != y][:3], len(a), len(b))


def ndash(s):
    return s.count("–") + s.count("—")


def build(part, fn):
    psegs = pali_segments(part)
    P = dict(psegs)
    segs = fn(P)
    assert [b for b, _ in segs] == [b for b, _ in psegs], (
        part, [(a, b) for (a, _), (b, _) in zip(segs, psegs) if a != b][:3])
    out = []
    for (bid, lines), (_, plines) in zip(segs, psegs):
        assert len(lines) == len(plines), (bid, len(lines), len(plines))
        for p, r in zip(plines, lines):
            assert ndash(p) == ndash(r), (bid, ndash(p), ndash(r), r)
            assert p.count("[") == r.count("["), (bid, p.count("["), r.count("["))
            assert p.count("…pe…") == r.count(ELL), (bid, p.count("…pe…"), r.count(ELL), r)
            assert p.count("?") == r.count("?"), (bid, p.count("?"), r.count("?"))
            assert p.startswith("#") == r.startswith("#"), (bid, p, r)
            assert "  " not in r and " ," not in r and ",," not in r and ".." not in r, (bid, r)
            if p.startswith("#"):
                assert HEAD[p] == r, (bid, p, r)
        lines = list(lines)
        lines[-1] += f" ^{bid}"
        out.append("\n".join(lines))
    text = "\n\n".join(out) + "\n"
    assert "—" not in text and ":-" not in text and "pe…" not in text and "\n\n\n" not in text
    assert unicodedata.normalize("NFC", text) == text
    return text, len(segs), P


if __name__ == "__main__":
    print("headings / closing lines checked:", check_headings())
    t2, n2, P2_ = build(PARTS[0], build_402)
    same_pali_checks(P2_)
    t3, n3, _ = build(PARTS[1], build_403)
    for name, t, n in ((PARTS[0], t2, n2), (PARTS[1], t3, n3)):
        (OUT_DIR / name).write_text(t, encoding="utf-8", newline="\n")
        print("wrote", OUT_DIR / name, "segments", n)
