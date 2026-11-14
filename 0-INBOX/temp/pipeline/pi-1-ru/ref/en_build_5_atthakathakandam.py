"""Build the English plain zero-shot of pi-1 chapter 5 (5-atthakathakandam.md).

usage: python -I -X utf8 build_5_atthakathakandam.py
Every matrix item named in a question or answer comes from build_matika.MATRIX_ITEMS
(variant bracket and final full stop dropped, first letter lower-cased inside a sentence).
All mind-class phrases are fixed constants below, so every repeat is byte-identical.
"""
import pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import build_matika as M  # noqa: E402  (importing does not write anything)

ROOT = HERE.parents[3]
PALI = ROOT / "AI_translation" / "pali" / "pi-1_split_chapters" / "5-atthakathakandam.md"
OUT = ROOT / "AI_translation" / "english" / "pi-1-english-plain-zeroshot_split_chapters" / "5-atthakathakandam.md"

DASH = "–"

# ---- matrix items -----------------------------------------------------------------------
ITEMS = {}
for bid, letter, pali, eng in M.MATRIX_ITEMS:
    ITEMS[(bid, letter)] = (pali, eng)


def ref_key(ref):
    """'T1a' -> ('1-M1-1', 'a'); 'P83b' -> ('1-M2-83', 'b')."""
    m = re.fullmatch(r"([TP])(\d+)([abc])", ref)
    return ("1-M1-" if m.group(1) == "T" else "1-M2-") + m.group(2), m.group(3)


def it(ref):
    eng = ITEMS[ref_key(ref)][1]
    eng = re.sub(r" \[variant: [^\]]*\]", "", eng)
    assert eng.endswith("."), eng
    eng = eng[:-1]
    return eng[0].lower() + eng[1:]


def cap(s):
    return s[0].upper() + s[1:]


def Q(ref):
    return f"What are {it(ref)}?"


def E(ref):
    return f"{DASH} these are {it(ref)}."


def QA(ref, answer, tail=""):
    s = Q(ref) + " " + cap(answer) + " " + E(ref)
    return s + (" " + tail if tail else "")


def NV(refs, dash=False):
    """na vattabbā A-tipi, B-tipi ... = not to be counted among A, nor among B ..."""
    s = "not to be counted " + (DASH + " " if dash else "") + "among " + it(refs[0])
    return s + "".join(", nor among " + it(r) for r in refs[1:])


def LA(*xs):
    """list whose last member carries Pāli 'ca': a, b and c"""
    return ", ".join(xs[:-1]) + " and " + xs[-1] if len(xs) > 1 else xs[0]


def LC(*xs):
    """plain comma list (no 'ca' in the Pāli)"""
    return ", ".join(xs)


# ---- mind classes (see notes-5.md) -------------------------------------------------------
K4 = "the wholesome mind of the four planes"            # catūsu bhūmīsu kusalaṃ
K3 = "the wholesome mind of the three planes"           # tīsu bhūmīsu kusalaṃ
AK = "the unwholesome mind"                             # akusalaṃ
V4 = "the results of the four planes"                   # catūsu bhūmīsu vipāko
V3 = "the results of the three planes"                  # tīsu bhūmīsu vipāko
F3 = "the indeterminate functional mind of the three planes"  # tīsu bhūmīsu kiriyābyākataṃ
R = "material form"                                     # rūpaṃ
ALLR = "all material form"                              # sabbañca rūpaṃ
NB = "Nibbāna"
KAMK = "the wholesome mind of the sense sphere"         # kāmāvacarakusalaṃ
KAMV = "the results of the sense sphere"                # kāmāvacarassa vipāko
ALL_KAMV = "all the results of the sense sphere"        # sabbo kāmāvacarassa vipāko
KAMKIR = "the indeterminate functional mind of the sense sphere"  # kāmāvacarakiriyābyākataṃ
ALL_AK = "every unwholesome mind"                       # sabbaṃ akusalaṃ
REST_AK = "the remaining unwholesome mind"              # avasesaṃ akusalaṃ
AK12 = "the twelve arisings of unwholesome mind"        # dvādasa akusalacittuppādā

KAMK_F = "from " + KAMK                                 # kāmāvacarakusalato
AK_F = "from the unwholesome mind"                      # akusalato
KAMKV_F = "from the results of " + KAMK                 # kāmāvacarakusalassa vipākato
AKV_F = "from the results of the unwholesome mind"      # akusalassa vipākato
KIR_F = "from the functional mind"                      # kiriyato
KAMV_F = "from " + KAMV                                 # kāmāvacarassa vipākato
KAMKIR_F = "from the functional mind of the sense sphere"  # kāmāvacarakiriyato

AHC = "the arisings of mind without roots"              # ahetuke cittuppāde
V4X = f"{V4} except for {AHC} {KAMV_F}"
F3X = f"{F3} except for {AHC} {KAMKIR_F}"

SOM = "arisings of mind accompanied by joy"             # somanassasahagatacittuppādā
UPE = "arisings of mind accompanied by equanimity"      # upekkhāsahagatacittuppādā
NSAMP = "arisings of mind associated with knowledge"    # ñāṇasampayuttacittuppādā
NVIPP = "arisings of mind dissociated from knowledge"   # ñāṇavippayuttacittuppādā
CU = "arisings of mind"                                 # cittuppādā

DIT4 = "the four arisings of mind associated with wrong view"          # cattāro diṭṭhigatasampayuttacittuppādā
LOBDV4 = "the four arisings of mind accompanied by greed and dissociated from wrong view"
LOBDS4 = "the four arisings of mind accompanied by greed and associated with wrong view"
LOB8 = "the eight arisings of mind accompanied by greed"              # aṭṭha lobhasahagatacittuppādā
DOM2 = "the two arisings of mind accompanied by sadness"              # dve domanassasahagatacittuppādā
VIC = "the arising of mind accompanied by doubt"                      # vicikicchāsahagato cittuppādo
UDD = "the arising of mind accompanied by restlessness"               # uddhaccasahagato cittuppādo
VICS = "the arisings of mind accompanied by doubt"                    # vicikicchāsahagatesu cittuppādesu
UDDS = "the arisings of mind accompanied by restlessness"             # uddhaccasahagatesu cittuppādesu
SASANKH = "the prompted unwholesome minds"                            # sasaṅkhārikesu akusalesu
ALL_AKS = "all unwholesome minds"                                     # sabbākusalesu
VICMOHA = "the delusion accompanied by doubt"                         # vicikicchāsahagato moho
UDDMOHA = "the delusion accompanied by restlessness"                  # uddhaccasahagato moho
VUMOHA = f"{VICMOHA} and {UDDMOHA}"     # vicikicchāsahagataṃ uddhaccasahagataṃ mohaṃ
DOMMOHA = f"the delusion arisen in {DOM2}"  # dvīsu domanassasahagatesu cittuppādesu uppanno moho

