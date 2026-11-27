"""Burmese zero-shot of pi-2 (Vibhaṅga, «ခွဲခြမ်းစိတ်ဖြာခြင်း»), chapter 18-dhammahadayavibhango.

usage: python3 -I -X utf8 make_ch18.py
Every line is generated from the Pāli by the frames below, from the tables of my2_formulas.py (imported read-only;
it loads the FINAL pi-1 Burmese module) plus this chapter's own tables (logged in notes-ch18.md). A sentence that
no frame matches stops the run (F.Miss); nothing is guessed. The chapter file is written only when every line
passed; on a stop the lines that passed go to scratch/partial-<chapter>. Sentences identical to pi-1 Pāli take the
pi-1 final Burmese (rails text) from the aligned pi-1 files (P1SENT); four near-identical pi-1 definitions are
derived from their pi-1 lines (variant brackets removed, the full aggregate list put in).
Never edits my2_formulas.py, my2-zeroshot-terms.md or anything in pi-1-my/.
"""
import pathlib
import re
import sys
import unicodedata

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import my2_formulas as F  # noqa: E402

ROOT = HERE.parents[3]
PALI = ROOT / "AI_translation/pali/pi-2_split_chapters"
OUT = ROOT / "AI_translation/burmese/pi-2-burmese-plain-zeroshot_split_chapters"
NAME = "18-dhammahadayavibhango.md"
Miss = F.Miss
P1 = F.P1
T = F.T
C, END, PE = F.C, F.END, F.PE
DH, DHP = F.DH, F.DHP
SIYA, NVATT, TIPI = F.SIYA, F.NVATT, F.TIPI
KATI, KATI_END = F.KATI, F.KATI_END
CL = P1.CL                                      # ပါး


def cop(pl):
    return "ဖြစ်ကြသည်" if pl else "ဖြစ်သည်"


def dh(pl):
    return DHP if pl else DH


def low(s):
    return s[0].lower() + s[1:] if s else s


# ===================================================================================== numbers
UNIT = {1: "တစ်", 2: "နှစ်", 3: "သုံး", 4: "လေး", 5: "ငါး", 6: "ခြောက်", 7: "ခုနစ်", 8: "ရှစ်", 9: "ကိုး"}


def num_my(n):
    """Integer -> Burmese number word (one token, no spaces)."""
    if n < 10:
        return UNIT[n]
    if n < 100:
        t, u = divmod(n, 10)
        tens = "ဆယ်" if t == 1 else UNIT[t] + "ဆယ်"
        return tens if not u else tens[:-1] + "့်" + UNIT[u]       # ဆယ် -> ဆယ့် before a unit
    for base, word in ((10000, "သောင်း"), (1000, "ထောင်"), (100, "ရာ")):
        if n >= base:
            q, r = divmod(n, base)
            head = UNIT[q] + word
            if not r:
                return head
            if word == "ထောင်":
                head = head[:-1] + "့်"                                   # ထောင် -> ထောင့်
            elif word == "ရာ":
                head = head + "့"
            return head + num_my(r)
    raise Miss(f"number {n}")


assert num_my(12) == "ဆယ့်နှစ်" and num_my(22) == "နှစ်ဆယ့်နှစ်" and num_my(10) == "ဆယ်"
assert num_my(1200) == "တစ်ထောင့်နှစ်ရာ" and num_my(16000) == "တစ်သောင်းခြောက်ထောင်"

# Pāli number words (free forms and compound stems)
NUMW = {"eko": 1, "ekā": 1, "ekaṃ": 1, "dve": 2, "tayo": 3, "tīṇi": 3, "tisso": 3, "cattāro": 4, "cattāri": 4,
        "catasso": 4, "pañca": 5, "cha": 6, "satta": 7, "aṭṭha": 8, "nava": 9, "dasa": 10, "ekādasa": 11,
        "dvādasa": 12, "terasa": 13, "cuddasa": 14, "pannarasa": 15, "soḷasa": 16, "aṭṭhārasa": 18}
NUMGEN = {"pañcannaṃ": 5, "sattannaṃ": 7, "dvādasannaṃ": 12, "aṭṭhārasannaṃ": 18, "catunnaṃ": 4}
NUMSTEM = {"ek": 1, "dv": 2, "tīṇ": 3, "cattār": 4, "pañc": 5, "satt": 7, "aṭṭh": 8, "nav": 9, "das": 10,
           "ekādas": 11, "dvādas": 12, "teras": 13, "cuddas": 14, "bāvīsat": 22}

# ===================================================================================== nouns
KH_N = P1.KHANDHA                               # အစုအဝေး
AYA_N = "အာရုံခံ နယ်ပယ်"
DHA_N = "ဓာတ်"
SAC_N = "သစ္စာ"                                  # saccaṃ (pi-1 termbase)
IND_N = P1.INDRIYA                              # စွမ်းရည်
HET_N = P1.ROOT                                 # အမြစ်
AHA_N = P1.AHARA                                # အာဟာရ
PHA_N = P1.PHASSA                               # တွေ့ထိမှု
NOUN = {    # Pāli noun forms -> Burmese
    "khandh": KH_N, "kkhandh": KH_N, "āyatan": AYA_N, "dhāt": DHA_N, "sacc": SAC_N, "indriy": IND_N,
    "het": HET_N, "kusalahet": f"{T['kusalā']} {HET_N}", "akusalahet": f"{T['akusalā']} {HET_N}",
    "abyākatahet": f"{T['abyākatā']} {HET_N}", "āhār": AHA_N, "phass": PHA_N, "vedan": P1.FEEL,
    "saññ": P1.SANNA, "cetan": P1.CETANA, "citt": P1.MIND,
}
NOUN_FORMS = {      # free noun form -> noun key
    "khandhā": "khandh", "khandho": "khandh", "khandhānaṃ": "khandh",
    "āyatanāni": "āyatan", "āyatanā": "āyatan", "āyatanānaṃ": "āyatan",
    "dhātuyo": "dhāt", "dhātūnaṃ": "dhāt",
    "saccāni": "sacc", "saccā": "sacc", "saccaṃ": "sacc", "saccānaṃ": "sacc",
    "indriyāni": "indriy", "indriyā": "indriy",
    "hetū": "het", "kusalahetū": "kusalahet", "akusalahetū": "akusalahet", "abyākatahetū": "abyākatahet",
    "āhārā": "āhār", "āhāro": "āhār", "phassā": "phass", "phasso": "phass",
    "vedanā": "vedan", "saññā": "saññ", "cetanā": "cetan", "cittāni": "citt", "cittā": "citt", "cittaṃ": "citt",
    "cittānaṃ": "citt",
}
COMP_RE = re.compile(r"(?P<n>" + "|".join(sorted(NUMSTEM, key=len, reverse=True)) + r")(?P<x>kkhandh|āyatan|indriy)"
                     r"(?:ā|āni|aṃ|o)")
APARA = "အခြား"                                 # aparāni / aparā (another)
DEM = "ဤ"                                       # ime / imāni / imā / idaṃ / ayaṃ (pi-1 «ဤသဘောတရားများ»)


def count_my(noun_key, n):
    return f"{NOUN[noun_key]} {num_my(n)}{CL}"


NP_NUM = "|".join(sorted(list(NUMW) + list(NUMGEN), key=len, reverse=True))
NP_NOUN = "|".join(sorted(NOUN_FORMS, key=len, reverse=True))
NP_RE = re.compile(r"(?:(?P<ap>[Aa]parā(?:ni)?) )?(?:(?P<num>" + "|".join(
    f"[{k[0].upper()}{k[0]}]{re.escape(k[1:])}" for k in sorted(list(NUMW) + list(NUMGEN), key=len, reverse=True))
    + r") (?P<noun>" + NP_NOUN + r")|(?P<comp>[A-Za-zāīūṃṅñṭḍṇḷ]+))(?![\wāīūṃṅñṭḍṇḷ])")


def np_at(s, pos):
    """Count noun phrase at s[pos:] -> (end, Burmese, plural, genitive) or None."""
    m = NP_RE.match(s, pos)
    if not m:
        return None
    pre = APARA + " " if m["ap"] else ""
    if m["num"]:
        w = low(m["num"])
        n = NUMW.get(w) or NUMGEN[w]
        return m.end(), pre + count_my(NOUN_FORMS[m["noun"]], n), n > 1, w in NUMGEN
    w = low(m["comp"])
    if w == "pañcakkhandhā":
        return m.end(), pre + count_my("khandh", 5), True, False
    cm = COMP_RE.fullmatch(w)
    if cm:
        key = "khandh" if cm["x"] == "kkhandh" else cm["x"]
        n = NUMSTEM[cm["n"]]
        return m.end(), pre + count_my(key, n), n > 1, False
    return None


# ===================================================================================== list items
SENSE = F.SENSE                                 # cakkhu မျက်စိ …
ITEMS = {}
for _k, _v in F.ITEM.items():
    ITEMS[_k] = _v
for _k in ("manāyatanaṃ", "dhammāyatanaṃ", "manoviññāṇadhātu", "dhammadhātu", "cakkhudhātu", "sotadhātu",
           "ghānadhātu", "jivhādhātu", "kāyadhātu", "rūpadhātu", "saddadhātu", "gandhadhātu", "rasadhātu",
           "phoṭṭhabbadhātu", "manindriyaṃ", "saddhindriyaṃ", "vīriyindriyaṃ", "satindriyaṃ", "samādhindriyaṃ",
           "paññindriyaṃ", "somanassindriyaṃ", "upekkhindriyaṃ", "jīvitindriyaṃ", "phassāhāro",
           "manosañcetanāhāro", "viññāṇāhāro", "alobho", "adoso", "amoho"):
    ITEMS[_k] = P1.NAMES[_k]
