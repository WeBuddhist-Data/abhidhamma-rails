"""Build the Hindi plain zero-shot of pi-1 chapter 5 (5-atthakathakandam.md).

usage: python -I -X utf8 build_5_hi.py
Structure mirrors pi-1-en/build_5_atthakathakandam.py. Every matrix item named in a question,
answer or "na vattabbā" clause comes from build_matika_hi (BARE, QUESTION, ANSWER), so it is
word for word the matrix wording. All mind-class phrases are fixed constants below (see
notes-5.md), so every repeat is byte-identical.
"""
import pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import build_matika_hi as M  # noqa: E402  (importing does not write anything)

ROOT = HERE.parents[3]
PALI = ROOT / "AI_translation" / "pali" / "pi-1_split_chapters" / "5-atthakathakandam.md"
OUT = ROOT / "AI_translation" / "hindi" / "pi-1-hindi-plain-zeroshot_split_chapters" / "5-atthakathakandam.md"

DASH = "–"
DANDA = "।"
PH = "परिघटनाएँ"
LET = {"a": "क", "b": "ख", "c": "ग"}


# ---- matrix items -------------------------------------------------------------------------
def key(ref):
    """'T1a' -> ('1-M1-1', 'क'); 'P83b' -> ('1-M2-83', 'ख')."""
    m = re.fullmatch(r"([TP])(\d+)([abc])", ref)
    return ("1-M1-" if m.group(1) == "T" else "1-M2-") + m.group(2), LET[m.group(3)]


def N(ref):
    """bare matrix item name, e.g. 'हितकर परिघटनाएँ'"""
    return M.BARE[key(ref)]


def OBL(name):
    assert name.endswith(PH), name
    return name[:-len(PH)] + "परिघटनाओं"


def SG(name):
    assert name.endswith(PH), name
    return name[:-len(PH)] + "परिघटना"


def Q(ref):
    return M.QUESTION(N(ref))


def E(ref):
    return DASH + " " + M.ANSWER(N(ref))


def QA(ref, answer, tail=""):
    s = f"{Q(ref)} {answer} {E(ref)}"
    return s + (" " + tail if tail else "")


def NV(refs, sg=False):
    """na vattabbā Xtipi, Ytipi … (after 'इन्हें' / '<subject> को')"""
    xs = [SG(N(r)) if sg else N(r) for r in refs]
    if len(xs) == 1:
        return f"{xs[0]} नहीं कहा जा सकता"
    return f"न {xs[0]} कहा जा सकता है" + "".join(f", न {x}" for x in xs[1:])


def NVD(subject_obl, refs, sg=False):
    """'<subject> dhammā na vattabbā – Xtipi, Ytipi.'"""
    xs = [SG(N(r)) if sg else N(r) for r in refs]
    return f"{subject_obl} को कहा नहीं जा सकता {DASH} " + ", ".join("न " + x for x in xs) + DANDA


def SY(*refs):
    """ime dhammā siyā X, siyā Y … (without final punctuation)"""
    return "ये " + ", ".join(f"कभी {N(r)} हैं" for r in refs)


def LA(*xs):
    """list whose last member carries Pāli 'ca': a, b और c"""
    return ", ".join(xs[:-1]) + " और " + xs[-1] if len(xs) > 1 else xs[0]


def LC(*xs):
    """plain comma list"""
    return ", ".join(xs)


# ---- mind classes (see notes-5.md) ----------------------------------------------------------
K4 = "चारों लोकों से संबंधित हितकर मन"                       # catūsu bhūmīsu kusalaṃ
K3 = "तीनों लोकों से संबंधित हितकर मन"                       # tīsu bhūmīsu kusalaṃ
AK = "हानिकर मन"                                             # akusalaṃ
V4 = "चारों लोकों से संबंधित कर्म-फल रूपी मन"                 # catūsu bhūmīsu vipāko
V3 = "तीनों लोकों से संबंधित कर्म-फल रूपी मन"                 # tīsu bhūmīsu vipāko
F3 = "तीनों लोकों से संबंधित केवल क्रिया रूपी नैतिक रूप से अनिर्धारित मन"  # tīsu bhūmīsu kiriyābyākataṃ
R = "भौतिक रूप"                                              # rūpaṃ
ALLR = "सारा भौतिक रूप"                                      # sabbañca rūpaṃ
NB = "निर्वाण"
KAMK = "इंद्रिय-सुखों के लोक से संबंधित हितकर मन"               # kāmāvacarakusalaṃ
ALL_KAMV = "इंद्रिय-सुखों के लोक से संबंधित सारा कर्म-फल रूपी मन"  # sabbo kāmāvacarassa vipāko
KAMKIR = "इंद्रिय-सुखों के लोक से संबंधित केवल क्रिया रूपी नैतिक रूप से अनिर्धारित मन"  # kāmāvacarakiriyābyākataṃ
ALL_AK = "सारा हानिकर मन"                                     # sabbaṃ akusalaṃ
REST_AK = "शेष हानिकर मन"                                     # avasesaṃ akusalaṃ
AK12 = "हानिकर मन की बारह उत्पत्तियाँ"                         # dvādasa akusalacittuppādā

KAMK_F = "इंद्रिय-सुखों के लोक से संबंधित हितकर मन में से"        # kāmāvacarakusalato
AK_F = "हानिकर मन में से"                                      # akusalato
KAMKV_F = "इंद्रिय-सुखों के लोक से संबंधित हितकर मन के कर्म-फल में से"  # kāmāvacarakusalassa vipākato
AKV_F = "हानिकर मन के कर्म-फल में से"                          # akusalassa vipākato
KIR_F = "केवल क्रिया रूपी मन में से"                            # kiriyato
KAMV_F = "इंद्रिय-सुखों के लोक से संबंधित कर्म-फल रूपी मन में से"  # kāmāvacarassa vipākato
KAMKIR_F = "इंद्रिय-सुखों के लोक से संबंधित केवल क्रिया रूपी मन में से"  # kāmāvacarakiriyato

AHC_X = "मूल से रहित मन की उत्पत्तियों को छोड़कर"               # ahetuke cittuppāde ṭhapetvā
V4X = f"{KAMV_F} {AHC_X} {V4}"
F3X = f"{KAMKIR_F} {AHC_X} {F3}"

SOM = "प्रसन्नता के साथ होने वाली"                              # somanassasahagata-
UPE = "समभाव के साथ होने वाली"                                  # upekkhāsahagata-
NS = "ज्ञान से जुड़ी"                                           # ñāṇasampayutta-
NV_ = "ज्ञान से अलग"                                            # ñāṇavippayutta-


def CU(qual, num="", obl=False):
    """<qual> cittuppādā / -esu: 'प्रसन्नता के साथ होने वाली मन की चार उत्पत्तियाँ'"""
    return f"{qual} मन की " + (num + " " if num else "") + ("उत्पत्तियों" if obl else "उत्पत्तियाँ")


SOM4_K = f"{KAMK_F} {CU(SOM, 'चार')}"
UPE4_K = f"{KAMK_F} {CU(UPE, 'चार')}"
NS4_K = f"{KAMK_F} {CU(NS, 'चार')}"
NS4_KIR = f"{KIR_F} {CU(NS, 'चार')}"
NV4_K = f"{KAMK_F} {CU(NV_, 'चार')}"
NV4_KIR = f"{KIR_F} {CU(NV_, 'चार')}"

