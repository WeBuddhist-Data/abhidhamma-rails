"""Builder for the Russian rails translation of pi-1 (Dhammasaṅgaṇī, plain audience), chapter 5
(Aṭṭhakathākaṇḍaṃ: for each matrix item, the kinds of mind and the phenomena it covers; ^1-1384 … ^1-1616).

Writes (only when run as a script):
  AI_translation/russian/pi-1-russian-plain-rails_split_chapters/5-atthakathakandam.md
  0-INBOX/temp/pipeline/pi-1-ru/rails/notes-5.md

Every line is built from the fixed strings below. The earlier rails builders are imported, never edited:
build_rails_sample_ru.py (S: matrix names, question and answer forms, headings), build_rails_4-01_ru.py (F: the
frames, «и та материальная форма, которая …», the taint / fetter / tie names, the sense-base strings, «Те самые …
и есть …»), build_rails_4-02_4-03_ru.py (G: hindrance and clinging names, the ten defilement bases, «Ум нельзя
определить – …», «То самое искажение …»). Segments whose Pāli is identical to a segment of chapters 2-4 reuse
that Russian from the finished output files (REUSE below, checked against the Pāli).
Punctuation before the Pāli dash (coordinator 2026-11-14): «X – это …» after a plain noun or list; «…, – это …»
where the dash closes a participial phrase, a subordinate clause or a closing «кроме …» phrase (sample ^1-62).
Items that end inside such a phrase carry the marker «§» until they are joined.
Terms follow the locked termbase AI_translation/russian/pi-1-pali-russian-termbase-plain.md; cittuppāda = «вид ума»
(user: «двенадцать видов неблагого ума»).

usage: python -I -X utf8 build_rails_5_ru.py
"""
import importlib.util
import pathlib
import re
import sys

HERE = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-ru\rails")
sys.path.insert(0, str(HERE))
import build_rails_sample_ru as S  # noqa: E402  (importing writes nothing)


def _load(name, fn):
    spec = importlib.util.spec_from_file_location(name, HERE / fn)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)       # importing writes nothing
    return mod


F = _load("build_rails_4_01_ru", "build_rails_4-01_ru.py")
G = _load("build_rails_4_02_4_03_ru", "build_rails_4-02_4-03_ru.py")

PART = "5-atthakathakandam.md"
PALI = S.PALI / PART
OUT = S.OUT / PART
cap, low = S.cap, S.low
PE, ELL = "…pe…", "…"
N, Q = F.N, F.Q
OPEN = "§"          # item ends inside a participial phrase / clause / «кроме …» phrase
NOTES = []          # (pali, russian) new recurring formulas, written to notes-5.md


def note(p, r):
    NOTES.append((p, r.replace(OPEN, "")))
    return r


def plain(s):
    return s.replace(OPEN, "")


def is_open(s):
    return s.endswith(OPEN)


# =========================================================================================
# 1. Answer frames
# =========================================================================================
def tail(body):
    """«body – » with the comma kept where the body ends inside a phrase."""
    return f"{cap(plain(body))}{', – ' if is_open(body) else ' – '}"


def qa(p, body):
    """Katame dhammā p? body – ime dhammā p."""
    return f"{Q(p)} {tail(body)}{S.a_form(N[p])}"


def ans(body, text):
    """body – ime dhammā <text>."""
    return f"{tail(body)}это {text}."


def nv(names):
    """na vattabbā Xtipi, Ytipi = ни как X, ни как Y; one item: как X"""
    return "как " + names[0] if len(names) == 1 else "ни как " + ", ни как ".join(names)


NV_ALL = "явления, которые нельзя определить {}"          # ime dhammā na vattabbā …
NV_THEM = "их нельзя определить {}"                        # (siyā) na vattabbā … (after a siyā list)
_NV_SUBJ = "{} нельзя определить – {}."                   # X dhammā na vattabbā – Ytipi, Ztipi.


class _NvSubj:
    """the subject closes its participial phrase with a comma: «Явления, не имеющие корней, нельзя …»"""
    @staticmethod
    def format(subj, rest):
        return _NV_SUBJ.format(subj + ("," if ", " in subj else ""), rest)


NV_SUBJ = _NvSubj()


def siya(*ps):
    return ", ".join(f"иногда {N[p]}" for p in ps)


note("Katame dhammā X? … – ime dhammā siyā X, siyā Y.", "Что такое X? … – это иногда X, иногда Y.")
note("na X (in a siyā list)", "но не X")
note("ime dhammā na vattabbā Xtipi, Ytipi", "это явления, которые нельзя определить ни как X, ни как Y")
note("siyā na vattabbā Xtipi, Ytipi / na vattabbā Xti", "иногда их нельзя определить ни как X, ни как Y / их нельзя "
     "определить как X")
note("X dhammā na vattabbā – Ytipi, Ztipi.", "X нельзя определить – ни как Y, ни как Z.")

# =========================================================================================
# 2. Kinds of mind
# =========================================================================================
K4 = note("Catūsu bhūmīsu kusalaṃ", "благой ум четырёх миров")
K3 = note("tīsu bhūmīsu kusalaṃ", "благой ум трёх миров")
AK = note("akusalaṃ", "неблагой ум")
V4 = note("catūsu bhūmīsu vipāko", "результат действий четырёх миров")
V3 = note("tīsu bhūmīsu vipāko", "результат действий трёх миров")
KR3 = note("tīsu bhūmīsu kiriyābyākataṃ", "этически неопределённый функциональный ум трёх миров")
KK = note("Kāmāvacarakusalaṃ / Kāmāvacaraṃ kusalaṃ", low(S.H_KAMA_KUSALA) + OPEN)
KV_ALL = note("sabbo kāmāvacarassa vipāko", "весь результат действий, относящийся к миру чувственных желаний" + OPEN)
KKR = note("kāmāvacarakiriyābyākataṃ",
           "этически неопределённый функциональный ум, относящийся к миру чувственных желаний" + OPEN)
AK12 = note("Dvādasa akusalacittuppādā", "двенадцать видов неблагого ума")
SABBAK = note("sabbaṃ akusalaṃ", "весь неблагой ум")
RN = note("rūpañca, nibbānañca (closing a list)", "и материальная форма, и нирвана")
SABBA_R = note("sabbañca rūpaṃ (closing a list)", "и вся материальная форма")
NIB = "и нирвана"
LOK3 = note("Cattāro maggā apariyāpannā, cattāri ca sāmaññaphalāni, nibbānañca",
            f"{F.FOUR_PATHS}, четыре плода отшельничества и нирвана")
LOK2 = note("Cattāro maggā apariyāpannā, cattāri ca sāmaññaphalāni",
            f"{F.FOUR_PATHS}, и четыре плода отшельничества")
PATHS4 = low(F.FOUR_PATHS) + OPEN                                     # in a longer list
FRUITS4 = "четыре плода отшельничества"
note("Kāmāvacarakusalaṃ, akusalaṃ, …", "благой ум, относящийся к миру чувственных желаний; неблагой ум; … "
     "(items with inner commas are joined with «;»)")

# the counted kinds of mind (cittuppāda = «вид ума»)
NUM = {"eko": "один", "dve": "два", "cattāro": "четыре", "pañca": "пять", "cha": "шесть", "satta": "семь",
       "aṭṭha": "восемь", "nava": "девять", "dasa": "десять", "ekādasa": "одиннадцать"}


def vid(n):
    n = NUM[n]
    return f"{n} {'вид' if n == 'один' else 'вида' if n in ('два', 'три', 'четыре') else 'видов'}"


def kkv(n, qual):
    """Kāmāvacarakusalato N <qual>cittuppādā"""
    return f"{vid(n)} благого ума, относящегося к миру чувственных желаний, {qual}{OPEN}"


def akv(n):
    """akusalato N"""
    return f"{vid(n)} неблагого ума"


def kkvip(n, cit=False):
    """kāmāvacarakusalassa vipākato N [cittuppādā]"""
    return (f"{vid(n) + ' ума' if cit else NUM[n]} в виде результатов благого ума, относящегося к миру чувственных "
            f"желаний{OPEN}")


def akvip(n):
    """akusalassa vipākato N"""
    return f"{NUM[n]} в виде результатов неблагого ума"


def kir(n, cit=False):
    """kiriyato N [cittuppādā]"""
    return f"{vid(n) + ' ума' if cit else NUM[n]} в функциональном виде"


def kirq(n, qual):
    """kiriyato N <qual>cittuppādā"""
    return f"{vid(n)} ума, {qual}, в функциональном виде"


note("Kāmāvacarakusalato N X-cittuppādā", "N видов благого ума, относящегося к миру чувственных желаний, X")
note("akusalato N", "N видов неблагого ума")
note("kāmāvacarakusalassa vipākato N [cittuppādā]",
     "N [видов ума] в виде результатов благого ума, относящегося к миру чувственных желаний")
note("akusalassa vipākato N", "N в виде результатов неблагого ума")
note("kiriyato N [cittuppādā]", "N [видов ума] в функциональном виде")
note("kiriyato N X-cittuppādā", "N видов ума, X, в функциональном виде")

KVK = note("kusalato ca vipākato ca kiriyato ca", "в благом виде, в виде результатов действий и в функциональном виде")
KV = note("kusalato ca vipākato ca", "в благом виде и в виде результатов действий")
KKI = note("kusalato ca kiriyato ca", "в благом виде и в функциональном виде")

# absorptions: <a><b>jjhānā = a by the fourfold method and b by the fivefold method
JN = {"ekakaduka": ("одно", "два"), "dukaduka": ("два", "два"), "dukatika": ("два", "три"),
      "tikatika": ("три", "три"), "tikacatukka": ("три", "четыре"), "catukkapañcaka": ("четыре", "пять")}


def rj(code, mode):
    a, b = JN[code]
    head = ("одно медитативное погружение, относящееся к миру форм," if a == "одно"
            else f"{a} медитативных погружения, относящихся к миру форм,")
    return f"{head} по четверичному методу и {b} по пятеричному {mode}"


