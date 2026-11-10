"""English->Pali keyword map for pi-1 chapters 3-02-rupakandam and 3-03-rupakandam.

usage: python -I -X utf8 map_3-02_3-03.py [--joins]
Writes <ch>.mapped.md next to <ch>.keywords.md. Conventions: map-conventions.md.

How it works: every Pali segment is walked in text order and cut into "units" that mirror the
phrase tables of the builder (../build_3-02_3-03.py): the question frame, each classification term,
each list item, each definition piece, each closing line. A unit maps the English keywords it
produces to the Pali it renders. A keyword takes its value from the FIRST unit (Pali order) that
produces it; units with a different lemma are joined with " / " (map-conventions §4).
Identical Pali therefore always gets identical values. NDE = "(no direct equivalent)".
"""
import importlib.util
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
PIPE = HERE.parent
ROOT = HERE.parents[4]
PALI = ROOT / "AI_translation" / "pali" / "pi-1_split_chapters"
NDE = "(no direct equivalent)"
CHAPTERS = ["3-02-rupakandam", "3-03-rupakandam"]

sys.dont_write_bytecode = True
sys.path.insert(0, str(PIPE))
_spec = importlib.util.spec_from_file_location("build_3_02_3_03", PIPE / "build_3-02_3-03.py")
B = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(B)

PE = "…pe…"

# =====================================================================================
# lemma groups (only used to decide "same lemma -> first occurrence" vs "different -> join")
# =====================================================================================
LEMMA_PREFIX = {
    "cakkhusamphass": "cakkhusamphassa", "sotasamphass": "sotasamphassa", "ghānasamphass": "ghānasamphassa",
    "jivhāsamphass": "jivhāsamphassa", "kāyasamphass": "kāyasamphassa",
    "cakkhuviññāṇ": "cakkhuviññāṇa", "sotaviññāṇ": "sotaviññāṇa", "ghānaviññāṇ": "ghānaviññāṇa",
    "jivhāviññāṇ": "jivhāviññāṇa", "kāyaviññāṇ": "kāyaviññāṇa",
    "cakkhu": "cakkhu", "sot": "sota", "ghān": "ghāna", "jivh": "jivhā", "kāy": "kāya",
    "rūp": "rūpa", "sadd": "sadda", "gandh": "gandha", "ras": "rasa", "phoṭṭhabb": "phoṭṭhabba",
    "upādā": "upādā", "upādiṇṇ": "upādiṇṇa", "anidassan": "anidassana", "sanidassan": "sanidassana",
    "sappaṭigh": "paṭigha", "appaṭigh": "paṭigha", "itth": "itthi", "puris": "purisa", "jīvit": "jīvita",
    "citta": "citta", "mano": "mano", "manasā": "mano", "vedanā": "vedanā", "saññā": "saññā",
    "cetanā": "cetanā", "ārammaṇ": "ārammaṇa", "vāc": "vācā", "vacī": "vācā", "kammassa": "kamma",
    "dasa": "dasa", "ekādasa": "ekādasa", "y": "ya", "mahābhūt": "mahābhūta", "bhūt": "mahābhūta",
    "dhātu": "dhātu", "indriy": "indriya", "satt": "satta", "upacay": "upacaya", "jarā": "jarā",
    "jaratā": "jarā", "aniccatā": "aniccatā", "lahutā": "lahutā", "mudutā": "mudutā",
    "kammaññatā": "kammaññatā", "santati": "santati", "viññatti": "viññatti", "āpo": "āpo",
    "viññāp": "viññāpeti", "ākās": "ākāsa", "kakkhaḷaṃ": "kakkhaḷa", "kakkhaḷabhāv": "kakkhaḷa",
}
_LP = sorted(LEMMA_PREFIX, key=len, reverse=True)


def lemma(v):
    if " " in v:  # a multiword fragment: the first occurrence of the formula wins
        return "PHRASE"
    v = v.lower()
    for p in _LP:
        if v.startswith(p):
            return LEMMA_PREFIX[p]
    return v


# =====================================================================================
# unit helpers
# =====================================================================================
def cap(d, token):
    """Copy a capital: a value cut from the start of a capitalised token keeps the capital (§1.1)."""
    if not token or not token[0].isupper():
        return d
    out = {}
    for k, v in d.items():
        if v != NDE and v[:2].lower() == token[:2].lower() and v[0].islower():
            v = v[0].upper() + v[1:]
        out[k] = v
    return out


FRAME = {"material": "rūpaṃ", "form": "rūpaṃ", "material form": "rūpaṃ"}

SENSES = {"cakkhu": "eye", "sota": "ear", "ghāna": "nose", "jivhā": "tongue", "kāya": "body"}
OBJS = {"rūpa": "visible-form", "sadda": "sound", "gandha": "smell", "rasa": "taste", "phoṭṭhabba": "touch"}
BASE_WORD = {"cakkhu": "cakkhāyatanaṃ", "sota": "sotāyatanaṃ", "ghāna": "ghānāyatanaṃ", "jivhā": "jivhāyatanaṃ",
             "kāya": "kāyāyatanaṃ", "rūpa": "rūpāyatanaṃ", "sadda": "saddāyatanaṃ", "gandha": "gandhāyatanaṃ",
             "rasa": "rasāyatanaṃ", "phoṭṭhabba": "phoṭṭhabbāyatanaṃ"}

ITEM = {}
for _stem, _eng in {**SENSES, **OBJS}.items():
    _w = BASE_WORD[_stem]
    ITEM[_w] = {_eng: _stem, f"{_eng} base": _w}
    _d = _stem + "dhātu"
    ITEM[_d] = {_eng: _stem, f"{_eng} element": _d, "element": "dhātu"}
for _w, _stem in {"cakkhundriyaṃ": "cakkhu", "sotindriyaṃ": "sota", "ghānindriyaṃ": "ghāna",
                  "jivhindriyaṃ": "jivhā", "kāyindriyaṃ": "kāya"}.items():
    ITEM[_w] = {SENSES[_stem]: _stem, "faculty": "indriyaṃ"}