for _p, _m in SENSE.items():
    ITEMS[_p + "viññāṇadhātu"] = f"{_m} {P1.VINNANA} {DHA_N}"      # pi-1 termbase cakkhuviññāṇadhātu
for _p, _m in F.SRC.items():
    ITEMS[_p + "samphasso"] = f"{_m}၏ {PHA_N}"                      # pi-1 termbase cakkhusamphasso
ITEMS["kāyaviññāṇadhātusamphasso"] = f"{ITEMS['kāyaviññāṇadhātu']}၏ {PHA_N}"
ITEMS["manodhātu"] = F.ITEM["manodhātu"]
for _k, _v in F.INDR.items():
    ITEMS[_k] = _v
ITEMS["anaññātaññassāmītindriyaṃ"] = "မသိရသေးသည်ကို သိရတော့မည်ဟူသော စွမ်းရည်"   # pi-1 termbase
ITEMS["aññindriyaṃ"] = "အပြည့်အဝ သိမြင်ခြင်း၏ စွမ်းရည်"                       # pi-1 termbase
ITEMS["aññātāvindriyaṃ"] = "အပြည့်အဝ သိမြင်ပြီးသူ၏ စွမ်းရည်"                    # pi-1 2-05 rails text
ITEMS["rūpajīvitindriyaṃ"] = f"{F.RUPA} {P1.NAMES['jīvitindriyaṃ']}"            # (new) material life faculty
DUKKHA_S = "ဒုက္ခ"                                                             # pi-1 Dukkhe (the first truth)
NEW_ITEMS = dict(F.TRUTH)    # consistency pass: the four truths as written, one form with ch4 (no added «ဒုက္ခ»)
assert NEW_ITEMS["dukkhasaccaṃ"] == f"{DUKKHA_S} {SAC_N}" and NEW_ITEMS["maggasaccaṃ"] == f"{P1.MAGGA} {SAC_N}"
ITEMS.update(NEW_ITEMS)
ITEMS["kabaḷīkārāhāro"] = ITEMS["kabaḷīkāro āhāro"]
KUSALAHETU_ATTR = f"{T['kusalā']} {HET_N} ဖြစ်သော"                                # pi-1 ^1-1441 «ကုသိုလ် အမြစ် ဖြစ်သော လောဘ မရှိခြင်း»
AKUSALAHETU_ATTR = f"{T['akusalā']} {HET_N} ဖြစ်သော"
VIPAKAHETU_ATTR = f"{T['vipākā']} စိတ်၏ {HET_N} ဖြစ်သော"                         # pi-1 ^1-1441 vipākahetu
for _p in ("alobho", "adoso", "amoho"):
    ITEMS[_p + " kusalahetu"] = f"{KUSALAHETU_ATTR} {P1.NAMES[_p]}"
    ITEMS[_p + " vipākahetu"] = f"{VIPAKAHETU_ATTR} {P1.NAMES[_p]}"
for _p in ("lobho", "doso", "moho"):
    ITEMS[_p + " akusalahetu"] = f"{AKUSALAHETU_ATTR} {_p and {'lobho': 'လောဘ', 'doso': 'ဒေါသ', 'moho': 'မောဟ'}[_p]}"
for _p in ("rūpakkhandho", "vedanākkhandho", "saññākkhandho", "saṅkhārakkhandho", "viññāṇakkhandho"):
    ITEMS[_p] = F.KH[_p][0]
OR = F.VA_OR                                                                   # vā … vā = «သို့မဟုတ်»
ITEMS["itthindriyaṃ vā purisindriyaṃ vā"] = f"{ITEMS['itthindriyaṃ']} {OR} {ITEMS['purisindriyaṃ']}"
ITEMS["somanassindriyaṃ vā upekkhindriyaṃ vā"] = f"{ITEMS['somanassindriyaṃ']} {OR} {ITEMS['upekkhindriyaṃ']}"
ITEM_RE = re.compile("(?:" + "|".join(f"[{k[0].upper()}{k[0]}]" + re.escape(k[1:])
                                      for k in sorted(ITEMS, key=len, reverse=True)) + r")(?![\wāīūṃṅñṭḍṇḷ])")

# ===================================================================================== variant readings
SIGLA = {"sī.": "Sī.", "syā.": "Syā.", "ka.": "Ka.", "?": F.SIG_UNKNOWN}        # «(?)» = unnamed edition (shared)
REF = {"dī. ni. 2.7": "ဒီဃနိကာယ် 2.7", "a. ni. 3.71": "အင်္ဂုတ္တရနိကာယ် 3.71"}
VAR = {     # variant text -> kind (P1.PATHA a different word, P1.LEKHANA spelling only)
    "kabaḷiṃkāro āhāro": P1.LEKHANA, "keci": P1.PATHA, "avasesā sattā": P1.PATHA, "sammatidevā": P1.LEKHANA,
    "cātummahārājike": P1.LEKHANA, "appaṃ vā bhiyyo vā": P1.PATHA, "rattidivo": P1.LEKHANA,
    "eko kappo": P1.PATHA, "chapi te": P1.PATHA, "bhavaggaṃ vāpi": P1.PATHA, "puna gacchanti": P1.PATHA,
}
VAR_FULL = re.compile(r"\[(?P<t>[^\[\]()]+?) \((?P<s>[^()]+)\)(?: (?P<r>[^\]]+))?\]")


def var_my(br):
    m = VAR_FULL.fullmatch(br)
    if not m or m["t"] not in VAR:
        raise Miss("variant: " + br)
    sig = ", ".join(SIGLA[s] for s in m["s"].split())
    ref = ("; " + REF[m["r"]]) if m["r"] else ""
    return f"[{VAR[m['t']]} ({sig}): {m['t']}{ref}]"


# ===================================================================================== planes, beings, names
PLANE = {   # Pāli -> Burmese name of the plane (kāmadhātu etc. as realm = the pi-1 plane names)
    "kāmadhātuyā": "ကာမဘုံ", "rūpadhātuyā": "သိမ်မွေ့သော ရုပ်ဘုံ", "arūpadhātuyā": "ရုပ်မရှိသော ဘုံ",
    "apariyāpanne": f"{T['apariyāpannā'].removesuffix('သော')}သောအရာ",
}
assert PLANE["kāmadhātuyā"] in T["kāmāvacarā"] and PLANE["rūpadhātuyā"] in T["rūpāvacarā"]
assert PLANE["arūpadhātuyā"] in T["arūpāvacarā"]
LOC = "၌"
PRESENT = "ရှိသော"                               # «kāmadhātuyā pañcakkhandhā» = «ကာမဘုံ၌ ရှိသော အစုအဝေး ငါးပါး»
UPAPATTI = "ပြန်လည် ဖြစ်ပေါ်"                     # upapatti / upapajjati (rebirth, arising in a plane)
KHANE = f"{UPAPATTI}သည့် ခဏ{LOC}"               # upapattikkhaṇe
PATU = "ထင်ရှားလာ"                              # pātubhavati (pi-1 pātubhūtā = ထင်ရှားလာပြီးသော)
WHO = {"sabbesaṃ": "အားလုံးအား", "kassaci": "အချို့အား", "kassa": "မည်သူတို့အား", "etesaṃ": "ဤသူတို့အား"}
WHICH = "မည်သည့်"                               # katama (in the rebirth questions)
DEVA = "နတ်"                                    # deva (pi-1 deve = နတ်)
DEVA_NAME = {   # proper names stay names (APPROVED.md rule 1); arūpa planes as pi-1 ^1-1291
    "cātumahārājik": "စာတုမဟာရာဇ်", "cātummahārājik": "စာတုမဟာရာဇ်", "tāvatiṃs": "တာဝတိံသာ", "yām": "ယာမာ",
    "tusit": "တုသိတာ", "nimmānaratī": "နိမ္မာနရတီ", "paranimmitavasavattī": "ပရနိမ္မိတဝသဝတ္တီ",
    "brahmapārisajj": "ဗြဟ္မပါရိသဇ္ဇ", "brahmapurohit": "ဗြဟ္မပုရောဟိတ", "mahābrahm": "မဟာဗြဟ္မာ",
    "parittābh": "ပရိတ္တာဘ", "appamāṇābh": "အပ္ပမာဏာဘ", "ābhassar": "အာဘဿရ", "parittasubh": "ပရိတ္တသုဘ",
    "appamāṇasubh": "အပ္ပမာဏသုဘ", "subhakiṇh": "သုဘကိဏှ", "asaññasatt": "အသညသတ်", "vehapphal": "ဝေဟပ္ဖိုလ်",
    "avih": "အဝိဟာ", "atapp": "အတပ္ပါ", "sudass": "သုဒဿာ", "sudassī": "သုဒဿီ", "akaniṭṭh": "အကနိဋ္ဌ",
    "ākāsānañcāyatanūpag": "အဆုံး မရှိသော ဟင်းလင်းပြင် နယ်ပယ် ဘုံသို့ ရောက်သော",
    "viññāṇañcāyatanūpag": "အဆုံး မရှိသော သိစိတ် နယ်ပယ် ဘုံသို့ ရောက်သော",
    "ākiñcaññāyatanūpag": "ဘာမျှ မရှိသော နယ်ပယ် ဘုံသို့ ရောက်သော",
    "nevasaññānāsaññāyatanūpag": "မှတ်သိမှု ရှိသည်လည်း မဟုတ်၊ မှတ်သိမှု မရှိသည်လည်း မဟုတ်သော နယ်ပယ် ဘုံသို့ ရောက်သော",
}
DEVA_RE = re.compile(r"(?P<n>" + "|".join(sorted(DEVA_NAME, key=len, reverse=True)) + r")(?:ānaṃ|īnaṃ|naṃ|e)"
                     r"(?P<ca>ñca)? (?:devānaṃ|deve)")
