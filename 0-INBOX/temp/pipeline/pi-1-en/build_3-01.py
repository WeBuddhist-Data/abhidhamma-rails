"""Build the English plain zero-shot of pi-1 part 3-01 (Rūpakaṇḍa: opening statement, matrix, Ekakaniddesa).

usage: python -I -X utf8 build_3-01.py
Sentence-level translation with fixed predicate strings, so every repeat is byte-identical.
The classifying predicates reuse the wording of the matrix items (1-matika.md / en-zeroshot-terms.md),
adapted only from 'States that are X' to 'material form that is X'.
"""
import pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
PART = "3-01-rupakandam.md"
PALI = ROOT / "AI_translation" / "pali" / "pi-1_split_chapters" / PART
OUT = ROOT / "AI_translation" / "english" / "pi-1-english-plain-zeroshot_split_chapters" / PART

DASH = "–"
PE = "…"
RF = "material form"

HEAD = {
    "Rūpakaṇḍaṃ": "The Chapter on Material Form",
    "Uddeso": "The Opening Statement",
    "Mātikā": "The Matrix",
    # same wording as notes-3-02_3-03.md (Catukkaṃ … Ekādasakaṃ, Dukaniddeso, Tikaniddeso)
    "Ekakaṃ": "The Sets of One",
    "Dukaṃ": "The Pairs",
    "Tikaṃ": "The Sets of Three",
    "Catukkaṃ": "The Sets of Four",
    "Pañcakaṃ": "The Set of Five",
    "Chakkaṃ": "The Set of Six",
    "Sattakaṃ": "The Set of Seven",
    "Aṭṭhakaṃ": "The Set of Eight",
    "Navakaṃ": "The Set of Nine",
    "Dasakaṃ": "The Set of Ten",
    "Ekādasakaṃ": "The Set of Eleven",
    "Rūpavibhatti": "The Classification of Material Form",
    "Ekakaniddeso": "The Exposition of the Sets of One",
}
WAYS = {"ekavidhena": "one way", "duvidhena": "two ways", "tividhena": "three ways",
        "catubbidhena": "four ways", "pañcavidhena": "five ways", "chabbidhena": "six ways",
        "sattavidhena": "seven ways", "aṭṭhavidhena": "eight ways", "navavidhena": "nine ways",
        "dasavidhena": "ten ways", "ekādasavidhena": "eleven ways"}
CLOSE = {h + ".": HEAD[h][0] + HEAD[h][1:].lower() + "." for h in HEAD if h not in ("Rūpakaṇḍaṃ", "Uddeso", "Rūpavibhatti")}
CLOSE["Mātikā."] = "The matrix."
for k, v in WAYS.items():
    CLOSE[f"Evaṃ {k} rūpasaṅgaho."] = f"Thus {RF} is classified in {v}."
    CLOSE[f"{k[0].upper() + k[1:]} rūpasaṅgaho –"] = f"{RF[0].upper() + RF[1:]} classified in {v} {DASH}"

# ---- predicates: Pāli -> (relative phrase after 'material form', verb phrase after a subject) ----------
# (wording of the matrix items: Derived states / States produced by past action / Visible states /
#  States that make impact / States arising from mind / Internal states …)
P = {}


def is_pair(pos_pali, neg_pali, pos_en, neg_en):
    """Predicates expressed with 'is': 'that is X' / 'is X'."""
    P[pos_pali] = ("that is " + pos_en, "is " + pos_en)
    P[neg_pali] = ("that is " + neg_en, "is " + neg_en)


is_pair("upādā", "no upādā", "derived", "not derived")
is_pair("upādiṇṇaṃ", "anupādiṇṇaṃ", "produced by past action", "not produced by past action")
is_pair("upādiṇṇupādāniyaṃ", "anupādiṇṇupādāniyaṃ", "produced by past action and subject to clinging",
        "not produced by past action but subject to clinging")
