"""Burmese zero-shot of pi-7 3-01 hetugocchaka and 3-02 cūḷantaraduka, the first DYAD chapters of the Dukapaṭṭhāna
(«အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ»), from the Pāli only.

usage: python3 -I -X utf8 make_ch3-01-02.py [chapter ...] [--dev] [--regress] [--slips] [--out DIR]
  (no flag)  translate the chapters and write them; stops on the first unmatched sentence (nothing is guessed).
  --dev      do not stop: list every unmatched skeleton with its count in chk-ch3-01-02/dev.txt (nothing written).
  --regress  regenerate the approved sample (1-00, 1-02) and the finished group 2-03 … 2-06 in memory through this
             script and compare them with the published files (they must be identical).

Engines (all read-only, imported, never run as scripts): make_ch2-03-06.py is IMPORTED for its in-memory engine
(PRIMARY: my7_formulas + make_sample + make_ch1-01; FALLBACK per sentence unit: an isolated copy with
make_ch1-03-05) and its extensions (notes, lexicon, chains). No main block of another script runs; no file of the
sample or of another group is edited. This script adds the dyads (pi-1 final Mātikā ^1-M2-1 … ^1-M2-13), their
names, the dyad-section switch, notes and unique sentences; every new string is logged in notes-ch3-01-02.md.

A chapter holds several dyads: it is cut at its dyad headings («###### Hetudukaṃ» …) and each part is translated
with only its own dyad active (the parts are joined with one blank line, as in the source).
Terms that are not a-stems (hetu / nahetu, rūpī / arūpī, the two-member terms «hetu ceva sahetuko ca» …) are read
as pseudo a-stem words before slotting (the Burmese of a term does not depend on its Pāli ending; the noun carries
number and case). «hetu» is a dyad term only before a dhamma word (or coordinated with «nahetu» before one);
otherwise it is the noun «အမြစ်» (root), as in the Pāli «hetuṃ paṭicca sampayuttakā khandhā».
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
NAMES = ["3-01-hetugocchaka.md", "3-02-culantaraduka.md"]
CHK = HERE / "chk-ch3-01-02"
WCH = r"[\wāīūṃṅñṭḍṇḷ]"


def _load(name, fn):
    spec = importlib.util.spec_from_file_location(name, HERE / fn)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


M = _load("ch20306", "make_ch2-03-06.py")          # its setup() runs on import; its main() does not
F, FG, G, K, S = M.F, M.FG, M.G, M.K, M.S
C, END, PE, W = F.C, F.END, F.PE, F.W

NEW = collections.OrderedDict()     # every new string of this script: Pāli -> Burmese


def new(pali, my):
    NEW.setdefault(pali, my)
    return my


# ===================================================================================== the dyads (pi-1 final)
_PL = " သဘောတရားများ"


def _dw(pali, my, bid):
    """a pi-1 Mātikā dyad term, read from the FINAL rails (attributive form, without « သဘောတရားများ»)"""
    return W(pali, my + _PL, "1", bid)[:-len(_PL)]


HETU = _dw("hetū dhammā", "အမြစ် ဖြစ်သော", "^1-M2-1")
NAHETU = _dw("na hetū dhammā", "အမြစ် မဟုတ်သော", "^1-M2-1")
SAHETUKA = _dw("sahetukā dhammā", "အမြစ် ရှိသော", "^1-M2-2")
AHETUKA_T = _dw("ahetukā dhammā", "အမြစ် မရှိသော", "^1-M2-2")
assert AHETUKA_T == F.AHETUKA            # the qualifier «ahetuka» of the sample (pi-2) is the same Burmese
DYADS = {
    "hetu": {"hetudk": HETU, "nahetudk": NAHETU},
    "sahetuka": {"sahetuk": SAHETUKA, "ahetuk": AHETUKA_T},
    "hetusamp": {"hetusampayutt": _dw("hetusampayuttā dhammā", "အမြစ်နှင့် ယှဉ်တွဲသော", "^1-M2-3"),
                 "hetuvippayutt": _dw("hetuvippayuttā dhammā", "အမြစ်နှင့် ကင်းကွာသော", "^1-M2-3")},
    "hetusahetuka": {"hetusahetukdk": _dw("hetū ceva dhammā sahetukā ca", "အမြစ်လည်း ဖြစ်၊ အမြစ်လည်း ရှိသော",
                                          "^1-M2-4"),
                     "sahetukanahetudk": _dw("sahetukā ceva dhammā na ca hetū", "အမြစ် ရှိသော်လည်း အမြစ် မဟုတ်သော",
                                             "^1-M2-4")},
    "hetuhetusamp": {"hetuhetusampdk": _dw("hetū ceva dhammā hetusampayuttā ca",
                                           "အမြစ်လည်း ဖြစ်၊ အမြစ်နှင့်လည်း ယှဉ်တွဲသော", "^1-M2-5"),
                     "hetusampnahetudk": _dw("hetusampayuttā ceva dhammā na ca hetū",
                                             "အမြစ်နှင့် ယှဉ်တွဲသော်လည်း အမြစ် မဟုတ်သော", "^1-M2-5")},
    # ^1-M2-6 «na hetū kho pana dhammā sahetukāpi / ahetukāpi» is not attributive in pi-1 («… အမြစ် မဟုတ်သော
    # သဘောတရားများအနက် အမြစ် ရှိသည်တို့လည်း»): the two terms are built from the pi-1 words, in the pattern of
    # «sahetuko ceva na ca hetu» «အမြစ် ရှိသော်လည်း အမြစ် မဟုတ်သော» and «hetu ceva sahetuko ca» (NEW)
    "nahetusahetuka": {"nahetusahetuk": new("nahetu sahetuko (dyad term)", "အမြစ် မဟုတ်သော်လည်း အမြစ် ရှိသော"),
                       "nahetuahetuk": new("nahetu ahetuko (dyad term)", "အမြစ် မဟုတ်၊ အမြစ် မရှိသော")},
    "sappaccaya": {"sappaccay": _dw("sappaccayā dhammā", "အကြောင်း ရှိသော", "^1-M2-7"),
                   "appaccay": _dw("appaccayā dhammā", "အကြောင်း မရှိသော", "^1-M2-7")},
    "sankhata": {"saṅkhat": _dw("saṅkhatā dhammā", "ပြုပြင်ဖန်တီးထားသော", "^1-M2-8"),
                 "asaṅkhat": _dw("asaṅkhatā dhammā", "ပြုပြင်ဖန်တီးထားခြင်း မရှိသော", "^1-M2-8")},
    "sanidassana": {"sanidassan": _dw("sanidassanā dhammā", "မြင်နိုင်သော", "^1-M2-9"),
                    "anidassan": _dw("anidassanā dhammā", "မမြင်နိုင်သော", "^1-M2-9")},
    "sappatigha": {"sappaṭigh": _dw("sappaṭighā dhammā", "ထိခိုက်မှု ရှိသော", "^1-M2-10"),
                   "appaṭigh": _dw("appaṭighā dhammā", "ထိခိုက်မှု မရှိသော", "^1-M2-10")},
    "rupi": {"rūpdk": _dw("rūpino dhammā", "ရုပ် ဖြစ်သော", "^1-M2-11"),
             "arūpdk": _dw("arūpino dhammā", "ရုပ် မဟုတ်သော", "^1-M2-11")},
    "lokiya": {"lokiy": _dw("lokiyā dhammā", "လောကနှင့် သက်ဆိုင်သော", "^1-M2-12"),
               "lokuttar": _dw("lokuttarā dhammā", "လောကကို ကျော်လွန်သော", "^1-M2-12")},
    "kenaci": {"kenaci viññeyy": _dw("kenaci viññeyyā dhammā", "တစ်စုံတစ်ခုသော စိတ်ဖြင့် သိနိုင်သော", "^1-M2-13"),
               "kenaci naviññeyy": _dw("kenaci na viññeyyā dhammā", "တစ်စုံတစ်ခုသော စိတ်ဖြင့် မသိနိုင်သော",
                                       "^1-M2-13")},
}
# both members of a dyad on one noun that is not dhamma («sanidassanañca anidassanañca … rūpaṃ», «kenaci viññeyyā ca
# kenaci naviññeyyā ca tayo khandhā»): one slot, the two qualifiers stacked «A၊ B N» (as 2-07 … 2-11 «A၊ B N» for two
# terms on one noun); with the noun dhamma the module's «A သဘောတရားနှင့် B သဘောတရား» stays
for _d, _tab in DYADS.items():
    _a, _b = list(_tab)
    _tab[_a + "_" + _b.replace(" ", "_") + "_both"] = f"{_tab[_a]}{C} {_tab[_b]}"
assert DYADS["rupi"]["rūpdk"] == F.QUAL["rūpino"] and DYADS["rupi"]["arūpdk"] == F.ARUPA

# dyad heading (level 6) -> dyad
DYAD_OF = {"Hetudukaṃ": "hetu", "Sahetukadukaṃ": "sahetuka", "Hetusampayuttadukaṃ": "hetusamp",
           "Hetusahetukadukaṃ": "hetusahetuka", "Hetuhetusampayuttadukaṃ": "hetuhetusamp",
           "Nahetusahetukadukaṃ": "nahetusahetuka", "Sappaccayadukaṃ": "sappaccaya", "Saṅkhatadukaṃ": "sankhata",
           "Sanidassanadukaṃ": "sanidassana", "Sappaṭighadukaṃ": "sappatigha", "Rūpīdukaṃ": "rupi",
           "Lokiyadukaṃ": "lokiya", "Kenaciviññeyyadukaṃ": "kenaci"}
_END = M._END.replace("|ānaṃ|", "|ānañca|ānaṃ|")          # + «-ānañca» (a genitive plural term opening a conjunct)
assert _END != M._END


def set_dyad(mod, d):
    M.set_triad(mod, None)                       # the 2-03 … 2-06 triads off
    for t in list(mod.TRIADS):
        if t in DYADS:
            mod.TRIADS.pop(t, None)
            mod.TRIAD_END.pop(t, None)
    if d:
        mod.TRIADS[d] = DYADS[d]
        mod.TRIAD_END[d] = _END
    mod.rebuild()


# ===================================================================================== names and headings
DUKA = F.DUKA
HETU_N = F.NOUN["hetū"][0]                                          # «အမြစ်» (pi-1)
GOCCHAKA = {"Hetugocchakaṃ": W("Hetugocchakaṃ", "အမြစ်တို့၏ အစု", "1", "^1-M-2-1-0"),
            "Cūḷantaradukaṃ": W("Cūḷantaradukaṃ", "ကြားညှပ် နှစ်မျိုးတွဲ အစုငယ်", "1", "^1-M-2-2-0")}
# the dyad names (NEW; the pattern of the triad names «<the notion of the first term> သုံးမျိုးတွဲ»)
DUKA_NAME = {
    "Hetudukaṃ": f"{HETU_N} {DUKA}",
    "Sahetukadukaṃ": f"{HETU_N} ရှိခြင်း {DUKA}",
    "Hetusampayuttadukaṃ": f"{HETU_N}နှင့် ယှဉ်တွဲခြင်း {DUKA}",
    "Hetusahetukadukaṃ": f"{HETU_N} ဖြစ်ခြင်းနှင့် {HETU_N} ရှိခြင်း {DUKA}",
    "Hetuhetusampayuttadukaṃ": f"{HETU_N} ဖြစ်ခြင်းနှင့် {HETU_N}နှင့် ယှဉ်တွဲခြင်း {DUKA}",
    "Nahetusahetukadukaṃ": f"{HETU_N} မဟုတ်ခြင်းနှင့် {HETU_N} ရှိခြင်း {DUKA}",
    "Sappaccayadukaṃ": f"{F.PACCAYA} ရှိခြင်း {DUKA}",
    "Saṅkhatadukaṃ": f"ပြုပြင်ဖန်တီးထားခြင်း {DUKA}",
    "Sanidassanadukaṃ": f"မြင်နိုင်ခြင်း {DUKA}",
    "Sappaṭighadukaṃ": f"ထိခိုက်မှု ရှိခြင်း {DUKA}",
    "Rūpīdukaṃ": f"ရုပ် ဖြစ်ခြင်း {DUKA}",
    "Lokiyadukaṃ": f"လောကနှင့် သက်ဆိုင်ခြင်း {DUKA}",
    "Kenaciviññeyyadukaṃ": f"တစ်စုံတစ်ခုသော စိတ်ဖြင့် သိနိုင်ခြင်း {DUKA}",
}
for _k, _v in DUKA_NAME.items():
    new(_k, _v)
HL_ADD = {
    "(Tatiyo bhāgo)": new("(Tatiyo bhāgo)", "(တတိယ အပိုင်း)"),
    "Dhammānulome dukapaṭṭhānaṃ": new("Dhammānulome dukapaṭṭhānaṃ",
                                     f"{F.HEAD['Dhammānulome']} {DUKA}တို့၏ {F.TITLE}"),
}
_H26 = G.HLINES["*2-6 Sahajāta-paccaya-nissaya-saṃsaṭṭha-sampayuttavāro*"][1:-1]          # 1-03 … 1-05
HL_ADD["2-6 Sahajāta-paccaya-nissaya-saṃsaṭṭha-sampayuttavāro"] = _H26
HL_ADD["2-6. Sahajāta-paccaya-nissaya-saṃsaṭṭha-sampayuttavāro"] = _H26.replace("2-6 ", "2-6. ")   # as 2-01 … 2-02
HL_ADD["4-6. Nissaya-saṃsaṭṭha-sampayuttavāro"] = new(
    "4-6. Nissaya-saṃsaṭṭha-sampayuttavāro", "4-6. " + (C + " ").join(F.HEAD[v][:-len(F.VARA)] for v in (
        "Nissayavāro", "Saṃsaṭṭhavāro")) + "နှင့် " + F.HEAD["Sampayuttavāro"])     # the pattern of 1-03 … 1-05
HL_ADD["*Vipākāhārapaccayā*"] = F.heading("*Vipāka-āhārapaccayā*")   # the «X-Ypaccayā» heading of the module
HL_ADD["Anulomapaccanīyaṃ"] = K.ORDER_N["anulomapaccanīyaṃ"]       # «အဟုတ်ပြ အငြင်းပြ ပုံစံ» (as 2-01 … 2-02)
HL_ADD.update(GOCCHAKA)
HL_ADD.update(DUKA_NAME)
for _k, _v in list(DUKA_NAME.items()) + list(GOCCHAKA.items()):
    HL_ADD[f"{_k} niṭṭhitaṃ."] = F.finished(_v)


def setup_names():
    F.HLINES.update(HL_ADD)


# ===================================================================================== Pāli preparation (in memory)
_U = {"u": "o", "uṃ": "aṃ", "uñca": "añca", "ussa": "assa", "ū": "ā", "ūnaṃ": "ānaṃ", "unā": "ena"}
_U_ALT = "ūnaṃ|uñca|ussa|unā|uṃ|ū|u"
_I = {"ī": "o", "iṃ": "aṃ", "iñca": "añca", "issa": "assa", "ino": "ā", "īnaṃ": "ānaṃ", "inā": "ena"}
_I_ALT = "|".join(sorted(_I, key=len, reverse=True))
_A_OF = {"o": "o", "a": "aṃ", "aṃ": "aṃ", "assa": "assa", "ā": "ā", "āna": "ānaṃ", "ānaṃ": "ānaṃ", "e": "e"}
_NB = r"(?!" + WCH + ")"
_PB = r"(?<!" + WCH + ")"
DHW = r"(?:dhamm|…)"


def _cap(m, s):
    return s[0].upper() + s[1:] if m[0][0].isupper() else s


def _pairfix(t, first, second):
    """«A B ca N» -> «A ca B ca N» when two terms are coordinated and the first one's own «ca» was folded in"""
    t = re.sub(_PB + "(" + first + r")(o|assa|ā|ānaṃ) (" + second + r"\w* ca" + _NB + ")", r"\1\2 ca \3", t,
               flags=re.I)
    t = re.sub(_PB + "(" + first + r")aṃ (" + second + r"\w*ñca" + _NB + ")", r"\1añca \2", t, flags=re.I)
    return t