DG = "ग़लत दृष्टि से जुड़ी"                                       # diṭṭhigatasampayutta-
LDV = "लोभ के साथ होने वाली और ग़लत दृष्टि से अलग"                # diṭṭhigatavippayuttalobhasahagata-
LDS = "लोभ के साथ होने वाली और ग़लत दृष्टि से जुड़ी"               # diṭṭhigatasampayuttalobhasahagata-
DIT4 = CU(DG, "चार")
DIT4_L = CU(DG, "चार", True) + " में"
LOBDV4 = CU(LDV, "चार")
LOBDV4_L = CU(LDV, "चार", True) + " में"
LOBDS4 = CU(LDS, "चार")
LOB8 = CU("लोभ के साथ होने वाली", "आठ")
LOB8_L = CU("लोभ के साथ होने वाली", "आठ", True) + " में"
DOM2 = CU("उदासी के साथ होने वाली", "दो")
DOM2_L = CU("उदासी के साथ होने वाली", "दो", True) + " में"
VIC = "संशय के साथ होने वाली मन की उत्पत्ति"                    # vicikicchāsahagato cittuppādo
UDD = "बेचैनी के साथ होने वाली मन की उत्पत्ति"                   # uddhaccasahagato cittuppādo
VICS_L = CU("संशय के साथ होने वाली", obl=True) + " में"         # vicikicchāsahagatesu cittuppādesu
UDDS_L = CU("बेचैनी के साथ होने वाली", obl=True) + " में"        # uddhaccasahagatesu cittuppādesu
SASANKH_L = "प्रेरणा सहित होने वाले हानिकर मनों में"              # sasaṅkhārikesu akusalesu
ALL_AKS_L = "सभी हानिकर मनों में"                                # sabbākusalesu
VICMOHA = "संशय के साथ होने वाला मोह"                           # vicikicchāsahagato moho
UDDMOHA = "बेचैनी के साथ होने वाला मोह"                          # uddhaccasahagato moho
VUMOHA_X = "संशय के साथ होने वाले और बेचैनी के साथ होने वाले मोह को छोड़कर"  # vicikicchāsahagataṃ uddhaccasahagataṃ mohaṃ ṭhapetvā
UDDMOHA_X = "बेचैनी के साथ होने वाले मोह को छोड़कर"               # uddhaccasahagataṃ mohaṃ ṭhapetvā
DOMMOHA = f"{DOM2_L} उत्पन्न मोह"                                # dvīsu domanassasahagatesu cittuppādesu uppanno moho

PV = "दोनों प्रकार की पाँच-पाँच इंद्रिय-चेतनाएँ"                  # dvepañcaviññāṇāni
MD3 = "मन के तीन तत्व"                                           # tisso (ca) manodhātuyo
AHM5 = "मूल से रहित मन की चेतना के पाँच तत्व"                     # pañca (ca) ahetukamanoviññāṇadhātuyo
KIRMD = "केवल क्रिया रूपी मन का तत्व"                             # kiriyāmanodhātu
KIRAH = "मूल से रहित केवल क्रिया रूपी मन की चेतना का वह तत्व जो"     # kiriyāhetukamanoviññāṇadhātu …sahagatā
KIRAH_SOM = KIRAH + " प्रसन्नता के साथ होता है"
KIRAH_UPE = KIRAH + " समभाव के साथ होता है"
AKV_MVD = f"{AKV_F} मन की चेतना का वह तत्व जो समभाव के साथ होता है"  # akusalassa vipākato manoviññāṇadhātu upekkhāsahagatā
DUKKHA_KV = "दुःख के साथ होने वाली शरीर की चेतना"                 # dukkhasahagataṃ kāyaviññāṇaṃ

M4 = "अस्तित्व के लोकों में न समाए हुए चार मार्ग"                  # cattāro maggā apariyāpannā
P4 = "श्रमण-जीवन के चार फल"                                      # cattāri (ca) sāmaññaphalāni
MPN = LA(M4, P4, NB)
MP = LA(M4, P4)

KAMMA = "जो भी भौतिक रूप कर्म किए जाने के कारण है"                 # yañca rūpaṃ kammassa katattā
NKAMMA = "जो भी भौतिक रूप कर्म किए जाने के कारण नहीं है"           # yañca rūpaṃ na kammassa katattā
RDH = ("जो भी भौतिक रूप दिखाई न देने वाला, टकराव से रहित और मन के विषयों के "
       "इंद्रिय-क्षेत्र में समाया हुआ है")                            # yañca rūpaṃ anidassanaṃ appaṭighaṃ dhammāyatanapariyāpannaṃ

KVK = "(हितकर, कर्म-फल रूपी और केवल क्रिया रूपी)"                # kusalato ca vipākato ca kiriyato ca
KV = "(हितकर और कर्म-फल रूपी)"                                    # kusalato ca vipākato ca
KK = "(हितकर और केवल क्रिया रूपी)"                                # kusalato ca kiriyato ca

RV = "सूक्ष्म भौतिक लोक से संबंधित"                               # rūpāvacara-
R1J = f"{RV} पहला ध्यान"
R4J = f"{RV} चौथा ध्यान"
L1J = "लोकोत्तर पहला ध्यान"
L4J = "लोकोत्तर चौथा ध्यान"
R2J5 = f"पाँच-पाँच की विधि में {RV} दूसरा ध्यान"                  # rūpāvacarapañcakanaye dutiyaṃ jhānaṃ
L2J5 = "पाँच-पाँच की विधि में लोकोत्तर दूसरा ध्यान"               # lokuttarapañcakanaye dutiyaṃ jhānaṃ
J4V = "चौथे ध्यान का कर्म-फल"                                    # catutthassa jhānassa vipāko
ARU4 = "चार अभौतिक अवस्थाएँ"                                     # cattāro āruppā
ARV4 = "अभौतिक लोक से संबंधित चार मन"                            # cattāro arūpāvacarā
AKAS = "अनंत आकाश का क्षेत्र"                                    # ākāsānañcāyatanaṃ
VINN = "अनंत चेतना का क्षेत्र"                                   # viññāṇañcāyatanaṃ
AKIN = "कुछ भी न होने का क्षेत्र"                                 # ākiñcaññāyatanaṃ
NEVA = "न पहचान न अ-पहचान का क्षेत्र"                             # nevasaññānāsaññāyatanaṃ


def JH(kind, a, b):
    """rūpāvacara/lokuttara + <a><b>jjhānā (tikacatukka = तीन, चार …)"""
    realm = RV if kind == "r" else "लोकोत्तर"
    return f"{realm} वे ध्यान जो चार-चार की विधि में {a} और पाँच-पाँच की विधि में {b} हैं"


def ETTH(x):
    """etthuppannaṃ X ṭhapetvā"""
    return f"इनमें उत्पन्न {x} को छोड़कर"


EYE_TOUCH = "आँख का इंद्रिय-क्षेत्र… स्पर्श का इंद्रिय-क्षेत्र"   # cakkhāyatanaṃ…pe… phoṭṭhabbāyatanaṃ
VIS = "दृश्य रूप का इंद्रिय-क्षेत्र"                                # rūpāyatanaṃ
NOOBJ = f"{R} और {NB} {N('P55b')} हैं{DANDA}"                    # Rūpañca nibbānañca anārammaṇā.

# ---- recurring answer lists ------------------------------------------------------------------
A4 = LA(K4, AK, V4, F3, R, NB)
A4_NOAK = LA(K4, V4, F3, R, NB)
A3R = LA(K3, AK, V3, F3, ALLR)
A3R_NOAK = LA(K3, V3, F3, ALLR)
A4R = LA(K4, AK, V4, F3, ALLR)
A4_INV = LC(K4, AK, V4, F3, RDH) + ", और " + NB
SAHETU = LC(K4, AK, V4X, F3X)
SAHETU_A = LC(f"{VUMOHA_X} {REST_AK}", K4, V4X, F3X)
AHETU = LA(VICMOHA, UDDMOHA, PV, MD3, AHM5, R, NB)

