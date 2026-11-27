"""Burmese zero-shot of pi-1 chapters 4-01, 4-02, 4-03 (Nikkhepakaṇḍa: the brief exposition of the Mātikā items).

usage: python3 -I -X utf8 make_ch4.py [4-01|4-02|4-03 ...]      (no argument: all three)
Every line is generated from the Pāli by my_formulas.translate_cu() (the 2-01 clause engine). This script only ADDS
entries in memory: Nikkhepa frames in F.CU_EXTRA_RULES, new factor names / synonyms in F.SYN, list heads in F.GEN,
headings in F.HEAD / F.COLO, variant kinds in F.VAR_KIND, sigla in F.SIGLA. No value of my_formulas.py is changed
(asserted by add()). Mātikā items always come from F.TERMS / F.CEVA / F.CEVANO / F.SUT unchanged; where the sentence
needs another grammatical form (predicate, locative, two items joined) the form is derived by pred() / loc() /
join2() and logged in notes-ch4.md. A line no rule matches stops the run (my_formulas.Miss): nothing is guessed.
Writes only the chapter files; never touches my_formulas.py or my-zeroshot-terms.md.
"""
import pathlib
import re
import sys
import unicodedata

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import my_formulas as F  # noqa: E402

ROOT = HERE.parents[3]
PALI = ROOT / "AI_translation/pali/pi-1_split_chapters"
OUT = ROOT / "AI_translation/burmese/pi-1-burmese-plain-zeroshot_split_chapters"
CHAPTERS = {"4-01": "4-01-nikkhepakandam.md", "4-02": "4-02-nikkhepakandam.md", "4-03": "4-03-nikkhepakandam.md"}

T = F.TERMS
DH, DHP = F.DHAMMA, F.DHAMMA_PL
END, COMMA = F.END, F.COMMA
NEG_RX = re.compile(r"မ(?=[က-ဪ](?!့?[္်]))")


def add(d, k, v):
    """Add a key to a my_formulas table; never change an existing value."""
    if k in d and d[k] != v:
        raise SystemExit(f"conflict in table for {k!r}: {d[k]!r} vs {v!r}")
    d[k] = v


# ===================================================================================================== grammar helpers
def is_neg(stem):
    """Does a Burmese verb stem end in a negated verb («မ» + verb, or «မဟုတ်»)?"""
    last = re.split(r"[ ၊]", stem)[-1]
    last = last.replace("မနော", "")
    return bool(NEG_RX.search(last))


def pred(v, pl=True):
    """Attributive Mātikā string -> predicate («… သော» -> «… ကြသည်»; negative «… ကြ»); noun -> «… ဖြစ်ကြသည်»."""
    k = "ကြ" if pl else ""
    if v.endswith("သော"):
        s = v[:-3]
        if s.endswith("ပြီး"):                    # «… ပြီးသော» -> «… ကြပြီ»
            return s[:-4] + k + "ပြီ"
        if s.endswith("သေး") and is_neg(s):        # «မ… သေးသော» -> «မ… ကြသေး»
            return s[:-3] + k + "သေး"
        return s + k if is_neg(s) else s + k + "သည်"
    if v.endswith("မည့်"):
        return v[:-4] + k + "မည်"
    if v.endswith("၏"):
        return f"{v} {DHP if pl else DH} ဖြစ်{k}သည်"
    return f"{v} ဖြစ်{k}သည်"


def join2(a, b):
    """Two attributive items of one phrase: «A-သော» + «B-သော» -> «A-၍ B-သော» (negative A: «A-ဘဲ B-သော»)."""
    if not a.endswith("သော"):
        raise F.Miss("join2: " + a)
    s = a[:-3]
    return f"{s}{'ဘဲ' if is_neg(s) else '၍'} {b}"


def loc(v):
    """Attributive Mātikā string -> locative noun «… သည်၌» (kāmāvacare = in what belongs to the sense sphere)."""
    if not v.endswith("သော"):
        raise F.Miss("loc: " + v)
    return v[:-3] + "သည်၌"


# ===================================================================================================== building blocks
ABY = T["abyākatā"]                                   # ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော
NEITHER = ABY[:-3]                                    # neva kusalā nākusalā
KUS, AKUS = T["kusalā"], T["akusalā"]
ROOT_ = F.ROOT
CL = F.CL
NUMW = {"tīṇi": "ti", "tayo": "ti", "cattāro": "catu", "cattāri": "catu", "pañca": "pañca", "cha": "cha",
        "nava": "nava", "dasa": "dasa", "dve": "dvi", "satta": "satta"}


def num(x, stem):
    return F.count_my(x, stem)


THAP = F.THAPETVA                                     # «ကို ချန်ထား၍»
TATTHA = "ထိုတို့အနက်"                                # Tattha (among those)
VUCC = "ဤသည်ကို {}ဟု ခေါ်သည်"                         # ayaṃ / idaṃ vuccati X
IME_PL = f"ဤ{DHP}သည်"                                 # ime dhammā … (subject of the closer)
CCD = f"{F.MIND}နှင့် {F.MIND}၏ အဖော် {DHP}"            # cittacetasikā dhammā
KIRIYA = F.KIRIYA[:-3]                                  # kiriyā (merely functional), verb stem (shared form)
SABBA_RUPA = "ရုပ် အားလုံးလည်း"                         # sabbañca rūpaṃ
ASANKH_DH = f"{T['asaṅkhatā']} ဓာတ်"                    # asaṅkhatā dhātu
AVASESA = "ကြွင်းကျန်သော"                                # avasesa
TAM_SAMP = "ထိုတို့နှင့် ယှဉ်တွဲသော"                      # taṃsampayutta
TAM_SAMU = "ထိုတို့မှ ဖြစ်ပေါ်လာသော"                     # taṃsamuṭṭhāna
TADEK = "ထိုတို့နှင့် တစ်နေရာတည်း တည်ရှိသော"               # tadekaṭṭha
KAMMA_KATATTA = "ကံကို ပြုခဲ့ခြင်းကြောင့်"                  # kammassa katattā
BHUMI = "ရှိရာ အဆင့်၌"                                   # -bhūmiyaṃ (in the plane / level where X is)
MAGGA, ARIYA = F.MAGGA, "အရိယာ"
PHALA = "ဖိုလ်"
KHANDHA = F.KHANDHA
VIN = F.VINNANA
AYAT = "အာရုံခံ နယ်ပယ်"
OBJ = {"rūpa": "အဆင်းအရောင်", "sadda": "အသံ", "gandha": "အနံ့", "rasa": "အရသာ", "phoṭṭhabba": "အထိအတွေ့",
       "dhamma": DH}
ORGAN = {"cakkhu": "မျက်စိ", "sota": "နား", "ghāna": "နှာခေါင်း", "jivhā": "လျှာ", "kāya": "ကိုယ်"}
DUKKHA_T = "ဒုက္ခ"                                       # dukkha (the truth of suffering; not the feeling «နာကျင်»)
SAMMADITTHI = F.NAMES["sammādiṭṭhi"]
DITTHI = "အယူ"                                           # diṭṭhi (as in the sample: sammādiṭṭhi, bhavadiṭṭhi …)
MICCHADITTHI = "မှားယွင်းသော အယူ"
KAMA = "ကာမ"                                             # kāma (sensual pleasure; everyday word)
BHAVA = "ဘဝ"
RAGA = "ရာဂ"                                             # rāga (lust; everyday word); taṇhā = «… ကို တပ်မက်မှု»
VICI = "ယုံမှားမှု"                                       # vicikicchā (kept apart from kaṅkhā = «သံသယ»)
SKD = "ကိုယ်ကို အတ္တဟု ယူဆသော အယူ"                        # sakkāyadiṭṭhi
SBP = "သီလ အကျင့်ဝတ်ဆိုင်ရာ မှားယွင်းသော ယူဆမှု"            # sīlabbataparāmāsa (parāmāsa = FAMILY N)
ATTA = "အတ္တ"
N_ = {st: d["N"] for st, d in F.FAMILY.items()}            # cluster nouns

# ===================================================================================================== headings, colophons
NIK = "အကျဉ်း ဖော်ပြချက်"                                  # nikkhepa (brief exposition)
_HEADS = {
    "Nikkhepakaṇḍaṃ": f"{NIK} {F.KANDA}",
    "Tikanikkhepaṃ": f"{F.TIKA} {NIK}",
    "Dukanikkhepaṃ": f"{F.DUKA} {NIK}",
    "Suttantikadukanikkhepaṃ": f"သုတ္တန် {F.DUKA} {NIK}",
}
_COLOS = {
    "Tikaṃ": F.TIKA,
    "Abhidhammadukaṃ": f"အဘိဓမ္မာ {F.DUKA}",
    "Nikkhepakaṇḍe paṭhamabhāṇavāro": f"{NIK} {F.KANDA}၌ {F.ORD['paṭhama']} {F.BHANAVARA}",
    "Nikkhepakaṇḍe dutiyabhāṇavāro": f"{NIK} {F.KANDA}၌ {F.ORD['dutiya']} {F.BHANAVARA}",
    "Nikkhepakaṇḍaṃ niṭṭhitaṃ": f"“{NIK} {F.KANDA}” {F.NITTHITA}",
}
for _k, _v in _HEADS.items():
    add(F.HEAD, _k, _v)
for _k, _v in _COLOS.items():
    add(F.COLO, _k, _v)

# ===================================================================================================== variant readings
add(F.SIGLA, "bahūsu", "Bahūsu")
for _k, _v in {
    "diṭṭhivisūkāyitaṃ": F.PATHA, "nandirāgo": F.LEKHANA, "sibbanī": F.LEKHANA, "āyūhanī": F.LEKHANA,
    "āsiṃsanā āsiṃsitattaṃ": F.LEKHANA, "bhavacchando": F.LEKHANA, "uṇṇati uṇṇāmo": F.LEKHANA,
    "ussuyā ussuyanā ussuyitattaṃ": F.LEKHANA, "uparimaṃ": F.PATHA, "rūpā": F.PATHA,
    "nīvaraṇāni": F.PATHA, "kāmūpādānaṃ diṭṭhūpādānaṃ sīlabbatūpādānaṃ attavādūpādānaṃ": F.LEKHANA,
    "samaggatā": F.PATHA, "paranimmitavasavattideve": F.LEKHANA, "akaniṭṭhadeve": F.LEKHANA,
    "diṭṭhadhammasukhavihārassa": F.PATHA, "upādāya": F.PATHA, "saṃvejanīyaṃ": F.LEKHANA,
    "cittassa ca": F.PATHA,
}.items():
    add(F.VAR_KIND, _k, _v)
MULTI_VAR = {   # one bracket with two readings: «[a (s1) b (s2)]»
    "[puñcikatā (syā.) pucchikatā (sī.)]": f"[{F.LEKHANA} (Syā.): puñcikatā၊ (Sī.): pucchikatā]",
}
_var_my_orig = F.var_my


def _var_my(br):
    if br in MULTI_VAR:
        return MULTI_VAR[br]
    return _var_my_orig(br)


F.var_my = _var_my           # in memory only: list_items() and r_var() look the name up in F at call time

# ===================================================================================================== lexicon
SYN = {}      # new synonyms / names (added to F.SYN: list items and stand-alone words)
PH = {}       # fixed phrases and clauses (stand-alone only)
LISTABLE = set()   # nouns that may stand in a space-separated series (joined with «၊»)


def syn(d, listable=False):
    d = F.harm(d)                  # the shared synonym table of the akusala factors (consistency pass)
    for k, v in d.items():
        add(SYN, k, v)
        if listable:
            LISTABLE.add(k)


def ph(d, listable=False):
    for k, v in d.items():
        add(PH, k, v)
        if listable:
            LISTABLE.add(k)


# ---------------------------------------------------------------------------------------- roots, aggregates, kamma
syn({"lobho": "လောဘ", "doso": "ဒေါသ", "moho": "မောဟ"}, True)
LISTABLE.update(["alobho", "adoso", "amoho", "vedanākkhandho", "saññākkhandho", "saṅkhārakkhandho",
                 "viññāṇakkhandho", "vedanā", "saññā"])
ph({"rūpakkhandho": f"ရုပ် {KHANDHA}", "rūpaṃ": "ရုပ်", "saṅkhārā": f"{F.SANKHARA}များ", "viññāṇaṃ": VIN,
    "kāyakammaṃ": "ကိုယ်ဖြင့် ပြုသော ကံ", "vacīkammaṃ": "နှုတ်ဖြင့် ပြုသော ကံ",
    "manokammaṃ": f"{F.MANO}ဖြင့် ပြုသော ကံ"}, True)