PV = "the two sets of five kinds of sense consciousness"   # dvepañcaviññāṇāni
MD3 = "the three mind elements"                            # tisso manodhātuyo
AHM5 = "the five mind-consciousness elements without roots"  # pañca ahetukamanoviññāṇadhātuyo
KIRMD = "the functional mind element"                      # kiriyāmanodhātu
KIRAH_SOM = "the functional mind-consciousness element without roots and accompanied by joy"
KIRAH_UPE = "the functional mind-consciousness element without roots and accompanied by equanimity"
DUKKHA_KV = "body consciousness accompanied by pain"       # dukkhasahagataṃ kāyaviññāṇaṃ

M4 = "the four paths not included in the spheres of existence"   # cattāro maggā apariyāpannā
P4 = "the four fruits of the contemplative life"                # cattāri sāmaññaphalāni
MPN = LA(M4, P4, NB)
MP = LA(M4, P4)

KAMMA = "whatever material form is due to action having been done"        # yañca rūpaṃ kammassa katattā
NKAMMA = "whatever material form is not due to action having been done"   # yañca rūpaṃ na kammassa katattā
RDH = "whatever material form is invisible, makes no impact and is included in the mental-object base"

KVK = "(wholesome, resultant and functional)"   # kusalato ca vipākato ca kiriyato ca
KV = "(wholesome and resultant)"                 # kusalato ca vipākato ca
KK = "(wholesome and functional)"                # kusalato ca kiriyato ca

R1J = "the first absorption of the fine-material sphere"
R4J = "the fourth absorption of the fine-material sphere"
L1J = "the first world-transcending absorption"
L4J = "the fourth world-transcending absorption"
R2J5 = "the second absorption of the fine-material sphere in the fivefold method"
L2J5 = "the second world-transcending absorption in the fivefold method"
J4V = "the result of the fourth absorption"       # catutthassa jhānassa vipāko
ARU4 = "the four immaterial attainments"          # cattāro āruppā
ARV4 = "the four minds of the immaterial sphere"  # cattāro arūpāvacarā
AKAS = "the base of infinite space"
VINN = "the base of infinite consciousness"
AKIN = "the base of nothingness"
NEVA = "the base of neither perception nor non-perception"


def JH(kind, a, b):
    """rūpāvacara/lokuttara + <a><b>jjhānā (e.g. tikacatukka = three, four)."""
    pl = "" if a == "one" else "s"
    head = (f"the {a} absorption{pl} of the fine-material sphere" if kind == "r"
            else f"the {a} world-transcending absorption{pl}")
    return f"{head} in the fourfold method and the {b} in the fivefold method"


def ETTH(x):
    return f"except for the {x} arisen here"


def SIYA(*parts):
    return "these are " + ", ".join(parts)


EYE_TOUCH = "the eye base … the touch base"
NOOBJ = cap(LA(R, NB)) + " are " + it("P55b") + "."   # Rūpañca nibbānañca anārammaṇā.

# ---- recurring answer lists ----------------------------------------------------------
A4 = LA(K4, AK, V4, F3, R, NB)              # catūsu kusalaṃ, akusalaṃ, catūsu vipāko, tīsu kiriyā, rūpañca, nibbānañca
A4_NOAK = LA(K4, V4, F3, R, NB)
A3R = LA(K3, AK, V3, F3, ALLR)              # tīsu kusalaṃ, akusalaṃ, tīsu vipāko, tīsu kiriyā, sabbañca rūpaṃ
A3R_NOAK = LA(K3, V3, F3, ALLR)
A4R = LA(K4, AK, V4, F3, ALLR)              # catūsu ..., sabbañca rūpaṃ
A4_INV = LC(K4, AK, V4, F3, RDH) + ", and " + NB
SAHETU = LC(K4, AK, V4X, F3X)
SAHETU_A = LC("except for " + VUMOHA, REST_AK, K4, V4X, F3X)
AHETU = LA(VICMOHA, UDDMOHA, PV, MD3, AHM5, R, NB)

# feeling / rapture / happiness / equanimity lists
L_SUKHA_V = LC(f"the four {SOM} {KAMK_F}", f"four {AK_F}", f"five {KAMKV_F} and {KIR_F}", JH("r", "three", "four") + " " + KVK,
               JH("l", "three", "four") + " " + KV)
L_UPE = LC(f"the four {UPE} {KAMK_F}", f"six {AK_F}", f"ten {KAMKV_F}", f"six {AKV_F}", f"six {KIR_F}",
           R4J + " " + KVK)
L_PITI = LC(f"the four {SOM} {KAMK_F}", f"four {AK_F}", f"five {KAMKV_F}", f"five {KIR_F}",
            JH("r", "two", "three") + " " + KVK, JH("l", "two", "three") + " " + KV)
L_SUKHA = LC(f"the four {SOM} {KAMK_F}", f"four {AK_F}", f"six {KAMKV_F}", f"five {KIR_F}",
             JH("r", "three", "four") + " " + KVK, JH("l", "three", "four") + " " + KV)
L_UPEKKHA = LC(L_UPE, ARU4 + " " + KVK, L4J + " " + KV)
L_APITI = LC(f"the four {UPE} {KAMK_F}", f"eight {AK_F}", f"eleven {KAMKV_F}", f"seven {AKV_F}",
             f"six {KIR_F}", JH("r", "two", "two") + " " + KVK, ARU4 + " " + KVK,
             JH("l", "two", "two") + " " + KV)
L_SAVITAKKA = LC(KAMK, AK, f"eleven {CU} {KAMKV_F}", f"two {AKV_F}", f"eleven {KIR_F}",
                 R1J + " " + KVK, L1J + " " + KV)

# ---- segments --------------------------------------------------------------------------
S = {}

S["1-4-0"] = ["### The Chapter of Explanations"]
S["1-4-1-0"] = ["#### Explanation of the Sets of Three"]

