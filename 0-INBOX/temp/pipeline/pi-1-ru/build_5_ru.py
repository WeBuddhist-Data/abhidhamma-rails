"""Build the Russian plain zero-shot of pi-1 chapter 5 (5-atthakathakandam.md, Aṭṭhakathākaṇḍaṃ).

usage: python -I -X utf8 build_5_ru.py
Every matrix item named in a question, answer or "na vattabbā" clause comes from build_matika_ru
(QUESTION / ANSWER / BARE / PRED). All mind-class phrases are fixed constants below, so every repeat
is byte-identical. Structure mirrors ref/en_build_5_atthakathakandam.py; the Russian is from the Pāli.
"""
import pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import build_matika_ru as M  # noqa: E402  (importing does not write anything)

ROOT = HERE.parents[3]
PALI = ROOT / "AI_translation" / "pali" / "pi-1_split_chapters" / "5-atthakathakandam.md"
OUT = ROOT / "AI_translation" / "russian" / "pi-1-russian-plain-zeroshot_split_chapters" / "5-atthakathakandam.md"

DASH = "–"
LETTER = {"a": "а", "b": "б", "c": "в"}


# ---- matrix items -----------------------------------------------------------------------
def key(ref):
    """'T1a' -> ('1-M1-1', 'а'); 'P83b' -> ('1-M2-83', 'б')."""
    m = re.fullmatch(r"([TP])(\d+)([abc])", ref)
    return ("1-M1-" if m.group(1) == "T" else "1-M2-") + m.group(2), LETTER[m.group(3)]


def it(ref):
    return M.BARE[key(ref)]


def pred(ref):
    return M.PRED[key(ref)]


def cap(s):
    return s[0].upper() + s[1:]


# a dependent phrase (participle, relative clause, «за исключением …») closing just before a dash
# or a verb takes a closing comma in Russian
KW = ("котор", "где", "сопровождаем", "связанн", "относящ", "возникш", "являющ", "имеющ", "подверженн",
      "свободн", "затронут", "служащ", "принадлежащ", "способн", "съедаем", "за исключением", "производн")


def needs_comma(s):
    t = s.split("; ")[-1]
    if t.startswith("за исключением"):
        return True
    if ", " not in t:
        return False
    last = t.rsplit(", ", 1)[1]
    if last.startswith("не "):
        last = last[3:]
    return last.startswith(KW)


def DJ(left, right):
    """left – right (the Pāli dash), with the closing comma where Russian needs it."""
    return left + ("," if needs_comma(left) else "") + " " + DASH + " " + right


def Q(ref):
    return M.QUESTION(key(ref))


def QA(ref, answer, tail=""):
    s = Q(ref) + " " + DJ(cap(answer), M.ANSWER(key(ref)))
    return s + (" " + tail if tail else "")


def NV(refs, dash=False):
    """na vattabbā A-tipi, B-tipi … = нельзя определить ни как A, ни как B …"""
    body = ("как " + it(refs[0])) if len(refs) == 1 else ", ".join("ни как " + it(r) for r in refs)
    return "нельзя определить " + (DASH + " " if dash else "") + body


def SNV(subj, refs, dash=False):
    """<subject> na vattabbo/-ā/-aṃ … (subject in the accusative = nominative for these nouns)."""
    return subj + ("," if needs_comma(subj) else "") + " " + NV(refs, dash) + "."


def ENV(refs):
    """ime dhammā na vattabbā … (after the Pāli dash)"""
    return "эти явления " + NV(refs) + "."


def SN(refs):
    """siyā na vattabbā …"""
    return "а иногда их " + NV(refs)


def SIYA(*parts):
    return "это " + ", ".join(parts)


def S_(ref):
    return "иногда " + it(ref)


def _sep(xs):
    return "; " if any(", " in x for x in xs) else ", "


def LC(*xs):
    """plain list (no 'ca' in the Pāli); items with inner commas are separated by semicolons"""
    return _sep(xs).join(xs)


def LA(*xs):
    """list whose last member carries Pāli 'ca': a, b и c"""
    if len(xs) == 1:
        return xs[0]
    if _sep(xs) == ", ":
        return ", ".join(xs[:-1]) + " и " + xs[-1]
    pen = xs[-2]
    join = ", и " if needs_comma(pen) else ("; и " if ", " in pen else " и ")
    return "; ".join(xs[:-1]) + join + xs[-1]


# ---- mind classes (see notes-5.md) -------------------------------------------------------
K4 = "благой ум четырёх миров"                         # catūsu bhūmīsu kusalaṃ
K3 = "благой ум трёх миров"                            # tīsu bhūmīsu kusalaṃ
AK = "неблагой ум"                                     # akusalaṃ
V4 = "результаты действий четырёх миров"               # catūsu bhūmīsu vipāko
V3 = "результаты действий трёх миров"                  # tīsu bhūmīsu vipāko
F3 = "этически неопределённый функциональный ум трёх миров"  # tīsu bhūmīsu kiriyābyākataṃ
R = "материальная форма"                               # rūpaṃ
ALLR = "вся материальная форма"                        # sabbañca rūpaṃ
NB = "нирвана"
KAMK = "благой ум, относящийся к миру чувственных желаний"   # kāmāvacarakusalaṃ / kāmāvacaraṃ kusalaṃ
ALL_KAMV = "все результаты действий, относящиеся к миру чувственных желаний"  # sabbo kāmāvacarassa vipāko
KAMKIR = "этически неопределённый функциональный ум, относящийся к миру чувственных желаний"
ALL_AK = "весь неблагой ум"                            # sabbaṃ akusalaṃ
REST_AK = "остальной неблагой ум"                      # avasesaṃ akusalaṃ

# cittuppāda (a countable class of mind) = вид ума
AK12 = "двенадцать видов неблагого ума"                # dvādasa akusalacittuppādā

KAMK_F = "из благого ума, относящегося к миру чувственных желаний"     # kāmāvacarakusalato
AK_F = "из неблагого ума"                                              # akusalato
KAMKV_F = "из результатов благого ума, относящегося к миру чувственных желаний"  # kāmāvacarakusalassa vipākato
AKV_F = "из результатов неблагого ума"                                 # akusalassa vipākato
KIR_F = "из функционального ума"                                       # kiriyato
KAMV_F = "из результатов, относящихся к миру чувственных желаний"      # kāmāvacarassa vipākato
KAMKIR_F = "из функционального ума, относящегося к миру чувственных желаний"  # kāmāvacarakiriyato

AHC_G = "видов ума без корней"                         # ahetuke cittuppāde (after ṭhapetvā)
V4X = f"{V4}, за исключением {AHC_G} {KAMV_F}"
F3X = f"{F3}, за исключением {AHC_G} {KAMKIR_F}"
NVIPP4_G = "четырёх видов ума, не связанных со знанием"  # cattāro ñāṇavippayutte cittuppāde (after ṭhapetvā)

SOM = "вида ума, сопровождаемые радостью"              # (cattāro) somanassasahagatacittuppādā
UPE = "вида ума, сопровождаемые невозмутимостью"       # (cattāro) upekkhāsahagatacittuppādā
NSAMP = "вида ума, связанные со знанием"               # (cattāro) ñāṇasampayuttacittuppādā
NVIPP = "вида ума, не связанные со знанием"            # (cattāro) ñāṇavippayuttacittuppādā
CU = "видов ума"                                       # (nava, dasa, ekādasa, cha) cittuppādā