ph({
    "Tīṇi kusalamūlāni": num(f"{KUS}၏ {ROOT_}", "ti"), "Tīṇi akusalamūlāni": num(f"{AKUS}၏ {ROOT_}", "ti"),
    "taṃsampayutto": TAM_SAMP, "taṃsamuṭṭhānaṃ": TAM_SAMU,
    "tadekaṭṭhā ca kilesā": f"{TADEK} {F.KIL}များလည်း", "Tadekaṭṭho": TADEK, "Avaseso": AVASESA,
    "avasesā": AVASESA,
    "Kusalākusalānaṃ dhammānaṃ vipākā": f"{KUS}နှင့် {AKUS} {DH}တို့၏ အကျိုး ဖြစ်သော",
    "Kusalākusalānaṃ dhammānaṃ avipakkavipākānaṃ vipākā":
        f"အကျိုး မရင့်ကျက်သေးသော {KUS}နှင့် {AKUS} {DH}တို့၏ အကျိုး ဖြစ်သော",
    "ye ca dhammā kiriyā neva kusalā nākusalā na ca kammavipākā":
        f"{F.KIRIYA_ATTR} {DHP}လည်း",
    "sabbañca rūpaṃ": SABBA_RUPA, "asaṅkhatā ca dhātu": f"{ASANKH_DH}လည်း", "Asaṅkhatā dhātu": ASANKH_DH,
    "Kusalākusalā dhammā": f"{KUS}နှင့် {AKUS} {DHP}",
    "kusalābyākatā dhammā": f"{KUS}နှင့် {ABY} {DHP}",
    "kusalākusalābyākatā dhammā": f"{KUS}၊ {AKUS}နှင့် {ABY} {DHP}",
    "Sabbeva kāmāvacarā kusalākusalābyākatā dhammā": f"{T['kāmāvacarā']} {KUS}၊ {AKUS}၊ {ABY} {DHP} အားလုံးပင်",
    "maggā ca": f"{MAGGA}များလည်း", "maggaphalāni ca": f"{MAGGA}၏ {PHALA}များလည်း",
    "yañca rūpaṃ kammassa katattā": f"{KAMMA_KATATTA} ဖြစ်သော ရုပ် ရှိသမျှလည်း",
    "yañca rūpaṃ na kammassa katattā": f"{KAMMA_KATATTA} ဖြစ်သည် မဟုတ်သော ရုပ် ရှိသမျှလည်း",
    "yañca rūpaṃ kammassa katattā uppajjissati": f"{KAMMA_KATATTA} ဖြစ်ပေါ်လာမည့် ရုပ်လည်း",
    "Te dhamme ṭhapetvā": f"ထို{DH}တို့{THAP}",
    "Cattāro maggā apariyāpannā": f"{T['apariyāpannā']} {num(MAGGA, 'catu')}",
    "heṭṭhimāni ca tīṇi sāmaññaphalāni": f"အောက်ပိုင်း {num(F.SAMANNAPHALA, 'ti')}လည်း",
    "Upariṭṭhimaṃ": "အမြင့်ဆုံး", "arahattaphalaṃ": f"ရဟန္တာ {PHALA}",
    "Pañca kammāni ānantarikāni": f"နောက်ဘဝ၌ ချက်ချင်း အကျိုးပေးသော {num('ကံ', 'pañca')}",
    "yā ca micchādiṭṭhiniyatā": f"ကျိန်းသေသော {MICCHADITTHI}လည်း",
    "yā ca micchādiṭṭhi niyatā": f"ကျိန်းသေသော {MICCHADITTHI}လည်း",
    "Ariyamaggaṃ ārabbha ye uppajjanti cittacetasikā dhammā": f"{ARIYA} {MAGGA}ကို အာရုံပြု၍ ဖြစ်ပေါ်ကြသော {CCD}",
    "Ariyamaggaṃ adhipatiṃ karitvā ye uppajjanti cittacetasikā dhammā":
        f"{ARIYA} {MAGGA}ကို အကြီးအမှူး ပြု၍ ဖြစ်ပေါ်ကြသော {CCD}",
    "Ariyamaggasamaṅgissa": f"{ARIYA} {MAGGA}နှင့် ပြည့်စုံသူ၏",
    "maggaṅgāni ṭhapetvā": f"{MAGGA}၏ အင်္ဂါတို့{THAP}",
    "sammādiṭṭhi maggo ceva hetu ca": f"{SAMMADITTHI}သည် {MAGGA}လည်း ဖြစ်၊ {ROOT_}လည်း ဖြစ်သည်",
    "sammādiṭṭhiṃ ṭhapetvā": f"{SAMMADITTHI}{THAP}",
    "vīmaṃsādhipateyyaṃ maggaṃ bhāvayantassa": f"{F.JH_Q['vīmaṃsādhipateyyaṃ']} {MAGGA}ကို ပွားများနေသူ၏",
    "vīmaṃsaṃ ṭhapetvā": f"{F.VIMAMSA}{THAP}",
    "Tadubhayaṃ": "ထိုနှစ်မျိုးလုံး",
    "yañca rūpaṃ anidassanaṃ appaṭighaṃ dhammāyatanapariyāpannaṃ":
        f"{T['anidassanaappaṭighā']}၊ {DH} {AYAT}၌ အကျုံးဝင်သော ရုပ် ရှိသမျှလည်း",   # the Mātikā term, as 5
    "Pañcakkhandhā": num(KHANDHA, "pañca"),
    "Cattāro ca mahābhūtā": f"{num('မူလဓာတ်ကြီး', 'catu')}လည်း",
    "catunnañca mahābhūtānaṃ upādāya rūpaṃ": f"{num('မူလဓာတ်ကြီး', 'catu')}ကို မှီ၍ ဖြစ်သော ရုပ်လည်း",
    "Kusalānaṃ vā dhammānaṃ vipākato": f"{KUS} {DH}တို့၏ အကျိုး အဖြစ်ဖြင့်ဖြစ်စေ",
    "kiriyābyākatesu vā dhammesu": f"{KIRIYA}သော {ABY} {DH}တို့၌ဖြစ်စေ",
    "Kusalānaṃ dhammānaṃ vipākato": f"{KUS} {DH}တို့၏ အကျိုး အဖြစ်ဖြင့်",
})
for _k in ["Sāsavā", "Apariyāpannā", "Rūpāvacarā"]:
    add(PH, _k, T[_k[0].lower() + _k[1:]])
for _k in ["kāmāvacarā", "rūpāvacarā", "arūpāvacarā", "apariyāpannā"]:
    add(PH, _k, T[_k])
    LISTABLE.add(_k)
for _k in ["kāmāvacarā", "rūpāvacarā", "arūpāvacarā", "apariyāpannā"]:   # locative kāmāvacare …
    add(PH, _k[:-1] + "e", loc(T[_k]))
    LISTABLE.add(_k[:-1] + "e")
# planes of consciousness («X-bhūmiyaṃ»)
_BH = {
    "Sukha": f"{F.SUKHA}မှု", "Dukkha": f"{F.DUKKHA}မှု", "Adukkhamasukha": f"မ{F.DUKKHA} မ{F.SUKHA}မှု",
    "Savitakkasavicāra": f"{F.VIT}နှင့် {F.VIC}", "Avitakkavicāramatta": None, "Avitakkaavicāra": None,
    "Pīti": "ပီတိ", "Upekkhā": "ဥပေက္ခာ", "Savitakka": F.VIT, "Savicāra": F.VIC, "Sappītika": "ပီတိ",
}
for _k, _v in _BH.items():
    if _v:
        ph({_k + "bhūmiyaṃ": f"{_v} {BHUMI}"})
ph({"Avitakkavicāramattabhūmiyaṃ": f"{F.VIT} မရှိဘဲ {F.VIC}သာ {BHUMI}",
    "Avitakkaavicārabhūmiyaṃ": f"{F.VIT}လည်း မရှိ၊ {F.VIC}လည်း မ{BHUMI}",
    "Avitakkabhūmiyaṃ": f"{F.VIT} မ{BHUMI}", "Avicārabhūmiyaṃ": f"{F.VIC} မ{BHUMI}",
    "Appītikabhūmiyaṃ": f"ပီတိ မ{BHUMI}",
    "Na pītibhūmiyaṃ": f"ပီတိ {BHUMI[:-1]} မဟုတ်သည့် နေရာ၌",
    "Na sukhabhūmiyaṃ": f"{F.SUKHA}မှု {BHUMI[:-1]} မဟုတ်သည့် နေရာ၌",
    "Na upekkhābhūmiyaṃ": f"ဥပေက္ခာ {BHUMI[:-1]} မဟုတ်သည့် နေရာ၌"})
ph({"sukhaṃ vedanaṃ ṭhapetvā": f"{F.SUKHA}သော {F.FEEL}{THAP}",
    "dukkhaṃ vedanaṃ ṭhapetvā": f"{F.DUKKHA}သော {F.FEEL}{THAP}",
    "adukkhamasukhaṃ vedanaṃ ṭhapetvā": f"မ{F.DUKKHA} မ{F.SUKHA}သော {F.FEEL}{THAP}",
    "vitakkavicāre ṭhapetvā": f"{F.VIT}နှင့် {F.VIC}{THAP}", "vicāraṃ ṭhapetvā": f"{F.VIC}{THAP}",
    "vitakkaṃ ṭhapetvā": f"{F.VIT}{THAP}", "pītiṃ ṭhapetvā": f"ပီတိ{THAP}",
    "sukhaṃ ṭhapetvā": f"{F.SUKHA}မှု{THAP}", "upekkhaṃ ṭhapetvā": f"ဥပေက္ခာ{THAP}"})

# ---------------------------------------------------------------------------------------- bases (āyatana), elements
for _o, _om in OBJ.items():
    _p = {"rūpa": "Rūpāyatanaṃ", "sadda": "saddāyatanaṃ", "gandha": "gandhāyatanaṃ", "rasa": "rasāyatanaṃ",
          "phoṭṭhabba": "phoṭṭhabbāyatanaṃ", "dhamma": None}[_o]
    if _p:
        ph({_p[0].lower() + _p[1:]: f"{_om} {AYAT}"}, True)
for _o, _p in {"cakkhu": "cakkhāyatanaṃ", "sota": "sotāyatanaṃ", "ghāna": "ghānāyatanaṃ",
               "jivhā": "jivhāyatanaṃ", "kāya": "kāyāyatanaṃ"}.items():
    ph({_p: f"{ORGAN[_o]} {AYAT}"}, True)
    ph({_o + "viññāṇaṃ": f"{ORGAN[_o]} {VIN}"}, True)
    ph({_o + "viññeyyā": f"{ORGAN[_o]}ဖြင့် သိနိုင်သော"})
LISTABLE.update(["manāyatanaṃ", "dhammāyatanaṃ", "manoviññāṇadhātu"])
ph({"manodhātu": f"{F.MANO} ဓာတ်"}, True)

# ---------------------------------------------------------------------------------------- uppanna / atīta lists
syn({"jātā": "မွေးဖွားပြီးသော", "bhūtā": "ဖြစ်ပြီးသော", "sañjātā": "ကောင်းစွာ မွေးဖွားပြီးသော",
     "nibbattā": "ပေါ်ထွက်ပြီးသော", "abhinibbattā": "ထင်ရှားစွာ ပေါ်ထွက်ပြီးသော", "pātubhūtā": "ထင်ရှားလာပြီးသော",
     "uppannā": T["uppannā"], "samuppannā": "ကောင်းစွာ ဖြစ်ပေါ်ပြီးသော", "uṭṭhitā": "ထပေါ်ပြီးသော",
     "samuṭṭhitā": "ကောင်းစွာ ထပေါ်ပြီးသော",
     "ajātā": "မမွေးဖွားသေးသော", "abhūtā": "မဖြစ်သေးသော", "asañjātā": "ကောင်းစွာ မမွေးဖွားသေးသော",
     "anibbattā": "မပေါ်ထွက်သေးသော", "anabhinibbattā": "ထင်ရှားစွာ မပေါ်ထွက်သေးသော",
     "apātubhūtā": "ထင်ရှား မလာသေးသော", "anuppannā": T["anuppannā"],
     "asamuppannā": "ကောင်းစွာ မဖြစ်ပေါ်သေးသော", "anuṭṭhitā": "မထပေါ်သေးသော",
     "asamuṭṭhitā": "ကောင်းစွာ မထပေါ်သေးသော",
     "atītā": pred(T["atītā"], False)[:-3] + "သော",           # «အတိတ် ဖြစ်သော» (noun term made attributive)
     "anāgatā": pred(T["anāgatā"], False)[:-3] + "သော",
     "paccuppannā": pred(T["paccuppannā"], False)[:-3] + "သော",
     "niruddhā": "ချုပ်ငြိမ်းပြီးသော", "vigatā": "ကင်းပျောက်ပြီးသော", "vipariṇatā": "ဖောက်ပြန် ပြောင်းလဲပြီးသော",
     "atthaṅgatā": "ကွယ်ပျောက်ပြီးသော", "abbhatthaṅgatā": "လုံးဝ ကွယ်ပျောက်ပြီးသော",
     "uppajjitvā vigatā": "ဖြစ်ပေါ်ပြီးမှ ကင်းပျောက်ပြီးသော"})
for _k in ["uppanna", "anuppanna", "atīta", "anāgata", "paccuppanna"]:
    _b = T[_k[:-1] + "ā"]
    syn({f"{_k[:-1]}aṃsena saṅgahitā": f"{_b} အပိုင်း၌ အကျုံးဝင်သော"})
syn({"ajjhattaṃ": "မိမိ၏ အတွင်း၌ ဖြစ်သော", "paccattaṃ": "ကိုယ်စီ ဖြစ်သော", "niyatā": "သီးသန့် ဖြစ်သော",
     "pāṭipuggalikā": "ပုဂ္ဂိုလ်တစ်ဦးချင်းစီ၏ ဖြစ်သော", "upādiṇṇā": T["upādiṇṇā"]})
YE_GEN = {"tesaṃ tesaṃ sattānaṃ": "ထိုထို သတ္တဝါတို့၏",
          "tesaṃ tesaṃ parasattānaṃ parapuggalānaṃ": "ထိုထို အခြား သတ္တဝါ၊ အခြား ပုဂ္ဂိုလ်တို့၏"}

# ---------------------------------------------------------------------------------------- the three fetters, views
ph({"Tīṇi saṃyojanāni": num(N_["saṃyojana"], "ti"), "Imāni tīṇi saṃyojanāni": f"ဤ{num(N_['saṃyojana'], 'ti')}",
    "sakkāyadiṭṭhi": SKD, "sīlabbataparāmāso": SBP}, True)
syn({"vicikicchā": VICI}, True)
ph({"Idha assutavā puthujjano ariyānaṃ adassāvī ariyadhammassa akovido ariyadhamme avinīto sappurisānaṃ adassāvī "
    "sappurisadhammassa akovido sappurisadhamme avinīto":
    "ဤလောက၌ အကြားအမြင် မရှိသော ပုထုဇဉ်သည် အရိယာတို့ကို မမြင်ဖူးသူ၊ အရိယာတို့၏ တရား၌ မကျွမ်းကျင်သူ၊ "
    "အရိယာတို့၏ တရား၌ မလေ့ကျင့်ထားသူ၊ သူတော်ကောင်းတို့ကို မမြင်ဖူးသူ၊ သူတော်ကောင်းတို့၏ တရား၌ "
    "မကျွမ်းကျင်သူ၊ သူတော်ကောင်းတို့၏ တရား၌ မလေ့ကျင့်ထားသူ ဖြစ်၍"})
_AGG = {   # aggregate: (Burmese, accusative, -vantaṃ stem, locative)
    "rūpa": ("ရုပ်", "rūpaṃ", "rūpavantaṃ", "rūpasmiṃ"),
    "vedanā": (F.FEEL, "vedanaṃ", "vedanāvantaṃ", "vedanāya"),
    "saññā": (F.SANNA, "saññaṃ", "saññāvantaṃ", "saññāya"),
    "saṅkhārā": (F.SANKHARA + "များ", "saṅkhāre", "saṅkhāravantaṃ", "saṅkhāresu"),
    "viññāṇa": (VIN, "viññāṇaṃ", "viññāṇavantaṃ", "viññāṇasmiṃ"),
}
for _a, (_m, _acc, _vant, _loc) in _AGG.items():
    ph({f"{_acc} attato samanupassati": f"{_m}ကို {ATTA}ဟု ရှုမြင်သည်",
        f"{_vant} vā attānaṃ": f"{ATTA}ကို {_m} ရှိသည်ဟုဖြစ်စေ",
        f"attani vā {_acc}": f"{ATTA}၌ {_m} ရှိသည်ဟုဖြစ်စေ",
        f"{_loc} vā attānaṃ": f"{_m}၌ {ATTA} ရှိသည်ဟုဖြစ်စေ ရှုမြင်သည်"})
    if _a in ("vedanā", "saññā", "saṅkhārā"):
        ph({_acc: f"{_m}ကို"})
# the view list (diṭṭhi … vipariyāsaggāho)
syn({"diṭṭhi": DITTHI, "diṭṭhigataṃ": f"{DITTHI}၌ ကျရောက်ခြင်း", "diṭṭhigahanaṃ": f"{DITTHI} တောအုပ်",
     "diṭṭhikantāro": f"{DITTHI} ကန္တာရ", "diṭṭhivisūkāyikaṃ": f"{DITTHI}၏ ကောက်ကွေးမှု",
     "diṭṭhivipphanditaṃ": f"{DITTHI}၏ တုန်လှုပ်မှု", "diṭṭhisaṃyojanaṃ": f"{DITTHI} {N_['saṃyojana']}",
     "gāho": "စွဲကိုင်ခြင်း", "paṭiggāho": "ခိုင်မြဲစွာ စွဲကိုင်ခြင်း", "patiṭṭhāho": "ခိုင်မြဲစွာ စွဲကိုင်ခြင်း",
     "abhiniveso": "သက်ဝင်ယုံကြည်ခြင်း", "parāmāso": N_["parāmāsa"], "kummaggo": "လမ်းမှား",
     "micchāpatho": "မှားယွင်းသော လမ်းကြောင်း", "micchattaṃ": "မှားယွင်းမှု",
     "titthāyatanaṃ": "အယူဝါဒတို့၏ တည်ရာ", "vipariyāsaggāho": "ပြောင်းပြန် စွဲကိုင်ခြင်း"})