is_pair("sanidassanaṃ", "anidassanaṃ", "visible", "invisible")
P["sappaṭighaṃ"] = ("that makes impact", "makes impact")
P["appaṭighaṃ"] = ("that makes no impact", "makes no impact")
is_pair("indriyaṃ", "na indriyaṃ", "a faculty", "not a faculty")
is_pair("mahābhūtaṃ", "na mahābhūtaṃ", "a great element", "not a great element")
is_pair("viññatti", "na viññatti", "intimation", "not intimation")
P["cittasamuṭṭhānaṃ"] = ("arising from mind", "arises from mind")
P["na cittasamuṭṭhānaṃ"] = ("not arising from mind", "does not arise from mind")
P["cittasahabhu"] = ("existing together with mind", "exists together with mind")
P["na cittasahabhu"] = ("not existing together with mind", "does not exist together with mind")
P["cittānuparivatti"] = ("accompanying mind", "accompanies mind")
P["na cittānuparivatti"] = ("not accompanying mind", "does not accompany mind")
is_pair("ajjhattikaṃ", "bāhiraṃ", "internal", "external")
is_pair("oḷārikaṃ", "sukhumaṃ", "gross", "subtle")
is_pair("dūre", "santike", "far", "near")
SENSE = {"cakkhu": "eye", "sota": "ear", "ghāna": "nose", "jivhā": "tongue", "kāya": "body"}
for s, e in SENSE.items():
    is_pair(f"{s}samphassassa vatthu", f"{s}samphassassa na vatthu", f"a basis for {e}-contact",
            f"not a basis for {e}-contact")
    is_pair(f"{s}viññāṇassa vatthu", f"{s}viññāṇassa na vatthu", f"a basis for {e}-consciousness",
            f"not a basis for {e}-consciousness")
    is_pair(f"{s}samphassassa ārammaṇaṃ", f"{s}samphassassa nārammaṇaṃ", f"an object of {e}-contact",
            f"not an object of {e}-contact")
    is_pair(f"{s}viññāṇassa ārammaṇaṃ", f"{s}viññāṇassa nārammaṇaṃ", f"an object of {e}-consciousness",
            f"not an object of {e}-consciousness")
AYATANA = {"cakkhāyatanaṃ": "the eye base", "sotāyatanaṃ": "the ear base", "ghānāyatanaṃ": "the nose base",
           "jivhāyatanaṃ": "the tongue base", "kāyāyatanaṃ": "the body base",
           "rūpāyatanaṃ": "the visible-form base", "saddāyatanaṃ": "the sound base",
           "gandhāyatanaṃ": "the smell base", "rasāyatanaṃ": "the taste base",
           "phoṭṭhabbāyatanaṃ": "the touch base"}
DHATU = {"cakkhudhātu": "the eye element", "sotadhātu": "the ear element", "ghānadhātu": "the nose element",
         "jivhādhātu": "the tongue element", "kāyadhātu": "the body element",
         "rūpadhātu": "the visible-form element", "saddadhātu": "the sound element",
         "gandhadhātu": "the smell element", "rasadhātu": "the taste element",
         "phoṭṭhabbadhātu": "the touch element",
         "ākāsadhātu": "the space element", "āpodhātu": "the water element",
         "pathavīdhātu": "the earth element", "tejodhātu": "the fire element", "vāyodhātu": "the air element"}
INDRIYA = {"cakkhundriyaṃ": "the faculty of the eye", "sotindriyaṃ": "the faculty of the ear",
           "ghānindriyaṃ": "the faculty of the nose", "jivhindriyaṃ": "the faculty of the tongue",
           "kāyindriyaṃ": "the faculty of the body", "itthindriyaṃ": "the faculty of femininity",
           "purisindriyaṃ": "the faculty of masculinity", "jīvitindriyaṃ": "the faculty of life"}
OTHER = {"kāyaviññatti": "bodily intimation", "vacīviññatti": "verbal intimation",
         "kabaḷīkāro āhāro": "edible food"}
for d in (AYATANA, DHATU, INDRIYA, OTHER):
    for k, v in d.items():
        is_pair(k, "na " + k, v, "not " + v)