AMONG = "တို့အနက်"
BEING_N = {     # nouns of the beings lists (genitive pl. -> Burmese)
    "kāmāvacarānaṃ devānaṃ": f"{T['kāmāvacarā']} {DEVA}", "paṭhamakappikānaṃ manussānaṃ": "ကမ္ဘာဦး လူ",
    "opapātikānaṃ petānaṃ": "အလိုအလျောက် ပေါ်လာသော ပြိတ္တာ",                       # pi-1 opapātikā
    "opapātikānaṃ asurānaṃ": "အလိုအလျောက် ပေါ်လာသော အသုရာ",
    "opapātikānaṃ tiracchānagatānaṃ": "အလိုအလျောက် ပေါ်လာသော တိရစ္ဆာန်",
    "nerayikānaṃ": "ငရဲသား", "gabbhaseyyakānaṃ sattānaṃ": "အမိဝမ်းတွင်း၌ ဖြစ်သော သတ္တဝါ",
    "asaññasattānaṃ devānaṃ": f"အသညသတ် {DEVA}",
}
BEING_Q = {     # qualifiers (stems; several joined by «၍»)
    "sahetukānaṃ": "အမြစ် ရှိ", "ahetukānaṃ": "အမြစ် မရှိ", "ñāṇasampayuttānaṃ": "ဉာဏ်နှင့် ယှဉ်တွဲ",
    "ñāṇavippayuttānaṃ": "ဉာဏ်နှင့် ကင်းကွာ", "paripuṇṇāyatanānaṃ": f"{AYA_N} ပြည့်စုံ",
    "jaccandhānaṃ": "မွေးရာပါ မျက်စိ ကန်း", "jaccabadhirānaṃ": "မွေးရာပါ နား ပင်း",
    "jaccandhabadhirānaṃ": "မွေးရာပါ မျက်စိ ကန်း၍ နား ပင်း", "napuṃsakānaṃ": "လိင် မရှိ",
}
THAPETVA = P1.THAPETVA.strip()                  # ကို ချန်ထား၍
PERSON = "သူ"


def beings_my(s):
    """«Kāmāvacarānaṃ devānaṃ, sahetukānaṃ ñāṇasampayuttānaṃ» -> «… နတ်တို့အနက် အမြစ် ရှိ၍ … သူတို့»."""
    s = s.rstrip(",")
    toks = re.split(r"(, | )", s)
    words = [t for t in toks if t.strip(", ")]
    nouns, quals, excl, i = [], [], [], 0
    lowered = [low(w) for w in words]
    while i < len(lowered):
        two = " ".join(lowered[i:i + 2])
        if two in BEING_N:
            nouns.append(BEING_N[two])
            i += 2
        elif lowered[i] in BEING_N:
            nouns.append(BEING_N[lowered[i]])
            i += 1
        elif lowered[i] == "ṭhapetvā" and i + 1 < len(lowered) and lowered[i + 1] in BEING_Q:
            excl.append(BEING_Q[lowered[i + 1]] + PERSON + "တို့" + THAPETVA)
            i += 2
        elif lowered[i] in BEING_Q:
            quals.append(BEING_Q[lowered[i]])
            i += 1
        else:
            raise Miss("being: " + words[i])
    out = f"{C} ".join(nouns)
    if quals:
        out += AMONG + " " + (" ".join(excl) + " " if excl else "") + "၍ ".join(quals) + PERSON + "တို့"
    elif excl:
        raise Miss("exclusion without qualifier: " + s)
    else:
        out += "တို့"
    return out


# ===================================================================================== predicate terms
TERM = {    # stem (case ending removed) -> (attributive, negated attributive)
    "pariyāpann": (T["pariyāpannā"], None), "apariyāpann": (T["apariyāpannā"], None),
    "abhiññeyy": ("ထူးကဲစွာ သိရမည့်", "ထူးကဲစွာ သိရမည် မဟုတ်သော"),        # (new) pi-1 abhiññā = ထူးကဲစွာ သိ၍
    "pariññeyy": ("ပိုင်းခြား သိရမည့်", "ပိုင်းခြား သိရမည် မဟုတ်သော"),          # (new)
    "pahātabb": (P1.PAH, P1.PAH_S + " မဟုတ်သော"),                            # pi-1 ပယ်ရမည့် / ပယ်ရမည် မဟုတ်
    "bhāvetabb": ("ပွားများရမည့်", "ပွားများရမည် မဟုတ်သော"),                 # (new) pi-1 bhāveti = ပွားများသည်
    "sacchikātabb": ("မျက်မှောက်ပြုရမည့်", "မျက်မှောက်ပြုရမည် မဟုတ်သော"),     # (new) pi-1 sacchikiriyāya
    "sārammaṇārammaṇ": ("အာရုံ ရှိသည်ကို အာရုံပြုသော", None),                 # (new) pi-1 parittārammaṇa form
    "anārammaṇārammaṇ": ("အာရုံ မရှိသည်ကို အာရုံပြုသော", None),
    "diṭṭh": ("မြင်ရသော", "မြင်ရသည် မဟုတ်သော"),                               # pi-1 Rūpakaṇḍa catukka
    "sut": ("ကြားရသော", "ကြားရသည် မဟုတ်သော"),
    "mut": ("နမ်း မြည်း ထိတွေ့ရသော", "နမ်း မြည်း ထိတွေ့ရသည် မဟုတ်သော"),
    "viññāt": ("သိရသော", "သိရသည် မဟုတ်သော"),
    "rūp": (T["rūpino"], None), "arūp": (T["arūpino"], None),
}
for _pl, _nm in (("kāmadhātu", "kāmadhātuyā"), ("rūpadhātu", "rūpadhātuyā"), ("arūpadhātu", "arūpadhātuyā")):
    TERM[_pl + "pariyāpann"] = (f"{PLANE[_nm]}{LOC} အကျုံးဝင်သော", f"{PLANE[_nm]}{LOC} အကျုံးဝင်သည် မဟုတ်သော")
TERM_END = ("āni", "aṃ", "ā", "o", "a")


def term_my(p, neg=False):
    p = p.replace("upādinn", "upādiṇṇ")
    for e in TERM_END:
        if p.endswith(e) and p[:-len(e)] in TERM:
            a, n = TERM[p[:-len(e)]]
            if neg:
                if n is None:
                    raise Miss("negated term: " + p)
                return n
            return a
    if neg:
        return F.term_my("na " + p)
    return F.term_my(p)


TERM_WORDS = 3          # longest Pāli term in words (sukhāya vedanāya sampayuttā)


def chain_my(toks):
    """['abhiññeyyo', 'pariññeyyo', 'na', 'pahātabbo'] -> «ထူးကဲစွာ သိရမည့်၊ … ပယ်ရမည် မဟုတ်သော»."""
    out, i = [], 0
    while i < len(toks):
        neg = toks[i] == "na"
        j = i + 1 if neg else i
        for k in range(TERM_WORDS, 0, -1):
            if j + k > len(toks):
                continue
            try:
                out.append(term_my(" ".join(toks[j:j + k]), neg))
                i = j + k
                break
            except Miss:
                continue
        else:
            raise Miss("term: " + " ".join(toks[j:j + 3]))
    return f"{C} ".join(out)


# ===================================================================================== statements
SUBJ_SEP = re.compile(r"(?:…pe… |… | … |…| …)")


def subj_at(s, pos):
    """Subject at s[pos:] (one NP or an ellipsis chain of NPs / items) -> (end, Burmese, plural) or None.
    The number of a chain is that of its last member (the Pāli verb agrees with it)."""
    text, pls, p = "", [], pos
    while True:
        r = np_at(s, p)
        if r and not r[3]:
            p2, my, pl, _ = r
        else:
            m = ITEM_RE.match(s, p)
            if not m:
                break
            p2, my, pl = m.end(), ITEMS[low(m[0])], False
        text += my
        pls.append(pl)
        m2 = SUBJ_SEP.match(s, p2)
        if m2 and (np_at(s, m2.end()) or ITEM_RE.match(s, m2.end())):
            text += PE + (" " if m2[0].endswith(" ") else "")
            p = m2.end()
            continue
        r3 = np_at(s, p2 + 1) if s.startswith(" ", p2) else None
        if r3 and not r3[3] and pls and r:                     # «satta cetanā satta cittā» (source slip ^2-1043)
            text += C + " "
            p = p2 + 1
            continue
        p = p2
        break
    if not pls:
        return None
    return p, text, pls[-1]


NV_RE = re.compile(r"(?P<t>.+?)(?P<e>ntipi|tipi|ti pi)$")


def nv_term(t):
    m = NV_RE.fullmatch(t)
    if not m:
        return None
    return term_my(m["t"] + ("ṃ" if m["e"] == "ntipi" else ""))


# consistency pass (harmonise-todo A): ^2-1039 «siyā dukkhamasukhāya» (a- missing) is translated AS WRITTEN:
# dukkham-asukha = painful and not pleasant («နာကျင် မသာယာသော»), not read as adukkhamasukha (logged)
T.setdefault("dukkhamasukhāya vedanāya sampayuttā", f"{P1.DUKKHA} မ{P1.SUKHA}သော {P1.FEEL}{P1.SAMP}")


