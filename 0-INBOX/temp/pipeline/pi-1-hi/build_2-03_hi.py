"""Build the Hindi plain zero-shot of pi-1 part 2-03 (the world-transcending wholesome mind, ^1-1-5-0 … ^1-364).

usage: python -I -X utf8 build_2-03_hi.py
Mirrors the English builder (pi-1-en/build_2-03.py + const_2_03_2_04.py): every source line is parsed
and rebuilt from fixed strings, so every repeat is byte-identical. Reuses the approved sample constants
(build_ch2_01_sample_hi.py) and matrix frames (build_matika_hi.py); importing them writes nothing.
New strings are listed in notes-2-03.md.
"""
import pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(HERE))
import build_matika_hi as M  # noqa: E402
import build_ch2_01_sample_hi as C  # noqa: E402

PART = "2-03-cittuppadakandam.md"
PALI = ROOT / "AI_translation" / "pali" / "pi-1_split_chapters" / PART
OUT = ROOT / "AI_translation" / "hindi" / "pi-1-hindi-plain-zeroshot_split_chapters" / PART

DASH, DANDA, ELL, PE = C.DASH, M.DANDA, "…", "…pe…"
KUSALA = C.KUSALA

# ---- factor names (sample + new), with gender for «होता/होती है» -----------------------------
NAMES_G = dict(C.NAMES_G)
NEW_NAMES_G = {
    "anaññātaññassāmītindriyaṃ": ("“जो अब तक नहीं जाना, उसे मैं जान लूँगा” की क्षमता", C.F),  # pi-5 ^5-21
    "aññindriyaṃ": ("पूर्ण ज्ञान की क्षमता", C.F),                                          # pi-5 ^5-21
    "sammāvācā": ("सही वाणी", C.F),                                                         # pi-5 ^5-106
    "sammākammanto": ("सही कर्म", C.M),                                                    # pi-5 ^5-106
    "sammāājīvo": ("सही आजीविका", C.F),                                                    # pi-5 ^5-106
    "saṅkhārakkhandho": ("मानसिक रचनाओं का समूह", C.M),
}
for k in NEW_NAMES_G:
    assert k not in NAMES_G, k
NAMES_G.update(NEW_NAMES_G)
N = {k: v[0] for k, v in NAMES_G.items()}
G = {k: v[1] for k, v in NAMES_G.items()}


def HOTI(key):
    return f"{N[key]} {C.HOTI[G[key]]}"


# ---- synonym strings ------------------------------------------------------------------------
MAGGA = "मार्ग का अंग, मार्ग में समाया हुआ"


def BOJJH(x):
    """'<x>sambojjhaṅgo' (pi-5: satisambojjhaṅgo = सजगता नामक जागृति का अंग)"""
    return f"{x} नामक जागृति का अंग"


_ABST_PI = "ārati virati paṭivirati veramaṇī akiriyā akaraṇaṃ anajjhāpatti velāanatikkamo setughāto"
_ABST_HI = ("से दूर रहना, विरत रहना, पूरी तरह विरत रहना, बचना, न करना, न अपनाना, दोष में न पड़ना, "
            "मर्यादा का उल्लंघन न करना, पुल को तोड़ देना")

BASES = dict(C.STRINGS)
BASES.update({
    "catūhi vacīduccaritehi " + _ABST_PI: "वाणी के चार दुराचरणों " + _ABST_HI,
    "tīhi kāyaduccaritehi " + _ABST_PI: "शरीर के तीन दुराचरणों " + _ABST_HI,
    "micchāājīvā " + _ABST_PI: "ग़लत आजीविका " + _ABST_HI,
})
TOKENS = {
    "maggaṅgaṃ maggapariyāpannaṃ": MAGGA,
    "pītisambojjhaṅgo": BOJJH("उल्लास"),
    "samādhisambojjhaṅgo": BOJJH("एकाग्रता"),
    "vīriyasambojjhaṅgo": BOJJH("उत्साह"),
    "satisambojjhaṅgo": BOJJH("सजगता"),
    "dhammavicayasambojjhaṅgo": BOJJH("परिघटनाओं की छानबीन"),
    "passaddhisambojjhaṅgo": BOJJH("प्रशांति"),
    "sammāvācā": N["sammāvācā"],
    "sammākammanto": N["sammākammanto"],
    "sammāājīvo": N["sammāājīvo"],
}
SHAME = {C.S_HIRI, C.S_OTTAPPA}