ITEM["itthindriyaṃ"] = {"faculty": "indriyaṃ", "femininity": "itthi", "faculty of femininity": "itthindriyaṃ"}
ITEM["purisindriyaṃ"] = {"faculty": "indriyaṃ", "masculinity": "purisa", "faculty of masculinity": "purisindriyaṃ"}
ITEM["jīvitindriyaṃ"] = {"faculty": "indriyaṃ", "life": "jīvita", "faculty of life": "jīvitindriyaṃ"}
ITEM["kāyaviññatti"] = {"bodily": "kāya", "intimation": "viññatti", "bodily intimation": "kāyaviññatti"}
ITEM["vacīviññatti"] = {"verbal": "vacī", "intimation": "viññatti", "verbal intimation": "vacīviññatti"}
for _w, (_stem, _eng) in {"ākāsadhātu": ("ākāsa", "space"), "pathavīdhātu": ("pathavī", "earth"),
                          "āpodhātu": ("āpo", "water"), "tejodhātu": ("tejo", "fire"),
                          "vāyodhātu": ("vāyo", "air")}.items():
    ITEM[_w] = {_eng: _stem, f"{_eng} element": _w, "element": "dhātu"}
RUPASSA = {"lahutā": "lightness", "mudutā": "pliancy", "kammaññatā": "workability", "upacayo": "growth",
           "santati": "continuity", "jaratā": "ageing", "aniccatā": "impermanence"}
ITEM["kabaḷīkāro āhāro"] = {"edible": "kabaḷīkāro", "food": "āhāro", "edible food": "kabaḷīkāro āhāro"}


def item_unit(tok):
    """tok: the item as it stands in the text, possibly with 'na ' / 'rūpassa na ' (negated term)."""
    t = tok[0].lower() + tok[1:]
    if t.startswith("rūpassa "):
        w = t.split()[-1]
        eng = RUPASSA[w]
        return {eng: w, f"{eng} of material": t, **{k: "rūpassa" for k in FRAME}}
    if t.startswith("na "):
        t = t[3:]
    return cap(ITEM[t], tok if not tok.lower().startswith("na ") else t)


# classification terms (predicates)
TERM = {
    "upādā": {"derived": "upādā"},
    "upādiṇṇaṃ": {"produced": "upādiṇṇaṃ", "produced by past": "upādiṇṇaṃ", "past action": "upādiṇṇaṃ"},
    "upādiṇṇupādāniyaṃ": {"produced": "upādiṇṇa", "produced by past": "upādiṇṇa", "past action": "upādiṇṇa",
                          "clinging": "upādāniyaṃ", "subject to clinging": "upādāniyaṃ",
                          "action and subject": "upādiṇṇupādāniyaṃ"},
    "anupādiṇṇupādāniyaṃ": {"produced": "upādiṇṇa", "produced by past": "upādiṇṇa", "past action": "upādiṇṇa",
                            "clinging": "upādāniyaṃ", "subject to clinging": "upādāniyaṃ",
                            "action but subject": "anupādiṇṇupādāniyaṃ"},
    "sanidassanaṃ": {"visible": "sanidassanaṃ"},
    "anidassanaṃ": {"invisible": "anidassanaṃ"},
    "sappaṭighaṃ": {"makes": "sappaṭighaṃ", "makes impact": "sappaṭighaṃ"},
    "appaṭighaṃ": {"makes": "appaṭighaṃ", "makes no impact": "appaṭighaṃ"},
    "indriyaṃ": {"faculty": "indriyaṃ"},
    "mahābhūtaṃ": {"great element": "mahābhūtaṃ", "element": "bhūtaṃ"},
    "viññatti": {"intimation": "viññatti"},
    "cittasamuṭṭhānaṃ": {"arises": "samuṭṭhānaṃ", "arise": "samuṭṭhānaṃ", "mind": "citta"},
    "cittasahabhu": {"exists": "cittasahabhu", "exist": "cittasahabhu", "together": "cittasahabhu",
                     "mind": "citta"},
    "cittānuparivatti": {"accompanies": "anuparivatti", "accompany": "anuparivatti", "mind": "citta"},
    "ajjhattikaṃ": {"internal": "ajjhattikaṃ"},
    "bāhiraṃ": {"external": "bāhiraṃ"},
    "oḷārikaṃ": {"gross": "oḷārikaṃ"},
    "sukhumaṃ": {"subtle": "sukhumaṃ"},
    "dūre": {},
    "santike": {},
    "anidassanaṃ appaṭighaṃ dhammāyatanapariyāpannaṃ": {
        "invisible": "anidassanaṃ", "makes": "appaṭighaṃ", "makes no impact": "appaṭighaṃ",
        "mental-object": "dhamma", "mental-object base": "dhammāyatana"},
}
GEN = {}
for _s, _eng in SENSES.items():
    GEN[f"{_s}samphassassa"] = {f"{_eng}-contact": f"{_s}samphassassa"}
    GEN[f"{_s}viññāṇassa"] = {f"{_eng}-consciousness": f"{_s}viññāṇassa"}
for _s in ("cakkhu", "kāya"):
    _b = f"{_s}samphassajāya"
    GEN[f"{_b} vedanāya"] = {"feeling": "vedanāya", "born": _b, "feeling born": f"{_b} vedanāya",
                             f"{SENSES[_s]}-contact": _b, f"born of {SENSES[_s]}-contact": _b}
GEN["saññāya"] = {"perception": "saññāya"}
GEN["cetanāya"] = {"intention": "cetanāya"}
REL = {"vatthu": {}, "ārammaṇaṃ": {"object": "ārammaṇaṃ"}}


def term_units(tok):
    """Units for one token of a question / closing predicate (builder vocabulary)."""
    if tok in B.COMPOSITE:
        g, neg, r = B.COMPOSITE[tok]
        return [GEN[g], REL[r]]
    if tok in GEN:
        return [GEN[tok]]
    base = tok
    for p in ("na ", "no "):
        if base.startswith(p):
            base = base[len(p):]
    if base.startswith("rūpassa ") or base in ITEM:
        return [item_unit(tok)]
    if base == "anupādiṇṇaṃ":
        return [TERM["upādiṇṇaṃ"]]
    return [TERM[base]]


def strip_neg(tok):
    for p in ("na ", "no "):
        if tok.startswith(p):
            tok = tok[len(p):]
    return "upādiṇṇaṃ" if tok == "anupādiṇṇaṃ" else tok