def lj(code, mode):
    a, b = JN[code]
    head = "одно надмирское медитативное погружение" if a == "одно" else f"{a} надмирских медитативных погружения"
    return f"{head} по четверичному методу и {b} по пятеричному {mode}"


assert lj("tikacatukka", "").strip() == ("три надмирских медитативных погружения по четверичному методу и четыре по "
                                          "пятеричному")   # termbase lokuttaratikacatukkajjhānā
note("rūpāvacara-tikacatukka-jjhānā (likewise ekakaduka, dukaduka, dukatika, tikatika, catukkapañcaka)",
     rj("tikacatukka", "").strip())
note("lokuttara-tikacatukka-jjhānā", lj("tikacatukka", "").strip())
RJ1 = "первое медитативное погружение, относящееся к миру форм,"     # rūpāvacaraṃ paṭhamaṃ jhānaṃ
RJ4 = "четвёртое медитативное погружение, относящееся к миру форм,"  # rūpāvacaraṃ catutthaṃ jhānaṃ
RJ2P = "второе медитативное погружение, относящееся к миру форм, по пятеричному методу"   # Rūpāvacarapañcakanaye …
LJ1 = "первое надмирское медитативное погружение"
LJ4 = "четвёртое надмирское медитативное погружение"
LJ2P = "второе надмирское медитативное погружение по пятеричному методу"
ARUPPA4 = "четыре бесформенных состояния"                          # cattāro āruppā
ARUPA4 = "четыре вида ума, относящихся к миру без форм,"           # cattāro arūpāvacarā
J4VIP = "результат действий четвёртого медитативного погружения"   # catutthassa jhānassa vipāko
for _p, _r in [("rūpāvacaraṃ paṭhamaṃ jhānaṃ X", RJ1 + " X"), ("rūpāvacaraṃ catutthaṃ jhānaṃ X", RJ4 + " X"),
               ("Rūpāvacarapañcakanaye dutiyaṃ jhānaṃ", RJ2P), ("lokuttaraṃ paṭhamaṃ jhānaṃ", LJ1),
               ("lokuttaraṃ catutthaṃ jhānaṃ", LJ4), ("lokuttarapañcakanaye dutiyaṃ jhānaṃ", LJ2P),
               ("cattāro āruppā", ARUPPA4), ("cattāro arūpāvacarā X", ARUPA4 + " X"),
               ("catutthassa jhānassa vipāko", J4VIP)]:
    note(_p, _r)
SPH = {"ākāsānañcāyatanaṃ": "сфера бесконечного пространства", "viññāṇañcāyatanaṃ": "сфера бесконечного сознания",
       "ākiñcaññāyatanaṃ": "сфера отсутствия чего-либо",
       "nevasaññānāsaññāyatanaṃ": "сфера ни восприятия, ни невосприятия"}
VN_NEVA = f"{cap(SPH['viññāṇañcāyatanaṃ'])} и {SPH['nevasaññānāsaññāyatanaṃ']}"

DVP = note("Dvepañcaviññāṇāni", "дважды пять видов сознания")
MD3 = note("tisso ca manodhātuyo", "три элемента ума")
AHM5 = note("pañca ca ahetukamanoviññāṇadhātuyo", "пять элементов умственного сознания без корней")
KMD = note("kiriyāmanodhātu", "функциональный элемент ума")
KAHM_S = note("kiriyāhetukamanoviññāṇadhātu somanassasahagatā",
              "функциональный элемент умственного сознания без корней, сопровождаемый радостью" + OPEN)
KAHM_U = note("kiriyāhetukamanoviññāṇadhātu upekkhāsahagatā",
              "функциональный элемент умственного сознания без корней, сопровождаемый невозмутимостью" + OPEN)
AKV_MVD_U = note("akusalassa vipākato manoviññāṇadhātu upekkhāsahagatā",
                 "элемент умственного сознания, сопровождаемый невозмутимостью, в виде результатов неблагого ума")
MOHA_V = note("vicikicchāsahagato moho", "заблуждение, сопровождаемое колебанием" + OPEN)
MOHA_U = note("uddhaccasahagato moho", "заблуждение, сопровождаемое беспокойством" + OPEN)
CU_V = note("vicikicchāsahagato cittuppādo", "вид ума, сопровождаемый колебанием" + OPEN)
CU_U = note("uddhaccasahagato cittuppādo", "вид ума, сопровождаемый беспокойством" + OPEN)
DS4 = note("Cattāro diṭṭhigatasampayuttacittuppādā", "четыре вида ума, связанных с приверженностью воззрениям" + OPEN)
DV4 = note("Cattāro diṭṭhigatavippayutta(-)lobhasahagatacittuppādā",
           "четыре вида ума, не связанных с приверженностью воззрениям, сопровождаемых жадностью" + OPEN)
DSL4 = note("Cattāro diṭṭhigatasampayuttalobhasahagatacittuppādā",
            "четыре вида ума, связанных с приверженностью воззрениям, сопровождаемых жадностью" + OPEN)
DOM2 = note("Dve domanassasahagatacittuppādā", "два вида ума, сопровождаемых унынием" + OPEN)
LOB8 = note("Aṭṭha lobhasahagatacittuppādā", "восемь видов ума, сопровождаемых жадностью" + OPEN)
DUKKHA_KV = note("dukkhasahagataṃ kāyaviññāṇaṃ", "осязательное сознание, сопровождаемое болью" + OPEN)
UPEKKHA_V = note("yā ca vedanā upekkhā", "то чувство, которое является невозмутимостью" + OPEN)
IN = {"lobha8": "в восьми видах ума, сопровождаемых жадностью",
      "domanassa2": "в двух видах ума, сопровождаемых унынием",
      "dv4": "в четырёх видах ума, не связанных с приверженностью воззрениям, сопровождаемых жадностью",
      "ds4": "в четырёх видах ума, связанных с приверженностью воззрениям",
      "vic": "в видах ума, сопровождаемых колебанием", "udd": "в видах ума, сопровождаемых беспокойством",
      "all": "во всех видах неблагого ума", "sas": "в видах неблагого ума с побуждением"}
for _p, _k in [("aṭṭhasu lobhasahagatesu cittuppādesu", "lobha8"),
               ("dvīsu domanassasahagatesu cittuppādesu", "domanassa2"),
               ("catūsu diṭṭhigatavippayuttalobhasahagatesu cittuppādesu", "dv4"),
               ("catūsu diṭṭhigatasampayuttesu cittuppādesu", "ds4"), ("vicikicchāsahagatesu cittuppādesu", "vic"),
               ("uddhaccasahagatesu cittuppādesu", "udd"), ("sabbākusalesu", "all"),
               ("sasaṅkhārikesu akusalesu", "sas")]:
    note(_p, IN[_k])
LOBHA_DV = note("Catūsu diṭṭhigatavippayuttalobhasahagatesu cittuppādesu uppanno lobho",
                f"жадность, возникшая {IN['dv4']}" + OPEN)
PATIGHA_D = note("dvīsu domanassasahagatesu cittuppādesu uppannaṃ paṭighaṃ",
                 f"неприязнь, возникшая {IN['domanassa2']}" + OPEN)
MOHA_D = note("Dvīsu domanassasahagatesu cittuppādesu uppanno moho",
              f"заблуждение, возникшее {IN['domanassa2']}" + OPEN)

# «кроме …»
EXC_RES = note("kāmāvacarassa vipākato ahetuke cittuppāde ṭhapetvā",
               "кроме видов ума без корней, относящихся к миру чувственных желаний, в виде результатов действий")
EXC_KIR = note("kāmāvacarakiriyato ahetuke cittuppāde ṭhapetvā",
               "кроме видов ума без корней, относящихся к миру чувственных желаний, в функциональном виде")
V4_EXC = f"{V4}, {EXC_RES}" + OPEN
KR3_EXC = f"{KR3}, {EXC_KIR}" + OPEN
REST_MU = note("Vicikicchāsahagataṃ uddhaccasahagataṃ mohaṃ ṭhapetvā avasesaṃ akusalaṃ",
               "кроме заблуждения, сопровождаемого колебанием, и заблуждения, сопровождаемого беспокойством, "
               "остальной неблагой ум")
REST_U = note("Uddhaccasahagataṃ mohaṃ ṭhapetvā avasesaṃ akusalaṃ",
              "кроме заблуждения, сопровождаемого беспокойством, остальной неблагой ум")
GEN = {"āsave": "влечений", "saṃyojane": "оков", "ganthe": "уз", "nīvaraṇe": "помех", "parāmāsaṃ": "искажения",
       "upādāne": "цепляний", "kilese": "омрачений", "hetū": "корней"}


def rest(key):
    """Ṭhapetvā X avasesaṃ akusalaṃ"""
    return f"кроме {GEN[key]}, остальной неблагой ум"


note("Ṭhapetvā X(-e) avasesaṃ akusalaṃ", "Кроме X (genitive), остальной неблагой ум")
# etthuppannaṃ X ṭhapetvā (sg.) / etthuppanne X ṭhapetvā (pl.); termbase: uppanne vitakkavicāre «возникшие в них
# направленная мысль и удержание мысли», uppannaṃ vicāraṃ «возникшее в них удержание мысли», uppanne hetū «возникшие
# в них корни», uppannaṃ vitakkaṃ «возникшая в них направленная мысль» (ettha = «в них»)
HERE_X = {"sukhaṃ vedanaṃ": "возникшего в них приятного чувства",
          "dukkhaṃ vedanaṃ": "возникшего в них болезненного чувства",
          "adukkhamasukhaṃ vedanaṃ": "возникшего в них чувства, которое ни болезненно, ни приятно",
          "vitakkavicāre": "возникших в них направленной мысли и удержания мысли",
          "vitakkaṃ": "возникшей в них направленной мысли", "vicāraṃ": "возникшего в них удержания мысли",
          "pītiṃ": "возникшего в них восторга", "sukhaṃ": "возникшего в них счастья",
          "upekkhaṃ": "возникшей в них невозмутимости", "mohaṃ": "возникшего в них заблуждения",
          "lobhaṃ": "возникшей в них жадности", "paṭighaṃ": "возникшей в них неприязни",
          "parāmāsaṃ": "возникшего в них искажения", "hetū": "возникших в них корней",
          "ganthe": "возникших в них уз", "upādāne": "возникших в них цепляний"}


