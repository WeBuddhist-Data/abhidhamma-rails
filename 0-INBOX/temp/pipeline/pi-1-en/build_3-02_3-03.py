"""Build the English plain zero-shot of pi-1 parts 3-02 and 3-03 (Rūpakaṇḍa, Rūpavibhatti:
the pairs, triads, fours ... elevens).

usage: python -I -X utf8 build_3-02_3-03.py
Every recurring string is a fixed constant, so every repeat is byte-identical.
Unknown Pāli raises an error instead of being guessed.
"""
import pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SRC = ROOT / "AI_translation" / "pali" / "pi-1_split_chapters"
OUT = ROOT / "AI_translation" / "english" / "pi-1-english-plain-zeroshot_split_chapters"
PARTS = ["3-02-rupakandam.md", "3-03-rupakandam.md"]

sys.path.insert(0, str(HERE))
import build_ch2_01_sample as C  # noqa: E402  (importing only computes the sample text, it does not write)

DASH = C.DASH
S_LAHUTA, S_MUDUTA, S_KAMMANNATA, S_JIVITA = C.S_LAHUTA, C.S_MUDUTA, C.S_KAMMANNATA, C.S_JIVITA
LIFE = C.NAMES["jīvitindriyaṃ"]  # the faculty of life

# =====================================================================================
# 1. Item names of material form (noun phrases)
# =====================================================================================
ITEMS = {
    "cakkhāyatanaṃ": "the eye base",
    "sotāyatanaṃ": "the ear base",
    "ghānāyatanaṃ": "the nose base",
    "jivhāyatanaṃ": "the tongue base",
    "kāyāyatanaṃ": "the body base",
    "rūpāyatanaṃ": "the visible-form base",
    "saddāyatanaṃ": "the sound base",
    "gandhāyatanaṃ": "the smell base",
    "rasāyatanaṃ": "the taste base",
    "phoṭṭhabbāyatanaṃ": "the touch base",
    "cakkhudhātu": "the eye element",
    "sotadhātu": "the ear element",
    "ghānadhātu": "the nose element",
    "jivhādhātu": "the tongue element",
    "kāyadhātu": "the body element",
    "rūpadhātu": "the visible-form element",
    "saddadhātu": "the sound element",
    "gandhadhātu": "the smell element",
    "rasadhātu": "the taste element",
    "phoṭṭhabbadhātu": "the touch element",
    "cakkhundriyaṃ": "the faculty of the eye",
    "sotindriyaṃ": "the faculty of the ear",
    "ghānindriyaṃ": "the faculty of the nose",
    "jivhindriyaṃ": "the faculty of the tongue",
    "kāyindriyaṃ": "the faculty of the body",
    "itthindriyaṃ": "the faculty of femininity",
    "purisindriyaṃ": "the faculty of masculinity",
    "jīvitindriyaṃ": LIFE,
    "kāyaviññatti": "bodily intimation",
    "vacīviññatti": "verbal intimation",
    "ākāsadhātu": "the space element",
    "pathavīdhātu": "the earth element",
    "āpodhātu": "the water element",
    "tejodhātu": "the fire element",
    "vāyodhātu": "the air element",
    "rūpassa lahutā": "lightness of material form",
    "rūpassa mudutā": "pliancy of material form",
    "rūpassa kammaññatā": "workability of material form",
    "rūpassa upacayo": "growth of material form",
    "rūpassa santati": "continuity of material form",
    "rūpassa jaratā": "ageing of material form",
    "rūpassa aniccatā": "impermanence of material form",
    "kabaḷīkāro āhāro": "edible food",
}

# =====================================================================================
# 2. Classification terms (predicates: "the material form that <VP>")
#    Built on the chapter-1 matrix names (^1-M2-9/10/60/61/62/66/67/68, ^1-M1-4).
# =====================================================================================
TERMS = {
    "upādā": "is derived",
    "no upādā": "is not derived",
    "upādiṇṇaṃ": "is produced by past action",
    "anupādiṇṇaṃ": "is not produced by past action",
    "upādiṇṇupādāniyaṃ": "is produced by past action and subject to clinging",
    "anupādiṇṇupādāniyaṃ": "is not produced by past action but subject to clinging",
    "sanidassanaṃ": "is visible",
    "anidassanaṃ": "is invisible",
    "sappaṭighaṃ": "makes impact",
    "appaṭighaṃ": "makes no impact",
    "indriyaṃ": "is a faculty",
    "na indriyaṃ": "is not a faculty",
    "mahābhūtaṃ": "is a great element",
    "na mahābhūtaṃ": "is not a great element",
    "viññatti": "is intimation",
    "na viññatti": "is not intimation",
    "cittasamuṭṭhānaṃ": "arises from mind",
    "na cittasamuṭṭhānaṃ": "does not arise from mind",
    "cittasahabhu": "exists together with mind",
    "na cittasahabhu": "does not exist together with mind",
    "cittānuparivatti": "accompanies mind",
    "na cittānuparivatti": "does not accompany mind",
    "ajjhattikaṃ": "is internal",
    "bāhiraṃ": "is external",
    "oḷārikaṃ": "is gross",
    "sukhumaṃ": "is subtle",
    "dūre": "is far",
    "santike": "is near",
    "anidassanaṃ appaṭighaṃ dhammāyatanapariyāpannaṃ":
        "is invisible, makes no impact and is included in the mental-object base",
}
for k, v in ITEMS.items():
    TERMS[k] = "is " + v
    if k.startswith("rūpassa "):
        TERMS["rūpassa na " + k[len("rūpassa "):]] = "is not " + v
    else:
        TERMS["na " + k] = "is not " + v