def tr_string(pi):
    """Longest matching base, then suffix tokens, each one more comma item."""
    best = max((k for k in BASES if pi == k or pi.startswith(k + " ")), key=len, default=None)
    if best is None:
        raise KeyError("no base for: " + pi)
    out, rest = [BASES[best]], pi[len(best):].strip()
    while rest:
        for t in sorted(TOKENS, key=len, reverse=True):
            if rest == t or rest.startswith(t + " "):
                out.append(TOKENS[t])
                rest = rest[len(t):].strip()
                break
        else:
            raise KeyError(f"unknown token at {rest!r} in {pi!r}")
    return ", ".join(out)


# ---- qualifiers of the answers -----------------------------------------------------------------
PREFIXES = [
    (r"tajjāmanoviññāṇadhātusamphassaj(?:aṃ|ā) ", C.TAJJA),
    (r"vedanākkhandhassa saññākkhandhassa saṅkhārakkhandhassa ", C.G_KAYA),
    (r"viññāṇakkhandhassa ", C.G_CITTA),
]
P_ANANNATA = "tesaṃ dhammānaṃ anaññātānaṃ adiṭṭhānaṃ appattānaṃ aviditānaṃ asacchikatānaṃ sacchikiriyāya "
P_ANNA = "tesaṃ dhammānaṃ ñātānaṃ diṭṭhānaṃ pattānaṃ viditānaṃ sacchikatānaṃ sacchikiriyāya "
G_ANANNATA = ("अब तक न जानी गई, न देखी गई, न पाई गई, न समझी गई और न प्रत्यक्ष अनुभव की गई "
              "उन परिघटनाओं के साक्षात्कार के लिए")
G_ANNA = ("जानी जा चुकी, देखी जा चुकी, पाई जा चुकी, समझी जा चुकी और प्रत्यक्ष अनुभव की जा चुकी "
          "उन परिघटनाओं के साक्षात्कार के लिए")

YEV_PI = "ye vā pana tasmiṃ samaye aññepi atthi paṭiccasamuppannā arūpino dhammā – ime dhammā kusalā"
YEV_HI = "या " + C.YEVAPANA(KUSALA)                     # ends with «।»
END_KUSALA = M.ANSWER(KUSALA)                           # ये हितकर परिघटनाएँ हैं।
assert YEV_HI.endswith(END_KUSALA)


def tr_tail(t):
    if t == ".":
        return DANDA
    if t == "; " + YEV_PI + ".":
        return "; " + YEV_HI
    if t == PE + " ime dhammā kusalā.":
        return ELL + " " + END_KUSALA
    raise ValueError("unknown tail: " + repr(t))


QA_RX = re.compile(r"Katam(?:o|ā|aṃ) tasmiṃ samaye (\S+) hoti([?.]) Y(?:o|ā|aṃ) (.*?) – (?:ayaṃ|idaṃ) "
                   r"tasmiṃ samaye (\S+) hoti(.*)")


def answer(x, lead, s):
    """'<lead> जो S है – यह उस समय X है' (lead: «उस समय …» or a genitive/purpose phrase)."""
    return f"{lead} जो {s} है {DASH} यह उस समय {x} है"


def tr_qa(line):
    m = QA_RX.fullmatch(line)
    if not m:
        return None
    key, qmark, body, key2, tail = m.groups()
    assert key == key2, line
    x = N[key]
    q = C.Q(x) if qmark == "?" else C.Q(x)[:-1] + DANDA
    if body.startswith("tasmiṃ samaye "):
        body = body[len("tasmiṃ samaye "):]
        lead = "उस समय"
        for rx, hi in PREFIXES:
            mm = re.match(rx, body)
            if mm:
                body, lead = body[mm.end():], f"उस समय {hi}"
                break
        s = tr_string(body)
        if s in SHAME:
            assert lead == "उस समय"
            a = f"उस समय {s} {DASH} यह उस समय {x} है"
        else:
            a = answer(x, lead, s)
    elif body.startswith("tesaṃ arūpīnaṃ dhammānaṃ "):
        a = answer(x, C.G_JIVITA, tr_string(body[len("tesaṃ arūpīnaṃ dhammānaṃ "):]))
    elif body.startswith(P_ANANNATA):
        a = answer(x, G_ANANNATA, tr_string(body[len(P_ANANNATA):]))
    else:
        raise ValueError("unknown answer body: " + body)
    return q + " " + a + tr_tail(tail)