COMBO = {"bāhiraṃ": "external and makes", "upādā": "derived and makes", "upādiṇṇaṃ": "action and makes"}
FORM_THAT = {"sappaṭighaṃ": "form that makes", "appaṭighaṃ": "form that makes",
             "cittasamuṭṭhānaṃ": "form that arises", "cittasahabhu": "form that exists",
             "cittānuparivatti": "form that accompanies"}


def predicate_units(q):
    """q: Pali predicate after 'Katamaṃ taṃ rūpaṃ' / 'idaṃ taṃ rūpaṃ'."""
    pieces = re.sub(r"\s*…pe…\s*", PE, q.strip()).split(PE)
    toks = [t for p in pieces for t in B.tokenize(p, B.VOCAB)]
    units = []
    if toks[0] in FORM_THAT:
        units.append({FORM_THAT[toks[0]]: f"rūpaṃ {toks[0]}"})
    for t in toks:
        units += term_units(t)
    if len(toks) == 2 and toks[1] in ("sappaṭighaṃ", "appaṭighaṃ") and strip_neg(toks[0]) in COMBO:
        units.append({COMBO[strip_neg(toks[0])]: f"{strip_neg(toks[0])} {toks[1]}"})
    return units


# =====================================================================================
# answer lists
# =====================================================================================
CLAUSE = "yaṃ vā panaññampi atthi rūpaṃ"
QUAL = {
    "kammassa katattā": {"due to past": "kammassa katattā", "past action": "kammassa"},
    "na kammassa katattā": {"due to past": "kammassa katattā", "past action": "kammassa"},
    "cittajaṃ cittahetukaṃ cittasamuṭṭhānaṃ": {
        "born": "cittajaṃ", "mind": "citta", "caused": "hetukaṃ", "arising": "samuṭṭhānaṃ",
        "arising from mind": "cittasamuṭṭhānaṃ"},
    "na cittajaṃ na cittahetukaṃ na cittasamuṭṭhānaṃ": {
        "born": "cittajaṃ", "mind": "citta", "caused": "hetukaṃ", "arising": "samuṭṭhānaṃ",
        "arising from mind": "cittasamuṭṭhānaṃ"},
}
LVOCAB = set(ITEM) | {"rūpassa " + w for w in RUPASSA} | {CLAUSE} | set(QUAL)


def list_units(a):
    words = re.sub(r"\s*…pe…\s*", " ", a).replace(",", " ").split()
    units, i = [], 0
    while i < len(words):
        for n in range(min(6, len(words) - i), 0, -1):
            cand = " ".join(words[i:i + n])
            low = cand[0].lower() + cand[1:]
            if low in LVOCAB:
                if low == CLAUSE:
                    units.append({"whatever": "yaṃ", **FRAME})
                elif low in QUAL:
                    units.append(cap(QUAL[low], cand))
                else:
                    units.append(item_unit(cand))
                i += n
                break
        else:
            raise ValueError(f"unknown list item at {words[i:]!r}")
    return units


# =====================================================================================
# definitions
# =====================================================================================
ORGAN = {"cakkhu": "cakkhu", "cakkhuṃ": "cakkhu", "sotaṃ": "sota", "ghānaṃ": "ghāna", "jivhā": "jivhā",
         "kāyo": "kāya"}
VERBS = {"cakkhu": ("seen", "sees", "see"), "sota": ("heard", "hears", "hear"),
         "ghāna": ("smelled", "smells", "smell"), "jivhā": ("tasted", "tastes", "taste"),
         "kāya": ("touched", "touches", "touch")}
OBJ_ENG = {"rūpa": "visible form", "sadda": "sound", "gandha": "smell", "rasa": "taste", "phoṭṭhabba": "touch"}
STRIKE = {"struck": "paṭihaññi", "strikes": "paṭihaññati", "strike": "paṭihaññissati"}
ARISE = {"arisen": "uppajji", "arises": "uppajjati", "arise": "uppajjissati"}
NAMES = {"door": "dvārā", "ocean": "samuddo", "radiance": "paṇḍaraṃ", "field": "khettaṃ", "guide": "nettaṃ",
         "leader": "nayanaṃ", "shore": "tīraṃ", "empty": "suñño", "village": "gāmo", "empty village": "suñño gāmo"}
ELEMENTS = {"great elements": "mahābhūtānaṃ", "elements": "bhūtānaṃ"}


def obj_noun(stem, word):
    """The sense object as a noun in the text (rūpaṃ, saddo, gandhamhi ...)."""
    d = {OBJ_ENG[stem]: word}
    if stem == "rūpa":
        d["visible"] = word
    return d


def quals(q1, q2, verb_form):
    """'visible/invisible and makes|making impact' pair."""
    pos = "visible" if q1.startswith("sanidassan") else "invisible"
    mk = "makes" if verb_form else "making"
    d = {pos: q1, f"{mk} impact": q2, f"{pos} and {mk}": f"{q1} {q2}"}
    if verb_form:
        d["makes"] = q2
    return d


def obj_stem(word):
    for s in ("rūpa", "sadda", "gandha", "rasa", "phoṭṭhabba"):
        if word.startswith(s[:-1]):
            return s
    raise ValueError(word)


def contact_chain(rest, organ_stem):
    """Units of the '...nissāya ... samphasso uppajji ...' (d) variant, in text order."""
    o = SENSES[organ_stem]
    u = []
    contact = re.search(r"(\S+samphasso) uppajji", rest).group(1)
    born = re.search(r"(\S+samphassajā) vedanā", rest).group(1)
    cons = re.search(r"(\S+viññāṇaṃ) uppajji", rest).group(1)
    u.append({f"{o}-contact": contact})
    u.append(ARISE)
    d = {"feeling": "vedanā", "born": born, "feeling born": f"{born} vedanā", f"{o}-contact": born}
    if organ_stem == "kāya":
        d["born of body-contact"] = born
    u.append(d)
    u.append({"perception": "saññā"})
    u.append({"intention": "cetanā"})
    u.append({f"{o}-consciousness": cons})
    u.append({"object": "ārammaṇo"})
    return u