S["1-1384"] = [QA("T1a", K4)]
S["1-1385"] = [QA("T1b", AK12)]
S["1-1386"] = [QA("T1c", LA(V4, F3, R, NB))]
S["1-1387"] = [QA("T2a", L_SUKHA_V + ", " + ETTH("pleasant feeling"))]
S["1-1388"] = [QA("T2b", LC(DOM2, DUKKHA_KV) + ", " + ETTH("painful feeling"))]
S["1-1389"] = [QA("T2c", LC(L_UPE, ARV4 + " " + KVK, L4J + " " + KV) + ", "
                  + ETTH("feeling that is neither painful nor pleasant"),
                  cap(LA("the three feelings", R, NB)) + " " + DASH + " these are "
                  + NV(["T2a", "T2b", "T2c"]) + ".")]
S["1-1390"] = [QA("T3a", V4)]
S["1-1391"] = [QA("T3b", LC(K4, AK))]
S["1-1392"] = [QA("T3c", LA(F3, R, NB))]
S["1-1393"] = [QA("T4a", LA(V3, KAMMA))]
S["1-1394"] = [QA("T4b", LA(K3, AK, F3, NKAMMA))]
S["1-1395"] = [QA("T4c", MPN)]
S["1-1396"] = [QA("T5a", AK12)]
S["1-1397"] = [QA("T5b", A3R_NOAK)]
S["1-1398"] = [QA("T5c", MPN)]
S["1-1399"] = [QA("T6a", L_SAVITAKKA + ", " + ETTH("applied thought and sustained thought"))]
S["1-1400"] = [QA("T6b", LC(R2J5 + " " + KVK, L2J5 + " " + KV) + ", " + ETTH("sustained thought")
                  + ", and applied thought")]
S["1-1401"] = [QA("T6c", LC(PV, JH("r", "three", "three") + " " + KVK, ARU4 + " " + KVK,
                            JH("l", "three", "three") + " " + KV)
                  + ", the sustained thought arisen in the second absorption [variant: dutiyajjhāne (Sī.)] "
                    "of the fivefold method, " + LA(R, NB),
                  "Sustained thought arisen together with applied thought is " + NV(["T6a", "T6b", "T6c"]) + ".")]
S["1-1402"] = [QA("T7a", L_PITI + ", " + ETTH("rapture"))]
S["1-1403"] = [QA("T7b", L_SUKHA + ", " + ETTH("happiness"))]
S["1-1404"] = [QA("T7c", L_UPEKKHA + ", " + ETTH("equanimity"),
                  f"Rapture does not belong to {it('T7a')}; it belongs to {it('T7b')}; "
                  f"it does not belong to {it('T7c')}. "
                  f"Happiness does not belong to {it('T7b')}; it sometimes belongs to {it('T7a')}; "
                  f"it does not belong to {it('T7c')}; and sometimes it is {NV(['T7a'])}. "
                  + cap(LA(DOM2, DUKKHA_KV, "the feeling that is equanimity", R, NB)) + " " + DASH
                  + " these are " + NV(["T7a", "T7b", "T7c"]) + ".")]
S["1-1405"] = [QA("T8a", LC(DIT4, VIC))]
S["1-1406"] = [QA("T8b", UDD, cap(LC(LOBDV4, DOM2)) + " " + DASH + " "
                  + SIYA(f"sometimes {it('T8a')}", f"sometimes {it('T8b')}") + ".")]
S["1-1407"] = [QA("T8c", A4_NOAK)]
S["1-1408"] = [QA("T9a", LC(DIT4, VIC) + ", " + ETTH("delusion"))]
S["1-1409"] = [QA("T9b", UDD + ", " + ETTH("delusion"), cap(LC(LOBDV4, DOM2)) + " " + DASH + " "
                  + SIYA(f"sometimes {it('T9a')}", f"sometimes {it('T9b')}") + ".")]
S["1-1410"] = [QA("T9c", LA(VICMOHA, UDDMOHA, K4, V4, F3, R, NB))]
S["1-1411"] = [QA("T10a", LC(K3, AK))]
S["1-1412"] = [QA("T10b", M4)]
S["1-1413"] = [QA("T10c", LA(V4, F3, R, NB))]
S["1-1414"] = [QA("T11a", LA(M4, "the three lower fruits of the contemplative life"))]
S["1-1415"] = [QA("T11b", "the highest fruit, the fruit of arahantship")]
S["1-1416"] = [QA("T11c", LA(K3, AK, V3, F3, R, NB))]
S["1-1417"] = [QA("T12a", LA(KAMK, AK, ALL_KAMV, KAMKIR, ALLR))]
S["1-1418"] = [QA("T12b", LC(it("P94a"), it("P95a"), "wholesome and indeterminate"))]
S["1-1419"] = [QA("T12c", MPN)]
S["1-1420"] = [QA("T13a", LC(ALL_KAMV, KIRMD, KIRAH_SOM))]
S["1-1421"] = [QA("T13b", LC(VINN, NEVA))]
S["1-1422"] = [QA("T13c", MP,
                  cap(LC(f"the four {NVIPP} {KAMK_F}", f"the four {NVIPP} {KIR_F}", ALL_AK)) + " " + DASH + " "
                  + SIYA(f"sometimes {it('T13a')}", f"sometimes {it('T13b')}", f"not {it('T13c')}",
                         f"and sometimes {NV(['T13a', 'T13b'])}") + ". "
                  + cap(LC(f"the four {NSAMP} {KAMK_F}", f"the four {NSAMP} {KIR_F}", R4J + " " + KK, KIRAH_UPE))
                  + " " + DASH + " "
                  + SIYA(f"sometimes {it('T13a')}", f"sometimes {it('T13b')}", f"sometimes {it('T13c')}",
                         f"and sometimes {NV(['T13a', 'T13b', 'T13c'])}") + ". "
                  + cap(LC(JH("r", "three", "four") + " " + KVK, J4V, AKAS, AKIN)) + " " + DASH
                  + " these are " + NV(["T13a", "T13b", "T13c"]) + ". " + NOOBJ)]
S["1-1423"] = [QA("T14a", AK12)]
S["1-1424"] = [QA("T14b", A3R_NOAK)]
S["1-1425"] = [QA("T14c", MPN)]
S["1-1426"] = [Q("T15a") + " " + cap(LC(DIT4, DOM2)) + " " + DASH + " "
               + SIYA(f"sometimes {it('T15a')}", f"sometimes {it('T15c')}") + "."]