def prep_dyad(t, d):
    if d == "hetu":
        # hetu as a term: before a dhamma word, or coordinated with nahetu before one
        t = re.sub(_PB + r"([Hh])et(" + _U_ALT + r")(?= (?:ca )?(?:[Nn]ahet\w*(?: ca)? )?dhamm)",
                   lambda m: m[1] + "etudk" + _U[m[2]], t)
        t = re.sub(_PB + r"([Nn])ahet(" + _U_ALT + ")" + _NB, lambda m: m[1] + "ahetudk" + _U[m[2]], t)
    elif d == "hetusahetuka":
        t = re.sub(_PB + r"([Hh])etu\w*?(?:ñceva| ceva) sahetuk(o|a|assa|ā|āna|e)(?:ñca| ca)" + _NB,
                   lambda m: m[1] + "etusahetukdk" + _A_OF[m[2]], t)
        t = re.sub(_PB + r"([Ss])ahetuk(o|a|aṃ|assa|ā|āna|e)(?:ñceva| ceva) na ca het(" + _U_ALT + ")" + _NB,
                   lambda m: m[1] + "ahetukanahetudk" + _U[m[3]], t)
        t = _pairfix(t, "hetusahetukdk", "sahetukanahetudk")
    elif d == "hetuhetusamp":
        t = re.sub(_PB + r"([Hh])etu\w*?(?:ñceva| ceva) hetusampayutt(o|a|assa|ā|āna|e)(?:ñca| ca)" + _NB,
                   lambda m: m[1] + "etuhetusampdk" + _A_OF[m[2]], t)
        t = re.sub(_PB + r"([Hh])etusampayutt(o|a|aṃ|assa|ā|āna|e)(?:ñceva| ceva) na ca het(" + _U_ALT + ")" + _NB,
                   lambda m: m[1] + "etusampnahetudk" + _U[m[3]], t)
        t = _pairfix(t, "hetuhetusampdk", "hetusampnahetudk")
    elif d == "nahetusahetuka":
        t = re.sub(_PB + r"([Nn])ahet(?:uṃ|ū|ussa|u) (a?)hetuk(?=" + WCH + ")", lambda m: m[1] + "ahetu" + m[2] + "hetuk"
                   if m[2] else m[1] + "ahetusahetuk", t)
        t = re.sub(_PB + r"([Nn])ahet(?:uṃ|ū|ussa|u) sahetuk(?=" + WCH + ")", lambda m: m[1] + "ahetusahetuk", t)
    elif d == "kenaci":
        pass
    if d in ("hetu", "hetusahetuka"):
        # «-cittasamaṅgissa» on a term («nahetucittasamaṅgissa», «sahetukā ceva na ca hetucittasamaṅgissa»)
        t = re.sub(_PB + r"([Nn])ahetucittasamaṅgissa", r"\1ahetudkacittasamaṅgissa", t)
        t = re.sub(_PB + r"([Ss])ahetukā ceva na ca hetucittasamaṅgissa", r"\1ahetukanahetudkacittasamaṅgissa", t)
        t = re.sub(_PB + r"([Hh])etu ceva sahetukādhipati" + _NB, r"\1etusahetukdkādhipati", t)
    # «X-ādhipati» = «X-o adhipati» (the term qualifies the noun adhipati, as make_ch1-03-05 / make_ch2-03-06)
    if d:
        keys = "|".join(f"[{k[0].upper()}{k[0]}]" + re.escape(k[1:]) for k in sorted(DYADS[d], key=len, reverse=True))
        t = re.sub(_PB + "(" + keys + r")ādhipati" + _NB, r"\1o adhipati", t)
    if d == "rupi":
        t = re.sub(_PB + r"([Aa]r|[Rr])ūp(" + _I_ALT + r")(?= (?:ca )?(?:[Aa]rūp\w*(?: ca)? )?dhamm)",
                   lambda m: m[1] + "ūpdk" + _I[m[2]], t)
        _ialt = "|".join(sorted((k for k in _I if k != "ino"), key=len, reverse=True))
        t = re.sub(_PB + r"([Aa]r|[Rr])ūp(" + _ialt + ")" + _NB, lambda m: m[1] + "ūpdk" + _I[m[2]], t)
        t = re.sub(_PB + r"([Aa]r|[Rr])ūpicittasamaṅgissa", r"\1ūpdkacittasamaṅgissa", t)
    if d:
        t = both_terms(t, d)
    return t


