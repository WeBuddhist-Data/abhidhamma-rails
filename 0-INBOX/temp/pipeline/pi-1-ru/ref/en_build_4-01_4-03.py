"""Build the English plain zero-shot of pi-1 parts 4-01 and 4-03 (Nikkhepakanda).

usage: python -I -X utf8 build_4-01_4-03.py
Matrix item wording comes from build_matika.MATRIX_ITEMS, synonym strings and factor
names from build_ch2_01_sample. All recurring formulas are fixed constants below.
"""
import pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import build_matika as M          # noqa: E402  (import does not write anything)
import build_ch2_01_sample as C   # noqa: E402

ROOT = HERE.parents[3]
PALI_DIR = ROOT / "AI_translation" / "pali" / "pi-1_split_chapters"
OUT_DIR = ROOT / "AI_translation" / "english" / "pi-1-english-plain-zeroshot_split_chapters"

D = C.DASH  # "–"
N = C.NAMES

# ---------------------------------------------------------------- matrix items -------
ITEM = {(bid, l): e for bid, l, p, e in M.MATRIX_ITEMS}


def item(bid, l, variant=False):
    e = ITEM[(f"1-M{bid}", l)]
    if not variant:
        e = re.sub(r" \[variant: [^\]]*\]", "", e)
    return e.rstrip(".")


def lc(s):
    return s[0].lower() + s[1:]


def kind(e):
    """A: '<adj> states'; P: predicate after 'states'; N: noun phrase 'the states ...'."""
    if not e.startswith("States "):
        assert e.endswith(" states"), e
        return "A", lc(e[:-len(" states")])
    rest = e[len("States "):]
    if rest.startswith("that some "):
        return "N", rest
    if rest.startswith("that "):
        return "P", rest[len("that "):]
    if rest.split()[0] in ("with", "without", "whose", "of", "leading"):
        return "N", rest
    return "P", "are " + rest


def Qd(e):
    """Frame shared with chapter 5 (build_5_atthakathakandam.Q): What are <item>?"""
    return f"What are {lc(e)}?"


def Cl(e):
    """Frame shared with chapter 5 (build_5_atthakathakandam.E): these are <item>"""
    return f"these are {lc(e)}"


def QA(mid, l, body):
    """Katame dhammā X? <body> – ime dhammā X."""
    e = item(mid, l)
    return f"{Qd(e)} {body} {D} {Cl(e)}."


def Q(mid, l):
    return Qd(item(mid, l))


def CL(mid, l):
    return Cl(item(mid, l))


# ---------------------------------------------------------------- fixed strings ------
SPH = {"k": "of the sense sphere", "r": "of the fine-material sphere", "a": "of the immaterial sphere",
       "p": "not included in the spheres of existence"}


def whether(keys):
    parts = [SPH[k] for k in keys]
    if len(parts) == 1:
        return parts[0]
    return "whether " + ", ".join(parts[:-1]) + " or " + parts[-1]


W4 = whether("krap")
W3 = whether("kra")

KH4 = "the aggregate of feeling, the aggregate of perception, the aggregate of mental formations, the aggregate of consciousness"
KH_PE = "the aggregate of feeling … the aggregate of consciousness"
KH5 = "the aggregate of material form, " + KH4
KH_R_PE = "the aggregate of material form … the aggregate of consciousness"
TS4 = "the associated aggregate of feeling, aggregate of perception, aggregate of mental formations, aggregate of consciousness"
TS_PE = "the associated aggregate of feeling … aggregate of consciousness"
TS3 = "the associated aggregate of perception, aggregate of mental formations, aggregate of consciousness"
KAMMA = "the bodily action, verbal action and mental action arising from them"
TADEK = "and the defilements that occur together with them"
ROOTS_K = f"The three wholesome roots {D} non-greed, non-hate, non-delusion"
ROOTS_A = f"The three unwholesome roots {D} greed, hate, delusion"
KIRIYA = "those states that are merely functional, neither wholesome nor unwholesome nor results of action"
RUPA_ASANKH = "all material form, and the unconditioned element"
MAGGA = "The paths not included in the spheres of existence, the fruits of the paths, and the unconditioned element"
PATHS4 = "The four paths not included in the spheres of existence"
VIPAKA = "The results of wholesome and unwholesome states"
KUSAKU = "Wholesome and unwholesome states"
TE_THAPETVA = "Except for those states, the remaining wholesome, unwholesome and indeterminate states"
RUPA_DHAY = ("whatever material form is invisible, makes no impact and is included in the mental-object base")
CITTACET = "The mind and mental factors that arise taking {} as their object"
KATATTA = "due to action having been done"

BASES = {"cakkh": "the eye base", "sot": "the ear base", "ghān": "the nose base", "jivh": "the tongue base",
         "kāy": "the body base", "rūp": "the visible-form base", "sadd": "the sound base",
         "gandh": "the smell base", "ras": "the taste base", "phoṭṭhabb": "the touch base",
         "man": "the mind base", "dhamm": "the mental-object base"}

# fetters, taints, ties (aligned with notes-5.md)
SAKKAYA = "identity view"
VICI = "doubt"
SILABBATA = "misapprehension of rules and observances"
THREE_FETTERS = f"The three fetters {D} {SAKKAYA}, {VICI}, {SILABBATA}"

KAMASAVA = "the taint of sensual desire"
BHAVASAVA = "the taint of existence"
DITTHASAVA = "the taint of views"
AVIJJASAVA = "the taint of ignorance"

SY = {"kāmarāga": "the fetter of sensual lust", "paṭigha": "the fetter of aversion",
      "māna": "the fetter of conceit", "diṭṭhi": "the fetter of views", "vicikicchā": "the fetter of doubt",
      "sīlabbataparāmāsa": "the fetter of misapprehension of rules and observances",
      "bhavarāga": "the fetter of lust for existence", "issā": "the fetter of envy",
      "macchariya": "the fetter of stinginess", "avijjā": "the fetter of ignorance"}

G_ABH = "the bodily tie of covetousness"
G_BYA = "the bodily tie of ill will"
G_SIL = "the bodily tie of misapprehension of rules and observances"
G_IDAM = "the bodily tie of dogmatic belief that this alone is true"

# synonym strings -------------------------------------------------------------------
DS = ("holding a view, the thicket of views, the wilderness of views, the contortion of views{v}, "
      "the vacillation of views, the fetter of views, grasping, holding firmly, adherence, misapprehension, "
      "a wrong road, a wrong path, wrongness, the ground of sectarian views, grasping things the wrong way round")
DS_PLAIN = DS.format(v="")
DS_V = DS.format(v=" [variant: diṭṭhivisūkāyitaṃ (Sī.)]")
EVA_DITTHI = "whatever view of this kind there is, " + DS_PLAIN
DS_PE = "holding a view … grasping things the wrong way round"

KANKHA_STR = ("uncertainty, being uncertain, the state of being uncertain, perplexity, doubt, wavering, "
              "a forked path, indecision, failure to take a definite stand, hesitation, vacillation, "
              "failure to plunge in, rigidity of mind, mental scratching")
VICI_INTRO = ("One is uncertain and in doubt about the Teacher, uncertain and in doubt about the Teaching, "
              "uncertain and in doubt about the Community, uncertain and in doubt about the training, "
              "uncertain and in doubt about the past, uncertain and in doubt about the future, "
              "uncertain and in doubt about both the past and the future, uncertain and in doubt about "
              "specific conditionality and dependently arisen states")
VICI_REST = "whatever " + KANKHA_STR.replace("uncertainty, ", "uncertainty of this kind there is, ", 1)

SIL_INTRO = ('Ascetics and brahmins outside this teaching hold that "purity comes through rules, '
             'purity comes through observances, purity comes through rules and observances"')