S["1-1427"] = [QA("T15b", M4)]
S["1-1428"] = [QA("T15c", LA(LOBDV4, VIC, UDD, K3, V4, F3, R, NB))]
S["1-1429"] = [Q("T16a") + " " + cap(LC(f"the four {NSAMP} {KAMK_F}", f"the four {NSAMP} {KIR_F}")) + " "
               + DASH + " these are sometimes " + it("T16a") + ", not " + it("T16b") + "; sometimes "
               + it("T16c") + ", and sometimes " + NV(["T16a", "T16c"]) + ". "
               + "The four noble paths are not " + it("T16a") + ", but " + it("T16b") + "; sometimes "
               + it("T16c") + ", and sometimes " + NV(["T16c"]) + ". "
               + cap(LC(R4J + " " + KK, KIRAH_UPE)) + " " + DASH + " these are sometimes " + it("T16a")
               + "; not " + it("T16b") + ", not " + it("T16c") + "; and sometimes " + NV(["T16a"]) + ". "
               + cap(LC(f"the four {NVIPP} {KAMK_F}", ALL_AK, ALL_KAMV, f"six {CU} {KIR_F}",
                        JH("r", "three", "four") + " " + KVK, J4V, ARU4 + " " + KVK)
                     + ", and " + P4) + " " + DASH + " these are " + NV(["T16a", "T16b", "T16c"]) + ". " + NOOBJ]
S["1-1430"] = [Q("T17a") + " " + cap(LA(V4, KAMMA)) + " " + DASH + " these are sometimes "
               + it("T17a") + ", sometimes " + it("T17c") + "; they are " + NV(["T17b"]) + ". "
               + cap(LA(K4, AK, F3, NKAMMA)) + " " + DASH + " these are sometimes " + it("T17a")
               + ", sometimes " + it("T17b") + "; they are " + NV(["T17c"]) + ". "
               + "Nibbāna is " + NV(["T17a", "T17b", "T17c"]) + "."]
S["1-1431"] = ["Except for Nibbāna, all states are sometimes " + it("T18a") + ", sometimes " + it("T18b")
               + ", sometimes " + it("T18c") + ". Nibbāna is " + NV(["T18a", "T18b", "T18c"]) + "."]
S["1-1432"] = [QA("T19a", LC(VINN, NEVA))]
S["1-1433"] = ["There are no states that are invariably " + it("T19b") + "."]
S["1-1434"] = [QA("T19c", LA(PV, MD3),
                  cap(LC(f"ten {CU} {KAMKV_F}",
                         f"the mind-consciousness element accompanied by equanimity {AKV_F}", KIRAH_SOM))
                  + " " + DASH + " " + SIYA(f"sometimes {it('T19a')}", f"sometimes {it('T19b')}",
                                            f"sometimes {it('T19c')}") + ". "
                  + cap(LC(KAMK, AK, f"nine {CU} {KIR_F}", R4J + " " + KK)) + " " + DASH + " "
                  + SIYA(f"sometimes {it('T19a')}", f"sometimes {it('T19b')}", f"sometimes {it('T19c')}")
                  + "; and sometimes " + NV(["T19a", "T19b", "T19c"]) + ". "
                  + cap(LC(JH("r", "three", "four") + " " + KVK, J4V, AKAS, AKIN, MP)) + " " + DASH
                  + " these are " + NV(["T19a", "T19b", "T19c"]) + ". " + NOOBJ)]
ANIND = "material form not bound up with the faculties"
S["1-1435"] = [f"Except for {ANIND} and Nibbāna, all states are sometimes {it('T20a')}, sometimes "
               f"{it('T20b')}, sometimes {it('T20c')}. {cap(ANIND)} and Nibbāna are {it('T20b')}."]
S["1-1436"] = [QA("T21a", LC(VINN, NEVA))]
S["1-1437"] = [QA("T21b", LC(JH("r", "three", "four") + " " + KVK, J4V, AKAS, MP),
                  "Except for material form, all the wholesome, unwholesome and indeterminate states of the "
                  "sense sphere, " + R4J + " " + KK + " " + DASH + " "
                  + SIYA(f"sometimes {it('T21a')}", f"sometimes {it('T21b')}", f"sometimes {it('T21c')}")
                  + ". " + cap(AKIN) + " is " + NV(["T21a", "T21b", "T21c"]) + ". " + NOOBJ)]
S["1-1438"] = [QA("T22a", "the visible-form base")]
S["1-1439"] = [QA("T22b", EYE_TOUCH)]
S["1-1440"] = [QA("T22c", A4_INV), "The sets of three."]

S["1-4-2-0"] = ["#### Explanation of the Pairs"]
for n in range(1, 14):
    S[f"1-4-2-{n}-0"] = [M.GROUPS[f"1-M-2-{n}-0"][0]]

# -- roots
S["1-1441"] = [
    Q("P1a") + " Three wholesome roots, three unwholesome roots, three indeterminate roots. "
    f"Non-greed as a wholesome root and non-hate as a wholesome root arise in the wholesome minds of the four "
    f"planes. Non-delusion as a wholesome root arises in the wholesome minds of the four planes, except for "
    f"the four {NVIPP} {KAMK_F}.",
    f"Greed arises in {LOB8}. Hate arises in {DOM2}. Delusion arises in {ALL_AKS}.",
    f"Non-greed as a resultant root and non-hate as a resultant root arise in the results of the four planes, "
    f"except for {AHC} {KAMV_F}. Non-delusion as a resultant root arises in the results of the four planes, "
    f"except for {AHC} {KAMV_F}, and except for the four {NVIPP}.",
    f"Non-greed as a functional root and non-hate as a functional root arise in the functional minds of the "
    f"three planes, except for {AHC} {KAMKIR_F}. Non-delusion as a functional root arises in the functional "
    f"minds of the three planes, except for {AHC} {KAMKIR_F}, and except for the four {NVIPP} " + E("P1a"),
]
S["1-1442"] = [QA("P1b", "except for the roots, " + A4)]
S["1-1443"] = [QA("P2a", SAHETU_A)]
S["1-1444"] = [QA("P2b", AHETU)]
S["1-1445"] = [QA("P3a", SAHETU_A)]
S["1-1446"] = [QA("P3b", AHETU)]
S["1-1447"] = [QA("P4a", "where two or three roots arise together")]
S["1-1448"] = [QA("P4b", SAHETU + ", " + ETTH("roots"),
                  cap(it("P2b")) + " are " + NV(["P4a", "P4b"], dash=True) + ".")]
S["1-1449"] = [QA("P5a", "where two or three roots arise together")]
S["1-1450"] = [QA("P5b", SAHETU + ", " + ETTH("roots"),
                  cap(it("P3b")) + " are " + NV(["P5a", "P5b"], dash=True) + ".")]
S["1-1451"] = [QA("P6a", SAHETU + ", " + ETTH("roots"))]
S["1-1452"] = [QA("P6b", LA(PV, MD3, AHM5, R, NB),
                  cap(it("P1a")) + " are " + NV(["P6a", "P6b"], dash=True) + ".")]