RUPASSA = {"lahutā": "lightness", "mudutā": "pliancy", "kammaññatā": "workability", "upacayo": "growth",
           "santati": "continuity", "jaratā": "ageing", "aniccatā": "impermanence"}
for k, v in RUPASSA.items():
    is_pair(f"rūpassa {k}", f"rūpassa na {k}", f"{v} of {RF}", f"not {v} of {RF}")


def rel(p):
    return P[p][0]


def vp(p):
    return P[p][1]


# ---- sentence patterns -----------------------------------------------------------------
RE_ATTHI = re.compile(r"^Atthi rūpaṃ (.+?), atthi rūpaṃ (.+?)\.$")
RE_YAM1 = re.compile(r"^Yaṃ taṃ rūpaṃ (.+?), taṃ (?!atthi )(.+?)\.$")
RE_YAM2 = re.compile(r"^Yaṃ taṃ rūpaṃ (.+?), taṃ atthi (.+?),? atthi (.+?)\.$")


def s_atthi(a, b):
    return f"There is {RF} {rel(a)}; there is {RF} {rel(b)}."


def s_yam1(a, p):
    return f"{RF[0].upper() + RF[1:]} {rel(a)} {vp(p)}."


def s_yam2(a, p, q):
    return f"Of {RF} {rel(a)}, some {vp(p)} and some {vp(q)}."


def chain(items):
    """'X…pe… Y…pe… Z' fragments: English joined with '… '."""
    return (PE + " ").join(items)


# sentences with '…pe…' chains (written out from the fixed strings above)
def contact_chain():
    """for ear-contact … nose-contact … tongue-contact … body-contact"""
    return chain([f"for {SENSE[s]}-contact" for s in ("sota", "ghāna", "jivhā", "kāya")])


def fpc(sense):
    """for feeling born of X-contact … for perception … for intention … for X-consciousness"""
    e = SENSE[sense]
    return chain([f"for feeling born of {e}-contact", "for perception", "for intention",
                  f"for {e}-consciousness"])


def obj_contact_chain():
    return chain([f"of {SENSE[s]}-contact" for s in ("sota", "ghāna", "jivhā", "kāya")])


def obj_fpc(sense):
    e = SENSE[sense]
    return chain([f"of feeling born of {e}-contact", "of perception", "of intention", f"of {e}-consciousness"])


RF_C = RF[0].upper() + RF[1:]
SPECIAL = {}
for s in ("cakkhu", "kāya"):
    e = SENSE[s]
    SPECIAL[f"Atthi rūpaṃ {s}samphassajāya vedanāya…pe… saññāya…pe… cetanāya…pe… {s}viññāṇassa vatthu, "
            f"atthi rūpaṃ {s}viññāṇassa na vatthu."] = \
        f"There is {RF} that is a basis {fpc(s)}; there is {RF} {rel(s + 'viññāṇassa na vatthu')}."
    SPECIAL[f"Atthi rūpaṃ {s}samphassajāya vedanāya…pe… saññāya…pe… cetanāya …pe… {s}viññāṇassa vatthu, "
            f"atthi rūpaṃ {s}viññāṇassa na vatthu."] = \
        f"There is {RF} that is a basis {fpc(s)}; there is {RF} {rel(s + 'viññāṇassa na vatthu')}."
    SPECIAL[f"Atthi rūpaṃ {s}samphassajāya vedanāya…pe… saññāya…pe… cetanāya…pe… {s}viññāṇassa ārammaṇaṃ, "
            f"atthi rūpaṃ {s}viññāṇassa nārammaṇaṃ."] = \
        f"There is {RF} that is an object {obj_fpc(s)}; there is {RF} {rel(s + 'viññāṇassa nārammaṇaṃ')}."
    SPECIAL[f"Yaṃ taṃ rūpaṃ bāhiraṃ, taṃ {s}samphassajāya vedanāya…pe… saññāya…pe… cetanāya…pe… "
            f"{s}viññāṇassa na vatthu."] = \
        f"{RF_C} {rel('bāhiraṃ')} is not a basis {fpc(s)}."
    SPECIAL[f"Yaṃ taṃ rūpaṃ ajjhattikaṃ, taṃ {s}samphassajāya vedanāya…pe… saññāya…pe… cetanāya…pe… "
            f"{s}viññāṇassa nārammaṇaṃ."] = \
        f"{RF_C} {rel('ajjhattikaṃ')} is not an object {obj_fpc(s)}."