L_SUKHA_V = LC(SOM4_K, f"{AK_F} चार", f"{KAMKV_F} और {KIR_F} पाँच",
               JH("r", "तीन", "चार") + " " + KVK, JH("l", "तीन", "चार") + " " + KV)
L_UPE = LC(UPE4_K, f"{AK_F} छह", f"{KAMKV_F} दस", f"{AKV_F} छह", f"{KIR_F} छह", R4J + " " + KVK)
L_PITI = LC(SOM4_K, f"{AK_F} चार", f"{KAMKV_F} पाँच", f"{KIR_F} पाँच",
            JH("r", "दो", "तीन") + " " + KVK, JH("l", "दो", "तीन") + " " + KV)
L_SUKHA = LC(SOM4_K, f"{AK_F} चार", f"{KAMKV_F} छह", f"{KIR_F} पाँच",
             JH("r", "तीन", "चार") + " " + KVK, JH("l", "तीन", "चार") + " " + KV)
L_UPEKKHA = LC(L_UPE, ARU4 + " " + KVK, L4J + " " + KV)
L_APITI = LC(UPE4_K, f"{AK_F} आठ", f"{KAMKV_F} ग्यारह", f"{AKV_F} सात", f"{KIR_F} छह",
             JH("r", "दो", "दो") + " " + KVK, ARU4 + " " + KVK, JH("l", "दो", "दो") + " " + KV)
L_SAVITAKKA = LC(KAMK, AK, f"{KAMKV_F} मन की ग्यारह उत्पत्तियाँ", f"{AKV_F} दो", f"{KIR_F} ग्यारह",
                 R1J + " " + KVK, L1J + " " + KV)

# ---- segments --------------------------------------------------------------------------------
S = {}

S["1-4-0"] = ["### अर्थ-व्याख्या का अध्याय"]
S["1-4-1-0"] = ["#### तीन-तीन के वर्गीकरणों का अर्थ-निर्धारण"]

S["1-1384"] = [QA("T1a", K4)]
S["1-1385"] = [QA("T1b", AK12)]
S["1-1386"] = [QA("T1c", LA(V4, F3, R, NB))]
S["1-1387"] = [QA("T2a", L_SUKHA_V + ", " + ETTH("सुखद अनुभूति"))]
S["1-1388"] = [QA("T2b", LC(DOM2, DUKKHA_KV) + ", " + ETTH("दुःखद अनुभूति"))]
S["1-1389"] = [QA("T2c", LC(L_UPE, ARV4 + " " + KVK, L4J + " " + KV) + ", " + ETTH("न दुःखद, न सुखद अनुभूति"),
                  # T2c itself begins with "न …", so the "न X, न Y" frame would give "न न"; listed instead
                  LA("तीनों अनुभूतियाँ", R, NB) + f" {DASH} इन्हें {N('T2a')}, {N('T2b')}"
                  + f" या {N('T2c')}, इनमें से कुछ भी नहीं कहा जा सकता" + DANDA)]
S["1-1390"] = [QA("T3a", V4)]
S["1-1391"] = [QA("T3b", LC(K4, AK))]
S["1-1392"] = [QA("T3c", LA(F3, R, NB))]
S["1-1393"] = [QA("T4a", LA(V3, KAMMA))]
S["1-1394"] = [QA("T4b", LA(K3, AK, F3, NKAMMA))]
S["1-1395"] = [QA("T4c", MPN)]
S["1-1396"] = [QA("T5a", AK12)]
S["1-1397"] = [QA("T5b", A3R_NOAK)]
S["1-1398"] = [QA("T5c", MPN)]
S["1-1399"] = [QA("T6a", L_SAVITAKKA + ", " + ETTH("आरंभिक विचार और सतत विचार"))]
S["1-1400"] = [QA("T6b", LC(R2J5 + " " + KVK, L2J5 + " " + KV) + ", " + ETTH("सतत विचार")
                  + ", और आरंभिक विचार")]
S["1-1401"] = [QA("T6c", LC(PV, JH("r", "तीन", "तीन") + " " + KVK, ARU4 + " " + KVK,
                            JH("l", "तीन", "तीन") + " " + KV)
                  + ", पाँच-पाँच की विधि के दूसरे ध्यान [वर्तनी-भेद (Sī.): dutiyajjhāne] में उत्पन्न सतत विचार, "
                  + LA(R, NB),
                  "आरंभिक विचार के साथ उत्पन्न सतत विचार को " + NV(["T6a", "T6b", "T6c"], sg=True) + DANDA)]
S["1-1402"] = [QA("T7a", L_PITI + ", " + ETTH("उल्लास"))]
S["1-1403"] = [QA("T7b", L_SUKHA + ", " + ETTH("सुख"))]
S["1-1404"] = [QA("T7c", L_UPEKKHA + ", " + ETTH("समभाव"),
                  f"उल्लास स्वयं {SG(N('T7a'))} नहीं है, {SG(N('T7b'))} है, {SG(N('T7c'))} नहीं है{DANDA} "
                  f"सुख स्वयं {SG(N('T7b'))} नहीं है, कभी {SG(N('T7a'))} है, {SG(N('T7c'))} नहीं है, "
                  f"और कभी इसे {SG(N('T7a'))} नहीं कहा जा सकता{DANDA} "
                  + LA(DOM2, DUKKHA_KV, "समभाव रूपी अनुभूति", R, NB)
                  + f" {DASH} इन्हें " + NV(["T7a", "T7b", "T7c"]) + DANDA)]
S["1-1405"] = [QA("T8a", LC(DIT4, VIC))]
S["1-1406"] = [QA("T8b", UDD, LC(LOBDV4, DOM2) + f" {DASH} " + SY("T8a", "T8b") + DANDA)]
S["1-1407"] = [QA("T8c", A4_NOAK)]
S["1-1408"] = [QA("T9a", LC(DIT4, VIC) + ", " + ETTH("मोह"))]
S["1-1409"] = [QA("T9b", UDD + ", " + ETTH("मोह"), LC(LOBDV4, DOM2) + f" {DASH} " + SY("T9a", "T9b") + DANDA)]
S["1-1410"] = [QA("T9c", LA(VICMOHA, UDDMOHA, K4, V4, F3, R, NB))]
S["1-1411"] = [QA("T10a", LC(K3, AK))]
S["1-1412"] = [QA("T10b", M4)]
S["1-1413"] = [QA("T10c", LA(V4, F3, R, NB))]
S["1-1414"] = [QA("T11a", LA(M4, "श्रमण-जीवन के निचले तीन फल"))]
S["1-1415"] = [QA("T11b", "सबसे ऊँचा फल, अर्हत्-पद का फल")]
S["1-1416"] = [QA("T11c", LA(K3, AK, V3, F3, R, NB))]
S["1-1417"] = [QA("T12a", LA(KAMK, AK, ALL_KAMV, KAMKIR, ALLR))]
S["1-1418"] = [QA("T12b", "सूक्ष्म भौतिक लोक से संबंधित और अभौतिक लोक से संबंधित हितकर तथा नैतिक रूप से अनिर्धारित "
                          + PH)]