# -- short intermediate pairs
S["1-1453"] = [QA("P7a", A4R)]
S["1-1454"] = [QA("P7b", NB)]
S["1-1455"] = [QA("P8a", A4R)]
S["1-1456"] = [QA("P8b", NB)]
S["1-1457"] = [QA("P9a", "the visible-form base")]
S["1-1458"] = [QA("P9b", EYE_TOUCH + ", " + A4_INV)]
S["1-1459"] = [QA("P10a", EYE_TOUCH)]
S["1-1460"] = [QA("P10b", A4_INV)]
S["1-1461"] = [QA("P11a", LA("the four great elements", "the material form derived from the four great elements"))]
S["1-1462"] = [QA("P11b", LA(K4, AK, V4, F3, NB))]
S["1-1463"] = [QA("P12a", A3R)]
S["1-1464"] = [QA("P12b", MPN, "All [variant: sabbeva (Syā.)] states are " + it("P13a") + " and " + it("P13b") + ".")]


# taints ^1-1465 ... ^1-1476
S["1-1465"] = [Q("P14a") + " The four taints " + DASH + " the taint of sensual desire, the taint of existence, "
               f"the taint of views, the taint of ignorance. The taint of sensual desire arises in {LOB8}, "
               f"the taint of existence arises in {LOBDV4}, the taint of views arises in {DIT4}. "
               f"The taint of ignorance arises in {ALL_AKS} " + E("P14a")]
S["1-1466"] = [QA("P14b", "except for the taints, " + LA(REST_AK, K4, V4, F3, R, NB))]
S["1-1467"] = [QA("P15a", A3R)]
S["1-1468"] = [QA("P15b", MPN)]
S["1-1469"] = [QA("P16a", f"{DOM2}, {ETTH('delusion')}; except for {VUMOHA}, {REST_AK}")]
S["1-1470"] = [QA("P16b", LA(DOMMOHA, VICMOHA, UDDMOHA, K4, V4, F3, R, NB))]
S["1-1471"] = [Q("P17a") + " Those same taints are " + it("P17a") + "."]
S["1-1472"] = [QA("P17b", "except for the taints, " + LA(REST_AK, K3, V3, F3, ALLR),
                  cap(it("P15b")) + " are " + NV(["P17a", "P17b"], dash=True) + ".")]
S["1-1473"] = [QA("P18a", "where two or three taints arise together")]
S["1-1474"] = [QA("P18b", "except for the taints, " + REST_AK,
                  cap(it("P16b")) + " are " + NV(["P18a", "P18b"], dash=True) + ".")]
S["1-1475"] = [QA("P19a", LA(DOMMOHA, VICMOHA, UDDMOHA, K3, V3, F3, ALLR))]
S["1-1476"] = [QA("P19b", MPN, cap(it("P16a")) + " are " + NV(["P19a", "P19b"], dash=True) + ".")]

# fetters ^1-1477 ... ^1-1488
F_LIST = ("the fetter of sensual lust, the fetter of aversion, the fetter of conceit, the fetter of views, "
          "the fetter of doubt, the fetter of misapprehension of rules and observances, the fetter of lust for "
          "existence, the fetter of envy, the fetter of stinginess, the fetter of ignorance")
S["1-1477"] = [Q("P20a") + " The ten fetters " + DASH + " " + F_LIST + ". "
               f"The fetter of sensual lust arises in {LOB8}. The fetter of aversion arises in {DOM2}. "
               f"The fetter of conceit arises in {LOBDV4}. The fetter of views arises in {DIT4}. "
               f"The fetter of doubt arises in {VICS}. The fetter of misapprehension of rules and observances "
               f"arises in {DIT4}. The fetter of lust for existence arises in {LOBDV4}. The fetter of envy and "
               f"the fetter of stinginess arise in {DOM2}. The fetter of ignorance arises in {ALL_AKS} "
               + E("P20a")]
# the Pāli question of ^1-1478 ends with a full stop (source slip), kept as written
S["1-1478"] = [Q("P20b")[:-1] + ". " + cap("except for the fetters, " + LA(REST_AK, K4, V4, F3, R, NB))
               + " " + E("P20b")]
S["1-1479"] = [QA("P21a", A3R)]
S["1-1480"] = [QA("P21b", MPN)]
S["1-1481"] = [QA("P22a", f"except for {UDDMOHA}, {REST_AK}")]
S["1-1482"] = [QA("P22b", LA(UDDMOHA, K4, V4, F3, R, NB))]
S["1-1483"] = [Q("P23a") + " Those same fetters are " + it("P23a") + "."]
S["1-1484"] = [QA("P23b", "except for the fetters, " + LA(REST_AK, K3, V3, F3, ALLR),
                  cap(it("P21b")) + " are " + NV(["P23a", "P23b"], dash=True) + ".")]
S["1-1485"] = [QA("P24a", "where two or three fetters arise together")]
S["1-1486"] = [QA("P24b", "except for the fetters, " + REST_AK,
                  cap(it("P22b")) + " are " + NV(["P24a", "P24b"], dash=True) + ".")]
S["1-1487"] = [QA("P25a", LA(UDDMOHA, K3, V3, F3, ALLR))]
S["1-1488"] = [QA("P25b", MPN, cap(it("P22a")) + " are " + NV(["P25a", "P25b"], dash=True) + ".")]

# ties ^1-1489 ... ^1-1500
T_COV = "the bodily tie of covetousness"
T_ILL = "the bodily tie of ill will"
T_SIL = "the bodily tie of misapprehension of rules and observances"
T_IDAM = "the bodily tie of dogmatic belief that this alone is true"
S["1-1489"] = [Q("P26a") + " The four ties " + DASH + " " + LC(T_COV, T_ILL, T_SIL, T_IDAM) + ". "
               f"{cap(T_COV)} arises in {LOB8}. {cap(T_ILL)} arises in {DOM2}. {cap(T_SIL)} and {T_IDAM} "
               f"arise in {DIT4} " + E("P26a")]
S["1-1490"] = [QA("P26b", "except for the ties, " + LA(REST_AK, K4, V4, F3, R, NB))]
S["1-1491"] = [QA("P27a", A3R)]
S["1-1492"] = [QA("P27b", MPN)]
S["1-1493"] = [QA("P28a", LC(DIT4, LOBDV4, ETTH("greed"), DOM2, ETTH("aversion")))]
GV = [f"the greed arisen in {LOBDV4}", f"the aversion arisen in {DOM2}", VIC, UDD]
S["1-1494"] = [QA("P28b", LA(*GV, K4, V4, F3, R, NB))]
S["1-1495"] = [Q("P29a") + " Those same ties are " + it("P29a") + "."]
S["1-1496"] = [QA("P29b", "except for the ties, " + LA(REST_AK, K3, V3, F3, ALLR),
                  cap(it("P27b")) + " are " + NV(["P29a", "P29b"], dash=True) + ".")]