DIT4 = "четыре вида ума, связанные с ложным воззрением"                    # cattāro diṭṭhigatasampayuttacittuppādā
LOBDV4 = "четыре вида ума, сопровождаемые жадностью и не связанные с ложным воззрением"
LOBDS4 = "четыре вида ума, сопровождаемые жадностью и связанные с ложным воззрением"
LOB8 = "восемь видов ума, сопровождаемых жадностью"                        # aṭṭha lobhasahagatacittuppādā
DOM2 = "два вида ума, сопровождаемые унынием"                              # dve domanassasahagatacittuppādā
VIC = "вид ума, сопровождаемый колебанием"                                 # vicikicchāsahagato cittuppādo
UDD = "вид ума, сопровождаемый беспокойством"                              # uddhaccasahagato cittuppādo
VICMOHA = "заблуждение, сопровождаемое колебанием"                         # vicikicchāsahagato moho
UDDMOHA = "заблуждение, сопровождаемое беспокойством"                      # uddhaccasahagato moho
VICMOHA_G = "заблуждения, сопровождаемого колебанием"
UDDMOHA_G = "заблуждения, сопровождаемого беспокойством"
VUMOHA_G = f"{VICMOHA_G}, и {UDDMOHA_G}"     # vicikicchāsahagataṃ uddhaccasahagataṃ mohaṃ (ṭhapetvā)

# locatives (… uppajjati / uppajjanti)
LOB8_L = "в восьми видах ума, сопровождаемых жадностью"                    # aṭṭhasu lobhasahagatesu cittuppādesu
DOM2_L = "в двух видах ума, сопровождаемых унынием"                        # dvīsu domanassasahagatesu cittuppādesu
LOBDV4_L = "в четырёх видах ума, сопровождаемых жадностью и не связанных с ложным воззрением"
DIT4_L = "в четырёх видах ума, связанных с ложным воззрением"              # catūsu diṭṭhigatasampayuttesu cittuppādesu
VICS_L = "в видах ума, сопровождаемых колебанием"                          # vicikicchāsahagatesu cittuppādesu
UDDS_L = "в видах ума, сопровождаемых беспокойством"                       # uddhaccasahagatesu cittuppādesu
SASANKH_L = "в неблагом уме с побуждением"                                 # sasaṅkhārikesu akusalesu
ALL_AK_L = "во всём неблагом уме"                                          # sabbākusalesu
K4_L = "в благом уме четырёх миров"                                        # catūsu bhūmīsu kusalesu
V4_L = "в результатах действий четырёх миров"                              # catūsu bhūmīsu vipākesu
F3_L = "в функциональном уме трёх миров"                                   # tīsu bhūmīsu kiriyesu

DOMMOHA = "заблуждение, возникшее в двух видах ума, сопровождаемых унынием"  # dvīsu domanassasahagatesu … uppanno moho

PV = "дважды пять видов сознания"                      # dvepañcaviññāṇāni
MD3 = "три элемента ума"                               # tisso manodhātuyo
AHM5 = "пять элементов умственного сознания без корней"  # pañca ahetukamanoviññāṇadhātuyo
KIRMD = "функциональный элемент ума"                   # kiriyāmanodhātu
KIRAH_SOM = "функциональный элемент умственного сознания без корней, сопровождаемый радостью"
KIRAH_UPE = "функциональный элемент умственного сознания без корней, сопровождаемый невозмутимостью"
DUKKHA_KV = "осязательное сознание, сопровождаемое болью"  # dukkhasahagataṃ kāyaviññāṇaṃ

M4 = "четыре пути, не принадлежащие к кругам существования"  # cattāro maggā apariyāpannā
P4 = "четыре плода отшельничества"                     # cattāri sāmaññaphalāni
MPN = LA(M4, P4, NB)
MP = LA(M4, P4)

KAMMA = "та материальная форма, которая является следствием совершённых действий"       # yañca rūpaṃ kammassa katattā
NKAMMA = "та материальная форма, которая не является следствием совершённых действий"   # … na kammassa katattā
RDH = ("та материальная форма, которая невидима, не способна к соударению и входит в сферу объектов ума")

KVK = "(в благом виде, в виде результатов действий и в функциональном виде)"  # kusalato ca vipākato ca kiriyato ca
KV = "(в благом виде и в виде результатов действий)"                         # kusalato ca vipākato ca
KK = "(в благом и функциональном виде)"                                       # kusalato ca kiriyato ca

R1J = "первое медитативное погружение мира форм"
R4J = "четвёртое медитативное погружение мира форм"
L1J = "первое надмирское медитативное погружение"
L4J = "четвёртое надмирское медитативное погружение"
R2J5 = "второе медитативное погружение мира форм по пятеричному методу"
L2J5 = "второе надмирское медитативное погружение по пятеричному методу"
J4V = "результат четвёртого медитативного погружения"   # catutthassa jhānassa vipāko
ARU4 = "четыре бесформенных состояния"                 # cattāro āruppā
ARV4 = "четыре вида ума, относящиеся к миру без форм"   # cattāro arūpāvacarā
AKAS = "сфера бесконечного пространства"
VINN = "сфера бесконечного сознания"
AKIN = "сфера отсутствия чего-либо"
AKIN_ACC = "сферу отсутствия чего-либо"
NEVA = "сфера ни восприятия, ни невосприятия"

NUM1 = {1: "одно", 2: "два", 3: "три", 4: "четыре"}
NUM2 = {2: "два", 3: "три", 4: "четыре", 5: "пять"}


def JH(kind, a, b):
    """rūpāvacara/lokuttara + <a><b>jjhānā (e.g. tikacatukka = three by the fourfold, four by the fivefold method)."""
    noun = "медитативное погружение" if a == 1 else "медитативных погружения"
    if kind == "r":
        head = f"{NUM1[a]} {noun} мира форм"
    else:
        head = f"{NUM1[a]} {'надмирское' if a == 1 else 'надмирских'} {noun}"
    return f"{head} по четверичному методу и {NUM2[b]} по пятеричному"


def ETTH(x, g):
    """etthuppannaṃ X ṭhapetvā; x in the genitive, g = gender/number of x."""
    part = {"m": "возникшего", "n": "возникшего", "f": "возникшей", "pl": "возникших"}[g]
    return f"за исключением {part} в них {x}"


def EXC_REST(gen):
    """Ṭhapetvā X avasesaṃ akusalaṃ"""
    return f"за исключением {gen}, {REST_AK}"


EYE_TOUCH = "сфера глаза… сфера осязаемого"       # Cakkhāyatanaṃ…pe… phoṭṭhabbāyatanaṃ
EYE_TOUCH_SP = "сфера глаза … сфера осязаемого"   # Cakkhāyatanaṃ …pe… phoṭṭhabbāyatanaṃ
RUPAYATANA = "сфера видимых форм"
NOOBJ = cap(LA(R, NB)) + " " + pred("P55b") + "."   # Rūpañca nibbānañca anārammaṇā.

