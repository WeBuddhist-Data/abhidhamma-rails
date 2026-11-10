"""Build the English plain zero-shot of pi-1 parts 2-01 (after the approved sample) and 2-02.

usage: python -I -X utf8 build_2-01_2-02.py          (builds both parts, runs the self-test)

Importing this file does NOT build anything. Later parts can load the fixed formulas with
    import importlib.util as u
    s = u.spec_from_file_location("F", r"...\\pi-1-en\\build_2-01_2-02.py"); F = u.module_from_spec(s); s.loader.exec_module(F)
and then use F.translate_line(pali_line) or the constants (KOTTHASA_*, SUNNATA_*, NAMEINFO, STR, PH ...).

Method: every line is translated from the Pāli source by fixed formula strings. The line
translators (Q/A frames, lists of factors, the Koṭṭhāsa/Suññata summaries, the "Katame dhammā
kusalā?" sentences of the absorptions, tails with "ye vā pana …") raise KeyError on any Pāli
they do not know, so nothing is guessed silently. Repeats are byte-identical by construction.
"""
import pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(HERE))
import build_ch2_01_sample as C  # noqa: E402  (importing does not rebuild the sample)

PALI_DIR = ROOT / "AI_translation" / "pali" / "pi-1_split_chapters"
OUT_DIR = ROOT / "AI_translation" / "english" / "pi-1-english-plain-zeroshot_split_chapters"
SAMPLE = HERE / "ch2-01-sample.md"
SAMPLE_PALI = HERE / "ch2-01-pali-1-122.md"

DASH = C.DASH
PE, ELL = "…pe…", "…"
cap = C.cap

# =========================================================================================
# 1. Names (factors and categories). Every X in "What is X at that time?" comes from here.
# =========================================================================================
N = dict(C.NAMES)
N.update({
    "upekkhā": "equanimity",
    "upekkhindriyaṃ": "the faculty of equanimity",
    "vedanākkhandho": "the aggregate of feeling",
    "saññākkhandho": "the aggregate of perception",
    "saṅkhārakkhandho": "the aggregate of mental formations",
    "viññāṇakkhandho": "the aggregate of consciousness",
    "manāyatanaṃ": "the mind base",
    "dhammāyatanaṃ": "the mental-object base",
    "manoviññāṇadhātu": "the mind-consciousness element",
    "dhammadhātu": "the mental-object element",
    "phassāhāro": "the nutriment of contact",
    "manosañcetanāhāro": "the nutriment of mental intention",
    "viññāṇāhāro": "the nutriment of consciousness",
    # provided for the Koṭṭhāsa summaries of later parts (not used in 2-01/2-02)
    "manodhātu": "the mind element",
    "cakkhuviññāṇadhātu": "the eye-consciousness element",
    "kāyaviññāṇadhātu": "the body-consciousness element",
})

# NAMEINFO: pali -> (noun in the summary "there is/are …", noun in Q/A "What is …", plural)
NAMEINFO = {k: (v, v, False) for k, v in N.items()}

# Koṭṭhāsavāra (section on categories): counted groups
KOTTHASA_PLURAL = {
    "cattāro khandhā": "four aggregates",
    "dvāyatanāni": "two sense bases",
    "dve dhātuyo": "two elements",
    "tayo āhārā": "three nutriments",
    "navindriyāni": "nine faculties",
    "aṭṭhindriyāni": "eight faculties",
    "sattindriyāni": "seven faculties",
    "pañcindriyāni": "five faculties",
    "cattāri indriyāni": "four faculties",
    "tīṇindriyāni": "three faculties",
    "satta balāni": "seven powers",
    "cha balāni": "six powers",
    "cattāri balāni": "four powers",
    "tīṇi balāni": "three powers",
    "tayo hetū": "three roots",
    "dve hetū": "two roots",
}
KOTTHASA_FACTORED = {
    "pañcaṅgikaṃ jhānaṃ": "five-factored absorption",
    "caturaṅgikaṃ jhānaṃ": "four-factored absorption",
    "tivaṅgikaṃ jhānaṃ": "three-factored absorption",
    "duvaṅgikaṃ jhānaṃ": "two-factored absorption",
    "aṭṭhaṅgiko maggo": "eight-factored path",
    "pañcaṅgiko maggo": "five-factored path",
    "caturaṅgiko maggo": "four-factored path",
    "tivaṅgiko maggo": "three-factored path",
    "duvaṅgiko maggo": "two-factored path",
}
for k, v in KOTTHASA_PLURAL.items():
    NAMEINFO[k] = (v, "the " + v, True)