S["1-1419"] = [QA("T12c", MPN)]
S["1-1420"] = [QA("T13a", LC(ALL_KAMV, KIRMD, KIRAH_SOM))]
S["1-1421"] = [QA("T13b", LC(VINN, NEVA))]
S["1-1422"] = [QA("T13c", MP,
                  LC(NV4_K, NV4_KIR, ALL_AK) + f" {DASH} "
                  + f"ये कभी {N('T13a')} हैं, कभी {N('T13b')} हैं, {N('T13c')} नहीं हैं, "
                  + "और कभी इन्हें " + NV(["T13a", "T13b"]) + DANDA + " "
                  + LC(NS4_K, NS4_KIR, R4J + " " + KK, KIRAH_UPE) + f" {DASH} "
                  + SY("T13a", "T13b", "T13c") + ", और कभी इन्हें " + NV(["T13a", "T13b", "T13c"]) + DANDA + " "
                  + LC(JH("r", "तीन", "चार") + " " + KVK, J4V, AKAS, AKIN) + f" {DASH} इन्हें "
                  + NV(["T13a", "T13b", "T13c"]) + DANDA + " " + NOOBJ)]
S["1-1423"] = [QA("T14a", AK12)]
S["1-1424"] = [QA("T14b", A3R_NOAK)]
S["1-1425"] = [QA("T14c", MPN)]
S["1-1426"] = [Q("T15a") + " " + LC(DIT4, DOM2) + f" {DASH} " + SY("T15a", "T15c") + DANDA]
S["1-1427"] = [QA("T15b", M4)]
S["1-1428"] = [QA("T15c", LA(LOBDV4, VIC, UDD, K3, V4, F3, R, NB))]
S["1-1429"] = [Q("T16a") + " " + LC(NS4_K, NS4_KIR) + f" {DASH} "
               + f"ये कभी {N('T16a')} हैं, {N('T16b')} नहीं हैं; कभी {N('T16c')} हैं, "
               + "और कभी इन्हें " + NV(["T16a", "T16c"]) + DANDA + " "
               + f"चार आर्य मार्ग {N('T16a')} नहीं हैं, {N('T16b')} हैं; कभी {N('T16c')} हैं, "
               + "और कभी इन्हें " + NV(["T16c"]) + DANDA + " "
               + LC(R4J + " " + KK, KIRAH_UPE) + f" {DASH} "
               + f"ये कभी {N('T16a')} हैं; {N('T16b')} नहीं हैं, {N('T16c')} नहीं हैं; "
               + "और कभी इन्हें " + NV(["T16a"]) + DANDA + " "
               + LC(NV4_K, ALL_AK, ALL_KAMV, f"{KIR_F} मन की छह उत्पत्तियाँ",
                    JH("r", "तीन", "चार") + " " + KVK, J4V, ARU4 + " " + KVK) + ", और " + P4
               + f" {DASH} इन्हें " + NV(["T16a", "T16b", "T16c"]) + DANDA + " " + NOOBJ]
S["1-1430"] = [Q("T17a") + " " + LA(V4, KAMMA) + f" {DASH} " + SY("T17a", "T17c")
               + "; इन्हें " + NV(["T17b"]) + DANDA + " "
               + LA(K4, AK, F3, NKAMMA) + f" {DASH} " + SY("T17a", "T17b")
               + "; इन्हें " + NV(["T17c"]) + DANDA + " "
               + "निर्वाण को " + NV(["T17a", "T17b", "T17c"], sg=True) + DANDA]
S["1-1431"] = [f"निर्वाण को छोड़कर सभी {PH} कभी {N('T18a')} हैं, कभी {N('T18b')} हैं, कभी {N('T18c')} हैं{DANDA} "
               + "निर्वाण को " + NV(["T18a", "T18b", "T18c"], sg=True) + DANDA]
S["1-1432"] = [QA("T19a", LC(VINN, NEVA))]
S["1-1433"] = [f"कोई भी {PH} ऐसी नहीं हैं जो अनिवार्य रूप से {N('T19b')} हों{DANDA}"]
S["1-1434"] = [QA("T19c", LA(PV, MD3),
                  LC(f"{KAMKV_F} मन की दस उत्पत्तियाँ", AKV_MVD, KIRAH_SOM) + f" {DASH} "
                  + SY("T19a", "T19b", "T19c") + DANDA + " "
                  + LC(KAMK, AK, f"{KIR_F} मन की नौ उत्पत्तियाँ", R4J + " " + KK) + f" {DASH} "
                  + SY("T19a", "T19b", "T19c") + "; और कभी इन्हें " + NV(["T19a", "T19b", "T19c"]) + DANDA + " "
                  + LC(JH("r", "तीन", "चार") + " " + KVK, J4V, AKAS, AKIN, MP) + f" {DASH} इन्हें "
                  + NV(["T19a", "T19b", "T19c"]) + DANDA + " " + NOOBJ)]
ANIND = "इंद्रियों से न बँधा भौतिक रूप"                          # anindriyabaddharūpaṃ
ANIND_OBL = "इंद्रियों से न बँधे भौतिक रूप"
S["1-1435"] = [f"{ANIND_OBL} और {NB} को छोड़कर, सभी {PH} कभी {N('T20a')} हैं, कभी {N('T20b')} हैं, "
               f"कभी {N('T20c')} हैं{DANDA} {ANIND} और {NB} {N('T20b')} हैं{DANDA}"]
S["1-1436"] = [QA("T21a", LC(VINN, NEVA))]
S["1-1437"] = [QA("T21b", LC(JH("r", "तीन", "चार") + " " + KVK, J4V, AKAS, MP),
                  f"{R} को छोड़कर, इंद्रिय-सुखों के लोक से संबंधित सभी हितकर, हानिकर और नैतिक रूप से अनिर्धारित {PH}, "
                  + R4J + " " + KK + f" {DASH} " + SY("T21a", "T21b", "T21c") + DANDA + " "
                  + "कुछ भी न होने के क्षेत्र को " + NV(["T21a", "T21b", "T21c"], sg=True) + DANDA + " " + NOOBJ)]
S["1-1438"] = [QA("T22a", VIS)]
S["1-1439"] = [QA("T22b", EYE_TOUCH)]
S["1-1440"] = [QA("T22c", A4_INV), "तीन-तीन के वर्गीकरण।"]

S["1-4-2-0"] = ["#### दो-दो के वर्गीकरणों का अर्थ-निर्धारण"]
for n in range(1, 14):
    S[f"1-4-2-{n}-0"] = [M.GROUPS[f"1-M-2-{n}-0"][0]]

