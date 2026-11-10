"""Shared fixed strings and the line translator for pi-1 parts 2-03 and 2-04 (English plain zero-shot).

Imported by build_2-03.py and build_2-04.py. Reuses the approved sample constants
(build_ch2_01_sample.py) and adds the formulas these parts need. Every recurring formula is a
fixed constant here, so repeats are byte-identical.
"""
import pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(HERE))
import build_ch2_01_sample as C  # noqa: E402  (importing does not rebuild the sample)

PALI_DIR = ROOT / "AI_translation" / "pali" / "pi-1_split_chapters"
OUT_DIR = ROOT / "AI_translation" / "english" / "pi-1-english-plain-zeroshot_split_chapters"
DASH = C.DASH
PE = "…pe…"
ELL = "…"

# ---- factor names (approved sample + new ones) -----------------------------------------
N = dict(C.NAMES)
NEW_NAMES = {
    "anaññātaññassāmītindriyaṃ": "the faculty of coming to know what is not yet known",
    "aññindriyaṃ": "the faculty of final knowledge",
    "sammāvācā": "right speech",
    "sammākammanto": "right action",
    "sammāājīvo": "right livelihood",
    "micchādiṭṭhi": "wrong view",
    "micchāsaṅkappo": "wrong thought",
    "micchāvāyāmo": "wrong effort",
    "micchāsamādhi": "wrong concentration",
    "ahirikabalaṃ": "the power of shamelessness",
    "anottappabalaṃ": "the power of fearlessness of wrongdoing",
    "lobho": "greed",
    "moho": "delusion",
    "abhijjhā": "covetousness",
    "ahirikaṃ": "shamelessness",
    "anottappaṃ": "fearlessness of wrongdoing",
    "upekkhā": "equanimity",
    "upekkhindriyaṃ": "the faculty of equanimity",
    "dukkhaṃ": "pain",
    "domanassindriyaṃ": "the faculty of sadness",
    "doso": "hate",
    "byāpādo": "ill will",
    "vicikicchā": "doubt",
    "uddhaccaṃ": "restlessness",
    "sukhindriyaṃ": "the faculty of pleasure",
    "saṅkhārakkhandho": "the aggregate of mental formations",
}
for k in NEW_NAMES:
    assert k not in N, k
N.update(NEW_NAMES)

# ---- synonym strings ----------------------------------------------------------------------
MAGGA = "a path factor, included in the path"
UNROOT = "the unwholesome root"
ABY_ROOT = "the indeterminate root"


def strip_end(s, tail):
    assert s.endswith(tail), (s, tail)
    return s[: -len(tail)]


# bases: exact Pāli -> English (the sample strings plus shortened bases and new strings)
BASES = dict(C.STRINGS)
_VIT = "takko vitakko saṅkappo appanā byappanā cetaso abhiniropanā"
_SAM = ("cittassa ṭhiti saṇṭhiti avaṭṭhiti avisāhāro avikkhepo avisāhaṭamānasatā samatho "
        "samādhindriyaṃ samādhibalaṃ")
_VIR = ("cetasiko vīriyārambho nikkamo parakkamo uyyāmo vāyāmo ussāho ussoḷhī thāmo dhiti "
        "asithilaparakkamatā anikkhittachandatā anikkhittadhuratā dhurasampaggāho vīriyaṃ "
        "vīriyindriyaṃ vīriyabalaṃ")
BASES[_VIT] = strip_end(C.S_VITAKKA, ", right thought")
BASES[_SAM] = strip_end(C.S_SAMADHI, ", right concentration")
BASES[_VIR] = strip_end(C.S_VIRIYA, ", right effort")
BASES["cittassa ṭhiti"] = "the stability of mind"
assert C.S_SAMADHI.startswith(BASES["cittassa ṭhiti"] + ",")

S_UPEKKHA = ("the mental state that is neither comfortable nor uncomfortable, the experience born of mind-contact "
             "that is neither painful nor pleasant, the feeling born of mind-contact that is neither "
             "painful nor pleasant")