for k, v in KOTTHASA_FACTORED.items():
    NAMEINFO[k] = (("an " if v[0] in "aeiou" else "a ") + v, "the " + v, False)
NAMEINFO["eko hetu"] = ("one root", "the one root", False)

# Suññatavāra (section on emptiness): bare group names
SUNNATA_GROUPS = {
    "dhammā": ("states", "the states", True),
    "khandhā": ("aggregates", "the aggregates", True),
    "āyatanāni": ("sense bases", "the sense bases", True),
    "dhātuyo": ("elements", "the elements", True),
    "āhārā": ("nutriments", "the nutriments", True),
    "indriyāni": ("faculties", "the faculties", True),
    "jhānaṃ": ("absorption", "absorption", False),
    "maggo": ("a path", "the path", False),
    "balāni": ("powers", "the powers", True),
    "hetū": ("roots", "the roots", True),
}
NAMEINFO.update(SUNNATA_GROUPS)


def strip_the(s):
    return s[4:] if s.startswith("the ") else s


def info(p):
    """pali name -> (summary noun, Q/A noun, plural). 'eko/ekā/ekaṃ X' = 'one X'."""
    if p in NAMEINFO:
        return NAMEINFO[p]
    m = re.fullmatch(r"(?:eko|ekā|ekaṃ) (\S+)", p)
    if m and m.group(1) in N:
        one = "one " + strip_the(N[m.group(1)])
        return (one, "the " + one, False)
    raise KeyError("name: " + p)


def q_en(p, verb):
    _, q, pl = info(p)
    assert pl == (verb == "honti"), (p, verb)
    return f"What {'are' if pl else 'is'} {q} at that time"


def this_en(p, verb):
    _, q, pl = info(p)
    assert pl == (verb == "honti"), (p, verb)
    return f"{'these are' if pl else 'this is'} {q} at that time"


def there_en(p, verb):
    s, _, pl = info(p)
    assert pl == (verb == "honti"), (p, verb)
    return f"there {'are' if pl else 'is'} {s}"


# =========================================================================================
# 2. Synonym strings (Pāli string = English). The sample's STRINGS plus new ones.
# =========================================================================================
STR = dict(C.STRINGS)
S_UPEKKHA_P = ("cetasikaṃ neva sātaṃ nāsātaṃ cetosamphassajaṃ adukkhamasukhaṃ vedayitaṃ "
               "cetosamphassajā adukkhamasukhā vedanā")
S_UPEKKHA = ("the mental state that is neither comfortable nor uncomfortable, the experience born of mind-contact "
             "that is neither painful nor pleasant, the feeling born of mind-contact that is neither painful "
             "nor pleasant")
STR[S_UPEKKHA_P] = S_UPEKKHA
# abbreviated strings (…pe… inside the string)
STR["paññā pajānanā…pe… amoho dhammavicayo sammādiṭṭhi"] = (
    "wisdom, understanding… non-delusion, investigation of states, right view")

# qualifiers placed before the string: Pāli prefix -> English ', <qualifier>,'
STR_PREFIX = [
    ("tajjāmanoviññāṇadhātusamphassajaṃ ", ", " + C.TAJJA + ","),
    ("tajjāmanoviññāṇadhātusamphassajā ", ", " + C.TAJJA + ","),
    ("vedanākkhandhassa saññākkhandhassa saṅkhārakkhandhassa ", ", " + C.G_KAYA + ","),
    ("viññāṇakkhandhassa ", ", " + C.G_CITTA + ","),
]

# =========================================================================================
# 3. Variant brackets
# =========================================================================================
SIGLA = {"sī.": "Sī.", "syā.": "Syā.", "ka.": "Ka.", "pī.": "Pī.", "kaṃ.": "Kaṃ.", "bahūsu": "in many editions"}


def var_en(br):
    m = re.fullmatch(r"\[(.+?) \(([^)]*)\)\]", br)
    words, sig = m.groups()
    return f"[variant: {words} ({', '.join(SIGLA[s] for s in sig.split())})]"


def vars_in(text):
    return re.sub(r"\[[^\]]*\]", lambda m: var_en(m.group(0)), text)