# ---- recurring answer lists ----------------------------------------------------------
A4 = LA(K4, AK, V4, F3, R, NB)              # catūsu kusalaṃ, akusalaṃ, catūsu vipāko, tīsu kiriyā, rūpañca, nibbānañca
A4_NOAK = LA(K4, V4, F3, R, NB)
A3R = LA(K3, AK, V3, F3, ALLR)              # tīsu kusalaṃ, akusalaṃ, tīsu vipāko, tīsu kiriyā, sabbañca rūpaṃ
A3R_NOAK = LA(K3, V3, F3, ALLR)
A4R = LA(K4, AK, V4, F3, ALLR)
A4_INV = LA(K4, AK, V4, F3, RDH, NB)
SAHETU = (K4, AK, V4X, F3X)
SAHETU_A = LC(f"за исключением {VUMOHA_G}, {REST_AK}", K4, V4X, F3X)
AHETU = LA(VICMOHA, UDDMOHA, PV, MD3, AHM5, R, NB)


def NUMF(src, n, noun=""):
    """'<from-phrase> <number>[ <noun>]': Pāli '<X>to <n> [cittuppādā]'"""
    return src + ("," if needs_comma(src) else "") + f" {n}" + (f" {noun}" if noun else "")


# feeling / rapture / happiness / equanimity lists (items)
I_SUKHA_V = [NUMF(KAMK_F, "четыре", SOM), NUMF(AK_F, "четыре"),
             f"{KAMKV_F}, и {KIR_F} пять", JH("r", 3, 4) + " " + KVK, JH("l", 3, 4) + " " + KV]
I_UPE = [NUMF(KAMK_F, "четыре", UPE), NUMF(AK_F, "шесть"), NUMF(KAMKV_F, "десять"), NUMF(AKV_F, "шесть"),
         NUMF(KIR_F, "шесть"), R4J + " " + KVK]
I_PITI = [NUMF(KAMK_F, "четыре", SOM), NUMF(AK_F, "четыре"), NUMF(KAMKV_F, "пять"), NUMF(KIR_F, "пять"),
          JH("r", 2, 3) + " " + KVK, JH("l", 2, 3) + " " + KV]
I_SUKHA = [NUMF(KAMK_F, "четыре", SOM), NUMF(AK_F, "четыре"), NUMF(KAMKV_F, "шесть"), NUMF(KIR_F, "пять"),
           JH("r", 3, 4) + " " + KVK, JH("l", 3, 4) + " " + KV]
I_UPEKKHA = I_UPE + [ARU4 + " " + KVK, L4J + " " + KV]
I_APITI = [NUMF(KAMK_F, "четыре", UPE), NUMF(AK_F, "восемь"), NUMF(KAMKV_F, "одиннадцать"), NUMF(AKV_F, "семь"),
           NUMF(KIR_F, "шесть"), JH("r", 2, 2) + " " + KVK, ARU4 + " " + KVK, JH("l", 2, 2) + " " + KV]
I_SAVITAKKA = [KAMK, AK, NUMF(KAMKV_F, "одиннадцать", CU), NUMF(AKV_F, "два"), NUMF(KIR_F, "одиннадцать"),
               R1J + " " + KVK, L1J + " " + KV]

# ---- segments --------------------------------------------------------------------------
S = {}

S["1-4-0"] = ["### Раздел разъяснений"]
S["1-4-1-0"] = ["#### Разъяснение смысла троек"]

S["1-1384"] = [QA("T1a", K4)]
S["1-1385"] = [QA("T1b", AK12)]
S["1-1386"] = [QA("T1c", LA(V4, F3, R, NB))]
S["1-1387"] = [QA("T2a", LC(*I_SUKHA_V, ETTH("приятного чувства", "n")))]
S["1-1388"] = [QA("T2b", LC(DOM2, DUKKHA_KV, ETTH("болезненного чувства", "n")))]
# ^1-1389: the Pāli «ya vedanāya sampayuttātipi» is a truncated adukkhamasukhāya …; written out as T2c
S["1-1389"] = [QA("T2c", LC(*I_UPE, ARV4 + " " + KVK, L4J + " " + KV,
                            ETTH("чувства, которое ни болезненно, ни приятно", "n")),
                  DJ(cap(LA("три чувства", R, NB)), ENV(["T2a", "T2b", "T2c"])))]
S["1-1390"] = [QA("T3a", V4)]
S["1-1391"] = [QA("T3b", LC(K4, AK))]
S["1-1392"] = [QA("T3c", LA(F3, R, NB))]
S["1-1393"] = [QA("T4a", LA(V3, KAMMA))]
S["1-1394"] = [QA("T4b", LA(K3, AK, F3, NKAMMA))]
S["1-1395"] = [QA("T4c", MPN)]
S["1-1396"] = [QA("T5a", AK12)]
S["1-1397"] = [QA("T5b", A3R_NOAK)]
S["1-1398"] = [QA("T5c", MPN)]
S["1-1399"] = [QA("T6a", LC(*I_SAVITAKKA, ETTH("направленной мысли и удержания мысли", "pl")))]
S["1-1400"] = [QA("T6b", LC(R2J5 + " " + KVK, L2J5 + " " + KV, ETTH("удержания мысли", "n"))
                  + "; а также направленная мысль")]
S["1-1401"] = [QA("T6c", LC(PV, JH("r", 3, 3) + " " + KVK, ARU4 + " " + KVK, JH("l", 3, 3) + " " + KV,
                            "удержание мысли, возникшее во втором медитативном погружении"
                            + M.V("s", "Sī.", "dutiyajjhāne") + " по пятеричному методу", LA(R, NB)),
                  SNV("Удержание мысли, возникшее вместе с направленной мыслью", ["T6a", "T6b", "T6c"]))]
S["1-1402"] = [QA("T7a", LC(*I_PITI, ETTH("восторга", "m")))]
S["1-1403"] = [QA("T7b", LC(*I_SUKHA, ETTH("счастья", "n")))]


def sg(p):
    return p.replace("сопровождаются", "сопровождается")


PITI_SUKHA = (f"Восторг не {sg(pred('T7a'))}, {sg(pred('T7b'))}, не {sg(pred('T7c'))}. "
              f"Счастье не {sg(pred('T7b'))}, иногда {sg(pred('T7a'))}, не {sg(pred('T7c'))}, "
              f"а иногда его {NV(['T7a'])}.")
S["1-1404"] = [QA("T7c", LC(*I_UPEKKHA, ETTH("невозмутимости", "f")),
                  PITI_SUKHA + " "
                  + DJ(cap(LA(DOM2, DUKKHA_KV, "то чувство, которое является невозмутимостью", R, NB)),
                       ENV(["T7a", "T7b", "T7c"])))]
