"""Burmese zero-shot of pi-6 (Yamaka, «အတွဲလိုက် မေးဖြေခြင်း»): 2-02-khandhayamaka, 4-dhatuyamaka,
5-01 / 5-02 / 5-03-saccayamaka.

usage: python3 -I -X utf8 make_ch2-02-4-5.py [chapter ...] [--misses] [--who]
Imports my6_formulas (READ ONLY: its tables are extended IN MEMORY here, never edited on disk; every new string is in
notes-ch2-02-4-5.md). Model: make_sample.py (functions copied, not run). Every line comes from the Pāli through the
module frames plus the frames / tables of this script:
  * terms: the 18 dhātus (pi-2 ^2-183 list, read at import), the four saccas (pi-4 ^4-M-5, pi-2 ^2-206), bare words
    (cakkhu … dhammo, dukkhaṃ … maggo, saccaṃ / saccā, dhātu / dhātū) with their accusatives, special subjects;
  * paṇṇattivāra frames for avaseso / avasesaṃ / avasesā (singular and plural), the special subjects, fragments
    between «…»;
  * pavattivāra: a lead parser for the person / moment / place leads of the sacca chapters (units joined «၊ »; a run
    of person groups joined as the module does; a final person run takes «အား», a final moment «ထိုသူတို့အား»);
    the «X-ñca … Y-ñca …» frame; pariññāvāra (parijānāti / pajahati) frames;
  * the «…pe…» engine: each piece between «…» translated (sentence or fragment), every «…» kept;
  * headings, colophons and the editorial notes (EDIT).
A sentence that nothing matches raises F.Miss: nothing is guessed. A chapter is written only when every line passes.
--misses lists unmatched lines; --who lists the leads.
"""
import pathlib
import re
import sys

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import my6_formulas as F  # noqa: E402

ROOT = HERE.parents[3]
PALI = ROOT / "AI_translation/pali/pi-6_split_chapters"
OUT = ROOT / "AI_translation/burmese/pi-6-burmese-plain-zeroshot_split_chapters"
NAMES_OUT = ["2-02-khandhayamaka.md", "4-dhatuyamaka.md", "5-01-saccayamaka.md", "5-02-saccayamaka.md",
             "5-03-saccayamaka.md"]
W = F.W
C, END, PE, AND, DAT = F.C, F.END, F.PE, F.AND, F.DAT
NEW = {}          # every new string of this script: Pāli -> Burmese (for the notes and the check)


def new(pali, my):
    NEW.setdefault(pali, my)
    return my


# ===================================================================================== terms: dhātu
DH_HEAD, DH = F.items("2", "^2-183")             # «ဓာတ် ဆယ့်ရှစ်ပါး», {cakkhudhātu: «မျက်စိ ဓာတ်», …}
DH_ORDER = ["cakkhudhātu", "sotadhātu", "ghānadhātu", "jivhādhātu", "kāyadhātu", "rūpadhātu", "saddadhātu",
            "gandhadhātu", "rasadhātu", "phoṭṭhabbadhātu", "cakkhuviññāṇadhātu", "sotaviññāṇadhātu",
            "ghānaviññāṇadhātu", "jivhāviññāṇadhātu", "kāyaviññāṇadhātu", "manodhātu", "manoviññāṇadhātu",
            "dhammadhātu"]
assert sorted(DH_ORDER) == sorted(DH)
DHATU = W("1", "^1-M2-121", "dhātu", "ဓာတ်", key="dhātu")
DHATU_PL = new("dhātū (plural)", DHATU + "တို့")     # as khandhā «အစုအဝေးတို့» (pi-5)
for k in DH_ORDER:
    F.add_subject(k, DH[k])
    F.add_term(k, DH[k], acc=k[:-1] + "uṃ")
F.add_term("dhātu", DHATU, acc="dhātuṃ")
F.add_term("dhātū", DHATU_PL, plural=True)
# bare words of the dhātu paṇṇatti: the dhātu name without «ဓာတ်» (pi-2 ^2-183), rūpaṃ as the sample («ရုပ်»)
BARE_DH = {"cakkhu": ("cakkhudhātu", "cakkhuṃ"), "sotaṃ": ("sotadhātu", None), "ghānaṃ": ("ghānadhātu", None),
           "jivhā": ("jivhādhātu", "jivhaṃ"), "kāyo": ("kāyadhātu", "kāyaṃ"), "saddo": ("saddadhātu", "saddaṃ"),
           "gandho": ("gandhadhātu", "gandhaṃ"), "raso": ("rasadhātu", "rasaṃ"),
           "phoṭṭhabbo": ("phoṭṭhabbadhātu", "phoṭṭhabbaṃ"), "mano": ("manodhātu", "manaṃ"),
           "dhammo": ("dhammadhātu", "dhammaṃ")}
for v in ("cakkhu", "sota", "ghāna", "jivhā", "kāya", "mano"):
    BARE_DH[v + "viññāṇaṃ"] = (v + "viññāṇadhātu", None)
for k, (d, acc) in BARE_DH.items():
    my = DH[d][: -len(" " + DHATU)]
    assert DH[d].endswith(" " + DHATU)
    F.add_term(k, my, acc=acc)
F.PT_ACC["jivha"] = "jivhā"                       # source slip ^6-4-15 «jivha ṭhapetvā» for jivhaṃ
W("1", "^1-1044", "rūpaṃ", "ရုပ်")

# ===================================================================================== terms: sacca
SACCA = W("2", "^2-206", "Cattāri saccāni", "သစ္စာ", key="sacca")
SACCA_H = W("2", "^2-206", "Cattāri saccāni", "သစ္စာ လေးပါး", key="Cattāri saccāni")
SACCAS = {"dukkhasaccaṃ": W("4", "^4-M-5", "dukkhasaccaṃ", "ဒုက္ခ သစ္စာ"),
          "samudayasaccaṃ": W("4", "^4-M-5", "samudayasaccaṃ", "ဖြစ်ပေါ်ခြင်း သစ္စာ"),
          "nirodhasaccaṃ": W("4", "^4-M-5", "nirodhasaccaṃ", "ချုပ်ငြိမ်းခြင်း သစ္စာ"),
          "maggasaccaṃ": W("4", "^4-M-5", "maggasaccaṃ", "မဂ် သစ္စာ")}
for k, v in SACCAS.items():
    F.add_subject(k, v)
    F.add_term(k, v)
F.add_term("saccaṃ", SACCA)
F.add_term("saccā", new("saccā (plural)", SACCA + "တို့"), plural=True)
# bare words: dukkhaṃ = painful feeling (pi-1 «နာကျင်မှု»: what kāyika / cetasika dukkha names), the others pi-1 / pi-4
DUKKHA = W("1", "^1-559", "dukkhaṃ hoti", "နာကျင်မှု", key="dukkhaṃ")
F.add_term("dukkhaṃ", DUKKHA)
F.add_term("samudayo", W("1", "^1-1063", "samuday", "ဖြစ်ပေါ်ခြင်း"), acc="samudayaṃ")
F.add_term("nirodho", W("1", "^1-1063", "nirodh", "ချုပ်ငြိမ်းခြင်း"), acc="nirodhaṃ")
MAGGA = W("1", "^1-1039", "maggahetukā", "မဂ်", key="magga")
F.add_term("maggo", MAGGA, acc="maggaṃ")
KAYIKA = W("1", "^1-559", "kāyikaṃ dukkhaṃ", "ကိုယ်ပိုင်းဆိုင်ရာ နာကျင်မှု", key="kāyikaṃ dukkhaṃ")
CETASIKA_D = new("cetasikaṃ dukkhaṃ", "စိတ်ပိုင်းဆိုင်ရာ " + DUKKHA)    # cetasika «စိတ်ပိုင်းဆိုင်ရာ» (pi-1 termbase)