SAKKAYA_BODY = (
    "Here an uninstructed ordinary person, who does not see the noble ones, is not skilled in the teaching "
    "of the noble ones and not trained in the teaching of the noble ones, who does not see good people, "
    "is not skilled in the teaching of good people and not trained in the teaching of good people, "
    "regards material form as self, or self as possessing material form, or material form as in self, "
    "or self as in material form. He regards feeling as self, or self as possessing feeling, or feeling as "
    "in self, or self as in feeling. He regards perception as self, or self as possessing perception, or "
    "perception as in self, or self as in perception. He regards mental formations as self, or self as "
    "possessing mental formations, or mental formations as in self, or self as in mental formations. "
    "He regards consciousness as self, or self as possessing consciousness, or consciousness as in self, "
    "or self as in consciousness. Whatever view of this kind there is, " + DS_V)

# greed
LOBHA = [
    "lust", "passion", "compliance", "accommodation", "delight", "delight and lust{v1}", "passion of the mind",
    "wanting", "infatuation", "holding on", "eagerness", "intense eagerness", "attachment", "the mire",
    "agitation", "deceit", "the begetter", "the producer", "the seamstress{v2}", "the net-maker", "the stream",
    "the entangler", "the thread", "the spreading one", "the accumulator{v3}", "the companion", "aspiration",
    "the conduit to existence", "the forest", "the undergrowth", "intimacy", "affection", "concern", "kinship",
    "hope", "hoping", "the state of hoping{v4}", "hope for visible forms", "hope for sounds", "hope for smells",
    "hope for tastes", "hope for touches", "hope for gain", "hope for wealth", "hope for children",
    "hope for life", "hankering", "intense hankering", "extreme hankering", "hankering", "the act of hankering",
    "the state of hankering", "voracity", "being voracious", "the state of voracity", "fawning{v5}",
    "the wish for fine things", "unrighteous lust", "lawless greed", "liking", "desiring", "longing", "envying",
    "earnest longing", "sensual craving", "craving for continued existence",
    "craving for non-existence", "craving for fine-material existence", "craving for immaterial existence",
    "craving for cessation", "craving for visible forms", "craving for sounds", "craving for smells",
    "craving for tastes", "craving for touches", "craving for mental objects", "the flood", "the yoke",
    "the tie", "clinging", "the obstruction", "the hindrance", "the covering", "the bond", "the corruption",
    "the underlying tendency", "the obsession", "the creeper", "meanness", "the root of suffering",
    "the source of suffering", "the origin of suffering", "Māra's snare", "Māra's hook", "Māra's domain",
    "the river of craving", "the net of craving", "the leash of craving", "the ocean of craving",
    "covetousness", "greed", "the unwholesome root"]
LOBHA_STR = ", ".join(LOBHA)
LOBHA_V = LOBHA_STR.format(v1=" [variant: nandirāgo (Sī.)]", v2=" [variant: sibbanī (Sī.)]",
                           v3=" [variant: āyūhanī (Sī., Syā.)]",
                           v4=" [variant: āsiṃsanā āsiṃsitattaṃ (Sī., Syā.)]",
                           v5=" [variant: puñcikatā (Syā.) pucchikatā (Sī.)]")
LOBHA_PLAIN = LOBHA_STR.format(v1="", v2="", v3="", v4="", v5="")

# hate
DOSA_INTRO = ('Annoyance arises at the thought "He has done me harm", annoyance arises at the thought '
              '"He is doing me harm", annoyance arises at the thought "He will do me harm", annoyance arises '
              'at the thought "He has done harm to someone dear and pleasing to me … he is doing harm … '
              'he will do harm", annoyance arises at the thought "He has done good to someone not dear and '
              'not pleasing to me … he is doing good … he will do good", or annoyance arises without reason.')
DOSA_STR = ("Whatever annoyance of the mind of this kind there is, resentment, aversion, opposition, irritation, "
            "exasperation, fury, hate, hatred, intense hatred, malevolence of the mind, mental hatred, anger, "
            "being angry, the state of being angry, hate, hating, the state of hating, malevolence, "
            "being malicious, the state of being malicious, conflict, opposition, ferocity, abusiveness, "
            "displeasure of the mind")
DOSA_BODY = DOSA_INTRO + " " + DOSA_STR

# delusion
NANA4 = ("knowledge of suffering, knowledge of the arising of suffering, knowledge of the cessation of "
         "suffering, knowledge of the way leading to the cessation of suffering, knowledge of the past, "
         "knowledge of the future, knowledge of both the past and the future, knowledge of specific "
         "conditionality and dependently arisen states")
ANANA4 = NANA4.replace("knowledge of", "lack of knowledge of")
MOHA_REST = ("lack of vision, non-realisation, non-understanding, non-awakening, non-penetration, failure to grasp, "
             "failure to plunge in, failure to examine, failure to reflect, failure to perceive directly, "
             "stupidity, foolishness, lack of clear awareness, delusion, deep delusion, utter delusion, ignorance, "
             "the flood of ignorance, the yoke of ignorance, the underlying tendency to ignorance, "
             "the obsession of ignorance, the bar of ignorance, delusion, the unwholesome root")
EVA_MOHA = "whatever lack of knowledge of this kind there is, " + MOHA_REST
MOHA_PE = "Whatever lack of knowledge there is, lack of vision … the bar of ignorance, delusion, the unwholesome root"

assert C.S_PANNA.startswith("wisdom, ")
EVA_PANNA = "whatever wisdom of this kind there is, " + C.S_PANNA[len("wisdom, "):]
PANNA_PE = "wisdom, understanding … non-delusion, investigation of states, right view"
EVA_PANNA_PE = "whatever wisdom of this kind there is, understanding … non-delusion, investigation of states, right view"

METTA = ("loving-kindness, being loving, the state of being loving, kindness, being kind, the state of being kind, "
         "seeking others' welfare, sympathy")
S_ADOSA_X = C.S_ADOSA.replace("the state of not hating, ", "the state of not hating, " + METTA + ", ", 1)
assert S_ADOSA_X != C.S_ADOSA
S_ADOSA_PE = "non-hate, not hating, the state of not hating … non-ill-will, absence of malice, non-hate, " + C.ROOT

KAMA_STR = ("sensual desire, sensual lust, sensual delight, sensual craving, sensual affection, sensual fever, "
            "sensual infatuation, sensual holding on")
BHAVA_STR = ("desire for existence{v}, lust for existence, delight in existence, craving for continued existence, "
             "affection for existence, fever for existence, infatuation with existence, holding on to existence")
KAMESU = "Whatever, with regard to sensual pleasures, is " + KAMA_STR
BHAVESU = "Whatever, with regard to states of existence, is " + BHAVA_STR

VIEWS10 = ["The world is eternal", "The world is not eternal", "The world has an end", "The world has no end",
           "The soul and the body are the same", "The soul is one thing and the body another",
           "The Tathāgata exists after death", "The Tathāgata does not exist after death",
           "The Tathāgata both exists and does not exist after death",
           "The Tathāgata neither exists nor does not exist after death"]
VIEWS10_STR = " or ".join(f'"{v}"' for v in VIEWS10)
IDAM10_STR = ", or ".join(f'"{v}; only this is true, anything else is false"' for v in VIEWS10)

MANA_BODY = ('Conceit that "I am better", conceit that "I am equal", conceit that "I am inferior". '
             "Whatever conceit of this kind there is, conceiving, the state of having conceived, loftiness, "
             "haughtiness [variant: uṇṇati uṇṇāmo (Syā.)], flag-raising, self-exaltation, "
             "the mind's wish to fly its banner")