# genitive / dative members of the contact chains
GEN = {
    "cakkhusamphassassa": "eye-contact",
    "sotasamphassassa": "ear-contact",
    "ghānasamphassassa": "nose-contact",
    "jivhāsamphassassa": "tongue-contact",
    "kāyasamphassassa": "body-contact",
    "cakkhusamphassajāya vedanāya": "feeling born of eye-contact",
    "kāyasamphassajāya vedanāya": "feeling born of body-contact",
    "saññāya": "perception",
    "cetanāya": "intention",
    "cakkhuviññāṇassa": "eye-consciousness",
    "kāyaviññāṇassa": "body-consciousness",
}
REL = {"vatthu": "a basis for", "ārammaṇaṃ": "an object of"}
COMPOSITE = {}
for g, ge in GEN.items():
    for r, re_ in REL.items():
        for neg in (False, True):
            key = f"{g} {'na ' if neg else ''}{r}"
            COMPOSITE[key] = (g, neg, r)
            TERMS[key] = f"is {'not ' if neg else ''}{re_} {ge}"

VOCAB = set(TERMS) | set(GEN)
MAXW = max(len(k.split()) for k in VOCAB)


def tokenize(text, vocab):
    words, out, i = text.split(), [], 0
    while i < len(words):
        for n in range(min(MAXW, len(words) - i), 0, -1):
            cand = " ".join(words[i:i + n])
            if cand in vocab:
                out.append(cand)
                i += n
                break
        else:
            raise ValueError(f"unknown term at {words[i:]!r} in {text!r}")
    return out


ADJ = {TERMS[k] for k in ("upādā", "no upādā", "upādiṇṇaṃ", "anupādiṇṇaṃ", "sanidassanaṃ", "anidassanaṃ",
                           "ajjhattikaṃ", "bāhiraṃ", "oḷārikaṃ", "sukhumaṃ", "dūre", "santike")}


def combine(a, b):
    """Join two predicates. 'is' is shared only between two adjectives, the first one positive."""
    if " and " in a or " but " in a or " and " in b or " but " in b:
        return a + ", and " + b
    if a in ADJ and " not " not in a and b in ADJ:
        return a + " and " + b[3:]
    return a + " and " + b


PE = "…pe…"


def norm_pe(s):
    return re.sub(r"\s*…pe…\s*", PE + " ", s).replace(PE + " ", PE + " ").strip()


def term_vp(q):
    """Pāli classification term(s) of a question/answer -> English verb phrase."""
    q = re.sub(r"\s*…pe…\s*", PE, q.strip())
    pieces = q.split(PE)
    first = tokenize(pieces[0], VOCAB)
    others = [tokenize(p, VOCAB) for p in pieces[1:]]
    if any(len(o) != 1 for o in others):
        raise ValueError(q)
    chain = [first[-1]] + [o[0] for o in others]
    prefix = first[:-1]
    if len(chain) == 1:
        vp = TERMS[chain[0]]
    elif all(c in TERMS and c not in COMPOSITE for c in chain):
        vps = [TERMS[c] for c in chain]
        assert all(v.startswith("is ") for v in vps), vps
        vp = vps[0] + "… " + "… ".join(v[3:] for v in vps[1:])
    else:
        assert all(c in GEN for c in chain[:-1]) and chain[-1] in COMPOSITE, chain
        g, neg, r = COMPOSITE[chain[-1]]
        vp = f"is {'not ' if neg else ''}{REL[r]} " + "… ".join(GEN[c] for c in chain[:-1] + [g])
    for p in reversed(prefix):
        vp = combine(TERMS[p], vp)
    return vp


# =====================================================================================
# 3. Answer lists of items
# =====================================================================================
CLAUSE = "yaṃ vā panaññampi atthi rūpaṃ"
QUALS = {
    "kammassa katattā": "that is due to past action",
    "na kammassa katattā": "that is not due to past action",
    "cittajaṃ cittahetukaṃ cittasamuṭṭhānaṃ": "that is born of mind, caused by mind, arising from mind",
    "na cittajaṃ na cittahetukaṃ na cittasamuṭṭhānaṃ":
        "that is not born of mind, not caused by mind, not arising from mind",
}
LEAD = {"kammassa katattā": "Due to past action:", "na kammassa katattā": "Not due to past action:"}
WHATEVER = "or whatever other material form there is "
LVOCAB = set(ITEMS) | {CLAUSE} | set(QUALS)