SIYA2 = cap(LC(LOBDV4, DOM2))     # cattāro diṭṭhigatavippayuttā(-) lobhasahagatacittuppādā, dve domanassa…
S["1-1405"] = [QA("T8a", LC(DIT4, VIC))]
S["1-1406"] = [QA("T8b", UDD, DJ(SIYA2, SIYA(S_("T8a"), S_("T8b")) + "."))]
S["1-1407"] = [QA("T8c", A4_NOAK)]
S["1-1408"] = [QA("T9a", LC(DIT4, VIC, ETTH("заблуждения", "n")))]
S["1-1409"] = [QA("T9b", LC(UDD, ETTH("заблуждения", "n")), DJ(SIYA2, SIYA(S_("T9a"), S_("T9b")) + "."))]
S["1-1410"] = [QA("T9c", LA(VICMOHA, UDDMOHA, K4, V4, F3, R, NB))]
S["1-1411"] = [QA("T10a", LC(K3, AK))]
S["1-1412"] = [QA("T10b", M4)]
S["1-1413"] = [QA("T10c", LA(V4, F3, R, NB))]
S["1-1414"] = [QA("T11a", LA(M4, "три низших плода отшельничества"))]
S["1-1415"] = [QA("T11b", "высший плод, плод состояния архата")]
S["1-1416"] = [QA("T11c", LA(K3, AK, V3, F3, R, NB))]
S["1-1417"] = [QA("T12a", LA(KAMK, AK, ALL_KAMV, KAMKIR, ALLR))]
# Rūpāvacarā, arūpāvacarā, kusalābyākatā
S["1-1418"] = [QA("T12b", f"{it('P94a')}, и {it('P95a')}, как благие, так и этически неопределённые")]
S["1-1419"] = [QA("T12c", MPN)]
S["1-1420"] = [QA("T13a", LC(ALL_KAMV, KIRMD, KIRAH_SOM))]
S["1-1421"] = [QA("T13b", LC(VINN, NEVA))]
S["1-1422"] = [QA("T13c", MP,
                  DJ(cap(LC(NUMF(KAMK_F, "четыре", NVIPP), NUMF(KIR_F, "четыре", NVIPP), ALL_AK)),
                     SIYA(S_("T13a"), S_("T13b"), "не " + it("T13c"), SN(["T13a", "T13b"])) + ". ")
                  + DJ(cap(LC(NUMF(KAMK_F, "четыре", NSAMP), NUMF(KIR_F, "четыре", NSAMP), R4J + " " + KK,
                              KIRAH_UPE)),
                       SIYA(S_("T13a"), S_("T13b"), S_("T13c"), SN(["T13a", "T13b", "T13c"])) + ". ")
                  + DJ(cap(LC(JH("r", 3, 4) + " " + KVK, J4V, AKAS, AKIN)), ENV(["T13a", "T13b", "T13c"]))
                  + " " + NOOBJ)]
S["1-1423"] = [QA("T14a", AK12)]
S["1-1424"] = [QA("T14b", A3R_NOAK)]
S["1-1425"] = [QA("T14c", MPN)]
S["1-1426"] = [Q("T15a") + " " + DJ(cap(LC(DIT4, DOM2)), SIYA(S_("T15a"), S_("T15c")) + ".")]
S["1-1427"] = [QA("T15b", M4)]
S["1-1428"] = [QA("T15c", LA(LOBDV4, VIC, UDD, K3, V4, F3, R, NB))]
S["1-1429"] = [Q("T16a") + " "
               + DJ(cap(LC(NUMF(KAMK_F, "четыре", NSAMP), NUMF(KIR_F, "четыре", NSAMP))),
                    "это иногда " + it("T16a") + ", не " + it("T16b") + "; иногда " + it("T16c") + ", "
                    + SN(["T16a", "T16c"]) + ". ")
               + "Четыре благородных пути не " + pred("T16a") + ", " + pred("T16b") + "; иногда "
               + pred("T16c") + ", а иногда их " + NV(["T16c"]) + ". "
               + DJ(cap(LC(R4J + " " + KK, KIRAH_UPE)),
                    "это иногда " + it("T16a") + "; не " + it("T16b") + ", не " + it("T16c") + "; "
                    + SN(["T16a"]) + ". ")
               + DJ(cap(LA(NUMF(KAMK_F, "четыре", NVIPP), ALL_AK, ALL_KAMV, NUMF(KIR_F, "шесть", CU),
                           JH("r", 3, 4) + " " + KVK, J4V, ARU4 + " " + KVK, P4)),
                    ENV(["T16a", "T16b", "T16c"]))
               + " " + NOOBJ]
S["1-1430"] = [Q("T17a") + " "
               + DJ(cap(LA(V4, KAMMA)), SIYA(S_("T17a"), S_("T17c")) + "; их " + NV(["T17b"]) + ". ")
               + DJ(cap(LA(K4, AK, F3, NKAMMA)), SIYA(S_("T17a"), S_("T17b")) + "; их " + NV(["T17c"]) + ". ")
               + SNV("Нирвану", ["T17a", "T17b", "T17c"])]
S["1-1431"] = ["За исключением нирваны, все явления иногда " + pred("T18a") + ", иногда " + pred("T18b")
               + ", иногда " + pred("T18c") + ". " + SNV("Нирвану", ["T18a", "T18b", "T18c"])]
S["1-1432"] = [QA("T19a", LC(VINN, NEVA))]
S["1-1433"] = ["Нет явлений, которые непременно " + pred("T19b") + "."]
S["1-1434"] = [QA("T19c", LA(PV, MD3),
                  DJ(cap(LC(NUMF(KAMKV_F, "десять", CU),
                            f"{AKV_F} элемент умственного сознания, сопровождаемый невозмутимостью", KIRAH_SOM)),
                     SIYA(S_("T19a"), S_("T19b"), S_("T19c")) + ". ")
                  + DJ(cap(LC(KAMK, AK, NUMF(KIR_F, "девять", CU), R4J + " " + KK)),
                       SIYA(S_("T19a"), S_("T19b"), S_("T19c")) + "; " + SN(["T19a", "T19b", "T19c"]) + ". ")
                  + DJ(cap(LA(JH("r", 3, 4) + " " + KVK, J4V, AKAS, AKIN, M4, P4)), ENV(["T19a", "T19b", "T19c"]))
                  + " " + NOOBJ)]
ANIND = "материальная форма, не связанная с органами чувств"        # anindriyabaddharūpaṃ
ANIND_G = "материальной формы, не связанной с органами чувств"
S["1-1435"] = [f"За исключением {ANIND_G}, и нирваны, все явления иногда {pred('T20a')}, иногда {pred('T20b')}, "
               f"иногда {pred('T20c')}. {cap(ANIND)}, и нирвана {pred('T20b')}."]
S["1-1436"] = [QA("T21a", LC(VINN, NEVA))]
S["1-1437"] = [QA("T21b", LC(JH("r", 3, 4) + " " + KVK, J4V, AKAS, MP),
                  DJ("За исключением материальной формы, все благие, неблагие и этически неопределённые явления, "
                     "относящиеся к миру чувственных желаний; " + R4J + " " + KK,
                     SIYA(S_("T21a"), S_("T21b"), S_("T21c")) + ". ")
                  + SNV(cap(AKIN_ACC), ["T21a", "T21b", "T21c"]) + " " + NOOBJ)]
S["1-1438"] = [QA("T22a", RUPAYATANA)]
S["1-1439"] = [QA("T22b", EYE_TOUCH)]
S["1-1440"] = [QA("T22c", A4_INV), "Тройки."]

S["1-4-2-0"] = ["#### Разъяснение смысла пар"]
for n in range(1, 14):
    S[f"1-4-2-{n}-0"] = [M.GROUPS[f"1-M-2-{n}-0"][0]]