add(F.GEN, "evarūpā", "ဤသို့ သဘောရှိသော")
add(F.GEN, "evarūpo", "ဤသို့ သဘောရှိသော")
add(F.GEN, "evarūpaṃ", "ဤသို့ သဘောရှိသော")
add(F.GEN, "evarūpo cittassa", f"ဤသို့ သဘောရှိသော {F.MIND}၏")
# vicikicchā
_VLOC = {"Satthari": "ဘုရားရှင်", "dhamme": "တရားတော်", "saṅghe": "သံဃာတော်", "sikkhāya": "ကျင့်စဉ်",
         "pubbante": "အတိတ်ကာလ", "aparante": "အနာဂတ်ကာလ", "pubbantāparante": "အတိတ်ကာလနှင့် အနာဂတ်ကာလ",
         "idappaccayatā paṭiccasamuppannesu dhammesu":
             f"ဤအကြောင်းကြောင့် ဤအကျိုး ဖြစ်ပုံနှင့် အကြောင်းတို့ကို မှီ၍ ဖြစ်ပေါ်လာသော {DH}တို့"}
for _k, _v in _VLOC.items():
    ph({f"{_k} kaṅkhati vicikicchati": f"{_v}အပေါ် သံသယ ဖြစ်၍ ယုံမှားသည်"})
syn({"kaṅkhā": "သံသယ", "kaṅkhāyanā": "သံသယ ဖြစ်ခြင်း", "kaṅkhāyitattaṃ": "သံသယ ဖြစ်ထားသော အဖြစ်",
     "vimati": "စိတ်ရှုပ်ထွေးခြင်း", "dveḷhakaṃ": "စိတ် နှစ်ခွ ဖြစ်ခြင်း", "dvedhāpatho": "လမ်း နှစ်ခွ",
     "saṃsayo": "ဒွိဟ ဖြစ်ခြင်း", "anekaṃsaggāho": "တစ်ထစ်ချ မယူနိုင်ခြင်း", "āsappanā": "ယိမ်းယိုင်ခြင်း",
     "parisappanā": "ပတ်ချာလည် ယိမ်းယိုင်ခြင်း", "apariyogāhanā": "နက်နက်နဲနဲ မသက်ဝင်နိုင်ခြင်း",
     "thambhitattaṃ cittassa": f"{F.MIND} တောင့်တင်းနေသော အဖြစ်", "manovilekho": f"{F.MANO}ကို ခြစ်ကုတ်ခြင်း"})
# sīlabbataparāmāsa
_SILA, _VATA = "သီလ", "အကျင့်ဝတ်"
_SUD = "စင်ကြယ်ခြင်း ရှိသည်"
ph({"Ito bahiddhā samaṇabrāhmaṇānaṃ": "ဤသာသနာ အပြင်ဘက်ရှိ ရဟန်းပုဏ္ဏားတို့၏",
    "‘sīlena suddhi": f"“{_SILA}ဖြင့် {_SUD}", "sīlena suddhi": f"{_SILA}ဖြင့် {_SUD}",
    "vatena suddhi": f"{_VATA}ဖြင့် {_SUD}",
    "sīlabbatena suddhī’ti": f"{_SILA}နှင့် {_VATA}ဖြင့် {_SUD}”ဟူ၍",
    "sīlabbatena suddhīti": f"{_SILA}နှင့် {_VATA}ဖြင့် {_SUD}ဟူ၍"})
CLOSE_EXTRA = {   # «ime dhammā X» with an X that is not a Mātikā item
    "dassanena pahātabbahetū": f"{F.DASS} {F.PAH} {ROOT_}များ",
    "bhāvanāya pahātabbahetū": f"{F.BHAV} {F.PAH} {ROOT_}များ",
    "maggahetū": f"{MAGGA}၏ {ROOT_}များ",
}

# ---------------------------------------------------------------------------------------- the roots in the hetu cluster
HETU_KIND = {"kusala": KUS, "akusala": AKUS, "abyākata": ABY, "kāmāvacara": T["kāmāvacarā"],
             "rūpāvacara": T["rūpāvacarā"], "arūpāvacara": T["arūpāvacarā"], "apariyāpanna": T["apariyāpannā"]}
syn({"metti": "မေတ္တာ", "mettāyanā": "မေတ္တာ ထားခြင်း", "mettāyitattaṃ": "မေတ္တာ ထားသော အဖြစ်",
     "anuddā": "သနားကြင်နာခြင်း", "anuddāyanā": "သနားကြင်နာနေခြင်း", "anudāyitattaṃ": "သနားကြင်နာထားသော အဖြစ်",
     "hitesitā": "အကျိုးကို လိုလားခြင်း", "anukampā": "စာနာ ထောက်ထားခြင်း",
     "dhammavicayasambojjhaṅgo": f"{F.SYN['dhammavicayo']} ဟူသော သိမြင်ခြင်း၏ အင်္ဂါ",
     "maggaṅgaṃ": f"{MAGGA}၏ အင်္ဂါ", "maggapariyāpannaṃ": f"{MAGGA}၌ အကျုံးဝင်သော အရာ"})
_ÑLOC = {"Dukkhe": DUKKHA_T, "dukkhasamudaye": f"{DUKKHA_T} ဖြစ်ပေါ်ခြင်း",
         "dukkhanirodhe": f"{DUKKHA_T} ချုပ်ငြိမ်းခြင်း",
         "dukkhanirodhagāminiyā paṭipadāya": f"{DUKKHA_T} ချုပ်ငြိမ်းရာသို့ ရောက်စေသော {F.PATIPADA}",
         "pubbante": "အတိတ်ကာလ", "aparante": "အနာဂတ်ကာလ", "pubbantāparante": "အတိတ်ကာလနှင့် အနာဂတ်ကာလ",
         "idappaccayatā paṭiccasamuppannesu dhammesu": _VLOC["idappaccayatā paṭiccasamuppannesu dhammesu"]}
for _k, _v in _ÑLOC.items():
    ph({f"{_k} ñāṇaṃ": f"{_v}ကို သိသော ဉာဏ်", f"{_k} aññāṇaṃ": f"{_v}ကို မသိခြင်း"})
# moha list
syn({"aññāṇaṃ": "မသိခြင်း", "adassanaṃ": "မမြင်ခြင်း", "anabhisamayo": "ထင်ထင်ရှားရှား မသိမြင်ခြင်း",
     "ananubodho": "လိုက်၍ မနားလည်ခြင်း", "asambodho": "ကောင်းစွာ မနားလည်ခြင်း",
     "appaṭivedho": "ထိုးဖောက်၍ မသိခြင်း", "asaṃgāhanā": "စုစည်း၍ မယူနိုင်ခြင်း",
     "asamapekkhanā": "ညီညီညွတ်ညွတ် မရှုမြင်ခြင်း", "apaccavekkhaṇā": "ပြန်လည် မဆင်ခြင်ခြင်း",
     "apaccakkhakammaṃ": "ကိုယ်တိုင် ထင်ထင်ရှားရှား မပြုခြင်း", "dummejjhaṃ": "ဉာဏ်နုံခြင်း",
     "bālyaṃ": "မိုက်မဲခြင်း", "asampajaññaṃ": F.SUT["asampajañña"], "pamoho": "အလွန် တွေဝေခြင်း",
     "sammoho": "လုံးဝ တွေဝေခြင်း", "avijjā": F.SUT["avijjā"],
     "avijjogho": f"{F.SUT['avijjā']} {N_['ogha']}", "avijjāyogo": f"{F.SUT['avijjā']} {N_['yoga']}",
     "avijjānusayo": f"{F.SUT['avijjā']} ကိန်းအောင်းခြင်း",
     "avijjāpariyuṭṭhānaṃ": f"{F.SUT['avijjā']} ထကြွခြင်း", "avijjālaṅgī": f"{F.SUT['avijjā']} တံခါးကန့်လန့်",
     "akusalamūlaṃ": f"{AKUS}၏ {ROOT_}"})
# lobha list
syn({"rāgo": RAGA, "sārāgo": "တပ်မက်ခြင်း", "anunayo": "လိုက်လျောခြင်း", "anurodho": "သဘောတူ လိုက်ပါခြင်း",
     "nandī": "နှစ်သက်ခြင်း", "nandīrāgo": f"နှစ်သက်မှု {RAGA}", "cittassa sārāgo": f"{F.MIND}၏ တပ်မက်ခြင်း",
     "icchā": "အလိုရှိခြင်း", "mucchā": "မိန်းမောခြင်း", "ajjhosānaṃ": "နစ်မွန်းခြင်း",
     "gedho": "ငမ်းငမ်းတက် လိုချင်ခြင်း", "paligedho": "အလွန် ငမ်းငမ်းတက် လိုချင်ခြင်း",
     "saṅgo": "တွယ်ကပ်ခြင်း", "paṅko": "ရွှံ့ညွန်", "ejā": "တုန်လှုပ်ခြင်း", "māyā": "လှည့်စားတတ်ခြင်း",
     "janikā": "မွေးဖွားပေးတတ်သူ", "sañjananī": "ကောင်းစွာ မွေးဖွားပေးတတ်သူ", "sibbinī": "ချုပ်လုပ်တတ်သူ",
     "jālinī": "ပိုက်ကွန်ကဲ့သို့ ဖြစ်သူ", "saritā": "စီးဆင်းတတ်သူ", "visattikā": "ပျံ့နှံ့ တွယ်ကပ်တတ်သူ",
     "suttaṃ": "ချည်ကြိုး", "visaṭā": "ပျံ့နှံ့ခြင်း", "āyūhinī": "ကြိုးပမ်းစေတတ်သူ", "dutiyā": "အဖော်",
     "paṇidhi": "စိတ်ညွှတ်ခြင်း", "bhavanetti": f"{BHAVA}သို့ ဆွဲဆောင်သော ကြိုး", "vanaṃ": "တော",
     "vanatho": "တောအုပ်", "santhavo": "ရင်းနှီးခြင်း", "sineho": "ချစ်ခင်ခြင်း", "apekkhā": "ငဲ့ကွက်ခြင်း",
     "paṭibandhu": "ဆွေမျိုး", "āsā": "မျှော်လင့်ခြင်း", "āsisanā": "တောင့်တခြင်း",
     "āsisitattaṃ": "တောင့်တထားသော အဖြစ်",
     "lābhāsā": "လာဘ်ကို မျှော်လင့်ခြင်း", "dhanāsā": "ဥစ္စာကို မျှော်လင့်ခြင်း",
     "puttāsā": "သားသမီးကို မျှော်လင့်ခြင်း", "jīvitāsā": f"{F.SYN['jīvitaṃ']}ကို မျှော်လင့်ခြင်း",
     "jappā": "တမ်းတခြင်း", "pajappā": "အလွန် တမ်းတခြင်း", "abhijappā": "ထူးထူးခြားခြား တမ်းတခြင်း",
     "jappanā": "တမ်းတနေခြင်း", "jappitattaṃ": "တမ်းတထားသော အဖြစ်", "loluppaṃ": "လိုချင်လွန်းခြင်း",
     "loluppāyanā": "လိုချင်လွန်းနေခြင်း", "loluppāyitattaṃ": "လိုချင်လွန်းထားသော အဖြစ်",
     "pucchañjikatā": "အမြီး ခါ၍ ချော့မော့ခြင်း", "sādhukamyatā": "ကောင်းသည်ထက် ကောင်းသည်ကို လိုချင်ခြင်း",
     "adhammarāgo": f"မတရားသော {RAGA}", "visamalobho": "ဖောက်ပြန်သော လောဘ", "nikanti": "စွဲလန်းခြင်း",
     "nikāmanā": "အလွန် လိုလားခြင်း", "patthanā": "ဆုတောင်းခြင်း", "pihanā": "အားကျ လိုချင်ခြင်း",
     "sampatthanā": "ကောင်းစွာ ဆုတောင်းခြင်း",
     "bhavataṇhā": F.SUT["bhavataṇhā"], "vibhavataṇhā": f"{BHAVA} ပြတ်စဲခြင်းကို တပ်မက်မှု",
     "rūpataṇhā": "ရုပ်ကို တပ်မက်မှု", "arūpataṇhā": "ရုပ်မရှိသော ဘဝကို တပ်မက်မှု",
     "nirodhataṇhā": "ချုပ်ငြိမ်းခြင်းကို တပ်မက်မှု", "dhammataṇhā": f"{DH}ကို တပ်မက်မှု",
     "ogho": N_["ogha"], "yogo": N_["yoga"], "gantho": N_["gantha"], "upādānaṃ": N_["upādāna"],
     "āvaraṇaṃ": "ပိတ်ဆို့ခြင်း", "nīvaraṇaṃ": N_["nīvaraṇa"], "chādanaṃ": "ဖုံးအုပ်ခြင်း",
     "bandhanaṃ": "အချည်အနှောင်", "upakkileso": "ညစ်နွမ်းစေတတ်သော အညစ်အကြေး", "anusayo": "ကိန်းအောင်းခြင်း",
     "pariyuṭṭhānaṃ": "ထကြွခြင်း", "latā": "နွယ်ပင်", "vevicchaṃ": "တစ်ကိုယ်ကောင်းဆန်ခြင်း",
     "dukkhamūlaṃ": f"{DUKKHA_T}၏ အမြစ်", "dukkhanidānaṃ": f"{DUKKHA_T}၏ ဇာစ်မြစ်",
     "dukkhappabhavo": f"{DUKKHA_T}၏ ဖြစ်ပေါ်ရာ", "mārapāso": "မာရ်၏ ကျော့ကွင်း",
     "mārabaḷisaṃ": "မာရ်၏ ငါးမျှားချိတ်", "māravisayo": "မာရ်၏ နယ်ပယ်", "taṇhānadī": "တပ်မက်မှု မြစ်",
     "taṇhājālaṃ": "တပ်မက်မှု ပိုက်ကွန်", "taṇhāgaddulaṃ": "တပ်မက်မှု ကြိုးသိုင်း",
     "taṇhāsamuddo": "တပ်မက်မှု သမုဒ္ဒရာ", "abhijjhā": "သူ့ဥစ္စာကို လိုချင်ခြင်း"})
for _o, _om in OBJ.items():
    if _o != "dhamma":
        syn({_o[:-1] + "āsā": f"{_om}ကို မျှော်လင့်ခြင်း"})
        if _o != "rūpa":
            syn({_o + "taṇhā": f"{_om}ကို တပ်မက်မှု"})