def statement_my(s):
    """One statement sentence (without its final «.») of the pariyāpanna / abhiññeyya / … / duka sections."""
    s = s.replace("kāmadhātu pariyāpann", "kāmadhātupariyāpann")             # source slip ^2-1000 (space)
    s = s.replace("sampayuttoti pi", "sampayuttotipi")                       # source slip ^2-1039 (space)
    groups = []                                                              # (separator, group)
    for i, g in enumerate(re.split(r"; |, ", s)):
        hs = re.split(r" (?=siyā )", g)                                     # «… siyā X siyā Y» without comma
        if len(hs) > 1:
            r0 = subj_at(hs[0], 0)
            if r0 and r0[0] == len(hs[0]):                                   # «S siyā …»: S is the subject
                hs[:2] = [hs[0] + " " + hs[1]]
        for j, h in enumerate(hs):
            groups.append(("" if i == 0 and j == 0 else (f"{C} " if j == 0 else " "), h))
    out, pl, nv_open = "", False, False
    for sep, g in groups:
        tail = ""
        mt = re.search(r" (\d+)$", g)                                        # stray footnote digit (^2-1041)
        if mt:
            tail, g = " " + mt[1], g[:mt.start()]
        if nv_open:
            t = nv_term(g) if not g.startswith(("siyā ", "na ")) else None
            if t:
                out += f"{C} {t} {dh(pl)}{TIPI}"
                continue
            out += " " + NVATT
            nv_open = False
        out += sep
        r = subj_at(g, 0)
        rest = g
        if r and (r[0] == len(g) or g[r[0]] == " "):
            rest = g[r[0]:].strip()
            pl = r[2]
            out += r[1] + "သည် "
        toks = rest.split(" ")
        pre = ""
        if toks[0] == "siyā":
            pre, toks = SIYA + " ", toks[1:]
        if toks[:2] in (["na", "vattabbo"], ["na", "vattabbā"], ["na", "vattabbaṃ"]):
            t = nv_term(" ".join(toks[2:]))
            if not t:
                raise Miss("na vattabbo: " + g)
            out += pre + f"{t} {dh(pl)}{TIPI}"
            nv_open = True
            continue
        try:
            out += pre + f"{chain_my(toks)} {dh(pl)} {cop(pl)}" + tail
            continue
        except Miss:
            pass
        # a new subject inside the chain without punctuation (source slip ^2-1042)
        for ti in range(1, len(toks)):
            sub = " ".join(toks[ti:])
            r2 = subj_at(sub, 0)
            if not r2 or r2[0] >= len(sub) or sub[r2[0]] != " ":
                continue
            try:
                head = chain_my(toks[:ti])
                rest2 = sub[r2[0]:].strip().split(" ")
                pre2 = ""
                if rest2[0] == "siyā":
                    pre2, rest2 = SIYA + " ", rest2[1:]
                body2 = chain_my(rest2)
            except Miss:
                continue
            out += pre + f"{head} {dh(pl)} {cop(pl)} "
            pl = r2[2]
            out += f"{r2[1]}သည် {pre2}{body2} {dh(pl)} {cop(pl)}" + tail
            break
        else:
            raise Miss("statement: " + g)
    if nv_open:
        out += " " + NVATT
    return out


# ===================================================================================== questions with «kati»
KATI_NOUN = {"khandhā": KH_N, "āyatanāni": AYA_N, "āyatanā": AYA_N, "dhātuyo": DHA_N, "saccāni": SAC_N,
             "indriyāni": IND_N, "hetū": HET_N, "āhārā": AHA_N, "phassā": PHA_N, "vedanā": P1.FEEL,
             "saññā": P1.SANNA, "cetanā": P1.CETANA, "cittāni": P1.MIND}


def kati_terms_my(s):
    """«Pañcannaṃ khandhānaṃ kati T1, kati T2…pe… sattannaṃ cittānaṃ kati T1, kati T2» (no final «?»)."""
    segs = re.split(r"( ?…pe… ?)", s)
    out = []
    for seg in segs:
        if seg.strip() == "…pe…":
            out.append(PE + " ")
            continue
        m = re.match(r"(?P<g>\S+ \S+) kati (?P<rest>.+)$", seg)
        if not m:
            raise Miss("kati: " + seg)
        r = np_at(m["g"], 0)
        if not r or not r[3] or r[0] != len(m["g"]):
            raise Miss("kati head: " + m["g"])
        items = m["rest"].split(", kati ")
        body = f"{C} ".join(chain_my(re.split(r",? ", it)) + f" {DH} {KATI}" for it in items)
        out.append(f"{r[1]}{AMONG} {body}")
    return "".join(out).replace(" … ", PE + " ").rstrip() + " " + KATI_END


def kati_nouns_my(s, verb=None):
    """«kati khandhā, kati āyatanāni …» (plane counts) or «kati khandhā pātubhavanti…pe… kati cittāni pātubhavanti»."""
    out = []
    for seg in re.split(r"(…pe… ?|, )", s):
        if seg in (", ",):
            out.append(C + " ")
            continue
        if seg.startswith("…pe…"):
            out.append(PE + " ")
            continue
        m = re.fullmatch(r"[Kk]ati (?P<n>\S+)(?: (?P<v>pātubhavanti|pātubhavati))?", seg)
        if not m or m["n"] not in KATI_NOUN:
            raise Miss("kati noun: " + seg)
        out.append(f"{KATI_NOUN[m['n']]} {KATI}" + (f" {PATU}ကြသနည်း" if m["v"] else ""))
    s2 = "".join(out)
    return s2 if verb else s2 + " " + KATI_END


# ===================================================================================== lists
LIST_SEP = re.compile(r"(…pe… | …pe… |…pe…| … |… |…|, )")


def list_my(s, ph=None):
    """Item list «A, B…pe… C» -> «A၊ B… C». Placeholders «§n§» after an item are kept."""
    out = []
    for part in LIST_SEP.split(s):
        if not part:
            continue
        if part == ", ":
            out.append(C + " ")
            continue
        if "…" in part:
            out.append(PE + (" " if part.endswith(" ") else ""))
            continue
        tail = ""
        mm = re.search(r" (§\d+§)$", part)
        if mm:
            tail, part = " " + mm[1], part[:mm.start()]
        if low(part) in ITEMS:
            out.append(ITEMS[low(part)] + tail)
            continue
        r = np_at(part, 0)
        if r and r[0] == len(part):
            out.append(r[1] + tail)
            continue
        words = part.split(" ")                                  # missing comma (source slip ^2-992)
        if len(words) == 2 and all(low(w) in ITEMS for w in words):
            out.append(" ".join(ITEMS[low(w)] for w in words) + tail)
            continue
        raise Miss("list item: " + part)
    return "".join(out)


# ===================================================================================== headings and fixed lines
VARA = P1.VARA                                  # ဖော်ပြချက်
CH_TITLE = f"{DHP}၏ နှလုံးသားကို {F.TITLE}"      # Dhammahadayavibhaṅgo (chapter title «X ကို ခွဲခြမ်းစိတ်ဖြာခြင်း»)
APAR_N = PLANE["apariyāpanne"]
PARI_N = f"{T['pariyāpannā'].removesuffix('သော')}သောအရာ"
SHOW = "ပြသသော"
HEAD = {
    "Dhammahadayavibhaṅgo": CH_TITLE,
    "Sabbasaṅgāhikavāro": f"အားလုံးကို စုစည်းသော {VARA}",
    "Uppattānuppattivāro": f"ဖြစ်ပေါ်ခြင်း မဖြစ်ပေါ်ခြင်း {VARA}",
    "Kāmadhātu": PLANE["kāmadhātuyā"], "Rūpadhātu": PLANE["rūpadhātuyā"], "Arūpadhātu": PLANE["arūpadhātuyā"],
    "Apariyāpannaṃ": APAR_N,
    "Pariyāpannāpariyāpannavāro": f"ဘဝဘုံ၌ အကျုံးဝင်ခြင်း အကျုံးမဝင်ခြင်း {VARA}",
    "Pariyāpannāpariyāpannaṃ": f"{PARI_N}နှင့် အကျုံးမဝင်သောအရာ",
    "Dhammadassanavāro": f"{DHP}ကို {SHOW} {VARA}",
    "Asaññasattā": "အသညသတ်များ",
    "Bhūmantaradassanavāro": f"ဘုံ အသီးသီးကို {SHOW} {VARA}",
    "Uppādakakammaāyuppamāṇavāro": f"ဖြစ်ပေါ်စေသော ကံနှင့် သက်တမ်း အတိုင်းအတာ {VARA}",
    "Uppādakakammaṃ": "ဖြစ်ပေါ်စေသော ကံ",
    "Āyuppamāṇaṃ": "သက်တမ်း အတိုင်းအတာ",
    "Abhiññeyyādivāro": f"{TERM['abhiññeyy'][0]} {DH} စသည်ကို {SHOW} {VARA}",
    "Sārammaṇānārammaṇavāro": f"အာရုံ ရှိခြင်း မရှိခြင်း {VARA}",
    "Diṭṭhasutādidassanavāro": f"မြင်ရသော ကြားရသော စသည်တို့ကို {SHOW} {VARA}",
    "Tikādidassanavāro": f"{P1.TIKA} စသည်တို့ကို {SHOW} {VARA}",
    "Kusalattikaṃ": f"{T['kusalā']} {P1.TIKA}", "Vedanātikaṃ": f"{P1.FEEL} {P1.TIKA}",
    "Vipākattikaṃ": f"{T['vipākā'].removesuffix(' ဖြစ်သော')} {P1.TIKA}",
    "Upādinnattikaṃ": f"{T['upādiṇṇā'].removesuffix(' ဖြစ်သော')} ဖြစ်ခြင်း {P1.TIKA}",
    "Vitakkattikaṃ": f"{P1.NAMES['vitakko']} {P1.TIKA}",
    "(1) Rūpadukaṃ": f"(1) {F.RUPA} {P1.DUKA}", "(2) Lokiyadukaṃ": f"(2) {T['lokiyā'].removesuffix('သော')}သော {P1.DUKA}",
}
COLO = {
    "Dhammahadayavibhaṅgo niṭṭhito.": f"“{CH_TITLE}” {F.NITTHITA}{END}",
    "Vibhaṅgapakaraṇaṃ niṭṭhitaṃ.": f"“{F.TITLE}” ကျမ်း {F.NITTHITA}{END}",          # pi-1 ^1-1616 pattern
}
KUSALA, AKUSALA = T["kusalā"], T["akusalā"]
YEAR, HUMAN_Y, DIVINE_Y = "နှစ်", "လူ့ နှစ်", f"{DEVA} နှစ်"
KAPPA = "ကမ္ဘာ"                                  # kappa (aeon)
KOTI, LAKH = "ကုဋေ", "သိန်း"                      # koṭi (10^7), satasahassa (10^5)
YEARS = "နှစ်ပေါင်း"


