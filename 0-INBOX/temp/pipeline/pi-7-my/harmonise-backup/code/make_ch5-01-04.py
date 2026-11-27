"""Burmese zero-shot of pi-7 part 5 (Pañcamo bhāgo), chapters 5-01 anuloma-tikatika, 5-02 anuloma-dukaduka,
5-03 paccanīya-tika, 5-04 paccanīya-duka («အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ»), from the Pāli only.

usage: python3 -I -X utf8 make_ch5-01-04.py [chapter ...] [--dev] [--slips] [--out DIR] [--dump]
  (no flag)  translate the chapters and write them; stops on the first unmatched sentence (nothing is guessed).
  --dev      do not stop: list every unmatched skeleton with its count in chk-ch5-01-04/dev.txt (nothing written).
  --dump     print the combined-term table (Pāli chain = Burmese) and stop.

Engines (read-only, imported, never run as scripts; each loaded on its OWN copies of my7_formulas / make_sample):
  * world A = make_ch3-09.py (it imports make_ch3-03-06 -> make_ch3-01-02 -> make_ch2-03-06: PRIMARY my7_formulas +
    make_sample + make_ch1-01, FALLBACK per unit make_ch1-03-05): the hetu … kenaci, āsava … yoga and mahantara dyads,
    and the engine for the triad chapters;
  * world B = make_ch4-01.py (it imports make_ch3-07-08-10 -> make_ch3-01-02 the same way): the nīvaraṇa, parāmāsa,
    upādāna, kilesa and piṭṭhiduka dyads;
  * value sources only: make_ch2-07-11.py (triads 2-01 … 2-02, 2-07 … 2-11) and make_ch2-12-17.py (2-12 … 2-17).
No main block of another script runs; no file of the sample or of another group is edited or written.

A chapter is cut at its part headings (5-01 «##### 1-1. Kusalattika-vedanāttikaṃ», 5-02 «##### 1-1.
Hetuduka-sahetukadukaṃ», 5-03 «##### Kusalattikaṃ», 5-04 «##### Hetudukaṃ»). In each part every term chain is
rewritten, before slotting, into ONE synthetic a-stem term whose Burmese is
  * two terms on one noun (triad x triad, dyad x dyad, the sixth dyads with «na»): the qualifiers stacked «A၊ B»
    (the stacking pattern of 2-01 … 2-02 / 2-07 … 2-11 / 3-01 … 3-02, coordinator);
  * a pair that is itself a dyad term of pi-1 (the sixth dyad of each cluster, «nahetu sahetuka / ahetuka», the
    «ceva … ca» dyads): that dyad's Burmese (finished groups);
  * «na-X» (paccanīya): the Burmese of X negated («…သော» -> «…သည် မဟုတ်သော», a noun -> «… မဟုတ်သော»);
then the engine translates the part with only that term table active. Every new string is logged in
notes-ch5-01-04.md.
"""
import collections
import importlib.util
import pathlib
import re
import sys

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
ROOT = HERE.parents[3]
PALI = ROOT / "AI_translation/pali/pi-7_split_chapters"
OUT = ROOT / "AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters"
NAMES = ["5-01-anuloma-tikatika.md", "5-02-anuloma-dukaduka.md", "5-03-paccaniya-tika.md", "5-04-paccaniya-duka.md"]
CHK = HERE / "chk-ch5-01-04"
WCH = r"[\wāīūṃṅñṭḍṇḷ]"
_NB = r"(?!" + WCH + ")"
_PB = r"(?<!" + WCH + ")"
_SHARED = ("my7_formulas", "make_sample")


def _load(name, fn):
    spec = importlib.util.spec_from_file_location(name, HERE / fn)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def _isolated(name, fn):
    """load a group script on its own fresh copies of the shared modules (the caller's copies are restored)"""
    saved = {k: sys.modules.pop(k) for k in _SHARED if k in sys.modules}
    try:
        return _load(name, fn)
    finally:
        for k in _SHARED:
            sys.modules.pop(k, None)
        sys.modules.update(saved)


A = _isolated("w5a_ch309", "make_ch3-09.py")
B = _isolated("w5b_ch401", "make_ch4-01.py")
L = _isolated("v5l_ch20711", "make_ch2-07-11.py")
U = _isolated("v5u_ch21217", "make_ch2-12-17.py")
assert A.F is not B.F

NEW = collections.OrderedDict()     # every new string of this script: Pāli -> Burmese
SLIPS = []                          # source slips (read as written unless an obvious omission / misspelling)


def new(pali, my):
    if pali in NEW:
        assert NEW[pali] == my, (pali, NEW[pali], my)
    NEW.setdefault(pali, my)
    return my


class World:
    def __init__(self, tag, mod, d):
        self.tag, self.mod, self.D = tag, mod, d
        self.M = d.M
        self.F, self.FG, self.K, self.G = d.M.F, d.M.FG, d.M.K, d.M.G


WA = World("A", A, A.M3)
WB = World("B", B, B.D)
F = WA.F
C, END, PE = F.C, F.END, F.PE
for _w in (WA, WB):
    assert (_w.F.C, _w.F.END, _w.F.PE) == (C, END, PE)
SEP = C + " "                     # the stacking separator «A၊ B»

# ===================================================================================== the triads (finished groups)
_FT = WA.F.TRIADS
_GT = WA.G.TRIADS_ADD
_MT = WA.M.TRIADS_ADD
_LM = L.M.TRIADS_ADD          # 2-01 … 2-02 (make_ch2-01-02 inside make_ch2-07-11)
_LT = L.TRIADS_ADD            # 2-07 … 2-11
_UT = U.TRIADS_ADD            # 2-12 … 2-17
TRIADS = {   # triad heading -> {Pāli stem: Burmese attributive}
    "Kusalattikaṃ": {k: _FT["kusala"][k] for k in ("kusal", "akusal", "abyākat")},
    "Vedanāttikaṃ": {k: _FT["vedana"][k] for k in ("sukhāya vedanāya sampayutt", "dukkhāya vedanāya sampayutt",
                                                    "adukkhamasukhāya vedanāya sampayutt")},
    "Vipākattikaṃ": {"vipāk": _GT["vipaka"]["vipāk"], "vipākadhammadhamm": _GT["vipaka"]["vipākadhammadhamm"],
                     "nevavipākanavipākadhammadhamm": _GT["vipaka"]["nevavipākanavipākadhammadhamm"]},
    "Upādinnattikaṃ": {k: _GT["upadinna"][k] for k in ("upādinnupādāniy", "anupādinnupādāniy",
                                                         "anupādinnaanupādāniy")},
    "Saṃkiliṭṭhattikaṃ": {k: _GT["sankilittha"][k] for k in ("saṃkiliṭṭhasaṃkilesik", "asaṃkiliṭṭhasaṃkilesik",
                                                              "asaṃkiliṭṭhaasaṃkilesik")},
    "Vitakkattikaṃ": {k: _LM["vitakka"][k] for k in ("savitakkasavicār", "avitakkavicāramatt", "avitakkaavicār")},
    "Pītittikaṃ": {k: _LM["piti"][k] for k in ("pītisahagat", "sukhasahagat", "upekkhāsahagat")},
    "Dassanenapahātabbattikaṃ": {k: _MT["dassana"][k] for k in ("dassanena pahātabb", "bhāvanāya pahātabb",
                                                                  "nevadassanena nabhāvanāya pahātabb")},
    "Dassanenapahātabbahetukattikaṃ": {k: _MT["dassanahetu"][k] for k in (
        "dassanena pahātabbahetuk", "bhāvanāya pahātabbahetuk", "nevadassanena nabhāvanāya pahātabbahetuk")},
    "Ācayagāmittikaṃ": {k: _MT["acaya"][k] for k in ("ācayagām", "apacayagām", "nevācayagāmināpacayagām")},
    "Sekkhattikaṃ": {k: _MT["sekkha"][k] for k in ("sekkh", "asekkh", "nevasekkhanāsekkh")},
    "Parittattikaṃ": {k: _LT["paritta"][k] for k in ("paritt", "mahaggat", "appamāṇ")},
    "Parittārammaṇattikaṃ": {k: _LT["parittarammana"][k] for k in ("parittārammaṇ", "mahaggatārammaṇ",
                                                                   "appamāṇārammaṇ")},
    "Hīnattikaṃ": {k: _LT["hina"][k] for k in ("hīn", "majjhim", "paṇīt")},
    "Micchattaniyatattikaṃ": {k: _LT["micchatta"][k] for k in ("micchattaniyat", "sammattaniyat", "aniyat")},
    "Maggārammaṇattikaṃ": {k: _LT["magga"][k] for k in ("maggārammaṇ", "maggahetuk", "maggādhipat")},
    "Uppannattikaṃ": {k: _UT["uppanna"][k] for k in ("uppann", "anuppann", "uppād")},
    "Atītattikaṃ": {k: _UT["atita"][k] for k in ("atīt", "anāgat", "paccuppann")},
    "Atītārammaṇattikaṃ": {k: _UT["atitarammana"][k] for k in ("atītārammaṇ", "anāgatārammaṇ", "paccuppannārammaṇ")},
    "Ajjhattattikaṃ": {k: _UT["ajjhatta"][k] for k in ("ajjhatt", "bahiddh", "ajjhattabahiddh")},
    "Ajjhattārammaṇattikaṃ": {k: _UT["ajjhattarammana"][k] for k in ("ajjhattārammaṇ", "bahiddhārammaṇ",
                                                                     "ajjhattabahiddhārammaṇ")},
    "Sanidassanasappaṭighattikaṃ": {k: _UT["sanidassana"][k] for k in ("sanidassanasappaṭigh", "anidassanasappaṭigh",
                                                                      "anidassanaappaṭigh")},
}
# the short triad names of the part headings («Kusalattika-dassanattikaṃ», «Micchattattikaṃ» …)
TRIAD_SHORT = {"dassanattika": "Dassanenapahātabbattikaṃ", "dassanahetukattika": "Dassanenapahātabbahetukattikaṃ",
               "dassanahetuttika": "Dassanenapahātabbahetukattikaṃ", "micchattattika": "Micchattaniyatattikaṃ",
               "sanidassanattika": "Sanidassanasappaṭighattikaṃ"}
