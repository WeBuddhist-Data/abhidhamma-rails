"""Burmese zero-shot of pi-7 3-03 āsavagocchaka, 3-04 saññojanagocchaka, 3-05 ganthagocchaka and 3-06
oghayogagocchaka (dyad chapters of the Dukapaṭṭhāna, «အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ»), from the Pāli only.

usage: python3 -I -X utf8 make_ch3-03-06.py [chapter ...] [--dev] [--regress] [--slips] [--out DIR]
  (no flag)  translate the chapters and write them; stops on the first unmatched sentence (nothing is guessed).
  --dev      do not stop: list every unmatched skeleton with its count in chk-ch3-03-06/dev.txt (nothing written).
  --regress  regenerate the approved sample (1-00, 1-02), 2-03 … 2-06 and 3-01 … 3-02 in memory through this script
             and compare them with the published files (they must be identical).

Engines (read-only, imported, never run as scripts): make_ch3-01-02.py is IMPORTED (it imports make_ch2-03-06.py:
PRIMARY my7_formulas + make_sample + make_ch1-01, FALLBACK per unit make_ch1-03-05) with its dyad machinery (the
chapter cut at its dyad headings, only that dyad active, pseudo a-stem terms, both-members slot, notes, lexicon).
No main block of another script runs; no file of the sample or of another group is edited. This script adds the
āsava / saṃyojana / gantha / ogha / yoga dyads (pi-1 final Mātikā ^1-M2-14 … ^1-M2-43), their names and nouns,
notes and unique sentences; every new string is logged in notes-ch3-03-06.md.

The six dyads of a cluster X (X = āsava, saññojana, gantha; ogha, yoga in 3-06) are built from one table:
  X / no X; S / a-S (S = sāsava, saññojaniya, ganthaniya); X-sampayutta / X-vippayutta; «X ceva S ca» /
  «S ceva no ca X»; «X ceva X-sampayutta ca» / «X-sampayutta ceva no ca X»; «X-vippayutta S» / «X-vippayutta a-S».
«X» is a dyad term only before a dhamma word (or coordinated with «no X» before one); otherwise it is the noun
(«āsave paṭicca sampayuttakā khandhā»), as make_ch3-01-02 reads hetu.
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
NAMES = ["3-03-asavagocchaka.md", "3-04-sannojanagocchaka.md", "3-05-ganthagocchaka.md", "3-06-oghayogagocchaka.md"]
CHK = HERE / "chk-ch3-03-06"
WCH = r"[\wāīūṃṅñṭḍṇḷ]"
_NB = r"(?!" + WCH + ")"
_PB = r"(?<!" + WCH + ")"


def _load(name, fn):
    spec = importlib.util.spec_from_file_location(name, HERE / fn)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


M3 = _load("ch30102", "make_ch3-01-02.py")         # its setup() runs on import; its main() does not
M = M3.M
F, FG, G, K, S = M.F, M.FG, M.G, M.K, M.S
C, END, PE, W = F.C, F.END, F.PE, F.W
DUKA = F.DUKA
NEW = collections.OrderedDict()                    # every new string of this script: Pāli -> Burmese


def new(pali, my):
    NEW.setdefault(pali, my)
    return my


# ===================================================================================== the clusters (pi-1 final)
_PL = " သဘောတရားများ"


def _dw(pali, my, bid):
    return W(pali, my + _PL, "1", bid)[:-len(_PL)]


# cluster: pi-7 stem X, pi-7 stem S (the «object of X» term), pi-1 Pāli X / S / a-S (plural), the noun, the Mātikā
# number of the first dyad, the cluster heading (pi-7 spelling, pi-1 spelling, bid)
CLUSTERS = {
    "asava": dict(x="āsav", s="sāsav", a_s="anāsav", px="āsavā", ps="sāsavā", pas="anāsavā", m=14,
                  head="Āsavagocchakaṃ", phead="Āsavagocchakaṃ", hb="^1-M-2-3-0"),
    "sannojana": dict(x="saññojan", s="saññojaniy", a_s="asaññojaniy", px="saṃyojanā", ps="saṃyojaniyā",
                      pas="asaṃyojaniyā", m=20, head="Saññojanagocchakaṃ", phead="Saṃyojanagocchakaṃ",
                      hb="^1-M-2-4-0"),
    "gantha": dict(x="ganth", s="ganthaniy", a_s="aganthaniy", px="ganthā", ps="ganthaniyā", pas="aganthaniyā", m=26,
                   head="Ganthagocchakaṃ", phead="Ganthagocchakaṃ", hb="^1-M-2-5-0"),
    "ogha": dict(x="ogh", s="oghaniy", a_s="anoghaniy", px="oghā", ps="oghaniyā", pas="anoghaniyā", m=32,
                 head="Oghagocchakaṃ", phead="Oghagocchakaṃ", hb="^1-M-2-6-0"),
    "yoga": dict(x="yog", s="yoganiy", a_s="ayoganiy", px="yogā", ps="yoganiyā", pas="ayoganiyā", m=38,
                 head="Yogagocchakaṃ", phead="Yogagocchakaṃ", hb="^1-M-2-7-0"),
}
NOUN_OF = {}            # cluster -> the Burmese noun (pi-1: «စိတ်အစွန်းအထင်း» …)
GNAME = {}              # cluster -> the cluster name (pi-1 heading)
DYADS = {}              # dyad -> {stem key: Burmese attributive}
DYAD_OF = {}            # dyad heading -> dyad
DUKA_NAME = {}          # dyad heading -> Burmese name
DYAD_CL = {}            # dyad -> (cluster, kind)
_NOUN_W = {"asava": ("āsavā", "စိတ်အစွန်းအထင်း"), "sannojana": ("saṃyojanā", "နှောင်ကြိုး"),
           "gantha": ("ganthā", "အထုံး"), "ogha": ("oghā", "ရေအလျဉ်"), "yoga": ("yogā", "ထမ်းပိုး")}


def _cap(s):
    return s[0].upper() + s[1:]


def build():
    for cl, c in CLUSTERS.items():
        n = c["m"]
        b = [f"^1-M2-{n + i}" for i in range(6)]
        px, ps, pas = c["px"], c["ps"], c["pas"]
        NOUN_OF[cl] = N_ = W(_NOUN_W[cl][0], _NOUN_W[cl][1], "1", b[0])
        GNAME[cl] = W(c["phead"], f"{N_}တို့၏ အစု", "1", c["hb"])
        x, s, a_s = c["x"], c["s"], c["a_s"]
        xs = x[:-0] if False else x
        t_x = _dw(f"{px} dhammā", f"{N_} ဖြစ်သော", b[0])
        t_nox = _dw(f"no {px} dhammā", f"{N_} မဟုတ်သော", b[0])
        t_s = _dw(f"{ps} dhammā", f"{N_}၏ အာရုံ ဖြစ်နိုင်သော", b[1])
        t_as = _dw(f"{pas} dhammā", f"{N_}၏ အာရုံ မဖြစ်နိုင်သော", b[1])
        px_st = px[:-1]                                   # pi-1 stem «āsav» / «saṃyojan»
        t_samp = _dw(f"{px_st}asampayuttā dhammā", f"{N_}နှင့် ယှဉ်တွဲသော", b[2])
        t_vipp = _dw(f"{px_st}avippayuttā dhammā", f"{N_}နှင့် ကင်းကွာသော", b[2])
        t_xs = _dw(f"{px} ceva dhammā {ps} ca", f"{N_}လည်း ဖြစ်၊ {N_}၏ အာရုံလည်း ဖြစ်နိုင်သော", b[3])
        t_snox = _dw(f"{ps} ceva dhammā no ca {px}", f"{N_}၏ အာရုံ ဖြစ်နိုင်သော်လည်း {N_} မဟုတ်သော", b[3])
        t_xxs = _dw(f"{px} ceva dhammā {px_st}asampayuttā ca", f"{N_}လည်း ဖြစ်၊ {N_}နှင့်လည်း ယှဉ်တွဲသော", b[4])
        t_xsnox = _dw(f"{px_st}asampayuttā ceva dhammā no ca {px}", f"{N_}နှင့် ယှဉ်တွဲသော်လည်း {N_} မဟုတ်သော",
                      b[4])
        W(f"{px_st}avippayuttā kho pana dhammā {ps}pi", f"{N_}နှင့် ကင်းကွာသော သဘောတရားများအနက် {N_}၏ အာရုံ "
          "ဖြစ်နိုင်သည်တို့လည်း", "1", b[5])
        # ^1-M2-19 … is not attributive in pi-1: the two terms are built from the pi-1 words in the pattern of
        # 3-01's «nahetu sahetuko» «အမြစ် မဟုတ်သော်လည်း အမြစ် ရှိသော» / «nahetu ahetuko» «အမြစ် မဟုတ်၊ အမြစ် မရှိသော»
        t_vs = new(f"{x}avippayutto {s}o (dyad term)", f"{N_}နှင့် ကင်းကွာသော်လည်း {N_}၏ အာရုံ ဖြစ်နိုင်သော")
        t_vas = new(f"{x}avippayutto {a_s}o (dyad term)", f"{N_}နှင့် ကင်းကွာ၊ {N_}၏ အာရုံ မဖြစ်နိုင်သော")
        DYADS[cl] = {f"{x}dk": t_x, f"no{x}": t_nox}
        DYADS[cl + "_s"] = {s: t_s, a_s: t_as}
        DYADS[cl + "_samp"] = {f"{x}asampayutt": t_samp, f"{x}avippayutt": t_vipp}
        DYADS[cl + "_xs"] = {f"{x}{s}dk": t_xs, f"{s}no{x}dk": t_snox}
        DYADS[cl + "_xxs"] = {f"{x}{x}sampdk": t_xxs, f"{x}sampno{x}dk": t_xsnox}
        DYADS[cl + "_vs"] = {f"{x}vipp{s}dk": t_vs, f"{x}vipp{a_s}dk": t_vas}
        for k, kind in (("", "x"), ("_s", "s"), ("_samp", "samp"), ("_xs", "xs"), ("_xxs", "xxs"), ("_vs", "vs")):
            DYAD_CL[cl + k] = (cl, kind)
        hx, hs = _cap(x) + "a", _cap(s) + "a"
        heads = {f"{hx}dukaṃ": (cl, f"{N_} {DUKA}"),
                 f"{hs}dukaṃ": (cl + "_s", f"{N_}၏ အာရုံ ဖြစ်နိုင်ခြင်း {DUKA}"),
                 f"{hx}sampayuttadukaṃ": (cl + "_samp", f"{N_}နှင့် ယှဉ်တွဲခြင်း {DUKA}"),
                 f"{hx}{s}adukaṃ": (cl + "_xs", f"{N_} ဖြစ်ခြင်းနှင့် {N_}၏ အာရုံ ဖြစ်နိုင်ခြင်း {DUKA}"),
                 f"{hx}{x}asampayuttadukaṃ": (cl + "_xxs", f"{N_} ဖြစ်ခြင်းနှင့် {N_}နှင့် ယှဉ်တွဲခြင်း {DUKA}"),
                 f"{hx}vippayutta{s}adukaṃ": (cl + "_vs", f"{N_}နှင့် ကင်းကွာခြင်းနှင့် {N_}၏ အာရုံ ဖြစ်နိုင်ခြင်း "
                                                          f"{DUKA}")}
        for h, (d, my) in heads.items():
            DYAD_OF[h] = d
            DUKA_NAME[h] = new(h, my)
    for _d, _tab in DYADS.items():
        _a, _b = list(_tab)
        _tab[_a + "_" + _b.replace(" ", "_") + "_both"] = f"{_tab[_a]}{C} {_tab[_b]}"


build()
M3.DYADS.update(DYADS)
M3.DYAD_OF.update(DYAD_OF)
M3.DUKA_NAME.update(DUKA_NAME)          # (the module's own dict: names inside notes)
_END = M3._END


# ===================================================================================== Pāli preparation (in memory)
_A = r"(o|aṃ|añca|assa|ā|ānaṃ|ānañca|e|ena)"
_A1 = {"o": "o", "aṃ": "aṃ", "añca": "añca", "assa": "assa", "ā": "ā", "ānaṃ": "ānaṃ", "ānañca": "ānañca", "e": "e",
       "ena": "ena", "a": "aṃ", "āna": "ānaṃ"}
_PREP_ORIG = M3.prep_dyad


def _ci(stem):
    return f"[{stem[0].upper()}{stem[0]}]" + re.escape(stem[1:])


def prep_dyad(t, d):
    if d not in DYAD_CL:
        return _PREP_ORIG(t, d)
    cl, kind = DYAD_CL[d]
    c = CLUSTERS[cl]
    x, s, a_s = c["x"], c["s"], c["a_s"]
    t = _GANTH2.sub(r"\1akāyagant\2", t)
    # «Y ca X-sampayuttakā ca khandhā» = «Y ca X-sampayuttakā khandhā ca» (as make_ch3-01-02's «sampayuttakā ca»)
    t = re.sub(r"(?<=ca) (" + re.escape(x) + r"asampayuttak(?:ā|e)) ca (khandh(?:ā|e))" + _NB, r" \1 \2 ca", t)

    def keep(m, stem):
        w = m[0]
        return (stem[0].upper() if w[0].isupper() else stem[0]) + stem[1:]

    if kind == "x":
        # X as a term: before a dhamma word, or coordinated with «no X» before one
        # (also before the noun «hetū»: «ganthā hetū», «ganthā ca noganthā ca hetū» = the roots that are X / not X)
        t = re.sub(_PB + "(" + _ci(x) + ")" + _A + r"(?= (?:ca )?(?:[Nn]o" + re.escape(x) + r"\w*(?: ca)? )?(?:dhamm|…|hetū"
                   + _NB + "))", lambda m: keep(m, x + "dk") + m[2], t)
    elif kind == "samp":
        # «X-sampayuttaka» (khandhā, cetanā …) = the term X-sampayutta on that noun
        t = re.sub(_PB + "(" + _ci(x + "asampayutt") + ")ak" + _A + _NB, lambda m: m[1] + m[2], t)
    elif kind == "xs":
        t = re.sub(_PB + _ci(s) + r"(o|a|aṃ|assa|ā|āna|e)(?:ñceva| ceva) no ca " + re.escape(x) + _A + _NB,
                   lambda m: keep(m, f"{s}no{x}dk") + m[2], t)
        t = re.sub(_PB + _ci(x) + r"\w*?(?:ñceva| ceva) " + re.escape(s) + r"(o|a|assa|ā|āna|e)(?:ñca| ca)" + _NB,
                   lambda m: keep(m, f"{x}{s}dk") + _A1[m[1]], t)
        t = M3._pairfix(t, f"{x}{s}dk", f"{s}no{x}dk")
    elif kind == "xxs":
        t = re.sub(_PB + _ci(x + "asampayutt") + r"(o|a|aṃ|assa|ā|āna|e)(?:ñceva| ceva) no ca " + re.escape(x) + _A
                   + _NB, lambda m: keep(m, f"{x}sampno{x}dk") + m[2], t)
        t = re.sub(_PB + _ci(x) + r"\w*?(?:ñceva| ceva) " + re.escape(x) + r"asampayutt(o|a|assa|ā|āna|e)(?:ñca| ca)"
                   + _NB, lambda m: keep(m, f"{x}{x}sampdk") + _A1[m[1]], t)
        t = M3._pairfix(t, f"{x}{x}sampdk", f"{x}sampno{x}dk")
    elif kind == "vs":
        t = re.sub(_PB + _ci(x + "avippayutt") + r"(?:o|aṃ|añca|assa|ā|ānaṃ|ānañca|e|a) ?(" + re.escape(s) + "|"
                   + re.escape(a_s) + ")" + _A + _NB,
                   lambda m: keep(m, f"{x}vipp{m[1]}dk") + m[2], t)
    if kind != "x":
        # «X-ā hetū» in the other dyads: X qualifies the noun hetū (the Burmese of the term X)
        t = re.sub(_PB + "(" + _ci(x) + r")ā hetū" + _NB, lambda m: keep(m, x + "aq") + " hetū", t)
    return _PREP_ORIG(t, d)


M3.prep_dyad = prep_dyad


# the 3-06 chapter has no single dyad heading: it is cut before its two sentences (ogha, yoga)
def parts_of(src):
    if "Oghayogagocchakaṃ" in src:
        i = src.index("Oghaṃ dhammaṃ")
        j = src.index("Yogaṃ dhammaṃ")
        return [("ogha", src[:i]), ("ogha", src[i:j]), ("yoga", src[j:])]
    return _PARTS_ORIG(src)


_PARTS_ORIG = M3.parts_of
M3.parts_of = parts_of


# ===================================================================================== names and headings
def setup_names():
    hl = {}
    for cl in CLUSTERS:
        hl[CLUSTERS[cl]["head"]] = GNAME[cl]
        hl[f"{CLUSTERS[cl]['head']} niṭṭhitaṃ."] = F.finished(GNAME[cl])
    hl.update(DUKA_NAME)
    for k, v in DUKA_NAME.items():
        hl[f"{k} niṭṭhitaṃ."] = F.finished(v)
    og = new("Oghayogagocchakaṃ", f"{GNAME['ogha']}နှင့် {GNAME['yoga']}")
    hl["6-7. Oghayogagocchakaṃ"] = f"6-7. {og}"
    hl["Oghayogagocchakaṃ niṭṭhitaṃ."] = F.finished(og)
    hl["1-4. Paccayānulomādi"] = F.HLINES["*1-4. Paccayānulomādi*"][1:-1]
    hl["1-7. Paṭiccavārādi"] = f"1-7. {M3.PATICCA_V} {F.ADI}"
    hl["1-7. Vārasattakaṃ"] = f"1-7. {M3.NEW['vārā (sections)']} ခုနစ်မျိုးတွဲ"
    hl["1-4. Paccayacatukkaṃ"] = f"1-4. {F.PACCAYA} လေးမျိုးတွဲ"
    for k in ("1-7. Paṭiccavārādi", "1-7. Vārasattakaṃ", "1-4. Paccayacatukkaṃ"):
        new(k, hl[k])
    hl["32-43. Oghādidukāni"] = "32-43. " + new("Oghādidukāni", f"{NOUN_OF['ogha']} {F.ADI}တို့၏ {DUKA}များ")
    F.HLINES.update(hl)
    for k, v in DUKA_NAME.items():              # a dyad named inside a note («yathā āsavadukaṃ»)
        K.WORDS_N.setdefault(k[0].lower() + k[1:], v)


# ===================================================================================== nouns
_MASC = {"o": ("n", False, "n"), "ā": ("n", True, "n"), "aṃ": ("a", False, "a"), "e": ("a", True, "a"),
         "assa": ("g", False, "g"), "ānaṃ": ("g", True, "g")}
_NEUT = {"o": ("n", False, "n"), "aṃ": ("n", False, "na"), "ā": ("n", True, "n"), "āni": ("n", True, "na"), "e": ("a", True, "a"),
         "assa": ("g", False, "g"), "ānaṃ": ("g", True, "g")}
NAMES_N = collections.OrderedDict()     # pi-7 stem -> Burmese (the members of the clusters; pi-1 termbase / rails)


def _names():
    a = NOUN_OF["asava"]
    sj = NOUN_OF["sannojana"]
    kg = W("kāyagantho", "ကိုယ် အထုံး", "1")
    sbp = W("sīlabbataparāmāso", "သီလ အကျင့်ဝတ်ဆိုင်ရာ မှားယွင်းသော ယူဆမှု", "1")
    t = {
        # āsava (pi-1 ^1-1102 …: «kāmāsavo» «ကာမ စိတ်အစွန်းအထင်း» …)
        "kāmāsav": W("kāmāsavo", f"ကာမ {a}", "1"), "bhavāsav": W("bhavāsavo", f"ဘဝ {a}", "1"),
        "diṭṭhāsav": W("diṭṭhāsavo", f"အယူ {a}", "1"), "avijjāsav": W("avijjāsavo", f"အမှန်ကို မသိမှု {a}", "1"),
        # saṃyojana (pi-1 spelling saṃyojana; pi-7 saññojana)
        "kāmarāgasaññojan": W("kāmarāgasaṃyojanaṃ", f"ကာမရာဂ {sj}", "1"),
        "paṭighasaññojan": W("paṭighasaṃyojanaṃ", f"မုန်းတီးမှု {sj}", "1"),
        "mānasaññojan": W("mānasaṃyojanaṃ", f"မာန {sj}", "1"),
        "diṭṭhisaññojan": W("diṭṭhisaṃyojanaṃ", f"အယူ {sj}", "1"),
        "vicikicchāsaññojan": W("vicikicchāsaṃyojanaṃ", f"ယုံမှားမှု {sj}", "1"),
        "sīlabbataparāmāsasaññojan": W("sīlabbataparāmāsasaṃyojanaṃ", f"{sbp} {sj}", "1"),
        "bhavarāgasaññojan": W("bhavarāgasaṃyojanaṃ", f"ဘဝရာဂ {sj}", "1"),
        "issāsaññojan": W("issāsaṃyojanaṃ", f"ငြူစူမှု {sj}", "1"),
        "macchariyasaññojan": W("macchariyasaṃyojanaṃ", f"ဝန်တိုမှု {sj}", "1"),
        "avijjāsaññojan": W("avijjāsaṃyojanaṃ", f"အမှန်ကို မသိမှု {sj}", "1"),
        # gantha (pi-1 «abhijjhā kāyagantho» … «Xဟူသော ကိုယ် အထုံး»)
        "abhijjhākāyaganth": W("abhijjhā kāyagantho", f"သူ့ဥစ္စာကို လိုချင်ခြင်းဟူသော {kg}", "1"),
        "byāpādakāyaganth": W("byāpādo kāyagantho", f"ဖျက်ဆီးလိုစိတ်ဟူသော {kg}", "1"),
        "sīlabbataparāmāsakāyaganth": W("sīlabbataparāmāso kāyagantho", f"{sbp}ဟူသော {kg}", "1"),
        "idaṃsaccābhinivesakāyaganth": W("saccābhiniveso kāyagantho",
                                         f"ဤအရာသာ အမှန်ဟု သက်ဝင်ယုံကြည်ခြင်းဟူသော {kg}", "1"),
    }
    NAMES_N.update(t)


# the two-word gantha names of the Pāli («sīlabbataparāmāsaṃ kāyaganthaṃ»): read as one word (same Burmese)
_GANTH2 = re.compile(_PB + r"([Ss]īlabbataparāmās|[Ii]daṃsaccābhinives|[Bb]yāpād)(?:o|aṃ|assa) kāyagant(h\w*)")


def setup_lex():
    _names()
    for mod in (F, FG):
        mod.add_qual(W("domanassasahagataṃ", "စိတ်ဆင်းရဲမှုနှင့်အတူ ဖြစ်သော", "1", "^1-413"), *[
            "domanassasahagat" + e for e in ("o", "aṃ", "ā", "e", "assa", "ānaṃ")])
        for e in ("o", "aṃ", "ā", "e", "assa", "ānaṃ"):
            mod.LEX.setdefault("domanassasahagat" + e, (mod.QUAL["domanassasahagato"], "adj"))
        for cl, c in CLUSTERS.items():
            neut = cl == "sannojana"
            tab = _NEUT if neut else _MASC
            for e, (case, pl, lk) in tab.items():
                mod.add_fixed(NOUN_OF[cl], case, pl, c["x"] + e)
                mod.NOUN.setdefault(c["x"] + e, (NOUN_OF[cl], case, pl))
                mod.LEX.setdefault(c["x"] + e, (NOUN_OF[cl] + ("+" if pl else ""), lk))
            # «X-sampayuttaka» / «X-sampayutta» on a noun where it is not a dyad term (= the term's Burmese)
            for e in ("o", "aṃ", "ā", "e", "assa", "ānaṃ", "ānañca"):
                for w in (c["x"] + "asampayuttak" + e, c["x"] + "asampayutt" + e):
                    mod.add_qual(DYADS[cl + "_samp"][c["x"] + "asampayutt"], w)
        for st, my in NAMES_N.items():
            neut = "saññojan" in st
            for e, (case, pl, lk) in (_NEUT if neut else _MASC).items():
                mod.add_fixed(my, case, pl, st + e)
                mod.NOUN.setdefault(st + e, (my, case, pl))
                mod.LEX.setdefault(st + e, (my + ("+" if pl else ""), lk))
        # diṭṭhigatavippayutta (pi-1 ^1-400 «အယူမှားနှင့် ကင်းကွာသော»), «-lobhasahagata» (pi-1 ^1-1406 «အယူမှားနှင့်
        # ကင်းကွာသော၊ လောဘနှင့်အတူ ဖြစ်သော»), paṭigha «မုန်းတီးမှု» (pi-1 ^1-1066)
        dv = W("diṭṭhigatavippayuttaṃ", "အယူမှားနှင့် ကင်းကွာသော", "1", "^1-400")
        dvl = W("diṭṭhigatavippayuttā lobhasahagatacittuppādā", f"{dv}၊ လောဘ{mod.SAHAGATA}", "1", "^1-1406")
        for e in ("o", "aṃ", "ā", "e", "assa", "ānaṃ"):
            mod.add_qual(dv, "diṭṭhigatavippayutt" + e)
            mod.add_qual(dvl, "diṭṭhigatavippayuttalobhasahagat" + e)
            mod.LEX.setdefault("diṭṭhigatavippayutt" + e, (dv, "adj"))
            mod.LEX.setdefault("diṭṭhigatavippayuttalobhasahagat" + e, (dvl, "adj"))
        pt = W("paṭighaṃ", "မုန်းတီးမှု", "1", "^1-1066")
        PATIGHA[0] = pt
        for e, (case, pl, lk) in _NEUT.items():
            mod.add_fixed(pt, case, pl, "paṭigh" + e)
            mod.NOUN.setdefault("paṭigh" + e, (pt, case, pl))
            mod.LEX.setdefault("paṭigh" + e, (pt + ("+" if pl else ""), lk))
        for cl, c in CLUSTERS.items():
            mod.add_qual(DYADS[cl][c["x"] + "dk"], c["x"] + "aq")
        dadh = f"{mod.QUAL['domanassasahagato']} {mod.N['adhipati']}"
        mod.add_fixed(dadh, "n", False, "domanassasahagatādhipati")
        mod.LEX.setdefault("domanassasahagatādhipati", (dadh, "n"))
    # coordinations for the lexicon frames (rendered once by the noun-phrase engine, as make_ch3-01-02 does)
    firsts = ["paṭighañca"]
    for cl, c in CLUSTERS.items():
        firsts += [c["x"] + "ā", c["x"] + "e"]
    for st in NAMES_N:
        firsts += ([] if "saññojan" in st else [st + "o"]) + [st + "añca"]
    for first in firsts:
        acc = first.endswith(("ñca", "e"))
        if first.endswith("e"):
            ph = f"{first} ca sampayuttake khandhe ca"
        elif first.endswith("ñca"):
            ph = f"{first} sampayuttake khandhe ca"
        else:
            ph = f"{first} ca sampayuttakā khandhā ca"
        my = F.np_my(ph.split(), iter([]), "@ārabbha" if acc else "n")[0]
        for mod in (F, FG):
            mod.LEX.setdefault(ph, (my, "x"))


PATIGHA = [None]


def setup_lex2():
    for mod in (F, FG):
        for k in ("saṃsaṭṭhaṃ", "saṃsaṭṭhā"):           # the link «saṃsaṭṭho» in its other genders / numbers
            mod.LINK.setdefault(k, mod.LINK["saṃsaṭṭho"])
        mod.add_qual(mod.QUAL["purimā purimā"], "purimaṃ purimaṃ")
        mod.add_qual(mod.QUAL["diṭṭhigatavippayuttalobhasahagataṃ"], "diṭṭhigatavippayuttaṃ lobhasahagataṃ")
        vk = new("vippayuttakā (cetanā)", "ကင်းကွာသော")                 # (vippayutta «ကင်းကွာ…»)
        mod.add_qual(vk, "vippayuttakā")
        mod.LEX.setdefault("vippayuttakā", (vk, "adj"))
        mod.LEX.setdefault("vikkhambhite", (mod.LEX["vikkhambhite kilese"][0].split(" ")[0], "x"))   # cut by «…»
        for cl, c in CLUSTERS.items():
            q = DYADS[cl + "_samp"][c["x"] + "asampayutt"]
            for e in ("o", "aṃ", "ā", "e", "assa", "ānaṃ"):
                for w in (c["x"] + "asampayuttak" + e, c["x"] + "asampayutt" + e):
                    mod.LEX.setdefault(w, (q, "adj"))
    # genitive conjuncts / phrases for the lexicon frames (rendered once by the noun-phrase engine)
    phs = []
    for cl, c in CLUSTERS.items():
        phs += [(f"{c['x']}ānaṃ sampayuttakānañca khandhānaṃ", "g"), (f"sampayuttakānaṃ {c['x']}ānaṃ", "g")]
    for ph, role in phs:
        my = F.np_my(ph.split(), iter([]), role)[0]
        for mod in (F, FG):
            mod.LEX.setdefault(ph, (my, "x"))
    # lobha / paṭigha coordinations of the gantha chapter (np input: the Pāli with the enclitic «ca» read after
    # each member, as make_ch2-03-06 reads «khandhānaṃ mohassa ca»)
    dvl = "diṭṭhigatavippayuttalobhasahagat"
    for ph, inp, role in (
            (f"{dvl}ā khandhā ca lobho ca", None, "n"),
            (f"{dvl}ā khandhā ca lobho ca domanassasahagatā khandhā ca paṭighañca", None, "n"),
            ("domanassasahagatā khandhā ca paṭighañca", None, "n"),
            (f"{dvl}e khandhe ca lobhañca domanassasahagate khandhe ca paṭighañca", None, "@ārabbha"),
            (f"{dvl}e khandhe ca lobhañca", None, "@ārabbha"),
            ("khandhe ca lobhañca paṭighañca", None, "@ārabbha"),
            ("khandhe ca lobhañca", None, "@ārabbha"),
            (f"{dvl}ānaṃ khandhānaṃ lobhassa ca domanassasahagatānaṃ khandhānaṃ paṭighassa ca",
             f"{dvl}ānaṃ khandhānaṃ ca lobhassa ca domanassasahagatānaṃ khandhānaṃ ca paṭighassa ca", "g"),
            (f"{dvl}ānaṃ khandhānaṃ lobhassa ca", f"{dvl}ānaṃ khandhānaṃ ca lobhassa ca", "g"),
            ("khandhānaṃ diṭṭhigatavippayuttassa lobhassa ca paṭighassa ca",
             "khandhānaṃ ca diṭṭhigatavippayuttassa lobhassa ca paṭighassa ca", "g"),
            ("khandhānaṃ diṭṭhigatavippayuttalobhassa ca paṭighassa ca",
             "khandhānaṃ ca diṭṭhigatavippayuttassa lobhassa ca paṭighassa ca", "g"),
            ("sampayuttakānaṃ khandhānaṃ ganthānañca cittasamuṭṭhānānañca rūpānaṃ", None, "g"),
            ("sampayuttakānaṃ khandhānaṃ lobhassa ca cittasamuṭṭhānānañca rūpānaṃ",
             "sampayuttakānaṃ khandhānaṃ ca lobhassa ca cittasamuṭṭhānānañca rūpānaṃ", "g"),
    ) + tuple((f"{c['x']}ā ca {c['x']}asampayuttakā khandhā ca", None, "n") for c in CLUSTERS.values()):
        my = F.np_my((inp or ph).split(), iter([]), role)[0]
        for mod in (F, FG):
            mod.LEX.setdefault(ph, (my, "x"))
    dvla = f"{F.QUAL[dvl + 'o']} {F.N['adhipati']}"
    for mod in (F, FG):
        mod.add_fixed(dvla, "n", False, dvl + "ādhipati")
        mod.LEX.setdefault(dvl + "ādhipati", (dvla, "n"))
    nb = F.LEX["nibbānaṃ"][0]
    for mod in (F, FG):
        mod.SKF.setdefault("nibbānaṃ garuṃ", f"{nb}ကို " + F.LEX["garuṃ katvā"][0].split(" ")[1])   # cut by «…»
    nm = NAMES_N
    cb = K.NOTE_FIXED["cakkaṃ bandhitabbaṃ"]
    for mod in (F, FG):
        # notes inside the list without a «,» (as the Pāli): one fragment
        mod.SKF.setdefault(
            "kāmāsavaṃ paṭicca diṭṭhāsavo avijjāsavo (cakkaṃ bandhitabbaṃ) bhavāsavaṃ paṭicca avijjāsavo (cakkaṃ "
            "bandhitabbaṃ) diṭṭhāsavaṃ paṭicca avijjāsavo.",
            f"{nm['kāmāsav']}ကို မှီ၍ {nm['diṭṭhāsav']}{C} {nm['avijjāsav']}များ ({cb}) {nm['bhavāsav']}ကို မှီ၍ "
            f"{nm['avijjāsav']} ({cb}) {nm['diṭṭhāsav']}ကို မှီ၍ {nm['avijjāsav']}{END}")
        # «pacchimānaṃ…» cut by «…» (the word of the pair «pacchimānaṃ pacchimānaṃ», pi-5 «နောက်နောက်»)
        mod.SKF.setdefault("purimā purimā §T§ā khandhā pacchimānaṃ",
                           f"{mod.QUAL['purimā purimā']} {{T1}} {F.KHANDHA}တို့သည် {mod.QUAL['pacchimānaṃ pacchimānaṃ']}")


# ===================================================================================== notes
NOTE_ADD = {}
CNT = F.COUNT
GARUK = new("garukārammaṇā", f"လေးစားဖွယ်ရာ {F.N['ārammaṇa']}")
AVAJ_VUTTH = f"{F.LEX['āvajjanā'][0]}လည်း{C} {F.LEX['vuṭṭhānassa'][0]}လည်း"      # āvajjanāpi vuṭṭhānampi
ASSADANA = new("assādanā", "သာယာ နှစ်သက်ခြင်း")                    # (assādeti abhinandati «သာယာ နှစ်သက်သည်»)
VIBHAJANA = new("vibhajanā", "ခွဲခြမ်းစိတ်ဖြာခြင်း")                # (vibhajitabbaṃ «ခွဲခြမ်းစိတ်ဖြာရမည်»)
PARIVATT = new("parivattetabbaṃ / -ā", "လှည့်ပြောင်းရမည်")
NA_KAT = new("na kātabbaṃ", "မပြုရ")                                  # (kātabbaṃ «ပြုရမည်»; sample «… မထည့်ရ»)
SEKHA = new("sekhā (persons)", "ကျင့်ကြံဆဲသူတို့သည်")                 # (2-06 sekkha «ကျင့်ကြံဆဲသူ»)


def _notes():
    """plain notes (keys as make_ch1-01's note_body() sees them: lower-case first, «,» spaced)"""
    return {
        "vibhajitabbaṃ": M3.VIBHAJ,
        "evaṃ kātabbaṃ": f"{M3.EVAM_T} {M3.KAT}",
        "anantarasadisaṃ": f"{F.N['anantara']}{F.SADISA}",
        "āvajjanāpi vuṭṭhānampi natthi": AVAJ_VUTTH + f" {M3.NATTHI}",
        "mūlā pucchitabbā": f"{M3.MULA}တို့ကို {M3.PUCCH}",
        "āsavasadisaṃ": f"{NOUN_OF['asava']}{F.SADISA}",
        "mahābhūtā": f"{M3.MAHAB}များ",
        "tīṇipi upanissayā": f"{F.N['upanissaya']} {CNT['tīṇi']}လုံး",
        "mūlaṃ": M3.MULA,
        "garukārammaṇā": GARUK,
        "garukārammaṇā kātabbā": f"{GARUK}အဖြစ် {M3.KAT}",
        "anulomamātikā": M3.ANUL_MATIKA,
    }


def _notep():
    """whole notes (raw Pāli, brackets included) -> Burmese; put in place before the slotter (as make_ch3-01-02)"""
    cn, cd, N = F.cname, F.cond, F.N
    E, CC, KAT, VITTH, GAN, VIB = END, C, M3.KAT, M3.VITTH, M3.GAN, M3.VIBHAJ
    EV, SAB, PANHA, NATTHI, NINN, NINK = M3.EVAM_T, M3.SAB, M3.PANHA, M3.NATTHI, M3.NINNANA, M3.NINNANAKARANA
    ITARE, GANANA, PV, VARA, LAK = M3.ITARE, S.GANANA, M3.PATICCA_V, M3.VARA, F.LAKAUNG
    SAMKH, CAKKA, MULA, PUCCH = F.NOTES["(saṃkhittaṃ)"][1:-1], M3.CAKKA, M3.MULA, M3.PUCCH
    pi, pio = M3._pi, M3._pi_obj
    ALL6 = ("paṭicca", "sahajāta", "paccaya", "nissaya", "saṃsaṭṭha", "sampayutta")
    lok = M3.DUKA_NAME["Lokiyadukaṃ"]
    lokut = f"{M3.DYADS['lokiya']['lokuttar']} {F.DHAMMA}"
    CULA = M3.GOCCHAKA["Cūḷantaradukaṃ"] + "၌"
    ADUKA, GDUKA = DUKA_NAME["Āsavadukaṃ"], DUKA_NAME["Ganthadukaṃ"]
    ANP = f"{K.ORDER_N['anulomaṃ']}၏ {F.PADA}တို့"
    am, sm = F.LEX["ārammaṇādhipati"][0], F.LEX["sahajātādhipati"][0]
    arabbha = F.LEX["ārabbha"][0].replace("ကို ", "")
    sbp = W("sīlabbataparāmāso", "သီလ အကျင့်ဝတ်ဆိုင်ရာ မှားယွင်းသော ယူဆမှု", "1")

    def lokiya_like(verb, tail=""):
        return f"{CULA} {lok}{K.KAYYA} {K.EVAM} {NINK} {verb}{tail}"

    return {
        # 3-03
        "(ekekampi cakkaṃ kātabbaṃ)": f"(တစ်ခုစီကိုလည်း {CAKKA} {KAT})",
        "(āsavamūlakaṃ tīṇi, paṭiccasadisā)":
            f"({DYADS['asava']['āsavdk']} {F.DHAMMA}{F.MULAKA}၌ {CNT['tīṇi']}{CC} {PV}{K.SADISANI})",
        "(evaṃ sabbe gaṇanā gaṇetabbā)": f"({EV} {GANANA} {SAB}ကို {GAN})",
        "(Gaṇanāpi sampayuttavāropi saṃsaṭṭhavārasadiso.)":
            f"({GANANA}လည်း{CC} {VARA('sampayutta')}လည်း {VARA('saṃsaṭṭha')}{F.SADISA}{E})",
        "(dutiyagamanaṃ)": f"(ဒုတိယ {M.GAMANA})",
        "(tīṇi ārammaṇasadisā, garukārammaṇā kātabbā)":
            f"({CNT['tīṇi']} {F.N['ārammaṇa']}{K.SADISANI}{CC} {GARUK}အဖြစ် {KAT})",  # harmonise H19: a bare «X-sadisa» (no «paccaya» in the Pāli) = the bare name
        "(tīṇi, garukārammaṇā)": f"({CNT['tīṇi']}{CC} {GARUK})",
        "(vatthu ca dassetabbaṃ)": f"({F.VATTHU}ကိုလည်း {M3.DASSET})",
        "(anulomapadā paripuṇṇā)": f"({ANP} {M3.PARIP}ကြသည်)",
        "(anulomapadāni gaṇitabbāni)": f"({ANP}ကို {GAN})",
        "(anulomapadāni kātabbāni)": f"({ANP}ကို {KAT})",
        "(anulomapadāni paripuṇṇāni kātabbāni)": f"({ANP}ကို {M3.PARIP}အောင် {KAT})",
        "(Yathā cūḷantaraduke lokiyadukaṃ evaṃ kātabbaṃ ninnānākaraṇaṃ.)": f"({lokiya_like(KAT)}{E})",
        "(Yathā cūḷantaraduke lokiyadukaṃ evaṃ vitthāretabbaṃ ninnānākaraṇaṃ, saṃkhittaṃ.)":
            f"({lokiya_like(VITTH)}{CC} {SAMKH}{E})",
        "(yathā cūḷantaraduke lokiyadukaṃ evaṃ vitthāretabbaṃ ninnānākaraṇaṃ)": f"({lokiya_like(VITTH)})",
        "(Yathā cūḷantaraduke lokiyadukaṃ evaṃ vibhajitabbaṃ ninnānākaraṇaṃ.)": f"({lokiya_like(VIB)}{E})",
        "(Cūḷantaraduke lokiyadukasadisaṃ, ninnānākaraṇaṃ.)": f"({CULA} {lok}{F.SADISA}{CC} {NINK}{E})",
        "(Imaṃ dukaṃ cūḷantaraduke lokiyadukasadisaṃ ninnānākaraṇaṃ.)":
            f"(ဤ {DUKA}သည် {NINK} {CULA} {lok}{F.SADISA}{E})",
        "(Evaṃ sabbe paccayā vitthāretabbā. Saṃkhittaṃ.)": f"({EV} {F.PACCAYA} {SAB}ကို {VITTH}{E} {SAMKH}{E})",
        "(Cakkaṃ. Evaṃ sabbe paccayā kātabbā.)": f"({CAKKA}{E} {EV} {F.PACCAYA} {SAB}ကို {KAT}{E})",
        "(Napacchājātapaccayā nava, naāsevanapaccayā nava.)":
            f"({cd('pacchājāta', 'ab', True)} {CNT['nava']}{CC} {cd('āsevana', 'ab', True)} {CNT['nava']}{E})",
        "(Idha assādanā natthi)": f"({M3.IHA} {ASSADANA} {NATTHI})",
        "(Pucchitabbaṃ mūlaṃ)": f"({MULA}ကို {PUCCH})",
        "(evaṃ cakkaṃ bandhitabbaṃ)": f"({EV} {K.NOTE_FIXED['cakkaṃ bandhitabbaṃ']})",
        "(sabbaṃ cakkaṃ)": f"({SAB} {CAKKA})",
        "(Evaṃ paṭiccavāropi sahajātavāropi paccayavāropi nissayavāropi saṃsaṭṭhavāropi sampayuttavāropi yathā "
        "āsavadukaṃ evaṃ kātabbaṃ, ninnānaṃ.)": f"({EV} {pio(*ALL6)} {ADUKA}{K.KAYYA} {K.EVAM} {KAT}{CC} {NINN}{E})",
        "(Pañhāvāre hetupaccayepi ārammaṇapaccayepi lokuttaraṃ na kātabbaṃ, sekhā gotrabhuṃ paccavekkhanti, vodānaṃ "
        "paccavekkhantīti kātabbā. Adhipatipaccayampi sabbaṃ jānitvā kātabbaṃ.)":
            (f"({VARA('pañhā')}၌ {cd('hetu', 'loc')}လည်း{CC} {cd('ārammaṇa', 'loc')}လည်း {lokut}ကို {NA_KAT}{CC} "
             f"{SEKHA} {F.LEX['gotrabhuṃ'][0]}ကို {F.LEX['paccavekkhanti'][0]}{CC} {F.LEX['vodānaṃ'][0]}ကို "
             f"{F.LEX['paccavekkhanti'][0]}ဟု {KAT}{E} {cn('adhipati')}ကိုလည်း {SAB} {M3.NEW['jānitvā']} {KAT}{E})"),
        "(evaṃ sabbaṃ vitthāretabbaṃ)": f"({EV} {SAB}ကို {VITTH})",
        "(Āsavadukepi anantaraṃ iminā sadisaṃ kātabbaṃ. Āvajjanāpi vuṭṭhānampi evaṃ samuddiṭṭhaṃ saṃkhittaṃ. "
        "Sabbaṃ paripuṇṇaṃ. Āsavadukasadisaṃ kātabbaṃ, ninnānaṃ.)":
            (f"({ADUKA}၌လည်း {cn('anantara')}ကို ဤသည်နှင့် တူအောင် {KAT}{E} {AVAJ_VUTTH} {EV} "
             + new("samuddiṭṭhaṃ saṃkhittaṃ", "အကျဉ်းချုပ်၍ ဖော်ပြထားသည်")
             + f"{E} {SAB} {M3.PARIP}သည်{E} {ADUKA}နှင့် တူအောင် {KAT}{CC} {NINN}{E})"),
        "(vipākaṃ natthi)": f"({N['vipāka']} {NATTHI})",
        "(nahetumūlakaṃ natthi)": f"({cd('hetu', 'n', True)}{F.MULAKA} {NATTHI})",
        "(Evaṃ itare dve gaṇanāpi sahajātavārampi paccayavārampi nissayavārampi saṃsaṭṭhavārampi sampayuttavārampi "
        "paripuṇṇaṃ paṭiccasadisā.)":
            (f"({EV} {ITARE} {GANANA} {CNT['dve']}လည်း{CC} {pi('sahajāta', 'paccaya', 'nissaya', 'saṃsaṭṭha', 'sampayutta')}"
             f" {M3.PARIP}စွာ {PV}{K.SADISANI}{E})"),
        "(ārammaṇasadisā, garukārammaṇā)": f"({F.N['ārammaṇa']}{K.SADISANI}{CC} {GARUK})",  # harmonise H19: a bare «X-sadisa» (no «paccaya» in the Pāli) = the bare name
        "(ārammaṇasadisā, garukārammaṇā kātabbā)": f"({F.N['ārammaṇa']}{K.SADISANI}{CC} {GARUK}အဖြစ် {KAT})",
        "(ārammaṇasadisāyeva, purimā purimāti kātabbā.)":
            f"({F.N['ārammaṇa']}{K.SADISANI}ပင်{CC} {F.QUAL['purimā purimā']}ဟု {KAT}{E})",
        "(ārammaṇasadisaṃyeva, vibhajanā natthi… tīṇi. Upanissayaṃ sabbaṃ kātabbaṃ)":
            (f"({F.N['ārammaṇa']}{F.SADISA}ပင်{CC} {VIBHAJANA} {NATTHI}{PE} {CNT['tīṇi']}{E} "
             f"{cn('upanissaya')}ကို {SAB} {KAT})"),
        "(evaṃ itarepi dve gaṇanā kātabbā)": f"({EV} {ITARE} {GANANA} {CNT['dve']}ကိုလည်း {KAT})",
        # 3-04
        "(vibhajitabbaṃ āsavasadisaṃ)": f"({NOUN_OF['asava']}နှင့် တူအောင် {VIB})",
        "(yāva paṭisandhi)": f"({F.PATISANDHI}အထိ)",
        "(yāva mahābhūtā)": f"({M3.MAHAB}တို့အထိ)",
        "(paṭiccasadisā)": f"({PV}{K.SADISANI})",
        "(ārammaṇanayena kātabbā)": f"({cn('ārammaṇa')}၏ " + new("nayena", "နည်းအတိုင်း") + f" {KAT})",
        "(Ārammaṇapaccaye rūpaṃ natthi. Adhipatipaccayo hetusadiso, vicikicchāsaññojanaṃ natthi.)":
            (f"({cd('ārammaṇa', 'loc')} ရုပ် {NATTHI}{E} {cn('adhipati')}သည် {N['hetu']}{F.SADISA}{CC} "
             f"{NAMES_N['vicikicchāsaññojan']} {NATTHI}{E})"),
        "(Saṃkhittaṃ. Āsavagocchakasadisaṃ. Naārammaṇāpi sabbe uddharitabbā.)":
            (f"({SAMKH}{E} {GNAME['asava']}{F.SADISA}{E} {cd('ārammaṇa', 'n', True)}တို့ကိုလည်း {SAB} "
             + new("uddharitabbā", "ထုတ်နုတ်ရမည်") + f"{E})"),
        "(evaṃ sabbaṃ gaṇetabbaṃ)": f"({EV} {SAB}ကို {GAN})",
        "(yattha yattha vatthu labbhati, tattha tattha ninnetabbaṃ)":
            f"({F.VATTHU}ကို " + new("yattha yattha … labbhati, tattha tattha ninnetabbaṃ",
                                     "တွေ့ရသည့် နေရာတိုင်း၊ ထိုထို နေရာ၌ ထည့်သွင်းရမည်") + ")",
        "(Evaṃ itarepi dve gaṇanā ca nissayavāro ca kātabbo.)":
            f"({EV} {ITARE} {GANANA} {CNT['dve']}ကို{LAK}{CC} {VARA('nissaya')}ကို{LAK} {KAT}{E})",
        "(evaṃ nava pañhā. Arūpāyeva kātabbā)": f"({EV} {PANHA} {CNT['nava']}{E} {M3.ARUPA_N}တို့ကိုသာ {KAT})",
        "(Saṃsaṭṭhavāropi sampayuttavāropi evaṃ kātabbā.)": f"({pio('saṃsaṭṭha', 'sampayutta')} {EV} {KAT}{E})",
        "(ārabbhayeva kātabbā)": f"({arabbha}ဟုသာ {KAT})",
        "(ārabbha kātabbā)": f"({arabbha}ဟု {KAT})",
        "(tiṇṇampi ārammaṇādhipati, sahajātādhipatipi kātabbā, vibhajitabbā tīṇipi)":
            f"({CNT['tīṇi']}လုံး၌ {am}{CC} {sm}ကိုလည်း {KAT}{CC} {CNT['tīṇi']}လုံးကို {VIB})",
        "(evaṃ dvepi kātabbā)": f"({EV} {CNT['dve']}လုံးကို {KAT})",
        "(evaṃ tīṇipi)": f"({EV} {CNT['tīṇi']}လုံး)",
        "(saṃkhittaṃ, evaṃ kātabbaṃ)": f"({SAMKH}{CC} {EV} {KAT})",
        "(Itare dve gaṇanāpi sampayuttavāropi kātabbo.)":
            f"({ITARE} {GANANA} {CNT['dve']}ကိုလည်း{CC} {VARA('sampayutta')}ကိုလည်း {KAT}{E})",
        "(Saññojanagocchake paṭhamadukasadisaṃ.)": f"({GNAME['sannojana']}၌ ပထမ {DUKA}{F.SADISA}{E})",
        "(Evaṃ imampi dukaṃ vitthāretabbaṃ, ninnānākaraṇaṃ ṭhapetvā lokuttaraṃ)":
            f"({EV} ဤ {DUKA}ကိုလည်း {VITTH}{CC} {lokut}ကို " + new("ṭhapetvā", "ချန်ထား၍") + f" {NINK})",
        "(Evaṃ itare dve gaṇanāpi sahajātavāropi kātabbo. Paccayavāropi nissayavāropi saṃsaṭṭhavāropi "
        "sampayuttavāropi paṭiccavārasadisā.)":
            (f"({EV} {ITARE} {GANANA} {CNT['dve']}ကိုလည်း{CC} {VARA('sahajāta')}ကိုလည်း {KAT}{E} "
             f"{pi('paccaya', 'nissaya', 'saṃsaṭṭha', 'sampayutta')} {PV}{K.SADISANI}{E})"),
        "(imāsu tīsupi pañhāsu ārammaṇādhipatipi sahajātādhipatipi kātabbā)":
            f"(ဤ {PANHA} {CNT['tīṇi']}လုံး၌ {am}ကိုလည်း{CC} {sm}ကိုလည်း {KAT})",
        "(ninnānākaraṇaṃ, vibhajanā natthi. Ārammaṇasadisā)":
            f"({NINK}{CC} {VIBHAJANA} {NATTHI}{E} {cn('ārammaṇa')}{K.SADISANI})",
        "(Saṃkhittaṃ. Evaṃ nava pañhā kātabbā. Tīsuyeva padesu parivattetabbā, nānākkhaṇikā natthi.)":
            (f"({SAMKH}{E} {EV} {PANHA} {CNT['nava']}ကို {KAT}{E} {F.PADA} {CNT['tīṇi']}၌သာ {PARIVATT}{CC} "
             f"{F.LEX['nānākkhaṇikā'][0]} {NATTHI}{E})"),
        "(yāva asaññasattā, mahābhūtā)": f"({M3.YAVA_AS}{CC} {M3.MAHAB}များ)",
        # 3-05
        "(arūpe sīlabbataparāmāso natthi, evaṃ nava pañhā kātabbā)":
            f"({F.PREFIX['arūpe']} {sbp} {NATTHI}{CC} {EV} {PANHA} {CNT['nava']}ကို {KAT})",
        "(Nissayavāro paccayavārasadisova. Saṃsaṭṭhavāropi sampayuttavāropi nava pañhā kātabbā, rūpaṃ natthi.)":
            (f"({VARA('nissaya')}သည် {VARA('paccaya')}{F.SADISA}ပင်{E} {pi('saṃsaṭṭha', 'sampayutta')} {PANHA} "
             f"{CNT['nava']}ကို {KAT}{CC} ရုပ် {NATTHI}{E})"),
        "(dve āvajjanā kātabbā, paṭhamo natthi)":
            f"({F.LEX['āvajjanā'][0]} {CNT['dve']}ကို {KAT}{CC} ပထမ {PANHA} {NATTHI})",
        "(ekampi vuṭṭhānaṃ kātabbaṃ, majjhe)":
            f"({F.LEX['vuṭṭhānassa'][0]} {CNT['ekaṃ']}ကိုလည်း {KAT}{CC} " + new("majjhe", "အလယ်၌") + ")",
        "(napurejāte vibhajantena arūpaṃ paṭhamaṃ kātabbaṃ, rūpaṃ yattha labbhati pacchā kātabbaṃ, paṭighañca "
        "arūpe natthi)":
            (f"({cd('purejāta', 'loc', True)} " + new("vibhajantena", "ခွဲခြမ်းစိတ်ဖြာလျက်") + f" {M3.ARUPA_N}ကို "
             + new("paṭhamaṃ (first)", "ပထမ") + f" {KAT}{CC} ရုပ်ကို တွေ့ရသည့် နေရာ၌ " + new("pacchā", "နောက်မှ")
             + f" {KAT}{CC} {F.PREFIX['arūpe']} {PATIGHA[0]}လည်း {NATTHI})"),
        "(Sahajātavāropi evaṃ kātabbo.)": f"({VARA('sahajāta')}ကိုလည်း {EV} {KAT}{E})",
        "(Tīsupi mūlā pucchitabbā)": f"({CNT['tīṇi']}လုံး၌ {MULA}တို့ကို {PUCCH})",
        "(tīṇi upanissayā)": f"({N['upanissaya']} {CNT['tīṇi']})",
        "(anulomamātikā vitthāretabbā)": f"({M3.ANUL_MATIKA}ကို {VITTH})",
        "(Paṭiccavārampi sahajātavārampi paccayavārampi nissayavārampi saṃsaṭṭhavārampi sampayuttavārampi "
        "ganthadukasadisaṃ ninnānākaraṇaṃ.)": f"({pi(*ALL6)} {NINK} {GDUKA}{F.SADISA}{E})",
        "(evaṃ nava pañhā vitthāretabbā)": f"({EV} {PANHA} {CNT['nava']}ကို {VITTH})",
        "(evaṃ itarepi tīṇi vitthāretabbā)": f"({EV} {ITARE} {CNT['tīṇi']}ကိုလည်း {VITTH})",
        "(Ārabbha kātabbā. Imasmiṃ duke lokuttaraṃ natthi, ganthadukasadisaṃ, ninnānākaraṇaṃ. \"Ganthaniya\"nti "
        "niyāmetabbaṃ, magge nava pañhā kātabbā.)":
            (f"({arabbha}ဟု {KAT}{E} ဤ {DUKA}၌ {lokut} {NATTHI}{CC} {GDUKA}{F.SADISA}{CC} {NINK}{E} "
             f"“{DYADS['gantha_s']['ganthaniy'][:-len('သော')]}သည်”ဟု {M3.NIYAM}{CC} {cd('magga', 'loc')} {PANHA} "
             f"{CNT['nava']}ကို {KAT}{E})"),
        "(Idha nahetupaccayo natthi)": f"({M3.IHA} {cd('hetu', 'n', True)} {NATTHI})",
        "(Evaṃ itare dve gaṇanāpi sahajātavāropi paccayavāropi nissayavāropi saṃsaṭṭhavāropi sampayuttavāropi "
        "paṭiccavārasadisā.)":
            (f"({EV} {ITARE} {GANANA} {CNT['dve']}လည်း{CC} "
             f"{pi('sahajāta', 'paccaya', 'nissaya', 'saṃsaṭṭha', 'sampayutta')} {PV}{K.SADISANI}{E})"),
        "(Evaṃ itarepi tīṇi pañhā kātabbā ārammaṇasadisaṃyeva. Adhipatiyāpi anantarepi upanissayepi vibhāgo "
        "natthi.)":
            (f"({EV} {ITARE} {PANHA} {CNT['tīṇi']}ကိုလည်း {F.N['ārammaṇa']}နှင့် တူအောင်ပင် {KAT}{E} "
             f"{cd('adhipati', 'loc')}လည်း{CC} {cd('anantara', 'loc')}လည်း{CC} {cd('upanissaya', 'loc')}လည်း "
             + new("vibhāgo", "ခွဲခြားချက်") + f" {NATTHI}{E})"),
        "(Arūpaṃyeva paccayaṃ, ekekassa tīṇi tīṇi kātabbā. Ārammaṇañca sahajātañca upanissayañca navasupi "
        "parivattetabbaṃ. Evaṃ pañhāvārepi sabbaṃ kātabbaṃ.)":
            (f"({M3.ARUPA_N}ကိုသာ {F.PACCAYA}အဖြစ်{CC} တစ်ခုစီ၏ {CNT['tīṇi']} {CNT['tīṇi']}စီကို {KAT}{E} "
             f"{cn('ārammaṇa')}ကို{LAK}{CC} {cn('sahajāta')}ကို{LAK}{CC} {cn('upanissaya')}ကို{LAK} "
             f"{CNT['nava']}လုံး၌ {PARIVATT}{E} {EV} {VARA('pañhā')}၌လည်း {SAB}ကို {KAT}{E})"),
        "(Mūlaṃ, tīṇipi upanissayā)": f"({MULA}{CC} {F.N['upanissaya']} {CNT['tīṇi']}လုံး)",
        # 3-06
        "(dvepi gocchakā āsavagocchakasadisā ninnānākaraṇā)":
            f"(" + new("gocchakā", "အစု") + f" {CNT['dve']}လုံးသည် {NINK} {GNAME['asava']}{K.SADISANI})",
    }


def setup_notes():
    NOTE_ADD.update(_notes())
    K.NOTE_FIXED.update(NOTE_ADD)
    for k, v in NOTE_ADD.items():
        new(k, v)
    base = len(M3.NOTEP)
    raw = "".join((PALI / n).read_text(encoding="utf-8-sig") for n in NAMES)
    for p_ in _notep():
        assert p_ in raw, "note not in the Pāli: " + p_
    for i, (p_, my) in enumerate(_notep().items(), base):
        new(p_, my)
        M3.NOTEP[p_] = my
        k = f"⁑d{i}"
        K.NOTE_FIXED[k] = my[1:-1]
        for mod in (F, FG):
            mod.NOTES[f"({k})"] = my


SLIP_FIX = {"Āsavañceva āsavasampayuttaṃ dhammaṃ paṭicca": "Āsavañceva āsavasampayuttañca dhammaṃ paṭicca",
            "(yāva āsaññasattā)": "(yāva asaññasattā)"}


def setup():
    setup_names()
    setup_lex()
    setup_lex2()
    setup_notes()
    M3.SLIP_FIX.update(SLIP_FIX)


setup()


# a sentence without its final «.» in the Pāli (source slip): read with it in memory, its «။» removed afterwards
NOEND = {"3-04-sannojanagocchaka.md": ["khandhe paṭicca saññojanā (2)"]}
NOEND_FIX = {"khandhe paṭicca saññojanā (2)": "khandhe paṭicca saññojanā. (2)"}
_TR_ORIG = M3.translate


def translate(name):
    src = (PALI / name).read_text(encoding="utf-8-sig")
    keys = NOEND.get(name, [])
    if not keys:
        return _TR_ORIG(name)
    out = []
    for k in keys:
        assert k in src
        F.SLIPS.add(f"«{k}» without its «.» (no «။» written)")
    fixed = src
    for k in keys:
        fixed = fixed.replace(k, NOEND_FIX[k])
    outs = [M3.translate_part(d, t) for d, t in M3.parts_of(fixed)]
    txt = "\n".join(outs)
    pl = [l for l in src.splitlines() if l.strip()]
    ml = txt.split("\n")
    j = 0
    for i, l in enumerate(ml):
        if not l.strip():
            continue
        if any(k in pl[j] for k in keys):
            assert l.count("။ (2)") == 1, l
            ml[i] = l.replace("။ (2)", " (2)")
        j += 1
    return "\n".join(ml)


def regress():
    bad = M3.regress()
    for n in M3.NAMES:
        txt = M3.translate(n)
        pub = (OUT / n).read_text(encoding="utf-8")
        a, b = txt.splitlines(), pub.splitlines()
        d = [i for i, (x, y) in enumerate(zip(a, b)) if x != y]
        ok = len(a) == len(b) and not d
        print(n, "identical" if ok else f"DIFFERS ({len(d)} lines: {d[:10]})")
        bad += not ok
    return bad


def main():
    global OUT
    K.CUR["fix"] = True
    if "--out" in sys.argv:
        OUT = pathlib.Path(sys.argv[sys.argv.index("--out") + 1]).resolve()
        del sys.argv[sys.argv.index("--out"):sys.argv.index("--out") + 2]
    if "--regress" in sys.argv:
        sys.exit(1 if regress() else 0)
    F.DEV = "--dev" in sys.argv
    names = [a for a in sys.argv[1:] if not a.startswith("--")] or NAMES
    if F.DEV:
        F.UNSEEN = M3.Counting()
    for n in names:
        txt = translate(n)
        if not F.DEV:
            (OUT / n).write_text(txt, encoding="utf-8")
            print(f"wrote {n}: {sum(1 for l in txt.splitlines() if l)} lines")
        else:
            CHK.mkdir(exist_ok=True)
            (CHK / ("dev-" + n)).write_text(txt, encoding="utf-8")
    if F.DEV:
        rows = sorted(F.UNSEEN.items(), key=lambda kv: -F.UNSEEN.cnt[kv[0]])
        CHK.mkdir(exist_ok=True)
        with open(CHK / "dev.txt", "w", encoding="utf-8") as fh:
            for k, v in rows:
                fh.write(f"[{F.UNSEEN.cnt[k]}] SK: {k}\n    {v}\n")
        print(len(rows), "unmatched skeletons,", sum(F.UNSEEN.cnt.values()), "occurrences")
    if F.SLIPS and "--slips" in sys.argv:
        print("slips:", *sorted(F.SLIPS), sep="\n  ")


if __name__ == "__main__":
    main()