def koti_my(k=None, lakh=None, ksata=None):
    parts = []
    if ksata:
        parts.append(f"{YEARS} {KOTI} {num_my(ksata * 100)}")
    if k:
        parts.append(f"{YEARS} {KOTI} {num_my(k)}")
    if lakh:
        parts.append(f"{YEARS} {LAKH} {num_my(lakh)}")
    if len(parts) == 1:
        return parts[0]
    return f"{C} ".join(parts[:-1]) + "နှင့် " + parts[-1]


FIXED = {   # whole sentences without a reusable frame (verses, the deva definitions, the uddāna)
    "Devāti.": f"“{DEVA}” ဟူသည်{END}",
    "Tayo devā – sammutidevā §0§, upapattidevā, visuddhidevā.":
        f"{DEVA} {num_my(3)}မျိုး – သမုတ်ခြင်းအားဖြင့် {DEVA} §0§{C} {UPAPATTI}ခြင်းအားဖြင့် {DEVA}{C} "
        f"စင်ကြယ်ခြင်းအားဖြင့် {DEVA}{END}",
    "Sammutidevā nāma – rājāno, deviyo, kumārā.":
        f"သမုတ်ခြင်းအားဖြင့် {DEVA} ဟူသည် – ဘုရင်များ{C} မိဖုရားများ{C} မင်းသားများ{END}",
    "Upapattidevā nāma – cātumahārājike §0§ deve upādāya tadupari devā.":
        f"{UPAPATTI}ခြင်းအားဖြင့် {DEVA} ဟူသည် – စာတုမဟာရာဇ် §0§ {DEVA}တို့မှ စ၍ ထိုအထက်ရှိ {DEVA}များ{END}",
    "Visuddhidevā nāma – arahanto vuccanti.":
        f"စင်ကြယ်ခြင်းအားဖြင့် {DEVA} ဟူသည် – ရဟန္တာတို့ကို ခေါ်သည်{END}",
    "Dānaṃ datvā, sīlaṃ samādiyitvā, uposathakammaṃ katvā kattha upapajjanti?":
        f"အလှူကို ပေး၍{C} သီလကို ဆောက်တည်၍{C} ဥပုသ်ကို စောင့်ထိန်း၍ မည်သည့်နေရာ၌ {UPAPATTI}ကြသနည်း{END}",
    "Vassasataṃ, appaṃ vā bhiyyo §0§.":
        f"{YEAR} {num_my(100)}{C} အနည်းငယ် လျော့သည်ဖြစ်စေ ပိုသည်ဖြစ်စေ §0§{END}",
    "Tāya rattiyā tiṃsa rattiyo māso.": f"ထိုညဖြင့် ည {num_my(30)}သည် {num_my(1)}လ ဖြစ်သည်{END}",
    "Tāya rattiyā tiṃsarattiyo māso.": f"ထိုညဖြင့် ည {num_my(30)}သည် {num_my(1)}လ ဖြစ်သည်{END}",
    "Tena māsena dvādasamāsiyo saṃvaccharo.": f"ထိုလဖြင့် {num_my(12)}လသည် {num_my(1)}နှစ် ဖြစ်သည်{END}",
    "Manussānaṃ gaṇanāya kittakaṃ hoti?": f"လူတို့၏ ရေတွက်ပုံဖြင့် {KATI} {KATI_END}{END}",
    "Navuti vassasatasahassāni.": f"{koti_my(lakh=90)}{END}",
    "Tisso ca vassakoṭiyo saṭṭhi ca vassasatasahassāni.": f"{koti_my(k=3, lakh=60)}{END}",
    "Cuddasañca vassakoṭiyo cattārīsañca vassasatasahassāni.": f"{koti_my(k=14, lakh=40)}{END}",
    "Sattapaññāsa vassakoṭiyo saṭṭhi ca vassasatasahassāni.": f"{koti_my(k=57, lakh=60)}{END}",
    "Dve vassakoṭisatāni tiṃsañca vassakoṭiyo cattārīsañca vassasatasahassāni.":
        f"{koti_my(ksata=2, k=30, lakh=40)}{END}",
    "Nava ca vassakoṭisatāni ekavīsañca vassakoṭiyo saṭṭhi ca vassasatasahassānīti.":
        f"{koti_my(ksata=9, k=21, lakh=60)} ဖြစ်သည်{END}",
    "Cha ete §0§ kāmāvacarā, sabbakāmasamiddhino;":
        f"{DEM}{DEVA}ဘုံ {num_my(6)}ပါးသည် §0§ {T['kāmāvacarā']} ဘုံများ ဖြစ်၍ ကာမဂုဏ် အားလုံးနှင့် ပြည့်စုံကြသည်{C}",
    "Sabbesaṃ ekasaṅkhāto, āyu bhavati kittako.":
        f"ထိုအားလုံး၏ သက်တမ်းကို တစ်ပေါင်းတည်း ရေတွက်လျှင် {KATI} {KATI_END}{END}",
    "Dvādasa koṭisataṃ tesaṃ, aṭṭhavīsañca koṭiyo;":
        f"ထိုသူတို့၏ သက်တမ်းသည် {KOTI} {num_my(1200)}{C} {KOTI} {num_my(28)}{C}",
    "Paññāsa satasahassāni, vassaggena pakāsitāti.":
        f"{LAKH} {num_my(50)} ဟူ၍ {YEAR}အားဖြင့် ဖော်ပြထားသည်{END}",
    "Ukkhittā puññatejena, kāmarūpagatiṃ gatā.":
        f"ကောင်းမှု၏ တန်ခိုးဖြင့် မြှောက်တင်ခံရ၍{C} ကာမဘုံနှင့် {PLANE['rūpadhātuyā']} လားရာသို့ ရောက်ကြသည်{END}",
    "Bhavaggatampi §0§ sampattā, punāgacchanti §1§ duggatiṃ.":
        f"ဘဝ၏ ထိပ်ဆုံးသို့ §0§ ရောက်ကြသော်လည်း{C} ဆိုးသော လားရာသို့ တဖန် ပြန်လာကြရသည် §1§{END}",
    "Tāva dīghāyukā sattā, cavanti āyusaṅkhayā;":
        f"ထိုမျှ သက်တမ်း ရှည်သော သတ္တဝါတို့သည်ပင်{C} သက်တမ်း ကုန်ဆုံးသဖြင့် စုတေကြရသည်{C}",
    "Natthi koci bhavo nicco, iti vuttaṃ mahesinā.":
        f"မြဲသော ဘဝ တစ်စုံတစ်ရာ မရှိ{C} ဟူ၍ မြတ်စွာဘုရား ဟောတော်မူခဲ့သည်{END}",
    "Tasmā hi dhīrā nipakā, nipuṇā atthacintakā;":
        f"ထို့ကြောင့် ပညာရှိ၍ ရင့်ကျက်သော{C} လိမ္မာ၍ အကျိုးကို စဉ်းစားတတ်သူတို့သည်{C}",
    "Jarāmaraṇamokkhāya, bhāventi maggamuttamaṃ.":
        f"အိုခြင်း သေခြင်းမှ လွတ်မြောက်ရန်{C} အမြတ်ဆုံး {P1.MAGGA}ကို ပွားများကြသည်{END}",
    "Bhāvayitvā suciṃ maggaṃ, nibbānogadhagāminaṃ;":
        f"နိဗ္ဗာန်ထဲသို့ သက်ဝင် ရောက်ရှိစေသော စင်ကြယ်သော {P1.MAGGA}ကို ပွားများ၍{C}",
    "Sabbāsave pariññāya, parinibbanti anāsavāti.":
        f"{T['sāsavā'].split('၏')[0]} အားလုံးကို ပိုင်းခြား သိ၍{C} {T['sāsavā'].split('၏')[0]} မရှိသူများအဖြစ် "
        f"ပရိနိဗ္ဗာန် ပြုကြသည်{END}",
    "Abhiññā dve sārammaṇā, diṭṭhā kusalavedanā;":
        f"{TERM['abhiññeyy'][0]}အရာ{C} {T['sārammaṇā']}အရာ {num_my(2)}မျိုး{C} {TERM['diṭṭh'][0]}အရာ{C} "
        f"{KUSALA}{C} {P1.FEEL}{C}",
    "Vipākā ca upādinnā, vitakkaṃ rūpalokiyāti.":
        f"{T['vipākā']}အရာနှင့် {T['upādiṇṇā']}အရာ{C} {P1.NAMES['vitakko']}{C} {F.RUPA}{C} "
        f"{T['lokiyā']}အရာ ဟူ၍ ဖြစ်သည်{END}",
}
VAR_LINES = {}          # filled per line: placeholder -> Burmese bracket


# ===================================================================================== pi-1 sentences
def _psplit(l):
    l = F.ID_RE.sub("", l)
    l = re.sub(r"\[[^\]]*\]", lambda m: m[0].replace(". ", ".\x00"), l)
    return [s.replace("\x00", " ") for s in re.split(r"(?<=[.?])(?:\"|”)? (?=\S)", l) if s]