# special subjects of the paṇṇatti sentences (Pāli -> (Burmese, plural))
SPECIAL = {
    "Dibbacakkhu paññācakkhu": (new("Dibbacakkhu paññācakkhu", "နတ်မျက်စိနှင့် ပညာမျက်စိတို့"), True),
    "Dibbasotaṃ taṇhāsotaṃ": (new("Dibbasotaṃ taṇhāsotaṃ", "နတ်နားနှင့် တပ်မက်မှု ရေစီးတို့"), True),
    "Sīlagandho samādhigandho paññāgandho":
        (new("Sīlagandho samādhigandho paññāgandho", "သီလ၏ အနံ့၊ သမာဓိ၏ အနံ့နှင့် ပညာ၏ အနံ့တို့"), True),
    "Attharaso dhammaraso vimuttiraso":
        (new("Attharaso dhammaraso vimuttiraso", "အနက်၏ အရသာ၊ တရား၏ အရသာနှင့် လွတ်မြောက်မှု၏ အရသာတို့"), True),
    "Kāyikaṃ dukkhaṃ cetasikaṃ dukkhaṃ": (new("Kāyikaṃ dukkhaṃ cetasikaṃ dukkhaṃ",
                                             f"{KAYIKA}{AND} {CETASIKA_D}တို့"), True),
}
W("5", "^5-374", "dibbacakkhuṃ, paññācakkhu", "နတ်မျက်စိ၊ ပညာမျက်စိ", key="dibbacakkhu / paññācakkhu")
W("5", "^5-375", "dibbasotaṃ", "နတ်နား", key="dibbasotaṃ")
# «sotaṃ» of the two Dibbasotaṃ taṇhāsotaṃ sentences: the Pāli word play (sota = ear and stream) is kept with the
# Pāli word in quotes: «“သောတ”» (understanding > consistency; see notes)
SOTA_WORD = new("sotaṃ (ear / stream, in the Dibbasotaṃ taṇhāsotaṃ sentences)", "“သောတ” (နား သို့မဟုတ် ရေစီး)")

# ===================================================================================== verbs: pariññāvāra
PVERB = {"parijān": W("5", "^5-317", "parijānaṃ", "ပိုင်းခြား သိ", key="parijānāti"),
         "pajah": W("5", "^5-317", "pajahaṃ", "ပယ်", key="pajahati")}


def p_verb(root, tense, neg=False, form="stmt", pl=False):
    """parijānāti «ပိုင်းခြား သိသည်» / pajahati «ပယ်သည်» in every tense / polarity (forms as F.my_verb);
    the negative «မ» goes before the last word: «ပိုင်းခြား မသိ», «မပယ်»."""
    stem = PVERB[root]
    if neg:
        head, _, last = stem.rpartition(" ")
        stem = (head + " " if head else "") + F.NEG + last
    fut = tense == "fut"
    ko_ = "ကြ" if pl else ""
    v = stem + ((ko_ + F.TENSE_MY[tense]) if fut else (F.TENSE_MY[tense] + ko_))
    if form == "stmt":
        return v if (neg or fut) else v + "သည်"
    if form == "cl":
        return v if (neg or fut) else v + "၏"
    if form == "q":
        return v + ("လော" if fut else "သလော")
    if form == "notso":
        return v + ("" if fut else "သည်") + F.NOT_SO
    raise ValueError(form)


PV_END = [("issanti", "fut", True), ("issati", "fut", False), ("ittha", "past", None), ("anti", "pres", True),
          ("āti", "pres", False), ("ati", "pres", False)]
PVB = r"(?:na |nap|n)?(?:parijān|pajah|ppajah)\w*"


def pali_pverb(w):
    """'parijānāti' / 'na parijānitthāti' / 'nappajahissanti' -> (root, tense, neg, plural or None)."""
    w = w.strip()
    neg = False
    if w.startswith("na "):
        neg, w = True, w[3:]
    if w.startswith("nappajah"):
        neg, w = True, w[3:]
    w = re.sub(r"īti$", "i", w)
    w = re.sub(r"itthāti$", "ittha", w)
    for root in PVERB:
        if w.startswith(root):
            rest = w[len(root):]
            for e, tense, pl in PV_END:
                if rest == e:
                    return root, tense, neg, pl
    raise F.Miss("pali_pverb: " + w)


def PV(w, form="stmt", pl=False):
    root, tense, neg, p = pali_pverb(w)
    return p_verb(root, tense, neg, form, pl or bool(p))


def obj(tok):
    """accusative object of a pariññā verb: rūpakkhandhaṃ / dukkhasaccaṃ / cakkhudhātuṃ / -ñca -> «Xကို»."""
    t = re.sub(r"ñca$", "ṃ", tok)
    t = F.PT_ACC.get(t, t)
    if t not in F.SUBJ:
        raise F.Miss("object: " + tok)
    return F.SUBJ[t] + "ကို"


YO = ("အကြင်သူသည်", "ထိုသူသည်")                    # yo … so …: «အကြင်သူသည် …၊ ထိုသူသည် … သလော။» (as yassa … tassa)
new("yo … so …", f"{YO[0]} …{C} {YO[1]} …")
ARAHA = W("4", "^4-M-7", "Arahā", "ရဟန္တာ", key="arahā")
W("5", "^5-546", "arahantānaṃ", "ရဟန္တာတို့", key="arahantānaṃ")
AGGA = W("2", "^2-1029", "agga", "အမြတ်ဆုံး", key="agga")   # as the ch. 3 agent (pi-2 ^2-1029)
AGGAMAGGA = f"{AGGA} {MAGGA}"
SAMANGI = W("1", "^1-1039", "Ariyamaggasamaṅgissa", "နှင့် ပြည့်စုံသူ", key="-samaṅgī")
AGGASAMANGI = new("Aggamaggasamaṅgī", f"{AGGAMAGGA}{SAMANGI}")
PUTHUJJANA = W("1", "^1-1007", "puthujjano", "ပုထုဇဉ်", key="puthujjana")
PATILABH = W("2", "^2-974", "paṭilabhati", "ရရှိ", key="paṭilabhati")
GET_PATH = new("maggaṃ paṭilabhissanti (relative)", f"{MAGGA}ကို {PATILABH}မည့်")
NOGET_PATH = new("maggaṃ na paṭilabhissanti (relative)", f"{MAGGA}ကို {F.NEG}{PATILABH}မည့်")
PUGGALA = F.PUGGALA
# pariññā subjects: Pāli -> (Burmese subject, plural)
P_WHO = {
    "Arahā": (ARAHA, False),
    "Aggamaggasamaṅgī": (AGGASAMANGI, False),
    "Ye maggaṃ paṭilabhissanti te": (new("Ye maggaṃ paṭilabhissanti te", f"{GET_PATH}{F.THEM}"), True),
    "Aggamaggasamaṅgiñca arahantañca ṭhapetvā avasesā puggalā":
        (new("Aggamaggasamaṅgiñca arahantañca ṭhapetvā avasesā puggalā",
             f"{AGGASAMANGI}{AND} {ARAHA}ကို {F.THAPETVA}{C} {F.AVASESA} {PUGGALA}တို့"), True),
    "Arahā ye ca puthujjanā maggaṃ na paṭilabhissanti te":
        (new("Arahā ye ca puthujjanā maggaṃ na paṭilabhissanti te", f"{ARAHA}{AND} {NOGET_PATH} {PUTHUJJANA}တို့"),
         True),
    "Aggamaggasamaṅgī ye ca puthujjanā maggaṃ na paṭilabhissanti te":
        (new("Aggamaggasamaṅgī ye ca puthujjanā maggaṃ na paṭilabhissanti te",
             f"{AGGASAMANGI}{AND} {NOGET_PATH} {PUTHUJJANA}တို့"), True),
}
PW = "(?P<who>" + "|".join(re.escape(k) for k in sorted(P_WHO, key=len, reverse=True)) + ")"
Q_PAR = re.compile(rf"^(?P<vp>[Yy]o vā pana|[Yy]o) (?P<x>\S+) (?P<v1>{PVB}) so (?P<y>\S+) (?P<v2>{PVB})[?.]$")
A_PAR_BUT = re.compile(rf"^{PW} (?P<x>\S+) (?P<v1>{PVB}), no ca (?P<te>te )?(?P<y>\S+) (?P<v2>{PVB})\.$")
A_PAR_BOTH = re.compile(rf"^{PW} (?P<x>\S+?ñca) (?P<v1>{PVB}) (?P<y>\S+?ñca) (?P<v2>{PVB})\.?$")


def pariñña_sentence(s):
    m = Q_PAR.match(s)
    if m:
        pre = F.VA_PANA + " " if "vā pana" in m["vp"] else ""
        return f"{pre}{YO[0]} {obj(m['x'])} {PV(m['v1'], 'cl')}{C} {YO[1]} {obj(m['y'])} {PV(m['v2'], 'q')}{END}"
    m = A_PAR_BUT.match(s)
    if m:
        who, pl = P_WHO[m["who"]]
        r2, t2, n2, p2 = pali_pverb(m["v2"])
        v2 = p_verb(r2, t2, True, "notso" if n2 else "stmt", pl)
        te = f"{F.PRO['tesaṃ'][:-len(DAT)]}သည် " if m["te"] else ""
        return f"{who}သည် {obj(m['x'])} {PV(m['v1'], pl=pl)}{C} {F.BUT} {te}{obj(m['y'])} {v2}{END}"
    m = A_PAR_BOTH.match(s)
    if m:
        who, pl = P_WHO[m["who"]]
        return (f"{who}သည် {obj(m['x'])}လည်း {PV(m['v1'], pl=pl)}{C} {obj(m['y'])}လည်း {PV(m['v2'], pl=pl)}"
                f"{END}")
    return None