# =========================================================================================
# 4. Tails: "ye vā pana …", "ayaṃ tasmiṃ samaye X hoti", "ime dhammā kusalā", "…pe…"
# =========================================================================================
YVP_P = "ye vā pana tasmiṃ samaye aññepi atthi paṭiccasamuppannā arūpino dhammā"
YVP_E = "or whatever other dependently arisen immaterial states there are at that time"
assert "or " + C.YEVAPANA == YVP_E + " " + DASH + " these states are wholesome."
THAP_P = "ṭhapetvā vedanākkhandhaṃ ṭhapetvā saññākkhandhaṃ ṭhapetvā viññāṇakkhandhaṃ"
THAP_E = "except the aggregate of feeling, except the aggregate of perception, except the aggregate of consciousness"
THAP_PV = "ṭhapetvā [thapetvā (ka.)] vedanākkhandhaṃ ṭhapetvā saññākkhandhaṃ ṭhapetvā viññāṇakkhandhaṃ"
THAP_EV = THAP_E.replace("except ", "except [variant: thapetvā (Ka.)] ", 1)
KUSALA_P, KUSALA_E = "ime dhammā kusalā", "these states are wholesome"


def tail_tr(t):
    t = t.replace(YVP_P + " " + THAP_PV, YVP_E + ", " + THAP_EV)
    t = t.replace(YVP_P + " " + THAP_P, YVP_E + ", " + THAP_E)
    t = t.replace(YVP_P, YVP_E)
    t = re.sub(r"(?<!\S)(ayaṃ|idaṃ|ime|imāni|imā) tasmiṃ samaye (.+?) (hoti|honti)",
               lambda m: this_en(m.group(2), m.group(3)), t)
    t = t.replace(KUSALA_P, KUSALA_E)
    t = t.replace(PE, ELL)
    return t


# =========================================================================================
# 5. Lists
# =========================================================================================
def there_list(s):
    """'phasso hoti, vedanā hoti…pe… avikkhepo hoti' -> 'there is contact, there is feeling… there is …'"""
    parts = re.split(r"(?:(?<=hoti)|(?<=honti))(…pe…\s*|,\s*|\s+)", s.strip())
    out = []
    for i, p in enumerate(parts):
        if i % 2:
            out.append(p.replace(PE, ELL) if PE in p else ", ")
        else:
            m = re.fullmatch(r"(.+) (hoti|honti)", p)
            out.append(there_en(m.group(1), m.group(2)))
    return "".join(out)


def name_list(s):
    """'Phasso cetanā…pe… avikkhepo' / 'Vedanākkhandho, saññākkhandho' -> English names, comma-separated"""
    parts = re.split(r"(…pe…\s*|,\s*|\s+)", s.strip())
    out = []
    for i, p in enumerate(parts):
        if i % 2:
            out.append(p.replace(PE, ELL) if PE in p else ", ")
        else:
            out.append(info(p[0].lower() + p[1:])[1])
    return "".join(out)


# =========================================================================================
# 6. Q/A frames (Koṭṭhāsavāra, Suññatavāra and every "Katamo tasmiṃ samaye X hoti?" line)
# =========================================================================================
QRE = re.compile(r"Katam(?:o|ā|aṃ|e|āni) tasmiṃ samaye (.+?) (hoti|honti)(\?|…pe…)\s*(.*)$")
ARE = re.compile(r"(?:Yo|Yā|Yaṃ) tasmiṃ samaye (.+?) – ((?:ayaṃ|idaṃ) tasmiṃ samaye .+)$")
JRE = re.compile(r"Yo tesaṃ arūpīnaṃ dhammānaṃ (.+?) – (idaṃ tasmiṃ samaye .+)$")
LRE = re.compile(r"(.+?)(\s–\s.*|;.*|\.)$")


def str_en(s):
    pre = ""
    for p, e in STR_PREFIX:
        if s.startswith(p):
            s, pre = s[len(p):], e
            break
    return pre, STR[s]


def answer_en(a):
    m = ARE.fullmatch(a)
    if m:
        s, rest = m.groups()
        pre, se = str_en(s)
        if s.startswith(("hirīyati", "ottappati")):
            return f"At that time, {se} {DASH} " + tail_tr(rest)
        return f"Whatever at that time{pre} is {se} {DASH} " + tail_tr(rest)
    m = JRE.fullmatch(a)
    if m:
        s, rest = m.groups()
        return f"Whatever, {C.G_JIVITA}, is {STR[s]} {DASH} " + tail_tr(rest)
    m = LRE.fullmatch(a)
    names, rest = m.groups()
    return cap(name_list(names)) + tail_tr(rest)


def qa_en(line):
    m = QRE.fullmatch(line)
    name, verb, mark, rest = m.groups()
    q = q_en(name, verb)
    if mark == "?":
        return q + "? " + answer_en(rest)
    return q + ELL + " " + tail_tr(rest)