def _bsplit(l):
    return [s for s in re.split(r"(?<=။) ", F.ID_RE.sub("", l)) if s]


P1SENT = {}
for _p in sorted(F.P1_PALI.glob("*.md")):
    for _x, _y in zip(_p.read_text(encoding="utf-8-sig").split("\n"),
                      (F.P1_RAILS / _p.name).read_text(encoding="utf-8").split("\n")):
        if _x.strip() and not _x.startswith("#"):
            _ps, _bs = _psplit(_x), _bsplit(_y)
            if len(_ps) == len(_bs):
                for _s, _t in zip(_ps, _bs):
                    P1SENT.setdefault(_s, set()).add(_t)


def _p1_body(ch, bid, sent=1):
    line = F._p1_line(ch, bid)
    return _bsplit(line)[sent]


def _novar(s):
    s = re.sub(r" \[[^\]]+\] ဖြစ်စေ", "ဖြစ်စေ", s)                 # «…သူ၏ [var] ဖြစ်စေ» -> «…သူ၏ဖြစ်စေ» (as ^1-1291)
    return re.sub(r" \[[^\]]+\]", "", s)


_KAMA = _novar(_p1_body("4-02-nikkhepakandam.md", "1-1287"))
_RUPA = _novar(_p1_body("4-02-nikkhepakandam.md", "1-1289"))
_ARUPA = _p1_body("4-02-nikkhepakandam.md", "1-1291")
_PARI = _p1_body("4-02-nikkhepakandam.md", "1-1293").replace(
    f"{ITEMS['rūpakkhandho']}{PE} {ITEMS['viññāṇakkhandho']}",
    f"{C} ".join(ITEMS[k] for k in ("rūpakkhandho", "vedanākkhandho", "saññākkhandho", "saṅkhārakkhandho",
                                    "viññāṇakkhandho")))
assert PE not in _PARI and "[" not in _KAMA + _RUPA + _ARUPA
_ABY3 = _p1_body("4-01-nikkhepakandam.md", "1-1068")
_ABY3_APAR = _ABY3.replace(f"စိတ်၌ဖြစ်စေ ပြုရုံမျှသာ ဖြစ်သော {T['abyākatā']} သဘောတရားတို့၌ဖြစ်စေ ", "စိတ်၌ ")
assert _ABY3_APAR != _ABY3
DERIVED = {     # Pāli sentence (this chapter) -> Burmese derived from the pi-1 line
    "Heṭṭhato avīcinirayaṃ pariyantaṃ karitvā, uparito paranimmitavasavattī deve antokaritvā, yaṃ etasmiṃ antare "
    "etthāvacarā ettha pariyāpannā khandhadhātuāyatanā; rūpaṃ, vedanā, saññā, saṅkhārā, viññāṇaṃ – ime dhammā "
    "kāmāvacarā.": _KAMA,
    "Heṭṭhato brahmalokaṃ pariyantaṃ karitvā, uparito akaniṭṭhe deve antokaritvā, yaṃ etasmiṃ antare etthāvacarā "
    "ettha pariyāpannā samāpannassa vā upapannassa vā diṭṭhadhammasukhavihārissa vā cittacetasikā dhammā – ime "
    "dhammā rūpāvacarā.": _RUPA,
    "Heṭṭhato ākāsānañcāyatanūpage deve pariyantaṃ karitvā, uparito nevasaññānāsaññāyatanūpage deve antokaritvā, "
    "yaṃ etasmiṃ antare etthāvacarā ettha pariyāpannā samāpannassa vā upapannassa vā diṭṭhadhammasukhavihārissa vā "
    "cittacetasikā dhammā – ime dhammā arūpāvacarā.": _ARUPA,
    "Sāsavā kusalākusalabyākatā dhammā kāmāvacarā, rūpāvacarā, arūpāvacarā, rūpakkhandho, vedanākkhandho, "
    "saññākkhandho, saṅkhārakkhandho, viññāṇakkhandho – ime dhammā pariyāpannā.": _PARI,
    "Kusalānaṃ vā dhammānaṃ vipākato kiriyābyākatesu vā dhammesu alobho, adoso, amoho – ime tayo abyākatahetū.":
        _ABY3,
    "Kusalānaṃ dhammānaṃ vipākato alobho, adoso, amoho – ime tayo abyākatahetū.": _ABY3_APAR,
}
REUSED = []             # (line, Pāli sentence) taken from P1SENT


# ===================================================================================== sentence frames
PL_ALT = "|".join(f"[{k[0].upper()}{k[0]}]{re.escape(k[1:])}" for k in PLANE)


def plane_my(p):
    return PLANE[low(p)]


def np_full(s):
    """Whole string = an NP chain (with ellipses) -> (Burmese, plural)."""
    r = subj_at(s, 0)
    if not r or r[0] != len(s):
        raise Miss("noun phrase: " + s)
    return r[1], r[2]


def named_np(s):
    """«kāmadhātuyā pañcakkhandhā» / «pañcakkhandhā» -> Burmese (plane + «၌ ရှိသော»)."""
    m = re.match(r"(?P<p>" + PL_ALT + r") (?P<n>.+)$", s)
    if m:
        n, pl = np_full(m["n"])
        return f"{plane_my(m['p'])}{LOC} {PRESENT} {n}", pl
    return np_full(s)


def f_tattha_q(m):
    n, pl = named_np(m["np"])
    return f"ထိုတို့အနက် {n} ဟူသည် အဘယ်{'တို့' if pl else ''}နည်း{END}"


def f_vuccati(m):
    pl = m["v"] != "vuccati"
    q = '“' if m["q1"] else ""
    n, _ = named_np(m["x"])
    return f"{DEM}သည်{'တို့' if pl else ''}ကို {q}{n}{'”' if q else ''}ဟု ခေါ်သည်{END}"


def f_list_vuccati(m):
    pl = m["v"] != "vuccati"
    q = '“' if m["q1"] else ""
    n, _ = named_np(m["x"])
    return f"{list_my(m['l'])} – {DEM}သည်{'တို့' if pl else ''}ကို {q}{n}{'”' if q else ''}ဟု ခေါ်သည်{END}"


def f_list_ime(m):
    n, pl = np_full(m["x"])
    return f"{list_my(m['l'])} – {DEM}သည်{'တို့' if pl else ''}မှာ {n} {cop(pl)}{END}"


def f_list_end(m):
    return list_my(m["l"]) + END


def f_list_pe_vuccati(m):           # «Tayo kusalahetū, …, tayo abyākatahetū…pe… ime vuccanti "…"»
    pl = m["v"] != "vuccati"
    n, _ = named_np(m["x"])
    return f"{list_my(m['l'])}{PE} {DEM}သည်{'တို့' if pl else ''}ကို “{n}”ဟု ခေါ်သည်{END}"


def f_plane_kati(m):
    pre = f"{plane_my(m['p'])}{LOC} " if m["p"] else ""
    return pre + kati_nouns_my(m["k"]) + END


def f_plane_counts(m):
    pre = f"{plane_my(m['p'])}{LOC} " if m["p"] else ""
    body = list_my(m["l"])
    return pre + body + (" ရှိသည်" if m["p"] else "") + END


def f_kati_terms(m):
    return kati_terms_my(m["s"]) + END


def f_statement(m):
    return statement_my(m["s"]) + END


# ---- rebirth (Dhammadassanavāro)
def khane_my(pre):
    """«Kāmadhātuyā» / beings genitive -> «… ပြန်လည် ဖြစ်ပေါ်သည့် ခဏ၌»."""
    if low(pre) in PLANE:
        return f"{plane_my(pre)}{LOC} {KHANE}"
    return f"{beings_my(pre)} {KHANE}"


def patu(sg, q=False):
    return f"{PATU}{'' if sg else 'ကြ'}{'သနည်း' if q else 'သည်'}"


def patu_clause(s):
    """«sabbesaṃ pañcakkhandhā pātubhavanti» / «kassaci §0§ ahetukā pātubhavanti» / «eko khandho pātubhavati – L»."""
    m = re.fullmatch(r"(?:(?P<w>sabbesaṃ|kassaci) )?(?:(?P<ph>§\d+§) )?(?P<np>.+?) (?P<v>pātubhavanti|pātubhavati)"
                     r"(?: – (?P<l>.+))?", s)
    if not m:
        raise Miss("pātubhavati clause: " + s)
    who = (WHO[m["w"]] + " ") if m["w"] else ""
    ph = (m["ph"] + " ") if m["ph"] else ""
    sg = m["v"] == "pātubhavati"
    if m["np"] == "ahetukā":
        body = f"{T['ahetukā'].removesuffix('သော')}ဘဲ"
    else:
        body, _ = np_full(m["np"])
    out = f"{who}{ph}{body} {patu(sg)}"
    if m["l"]:
        out += " – " + list_my(m["l"])
    return out


def f_patu_q(m):            # «X upapattikkhaṇe kati khandhā pātubhavanti…pe… kati cittāni pātubhavanti?»
    return f"{khane_my(m['p'])} {kati_nouns_my(m['k'], verb=True)}{END}"


def f_patu_all(m):          # «X upapattikkhaṇe[, ṭhapetvā …,] clause; clause …»
    head = khane_my(m["p"])
    if m["ex"]:
        head += f"{C} {beings_my(m['ex'])}{THAPETVA}{C}"
    parts = re.split(r"(; )" if "; " in m["c"] else r"(, )", m["c"])
    out = []
    for x in parts:
        if x in ("; ", ", "):
            out.append(C + " ")
        else:
            out.append(patu_clause(x))
    return f"{head} {''.join(out)}{END}"