# ===================================================================================== pavattivāra: leads
PLACES_NEW = {"apāya": W("5", "^5-317", "Catūhapāyehi", "အပါယ်", key="apāya")}
F.PLACES.update(PLACES_NEW)
AVASESE = F.AVASESA                                                    # avasese (loc.) «ကြွင်းကျန်သော …၌»
KHANA = W("5", "^5-366", "Uppādakkhaṇe vimuttaṃ, bhaṅgakkhaṇe", "ဖြစ်ခြင်း ခဏ၌", key="uppādakkhaṇe")
MOMENT = {"uppādakkhaṇe": KHANA,
          "bhaṅgakkhaṇe": W("5", "^5-366", "bhaṅgakkhaṇe", "ပြိုပျက်ခြင်း ခဏ၌")}
CITTA = F.TOPICS["Citta"]                                              # «စိတ်»
TANHA = W("2", "^2-834", "tisso taṇhā", "တပ်မက်မှု", key="taṇhā")
VIPP = "နှင့် ကင်းကွာသော"                                              # -vippayutta (core style rule)
PHALA = W("1", "^1-996", "maggaphalāni", "ဖိုလ်", key="phala")
GEN = {   # genitive of a moment phrase -> Burmese (before «၏»)
    "cittassa": CITTA,
    "taṇhāya": TANHA,
    "maggassa": MAGGA,
    "aggamaggassa": AGGAMAGGA,
    "phalassa": PHALA,
    "aggaphalassa": f"{AGGA} {PHALA}",
    "maggassa ca phalassa ca": f"{MAGGA}{AND} {PHALA}",
    "aggamaggassa ca phalassa ca": f"{AGGAMAGGA}{AND} {PHALA}",
    "pacchimacittassa": new("pacchimacitta", f"နောက်ဆုံး {CITTA}"),
    "upapatticittassa": new("upapatticitta", f"{F.PART['upapajjantānaṃ'][0][:-2]}ခြင်း {CITTA}"),
    "taṇhāvippayuttacittassa": f"{TANHA}{VIPP} {CITTA}",
    "maggavippayuttacittassa": f"{MAGGA}{VIPP} {CITTA}",
    "maggavippayuttataṇhāvippayuttacittassa": new("maggavippayuttataṇhāvippayuttacitta",
                                                   f"{MAGGA}နှင့် ကင်းကွာ၍ {TANHA}{VIPP} {CITTA}"),
    "taṇhāvippayuttamaggavippayuttacittassa": new("taṇhāvippayuttamaggavippayuttacitta",
                                                   f"{TANHA}နှင့် ကင်းကွာ၍ {MAGGA}{VIPP} {CITTA}"),
}
GEN["uppatticittassa"] = GEN["upapatticittassa"]
PAVATTE = new("pavatte (in the course of existence)", "ဘဝ တည်နေစဉ်")
VATTAMANE = W("5", "^5-556", "citte vattamāne", "စိတ် ဖြစ်နေစဉ်", key="citte vattamāne")
CITTE = {   # «… citte vattamāne» -> Burmese
    "taṇhāvippayuttacitte": f"{TANHA}{VIPP} {VATTAMANE}",
    "maggavippayuttacitte": f"{MAGGA}{VIPP} {VATTAMANE}",
    "dutiye citte": new("dutiye citte vattamāne", f"ဒုတိယ {VATTAMANE}"),
    "dutiye akusale citte": new("dutiye akusale citte vattamāne", f"ဒုတိယ {F.BASE['akusala'][0]} {VATTAMANE}"),
}
ANANTARA = W("2", "^2-751", "samanantarā", "ချက်ချင်း နောက်၌", key="anantarā")
REL = {   # relative clauses and named persons (gen. pl.) -> Burmese person phrase
    "ye maggaṃ paṭilabhissanti": f"{GET_PATH}{F.THEM}",
    "ye ca maggaṃ paṭilabhissanti": f"{GET_PATH}{F.THEM}",
    "ye caññe maggaṃ paṭilabhissanti": new("ye caññe maggaṃ paṭilabhissanti", f"{GET_PATH} {F.OTHERS}"),
    "ye puthujjanā maggaṃ na paṭilabhissanti": new("ye puthujjanā maggaṃ na paṭilabhissanti",
                                                   f"{NOGET_PATH} {PUTHUJJANA}တို့"),
    "ye ca puthujjanā maggaṃ na paṭilabhissanti": f"{NOGET_PATH} {PUTHUJJANA}တို့",
    "yassa cittassa anantarā aggamaggaṃ paṭilabhissanti":
        new("yassa cittassa anantarā aggamaggaṃ paṭilabhissanti",
            f"အကြင်{CITTA}၏ {ANANTARA} {AGGAMAGGA}ကို {PATILABH}မည့်{F.THEM}"),
    "ye ca arūpaṃ upapajjitvā parinibbāyissanti": F.GROUP_ATOMS["ye arūpaṃ upapajjitvā parinibbāyissanti"],
    "arahantānaṃ": "ရဟန္တာတို့",
    "aggamaggasamaṅgīnaṃ": f"{AGGASAMANGI}တို့",
    "pacchimacittasamaṅgīnaṃ": new("pacchimacittasamaṅgīnaṃ", f"{GEN['pacchimacittassa']}{SAMANGI}တို့"),
    "āpāyikānaṃ": new("āpāyikānaṃ", f"{PLACES_NEW['apāya']}{F.LOC} {F.HAS}{F.THEM}"),
    "nirodhasamāpannānaṃ": new("nirodhasamāpannānaṃ", "ချုပ်ငြိမ်းခြင်း သမာပတ်ကို ဝင်စားနေ" + F.THEM),
}
REL_RE = sorted(REL, key=lambda k: -len(k.split()))
ABHI = new("abhisametāvī (attr.)", "သစ္စာကို ထင်ထင်ရှားရှား သိမြင်ပြီး")       # pi-5 abhisameti «ထင်ထင်ရှားရှား သိမြင်»
ANABHI = new("anabhisametāvī (attr.)", "သစ္စာကို ထင်ထင်ရှားရှား မသိမြင်ရသေး")
W("5", "^5-431", "abhisametu", "ထင်ထင်ရှားရှား သိမြင်", key="abhisameti")
W("5", "^5-556", "Puthujjano", "ပုထုဇဉ်", key="puthujjano")
# person attributes before a participle (or alone): gen. pl. -> attributive stem (+ «သော» / «သူတို့»)
ATTR = {"abhisametāvīnaṃ": ABHI, "anabhisametāvīnaṃ": ANABHI}
SA = {"cakkhu": "မျက်စိ", "sota": "နား", "ghāna": "နှာခေါင်း", "rūpa": F.RUPA_W, "citta": CITTA}
SA_ATTR = {}      # sa-X-ka «X ရှိလျက်» / a-X-ka «X မရှိဘဲ» (as the ch. 3 agent), joined with a space
for k, v in SA.items():
    SA_ATTR[f"sa{k}kānaṃ"] = new(f"sa{k}ka", f"{v} {F.HAVE}လျက်")
    SA_ATTR[f"a{k}kānaṃ"] = new(f"a{k}ka", f"{v} မ{F.HAVE}ဘဲ")
ATTR.update(SA_ATTR)
W("1", "^1-M2-2", "ahetukā dhammā", "အမြစ် မရှိသော", key="a-X-ka (without)")


