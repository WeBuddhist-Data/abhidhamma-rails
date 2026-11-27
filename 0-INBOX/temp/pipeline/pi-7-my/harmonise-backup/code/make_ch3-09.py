"""Burmese zero-shot of pi-7 3-09 mahantaraduka (the fourteen «mahantara» dyads of the Dukapaṭṭhāna,
«အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ»), from the Pāli only.

usage: python3 -I -X utf8 make_ch3-09.py [--dev] [--regress] [--slips] [--out DIR]
  (no flag)  translate the chapter and write it; stops on the first unmatched sentence (nothing is guessed).
  --dev      do not stop: list every unmatched skeleton with its count in chk-ch3-09/dev.txt (nothing written).
  --regress  regenerate the approved sample (1-00, 1-02), 2-03 … 2-06, 3-01 … 3-02 and 3-03 … 3-06 in memory through
             this script and compare them with the published files (they must be identical).

Engines (read-only, imported, never run as scripts): make_ch3-03-06.py is IMPORTED (it imports make_ch3-01-02.py,
which imports make_ch2-03-06.py: PRIMARY my7_formulas + make_sample + make_ch1-01, FALLBACK per unit make_ch1-03-05)
with its dyad machinery (the chapter cut at its dyad headings, only that dyad active, pseudo a-stem terms,
both-members slot, notes, lexicon). No main block of another script runs; no file of the sample or of another group
is edited. This script adds the fourteen dyads (pi-1 final Mātikā ^1-M2-55 … ^1-M2-68), their names, notes and unique
sentences; every new string is logged in notes-ch3-09.md.

Terms that are not a-stems (cittasahabhū, cittānuparivattī, the two long -sahabhū / -ānuparivattī terms, upādā) are
read as pseudo a-stem words before slotting; where the Pāli ending does not show the case and number (-ū, -uno, -ī,
-ino, -u / -i before another word, the indeclinable upādā) the ending of the next noun is taken. «citta» is a dyad
term only before a dhamma word (or coordinated with «nocitta» before one); otherwise it is the noun «စိတ်» (as
make_ch3-01-02 reads hetu).
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
NAMES = ["3-09-mahantaraduka.md"]
CHK = HERE / "chk-ch3-09"
WCH = r"[\wāīūṃṅñṭḍṇḷ]"
_NB = r"(?!" + WCH + ")"
_PB = r"(?<!" + WCH + ")"


def _load(name, fn):
    spec = importlib.util.spec_from_file_location(name, HERE / fn)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


M4 = _load("ch30306", "make_ch3-03-06.py")         # its setup() runs on import; its main() does not
M3 = M4.M3
M = M3.M
F, FG, G, K, S = M.F, M.FG, M.G, M.K, M.S
C, END, PE, W = F.C, F.END, F.PE, F.W
DUKA = F.DUKA
NEW = collections.OrderedDict()                    # every new string of this script: Pāli -> Burmese


def new(pali, my):
    NEW.setdefault(pali, my)
    return my


# ===================================================================================== the dyads (pi-1 final)
_PL = " သဘောတရားများ"


def _dw(pali, my, bid):
    return W(pali, my + _PL, "1", bid)[:-len(_PL)]


SARAMMANA = _dw("sārammaṇā dhammā", "အာရုံ ရှိသော", "^1-M2-55")
ANARAMMANA = _dw("anārammaṇā dhammā", "အာရုံ မရှိသော", "^1-M2-55")
CITTA_T = _dw("cittā dhammā", "စိတ် ဖြစ်သော", "^1-M2-56")
NOCITTA_T = _dw("no cittā dhammā", "စိတ် မဟုတ်သော", "^1-M2-56")
CETASIKA = _dw("cetasikā dhammā", "စိတ်၏ အဖော် ဖြစ်သော", "^1-M2-57")
ACETASIKA = _dw("acetasikā dhammā", "စိတ်၏ အဖော် မဟုတ်သော", "^1-M2-57")
CSAMP = _dw("cittasampayuttā dhammā", "စိတ်နှင့် ယှဉ်တွဲသော", "^1-M2-58")
CVIPP = _dw("cittavippayuttā dhammā", "စိတ်နှင့် ကင်းကွာသော", "^1-M2-58")
CSAMS = _dw("cittasaṃsaṭṭhā dhammā", "စိတ်နှင့် ရောနှောသော", "^1-M2-59")
CVISAMS = _dw("cittavisaṃsaṭṭhā dhammā", "စိတ်နှင့် မရောနှောသော", "^1-M2-59")
CSAMU = _dw("cittasamuṭṭhānā dhammā", "စိတ်မှ ဖြစ်ပေါ်လာသော", "^1-M2-60")
NOCSAMU = _dw("no cittasamuṭṭhānā dhammā", "စိတ်မှ ဖြစ်ပေါ်လာသည် မဟုတ်သော", "^1-M2-60")
CSAHA = _dw("cittasahabhuno dhammā", "စိတ်နှင့်အတူ တည်ရှိသော", "^1-M2-61")
NOCSAHA = _dw("no cittasahabhuno dhammā", "စိတ်နှင့်အတူ တည်ရှိသည် မဟုတ်သော", "^1-M2-61")
CANU = _dw("cittānuparivattino dhammā", "စိတ်နောက်သို့ လိုက်ပါသော", "^1-M2-62")
NOCANU = _dw("no cittānuparivattino dhammā", "စိတ်နောက်သို့ လိုက်ပါသည် မဟုတ်သော", "^1-M2-62")
CSS = _dw("cittasaṃsaṭṭhasamuṭṭhānā dhammā", "စိတ်နှင့် ရောနှော၍ စိတ်မှ ဖြစ်ပေါ်လာသော", "^1-M2-63")
NOCSS = _dw("no cittasaṃsaṭṭhasamuṭṭhānā dhammā", "စိတ်နှင့် ရောနှော၍ စိတ်မှ ဖြစ်ပေါ်လာသည် မဟုတ်သော", "^1-M2-63")
CSSSAHA = _dw("cittasaṃsaṭṭhasamuṭṭhānasahabhuno dhammā",
              "စိတ်နှင့် ရောနှော၍ စိတ်မှ ဖြစ်ပေါ်လာပြီး စိတ်နှင့်အတူ တည်ရှိသော", "^1-M2-64")
NOCSSSAHA = _dw("no cittasaṃsaṭṭhasamuṭṭhānasahabhuno dhammā",
                "စိတ်နှင့် ရောနှော၍ စိတ်မှ ဖြစ်ပေါ်လာပြီး စိတ်နှင့်အတူ တည်ရှိသည် မဟုတ်သော", "^1-M2-64")
CSSANU = _dw("cittasaṃsaṭṭhasamuṭṭhānānuparivattino dhammā",
             "စိတ်နှင့် ရောနှော၍ စိတ်မှ ဖြစ်ပေါ်လာပြီး စိတ်နောက်သို့ လိုက်ပါသော", "^1-M2-65")
NOCSSANU = _dw("no cittasaṃsaṭṭhasamuṭṭhānānuparivattino dhammā",
               "စိတ်နှင့် ရောနှော၍ စိတ်မှ ဖြစ်ပေါ်လာပြီး စိတ်နောက်သို့ လိုက်ပါသည် မဟုတ်သော", "^1-M2-65")
AJJHATTIKA_T = _dw("ajjhattikā dhammā", "အတွင်းပိုင်း", "^1-M2-66")
BAHIRA_T = _dw("bāhirā dhammā", "ပြင်ပ", "^1-M2-66")
UPADA_T = _dw("upādā dhammā", "မူလဓာတ်ကြီးများကို မှီ၍ ဖြစ်သော", "^1-M2-67")
NOUPADA_T = _dw("no upādā dhammā", "မူလဓာတ်ကြီးများကို မှီ၍ ဖြစ်သည် မဟုတ်သော", "^1-M2-67")
# ^1-M2-68: the Burmese has the spelling variant between the term and «သဘောတရားများ» (as the Pāli)
UPADINNA_T = W("upādiṇṇā dhammā", "ကံကြောင့် ဖြစ်သော", "1", "^1-M2-68")
ANUPADINNA_T = _dw("anupādiṇṇā dhammā", "ကံကြောင့် မဖြစ်သော", "^1-M2-68")

DYADS = {
    "sarammana": {"sārammaṇ": SARAMMANA, "anārammaṇ": ANARAMMANA},
    "citta": {"cittdk": CITTA_T, "nocittdk": NOCITTA_T},
    "cetasika": {"cetasik": CETASIKA, "acetasik": ACETASIKA},
    "cittasamp": {"cittasampayutt": CSAMP, "cittavippayutt": CVIPP},
    "cittasams": {"cittasaṃsaṭṭh": CSAMS, "cittavisaṃsaṭṭh": CVISAMS},
    "cittasamu": {"cittasamuṭṭhān": CSAMU, "nocittasamuṭṭhān": NOCSAMU},
    "cittasaha": {"cittasahabhudk": CSAHA, "nocittasahabhudk": NOCSAHA},
    "cittanu": {"cittānuparivattdk": CANU, "nocittānuparivattdk": NOCANU},
    "css": {"cittasaṃsaṭṭhasamuṭṭhān": CSS, "nocittasaṃsaṭṭhasamuṭṭhān": NOCSS},
    "csssaha": {"cittasaṃsaṭṭhasamuṭṭhānasahabhudk": CSSSAHA, "nocittasaṃsaṭṭhasamuṭṭhānasahabhudk": NOCSSSAHA},
    "cssanu": {"cittasaṃsaṭṭhasamuṭṭhānānuparivattdk": CSSANU,
               "nocittasaṃsaṭṭhasamuṭṭhānānuparivattdk": NOCSSANU},
    "ajjhattika": {"ajjhattik": AJJHATTIKA_T, "bāhir": BAHIRA_T},
    "upada": {"upādādk": UPADA_T, "noupādādk": NOUPADA_T},
    "upadinna": {"upādinn": UPADINNA_T, "anupādinn": ANUPADINNA_T},
}
for _d, _tab in DYADS.items():
    _a, _b = list(_tab)
    _tab[_a + "_" + _b.replace(" ", "_") + "_both"] = f"{_tab[_a]}{C} {_tab[_b]}"

DYAD_OF = {"Sārammaṇadukaṃ": "sarammana", "Cittadukaṃ": "citta", "Cetasikadukaṃ": "cetasika",
           "Cittasampayuttadukaṃ": "cittasamp", "Cittasaṃsaṭṭhadukaṃ": "cittasams",
           "Cittasamuṭṭhānadukaṃ": "cittasamu", "Cittasahabhūdukaṃ": "cittasaha",
           "Cittānuparivattidukaṃ": "cittanu", "Cittasaṃsaṭṭhasamuṭṭhānadukaṃ": "css",
           "Cittasaṃsaṭṭhasamuṭṭhānasahabhūdukaṃ": "csssaha",
           "Cittasaṃsaṭṭhasamuṭṭhānānuparivattidukaṃ": "cssanu", "Ajjhattikadukaṃ": "ajjhattika",
           "Upādādukaṃ": "upada", "Upādinnadukaṃ": "upadinna"}
# the dyad names (NEW; the pattern of make_ch3-01-02's «<the notion of the first term> နှစ်မျိုးတွဲ»)
_CITTA_N = "စိတ်"
DUKA_NAME = {
    "Sārammaṇadukaṃ": f"အာရုံ ရှိခြင်း {DUKA}",
    "Cittadukaṃ": f"{_CITTA_N} ဖြစ်ခြင်း {DUKA}",
    "Cetasikadukaṃ": f"{_CITTA_N}၏ အဖော် ဖြစ်ခြင်း {DUKA}",
    "Cittasampayuttadukaṃ": f"{_CITTA_N}နှင့် ယှဉ်တွဲခြင်း {DUKA}",
    "Cittasaṃsaṭṭhadukaṃ": f"{_CITTA_N}နှင့် ရောနှောခြင်း {DUKA}",
    "Cittasamuṭṭhānadukaṃ": f"{_CITTA_N}မှ ဖြစ်ပေါ်လာခြင်း {DUKA}",
    "Cittasahabhūdukaṃ": f"{_CITTA_N}နှင့်အတူ တည်ရှိခြင်း {DUKA}",
    "Cittānuparivattidukaṃ": f"{_CITTA_N}နောက်သို့ လိုက်ပါခြင်း {DUKA}",
    "Cittasaṃsaṭṭhasamuṭṭhānadukaṃ": f"{_CITTA_N}နှင့် ရောနှော၍ {_CITTA_N}မှ ဖြစ်ပေါ်လာခြင်း {DUKA}",
    "Cittasaṃsaṭṭhasamuṭṭhānasahabhūdukaṃ":
        f"{_CITTA_N}နှင့် ရောနှော၍ {_CITTA_N}မှ ဖြစ်ပေါ်လာပြီး {_CITTA_N}နှင့်အတူ တည်ရှိခြင်း {DUKA}",
    "Cittasaṃsaṭṭhasamuṭṭhānānuparivattidukaṃ":
        f"{_CITTA_N}နှင့် ရောနှော၍ {_CITTA_N}မှ ဖြစ်ပေါ်လာပြီး {_CITTA_N}နောက်သို့ လိုက်ပါခြင်း {DUKA}",
    "Ajjhattikadukaṃ": f"အတွင်းပိုင်း ဖြစ်ခြင်း {DUKA}",
    "Upādādukaṃ": f"မူလဓာတ်ကြီးများကို မှီ၍ ဖြစ်ခြင်း {DUKA}",
    "Upādinnadukaṃ": f"ကံကြောင့် ဖြစ်ခြင်း {DUKA}",
}
for _k, _v in DUKA_NAME.items():
    new(_k, _v)
MAHANTARA = W("Mahantaradukaṃ", "ကြားညှပ် နှစ်မျိုးတွဲ အစုကြီး", "1", "^1-M-2-10-0")

M3.DYADS.update(DYADS)
M3.DYAD_OF.update(DYAD_OF)
M3.DUKA_NAME.update(DUKA_NAME)


# ===================================================================================== Pāli preparation (in memory)
# a-stem ending of the next noun («Cittasahabhū dhammo» -> «…o», «upādā dhammassa» -> «…assa»): the noun's stem
# is cut off first («cittasamuṭṭhānaṃ» -> «aṃ», not «ānaṃ»)
_NOUN_STEMS = ("cittasamuṭṭhān", "kaṭattārūp", "upādārūp", "mahābhūt", "dhamm", "khandh", "cetan", "kāy", "rūp",
               "āhār", "indriy", "het", "kabaḷīkār")
_NEXT_MAP = {"ānañca": "ānañca", "ānaṃ": "ānaṃ", "añca": "aṃ", "assa": "assa", "āni": "ā", "aṃ": "aṃ", "o": "o",
             "ā": "ā", "e": "e", "ena": "ena", "u": "o", "ū": "ā", "ūnaṃ": "ānaṃ", "uṃ": "aṃ", "ussa": "assa",
             "āya": "assa", "ānañca ": "ānañca"}
_U_FIX = {"ūnañca": "ānañca", "ūnaṃ": "ānaṃ", "uñca": "añca", "ussa": "assa", "uṃ": "aṃ"}
_I_FIX = {"īnañca": "ānañca", "īnaṃ": "ānaṃ", "iñca": "añca", "issa": "assa", "iṃ": "aṃ"}


def _next_end(rest, own):
    """the a-stem ending for a term whose own ending is ambiguous: that of the next noun after «ca» / other terms"""
    for w in rest.split()[:6]:
        w = w.strip(",.;()")
        if w in ("ca",) or not w:
            continue
        if any(s in w for s in ("sahabh", "nuparivatt", "upādādk")) or re.fullmatch(r"[Nn]?o?upādā", w):
            continue
        if w.startswith("…"):
            break
        if w in F.NP_NUM:
            continue
        st = next((x for x in _NOUN_STEMS if w.startswith(x)), None)
        if st is None:
            break
        e = w[len(st):]
        if e in _NEXT_MAP:
            return _NEXT_MAP[e]
        break
    return {"ū": "o", "u": "o", "ī": "o", "i": "o", "uno": "assa", "ino": "assa", "ā": "ā"}[own]


def _pseudo(t, stem_re, key, fix, amb):
    """stem_re + its own endings -> key + a-stem ending (fix: the clear endings; amb: those read from the next noun);
    an ambiguous ending with its own enclitic «ca» whose noun is -aṃ / -ānaṃ takes the «-ñca» form («upādā ca
    noupādā ca cittasamuṭṭhānaṃ rūpaṃ» = «upādañca noupādañca …», as make_ch3-01-02's both-members slot reads)"""
    alts = "|".join(sorted(list(fix) + list(amb), key=len, reverse=True))

    def rep(m):
        e, ca = m[2], m[3] or ""
        lead = key[0].upper() + key[1:] if m[1][0].isupper() else key
        if e in fix:
            return lead + fix[e] + ca
        a = _next_end(t[m.end():], e)
        if ca and a in ("aṃ", "ānaṃ"):
            return lead + a[:-1] + "ñca"
        return lead + a + ca
    return re.sub(_PB + "(" + stem_re + ")(" + alts + ")" + _NB + "((?: ca)(?!" + WCH + "))?", rep, t)


def _ci(stem):
    return f"[{stem[0].upper()}{stem[0]}]" + re.escape(stem[1:])


_A = r"(o|aṃ|añca|assa|ā|ānaṃ|ānañca|e|ena)"
_PREP_PREV = M3.prep_dyad


def prep_dyad(t, d):
    if d not in DYADS:
        return _PREP_PREV(t, d)
    if d == "citta":
        t = re.sub(_PB + "([Cc])itt" + _A + r"(?= (?:ca )?(?:[Nn]ocitt\w*(?: ca)? )?(?:dhamm|…))",
                   lambda m: m[1] + "ittdk" + m[2], t)
        t = re.sub(_PB + "([Nn])ocitt" + _A + _NB, lambda m: m[1] + "ocittdk" + m[2], t)
        t = re.sub(_PB + "([Nn])ocittādhipati" + _NB, lambda m: m[1] + "ocittdkādhipati", t)
    elif d in ("cittasaha", "csssaha"):
        st = "cittasahabhu" if d == "cittasaha" else "cittasaṃsaṭṭhasamuṭṭhānasahabhu"
        for neg in ("no", ""):
            s = neg + st
            t = _pseudo(t, _ci(s[:-1]), s + "dk", {k: v for k, v in _U_FIX.items()},
                        ("ū", "uno", "u"))
    elif d in ("cittanu", "cssanu"):
        st = "cittānuparivatt" if d == "cittanu" else "cittasaṃsaṭṭhasamuṭṭhānānuparivatt"
        for neg in ("no", ""):
            s = neg + st
            t = _pseudo(t, _ci(s), s + "dk", dict(_I_FIX), ("ī", "ino", "i"))
    elif d == "upada":
        t = re.sub(_PB + "([Nn]oupād|[Uu]pād)(ādhipati|ācittasamaṅgissa)" + _NB,
                   lambda m: m[1] + "ādk" + ("ādhipati" if m[2] == "ādhipati" else "acittasamaṅgissa"), t)
        t = _pseudo(t, "[Nn]oupād", "noupādādk", {}, ("ā",))
        t = _pseudo(t, "[Uu]pād", "upādādk", {}, ("ā",))
    elif d == "cittasamp":
        # «cittasampayuttaka» (khandhā …) = the term cittasampayutta on that noun (as 3-03-06's X-sampayuttaka)
        t = re.sub(_PB + "([Cc]ittasampayutt)ak" + _A + _NB, lambda m: m[1] + m[2], t)
    if d == "citta":
        t = re.sub(_PB + "([Nn])ocittdk?asamaṅgissa" + _NB, lambda m: m[1] + "ocittdkasamaṅgissa", t)
        t = re.sub(_PB + "([Nn])ocittasamaṅgissa" + _NB, lambda m: m[1] + "ocittdkasamaṅgissa", t)
    # «T-o kabaḷīkāro āhāro» (a term before the fixed noun): read as one noun «kabaḷīkārāhāro» (same Burmese)
    keys = "|".join(_ci(k) for k in sorted(DYADS[d], key=len, reverse=True) if not k.endswith("_both"))
    t = re.sub("(" + _PB + "(?:" + keys + r")\w*(?: ca)?) kabaḷīkār(o|aṃ|assa) āhār(?:o|aṃ|assa)" + _NB,
               lambda m: f"{m[1]} kabaḷīkārāhār{m[2]}", t)
    # one «ca» after the last member: «T-ā khandhā kabaḷīkāro āhāro ca» = «… khandhā ca kabaḷīkāro āhāro ca»;
    # «X-ānaṃ khandhānaṃ cittassa ca» = «… khandhānaṃ ca cittassa ca» (as make_ch3-01-02's _CA_AFTER)
    t = re.sub(r"(?<= khandhā) (?=kabaḷīkāro āhāro ca" + _NB + ")", " ca ", t)
    t = re.sub(r"(?<= khandhānaṃ) (?=cittassa ca" + _NB + ")", " ca ", t)
    # «cittaṃ sampayuttakā ca khandhā» / «cittaṃ sampayuttakā khandhā ca» = «cittañca sampayuttakā khandhā ca»
    t = re.sub(_PB + r"cittaṃ sampayuttakā (?:ca khandhā|khandhā ca)" + _NB, "cittañca sampayuttakā khandhā ca", t)
    return _PREP_PREV(t, d)


M3.prep_dyad = prep_dyad


# ===================================================================================== names and headings
def setup_names():
    hl = {"Mahantaradukaṃ": MAHANTARA, "Mahantaradukaṃ niṭṭhitaṃ.": F.finished(MAHANTARA),
          "*Pacchājātāsevanapaccayā*": F.heading("*Pacchājāta-āsevanapaccayā*")}
    hl.update(DUKA_NAME)
    for k, v in DUKA_NAME.items():
        hl[f"{k} niṭṭhitaṃ."] = F.finished(v)
    F.HLINES.update(hl)
    for k, v in DUKA_NAME.items():              # a dyad named inside a note («yathā cittasahabhūdukaṃ»)
        K.WORDS_N.setdefault(k[0].lower() + k[1:], v)


# ===================================================================================== notes
NOTE_ADD = {}


def _notes():
    return {}


def _notep():
    """whole notes (raw Pāli, brackets included) -> Burmese; put in place before the slotter (as make_ch3-01-02)"""
    cn, cd, N, CNT = F.cname, F.cond, F.N, F.COUNT
    E, CC, KAT, VITTH, GAN, VIB = END, C, M3.KAT, M3.VITTH, M3.GAN, M3.VIBHAJ
    EV, SAB, PANHA, NATTHI, NINN, NINK = M3.EVAM_T, M3.SAB, M3.PANHA, M3.NATTHI, M3.NINNANA, M3.NINNANAKARANA
    ITARE, GANANA, PV, VARA, LAK, KAYYA, EVAM = M3.ITARE, S.GANANA, M3.PATICCA_V, M3.VARA, F.LAKAUNG, K.KAYYA, K.EVAM
    SAMKH, MULA, PUCCH, SADISA, SADISANI = F.NOTES["(saṃkhittaṃ)"][1:-1], M3.MULA, M3.PUCCH, F.SADISA, K.SADISANI
    PS, APS, PAT, NIYAM, MAHAB = (F.PREFIX["paṭisandhikkhaṇe"], F.PREFIX["ahetukapaṭisandhikkhaṇe"], F.PATISANDHI,
                                  M3.NIYAM, M3.MAHAB)
    am, sm = F.LEX["ārammaṇādhipati"][0], F.LEX["sahajātādhipati"][0]
    MOHO, PV5, VUTTH = F.LEX["moho"][0], F.LEX["pañcaviññāṇaṃ"][0], F.LEX["vuṭṭhānassa"][0]
    GAMANA, PG = M.GAMANA, f"{M3.PATHAMA_GAMANA}{F.SADISA}"                 # paṭhamagamanasadisaṃ
    DN = DUKA_NAME
    DSAMU, DSAHA, DCSS = DN["Cittasamuṭṭhānadukaṃ"], DN["Cittasahabhūdukaṃ"], DN["Cittasaṃsaṭṭhasamuṭṭhānadukaṃ"]
    AHET = F.AHETUKA[:-len("သော")] + "သည်"                               # «ahetuka»nti (as 3-01-02 «…မရှိသည်ဟု»)
    KINDS = {k: K.kind_word(k) for k in ("sahajātaṃ", "purejātaṃ", "pacchājātaṃ")}
    NIKKH = new("yathā nikkhittapadāni", "ချထားသော ပုဒ်များအတိုင်း")
    PURET = new("pūretukāmena", "ပြည့်စုံစေလိုသူသည်")
    PURETVA = new("pūretvā / pūritvā", "ပြည့်စုံစေ၍")
    PURIMA_G = new("purimagamanaṃ", f"ရှေး {GAMANA}")                   # (purimā purimā «ရှေးရှေး»)
    TIYM = new("tīṇiyeva moho", f"{MOHO}နှင့် {CNT['tīṇi']}သာ")          # (Marathi meaning: «with moha only three»)
    TISUYM = new("tīsuyeva moho", f"{CNT['tīṇi']}၌သာ {MOHO}")
    ASAMM = S.PH["asammuyhantena"]                                     # «မရောထွေးစေဘဲ» (sample; 2-01-02 asammohantena)
    MULAPADE = new("mūlapade", f"{MULA} {F.PADA}၌")
    PAVES = new("pavesetvā", "ထည့်သွင်း၍")
    ANTE = new("ante", "အဆုံး၌")
    LABBHATI = new("labbhati", "တွေ့ရသည်")
    SABBATTH_N = new("sabbaṭṭhāne", f"နေရာ {SAB}၌")
    GHATANAYA = new("paṭhamaghaṭanānayena", f"ပထမ {F.GHATANA}၏ " + M4.NEW["nayena"])
    PAVATTI = M3.PAVATTE[:-len("၌")]                                    # pavatti «ဘဝ ဖြစ်စဉ်»
    EKAMULA = new("ekamūlānaṃ", f"{CNT['ekaṃ']}ကို အခြေခံသည်တို့၏")
    UDDHAR = M4.NEW["uddharitabbā"]
    IMINAKARENA = M3.NEW["iminākārena"]

    def mula(term):
        return f"{term} {F.DHAMMA}{F.MULAKA}၌"
    gsamp = f"{ITARE} {GANANA} {CNT['dve']}ကိုလည်း{CC} {VARA('sampayutta')}ကိုလည်း"
    gniss = f"{ITARE} {GANANA} {CNT['dve']}ကိုလည်း{CC} {VARA('nissaya')}ကိုလည်း"
    return {
        # Sārammaṇa
        "(Evaṃ itare dve gaṇanāpi sampayuttavārāpi kātabbā.)": f"({EV} {gsamp} {KAT}{E})",
        # Citta
        "(Evaṃ itare dve gaṇanāpi sampayuttavāropi sabbe kātabbā.)": f"({EV} {gsamp} {SAB} {KAT}{E})",
        "(paṭhamagamanasadisaṃ ninnānākaraṇaṃ, imaṃ nānaṃ)": f"({PG} {NINK}{CC} {M3.NOTE_ADD['imaṃ nānaṃ']})",
        "(dvepi gamanā paṭhamagamanasadisaṃ ninnānākaraṇaṃ. Ārammaṇādhipati sahajātādhipati kātabbā)":
            f"({GAMANA} {CNT['dve']}လုံးသည် {PG} {NINK}{E} {am}{CC} {sm}ကို {KAT})",
        "(tīṇipi garukārammaṇā kātabbā, ārammaṇādhipatiyeva)":
            f"({CNT['tīṇi']}လုံးကို {M4.GARUK}အဖြစ် {KAT}{CC} {am}သာ)",
        "(ime dve pūretukāmena kātabbā, purimagamanasadisaṃ)":
            f"(ဤ {CNT['dve']}ကို {PURET} {KAT}{CC} {PURIMA_G}{SADISA})",
        "(ime dvepi pūretukāmena sabbattha kātabbā, paṭhamagamanasadisaṃ ninnānākaraṇaṃ)":
            f"(ဤ {CNT['dve']}လုံးကို {PURET} {K.SABBATTHA} {KAT}{CC} {PG} {NINK})",
        "(paṭisandhikkhaṇepi dve)": f"({PS}လည်း {CNT['dve']})",
        # Cetasika
        "(paṭisandhikkhaṇe dvepi kātabbā, saṃkhittaṃ)": f"({PS} {CNT['dve']}လုံးကို {KAT}{CC} {SAMKH})",
        "(paṭisandhikkhaṇe dvepi kātabbā)": f"({PS} {CNT['dve']}လုံးကို {KAT})",
        "(paṭisandhikkhaṇe tīṇipi kātabbā)": f"({PS} {CNT['tīṇi']}လုံးကို {KAT})",
        "(paṭisandhikkhaṇe ekaṃ)": f"({PS} {CNT['ekaṃ']})",
        "(paṭisandhikkhaṇe dve)": f"({PS} {CNT['dve']})",
        "(paṭisandhikkhaṇe ekaṃ, saṃkhittaṃ)": f"({PS} {CNT['ekaṃ']}{CC} {SAMKH})",
        "(Nava pañhā pañcaviññāṇampi yathā ārammaṇapaccayā evaṃ kātabbaṃ, tīsuyeva moho. Sabbe pañhā "
        "pavattipaṭisandhiyā kātabbā asammohantena.)":
            (f"({PANHA} {CNT['nava']}{CC} {PV5}ကိုလည်း {cn('ārammaṇa')}{KAYYA} {EVAM} {KAT}{CC} {TISUYM}{E} "
             f"{PANHA} {SAB}ကို {M3.PAV_PS} {ASAMM} {KAT}{E})"),
        "(evaṃ pañcapi pañhā kātabbā, tīṇiyeva moho. Saṃkhittaṃ)":
            f"({EV} {PANHA} {CNT['pañca']}လုံးကို {KAT}{CC} {TIYM}{E} {SAMKH})",
        "(Evaṃ itare dve gaṇanāpi sampayuttavāropi kātabbo.)": f"({EV} {gsamp} {KAT}{E})",
        "(paṭhamagamanasadisaṃ)": f"({PG})",
        "(paṭhamagamanaṃ)": f"({M3.PATHAMA_GAMANA})",
        "(ārammaṇādhipatiyeva)": f"({am}သာ)",
        "(evaṃ tīṇi kātabbāni, paṭhamagamanasadisaṃ. Pūritvā kātabbaṃ, ninnānākaraṇaṃ)":
            f"({EV} {CNT['tīṇi']}ကို {KAT}{CC} {PG}{E} {PURETVA} {KAT}{CC} {NINK})",
        "(Mūlaṃ pucchitabbaṃ, tīṇi upanissayā)": f"({MULA}ကို {PUCCH}{CC} {N['upanissaya']} {CNT['tīṇi']})",
        "(tīṇi, paṭhamagamanasadisaṃ ninnānākaraṇaṃ)": f"({CNT['tīṇi']}{CC} {PG} {NINK})",
        "(purejātasadisaṃ ninnānākaraṇaṃ)": f"({cn('purejāta')}{SADISA} {NINK})",
        "(purejātasadisaṃ ninnānaṃ)": f"({cn('purejāta')}{SADISA} {NINN})",
        "(paṭisandhikkhaṇe)": f"({PS})",
        "(paṭisandhiyā dve kātabbā)": f"({PAT}၌ {CNT['dve']}ကို {KAT})",
        # Cittasampayutta
        "(Evaṃ navapi pañhā kātabbā. Ahetukanti sabbattha niyāmetabbaṃ, ekaṃyeva mohaṃ mūlapade.)":
            (f"({EV} {PANHA} {CNT['nava']}လုံးကို {KAT}{E} {AHET}ဟု {K.SABBATTHA} {NIYAM}{CC} {MULAPADE} "
             f"{MOHO} {CNT['ekaṃ']}တည်းကိုသာ{E})"),
        "(Evaṃ dve pañhā pavattipaṭisandhi kātabbā. Saṃkhittaṃ.)":
            f"({EV} {PANHA} {CNT['dve']}ကို {M3.PAV_PS} {KAT}{E} {SAMKH}{E})",
        "(paṭiccasadisā, pañhāghaṭanā natthi)": f"({PV}{SADISANI}{CC} {PANHA} {F.GHATANA} {NATTHI})",
        "(paccayavārasadisā, pañhāghaṭanā natthi)": f"({VARA('paccaya')}{SADISANI}{CC} {PANHA} {F.GHATANA} {NATTHI})",
        # Cittasaṃsaṭṭha
        "(Cittasaṃsaṭṭhadukaṃ yathā cittasampayuttadukaṃ evaṃ kātabbaṃ, ninnānākaraṇaṃ.)":
            f"({DN['Cittasaṃsaṭṭhadukaṃ']}ကို {DN['Cittasampayuttadukaṃ']}{KAYYA} {EVAM} {KAT}{CC} {NINK}{E})",
        # Cittasamuṭṭhāna
        "(yāva asaññasattā kātabbā)": f"({M3.YAVA_AS} {KAT})",
        "(paṭisandhikkhaṇe dvepi paṭiccavārasadisā)": f"({PS} {CNT['dve']}လုံးသည် {PV}{SADISANI})",
        "(paṭisandhikkhaṇe tīṇipi kātabbā paṭiccavārasadisā)": f"({PS} {CNT['tīṇi']}လုံးကို {PV}နှင့် တူအောင် {KAT})",
        "(paṭisandhikkhaṇe dvepi kātabbā paṭiccavārasadisā)": f"({PS} {CNT['dve']}လုံးကို {PV}နှင့် တူအောင် {KAT})",
        "(paṭisandhikkhaṇe dvepi)": f"({PS} {CNT['dve']}လုံး)",
        "(Sabbe navapi pañhā kātabbā, paṭiccavārasadisā. Pañcaviññāṇampi kātabbaṃ. Tīṇiyeva moho.)":
            f"({PANHA} {CNT['nava']}လုံး {SAB}ကို {KAT}{CC} {PV}{SADISANI}{E} {PV5}ကိုလည်း {KAT}{E} {TIYM}{E})",
        "(Evaṃ itare dve gaṇanāpi nissayavāropi kātabbo.)": f"({EV} {gniss} {KAT}{E})",
        "(pañca pañhā kātabbā. Tīṇi. Moho)": f"({PANHA} {CNT['pañca']}ကို {KAT}{E} {CNT['tīṇi']}{E} {MOHO})",
        "(tīṇipi ārammaṇādhipati, sahajātādhipatipi kātabbā)":
            f"({CNT['tīṇi']}လုံး၌ {am}{CC} {sm}ကိုလည်း {KAT})",
        "(vuṭṭhānaṃ natthi)": f"({VUTTH} {NATTHI})",
        "(itare dve gaṇanā, imassa sadisāyeva kātabbā)":
            f"({ITARE} {GANANA} {CNT['dve']}{CC} ဤသည်နှင့် တူအောင်ပင် {KAT})",
        "(tīṇi kātabbā, vuṭṭhānaṃ natthi)": f"({CNT['tīṇi']}ကို {KAT}{CC} {VUTTH} {NATTHI})",
        "(iminākāreneva pacchājāto vitthāretabbo)": f"({IMINAKARENA}ပင် {cn('pacchājāta')}ကို {VITTH})",
        "(paccayavārasadisaṃ paṭisandhipi pavattipi kātabbā sabbesampi pañhānaṃ.)":
            f"({VARA('paccaya')}{SADISA} {PANHA} {SAB}၏ {PAT}ကိုလည်း{CC} {PAVATTI}ကိုလည်း {KAT}{E})",
        "(anulomagaṇanā kātabbā)": f"({K.ORDER_N['anulomagaṇanā']}ကို {KAT})",
        # Cittasahabhū
        "(arūpaṃ sabbaṃ uddharitabbaṃ. Cittasamuṭṭhānadukasadisaṃ.)":
            f"({M3.ARUPA_N}ကို {SAB} {UDDHAR}{E} {DSAMU}{SADISA}{E})",
        "(mahābhūtā chasupi pañhesu kātabbā, adhipatiyā tīsu natthi.)":
            f"({MAHAB}တို့ကို {PANHA} {CNT['cha']}လုံး၌ {KAT}{CC} {cd('adhipati', 'loc')} {CNT['tīṇi']}၌ {NATTHI}{E})",
        "(Evaṃ navapi pañhā kātabbā. \"Ahetuka\"nti niyāmetabbaṃ. Yathā anulome labbhati evaṃ kātabbaṃ. Tīṇi moho "
        "yathā cittasamuṭṭhānaduke evameva kātabbā.)":
            (f"({EV} {PANHA} {CNT['nava']}လုံးကို {KAT}{E} “{AHET}”ဟု {NIYAM}{E} {K.ORDER_L['anulome']} "
             f"{M3.LABBH} {KAT}{E} {CNT['tīṇi']} {MOHO}ကို {DSAMU}၌{KAYYA} {EVAM}ပင် {KAT}{E})"),
        "(evaṃ itare dvepi gaṇanā kātabbā)": f"({EV} {ITARE} {GANANA} {CNT['dve']}လုံးကို {KAT})",
        "(paṭiccavārasadisaṃ, sabbe mahābhūtā)": f"({PV}{SADISA}{CC} {MAHAB} {SAB})",
        "(sabbe mahābhūtā paṭiccasadisaṃ)": f"({MAHAB} {SAB} {PV}{SADISA})",
        "(paṭiccasadisaṃ, sabbe mahābhūtā)": f"({PV}{SADISA}{CC} {MAHAB} {SAB})",
        "(Imaṃ cittasamuṭṭhānadukaṃ paccayavāre ārammaṇasadisaṃ. Channampi imesaṃ pañcaviññāṇamūlā kātabbā. "
        "Saṃkhittaṃ.)":
            (f"(ဤ {DSAMU}သည် {VARA('paccaya')}၌ {cn('ārammaṇa')}{SADISA}{E} ဤ {CNT['cha']}လုံး၏ "
             f"{PV5}{F.MULAKA}တို့ကို {KAT}{E} {SAMKH}{E})"),
        "(Saṃkhittaṃ. Sabbaṃ kātabbaṃ. Paccayavārassa pañcaviññāṇaṃ channampi mūlā kātabbā. Sabbe mahābhūte "
        "tīṇiyeva moho. Saṃkhittaṃ.)":
            (f"({SAMKH}{E} {SAB}ကို {KAT}{E} {VARA('paccaya')}၏ {PV5}{CC} {CNT['cha']}လုံး၏ {MULA}တို့ကို {KAT}{E} "
             f"{MAHAB} {SAB}ကို {TIYM}{E} {SAMKH}{E})"),
        "(tīṇi, moho)": f"({CNT['tīṇi']}{CC} {MOHO})",
        "(Itare dve gaṇanāpi sampayuttavāropi sabbaṃ kātabbaṃ.)": f"({gsamp} {SAB} {KAT}{E})",
        "(cittasamuṭṭhānadukasadisaṃ, ninnānākaraṇaṃ)": f"({DSAMU}{SADISA}{CC} {NINK})",
        "(ārammaṇādhipatipi sahajātādhipatipi kātabbā)": f"({am}ကိုလည်း{CC} {sm}ကိုလည်း {KAT})",
        "(ārammaṇādhipatipi sahajātādhipatipi imesampi tiṇṇaṃ kātabbā. Navapi pañhā cittasamuṭṭhānadukasadisā. Ante "
        "tīṇi ārammaṇādhipatiyeva)":
            (f"({am}ကိုလည်း{CC} {sm}ကိုလည်း ဤ {CNT['tīṇi']}လုံး၌ {KAT}{E} {PANHA} {CNT['nava']}လုံးသည် "
             f"{DSAMU}{SADISANI}{E} {ANTE} {CNT['tīṇi']}သည် {am}သာ)"),
        "(cittasamuṭṭhānadukasadisā)": f"({DSAMU}{SADISANI})",
        "(nocittasahabhū mūlaṃyeva labbhati, cittasamuṭṭhānadukasadisā. Tīṇipi ninnānākaraṇaṃ)":
            (f"({NOCSAHA} {F.DHAMMA}{F.MULAKA}သာ {LABBHATI}{CC} {DSAMU}{SADISANI}{E} {CNT['tīṇi']}လုံး "
             f"{NINK})"),
        "(cittasamuṭṭhānadukasadisaṃ)": f"({DSAMU}{SADISA})",
        "(cittasamuṭṭhānadukasadisā. Imampi ekaṃ kabaḷīkāraāhārasadisaṃ)":
            f"({DSAMU}{SADISANI}{E} ဤ {CNT['ekaṃ']}သည်လည်း {KABALI}{SADISA})",
        "(sabbaṃ paṭisandhiyaṃ kātabbaṃ, sahajātaṃ purejātampi)":
            f"({SAB}ကို {PAT}၌ {KAT}{CC} {KINDS['sahajātaṃ']}{CC} {KINDS['purejātaṃ']}လည်း)",
        # Cittānuparivatti
        "(yathā cittasahabhūdukaṃ evaṃ imaṃ dukaṃ kātabbaṃ, ninnānākaraṇaṃ)":
            f"({DSAHA}{KAYYA} {EVAM} ဤ {DUKA}ကို {KAT}{CC} {NINK})",
        # Cittasaṃsaṭṭhasamuṭṭhāna
        "(ahetukapaṭisandhikkhaṇe dvepi kātabbā)": f"({APS} {CNT['dve']}လုံးကို {KAT})",
        "(paṭisandhikkhaṇe dve, saṃkhittaṃ)": f"({PS} {CNT['dve']}{CC} {SAMKH})",
        "(paṭisandhikkhaṇe ekaṃ kātabbaṃ)": f"({PS} {CNT['ekaṃ']}ကို {KAT})",
        "(paṭisandhikkhaṇe dve kātabbā)": f"({PS} {CNT['dve']}ကို {KAT})",
        "(paṭisandhikkhaṇe ekaṃ kātabbaṃ, saṃkhittaṃ)": f"({PS} {CNT['ekaṃ']}ကို {KAT}{CC} {SAMKH})",
        "(evaṃ nava pañhā kātabbā. Paccayavāre pañcaviññāṇampi kātabbaṃ, tīṇiyeva moho)":
            f"({EV} {PANHA} {CNT['nava']}ကို {KAT}{E} {VARA('paccaya')}၌ {PV5}ကိုလည်း {KAT}{CC} {TIYM})",
        "(saṃkhittaṃ. Tīṇiyeva moho)": f"({SAMKH}{E} {TIYM})",
        "(Saṃkhittaṃ. Yathā cittasahabhūduke ārammaṇaṃ evaṃ kātabbaṃ, ninnānākaraṇaṃ. Navapi pañhā.)":
            (f"({SAMKH}{E} {DSAHA}၌ {cn('ārammaṇa')}{KAYYA} {EVAM} {KAT}{CC} {NINK}{E} {PANHA} "
             f"{CNT['nava']}လုံး{E})"),
        "(dvepi adhipatī kātabbā)": f"({N['adhipati']} {CNT['dve']}လုံးကို {KAT})",
        "(dvepi adhipati kātabbā)": f"({N['adhipati']} {CNT['dve']}လုံးကို {KAT})",
        "(Ekāyeva adhipati kātabbā, navapi pañhā. Yathā cittasahabhūdukaṃ, evaṃ kātabbaṃ, ninnānākaraṇaṃ)":
            (f"({N['adhipati']} {CNT['ekaṃ']}တည်းကိုသာ {KAT}{CC} {PANHA} {CNT['nava']}လုံး{E} {DSAHA}{KAYYA}{CC} "
             f"{EVAM} {KAT}{CC} {NINK})"),
        "(navapi pañhā cittasahabhūdukasadisā)": f"({PANHA} {CNT['nava']}လုံးသည် {DSAHA}{SADISANI})",
        "(navapi pañhā cittasahabhūdukasadisā, ninnānākaraṇaṃ)":
            f"({PANHA} {CNT['nava']}လုံးသည် {DSAHA}{SADISANI}{CC} {NINK})",
        "(cittasahabhūdukasadisā, ninnānākaraṇaṃ)": f"({DSAHA}{SADISANI}{CC} {NINK})",
        "(cittasahabhūdukasadisā, ninnānākaraṇaṃ. Tīṇipi pacchājātā. Dve. Ekamūlānaṃ ekā ghaṭanā)":
            (f"({DSAHA}{SADISANI}{CC} {NINK}{E} {CNT['tīṇi']}လုံး {N['pacchājāta']}{E} {CNT['dve']}{E} "
             f"{EKAMULA} {F.GHATANA} {CNT['ekaṃ']})"),
        "(cittasahabhūdukasadisā ninnānākaraṇā. Tīṇipi sahajātā, nānākkhaṇikā)":
            (f"({DSAHA}{SADISANI} {NINK}{E} {CNT['tīṇi']}လုံး {F.LEX['sahajātā'][0]}{CC} "
             f"{F.LEX['nānākkhaṇikā'][0]})"),
        "(cittasahabhūgamanasadisā, ekaṃyeva kabaḷīkāraṃ āhāraṃ)":
            f"({DSAHA}၏ {GAMANA}{SADISANI}{CC} {KABALI} {CNT['ekaṃ']}တည်းကိုသာ)",
        "(purejātasadisaṃ purejātaṃ kātabbaṃ. Sabbaṃ saṃkhittaṃ. Vitthāretabbaṃ)":
            f"({KINDS['purejātaṃ']}ကို {cn('purejāta')}နှင့် တူအောင် {KAT}{E} {SAB} {SAMKH}{E} {VITTH})",
        "(purejātasadisaṃ, ninnānākaraṇaṃ)": f"({cn('purejāta')}{SADISA}{CC} {NINK})",
        "(paṭisandhikkhaṇe tīṇi kātabbā)": f"({PS} {CNT['tīṇi']}ကို {KAT})",
        # the long -sahabhū / -ānuparivattī dyads
        "(yathā cittasaṃsaṭṭhasamuṭṭhānadukaṃ, evaṃ imampi dukaṃ, ninnānākaraṇaṃ)":
            f"({DCSS}{KAYYA}{CC} {EVAM} ဤ {DUKA}ကိုလည်း{CC} {NINK})",
        "(yathā cittasaṃsaṭṭhasamuṭṭhānadukasadisaṃ, ninnānākaraṇaṃ)": f"({DCSS}နှင့် တူသည့်အတိုင်း{CC} {NINK})",
        # Ajjhattika
        "(paṭisandhikkhaṇe dvepi kātabbā, yāva ajjhattikā mahābhūtā)":
            f"({PS} {CNT['dve']}လုံးကို {KAT}{CC} {AJJHATTIKA_T} {MAHAB}တို့အထိ)",
        "(Saṃkhittaṃ. Evaṃ navapi pañhā kātabbā. Pañcaviññāṇampi pavesetvā tīṇiyeva moho.)":
            f"({SAMKH}{E} {EV} {PANHA} {CNT['nava']}လုံးကို {KAT}{E} {PV5}ကိုလည်း {PAVES} {TIYM}{E})",
        "(anulomaṃ)": f"({K.ORDER_N['anulomaṃ']})",
        "(evaṃ pañca kātabbā, tīṇiyeva moho)": f"({EV} {CNT['pañca']}ကို {KAT}{CC} {TIYM})",
        "(paccanīyaṃ)": f"({K.ORDER_N['paccanīyaṃ']})",
        "(dve adhipatī tiṇṇampi kātabbā)": f"({N['adhipati']} {CNT['dve']}ကို {CNT['tīṇi']}လုံး၌ {KAT})",
        "(tiṇṇampi ekāyeva adhipati)": f"({CNT['tīṇi']}လုံး၌ {N['adhipati']} {CNT['ekaṃ']}တည်းသာ)",
        "(tiṇṇampi ekasadisā)": f"({CNT['tīṇi']}လုံး {M3.EKASADISA})",
        "(tīṇipi pūretvā kātabbā, cittassāti kātabbā, sampayuttakānañcāti kātabbā)":
            (f"({CNT['tīṇi']}လုံးကို {PURETVA} {KAT}{CC} {CITTA_N}အားဟု {KAT}{CC} "
             f"{F.QUAL['sampayuttakā']}တို့အား{LAK}ဟု {KAT})"),
        "(evaṃ navapi pañhā kātabbā)": f"({EV} {PANHA} {CNT['nava']}လုံးကို {KAT})",
        "(Idha atthi sabbaṭṭhāne sahajātaṃ paccayavārasadisaṃ. Purejātaṃ purejātasadisaṃ. Pacchājātaṃ "
        "pacchājātasadisaṃ kātabbaṃ, ninnānākaraṇaṃ)":
            (f"({M3.IHA} {cn('atthi')}၏ {SABBATTH_N} {KINDS['sahajātaṃ']}သည် {VARA('paccaya')}{SADISA}{E} "
             f"{KINDS['purejātaṃ']}သည် {cn('purejāta')}{SADISA}{E} {KINDS['pacchājātaṃ']}ကို "
             f"{cn('pacchājāta')}နှင့် တူအောင် {KAT}{CC} {NINK})"),
        "(sahajātapaccayavārasadisaṃ ninnānākaraṇaṃ, paṭhamagamanasadisaṃyeva. Sabbe padā paṭhamaghaṭanānayena "
        "vibhajitabbā)":
            (f"({VARA('sahajāta')}နှင့် {VARA('paccaya')}တို့နှင့် တူသည် {NINK}{CC} {M3.PATHAMA_GAMANA}{SADISA}ပင်{E} "
             f"{F.PADA} {SAB}ကို {GHATANAYA} {VIB})"),
        "(saṃkhittaṃ. Sabbe padā vibhajitabbā paṭhamaghaṭanānayena)":
            f"({SAMKH}{E} {F.PADA} {SAB}ကို {GHATANAYA} {VIB})",
        # Upādā
        "(yāva asaññasattā, evaṃ tīṇi noupādāmūlake)": f"({M3.YAVA_AS}{CC} {EV} {mula(NOUPADA_T)} {CNT['tīṇi']})",
        "(noupādāmūlake tīṇipi paṭiccasadisā, ninnānākaraṇā)":
            f"({mula(NOUPADA_T)} {CNT['tīṇi']}လုံးသည် {PV}{SADISANI}{CC} {NINK})",
        "(tīṇipi paṭiccasadisā, ninnānākaraṇā)": f"({CNT['tīṇi']}လုံးသည် {PV}{SADISANI}{CC} {NINK})",
        "(noupādāmūlake tīṇi, paṭisandhikkhaṇe tīṇipi kātabbā)":
            f"({mula(NOUPADA_T)} {CNT['tīṇi']}{CC} {PS} {CNT['tīṇi']}လုံးကို {KAT})",
        "(saṃkhittaṃ. Purejātasadisaṃ ninnānākaraṇaṃ)": f"({SAMKH}{E} {cn('purejāta')}{SADISA} {NINK})",
        # Upādinna
        "(yāva utusamuṭṭhānaṃ)": f"({F.QUAL['utusamuṭṭhānaṃ']} ရုပ်အထိ)",          # (rūpaṃ supplied; logged)
        "(nahetusadisaṃ, moho natthi)": f"({cd('hetu', 'n', True)}{SADISA}{CC} {MOHO} {NATTHI})",
        "(Evaṃ itare dve gaṇanāpi sampayuttavāropi kātabbā.)": f"({EV} {gsamp} {KAT}{E})",
        "(saṃkhittaṃ. Upādinnamūlake tīṇi. )": f"({SAMKH}{E} {mula(UPADINNA_T)} {CNT['tīṇi']}{E})",
        "(upādinnamūlake tīṇi, paṭhamasseva rūpajīvitindriyaṃ, itaresu natthi)":
            (f"({mula(UPADINNA_T)} {CNT['tīṇi']}{CC} ပထမ {PANHA}၌သာ {M3.RJIVIT}{CC} {ITARE}တို့၌ "
             f"{NATTHI})"),                                                 # (pañhā supplied as 3-05; logged)
        "(saṃkhittaṃ. Yathā nikkhittapadāni vibhajitabbāni paripuṇṇāni)":
            f"({SAMKH}{E} {NIKKH} {M3.PARIP}အောင် {VIB})",
        "(saṃkhittaṃ, yathā nikkhittapadāni vitthāretabbāni)": f"({SAMKH}{CC} {NIKKH} {VITTH})",
        "(saṃkhittaṃ, yathā nikkhittapadāni vibhajitabbāni)": f"({SAMKH}{CC} {NIKKH} {VIB})",
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


SLIP_FIX = {"ahetukā nocitte khandhā vicikicchāsahagate": "ahetukā nocittā khandhā, vicikicchāsahagate",
            "No upādā dhammo": "Noupādā dhammo", "cittaṃ kaṭattā rūpānaṃ": "cittaṃ kaṭattārūpānaṃ", "khandhañca citañca": "khandhañca cittañca",
            "khandhā uppajanti.": "khandhā uppajjanti.", "cittasahabhuṃ eka khandhañca": "cittasahabhuṃ ekaṃ khandhañca"}
M3._END = M3._END.replace("|acittasamaṅgissa)", "|acittasamaṅgissa|asamaṅgissa)")


# ===================================================================================== nouns and lexicon
KABALI = M3.KABALI
SAMPADA = W("sīlasampadā", "သီလ ပြည့်စုံခြင်း", "4")[len("သီလ "):]
SAMP_X = {"vaṇṇa": "အဆင်းအရောင်", "sadda": "အသံ", "gandha": "အနံ့", "rasa": "အရသာ", "phoṭṭhabba": "အထိအတွေ့",
          "cakkhu": "မျက်စိ", "sota": "နား", "ghāna": "နှာခေါင်း", "jivhā": "လျှာ", "kāya": "ကိုယ်"}   # = 2-12 … 2-17
INDR9 = {"upekkhindriyaṃ": W("upekkhindriyaṃ", "ဥပေက္ခာ၏ စွမ်းရည်", "6"),
         "sukhindriyaṃ": W("sukhindriyaṃ", "သာယာမှု၏ စွမ်းရည်", "2"),
         "dukkhindriyaṃ": W("dukkhindriyaṃ", "နာကျင်မှု၏ စွမ်းရည်", "2")}
CITTA_N = F.LEX["cittaṃ"][0]                                    # «စိတ်» (the module's noun cittaṃ)
assert CITTA_N == _CITTA_N


GATED = {}          # id(module) -> (module, {QUAL key: value}, {LEX key: value}) added only while this chapter runs


def gate(on):
    for mod, qual, lex in GATED.values():
        for k, v in qual.items():
            if on:
                mod.QUAL[k] = v
            else:
                mod.QUAL.pop(k, None)
        for k, v in lex.items():
            if on:
                mod.LEX[k] = v
            else:
                mod.LEX.pop(k, None)


def setup_lex():
    for mod in (F, FG):
        # citta as a noun (where it is not the dyad term): neuter, -aṃ subject or object (as 3-03-06's saññojana)
        for e, (case, pl, lk) in M4._NEUT.items():
            if e in ("o", "ā"):
                continue
            mod.add_fixed(CITTA_N, case, pl, "citt" + e)
            mod.NOUN.setdefault("citt" + e, (CITTA_N, case, pl))
            mod.LEX.setdefault("citt" + e, (CITTA_N + ("+" if pl else ""), lk))
    # «ahetuke» before a term (the fallback make_ch1-03-05's qualifier, also in the primary)
    F.add_qual(F.AHETUKA, "ahetuke")
    for mod in (F, FG):
        # «kabaḷīkārāhāro» (prep: a term before «kabaḷīkāro āhāro»): the fixed noun
        for e, case in (("o", "n"), ("aṃ", "a"), ("assa", "g")):
            mod.add_fixed(KABALI, case, False, "kabaḷīkārāhār" + e)
            mod.NOUN.setdefault("kabaḷīkārāhār" + e, (KABALI, case, False))
            mod.LEX.setdefault("kabaḷīkārāhār" + e, (KABALI, {"n": "n", "a": "a", "g": "g"}[case]))
        # «X-viññāṇasahagata» in all its forms (3-01-02: «-sahagataṃ», «-sahagatānaṃ»)
        # (only while this chapter runs: with them make_ch3-01-02 would read 3-02 ^7-25-… «cakkhuviññāṇasahagato eko
        # khandho ca cakkhāyatanañca tiṇṇannaṃ khandhānaṃ» otherwise than published; logged for the harmonise pass)
        for _s in ("cakkhu", "sota", "ghāna", "jivhā", "kāya"):
            q = f"{K.CAKKHUVINNANA[_s]} သိစိတ်{mod.SAHAGATA}"
            for e in ("o", "aṃ", "ā", "e", "assa", "ānaṃ"):
                w = f"{_s}viññāṇasahagat{e}"
                if w not in mod.QUAL:
                    GATED.setdefault(id(mod), (mod, {}, {}))[1][w] = q
                if w not in mod.LEX:
                    GATED.setdefault(id(mod), (mod, {}, {}))[2][w] = (q, "adj")
        # «cittasampayuttaka» / «cittasaṃsaṭṭhā» on a noun (the Mātikā words, pi-1 ^1-M2-58 / ^1-M2-59)
        for e in ("o", "aṃ", "ā", "e", "assa", "ānaṃ"):
            mod.add_qual(CSAMP, "cittasampayuttak" + e)
            mod.LEX.setdefault("cittasampayuttak" + e, (CSAMP, "adj"))
        mod.add_qual(CSAMS, "cittasaṃsaṭṭhā")
        mod.LEX.setdefault("cittasaṃsaṭṭhā", (CSAMS, "adj"))
        # the indriyas of 3-09 (pi-2 / pi-6 final)
        for w, my in INDR9.items():
            mod.add_fixed(my, "n", False, w)
            mod.LEX.setdefault(w, (my, "na"))
            mod.add_fixed(my, "g", False, w[:-1] + "ssa")
            mod.LEX.setdefault(w[:-1] + "ssa", (my, "g"))
        # X-sampadā (as make_ch2-12-17: «X ပြည့်စုံခြင်း»)
        for x, my in SAMP_X.items():
            v = new(f"{x}sampadā", f"{my} {SAMPADA}")
            mod.LEX.setdefault(f"{x}sampadaṃ", (v, "a"))
            mod.LEX.setdefault(f"{x}sampadā", (v, "n"))
        mod.LEX.setdefault("imassa", ("ဤ", "x"))
        mod.LEX.setdefault("kāyassa", (mod.FIXED["imassa kāyassa"][0][len("ဤ"):], "g"))
        mod.TAIL.setdefault("asamaṅgissa", (f"{mod.DHAMMA}နှင့် ပြည့်စုံသူ", "G"))
        mod.add_qual(mod.QUAL["purimā purimā"], "purimaṃ purimaṃ")
    # coordinations with the noun citta for the lexicon frames (rendered once by the noun-phrase engine)
    for ph, role in (("cittañca sampayuttakā khandhā ca", "n"), ("cittañca sampayuttake khandhe ca", "@ārabbha"),
                     ("khandhā ca cittañca", "n"), ("khandhe ca cittañca", "@ārabbha"),
                     ("cittañca vatthuñca", "n"), ("cittañca mahābhūtā ca", "n")):
        my = F.np_my(ph.split(), iter([]), role)[0]
        for mod in (F, FG):
            mod.LEX.setdefault(ph, (my, "x"))


# ===================================================================================== unique fragments
SKF_ADD = {}


def setup_sk():
    kh, lk, Q = F.KHANDHA, F.LAKAUNG, F.QUAL
    garu = F.LEX["garuṃ katvā"][0].split(" ")[1]                       # «လေးစားဖွယ်ရာ» (cut by «…», as 3-03-06)
    ariya = F.translate("ariyā maggā vuṭṭhahitvā maggaṃ garuṃ katvā paccavekkhanti.")
    cut = ariya[:ariya.index(garu) + len(garu)]
    assert cut.endswith(f"မဂ်ကို {garu}"), cut
    SKF_ADD.update({
        "ariyā maggā vuṭṭhahitvā maggaṃ garuṃ": cut,
        "maggaṃ garuṃ": f"{F.LEX['maggaṃ'][0]}ကို {garu}",
        "phalaṃ garuṃ": f"{F.LEX['phalaṃ'][0]}ကို {garu}",
        "purimā purimā §T§ā": f"{Q['purimā purimā']} {{T1}}",
        "purimaṃ purimaṃ cittaṃ pacchimassa pacchimassa":
            f"{Q['purimā purimā']} {CITTA_N}သည် {Q['pacchimassa pacchimassa']}",
    })
    AY = F.FIXED
    pho, vt = AY["phoṭṭhabbāyatanaṃ"][0], F.VATTHU
    SKF_ADD.update({
        "kāyindriyaṃ ca": f"{AY['kāyindriyaṃ'][0]}{lk}",                    # cut short (as «dve khandhā ca»)
        "kāyaviññāṇasahagatā khandhā ca": f"{K.CAKKHUVINNANA['kāya']} သိစိတ်{F.SAHAGATA} {kh}{lk}",
        "§T§aṃ phoṭṭhabbāyatanaṃ ca": f"{{T1}} {pho}{lk}",
        "§T§aṃ phoṭṭhabbāyatanañca vatthu ca": f"{{T1}} {pho}{lk}{C} {vt}{lk}",
        # (cut before its link: the objects take the line's link, as «dve khandhe ca…»)
        "ahetukapaṭisandhikkhaṇe §T§aṃ ekaṃ khandhañca cittañca": lambda sl: (
            f"{F.PREFIX['ahetukapaṭisandhikkhaṇe']} {sl['T'][0]} {kh} {F.PAA[1]}{K.ROLE_MARK[K.CUR['link']]}{lk}{C} "
            f"{CITTA_N}{K.ROLE_MARK[K.CUR['link']]}{lk}"),
        # «uppajjati namaggapaccayā pañca…»: the count after the condition, the verb before it (as «…paccayā… tīṇi»)
        "§T§aṃ dhammaṃ paṭicca §T§o dhammo uppajjati §C§ā pañca":
            f"{{T1}} {F.DHAMMA}ကို မှီ၍ {{T2}} {F.DHAMMA}သည် {{C1.ab}} {F.UP} {F.COUNT['pañca']}",
    })
    # «senāsanaṃ cittaṃ X-ānaṃ khandhānaṃ cittassa ca» (as written: citta read as the last support of the list)
    SKF_ADD["senāsanaṃ cittaṃ §T§ānaṃ khandhānaṃ ca cittassa ca §C§ena paccayo"] = (
        f"{F.LEX['senāsanaṃ'][0]}{C} {CITTA_N}သည် {{T1}} {kh}တို့အား{lk}{C} {CITTA_N}အား{lk} {{C1.if}}")
    mh = f"{F.NOUN['mahābhūtā'][0]} {F.PAA[1]}"                         # «ekaṃ mahābhūtaṃ…» «မူလဓာတ်ကြီး တစ်ပါး…»
    b, a, u, asa = Q["bāhiraṃ"], Q["āhārasamuṭṭhānaṃ"], Q["utusamuṭṭhānaṃ"], F.PREFIX["asaññasattānaṃ"]
    SKF_ADD["bāhiraṃ utusamuṭṭhānaṃ asaññasattānaṃ ekaṃ mahābhūtaṃ"] = f"{b}{C} {u}{C} {asa} {mh}"
    SKF_ADD["bāhiraṃ āhārasamuṭṭhānaṃ utusamuṭṭhānaṃ asaññasattānaṃ ekaṃ mahābhūtaṃ"] = f"{b}{C} {a}{C} {u}{C} {asa} {mh}"
    for mod in (F, FG):
        mod.SKF.update(SKF_ADD)
        # an asyndetic list of the kinds of matter without «…» (with «…» the module gives «ပြင်ပ… အာဟာရမှ …»): «၊»
        b, a, u, asa = Q["bāhiraṃ"], Q["āhārasamuṭṭhānaṃ"], Q["utusamuṭṭhānaṃ"], F.PREFIX["asaññasattānaṃ"]
        pre = {}
        for e in ("aṃ", "e"):
            ws = {"b": f"bāhir{e}", "a": f"āhārasamuṭṭhān{e}", "u": f"utusamuṭṭhān{e}"}
            for keys in ("bau", "bu"):
                ph = " ".join(ws[k] for k in keys)
                my = (C + " ").join({"b": b, "a": a, "u": u}[k] for k in keys)
                mod.LEX.setdefault(ph, (my, "x"))
                pre[ph + " asaññasattānaṃ"] = my + C + " " + asa
        old = dict(mod.PREFIX)
        mod.PREFIX.clear()
        mod.PREFIX.update(pre)                      # the longer prefixes first (the clause regex alternation)
        mod.PREFIX.update(old)
        for k, v in pre.items():
            mod.LEX.setdefault(k, (v, "x"))
        mod.LEX.setdefault("naadhipatiyā", (mod.cond("adhipati", "loc", True), "x"))     # cut by «…» (no count)
        mod.LEX.setdefault("pubbe samudāciṇṇe", (mod.LEX["pubbe samudāciṇṇe kilese"][0][:-len("ကိလေသာ+")].rstrip(),
                                                  "x"))                                # cut by «…»


_PIECE0 = None
_IN_PIECE = [False]
MY_RUN = [False]                 # the extensions below act only while this chapter is translated (--regress: identical)
PIECE_LOG = collections.Counter()


def _piece(p, slots, ti, ci, vi=None):
    """make_ch1-01's piece; then (this chapter only) a piece without slots cut short before «…»: «dve khandhe ca» =
    the object with the line's link and «လည်းကောင်း» (as the module renders the fragment «dve khandhe ca…»), other
    slot-free pieces through the fragment tables («kāyindriyaṃ ca», the bāhira lists)"""
    r = _PIECE0(p, slots, ti, ci, vi)
    if r is not None or not MY_RUN[0] or "§" in p or _IN_PIECE[0]:
        return r
    _IN_PIECE[0] = True
    try:
        ws = p.split()
        if len(ws) > 1 and ws[-1] == "ca" and F._case_of(ws[:-1]) == "a" and K.CUR["link"]:
            r0, _, _ = K.np_my2(ws[:-1], iter([]), "")
            r = re.sub(r"များ$", "တို့", r0) + K.ROLE_MARK[K.CUR["link"]] + F.LAKAUNG
        else:
            r = F.try_sk(p.strip(), F.SKF)
            if r is None:
                r = F.frags_my(p)
        PIECE_LOG[(p, r)] += 1
    except (KeyError, F.Miss, IndexError, StopIteration):
        r = None
    finally:
        _IN_PIECE[0] = False
    return r


def setup():
    global _PIECE0
    setup_names()
    setup_lex()
    setup_notes()
    M3.SLIP_FIX.update(SLIP_FIX)
    setup_sk()
    _PIECE0 = K._piece
    K._piece = _piece


setup()


def stub_notes():
    """--stub (development only): every note the engine cannot read gets a placeholder, so that the other unmatched
    sentences show (nothing is written in this mode)"""
    src = (PALI / NAMES[0]).read_text(encoding="utf-8-sig")
    stubs = {}
    for d, t in M3.parts_of(src):
        for m in re.finditer(r"\([^()]*\)", re.sub(r"\{[^{}]*\}", "", t)):
            k = m[0]
            if re.fullmatch(r"\(\d+\)", k) or k in M3.NOTEP or k in stubs:
                continue
            M3.set_dyad(F, d)
            kk = M3.prep_dyad(k, d)
            try:
                r = K.note_unit(kk)
            except Exception:
                r = None
            if r is None and kk not in F.NOTES and F.lc(kk) not in F.NOTES:
                stubs[k] = "(STUB)"
                if "--list" in sys.argv:
                    print("NOTE", d, k)
    base = len(M3.NOTEP)
    for i, (p_, my) in enumerate(stubs.items(), base):
        M3.NOTEP[p_] = my
        K.NOTE_FIXED[f"⁑d{i}"] = my[1:-1]
        for mod in (F, FG):
            mod.NOTES[f"(⁑d{i})"] = my
    M3.set_dyad(F, None)
    print(len(stubs), "notes stubbed")


# a note that the Pāli does not close («(saṃkhittaṃ, yathā nikkhittapadāni vitthāretabbāni. (2)», ^7-32-466): read with
# its «)» in memory (the note of the next line), then the «)» removed and the «.» kept as «။» (as written; logged)
UNCLOSED = "(saṃkhittaṃ, yathā nikkhittapadāni vitthāretabbāni. (2)"


def translate(name):
    src = (PALI / name).read_text(encoding="utf-8-sig")
    fixed = src
    if UNCLOSED in src:
        assert src.count(UNCLOSED) == 1
        F.SLIPS.add(f"«{UNCLOSED}»: the note is not closed (no «)» written)")
        fixed = src.replace(UNCLOSED, UNCLOSED.replace(". (2)", "). (2)"))
    MY_RUN[0] = True
    gate(True)
    try:
        outs = [M3.translate_part(d, t) for d, t in M3.parts_of(fixed)]
    finally:
        MY_RUN[0] = False
        gate(False)
    txt = "\n".join(outs)
    if fixed != src:
        pl = [l for l in src.splitlines() if l.strip()]
        ml = txt.split("\n")
        j = 0
        for i, l in enumerate(ml):
            if not l.strip():
                continue
            if UNCLOSED in pl[j]:
                assert l.count(")။ (2)") == 1, l
                ml[i] = l.replace(")။ (2)", "။ (2)")
            j += 1
        txt = "\n".join(ml)
    return txt


def regress():
    bad = M4.regress()
    for n in M4.NAMES:
        txt = M4.translate(n)
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
        if "--stub" in sys.argv:
            stub_notes()
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
    if "--pieces" in sys.argv:
        for (pp, rr), c in PIECE_LOG.most_common():
            print(f"[{c}] {pp} => {rr}")
    if F.SLIPS and "--slips" in sys.argv:
        print("slips:", *sorted(F.SLIPS), sep="\n  ")


if __name__ == "__main__":
    main()