def organ_def(a):
    m = re.match(r"^(Yaṃ|Yā|Yo) (\S+)( \[[^\]]*\])? catunnaṃ mahābhūtānaṃ upādāya pasādo", a)
    word = m.group(2)
    stem = ORGAN[word]
    o = SENSES[stem]
    u = [{o: word}]
    if m.group(3):
        u.append({"variant": NDE})
    u.append(ELEMENTS)
    u.append({"derived": "upādāya", "sensitivity": "pasādo", "sensitivity derived": "upādāya pasādo"})
    if "pasādo…pe…" in a:
        u.append(NAMES)
        return u
    u.append({"person": "attabhāva"})
    u.append({"invisible": "anidassano", "making impact": "sappaṭigho", "invisible and making": "anidassano sappaṭigho"})
    rest, names = re.match(r"^.*?sappaṭigho, (.*), (\S+ pe(?:taṃ|sā|so) .*)$", a).groups()
    t = rest.split()
    if " nissāya " in rest:  # d
        org = re.search(r"yaṃ (\S+) nissāya", rest).group(1)
        u.append({o: org, "depending": "nissāya", f"{o} depending": f"{org} nissāya"})
        ob = re.search(r"nissāya (\S+) ārabbha", rest).group(1)
        u.append(obj_noun(obj_stem(ob), ob))
        u += contact_chain(rest, stem)
    else:  # a / b / c: rel organ q q obj q q verbs...
        u.append({o: t[1]})
        u.append(quals(t[2], t[3], False))
        ob = t[4]
        u.append(obj_noun(obj_stem(ob), ob))
        if "sappaṭigh" in t[5] and t[5].startswith("anidassana"):  # phoṭṭhabbaṃ anidassanasappaṭighaṃ
            u.append({"invisible": "anidassana", "invisible and makes": t[5], "makes": "sappaṭighaṃ",
                      "makes impact": "sappaṭighaṃ"})
            v = t[6:]
        else:
            u.append(quals(t[5], t[6], True))
            v = t[7:]
        if v[0].startswith("paṭihaññ"):
            u.append(STRIKE)
            if t[0] in ("yamhi", "yāya") and not t[4].endswith("mhi"):  # b: '... makes impact has struck'
                u.append({"impact has struck": f"{t[6]} {v[0]}"})
        else:
            past, pres, base = VERBS[stem]
            u.append({past: v[0], pres: v[2], base: v[4]})
    # names: cakkhuṃ petaṃ cakkhāyatanaṃ petaṃ cakkhudhātu pesā cakkhundriyaṃ petaṃ loko peso ...
    nw = names.split()
    u.append({o: nw[0]})
    u.append(ITEM[BASE_WORD[stem]])
    u.append(ITEM[stem + "dhātu"])
    u.append({"faculty": "indriyaṃ"})
    u.append(NAMES)
    return u


COLOURS = {
    "colour": "vaṇṇa", "appearance": "nibhā", "colour and appearance": "vaṇṇanibhā",
    "appearance derived": "upādāya vaṇṇanibhā",
}
COLOUR_LIST = {
    "blue": "nīlaṃ", "yellow": "pītakaṃ", "red": "lohitakaṃ", "white": "odātaṃ", "black": "kāḷakaṃ",
    "crimson": "mañjiṭṭhakaṃ", "green": "hari", "green-coloured": "harivaṇṇaṃ",
    "colour of mango": "ambaṅkuravaṇṇaṃ", "mango": "amba", "shoots": "aṅkura",
    "round": "vaṭṭaṃ", "circular": "parimaṇḍalaṃ", "square": "caturaṃsaṃ", "six-sided": "chaḷaṃsaṃ",
    "eight-sided": "aṭṭhaṃsaṃ", "sixteen-sided": "soḷasaṃsaṃ", "shadow": "chāyā", "sunshine": "ātapo",
    "light": "āloko", "darkness": "andhakāro", "cloud": "abbhā", "mist": "mahikā", "smoke": "dhūmo",
    "dust": "rajo", "moon": "canda", "disc": "maṇḍalassa", "sun": "sūriya", "stars": "tārakarūpānaṃ",
    "mirror": "ādāsa", "gems": "maṇi", "conch": "saṅkha", "shells": "saṅkha", "pearls": "muttā",
    "beryl": "veḷuriyassa", "appearance of gems": "maṇisaṅkhamuttāveḷuriyassa vaṇṇanibhā",
    "gold": "jātarūpa", "silver": "rajatassa", "appearance of gold": "jātarūparajatassa vaṇṇanibhā",
}
SOUND_LIST = {
    "drums": "bheri", "sound of drums": "bherisaddo", "tabors": "mudiṅga", "sound of tabors": "mudiṅgasaddo",
    "conches": "saṅkha", "sound of conches": "saṅkhasaddo", "tom-toms": "paṇava",
    "sound of tom-toms": "paṇavasaddo", "singing": "gīta", "sound of singing": "gītasaddo",
    "instruments": "vādita", "sound of instruments": "vāditasaddo", "cymbals": "samma",
    "sound of cymbals": "sammasaddo", "hand-clapping": "pāṇi", "sound of hand-clapping": "pāṇisaddo",
    "beings": "sattānaṃ", "noise": "nigghosasaddo", "things": "dhātūnaṃ", "knocking": "sannighāta",
    "together": "sannighāta", "sound of things": "dhātūnaṃ sannighātasaddo", "wind": "vāta",
    "sound of wind": "vātasaddo", "water": "udaka", "sound of water": "udakasaddo", "humans": "manussa",
    "sound of humans": "manussasaddo", "non-human": "amanussa", "sound of non-human": "amanussasaddo",
}
SOUND_LIST_2 = {"beings": "amanussa"}  # 'the sound of non-human beings' (second source of 'beings')
SMELL_LIST = {
    "roots": "mūla", "smell of roots": "mūlagandho", "heartwood": "sāra", "smell of heartwood": "sāragandho",
    "bark": "taca", "smell of bark": "tacagandho", "leaves": "patta", "smell of leaves": "pattagandho",
    "flowers": "puppha", "smell of flowers": "pupphagandho", "fruits": "phala", "smell of fruits": "phalagandho",
    "raw": "āmaka", "flesh": "āmaka", "smell of raw": "āmakagandho", "rot": "vissa", "smell of rot": "vissagandho",
    "pleasant": "sugandho", "pleasant smell": "sugandho", "unpleasant": "duggandho",
    "unpleasant smell": "duggandho",
}
TASTE_LIST = {
    "roots": "mūla", "taste of roots": "mūlaraso", "stems": "khandha", "taste of stems": "khandharaso",
    "bark": "taca", "taste of bark": "tacaraso", "leaves": "patta", "taste of leaves": "pattaraso",
    "flowers": "puppha", "taste of flowers": "puppharaso", "fruits": "phala", "taste of fruits": "phalaraso",
    "sour": "ambilaṃ", "sweet": "madhuraṃ", "bitter": "tittakaṃ", "pungent": "kaṭukaṃ", "salty": "loṇikaṃ",
    "alkaline": "khārikaṃ", "tart": "lambilaṃ", "astringent": "kasāvo", "tasty": "sādu",
}
TOUCH_HEAD = [
    {"earth": "Pathavī", "earth element": "Pathavīdhātu", "element": "dhātu"},
    {"fire": "tejo", "fire element": "tejodhātu", "element": "dhātu"},
    {"air": "vāyo", "air element": "vāyodhātu", "element": "dhātu"},
    {"hard": "kakkhaḷaṃ", "soft": "mudukaṃ", "smooth": "saṇhaṃ", "rough": "pharusaṃ"},
    {"pleasant": "sukha", "touch": "samphassaṃ"},
    {"painful": "dukkha", "touch": "samphassaṃ"},
    {"heavy": "garukaṃ", "light": "lahukaṃ"},
]