S_DUKKHA = ("mental discomfort, mental pain, the uncomfortable, painful experience born of mind-contact, "
            "the uncomfortable, painful feeling born of mind-contact")
S_KAYASUKHA = ("bodily comfort, bodily pleasure, the comfortable, pleasant experience born of body-contact, "
               "the comfortable, pleasant feeling born of body-contact")
S_DITTHI = ("view, holding views, the thicket of views, the wilderness of views, the contortion of views, "
            "the vacillation of views, the fetter of views, grasping, fixation, adherence, misapprehension, "
            "a wrong path, a false way, wrongness, a basis for sectarian doctrines, a distorted grasp")
S_DITTHI_V = (S_DITTHI.replace("fixation,", "fixation [variant: paṭiggāho (Sī., Syā.)],")
              + " [variant: vipariyesagāho (Ka.)]")
S_LOBHA = ("greed, being greedy, the state of being greedy, lust, lusting, the state of lusting, "
           "covetousness, greed, " + UNROOT)
S_MOHA = ("lack of knowledge, lack of vision, lack of breakthrough, lack of understanding, lack of awakening, "
          "lack of penetration, failure to take in, failure to fathom, failure to consider, failure to review, "
          "failure to see for oneself, stupidity, foolishness, lack of clear awareness, delusion, deep delusion, "
          "confusion, ignorance, the flood of ignorance, the yoke of ignorance, the underlying tendency to "
          "ignorance, the obsession of ignorance, the bar of ignorance, delusion, " + UNROOT)
S_DOSA = ("hate, hating, the state of hating, malice, being malicious, the state of being malicious, "
          "hostility, antagonism, fierceness, abusiveness, discontent of mind")
S_VICIKICCHA = ("uncertainty, being uncertain, the state of being uncertain, perplexity, doubt, indecision, "
                "a fork in the road, wavering, failure to take a definite stand, hesitation, faltering, "
                "failure to fathom, stiffness of mind, scratching of the mind")
S_UDDHACCA = "restlessness of mind, disquiet, distraction of the mind, agitation of mind"
S_AHIRIKA = ("not being ashamed of what one should be ashamed of, not being ashamed of engaging in bad, "
             "unwholesome states")
S_ANOTTAPPA = "not fearing what one should fear, not fearing engaging in bad, unwholesome states"


def ABST(obj):
    return (f"avoidance of {obj}, abstaining, refraining, abstinence, not doing, not performing, "
            "not committing, not overstepping the boundary, destroying the causeway")


_ABST_PI = "ārati virati paṭivirati veramaṇī akiriyā akaraṇaṃ anajjhāpatti velāanatikkamo setughāto"
_CITTA_PI = "cittaṃ mano mānasaṃ hadayaṃ paṇḍaraṃ mano manāyatanaṃ manindriyaṃ viññāṇaṃ viññāṇakkhandho"
_CITTA_EN = strip_end(C.S_CITTA, ", the corresponding mind-consciousness element")