# kāma- / bhava- lists (kāmāsava, bhavāsava, fetters, hindrance, clinging)
for _p, _pm in {"kāma": KAMA, "bhava": BHAVA}.items():
    syn({f"{_p}{'cchando' if _p == 'kāma' else 'chando'}": f"{_pm}ကို လိုလားမှု", f"{_p}rāgo": f"{_pm}{RAGA}",       # ကာမရာဂ / ဘဝရာဂ (one word, consistency pass)
         f"{_p}nandī": f"{_pm}ကို နှစ်သက်မှု", f"{_p}taṇhā": f"{_pm}ကို တပ်မက်မှု",
         f"{_p}sineho": f"{_pm}ကို ချစ်ခင်မှု", f"{_p}pariḷāho": f"{_pm}ကြောင့် ပူလောင်မှု",
         f"{_p}mucchā": f"{_pm}၌ မိန်းမောမှု", f"{_p}jjhosānaṃ": f"{_pm}၌ နစ်မွန်းမှု"})
add(F.GEN, "kāmesu", f"{KAMA}တို့၌ ရှိသော")
add(F.GEN, "bhavesu", f"{BHAVA}တို့၌ ရှိသော")
assert SYN["bhavataṇhā"] == F.SUT["bhavataṇhā"]
# dosa
_HARM, _GOOD = "မကောင်းမှု", "အကျိုး"
_AGH = "ရန်ငြိုးဖွဲ့ခြင်း ဖြစ်ပေါ်သည်"
_PIYA = "ငါ ချစ်ခင်သော နှစ်လိုဖွယ်ကောင်းသော သူအား"
_APIYA = "ငါ မချစ်ခင်သော နှစ်လိုဖွယ် မကောင်းသော သူအား"
ph({"Anatthaṃ me acarīti āghāto jāyati": f"ငါ့အား {_HARM} ပြုခဲ့ပြီဟု {_AGH}",
    "Anatthaṃ me acarī ti āghāto jāyati": f"ငါ့အား {_HARM} ပြုခဲ့ပြီဟု {_AGH}",
    "anatthaṃ me caratīti āghāto jāyati": f"ငါ့အား {_HARM} ပြုနေသည်ဟု {_AGH}",
    "anatthaṃ me carissatīti āghāto jāyati": f"ငါ့အား {_HARM} ပြုလိမ့်မည်ဟု {_AGH}",
    "piyassa me manāpassa anatthaṃ acari": f"{_PIYA} {_HARM} ပြုခဲ့ပြီ",
    "anatthaṃ carati": f"{_HARM} ပြုနေသည်",
    "anatthaṃ carissatīti āghāto jāyati": f"{_HARM} ပြုလိမ့်မည်ဟု {_AGH}",
    "appiyassa me amanāpassa atthaṃ acari": f"{_APIYA} {_GOOD}ကို ပြုခဲ့ပြီ",
    "atthaṃ carati": f"{_GOOD}ကို ပြုနေသည်",
    "atthaṃ carissatīti āghāto jāyati": f"{_GOOD}ကို ပြုလိမ့်မည်ဟု {_AGH}",
    "aṭṭhāne vā pana āghāto jāyati": f"အကြောင်း မရှိဘဲလည်း {_AGH}"})
syn({"āghāto": "ရန်ငြိုးဖွဲ့ခြင်း", "paṭighāto": "ပြန်လည် ရန်ငြိုးဖွဲ့ခြင်း", "paṭighaṃ": "စိတ်ထိခိုက်ခြင်း",
     "paṭivirodho": "ပြန်လည် ဆန့်ကျင်ခြင်း", "kopo": "အမျက်ထွက်ခြင်း", "pakopo": "အလွန် အမျက်ထွက်ခြင်း",
     "sampakopo": "ပြင်းစွာ အမျက်ထွက်ခြင်း", "padoso": "အလွန် ဒေါသထွက်ခြင်း",
     "sampadoso": "ပြင်းစွာ ဒေါသထွက်ခြင်း", "cittassa byāpatti": f"{F.MIND}၏ ဖောက်ပြန်ခြင်း",
     "manopadoso": f"{F.MANO}ဖြင့် ဒေါသထွက်ခြင်း", "kodho": "အမျက်ဒေါသ", "kujjhanā": "အမျက်ဒေါသ ထွက်ခြင်း",
     "kujjhitattaṃ": "အမျက်ဒေါသ ထွက်ထားသော အဖြစ်", "dussanā": "စိတ်ဆိုးခြင်း",
     "dussitattaṃ": "စိတ်ဆိုးထားသော အဖြစ်", "byāpatti": "ဖောက်ပြန်ခြင်း", "byāpajjanā": "ညှဉ်းဆဲလိုခြင်း",
     "byāpajjitattaṃ": "ညှဉ်းဆဲလိုသော အဖြစ်", "virodho": "ဆန့်ကျင်ခြင်း", "caṇḍikkaṃ": "ကြမ်းကြုတ်ခြင်း",
     "asuropo": "စကား ကြမ်းခြင်း", "anattamanatā cittassa": f"{F.MIND}၏ မနှစ်သိမ့်ခြင်း"})
assert SYN["dussanā"].replace("စိတ်ဆိုး", "စိတ်မဆိုး") == F.SYN["adussanā"]

# ---------------------------------------------------------------------------------------- the clusters
_CL_NAMES = {   # cluster member: Pāli nominative -> Burmese (instrumental = «…ဖြင့်»)
    "kāmāsavo": f"{KAMA} {N_['āsava']}", "bhavāsavo": f"{BHAVA} {N_['āsava']}",
    "diṭṭhāsavo": f"{DITTHI} {N_['āsava']}", "avijjāsavo": f"{F.SUT['avijjā']} {N_['āsava']}",
    "kāmarāgasaṃyojanaṃ": f"{F.KAMARAGA} {N_['saṃyojana']}",
    "paṭighasaṃyojanaṃ": f"{SYN['paṭighaṃ']} {N_['saṃyojana']}",
    "mānasaṃyojanaṃ": f"မာန {N_['saṃyojana']}", "diṭṭhisaṃyojanaṃ": SYN["diṭṭhisaṃyojanaṃ"],
    "vicikicchāsaṃyojanaṃ": f"{VICI} {N_['saṃyojana']}",
    "sīlabbataparāmāsasaṃyojanaṃ": f"{SBP} {N_['saṃyojana']}",
    "bhavarāgasaṃyojanaṃ": f"{F.BHAVARAGA} {N_['saṃyojana']}",
    "issāsaṃyojanaṃ": f"ငြူစူမှု {N_['saṃyojana']}", "macchariyasaṃyojanaṃ": f"ဝန်တိုမှု {N_['saṃyojana']}",
    "avijjāsaṃyojanaṃ": f"{F.SUT['avijjā']} {N_['saṃyojana']}",
    "abhijjhā kāyagantho": f"{SYN['abhijjhā']}ဟူသော ကိုယ် {N_['gantha']}",
    "byāpādo kāyagantho": f"ဖျက်ဆီးလိုစိတ်ဟူသော ကိုယ် {N_['gantha']}",
    "sīlabbataparāmāso kāyagantho": f"{SBP}ဟူသော ကိုယ် {N_['gantha']}",
    "idaṃsaccābhiniveso kāyagantho": f"ဤအရာသာ အမှန်ဟု {SYN['abhiniveso']}ဟူသော ကိုယ် {N_['gantha']}",
}
_CL_NAMES["abhijjhākāyagantho"] = _CL_NAMES["abhijjhā kāyagantho"]
_CL_NAMES["idaṃ saccābhiniveso kāyagantho"] = _CL_NAMES["idaṃsaccābhiniveso kāyagantho"]
assert F.NAMES["abyāpādo"] == "ဖျက်ဆီးလိုစိတ် မရှိခြင်း"
ph(_CL_NAMES, True)


def instr(pali_nom):
    """kāmāsavo -> kāmāsavena; saṃyojanaṃ -> saṃyojanena; diṭṭhi -> diṭṭhiyā; vicikicchā -> vicikicchāya."""
    w = pali_nom
    if w.endswith("o"):
        return w[:-1] + "ena"
    if w.endswith("aṃ"):
        return w[:-2] + "ena"
    if w.endswith("i"):
        return w + "yā"
    if w.endswith("ā"):
        return w + "ya"
    raise F.Miss("instr: " + w)


INSTR = {}
SUBJ = {}
for _k, _v in _CL_NAMES.items():
    if " " not in _k:
        INSTR[instr(_k)] = _v + "ဖြင့်"
    SUBJ[_k] = _v
for _k in ["lobho", "doso", "moho"]:
    SUBJ[_k] = SYN[_k]
    INSTR[instr(_k)] = SYN[_k] + "ဖြင့်"
INSTR["sīlabbataparāmāsena kāyaganthena"] = _CL_NAMES["sīlabbataparāmāso kāyagantho"] + "ဖြင့်"
INSTR["idaṃsaccābhinivesena kāyaganthena"] = _CL_NAMES["idaṃsaccābhiniveso kāyagantho"] + "ဖြင့်"
INSTR["abhijjhākāyaganthena"] = _CL_NAMES["abhijjhā kāyagantho"] + "ဖြင့်"
ph({"Cattāro āsavā": num(N_["āsava"], "catu"), "Dasa saṃyojanāni": num(N_["saṃyojana"], "dasa"),
    "Cattāro ganthā": num(N_["gantha"], "catu")})
# idaṃsaccābhinivesa views and the diṭṭhāsava views
_VIEWS = {
    "Sassato loko": "လောကသည် ထာဝရ တည်မြဲသည်", "asassato loko": "လောကသည် ထာဝရ မတည်မြဲ",
    "antavā loko": "လောကသည် အဆုံး ရှိသည်", "anantavā loko": "လောကသည် အဆုံး မရှိ",
    "taṃ jīvaṃ taṃ sarīraṃ": "အသက်သည် ကိုယ်ခန္ဓာပင် ဖြစ်သည်",
    "aññaṃ jīvaṃ aññaṃ sarīraṃ": "အသက်နှင့် ကိုယ်ခန္ဓာသည် တခြားစီ ဖြစ်သည်",
    "hoti tathāgato paraṃ maraṇā": "မြတ်စွာဘုရားသည် သေပြီးနောက် ရှိသည်",
    "na hoti tathāgato paraṃ maraṇā": "မြတ်စွာဘုရားသည် သေပြီးနောက် မရှိ",
    "hoti ca na ca hoti tathāgato paraṃ maraṇā": "မြတ်စွာဘုရားသည် သေပြီးနောက် ရှိသည်လည်း ဖြစ် မရှိသည်လည်း ဖြစ်သည်",
    "neva hoti na na hoti tathāgato paraṃ maraṇā":
        "မြတ်စွာဘုရားသည် သေပြီးနောက် ရှိသည်လည်း မဟုတ် မရှိသည်လည်း မဟုတ်",
}
_VA = "ဟူ၍ဖြစ်စေ"
for _k, _v in _VIEWS.items():
    _kk = _k[0].lower() + _k[1:]
    _ti = {"loko": "lokoti", "sarīraṃ": "sarīranti", "maraṇā": "maraṇāti"}[_kk.split()[-1]]
    ph({" ".join(_kk.split()[:-1] + [_ti]) + " vā": _v + _VA})
    ph({_kk: _v})
ph({"idameva saccaṃ moghamaññanti vā": f"ဤအရာသာ အမှန် ဖြစ်၍ အခြားအရာသည် အချည်းနှီး ဖြစ်သည်{_VA}"})
# māna
ph({"Seyyohamasmīti māno": "ငါသည် သာလွန်သူ ဖြစ်သည်ဟူသော မာန",
    "sadisohamasmīti māno": "ငါသည် တူညီသူ ဖြစ်သည်ဟူသော မာန",
    "hīnohamasmīti māno": f"ငါသည် {T['hīnā'][:-3]}သူ ဖြစ်သည်ဟူသော မာန"})
syn({"māno": "မာန", "maññanā": "ထင်မှတ်ခြင်း", "maññitattaṃ": "ထင်မှတ်ထားသော အဖြစ်", "unnati": "စိတ် မြင့်တက်ခြင်း",
     "unnamo": "ခေါင်းမော့ခြင်း", "dhajo": "အလံ", "sampaggāho": "အလွန် မြှင့်တင်ခြင်း",
     "ketukamyatā cittassa": f"{F.MIND}၏ အလံ ထူလိုခြင်း"}, True)
# issā, macchariya
add(F.GEN, "paralābhasakkāragarukāramānanavandanapūjanāsu",
    "သူတစ်ပါး၏ လာဘ်၊ အရိုအသေ ပြုခံရမှု၊ လေးစားခံရမှု၊ ချီးမြှောက်ခံရမှု၊ ရှိခိုးခံရမှု၊ ပူဇော်ခံရမှုတို့၌ ဖြစ်သော")
syn({"issā": "ငြူစူမှု", "issāyanā": "ငြူစူခြင်း", "issāyitattaṃ": "ငြူစူထားသော အဖြစ်", "usūyā": "သဝန်တိုမှု",
     "usūyanā": "သဝန်တိုခြင်း", "usūyitattaṃ": "သဝန်တိုထားသော အဖြစ်",
     "maccheraṃ": "ဝန်တိုခြင်း", "maccharāyanā": "ဝန်တိုနေခြင်း", "maccharāyitattaṃ": "ဝန်တိုထားသော အဖြစ်",
     "kadariyaṃ": "ကပ်စေးနည်းခြင်း", "kaṭukañcukatā": "တွန့်တိုခြင်း",
     "aggahitattaṃ cittassa": f"{F.MIND}၏ တင်းတင်း ဆုပ်ကိုင်ထားသော အဖြစ်"})
ph({"Pañca macchariyāni": num("ဝန်တိုမှု", "pañca"), "āvāsamacchariyaṃ": "နေရာထိုင်ခင်းကို ဝန်တိုမှု",
    "kulamacchariyaṃ": "ကိုးကွယ်သော အိမ်ကို ဝန်တိုမှု", "lābhamacchariyaṃ": "လာဘ်ကို ဝန်တိုမှု",
    "vaṇṇamacchariyaṃ": "ဂုဏ်သတင်းကို ဝန်တိုမှု", "dhammamacchariyaṃ": "တရားကို ဝန်တိုမှု"})

# ---------------------------------------------------------------------------------------- 4-02: hindrances, clinging, defilements
THINA, MIDDHA = "ထိုင်းမှိုင်းမှု", "ငိုက်မျဉ်းမှု"           # thina (sloth) / middha (torpor)
UDDH, KUKK = "ယောက်ယက်ခတ်မှု", "နောင်တ ပူပန်မှု"          # uddhacca (restlessness) / kukkucca (worry)
ATTAVADA = f"{ATTA}ဟူသော ဝါဒ"
_CL2 = {
    "kāmacchandanīvaraṇaṃ": f"{SYN['kāmacchando']} {N_['nīvaraṇa']}",
    "byāpādanīvaraṇaṃ": f"ဖျက်ဆီးလိုစိတ် {N_['nīvaraṇa']}",
    "thinamiddhanīvaraṇaṃ": f"{THINA}နှင့် {MIDDHA} {N_['nīvaraṇa']}",
    "uddhaccakukkuccanīvaraṇaṃ": f"{UDDH}နှင့် {KUKK} {N_['nīvaraṇa']}",
    "uddhaccanīvaraṇaṃ": f"{UDDH} {N_['nīvaraṇa']}", "kukkuccanīvaraṇaṃ": f"{KUKK} {N_['nīvaraṇa']}",
    "vicikicchānīvaraṇaṃ": f"{VICI} {N_['nīvaraṇa']}", "avijjānīvaraṇaṃ": f"{F.SUT['avijjā']} {N_['nīvaraṇa']}",
    "diṭṭhiparāmāso": f"{DITTHI}ဆိုင်ရာ {N_['parāmāsa']}",
    "kāmupādānaṃ": f"{KAMA} {N_['upādāna']}", "diṭṭhupādānaṃ": f"{DITTHI} {N_['upādāna']}",
    "sīlabbatupādānaṃ": f"{_SILA} {_VATA} {N_['upādāna']}", "attavādupādānaṃ": f"{ATTAVADA} {N_['upādāna']}",
    "thinaṃ": THINA, "middhaṃ": MIDDHA, "uddhaccaṃ": UDDH, "kukkuccaṃ": KUKK, "māno": "မာန", "diṭṭhi": DITTHI,
    "vicikicchā": VICI, "ahirikaṃ": F.SUT["ahirika"], "anottappaṃ": F.SUT["anottappa"],
}
for _k, _v in _CL2.items():
    if _k not in SYN:
        add(SYN, _k, _v)
        LISTABLE.add(_k)
    SUBJ[_k] = _v
    INSTR[instr(_k)] = _v + "ဖြင့်"
