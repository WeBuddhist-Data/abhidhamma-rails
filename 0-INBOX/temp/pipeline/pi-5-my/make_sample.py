"""Burmese zero-shot SAMPLE of pi-5 (Kathāvatthu, «အငြင်းပွားရာ အကြောင်းအရာများကို ဆွေးနွေးခြင်း»): preamble and
1-puggalakatha (the whole Puggalakathā, ^5-1-0 … ^5-238).

usage: python3 -I -X utf8 make_sample.py [chapter ...] [--misses]
Every line is generated from the Pāli by my5_formulas.translate_line() through the frames, rules and tables of
my5_formulas.py (which reads / checks the FINAL pi-1 … pi-4 Burmese, read only) and the tables of this script:
PROP_1 (the propositions of the Puggalakathā no rule builds), QUOTE_1 (sutta quotations), SENT_1 (unique sentences),
LINES_1 (unique whole lines: verses, the long sutta passages). A sentence no frame / rule / table entry matches stops
the run (my5_formulas.Miss): nothing is guessed. Each line is also checked here against its Pāli (dash count,
ellipsis count, «[» count, item number, no «?», no «।», no «:-»); a chapter is written only when every line passed.
--misses lists every unmatched unit and writes nothing.
Model for later chapters: copy this file, put the chapter's unique propositions / sentences in its own tables, shared
ones into my5_formulas (never change an existing value without the user's approval); change NAMES_OUT.
"""
import pathlib
import re
import sys
import unicodedata

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import my5_formulas as F  # noqa: E402
from my5_formulas import V, FR, Cl, C, END, PE, PUGGALA, SACC, FOUND  # noqa: E402

ROOT = HERE.parents[3]
PALI = ROOT / "AI_translation/pali/pi-5_split_chapters"
OUT = ROOT / "AI_translation/burmese/pi-5-burmese-plain-zeroshot_split_chapters"
NAMES_OUT = ["preamble.md", "1-puggalakatha.md"]

# ===================================================================================== tables of the Puggalakathā
W = F.witness
NOUN = F.add_noun
OTHER = F.other_cl
PUG = PUGGALA
SA = F.SAY_ANS
ANICCA = ("မမြဲသော၊ ပြုပြင်ဖန်တီးထားသော၊ အကြောင်းတို့ကို မှီ၍ ဖြစ်ပေါ်လာသော၊ ကုန်ခန်းတတ်သော သဘော၊ "
          "ပျက်စီးတတ်သော သဘော၊ ပြယ်ပျောက်တတ်သော သဘော၊ ချုပ်ငြိမ်းတတ်သော သဘော၊ ဖောက်ပြန်ပြောင်းလဲတတ်သော "
          "သဘော ရှိသော")            # anicca saṅkhata paṭiccasamuppanna khaya- vaya- virāga- nirodha- vipariṇāmadhamma
W("1", "^1-57", "paṭiccasamuppannā", "အကြောင်းတို့ကို မှီ၍ ဖြစ်ပေါ်လာသော")
W("2", "^2-806", "khayadhammaṃ vayadhammaṃ virāgadhammaṃ nirodhadhammanti",
  "ကုန်ခန်းတတ်သော သဘော၊ ပျက်စီးတတ်သော သဘော၊ ပြယ်ပျောက်တတ်သော သဘော၊ ချုပ်ငြိမ်းတတ်သော သဘော")
W("2", "^2-943", "vipariṇāmadhammā", "ဖောက်ပြန်ပြောင်းလဲတတ်သော သဘော")
W("2", "^2-154", "Cakkhuṃ aniccaṃ", "မမြဲသော")
PROP_1 = {}
QUOTE_1 = {}
SENT_1 = {}
LINES_1 = {}
ANCHOR_1 = {"re": "အမှန်ပင်", "mahiṃso": "ကျွဲ", "kāyasakkhi": F.KAYASAKKHI, "dhammānaṃ": "သဘောတရားတို့၏", "tava": "သင်၏",
            "paṭijānantaṃ": "ဝန်ခံနေသော သင့်ကို", "hevamevaṃ": "ဤနည်းအတိုင်းပင်", "anamataggoyaṃ": "ဤသံသရာသည်",
            "Bāvīsatīnaṃ": "နှစ်ဆယ့်နှစ်ပါးကို", "cattārova": "လေးယောက်ပင်", "ūhacca": "နှုတ်ပယ်၍",
            "anupalabbhiyamāne": "မတွေ့ရသောအခါ", "yampidaṃ": "ဤ အယူ၏ တည်ရာ", "hi": "ဥပမာ",
            "sammuti": "သမုတ်ခေါ်ဝေါ်ချက်", "aññindriyañca": F.NOUN["aññindriyaṃ"][0].my + "ကိုလည်း"}

# ---- nouns of the Puggalakathā (beyond the pi-2 lists)
KAYA_N = NOUN(F.KAYA, nom="kāyo")
JIVA_N = NOUN(F.JIVA, nom="jīvaṃ")
SARIRA_N = NOUN(F.SARIRA, nom="sarīraṃ")
NOUN("အစုအဝေးတို့", nom="khandhā")
NOUN(F.NIBBANA, nom="nibbānaṃ")
NOUN("ပြုပြင်ဖန်တီးထားသော အရာ", nom="saṅkhataṃ")
NOUN("ပြုပြင်ဖန်တီးထားခြင်း မရှိသော အရာ", nom="asaṅkhataṃ")
NOUN("စိတ်", nom="cittaṃ")
NOUN("သဘောတရားတို့", nom="dhammā")
for _p, _m in (("cakkhuṃ", "မျက်စိ"), ("sotaṃ", "နား"), ("ghānaṃ", "နှာခေါင်း"), ("jivhaṃ", "လျှာ"),
               ("kāyaṃ", F.KAYA), ("manaṃ", "မနော")):
    NOUN(_m, acc=_p)
NOUN("မျက်စိ", loc="cakkhumhi")
NOUN("မနော", loc="manamhi")
for _x, _m in (("Cakkhuṃ", "မျက်စိ"), ("Sotaṃ", "နား"), ("Ghānaṃ", "နှာခေါင်း"), ("Jivhā", "လျှာ"), ("Kāyo", "ကိုယ်"),
               ("Mano", "မနော")):
    W("2", "^2-154", _x, _m)
PATH = {}        # the eight wrong / right path factors: Pāli stem -> Burmese (pi-2 ^2-U30 / pi-1 / pi-2 ^2-487)
for _stem, _my in (("diṭṭhi", "အယူ"), ("saṅkappa", "ကြံစည်မှု"), ("vācā", "စကား"), ("kammanta", "အလုပ်"),
                   ("ājīva", "အသက်မွေးမှု"), ("vāyāma", "အားထုတ်မှု"), ("sati", "သတိ"), ("samādhi", "သမာဓိ")):
    for _pre, _adj in (("micchā", "မှားယွင်းသော"), ("sammā", "မှန်ကန်သော")):
        PATH[_pre + _stem] = f"{_adj} {_my}"
W("2", "^2-U30", "Micchādiṭṭhi, micchāsaṅkappo, micchāvācā, micchākammanto, micchāājīvo, micchāvāyāmo, "
  "micchāsati, micchāsamādhi", "မှားယွင်းသော အယူ၊ မှားယွင်းသော ကြံစည်မှု၊ မှားယွင်းသော စကား၊ မှားယွင်းသော အလုပ်၊ "
  "မှားယွင်းသော အသက်မွေးမှု၊ မှားယွင်းသော အားထုတ်မှု၊ မှားယွင်းသော သတိ၊ မှားယွင်းသော သမာဓိ")
W("2", "^2-487", "sammākammanto", "မှန်ကန်သော အလုပ်")
_ACC = {"diṭṭhi": "diṭṭhiṃ", "saṅkappa": "saṅkappaṃ", "vācā": "vācaṃ", "kammanta": "kammantaṃ",
        "ājīva": "ājīvaṃ", "vāyāma": "vāyāmaṃ", "sati": "satiṃ", "samādhi": "samādhiṃ"}
for _k, _v in PATH.items():
    _pre = "micchā" if _k.startswith("micchā") else "sammā"
    _stem = _k[len(_pre):]
    NOUN(_v, acc=_pre + _ACC[_stem])
NOUN(PATH["micchādiṭṭhi"], loc="micchādiṭṭhiyā")
NOUN(PATH["sammādiṭṭhi"], loc="sammādiṭṭhiyā")
NOUN(PATH["micchāsamādhi"], loc="micchāsamādhimhi")
NOUN(PATH["sammāsamādhi"], loc="sammāsamādhimhi")
HAVER = {"cakkhumā": "မျက်စိ ရှိသော", "manavā": "မနော ရှိသော",
         "micchādiṭṭhiyo": f"{PATH['micchādiṭṭhi']} ရှိသော", "micchāsamādhiyo": f"{PATH['micchāsamādhi']} ရှိသော",
         "sammādiṭṭhiyo": f"{PATH['sammādiṭṭhi']} ရှိသော", "sammāsamādhiyo": f"{PATH['sammāsamādhi']} ရှိသော"}


@F.rule(r"(?P<x>\S+) puggalo(?P<n> niruddho)?")
def _r_haver(m):
    """cakkhumā puggalo (niruddho): «မျက်စိ ရှိသော ပုဂ္ဂိုလ် (ချုပ်ငြိမ်းသွား)» (inside a quotation)."""
    if m["x"] not in HAVER:
        return None
    if m["n"]:
        return Cl(f"{HAVER[m['x']]} {PUG}", "ချုပ်ငြိမ်းသွား", "မချုပ်ငြိမ်းသွား")
    return FR(f"{HAVER[m['x']]} {PUG}")


# ---- Vacanasodhana (^5-55 … ^5-60)
_VS = {"upalabbhati": ("တွေ့ရ", "တွေ့ရသော အရာ"), "saccikaṭṭho": (None, F.SACCIKATTHA_W),
       "vijjamāno": (None, "ရှိနေသော အရာ"), "saṃvijjamāno": (None, "ထင်ရှား ရှိနေသော အရာ"),
       "atthi": ("ရှိ", "ရှိသော အရာ")}
for _k, (_verb, _noun) in _VS.items():
    if _verb:
        PROP_1[f"puggalo {_k}"] = V(PUG + ("ကို" if _verb == FOUND else ""), _verb)
    else:
        PROP_1[f"puggalo {_k}"] = V(f"{PUG}သည် {_noun}")
    PROP_1[f"{_k} puggalo"] = V(f"{_noun}သည် {PUG}")
    PROP_1[f"{_k} kehici puggalo kehici na puggalo"] = V(f"{_noun}သည် အချို့အားဖြင့် {PUG} ဖြစ်၍ "
                                                       f"အချို့အားဖြင့် {PUG}", neg=True)
PROP_1["puggalo kehici upalabbhati kehici na upalabbhati"] = V(f"{PUG}ကို အချို့အားဖြင့် တွေ့ရ၍ အချို့အားဖြင့်",
                                                              FOUND, neg=True)
for _k in ("saccikaṭṭho", "vijjamāno", "saṃvijjamāno"):
    _n = _VS[_k][1]
    PROP_1[f"puggalo kehici {_k} kehici na {_k}"] = V(f"{PUG}သည် အချို့အားဖြင့် {_n} ဖြစ်၍ အချို့အားဖြင့် {_n}",
                                                     neg=True)
PROP_1["puggalo kehici atthi kehici natthi"] = V(f"{PUG}သည် အချို့အားဖြင့် ရှိ၍ အချို့အားဖြင့်", "ရှိ", neg=True)
PROP_1["puggalo natthi"] = V(PUG, "ရှိ", neg=True)
PROP_1["atthi na sabbo puggalo"] = V(f"ရှိသော အရာ အားလုံးသည် {PUG}", neg=True)
PROP_1["natthi na sabbo puggalo"] = V(f"မရှိသော အရာ အားလုံးသည် {PUG}", neg=True)
SENT_1["(Saṃkhittaṃ)"] = F.SANKHITTA
SENT_1["(Saṃkhittaṃ)."] = F.SANKHITTA + END

# ---- Paññattānuyoga (^5-61 … ^5-68)
RUPA_B, ARUPA_B, KAMA_B = "သိမ်မွေ့သော ရုပ်ဘုံ", "ရုပ်မရှိသော ဘုံ", "ကာမဘုံ"     # core plane names
_PL = {"rūpī puggalo": ("ရုပ် ရှိသူ", PUG), "arūpī puggalo": ("ရုပ် မရှိသူ", PUG),
       "kāmī puggalo": ("ကာမ ရှိသူ", PUG), "rūpino sattā": ("ရုပ် ရှိသူတို့", F.SATTA + "တို့"),
       "arūpino sattā": ("ရုပ် မရှိသူတို့", F.SATTA + "တို့"), "kāmino sattā": ("ကာမ ရှိသူတို့", F.SATTA + "တို့")}