BASES.update({
    "cetasikaṃ neva sātaṃ nāsātaṃ cetosamphassajaṃ adukkhamasukhaṃ vedayitaṃ cetosamphassajā adukkhamasukhā vedanā":
        S_UPEKKHA,
    "cetasikaṃ asātaṃ cetasikaṃ dukkhaṃ cetosamphassajaṃ asātaṃ dukkhaṃ vedayitaṃ cetosamphassajā asātā dukkhā vedanā":
        S_DUKKHA,
    "kāyikaṃ sātaṃ kāyikaṃ sukhaṃ kāyasamphassajaṃ sātaṃ sukhaṃ vedayitaṃ kāyasamphassajā sātā sukhā vedanā":
        S_KAYASUKHA,
    "diṭṭhi diṭṭhigataṃ diṭṭhigahanaṃ diṭṭhikantāro diṭṭhivisūkāyikaṃ diṭṭhivipphanditaṃ diṭṭhisaṃyojanaṃ "
    "gāho patiṭṭhāho abhiniveso parāmāso kummaggo micchāpatho micchattaṃ titthāyatanaṃ vipariyāsaggāho":
        S_DITTHI,
    "diṭṭhi diṭṭhigataṃ diṭṭhigahanaṃ diṭṭhikantāro diṭṭhivisūkāyikaṃ diṭṭhivipphanditaṃ diṭṭhisaṃyojanaṃ "
    "gāho patiṭṭhāho [paṭiggāho (sī. syā.)] abhiniveso parāmāso kummaggo micchāpatho micchattaṃ titthāyatanaṃ "
    "vipariyāsaggāho [vipariyesagāho (ka.)]":
        S_DITTHI_V,
    "lobho lubbhanā lubbhitattaṃ sārāgo sārajjanā sārajjitattaṃ abhijjhā lobho akusalamūlaṃ": S_LOBHA,
    "aññāṇaṃ adassanaṃ anabhisamayo ananubodho asambodho appaṭivedho asaṃgāhanā apariyogāhanā asamapekkhanā "
    "apaccavekkhanā apaccakkhakammaṃ dummejjhaṃ bālyaṃ asampajaññaṃ moho pamoho sammoho avijjā avijjogho "
    "avijjāyogo avijjānusayo avijjāpariyuṭṭhānaṃ avijjālaṅgī moho akusalamūlaṃ": S_MOHA,
    "doso dussanā dussitattaṃ byāpatti byāpajjanā byāpajjitattaṃ virodho paṭivirodho caṇḍikkaṃ asuropo "
    "anattamanatā cittassa": S_DOSA,
    "kaṅkhā kaṅkhāyanā kaṅkhāyitattaṃ vimati vicikicchā dveḷhakaṃ dvedhāpatho saṃsayo anekaṃsaggāho "
    "āsappanā parisappanā apariyogāhanā thambhitattaṃ cittassa manovilekho": S_VICIKICCHA,
    "cittassa uddhaccaṃ avūpasamo cetaso vikkhepo bhantattaṃ cittassa": S_UDDHACCA,
    "na hirīyati hiriyitabbena na hirīyati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā": S_AHIRIKA,
    "na ottappati ottappitabbena na ottappati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā": S_ANOTTAPPA,
    "catūhi vacīduccaritehi " + _ABST_PI: ABST("the four kinds of verbal misconduct"),
    "tīhi kāyaduccaritehi " + _ABST_PI: ABST("the three kinds of bodily misconduct"),
    "micchāājīvā " + _ABST_PI: ABST("wrong livelihood"),
    _CITTA_PI + " tajjācakkhuviññāṇadhātu": _CITTA_EN + ", the corresponding eye-consciousness element",
    _CITTA_PI + " tajjākāyaviññāṇadhātu": _CITTA_EN + ", the corresponding body-consciousness element",
    _CITTA_PI + " tajjāmanodhātu": _CITTA_EN + ", the corresponding mind element",
})
SHAME_STRINGS = {C.S_HIRI, C.S_OTTAPPA, S_AHIRIKA, S_ANOTTAPPA}

# suffix tokens appended after a base (each becomes one more comma item)
TOKENS = {
    "maggaṅgaṃ maggapariyāpannaṃ": MAGGA,
    "pītisambojjhaṅgo": "the awakening factor of rapture",
    "samādhisambojjhaṅgo": "the awakening factor of concentration",
    "vīriyasambojjhaṅgo": "the awakening factor of energy",
    "satisambojjhaṅgo": "the awakening factor of mindfulness",
    "dhammavicayasambojjhaṅgo": "the awakening factor of investigation of states",
    "passaddhisambojjhaṅgo": "the awakening factor of tranquillity",
    "sammāsaṅkappo": "right thought",
    "micchāsaṅkappo": "wrong thought",
    "sammāsamādhi": "right concentration",
    "micchāsamādhi": "wrong concentration",
    "sammāvāyāmo": "right effort",
    "micchāvāyāmo": "wrong effort",
    "sammāvācā": "right speech",
    "sammākammanto": "right action",
    "sammāājīvo": "right livelihood",
}