S["1-1497"] = [QA("P30a", "where view and greed arise together")]
S["1-1498"] = [QA("P30b", LC(LOB8, DOM2) + ", " + ETTH("ties"),
                  cap(it("P28b")) + " are " + NV(["P30a", "P30b"], dash=True) + ".")]
S["1-1499"] = [QA("P31a", LA(*GV, K3, V3, F3, ALLR))]
S["1-1500"] = [QA("P31b", MPN, cap(it("P28a")) + " are " + NV(["P31a", "P31b"], dash=True) + ".")]

# floods, yokes (abridged in the Pāli)
S["1-1501"] = [f"What are {it('P32a')}…."]
S["1-1502"] = [f"What are {it('P38a')}…."]

# hindrances ^1-1503 ... ^1-1514
H_LIST = ("the hindrance of sensual desire, the hindrance of ill will, the hindrance of sloth and torpor, "
          "the hindrance of restlessness and remorse, the hindrance of doubt, the hindrance of ignorance")
S["1-1503"] = [Q("P44a") + " The six hindrances " + DASH + " " + H_LIST + ". "
               f"The hindrance of sensual desire arises in {LOB8}, the hindrance of ill will arises in {DOM2}, "
               f"the hindrance of sloth and torpor arises in {SASANKH}, the hindrance of restlessness arises in "
               f"{UDDS}, the hindrance of remorse arises in {DOM2}, the hindrance of doubt arises in {VICS}, "
               f"the hindrance of ignorance arises in {ALL_AKS} " + E("P44a")]
S["1-1504"] = [QA("P44b", "except for the hindrances, " + LA(REST_AK, K4, V4, F3, R, NB))]
S["1-1505"] = [QA("P45a", A3R)]
S["1-1506"] = [QA("P45b", MPN)]
S["1-1507"] = [QA("P46a", AK12)]
S["1-1508"] = [QA("P46b", A4_NOAK)]
S["1-1509"] = [Q("P47a") + " Those same hindrances are " + it("P47a") + "."]
S["1-1510"] = [QA("P47b", "except for the hindrances, " + LA(REST_AK, K3, V3, F3, ALLR),
                  cap(it("P45b")) + " are " + NV(["P47a", "P47b"], dash=True) + ".")]
S["1-1511"] = [QA("P48a", "where two or three hindrances arise together")]
S["1-1512"] = [QA("P48b", "except for the hindrances, " + REST_AK,
                  cap(it("P46b")) + " are " + NV(["P48a", "P48b"], dash=True) + ".")]
S["1-1513"] = [QA("P49a", A3R_NOAK)]
S["1-1514"] = [QA("P49b", MPN, cap(it("P46a")) + " are " + NV(["P49a", "P49b"], dash=True) + ".")]

# misapprehension ^1-1515 ... ^1-1524
S["1-1515"] = [QA("P50a", f"misapprehension by view arises in {DIT4}")]
S["1-1516"] = [QA("P50b", "except for misapprehension, " + LA(REST_AK, K4, V4, F3, R, NB))]
S["1-1517"] = [QA("P51a", A3R)]
S["1-1518"] = [QA("P51b", MPN)]
S["1-1519"] = [QA("P52a", DIT4 + ", " + ETTH("misapprehension"))]
PV4 = [LOBDV4, DOM2, VIC, UDD]
S["1-1520"] = [QA("P52b", LA(*PV4, K4, V4, F3, R, NB),
                  "Misapprehension is " + NV(["P52a", "P52b"], dash=True) + ".")]
S["1-1521"] = [Q("P53a") + " That same misapprehension is one of the " + it("P53a") + "."]
S["1-1522"] = [QA("P53b", "except for misapprehension, " + LA(REST_AK, K3, V3, F3, ALLR),
                  cap(it("P51b")) + " are " + NV(["P53a", "P53b"], dash=True) + ".")]
S["1-1523"] = [QA("P54a", LA(*PV4, K3, V3, F3, ALLR))]
S["1-1524"] = [QA("P54b", MPN, cap(it("P50a")) + " and " + it("P52a") + " are "
                  + NV(["P54a", "P54b"], dash=True) + ".")]

# long intermediate pairs ^1-1525 ... ^1-1552
AGG3 = "the aggregate of feeling, the aggregate of perception, the aggregate of mental formations"
INTIM = "bodily intimation, verbal intimation"
S["1-1525"] = [QA("P55a", LC(K4, AK, V4, F3))]
S["1-1526"] = [QA("P55b", LA(R, NB))]
S["1-1527"] = [QA("P56a", "eye consciousness, ear consciousness, nose consciousness, tongue consciousness, "
                          "body consciousness, the mind element, the mind-consciousness element")]
S["1-1528"] = [QA("P56b", AGG3 + ", " + LA(R, NB))]
S["1-1529"] = [QA("P57a", AGG3)]
S["1-1530"] = [QA("P57b", LA("mind", R, NB))]
S["1-1531"] = [QA("P58a", AGG3)]
S["1-1532"] = [QA("P58b", LA(R, NB), "Mind is not to be described " + DASH
                  + " as associated with mind, nor as dissociated from mind.")]
S["1-1533"] = [QA("P59a", AGG3)]
S["1-1534"] = [QA("P59b", LA(R, NB), "Mind is not to be described " + DASH
                  + " as joined with mind, nor as not joined with mind.")]
S["1-1535"] = [QA("P60a", AGG3 + ", " + INTIM + ", or whatever other material form there is that is born of "
                  "mind, caused by mind, arising from mind " + DASH + " the visible-form base, the sound base, "
                  "the smell base, the taste base, the touch base, the space element, the water element, "
                  "lightness of material form, pliancy of material form, workability of material form, "
                  "growth of material form, continuity of material form, the nutriment of solid food")]