for _b, _bm in (("rūpadhātuyā", RUPA_B), ("arūpadhātuyā", ARUPA_B), ("kāmadhātuyā", KAMA_B)):
    for _k, (_h, _s) in _PL.items():
        PROP_1[f"{_b} {_k}"] = V(f"{_bm}၌ {_s}သည် {_h}")
for _k1, _k2 in (("rūpī puggalo", "arūpī puggalo"), ("rūpino sattā", "arūpino sattā")):
    _a, _b = PROP_1[f"rūpadhātuyā {_k1}"], PROP_1[f"arūpadhātuyā {_k2}"]
    PROP_1[f"rūpadhātuyā {_k1} arūpadhātuyā {_k2}"] = V(f"{_a.f('stmt')}{C} {_b.pre}")
PROP_1["atthi ca koci rūpadhātuyā cuto arūpadhātuṃ upapajjati"] = V(
    f"{RUPA_B}မှ သေ၍ {ARUPA_B}၌ ပြန်လည် ဖြစ်ပေါ်သူ တစ်စုံတစ်ယောက်လည်း", "ရှိ")
for _w, _s in (("puggalo", PUG), ("satto", F.SATTA)):
    PROP_1[f"rūpī {_w} upacchinno, arūpī {_w} jāto"] = Cl(
        f"ရုပ် ရှိသော {_s}သည် ပြတ်စဲသွားသည်{C} ရုပ် မရှိသော {_s}သည်", "မွေးဖွားလာ", "မမွေးဖွားလာ")
_KAYA_SYN = (f"{F.KAYA}ဟုဖြစ်စေ{C} {F.SARIRA}ဟုဖြစ်စေ{C} {F.SARIRA}ဟုဖြစ်စေ{C} {F.KAYA}ဟုဖြစ်စေ{C} "
             f"{F.KAYA}ဟူသော စကားကို ဦးစားမပေးဘဲ ဤစကားတို့သည် အနက် တူသော၊ ညီမျှသော၊ အချိုး တူသော၊ "
             f"တစ်မျိုးတည်းမှ ဖြစ်သော စကားတို့")
_JIVA_SYN = (f"{PUG}ဟုဖြစ်စေ{C} {F.JIVA}ဟုဖြစ်စေ{C} {F.JIVA}ဟုဖြစ်စေ{C} {PUG}ဟုဖြစ်စေ{C} "
             f"{PUG}ဟူသော စကားကို ဦးစားမပေးဘဲ ဤစကားတို့သည် အနက် တူသော၊ ညီမျှသော၊ အချိုး တူသော၊ "
             f"တစ်မျိုးတည်းမှ ဖြစ်သော စကားတို့")
PROP_1["kāyoti vā sarīranti vā, sarīranti vā kāyoti vā, kāyaṃ appiyaṃ karitvā esese ekaṭṭhe same samabhāge "
       "tajjāte"] = V(_KAYA_SYN)
PROP_1["puggaloti vā jīvoti vā, jīvoti vā puggaloti vā, puggalaṃ appiyaṃ karitvā esese ekaṭṭhe same samabhāge "
       "tajjāte"] = V(_JIVA_SYN)
PROP_1["taṃ jīvaṃ taṃ sarīraṃ"] = V(F.JIVA_SARIRA_SAME[:-len(" ဖြစ်")])

# ---- Gatianuyoga (^5-69 … ^5-94)
_WORLDS = f"ဤလောကမှ တမလွန် လောကသို့{C} တမလွန် လောကမှ ဤလောကသို့"   # asmā lokā paraṃ lokaṃ, parasmā …
W("1", "^1-1221", "natthi ayaṃ loko, natthi paro loko", "ဤလောက မရှိ၊ တမလွန် လောက မရှိ")
W("4", "^4-31", "sandhāvitvā", "ကူးသွား")
SANDH = "ကူးသွား"
_LOKA = "asmā lokā paraṃ lokaṃ, parasmā lokā imaṃ lokaṃ"
for _pk, _pm in (("puggalo", f"{PUG}သည်"), ("so puggalo", f"ထို{PUG}သည်"), ("añño puggalo", f"အခြား {PUG}သည်"),
                 ("sveva puggalo", f"ထို{PUG}သည်ပင်"), ("so ca añño ca", "ထိုသူလည်း အခြားသူလည်း")):
    PROP_1[f"{_pk} sandhāvati {_LOKA}"] = V(f"{_pm} {_WORLDS}", SANDH)
PROP_1[f"neva so sandhāvati, na añño sandhāvati {_LOKA}"] = V(f"ထိုသူလည်း မ{SANDH}{C} အခြားသူလည်း {_WORLDS}",
                                                            SANDH, neg=True)
PROP_1[f"neva so sandhāvati na añño sandhāvati {_LOKA}"] = PROP_1[f"neva so sandhāvati, na añño sandhāvati {_LOKA}"]
PROP_1["so puggalo sandhāvati"] = V(f"ထို{PUG}သည်", SANDH)
PROP_1["añño puggalo sandhāvati"] = V(f"အခြား {PUG}သည်", SANDH)
PROP_1["so ca añño ca sandhāvati"] = V("ထိုသူလည်း အခြားသူလည်း", SANDH)
SENT_1["Nanu vuttaṃ bhagavatā –"] = f"{F.BHAGAVA} ဤသို့ ဟောတော်မူသည် မဟုတ်လော –"
PN = {  # persons of the gati / ñātaka / paṭivedha sections: Pāli nominative -> Burmese
    "manusso": F.MANUSSA, "devo": F.DEVA, "yakkho": "ဘီလူး", "peto": F.PETA, "nerayiko": F.NERAYIKA,
    "tiracchānagato": F.TIRACCHANA, "oṭṭho": "ကုလားအုတ်", "goṇo": "နွား", "gadrabho": "မြည်း", "sūkaro": "ဝက်",
    "mahiṃso": "ကျွဲ", "khattiyo": F.KHATTIYA, "brāhmaṇo": F.BRAHMANA, "vesso": F.VESSA, "suddo": F.SUDDA,
    "mātā": F.MATA, "pitā": F.PITA, "bhātā": W("2", "^2-200", "bhātā vā", "ညီအစ်ကို"),
    "bhaginī": W("2", "^2-200", "bhaginī vā", "ညီအစ်မ"), "gahaṭṭho": F.GAHATTHA, "pabbajito": F.PABBAJITA,
    "puggalo": PUG, "sotāpanno": F.SOTAPANNA, "sakadāgāmī": F.SAKADAGAMI, "anāgāmī": F.ANAGAMI,
    "arahā": F.ARAHA, "ubhatobhāgavimutto": F.UBHATO, "paññāvimutto": F.PANNAVIM, "kāyasakkhi": F.KAYASAKKHI,
    "diṭṭhippatto": F.DITTHIPPATTA, "saddhāvimutto": F.SADDHAVIM, "dhammānusārī": F.DHAMMANUSARI,
    "saddhānusārī": F.SADDHANUSARI,
}
KOCI = "တစ်စုံတစ်ယောက်"                                  # koci


def _hutva(na_a, a, na_b, b):
    """(na) A hutvā (na) B hoti -> the relative clause «…သူ»."""
    A, B = PN[a], PN[b]
    if na_a:
        return f"{A} မဖြစ်ခဲ့ဘဲ {B} ဖြစ်လာသူ"
    if na_b:
        return f"{A} ဖြစ်ပြီးမှ {B} မဖြစ်တော့သူ"
    return f"{A} ဖြစ်ပြီးမှ {B} ဖြစ်သူ"


@F.rule(r"(?:atthi koci )?(?P<na>na )?(?P<a>\S+) hutvā")
def _r_hutva_fr(m):
    """atthi koci (na) A hutvā … (an elided series item)."""
    if m["a"] not in PN:
        return None
    return FR(f"{PN[m['a']]} မဖြစ်ခဲ့ဘဲ" if m["na"] else f"{PN[m['a']]} ဖြစ်ပြီးမှ")


@F.rule(r"(?:atthi koci )?(?P<na>na )?(?P<a>\S+) hutvā (?P<nb>na )?(?P<b>\S+) hoti")
def _r_hutva(m):
    if m["a"] not in PN or m["b"] not in PN:
        return None
    return V(f"{_hutva(m['na'], m['a'], m['nb'], m['b'])} {KOCI}", "ရှိ")


@F.rule(r"atthi koci (?P<a>\S+) hutvā (?P<l>(?:\S+ hoti, )+\S+ hoti)")
def _r_hutva_list(m):
    """atthi koci A hutvā B hoti, C hoti, … (the list of rebirths)."""
    bs = [x[:-len(" hoti")] for x in m["l"].split(", ")]
    if m["a"] not in PN or any(b not in PN for b in bs):
        return None
    rel = f"{C} ".join(f"{PN[b]} ဖြစ်သော" for b in bs)
    return V(f"{PN[m['a']]} ဖြစ်ပြီးမှ {rel} သူ {KOCI}", "ရှိ")


@F.rule(r"sveva (?P<a>\S+) so (?P<b>\S+)")
def _r_sveva(m):
    if m["a"] not in PN or m["b"] not in PN:
        return None
    return V(f"ထို{PN[m['a']]}သည်ပင် ထို{PN[m['b']]}")


@F.rule(r"(?P<a>\S+) atthi")
def _r_atthi(m):
    """X atthi (a person, or a thing of the Purisakāra list)."""
    if m["a"] in PN:
        return V(PN[m["a"]], "ရှိ")
    return None


PROP_1["cattāro purisayugā aṭṭha purisapuggalā atthi"] = V(f"လူ အတွဲ လေးတွဲ{C} {PUG} ရှစ်ယောက်", "ရှိ")
for _x, _mn in (("devo", F.DEVA), ("mahiṃso", "ကျွဲ")):
    PROP_1[f"manusso hutvā {_x} hoti, {_x} hutvā manusso hoti, manussabhūto añño, {_x} añño, manussabhūto "
           "svevāyaṃ sandhāvati"] = V(
        f"{F.MANUSSA} ဖြစ်ပြီးမှ {_mn} ဖြစ်သည်{C} {_mn} ဖြစ်ပြီးမှ {F.MANUSSA} ဖြစ်သည်{C} {F.MANUSSA} ဖြစ်ခဲ့သူ "
        f"တခြား၊ {_mn} တခြား ဖြစ်သည်{C} {F.MANUSSA} ဖြစ်ခဲ့သော ဤသူသည်ပင်", SANDH)
SENT_1["Sace hi sandhāvati sveva puggalo ito cuto paraṃ lokaṃ anañño, hevaṃ maraṇaṃ na hehiti, pāṇātipātopi "
       "nupalabbhati."] = (f"အကယ်၍ ထို{PUG}သည်ပင် ဤလောကမှ သေ၍ တမလွန် လောကသို့ အခြား မဖြစ်ဘဲ {SANDH}လျှင် "
                           f"ဤသို့ဆိုသော် သေခြင်း ဖြစ်လိမ့်မည် မဟုတ်{C} {F.PANATIPATA}ကိုလည်း မတွေ့ရ{END}")
PROP_1["kammaṃ atthi"] = V(F.KAMMA, "ရှိ")
PROP_1["kammavipāko atthi"] = V(f"{F.KAMMA}၏ {F.VIPAKA}", "ရှိ")
PROP_1["katānaṃ kammānaṃ vipāko atthi"] = V(f"ပြုခဲ့သော {F.KAMMA}တို့၏ {F.VIPAKA}", "ရှိ")
PROP_1["kusalākusale vipaccamāne svevāyaṃ sandhāvati"] = V(
    f"ကုသိုလ်နှင့် အကုသိုလ်တို့ {F.VIPAKA} ပေးနေစဉ် ဤသူသည်ပင်", SANDH)
_MAIM = [("hatthacchinno", "လက် ပြတ်သူ"), ("pādacchinno", "ခြေ ပြတ်သူ"), ("hatthapādacchinno", "လက်ခြေ ပြတ်သူ"),
         ("kaṇṇacchinno", "နား ပြတ်သူ"), ("nāsacchinno", "နှာခေါင်း ပြတ်သူ"), ("kaṇṇanāsacchinno", "နားနှာခေါင်း ပြတ်သူ"),
         ("aṅgulicchinno", "လက်ချောင်း ပြတ်သူ"), ("aḷacchinno", "လက်မ ပြတ်သူ"), ("kaṇḍaracchinno", "အကြော ပြတ်သူ"),
         ("kuṇihatthako", "လက် ကောက်သူ"), ("phaṇahatthako", "လက်ချောင်းများ ကပ်နေသူ"), ("kuṭṭhiyo", "နူနာ စွဲသူ"),
         ("gaṇḍiyo", "အကျိတ်အနာ ရှိသူ"), ("kilāsiyo", "အရေပြား အဖြူကွက် ရောဂါ ရှိသူ"),
         ("sosiyo", "ချောင်းဆိုး ပန်းနာ ရောဂါ ရှိသူ"), ("apamāriyo", "ဝက်ရူး ပြန်သူ"),
         ("oṭṭho", "ကုလားအုတ်"), ("goṇo", "နွား"), ("gadrabho", "မြည်း"), ("sūkaro", "ဝက်"), ("mahiṃso", "ကျွဲ")]