STEM_CLASS = {"ācayagām": "i", "apacayagām": "i", "nevācayagāmināpacayagām": "i", "maggādhipat": "i",
              "uppād": "i", "bahiddh": "d", "ajjhattabahiddh": "d"}
TIKA_NAME = {}
for _tn in (WA.F.TIKA_NAME, L.F.TIKA_NAME, U.F.TIKA_NAME):
    for _k, _v in _tn.items():
        if _k in TRIADS:
            assert TIKA_NAME.get(_k, _v) == _v, _k
            TIKA_NAME[_k] = _v
assert set(TIKA_NAME) == set(TRIADS), set(TRIADS) - set(TIKA_NAME)


def triad_of(word):
    """«Kusalattika» / «vedanāttikaṃ» / «Micchattattikaṃ» -> the TRIADS key"""
    w = re.sub(r"ttik(?:aṃ|a)$", "ttika", word)
    w = w[0].lower() + w[1:]
    if w in TRIAD_SHORT:
        return TRIAD_SHORT[w]
    k = w[0].upper() + w[1:] + "ṃ"
    if k in TRIADS:
        return k
    raise KeyError("triad " + word)


# ===================================================================================== the dyads (finished groups)
DA, DB = WA.D.DYADS, WB.D.DYADS


def _dv(world_dyads, dk, tk):
    return world_dyads[dk][tk]


# atom: Pāli surface stem (as written; first letter of either case) -> (class, Burmese). class: a (a-stem endings),
# u (hetu: u / uṃ / uñca / ussa / ū), i (-in / -i stems), d (indeclinable «bahiddhā», «upādā»: the case of a
# neighbour). Two-member dyad terms («X ceva Y ca», «Y ceva na / no ca X») are pairs of atoms; their Burmese is
# the finished groups' dyad term (KNOWN).
ATOM = {}
KNOWN = {}          # (atom, atom) joined by «ceva» -> Burmese of the pi-1 dyad term («hetu ceva sahetuko ca» …)
KNOWN_ADJ = {}      # (atom, atom) side by side -> Burmese of the pi-1 dyad term (the sixth dyads)
DYAD_TERMS = {}     # dyad heading -> [atoms] (positive), for the parts


def atom(surf, cls, my):
    if surf in ATOM:
        assert ATOM[surf] == (cls, my), (surf, ATOM[surf], (cls, my))
    ATOM[surf] = (cls, my)
    return surf


def dy(head, *atoms):
    DYAD_TERMS.setdefault(head, [])
    DYAD_TERMS[head] += [a for a in atoms if a not in DYAD_TERMS[head]]


# hetu cluster (3-01)
dy("Hetudukaṃ", atom("het", "u", DA["hetu"]["hetudk"]), atom("nahet", "u", DA["hetu"]["nahetudk"]))
dy("Sahetukadukaṃ", atom("sahetuk", "a", DA["sahetuka"]["sahetuk"]), atom("ahetuk", "a", DA["sahetuka"]["ahetuk"]))
dy("Hetusampayuttadukaṃ", atom("hetusampayutt", "a", DA["hetusamp"]["hetusampayutt"]),
   atom("hetuvippayutt", "a", DA["hetusamp"]["hetuvippayutt"]))
atom("na ca het", "u", DA["hetu"]["nahetudk"])              # inside «Y ceva na ca hetu»
KNOWN[("het", "sahetuk")] = DA["hetusahetuka"]["hetusahetukdk"]               # hetu ceva sahetuko ca
KNOWN[("sahetuk", "na ca het")] = DA["hetusahetuka"]["sahetukanahetudk"]      # sahetuko ceva na ca hetu
KNOWN[("het", "hetusampayutt")] = DA["hetuhetusamp"]["hetuhetusampdk"]
KNOWN[("hetusampayutt", "na ca het")] = DA["hetuhetusamp"]["hetusampnahetudk"]
KNOWN_ADJ[("nahet", "sahetuk")] = DA["nahetusahetuka"]["nahetusahetuk"]          # the sixth hetu dyad (3-01)
KNOWN_ADJ[("nahet", "ahetuk")] = DA["nahetusahetuka"]["nahetuahetuk"]
atom("nahetusahetuk", "a", DA["nahetusahetuka"]["nahetusahetuk"])             # written as one word (5-02, 5-04)
dy("Hetusahetukadukaṃ", "het", "sahetuk", "na ca het")
dy("Hetuhetusampayuttadukaṃ", "het", "hetusampayutt", "na ca het")
dy("Nahetusahetukadukaṃ", "nahet", "sahetuk", "ahetuk", "nahetusahetuk")
# cūḷantara (3-02)
for _h, _dk, _pairs in (("Sappaccayadukaṃ", "sappaccaya", (("sappaccay", "sappaccay"), ("appaccay", "appaccay"))),
                        ("Saṅkhatadukaṃ", "sankhata", (("saṅkhat", "saṅkhat"), ("asaṅkhat", "asaṅkhat"))),
                        ("Sanidassanadukaṃ", "sanidassana", (("sanidassan", "sanidassan"), ("anidassan", "anidassan"))),
                        ("Sappaṭighadukaṃ", "sappatigha", (("sappaṭigh", "sappaṭigh"), ("appaṭigh", "appaṭigh"))),
                        ("Rūpīdukaṃ", "rupi", (("rūp", "rūpdk"), ("arūp", "arūpdk"))),
                        ("Lokiyadukaṃ", "lokiya", (("lokiy", "lokiy"), ("lokuttar", "lokuttar"))),
                        ("Kenaciviññeyyadukaṃ", "kenaci", (("kenaci viññeyy", "kenaci viññeyy"),
                                                            ("kenaci naviññeyy", "kenaci naviññeyy")))):
    dy(_h, *[atom(s, "i" if _dk == "rupi" else "a", DA[_dk][k]) for s, k in _pairs])

# the five clusters of 3-03 … 3-06 (world A) and the three of 3-07 … 3-10 (world B): six dyads each
CL = {}             # cluster -> dict(x, nox, s, as, samp, vipp)


def cluster(cl, x, s, a_s, keys, tab):
    """x «āsav», s «sāsav», a_s «anāsav»; keys: the six dyad keys of the world table"""
    k1, k2, k3, k4, k5, k6 = keys
    X, NOX = list(tab[k1])[:2]
    S, AS = list(tab[k2])[:2]
    SAMP, VIPP = list(tab[k3])[:2]
    cap = x[0].upper() + x[1:]
    atom(x, "a", tab[k1][X])
    atom("no" + x, "a", tab[k1][NOX])
    atom("no " + x, "a", tab[k1][NOX])                       # «hetu no parāmāso» (written apart)
    atom("no ca " + x, "a", tab[k1][NOX])                    # inside «Y ceva no ca X»
    atom(s, "a", tab[k2][S])
    atom(a_s, "a", tab[k2][AS])
    atom(x + "asampayutt", "a", tab[k3][SAMP])
    atom(x + "avippayutt", "a", tab[k3][VIPP])
    if k4:
        A4, B4 = list(tab[k4])[:2]
        KNOWN[(x, s)] = tab[k4][A4]                          # X ceva S ca
        KNOWN[(s, "no ca " + x)] = tab[k4][B4]               # S ceva no ca X
    if k5:
        A5, B5 = list(tab[k5])[:2]
        KNOWN[(x, x + "asampayutt")] = tab[k5][A5]
        KNOWN[(x + "asampayutt", "no ca " + x)] = tab[k5][B5]
    A6, B6 = list(tab[k6])[:2]
    KNOWN_ADJ[(x + "avippayutt", s)] = tab[k6][A6]               # the sixth dyad (3-03-06 forms, coordinator)
    KNOWN_ADJ[(x + "avippayutt", a_s)] = tab[k6][B6]
    CL[cl] = dict(x=x, s=s, a_s=a_s, samp=x + "asampayutt", vipp=x + "avippayutt", cap=cap)
    dy(f"{cap}adukaṃ", x, "no" + x, "no " + x)
    dy(f"{s[0].upper() + s[1:]}adukaṃ", s, a_s)
    dy(f"{cap}asampayuttadukaṃ", x + "asampayutt", x + "avippayutt")
    if k4:
        dy(f"{cap}a{s}adukaṃ", x, s, "no ca " + x)
    if k5:
        dy(f"{cap}a{x}asampayuttadukaṃ", x, x + "asampayutt", "no ca " + x)
    dy(f"{cap}avippayutta{s}adukaṃ", x + "avippayutt", s, a_s)


for _cl, _x, _s, _as in (("asava", "āsav", "sāsav", "anāsav"), ("sannojana", "saññojan", "saññojaniy", "asaññojaniy"),
                         ("gantha", "ganth", "ganthaniy", "aganthaniy"), ("ogha", "ogh", "oghaniy", "anoghaniy"),
                         ("yoga", "yog", "yoganiy", "ayoganiy")):
    cluster(_cl, _x, _s, _as, (_cl, _cl + "_s", _cl + "_samp", _cl + "_xs", _cl + "_xxs", _cl + "_vs"), DA)