def ex(key):
    return f"кроме {HERE_X[key]}"


note("etthuppannaṃ X ṭhapetvā / etthuppanne X ṭhapetvā", "кроме возникшего в них X / кроме возникших в них X")


# =========================================================================================
# 3. Joining a list of items
# =========================================================================================
CLOSERS_DOUBLE = (RN,)                    # «и …, и …»: always after the separator
CLOSERS_SINGLE = (SABBA_R, NIB)           # single «и …»: no comma before it in a comma list


def J(*items, trailer=None):
    """Join answer items as the Pāli lists them; «;» between items once any item has inner commas.
    trailer: a closing «кроме …» phrase that applies to the whole list."""
    its = list(items)
    inner = [plain(x) for x in its if x not in CLOSERS_DOUBLE and "которая" not in x]
    sep = "; " if any("," in x for x in inner) else ", "
    out = plain(its[0])
    for i, x in enumerate(its[1:], 1):
        prev = its[i - 1]
        if sep == ", " and x in CLOSERS_SINGLE and not is_open(prev) and "которая" not in prev:
            out += " " + x
        else:
            out += sep + plain(x)
    last_open = is_open(its[-1])
    if trailer:
        out += ", " + trailer
        last_open = True
    return out + (OPEN if last_open else "")


# =========================================================================================
# 4. Name forms used outside the «это X» frame
# =========================================================================================
SG = {"savitakkasavicārā": "явление с направленной мыслью и удержанием мысли",
      "avitakkavicāramattā": "явление без направленной мысли, только с удержанием мысли",
      "avitakkaavicārā": "явление без направленной мысли и без удержания мысли",
      "pītisahagatā": "явление, сопровождаемое восторгом",
      "uppannā": "возникшее явление", "anuppannā": "невозникшее явление",
      "uppādino": "явление, которому предстоит возникнуть",
      "atītā": "прошлое явление", "anāgatā": "будущее явление", "paccuppannā": "настоящее явление",
      "ajjhattārammaṇā": "явление с внутренним объектом", "bahiddhārammaṇā": "явление с внешним объектом",
      "ajjhattabahiddhārammaṇā": "явление с внутренним и внешним объектом"}
INS ={"atītā": "прошлыми явлениями", "anāgatā": "будущими явлениями", "paccuppannā": "настоящими явлениями",
       "ajjhattā": "внутренними явлениями", "bahiddhā": "внешними явлениями",
       "ajjhattabahiddhā": "внутренними и внешними явлениями"}
for _p, _r in INS.items():
    assert N[_p].split()[-1] == "явления" and _r.endswith("явлениями"), _p


def nvn(*ps):
    return nv([N[p] for p in ps])


def nvs(*ps):
    return nv([SG[p] for p in ps])


# =========================================================================================
# 5. Headings, fixed lines, reuse
# =========================================================================================
EXACT = {
    "### Aṭṭhakathākaṇḍaṃ": "### " + S.CH_HEADINGS["Aṭṭhakathākaṇḍaṃ"],
    "#### Tikaatthuddhāro": "#### Разъяснение смысла троек",
    "#### Dukaatthuddhāro": "#### Разъяснение смысла пар",
    "Tikaṃ.": F.EXACT["Tikaṃ."],
    "Atthuddhāro niṭṭhito.": "Разъяснение смысла завершено.",
    "Dhammasaṅgaṇīpakaraṇaṃ niṭṭhitaṃ.": f"Книга «{S.H_BOOK}» завершена.",
}
for _p, _r in EXACT.items():
    note(_p, _r)

PREV = ["4-01-nikkhepakandam.md", "4-02-nikkhepakandam.md", "4-03-nikkhepakandam.md"]
STRIP = re.compile(r"\s*\^[0-9A-Za-z-]+\s*$")
REUSE = {   # chapter-5 segment = earlier segment with identical Pāli (found by reuse_5.py)
    "1-1412": "1-1021", "1-1414": "1-1023", "1-1427": "1-1036", "1-1438": "1-1056", "1-4-2-1-0": "1-3-2-1-0",
    "1-4-2-2-0": "1-3-2-2-0", "1-1457": "1-1093", "1-1459": "1-1095", "1-4-2-3-0": "1-3-2-3-0",
    "1-4-2-4-0": "1-3-2-4-0", "1-1483": "1-1134", "1-4-2-5-0": "1-3-2-5-0", "1-1495": "1-1150",
    "1-4-2-6-0": "1-3-2-6-0", "1-4-2-7-0": "1-3-2-7-0", "1-4-2-8-0": "1-3-2-8-0", "1-1509": "1-1174",
    "1-4-2-9-0": "1-3-2-9-0", "1-4-2-10-0": "1-3-2-10-0", "1-1527": "1-1193", "1-1529": "1-1195",
    "1-1531": "1-1197", "1-1533": "1-1199", "1-1537": "1-1203", "1-1539": "1-1205", "1-1541": "1-1207",
    "1-1543": "1-1209", "1-1545": "1-1211", "1-1547": "1-1213", "1-1548": "1-1214", "1-1549": "1-1215",
    "1-4-2-11-0": "1-3-2-11-0", "1-1559": "1-1229", "1-4-2-12-0": "1-3-2-12-0", "1-1573": "1-1253",
    "1-1575": "1-1255", "1-4-2-13-0": "1-3-2-13-0", "1-1602": "1-1288", "1-1604": "1-1290", "1-1606": "1-1292",
    "1-1609": "1-1295",
}


def _prev():
    pali, ru = {}, {}
    for ch in PREV:
        for sid, pl in S.segments(S.PALI / ch):
            pali[sid] = [STRIP.sub("", x) for x in pl]
        for sid, rl in S.segments(S.OUT / ch):
            ru[sid] = [STRIP.sub("", x) for x in rl]
    return pali, ru


PREV_PALI, PREV_RU = _prev()

# =========================================================================================
# 6. The segments
# =========================================================================================
R = {}


def seg(sid, *lines):
    assert sid not in R, sid
    R[sid] = list(lines)


NV_FEEL = NV_ALL.format(nvn("sukhāya vedanāya sampayuttā", "dukkhāya vedanāya sampayuttā",
                            "adukkhamasukhāya vedanāya sampayuttā"))
UPEKKHA_SET = [kkv("cattāro", "сопровождаемых невозмутимостью"), akv("cha"), kkvip("dasa"), akvip("cha"), kir("cha"),
               f"{RJ4} {KVK}"]

# ---------------------------------------------------------------- triads
seg("1-1384", qa("kusalā", K4))
seg("1-1385", qa("akusalā", AK12))
seg("1-1386", qa("abyākatā", J(V4, KR3, RN)))
seg("1-1387", qa("sukhāya vedanāya sampayuttā",
                 J(kkv("cattāro", "сопровождаемых радостью"), akv("cattāro"),
                   "по пять в виде результатов благого ума, относящегося к миру чувственных желаний, и в "
                   "функциональном виде", rj("tikacatukka", KVK), lj("tikacatukka", KV), trailer=ex("sukhaṃ vedanaṃ"))))
seg("1-1388", qa("dukkhāya vedanāya sampayuttā", J(DOM2, DUKKHA_KV, trailer=ex("dukkhaṃ vedanaṃ"))))
seg("1-1389", qa("adukkhamasukhāya vedanāya sampayuttā",
                 J(*UPEKKHA_SET, f"{ARUPA4} {KVK}", f"{LJ4} {KV}", trailer=ex("adukkhamasukhaṃ vedanaṃ")))
    + " " + ans("И три чувства, и материальная форма, и нирвана", NV_FEEL))
seg("1-1390", qa("vipākā", V4))
seg("1-1391", qa("vipākadhammadhammā", f"{K4} и {AK}"))
seg("1-1392", qa("nevavipākanavipākadhammadhammā", J(KR3, RN)))
seg("1-1393", qa("upādiṇṇupādāniyā", f"{V3}, {F.YANCA_KAMMA}" + OPEN))
seg("1-1394", qa("anupādiṇṇupādāniyā", f"{K3}, {AK}, {KR3}, {F.YANCA_NA_KAMMA}" + OPEN))
seg("1-1395", qa("anupādiṇṇaanupādāniyā", LOK3))
seg("1-1396", qa("saṃkiliṭṭhasaṃkilesikā", AK12))
seg("1-1397", qa("asaṃkiliṭṭhasaṃkilesikā", J(K3, V3, KR3, SABBA_R)))
seg("1-1398", qa("asaṃkiliṭṭhaasaṃkilesikā", LOK3))
SAVITAKKA_SET = [KK, AK, kkvip("ekādasa", True), akvip("dve"), kir("ekādasa")]
seg("1-1399", qa("savitakkasavicārā", J(*SAVITAKKA_SET, f"{RJ1} {KVK}", f"{LJ1} {KV}", trailer=ex("vitakkavicāre"))))
seg("1-1400", qa("avitakkavicāramattā",
                 J(f"{RJ2P} {KVK}", J(f"{LJ2P} {KV}", trailer=ex("vicāraṃ")), "и направленная мысль")))
VIC_UPP = (f"удержание мысли, возникшее во втором медитативном погружении {S.spell('Sī.', 'dutiyajjhāne')} "
           "по пятеричному методу")
note("pañcakanaye dutiye jhāne uppanno ca vicāro", VIC_UPP.replace(" " + S.spell('Sī.', 'dutiyajjhāne'), ""))
seg("1-1401", qa("avitakkaavicārā", J(DVP, rj("tikatika", KVK), f"{ARUPPA4} {KVK}", lj("tikatika", KV), VIC_UPP, RN))
    + " Удержание мысли, возникшее вместе с направленной мыслью, нельзя определить "
    + nvs("savitakkasavicārā", "avitakkavicāramattā", "avitakkaavicārā") + ".")
seg("1-1402", qa("pītisahagatā", J(kkv("cattāro", "сопровождаемых радостью"), akv("cattāro"), kkvip("pañca"),
                                   kir("pañca"), rj("dukatika", KVK), lj("dukatika", KV), trailer=ex("pītiṃ"))))