for _p, _m in _MAIM:
    PROP_1[_p] = FR(_m)
    PROP_1[f"{_p} {_p}va hoti"] = V(f"{_m}သည် {_m}ပင်")
PROP_1["sotāpanno puggalo manussalokā cuto devalokaṃ upapanno tatthapi sotāpannova hoti"] = V(
    f"{F.SOTAPANNA} {PUG}သည် လူ့လောကမှ သေ၍ နတ်လောက၌ ပြန်လည် ဖြစ်ပေါ်သောအခါ ထိုနတ်လောက၌လည်း {F.SOTAPANNA}ပင်")
PROP_1["sotāpanno puggalo manussalokā cuto devalokaṃ upapanno tatthapi manusso hoti"] = V(
    f"{F.SOTAPANNA} {PUG}သည် လူ့လောကမှ သေ၍ နတ်လောက၌ ပြန်လည် ဖြစ်ပေါ်သောအခါ ထိုနတ်လောက၌လည်း {F.MANUSSA}")
PROP_1["anañño avigato sandhāvati"] = V("အခြား မဖြစ်ဘဲ မကွယ်ပျောက်ဘဲ", SANDH)
for _p, _n in (("rūpo", F.RUPA), ("vedano", F.VEDANA), ("sañño", F.SANNA), ("saṅkhāro", F.SANKHARA),
               ("viññāṇo", F.VINNANA)):
    PROP_1["sa" + _p] = FR(f"{_n.my}နှင့်တကွ")
    PROP_1["sa" + _p + " sandhāvati"] = V(f"{_n.my}နှင့်တကွ", SANDH)
    PROP_1["a" + _p] = FR(f"{_n.my} မပါဘဲ")
    PROP_1["a" + _p + " sandhāvati"] = V(f"{_n.my} မပါဘဲ", SANDH)
for _n in F.KHANDHA5:
    _nom = _n.pali["nom"]
    PROP_1[f"{_nom} sandhāvati"] = V(f"{_n.my}သည်", SANDH)
    PROP_1[f"{_nom} na sandhāvati"] = V(f"{_n.my}သည်", SANDH, neg=True)


@F.rule(r"(?P<a>\S+)")
def _r_bare_noun(m):
    """A bare noun as an elided series item (Vedanā… saññā… saṅkhārā…): «Xသည်»."""
    n = F.noun(m["a"], "nom")
    return FR(f"{n.my}သည်") if n else None


LINES_1["Sa sattakkhattuparamaṃ, sandhāvitvāna puggalo;"] = (
    f"“ထို{PUG}သည် အများဆုံး ခုနစ်ကြိမ် {SANDH}ပြီးလျှင်{C}")
LINES_1["Dukkhassantakaro hoti, sabbasaṃyojanakkhayāti."] = (
    f"နှောင်ကြိုး အားလုံး ကုန်ခန်းခြင်းကြောင့် {F.DUKKHA_END}သူ ဖြစ်သည်”{END}")
W("4", "^4-31", "sattakkhattuṃ", "ခုနစ်ကြိမ်")
LINES_1["Khandhesu bhijjamānesu, so ce bhijjati puggalo;"] = (
    f"အစုအဝေးတို့ ပြိုကွဲကြသောအခါ ထို{PUG}သည်လည်း ပြိုကွဲသည် ဆိုလျှင်{C}")
LINES_1["Ucchedā bhavati diṭṭhi, yā buddhena vivajjitā."] = (
    f"ဘုရားရှင် ပယ်ရှားတော်မူသော ပြတ်စဲခြင်း အယူ ဖြစ်လာ၏{END}")
LINES_1["Khandhesu bhijjamānesu, no ce bhijjati puggalo;"] = (
    f"အစုအဝေးတို့ ပြိုကွဲကြသောအခါ {PUG}သည် မပြိုကွဲ ဆိုလျှင်{C}")
LINES_1["Puggalo sassato hoti, nibbānena samasamoti."] = (
    f"{PUG}သည် နိဗ္ဗာန်နှင့် အလွန် တူညီစွာ ထာဝရ တည်မြဲသူ ဖြစ်လာ၏{END}")
QUOTE_1["anamataggoyaṃ, bhikkhave, saṃsāro. Pubbakoṭi na paññāyati, avijjānīvaraṇānaṃ sattānaṃ "
        "taṇhāsaṃyojanānaṃ sandhāvataṃ saṃsarataṃ"] = (
    "ရဟန်းတို့၊ ဤသံသရာသည် အစကို ရှာ၍ မတွေ့နိုင်။ အမှန်ကို မသိမှု အတားအဆီး ရှိကြ၍ တဏှာ နှောင်ကြိုး ရှိကြသော၊ "
    f"{SANDH} ကျင်လည်နေကြသော {F.SATTA}တို့၏ ရှေးဦး အစွန်းသည် မထင်ရှား")
W("4", "^4-31", "sandhāvitvā saṃsaritvā", "ကူးသွား ကျင်လည်")

# ---- Opamma: a source slip (^5-43: no comma before «cakkhāyatanañca»)
_DA = F.found_cl(F.AYATANA["dhammāyatana"])
PROP_1["dhammāyatanaṃ upalabbhati saccikaṭṭhaparamatthena cakkhāyatanañca upalabbhati"] = V(
    f"{_DA.f('bare')}၍ {F.AYATANA['cakkhāyatana'].my}ကိုလည်း", FOUND)
# harmonise A4: no comma in the Pāli = the connective «…၍», no «၊» added (was «…တွေ့ရသည်၊ …»)

# ---- Upādāpaññatti (^5-95 … ^5-122)
for _n in F.KHANDHA5:
    PROP_1[f"{_n.pali['nom']} aniccaṃ saṅkhataṃ paṭiccasamuppannaṃ khayadhammaṃ vayadhammaṃ virāgadhammaṃ "
           "nirodhadhammaṃ vipariṇāmadhammaṃ"] = V(f"{_n.my}သည် {ANICCA} အရာ")
PROP_1["puggalopi anicco saṅkhato paṭiccasamuppanno khayadhammo vayadhammo virāgadhammo nirodhadhammo "
       "vipariṇāmadhammo"] = V(f"{PUG}သည်လည်း {ANICCA}သူ")
PROP_1["bhavo anicco saṅkhato paṭiccasamuppanno khayadhammo vayadhammo virāgadhammo nirodhadhammo "
       "vipariṇāmadhammo"] = V(f"ဘဝသည် {ANICCA} အရာ")
_COL = {"nīlaṃ": ("nīlakassa", "အပြာ"), "pītaṃ": ("pītakassa", "အဝါ"), "lohitaṃ": ("lohitakassa", "အနီ"),
        "odātaṃ": ("odātassa", "အဖြူ"), "sanidassanaṃ": ("sanidassanassa", F.SANIDASSANA),
        "anidassanaṃ": ("anidassanassa", F.ANIDASSANA), "sappaṭighaṃ": ("sappaṭighassa", F.SAPPATIGHA),
        "appaṭighaṃ": ("appaṭighassa", F.APPATIGHA)}
W("1", "^1-616", "nīlaṃ pītakaṃ lohitakaṃ odātaṃ", "အပြာ၊ အဝါ၊ အနီ၊ အဖြူ")
for _c, (_g, _m) in _COL.items():
    PROP_1[f"{_c} rūpaṃ upādāya"] = FR(f"{_m} {F.RUPA.my}{F.UPADAYA}")
    PROP_1[f"{_c} rūpaṃ upādāya {_g} puggalassa paññatti"] = V(
        f"{_m} {F.RUPA.my}{F.UPADAYA} {_m} {PUG}၏ {F.PANNATTI}", "ရှိ")
ABY = "ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော"           # abyākata (core term)
_ETH = {"kusala": "ကုသိုလ်", "akusala": "အကုသိုလ်", "abyākata": ABY}
for _e, _em in _ETH.items():
    for _n in (F.VEDANA, F.VINNANA):
        _acc = {F.VEDANA: "vedanaṃ", F.VINNANA: "viññāṇaṃ"}[_n]
        PROP_1[f"{_e[:-1]}aṃ {_acc} upādāya {_e}ssa puggalassa paññatti"] = V(
            f"{_em} {_n.my}{F.UPADAYA} {_em} {PUG}၏ {F.PANNATTI}", "ရှိ")
_FR_K = ("အသီးအပွင့် ရှိသော၊ အကျိုး ရှိသော၊ လိုလားဖွယ် အသီးအပွင့် ရှိသော၊ ချစ်ခင်ဖွယ် အသီးအပွင့် ရှိသော၊ "
         "စိတ်နှင့် တွေ့သော အသီးအပွင့် ရှိသော၊ မရောနှောသော အသီးအပွင့် ရှိသော၊ ချမ်းသာကို ဖြစ်ပေါ်စေသော၊ "
         "ချမ်းသာသော အကျိုး ရှိသော")
_FR_A = ("အသီးအပွင့် ရှိသော၊ အကျိုး ရှိသော၊ မလိုလားဖွယ် အသီးအပွင့် ရှိသော၊ မချစ်ခင်ဖွယ် အသီးအပွင့် ရှိသော၊ "
         "စိတ်နှင့် မတွေ့သော အသီးအပွင့် ရှိသော၊ ရောနှောသော အသီးအပွင့် ရှိသော၊ ဆင်းရဲကို ဖြစ်ပေါ်စေသော၊ "
         "ဆင်းရဲသော အကျိုး ရှိသော")
W("2", "^2-200", "iṭṭhā kantā manāpā", "လိုလားဖွယ်ကောင်းသော၊ ချစ်ခင်ဖွယ်ကောင်းသော၊ စိတ်နှင့် တွေ့သော")
_K_PI = "saphalā savipākā iṭṭhaphalā kantaphalā manuññaphalā asecanakaphalā sukhudrayā sukhavipākā"
_A_PI = "saphalā savipākā aniṭṭhaphalā akantaphalā amanuññaphalā secanakaphalā dukkhudrayā dukkhavipākā"
PROP_1[f"kusalā vedanā {_K_PI}"] = V(f"ကုသိုလ် {F.VEDANA.my}သည် {_FR_K} အရာ")
PROP_1[f"akusalā vedanā {_A_PI}"] = V(f"အကုသိုလ် {F.VEDANA.my}သည် {_FR_A} အရာ")
_nt = lambda s: " ".join(w[:-1] + "aṃ" for w in s.split())          # saphalā -> saphalaṃ
_ms = lambda s: " ".join(w[:-1] + "o" for w in s.split())           # saphalā -> saphalo
PROP_1[f"kusalaṃ viññāṇaṃ {_nt(_K_PI)}"] = V(f"ကုသိုလ် {F.VINNANA.my}သည် {_FR_K} အရာ")
PROP_1[f"akusalaṃ viññāṇaṃ {_nt(_A_PI)}"] = V(f"အကုသိုလ် {F.VINNANA.my}သည် {_FR_A} အရာ")
PROP_1[f"kusalopi puggalo {_ms(_K_PI)}"] = V(f"ကုသိုလ် {PUG}သည်လည်း {_FR_K}သူ")
PROP_1[f"akusalopi puggalo {_ms(_A_PI)}"] = V(f"အကုသိုလ် {PUG}သည်လည်း {_FR_A}သူ")
PROP_1["abyākatā vedanā aniccā saṅkhatā paṭiccasamuppannā khayadhammā vayadhammā virāgadhammā nirodhadhammā "
       "vipariṇāmadhammā"] = V(f"{ABY} {F.VEDANA.my}သည် {ANICCA} အရာ")
PROP_1["abyākataṃ viññāṇaṃ aniccaṃ saṅkhataṃ paṭiccasamuppannaṃ khayadhammaṃ vayadhammaṃ virāgadhammaṃ "
       "nirodhadhammaṃ vipariṇāmadhammaṃ"] = V(f"{ABY} {F.VINNANA.my}သည် {ANICCA} အရာ")