SPECIAL.update({
    "Atthi rūpaṃ sotasamphassassa…pe… ghānasamphassassa…pe… jivhāsamphassassa…pe… kāyasamphassassa vatthu, "
    "atthi rūpaṃ kāyasamphassassa na vatthu.":
        f"There is {RF} that is a basis {contact_chain()}; "
        f"there is {RF} {rel('kāyasamphassassa na vatthu')}.",
    "Atthi rūpaṃ sotasamphassassa…pe… ghānasamphassassa…pe… jivhāsamphassassa…pe… kāyasamphassassa ārammaṇaṃ, "
    "atthi rūpaṃ kāyasamphassassa nārammaṇaṃ.":
        f"There is {RF} that is an object {obj_contact_chain()}; there is {RF} {rel('kāyasamphassassa nārammaṇaṃ')}.",
    "Yaṃ taṃ rūpaṃ bāhiraṃ, taṃ sotasamphassassa…pe… ghānasamphassassa…pe… jivhāsamphassassa…pe… "
    "kāyasamphassassa na vatthu.":
        f"{RF_C} {rel('bāhiraṃ')} is not a basis {contact_chain()}.",
    "Yaṃ taṃ rūpaṃ ajjhattikaṃ, taṃ sotasamphassassa…pe… ghānasamphassassa…pe… jivhāsamphassassa…pe… "
    "kāyasamphassassa nārammaṇaṃ.":
        f"{RF_C} {rel('ajjhattikaṃ')} is not an object {obj_contact_chain()}.",
})


def neg_chain(d, keys, prefix_na):
    return chain([("not " if prefix_na else "") + d[k] for k in keys])


SENSE_AY = ["sotāyatanaṃ", "ghānāyatanaṃ", "jivhāyatanaṃ", "kāyāyatanaṃ"]
OBJ_AY = ["saddāyatanaṃ", "gandhāyatanaṃ", "rasāyatanaṃ", "phoṭṭhabbāyatanaṃ"]
SENSE_DH = ["sotadhātu", "ghānadhātu", "jivhādhātu", "kāyadhātu"]
OBJ_DH = ["saddadhātu", "gandhadhātu", "rasadhātu", "phoṭṭhabbadhātu"]
SENSE_IN = ["sotindriyaṃ", "ghānindriyaṃ", "jivhindriyaṃ", "kāyindriyaṃ"]
for keys, d in ((SENSE_AY, AYATANA), (OBJ_AY, AYATANA), (SENSE_DH, DHATU), (OBJ_DH, DHATU),
                (SENSE_IN, INDRIYA)):
    pali_pos = "…pe… ".join(keys)
    pali_neg = "…pe… ".join("na " + k for k in keys)
    last = keys[-1]
    SPECIAL[f"Atthi rūpaṃ {pali_pos}, atthi rūpaṃ na {last}."] = \
        f"There is {RF} that is {neg_chain(d, keys, False)}; there is {RF} {rel('na ' + last)}."
    for who in ("ajjhattikaṃ", "bāhiraṃ"):
        SPECIAL[f"Yaṃ taṃ rūpaṃ {who}, taṃ {pali_neg}."] = f"{RF_C} {rel(who)} is {neg_chain(d, keys, True)}."

# ---- Uddeso, Ekaka lists ---------------------------------------------------------------
UDDESO_P = ("Katame dhammā abyākatā? Kusalākusalānaṃ dhammānaṃ vipākā kāmāvacarā rūpāvacarā arūpāvacarā "
            "apariyāpannā vedanākkhandho saññākkhandho saṅkhārakkhandho viññāṇakkhandho, ye ca dhammā kiriyā "
            "neva kusalā nākusalā na ca kammavipākā, sabbañca rūpaṃ, asaṅkhatā ca dhātu – ime dhammā abyākatā.")