# -- roots
S["1-1441"] = [
    Q("P1a") + " Три благих корня, три неблагих корня, три этически неопределённых корня. "
    f"Отсутствие жадности как благой корень и отсутствие злобы как благой корень возникают {K4_L}. "
    f"Отсутствие заблуждения как благой корень возникает {K4_L}, за исключением {NVIPP4_G}, {KAMK_F}.",
    f"Жадность возникает {LOB8_L}. Злоба возникает {DOM2_L}. Заблуждение возникает {ALL_AK_L}.",
    "Отсутствие жадности как корень, являющийся результатом действий, и отсутствие злобы как корень, "
    f"являющийся результатом действий, возникают {V4_L}, за исключением {AHC_G} {KAMV_F}. "
    f"Отсутствие заблуждения как корень, являющийся результатом действий, возникает {V4_L}, "
    f"за исключением {AHC_G} {KAMV_F}, и за исключением {NVIPP4_G}.",
    "Отсутствие жадности как функциональный корень и отсутствие злобы как функциональный корень возникают "
    f"{F3_L}, за исключением {AHC_G} {KAMKIR_F}. Отсутствие заблуждения как функциональный корень возникает "
    + DJ(f"{F3_L}, за исключением {AHC_G} {KAMKIR_F}, и за исключением {NVIPP4_G}", M.ANSWER(key("P1a"))),
]
S["1-1442"] = [QA("P1b", "за исключением корней, " + A4)]
S["1-1443"] = [QA("P2a", SAHETU_A)]
S["1-1444"] = [QA("P2b", AHETU)]
S["1-1445"] = [QA("P3a", SAHETU_A)]
S["1-1446"] = [QA("P3b", AHETU)]
S["1-1447"] = [QA("P4a", "там, где два или три корня возникают вместе")]
S["1-1448"] = [QA("P4b", LC(*SAHETU, ETTH("корней", "pl")), SNV(cap(it("P2b")), ["P4a", "P4b"], dash=True))]
S["1-1449"] = [QA("P5a", "там, где два или три корня возникают вместе")]
S["1-1450"] = [QA("P5b", LC(*SAHETU, ETTH("корней", "pl")), SNV(cap(it("P3b")), ["P5a", "P5b"], dash=True))]
S["1-1451"] = [QA("P6a", LC(*SAHETU, ETTH("корней", "pl")))]
S["1-1452"] = [QA("P6b", LA(PV, MD3, AHM5, R, NB), SNV(cap(it("P1a")), ["P6a", "P6b"], dash=True))]

# -- short intermediate pairs
S["1-1453"] = [QA("P7a", A4R)]
S["1-1454"] = [QA("P7b", NB)]
S["1-1455"] = [QA("P8a", A4R)]
S["1-1456"] = [QA("P8b", NB)]
S["1-1457"] = [QA("P9a", RUPAYATANA)]
S["1-1458"] = [QA("P9b", LA(EYE_TOUCH_SP, K4, AK, V4, F3, RDH, NB))]
S["1-1459"] = [QA("P10a", EYE_TOUCH)]
S["1-1460"] = [QA("P10b", A4_INV)]
S["1-1461"] = [QA("P11a", "четыре великих элемента и материальная форма, производная от четырёх великих элементов")]
S["1-1462"] = [QA("P11b", LA(K4, AK, V4, F3, NB))]
S["1-1463"] = [QA("P12a", A3R)]
S["1-1464"] = [QA("P12b", MPN, "Все" + M.V("p", "Syā.", "sabbeva") + " явления " + pred("P13a") + " и "
                  + pred("P13b") + ".")]

# taints ^1-1465 ... ^1-1476
S["1-1465"] = [Q("P14a") + " Четыре влечения " + DASH + " влечение к чувственным удовольствиям, влечение к "
               "существованию, влечение к воззрениям, влечение неведения. Влечение к чувственным удовольствиям "
               f"возникает {LOB8_L}, влечение к существованию возникает {LOBDV4_L}, влечение к воззрениям "
               f"возникает {DIT4_L}. "
               + DJ(f"Влечение неведения возникает {ALL_AK_L}", M.ANSWER(key("P14a")))]
S["1-1466"] = [QA("P14b", LA(EXC_REST("влечений"), K4, V4, F3, R, NB))]
S["1-1467"] = [QA("P15a", A3R)]
S["1-1468"] = [QA("P15b", MPN)]
S["1-1469"] = [QA("P16a", LC(f"{DOM2}, {ETTH('заблуждения', 'n')}", f"за исключением {VUMOHA_G}, {REST_AK}"))]
S["1-1470"] = [QA("P16b", LA(DOMMOHA, VICMOHA, UDDMOHA, K4, V4, F3, R, NB))]
S["1-1471"] = [Q("P17a") + " Эти же влечения " + pred("P17a") + "."]
S["1-1472"] = [QA("P17b", LA(EXC_REST("влечений"), K3, V3, F3, ALLR),
                  SNV(cap(it("P15b")), ["P17a", "P17b"], dash=True))]
S["1-1473"] = [QA("P18a", "там, где два или три влечения возникают вместе")]
S["1-1474"] = [QA("P18b", EXC_REST("влечений"), SNV(cap(it("P16b")), ["P18a", "P18b"], dash=True))]
S["1-1475"] = [QA("P19a", LA(DOMMOHA, VICMOHA, UDDMOHA, K3, V3, F3, ALLR))]
S["1-1476"] = [QA("P19b", MPN, SNV(cap(it("P16a")), ["P19a", "P19b"], dash=True))]

# fetters ^1-1477 ... ^1-1488
F_LIST = ("оковы чувственной страсти, оковы неприязни, оковы самомнения, оковы воззрений, оковы колебания, "
          "оковы приверженности обрядам и обетам, оковы страсти к существованию, оковы зависти, оковы скупости, "
          "оковы неведения")
S["1-1477"] = [Q("P20a") + " Десять оков " + DASH + " " + F_LIST + ". "
               f"Оковы чувственной страсти возникают {LOB8_L}. Оковы неприязни возникают {DOM2_L}. "
               f"Оковы самомнения возникают {LOBDV4_L}. Оковы воззрений возникают {DIT4_L}. "
               f"Оковы колебания возникают {VICS_L}. Оковы приверженности обрядам и обетам возникают {DIT4_L}. "
               f"Оковы страсти к существованию возникают {LOBDV4_L}. Оковы зависти и оковы скупости "
               f"возникают {DOM2_L}. "
               + DJ(f"Оковы неведения возникают {ALL_AK_L}", M.ANSWER(key("P20a")))]
# the Pāli question of ^1-1478 ends with a full stop (source slip), kept as written
S["1-1478"] = [Q("P20b")[:-1] + ". " + DJ(cap(LA(EXC_REST("оков"), K4, V4, F3, R, NB)), M.ANSWER(key("P20b")))]
S["1-1479"] = [QA("P21a", A3R)]
S["1-1480"] = [QA("P21b", MPN)]
S["1-1481"] = [QA("P22a", f"за исключением {UDDMOHA_G}, {REST_AK}")]
S["1-1482"] = [QA("P22b", LA(UDDMOHA, K4, V4, F3, R, NB))]
S["1-1483"] = [Q("P23a") + " Эти же оковы " + pred("P23a") + "."]
S["1-1484"] = [QA("P23b", LA(EXC_REST("оков"), K3, V3, F3, ALLR),
                  SNV(cap(it("P21b")), ["P23a", "P23b"], dash=True))]