ISSA_BODY = ("Whatever envy there is at others' gain, honour, respect, reverence, salutation and veneration, "
             "envying, the state of envying, jealousy, being jealous, the state of jealousy "
             "[variant: ussuyā ussuyanā ussuyitattaṃ (Ka.)]")
MACCH_BODY = (f"The five kinds of stinginess {D} stinginess about dwellings, stinginess about families, "
              "stinginess about gain, stinginess about praise, stinginess about the Teaching. Whatever stinginess "
              "of this kind there is, being stingy, the state of being stingy, meanness, miserliness, "
              "tight-fistedness, the mind's tightness")


def T(x, body, close=None, pron="this"):
    """Tattha katamo X? <body> – ayaṃ vuccati X."""
    return f"Therein, what is {x}? {body} {D} {pron} is called {close or x}."


def TPE(x):
    """Tattha katamā X…pe… ayaṃ vuccati X."""
    return f"Therein, what is {x} … this is called {x}."


# ---------------------------------------------------------------- 4-01 ---------------
def bhumi(name, keys, excl):
    """name: 'of pleasant feeling' / 'with applied thought ...'"""
    s = f"In the plane {name}, {whether(keys)}"
    return s + (f", except for {excl}" if excl else "")


def kenaci_seg(pali):
    sense = {"cakkhu": "eye", "sota": "ear", "ghāna": "nose", "jivhā": "tongue", "kāya": "body"}
    pairs = re.findall(r"Ye te dhammā (\w+?)viññeyyā,? na te dhammā (\w+?)viññeyyā", pali)
    assert len(pairs) == 20, len(pairs)
    sents = []
    for a, b in pairs:
        A, B = sense[a], sense[b]
        sents.append(f"The states that {A}-consciousness can know are not states that {B}-consciousness can know; "
                     f"and the states that {B}-consciousness can know are not states that {A}-consciousness can know.")
    a, b = item("2-13", "a"), item("2-13", "b")
    q = f"What are {lc(a)} and {lc(b)}?"
    return " ".join([q] + sents + [f"These are {lc(a)} and {lc(b)}."])


def both_assoc(pairs, sg, tail):
    """X is both a <sg> and associated with a <sg> through Y, ... – these states ..."""
    return ", ".join(f"{x} is both a {sg} and associated with a {sg} through {y}" for x, y in pairs)