seg("1-1403", qa("sukhasahagatā", J(kkv("cattāro", "сопровождаемых радостью"), akv("cattāro"), kkvip("cha"),
                                    kir("pañca"), rj("tikacatukka", KVK), lj("tikacatukka", KV), trailer=ex("sukhaṃ"))))
UPEKKHA_BODY = J(*UPEKKHA_SET, f"{ARUPPA4} {KVK}", f"{LJ4} {KV}", trailer=ex("upekkhaṃ"))
PITI_SUKHA = ("Восторг не сопровождается восторгом, сопровождается счастьем, не сопровождается невозмутимостью. "
              "Счастье не сопровождается счастьем, иногда сопровождается восторгом, не сопровождается "
              f"невозмутимостью, иногда его нельзя определить {nvs('pītisahagatā')}.")
note("Pīti na pītisahagatā, sukhasahagatā, na upekkhāsahagatā. Sukhaṃ na sukhasahagataṃ, siyā pītisahagataṃ, …",
     PITI_SUKHA)
NV_PSU = NV_ALL.format(nvn("pītisahagatā", "sukhasahagatā", "upekkhāsahagatā"))
seg("1-1404", qa("upekkhāsahagatā", UPEKKHA_BODY) + " " + PITI_SUKHA + " "
    + ans(J(DOM2, DUKKHA_KV, UPEKKHA_V, RN), NV_PSU))
seg("1-1405", qa("dassanena pahātabbā", J(DS4, CU_V)))
seg("1-1406", qa("bhāvanāya pahātabbā", CU_U) + " "
    + ans(J(DV4, DOM2), siya("dassanena pahātabbā", "bhāvanāya pahātabbā")))
REST_KVK4 = [K4, V4, KR3, RN]
seg("1-1407", qa("neva dassanena na bhāvanāya pahātabbā", J(*REST_KVK4)))
seg("1-1408", qa("dassanena pahātabbahetukā", J(DS4, CU_V, trailer=ex("mohaṃ"))))
seg("1-1409", qa("bhāvanāya pahātabbahetukā", J(CU_U, trailer=ex("mohaṃ"))) + " "
    + ans(J(DV4, DOM2), siya("dassanena pahātabbahetukā", "bhāvanāya pahātabbahetukā")))
seg("1-1410", qa("neva dassanena na bhāvanāya pahātabbahetukā", J(MOHA_V, MOHA_U, *REST_KVK4)))
seg("1-1411", qa("ācayagāmino", f"{K3} и {AK}"))
seg("1-1413", qa("nevācayagāmināpacayagāmino", J(V4, KR3, RN)))
seg("1-1415", qa("asekkhā", "Высший плод состояния архата"))
REST_3 = [K3, AK, V3, KR3]
seg("1-1416", qa("nevasekkhanāsekkhā", J(*REST_3, RN)))
KAMA_SET = [KK, AK, KV_ALL, KKR, SABBA_R]
seg("1-1417", qa("parittā", J(*KAMA_SET)))
seg("1-1418", qa("mahaggatā", "Относящиеся к миру форм и к миру без форм благие и этически неопределённые явления"))
seg("1-1419", qa("appamāṇā", LOK3))
seg("1-1420", qa("parittārammaṇā", J(KV_ALL, KMD, KAHM_S)))
seg("1-1421", qa("mahaggatārammaṇā", VN_NEVA))
SIYA_PM = (siya("parittārammaṇā", "mahaggatārammaṇā") + f", но не {N['appamāṇārammaṇā']}, иногда "
           + NV_THEM.format(nvn("parittārammaṇā", "mahaggatārammaṇā")))
SIYA_PMA = (siya("parittārammaṇā", "mahaggatārammaṇā", "appamāṇārammaṇā") + ", иногда "
            + NV_THEM.format(nvn("parittārammaṇā", "mahaggatārammaṇā", "appamāṇārammaṇā")))
ANARAMMANA = f"{cap(RN)} не имеют объекта."
note("Rūpañca nibbānañca anārammaṇā.", ANARAMMANA)
RUPA_JH = [rj("tikacatukka", KVK), J4VIP]
seg("1-1422", qa("appamāṇārammaṇā", LOK2) + " "
    + ans(J(kkv("cattāro", "не связанных со знанием"), kirq("cattāro", "не связанных со знанием"), SABBAK), SIYA_PM)
    + " " + ans(J(kkv("cattāro", "связанных со знанием"), kirq("cattāro", "связанных со знанием"), f"{RJ4} {KKI}",
                  KAHM_U), SIYA_PMA)
    + " " + ans(J(*RUPA_JH, SPH["ākāsānañcāyatanaṃ"], SPH["ākiñcaññāyatanaṃ"]),
                NV_ALL.format(nvn("parittārammaṇā", "mahaggatārammaṇā", "appamāṇārammaṇā")))
    + " " + ANARAMMANA)
seg("1-1423", qa("hīnā", AK12))
seg("1-1424", qa("majjhimā", J(K3, V3, KR3, SABBA_R)))
seg("1-1425", qa("paṇītā", LOK3))
seg("1-1426", f"{Q('micchattaniyatā')} " + ans(J(DS4, DOM2), siya("micchattaniyatā", "aniyatā")))
ANIYATA_BODY = J(DV4, CU_V, CU_U, K3, V4, KR3, RN)
seg("1-1428", qa("aniyatā", ANIYATA_BODY))
MR, MH, MA = "maggārammaṇā", "maggahetukā", "maggādhipatino"
seg("1-1429", f"{Q(MR)} "
    + ans(J(kkv("cattāro", "связанных со знанием"), kirq("cattāro", "связанных со знанием")),
          f"иногда {N[MR]}, но не {N[MH]}; иногда {N[MA]}, иногда " + NV_THEM.format(nvn(MR, MA)))
    + " Четыре благородных пути не имеют объектом путь, имеют корнем путь; иногда находятся под главенством пути, "
      "иногда " + NV_THEM.format(nvn(MA)) + "."
    + " " + ans(J(f"{RJ4} {KKI}", KAHM_U),
                f"иногда {N[MR]}; не {N[MH]}, и не {N[MA]}; иногда " + NV_THEM.format(nvn(MR)))
    + " " + ans(J(kkv("cattāro", "не связанных со знанием"), SABBAK, KV_ALL, kir("cha", True), *RUPA_JH,
                  f"{ARUPPA4} {KVK}", FRUITS4), NV_ALL.format(nvn(MR, MH, MA)))
    + " " + ANARAMMANA)
note("Cattāro ariyamaggā na maggārammaṇā, maggahetukā; siyā maggādhipatino, …",
     "Четыре благородных пути не имеют объектом путь, имеют корнем путь; иногда находятся под главенством пути, …")
seg("1-1430", f"{Q('uppannā')} "
    + ans(f"{cap(V4)}, {F.YANCA_KAMMA}" + OPEN,
          siya("uppannā", "uppādino") + "; " + NV_THEM.format(nvn("anuppannā")))
    + " " + ans(f"{K4}, {AK}, {KR3}, {F.YANCA_NA_KAMMA}" + OPEN,
                siya("uppannā", "anuppannā") + "; " + NV_THEM.format(nvn("uppādino")))
    + " Нирвану нельзя определить " + nvs("uppannā", "anuppannā", "uppādino") + ".")
seg("1-1431", "Кроме нирваны, все явления " + ", ".join(f"иногда являются {INS[p]}" if i == 0 else f"иногда {INS[p]}"
                                                         for i, p in enumerate(("atītā", "anāgatā", "paccuppannā")))
    + ". Нирвану нельзя определить " + nvs("atītā", "anāgatā", "paccuppannā") + ".")
seg("1-1432", qa("atītārammaṇā", VN_NEVA))
seg("1-1433", f"Явлений, которые непременно являются явлениями с будущим объектом, нет.")
note("Niyogā anāgatārammaṇā natthi.", R["1-1433"][0])
SIYA_3T = siya("atītārammaṇā", "anāgatārammaṇā", "paccuppannārammaṇā")
NV_3T = nvn("atītārammaṇā", "anāgatārammaṇā", "paccuppannārammaṇā")
seg("1-1434", qa("paccuppannārammaṇā", f"{DVP} и {MD3}") + " "
    + ans(J(kkvip("dasa", True), AKV_MVD_U, KAHM_S), SIYA_3T)
    + " " + ans(J(KK, AK, kir("nava", True), f"{RJ4} {KKI}"), SIYA_3T + "; иногда " + NV_THEM.format(NV_3T))
    + " " + ans(J(*RUPA_JH, SPH["ākāsānañcāyatanaṃ"], SPH["ākiñcaññāyatanaṃ"], PATHS4, FRUITS4),
                NV_ALL.format(NV_3T))
    + " " + ANARAMMANA)
ANINDRIYA = "материальной формы, не связанной с органами чувств"
seg("1-1435", f"Кроме {ANINDRIYA}, и нирваны, все явления "
    + ", ".join(f"иногда являются {INS[p]}" if i == 0 else f"иногда {INS[p]}"
                for i, p in enumerate(("ajjhattā", "bahiddhā", "ajjhattabahiddhā")))
    + ". И материальная форма, не связанная с органами чувств, и нирвана являются внешними явлениями.")
note("Anindriyabaddharūpañca nibbānañca", "и материальная форма, не связанная с органами чувств, и нирвана")
seg("1-1436", qa("ajjhattārammaṇā", VN_NEVA))
seg("1-1437", qa("bahiddhārammaṇā", J(*RUPA_JH, SPH["ākāsānañcāyatanaṃ"], f"{PATHS4[:-1]}, и {FRUITS4}")) + " "
    + ans(f"Кроме материальной формы, все без исключения {F.KAA}, относящиеся к миру чувственных желаний, и {RJ4} {KKI}",
          siya("ajjhattārammaṇā", "bahiddhārammaṇā", "ajjhattabahiddhārammaṇā"))
    + " Сферу отсутствия чего-либо нельзя определить "
    + nvs("ajjhattārammaṇā", "bahiddhārammaṇā", "ajjhattabahiddhārammaṇā") + ". " + ANARAMMANA)