S["1-1485"] = [QA("P24a", "там, где два или три вида оков возникают вместе")]
S["1-1486"] = [QA("P24b", EXC_REST("оков"), SNV(cap(it("P22b")), ["P24a", "P24b"], dash=True))]
S["1-1487"] = [QA("P25a", LA(UDDMOHA, K3, V3, F3, ALLR))]
S["1-1488"] = [QA("P25b", MPN, SNV(cap(it("P22a")), ["P25a", "P25b"], dash=True))]

# ties ^1-1489 ... ^1-1500
T_COV = "телесные узы алчности"
T_ILL = "телесные узы недоброжелательности"
T_SIL = "телесные узы приверженности обрядам и обетам"
T_IDAM = "телесные узы убеждённости «только это истинно»"
S["1-1489"] = [Q("P26a") + " Четыре вида уз " + DASH + " " + LC(T_COV, T_ILL, T_SIL, T_IDAM) + ". "
               f"{cap(T_COV)} возникают {LOB8_L}. {cap(T_ILL)} возникают {DOM2_L}. "
               + DJ(f"{cap(T_SIL)} и {T_IDAM} возникают {DIT4_L}", M.ANSWER(key("P26a")))]
S["1-1490"] = [QA("P26b", LA(EXC_REST("уз"), K4, V4, F3, R, NB))]
S["1-1491"] = [QA("P27a", A3R)]
S["1-1492"] = [QA("P27b", MPN)]
S["1-1493"] = [QA("P28a", LC(DIT4, LOBDV4, ETTH("жадности", "f"), DOM2, ETTH("неприязни", "f")))]
GV = ["жадность, возникшая " + LOBDV4_L, "неприязнь, возникшая " + DOM2_L, VIC, UDD]
S["1-1494"] = [QA("P28b", LA(*GV, K4, V4, F3, R, NB))]
S["1-1495"] = [Q("P29a") + " Эти же узы " + pred("P29a") + "."]
S["1-1496"] = [QA("P29b", LA(EXC_REST("уз"), K3, V3, F3, ALLR),
                  SNV(cap(it("P27b")), ["P29a", "P29b"], dash=True))]
S["1-1497"] = [QA("P30a", "там, где воззрение и жадность возникают вместе")]
S["1-1498"] = [QA("P30b", LC(LOB8, DOM2, ETTH("уз", "pl")), SNV(cap(it("P28b")), ["P30a", "P30b"], dash=True))]
S["1-1499"] = [QA("P31a", LA(*GV, K3, V3, F3, ALLR))]
S["1-1500"] = [QA("P31b", MPN, SNV(cap(it("P28a")), ["P31a", "P31b"], dash=True))]

# floods, yokes (abridged in the Pāli)
S["1-1501"] = [Q("P32a")[:-1] + "…."]
S["1-1502"] = [Q("P38a")[:-1] + "…."]

# hindrances ^1-1503 ... ^1-1514
H_LIST = ("помеха чувственного желания, помеха недоброжелательности, помеха вялости и сонливости, "
          "помеха беспокойства и угрызений, помеха колебания, помеха неведения")
S["1-1503"] = [Q("P44a") + " Шесть помех " + DASH + " " + H_LIST + ". "
               f"Помеха чувственного желания возникает {LOB8_L}, помеха недоброжелательности возникает {DOM2_L}, "
               f"помеха вялости и сонливости возникает {SASANKH_L}, помеха беспокойства возникает {UDDS_L}, "
               f"помеха угрызений возникает {DOM2_L}, помеха колебания возникает {VICS_L}, "
               + DJ(f"помеха неведения возникает {ALL_AK_L}", M.ANSWER(key("P44a")))]
S["1-1504"] = [QA("P44b", LA(EXC_REST("помех"), K4, V4, F3, R, NB))]
S["1-1505"] = [QA("P45a", A3R)]
S["1-1506"] = [QA("P45b", MPN)]
S["1-1507"] = [QA("P46a", AK12)]
S["1-1508"] = [QA("P46b", A4_NOAK)]
S["1-1509"] = [Q("P47a") + " Эти же помехи " + pred("P47a") + "."]
S["1-1510"] = [QA("P47b", LA(EXC_REST("помех"), K3, V3, F3, ALLR),
                  SNV(cap(it("P45b")), ["P47a", "P47b"], dash=True))]
S["1-1511"] = [QA("P48a", "там, где две или три помехи возникают вместе")]
S["1-1512"] = [QA("P48b", EXC_REST("помех"), SNV(cap(it("P46b")), ["P48a", "P48b"], dash=True))]
S["1-1513"] = [QA("P49a", A3R_NOAK)]
S["1-1514"] = [QA("P49b", MPN, SNV(cap(it("P46a")), ["P49a", "P49b"], dash=True))]

# misapprehension ^1-1515 ... ^1-1524
S["1-1515"] = [QA("P50a", f"искажение из-за воззрения возникает {DIT4_L}")]
S["1-1516"] = [QA("P50b", LA(EXC_REST("искажения"), K4, V4, F3, R, NB))]
S["1-1517"] = [QA("P51a", A3R)]
S["1-1518"] = [QA("P51b", MPN)]
S["1-1519"] = [QA("P52a", LC(DIT4, ETTH("искажения", "n")))]
PV4 = [LOBDV4, DOM2, VIC, UDD]
S["1-1520"] = [QA("P52b", LA(*PV4, K4, V4, F3, R, NB), SNV("Искажение", ["P52a", "P52b"], dash=True))]
# So eva parāmāso parāmāso ceva parāmaṭṭho ca: the P53a predicate, put in the singular
S["1-1521"] = [Q("P53a") + " Это же искажение является искажением и затронуто искажениями."]
S["1-1522"] = [QA("P53b", LA(EXC_REST("искажения"), K3, V3, F3, ALLR),
                  SNV(cap(it("P51b")), ["P53a", "P53b"], dash=True))]
S["1-1523"] = [QA("P54a", LA(*PV4, K3, V3, F3, ALLR))]
S["1-1524"] = [QA("P54b", MPN, SNV(cap(it("P50a")) + ", и " + it("P52a"), ["P54a", "P54b"], dash=True))]

# long intermediate pairs ^1-1525 ... ^1-1552
AGG = ["совокупность чувств", "совокупность восприятия", "совокупность формирующих факторов"]
AGG3 = LC(*AGG)
INTIM = ["телесное сообщение", "речевое сообщение"]   # kāyaviññatti, vacīviññatti
S["1-1525"] = [QA("P55a", LC(K4, AK, V4, F3))]
S["1-1526"] = [QA("P55b", LA(R, NB))]
S["1-1527"] = [QA("P56a", "зрительное сознание, слуховое сознание, обонятельное сознание, вкусовое сознание, "
                          "осязательное сознание, элемент ума, элемент умственного сознания")]
S["1-1528"] = [QA("P56b", LA(*AGG, R, NB))]
S["1-1529"] = [QA("P57a", AGG3)]
S["1-1530"] = [QA("P57b", LA("ум", R, NB))]
S["1-1531"] = [QA("P58a", AGG3)]
S["1-1532"] = [QA("P58b", LA(R, NB), "Ум нельзя определить " + DASH
                  + " ни как связанный с умом, ни как не связанный с умом.")]
