"""Burmese zero-shot of pi-7 4-01 kilesagocchaka (the kilesa dyads and the piṭṭhiduka dyads of the Dukapaṭṭhāna,
«အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ»), from the Pāli only.

usage: python3 -I -X utf8 make_ch4-01.py [--dev] [--regress] [--slips] [--out DIR]
  (no flag)  translate the chapter and write it; stops on the first unmatched sentence (nothing is guessed).
  --dev      do not stop: list every unmatched skeleton with its count in chk-ch4-01/dev.txt (nothing written).
  --regress  regenerate 3-07, 3-08, 3-10 (and through them 3-01 … 3-02) in memory and compare them with the
             published files (they must be identical).

Engine (read-only, imported, never run as a script): make_ch3-07-08-10.py is IMPORTED (it imports make_ch3-01-02.py,
which imports make_ch2-03-06.py in the same way: PRIMARY my7_formulas + make_sample + make_ch1-01, FALLBACK per unit
make_ch1-03-05). Its gocchaka machinery (the term glue of dyads 1, 4, 5, 6, own term endings) and 3-01 … 3-02's dyad
machinery (the chapter cut at the dyad headings, one dyad active per part, pseudo a-stem terms, both-members slots,
NOTEP placeholders, lexicon) are reused as they are; this script adds the kilesa dyads (pi-1 final Mātikā ^1-M2-75 …
^1-M2-82) and the piṭṭhiduka dyads (^1-M2-83 … ^1-M2-100), their names, nouns, notes and unique sentences. No main
block of another script runs; no file of the sample or of another group is edited. Every new string is logged in
notes-ch4-01.md.
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
NAMES = ["4-01-kilesagocchaka.md"]
CHK = HERE / "chk-ch4-01"
WCH = r"[\wāīūṃṅñṭḍṇḷ]"
_NB = r"(?!" + WCH + ")"
_PB = r"(?<!" + WCH + ")"


def _load(name, fn):
    spec = importlib.util.spec_from_file_location(name, HERE / fn)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


B = _load("ch3070810", "make_ch3-07-08-10.py")     # its setup() runs on import; its main() does not
D = B.D
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
KIL = W("kilesā dhammā", "ကိလေသာ", "1", "^1-M2-75")
DYADS_ADD = {
    # kilesa (^1-M2-75 … ^1-M2-82); the keys «kil1 / kil4 / kil5 / kil6» take 3-07 … 3-10's glue (prep_mine)
    "kil1": {"kilesdk": _dw("kilesā dhammā", "ကိလေသာ ဖြစ်သော", "^1-M2-75"),
             "nokiles": _dw("no kilesā dhammā", "ကိလေသာ မဟုတ်သော", "^1-M2-75")},
    "kil2": {"saṃkilesik": _dw("saṃkilesikā dhammā", "ကိလေသာ၏ အာရုံ ဖြစ်နိုင်သော", "^1-M2-76"),
             "asaṃkilesik": _dw("asaṃkilesikā dhammā", "ကိလေသာ၏ အာရုံ မဖြစ်နိုင်သော", "^1-M2-76")},
    "kilS": {"saṃkiliṭṭh": _dw("saṃkiliṭṭhā dhammā", "ကိလေသာဖြင့် ညစ်နွမ်းသော", "^1-M2-77"),
             "asaṃkiliṭṭh": _dw("asaṃkiliṭṭhā dhammā", "ကိလေသာဖြင့် မညစ်နွမ်းသော", "^1-M2-77")},
    "kilP": {"kilesasampayutt": _dw("kilesasampayuttā dhammā", "ကိလေသာနှင့် ယှဉ်တွဲသော", "^1-M2-78"),
             "kilesavippayutt": _dw("kilesavippayuttā dhammā", "ကိလေသာနှင့် ကင်းကွာသော", "^1-M2-78")},
    "kil4": {"kilesasaṃkilesikdk": _dw("kilesā ceva dhammā saṃkilesikā ca",
                                       "ကိလေသာလည်း ဖြစ်၊ ကိလေသာ၏ အာရုံလည်း ဖြစ်နိုင်သော", "^1-M2-79"),
             "saṃkilesikanokilesdk": _dw("saṃkilesikā ceva dhammā no ca kilesā",
                                         "ကိလေသာ၏ အာရုံ ဖြစ်နိုင်သော်လည်း ကိလေသာ မဟုတ်သော", "^1-M2-79")},
    "kilB": {"kilesasaṃkiliṭṭhdk": _dw("kilesā ceva dhammā saṃkiliṭṭhā ca",
                                       "ကိလေသာလည်း ဖြစ်၊ ကိလေသာဖြင့်လည်း ညစ်နွမ်းသော", "^1-M2-80"),
             "saṃkiliṭṭhanokilesdk": _dw("saṃkiliṭṭhā ceva dhammā no ca kilesā",
                                         "ကိလေသာဖြင့် ညစ်နွမ်းသော်လည်း ကိလေသာ မဟုတ်သော", "^1-M2-80")},
    "kil5": {"kilesakilesasampdk": _dw("kilesā ceva dhammā kilesasampayuttā ca",
                                       "ကိလေသာလည်း ဖြစ်၊ ကိလေသာနှင့်လည်း ယှဉ်တွဲသော", "^1-M2-81"),
             "kilesasampnokilesdk": _dw("kilesasampayuttā ceva dhammā no ca kilesā",
                                        "ကိလေသာနှင့် ယှဉ်တွဲသော်လည်း ကိလေသာ မဟုတ်သော", "^1-M2-81")},
    # ^1-M2-82 is not attributive in pi-1: the two terms in the forms of 3-03 … 3-06 / 3-07 … 3-10 (NEW)
    "kil6": {"kilesavippsaṃkilesik": new("kilesavippayutto saṃkilesiko (dyad term)",
                                         "ကိလေသာနှင့် ကင်းကွာသော်လည်း ကိလေသာ၏ အာရုံ ဖြစ်နိုင်သော"),
             "kilesavippasaṃkilesik": new("kilesavippayutto asaṃkilesiko (dyad term)",
                                          "ကိလေသာနှင့် ကင်းကွာ၊ ကိလေသာ၏ အာရုံ မဖြစ်နိုင်သော")},
    # piṭṭhiduka (^1-M2-83 … ^1-M2-100)
    "dass": {"dassanena pahātabb": _dw("dassanena pahātabbā dhammā", "သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ရမည့်", "^1-M2-83"),
             "nadassanena pahātabb": _dw("na dassanena pahātabbā dhammā",
                                         "သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ရမည် မဟုတ်သော", "^1-M2-83")},
    "bhav": {"bhāvanāya pahātabb": _dw("bhāvanāya pahātabbā dhammā", "ဘာဝနာ ပွားများခြင်းဖြင့် ပယ်ရမည့်", "^1-M2-84"),
             "nabhāvanāya pahātabb": _dw("na bhāvanāya pahātabbā dhammā",
                                         "ဘာဝနာ ပွားများခြင်းဖြင့် ပယ်ရမည် မဟုတ်သော", "^1-M2-84")},
    "dassh": {"dassanena pahātabbahetuk": _dw("dassanena pahātabbahetukā dhammā",
                                              "သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ရမည့် အမြစ် ရှိသော", "^1-M2-85"),
              "nadassanena pahātabbahetuk": _dw("na dassanena pahātabbahetukā dhammā",
                                                "သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ရမည့် အမြစ် ရှိသည် မဟုတ်သော", "^1-M2-85")},
    "bhavh": {"bhāvanāya pahātabbahetuk": _dw("bhāvanāya pahātabbahetukā dhammā",
                                              "ဘာဝနာ ပွားများခြင်းဖြင့် ပယ်ရမည့် အမြစ် ရှိသော", "^1-M2-86"),
              "nabhāvanāya pahātabbahetuk": _dw("na bhāvanāya pahātabbahetukā dhammā",
                                                "ဘာဝနာ ပွားများခြင်းဖြင့် ပယ်ရမည့် အမြစ် ရှိသည် မဟုတ်သော", "^1-M2-86")},
    "vitakka": {"savitakk": _dw("savitakkā dhammā", "စတင်ကြံစည်မှု ရှိသော", "^1-M2-87"),
                "avitakk": _dw("avitakkā dhammā", "စတင်ကြံစည်မှု မရှိသော", "^1-M2-87")},
    "vicara": {"savicār": _dw("savicārā dhammā", "ဆက်လက်သုံးသပ်မှု ရှိသော", "^1-M2-88"),
               "avicār": _dw("avicārā dhammā", "ဆက်လက်သုံးသပ်မှု မရှိသော", "^1-M2-88")},
    "sappitika": {"sappītik": _dw("sappītikā dhammā", "ပီတိ ရှိသော", "^1-M2-89"),
                  "appītik": _dw("appītikā dhammā", "ပီတိ မရှိသော", "^1-M2-89")},
    "piti": {"pītisahagat": _dw("pītisahagatā dhammā", "ပီတိနှင့်အတူ ဖြစ်သော", "^1-M2-90"),
             "napītisahagat": _dw("na pītisahagatā dhammā", "ပီတိနှင့်အတူ ဖြစ်သည် မဟုတ်သော", "^1-M2-90")},
    "sukha": {"sukhasahagat": _dw("sukhasahagatā dhammā", "သာယာမှုနှင့်အတူ ဖြစ်သော", "^1-M2-91"),
              "nasukhasahagat": _dw("na sukhasahagatā dhammā", "သာယာမှုနှင့်အတူ ဖြစ်သည် မဟုတ်သော", "^1-M2-91")},
    "upekkha": {"upekkhāsahagat": _dw("upekkhāsahagatā dhammā", "ဥပေက္ခာနှင့်အတူ ဖြစ်သော", "^1-M2-92"),
                "naupekkhāsahagat": _dw("na upekkhāsahagatā dhammā", "ဥပေက္ခာနှင့်အတူ ဖြစ်သည် မဟုတ်သော",
                                        "^1-M2-92")},
    "kama": {"kāmāvacar": _dw("kāmāvacarā dhammā", "ကာမဘုံနှင့် ဆိုင်သော", "^1-M2-93"),
             "nakāmāvacar": _dw("na kāmāvacarā dhammā", "ကာမဘုံနှင့် ဆိုင်သည် မဟုတ်သော", "^1-M2-93")},
    "rupa": {"rūpāvacar": _dw("rūpāvacarā dhammā", "သိမ်မွေ့သော ရုပ်ဘုံနှင့် ဆိုင်သော", "^1-M2-94"),
             "narūpāvacar": _dw("na rūpāvacarā dhammā", "သိမ်မွေ့သော ရုပ်ဘုံနှင့် ဆိုင်သည် မဟုတ်သော", "^1-M2-94")},
    "arupa": {"arūpāvacar": _dw("arūpāvacarā dhammā", "ရုပ်မရှိသော ဘုံနှင့် ဆိုင်သော", "^1-M2-95"),
              "naarūpāvacar": _dw("na arūpāvacarā dhammā", "ရုပ်မရှိသော ဘုံနှင့် ဆိုင်သည် မဟုတ်သော", "^1-M2-95")},
    "pariyapanna": {"pariyāpann": _dw("pariyāpannā dhammā", "ဘဝဘုံတို့၌ အကျုံးဝင်သော", "^1-M2-96"),
                    "apariyāpann": _dw("apariyāpannā dhammā", "ဘဝဘုံတို့၌ အကျုံးမဝင်သော", "^1-M2-96")},
    "niyyanika": {"niyyānik": _dw("niyyānikā dhammā", "လွတ်မြောက်ရာသို့ ပို့ဆောင်သော", "^1-M2-97"),
                  "aniyyānik": _dw("aniyyānikā dhammā", "လွတ်မြောက်ရာသို့ မပို့ဆောင်သော", "^1-M2-97")},
    "niyata": {"niyat": _dw("niyatā dhammā", "ကျိန်းသေသော", "^1-M2-98"),
               "aniyat": _dw("aniyatā dhammā", "မကျိန်းသေသော", "^1-M2-98")},
    "sauttara": {"sauttar": _dw("sauttarā dhammā", "ထိုထက် သာလွန်သည် ရှိသေးသော", "^1-M2-99"),
                 "anuttar": _dw("anuttarā dhammā", "ထိုထက် သာလွန်သည် မရှိသော", "^1-M2-99")},
    "sarana": {"saraṇ": _dw("saraṇā dhammā", "ပဋိပက္ခ ရှိသော", "^1-M2-100"),
               "araṇ": _dw("araṇā dhammā", "ပဋိပက္ခ မရှိသော", "^1-M2-100")},
}
for _d, _tab in DYADS_ADD.items():
    _a, _b = list(_tab)
    _tab[_a + "_" + _b.replace(" ", "_") + "_both"] = f"{_tab[_a]}{C} {_tab[_b]}"
D.DYADS.update(DYADS_ADD)

# dyad heading (level 6) -> dyad
DYAD_OF_ADD = {
    "Kilesadukaṃ": "kil1", "Saṃkilesikadukaṃ": "kil2", "Saṃkiliṭṭhadukaṃ": "kilS", "Kilesasampayuttadukaṃ": "kilP",
    "Kilesasaṃkilesikadukaṃ": "kil4", "Kilesasaṃkiliṭṭhadukaṃ": "kilB", "Kilesakilesasampayuttadukaṃ": "kil5",
    "Kilesavippayuttasaṃkilesikadukaṃ": "kil6",
    "Dassanenapahātabbadukaṃ": "dass", "Bhāvanāyapahātabbadukaṃ": "bhav",
    "Dassanenapahātabbahetukadukaṃ": "dassh", "Bhāvanāyapahātabbahetukadukaṃ": "bhavh",
    "Savitakkadukaṃ": "vitakka", "Savicāradukaṃ": "vicara", "Sappītikadukaṃ": "sappitika",
    "Pītisahagatadukaṃ": "piti", "Sukhasahagatadukaṃ": "sukha", "Upekkhāsahagatadukaṃ": "upekkha",
    "Kāmāvacaradukaṃ": "kama", "Rūpāvacaradukaṃ": "rupa", "Arūpāvacaradukaṃ": "arupa",
    "Pariyāpannadukaṃ": "pariyapanna", "Niyyānikadukaṃ": "niyyanika", "Niyatadukaṃ": "niyata",
    "Sauttaradukaṃ": "sauttara", "Saraṇadukaṃ": "sarana",
}
D.DYAD_OF.update(DYAD_OF_ADD)

# ===================================================================================== names and headings
GOCCHAKA = {"Kilesagocchakaṃ": W("Kilesagocchakaṃ", "ကိလေသာတို့၏ အစု", "1", "^1-M-2-12-0"),
            "Piṭṭhidukaṃ": W("Piṭṭhidukaṃ", "နောက်ဆုံး နှစ်မျိုးတွဲများ", "1", "^1-M-2-13-0")}
_AR = "၏ အာရုံ ဖြစ်နိုင်ခြင်း"
_KS = "ဖြင့် ညစ်နွမ်းခြင်း"
_TK = {k: v for k, v in M.TIKA_ADD.items()} if hasattr(M, "TIKA_ADD") else {}
_DASS_N = _TK["Dassanenapahātabbattikaṃ"][:-len(F.TIKA)] + DUKA          # = 2-03's triad name, «နှစ်မျိုးတွဲ»
_DASSH_N = _TK["Dassanenapahātabbahetukattikaṃ"][:-len(F.TIKA)] + DUKA
# the dyad names (NEW; the pattern of 3-01 … 3-10: «X နှစ်မျိုးတွဲ», «X ရှိခြင်း …», «Xနှင့် ယှဉ်တွဲခြင်း …»,
# «X ဖြစ်ခြင်းနှင့် Y …», «Xနှင့် ကင်းကွာခြင်းနှင့် Y …»)
DUKA_NAME = {
    "Kilesadukaṃ": f"{KIL} {DUKA}",
    "Saṃkilesikadukaṃ": f"{KIL}{_AR} {DUKA}",
    "Saṃkiliṭṭhadukaṃ": f"{KIL}{_KS} {DUKA}",
    "Kilesasampayuttadukaṃ": f"{KIL}နှင့် ယှဉ်တွဲခြင်း {DUKA}",
    "Kilesasaṃkilesikadukaṃ": f"{KIL} ဖြစ်ခြင်းနှင့် {KIL}{_AR} {DUKA}",
    "Kilesasaṃkiliṭṭhadukaṃ": f"{KIL} ဖြစ်ခြင်းနှင့် {KIL}{_KS} {DUKA}",
    "Kilesakilesasampayuttadukaṃ": f"{KIL} ဖြစ်ခြင်းနှင့် {KIL}နှင့် ယှဉ်တွဲခြင်း {DUKA}",
    "Kilesavippayuttasaṃkilesikadukaṃ": f"{KIL}နှင့် ကင်းကွာခြင်းနှင့် {KIL}{_AR} {DUKA}",
    "Dassanenapahātabbadukaṃ": _DASS_N,
    "Bhāvanāyapahātabbadukaṃ": _DASS_N.replace("သစ္စာကို မြင်ခြင်းဖြင့်", "ဘာဝနာ ပွားများခြင်းဖြင့်"),
    "Dassanenapahātabbahetukadukaṃ": _DASSH_N,
    "Bhāvanāyapahātabbahetukadukaṃ": _DASSH_N.replace("သစ္စာကို မြင်ခြင်းဖြင့်", "ဘာဝနာ ပွားများခြင်းဖြင့်"),
    "Savitakkadukaṃ": f"စတင်ကြံစည်မှု ရှိခြင်း {DUKA}",
    "Savicāradukaṃ": f"ဆက်လက်သုံးသပ်မှု ရှိခြင်း {DUKA}",
    "Sappītikadukaṃ": f"ပီတိ ရှိခြင်း {DUKA}",
    "Pītisahagatadukaṃ": f"ပီတိနှင့်အတူ ဖြစ်ခြင်း {DUKA}",
    "Sukhasahagatadukaṃ": f"သာယာမှုနှင့်အတူ ဖြစ်ခြင်း {DUKA}",
    "Upekkhāsahagatadukaṃ": f"ဥပေက္ခာနှင့်အတူ ဖြစ်ခြင်း {DUKA}",
    "Kāmāvacaradukaṃ": f"ကာမဘုံနှင့် ဆိုင်ခြင်း {DUKA}",
    "Rūpāvacaradukaṃ": f"သိမ်မွေ့သော ရုပ်ဘုံနှင့် ဆိုင်ခြင်း {DUKA}",
    "Arūpāvacaradukaṃ": f"ရုပ်မရှိသော ဘုံနှင့် ဆိုင်ခြင်း {DUKA}",
    "Pariyāpannadukaṃ": f"ဘဝဘုံတို့၌ အကျုံးဝင်ခြင်း {DUKA}",
    "Niyyānikadukaṃ": f"လွတ်မြောက်ရာသို့ ပို့ဆောင်ခြင်း {DUKA}",
    "Niyatadukaṃ": f"ကျိန်းသေခြင်း {DUKA}",
    "Sauttaradukaṃ": f"ထိုထက် သာလွန်သည် ရှိခြင်း {DUKA}",
    "Saraṇadukaṃ": f"ပဋိပက္ခ ရှိခြင်း {DUKA}",
}
assert set(DUKA_NAME) == set(DYAD_OF_ADD), set(DUKA_NAME) ^ set(DYAD_OF_ADD)
for _k, _v in DUKA_NAME.items():
    new(_k, _v)
HL_ADD = {}
HL_ADD.update(GOCCHAKA)
HL_ADD.update(DUKA_NAME)
for _k, _v in list(DUKA_NAME.items()) + list(GOCCHAKA.items()):
    HL_ADD[f"{_k} niṭṭhitaṃ."] = F.finished(_v)
HL_ADD["1-6. Paṭiccavārādi"] = new("1-6. Paṭiccavārādi", f"1-6. {F.HEAD['Paṭiccavāro']} {F.ADI}")   # = 3-07 «1-7. …»
HL_ADD["*1-7. Paṭiccavārādi*"] = f"*{B.HL_ADD['1-7. Paṭiccavārādi']}*"
HL_ADD["1-4. Paccayacatukkaṃ"] = G.HLINES["*1-4. Paccayacatukkaṃ*"][1:-1]                   # = 1-03 … 1-05
HL_ADD["4-5. Nissaya-saṃsaṭṭhavāro"] = new(
    "4-5. Nissaya-saṃsaṭṭhavāro", f"4-5. {F.HEAD['Nissayavāro'][:-len(F.VARA)]}နှင့် {F.HEAD['Saṃsaṭṭhavāro']}")
HL_ADD["(Catuttho bhāgo)"] = new("(Catuttho bhāgo)", "(စတုတ္ထ အပိုင်း)")              # = 3-01 «(တတိယ အပိုင်း)»
HL_ADD["Dhammānulome dukapaṭṭhānaṃ niṭṭhitaṃ."] = F.finished(D.HL_ADD["Dhammānulome dukapaṭṭhānaṃ"])


def setup_names():
    F.HLINES.update(HL_ADD)
    for k, v in DUKA_NAME.items():              # a dyad named inside a note («yathā sappītikadukaṃ»)
        K.WORDS_N.setdefault(k[0].lower() + k[1:], v)


# ===================================================================================== Pāli preparation (in memory)
B.GOC["kil"] = ("kiles", "saṃkilesik", "asaṃkilesik")                   # dyads kil1 / kil4 / kil5 / kil6
_A_OF = B._A_OF


def prep_kilB(t):
    """«kilesā ceva saṃkiliṭṭhā ca» / «saṃkiliṭṭhā ceva no ca kilesā» glued to one word (as 3-07 … 3-10's dyad 4)"""
    x, y = "kiles", "saṃkiliṭṭh"
    X, Y = B._ci(x), B._ci(y)
    t = re.sub(_PB + "(" + X + r")\w*?(?:ñceva| ceva) " + re.escape(y) + r"(o|a|assa|ā|āna|e)(?:ñca| ca)" + _NB,
               lambda m: m[1] + "a" + y + "dk" + _A_OF[m[2]], t)
    t = re.sub(_PB + "(" + Y + r")(o|a|aṃ|assa|ā|āna|e)(?:ñceva| ceva) no ca " + re.escape(x) +
               r"(añca|ādhipati|o|aṃ|assa|ā|ānaṃ|e)" + _NB, lambda m: m[1] + "ano" + x + "dk" + _A_OF[m[3]], t)
    return D._pairfix(t, x + "a" + y + "dk", y + "ano" + x + "dk")


# readings for the parser (in memory; logged in the notes):
# «A, B, Xassa ca §C§» (a comma before the last recipient, which takes «ca»): read «A, B Xassa ca» (the 2-03 … 2-06
# reading «āvajjanāya mohassa ca»: the last two members coordinated)
_FAC_G = "vitakkassa|pītiyā|sukhassa|upekkhāya"
_COMMA_CA = re.compile(r"(?<=ssa|āya|iyā), (" + _FAC_G + r") ca(?= )")
# «Xñca vitakko ca …» / «Xñca sukhañca …» (the enclitic written together): read «Xṃ ca vitakko ca» (= 2-01 … 2-02 NCA)
_NCA = re.compile(r"(?<!\w)(?!khandh)(\w+?)añca (?=(?:vitakko|pīti|upekkhā) ca(?!\w)|sukhañca(?!\w))")
_SUKHA_CA = re.compile(r"(aṃ ca |dhātu ca |senāsanaṃ )sukhañca(?!\w)")
READ = {"pīti ca cittasamuṭṭhānañca rūpaṃ": "pīti cittasamuṭṭhānañca rūpaṃ",     # (as «vitakko cittasamuṭṭhānañca»)
        # «khandhā ca sukhañca pacchim…» (anantara): «sukhaṃ» is the nominative here (a parser token, as «vitakko»)
        "khandhā ca sukhañca pacchim": "khandhā ca sukhaṃ_n ca pacchim"}
READ_LOG = set()
# source slip: «…pe… novigatapaccayena paccayo» closing an anuloma list (bhāvanāya pahātabbahetuka, pañhāvāra; the
# other dyads close with «avigatapaccayena paccayo»): translated as written, the negative frame «… ဖြစ်သည် မဟုတ်»
SLIP_READ = {"…pe… novigatapaccayena paccayo.": "…pe… na vigatapaccayena paccayo."}


# coordinator decision H7: «Sahajātā –» naming a kind of kamma (in a kamma sentence «Sahajātā – X cetanā …
# kammapaccayena paccayo», or right after the kinds «sahajātā, nānākkhaṇikā.») = «အတူ ပေါ်ပေါက်သည့် ကံ –», also
# where the kamma passage has no «*Kammapaccayo*» heading (the engine reads the section from that heading only); the
# atthi / vippayutta kinds stay the bare name. The label is marked with a parser token (LEX = the module's «sahajātā»).
_KAMMA_LABEL = re.compile(r"(?<![\wāīūṃṅñṭḍṇḷ])Sahajātā(?= –[^.;]*?kammapaccayena paccayo)|"
                          r"(?<=nānākkhaṇikā\. )Sahajātā(?= –| \()")


def prep_mine(t):
    t = _KAMMA_LABEL.sub("Sahajātākamma", t)
    for a, b in SLIP_READ.items():
        if a in t:
            F.SLIPS.add(f"«{a}» read as «{b}» (as written: no-vigata)")
            t = t.replace(a, b)
    for a, b in READ.items():
        if a in t:
            READ_LOG.add(f"«{a}» parsed as «{b}»")
            t = t.replace(a, b)
    for rx, rep, tag in ((_COMMA_CA, r" \1 ca", "comma before the last «X ca» recipient"),
                         (_NCA, r"\1aṃ ca ", "«Xñca» before a factor «ca» split"),
                         (_SUKHA_CA, r"\1sukhaṃ ca", "«sukhañca» split")):
        t2 = rx.sub(rep, t)
        if t2 != t:
            READ_LOG.add(tag)
            t = t2
    return t


def _prep_dyad(t, d):
    if d not in DYADS_ADD:                     # another group's dyad (--regress): its own preparation only
        return _PREV_PREP(t, d)
    t = prep_mine(t)
    t = _CA_GEN.sub(" ca ", t)
    if d == "kilB":
        t = prep_kilB(t)
    return _PREV_PREP(t, d)


def _set_dyad(mod, d):
    _PREV_SET(mod, d)
    if d and d[:3] == "kil":
        mod.TRIAD_END[d] = B.MY_END
        mod.rebuild()


# ===================================================================================== nouns and lexicon
# the kilesa noun (pi-1 ^1-M2-75) and the ten kilesas (pi-1 ^1-1565)
_KILW = {"lobh": "လောဘ", "dos": "ဒေါသ", "moh": "မောဟ", "mān": "မာန", "diṭṭh": "အယူ", "vicikicch": "ယုံမှားမှု",
         "thin": "ထိုင်းမှိုင်းမှု", "uddhacc": "ယောက်ယက်ခတ်မှု", "ahirik": "ဒုစရိုက်ကို မရှက်မှု",
         "anottapp": "ဒုစရိုက်ကို မကြောက်ရွံ့မှု"}
for _k, _v in _KILW.items():
    W({"diṭṭh": "diṭṭhi", "vicikicch": "vicikicchā", "thin": "thinaṃ", "uddhacc": "uddhaccaṃ", "ahirik": "ahirikaṃ",
       "anottapp": "anottappaṃ"}.get(_k, _k + "o"), _v, "1", "^1-1565")
_NF = B._NF
# Pāli forms of each kilesa (case, plural, LEX kind)
_KIL_FORMS = {
    "lobh": {"o": ("n", "n"), "aṃ": ("a", "a"), "assa": ("g", "g")},
    "dos": {"o": ("n", "n"), "aṃ": ("a", "a"), "assa": ("g", "g")},
    "moh": {"o": ("n", "n"), "aṃ": ("a", "a"), "assa": ("g", "g")},
    "mān": {"o": ("n", "n"), "aṃ": ("a", "a"), "assa": ("g", "g")},
    "diṭṭh": {"i": ("n", "n"), "iṃ": ("a", "a"), "iyā": ("g", "g")},
    "vicikicch": {"ā": ("n", "n"), "aṃ": ("a", "a"), "āya": ("g", "g")},
    "thin": {"aṃ": ("a", "na"), "assa": ("g", "g")},
    "uddhacc": {"aṃ": ("a", "na"), "assa": ("g", "g")},
    "ahirik": {"aṃ": ("a", "na"), "assa": ("g", "g")},
    "anottapp": {"aṃ": ("a", "na"), "assa": ("g", "g")},
}


# the jhāna factors as nouns (pi-1 ^1-M2-87 … ^1-M2-92 «စတင်ကြံစည်မှု», «ဆက်လက်သုံးသပ်မှု», «ပီတိ», «သာယာမှု»,
# «ဥပေက္ခာ»): (Burmese, {Pāli form: (case, plural, LEX kind)})
VITAKKA = W("vitakko", "စတင်ကြံစည်မှု", "1")
VICARA = W("vicāro", "ဆက်လက်သုံးသပ်မှု", "1")
PITI = W("pīti", "ပီတိ", "1")
SUKHA = F.LEX["sukhaṃ"][0]
UPEKKHA = W("upekkhā", "ဥပေက္ခာ", "1")
_FAC = {
    VITAKKA: {"vitakko": ("n", False, "n"), "vitakkaṃ": ("a", False, "a"), "vitakkassa": ("g", False, "g")},
    VICARA: {"vicāro": ("n", False, "n"), "vicāraṃ": ("a", False, "a"), "vicārassa": ("g", False, "g")},
    PITI: {"pīti": ("n", False, "n"), "pītiṃ": ("a", False, "a"), "pītiyā": ("g", False, "g")},
    SUKHA: {"sukhaṃ": ("a", False, "na"), "sukhassa": ("g", False, "g")},
    UPEKKHA: {"upekkhā": ("n", False, "n"), "upekkhaṃ": ("a", False, "a"), "upekkhāya": ("g", False, "g")},
}


MICCHA_N = W("micchattaniyatā dhammā", "မှားယွင်းမှု၌ ကျိန်းသေသော", "1")
# the heinous deeds as in pi-5 (coordinator decision; pi-5 ^5-… «အမိကို သတ်ခြင်း ကံ» …): these four LEX values of the
# module («… သတ်သော ကံ», 1-01) are replaced IN MEMORY for this chapter only
_DEEDS5 = {"mātughātikamm": W("mātughāta", "အမိကို သတ်ခြင်း ကံ", "5"),
           "pitughātikamm": W("pitughāta", "အဖကို သတ်ခြင်း ကံ", "5"),
           "arahantaghātikamm": W("arahantaghāta", "ရဟန္တာကို သတ်ခြင်း ကံ", "5"),
           "ruhiruppādakamm": W("ruhiruppāda", "ဘုရား၏ ကိုယ်တော်မှ သွေးကို ထွက်စေခြင်း ကံ", "5"),
           "saṅghabhedakamm": W("saṅghabhedakammassa", "သံဃာကို သင်းခွဲခြင်း ကံ", "5")}
LEX_OVERRIDE = set()
LEX_ADD = []
for _st, _my in _DEEDS5.items():
    for _w, _k, _sfx in ((_st + "aṃ", "n", ""), (_st + "assa", "g", ""), (_st + "assa ca", "x", "အားလည်းကောင်း")):
        LEX_ADD.append((_w, _my + _sfx, _k))
        LEX_OVERRIDE.add(_w)
LEX_ADD += [
    ("uddhacca", "ယောက်ယက်ခတ်မှု", "n"),                        # «uddhacca…» (cut short by «…»; the module's uddhaccaṃ)
    ("vikkhambhite", "ခွာထားပြီးသော", "x"),                     # cut by «…» (= 3-03 … 3-06)
    ("dibbena", "နတ်", "x"),                                     # «dibbena…» cut short (the module's «dibbena cakkhunā»)
    ("domanassassa", "စိတ်ဆင်းရဲမှု", "g"),                       # (the module's domanassaṃ)
    ("ekaṃyeva", "တစ်ခုတည်း", "x"),                               # (3-07 … 3-10 «ekaṃyeva» «… တစ်ခုတည်း»)
    ("nava pañhā", f"{K.PANHA} {F.COUNT['nava']}", "x"),
    ("sukhaṃ_n", F.LEX["sukhaṃ"][0], "n"),                        # parser token (READ), the module's sukhaṃ
    ("sahajātākamma", F.LEX["sahajātā"][0], "x"),                  # parser token (the kamma label), = «sahajātā»
    ("dibbaṃ cakkhuṃ", F.LEX["dibbacakkhu"][0], "a"),             # (the module's dibbacakkhu / dibbasotadhātu)
    ("dibbaṃ sotadhātuṃ", F.LEX["dibbasotadhātu"][0], "a"),
    ("kāyaviññāṇaṃ", F.KAYAVINNANA, "na"),                        # = 2-01 … 2-02
    ("rūpajīvitindriyaṃ", D.RJIVIT, "n"),                         # (the module's FIXED rūpajīvitindriyaṃ)
] + [(_w.replace("ppaṭisambhidāya", "paṭisambhidāya"), F.LEX[_w][0], F.LEX[_w][1]) for _w in
     ("atthappaṭisambhidāya", "dhammappaṭisambhidāya", "niruttippaṭisambhidāya")]   # spelt with one «p» here
for _w, _my, _k in LEX_ADD:
    if _w not in LEX_OVERRIDE:
        new(_w, _my)


# «mānaṃ» is not made a FIXED noun: the module's noun parser would then read it inside «dhammānaṃ» (the sample's
# «… taṃsampayuttakānañca dhammānaṃ» stops); it stays a LEX word
_NO_FIXED = {"mānaṃ"}


def setup_lex():
    for mod in (F, FG):
        for my, forms in _FAC.items():
            for w, (case, pl, lk) in forms.items():
                mod.add_fixed(my, case, pl, w)
                mod.NOUN.setdefault(w, (my, case, pl))
                mod.LEX.setdefault(w, (my, lk))
        mod.add_qual(mod.QUAL["pacchimassa pacchimassa"], "pacchimāya pacchimāya")
        mod.add_qual(mod.AHETUKA, "ahetuke")
        mod.add_fixed(SUKHA, "n", False, "sukhaṃ_n")                       # the READ token (nominative sukhaṃ)
        mod.NOUN.setdefault("sukhaṃ_n", (SUKHA, "n", False))
        mod.add_qual(mod.VIPAKA_ADJ, "vipākaṃ", "vipāke")                  # = «vipāko» (the sample)
        mod.add_qual(DYADS_ADD["piti"]["pītisahagat"], "pītisahagatā")     # outside its own dyad (pi-1 ^1-M2-90)
        mod.add_qual(MICCHA_N, "micchattaniyatā", "micchattaniyatānaṃ")
        for w, my, k in LEX_ADD:
            mod.LEX[w] = (my, k) if w in LEX_OVERRIDE else mod.LEX.get(w, (my, k))
    for mod in (F, FG):
        for e, (case, pl, lk) in _NF.items():
            w = "kiles" + e
            mod.add_fixed(KIL, case, pl, w)
            mod.NOUN.setdefault(w, (KIL, case, pl))
            mod.LEX.setdefault(w, (KIL + ("+" if pl else ""), lk))
        for st, forms in _KIL_FORMS.items():
            my = _KILW[st]
            for e, (case, lk) in forms.items():
                w = st + e
                if w not in _NO_FIXED:
                    mod.add_fixed(my, case, False, w)
                mod.LEX.setdefault(w, (my, lk))
    setup_coord()
    # «kilesā ca sampayuttakā khandhā ca» … (as 3-07 … 3-10; the module renders them once)
    for st in ["kiles"] + list(_KIL_FORMS):
        for ph, role in ((f"{st}ā ca sampayuttakā khandhā ca", "n"), (f"{st}o ca sampayuttakā khandhā ca", "n"),
                         (f"{st}añca sampayuttake khandhe ca", "@ārabbha"),
                         (f"{st}e ca sampayuttake khandhe ca", "@ārabbha")):
            try:
                my = F.np_my(ph.split(), iter([]), role)[0]
            except (KeyError, StopIteration):
                continue
            for mod in (F, FG):
                mod.LEX.setdefault(ph, (my, "x"))
        for ph in (f"{st}ānaṃ sampayuttakānañca khandhānaṃ", f"{st}assa sampayuttakānañca khandhānaṃ"):
            try:
                my = F.np_my(ph.split(), iter([]), "g")[0]
            except (KeyError, StopIteration):
                continue
            for mod in (F, FG):
                mod.LEX.setdefault(ph, (my, "x"))
                if "assa " in ph:
                    mod.LEX.setdefault(ph.replace("assa ", "assa ca "), (my, "x"))


# nominative, accusative, genitive of the single nouns that are coordinated with khandhas («khandhe ca vitakkañca»,
# «khandhā ca vitakko ca», «khandhānaṃ (ca) vitakkassa ca», «vitakko ca sampayuttakā khandhā ca» …)
COORD = {VITAKKA: ("vitakko", "vitakkaṃ", "vitakkassa"), VICARA: ("vicāro", "vicāraṃ", "vicārassa"),
         PITI: ("pīti", "pītiṃ", "pītiyā"), SUKHA: ("sukhaṃ", "sukhaṃ", "sukhassa"),
         UPEKKHA: ("upekkhā", "upekkhaṃ", "upekkhāya"),
         KIL: ("kileso", "kilesaṃ", "kilesassa")}
for _st, _f in _KIL_FORMS.items():
    _n = [e for e, v in _f.items() if v[0] == "n"]
    COORD[_KILW[_st]] = (_st + (_n[0] if _n else "aṃ"), _st + [e for e, v in _f.items() if v[0] == "a"][0],
                         _st + [e for e, v in _f.items() if v[0] == "g"][0])
_GEN_CA = "|".join(re.escape(g) for _, _, g in COORD.values())
# «… khandhānaṃ vitakkassa ca» (one «ca» after the last member): read as «khandhānaṃ ca vitakkassa ca» (as 2-03 … 2-06
# «khandhānaṃ mohassa ca», 3-07 … 3-10 «khandhānaṃ lobhassa ca»)
_CA_GEN = re.compile(r"(?<= khandhānaṃ) (?=(?:" + _GEN_CA + r") ca" + _NB + ")")


def _ca(w):
    return w[:-1] + "ñca" if w.endswith("ṃ") else w + " ca"


COORD_SKIPPED = []


def setup_coord():
    kh, lk = F.KHANDHA, F.LAKAUNG
    for my, (n, a, g) in COORD.items():
        rows = [(f"khandhe ca {_ca(a)}", f"{kh}တို့ကို{lk}{C} {my}ကို{lk}"),
                (f"khandhānaṃ ca {g} ca", f"{kh}တို့အား{lk}{C} {my}အား{lk}"),
                (f"khandhā ca {_ca(n)}", None, "n"),
                (f"{_ca(n)} sampayuttakā khandhā ca", None, "n"),
                (f"{_ca(a)} sampayuttake khandhe ca", None, "@ārabbha"),
                (f"{g} sampayuttakānañca khandhānaṃ", None, "g")]
        for r in rows:
            ph, my_ = r[0], r[1]
            if my_ is None:
                try:
                    my_ = F.np_my(ph.split(), iter([]), r[2])[0]
                except (KeyError, StopIteration):
                    COORD_SKIPPED.append(ph)          # not renderable by the module (and not in this chapter)
                    continue
            for mod in (F, FG):
                mod.LEX.setdefault(ph, (my_, "x"))
                if ph.startswith(g + " sampayuttakānañca"):       # «Xassa ca sampayuttakānañca …»: the same members
                    mod.LEX.setdefault(ph.replace(g + " ", g + " ca ", 1), (my_, "x"))


# ===================================================================================== coordination in the lexicon frame
# (copied from make_ch2-01-02.py (b), the group that first rendered vitakka / pīti coordinations; used here ONLY where
# the engine's own lexicon frame fails, so every sentence the engine already renders keeps its Burmese):
# «A ca B ca» and «A B ca» (A, B = [terms] + one LEX item of the same case) become one item rendered as the module's
# coordination «Aလည်းကောင်း၊ Bလည်းကောင်း» (nominative), «Aအားလည်းကောင်း၊ …» (recipient), «Aကိုလည်းကောင်း၊ …» (object)
_CASE_MARK = {"n": "", "g": "အား", "a": "ကို", "na": "ကို", "i": "ဖြင့်", "G": "၏"}
_GROUP_N = [0]
_LEX0 = None


def _conjunct(words, end):
    for n in (3, 2, 1):
        st = end - n
        if st < 0:
            continue
        key = " ".join(words[st:end])
        if key in F.LEX and F.LEX[key][1] in _CASE_MARK:
            my, kind = F.LEX[key]
            k = st
            while k > 0 and words[k - 1].startswith("§T§") and words[k - 1][3:] in F.TERM_TAIL_OK:
                k -= 1
            pl = my.endswith("+")
            return k, kind, my[:-1] if pl else my, pl, st - k
    return None


def _compat(k1, k2):
    return k1 == k2 or {k1, k2} in ({"n", "na"}, {"a", "na"})


# a group whose members are all nominative-or-accusative («cuticittaṃ ca sukhaṃ ca …»): accusative only before an
# object word (ārabbha, garuṃ katvā, paṭicca …), otherwise nominative (the subject of «… §C§ena paccayo»)
# (2-01 … 2-02's copy takes «ကို» for such a group; here the case follows the next word)
_OBJ_NEXT = {"ārabbha", "garuṃ", "paṭicca", "paccayā", "nissāya", "upanissāya", "aniccato", "paccavekkhati",
             "paccavekkhanti", "assādeti", "vipassati", "jānāti", "jānanti", "saṃsaṭṭhā", "sampayuttā", "sahajātā"}


def _group_my(items, tvals, nxt_word=None):
    out, ti = [], 0
    kinds = {it[1] for it in items}
    if kinds <= {"na"} and (nxt_word or "").rstrip(",.;") not in _OBJ_NEXT:
        kinds = {"n"}
    for (_, kind, my, pl, nt) in items:
        pre = " ".join(tvals[ti:ti + nt])
        ti += nt
        mark = "" if "n" in kinds else _CASE_MARK[kind]
        num = re.search(r" (?:" + "|".join(F.PAA.values()) + r")$", my)
        out.append((pre + " " if pre else "") + my + ("တို့" if pl and mark and not num else "") + mark + F.LAKAUNG)
    return (C + " ").join(out)


def _lex_coord(frag, slots, ti, ci, ki, di, vi):
    lead = frag[:len(frag) - len(frag.lstrip())]
    words = frag.strip().split(" ")
    tpos = {}
    for i, w in enumerate(words):
        if w.startswith("§T§"):
            tpos[i] = len(tpos)
    groups = []
    i = 0
    while i < len(words):
        if words[i] != "ca":
            i += 1
            continue
        b = _conjunct(words, i)
        if b is None:
            raise KeyError("lex coordination: " + " ".join(words))
        items, st, end = [b], b[0], i + 1
        while True:
            e = next((e for e in range(end + 1, min(end + 12, len(words))) if words[e] == "ca"), None)
            c = _conjunct(words, e) if e is not None else None
            if c is None or c[0] != end:
                break
            items.append(c)
            end = e + 1
        if len(items) == 1:
            a = _conjunct(words, st)
            if a is None or not _compat(a[1], b[1]) or (groups and groups[-1][1] > a[0]):
                raise KeyError("lex coordination: " + " ".join(words))
            items.insert(0, a)
            st = a[0]
        groups.append((st, end, items))
        i = end
    new_words, used_t = [], 0
    gi, i = 0, 0
    tvals = slots["T"][ti[0]:]
    rem = []
    while i < len(words):
        if gi < len(groups) and i == groups[gi][0]:
            st, end, items = groups[gi]
            idx = [tpos[k] for k in range(st, end) if k in tpos]
            key = f"§G{_GROUP_N[0]}§"
            _GROUP_N[0] += 1
            nxt = gi + 1 < len(groups) and groups[gi + 1][0] == end
            F.LEX[key] = (_group_my(items, [tvals[j] for j in idx], words[end] if end < len(words) else None)
                          + (C if nxt else ""), "x")
            new_words.append(key)
            used_t += len(idx)
            i = end
            gi += 1
            continue
        if i in tpos:
            rem.append(tvals[tpos[i]])
        new_words.append(words[i])
        i += 1
    sl = dict(slots)
    sl["T"] = rem
    t2 = [0]
    try:
        r = _LEX0(lead + " ".join(new_words), sl, t2, ci, ki, di, vi)
    finally:
        for k in [k for k in F.LEX if k.startswith("§G")]:
            del F.LEX[k]
    ti[0] += t2[0] + used_t
    return r


COORD_USED = collections.Counter()


def lex(frag, slots, ti, ci, ki, di, vi):
    saved = [c[0] for c in (ti, ci, ki, di, vi)]
    try:
        return _LEX0(frag, slots, ti, ci, ki, di, vi)
    except KeyError:
        if " ca " not in f" {frag.strip()} ":
            raise
        for c, v in zip((ti, ci, ki, di, vi), saved):
            c[0] = v
    r = _lex_coord(frag, slots, ti, ci, ki, di, vi)
    COORD_USED[frag.strip()] += 1
    return r


# ===================================================================================== editorial notes
CNT = F.COUNT
KAT, VITTH, GAN, VIBHAJ = K.KATABBA, K.VITTH, K.GANETABBA, M.VIBHAJ
EVAM_T, EVAM, KAYYA, SADISANI, SADISA = D.EVAM_T, K.EVAM, K.KAYYA, K.SADISANI, F.SADISA
PANHA, NATTHI, PARIP, SAB = K.PANHA, K.NATTHI, K.PARIPUNNA, D.SAB
CAKKA, ITARE, NINNANAKARANA, NINNANA = D.CAKKA, D.ITARE, D.NINNANAKARANA, K.NOTE_FIXED["ninnānaṃ"]
SAMKH = F.NOTES["(saṃkhittaṃ)"][1:-1]
VARA, PATICCA_V, _pi, _pi_obj = D.VARA, D.PATICCA_V, D._pi, D._pi_obj
DN = DUKA_NAME


GANANA, GHATANA, PADA, DHAMMA = S.GANANA, F.GHATANA, F.PADA, F.DHAMMA
AVAJJ, VUTTH = F.LEX["āvajjanā"][0], F.LEX["vuṭṭhānassa"][0]
ADH = F.N["adhipati"]
AVAS_O, ARUPA_N, ARUPE = B.AVAS_O, D.ARUPA_N, F.PREFIX["arūpe"]
AJJH, MAHAB, YAVA_AS = D.AJJH, D.MAHAB, D.YAVA_AS
AMASANA, ARABBHA, NAKAT, VARAS = B.AMASANA, B.ARABBHA, B.NAKAT, B.VARAS
ANUL_MATIKA, IHA, MULA, NIYAM, PAV_PS, PAVATTE = D.ANUL_MATIKA, D.IHA, D.MULA, D.NIYAM, D.PAV_PS, D.PAVATTE
CULA, LOKIYA = B.CULA, B.LOKIYA
DK_LOK = f"{CULA}၌ {LOKIYA}"
GAMANA = M.GAMANA
ORD, ORDL = K.ORDER_N, K.ORDER_L
PACC_VIBH = f"{ORD['paccanīyaṃ']}၏ {ORD['vibhaṅgo']}"
PS_KHANA = F.LEX["paṭisandhikkhaṇe"][0]
MOHA, DOSA = D.ROOT_N["moh"], D.ROOT_N["dos"]
PANCAV = B.NEW["pañca viññāṇā"]                                        # «သိစိတ် ငါးပါး» (3-10)
NANAKK = F.LEX["nānākkhaṇikā"][0]                                       # «ခဏ ကွဲပြားသည့် ကံ» (1-01)
SAH_KAMMA = new("sahajātā (a kind of kamma, in a note)", "အတူ ပေါ်ပေါက်သည့် ကံ")   # coordinator decision H7
UDDH_SAH, VICI_SAH = F.QUAL["uddhaccasahagate"], F.QUAL["vicikicchāsahagato"]
PAVATTI = new("pavatti", "ဘဝ ဖြစ်စဉ်")                                  # (D «pavatte» «ဘဝ ဖြစ်စဉ်၌»)
AHET_S = F.AHETUKA[:-len("သော")] + "သည်"                                 # «ahetukanti» (3-01 … 3-02)
AHET_P = new("ahetukā (inside a note, plural)", F.AHETUKA[:-len("သော")] + "ကြသည်")
UDDHAR = new("uddharitabbo", "ထုတ်နုတ်ရမည်")                              # (1-01 paccanīyuddhāro «… ထုတ်နုတ်ချက်»)
THAPET = new("ṭhapetabbo", "ထားရမည်")
ATIREKA = new("atirekā", "ပိုသည်")
LIKHITA = new("likhita", "ရေးထားသော")                                    # (2-03 … 2-06 «na likhitā» «မရေးထားသော»)
PACCAVEKKH = B.NEW["paccavekkhitvā"]
PARANTENA = new("parantena", "အဆုံးပိုင်း၌")
# «sakabhaṇḍachandarāgo» = 2-03 … 2-06's «sakabhaṇḍe chandarāgo» «မိမိ ပစ္စည်း၌ ဖြစ်သော ဆန္ဒရာဂ» (its SK; pi-2's termbase
# has chandarāgo «လိုလားမှု ရာဂ»: logged for the harmonise pass)
SAKABH = new("sakabhaṇḍachandarāgo", F.SK["sakabhaṇḍe chandarāgo parabhaṇḍe chandarāgassa §C§ena paccayo"].split("သည် ")[0])
VIMATI = W("vimati", "စိတ်ရှုပ်ထွေးခြင်း", None)
YADIPI = new("yadipi … (concessive)", "အကယ်၍")
NANAPADA = new("nānāpadāyeva", "ကွဲပြားသော ပုဒ်များပင်")
PAKATIKA = new("pākatikā", "ပကတိအတိုင်း")                                 # (3-01 … 3-02 pakatikāyeva «ပကတိအတိုင်းပင်»)
GAHET = new("gahetabbā", "ယူရမည်")
BHAJANA = new("bhājanakāraṇe", "ခွဲခြားသည့် နည်းလမ်း၌")                    # (iminā kāraṇena «ဤနည်းလမ်းဖြင့်»)
LABHATI = new("labbhati", "ရသည်")
VIBHAGA = new("vibhāgo", "ခွဲခြားချက်")
KARANENA = new("-karaṇena (by the treatment of)", "ပြုပုံအတိုင်း")
DATTH = new("daṭṭhabbaṃ", "ရှုရမည်")
LEKHA = new("lekhaṃ", "စာ")
PASSITVA = new("passitvā", "ကြည့်၍")
BHAVANA = new("bhāvanā (inside a note)", "ဘာဝနာ ပွားများခြင်း")             # (the term «ဘာဝနာ ပွားများခြင်းဖြင့်»)
MISSAKE = new("missake", "ရောနှောသော အပိုင်း၌")
SUDDHIKE = D.SUDDHAKE                                                    # suddhike = suddhake «ရိုးရိုး အပိုင်း၌»
SAMEN = new("na sameti", "မညီ")                                         # (2-03 … 2-06 «na samenti» «မညီကြ»)
ARUPAD = new("arūpaduka (inside a note)", f"ရုပ်မရှိသော ဘုံ {DUKA}")       # as written («arūpa» = «ရုပ်မရှိသော ဘုံ»)
KILD = DN["Kilesadukaṃ"]
DASSD, DASSHD = DN["Dassanenapahātabbadukaṃ"], DN["Dassanenapahātabbahetukadukaṃ"]
SAVD, SAVICD, SAPD = DN["Savitakkadukaṃ"], DN["Savicāradukaṃ"], DN["Sappītikadukaṃ"]
PITID, SUKD, ARUD, NIYYD = DN["Pītisahagatadukaṃ"], DN["Sukhasahagatadukaṃ"], DN["Arūpāvacaradukaṃ"], DN["Niyyānikadukaṃ"]
T = {d: DYADS_ADD[d] for d in DYADS_ADD}
NOKIL = T["kil1"]["nokiles"]
NBH = T["bhav"]["nabhāvanāya pahātabb"]
NBH_HT, BHH_T = T["bhavh"]["nabhāvanāya pahātabbahetuk"], T["bhavh"]["bhāvanāya pahātabbahetuk"]
SAVIT, SAPT, NAKAMA = T["vitakka"]["savitakk"], T["sappitika"]["sappītik"], T["kama"]["nakāmāvacar"]
ALL6 = ("paṭicca", "sahajāta", "paccaya", "nissaya", "saṃsaṭṭha", "sampayutta")


def _notep_mine():
    cn, cd, N = F.cname, F.cond, F.N
    nine, two, three, four = CNT["nava"], CNT["dve"], CNT["tīṇi"], CNT["cattāri"]
    lok = F.cname("upanissaya") + "၌ " + B.LOKUTTARA + " " + NATTHI
    return {
        # kilesa dyads
        "(arūpe dosamūlakaṃ natthi)": f"({ARUPE} {DOSA}{F.MULAKA} {NATTHI})",
        "(evaṃ navapi pañhā kātabbā)": f"({EVAM_T} {PANHA} {nine}လုံးကို {KAT})",
        "(Evaṃ sabbe paccayā kātabbā.)": f"({EVAM_T} {F.PACCAYA} {SAB}ကို {KAT}{END})",
        "(Evaṃ itare dve gaṇanāpi sahajātavāropi kātabbo.)":
            f"({EVAM_T} {ITARE} {GANANA} {two}ကိုလည်း{C} {VARA('sahajāta')}ကိုလည်း {KAT}{END})",
        "(Ārammaṇapaccaye nokilesamūle pañca viññāṇā kātabbā.)":
            f"({cd('ārammaṇa', 'loc')} {NOKIL} {DHAMMA}{F.MULAKA}၌ {PANCAV}ကို {KAT}{END})",
        "(Cakkaṃ. Evaṃ nava pañhā kātabbā.)": f"({CAKKA}{END} {EVAM_T} {PANHA} {nine}ကို {KAT}{END})",
        "(evaṃ nahetupañhā cattāri kātabbā.)": f"({EVAM_T} {cd('hetu', 'n', True)}၏ {PANHA} {four}ကို {KAT}{END})",
        "(saṃkhittaṃ. Vitthāretabbaṃ.)": f"({SAMKH}{END} {VITTH}{END})",
        # (the engine's own note frame names the first condition «…ဟူသော အကြောင်းသည်»; written as 3-07 … 3-10's
        # «(imesu sahajātaṃ sahajātasadisaṃ, …)» with the bare names)
        "(sahajātaṃ sahajātasadisaṃ, purejātaṃ purejātasadisaṃ.)":
            f"({N['sahajāta']}သည် {N['sahajāta']}{SADISA}{C} {N['purejāta']}သည် {N['purejāta']}{SADISA}{END})",
        "(saṃkhittaṃ. Sahajātaṃ sahajātasadisaṃ, purejātaṃ purejātasadisaṃ.)":
            (f"({SAMKH}{END} {N['sahajāta']}သည် {N['sahajāta']}{SADISA}{C} {N['purejāta']}သည် "
             f"{N['purejāta']}{SADISA}{END})"),
        "(yathā lokiyadukaṃ, evaṃ ninnānākaraṇaṃ.)": f"({LOKIYA}{KAYYA} {EVAM} {NINNANAKARANA}{END})",
        "(Yathā lokiyadukaṃ, evaṃ ninnānākaraṇaṃ.)": f"({LOKIYA}{KAYYA} {EVAM} {NINNANAKARANA}{END})",
        "(Kilesasampayuttadukaṃ saṃkiliṭṭhadukasadisaṃ, ninnānākaraṇaṃ.)":
            f"({DN['Kilesasampayuttadukaṃ']}သည် {DN['Saṃkiliṭṭhadukaṃ']}{SADISA}{C} {NINNANAKARANA}{END})",
        "(Evaṃ paṭiccavāropi sahajātavāropi paccayavāropi nissayavāropi saṃsaṭṭhavāropi sampayuttavāropi "
        "kilesadukasadisā. Ninnānākaraṇaṃ. Āmasanaṃ nānaṃ.)":
            (f"({EVAM_T} {_pi(*ALL6)} {KILD}{SADISANI}{END} {NINNANAKARANA}{END} {AMASANA}သည် {K.NANAKARANA} "
             f"ဖြစ်သည်{END})"),
        "(evaṃ cattāri, kilesadukasadisaṃ.)": f"({EVAM_T} {four}{C} {KILD}{SADISA}{END})",
        "(itare dve kilesadukasadisā, ghaṭanārammaṇāpi kilesadukasadisā)":
            f"({ITARE} {two}သည် {KILD}{SADISANI}{C} {GHATANA} {N['ārammaṇa']}တို့သည်လည်း {KILD}{SADISANI})",
        "(Itare dvepi kilesadukasadisā. Ghaṭanādhipatipi.)":
            f"({ITARE} {two}လုံးလည်း {KILD}{SADISANI}{END} {GHATANA} {ADH}လည်း{END})",
        "(kilesadukasadisā)": f"({KILD}{SADISANI})",
        "(Itare dve anantarā kilesadukasadisā, ninnānākaraṇā. Ghaṭanānantarampi sabbe paccayā kilesadukasadisā, "
        "ninnānākaraṇā. Upanissaye lokuttaraṃ natthi, idaṃ dukaṃ kilesadukasadisaṃ, ninnānākaraṇaṃ.)":
            (f"({ITARE} {N['anantara']} {two}သည် {KILD}{SADISANI}{C} {NINNANAKARANA}{END} {GHATANA} "
             f"{N['anantara']}လည်း{C} {F.PACCAYA} {SAB}တို့သည် {KILD}{SADISANI}{C} {NINNANAKARANA}{END} {lok}{C} "
             f"ဤ {DUKA}သည် {KILD}{SADISA}{C} {NINNANAKARANA}{END})"),
        "(Evaṃ itare dve gaṇanāpi sahajātavāropi paccayavāropi nissayavāropi saṃsaṭṭhavāropi sampayuttavāropi "
        "paṭiccavārasadisā.)":
            (f"({EVAM_T} {ITARE} {GANANA} {two}လည်း{C} {_pi(*ALL6[1:])} {PATICCA_V}{SADISANI}{END})"),
        "(Itarepi tīṇi kātabbā.)": f"({ITARE} {three}ကိုလည်း {KAT}{END})",
        "(Dve adhipati tīṇipi kātabbā, itare dvepi tīṇi kātabbā.)":
            f"({ADH} {two}၌ {three}လုံးကို {KAT}{C} {ITARE} {two}လုံး၌လည်း {three}ကို {KAT}{END})",
        "(navapi kātabbā, āvajjanāpi vuṭṭhānampi natthi)":
            f"({nine}လုံးကို {KAT}{C} {AVAJJ}လည်း{C} {VUTTH}လည်း {NATTHI})",
        "(purejātapaccayo pacchājātapaccayopi natthi)": f"({cn('purejāta')}{C} {cn('pacchājāta')}လည်း {NATTHI})",
        "(Navapi, tīṇiyeva padā kātabbā.)": f"({nine}လုံး{C} {PADA} {three}ကိုသာ {KAT}{END})",
        "(Kilesasaṃkiliṭṭhadukasadisaṃ ninnānākaraṇaṃ, sabbe vārā.)":
            f"({DN['Kilesasaṃkiliṭṭhadukaṃ']}{SADISA}{C} {NINNANAKARANA}{C} {VARAS} {SAB}{END})",
        # piṭṭhiduka: dassanena / bhāvanāya pahātabba (-hetuka)
        "(Itare dve gaṇanāpi sahajātavāropi kātabbo.)":
            f"({ITARE} {GANANA} {two}ကိုလည်း{C} {VARA('sahajāta')}ကိုလည်း {KAT}{END})",
        "(Itare dve gaṇanāpi nissayavāropi kātabbo.)":
            f"({ITARE} {GANANA} {two}ကိုလည်း{C} {VARA('nissaya')}ကိုလည်း {KAT}{END})",
        "(yathā dassanadukaṃ, evaṃ vitthāretabbaṃ, ninnānākaraṇaṃ)":
            f"({DASSD}{KAYYA} {EVAM} {VITTH}{C} {NINNANAKARANA})",
        "(Paccayavārapaccanīye nahetupaccaye uddhaccasahagate tīṇi, moho uddharitabbo. Sabbepi vārā "
        "dassanadukasadisā, uddhaccapaccanīyampi nānaṃ.)":
            (f"({VARA('paccaya')}၏ {ORD['paccanīyaṃ']}၌ {cd('hetu', 'loc', True)} {UDDH_SAH} {DHAMMA}၌ {three}{C} "
             f"{MOHA}ကို {UDDHAR}{END} {VARAS} {SAB}လည်း {DASSD}{SADISANI}{C} {F.LEX['uddhaccaṃ'][0]}၏ "
             f"{ORD['paccanīyaṃ']}လည်း {K.NANAKARANA} ဖြစ်သည်{END})"),
        "(dassanadukasadisā bhāvanā ninnānākaraṇā)": f"({DASSD}{SADISANI}{C} {BHAVANA}{C} {NINNANAKARANA})",
        "(Sabbapaccayā dassanadukasadisā, bhāvanā ninnānākaraṇā.)":
            f"({F.PACCAYA} {SAB}တို့သည် {DASSD}{SADISANI}{C} {BHAVANA}{C} {NINNANAKARANA}{END})",
        "(Paccanīyavibhaṅgo dassanadukasadiso vibhajitabbo. Evaṃ tīṇi gaṇanāpi gaṇetabbā.)":
            (f"({PACC_VIBH}ကို {DASSD}နှင့် တူအောင် {VIBHAJ}{END} {EVAM_T} {GANANA} {three}ကိုလည်း {GAN}{END})"),
        "(Avasesesu dvīsu anantarūpanissayo, pakatūpanissayo.)":
            f"({AVAS_O} {two}၌ {F.LEX['anantarūpanissayo'][0]}{C} {F.LEX['pakatūpanissayo'][0]}{END})",
        "(Saṃkhittaṃ. Vatthupurejātaṃ saṃkhittaṃ.)": f"({SAMKH}{END} {F.LEX['vatthupurejātaṃ'][0]} {SAMKH}{END})",
        "(Vatthupurejātaṃ saṃkhittaṃ.)": f"({F.LEX['vatthupurejātaṃ'][0]} {SAMKH}{END})",
        "(Evaṃ paṭiccavāropi sahajātavāropi paccayavāropi nissayavāropi saṃsaṭṭhavāropi sampayuttavāropi dassanena "
        "pahātabbahetukadukasadisā. Uddhaccasahagato moho vicikicchāsahagatamohaṭṭhāne ṭhapetabbo.)":
            (f"({EVAM_T} {_pi(*ALL6)} {DASSHD}{SADISANI}{END} {UDDH_SAH} {MOHA}ကို {VICI_SAH} {MOHA}၏ နေရာ၌ "
             f"{THAPET}{END})"),
        "(dassanena pahātabbahetukadukasadisā)": f"({DASSHD}{SADISANI})",
        "(ārabbha dassanena pahātabbahetukadukasadisā)": f"({ARABBHA} {DASSHD}{SADISANI})",
        "(ghaṭanārammaṇā tīṇipi kātabbā)": f"({GHATANA} {N['ārammaṇa']} {three}လုံးကို {KAT})",
        "(Anantarapaccaye nabhāvanāya pahātabbahetukakāraṇā vicikicchāsahagato moho na kātabbo, uddhaccasahagato "
        "moho kātabbo.)":
            (f"({cd('anantara', 'loc')} {NBH_HT} {DHAMMA} ဖြစ်သည့် အကြောင်းကြောင့် {VICI_SAH} {MOHA}ကို {NAKAT}{C} "
             f"{UDDH_SAH} {MOHA}ကို {KAT}{END})"),
        "(ghaṭanūpanissayāpi tīṇipi kātabbā)": f"({GHATANA} {N['upanissaya']}လည်း {three}လုံးကို {KAT})",
        "(nabhāvanāya pahātabbabhājanakāraṇe nānākkhaṇikā labbhati )":
            f"({NBH} {DHAMMA}ကို {BHAJANA} {NANAKK}ကို {LABHATI})",
        "(Saṃkhittaṃ. Yathā dassanena pahātabbahetukadukaṃ evaṃ bhāvanāya pahātabbahetukapaccayāpi paccanīyāpi "
        "vibhāgopi gaṇanāpi ninnānākaraṇā.)":
            (f"({SAMKH}{END} {DASSHD}{KAYYA} {EVAM} {BHH_T} {DHAMMA}၏ {F.PACCAYA}တို့လည်း{C} "
             f"{ORD['paccanīyaṃ']}တို့လည်း{C} {VIBHAGA}လည်း{C} {GANANA}တို့လည်း {NINNANAKARANA}{END})"),
        "(Parantena sakabhaṇḍachandarāgopi kātabbo.)": f"({PARANTENA} {SAKABH}ကိုလည်း {KAT}{END})",
        '(Parantena "sakabhaṇḍachandarāgo"ti kātabbaṃ.)': f"({PARANTENA} “{SAKABH}”ဟု {KAT}{END})",
        # savitakka / savicāra
        "(Savitakkamūlakā avasesā dve pañhā kātabbā, ahetukaṃ ninnānaṃ.)":
            f"({SAVIT} {DHAMMA}{F.MULAKA}၌ {AVAS_O} {PANHA} {two}ကို {KAT}{C} {AHET_S}{C} {NINNANA}{END})",
        '(Saṃkhittaṃ. Hetupaccayasadisaṃ. "Ahetuka"nti niyāmetabbaṃ.)':
            f"({SAMKH}{END} {cn('hetu')}{SADISA}{END} “{AHET_S}”ဟု {NIYAM}{END})",
        "(Avasesā dve pañhā hetupaccayasadisā ninnānā, ahetukanti niyāmetabbaṃ.)":
            f"({AVAS_O} {PANHA} {two}သည် {cn('hetu')}{SADISANI}{C} {NINNANA}{C} {AHET_S}ဟု {NIYAM}{END})",
        "(paṭisandhiyāpi dve)": f"({F.PATISANDHI}၌လည်း {two})",
        "(paṭisandhiyāpi pavattisadisāyeva)": f"({F.PATISANDHI}၌လည်း {PAVATTI}{SADISA}ပင်)",
        "(paṭisandhikkhaṇe dve kātabbā)": f"({PS_KHANA} {two}ကို {KAT})",
        "(tīṇi, paṭisandhiyāpi)": f"({three}{C} {F.PATISANDHI}၌လည်း)",
        '(Nava pañhā kātabbā. "Ahetukā"ti niyāmetabbā tīṇiyeva. Moho uddharitabbo, yathā paṭiccavāre '
        "hetupaccayasadisāyeva pañhā pañcaviññāṇā atirekā moho vitakkaṃ.)":
            (f"({PANHA} {nine}ကို {KAT}{END} “{AHET_P}”ဟု {three}ကိုသာ {NIYAM}{END} {MOHA}ကို {UDDHAR}{C} "
             f"{PATICCA_V}၌ {cn('hetu')}နှင့် တူသော {PANHA}များပင် ဖြစ်သကဲ့သို့ {PANCAV} {ATIREKA}{C} {MOHA}{C} "
             f"{VITAKKA}{END})"),
        "(Evaṃ cha pañhā kātabbā anulomasadisā, ahetukāti niyāmetabbā, tīṇiyeva, moho uddharitabbo.)":
            (f"({EVAM_T} {PANHA} {CNT['cha']}ကို {KAT}{C} {ORD['anulomaṃ']}နှင့် တူကြသည်{C} {AHET_P}ဟု {NIYAM}{C} "
             f"{three}သာ{C} {MOHA}ကို {UDDHAR}{END})"),
        "(heṭṭhā likhitaṃ lekhaṃ iminā kāraṇena daṭṭhabbaṃ)":
            f"({B.NEW['heṭṭhā']} {LIKHITA} {LEKHA}ကို {D.IMINA} {DATTH})",
        "(tīṇipi upanissayā sabbattha kātabbā)": f"({N['upanissaya']} {three}လုံးကို {K.SABBATTHA} {KAT})",
        "(dutiyavāre likhitapadā sabbe kātabbā)": f"(ဒုတိယ {VARAS}၌ {LIKHITA} {PADA} {SAB}ကို {KAT})",
        "(tīṇi, pacchājātā)": f"({three}{C} {N['pacchājāta']})",
        "(Evaṃ cattāri, sahajātāpi nānākkhaṇikāpi kātabbā.)":
            f"({EVAM_T} {four}{C} {SAH_KAMMA}ကိုလည်း{C} {NANAKK}ကိုလည်း {KAT}{END})",
        "(paṭisandhikkhaṇe sahajātāpi dvepi kātabbā)": f"({PS_KHANA} {N['sahajāta']} {two}လုံးကိုလည်း {KAT})",
        "(paṭisandhikkhaṇe, tīṇi)": f"({PS_KHANA}{C} {three})",
        "(anulomamātikā vitthāretabbā)": f"({ANUL_MATIKA}ကို {VITTH})",
        "(Yathā savitakkadukaṃ, evaṃ kātabbaṃ, ninnānākaraṇaṃ. Idha magge cattāri kātabbāni. Savicāraduke imaṃ "
        "nānākaraṇaṃ.)":
            (f"({SAVD}{KAYYA} {EVAM} {KAT}{C} {NINNANAKARANA}{END} {IHA} {cd('magga', 'loc')} {four}ကို {KAT}{END} "
             f"{SAVICD}၌ ဤသည် {K.NANAKARANA} ဖြစ်သည်{END})"),
        # sappītika / pīti / sukha / upekkhā
        "(Yathā savitakkadukaṃ sabbattha, evaṃ sappītikadukaṃ kātabbaṃ, sabbattha pavattipaṭisandhi navapi pañhā.)":
            (f"({SAVD}{KAYYA} {K.SABBATTHA}{C} {EVAM} {SAPD}ကို {KAT}{C} {K.SABBATTHA} {PAV_PS} {PANHA} "
             f"{nine}လုံး{END})"),
        "(yāva asaññasattāpi)": f"({YAVA_AS}လည်း)",
        "(Saṃkhittaṃ. Yathā savitakkaduke anulomapaccayavāraṃ, evaṃ pavattipaṭisandhi nava pañhā paripuṇṇā pīti "
        "ninnānākaraṇā.)":
            (f"({SAMKH}{END} {SAVD}၌ {ORD['anulomaṃ']}၏ {VARA('paccaya')}{KAYYA} {EVAM} {PAV_PS} {PANHA} {nine} "
             f"{PARIP}ကြသည်{C} {PITI}{C} {NINNANAKARANA}{END})"),
        "(Pavattipaṭisandhi kātabbā paṭiccavārasadisā, yāva asaññasattā.)":
            f"({PAV_PS} {KAT}{C} {PATICCA_V}{SADISANI}{C} {YAVA_AS}{END})",
        "(Anulomasadisā nava pañhā, pavattiyeva paṭisandhi natthi, ekoyeva moho.)":
            (f"({ORD['anulomaṃ']}နှင့် တူသော {PANHA} {nine}{C} {PAVATTI}သာ{C} {F.PATISANDHI} {NATTHI}{C} {MOHA} "
             f"တစ်ခုတည်း{END})"),
        "(dutiyavārasadisaṃ)": f"(ဒုတိယ {VARAS}{SADISA})",
        "(tīṇipi upanissayā)": f"({N['upanissaya']} {three}လုံး)",
        "(sahajātāpi nānākkhaṇikāpi kātabbā… dve nānākkhaṇikā)":
            f"({SAH_KAMMA}ကိုလည်း{C} {NANAKK}ကိုလည်း {KAT}{PE} {NANAKK} {two})",
        "(saṃkhittaṃ. Savitakkadukasadisaṃ kātabbaṃ.)": f"({SAMKH}{END} {SAVD}နှင့် တူအောင် {KAT}{END})",
        "(Paccanīyavibhaṅgagaṇanāpi savitakkadukasadisā. Yadipi na sameti imaṃ anulomaṃ paccavekkhitvā gaṇetabbaṃ, "
        "itare dve gaṇanā gaṇetabbā.)":
            (f"({PACC_VIBH}နှင့် {GANANA}တို့သည်လည်း {SAVD}{SADISANI}{END} {YADIPI} {SAMEN}သော်လည်း ဤ "
             f"{ORD['anulomaṃ']}ကို {PACCAVEKKH} {GAN}{C} {ITARE} {GANANA} {two}ကို {GAN}{END})"),
        "(evaṃ pītisahagatadukaṃ vitthāretabbaṃ, sappītikadukasadisaṃ ninnānākaraṇaṃ, āmasanaṃ ninnānaṃ.)":
            (f"({EVAM_T} {PITID}ကို {VITTH}{C} {SAPD}{SADISA}{C} {NINNANAKARANA}{C} {AMASANA}သည် {NINNANA}{END})"),
        "(Evaṃ sukhasahagatadukaṃ vitthāretabbaṃ, yathā sappītikadukassa anulomapaṭiccavāro.)":
            f"({EVAM_T} {SUKD}ကို {VITTH}{C} {SAPD}၏ {ORD['anulomaṃ']}၏ {PATICCA_V}{KAYYA}{END})",
        "(Yathā sappītike nahetupaccayasadisaṃ, ninnānaṃ sabbatthameva nava pañhā.)":
            (f"({SAPT} {DHAMMA}၌{KAYYA} {cd('hetu', 'n', True)}{SADISA}{C} {NINNANA}{C} {K.SABBATTHA}ပင် {PANHA} "
             f"{nine}{END})"),
        "(Evaṃ itare dve gaṇanāpi sahajātavāropi paṭiccavārasadisā. Paccayavāre pavattipi paṭisandhipi "
        "vitthāretabbā, yathā sappītikadukapaccayavārapaccanīyepi pavatte vatthu ca vitthāretabbaṃ, yathā "
        "sappītikaduke ekoyeva moho, evaṃ itare dve gaṇanāpi nissayavāropi saṃsaṭṭhavāropi sampayuttavāropi yathā "
        "sappītikadukaṃ, evaṃ kātabbaṃ.)":
            (f"({EVAM_T} {ITARE} {GANANA} {two}လည်း{C} {VARA('sahajāta')}လည်း {PATICCA_V}{SADISANI}{END} "
             f"{VARA('paccaya')}၌ {PAVATTI}ကိုလည်း{C} {F.PATISANDHI}ကိုလည်း {VITTH}{C} {SAPD}၏ {VARA('paccaya')}၏ "
             f"{ORD['paccanīyaṃ']}၌လည်း{KAYYA} {PAVATTE} {F.VATTHU}ကို{F.LAKAUNG} {VITTH}{C} {SAPD}၌ {MOHA} "
             f"တစ်ခုတည်း ဖြစ်သကဲ့သို့{C} {EVAM_T} {ITARE} {GANANA} {two}ကိုလည်း{C} "
             f"{_pi_obj('nissaya', 'saṃsaṭṭha', 'sampayutta')} {SAPD}{KAYYA} {EVAM} {KAT}{END})"),
        "(Ārammaṇepi adhipatiyāpi sappītikadukasadisā, sukhanti nānākaraṇaṃ.)":
            (f"({cd('ārammaṇa', 'loc')}လည်း{C} {cd('adhipati', 'loc')}လည်း {SAPD}{SADISANI}{C} {SUKHA}ဟူ၍ "
             f"{K.NANAKARANA} ဖြစ်သည်{END})"),
        "(Mūlaṃ. Tīṇipi sappītikadukasadisā.)": f"({MULA}{END} {three}လုံး {SAPD}{SADISANI}{END})",
        "(dutiyagamanasadisaṃ)": f"(ဒုတိယ {GAMANA}{SADISA})",
        "(Cha kammāni cattāri sahajātāpi nānākkhaṇikāpi kātabbā, dve nānākkhaṇikā.)":
            (f"({N['kamma']} {CNT['cha']}{C} {four}၌ {SAH_KAMMA}ကိုလည်း{C} {NANAKK}ကိုလည်း {KAT}{C} {two}သည် "
             f"{NANAKK}{END})"),
        "(Evaṃ paccanīyavibhaṅgopi gaṇanāpi sappītikadukasadisaṃ kātabbaṃ, yadipi vimati atthi anulomaṃ passitvā "
        "gaṇetabbaṃ.)":
            (f"({EVAM_T} {PACC_VIBH}ကိုလည်း{C} {GANANA}တို့ကိုလည်း {SAPD}နှင့် တူအောင် {KAT}{C} {YADIPI} {VIMATI} "
             f"ရှိသော်လည်း {ORD['anulomaṃ']}ကို {PASSITVA} {GAN}{END})"),
        "(Sappītikadukasadisaṃ, anulome navapi pañhā.)": f"({SAPD}{SADISA}{C} {ORDL['anulome']} {PANHA} {nine}လုံး{END})",
        '(yathā savitakkadukasadisaṃ paccayavāre nānākaraṇaṃ. "Upekkha"nti navapi pañhā kātabbā, '
        "paṭisandhipavattipi vatthupi.)":
            (f"({SAVD}နှင့် တူသည့်အတိုင်း {VARA('paccaya')}၌ {K.NANAKARANA}{END} “{UPEKKHA}”ဟု {PANHA} {nine}လုံးကို "
             f"{KAT}{C} {F.PATISANDHI}၌လည်း{C} {PAVATTE}လည်း{C} {F.VATTHU}လည်း{END})"),
        "(Evaṃ navapi pañhā pavattipaṭisandhiyo yathā savitakkadukassa evaṃ kātabbā. Tīṇiyeva moho, pavatte vatthupi "
        "kātabbā.)":
            (f"({EVAM_T} {PANHA} {nine}လုံးကို {PAV_PS} {SAVD}၌{KAYYA} {EVAM} {KAT}{END} {MOHA} {three}သာ{C} "
             f"{PAVATTE} {F.VATTHU}ကိုလည်း {KAT}{END})"),
        "(Yathā savitakkadukaṃ sampayuttavāro evaṃ kātabbo.)":
            f"({SAVD}၏ {VARA('sampayutta')}{KAYYA} {EVAM} {KAT}{END})",
        "(Evaṃ pañca pañhā yathā savitakkaduke evaṃ kātabbā.)":
            f"({EVAM_T} {PANHA} {CNT['pañca']}ကို {SAVD}၌{KAYYA} {EVAM} {KAT}{END})",
        "(Evaṃ cattāri pañhā yathā savitakkadukassa.)": f"({EVAM_T} {PANHA} {four}{C} {SAVD}၌{KAYYA}{END})",
        '(Yathā sappītikadukaṃ evaṃ ārammaṇampi adhipatipi vitthāretabbā, "upekkhā"ti nānaṃ.)':
            (f"({SAPD}{KAYYA} {EVAM} {N['ārammaṇa']}ကိုလည်း{C} {N['adhipati']}ကိုလည်း {VITTH}{C} “{UPEKKHA}”ဟူ၍ "
             f"{K.NANAKARANA} ဖြစ်သည်{END})"),
        "(tīṇi upanissayā dutiyagamanasadisā)": f"({N['upanissaya']} {three}သည် ဒုတိယ {GAMANA}{SADISANI})",
        "(sappītikadukasadisā)": f"({SAPD}{SADISANI})",
        "(Cattāri sahajātā nānākkhaṇikā kātabbā, dve nānākkhaṇikā ca.)":
            f"({four}၌ {SAH_KAMMA}{C} {NANAKK}ကို {KAT}{C} {two}၌ {NANAKK}ကိုလည်း{END})",
        "(Imāni paccayāni sappītikakaraṇena vibhajitabbāni.)":
            f"(ဤ {F.PACCAYA}တို့ကို {SAPT} {DHAMMA}၏ {KARANENA} {VIBHAJ}{END})",
        "(Evaṃ paccanīyavibhaṅgopi itare tīṇi gaṇanāpi sappītikadukasadisā kātabbā.)":
            (f"({EVAM_T} {PACC_VIBH}ကိုလည်း{C} {ITARE} {GANANA} {three}ကိုလည်း {SAPD}နှင့် တူအောင် {KAT}{END})"),
        # kāmāvacara … saraṇa
        "(itare dve pākatikā)": f"({ITARE} {two}သည် {PAKATIKA})",
        "(Avasesā tīṇi pākatikā. Saṃkhittaṃ.)": f"({AVAS_O} {three}သည် {PAKATIKA}{END} {SAMKH}{END})",
        "(Avasesā gaṇanāpi sahajātavāropi kātabbo.)":
            f"({AVAS_O} {GANANA}တို့ကိုလည်း{C} {VARA('sahajāta')}ကိုလည်း {KAT}{END})",
        "(paṭiccasadisā. Mūlaṃ kātabbaṃ.)": f"({PATICCA_V}{SADISANI}{END} {K.NOTE_FIXED['mūlaṃ kātabbaṃ']}{END})",
        '(suddhake arūpamissake ca "vipāka"nti niyāmetabbaṃ, rūpamissake natthi. Saṃkhittaṃ)':
            (f"({D.SUDDHAKE}{F.LAKAUNG}{C} {ARUPA_N}နှင့် {MISSAKE}{F.LAKAUNG} “{N['vipāka']}”ဟု {NIYAM}{C} "
             f"ရုပ်နှင့် {MISSAKE} {NATTHI}{END} {SAMKH})"),
        "(Nakāmāvacaraṃ paṭiccavārasadisaṃ ninnānaṃ, idha sabbe mahābhūtā kātabbā.)":
            (f"({NAKAMA} {DHAMMA}သည် {PATICCA_V}{SADISA}{C} {NINNANA}{C} {IHA} {MAHAB} {SAB}ကို {KAT}{END})"),
        "(yāva asaññasattā, itare pañcapi pañhā, anulomaṃ kātabbaṃ)":
            f"({YAVA_AS}{C} {ITARE} {PANHA} {CNT['pañca']}လုံး{C} {ORD['anulomaṃ']}ကို {KAT})",
        "(saṃkhittaṃ. Mūlaṃ. Itarepi pañhā kātabbā)": f"({SAMKH}{END} {MULA}{END} {ITARE} {PANHA}တို့ကိုလည်း {KAT})",
        "(yāva ajjhattikaṃ mahābhūtaṃ)": f"({AJJH} {MAHAB}အထိ)",
        '(suddhike arūpe ca missake ca "vipāka"nti niyāmetabbaṃ)':
            f"({SUDDHIKE} {ARUPE}{F.LAKAUNG}{C} {MISSAKE}{F.LAKAUNG} “{N['vipāka']}”ဟု {NIYAM})",
        "(anulomaṃ)": f"({ORD['anulomaṃ']})",
        "(paccanīyaṃ)": f"({ORD['paccanīyaṃ']})",
        "(Yathā cūḷantaraduke lokiyadukaṃ. Evaṃ imampi dukaṃ kātabbaṃ, ninnānākaraṇaṃ.)":
            f"({DK_LOK}{KAYYA}{END} {EVAM_T} ဤ {DUKA}ကိုလည်း {KAT}{C} {NINNANAKARANA}{END})",
        "(yāva asaññasattā kātabbā)": f"({YAVA_AS} {KAT})",
        "(arūpadukasadisā kātabbā)": f"({ARUPAD}နှင့် တူအောင် {KAT})",
        "(arūpadukasadisā kātabbā, āmasanā nānāpadāyeva)":
            f"({ARUPAD}နှင့် တူအောင် {KAT}{C} {AMASANA}တို့သည် {NANAPADA})",
        "(saṃkhittaṃ. Pañcapi pañhā kātabbā. Yathā niyyānikadukaṃ evaṃ paṭiccavāropi sahajātavāropi paccayavāropi "
        "nissayavāropi saṃsaṭṭhavāropi sampayuttavāropi kātabbā, ninnānākaraṇaṃ āmasanaṃ nānaṃ)":
            (f"({SAMKH}{END} {PANHA} {CNT['pañca']}လုံးကို {KAT}{END} {NIYYD}{KAYYA} {EVAM} {_pi_obj(*ALL6)} {KAT}{C} "
             f"{NINNANAKARANA}{C} {AMASANA}သည် {K.NANAKARANA} ဖြစ်သည်)"),
        "(niyyānikadukasadisā ninnānākaraṇā)": f"({NIYYD}{SADISANI}{C} {NINNANAKARANA})",
        "(arūpadukasadisaṃ)": f"({ARUPAD}{SADISA})",
        "(arūpāvacaradukasadisaṃ)": f"({ARUD}{SADISA})",
        "(Yāva ajjhattikā mahābhūtā. Yathā cūḷantaraduke lokiyadukasadisaṃ ninnānākaraṇaṃ.)":
            f"({AJJH} {MAHAB}တို့အထိ{END} {DK_LOK}နှင့် တူသည့်အတိုင်း{C} {NINNANAKARANA}{END})",
        "(Pañca pañhā arūpāvacaradukasadisā, anulomapaṭiccasadisā.)":
            f"({PANHA} {CNT['pañca']}သည် {ARUD}{SADISANI}{C} {ORD['anulomaṃ']}၏ {PATICCA_V}{SADISANI}{END})",
        "(yathā arūpāvacaradukassa paccayavāropi evaṃ kātabbo)": f"({ARUD}၌{KAYYA} {VARA('paccaya')}ကိုလည်း {EVAM} {KAT})",
        "(Evaṃ itare dve gaṇanāpi nissayavāropi kātabbo, saṃsaṭṭhavārepi dve pañhā kātabbā sabbattha.)":
            (f"({EVAM_T} {ITARE} {GANANA} {two}ကိုလည်း{C} {VARA('nissaya')}ကိုလည်း {KAT}{C} "
             f"{VARA('saṃsaṭṭha')}၌လည်း {K.SABBATTHA} {PANHA} {two}ကို {KAT}{END})"),
        "(arūpadukasadisaṃ, cattāri)": f"({ARUPAD}{SADISA}{C} {four})",
        "(arūpadukasadisā)": f"({ARUPAD}{SADISANI})",
        "(anulomamātikā gahetabbā)": f"({ANUL_MATIKA}ကို {GAHET})",
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
SK_ADD, SKF_ADD = {}, {}
_VAR_UNIT = ("lobhaṃ paṭicca moho diṭṭhi thinaṃ {thīnaṃ (sī. syā.)} uddhaccaṃ ahirikaṃ anottappaṃ, lobhaṃ paṭicca moho "
             "diṭṭhi uddhaccaṃ ahirikaṃ anottappaṃ, lobhaṃ paṭicca moho māno thinaṃ uddhaccaṃ ahirikaṃ anottappaṃ, lobhaṃ "
             "paṭicca moho māno uddhaccaṃ ahirikaṃ anottappaṃ, lobhaṃ paṭicca moho thinaṃ uddhaccaṃ ahirikaṃ anottappaṃ, "
             "lobhaṃ paṭicca moho uddhaccaṃ ahirikaṃ anottappaṃ")
_KIL_GEN = ("diṭṭhiyā", "thinassa", "uddhaccassa", "ahirikassa", "anottappassa")


def _swap(plain, old, new_, n=1):
    assert plain.count(old) >= n, (old, plain)
    return plain.replace(old, new_, n)


def setup_sk():
    eng = B._engine
    kh, lk = F.KHANDHA, F.LAKAUNG
    # (1) the kilesa list with a variant inside it: the engine renders it without the variant, the variant after its
    #     word (as 3-07 … 3-10)
    plain = eng(re.sub(r" \{[^{}]*\}", "", _VAR_UNIT), "kil1")
    anchor = _KILW["thin"]
    assert plain.count(anchor) > 1 and "{" not in plain
    SK_ADD[D._key(_VAR_UNIT, "kil1")] = plain.replace(anchor, anchor + " {V1}", 1)
    # (2) «… mohassa ca, diṭṭhiyā, thinassa, … atthipaccayena»: the engine renders the coordinated members (the «ca» of
    #     the first ones read on each member, as 3-07 … 3-10's READ), the comma list after «mohassa ca» kept as a
    #     comma list «…အား၊ …အား»
    u = ("nokileso eko khandho ca lobho ca tiṇṇannaṃ khandhānaṃ cittasamuṭṭhānānañca rūpānaṃ mohassa ca, diṭṭhiyā, "
         "thinassa, uddhaccassa, ahirikassa, anottappassa atthipaccayena paccayo…pe… dve khandhā ca…pe….")
    r = ("nokileso eko khandho ca lobho ca tiṇṇannaṃ khandhānaṃ ca cittasamuṭṭhānānaṃ rūpānaṃ ca mohassa ca "
         "atthipaccayena paccayo…pe… dve khandhā ca…pe….")
    plain = eng(r, "kil1")
    moha = MOHA + "အား" + lk
    tail = "".join(f"{C} {F.LEX[g][0]}အား" for g in _KIL_GEN)
    term = DYADS_ADD["kil1"]["nokiles"]
    SK_ADD[D._key(u, "kil1")] = "{T1}" + _swap(_swap(plain, moha, moha + tail), F.iframe("atthi"), "{C1.if}")[len(term):]
    # (3) «… saṃsaṭṭhā tayo khandhā…pe… dve khandhe ca…pe….»: «dve khandhe ca» cut short (with its «ca»)
    u = "vicikicchāsahagataṃ ekaṃ khandhañca mohañca saṃsaṭṭhā tayo khandhā…pe… dve khandhe ca…pe…."
    plain = eng(u.replace("dve khandhe ca", "dve khandhe"), "dassh")
    SK_ADD[D._key(u, "dassh")] = _swap(plain, f"{kh} {F.PAA[2]}{PE}", f"{kh} {F.PAA[2]}နှင့်{lk}{PE}")
    # (4) «… tayo khandhā cittasamuṭṭhānañca…pe…»: the noun «rūpaṃ» left out (cut by «…», as the Pāli)
    u = "dassanena pahātabbaṃ ekaṃ khandhaṃ paṭicca tayo khandhā cittasamuṭṭhānañca…pe… dve khandhe…pe…."
    plain = eng(u.replace("cittasamuṭṭhānañca…", "cittasamuṭṭhānañca rūpaṃ…"), "dass")
    term = DYADS_ADD["dass"]["dassanena pahātabb"]
    SK_ADD[D._key(u, "dass")] = "{T1}" + _swap(plain, f" ရုပ်{lk}{PE}", PE)[len(term):]
    # (5) «mahābhūte paccayā cittasamuṭṭhānaṃ.» (the noun «rūpaṃ» left out: supplied, logged)
    u = "vatthuṃ paccayā dassanena pahātabbā khandhā, mahābhūte paccayā cittasamuṭṭhānaṃ."
    plain = eng(u.replace("cittasamuṭṭhānaṃ.", "cittasamuṭṭhānaṃ rūpaṃ."), "dass")
    SK_ADD[D._key(u, "dass")] = plain.replace(DYADS_ADD["dass"]["dassanena pahātabb"], "{T1}", 1)
    SUPPLIED.append("«mahābhūte paccayā cittasamuṭṭhānaṃ.» (dassanena pahātabba, paccayavāra): «ရုပ်» supplied")
    # (6) «yaṃ vatthuṃ āmasantassa …» (niyata dyad, ārammaṇa)
    u = ("yaṃ vatthuṃ āmasantassa micchattaniyatā khandhā uppajjanti, taṃ vatthu micchattaniyatānaṃ khandhānaṃ "
         "ārammaṇapaccayena paccayo.")
    SK_ADD[D._key(u, "niyata")] = (
        f"အကြင် {F.VATTHU}ကို " + new("āmasantassa", "စွဲကိုင်သူ၏") + f" {MICCHA_N} {kh}တို့ ဖြစ်ပေါ်ကြသည်{C} "
        f"ထို {F.VATTHU}သည် {MICCHA_N} {kh}တို့အား {{C1.if}}{END}")
    # (7) «rūpāvacarādhipati vipākaṃ, rūpāvacaraṃ ekaṃ khandhaṃ» (source slip: the comma after «vipākaṃ», as against
    #     «nakāmāvacarādhipati, vipākaṃ nakāmāvacaraṃ …» of the kāmāvacara dyad): translated as written, «vipākaṃ»
    #     after the adhipati and the comma after it
    u = ("rūpāvacare khandhe paṭicca rūpāvacarādhipati vipākaṃ, rūpāvacaraṃ ekaṃ khandhaṃ paṭicca tayo khandhā…pe… "
         "dve khandhe…pe… paṭisandhikkhaṇe…pe….")
    plain = eng(u.replace("rūpāvacarādhipati vipākaṃ, rūpāvacaraṃ", "rūpāvacarādhipati, vipākaṃ rūpāvacaraṃ"), "rupa")
    rv = DYADS_ADD["rupa"]["rūpāvacar"]
    plain = _swap(plain, f"{C} {F.VIPAKA_ADJ} {rv}", f" {F.N['vipāka']}{C} {rv}")
    SK_ADD[D._key(u, "rupa")] = plain.replace(rv, "{T1}", 1).replace(rv, "{T2}", 1).replace(rv, "{T3}", 1)
    SLIPS_MINE.append("rūpāvacara dyad, paṭiccavāra naadhipati: «rūpāvacarādhipati vipākaṃ, rūpāvacaraṃ ekaṃ khandhaṃ» "
                      "(the comma after «vipākaṃ»; the kāmāvacara dyad has «…adhipati, vipākaṃ …»): translated as written")
    # (8) two sentences of the dassana / bhāvanā dyads placed at the end of the bhāvanāya-pahātabbahetuka dyad: their
    #     terms are not this part's terms (no slot): written from the two dyads' terms
    nd, bh, nb = (DYADS_ADD["dass"]["nadassanena pahātabb"], DYADS_ADD["bhav"]["bhāvanāya pahātabb"],
                  DYADS_ADD["bhav"]["nabhāvanāya pahātabb"])
    for u, a, b in (("Nadassanena pahātabbo dhammo nadassanena pahātabbassa dhammassa…pe….", nd, nd),
                    ("Bhāvanāya pahātabbo dhammo nabhāvanāya pahātabbassa dhammassa…pe….", bh, nb)):
        SK_ADD[D._key(u, "bhavh")] = f"{a} {F.DHAMMA}သည် {b} {F.DHAMMA}အား{PE}{END}"
    SKF_ADD.update({
        "§T§o dhammo §T§assa dhammassa": f"{{T1}} {F.DHAMMA}သည် {{T2}} {F.DHAMMA}အား",     # cut short by «…»
        "purimā purimā §T§ā": f"{F.QUAL['purimā purimā']} {{T1}}",                          # cut short by «…»
    })
    for mod in (F, FG):
        mod.SK.update(SK_ADD)
        mod.SKF.update(SKF_ADD)


SUPPLIED = []
SLIPS_MINE = []


# ===================================================================================== the run
def translate(name):
    return D.translate(name)


_PREV_PREP = _PREV_SET = None


def setup():
    global _PREV_PREP, _PREV_SET
    setup_names()
    setup_lex()
    setup_notes()
    global _LEX0
    _LEX0 = F.lex
    F.lex = lex
    _PREV_PREP = D.prep_dyad
    D.prep_dyad = _prep_dyad
    _PREV_SET = D.set_dyad
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
    for n in B.NAMES:
        txt = B.translate(n)
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