cluster("niv", "nīvaraṇ", "nīvaraṇiy", "anīvaraṇiy", ("niv1", "niv2", "niv3", "niv4", "niv5", "niv6"), DB)
cluster("par", "parāmās", "parāmaṭṭh", "aparāmaṭṭh", ("par1", "par2", "par3", "par4", None, "par6"), DB)
cluster("upa", "upādān", "upādāniy", "anupādāniy", ("upa1", "upa2", "upa3", "upa4", "upa5", "upa6"), DB)
# kilesa (4-01): kiles / nokiles, saṃkilesik, saṃkiliṭṭh, kilesasampayutt, the ceva dyads, the sixth dyad
_K = DB
atom("kiles", "a", _K["kil1"]["kilesdk"])
atom("nokiles", "a", _K["kil1"]["nokiles"])
atom("no ca kiles", "a", _K["kil1"]["nokiles"])
atom("saṃkilesik", "a", _K["kil2"]["saṃkilesik"])
atom("asaṃkilesik", "a", _K["kil2"]["asaṃkilesik"])
atom("saṃkiliṭṭh", "a", _K["kilS"]["saṃkiliṭṭh"])
atom("asaṃkiliṭṭh", "a", _K["kilS"]["asaṃkiliṭṭh"])
atom("kilesasampayutt", "a", _K["kilP"]["kilesasampayutt"])
atom("kilesavippayutt", "a", _K["kilP"]["kilesavippayutt"])
KNOWN[("kiles", "saṃkilesik")] = _K["kil4"]["kilesasaṃkilesikdk"]
KNOWN[("saṃkilesik", "no ca kiles")] = _K["kil4"]["saṃkilesikanokilesdk"]
KNOWN[("kiles", "saṃkiliṭṭh")] = _K["kilB"]["kilesasaṃkiliṭṭhdk"]
KNOWN[("saṃkiliṭṭh", "no ca kiles")] = _K["kilB"]["saṃkiliṭṭhanokilesdk"]
KNOWN[("kiles", "kilesasampayutt")] = _K["kil5"]["kilesakilesasampdk"]
KNOWN[("kilesasampayutt", "no ca kiles")] = _K["kil5"]["kilesasampnokilesdk"]
KNOWN_ADJ[("kilesavippayutt", "saṃkilesik")] = _K["kil6"]["kilesavippsaṃkilesik"]
KNOWN_ADJ[("kilesavippayutt", "asaṃkilesik")] = _K["kil6"]["kilesavippasaṃkilesik"]
dy("Kilesadukaṃ", "kiles", "nokiles")
dy("Saṃkilesikadukaṃ", "saṃkilesik", "asaṃkilesik")
dy("Saṃkiliṭṭhadukaṃ", "saṃkiliṭṭh", "asaṃkiliṭṭh")
dy("Kilesasampayuttadukaṃ", "kilesasampayutt", "kilesavippayutt")
dy("Kilesasaṃkilesikadukaṃ", "kiles", "saṃkilesik", "no ca kiles")
dy("Kilesasaṃkiliṭṭhadukaṃ", "kiles", "saṃkiliṭṭh", "no ca kiles")
dy("Kilesakilesasampayuttadukaṃ", "kiles", "kilesasampayutt", "no ca kiles")
dy("Kilesavippayuttasaṃkilesikadukaṃ", "kilesavippayutt", "saṃkilesik", "asaṃkilesik")
# mahantara (3-09, world A)
for _h, _dk, _pairs, _cls in (
        ("Sārammaṇadukaṃ", "sarammana", (("sārammaṇ", "sārammaṇ"), ("anārammaṇ", "anārammaṇ")), "a"),
        ("Cittadukaṃ", "citta", (("citt", "cittdk"), ("nocitt", "nocittdk")), "a"),
        ("Cetasikadukaṃ", "cetasika", (("cetasik", "cetasik"), ("acetasik", "acetasik")), "a"),
        ("Cittasampayuttadukaṃ", "cittasamp", (("cittasampayutt", "cittasampayutt"),
                                               ("cittavippayutt", "cittavippayutt")), "a"),
        ("Cittasaṃsaṭṭhadukaṃ", "cittasams", (("cittasaṃsaṭṭh", "cittasaṃsaṭṭh"),
                                             ("cittavisaṃsaṭṭh", "cittavisaṃsaṭṭh")), "a"),
        ("Cittasamuṭṭhānadukaṃ", "cittasamu", (("cittasamuṭṭhān", "cittasamuṭṭhān"),
                                              ("nocittasamuṭṭhān", "nocittasamuṭṭhān")), "a"),
        ("Cittasahabhūdukaṃ", "cittasaha", (("cittasahabh", "cittasahabhudk"),
                                            ("nocittasahabh", "nocittasahabhudk")), "u"),
        ("Cittānuparivattidukaṃ", "cittanu", (("cittānuparivatt", "cittānuparivattdk"),
                                              ("nocittānuparivatt", "nocittānuparivattdk")), "i"),
        ("Cittasaṃsaṭṭhasamuṭṭhānadukaṃ", "css", (("cittasaṃsaṭṭhasamuṭṭhān", "cittasaṃsaṭṭhasamuṭṭhān"),
                                                   ("nocittasaṃsaṭṭhasamuṭṭhān", "nocittasaṃsaṭṭhasamuṭṭhān")), "a"),
        ("Cittasaṃsaṭṭhasamuṭṭhānasahabhūdukaṃ", "csssaha", (
            ("cittasaṃsaṭṭhasamuṭṭhānasahabh", "cittasaṃsaṭṭhasamuṭṭhānasahabhudk"),
            ("nocittasaṃsaṭṭhasamuṭṭhānasahabh", "nocittasaṃsaṭṭhasamuṭṭhānasahabhudk")), "u"),
        ("Cittasaṃsaṭṭhasamuṭṭhānānuparivattidukaṃ", "cssanu", (
            ("cittasaṃsaṭṭhasamuṭṭhānānuparivatt", "cittasaṃsaṭṭhasamuṭṭhānānuparivattdk"),
            ("nocittasaṃsaṭṭhasamuṭṭhānānuparivatt", "nocittasaṃsaṭṭhasamuṭṭhānānuparivattdk")), "i"),
        ("Ajjhattikadukaṃ", "ajjhattika", (("ajjhattik", "ajjhattik"), ("bāhir", "bāhir")), "a"),
        ("Upādādukaṃ", "upada", (("upād", "upādādk"), ("noupād", "noupādādk")), "d"),
        ("Upādinnadukaṃ", "upadinna", (("upādinn", "upādinn"), ("anupādinn", "anupādinn")), "a")):
    dy(_h, *[atom(s, _cls, DA[_dk][k]) for s, k in _pairs])
# piṭṭhiduka (4-01, world B)
for _h, _dk in (("Dassanenapahātabbadukaṃ", "dass"), ("Bhāvanāyapahātabbadukaṃ", "bhav"),
                ("Dassanenapahātabbahetukadukaṃ", "dassh"), ("Bhāvanāyapahātabbahetukadukaṃ", "bhavh"),
                ("Savitakkadukaṃ", "vitakka"), ("Savicāradukaṃ", "vicara"), ("Sappītikadukaṃ", "sappitika"),
                ("Pītisahagatadukaṃ", "piti"), ("Sukhasahagatadukaṃ", "sukha"), ("Upekkhāsahagatadukaṃ", "upekkha"),
                ("Kāmāvacaradukaṃ", "kama"), ("Rūpāvacaradukaṃ", "rupa"), ("Arūpāvacaradukaṃ", "arupa"),
                ("Pariyāpannadukaṃ", "pariyapanna"), ("Niyyānikadukaṃ", "niyyanika"), ("Niyatadukaṃ", "niyata"),
                ("Sauttaradukaṃ", "sauttara"), ("Saraṇadukaṃ", "sarana")):
    _a, _b = [k for k in DB[_dk] if not k.endswith("_both")]
    dy(_h, atom(_a, "a", DB[_dk][_a]), atom(_b, "a", DB[_dk][_b]))

# which world owns a dyad (its notes, names and colophons)
WORLD_B_DYADS = {h for h in DYAD_TERMS if h.startswith(("Nīvaraṇ", "Parām", "Upādān", "Kiles", "Saṃkiles", "Saṃkiliṭṭh",
                                                        "Dassanenapahātabb", "Bhāvanāyapahātabb", "Savitakk",
                                                        "Savicār", "Sappītik", "Pītisahagat", "Sukhasahagat",
                                                        "Upekkhāsahagat", "Kāmāvacar", "Rūpāvacar", "Arūpāvacar",
                                                        "Pariyāpann", "Niyyānik", "Niyat", "Sauttar", "Saraṇ"))}

# the dyad names: the finished groups' DUKA_NAME
DUKA_NAME = {}
for _dn in (WA.D.DUKA_NAME, A.M4.DUKA_NAME, A.DUKA_NAME, WB.D.DUKA_NAME, B.B.DUKA_NAME, B.DUKA_NAME):
    for _k, _v in _dn.items():
        assert DUKA_NAME.get(_k, _v) == _v, _k
        DUKA_NAME[_k] = _v

# ===================================================================================== negation («na-X», paccanīya)
NOT = F.NOT                           # «မဟုတ်»
_VERBAL = ("ကြောင့်", "၍", "နှင့်အတူ", "မှ", "၌", "သို့", "ဖြင့်")   # «… ဖြစ်သော» = arising, not «being X»