def f_patu_which(m):        # «X upapattikkhaṇe [sabbesaṃ] katame N pātubhavanti?» / «kassa N pātubhavanti?»
    who = (WHO[m["w"]] + " ") if m["w"] else ""
    n, _ = np_full(m["np"])
    sg = m["v"] == "pātubhavati"
    which = "" if m["w"] == "kassa" else WHICH + " "
    return f"{khane_my(m['p'])} {who}{which}{n} {patu(sg, q=True)}{END}"


def f_patu_these(m):        # «– X upapattikkhaṇe [sabbesaṃ|etesaṃ] ime N pātubhavanti.»
    who = (WHO[m["w"]] + " ") if m["w"] else ""
    n, _ = np_full(m["np"])
    sg = m["v"] == "pātubhavati"
    return f"{khane_my(m['p'])} {who}{DEM}{n} {patu(sg)}"


def f_patu_answer(m):       # «L – X upapattikkhaṇe … ime N pātubhavanti.»
    mm = THESE_RE.fullmatch(m["t"])
    if not mm:
        raise Miss("these: " + m["t"])
    return f"{list_my(m['l'])} – {f_patu_these(mm)}{END}"


def f_beings_patu(m):       # «Beings upapattikkhaṇe N pātubhavanti – L.»
    n, _ = np_full(m["np"])
    sg = m["v"] == "pātubhavati"
    return f"{khane_my(m['b'])} {n} {patu(sg)} – {list_my(m['l'])}{END}"


def f_these_alone(m):
    return f_patu_these(m) + END


def f_avasesa(m):
    return f"ကြွင်းသော သတ္တဝါတို့အား {m['ph']} {T['ahetukā'].removesuffix('သော')}ဘဲ {patu(False)}{END}"


def f_asanna_neg(m):        # «Asaññasattā devā ahetukā anāhārā … pātubhavanti.»
    NEGN = {"ahetukā": HET_N, "anāhārā": AHA_N, "aphassakā": PHA_N, "avedanakā": P1.FEEL,
            "asaññakā": P1.SANNA, "acetanakā": P1.CETANA, "acittakā": P1.MIND}
    ws = m["l"].split(" ")
    if any(w not in NEGN for w in ws):
        raise Miss("asañña: " + m["l"])
    body = f"{C} ".join(f"{NEGN[w]} မရှိ" for w in ws)
    return f"အသညသတ် {DEVA}တို့သည် {body}ဘဲ {patu(False)}{END}"


# ---- life span (Uppādakakamma / Āyuppamāṇa)
def deva_my(s):
    m = DEVA_RE.fullmatch(s)
    if not m:
        raise Miss("deva: " + s)
    return f"{DEVA_NAME[m['n']]} {DEVA}"


def devas_my(s):
    """«asaññasattānañca vehapphalānañca devānaṃ» / «X devānaṃ» -> «A နတ်တို့နှင့် B နတ်တို့»."""
    m = re.fullmatch(r"(?P<a>\S+)ñca (?P<b>\S+)ñca devānaṃ", s)
    if m:
        return f"{deva_my(m['a'] + 'ṃ devānaṃ')}တို့နှင့် {deva_my(m['b'] + 'ṃ devānaṃ')}တို့"
    return deva_my(s) + "တို့"


HUMANS = "လူ"
LIFE = "သက်တမ်း အတိုင်းအတာ"                    # āyuppamāṇa


def f_life_q(m):
    who = {"Manussānaṃ": HUMANS + "တို့", "Tesaṃ": "ထိုသူတို့"}.get(m["w"]) or devas_my(low(m["w"]))
    return f"{who}၏ {LIFE}သည် {KATI} {KATI_END}{END}"


PALI_N = {"paññāsa": 50, "vassāni": None}


def years_my(p):
    """«paññāsa vassāni» / «vassasataṃ» / «dve vassasatāni» / «soḷasa vassasatāni» -> years (int)."""
    m = re.fullmatch(r"(?:(?P<n>\S+) )?vass(?:a(?P<m>sat|sahass))?(?:aṃ|āni)", p)
    if not m:
        raise Miss("years: " + p)
    n = {"paññāsa": 50, "dve": 2, "cattāri": 4, "aṭṭha": 8, "soḷasa": 16, "pañca": 5, None: 1}[m["n"]]
    return n * {"sat": 100, "sahass": 1000, None: 1}[m["m"]]


def f_day(m):               # «Yāni mānusakāni N vassāni, X devānaṃ eso eko rattindivo [§0§].»
    y = years_my(m["y"])
    ph = (" " + m["ph"]) if m["ph"] else ""
    return f"{HUMAN_Y} {num_my(y)}သည် {devas_my(m['d'])}၏ {num_my(1)}ရက် ဖြစ်သည်{ph}{END}"


def f_life_div(m):          # «Tena saṃvaccharena dibbāni pañca vassasatāni X devānaṃ āyuppamāṇaṃ.»
    y = years_my(m["y"])
    return f"ထိုနှစ်ဖြင့် {DIVINE_Y} {num_my(y)}သည် {devas_my(m['d'])}၏ {LIFE} ဖြစ်သည်{END}"


ORD = P1.ORD
LEVEL = {"parittaṃ": f"{T['parittā']} အဆင့်ဖြင့်", "majjhimaṃ": f"{T['majjhimā']} အဆင့်ဖြင့်",
         "paṇītaṃ": f"{T['paṇītā']} အဆင့်ဖြင့်", None: ""}
JHANA = P1.JHANA
WHERE = "မည်သည့်နေရာ၌"                           # kattha
WITH = "နှင့် အတူ"                                # sahabyataṃ (in the company of)


def jhana_my(o, lvl):
    s = f"{ORD[o.lower().removesuffix('ṃ')]} {JHANA}ကို"
    s += (" " + LEVEL[lvl]) if lvl else ""
    return s + " ပွားများ၍"


def f_jhana_q(m):
    return f"{jhana_my(m['o'], m['l'])} {WHERE} {UPAPATTI}ကြသနည်း{END}"


def f_jhana_a(m):
    return f"{jhana_my(m['o'], m['l'])} {devas_my(m['d'])}{WITH} {UPAPATTI}ကြသည်{END}"


FAMILY_N = {"khattiyamahāsālānaṃ": "ကြွယ်ဝသော မင်းမျိုး", "brāhmaṇamahāsālānaṃ": "ကြွယ်ဝသော ပုဏ္ဏားမျိုး",
            "gahapatimahāsālānaṃ": "ကြွယ်ဝသော သူကြွယ်မျိုး"}
SOME = "အချို့တို့သည်"                          # appekacce
NANATTA = {"ārammaṇa": "အာရုံ", "manasikāra": "နှလုံးသွင်းခြင်း", "chanda": "ဆန္ဒ", "paṇidhi": "စိတ်ညွှတ်ခြင်း",
           "adhimokkha": F.ADHIMOKKHA, "abhinīhāra": "ဦးတည် ပို့ဆောင်ခြင်း", "paññā": "ပညာ"}


def company_my(s):
    """«appekacce X sahabyataṃ upapajjanti, appekacce …» -> «အချို့တို့သည် Xနှင့် အတူ ပြန်လည် ဖြစ်ပေါ်ကြသည်၊ …»."""
    out = []
    for c in s.split(", "):
        m = re.fullmatch(r"appekacce (?P<x>.+?) sahabyataṃ upapajjanti", c)
        if not m:
            raise Miss("company: " + c)
        x = FAMILY_N[m["x"]] + "တို့" if m["x"] in FAMILY_N else devas_my(m["x"])
        out.append(f"{SOME} {x}{WITH} {UPAPATTI}ကြသည်")
    return f"{C} ".join(out)


def f_dana_a(m):
    return (f"အလှူကို ပေး၍{C} သီလကို ဆောက်တည်၍{C} ဥပုသ်ကို စောင့်ထိန်း၍ {company_my(m['c'])}{END}")


def f_jhana4(m):
    ws = m["n"].split(" ")
    names = []
    for w in ws:
        k = w.removesuffix("nānattatā")
        if k not in NANATTA:
            raise Miss("nānattatā: " + w)
        names.append(f"{NANATTA[k]} ကွဲပြားခြင်း")
    return f"{jhana_my('catutthaṃ', None)} {f'{C} '.join(names)}တို့ကြောင့် {company_my(m['c'])}{END}"


def kappa_my(p):
    """«Kappassa tatiyo bhāgo» … «Caturāsīti kappasahassānīti» -> Burmese."""
    FIX = {"Kappassa tatiyo bhāgo": f"{KAPPA}၏ သုံးပုံတစ်ပုံ", "Upaḍḍhakappo": f"{KAPPA} {num_my(1)}ဝက်",
           "Kappo §0§": f"{num_my(1)}{KAPPA} §0§"}
    if p in FIX:
        return FIX[p]
    ti = p.endswith("nīti")
    if ti:
        p = p[:-4] + "ni"
    m = re.fullmatch(r"(?:(?P<n>\S+) )?(?P<c>[Kk]app|Pañcakapp)(?:a(?P<m>sahass|sat))?(?:aṃ|āni|ā)", p)
    if not m:
        raise Miss("kappa: " + p)
    nw = {"Dve": 2, "Cattāro": 4, "Aṭṭha": 8, "Soḷasa": 16, "Bāttiṃsa": 32, "Catusaṭṭhi": 64, "Cattāri": 4,
          "Vīsati": 20, "Cattārīsa": 40, "Saṭṭhi": 60, "Caturāsīti": 84, None: 1}
    n = nw[m["n"]] * (5 if m["c"] == "Pañcakapp" else 1) * {"sahass": 1000, "sat": 100, None: 1}[m["m"]]
    if m["m"] is None and m["c"] != "Pañcakapp":
        return f"{num_my(n)}{KAPPA}" + (" ဖြစ်သည်" if ti else "")
    return f"{KAPPA} {num_my(n)}" + (" ဖြစ်သည်" if ti else "")


