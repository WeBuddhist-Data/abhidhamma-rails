"""Burmese zero-shot of pi-7 4-02 … 4-09, the first DUKATIKA chapters of the Paṭṭhāna («အကြောင်းနှင့် အကျိုး
ဆက်စပ်ပုံ»): a dyad combined with a triad on one noun («hetuṃ kusalaṃ dhammaṃ paṭicca …»), from the Pāli only.

usage: python3 -I -X utf8 make_ch4-02-09.py [chapter ...] [--dev] [--slips] [--new] [--out DIR] [--dump]
  (no flag)  translate the chapters and write them; stops on the first unmatched sentence (nothing is guessed).
  --dev      do not stop: list every unmatched skeleton with its count in chk-ch4-02-09/dev.txt (nothing written).
  --dump     print the combined-term table (dyad term + triad term = Burmese) and stop.
  --new      translate without writing and print every new string («Pāli = Burmese») and the readings.

Engines (read-only, imported, never run as scripts; each loaded on its OWN copies of my7_formulas / make_sample):
  * world A = make_ch3-03-06.py (it imports make_ch3-01-02 -> make_ch2-03-06: PRIMARY my7_formulas + make_sample +
    make_ch1-01, FALLBACK per unit make_ch1-03-05), for 4-02 … 4-07 (the 3-01 … 3-06 dyads);
  * world B = make_ch3-07-08-10.py (it imports make_ch3-01-02 the same way), for 4-08 … 4-09 (nīvaraṇa, parāmāsa);
  * value sources only (their tables are read, nothing of them runs on A or B): make_ch2-07-11.py (it imports
    make_ch2-01-02 + make_ch1-03-05: the triads 1-03 … 2-02, 2-07 … 2-11) and make_ch2-12-17.py (2-12 … 2-17).
No main block of another script runs; no file of the sample or of another group is edited or written.

A chapter is cut at its dyad-triad headings («##### 1-1 Hetuduka-kusalattikaṃ» …); in each part a combined term
«<dyad term> <triad term>» is rewritten before slotting into ONE synthetic a-stem term (the ending of the triad
word; for the indeclinable bahiddhā the ending of the dyad word) whose Burmese is the two qualifiers stacked
«<dyad term>၊ <triad term>» (the stacking pattern of 2-01 … 2-02 / 2-07 … 2-11 / 3-01 … 3-02, coordinator); then
the dyad chapters' engine translates the part with only that term table active. Every new string is logged in
notes-ch4-02-09.md.
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
NAMES = ["4-02-dukatika-hetuduka.md", "4-03-dukatika-sahetukaduka.md", "4-04-dukatika-sappaccayaduka.md",
         "4-05-dukatika-asavaduka.md", "4-06-dukatika-sannojanaduka.md", "4-07-dukatika-ganthaduka.md",
         "4-08-dukatika-nivaranaduka.md", "4-09-dukatika-paramasaduka.md"]
CHK = HERE / "chk-ch4-02-09"
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


A = _isolated("w_a_ch30306", "make_ch3-03-06.py")
B = _isolated("w_b_ch3070810", "make_ch3-07-08-10.py")
L = _isolated("v_l_ch20711", "make_ch2-07-11.py")
U = _isolated("v_u_ch21217", "make_ch2-12-17.py")
assert A.F is not B.F and A.M3 is not B.D

NEW = collections.OrderedDict()     # every new string of this script: Pāli -> Burmese
SLIPS = set()


def new(pali, my):
    if pali in NEW:
        assert NEW[pali] == my, (pali, NEW[pali], my)
    NEW.setdefault(pali, my)
    return my


# ===================================================================================== the worlds
class World:
    def __init__(self, tag, mod, d):
        self.tag, self.mod, self.D = tag, mod, d
        self.M = d.M
        self.F, self.FG, self.K, self.G = d.M.F, d.M.FG, d.M.K, d.M.G
        self.DYADS = d.DYADS


WA = World("A", A, A.M3)
WB = World("B", B, B.D)
WORLD_OF = {n: (WB if n.startswith(("4-08", "4-09")) else WA) for n in NAMES}
C, END, PE = WA.F.C, WA.F.END, WA.F.PE
for _w in (WA, WB):
    assert (_w.F.C, _w.F.END, _w.F.PE) == (C, END, PE)

# ===================================================================================== the triads (finished groups)
# triad -> (heading word «Xttikaṃ», {Pāli surface stem: (table key, Burmese)}, stem class)
# stem class: a (a-stem endings), i (-in / -i stem: ī/i/iṃ/issa/iñca), d (indeclinable «bahiddhā»: the dyad's case)
_FT = WA.F.TRIADS
_GT = WA.G.TRIADS_ADD
_MT = WA.M.TRIADS_ADD
_LM = L.M.TRIADS_ADD          # 2-01 … 2-02 (make_ch2-01-02 inside make_ch2-07-11)
_LT = L.TRIADS_ADD            # 2-07 … 2-11
_UT = U.TRIADS_ADD            # 2-12 … 2-17


def _t(tab, key):
    return tab[key]


TRIADS = {
    "Kusalattikaṃ": {"kusal": _t(_FT["kusala"], "kusal"), "akusal": _t(_FT["kusala"], "akusal"),
                     "abyākat": _t(_FT["kusala"], "abyākat")},
    "Vedanāttikaṃ": {"sukhāya vedanāya sampayutt": _t(_FT["vedana"], "sukhāya vedanāya sampayutt"),
                     "dukkhāya vedanāya sampayutt": _t(_FT["vedana"], "dukkhāya vedanāya sampayutt"),
                     "adukkhamasukhāya vedanāya sampayutt": _t(_FT["vedana"], "adukkhamasukhāya vedanāya sampayutt")},
    "Vipākattikaṃ": {"vipāk": _t(_GT["vipaka"], "vipāk"), "vipākadhammadhamm": _t(_GT["vipaka"], "vipākadhammadhamm"),
                     "nevavipākanavipākadhammadhamm": _t(_GT["vipaka"], "nevavipākanavipākadhammadhamm")},
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
    "Parittattikaṃ": {k: _LT["paritt"][k] if False else _LT["paritta"][k] for k in ("paritt", "mahaggat", "appamāṇ")},
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
# stem class of a triad term (default a)
STEM_CLASS = {"ācayagām": "i", "apacayagām": "i", "nevācayagāmināpacayagām": "i", "maggādhipat": "i",
              "uppād": "i", "bahiddh": "d", "ajjhattabahiddh": "d"}
# the triad names (the finished groups' TIKA_NAME)
TIKA_NAME = {}
for _tn in (WA.F.TIKA_NAME, L.F.TIKA_NAME, U.F.TIKA_NAME):
    for _k, _v in _tn.items():
        if _k in TRIADS:
            assert TIKA_NAME.get(_k, _v) == _v, _k
            TIKA_NAME[_k] = _v
assert set(TIKA_NAME) == set(TRIADS), set(TRIADS) - set(TIKA_NAME)

# ===================================================================================== the dyads (finished groups)
# dyad heading «Xdukaṃ» -> [(world dyad key, term key, surface regex)]; {A} a-stem ending, {U} u-stem, {I} i-stem
_EA = r"(?:o|aṃ|añca|assa|ā|ānaṃ|ānañca|e|ena)"
_EU = r"(?:uṃ|ussa|ūnaṃ|uñca|u|ū)"
_EI = r"(?:iṃ|issa|ino|īnaṃ|iñca|ī|i)"
_EV = r"(?:o|a|assa|ā|āna|e)"            # a first member before «ñceva / ceva»
_EC = r"(?:o|a|aṃ|assa|ā|āna|e)"         # a second member before «ñca / ca» (or without it: a slip, logged)
_CEVA = r"(?:ñceva| ceva)"
_CA2 = r"(?:ñca| ca|ca)?"


def _ci(s):
    return f"[{s[0].upper()}{s[0]}]" + re.escape(s[1:])


DYAD_SURF = {
    "Hetudukaṃ": [("hetu", "hetudk", _ci("het") + _EU), ("hetu", "nahetudk", _ci("nahet") + _EU)],
    "Sahetukadukaṃ": [("sahetuka", "sahetuk", _ci("sahetuk") + _EA), ("sahetuka", "ahetuk", _ci("ahetuk") + _EA)],
    "Hetusampayuttadukaṃ": [("hetusamp", "hetusampayutt", _ci("hetusampayutt") + _EA),
                            ("hetusamp", "hetuvippayutt", _ci("hetuvippayutt") + _EA)],
    "Hetusahetukadukaṃ": [
        ("hetusahetuka", "hetusahetukdk", _ci("het") + _EU + _CEVA + " sahetuk" + _EC + _CA2),
        ("hetusahetuka", "sahetukanahetudk", _ci("sahetuk") + _EV + _CEVA + " na ca het" + _EU)],
    "Hetuhetusampayuttadukaṃ": [
        ("hetuhetusamp", "hetuhetusampdk", _ci("het") + _EU + _CEVA + " hetusampayutt" + _EC + _CA2),
        ("hetuhetusamp", "hetusampnahetudk", _ci("hetusampayutt") + _EV + _CEVA + " na ca het" + _EU)],
    "Nahetusahetukadukaṃ": [
        ("nahetusahetuka", "nahetusahetuk", _ci("nahet") + _EU + " sahetuk" + _EA),
        ("nahetusahetuka", "nahetuahetuk", _ci("nahet") + _EU + " ahetuk" + _EA)],
    "Sappaccayadukaṃ": [("sappaccaya", "sappaccay", _ci("sappaccay") + _EA),
                        ("sappaccaya", "appaccay", _ci("appaccay") + _EA)],
    "Saṅkhatadukaṃ": [("sankhata", "saṅkhat", _ci("saṅkhat") + _EA), ("sankhata", "asaṅkhat", _ci("asaṅkhat") + _EA)],
    "Sanidassanadukaṃ": [("sanidassana", "sanidassan", _ci("sanidassan") + _EA),
                         ("sanidassana", "anidassan", _ci("anidassan") + _EA)],
    "Sappaṭighadukaṃ": [("sappatigha", "sappaṭigh", _ci("sappaṭigh") + _EA),
                        ("sappatigha", "appaṭigh", _ci("appaṭigh") + _EA)],
    "Rūpīdukaṃ": [("rupi", "rūpdk", _ci("rūp") + _EI), ("rupi", "arūpdk", _ci("arūp") + _EI)],
    "Lokiyadukaṃ": [("lokiya", "lokiy", _ci("lokiy") + _EA), ("lokiya", "lokuttar", _ci("lokuttar") + _EA)],
    "Kenaciviññeyyadukaṃ": [("kenaci", "kenaci viññeyy", _ci("kenaci viññeyy") + _EA),
                            ("kenaci", "kenaci naviññeyy", _ci("kenaci naviññeyy") + _EA)],
}


def _cluster(head_x, head_s, cl, x, s, a_s, samp, vipp, key_of):
    """the six dyads of a cluster (the pattern of make_ch3-03-06 / make_ch3-07-08-10)"""
    k = key_of
    hx = head_x
    DYAD_SURF[f"{hx}dukaṃ"] = [(k["x"][0], k["x"][1], _ci(x) + _EA), (k["x"][0], k["x"][2], _ci("no" + x) + _EA)]
    DYAD_SURF[f"{head_s}dukaṃ"] = [(k["s"][0], k["s"][1], _ci(s) + _EA), (k["s"][0], k["s"][2], _ci(a_s) + _EA)]
    DYAD_SURF[f"{hx}sampayuttadukaṃ"] = [(k["samp"][0], k["samp"][1], _ci(samp) + _EA),
                                         (k["samp"][0], k["samp"][2], _ci(vipp) + _EA)]
    DYAD_SURF[f"{hx}{s}adukaṃ"] = [
        (k["xs"][0], k["xs"][1], _ci(x) + _EV + _CEVA + " " + re.escape(s) + _EC + _CA2),
        (k["xs"][0], k["xs"][2], _ci(s) + _EV + _CEVA + " no ca " + re.escape(x) + _EA)]
    if "xxs" in k:
        DYAD_SURF[f"{hx}{x}asampayuttadukaṃ"] = [
            (k["xxs"][0], k["xxs"][1], _ci(x) + _EV + _CEVA + " " + re.escape(samp) + _EC + _CA2),
            (k["xxs"][0], k["xxs"][2], _ci(samp) + _EV + _CEVA + " no ca " + re.escape(x) + _EA)]
    DYAD_SURF[f"{hx}vippayutta{s}adukaṃ"] = [
        (k["vs"][0], k["vs"][1], _ci(vipp) + _EA + " " + re.escape(s) + _EA),
        (k["vs"][0], k["vs"][2], _ci(vipp) + _EA + " " + re.escape(a_s) + _EA)]


for _cl, _c in A.CLUSTERS.items():
    if _cl in ("ogha", "yoga"):
        continue
    _x, _s, _as = _c["x"], _c["s"], _c["a_s"]
    _cluster(_x[0].upper() + _x[1:] + "a", _s[0].upper() + _s[1:] + "a", _cl, _x, _s, _as, _x + "asampayutt",
             _x + "avippayutt",
             {"x": (_cl, f"{_x}dk", f"no{_x}"), "s": (_cl + "_s", _s, _as),
              "samp": (_cl + "_samp", f"{_x}asampayutt", f"{_x}avippayutt"),
              "xs": (_cl + "_xs", f"{_x}{_s}dk", f"{_s}no{_x}dk"),
              "xxs": (_cl + "_xxs", f"{_x}{_x}sampdk", f"{_x}sampno{_x}dk"),
              "vs": (_cl + "_vs", f"{_x}vipp{_s}dk", f"{_x}vipp{_as}dk")})
for _g, _x, _s, _as, _n in (("niv", "nīvaraṇ", "nīvaraṇiy", "anīvaraṇiy", (1, 2, 3, 4, 5, 6)),
                             ("par", "parāmās", "parāmaṭṭh", "aparāmaṭṭh", (1, 2, 3, 4, None, 6))):
    _k = {"x": (f"{_g}1", f"{_x}dk", f"no{_x}"), "s": (f"{_g}2", _s, _as),
          "samp": (f"{_g}3", f"{_x}asampayutt", f"{_x}avippayutt"),
          "xs": (f"{_g}4", f"{_x}a{_s}dk", f"{_s}ano{_x}dk"),
          "vs": (f"{_g}6", f"{_x}avipp{_s}", f"{_x}avipp{_as}")}
    if _n[4]:
        _k["xxs"] = (f"{_g}5", f"{_x}a{_x}asampdk", f"{_x}asampno{_x}dk")
    _cluster(_x[0].upper() + _x[1:] + "a", _s[0].upper() + _s[1:] + "a", _g, _x, _s, _as, _x + "asampayutt",
             _x + "avippayutt", _k)


def dyad_world_of(head):
    return WB if head.startswith(("Nīvaraṇ", "Parām")) else WA


def dyad_value(head, tk):
    w = dyad_world_of(head)
    for dk, k, _ in DYAD_SURF[head]:
        if k == tk:
            return w.DYADS[dk][k]
    raise KeyError(tk)


# dyad names: the finished groups' DUKA_NAME
DUKA_NAME = {}
for _dn in (A.M3.DUKA_NAME, A.DUKA_NAME, B.DUKA_NAME):
    for _k, _v in _dn.items():
        assert DUKA_NAME.get(_k, _v) == _v, _k
        DUKA_NAME[_k] = _v
assert all(h in DUKA_NAME for h in DYAD_SURF), [h for h in DYAD_SURF if h not in DUKA_NAME]

# ===================================================================================== combined terms
_CONS = "bcdfghjklmnpqrstvwxz"


def _skey(i):
    s = ""
    i += 1
    while i:
        i, r = divmod(i - 1, len(_CONS))
        s = _CONS[r] + s
    return "zqt" + s


COMBO = {}           # (dyad head, triad head) -> {synthetic key: Burmese}
COMBO_RE = {}        # (dyad head, triad head) -> (regex, {group: (dyad term key, triad term key, key)})
COMBO_PALI = {}      # synthetic key -> (dyad head, dyad term, triad head, triad term)
_T_END = {"a": "(?P<e>o|aṃ|añca|assa|ā|ānaṃ|ānañca|e|ena)",
          "i": "(?P<e>issa|iṃ|iñca|ino|īnaṃ|ī|i)",
          "d": "(?P<e>ā)"}
_I2A = {"issa": "assa", "iṃ": "aṃ", "iñca": "añca", "ino": "ā", "īnaṃ": "ānaṃ", "ī": "o", "i": "o"}
_DYCASE = [("ūnaṃ", "ānaṃ"), ("ānaṃ", "ānaṃ"), ("ussa", "assa"), ("assa", "assa"), ("issa", "assa"), ("uṃ", "aṃ"),
           ("aṃ", "aṃ"), ("iṃ", "aṃ"), ("ū", "ā"), ("ā", "ā"), ("u", "o"), ("o", "o"), ("ī", "o"), ("ino", "ā")]
_N = [0]


def combo(dh, th):
    if (dh, th) in COMBO:
        return COMBO[(dh, th)]
    tab, groups, alts = {}, {}, []
    for dk, dterm, dsurf in DYAD_SURF[dh]:
        dval = dyad_value(dh, dterm)
        for tterm, tval in sorted(TRIADS[th].items(), key=lambda kv: -len(kv[0])):
            key = _skey(_N[0])
            _N[0] += 1
            g = f"g{len(groups)}"
            groups[g] = (dterm, tterm, key)
            tab[key] = f"{dval}{C} {tval}"
            COMBO_PALI[key] = (dh, dterm, th, tterm)
            cls = STEM_CLASS.get(tterm, "a")
            tend = _T_END[cls].replace("(?P<e>", f"(?P<e{g}>")
            alts.append(f"(?P<{g}>(?P<d{g}>{dsurf}) {re.escape(tterm)}{tend})")
    rx = re.compile(_PB + "(?:" + "|".join(alts) + ")" + _NB)
    COMBO[(dh, th)] = tab
    COMBO_RE[(dh, th)] = (rx, groups)
    return tab


def combine(text, dh, th):
    combo(dh, th)
    rx, groups = COMBO_RE[(dh, th)]

    def rep(m):
        g = next(k for k in groups if m.group(k))
        dterm, tterm, key = groups[g]
        e = m.group("e" + g)
        cls = STEM_CLASS.get(tterm, "a")
        if cls == "i":
            e = _I2A[e]
        elif cls == "d":           # «bahiddhā»: the case of the dyad word
            dw = m.group("d" + g)
            e = next(a for s, a in _DYCASE if dw.endswith(s))
        cap = m.group(g)[0].isupper()
        return (key[0].upper() + key[1:] if cap else key) + e
    return rx.sub(rep, text)


# «-dhammadhamma» triad terms hold their noun («hetu vipākadhammadhammo uppajjati»): when no noun and no coordinated
# term follows, the noun is split off after the synthetic term (as make_ch1-03-05 splits «vipākadhamma dhammo»);
# «A-añca B-añca paṭicca» (two such terms, the noun inside the compounds) gets the noun after the last one
DD_TERMS = {"vipākadhammadhamm", "nevavipākanavipākadhammadhamm"}
_KEEP_NEXT = ("ca", "dhamm")
_DD_NOUN = {"o": "ā", "ā": "ā", "aṃ": "aṃ", "assa": "assa"}


def dd_split(text):
    keys = [k for k, v in COMBO_PALI.items() if v[3] in DD_TERMS]
    if not keys:
        return text
    alt = "|".join(f"[{k[0].upper()}{k[0]}]" + re.escape(k[1:]) for k in sorted(keys, key=len, reverse=True))
    # coordinations «X-añca Y-añca» / «X-o ca Y-o ca» not followed by a noun
    text = re.sub(_PB + "((?:(?:" + alt + r")añca ?)+)(?! ?dhamm)", lambda m: m[1].rstrip() + " dhammaṃ" +
                  (" " if m[1].endswith(" ") else ""), text)
    # (the noun of the frame: «X-o ca Y-o ca dhammā», «X-assa ca Y-assa ca dhammassa»)
    text = re.sub(_PB + "((?:(?:" + alt + r")(o|ā|aṃ|assa) ca ?){2,})(?! ?dhamm)",
                  lambda m: m[1].rstrip() + f" dhamm{_DD_NOUN[m[2]]}" + (" " if m[1].endswith(" ") else ""), text)

    def single(m):
        nxt = text[m.end():m.end() + 12].lstrip()
        if nxt.startswith(_KEEP_NEXT):
            return m[0]
        return f"{m[0]} dhamm{m[2]}"
    return re.sub(_PB + "(" + alt + r")(o|aṃ|assa|ā|ānaṃ|e)" + _NB, single, text)


# ===================================================================================== headings and names
PADA = WA.F.PADA
PART_HEAD = re.compile(r"^(#{5,6}) (\d+-\d+\.?) (\S+?)duka-(\S+?)ttikaṃ \^", re.M)


def part_name(dh, th):
    """«Xduka-Yttikaṃ» = «<dyad name>နှင့် <triad name>» (the sample's «Dukaṃ tikañca» «နှစ်မျိုးတွဲနှင့် သုံးမျိုးတွဲ»)"""
    return f"{DUKA_NAME[dh]}နှင့် {TIKA_NAME[th]}"


def _pada_key(tterm):
    s = tterm.replace(" ", "").replace("dhammadhamm", "dhamm")
    s = s[0].upper() + s[1:]
    cls = STEM_CLASS.get(tterm, "a")
    return s + {"a": "a", "i": "i", "d": "ā"}[cls] + "padaṃ"


def heading_lines(w, parts):
    hl = {}
    F = w.F
    hl["Dhammānulome dukatikapaṭṭhānaṃ"] = new("Dhammānulome dukatikapaṭṭhānaṃ",
                                              f"{F.HEAD['Dhammānulome']} {F.DUKA}နှင့် {F.TIKA}တို့၏ {F.TITLE}")
    hl["*Paccayacatukkaṃ*"] = new("Paccayacatukkaṃ", f"*{F.PACCAYA} {F.GROUP['catukka']}*")   # = 1-03 … 1-05
    pv = f"{F.HEAD['Paṭiccavāro']} {F.ADI}"                              # = 3-03 … 3-08 «1-7. Paṭiccavārādi»
    hl["1-6. Paṭiccavārādi"] = f"1-6. {pv}"
    hl["Paṭiccavārādi"] = pv
    hl["*1-7. Paṭiccavārādi*"] = f"*1-7. {pv}*"
    hl["1-2. Kusalākusalapadaṃ"] = "1-2. " + F.heading("Kusalākusalapadaṃ")
    for h, conds in (("*Hetu-ārammaṇapaccayādi*", (("hetu", False), ("ārammaṇa", False))),
                     ("*Nahetu-naārammaṇapaccayādi*", (("hetu", True), ("ārammaṇa", True)))):
        hl[h] = new(h, "*" + F._join_and([F.cond(c, "n", ng) for c, ng in conds]) + f" {F.ADI}*")
    for g, gn in GOC_NAME.items():
        for th in {p[1] for p in parts}:
            hl[f"{g}{th[0].lower()}{th[1:]} niṭṭhitaṃ."] = F.finished(f"{gn}နှင့် {TIKA_NAME[th]}")
    for dh, th, num, _ in parts:
        name = part_name(dh, th)
        hl[f"{num} {dh[:-1]}-{th[0].lower()}{th[1:]}"] = f"{num} {name}"
        new(f"{dh[:-1]}-{th[0].lower()}{th[1:]}", name)
        hl[f"{dh[:-1]}{th[0].lower()}{th[1:]} niṭṭhitaṃ."] = F.finished(name)
        for tterm, tval in TRIADS[th].items():
            hl.setdefault(_pada_key(tterm), f"{tval} {PADA}")
    return hl


def parts_of(src):
    """[(dyad head, triad head, number, text)]: the chapter cut before each dyad-triad heading"""
    ms = list(PART_HEAD.finditer(src))
    if not ms:
        raise SystemExit("no dyad-triad heading")
    out = []
    for i, m in enumerate(ms):
        s = 0 if i == 0 else m.start()
        e = ms[i + 1].start() if i + 1 < len(ms) else len(src)
        dh = m[3] + "dukaṃ"
        th = m[4][0].upper() + m[4][1:] + "ttikaṃ"
        if dh not in DYAD_SURF or th not in TRIADS:
            raise SystemExit(f"unknown part {dh} / {th}")
        out.append((dh, th, m[2], src[s:e]))
    return out


# ===================================================================================== notes and slips
SLIP_FIX = {   # source slips: read as the usual form (logged); the Burmese is that of the usual form
    "nahetu asakkho dhammo": "nahetu asekkho dhammo",
    "Āsavo ceva sāsavoca akusalo": "Āsavo ceva sāsavo ca akusalo",
    "nīvaraṇo ca nīvaraṇiyo ca akusalo": "nīvaraṇo ceva nīvaraṇiyo ca akusalo",
    "kamma nava, vipāke": "kamme nava, vipāke",
    "avigata nava (saṃkhittaṃ)": "avigate nava (saṃkhittaṃ)",
    "(saṃkhittaṃ, anuloma paccanīyaṃ)": "(saṃkhittaṃ, anulomapaccanīyaṃ)",
    "paccanīyānulomampi naṇitaṃ": "paccanīyānulomampi gaṇitaṃ",
    "saṃsaṭṭhavāro sampayuttavāropi": "saṃsaṭṭhavāropi sampayuttavāropi",
    "*Nahetunaārammaṇapaccayādi*": "*Nahetu-naārammaṇapaccayādi*",
    # a second member without its closing «ca» («X-añceva Y-aṃ Z-añca …»): read with it
    "Saññojanañceva saññojanasampayuttaṃ akusalañca": "Saññojanañceva saññojanasampayuttañca akusalañca",
    "Ganthañceva ganthaniyaṃ akusalañca": "Ganthañceva ganthaniyañca akusalañca",
    "Nīvaraṇañceva nīvaraṇiyaṃ akusalañca": "Nīvaraṇañceva nīvaraṇiyañca akusalañca",
    "Parāmāsañceva parāmaṭṭhaṃ akusalañca": "Parāmāsañceva parāmaṭṭhañca akusalañca",
}
READ = {   # readings (not slips; logged): one triad word shared by two dyad terms = the two combined terms
    "Nīvaraṇañca nonīvaraṇañca akusalaṃ dhammaṃ": "Nīvaraṇaṃ akusalañca nonīvaraṇaṃ akusalañca dhammaṃ",
}
READ_LOG = set()
NOTEP = {"A": {}, "B": {}}     # per world: raw Pāli note -> Burmese (placeholders «(⁑k<i>)»)
_NOTE_IDS = {}                 # raw Pāli note -> placeholder index (one index per note, both worlds)

VARA_RE = re.compile(r"(paṭicca|sahajāta|paccaya|nissaya|saṃsaṭṭha|sampayutta|pañhā)vār(opi|ampi|epi)")
_VL = r"(?:(?:paṭicca|sahajāta|paccaya|nissaya|saṃsaṭṭha|sampayutta|pañhā)vār(?:opi|ampi|epi)(?:…| …|…pe…| …pe…)? ?)+"


class S_:
    """the strings of one world (all taken from the finished groups' modules; NEW ones logged)"""

    def __init__(self, w):
        F, K, M, D = w.F, w.K, w.M, w.D
        self.w = w
        self.SAMK = F.NOTES["(saṃkhittaṃ)"][1:-1]
        self.ORD = dict(K.ORDER_N)
        self.SABB = K.SABBATTHA
        self.CNT = F.COUNT
        self.VITTH = K.VITTH
        self.KAT = K.KATABBA
        self.NATTHI = K.NATTHI
        self.SADISA = F.SADISA
        self.SADISANI = K.SADISANI
        self.EVAM = K.EVAM
        self.PATV = F.HEAD["Paṭiccavāro"]
        assert self.PATV == D.PATICCA_V
        self.vara = K.vara
        self.cname = F.cname
        self.DH = F.DHAMMA
        self.SAB = D.SAB
        self.ITARE = D.ITARE
        self.GAMANA = M.GAMANA
        self.AA = F.LEX["ārammaṇādhipati"][0]
        self.SAA = F.LEX["sahajātādhipati"][0]
        self.AUP = F.LEX["anantarūpanissayo"][0]
        self.PUP = F.LEX["pakatūpanissayo"][0]
        self.NALABBH = F.LEX["na labbhati"][0]
        self.SAH_KAMMA = F.LEX["sahajātā"][0] if F.LEX.get("sahajātā", ("",))[0].endswith("ကံ") else "အတူ ပေါ်ပေါက်သည့် ကံ"
        self.KT = TIKA_NAME["Kusalattikaṃ"]
        self.GANITA = WA.G.GANITA
        self.GANETABBA = WA.G.YEND["gaṇetabbaṃ"]
        self.TAUNG = new("X-sadisā vitthāretabbā (like X, to be expanded)", "နှင့် တူအောင်")
        self.LIKE_AS = new("yathā … X-sadisaṃ", "နှင့် တူသည့်အတိုင်း")
        self.CUL = D.GOCCHAKA["Cūḷantaradukaṃ"]
        self.LD = DUKA_NAME["Lokiyadukaṃ"]
        lk, lt = dyad_value("Lokiyadukaṃ", "lokiy"), dyad_value("Lokiyadukaṃ", "lokuttar")
        self.LL = new("lokiyalokuttara (the lokiya dyad named by both terms)",
                      f"{lk[:-len('သော')]}ခြင်းနှင့် {lt[:-len('သော')]}ခြင်း")
        self.LLD = new("lokiyalokuttaraduka", f"{self.LL} {F.DUKA}")
        self.GN = A.GNAME
        self.DUKATIKE = new("imamhi dukatike", f"ဤ {F.DUKA}နှင့် {F.TIKA}၌")
        self.LABBHATI = new("labbhati", "တွေ့ရသည်")                 # = 3-09
        self.MAJJHE3 = new("majjhe tiṇṇaṃ", f"အလယ် {F.COUNT['tīṇi']}၌")
        self.MAJJHIME = new("majjhime (in the middle)", "အလယ်၌")      # (3-05 «majjhe» «အလယ်၌»)
        self.ANTE = new("ante (at the end)", "အဆုံး၌")
        self.LAK = F.LAKAUNG
        self.IMAMPI = new("imampi", "ဤသည်ကိုလည်း")                   # = the sample's «idampi»
        self.NATABBA = new("ñātabbaṃ", "သိရမည်")
        self.TADAR = new("tadārammaṇā (the minds)", "ထိုအာရုံကိုပင် အာရုံပြုသော စိတ်")   # (1-03 … 1-05 tadārammaṇatā)
        self.SADISA_PL = new("sabbattha sadisā (alike everywhere)", "တူကြသည်")

    def term_n(self, th, tterm):
        """a triad term used as a noun («atītampi»): the term + «သဘောတရား» (as 1-01 «abyākataṃ»)"""
        return f"{TRIADS[th][tterm]} {self.DH}"

    def comb_n(self, dh, dterm, th, tterm):
        return f"{dyad_value(dh, dterm)}{C} {TRIADS[th][tterm]} {self.DH}"


_SS = {}


def S(w):
    if w.tag not in _SS:
        _SS[w.tag] = S_(w)
    return _SS[w.tag]


def vara_list(s, txt, obj=False):
    """«Xvāropi Yvāropi…» -> «Xလည်း၊ Yလည်း…»; «Xvārepi …» -> «X၌လည်း …»; obj: the object of a verb
    («… vitthāretabbaṃ»): «Xကိုလည်း၊ Yကိုလည်း…» (harmonise H20, as 2-15, 3-01 … 3-02, 5-01 … 5-04)"""
    out = VARA_RE.sub(lambda m: s.vara(m[1]) + ("၌လည်း" if m[2] == "epi" else "ကိုလည်း" if obj else "လည်း"),
                      txt.strip())
    out = re.sub(r"(?<=လည်း) (?=[^…\s])", C + " ", out)
    return out


def piece(s, p):
    """one comma-free piece of a note (lower-case first letter, no final «.»)"""
    O = s.ORD
    fixed = {
        "saṃkhittaṃ": s.SAMK, "anulomaṃ": O["anulomaṃ"], "paccanīyaṃ": O["paccanīyaṃ"],
        "anulomapaccanīyaṃ": O["anulomapaccanīyaṃ"], "paccanīyānulomaṃ": O["paccanīyānulomaṃ"],
        "sabbe paccayā kātabbā": f"{F_(s).PACCAYA} {s.SAB}ကို {s.KAT}",
        "hetupaccayo natthi": f"{s.cname('hetu')} {s.NATTHI}",
        "pañhāvārepi imesaṃ tiṇṇannaṃ hetupaccayo natthi":
            f"{s.vara('pañhā')}၌လည်း ဤ {s.CNT['tīṇi']}တို့၌ {s.cname('hetu')} {s.NATTHI}",
        "ārammaṇādhipatiyeva": f"{s.AA}သာ",
        "tadārammaṇāyeva labbhanti": f"{s.TADAR}တို့ကိုသာ {s.LABBHATI}",
        "sahajātādhipatiyeva labbhati": f"{s.SAA}ကိုသာ {s.LABBHATI}",
        "ārammaṇādhipati natthi": f"{s.AA} {s.NATTHI}",
        "itare dve anantarūpanissayo pakatūpanissayoyeva": f"{s.ITARE} {s.CNT['dve']}သည် {s.AUP}နှင့် {s.PUP}သာ",
        "sahajātakammameva": f"{s.SAH_KAMMA}သာ",
        "majjhe tiṇṇaṃ sahajātādhipati labbhati": f"{s.MAJJHE3} {s.SAA}ကို {s.LABBHATI}",
        "majjhime ca ante ca ārammaṇādhipati": f"{s.MAJJHIME}{s.LAK}{C} {s.ANTE}{s.LAK} {s.AA}",
        "lokiyalokuttaradukasadisaṃ": f"{s.LLD}{s.SADISA}",
        "lokiyadukasadisaṃ": f"{s.LD}{s.SADISA}",
        "lokiyalokuttaragamanasadisaṃ": f"{s.LL}၏ {s.GAMANA}{s.SADISA}",
        "cūḷantaraduke lokiyadukasadisaṃ": f"{s.CUL}၌ {s.LD}{s.SADISA}",
        "yathā cūḷantaraduke lokiyadukasadisaṃ": f"{s.CUL}၌ {s.LD}{s.LIKE_AS}",
        "sappaccayasadisaṃ vitthāretabbaṃ":
            f"{dyad_value('Sappaccayadukaṃ', 'sappaccay')} {s.DH}{s.TAUNG} {s.VITTH}",
        "ajjhattabahiddhā na labbhanti": f"{s.term_n('Ajjhattattikaṃ', 'ajjhattabahiddh')}များ {s.NALABBH}",
        "appaccayampi asaṅkhatampi sanidassanampi na labbhati":
            (f"{dyad_value('Sappaccayadukaṃ', 'appaccay')} {s.DH}လည်း{C} {dyad_value('Saṅkhatadukaṃ', 'asaṅkhat')} "
             f"{s.DH}လည်း{C} {dyad_value('Sanidassanadukaṃ', 'sanidassan')} {s.DH}လည်း {s.NALABBH}"),
        "kenaci viññeyyaṃ akusalampi kenaci viññeyyaṃ abyākatampi kenaci viññeyyakusalasadisaṃ vitthāretabbaṃ":
            (f"{s.comb_n('Kenaciviññeyyadukaṃ', 'kenaci viññeyy', 'Kusalattikaṃ', 'akusal')}လည်း{C} "
             f"{s.comb_n('Kenaciviññeyyadukaṃ', 'kenaci viññeyy', 'Kusalattikaṃ', 'abyākat')}လည်း "
             f"{s.comb_n('Kenaciviññeyyadukaṃ', 'kenaci viññeyy', 'Kusalattikaṃ', 'kusal')}{s.TAUNG} {s.VITTH}"),
        "oghagocchakampi yogagocchakampi āsavagocchakakusalattikasadisaṃ":
            f"{s.GN['ogha']}လည်း{C} {s.GN['yoga']}လည်း {s.GN['asava']}နှင့် {s.KT}{s.SADISANI}",
        "yathā kusalattike pañhāvārassa anulomampi paccanīyampi anulomapaccanīyampi paccanīyānulomampi gaṇitaṃ, "
        "evaṃ gaṇetabbaṃ":
            (f"{s.KT}၌ {s.vara('pañhā')}၏ " + (C + " ").join(O[k] + "ကိုလည်း" for k in (
                "anulomaṃ", "paccanīyaṃ", "anulomapaccanīyaṃ", "paccanīyānulomaṃ")) + f" {s.GANITA} {s.EVAM} {s.GANETABBA}"),
        "yathā cūḷantaraduke lokiyadukagamanaṃ, evaṃ imampi ñātabbaṃ":
            f"{s.CUL}၌ {s.LD}၏ {s.GAMANA}အတိုင်း {s.IMAMPI} {s.EVAM} {s.NATABBA}",
    }
    p2 = re.sub(r"gaṇitaṃ evaṃ", "gaṇitaṃ, evaṃ", p)       # (no comma: the same Burmese, no comma there)
    if p2 in fixed:
        return fixed[p2]
    m = re.fullmatch(r"sabbattha (\w+)", p)
    if m and m[1] in s.CNT:
        return f"{s.SABB} {s.CNT[m[1]]}"
    m = re.fullmatch(r"imamhi dukatike (" + _VL + r")(\w+?)(?:mpi|pi) (\w+?)(?:mpi|pi) natthi", p)
    if m:
        th = {"anuppanna": "Uppannattikaṃ", "uppādī": "Uppannattikaṃ", "atīta": "Atītattikaṃ",
              "anāgata": "Atītattikaṃ"}
        tk = {"anuppanna": "anuppann", "uppādī": "uppād", "atīta": "atīt", "anāgata": "anāgat"}
        a, b = m[2], m[3]
        if a in th and b in th:
            return (f"{s.DUKATIKE} {vara_list(s, m[1])}{C} {s.term_n(th[a], tk[a])}လည်း{C} "
                    f"{s.term_n(th[b], tk[b])}လည်း {s.NATTHI}")
    m = re.fullmatch("(" + _VL + r")(.+)", p)
    if m:
        lst, pred = m[1], m[2]
        loc = "vārepi" in lst
        L_ = vara_list(s, lst, obj=not loc and "vitthāret" in pred)      # harmonise H20
        preds_nom = {
            "vitthāretabbā": s.VITTH, "vitthāretabbo": s.VITTH, "vitthāretabbaṃ": s.VITTH,
            "sabbattha vitthāretabbo": f"{s.SABB} {s.VITTH}", "sabbattha vitthāretabbā": f"{s.SABB} {s.VITTH}",
            "paṭiccavārasadisā": f"{s.PATV}{s.SADISANI}", "paṭiccavārasadisaṃ": f"{s.PATV}{s.SADISA}",   # H24: -sadisaṃ «တူသည်»
            "paṭiccavārasadisā vitthāretabbā": f"{s.PATV}{s.TAUNG} {s.VITTH}",
            "paṭiccavārasadisaṃ vitthāretabbaṃ": f"{s.PATV}{s.TAUNG} {s.VITTH}",
            "sabbattha sadisā": f"{s.SABB} {s.SADISA_PL}",
        }
        preds_loc = {"sabbattha vitthāretabbaṃ": f"{s.SABB} {s.VITTH}"}
        for k, v in s.CNT.items():
            preds_loc[f"sabbattha {k}"] = f"{s.SABB} {v}"
        tab = preds_loc if loc else preds_nom
        if pred in tab and all(("epi" in x) == loc for x in VARA_RE.findall(lst) for x in [x[1]]):
            return f"{L_} {tab[pred]}"
    return None


def F_(s):
    return s.w.F


def note_my(w, note):
    """a whole note «(…)» -> Burmese, or None (then the engine's own frames take it)"""
    s = S(w)
    inner = w.F.pe(note[1:-1])
    sents = re.split(r"(?<=\.) +(?=\S)", inner.strip())
    out = []
    for sent in sents:
        dot = sent.endswith(".")
        body = sent[:-1] if dot else sent
        body = body.strip()
        body = body[0].lower() + body[1:] if body else body
        r = piece(s, body)
        if r is None and ", " in body:
            ps = [piece(s, x.strip()) for x in body.split(", ")]
            r = None if None in ps else (C + " ").join(ps)
        if r is None:
            return None
        out.append(r + (END if dot else ""))
    lead = " " if note[1:2] == " " else ""
    return "(" + lead + " ".join(out) + ")"


NOTE_RX = re.compile(r"\([^()]*\)")


def register_notes(w, text):
    """every note of a part that the engine has no entry for and that note_my() renders: a placeholder"""
    for m in NOTE_RX.finditer(re.sub(r"\{[^{}]*\}", "", text)):
        k = m[0]
        if re.fullmatch(r"\(\d+\)", k) or k in NOTEP[w.tag]:
            continue
        if k in w.F.NOTES or w.F.lc(k) in w.F.NOTES:
            continue
        my = note_my(w, k)
        if my is None:
            continue
        i = _NOTE_IDS.setdefault(k, len(_NOTE_IDS))
        NOTEP[w.tag][k] = my
        new(k, my) if k not in NEW else None
        w.K.NOTE_FIXED[f"⁑k{i}"] = my[1:-1]
        for mod in (w.F, w.FG):
            mod.NOTES[f"(⁑k{i})"] = my


def prep(w, text, dh, th):
    for a, b in SLIP_FIX.items():
        if a in text and a != b:
            SLIPS.add(f"«{a}» read as «{b}»")
            text = text.replace(a, b)
    for a, b in READ.items():
        if a in text:
            READ_LOG.add(f"«{a}» read as «{b}»")
            text = text.replace(a, b)
    register_notes(w, text)
    for k in sorted(NOTEP[w.tag], key=len, reverse=True):
        text = text.replace(k, f"(⁑k{_NOTE_IDS[k]})")
    text = combine(text, dh, th)
    text = dd_split(text)
    return text


# ===================================================================================== the run
def set_terms(w, tab):
    for mod in (w.F, w.FG):
        w.D.set_dyad(mod, None)
        mod.TRIADS["dukatika"] = tab
        mod.TRIAD_END["dukatika"] = w.D._END
        mod.rebuild()


def translate_part(w, dh, th, text):
    tab = combo(dh, th)
    t = prep(w, text, dh, th)
    set_terms(w, tab)
    t = w.D.prep(t, None)
    w.D.chapter_notes(t, None)
    w.FG.translate("")
    return w.F.translate(t)


def translate(name):
    w = WORLD_OF[name]
    src = (PALI / name).read_text(encoding="utf-8-sig")
    parts = parts_of(src)
    w.F.HLINES.update(heading_lines(w, parts))
    return "\n".join(translate_part(w, dh, th, t) for dh, th, _, t in parts)


class Counting(dict):
    cnt = collections.Counter()

    def setdefault(self, k, v):
        self.cnt[k] += 1
        return super().setdefault(k, v)


# a bare locative ending a counting fragment before «…» («…, kamme…pe… magge cattāri», «nakamme…pe… namagge
# ekaṃ»): the condition in the locative alone, as the Pāli (its count is left out with the «…pe…»)
def _install_chain(mod):
    prev = mod.chain

    def chain(s, slots, ci, ki, di, vi=None):
        try:
            return prev(s, slots, ci, ki, di, vi)
        except KeyError:
            pass
        loc = r"(?:[Nn]a|[Nn]o)?(?:" + mod._LOC_ALT + ")"
        m = re.search(r"(?:(?<=, )|^)((?:" + loc + " )*" + loc + r")(\s*)$", s)
        if not m:
            raise KeyError("chain: " + s)
        out = []
        for wd in m[1].split():
            neg = bool(re.match(r"(?i)n[ao]", wd)) and wd.lower()[2:] in mod.LOC2STEM
            lw = wd.lower()[2:] if neg else wd.lower()
            out.append(mod.cond(mod.LOC2STEM[lw], "loc", neg))
        k = "\u0004L4\u0004"
        mod.NOTES[k] = (C + " ").join(out)        # a run of them: joined by «၊» (as make_ch2-03-06 runs)
        try:
            return prev(s[:m.start()] + k + m[2], slots, ci, ki, di, vi)
        finally:
            mod.NOTES.pop(k, None)
    mod.chain = chain


GOC_NAME = {}        # «Xgocchaka» (in «XgocchakaYttikaṃ niṭṭhitaṃ.») -> the cluster name (finished groups)


def setup():
    for k, v in A.GNAME.items():
        GOC_NAME[A.CLUSTERS[k]["head"][:-1]] = v
    for k, v in B.GOCCHAKA.items():
        GOC_NAME[k[:-1]] = v
    for w in (WA, WB):
        w.K.CUR["fix"] = True
        _install_chain(w.F)
        _install_chain(w.FG)
        s = S(w)
        for pali in ("Cūḷantaraduke lokiyadukasadisaṃ.",):
            key = w.D._key(pali, None)
            my = piece(s, pali[0].lower() + pali[1:-1]) + END
            new(pali, my)
            for mod in (w.F, w.FG):
                mod.SK[key] = my


setup()


def main():
    global OUT
    if "--out" in sys.argv:
        OUT = pathlib.Path(sys.argv[sys.argv.index("--out") + 1]).resolve()
        del sys.argv[sys.argv.index("--out"):sys.argv.index("--out") + 2]
    names = [a for a in sys.argv[1:] if not a.startswith("--")] or NAMES
    if "--dump" in sys.argv:
        for n in names:
            for dh, th, _, _ in parts_of((PALI / n).read_text(encoding="utf-8-sig")):
                for k, v in combo(dh, th).items():
                    print(n, k, COMBO_PALI[k], v, sep="\t")
        return
    dev = "--dev" in sys.argv or "--new" in sys.argv
    for w in (WA, WB):
        w.F.DEV = dev
        if dev:
            w.F.UNSEEN = Counting()
    for n in names:
        txt = translate(n)
        if not dev:
            (OUT / n).write_text(txt, encoding="utf-8")
            print(f"wrote {n}: {sum(1 for l in txt.splitlines() if l)} lines")
        else:
            CHK.mkdir(exist_ok=True)
            (CHK / ("dev-" + n)).write_text(txt, encoding="utf-8")
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
    if "--new" in sys.argv:
        for k, v in NEW.items():
            print(f"{k} = {v}")
        print("readings:", *sorted(READ_LOG), sep="\n  ")
    if "--slips" in sys.argv:
        print("slips:", *sorted(SLIPS | WA.F.SLIPS | WB.F.SLIPS), sep="\n  ")


if __name__ == "__main__":
    main()