# ---- ^1-338: the aggregate of mental formations ---------------------------------------------------
EXCEPT = "अनुभूति के समूह को छोड़कर, पहचान के समूह को छोड़कर, चेतना के समूह को छोड़कर"
KOTTHASA_RX = re.compile(r"Katamo tasmiṃ samaye saṅkhārakkhandho hoti\? (.*?); " + re.escape(
    "ye vā pana tasmiṃ samaye aññepi atthi paṭiccasamuppannā arūpino dhammā ṭhapetvā vedanākkhandhaṃ "
    "ṭhapetvā saññākkhandhaṃ ṭhapetvā viññāṇakkhandhaṃ – ayaṃ tasmiṃ samaye saṅkhārakkhandho hoti") + r"(.*)")


def tr_kotthasa(line):
    m = KOTTHASA_RX.fullmatch(line)
    if not m:
        return None
    x = N["saṅkhārakkhandho"]
    lst = ", ".join(N[k[0].lower() + k[1:]] for k in m.group(1).split(" "))
    return (C.Q(x) + " " + lst + "; या " + C.YEVAPANA_BODY + ", " + EXCEPT
            + f" {DASH} यह उस समय {x} है" + tr_tail(m.group(2)))


# ---- ^1-337: 'Tasmiṃ kho pana samaye cattāro khandhā honti, …' --------------------------------------
SANGAHA = [
    ("cattāro khandhā honti", "चार समूह होते हैं"),
    ("dvāyatanāni honti", "दो इंद्रिय-क्षेत्र होते हैं"),
    ("dve dhātuyo honti", "दो तत्व होते हैं"),
    ("tayo āhārā honti", "तीन आहार होते हैं"),
    ("navindriyāni honti", "नौ क्षमताएँ होती हैं"),
    ("pañcaṅgikaṃ jhānaṃ hoti", "पाँच अंगों वाला ध्यान होता है"),
    ("aṭṭhaṅgiko maggo hoti", "आठ अंगों वाला मार्ग होता है"),
    ("satta balāni honti", "सात बल होते हैं"),
    ("tayo hetū honti", "तीन मूल होते हैं"),
    ("eko phasso hoti", "एक संपर्क होता है"),
    ("ekā vedanā hoti", "एक अनुभूति होती है"),
    ("ekā saññā hoti", "एक पहचान होती है"),
    ("ekā cetanā hoti", "एक इरादा होता है"),
    ("ekaṃ cittaṃ hoti", "एक मन होता है"),
    ("eko vedanākkhandho hoti", "एक अनुभूति का समूह होता है"),
    ("eko saññākkhandho hoti", "एक पहचान का समूह होता है"),
    ("eko saṅkhārakkhandho hoti", "एक मानसिक रचनाओं का समूह होता है"),
    ("eko viññāṇakkhandho hoti", "एक चेतना का समूह होता है"),
    ("ekaṃ manāyatanaṃ hoti", "एक मन का इंद्रिय-क्षेत्र होता है"),
    ("ekaṃ manindriyaṃ hoti", "एक मन की क्षमता होती है"),
    ("ekā manoviññāṇadhātu hoti", "एक मन की चेतना का तत्व होता है"),
    ("ekaṃ dhammāyatanaṃ hoti", "एक मन के विषयों का इंद्रिय-क्षेत्र होता है"),
    ("ekā dhammadhātu hoti", "एक मन के विषयों का तत्व होता है"),
]
SANGAHA_D = dict(SANGAHA)
SANGAHA_HEAD_PI, SANGAHA_HEAD = "Tasmiṃ kho pana samaye ", "और उस समय "


def tr_sangaha(line):
    if not line.startswith(SANGAHA_HEAD_PI):
        return None
    body, tail = line[len(SANGAHA_HEAD_PI):].split("; ", 1)
    hi = SANGAHA_HEAD + ", ".join(SANGAHA_D[x] for x in body.split(", "))
    assert tail == YEV_PI + PE + ".", tail
    return hi + "; " + YEV_HI[:-1] + ELL + DANDA