# =========================================================================================
# 7. "Katame dhammā kusalā? Yasmiṃ samaye …" sentences: fixed phrase table
# =========================================================================================
ORD = {"paṭhamaṃ": "first", "dutiyaṃ": "second", "tatiyaṃ": "third", "catutthaṃ": "fourth", "pañcamaṃ": "fifth"}
INTROS = [
    ("rūpūpapattiyā maggaṃ bhāveti ",
     "At a time when one develops the path to rebirth in the fine-material sphere and "),
    ("arūpūpapattiyā maggaṃ bhāveti ",
     "At a time when one develops the path to rebirth in the immaterial sphere and "),
    ("kāmāvacaraṃ kusalaṃ cittaṃ uppannaṃ hoti ",
     "At a time when a wholesome mind of the sense sphere has arisen, "),
]
Q_KUSALA = "What states are wholesome?"
assert C.FRAMES["Katame dhammā kusalā?"] == Q_KUSALA

# {V} marks where a variant bracket of that phrase goes (else it goes at the end of the phrase)
J_ENTER = "enters and dwells in the {} absorption{{V}}"
PH = {
    # --- the absorption formulas (full) -------------------------------------------------
    "vivicceva kāmehi vivicca akusalehi dhammehi savitakkaṃ savicāraṃ vivekajaṃ pītisukhaṃ paṭhamaṃ jhānaṃ "
    "upasampajja viharati":
        "quite secluded from sensual pleasures, secluded from unwholesome states, enters and dwells in the "
        "first absorption{V}, which has applied thought and sustained thought, and rapture and happiness born "
        "of seclusion",
    "vitakkavicārānaṃ vūpasamā ajjhattaṃ sampasādanaṃ cetaso ekodibhāvaṃ avitakkaṃ avicāraṃ samādhijaṃ "
    "pītisukhaṃ dutiyaṃ jhānaṃ upasampajja viharati":
        "with the stilling of applied thought and sustained thought, enters and dwells in the second "
        "absorption{V}, which has inner confidence and unification of mind, is without applied thought and "
        "without sustained thought, and has rapture and happiness born of concentration",
    "pītiyā ca virāgā upekkhako ca viharati sato ca sampajāno sukhañca kāyena paṭisaṃvedeti yaṃ taṃ ariyā "
    "ācikkhanti – \"upekkhako satimā sukhavihārī\"ti tatiyaṃ jhānaṃ upasampajja viharati":
        "with the fading away of rapture, dwells equanimous, mindful and clearly aware, experiences happiness "
        "with the body, and enters and dwells in the third absorption{V}, of which the noble ones declare "
        + DASH + " \"Equanimous and mindful, one dwells in happiness\"",
    "sukhassa ca pahānā dukkhassa ca pahānā pubbeva somanassadomanassānaṃ atthaṅgamā adukkhamasukhaṃ "
    "upekkhāsatipārisuddhiṃ catutthaṃ jhānaṃ upasampajja viharati":
        "with the abandoning of pleasure and the abandoning of pain, and with the earlier disappearance of joy "
        "and sadness, enters and dwells in the fourth absorption{V}, which is neither painful nor pleasant and "
        "has purity of mindfulness due to equanimity",
    "avitakkaṃ vicāramattaṃ samādhijaṃ pītisukhaṃ dutiyaṃ jhānaṃ upasampajja viharati":
        "enters and dwells in the second absorption{V}, which is without applied thought but with sustained "
        "thought only, and has rapture and happiness born of concentration",
    # --- the absorption formulas (opening words only, before …pe…) ---------------------
    "vivicceva kāmehi": "quite secluded from sensual pleasures",
    "vitakkavicārānaṃ vūpasamā": "with the stilling of applied thought and sustained thought",
    "pītiyā ca virāgā": "with the fading away of rapture",
    "sukhassa ca pahānā": "with the abandoning of pleasure",
    # --- modes of progress ---------------------------------------------------------------
    "dukkhapaṭipadaṃ dandhābhiññaṃ": "with painful progress{V} and slow direct knowledge",
    "dukkhapaṭipadaṃ khippābhiññaṃ": "with painful progress{V} and quick direct knowledge",
    "sukhapaṭipadaṃ dandhābhiññaṃ": "with pleasant progress{V} and slow direct knowledge",
    "sukhapaṭipadaṃ khippābhiññaṃ": "with pleasant progress{V} and quick direct knowledge",
    # --- the absorption and its object ----------------------------------------------------
    "parittaṃ parittārammaṇaṃ": "limited and with a limited object",
    "parittaṃ appamāṇārammaṇaṃ": "limited and with an immeasurable object",
    "appamāṇaṃ parittārammaṇaṃ": "immeasurable and with a limited object",
    "appamāṇaṃ appamāṇārammaṇaṃ": "immeasurable and with an immeasurable object",
    # --- meditation devices ----------------------------------------------------------------
    "pathavīkasiṇaṃ": "using earth as the meditation device",
    "āpokasiṇaṃ": "using water as the meditation device",
    "tejokasiṇaṃ": "using fire as the meditation device",
    "vāyokasiṇaṃ": "using air as the meditation device",
    "nīlakasiṇaṃ": "using blue as the meditation device",
    "pītakasiṇaṃ": "using yellow as the meditation device",
    "lohitakasiṇaṃ": "using red as the meditation device",
    "odātakasiṇaṃ": "using white as the meditation device",
    # --- bases of mastery ---------------------------------------------------------------------
    "ajjhattaṃ arūpasaññī bahiddhā rūpāni passati":
        "not perceiving material form in oneself, sees visible forms outside",
    "parittāni": "limited ones",
    "appamāṇāni": "immeasurable ones",
    "suvaṇṇadubbaṇṇāni": "beautiful and ugly",
    "nīlāni nīlavaṇṇāni nīlanidassanāni nīlanibhāsāni": "blue ones, blue in colour, blue in appearance, shining blue",
    "pītāni pītavaṇṇāni pītanidassanāni pītanibhāsāni":
        "yellow ones, yellow in colour, yellow in appearance, shining yellow",
    "lohitakāni lohitakavaṇṇāni lohitakanidassanāni lohitakanibhāsāni":
        "red ones, red in colour, red in appearance, shining red",
    "odātāni odātavaṇṇāni odātanidassanāni odātanibhāsāni":
        "white ones, white in colour, white in appearance, shining white",
    "tāni abhibhuyya jānāmi passāmīti": "and, having mastered them, thinks \"I know, I see\"",
    # --- liberations ------------------------------------------------------------------------------
    "rūpī rūpāni passati": "possessing material form, sees visible forms",
    "subhanti": "with the thought \"beautiful\"",
    # --- divine abidings ------------------------------------------------------------------------
    "mettāsahagataṃ": "accompanied by loving-kindness",
    "karuṇāsahagataṃ": "accompanied by compassion",
    "muditāsahagataṃ": "accompanied by sympathetic joy",
    "upekkhāsahagataṃ": "accompanied by equanimity",
    # --- the unattractive ---------------------------------------------------------------------------
    "uddhumātakasaññāsahagataṃ": "accompanied by the perception of a bloated corpse",
    "vinīlakasaññāsahagataṃ": "accompanied by the perception of a discoloured corpse",
    "vipubbakasaññāsahagataṃ": "accompanied by the perception of a festering corpse",
    "vicchiddakasaññāsahagataṃ": "accompanied by the perception of a corpse cut apart",
    "vikkhāyitakasaññāsahagataṃ": "accompanied by the perception of a gnawed corpse",
    "vikkhittakasaññāsahagataṃ": "accompanied by the perception of a scattered corpse",
    "hatavikkhittakasaññāsahagataṃ": "accompanied by the perception of a hacked and scattered corpse",
    "lohitakasaññāsahagataṃ": "accompanied by the perception of a bleeding corpse",
    "puḷavakasaññāsahagataṃ": "accompanied by the perception of a worm-infested corpse",
    "aṭṭhikasaññāsahagataṃ": "accompanied by the perception of a skeleton",
    # --- the immaterial absorptions ---------------------------------------------------------------
    "sabbaso rūpasaññānaṃ samatikkamā paṭighasaññānaṃ atthaṅgamā nānattasaññānaṃ amanasikārā":
        "by completely passing beyond perceptions of material form, by the disappearance of perceptions of "
        "impact, by not attending to perceptions of diversity",
    "ākāsānañcāyatanasaññāsahagataṃ": "accompanied by the perception of the base of infinite space",
    "sabbaso ākāsānañcāyatanaṃ samatikkamma": "having completely passed beyond the base of infinite space",
    "viññāṇañcāyatanasaññāsahagataṃ": "accompanied by the perception of the base of infinite consciousness",
    "sabbaso viññāṇañcāyatanaṃ samatikkamma": "having completely passed beyond the base of infinite consciousness",
    "ākiñcaññāyatanasaññāsahagataṃ": "accompanied by the perception of the base of nothingness",
    "sabbaso ākiñcaññāyatanaṃ samatikkamma": "having completely passed beyond the base of nothingness",
    "nevasaññānāsaññāyatanasaññāsahagataṃ":
        "accompanied by the perception of the base of neither perception nor non-perception",
    # --- levels and dominant factors --------------------------------------------------------------
    "hīnaṃ": "inferior",
    "majjhimaṃ": "middling",
    "paṇītaṃ": "superior",
    "chandādhipateyyaṃ": "with desire as the dominant factor",
    "vīriyādhipateyyaṃ": "with energy as the dominant factor",
    "cittādhipateyyaṃ": "with mind as the dominant factor",
    "vīmaṃsādhipateyyaṃ": "with inquiry as the dominant factor",
    # --- the eight wholesome minds of the sense sphere ------------------------------------------
    "somanassasahagataṃ ñāṇasampayuttaṃ": "accompanied by joy and associated with knowledge",
    "somanassasahagataṃ ñāṇavippayuttaṃ": "accompanied by joy and dissociated from knowledge",
    "upekkhāsahagataṃ ñāṇasampayuttaṃ": "accompanied by equanimity and associated with knowledge",
    "upekkhāsahagataṃ ñāṇavippayuttaṃ": "accompanied by equanimity and dissociated from knowledge",
    "sasaṅkhārena": "with prompting",
    "rūpārammaṇaṃ vā saddārammaṇaṃ vā gandhārammaṇaṃ vā rasārammaṇaṃ vā phoṭṭhabbārammaṇaṃ vā "
    "dhammārammaṇaṃ vā yaṃ yaṃ vā panārabbha":
        C.FRAMES["rūpārammaṇaṃ vā saddārammaṇaṃ vā gandhārammaṇaṃ vā rasārammaṇaṃ vā phoṭṭhabbārammaṇaṃ vā "
                 "dhammārammaṇaṃ vā yaṃ yaṃ vā panārabbha"],
    "rūpārammaṇaṃ vā": "with a visible form as its object",
    "dhammārammaṇaṃ vā yaṃ yaṃ vā panārabbha":
        "or a mental object as its object, or whatever it takes up as its object",
}
for p, e in ORD.items():
    PH[f"{p} jhānaṃ upasampajja viharati"] = J_ENTER.format(e)
    PH[f"{p} jhānaṃ"] = f"the {e} absorption{{V}}"
