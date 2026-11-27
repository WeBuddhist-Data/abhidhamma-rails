"""Shared Burmese formulas for pi-2 (Vibhaṅga, «ခွဲခြမ်းစိတ်ဖြာခြင်း»), plain audience.

Every pi-2 Burmese generator imports this module, so that identical Pāli gets identical Burmese, within pi-2 and
with the FINAL pi-1 Burmese (the rails text). Writes no files at import (no bytecode either). It holds:
  * pi-1 reuse: pi-1-my/my_formulas.py and pi-1-my/make_ch3.py are read as text, the rails patches of
    pi-1-my/rails/my_formulas_rails.py are applied in memory (exactly as rails/build_rails.py does) and the code is
    executed here: P1 = the final pi-1 module (TERMS, CEVA, CEVANO, NAMES, SYN …), C3 = the Rūpakaṇḍa namespace
    (matter predicates, the ekaka list, the matter frames). Nothing in pi-1-my is written;
  * the 4-01 definition lists (atīta / anāgata / paccuppanna / ajjhatta / bahiddhā items) read from the final pi-1
    Burmese lines ^1-1044 … ^1-1051 (DEF);
  * the book frame, headings, colophons (HEAD, COLO, EDIT); the five aggregates (KH) and the topic nouns (NOUN);
  * the eleven qualifiers (Q11A attributive, Q11V «…ဖြစ်စေ», Q11P predicative), the new definition items (DEF),
    the statement qualifiers of the oḷārika / hīna / dūre passages (QV);
  * the abhidhamma part: VIDHA (number of kinds), ITEM (list items), «atthi T» = «T KN ရှိသည်»;
  * the pañhāpucchaka: «S T» = «Sသည် T သဘောတရား ဖြစ်သည်», siyā = «တစ်ခါတစ်ရံ», «na vattabbo – "A"tipi» =
    «Sသည် – “A သဘောတရား”ဟုလည်းကောင်း … ခေါ်ဆို၍ မရ» (pi-1 ^1-1198, ^1-1404, ^1-1406);
  * the engine: translate_line() -> line_my() -> heading / colophon / clauses_my(); any text no rule matches raises
    Miss: nothing is guessed.
Later chapters: import this module, add entries to the tables (never change an existing value without the user's
approval), add (regex, function) pairs to EXTRA_RULES, then call rebuild().
"""
import importlib.util
import pathlib
import re
import sys
import types

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
P1DIR = HERE.parent / "pi-1-my"
ROOT = HERE.parents[3]
P1_RAILS = ROOT / "AI_translation/burmese/pi-1-burmese-plain-rails_split_chapters"
P1_PALI = ROOT / "AI_translation/pali/pi-1_split_chapters"