UDDESO_E = ("What states are indeterminate? The results of wholesome and unwholesome states, of the sense sphere, "
            "of the fine-material sphere, of the immaterial sphere, and not included in the spheres of existence: "
            "the aggregate of feeling, the aggregate of perception, the aggregate of mental formations, the aggregate "
            "of consciousness; the states that are functional, neither wholesome nor unwholesome nor results of "
            f"action; all {RF}; and the unconditioned element {DASH} these states are indeterminate.")

# (Pāli in ^1-584, English verb phrase); reuses the matrix wording
EKAKA = [
    ("na hetu", "is not a root"),
    ("ahetukaṃ", "is without roots"),
    ("hetuvippayuttaṃ", "is dissociated from roots"),
    ("sappaccayaṃ", "has conditions"),
    ("saṅkhataṃ", "is conditioned"),
    ("rūpaṃ [rūpiyaṃ (sī.)]", "is material [variant: rūpiyaṃ (Sī.)]"),
    ("lokiyaṃ", "is worldly"),
    ("sāsavaṃ", "is subject to taints"),
    ("saṃyojaniyaṃ", "is subject to fetters"),
    ("ganthaniyaṃ", "is subject to ties"),
    ("oghaniyaṃ", "is subject to floods"),
    ("yoganiyaṃ", "is subject to yokes"),
    ("nīvaraṇiyaṃ", "is subject to hindrances"),
    ("parāmaṭṭhaṃ", "is misapprehended"),
    ("upādāniyaṃ", "is subject to clinging"),
    ("saṃkilesikaṃ", "is subject to defilement"),
    ("abyākataṃ", "is indeterminate"),
    ("anārammaṇaṃ", "is without an object"),
    ("acetasikaṃ", "is not a mental factor"),
    ("cittavippayuttaṃ", "is dissociated from mind"),
    ("nevavipākanavipākadhammadhammaṃ", "neither is a result nor produces results"),
    ("asaṃkiliṭṭhasaṃkilesikaṃ", "is undefiled but subject to defilement"),
    ("na savitakkasavicāraṃ", "is not with applied thought and sustained thought"),
    ("na avitakkavicāramattaṃ", "is not without applied thought but with sustained thought only"),
    ("avitakkaavicāraṃ", "is without applied thought and without sustained thought"),
    ("na pītisahagataṃ", "is not accompanied by rapture"),
    ("na sukhasahagataṃ", "is not accompanied by happiness"),
    ("na upekkhāsahagataṃ", "is not accompanied by equanimity"),
    ("neva dassanena na bhāvanāya pahātabbaṃ", "is to be abandoned neither by seeing nor by development"),
    ("neva dassanena na bhāvanāya pahātabbahetukaṃ",
     "is among the states whose roots are to be abandoned neither by seeing nor by development"),
    ("neva ācayagāmi na apacayagāmi", "leads neither to nor away from accumulation"),
    ("nevasekkhanāsekkhaṃ", "is of one neither in training nor beyond training"),
    ("parittaṃ", "is limited"),
    ("kāmāvacaraṃ", "is of the sense sphere"),
    ("na rūpāvacaraṃ", "is not of the fine-material sphere"),
    ("na arūpāvacaraṃ", "is not of the immaterial sphere"),
    ("pariyāpannaṃ", "is included in the spheres of existence"),
    ("no apariyāpannaṃ", "is not among the states not included in the spheres of existence"),
    ("aniyataṃ", "is not fixed"),
    ("aniyyānikaṃ", "does not lead to liberation"),
    ("uppannaṃ", "is arisen"),
    ("chahi viññāṇehi viññeyyaṃ", "is knowable by the six kinds of consciousness"),
    ("aniccaṃ", "is impermanent"),
    ("jarābhibhūtaṃ", "is overcome by ageing"),
]
EKAKA_HEAD_P = ("Tattha katamaṃ sabbaṃ rūpaṃ? Cattāro ca mahābhūtā, catunnañca mahābhūtānaṃ upādāya rūpaṃ – "
                "idaṃ vuccati sabbaṃ rūpaṃ. ")