def build_401(pali_text):
    S = {}
    S["1-3-0"] = ["### The Chapter of Summaries"]
    S["1-3-1-0"] = ["#### Summary of the Sets of Three"]
    S["1-985"] = [QA("1-1", "a", f"{ROOTS_K}; {TS4}; {KAMMA}")]
    S["1-986"] = [QA("1-1", "b", f"{ROOTS_A}; {TADEK}; {TS4}; {KAMMA}")]
    S["1-987"] = [QA("1-1", "c", f"{VIPAKA}, {W4}; {KH4}; and {KIRIYA}; {RUPA_ASANKH}")]
    S["1-988"] = [QA("1-2", "a", f"{bhumi('of pleasant feeling', 'krp', 'pleasant feeling')}; {TS3}")]
    S["1-989"] = [QA("1-2", "b", f"{bhumi('of painful feeling', 'k', 'painful feeling')}; {TS3}")]
    neut = "feeling that is neither painful nor pleasant"
    S["1-990"] = [QA("1-2", "c", f"{bhumi('of ' + neut, 'krap', neut)}; {TS3}")]
    S["1-991"] = [QA("1-3", "a", f"{VIPAKA}, {W4}; {KH_PE}")]
    S["1-992"] = [QA("1-3", "b", f"{KUSAKU}, {W4}; {KH_PE}")]
    S["1-993"] = [QA("1-3", "c", f"{KIRIYA[0].upper() + KIRIYA[1:]}, {RUPA_ASANKH}")]
    S["1-994"] = [QA("1-4", "a", f"The results, subject to taints, of wholesome and unwholesome states, {W3}; "
                                  f"{KH_PE}; and whatever material form is {KATATTA}")]
    S["1-995"] = [QA("1-4", "b", f"{KUSAKU} subject to taints, {W3}; {KH_PE}; and {KIRIYA}; "
                                  f"and whatever material form is not {KATATTA}")]
    S["1-996"] = [QA("1-4", "c", MAGGA)]
    S["1-997"] = [QA("1-5", "a", f"{ROOTS_A}; {TADEK}; {TS_PE}; {KAMMA}")]
    S["1-998"] = [QA("1-5", "b", f"Wholesome and indeterminate states subject to taints, {W3}; {KH5}")]
    S["1-999"] = [QA("1-5", "c", MAGGA)]
    vv = "applied thought and sustained thought"
    S["1-1000"] = [QA("1-6", "a", f"{bhumi('with ' + vv, 'krp', vv)}; {TS_PE}")]
    S["1-1001"] = [QA("1-6", "b", f"{bhumi('without applied thought but with sustained thought only', 'rp', 'sustained thought')}; {TS_PE}")]
    S["1-1002"] = [QA("1-6", "c", f"{bhumi('without applied thought and without sustained thought', 'krap', None)}; "
                                   f"{KH_PE}; {RUPA_ASANKH}")]
    S["1-1003"] = [QA("1-7", "a", f"{bhumi('of rapture', 'krp', 'rapture')}; {TS_PE}")]
    S["1-1004"] = [QA("1-7", "b", f"{bhumi('of happiness', 'krp', 'happiness')}; {TS3}")]
    S["1-1005"] = [QA("1-7", "c", f"{bhumi('of equanimity', 'krap', 'equanimity')}; {TS3}")]
    S["1-1006"] = [f"{Q('1-8', 'a')} {THREE_FETTERS}."]
    S["1-1007"] = [T(SAKKAYA, SAKKAYA_BODY)]
    S["1-1008"] = [T(VICI, VICI_INTRO + ". " + VICI_REST[0].upper() + VICI_REST[1:])]
    S["1-1009"] = [T(SILABBATA, SIL_INTRO + "; " + EVA_DITTHI)]
    S["1-1010"] = [f"These three fetters; {TADEK}; {TS_PE}; {KAMMA} {D} {CL('1-8', 'a')}."]
    S["1-1011"] = [QA("1-8", "b", f"The remaining greed, hate, delusion; {TADEK}; {TS_PE}; {KAMMA}")]
    S["1-1012"] = [QA("1-8", "c", f"Wholesome and indeterminate states, {W4}; {KH_PE}; {RUPA_ASANKH}")]
    S["1-1013"] = [f"{Q('1-9', 'a')} {THREE_FETTERS}."]
    S["1-1014"] = [TPE(SAKKAYA)]
    S["1-1015"] = [TPE(VICI)]
    S["1-1016"] = [TPE(SILABBATA)]
    TADEK_CAP = "A" + TADEK[1:]
    S["1-1017"] = [f"These three fetters; {TADEK}; {TS_PE}; {KAMMA} {D} {CL('1-9', 'a')}. "
                   f"{THREE_FETTERS} {D} {CL('1-8', 'a')}. "
                   f"The greed, hate, delusion that occur together with them {D} these are roots to be "
                   f"abandoned by seeing. {TADEK_CAP}; {TS_PE}; {KAMMA} {D} {CL('1-9', 'a')}."]
    S["1-1018"] = [f"{Q('1-9', 'b')} The remaining greed, hate, delusion {D} these are roots to be abandoned "
                   f"by development. {TADEK_CAP}; {TS_PE}; {KAMMA} {D} {CL('1-9', 'b')}."]
    S["1-1019"] = [QA("1-9", "c", f"{TE_THAPETVA}, {W4}; {KH4}; {RUPA_ASANKH}")]
    S["1-1020"] = [QA("1-10", "a", f"{KUSAKU} subject to taints, {W3}; {KH_PE}")]
    S["1-1021"] = [QA("1-10", "b", PATHS4)]
    S["1-1022"] = [QA("1-10", "c", f"{VIPAKA}, {W4}; {KH_PE}; and {KIRIYA}; {RUPA_ASANKH}")]
    S["1-1023"] = [QA("1-11", "a", f"{PATHS4}, and the three lower fruits of the contemplative life")]
    S["1-1024"] = [QA("1-11", "b", "The highest [variant: uparimaṃ (Syā.)] fruit, the fruit of arahantship")]
    S["1-1025"] = [QA("1-11", "c", f"{TE_THAPETVA}, {W3}; {KH_PE}; {RUPA_ASANKH}")]
    S["1-1026"] = [QA("1-12", "a", f"All wholesome, unwholesome and indeterminate states of the sense sphere; {KH_R_PE}")]
    S["1-1027"] = [QA("1-12", "b", f"Wholesome and indeterminate states of the fine-material sphere and of the "
                                    f"immaterial sphere; {KH_PE}")]
    S["1-1028"] = [QA("1-12", "c", MAGGA)]
    S["1-1029"] = [QA("1-13", "a", CITTACET.format("limited states"))]
    S["1-1030"] = [QA("1-13", "b", CITTACET.format("exalted states"))]
    S["1-1031"] = [QA("1-13", "c", CITTACET.format("immeasurable states"))]
    S["1-1032"] = [QA("1-14", "a", f"{ROOTS_A}; {TADEK}; {TS_PE}; {KAMMA}")]
    S["1-1033"] = [QA("1-14", "b", f"Wholesome and indeterminate states subject to taints, {W3}, {KH_R_PE}")]
    S["1-1034"] = [QA("1-14", "c", MAGGA)]
    S["1-1035"] = [QA("1-15", "a", "The five actions with immediate result, and the wrong views that are fixed")]
    S["1-1036"] = [QA("1-15", "b", PATHS4)]
    S["1-1037"] = [QA("1-15", "c", f"{TE_THAPETVA}, {W4}; {KH_PE}; {RUPA_ASANKH}")]
    S["1-1038"] = [QA("1-16", "a", CITTACET.format("the noble path"))]
    sam = "one who possesses the noble path"
    S["1-1039"] = [f"{Q('1-16', 'b')} Except for the path factors in {sam}; {TS_PE} {D} {CL('1-16', 'b')}. "
                   f"In {sam}, right view is both path and root; except for right view, {TS_PE} {D} {CL('1-16', 'b')}. "
                   f"In {sam}, non-greed, non-hate, non-delusion {D} these are roots that belong to the path. "
                   f"The associated aggregate of feeling … aggregate of consciousness {D} {CL('1-16', 'b')}."]
    S["1-1040"] = [f"{Q('1-16', 'c')} The mind and mental factors that arise making the noble path their dominant "
                   f"factor {D} {CL('1-16', 'c')}. In {sam} and develops the path with inquiry as the dominant "
                   f"factor, except for inquiry; {TS_PE} {D} {CL('1-16', 'c')}."]
    NAMES5 = "material form{v}, feeling, perception, mental formations, consciousness"
    POS = ("born, come to be, produced, generated, fully generated, made manifest, arisen, fully arisen, "
           "risen, fully risen")
    NEG = ", ".join("not " + w for w in POS.split(", "))
    S["1-1041"] = [QA("1-17", "a", f"Those states that are {POS}, arisen, and included under the heading "
                                    f'"arisen": ' + NAMES5.format(v=" [variant: rūpā (in many editions)]"))]
    S["1-1042"] = [QA("1-17", "b", f"Those states that are {NEG}, not arisen, and included under the heading "
                                    f'"not arisen": ' + NAMES5.format(v=""))]
    S["1-1043"] = [QA("1-17", "c", f"{VIPAKA} whose results have not yet ripened, {W4}; {KH_PE}; "
                                    f"and whatever material form will arise {KATATTA}")]
    S["1-1044"] = [QA("1-18", "a", "Those states that are past, ceased, gone, changed, ended, completely ended, "
                                    "gone after having arisen, past, and included under the heading \"past\": "
                                    + NAMES5.format(v=""))]
    S["1-1045"] = [QA("1-18", "b", f"Those states that are {NEG}, future, and included under the heading "
                                    f'"future": ' + NAMES5.format(v=""))]
    S["1-1046"] = [QA("1-18", "c", f"Those states that are {POS}, present, and included under the heading "
                                    f'"present": ' + NAMES5.format(v=""))]
    S["1-1047"] = [QA("1-19", "a", CITTACET.format("past states"))]
    S["1-1048"] = [QA("1-19", "b", CITTACET.format("future states"))]
    S["1-1049"] = [QA("1-19", "c", CITTACET.format("present states"))]
    S["1-1050"] = [QA("1-20", "a", "Those states that are within each particular being, personal to it, bound to "
                                    "it, individual to it and produced by past action: " + NAMES5.format(v=""))]
    S["1-1051"] = [QA("1-20", "b", "Those states that are within each particular other being and other person, "
                                    "personal to them, bound to them, individual to them and produced by past "
                                    "action: " + NAMES5.format(v=""))]
    S["1-1052"] = [QA("1-20", "c", "Both of these")]
    S["1-1053"] = [QA("1-21", "a", CITTACET.format("one's own states"))]
    S["1-1054"] = [QA("1-21", "b", CITTACET.format("others' states"))]
    S["1-1055"] = [QA("1-21", "c", CITTACET.format("states both one's own and others'"))]
    S["1-1056"] = [QA("1-22", "a", "The visible-form base")]
    S["1-1057"] = [QA("1-22", "b", ", ".join(BASES[k] for k in
                                             ("cakkh", "sot", "ghān", "jivh", "kāy", "sadd", "gandh", "ras", "phoṭṭhabb"))
                      .replace("the eye base", "The eye base", 1))]
    S["1-1058"] = [QA("1-22", "c", f"{KH4[0].upper() + KH4[1:]}; and {RUPA_DHAY}; and the unconditioned element"),
                   "The sets of three."]
    # ---- pairs: roots
    S["1-3-2-0"] = ["#### Summary of the Pairs"]
    S["1-3-2-1-0"] = [M.GROUPS["1-M-2-1-0"][0]]
    S["1-1059"] = [f"{Q('2-1', 'a')} Three wholesome roots, three unwholesome roots, three indeterminate roots, nine "
                   "roots of the sense sphere, six roots of the fine-material sphere, six roots of the immaterial "
                   "sphere, six roots not included in the spheres of existence."]
    R3K = "the three wholesome roots"
    S["1-1060"] = [f"Therein, what are {R3K}? Non-greed, non-hate, non-delusion."]
    S["1-1061"] = [T(N["alobho"], "Whatever is " + C.S_ALOBHA)]
    S["1-1062"] = [T(N["adoso"], "Whatever is " + S_ADOSA_X)]
    S["1-1063"] = [T(N["amoho"], NANA4[0].upper() + NANA4[1:] + ", " + EVA_PANNA), f"These are {R3K}."]
    S["1-1064"] = ["Therein, what are the three unwholesome roots? Greed, hate, delusion."]
    S["1-1065"] = [T("greed", "Whatever is " + LOBHA_V)]
    S["1-1066"] = [T("hate", DOSA_BODY)]
    S["1-1067"] = [T("delusion", ANANA4[0].upper() + ANANA4[1:] + ", " + EVA_MOHA),
                   "These are the three unwholesome roots."]
    R3A = "the three indeterminate roots"
    NGD = "Non-greed, non-hate and non-delusion arising as results of wholesome states"
    S["1-1068"] = [f"Therein, what are {R3A}? {NGD}, or in indeterminate states that are merely functional {D} "
                   f"these are {R3A}."]
    S["1-1069"] = [f"Therein, what are the nine roots of the sense sphere? The three wholesome roots, the three "
                   f"unwholesome roots, the three indeterminate roots {D} these are the nine roots of the sense sphere."]
    for bid, sph in (("1-1070", "of the fine-material sphere"), ("1-1071", "of the immaterial sphere"),
                     ("1-1072", "not included in the spheres of existence")):
        S[bid] = [f"Therein, what are the six roots {sph}? The three wholesome roots, the three indeterminate roots "
                  f"{D} these are the six roots {sph}."]
    S["1-1073"] = S["1-1060"]
    S["1-1074"] = S["1-1061"]
    S["1-1075"] = [T(N["adoso"], "Whatever is " + S_ADOSA_PE)]
    S["1-1076"] = [T(N["amoho"], NANA4[0].upper() + NANA4[1:] + ", " + EVA_PANNA +
                     ", investigation of states as a factor of awakening, a factor of the path, included in the path"),
                   f"These are {R3K}."]
    S["1-1077"] = [f"Therein, what are {R3A}? {NGD} {D} these are {R3A}. These are the six roots not included in "
                   f"the spheres of existence {D} {CL('2-1', 'a')}."]
    S["1-1078"] = [QA("2-1", "b", f"{TE_THAPETVA}, {W4}; {KH_PE}; {RUPA_ASANKH}")]
    REL = "The states that, in relation to those states, {}"
    AMONG = "Among the states that, in relation to those states, {}, except for those states,"
    ASSOC = "The states that are associated with those states"
    DISS = "The states that are dissociated from those states"
    AMONG_ASSOC = "Among the states that are associated with those states, except for those states,"
    S["1-1079"] = [QA("2-2", "a", REL.format("have roots") + f": {KH_PE}")]
    S["1-1080"] = [QA("2-2", "b", REL.format("are without roots") + f": {KH_PE}, {RUPA_ASANKH}")]
    S["1-1081"] = [QA("2-3", "a", f"{ASSOC}: {KH_PE}")]
    S["1-1082"] = [QA("2-3", "b", f"{DISS}: {KH_PE}, {RUPA_ASANKH}")]
    gm = [("greed", "delusion"), ("delusion", "greed"), ("hate", "delusion"), ("delusion", "hate")]
    S["1-1083"] = [QA("2-4", "a", ", ".join(f"{a} is both a root and has a root through {b}" for a, b in gm)
                      .replace("greed", "Greed", 1)
                      + "; non-greed, non-hate, non-delusion are each both roots and have roots through one another")]
    S["1-1084"] = [QA("2-4", "b", AMONG.format("have roots") + f" {KH_PE}")]
    S["1-1085"] = [QA("2-5", "a", ", ".join(f"{a} is both a root and associated with a root through {b}" for a, b in gm)
                      .replace("greed", "Greed", 1)
                      + "; non-greed, non-hate, non-delusion are each both roots and associated with roots "
                        "through one another")]
    S["1-1086"] = [QA("2-5", "b", f"{AMONG_ASSOC} {KH_PE}")]
    S["1-1087"] = [QA("2-6", "a", REL.format("are not roots but have roots") + f": {KH_PE}")]
    S["1-1088"] = [QA("2-6", "b", REL.format("are not roots and are without roots") + f": {KH_PE}, {RUPA_ASANKH}")]
    # ---- short intermediate pairs
    S["1-3-2-2-0"] = [M.GROUPS["1-M-2-2-0"][0]]
    S["1-1089"] = [QA("2-7", "a", f"The five aggregates {D} {KH5}")]
    S["1-1090"] = [QA("2-7", "b", "The unconditioned element")]
    S["1-1091"] = [f"{Q('2-8', 'a')} Whatever states have conditions, those very states are conditioned."]
    S["1-1092"] = [f"{Q('2-8', 'b')} Whatever state is without conditions, that very state is unconditioned."]
    S["1-1093"] = [QA("2-9", "a", "The visible-form base")]
    S["1-1094"] = [QA("2-9", "b", f"The eye base … the touch base, {KH_PE}, {RUPA_DHAY}, and the unconditioned element")]
    S["1-1095"] = [QA("2-10", "a", "The eye base … the touch base")]
    S["1-1096"] = [QA("2-10", "b", f"{KH_PE[0].upper() + KH_PE[1:]}, {RUPA_DHAY}, and the unconditioned element")]
    S["1-1097"] = [QA("2-11", "a", "The four great elements and the material form derived from the four great elements")]
    S["1-1098"] = [QA("2-11", "b", f"{KH_PE[0].upper() + KH_PE[1:]}, and the unconditioned element")]
    S["1-1099"] = [QA("2-12", "a", f"Wholesome, unwholesome and indeterminate states subject to taints, {W3}, {KH_R_PE}")]
    S["1-1100"] = [QA("2-12", "b", MAGGA)]
    S["1-1101"] = [kenaci_seg(pali_text)]
    # ---- taints
    S["1-3-2-3-0"] = [M.GROUPS["1-M-2-3-0"][0]]
    S["1-1102"] = [f"{Q('2-14', 'a')} The four taints {D} {KAMASAVA}, {BHAVASAVA}, {DITTHASAVA}, {AVIJJASAVA}."]
    S["1-1103"] = [T(KAMASAVA, KAMESU)]
    S["1-1104"] = [T(BHAVASAVA, BHAVESU.format(v=" [variant: bhavacchando (Sī., Syā.)]"))]
    S["1-1105"] = [T(DITTHASAVA, VIEWS10_STR + "; " + EVA_DITTHI) + " All wrong view is the taint of views."]
    S["1-1106"] = [T(AVIJJASAVA, ANANA4[0].upper() + ANANA4[1:] + "; " + EVA_MOHA), "These states are taints."]

    def group(first, mid0, plural, sg, oth, both_body, very):
        """first: block number of 'no X' item; mid0: matrix pair number of 'X' item."""
        m = lambda i: f"2-{mid0 + i}"
        b = lambda i: f"1-{first + i}"
        S[b(0)] = [QA(m(0), "b", f"{TE_THAPETVA}, {W4}; {KH_PE}; {RUPA_ASANKH}")]
        sas = " subject to taints" if very else ""  # Pāli 'Sāsavā' opens ^1130 / ^1146, not ^1108
        S[b(1)] = [QA(m(1), "a", f"Wholesome, unwholesome and indeterminate states{sas}, {W3}; {KH_R_PE}")]
        S[b(2)] = [QA(m(1), "b", MAGGA)]
        S[b(3)] = [QA(m(2), "a", f"{ASSOC}: {KH_PE}")]
        S[b(4)] = [QA(m(2), "b", f"{DISS}: {KH_PE}; {RUPA_ASANKH}")]
        S[b(5)] = [f"{Q(m(3), 'a')} Those same {plural} are {lc(item(m(3), 'a'))}."]
        S[b(6)] = [QA(m(3), "b", AMONG.format(oth) + f" the remaining wholesome, unwholesome and indeterminate "
                                                   f"states subject to taints, {W3}; {KH_R_PE}")]
        S[b(7)] = [QA(m(4), "a", both_body)]
        S[b(8)] = [QA(m(4), "b", f"{AMONG_ASSOC} {KH_PE}")]
        S[b(9)] = [QA(m(5), "a", f"{DISS} and are wholesome, unwholesome and indeterminate states subject to "
                                  f"taints, {W3}, {KH_R_PE}")]
        S[b(10)] = [QA(m(5), "b", MAGGA)]

    av = [(KAMASAVA, AVIJJASAVA), (AVIJJASAVA, KAMASAVA), (BHAVASAVA, AVIJJASAVA), (AVIJJASAVA, BHAVASAVA),
          (DITTHASAVA, AVIJJASAVA), (AVIJJASAVA, DITTHASAVA)]
    group(1107, 14, "taints", "taint", "are subject to taints",
          both_assoc(av, "taint", "")[0].upper() + both_assoc(av, "taint", "")[1:], False)
    S["1-1117"].append("The first recitation section of the chapter of summaries.")
    # ---- fetters
    S["1-3-2-4-0"] = [M.GROUPS["1-M-2-4-0"][0]]
    order = ["kāmarāga", "paṭigha", "māna", "diṭṭhi", "vicikicchā", "sīlabbataparāmāsa", "bhavarāga", "issā",
             "macchariya", "avijjā"]
    S["1-1118"] = [f"{Q('2-20', 'a')} The ten fetters {D} " + ", ".join(SY[k] for k in order) + "."]
    S["1-1119"] = [T(SY["kāmarāga"], KAMESU)]
    S["1-1120"] = [T(SY["paṭigha"], DOSA_BODY)]
    S["1-1121"] = [T(SY["māna"], MANA_BODY)]
    S["1-1122"] = [T(SY["diṭṭhi"], VIEWS10_STR + "; " + EVA_DITTHI) + " Except for "
                   + SY["sīlabbataparāmāsa"] + ", all wrong view is the fetter of views."]
    S["1-1123"] = [T(SY["vicikicchā"], VICI_INTRO + "; " + VICI_REST)]
    S["1-1124"] = [T(SY["sīlabbataparāmāsa"], SIL_INTRO + "; " + EVA_DITTHI)]
    S["1-1125"] = [T(SY["bhavarāga"], BHAVESU.format(v=""))]
    S["1-1126"] = [T(SY["issā"], ISSA_BODY)]
    S["1-1127"] = [T(SY["macchariya"], MACCH_BODY)]
    S["1-1128"] = [T(SY["avijjā"], ANANA4[0].upper() + ANANA4[1:] + "; " + EVA_MOHA), "These states are fetters."]
    fp = []
    for k in order[:-1]:
        fp += [(SY[k], SY["avijjā"]), (SY["avijjā"], SY[k])]
    fb = both_assoc(fp, "fetter", "")
    group(1129, 20, "fetters", "fetter", "are subject to fetters", fb[0].upper() + fb[1:], True)
    # ---- ties
    S["1-3-2-5-0"] = [M.GROUPS["1-M-2-5-0"][0]]
    S["1-1140"] = [f"{Q('2-26', 'a')} The four ties {D} {G_ABH}, {G_BYA}, {G_SIL}, {G_IDAM}."]
    S["1-1141"] = [T(G_ABH, "Whatever is " + LOBHA_PLAIN)]
    S["1-1142"] = [T(G_BYA, DOSA_BODY)]
    S["1-1143"] = [T(G_SIL, SIL_INTRO + "; " + EVA_DITTHI)]
    S["1-1144"] = [T(G_IDAM, IDAM10_STR + "; " + EVA_DITTHI) + f" Except for {G_SIL}, all wrong view is {G_IDAM}.",
                   "These states are ties."]
    gp = [(G_SIL, G_ABH), (G_ABH, G_SIL), (G_IDAM, G_ABH), (G_ABH, G_IDAM)]
    gb = both_assoc(gp, "tie", "")
    group(1145, 26, "ties", "tie", "are subject to ties", gb[0].upper() + gb[1:], True)
    return S