def _moment_at(toks, i):
    """A moment phrase at toks[i]: [avasese] [places-loc] [pavatte] GEN (uppāda|bhaṅga)kkhaṇe | … citte vattamāne
    | tassa cittassa …kkhaṇe -> (Burmese, next i) or None."""
    j, pre = i, []
    places = []
    while j < len(toks) and F._place_form(toks[j]) and F._place_form(toks[j])[1] == "loc":
        places.append(F._place_form(toks[j])[0])
        j += 1
    if places:
        pre.append(F._join_places(places) + F.LOC)
    if j < len(toks) and toks[j] == "pavatte":
        pre.append(PAVATTE)
        j += 1
    if j + 1 < len(toks) and toks[j] == "tassa" and toks[j + 1] == "cittassa" and j + 2 < len(toks) \
            and toks[j + 2] in MOMENT:
        return " ".join(pre + [f"ထို{CITTA}၏ {MOMENT[toks[j + 2]]}"]), j + 3
    for n in (4, 1):
        g = " ".join(toks[j:j + n])
        if g in GEN and j + n < len(toks) and toks[j + n] in MOMENT:
            return " ".join(pre + [f"{GEN[g]}၏ {MOMENT[toks[j + n]]}"]), j + n + 1
    for n in (3, 2, 1):
        g = " ".join(toks[j:j + n])
        if g in CITTE and j + n < len(toks) and toks[j + n] == "vattamāne":
            return " ".join(pre + [CITTE[g]]), j + n + 1
    return None


def _is_module_tok(t):
    return t in ("sabbesaṃ", "itaresaṃ", "pacchimabhavikānaṃ") or t in F.PART or bool(F._place_form(t))


def lead_units(who):
    """A person / moment / place lead -> list of (kind, Burmese): P person, M moment."""
    raw = [t.rstrip(",") for t in who.split()]
    toks, brs = [], {}                  # brs: index of the token before the bracket -> brackets
    for t in raw:
        if t.startswith("⟦"):
            if not toks:
                raise F.Miss("lead: bracket first")
            brs.setdefault(len(toks) - 1, []).append(t)
        else:
            t = t[0].lower() + t[1:]
            toks.append(SLIPS.get(t, t))
    units = _lead_units(toks)
    out = []
    for kind, txt, a, b in units:
        for k in range(a, b):
            for br in brs.get(k, []):
                txt += " " + br
        out.append((kind, txt))
    return out


SLIPS = {"asaññattā": "asaññasattā",            # ^6-5-76 «asaññattā cavantānaṃ» (slip)
         "paṭilabhissānti": "paṭilabhissanti"}  # ^6-5-74 «paṭilabhissānti» (slip)


def _lead_units(toks):
    """toks (no brackets) -> [(kind, Burmese, first token, end token)]; kind P person, M moment, L place."""
    units, i, prefix = [], 0, ""
    while i < len(toks):
        t = toks[i]
        mo = None if t == "avasese" else _moment_at(toks, i)
        if mo:
            units.append(("M", prefix + mo[0], i, mo[1]))
            prefix = ""
            i = mo[1]
            continue
        if t == "sabbesaṃ" and _moment_at(toks, i + 1):
            prefix = new("sabbesaṃ (before a moment)", f"{F.ALL_OF}၏ ")
            i += 1
            continue
        if t == "tesaṃ":                              # inner «tesaṃ» after a relative clause
            if i + 1 < len(toks) and toks[i + 1] in F.PART and units and units[-1][0] == "P" \
                    and units[-1][1].endswith(F.THEM[-len("တို့"):]):
                verb, cw = F.PART[toks[i + 1]]
                k0, t0, a0, b0 = units[-1]
                units[-1] = ("P", t0 + new("tesaṃ + participle (inner, after a relative)", "အနက် ") + verb + F.THEM,
                             a0, i + 2)
                i += 2
                continue
            if _moment_at(toks, i + 1):
                prefix = new("tesaṃ + moment (inner)", "ထိုသူတို့၏ ")
                i += 1
                continue
            raise F.Miss("lead: inner tesaṃ")
        hit = None
        for k in REL_RE:
            kt = k.split()
            if toks[i:i + len(kt)] == kt:
                hit = (REL[k], i + len(kt))
                break
        if hit:
            units.append(("P", hit[0], i, hit[1]))
            i = hit[1]
            continue
        if t in ATTR:                                 # attributes (+ participle)
            ats, i0 = [], i
            while i < len(toks) and toks[i] in ATTR:
                ats.append(ATTR[toks[i]])
                i += 1
            if i < len(toks) and toks[i] in F.PART:
                if all(a in SA_ATTR.values() for a in ats):
                    pre = " ".join(ats)
                else:
                    pre = f"{C} ".join(a + "သော" for a in ats)
                units.append(("P", pre + " " + F.PART[toks[i]][0] + F.THEM, i0, i + 1))
                i += 1
            else:
                if len(ats) != 1:
                    raise F.Miss("lead: attributes without participle")
                units.append(("P", ats[0] + F.THEM, i0, i))
            continue
        if t == "avasese":
            j, places = i + 1, []
            while j < len(toks) and F._place_form(toks[j]) and F._place_form(toks[j])[1] == "loc":
                places.append(F._place_form(toks[j])[0])
                j += 1
            units.append(("L", f"{AVASESE} " + F._join_places(places) + F.LOC, i, j))
            i = j
            continue
        if _is_module_tok(t):
            j = i
            while j < len(toks) and _is_module_tok(toks[j]) and not (j > i and _moment_at(toks, j)) \
                    and not (toks[j] == "sabbesaṃ" and _moment_at(toks, j + 1)):
                j += 1
            run = toks[i:j]
            if all(F._place_form(x) and F._place_form(x)[1] == "loc" for x in run):
                units.append(("L", F.place_my(" ".join(run)), i, j))
            else:
                k = i
                while run:
                    n = len(run)
                    txt = F._one_group(run)
                    units.append(("P", txt, k, k + n - len(run)))
                    k += n - len(run)
            i = j
            continue
        raise F.Miss("lead token: " + t + " in " + " ".join(toks))
    if prefix:
        raise F.Miss("lead: dangling prefix")
    return units

def join_lead(units):
    """Consecutive person units joined as the module joins person groups («A၊ Bနှင့် C»), the rest with «၊ »."""
    segs, run = [], []
    for kind, txt in units:
        if kind == "P":
            run.append(txt)
            continue
        if kind == "R":                     # «tesaṃ cavantānaṃ»: of the groups before, those passing away
            if not run:
                raise F.Miss("lead: inner tesaṃ without persons")
            segs.append(_join_p(run))
            run = []
            segs.append(txt)
            continue
        if run:
            segs.append(_join_p(run))
            run = []
        segs.append(txt)
    if run:
        segs.append(_join_p(run))
    return f"{C} ".join(segs)


def _join_p(parts):
    return parts[0] if len(parts) == 1 else f"{C} ".join(parts[:-1]) + f"{AND} " + parts[-1]


THEM_DAT = F.PRO["tesaṃ"]                      # «ထိုသူတို့အား» after a final moment


_who_module = F.who_my


def who_my(who, pro):
    """The module's who_my first (pure person runs / places, identical to the sample); else the lead parser."""
    try:
        return _who_module(who, pro)
    except F.Miss:
        pass
    units = lead_units(who)
    out = join_lead(units)
    mb = re.search(r"((?: ⟦\d+⟧)+)$", out)       # a variant at the end of the lead goes after «…အား» (as the sample)
    tail = mb[1] if mb else ""
    out = out[: len(out) - len(tail)]
    last = "P" if units[-1][0] == "R" else units[-1][0]
    if pro == "tattha":
        if any(k != "L" for k, _ in units):
            raise F.Miss("lead: tattha after persons")
        return out + tail
    if last == "P":
        out += DAT
    elif last == "M":
        out += " " + THEM_DAT
    else:
        raise F.Miss("lead: place before tesaṃ")
    return out + tail + (" " + F.FT["tattha"] if pro == "tesaṃ tattha" else "")


F.who_my = who_my
_pali_verb_module = F.pali_verb


def pali_verb(w):
    """the module's pali_verb; the slip «nirujjhiti» (^6-5-125, for nirujjhati) read as present."""
    w2 = re.sub(r"nirujjhiti$", "nirujjhati", w.strip())
    if w2 != w.strip():
        new("nirujjhiti (slip ^6-5-125)", "read as nirujjhati")
    return _pali_verb_module(w2)


F.pali_verb = pali_verb
F.SUBJ["vadanākkhandho"] = F.SUBJ["vedanākkhandho"]      # source slip ^6-2-185 «vadanākkhandho»

# --- «X-ñca V1 Y-ñca V2» (neuter subjects) and the slips without one «ca» / with a stray comma
VB = F.VB
A_BOTH2 = re.compile(rf"^(?P<who>.+?) (?P<pro>{F.PROR}) (?P<x>\S+?)(?P<c1>ñca| ca)? (?P<v1>{VB}),? (?P<y>\S+?)"
                     rf"(?P<c2>ñca| ca)? (?P<v2>{VB})\.$")


def subj_ca(x, c):
    return F.subj(x + "ṃ" if c == "ñca" else x)