# -- roots
NV4_X = CU(NV_, "चार", True) + " को छोड़कर"                     # cattāro ñāṇavippayutte cittuppāde ṭhapetvā
S["1-1441"] = [
    Q("P1a") + " तीन हितकर मूल, तीन हानिकर मूल, तीन नैतिक रूप से अनिर्धारित मूल। "
    "लोभ का अभाव (हितकर मूल) और द्वेष का अभाव (हितकर मूल) चारों लोकों से संबंधित हितकर मनों में "
    "उत्पन्न होते हैं। मोह का अभाव (हितकर मूल), " + f"{KAMK_F} {NV4_X}, "
    "चारों लोकों से संबंधित हितकर मनों में उत्पन्न होता है।",
    f"लोभ {LOB8_L} उत्पन्न होता है। द्वेष {DOM2_L} उत्पन्न होता है। मोह {ALL_AKS_L} उत्पन्न होता है।",
    "लोभ का अभाव (कर्म-फल रूपी मूल) और द्वेष का अभाव (कर्म-फल रूपी मूल), " + f"{KAMV_F} {AHC_X}, "
    "चारों लोकों से संबंधित कर्म-फल रूपी मनों में उत्पन्न होते हैं। मोह का अभाव (कर्म-फल रूपी मूल), "
    + f"{KAMV_F} {AHC_X}, {NV4_X}, " + "चारों लोकों से संबंधित कर्म-फल रूपी मनों में उत्पन्न होता है।",
    "लोभ का अभाव (केवल क्रिया रूपी मूल) और द्वेष का अभाव (केवल क्रिया रूपी मूल), " + f"{KAMKIR_F} {AHC_X}, "
    "तीनों लोकों से संबंधित केवल क्रिया रूपी मनों में उत्पन्न होते हैं। मोह का अभाव (केवल क्रिया रूपी मूल), "
    + f"{KAMKIR_F} {AHC_X}, {NV4_X}, " + "तीनों लोकों से संबंधित केवल क्रिया रूपी मनों में उत्पन्न होता है "
    + E("P1a"),
]
S["1-1442"] = [QA("P1b", "मूलों को छोड़कर, " + A4)]
S["1-1443"] = [QA("P2a", SAHETU_A)]
S["1-1444"] = [QA("P2b", AHETU)]
S["1-1445"] = [QA("P3a", SAHETU_A)]
S["1-1446"] = [QA("P3b", AHETU)]
S["1-1447"] = [QA("P4a", "जहाँ दो या तीन मूल एक साथ उत्पन्न होते हैं")]
S["1-1448"] = [QA("P4b", SAHETU + ", " + ETTH("मूलों"), NVD(OBL(N("P2b")), ["P4a", "P4b"]))]
S["1-1449"] = [QA("P5a", "जहाँ दो या तीन मूल एक साथ उत्पन्न होते हैं")]
S["1-1450"] = [QA("P5b", SAHETU + ", " + ETTH("मूलों"), NVD(OBL(N("P3b")), ["P5a", "P5b"]))]
S["1-1451"] = [QA("P6a", SAHETU + ", " + ETTH("मूलों"))]
S["1-1452"] = [QA("P6b", LA(PV, MD3, AHM5, R, NB), NVD(OBL(N("P1a")), ["P6a", "P6b"]))]

# -- short intermediate pairs
S["1-1453"] = [QA("P7a", A4R)]
S["1-1454"] = [QA("P7b", NB)]
S["1-1455"] = [QA("P8a", A4R)]
S["1-1456"] = [QA("P8b", NB)]
S["1-1457"] = [QA("P9a", VIS)]
S["1-1458"] = [QA("P9b", EYE_TOUCH + ", " + A4_INV)]
S["1-1459"] = [QA("P10a", EYE_TOUCH)]
S["1-1460"] = [QA("P10b", A4_INV)]
S["1-1461"] = [QA("P11a", LA("चार महाभूत", "चार महाभूतों से व्युत्पन्न भौतिक रूप"))]
S["1-1462"] = [QA("P11b", LA(K4, AK, V4, F3, NB))]
S["1-1463"] = [QA("P12a", A3R)]
S["1-1464"] = [QA("P12b", MPN, f"सभी [पाठभेद (Syā.): sabbeva] {PH} {N('P13a')} भी हैं और {N('P13b')} भी{DANDA}")]


def EXC(x, rest):
    """Ṭhapetvā X avasesaṃ akusalaṃ, …"""
    return f"{x} को छोड़कर {rest}"


# taints ^1-1465 ... ^1-1476
AS = "मन के मैलों"
S["1-1465"] = [Q("P14a") + f" मन के चार मैल {DASH} इंद्रिय-सुखों का मैल, अस्तित्व का मैल, ग़लत दृष्टि का मैल, "
               f"अज्ञान का मैल। इंद्रिय-सुखों का मैल {LOB8_L} उत्पन्न होता है, अस्तित्व का मैल {LOBDV4_L} "
               f"उत्पन्न होता है, ग़लत दृष्टि का मैल {DIT4_L} उत्पन्न होता है। अज्ञान का मैल {ALL_AKS_L} "
               "उत्पन्न होता है " + E("P14a")]
S["1-1466"] = [QA("P14b", EXC(AS, LA(REST_AK, K4, V4, F3, R, NB)))]
S["1-1467"] = [QA("P15a", A3R)]
S["1-1468"] = [QA("P15b", MPN)]
S["1-1469"] = [QA("P16a", f"{DOM2}, {ETTH('मोह')}; {VUMOHA_X}, {REST_AK}")]
S["1-1470"] = [QA("P16b", LA(DOMMOHA, VICMOHA, UDDMOHA, K4, V4, F3, R, NB))]
S["1-1471"] = [Q("P17a") + f" वे ही मन के मैल {N('P17a')} हैं{DANDA}"]
S["1-1472"] = [QA("P17b", EXC(AS, LA(REST_AK, K3, V3, F3, ALLR)), NVD(OBL(N("P15b")), ["P17a", "P17b"]))]
S["1-1473"] = [QA("P18a", "जहाँ दो या तीन मन के मैल एक साथ उत्पन्न होते हैं")]
S["1-1474"] = [QA("P18b", EXC(AS, REST_AK), NVD(OBL(N("P16b")), ["P18a", "P18b"]))]
S["1-1475"] = [QA("P19a", LA(DOMMOHA, VICMOHA, UDDMOHA, K3, V3, F3, ALLR))]
S["1-1476"] = [QA("P19b", MPN, NVD(OBL(N("P16a")), ["P19a", "P19b"]))]

# fetters ^1-1477 ... ^1-1488
SJ = "बंधनों"
F_LIST = ("इंद्रिय-सुखों के राग का बंधन, चिढ़ का बंधन, अहंकार का बंधन, ग़लत दृष्टि का बंधन, संशय का बंधन, "
          "कर्मकांडों और व्रतों से चिपकाव का बंधन, अस्तित्व के राग का बंधन, ईर्ष्या का बंधन, कंजूसी का बंधन, "
          "अज्ञान का बंधन")
S["1-1477"] = [Q("P20a") + f" दस बंधन {DASH} {F_LIST}। "
               f"इंद्रिय-सुखों के राग का बंधन {LOB8_L} उत्पन्न होता है। चिढ़ का बंधन {DOM2_L} उत्पन्न होता है। "
               f"अहंकार का बंधन {LOBDV4_L} उत्पन्न होता है। ग़लत दृष्टि का बंधन {DIT4_L} उत्पन्न होता है। "
               f"संशय का बंधन {VICS_L} उत्पन्न होता है। कर्मकांडों और व्रतों से चिपकाव का बंधन {DIT4_L} "
               f"उत्पन्न होता है। अस्तित्व के राग का बंधन {LOBDV4_L} उत्पन्न होता है। ईर्ष्या का बंधन और कंजूसी "
               f"का बंधन {DOM2_L} उत्पन्न होते हैं। अज्ञान का बंधन {ALL_AKS_L} उत्पन्न होता है " + E("P20a")]
# the Pāli question of ^1-1478 ends with a full stop (source slip), kept as written
S["1-1478"] = [Q("P20b")[:-1] + DANDA + " " + EXC(SJ, LA(REST_AK, K4, V4, F3, R, NB)) + " " + E("P20b")]
S["1-1479"] = [QA("P21a", A3R)]
S["1-1480"] = [QA("P21b", MPN)]
S["1-1481"] = [QA("P22a", f"{UDDMOHA_X} {REST_AK}")]
S["1-1482"] = [QA("P22b", LA(UDDMOHA, K4, V4, F3, R, NB))]
S["1-1483"] = [Q("P23a") + f" वे ही बंधन {N('P23a')} हैं{DANDA}"]
S["1-1484"] = [QA("P23b", EXC(SJ, LA(REST_AK, K3, V3, F3, ALLR)), NVD(OBL(N("P21b")), ["P23a", "P23b"]))]
S["1-1485"] = [QA("P24a", "जहाँ दो या तीन बंधन एक साथ उत्पन्न होते हैं")]
S["1-1486"] = [QA("P24b", EXC(SJ, REST_AK), NVD(OBL(N("P22b")), ["P24a", "P24b"]))]
S["1-1487"] = [QA("P25a", LA(UDDMOHA, K3, V3, F3, ALLR))]
S["1-1488"] = [QA("P25b", MPN, NVD(OBL(N("P22a")), ["P25a", "P25b"]))]

