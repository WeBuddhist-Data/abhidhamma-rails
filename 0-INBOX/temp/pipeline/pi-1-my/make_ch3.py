"""Burmese zero-shot of pi-1 chapters 3-01, 3-02, 3-03 (Rūpakaṇḍa: the chapter on matter).

usage: python3 -I -X utf8 make_ch3.py [3-01|3-02|3-03 ...] [--terms]
Every line is generated from the Pāli by my_formulas.translate_cu(): the Mātikā tables (TERMS, FAMILY), the 2-01 tables
(NAMES, SYN, GEN, the frames) and, added here IN MEMORY ONLY (my_formulas.py is not changed), the Rūpakaṇḍa tables and
frames (CU_EXTRA_RULES). A line no rule matches stops the run (my_formulas.Miss), nothing is guessed.
With chapter arguments only those chapters are written; --terms (also done by default) rewrites the generated
«## New terms (generated)» section at the end of notes-ch3.md. Writes nothing else.
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
CHAPTERS = {"3-01": "3-01-rupakandam.md", "3-02": "3-02-rupakandam.md", "3-03": "3-03-rupakandam.md"}
NOTES = HERE / "notes-ch3.md"
TERMS_HEAD = "## New terms (generated)"

Miss = F.Miss
T = F.TERMS
C = F.COMMA
NEW = {}          # every new string, by group, for the notes: group -> [(pāli, burmese)]


def new(group, d, k, v):
    """Add k = v to table d (additive only: an existing different value stops the run) and log it."""
    if k in d and d[k] != v:
        raise SystemExit(f"conflict in table for {k!r}: {d[k]!r} vs {v!r}")
    d[k] = v
    NEW.setdefault(group, []).append((k, v))
    return v


# ===================================================================================== building blocks
RUPA = "ရုပ်"                                   # rūpa = matter (core term)
RUPA_V = F.ARAMMANA["rūpārammaṇaṃ"]             # rūpa = visible form (object of the eye), as rūpārammaṇa
SABBA = "အားလုံး"                                # sabba (all)
MAHABHUTA = "မူလဓာတ်ကြီး"                       # mahābhūta, as in TERMS['upādā'] «မူလဓာတ်ကြီးများကို မှီ၍ ဖြစ်သော»
assert T["upādā"].startswith(MAHABHUTA)
UPADAYA4 = f"{MAHABHUTA} {F.NUM['catu']}{F.CL}ကို မှီ၍"     # catunnaṃ mahābhūtānaṃ upādāya
NISSAYA = "ကို မှီ၍"                             # nissāya (depending on)
ARABBHA = "ကို အာရုံပြု၍"                        # ārabbha (taking as object), cf. ARAMMANA_VA
PASADA = "အာရုံခံ ကြည်လင်မှု"                   # pasāda (sensitivity)
ATTABHAVA = "မိမိ ကိုယ်ခန္ဓာ၌ အကျုံးဝင်သော"        # attabhāvapariyāpanna (included in one's own person)
A_NS = f"{T['anidassanā']}{C} {T['sappaṭighā']}"   # anidassana sappaṭigha (two words)
A_SS = f"{T['sanidassanā']}{C} {T['sappaṭighā']}"  # sanidassana sappaṭigha
A_NSC = T["anidassanasappaṭighā"]                 # anidassanasappaṭigha (one compound)
VANNA = "အရောင်အသွေး"                            # vaṇṇanibhā (colour and appearance)
VATTHU = "မှီရာ"                                  # vatthu (base, support)
VINNATTI = "ထုတ်ဖော်ပြသမှု"                       # viññatti (intimation)
VACA = "စကား"                                    # vācā (speech)
AYATANA = "အာရုံခံ နယ်ပယ်"                       # āyatana (model)
assert F.NAMES["manāyatanaṃ"] == f"{F.MANO} {AYATANA}"
DHATU = "ဓာတ်"
KAMMA = "ပြုခဲ့သော ကံကြောင့် ဖြစ်သော"               # kammassa katattā (because of kamma done)
KIRIYA = F.KIRIYA                                   # kiriyā (merely functional; shared form, consistency pass)
DITTHA, SUTA, MUTA, VINNATA = "မြင်ရသော", "ကြားရသော", "နမ်း မြည်း ထိတွေ့ရသော", "သိရသော"
RUPAKANDA = f"{RUPA} {F.KANDA}"                  # Rūpakaṇḍa
NIDDESA, UDDESA = f"အကျယ် {F.VARA}", f"အကျဉ်း {F.VARA}"   # niddesa (detailed) / uddesa (summary) exposition
SANGAHA = "စုစည်းခြင်း"                          # saṅgaha (grouping), one root with saṅgaṇī «စုစည်းရေတွက်ခြင်း»
PI_THIS = "လည်း ဤသည်ပင်"                         # X petaṃ / peso / pesā (this, too, is X)
OJA = "အဆီအနှစ်"                                 # ojā (nutritive essence)

# number words beyond F.NUM (local, for the eleven groupings and the sixteen-sided shape)
NUMW = {"eka": "တစ်", "du": "နှစ်", "ti": "သုံး", "catub": "လေး", "pañca": "ငါး", "chab": "ခြောက်", "satta": "ခုနစ်",
        "aṭṭha": "ရှစ်", "nava": "ကိုး", "dasa": "ဆယ်", "ekādasa": "ဆယ့်တစ်"}
KIND = "မျိုး"                                   # -vidha (kind)

# ===================================================================================== the senses and their objects
SENSE = {"cakkhu": "မျက်စိ", "sota": "နား", "ghāna": "နှာခေါင်း", "jivhā": "လျှာ", "kāya": "ကိုယ်"}
OBJECT = {"rūpa": RUPA_V, "sadda": F.ARAMMANA["saddārammaṇaṃ"], "gandha": F.ARAMMANA["gandhārammaṇaṃ"],
          "rasa": F.ARAMMANA["rasārammaṇaṃ"], "phoṭṭhabba": F.ARAMMANA["phoṭṭhabbārammaṇaṃ"]}
AYAT_PI = {"cakkhu": "cakkhāyatanaṃ", "sota": "sotāyatanaṃ", "ghāna": "ghānāyatanaṃ", "jivhā": "jivhāyatanaṃ",
           "kāya": "kāyāyatanaṃ", "rūpa": "rūpāyatanaṃ", "sadda": "saddāyatanaṃ", "gandha": "gandhāyatanaṃ",
           "rasa": "rasāyatanaṃ", "phoṭṭhabba": "phoṭṭhabbāyatanaṃ"}
INDR_PI = {"cakkhu": "cakkhundriyaṃ", "sota": "sotindriyaṃ", "ghāna": "ghānindriyaṃ", "jivhā": "jivhindriyaṃ",
           "kāya": "kāyindriyaṃ"}
BOTH = {**SENSE, **OBJECT}
ELEM = {"pathavīdhātu": "မြေဓာတ်", "āpodhātu": "ရေဓာတ်", "tejodhātu": "မီးဓာတ်", "vāyodhātu": "လေဓာတ်",
        "ākāsadhātu": f"ဟင်းလင်းပြင် {DHATU}"}
FEM, MASC = "မိန်းမ", "ယောက်ျား"

# ---- nouns (answers of the questions, list items): F.NAMES
NOUN = {}
for k, my in BOTH.items():
    NOUN[AYAT_PI[k]] = f"{my} {AYATANA}"
    NOUN[k + "dhātu"] = f"{my} {DHATU}"
for k, my in SENSE.items():
    NOUN[INDR_PI[k]] = F._ix(my, F.INDRIYA)
NOUN.update(ELEM)
NOUN.update({
    "itthindriyaṃ": F._ix(FEM, F.INDRIYA), "purisindriyaṃ": F._ix(MASC, F.INDRIYA),
    "kāyaviññatti": f"{SENSE['kāya']}ဖြင့် {VINNATTI}", "vacīviññatti": f"နှုတ်ဖြင့် {VINNATTI}",
    "rūpassa lahutā": f"{RUPA}၏ {F.SYN['lahutā']}", "rūpassa mudutā": f"{RUPA}၏ {F.SYN['mudutā']}",
    "rūpassa kammaññatā": f"{RUPA}၏ {F.SYN['kammaññatā']}", "rūpassa upacayo": f"{RUPA}၏ တိုးပွားခြင်း",
    "rūpassa santati": f"{RUPA}၏ ဆက်လက်ဖြစ်ပေါ်ခြင်း", "rūpassa jaratā": f"{RUPA}၏ အိုမင်းခြင်း",
    "rūpassa aniccatā": f"{RUPA}၏ မမြဲခြင်း", "kabaḷīkāro āhāro": f"လုတ်ပြု၍ စားရသော {F.AHARA}",
    # the tangible (phoṭṭhabba) list and the earth-element list
    "kakkhaḷaṃ": "ကြမ်းတမ်းသောအရာ", "mudukaṃ": "ပျော့ပျောင်းသောအရာ", "saṇhaṃ": "ချောမွေ့သောအရာ",
    "pharusaṃ": "ဖုထစ်သောအရာ", "sukhasamphassaṃ": f"ထိတွေ့ရ {F.SUKHA}သောအရာ",
    "dukkhasamphassaṃ": f"ထိတွေ့ရ {F.DUKKHA}သောအရာ", "garukaṃ": "လေးလံသောအရာ", "lahukaṃ": "ပေါ့ပါးသောအရာ",
    # edible food
    "odano": "ထမင်း", "kummāso": "ဆန်ပြုတ်", "sattu": "မုယောမှုန့်", "maccho": "ငါး", "maṃsaṃ": "အသား",
    "khīraṃ": "နွားနို့", "dadhi": "နို့ချဉ်", "sappi": "ထောပတ်ကြည်", "navanītaṃ": "ထောပတ်", "telaṃ": "ဆီ",
    "madhu": "ပျားရည်", "phāṇitaṃ": "တင်လဲ",
})
for k, v in NOUN.items():
    new("Nouns (names of matter, list items)", F.NAMES, k, v)

# ---- predicates of «Katamaṃ taṃ rūpaṃ P / Atthi rūpaṃ P / idaṃ taṃ rūpaṃ P»: attributive Burmese before «ရုပ်»
PRED = {}
GENW = {}         # genitive members of a «…pe…» chain (cakkhusamphassajāya vedanāya…pe… saññāya…)


def noun_pred(pali, my):
    PRED[pali] = f"{my} ဖြစ်သော"
    PRED["na " + pali] = f"{my} မဟုတ်သော"


LIST_ONLY = ("kakkhaḷaṃ", "mudukaṃ", "saṇhaṃ", "pharusaṃ", "sukhasamphassaṃ", "dukkhasamphassaṃ", "garukaṃ",
             "lahukaṃ", "odano", "kummāso", "sattu", "maccho", "maṃsaṃ", "khīraṃ", "dadhi", "sappi", "navanītaṃ",
             "telaṃ", "madhu", "phāṇitaṃ")        # nouns that are never a predicate of «… taṃ rūpaṃ»
for k in list(NOUN):
    if k in LIST_ONLY:
        continue
    if k.startswith("rūpassa "):
        PRED[k] = f"{NOUN[k]} ဖြစ်သော"
        PRED["rūpassa na " + k[8:]] = f"{NOUN[k]} မဟုတ်သော"
        continue
    noun_pred(k, NOUN[k])
noun_pred("jīvitindriyaṃ", F.NAMES["jīvitindriyaṃ"])
noun_pred("indriyaṃ", F.INDRIYA)
noun_pred("mahābhūtaṃ", MAHABHUTA)
noun_pred("viññatti", VINNATTI)
for k, my in SENSE.items():
    ph, vi = f"{my}၏ {F.PHASSA}", f"{my} {F.VINNANA}"
    GENW[k + "samphassassa"] = ph + "၏"
    GENW[k + "samphassajāya vedanāya"] = f"{ph}မှ ဖြစ်ပေါ်သော {F.FEEL}၏"
    for pre, my2 in ((k + "samphassassa", ph), (k + "viññāṇassa", vi)):
        PRED[pre + " vatthu"] = f"{my2}၏ {VATTHU} ဖြစ်သော"
        PRED[pre + " na vatthu"] = f"{my2}၏ {VATTHU} မဟုတ်သော"
        PRED[pre + " ārammaṇaṃ"] = f"{my2}၏ အာရုံ ဖြစ်သော"
        PRED[pre + " na ārammaṇaṃ"] = f"{my2}၏ အာရုံ မဟုတ်သော"
        PRED[pre + " nārammaṇaṃ"] = PRED[pre + " na ārammaṇaṃ"]       # na + ārammaṇaṃ (sandhi)
GENW["saññāya"] = F.SANNA + "၏"
GENW["cetanāya"] = F.CETANA + "၏"
# adjectives of the Mātikā (TERMS, neuter singular -> the plural key of the sample)
for neut, pl in {"upādā": "upādā", "no upādā": "no upādā", "upādiṇṇaṃ": "upādiṇṇā", "anupādiṇṇaṃ": "anupādiṇṇā",
                 "upādiṇṇupādāniyaṃ": "upādiṇṇupādāniyā", "anupādiṇṇupādāniyaṃ": "anupādiṇṇupādāniyā",
                 "sanidassanaṃ": "sanidassanā", "anidassanaṃ": "anidassanā", "sappaṭighaṃ": "sappaṭighā",
                 "appaṭighaṃ": "appaṭighā", "ajjhattikaṃ": "ajjhattikā", "bāhiraṃ": "bāhirā",
                 "cittasamuṭṭhānaṃ": "cittasamuṭṭhānā", "na cittasamuṭṭhānaṃ": "no cittasamuṭṭhānā",
                 "cittasahabhu": "cittasahabhuno", "na cittasahabhu": "no cittasahabhuno",
                 "cittānuparivatti": "cittānuparivattino", "na cittānuparivatti": "no cittānuparivattino",
                 "anidassanaappaṭighaṃ": "anidassanaappaṭighā", "anidassanaṃ appaṭighaṃ": "anidassanaappaṭighā"}.items():
    v = T[pl]
    PRED[neut] = v if v.endswith("သော") else v + " ဖြစ်သော"
SUKHUMA = "နုညံ့သော"
PRED.update({
    "oḷārikaṃ": "ရုန့်ရင်းသော", "sukhumaṃ": SUKHUMA, "dūre": "အဝေး၌ ရှိသော", "santike": "အနီး၌ ရှိသော",
    "sukhasamphassaṃ": f"ထိတွေ့ရ {F.SUKHA}သော", "dukkhasamphassaṃ": f"ထိတွေ့ရ {F.DUKKHA}သော",
    "dhammāyatanapariyāpannaṃ": f"{F.NAMES['dhammāyatanaṃ']}၌ အကျုံးဝင်သော",
})
assert PRED["sukhasamphassaṃ"] + "အရာ" == NOUN["sukhasamphassaṃ"]
VINNEYYA = {k + "viññeyyaṃ": f"{my}ဖြင့် သိနိုင်သော" for k, my in SENSE.items()}
VINNEYYA.update({"manoviññeyyaṃ": f"{F.MANO}ဖြင့် သိနိုင်သော",
                 "manodhātuviññeyyaṃ": f"{F.MANO} {DHATU}ဖြင့် သိနိုင်သော",
                 "manoviññāṇadhātuviññeyyaṃ": f"{F.NAMES['manoviññāṇadhātu']}ဖြင့် သိနိုင်သော"})
for k, v in {**PRED, **VINNEYYA}.items():
    if k not in NOUN and not k.startswith(("na ", "rūpassa na ")) and "vatthu" not in k and "ārammaṇaṃ" not in k:
        NEW.setdefault("Predicates (attributive before «ရုပ်»)", []).append((k, v))
for k, v in GENW.items():
    NEW.setdefault("Genitive members of «…pe…» chains", []).append((k, v))
NEW.setdefault("Predicate patterns", []).extend([
    ("X (noun) as predicate", "X ဖြစ်သော"), ("na X", "X မဟုတ်သော"),
    ("Csamphassassa vatthu / na vatthu", f"C၏ {F.PHASSA}၏ {VATTHU} ဖြစ်သော / မဟုတ်သော"),
    ("Cviññāṇassa ārammaṇaṃ / nārammaṇaṃ", f"C {F.VINNANA}၏ အာရုံ ဖြစ်သော / မဟုတ်သော"),
    ("Csamphassajāya vedanāya", f"C၏ {F.PHASSA}မှ ဖြစ်ပေါ်သော {F.FEEL}၏"),
    ("rūpassa X / rūpassa na X", f"{RUPA}၏ X ဖြစ်သော / မဟုတ်သော"),
])

# ---- the ekaka list (Sabbaṃ rūpaṃ na hetu, ahetukaṃ, …): neuter singular -> TERMS plural key
EKA_SPECIAL = {"na hetu": "na hetū", "rūpaṃ": "rūpino", "neva ācayagāmi na apacayagāmi": "nevācayagāmināpacayagāmino",
               "nevasekkhanāsekkhaṃ": "nevasekkhanāsekkhā"}
EKA_NEW = {"aniccaṃ": "မမြဲသော", "jarābhibhūtaṃ": "အိုခြင်း လွှမ်းမိုးခံရသော",
           "chahi viññāṇehi viññeyyaṃ": f"{F.VINNANA} {F.NUM['cha']}{F.CL}ဖြင့် သိနိုင်သော"}
for k, v in EKA_NEW.items():
    NEW.setdefault("Ekaka predicates", []).append((k, v))


def eka_attr(item):
    """One ekaka member (neuter singular, without «-meva») -> Burmese attributive «…သော»."""
    if item in EKA_NEW:
        return EKA_NEW[item]
    if item in EKA_SPECIAL:
        return T[EKA_SPECIAL[item]]
    neg = re.match(r"(na|no) (.+)$", item)
    base = neg[2] if neg else item
    if not base.endswith("aṃ"):
        raise Miss("ekaka: " + item)
    pl = base[:-2] + "ā"
    if neg:
        for k in (f"{neg[1]} {pl}", f"na {pl}", f"no {pl}"):
            if k in T:
                return T[k]
        return F.no_(T[pl])
    if pl not in T:
        raise Miss("ekaka term: " + item)
    return T[pl]


def stem(x):
    if not x.endswith("သော"):
        raise Miss("stem: " + x)
    return x[:-3]


def r_ekaka(m):
    """«Sabbaṃ rūpaṃ A, B, …» (eva = False) or «… A-meva, B-meva …» -> «ရုပ် အားလုံးသည် A၊ B၊ … Zသည်» / «…သည်ပင်»."""
    items = m["l"].split(", ")
    eva = items[0].endswith("meva")
    out = []
    for it in items:
        vm = re.fullmatch(r"(.+?) (\[[^\]]+\])", it)
        var = " " + F.var_my(vm[2]) if vm else ""
        it = vm[1] if vm else it
        if eva:
            if not it.endswith("meva"):
                raise Miss("eva: " + it)
            it = it[:-5] + "aṃ" if it.endswith("ameva") else it[:-4]
        two = re.fullmatch(r"(uppannaṃ) (chahi viññāṇehi viññeyyaṃ)", it)
        if two:                                         # ^1-594: «uppannaṃ chahi viññāṇehi viññeyyameva» (one member)
            s = f"{stem(T['uppannā'])}၍ {stem(eka_attr(two[2]))}"
        else:
            s = stem(eka_attr(it))
        out.append([s, var])
    for j, (s, var) in enumerate(out):
        if eva:
            out[j] = s + "သည်ပင်" + var
        else:
            out[j] = s + ("သည်" if j == len(out) - 1 else "") + var
    return f"{RUPA} {SABBA}သည် " + f"{C} ".join(out)


# ===================================================================================== the predicate chain
def _alt(keys):
    return "(?:" + "|".join(re.escape(k) for k in sorted(keys, key=len, reverse=True)) + ")"


NA = F.NA
UNIT = _alt(list(PRED) + list(GENW)) + NA
VAR = r"(?: \[[^\]]+\])?"
CHAIN = rf"{UNIT}{VAR}(?:(?: ?…pe… | ){UNIT}{VAR})*"
_STEP = re.compile(rf"(?P<sep> ?…pe… | |)(?P<u>{UNIT})(?: (?P<v>\[[^\]]+\]))?")


def chain_my(s):
    """«bāhiraṃ cakkhusamphassajāya vedanāya…pe… saññāya…pe… cakkhuviññāṇassa na vatthu» -> Burmese attributive."""
    pos, out, prev_gen = 0, "", False
    while pos < len(s):
        m = _STEP.match(s, pos)
        if not m or m.end() == pos:
            raise Miss("chain: " + s[pos:pos + 60])
        u = m["u"]
        my = GENW[u] if u in GENW else PRED[u]
        if m["sep"].strip():
            out += F.PE + " "
        elif m["sep"]:
            out += " " if prev_gen else C + " "
        out += my + (" " + F.var_my(m["v"]) if m["v"] else "")
        prev_gen = u in GENW
        pos = m.end()
    if prev_gen:
        raise Miss("chain ends in a genitive: " + s)
    return out


# ===================================================================================== the sense clauses (3-02, 3-03)
ORG = {   # organ: Pāli forms by case
    "cakkhu": dict(nom=["cakkhu", "cakkhuṃ"], acc=["cakkhuṃ"], ins=["cakkhunā"], loc=["cakkhumhi"]),
    "sota": dict(nom=["sotaṃ"], acc=["sotaṃ"], ins=["sotena"], loc=["sotamhi"]),
    "ghāna": dict(nom=["ghānaṃ"], acc=["ghānaṃ"], ins=["ghānena"], loc=["ghānamhi"]),
    "jivhā": dict(nom=["jivhā"], acc=["jivhaṃ"], ins=["jivhāya"], loc=["jivhāya"]),
    "kāya": dict(nom=["kāyo"], acc=["kāyaṃ"], ins=["kāyena"], loc=["kāyamhi"]),
}
OBJ = {
    "rūpa": dict(nom=["rūpaṃ"], acc=["rūpaṃ"], loc=["rūpamhi"]),
    "sadda": dict(nom=["saddo"], acc=["saddaṃ"], loc=["saddamhi"]),
    "gandha": dict(nom=["gandho"], acc=["gandhaṃ"], loc=["gandhamhi"]),
    "rasa": dict(nom=["raso"], acc=["rasaṃ"], loc=["rasamhi"]),
    "phoṭṭhabba": dict(nom=["phoṭṭhabbo"], acc=["phoṭṭhabbaṃ"], loc=["phoṭṭhabbamhi"]),
}
CASE_MY = {"ins": "ဖြင့်", "loc": "၌", "nom": "သည်", "acc": "ကို"}
VERBS = {   # Pāli stem of the four forms -> Burmese verb
    ("passi", "passati", "passissati", "passe"): "မြင်",
    ("suṇi", "suṇāti", "suṇissati", "suṇe"): "ကြား",
    ("ghāyi", "ghāyati", "ghāyissati", "ghāye"): "နမ်း",
    ("sāyi", "sāyati", "sāyissati", "sāye"): "မြည်း",
    ("phusi", "phusati", "phusissati", "phuse"): "ထိ",
    ("paṭihaññi", "paṭihaññati", "paṭihaññissati", "paṭihaññe"): "ထိခိုက်",
    ("uppajji", "uppajjati", "uppajjissati", "uppajje"): "ဖြစ်ပေါ်",
}
V4 = {" vā ".join(k) + " vā": v for k, v in VERBS.items()}
V4_RE = _alt(V4)


def v4_my(p):
    v = V4[p]
    return f"{C} ".join(f"{v}{e}ဖြစ်စေ" for e in ("ခဲ့သည်", "သည်", "လိမ့်မည်", "နိုင်သည်"))


NEW.setdefault("Verbs (four tenses «X-i vā X-ati vā X-issati vā X-e vā»)", []).extend(
    [(" vā ".join(k) + " vā", v4_my(" vā ".join(k) + " vā")) for k in VERBS])
ADJ = r"(?:anidassanasappaṭighaṃ|(?:an|san)idassan\w+ sappaṭigh\w+)"


def adj_my(a):
    if a == "anidassanasappaṭighaṃ":
        return A_NSC
    return A_NS if a.startswith("an") else A_SS


def forms(w):
    """[(kind, key, case)] for a Pāli word form of an organ or an object."""
    out = []
    for kind, tab in (("org", ORG), ("obj", OBJ)):
        for key, d in tab.items():
            for case, fs in d.items():
                if w in fs:
                    out.append((kind, key, case))
    return out


def r_sense(m):
    """«yena cakkhunā ADJ rūpaṃ ADJ passi vā …» and the other five orders -> Burmese (instr./loc. phrase first)."""
    strike = V4[m["v"]] == "ထိခိုက်"
    allowed = ("loc", "nom") if strike else ("ins", "acc")
    words = []
    for w, a in ((m["w1"], m["a1"]), (m["w2"], m["a2"])):
        c = [f for f in forms(w) if f[2] in allowed]
        if len({(k, key) for k, key, _ in c}) != 1:
            raise Miss("sense word: " + w)
        words.append((c, a))
    (c1, a1), (c2, a2) = words
    kinds = {c1[0][0], c2[0][0]}
    if kinds != {"org", "obj"}:
        raise Miss("sense clause: " + m[0])
    case1 = {f[2] for f in c1}
    case2 = {f[2] for f in c2}
    if case1 == set(allowed):                 # both cases possible for w1: decide by w2
        case1 = set(allowed) - case2
    if case2 == set(allowed):
        case2 = set(allowed) - case1
    if len(case1) != 1 or len(case2) != 1 or case1 == case2:
        raise Miss("sense cases: " + m[0])
    ph = []
    for c, a, case, first in ((c1, a1, case1.pop(), True), (c2, a2, case2.pop(), False)):
        my = BOTH[c[0][1]]
        ph.append((case, ("ထို " if first else "") + f"{adj_my(a)} {my}{CASE_MY[case]}"))
    ph.sort(key=lambda x: 0 if x[0] in ("ins", "loc") else 1)
    return f"{ph[0][1]} {ph[1][1]} {v4_my(m['v'])}"


CACC = _alt([d["acc"][0] for d in ORG.values()])
OACC = _alt([d["acc"][0] for d in OBJ.values()])
ARM2OBJ = {}
for _k in OBJ:
    for _e in ("ārammaṇo", "ārammaṇā"):
        ARM2OBJ[_k[:-1] + _e] = _k                 # rūpārammaṇo, saddārammaṇā …
OARM = _alt(ARM2OBJ)
SAMPH = _alt([k + "samphasso" for k in SENSE])
SAMPHJ = _alt([k + "samphassajā" for k in SENSE])
V4U = re.escape([k for k, v in V4.items() if v == "ဖြစ်ပေါ်"][0])
ACC2ORG = {d["acc"][0]: k for k, d in ORG.items()}
ACC2OBJ = {d["acc"][0]: k for k, d in OBJ.items()}


def _rest(m, c):
    if m["s"]:
        if m["s"] != c + "samphasso":
            raise Miss("samphassa: " + m[0])
        return f"{SENSE[c]}၏ {F.PHASSA} {v4_my(m['v'])}"
    if m["sj"] != c + "samphassajā":
        raise Miss("samphassajā: " + m[0])
    return f"{SENSE[c]}၏ {F.PHASSA}မှ ဖြစ်ပေါ်သော {F.FEEL}"


def _obj(m):
    if m["o"]:
        return ACC2OBJ[m["o"]], False
    return ARM2OBJ[m["oa"]], True


def r_nis_org(m):
    """«yaṃ cakkhuṃ nissāya rūpaṃ ārabbha / rūpārammaṇo(ā) …»."""
    c = ACC2ORG[m["c"]]
    o, arm = _obj(m)
    mid = f"{OBJECT[o]}{F.TAKES}" if arm else f"{OBJECT[o]}{ARABBHA}"
    return f"ထို {SENSE[c]}{NISSAYA} {mid} {_rest(m, c)}"


def r_nis_obj(m):
    """«yaṃ rūpaṃ ārabbha cakkhuṃ nissāya …» / «yaṃ rūpārammaṇo(ā) cakkhuṃ nissāya …»."""
    c = ACC2ORG[m["c"]]
    o, arm = _obj(m)
    if arm:
        return f"{SENSE[c]}{NISSAYA} ထို {OBJECT[o]}{F.TAKES} {_rest(m, c)}"
    return f"ထို {OBJECT[o]}{ARABBHA} {SENSE[c]}{NISSAYA} {_rest(m, c)}"


def r_vinnana(m):
    return f"{SENSE[m['c']]} {F.VINNANA} {v4_my(m['v'])}"


# the organ head «Yaṃ cakkhu catunnaṃ mahābhūtānaṃ upādāya pasādo [attabhāvapariyāpanno anidassano sappaṭigho]»
ORG_NOM = {"cakkhu": "cakkhu", "sotaṃ": "sota", "ghānaṃ": "ghāna", "jivhā": "jivhā", "kāyo": "kāya"}


def r_org_head(m):
    c = ORG_NOM[m["c"]]
    var = " " + F.var_my(m["v"]) if m["v"] else ""
    full = f"{C} {ATTABHAVA}{C} {A_NS}" if m["full"] else ""
    return f"{UPADAYA4} ဖြစ်သော {PASADA} ဖြစ်သည့်{full} {SENSE[c]}{var}"


# the object heads with their lists of kinds
COLOUR = {"nīlaṃ": "အပြာ", "pītakaṃ": "အဝါ", "lohitakaṃ": "အနီ", "odātaṃ": "အဖြူ", "kāḷakaṃ": "အမည်း",
          "mañjiṭṭhakaṃ": "ကြက်သွေးရောင်", "hari": "အစိမ်း", "harivaṇṇaṃ": "အစိမ်းနှင့် တူသော အရောင်",
          "ambaṅkuravaṇṇaṃ": "သရက်ညွန့် အရောင်", "dīghaṃ": "အရှည်", "rassaṃ": "အတို", "aṇuṃ": "အသေး",
          "thūlaṃ": "အကြီး", "vaṭṭaṃ": "အဝိုင်း", "parimaṇḍalaṃ": "စက်ဝိုင်းပုံ", "caturaṃsaṃ": "လေးထောင့်ပုံ",
          "chaḷaṃsaṃ": "ခြောက်ထောင့်ပုံ", "aṭṭhaṃsaṃ": "ရှစ်ထောင့်ပုံ", "soḷasaṃsaṃ": "ဆယ့်ခြောက်ထောင့်ပုံ",
          "ninnaṃ": "နိမ့်ရာ", "thalaṃ": "မြင့်ရာ", "chāyā": "အရိပ်", "ātapo": "နေရောင်", "āloko": "အလင်း",
          "andhakāro": "အမှောင်", "abbhā": "တိမ်", "mahikā": "မြူ", "dhūmo": "မီးခိုး", "rajo": "ဖုန်"}
COLOUR_GEN = {"candamaṇḍalassa": "လဝန်း၏", "sūriyamaṇḍalassa": "နေဝန်း၏", "tārakarūpānaṃ": "ကြယ်တို့၏",
              "ādāsamaṇḍalassa": "မှန်ဝန်း၏", "maṇisaṅkhamuttāveḷuriyassa": "ကျောက်မျက် ခရုသင်း ပုလဲ ကြောင်မျက်ရွဲတို့၏",
              "jātarūparajatassa": "ရွှေ ငွေတို့၏"}
SOUND = {"bherisaddo": "စည်ကြီးသံ", "mudiṅgasaddo": "ဗုံသံ", "saṅkhasaddo": "ခရုသင်းသံ", "paṇavasaddo": "စည်ငယ်သံ",
         "gītasaddo": "သီချင်းသံ", "vāditasaddo": "တီးမှုတ်သံ", "sammasaddo": "လင်းကွင်းသံ", "pāṇisaddo": "လက်ခုပ်သံ",
         "sattānaṃ nigghosasaddo": "သတ္တဝါတို့၏ ဆူညံသံ", "dhātūnaṃ sannighātasaddo": f"{DHATU}တို့ ရိုက်ခတ်သံ",
         "vātasaddo": "လေတိုက်သံ", "udakasaddo": "ရေသံ", "manussasaddo": "လူသံ",
         "amanussasaddo": "လူ မဟုတ်သူတို့၏ အသံ"}
SMELL = {"mūlagandho": "အမြစ် အနံ့", "sāragandho": "အနှစ် အနံ့", "tacagandho": "အခေါက် အနံ့", "pattagandho": "အရွက် အနံ့",
         "pupphagandho": "ပန်း အနံ့", "phalagandho": "အသီး အနံ့", "āmakagandho": "အစိမ်း အနံ့",
         "vissagandho": "ပုပ်သိုး အနံ့", "sugandho": "မွှေးသော အနံ့", "duggandho": "နံစော်သော အနံ့"}
TASTE = {"mūlaraso": "အမြစ် အရသာ", "khandharaso": "ပင်စည် အရသာ", "tacaraso": "အခေါက် အရသာ", "pattaraso": "အရွက် အရသာ",
         "puppharaso": "ပန်း အရသာ", "phalaraso": "အသီး အရသာ", "ambilaṃ": "အချဉ်", "madhuraṃ": "အချို",
         "tittakaṃ": "အခါး", "kaṭukaṃ": "အစပ်", "loṇikaṃ": "အငန်", "khārikaṃ": "ပြာရည် အရသာ", "lambilaṃ": "အချဉ်စူး",
         "kasāvo": "အဖန်", "sādu": "စားကောင်းသော အရသာ", "asādu": "စားမကောင်းသော အရသာ"}
for g, d in (("Visible-form list (rūpāyatana)", COLOUR), ("Visible-form list: «X vaṇṇanibhā»", COLOUR_GEN),
             ("Sound list (saddāyatana)", SOUND), ("Smell list (gandhāyatana)", SMELL),
             ("Taste list (rasāyatana)", TASTE)):
    NEW.setdefault(g, []).extend((k, (v + " " + VANNA) if d is COLOUR_GEN else v) for k, v in d.items())
for k in ("mañjeṭṭhakaṃ", "caturassaṃ", "suriyamaṇḍalassa"):
    F.VAR_KIND.setdefault(k, F.LEKHANA)
F.VAR_KIND.setdefault("lapilakaṃ", F.PATHA)


def kinds_my(text, table, gens=None):
    """A space-separated list of kinds (variants after a word) -> «A၊ B၊ …»; two kinds never share a Burmese value."""
    toks = re.findall(r"\[[^\]]*\]|[^\s\[]+", text)
    out, seen, i = [], {}, 0
    while i < len(toks):
        t = toks[i]
        if t.startswith("["):
            if not out:
                raise Miss("variant first: " + text[:60])
            out[-1] += " " + F.var_my(t)
            i += 1
            continue
        two = " ".join(toks[i:i + 2])
        if two in table:
            key, my, i = two, table[two], i + 2
        elif t in table:
            key, my, i = t, table[t], i + 1
        elif gens and t in gens:
            j = i + 1
            var = ""
            if j < len(toks) and toks[j].startswith("["):
                var = " " + F.var_my(toks[j])
                j += 1
            if j >= len(toks) or toks[j] != "vaṇṇanibhā":
                raise Miss("vaṇṇanibhā: " + t)
            key, my, i = t, f"{gens[t]}{var} {VANNA}", j + 1
        else:
            raise Miss("kind: " + t + " in " + text[:60])
        base = my.split(" [")[0]
        if base in seen and seen[base] != key:
            raise Miss(f"two kinds share «{base}»")
        seen[base] = key
        out.append(my)
    return f"{C} ".join(out)


OBJ_NOM = {"saddo": ("sadda", SOUND), "gandho": ("gandha", SMELL), "raso": ("rasa", TASTE)}


def r_colour_head(m):
    if m["l"] is None:
        return f"{UPADAYA4} ဖြစ်သော {VANNA} ဖြစ်သည့် {RUPA_V}"
    return f"{UPADAYA4} ဖြစ်သော {VANNA} ဖြစ်သည့်{C} {A_SS} {RUPA_V}မှာ {kinds_my(m['l'], COLOUR, COLOUR_GEN)}"


def r_obj_head(m):
    o, tab = OBJ_NOM[m["o"]]
    return f"{UPADAYA4} ဖြစ်သော{C} {A_NS} {OBJECT[o]}မှာ {kinds_my(m['l'], tab)}"


def r_obj_other(m):
    if m["o"] == "rūpaṃ":
        return f"{UPADAYA4} ဖြစ်သော {VANNA} ဖြစ်သည့်{C} {A_SS} အခြား {RUPA_V} ရှိသမျှလည်း"
    return f"{UPADAYA4} ဖြစ်သော{C} {A_NS} အခြား {OBJECT[OBJ_NOM[m['o']][0]]} ရှိသမျှလည်း"


# «X petaṃ / peso / pesā» (this, too, is X)
PI = {"cakkhuṃ": SENSE["cakkhu"], "sotaṃ": SENSE["sota"], "ghānaṃ": SENSE["ghāna"], "jivhā": SENSE["jivhā"],
      "kāyo": SENSE["kāya"], "rūpaṃ": RUPA_V, "saddo": OBJECT["sadda"], "gandho": OBJECT["gandha"],
      "raso": OBJECT["rasa"], "phoṭṭhabbo": OBJECT["phoṭṭhabba"],
      "loko": "လောက", "dvārā": "တံခါး", "samuddo": "သမုဒ္ဒရာ", "paṇḍaraṃ": F.SYN["paṇḍaraṃ"],
      "khettaṃ": "လယ်ကွင်း", "vatthuṃ": VATTHU, "nettaṃ": "လမ်းပြ", "nayanaṃ": "ခေါင်းဆောင်",
      "orimaṃ tīraṃ": "ဤဘက်ကမ်း", "suñño gāmo": "ဆိတ်သုဉ်းသော ရွာ"}
for k, my in BOTH.items():
    PI[AYAT_PI[k]] = NOUN[AYAT_PI[k]]
    PI[k + "dhātu"] = NOUN[k + "dhātu"]
for k in SENSE:
    PI[INDR_PI[k]] = NOUN[INDR_PI[k]]
NEW.setdefault("«X petaṃ / peso / pesā» (this, too, is X)", []).extend(
    [("X petaṃ / peso / pesā", "X" + PI_THIS)] +
    [(k, v) for k, v in PI.items() if k in ("loko", "dvārā", "samuddo", "khettaṃ", "vatthuṃ", "nettaṃ", "nayanaṃ",
                                            "orimaṃ tīraṃ", "suñño gāmo")])
PI_ITEM = rf"{_alt(PI)} ?pe(?:taṃ|so|sā)"
_PI_ONE = re.compile(rf"(?P<k>{_alt(PI)}) ?pe(?:taṃ|so|sā)")


def r_pi(m):
    return f"{C} ".join(PI[x["k"]] + PI_THIS for x in _PI_ONE.finditer(m[0]))


# ===================================================================================== other definitions
SYN_NEW = {
    # itthindriya / purisindriya
    "itthiliṅgaṃ": f"{FEM} အသွင်သဏ္ဌာန်", "itthinimittaṃ": f"{FEM} အမှတ်အသား", "itthikuttaṃ": f"{FEM} အမူအရာ",
    "itthākappo": f"{FEM} ဟန်ပန်", "itthattaṃ": f"{FEM} ဖြစ်သော အဖြစ်", "itthibhāvo": f"{FEM} ဖြစ်သော သဘော",
    "purisaliṅgaṃ": f"{MASC} အသွင်သဏ္ဌာန်", "purisanimittaṃ": f"{MASC} အမှတ်အသား", "purisakuttaṃ": f"{MASC} အမူအရာ",
    "purisākappo": f"{MASC} ဟန်ပန်", "purisattaṃ": f"{MASC} ဖြစ်သော အဖြစ်", "purisabhāvo": f"{MASC} ဖြစ်သော သဘော",
    # kāyaviññatti / vacīviññatti
    "thambhanā": "တောင့်တင်းခြင်း", "santhambhanā": "ကောင်းစွာ တောင့်တင်းခြင်း",
    "santhambhitattaṃ": "ကောင်းစွာ တောင့်တင်းထားသော အဖြစ်", "viññatti": VINNATTI, "viññāpanā": "ထုတ်ဖော်ပြသခြင်း",
    "viññāpitattaṃ": "ထုတ်ဖော်ပြသထားသော အဖြစ်",
    "vācā": VACA, "girā": "စကားသံ", "byappatho": "ပြောဆိုပုံ", "udīraṇaṃ": "ရွတ်ဆိုခြင်း", "ghoso": "အသံဗလံ",
    "ghosakammaṃ": "အသံ ထုတ်ခြင်း", "vacībhedo": "နှုတ်မှ စကား ကွဲထွက်ခြင်း",
    # ākāsadhātu
    "ākāso": "ဟင်းလင်းပြင်", "ākāsagataṃ": "ဟင်းလင်းပြင် သဘော ရှိသောအရာ", "aghaṃ": "ဗလာ",
    "aghagataṃ": "ဗလာ သဘော ရှိသောအရာ", "vivaro": "အပေါက်", "vivaragataṃ": "အပေါက် သဘော ရှိသောအရာ",
    "asamphuṭṭhaṃ catūhi mahābhūtehi": f"{MAHABHUTA} {F.NUM['catu']}{F.CL}နှင့် မထိတွေ့သောအရာ",
    # jaratā, aniccatā
    "jarā": "အိုခြင်း", "jīraṇatā": "ဆွေးမြေ့ခြင်း", "khaṇḍiccaṃ": "သွားကျိုးခြင်း", "pāliccaṃ": "ဆံပင်ဖြူခြင်း",
    "valittacatā": "အရေတွန့်ခြင်း", "āyuno saṃhāni": f"{F.SYN['āyu']} ယုတ်လျော့ခြင်း",
    "indriyānaṃ paripāko": f"{F.INDRIYA}တို့ ရင့်ရော်ခြင်း",
    "khayo": "ကုန်ခန်းခြင်း", "vayo": "ပျက်ခြင်း", "bhedo": "ကွဲခြင်း", "paribhedo": "ကွဲကြေခြင်း",
    "aniccatā": "မမြဲခြင်း", "antaradhānaṃ": "ကွယ်ပျောက်ခြင်း",
    # the four elements
    "kharagataṃ": "ခက်မာ သဘော ရှိသောအရာ", "kakkhaḷattaṃ": "ကြမ်းတမ်းသော အဖြစ်", "kakkhaḷabhāvo": "ကြမ်းတမ်းသော သဘော",
    "āpo": "ရေ", "āpogataṃ": "ရေ သဘော ရှိသောအရာ", "sineho": "စေးကပ်မှု", "sinehagataṃ": "စေးကပ်မှု သဘော ရှိသောအရာ",
    "bandhanattaṃ rūpassa": f"{RUPA}၏ ဖွဲ့စည်းချည်နှောင်ထားသော အဖြစ်",
    "tejo": "မီး", "tejogataṃ": "မီး သဘော ရှိသောအရာ", "usmā": "အပူ", "usmāgataṃ": "အပူ သဘော ရှိသောအရာ",
    "usumaṃ": "အပူငွေ့", "usumagataṃ": "အပူငွေ့ သဘော ရှိသောအရာ",
    "vāyo": "လေ", "vāyogataṃ": "လေ သဘော ရှိသောအရာ", "thambhitattaṃ rūpassa": f"{RUPA}၏ တောင့်တင်းထားသော အဖြစ်",
}
for k, v in SYN_NEW.items():
    new("Synonym lists (SYN)", F.SYN, k, v)
assert NOUN["rūpassa aniccatā"] == f"{RUPA}၏ {F.SYN['aniccatā']}"
F.SYN["dhoso"] = F.SYN["ghoso"]        # ^1-850 source slip «dhoso» for «ghoso» (rendered as ghoso)
F.VAR_KIND.setdefault("cakkhuṃ", F.LEKHANA)
F.VAR_KIND.setdefault("itthittaṃ itthībhāvo", F.LEKHANA)
F.VAR_KIND.setdefault("kharigataṃ", F.LEKHANA)
F.VAR_KIND.setdefault("rūpiyaṃ", F.PATHA)
F.VAR_KIND.setdefault("anidassanaṃ appaṭighaṃ", F.LEKHANA)

CITTA3 = (f"{T['kusalā']}{F.MIND}၏ဖြစ်စေ{C} {T['akusalā']}{F.MIND}၏ဖြစ်စေ{C} "
          f"{T['abyākatā']} {F.MIND}၏ဖြစ်စေ")     # kusalacittassa vā akusalacittassa vā abyākatacittassa vā
MOVES = ["ရှေ့သို့ တိုးသွားသူ၏ဖြစ်စေ", "နောက်သို့ ဆုတ်သူ၏ဖြစ်စေ", "ရှေ့တည့်တည့် ကြည့်သူ၏ဖြစ်စေ",
         "ဘေးဘီ ကြည့်သူ၏ဖြစ်စေ", "ကွေးသူ၏ဖြစ်စေ", "ဆန့်သူ၏ဖြစ်စေ"]
_KAYA_GEN = ("kusalacittassa vā akusalacittassa vā abyākatacittassa vā abhikkamantassa vā paṭikkamantassa vā "
             "ālokentassa vā vilokentassa vā samiñjentassa vā pasārentassa vā kāyassa")
GEN_NEW = {
    "itthiyā": f"{FEM}၏", "purisassa": f"{MASC}၏",
    "tesaṃ rūpīnaṃ dhammānaṃ": f"ထို {T['rūpino']} {F.DHAMMA}တို့၏", "rūpassa": f"{RUPA}၏",
    _KAYA_GEN: f"{CITTA3}{C} {f'{C} '.join(MOVES)} {SENSE['kāya']}၏",
    "tāya vācāya": f"ထို{VACA}ဖြင့်",
}
for k, v in GEN_NEW.items():
    new("List heads (GEN)", F.GEN, k, v)
TAIL_PI = "ajjhattaṃ vā bahiddhā vā upādiṇṇaṃ vā anupādiṇṇaṃ vā"
TAIL = f"{C} ".join(stem(T[k]) + "သည်ဖြစ်စေ" for k in ("ajjhattā", "bahiddhā", "upādiṇṇā", "anupādiṇṇā"))
CITTAJA, CITTAHETU = f"{F.MIND}မှ မွေးဖွားသော", f"{F.MIND}ကို အမြစ်ပြုသော"
CAUSE = {"kammassa katattā": KAMMA, "na kammassa katattā": F.no_(KAMMA),
         "cittajaṃ cittahetukaṃ cittasamuṭṭhānaṃ": f"{CITTAJA}{C} {CITTAHETU}{C} {T['cittasamuṭṭhānā']}",
         "na cittajaṃ na cittahetukaṃ na cittasamuṭṭhānaṃ":
             f"{F.no_(CITTAJA)}{C} {F.no_(CITTAHETU)}{C} {T['no cittasamuṭṭhānā']}"}
MANAPA, AMANAPA = "စိတ်နှင့် တွေ့သော", "စိတ်နှင့် မတွေ့သော"

FIXED = {
    "Katame dhammā abyākatā": f"{T['abyākatā']} {F.DHAMMA_PL} {F.CU_Q['pl']}",
    ("Kusalākusalānaṃ dhammānaṃ vipākā kāmāvacarā rūpāvacarā arūpāvacarā apariyāpannā vedanākkhandho "
     "saññākkhandho saṅkhārakkhandho viññāṇakkhandho"):
        (f"{T['kusalā']}နှင့် {T['akusalā']} {F.DHAMMA}တို့၏ အကျိုး ဖြစ်သော{C} {T['kāmāvacarā']}{C} "
         f"{T['rūpāvacarā']}{C} {T['arūpāvacarā']}{C} {T['apariyāpannā']} "
         + f"{C} ".join(F.NAMES[k] for k in ("vedanākkhandho", "saññākkhandho", "saṅkhārakkhandho",
                                             "viññāṇakkhandho"))),
    "ye ca dhammā kiriyā neva kusalā nākusalā na ca kammavipākā":
        f"{F.KIRIYA_ATTR} {F.DHAMMA_PL}လည်း",              # as 4-01 / 5 (… ca = လည်း; consistency pass)
    "sabbañca rūpaṃ": f"{RUPA} {SABBA}လည်း",
    "asaṅkhatā ca dhātu": f"{T['asaṅkhatā']} {DHATU}လည်း",
    "ime dhammā abyākatā": f"ဤ{F.DHAMMA_PL}သည် {T['abyākatā']} {F.DHAMMA_PL} {F.CU_COP['pl']}",
    "Tattha katamaṃ sabbaṃ rūpaṃ": f"ထိုတို့အနက် {RUPA} {SABBA} {F.CU_Q['sg']}",   # Tattha, as 4-0x
    "Cattāro ca mahābhūtā, catunnañca mahābhūtānaṃ upādāya rūpaṃ":
        f"{MAHABHUTA} {F.NUM['catu']}{F.CL}လည်းကောင်း{C} {UPADAYA4} ဖြစ်သော {RUPA}လည်းကောင်း",
    "idaṃ vuccati sabbaṃ rūpaṃ": f"ဤသည်ကို {RUPA} {SABBA}ဟု ခေါ်သည်",          # vuccati, as 4-0x
    "ayaṃ vuccati vācā": f"ဤသည်ကို {VACA}ဟု ခေါ်သည်",
    "Diṭṭhaṃ sutaṃ mutaṃ viññātaṃ rūpaṃ": f"{DITTHA}{C} {SUTA}{C} {MUTA}{C} {VINNATA} {RUPA}",
    ("Rūpāyatanaṃ diṭṭhaṃ, saddāyatanaṃ sutaṃ, gandhāyatanaṃ rasāyatanaṃ phoṭṭhabbāyatanaṃ mutaṃ, sabbaṃ rūpaṃ "
     "manasā viññātaṃ rūpaṃ"):
        (f"{NOUN['rūpāyatanaṃ']}သည် {DITTHA}အရာ{C} {NOUN['saddāyatanaṃ']}သည် {SUTA}အရာ{C} "
         f"{NOUN['gandhāyatanaṃ']}{C} {NOUN['rasāyatanaṃ']}{C} {NOUN['phoṭṭhabbāyatanaṃ']}တို့သည် {MUTA}အရာ{C} "
         f"{RUPA} {SABBA}သည် {F.MANO}ဖြင့် {VINNATA} {RUPA} {F.CU_COP['sg']}"),
    "Yo āyatanānaṃ ācayo, so rūpassa upacayo":
        f"{AYATANA}တို့၏ စုပုံခြင်း{C} ထိုအရာသည် {NOUN['rūpassa upacayo']} {F.CU_COP['sg']}",
    "Yo rūpassa upacayo, sā rūpassa santati":
        f"{NOUN['rūpassa upacayo']}{C} ထိုအရာသည် {NOUN['rūpassa santati']} {F.CU_COP['sg']}",
    "manāpiyo phoṭṭhabbo sukhasamphasso kāyaviññeyyaṃ rūpaṃ":
        f"{MANAPA}{C} {PRED['sukhasamphassaṃ']} {OBJECT['phoṭṭhabba']}သည် {VINNEYYA['kāyaviññeyyaṃ']} {RUPA} "
        f"{F.CU_COP['sg']}",
    "amanāpiyo phoṭṭhabbo dukkhasamphasso kāyaviññeyyaṃ rūpaṃ":
        f"{AMANAPA}{C} {PRED['dukkhasamphassaṃ']} {OBJECT['phoṭṭhabba']}သည် {VINNEYYA['kāyaviññeyyaṃ']} {RUPA} "
        f"{F.CU_COP['sg']}",
    ("yaṃ vā panaññampi atthi rūpaṃ yamhi yamhi janapade tesaṃ tesaṃ sattānaṃ mukhāsiyaṃ dantavikhādanaṃ "
     "galajjhoharaṇīyaṃ kucchivitthambhanaṃ"):
        (f"ဒေသ အသီးသီး၌ ထိုထို သတ္တဝါတို့၏ ခံတွင်းဖြင့် စားရသော{C} သွားဖြင့် ဝါးရသော{C} လည်ချောင်းမှ မျိုချရသော{C} "
         f"ဝမ်းကို ပြည့်စေသော အခြား {RUPA} ရှိသမျှလည်း"),
    "yāya ojāya sattā yāpenti": f"သတ္တဝါတို့ အသက် ရှင်သန်ကြရာ ဖြစ်သော {OJA}",
    "Rūpakaṇḍe paṭhamabhāṇavāro": f"{RUPAKANDA}၌ {F.COLO['Paṭhamabhāṇavāro']}",   # X-kaṇḍe = «X အခန်း၌», as 4-0x
    "Rūpakaṇḍaṃ niṭṭhitaṃ": f"“{RUPAKANDA}” {F.NITTHITA}",
}
NEW.setdefault("Fixed sentences and phrases", []).extend(FIXED.items())
NEW.setdefault("Building blocks", []).extend([
    ("rūpa (matter)", RUPA), ("rūpa (visible form)", RUPA_V), ("sabba", SABBA), ("mahābhūta", MAHABHUTA),
    ("catunnaṃ mahābhūtānaṃ upādāya", UPADAYA4), ("nissāya", NISSAYA), ("ārabbha", ARABBHA),
    ("-ārammaṇo / -ārammaṇā", F.TAKES), ("pasāda", PASADA), ("attabhāvapariyāpanna", ATTABHAVA),
    ("vaṇṇanibhā", VANNA), ("vatthu", VATTHU), ("viññatti", VINNATTI), ("vācā", VACA), ("kiriyā", KIRIYA),
    ("kammassa katattā", KAMMA), ("cittaja", CITTAJA), ("cittahetuka", CITTAHETU), ("ojā", OJA),
    ("diṭṭha / suta / muta / viññāta", f"{DITTHA} / {SUTA} / {MUTA} / {VINNATA}"),
    ("manāpiya / amanāpiya", f"{MANAPA} / {AMANAPA}"), ("-vidhena rūpasaṅgaho", f"{RUPA}ကို N{KIND}ဖြင့် {SANGAHA}"),
    ("Evaṃ … rūpasaṅgaho", f"ဤသို့ {RUPA}ကို N{KIND}ဖြင့် {SANGAHA} {F.CU_COP['sg']}"),
    (TAIL_PI, TAIL), ("-assa vā (genitive alternatives)", "…၏ဖြစ်စေ"),
    ("kāyaviññatti movements: abhikkamantassa … pasārentassa vā", f"{C} ".join(MOVES)),
    ("Yaṃ taṃ rūpaṃ X, taṃ Y", f"X {RUPA}{C} ထို{RUPA}သည် Y {RUPA} {F.CU_COP['sg']}"),
    ("taṃ atthi Y", f"ထို{RUPA}တွင် Y {RUPA} {F.CU_HOTI['sg']}"),
    ("Atthi rūpaṃ X / atthi X", f"X {RUPA} {F.CU_HOTI['sg']}"),
    ("Katamaṃ taṃ rūpaṃ X?", f"X {RUPA} {F.CU_Q['sg']}။"),
    ("idaṃ taṃ rūpaṃ X.", f"{F.CU_DEM['sg']} X {RUPA} {F.CU_COP['sg']}။"),
    ("yañca rūpaṃ X", f"X {RUPA}လည်း"), ("yaṃ / yo vā panaññampi / panaññopi atthi X", f"… အခြား X ရှိသမျှလည်း"),
    ("Sabbaṃ rūpaṃ A, B, … Z (ekaka)", f"{RUPA} {SABBA}သည် A၊ B၊ … Zသည်"),
    ("… A-meva, B-meva … (ekaka niddesa)", f"… Aသည်ပင်၊ Bသည်ပင် …"),
])

# ---- headings and colophons
GROUP = {"Ekakaṃ": "eka", "Dukaṃ": "du", "Tikaṃ": "ti", "Catukkaṃ": "catub", "Pañcakaṃ": "pañca",
         "Chakkaṃ": "chab", "Sattakaṃ": "satta", "Aṭṭhakaṃ": "aṭṭha", "Navakaṃ": "nava", "Dasakaṃ": "dasa",
         "Ekādasakaṃ": "ekādasa"}
TITLES = {}
for g, n in GROUP.items():
    TITLES[g] = f"{NUMW[n]}{KIND}တွဲ"
assert TITLES["Dukaṃ"] == F.DUKA and TITLES["Tikaṃ"] == F.TIKA
for g in ("Ekaka", "Duka", "Tika"):
    TITLES[g + "niddeso"] = f"{TITLES[g + 'ṃ']} {NIDDESA}"
TITLES.update({"Rūpakaṇḍaṃ": RUPAKANDA, "Uddeso": UDDESA, "Rūpavibhatti": f"{RUPA}ကို ခွဲခြား {F.VARA}",
               "Upādābhājanīyaṃ": f"{T['upādā']} {RUPA}ကို ခွဲခြမ်း {F.VARA}"})
for k, v in TITLES.items():
    F.HEAD.setdefault(k, v)
    F.COLO.setdefault(k, v)
    if F.HEAD[k] != v or F.COLO[k] != v:
        raise SystemExit("heading conflict: " + k)
NEW.setdefault("Headings and colophons", []).extend(TITLES.items())


def r_sangaha(m):
    n = NUMW[m["n"].lower()]
    if m["e"]:
        return f"ဤသို့ {RUPA}ကို {n}{KIND}ဖြင့် {SANGAHA} {F.CU_COP['sg']}"
    return f"{RUPA}ကို {n}{KIND}ဖြင့် {SANGAHA}"


def att(s):
    return chain_my(s)


def r_q(m):
    return f"{att(m['p'])} {RUPA} {F.CU_Q['sg']}"


def r_close(m):
    return f"{F.CU_DEM['sg']} {att(m['p'])} {RUPA} {F.CU_COP['sg']}"


def r_atthi(m):
    return f"{att(m['p'])} {RUPA} {F.CU_HOTI['sg']}"


def r_yam_tam(m):
    return f"{att(m['p'])} {RUPA}"


def r_tam(m):
    return f"ထို{RUPA}သည် {att(m['p'])} {RUPA} {F.CU_COP['sg']}"


def r_tam_atthi(m):
    return f"ထို{RUPA}တွင် {att(m['p'])} {RUPA} {F.CU_HOTI['sg']}"


def r_yanca(m):
    return f"{att(m['p'])} {RUPA}လည်း"


def r_p_atthi(m):
    return f"{att(m['p'])} {RUPA}တွင် {att(m['q'])} {RUPA} {F.CU_HOTI['sg']}"


def r_vinneyya(m):
    return f"{VINNEYYA[m['p'][0].lower() + m['p'][1:]]} {RUPA}"


_NAME_ALT = None


def r_names(m):
    """A space-separated run of names, multi-word names included (rūpassa upacayo …) -> «A၊ B၊ …»."""
    found = re.findall(_NAME_ALT, m[0])
    if " ".join(found) != m[0]:
        raise Miss("names: " + m[0])
    return f"{C} ".join(F._name(x) for x in found)


def r_names_vinneyya(m):
    found = re.findall(F._alt(NOUN), m["n"])
    if " ".join(found) != m["n"]:
        raise Miss("names: " + m["n"])
    ns = [F._name(x) for x in found]
    head = ns[0] if len(ns) == 1 else f"{C} ".join(ns) + "တို့"
    return f"{head}သည် {VINNEYYA[m['p']]} {RUPA} {F.CU_COP['sg']}"


def r_sabba_vinneyya(m):
    return f"{RUPA} {SABBA}သည် {VINNEYYA[m['p']]} {RUPA} {F.CU_COP['sg']}"


def r_cause_other(m):
    return f"{CAUSE[m['q']]} အခြား {RUPA} ရှိသမျှလည်း"


def r_cause(m):
    return CAUSE[m[0][0].lower() + m[0][1:]]


def r_elem(m):
    return f"{F.items_my(F.list_items(m['l']))}{C} {TAIL}"


def r_vaca(m):
    return f"{CITTA3} {F.items_my(F.list_items(m['l']))}"


def r_fixed(m):
    return FIXED[m[0]]


Q_LOOK = r"(?=[?.]| [^\s…]+…pe…)"
RULES = [
    (_alt(FIXED), r_fixed),
    (r"Sabbaṃ rūpaṃ (?P<l>(?:\[[^\]]*\]|[^.\[])+)(?=\.)", r_ekaka),
    (r"(?P<e>[Ee]vaṃ )?(?P<n>[Ee]kādasa|[Ee]ka|[Dd]u|[Tt]i|[Cc]atub|[Pp]añca|[Cc]hab|[Ss]atta|[Aa]ṭṭha|[Nn]ava|[Dd]asa)"
     r"[vb]idhena rūpasaṅgaho", r_sangaha),
    (rf"Katamaṃ taṃ rūpaṃ (?P<p>{CHAIN}){Q_LOOK}", r_q),
    (rf"[Ii]daṃ taṃ rūpaṃ (?P<p>{CHAIN})", r_close),
    (rf"[Aa]tthi rūpaṃ (?P<p>{CHAIN})", r_atthi),
    (rf"Yaṃ taṃ rūpaṃ (?P<p>{CHAIN})", r_yam_tam),
    (rf"taṃ atthi (?P<p>{CHAIN})", r_tam_atthi),
    (rf"taṃ (?P<p>{CHAIN})", r_tam),
    (rf"atthi (?P<p>{CHAIN})", r_atthi),
    (rf"yañca rūpaṃ (?P<p>{CHAIN})", r_yanca),
    (rf"(?P<p>{CHAIN}) rūpaṃ atthi (?P<q>{CHAIN})", r_p_atthi),
    (rf"sabbaṃ rūpaṃ (?P<p>{_alt(VINNEYYA)}) rūpaṃ", r_sabba_vinneyya),
    (rf"(?P<n>{F._alt(NOUN)}(?: {F._alt(NOUN)})*) (?P<p>{_alt(VINNEYYA)}) rūpaṃ", r_names_vinneyya),
    (rf"(?P<p>{F._alt(VINNEYYA)}) rūpaṃ", r_vinneyya),
    (r"(?P<rel>Yaṃ|Yā|Yo) (?P<c>cakkhu|sotaṃ|ghānaṃ|jivhā|kāyo)(?: (?P<v>\[[^\]]+\]))? catunnaṃ mahābhūtānaṃ upādāya "
     r"pasādo(?P<full> attabhāvapariyāpanno anidassano sappaṭigho)?", r_org_head),
    (r"Yaṃ rūpaṃ catunnaṃ mahābhūtānaṃ upādāya vaṇṇanibhā(?: sanidassanaṃ sappaṭighaṃ (?P<l>.+?)(?=, yaṃ vā "
     r"panaññampi))?", r_colour_head),
    (r"Yo (?P<o>saddo|gandho|raso) catunnaṃ mahābhūtānaṃ upādāya anidassano sappaṭigho (?P<l>.+?)(?=, yo vā "
     r"panaññopi)", r_obj_head),
    (r"(?:yaṃ vā panaññampi atthi (?P<o>rūpaṃ) catunnaṃ mahābhūtānaṃ upādāya vaṇṇanibhā sanidassanaṃ sappaṭighaṃ|"
     r"yo vā panaññopi atthi (?P<o2>saddo|gandho|raso) catunnaṃ mahābhūtānaṃ upādāya anidassano sappaṭigho)",
     lambda m: r_obj_other({"o": m["o"] or m["o2"]})),
    (rf"(?P<rel>yena|yāya|yamhi|yaṃ|yā|yo) (?P<w1>\S+) (?P<a1>{ADJ}) (?P<w2>\S+) (?P<a2>{ADJ}) (?P<v>{V4_RE})",
     r_sense),
    (rf"yaṃ (?P<c>{CACC}) nissāya (?:(?P<o>{OACC}) ārabbha|(?P<oa>{OARM})) "
     rf"(?:(?P<s>{SAMPH}) (?P<v>{V4U})|(?P<sj>{SAMPHJ}) vedanā)", r_nis_org),
    (rf"yaṃ (?:(?P<o>{OACC}) ārabbha|(?P<oa>{OARM})) (?P<c>{CACC}) nissāya "
     rf"(?:(?P<s>{SAMPH}) (?P<v>{V4U})|(?P<sj>{SAMPHJ}) vedanā)", r_nis_obj),
    (rf"(?P<c>{_alt(SENSE)})viññāṇaṃ (?P<v>{V4U})", r_vinnana),
    (rf"{PI_ITEM}(?: {PI_ITEM})*", r_pi),
    (rf"yaṃ vā panaññampi atthi rūpaṃ (?P<q>{_alt(CAUSE)})", r_cause_other),
    (r"(?:[Kk]ammassa katattā|Na kammassa katattā)", r_cause),
    (rf"Yaṃ (?P<l>(?:(?! – ).)+?) {TAIL_PI}(?= – )", r_elem),
    (r"Yā kusalacittassa vā akusalacittassa vā abyākatacittassa vā (?P<l>vācā .+? vacībhedo)(?=, ayaṃ| – ayaṃ)",
     r_vaca),
]
_NAME_ALT = F._alt(F.NAMES) + NA
RULES.append((rf"{_NAME_ALT}(?: {_NAME_ALT})+", r_names))
F.CU_EXTRA_RULES[:] = [(re.compile(p), f) for p, f in RULES]
if (" –", " –") not in F.CU_SEP:          # a dash at the end of a line («Duvidhena rūpasaṅgaho –»), in memory
    F.CU_SEP.insert(F.CU_SEP.index((" – ", " – ")) + 1, (" –", " –"))
F.rebuild_cu()


# ===================================================================================== output
def write(name, txt):
    txt = unicodedata.normalize("NFC", txt)
    (OUT / name).write_text(txt, encoding="utf-8")
    print(f"wrote {name}: {sum(1 for l in txt.splitlines() if l)} lines")


def chapter(name):
    write(name, F.translate_cu((PALI / name).read_text(encoding="utf-8-sig")))


def terms_section():
    L = [TERMS_HEAD, "", "Generated by make_ch3.py from its in-memory tables (my_formulas.py and my-zeroshot-terms.md "
         "are not changed). One «Pāli = Burmese» per line.", ""]
    for g, items in NEW.items():
        L += [f"### {g}", ""]
        seen = set()
        for k, v in items:
            if k in seen:
                continue
            seen.add(k)
            L.append(f"{k} = {v}")
        L.append("")
    return "\n".join(L).rstrip("\n") + "\n"


def write_terms():
    txt = NOTES.read_text(encoding="utf-8") if NOTES.exists() else ""
    i = txt.find("\n" + TERMS_HEAD + "\n")
    base = (txt[:i + 1] if i >= 0 else txt).rstrip("\n") + "\n\n"
    NOTES.write_text(unicodedata.normalize("NFC", base + terms_section()), encoding="utf-8")
    print("updated notes-ch3.md:", TERMS_HEAD)


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a != "--terms"]
    for a in args or list(CHAPTERS):
        chapter(CHAPTERS[a])
    if "--terms" in sys.argv or not args:
        write_terms()