assert PH["somanassasahagataṃ ñāṇasampayuttaṃ"] in C.FRAMES[
    "Yasmiṃ samaye kāmāvacaraṃ kusalaṃ cittaṃ uppannaṃ hoti somanassasahagataṃ ñāṇasampayuttaṃ"]
PH_MAX = max(len(k.split()) for k in PH)


def chunk_tr(part):
    words = []
    for t in re.findall(r"\[[^\]]*\]|[^\s\[]+", part):
        if t.startswith("["):
            words[-1][1].append(var_en(t))
        else:
            words.append([t.rstrip(","), []])
    res, i = [], 0
    while i < len(words):
        for L in range(min(PH_MAX, len(words) - i), 0, -1):
            key = " ".join(w for w, _ in words[i:i + L])
            if key in PH:
                break
        else:
            raise KeyError("phrase: " + " ".join(w for w, _ in words[i:]))
        en = PH[key]
        vs = [v for _, vv in words[i:i + L] for v in vv]
        if vs:
            vt = " " + " ".join(vs)
            en = en.replace("{V}", vt) if "{V}" in en else en + vt
        res.append(en.replace("{V}", ""))
        i += L
    return ", ".join(res)


def x_tr(x):
    out = []
    for i, part in enumerate(re.split(r"(\s*…pe…\s*)", x)):
        if i % 2:
            out.append(part.replace(PE, ELL))
        elif part.strip():
            out.append(chunk_tr(part))
    return "".join(out)