def neg(my):
    """the Burmese of «na-X» from the Burmese of X (free na = «… မဟုတ်», brief): an attributive «…သော» ->
    «…သည် မဟုတ်သော» (as pi-1 «na pītisahagatā» «ပီတိနှင့်အတူ ဖြစ်သည် မဟုတ်သော»); a noun or genitive -> «… မဟုတ်သော»
    (as pi-1 «na hetū» «အမြစ် မဟုတ်သော» beside hetu «အမြစ်»)"""
    m = re.fullmatch(r"(.+) ဖြစ်သော", my)
    if m and " " not in m[1].replace("မှားယွင်းသော ", "").replace("စိတ်၏ ", "").replace("ကံ၏ ", "") \
            and not m[1].endswith(_VERBAL):         # «X ဖြစ်သော» (being X) -> «X မဟုတ်သော» (pi-1 hetu / na hetu)
        return f"{m[1]} {NOT}သော"
    if my.endswith("မည့်"):                          # pahātabba «ပယ်ရမည့်» -> «ပယ်ရမည် မဟုတ်သော» (pi-1)
        return my[:-len("မည့်")] + f"မည် {NOT}သော"
    if my.endswith("သော"):
        return my[:-len("သော")] + f"သည် {NOT}သော"
    return f"{my} {NOT}သော"


NEG_LOG = collections.OrderedDict()


def neg_atom(surf):
    """«na» + an atom (written together; «na nahetu» / «na noX» also apart)"""
    cls, my = ATOM[surf]
    n = "na" + surf
    v = neg(my)
    NEG_LOG.setdefault(n, v)
    atom(n, cls, v)
    out = [n]
    if surf.startswith(("na", "no")):
        atom("na " + surf, cls, v)
        out.append("na " + surf)
    return out




# ===================================================================================== chains -> synthetic terms
_CONS = "bcdfghjklmnpqrstvwxz"


def _skey(i):
    s = ""
    i += 1
    while i:
        i, r = divmod(i - 1, len(_CONS))
        s = _CONS[r] + s
    return "zqw" + s


KEYS = {}            # Burmese -> synthetic key (one key per Burmese)
KEY_PALI = {}        # synthetic key -> the Pāli chains it stands for
_N = [0]


def key_of(my, pali):
    if my not in KEYS:
        KEYS[my] = _skey(_N[0])
        _N[0] += 1
    k = KEYS[my]
    KEY_PALI.setdefault(k, set()).add(pali)
    return k


_END = {"a": ["añceva", "ānañca", "añca", "assa", "ānaṃ", "aṃ", "ena", "o", "ā", "e"],
        "u": ["uñceva", "ūnaṃ", "uñca", "ussa", "uṃ", "ū", "u"],
        "i": ["iñceva", "īnaṃ", "iñca", "issa", "ino", "iṃ", "ī", "i"],
        "d": ["ā"]}
# the a-stem case of an ending; None: ambiguous (the next noun decides; a d-class word: the previous member)
_CASE = {"a": {"añceva": "aṃ", "ānañca": "ānaṃ", "añca": "aṃ", "assa": "assa", "ānaṃ": "ānaṃ", "aṃ": "aṃ", "ena": "ena",
               "o": "o", "ā": "ā", "e": "e"},
         "u": {"uñceva": "aṃ", "ūnaṃ": "ānaṃ", "uñca": "aṃ", "ussa": "assa", "uṃ": "aṃ", "ū": None, "u": "o"},
         "i": {"iñceva": "aṃ", "īnaṃ": "ānaṃ", "iñca": "aṃ", "issa": "assa", "ino": "ā", "iṃ": "aṃ", "ī": None,
               "i": None},
         "d": {"ā": None}}
_NOUN_END = {"o": "o", "aṃ": "aṃ", "ā": "ā", "assa": "assa", "ānaṃ": "ānaṃ", "e": "e"}
_NOUN_RX = re.compile(_PB + r"(?:dhamm|khandh)(o|aṃ|ā|assa|ānaṃ|e)" + _NB)
_NOUNISH = re.compile(r" (?:dhamm|khandh|(?:ekaṃ|eko|ekassa|dve|tayo|tiṇṇaṃ|tiṇṇannaṃ) khandh|kaṭattārūp)")


def _noun_case(text, end):
    """the case of the next head noun (dhamma / khandha) of the sentence"""
    seg = re.split(r"[.;–]| paṭicca", text[end:end + 160])[0]
    m = _NOUN_RX.search(seg)
    return _NOUN_END[m[1]] if m else None


class Part:
    """the terms of one part: its atoms; stack: side-by-side terms are one chain (two qualifiers on one noun);
    closer_links: a «ceva … ca» term followed by a term stacks with it (5-02 «Hetuñceva sahetukañca hetuṃ»), else
    its closer «ca» also coordinates (5-04 «Nahetuñceva naahetukañca naahetukañceva na nahetuñca dhammaṃ»);
    singles: the atoms that are rewritten when they stand alone (before a noun, or coordinated)"""

    def __init__(self, atoms, stack=True, closer_links=False, singles=()):
        self.atoms = set(atoms)
        self.stack = stack
        self.closer_links = closer_links
        self.singles = set(singles)
        alts = []
        for s in sorted(self.atoms, key=len, reverse=True):
            ends = "|".join(_END[ATOM[s][0]])
            pat = f"[{s[0].upper()}{s[0]}]" + re.escape(s[1:]).replace(r"\ ", " ")
            alts.append(f"(?:{pat})(?:{ends})")
        self.rx = re.compile(_PB + "(?:" + "|".join(alts) + ")" + _NB) if alts else None
        self.order = sorted(self.atoms, key=len, reverse=True)

    def split(self, w):
        lw = w[0].lower() + w[1:]
        for s in self.order:
            if lw.startswith(s) and lw[len(s):] in _END[ATOM[s][0]]:
                return s, lw[len(s):]
        raise KeyError(w)


class Term:
    def __init__(self, occs, part):
        self.occs = occs
        self.atoms = [part.split(m[0]) for m in occs]
        self.start, self.end = occs[0].start(), occs[-1].end()
        self.ceva = len(occs) == 2
        self.coord = None          # 'in' (ñca) / 'apart' (« ca») / None
        self.closer = None         # for a ceva term: 'in' / 'apart' / None


def _terms(text, part):
    occ = list(part.rx.finditer(text))
    terms, i = [], 0
    while i < len(occ):
        if i + 1 < len(occ):
            gap = text[occ[i].end():occ[i + 1].start()]
            if gap == " ceva " or (gap == " " and occ[i][0].endswith("ñceva")):
                t = Term([occ[i], occ[i + 1]], part)
                e = t.atoms[1][1]
                if e.endswith("ñca"):
                    t.closer = "in"
                elif re.match(r" ca" + _NB, text[t.end:t.end + 4]):
                    t.closer = "apart"
                terms.append(t)
                i += 2
                continue
        t = Term([occ[i]], part)
        e = t.atoms[0][1]
        if e.endswith("ñca"):
            t.coord = "in"
        elif re.match(r" ca" + _NB, text[t.end:t.end + 4]):
            t.coord = "apart"
        terms.append(t)
        i += 1
    return terms


def _span_end(text, t):
    return t.end + (3 if (t.closer == "apart" or t.coord == "apart") else 0)


def _chains(text, terms, part):
    chains, cur = [], [terms[0]] if terms else []
    for a, b in zip(terms, terms[1:]):
        gap_ok = text[_span_end(text, a):b.start] == " "
        link = False
        if gap_ok and part.stack:
            if not a.ceva and a.coord is None:
                link = True
            elif a.ceva and (a.closer is None or part.closer_links):
                link = True
        if link:                                  # two qualifiers of one noun share its case
            ca, cb = _CASE[ATOM[a.atoms[-1][0]][0]][a.atoms[-1][1]], _CASE[ATOM[b.atoms[0][0]][0]][b.atoms[0][1]]
            if ca is not None and cb is not None and ca != cb:
                link = False
        if link:
            cur.append(b)
        else:
            chains.append(cur)
            cur = [b]
    if cur:
        chains.append(cur)
    return chains


def _value(chain):
    """[Term] -> Burmese: the qualifiers stacked «A၊ B» (a pi-1 dyad pair: its own Burmese)"""
    items = []
    for t in chain:
        surfs = tuple(s for s, _ in t.atoms)
        if t.ceva:
            items.append(KNOWN.get(surfs, SEP.join(ATOM[s][1] for s in surfs)))
        else:
            items.append(surfs[0])
    vals, k = [], 0
    while k < len(items):                         # side-by-side pairs that are one dyad term (the sixth dyads)
        a = items[k]
        b = items[k + 1] if k + 1 < len(items) else None
        if isinstance(a, str) and a in ATOM and isinstance(b, str) and b in ATOM and (a, b) in KNOWN_ADJ \
                and not chain[k].ceva and not chain[k + 1].ceva:
            vals.append(KNOWN_ADJ[(a, b)])
            k += 2
            continue
        vals.append(ATOM[a][1] if (isinstance(a, str) and a in ATOM and not chain[k].ceva) else a)
        k += 1
    return SEP.join(vals)