S["1-1533"] = [QA("P59a", AGG3)]
S["1-1534"] = [QA("P59b", LA(R, NB), "Ум нельзя определить " + DASH
                  + " ни как соединённый с умом, ни как не соединённый с умом.")]
S["1-1535"] = [QA("P60a", LC(*AGG, *INTIM) + ", или любая другая материальная форма, рождённая умом, "
                  "вызванная умом, порождённая умом, " + DASH + " сфера видимых форм, сфера звуков, сфера запахов, "
                  "сфера вкусов, сфера осязаемого, элемент пространства, элемент воды, лёгкость материальной формы, "
                  "мягкость материальной формы, работоспособность материальной формы, нарастание материальной "
                  "формы, непрерывность материальной формы, пища, съедаемая кусками")]
NOT_CS = LA("ум", "остальная материальная форма", NB)
S["1-1536"] = [QA("P60b", NOT_CS)]
S["1-1537"] = [QA("P61a", LC(*AGG, *INTIM))]
S["1-1538"] = [QA("P61b", NOT_CS)]
S["1-1539"] = [QA("P62a", LC(*AGG, *INTIM))]
S["1-1540"] = [QA("P62b", NOT_CS)]
MRN = LA("ум", R, NB)
S["1-1541"] = [QA("P63a", AGG3)]
S["1-1542"] = [QA("P63b", MRN)]
S["1-1543"] = [QA("P64a", AGG3)]
S["1-1544"] = [QA("P64b", MRN)]
S["1-1545"] = [QA("P65a", AGG3)]
S["1-1546"] = [QA("P65b", MRN)]
S["1-1547"] = [QA("P66a", "сфера глаза… сфера ума")]
S["1-1548"] = [QA("P66b", "сфера видимых форм… сфера объектов ума")]
S["1-1549"] = [QA("P67a", "сфера глаза… пища, съедаемая кусками")]
S["1-1550"] = [QA("P67b", LA(K4, AK, V4, F3, "четыре великих элемента", NB))]
S["1-1551"] = [QA("P68a", LA(V3, KAMMA))]
S["1-1552"] = [QA("P68b", LA(K3, AK, F3, NKAMMA, M4, P4, NB))]

# clinging ^1-1553 ... ^1-1564
U_SENS = "цепляние за чувственные удовольствия"
U_DIT = "цепляние за воззрения"
U_SIL = "цепляние за обряды и обеты"
U_ATTA = "цепляние за учение о «я»"
S["1-1553"] = [Q("P69a") + " Четыре цепляния " + DASH + " " + LC(U_SENS, U_DIT, U_SIL, U_ATTA) + ". "
               f"{cap(U_SENS)} возникает {LOB8_L}. "
               + DJ(f"{cap(U_DIT)}, {U_SIL} и {U_ATTA} возникают {DIT4_L}", M.ANSWER(key("P69a")))]
S["1-1554"] = [QA("P69b", LA(EXC_REST("цепляний"), K4, V4, F3, R, NB))]
S["1-1555"] = [QA("P70a", A3R)]
S["1-1556"] = [QA("P70b", MPN)]
S["1-1557"] = [QA("P71a", LC(LOBDS4, LOBDV4, ETTH("жадности", "f")))]
UV = ["жадность, возникшая " + LOBDV4_L, DOM2, VIC, UDD]
S["1-1558"] = [QA("P71b", LA(*UV, K4, V4, F3, R, NB))]
S["1-1559"] = [Q("P72a") + " Эти же цепляния " + pred("P72a") + "."]
S["1-1560"] = [QA("P72b", LA(EXC_REST("цепляний"), K3, V3, F3, ALLR),
                  SNV(cap(it("P70b")), ["P72a", "P72b"], dash=True))]
S["1-1561"] = [QA("P73a", "там, где воззрение и жадность возникают вместе")]
S["1-1562"] = [QA("P73b", LC(LOB8, ETTH("цепляний", "pl")), SNV(cap(it("P71b")), ["P73a", "P73b"], dash=True))]
S["1-1563"] = [QA("P74a", LA(*UV, K3, V3, F3, ALLR))]
S["1-1564"] = [QA("P74b", MPN, SNV(cap(it("P71a")), ["P74a", "P74b"], dash=True))]

# defilements ^1-1565 ... ^1-1580
S["1-1565"] = [Q("P75a") + " Десять оснований омрачений " + DASH + " жадность, злоба, заблуждение, самомнение, "
               "воззрение, колебание, вялость, беспокойство, бессовестность, отсутствие страха перед дурным. "
               f"Жадность возникает {LOB8_L}. Злоба возникает {DOM2_L}. Заблуждение возникает {ALL_AK_L}. "
               f"Самомнение возникает {LOBDV4_L}. Воззрение возникает {DIT4_L}. Колебание возникает {VICS_L}. "
               f"Вялость возникает {SASANKH_L}. "
               + DJ(f"Беспокойство, бессовестность и отсутствие страха перед дурным возникают {ALL_AK_L}",
                    M.ANSWER(key("P75a")))]
S["1-1566"] = [QA("P75b", LA(EXC_REST("омрачений"), K4, V4, F3, R, NB))]
S["1-1567"] = [QA("P76a", A3R)]
S["1-1568"] = [QA("P76b", MPN)]
S["1-1569"] = [QA("P77a", AK12)]
S["1-1570"] = [QA("P77b", A4_NOAK)]
S["1-1571"] = [QA("P78a", AK12)]
S["1-1572"] = [QA("P78b", A4_NOAK)]
S["1-1573"] = [Q("P79a") + " Эти же омрачения " + pred("P79a") + "."]
S["1-1574"] = [QA("P79b", LA(EXC_REST("омрачений"), K3, V3, F3, ALLR),
                  SNV(cap(it("P76b")), ["P79a", "P79b"], dash=True))]
S["1-1575"] = [Q("P80a") + " Эти же омрачения " + pred("P80a") + "."]
S["1-1576"] = [QA("P80b", EXC_REST("омрачений"), SNV(cap(it("P77b")), ["P80a", "P80b"], dash=True))]
S["1-1577"] = [QA("P81a", "там, где два или три омрачения возникают вместе")]
S["1-1578"] = [QA("P81b", EXC_REST("омрачений"), SNV(cap(it("P78b")), ["P81a", "P81b"], dash=True))]
S["1-1579"] = [QA("P82a", A3R_NOAK)]
S["1-1580"] = [QA("P82b", MPN, SNV(cap(it("P78a")), ["P82a", "P82b"], dash=True))]