def list_en(a):
    a = a[0].lower() + a[1:]
    a = re.sub(r"\s*…pe…\s*", " " + PE + " ", a).replace(",", " , ")
    words = a.split()
    toks, i = [], 0
    while i < len(words):
        w = words[i]
        if w in (",", PE):
            toks.append(w); i += 1; continue
        for n in range(min(6, len(words) - i), 0, -1):
            cand = " ".join(words[i:i + n])
            if cand in LVOCAB:
                toks.append(cand); i += n; break
        else:
            raise ValueError(f"unknown list item at {words[i:]!r} in {a!r}")
    out, prev = "", None  # prev: 'item' | 'pe' | 'colon' | None
    j = 0
    while j < len(toks):
        t = toks[j]
        if t == ",":
            j += 1; continue
        if t == PE:
            out += "…"; prev = "pe"; j += 1; continue
        if t == CLAUSE:
            q = toks[j + 1]
            assert q in QUALS, toks
            out += ", " + WHATEVER + QUALS[q] + ":"
            prev = "colon"; j += 2; continue
        if t in LEAD and prev is None:
            out += LEAD[t]; prev = "colon"; j += 1; continue
        assert t in ITEMS, t
        if prev == "item":
            out += ", "
        elif prev in ("pe", "colon"):
            out += " "
        out += ITEMS[t]; prev = "item"; j += 1
    return out[0].upper() + out[1:]


# =====================================================================================
# 4. Definitions
# =====================================================================================
IA = "invisible and making impact"
VA = "visible and making impact"
ARISE = "has arisen, arises, will arise or might arise"
STRIKE = "has struck, strikes, will strike or might strike"
SENS = "sensitivity derived from the four great elements, included in one's own person, " + IA
NAMES_COMMON = ("this is a world, this is a door, this is an ocean, this is radiance, this is a field, "
                "this is a basis")
NAMES_TAIL = "this is the near shore, this is an empty village"

ORGANS = {
    # key: (noun, base, element, faculty, verbs(past, present, base), object-with-clause, object short,
    #       contact, consciousness, extra names)
    "cakkhu": ("eye", ("seen", "sees", "see"), "a visible form that is visible and makes impact",
               "a visible form", True),
    "sotaṃ": ("ear", ("heard", "hears", "hear"), "a sound that is invisible and makes impact", "a sound", False),
    "ghānaṃ": ("nose", ("smelled", "smells", "smell"), "a smell that is invisible and makes impact",
               "a smell", False),
    "jivhā": ("tongue", ("tasted", "tastes", "taste"), "a taste that is invisible and makes impact",
              "a taste", False),
    "kāyo": ("body", ("touched", "touches", "touch"), "a touch that is invisible and makes impact",
             "a touch", False),
}


def verbs(v):
    return f"{v[0]}, {v[1]}, will {v[2]} or might {v[2]}"


def organ_names(o, extra):
    s = (f"this is the {o}, this is the {o} base, this is the {o} element, this is the faculty of the {o}, "
         + NAMES_COMMON + ", ")
    if extra:
        s += "this is a guide, this is a leader, "
    return s + NAMES_TAIL


def organ_def(key, variant, vbracket=""):
    o, v, obj, objs, extra = ORGANS[key]
    head = f"The {o}{vbracket} that is {SENS}"
    names = organ_names(o, extra)
    contact, cons = f"{o}-contact", f"{o}-consciousness"
    if variant == "abbr":
        return f"The {o} that is sensitivity derived from the four great elements… {NAMES_TAIL.split(', ')[-1]}"
    if variant == "a":
        mid = f"the {o}, {IA}, with which one has {verbs(v)} {obj}"
    elif variant == "b":
        mid = f"the {o}, {IA}, on which {obj} {STRIKE}"
    elif variant == "c":
        mid = f"the {o}, {IA}, which {STRIKE} against {obj}"
    elif variant == "d":
        mid = (f"the {o} depending on which, on account of {objs}, {contact} {ARISE}… "
               f"the {o} depending on which, on account of {objs}, feeling born of {contact}… perception… "
               f"intention… {cons} {ARISE}… "
               f"the {o} depending on which {contact} with {objs} as its object {ARISE}… "
               f"the {o} depending on which feeling born of {contact} with {objs} as its object… perception… "
               f"intention… {cons} {ARISE}")
    return f"{head}; {mid}; {names}"