def a_both2(s):
    m = A_BOTH2.match(s)
    if not m or not (m["c1"] or m["c2"]) or (m["c1"] and m["c2"] and m["c1"] == " ca" and m["c2"] == " ca"
                                             and "," not in s):
        return None
    X, Y = subj_ca(m["x"], m["c1"]), subj_ca(m["y"], m["c2"])
    also = "လည်း"
    return (f"{F.who_my(m['who'], m['pro'])} {X}{also if m['c1'] else ''} {F.V(m['v1'])}{C} "
            f"{Y}{also if m['c2'] else ''} {F.V(m['v2'])}{END}")


# ===================================================================================== paṇṇatti frames (extension)
AV_N = {"avaseso": (F.AVASESA + " " + F.THING, False), "avasesaṃ": (F.AVASESA + " " + F.THING, False),
        "avasesā": (F.AVASESA_N, True)}
new("avaseso / avasesaṃ (bare, singular)", AV_N["avaseso"][0])
AVR = r"(?P<av>avaseso|avasesaṃ|avasesā)"
SPR = "(?P<s>" + "|".join(re.escape(k) for k in SPECIAL) + ")"
V_ = r"(?P<v> ⟦\d+⟧)?"
X1 = re.compile(rf"^{SPR} (?P<a>\S+), na (?P<b>\S+)\.$")                       # special A, na B.
X4 = re.compile(rf"^{SPR} na (?P<b>\S+), (?P<a>\S+)\.$")                       # special na B, A.
X2 = re.compile(rf"^{SPR} (?P<a>\S+?)(?P<ce>ñceva| ceva) (?P<b>\S+?ñca|\S+ ca)\.$")   # special Añceva Bñca.
XS = re.compile(rf"^{SPR} ṭhapetvā {AVR} (?P<a>[^\s,⟦]+){V_},? na (?P<b>\S+)\.$")   # special ṭhapetvā avasesaṃ A, na B.
XSN = re.compile(rf"^{SPR} ṭhapetvā {AVR} na (?P<b>[^\s,⟦]+){V_},? (?P<a>\S+)\.$")
TK = r"[^\s,⟦]+"                                  # one Pāli word (no comma, no variant placeholder)
Y1 = re.compile(rf"^(?P<s>\S+) ṭhapetvā {AVR} (?:(?P<k>{TK}) )?(?P<a>{TK}){V_}, na (?P<b>\S+)\.$")   # S ṭh. av. [K] A, na B.
Y1B = re.compile(rf"^(?P<s>\S+) ṭhapetvā {AVR}{V_} (?P<a>\S+), na (?P<b>\S+)\.$")
Y4 = re.compile(rf"^(?P<s>\S+) ṭhapetvā {AVR}{V_} (?:(?P<k>{TK}) )?na (?P<b>{TK})(?:, (?P<a>\S+))?\.$")  # … na B, A.
Y5 = re.compile(rf"^(?P<a>\S+?ñca|\S+ ca) (?P<b>\S+?ñca|\S+ ca) ṭhapetvā {AVR}{V_} na ceva (?P<a2>\S+) "
                rf"na ca (?P<b2>\S+)\.$")
Y3 = re.compile(rf"^Avasesā (?P<a>[^\s,⟦]+){V_} na (?P<b>\S+)\.$")
Y2 = re.compile(r"^(?P<x>\S+) (?P<a>\S+?)(?P<ce>ñceva| ceva) (?P<b>\S+?ñca|\S+ ca)\.$")


def T(w):
    if w.endswith("ūti"):
        w = w[:-3] + "u"
    return F.term(w)


def av_subj(av, k=None):
    if k:
        return f"{F.AVASESA} {T(k)[0]}", T(k)[1]
    return AV_N[av]


def pannatti2(s):
    m = X1.match(s) or X4.match(s)
    if m:
        S, pl = SPECIAL[m["s"]]
        A = SOTA_WORD if (m["s"].startswith("Dibbasot") and m["a"] == "sotaṃ") else T(m["a"])[0]
        B = T(m["b"])[0]
        if m.re is X1:
            return f"{S}သည် {F.is_(A, pl)}{C} {F.isnt(B, pl)}{END}"
        return f"{S}သည် {F.isnt(B, pl)}{C} {F.is_(A, pl)}{END}"
    m = X2.match(s)
    if m:
        S, pl = SPECIAL[m["s"]]
        A, B = T(m["a"] + ("ñceva" if m["ce"] == "ñceva" else ""))[0], T(m["b"])[0]
        return f"{S}သည် {A}လည်း {F.BE}{C} {B}လည်း {F.BE}{'ကြ' if pl else ''}သည်{END}"
    m = XS.match(s) or XSN.match(s)
    if m:
        S, _ = SPECIAL[m["s"]]
        sub, pl = AV_N[m["av"]]
        A, B = T(m["a"])[0], T(m["b"])[0]
        lv = f"{S[:-len('တို့')] if S.endswith('တို့') else S}ကို {F.THAPETVA}{C}"
        if m.re is XS:
            return f"{lv} {sub}သည်{m['v'] or ''} {F.is_(A, pl)}{C} {F.isnt(B, pl)}{END}"
        return f"{lv} {sub}သည် {F.isnt(B, pl)}{m['v'] or ''}{C} {F.is_(A, pl)}{END}"
    m = Y1.match(s)
    if m and not s.startswith(tuple(SPECIAL)):
        S, A, B = T(m["s"]), T(m["a"]), T(m["b"])
        sub, pl = av_subj(m["av"], m["k"])
        return f"{F.leave(S)} {sub}သည် {A[0]}{m['v'] or ''} {F.BE}{'ကြ' if pl else ''}သည်{C} {F.isnt(B[0], pl)}{END}"
    m = Y1B.match(s)
    if m and not s.startswith(tuple(SPECIAL)):
        S, A, B = T(m["s"]), T(m["a"]), T(m["b"])
        sub, pl = av_subj(m["av"])
        return f"{F.leave(S)} {sub}သည်{m['v'] or ''} {F.is_(A[0], pl)}{C} {F.isnt(B[0], pl)}{END}"
    m = Y4.match(s)
    if m and not s.startswith(tuple(SPECIAL)):
        S, B = T(m["s"]), T(m["b"])
        sub, pl = av_subj(m["av"], m["k"])
        tail = f"{C} {F.is_(T(m['a'])[0], pl)}" if m["a"] else ""
        return f"{F.leave(S)} {sub}သည်{m['v'] or ''} {F.isnt(B[0], pl)}{tail}{END}"
    m = Y5.match(s)
    if m:
        A, B, A2, B2 = (T(m[k]) for k in ("a", "b", "a2", "b2"))
        sub, pl = AV_N[m["av"]]
        return (f"{F.leave(A, B)} {sub}သည်{m['v'] or ''} {A2[0]}လည်း {F.NEGV[F.BE]}{C} {B2[0]}လည်း "
                f"{F.NEGV[F.BE]}{END}")
    m = Y3.match(s)
    if m:
        A, B = T(m["a"]), T(m["b"])
        return f"{F.AVASESA} {A[0]}သည်{m['v'] or ''} {F.isnt(B[0], A[1])}{END}"
    m = Y2.match(s)
    if m:
        X, B = T(m["x"]), T(m["b"])
        A = T(m["a"] + ("ñceva" if m["ce"] == "ñceva" else ""))
        return f"{X[0]}သည် {A[0]}လည်း {F.BE}{C} {B[0]}လည်း {F.BE}{F.ko(X)}သည်{END}"
    m = F.P_Q.match(s[0].lower() + s[1:])
    if m and bool(m["n1"]) == bool(m["n2"]):
        try:
            A, B = T(m["a"]), T(m["b"])
        except F.Miss:
            return None
        if m["n1"]:
            return f"{A[0]} {F.NEGV[F.BE]}သော {F.THING}သည် {B[0]} {F.NEGV[F.BE]}သလော{END}"
        return f"{A[0]}သည် {B[0]} {F.BE}{F.ko(A)}သလော{END}"
    return None