# ---------------------------------------------------------------- 4-03 ---------------
def build_403():
    S = {}
    S["1-3-3-0"] = ["#### Summary of the Discourse Pairs"]
    S["1-1303"] = [QA("2-101", "a", "The states associated with true knowledge")]
    S["1-1304"] = [QA("2-101", "b", "The states associated with ignorance")]
    S["1-1305"] = [QA("2-102", "a", "Wisdom in the three lower noble paths")]
    S["1-1306"] = [QA("2-102", "b", "Wisdom in the highest path, the path of arahantship")]
    ah = "Shamelessness and fearlessness of wrongdoing"
    hi = "Moral shame and fear of wrongdoing"
    S["1-1307"] = [QA("2-103", "a", ah) + " All unwholesome states are foolish."]
    S["1-1308"] = [QA("2-103", "b", hi) + " All wholesome states are wise."]
    S["1-1309"] = [QA("2-104", "a", ah) + " All unwholesome states are dark."]
    S["1-1310"] = [QA("2-104", "b", hi)[:-1] + "? All wholesome states are bright."]  # Pāli "?" (source slip)
    S["1-1311"] = [QA("2-105", "a", "Bodily misconduct, verbal misconduct, mental misconduct")
                   + " All unwholesome states cause torment."]
    S["1-1312"] = [QA("2-105", "b", "Good bodily conduct, good verbal conduct, good mental conduct")
                   + " All wholesome states are states that do not cause torment."]
    NAMING = ("Whatever reckoning, label, designation, usage, name, naming, appellation, expression, term or "
              "utterance there is for each of those states")
    for bid, mid in (("1-1313", "2-106"), ("1-1314", "2-107"), ("1-1315", "2-108")):
        b = item(mid, "b")
        S[bid] = [QA(mid, "a", NAMING) + f" All states {kind(b)[1]}."]
    x = lambda mid, l: lc(item(mid, l))
    S["1-1316"] = [T(x("2-109", "a"), KH4[0].upper() + KH4[1:] + ", and the unconditioned element")]
    S["1-1317"] = [T(x("2-109", "b"), "The four great elements and the material form derived from the four great "
                                      "elements")]
    S["1-1318"] = [T(x("2-110", "a"), MOHA_PE)]
    S["1-1319"] = [T(x("2-110", "b"), "Whatever, with regard to states of existence, is desire for existence … "
                                      "holding on to existence")]
    ev = "whatever view of this kind there is, " + DS_PE
    for bid, mid, l, v in (("1-1320", "2-111", "a", "The self and the world will exist"),
                           ("1-1321", "2-111", "b", "The self and the world will not exist"),
                           ("1-1322", "2-112", "a", "The self and the world are eternal"),
                           ("1-1323", "2-112", "b", "The self and the world will be annihilated"),
                           ("1-1324", "2-113", "a", "The self and the world have an end"),
                           ("1-1325", "2-113", "b", "The self and the world have no end")):
        S[bid] = [T(x(mid, l), f'"{v}", {ev}')]
    S["1-1326"] = [T(x("2-114", "a"), f"Whatever view arises concerning the past, {DS_PE}")]
    S["1-1327"] = [T(x("2-114", "b"), f"Whatever view arises concerning the future, {DS_PE}")]
    neg_hiri = "Not being ashamed of what one should be ashamed of, not being ashamed of engaging in bad, unwholesome states"
    neg_ott = "Not fearing what one should fear, not fearing engaging in bad, unwholesome states"
    S["1-1328"] = [T(x("2-115", "a"), neg_hiri)]
    S["1-1329"] = [T(x("2-115", "b"), neg_ott)]
    S["1-1330"] = [T(x("2-116", "a"), C.S_HIRI[0].upper() + C.S_HIRI[1:])]
    S["1-1331"] = [T(x("2-116", "b"), C.S_OTTAPPA[0].upper() + C.S_OTTAPPA[1:])]
    SPOKEN = "When one is spoken to in accordance with the Teaching, "
    S["1-1332"] = [T(x("2-117", "a"), SPOKEN + "intractability, unruliness, being hard to correct, taking things "
                                      "the opposite way, delight in opposing, disregard, disregarding, disrespect, "
                                      "lack of deference")]
    ASSOC = ("whatever associating with them there is, frequenting them, keeping company with them, resorting to them, "
             "closely resorting to them, devotion to them, close devotion to them, leaning towards them")
    S["1-1333"] = [T(x("2-117", "b"), "Those persons who are without faith, immoral, of little learning, stingy and "
                                      "unwise: " + ASSOC)]
    S["1-1334"] = [T(x("2-118", "a"), SPOKEN + "tractability, compliance, being easy to correct, not taking things "
                                      "the opposite way, not delighting in opposing, respect, regard, regarding, "
                                      "deference")]
    S["1-1335"] = [T(x("2-118", "b"), "Those persons who have faith, are moral, of much learning, generous and "
                                      "wise: " + ASSOC)]
    PPE = ", " + PANNA_PE
    S["1-1336"] = [T(x("2-119", "a"), "The five classes of offences are offences, and the seven classes of "
                                      "offences are offences. Whatever " + x("2-119", "a")
                     + " there is with respect to those offences" + PPE)]
    S["1-1337"] = [T(x("2-119", "b"), "Whatever skill in emerging from those offences there is" + PPE)]
    S["1-1338"] = [T(x("2-120", "a"), "There is meditative attainment " + lc(item("1-6", "a"))[len("states "):]
                     + ", there is meditative attainment " + lc(item("1-6", "b"))[len("states "):]
                     + ", there is meditative attainment " + lc(item("1-6", "c"))[len("states "):]
                     + ". Whatever " + x("2-120", "a") + " there is with respect to those attainments" + PPE)]
    S["1-1339"] = [T(x("2-120", "b"), "Whatever skill in emerging from those attainments there is" + PPE)]
    EL18 = ("the eye element, the visible-form element, the eye-consciousness element, the ear element, "
            "the sound element, the ear-consciousness element, the nose element, the smell element, "
            "the nose-consciousness element, the tongue element, the taste element, the tongue-consciousness element, "
            "the body element, the touch element, the body-consciousness element, the mind element, "
            "the element of mental objects, the mind-consciousness element")
    S["1-1340"] = [T(x("2-121", "a"), "The eighteen elements: " + EL18 + ". Whatever " + x("2-121", "a")
                     + " there is with respect to those elements" + PPE)]
    S["1-1341"] = [T(x("2-121", "b"), "Whatever " + x("2-121", "b") + " there is with respect to those elements" + PPE)]
    B12 = ", ".join(BASES[k] for k in ("cakkh", "rūp", "sot", "sadd", "ghān", "gandh", "jivh", "ras", "kāy",
                                       "phoṭṭhabb", "man", "dhamm"))
    S["1-1342"] = [T(x("2-122", "a"), f"The twelve sense bases {D} {B12}. Whatever " + x("2-122", "a")
                     + " there is with respect to those sense bases" + PPE)]
    PS = ("With ignorance as condition there are mental formations, with mental formations as condition there is "
          "consciousness, with consciousness as condition there are mentality and material form, with mentality "
          "and material form as condition there are the six sense bases, with the six sense bases as condition "
          "there is contact, with contact as condition there is feeling, with feeling as condition there is "
          "craving, with craving as condition there is clinging, with clinging as condition there is existence, "
          "with existence as condition there is birth, with birth as condition ageing and death, sorrow, "
          "lamentation, pain, sadness and despair come to be; thus there is the arising of this whole mass of "
          "suffering. Whatever wisdom there is in this, understanding … non-delusion, investigation of states, "
          "right view")
    S["1-1343"] = [T(x("2-122", "b"), PS)]
    S["1-1344"] = [T(x("2-123", "a"), "Whatever states are roots and conditions of whatever states for their arising "
                                      "[variant: upādāya (Sī., Ka.)], that in each case is what is possible; whatever "
                                      "wisdom there is in this, understanding … non-delusion, investigation of states, "
                                      "right view")]
    S["1-1345"] = [T(x("2-123", "b"), "Whatever states are not roots and not conditions of whatever states for their "
                                      "arising, that in each case is what is impossible; whatever wisdom there is in "
                                      "this, understanding … non-delusion, investigation of states, right view")]
    S["1-1346"] = [T(x("2-124", "a"), "Whatever is straightforwardness, "
                     + C.S_UJUTA[C.S_UJUTA.index("freedom from deviousness"):])]
    S["1-1347"] = [T(x("2-124", "b"), "Whatever is " + C.S_MUDUTA + ", humility of mind")]
    S["1-1348"] = [T(x("2-125", "a"), "Whatever is patience, forbearance, endurance, non-ferocity, non-abusiveness, "
                                      "contentment of mind")]
    NONTR = "non-transgression by body, non-transgression by speech, non-transgression by body and speech"
    TR = "transgression by body, transgression by speech, transgression by body and speech"
    RESTRAINT = "All restraint by morality is {}."
    S["1-1349"] = [T(x("2-125", "b"), "Whatever is " + NONTR) + " " + RESTRAINT.format(x("2-125", "b"))]
    S["1-1350"] = [T(x("2-126", "a"), "Having given up the kind of speech that is rough, harsh, hurtful to others, "
                                      "offensive to others, bordering on anger and not conducive to concentration, "
                                      "one speaks the kind of speech that is blameless, pleasing to the ear, lovable, "
                                      "going to the heart, polite, liked by many and pleasing to many; whatever "
                                      "smooth speech there is in this, courteous speech, non-harsh speech")]
    hosp = x("2-126", "b")
    S["1-1351"] = [T(hosp, f"There are two kinds of {hosp} {D} {hosp} with material things and {hosp} with the "
                           f"Teaching. Here someone is hospitable, through {hosp} with material things or through "
                           f"{hosp} with the Teaching")]

    def senses(neg):
        n = "" if not neg else "not "
        g = ("grasps at its general features and grasps at its details" if neg
             else "does not grasp at its general features and does not grasp at its details")
        act = ("he does not practise its restraint, he does not guard the faculty of {f}, he does not undertake "
               "the restraint of the faculty of {f}") if neg else \
              ("he practises its restraint, he guards the faculty of {f}, he undertakes the restraint of the "
               "faculty of {f}")
        why = ("Since, if he leaves the faculty of {f} unrestrained, bad, unwholesome states of covetousness and "
               "sadness might flow in upon him, ")
        return (f"Here someone, on seeing a visible form with the eye, {g}. " + why.format(f="the eye")
                + act.format(f="the eye") + ". On hearing a sound with the ear … on smelling a smell with the nose … "
                "on tasting a taste with the tongue … on touching a touch with the body … on cognising a mental "
                f"object with the mind, he {g}. " + why.format(f="mind") + act.format(f="mind") + ". ")
    S["1-1352"] = [T(x("2-127", "a"), senses(True) + "Whatever non-guarding, non-protection, non-watching, "
                                                      "non-restraint there is of these six faculties")]
    S["1-1354"] = [T(x("2-128", "a"), senses(False) + "Whatever guarding, protection, watching, restraint there is "
                                                       "of these six faculties")]
    S["1-1353"] = [T(x("2-127", "b"), "Here someone, without reflecting and unwisely, takes food for amusement, for "
                                      "intoxication, for adornment, for beautification. Whatever there is in this of "
                                      "not being content, not knowing moderation and lack of reflection in eating")]
    S["1-1355"] = [T(x("2-128", "b"), f"Here someone, reflecting wisely, takes food {D} not for amusement, not for "
                                      "intoxication, not for adornment, not for beautification, but only for the "
                                      "support and maintenance of this body, for ending discomfort, for assisting the "
                                      'holy life, thinking, "Thus I shall put an end to old feeling and not give rise '
                                      "to new feeling, and I shall have continued life, blamelessness and living at "
                                      'ease." Whatever there is in this of being content, knowing moderation and '
                                      "reflection in eating")]
    S["1-1356"] = [T(x("2-129", "a"), "Whatever is lack of mindfulness, lack of recollection, lack of recall, lack of "
                                      "mindfulness, not remembering, not keeping in mind, floating away, forgetting")]
    S["1-1357"] = [T(x("2-129", "b"), MOHA_PE)]
    S["1-1358"] = [T(x("2-130", "a"), "Whatever is " + C.S_SATI)]
    S["1-1359"] = [T(x("2-130", "b"), "Whatever is " + PANNA_PE)]
    S["1-1360"] = [T(x("2-131", "a"), "Whatever is " + PANNA_PE)]
    S["1-1361"] = [T(x("2-131", "b"), "Whatever is practice, development and repeated practice of wholesome states")
                   + " The seven factors of awakening too are " + x("2-131", "b") + "."]
    SAM_PE = "Whatever is the stability of mind … right concentration"
    VIR_PE = "Whatever is the mental arousing of energy … right effort"
    S["1-1362"] = [T(x("2-132", "a"), SAM_PE)]
    S["1-1363"] = [T(x("2-132", "b"), "Whatever is " + PANNA_PE)]
    S["1-1364"] = [T(x("2-133", "a"), SAM_PE)]
    S["1-1365"] = [T(x("2-133", "b"), VIR_PE)]
    S["1-1366"] = [T(x("2-134", "a"), VIR_PE)]
    S["1-1367"] = [T(x("2-134", "b"), SAM_PE)]
    S["1-1368"] = [T(x("2-135", "a"), "Whatever is " + TR) + " All immorality is " + x("2-135", "a") + "."]
    NIHIL = ('"There is nothing given, there is nothing offered, there is nothing sacrificed, there is no fruit or '
             "result of good and bad actions, there is no this world, there is no other world, there is no mother, "
             "there is no father, there are no beings spontaneously reborn, there are in the world no ascetics and "
             "brahmins who have gone rightly and practise rightly and who, having realised this world and the other "
             'world by their own direct knowledge, make them known"')
    RIGHT = ('"There is what is given, there is what is offered, there is what is sacrificed, there is fruit and '
             "result of good and bad actions, there is this world, there is the other world, there is mother, "
             "there is father, there are beings spontaneously reborn, there are in the world ascetics and brahmins "
             "who have gone rightly and practise rightly and who, having realised this world and the other world "
             'by their own direct knowledge, make them known"')
    S["1-1369"] = [T(x("2-135", "b"), NIHIL + "; whatever view of this kind there is, " + DS_PE)
                   + " All wrong view is " + x("2-135", "b") + "."]
    S["1-1370"] = [T(x("2-136", "a"), "Whatever is " + NONTR) + " " + RESTRAINT.format(x("2-136", "a"))]
    S["1-1371"] = [T(x("2-136", "b"), RIGHT + "; " + EVA_PANNA_PE) + " All right view is " + x("2-136", "b") + "."]
    S["1-1372"] = [T(x("2-137", "a"), "Whatever is " + NONTR) + " " + RESTRAINT.format(x("2-137", "a"))]
    S["1-1373"] = [f"Therein, what is {x('2-137', 'b')}? Knowledge of the ownership of action, knowledge in "
                   "conformity with the truths, the knowledge of one who possesses the path, the knowledge of one "
                   "who possesses the fruit."]

    def cite(mid, l):
        return '"' + item(mid, l) + '"'
    S["1-1374"] = [f"{cite('2-138', 'a')} {D} whatever is {PANNA_PE}."]
    S["1-1375"] = [f"{cite('2-138', 'b')} {D} {lc(VIR_PE)}."]
    S["1-1376"] = [f'"A sense of urgency" {D} fear of birth, fear of ageing, fear of sickness, fear of death. '
                   f'"The things that should stir it" [variant: saṃvejanīyaṃ (Sī.)] {D} birth, ageing, sickness, '
                   f"death."]
    EFF = "generates desire, makes an effort, arouses energy, exerts the mind and strives"
    S["1-1377"] = [f"{cite('2-139', 'b')} {D} here a bhikkhu, for the non-arising of bad, unwholesome states that "
                   f"have not yet arisen, {EFF}; for the abandoning of bad, unwholesome states that have arisen, he "
                   f"{EFF}; for the arising of wholesome states that have not yet arisen, he {EFF}; for the "
                   f"continuance, non-decline, increase, abundance, development and fulfilment of wholesome states "
                   f"that have arisen, he {EFF}."]
    S["1-1378"] = [f"{cite('2-140', 'a')} {D} whatever wish for more there is in one who is not content in the "
                   f"development of wholesome states."]
    S["1-1379"] = [f"{cite('2-140', 'b')} {D} whatever there is, in the development of wholesome states, of acting "
                   "carefully, acting persistently, acting without stopping, not being sluggish, not putting down "
                   "desire, not putting down the burden, practice, development and repeated practice."]
    S["1-1380"] = [f"{cite('2-141', 'a')} {D} the three kinds of true knowledge {D} knowledge of the recollection of "
                   "past lives is true knowledge, knowledge of the passing away and reappearance of beings is true "
                   "knowledge, knowledge of the destruction of the taints is true knowledge."]
    S["1-1381"] = [f"{cite('2-141', 'b')} {D} the two kinds of liberation {D} the release of the mind "
                   "[variant: cittassa ca (Sī., Syā.)], and Nibbāna."]
    S["1-1382"] = [f"{cite('2-142', 'a')} {D} the knowledge of one who possesses the path."]
    S["1-1383"] = [f"{cite('2-142', 'b')} {D} the knowledge of one who possesses the fruit.",
                   "The chapter of summaries is complete."]
    return S


