"""Burmese zero-shot of pi-7 3-07 nīvaraṇagocchaka, 3-08 parāmāsagocchaka and 3-10 upādānagocchaka (dyad chapters of
the Dukapaṭṭhāna, «အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ»), from the Pāli only.

usage: python3 -I -X utf8 make_ch3-07-08-10.py [chapter ...] [--dev] [--regress] [--slips] [--out DIR]
  (no flag)  translate the chapters and write them; stops on the first unmatched sentence (nothing is guessed).
  --dev      do not stop: list every unmatched skeleton with its count in chk-ch3-07-08-10/dev.txt (nothing written).
  --regress  regenerate 3-01 … 3-02 (and through it the sample and 2-03 … 2-06) in memory and compare them with the
             published files (they must be identical).

Engine (read-only, imported, never run as a script): make_ch3-01-02.py is IMPORTED (it imports make_ch2-03-06.py in
the same way: PRIMARY my7_formulas + make_sample + make_ch1-01, FALLBACK per unit make_ch1-03-05). Its dyad machinery
(cut at the dyad headings, one dyad active per part, pseudo a-stem terms, both-members slots, notes, lexicon) is reused
as it is; this script adds the nīvaraṇa / parāmāsa / upādāna dyads (pi-1 final Mātikā ^1-M2-44 … ^1-M2-49, ^1-M2-50 …
^1-M2-54, ^1-M2-69 … ^1-M2-74), their names, nouns, notes and unique sentences. No main block of another script runs; no
file of the sample or of another group is edited. Every new string is logged in notes-ch3-07-08-10.md.
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
NAMES = ["3-07-nivaranagocchaka.md", "3-08-paramasagocchaka.md", "3-10-upadanagocchaka.md"]
CHK = HERE / "chk-ch3-07-08-10"
WCH = r"[\wāīūṃṅñṭḍṇḷ]"
_NB = r"(?!" + WCH + ")"
_PB = r"(?<!" + WCH + ")"


def _load(name, fn):
    spec = importlib.util.spec_from_file_location(name, HERE / fn)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


D = _load("ch30102", "make_ch3-01-02.py")          # its setup() runs on import; its main() does not
M = D.M
F, FG, G, K, S = D.F, D.FG, D.G, D.K, D.S
C, END, PE, W = F.C, F.END, F.PE, F.W

NEW = collections.OrderedDict()     # every new string of this script: Pāli -> Burmese


def new(pali, my):
    NEW.setdefault(pali, my)
    return my


# ===================================================================================== the dyads (pi-1 final)
_dw = D._dw
DUKA = F.DUKA
# the three gocchakas: the noun (pi-1 final ^1-M2-44 / 50 / 69), the Pāli stems of the six dyads
NIV = W("nīvaraṇā dhammā", "အတားအဆီး", "1", "^1-M2-44")
PAR = W("parāmāsā dhammā", "မှားယွင်းသော ယူဆမှု", "1", "^1-M2-50")
UPA = W("upādānā dhammā", "စွဲလမ်းမှု", "1", "^1-M2-69")

DYADS_ADD = {
    # nīvaraṇa (^1-M2-44 … ^1-M2-49)
    "niv1": {"nīvaraṇdk": _dw("nīvaraṇā dhammā", "အတားအဆီး ဖြစ်သော", "^1-M2-44"),
             "nonīvaraṇ": _dw("no nīvaraṇā dhammā", "အတားအဆီး မဟုတ်သော", "^1-M2-44")},
    "niv2": {"nīvaraṇiy": _dw("nīvaraṇiyā dhammā", "အတားအဆီး၏ အာရုံ ဖြစ်နိုင်သော", "^1-M2-45"),
             "anīvaraṇiy": _dw("anīvaraṇiyā dhammā", "အတားအဆီး၏ အာရုံ မဖြစ်နိုင်သော", "^1-M2-45")},
    "niv3": {"nīvaraṇasampayutt": _dw("nīvaraṇasampayuttā dhammā", "အတားအဆီးနှင့် ယှဉ်တွဲသော", "^1-M2-46"),
             "nīvaraṇavippayutt": _dw("nīvaraṇavippayuttā dhammā", "အတားအဆီးနှင့် ကင်းကွာသော", "^1-M2-46")},
    "niv4": {"nīvaraṇanīvaraṇiydk": _dw("nīvaraṇā ceva dhammā nīvaraṇiyā ca",
                                        "အတားအဆီးလည်း ဖြစ်၊ အတားအဆီး၏ အာရုံလည်း ဖြစ်နိုင်သော", "^1-M2-47"),
             "nīvaraṇiyanonīvaraṇdk": _dw("nīvaraṇiyā ceva dhammā no ca nīvaraṇā",
                                          "အတားအဆီး၏ အာရုံ ဖြစ်နိုင်သော်လည်း အတားအဆီး မဟုတ်သော", "^1-M2-47")},
    "niv5": {"nīvaraṇanīvaraṇasampdk": _dw("nīvaraṇā ceva dhammā nīvaraṇasampayuttā ca",
                                           "အတားအဆီးလည်း ဖြစ်၊ အတားအဆီးနှင့်လည်း ယှဉ်တွဲသော", "^1-M2-48"),
             "nīvaraṇasampnonīvaraṇdk": _dw("nīvaraṇasampayuttā ceva dhammā no ca nīvaraṇā",
                                            "အတားအဆီးနှင့် ယှဉ်တွဲသော်လည်း အတားအဆီး မဟုတ်သော", "^1-M2-48")},
    # ^1-M2-49 is not attributive in pi-1 («… ကင်းကွာသော သဘောတရားများအနက် … ဖြစ်နိုင်သည်တို့လည်း»): the two terms
    # are built in the pattern of 3-01's «nahetu sahetuko / ahetuko» (NEW)
    "niv6": {"nīvaraṇavippnīvaraṇiy": new("nīvaraṇavippayutto nīvaraṇiyo (dyad term)",
                                          "အတားအဆီးနှင့် ကင်းကွာသော်လည်း အတားအဆီး၏ အာရုံ ဖြစ်နိုင်သော"),
             "nīvaraṇavippanīvaraṇiy": new("nīvaraṇavippayutto anīvaraṇiyo (dyad term)",
                                           "အတားအဆီးနှင့် ကင်းကွာ၊ အတားအဆီး၏ အာရုံ မဖြစ်နိုင်သော")},
    # parāmāsa (^1-M2-50 … ^1-M2-54; five dyads)
    "par1": {"parāmāsdk": _dw("parāmāsā dhammā", "မှားယွင်းသော ယူဆမှု ဖြစ်သော", "^1-M2-50"),
             "noparāmās": _dw("no parāmāsā dhammā", "မှားယွင်းသော ယူဆမှု မဟုတ်သော", "^1-M2-50")},
    "par2": {"parāmaṭṭh": _dw("parāmaṭṭhā dhammā", "မှားယွင်းသော ယူဆမှု၏ အာရုံ ဖြစ်နိုင်သော", "^1-M2-51"),
             "aparāmaṭṭh": _dw("aparāmaṭṭhā dhammā", "မှားယွင်းသော ယူဆမှု၏ အာရုံ မဖြစ်နိုင်သော", "^1-M2-51")},
    "par3": {"parāmāsasampayutt": _dw("parāmāsasampayuttā dhammā", "မှားယွင်းသော ယူဆမှုနှင့် ယှဉ်တွဲသော", "^1-M2-52"),
             "parāmāsavippayutt": _dw("parāmāsavippayuttā dhammā", "မှားယွင်းသော ယူဆမှုနှင့် ကင်းကွာသော",
                                      "^1-M2-52")},
    "par4": {"parāmāsaparāmaṭṭhdk": _dw("parāmāsā ceva dhammā parāmaṭṭhā ca",
                                        "မှားယွင်းသော ယူဆမှုလည်း ဖြစ်၊ မှားယွင်းသော ယူဆမှု၏ အာရုံလည်း ဖြစ်နိုင်သော",
                                        "^1-M2-53"),
             "parāmaṭṭhanoparāmāsdk": _dw("parāmaṭṭhā ceva dhammā no ca parāmāsā",
                                          "မှားယွင်းသော ယူဆမှု၏ အာရုံ ဖြစ်နိုင်သော်လည်း မှားယွင်းသော ယူဆမှု မဟုတ်သော",
                                          "^1-M2-53")},
    "par6": {"parāmāsavippparāmaṭṭh": new("parāmāsavippayutto parāmaṭṭho (dyad term)",
                                          "မှားယွင်းသော ယူဆမှုနှင့် ကင်းကွာသော်လည်း မှားယွင်းသော ယူဆမှု၏ အာရုံ ဖြစ်နိုင်သော"),
             "parāmāsavippaparāmaṭṭh": new("parāmāsavippayutto aparāmaṭṭho (dyad term)",
                                           "မှားယွင်းသော ယူဆမှုနှင့် ကင်းကွာ၊ မှားယွင်းသော ယူဆမှု၏ အာရုံ မဖြစ်နိုင်သော")},
    # upādāna (^1-M2-69 … ^1-M2-74)
    "upa1": {"upādāndk": _dw("upādānā dhammā", "စွဲလမ်းမှု ဖြစ်သော", "^1-M2-69"),
             "noupādān": _dw("no upādānā dhammā", "စွဲလမ်းမှု မဟုတ်သော", "^1-M2-69")},
    "upa2": {"upādāniy": _dw("upādāniyā dhammā", "စွဲလမ်းမှု၏ အာရုံ ဖြစ်နိုင်သော", "^1-M2-70"),
             "anupādāniy": _dw("anupādāniyā dhammā", "စွဲလမ်းမှု၏ အာရုံ မဖြစ်နိုင်သော", "^1-M2-70")},
    "upa3": {"upādānasampayutt": _dw("upādānasampayuttā dhammā", "စွဲလမ်းမှုနှင့် ယှဉ်တွဲသော", "^1-M2-71"),
             "upādānavippayutt": _dw("upādānavippayuttā dhammā", "စွဲလမ်းမှုနှင့် ကင်းကွာသော", "^1-M2-71")},
    "upa4": {"upādānaupādāniydk": _dw("upādānā ceva dhammā upādāniyā ca",
                                      "စွဲလမ်းမှုလည်း ဖြစ်၊ စွဲလမ်းမှု၏ အာရုံလည်း ဖြစ်နိုင်သော", "^1-M2-72"),
             "upādāniyanoupādāndk": _dw("upādāniyā ceva dhammā no ca upādānā",
                                        "စွဲလမ်းမှု၏ အာရုံ ဖြစ်နိုင်သော်လည်း စွဲလမ်းမှု မဟုတ်သော", "^1-M2-72")},
    "upa5": {"upādānaupādānasampdk": _dw("upādānā ceva dhammā upādānasampayuttā ca",
                                         "စွဲလမ်းမှုလည်း ဖြစ်၊ စွဲလမ်းမှုနှင့်လည်း ယှဉ်တွဲသော", "^1-M2-73"),
             "upādānasampnoupādāndk": _dw("upādānasampayuttā ceva dhammā no ca upādānā",
                                          "စွဲလမ်းမှုနှင့် ယှဉ်တွဲသော်လည်း စွဲလမ်းမှု မဟုတ်သော", "^1-M2-73")},
    "upa6": {"upādānavippupādāniy": new("upādānavippayutto upādāniyo (dyad term)",
                                        "စွဲလမ်းမှုနှင့် ကင်းကွာသော်လည်း စွဲလမ်းမှု၏ အာရုံ ဖြစ်နိုင်သော"),
             "upādānavippanupādāniy": new("upādānavippayutto anupādāniyo (dyad term)",
                                          "စွဲလမ်းမှုနှင့် ကင်းကွာ၊ စွဲလမ်းမှု၏ အာရုံ မဖြစ်နိုင်သော")},
}
for _d, _tab in DYADS_ADD.items():
    _a, _b = list(_tab)
    _tab[_a + "_" + _b + "_both"] = f"{_tab[_a]}{C} {_tab[_b]}"
D.DYADS.update(DYADS_ADD)

# dyad heading (level 6) -> dyad
DYAD_OF_ADD = {
    "Nīvaraṇadukaṃ": "niv1", "Nīvaraṇiyadukaṃ": "niv2", "Nīvaraṇasampayuttadukaṃ": "niv3",
    "Nīvaraṇanīvaraṇiyadukaṃ": "niv4", "Nīvaraṇanīvaraṇasampayuttadukaṃ": "niv5",
    "Nīvaraṇavippayuttanīvaraṇiyadukaṃ": "niv6",
    "Parāmāsadukaṃ": "par1", "Parāmaṭṭhadukaṃ": "par2", "Parāmāsasampayuttadukaṃ": "par3",
    "Parāmāsaparāmaṭṭhadukaṃ": "par4", "Parāmāsavippayuttaparāmaṭṭhadukaṃ": "par6",
    "Upādānadukaṃ": "upa1", "Upādāniyadukaṃ": "upa2", "Upādānasampayuttadukaṃ": "upa3",
    "Upādānaupādāniyadukaṃ": "upa4", "Upādānaupādānasampayuttadukaṃ": "upa5",
    "Upādānavippayuttaupādāniyadukaṃ": "upa6",
}
D.DYAD_OF.update(DYAD_OF_ADD)

# ===================================================================================== names and headings
GOCCHAKA = {"Nīvaraṇagocchakaṃ": W("Nīvaraṇagocchakaṃ", "အတားအဆီးတို့၏ အစု", "1", "^1-M-2-8-0"),
            "Parāmāsagocchakaṃ": W("Parāmāsagocchakaṃ", "မှားယွင်းသော ယူဆမှုတို့၏ အစု", "1", "^1-M-2-9-0"),
            "Upādānagocchakaṃ": W("Upādānagocchakaṃ", "စွဲလမ်းမှုတို့၏ အစု", "1", "^1-M-2-11-0")}
_AR = "၏ အာရုံ ဖြစ်နိုင်ခြင်း"
# the dyad names (NEW; the pattern of 3-01 … 3-02: «X နှစ်မျိုးတွဲ», «X ရှိခြင်း …», «Xနှင့် ယှဉ်တွဲခြင်း …»,
# «X ဖြစ်ခြင်းနှင့် Y …», «X မဟုတ်ခြင်းနှင့် Y …»)
DUKA_NAME = {}
for _p, _pi, _my in (("Nīvaraṇ", "Nīvaraṇiy", NIV), ("Parāmās", "Parāmaṭṭh", PAR), ("Upādān", "Upādāniy", UPA)):
    _lo = _p.lower()
    DUKA_NAME[f"{_p}adukaṃ"] = f"{_my} {DUKA}"
    DUKA_NAME[f"{_pi}adukaṃ"] = f"{_my}{_AR} {DUKA}"
    DUKA_NAME[f"{_p}asampayuttadukaṃ"] = f"{_my}နှင့် ယှဉ်တွဲခြင်း {DUKA}"
    DUKA_NAME[f"{_p}a{_pi.lower()}adukaṃ".replace("aupādān", "aupādān")] = f"{_my} ဖြစ်ခြင်းနှင့် {_my}{_AR} {DUKA}"
    if _p != "Parāmās":
        DUKA_NAME[f"{_p}a{_lo}asampayuttadukaṃ"] = f"{_my} ဖြစ်ခြင်းနှင့် {_my}နှင့် ယှဉ်တွဲခြင်း {DUKA}"
    DUKA_NAME[f"{_p}avippayutta{_pi.lower()}adukaṃ"] = f"{_my}နှင့် ကင်းကွာခြင်းနှင့် {_my}{_AR} {DUKA}"
assert set(DUKA_NAME) == set(DYAD_OF_ADD), set(DUKA_NAME) ^ set(DYAD_OF_ADD)
for _k, _v in DUKA_NAME.items():
    new(_k, _v)
HL_ADD = {}
HL_ADD.update(GOCCHAKA)
HL_ADD.update(DUKA_NAME)
for _k, _v in list(DUKA_NAME.items()) + list(GOCCHAKA.items()):
    HL_ADD[f"{_k} niṭṭhitaṃ."] = F.finished(_v)


HL_ADD["*1-4. Paccayacatukkaṃ*"] = G.HLINES["*1-4. Paccayacatukkaṃ*"]          # = 1-03 … 1-05
HL_ADD["1-4. Paccayānulomādi"] = F.HLINES["*1-4. Paccayānulomādi*"][1:-1]       # = 2-03 … 2-06 (no asterisks)
HL_ADD["1-7. Paṭiccavārādi"] = new("1-7. Paṭiccavārādi", f"1-7. {F.HEAD['Paṭiccavāro']} {F.ADI}")
# the summary verse of 3-07 (Nīvaraṇiyaduka; unique lines, NEW; paṭigha «မုန်းတီးမှု» pi-1 termbase)
_PATIGHA = W("paṭighasampayuttaṃ", "မုန်းတီးမှုနှင့် ယှဉ်တွဲသော", "1").split("နှင့်")[0]
HL_ADD["Dvikkhattuṃ kāmacchandena, catukkhattuṃ paṭighena ca;"] = new(
    "Dvikkhattuṃ kāmacchandena, catukkhattuṃ paṭighena ca;",
    f"ကာမကို လိုလားမှုဖြင့် နှစ်ကြိမ်{C} {_PATIGHA}ဖြင့်လည်း လေးကြိမ်{C}")
HL_ADD["Uddhaccaṃ vicikicchā ca, ubhopete sakiṃ sakiṃ;"] = new(
    "Uddhaccaṃ vicikicchā ca, ubhopete sakiṃ sakiṃ;",
    f"{F.LEX['uddhaccaṃ'][0]}နှင့် {F.LEX['vicikicchā'][0]}{C} ထိုနှစ်ပါးလုံး တစ်ကြိမ်စီ{C}")
HL_ADD["Nīvaraṇānaṃ nīvaraṇehi, aṭṭhavidhaṃ payojanaṃ."] = new(
    "Nīvaraṇānaṃ nīvaraṇehi, aṭṭhavidhaṃ payojanaṃ.",
    f"{NIV}တို့၏ {NIV}တို့နှင့် ယှဉ်စပ်ခြင်း{C} ရှစ်မျိုး ရှိသည်{END}")
HL_ADD["Tatiyo bhāgo niṭṭhito."] = new("Tatiyo bhāgo niṭṭhito.", f"တတိယ အပိုင်း {F.DONE}{END}")   # = 2-17 «Dutiyo …»
HL_ADD["*Pacchājātāsevanapaccayā*"] = F.heading("*Pacchājāta-āsevanapaccayā*")  # the «X-Ypaccayā» heading


def setup_names():
    F.HLINES.update(HL_ADD)
    K.KIND["pacchājāto"] = K.KIND["pacchājātā"]          # «Pacchājāto –» (masculine: parāmāso) = «Pacchājātā –»
    for k, v in DUKA_NAME.items():              # a dyad named inside a note («yathā nīvaraṇadukaṃ»)
        K.WORDS_N.setdefault(k[0].lower() + k[1:], v)


# ===================================================================================== Pāli preparation (in memory)
_AE = r"(o|aṃ|assa|ā|ānaṃ|ānañca|añca|e|ena|āni|ādhipati|acittasamaṅgissa)"
_A_OF = {"o": "o", "a": "aṃ", "aṃ": "aṃ", "assa": "assa", "ā": "ā", "āna": "ānaṃ", "ānaṃ": "ānaṃ", "e": "e",
        "añca": "añca", "ādhipati": "ādhipati"}
# per gocchaka: (noun stem X, term-2 stem Y, negative of term 2)
GOC = {"niv": ("nīvaraṇ", "nīvaraṇiy", "anīvaraṇiy"), "par": ("parāmās", "parāmaṭṭh", "aparāmaṭṭh"),
       "upa": ("upādān", "upādāniy", "anupādāniy")}


def _ci(s):
    return f"[{s[0].upper()}{s[0]}]" + re.escape(s[1:])


# readings for the parser (in memory; logged): a «ca» placed once for a whole list, or one compound read as two
# words; the Burmese is the module's list rendering «…လည်းကောင်း၊ …လည်းကောင်း» of the same members
READ = {
    "eko khandho ca kāmacchandanīvaraṇañca tiṇṇannaṃ khandhānaṃ thinamiddhanīvaraṇassa uddhaccanīvaraṇassa "
    "avijjānīvaraṇassa ca cittasamuṭṭhānānañca rūpānaṃ":
        "eko khandho ca kāmacchandanīvaraṇaṃ ca tiṇṇannaṃ khandhānaṃ ca thinamiddhanīvaraṇassa uddhaccanīvaraṇassa "
        "avijjānīvaraṇassa ca cittasamuṭṭhānānaṃ rūpānaṃ ca",
    "eko khandho ca diṭṭhupādānañca tiṇṇannaṃ khandhānaṃ kāmupādānassa ca cittasamuṭṭhānānaṃ rūpānaṃ":
        "eko khandho ca diṭṭhupādānaṃ ca tiṇṇannaṃ khandhānaṃ ca kāmupādānassa ca cittasamuṭṭhānānaṃ rūpānaṃ ca",
    "tayo khandhā kāmupādānañca cittasamuṭṭhānaṃ rūpaṃ": "tayo khandhā kāmupādānañca cittasamuṭṭhānañca rūpaṃ",
    "khandhānaṃ upādānānañca cittasamuṭṭhānānaṃ rūpānaṃ": "khandhānaṃ upādānānañca cittasamuṭṭhānānañca rūpānaṃ",
    "ahetukaparāmāsavippayuttā khandhā": "ahetukā parāmāsavippayuttā khandhā",
}
SLIP_ADD = {"parāmāsampayuttakānaṃ": "parāmāsasampayuttakānaṃ"}
READ_LOG = set()


def prep_mine(t, d):
    for a, b in READ.items():
        if a in t:
            READ_LOG.add(f"«{a}» parsed as «{b}»")
            t = t.replace(a, b)
    t = _CA_LOBHA.sub(" ca ", t)
    g, n = d[:3], d[3:]
    x, y, ny = GOC[g]
    X, Y = _ci(x), _ci(y)
    if n == "1":
        # X as a term: before a dhamma word (or coordinated with noX before one), before «hetū / hetu» (the roots
        # that are hindrances …) and in «X-ādhipati»; otherwise X is the noun («nīvaraṇe paṭicca …»)
        t = re.sub(_PB + "(" + X + r")(o|aṃ|assa|ā|ānaṃ|añca|e)(?= (?:ca )?(?:[Nn]o" + re.escape(x) + r"\w*(?: ca)? )?"
                   r"(?:dhamm|hetū?" + _NB + "))", lambda m: m[1] + "dk" + m[2], t)
        t = re.sub(_PB + "(" + X + r")ādhipati" + _NB, r"\1dkādhipati", t)
    elif n == "4":
        t = re.sub(_PB + "(" + X + r")\w*?(?:ñceva| ceva) " + re.escape(y) + r"(o|a|assa|ā|āna|e)(?:ñca| ca)" + _NB,
                   lambda m: m[1] + "a" + y + "dk" + _A_OF[m[2]], t)
        t = re.sub(_PB + "(" + Y + r")(o|a|aṃ|assa|ā|āna|e)(?:ñceva| ceva) no ca " + re.escape(x) +
                   r"(añca|ādhipati|o|aṃ|assa|ā|ānaṃ|e)" + _NB, lambda m: m[1] + "ano" + x + "dk" + _A_OF[m[3]], t)
        t = D._pairfix(t, x + "a" + y + "dk", y + "ano" + x + "dk")
    elif n == "5":
        s = x + "asampayutt"
        t = re.sub(_PB + "(" + X + r")\w*?(?:ñceva| ceva) " + re.escape(s) + r"(o|a|assa|ā|āna|e)(?:ñca| ca)" + _NB,
                   lambda m: m[1] + "a" + x + "asampdk" + _A_OF[m[2]], t)
        t = re.sub(_PB + "(" + _ci(s) + r")(o|a|aṃ|assa|ā|āna|akāna|e)(?:ñceva| ceva) no ca " + re.escape(x) +
                   r"(añca|ādhipati|o|aṃ|assa|ā|ānaṃ|e)" + _NB, lambda m: m[1][:-5] + "no" + x + "dk" + _A_OF[m[3]], t)
        t = D._pairfix(t, x + "a" + x + "asampdk", x + "asampno" + x + "dk")
    elif n == "6":
        # «X-vippayuttaṃ Y-aṃ» / «X-vippayuttaṃ aY-aṃ» glued to one word «X-vippY-aṃ» / «X-vippaY-aṃ» (the ending of
        # the second word gives the slot tail)
        t = re.sub(_PB + "(" + _ci(x + "avipp") + r")ayutt(?:o|aṃ|assa|ā|ānaṃ|añca|e) (" + re.escape(ny) + "|"
                   + re.escape(y) + ")(?=" + WCH + ")", r"\1\2", t)
    return D._PREP_DYAD(t, d)


MY_END = D._END.replace("|ānañca|", "|ānañca|akānaṃ|akā|ake|")
assert MY_END != D._END


def _set_dyad(mod, d):
    D._SET_DYAD(mod, d)
    if d and d[:3] in GOC:
        mod.TRIAD_END[d] = MY_END
        mod.rebuild()


def _prep_dyad(t, d):
    if d and d[:3] in GOC:
        return prep_mine(t, d)
    return D._PREP_DYAD(t, d)


# ===================================================================================== nouns and lexicon
# the gocchaka nouns (pi-1 ^1-M2-44 / 50 / 69) in their case forms; the single hindrances and clingings (pi-1 final
# ^1-1158 / ^1-1164 / ^1-1503 / ^1-1219)
NOUN_FORMS = {NIV: "nīvaraṇ", PAR: "parāmās", UPA: "upādān"}
_NF = {"o": ("n", False, "n"), "aṃ": ("a", False, "na"), "assa": ("g", False, "g"), "ā": ("n", True, "n"),
       "e": ("a", True, "a"), "ānaṃ": ("g", True, "g"), "āni": ("n", True, "n")}
_KU = W("kukkuccaṃ", "နောင်တ ပူပန်မှု", "1", "^1-1164")
NAMED = {
    "kāmacchandanīvaraṇ": W("kāmacchandanīvaraṇaṃ", f"ကာမကို လိုလားမှု {NIV}", "1"),
    "byāpādanīvaraṇ": W("byāpādanīvaraṇaṃ", f"ဖျက်ဆီးလိုစိတ် {NIV}", "1"),
    "thinamiddhanīvaraṇ": W("thinamiddhanīvaraṇaṃ", f"ထိုင်းမှိုင်းမှုနှင့် ငိုက်မျဉ်းမှု {NIV}", "1"),
    "uddhaccanīvaraṇ": W("uddhaccanīvaraṇaṃ", f"ယောက်ယက်ခတ်မှု {NIV}", "1"),
    "kukkuccanīvaraṇ": new("kukkuccanīvaraṇaṃ", f"{_KU} {NIV}"),
    "vicikicchānīvaraṇ": W("vicikicchānīvaraṇaṃ", f"ယုံမှားမှု {NIV}", "1"),
    "avijjānīvaraṇ": W("avijjānīvaraṇaṃ", f"အမှန်ကို မသိမှု {NIV}", "1"),
    "kāmupādān": W("kāmupādānaṃ", f"ကာမ {UPA}", "1"),
    "diṭṭhupādān": W("diṭṭhupādānaṃ", f"အယူ {UPA}", "1"),
    "sīlabbatupādān": W("sīlabbatupādānaṃ", f"သီလ အကျင့်ဝတ် {UPA}", "1"),
    "attavādupādān": W("attavādupādānaṃ", f"အတ္တဟူသော ဝါဒ {UPA}", "1"),
}

# 3-10: «diṭṭhigatavippayuttalobhasahagata-» (pi-1 ^1-1406 «diṭṭhigatavippayuttā lobhasahagata-»: the two qualifiers
# stacked with «၊»), «diṭṭhigatavippayutta lobha» (pi-1 «အယူမှားနှင့် ကင်းကွာသော»; lobha «လောဘ» pi-1)
DGV = W("diṭṭhigatavippayuttaṃ", "အယူမှားနှင့် ကင်းကွာသော", "1")
DLS = W("diṭṭhigatavippayuttā lobhasahagata", "အယူမှားနှင့် ကင်းကွာသော၊ လောဘနှင့်အတူ ဖြစ်သော", "1", "^1-1406")
LOBHA = D.ROOT_N["lobh"]
RAGA = F.LEX["rāgo"][0]
MOHA = D.ROOT_N["moh"]
_DLS_E = {"ā": ("n", True), "aṃ": ("a", False), "o": ("n", False), "e": ("a", True), "ānaṃ": ("g", True),
          "assa": ("g", False)}


def setup_lex_dl():
    for mod in (F, FG):
        for e in _DLS_E:
            mod.add_qual(DLS, "diṭṭhigatavippayuttalobhasahagat" + e)
            mod.add_qual(DGV, "diṭṭhigatavippayutt" + e)
        mod.add_noun(LOBHA, n=["lobho"], a=["lobhaṃ"], g=["lobhassa"])
        mod.add_noun(RAGA, n=["rāgo"], a=["rāgaṃ"], g=["rāgassa"])
        mod.add_noun(MOHA, n=["moho"], a=["mohaṃ"], g=["mohassa"])
        mod.add_noun("စေ့ဆော်မှု", n=["cetanā"])
        for ph, my, k in (("diṭṭhigatavippayutto lobho", f"{DGV} {LOBHA}", "n"),
                          ("diṭṭhigatavippayuttaṃ lobhaṃ", f"{DGV} {LOBHA}", "na"),
                          ("diṭṭhigatavippayuttassa lobhassa", f"{DGV} {LOBHA}", "g"),
                          ("diṭṭhigatavippayuttalobhassa", f"{DGV} {LOBHA}", "g"),
                          ("diṭṭhigatavippayutto rāgo", f"{DGV} {RAGA}", "n"),
                          ("diṭṭhigatavippayuttaṃ rāgaṃ", f"{DGV} {RAGA}", "na"),
                          ("diṭṭhigatavippayuttalobhasahagatā khandhā", f"{DLS} {F.KHANDHA}+", "n"),
                          ("diṭṭhigatavippayuttalobhasahagate khandhe", f"{DLS} {F.KHANDHA}+", "a"),
                          ("diṭṭhigatavippayuttalobhasahagatānaṃ khandhānaṃ", f"{DLS} {F.KHANDHA}+", "g"),
                          ("diṭṭhigatavippayuttalobhasahagatā hetū", f"{DLS} {D.HETU_N}+", "n"),
                          ("diṭṭhigatavippayuttalobhasahagato moho", f"{DLS} {MOHA}", "n"),
                          ("diṭṭhigatavippayuttalobhasahagatā cetanā", f"{DLS} စေ့ဆော်မှု", "n"),
                          ("diṭṭhigatavippayuttalobhasahagatādhipati", f"{DLS} {F.N['adhipati']}", "n")):
            mod.LEX.setdefault(ph, (my, k))
        mod.add_fixed(f"{DLS} {F.N['adhipati']}", "n", False, "diṭṭhigatavippayuttalobhasahagatādhipati")
        # coordinated items with greed (as 2-03 … 2-06 «khandhe ca mohañca» …: each conjunct takes the marker)
        kh, lk = mod.KHANDHA, mod.LAKAUNG
        for pk, my in (("khandhe ca lobhañca", f"{kh}တို့ကို{lk}{C} {LOBHA}ကို{lk}"),
                       ("khandhānaṃ ca lobhassa ca", f"{kh}တို့အား{lk}{C} {LOBHA}အား{lk}")):
            mod.LEX.setdefault(pk, (my, "x"))

        for pk, my, role in (("khandhā ca lobho ca", None, "n"),
                             ("diṭṭhigatavippayuttalobhasahagatā khandhā ca lobho ca", None, "n"),
                             ("diṭṭhigatavippayuttalobhasahagate khandhe ca lobhañca",
                              f"{DLS} {kh}တို့ကို{lk}{C} {LOBHA}ကို{lk}", None),
                             ("diṭṭhigatavippayuttalobhasahagatānaṃ khandhānaṃ ca lobhassa ca",
                              f"{DLS} {kh}တို့အား{lk}{C} {LOBHA}အား{lk}", None)):
            mod.LEX.setdefault(pk, (my or F.np_my(pk.split(), iter([]), role)[0], "x"))
        mod.LEX.setdefault("pubbe samudāciṇṇe", (mod.LEX["pubbe samudāciṇṇe kilese"][0][:-len(" ကိလေသာ+")], "x"))
        mod.add_fixed(f"{DGV} {LOBHA}", "g", False, "diṭṭhigatavippayuttalobhassa")


# «… khandhānaṃ lobhassa ca» (one «ca» after the last member): read as «khandhānaṃ ca lobhassa ca» (as 2-03 … 2-06
# «khandhānaṃ mohassa ca»)
_CA_LOBHA = re.compile(r"(?<= khandhānaṃ) (?=lobhassa ca" + _NB + ")")


def setup_lex():
    setup_lex_dl()
    for mod in (F, FG):
        for my, st in list(NOUN_FORMS.items()) + [(v, k) for k, v in NAMED.items()]:
            for e, (case, pl, lk) in _NF.items():
                w = st + e
                mod.add_fixed(my, case, pl, w)
                mod.NOUN.setdefault(w, (my, case, pl))
                mod.LEX.setdefault(w, (my + ("+" if pl else ""), lk))
    # «X-ā ca sampayuttakā khandhā ca» / «X-añca sampayuttake khandhe ca» … (as 3-01's «hetū ca sampayuttakā khandhā
    # ca»; the module renders them once)
    for st in list(NOUN_FORMS.values()) + list(NAMED):
        for ph, role in ((f"{st}ā ca sampayuttakā khandhā ca", "n"), (f"{st}o ca sampayuttakā khandhā ca", "n"),
                         (f"{st}añca sampayuttake khandhe ca", "@ārabbha"),
                         (f"{st}e ca sampayuttake khandhe ca", "@ārabbha")):
            my = F.np_my(ph.split(), iter([]), role)[0]
            for mod in (F, FG):
                mod.LEX.setdefault(ph, (my, "x"))
        for ph in (f"{st}ānaṃ sampayuttakānañca khandhānaṃ", f"{st}assa sampayuttakānañca khandhānaṃ"):
            my = F.np_my(ph.split(), iter([]), "g")[0]
            for mod in (F, FG):
                mod.LEX.setdefault(ph, (my, "x"))
                if "assa " in ph:            # «Xassa ca sampayuttakānañca khandhānaṃ»: the same two members
                    mod.LEX.setdefault(ph.replace("assa ", "assa ca "), (my, "x"))
    for mod in (F, FG):                      # «vipāko X eko…» (cut short by «…»; the noun left out, as the Pāli)
        mod.SKF["vipāko §T§o eko"] = f"{F.VIPAKA_ADJ} {{T1}} {F.PAA[1]}"
        mod.SKF["kāyāyatanaṃ paccayā kāyaviññāṇaṃ, vatthuṃ paccayā ahetukā §T§ā khandhā"] = (
            f"{F.FIXED['kāyāyatanaṃ'][0]}{F.KYAUNG} {F.KAYAVINNANA}{C} {F.VATTHU}{F.KYAUNG} {F.AHETUKA} {{T1}} "
            f"{F.KHANDHA}များ")
    # the link «saṃsaṭṭhaṃ» (neuter: «kāmacchandanīvaraṇaṃ saṃsaṭṭhaṃ …») = «saṃsaṭṭho»
    for mod in (F, FG):
        mod.LINK["saṃsaṭṭhaṃ"] = mod.LINK["saṃsaṭṭho"]
        mod.CASE["@saṃsaṭṭhaṃ"] = mod.CASE.get("@saṃsaṭṭho", "နှင့်")
    K.ROLE_MARK["saṃsaṭṭhaṃ"] = K.ROLE_MARK["saṃsaṭṭho"]
    K.ROLE_REST["saṃsaṭṭhaṃ"] = K.ROLE_REST["saṃsaṭṭho"]
    K.LINK_ALT = "|".join(sorted(F.LINK, key=len, reverse=True))

# ===================================================================================== editorial notes
# every note of these chapters that the engines do not render is a placeholder «(⁑d<i>)» (D.NOTEP, as 3-01 … 3-02):
# its Burmese is written here from the shared words (1-01 K, 2-03 … 2-06 M, 3-01 … 3-02 D; each new word logged)
CNT = F.COUNT
KAT, VITTH, GAN, VIBHAJ = K.KATABBA, K.VITTH, K.GANETABBA, M.VIBHAJ
EVAM_T, EVAM, KAYYA, SADISANI, SADISA = D.EVAM_T, K.EVAM, K.KAYYA, K.SADISANI, F.SADISA
PANHA, NATTHI, PARIP, SAB = K.PANHA, K.NATTHI, K.PARIPUNNA, D.SAB
CAKKA, ITARE, NINNANAKARANA, NINNANA = D.CAKKA, D.ITARE, D.NINNANAKARANA, K.NOTE_FIXED["ninnānaṃ"]
SAMKH = F.NOTES["(saṃkhittaṃ)"][1:-1]
VARA, PATICCA_V, _pi, _pi_obj = D.VARA, D.PATICCA_V, D._pi, D._pi_obj
AVAS_O = "ကြွင်းသော"                                                  # avasesā (attributive, as 3-01 … 3-02)
ARUPA_N, ARUPE = D.ARUPA_N, F.PREFIX["arūpe"]
AJJH, MAHAB, ASANNA = D.AJJH, D.MAHAB, D.ASANNA
GANANA, GHATANA, PADA, DHAMMA = S.GANANA, F.GHATANA, F.PADA, F.DHAMMA
AVAJJ, VUTTH = F.LEX["āvajjanā"][0], F.LEX["vuṭṭhānassa"][0]
AA = F.LEX["ārammaṇādhipati"][0]                                     # «အာရုံ အကြီးအမှူး»
SAA = F.LEX["sahajātādhipati"][0]                                    # «အတူ ပေါ်ပေါက်သော အကြီးအမှူး»
ADH = F.N["adhipati"]
CULA = D.GOCCHAKA["Cūḷantaradukaṃ"]
LOKIYA = D.DUKA_NAME["Lokiyadukaṃ"]
LOKUTTARA = f"{D.DYADS['lokiya']['lokuttar']} {DHAMMA}"
VARAS = D.NEW["vārā (sections)"]
ANUL_MATIKA, MATIKA, IHA, IMINA, MULA, DASSET, LABBH = (D.ANUL_MATIKA, D.MATIKA, D.IHA, D.IMINA, D.MULA, D.DASSET,
                                                        D.LABBH)
ARABBHA = new("ārabbha (inside a note)", "အာရုံပြု၍")               # LEX «ārabbha» «ကို အာရုံပြု၍»
NAKAT = new("na kātabbaṃ", "မပြုရ")                                   # = 2-07 … 2-11
PANCAY = D.NEW["pañcāyatanāni"]
AMASANA = new("āmasanaṃ", "ရည်ညွှန်းပုံ")
CHADDETABBA = new("chaḍḍetabbaṃ", "ဖယ်ရမည်")                          # (3-01 … 3-02 chaḍḍetvā «ဖယ်၍»)
DN = DUKA_NAME
NIV_T, PAR_T, UPA_T = NIV, PAR, UPA


def _notep_mine():
    cn, cd = F.cname, F.cond
    nm_niv, nm_par, nm_upa = DN["Nīvaraṇadukaṃ"], DN["Parāmāsadukaṃ"], DN["Upādānadukaṃ"]
    dk_lok = f"{CULA}၌ {LOKIYA}"
    return {
        # 3-07
        "(cakkaṃ. Saṃkhittaṃ)": f"({CAKKA}{END} {SAMKH})",
        "(cakkaṃ. Saṃkhittaṃ.)": f"({CAKKA}{END} {SAMKH}{END})",
        "(Avasesā pañhā sabbe vitthāretabbā. Arūpaṃ paṭhamaṃ kātabbaṃ, rūpaṃ pacchā yathā labhati.)":
            (f"({AVAS_O} {PANHA} {SAB}ကို {VITTH}{END} {ARUPA_N}ကို " + new("paṭhamaṃ", "ပထမ") + f" {KAT}{C} ရုပ်ကို "
             + new("pacchā", "နောက်မှ") + f" {LABBH}{END})"),
        "(Sahajātavāropi evaṃ vitthāretabbo)": f"({VARA('sahajāta')}ကိုလည်း {EVAM_T} {VITTH})",
        "(yāva ajjhattikā mahābhūtā)": f"({AJJH} {MAHAB}တို့အထိ)",
        "(cakkaṃ. Sabbaṃ nīvaraṇaṃ vitthāretabbaṃ)": f"({CAKKA}{END} {NIV} {SAB}ကို {VITTH})",
        "(Evaṃ itare dve gaṇanāpi sampayuttavāropi kātabbo.)":
            f"({EVAM_T} {ITARE} {GANANA} {CNT['dve']}ကိုလည်း{C} {VARA('sampayutta')}ကိုလည်း {KAT}{END})",
        "(Evaṃ itare dve gaṇanāpi sampayuttavārāpi kātabbā.)":
            f"({EVAM_T} {ITARE} {GANANA} {CNT['dve']}ကိုလည်း{C} {VARA('sampayutta')}ကိုလည်း {KAT}{END})",
        "(Evaṃ itare dve gaṇanāpi nissayavāropi kātabbo.)":
            f"({EVAM_T} {ITARE} {GANANA} {CNT['dve']}ကိုလည်း{C} {VARA('nissaya')}ကိုလည်း {KAT}{END})",
        "(ārabbha kātabbā)": f"({ARABBHA} {KAT})",
        "(ārammaṇādhipatiyeva)": f"({AA}သာ)",
        "(tīṇi upanissayā)": f"({F.N['upanissaya']} {CNT['tīṇi']})",
        "(purejātaṃ ārammaṇasadisaṃ kusalākusalassa vibhajitabbaṃ)":
            f"({F.N['purejāta']}ကို {F.N['ārammaṇa']}နှင့် တူအောင် {F.LEX['kusalākusalaṃ'][0]}အား {VIBHAJ})",
        "(evaṃ avasesā cattāri pañhā kātabbā)": f"({EVAM_T} {AVAS_O} {PANHA} {CNT['cattāri']}ကို {KAT})",
        "(evaṃ nīvaraṇamūle tīṇi )": f"({EVAM_T} {DYADS_ADD['niv1']['nīvaraṇdk']} {DHAMMA}{F.MULAKA}၌ {CNT['tīṇi']})",
        "(anulomamātikā)": f"({ANUL_MATIKA})",
        "(anulomamātikā )": f"({ANUL_MATIKA})",
        "(nīvaraṇiyadukaṃ yathā lokiyadukaṃ evaṃ kātabbaṃ ninnānākaraṇaṃ)":
            f"({DN['Nīvaraṇiyadukaṃ']}ကို {LOKIYA}{KAYYA} {EVAM} {NINNANAKARANA} {KAT})",   # harmonise (align): = 3-03 order, no «၊» the Pāli lacks
        "(Nīvaraṇadukassa mātikā idha katā.)":
            f"({nm_niv}၏ {MATIKA}ကို {IHA} " + new("katā", "ပြုထားသည်") + f"{END})",
        "(yāva asaññasattā. Saṃkhittaṃ)": f"({D.YAVA_AS}{END} {SAMKH})",
        "(Sahajātavāropi evaṃ kātabbo.)": f"({VARA('sahajāta')}ကိုလည်း {EVAM_T} {KAT}{END})",
        "(yāva āvajjanāya)": f"({AVAJJ}အထိ)",
        "(idha purimā purimāti natthi)": f"({IHA} {F.QUAL['purimā purimā']}ဟူ၍ {NATTHI})",
        "(anulomagaṇanā)": f"({K.ORDER_N['anulomagaṇanā']})",
        "(Evaṃ sabbe gaṇanā vibhajitabbā, nīvaraṇadukasadisaṃ ninnānākaraṇaṃ.)":
            f"({EVAM_T} {GANANA} {SAB}ကို {VIBHAJ}{C} {nm_niv}{SADISA}{C} {NINNANAKARANA}{END})",
        "(yāva āvajjanā tāva kātabbā)": f"({AVAJJ}အထိ {KAT})",
        "(evaṃ itarepi tīṇi kātabbā)": f"({EVAM_T} {ITARE} {CNT['tīṇi']}ကိုလည်း {KAT})",
        "(Ārammaṇasadisā adhipatipaccayā, purejātampi ārammaṇasadisaṃ. Upanissayepi lokuttaraṃ na kātabbaṃ. "
        "Saṃkhittaṃ, evaṃ vitthāretabbaṃ yathā nīvaraṇadukaṃ, evaṃ paccavekkhitvā kātabbaṃ.)":
            (f"({cn('adhipati')}တို့သည် {F.N['ārammaṇa']}{SADISANI}{C} {F.N['purejāta']}သည်လည်း "
             f"{F.N['ārammaṇa']}{SADISA}{END} {cn('upanissaya')}၌လည်း {LOKUTTARA}ကို {NAKAT}{END} {SAMKH}{C} "
             f"{nm_niv}{KAYYA} {EVAM} {VITTH}{C} {EVAM_T} " + new("paccavekkhitvā", "ပြန်လည် ဆင်ခြင်၍")
             + f" {KAT}{END})"),
        "(cakkaṃ. Sabbepi nīvaraṇā kātabbā)": f"({CAKKA}{END} {NIV} {SAB}ကိုလည်း {KAT})",
        "(Evaṃ sahajātavāropi paccayavāropi nissayavāropi saṃsaṭṭhavāropi sampayuttavāropi paṭiccavārasadisā "
        "ninnānākaraṇā.)":
            (f"({EVAM_T} {_pi('sahajāta', 'paccaya', 'nissaya', 'saṃsaṭṭha', 'sampayutta')} {PATICCA_V}{SADISANI}"
             f"{C} {NINNANAKARANA}{END})"),
        "(garukārammaṇāyeva)": "(" + new("garukārammaṇa", "လေးစားဖွယ်ရာ ပြုထားသော အာရုံ") + "သာ)",
        "(āvajjanāpi vuṭṭhānampi natthi, sabbattha purimā purimā kātabbā)":
            f"({AVAJJ}လည်း{C} {VUTTH}လည်း {NATTHI}{C} {K.SABBATTHA} {F.QUAL['purimā purimā']}ကို {KAT})",
        "(ārammaṇasadisaṃ, vipāko natthi)": f"({F.N['ārammaṇa']}{SADISA}{C} {F.N['vipāka']} {NATTHI})",
        "(evaṃ navapi tīsu padesu parivattetabbā)":
            (f"({EVAM_T} {CNT['nava']}လုံးကို {PADA} {CNT['tīṇi']}၌ " + new("parivattetabbā", "လှည့်ပြောင်းရမည်")
             + ")"),
        "(Yathā cūḷantaraduke lokiyadukaṃ evaṃ kātabbaṃ ninnānākaraṇaṃ.)":
            f"({dk_lok}{KAYYA} {EVAM} {NINNANAKARANA} {KAT}{END})",   # harmonise (align): = 3-03 «… ထိုနည်းတူ ကွဲပြားချက် မရှိ ပြုရမည်။»
        # 3-08
        "(yāva asaññasattā mahābhūtā)": f"({ASANNA}တို့၏ {MAHAB}တို့အထိ)",
        "(evaṃ sabbattha kātabbaṃ)": f"({EVAM_T} {K.SABBATTHA} {KAT})",
        "(evaṃ pañca pañhā kātabbā arūpeyeva, saṃsaṭṭhavāropi sampayuttavāropi evaṃ kātabbā)":
            (f"({EVAM_T} {PANHA} {CNT['pañca']}ကို {ARUPE}ပင် {KAT}{C} {_pi_obj('saṃsaṭṭha', 'sampayutta')} "
             f"{EVAM_T} {KAT})"),
        "(ārammaṇādhipatiyeva kātabbā)": f"({AA}ကိုသာ {KAT})",
        "(pacchājātā kātabbā)": f"({F.N['pacchājāta']}ကို {KAT})",
        "(evaṃ pañca pañhā kātabbā)": f"({EVAM_T} {PANHA} {CNT['pañca']}ကို {KAT})",
        "(parāmaṭṭhadukaṃ yathā cūḷantaraduke lokiyadukaṃ evaṃ kātabbaṃ ninnānākaraṇaṃ)":
            f"({DN['Parāmaṭṭhadukaṃ']}ကို {dk_lok}{KAYYA} {EVAM} {NINNANAKARANA} {KAT})",   # harmonise (align): = 3-03 order
        "(Sabbe vārā yathā parāmāsadukaṃ evaṃ kātabbaṃ ninnānākaraṇaṃ.)":
            f"({VARAS} {SAB}ကို {nm_par}{KAYYA} {EVAM} {NINNANAKARANA} {KAT}{END})",   # harmonise (align): = 3-03 order
        "(ārabbha kātabbāni parāmāsadukasadisaṃ)": f"({ARABBHA} {KAT}{C} {nm_par}{SADISA})",
        "(yāva āvajjanā sabbaṃ kātabbaṃ)": f"({AVAJJ}အထိ {SAB}ကို {KAT})",
        "(Evaṃ itarepi tīṇi ārabbha kātabbāni. Imaṃ dukaṃ parāmāsadukasadisaṃ. Lokuttaraṃ yahiṃ na labbhati tahiṃ na "
        "kātabbaṃ.)":
            (f"({EVAM_T} {ITARE} {CNT['tīṇi']}ကိုလည်း {ARABBHA} {KAT}{END} ဤ {DUKA}သည် {nm_par}{SADISA}{END} "
             f"{LOKUTTARA}ကို " + new("yahiṃ na labbhati tahiṃ", "မတွေ့ရသော နေရာ၌") + f" {NAKAT}{END})"),
        # 3-10
        "(sabbaṃ cakkaṃ kātabbaṃ)": f"({CAKKA} {SAB}ကို {KAT})",
        "(sabbe cakkā kātabbā)": f"({CAKKA} {SAB}ကို {KAT})",
        "(navapi pañhā kātabbā, rūpaṃ chaḍḍetabbaṃ)":
            f"({PANHA} {CNT['nava']}လုံးကို {KAT}{C} ရုပ်ကို {CHADDETABBA})",
        "(saṃkhittaṃ, navapi pañhā arūpe dve upādānā)":
            f"({SAMKH}{C} {PANHA} {CNT['nava']}လုံး{C} {ARUPE} {UPA} {F.PAA[2]})",
        "(Sahajātavāro paṭiccavārasadiso vibhajantena diṭṭhupādānaṃ \"sahajātaṃ kāmupādāna\"nti kātabbaṃ.)":
            (f"({VARA('sahajāta')}သည် {PATICCA_V}{SADISA}{C} " + new("vibhajantena", "ခွဲခြမ်းစိတ်ဖြာသူသည်")
             + f" {NAMED['diṭṭhupādān']}ကို “အတူ ပေါ်ပေါက်သော {NAMED['kāmupādān']}”ဟု {KAT}{END})"),
        "(paṭiccasadisā)": f"({PATICCA_V}{SADISANI})",
        "(ārammaṇe noupādānamūlake pañcāyatanañca vatthuñca kātabbā)":
            (f"({cd('ārammaṇa', 'loc')} {DYADS_ADD['upa1']['noupādān']} {DHAMMA}{F.MULAKA}၌ {PANCAY}ကို{F.LAKAUNG}{C} "
             f"{F.VATTHU}ကို{F.LAKAUNG} {KAT})"),
        "(cakkaṃ. Evaṃ navapi pañhā kātabbā)": f"({CAKKA}{END} {EVAM_T} {PANHA} {CNT['nava']}လုံးကို {KAT})",
        "(ārabbha kātabbā, ārammaṇādhipatiyeva)": f"({ARABBHA} {KAT}{C} {AA}သာ)",
        "(ekoyeva kabaḷīkāro āhāro)": f"({D.KABALI} တစ်ခုတည်း)",
        "(rūpajīvitindriyaṃ ekaṃyeva)": f"({D.RJIVIT} တစ်ခုတည်း)",
        "(iminā kāraṇena nava pañhā kātabbā)": f"({IMINA} {PANHA} {CNT['nava']}ကို {KAT})",
        "(saṃkhittaṃ, sahajātasadisaṃ sahajātaṃ vibhajitabbaṃ, purejātasadisaṃ purejātaṃ)":
            (f"({SAMKH}{C} {F.N['sahajāta']}ကို {F.N['sahajāta']}နှင့် တူအောင် {VIBHAJ}{C} {F.N['purejāta']}ကို "
             f"{F.N['purejāta']}နှင့် တူအောင်)"),
        "(yathā lokiyadukaṃ, evaṃ kātabbaṃ. Ninnānākaraṇaṃ)": f"({LOKIYA}{KAYYA} {EVAM} {KAT}{END} {NINNANAKARANA})",
        "(Itare dve gaṇanāpi kātabbā. Sahajātavāro paṭiccavārasadiso.)":
            f"({ITARE} {GANANA} {CNT['dve']}ကိုလည်း {KAT}{END} {VARA('sahajāta')}သည် {PATICCA_V}{SADISA}{END})",
        "(Saṃkhittaṃ. Ārammaṇapaccayamhi pañca viññāṇā kātabbā.)":
            f"({SAMKH}{END} {cd('ārammaṇa', 'loc')} " + new("pañca viññāṇā", "သိစိတ် ငါးပါး") + f"ကို {KAT}{END})",
        "(paṭiccasadisaṃ, arūpaṃyeva kātabbaṃ)": f"({PATICCA_V}{SADISA}{C} {ARUPA_N}ကိုသာ {KAT})",
        "(sabbaṃ paripuṇṇaṃ)": f"({SAB} {PARIP}သည်)",
        "(yāva kāyaviññāṇaṃ)": f"({F.KAYAVINNANA}အထိ)",
        "(imesu catūsupi yathā kammapaccaye diṭṭhigatavippayutto lobho dassito evaṃ dassetabbo. Cattāri cattāri "
        "pañhā)":
            (f"(ဤ {CNT['cattāri']}လုံး၌ {cd('kamma', 'loc')} {DGV} {LOBHA}ကို " + new("dassito", "ပြထားသ")
             + f"{KAYYA} {EVAM} {DASSET}{END} {PANHA} " + new("cattāri cattāri", "လေးခုစီ") + ")"),
        "(imesu sahajātaṃ sahajātasadisaṃ, purejātaṃ purejātasadisaṃ)":
            (f"(ဤတို့၌ {F.N['sahajāta']}သည် {F.N['sahajāta']}{SADISA}{C} {F.N['purejāta']}သည် "
             f"{F.N['purejāta']}{SADISA})"),
        "(Yathā upādānadukaṃ evaṃ paṭiccavāropi sahajātavāropi paccayavāropi nissayavāropi saṃsaṭṭhavāropi "
        "sampayuttavāropi kātabbā, ninnānākaraṇā, āmasanaṃ nānākaraṇaṃ.)":
            (f"({nm_upa}{KAYYA} {EVAM} {_pi_obj('paṭicca', 'sahajāta', 'paccaya', 'nissaya', 'saṃsaṭṭha', 'sampayutta')} "
             f"{KAT}{C} {NINNANAKARANA}{C} {AMASANA}သည် {K.NANAKARANA} ဖြစ်သည်{END})"),
        "(upādānadukasadisā ninnānā, nava pañhā)": f"({nm_upa}{SADISANI}{C} {NINNANA}{C} {PANHA} {CNT['nava']})",
        "(saṃkhittaṃ, itare dve upādānadukasadisā)": f"({SAMKH}{C} {ITARE} {CNT['dve']}သည် {nm_upa}{SADISANI})",
        # harmonise H22: heṭṭhā (earlier in the text) «ရှေ့၌» as pi-6 (was «အထက်၌»)
        "(heṭṭhā adhipati tīṇi, upādānadukasadisā)":
            "(" + new("heṭṭhā", "ရှေ့၌") + f" {ADH} {CNT['tīṇi']}{C} {nm_upa}{SADISANI})",
        "(avasesā dvepi ārammaṇādhipati sahajātādhipatipi upādānadukasadisā)":
            f"({AVAS_O} {CNT['dve']}လုံး {AA}{C} {SAA}လည်း {nm_upa}{SADISANI})",
        "(Ghaṭanā adhipati tīṇi, upādānadukasadisā. Sabbe paccayā upādānadukasadisā. Upādāniye lokuttaraṃ natthi, "
        "paccanīyampi itare dve gaṇanāpi upādānadukasadisaṃ.)":
            (f"({GHATANA} {ADH} {CNT['tīṇi']}{C} {nm_upa}{SADISANI}{END} {F.PACCAYA} {SAB}တို့သည် {nm_upa}{SADISANI}{END} "
             f"{DYADS_ADD['upa2']['upādāniy']} {DHAMMA}၌ {LOKUTTARA} {NATTHI}{C} {K.ORDER_N['paccanīyaṃ']}လည်း{C} "
             f"{ITARE} {GANANA} {CNT['dve']}လည်း {nm_upa}{SADISA}{END})"),
        "(Saṃkhittaṃ. Āmasanaṃ nānākaraṇaṃ upādānadukasadisaṃ nava pañhā. Rūpaṃ natthi. Evaṃ sabbepi vārā "
        "vitthāretabbā. Arūpaṃyeva.)":
            (f"({SAMKH}{END} {AMASANA}သည် {K.NANAKARANA} ဖြစ်သည်{C} {nm_upa}{SADISA}{C} {PANHA} {CNT['nava']}{END} "
             f"ရုပ် {NATTHI}{END} {EVAM_T} {VARAS} {SAB}ကိုလည်း {VITTH}{END} {ARUPA_N}သာ{END})"),
        "(tīṇipi kātabbā, ghaṭane tīṇipi kātabbā)":
            f"({CNT['tīṇi']}လုံးကို {KAT}{C} {GHATANA}၌ {CNT['tīṇi']}လုံးကို {KAT})",
        "(tīṇipi, tīsupi dvepi adhipati kātabbā, ghaṭanādhipatipi tīṇi)":
            (f"({CNT['tīṇi']}လုံး{C} {CNT['tīṇi']}လုံး၌ {ADH} {CNT['dve']}လုံးကို {KAT}{C} {GHATANA} {ADH}လည်း "
             f"{CNT['tīṇi']})"),
        "(evaṃ navapi pañhā kātabbā, āvajjanāpi vuṭṭhānampi natthi)":
            f"({EVAM_T} {PANHA} {CNT['nava']}လုံးကို {KAT}{C} {AVAJJ}လည်း{C} {VUTTH}လည်း {NATTHI})",
        "(tīṇi ghaṭanupanissayepi tīṇi)": f"({CNT['tīṇi']}{C} {GHATANA} {F.N['upanissaya']}၌လည်း {CNT['tīṇi']})",
        "(evaṃ navapi kātabbā, ekekassa mūle tīṇi tīṇi pañhā)":
            (f"({EVAM_T} {CNT['nava']}လုံးကို {KAT}{C} {MULA} " + new("ekekassa", "တစ်ခုစီ") + f"၌ {PANHA} "
             + new("tīṇi tīṇi", "သုံးခုစီ") + ")"),
        "(Imaṃ dukaṃ cūḷantaraduke lokiyadukasadisaṃ, ninnānākaraṇaṃ.)":
            f"(ဤ {DUKA}သည် {dk_lok}{SADISA}{C} {NINNANAKARANA}{END})",
    }


def setup_notes():
    for k, my in _notep_mine().items():
        if k in D.NOTEP:
            raise SystemExit("note twice: " + k)
        D.NOTEP[k] = my
        i = list(D.NOTEP).index(k)
        new(k, my)
        K.NOTE_FIXED[f"⁑d{i}"] = my[1:-1]
        for mod in (F, FG):
            mod.NOTES[f"(⁑d{i})"] = my

# ===================================================================================== unique sentences
SK_ADD = {}
_VAR_UNIT = ("kāmacchandanīvaraṇaṃ paṭicca thinamiddhanīvaraṇaṃ {thīnamiddhanīvaraṇaṃ (syā.)} uddhaccanīvaraṇaṃ "
             "avijjānīvaraṇaṃ, kāmacchandanīvaraṇaṃ paṭicca uddhaccanīvaraṇaṃ avijjānīvaraṇaṃ, byāpādanīvaraṇaṃ paṭicca "
             "thinamiddhanīvaraṇaṃ uddhaccanīvaraṇaṃ avijjānīvaraṇaṃ, byāpādanīvaraṇaṃ paṭicca uddhaccanīvaraṇaṃ "
             "avijjānīvaraṇaṃ, byāpādanīvaraṇaṃ paṭicca thinamiddhanīvaraṇaṃ uddhaccanīvaraṇaṃ kukkuccanīvaraṇaṃ "
             "avijjānīvaraṇaṃ, byāpādanīvaraṇaṃ paṭicca uddhaccanīvaraṇaṃ kukkuccanīvaraṇaṃ avijjānīvaraṇaṃ, "
             "vicikicchānīvaraṇaṃ paṭicca uddhaccanīvaraṇaṃ, uddhaccanīvaraṇaṃ paṭicca avijjānīvaraṇaṃ.")
_DEEDS = ("adinnaṃ ādiyati", "musā bhaṇati", "pisuṇaṃ bhaṇati", "samphaṃ palapati", "sandhiṃ chindati",
          "nillopaṃ harati", "ekāgārikaṃ karoti", "paripanthe tiṭṭhati", "paradāraṃ gacchati", "gāmaghātaṃ karoti")


def _engine(text, d):
    """a unit through the engine with dyad d active (to build a template from the same frames)"""
    D.set_dyad(F, d)
    D.set_dyad(FG, d)
    FG.translate("")
    try:
        return F.translate(D.prep(text, d)).strip("\n")
    finally:
        D.set_dyad(F, None)
        D.set_dyad(FG, None)


def setup_sk():
    # the hindrance list with a variant inside it: the list rendered by the engine without the variant, the variant
    # after its word (as the Pāli)
    plain = _engine(re.sub(r" \{[^{}]*\}", "", _VAR_UNIT), "niv1")
    anchor = NAMED["thinamiddhanīvaraṇ"]
    assert plain.count(anchor) > 1 and "{" not in plain
    SK_ADD[D._key(_VAR_UNIT, "niv1")] = plain.replace(anchor, anchor + " {V1}", 1)
    # «… rūpaṃ, dve khandhe ca…pe…»: «dve khandhe ca» after a comma (elsewhere after «…pe…»): rendered by the engine
    # with «…pe…» in the comma's place, then the comma restored as «၊»
    # (the engine cuts the note «(cakkaṃ kātabbaṃ)» off first: the key is the unit before it)
    u_read = ("noupādānaṃ ekaṃ khandhañca diṭṭhupādānañca paṭicca tayo khandhā kāmupādānañca cittasamuṭṭhānañca rūpaṃ, "
              "dve khandhe ca…pe…")
    plain = _engine(u_read.replace("rūpaṃ, dve", "rūpaṃ…pe… dve"), "upa1")
    term = DYADS_ADD["upa1"]["noupādān"]
    assert plain.startswith(term) and plain.count(term) == 1 and plain.count(PE) == 2, plain
    SK_ADD[D._key(u_read, "upa1")] = "{T1}" + plain[len(term):].replace(PE + " ", C + " ", 1)
    kh, lk = F.KHANDHA, F.LAKAUNG
    SK_ADD[D._key("(Mūlaṃ kātabbaṃ) purimā purimā noparāmāsā khandhā pacchimassa pacchimassa parāmāsassa ca "
                  "sampayuttakānañca khandhānaṃ anantarapaccayena paccayo", "par1")] = (
        f"({K.NOTE_FIXED['mūlaṃ kātabbaṃ']}) "
        f"{F.QUAL['purimā purimā']} {{T1}} {kh}တို့သည် {F.QUAL['pacchimassa pacchimassa']} "
        f"{F.LEX['parāmāsassa ca sampayuttakānañca khandhānaṃ'][0]} {{C1.if}}")
    SK_ADD[D._key("tīṇi upanissayā parāmāso ca sampayuttakā ca khandhā parāmāsassa upanissayapaccayena paccayo… tīṇi.",
                  "par1")] = (
        f"{F.N['upanissaya']} {CNT['tīṇi']}{C} {F.LEX['parāmāso ca sampayuttakā khandhā ca'][0]} {PAR}အား "
        f"{{C1.if}}{PE} {CNT['tīṇi']}{END}")
    for mod in (F, FG):
        mod.SK.update(SK_ADD)
        for dd in _DEEDS:                 # the deeds cut short by «…» (the object of the module's full deed)
            w = dd.split()[0]
            full = mod.LEX[dd][0]
            m = re.match(r"(.*?(?:ကို|၌|ထံ))(?= )", full)
            mod.LEX.setdefault(w, (m[1] if m else full.split(" ")[0], "x"))

# ===================================================================================== the run
def translate(name):
    return D.translate(name)


def setup():
    setup_names()
    setup_lex()
    setup_notes()
    D.SLIP_FIX.update(SLIP_ADD)
    D._PREP_DYAD = D.prep_dyad
    D.prep_dyad = _prep_dyad
    D._SET_DYAD = D.set_dyad
    D.set_dyad = _set_dyad
    setup_sk()


setup()


class Counting(dict):
    cnt = collections.Counter()

    def setdefault(self, k, v):
        self.cnt[k] += 1
        return super().setdefault(k, v)


def regress():
    bad = 0
    for n in D.NAMES:
        txt = D.translate(n)
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
        print(len(rows), "unmatched skeletons,", sum(F.UNSEEN.cnt.values()), "occurrences")
    if F.SLIPS and "--slips" in sys.argv:
        print("slips:", *sorted(F.SLIPS), sep="\n  ")


if __name__ == "__main__":
    main()