add(PH, "ahirīkaṃ", F.SUT["ahirika"])
add(F.GEN, "cittassa", f"{F.MIND}၏")
add(F.GEN, "kāyassa", f"{F.KAYA}၏")
ph({"Cattāro oghā": num(N_["ogha"], "catu"), "Cattāro yogā": num(N_["yoga"], "catu"),
    "Cha nīvaraṇā": num(N_["nīvaraṇa"], "cha"), "Cattāri upādānāni": num(N_["upādāna"], "catu"),
    "Dasa kilesavatthūni": num(f"{F.KIL} ဖြစ်ရာ အခြေခံ", "dasa"),
    "Atthi thinaṃ": f"{THINA} ရှိသည်", "atthi middhaṃ": f"{MIDDHA} ရှိသည်",
    "Atthi uddhaccaṃ": f"{UDDH} ရှိသည်", "atthi kukkuccaṃ": f"{KUKK} ရှိသည်",
    "Iti idañca thinaṃ": f"ဤသို့ ဤ{THINA}လည်း", "idañca middhaṃ": f"ဤ{MIDDHA}လည်း",
    "Iti idañca uddhaccaṃ": f"ဤသို့ ဤ{UDDH}လည်း", "idañca kukkuccaṃ": f"ဤ{KUKK}လည်း",
    "Akappiye kappiyasaññitā": "မအပ်စပ်သည်၌ အပ်စပ်သည်ဟု မှတ်ထင်ခြင်း",
    "kappiye akappiyasaññitā": "အပ်စပ်သည်၌ မအပ်စပ်သည်ဟု မှတ်ထင်ခြင်း",
    "avajje vajjasaññitā": "အပြစ်မရှိသည်၌ အပြစ်ရှိသည်ဟု မှတ်ထင်ခြင်း",
    "vajje avajjasaññitā": "အပြစ်ရှိသည်၌ အပြစ်မရှိသည်ဟု မှတ်ထင်ခြင်း"})
syn({"akallatā": "မကျန်းမာခြင်း", "akammaññatā": "အသုံးပြုရန် မသင့်တော်ခြင်း", "olīyanā": "တွန့်ဆုတ်ခြင်း",
     "sallīyanā": "လုံးဝ တွန့်ဆုတ်ခြင်း", "līnaṃ": "အားပျော့ခြင်း", "līyanā": "အားပျော့နေခြင်း",
     "līyitattaṃ": "အားပျော့ထားသော အဖြစ်", "thiyanā": "ထိုင်းမှိုင်းခြင်း",
     "thiyitattaṃ cittassa": f"{F.MIND}၏ ထိုင်းမှိုင်းထားသော အဖြစ်",
     "onāho": "ပိတ်ဖုံးခံရခြင်း", "pariyonāho": "အပြည့် ပိတ်ဖုံးခံရခြင်း", "antosamorodho": "အတွင်း၌ ပိတ်ဆို့ခံရခြင်း",
     "soppaṃ": "အိပ်ငိုက်ခြင်း", "pacalāyikā": "ငိုက်ဆင်းခြင်း", "supanā": "အိပ်ပျော်ခြင်း",
     "supitattaṃ": "အိပ်ပျော်ထားသော အဖြစ်",
     "avūpasamo": "မငြိမ်ဝပ်ခြင်း", "cetaso vikkhepo": f"{F.MIND}၏ ပျံ့လွင့်ခြင်း",
     "bhantattaṃ cittassa": f"{F.MIND}၏ ယိမ်းထိုးနေသော အဖြစ်",
     "kukkuccāyanā": "နောင်တ ပူပန်ခြင်း", "kukkuccāyitattaṃ": "နောင်တ ပူပန်ထားသော အဖြစ်",
     "cetaso vippaṭisāro": f"{F.MIND}၏ နောင်တ ရခြင်း"})
LISTABLE.update(["thambhitattaṃ cittassa", "manovilekho"])
ph({"Cittañca": f"{F.MIND}လည်း", "avasesañca rūpaṃ": f"{AVASESA} ရုပ်လည်း",
    # «Cittaṃ na vattabbaṃ – A-ntipi, B-ntipi» = the Aṭṭhakathākaṇḍa frame (verb «ခေါ်ဆို၍ မရ» at the end; consistency pass)
    "Cittaṃ na vattabbaṃ – cittena sampayuttantipi, cittena vippayuttantipi":
        f"{F.MIND}သည် – {T['cittasampayuttā']} {DH}ဟုလည်းကောင်း၊ {T['cittavippayuttā']} {DH}ဟုလည်းကောင်း ခေါ်ဆို၍ မရ",
    "Cittaṃ na vattabbaṃ – cittena saṃsaṭṭhantipi, cittena visaṃsaṭṭhantipi":
        f"{F.MIND}သည် – {T['cittasaṃsaṭṭhā']} {DH}ဟုလည်းကောင်း၊ {T['cittavisaṃsaṭṭhā']} {DH}ဟုလည်းကောင်း ခေါ်ဆို၍ မရ",
    "yaṃ vā panaññampi atthi rūpaṃ cittajaṃ cittahetukaṃ cittasamuṭṭhānaṃ":
        f"{F.CITTAJA}၊ {F.CITTAHETUKA}၊ {T['cittasamuṭṭhānā']} အခြား ရုပ် ရှိသမျှလည်း"})
ph({"kāyaviññatti": F.KAYAVINNATTI, "vacīviññatti": F.VACIVINNATTI,      # the Rūpakaṇḍa forms (consistency pass)
    "ākāsadhātu": F.AKASADHATU, "āpodhātu": F.APODHATU, "rūpassa lahutā": f"ရုပ်၏ {F.SYN['lahutā']}",
    "rūpassa mudutā": f"ရုပ်၏ {F.SYN['mudutā']}", "rūpassa kammaññatā": f"ရုပ်၏ {F.SYN['kammaññatā']}",
    "rūpassa upacayo": "ရုပ်၏ တိုးပွားခြင်း", "rūpassa santati": F.RUPA_SANTATI,
    "kabaḷīkāro āhāro": F.KABALIKARA, "dhammāyatanaṃ": F.NAMES["dhammāyatanaṃ"]}, True)
# wrong views of diṭṭhupādāna / diṭṭhivipatti (natthi …) and diṭṭhisampadā (atthi …)
_NATTHI = {"dinnaṃ": "ပေးလှူခြင်း", "yiṭṭhaṃ": "ယဇ်ပူဇော်ခြင်း", "hutaṃ": "ပူဇော်သကာ ဆက်ကပ်ခြင်း",
           "sukatadukkaṭānaṃ kammānaṃ phalaṃ vipāko": "ကောင်းစွာ ပြုသော ကံ၊ ဆိုးစွာ ပြုသော ကံတို့၏ အသီးအပွင့် အကျိုးဆက်",
           "ayaṃ loko": "ဤလောက", "paro loko": "တမလွန် လောက", "mātā": "အမိ", "pitā": "အဖ",
           "sattā opapātikā": "အလိုအလျောက် ပေါ်လာသော သတ္တဝါ"}
for _k, _v in _NATTHI.items():
    ph({f"natthi {_k}": f"{_v} မရှိ", f"atthi {_k}": f"{_v} ရှိသည်"})
SAMANA_RE = (r"(?P<n>natthi|atthi) loke samaṇabrāhmaṇā sammaggatā(?: (?P<v>\[[^\]]+\]))? sammāpaṭipannā(?P<c>,)?"
             r" ye imañca lokaṃ parañca lokaṃ sayaṃ abhiññā sacchikatvā pavedentīti")


def r_samana(m):
    """«natthi / atthi loke samaṇabrāhmaṇā … pavedentīti»: the verb of «natthi / atthi» closes the Burmese clause."""
    v = " " + F.var_my(m["v"]) if m["v"] else ""
    c = COMMA if m["c"] else ""
    verb = "မရှိ" if m["n"] == "natthi" else "ရှိသည်"
    return (f"လောက၌ မှန်ကန်စွာ ရောက်ရှိသော{v} မှန်ကန်စွာ ကျင့်ကြံသော{c} ဤလောကကိုလည်း တမလွန် လောကကိုလည်း "
            f"ကိုယ်တိုင် {F.ABHINNA.removesuffix('ခြင်း')}၍ မျက်မှောက်ပြုပြီး ဟောကြားသော ရဟန်းပုဏ္ဏားတို့ {verb}ဟူ၍")
ph({"Vitakko ca": f"{F.VIT}လည်း", "vicāro ca": f"{F.VIC}လည်း", "pīti ca": "ပီတိလည်း",
    "sukhañca": f"{F.SUKHA}မှုလည်း", "upekkhā ca": "ဥပေက္ခာလည်း"})
# the planes (kāmāvacara … arūpāvacara)
_ANTARE = "ဤအကြား၌ ကျင်လည်သော၊ ဤအကြား၌ အကျုံးဝင်သော"
ph({"Heṭṭhato avicinirayaṃ pariyantaṃ karitvā": "အောက်၌ အဝီစိ ငရဲကို အဆုံးအစွန် ပြု၍",
    "uparito paranimmitavasavattī deve": "အထက်၌ ပရနိမ္မိတဝသဝတ္တီ နတ်တို့ကို",
    "anto karitvā": "အတွင်း ထည့်သွင်း၍",
    "yaṃ etasmiṃ antare etthāvacarā ettha pariyāpannā khandhadhātu āyatanā":
        f"{_ANTARE} {KHANDHA}၊ ဓာတ်၊ {AYAT}တို့",
    "Heṭṭhato brahmalokaṃ pariyantaṃ karitvā": "အောက်၌ ဗြဟ္မာ့ပြည်ကို အဆုံးအစွန် ပြု၍",
    "uparito akaniṭṭhe deve": "အထက်၌ အကနိဋ္ဌ နတ်တို့ကို",
    "yaṃ etasmiṃ antare etthāvacarā ettha pariyāpannā": _ANTARE,
    "samāpannassa vā": "ဈာန် ဝင်စားသူ၏ဖြစ်စေ", "upapannassa vā": "ထိုဘုံ၌ ဖြစ်ပေါ်သူ၏ဖြစ်စေ",
    "diṭṭhadhammasukhavihārissa": "မျက်မှောက်ဘဝ၌ပင် သာယာစွာ နေထိုင်သူ၏",          # as 2-05 (sukha = သာယာ)
    "diṭṭhadhammasukhavihārissa vā": "မျက်မှောက်ဘဝ၌ပင် သာယာစွာ နေထိုင်သူ၏ဖြစ်စေ",
    "cittacetasikā dhammā": CCD,
    "vā cittacetasikā dhammā": f"ဖြစ်စေ {CCD}",
    "Heṭṭhato ākāsānañcāyatanupage deve pariyantaṃ karitvā":
        f"အောက်၌ {F.JH_ARUPA_BASE['ākāsānañcāyatana']} ဘုံသို့ ရောက်သော နတ်တို့ကို အဆုံးအစွန် ပြု၍",   # shared names
    "uparito nevasaññānāsaññāyatanupage deve":
        f"အထက်၌ {F.JH_ARUPA_BASE['nevasaññānāsaññāyatana']} ဘုံသို့ ရောက်သော နတ်တို့ကို"})
# hiri / ottappa and their absence (sentence definitions, as BODY of 2-01 without «ထိုအချိန်၌»)
_PAPA = F._PAPA
ph({"Yaṃ na hirīyati hiriyitabbena": "ရှက်ထိုက်သည့်အရာကို မရှက်ခြင်း",
    "na hirīyati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā": f"{_PAPA} မရှက်ခြင်း",
    "Yaṃ na ottappati ottappitabbena": "ကြောက်ရွံ့ထိုက်သည့်အရာကို မကြောက်ရွံ့ခြင်း",
    "na ottappati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā": f"{_PAPA} မကြောက်ရွံ့ခြင်း",
    "Yaṃ hirīyati hiriyitabbena": "ရှက်ထိုက်သည့်အရာကို ရှက်ခြင်း",
    "hirīyati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā": f"{_PAPA} ရှက်ခြင်း",
    "Yaṃ ottappati ottappitabbena": "ကြောက်ရွံ့ထိုက်သည့်အရာကို ကြောက်ရွံ့ခြင်း",
    "ottappati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā": f"{_PAPA} ကြောက်ရွံ့ခြင်း"})
assert F.BODY["Yaṃ tasmiṃ samaye hirīyati hiriyitabbena hirīyati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā"] \
    == f"{F.TASMIM} {PH['Yaṃ hirīyati hiriyitabbena']}၊ {PH['hirīyati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā']}"

# ---------------------------------------------------------------------------------------- 4-03: suttantika dyads
S = F.SUT
DUCC, SUCC = "ဒုစရိုက်", "သုစရိုက်"
ph({"Vijjāya sampayuttakā dhammā": f"{S['vijjā']}{F.SAMP} {DHP}",
    "Avijjāya sampayuttakā dhammā": f"{S['avijjā']}{F.SAMP} {DHP}",
    "Heṭṭhimesu tīsu ariyamaggesu paññā": f"အောက်ပိုင်း {num(ARIYA + ' ' + MAGGA, 'ti')}တို့၌ ရှိသော ပညာ",
    "Upariṭṭhime arahattamagge paññā": f"အမြင့်ဆုံး ရဟန္တာ {MAGGA}၌ ရှိသော ပညာ",
    "Ahirīkañca anottappañca": f"{S['ahirika']}လည်း {S['anottappa']}လည်း",
    "Hirī ca ottappañca": f"{S['hirī']}လည်း {S['ottappa']}လည်း",
    "Kāyaduccaritaṃ": f"ကိုယ်ဖြင့် ပြုသော {DUCC}", "vacīduccaritaṃ": f"နှုတ်ဖြင့် ပြုသော {DUCC}",
    "manoduccaritaṃ": f"{F.MANO}ဖြင့် ပြုသော {DUCC}",
    "Kāyasucaritaṃ": f"ကိုယ်ဖြင့် ပြုသော {SUCC}", "vacīsucaritaṃ": f"နှုတ်ဖြင့် ပြုသော {SUCC}",
    "manosucaritaṃ": f"{F.MANO}ဖြင့် ပြုသော {SUCC}"})