def kusala_en(line):
    body = line[len("Katame dhammā kusalā? Yasmiṃ samaye "):]
    for p, e in INTROS:
        if body.startswith(p):
            body, intro = body[len(p):], e
            break
    else:
        raise KeyError("intro: " + body[:60])
    idx = body.index(" tasmiṃ samaye ")
    x, rest = body[:idx].rstrip(), body[idx + len(" tasmiṃ samaye "):]
    if x.endswith(DASH):
        sep, x = " " + DASH, x[:-1].rstrip()
    elif x.endswith(","):
        sep, x = ",", x[:-1]
    else:
        sep = ""  # the Pāli has no punctuation here; kept as written
    m = re.fullmatch(r"(.*? hoti)(…pe… ime dhammā kusalā.*|; ye vā pana.*)", rest)
    return (Q_KUSALA + " " + intro + x_tr(x) + sep + " at that time " + there_list(m.group(1))
            + tail_tr(m.group(2)))


def summary_en(line):
    """'Tasmiṃ kho pana samaye cattāro khandhā honti, …; ye vā pana …' (Koṭṭhāsa / Suññata summaries)"""
    body = line[len("Tasmiṃ kho pana samaye "):]
    items, rest = body.split(";", 1)
    return "Now at that time " + there_list(items) + ";" + tail_tr(rest)