# ---- headings and closing lines ---------------------------------------------------------------------
PP_HEAD = "प्रगति के ढंग"   # paṭipadā (terms file: Catasso paṭipadā = प्रगति के चार ढंग)
HEAD = {
    "#### Lokuttarakusalaṃ": "#### लोकोत्तर हितकर मन",              # terms file
    "##### Suddhikapaṭipadā": f"##### केवल {PP_HEAD}",
    "##### Suññataṃ": "##### शून्यता",
    "##### Suññatamūlakapaṭipadā": f"##### शून्यता पर आधारित {PP_HEAD}",
    "##### Appaṇihitaṃ": "##### इच्छाओं का अभाव",
    "##### Appaṇihitamūlakapaṭipadā": f"##### इच्छाओं के अभाव पर आधारित {PP_HEAD}",
    "##### Vīsati mahānayā": "##### बीस मुख्य विधियाँ",             # terms file
    "##### Adhipati": "##### प्रधानता",                             # terms file
}
CLOSE = {("Suddhikapaṭipadā.", f"केवल {PP_HEAD}"), ("Suññataṃ.", "शून्यता"),
         ("Suññatamūlakapaṭipadā.", f"शून्यता पर आधारित {PP_HEAD}"), ("Appaṇihitaṃ.", "इच्छाओं का अभाव"),
         ("Appaṇihitamūlakapaṭipadā.", f"इच्छाओं के अभाव पर आधारित {PP_HEAD}"),
         ("Vīsati mahānayā.", "बीस मुख्य विधियाँ"), ("Adhipati.", "प्रधानता"),
         ("Paṭhamo maggo.", "पहला मार्ग"), ("Dutiyo maggo.", "दूसरा मार्ग"), ("Tatiyo maggo.", "तीसरा मार्ग"),
         ("Catuttho maggo.", "चौथा मार्ग"), ("Lokuttaraṃ cittaṃ.", "लोकोत्तर मन")}
CLOSE = {p: h + DANDA for p, h in CLOSE}
for p, h in CLOSE.items():  # a closing line repeats its heading's words
    hp = "##### " + p[:-1]
    if hp in HEAD:
        assert HEAD[hp] == "##### " + h[:-1], (p, h)

# ---- opening clauses -------------------------------------------------------------------------------
DEV_JHANA = "कोई लोकोत्तर ध्यान का अभ्यास करता है"
LEADS = ("जो " + M.BARE[("1-M2-97", "क")].replace(" परिघटनाएँ", "").replace("वाली", "वाला") + " और "
         + M.BARE[("1-M1-10", "ख")].replace(" परिघटनाएँ", "").replace("वाली", "वाला") + " है")
assert LEADS == "जो मुक्ति की ओर ले जाने वाला और संचय घटाने की ओर ले जाने वाला है", LEADS
TWENTY = ["मार्ग", "सजगता के आधार", "सही प्रयास", "सिद्धि के आधार", "क्षमता", "बल", "जागृति के अंग",
          "सत्य", "शांति", "परिघटना", "समूह", "इंद्रिय-क्षेत्र", "तत्व", "आहार", "संपर्क", "अनुभूति",
          "पहचान", "इरादे", "मन"]
assert len(TWENTY) == 19
DEV_TWENTY = "कोई " + f"{ELL} ".join(f"लोकोत्तर {o} का अभ्यास करता है" for o in TWENTY)
STAGE = {
    1: "दृष्टियों में फँसने को छोड़ने के लिए, पहले चरण की प्राप्ति के लिए",
    2: "इंद्रिय-सुखों के राग और दुर्भावना को क्षीण करने के लिए, दूसरे चरण की प्राप्ति के लिए",
    3: "इंद्रिय-सुखों के राग और दुर्भावना को पूरी तरह छोड़ने के लिए, तीसरे चरण की प्राप्ति के लिए",
    4: ("सूक्ष्म भौतिक लोक के राग, अभौतिक लोक के राग, अहंकार, बेचैनी और अज्ञान को पूरी तरह छोड़ने के लिए, "
        "चौथे चरण की प्राप्ति के लिए"),
}
# jhāna formulas as in the approved Hindi pi-4 (^4-198: 'इंद्रिय-सुखों से अलग होकर, … पहले ध्यान को
# प्राप्त करके उसमें रहता है; आरंभिक विचार और सतत विचार के शांत होने से दूसरे ध्यान को…')
J1 = f"इंद्रिय-सुखों से अलग होकर{ELL} पहले ध्यान को प्राप्त करके उसमें रहता है"
J5 = (f"आरंभिक विचार और सतत विचार के शांत होने से{ELL} दूसरे ध्यान को{ELL} तीसरे ध्यान को{ELL} "
      f"चौथे ध्यान को{ELL} पहले ध्यान को{ELL} पाँचवें ध्यान को प्राप्त करके उसमें रहता है")