COLOURS = ("blue, yellow, red, white, black, crimson{v1}, green, green-coloured, the colour of mango shoots, "
           "long, short, small, large, round, circular, square{v2}, six-sided, eight-sided, sixteen-sided, "
           "low, high, shadow, sunshine, light, darkness, cloud, mist, smoke, dust, "
           "the colour and appearance of the moon's disc, the colour and appearance of the sun's disc{v3}, "
           "the colour and appearance of the stars, the colour and appearance of a mirror's disc, "
           "the colour and appearance of gems, conch shells, pearls and beryl, "
           "the colour and appearance of gold and silver")
SOUNDS = ("the sound of drums, the sound of tabors, the sound of conches, the sound of tom-toms, "
          "the sound of singing, the sound of instruments, the sound of cymbals, the sound of hand-clapping, "
          "the noise of beings, the sound of things knocking together, the sound of wind, the sound of water, "
          "the sound of humans, the sound of non-human beings")
SMELLS = ("the smell of roots, the smell of heartwood, the smell of bark, the smell of leaves, "
          "the smell of flowers, the smell of fruits, the smell of raw flesh, the smell of rot, "
          "a pleasant smell, an unpleasant smell")
TASTES = ("the taste of roots, the taste of stems, the taste of bark, the taste of leaves, the taste of flowers, "
          "the taste of fruits, sour, sweet, bitter, pungent, salty, alkaline, tart{v1}, astringent, tasty, "
          "not tasty")
TOUCH_HEAD = ("The earth element, the fire element, the air element, hard, soft, smooth, rough, "
              "pleasant to touch, painful to touch, heavy, light")

OBJECTS = {
    # key: (object noun, organ, verbs, quality, head-template, names)
    "rūpa": ("visible form", "eye", ("seen", "sees", "see"), VA, None,
             "this is visible form, this is the visible-form base, this is the visible-form element", "eye"),
    "sadda": ("sound", "ear", ("heard", "hears", "hear"), IA, SOUNDS,
              "this is sound, this is the sound base, this is the sound element", "ear"),
    "gandha": ("smell", "nose", ("smelled", "smells", "smell"), IA, SMELLS,
               "this is smell, this is the smell base, this is the smell element", "nose"),
    "rasa": ("taste", "tongue", ("tasted", "tastes", "taste"), IA, TASTES,
             "this is taste, this is the taste base, this is the taste element", "tongue"),
    "phoṭṭhabba": ("touch", "body", ("touched", "touches", "touch"), IA, None,
                   "this is touch, this is the touch base, this is the touch element", "body"),
}


def object_head(key, bracket_variants):
    n, organ, v, q, lst, names, _ = OBJECTS[key]
    if key == "rūpa":
        if bracket_variants:
            col = COLOURS.format(v1=" [variant: mañjeṭṭhakaṃ (Sī., Syā.)]", v2=" [variant: caturassaṃ (Sī., Ka.)]",
                                 v3=" [variant: suriyamaṇḍalassa (Sī., Syā.)]")
        else:
            col = COLOURS.format(v1="", v2="", v3="")
        d = f"colour and appearance derived from the four great elements, {VA}"
        return f"The visible form that is {d}: {col}, or whatever other visible form there is that is {d}"
    if key == "phoṭṭhabba":
        return TOUCH_HEAD
    if key == "rasa":
        lst = lst.format(v1=" [variant: lapilakaṃ (Sī.)]" if bracket_variants else "")
    d = f"derived from the four great elements, {IA}"
    return f"The {n} that is {d}: {lst}, or whatever other {n} there is that is {d}"


def object_def(key, variant, bracket_variants=False):
    n, organ, v, q, lst, names, _ = OBJECTS[key]
    if variant == "abbr":
        if key == "rūpa":
            return ("The visible form that is colour and appearance derived from the four great elements… "
                    "this is the visible-form element")
        if key == "phoṭṭhabba":
            return "The earth element… this is the touch element"
        raise ValueError(key)
    head = object_head(key, bracket_variants)
    contact, cons = f"{organ}-contact", f"{organ}-consciousness"
    if variant == "a":
        mid = f"the {n}, {q}, that one has {verbs(v)} with the {organ}, {IA}"
    elif variant == "b":
        mid = f"the {n}, {q}, on which the {organ}, {IA}, {STRIKE}"
    elif variant == "c":
        mid = f"the {n}, {q}, which {STRIKE} against the {organ}, {IA}"
    elif variant == "d":
        mid = (f"the {n} on account of which, depending on the {organ}, {contact} {ARISE}… "
               f"the {n} on account of which, depending on the {organ}, feeling born of {contact}… perception… "
               f"intention… {cons} {ARISE}… "
               f"the {n} with which as its object, depending on the {organ}, {contact} {ARISE}… "
               f"the {n} with which as its object, depending on the {organ}, feeling born of {contact}… "
               f"perception… intention… {cons} {ARISE}")
    return f"{head}; {mid}; {names}"