EKAKA_HEAD_E = (f"Among these, what is all {RF}? The four great elements and the {RF} derived from the four great "
                f"elements {DASH} this is called all {RF}. ")
EKAKA_P = EKAKA_HEAD_P + "Sabbaṃ rūpaṃ " + ", ".join(p for p, _ in EKAKA) + "."
EKAKA_E = EKAKA_HEAD_E + f"All {RF} " + ", ".join(e for _, e in EKAKA) + "."


def indeed(e):
    return "is indeed " + e[3:] if e.startswith("is ") else "indeed " + e


def meva(p):
    p = re.sub(r" \[.*?\]", "", p)
    if p.endswith("ṃ"):
        return p[:-1] + "meva"
    return p + "meva"


# ^1-594: every item with '-meva'; 'uppannaṃ chahi viññāṇehi viññeyyameva' is one item there (no comma)
NIDDESA = []
for p, e in EKAKA:
    if p == "uppannaṃ":
        continue
    if p == "chahi viññāṇehi viññeyyaṃ":
        NIDDESA.append(("uppannaṃ chahi viññāṇehi viññeyyameva",
                        "is indeed knowable, once arisen, by the six kinds of consciousness"))
        continue
    e2 = re.sub(r" \[variant: .*?\]", "", e)
    NIDDESA.append((meva(p), indeed(e2)))
NIDDESA_P = "Sabbaṃ rūpaṃ " + ", ".join(p for p, _ in NIDDESA) + "."
NIDDESA_E = f"All {RF} " + ", ".join(e for _, e in NIDDESA) + "."