def rewrite(text, part):
    """every term chain of the part -> one synthetic a-stem term (see the module doc)"""
    if part.rx is None:
        return text
    terms = _terms(text, part)
    if not terms:
        return text
    chains = _chains(text, terms, part)
    # coordination of the chains: a single term with its «ca» / «ñca»; a ceva term's closer also coordinates
    # when another chain follows right after it (or it closes a coordination), unless closer_links
    coord = []
    for n, ch in enumerate(chains):
        last = ch[-1]
        if not last.ceva:
            c = last.coord is not None
        elif last.closer is None:
            c = False
        else:
            nxt = chains[n + 1][0] if n + 1 < len(chains) else None
            adj_next = nxt is not None and text[_span_end(text, last):nxt.start] == " "
            adj_prev = n > 0 and coord[-1] and text[_span_end(text, chains[n - 1][-1]):ch[0].start] == " "
            c = adj_next or adj_prev
        coord.append(c)
    out, pos = [], 0
    for n, ch in enumerate(chains):
        first, last = ch[0], ch[-1]
        start, end = first.start, last.end
        lone = len(ch) == 1 and not first.ceva
        if lone:
            surf = first.atoms[0][0]
            if surf not in part.singles or not (coord[n] or _NOUNISH.match(text[end:end + 30])
                                                or surf.endswith("dhammadhamm")):
                continue                          # a lone atom not before a noun stays («hetū», «cittaṃ» …)
        # the case: from the last member backwards (d-class: the previous member; ambiguous: the next noun)
        case = None
        members = [a for t in ch for a in t.atoms]
        for surf, e in reversed(members):
            c = _CASE[ATOM[surf][0]][e]
            if c is not None:
                case = c
                break
            if ATOM[surf][0] != "d":
                break
        if case is None:
            case = _noun_case(text, end)
        if case is None:
            raise KeyError(f"case of «{text[start:end]}»")
        span_end = end
        tail = ""
        apart = (last.closer == "apart" or last.coord == "apart")
        if coord[n]:
            if apart:
                span_end = end + 3
            tail = "añca" if case == "aṃ" else ("ānañca" if case == "ānaṃ" else " ca")
            if tail == " ca":
                tail = case + " ca"
            case = ""
        elif last.ceva and last.closer == "apart":
            span_end = end + 3                    # the closer « ca» of a ceva term (not coordinated)
        my = _value(ch)
        pali = text[start:span_end]
        key = key_of(my, pali)
        cap = pali[0].isupper()
        out.append(text[pos:start])
        out.append((key[0].upper() + key[1:] if cap else key) + case + tail)
        pos = span_end
        # «-dhammadhamma» terms hold their noun: the noun follows the term when the Pāli has none
        if members[-1][0].endswith("dhammadhamm") and not tail and not re.match(r" (?:ca )?dhamm", text[span_end:]):
            out.append(" dhamm" + case)
    out.append(text[pos:])
    return "".join(out)


# ===================================================================================== the triad atoms
TRI_ATOMS = {}       # triad heading -> [atoms]
for _th, _tab in TRIADS.items():
    TRI_ATOMS[_th] = [atom(_s, STEM_CLASS.get(_s, "a"), _v) for _s, _v in _tab.items()]
NEG_TRI = {th: sum((neg_atom(s) for s in ats), []) for th, ats in TRI_ATOMS.items()}
NEG_DY = {h: sum((neg_atom(s) for s in ats), []) for h, ats in DYAD_TERMS.items()}
# the paccanīya of a «na-» term («nakenaci viññeyya» -> «nanakenaci viññeyya»)
NEG2_DY = {h: sum((neg_atom(s) for s in ns if s.startswith("na") and not s.startswith("na ") and not
                   s[2:].startswith(("na", "no"))), []) for h, ns in NEG_DY.items()}
# «nakenaci viññeyyaṃ» (5-02 7-1: the second term of the cūḷantara dyad written with «na» first) = the paccanīya
# «na-kenaci viññeyya» of 5-04 (identical Pāli, identical Burmese)
assert "nakenaci viññeyy" in ATOM

# ===================================================================================== headings and names
TITLE, TIKA, DUKA, PADA, ADI = F.TITLE, F.TIKA, F.DUKA, F.PADA, F.ADI
HEAD_ANUL = F.HEAD["Dhammānulome"]                                       # «သဘောတရား အဟုတ်ပြ ပုံစံ၌»
ORDER_L = WA.K.ORDER_L
HEAD_PACC = new("Dhammapaccanīye", HEAD_ANUL.replace(ORDER_L["anulome"], ORDER_L["paccanīye"]))
HL = {}


def hl(pali, my, log=True):
    if pali in HL:
        assert HL[pali] == my, (pali, HL[pali], my)
    HL[pali] = my
    if log:
        new(pali, my)


hl("(Pañcamo bhāgo)", "(ပဉ္စမ အပိုင်း)")
_TT = f"{TIKA}နှင့် {TIKA}တို့၏ {TITLE}"
_DD = f"{DUKA}နှင့် {DUKA}တို့၏ {TITLE}"
hl("Dhammānulome tikatikapaṭṭhānaṃ", f"{HEAD_ANUL} {_TT}")
hl("Dhammānulome tikatikapaṭṭhānaṃ niṭṭhitaṃ.", f"{HEAD_ANUL} “{_TT}” {F.DONE}{END}")
hl("Dhammānulome dukadukapaṭṭhānaṃ", f"{HEAD_ANUL} {_DD}")
hl("Dhammānulome dukadukapaṭṭhānaṃ niṭṭhitaṃ.", f"{HEAD_ANUL} “{_DD}” {F.DONE}{END}")
hl("Anulomapaṭṭhānaṃ niṭṭhitaṃ.", f"{ORDER_L['anulome']} “{TITLE}” {F.DONE}{END}")
hl("Dhammapaccanīye tikapaṭṭhānaṃ", f"{HEAD_PACC} {F.HEAD['Tikapaṭṭhānaṃ']}")
hl("Dhammapaccanīye tikapaṭṭhānaṃ niṭṭhitaṃ.", f"{HEAD_PACC} “{F.HEAD['Tikapaṭṭhānaṃ']}” {F.DONE}{END}")
_DUKAP = WA.D.HL_ADD["Dhammānulome dukapaṭṭhānaṃ"][len(HEAD_ANUL) + 1:]     # «နှစ်မျိုးတွဲတို့၏ …» (3-01)
hl("Dhammapaccanīye dukapaṭṭhānaṃ", f"{HEAD_PACC} {_DUKAP}")
hl("Dhammapaccanīye dukapaṭṭhānaṃ niṭṭhitaṃ.", f"{HEAD_PACC} “{_DUKAP}” {F.DONE}{END}")
# pada headings: «X padaṃ» = «<term> ပုဒ်» (4-02 … 4-09 pattern)
for _p, (_th, _s) in {"Sukhāyavedanāyasampayuttapadaṃ": ("Vedanāttikaṃ", "sukhāya vedanāya sampayutt"),
                      "Dukkhāyavedanāyasampayuttapadaṃ": ("Vedanāttikaṃ", "dukkhāya vedanāya sampayutt"),
                      "Adukkhamasukhavedanāyasampayuttapadaṃ": ("Vedanāttikaṃ", "adukkhamasukhāya vedanāya sampayutt"),
                      "Paṇītapadaṃ": ("Hīnattikaṃ", "paṇīt"),
                      "Anāgatārammaṇapadaṃ": ("Atītārammaṇattikaṃ", "anāgatārammaṇ"),
                      "Paccuppannārammaṇapadaṃ": ("Atītārammaṇattikaṃ", "paccuppannārammaṇ"),
                      "Bahiddhāpadaṃ": ("Ajjhattattikaṃ", "bahiddh")}.items():
    hl(_p, f"{TRIADS[_th][_s]} {PADA}")
hl("Paccayacatukkaṃ", WA.F.HLINES["1-4. Paccayacatukkaṃ"][len("1-4. "):], log=False)     # (3-03 … 3-06)
hl("Mahaggatādipadāni", f"{TRIADS['Parittattikaṃ']['mahaggat']} {PADA} {ADI}")   # «X ပုဒ် စသည်» (as «-ādi» headings «… စသည်»)
for _p, _a in (("Sahetukapadaṃ", "sahetuk"), ("Ahetukapadaṃ", "ahetuk")):
    hl(_p, f"{ATOM[_a][1]} {PADA}")
_HA = F.cname("hetu"), F.cname("ārammaṇa")
hl("Hetuārammaṇapaccayādi", f"{_HA[0]}နှင့် {_HA[1]} {ADI}")                # as «Hetu-ārammaṇapaccayā» + ādi
for _th in TRIADS:
    hl(_th, TIKA_NAME[_th], log=False)
for _s, _th in TRIAD_SHORT.items():
    hl(_s[0].upper() + _s[1:] + "ṃ", TIKA_NAME[_th])
for _h, _v in DUKA_NAME.items():
    hl(_h, _v, log=False)

# gocchaka / group names (finished groups)
GNAME = {}
for _src in (WA.D.GOCCHAKA, A.M4.GNAME if hasattr(A.M4, "GNAME") else {}, B.B.GOCCHAKA, B.GOCCHAKA):
    GNAME.update(_src)
GNAME["Mahantaradukaṃ"] = A.MAHANTARA
for _cl, _c in A.M4.CLUSTERS.items():
    GNAME.setdefault(_c["head"], GNAME[_cl])
_GOC_TAIL = "တို့၏ အစု"
ADI_NOUN = {"saññojan": GNAME["sannojana"][:-len(_GOC_TAIL)], "ogh": GNAME["ogha"][:-len(_GOC_TAIL)],
            "parāmās": GNAME["Parāmāsagocchakaṃ"][:-len(_GOC_TAIL)]}   # the cluster nouns (pi-1)