# =========================================================================================
# 8. Headings and closing lines (exact)
# =========================================================================================
EXACT = {
    "##### Koṭṭhāsavāro": "##### The Section on Categories",
    "Koṭṭhāsavāro.": "The section on categories.",
    "##### Suññatavāro": "##### The Section on Emptiness",
    "Suññatavāro.": "The section on emptiness.",
    "Paṭhamaṃ cittaṃ.": "The first type of mind.",
    "Dutiyaṃ cittaṃ.": "The second type of mind.",
    "Tatiyaṃ cittaṃ.": "The third type of mind.",
    "Catutthaṃ cittaṃ.": "The fourth type of mind.",
    "Pañcamaṃ cittaṃ.": "The fifth type of mind.",
    "Chaṭṭhaṃ cittaṃ.": "The sixth type of mind.",
    "Sattamaṃ cittaṃ.": "The seventh type of mind.",
    "Aṭṭhamaṃ cittaṃ.": "The eighth type of mind.",
    "Aṭṭha kāmāvacaramahākusalacittāni.": "The eight great wholesome types of mind of the sense sphere.",
    "Dutiyabhāṇavāro.": "The second recitation section.",
    # 2-02
    "#### Rūpāvacarakusalaṃ": "#### The Wholesome Mind of the Fine-Material Sphere",
    "#### Arūpāvacarakusalaṃ": "#### The Wholesome Mind of the Immaterial Sphere",
    "#### Tebhūmakakusalaṃ": "#### The Wholesome Mind of the Three Planes",
    "##### Kāmāvacarakusalaṃ": "##### The Wholesome Mind of the Sense Sphere",
    "##### Rūpāvacarakusalaṃ": "##### The Wholesome Mind of the Fine-Material Sphere",
    "##### Arūpāvacarakusalaṃ": "##### The Wholesome Mind of the Immaterial Sphere",
    "Kāmāvacarakusalaṃ.": "The wholesome mind of the sense sphere.",
    "Rūpāvacarakusalaṃ.": "The wholesome mind of the fine-material sphere.",
    "Arūpāvacarakusalaṃ.": "The wholesome mind of the immaterial sphere.",
    "##### Catukkanayo": "##### The Fourfold Method",
    "Catukkanayo.": "The fourfold method.",
    "##### Pañcakanayo": "##### The Fivefold Method",
    "Pañcakanayo.": "The fivefold method.",
    "##### Catasso paṭipadā": "##### The Four Modes of Progress",
    "Catasso paṭipadā.": "The four modes of progress.",
    "##### Cattāri ārammaṇāni": "##### The Four Kinds of Object",
    "Cattāri ārammaṇāni.": "The four kinds of object.",
    "##### Dve ārammaṇāni": "##### The Two Kinds of Object",
    "Dve ārammaṇāni.": "The two kinds of object.",
    "##### Soḷasakkhattukaṃ": "##### The Sixteenfold Set",
    "Soḷasakkhattukaṃ.": "The sixteenfold set.",
    "##### Aṭṭhakkhattukaṃ": "##### The Eightfold Set",
    "Aṭṭhakkhattukaṃ.": "The eightfold set.",
    "##### Idampi aṭṭhakkhattukaṃ": "##### This Too Is an Eightfold Set",
    "Idampi aṭṭhakkhattukaṃ.": "This too is an eightfold set.",
    "##### Aparampi aṭṭhakkhattukaṃ": "##### Another Eightfold Set",
    "Aparampi aṭṭhakkhattukaṃ.": "Another eightfold set.",
    "##### Aṭṭhakasiṇaṃ soḷasakkhattukaṃ": "##### The Eight Meditation Devices, Sixteenfold",
    "Aṭṭhakasiṇaṃ soḷasakkhattukaṃ.": "The eight meditation devices, sixteenfold.",
    "##### Abhibhāyatanāni parittāni": "##### The Bases of Mastery over Limited Forms",
    "##### Appamāṇāni": "##### The Bases of Mastery over Immeasurable Forms",
    "Imānipi abhibhāyatanāni soḷasakkhattukāni.": "These bases of mastery too are sixteenfold.",
    "##### Tīṇi vimokkhāni soḷasakkhattukāni": "##### The Three Liberations, Sixteenfold",
    "Imānipi tīṇi vimokkhāni soḷasakkhattukāni.": "These three liberations too are sixteenfold.",
    "##### Cattāri brahmavihārajhānāni soḷasakkhattukāni":
        "##### The Four Absorptions of the Divine Abidings, Sixteenfold",
    "Cattāri brahmavihārajhānāni [brahmavihārajjhānāni (sī. syā.)] soḷasakkhattukāni.":
        "The four absorptions of the divine abidings [variant: brahmavihārajjhānāni (Sī., Syā.)], sixteenfold.",
    "##### Asubhajhānaṃ soḷasakkhattukaṃ": "##### The Absorption on the Unattractive, Sixteenfold",
    "Asubhajhānaṃ [asubhajjhānaṃ (sī. syā.)] soḷasakkhattukaṃ.":
        "The absorption on the unattractive [variant: asubhajjhānaṃ (Sī., Syā.)], sixteenfold.",
    "##### Cattāri arūpajhānāni [arūpajjhānāni (sī. syā.)] soḷasakkhattukāni":
        "##### The Four Immaterial Absorptions [variant: arūpajjhānāni (Sī., Syā.)], Sixteenfold",
    "Cattāri arūpajhānāni soḷasakkhattukāni.": "The four immaterial absorptions, sixteenfold.",
}