PP = [
    "दुःखद प्रगति और धीमे उच्च ज्ञान वाला",
    "दुःखद प्रगति और शीघ्र उच्च ज्ञान वाला",
    "सुखद प्रगति और धीमे उच्च ज्ञान वाला",
    "सुखद प्रगति और शीघ्र उच्च ज्ञान वाला",
]
EMPTY = "शून्य"
DESIRELESS = "इच्छा-रहित"
ADHI = f"{ELL} ".join(f"{x} की प्रधानता वाला" for x in ("चाह", "उत्साह", "मन", "जाँच-परख"))


def CL(quals, jh=J1, stage=1, dev=DEV_JHANA):
    """quals: list of qualifier chains of the absorption, joined by «…» ('jo dhyāna … hai')."""
    q = f"{ELL} ".join(quals)
    return f"{dev}, {LEADS}, और {STAGE[stage]}, {jh}, जो ध्यान {q} है"


def ALL4(suffix=""):
    return [p + suffix for p in PP]


E, D = " और " + EMPTY, " और " + DESIRELESS
OPEN = {
    "1-277": CL([PP[0]]),
    "1-339": CL([PP[1]]),
    "1-340": CL([PP[2]]),
    "1-341": CL([PP[3]]),
    "1-342": CL(ALL4(), jh=J5),
    "1-343": CL([EMPTY]),
    "1-344": CL([EMPTY], jh=J5),
    "1-345": CL([PP[0] + E]),
    "1-346": CL([PP[1] + E]),
    "1-347": CL([PP[2] + E]),
    "1-348": CL([PP[3] + E]),
    "1-349": CL(ALL4(E), jh=J5),
    "1-350": CL([DESIRELESS]),
    "1-351": CL([DESIRELESS], jh=J5),
    "1-352": CL([PP[0] + D]),
    "1-353": CL([PP[1] + D]),
    "1-354": CL([PP[2] + D]),
    "1-355": CL([PP[3] + D]),
    "1-356": CL(ALL4(D), jh=J5),
    "1-357": CL([PP[0]], dev=DEV_TWENTY),
    "1-358": CL([PP[0] + " और " + ADHI]),
    "1-359": CL([PP[0] + " और " + ADHI], jh=J5),
    "1-360": CL([PP[0] + " और " + ADHI], dev=DEV_TWENTY),
    "1-361": CL([PP[0]], stage=2),
    "1-362": CL([PP[0]], stage=3),
    "1-363": CL([PP[0]], stage=4),
}
# Pāli markers each clause must show (cheap cross-check of the OPEN table against the source)
MARK = [("dandhābhiññaṃ", "धीमे"), ("khippābhiññaṃ", "शीघ्र"), ("suññataṃ", EMPTY), ("appaṇihitaṃ", DESIRELESS),
        ("pañcamaṃ jhānaṃ", "पाँचवें"), ("lokuttaraṃ maggaṃ", "लोकोत्तर मार्ग"),
        ("ādhipateyyaṃ", "प्रधानता"), ("dutiyāya", "दूसरे चरण"), ("tatiyāya", "तीसरे चरण"),
        ("catutthāya", "चौथे चरण")]

OPEN_RX = re.compile(r"Katame dhammā kusalā\? Yasmiṃ samaye (.*?), tasmiṃ samaye (.*)")