LISTS = {
    "Diṭṭhaṃ sutaṃ mutaṃ viññātaṃ rūpaṃ.": f"{RF_C} that is seen, heard, sensed, cognized.",
    "Pathavīdhātu, āpodhātu, tejodhātu, vāyodhātu, yañca rūpaṃ upādā.":
        f"The earth element, the water element, the fire element, the air element, and the {RF} that is derived.",
    "Cakkhuviññeyyaṃ rūpaṃ, sotaviññeyyaṃ rūpaṃ, ghānaviññeyyaṃ rūpaṃ, jivhāviññeyyaṃ rūpaṃ, kāyaviññeyyaṃ rūpaṃ, "
    "manoviññeyyaṃ rūpaṃ.":
        f"{RF_C} knowable by the eye, {RF} knowable by the ear, {RF} knowable by the nose, {RF} knowable by the "
        f"tongue, {RF} knowable by the body, {RF} knowable by the mind.",
    "Cakkhuviññeyyaṃ rūpaṃ, sotaviññeyyaṃ rūpaṃ, ghānaviññeyyaṃ rūpaṃ, jivhāviññeyyaṃ rūpaṃ, kāyaviññeyyaṃ rūpaṃ, "
    "manodhātuviññeyyaṃ rūpaṃ, manoviññāṇadhātuviññeyyaṃ rūpaṃ.":
        f"{RF_C} knowable by the eye, {RF} knowable by the ear, {RF} knowable by the nose, {RF} knowable by the "
        f"tongue, {RF} knowable by the body, {RF} knowable by the mind element, {RF} knowable by the "
        f"mind-consciousness element.",
    "Cakkhuviññeyyaṃ rūpaṃ, sotaviññeyyaṃ rūpaṃ, ghānaviññeyyaṃ rūpaṃ, jivhāviññeyyaṃ rūpaṃ, kāyaviññeyyaṃ rūpaṃ, "
    "atthi sukhasamphassaṃ, atthi dukkhasamphassaṃ, manodhātuviññeyyaṃ rūpaṃ, manoviññāṇadhātuviññeyyaṃ rūpaṃ.":
        f"{RF_C} knowable by the eye, {RF} knowable by the ear, {RF} knowable by the nose, {RF} knowable by the "
        f"tongue, {RF} knowable by the body, some pleasant to touch, some painful to touch, {RF} knowable "
        f"by the mind element, {RF} knowable by the mind-consciousness element.",
    # the Pāli lacks a comma after jivhindriyaṃ in ^1-591 and ^1-592
    "Cakkhundriyaṃ, sotindriyaṃ, ghānindriyaṃ, jivhindriyaṃ kāyindriyaṃ, itthindriyaṃ, purisindriyaṃ, "
    "jīvitindriyaṃ, yañca rūpaṃ na indriyaṃ.":
        "The faculty of the eye, the faculty of the ear, the faculty of the nose, the faculty of the tongue, "
        "the faculty of the body, the faculty of femininity, the faculty of masculinity, the faculty of life, "
        f"and the {RF} that is not a faculty.",
    "Cakkhundriyaṃ, sotindriyaṃ, ghānindriyaṃ, jivhindriyaṃ kāyindriyaṃ, itthindriyaṃ, purisindriyaṃ, "
    "jīvitindriyaṃ, na indriyaṃ rūpaṃ atthi sappaṭighaṃ, atthi appaṭighaṃ.":
        "The faculty of the eye, the faculty of the ear, the faculty of the nose, the faculty of the tongue, "
        "the faculty of the body, the faculty of femininity, the faculty of masculinity, the faculty of life, "
        f"and {RF} that is not a faculty, of which some makes impact and some makes no impact.",
    "Cakkhāyatanaṃ, sotāyatanaṃ, ghānāyatanaṃ, jivhāyatanaṃ, kāyāyatanaṃ, rūpāyatanaṃ, saddāyatanaṃ, "
    "gandhāyatanaṃ, rasāyatanaṃ, phoṭṭhabbāyatanaṃ, yañca rūpaṃ anidassanaappaṭighaṃ "
    "[anidassanaṃ appaṭighaṃ (sī. syā.)] dhammāyatanapariyāpannaṃ.":
        "The eye base, the ear base, the nose base, the tongue base, the body base, the visible-form base, "
        f"the sound base, the smell base, the taste base, the touch base, and the {RF} that is invisible and "
        "makes no impact [variant: anidassanaṃ appaṭighaṃ (Sī., Syā.)] and is included in the mental-object base.",
}
WHOLE = {UDDESO_P: UDDESO_E, NIDDESA_P: NIDDESA_E, EKAKA_P: EKAKA_E}
WHOLE.update(LISTS)
WHOLE.update(CLOSE)


def tr_sentence(s):
    if s in SPECIAL:
        return SPECIAL[s]
    m = RE_ATTHI.match(s)
    if m:
        return s_atthi(m[1], m[2])
    m = RE_YAM2.match(s)
    if m:
        return s_yam2(m[1], m[2], m[3])
    m = RE_YAM1.match(s)
    if m:
        return s_yam1(m[1], m[2])
    raise KeyError(f"no rule for sentence: {s!r}")


def split_sentences(line):
    """Split at '. ' boundaries that start a new 'Atthi'/'Yaṃ' sentence; keep '…pe…' chains whole."""
    return re.split(r"(?<=\.) (?=(?:Atthi rūpaṃ|Yaṃ taṃ rūpaṃ) )", line)


def tr_line(line):
    if line in WHOLE:
        return WHOLE[line]
    return " ".join(tr_sentence(s) for s in split_sentences(line))


def build():
    out = []
    for line in PALI.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            out.append("")
            continue
        m = re.match(r"^(.*?)(\s*\^[0-9A-Za-z-]+)?$", line)
        body, bid = m.group(1), m.group(2) or ""
        if body.startswith("#"):
            hashes, title = body.split(" ", 1)
            out.append(f"{hashes} {HEAD[title]}{bid}")
        else:
            out.append(tr_line(body) + bid)
    return "\n".join(out).rstrip("\n") + "\n"


if __name__ == "__main__":
    OUT.write_text(build(), encoding="utf-8", newline="\n")
    print("wrote", OUT)