_BOTH_END = {"añca": "añca", "ānañca": "ānañca", "ā ca": "ā", "o ca": "o", "e ca": "e", "assa ca": "assa",
             "ānaṃ ca": "ānaṃ"}


def both_terms(t, d):
    """«A-X ca B-X ca N» / «A-Xñca B-Xñca N» with N not a dhamma word -> «A_B_both-X N» (one ñca kept: it opens the
    conjunct); then a term without its «ca» before a qualifier with «-ñca» takes that «ca» («T-aṃ Q-añca rūpaṃ» =
    «T-añca Q-aṃ rūpaṃ»), and a second «ca» on that qualifier is dropped («T-añca Q-añca rūpaṃ»)"""
    a, b = [k for k in DYADS[d] if not k.endswith("_both")]
    both = a + "_" + b.replace(" ", "_") + "_both"
    ra = f"[{a[0].upper()}{a[0]}]" + re.escape(a[1:])
    rb = re.escape(b)
    for e, e2 in sorted(_BOTH_END.items(), key=lambda kv: -len(kv[0])):
        ex = re.escape(e)
        t = re.sub(_PB + "(" + ra + ")" + ex + " " + rb + ex + r"(?= (?!dhamm)|…)",
                   lambda m: (both[0].upper() if m[1][0].isupper() else both[0]) + both[1:] + e2, t)
    keys = "|".join(re.escape(k) for k in sorted(DYADS[d], key=len, reverse=True))
    # «T-aṃ kaṭattā ca rūpaṃ» = «T-añca kaṭattārūpaṃ» (the fixed «kaṭattā ca rūpaṃ» has the same Burmese)
    t = re.sub(_PB + "(" + keys + r")aṃ kaṭattā ca rūpaṃ" + _NB, r"\1añca kaṭattārūpaṃ", t)
    t = re.sub(_PB + "(" + keys + r")(aṃ|ānaṃ) (\w+?)(añca|ānañca) (?=rūp)",
               lambda m: f"{m[1]}{'añca' if m[2] == 'aṃ' else 'ānañca'} {m[3]}{'aṃ' if m[4] == 'añca' else 'ānaṃ'} ", t)
    t = re.sub(_PB + "(" + keys + r")(añca|ānañca) (\w+?)(añca|ānañca) (?=rūp)",
               lambda m: f"{m[1]}{m[2]} {m[3]}{'aṃ' if m[4] == 'añca' else 'ānaṃ'} ", t)
    return t


# «X ca sampayuttakā ca khandhā» / «Xñca sampayuttake ca khandhe» (the enclitic «ca» of the second member after its
# first word): read as «X ca sampayuttakā khandhā ca» (the module closes a conjunct after each «ca»)
_SAMP_CA = re.compile(r"(?<=ca) (sampayuttak(?:ā|e)) ca (khandh(?:ā|e))" + _NB)
# «hetuñca nahetuñca khandhe» (a noun, then a term on the next noun): the «ca» of the term read after its noun,
# «hetuñca nahetuṃ khandhe ca» (the same reading as «X ca sampayuttakā ca khandhā»)
_TERM_CA = re.compile(r"(?<=ñca )(\w+dk)añca (khandh(?:e|ā))" + _NB)


def prep(text, d):
    text = M.prep(text)
    for i, k in enumerate(NOTEP):
        text = text.replace(k, f"(⁑d{i})")
    for a, b in SLIP_FIX.items():
        if a in text:
            F.SLIPS.add(f"«{a}» read as «{b}»")
            text = text.replace(a, b)
    return M._outside_braces(text, lambda t: _TERM_CA.sub(r"\1aṃ \2 ca", _SAMP_CA.sub(r" \1 \2 ca", _CA_AFTER.sub(" ca ", prep_dyad(t, d)))))


# ===================================================================================== the run: parts by dyad
DYAD_HEAD = re.compile(r"^###### (\S+dukaṃ) \^", re.M)


def parts_of(src):
    """[(dyad, text)]: the chapter cut before each dyad heading (the lines before the first go with the first)"""
    cuts = [m.start() for m in DYAD_HEAD.finditer(src) if m[1] in DYAD_OF]
    if not cuts:
        raise SystemExit("no dyad heading")
    starts = [0] + cuts[1:]
    out = []
    for i, s in enumerate(starts):
        e = starts[i + 1] if i + 1 < len(starts) else len(src)
        name = DYAD_HEAD.search(src, cuts[i])[1]
        out.append((DYAD_OF[name], src[s:e]))
    return out


TERM_REF = {}
# a dyad term named inside a note of its own dyad («Hetu dhammo … (hetumūlake tīṇi)»: the series that starts from the
# term hetu, not the condition); make_ch2-03-06's note frame «X-mūlake N» reads TERM_REF first
TERM_REFS = {"hetu": {"hetu": f"{HETU} {F.DHAMMA}"}}


def chapter_notes(text, d=None):
    """as make_ch2-03-06.chapter_notes: every note of the part registered for the chains (F.NOTES)"""
    M.TERM_REF.clear()
    M.TERM_REF.update(TERM_REF)
    M.TERM_REF.update(TERM_REFS.get(d, {}))
    src = re.sub(r"\{[^{}]*\}", "", text)
    for m in re.finditer(r"\(([^()]*)\)", src):
        k = m[0]
        if re.fullmatch(r"\(\d+\)", k) or k in F.NOTES:
            continue
        r = K.note_unit(k)
        if r is not None:
            F.NOTES[k] = r
            FG.NOTES.setdefault(k, r)
        pieces = re.split(r"(?<=\.) (?=\S)", m[1])
        if len(pieces) > 1:
            last = pieces[-1] + ")"
            r = K.note_unit(last)
            if r is not None:
                F.NOTES.setdefault(F.lc(last), r)
                FG.NOTES.setdefault(F.lc(last), r)


def translate_part(d, text):
    set_dyad(F, d)
    set_dyad(FG, d)
    t = prep(text, d)
    chapter_notes(t, d)
    FG.translate("")                   # (re)builds the fallback's frame regexes
    return F.translate(t)


def translate(name):
    src = (PALI / name).read_text(encoding="utf-8-sig")
    outs = [translate_part(d, t) for d, t in parts_of(src)]
    return "\n".join(outs)