add(F.GEN, "tesaṃ tesaṃ dhammānaṃ", f"ထိုထို {DH}တို့၏")
syn({"saṅkhā": "ရေတွက် ခေါ်ဝေါ်ခြင်း", "samaññā": "အများ သမုတ်ခြင်း", "paññatti": T["paññatti"][:-7].rstrip(),
     "vohāro": "ပြောဆို သုံးနှုန်းခြင်း", "nāmaṃ": "အမည်", "nāmakammaṃ": "အမည်ပေးခြင်း", "nāmadheyyaṃ": "အမည်နာမ",
     "nirutti": T["nirutti"][:-7].rstrip(), "byañjanaṃ": "ဖော်ပြသော စကားလုံး", "abhilāpo": "ခေါ်ဆိုခြင်း"})
assert SYN["paññatti"] == "သတ်မှတ်ချက်" and SYN["nirutti"] == "စကားဖြင့် ဖော်ပြမှု"
_AL = f"{ATTA}နှင့် လောကသည်"
ph({"Bhavissati attā ca loko cāti": f"{_AL} ဆက်လက် တည်ရှိလိမ့်မည်ဟူ၍",
    "Na bhavissati attā ca loko cāti": f"{_AL} ဆက်လက် တည်ရှိလိမ့်မည် မဟုတ်ဟူ၍",
    "Sassato attā ca loko cāti": f"{_AL} ထာဝရ တည်မြဲသည်ဟူ၍",
    "Ucchijjissati attā ca loko cāti": f"{_AL} ပြတ်စဲသွားလိမ့်မည်ဟူ၍",
    "Antavā attā ca loko cāti": f"{_AL} အဆုံး ရှိသည်ဟူ၍",
    "Anantavā attā ca loko cāti": f"{_AL} အဆုံး မရှိဟူ၍",
    "Pubbantaṃ ārabbha": "အတိတ်ကာလကို အာရုံပြု၍", "Aparantaṃ ārabbha": "အနာဂတ်ကာလကို အာရုံပြု၍"})
add(F.GEN, "uppajjati", "ဖြစ်ပေါ်သော")
ph({"Sahadhammike vuccamāne": "တရားနှင့် လျော်စွာ သွန်သင် ပြောဆိုသောအခါ"})
syn({"dovacassāyaṃ": "စကား နားမထောင်ခြင်း", "dovacassiyaṃ": "စကား နားမထောင်သော အဖြစ်",
     "dovacassatā": S["dovacassatā"], "vippaṭikūlaggāhitā": "ဆန့်ကျင်ဘက် ယူခြင်း",
     "vipaccanīkasātatā": "ဆန့်ကျင်ခြင်း၌ နှစ်သက်ခြင်း", "anādariyaṃ": "မလေးစားခြင်း",
     "anādaratā": "မလေးစားသော အဖြစ်", "agāravatā": "ရိုသေမှု မရှိခြင်း", "appaṭissavatā": "နာခံမှု မရှိခြင်း",
     "sovacassāyaṃ": "စကား နားထောင်ခြင်း", "sovacassiyaṃ": "စကား နားထောင်သော အဖြစ်",
     "sovacassatā": S["sovacassatā"], "appaṭikūlaggāhitā": "ဆန့်ကျင်ဘက် မယူခြင်း",
     "avipaccanīkasātatā": "ဆန့်ကျင်ခြင်း၌ မနှစ်သက်ခြင်း", "sagāravatā": "ရိုသေမှု ရှိခြင်း",
     "sādariyaṃ": "လေးစားခြင်း", "sādaratā": "လေးစားသော အဖြစ်", "sappaṭissavatā": "နာခံမှု ရှိခြင်း"}, True)
_PUGG = "ပုဂ္ဂိုလ်တို့ ရှိကြ၏"
ph({"Ye te puggalā assaddhā dussīlā appassutā maccharino duppaññā":
        f"ယုံကြည်မှု မရှိသော၊ သီလ ပျက်သော၊ အကြားအမြင် နည်းသော၊ ဝန်တိုသော၊ ပညာ နည်းသော {_PUGG}",
    "Ye te puggalā saddhā sīlavanto bahussutā cāgavanto paññavanto":
        f"ယုံကြည်မှု ရှိသော၊ သီလ ရှိသော၊ အကြားအမြင် များသော၊ စွန့်ကြဲမှု ရှိသော၊ ပညာ ရှိသော {_PUGG}"})
add(F.GEN, "tesaṃ", "ထိုသူတို့ကို")
syn({"sevanā": "ပေါင်းသင်းခြင်း", "nisevanā": "နီးကပ်စွာ ပေါင်းသင်းခြင်း", "saṃsevanā": "ကောင်းစွာ ပေါင်းသင်းခြင်း",
     "bhajanā": "ဆည်းကပ်ခြင်း", "sambhajanā": "ကောင်းစွာ ဆည်းကပ်ခြင်း", "bhatti": "ကိုးကွယ်ခြင်း",
     "sambhatti": "ကောင်းစွာ ကိုးကွယ်ခြင်း", "taṃsampavaṅkatā": "ထိုသူတို့ဘက်သို့ ညွတ်ကိုင်းခြင်း"})
_APATTI, _SAMAP = "အပြစ်", "ဈာန် ဝင်စားမှု"
ph({"Pañcapi āpattikkhandhā āpattiyo": f"{num(_APATTI + ' အစု', 'pañca')}လုံးသည် {_APATTI}တို့ ဖြစ်သည်",
    "sattapi āpattikkhandhā āpattiyo": f"{num(_APATTI + ' အစု', 'satta')}လုံးသည် {_APATTI}တို့ ဖြစ်သည်",
    "Atthi savitakkasavicārā samāpatti": f"{T['savitakkasavicārā']} {_SAMAP} ရှိသည်",
    "atthi avitakkavicāramattā samāpatti": f"{T['avitakkavicāramattā']} {_SAMAP} ရှိသည်",
    "atthi avitakkaavicārā samāpatti": f"{T['avitakkaavicārā']} {_SAMAP} ရှိသည်",
    "Aṭṭhārasa dhātuyo": "ဓာတ် ဆယ့်ရှစ်ပါး", "Dvādasāyatanāni": f"{AYAT} ဆယ့်နှစ်ပါး"})
for _k, _v in {"tāsaṃ āpattīnaṃ": f"ထို{_APATTI}တို့၌", "tāhi āpattīhi": f"ထို{_APATTI}တို့မှ",
               "tāsaṃ samāpattīnaṃ": f"ထို{_SAMAP}တို့၌", "tāhi samāpattīhi": f"ထို{_SAMAP}တို့မှ",
               "tāsaṃ dhātūnaṃ": "ထိုဓာတ်တို့၌", "tesaṃ āyatanānaṃ": f"ထို{AYAT}တို့၌", "tattha": "ထို၌ ရှိသော",
               "kusalānaṃ dhammānaṃ": f"{KUS} {DH}တို့ကို",
               "kusalānaṃ dhammānaṃ bhāvanāya": f"{KUS} {DH}တို့ကို ပွားများရာ၌",
               "kusalānaṃ dhammānaṃ bhāvanāya asantuṭṭhassa": f"{KUS} {DH}တို့ကို ပွားများရာ၌ မရောင့်ရဲသူ၏",
               "imesaṃ channaṃ indriyānaṃ": f"ဤ {num('အာရုံခံ အင်္ဂါ', 'cha')}တို့၏"}.items():
    add(F.GEN, _k, _v)
for _k in ["āpattikusalatā", "samāpattikusalatā", "dhātukusalatā", "manasikārakusalatā", "āyatanakusalatā"]:
    syn({_k: S[_k]})
syn({"vuṭṭhānakusalatā": "ထမြောက်ရာ၌ ကျွမ်းကျင်ခြင်း"})
for _o, _om in OBJ.items():
    if _o != "dhamma":
        ph({_o + "dhātu": f"{_om} ဓာတ်"}, True)
for _o, _om in ORGAN.items():
    ph({_o + "dhātu": f"{_om} ဓာတ်", _o + "viññāṇadhātu": f"{_om} {VIN} ဓာတ်"}, True)
LISTABLE.add("dhammadhātu")
# paṭiccasamuppāda
_PS = [("Avijjā", S["avijjā"], "saṅkhārā", f"{F.SANKHARA}များ"), ("saṅkhāra", f"{F.SANKHARA}များ", "viññāṇaṃ", VIN),
       ("viññāṇa", VIN, "nāmarūpaṃ", f"{S['nāma']}နှင့် {S['rūpa']}"),
       ("nāmarūpa", f"{S['nāma']}နှင့် {S['rūpa']}", "saḷāyatanaṃ", num(AYAT, "cha")),
       ("saḷāyatana", num(AYAT, "cha"), "phasso", F.PHASSA), ("phassa", F.PHASSA, "vedanā", F.FEEL),
       ("vedanā", F.FEEL, "taṇhā", "တပ်မက်မှု"), ("taṇhā", "တပ်မက်မှု", "upādānaṃ", N_["upādāna"]),
       ("upādāna", N_["upādāna"], "bhavo", BHAVA), ("bhava", BHAVA, "jāti", "မွေးဖွားခြင်း")]
for _a, _am, _b, _bm in _PS:
    ph({f"{_a}paccayā {_b}": f"{_am}ကြောင့် {_bm} ဖြစ်ပေါ်သည်"})
ph({"jātipaccayā jarāmaraṇaṃ sokaparidevadukkhadomanassupāyāsā sambhavanti":
        "မွေးဖွားခြင်းကြောင့် အိုခြင်း၊ သေခြင်း၊ စိုးရိမ်ခြင်း၊ ငိုကြွေးခြင်း၊ ကိုယ်ဆင်းရဲခြင်း၊ စိတ်ဆင်းရဲခြင်း၊ "
        "ပြင်းစွာ ပူပန်ခြင်းတို့ ဖြစ်ပေါ်ကြသည်",
    "evametassa kevalassa dukkhakkhandhassa samudayo hotīti":
        f"ဤသို့ ဤ{DUKKHA_T} {KHANDHA} အားလုံး၏ ဖြစ်ပေါ်ခြင်း ရှိသည်ဟူ၍",
    "Ye ye dhammā yesaṃ yesaṃ dhammānaṃ hetū paccayā uppādāya":
        f"အကြင် အကြင် {DH}တို့သည် အကြင် အကြင် {DH}တို့ ဖြစ်ပေါ်ရန် အကြောင်း၊ အထောက်အပံ့ ဖြစ်ကြ၏",
    "taṃ taṃ ṭhānanti": "ထိုထိုသည် ဖြစ်နိုင်သည့်အရာ ဖြစ်သည်ဟူ၍",
    "Ye ye dhammā yesaṃ yesaṃ dhammānaṃ na hetū na paccayā uppādāya taṃ taṃ aṭṭhānanti":
        f"အကြင် အကြင် {DH}တို့သည် အကြင် အကြင် {DH}တို့ ဖြစ်ပေါ်ရန် အကြောင်း မဟုတ်၊ အထောက်အပံ့ မဟုတ်ကြ၊ "
        "ထိုထိုသည် မဖြစ်နိုင်သည့်အရာ ဖြစ်သည်ဟူ၍"})
syn({"ajjavatā": "ဖြောင့်မတ်သော အဖြစ်", "nīcacittatā": "စိတ် နှိမ့်ချခြင်း", "khanti": S["khanti"],
     "khamanatā": "ခွင့်လွှတ်ခြင်း", "adhivāsanatā": "လက်ခံ သည်းညည်းခံခြင်း", "acaṇḍikkaṃ": "မကြမ်းကြုတ်ခြင်း",
     "anasuropo": "စကား မကြမ်းခြင်း"})
_VIT = {"kāyiko": "ကိုယ်ဖြင့်", "vācasiko": "နှုတ်ဖြင့်", "kāyikavācasiko": "ကိုယ်နှင့် နှုတ်ဖြင့်"}
for _k, _v in _VIT.items():
    _y = "Yo " if _k == "kāyiko" else ""
    ph({f"{_y}{_k} avītikkamo": f"{_v} မကျူးလွန်ခြင်း", f"{_y}{_k} vītikkamo": f"{_v} ကျူးလွန်ခြင်း"})
ALL_SUBJ = {"Sabbopi sīlasaṃvaro": "သီလဖြင့် စောင့်စည်းမှု အားလုံးသည်", "Sabbampi dussilyaṃ": "သီလ ဖောက်ဖျက်မှု အားလုံးသည်",
            "Sabbāpi sammādiṭṭhi": f"{SAMMADITTHI} အားလုံးသည်",
            "Sattapi bojjhaṅgā": f"{num('သိမြင်ခြင်း၏ အင်္ဂါ', 'satta')}လုံးသည်"}
# sākhalya
ph({"Yā sā vācā aṇḍakā kakkasā parakaṭukā parābhisajjanī kodhasāmantā asamādhisaṃvattanikā":
        "ခက်ထန်သော၊ ကြမ်းတမ်းသော၊ သူတစ်ပါးကို နာကျင်စေသော၊ သူတစ်ပါးကို ထိခိုက်စေသော၊ ဒေါသနှင့် နီးစပ်သော၊ "
        "သမာဓိ မဖြစ်စေသော စကား ရှိ၏",
    "tathārūpiṃ vācaṃ pahāya": "ထိုသို့သော စကားကို ပယ်၍",
    "yā sā vācā neḷā kaṇṇasukhā pemanīyā hadayaṅgamā porī bahujanakantā bahujanamanāpā":
        "အပြစ်ကင်းသော၊ နားဝင်ချိုသော၊ ချစ်ခင်ဖွယ်ကောင်းသော၊ နှလုံးသို့ ရောက်သော၊ ယဉ်ယဉ်ကျေးကျေး ရှိသော၊ "
        "လူအများ နှစ်သက်သော၊ လူအများ စိတ်တွေ့သော စကား ရှိ၏",
    "tathārūpiṃ vācaṃ bhāsitā hoti": "ထိုသို့သော စကားကို ပြောဆိုသူ ဖြစ်၏"})
syn({"saṇhavācatā": "ချောမွေ့သော စကားကို ဆိုခြင်း", "sakhilavācatā": "ချိုသာသော စကားကို ဆိုခြင်း",
     "apharusavācatā": "မကြမ်းတမ်းသော စကားကို ဆိုခြင်း"})
# paṭisanthāra
ph({"Dve paṭisanthārā": num(S["paṭisanthāro"], "dvi"),
    "āmisapaṭisanthāro ca": f"ပစ္စည်းဖြင့် {S['paṭisanthāro']}လည်း",
    "dhammapaṭisanthāro ca": f"တရားဖြင့် {S['paṭisanthāro']}လည်း",
    "Idhekacco paṭisanthārako hoti āmisapaṭisanthārena vā dhammapaṭisanthārena vā":
        f"ဤလောက၌ အချို့သော သူသည် ပစ္စည်းဖြင့်ဖြစ်စေ တရားဖြင့်ဖြစ်စေ {S['paṭisanthāro'].removesuffix('ခြင်း')}သူ ဖြစ်၏"})