# ties ^1-1489 ... ^1-1500
GT = "गाँठों"
T_COV = "लालच रूपी काया की गाँठ"
T_ILL = "दुर्भावना रूपी काया की गाँठ"
T_SIL = "कर्मकांडों और व्रतों से चिपकाव रूपी काया की गाँठ"
T_IDAM = "“यही सत्य है” इस आग्रह रूपी काया की गाँठ"
S["1-1489"] = [Q("P26a") + f" चार गाँठें {DASH} " + LC(T_COV, T_ILL, T_SIL, T_IDAM) + "। "
               f"{T_COV} {LOB8_L} उत्पन्न होती है। {T_ILL} {DOM2_L} उत्पन्न होती है। {T_SIL} और {T_IDAM} "
               f"{DIT4_L} उत्पन्न होती हैं " + E("P26a")]
S["1-1490"] = [QA("P26b", EXC(GT, LA(REST_AK, K4, V4, F3, R, NB)))]
S["1-1491"] = [QA("P27a", A3R)]
S["1-1492"] = [QA("P27b", MPN)]
S["1-1493"] = [QA("P28a", LC(DIT4, LOBDV4, ETTH("लोभ"), DOM2, ETTH("चिढ़")))]
GV = [f"{LOBDV4_L} उत्पन्न लोभ", f"{DOM2_L} उत्पन्न चिढ़", VIC, UDD]
S["1-1494"] = [QA("P28b", LA(*GV, K4, V4, F3, R, NB))]
S["1-1495"] = [Q("P29a") + f" वे ही गाँठें {N('P29a')} हैं{DANDA}"]
S["1-1496"] = [QA("P29b", EXC(GT, LA(REST_AK, K3, V3, F3, ALLR)), NVD(OBL(N("P27b")), ["P29a", "P29b"]))]
S["1-1497"] = [QA("P30a", "जहाँ ग़लत दृष्टि और लोभ एक साथ उत्पन्न होते हैं")]
S["1-1498"] = [QA("P30b", LC(LOB8, DOM2) + ", " + ETTH(GT), NVD(OBL(N("P28b")), ["P30a", "P30b"]))]
S["1-1499"] = [QA("P31a", LA(*GV, K3, V3, F3, ALLR))]
S["1-1500"] = [QA("P31b", MPN, NVD(OBL(N("P28a")), ["P31a", "P31b"]))]

# floods, yokes (abridged in the Pāli)
S["1-1501"] = [f"{N('P32a')} कौन-सी हैं…{DANDA}"]
S["1-1502"] = [f"{N('P38a')} कौन-सी हैं…{DANDA}"]

# hindrances ^1-1503 ... ^1-1514
NI = "बाधाओं"
H_LIST = ("इंद्रिय-सुखों की चाह की बाधा, दुर्भावना की बाधा, सुस्ती और तंद्रा की बाधा, बेचैनी और पछतावे की बाधा, "
          "संशय की बाधा, अज्ञान की बाधा")
S["1-1503"] = [Q("P44a") + f" छह बाधाएँ {DASH} {H_LIST}। "
               f"इंद्रिय-सुखों की चाह की बाधा {LOB8_L} उत्पन्न होती है, दुर्भावना की बाधा {DOM2_L} उत्पन्न होती है, "
               f"सुस्ती और तंद्रा की बाधा {SASANKH_L} उत्पन्न होती है, बेचैनी की बाधा {UDDS_L} उत्पन्न होती है, "
               f"पछतावे की बाधा {DOM2_L} उत्पन्न होती है, संशय की बाधा {VICS_L} उत्पन्न होती है, "
               f"अज्ञान की बाधा {ALL_AKS_L} उत्पन्न होती है " + E("P44a")]
S["1-1504"] = [QA("P44b", EXC(NI, LA(REST_AK, K4, V4, F3, R, NB)))]
S["1-1505"] = [QA("P45a", A3R)]
S["1-1506"] = [QA("P45b", MPN)]
S["1-1507"] = [QA("P46a", AK12)]
S["1-1508"] = [QA("P46b", A4_NOAK)]
S["1-1509"] = [Q("P47a") + f" वे ही बाधाएँ {N('P47a')} हैं{DANDA}"]
S["1-1510"] = [QA("P47b", EXC(NI, LA(REST_AK, K3, V3, F3, ALLR)), NVD(OBL(N("P45b")), ["P47a", "P47b"]))]
S["1-1511"] = [QA("P48a", "जहाँ दो या तीन बाधाएँ एक साथ उत्पन्न होती हैं")]
S["1-1512"] = [QA("P48b", EXC(NI, REST_AK), NVD(OBL(N("P46b")), ["P48a", "P48b"]))]
S["1-1513"] = [QA("P49a", A3R_NOAK)]
S["1-1514"] = [QA("P49b", MPN, NVD(OBL(N("P46a")), ["P49a", "P49b"]))]

# misapprehension ^1-1515 ... ^1-1524
PM = "ग़लत धारणा"
S["1-1515"] = [QA("P50a", f"दृष्टि रूपी ग़लत धारणा {DIT4_L} उत्पन्न होती है")]
S["1-1516"] = [QA("P50b", EXC(PM, LA(REST_AK, K4, V4, F3, R, NB)))]
S["1-1517"] = [QA("P51a", A3R)]
S["1-1518"] = [QA("P51b", MPN)]
S["1-1519"] = [QA("P52a", DIT4 + ", " + ETTH(PM))]
PV4 = [LOBDV4, DOM2, VIC, UDD]
S["1-1520"] = [QA("P52b", LA(*PV4, K4, V4, F3, R, NB), NVD(PM, ["P52a", "P52b"], sg=True))]
S["1-1521"] = [Q("P53a") + f" वही ग़लत धारणा {SG(N('P53a'))} है{DANDA}"]
S["1-1522"] = [QA("P53b", EXC(PM, LA(REST_AK, K3, V3, F3, ALLR)), NVD(OBL(N("P51b")), ["P53a", "P53b"]))]
S["1-1523"] = [QA("P54a", LA(*PV4, K3, V3, F3, ALLR))]
S["1-1524"] = [QA("P54b", MPN, NVD(OBL(N("P50a")) + " और " + OBL(N("P52a")), ["P54a", "P54b"]))]

# long intermediate pairs ^1-1525 ... ^1-1552
AGG3 = "अनुभूति का समूह, पहचान का समूह, मानसिक रचनाओं का समूह"
INTIM = "शारीरिक संकेत, वाचिक संकेत"                              # kāyaviññatti, vacīviññatti
S["1-1525"] = [QA("P55a", LC(K4, AK, V4, F3))]
S["1-1526"] = [QA("P55b", LA(R, NB))]
S["1-1527"] = [QA("P56a", "आँख की चेतना, कान की चेतना, नाक की चेतना, जीभ की चेतना, शरीर की चेतना, "
                          "मन का तत्व, मन की चेतना का तत्व")]
S["1-1528"] = [QA("P56b", AGG3 + ", " + LA(R, NB))]
S["1-1529"] = [QA("P57a", AGG3)]
S["1-1530"] = [QA("P57b", LA("मन", R, NB))]
S["1-1531"] = [QA("P58a", AGG3)]
S["1-1532"] = [QA("P58b", LA(R, NB), f"मन को कहा नहीं जा सकता {DASH} न मन से जुड़ा, न मन से अलग{DANDA}")]
S["1-1533"] = [QA("P59a", AGG3)]
S["1-1534"] = [QA("P59b", LA(R, NB), f"मन को कहा नहीं जा सकता {DASH} न मन से घुला-मिला, "
                                       f"न मन से घुला-मिला न होने वाला{DANDA}")]