# ===================================================================================== editorial notes and lines
YASSAKA = new("yassaka", f"“{F.CL['yassa'][0]}” အပိုင်း")           # as the ch. 3 agent
YATTHAKA = new("yatthaka", f"“{F.CL['yattha'][0]}” အပိုင်း")
YY = new("yassayatthaka", f"“{F.CL['yassa yattha'][0]}” အပိုင်း")
SAME = new("sadisaṃ / sadisā", "တူညီသည်")
NODIFF = new("natthi nānākaraṇaṃ", "ကွဲပြားချက် မရှိ")
VITTH = new("vitthāretabbaṃ / vitthāretabbā", "အကျယ် ချဲ့ရမည်")
VIBH = new("vibhajitabbaṃ / vibhajitabbā", "ခွဲခြား ပြရမည်")                # as the ch. 3 agent (pi-2)
VIBHATTA = new("vibhattaṃ / vibhattā (as … is analysed)", "ခွဲခြား ပြထားသကဲ့သို့")
CAKKA_B = new("cakkaṃ bandhitabbaṃ", f"{F.CAKKA}ကို အပြည့်အစုံ ဖွဲ့ရမည်")   # as the ch. 3 agent
AYAT = F.quoted(F.H["Āyatanayamakaṃ"])
DHAT = F.quoted(F.H["Dhātuyamakaṃ"])
ANU_PAC = f"{F.ANULOMA}လည်း၊ {F.PACCANIKA}လည်း"
PUCCHA = W("5", "^5-652", "pucchā", "အမေး", key="pucchā")
ASAMMOHA = new("asammohantena", "မရောထွေးစေဘဲ")
UPP, NIR = F.UPPADA, F.NIRODHA
UN = f"{UPP}{AND} {NIR}"
EDIT = {   # editorial notes / unique lines (Pāli with brackets as ⟦v⟧) -> Burmese ({v} = the variant)
    "(yatthakaṃ paripuṇṇaṃ kātabbaṃ)": f"({YATTHAKA}ကို ပြည့်စုံအောင် ပြုရမည်)",
    "(Yathā uppādavāre paccuppannātītaṃ vibhattaṃ tathā idha vibhajitabbaṃ).":
        f"({F.vara(UPP)}၌ {F.TIMES['Paccuppanna']}{AND} {F.TIMES['Atīta']}ကို {VIBHATTA} ဤနေရာ၌လည်း {VIBH})။",
    "(Yathā āyatanayamake cakkaṃ bandhitaṃ evamidha cakkaṃ bandhitabbaṃ.)":
        f"({AYAT}၌ {F.CAKKA}ကို ဖွဲ့ထားသကဲ့သို့ ဤနေရာ၌လည်း {CAKKA_B}။)",
    "(Cakkaṃ bandhitabbaṃ).": f"({CAKKA_B})။",
    "(Jivhāpi ghānadhātusadisā).": f"(လျှာလည်း {DH['ghānadhātu']}နှင့် {SAME})။",
    "(Saddo ghānasadiso).": f"(အသံသည် နှာခေါင်းနှင့် {SAME})။",
    "(Phoṭṭhabbo ghānasadiso).": f"(အထိအတွေ့သည် နှာခေါင်းနှင့် {SAME})။",
    "(saṃkhittaṃ⟦v⟧, ubhato āmantā).": new("(saṃkhittaṃ, ubhato āmantā)",
                                            "(အကျဉ်း ဖော်ပြထားသည်{v}၊ နှစ်ဖက်စလုံး “ဟုတ်ပါသည်”)။"),
    "(Yathā āyatanayamake paṇṇatti evaṃ dhātuyamakepi paṇṇatti.":
        f"({AYAT}၌ {F.PANNATTI} ရှိသကဲ့သို့ {DHAT}၌လည်း {F.PANNATTI} ရှိသည်။",
    "Cakkaṃ bandhitabbaṃ).": f"{CAKKA_B})။",
    "(Cakkaṃ bandhitabbaṃ, sabbe āmantā ubhatopi sesepi).":
        f"({CAKKA_B}၊ နှစ်ဖက်စလုံး၌လည်း၊ ကြွင်းကျန်သည်တို့၌လည်း အားလုံး “ဟုတ်ပါသည်”)။",
    "(Yathā āyatanayamakassa paṇṇatti evaṃ dhātuyamakassa paṇṇatti vitthāretabbā)":
        f"({AYAT}၏ {F.PANNATTI}ကဲ့သို့ {DHAT}၏ {F.PANNATTI}ကို {VITTH})",
    "(Yathā āyatanayamakaṃ vibhattaṃ evaṃ dhātuyamakampi vibhajitabbaṃ, sadisaṃ kātabbaṃ).":
        f"({AYAT}ကို {VIBHATTA} {DHAT}ကိုလည်း {VIBH}၊ တူညီအောင် ပြုရမည်)။",
    "(dhātuyamakaṃ paripuṇṇaṃ peyyālena).": f"({DHAT}ကို အကျဉ်းချုံ့၍ ပြည့်စုံအောင် ပြုထားသည်)။",
    "(Yassakampi yassayatthakampi sadisaṃ vitthāretabbaṃ).": f"({YASSAKA}လည်း၊ {YY}လည်း {SAME}၊ {VITTH})။",
    "(Yassakampi yassayatthakampi sadisaṃ).": f"({YASSAKA}လည်း၊ {YY}လည်း {SAME})။",
    "(Yassayatthakampi sadisaṃ vitthāretabbaṃ).": f"({YY}လည်း {SAME}၊ {VITTH})။",
    "(Yatthakampi sabbattha sadisaṃ.": f"({YATTHAKA}လည်း နေရာတိုင်း၌ {SAME}။",
    "Tantinānākaraṇaṃ heṭṭhā yatthakasadisaṃ).":
        new("Tantinānākaraṇaṃ heṭṭhā yatthakasadisaṃ", f"စာကိုယ် ကွဲပြားချက်သည် ရှေ့၌ ရှိသော {YATTHAKA}နှင့် {SAME})။"),
    "(yatthakampi yassayatthakasadisaṃ kātabbaṃ)": f"({YATTHAKA}ကိုလည်း {YY}နှင့် တူညီအောင် ပြုရမည်)",
    "(yatthakā sadisā sabbe)": f"({YATTHAKA}များ အားလုံး {SAME})",
    "(Yatthakaṃ uppādepi nirodhepi uppādanirodhepi sadisaṃ, natthi nānākaraṇaṃ).":
        f"({YATTHAKA}သည် {UPP}၌လည်း၊ {NIR}၌လည်း၊ {UN}၌လည်း {SAME}၊ {NODIFF})။",
    "(Yatthakaṃ uppādavārepi nirodhavārepi uppādanirodhavārepi sadisaṃ natthi nānākaraṇaṃ).":
        f"({YATTHAKA}သည် {F.vara(UPP)}၌လည်း၊ {F.vara(NIR)}၌လည်း၊ {F.vara(UN)}၌လည်း {SAME}၊ {NODIFF})။",
    "(Yassakampi⟦v⟧ yassayatthakampi sadisaṃ, yassayatthakepi nirodhasamāpannānanti cetaṃ na kātabbaṃ).":
        f"({YASSAKA}လည်း{{v}}၊ {YY}လည်း {SAME}၊ {YY}၌လည်း “{REL['nirodhasamāpannānaṃ']}အား”ဟူသော "
        f"ဤစကားကို မပြုရ)။",
    "(Yassakampi yassayatthakampi sadisaṃ, yassayatthakepi nirodhasamāpannānanti na kātabbaṃ).":
        f"({YASSAKA}လည်း၊ {YY}လည်း {SAME}၊ {YY}၌လည်း “{REL['nirodhasamāpannānaṃ']}အား”ဟု မပြုရ)။",
    "(Yathā uppādavāre atītā pucchā anulomampi paccanīkampi vibhattā evaṃ nirodhepi vibhajitabbā, natthi "
    "nānākaraṇaṃ).":
        f"({F.vara(UPP)}၌ {F.TIMES['Atīta']} {PUCCHA}ကို {ANU_PAC} {VIBHATTA} {NIR}၌လည်း {VIBH}၊ {NODIFF})။",
    "(Atītā pucchā yathā uppādavāre vibhattā evaṃ uppādanirodhavārepi anulomampi paccanīkampi vibhajitabbaṃ).":
        f"({F.TIMES['Atīta']} {PUCCHA}ကို {F.vara(UPP)}၌ {VIBHATTA} {F.vara(UN)}၌လည်း {ANU_PAC} {VIBH})။",
    "(Paccuppannaatītā⟦v⟧ pucchā uppādavārepi uppādanirodhavārepi yassakampi yatthakampi yassayatthakampi "
    "anulomampi paccanīkampi sadisaṃ, asammohantena vibhajitabbā).":
        f"({F.TIMES['Paccuppanna']}{AND} {F.TIMES['Atīta']}{{v}} {PUCCHA}သည် {F.vara(UPP)}၌လည်း၊ {F.vara(UN)}၌လည်း၊ "
        f"{YASSAKA}၊ {YATTHAKA}၊ {YY}၌လည်း၊ {ANU_PAC} {SAME}၊ {ASAMMOHA} {VIBH})။",
    "(Yathā nirodhavāre atītānāgatā⟦v⟧ pucchā anulomampi paccanīkampi vibhattā evaṃ uppādanirodhavārepi "
    "asammohantena vibhajitabbaṃ).":
        f"({F.vara(NIR)}၌ {F.TIMES['Atīta']}{AND} {F.TIMES['Anāgata']}{{v}} {PUCCHA}ကို {ANU_PAC} {VIBHATTA} "
        f"{F.vara(UN)}၌လည်း {ASAMMOHA} {VIBH})။",
}
# (^6-5-427) the note with a whole answer inside: «(Yassakampi …, samudayasaccaṃ maggasaccaṃ nānākaraṇaṃ,
#  aggamaggassa bhaṅgakkhaṇe, arahantānaṃ asaññasattānaṃ tesaṃ tattha maggasaccañca na nirujjhissati
#  samudayasaccañca nuppajjissati).» is built below (edit_427) from the frames.
VAR_NOTES = {   # trailing notes inside variant brackets
    "aññehi yamakehi saṃsanditabbaṃ": new("aññehi yamakehi saṃsanditabbaṃ",
                                         "အခြား အတွဲလိုက် မေးဖြေခြင်းများနှင့် တိုက်ဆိုင် စစ်ဆေးရမည်"),
    "evaṃ avasesesu tīsu saccesu": new("evaṃ avasesesu tīsu saccesu",
                                       f"{F.AVASESA} {SACCA} သုံးပါးတို့၌လည်း ဤနည်းတူ"),
    "evaṃ puggalokāsepi nirodhavārepi": new("evaṃ puggalokāsepi nirodhavārepi",
                                            f"{PUGGALA}{AND} {F.OKASA}အလိုက်၌လည်း၊ {F.vara(NIR)}၌လည်း ဤနည်းတူ"),
    "puggalokāsavārepi": new("puggalokāsavārepi", f"{F.vara(PUGGALA + AND + ' ' + F.OKASA)}၌လည်း"),
    "uppādavāre pana pāṭhantaraṃ natthi": new("uppādavāre pana pāṭhantaraṃ natthi",
                                              f"{F.vara(UPP)}၌ကား ပါဌ်ကွဲ မရှိ"),
}
_variant_module = F.variant