def tr_string(pi):
    """Translate a bare synonym string: the longest matching base plus suffix tokens."""
    best = None
    for k in BASES:
        if pi == k or pi.startswith(k + " "):
            if best is None or len(k) > len(best):
                best = k
    if best is None:
        raise KeyError("no base for: " + pi)
    out = [BASES[best]]
    rest = pi[len(best):].strip()
    while rest:
        for t in sorted(TOKENS, key=len, reverse=True):
            if rest == t or rest.startswith(t + " "):
                out.append(TOKENS[t])
                rest = rest[len(t):].strip()
                break
        else:
            raise KeyError(f"unknown token at: {rest!r} (in {pi!r})")
    return ", ".join(out)


# ---- frame qualifiers --------------------------------------------------------------------
def TAJJA_OF(element):
    return f"born of the contact of the corresponding {element}"


assert TAJJA_OF("mind-consciousness element") == C.TAJJA
PREFIXES = [  # (Pāli prefix regex, English qualifier)
    (r"tajjāmanoviññāṇadhātusamphassaj(?:aṃ|ā) ", C.TAJJA),
    (r"tajjācakkhuviññāṇadhātusamphassaj(?:aṃ|ā) ", TAJJA_OF("eye-consciousness element")),
    (r"tajjākāyaviññāṇadhātusamphassaj(?:aṃ|ā) ", TAJJA_OF("body-consciousness element")),
    (r"tajjāmanodhātusamphassaj(?:aṃ|ā) ",TAJJA_OF("mind element")),
    (r"vedanākkhandhassa saññākkhandhassa saṅkhārakkhandhassa ", C.G_KAYA),
    (r"viññāṇakkhandhassa ", C.G_CITTA),
]
G_ANANNATA = ("for the realization of those states not yet known, not yet seen, not yet reached, "
              "not yet discovered and not yet realized")
G_ANNA = "for the realization of those states known, seen, reached, discovered and realized"
P_ANANNATA = "tesaṃ dhammānaṃ anaññātānaṃ adiṭṭhānaṃ appattānaṃ aviditānaṃ asacchikatānaṃ sacchikiriyāya "
P_ANNA = "tesaṃ dhammānaṃ ñātānaṃ diṭṭhānaṃ pattānaṃ viditānaṃ sacchikatānaṃ sacchikiriyāya "

# ---- closing formulas -----------------------------------------------------------------------
KIND = {"kusalā": "wholesome", "akusalā": "unwholesome", "abyākatā": "indeterminate"}


def YEV(kind):
    return ("whatever other dependently arisen immaterial states there are at that time "
            + DASH + " these states are " + KIND[kind] + ".")


assert YEV("kusalā") == C.YEVAPANA
YEV_PI = "ye vā pana tasmiṃ samaye aññepi atthi paṭiccasamuppannā arūpino dhammā – ime dhammā "
EXCEPT = ("except the aggregate of feeling, except the aggregate of perception, "
          "except the aggregate of consciousness")


def tr_tail(t):
    """Tail after '... X hoti' at the end of an answer or list."""
    t = t.replace(" " + PE, PE)
    if t in (".", "?"):
        return t
    if t == PE + ".":
        return ELL + "."
    m = re.fullmatch(r"(;|…pe…) " + re.escape(YEV_PI) + r"(kusalā|akusalā|abyākatā)(\.|…pe…\.)", t)
    if m:
        lead = "; or " if m.group(1) == ";" else ELL + " or "
        s = lead + YEV(m.group(2))
        if m.group(3) != ".":
            s = s[:-1] + ELL + "."
        return s
    m = re.fullmatch(r"…pe… ime dhammā (kusalā|akusalā|abyākatā)\.", t)
    if m:
        return ELL + " these states are " + KIND[m.group(1)] + "."
    raise ValueError("unknown tail: " + repr(t))


# ---- question / answer lines -----------------------------------------------------------------
QA_RX = re.compile(r"Katam(?:o|ā|aṃ) tasmiṃ samaye (\S+) hoti([?.]) Y(?:o|ā|aṃ) (.*?) – (?:ayaṃ|idaṃ) "
                   r"tasmiṃ samaye (\S+) hoti(.*)")