def tr_rest(rest):
    if rest.startswith("phasso hoti, vedanā hoti"):
        lst, tail = rest.split("; ", 1)
        items = lst.split(" hoti, ")
        assert items[-1].endswith(" hoti")
        items[-1] = items[-1][: -len(" hoti")]
        return "उस समय " + ", ".join(HOTI(k) for k in items) + tr_tail("; " + tail)
    end = DANDA
    if rest.endswith(PE + "."):
        rest, end = rest[: -len(PE + ".")], ELL + DANDA
    else:
        assert rest.endswith(".")
        rest = rest[:-1]
    out = []
    for p in rest.split(PE):
        p = p.strip()
        if p.endswith(" hoti"):
            out.append(HOTI(p[: -len(" hoti")]))
        else:
            assert p == "ime dhammā kusalā", p
            out.append(M.ANSWER_BARE(KUSALA))
    return "उस समय " + f"{ELL} ".join(out) + end


def tr_opening(line, clause):
    m = OPEN_RX.fullmatch(line)
    assert m, line
    cl_pi, rest = m.groups()
    for pi, hi in MARK:
        assert (pi in cl_pi) == (hi in clause), (line[:90], pi)
    return M.QUESTION(KUSALA) + " जिस समय " + clause + ", " + tr_rest(rest)


# ---- ^1-364: the faculty of final knowledge (the Pāli has a comma, not a dash, before «idaṃ») ------
_X = N["aññindriyaṃ"]
_S_ANNA_PI = ("paññā pajānanā vicayo pavicayo dhammavicayo sallakkhaṇā upalakkhaṇā paccupalakkhaṇā paṇḍiccaṃ "
              "kosallaṃ nepuññaṃ vebhabyā cintā upaparikkhā bhūrī medhā pariṇāyikā vipassanā sampajaññaṃ "
              "patodo paññā paññindriyaṃ paññābalaṃ paññāsatthaṃ paññāpāsādo paññāāloko paññāobhāso "
              "paññāpajjoto paññāratanaṃ amoho dhammavicayo sammādiṭṭhi dhammavicayasambojjhaṅgo maggaṅgaṃ "
              "maggapariyāpannaṃ")
MANUAL = {
    ("1-364", 0): (C.Q(_X) + f" {G_ANNA} जो {tr_string(_S_ANNA_PI)} है, यह उस समय {_X} है{ELL} "
                   + HOTI("avikkhepo") + f"{ELL} " + YEV_HI),
}


# ---- assembly ---------------------------------------------------------------------------------------
ID_RX = re.compile(r"\s\^([0-9A-Za-z-]+)\s*$")


def pali_segments():
    segs, buf = [], []
    for line in PALI.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        m = ID_RX.search(line)
        if m:
            buf.append(line[: m.start()])
            segs.append((m.group(1), buf))
            buf = []
        else:
            buf.append(line)
    assert not buf
    return segs


def cnt(p, h):
    """(dashes, '?', ellipses) of a Pāli line vs its Hindi line; «…pe…» = one «…»."""
    d = lambda s: s.count("–") + s.count("—")
    return (d(p), p.count("?"), p.count(PE)), (d(h), h.count("?"), h.count(ELL))


def build():
    segs, used = [], set()
    for bid, lines in pali_segments():
        hl = []
        for i, line in enumerate(lines):
            if (bid, i) in MANUAL:
                h = MANUAL[(bid, i)]
                used.add(("M", bid, i))
            elif line in HEAD:
                h = HEAD[line]
            elif line in CLOSE:
                h = CLOSE[line]
            else:
                h = tr_qa(line) or tr_kotthasa(line) or tr_sangaha(line)
                if h is None:
                    assert i == 0 and bid in OPEN, (bid, i, line[:80])
                    h = tr_opening(line, OPEN[bid])
                    used.add(("O", bid))
            a, b = cnt(line, h)
            assert a == b, (bid, i, a, b, h[:120])
            assert "—" not in h and ":-" not in h and "pe…" not in h, (bid, h)
            assert not re.search(r"[A-Za-zāīūṃṅñṭḍṇḷ]", h), (bid, h)
            assert "  " not in h and " ," not in h, (bid, h)
            hl.append(h)
        hl[-1] += f" ^{bid}"
        segs.append("\n".join(hl))
    unused = [k for k in OPEN if ("O", k) not in used] + [k for k in MANUAL if ("M",) + k not in used]
    assert not unused, unused
    return "\n\n".join(segs) + "\n", len(segs)


if __name__ == "__main__":
    text, n = build()
    OUT.write_text(text, encoding="utf-8", newline="\n")
    print("wrote", OUT, n, "segments")