def variant(inner):
    for k, v in VAR_NOTES.items():
        if inner.endswith(" " + k):
            out = _variant_module(inner[: -len(k) - 1])
            return out[:-1] + f"{C} {v}]"
    return _variant_module(inner)


F.variant = variant
F.SPELLING.update({"dhātu (sī. ka.)", "uppatticittassa (syā.)"})     # vowel length / spelling only
HEADS = {
    "Uppādanirodhavāro": F.vara(UN),
    "Pariññāvāro": new("Pariññāvāro", F.vara(W("5", "^5-317", "parijānaṃ", "ပိုင်းခြား သိ") + "ခြင်း")),
    "Pavatti 3. uppādanirodhavāro": f"{F.PAVATTI} 3. {F.vara(UN)}",
    "Suddhadhātuvāro": F.vara(f"{F.SUDDHA} {DHATU}", False),
    "Suddhadhātumūlacakkavāro": F.vara(f"{F.SUDDHA} {DHATU}{F.BASED} {F.CAKKA}", False),
    "Suddhasaccavāro": F.vara(f"{F.SUDDHA} {SACCA}", False),
    "Suddhasaccamūlacakkavāro": F.vara(f"{F.SUDDHA} {SACCA}{F.BASED} {F.CAKKA}", False),
    "Paṇṇattivāra": F.H["Paṇṇattivāro"],
}
for k, v in HEADS.items():
    if k in F.H and F.H[k] != v:
        raise SystemExit("heading clash " + k)
    F.H[k] = new(k + " (heading)", v)
COLO_NEW = {
    "Nirodhavāro.": F.vara(NIR) + END,
    "Uppādanirodhavāro.": F.vara(UN) + END,
    "Uppādanirodhavāro": F.vara(UN),
    "Pavattivāro niṭṭhito.": F.finished(F.vara(F.PAVATTI)),
    "Pariññāvāro.": HEADS["Pariññāvāro"] + END,
    "Uppādavāro.": F.vara(UPP) + END,
}
for k, v in COLO_NEW.items():
    F.COLO.setdefault(k, new(k + " (colophon)", v))
F.LINES["Aṭṭhārasa dhātuyo – " + ", ".join(DH_ORDER) + "."] = new(
    "Aṭṭhārasa dhātuyo – … (Yamaka order)", f"{DH_HEAD} – " + f"{C} ".join(DH[k] for k in DH_ORDER) + END)
F.LINES["Cattāri saccāni – dukkhasaccaṃ, samudayasaccaṃ nirodhasaccaṃ, maggasaccaṃ."] = new(
    "Cattāri saccāni – … (comma missing in the source)", f"{SACCA_H} – " + f"{C} ".join(SACCAS.values()) + END)


# ===================================================================================== fragments between «…»
FR_Q_PAV = re.compile(rf"^{F.CLR}(?: (?P<x>\S+) (?P<v1>{VB}))?$")
FR_ANS = re.compile(rf"^(?P<who>.+?) (?P<pro>{F.PROR}) (?P<x>\S+) (?P<v>{VB})$")
FR_VB = re.compile(rf"^(?P<v>{VB})$")


def fragment(p):
    """A piece (or sentence) between «…» that no frame takes -> Burmese. With «?» it ends «…လော။» / «…သလော။»,
    with «.» «။», without a stop it has none."""
    q, st = p.endswith("?"), p.endswith(".")
    t = p[:-1] if (q or st) else p
    endq = "လော" + END if q else (END if st else "")
    m = FR_VB.match(t)
    if m and q:
        return F.V(m["v"], "q") + END
    m = FR_Q_PAV.match(t)
    if m:
        c = m["cl"].lower()
        pre = F.VA_PANA + " " if " vā pana" in c else ""
        c = c.replace(" vā pana", "")
        return f"{pre}{F.CL[c][0]}" + (f" {F.subj(m['x'])} {F.V(m['v1'], 'cl')}" if m["x"] else "") + endq
    m = re.fullmatch(rf"(?P<who>.+?) (?P<pro>{F.PROR})(?: (?P<x>\S+))?", t)
    if m and not q and (not m["x"] or m["x"] in F.SUBJ):          # «… tesaṃ tattha [X]»
        return F.who_my(m["who"], m["pro"]) + (f" {F.subj(m['x'])}" if m["x"] else "") + (END if st else "")
    if t.lower() in ("yo vā pana", "yo"):
        return (F.VA_PANA + " " if "vā pana" in t else "") + YO[0] + endq
    m = FR_ANS.match(t)
    if m and not q:
        return f"{F.who_my(m['who'], m['pro'])} {F.subj(m['x'])} {F.V(m['v'])}" + (END if st else "")
    m = re.fullmatch(r"(?P<a>\S+) ṭhapetvā", t)
    if m:
        return F.leave(T(m["a"]))[:-1] + (END if st else "")
    m = re.fullmatch(r"(?P<n>[Nn]a )?(?P<a>\S+)", t)
    if m:
        A = T(m["a"])[0]
        return (f"{A} {F.NEGV[F.BE]}သော {F.THING}" if m["n"] else A) + endq
    m = F.P_Q.match(t[0].lower() + t[1:] + "?")
    if m and bool(m["n1"]) == bool(m["n2"]):     # an abbreviated question (with or without «?»)
        r = pannatti2(t + "?")
        return r if q else r[:-1]
    raise F.Miss("fragment: " + p)


def piece_my(p):
    """One piece between «…»: sentences, the last may lack its stop (then no «။»); what no frame takes is a
    fragment."""
    p0 = p.strip()
    if not p0:
        return ""
    if p0 in (".", "?"):
        return END if p0 == "." else "လော" + END
    lead = ""
    if p0.startswith("? "):                    # «…pe…? Āmantā.»: the question closes after «…»
        lead, p0 = "လော" + END + " ", p0[2:]
    elif p0.startswith(". "):                  # «…pe…. Saccā …»: the stop after «…», then a new sentence
        lead, p0 = END + " ", p0[2:]
    for ek0, tail in ((p0, ""), (p0[:-1], END) if p0.endswith(").") else (None, None)):
        if ek0 is None:
            continue
        ek = re.sub(r" ?(⟦\d+⟧)", "⟦v⟧", ek0)
        if ek in EDIT:
            br = re.search(r" ?(⟦\d+⟧)", ek0)
            return lead + (EDIT[ek].format(v=" " + br[1]) if br else EDIT[ek]) + tail
    sents = F.SPLIT.split(p0)
    out = []
    for k, s in enumerate(sents):
        if s in EDIT:
            out.append(EDIT[s])
            continue
        last = k == len(sents) - 1
        open_ = last and not s.endswith((".", "?", ")"))
        try:
            r = sentence_my(s + "." if open_ else s)
            if open_:
                r = r[:-1]
        except F.Miss:
            r = fragment(s)
        out.append(r)
    return lead + " ".join(out)