assert all(GNAME[k].endswith(_GOC_TAIL) for k in ("sannojana", "ogha", "Parāmāsagocchakaṃ"))


def part_name_tt(num, a, b):
    return f"{num} {TIKA_NAME[a]}နှင့် {TIKA_NAME[b]}"


def finished_name(name):
    return F.finished(name)


# ===================================================================================== parts
PH_TT = re.compile(r"^##### (\d+-\d+\.) (\S+?ttika)-(\S+?ttikaṃ) \^", re.M)
PH_DD = re.compile(r"^##### ([\d-]+\.) (\S+?)(duka|gocchaka)-(\S+?)(dukaṃ|dukāni|gocchakaṃ) \^", re.M)
PH_T = re.compile(r"^##### (\S+ttikaṃ) \^", re.M)
PH_D = re.compile(r"^##### (?:[\d-]+\. )?(\S+?(?:dukaṃ|dukāni|gocchakaṃ)) \^", re.M)

# 5-02 group words -> dyad headings
_CLUSTER_HEADS = {}
for _cl, _c in CL.items():
    _cap = _c["cap"]
    _CLUSTER_HEADS[_cl] = [h for h in DYAD_TERMS if h.startswith(_cap)]
_HETU_CL = ["Hetudukaṃ", "Sahetukadukaṃ", "Hetusampayuttadukaṃ", "Hetusahetukadukaṃ", "Hetuhetusampayuttadukaṃ",
            "Nahetusahetukadukaṃ"]
_CULA = ["Sappaccayadukaṃ", "Saṅkhatadukaṃ", "Sanidassanadukaṃ", "Sappaṭighadukaṃ", "Rūpīdukaṃ", "Lokiyadukaṃ",
         "Kenaciviññeyyadukaṃ"]
_MAHA = ["Sārammaṇadukaṃ", "Cittadukaṃ", "Cetasikadukaṃ", "Cittasampayuttadukaṃ", "Cittasaṃsaṭṭhadukaṃ",
         "Cittasamuṭṭhānadukaṃ", "Cittasahabhūdukaṃ", "Cittānuparivattidukaṃ", "Cittasaṃsaṭṭhasamuṭṭhānadukaṃ",
         "Cittasaṃsaṭṭhasamuṭṭhānasahabhūdukaṃ", "Cittasaṃsaṭṭhasamuṭṭhānānuparivattidukaṃ", "Ajjhattikadukaṃ",
         "Upādādukaṃ", "Upādinnadukaṃ"]
_KIL = [h for h in DYAD_TERMS if h.startswith(("Kiles", "Saṃkiles", "Saṃkiliṭṭh"))]
_PITTHI = [h for h in DYAD_TERMS if h in WORLD_B_DYADS and h not in _KIL and not h.startswith(("Nīvaraṇ", "Parām",
                                                                                                 "Upādān"))]
_SANN_ADI = sum((_CLUSTER_HEADS[c] for c in ("sannojana", "gantha", "ogha", "yoga", "niv", "par")), [])
# a dyad's cluster (the paccanīya of a «ceva» dyad uses the terms of the cluster's other dyads: «nahetuñceva
# naahetukañca»)
CLUSTER_OF = {}
for _grp in [_HETU_CL] + [_CLUSTER_HEADS[c] for c in _CLUSTER_HEADS] + [_KIL]:
    for _h in _grp:
        CLUSTER_OF[_h] = _grp
GROUP_DYADS = {"saññojanādi": _SANN_ADI, "Saññojanādi": _SANN_ADI, "upādāna": _CLUSTER_HEADS["upa"],
               "Upādāna": _CLUSTER_HEADS["upa"], "kilesa": _KIL, "Kilesa": _KIL, "piṭṭhi": _PITTHI, "Piṭṭhi": _PITTHI,
               "Cūḷantara": _CULA, "Āsava": _CLUSTER_HEADS["asava"], "Mahantara": _MAHA,
               "Oghādi": _CLUSTER_HEADS["ogha"] + _CLUSTER_HEADS["yoga"] + _CLUSTER_HEADS["niv"],
               "Parāmāsādi": _CLUSTER_HEADS["par"]}


def dyads_of(word, kind):
    """«sahetuka»+«duka» -> [Sahetukadukaṃ]; «saññojanādi»+«dukāni» -> the group"""
    if word in GROUP_DYADS:
        return GROUP_DYADS[word]
    h = word[0].upper() + word[1:] + "dukaṃ"
    if h in DYAD_TERMS:
        return [h]
    raise KeyError(f"dyad {word}{kind}")


def parts_of(name, src):
    """[(world, Part, text)] for a chapter (the lines before the first part heading go with the first part)"""
    if name.startswith("5-01"):
        rx = PH_TT
    elif name.startswith("5-02"):
        rx = PH_DD
    elif name.startswith("5-03"):
        rx = PH_T
    else:
        rx = PH_D
    ms = list(rx.finditer(src))
    if not ms:
        raise SystemExit("no part heading in " + name)
    out = []
    for i, m in enumerate(ms):
        s = 0 if i == 0 else m.start()
        e = ms[i + 1].start() if i + 1 < len(ms) else len(src)
        text = src[s:e]
        if name.startswith("5-01"):
            a, b = triad_of(m[2]), triad_of(m[3])
            hl(f"{m[1]} {m[2]}-{m[3]}", part_name_tt(m[1], a, b))
            hl(f"{m[2]}{m[3]} niṭṭhitaṃ.", F.finished(f"{TIKA_NAME[a]}နှင့် {TIKA_NAME[b]}"))
            part = Part(TRI_ATOMS[a] + TRI_ATOMS[b])
            out.append((WA, part, text))
        elif name.startswith("5-02"):
            d1 = dyads_of(m[2], m[3])
            d2 = dyads_of(m[4], m[5])
            atoms = sum((DYAD_TERMS[h] for h in d1 + d2), [])
            if "Kenaciviññeyyadukaṃ" in d1 + d2:
                atoms.append("nakenaci viññeyy")
            hl(f"{m[1]} {m[2]}{m[3]}-{m[4]}{m[5]}", f"{m[1]} {dd_name(m[2], m[3], d1)}နှင့် {dd_name(m[4], m[5], d2)}")
            w = WB if any(h in WORLD_B_DYADS for h in d1 + d2) and not any(
                h in DYAD_TERMS and h not in WORLD_B_DYADS for h in d1 + d2 if h not in ("Hetudukaṃ",)) else WA
            out.append((w, Part(atoms, closer_links=True), text))
        elif name.startswith("5-03"):
            th = triad_of(m[1])
            pos = TRI_ATOMS[th]
            negs = NEG_TRI[th]
            singles = negs + (pos if th == "Kusalattikaṃ" else [])
            out.append((WA, Part(pos + negs, singles=singles), text))
        else:
            hs = dyads_of(*re.match(r"(.+?)(dukaṃ|dukāni|gocchakaṃ)$", m[1]).groups()) if m[1] not in DYAD_TERMS \
                else [m[1]]
            hs = sorted({c for h in hs for c in CLUSTER_OF.get(h, [h])}, key=list(DYAD_TERMS).index)
            pos = sum((DYAD_TERMS[h] for h in hs), [])
            negs = sum((NEG_DY[h] + NEG2_DY[h] for h in hs), [])
            w = WB if all(h in WORLD_B_DYADS for h in hs) else WA
            out.append((w, Part(pos + negs, singles=pos + negs), text))
    return out


def dd_name(word, kind, heads):
    """the name of the dyad / group in a 5-02 part heading"""
    if len(heads) == 1 and kind in ("duka", "dukaṃ"):
        return DUKA_NAME[heads[0]]
    full = word[0].upper() + word[1:] + kind + ("ṃ" if kind.endswith("a") else "")
    full = full.replace("dukaṃṃ", "dukaṃ")
    if full in GNAME:
        return GNAME[full]
    if word.endswith("ādi"):
        base = word[:-3]
        noun = ADI_NOUN[base.lower()]
        return f"{noun} {ADI}တို့၏ {DUKA}" + ("များ" if kind == "dukāni" else "")
    if kind == "duka" and full + "ṃ" in GNAME:
        return GNAME[full + "ṃ"]
    if word.lower() == "piṭṭhi":
        return GNAME["Piṭṭhidukaṃ"]
    raise KeyError(f"group name {word}{kind}")


# ===================================================================================== numbers
_TEEN = WA.G.TEEN
NUM_ADD = {"catuvīsa": (24, _TEEN["catuvīsati"][1]),                       # as 2-12 … 2-17 (1-03 … 1-05 value)
           "ekūnatiṃsa": (29, new("ekūnatiṃsa", "နှစ်ဆယ့်ကိုး")), "tiṃsa": (30, new("tiṃsa", "သုံးဆယ်")),
           "catuttiṃsa": (34, new("catuttiṃsa", "သုံးဆယ့်လေး")), "pañcatiṃsa": (35, new("pañcatiṃsa", "သုံးဆယ့်ငါး")),
           "chattiṃsa": (36, new("chattiṃsa", "သုံးဆယ့်ခြောက်")), "sattatiṃsa": (37, new("sattatiṃsa", "သုံးဆယ့်ခုနစ်"))}