IN_RUPA = "Whatever, in material form, is "
OWN_OTHERS = ", whether one's own or others', produced by past action or not produced by past action"
SPEECH = "speech, utterance, way of speaking, uttering, voice, voicing, speech, breaking into speech"
MINDS = "from a wholesome mind, an unwholesome mind or an indeterminate mind"
INTIM = "intimation, making known, the state of having made known"

SHORT_DEFS = {
    "Yaṃ itthiyā itthiliṅgaṃ itthinimittaṃ itthikuttaṃ itthākappo itthattaṃ itthibhāvo":
        "Whatever, in a woman, is the feminine feature, the feminine sign, feminine conduct, the feminine manner, "
        "femininity, the state of being a woman",
    "Yaṃ purisassa purisaliṅgaṃ purisanimittaṃ purisakuttaṃ purisākappo purisattaṃ purisabhāvo":
        "Whatever, in a man, is the masculine feature, the masculine sign, masculine conduct, the masculine manner, "
        "masculinity, the state of being a man",
    "Yo tesaṃ rūpīnaṃ dhammānaṃ āyu ṭhiti yapanā yāpanā iriyanā vattanā pālanā jīvitaṃ jīvitindriyaṃ":
        "Whatever, in those material states, is " + S_JIVITA,
    "Yā kusalacittassa vā akusalacittassa vā abyākatacittassa vā abhikkamantassa vā paṭikkamantassa vā "
    "ālokentassa vā vilokentassa vā samiñjentassa vā pasārentassa vā kāyassa thambhanā santhambhanā "
    "santhambhitattaṃ viññatti viññāpanā viññāpitattaṃ":
        f"Whatever, {MINDS}, in one who goes forward, goes back, looks ahead, looks around, bends or stretches, "
        f"is the stiffening of the body, firm stiffening, the state of being firmly stiffened, {INTIM}",
    "Yo ākāso ākāsagataṃ aghaṃ aghagataṃ vivaro vivaragataṃ asamphuṭṭhaṃ catūhi mahābhūtehi":
        "Whatever is space, what counts as space, void, what counts as void, an opening, what counts as an opening, "
        "untouched by the four great elements",
    "Yaṃ āpo āpogataṃ sineho sinehagataṃ bandhanattaṃ rūpassa":
        "Whatever is water, what counts as water, moisture, what counts as moisture, the binding of material form",
    "Yā rūpassa lahutā lahupariṇāmatā adandhanatā avitthanatā": IN_RUPA + S_LAHUTA,
    "Yā rūpassa mudutā maddavatā akakkhaḷatā akathinatā": IN_RUPA + S_MUDUTA,
    "Yā rūpassa kammaññatā kammaññattaṃ kammaññabhāvo": IN_RUPA + S_KAMMANNATA,
    "Yo āyatanānaṃ ācayo, so rūpassa upacayo":
        "Whatever is accumulation of the sense bases, that is growth of material form",
    "Yo rūpassa upacayo, sā rūpassa santati":
        "Whatever is growth of material form, that is continuity of material form",
    "Yā rūpassa jarā jīraṇatā khaṇḍiccaṃ pāliccaṃ valittacatā āyuno saṃhāni indriyānaṃ paripāko":
        IN_RUPA + "ageing, growing old, broken teeth, grey hair, wrinkled skin, the dwindling of life, "
        "the over-ripening of the faculties",
    "Yo rūpassa khayo vayo bhedo paribhedo aniccatā antaradhānaṃ":
        IN_RUPA + "destruction, passing away, breaking up, falling apart, impermanence, disappearance",
    "Yaṃ kakkhaḷaṃ kharagataṃ [kharigataṃ (ka.)] kakkhaḷattaṃ kakkhaḷabhāvo ajjhattaṃ vā bahiddhā vā "
    "upādiṇṇaṃ vā anupādiṇṇaṃ vā":
        "Whatever is hard, what counts as harsh [variant: kharigataṃ (Ka.)], hardness, the state of being hard"
        + OWN_OTHERS,
    "Yaṃ āpo āpogataṃ sineho sinehagataṃ bandhanattaṃ rūpassa ajjhattaṃ vā bahiddhā vā upādiṇṇaṃ vā "
    "anupādiṇṇaṃ vā":
        "Whatever is water, what counts as water, moisture, what counts as moisture, the binding of material form"
        + OWN_OTHERS,
    "Yaṃ tejo tejogataṃ usmā usmāgataṃ usumaṃ usumagataṃ ajjhattaṃ vā bahiddhā vā upādiṇṇaṃ vā anupādiṇṇaṃ vā":
        "Whatever is fire, what counts as fire, warmth, what counts as warmth, heat, what counts as heat"
        + OWN_OTHERS,
    "Yaṃ vāyo vāyogataṃ thambhitattaṃ rūpassa ajjhattaṃ vā bahiddhā vā upādiṇṇaṃ vā anupādiṇṇaṃ vā":
        "Whatever is air, what counts as air, the stiffened state of material form" + OWN_OTHERS,
}
_VACI_HEAD = f"Whatever, {MINDS}, is {SPEECH}"
_VACI_TAIL = f"this is called speech. Whatever, through that speech, is {INTIM}"
_KABALI = ("Boiled rice, porridge, barley meal, fish, meat, milk, curd, ghee, butter, oil, honey, molasses, "
           "or whatever other material form there is in whatever country that the beings there eat with the mouth, "
           "chew with the teeth, swallow down the throat and that fills the belly, the nutritive essence by which "
           "beings keep alive")