def object_def(a, stem):
    o = OBJ_ENG[stem]
    u = []
    if stem == "phoṭṭhabba":
        if "…pe…" in a.split(",")[0] and "ārabbha" not in a:  # 'Pathavīdhātu…pe… phoṭṭhabbadhātu pesā'
            return [TOUCH_HEAD[0], ITEM["phoṭṭhabbadhātu"]]
        u += TOUCH_HEAD
        rest = a.split("lahukaṃ, ", 1)[1]
    else:
        word = a.split()[1]  # rūpaṃ / saddo / gandho / raso
        u.append(obj_noun(stem, word))
        u.append(ELEMENTS)
        u.append({"derived": "upādāya"})
        if stem == "rūpa":
            u.append(COLOURS)
            if "…pe…" in a.split(",")[0]:  # abbreviated: 'vaṇṇanibhā…pe… rūpadhātu pesā'
                u.append(ITEM["rūpadhātu"])
                return u
            u.append({"visible": "sanidassanaṃ", "making impact": "sappaṭighaṃ",
                      "visible and making": "sanidassanaṃ sappaṭighaṃ"})
            u.append(COLOUR_LIST)
        else:
            u.append({"invisible": "anidassano", "making impact": "sappaṭigho",
                      "invisible and making": "anidassano sappaṭigho"})
            u.append({"sadda": SOUND_LIST, "gandha": SMELL_LIST, "rasa": TASTE_LIST}[stem])
            if stem == "sadda":
                u.append(SOUND_LIST_2)
        if "[" in a:
            u.append({"variant": NDE})
        u.append({"whatever": "yaṃ" if stem == "rūpa" else "yo"})
        rest = a.split("sappaṭighaṃ, " if stem == "rūpa" else "sappaṭigho, ")[-1]
    rest, names = re.match(r"^(.*?),? (\S+ pe(?:taṃ|sā|so) .*)$", rest).groups()
    t = rest.split()
    organ_stem = {"rūpa": "cakkhu", "sadda": "sota", "gandha": "ghāna", "rasa": "jivhā", "phoṭṭhabba": "kāya"}[stem]
    org_eng = SENSES[organ_stem]
    if "ārabbha" in rest:  # d: yaṃ rūpaṃ ārabbha cakkhuṃ nissāya ...
        ob = t[1]
        u.append(obj_noun(stem, ob))
        org = re.search(r"ārabbha (\S+) nissāya", rest).group(1)
        u.append({org_eng: org, "depending": "nissāya"})
        u += contact_chain(rest, organ_stem)
    else:  # a / b / c: rel obj q q organ q q verbs
        u.append(obj_noun(stem, t[1]))
        u.append(quals(t[2], t[3], False))
        u.append({org_eng: t[4]})
        u.append(quals(t[5], t[6], False))
        v = t[7:]
        if v[0].startswith("paṭihaññ"):
            u.append(STRIKE)
        else:
            past, pres, base = VERBS[organ_stem]
            u.append({past: v[0], pres: v[2], base: v[4]})
    nw = names.split()
    u.append(obj_noun(stem, nw[0]))
    u.append(ITEM[BASE_WORD[stem]])
    u.append(ITEM[stem + "dhātu"])
    return u