# ===================================================================================== nouns and lexicon
# the roots as nouns (pi-1 termbase: alobho «လောဘ မရှိခြင်း» …, lobho «လောဘ», doso «ဒေါသ», moho «မောဟ»); hetu (noun)
# «အမြစ်» (pi-1 ^1-M2-1, the module's NOUN «hetū»)
MAHAB_ = F.NOUN["mahābhūtā"][0]
APO = W("āpodhātu", "ရေဓာတ်", "1")
INDR = {"itthindriya": W("itthindriyaṃ", "မိန်းမ၏ စွမ်းရည်", "1"), "purisindriya": W("purisindriyaṃ", "ယောက်ျား၏ စွမ်းရည်", "1"),
        "jīvitindriya": W("jīvitindriyaṃ", "အသက်၏ စွမ်းရည်", "1")}
VANNA = new("vaṇṇasampadā", "အဆင်းအရောင် ပြည့်စုံခြင်း")            # as 2-12 … 2-17 (in progress)
PATTHAY = new("patthayamāno", "တောင့်တလျက်")                          # as 2-12 … 2-17 (patthanā «တောင့်တခြင်း»)
HETU_ADHIPATI = new("hetu adhipati", f"{HETU_N} {F.N['adhipati']}")    # as «chandādhipati» «ဆန္ဒ အကြီးအမှူး»
ROOT_N = {"alobh": W("alobho", "လောဘ မရှိခြင်း", "1"), "ados": W("adoso", "ဒေါသ မရှိခြင်း", "1"),
          "amoh": W("amoho", "မောဟ မရှိခြင်း", "1"), "lobh": W("lobho", "လောဘ", "1"),
          "dos": W("doso", "ဒေါသ", "1"), "moh": W("moho", "မောဟ", "1")}
_ROOT_CASE = {"o": ("n", "n"), "aṃ": ("a", "a"), "assa": ("g", "g")}
HETU_FORMS = {"hetu": ("n", False, "n"), "hetuṃ": ("a", False, "a"), "hetussa": ("g", False, "g"),
              "hetū": ("n", True, "n"), "hetūnaṃ": ("g", True, "g")}


def setup_lex():
    for mod in (F, FG):
        for st, my in ROOT_N.items():
            for e, (case, lk) in _ROOT_CASE.items():
                mod.add_fixed(my, case, False, st + e)
                mod.LEX.setdefault(st + e, (my, lk))
        for w, (case, pl, lk) in HETU_FORMS.items():
            mod.add_fixed(HETU_N, case, pl, w)
            mod.LEX.setdefault(w, (HETU_N + ("+" if pl else ""), lk))
        mod.add_noun(mod.N["adhipati"], n=["adhipati"])                   # as make_ch1-03-05 (the noun adhipati)
        mod.add_fixed(HETU_ADHIPATI, "n", False, "hetu adhipati")
        mod.add_qual(mod.QUAL["sampayuttakā"], "sampayuttake")
    # coordinations for the lexicon frames (rendered once by the noun-phrase engine, so that they equal the other
    # frames): «hetū ca sampayuttakā khandhā ca» (as prep() reads «hetū ca sampayuttakā ca khandhā») …
    for first in ("hetū", "hetuñca", "alobho", "lobho", "doso", "moho", "alobhañca", "lobhañca", "dosañca",
                  "mohañca"):
        acc = first.endswith("ñca")
        ph = f"{first} sampayuttake khandhe ca" if acc else f"{first} ca sampayuttakā khandhā ca"
        my = F.np_my(ph.split(), iter([]), "@ārabbha" if acc else "n")[0]
        for mod in (F, FG):
            mod.LEX.setdefault(ph, (my, "x"))
    for mod in (F, FG):
        mod.add_fixed(f"{MAHAB_} {M.SABBE}", "n", False, "sabbe mahābhūtā")   # («အားလုံး»: no «များ»)
        mod.LEX.setdefault("moho ca", (f"{ROOT_N['moh']}{F.LAKAUNG}", "x"))
        mod.LEX.setdefault("mohassa ca", (f"{ROOT_N['moh']}အား{F.LAKAUNG}", "x"))
        mod.EDNOTES["ākāsānañcāyatanakiriyaṃ (syā.) evamuparipi tīsu ṭhānesu"] = (
            f"{mod.VAR_P} (Syā.): ākāsānañcāyatanakiriyaṃ{C} " + new("evamuparipi tīsu ṭhānesu",
                                                                    "နောက်တွင်လည်း နေရာ သုံးခု၌ ဤနည်းတူ"))
    # rūpa words of 3-02 (pi-1 / pi-2 termbases): āpodhātu «ရေဓာတ်», itthindriya / purisindriya / jīvitindriya
    for mod in (F, FG):
        for w, case in (("āpodhātu", "n"), ("āpodhātuṃ", "a"), ("āpodhātuyā", "g")):
            mod.add_fixed(APO, case, False, w)
            mod.LEX.setdefault(w, (APO, {"n": "n", "a": "na", "g": "g"}[case]))
        for st, my in INDR.items():
            mod.add_fixed(my, "n", False, st + "ṃ")
            mod.add_fixed(my, "g", False, st + "ssa")
            mod.LEX.setdefault(st + "ṃ", (my, "na"))
            mod.LEX.setdefault(st + "ssa", (my, "g"))
        mod.add_fixed(KABALI, "a", False, "kabaḷīkāraṃ āhāraṃ")
        mod.add_fixed(KABALI, "g", False, "kabaḷīkārassa āhārassa")
        mod.LEX.setdefault("kabaḷīkāraṃ āhāraṃ", (KABALI, "na"))
        mod.LEX.setdefault("kabaḷīkārassa āhārassa", (KABALI, "g"))
        for _p, _my in mod.FIXED.copy().items():           # the āyatana names in the genitive («cakkhāyatanassa»)
            if _p.endswith("āyatanaṃ") and _p[0].islower() and _my[1] == "n":
                mod.add_fixed(_my[0], "g", False, _p[:-1] + "ssa")
                mod.LEX.setdefault(_p[:-1] + "ssa", (_my[0], "g"))
        mod.add_qual(f"{mod.FIXED['cakkhuviññāṇaṃ'][0]}{mod.SAHAGATA}", "cakkhuviññāṇasahagatānaṃ")
        for _s in ("cakkhu", "sota", "ghāna", "jivhā", "kāya"):          # «X-viññāṇasahagataṃ» (as kāyaviññāṇa-)
            mod.add_qual(f"{K.CAKKHUVINNANA[_s]} သိစိတ်{mod.SAHAGATA}", f"{_s}viññāṇasahagataṃ")
        mod.add_qual(mod.FIXED["purejātassa imassa kāyassa"][0].split(" ဤ")[0], "purejātassa")
        mod.add_qual("ဤ", "imassa")
        mod.add_noun(mod.FIXED["imassa kāyassa"][0][len("ဤ"):], g=["kāyassa"])
        mod.LEX.setdefault("dānaṃ", (mod.LEX["dānaṃ datvā"][0].split("ကို")[0], "na"))
        for w in ("rūpino", "arūpino"):
            mod.LEX.setdefault(w, (mod.QUAL[w], "adj"))
        for a, b in (("bāhiraṃ", ("bāhirā", "bāhire")), ("āhārasamuṭṭhānaṃ", ("āhārasamuṭṭhānā", "āhārasamuṭṭhāne")),
                     ("utusamuṭṭhānaṃ", ("utusamuṭṭhānā", "utusamuṭṭhāne"))):
            for w in b:
                mod.LEX.setdefault(w, (mod.QUAL[a], "x"))
        mod.LEX.setdefault("vaṇṇasampadaṃ", (VANNA, "a"))
        mod.LEX.setdefault("vaṇṇasampadā", (VANNA, "n"))
        mod.LEX.setdefault("patthayamāno", ("ကို " + PATTHAY, "post"))
        mod.LEX.setdefault("lokiye ekaṃ", (f"{DYADS['lokiya']['lokiy']} {mod.DHAMMA}၌ {mod.COUNT['ekaṃ']}", "x"))
        mod.LEX.setdefault("lokuttare tīṇi", (f"{DYADS['lokiya']['lokuttar']} {mod.DHAMMA}၌ {mod.COUNT['tīṇi']}", "x"))
    ph = "hetū ca sampayuttake khandhe ca"                              # hetū (accusative plural)
    my = F.np_my(ph.split(), iter([]), "@ārabbha")[0]
    for mod in (F, FG):
        mod.LEX.setdefault(ph, (my, "x"))
    for ph in ("khandhā ca hetū ca",):
        my = F.np_my(ph.split(), iter([]), "n")[0]
        for mod in (F, FG):
            mod.LEX.setdefault(ph, (my, "x"))