seg("1-1439", qa("anidassanasappaṭighā", F.SENSE_PE))
ANID_BODY = f"{K4}, {AK}, {V4}, {KR3}, {F.YANCA_ANID}, {NIB}"
seg("1-1440", qa("anidassanaappaṭighā", ANID_BODY), EXACT["Tikaṃ."])

# ---------------------------------------------------------------- the root group
HK = "отсутствие жадности как благой корень и отсутствие злобы как благой корень"
seg("1-1441",
    f"{Q('hetū')} {F.THREE_ROOTS}. {cap(HK)} возникают в благом уме четырёх миров. Отсутствие заблуждения как благой "
    "корень возникает в благом уме четырёх миров, кроме четырёх видов благого ума, относящегося к миру чувственных "
    "желаний, не связанных со знанием.",
    f"Жадность возникает {IN['lobha8']}. Злоба возникает {IN['domanassa2']}. Заблуждение возникает {IN['all']}.",
    "Отсутствие жадности как корень, являющийся результатом действий, и отсутствие злобы как корень, являющийся "
    f"результатом действий, возникают в результатах действий четырёх миров, {EXC_RES}. Отсутствие заблуждения как "
    f"корень, являющийся результатом действий, возникает в результатах действий четырёх миров, {EXC_RES} и кроме "
    "четырёх видов ума, не связанных со знанием.",
    "Отсутствие жадности как функциональный корень и отсутствие злобы как функциональный корень возникают в "
    f"функциональном уме трёх миров, {EXC_KIR}. Отсутствие заблуждения как функциональный корень возникает в "
    f"функциональном уме трёх миров, {EXC_KIR} и кроме четырёх видов ума, не связанных со знанием, – "
    + S.a_form(N["hetū"]))
note("Alobho kusalahetu, adoso kusalahetu, catūsu bhūmīsu kusalesu uppajjanti.",
     f"{cap(HK)} возникают в благом уме четырёх миров.")
note("X vipākahetu / kiriyahetu", "X как корень, являющийся результатом действий / X как функциональный корень")
note("catūsu bhūmīsu vipākesu / tīsu bhūmīsu kiriyesu", "в результатах действий четырёх миров / в функциональном "
     "уме трёх миров")
seg("1-1442", qa("na hetū", f"Кроме корней, {J(*REST_KVK4[:1], AK, *REST_KVK4[1:])}"))
SAHETUKA = J(cap(REST_MU), K4, V4_EXC, KR3_EXC)
AHETUKA = J(MOHA_V, MOHA_U, DVP, MD3, AHM5, RN)
seg("1-1443", qa("sahetukā", SAHETUKA))
seg("1-1444", qa("ahetukā", AHETUKA))
seg("1-1445", qa("hetusampayuttā", SAHETUKA))
seg("1-1446", qa("hetuvippayuttā", AHETUKA))
TOGETHER = "Там, где {} возникают вместе" + OPEN                # Yattha … ekato uppajjanti
note("Yattha dve tayo hetū ekato uppajjanti – ime dhammā …", "Там, где два или три корня возникают вместе, – это …")
seg("1-1447", qa("hetū ceva sahetukā ca", TOGETHER.format("два или три корня")))
SAHET_EX = J(K4, AK, V4_EXC, KR3_EXC, trailer=ex("hetū"))
seg("1-1448", qa("sahetukā ceva na ca hetū", SAHET_EX) + " "
    + NV_SUBJ.format(cap(N["ahetukā"]), nvn("hetū ceva sahetukā ca", "sahetukā ceva na ca hetū")))
seg("1-1449", qa("hetū ceva hetusampayuttā ca", TOGETHER.format("два или три корня")))
seg("1-1450", qa("hetusampayuttā ceva na ca hetū", SAHET_EX) + " "
    + NV_SUBJ.format(cap(N["hetuvippayuttā"]), nvn("hetū ceva hetusampayuttā ca", "hetusampayuttā ceva na ca hetū")))
seg("1-1451", qa("na hetū sahetukā", SAHET_EX))
seg("1-1452", qa("na hetū ahetukā", J(DVP, MD3, AHM5, RN)) + " "
    + NV_SUBJ.format(cap(N["hetū"]), nvn("na hetū sahetukā", "na hetū ahetukā")))

# ---------------------------------------------------------------- the short intermediate pairs
ALL4_SABBA = J(K4, AK, V4, KR3, SABBA_R)
seg("1-1453", qa("sappaccayā", ALL4_SABBA))
seg("1-1454", qa("appaccayā", "Нирвана"))
seg("1-1455", qa("saṅkhatā", ALL4_SABBA))
seg("1-1456", qa("asaṅkhatā", "Нирвана"))
seg("1-1458", qa("anidassanā", f"{F.SENSE_PE}, {low(ANID_BODY)}"))
seg("1-1460", qa("appaṭighā", ANID_BODY))
seg("1-1461", qa("rūpino", F.FOUR_GREAT + OPEN))
assert F.R["1-1097"][0] == qa("rūpino", F.FOUR_GREAT + OPEN)
seg("1-1462", qa("arūpino", J(K4, AK, V4, KR3, NIB)))
ALL3_SABBA = J(K3, AK, V3, KR3, SABBA_R)
seg("1-1463", qa("lokiyā", ALL3_SABBA))
seg("1-1464", qa("lokuttarā", LOK3) + f" Все {S.reading('Syā.', 'sabbeva')} явления познаваемы тем или иным видом "
    "сознания и не познаваемы тем или иным видом сознания.")
note("Sabbe dhammā kenaci viññeyyā, kenaci na viññeyyā.",
     "Все явления познаваемы тем или иным видом сознания и не познаваемы тем или иным видом сознания.")

# ---------------------------------------------------------------- the defilement groups
REST4_RN = [K4, V4, KR3, RN]
REST3_SABBA = [K3, V3, KR3, SABBA_R]


def same(name, plural):
    return G.same_as(name, plural)


def nv_pair(subj, a, b):
    return NV_SUBJ.format(cap(N[subj]), nvn(a, b))


AS = F.ASAVA
seg("1-1465", f"{Q('āsavā')} Четыре влечения – {F.AS4}. "
    f"{cap(AS['kāmāsavo'][0])} возникает {IN['lobha8']}; {AS['bhavāsavo'][0]} возникает {IN['dv4']}; "
    f"{AS['diṭṭhāsavo'][0]} возникает {IN['ds4']}. {cap(AS['avijjāsavo'][0])} возникает {IN['all']} – "
    + S.a_form(N["āsavā"]))
assert F.R["1-1102"][0] == f"{Q('āsavā')} Четыре влечения – {F.AS4}."
seg("1-1466", qa("no āsavā", J(cap(rest("āsave")), *REST4_RN)))
seg("1-1467", qa("sāsavā", ALL3_SABBA))
seg("1-1468", qa("anāsavā", LOK3))
seg("1-1469", qa("āsavasampayuttā", f"{cap(plain(DOM2))}, {ex('mohaṃ')}; {REST_MU}"))
seg("1-1470", qa("āsavavippayuttā", J(MOHA_D, MOHA_V, MOHA_U, *REST4_RN)))
seg("1-1471", same("āsavā ceva sāsavā ca", "влечения"))
assert F.R["1-1112"][0] == R["1-1471"][0]
seg("1-1472", qa("sāsavā ceva no ca āsavā", J(cap(rest("āsave")), *REST3_SABBA)) + " "
    + nv_pair("anāsavā", "āsavā ceva sāsavā ca", "sāsavā ceva no ca āsavā"))
seg("1-1473", qa("āsavā ceva āsavasampayuttā ca", TOGETHER.format("два или три влечения")))
seg("1-1474", qa("āsavasampayuttā ceva no ca āsavā", rest("āsave")) + " "
    + nv_pair("āsavavippayuttā", "āsavā ceva āsavasampayuttā ca", "āsavasampayuttā ceva no ca āsavā"))
seg("1-1475", qa("āsavavippayuttā sāsavā", J(MOHA_D, MOHA_V, MOHA_U, *REST3_SABBA)))
seg("1-1476", qa("āsavavippayuttā anāsavā", LOK3) + " "
    + nv_pair("āsavasampayuttā", "āsavavippayuttā sāsavā", "āsavavippayuttā anāsavā"))

SM = {k: v[0] for k, v in F.SAMY.items()}
seg("1-1477", f"{Q('saṃyojanā')} Десять оков – {', '.join(SM[k] for k in F.SAMY10)}. "
    f"{cap(SM['kāmarāga'])} возникают {IN['lobha8']}. {cap(SM['paṭigha'])} возникают {IN['domanassa2']}. "
    f"{cap(SM['māna'])} возникают {IN['dv4']}. {cap(SM['diṭṭhi'])} возникают {IN['ds4']}. "
    f"{cap(SM['vicikicchā'])} возникают {IN['vic']}. {cap(SM['sīlabbataparāmāsa'])} возникают {IN['ds4']}. "
    f"{cap(SM['bhavarāga'])} возникают {IN['dv4']}. {cap(SM['issā'])} и {SM['macchariya']} возникают "
    f"{IN['domanassa2']}. {cap(SM['avijjā'])} возникают {IN['all']} – " + S.a_form(N["saṃyojanā"]))
assert F.R["1-1118"][0] == f"{Q('saṃyojanā')} Десять оков – {', '.join(SM[k] for k in F.SAMY10)}."
seg("1-1478", f"{S.q_form(N['no saṃyojanā'])[:-1]}. " + tail(J(cap(rest("saṃyojane")), *REST4_RN))
    + S.a_form(N["no saṃyojanā"]))
seg("1-1479", qa("saṃyojaniyā", ALL3_SABBA))
seg("1-1480", qa("asaṃyojaniyā", LOK3))
seg("1-1481", qa("saṃyojanasampayuttā", cap(REST_U)))
seg("1-1482", qa("saṃyojanavippayuttā", J(MOHA_U, *REST4_RN)))
seg("1-1484", qa("saṃyojaniyā ceva no ca saṃyojanā", J(cap(rest("saṃyojane")), *REST3_SABBA)) + " "
    + nv_pair("asaṃyojaniyā", "saṃyojanā ceva saṃyojaniyā ca", "saṃyojaniyā ceva no ca saṃyojanā"))