def pe_line(line):
    s = line.replace("…pe…", PE).replace("…Pe…", PE)
    out = []
    for p in s.split(PE):
        q = piece_my(p)
        out.append((" " if p.startswith(" ") and q and not q.startswith(("လော", END)) else "") + q)
    return PE.join(out)


# ===================================================================================== engine
_body_module = F.body_my
FRAMES_MINE = [pariñña_sentence, a_both2, pannatti2]


NOTE_END = re.compile(r"^(?P<a>.+?) (?P<n>\([^)]*\))\.$")


def sentence_my(s):
    if s in EDIT:
        return EDIT[s]
    m = NOTE_END.match(s)
    if m and m["n"] in EDIT:                      # «Yattha X V (note).»: a fragment and the note
        return f"{fragment(m['a'])} {EDIT[m['n']]}{END}"
    r = F.pavatti_sentence(s)
    if r:
        return r
    for fn in FRAMES_MINE:
        r = fn(s)
        if r:
            return r
    r = F.pannatti_sentence(s)
    if r:
        return r
    raise F.Miss("no frame for: " + s)


def edit_427(s):
    m = re.fullmatch(r"\(Yassakampi yassayatthakampi sadisaṃ, samudayasaccaṃ maggasaccaṃ nānākaraṇaṃ, (?P<a>.+)\)\.", s)
    if not m:
        return None
    ans = sentence_my(m["a"].replace("aggamaggassa bhaṅgakkhaṇe, ", "Aggamaggassa bhaṅgakkhaṇe ") + ".")
    return (new("(Yassakampi yassayatthakampi sadisaṃ, samudayasaccaṃ maggasaccaṃ nānākaraṇaṃ, …)",
                f"({YASSAKA}လည်း၊ {YY}လည်း {SAME}၊ {SACCAS['samudayasaccaṃ']}{AND} {SACCAS['maggasaccaṃ']} "
                f"ကွဲပြားချက်ကား ") + ans[:-1] + ")။")


def body_my(line):
    """A line without block ID, heading mark or label -> Burmese (pe lines through pe_line)."""
    if line in F.COLO:
        return F.COLO[line]
    vars_ = []

    def keep(m):
        vars_.append(variant(m[1]))
        return f" ⟦{len(vars_) - 1}⟧"
    if line in F.LINES:
        return F.LINES[line]
    key = F.BRACKET.sub("⟦v⟧", line)
    k2 = re.sub(r" ⟦v⟧", "⟦v⟧", key)
    for kk in (key, k2):
        if kk in EDIT:
            br = F.BRACKET.search(line)
            return EDIT[kk].format(v=" " + variant(br[1])) if br else EDIT[kk]
    line = F.BRACKET.sub(keep, line)
    if "…" in line:
        out = pe_line(line)
    else:
        e = edit_427(line)
        out = e if e else " ".join(sentence_my(s) for s in F.SPLIT.split(line))
    for i, v in enumerate(vars_):
        out = out.replace(f"⟦{i}⟧", v)
    return out


F.body_my = body_my


_sentence_frames = sentence_my


def sentence_my(s):                     # noqa: F811  (the frames, then the variant-placeholder fallback)
    """inside «…» pieces too: a placeholder the frames do not take goes after the Burmese of the word before it."""
    try:
        return _sentence_frames(s)
    except F.Miss:
        if "⟦" not in s:
            raise
        return _sent_fallback(s, _sentence_frames)


def _sent_fallback(s, inner):
    m = re.search(r" (⟦\d+⟧)", s)
    s2 = s[: m.start()] + s[m.end():]
    r = inner(s2)
    prev = s[: m.start()].split()[-1]
    my = T(prev)[0]
    k = r.find(my)
    if k < 0 or r.count(my) != 1:
        raise F.Miss("bracket placement: " + s)
    k += len(my)
    for part in ("သည်", "ကို"):
        if r.startswith(part, k):
            k += len(part)
    return r[:k] + " " + m[1] + r[k:]


# ===================================================================================== per-line check, run
def num(l):
    m = re.match(r"\((\d+)\)", l)
    return m[1] if m else None


def line_check(p, m):
    e = []
    for mark in ("–", "—"):
        if p.count(mark) != m.count(mark):
            e.append(f"dash {mark}")
    if p.replace("…pe…", "…").replace("…Pe…", "…").count("…") != m.count("…"):
        e.append("ellipsis")
    if p.count("[") != m.count("[") or p.count("]") != m.count("]"):
        e.append("brackets")
    if num(p) != num(m):
        e.append("item number")
    lp, lm = F.LABEL_RE.match(p), re.match(r"^\(([က-အ])\) ", m)
    if bool(lp) != bool(lm) or (lp and F.AKKHARA[lp[1]] != lm[1]):
        e.append("label")
    ip, im = F.ID_RE.search(p), F.ID_RE.search(m)
    if bool(ip) != bool(im) or (ip and ip[1] != im[1]):
        e.append("block ID")
    hp, hm = re.match(r"^(#+) ", p), re.match(r"^(#+) ", m)
    if (hp and hp[1]) != (hm and hm[1]):
        e.append("heading level")
    for bad in ("?", "।", ":-"):
        if bad in m:
            e.append(f"«{bad}»")
    if re.search(r"[A-Za-zāīūṃṅñṭḍṇḷ]", re.sub(r"\[[^\]]*\]", "", F.strip_id(m))):
        e.append("Latin letters")
    if not hm and not F.strip_id(m).rstrip().endswith(("။", "…", ")")) and F.strip_id(p).rstrip()[-1:] in ".?":
        e.append("no final «။»")
    return e


def run(name):
    src = (PALI / name).read_text(encoding="utf-8-sig")
    out = F.translate_text(src)
    nbad = 0
    P = [l for l in src.splitlines() if l.strip()]
    M = [l for l in out.splitlines() if l.strip()]
    if len(P) != len(M):
        print(f"{name}: {len(P)} vs {len(M)} lines")
        nbad += 1
    for i, (p, m) in enumerate(zip(P, M), 1):
        e = line_check(p, m)
        if e:
            nbad += 1
            print(f"{name}:{i} {e}\n  {p}\n  {m}")
    return out, nbad


def misses(name):
    n = 0
    for i, l in enumerate((PALI / name).read_text(encoding="utf-8-sig").splitlines(), 1):
        try:
            F.translate_line(l)
        except F.Miss as ex:
            n += 1
            print(f"{name}:{i} {ex}")
    return n


def who_list(names):
    """--who: every distinct lead (before «tesaṃ» / «tattha») of the answers, with counts."""
    import collections
    c = collections.Counter()
    for n in names:
        for l in (PALI / n).read_text(encoding="utf-8-sig").splitlines():
            for s in F.SPLIT.split(re.sub(r" ?\[[^\]]*\]", "", F.strip_id(l))):
                m = re.match(r"^(.+?) (tesaṃ tattha|tesaṃ|tattha) \S+ (?:ca )?" + VB, s)
                if m and not re.match(r"^\(\w+\) ", s) and not s.lower().startswith(("yassa", "yattha")):
                    c[m[1]] += 1
    for k, v in sorted(c.items()):
        print(v, k)


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    names = args or NAMES_OUT
    if "--who" in sys.argv:
        who_list(names)
        sys.exit(0)
    if "--misses" in sys.argv:
        print("misses:", sum(misses(n) for n in names))
        sys.exit(0)
    OUT.mkdir(parents=True, exist_ok=True)
    for n in names:
        if n not in NAMES_OUT:
            sys.exit(f"{n}: not one of this agent's chapters")
        text, nbad = run(n)
        if nbad:
            sys.exit(f"{n}: {nbad} bad lines, nothing written")
        (OUT / n).write_text(text, encoding="utf-8")
        print(f"{n}: written, {len([l for l in text.splitlines() if l.strip()])} lines")