# «tayo khandhā adoso amoho ca cittasamuṭṭhānañca rūpaṃ» (one «ca» after the last member): read as «tayo khandhā ca
# adoso amoho ca …», as make_ch2-03-06 / make_ch1-03-05 read «khandhā moho ca» / «khandhā vatthu ca»
_CA_AFTER = re.compile(r"(?:(?<= khandhā)|(?<= mahābhūtā)) (?=(?:adoso amoho|alobho amoho|alobho adoso|lobho|doso|hetu|hetū|"
                       r"āpodhātu) ca" + _NB + ")")


# ===================================================================================== editorial notes
# keys as make_ch1-01's note_body() sees them (lower-case first, «,» spaced); the words are those of 1-01 (K),
# 2-03 … 2-06 (M) and 2-01 … 2-02 where they exist (each listed in the notes file)
CAKKA = K.NOTE_FIXED["cakkaṃ kātabbaṃ"].split(" ")[0]              # «စက်ဝိုင်း» (1-01)
PATHAMA_GAMANA = f"ပထမ {M.GAMANA}"                                  # paṭhamagamanaṃ (2-03 … 2-06 gamanaṃ «သွားပုံ»)
KAT, VITTH, GAN, VIBHAJ = K.KATABBA, K.VITTH, K.GANETABBA, M.VIBHAJ
EVAM_T = M.EVAM_THUS                                               # evaṃ (alone) «ဤသို့» (2-03 … 2-06)
PANHA, NATTHI, PARIP, AVAS = K.PANHA, K.NATTHI, K.PARIPUNNA, K.AVASESA
SAB = M.SABBE                                                      # «အားလုံး»
MAHAB = M.MAHABHUTA
CNT = F.COUNT
NIYAM = M.NOTE_ADD['"uddhacca"nti niyāmetabbaṃ'].split("ဟု ")[1]   # «သတ်မှတ်ရမည်» (2-03 … 2-06)
PAV_PS = M.NOTE_ADD["pavattipaṭisandhi"]                           # «ဘဝ ဖြစ်စဉ်၌လည်း၊ ပဋိသန္ဓေ၌လည်း» (2-03 … 2-06)
NINNANA = M.NOTE_ADD["ninnānaṃ"]                                   # «ကွဲပြားမှု မရှိ» (2-03 … 2-06)
ASANNA = K.ASANNA                                                  # «အသညသတ်» (pi-5)
YAVA_AS = new("yāva asaññasattā", f"{ASANNA}တို့အထိ")            # yāva X «Xအထိ» (1-01 «yāvāsevanā … အထိ»)
IHA = new("iha / idha", "ဤနေရာ၌")                                  # as 2-03 … 2-06 «idha» «ဤနေရာ၌»
NO_GH = f"{IHA} {F.GHATANA} {NATTHI}"                              # iha ghaṭanā natthi
NINNANAKARANA = new("ninnānākaraṇaṃ", f"{K.NANAKARANA} မရှိ")      # (1-01 nānākaraṇaṃ «ကွဲပြားချက်»)
IMINA = new("iminā kāraṇena", "ဤနည်းလမ်းဖြင့်")                   # = 2-01 … 2-02
ARUPA_N = F.ARUPA + " " + F.DHAMMA                                # arūpa (noun) «ရုပ် မဟုတ်သော သဘောတရား» (2-01 … 2-02)
MULA = new("mūla (the starting point of a series)", "အခြေခံ")      # (1-01 «imāni tīṇi mūlāni» «ဤ အခြေခံ သုံးခု»)
PUCCH = new("pucchitabbaṃ / -āni", "မေးရမည်")
EKASADISA = new("ekasadisaṃ / -ā", "တူညီကြသည်")                   # (1-01 «ekasadisāni» «တူညီကြသည်»)
EKAYEVA = new("ekāyeva / ekoyeva pañhā", f"{PANHA} တစ်ခုတည်း")
ITARE = new("itare (the others)", "အခြား")
VAJJ = new("vajjetabbā", "ဖယ်ရှားရမည်")
CHADD = new("chaḍḍetvā", "ဖယ်၍")
DASSET = new("dassetabbāni", "ပြသရမည်")                              # = 2-01 … 2-02 «dassetabbo»
LABBH = new("yathā labbhanti / yathā yathā labbhati", "တွေ့ရသည့်အတိုင်း")
AGGE = new("agge", "ရှေ့ဆုံးတွင်")
PAVATTE = new("pavatte (in the course of life)", "ဘဝ ဖြစ်စဉ်၌")      # (2-03 … 2-06 pavatti «ဘဝ ဖြစ်စဉ်»)
MATIKA = W("Mātikā", "ခေါင်းစဉ်စာရင်း", "1")
ANUL_MATIKA = new("anulomamātikā", f"{K.ORDER_N['anulomaṃ']}၏ {MATIKA}")
SUDDHAKE = new("suddhake", f"{F.HEAD['Suddhaṃ']} အပိုင်း၌")
VARA = K.vara
PATICCA_V = VARA("paṭicca")
AJJH = M.AJJHATTIKA                                                 # «အတွင်းပိုင်း ဖြစ်သော» (pi-1)
BAHIRA = K.BAHIRA                                                   # «ပြင်ပ» (pi-1)
KABALI = F.FIXED["kabaḷīkāro āhāro"][0]
RJIVIT = F.FIXED["rūpajīvitindriyaṃ"][0]
JIVIT = W("jīvitindriyaṃ", "အသက်၏ စွမ်းရည်", "1")


def _pi(*vs):
    """«Xvāropi Yvāropi …» = «Xလည်း၊ Yလည်း …»"""
    return (C + " ").join(VARA(v) + "လည်း" for v in vs)


def _pi_obj(*vs):
    return (C + " ").join(VARA(v) + "ကိုလည်း" for v in vs)


NOTE_ADD = {}