def setup_numbers(mod):
    for w, (n, my) in NUM_ADD.items():
        if w in mod.COUNT:
            assert mod.COUNT[w] == my + "ခု", (w, mod.COUNT[w])
        mod.COUNT.setdefault(w, my + "ခု")
        mod.COUNT_VAL.setdefault(w, n)
        mod.LEX.setdefault(w, (mod.COUNT[w], "x"))
    mod._CNT_ALT = "|".join(sorted(mod.COUNT, key=len, reverse=True))
    mod.COUNT_RE = re.compile(r"(?<![\wāīūṃṅñṭḍṇḷ])(?P<neg>[Nn]a|[Nn]o)?(?P<loc>(?i:" + mod._LOC_ALT + r")) (?P<num>"
                              + mod._CNT_ALT + r")(?![\wāīūṃṅñṭḍṇḷ])")


# ===================================================================================== notes
# The notes of these chapters (none of them is in a finished chapter) are composed from the finished groups' words:
K = WA.K
SAMKH = F.NOTES["(saṃkhittaṃ)"][1:-1]                     # «အကျဉ်းချုပ်»
SABB = K.SABBATTHA                                        # sabbattha «နေရာတိုင်း၌»
VITTH = K.VITTH                                           # vitthāretabbaṃ «အကျယ် ချဲ့ရမည်»
VITTHARO = WA.D.NEW["vitthāro"]                           # vitthāro «အကျယ် ချဲ့ခြင်း» (3-01 … 3-02)
EVAM = K.EVAM                                             # evaṃ (after yathā) «ထိုနည်းတူ»
EVAM_T = WA.M.EVAM_THUS                                   # evaṃ (alone) «ဤသို့» (2-03 … 2-06)
GANETABBA = K.GANETABBA                                   # «ရေတွက်ရမည်»
SADISA = K.SADISA                                         # -sadisaṃ «… နှင့် တူသည်»
NATTHI = K.NATTHI                                         # natthi «မရှိ»
PANHAVARA = F.HEAD["Pañhāvāro"]
KT_L = TIKA_NAME["Kusalattikaṃ"] + "၌"                    # kusalattike «ကုသိုလ် သုံးမျိုးတွဲ၌»
GANITA = "ရေတွက်ထားသည့်အတိုင်း"                          # gaṇitaṃ (yathā … gaṇitaṃ, 1-03 … 1-05)
TUAUNG = "နှင့် တူအောင်"                                  # X-sadisaṃ + verb (2-01 «… နှင့် တူအောင် ပြုရမည်»)
AMASANA = new("āmasanaṃ", "ရည်ညွှန်းပုံ")                   # the way the terms are touched on (NEW)
GOCCHAKA_N = new("gocchakaṃ (the cluster)", "အစု")          # (pi-1 «…တို့၏ အစု»)
VATTABBA_NA = new("na vattabbaṃ", "ခေါ်ဆို၍ မရ")         # pi-1 vattabbaṃ «ခေါ်ဆို၍ ရ»
PURETUM = new("pūretuṃ", "ပြည့်စုံစေရန်")                   # (3-09 pūretukāmena «ပြည့်စုံစေလိုသူသည်»)
KAROTU = new("karotu", "ပြုပါစေ")
MATTA = new("-mattāni (only)", "သာ")
VARA_W = {"paṭicca": "paṭicca", "sahajāta": "sahajāta", "paccaya": "paccaya", "nissaya": "nissaya",
          "saṃsaṭṭha": "saṃsaṭṭha", "sampayutta": "sampayutta", "pañhā": "pañhā"}
_VARA_RX = re.compile(r"^(paṭicca|sahajāta|paccaya|nissaya|saṃsaṭṭha|sampayutta|pañhā)vār(ampi|epi)$")


def _members(seq):
    """«sahajātavārampi…pe… sampayuttavārampi pañhāvārampi» -> [(vara, case)], separators ['…', ' ']"""
    toks = re.split(r"(\s*…\s*|\s+)", seq.strip())
    mem, seps = [], []
    for i, t in enumerate(toks):
        if i % 2:
            seps.append(t)
            continue
        m = _VARA_RX.match(t)
        if not m:
            return None
        mem.append((m[1], m[2]))
    return mem, seps


def _vara_list(mem, seps, role):
    """role: n (nominative «Xလည်း»), a (object «Xကိုလည်း»); a «-vārepi» member is locative «X၌လည်း»"""
    out = []
    for i, (v, c) in enumerate(mem):
        mk = "၌လည်း" if c == "epi" else ("ကိုလည်း" if role == "a" else "လည်း")
        out.append(K.vara(v) + mk)
        if i < len(seps):
            sp = seps[i]
            out.append(sp if "…" in sp else f"{C} ")
    return "".join(out)


_PRED = [   # predicate after a vāra list -> (role of the list, Burmese)
    (r"paṭiccavārasadisaṃ", "n", lambda: f"{K.vara('paṭicca')}{SADISA}"),
    (r"paṭiccavārasadisaṃ vitthāretabbaṃ", "a", lambda: f"{K.vara('paṭicca')}{TUAUNG} {VITTH}"),
    (r"paṭiccavārasadisaṃ evaṃ vitthāretabbaṃ", "a", lambda: f"{K.vara('paṭicca')}{TUAUNG} {EVAM_T} {VITTH}"),
    (r"vitthāretabbaṃ", "a", lambda: VITTH),
    (r"evaṃ vitthāretabbaṃ", "a", lambda: f"{EVAM_T} {VITTH}"),
    (r"sabbattha vitthāro", "n", lambda: f"{SABB} {VITTHARO}"),
    (r"sabbattha vitthāretabbaṃ", "a", lambda: f"{SABB} {VITTH}"),
    (r"sabbattha (\w+)", "n", None),
]


def _clause(c):
    """one clause of a note (lower case, no final «.») -> Burmese, or None"""
    if c == "saṃkhittaṃ":
        return SAMKH
    if c.startswith("saṃkhittaṃ…"):
        r = _clause(c[len("saṃkhittaṃ…"):].strip())
        return None if r is None else f"{SAMKH}… {r}" if c[len("saṃkhittaṃ…"):].startswith(" ") else f"{SAMKH}…{r}"
    if c == "sabbattha vitthāro":
        return f"{SABB} {VITTHARO}"
    if c == "sabbattha vitthāretabbaṃ":
        return f"{SABB} {VITTH}"
    if c == "sabbattha gocchakaṃ vitthāretabbaṃ":
        return f"{SABB} {GOCCHAKA_N}ကို {VITTH}"
    m = re.fullmatch(r"sabbattha (\w+)", c)
    if m and m[1] in F.COUNT:
        return f"{SABB} {F.COUNT[m[1]]}"
    if re.fullmatch(r"\w+", c) and c in F.COUNT:
        return F.COUNT[c]
    if c == "vipākaṃ natthi":
        return f"{F.cname('vipāka')} {NATTHI}"
    if c == "pañhāvārampi evaṃ vitthāretabbaṃ":
        return f"{PANHAVARA}ကိုလည်း {EVAM_T} {VITTH}"
    if c == "evaṃ vitthāretabbaṃ":
        return f"{EVAM_T} {VITTH}"
    m = re.fullmatch(r"(\w+)dukasadisaṃ", c)
    if m:
        h = m[1][0].upper() + m[1][1:] + "dukaṃ"
        return f"{DUKA_NAME[h]}{SADISA}"
    # a list of sections + its predicate
    for rx, role, fn in sorted(_PRED, key=lambda p: -len(p[0])):
        mm = re.fullmatch(r"(.+?) " + rx, c)
        if not mm:
            continue
        lst = _members(mm[1])
        if not lst:
            continue
        if fn is None:
            if mm[2] not in F.COUNT:
                continue
            pred = f"{SABB} {F.COUNT[mm[2]]}"
        else:
            pred = fn()
        return f"{_vara_list(*lst, role)} {pred}"
    return None


ORDERS_A = {"anulomampi": "anulomaṃ", "paccanīyampi": "paccanīyaṃ", "anulomapaccanīyampi": "anulomapaccanīyaṃ",
            "paccanīyānulomampi": "paccanīyānulomaṃ"}


def _sentence(snt):
    """a sentence of a note (lower-case first letter, no final «.») -> Burmese or None"""
    m = re.fullmatch(r"yathā kusalattike pañhāvāraṃ,? evaṃ vitthāretabbaṃ", snt)
    if m:
        return f"{KT_L} {PANHAVARA}အတိုင်း {EVAM} {VITTH}"
    m = re.fullmatch(r"yathā kusalattike pañhāvārassa ((?:\w+ampi )+)gaṇitaṃ evaṃ gaṇetabbaṃ", snt)
    if m:
        ords = [K.ORDER_N[ORDERS_A[w]] + "ကိုလည်း" for w in m[1].split()]
        return f"{KT_L} {PANHAVARA}၏ {(C + ' ').join(ords)} {GANITA} {EVAM} {GANETABBA}"
    m = re.fullmatch(r"yathā kusalattike ((?:\w+vārampi )+)gaṇitaṃ evaṃ gaṇetabbaṃ", snt)
    if m:
        lst = _members(m[1])
        return f"{KT_L} {_vara_list(*lst, 'a')} {GANITA} {EVAM} {GANETABBA}"
    m = re.fullmatch(r"(\w+)gocchaka(\w+)gocchakesu āmasanaṃ (\w+)gocchake āmasanasadisaṃ", snt)
    if m:
        g1, g2, g3 = (GNAME[_GOC[x]] for x in m.groups())
        return f"{g1}နှင့် {g2}တို့၌ {AMASANA}သည် {g3}၌ {AMASANA}{SADISA}"
    m = re.fullmatch(r"(\w+)gocchake āmasanaṃ (\w+)gocchake āmasanasadisaṃ", snt)
    if m:
        g1, g2 = (GNAME[_GOC[x]] for x in m.groups())
        return f"{g1}၌ {AMASANA}သည် {g2}၌ {AMASANA}{SADISA}"
    if snt == "paccanīyadukamattāni na vattabbaṃ dhammaṃ pūretuṃ nava nava pañhāni karotu":
        return (f"{ORDER_N_P} {DUKA}များ{MATTA}{C} {VATTABBA_NA}သော {F.DHAMMA}ကို {PURETUM} "
                f"{K.PANHA} {F.COUNT['nava']} {F.COUNT['nava']}စီကို {KAROTU}")
    # «…, …» clauses
    parts = re.split(r"(, )", snt)
    out = []
    for i, p in enumerate(parts):
        if i % 2:
            out.append(C + " ")
            continue
        r = _clause(p)
        if r is None:
            # a whole sentence «X, evaṃ vitthāretabbaṃ» after a list: «…sadisaṃ, evaṃ vitthāretabbaṃ»
            return None
        out.append(r)
    return "".join(out)