NOT_CS = LA("mind", "the remaining material form", NB)
S["1-1536"] = [QA("P60b", NOT_CS)]
S["1-1537"] = [QA("P61a", AGG3 + ", " + INTIM)]
S["1-1538"] = [QA("P61b", NOT_CS)]
S["1-1539"] = [QA("P62a", AGG3 + ", " + INTIM)]
S["1-1540"] = [QA("P62b", NOT_CS)]
MRN = LA("mind", R, NB)
S["1-1541"] = [QA("P63a", AGG3)]
S["1-1542"] = [QA("P63b", MRN)]
S["1-1543"] = [QA("P64a", AGG3)]
S["1-1544"] = [QA("P64b", MRN)]
S["1-1545"] = [QA("P65a", AGG3)]
S["1-1546"] = [QA("P65b", MRN)]
S["1-1547"] = [QA("P66a", "the eye base … the mind base")]
S["1-1548"] = [QA("P66b", "the visible-form base … the mental-object base")]
S["1-1549"] = [QA("P67a", "the eye base … the nutriment of solid food")]
S["1-1550"] = [QA("P67b", LA(K4, AK, V4, F3, "the four great elements", NB))]
S["1-1551"] = [QA("P68a", LA(V3, KAMMA))]
S["1-1552"] = [QA("P68b", LA(K3, AK, F3, NKAMMA, M4, P4, NB))]

# clinging ^1-1553 ... ^1-1564
U_SENS = "clinging to sensual pleasures"
U_DIT = "clinging to views"
U_SIL = "clinging to rules and observances"
U_ATTA = "clinging to a doctrine of self"
S["1-1553"] = [Q("P69a") + " The four kinds of clinging " + DASH + " " + LC(U_SENS, U_DIT, U_SIL, U_ATTA) + ". "
               f"{cap(U_SENS)} arises in {LOB8}. {cap(U_DIT)}, {U_SIL} and {U_ATTA} arise in {DIT4} "
               + E("P69a")]
S["1-1554"] = [QA("P69b", "except for the kinds of clinging, " + LA(REST_AK, K4, V4, F3, R, NB))]
S["1-1555"] = [QA("P70a", A3R)]
S["1-1556"] = [QA("P70b", MPN)]
S["1-1557"] = [QA("P71a", LC(LOBDS4, LOBDV4) + ", " + ETTH("greed"))]
UV = [f"the greed arisen in {LOBDV4}", DOM2, VIC, UDD]
S["1-1558"] = [QA("P71b", LA(*UV, K4, V4, F3, R, NB))]
S["1-1559"] = [Q("P72a") + " Those same kinds of clinging are " + it("P72a") + "."]
S["1-1560"] = [QA("P72b", "except for the kinds of clinging, " + LA(REST_AK, K3, V3, F3, ALLR),
                  cap(it("P70b")) + " are " + NV(["P72a", "P72b"], dash=True) + ".")]
S["1-1561"] = [QA("P73a", "where view and greed arise together")]
S["1-1562"] = [QA("P73b", LOB8 + ", " + ETTH("kinds of clinging"),
                  cap(it("P71b")) + " are " + NV(["P73a", "P73b"], dash=True) + ".")]
S["1-1563"] = [QA("P74a", LA(*UV, K3, V3, F3, ALLR))]
S["1-1564"] = [QA("P74b", MPN, cap(it("P71a")) + " are " + NV(["P74a", "P74b"], dash=True) + ".")]

# defilements ^1-1565 ... ^1-1580
S["1-1565"] = [Q("P75a") + " The ten bases of defilement " + DASH + " greed, hate, delusion, conceit, view, "
               "doubt, sloth, restlessness, shamelessness, fearlessness of wrongdoing. "
               f"Greed arises in {LOB8}. Hate arises in {DOM2}. Delusion arises in {ALL_AKS}. "
               f"Conceit arises in {LOBDV4}. View arises in {DIT4}. Doubt arises in {VICS}. "
               f"Sloth arises in {SASANKH}. Restlessness, shamelessness and fearlessness of wrongdoing arise in "
               f"{ALL_AKS} " + E("P75a")]
S["1-1566"] = [QA("P75b", "except for the defilements, " + LA(REST_AK, K4, V4, F3, R, NB))]
S["1-1567"] = [QA("P76a", A3R)]
S["1-1568"] = [QA("P76b", MPN)]
S["1-1569"] = [QA("P77a", AK12)]
S["1-1570"] = [QA("P77b", A4_NOAK)]
S["1-1571"] = [QA("P78a", AK12)]
S["1-1572"] = [QA("P78b", A4_NOAK)]
S["1-1573"] = [Q("P79a") + " Those same defilements are " + it("P79a") + "."]
S["1-1574"] = [QA("P79b", "except for the defilements, " + LA(REST_AK, K3, V3, F3, ALLR),
                  cap(it("P76b")) + " are " + NV(["P79a", "P79b"], dash=True) + ".")]
S["1-1575"] = [Q("P80a") + " Those same defilements are " + it("P80a") + "."]
S["1-1576"] = [QA("P80b", "except for the defilements, " + REST_AK,
                  cap(it("P77b")) + " are " + NV(["P80a", "P80b"], dash=True) + ".")]
S["1-1577"] = [QA("P81a", "where two or three defilements arise together")]
S["1-1578"] = [QA("P81b", "except for the defilements, " + REST_AK,
                  cap(it("P78b")) + " are " + NV(["P81a", "P81b"], dash=True) + ".")]
S["1-1579"] = [QA("P82a", A3R_NOAK)]
S["1-1580"] = [QA("P82b", MPN, cap(it("P78a")) + " are " + NV(["P82a", "P82b"], dash=True) + ".")]

# closing pairs ^1-1581 ... ^1-1616
SIYA2 = cap(LC(LOBDV4, DOM2)) + " " + DASH + " "
S["1-1581"] = [QA("P83a", LC(DIT4, VIC), SIYA2 + SIYA(f"sometimes {it('P83a')}", f"sometimes {it('P83b')}") + ".")]
S["1-1582"] = [QA("P83b", LA(UDD, K4, V4, F3, R, NB))]
S["1-1583"] = [QA("P84a", UDD, SIYA2 + SIYA(f"sometimes {it('P84a')}", f"sometimes {it('P84b')}") + ".")]
S["1-1584"] = [QA("P84b", LA(DIT4, VIC, K4, V4, F3, R, NB))]
S["1-1585"] = [QA("P85a", LC(DIT4, VIC) + ", " + ETTH("delusion"),
                  SIYA2 + SIYA(f"sometimes {it('P85a')}", f"sometimes {it('P85b')}") + ".")]
S["1-1586"] = [QA("P85b", LA(VICMOHA, UDD, K4, V4, F3, R, NB))]
S["1-1587"] = [QA("P86a", UDD + ", " + ETTH("delusion"),
                  SIYA2 + SIYA(f"sometimes {it('P86a')}", f"sometimes {it('P86b')}") + ".")]