_VACI_P = ("Yā kusalacittassa vā akusalacittassa vā abyākatacittassa vā vācā girā byappatho udīraṇaṃ {g} "
           "ghosakammaṃ vācā vacībhedo{sep} ayaṃ vuccati vācā. Yā tāya vācāya viññatti viññāpanā viññāpitattaṃ")
SHORT_DEFS[_VACI_P.format(g="ghoso", sep=" –")] = f"{_VACI_HEAD} {DASH} {_VACI_TAIL}"
SHORT_DEFS[_VACI_P.format(g="ghoso", sep=",")] = f"{_VACI_HEAD}, {_VACI_TAIL}"
SHORT_DEFS[_VACI_P.format(g="dhoso", sep=",")] = f"{_VACI_HEAD}, {_VACI_TAIL}"  # ^1-850: 'dhoso' (source slip)
_KAB_P = ("Odano kummāso sattu maccho maṃsaṃ khīraṃ dadhi sappi navanītaṃ telaṃ madhu phāṇitaṃ, yaṃ vā "
          "panaññampi atthi rūpaṃ yamhi yamhi janapade tesaṃ tesaṃ sattānaṃ mukhāsiyaṃ dantavikhādanaṃ "
          "galajjhoharaṇīyaṃ kucchivitthambhanaṃ{sep} yāya ojāya sattā yāpenti")
SHORT_DEFS[_KAB_P.format(sep=",")] = _KABALI
SHORT_DEFS[_KAB_P.format(sep="")] = _KABALI
SHORT_DEFS[
    "Yaṃ itthiyā itthiliṅgaṃ itthinimittaṃ itthikuttaṃ itthākappo itthattaṃ itthibhāvo [itthittaṃ itthībhāvo (syā.)]"
] = SHORT_DEFS["Yaṃ itthiyā itthiliṅgaṃ itthinimittaṃ itthikuttaṃ itthākappo itthattaṃ itthibhāvo"] + \
    " [variant: itthittaṃ itthībhāvo (Syā.)]"

ORG_RE = re.compile(r"^(Yaṃ cakkhu|Yaṃ sotaṃ|Yaṃ ghānaṃ|Yā jivhā|Yo kāyo)( \[cakkhuṃ \(sī\. syā\.\)\])? "
                    r"catunnaṃ mahābhūtānaṃ upādāya pasādo")
OBJ_RE = re.compile(r"^(Yaṃ rūpaṃ|Yo saddo|Yo gandho|Yo raso) catunnaṃ mahābhūtānaṃ upādāya")
OBJ_KEY = {"Yaṃ rūpaṃ": "rūpa", "Yo saddo": "sadda", "Yo gandho": "gandha", "Yo raso": "rasa"}


def def_en(a):
    """Return the English of a definition answer, or None if `a` is an item list."""
    if a in SHORT_DEFS:
        return SHORT_DEFS[a]
    m = ORG_RE.match(a)
    if m:
        key = m.group(1).split()[1]
        vb = " [variant: cakkhuṃ (Sī., Syā.)]" if m.group(2) else ""
        if "pasādo…pe…" in a:
            assert a.endswith("suñño gāmo peso"), a
            return organ_def(key, "abbr")
        rest = a.split("sappaṭigho, ", 1)[1]
        if " nissāya " in rest:
            var = "d"
        elif re.search(r"\b(passi|suṇi|ghāyi|sāyi|phusi) vā", rest):
            var = "a"
        elif rest.startswith(("yamhi", "yāya")):
            var = "b"
        elif re.match(r"(yaṃ cakkhu|yaṃ sotaṃ|yaṃ ghānaṃ|yā jivhā|yo kāyo) anidassan", rest):
            var = "c"
        else:
            raise ValueError(a)
        assert re.search(r"suñño gāmo ?peso$", a), a
        return organ_def(key, var, vb)
    m = OBJ_RE.match(a)
    if m or a.startswith("Pathavīdhātu"):
        key = OBJ_KEY[m.group(1)] if m else "phoṭṭhabba"
        if "…pe…" in a.split(",")[0] and "ārabbha" not in a:
            return object_def(key, "abbr")
        tail = a.rsplit("sappaṭighaṃ, " if key == "rūpa" else
                        ("lahukaṃ, " if key == "phoṭṭhabba" else "sappaṭigho, "), 1)[1]
        if "ārabbha" in tail:
            var = "d"
        elif re.search(r"\b(passi|suṇi|ghāyi|sāyi|phusi) vā", tail):
            var = "a"
        elif tail.startswith("yamhi"):
            var = "b"
        elif "paṭihaññi" in tail:
            var = "c"
        else:
            raise ValueError(a)
        return object_def(key, var, "[" in a)
    return None