seg("1-1485", qa("saṃyojanā ceva saṃyojanasampayuttā ca", TOGETHER.format("двое или трое оков")))
seg("1-1486", qa("saṃyojanasampayuttā ceva no ca saṃyojanā", rest("saṃyojane")) + " "
    + nv_pair("saṃyojanavippayuttā", "saṃyojanā ceva saṃyojanasampayuttā ca", "saṃyojanasampayuttā ceva no ca saṃyojanā"))
seg("1-1487", qa("saṃyojanavippayuttā saṃyojaniyā", J(MOHA_U, *REST3_SABBA)))
seg("1-1488", qa("saṃyojanavippayuttā asaṃyojaniyā", LOK3) + " "
    + nv_pair("saṃyojanasampayuttā", "saṃyojanavippayuttā saṃyojaniyā", "saṃyojanavippayuttā asaṃyojaniyā"))

GN = {k: v[0] for k, v in F.GAN.items()}
seg("1-1489", f"{Q('ganthā')} Четыре узы – {', '.join(GN[k] for k in F.GAN4)}. "
    f"{cap(GN['abhijjhā'])} возникают {IN['lobha8']}. {cap(GN['byāpādo'])} возникают {IN['domanassa2']}. "
    f"{cap(GN['sīlabbataparāmāso'])} и {GN['idaṃsaccābhiniveso']} возникают {IN['ds4']}, – "
    + S.a_form(N["ganthā"]))
assert F.R["1-1140"][0] == f"{Q('ganthā')} Четыре узы – {', '.join(GN[k] for k in F.GAN4)}."
seg("1-1490", qa("no ganthā", J(cap(rest("ganthe")), *REST4_RN)))
seg("1-1491", qa("ganthaniyā", ALL3_SABBA))
seg("1-1492", qa("aganthaniyā", LOK3))
seg("1-1493", qa("ganthasampayuttā", f"{cap(plain(DS4))}; {plain(DV4)}, {ex('lobhaṃ')}; {plain(DOM2)}, "
                                     f"{ex('paṭighaṃ')}" + OPEN))
GAN_DISS = [LOBHA_DV, PATIGHA_D, CU_V, CU_U]
seg("1-1494", qa("ganthavippayuttā", J(*GAN_DISS, *REST4_RN)))
seg("1-1496", qa("ganthaniyā ceva no ca ganthā", J(cap(rest("ganthe")), *REST3_SABBA)) + " "
    + nv_pair("aganthaniyā", "ganthā ceva ganthaniyā ca", "ganthaniyā ceva no ca ganthā"))
seg("1-1497", qa("ganthā ceva ganthasampayuttā ca", TOGETHER.format("воззрение и жадность")))
seg("1-1498", qa("ganthasampayuttā ceva no ca ganthā", J(LOB8, DOM2, trailer=ex("ganthe"))) + " "
    + nv_pair("ganthavippayuttā", "ganthā ceva ganthasampayuttā ca", "ganthasampayuttā ceva no ca ganthā"))
seg("1-1499", qa("ganthavippayuttā ganthaniyā", J(*GAN_DISS, *REST3_SABBA)))
seg("1-1500", qa("ganthavippayuttā aganthaniyā", LOK3) + " "
    + nv_pair("ganthasampayuttā", "ganthavippayuttā ganthaniyā", "ganthavippayuttā aganthaniyā"))

seg("1-1501", f"Что такое {N['oghā']}{ELL}.")
seg("1-1502", f"Что такое {N['yogā']}{ELL}.")

NV6 = {k: v[0] for k, v in G.NIV.items()}
seg("1-1503", f"{Q('nīvaraṇā')} Шесть помех – {', '.join(NV6[k] for k in G.NIV6)}. "
    f"{cap(NV6['kāmacchanda'])} возникает {IN['lobha8']}; {NV6['byāpāda']} возникает {IN['domanassa2']}; "
    f"{NV6['thinamiddha']} возникает {IN['sas']}; {NV6['uddhacca']} возникает {IN['udd']}; "
    f"{NV6['kukkucca']} возникает {IN['domanassa2']}; {NV6['vicikicchā']} возникает {IN['vic']}; "
    f"{NV6['avijjā']} возникает {IN['all']} – " + S.a_form(N["nīvaraṇā"]))
seg("1-1504", qa("no nīvaraṇā", J(cap(rest("nīvaraṇe")), *REST4_RN)))
seg("1-1505", qa("nīvaraṇiyā", ALL3_SABBA))
seg("1-1506", qa("anīvaraṇiyā", LOK3))
seg("1-1507", qa("nīvaraṇasampayuttā", AK12))
seg("1-1508", qa("nīvaraṇavippayuttā", J(*REST4_RN)))
seg("1-1510", qa("nīvaraṇiyā ceva no ca nīvaraṇā", J(cap(rest("nīvaraṇe")), *REST3_SABBA)) + " "
    + nv_pair("anīvaraṇiyā", "nīvaraṇā ceva nīvaraṇiyā ca", "nīvaraṇiyā ceva no ca nīvaraṇā"))
seg("1-1511", qa("nīvaraṇā ceva nīvaraṇasampayuttā ca", TOGETHER.format("две или три помехи")))
seg("1-1512", qa("nīvaraṇasampayuttā ceva no ca nīvaraṇā", rest("nīvaraṇe")) + " "
    + nv_pair("nīvaraṇavippayuttā", "nīvaraṇā ceva nīvaraṇasampayuttā ca", "nīvaraṇasampayuttā ceva no ca nīvaraṇā"))
seg("1-1513", qa("nīvaraṇavippayuttā nīvaraṇiyā", J(*REST3_SABBA)))
seg("1-1514", qa("nīvaraṇavippayuttā anīvaraṇiyā", LOK3) + " "
    + nv_pair("nīvaraṇasampayuttā", "nīvaraṇavippayuttā nīvaraṇiyā", "nīvaraṇavippayuttā anīvaraṇiyā"))

seg("1-1515", f"{Q('parāmāsā')} {cap(G.PARAMASA[0])} возникает {IN['ds4']}, – " + S.a_form(N["parāmāsā"]))
seg("1-1516", qa("no parāmāsā", J(cap(rest("parāmāsaṃ")), *REST4_RN)))
seg("1-1517", qa("parāmaṭṭhā", ALL3_SABBA))
seg("1-1518", qa("aparāmaṭṭhā", LOK3))
seg("1-1519", qa("parāmāsasampayuttā", J(DS4, trailer=ex("parāmāsaṃ"))))
PAR_DISS = [DV4, DOM2, CU_V, CU_U]
seg("1-1520", qa("parāmāsavippayuttā", J(*PAR_DISS, *REST4_RN))
    + " Искажение нельзя определить – ни как связанное с искажениями, ни как не связанное с искажениями.")
note("Parāmāso na vattabbo – parāmāsasampayuttotipi, parāmāsavippayuttotipi.",
     "Искажение нельзя определить – ни как связанное с искажениями, ни как не связанное с искажениями.")
seg("1-1521", f"{Q('parāmāsā ceva parāmaṭṭhā ca')} {G.PARAMASA_SAME}")
seg("1-1522", qa("parāmaṭṭhā ceva no ca parāmāsā", J(cap(rest("parāmāsaṃ")), *REST3_SABBA)) + " "
    + nv_pair("aparāmaṭṭhā", "parāmāsā ceva parāmaṭṭhā ca", "parāmaṭṭhā ceva no ca parāmāsā"))
seg("1-1523", qa("parāmāsavippayuttā parāmaṭṭhā", J(*PAR_DISS, *REST3_SABBA)))
seg("1-1524", qa("parāmāsavippayuttā aparāmaṭṭhā", LOK3) + " "
    + NV_SUBJ.format(f"{cap(N['parāmāsā'])}, и {N['parāmāsasampayuttā']}",
                     nvn("parāmāsavippayuttā parāmaṭṭhā", "parāmāsavippayuttā aparāmaṭṭhā")))

# ---------------------------------------------------------------- the great intermediate pairs
seg("1-1525", qa("sārammaṇā", f"{K4}, {AK}, {V4} и {KR3}"))
seg("1-1526", qa("anārammaṇā", cap(RN)))
CET3 = ", ".join(G.CET3_ITEMS)
seg("1-1528", qa("no cittā", f"{cap(CET3)}, {RN}"))
CITTA_RN = f"И ум, {RN}"
CITTA_REST_N = "И ум, и остальная материальная форма, и нирвана"
assert G.CITTA_REST == "И ум, и остальная материальная форма, и необусловленный элемент"
seg("1-1530", qa("acetasikā", CITTA_RN))
seg("1-1532", qa("cittavippayuttā", cap(RN)) + " " + G.NOT_SAY.format("связанный"))
seg("1-1534", qa("cittavisaṃsaṭṭhā", cap(RN)) + " " + G.NOT_SAY.format("соединённый"))
seg("1-1535", qa("cittasamuṭṭhānā", f"{cap(CET3)}, {G.VINNATTI2}, {G.CITTAJA_CLAUSE}, – {G.CITTAJA_ITEMS}"))
seg("1-1536", qa("no cittasamuṭṭhānā", CITTA_REST_N))
seg("1-1538", qa("no cittasahabhuno", CITTA_REST_N))
seg("1-1540", qa("no cittānuparivattino", CITTA_REST_N))
seg("1-1542", qa("no cittasaṃsaṭṭhasamuṭṭhānā", CITTA_RN))
seg("1-1544", qa("no cittasaṃsaṭṭhasamuṭṭhānasahabhuno", CITTA_RN))
seg("1-1546", qa("no cittasaṃsaṭṭhasamuṭṭhānānuparivattino", CITTA_RN))
seg("1-1550", qa("no upādā", f"{K4}, {AK}, {V4}, {KR3}, и четыре великих элемента, и нирвана"))
seg("1-1551", qa("upādiṇṇā", f"{V3}, {F.YANCA_KAMMA}" + OPEN))
seg("1-1552", qa("anupādiṇṇā", f"{K3}, {AK}, {KR3}, {F.YANCA_NA_KAMMA}; {low(LOK3)}"))