S["1-1588"] = [QA("P86b", LA(DIT4, VIC, UDDMOHA, K4, V4, F3, R, NB))]
S["1-1589"] = [QA("P87a", L_SAVITAKKA + ", " + ETTH("applied thought"))]
S["1-1590"] = [QA("P87b", LA(PV, JH("r", "three", "four") + " " + KVK, ARV4 + " " + KVK,
                             JH("l", "three", "four") + " " + KV, "applied thought", R, NB))]
S["1-1591"] = [QA("P88a", LC(KAMK, AK, f"eleven {CU} {KAMKV_F}", f"two {AKV_F}", f"eleven {KIR_F}",
                             JH("r", "one", "two") + " " + KVK, JH("l", "one", "two") + " " + KV)
                  + ", " + ETTH("sustained thought"))]
S["1-1592"] = [QA("P88b", LA(PV, JH("r", "three", "three") + " " + KVK, ARU4 + " " + KVK,
                             JH("l", "three", "three") + " " + KV, "sustained thought", R, NB))]
S["1-1593"] = [QA("P89a", L_PITI + ", " + ETTH("rapture"))]
S["1-1594"] = [QA("P89b", LA(L_APITI, "rapture", R, NB))]
S["1-1595"] = [QA("P90a", L_PITI + ", " + ETTH("rapture"))]
S["1-1596"] = [QA("P90b", LA(L_APITI, "rapture", R, NB))]
S["1-1597"] = [QA("P91a", L_SUKHA + ", " + ETTH("happiness"))]
S["1-1598"] = [QA("P91b", LA(f"the four {UPE} {KAMK_F}", f"eight {AK_F}", f"ten {KAMKV_F}", f"seven {AKV_F}",
                             f"six {KIR_F}", R4J + " " + KVK, ARU4 + " " + KVK, L4J + " " + KV,
                             "happiness", R, NB))]
S["1-1599"] = [QA("P92a", L_UPEKKHA + ", " + ETTH("equanimity"))]
S["1-1600"] = [QA("P92b", LA(f"the four {SOM} {KAMK_F}", f"six {AK_F}", f"six {KAMKV_F}", f"one {AKV_F}",
                             f"five {KIR_F}", JH("r", "three", "four") + " " + KVK,
                             JH("l", "three", "four") + " " + KV, "equanimity", R, NB))]
S["1-1601"] = [QA("P93a", LA(KAMK, AK, ALL_KAMV, KAMKIR, ALLR))]
S["1-1602"] = [QA("P93b", LC(it("P94a"), it("P95a"), it("P96b")))]
S["1-1603"] = [QA("P94a", JH("r", "four", "five") + " " + KVK)]
S["1-1604"] = [QA("P94b", LC(it("P93a"), it("P95a"), it("P96b")))]
S["1-1605"] = [QA("P95a", ARU4 + " " + KVK)]
S["1-1606"] = [QA("P95b", LC(it("P93a"), it("P94a"), it("P96b")))]
S["1-1607"] = [QA("P96a", A3R)]
S["1-1608"] = [QA("P96b", MPN)]
S["1-1609"] = [QA("P97a", M4)]
S["1-1610"] = [QA("P97b", LA(K3, AK, V4, F3, R, NB))]
S["1-1611"] = [Q("P98a") + " " + cap(LC(DIT4, DOM2)) + " " + DASH + " "
               + SIYA(f"sometimes {it('P98a')}", f"sometimes {it('P98b')}") + ". "
               + cap(M4) + " " + E("P98a")]
S["1-1612"] = [QA("P98b", LA(LOBDV4, VIC, UDD, K3, V4, F3, R, NB))]
S["1-1613"] = [QA("P99a", A3R)]
S["1-1614"] = [QA("P99b", MPN)]
S["1-1615"] = [QA("P100a", AK12)]
S["1-1616"] = [QA("P100b", A4_NOAK), "The explanation is complete.", "The Enumeration of Phenomena is complete."]

# ---- build ----------------------------------------------------------------------------
ID = re.compile(r"\s*\^([0-9A-Za-z-]+)\s*$")


def pali_segments():
    segs, buf = [], []
    for line in PALI.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        m = ID.search(line)
        if m:
            buf.append(line[:m.start()])
            segs.append((m.group(1), buf))
            buf = []
        else:
            buf.append(line)
    assert not buf, "trailing lines without id"
    return segs


def norm_item(p):
    p = re.sub(r"\s*\[[^\]]*\]", "", p).rstrip(".").replace("kho pana ", "")
    return " ".join(w for w in p.split() if w != "dhammā")


def check_questions(segs):
    """Each 'Katame dhammā X?' must be answered with the matrix item whose Pāli is X."""
    rev = {}
    for (bid, letter), (p, e) in ITEMS.items():
        ref = ("T" if bid.startswith("1-M1-") else "P") + bid.split("-")[-1] + letter
        rev.setdefault(it(ref), []).append(norm_item(p))
    bad = []
    for bid, plines in segs:
        pm = re.match(r"Katame dhammā (.+?)(\?|\.|…)", plines[0])
        if not pm:
            continue
        em = re.match(r"What are (.+?)(\?|\.$|\. |…)", S[bid][0])
        pq = pm.group(1)
        cands = rev.get(em.group(1), [])
        if pq not in cands:
            bad.append((bid, pq, em.group(1), cands))
    return bad


def build():
    out = []
    segs = pali_segments()
    assert len(segs) == len(S) and {b for b, _ in segs} == set(S), (set(S) ^ {b for b, _ in segs})
    for b in check_questions(segs):
        print("QUESTION/ITEM CHECK:", b)
    for bid, plines in segs:
        elines = S[bid]
        assert len(elines) == len(plines), (bid, len(plines), len(elines))
        for p, e in zip(plines, elines):
            assert p.count("–") + p.count("—") == e.count("–") + e.count("—"), (bid, p, e)
            assert p.count("?") == e.count("?"), (bid, p, e)
            assert ("[" in p) == ("[" in e), (bid, p, e)
            assert "—" not in e and ":-" not in e and "  " not in e, (bid, e)
        elines = [cap(elines[0])] + elines[1:]
        elines = elines[:-1] + [elines[-1] + f" ^{bid}"]
        out.append("\n".join(elines))
    return "\n\n".join(out) + "\n"


if __name__ == "__main__":
    TEXT = build()
    OUT.write_text(TEXT, encoding="utf-8", newline="\n")
    print("wrote", OUT, "segments", len(S))