def tr_qa(line):
    m = QA_RX.fullmatch(line)
    if not m:
        return None
    key, qmark, body, key2, tail = m.groups()
    assert key == key2, line
    x = N[key]
    q = f"What is {x} at that time{qmark}"
    if body.startswith("tasmiṃ samaye "):
        body = body[len("tasmiṃ samaye "):]
        pre = ""
        for rx, en in PREFIXES:
            mm = re.match(rx, body)
            if mm:
                body = body[mm.end():]
                pre = ", " + en + ","
                break
        s = tr_string(body)
        if s in SHAME_STRINGS:
            assert not pre
            a = f"At that time, {s} {DASH} this is {x} at that time"
        else:
            a = f"Whatever at that time{pre} is {s} {DASH} this is {x} at that time"
    elif body.startswith("tesaṃ arūpīnaṃ dhammānaṃ "):
        s = tr_string(body[len("tesaṃ arūpīnaṃ dhammānaṃ "):])
        a = f"Whatever, {C.G_JIVITA}, is {s} {DASH} this is {x} at that time"
    elif body.startswith(P_ANANNATA):
        s = tr_string(body[len(P_ANANNATA):])
        a = f"Whatever, {G_ANANNATA}, is {s} {DASH} this is {x} at that time"
    else:
        raise ValueError("unknown answer body: " + body)
    return q + " " + a + tr_tail(tail)


# ---- lists of factors ---------------------------------------------------------------------------
def hoti_list(pali):
    """'phasso hoti, vedanā hoti, ... avikkhepo hoti' -> 'there is contact, there is feeling, ...'."""
    items = pali.split(" hoti, ")
    assert items[-1].endswith(" hoti"), pali
    items[-1] = items[-1][: -len(" hoti")]
    return ", ".join(f"there is {N[k]}" for k in items)


def bare_list(pali):
    """'Phasso cetanā vitakko ...' -> 'Contact, intention, applied thought, ...'."""
    s = ", ".join(N[k[0].lower() + k[1:]] for k in pali.split(" "))
    return s[0].upper() + s[1:]


KOTTHASA_RX = re.compile(r"Katamo tasmiṃ samaye saṅkhārakkhandho hoti\? (.*?); " + re.escape(
    "ye vā pana tasmiṃ samaye aññepi atthi paṭiccasamuppannā arūpino dhammā ṭhapetvā vedanākkhandhaṃ "
    "ṭhapetvā saññākkhandhaṃ ṭhapetvā viññāṇakkhandhaṃ – ayaṃ tasmiṃ samaye saṅkhārakkhandho hoti")
    + r"(.*)")


def tr_kotthasa(line):
    m = KOTTHASA_RX.fullmatch(line)
    if not m:
        return None
    x = N["saṅkhārakkhandho"]
    return (f"What is {x} at that time? {bare_list(m.group(1))}; or whatever other dependently arisen "
            f"immaterial states there are at that time, {EXCEPT} {DASH} this is {x} at that time"
            + tr_tail(m.group(2)))