# =========================================================================================
# 9. Line dispatch, segments, build
# =========================================================================================
IDRE = re.compile(r"\s*\^([0-9A-Za-z-]+)\s*$")


def translate_line(line):
    if line in EXACT:
        return EXACT[line]
    if line.startswith("Katame dhammā kusalā? Yasmiṃ samaye "):
        return kusala_en(line)
    if line.startswith("Tasmiṃ kho pana samaye "):
        return summary_en(line)
    if QRE.fullmatch(line):
        return qa_en(line)
    if line.startswith("Ye vā pana ") or re.match(r"(Ime|Imāni|Imā|Idaṃ|Ayaṃ) tasmiṃ samaye ", line):
        return cap(tail_tr(line[0].lower() + line[1:]))
    raise KeyError("line: " + line[:80])


PALI_CHARS = set("āīūṃṅñṭḍṇḷ")


def check_no_pali(en):
    bare = re.sub(r"\[variant: [^\]]*\]", "", en)
    bad = PALI_CHARS & set(bare)
    assert not bad, (bad, en[:120])


def segments(text):
    segs, buf = [], []
    for line in text.splitlines():
        if not line.strip():
            continue
        m = IDRE.search(line)
        if m:
            buf.append(line[:m.start()])
            segs.append((m.group(1), buf))
            buf = []
        else:
            buf.append(line)
    assert not buf
    return segs


def render(segs):
    out = []
    for bid, lines in segs:
        en = [cap(translate_line(l)) for l in lines]
        for e in en:
            check_no_pali(e)
        en[-1] += f" ^{bid}"
        out.append("\n".join(en))
    return out


def build_2_01():
    segs = segments((PALI_DIR / "2-01-cittuppadakandam.md").read_text(encoding="utf-8"))
    ids = [b for b, _ in segs]
    k = ids.index("1-57") + 1
    sample = SAMPLE.read_text(encoding="utf-8")
    assert sample.endswith(" ^1-57\n") and sample == C.TEXT
    return sample + "\n" + "\n\n".join(render(segs[k:])) + "\n", len(segs)


def build_2_02():
    segs = segments((PALI_DIR / "2-02-cittuppadakandam.md").read_text(encoding="utf-8"))
    return "\n\n".join(render(segs)) + "\n", len(segs)


def selftest():
    """Run the translators on the sample's Pāli; every line must equal the approved sample, except the
    lines whose strings carry variant brackets (handled by hand in the sample) and ^1-1 / ^1-34 / ^1-33."""
    pal = segments(SAMPLE_PALI.read_text(encoding="utf-8"))
    eng = segments(SAMPLE.read_text(encoding="utf-8"))
    skip = {"1-1-0", "1-1-1-0", "1-1-1-1-0", "1-1", "1-5", "1-13", "1-19", "1-33", "1-34", "1-40", "1-57"}
    ok = bad = 0
    for (b, pl), (b2, el) in zip(pal, eng):
        assert b == b2
        if b in skip:
            continue
        for p, e in zip(pl, el):
            if cap(translate_line(p)) == e:
                ok += 1
            else:
                bad += 1
                print("SELFTEST MISMATCH", b, "\n  got:", cap(translate_line(p)), "\n  exp:", e)
    print(f"selftest: {ok} lines identical to the approved sample, {bad} mismatches")
    return bad == 0


if __name__ == "__main__":
    assert selftest()
    for name, fn in (("2-01-cittuppadakandam.md", build_2_01), ("2-02-cittuppadakandam.md", build_2_02)):
        text, n = fn()
        (OUT_DIR / name).write_text(text, encoding="utf-8", newline="\n")
        print("wrote", OUT_DIR / name, n, "segments")