PROP_1["abyākatopi puggalo anicco saṅkhato paṭiccasamuppanno khayadhammo vayadhammo virāgadhammo nirodhadhammo "
       "vipariṇāmadhammo"] = V(f"{ABY} {PUG}သည်လည်း {ANICCA}သူ")
_NUMK = {"dvinnaṃ": 2, "pañcannaṃ": 5, "dvādasannaṃ": 12, "aṭṭhārasannaṃ": 18, "bāvīsatīnaṃ": 22}
_TOP = {"khandhānaṃ": F.KHANDHA_W, "āyatanānaṃ": F.AYATANA_W, "dhātūnaṃ": F.DHATU_W, "indriyānaṃ": F.INDRIYA_W}


@F.rule(r"(?P<n>dvinnaṃ|pañcannaṃ|dvādasannaṃ|aṭṭhārasannaṃ|bāvīsatīnaṃ) (?P<t>khandhānaṃ|āyatanānaṃ|dhātūnaṃ|"
        r"indriyānaṃ) upādāya (?P<n2>\S+) puggalānaṃ paññatti")
def _r_num_pannatti(m):
    """dvinnaṃ khandhānaṃ upādāya dvinnaṃ puggalānaṃ paññatti: «အစုအဝေး နှစ်ပါးကို မှီ၍ ပုဂ္ဂိုလ် နှစ်ယောက်၏ …»."""
    if m["n"] != m["n2"]:
        return None
    k = F.NUM_MY[_NUMK[m["n"]]]
    return V(f"{_TOP[m['t']]} {k}{F.CL}{F.UPADAYA} {PUG} {k}{F.CL_P}၏ {F.PANNATTI}", "ရှိ")


VOK = {"eka": 1, "catu": 4, "pañca": 5}
_VOK_MY = {n: W("2", "^2-234", f"{p}vokārabhavo", f"{F.KHANDHA_W} {F.NUM_MY[n]}{F.CL} ရှိသော ဘဝ")
           for p, n in VOK.items()}
for _p, _gen in (("eka", "ekassa puggalassa"), ("catu", "catunnaṃ puggalānaṃ"), ("pañca", "pañcannaṃ puggalānaṃ")):
    _n = VOK[_p]
    _who = f"{PUG}၏" if _n == 1 else f"{PUG} {F.NUM_MY[_n]}{F.CL_P}၏"
    if _n == 1:
        _who = f"{PUG} {F.NUM_MY[1]}{F.CL_P}၏"
    PROP_1[f"{_p}vokārabhavaṃ upādāya {_gen} paññatti"] = V(f"{_VOK_MY[_n]}{F.UPADAYA} {_who} {F.PANNATTI}", "ရှိ")
PROP_1["ekavokārabhave ekova puggalo"] = V(f"{_VOK_MY[1]}၌ {PUG} {F.NUM_MY[1]}{F.CL_P}တည်းသာ", "ရှိ")
PROP_1["catuvokārabhave cattārova puggalā"] = V(f"{_VOK_MY[4]}၌ {PUG} {F.NUM_MY[4]}{F.CL_P}ပင်", "ရှိ")
PROP_1["pañcavokārabhave pañceva puggalā"] = V(f"{_VOK_MY[5]}၌ {PUG} {F.NUM_MY[5]}{F.CL_P}ပင်", "ရှိ")
ANCHOR_1["cattārova"] = f"{F.NUM_MY[4]}{F.CL_P}ပင်"
ANCHOR_1["Bāvīsatīnaṃ"] = f"{F.NUM_MY[22]}{F.CL}{F.UPADAYA}"
_RP = f"{F.RUPA.my}{F.UPADAYA} {PUG}၏ {F.PANNATTI}"          # rūpaṃ upādāya puggalassa paññatti
EVAM = W("4", "^4-94", "Evamevaṃ", "ထို့အတူပင်")
for _a, _am, _b, _bm in (("rukkhaṃ", "သစ်ပင်", "chāyāya", "အရိပ်"), ("gāmaṃ", "ရွာ", "gāmikassa", "ရွာသား"),
                         ("raṭṭhaṃ", "တိုင်းပြည်", "rañño", "မင်း")):
    _head = f"yathā {_a} upādāya {_b} paññatti"
    _hm = f"{_am}ကို မှီ၍ {_bm}၏ {F.PANNATTI} ရှိ"
    PROP_1[f"{_head}, evamevaṃ rūpaṃ upādāya puggalassa paññatti"] = V(f"{_hm}သကဲ့သို့ {EVAM} {_RP}", "ရှိ")
_RK = "yathā rukkhaṃ upādāya chāyāya paññatti"
PROP_1[f"{_RK}, rukkhopi anicco chāyāpi aniccā, evamevaṃ rūpaṃ upādāya puggalassa paññatti, rūpampi aniccaṃ "
       "puggalopi anicco"] = Cl(
    f"သစ်ပင်ကို မှီ၍ အရိပ်၏ {F.PANNATTI} ရှိ၍ သစ်ပင်လည်း မမြဲ၊ အရိပ်လည်း မမြဲသကဲ့သို့ {EVAM} {_RP} ရှိ၍ "
    f"{F.RUPA.my}လည်း မမြဲ၊ {PUG}လည်း", "မြဲ", "မမြဲ", neg=True)
for _a, _am, _b, _bm, _o in (("rukkhaṃ", "သစ်ပင်", "chāyāya", "အရိပ်", "añño rukkho aññā chāyā"),
                             ("gāmaṃ", "ရွာ", "gāmikassa", "ရွာသား", "añño gāmo añño gāmiko"),
                             ("raṭṭhaṃ", "တိုင်းပြည်", "rañño", "မင်း", "aññaṃ raṭṭhaṃ añño rājā")):
    PROP_1[f"yathā {_a} upādāya {_b} paññatti, {_o}, evamevaṃ rūpaṃ upādāya puggalassa paññatti, aññaṃ rūpaṃ "
           "añño puggalo"] = V(f"{_am}ကို မှီ၍ {_bm}၏ {F.PANNATTI} ရှိ၍ {_am}နှင့် {_bm}သည် တခြားစီ ဖြစ်သကဲ့သို့ "
                              f"{EVAM} {_RP} ရှိ၍ {F.RUPA.my}နှင့် {PUG}သည် တခြားစီ")
_NIG = (f"သံခြေချင်းသည် သံခြေချင်း ခတ်ထားသူ မဟုတ်၊ အကြင်သူ၌ သံခြေချင်း ရှိ၏၊ ထိုသူသည် သံခြေချင်း ခတ်ထားသူ "
        f"ဖြစ်သကဲ့သို့ {EVAM} {F.RUPA.my}သည် {F.RUPA.my} ရှိသူ မဟုတ်၊ အကြင်သူ၌ {F.RUPA.my} ရှိ၏၊ ထိုသူသည် "
        f"{F.RUPA.my} ရှိသူ")
PROP_1["yathā na nigaḷo negaḷiko, yassa nigaḷo so negaḷiko, evamevaṃ na rūpaṃ rūpavā, yassa rūpaṃ so "
       "rūpavā"] = V(_NIG)
PROP_1["yathā na nigaḷo negaḷiko, yassa nigaḷo so negaḷiko, añño nigaḷo añño negaḷiko, evamevaṃ na rūpaṃ "
       "rūpavā, yassa rūpaṃ so rūpavā, aññaṃ rūpaṃ añño rūpavā"] = V(
    f"သံခြေချင်းသည် သံခြေချင်း ခတ်ထားသူ မဟုတ်၊ အကြင်သူ၌ သံခြေချင်း ရှိ၏၊ ထိုသူသည် သံခြေချင်း ခတ်ထားသူ "
    f"ဖြစ်၍ သံခြေချင်းနှင့် သံခြေချင်း ခတ်ထားသူသည် တခြားစီ ဖြစ်သကဲ့သို့ {EVAM} {F.RUPA.my}သည် {F.RUPA.my} "
    f"ရှိသူ မဟုတ်၊ အကြင်သူ၌ {F.RUPA.my} ရှိ၏၊ ထိုသူသည် {F.RUPA.my} ရှိသူ ဖြစ်၍ {F.RUPA.my}နှင့် "
    f"{F.RUPA.my} ရှိသူသည် တခြားစီ")
PROP_1["citte citte puggalassa paññatti"] = V(f"စိတ် တစ်ခုစီ၌ {PUG}၏ {F.PANNATTI}", "ရှိ")
PROP_1["citte citte puggalo jāyati jīyati mīyati cavati upapajjati"] = Cl(
    f"စိတ် တစ်ခုစီ၌ {PUG}သည် မွေးဖွား၊ အို၊ သေဆုံး၊ စုတေ၍ ပြန်လည်", "ဖြစ်ပေါ်", "မဖြစ်ပေါ်")
_WORDS = {"so": "ထိုသူ", "añño": "အခြားသူ", "kumārako": "သူငယ်", "kumārikā": "သူငယ်မ",
          "itthī": W("2", "^2-219", "itthindriyaṃ", "မိန်းမ"), "puriso": W("2", "^2-219", "purisindriyaṃ", "ယောက်ျား"),
          "gahaṭṭho": F.GAHATTHA, "pabbajito": F.PABBAJITA, "devo": F.DEVA, "manusso": F.MANUSSA}


@F.rule(r"dutiye citte uppanne (?P<na>na )?vattabbaṃ(?P<d> –)? (?P<l>.+)")
def _r_dutiye(m):
    """dutiye citte uppanne (na) vattabbaṃ – "Xti vā Yti vā": «ဒုတိယ စိတ် ဖြစ်ပေါ်သောအခါ ဤသို့ (မ)ဆိုသင့် – …»."""
    ws = re.findall(r"(\S+?)ti vā", m["l"] + " ")
    if not ws or any(w not in _WORDS for w in ws) or "".join(f"{w}ti vā " for w in ws).strip() != m["l"].strip():
        return None
    if not m["d"]:     # no dash in the Pāli: no quotation marks, the items before the verb
        items = f"{C} ".join(f"{_WORDS[w]}ဟုဖြစ်စေ" for w in ws)
        return Cl(f"ဒုတိယ စိတ် ဖြစ်ပေါ်သောအခါ {items}", "ဆိုသင့်", "မဆိုသင့်", neg=bool(m["na"]))
    post = " – " + f"{C} ".join(f"«{_WORDS[w]}»ဟုဖြစ်စေ" for w in ws)
    return Cl("ဒုတိယ စိတ် ဖြစ်ပေါ်သောအခါ ဤသို့", "ဆိုသင့်", "မဆိုသင့်", neg=bool(m["na"]), post=post)


# harmonise B2: ghāyati / sāyati = pi-1 / pi-2 «နမ်း / လျက်» book-wide (was «အနံ့ ခံ / အရသာ ခံ»; its negative
# «မ» + verb gave «မအနံ့ ခံ», and ch5 «အနံ့ကို အနံ့ ခံ»)
SEE = {"passati": "မြင်", "suṇāti": "ကြား", "ghāyati": F.GHAYATI, "sāyati": F.SAYATI, "phusati": "ထိ",
       "vijānāti": "သိ"}


@F.rule(r"yo (?P<n>na )?(?P<v>passati|suṇāti|ghāyati|sāyati|phusati|vijānāti)"
        r"(?P<full> yaṃ (?P=n)?(?P=v) yena (?P=n)?(?P=v), so (?P=n)?(?P=v) taṃ (?P=n)?(?P=v) tena (?P=n)?(?P=v))?")
def _r_see(m):
    """yo passati yaṃ passati yena passati, so passati taṃ passati tena passati (and with na; and the series item)."""
    v = SEE[m["v"]]
    vv = ("မ" + v) if m["n"] else v + "သည်"
    if not m["full"]:
        return FR(f"အကြင်သူသည် {'မ' + v if m['n'] else v}")
    pre = (f"အကြင်သူသည် {vv}{C} အကြင်အရာကို {vv}{C} အကြင်အရာဖြင့် {vv}{C} ထိုသူသည် {vv}{C} "
           f"ထိုအရာကို {vv}{C} ထိုအရာဖြင့်")
    return V(pre, v, neg=bool(m["n"]))


QUOTE_1["passāmahaṃ, bhikkhave, dibbena cakkhunā visuddhena atikkantamānusakena satte cavamāne upapajjamāne hīne "
        "paṇīte suvaṇṇe dubbaṇṇe, sugate duggate yathākammūpage satte pajānāmi"] = (
    f"ရဟန်းတို့၊ ငါသည် {F.DIBBACAKKHU} {F.CUTUPAPATA} {F.SATTA}တို့ကို မြင်၏၊ {F.YATHAKAMMA}၏")