def _notes():
    cn, cd, N = F.cname, F.cond, F.N
    return {
        "cakkaṃ": CAKKA,
        "paṭhamagamanaṃyeva": new("paṭhamagamanaṃyeva", f"{PATHAMA_GAMANA}အတိုင်းပင်"),
        "yathā paṭhamagamanaṃ evaṃ ninnānaṃ": f"{PATHAMA_GAMANA}{K.KAYYA} {K.EVAM} {NINNANA}",
        "āvajjanā natthi": f"{F.LEX['āvajjanā'][0]} {NATTHI}",
        "imesu dvīsu nava": f"ဤ {CNT['dve']}၌ {CNT['nava']}",
        "sahajātavāropi paccayavāropi nissayavāropi paṭiccavārasadisāyeva pañhā":
            f"{_pi('sahajāta', 'paccaya', 'nissaya')} {PATICCA_V}နှင့် တူသော {PANHA}များပင်",
        "saṃsaṭṭhavāropi sampayuttavāropi paripuṇṇo": f"{_pi('saṃsaṭṭha', 'sampayutta')} {PARIP}သည်",
        "rūpaṃ natthi , arūpameva": f"ရုပ် {NATTHI}{C} {ARUPA_N}သာ",
        "dutiyaupanissayasadisaṃ": f"ဒုတိယ {N['upanissaya']}{F.SADISA}",
        "dvīsupi paṭisandhi natthi": f"{CNT['dve']}လုံး၌ {F.PATISANDHI} {NATTHI}",
        "evaṃ indriyapaccayā vitthāretabbā": f"{cn('indriya')}ကို {EVAM_T} {VITTH}",
        "imaṃ nānaṃ": f"ဤသည် {K.NANAKARANA} ဖြစ်သည်",
        "ime dvepi paṭiccasadisā": f"ဤ {CNT['dve']}လုံးသည် {PATICCA_V}{K.SADISANI}",
        "rūpaṃ chaḍḍetvā arūpeyeva nava pañhā": f"ရုပ်ကို {CHADD} {F.PREFIX['arūpe']}ပင် {PANHA} {CNT['nava']}",
        "sabbe mahābhūtā yāva asaññasattā": f"{MAHAB} {SAB} {YAVA_AS}",
        "tattha tattha ṭhitena imaṃ kātabbaṃ dutiyagamanasadisaṃ":
            f"ထိုထို နေရာ{K.THITA} ဤသည်ကို ဒုတိယ {M.GAMANA}နှင့် တူအောင် {KAT}",
        "vitthāretabbaṃ yāva": new("vitthāretabbaṃ yāva", f"အောက်ပါအထိ {VITTH}"),
        "vitthāretabbaṃ": VITTH,
        "yathā hetusahetukadukaṃ evaṃ vitthāretabbaṃ , ninnānākaraṇaṃ":
            f"{DUKA_NAME['Hetusahetukadukaṃ']}{K.KAYYA} {K.EVAM} {VITTH}{C} {NINNANAKARANA}",
        "iminā kāraṇena vitthāretabbaṃ yathā sahetukadukaṃ ninnānākaraṇaṃ":
            f"{IMINA} {DUKA_NAME['Sahetukadukaṃ']}{K.KAYYA} {NINNANAKARANA} {VITTH}",
        "dve mūlāni pucchitabbāni": f"{MULA} {CNT['dve']}ကို {PUCCH}",
        "mūlaṃ kātabbaṃ": f"{MULA}ကို {KAT}",
        "mūlaṃ pucchitabbaṃ": f"{MULA}ကို {PUCCH}",
        "imesaṃ dvinnampi pañhānaṃ mūlāni pucchitabbāni": f"ဤ {PANHA} {CNT['dve']}လုံး၏ {MULA}တို့ကို {PUCCH}",
        "sahajātavāropi paccayavāropi nissayavāropi saṃsaṭṭhavāropi sampayuttavāropi paṭiccavārasadisā":
            f"{_pi('sahajāta', 'paccaya', 'nissaya', 'saṃsaṭṭha', 'sampayutta')} {PATICCA_V}{K.SADISANI}",
        "sahetuko ceva na ca hetumūlakaṃ tīṇipi ekasadisā":
            f"{DYADS['hetusahetuka']['sahetukanahetudk']} {F.DHAMMA}{F.MULAKA}၌ {CNT['tīṇi']}လုံး {EKASADISA}",
        "sahetuko ceva na ca hetumūlake iminākārena vitthāretabbā avasesā dve pañhā":
            (f"{DYADS['hetusahetuka']['sahetukanahetudk']} {F.DHAMMA}{F.MULAKA}၌ ကြွင်းသော {PANHA} {CNT['dve']}ကို "
             + new("iminākārena", "ဤ ပုံစံအတိုင်း") + f" {VITTH}"),
        "evaṃ vitthāretabbaṃ": f"{EVAM_T} {VITTH}",
        "indriyanti niyāmetabbaṃ , navapi paripuṇṇaṃ":
            f"{N['indriya']}ဟု {NIYAM}{C} {CNT['nava']}လုံး {PARIP}သည်",
        "paripuṇṇaṃ nava": f"{PARIP}စွာ {CNT['nava']}",
        "tīṇipi paccayā paṭiccavāre hetusadisā": f"{F.PACCAYA} {CNT['tīṇi']}လုံးသည် {PATICCA_V}၌ {N['hetu']}{K.SADISANI}",
        "navapi vipākanti niyāmetabbaṃ": f"{CNT['nava']}လုံးကို {N['vipāka']}ဟု {NIYAM}",
        "yathā paṭiccavārasadisaṃ": f"{PATICCA_V}နှင့် တူသည့်အတိုင်း",
        "evaṃ avasesāpi dve gaṇanā gaṇetabbā": f"ကြွင်းသော {S.GANANA} {CNT['dve']}ကိုလည်း {EVAM_T} {GAN}",
        "sahajātavārepi evaṃ gaṇetabbaṃ": f"{VARA('sahajāta')}၌လည်း {EVAM_T} {GAN}",
        "cattāripi kātabbāni": f"{CNT['cattāri']}လုံးကို {KAT}",
        "ghaṭanā tīṇi , pavattipaṭisandhi paripuṇṇaṃ": f"{F.GHATANA} {CNT['tīṇi']}{C} {PAV_PS} {PARIP}သည်",
        "iha ghaṭanā natthi , satta pañhā": f"{NO_GH}{C} {PANHA} {CNT['satta']}",
        "pavattipaṭisandhi satta pañhā , iha ghaṭanā natthi": f"{PAV_PS} {PANHA} {CNT['satta']}{C} {NO_GH}",
        "evaṃ vibhajitabbaṃ": f"{EVAM_T} {VIBHAJ}",
        "yāva asaññasattā moho natthi": f"{YAVA_AS} {F.NOUN['moho'][0]} {NATTHI}",
        "yāva asaññasattā": YAVA_AS,
        "sabbaṃ yāva asaññasattā tāva kātabbaṃ": f"{SAB}ကို {YAVA_AS} {KAT}",
        "āvajjanampi bhavaṅgampi natthi , āsevanapaccaye vajjetabbā navapi":
            (f"{F.LEX['āvajjanā'][0]}လည်း{C} {F.LEX['bhavaṅgaṃ'][0]}လည်း {NATTHI}{C} {cd('āsevana', 'loc')} "
             f"{CNT['nava']}လုံးကို {VAJJ}"),
        "anulomasahajātasadisā": f"{K.ORDER_N['anulomaṃ']}၏ {cn('sahajāta')}{K.SADISANI}",
        "ime pañca pañhā hetusadisā , ninnānaṃ": f"ဤ {PANHA} {CNT['pañca']}သည် {N['hetu']}{K.SADISANI}{C} {NINNANA}",
        "bāhirā mahābhūtā natthi": f"{BAHIRA} {MAHAB}တို့ {NATTHI}",
        "paṭiccavārasadisaṃyeva": f"{PATICCA_V}{F.SADISA}ပင်",
        "paṭiccavāre nissayapaccayasadisaṃ , iha ghaṭanā natthi":
            f"{PATICCA_V}၌ {cn('nissaya')}{F.SADISA}{C} {NO_GH}",
        "paṭiccavāre sahajātasadisaṃ , iha ghaṭanā natthi": f"{PATICCA_V}၌ {cn('sahajāta')}{F.SADISA}{C} {NO_GH}",
        "paṭiccavāre sampayuttasadisā cha pañhā": f"{PATICCA_V}၌ {cn('sampayutta')}နှင့် တူသော {PANHA} {CNT['cha']}",
        "sahetukamūlakaṃ paṭiccavārasadisaṃ":
            f"{SAHETUKA} {F.DHAMMA}{F.MULAKA}သည် {PATICCA_V}{F.SADISA}",
        "saṃkhittaṃ , yāva asaññasattā": f"{F.NOTES['(saṃkhittaṃ)'][1:-1]}{C} {YAVA_AS}",
        "yāva asaññasattā kātabbaṃ": f"{YAVA_AS} {KAT}",
        "yāva asaññasattā tāva vitthāro": f"{YAVA_AS} " + new("vitthāro", "အကျယ် ချဲ့ခြင်း"),
        # 3-02
        "sahajātavāropi paccayavāropi nissayavāropi saṃsaṭṭhavāropi sampayuttavāropi evaṃ vitthāretabbā":
            f"{_pi_obj('sahajāta', 'paccaya', 'nissaya', 'saṃsaṭṭha', 'sampayutta')} {EVAM_T} {VITTH}",
        "paccayavāre vatthu ca pañcāyatanāni ca dassetabbāni":
            (f"{VARA('paccaya')}၌ {F.VATTHU}ကို{F.LAKAUNG}{C} " + new("pañcāyatanāni", "အာရုံခံ နယ်ပယ် ငါးပါး")
             + f"တို့ကို{F.LAKAUNG} {DASSET}"),
        "yathā yathā labbhati taṃ taṃ kātabbaṃ": f"{LABBH} ထိုထို အရာကို {KAT}",
        "evaṃ cattāripi gaṇanā paripuṇṇā": f"{EVAM_T} {S.GANANA} {CNT['cattāri']}လုံး {PARIP}ကြသည်",
        "saṃsaṭṭhavāro evaṃ vitthāretabbo , saha gaṇanāhi dve pañhā":
            f"{VARA('saṃsaṭṭha')}ကို {EVAM_T} {VITTH}{C} {S.GANANA}တို့နှင့်တကွ {PANHA} {CNT['dve']}",
        "anulomamātikā kātabbā": f"{ANUL_MATIKA}ကို {KAT}",
        "anulomamātikā gaṇetabbā": f"{ANUL_MATIKA}ကို {GAN}",
        "naanantarapadādī paccanīyasadisā": f"{cd('anantara', 'n', True)} {F.PADA} {F.ADI}တို့သည် {K.ORDER_N['paccanīyaṃ']}{K.SADISANI}",
        "nasamanantarapadādī paccanīyasadisā":
            f"{cd('samanantara', 'n', True)} {F.PADA} {F.ADI}တို့သည် {K.ORDER_N['paccanīyaṃ']}{K.SADISANI}",
        "pañca pañhā , ghaṭanā natthi": f"{PANHA} {CNT['pañca']}{C} {F.GHATANA} {NATTHI}",
        "paṭisandhi kātabbā": f"{F.PATISANDHI}ကို {KAT}",
        "evaṃ paccanīyādīni gaṇanāpi sampayuttavārepi sabbe kātabbā":
            (f"{EVAM_T} {K.ORDER_N['paccanīyaṃ']} {F.ADI}တို့၏ {S.GANANA}တို့ကိုလည်း{C} {VARA('sampayutta')}၌လည်း "
             f"{SAB}ကို {KAT}"),
        "ekoyeva pañho": EKAYEVA,
        "ekāyeva pañhā": EKAYEVA,
        "nissayavāropi paccayavārasadiso": f"{VARA('nissaya')}သည်လည်း {VARA('paccaya')}{F.SADISA}",
        "sahajātavāropi paṭiccavārasadiso": f"{VARA('sahajāta')}သည်လည်း {PATICCA_V}{F.SADISA}",
        "sampayuttavāropi saṃsaṭṭhavārasadiso": f"{VARA('sampayutta')}သည်လည်း {VARA('saṃsaṭṭha')}{F.SADISA}",
        "evaṃ avasesā pañhā , pavattipaṭisandhi vibhajitabbā": f"ကြွင်းသော {PANHA}တို့လည်း {EVAM_T}ပင်{C} {PAV_PS} {VIBHAJ}",
        "pavattipaṭisandhi kātabbā": f"{PAV_PS} {KAT}",
        "paṭiccasadisaṃ": f"{PATICCA_V}{F.SADISA}",
        "sabbe kātabbā": f"{SAB}ကို {KAT}",
        "evaṃ sabbe kātabbā": f"{EVAM_T} {SAB}ကို {KAT}",
        "saṃkhittaṃ , sabbe kātabbā": f"{F.NOTES['(saṃkhittaṃ)'][1:-1]}{C} {SAB}ကို {KAT}",
        "nissayavāropi evaṃ kātabbo": f"{VARA('nissaya')}ကိုလည်း {EVAM_T} {KAT}",
        "itarepi dve kātabbā": f"{ITARE} {CNT['dve']}ကိုလည်း {KAT}",
        "itarepi dve pañhā kātabbā": f"{ITARE} {PANHA} {CNT['dve']}ကိုလည်း {KAT}",
        "tīsupi kabaḷīkāro āhāro kātabbo": f"{CNT['tīṇi']}လုံး၌ {KABALI}ကို {KAT}",
        "tīsupi rūpajīvitindriyaṃ": f"{CNT['tīṇi']}လုံး၌ {RJIVIT}",
        "imaṃ dukaṃ yathā sappaccayadukaṃ , evaṃ gaṇetabbaṃ , ninnānākaraṇaṃ":
            f"ဤ {DUKA}ကို {DUKA_NAME['Sappaccayadukaṃ']}{K.KAYYA} {K.EVAM} {GAN}{C} {NINNANAKARANA}",
        "evaṃ paccayavāropi nissayavāropi saṃsaṭṭhavāropi sampayuttavāropi vitthāretabbo , sabbattha ekāyeva pañhā":
            f"{EVAM_T} {_pi_obj('paccaya', 'nissaya', 'saṃsaṭṭha', 'sampayutta')} {VITTH}{C} {K.SABBATTHA} {EKAYEVA}",
        "dve pañhā upanissayamūlaṃ": f"{cn('upanissaya')}{F.MULAKA}၌ {PANHA} {CNT['dve']}",
        "sabbattha ekāyeva pañhā": f"{K.SABBATTHA} {EKAYEVA}",
        "avasesā pañca pañhā paṭiccavārasadisā": f"ကြွင်းသော {PANHA} {CNT['pañca']}သည် {PATICCA_V}{K.SADISANI}",
        "avasesā dvepi pañhā kātabbā , paṭisandhi kabaḷīkāro āhāro dvīsupi kātabbo agge":
            (f"ကြွင်းသော {PANHA} {CNT['dve']}လုံးကို {KAT}{C} {F.PATISANDHI}နှင့် {KABALI}ကို {CNT['dve']}လုံး၌ "
             f"{AGGE} {KAT}"),
        "dvinnampi mūlā kātabbā": f"{CNT['dve']}လုံး၏ {MULA}တို့ကို {KAT}",
        "evaṃ paccanīyagaṇanāpi kātabbā": f"{EVAM_T} {K.ORDER_N['paccanīyagaṇanā']}ကိုလည်း {KAT}",
        "ime ajjhattikabāhirā mahābhūtā kātabbā": f"ဤ {AJJH}၊ {BAHIRA} {MAHAB}တို့ကို {KAT}",
        "paṭiccasadisaṃ yāva asaññasattā": f"{YAVA_AS} {PATICCA_V}{F.SADISA}",
        "paṭiccasadisā paṭhamapañhā": f"ပထမ {PANHA}သည် {PATICCA_V}{F.SADISA}",
        "paṭisandhi vajjetabbā , kaṭattārūpā ca":
            f"{F.PATISANDHI}ကို{F.LAKAUNG}{C} {F.KATATTARUPA}တို့ကို{F.LAKAUNG} {VAJJ}",
        "sabbaṃ saṃkhittaṃ": f"{SAB} {F.NOTES['(saṃkhittaṃ)'][1:-1]}",
        "tīsupi jīvitindriyaṃ agge kātabbaṃ": f"{CNT['tīṇi']}လုံး၌ {JIVIT}ကို {AGGE} {KAT}",
        "ghaṭanepi tīṇi pañhā kātabbā": f"{F.GHATANA}၌လည်း {PANHA} {CNT['tīṇi']}ကို {KAT}",
        "ajjhattikā bāhirā mahābhūtā sabbe jānitvā kātabbā":
            f"{AJJH}၊ {BAHIRA} {MAHAB} {SAB}ကို " + new("jānitvā", "သိ၍") + f" {KAT}",
        "arūpapañhāyeva": new("arūpapañhāyeva", f"{ARUPA_N}ဆိုင်ရာ {PANHA}သာ"),   # = 2-01 … 2-02 «arūpapañhameva»
        "nahetumūlakaṃ tīṇipi ekasadisaṃ": f"{NAHETU} {F.DHAMMA}{F.MULAKA}၌ {CNT['tīṇi']}လုံး {EKASADISA}",
        "vipākavibhaṅge nava pañhā": f"{cn('vipāka')}၏ {K.ORDER_N['vibhaṅgo']}၌ {PANHA} {CNT['nava']}",
        **{f"sabbattha {w}": f"{K.SABBATTHA} {my}" for w, my in CNT.items()},
        "evaṃ sabbaṃ sappaccayagaṇanāhi saddhiṃ kātabbaṃ":
            f"{EVAM_T} {SAB}ကို {DUKA_NAME['Sappaccayadukaṃ']}၏ {S.GANANA}တို့နှင့်အတူ {KAT}",
        "dvepi vārā kātabbā": new("vārā (sections)", "ဖော်ပြချက်") + f" {CNT['dve']}လုံးကို {KAT}",
    }