# ---------------------------------------------------------------- clinging
UP = {k: v[0] for k, v in G.UPA.items()}
seg("1-1553", f"{Q('upādānā')} Четыре цепляния – {', '.join(UP[k] for k in G.UPA4)}. "
    f"{cap(UP['kām'])} возникает {IN['lobha8']}. {cap(UP['diṭṭh'])}, {UP['sīlabbat']} и {UP['attavād']} "
    f"возникают {IN['ds4']}, – " + S.a_form(N["upādānā"]))
seg("1-1554", qa("no upādānā", J(cap(rest("upādāne")), *REST4_RN)))
seg("1-1555", qa("upādāniyā", ALL3_SABBA))
seg("1-1556", qa("anupādāniyā", LOK3))
seg("1-1557", qa("upādānasampayuttā", J(DSL4, DV4, trailer=ex("lobhaṃ"))))
UPA_DISS = [LOBHA_DV, DOM2, CU_V, CU_U]
seg("1-1558", qa("upādānavippayuttā", J(*UPA_DISS, *REST4_RN)))
seg("1-1560", qa("upādāniyā ceva no ca upādānā", J(cap(rest("upādāne")), *REST3_SABBA)) + " "
    + nv_pair("anupādāniyā", "upādānā ceva upādāniyā ca", "upādāniyā ceva no ca upādānā"))
seg("1-1561", qa("upādānā ceva upādānasampayuttā ca", TOGETHER.format("воззрение и жадность")))
seg("1-1562", qa("upādānasampayuttā ceva no ca upādānā", J(LOB8, trailer=ex("upādāne"))) + " "
    + nv_pair("upādānavippayuttā", "upādānā ceva upādānasampayuttā ca", "upādānasampayuttā ceva no ca upādānā"))
seg("1-1563", qa("upādānavippayuttā upādāniyā", J(*UPA_DISS, *REST3_SABBA)))
seg("1-1564", qa("upādānavippayuttā anupādāniyā", LOK3) + " "
    + nv_pair("upādānasampayuttā", "upādānavippayuttā upādāniyā", "upādānavippayuttā anupādāniyā"))

# ---------------------------------------------------------------- defilements
KL = dict(zip(["lobho", "doso", "moho", "māno", "diṭṭhi", "vicikicchā", "thinaṃ", "uddhaccaṃ", "ahirikaṃ",
               "anottappaṃ"], G.KIL10))
seg("1-1565", f"{Q('kilesā')} Десять основ омрачений – {', '.join(G.KIL10)}. "
    f"{cap(KL['lobho'])} возникает {IN['lobha8']}. {cap(KL['doso'])} возникает {IN['domanassa2']}. "
    f"{cap(KL['moho'])} возникает {IN['all']}. {cap(KL['māno'])} возникает {IN['dv4']}. "
    f"{cap(KL['diṭṭhi'])} возникает {IN['ds4']}. {cap(KL['vicikicchā'])} возникает {IN['vic']}. "
    f"{cap(KL['thinaṃ'])} возникает {IN['sas']}. {cap(KL['uddhaccaṃ'])}, {KL['ahirikaṃ']} и {KL['anottappaṃ']} "
    f"возникают {IN['all']} – " + S.a_form(N["kilesā"]))
seg("1-1566", qa("no kilesā", J(cap(rest("kilese")), *REST4_RN)))
seg("1-1567", qa("saṃkilesikā", ALL3_SABBA))
seg("1-1568", qa("asaṃkilesikā", LOK3))
seg("1-1569", qa("saṃkiliṭṭhā", AK12))
seg("1-1570", qa("asaṃkiliṭṭhā", J(*REST4_RN)))
seg("1-1571", qa("kilesasampayuttā", AK12))
seg("1-1572", qa("kilesavippayuttā", J(*REST4_RN)))
seg("1-1574", qa("saṃkilesikā ceva no ca kilesā", J(cap(rest("kilese")), *REST3_SABBA)) + " "
    + nv_pair("asaṃkilesikā", "kilesā ceva saṃkilesikā ca", "saṃkilesikā ceva no ca kilesā"))
seg("1-1576", qa("saṃkiliṭṭhā ceva no ca kilesā", rest("kilese")) + " "
    + nv_pair("asaṃkiliṭṭhā", "kilesā ceva saṃkiliṭṭhā ca", "saṃkiliṭṭhā ceva no ca kilesā"))
seg("1-1577", qa("kilesā ceva kilesasampayuttā ca", TOGETHER.format("два или три омрачения")))
seg("1-1578", qa("kilesasampayuttā ceva no ca kilesā", rest("kilese")) + " "
    + nv_pair("kilesavippayuttā", "kilesā ceva kilesasampayuttā ca", "kilesasampayuttā ceva no ca kilesā"))
seg("1-1579", qa("kilesavippayuttā saṃkilesikā", J(*REST3_SABBA)))
seg("1-1580", qa("kilesavippayuttā asaṃkilesikā", LOK3) + " "
    + nv_pair("kilesasampayuttā", "kilesavippayuttā saṃkilesikā", "kilesavippayuttā asaṃkilesikā"))

# ---------------------------------------------------------------- the closing pairs
seg("1-1581", qa("dassanena pahātabbā", J(DS4, CU_V)) + " "
    + ans(J(DV4, DOM2), siya("dassanena pahātabbā", "na dassanena pahātabbā")))
seg("1-1582", qa("na dassanena pahātabbā", J(CU_U, *REST4_RN)))
seg("1-1583", qa("bhāvanāya pahātabbā", CU_U) + " "
    + ans(J(DV4, DOM2), siya("bhāvanāya pahātabbā", "na bhāvanāya pahātabbā")))
seg("1-1584", qa("na bhāvanāya pahātabbā", J(DS4, CU_V, *REST4_RN)))
seg("1-1585", qa("dassanena pahātabbahetukā", J(DS4, CU_V, trailer=ex("mohaṃ"))) + " "
    + ans(J(DV4, DOM2), siya("dassanena pahātabbahetukā", "na dassanena pahātabbahetukā")))
seg("1-1586", qa("na dassanena pahātabbahetukā", J(MOHA_V, CU_U, *REST4_RN)))
seg("1-1587", qa("bhāvanāya pahātabbahetukā", J(CU_U, trailer=ex("mohaṃ"))) + " "
    + ans(J(DV4, DOM2), siya("bhāvanāya pahātabbahetukā", "na bhāvanāya pahātabbahetukā")))
seg("1-1588", qa("na bhāvanāya pahātabbahetukā", J(DS4, CU_V, MOHA_U, *REST4_RN)))
seg("1-1589", qa("savitakkā", J(*SAVITAKKA_SET, f"{RJ1} {KVK}", f"{LJ1} {KV}", trailer=ex("vitakkaṃ"))))
seg("1-1590", qa("avitakkā", J(DVP, rj("tikacatukka", KVK), f"{ARUPA4} {KVK}", lj("tikacatukka", KV),
                               "направленная мысль", RN)))
seg("1-1591", qa("savicārā", J(*SAVITAKKA_SET, rj("ekakaduka", KVK), lj("ekakaduka", KV), trailer=ex("vicāraṃ"))))
seg("1-1592", qa("avicārā", J(DVP, rj("tikatika", KVK), f"{ARUPPA4} {KVK}", lj("tikatika", KV), "удержание мысли",
                              RN)))
PITI_BODY = J(kkv("cattāro", "сопровождаемых радостью"), akv("cattāro"), kkvip("pañca"), kir("pañca"),
              rj("dukatika", KVK), lj("dukatika", KV), trailer=ex("pītiṃ"))
assert qa("pītisahagatā", PITI_BODY) == R["1-1402"][0]
seg("1-1593", qa("sappītikā", PITI_BODY))
APITI_BODY = J(kkv("cattāro", "сопровождаемых невозмутимостью"), akv("aṭṭha"), kkvip("ekādasa"), akvip("satta"),
               kir("cha"), rj("dukaduka", KVK), f"{ARUPPA4} {KVK}", lj("dukaduka", KV), "восторг", RN)
seg("1-1594", qa("appītikā", APITI_BODY))
seg("1-1595", qa("pītisahagatā", PITI_BODY))
seg("1-1596", qa("na pītisahagatā", APITI_BODY))
seg("1-1597", R["1-1403"][0])
seg("1-1598", qa("na sukhasahagatā", J(kkv("cattāro", "сопровождаемых невозмутимостью"), akv("aṭṭha"), kkvip("dasa"),
                                       akvip("satta"), kir("cha"), f"{RJ4} {KVK}", f"{ARUPPA4} {KVK}", f"{LJ4} {KV}",
                                       "счастье", RN)))
seg("1-1599", qa("upekkhāsahagatā", UPEKKHA_BODY))
seg("1-1600", qa("na upekkhāsahagatā", J(kkv("cattāro", "сопровождаемых радостью"), akv("cha"), kkvip("cha"),
                                         akvip("eko"), kir("pañca"), rj("tikacatukka", KVK), lj("tikacatukka", KV),
                                         "невозмутимость", RN)))
seg("1-1601", qa("kāmāvacarā", J(*KAMA_SET)))
seg("1-1603", qa("rūpāvacarā", rj("catukkapañcaka", KVK)))
seg("1-1605", qa("arūpāvacarā", f"{ARUPPA4} {KVK}"))
seg("1-1607", qa("pariyāpannā", ALL3_SABBA))
seg("1-1608", qa("apariyāpannā", LOK3))
seg("1-1610", qa("aniyyānikā", J(K3, AK, V4, KR3, RN)))
seg("1-1611", f"{Q('niyatā')} " + ans(J(DS4, DOM2), siya("niyatā", "aniyatā")) + " "
    + ans(F.FOUR_PATHS + OPEN, N["niyatā"]))