_BS = f"{F.BHAGAVA}သည် {F.DIBBACAKKHU}"
PROP_1["bhagavā dibbena cakkhunā visuddhena atikkantamānusakena rūpaṃ passati puggalaṃ passati"] = Cl(
    f"{_BS} {F.RUPA_SEEN}ကို မြင်တော်မူသလော၊ {PUG}ကို", "မြင်တော်မူ", "မမြင်တော်မူ")   # harmonise B2: RUPA_SEEN
SENT_1["Rūpaṃ passati."] = f"{F.RUPA_SEEN}ကို မြင်တော်မူသည်{END}"
SENT_1["Puggalaṃ passati."] = f"{PUG}ကို မြင်တော်မူသည်{END}"
SENT_1["Ubho passati."] = f"နှစ်မျိုးလုံးကို မြင်တော်မူသည်{END}"
YK = "ကံအားလျော်စွာ ရောက်သွားသော"                           # yathākammūpaga (pi-4 «… ရောက်သွားကြသော»)
CAVATI, UPAP = "စုတေ", "ပြန်လည် ဖြစ်ပေါ်"                   # cavati / upapajjati (verbs)
PROP_1["rūpaṃ cavati"] = Cl(f"{F.RUPA.my}သည်", CAVATI, "မ" + CAVATI)
PROP_1["rūpaṃ upapajjati"] = Cl(f"{F.RUPA.my}သည် ပြန်လည်", "ဖြစ်ပေါ်", "မဖြစ်ပေါ်")
PROP_1["rūpaṃ yathākammūpagaṃ"] = V(f"{F.RUPA.my}သည် {YK} အရာ")
_RUPA_SET = (f"{F.RUPA.my}၊ {F.AYATANA['rūpāyatana'].my}၊ {F.DHATU['rūpadhātu'].my}")
PROP_1["puggalo rūpaṃ rūpāyatanaṃ rūpadhātu nīlaṃ pītakaṃ lohitakaṃ odātaṃ cakkhuviññeyyaṃ cakkhusmiṃ "
       "paṭihaññati"] = Cl(
    f"{PUG}သည် {_RUPA_SET}၊ အပြာ၊ အဝါ၊ အနီ၊ အဖြူ၊ မျက်စိဖြင့် သိနိုင်သော အရာ ဖြစ်၍ မျက်စိ၌", "ထိခိုက်", "မထိခိုက်")
W("1", "^1-588", "Cakkhuviññeyyaṃ rūpaṃ", "မျက်စိဖြင့် သိနိုင်သော")
PROP_1["cakkhussa āpāthaṃ āgacchati"] = Cl("မျက်စိ၏ အာရုံ နယ်ပယ်သို့", "ရောက်လာ", "မရောက်လာ")
PROP_1["ubho rūpaṃ rūpāyatanaṃ rūpadhātu"] = V(f"နှစ်မျိုးလုံးသည် {_RUPA_SET}")
for _p, _m in (("nīlā", "အပြာ"), ("pītakā", "အဝါ"), ("lohitakā", "အနီ"), ("odātā", "အဖြူ"),
               ("cakkhuviññeyyā", "မျက်စိဖြင့် သိနိုင်သော အရာ"), ("yathākammūpagā", f"{YK} အရာ")):
    PROP_1[f"ubho {_p}"] = V(f"နှစ်မျိုးလုံးသည် {_m}")
PROP_1["ubho cakkhusmiṃ paṭihaññanti"] = Cl("နှစ်မျိုးလုံးသည် မျက်စိ၌", "ထိခိုက်", "မထိခိုက်")
PROP_1["ubho cakkhussa āpāthaṃ āgacchanti"] = Cl("နှစ်မျိုးလုံးသည် မျက်စိ၏ အာရုံ နယ်ပယ်သို့", "ရောက်လာ", "မရောက်လာ")
PROP_1["ubho cavanti"] = Cl("နှစ်မျိုးလုံးသည်", CAVATI, "မ" + CAVATI)
PROP_1["ubho upapajjanti"] = Cl("နှစ်မျိုးလုံးသည် ပြန်လည်", "ဖြစ်ပေါ်", "မဖြစ်ပေါ်")

# ---- Purisakāra (^5-123 … ^5-192)
KP = "ကောင်းမွန်သော ကံနှင့် ယုတ်မာသော ကံတို့"                    # kalyāṇapāpakāni kammāni
THING = {  # nominative -> (Burmese, genitive Pāli)
    "kalyāṇapāpakāni kammāni": (KP, "kalyāṇapāpakānaṃ kammānaṃ"),
    "puggalo": (PUG, "puggalassa"), "nibbānaṃ": (F.NIBBANA, "nibbānassa"),
    "mahāpathavī": ("မြေကြီး", "mahāpathaviyā"), "mahāsamuddo": ("သမုဒ္ဒရာ", "mahāsamuddassa"),
    "sinerupabbatarājā": ("မြင့်မိုရ် တောင်မင်း", "sinerussa pabbatarājassa"), "āpo": ("ရေ", "āpassa"),
    "tejo": ("မီး", "tejassa"), "vāyo": ("လေ", "vāyassa"),
    "tiṇakaṭṭhavanappatayo": ("မြက်၊ ထင်း၊ သစ်ပင်တို့", "tiṇakaṭṭhavanappatīnaṃ"),
    "dibbaṃ sukhaṃ": ("နတ်တို့၏ ချမ်းသာ", "dibbassa sukhassa"),
    "mānusakaṃ sukhaṃ": ("လူတို့၏ ချမ်းသာ", "mānusakassa sukhassa"),
    "āpāyikaṃ dukkhaṃ": ("အပါယ်၏ ဆင်းရဲ", "āpāyikassa dukkhassa"),
    "nerayikaṃ dukkhaṃ": ("ငရဲ၏ ဆင်းရဲ", "nerayikassa dukkhassa"),
    "kalyāṇapāpakānaṃ kammānaṃ vipāko": (f"{KP}၏ {F.VIPAKA}", None), "vipāko": (F.VIPAKA, None),
    "kammaṃ": (F.KAMMA, None), "tassa": ("ထိုသူ", "tassa"),
}
GEN = {g: my for my, g in THING.values() if g}
KATTA = "ပြုလုပ်သူ၊ ပြုလုပ်စေသူ"                                 # kattā kāretā
PSV = "ခံစားသူ"                                                  # paṭisaṃvedī
VPSV = f"{F.VIPAKA}ကို ခံစားသူ"                                  # vipākapaṭisaṃvedī
KARAKA = "ပြုသူ"                                                 # kārako


@F.rule(r"(?P<x>.+?) (?:upalabbhati|upalabbhanti|(?P<a>atthi))")
def _r_thing(m):
    """X upalabbhati / upalabbhanti / atthi; GEN kattā kāretā / (vipāka)paṭisaṃvedī / kārako upalabbhati / atthi."""
    x, verb = m["x"], ("ရှိ" if m["a"] else FOUND)
    obj = "" if m["a"] else "ကို"
    if x in THING:
        return V(THING[x][0] + obj, verb)
    mm = re.fullmatch(r"(?P<g>.+?) (?P<r>kattā kāretā vipākapaṭisaṃvedī|kattā kāretā|vipākapaṭisaṃvedī|"
                      r"paṭisaṃvedī|kārako)", x)
    if mm and mm["g"] in GEN:
        g = GEN[mm["g"]]
        role = {"kattā kāretā": f"{g}ကို {KATTA}", "paṭisaṃvedī": f"{g}ကို {PSV}", "kārako": f"{g}ကို {KARAKA}",
                "vipākapaṭisaṃvedī": f"{g}၏ {VPSV}",
                "kattā kāretā vipākapaṭisaṃvedī": f"{g}ကို {KATTA}၊ {g}၏ {VPSV}"}[mm["r"]]
        return V(role + obj, verb)
    single = {"kammakārako": f"{F.KAMMA}ကို {KARAKA}", "vipākapaṭisaṃvedī": VPSV}
    if x in single:
        return V(single[x] + obj, verb)
    return None


NOUN(KP, nom="kalyāṇapāpakāni kammāni")
NOUN(f"{KP}ကို {KATTA}", nom="kalyāṇapāpakānaṃ kammānaṃ kattā kāretā")
NOUN(f"{KP}၏ {F.VIPAKA}", nom="kalyāṇapāpakānaṃ kammānaṃ vipāko")
NOUN(f"{KP}၏ {VPSV}", nom="kalyāṇapāpakānaṃ kammānaṃ vipākapaṭisaṃvedī")
for _k in ("dibbaṃ sukhaṃ", "mānusakaṃ sukhaṃ", "āpāyikaṃ dukkhaṃ", "nerayikaṃ dukkhaṃ"):
    _my, _g = THING[_k]
    NOUN(_my, nom=_k)
    NOUN(f"{_my}ကို {PSV}", nom=f"{_g} paṭisaṃvedī")
NOUN(F.KAMMA, nom="kammaṃ")
NOUN(f"{F.KAMMA}ကို {KARAKA}", nom="kammakārako")
NOUN(F.VIPAKA, nom="vipāko")
NOUN(VPSV, nom="vipākapaṭisaṃvedī")
PROP_1["aññāni kalyāṇapāpakāni kammāni añño kalyāṇapāpakānaṃ kammānaṃ kattā kāretā"] = OTHER(
    F.noun("kalyāṇapāpakāni kammāni", "nom"), F.noun("kalyāṇapāpakānaṃ kammānaṃ kattā kāretā", "nom"))
PROP_1["tassa tasseva natthi dukkhassa antakiriyā"] = V(f"ထိုထိုသူ၏ပင် {F.DUKKHA_END}ခြင်း", "ရှိ", neg=True)
PROP_1["natthi vaṭṭupacchedo"] = V("သံသရာ စက်ဝန်း ပြတ်ခြင်း", "ရှိ", neg=True)
PROP_1["natthi anupādāparinibbānaṃ"] = V("စွဲလမ်းမှု မရှိဘဲ ပရိနိဗ္ဗာန် ပြုခြင်း", "ရှိ", neg=True)
W("4", "^4-M-7", "parinibbāyī", "ပရိနိဗ္ဗာန် ပြုသူ")
SO_ANNO = {"so": "ထိုသူ", "añño": "အခြားသူ", "so ca añño ca": "ထိုသူနှင့် အခြားသူ"}
PROP_1["so karoti so paṭisaṃvedeti"] = V("ထိုသူ ပြု၍ ထိုသူ", "ခံစား")
PROP_1["añño karoti añño paṭisaṃvedeti"] = V("တစ်ယောက်က ပြု၍ အခြားတစ်ယောက်က", "ခံစား")
PROP_1["so ca añño ca karonti so ca añño ca paṭisaṃvedenti"] = V("ထိုသူနှင့် အခြားသူ ပြု၍ ထိုသူနှင့် အခြားသူ",
                                                                  "ခံစား")
PROP_1["so ca añño ca karonti, so ca añño ca paṭisaṃvedenti"] = PROP_1[
    "so ca añño ca karonti so ca añño ca paṭisaṃvedenti"]
PROP_1["neva so karoti na so paṭisaṃvedeti"] = V("ထိုသူလည်း မပြု၊ ထိုသူလည်း", "ခံစား", neg=True)
PROP_1["na añño karoti na añño paṭisaṃvedeti"] = V("အခြားသူလည်း မပြု၊ အခြားသူလည်း", "ခံစား", neg=True)
SD = "ချမ်းသာနှင့် ဆင်းရဲ"                                         # sukhadukkha
PROP_1["sayaṅkataṃ sukhadukkhaṃ"] = V(f"{SD}သည် မိမိ ပြုထားသော အရာ")
PROP_1["paraṅkataṃ sukhadukkhaṃ"] = V(f"{SD}သည် သူတစ်ပါး ပြုထားသော အရာ")
PROP_1["sayaṅkatañca paraṅkatañca sukhadukkhaṃ"] = V(f"{SD}သည် မိမိ ပြုထားသော အရာလည်း၊ သူတစ်ပါး ပြုထားသော "
                                                     "အရာလည်း")
PROP_1["asayaṅkāraṃ aparaṅkāraṃ adhiccasamuppannaṃ sukhadukkhaṃ"] = V(
    f"{SD}သည် မိမိ မပြု၊ သူတစ်ပါး မပြုဘဲ အကြောင်းမဲ့ ဖြစ်ပေါ်လာသော အရာ")
W("2", "^2-977", "adhiccasamuppannikā", "အကြောင်းမဲ့ ဖြစ်ပေါ်")
W("4", "^4-M-10", "parahitāya", "သူတစ်ပါး")
F.VAGGA_NAME["Kalyāṇa"] = "“ကောင်းမွန်သော”"