DEFS = [
    ("Yaṃ itthiyā", [
        {"whatever": "Yaṃ", "woman": "itthiyā"},
        {"feminine": "itthi", "feature": "liṅgaṃ"}, {"sign": "nimittaṃ"}, {"conduct": "kuttaṃ"},
        {"manner": "ākappo"}, {"femininity": "itthattaṃ"}, {"woman": "itthibhāvo"}]),
    ("Yaṃ purisassa", [
        {"whatever": "Yaṃ", "man": "purisassa"},
        {"masculine": "purisa", "feature": "liṅgaṃ"}, {"sign": "nimittaṃ"}, {"conduct": "kuttaṃ"},
        {"manner": "ākappo"}, {"masculinity": "purisattaṃ"}, {"man": "purisabhāvo"}]),
    ("Yo tesaṃ rūpīnaṃ dhammānaṃ", [
        {"whatever": "Yo", "material states": "rūpīnaṃ dhammānaṃ", "material": "rūpīnaṃ"},
        {"lifespan": "āyu", "persistence": "ṭhiti", "carrying": "yapanā", "keeping": "yāpanā", "going": "yāpanā",
         "moving": "iriyanā", "continuing": "vattanā", "protection": "pālanā", "life": "jīvitaṃ"},
        ITEM["jīvitindriyaṃ"]]),
    ("Yo ākāso", [
        {"whatever": "Yo", "space": "ākāso"}, {"counts": "gataṃ"}, {"void": "aghaṃ"}, {"opening": "vivaro"},
        {"untouched": "asamphuṭṭhaṃ", "great elements": "mahābhūtehi", "elements": "bhūtehi"}]),
    ("Yaṃ āpo", [
        {"whatever": "Yaṃ", "water": "āpo"}, {"counts": "gataṃ"}, {"moisture": "sineho"},
        {"binding": "bandhanattaṃ", "binding of material": "bandhanattaṃ rūpassa"}]),
    ("Yā rūpassa lahutā", [
        {"whatever": "Yā"}, {"lightness": "lahutā", "lightness of material": "rūpassa lahutā"},
        {"quickness": "lahupariṇāmatā"},
        {"freedom": "adandhanatā / avitthanatā", "slowness": "dandhanatā", "sluggishness": "vitthanatā"}]),
    ("Yā rūpassa mudutā", [
        {"whatever": "Yā"}, {"pliancy": "mudutā", "pliancy of material": "rūpassa mudutā"},
        {"softness": "maddavatā"},
        {"freedom": "akakkhaḷatā / akathinatā", "hardness": "kakkhaḷatā", "rigidity": "kathinatā"}]),
    ("Yā rūpassa kammaññatā", [
        {"whatever": "Yā"}, {"workability": "kammaññatā", "workability of material": "rūpassa kammaññatā"},
        {"workable": "kammaññattaṃ"}, {"condition": "bhāvo"}]),
    ("Yo āyatanānaṃ ācayo", [
        {"whatever": "Yo", "sense": "āyatanānaṃ", "bases": "āyatanānaṃ", "sense bases": "āyatanānaṃ"},
        {"accumulation": "ācayo"}, {"growth of material": "rūpassa upacayo"}]),
    ("Yo rūpassa upacayo", [
        {"whatever": "Yo", "growth of material": "rūpassa upacayo"},
        {"continuity": "santati", "continuity of material": "rūpassa santati"}]),
    ("Yā rūpassa jarā", [
        {"whatever": "Yā", "ageing": "jarā"}, {"growing": "jīraṇatā", "old": "jīraṇatā"},
        {"broken": "khaṇḍiccaṃ", "teeth": "khaṇḍiccaṃ"}, {"grey": "pāliccaṃ", "hair": "pāliccaṃ"},
        {"wrinkled": "valittacatā", "skin": "valittacatā"}, {"life": "āyuno", "dwindling": "saṃhāni"},
        {"faculties": "indriyānaṃ", "over-ripening": "paripāko"}]),
    ("Yo rūpassa khayo", [
        {"whatever": "Yo", "destruction": "khayo"}, {"passing": "vayo", "away": "vayo"},
        {"breaking": "bhedo"}, {"falling": "paribhedo", "apart": "paribhedo"},
        {"impermanence": "aniccatā"}, {"disappearance": "antaradhānaṃ"}]),
    ("Odano", [
        {"boiled": "Odano", "rice": "Odano", "porridge": "kummāso", "barley": "sattu", "meal": "sattu",
         "fish": "maccho", "meat": "maṃsaṃ", "milk": "khīraṃ", "curd": "dadhi", "ghee": "sappi",
         "butter": "navanītaṃ", "honey": "madhu", "molasses": "phāṇitaṃ"},
        {"whatever": "yaṃ", **FRAME}, {"whatever": "yamhi"}, {"beings": "sattānaṃ"},
        {"mouth": "mukha", "eat": "āsiyaṃ"}, {"teeth": "danta", "chew": "vikhādanaṃ"},
        {"throat": "gala", "swallow": "ajjhoharaṇīyaṃ"}, {"belly": "kucchi", "fills": "vitthambhanaṃ"},
        {"nutritive": "ojāya", "essence": "ojāya"}, {"beings": "sattā"}, {"keep": "yāpenti", "alive": "yāpenti"}]),
    ("Yaṃ kakkhaḷaṃ", [
        {"whatever": "Yaṃ", "hard": "kakkhaḷaṃ"}, {"harsh": "khara", "counts": "gataṃ"}, {"variant": NDE},
        {"hardness": "kakkhaḷattaṃ"}, {"hard": "kakkhaḷabhāvo"}]),
    ("Yaṃ tejo", [
        {"whatever": "Yaṃ", "fire": "tejo"}, {"counts": "gataṃ"}, {"warmth": "usmā"}, {"heat": "usumaṃ"}]),
    ("Yaṃ vāyo", [
        {"whatever": "Yaṃ", "air": "vāyo"}, {"counts": "gataṃ"},
        {"stiffened": "thambhitattaṃ", "material": "rūpassa", "form": "rūpassa", "material form": "rūpassa"}]),
]
OWN_OTHERS = [{"others": "bahiddhā"}, {"produced": "upādiṇṇaṃ", "produced by past": "upādiṇṇaṃ",
                                       "past action": "upādiṇṇaṃ"}]
MINDS = [{"wholesome": "kusala", "wholesome mind": "kusalacittassa", "mind": "cittassa"},
         {"unwholesome": "akusala", "unwholesome mind": "akusalacittassa", "mind": "cittassa"},
         {"indeterminate": "abyākata", "mind": "cittassa"}]
INTIM = [{"intimation": "viññatti"}, {"known": "viññāpanā"}, {"having": NDE, "known": "viññāpitattaṃ"}]


def short_def(a):
    if a.startswith("Yā kusalacittassa"):
        u = [{"whatever": "Yā"}] + MINDS
        if "abhikkamantassa" in a:
            u += [{"goes": "abhikkamantassa / paṭikkamantassa", "forward": "abhikkamantassa"},
                  {"looks": "ālokentassa / vilokentassa", "ahead": "ālokentassa"},
                  {"bends": "samiñjentassa"}, {"stretches": "pasārentassa"},
                  {"body": "kāyassa", "stiffening": "thambhanā"},
                  {"firmly": "santhambhitattaṃ", "stiffened": "santhambhitattaṃ"}]
        else:
            voice = "dhoso" if " dhoso " in a else "ghoso"
            u += [{"speech": "vācā"}, {"utterance": "girā"}, {"speaking": "byappatho"},
                  {"uttering": "udīraṇaṃ"}, {"voice": voice}, {"voicing": "ghosakammaṃ"},
                  {"speech": "vācā"}, {"speech": "vacī", "breaking": "bhedo"}, {"speech": "vācā"},
                  {"whatever": "Yā"}, {"speech": "vācāya"}]
        return u + INTIM
    for key, units in DEFS:
        if a.startswith(key):
            u = list(units)
            if key == "Yaṃ itthiyā" and "[" in a:
                u.append({"variant": NDE})
            if "ajjhattaṃ vā bahiddhā vā" in a:
                u += OWN_OTHERS
            return u
    return None


