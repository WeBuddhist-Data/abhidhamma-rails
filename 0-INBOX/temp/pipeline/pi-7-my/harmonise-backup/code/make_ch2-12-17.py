"""Burmese zero-shot of pi-7 2-12 uppannattika, 2-13 atītattika, 2-14 atītārammaṇattika, 2-15 ajjhattattika,
2-16 ajjhattārammaṇattika, 2-17 sanidassanasappaṭighattika («အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ»), from the Pāli only.

usage: python3 -I -X utf8 make_ch2-12-17.py [chapter ...] [--dev] [--regress] [--slips] [--out DIR]
  (no flag)  translate the chapters and write them; stops on the first unmatched sentence (nothing is guessed).
  --dev      do not stop: list every unmatched skeleton with its count in chk-ch2-12-17/dev.txt (nothing written).
  --regress  regenerate the approved sample (1-00, 1-02) and the finished group 2-03 … 2-06 in memory through this
             script and compare them with the published files (they must be identical).

Engines (all read-only, imported, never run as scripts): make_ch2-03-06.py is IMPORTED for its in-memory engine
(PRIMARY: my7_formulas + make_sample + make_ch1-01; FALLBACK per sentence unit: an isolated copy with
make_ch1-03-05) and its extensions (notes, lexicon, chains). No main block of another script runs; no file of the
sample or of another group is edited. This script adds the six triads (pi-1 final Mātikā ^1-M1-17 … ^1-M1-22), their
names, notes and unique sentences; every new string is logged in notes-ch2-12-17.md.
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
NAMES = ["2-12-uppannattika.md", "2-13-atitattika.md", "2-14-atitarammanattika.md", "2-15-ajjhattattika.md",
         "2-16-ajjhattarammanattika.md", "2-17-sanidassanasappatighattika.md"]
CHK = HERE / "chk-ch2-12-17"
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


# ===================================================================================== the six triads (pi-1 final)
def _tw(pali, my, bid, tail=" သဘောတရားများ"):
    """a pi-1 Mātikā term, read from the FINAL rails (attributive form, without « သဘောတရားများ»)"""
    return W(pali, my + tail, "1", bid)[:-len(tail)] if tail else W(pali, my, "1", bid)


TRIADS_ADD = {
    "uppanna": {
        "uppann": _tw("uppannā dhammā", "ဖြစ်ပေါ်ပြီးသော", "^1-M1-17"),
        "anuppann": _tw("anuppannā dhammā", "မဖြစ်ပေါ်သေးသော", "^1-M1-17"),
        # uppādī (an -in stem): prep() reads its endings as the a-stem endings «uppād-o/-aṃ/…»
        "uppād": _tw("uppādino dhammā", "ဖြစ်ပေါ်လာမည့်", "^1-M1-17"),
    },
    "atita": {
        "atīt": _tw("atītā dhammā", "အတိတ်", "^1-M1-18"),
        "anāgat": _tw("anāgatā dhammā", "အနာဂတ်", "^1-M1-18"),
        "paccuppann": _tw("paccuppannā dhammā", "ပစ္စုပ္ပန်", "^1-M1-18"),
    },
    "atitarammana": {
        "atītārammaṇ": _tw("atītārammaṇā dhammā", "အတိတ်ကို အာရုံပြုသော", "^1-M1-19"),
        "anāgatārammaṇ": _tw("anāgatārammaṇā dhammā", "အနာဂတ်ကို အာရုံပြုသော", "^1-M1-19"),
        "paccuppannārammaṇ": _tw("paccuppannārammaṇā dhammā", "ပစ္စုပ္ပန်ကို အာရုံပြုသော", "^1-M1-19"),
    },
    "ajjhatta": {
        "ajjhatt": _tw("ajjhattā dhammā", "မိမိ၌ ရှိသော", "^1-M1-20"),
        "bahiddh": _tw("bahiddhā dhammā", "မိမိ၏ ပြင်ပ၌ ရှိသော", "^1-M1-20"),
        "ajjhattabahiddh": _tw("ajjhattabahiddhā dhammā", "မိမိ၌နှင့် မိမိ၏ ပြင်ပ၌ ရှိသော", "^1-M1-20"),
    },
    "ajjhattarammana": {
        "ajjhattārammaṇ": _tw("ajjhattārammaṇā dhammā", "မိမိ၌ ရှိသည်ကို အာရုံပြုသော", "^1-M1-21"),
        "bahiddhārammaṇ": _tw("bahiddhārammaṇā dhammā", "မိမိ၏ ပြင်ပ၌ ရှိသည်ကို အာရုံပြုသော", "^1-M1-21"),
        "ajjhattabahiddhārammaṇ": _tw("ajjhattabahiddhārammaṇā dhammā",
                                      "မိမိ၌နှင့် မိမိ၏ ပြင်ပ၌ ရှိသည်ကို အာရုံပြုသော", "^1-M1-21"),
    },
    "sanidassana": {
        "sanidassanasappaṭigh": _tw("sanidassanasappaṭighā dhammā", "မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိသော", "^1-M1-22"),
        "anidassanasappaṭigh": _tw("anidassanasappaṭighā dhammā", "မမြင်နိုင်သော်လည်း ထိခိုက်မှု ရှိသော",
                                   "^1-M1-22"),
        # the pi-1 line carries a spelling variant between the term and its noun: the term alone is witnessed
        "anidassanaappaṭigh": _tw("anidassanaappaṭighā", "မမြင်နိုင်၊ ထိခိုက်မှုလည်း မရှိသော", "^1-M1-22", ""),
    },
}
CH_TRIAD = dict(zip(NAMES, TRIADS_ADD))
# endings: the a-stem endings of 1-03 … 2-06 + two «X-ārammaṇa-Y-citta-samaṅgissa» tails (2-14, 2-16)
_END = M._END.replace("|acittasamaṅgissa", "|apaccuppannacittasamaṅgissa|abahiddhācittasamaṅgissa|acittasamaṅgissa"
                      ).replace("|ānaṃ|", "|ānaṃ|ānañca|")
assert _END != M._END


def set_triad(mod, tri):
    M.set_triad(mod, None)                       # the 2-03 … 2-06 triads off
    for t in list(mod.TRIADS):
        if t in TRIADS_ADD or t.endswith("_cut"):
            mod.TRIADS.pop(t, None)
            mod.TRIAD_END.pop(t, None)
    if tri:
        mod.TRIADS[tri] = TRIADS_ADD[tri]
        mod.TRIAD_END[tri] = _END
    mod.rebuild()


# ===================================================================================== Pāli preparation (in memory)
# uppādī (an -in stem) -> the a-stem endings the frames know (the Burmese of a term does not depend on its ending; the
# noun carries number and case), as make_ch2-03-06 does for ācayagāmī.
_IN = {"ī": "o", "iṃ": "aṃ", "issa": "assa", "iñca": "añca", "īnaṃ": "ānaṃ", "iyā": "āya", "ino": "ā",
       "icittasamaṅgissa": "acittasamaṅgissa"}
_IN_RE = re.compile(r"(?<!" + WCH + r")([Uu]ppād)(" + "|".join(sorted(_IN, key=len, reverse=True)) + r")(?!"
                    + WCH + ")")
SLIP_FIX = {   # source slips: read as the usual form (logged); the Burmese is that of the usual form
    "sotudhātuyā": "sotadhātuyā",
    "vipāko paccuppano eko": "vipāko paccuppanno eko",
    "kaṭatārūpaṃ": "kaṭattārūpaṃ",
}
_STEMS_RX = "|".join(f"[{k[0].upper()}{k[0]}]" + re.escape(k[1:]) for tab in TRIADS_ADD.values()
                     for k in sorted(tab, key=len, reverse=True))


NOTEP = {}          # notes whose Pāli holds a triad term or several sentences: Pāli -> Burmese (set up below)


def prep(text):
    text = M.prep(text)
    for i, a in enumerate(NOTEP):
        text = text.replace(a, f"(⁑q{i})")

    def fix(t):
        for a, b in SLIP_FIX.items():
            if a in t:
                F.SLIPS.add(f"«{a}» read as «{b}»")
                t = t.replace(a, b)
        t = re.sub(r"(?<!" + WCH + r")([Uu]ppād)ī(?= khandh([āe])(?!" + WCH + "))", lambda m: m[1] + m[2], t)
        t = _IN_RE.sub(lambda m: m[1] + _IN[m[2]], t)
        return re.sub(r"(?<![\wāīūṃṅñṭḍṇḷ])(" + _STEMS_RX + r")ādhipati(?![\wāīūṃṅñṭḍṇḷ])", r"\1o adhipati", t)
    return M._outside_braces(text, fix)


# ===================================================================================== numbers
# short forms in -vīsa (as make_ch2-03-06 «ekavīsa»): the 1-03 … 1-05 values of the -vīsati forms; dvādasa / tevīsa as
# 1-03 … 1-05 (they are on the fallback copy only)
NUM_ADD = {"dvāvīsa": (22, G.TEEN["dvāvīsati"][1]), "bāvīsa": (22, G.TEEN["bāvīsati"][1]),
           "catuvīsa": (24, G.TEEN["catuvīsati"][1]), "pañcavīsa": (25, new("pañcavīsa(ti)", "နှစ်ဆယ့်ငါး")),
           "dvādasa": G.TEEN["dvādasa"], "tevīsa": G.TEEN["tevīsa"]}


def setup_numbers(mod):
    for w, (n, my) in NUM_ADD.items():
        mod.COUNT.setdefault(w, my + "ခု")
        mod.COUNT_VAL.setdefault(w, n)
        mod.LEX.setdefault(w, (mod.COUNT[w], "x"))
    mod._CNT_ALT = "|".join(sorted(mod.COUNT, key=len, reverse=True))
    mod.COUNT_RE = re.compile(r"(?<![\wāīūṃṅñṭḍṇḷ])(?P<neg>[Nn]a|[Nn]o)?(?P<loc>(?i:" + mod._LOC_ALT + r")) (?P<num>"
                              + mod._CNT_ALT + r")(?![\wāīūṃṅñṭḍṇḷ])")


# ===================================================================================== chapter names
TIKA_ADD = {   # NEW (the pattern of 1-03 … 2-11: the key notion of the first term + «သုံးမျိုးတွဲ»)
    "Uppannattikaṃ": new("Uppannattikaṃ", f"ဖြစ်ပေါ်ပြီးခြင်း {F.TIKA}"),
    "Atītattikaṃ": new("Atītattikaṃ", f"အတိတ် {F.TIKA}"),
    "Atītārammaṇattikaṃ": new("Atītārammaṇattikaṃ", f"အတိတ်ကို အာရုံပြုခြင်း {F.TIKA}"),
    "Ajjhattattikaṃ": new("Ajjhattattikaṃ", f"မိမိ၌ ရှိခြင်း {F.TIKA}"),
    "Ajjhattārammaṇattikaṃ": new("Ajjhattārammaṇattikaṃ", f"မိမိ၌ ရှိသည်ကို အာရုံပြုခြင်း {F.TIKA}"),
    "Sanidassanasappaṭighattikaṃ": new("Sanidassanasappaṭighattikaṃ", f"မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိခြင်း {F.TIKA}"),
}


def setup_names():
    F.HLINES["Pañhāvāro niṭṭhito."] = F.finished(F.HEAD["Pañhāvāro"])     # the colophon form of the sample
    F.HLINES["Dhammānulome tikapaṭṭhānaṃ niṭṭhitaṃ."] = (f"{F.HEAD['Dhammānulome']} “{F.HEAD['Tikapaṭṭhānaṃ']}” "
                                                          f"{F.DONE}{END}")
    F.HLINES["Dutiyo bhāgo niṭṭhito."] = new("Dutiyo bhāgo niṭṭhito.", f"ဒုတိယ အပိုင်း {F.DONE}{END}")
    F.TIKA_NAME.update(TIKA_ADD)
    for p, my in TIKA_ADD.items():
        F.HLINES[f"{p} niṭṭhitaṃ."] = F.finished(my)


# ===================================================================================== notes, lexicon
# X-sampadā «X ပြည့်စုံခြင်း» (pi-1 / pi-4 sīlasampadā «သီလ ပြည့်စုံခြင်း»); X = the bases as the module's nouns
SAMPADA = W("sīlasampadā", "သီလ ပြည့်စုံခြင်း", "4")[len("သီလ "):]
_SAMP_X = {"vaṇṇa": "အဆင်းအရောင်", "sadda": "အသံ", "gandha": "အနံ့", "rasa": "အရသာ", "phoṭṭhabba": "အထိအတွေ့",
           "cakkhu": "မျက်စိ", "sota": "နား", "ghāna": "နှာခေါင်း", "jivhā": "လျှာ", "kāya": "ကိုယ်"}
PATTHAY = new("patthayamāno", "တောင့်တလျက်")            # patthanā «တောင့်တခြင်း» (sample)


ANUPASSANA = W("anupassanā", "အဖန်ဖန် ရှုခြင်း", "2")
PATISANDHICITTA = new("paṭisandhicittaṃ", f"{F.PATISANDHI} စိတ်")       # as cuticittaṃ «စုတေခြင်း စိတ်» (sample)
# the words of another triad used as plain adjectives (2-14 atīta-, 2-16 ajjhatta- / bahiddhā): the pi-1 values
ADJ = {"atīt": TRIADS_ADD["atita"]["atīt"], "anāgat": TRIADS_ADD["atita"]["anāgat"],
       "paccuppann": TRIADS_ADD["atita"]["paccuppann"], "ajjhatt": TRIADS_ADD["ajjhatta"]["ajjhatt"]}
ADJ_END = ("aṃ", "ā", "e", "o", "assa", "ānaṃ")


def setup_lex():
    for mod in (F, FG):
        mod.TAIL["apaccuppannacittasamaṅgissa"] = (new("-paccuppannacittasamaṅgissa",
                                                       f"{TRIADS_ADD['atita']['paccuppann']} "
                                                       f"{mod.TAIL['acittasamaṅgissa'][0]}"), "G")
        mod.TAIL["abahiddhācittasamaṅgissa"] = (new("-bahiddhācittasamaṅgissa",
                                                    f"{TRIADS_ADD['ajjhatta']['bahiddh']} "
                                                    f"{mod.TAIL['acittasamaṅgissa'][0]}"), "G")
        for st, my in ADJ.items():
            for e in ADJ_END:
                mod.LEX.setdefault(st + e, (my, "adj"))
        mod.LEX.setdefault("bahiddhā", (TRIADS_ADD["ajjhatta"]["bahiddh"], "adj"))
        for x, my in (("anicc", "မမြဲဟု"), ("dukkh", "ဆင်းရဲဟု"), ("anatt", "အတ္တ မဟုတ်ဟု")):   # as aniccato …
            v = new(f"{x}ānupassanā", f"{my} {ANUPASSANA}")
            mod.LEX.setdefault(f"{x}ānupassanā", (v, "n"))
            mod.LEX.setdefault(f"{x}ānupassanāya", (v, "g"))
        mod.LEX.setdefault("paṭisandhicittaṃ", (PATISANDHICITTA, "na"))
        mod.LEX.setdefault("paṭisandhicittassa", (PATISANDHICITTA, "g"))
        # the higher knowledges as objects (1-01 has them as subjects, «n»): the phrase with its verb
        for k in ("iddhividhañāṇaṃ", "cetopariyañāṇaṃ", "pubbenivāsānussatiñāṇaṃ", "yathākammūpagañāṇaṃ",
                  "anāgataṃsañāṇaṃ"):
            my = F.LEX[k][0]
            mod.LEX.setdefault(k + " paccavekkhati", (f"{my}ကို {F.LEX['paccavekkhati'][0]}", "x"))
            mod.LEX.setdefault(k + " garuṃ katvā", (f"{my}ကို {F.GARU}", "x"))
        # «dve mahābhūtā…» (cut by «…»): as the module's «dve khandhā» (the bare count word would come first)
        mod.LEX.setdefault("dve mahābhūtā", (f"{M.MAHABHUTA} {F.PAA[2]}+", "n"))
        mod.LEX.setdefault("paro", (M.PARA, "n"))                      # another person (pi-? para «သူတစ်ပါး»)
        # matter (pi-1 / pi-2 final)
        apo = W("āpodhātu", "ရေဓာတ်", "1")
        mod.add_noun(apo, n=["āpodhātu"], a=["āpodhātuṃ"])
        mod.add_fixed(W("itthindriyaṃ", "မိန်းမ၏ စွမ်းရည်", "1"), "n", False, "itthindriyaṃ", "Itthindriyaṃ")
        mod.add_fixed(W("indriyaṃ", "စွမ်းရည်", "1"), "n", False, "indriyaṃ")
        mod.add_fixed(W("purisindriyaṃ", "ယောက်ျား၏ စွမ်းရည်", "1"), "n", False, "purisindriyaṃ", "Purisindriyaṃ")
        mod.LEX.setdefault("purisindriyaṃ", (mod.FIXED["purisindriyaṃ"][0], "n"))
        mod.LEX.setdefault("āpodhātu", (apo, "n"))
        mod.LEX.setdefault("āpodhātuṃ", (apo, "a"))
        mod.LEX.setdefault("itthindriyaṃ", (mod.FIXED["itthindriyaṃ"][0], "n"))
        jiv = W("jīvitindriyaṃ", "အသက်၏ စွမ်းရည်", "1")
        mod.LEX.setdefault("jīvitindriyaṃ", (jiv, "n"))
        mod.LEX.setdefault("itthindriyassa", (mod.FIXED["itthindriyaṃ"][0], "g"))
        mod.LEX.setdefault("kabaḷīkāraṃ āhāraṃ", (mod.FIXED["kabaḷīkāro §V§ āhāro"][0], "a"))
        mod.LEX.setdefault("kabaḷīkārāhārassa ca", (mod.FIXED["kabaḷīkāro §V§ āhāro"][0] + "အား" + mod.LAKAUNG, "x"))
        mod.add_fixed("ကိုယ်", "g", False, "kāyassa")
        mod.LEX.setdefault("kāyassa", ("ကိုယ်", "g"))
        mod.LEX.setdefault("pubbe samudāciṇṇe", (mod.LEX["pubbe samudāciṇṇe kilese"][0][:-len(" ကိလေသာ+")], "x"))
        mod.LEX.setdefault("cittasamaṅgissa", (mod.TAIL["acittasamaṅgissa"][0], "G"))
        mod.LEX.setdefault("ajjhattikā indriyā", (f"{M.AJJHATTIKA} {F.N['indriya']}များ", "x"))
        mod.LEX.setdefault("utusamuṭṭhānā mahābhūtā", (f"{mod.QUAL['utusamuṭṭhānaṃ']} {M.MAHABHUTA}+", "n"))
        mod.add_qual(mod.QUAL["utusamuṭṭhānaṃ"], "utusamuṭṭhānā")
        for ay, my in mod._AY.items():                       # āyatana names inside «…» lists
            mod.LEX.setdefault(ay, (my, "n"))
            mod.LEX.setdefault(ay[:-1] + "ssa", (my, "g"))
        mod.LEX.setdefault("rūpāyatanañca cakkhu ca", (
            f"{mod._AY['rūpāyatanaṃ']}{mod.LAKAUNG}{C} {mod.LEX['cakkhuṃ'][0]}{mod.LAKAUNG}", "x"))
        mod.LEX.setdefault("cittasamuṭṭhānānaṃ rūpānaṃ kaṭattārūpānaṃ upādārūpānaṃ", (
            f"{mod.QUAL['cittasamuṭṭhānānaṃ']} ရုပ်တို့အား{C} {mod.KATATTARUPA}တို့အား{C} "
            f"{mod.FIXED['upādārūpānaṃ'][0]}တို့အား", "x"))
        for dh in ("cakkhu", "sota", "ghāna", "jivhā", "kāya"):
            mod.LEX.setdefault(dh + "viññāṇassa", (mod._DH[dh + "viññāṇadhātu"][:-len(" ဓာတ်")], "g"))
        mod.LEX.setdefault("phoṭṭhabbāyatanañca kāyāyatanañca", (
            f"{mod._AY['phoṭṭhabbāyatanaṃ']}{mod.LAKAUNG}{C} {mod._AY['kāyāyatanaṃ']}{mod.LAKAUNG}", "x"))
        mod.LEX.setdefault("dibbaṃ cakkhuṃ", (K.DIBBACAKKHU, "a"))
        mod.LEX.setdefault("dibbaṃ sotadhātuṃ", (K.DIBBASOTA, "a"))
    for mod in (F, FG):
        for x, my in _SAMP_X.items():
            v = new(f"{x}sampadā", f"{my} {SAMPADA}")
            mod.LEX.setdefault(f"{x}sampadaṃ", (v, "a"))
            mod.LEX.setdefault(f"{x}sampadā", (v, "n"))
        mod.LEX.setdefault("patthayamāno", ("ကို " + PATTHAY, "post"))
        mod.LEX.setdefault("kāyikassa", (K.KAYIKA, "x"))     # «kāyikassa…» (the pair cut by «…»)
        # two objects side by side without «…pe…» (as written; joined by «၊»)
        mod.LEX.setdefault("ghānasampadaṃ jivhāsampadaṃ", (
            f"{mod.LEX['ghānasampadaṃ'][0]}{C} {mod.LEX['jivhāsampadaṃ'][0]}", "a"))
        mod.LEX.setdefault("bhojanaṃ senāsanaṃ", (
            f"{mod.LEX['bhojanaṃ'][0]}{C} {mod.LEX['senāsanaṃ'][0]}", "a"))
    F.HEAD.setdefault("Paccanīyānulomaṃ", F.HLINES["Paccanīyānulomaṃ."][:-1])
    vt, kh = F.VATTHU, F.KHANDHA
    pv = new("pañcaviññāṇasahagataṃ", f"{F.LEX['pañcaviññāṇaṃ'][0]}{F.SAHAGATA}")   # as catuviññāṇasahagataṃ
    SKF_ADD["pañcaviññāṇasahagataṃ §T§aṃ ekaṃ"] = f"{pv} {{T1}} {F.PAA[1]}"   # as 2-03 … 2-06 «ahetukaṃ ekaṃ»
    SK_ADD.update({
        # two pairs in one sentence (not a list of three subjects): «khandhā → vatthu, vatthu → khandhā»
        "khandhā vatthussa, vatthu khandhānaṃ §C§ena paccayo": f"{kh}တို့သည် {vt}အား{C} {vt}သည် {kh}တို့အား {{C1.if}}",
    })
    for mod in (F, FG):
        mod.SK.update(SK_ADD)
        mod.SKF.update(SKF_ADD)


SK_ADD, SKF_ADD = {}, {}


# ===================================================================================== editorial notes
EVA = W("eva", "ပင်", "5") if False else "ပင်"          # eva «ပင်» (pi-5 termbase; 2-01-02 «…နှင့်ပင် တူကြသည်»)
TIKA_REF = {"uppannattik": TIKA_ADD["Uppannattikaṃ"]}


# words of the notes (NEW unless marked; the shared ones from 1-01 (K), 1-03 … 1-05 (G), 2-01 … 2-02 and 2-03 … 2-06 (M))
IMINA = new("iminā kāraṇena", "ဤနည်းလမ်းဖြင့်")                      # as 2-01 … 2-02
ASAMM = S.PH["asammuyhantena"]                                         # «မရောထွေးစေဘဲ» (sample; 2-01 … 2-02)
AVASESA_A = new("avasesā (attributive)", "ကြွင်းသော")                   # as 2-01 … 2-02
SADISA_PL = K.SADISANI                                                 # «နှင့် တူကြသည်» (1-01; 2-01 … 2-02)
MUL_A = new("-mūlakā (attributive)", "ကို အခြေခံသော")                    # as 2-01 … 2-02
NINNANAK = new("ninnānākaraṇaṃ / -ā", f"{G.NANAKARANA} {K.NATTHI}")     # nānākaraṇaṃ «ကွဲပြားချက်» (1-03 … 1-05)
TIVIDHA = new("tividharūpasaṅgaho", "ရုပ် သုံးမျိုးကို " + W("saṅgaho", "စုစည်းခြင်း"))
PANCAVOK = W("pañcavokāre", "အစုအဝေး ငါးပါး ရှိသော ဘဝ")
VARA_N = {v: F.HEAD[v] for v in ("Paṭiccavāro", "Sahajātavāro", "Paccayavāro", "Nissayavāro", "Saṃsaṭṭhavāro",
                                 "Sampayuttavāro")}
ARUPA_N = F.ARUPA + " " + F.DHAMMA                                     # «ရုပ် မဟုတ်သော သဘောတရား» (2-01 … 2-02)
MATIKA_P = W("Mātikā", "ခေါင်းစဉ်စာရင်း", "1") + f" {F.PADA}"          # mātikāpadāni
ASANNA = "အသညသတ်"                                                       # asaññasatta (1-01 «အသညသတ်တို့၏»)
PAVPAT_A = f"ဘဝ ဖြစ်စဉ်ကိုလည်း{C} {F.PATISANDHI}ကိုလည်း"                # pavattipaṭisandhi (object; M «ဘဝ ဖြစ်စဉ်»)
VIBHAJITVA = new("vibhajitvā", "ခွဲခြမ်းစိတ်ဖြာ၍")


def _p(n, pi=False, case="ကို"):
    """«N pañhā» (+ -pi «…လုံး…လည်း»)"""
    c = F.COUNT[n]
    return f"{K.PANHA} {c}လုံး{case}လည်း" if pi else f"{K.PANHA} {c}{case}"


def _notes():
    sd, cd, cn, N = M.sadisa_name, F.cond, F.cname, F.N
    KAT, VIB, VIT, GAN = K.KATABBA, G.VIBHAJ, K.VITTH, K.GANETABBA
    th, PS, NT = M.EVAM_THUS, F.PATISANDHI, K.NATTHI
    pv = M.NOTE_ADD["pavattipaṭisandhi"]
    S_ = F.TRIADS if False else None
    sa = TRIADS_ADD["sanidassana"]
    mul = {"anidassanasappaṭighamūlak": f"{sa['anidassanasappaṭigh']} {F.DHAMMA}",
           "anidassanaappaṭighamūlak": f"{sa['anidassanaappaṭigh']} {F.DHAMMA}"}
    d = {
        "uppannattike atthisadisaṃ": f"{TIKA_REF['uppannattik']}၌ {sd('atthi')}{F.SADISA}",
        "imesu padesu ekaṃyeva": f"ဤ {F.PADA}တို့၌ {F.COUNT['ekaṃ']}{EVA}",
        "purejātepi āsevanepi paṭisandhi natthi": f"{cd('purejāta', 'loc')}လည်း{C} {cd('āsevana', 'loc')}လည်း {PS} {NT}",
        "anulomasahajātasadisaṃ": f"{K.ORDER_L['anulome']} {N['sahajāta']}{F.SADISA}",
        "ninnānākaraṇaṃ": NINNANAK,
        "nahetusadisā tisso pañhā , moho natthi":
            f"{sd('nahetu')}{SADISA_PL}{C} {K.PANHA} {F.COUNT['tīṇi']}{C} {F.LEX['moho'][0]} {NT}",
        "moho natthi": f"{F.LEX['moho'][0]} {NT}",
        "tayopi paccayā paṭiccavārasadisā": f"{F.PACCAYA} {F.PAA[3]}လုံးလည်း {VARA_N['Paṭiccavāro']}{SADISA_PL}",
        "sahajātavāropi paccayavāropi nissayavāropi saṃsaṭṭhavāropi sampayuttavāropi paṭiccavārasadisā":
            (C + " ").join(VARA_N[v] + "လည်း" for v in ("Sahajātavāro", "Paccayavāro", "Nissayavāro", "Saṃsaṭṭhavāro",
                                                         "Sampayuttavāro")) + f" {VARA_N['Paṭiccavāro']}{SADISA_PL}",
        "sahajātavāropi paccayavāropi nissayavāropi paṭiccavārasadisā , saṃsaṭṭhavāropi sampayuttavāropi arūpeyeva "
        "kātabbā":
            (C + " ").join(VARA_N[v] + "လည်း" for v in ("Sahajātavāro", "Paccayavāro", "Nissayavāro"))
            + f" {VARA_N['Paṭiccavāro']}{SADISA_PL}{C} {VARA_N['Saṃsaṭṭhavāro']}ကိုလည်း{C} "
            f"{VARA_N['Sampayuttavāro']}ကိုလည်း {ARUPA_N}၌သာ {KAT}",
        "pavattipaṭisandhi kātabbā": f"{PAVPAT_A} {KAT}",
        "pavattipaṭisandhipi mahābhūtāpi kātabbā": f"{PAVPAT_A}{C} {M.MAHABHUTA}တို့ကိုလည်း {KAT}",
        "vatthuṃ atirekaṃ": f"{F.VATTHU} " + new("atirekaṃ", "ပိုသည်"),
        "sahajātavāre paripuṇṇā": f"{VARA_N['Sahajātavāro']}၌ {K.PARIPUNNA}ကြသည်",
        "mahābhūtānaṃ khandhānañca pacchā pañcāyatanāni ca vatthu ca kātabbā":
            (f"{M.MAHABHUTA}တို့နှင့် {F.KHANDHA}တို့၏ " + new("pacchā", "နောက်၌") + " "
             + new("pañcāyatanāni", "အာရုံခံ နယ်ပယ် ငါးပါး") + f"ကို{F.LAKAUNG}{C} {F.VATTHU}ကို{F.LAKAUNG} {KAT}"),
        "nissayavāro paccayavārasadiso": f"{VARA_N['Nissayavāro']}သည် {VARA_N['Paccayavāro']}{F.SADISA}",
        "saṃsaṭṭhavāropi sampayuttavāropi vitthāretabbo":
            f"{VARA_N['Saṃsaṭṭhavāro']}ကိုလည်း{C} {VARA_N['Sampayuttavāro']}ကိုလည်း {VIT}",
        "ajjhattasadisaṃyeva": f"{TRIADS_ADD['ajjhatta']['ajjhatt']} {F.DHAMMA}နှင့်{EVA} တူသည်",
        "rūpajīvitindriyampi vitthāretabbaṃ": f"{F.FIXED['Rūpajīvitindriyaṃ'][0]}ကိုလည်း {VIT}",
        "mātikāpadāni anumajjantena vitthāretabbāni": f"{MATIKA_P}တို့ကို {M.ANUMAJJ} {VIT}",
        "mātikāpadāni vitthāretabbāni": f"{MATIKA_P}တို့ကို {VIT}",
        "anulomapadāni gaṇetabbāni": f"အဟုတ်ပြ ပုံစံ၏ {F.PADA}တို့ကို {GAN}",
        "purimā purimā bahiddhāti nānākaraṇaṃ , taṃyeva gamanaṃ":
            (f"{F.QUAL['purimā purimā']} {TRIADS_ADD['ajjhatta']['bahiddh']} {F.DHAMMA}ဟူ၍ {G.NANAKARANA} {K.ATTHI}သည်"
             f"{C} ထို {M.GAMANA}{EVA} ဖြစ်သည်"),
        # 2-17
        "iminā kāraṇena sattapi pañhā vibhajitabbā": f"{IMINA} {_p('satta', True)} {VIB}",
        "iminā kāraṇena satta pañhā vibhajitabbā": f"{IMINA} {_p('satta')} {VIB}",
        "iminā kāraṇena satta pañhā vitthāretabbā asammohantena": f"{IMINA} {_p('satta')} {ASAMM} {VIT}",
        "ghaṭane iminā kāraṇena sattapi pañhā vibhajitabbā": f"{F.GHATANA}၌ {IMINA} {_p('satta', True)} {VIB}",
        "iminā kāraṇena ekavīsa pañhā vibhajitabbā": f"{IMINA} {_p('ekavīsa')} {VIB}",
        "iminā kāraṇena vibhajitabbā ekavīsāpi": f"{IMINA} {F.COUNT['ekavīsa']}လုံးကိုလည်း {VIB}",
        "kammaṃ vibhajitvā nakammeneva ekavīsa pañhā kātabbā":
            f"{N['kamma']}ကို {VIBHAJITVA} {cd('kamma', 'n', True)}ဖြင့်{EVA} {_p('ekavīsa')} {KAT}",
        "paṭisandhipi kaṭattāpi natthi , pañcavokāreyeva kātabbā":
            f"{PS}လည်း{C} {F.KATATTARUPA}လည်း {NT}{C} {PANCAVOK}၌သာ {KAT}",
        "saṃkhittaṃ , sabbe pañhā vibhajitabbā": f"{F.NOTES['(saṃkhittaṃ)'][1:-1]}{C} {K.PANHA} {M.SABBE}ကို {VIB}",
        "saṃkhittaṃ , sattapi pañhā vibhajitabbā": f"{F.NOTES['(saṃkhittaṃ)'][1:-1]}{C} {_p('satta', True)} {VIB}",
        "evaṃ sattapi pañhā vibhajitabbā": f"{th} {_p('satta', True)} {VIB}",
        "nahetusadisaṃ kātabbaṃ": f"{sd('nahetu')}နှင့် တူအောင် {KAT}",
        "paripuṇṇaṃ": f"{K.PARIPUNNA}သည်",
        "paṭiccavārasadisaṃ sādhukaṃ kātabbaṃ":
            f"{VARA_N['Paṭiccavāro']}နှင့် တူအောင် " + new("sādhukaṃ", "ကောင်းစွာ") + f" {KAT}",
        "aññamaññapaccaye paṭiccavāre aññamaññasadisaṃ , nissayapaccaye paṭiccavārasadisaṃ":
            (f"{cd('aññamañña', 'loc')} {VARA_N['Paṭiccavāro']}၌ {N['aññamañña']}{F.SADISA}{C} "
             f"{cd('nissaya', 'loc')} {VARA_N['Paṭiccavāro']}{F.SADISA}"),
        "evaṃ satta pañhā vibhajitabbā , tividharūpasaṅgaho": f"{th} {_p('satta')} {VIB}{C} {TIVIDHA}",
        "evaṃ satta pañhā sahajātā nānākkhaṇikā iminā kāraṇena vibhajitabbā , tividharūpasaṅgaho":
            (f"{th} {_p('satta')} {F.LEX['sahajātā'][0]}{C} {F.LEX['nānākkhaṇikā'][0]}ဟု {IMINA} {VIB}{C} "
             f"{TIVIDHA}"),
        "evaṃ satta pañhā vitthāretabbā , pavattipaṭisandhi": f"{th} {_p('satta')} {VIT}{C} {pv}",
        "evaṃ satta pañhā pavattipaṭisandhi vibhajitabbā , sattasupi kabaḷīkāro āhāro kātabbo":
            (f"{th} {_p('satta')} {pv} {VIB}{C} {F.COUNT['satta']}လုံး၌လည်း "
             f"{F.FIXED['kabaḷīkāro §V§ āhāro'][0]}ကို {KAT}"),
        "evaṃ pavattipaṭisandhi satta pañhā vibhajitabbā , rūpajīvitindriyañca ante ante":
            (f"{th} {pv} {_p('satta')} {VIB}{C} {F.FIXED['Rūpajīvitindriyaṃ'][0]}ကိုလည်း "
             + new("ante ante", "အဆုံးတိုင်း၌")),
        "avasesā pañca pañhā evaṃ vitthāretabbā": f"{AVASESA_A} {_p('pañca')} {th} {VIT}",
        "sahajātā , pacchājātā": f"{N['sahajāta']}{C} {N['pacchājāta']}",
        "avasesā cattāro pañhā vitthāretabbā": f"{AVASESA_A} {_p('cattāri')} {VIT}",
        "paṭiccavāre sahajātapaccayasadisā , ninnānākaraṇā":
            f"{VARA_N['Paṭiccavāro']}၌ {cn('sahajāta')}{SADISA_PL}{C} {NINNANAK}",
        "evaṃ avasesā cha pañhā vibhajitabbā": f"{th} {AVASESA_A} {_p('cha')} {VIB}",
        "sahajātaṃ , pacchājātaṃ , āhāraṃ , indriyampi kātabbā":
            f"{N['sahajāta']}{C} {N['pacchājāta']}{C} {N['āhāra']}{C} {N['indriya']}ကိုလည်း {KAT}",
        "saṃkhittaṃ , asaññasattānañca kātabbā": f"{F.NOTES['(saṃkhittaṃ)'][1:-1]}{C} {ASANNA}တို့ကိုလည်း {KAT}",
        "yāva asaññasattā kātabbā": f"{ASANNA}တို့" + new("yāva X", "အထိ") + f" {KAT}",
        "yāva asaññasattā vitthāretabbā": f"{ASANNA}တို့အထိ {VIT}",
        "avasesā catasso pañhā vibhajitabbā": f"{AVASESA_A} {_p('cattāri')} {VIB}",
        "natthivigatapaccayaṃ anantarasadisaṃ": f"{cn('natthi')}{C} {cn('vigata')}သည် {N['anantara']}{F.SADISA}",
        "avigatapaccayaṃ atthisadisaṃ": f"{cn('avigata')}သည် {N['atthi']}{F.SADISA}",
        "evaṃ sabbo gaṇanavāro gaṇetabbo": f"{th} {F.HEAD['Saṅkhyāvāro']} {M.SABBE}ကို {GAN}",
        "paṭiccavāre nissayapaccayasadisaṃ": f"{VARA_N['Paṭiccavāro']}၌ {cn('nissaya')}{F.SADISA}",
        "paṭhamagamanasadisaṃ": "ပထမ " + M.GAMANA + F.SADISA,
        "idhāpi saṃkhittaṃ": f"{G.YADV['idhāpi']} {F.NOTES['(saṃkhittaṃ)'][1:-1]}",
    }
    for st, my in mul.items():
        d[f"{st}e iminā kāraṇena satta pañhā vibhajitabbā , pariyosānapadā natthi"] = (
            f"{my}{F.MULAKA}၌ {IMINA} {_p('satta')} {VIB}{C} " + new("pariyosānapadā", "အဆုံးသတ် ပုဒ်တို့") + f" {NT}")
        d[f"iminā kāraṇena {st}e satta pañhā vibhajitabbā , niṭṭhānapadā natthi"] = (
            f"{IMINA} {my}{F.MULAKA}၌ {_p('satta')} {VIB}{C} " + new("niṭṭhānapadā", "အပြီးသတ် ပုဒ်တို့") + f" {NT}")
        d[f"{st}ā satta pañhā iminā kāraṇena vibhajitabbā"] = f"{my}{MUL_A} {_p('satta')} {IMINA} {VIB}"
        d[f"{st}e satta pañhā iminā kāraṇena kātabbā"] = f"{my}{F.MULAKA}၌ {_p('satta')} {IMINA} {KAT}"
        d[f"{st}e iminā kāraṇena sattapi pañhā vibhajitabbā"] = f"{my}{F.MULAKA}၌ {IMINA} {_p('satta', True)} {VIB}"
        d[f"{st}ā iminā kāraṇena satta pañhā vibhajitabbā"] = f"{my}{MUL_A} {_p('satta')} {IMINA} {VIB}"
        d[f"{st}ā iminā kāraṇena sattapi pañhā vitthāretabbā"] = f"{my}{MUL_A} {_p('satta', True)} {IMINA} {VIT}"
        d[f"{st}e iminā kāraṇena sattapi pañhā vitthāretabbā"] = f"{my}{F.MULAKA}၌ {IMINA} {_p('satta', True)} {VIT}"
        d[f"{st}eyeva iminā kāraṇena satta pañhā vibhajitabbā"] = f"{my}{F.MULAKA}၌{EVA} {IMINA} {_p('satta')} {VIB}"
        d[f"{st}e sattapi pañhā vibhajitabbā , adhipati tividharūpasaṅgahena"] = (
            f"{my}{F.MULAKA}၌ {_p('satta', True)} {VIB}{C} {N['adhipati']}ကို "
            + TIVIDHA.replace("စုစည်းခြင်း", "စုစည်းခြင်းဖြင့်"))
    return d


def my_clause(t):
    """generic note clauses: «sabbattha N [kātabbā]»"""
    m = re.fullmatch(r"sabbattha (\w+)( kātabbā)?", t)
    if m and m[1] in F.COUNT:
        return f"{K.SABBATTHA} {F.COUNT[m[1]]}" + (f"ကို {K.KATABBA}" if m[2] else "")
    return None


_M_CLAUSE = None


def note_clause(t):
    r = None
    try:
        r = _M_CLAUSE(t)
    except KeyError:
        r = None
    return r if r is not None else my_clause(t)


NOTE_ADD = {}


def setup_notes():
    global _M_CLAUSE
    NOTE_ADD.update(_notes())
    K.NOTE_FIXED.update(NOTE_ADD)
    _M_CLAUSE = K.note_clause
    K.note_clause = note_clause
    at, aj = TRIADS_ADD["atitarammana"], TRIADS_ADD["ajjhatta"]
    NOTEP.update({
        "(vipākaṃ atītārammaṇaṃ ekaṃ khandhaṃ, tissopi pañhā paripuṇṇā. Pavattipaṭisandhi kātabbā)":
            (f"({F.VIPAKA_ADJ} {at['atītārammaṇ']} {F.KHANDHA} {F.PAA[1]}ကို{C} {_p('tīṇi', True, '')} "
             f"{K.PARIPUNNA}ကြသည်{END} {NOTE_ADD['pavattipaṭisandhi kātabbā']})"),
        "(bahiddhā ninnānākaraṇaṃ, mātikāpadāni vitthāretabbāni)":
            f"({aj['bahiddh']} {F.DHAMMA}၌ {NINNANAK}{C} {NOTE_ADD['mātikāpadāni vitthāretabbāni']})",
        "(purimā purimā bahiddhāti nānākaraṇaṃ, taṃyeva gamanaṃ)":
            f"({NOTE_ADD['purimā purimā bahiddhāti nānākaraṇaṃ , taṃyeva gamanaṃ']})",
        "(avipākaṃ-4)": f"({K.sa_x('vipāka', True)}-4)",
        "(savipākaṃ-5)": f"({K.sa_x('vipāka')}-5)",
    })
    for i, (a, b) in enumerate(NOTEP.items()):
        F.NOTES[f"(⁑q{i})"] = b
        FG.NOTES[f"(⁑q{i})"] = b
    F.HLINES["*2-6. Sahajāta-paccaya-nissaya-saṃsaṭṭha-sampayuttavāro*"] = \
        G.HLINES["*2-6 Sahajāta-paccaya-nissaya-saṃsaṭṭha-sampayuttavāro*"].replace("*2-6 ", "*2-6. ")
    F.HLINES["*4-6. Nissaya-saṃsaṭṭha-sampayuttavāro*"] = (
        "*4-6. " + new("Nissaya-saṃsaṭṭha-sampayuttavāro", "အမှီပြု၍ ဖြစ်ပေါ်ခြင်း၊ ရောနှောခြင်းနှင့် ယှဉ်တွဲခြင်းအလိုက် ဖော်ပြချက်") + "*")


TERM_REF = {}       # per chapter: a term named inside a note


def chapter_notes(name):
    """as make_ch2-03-06.chapter_notes: every note of the chapter registered for the chains (F.NOTES)"""
    M.TERM_REF.clear()
    M.TERM_REF.update(TERM_REF.get(name, {}))
    src = prep((PALI / name).read_text(encoding="utf-8-sig"))
    src = re.sub(r"\{[^{}]*\}", "", src)
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


# ===================================================================================== chains: a run of conditions
# that the «…» cuts («… naaññamaññe naupanissaye…pe… nasampayutte … novigate ekaṃ»): the run at the end of a
# fragment is rendered as make_ch2-03-06's runs (each condition in the locative, joined by «၊»)
_M_CHAIN = None


def chain(s, slots, ci, ki, di, vi=None):
    try:
        return _M_CHAIN(s, slots, ci, ki, di, vi)
    except KeyError:
        pass
    loc = r"(?:(?:[Nn]a|[Nn]o)?(?:" + F._LOC_ALT + r"))"
    m = re.search(r"(?<![\wāīūṃṅñṭḍṇḷ§])((?:" + loc + r" )*" + loc + r")\s*$", s)
    if not m:
        raise KeyError("chain: " + s)
    tok = "\u0004E\u0004"
    F.NOTES[tok] = M._run_tok(m)
    try:
        return _M_CHAIN(s[:m.start()] + tok, slots, ci, ki, di, vi)
    finally:
        F.NOTES.pop(tok, None)


# ===================================================================================== lexicon wrapper
_M_LEX = None


def lex(frag, slots, ti, ci, ki, di, vi):
    try:
        return _M_LEX(frag, slots, ti, ci, ki, di, vi)
    except KeyError as e:
        if "post word first" not in str(e) or frag.strip() not in ("patthayamāno",):
            raise
    lead = frag[:len(frag) - len(frag.lstrip())]
    return lead + PATTHAY                      # «…patthayamāno…» (the object cut off by «…»)


# ===================================================================================== engine: term-strip fallback
# A unit that no frame takes because a triad term stands before a noun that is not «dhamma» («anidassanasappaṭighe
# mahābhūte paṭicca sanidassanasappaṭighaṃ cittasamuṭṭhānaṃ rūpaṃ …»): the unit is translated without those terms
# (the frames know the bare sentence), and each term is put back right before the Burmese of the word it stood before
# (stacked terms «Xañca Yañca N» joined by «၊», as 1-01's stacked qualifiers; a «-ñca» after a noun list moves to the
# noun: «tayo khandhā Xañca cittasamuṭṭhānaṃ rūpaṃ» = «tayo khandhā cittasamuṭṭhānañca rūpaṃ» + X).
_NUMW = r"(?:ekaṃ|eko|ekassa|dve|dvinnaṃ|tayo|tiṇṇannaṃ|tiṇṇaṃ|cattāro|catunnaṃ)"
HEADS = [(r"mahābhūt", "မူလဓာတ်ကြီး"), (r"khandh", F.KHANDHA), (r"cittasamuṭṭhān", "စိတ်မှ ဖြစ်ပေါ်လာသော"),
         (r"kaṭattā", "ကံ ပြုခဲ့သောကြောင့်"), (r"upādārūp", "မူလဓာတ်ကြီးတို့ကို မှီ၍ ဖြစ်သော"),
         (r"hetū?$", "အမြစ်"), (r"adhipati$", "အကြီးအမှူး"), (r"cetanā$", "စေ့ဆော်မှု"), (r"āhārā?$", "အာဟာရ"),
         (r"indriyā$", "စွမ်းရည်"), (r"kāy(?:assa|o|aṃ)$", "ကိုယ်"), (r"kabaḷīkār", "လုတ်ပြု၍"),
         (r"āpodhātu", "ရေဓာတ်"), (r"vatthu", "မှီရာ"), (r"rāgo$", "ရာဂ"),
         (r"rūpāyatan", "အဆင်းအရောင် အာရုံခံ"), (r"cakkhāyatan", "မျက်စိ အာရုံခံ"),
         (r"phoṭṭhabbāyatan", "အထိအတွေ့ အာရုံခံ"), (r"kāyāyatan", "ကိုယ် အာရုံခံ"),
         (r"cakkhuviññāṇ", "မျက်စိ သိစိတ်"), (r"kāyaviññāṇ", "ကိုယ် သိစိတ်"), (r"cakkhu$", "မျက်စိ"),
         (r"cittasamaṅgissa$", "စိတ်နှင့်")]
_ÑCA = {"kaṭattārūpaṃ": "kaṭattā ca rūpaṃ", "kaṭattārūpānaṃ": "kaṭattā ca rūpānaṃ"}
VIA_STRIP = collections.Counter()


def _head(word):
    for rx, my in HEADS:
        if re.match(rx, word):
            return my
    raise KeyError("strip head: " + word)


def term_strip(u):
    ms = [m for m in F.TERM_RE.finditer(u) if not re.match(r"\s+dhamm", u[m.end():])]
    if not ms:
        return None
    toks, pos, groups = [], 0, []          # groups: [values, next word, «ñca» moved]
    i = 0
    while i < len(ms):
        grp = [ms[i]]
        while i + 1 < len(ms) and u[grp[-1].end():ms[i + 1].start()] == " ":
            i += 1
            grp.append(ms[i])
        toks.append(u[pos:grp[0].start()])
        pos = grp[-1].end()
        rest = u[pos:].lstrip(" ")
        pos = len(u) - len(rest)
        w = re.match(r"[^\s.,…;()]+", rest)
        if not w:
            raise KeyError("strip: no word after a term")
        word = w[0]
        prev = toks[-1].rstrip().split(" ")[-1] if toks[-1].strip() else ""
        nca = grp[-1][0].endswith("ñca") and re.match(r"(khandh|mahābhūt)", prev) is not None
        if nca and not word.endswith("ñca"):
            neww = _ÑCA.get(word) or (word[:-1] + "ñca" if word.endswith("ṃ") else None)
            if neww is None:
                raise KeyError("strip ñca: " + word)
            toks.append(neww)
            pos += len(word)
        nw = word
        if re.fullmatch(_NUMW, word):                       # «X ekaṃ mahābhūtaṃ»: the noun after the number
            m2 = re.match(r"\S+ ([^\s.,…;()]+)", rest)
            if not m2:
                raise KeyError("strip: a number without its noun")
            nw = m2[1]
        groups.append(([F.term_value(m) for m in grp], nw))
        i += 1
    toks.append(u[pos:])
    stripped = "".join(toks)
    out = _M_UNIT(stripped)
    cur = 0
    for vals, nw in groups:
        head = _head(nw)
        k = out.find(head, cur)
        if k < 0:
            raise KeyError(f"strip: «{head}» not found after {cur} in «{out}»")
        ins = (C + " ").join(vals) + " "
        if k and out[k - 1] != " ":
            ins = " " + ins
        out = out[:k] + ins + out[k:]
        cur = k + len(ins) + len(head)
    VIA_STRIP[u.strip()] += 1
    return out


_M_UNIT = None


def unit_my(u):
    m = re.fullmatch(r"(\s*)(.*?) (\(⁑q\d+\))(\.?)", u)
    if m and re.search(r"(?:nti|īti) \w+$", m[2]):          # a ghaṭanā line with a note after its count
        return m[1] + _M_UNIT(m[2]) + " " + F.NOTES[m[3]] + F.punct(m[4])
    try:
        return _M_UNIT(u)
    except M.ERRS as e1:
        try:
            r = term_strip(u)
        except M.ERRS as e2:
            r = None
            e1 = F.Miss(f"{e1} || strip: {str(e2)[:300]}")
        if r is None:
            raise F.Miss(str(e1))
        return r


def setup():
    global _M_CHAIN, _M_LEX, _M_UNIT
    setup_numbers(F)
    setup_numbers(FG)
    setup_names()
    setup_lex()
    setup_notes()
    _M_CHAIN = F.chain
    F.chain = chain
    _M_LEX = F.lex
    F.lex = lex
    _M_UNIT = F.unit_my
    F.unit_my = unit_my


setup()


# ===================================================================================== run
class Counting(dict):
    cnt = collections.Counter()

    def setdefault(self, k, v):
        self.cnt[k] += 1
        return super().setdefault(k, v)


def translate(name):
    tri = CH_TRIAD.get(name)
    if name in M.CH_TRIAD:
        M.chapter_notes(name)
    set_triad(F, tri)
    if tri:
        chapter_notes(name)
    set_triad(FG, tri)
    if name in M.CH_TRIAD:
        M.set_triad(F, M.CH_TRIAD[name])
        M.set_triad(FG, M.CH_TRIAD[name])
    FG.translate("")                   # (re)builds the fallback's frame regexes
    src = (PALI / name).read_text(encoding="utf-8-sig")
    return F.translate(prep(src))


def regress():
    bad = 0
    for n in ["1-00-paccaya.md", "1-02-vedanattika.md"] + M.NAMES:
        txt = translate(n)
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
    if F.DEV:
        rows = sorted(F.UNSEEN.items(), key=lambda kv: -F.UNSEEN.cnt[kv[0]])
        CHK.mkdir(exist_ok=True)
        with open(CHK / "dev.txt", "w", encoding="utf-8") as fh:
            for k, v in rows:
                fh.write(f"[{F.UNSEEN.cnt[k]}] SK: {k}\n    {v}\n")
        (CHK / "dev-out.md").write_text(txt, encoding="utf-8")
        with open(CHK / "via-g.txt", "w", encoding="utf-8") as fh:
            for k, v in M.VIA_G.most_common():
                fh.write(f"[{v}] {k}\n")
        print(len(rows), "unmatched skeletons,", sum(F.UNSEEN.cnt.values()), "occurrences")
    if F.SLIPS and "--slips" in sys.argv:
        print("slips:", *sorted(F.SLIPS), sep="\n  ")


if __name__ == "__main__":
    main()