# ---- Abhiññā, Ñātaka, Paṭivedha, Saṅgha (^5-193 … ^5-207)
REL = {  # «yo X» / «atthi koci X»: Pāli predicate -> Burmese relative noun «…သူ»
    "iddhiṃ vikubbati": f"{F.IDDHI}ကို ဖန်ဆင်းပြသူ", "iddhiṃ na vikubbati": f"{F.IDDHI}ကို ဖန်ဆင်း မပြသူ",
    "dibbāya sotadhātuyā saddaṃ suṇāti": f"{F.SOTADHATU_DIBBA} အသံကို ကြားသူ",
    "paracittaṃ vijānāti": f"{F.PARACITTA}သူ", "pubbenivāsaṃ anussarati": f"{F.PUBBENIVASA}သူ",
    "dibbena cakkhunā rūpaṃ passati": f"နတ်မျက်စိဖြင့် {F.RUPA_SEEN}ကို မြင်သူ",     # harmonise B2 (was «ရုပ်ကို»)
    "āsavānaṃ khayaṃ sacchikaroti": f"{F.ASAVAKHAYA}ကို မျက်မှောက်ပြုသူ",
    "āsavānaṃ khayaṃ na sacchikaroti": f"{F.ASAVAKHAYA}ကို မျက်မှောက် မပြုသူ",
    "kāye kāyānupassī viharati": f"{F.KAYANUPASSI} နေသူ", "na kāye kāyānupassī viharati": f"{F.KAYANUPASSI} မနေသူ",
    "dhammesu dhammānupassī viharati": f"{F.DHAMMANUPASSI} ဖြစ်လျက် နေသူ",
    "na dhammesu dhammānupassī viharati": f"{F.DHAMMANUPASSI} ဖြစ်လျက် မနေသူ",
}
W("4", "^4-M-7", "sacchikiriyāya", "မျက်မှောက်ပြု")
FEEL = {"sukhaṃ": "သာယာသော", "dukkhaṃ": "နာကျင်သော", "adukkhamasukhaṃ": "မနာကျင် မသာယာသော"}
W("1", "^1-M1-2", "adukkhamasukhāya vedanāya", "မနာကျင် မသာယာသော ခံစားမှု")
for _f, _fm in FEEL.items():
    _vm = f"{_fm} {F.VEDANA.my}ကို ခံစားနေစဉ် «ငါ {_fm} {F.VEDANA.my}ကို ခံစားနေသည်»ဟု"
    REL[f"{_f} vedanaṃ vediyamāno {_f} vedanaṃ vediyāmīti pajānāti"] = f"{_vm} ကွဲပြားစွာ သိသူ"
    REL[f"{_f} vedanaṃ vediyamāno {_f} vedanaṃ vediyāmīti na pajānāti"] = f"{_vm} ကွဲပြားစွာ မသိသူ"
    PROP_1[f"{_f} vedanaṃ vediyamāno"] = FR(f"{_fm} {F.VEDANA.my}ကို ခံစားနေစဉ်")
    PROP_1[f"yo {_f} vedanaṃ vediyamāno"] = FR(f"{_fm} {F.VEDANA.my}ကို ခံစားနေစဉ်")
    PROP_1[f"atthi koci {_f} vedanaṃ vediyamāno"] = FR(f"{_fm} {F.VEDANA.my}ကို ခံစားနေစဉ်")
W("2", "^2-487", "Idha bhikkhu kāye kāyānupassī", "ကိုယ်၌ ကိုယ်ကို အဖန်ဖန် ရှုသူ")
FEEL_V = {"sukhā": "သာယာသော", "dukkhā": "နာကျင်သော", "adukkhamasukhā": "မနာကျင် မသာယာသော"}


@F.rule(r"(?P<k>atthi koci |yo )?(?P<x>.+)")
def _r_rel(m):
    """atthi koci X / yo X (a series item or the clause)."""
    x = m["x"]
    if x not in REL:
        return None
    if m["k"] == "yo ":
        return FR(REL[x] + "သည်")
    return V(f"{REL[x]} {KOCI}", "ရှိ")


@F.rule(r"(?:yo )?(?P<x>.+?), (?P<n>sveva puggalo|na so puggalo)")
def _r_yo_sveva(m):
    """yo X, sveva puggalo / yo na X, na so puggalo."""
    if m["x"] not in REL:
        return None
    if m["n"] == "sveva puggalo":
        return V(f"{REL[m['x']]}သည်ပင် {PUG}")
    return V(f"{REL[m['x']]}သည် {PUG}", neg=True)


for _x, _m in (("paracittaṃ vijānāti", REL["paracittaṃ vijānāti"]),
               ("pubbenivāsaṃ anussarati", REL["pubbenivāsaṃ anussarati"]),
               ("dibbena cakkhunā rūpaṃ passati", REL["dibbena cakkhunā rūpaṃ passati"])):
    PROP_1[_x] = FR(_m)
PROP_1["āsavānaṃ khayaṃ sacchikaroti"] = V(f"{REL['āsavānaṃ khayaṃ sacchikaroti']} {KOCI}", "ရှိ")
PROP_1["atthi koci vedanāsu"] = FR(f"{F.VEDANA.my}တို့၌")
PROP_1["yo vedanāsu"] = FR(f"{F.VEDANA.my}တို့၌")
PROP_1["citte"] = FR("စိတ်၌")
PROP_1["dhammesu dhammānupassī viharati"] = V(f"{REL['dhammesu dhammānupassī viharati']} {KOCI}", "ရှိ")
PROP_1["yo dukkhaṃ vedanaṃ vediyamāno"] = FR(f"{FEEL['dukkhaṃ']} {F.VEDANA.my}ကို ခံစားနေစဉ်")
PROP_1["dukkhaṃ vedanaṃ vediyamāno"] = FR(f"{FEEL['dukkhaṃ']} {F.VEDANA.my}ကို ခံစားနေစဉ်")
for _f, _fm in FEEL_V.items():
    _pf = {"sukhā": "sukhaṃ", "dukkhā": "dukkhaṃ", "adukkhamasukhā": "adukkhamasukhaṃ"}[_f]
    PROP_1[f"aññā {_f} vedanā, añño {_pf} vedanaṃ vediyamāno {_pf} vedanaṃ vediyāmīti pajānāti"] = V(
        f"{_fm} {F.VEDANA.my}နှင့် {REL[f'{_pf} vedanaṃ vediyamāno {_pf} vedanaṃ vediyāmīti pajānāti']}သည် {F.OTHER}")
    PROP_1[f"aññā {_f} vedanā"] = FR(f"{_fm} {F.VEDANA.my}နှင့်")
PROP_1["añño kāyo, añño kāye kāyānupassī viharati"] = V(f"{F.KAYA}နှင့် {REL['kāye kāyānupassī viharati']}သည် "
                                                       f"{F.OTHER}")
PROP_1["aññā vedanā"] = FR(f"{F.VEDANA.my}နှင့်")
PROP_1["aññaṃ cittaṃ"] = FR("စိတ်နှင့်")
PROP_1["aññe dhammā, añño dhammesu dhammānupassī viharati"] = V(
    f"သဘောတရားတို့နှင့် {REL['dhammesu dhammānupassī viharati']}သည် {F.OTHER}")
PROP_1["cattāro purisayugā aṭṭha purisapuggalā buddhapātubhāvā pātubhavanti"] = Cl(
    f"လူ အတွဲ လေးတွဲ{C} {PUG} ရှစ်ယောက်တို့သည် ဘုရား ပွင့်ပေါ်ခြင်းကြောင့်", "ပေါ်ပေါက်", "မပေါ်ပေါက်")
PROP_1["puggalo buddhapātubhāvā pātubhavati"] = Cl(f"{PUG}သည် ဘုရား ပွင့်ပေါ်ခြင်းကြောင့်", "ပေါ်ပေါက်", "မပေါ်ပေါက်")
PROP_1["buddhassa bhagavato parinibbute ucchinno puggalo"] = Cl(
    f"ဘုရားရှင် {F.BHAGAVA} ပရိနိဗ္ဗာန် ပြုတော်မူပြီးသောအခါ {PUG}သည်", "ပြတ်စဲသွား", "မပြတ်စဲသွား")
PROP_1["natthi puggalo"] = V(PUG, "ရှိ", neg=True)

# ---- Saccikaṭṭhasabhāga (^5-208 … ^5-238)
LAK = {"sappaccayo": F.SAPPACCAYA, "appaccayo": "အကြောင်း မရှိသော", "saṅkhato": F.SANKHATA,
       "asaṅkhato": F.ASANKHATA, "sassato": F.SASSATA + "သော", "asassato": F.ASASSATA + "သော",
       "sanimitto": f"{F.NIMITTA} ရှိသော", "animitto": f"{F.NIMITTA} မရှိသော"}
for _k, _m in LAK.items():
    PROP_1[f"puggalo {_k}"] = V(f"{PUG}သည် {_m} အရာ")
PROP_1["puggalo neva saṅkhato nāsaṅkhato"] = V(f"{PUG}သည် {F.SANKHATA} အရာလည်း မဟုတ်၊ {F.ASANKHATA} အရာလည်း",
                                               neg=True)
PROP_1["saṅkhatañca asaṅkhatañca ṭhapetvā atthaññā tatiyā koṭi"] = V(
    f"{F.SANKHATA} အရာနှင့် {F.ASANKHATA} အရာကို ချန်ထား၍ အခြား တတိယ အစွန်း", "ရှိ")
W("1", "^1-1431", "Nibbānaṃ ṭhapetvā", "ချန်ထား၍")
QUOTE_1["dvemā, bhikkhave, dhātuyo. Katamā dve? Saṅkhatā ca dhātu asaṅkhatā ca dhātu. Imā kho, bhikkhave, dve "
        "dhātuyo"] = (f"ရဟန်းတို့၊ ဤ{F.DHATU_W} နှစ်ပါး ရှိသည်။ အဘယ် နှစ်ပါးနည်း။ {F.SANKHATA} {F.DHATU_W}နှင့် "
                      f"{F.ASANKHATA} {F.DHATU_W}တို့ ဖြစ်သည်။ ရဟန်းတို့၊ ဤသည်တို့ကား {F.DHATU_W} နှစ်ပါးတို့ ဖြစ်ကြသည်")
W("1", "^1-583", "asaṅkhatā ca dhātu", f"{F.ASANKHATA} {F.DHATU_W}")
PROP_1["khandhā saṅkhatā"] = V(f"အစုအဝေးတို့သည် {F.SANKHATA} အရာ")
PROP_1["nibbānaṃ asaṅkhataṃ"] = V(f"{F.NIBBANA}သည် {F.ASANKHATA} အရာ")
for _n in F.KHANDHA5:
    PROP_1[f"{_n.pali['nom']} saṅkhataṃ"] = V(f"{_n.my}သည် {F.SANKHATA} အရာ")
PAN, NPAN = "ထင်ရှား", "မထင်ရှား"                                    # paññāyati
for _na, _neg in (("", False), ("na ", True)):
    PROP_1[f"puggalassa {_na}uppādo paññāyati"] = Cl(f"{PUG}၏ ဖြစ်ခြင်းသည်", PAN, NPAN, _neg)
    PROP_1[f"{_na}vayo paññāyati"] = Cl("ပျက်ခြင်းသည်", PAN, NPAN, _neg)
    PROP_1[f"{_na}ṭhitassa aññathattaṃ paññāyati"] = Cl("တည်နေစဉ် ပြောင်းလဲခြင်းသည်", PAN, NPAN, _neg)
QUOTE_1["tīṇimāni, bhikkhave, saṅkhatassa saṅkhatalakkhaṇāni. Saṅkhatānaṃ, bhikkhave, dhammānaṃ uppādo "
        "paññāyati, vayo paññāyati, ṭhitānaṃ aññathattaṃ paññāyati"] = (
    f"ရဟန်းတို့၊ {F.SANKHATA} အရာ၏ {F.SANKHATA} လက္ခဏာ သုံးပါးတို့ကား ဤသည်တို့ပင်။ ရဟန်းတို့၊ {F.SANKHATA} "
    f"သဘောတရားတို့၏⟦b⟧ ဖြစ်ခြင်းသည် ထင်ရှား၏၊ ပျက်ခြင်းသည် ထင်ရှား၏၊ တည်နေစဉ် ပြောင်းလဲခြင်းသည် ထင်ရှား၏")
QUOTE_1["tīṇimāni, bhikkhave, asaṅkhatassa asaṅkhatalakkhaṇāni. Asaṅkhatānaṃ, bhikkhave, dhammānaṃ na uppādo "
        "paññāyati, na vayo paññāyati, na ṭhitānaṃ aññathattaṃ paññāyati"] = (
    f"ရဟန်းတို့၊ {F.ASANKHATA} အရာ၏ {F.ASANKHATA} လက္ခဏာ သုံးပါးတို့ကား ဤသည်တို့ပင်။ ရဟန်းတို့၊ {F.ASANKHATA} "
    f"သဘောတရားတို့၏ ဖြစ်ခြင်းသည် မထင်ရှား၊ ပျက်ခြင်းသည် မထင်ရှား၊ တည်နေစဉ် ပြောင်းလဲခြင်းသည် မထင်ရှား")