assert S["paṭisanthāro"].endswith("ခြင်း")
# restraint of the faculties
_EKACCO = "ဤလောက၌ အချို့သော သူသည်"
_NIM = "အမှတ်အသားကို စွဲယူသူ"
_ANUB = "အသေးစိတ်ကို စွဲယူသူ"
_IND = {"cakkhu": f"{ORGAN['cakkhu']}၏ {F.INDRIYA}", "man": F.NAMES["manindriyaṃ"]}
ph({"Idhekacco": _EKACCO, "cakkhunā rūpaṃ disvā": f"{ORGAN['cakkhu']}ဖြင့် {OBJ['rūpa']}ကို မြင်၍",
    "nimittaggāhī hoti anubyañjanaggāhī": f"{_NIM} {_ANUB} ဖြစ်၏",
    "na nimittaggāhī hoti na anubyañjanaggāhī": f"{_NIM} မဟုတ်၊ {_ANUB} မဟုတ်",
    "na nimittaggāhī hoti nānubyañjanaggāhī": f"{_NIM} မဟုတ်၊ {_ANUB} မဟုတ်",
    "Sotena saddaṃ sutvā": f"{ORGAN['sota']}ဖြင့် {OBJ['sadda']}ကို ကြား၍",
    "ghānena gandhaṃ ghāyitvā": f"{ORGAN['ghāna']}ဖြင့် {OBJ['gandha']}ကို နမ်း၍",
    "jivhāya rasaṃ sāyitvā": f"{ORGAN['jivhā']}ဖြင့် {OBJ['rasa']}ကို လျက်၍",
    "kāyena phoṭṭhabbaṃ phusitvā": f"{ORGAN['kāya']}ဖြင့် {OBJ['phoṭṭhabba']}ကို ထိ၍",
    "manasā dhammaṃ viññāya": f"{F.MANO}ဖြင့် {DH}ကို သိ၍",
    "tassa saṃvarāya na paṭipajjati": "ထိုစွမ်းရည်ကို စောင့်စည်းရန် မကျင့်ကြံ",
    "tassa saṃvarāya paṭipajjati": "ထိုစွမ်းရည်ကို စောင့်စည်းရန် ကျင့်ကြံ၏"})
for _k, _v in _IND.items():
    _p = "cakkhundriy" if _k == "cakkhu" else "manindriy"
    ph({f"Yatvādhikaraṇamenaṃ {_p}aṃ asaṃvutaṃ viharantaṃ abhijjhādomanassā pāpakā akusalā dhammā anvāssaveyyuṃ":
        f"အကြင် အကြောင်းကြောင့် {_v}ကို မစောင့်စည်းဘဲ နေသော ထိုသူ့ထံသို့ {SYN['abhijjhā']}၊ စိတ်ဆင်းရဲခြင်း ဟူသော "
        f"ယုတ်မာသော {AKUS} {DHP} စီးဝင်လာနိုင်သည်",
        f"na rakkhati {_p}aṃ": f"{_v}ကို မစောင့်ရှောက်", f"rakkhati {_p}aṃ": f"{_v}ကို စောင့်ရှောက်၏",
        f"{_p}e na saṃvaraṃ āpajjati": f"{_v}၌ စောင့်စည်းမှု မပြု",
        f"{_p}e saṃvaraṃ āpajjati": f"{_v}၌ စောင့်စည်းမှု ပြု၏"})
syn({"agutti": "မစောင့်ထိန်းခြင်း", "agopanā": "မကာကွယ်ခြင်း", "anārakkho": "မစောင့်ရှောက်ခြင်း",
     "asaṃvaro": "မစောင့်စည်းခြင်း", "gutti": "စောင့်ထိန်းခြင်း", "gopanā": "ကာကွယ်ခြင်း",
     "ārakkho": "စောင့်ရှောက်ခြင်း", "saṃvaro": "စောင့်စည်းခြင်း"})
# moderation in food
ph({"Idhekacco appaṭisaṅkhā ayoniso āhāraṃ āhāreti davāya madāya maṇḍanāya vibhūsanāya":
        f"{_EKACCO} ပြန်လည် မဆင်ခြင်ဘဲ မသင့်လျော်စွာ ကစားရန် မာန်ယစ်ရန် အလှပြင်ရန် တန်ဆာဆင်ရန် အစာကို စားသုံး၏",
    "Idhekacco paṭisaṅkhā yoniso āhāraṃ āhāreti": f"{_EKACCO} ပြန်လည် ဆင်ခြင်၍ သင့်လျော်စွာ အစာကို စားသုံး၏",
    "neva davāya na madāya na maṇḍanāya na vibhūsanāya yāvadeva imassa kāyassa ṭhitiyā yāpanāya vihiṃsūparatiyā "
    "brahmacariyānuggahāya":
        "ကစားရန် မဟုတ်၊ မာန်ယစ်ရန် မဟုတ်၊ အလှပြင်ရန် မဟုတ်၊ တန်ဆာဆင်ရန် မဟုတ်၊ ဤကိုယ်ခန္ဓာ တည်တံ့ရန်၊ "
        "ဆက်လက် ရှင်သန်ရန်၊ ညှဉ်းပန်းမှု ငြိမ်းရန်၊ မြင့်မြတ်သော အကျင့်ကို ထောက်ပံ့ရန်သာ ဖြစ်၏",
    "iti purāṇañca vedanaṃ paṭihaṅkhāmi": f"ဤသို့ ဟောင်းသော {F.FEEL}ကိုလည်း ပယ်ဖျောက်မည်",
    "navañca vedanaṃ na uppādessāmi": f"သစ်သော {F.FEEL}ကိုလည်း မဖြစ်ပေါ်စေမည်",
    "yātrā ca me bhavissati anavajjatā ca phāsuvihāro cāti":
        "ငါ၏ အသက်မွေးမှုလည်း ဖြစ်လိမ့်မည်၊ အပြစ် မရှိမှုလည်း၊ ချမ်းသာစွာ နေထိုင်မှုလည်း ဖြစ်လိမ့်မည်ဟူ၍"})
syn({"asantuṭṭhitā": "ရောင့်ရဲမှု မရှိခြင်း", "amattaññutā": "အတိုင်းအရှည်ကို မသိခြင်း",
     "appaṭisaṅkhā bhojane": "အစားအစာ၌ ပြန်လည် မဆင်ခြင်ခြင်း", "santuṭṭhitā": "ရောင့်ရဲခြင်း",
     "mattaññutā": "အတိုင်းအရှည်ကို သိခြင်း", "paṭisaṅkhā bhojane": "အစားအစာ၌ ပြန်လည် ဆင်ခြင်ခြင်း"})
assert F.MFIXED["asantuṭṭhitā ca kusalesu dhammesu."].count(SYN["asantuṭṭhitā"]) == 1
# mindfulness, development
syn({"asati": "သတိ မရှိခြင်း", "ananussati": "အဖန်ဖန် မအောက်မေ့ခြင်း", "appaṭissati": "ပြန်လည် မအောက်မေ့ခြင်း",
     "asaraṇatā": "မမှတ်မိခြင်း", "adhāraṇatā": "စွဲမှတ် မထားခြင်း", "pilāpanatā": "အပေါ်ယံ ပေါ်လောခြင်း",
     "sammusanatā": "မေ့လျော့ခြင်း", "āsevanā": "အလေ့အကျင့် ပြုခြင်း", "bhāvanā": "ပွားများခြင်း",
     "bahulīkammaṃ": "အကြိမ်ကြိမ် ပြုခြင်း", "bhiyyokamyatā": "ပိုမို လိုလားခြင်း",
     "sakkaccakiriyatā": "ရိုသေစွာ ပြုခြင်း", "sātaccakiriyatā": "အစဉ်တစိုက် ပြုခြင်း",
     "aṭṭhitakiriyatā": "ရပ်တန့်ခြင်း မရှိဘဲ ပြုခြင်း", "anolīnavuttitā": "မတွန့်ဆုတ်ဘဲ ကျင့်ခြင်း"})
assert F.SYN["apilāpanatā"] == "အပေါ်ယံ မပေါ်လောခြင်း" and F.SYN["asammussanatā"] == "မမေ့လျော့ခြင်း"
syn({"asammusanatā": F.SYN["asammussanatā"]})      # 4-03 spells «-mus-» where 2-01 has «-muss-»
# purity of view, the Mātikā quotations («… ti –»)
ph({"kammassakatañāṇaṃ": "ကံသာ မိမိ၏ ဥစ္စာ ဖြစ်ကြောင်း သိသော ဉာဏ်", "saccānulomikañāṇaṃ": "သစ္စာနှင့် လျော်ညီသော ဉာဏ်",
    "maggasamaṅgissa ñāṇaṃ": f"{MAGGA}နှင့် ပြည့်စုံသူ၏ ဉာဏ်", "phalasamaṅgissa ñāṇaṃ": f"{PHALA}နှင့် ပြည့်စုံသူ၏ ဉာဏ်",
    "jātibhayaṃ": "မွေးဖွားခြင်း ဘေး", "jarābhayaṃ": "အိုခြင်း ဘေး", "byādhibhayaṃ": "နာခြင်း ဘေး",
    "maraṇabhayaṃ": "သေခြင်း ဘေး", "jāti": "မွေးဖွားခြင်း", "jarā": "အိုခြင်း", "byādhi": "နာခြင်း",
    "maraṇaṃ": "သေခြင်း"}, True)
_TI = " ဟူသည်"
_MF = F.MFIXED
ph({"Diṭṭhivisuddhi kho panāti": _MF["diṭṭhivisuddhi kho pana."][:-1] + _TI,
    "Yathādiṭṭhissa ca padhānanti": _MF["yathādiṭṭhissa ca padhānaṃ."][:-1] + _TI,
    "Saṃvegoti": F.SAMVEGA + _TI, "Saṃvejaniyaṃ": f"{F.SAMVEGA} ရဖွယ်", "ṭhānanti": "အခြေအနေ" + _TI,
    "Saṃviggassa ca yoniso padhānanti": _MF["saṃviggassa ca yoniso padhānaṃ."][:-1] + _TI,
    "Asantuṭṭhitā ca kusalesu dhammesūti": _MF["asantuṭṭhitā ca kusalesu dhammesu."][:-1] + _TI,
    "Appaṭivānitā ca padhānasminti": _MF["appaṭivānitā ca padhānasmiṃ."][:-1] + _TI,
    "Vijjāti": S["vijjā"] + _TI, "Vimuttīti": S["vimutti"] + _TI,
    "Khaye ñāṇanti": _MF["khaye ñāṇaṃ."][:-1] + _TI, "Anuppāde ñāṇanti": _MF["anuppāde ñāṇanti."][:-1] + _TI})
assert _MF["saṃvego ca saṃvejaniyesu ṭhānesu."].startswith(f"{F.SAMVEGA} ရဖွယ် အခြေအနေ")
ph({"idha bhikkhu": "ဤသာသနာ၌ ရဟန်းသည်",
    "anuppannānaṃ pāpakānaṃ akusalānaṃ dhammānaṃ anuppādāya":
        f"{T['anuppannā']} ယုတ်မာသော {AKUS} {DH}တို့ မဖြစ်ပေါ်စေရန်",
    "chandaṃ janeti vāyamati vīriyaṃ ārabhati cittaṃ paggaṇhāti padahati":
        "ဆန္ဒကို ဖြစ်စေ၏၊ အားထုတ်၏၊ ဝီရိယကို စတင်၏၊ စိတ်ကို မြှင့်တင်၏၊ ကြိုးပမ်း၏",
    "uppannānaṃ pāpakānaṃ akusalānaṃ dhammānaṃ pahānāya": f"{T['uppannā']} ယုတ်မာသော {AKUS} {DH}တို့ကို ပယ်ရန်",
    "anuppannānaṃ kusalānaṃ dhammānaṃ uppādāya": f"{T['anuppannā']} {KUS} {DH}တို့ ဖြစ်ပေါ်စေရန်",
    "uppannānaṃ kusalānaṃ dhammānaṃ ṭhitiyā asammosāya bhiyyobhāvāya vepullāya bhāvanāya pāripūriyā":
        f"{T['uppannā']} {KUS} {DH}တို့ တည်တံ့ရန်၊ မပျောက်ပျက်ရန်၊ ပိုမို တိုးပွားရန်၊ ပြန့်ပြောရန်၊ "
        "ပွားများခြင်းဖြင့် ပြည့်စုံရန်",
    "tisso vijjā": num(S["vijjā"], "ti"),
    "pubbenivāsānussati ñāṇaṃ vijjā": f"ရှေးဘဝများကို အောက်မေ့နိုင်သော ဉာဏ်သည် {S['vijjā']} ဖြစ်သည်",
    "sattānaṃ cutūpapāte ñāṇaṃ vijjā": f"သတ္တဝါတို့၏ သေခြင်းနှင့် ဖြစ်ပေါ်ခြင်းကို သိသော ဉာဏ်သည် {S['vijjā']} ဖြစ်သည်",
    "āsavānaṃ khaye ñāṇaṃ vijjā":
        f"{N_['āsava']}တို့ {_MF['khaye ñāṇaṃ.'][:-1]}သည် {S['vijjā']} ဖြစ်သည်",
    "dve vimuttiyo": num(S["vimutti"], "dvi"), "cittassa": f"{F.MIND}၏",
    "adhimutti": f"အလွန် {S['vimutti']}", "nibbānañca": "နိဗ္ဗာန်လည်း"})
DEF_SUT = {}
for _k, _v in S.items():
    DEF_SUT[_k] = _v
    DEF_SUT[_k + "ṃ"] = _v

# saṅkhata / asaṅkhata (cūḷantara)
ph({"Yeva te dhammā sappaccayā": f"အကြင် {DHP}သည် {pred(T['sappaccayā'])}",
    "teva te dhammā saṅkhatā": f"ထို{DHP}သည်ပင် {pred(T['saṅkhatā'])}",
    "Yo eva so dhammo appaccayo": f"အကြင် {DH}သည် {pred(T['appaccayā'], False)}",
    "so eva so dhammo asaṅkhato": f"ထို{DH}သည်ပင် {pred(T['asaṅkhatā'], False)}"})

# ===================================================================================================== frames
ALLQ = {}     # Mātikā item as it stands after «Katame dhammā» / «ime dhammā»
for _k, _v in T.items():
    ALLQ[_k] = _v
for (_x, _y), _v in F.CEVA.items():
    ALLQ[f"{_x} ceva {_y} ca"] = _v
for (_y, _x), _v in F.CEVANO.items():
    ALLQ[f"{_y} ceva no ca {_x}"] = _v
    ALLQ[f"{_y} ceva na ca {_x}"] = _v
for _st, _d in F.FAMILY.items():
    _vp = _st + "vippayuttā"
    # a «kho pana» pair of the Mātikā: «X သဘောတရားများအနက် Y» (the approved sample form; consistency pass)
    ALLQ[f"{_vp} {_d['y']}"] = f"{T[_vp]} {F.DHAMMA_AMONG} {T[_d['y']]}"
    ALLQ[f"{_vp} {_d['ny']}"] = f"{T[_vp]} {F.DHAMMA_AMONG} {T[_d['ny']]}"