# ---- 'Tasmiṃ kho pana samaye cattāro khandhā honti, ...' -----------------------------------------
SANGAHA_ITEMS = {
    "cattāro khandhā honti": "there are four aggregates",
    "dvāyatanāni honti": "there are two sense bases",
    "dve dhātuyo honti": "there are two elements",
    "tayo āhārā honti": "there are three nutriments",
    "navindriyāni honti": "there are nine faculties",
    "pañcindriyāni honti": "there are five faculties",
    "cattāri indriyāni honti": "there are four faculties",
    "tīṇindriyāni honti": "there are three faculties",
    "pañcaṅgikaṃ jhānaṃ hoti": "there is a five-factored absorption",
    "caturaṅgikaṃ jhānaṃ hoti": "there is a four-factored absorption",
    "aṭṭhaṅgiko maggo hoti": "there is an eight-factored path",
    "caturaṅgiko maggo hoti": "there is a four-factored path",
    "tivaṅgiko maggo hoti": "there is a three-factored path",
    "duvaṅgiko maggo hoti": "there is a two-factored path",
    "satta balāni honti": "there are seven powers",
    "cattāri balāni honti": "there are four powers",
    "tīṇi balāni honti": "there are three powers",
    "tayo hetū honti": "there are three roots",
    "dve hetū honti": "there are two roots",
    "eko hetu hoti": "there is one root",
    "eko phasso hoti": "there is one contact",
    "ekā vedanā hoti": "there is one feeling",
    "ekā saññā hoti": "there is one perception",
    "ekā cetanā hoti": "there is one intention",
    "ekaṃ cittaṃ hoti": "there is one mind",
    "eko vedanākkhandho hoti": "there is one aggregate of feeling",
    "eko saññākkhandho hoti": "there is one aggregate of perception",
    "eko saṅkhārakkhandho hoti": "there is one aggregate of mental formations",
    "eko viññāṇakkhandho hoti": "there is one aggregate of consciousness",
    "ekaṃ manāyatanaṃ hoti": "there is one mind base",
    "ekaṃ manindriyaṃ hoti": "there is one faculty of mind",
    "ekā manoviññāṇadhātu hoti": "there is one mind-consciousness element",
    "ekā cakkhuviññāṇadhātu hoti": "there is one eye-consciousness element",
    "ekā kāyaviññāṇadhātu hoti": "there is one body-consciousness element",
    "ekā manodhātu hoti": "there is one mind element",
    "ekaṃ dhammāyatanaṃ hoti": "there is one mental-object base",
    "ekā dhammadhātu hoti": "there is one mental-object element",
}
SANGAHA_HEAD_PI = "Tasmiṃ kho pana samaye "
SANGAHA_HEAD = "Now at that time "


def tr_sangaha(line):
    if not line.startswith(SANGAHA_HEAD_PI + "cattāro khandhā honti"):
        return None
    body, tail = line[len(SANGAHA_HEAD_PI):].split("; ", 1)
    parts = []
    for item in body.split(", "):
        parts.append((ELL + " ").join(SANGAHA_ITEMS[x.strip()] for x in item.split(PE)))
    return SANGAHA_HEAD + ", ".join(parts) + tr_tail("; " + tail)


# ---- object strings of the opening sentences -------------------------------------------------------
ARAM_FULL = C.FRAMES["rūpārammaṇaṃ vā saddārammaṇaṃ vā gandhārammaṇaṃ vā rasārammaṇaṃ vā "
                     "phoṭṭhabbārammaṇaṃ vā dhammārammaṇaṃ vā yaṃ yaṃ vā panārabbha"]
ARAM_VISIBLE = "with a visible form as its object"
ARAM_ANY = "or whatever it takes up as its object"
assert ARAM_FULL.startswith(ARAM_VISIBLE + ", ") and ARAM_FULL.endswith(", " + ARAM_ANY)
ARAM_ABBR = f"{ARAM_VISIBLE}{ELL} or a mental object as its object, {ARAM_ANY}"       # rūpa…pe… dhamma
ARAM_ABBR_TOUCH = f"{ARAM_VISIBLE}{ELL} or a touch as its object, {ARAM_ANY}"       # rūpa…pe… phoṭṭhabba
ARAM_ABBR_ANY = f"{ARAM_VISIBLE}{ELL} {ARAM_ANY}"                                    # rūpa…pe… yaṃ yaṃ
PROMPTED = "with prompting"
ABBR_LIST = f"at that time there is contact{ELL} there is non-distraction{ELL} these states are "

# ---- opening sentences: 'Katame dhammā K? Yasmiṃ samaye <clause>, tasmiṃ samaye <rest>' -------------
OPEN_RX = re.compile(r"Katame dhammā (kusalā|akusalā|abyākatā)\? Yasmiṃ samaye (.*?), tasmiṃ samaye (.*)")
PIECES = {
    "ime dhammā kusalā": "these states are wholesome",
    "ime dhammā akusalā": "these states are unwholesome",
    "ime dhammā abyākatā": "these states are indeterminate",
    "alobho abyākatamūlaṃ": f"non-greed, {ABY_ROOT}",
    "adoso abyākatamūlaṃ": f"non-hate, {ABY_ROOT}",
}
assert N["alobho"] == "non-greed" and N["adoso"] == "non-hate"