_GOC = {"ogha": "ogha", "yoga": "yoga", "āsava": "asava", "Nīvaraṇa": "Nīvaraṇagocchakaṃ", "nīvaraṇa": "Nīvaraṇagocchakaṃ",
        "saññojana": "sannojana"}
ORDER_N_P = K.ORDER_N["paccanīyaṃ"]


def note_my(note):
    """«(…)» -> «(…)» or None: sentences split at «. », each ending «။» where the Pāli has «.»"""
    inner = note[1:-1]
    body = inner.rstrip()
    trail = inner[len(body):]
    dot = body.endswith(".")
    if dot:
        body = body[:-1]
    body = F.pe(body)
    snts = re.split(r"\. ", body)
    out = []
    for i, snt in enumerate(snts):
        r = _sentence(F.lc(snt.strip()))
        if r is None:
            return None
        out.append(r + (END if (i + 1 < len(snts) or dot) else ""))
    return "(" + " ".join(out) + trail + ")"


NOTE_MINE = collections.OrderedDict()     # note (as written) -> Burmese
NOTE_PH = {}                              # note -> placeholder «(⁑qN)»


def notes_of(text):
    """the notes of a part that the engine does not render: rendered here, replaced by placeholders"""
    for m in re.finditer(r"\([^()]*\)", text):
        k = m[0]
        if re.fullmatch(r"\(\d+\)", k):
            continue
        if k in WA.F.NOTES or F.lc(k) in WA.F.NOTES:
            continue
        r = note_my(k)
        if r is None:
            continue
        if k not in NOTE_MINE:
            NOTE_MINE[k] = r
            NOTE_PH[k] = f"(⁑q{len(NOTE_PH)})"
            for w in (WA, WB):
                w.K.NOTE_FIXED[NOTE_PH[k][1:-1]] = r[1:-1]
                for mod in (w.F, w.FG):
                    mod.NOTES[NOTE_PH[k]] = r
    for k in sorted(NOTE_PH, key=len, reverse=True):
        text = text.replace(k, NOTE_PH[k])
    return text


# 5-04 group headings and the 5-02 colophons of a dyad with a cluster
for _n, _g in (("32-49. Oghādidukāni", "ogh"), ("50-54. Parāmāsādidukāni", "parāmās")):
    hl(_n, f"{_n.split(' ')[0]} {ADI_NOUN[_g]} {ADI}တို့၏ {DUKA}များ")               # as «Ārammaṇādidukāni» (1-01)
hl("69-74. Upādānagocchakaṃ", f"69-74. {GNAME['Upādānagocchakaṃ']}", log=False)
for _g in ("Āsavagocchakaṃ", "Parāmāsagocchakaṃ", "Mahantaradukaṃ", "Piṭṭhidukaṃ"):
    hl(f"Hetuduka{_g[0].lower()}{_g[1:]} niṭṭhitaṃ.", F.finished(f"{DUKA_NAME['Hetudukaṃ']}နှင့် {GNAME[_g]}"))


# ===================================================================================== the run
SLIP_FIX = {         # source slips: Pāli as written -> read as (logged)
    "nanoasaññojano ca": "nano ca saññojano ca",          # (5-04 ^7-58-37; = «nano ca saññojano» of the same dyad)
    "Saññojanavippayutto nasaññojaniyañca": "Saññojanavippayuttaṃ nasaññojaniyañca",   # (5-04 ^7-58-39; the
}                                                           # accusative of the object, as the parallel ^7-58-33 / -45)
# «… uppajjati hetupaccayā ekaṃ.» (a count written after the condition, no «…»): the count follows the verb
# «… ဖြစ်ပေါ်သည် တစ်ခု။» (as «hetupaccayā (ekaṃ).» «… ဖြစ်ပေါ်သည် (တစ်ခု)။», without the brackets the Pāli lacks)
_COUNT_AFTER = re.compile(r"(?<=paccayā) (ekaṃ|dve|tīṇi)(?=\.)")


def set_terms(w, tab):
    for mod in (w.F, w.FG):
        w.D.set_dyad(mod, None)
        mod.TRIADS["pancama"] = tab
        mod.TRIAD_END["pancama"] = w.D._END
        mod.rebuild()


def prep_text(text, part):
    lines = text.split("\n")
    out = []
    for ln in lines:
        if ln.startswith("#") or not ln.strip():
            out.append(ln)
            continue
        for a, b in SLIP_FIX.items():
            if a in ln:
                SLIPS.append(f"«{a}» read as «{b}»")
                ln = ln.replace(a, b)
        ln = _COUNT_AFTER.sub(lambda m: f" (⁑n{m[1]})", ln)
        out.append(rewrite(notes_of(ln), part))
    return "\n".join(out)


def translate_part(w, part, text):
    t = prep_text(text, part)
    tab = {k: m for m, k in KEYS.items()}
    set_terms(w, tab)
    t = w.D.prep(t, None)
    w.D.chapter_notes(t, None)
    w.FG.translate("")
    out = w.F.translate(t)
    out = re.sub(r"\(?⁂(\w+)⁂\)?", lambda m: w.F.COUNT[m[1]], out)       # the bare count (no brackets in the Pāli)
    assert "⁂" not in out and "⁑" not in out and not re.search(r"zqw", out, re.I)
    return out


def translate(name):
    src = (PALI / name).read_text(encoding="utf-8-sig")
    parts = parts_of(name, src)
    for w in (WA, WB):
        for k, v in HL.items():
            w.F.HLINES.setdefault(k, v)
            assert w.F.HLINES[k] == v or k in HL_OVERRIDE, (k, w.F.HLINES[k], v)
    return "\n".join(translate_part(w, p, t) for w, p, t in parts)


HL_OVERRIDE = set()
HL_DIFF_OK = set()


class Counting(dict):
    cnt = collections.Counter()

    def setdefault(self, k, v):
        self.cnt[k] += 1
        return super().setdefault(k, v)


def setup():
    for w in (WA, WB):
        w.K.CUR["fix"] = True
        for c in ("ekaṃ", "dve", "tīṇi"):
            w.K.NOTE_FIXED[f"⁑n{c}"] = f"⁂{c}⁂"
            for mod in (w.F, w.FG):
                mod.NOTES[f"(⁑n{c})"] = f"(⁂{c}⁂)"
    # the headings and colophons of both worlds (the same Burmese where both have them)
    for k, v in list(WB.F.HLINES.items()):
        if k in WA.F.HLINES:
            assert WA.F.HLINES[k] == v or k in HL_DIFF_OK, (k, WA.F.HLINES[k], v)
        WA.F.HLINES.setdefault(k, v)
    for k, v in list(WA.F.HLINES.items()):
        WB.F.HLINES.setdefault(k, v)
    for w in (WA, WB):
        for mod in (w.F, w.FG):
            setup_numbers(mod)


setup()


def main():
    global OUT
    if "--out" in sys.argv:
        OUT = pathlib.Path(sys.argv[sys.argv.index("--out") + 1]).resolve()
        del sys.argv[sys.argv.index("--out"):sys.argv.index("--out") + 2]
    names = [a for a in sys.argv[1:] if not a.startswith("--")] or NAMES
    names = [next(n for n in NAMES if n.startswith(a)) for a in names]
    dev = "--dev" in sys.argv
    for w in (WA, WB):
        w.F.DEV = dev
        if dev:
            w.F.UNSEEN = Counting()
    for n in names:
        txt = translate(n)
        if "--dump" in sys.argv:
            continue
        if not dev:
            (OUT / n).write_text(txt, encoding="utf-8")
            print(f"wrote {n}: {sum(1 for l in txt.splitlines() if l)} lines")
        else:
            CHK.mkdir(exist_ok=True)
            (CHK / ("dev-" + n)).write_text(txt, encoding="utf-8")
    if "--dump" in sys.argv:
        for my, k in KEYS.items():
            print(k, " | ".join(sorted(KEY_PALI[k])), "=", my, sep="\t")
        return
    if dev:
        CHK.mkdir(exist_ok=True)
        with open(CHK / "dev.txt", "w", encoding="utf-8") as fh:
            tot = 0
            for w in (WA, WB):
                rows = sorted(w.F.UNSEEN.items(), key=lambda kv: -w.F.UNSEEN.cnt[kv[0]])
                tot += len(rows)
                for k, v in rows:
                    fh.write(f"[{w.tag} {w.F.UNSEEN.cnt[k]}] SK: {k}\n    {v}\n")
        print(tot, "unmatched skeletons")
    if "--slips" in sys.argv:
        print("slips:", *sorted(set(SLIPS) | WA.F.SLIPS | WB.F.SLIPS), sep="\n  ")


if __name__ == "__main__":
    main()