ALLQ["na hetū sahetukā"] = f"{T['na hetū']} {F.DHAMMA_AMONG} {T['sahetukā']}"
ALLQ["na hetū ahetukā"] = f"{T['na hetū']} {F.DHAMMA_AMONG} {T['ahetukā']}"
ALLQ["kenaci viññeyyā, kenaci na viññeyyā"] = f"{T['kenaci viññeyyā']}{COMMA} {T['kenaci na viññeyyā']}"
ALLQ["kenaci viññeyyā kenaci na viññeyyā"] = join2(T["kenaci viññeyyā"], T["kenaci na viññeyyā"])
ALLQ["neva ācayagāmi na apacayagāmino"] = T["nevācayagāmināpacayagāmino"]   # spelling of the Nikkhepa line
ALLQ["kilesā"] = T["kilesā"]


def q_term(k):
    if k not in ALLQ:
        raise F.Miss("Katame: " + k)
    return ALLQ[k]


def r_katame(m):
    return f"{q_term(m['t'])} {DHP} {F.CU_Q['pl']}"


PRED_NOUN = {"kusalā", "akusalā"}     # «ime dhammā kusalā / akusalā» = the model's noun predicate


def r_ime(m):
    """«ime dhammā X» = «ဤသဘောတရားများသည် {Mātikā X} သဘောတရားများ ဖြစ်ကြသည်» (the Aṭṭhakathākaṇḍa and 2-04 / 2-05
    form: the approved Mātikā string unchanged; consistency pass); kusalā / akusalā: «… ကုသိုလ် ဖြစ်ကြသည်»."""
    k = m["t"]
    if k == "kusalā":
        return F.IME_KUSALA
    if k in PRED_NOUN:
        return f"{IME_PL} {T[k]} {F.CU_COP['pl']}"
    if k in CLOSE_EXTRA:
        return f"{IME_PL} {pred(CLOSE_EXTRA[k])}"
    return f"{IME_PL} {q_term(k)} {DHP} {F.CU_COP['pl']}"


# «Tattha katamo X?» / «ayaṃ vuccati X»: definienda
DEF = {}
for _k, _v in {**SUBJ, "sakkāyadiṭṭhi": SKD, "vicikicchā": VICI, "sīlabbataparāmāso": SBP, "lobho": "လောဘ",
               "doso": "ဒေါသ", "moho": "မောဟ", "alobho": F.NAMES["alobho"], "adoso": F.NAMES["adoso"],
               "amoho": F.NAMES["amoho"]}.items():
    DEF[_k] = _v
for _k in list(HETU_KIND):
    for _n, _st in [("tayo", "ti"), ("nava", "nava"), ("cha", "cha")]:
        DEF[f"{_n} {_k}hetū"] = num(f"{HETU_KIND[_k]} {ROOT_}", _st)
for _k, _v in DEF_SUT.items():
    DEF.setdefault(_k, _v)
PL_DEF = {k for k in DEF if k.split()[0] in ("tayo", "nava", "cha")}


def r_term_series(m):
    """«Rūpāvacarā, arūpāvacarā, apariyāpannā – ime dhammā …»: each Mātikā term with its noun (consistency pass)."""
    return f"{COMMA} ".join(f"{T[x[0].lower() + x[1:]]} {DHP}" for x in m["l"].split(", "))


def r_tattha(m):
    k = m["n"][0].lower() + m["n"][1:]
    if k not in DEF:
        raise F.Miss("Tattha: " + k)
    n = "pl" if m["k"] == "e" else "sg"
    return f"{TATTHA} {DEF[k]} {F.CU_Q[n]}"


def r_vuccati(m):
    k = m["n"]
    if k not in DEF:
        raise F.Miss("vuccati: " + k)
    return VUCC.format(DEF[k])


def r_hetu_count(m):
    return DEF[f"{m['n'].lower()} {m['k']}hetū"]


def r_ime_count(m):
    return f"{F.CU_DEM['pl']} {DEF[m['n'] + ' ' + m['k'] + 'hetū']} {F.CU_COP['pl']}"


CEVA_SG = {   # singular «X Y-ena x ceva y ca» -> the plural Mātikā key
    "hetu ceva sahetuko ca": ("hetū", "sahetukā"), "hetu ceva hetusampayutto ca": ("hetū", "hetusampayuttā"),
    "āsavo ceva āsavasampayutto ca": ("āsavā", "āsavasampayuttā"),
    "saṃyojanañceva saṃyojanasampayuttañca": ("saṃyojanā", "saṃyojanasampayuttā"),
    "gantho ceva ganthasampayutto ca": ("ganthā", "ganthasampayuttā"),
    "nīvaraṇañceva nīvaraṇasampayuttañca": ("nīvaraṇā", "nīvaraṇasampayuttā"),
    "upādānañceva upādānasampayuttañca": ("upādānā", "upādānasampayuttā"),
    "kileso ceva kilesasampayutto ca": ("kilesā", "kilesasampayuttā"),
    "kileso ceva kilesasampayuttā ca": ("kilesā", "kilesasampayuttā"),
    "kileso ceva kilesasampayuttañca": ("kilesā", "kilesasampayuttā"),
    "parāmāso ceva parāmaṭṭho ca": ("parāmāsā", "parāmaṭṭhā"),
}


def r_ceva_sg(m):
    a = m["a"][0].lower() + m["a"][1:]
    return f"{SUBJ[a]}သည် {INSTR[m['b']]} {pred(F.CEVA[CEVA_SG[m['c']]], False)}"


def r_aññamañña(m):
    return f"ထိုတို့သည် အချင်းချင်း {pred(ALLQ[m['c']])}"


TEVA_N = {"āsavā": N_["āsava"], "saṃyojanāni": N_["saṃyojana"], "ganthā": N_["gantha"],
          "nīvaraṇāni": N_["nīvaraṇa"], "upādānāni": N_["upādāna"], "kilesā": N_["kilesa"],
          "parāmāso": N_["parāmāsa"]}


def r_teva(m):
    c = m["c"]
    if c in CEVA_SG:          # «ထို Xသည်ပင် … သဘောတရား ဖြစ်သည်» (the Aṭṭhakathākaṇḍa form; consistency pass)
        return f"ထို {TEVA_N[m['n']]}သည်ပင် {F.CEVA[CEVA_SG[c]]} {DH} {F.CU_COP['sg']}"
    return f"ထို {TEVA_N[m['n']]}များသည်ပင် {ALLQ[c]} {DHP} {F.CU_COP['pl']}"


TEHI_Y = {"sampayuttā": f"ထို{DH}တို့နှင့် ယှဉ်တွဲသော", "vippayuttā": f"ထို{DH}တို့နှင့် ကင်းကွာသော"}
for _y in ["sahetukā", "ahetukā", "na hetū sahetukā", "na hetū ahetukā", "sāsavā", "saṃyojaniyā", "ganthaniyā",
           "nīvaraṇiyā", "parāmaṭṭhā", "upādāniyā", "saṃkilesikā", "saṃkiliṭṭhā"]:
    TEHI_Y[_y] = f"ထို{DH}တို့နှင့် စပ်လျဉ်း၍ {q_term(_y)}"


def r_tehi(m):
    return f"{TEHI_Y[m['y']]} {DHP}"


LOCPL = {"Paritte": "parittā", "Mahaggate": "mahaggatā", "Appamāṇe": "appamāṇā", "Atīte": "atītā",
         "Anāgate": "anāgatā", "Paccuppanne": "paccuppannā", "Ajjhatte": "ajjhattā", "Bahiddhā": "bahiddhā",
         "Ajjhattabahiddhā": "ajjhattabahiddhā"}


def r_arabbha(m):
    return f"{T[LOCPL[m['x']]]} {DH}တို့ကို အာရုံပြု၍ ဖြစ်ပေါ်ကြသော {CCD}"


def _vpred(a):
    return pred(PH[a], True)


def r_kenaci(m):
    a, b, sep = m["a"], m["b"], COMMA if m["c"] else ""
    head = "တစ်ဖန် " if m["vp"] else ""
    return f"{head}အကြင် {DHP}သည် {_vpred(a)}{sep} ထို{DHP}သည် {PH[b][:-3]}သည် မဟုတ်ကြ"


def r_ye(m):
    g = YE_GEN[m["gen"]] + " " if m["gen"] else ""
    return f"{g}{F.items_my(F.list_items(m['list']))} {DHP}"


def r_rel(m):
    """Synonym list after «Yo / Yā / Yaṃ [GEN]»; a Pāli comma inside the list is the same «၊» as the joiner."""
    g = F.GEN[m["gen"]] + " " if m["gen"] else ""
    return g + F.items_my(F.list_items(m["list"].replace(",", "")))


MICCHA_ALL = f"{MICCHADITTHI} အားလုံးသည်"


def r_sabbapi(m):
    x = m["x"]
    if x not in DEF:
        raise F.Miss("sabbāpi: " + x)
    th = f"{THAPETVA_ACC[m['th']]}{THAP} " if m["th"] else ""
    return f"{th}{MICCHA_ALL} {DEF[x]} ဖြစ်သည်"


THAPETVA_ACC = {"sīlabbataparāmāsasaṃyojanaṃ": _CL_NAMES["sīlabbataparāmāsasaṃyojanaṃ"],
                "sīlabbataparāmāsaṃ kāyaganthaṃ": _CL_NAMES["sīlabbataparāmāso kāyagantho"],
                "sīlabbatupādānañca attavādupādānañca":
                    f"{_CL2['sīlabbatupādānaṃ']}နှင့် {_CL2['attavādupādānaṃ']}"}


def r_sabbepi(m):
    head = f"{T[m['k']]} {DH} အားလုံးသည်" if m["k"] else f"{DH} အားလုံးသည်"
    t = m["t"]           # the Mātikā term + its noun, as the «ime dhammā X» closer (consistency pass)
    return f"{head} {T[t] if t in PRED_NOUN else q_term(t) + ' ' + DHP} {F.CU_COP['pl']}"


def r_allsubj(m):
    return f"{ALL_SUBJ[m['s']]} {DEF[m['x']]} ဖြစ်သည်"


def r_seq(m):
    parts = []
    pos = 0
    s = m[0]
    while pos < len(s):
        mm = LIST_ONE.match(s, pos)
        parts.append(lex(mm[0]))
        pos = mm.end()
        if s.startswith(" ", pos):
            pos += 1
    return (COMMA + " ").join(parts)


def lex(k):
    for k2 in (k, k[0].lower() + k[1:], k[0].upper() + k[1:]):
        if k2 in LEX:
            return LEX[k2]
    raise F.Miss("lex: " + k)


def r_lex(m):
    return lex(m[0])


LEX = {}
LIST_ONE = None


def build():
    """Install the Nikkhepa rules (in memory) and rebuild the clause engine."""
    global LIST_ONE
    for k, v in SYN.items():
        add(F.SYN, k, v)
    F.SYN_MAXLEN = max(F.SYN_MAXLEN, max(len(k.split()) for k in F.SYN))
    LEX.clear()
    for d in (F.NAMES, F.SYN, PH):
        for k, v in d.items():
            if v is None:
                continue
            if k in LEX and LEX[k] != v:
                if d is PH:
                    raise SystemExit(f"PH conflicts with table: {k}")
                continue
            LEX.setdefault(k, v)
    for k in list(LEX):
        LEX.setdefault(k[0].lower() + k[1:], LEX[k])
    na = F.NA
    alt = F._alt
    L = alt({k[0].lower() + k[1:] for k in LISTABLE})
    LIST_ONE = re.compile(f"{L}{na}")
    qt = alt(ALLQ.keys() | CLOSE_EXTRA.keys())
    mt = alt({k[0].upper() + k[1:] for k in T if not k.startswith(("na ", "no "))} | set(T))
    rules = [
        (rf"(?P<l>{mt}(?:, {mt})+)(?= – ime dhammā)", r_term_series),
        (rf"Katame dhammā (?P<t>{qt})(?=\?)", r_katame),
        (rf"[Ii]me dhammā (?P<t>{qt})(?=[.?]|$)", r_ime),
        (rf"Tattha katam(?P<k>o|ā|aṃ|e) (?P<n>{alt(DEF)})(?=\?|…pe…)", r_tattha),
        (rf"(?:ayaṃ|idaṃ) vuccati (?P<n>{alt(DEF)}){na}", r_vuccati),
        (rf"(?P<n>[Tt]ayo|nava|cha) (?P<k>{alt(HETU_KIND)})hetū{na}", r_hetu_count),
        (rf"[Ii]me (?P<n>tayo|nava|cha) (?P<k>{alt(HETU_KIND)})hetū{na}", r_ime_count),
        (rf"(?P<a>{alt(SUBJ)}) (?P<b>{alt(INSTR)}) (?P<c>{alt(CEVA_SG)}){na}", r_ceva_sg),
        (rf"te aññamaññaṃ (?P<c>hetū ceva sahetukā ca|hetū ceva hetusampayuttā ca){na}", r_aññamañña),
        (rf"(?:Teyeva|Teva|Tāneva|Sveva) (?P<n>{alt(TEVA_N)}) (?P<c>{qt}|{alt(CEVA_SG)}){na}", r_teva),
        (rf"Tehi dhammehi ye dhammā (?P<y>{alt(TEHI_Y)}){na}", r_tehi),
        (rf"(?P<x>{alt(LOCPL)}) dhamme ārabbha ye uppajjanti cittacetasikā dhammā", r_arabbha),
        (r"(?:(?P<vp>ye vā pana )|Ye )te dhammā (?P<a>\w+viññeyyā)(?P<c>,)? na te dhammā (?P<b>\w+viññeyyā)",
         r_kenaci),
        (rf"Ye dhammā (?:(?P<gen>{alt(YE_GEN)}) )?(?P<list>[^,]+?)(?=, )", r_ye),
        (rf"(?:Ṭhapetvā (?P<th>{alt(THAPETVA_ACC)}) )?[Ss]abbāpi micchādiṭṭhi (?P<x>{alt(DEF)}){na}", r_sabbapi),
        (SAMANA_RE, r_samana),
        (rf"(?:Sabbepi (?P<k>akusalā|kusalā)|Sabbeva) dhammā (?P<t>{qt})(?=[.?]|$)", r_sabbepi),
        (rf"(?P<s>{alt(ALL_SUBJ)}) (?P<x>{alt(DEF)}){na}", r_allsubj),
        (rf"{L}{na}(?: {L}{na})+", r_seq),
        (alt(LEX) + na, r_lex),
        (rf"(?:[Yy]o|[Yy]ā|[Yy]aṃ)(?: (?P<gen>{alt(F.GEN)}))? (?P<list>[^;–]+?)(?= – |\.$)", r_rel),
    ]
    F.CU_SEP.insert(0, ("ः ", COMMA + " "))
    F.CU_EXTRA_RULES[:] = [(re.compile(p), f) for p, f in rules]
    F.rebuild_cu()


def write(name, txt):
    txt = unicodedata.normalize("NFC", txt)
    (OUT / name).write_text(txt, encoding="utf-8")
    print(f"wrote {name}: {sum(1 for l in txt.splitlines() if l)} lines")


def chapter(key):
    name = CHAPTERS[key]
    write(name, F.translate_cu((PALI / name).read_text(encoding="utf-8-sig")))


if __name__ == "__main__":
    build()
    for key in (sys.argv[1:] or list(CHAPTERS)):
        chapter(key)