ORG_RE = re.compile(r"^(Yaṃ cakkhu|Yaṃ sotaṃ|Yaṃ ghānaṃ|Yā jivhā|Yo kāyo)( \[[^\]]*\])? catunnaṃ mahābhūtānaṃ "
                    r"upādāya pasādo")
OBJ_RE = re.compile(r"^(Yaṃ rūpaṃ|Yo saddo|Yo gandho|Yo raso) catunnaṃ mahābhūtānaṃ upādāya")
OBJ_KEY = {"Yaṃ rūpaṃ": "rūpa", "Yo saddo": "sadda", "Yo gandho": "gandha", "Yo raso": "rasa"}


def answer_units(a):
    u = short_def(a)
    if u is not None:
        return u
    if ORG_RE.match(a):
        return organ_def(a)
    m = OBJ_RE.match(a)
    if m:
        return object_def(a, OBJ_KEY[m.group(1)])
    if a.startswith("Pathavīdhātu"):
        return object_def(a, "phoṭṭhabba")
    return list_units(a)


# =====================================================================================
# lines
# =====================================================================================
NUMW = {"du": None, "ti": None, "catub": None, "pañca": None, "cha": None, "satta": None, "aṭṭha": None,
        "nava": None, "dasa": "ten", "ekādasa": "eleven"}
LINE_UNITS = {
    "##### Dukaniddeso": [{"pairs": "Duka", "exposition": "niddeso"}],
    "Dukaniddeso.": [{"pairs": "Duka", "exposition": "niddeso"}],
    "###### Upādābhājanīyaṃ": [{"derived": "Upādā", "derived material": "Upādā", "derived material form": "Upādā",
                                "material": NDE, "form": NDE, "material form": NDE, "analysis": "bhājanīyaṃ"}],
    "Upādābhājanīyaṃ.": [{"derived": "Upādā", "derived material": "Upādā", "derived material form": "Upādā",
                          "analysis": "bhājanīyaṃ"}],
    "##### Tikaniddeso": [{"exposition": "niddeso"}],
    "Tikaniddeso.": [{"exposition": "niddeso"}],
    "##### Dasakaṃ": [{"ten": "Dasakaṃ", "set of ten": "Dasakaṃ"}],
    "Dasakaṃ.": [{"ten": "Dasakaṃ", "set of ten": "Dasakaṃ"}],
    "##### Ekādasakaṃ": [{"eleven": "Ekādasakaṃ", "set of eleven": "Ekādasakaṃ"}],
    "Ekādasakaṃ.": [{"eleven": "Ekādasakaṃ", "set of eleven": "Ekādasakaṃ"}],
    "Rūpakaṇḍe paṭhamabhāṇavāro.": [{"chapter": "kaṇḍe"}, {"recitation": "bhāṇa", "section": "vāro"}],
    "Aṭṭhamabhāṇavāro.": [{"eighth": "Aṭṭhama", "recitation": "bhāṇa", "section": "vāro"}],
    "Rūpavibhatti.": [{"classification": "vibhatti"}],
    "Rūpakaṇḍaṃ niṭṭhitaṃ.": [{"chapter": "kaṇḍaṃ"}, {"complete": "niṭṭhitaṃ"}],
    "Idaṃ taṃ rūpaṃ upādā.": [FRAME, TERM["upādā"]],
    "Idaṃ taṃ rūpaṃ no upādā.": [FRAME, TERM["upādā"]],
    "Rūpāyatanaṃ diṭṭhaṃ, saddāyatanaṃ sutaṃ, gandhāyatanaṃ rasāyatanaṃ phoṭṭhabbāyatanaṃ mutaṃ, "
    "sabbaṃ rūpaṃ manasā viññātaṃ rūpaṃ.": [
        cap(ITEM["rūpāyatanaṃ"], "Rūpāyatanaṃ"), ITEM["saddāyatanaṃ"], {"heard": "sutaṃ"},
        ITEM["gandhāyatanaṃ"], ITEM["rasāyatanaṃ"], ITEM["phoṭṭhabbāyatanaṃ"], {"sensed": "mutaṃ"}, FRAME,
        {"form is material": "rūpaṃ manasā viññātaṃ rūpaṃ", "mind": "manasā",
         "cognized": "viññātaṃ", "material form cognized": "viññātaṃ rūpaṃ"}],
}
for _n in ("Catukkaṃ", "Pañcakaṃ", "Chakkaṃ", "Sattakaṃ", "Aṭṭhakaṃ", "Navakaṃ"):
    LINE_UNITS[f"##### {_n}"] = []
    LINE_UNITS[f"{_n}."] = []

KNOW = {"cakkhu": "eye", "sota": "ear", "ghāna": "nose", "jivhā": "tongue", "kāya": "body"}