def f_kappa(m):
    return kappa_my(m["k"]) + END


# ---- frame table (sentence-level, fullmatch; the sentence includes its final mark)
NPX = r"[^?–]+?"
BEINGS = r"(?P<b>[^?–]+?)"
SENT_FRAMES = [
    # sabbasaṅgāhika / uppattānuppatti
    (r"(?:(?P<p>" + PL_ALT + r") )?(?P<k>[Kk]ati \S+(?:, kati \S+|…pe… kati \S+| …pe… kati \S+)*)\?", f_plane_kati),
    (r"(?:(?P<p>" + PL_ALT + r") )?(?P<l>(?:[Pp]añcakkhandhā|cattāro khandhā), [^–?]+)\.", f_plane_counts),
    (r"Tattha katam(?:e|ā|āni|o|aṃ) (?P<np>" + NPX + r")\?", f_tattha_q),
    (r"(?P<l>[^–]+?) – (?:ime|imāni|imā|ayaṃ|idaṃ) (?P<v>vuccanti|vuccati|vuccatti) (?P<q1>\")(?P<x>[^\"]+)\"\.",
     f_list_vuccati),
    (r"(?P<l>[^–]+?)…pe… (?:ime|imāni|imā) (?P<v>vuccanti) \"(?P<x>[^\"]+)\"\.", f_list_pe_vuccati),
    (r"(?:Ime|Imāni|Imā) (?P<v>vuccanti|vuccati) (?P<q1>\")?(?P<x>[^\"]+)\"?\.", f_vuccati),
    (r"(?P<l>[^–]+?) – ime (?P<x>(?:tayo|dve) (?:kusalahetū|akusalahetū|abyākatahetū))\.", f_list_ime),
    (r"(?P<l>(?:Tayo|tayo) [a-zāīūṃṅñṭḍṇḷ]+hetū(?:, (?:tayo|dve) [a-zāīūṃṅñṭḍṇḷ]+hetū)*)\.", f_list_end),
    # pariyāpanna / abhiññeyya / … : kati questions and statements
    (r"(?P<s>(?:Pañcannaṃ khandhānaṃ|Dvādasannaṃ āyatanānaṃ|Aṭṭhārasannaṃ dhātūnaṃ|Catunnaṃ saccānaṃ) kati .+)\?",
     f_kati_terms),
    # rebirth
    (r"(?P<p>" + PL_ALT + r"|Asaññasattānaṃ devānaṃ) upapattikkhaṇe (?P<k>kati \S+ pātubhavanti(?: ?…pe… kati \S+ "
     r"pātubhavanti)*)\?", f_patu_q),
    (r"(?P<p>" + PL_ALT + r") upapattikkhaṇe (?:(?P<w>sabbesaṃ|kassa) )?(?:katam(?:e|ā|āni|o|aṃ) )?(?P<np>[^?]+?) "
     r"(?P<v>pātubhavanti|pātubhavati)[?.]", f_patu_which),
    (r"(?P<l>[^–]+?) – (?P<t>[^–]+?)\.", f_patu_answer),
    (r"(?P<p>" + PL_ALT + r") upapattikkhaṇe (?:(?P<w>etesaṃ|sabbesaṃ) )?(?:ime|imāni|imā|idaṃ|ayaṃ) (?P<np>.+?) "
     r"(?P<v>pātubhavanti|pātubhavati)\.", f_these_alone),
    (BEINGS + r" upapattikkhaṇe (?P<np>[^–]+?) (?P<v>pātubhavanti|pātubhavati) – (?P<l>[^–]+)\.", f_beings_patu),
    (r"Avasesānaṃ sattānaṃ (?P<ph>§\d+§) ahetukā pātubhavanti\.", f_avasesa),
    (r"(?P<p>" + PL_ALT + r"|Asaññasattānaṃ devānaṃ) upapattikkhaṇe(?:, ṭhapetvā (?P<ex>[^,]+),)? (?P<c>.+ "
     r"pātubhava(?:n)?ti.*)\.", f_patu_all),
    (r"Asaññasattā devā (?P<l>.+) pātubhavanti\.", f_asanna_neg),
    # life span
    (r"(?P<w>.+?) kittakaṃ āyuppamāṇaṃ\?", f_life_q),
    (r"(?:Yāni|Yaṃ) mānusak(?:āni|aṃ) (?P<y>.+?), (?P<d>\S+ devānaṃ) eso eko rattindivo(?: (?P<ph>§\d+§))?\.", f_day),
    (r"Tena saṃvaccharena (?:dibbāni|dibbaṃ) (?P<y>.+?) (?P<d>\S+ devānaṃ) āyuppamāṇaṃ\.", f_life_div),
    (r"(?P<o>Paṭhamaṃ|Dutiyaṃ|Tatiyaṃ) jhānaṃ (?P<l>parittaṃ|majjhimaṃ|paṇītaṃ) bhāvetvā kattha upapajjanti\?",
     f_jhana_q),
    (r"(?P<o>Paṭhamaṃ|Dutiyaṃ|Tatiyaṃ) jhānaṃ (?P<l>parittaṃ|majjhimaṃ|paṇītaṃ) bhāvetvā (?P<d>\S+ devānaṃ) "
     r"sahabyataṃ upapajjanti\.", f_jhana_a),
    (r"Dānaṃ datvā, sīlaṃ samādiyitvā, uposathakammaṃ katvā (?P<c>appekacce .+)\.", f_dana_a),
    (r"Catutthaṃ jhānaṃ bhāvetvā (?P<n>\S+nānattatā(?: \S+nānattatā)*) (?P<c>appekacce .+)\.", f_jhana4),
    (r"(?P<k>Kappassa tatiyo bhāgo|Upaḍḍhakappo|Kappo §0§|(?:\S+ )?\S*[Kk]app\S*)\.", f_kappa),
    # generic statement (last)
    (r"(?P<s>[^?–\"]+)\.", f_statement),
]
SENT_FRAMES = [(re.compile(p), f) for p, f in SENT_FRAMES]
THESE_RE = re.compile(r"(?P<p>" + PL_ALT + r") upapattikkhaṇe (?:(?P<w>etesaṃ|sabbesaṃ) )?(?:ime|imāni|imā|idaṃ|ayaṃ) "
                      r"(?P<np>.+?) (?P<v>pātubhavanti|pātubhavati)")
MATIKA8 = ("Kāmāvacarā dhammā, na kāmāvacarā dhammā, rūpāvacarā dhammā, na rūpāvacarā dhammā, arūpāvacarā dhammā, "
           "na arūpāvacarā dhammā, pariyāpannā dhammā, apariyāpannā dhammā.")


def sentence_my(s, lineno):
    if s in P1SENT:
        if len(P1SENT[s]) != 1:
            raise Miss("pi-1 sentence with two Burmese forms: " + s)
        REUSED.append((lineno, s))
        return next(iter(P1SENT[s]))
    if s in DERIVED:
        return DERIVED[s]
    if s in FIXED:
        return FIXED[s]
    if s in COLO:
        return COLO[s]
    if s == MATIKA8:
        items = []
        for it in s[:-1].split(", "):
            items.append(f"{F.term_my(low(it.removesuffix(' dhammā')))} {DHP}")
        return f"{C} ".join(items) + END
    for rx, f in SENT_FRAMES:
        m = rx.fullmatch(s)
        if m:
            try:
                return f(m)
            except Miss:
                if f is f_statement:
                    raise
                continue
    raise Miss("no frame: " + s[:140])


def split_sentences(body):
    """Split at «. » / «? » outside brackets (brackets are placeholders by then)."""
    return [x for x in re.split(r"(?<=[.?]) (?=\S)", body) if x]


def line_my(body, lineno):
    m = F.HEAD_RE.fullmatch(body)
    if m:
        if m["t"] not in HEAD:
            raise Miss("heading: " + body)
        return f"{m['h']} {HEAD[m['t']]}"
    brs = re.findall(r"\[[^\]]+\]", body)
    ph = {}
    for i, b in enumerate(brs):
        body = body.replace(" " + b, f" §{i}§", 1)
        ph[f"§{i}§"] = var_my(b)
    out = []
    for s in split_sentences(body):
        out.append(sentence_my(s, lineno))
    txt = " ".join(out)
    for k, v in ph.items():
        if k not in txt:
            raise Miss(f"placeholder {k} lost")
        txt = txt.replace(k, v)
    if "§" in txt:
        raise Miss("placeholder left")
    return txt


def translate_line(line, lineno):
    if not line.strip():
        return ""
    m = F.ID_RE.search(line)
    body = line[:m.start()] if m else line
    return line_my(body, lineno) + (" " + m.group(1) if m else "")


def main():
    lines = (PALI / NAME).read_text(encoding="utf-8-sig").splitlines()
    done = []
    for i, line in enumerate(lines):
        try:
            done.append(translate_line(line, i + 1))
        except Miss as e:
            part = HERE / "scratch" / ("partial-" + NAME)
            part.parent.mkdir(exist_ok=True)
            part.write_text("\n".join(done) + "\n", encoding="utf-8")
            print(f"STOP {NAME} line {i + 1}: {e}\n  {line[:160]}\n  ({len(done)} lines kept in {part})")
            sys.exit(1)
    txt = unicodedata.normalize("NFC", "\n".join(done).rstrip("\n") + "\n")
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / NAME).write_text(txt, encoding="utf-8")
    print(f"wrote {NAME}: {sum(1 for l in txt.splitlines() if l)} lines; pi-1 sentences reused: {len(REUSED)}")


if __name__ == "__main__":
    main()