# ===================================================================================== pi-1 (final) loaded read-only
def _load_rails_layer():
    spec = importlib.util.spec_from_file_location("pi1_my_rails_layer", P1DIR / "rails" / "my_formulas_rails.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _patched(src, patches, where):
    for old, new, count, reason in patches:
        n = src.count(old)
        if n != count:
            raise SystemExit(f"{where}: rails patch occurs {n}x, expected {count} ({reason})")
        src = src.replace(old, new)
    return src


L1 = _load_rails_layer()
_src = _patched((P1DIR / "my_formulas.py").read_text(encoding="utf-8"), L1.FORMULA_PATCHES, "my_formulas.py")
P1 = types.ModuleType("my_formulas")
P1.__file__ = str(P1DIR / "my_formulas.py")
_saved = sys.modules.get("my_formulas")
sys.modules["my_formulas"] = P1
exec(compile(_src, P1.__file__, "exec"), P1.__dict__)
_c3 = _patched((P1DIR / "make_ch3.py").read_text(encoding="utf-8"), L1.GEN_PATCHES.get("make_ch3", []), "make_ch3.py")
_c3 = _c3.split('\nif __name__ == "__main__":')[0]
C3 = {"__name__": "pi1_make_ch3", "__file__": str(P1DIR / "make_ch3.py")}
exec(compile(_c3, C3["__file__"], "exec"), C3)
if _saved is None:
    sys.modules.pop("my_formulas", None)
else:
    sys.modules["my_formulas"] = _saved

Miss = P1.Miss
T = P1.TERMS
C = P1.COMMA                         # «၊»
END = P1.END                         # «။»
PE = P1.PE                           # …pe… / …Pe… = one «…»
DH, DHP = P1.DHAMMA, P1.DHAMMA_PL    # သဘောတရား / သဘောတရားများ
AMONG = P1.DHAMMA_AMONG              # သဘောတရားများအနက်
COP = {False: "ဖြစ်သည်", True: "ဖြစ်ကြသည်"}
HOTI = "ရှိသည်"
RUPA = C3["RUPA"]                    # ရုပ်
SENSE = C3["SENSE"]                  # cakkhu မျက်စိ, sota နား, ghāna နှာခေါင်း, jivhā လျှာ, kāya ကိုယ်
OBJECT = C3["OBJECT"]


def stem(x):
    if not x.endswith("သော"):
        raise Miss("stem: " + x)
    return x[:-3]


# ===================================================================================== book frame
NAMO = P1.NAMO
ABHI = P1.ABHI
TITLE = "ခွဲခြမ်းစိတ်ဖြာခြင်း"          # Vibhaṅgapāḷi (book title, Burmese only; proposed)
NITTHITA = P1.NITTHITA

# ===================================================================================== aggregates
KHANDHA = P1.KHANDHA                 # အစုအဝေး
NOUN = {    # topic noun: Burmese, always plural, Pāli forms (case-free)
    "rūpa": dict(my=RUPA, pl=False, forms={"rūpaṃ"}),
    "vedanā": dict(my=P1.FEEL, pl=False, forms={"vedanā", "vedanāya", "vedanāhi", "vedanaṃ"}),
    "saññā": dict(my=P1.SANNA, pl=False, forms={"saññā", "saññāya", "saññāhi", "saññaṃ"}),
    "saṅkhārā": dict(my=P1.SANKHARA, pl=True, forms={"saṅkhārā", "saṅkhārehi", "saṅkhārānaṃ", "saṅkhāre"}),
    "viññāṇa": dict(my=P1.VINNANA, pl=False, forms={"viññāṇaṃ", "viññāṇā", "viññāṇehi", "viññāṇassa"}),
}
NOUN_PI = {"rūpaṃ": "rūpa", "vedanā": "vedanā", "saññā": "saññā", "saṅkhārā": "saṅkhārā", "viññāṇaṃ": "viññāṇa",
           "vedanaṃ": "vedanā", "saññaṃ": "saññā", "saṅkhāre": "saṅkhārā"}
KH = {      # subject: (Burmese, topic noun, plural)
    "rūpakkhandho": (f"{RUPA} {KHANDHA}", "rūpa", False),
    "vedanākkhandho": (P1.NAMES["vedanākkhandho"], "vedanā", False),
    "saññākkhandho": (P1.NAMES["saññākkhandho"], "saññā", False),
    "saṅkhārakkhandho": (P1.NAMES["saṅkhārakkhandho"], "saṅkhārā", False),
    "viññāṇakkhandho": (P1.NAMES["viññāṇakkhandho"], "viññāṇa", False),
    "pañcakkhandhā": (P1.count_my(KHANDHA, "pañca"), None, True),
    "cattāro khandhā": (P1.NAMES["cattāro khandhā"], None, True),
    "tayo khandhā": (P1.count_my(KHANDHA, "ti"), None, True),
    "dve khandhā": (P1.count_my(KHANDHA, "dvi"), None, True),
}
KH_ORDER = ["rūpakkhandho", "vedanākkhandho", "saññākkhandho", "saṅkhārakkhandho", "viññāṇakkhandho"]
assert KH["rūpakkhandho"][0] == "ရုပ် အစုအဝေး"           # pi-1 termbase rūpakkhandho


def kh(p):
    k = p[0].lower() + p[1:]
    if k not in KH:
        raise Miss("subject: " + p)
    return KH[k]


def nmy(n, pl=False):
    d = NOUN[n]
    return d["my"] + ("များ" if pl or d["pl"] else "")


# ===================================================================================== headings, colophons
VARA = P1.VARA                       # ဖော်ပြချက်
BHAJANIYA = f"ခွဲခြမ်း {VARA}"       # -bhājanīya, as pi-1 Padabhājanīyaṃ / Upādābhājanīyaṃ
HEAD = {
    "Khandhavibhaṅgo": f"{KHANDHA}များကို {TITLE}",
    "Suttantabhājanīyaṃ": f"သုတ္တန်အလိုက် {BHAJANIYA}",
    "Abhidhammabhājanīyaṃ": f"အဘိဓမ္မာအလိုက် {BHAJANIYA}",
    "Pañhāpucchakaṃ": f"မေးခွန်းများဖြင့် {VARA}",
    "Tikaṃ": P1.TIKA, "Dukaṃ": P1.DUKA,
}
for _k in KH_ORDER:
    HEAD[_k[0].upper() + _k[1:]] = KH[_k][0]
NAYA = "ခွဲနည်း"                     # method (pi-1 Catukkanayo = ဈာန် လေးပါး ခွဲနည်း)
COLO = {
    "Suttantabhājanīyaṃ": HEAD["Suttantabhājanīyaṃ"],
    "Abhidhammabhājanīyaṃ": HEAD["Abhidhammabhājanīyaṃ"],
    "Pañhāpucchakaṃ": HEAD["Pañhāpucchakaṃ"],
    "Dukamūlakaṃ": f"{P1.DUKA}ကို အခြေခံသော {NAYA}",
    "Tikamūlakaṃ": f"{P1.TIKA}ကို အခြေခံသော {NAYA}",
    "Ubhatovaḍḍhakaṃ": f"နှစ်ဘက်စလုံး တိုးပွားသော {NAYA}",
    "Khandhavibhaṅgo niṭṭhito": f"“{HEAD['Khandhavibhaṅgo']}” {NITTHITA}",
}
EDIT = {    # editorial instructions in round brackets (Pāli without the brackets)
    "Yathā rūpakaṇḍe vibhattaṃ, tathā idha vibhajitabbaṃ.":
        f"{C3['RUPAKANDA']}၌ ခွဲခြားထားသည့်အတိုင်း ဤနေရာ၌လည်း ထိုနည်းတူ ခွဲခြားရမည်{END}",
    "Yathā kusalattike vitthāro, evaṃ sabbepi tikā vitthāretabbā.":
        f"{T['kusalā']} {P1.TIKA}၌ အကျယ် ဖော်ပြထားသည့်အတိုင်း {P1.TIKA} အားလုံးကိုလည်း ထိုနည်းတူ အကျယ် ဖော်ပြရမည်{END}",
}

# ===================================================================================== variant readings
VAR_KIND = P1.VAR_KIND
for _k in ("kabaḷiṃkāro", "nupādā"):
    VAR_KIND.setdefault(_k, P1.LEKHANA)
var_my = P1.var_my

# ===================================================================================== mātikā terms (pi-1 final)
CEVA, CEVANO = P1.CEVA, P1.CEVANO
SAMP, TOGETHER = P1.SAMP, P1.TOGETHER
NEW_TERMS = {
    "phassasampayuttā": P1.PHASSA + SAMP,                       # တွေ့ထိမှုနှင့် ယှဉ်တွဲသော
    "dukkhasahagatā": f"{P1.DUKKHA}မှု{TOGETHER}",              # as pi-1 «နာကျင်မှုနှင့်အတူ ဖြစ်သော ကိုယ် သိစိတ်»
    "sukhā": f"{P1.SUKHA}သော", "dukkhā": f"{P1.DUKKHA}သော",     # «… vedanā atthi sukhā, atthi dukkhā»
}
INDR = {    # the feeling faculties (pi-1 final names)
    "sukhindriyaṃ": P1._ix(P1.SUKHA + "မှု", P1.INDRIYA), "dukkhindriyaṃ": P1._ix(P1.DUKKHA + "မှု", P1.INDRIYA),
    "somanassindriyaṃ": P1.NAMES["somanassindriyaṃ"], "domanassindriyaṃ": P1._ix("စိတ်ဆင်းရဲမှု", P1.INDRIYA),
    "upekkhindriyaṃ": P1.NAMES["upekkhindriyaṃ"],
}
for _k, _v in INDR.items():
    NEW_TERMS[_k[:-1] + "sampayuttā"] = _v + SAMP


def combo(a, b):
    """Two dyad terms in one compound (na hetū sahetukā, āsavavippayuttā sāsavā): pi-1 ^1-1087 / ^1-1116 form."""
    return f"{T[a]} {AMONG} {T[b]}"


NEW_TERMS["na hetū sahetukā"] = combo("na hetū", "sahetukā")
NEW_TERMS["na hetū ahetukā"] = combo("na hetū", "ahetukā")
for _st, _d in P1.FAMILY.items():
    NEW_TERMS[_st + "vippayutta" + _d["y"]] = combo(_st + "vippayuttā", _d["y"])
    NEW_TERMS[_st + "vippayutta" + _d["ny"]] = combo(_st + "vippayuttā", _d["ny"])
for _k, _v in NEW_TERMS.items():
    if _k in T and T[_k] != _v:
        raise SystemExit("term conflict " + _k)
    T.setdefault(_k, _v)

TERM_IRREG = {
    "hetu": "hetū", "na hetu": "na hetū",
    "maggādhipati": "maggādhipatino", "uppādī": "uppādino", "ācayagāmī": "ācayagāmino",
    "apacayagāmī": "apacayagāmino", "nevācayagāmināpacayagāmī": "nevācayagāmināpacayagāmino",
    "cittasahabhu": "cittasahabhuno", "cittasahabhū": "cittasahabhuno", "no cittasahabhū": "no cittasahabhuno",
    "cittānuparivatti": "cittānuparivattino", "no cittānuparivatti": "no cittānuparivattino",
    "rūpaṃ": "rūpino", "arūpā": "arūpino", "cittaṃ": "cittā",
    "ajjhatto": "ajjhattā", "bahiddho": "bahiddhā", "ajjhattabahiddho": "ajjhattabahiddhā",
    "cittena sampayutto": "cittasampayuttā", "cittena vippayutto": "cittavippayuttā",
    "cittena saṃsaṭṭho": "cittasaṃsaṭṭhā", "cittena visaṃsaṭṭho": "cittavisaṃsaṭṭhā",
    "āsavippayuttaanāsavo": "āsavavippayuttaanāsavā",       # source slip (read as āsavavippayutta-)
}


def term_key(p):
    """Pāli surface of a mātikā term (any gender / number) -> TERMS key."""
    p = p.replace("upādinn", "upādiṇṇ")
    p = re.sub(r"^na hetu ?(?=s?a?hetuk)", "na hetū ", p)
    if p in T:
        return p
    if p in TERM_IRREG:
        return TERM_IRREG[p]
    for a, b in (("o", "ā"), ("aṃ", "ā"), ("ī", "ino"), ("i", "ino"), ("u", "uno"), ("ū", "uno"), ("ā", "ā")):
        if p.endswith(a) and p[:-len(a)] + b in T:
            return p[:-len(a)] + b
    if p.endswith("āti") and p[:-2] in T:          # the closing «ti» of a section («… siyā araṇāti.»)
        return p[:-2]
    raise Miss("mātikā term: " + p)


CEVA_RE = re.compile(r"(?P<x>\S+?)(?P<n>ñceva| ceva) (?P<y>\S+) c[aā]")
CEVANO_RE = re.compile(r"(?P<y>\S+) ceva (?:no|na) ca (?P<x>\S+)")


def term_my(p):
    """Burmese attributive of a mātikā term (also «X ceva Y ca», «Y ceva no ca X»)."""
    m = CEVA_RE.fullmatch(p)
    if m:
        x = m["x"] + ("ṃ" if m["n"] == "ñceva" else "")
        k = (term_key(x), term_key(m["y"]))
        if k not in CEVA:
            raise Miss("ceva: " + p)
        return CEVA[k]
    m = CEVANO_RE.fullmatch(p)
    if m:
        k = (term_key(m["y"]), term_key(m["x"]))
        if k not in CEVANO:
            raise Miss("ceva no: " + p)
        return CEVANO[k]
    if p in INDR:
        return INDR[p] + " ဖြစ်သော"                   # a faculty as a kind («X ဖြစ်သော KN»)
    return T[term_key(p)]


# ===================================================================================== the eleven qualifiers
PRED = C3["PRED"]
Q11A = {    # attributive, before the noun (pi-1 TERMS / Rūpakaṇḍa)
    "atīta": T["atītā"], "anāgata": T["anāgatā"], "paccuppanna": T["paccuppannā"],
    "ajjhatta": T["ajjhattā"], "bahiddhā": T["bahiddhā"],
    "oḷārika": PRED["oḷārikaṃ"], "sukhuma": PRED["sukhumaṃ"], "hīna": T["hīnā"], "paṇīta": T["paṇītā"],
    "dūre": PRED["dūre"], "santike": PRED["santike"],
}
NOUNLIKE = ("atīta", "anāgata", "paccuppanna")
Q11V = {k: (v + "ဖြစ်စေ" if k in NOUNLIKE else stem(v) + "သည်ဖြစ်စေ") for k, v in Q11A.items()}   # «X vā»
Q11P = {k: stem(v) for k, v in Q11A.items() if k not in NOUNLIKE}      # predicate stem (+ ကြ) + သည်
Q11_FORMS = {}
for _k in Q11A:
    for _e in (("aṃ", "ā") if _k not in ("bahiddhā", "dūre", "santike") else ("",)):
        Q11_FORMS[(_k[:-1] + _e) if _e else _k] = _k
Q11_FORMS.update({"bahiddhā": "bahiddhā", "dūre": "dūre", "santike": "santike"})
FAR, NEAR = "ဝေး", "နီး"               # «X N Y-N-abl dūre / -gen santike» = «Nနှင့် ဝေးသည် / နီးသည်»
VA_OR = "သို့မဟုတ်"                    # vā pana (or else)
COMPARE = "နှင့် နှိုင်းယှဉ်၍"           # upādāyupādāya (relative to)
SHOULD = "မှတ်ယူရမည်"                  # daṭṭhabba (should be regarded)
SUMMARY_END = "ထိုအားလုံးကို တစ်စုတည်း ပေါင်းစု၍ အကျဉ်းချုံ့၍"   # tadekajjhaṃ abhisaññūhitvā abhisaṅkhipitvā


# ===================================================================================== definition lists
def _p1_line(ch, bid):
    for l in (P1_RAILS / ch).read_text(encoding="utf-8").splitlines():
        if l.endswith(" ^" + bid):
            return l[:-len(bid) - 2]
    raise SystemExit("pi-1 line not found: " + bid)


def dkey(w):
    """Definition-list word / phrase in any gender -> key (stem without the case ending)."""
    w = w.replace("upādinn", "upādiṇṇ")
    out = []
    for x in w.split(" "):
        for e in ("aṃ", "ā", "o"):
            if x.endswith(e) and len(x) > 3:
                x = x[:-len(e)]
                break
        out.append(x)
    return " ".join(out)


DEF = {}            # key -> Burmese attributive (one Pāli item = one Burmese item)
DEF_SRC = {}        # key -> pi-1 block id (reused) or "new"
_P1LISTS = {        # pi-1 4-01 ids -> Pāli items (in order)
    "1-1044": "atītā|niruddhā|vigatā|vipariṇatā|atthaṅgatā|abbhatthaṅgatā|uppajjitvā vigatā|atītā|atītaṃsena saṅgahitā",
    "1-1045": "ajātā|abhūtā|asañjātā|anibbattā|anabhinibbattā|apātubhūtā|anuppannā|asamuppannā|anuṭṭhitā|asamuṭṭhitā|"
              "anāgatā|anāgataṃsena saṅgahitā",
    "1-1046": "jātā|bhūtā|sañjātā|nibbattā|abhinibbattā|pātubhūtā|uppannā|samuppannā|uṭṭhitā|samuṭṭhitā|paccuppannā|"
              "paccuppannaṃsena saṅgahitā",
    "1-1050": "ajjhattaṃ|paccattaṃ|niyatā|pāṭipuggalikā|upādiṇṇā",
}
YE_GEN = {"tesaṃ tesaṃ sattānaṃ": "ထိုထို သတ္တဝါတို့၏",            # pi-1 make_ch4 YE_GEN (final ^1-1050 / 1051)
          "tesaṃ tesaṃ parasattānaṃ parapuggalānaṃ": "ထိုထို အခြား သတ္တဝါ၊ အခြား ပုဂ္ဂိုလ်တို့၏"}
for _id, _items in _P1LISTS.items():
    _b = _p1_line("4-01-nikkhepakandam.md", _id).split(END + " ", 1)[1]
    for _g in YE_GEN.values():
        _b = _b.removeprefix(_g + " ")
    _b = _b.split(f" {DHP}{C} {RUPA}{C}")[0].split(f"{C} ")
    _items = _items.split("|")
    if len(_b) != len(_items):
        raise SystemExit(f"pi-1 list {_id}: {len(_items)} Pāli / {len(_b)} Burmese items")
    for _p, _m in zip(_items, _b):
        if DEF.get(dkey(_p), _m) != _m:
            raise SystemExit("pi-1 list conflict " + _p)
        DEF[dkey(_p)] = _m
        DEF_SRC[dkey(_p)] = "^" + _id
_NEW_DEF = {
    # ajjhatta (Vb «niyaka» = one's own; Dhs «niyatā» = သီးသန့် ဖြစ်သော is another word)
    "niyakaṃ": "ကိုယ်ပိုင် ဖြစ်သော",
    # hīna (after «tesaṃ tesaṃ sattānaṃ» = agent «ထိုထို သတ္တဝါတို့က»)
    "uññātaṃ": "အထင်သေးထားသော", "avaññātaṃ": "လျစ်လျူရှုထားသော", "hīḷitaṃ": "ကဲ့ရဲ့ထားသော",
    "paribhūtaṃ": "စော်ကားထားသော", "acittīkataṃ": "အလေးမထားသော", "hīnaṃ": T["hīnā"],
    "hīnamataṃ": "ယုတ်ညံ့သည်ဟု ယူဆထားသော", "hīnasammataṃ": "ယုတ်ညံ့သည်ဟု အများ သတ်မှတ်ထားသော",
    "aniṭṭhaṃ": "လိုလားဖွယ် မကောင်းသော", "akantaṃ": "ချစ်ခင်ဖွယ် မကောင်းသော",
    "amanāpaṃ": C3["AMANAPA"],
    # paṇīta
    "anuññātaṃ": "အထင်မသေးထားသော", "anavaññātaṃ": "လျစ်လျူ မရှုထားသော", "ahīḷitaṃ": "မကဲ့ရဲ့ထားသော",
    "aparibhūtaṃ": "မစော်ကားထားသော", "cittīkataṃ": "အလေးထားသော", "paṇītaṃ": T["paṇītā"],
    "paṇītamataṃ": "မွန်မြတ်သည်ဟု ယူဆထားသော", "paṇītasammataṃ": "မွန်မြတ်သည်ဟု အများ သတ်မှတ်ထားသော",
    "iṭṭhaṃ": "လိုလားဖွယ်ကောင်းသော", "kantaṃ": "ချစ်ခင်ဖွယ်ကောင်းသော", "manāpaṃ": C3["MANAPA"],
    # dūre / santike (after «yaṃ vā panaññampi atthi rūpaṃ»)
    "anāsanne": "မနီးကပ်သော", "anupakaṭṭhe": "အနားမကပ်သော", "dūre": PRED["dūre"], "asantike": "အနီး၌ မရှိသော",
    "āsanne": "နီးကပ်သော", "upakaṭṭhe": "အနားကပ်သော", "avidūre": "မဝေးလှသော", "santike": PRED["santike"],
}
for _p, _m in _NEW_DEF.items():
    DEF[dkey(_p)] = _m
    DEF_SRC[dkey(_p)] = "new"
DEF_MAXLEN = 4
AGENT = {"tesaṃ tesaṃ sattānaṃ": "ထိုထို သတ္တဝါတို့က"}       # before uññātaṃ … / anuññātaṃ … (by those beings)
YAM_VA = "အခြား"                                               # yaṃ vā panaññampi atthi rūpaṃ L … (pi-1 frame)

# content after the definition (CONTENT) and list items (ITEM)
MAHABHUTA2 = C3["FIXED"]["Cattāro ca mahābhūtā, catunnañca mahābhūtānaṃ upādāya rūpaṃ"]
CONTENT = {"cattāro ca mahābhūtā catunnañca mahābhūtānaṃ upādāyarūpaṃ": MAHABHUTA2}
SRC = dict(SENSE)
SRC.update({"mano": P1.MANO, "manodhātu": f"{P1.MANO} ဓာတ်", "manoviññāṇadhātu": P1.NAMES["manoviññāṇadhātu"]})
ITEM = {}
for _p, _m in SRC.items():
    for _n, _nm in (("vedanā", P1.FEEL), ("saññā", P1.SANNA), ("cetanā", P1.CETANA)):
        ITEM[f"{_p}samphassajā {_n}"] = f"{_m}၏ {P1.PHASSA}မှ ဖြစ်ပေါ်သော {_nm}"      # pi-1 3-02 ^1-599 form
for _p in list(SENSE) + ["mano"]:
    ITEM[_p + "viññāṇaṃ"] = f"{SRC[_p]} {P1.VINNANA}"
ITEM["manodhātu"] = SRC["manodhātu"]
ITEM["manoviññāṇadhātu"] = SRC["manoviññāṇadhātu"]
ITEM["sukhā vedanā"] = f"{P1.SUKHA}သော {P1.FEEL}"
ITEM["dukkhā vedanā"] = f"{P1.DUKKHA}သော {P1.FEEL}"
ITEM["adukkhamasukhā vedanā"] = f"မ{P1.DUKKHA} မ{P1.SUKHA}သော {P1.FEEL}"
for _p, _o in (("rūpā", "rūpa"), ("saddā", "sadda"), ("gandhā", "gandha"), ("rasā", "rasa"), ("phoṭṭhabbā", "phoṭṭhabba")):
    ITEM[_p] = OBJECT[_o]
for _k, _v in C3["NOUN"].items():
    if _k.endswith(("āyatanaṃ", "ndriyaṃ")) or _k in ("kabaḷīkāro āhāro",) or _k in C3["ELEM"]:
        ITEM.setdefault(_k, _v)
for _k in KH_ORDER:
    ITEM[_k] = KH[_k][0]
ITEM["jīvitindriyaṃ"] = P1.NAMES["jīvitindriyaṃ"]
PACCAYA = {_p: f"{SRC[_p]}၏ {P1.PHASSA}ကို အကြောင်းပြု၍ ဖြစ်သော" for _p in list(SENSE) + ["mano"]}  # Xsamphassapaccayā

# statement qualifiers of the oḷārika / hīna / dūre passages: canonical Pāli -> (attributive or (A, B), plural)
_SU, _DU = f"{P1.SUKHA}သော", f"{P1.DUKKHA}သော"
_AD = f"မ{P1.DUKKHA} မ{P1.SUKHA}သော"
_F = P1.FEEL
_ABY = T["abyākatā"]
QV = {
    "akusal": (T["akusalā"], False), "kusal": (T["kusalā"], False), "abyākat": (_ABY, False),
    "kusalābyākat": ((T["kusalā"], _ABY), True), "akusalābyākat": ((T["akusalā"], _ABY), True),
    "kusalākusal": ((T["kusalā"], T["akusalā"]), True),
    "dukkh": (_DU, False), "sukh": (_SU, False), "adukkhamasukh": (_AD, False),
    "sukh ca adukkhamasukh ca": ((_SU, _AD), True), "dukkh ca adukkhamasukh ca": ((_DU, _AD), True),
    "sukhadukkh": ((_SU, _DU), True),
    "sāsav": (T["sāsavā"], False), "anāsav": (T["anāsavā"], False),
    "asamāpann": ("ဈာန် မဝင်စားသူ၏", False), "samāpann": ("ဈာန် ဝင်စားသူ၏", False),   # pi-1 ^1-1289 samāpannassa
    "paṭighasamphassaj": (f"{P1.IMPACT}၏ {P1.PHASSA}မှ ဖြစ်ပေါ်သော", False),
    "adhivacanasamphassaj": (f"{T['adhivacanā'].removesuffix(' ဖြစ်သော')}၏ {P1.PHASSA}မှ ဖြစ်ပေါ်သော", False),
    "dukkh vedan sampayutt": (T["dukkhāya vedanāya sampayuttā"], False),
    "sukh vedan sampayutt": (T["sukhāya vedanāya sampayuttā"], False),
    "adukkhamasukh vedan sampayutt": (T["adukkhamasukhāya vedanāya sampayuttā"], False),
    "sukh ca adukkhamasukh ca vedan sampayutt": (f"{_SU} {_F}နှင့် {_AD} {_F}တို့{SAMP}", True),
    "dukkh ca adukkhamasukh ca vedan sampayutt": (f"{_DU} {_F}နှင့် {_AD} {_F}တို့{SAMP}", True),
    "sukhadukkh vedan sampayutt": (f"{_SU} {_F}နှင့် {_DU} {_F}တို့{SAMP}", True),
}
CASE_END = ("ānaṃ", "āhi", "āya", "ehi", "assa", "aṃ", "ā", "o", "e")


def qv_key(q):
    out = []
    for w in q.split(" "):
        w = w[0].lower() + w[1:]
        if w != "ca":
            for e in CASE_END:
                if w.endswith(e) and len(w) > len(e) + 2:
                    w = w[:-len(e)]
                    break
        out.append(w)
    k = " ".join(out)
    if k not in QV:
        raise Miss("qualifier: " + q)
    return k


def np_my(n, q):
    """«QUAL NOUN» -> (Burmese, plural)."""
    a, pl = QV[qv_key(q)]
    pl = pl or NOUN[n]["pl"]
    base = NOUN[n]["my"]
    if isinstance(a, tuple):
        s = f"{a[0]} {base}နှင့် {a[1]} {base}"
    else:
        s = f"{a} {base}"
    return s + ("များ" if pl else ""), pl


# ===================================================================================== abhidhamma part
NUMW = dict(C3["NUMW"])
NUMW.update({"catuvīsati": "နှစ်ဆယ့်လေး", "tiṃsati": "သုံးဆယ်", "tiṃsa": "သုံးဆယ်"})
KIND = C3["KIND"]                                  # မျိုး (pi-1 -vidhena)
VIDHA = {}
for _p, _m in NUMW.items():
    VIDHA[(_p + "bidhena") if _p in ("catub", "chab") else (_p + "vidhena")] = f"{_m}{KIND}ဖြင့်"
VIDHA["bahuvidhena"] = f"အ{KIND}{KIND}ဖြင့်"         # in many ways
LOOK = "ကြည့်လျှင်"                                 # «Xvidhena K –» = «Nမျိုးဖြင့် ကြည့်လျှင် K –»
APARO = "နောက်တစ်နည်းဖြင့်"                         # Aparopi
EVAM = "ဤသို့"                                     # Evaṃ … K = «ဤသို့ Nမျိုးဖြင့် ကြည့်လျှင် K ဖြစ်သည်»
IN = "တွင်"                                         # «X atthi T» = «Xတွင် T KN ရှိသည်» (pi-1 ^1-592)
C3["EKA_SPECIAL"]["nevācayagāmināpacayagāmī"] = "nevācayagāmināpacayagāmino"     # in memory only
VINNEYYA = C3["VINNEYYA"]

# ===================================================================================== pañhāpucchaka
SIYA = "တစ်ခါတစ်ရံ"                                 # siyā (pi-1 termbase)
NVATT = "ခေါ်ဆို၍ မရ"                               # na vattabbo / ā (pi-1 ^1-1198)
TIPI, TI = "ဟုလည်းကောင်း", "ဟု"                    # "X"tipi / "X"ti
KATI = "မည်မျှ"                                     # kati
KATI_END = "ရှိသနည်း"
AMONG_KH = f"{KH['pañcakkhandhā'][0]}တို့အနက်"       # Pañcannaṃ khandhānaṃ


# ===================================================================================== the engine
STATE = {}
EXTRA_RULES = []
RULES = []
W = r"[\wāīūṃṅñṭḍṇḷ]"
NA = r"(?![\wāīūṃṅñṭḍṇḷ])"


def _alt(keys):
    return "(?:" + "|".join(f"[{k[0].upper()}{k[0]}]" + re.escape(k[1:])
                            for k in sorted(keys, key=len, reverse=True)) + ")"


def _esc(keys):
    return "(?:" + "|".join(re.escape(k) for k in sorted(keys, key=len, reverse=True)) + ")"


def _low(s):
    return s[0].lower() + s[1:]


# ---- general
def r_pancakkhandha(m):
    return KH["pañcakkhandhā"][0]


def r_question_kh(m):
    STATE["noun"] = None
    return f"ထိုတို့အနက် {kh(m['k'])[0]} ဟူသည် အဘယ်နည်း"


def r_question_q(m):
    n = NOUN_PI[m["n"]]
    STATE["noun"] = n
    qs = [Q11_FORMS[w] for w in m["q"].split(" ")]
    pl = NOUN[n]["pl"] or len(qs) > 1
    np_ = "နှင့် ".join(f"{Q11A[q]} {nmy(n)}" for q in qs)
    return f"ထိုတို့အနက် {np_} ဟူသည် အဘယ်{'တို့' if pl else ''}နည်း"


def r_vuccati(m):
    x = m["x"]
    pl = m["v"] == "vuccanti"
    if _low(x) in KH:
        name = kh(x)[0]
    else:
        mm = re.fullmatch(r"(?P<n>\S+) (?P<q>\S+)", x)
        if not mm or mm["n"] not in NOUN_PI or mm["q"] not in Q11_FORMS:
            raise Miss("vuccati: " + x)
        name = f"{Q11A[Q11_FORMS[mm['q']]]} {nmy(NOUN_PI[mm['n']])}"
    return f"ဤသည်{'တို့' if pl else ''}ကို {name}ဟု ခေါ်သည်"


def r_summary(m):
    n = NOUN_PI[m["n"]]
    v = Q11V
    head = (f"{v['atīta']}{C} {v['anāgata']}{C} {v['paccuppanna']}{C} {v['ajjhatta']}{C} {v['bahiddhā']}{C} "
            f"{v['oḷārika']}{C} {v['sukhuma']}{C} {v['hīna']}{C} {v['paṇīta']}{C} {v['dūre']}{C} {v['santike']}")
    sep = C if m["c"] else ""
    return f"{head} မည်သည့် {nmy(n)}မဆို{sep} {SUMMARY_END}"


def def_items(text):
    toks = text.split(" ")
    out, i = [], 0
    while i < len(toks):
        for k in range(DEF_MAXLEN, 0, -1):
            key = dkey(" ".join(toks[i:i + k]))
            if len(toks[i:i + k]) == k and key in DEF:
                out.append(key)
                i += k
                break
        else:
            raise Miss("definition item: " + toks[i])
    return out


def r_deflist(m):
    n = NOUN_PI[m["n"]]
    STATE["noun"] = n
    lst, head = m["list"], ""
    if m["ag"]:
        head = AGENT[m["ag"]] + " "
    for g, gm in YE_GEN.items():
        if lst.startswith(g + " "):
            head, lst = gm + " ", lst[len(g) + 1:]
    keys = def_items(lst)
    STATE.setdefault("lists", []).append(keys)
    return head + f"{C} ".join(DEF[k] for k in keys) + f" {nmy(n)} ရှိသမျှ"


def r_content(m):
    return CONTENT[m[0]]


def _item_tail(m):
    return IN if m.string.startswith(" atthi ", m.end()) else ""


def r_itemrun(m):
    toks = m[0].split(" ")
    out, i = [], 0
    while i < len(toks):
        for k in (2, 1):
            key = _low(" ".join(toks[i:i + k]))
            if len(toks[i:i + k]) == k and key in ITEM:
                out.append(ITEM[key])
                i += k
                break
        else:
            raise Miss("item: " + toks[i])
    return f"{C} ".join(out) + _item_tail(m)


def r_item(m):
    return ITEM[_low(m[0])] + _item_tail(m)


def r_compare(m):
    n = NOUN_PI[m["n2"]]
    a, b = (Q11P[Q11_FORMS[w]] for w in m["q"].split(" "))
    N = nmy(n)
    return f"{VA_OR} ထိုထို {N}{COMPARE} {N}ကို {a}သည်{TIPI}{C} {b}သည်{TIPI} {SHOULD}"


PRED_Q = {"oḷārik": "oḷārika", "sukhum": "sukhuma", "hīn": "hīna", "paṇīt": "paṇīta"}


def _split_np(words, n):
    for i, w in enumerate(words):
        if w in NOUN[n]["forms"] and i > 0:
            return " ".join(words[:i]), words[i + 1:]
    raise Miss("noun phrase: " + " ".join(words))


def r_statement(m):
    n = STATE.get("noun")
    if not n:
        return None
    words = m[0].split(" ")
    q1, rest = _split_np(words, n)
    np1, pl1 = np_my(n, q1)
    k = "ကြ" if pl1 else ""
    if len(rest) == 1:
        p = re.sub(r"(?:aṃ|ā)$", "", rest[0])
        if p in PRED_Q:
            return f"{np1}သည် {Q11P[PRED_Q[p]]}{k}သည်"
    if rest and rest[-1] in ("dūre", "santike"):
        q2, rest2 = _split_np(rest[:-1], n)
        if rest2:
            raise Miss("statement: " + m[0])
        np2, _ = np_my(n, q2)
        return f"{np1}သည် {np2}{'မှ' if rest[-1] == 'dūre' else 'နှင့်'} {FAR if rest[-1] == 'dūre' else NEAR}{k}သည်"
    raise Miss("statement: " + m[0])


def r_yamva(m):
    keys = def_items(m["list"])
    STATE.setdefault("lists", []).append(keys)
    return f"{C} ".join(DEF[k] for k in keys) + f" {YAM_VA} {RUPA} ရှိသမျှလည်း"


# ---- abhidhamma part
def r_vidha(m):
    name, n, _ = kh(m["k"])
    STATE["kh"] = n
    pre = (APARO + " ") if m["ap"] else ""
    return f"{pre}{VIDHA[m['v'].lower()]} {LOOK} {name}"


def r_evam(m):
    return f"{EVAM} {VIDHA[m['v'].lower()]} {LOOK} {kh(m['k'])[0]} {COP[False]}"


def r_atthi(m):
    n = STATE.get("kh")
    if not n or n == "rūpa":
        return None
    return f"{term_my(m['t'])} {NOUN[n]['my']} {HOTI}"


def r_pred_bare(m):
    return f"{term_my(m['t'])} {DH} {COP[False]}"


def r_paccaya(m):
    out = PACCAYA[_low(m["s"])]
    if m["k"]:
        out += " " + kh(m["k"])[0] + _item_tail(m)
    return out


def r_sabbam(m):
    return C3["r_ekaka"]({"l": m["l"]})


def r_yamtam_nocomma(m):
    return C3["r_yam_tam"](m) + C


def r_vinneyya_atthi(m):
    return f"{VINNEYYA[m['p']]} {RUPA}{IN}"


def r_catu(m):
    return C3["FIXED"]["Diṭṭhaṃ sutaṃ mutaṃ viññātaṃ rūpaṃ"]


def r_matter(m):
    return None                                    # placeholder (the C3 rules are tried in clauses_my)


# ---- pañhāpucchaka
def r_kati_head(m):
    STATE["pl"] = True
    return AMONG_KH


def r_kati_t(m):
    end = " " + KATI_END if m.string.startswith("?", m.end()) else ""
    return f"{term_my(m['t'])} {DH} {KATI}{end}"


def r_subj(m):
    name, n, pl = kh(m["s"])
    STATE["pl"] = pl
    if m["nv"]:
        STATE["nv"] = True
    return f"{name}သည်"


def _dh(pl=None):
    pl = STATE.get("pl", False) if pl is None else pl
    return DHP if pl else DH


QUOTE_RE = re.compile(r'"?(?P<q>[^"]+?)"(?P<t>ntipi|nti|ti ?pi|ti)?(?=, |\.|;|$)')


def r_quotes(m):
    """The quotes after «na vattabbo –» / «siyā na vattabbo –»: “A …”ဟုလည်းကောင်း၊ … ခေါ်ဆို၍ မရ."""
    if not STATE.get("nv"):
        return None
    STATE["nv"] = False
    text, pos, parts = m["q"], 0, []
    while pos < len(text):
        mm = QUOTE_RE.match(text, pos)
        if not mm:
            raise Miss("quote: " + text[pos:pos + 60])
        q, t = mm["q"], mm["t"] or ""
        if t.startswith("n"):
            q, t = q + "ṃ", t[1:]
        open_q = "“" if text[mm.start()] == '"' else ""        # a missing opening quote is kept as written
        word = {"tipi": TIPI, "ti pi": TIPI, "ti": TI, "": None}[t]
        parts.append((f"{open_q}{term_my(q)} {_dh()}”", word))
        pos = mm.end()
        if text.startswith(", ", pos):
            pos += 2
    out = []
    for i, (q, w) in enumerate(parts):
        if w is None:                      # a quoted statement without «ti» (source slip): «… ” ဖြစ်သည်»
            if i == 0:
                raise Miss("quote without ti first")
            out.append(f"{C} {q} {COP[STATE.get('pl', False)]}")
            continue
        if i and parts[i - 1][1] is not None:
            out.append(f"{C} ")
        out.append(q + w)
        if i == len(parts) - 1 or parts[i + 1][1] is None:
            out.append(" " + NVATT)
    return "".join(out)


def r_siya_nv(m):
    STATE["nv"] = True
    return SIYA


def r_siya(m):
    t = m["t"]
    pl = STATE.get("pl", False)
    mm = re.fullmatch(r"(?P<a>\S+) na (?P<b>\S+) na (?P<c>\S+)", t)
    if mm:
        body = f"{C} ".join([term_my(mm["a"]), term_my("na " + mm["b"]), term_my("na " + mm["c"])])
    else:
        body = term_my(t)
    return f"{SIYA} {body} {_dh()} {COP[pl]}"


def r_bare(m):
    if "pl" not in STATE:
        return None
    return f"{term_my(m['t'])} {_dh()} {COP[STATE['pl']]}"


SEP = [("…pe…. ", PE + END + " "), ("…pe….", PE + END), (" …pe… ", PE + " "), ("…pe… ", PE + " "), ("…pe…", PE),
       ("? ", END + " "), ("?", END), ("; ", C + " "), (", ", C + " "), (" – ", " – "), (". ", END + " "),
       (".", END), (" ", " ")]


def rebuild():
    kh_alt = _alt(KH)
    vidha = _alt(VIDHA)
    q11 = _esc(Q11_FORMS)
    nouns = _esc(NOUN_PI)
    items = _alt(ITEM)
    tw = r"(?!atthi(?: |$)|siyā )" + W + "+"
    term = r"(?:" + tw + r"(?: " + tw + r"){0,8}?)"
    end = r"(?=, |\. |\.$|; |;|…| …|$| – |\?| atthi )"
    rules = [
        (r"Pañcakkhandhā(?= – )", r_pancakkhandha),
        (r"Tattha katam(?:o|ā|aṃ|e) (?P<k>" + kh_alt + r")(?=\?)", r_question_kh),
        (r"Tattha katam(?:o|ā|aṃ|e) (?P<n>" + nouns + r") (?P<q>" + q11 + r"(?: " + q11 + r")?)(?=\?)", r_question_q),
        (r"(?:[Aa]yaṃ|[Ii]daṃ|[Ii]me) (?P<v>vuccati|vuccanti) (?P<x>[^.–;?]+?)(?=\.|$)", r_vuccati),
        (r"(?:Yaṃ kiñci|Yā kāci|Ye keci) (?P<n>" + nouns + r") atītānāgatapaccuppann\w+ ajjhatt\w+ vā bahiddhā vā "
         r"oḷārik\w+ vā sukhum\w+ vā hīn\w+ vā paṇīt\w+ vā (?:yaṃ|yā|ye) dūre santike vā(?P<c>,)? tadekajjhaṃ "
         r"abhisaññūhitvā abhisaṅkhipitvā", r_summary),
        (r"(?:Yaṃ|Yā|Ye) (?P<n>" + nouns + r") (?:(?P<ag>tesaṃ tesaṃ sattānaṃ)(?= (?:uññātaṃ|anuññātaṃ)) )?"
         r"(?P<list>[^,]+?)(?=,)", r_deflist),
        (_esc(CONTENT), r_content),
        (r"(?:[Tt]aṃ taṃ|Te te) vā pana (?:rūpaṃ|vedanaṃ|saññaṃ|viññāṇaṃ|saṅkhāre) upādāyupādāya (?P<n2>" + nouns
         + r") (?P<q>" + q11 + r" " + q11 + r") daṭṭhabb(?:aṃ|ā)", r_compare),
        (r"kabaḷīkāro (?P<v>\[[^\]]+\]) āhāro",
         lambda m: f"{stem(PRED['kabaḷīkāro āhāro']).removesuffix(' ' + P1.AHARA + ' ဖြစ်')} {var_my(m['v'])} "
                   f"{P1.AHARA}" + _item_tail(m)),
        (r"yaṃ vā panaññampi atthi rūpaṃ (?P<list>[^–]+?)(?= – )", r_yamva),
        # abhidhamma part
        (r"(?P<ap>Aparopi )?(?P<v>" + vidha + r") (?P<k>" + kh_alt + r")" + NA, r_vidha),
        (r"[Ee]vaṃ (?P<v>" + vidha + r") (?P<k>" + kh_alt + r")" + NA, r_evam),
        (r"sabbaṃ rūpaṃ (?P<l>na hetu, .+?, jarābhibhūtaṃ)(?=\.)", r_sabbam),
        (r"[Yy]aṃ taṃ rūpaṃ (?P<p>" + C3["CHAIN"] + r")(?= taṃ )", r_yamtam_nocomma),
        (r"(?P<p>" + _esc(VINNEYYA) + r") rūpaṃ(?= atthi )", r_vinneyya_atthi),
        (r"diṭṭhaṃ, sutaṃ, mutaṃ, viññātaṃ rūpaṃ", r_catu),
        ("MATTER", None),
        (r"(?P<s>(?:[Cc]akkhu|[Ss]ota|[Gg]hāna|[Jj]ivhā|[Kk]āya|[Mm]ano))samphassapaccayā(?: (?P<k>" + kh_alt + r"))?"
         + NA, r_paccaya),
        (r"[Aa]tthi (?P<t>" + term + r")" + end, r_atthi),
        (r"(?P<t>phassasampayutto|cittasampayutto)" + NA, r_pred_bare),
        # pañhāpucchaka
        (r"Pañcannaṃ khandhānaṃ(?= kati)", r_kati_head),
        (r"kati (?P<t>" + term + r")" + end, r_kati_t),
        (r"(?P<s>" + kh_alt + r")(?P<nv> na vattabb(?:o|ā)(?= – ))?(?= )",
         lambda m: r_subj(m) if STATE.get("part") == "pan" else None),
        (r'(?P<q>"?[^"–]+"(?:ntipi|nti|ti ?pi|ti)?(?:, "[^"]+"(?:ntipi|nti|ti ?pi|ti)?)*)(?=\.|;|, (?!")|$)',
         r_quotes),
        (r"siyā na vattabb(?:o|ā)(?= – )", r_siya_nv),
        (r"siyā (?P<t>" + term + r")(?=, |\.|;|$)", r_siya),
        # statements of the suttanta oḷārika / dūre passages (topic noun set by the question)
        (r"(?:[Aa]kusal|[Kk]usal|[Aa]byākat|[Dd]ukkh|[Ss]ukh|[Aa]dukkhamasukh|[Aa]samāpann|[Ss]amāpann|[Ss]āsav|"
         r"[Aa]nāsav|[Pp]aṭighasamphass|[Aa]dhivacanasamphass)[^;.,–]*?(?: (?:oḷārik\w*|sukhum\w*|hīn\w*|paṇīt\w*|dūre|"
         r"santike))(?=[;.,]| –)", r_statement),
        # list items
        (r"(?:" + items + r")(?: (?:" + items + r"))+(?= – |, |\.)", r_itemrun),
        (items + NA, r_item),
        (r"(?P<t>" + term + r")(?=, |\.|;|$|…)", r_bare),
    ]
    RULES[:] = [(p if p == "MATTER" else re.compile(p), f) for p, f in list(EXTRA_RULES) + rules]


rebuild()
C3_RULES = list(P1.CU_EXTRA_RULES)        # the Rūpakaṇḍa frames (atthi rūpaṃ P, taṃ atthi P, yañca rūpaṃ P …)


def clauses_my(s):
    pos, out = 0, []
    while pos < len(s):
        for p, my in SEP:
            if s.startswith(p, pos):
                out.append(my)
                pos += len(p)
                break
        else:
            for rx, f in RULES:
                if rx == "MATTER":
                    if STATE.get("kh") != "rūpa":
                        continue
                    hit = None
                    for rx3, f3 in C3_RULES:
                        m = rx3.match(s, pos)
                        if m and m.end() > pos:
                            hit = (m, f3)
                            break
                    if hit:
                        out.append(hit[1](hit[0]))
                        pos = hit[0].end()
                        break
                    continue
                m = rx.match(s, pos)
                if m and m.end() > pos:
                    r = f(m)
                    if r is None:
                        continue
                    out.append(r)
                    pos = m.end()
                    break
            else:
                raise Miss("no frame: " + s[pos:pos + 100])
    return "".join(out)


ID_RE = re.compile(r" (\^[0-9A-Za-z-]+)\s*$")
HEAD_RE = re.compile(r"(?P<h>#+) (?P<t>.+?)$")
PART = {"Suttantabhājanīyaṃ": "sut", "Abhidhammabhājanīyaṃ": "abh", "Pañhāpucchakaṃ": "pan"}
FIXED = {   # whole lines that are not built from a frame
    "Sappaccayā, saṅkhatā.": f"{T['sappaccayā']} {DHP} {COP[True]}{C} {T['saṅkhatā']} {DHP} {COP[True]}{END}",
}


def line_my(body):
    for k in ("pl", "nv"):
        STATE.pop(k, None)
    body = body.replace("upādinn", "upādiṇṇ")        # Vb spelling -> the pi-1 keys (same word)
    if body in FIXED:
        return FIXED[body]
    m = HEAD_RE.fullmatch(body)
    if m:
        if m["t"] not in HEAD:
            raise Miss("heading: " + body)
        if m["t"] in PART:
            STATE["part"] = PART[m["t"]]
        return f"{m['h']} {HEAD[m['t']]}"
    if body.endswith(".") and body[:-1] in COLO:
        return COLO[body[:-1]] + END
    m = re.fullmatch(r"\((?P<t>.+)\)", body)
    if m:
        if m["t"] not in EDIT:
            raise Miss("editorial: " + body)
        return f"({EDIT[m['t']]})"
    return clauses_my(body)


def translate_line(line):
    if not line.strip():
        return ""
    m = ID_RE.search(line)
    body = line[:m.start()] if m else line
    return line_my(body) + (" " + m.group(1) if m else "")


# ===================================================================================== consistency pass (2026-11-18)
# One Burmese form per Pāli item across the book (harmonise-todo.md; reasons, counts and the generators that read each
# value: harmonise-notes.md). Precedence: pi-1 final Burmese for identical Pāli; the approved sample; the majority of
# the chapters; the plainest. Nothing above this block was changed; the generators read these values.
def _p1_views():
    """The ten views of the final pi-1 text (4-01 «Sassato lokoti vā, asassato lokoti vā …»), item by item."""
    for l in (P1_RAILS / "4-01-nikkhepakandam.md").read_text(encoding="utf-8").splitlines():
        if l.startswith("လောကသည် ထာဝရ တည်မြဲသည်ဟူ၍ဖြစ်စေ"):
            vs = l.split(f"ဟူ၍ဖြစ်စေ{C} ဤသို့")[0].split(f"ဟူ၍ဖြစ်စေ{C} ")
            assert len(vs) == 10, vs
            return vs
    for l in (P1_RAILS / "4-01-nikkhepakandam.md").read_text(encoding="utf-8").splitlines():
        if "လောကသည် ထာဝရ တည်မြဲသည်ဟူ၍ဖြစ်စေ" in l:
            s = l[l.index("လောကသည် ထာဝရ တည်မြဲသည်ဟူ၍ဖြစ်စေ"):]
            vs = s.split(f"ဟူ၍ဖြစ်စေ{C} ဤသို့")[0].split(f"ဟူ၍ဖြစ်စေ{C} ")
            assert len(vs) == 10, vs
            return vs
    raise SystemExit("pi-1 ten views not found")


VIEW10 = dict(zip(["sassato loko", "asassato loko", "antavā loko", "anantavā loko", "taṃ jīvaṃ taṃ sarīraṃ",
                   "aññaṃ jīvaṃ aññaṃ sarīraṃ", "hoti tathāgato paraṃ maraṇā", "na hoti tathāgato paraṃ maraṇā",
                   "hoti ca na ca hoti tathāgato paraṃ maraṇā", "neva hoti na na hoti tathāgato paraṃ maraṇā"],
                  _p1_views()))
TI_VA = "ဟူ၍ဖြစ်စေ"              # «X"ti vā» (pi-1 frame of the views list; ch17 had «ဟုဖြစ်စေ»)
SIG_UNKNOWN = "အမည်မသိ မူ"       # the editors' «(?)» (ch17, ch18: 4 uses; ch2-4 had «ရင်းမြစ် မသေချာ»)
UPAPATTI = "ပြန်လည် ဖြစ်ပေါ်ခြင်း"  # upapatti (noun): ch18 (55 lines), pi-1 upapattiyā «ဖြစ်ပေါ်ရန်»
ADHIMOKKHA = "ဆုံးဖြတ်မှု"         # adhimokkha: ch6 (150 uses); ch18 had «ဆုံးဖြတ်ချက်»
UPK = "စွဲလမ်းမှု၏ အာရုံ ဖြစ်သော"   # -upādānakkhandha (ch4, ch7); ch12 had «… ဖြစ်နိုင်သော»
TRUTH = {   # the four truths as written (ch4: 41 / 40 uses); ch18 had «ဒုက္ခ ဖြစ်ပေါ်ခြင်း / ချုပ်ငြိမ်းခြင်း သစ္စာ»
    "dukkhasaccaṃ": "ဒုက္ခ သစ္စာ", "samudayasaccaṃ": "ဖြစ်ပေါ်ခြင်း သစ္စာ",
    "nirodhasaccaṃ": "ချုပ်ငြိမ်းခြင်း သစ္စာ", "maggasaccaṃ": "မဂ် သစ္စာ",
}
PAJANATI = "ကွဲပြားစွာ သိ၏"        # (bhikkhu) pajānāti: ch7 (pi-1 pajānanā «ကွဲပြားစွာ သိခြင်း»); ch16 had «သိသည်»
CITTA16 = {  # the sixteen states of mind (cittānupassanā ch7 = cetopariyañāṇa ch16)
    "sarāgaṃ": "ရာဂ ရှိသော", "vītarāgaṃ": "ရာဂ ကင်းသော", "sadosaṃ": "ဒေါသ ရှိသော", "vītadosaṃ": "ဒေါသ ကင်းသော",
    "samohaṃ": "မောဟ ရှိသော", "vītamohaṃ": "မောဟ ကင်းသော", "saṃkhittaṃ": "တွန့်ဆုတ်နေသော",
    "vikkhittaṃ": "ပျံ့လွင့်နေသော", "mahaggataṃ": T["mahaggatā"], "amahaggataṃ": "မ" + T["mahaggatā"],
    "sauttaraṃ": T["sauttarā"], "anuttaraṃ": T["anuttarā"], "samāhitaṃ": "တည်ကြည်သော",
    "asamāhitaṃ": "မတည်ကြည်သော", "vimuttaṃ": "လွတ်မြောက်သော", "avimuttaṃ": "မလွတ်မြောက်သော",
}
SPEECH = {  # the four wrong speeches (ch17: 4 lists); pharusā vācā was one form already
    "musāvāda": "မုသား ပြောခြင်း", "pisuṇā vācā": "ကုန်းတိုက်သော စကား", "pharusā vācā": "ကြမ်းတမ်းသော စကား",
    "samphappalāpa": "အကျိုးမဲ့ ပြိန်ဖျင်းသော စကား",
}
VIHIMSA = "ညှဉ်းပန်းမှု"            # vihiṃsā (pi-1 termbase vihiṃsūparati; ch3, ch4, ch12, ch17)
SANKAPPA = {  # sammāsaṅkappa items (ch4 / ch11): «X-ဆိုင်ရာ ကြံစည်မှု»
    "nekkhammasaṅkappo": "ကာမမှ ထွက်မြောက်ခြင်းဆိုင်ရာ ကြံစည်မှု",
    "abyāpādasaṅkappo": "ဖျက်ဆီးလိုစိတ် မရှိခြင်းဆိုင်ရာ ကြံစည်မှု",
    "avihiṃsāsaṅkappo": f"{VIHIMSA} မရှိခြင်းဆိုင်ရာ ကြံစည်မှု",
}
VITIKKAMA = {  # kāyika / vācasika (pi-1 kāyika «ကိုယ်ပိုင်းဆိုင်ရာ»; ch17); ch12 had «ကိုယ်ဖြင့် / နှုတ်ဖြင့်»
    "kāyiko": "ကိုယ်ပိုင်းဆိုင်ရာ", "vācasiko": "နှုတ်ပိုင်းဆိုင်ရာ",
    "kāyikavācasiko": "ကိုယ်ပိုင်းဆိုင်ရာနှင့် နှုတ်ပိုင်းဆိုင်ရာ",
}
SUTTANTA = {  # the suttanta definitions of birth … despair (ch4 = ch6, one table)
    "tamhi tamhi sattanikāye": "ထိုထို သတ္တဝါ အမျိုးအစား၌", "tamhā tamhā sattanikāyā": "ထိုထို သတ္တဝါ အမျိုးအစားမှ",
    "abhinibbatti": "ထင်ရှားစွာ ပေါ်ထွက်ခြင်း",          # pi-1 abhinibbattā «ထင်ရှားစွာ ပေါ်ထွက်ပြီးသော»
    "pātubhāvo": "ထင်ရှား လာခြင်း",                     # ch18 pātubhavanti «ထင်ရှားလာကြသည်»
    "antoparisoko": "အတွင်း ပြင်းစွာ စိုးရိမ်ခြင်း",       # pari- as upāyāso «ပြင်းစွာ ပူပန်ခြင်း»
    "phuṭṭhassa": "ထိခိုက်ခံရသူ၏", "samannāgatassa": "ကြုံတွေ့နေရသူ၏",
    "byasanena vā": "ပျက်စီးခြင်းဖြင့်", "dukkhadhammena": "ဆင်းရဲဖွယ်ရာဖြင့်",
    # parideva: one Burmese item per Pāli word (ch4); ch6 had «စကား ပေါက်ကရ ပြောခြင်း» for two words
    "vācā": C3["VACA"], "palāpo": "ပေါက်ကရ ပြောခြင်း", "vippalāpo": "ကမောက်ကမ ပြောခြင်း", "lālappo": "မြည်တမ်းခြင်း",
    "lālappanā": "မြည်တမ်းနေခြင်း", "lālappitattaṃ": "မြည်တမ်းထားသော အဖြစ်",
}
BYASANA_HEAD = (f"{C} ".join(f"{v} {SUTTANTA['byasanena vā']} {SUTTANTA['phuṭṭhassa']}ဖြစ်စေ"
                             for v in ("ဆွေမျိုး", "စည်းစိမ်", "ကျန်းမာရေး", "သီလ", "အယူ"))
                + f"{C} တစ်ခုခုသော ပျက်စီးခြင်းနှင့် {SUTTANTA['samannāgatassa']}{C} တစ်ခုခုသော "
                  f"{SUTTANTA['dukkhadhammena']} {SUTTANTA['phuṭṭhassa']}")
SANGATI = {  # saṅgati … pātubhāvo (ch6: 5 uses each; ch4 had another assignment of the same words)
    "saṅgati": "စုဝေးခြင်း", "samāgamo": "ဆုံဆည်းခြင်း", "samodhānaṃ": "ပေါင်းစည်းခြင်း",
}
CETOVIMUTTI = "စိတ်လွတ်မြောက်မှု"   # -cetovimutti (ch13: 40 uses); ch3 had «စိတ် လွတ်မြောက်ခြင်း»
ADINNADANA = "မပေးသည်ကို ယူခြင်း"   # adinnādāna (ch4, ch11, ch17: 7 uses); ch14 had «မပေးသောအရာကို ယူခြင်း»
FEEL_SYN = {  # the mental feelings (pi-1 SYN; asāta items = ch5-7-11 / ch12-14); ch17 had «ချမ်းသာ / စိတ်၌ ဖြစ်သော»
    k: P1.SYN[k] for k in ("cetasikaṃ sātaṃ", "cetasikaṃ sukhaṃ", "cetosamphassajaṃ sātaṃ sukhaṃ vedayitaṃ",
                           "cetosamphassajā sātā sukhā vedanā", "cetasikaṃ neva sātaṃ nāsātaṃ",
                           "cetosamphassajaṃ adukkhamasukhaṃ vedayitaṃ", "cetosamphassajā adukkhamasukhā vedanā")}
FEEL_SYN.update({
    "cetasikaṃ asātaṃ": "စိတ်ပိုင်းဆိုင်ရာ နှစ်သက်ဖွယ် မကောင်းမှု", "cetasikaṃ dukkhaṃ": "စိတ်ပိုင်းဆိုင်ရာ နာကျင်မှု",
    "cetosamphassajaṃ asātaṃ dukkhaṃ vedayitaṃ": "စိတ်၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော နှစ်သက်ဖွယ် မကောင်း၍ နာကျင်သော ခံစားရခြင်း",
    "cetosamphassajā asātā dukkhā vedanā": "စိတ်၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော နှစ်သက်ဖွယ် မကောင်း၍ နာကျင်သော ခံစားမှု",
})
VIEW_NAMES = {   # the suttantika views of pi-1 (SUT), for the ch17 duka headings and lists
    "bhavadiṭṭhi": P1.SUT["bhavadiṭṭhi"], "vibhavadiṭṭhi": P1.SUT["vibhavadiṭṭhi"],
    "sassatadiṭṭhi": P1.SUT["sassatadiṭṭhi"], "ucchedadiṭṭhi": P1.SUT["ucchedadiṭṭhi"],
    "antavādiṭṭhi": P1.SUT["antavā diṭṭhi"], "anantavādiṭṭhi": P1.SUT["anantavā diṭṭhi"],
    "pubbantānudiṭṭhi": P1.SUT["pubbantānudiṭṭhi"], "aparantānudiṭṭhi": P1.SUT["aparantānudiṭṭhi"],
}