def knowable_line(line):
    """Chakkaṃ / Sattakaṃ / Aṭṭhakaṃ lists: 'Rūpāyatanaṃ cakkhuviññeyyaṃ rūpaṃ, ...'."""
    u = []
    first = True
    for part in line.rstrip(".").split(", "):
        w = part.split()
        if w[0] == "sabbaṃ":  # sabbaṃ rūpaṃ X-viññeyyaṃ rūpaṃ
            kn = w[2][:-len("viññeyyaṃ")]
            u.append(FRAME)
            d = {"form is material": " ".join(w[1:])}
            if kn == "mano":
                d.update({"mind": "mano"})
            else:  # manoviññāṇadhātu
                d.update({"mind-consciousness": "manoviññāṇa", "mind-consciousness element": "manoviññāṇadhātu",
                          "element": "dhātu"})
            u.append(d)
            continue
        if w[0] in ("manāpiyo", "amanāpiyo"):  # manāpiyo phoṭṭhabbo sukhasamphasso kāyaviññeyyaṃ rūpaṃ
            u.append({"agreeable" if w[0] == "manāpiyo" else "disagreeable": w[0]})
            u.append({"touch": "phoṭṭhabbo"})
            u.append({"pleasant" if w[2].startswith("sukha") else "painful": w[2][:-len("samphasso")],
                      "touch": "samphasso"})
            u.append({"body": "kāya", "knowable": "viññeyyaṃ", **FRAME,
                      "material form knowable": "viññeyyaṃ rūpaṃ", "form knowable": "viññeyyaṃ rūpaṃ"})
            continue
        items = [x for x in w if x.endswith("āyatanaṃ")]
        for x in items:
            u.append(item_unit(x) if first else ITEM[x[0].lower() + x[1:]])
            first = False
        kv = w[len(items)]
        kn = kv[:-len("viññeyyaṃ")]
        if len(items) == 1:
            d = {"base is material": f"āyatanaṃ {kv} rūpaṃ"}
        else:
            d = {"base are material": f"āyatanaṃ {kv} rūpaṃ"}
        if kn in KNOW:
            d[KNOW[kn]] = kn
        elif kn == "manodhātu":
            d.update({"mind": "mano", "mind element": "manodhātu", "element": "dhātu"})
        u.append(d)
        u.append({"knowable": "viññeyyaṃ", **FRAME, "material form knowable": "viññeyyaṃ rūpaṃ",
                  "form knowable": "viññeyyaṃ rūpaṃ"})
    return u


QA_RE = re.compile(r"^Katamaṃ taṃ rūpaṃ (.+?)([?.]) (.+) – idaṃ taṃ rūpaṃ (.+?)([.?])$")
NOQ_RE = re.compile(r"^Katamaṃ taṃ rūpaṃ (\S+ \S+) (itthindriyaṃ…pe… kabaḷīkāro āhāro|"
                    r"cakkhāyatanaṃ…pe… kāyāyatanaṃ, .+) – idaṃ taṃ rūpaṃ (.+?)([.?])$")


def line_units(line):
    if line in LINE_UNITS:
        return LINE_UNITS[line]
    m = re.match(r"^Evaṃ (\S+?)(?:vidhena|bbidhena) rūpasaṅgaho\.$", line)
    if m:  # 'vidhena' is written in its own form also where the text doubles it (catubbidhena, chabbidhena)
        num = m.group(1)
        u = [{**{k: "rūpa" for k in FRAME}, "form is classified": "rūpasaṅgaho", "classified": "saṅgaho"},
             {"ways": "vidhena"}]
        if NUMW.get(num):
            u.insert(0, {NUMW[num]: num})
        return u
    if line.startswith("Katamaṃ taṃ rūpaṃ"):
        m = QA_RE.match(line)
        if m:
            q, _, a, q2, _ = m.groups()
        elif " – " not in line:  # bare list answer (^1-595, ^1-646)
            m = re.match(r"^Katamaṃ taṃ rūpaṃ (.+?)\? (.+)\.$", line)
            q, a, q2 = m.group(1), m.group(2), None
        else:  # ^1-895, ^1-939: no question mark
            m = NOQ_RE.match(line)
            q, a, q2, _ = m.groups()
        u = [FRAME] + predicate_units(q) + answer_units(a)
        if q2:
            u += [FRAME] + predicate_units(q2)
        return u
    if line.startswith("Rūpāyatanaṃ cakkhuviññeyyaṃ"):
        return knowable_line(line)
    raise ValueError(f"no units for line {line!r}")


# =====================================================================================
# segments and resolution
# =====================================================================================
ID = re.compile(r"\s*\^([0-9A-Za-z-]+)\s*$")


def segments(ch):
    text = (PALI / f"{ch}.md").read_text(encoding="utf-8")
    out = {}
    for seg in [s for s in text.split("\n\n") if s.strip()]:
        lines = [l.strip() for l in seg.split("\n") if l.strip()]
        m = ID.search(lines[-1])
        lines[-1] = lines[-1][:m.start()].strip()
        out[m.group(1)] = lines
    return out


def resolve(units, kw):
    k = kw.lower()
    atoms, lemmas = [], []
    for d in units:
        v = d.get(k)
        if v is None:
            continue
        for atom in v.split(" / "):
            lm = "NDE" if atom == NDE else lemma(atom)
            if lm not in lemmas:
                lemmas.append(lm)
                atoms.append(atom)
    if len(atoms) > 1 and NDE in atoms:
        atoms.remove(NDE)
    return " / ".join(atoms) if atoms else None


def build(ch, show_joins=False):
    segs = segments(ch)
    src = (HERE / f"{ch}.keywords.md").read_text(encoding="utf-8").splitlines()
    out, missing, joins = [], [], []
    for line in src:
        bid, rest = line.split("] ", 1)
        bid = bid[1:]
        units = [u for l in segs[bid] for u in line_units(l)]
        pairs = []
        for kw in [x.strip() for x in rest.split(", ")]:
            v = resolve(units, kw)
            if v is None:
                missing.append((bid, kw))
                v = "???"
            if " / " in v:
                joins.append((bid, kw, v))
            assert ", " not in v, (bid, kw, v)
            pairs.append(f"{v}={kw}")
        out.append(f"[{bid}] " + ", ".join(pairs))
    if missing:
        for x in missing:
            print("MISSING", *x)
        raise SystemExit(f"{ch}: {len(missing)} keywords without a unit")
    (HERE / f"{ch}.mapped.md").write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")
    print(ch, "lines", len(out), "joined values", len(joins))
    if show_joins:
        seen = {}
        for bid, kw, v in joins:
            seen.setdefault((kw, v), []).append(bid)
        for (kw, v), ids in sorted(seen.items()):
            print(f"   {v}={kw}  [{len(ids)}] {ids[0]}..{ids[-1]}")


if __name__ == "__main__":
    for ch in CHAPTERS:
        build(ch, "--joins" in sys.argv)