# notes whose Pāli holds condition / term / count words (the slotter would cut them): prep() puts a placeholder
# «(⁑d<i>)» in their place (as make_ch2-07-11's NOTEP); key: the raw Pāli note (after the dyad prep)
def _notep():
    cn, cd, N = F.cname, F.cond, F.N
    sah = f"{cd('sahajāta', 'loc')} {CNT['satta']}{C} {NO_GH}"
    return {
        "(adhipatiyā nava pañhā pavatteyeva)": f"({cd('adhipati', 'loc')} {PANHA} {CNT['nava']} {PAVATTE}ပင်)",
        "(yathā hetupaccayā evaṃ vitthāretabbaṃ, navapi vipākanti niyāmetabbaṃ)":
            f"({cn('hetu')}{K.KAYYA} {K.EVAM} {VITTH}{C} {CNT['nava']}လုံးကို {N['vipāka']}ဟု {NIYAM})",
        "(jhānampi maggampi sahajātapaccayasadisā, bāhirā mahābhūtā natthi )":
            (f"({cn('jhāna')}လည်း{C} {cn('magga')}လည်း {cn('sahajāta')}{K.SADISANI}{C} {BAHIRA} {MAHAB}တို့ "
             f"{NATTHI})"),
        "(nahetupaccayā nava pañhā, ahetukanti niyāmetabbaṃ)":
            f"({cd('hetu', 'ab', True)} {PANHA} {CNT['nava']}{C} {F.AHETUKA[:-len("သော")]}သည်ဟု {NIYAM})",
        "(Sahajātapaccaye satta, iha ghaṭanā natthi. Aññamaññapaccaye cha, nissayapaccaye satta pañhā, iha ghaṭanā "
        "natthi)": (f"({sah}{END} {cd('aññamañña', 'loc')} {CNT['cha']}{C} {cd('nissaya', 'loc')} {PANHA} "
                    f"{CNT['satta']}{C} {NO_GH})"),
        "(Saṃsaṭṭhavārepi sabbattha ekaṃ, saṃkhittaṃ. Avigatapaccayā, ekāyeva pañhā. Dvepi vārā kātabbā.)":
            (f"({VARA('saṃsaṭṭha')}၌လည်း {K.SABBATTHA} {CNT['ekaṃ']}{C} {F.NOTES['(saṃkhittaṃ)'][1:-1]}{END} "
             f"{cd('avigata', 'ab')}{C} {EKAYEVA}{END} {NOTE_ADD['dvepi vārā kātabbā']}{END})"),
        "(Appaṭighamūlakaṃ itarepi dve pañhā kātabbā. Ghaṭanepi tīṇi pañhā kātabbā. Ajjhattikā bāhirā mahābhūtā "
        "sabbe jānitvā kātabbā.)":
            (f"({DYADS['sappatigha']['appaṭigh']} {F.DHAMMA}{F.MULAKA}၌ {ITARE} {PANHA} {CNT['dve']}ကိုလည်း {KAT}{END} "
             f"{NOTE_ADD['ghaṭanepi tīṇi pañhā kātabbā']}{END} "
             f"{NOTE_ADD['ajjhattikā bāhirā mahābhūtā sabbe jānitvā kātabbā']}{END})"),
        "(saṃkhittaṃ. Yāva vatthu nahetū ca khandhā tāva kātabbaṃ)":
            f"({F.NOTES['(saṃkhittaṃ)'][1:-1]}{END} {VATTHU_NAHETU_KH}အထိ {KAT})",
        "(yāva vatthu nahetū khandhā, ca tāva kātabbaṃ)": f"({VATTHU_NAHETU_KH}အထိ {KAT})",
        "(vitthāretabbaṃ yāva. Nahetū khandhā)":
            f"({NOTE_ADD['vitthāretabbaṃ yāva']}{END} {NAHETU} {F.KHANDHA}များ)",
        "(lokuttare arūpe vipākanti niyāmetabbaṃ)":
            f"({DYADS['lokiya']['lokuttar']} {F.DHAMMA}၌ {F.PREFIX['arūpe']} {N['vipāka']}ဟု {NIYAM})",
        "(naāsevanamūlake lokuttare suddhake vipākoti niyāmetabbaṃ, avasesā pakatikāyeva)":
            (f"({cd('āsevana', 'n', True)}{F.MULAKA}၌ {DYADS['lokiya']['lokuttar']} {F.DHAMMA}၏ {SUDDHAKE} "
             f"{N['vipāka']}ဟု {NIYAM}{C} {AVAS}တို့သည် " + new("pakatikāyeva", "ပကတိအတိုင်းပင်") + ")"),
    }