# ---------------------------------------------------------------- assemble -----------
ID = re.compile(r"\s*\^([0-9A-Za-z-]+)\s*$")


def pali_segments(path):
    segs, buf = [], []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        m = ID.search(line)
        if m:
            buf.append(line[:m.start()])
            segs.append((m.group(1), buf))
            buf = []
        else:
            buf.append(line)
    assert not buf
    return segs


def dashes(t):
    return t.count("–") + t.count("—")


def assemble(part, S):
    path = PALI_DIR / part
    out, problems = [], []
    segs = pali_segments(path)
    assert set(S) == {b for b, _ in segs}, (set(S) ^ {b for b, _ in segs})
    for bid, plines in segs:
        elines = S[bid]
        if len(elines) != len(plines):
            problems.append((bid, "lines", len(plines), len(elines)))
        for p, e in zip(plines, elines):
            if dashes(p) != dashes(e):
                problems.append((bid, "dash", dashes(p), dashes(e)))
            if p.count("…pe…") != e.count("…") - e.count("……"):
                problems.append((bid, "pe", p.count("…pe…"), e.count("…")))
            if ("[" in p) != ("[" in e) or p.count("[") != e.count("["):
                problems.append((bid, "variant", p.count("["), e.count("[")))
            if e[0].islower():
                problems.append((bid, "lowercase start"))
            if ":-" in e or "  " in e or "outline" in e.lower():
                problems.append((bid, "bad chars"))
        out.append("\n".join(elines[:-1] + [elines[-1] + f" ^{bid}"]))
    text = "\n\n".join(out) + "\n"
    return text, problems, len(segs)


if __name__ == "__main__":
    p401 = (PALI_DIR / "4-01-nikkhepakandam.md").read_text(encoding="utf-8")
    ok = True
    for part, S in (("4-01-nikkhepakandam.md", build_401(p401)), ("4-03-nikkhepakandam.md", build_403())):
        text, problems, n = assemble(part, S)
        for pr in problems:
            print(part, pr)
        if problems:
            ok = False
        (OUT_DIR / part).write_text(text, encoding="utf-8", newline="\n")
        print("wrote", part, "segments", n, "problems", len(problems))
    sys.exit(0 if ok else 1)