S["1-1535"] = [QA("P60a", AGG3 + ", " + INTIM + ", या जो भी दूसरा भौतिक रूप है जो मन से जन्मा, मन के कारण "
                  f"और मन से उत्पन्न है {DASH} दृश्य रूप का इंद्रिय-क्षेत्र, ध्वनि का इंद्रिय-क्षेत्र, "
                  "गंध का इंद्रिय-क्षेत्र, स्वाद का इंद्रिय-क्षेत्र, स्पर्श का इंद्रिय-क्षेत्र, आकाश तत्व, जल तत्व, "
                  "भौतिक रूप का हल्कापन, भौतिक रूप की मृदुता, भौतिक रूप की कार्य-योग्यता, भौतिक रूप का संचय, "
                  "भौतिक रूप की धारा, कौर-कौर खाया जाने वाला आहार")]
NOT_CS = LA("मन", "शेष भौतिक रूप", NB)
S["1-1536"] = [QA("P60b", NOT_CS)]
S["1-1537"] = [QA("P61a", AGG3 + ", " + INTIM)]
S["1-1538"] = [QA("P61b", NOT_CS)]
S["1-1539"] = [QA("P62a", AGG3 + ", " + INTIM)]
S["1-1540"] = [QA("P62b", NOT_CS)]
MRN = LA("मन", R, NB)
S["1-1541"] = [QA("P63a", AGG3)]
S["1-1542"] = [QA("P63b", MRN)]
S["1-1543"] = [QA("P64a", AGG3)]
S["1-1544"] = [QA("P64b", MRN)]
S["1-1545"] = [QA("P65a", AGG3)]
S["1-1546"] = [QA("P65b", MRN)]
S["1-1547"] = [QA("P66a", "आँख का इंद्रिय-क्षेत्र… मन का इंद्रिय-क्षेत्र")]
S["1-1548"] = [QA("P66b", "दृश्य रूप का इंद्रिय-क्षेत्र… मन के विषयों का इंद्रिय-क्षेत्र")]
S["1-1549"] = [QA("P67a", "आँख का इंद्रिय-क्षेत्र… कौर-कौर खाया जाने वाला आहार")]
S["1-1550"] = [QA("P67b", LA(K4, AK, V4, F3, "चार महाभूत", NB))]
S["1-1551"] = [QA("P68a", LA(V3, KAMMA))]
S["1-1552"] = [QA("P68b", LA(K3, AK, F3, NKAMMA, M4, P4, NB))]

# clinging ^1-1553 ... ^1-1564
UP = "आसक्तियों"
U_SENS = "इंद्रिय-सुखों की आसक्ति"
U_DIT = "ग़लत दृष्टि की आसक्ति"
U_SIL = "कर्मकांडों और व्रतों की आसक्ति"
U_ATTA = "आत्मा के सिद्धांत की आसक्ति"
S["1-1553"] = [Q("P69a") + f" चार आसक्तियाँ {DASH} " + LC(U_SENS, U_DIT, U_SIL, U_ATTA) + "। "
               f"{U_SENS} {LOB8_L} उत्पन्न होती है। {U_DIT}, {U_SIL} और {U_ATTA} {DIT4_L} उत्पन्न होती हैं "
               + E("P69a")]
S["1-1554"] = [QA("P69b", EXC(UP, LA(REST_AK, K4, V4, F3, R, NB)))]
S["1-1555"] = [QA("P70a", A3R)]
S["1-1556"] = [QA("P70b", MPN)]
S["1-1557"] = [QA("P71a", LC(LOBDS4, LOBDV4) + ", " + ETTH("लोभ"))]
UV = [f"{LOBDV4_L} उत्पन्न लोभ", DOM2, VIC, UDD]
S["1-1558"] = [QA("P71b", LA(*UV, K4, V4, F3, R, NB))]
S["1-1559"] = [Q("P72a") + f" वे ही आसक्तियाँ {N('P72a')} हैं{DANDA}"]
S["1-1560"] = [QA("P72b", EXC(UP, LA(REST_AK, K3, V3, F3, ALLR)), NVD(OBL(N("P70b")), ["P72a", "P72b"]))]
S["1-1561"] = [QA("P73a", "जहाँ ग़लत दृष्टि और लोभ एक साथ उत्पन्न होते हैं")]
S["1-1562"] = [QA("P73b", LOB8 + ", " + ETTH(UP), NVD(OBL(N("P71b")), ["P73a", "P73b"]))]
S["1-1563"] = [QA("P74a", LA(*UV, K3, V3, F3, ALLR))]
S["1-1564"] = [QA("P74b", MPN, NVD(OBL(N("P71a")), ["P74a", "P74b"]))]

# defilements ^1-1565 ... ^1-1580
KL = "मन के क्लेशों"
S["1-1565"] = [Q("P75a") + f" मन के क्लेशों के दस आधार {DASH} लोभ, द्वेष, मोह, अहंकार, ग़लत दृष्टि, संशय, सुस्ती, "
               "बेचैनी, निर्लज्जता, बुराई के प्रति निडरता। "
               f"लोभ {LOB8_L} उत्पन्न होता है। द्वेष {DOM2_L} उत्पन्न होता है। मोह {ALL_AKS_L} उत्पन्न होता है। "
               f"अहंकार {LOBDV4_L} उत्पन्न होता है। ग़लत दृष्टि {DIT4_L} उत्पन्न होती है। संशय {VICS_L} "
               f"उत्पन्न होता है। सुस्ती {SASANKH_L} उत्पन्न होती है। बेचैनी, निर्लज्जता और बुराई के प्रति निडरता "
               f"{ALL_AKS_L} उत्पन्न होती हैं " + E("P75a")]
S["1-1566"] = [QA("P75b", EXC(KL, LA(REST_AK, K4, V4, F3, R, NB)))]
S["1-1567"] = [QA("P76a", A3R)]
S["1-1568"] = [QA("P76b", MPN)]
S["1-1569"] = [QA("P77a", AK12)]
S["1-1570"] = [QA("P77b", A4_NOAK)]
S["1-1571"] = [QA("P78a", AK12)]
S["1-1572"] = [QA("P78b", A4_NOAK)]
S["1-1573"] = [Q("P79a") + f" वे ही मन के क्लेश {N('P79a')} हैं{DANDA}"]
S["1-1574"] = [QA("P79b", EXC(KL, LA(REST_AK, K3, V3, F3, ALLR)), NVD(OBL(N("P76b")), ["P79a", "P79b"]))]
S["1-1575"] = [Q("P80a") + f" वे ही मन के क्लेश {N('P80a')} हैं{DANDA}"]
S["1-1576"] = [QA("P80b", EXC(KL, REST_AK), NVD(OBL(N("P77b")), ["P80a", "P80b"]))]
S["1-1577"] = [QA("P81a", "जहाँ दो या तीन मन के क्लेश एक साथ उत्पन्न होते हैं")]
S["1-1578"] = [QA("P81b", EXC(KL, REST_AK), NVD(OBL(N("P78b")), ["P81a", "P81b"]))]
S["1-1579"] = [QA("P82a", A3R_NOAK)]
S["1-1580"] = [QA("P82b", MPN, NVD(OBL(N("P78a")), ["P82a", "P82b"]))]