NOTEP = {}
VATTHU_NAHETU_KH = f"{F.VATTHU}နှင့် {NAHETU} {F.KHANDHA}တို့"     # «vatthu nahetū (ca) khandhā» inside a note


def setup_notes():
    NOTE_ADD.update(_notes())
    K.NOTE_FIXED.update(NOTE_ADD)
    NOTEP.update(_notep())
    for i, (p_, my) in enumerate(NOTEP.items()):
        new(p_, my)
        k = f"⁑d{i}"
        K.NOTE_FIXED[k] = my[1:-1]
        for mod in (F, FG):
            mod.NOTES[f"({k})"] = my
    for k, v in DUKA_NAME.items():              # a dyad named inside a note («yathā sahetukadukaṃ»)
        K.WORDS_N.setdefault(k[0].lower() + k[1:], v)


# ===================================================================================== unique sentences
SK_ADD, SKF_ADD = {}, {}
SLIP_FIX = {"ādhipatiyā cattāri": "adhipatiyā cattāri", "lokuttarasa dhammassa": "lokuttarassa dhammassa"}       # source slips (read as the usual form; logged)


def _key(pali, d=None):
    """the skeleton of a Pāli unit as the engine sees it (with dyad d active)"""
    set_dyad(F, d)
    try:
        return F.slot(F.lc(F.pe(prep(pali, d).strip())))[0]
    finally:
        set_dyad(F, None)


def setup_sk():
    kh, lk = F.KHANDHA, F.LAKAUNG
    SKF_ADD.update({
        "dve khandhā ca": f"{kh} {F.PAA[2]}{lk}",                          # cut short (as 2-07 … 2-11)
        "§T§ā khandhā purejātassa": f"{{T1}} {kh}တို့သည် {F.FIXED['purejātassa imassa kāyassa'][0].split(' ဤ')[0]}",
        "kabaḷīkāro āhāro imassa kāyassa": f"{KABALI}သည် {F.FIXED['imassa kāyassa'][0]}အား",
        # cut short by «…» after the second recipient (its noun left out, as the Pāli)
        "§T§o eko khandho tiṇṇannaṃ khandhānaṃ §T§ānañca":
            (f"{{T1}} {kh} {F.PAA[1]}သည် " + F.np_my(["tiṇṇannaṃ", "khandhānaṃ"], iter([]), "g")[0]
             + f"{lk}{C} {{T2}}"),
    })
    rup = F.FIXED["rūpāyatanaṃ"][0]
    pho = F.FIXED["phoṭṭhabbāyatanaṃ"][0]
    SK_ADD.update({
        _key('Mahābhūtesu niṭṭhitesu "vatthuṃ paccayā"ti kātabbā.'):
            f"{MAHAB}တို့ " + new("niṭṭhitesu", "ပြီးဆုံးသောအခါ") + f" “{F.LINK['paccayā'](F.VATTHU)}”ဟု {KAT}{END}",
        _key("Pañcāyatanāni anulomepi paccanīyepi yathā labbhanti tathā kātabbā."):
            (f"{NOTE_ADD_P['pañcāyatanāni']}တို့ကို {K.ORDER_L['anulome']}လည်း{C} {K.ORDER_L['paccanīye']}လည်း "
             f"{LABBH} {KAT}{END}"),
        _key("Rūpāyatanaṃ cakkhuviññāṇassa…pe… phoṭṭhabbāyatanaṃ kāyaviññāṇassāti idaṃ natthi)."):
            (f"{rup}သည် {F.FIXED_CV['cakkhu']}အား{PE} {pho}သည် {F.FIXED_CV['kāya']}အားဟူသော ဤသည် {NATTHI}){END}"),
    })
    for mod in (F, FG):
        mod.SK.update(SK_ADD)
        mod.SKF.update(SKF_ADD)


NOTE_ADD_P = {}
_K_UNIT = None
LABEL_NODASH = re.compile(r"^(Sahajātādhipati) (?!–)(\S.*)$")


def unit_my(u):
    lead = u[:len(u) - len(u.lstrip())]
    m = LABEL_NODASH.match(u.strip())
    if m:                     # a kind label without its « – » (source slip; no dash added)
        F.SLIPS.add(f"«{m[1]}» without « – » (no dash added)")
        return lead + F.LEX[m[1].lower()][0] + " " + _K_UNIT(m[2])
    return _K_UNIT(u)


# a term before an asyndetic list of rūpa nouns («anidassanaṃ cittasamuṭṭhānaṃ rūpaṃ kaṭattārūpaṃ upādārūpaṃ»): the
# term before the list, as in the Pāli (make_ch1-01's list rule takes term-free lists only)
_K_NP = None


def np_my(words, terms, role):
    vals = [next(terms) for w in words if w.startswith("§T§")]
    try:
        return _K_NP(words, iter(vals), role)
    except (KeyError, StopIteration):
        ws = [w.rstrip(",") for w in words]
        if not (len(ws) > 2 and ws[0].startswith("§T§") and ws[0][3:] in ("aṃ", "ānaṃ", "añca", "ānañca")
                and len(vals) == 1):
            raise
    r, pl, k = _K_NP(words[1:], iter([]), role)
    return f"{vals[0]} {r}", pl, k + 1


def setup():
    global _K_UNIT, _K_NP
    setup_names()
    setup_lex()
    setup_notes()
    NOTE_ADD_P["pañcāyatanāni"] = NEW["pañcāyatanāni"]
    F.FIXED_CV = {"cakkhu": F.FIXED["cakkhuviññāṇadhātu"][0].replace(" ဓာတ်", ""),
                  "kāya": F.KAYAVINNANA}
    setup_sk()
    _K_NP = K.np_my2
    K.np_my2 = np_my
    F.np_my = np_my
    _K_UNIT = F.unit_my
    F.unit_my = unit_my


setup()


class Counting(dict):
    cnt = collections.Counter()

    def setdefault(self, k, v):
        self.cnt[k] += 1
        return super().setdefault(k, v)


def regress():
    bad = 0
    for n in ["1-00-paccaya.md", "1-02-vedanattika.md"] + M.NAMES:
        set_dyad(F, None)
        set_dyad(FG, None)
        txt = M.translate(n)
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
    if "--out" in sys.argv:                  # write a review copy elsewhere (inside pi-7-my/)
        OUT = pathlib.Path(sys.argv[sys.argv.index("--out") + 1]).resolve()
        del sys.argv[sys.argv.index("--out"):sys.argv.index("--out") + 2]
    if "--regress" in sys.argv:
        sys.exit(1 if regress() else 0)
    F.DEV = "--dev" in sys.argv
    names = [a for a in sys.argv[1:] if not a.startswith("--")] or NAMES
    if F.DEV:
        F.UNSEEN = Counting()
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
        with open(CHK / "via-g.txt", "w", encoding="utf-8") as fh:
            for k, v in M.VIA_G.most_common():
                fh.write(f"[{v}] {k}\n")
        print(len(rows), "unmatched skeletons,", sum(F.UNSEEN.cnt.values()), "occurrences")
    if F.SLIPS and "--slips" in sys.argv:
        print("slips:", *sorted(F.SLIPS), sep="\n  ")


if __name__ == "__main__":
    main()