PB = "ပရိနိဗ္ဗာန် ပြုပြီးသော"
PROP_1["parinibbuto puggalo atthatthamhi, natthatthamhi"] = Cl(
    f"{PB} {PUG}သည် ရှိခြင်း သဘော၌ ရှိသလော၊ မရှိခြင်း သဘော၌", "ရှိ", "မရှိ")
SENT_1["Atthatthamhīti."] = f"ရှိခြင်း သဘော၌ ဖြစ်သည်{END}"
SENT_1["natthatthamhīti."] = f"မရှိခြင်း သဘော၌ ဖြစ်သည်{END}"
PROP_1["parinibbuto puggalo sassato"] = Cl(f"{PB} {PUG}သည် ထာဝရ", "တည်မြဲ", "မတည်မြဲ")
PROP_1["parinibbuto puggalo ucchinno"] = Cl(f"{PB} {PUG}သည်", "ပြတ်စဲသွား", "မပြတ်စဲသွား")
SENT_1["Puggalo kiṃ nissāya tiṭṭhatīti?"] = f"{PUG}သည် အဘယ်ကို မှီ၍ တည်သနည်း{END}"
SENT_1["Bhavaṃ nissāya tiṭṭhatīti."] = f"ဘဝကို မှီ၍ တည်သည်{END}"
PROP_1["puggalo avekkhati"] = Cl(f"{PUG}သည်", "ရှုမြင်", "မရှုမြင်")
PROP_1["saha rūpena avekkhati, vinā rūpena avekkhati"] = Cl(
    f"{F.RUPA.my}နှင့်အတူ ရှုမြင်သလော၊ {F.RUPA.my} မပါဘဲ", "ရှုမြင်", "မရှုမြင်")
SENT_1["Saha rūpena avekkhatīti."] = f"{F.RUPA.my}နှင့်အတူ ရှုမြင်သည်{END}"
PROP_1["vinā rūpena avekkhati"] = Cl(f"{F.RUPA.my} မပါဘဲ", "ရှုမြင်", "မရှုမြင်")
PROP_1["abbhantaragato avekkhati, bahiddhā nikkhamitvā avekkhati"] = Cl(
    "အတွင်း၌ ရှိနေလျက် ရှုမြင်သလော၊ အပြင်သို့ ထွက်၍", "ရှုမြင်", "မရှုမြင်")
SENT_1["Abbhantaragato avekkhatīti."] = f"အတွင်း၌ ရှိနေလျက် ရှုမြင်သည်{END}"
PROP_1["bahiddhā nikkhamitvā avekkhati"] = Cl("အပြင်သို့ ထွက်၍", "ရှုမြင်", "မရှုမြင်")
SACCAVADI = (f"{F.BHAGAVA}သည် မှန်သော စကားကို ဆိုတော်မူသူ၊ သင့်လျော်သော အချိန်၌ ဆိုတော်မူသူ၊ ဖြစ်ရပ်မှန်ကို "
             "ဆိုတော်မူသူ၊ ဟုတ်တိုင်း ဆိုတော်မူသူ၊ မမှားယွင်းဘဲ ဆိုတော်မူသူ၊ အခြားတစ်မျိုး မဆိုတော်မူသူ")
PROP_1["bhagavā saccavādī kālavādī bhūtavādī tathavādī avitathavādī anaññathavādī"] = V(SACCAVADI)
QUOTE_1["ekapuggalo, bhikkhave, loke uppajjamāno uppajjati bahujanahitāya bahujanasukhāya lokānukampāya atthāya "
        "hitāya sukhāya devamanussānaṃ"] = (
    f"ရဟန်းတို့၊ {PUG} တစ်ယောက်သည် လောက၌ ပေါ်ပေါက်လာသောအခါ လူအများ၏ အကျိုးစီးပွားအတွက်၊ လူအများ၏ "
    f"ချမ်းသာအတွက်၊ လောကကို သနားခြင်းအတွက်၊ နတ်နှင့် လူတို့၏ အကျိုးအတွက်၊ စီးပွားအတွက်၊ ချမ်းသာအတွက် "
    f"ပေါ်ပေါက်လာ၏")
QUOTE_1["sabbe dhammā anattā"] = "သဘောတရား အားလုံးသည် အတ္တ မဟုတ်"
W("2", "^2-154", "anattā", "အတ္တ မဟုတ်")
QUOTE_1["dukkhameva uppajjamānaṃ uppajjati, dukkhameva nirujjhamānaṃ nirujjhatīti na kaṅkhati na vicikicchati, "
        "aparappaccayaññāṇamevassa ettha hoti. Ettāvatā kho, kaccāna, sammādiṭṭhi hoti"] = (
    "ဖြစ်ပေါ်သည်မှာ ဒုက္ခသာ ဖြစ်ပေါ်၏၊ ချုပ်ငြိမ်းသည်မှာ ဒုက္ခသာ⟦b⟧ ချုပ်ငြိမ်း၏ဟု သံသယ မဖြစ်၊ မယုံမှား၊ "
    f"ဤအရာ၌ ထိုသူ၏ သူတစ်ပါးကို မမှီသော ဉာဏ်သည်ပင် ဖြစ်၏။ ကစ္စာန၊ ဤမျှဖြင့် {F.SAMMADITTHI} ဖြစ်၏")
W("1", "^1-425", "kaṅkhā", "သံသယ")
W("1", "^1-425", "vicikicchā hoti", "ယုံမှားမှု")
QUOTE_1["sappikumbho"] = "ထောပတ်ကြည် အိုး"
W("1", "^1-645", "sappi", "ထောပတ်ကြည်")
PROP_1["atthi koci sappissa kumbhaṃ karoti"] = V(f"ထောပတ်ကြည်ဖြင့် အိုးကို ပြုလုပ်သူ {KOCI}", "ရှိ")
QUOTE_1["telakumbho… madhukumbho… phāṇitakumbho… khīrakumbho… udakakumbho… pānīyathālakaṃ… pānīyakosakaṃ… "
        "pānīyasarāvakaṃ… niccabhattaṃ… dhuvayāgu"] = (
    "ဆီ အိုး… ပျားရည် အိုး… တင်လဲ အိုး… နွားနို့ အိုး… ရေ အိုး… သောက်ရေ ဗန်း… သောက်ရေ ခွက်… သောက်ရေ ပန်းကန်… "
    "အမြဲ ထမင်း… အမြဲ ယာဂု")
W("1", "^1-645", "telaṃ madhu phāṇitaṃ", "ဆီ၊ ပျားရည်၊ တင်လဲ")
NICCA = f"မြဲသော၊ ခိုင်ခံ့သော၊ {F.SASSATA}သော၊ ဖောက်ပြန်ပြောင်းလဲတတ်သော သဘော မရှိသော"   # nicca dhuva sassata avipariṇāma-
PROP_1["atthi kāci yāgu niccā dhuvā sassatā avipariṇāmadhammā"] = V(f"{NICCA} ယာဂု တစ်စုံတစ်ရာ", "ရှိ")

# ---- the long sutta passages and verses (whole units / lines; quote marks typed as in the Pāli)
LINES_1["Suññato lokaṃ avekkhassu, mogharāja sadā sato;"] = (
    "“မောဃရာဇ၊ အမြဲ သတိ ရှိလျက် လောကကို ဆိတ်သုဉ်းသည်ဟု ရှုမြင်လော့၊")
W("1", "^1-1-1-3-0", "Suññatavāro", "ဆိတ်သုဉ်း")
LINES_1["Attānudiṭṭhiṃ ūhacca, evaṃ maccutaro siyā;"] = "အတ္တ အယူကို နှုတ်ပယ်၍ ⟦0⟧ ဤသို့ သေမင်းကို ကူးမြောက်သူ ဖြစ်ရာ၏၊"
LINES_1["Evaṃ lokaṃ avekkhantaṃ, maccurājā na passatīti."] = (
    "ဤသို့ လောကကို ရှုမြင်နေသူကို သေမင်းသည် မမြင်” ⟦0⟧။")
SENT_1["Nanu vajirā bhikkhunī māraṃ pāpimantaṃ etadavoca –"] = (
    "ဝဇိရာ ဘိက္ခုနီသည် မကောင်းမှု ပြုသော မာရ်နတ်ကို ဤသို့ ပြောခဲ့သည် မဟုတ်လော –")
LINES_1["Kinnu sattoti paccesi, māra diṭṭhigataṃ nu te;"] = (
    f"“မာရ်နတ်၊ သင်သည် {F.SATTA}ဟု အဘယ်ကြောင့် ယုံကြည်သနည်း။ ဤသည် သင်၏ အယူမှား ဖြစ်လေသလော။")
LINES_1["Suddhasaṅkhārapuñjoyaṃ, nayidha sattupalabbhati."] = (
    f"ဤသည်ကား သက်သက် {F.SANKHARA.my}၏ အစုအပုံသာ ဖြစ်၏၊ ဤ၌ {F.SATTA}ကို မတွေ့ရ။")
LINES_1["Yathā hi aṅgasambhārā, hoti saddo ratho iti;"] = (
    "“ဥပမာ ⟦0⟧ အင်္ဂါ အစိတ်အပိုင်းတို့ စုပေါင်းမိသောအခါ ရထားဟူသော အသံ ဖြစ်သကဲ့သို့၊")
LINES_1["Evaṃ khandhesu santesu, hoti sattoti sammuti."] = (
    f"ထို့အတူ အစုအဝေးတို့ ရှိကြသောအခါ {F.SATTA}ဟူသော သမုတ်ခေါ်ဝေါ်ချက် ⟦0⟧ ဖြစ်၏။")
LINES_1["Dukkhameva hi sambhoti, dukkhaṃ tiṭṭhati veti ca;"] = "“ဒုက္ခသာလျှင် ဖြစ်ပေါ်၏၊ ဒုက္ခသာ တည်၍ ပျက်ကွယ်၏၊"
LINES_1["Nāññatra dukkhā sambhoti, nāññaṃ dukkhā nirujjhatīti."] = (
    "ဒုက္ခမှ တစ်ပါး အခြား မဖြစ်ပေါ်၊ ဒုက္ခမှ တစ်ပါး အခြား မချုပ်ငြိမ်း” ⟦0⟧။")
SU = "ဆိတ်သုဉ်း"
AT = "အတ္တမှ ဖြစ်စေ၊ အတ္တနှင့် ဆိုင်သော အရာမှ ဖြစ်စေ"              # attena vā attaniyena vā
SENT_1["Nanu āyasmā ānando bhagavantaṃ etadavoca – suñño loko suñño lokoti, bhante, vuccati. Kittāvatā nu kho, "
       "bhante, suñño lokoti vuccatīti?"] = (
    f"အသျှင် အာနန္ဒာသည် {F.BHAGAVA}ကို ဤသို့ လျှောက်ခဲ့သည် မဟုတ်လော – “အသျှင်ဘုရား၊ ‘လောကသည် {SU}၏၊ "
    f"လောကသည် {SU}၏’ဟု ဆိုကြပါသည်။ အသျှင်ဘုရား၊ အဘယ်မျှဖြင့် ‘လောကသည် {SU}၏’ဟု ဆိုကြပါသနည်း”{END}")
_PH = "တွေ့ထိမှု"
_VY = (f"{_PH}ကြောင့် ဖြစ်ပေါ်သော သာယာသည်ဖြစ်စေ၊ နာကျင်သည်ဖြစ်စေ၊ မနာကျင် မသာယာသည်ဖြစ်စေ ခံစားရမှု ရှိသမျှ၊ "
       f"ထိုခံစားရမှုသည်လည်း {AT} {SU}၏")