# closing pairs ^1-1581 ... ^1-1616
S["1-1581"] = [QA("P83a", LC(DIT4, VIC), DJ(SIYA2, SIYA(S_("P83a"), S_("P83b")) + "."))]
S["1-1582"] = [QA("P83b", LA(UDD, K4, V4, F3, R, NB))]
S["1-1583"] = [QA("P84a", UDD, DJ(SIYA2, SIYA(S_("P84a"), S_("P84b")) + "."))]
S["1-1584"] = [QA("P84b", LA(DIT4, VIC, K4, V4, F3, R, NB))]
S["1-1585"] = [QA("P85a", LC(DIT4, VIC, ETTH("заблуждения", "n")), DJ(SIYA2, SIYA(S_("P85a"), S_("P85b")) + "."))]
S["1-1586"] = [QA("P85b", LA(VICMOHA, UDD, K4, V4, F3, R, NB))]
S["1-1587"] = [QA("P86a", LC(UDD, ETTH("заблуждения", "n")), DJ(SIYA2, SIYA(S_("P86a"), S_("P86b")) + "."))]
S["1-1588"] = [QA("P86b", LA(DIT4, VIC, UDDMOHA, K4, V4, F3, R, NB))]
S["1-1589"] = [QA("P87a", LC(*I_SAVITAKKA, ETTH("направленной мысли", "f")))]
S["1-1590"] = [QA("P87b", LA(PV, JH("r", 3, 4) + " " + KVK, ARV4 + " " + KVK, JH("l", 3, 4) + " " + KV,
                             "направленная мысль", R, NB))]
S["1-1591"] = [QA("P88a", LC(KAMK, AK, NUMF(KAMKV_F, "одиннадцать", CU), NUMF(AKV_F, "два"),
                             NUMF(KIR_F, "одиннадцать"), JH("r", 1, 2) + " " + KVK, JH("l", 1, 2) + " " + KV,
                             ETTH("удержания мысли", "n")))]
S["1-1592"] = [QA("P88b", LA(PV, JH("r", 3, 3) + " " + KVK, ARU4 + " " + KVK, JH("l", 3, 3) + " " + KV,
                             "удержание мысли", R, NB))]
S["1-1593"] = [QA("P89a", LC(*I_PITI, ETTH("восторга", "m")))]
S["1-1594"] = [QA("P89b", LA(*I_APITI, "восторг", R, NB))]
S["1-1595"] = [QA("P90a", LC(*I_PITI, ETTH("восторга", "m")))]
S["1-1596"] = [QA("P90b", LA(*I_APITI, "восторг", R, NB))]
S["1-1597"] = [QA("P91a", LC(*I_SUKHA, ETTH("счастья", "n")))]
S["1-1598"] = [QA("P91b", LA(NUMF(KAMK_F, "четыре", UPE), NUMF(AK_F, "восемь"), NUMF(KAMKV_F, "десять"),
                             NUMF(AKV_F, "семь"), NUMF(KIR_F, "шесть"), R4J + " " + KVK, ARU4 + " " + KVK,
                             L4J + " " + KV, "счастье", R, NB))]
S["1-1599"] = [QA("P92a", LC(*I_UPEKKHA, ETTH("невозмутимости", "f")))]
S["1-1600"] = [QA("P92b", LA(NUMF(KAMK_F, "четыре", SOM), NUMF(AK_F, "шесть"), NUMF(KAMKV_F, "шесть"),
                             NUMF(AKV_F, "один"), NUMF(KIR_F, "пять"), JH("r", 3, 4) + " " + KVK,
                             JH("l", 3, 4) + " " + KV, "невозмутимость", R, NB))]
S["1-1601"] = [QA("P93a", LA(KAMK, AK, ALL_KAMV, KAMKIR, ALLR))]
S["1-1602"] = [QA("P93b", LC(it("P94a"), it("P95a"), it("P96b")))]
S["1-1603"] = [QA("P94a", JH("r", 4, 5) + " " + KVK)]
S["1-1604"] = [QA("P94b", LC(it("P93a"), it("P95a"), it("P96b")))]
S["1-1605"] = [QA("P95a", ARU4 + " " + KVK)]
S["1-1606"] = [QA("P95b", LC(it("P93a"), it("P94a"), it("P96b")))]
S["1-1607"] = [QA("P96a", A3R)]
S["1-1608"] = [QA("P96b", MPN)]
S["1-1609"] = [QA("P97a", M4)]
S["1-1610"] = [QA("P97b", LA(K3, AK, V4, F3, R, NB))]
S["1-1611"] = [Q("P98a") + " " + DJ(cap(LC(DIT4, DOM2)), SIYA(S_("P98a"), S_("P98b")) + ". ")
               + DJ(cap(M4), M.ANSWER(key("P98a")))]
S["1-1612"] = [QA("P98b", LA(LOBDV4, VIC, UDD, K3, V4, F3, R, NB))]
S["1-1613"] = [QA("P99a", A3R)]
S["1-1614"] = [QA("P99b", MPN)]
S["1-1615"] = [QA("P100a", AK12)]
S["1-1616"] = [QA("P100b", A4_NOAK), "Разъяснение смысла завершено.", "Книга «Перечисление явлений» завершена."]

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
    ws = [w for w in p.split() if w != "dhammā"]
    if ws and ws[-1].endswith("āpi"):
        ws[-1] = ws[-1][:-2]
    return " ".join(ws)


def check_questions(segs):
    """Each 'Katame dhammā X?' must open with the Russian question of a matrix item whose Pāli is X."""
    qs, prev = {}, {}
    for bid, letter, pali, _ru in M.MATRIX_ITEMS_RU:
        n = norm_item(pali)
        if letter == "б" and " " not in n and pali.rstrip(".").endswith("pi"):
            n = " ".join(prev[bid].split()[:-1] + [n])     # elliptical (б) line: na hetū … ahetukāpi
        prev[bid] = n
        if M.PRED[(bid, letter)]:
            qs.setdefault(n, set()).add(M.QUESTION((bid, letter))[:-1])
    bad = []
    for bid, plines in segs:
        pm = re.match(r"Katame dhammā (.+?)(\?|\.|…)", plines[0])
        if not pm:
            continue
        cands = qs.get(pm.group(1), set())
        if not any(S[bid][0].startswith(c) for c in cands):
            bad.append((bid, pm.group(1), S[bid][0][:80]))
    return bad


def build():
    out = []
    segs = pali_segments()
    assert len(segs) == len(S) and {b for b, _ in segs} == set(S), (set(S) ^ {b for b, _ in segs})
    bad = check_questions(segs)
    assert not bad, bad
    for bid, plines in segs:
        rlines = S[bid]
        assert len(rlines) == len(plines), (bid, len(plines), len(rlines))
        for p, r in zip(plines, rlines):
            assert p.count("–") + p.count("—") == r.count("–") + r.count("—"), (bid, p, r)
            assert p.count("?") == r.count("?"), (bid, p, r)
            assert p.count("[") == r.count("["), (bid, p, r)
            assert p.count("…pe…") == r.count("…"), (bid, p, r)
            assert "—" not in r and ":-" not in r and "  " not in r and ",," not in r, (bid, r)
            assert p.startswith("#") == r.startswith("#"), (bid, p, r)
            if p.startswith("#"):
                assert len(p) - len(p.lstrip("#")) == len(r) - len(r.lstrip("#")), (bid, p, r)
        rlines = [cap(rlines[0])] + rlines[1:]
        rlines = rlines[:-1] + [rlines[-1] + f" ^{bid}"]
        out.append("\n".join(rlines))
    return "\n\n".join(out) + "\n"


if __name__ == "__main__":
    TEXT = build()
    OUT.write_text(TEXT, encoding="utf-8", newline="\n")
    print("wrote", OUT, "segments", len(S))