# =====================================================================================
# 5. Fixed lines and headings
# =====================================================================================
HEADINGS = {
    "##### Dukaniddeso": "##### The Exposition of the Pairs",
    "###### Upādābhājanīyaṃ": "###### The Analysis of Derived Material Form",
    "##### Tikaniddeso": "##### The Exposition of the Sets of Three",
    "##### Catukkaṃ": "##### The Sets of Four",
    "##### Pañcakaṃ": "##### The Set of Five",
    "##### Chakkaṃ": "##### The Set of Six",
    "##### Sattakaṃ": "##### The Set of Seven",
    "##### Aṭṭhakaṃ": "##### The Set of Eight",
    "##### Navakaṃ": "##### The Set of Nine",
    "##### Dasakaṃ": "##### The Set of Ten",
    "##### Ekādasakaṃ": "##### The Set of Eleven",
}
NUM = {"du": "two", "ti": "three", "catub": "four", "pañca": "five", "cha": "six", "satta": "seven",
       "aṭṭha": "eight", "nava": "nine", "dasa": "ten", "ekādasa": "eleven"}
KN = "knowable by"
LINES = {
    "Idaṃ taṃ rūpaṃ upādā.": "This is the material form that is derived.",
    "Upādābhājanīyaṃ.": "The analysis of derived material form.",
    "Rūpakaṇḍe paṭhamabhāṇavāro.": "The first recitation section of the chapter on material form.",
    "Idaṃ taṃ rūpaṃ no upādā.": "This is the material form that is not derived.",
    "Dukaniddeso.": "The exposition of the pairs.",
    "Tikaniddeso.": "The exposition of the sets of three.",
    "Catukkaṃ.": "The sets of four.",
    "Pañcakaṃ.": "The set of five.",
    "Chakkaṃ.": "The set of six.",
    "Sattakaṃ.": "The set of seven.",
    "Aṭṭhakaṃ.": "The set of eight.",
    "Navakaṃ.": "The set of nine.",
    "Dasakaṃ.": "The set of ten.",
    "Ekādasakaṃ.": "The set of eleven.",
    "Aṭṭhamabhāṇavāro.": "The eighth recitation section.",
    "Rūpavibhatti.": "The classification of material form.",
    "Rūpakaṇḍaṃ niṭṭhitaṃ.": "The chapter on material form is complete.",
    "Rūpāyatanaṃ diṭṭhaṃ, saddāyatanaṃ sutaṃ, gandhāyatanaṃ rasāyatanaṃ phoṭṭhabbāyatanaṃ mutaṃ, "
    "sabbaṃ rūpaṃ manasā viññātaṃ rūpaṃ.":
        "The visible-form base is seen, the sound base is heard, the smell base, the taste base and the touch base "
        "are sensed, and all material form is material form cognized by the mind.",
}
for p, e in (("du", "two"), ("ti", "three"), ("catub", "four"), ("pañca", "five"), ("cha", "six"),
             ("satta", "seven"), ("aṭṭha", "eight"), ("nava", "nine"), ("dasa", "ten"), ("ekādasa", "eleven")):
    LINES[f"Evaṃ {p}vidhena rūpasaṅgaho."] = f"Thus material form is classified in {e} ways."
LINES["Evaṃ catubbidhena rūpasaṅgaho."] = LINES.pop("Evaṃ catubvidhena rūpasaṅgaho.")
LINES["Evaṃ chabbidhena rūpasaṅgaho."] = LINES.pop("Evaṃ chavidhena rūpasaṅgaho.")

_FIVE = (f"the visible-form base is material form {KN} the eye, the sound base is material form {KN} the ear, "
         f"the smell base is material form {KN} the nose, the taste base is material form {KN} the tongue")
_BODY = f"the touch base is material form {KN} the body"
_MANODHATU = (f"the visible-form base, the sound base, the smell base, the taste base and the touch base are "
              f"material form {KN} the mind element")
_LAST = f"and all material form is material form {KN} the mind-consciousness element."
_AGREE = (f"an agreeable touch that is pleasant to touch is material form {KN} the body, "
          f"a disagreeable touch that is painful to touch is material form {KN} the body")
LINES[("Rūpāyatanaṃ cakkhuviññeyyaṃ rūpaṃ, saddāyatanaṃ sotaviññeyyaṃ rūpaṃ, gandhāyatanaṃ ghānaviññeyyaṃ "
       "rūpaṃ, rasāyatanaṃ jivhāviññeyyaṃ rūpaṃ, phoṭṭhabbāyatanaṃ kāyaviññeyyaṃ rūpaṃ, sabbaṃ rūpaṃ "
       "manoviññeyyaṃ rūpaṃ.")] = \
    "T" + _FIVE[1:] + f", {_BODY}, and all material form is material form {KN} the mind."