SENT_1["Yasmā kho, ānanda, suññaṃ attena vā attaniyena vā, tasmā suñño lokoti vuccati. Kiñcānanda, suññaṃ attena "
       "vā attaniyena vā? Cakkhuṃ kho, ānanda, suññaṃ attena vā attaniyena vā, rūpā suññā… cakkhuviññāṇaṃ suññaṃ… "
       "cakkhusamphasso suñño… yampidaṃ cakkhusamphassapaccayā uppajjati vedayitaṃ sukhaṃ vā dukkhaṃ vā "
       "adukkhamasukhaṃ vā, tampi suññaṃ attena vā attaniyena vā, sotaṃ suññaṃ… saddā suññā… ghānaṃ suññaṃ… "
       "gandhā suññā… jivhā suññā… rasā suññā… kāyo suñño… phoṭṭhabbā suññā… mano suñño… dhammā suññā… "
       "manoviññāṇaṃ suññaṃ… manosamphasso suñño… yampidaṃ manosamphassapaccayā uppajjati vedayitaṃ sukhaṃ vā "
       "dukkhaṃ vā adukkhamasukhaṃ vā, tampi suññaṃ attena vā attaniyena vā. Yasmā kho, ānanda, suññaṃ attena vā "
       "attaniyena vā, tasmā suñño lokoti vuccatīti."] = (
    f"“အာနန္ဒာ၊ {AT} {SU}သောကြောင့် ‘လောကသည် {SU}၏’ဟု ဆိုကြ၏။ အာနန္ဒာ၊ {AT} {SU}သော အရာ ဟူသည် "
    f"အဘယ်နည်း။ အာနန္ဒာ၊ မျက်စိသည် {AT} {SU}၏၊ အဆင်းအရောင်တို့သည် {SU}ကုန်၏… မျက်စိ သိစိတ်သည် {SU}၏… "
    f"မျက်စိ {_PH}သည် {SU}၏… မျက်စိ {_VY}၊ နားသည် {SU}၏… အသံတို့သည် {SU}ကုန်၏… နှာခေါင်းသည် {SU}၏… "
    f"အနံ့တို့သည် {SU}ကုန်၏… လျှာသည် {SU}၏… အရသာတို့သည် {SU}ကုန်၏… ကိုယ်သည် {SU}၏… အထိအတွေ့တို့သည် "
    f"{SU}ကုန်၏… မနောသည် {SU}၏… သဘောတရားတို့သည် {SU}ကုန်၏… မနော သိစိတ်သည် {SU}၏… မနော {_PH}သည် {SU}၏… "
    f"မနော {_VY}။ အာနန္ဒာ၊ {AT} {SU}သောကြောင့် ‘လောကသည် {SU}၏’ဟု ဆိုကြ၏”{END}")
W("1", "^1-1", "phasso hoti", _PH)
QUOTE_1["attani vā, bhikkhave, sati attaniyaṃ meti assā"] = (
    "ရဟန်းတို့၊ အတ္တ ရှိလျှင် ‹ငါ၏ အတ္တနှင့် ဆိုင်သော အရာ›ဟူ၍ ဖြစ်ရာသလော")
SENT_1["Evaṃ, bhante."] = "“မှန်ပါ၊ အသျှင်ဘုရား”။"
SENT_1["Attaniye vā, bhikkhave, sati attā meti assāti?"] = (
    "“ရဟန်းတို့၊ အတ္တနှင့် ဆိုင်သော အရာ ရှိလျှင် ‘ငါ၏ အတ္တ’ဟူ၍ ဖြစ်ရာသလော”။")
SENT_1["Attani ca, bhikkhave, attaniye ca saccato thetato anupalabbhiyamāne yampidaṃ diṭṭhiṭṭhānaṃ so loko so attā "
       "so pecca bhavissāmi nicco dhuvo sassato avipariṇāmadhammo, sassatisamaṃ tatheva ṭhassāmīti – nanvāyaṃ, "
       "bhikkhave, kevalo paripūro bāladhammoti?"] = (
    "“ရဟန်းတို့၊ အတ္တကိုလည်း၊ အတ္တနှင့် ဆိုင်သော အရာကိုလည်း အမှန်အားဖြင့် ခိုင်မြဲစွာ မတွေ့ရသောအခါ⟦b⟧ ထိုသည်ကား "
    f"လောက၊ ထိုသည်ကား အတ္တ၊ ငါသည် သေပြီးနောက် {NICCA} အရာ "
    "ဖြစ်လိမ့်မည်၊ ထာဝရ တည်မြဲသည်နှင့် တူစွာ ထိုအတိုင်းပင် တည်လိမ့်မည်ဟူသော ဤ⟦b⟧ အယူ၏ တည်ရာ – "
    "‘ရဟန်းတို့၊ ဤသည်ကား သက်သက် ပြည့်စုံသော လူမိုက်၏ တရား မဟုတ်လော’”။")
SENT_1["Kiñhi no siyā, bhante, kevalo hi, bhante, paripūro bāladhammoti."] = (
    "“အသျှင်ဘုရား၊ အဘယ်ကြောင့် မဖြစ်ရာပါမည်နည်း၊ အသျှင်ဘုရား၊ သက်သက် ပြည့်စုံသော လူမိုက်၏ တရားပင် "
    "ဖြစ်ပါသည်” ⟦b⟧။")
TEACH = "အတ္တကို အမှန်အားဖြင့် ခိုင်မြဲစွာ"                         # attānaṃ saccato thetato (pi-4 ^4-131)
W("4", "^4-131", "attānaṃ saccato thetato paññapeti", f"{TEACH} ပညတ်")
DIT, SAMP = W("4", "^4-131", "diṭṭhe ceva dhamme", "မျက်မှောက်ဘဝ၌ပင်"), W("4", "^4-131", "abhisamparāyañca",
                                                                      "တမလွန်ဘဝ၌လည်း")
SANTO = W("4", "^4-94", "santo saṃvijjamānā lokasmiṃ", "လောက၌ ရှိကြ၏၊ ထင်ရှား ရှိကြ၏")
_T1 = f"{DIT} {TEACH} ပညတ်၏၊ {SAMP} {TEACH} ပညတ်"
_T2 = f"မျက်မှောက်ဘဝ၌သာ {TEACH} ပညတ်၏၊ တမလွန်ဘဝ၌ကား {TEACH} မပညတ်"
_T3 = f"{DIT} {TEACH} မပညတ်၊ {SAMP} {TEACH} မပညတ်"
SENT_1["Vuttaṃ bhagavatā – tayo me, seniya, satthāro santo saṃvijjamānā lokasmiṃ. Katame tayo? Idha, seniya, "
       "ekacco satthā diṭṭheva dhamme attānaṃ saccato thetato paññāpeti, abhisamparāyañca attānaṃ saccato thetato "
       "paññāpeti."] = (
    f"{F.BHAGAVA} ဤသို့ ဟောတော်မူသည် – “သေနိယ၊ ဆရာ သုံးယောက်တို့သည် {SANTO}။ "
    f"အဘယ် သုံးယောက်တို့နည်း။ သေနိယ၊ ဤလောက၌ အချို့သော ဆရာသည် {_T1}၏။")
LINES_1["Idha pana, seniya, ekacco satthā diṭṭheva hi kho dhamme attānaṃ saccato thetato paññāpeti, no ca kho "
        "abhisamparāyaṃ attānaṃ saccato thetato paññāpeti."] = (
    f"“သေနိယ၊ တစ်ဖန် ဤလောက၌ အချို့သော ဆရာသည် {_T2}။")
LINES_1["Idha pana, seniya, ekacco satthā diṭṭhe ceva dhamme attānaṃ saccato thetato na paññāpeti, "
        "abhisamparāyañca attānaṃ saccato thetato na paññāpeti."] = (
    f"“သေနိယ၊ တစ်ဖန် ဤလောက၌ အချို့သော ဆရာသည် {_T3}။")
_SV = W("4", "^4-131", "sassatavādo satthā", "ထာဝရ တည်မြဲသည်ဟု ဆိုသော ဝါဒ ရှိသော ဆရာ")
_UV = "ပြတ်စဲသွားသည်ဟု ဆိုသော ဝါဒ ရှိသော ဆရာ"
W("2", "^2-977", "ucchedavādā", "ပြတ်စဲသွားသည်ဟု ဆိုသော ဝါဒ")
_SB = F.NAMO.split("၊ ")[-1].replace("ဘုရားရှင်အား ရှိခိုးပါ၏", "ဘုရားရှင်")
LINES_1["Tatra, seniya, yvāyaṃ satthā diṭṭhe ceva dhamme attānaṃ saccato thetato paññāpeti, abhisamparāyañca "
        "attānaṃ saccato thetato paññāpeti – ayaṃ vuccati, seniya, satthā sassatavādo."] = (
    f"“သေနိယ၊ ထိုဆရာတို့အနက် {_T1}သော အကြင် ဆရာ ရှိ၏ – သေနိယ၊ ဤဆရာကို {_SV}ဟု ခေါ်သည်။")
LINES_1["Tatra, seniya, yvāyaṃ satthā diṭṭheva hi kho dhamme attānaṃ saccato thetato paññāpeti, no ca kho "
        "abhisamparāyaṃ attānaṃ saccato thetato paññāpeti – ayaṃ vuccati, seniya, satthā ucchedavādo."] = (
    f"“သေနိယ၊ ထိုဆရာတို့အနက် {_T2}သော အကြင် ဆရာ ရှိ၏ – သေနိယ၊ ဤဆရာကို {_UV}ဟု ခေါ်သည်။")
SENT_1["Tatra, seniya, yvāyaṃ satthā diṭṭhe ceva dhamme attānaṃ saccato thetato na paññāpeti, abhisamparāyañca "
       "attānaṃ saccato thetato na paññāpeti – ayaṃ vuccati, seniya, satthā sammāsambuddho. Ime kho, seniya, tayo "
       "satthāro santo saṃvijjamānā lokasminti."] = (
    f"“သေနိယ၊ ထိုဆရာတို့အနက် {_T3}သော အကြင် ဆရာ ရှိ၏ – သေနိယ၊ ဤဆရာကို {_SB}ဟု ခေါ်သည်။ သေနိယ၊ "
    f"ဤဆရာ သုံးယောက်တို့သည် {SANTO}” ⟦b⟧။")
LINES_1["Aṭṭhakaniggahapeyyālā, sandhāvaniyā upādāya;"] = (
    f"{F.CLOSE['Aṭṭhakaniggaho']}နှင့် အကျဉ်းချုံ့ချက်တို့၊ {SANDH}ခြင်း၊ မှီ၍ {F.PANNATTI}၊")
LINES_1["Cittena pañcamaṃ kalyāṇaṃ, iddhisuttāharaṇena aṭṭhamaṃ."] = (
    f"စိတ်နှင့်တကွ {F.ORD_MY[5]}မြောက် ဖြစ်သော “ကောင်းမွန်သော” {F.VAGGA_W}၊ {F.IDDHI}နှင့် {F.SUTTANTA} "
    f"ကိုးကားခြင်းဖြင့် {F.ORD_MY[8]}မြောက်{END}")


# ===================================================================================== run
F.PROP.update(PROP_1)
F.QUOTE.update(QUOTE_1)
F.SENT.update(SENT_1)
F.LINES.update(LINES_1)
F.ANCHOR.update(ANCHOR_1)

DASH = ("–", "—")


def line_check(p, m):
    """Per-line hard rules against the Pāli line."""
    errs = []
    if sum(p.count(d) for d in DASH) != sum(m.count(d) for d in DASH):
        errs.append("dash")
    if p.replace("…Pe…", "…pe…").replace("…pe…", "…").count("…") != m.count("…"):
        errs.append("ellipsis")
    if p.count("[") != m.count("["):
        errs.append("[")
    if (re.match(r"\((\d+)\)", p) or [None, None])[1] != (re.match(r"\((\d+)\)", m) or [None, None])[1]:
        errs.append("item number")
    for bad in ("?", "।", ":-"):
        if bad in m:
            errs.append(bad)
    if re.findall(r"\d+", F.strip_id(p)) != re.findall(r"\d+", F.strip_id(m)):
        errs.append("digits")
    return errs


def run(name, misses=False):
    src = (PALI / name).read_text(encoding="utf-8-sig")
    out, bad = [], 0
    for ln, line in enumerate(src.splitlines(), 1):
        if not line.strip():
            out.append("")
            continue
        try:
            my = unicodedata.normalize("NFC", F.translate_line(line))
        except F.Miss as e:
            bad += 1
            print(f"{name}:{ln}: MISS {e}")
            if not misses:
                sys.exit(1)
            out.append("?")
            continue
        errs = line_check(line, my)
        if errs:
            bad += 1
            print(f"{name}:{ln}: CHECK {errs}\n  P: {line[:300]}\n  M: {my[:300]}")
            if not misses:
                sys.exit(1)
        out.append(my)
    return "\n".join(out).rstrip("\n") + "\n", bad


def main():
    args = sys.argv[1:]
    misses = "--misses" in args
    names = [a for a in args if not a.startswith("--")] or NAMES_OUT
    total = 0
    for name in names:
        text, bad = run(name, misses)
        total += bad
        if not misses and not bad:
            OUT.mkdir(parents=True, exist_ok=True)
            assert "\n\n\n" not in text
            (OUT / name).write_text(text, encoding="utf-8")
            print(f"wrote {name}")
    if misses:
        print(f"{total} misses")


if __name__ == "__main__":
    main()