seg("1-1612", qa("aniyatā", ANIYATA_BODY))
seg("1-1613", qa("sauttarā", ALL3_SABBA))
seg("1-1614", qa("anuttarā", LOK3))
seg("1-1615", qa("saraṇā", AK12))
seg("1-1616", qa("araṇā", J(*REST4_RN)), EXACT["Atthuddhāro niṭṭhito."], EXACT["Dhammasaṅgaṇīpakaraṇaṃ niṭṭhitaṃ."])

# =========================================================================================
# 7. Line dispatch, checks, build
# =========================================================================================
Q_RE = re.compile(r"^Katame dhammā (.+?)\? ")
A_RE = re.compile(r"– ime dhammā ([^–?]+?)\.$")
LATIN = re.compile(r"[A-Za-zĀāĪīŪūṂṃṄṅÑñṬṭḌḍṆṇḶḷ]")


def check_line(sid, p, r):
    assert OPEN not in r, ("marker", sid)
    assert p.count("–") + p.count("—") == r.count("–") and "—" not in r, ("dash", sid, p.count("–"), r.count("–"))
    assert p.count(PE) == r.count(ELL), ("pe", sid, p.count(PE), r.count(ELL))
    assert p.count("?") == r.count("?"), ("question", sid, p.count("?"), r.count("?"))
    assert p.endswith("?") == r.endswith("?"), ("end", sid)
    assert "  " not in r and " ," not in r and ",," not in r and " ." not in r and ";;" not in r, ("spacing", sid, r)
    assert ", ;" not in r and "; ," not in r and ":-" not in r, ("punct", sid)
    assert not re.search(r"(?<![А-Яа-яЁё])ли(?![А-Яа-яЁё])", r), ("li", sid)
    stripped = re.sub(r"\[[^\]]*\]", "", r)
    assert not LATIN.search(stripped), ("latin", sid, LATIN.search(stripped).group(0))
    m = Q_RE.match(p)
    if m:
        assert r.startswith(Q(m.group(1)) + " "), ("q-frame", sid, m.group(1))
    m = A_RE.search(p)
    if m and m.group(1) in N:
        assert r.endswith(S.a_form(N[m.group(1)])), ("a-frame", sid, m.group(1), r[-80:])


def translate(sid, plines):
    if sid in REUSE:
        old = REUSE[sid]
        assert PREV_PALI[old] == plines, ("reuse differs", sid, old)
        return PREV_RU[old]
    if sid in R:
        return R[sid]
    assert len(plines) == 1, sid
    if plines[0] in EXACT:
        return [EXACT[plines[0]]]
    raise KeyError(f"no translation for ^{sid}: {plines[0][:80]}")


def build():
    segs = S.segments(PALI)
    ru = {}
    for sid, plines in segs:
        plines = [STRIP.sub("", x) for x in plines]
        rlines = translate(sid, plines)
        assert len(rlines) == len(plines), (sid, len(plines), len(rlines))
        for p, r in zip(plines, rlines):
            check_line(sid, p, r)
        ru[sid] = rlines
    unused = (set(R) | set(REUSE)) - {s for s, _ in segs}
    assert not unused, unused
    return ru, len(segs)


DECISIONS = [
    "bhūmīsu (termbase «мир»): catūsu / tīsu bhūmīsu = «четырёх / трёх миров» after the noun (genitive).",
    "cittuppāda = «вид ума» (user): «двенадцать видов неблагого ума», «четыре вида ума, связанных с приверженностью "
    "воззрениям»; the ablatives kusalato / vipākato / kiriyato keep the termbase «в благом виде» / «в виде "
    "результатов действий» / «в функциональном виде»; akusalato (termbase «неблагой ум») = «N видов неблагого ума»; "
    "Kāmāvacarakusalato (no entry) = «N видов благого ума, относящегося к миру чувственных желаний».",
    "vipāko (catūsu bhūmīsu vipāko) = «результат действий» (2-05: «Lokuttaravipāko» = «Надмирский результат "
    "действий»); vipākesu = «в результатах действий»; kusalesu / kiriyesu = «в благом / функциональном уме»; "
    "sabbākusalesu = «во всех видах неблагого ума»; sasaṅkhārikesu akusalesu = «в видах неблагого ума с побуждением».",
    "kāmāvacarakusalassa vipākato ca kiriyato ca pañca (^1-1387) = «по пять в виде результатов … и в функциональном "
    "виде» (five resultant and five functional kinds).",
    "cattāro arūpāvacarā (^1-1389, 1590) = «четыре вида ума, относящихся к миру без форм» (the noun is implied in the "
    "Pāli); cattāro āruppā = «четыре бесформенных состояния» (termbase).",
    "rūpāvacara-<a><b>-jjhānā built on the termbase lokuttaratikacatukkajjhānā: «три медитативных погружения, "
    "относящихся к миру форм, по четверичному методу и четыре по пятеричному».",
    "Dvepañcaviññāṇāni = «дважды пять видов сознания» (termbase pañcaviññāṇāni «пять видов сознания»).",
    "na vattabbā (termbase «определить»): «это явления, которые нельзя определить ни как X, ни как Y»; after a "
    "siyā list «иногда их нельзя определить …»; with a subject and the Pāli dash «X нельзя определить – ни как …» "
    "(4-02 «Ум нельзя определить – …»); singular subjects take the singular name («явление с …»).",
    "etthuppannaṃ / etthuppanne X ṭhapetvā = «кроме возникшего / возникших в них X» (termbase uppanne hetū «возникшие "
    "в них корни», uppannaṃ vicāraṃ «возникшее в них удержание мысли»).",
    "siyā = «иногда»; a bare «na X» inside a siyā list = «но не X» (after «;» simply «не X»).",
    "Pīti / Sukhaṃ … (^1-1404) and Cattāro ariyamaggā … (^1-1429) take verbs («не сопровождается восторгом», «не имеют "
    "объектом путь»), as 3-01 «не сопровождается счастьем».",
    "rūpañca, nibbānañca = «и материальная форма, и нирвана» (4-01 «и вся материальная форма, и необусловленный "
    "элемент»); «Rūpañca nibbānañca anārammaṇā.» = «И материальная форма, и нирвана не имеют объекта.»",
    "Punctuation: a list that ends with «кроме …» keeps the comma before the Pāli dash («…, кроме возникшего в них "
    "заблуждения, – это …»), as the approved sample ^1-62; ^1-1535 «…cittasamuṭṭhānaṃ – rūpāyatanaṃ …» has a Pāli dash "
    "where 4-02 ^1-1201 has none, so the 4-02 colon becomes «, –».",
    "dukkhasahagata(ṃ) kāyaviññāṇaṃ (^1-1388, 1404) = «осязательное сознание, сопровождаемое болью» (2-05 "
    "dukkhasahagataṃ «сопровождаемое болью», termbase dukkhaṃ «боль»; the adherence check flags dukkha «болезненный» "
    "in ^1-1404).",
    "Yattha dve tīṇi saṃyojanāni = «двое или трое оков» (оковы has no singular); dve tīṇi nīvaraṇāni «две или три "
    "помехи»; dve tayo āsavā / kilesā «два или три влечения / омрачения».",
    "sabbeva (^1-1437) = «все без исключения»: the termbase eva senses («полностью», «несомненно») do not fit.",
    "Niyogā anāgatārammaṇā natthi (^1-1433) = «Явлений, которые непременно являются явлениями с будущим объектом, "
    "нет.» (Niyogā «непременно»; Natthi's termbase sense belongs to the nihilist view).",
    "Dhammasaṅgaṇīpakaraṇaṃ = «Книга «Перечисление явлений»»: pakaraṇa is not in the termbase.",
    "Headings: Tikaatthuddhāro / Dukaatthuddhāro = «Разъяснение смысла троек / пар» (termbase atthuddhāro "
    "«разъяснение смысла»); the chapter heading «Раздел разъяснений» is from the sample.",
    "Reused word for word (identical Pāli): ^1-1412, 1414, 1427, 1438, 1457, 1459, 1483, 1495, 1509, 1527, 1529, 1531, "
    "1533, 1537, 1539, 1541, 1543, 1545, 1547-1549, 1559, 1573, 1575, 1602, 1604, 1606, 1609 and the group headings "
    "(from 4-01 … 4-03).",
    "Source slips: ^1-1389 «ya vedanāya sampayuttātipi» is a clipped «adukkhamasukhāya vedanāya sampayuttātipi» and is "
    "rendered as the full matrix item; ^1-1478 ends the question with «.» (kept); ^1-1501 / 1502 abridge the flood "
    "and yoke groups to «Katame dhammā oghā…pe….» (kept); missing commas (^1-1387, 1401, 1446, 1465, 1518, 1567, "
    "1591, 1594, 1597, 1598) are not mirrored.",
    "Variants: [dutiyajjhāne (sī.)] = «вариант написания»; [sabbeva (syā.)] = «вариант чтения» (adds eva).",
]


def notes():
    L = ["# pi-1 Russian rails: new formulas of 5 (Aṭṭhakathākaṇḍaṃ)", "",
         "Generated by build_rails_5_ru.py from its fixed strings; import that file instead of retyping. Strings "
         "already in ru-rails-formulas.md or the notes of chapters 2-4 are not repeated (the taint, fetter, tie, "
         "hindrance and clinging names, «Те самые … и есть …», «Ум нельзя определить – …» come from the 4-0x "
         "builders). Matrix names in the question and answer frames come verbatim from build_rails_sample_ru.py.", "",
         "Punctuation before the Pāli dash: «X – это …» after a plain noun or list; «…, – это …» where the dash "
         "closes a participial phrase, a subordinate clause or a closing «кроме …» phrase.", "",
         "## Formulas (Pāli = Russian)", ""]
    seen = set()
    for p, r in NOTES:
        if p not in seen:
            seen.add(p)
            L.append(f"{p} = {r}")
    L += ["", "## Decisions and termbase misfits (reported)", ""] + DECISIONS
    (HERE / "notes-5.md").write_text("\n".join(L) + "\n", encoding="utf-8", newline="\n")
    print("wrote", HERE / "notes-5.md")


def main():
    ru, n = build()
    S.emit(PALI, ru, OUT)
    notes()


if __name__ == "__main__":
    main()