# closing pairs ^1-1581 ... ^1-1616
SIYA2 = LC(LOBDV4, DOM2) + f" {DASH} "
S["1-1581"] = [QA("P83a", LC(DIT4, VIC), SIYA2 + SY("P83a", "P83b") + DANDA)]
S["1-1582"] = [QA("P83b", LA(UDD, K4, V4, F3, R, NB))]
S["1-1583"] = [QA("P84a", UDD, SIYA2 + SY("P84a", "P84b") + DANDA)]
S["1-1584"] = [QA("P84b", LA(DIT4, VIC, K4, V4, F3, R, NB))]
S["1-1585"] = [QA("P85a", LC(DIT4, VIC) + ", " + ETTH("मोह"), SIYA2 + SY("P85a", "P85b") + DANDA)]
S["1-1586"] = [QA("P85b", LA(VICMOHA, UDD, K4, V4, F3, R, NB))]
S["1-1587"] = [QA("P86a", UDD + ", " + ETTH("मोह"), SIYA2 + SY("P86a", "P86b") + DANDA)]
S["1-1588"] = [QA("P86b", LA(DIT4, VIC, UDDMOHA, K4, V4, F3, R, NB))]
S["1-1589"] = [QA("P87a", L_SAVITAKKA + ", " + ETTH("आरंभिक विचार"))]
S["1-1590"] = [QA("P87b", LA(PV, JH("r", "तीन", "चार") + " " + KVK, ARV4 + " " + KVK,
                             JH("l", "तीन", "चार") + " " + KV, "आरंभिक विचार", R, NB))]
S["1-1591"] = [QA("P88a", LC(KAMK, AK, f"{KAMKV_F} मन की ग्यारह उत्पत्तियाँ", f"{AKV_F} दो", f"{KIR_F} ग्यारह",
                             JH("r", "एक", "दो") + " " + KVK, JH("l", "एक", "दो") + " " + KV)
                  + ", " + ETTH("सतत विचार"))]
S["1-1592"] = [QA("P88b", LA(PV, JH("r", "तीन", "तीन") + " " + KVK, ARU4 + " " + KVK,
                             JH("l", "तीन", "तीन") + " " + KV, "सतत विचार", R, NB))]
S["1-1593"] = [QA("P89a", L_PITI + ", " + ETTH("उल्लास"))]
S["1-1594"] = [QA("P89b", LA(L_APITI, "उल्लास", R, NB))]
S["1-1595"] = [QA("P90a", L_PITI + ", " + ETTH("उल्लास"))]
S["1-1596"] = [QA("P90b", LA(L_APITI, "उल्लास", R, NB))]
S["1-1597"] = [QA("P91a", L_SUKHA + ", " + ETTH("सुख"))]
S["1-1598"] = [QA("P91b", LA(UPE4_K, f"{AK_F} आठ", f"{KAMKV_F} दस", f"{AKV_F} सात", f"{KIR_F} छह",
                             R4J + " " + KVK, ARU4 + " " + KVK, L4J + " " + KV, "सुख", R, NB))]
S["1-1599"] = [QA("P92a", L_UPEKKHA + ", " + ETTH("समभाव"))]
S["1-1600"] = [QA("P92b", LA(SOM4_K, f"{AK_F} छह", f"{KAMKV_F} छह", f"{AKV_F} एक", f"{KIR_F} पाँच",
                             JH("r", "तीन", "चार") + " " + KVK, JH("l", "तीन", "चार") + " " + KV,
                             "समभाव", R, NB))]
S["1-1601"] = [QA("P93a", LA(KAMK, AK, ALL_KAMV, KAMKIR, ALLR))]
S["1-1602"] = [QA("P93b", LC(N("P94a"), N("P95a"), N("P96b")))]
S["1-1603"] = [QA("P94a", JH("r", "चार", "पाँच") + " " + KVK)]
S["1-1604"] = [QA("P94b", LC(N("P93a"), N("P95a"), N("P96b")))]
S["1-1605"] = [QA("P95a", ARU4 + " " + KVK)]
S["1-1606"] = [QA("P95b", LC(N("P93a"), N("P94a"), N("P96b")))]
S["1-1607"] = [QA("P96a", A3R)]
S["1-1608"] = [QA("P96b", MPN)]
S["1-1609"] = [QA("P97a", M4)]
S["1-1610"] = [QA("P97b", LA(K3, AK, V4, F3, R, NB))]
S["1-1611"] = [Q("P98a") + " " + LC(DIT4, DOM2) + f" {DASH} " + SY("P98a", "P98b") + DANDA + " "
               + M4 + " " + E("P98a")]
S["1-1612"] = [QA("P98b", LA(LOBDV4, VIC, UDD, K3, V4, F3, R, NB))]
S["1-1613"] = [QA("P99a", A3R)]
S["1-1614"] = [QA("P99b", MPN)]
S["1-1615"] = [QA("P100a", AK12)]
S["1-1616"] = [QA("P100b", A4_NOAK), "अर्थ-निर्धारण पूरा हुआ।", "“परिघटनाओं की गणना” ग्रंथ पूरा हुआ।"]

# ---- build ---------------------------------------------------------------------------------
ID = re.compile(r"\s*\^([0-9A-Za-z-]+)\s*$")
LATIN = re.compile(r"[A-Za-zĀāĪīŪūṃṆṇṄṅÑñṬṭḌḍḶḷ]")


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
    """Each 'Katame dhammā X?' must be asked with the matrix item whose Pāli is X."""
    q2pali = {}
    ka = {}
    for bid, letter, pali, hi in M.MATRIX_ITEMS_HI:
        p = norm_item(pali)
        if p.endswith("pi"):          # 'sahetukāpi' / elliptical (Kha) 'ahetukāpi'
            p = p[:-2]
            if letter == "ख" and " " not in p:
                p = " ".join(ka[bid].split()[:-1] + [p])
        if letter == "क":
            ka[bid] = p
        q2pali.setdefault(M.QUESTION(M.bare(hi)), set()).add(p)
    bad = []
    for bid, plines in segs:
        pm = re.match(r"Katame dhammā (.+?)(\?|\.|…)", plines[0])
        if not pm:
            continue
        h = S[bid][0]
        hit = [q for q in q2pali if h.startswith(q[:-1])]
        pq = pm.group(1)
        if not any(pq in q2pali[q] for q in hit):
            bad.append((bid, pq, h[:60]))
    return bad


def build():
    out = []
    segs = pali_segments()
    assert len(segs) == len(S) and {b for b, _ in segs} == set(S), (set(S) ^ {b for b, _ in segs})
    bad = check_questions(segs)
    for b in bad:
        print("QUESTION/ITEM CHECK:", b)
    assert not bad
    for bid, plines in segs:
        hlines = S[bid]
        assert len(hlines) == len(plines), (bid, len(plines), len(hlines))
        for p, h in zip(plines, hlines):
            assert p.count("–") + p.count("—") == h.count("–") + h.count("—"), (bid, p, h)
            assert p.count("?") == h.count("?"), (bid, p, h)
            assert p.count("[") == h.count("["), (bid, p, h)
            assert "—" not in h and ":-" not in h and "  " not in h, (bid, h)
            assert not LATIN.search(re.sub(r"\[[^\]]*\]", "", h)), (bid, h)
            assert p.startswith("#") == h.startswith("#"), (bid, p, h)
        hlines = hlines[:-1] + [hlines[-1] + f" ^{bid}"]
        out.append("\n".join(hlines))
    return "\n\n".join(out) + "\n"


if __name__ == "__main__":
    TEXT = build()
    OUT.write_text(TEXT, encoding="utf-8", newline="\n")
    print("wrote", OUT, "segments", len(S))