LINES[("Rūpāyatanaṃ cakkhuviññeyyaṃ rūpaṃ, saddāyatanaṃ sotaviññeyyaṃ rūpaṃ, gandhāyatanaṃ ghānaviññeyyaṃ "
       "rūpaṃ, rasāyatanaṃ jivhāviññeyyaṃ rūpaṃ, phoṭṭhabbāyatanaṃ kāyaviññeyyaṃ rūpaṃ, rūpāyatanaṃ "
       "saddāyatanaṃ gandhāyatanaṃ rasāyatanaṃ phoṭṭhabbāyatanaṃ manodhātuviññeyyaṃ rūpaṃ, sabbaṃ rūpaṃ "
       "manoviññāṇadhātuviññeyyaṃ rūpaṃ.")] = \
    "T" + _FIVE[1:] + f", {_BODY}, {_MANODHATU}, {_LAST}"
LINES[("Rūpāyatanaṃ cakkhuviññeyyaṃ rūpaṃ, saddāyatanaṃ sotaviññeyyaṃ rūpaṃ, gandhāyatanaṃ ghānaviññeyyaṃ "
       "rūpaṃ, rasāyatanaṃ jivhāviññeyyaṃ rūpaṃ, manāpiyo phoṭṭhabbo sukhasamphasso kāyaviññeyyaṃ rūpaṃ, "
       "amanāpiyo phoṭṭhabbo dukkhasamphasso kāyaviññeyyaṃ rūpaṃ, rūpāyatanaṃ saddāyatanaṃ gandhāyatanaṃ "
       "rasāyatanaṃ phoṭṭhabbāyatanaṃ manodhātuviññeyyaṃ rūpaṃ, sabbaṃ rūpaṃ manoviññāṇadhātuviññeyyaṃ rūpaṃ.")] = \
    "T" + _FIVE[1:] + f", {_AGREE}, {_MANODHATU}, {_LAST}"

FRAME_Q = "What is the material form that {}{}"
FRAME_A = "{} " + DASH + " this is the material form that {}{}"

QA_RE = re.compile(r"^Katamaṃ taṃ rūpaṃ (.+?)([?.]) (.+) – idaṃ taṃ rūpaṃ (.+?)([.?])$")
NOQ_RE = re.compile(r"^Katamaṃ taṃ rūpaṃ (\S+ \S+) (itthindriyaṃ…pe… kabaḷīkāro āhāro|"
                    r"cakkhāyatanaṃ…pe… kāyāyatanaṃ, .+) – idaṃ taṃ rūpaṃ (.+?)([.?])$")


def qa_en(line):
    m = QA_RE.match(line)
    if m:
        q, qp, a, q2, ap = m.groups()
        qtext = FRAME_Q.format(term_vp(q), qp)
    elif " – " not in line:  # ^1-595, ^1-646: bare list answer, no closing formula
        m = re.match(r"^Katamaṃ taṃ rūpaṃ (.+?)\? (.+)\.$", line)
        return FRAME_Q.format(term_vp(m.group(1)), "?") + " " + list_en(m.group(2)) + "."
    else:  # ^1-895, ^1-939: no question mark after the question (source as written)
        m = NOQ_RE.match(line)
        if not m:
            raise ValueError(line)
        q, a, q2, ap = m.groups()
        qtext = FRAME_Q.format(term_vp(q), "")
        a = a[0].upper() + a[1:]
    ae = def_en(a)
    if ae is None:
        ae = list_en(a)
    if not m.re is QA_RE:
        ae = ae[0].lower() + ae[1:]
    return qtext + " " + FRAME_A.format(ae, term_vp(q2), ap)


def line_en(line):
    if line.startswith("#"):
        return HEADINGS[line]
    if line.startswith("Katamaṃ taṃ rūpaṃ"):
        return qa_en(line)
    return LINES[line]


ID = re.compile(r"\s*\^([0-9A-Za-z-]+)\s*$")


def build(part):
    text = (SRC / part).read_text(encoding="utf-8")
    segs = [s for s in text.split("\n\n") if s.strip()]
    out = []
    for seg in segs:
        lines = [l for l in seg.split("\n") if l.strip()]
        m = ID.search(lines[-1])
        assert m, lines[-1]
        lines[-1] = lines[-1][:m.start()]
        en = [line_en(l.strip()) for l in lines]
        en[-1] += f" ^{m.group(1)}"
        out.append("\n".join(en))
    return "\n\n".join(out) + "\n"


if __name__ == "__main__":
    for part in PARTS:
        t = build(part)
        (OUT / part).write_text(t, encoding="utf-8", newline="\n")
        print("wrote", OUT / part, t.count("\n\n") + 1, "segments")