def tr_rest(rest):
    """The part after 'tasmiṃ samaye' in an opening sentence."""
    if "; " + YEV_PI in rest:
        lst, tail = rest.split("; ", 1)
        return "at that time " + hoti_list(lst) + tr_tail("; " + tail)
    end = "."
    if rest.endswith(PE + "."):
        rest, end = rest[: -len(PE + ".")], ELL + "."
    else:
        assert rest.endswith("."), rest
        rest = rest[:-1]
    out = []
    for p in rest.split(PE):
        p = p.strip()
        if p.endswith(" hoti"):
            out.append("there is " + N[p[: -len(" hoti")]])
        else:
            out.append(PIECES[p])
    return "at that time " + (ELL + " ").join(out) + end


def tr_opening(line, clause_en):
    m = OPEN_RX.fullmatch(line)
    assert m, line
    kind, _clause_pi, rest = m.groups()
    lead = "" if clause_en.startswith(",") else " "
    return f"What states are {KIND[kind]}? At a time when{lead}{clause_en}, " + tr_rest(rest)


def build_part(part, HEAD, CLOSE, OPEN, MANUAL):
    """HEAD/CLOSE: exact Pāli line -> English; OPEN: bid -> clause English (first line of the segment);
    MANUAL: (bid, line index) -> full English line."""
    pali = pali_segments(PALI_DIR / part)
    used = set()
    segs = []
    for bid, lines in pali:
        el = []
        for i, line in enumerate(lines):
            if (bid, i) in MANUAL:
                en = MANUAL[(bid, i)]
                used.add(("M", bid, i))
            elif line in HEAD:
                en = HEAD[line]
            elif line in CLOSE:
                en = CLOSE[line]
            else:
                en = tr_qa(line) or tr_kotthasa(line) or tr_sangaha(line)
                if en is None:
                    assert i == 0 and bid in OPEN, (bid, i, line[:80])
                    en = tr_opening(line, OPEN[bid])
                    used.add(("O", bid))
            el.append(en[0].upper() + en[1:] if not en.startswith("#") else en)
        segs.append((bid, el))
    unused = [k for k in OPEN if ("O", k) not in used] + [k for k in MANUAL if ("M",) + k not in used]
    assert not unused, unused
    text = assemble(segs, pali)
    out = OUT_DIR / part
    out.write_text(text, encoding="utf-8", newline="\n")
    print("wrote", out, len(segs), "segments")
    return text


# ---- verification helpers -----------------------------------------------------------------------
ID_RX = re.compile(r"\s\^([0-9A-Za-z-]+)\s*$")


def pali_segments(path):
    """[(block_id, [lines without the id])] in source order."""
    segs, buf = [], []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        m = ID_RX.search(line)
        if m:
            buf.append(line[: m.start()])
            segs.append((m.group(1), buf))
            buf = []
        else:
            buf.append(line)
    assert not buf, buf
    return segs


def cnt(s):
    return s.count("–") + s.count("—"), s.count("?")


def assemble(segs_en, pali_segs):
    out = []
    for (bid, pl), (bid2, el) in zip(pali_segs, segs_en):
        assert bid == bid2, (bid, bid2)
        assert len(pl) == len(el), (bid, len(pl), len(el))
        for p, e in zip(pl, el):
            assert cnt(p) == cnt(e), (bid, cnt(p), cnt(e), e)
            assert "—" not in e and ":-" not in e and "pe…" not in e, (bid, e)
            assert "outline" not in e.lower(), (bid, e)
            assert not re.search(r"[āīūṃṅñṭḍṇḷ]", re.sub(r"\[variant: [^\]]*\]", "", e)), (bid, e)
        el = list(el)
        el[-1] += f" ^{bid}"
        out.append("\n".join(el))
    assert len(pali_segs) == len(segs_en)
    return "\n\n".join(out) + "\n"
