"""Build the Russian plain zero-shot of pi-1 part 2-04 (twelve unwholesome minds; results of the wholesome).

usage: python -I -X utf8 build_2-04_ru.py
Mirrors ref/en_build_2-04.py + ref/en_const_2_03_2_04.py. Reuses the approved sample constants
(build_ch2_01_sample_ru.py) and matrix frames (build_matika_ru.py); every recurring formula is a fixed
constant below, so every repeat is byte-identical.
"""
import pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(HERE))
import build_matika_ru as M  # noqa: E402  (importing does not rewrite the outputs)
import build_ch2_01_sample_ru as C  # noqa: E402

PART = "2-04-cittuppadakandam.md"
PALI_DIR = ROOT / "AI_translation" / "pali" / "pi-1_split_chapters"
OUT_DIR = ROOT / "AI_translation" / "russian" / "pi-1-russian-plain-zeroshot_split_chapters"
DASH = C.DASH
PE = "…pe…"
ELL = "…"
T = C.TASMIM  # «в это время»
V = M.V

ITEM = {"kusalā": C.KUSALA, "akusalā": C.AKUSALA, "abyākatā": C.ABYAKATA}

# ---- headings and closing lines (headings from ru-zeroshot-terms.md) ---------------------------
HEAD = {
    "#### Dvādasa akusalāni": "#### Двенадцать видов неблагого ума",
    "#### Abyākatavipāko": "#### Этически неопределённые результаты действий",
    "##### Kusalavipākapañcaviññāṇāni": "##### Пять видов сознания, являющихся результатом благих действий",
    "##### Kusalavipākamanodhātu": "##### Элемент ума, являющийся результатом благих действий",
    "##### Kusalavipākamanoviññāṇadhātusomanassasahagatā":
        "##### Элемент умственного сознания, являющийся результатом благих действий и сопровождаемый радостью",
    "##### Kusalavipākamanoviññāṇadhātuupekkhāsahagatā":
        "##### Элемент умственного сознания, являющийся результатом благих действий и сопровождаемый "
        "невозмутимостью",
    "##### Aṭṭhamahāvipākā": "##### Восемь великих результатов действий",
    "##### Rūpāvacaravipākā": "##### Результаты действий, относящиеся к миру форм",
    "##### Arūpāvacaravipākā": "##### Результаты действий, относящиеся к миру без форм",
}
CLOSE = {
    "Dvādasa akusalacittāni.": "Двенадцать видов неблагого ума.",
    "Kusalavipākāni pañcaviññāṇāni.": "Пять видов сознания, являющихся результатом благих действий.",
    "Kusalavipākā manodhātu.": "Элемент ума, являющийся результатом благих действий.",
    "Kusalavipākā manoviññāṇadhātu somanassasahagatā.":
        "Элемент умственного сознания, являющийся результатом благих действий и сопровождаемый радостью.",
    "Kusalavipākā upekkhāsahagatā manoviññāṇadhātu.":
        "Элемент умственного сознания, являющийся результатом благих действий и сопровождаемый невозмутимостью.",
    "Aṭṭhamahāvipākā.": "Восемь великих результатов действий.",
    "Rūpāvacaravipākā.": "Результаты действий, относящиеся к миру форм.",
    "Arūpāvacaravipākā.": "Результаты действий, относящиеся к миру без форм.",
}
# ---- factor names: Pāli = (nominative, instrumental) -------------------------------------------
NC = dict(C.NAMES_C)
NEW_NAMES = {
    "micchādiṭṭhi": ("ложное воззрение", "ложным воззрением"),
    "micchāsaṅkappo": ("ложный помысел", "ложным помыслом"),
    "micchāvāyāmo": ("ложное усилие", "ложным усилием"),
    "micchāsamādhi": ("ложное сосредоточение", "ложным сосредоточением"),
    "ahirikabalaṃ": ("сила бессовестности", "силой бессовестности"),
    "anottappabalaṃ": ("сила отсутствия страха перед дурным", "силой отсутствия страха перед дурным"),
    "lobho": ("жадность", "жадностью"),
    "moho": ("заблуждение", "заблуждением"),
    "abhijjhā": ("алчность", "алчностью"),
    "ahirikaṃ": ("бессовестность", "бессовестностью"),
    "anottappaṃ": ("отсутствие страха перед дурным", "отсутствием страха перед дурным"),
    "upekkhā": ("невозмутимость", "невозмутимостью"),
    "upekkhindriyaṃ": ("способность невозмутимости", "способностью невозмутимости"),
    "dukkhaṃ": ("боль", "болью"),
    "domanassindriyaṃ": ("способность уныния", "способностью уныния"),
    "doso": ("злоба", "злобой"),
    "byāpādo": ("недоброжелательность", "недоброжелательностью"),
    "vicikicchā": ("колебание", "колебанием"),
    "uddhaccaṃ": ("беспокойство", "беспокойством"),
    "sukhindriyaṃ": ("способность удовольствия", "способностью удовольствия"),
    "saṅkhārakkhandho": ("совокупность формирующих факторов", "совокупностью формирующих факторов"),
}
for k in NEW_NAMES:
    assert k not in NC, k
NC.update(NEW_NAMES)
N = {k: v[0] for k, v in NC.items()}
INS = {k: v[1] for k, v in NC.items()}
# the matrix forms of ahirika / anottappa (^1-M2-115) agree with the names
assert M.BARE[("1-M2-115", "а")].lower().startswith(N["ahirikaṃ"])
assert M.BARE[("1-M2-115", "б")].lower().startswith(N["anottappaṃ"])

# ---- synonym strings ----------------------------------------------------------------------------
UNROOT = "неблагой корень"            # akusalamūlaṃ
ABY_ROOT = "этически неопределённый корень"  # abyākatamūlaṃ


def strip_end(s, tail):
    assert s.endswith(tail), (s, tail)
    return s[: -len(tail)]


BASES = dict(C.STRINGS)
_VIT = "takko vitakko saṅkappo appanā byappanā cetaso abhiniropanā"
_SAM = ("cittassa ṭhiti saṇṭhiti avaṭṭhiti avisāhāro avikkhepo avisāhaṭamānasatā samatho "
        "samādhindriyaṃ samādhibalaṃ")
_VIR = ("cetasiko vīriyārambho nikkamo parakkamo uyyāmo vāyāmo ussāho ussoḷhī thāmo dhiti "
        "asithilaparakkamatā anikkhittachandatā anikkhittadhuratā dhurasampaggāho vīriyaṃ "
        "vīriyindriyaṃ vīriyabalaṃ")
BASES[_VIT] = strip_end(C.S_VITAKKA, ", " + N["sammāsaṅkappo"])
BASES[_SAM] = strip_end(C.S_SAMADHI, ", " + N["sammāsamādhi"])
BASES[_VIR] = strip_end(C.S_VIRIYA, ", " + N["sammāvāyāmo"])
BASES["cittassa ṭhiti"] = "устойчивость ума"
assert C.S_SAMADHI.startswith(BASES["cittassa ṭhiti"] + ",")

# upekkhā string: as build_2-01_2-02_ru.py S_UPEKKHA (2-01 has this Pāli string first)
S_UPEKKHA = ("душевное состояние, которое ни отрадно, ни неотрадно, рождённое контактом ума переживание, "
             "которое ни болезненно, ни приятно, рождённое контактом ума чувство, которое ни болезненно, "
             "ни приятно")
# dukkha / bodily sukha strings: the pattern of the sample's sāta string and of build_2-05_ru.py S_KAYA_DUKKHA
S_DUKKHA = ("душевная безотрадность, душевная боль, рождённое контактом ума безотрадное и болезненное переживание, "
            "рождённое контактом ума безотрадное и болезненное чувство")
S_KAYASUKHA = ("телесная отрада, телесное удовольствие, рождённое контактом тела отрадное и приятное переживание, "
               "рождённое контактом тела отрадное и приятное чувство")
# diṭṭhi string: the approved pi-4 wording (^4-62) with diṭṭhi = воззрение and parāmāsa = искажение
S_DITTHI = ("воззрение, приверженность воззрениям, дебри воззрений, пустыня воззрений, изворотливость воззрений, "
            "метания воззрений, оковы воззрений, хватка, закрепление, упрямство, искажение, кривая дорога, "
            "ложный путь, ложность, прибежище сектантских учений, превратная хватка")
S_DITTHI_V = (S_DITTHI.replace("закрепление,", "закрепление" + V("p", "Sī., Syā.", "paṭiggāho") + ",", 1)
              + V("s", "Ka.", "vipariyesagāho"))
assert S_DITTHI_V.count("[") == 2
# lobha string: the sample's alobha string turned positive
S_LOBHA = ("жадность, проявление жадности, состояние жадности, страсть, проявление страсти, состояние страсти, "
           "алчность, жадность, " + UNROOT)
# moha string: the approved pi-4 wording (^4-60), verbatim
S_MOHA = ("незнание, отсутствие видения, отсутствие постижения, отсутствие понимания, непробуждённость, "
          "отсутствие проникновения, неохватывание, отсутствие углубления, отсутствие рассмотрения, "
          "отсутствие обдумывания, неспособность видеть воочию, тупость, глупость, отсутствие ясного понимания, "
          "заблуждение, сильное заблуждение, полное заблуждение, неведение, поток неведения, ярмо неведения, "
          "скрытая склонность к неведению, одержимость неведением, засов неведения, заблуждение, " + UNROOT)
# dosa string: pi-4 (^4-45) with dosa = злоба, in the pattern of the sample's adosa string
S_DOSA = ("злоба, проявление злобы, состояние злобы, недоброжелательность, проявление недоброжелательности, "
          "состояние недоброжелательности, вражда, противодействие, свирепость, грубость, недовольство ума")
S_VICIKICCHA = ("сомнение, проявление сомнения, состояние сомнения, растерянность, колебание, двойственность, "
                "распутье, неуверенность, неспособность прийти к определённому выводу, шатание, нерешительность, "
                "отсутствие углубления, оцепенение ума, терзание ума")
S_UDDHACCA = "беспокойство ума, отсутствие затихания, отвлечение ума, взбудораженность ума"
# ahirika / anottappa strings: the approved pi-4 wording (^4-53, ^4-54), verbatim
S_AHIRIKA = "человек не стыдится того, чего следует стыдиться, не стыдится допускать в себе дурные неблагие явления"
S_ANOTTAPPA = "человек не боится того, чего следует бояться, не боится допускать в себе дурные неблагие явления"
assert S_AHIRIKA == C.S_HIRI.replace("стыдится", "не стыдится")
assert S_ANOTTAPPA == C.S_OTTAPPA.replace("боится", "не боится")

_CITTA_PI = "cittaṃ mano mānasaṃ hadayaṃ paṇḍaraṃ mano manāyatanaṃ manindriyaṃ viññāṇaṃ viññāṇakkhandho"
_CITTA_RU = strip_end(C.S_CITTA, ", соответствующий элемент умственного сознания")

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
    _CITTA_PI + " tajjācakkhuviññāṇadhātu": _CITTA_RU + ", соответствующий элемент зрительного сознания",
    _CITTA_PI + " tajjākāyaviññāṇadhātu": _CITTA_RU + ", соответствующий элемент осязательного сознания",
    _CITTA_PI + " tajjāmanodhātu": _CITTA_RU + ", соответствующий элемент ума",
})
SHAME_STRINGS = {C.S_HIRI, C.S_OTTAPPA, S_AHIRIKA, S_ANOTTAPPA}

# suffix tokens appended after a base (each becomes one more comma item)
TOKENS = {
    "micchāsaṅkappo": N["micchāsaṅkappo"],
    "micchāsamādhi": N["micchāsamādhi"],
    "micchāvāyāmo": N["micchāvāyāmo"],
}


def tr_string(pi):
    """A bare synonym string: the longest matching base plus suffix tokens."""
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


# ---- frame qualifiers (the sample's TAJJA pattern) -----------------------------------------------
def TAJJA_OF(element_gen):
    return f"рождённое контактом соответствующего {element_gen}"


assert TAJJA_OF("элемента умственного сознания") == C.TAJJA
PREFIXES = [  # (Pāli prefix regex, Russian qualifier)
    (r"tajjāmanoviññāṇadhātusamphassaj(?:aṃ|ā) ", C.TAJJA),
    (r"tajjācakkhuviññāṇadhātusamphassaj(?:aṃ|ā) ", TAJJA_OF("элемента зрительного сознания")),
    (r"tajjākāyaviññāṇadhātusamphassaj(?:aṃ|ā) ", TAJJA_OF("элемента осязательного сознания")),
    (r"tajjāmanodhātusamphassaj(?:aṃ|ā) ", TAJJA_OF("элемента ума")),
]

# ---- closing formulas ------------------------------------------------------------------------------
YEV_PI = "ye vā pana tasmiṃ samaye aññepi atthi paṭiccasamuppannā arūpino dhammā – ime dhammā "
EXCEPT = "кроме совокупности чувств, кроме совокупности восприятия, кроме совокупности сознания"  # as 2-01, 2-03, 2-05
assert C.YEVAPANA(C.KUSALA) == C.FRAMES["Ye vā pana tasmiṃ samaye aññepi atthi paṭiccasamuppannā arūpino dhammā "
                                        "– ime dhammā kusalā."][len("Или же "):]


def tr_tail(t):
    """Tail after '... X hoti' at the end of an answer or list."""
    t = t.replace(" " + PE, PE)
    if t in (".", "?"):
        return t
    if t == PE + ".":
        return ELL + "."
    m = re.fullmatch(r"(;|…pe…) " + re.escape(YEV_PI) + r"(kusalā|akusalā|abyākatā)(\.|…pe…\.)", t)
    if m:
        lead = "; или же " if m.group(1) == ";" else ELL + " или же "
        s = lead + C.YEVAPANA(ITEM[m.group(2)])
        if m.group(3) != ".":
            s = s[:-1] + ELL + "."
        return s
    m = re.fullmatch(r"…pe… ime dhammā (kusalā|akusalā|abyākatā)\.", t)
    if m:
        return ELL + " " + M.ANSWER(ITEM[m.group(1)])
    raise ValueError("unknown tail: " + repr(t))


# ---- question / answer lines ------------------------------------------------------------------------
QA_RX = re.compile(r"Katam(?:o|ā|aṃ) tasmiṃ samaye (\S+) hoti([?.]) Y(?:o|ā|aṃ) (.*?) – (?:ayaṃ|idaṃ) "
                   r"tasmiṃ samaye (\S+) hoti(.*)")


def tr_qa(line):
    m = QA_RX.fullmatch(line)
    if not m:
        return None
    key, qmark, body, key2, tail = m.groups()
    assert key == key2, line
    q = f"Что {T} является {INS[key]}{qmark}"
    end = f"{DASH} это и есть {N[key]} {T}"
    if body.startswith("tasmiṃ samaye "):
        body = body[len("tasmiṃ samaye "):]
        pre = ""
        for rx, ru in PREFIXES:
            mm = re.match(rx, body)
            if mm:
                body = body[mm.end():]
                pre = ", " + ru + ","
                break
        s = tr_string(body)
        if s in SHAME_STRINGS:
            assert not pre
            a = f"То, что {T} {s}, {end}"
        else:
            a = f"То, что {T}{pre} есть {s}, {end}"
    elif body.startswith("tesaṃ arūpīnaṃ dhammānaṃ "):
        s = tr_string(body[len("tesaṃ arūpīnaṃ dhammānaṃ "):])
        a = f"То, что {C.G_JIVITA} есть {s}, {end}"
    else:
        raise ValueError("unknown answer body: " + body)
    return q + " " + a + tr_tail(tail)


# the frames agree byte for byte with the approved sample
assert tr_qa("Katamo tasmiṃ samaye phasso hoti? Yo tasmiṃ samaye phasso phusanā saṃphusanā saṃphusitattaṃ – "
             "ayaṃ tasmiṃ samaye phasso hoti.") == C.QA("phasso", C.S_PHASSA)
assert tr_qa("Katamā tasmiṃ samaye saññā hoti? Yā tasmiṃ samaye tajjāmanoviññāṇadhātusamphassajā saññā sañjānanā "
             "sañjānitattaṃ – ayaṃ tasmiṃ samaye saññā hoti.") == C.T("saññā", C.S_SANNA)
assert tr_qa("Katamaṃ tasmiṃ samaye jīvitindriyaṃ hoti? Yo tesaṃ arūpīnaṃ dhammānaṃ āyu ṭhiti yapanā yāpanā "
             "iriyanā vattanā pālanā jīvitaṃ jīvitindriyaṃ – idaṃ tasmiṃ samaye jīvitindriyaṃ hoti.") \
    == C.JIVITA("jīvitindriyaṃ", C.S_JIVITA)
assert tr_qa("Katamaṃ tasmiṃ samaye hiribalaṃ hoti? Yaṃ tasmiṃ samaye hirīyati hiriyitabbena hirīyati pāpakānaṃ "
             "akusalānaṃ dhammānaṃ samāpattiyā – idaṃ tasmiṃ samaye hiribalaṃ hoti.") \
    == C.SHAME("hiribalaṃ", C.S_HIRI)


# ---- lists of factors ------------------------------------------------------------------------------
def hoti_list(pali):
    """'phasso hoti, vedanā hoti, ... avikkhepo hoti' -> 'есть контакт, есть чувство, ...'."""
    items = pali.split(" hoti, ")
    assert items[-1].endswith(" hoti"), pali
    items[-1] = items[-1][: -len(" hoti")]
    return ", ".join(f"есть {N[k]}" for k in items)


assert hoti_list("phasso hoti, vedanā hoti") == C.LIST_ITEM("phasso") + ", " + C.LIST_ITEM("vedanā")


def bare_list(pali):
    """'Phasso cetanā vitakko ...' -> 'Контакт, намерение, направленная мысль, ...'."""
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
    k = "saṅkhārakkhandho"
    return (f"Что {T} является {INS[k]}? {bare_list(m.group(1))}; или же {C.YEVAPANA_BODY}, {EXCEPT}, "
            f"{DASH} это и есть {N[k]} {T}" + tr_tail(m.group(2)))


# ---- 'Tasmiṃ kho pana samaye cattāro khandhā honti, ...' -----------------------------------------------
SANGAHA_ITEMS = {
    "cattāro khandhā honti": "есть четыре совокупности",
    "dvāyatanāni honti": "есть две сферы восприятия",
    "dve dhātuyo honti": "есть два элемента",
    "tayo āhārā honti": "есть три вида питания",
    "pañcindriyāni honti": "есть пять способностей",
    "cattāri indriyāni honti": "есть четыре способности",
    "tīṇindriyāni honti": "есть три способности",
    # «-частный» as build_2-01_2-02_ru.py COUNTED
    "pañcaṅgikaṃ jhānaṃ hoti": "есть пятичастное медитативное погружение",
    "caturaṅgikaṃ jhānaṃ hoti": "есть четырёхчастное медитативное погружение",
    "caturaṅgiko maggo hoti": "есть четырёхчастный путь",
    "tivaṅgiko maggo hoti": "есть трёхчастный путь",
    "duvaṅgiko maggo hoti": "есть двухчастный путь",
    "cattāri balāni honti": "есть четыре силы",
    "tīṇi balāni honti": "есть три силы",
    "dve hetū honti": "есть два корня",
    "eko hetu hoti": "есть один корень",
    "eko phasso hoti": "есть один контакт",
    "ekā cakkhuviññāṇadhātu hoti": "есть один элемент зрительного сознания",
    "ekā kāyaviññāṇadhātu hoti": "есть один элемент осязательного сознания",
    "ekā manodhātu hoti": "есть один элемент ума",
    "ekā manoviññāṇadhātu hoti": "есть один элемент умственного сознания",
    "ekaṃ dhammāyatanaṃ hoti": "есть одна сфера объектов ума",
    "ekā dhammadhātu hoti": "есть один элемент объектов ума",
}
SANGAHA_HEAD_PI = "Tasmiṃ kho pana samaye "
SANGAHA_HEAD = f"И {T} "


def tr_sangaha(line):
    if not line.startswith(SANGAHA_HEAD_PI + "cattāro khandhā honti"):
        return None
    body, tail = line[len(SANGAHA_HEAD_PI):].split("; ", 1)
    parts = []
    for item in body.split(", "):
        parts.append((ELL + " ").join(SANGAHA_ITEMS[x.strip()] for x in item.split(PE)))
    return SANGAHA_HEAD + ", ".join(parts) + tr_tail("; " + tail)


# ---- objects of the opening sentences ----------------------------------------------------------------
ARAM_FULL = C.ARAMMANA
ARAM_VISIBLE = "имеющий объектом видимую форму"
ARAM_ANY = "или что бы то ни было"
assert ARAM_FULL.startswith(ARAM_VISIBLE + ", ") and ARAM_FULL.endswith(", " + ARAM_ANY)
assert ", или объект ума, " in ARAM_FULL and ", или осязаемое, " in ARAM_FULL
ARAM_ABBR = f"{ARAM_VISIBLE}{ELL} или объект ума, {ARAM_ANY}"        # rūpa…pe… dhamma
ARAM_ABBR_TOUCH = f"{ARAM_VISIBLE}{ELL} или осязаемое, {ARAM_ANY}"   # rūpa…pe… phoṭṭhabba
ARAM_ABBR_ANY = f"{ARAM_VISIBLE}{ELL} {ARAM_ANY}"                    # rūpa…pe… yaṃ yaṃ
PROMPTED = "с побуждением"  # sasaṅkhārena

# ---- the unwholesome minds -----------------------------------------------------------------------------
JOY = "сопровождаемый радостью"
EQU = "сопровождаемый невозмутимостью"
SAD = "сопровождаемый унынием"
assert C.ACC_SOMA_NANA.startswith(JOY + " и ")
W_ASSOC = "связанный с приверженностью воззрениям"
W_DISS = "не связанный с приверженностью воззрениям"
UNW = "возникает неблагой ум, "


def U(acc, assoc, aram, prompted=False):
    return UNW + f"{acc} и {assoc}, " + (PROMPTED + ", " if prompted else "") + aram


# ---- results of the wholesome -------------------------------------------------------------------------
def DONE(action):
    """'<X>ssa kusalassa kammassa katattā upacitattā …' (shape of build_2-05_ru.py AKUS_KAMMA)"""
    return f"вследствие того, что {action} было совершено и накоплено"


KAMA_ACTION = "благое действие, относящееся к миру чувственных желаний,"
RES_N = "являющееся его результатом"  # vipākaṃ (with сознание), as build_2-05_ru.py
RES_M = "являющийся его результатом"  # vipākā (with элемент)
RES_KAMA = DONE(KAMA_ACTION) + ", возникает "
KNOW_A = "связанный со знанием"
KNOW_D = "не связанный со знанием"
assert C.ACC_SOMA_NANA == f"{JOY} и {KNOW_A}"
EIGHT = (ELL + " ").join(
    f"{acc} и {kn}" + (", " + PROMPTED if pr else "")
    for acc in (JOY, EQU) for kn in (KNOW_A, KNOW_D) for pr in (False, True))
N_EQU = "сопровождаемое невозмутимостью"  # neuter: with сознание
N_HAPPY = "сопровождаемое счастьем"

OPEN = {
    "1-365": U(JOY, W_ASSOC, ARAM_FULL),
    "1-399": U(JOY, W_ASSOC, ARAM_ABBR, True),
    "1-400": U(JOY, W_DISS, ARAM_FULL),
    "1-402": U(JOY, W_DISS, ARAM_ABBR, True),
    "1-403": U(EQU, W_ASSOC, ARAM_FULL),
    "1-409": U(EQU, W_ASSOC, ARAM_ABBR, True),
    "1-410": U(EQU, W_DISS, ARAM_FULL),
    "1-412": U(EQU, W_DISS, ARAM_ABBR, True),
    "1-413": U(SAD, "связанный с неприязнью", ARAM_FULL),
    "1-421": U(SAD, "связанный с неприязнью", ARAM_ABBR, True),
    "1-422": U(EQU, "связанный с колебанием", ARAM_FULL),
    "1-427": U(EQU, "связанный с беспокойством", ARAM_ABBR_ANY),
    "1-431": RES_KAMA + f"зрительное сознание, {RES_N}, {N_EQU}, имеющее объектом видимую форму",
    "1-443": (RES_KAMA + f"слуховое сознание, {RES_N}, {N_EQU}, имеющее объектом звук{ELL} "
              f"возникает обонятельное сознание, {N_EQU}, имеющее объектом запах{ELL} "
              f"возникает вкусовое сознание, {N_EQU}, имеющее объектом вкус{ELL} "
              f"возникает осязательное сознание, {N_HAPPY}, имеющее объектом осязаемое"),
    "1-455": RES_KAMA + f"элемент ума, {RES_M}, {EQU}, " + ARAM_ABBR_TOUCH,
    "1-469": RES_KAMA + f"элемент умственного сознания, {RES_M}, {JOY}, " + ARAM_ABBR,
    "1-484": RES_KAMA + f"элемент умственного сознания, {RES_M}, {EQU}, " + ARAM_ABBR,
    "1-498": RES_KAMA + f"элемент умственного сознания, {RES_M}, {EIGHT}, " + ARAM_ABBR,
}

OPEN_RX = re.compile(r"Katame dhammā (kusalā|akusalā|abyākatā)\? Yasmiṃ samaye (.*?), tasmiṃ samaye (.*)")
PIECES = {
    "ime dhammā kusalā": M.ANSWER_BARE(C.KUSALA),
    "ime dhammā akusalā": M.ANSWER_BARE(C.AKUSALA),
    "ime dhammā abyākatā": M.ANSWER_BARE(C.ABYAKATA),
    "alobho abyākatamūlaṃ": f"{N['alobho']}, {ABY_ROOT}",
    "adoso abyākatamūlaṃ": f"{N['adoso']}, {ABY_ROOT}",
}


def tr_rest(rest):
    """The part after 'tasmiṃ samaye' in an opening sentence."""
    if "; " + YEV_PI in rest:
        lst, tail = rest.split("; ", 1)
        return f"{T} " + hoti_list(lst) + tr_tail("; " + tail)
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
            out.append(C.LIST_ITEM(p[: -len(" hoti")]) if p[: -len(" hoti")] in C.NAMES
                       else "есть " + N[p[: -len(" hoti")]])
        else:
            out.append(PIECES[p])
    return f"{T} " + (ELL + " ").join(out) + end


def tr_opening(line, clause_ru):
    m = OPEN_RX.fullmatch(line)
    assert m, line
    kind, _clause_pi, rest = m.groups()
    return f"{M.QUESTION(ITEM[kind])} В то время, когда {clause_ru}, " + tr_rest(rest)


# ---- results of the fine-material and immaterial spheres (two sentences on one line) --------------------
# The kusala half repeats the 2-02 sentences; its intros and phrases are copied byte for byte from
# build_2-01_2-02_ru.py (INTROS, PH, ORD), so identical Pāli gets identical Russian. check_against_2_02()
# compares them with that module when it is importable and prints any drift.
INTRO = {
    "rūpūpapattiyā": "В то время, когда человек, развивая путь к рождению в мире форм, ",
    "arūpūpapattiyā": "В то время, когда человек, развивая путь к рождению в мире без форм, ",
}
SPHERE = {"rūpāvacarassa": "форм", "arūpāvacarassa": "без форм"}
J = "медитативное погружение"
DWELL = "и пребывает в нём"
PH = {
    "vivicceva kāmehi": "полностью уединившись от чувственных удовольствий",
    "vitakkavicārānaṃ vūpasamā": "с затиханием направленной мысли и удержания мысли",
    "sukhassa ca pahānā": "с устранением приятного",
    "pathavīkasiṇaṃ": "на всеохватном объекте земли",
    "sabbaso rūpasaññānaṃ samatikkamā paṭighasaññānaṃ atthaṅgamā nānattasaññānaṃ amanasikārā":
        "полностью преодолев восприятия материальной формы, с исчезновением восприятий соударения, "
        "не уделяя внимания восприятиям разнообразия",
    "ākāsānañcāyatanasaññāsahagataṃ": "с восприятием сферы бесконечного пространства",
    "sabbaso ākāsānañcāyatanaṃ samatikkamma": "полностью преодолев сферу бесконечного пространства",
    "viññāṇañcāyatanasaññāsahagataṃ": "с восприятием сферы бесконечного сознания",
    "sabbaso viññāṇañcāyatanaṃ samatikkamma": "полностью преодолев сферу бесконечного сознания",
    "ākiñcaññāyatanasaññāsahagataṃ": "с восприятием сферы отсутствия чего-либо",
    "sabbaso ākiñcaññāyatanaṃ samatikkamma": "полностью преодолев сферу отсутствия чего-либо",
    "nevasaññānāsaññāyatanasaññāsahagataṃ": "с восприятием сферы ни восприятия, ни невосприятия",
}
ORD = {"paṭhamaṃ": ("первое", "в"), "dutiyaṃ": ("второе", "во"), "tatiyaṃ": ("третье", "в"),
       "catutthaṃ": ("четвёртое", "в"), "pañcamaṃ": ("пятое", "в")}
for _p, (_o, _prep) in ORD.items():
    PH[f"{_p} jhānaṃ upasampajja viharati"] = f"входит {_prep} {_o} {J}"
    PH[f"{_p} jhānaṃ"] = f"{_o} {J}"
PH_MAX = max(len(k.split()) for k in PH)


def chunk_tr(part):
    """Greedy longest-phrase translation of a Pāli chunk without …pe…; phrases joined by commas."""
    words = part.split()
    res, i = [], 0
    while i < len(words):
        for L in range(min(PH_MAX, len(words) - i), 0, -1):
            key = " ".join(words[i:i + L])
            if key in PH:
                break
        else:
            raise KeyError("phrase: " + " ".join(words[i:]))
        res.append(PH[key])
        i += L
    return ", ".join(res)


def x_tr(x):
    out = []
    for i, part in enumerate(re.split(r"(\s*…pe…\s*)", x)):
        if i % 2:
            out.append(part.replace(PE, ELL))
        elif part.strip():
            out.append(chunk_tr(part))
    xr = "".join(out)
    # as build_2-01_2-02_ru.py kusala_ru: «и пребывает в нём» closes the whole qualifier chain
    assert x.count("upasampajja viharati") == 1, x
    return xr + (" " if xr.endswith(J) else ", ") + DWELL


ABBR_LIST = f"{T} есть {N['phasso']}{ELL} есть {N['avikkhepo']}{ELL} "
SPHERE_RX = re.compile(
    r"Katame dhammā abyākatā\? Yasmiṃ samaye (rūpūpapattiyā|arūpūpapattiyā) maggaṃ bhāveti (.*?), "
    r"tasmiṃ samaye phasso hoti…pe… avikkhepo hoti…pe… ime dhammā kusalā\. "
    r"Tasseva (rūpāvacarassa|arūpāvacarassa) kusalassa kammassa katattā upacitattā vipākaṃ (.*?), "
    r"tasmiṃ samaye phasso hoti…pe… avikkhepo hoti…pe… ime dhammā abyākatā\.")


def kusala_half(up, x):
    """'Yasmiṃ samaye rūpūpapattiyā maggaṃ bhāveti X, tasmiṃ samaye phasso hoti…pe… … ime dhammā kusalā.'"""
    return INTRO[up] + x_tr(x) + ", " + ABBR_LIST + M.ANSWER(C.KUSALA)


def tr_sphere(line):
    m = SPHERE_RX.fullmatch(line)
    if not m:
        return None
    up, x1, sphere, x2 = m.groups()
    x2r = x_tr(x2)
    lead = ", " if x2r.startswith("полностью ") else " "  # a participial clause is set off by commas
    res = ("Когда " + DONE(f"это же благое действие, относящееся к миру {SPHERE[sphere]},")
           + ", человек в качестве его результата" + lead + x2r + ", " + ABBR_LIST + M.ANSWER(C.ABYAKATA))
    return M.QUESTION(C.ABYAKATA) + " " + kusala_half(up, x1) + " " + res


def check_against_2_02():
    """Soft check: compare the copied 2-02 phrases with build_2-01_2-02_ru.py (if importable)."""
    try:
        import importlib
        B = importlib.import_module("build_2-01_2-02_ru")
    except Exception as e:  # the other part may be mid-edit
        print("note: build_2-01_2-02_ru.py not importable, cross-check skipped:", type(e).__name__)
        return
    drift = []
    for k, v in PH.items():
        b = B.PH.get(k)
        if b is None or b.replace("{V}", "") != v:
            drift.append((k, v, b))
    intros = {p.split(" ")[0]: r for p, r, _ in B.INTROS}
    for k, v in INTRO.items():
        if intros.get(k) != v:
            drift.append((k, v, intros.get(k)))
    if B.S_UPEKKHA != S_UPEKKHA:
        drift.append(("S_UPEKKHA", S_UPEKKHA, B.S_UPEKKHA))
    if B.THAP_R != EXCEPT:
        drift.append(("ṭhapetvā …", EXCEPT, B.THAP_R))
    for p, mine in (("pañcaṅgikaṃ jhānaṃ", "pañcaṅgikaṃ jhānaṃ hoti"),
                    ("caturaṅgikaṃ jhānaṃ", "caturaṅgikaṃ jhānaṃ hoti"),
                    ("caturaṅgiko maggo", "caturaṅgiko maggo hoti")):
        if "есть " + B.COUNTED[p][0] != SANGAHA_ITEMS[mine]:
            drift.append((p, SANGAHA_ITEMS[mine], B.COUNTED[p][0]))
    # the whole kusala half, rendered by 2-02's own sentence translator
    for bid, lines in pali_segments(PALI_DIR / PART):
        m = SPHERE_RX.fullmatch(lines[0])
        if not m:
            continue
        kl = (f"Katame dhammā kusalā? Yasmiṃ samaye {m.group(1)} maggaṃ bhāveti {m.group(2)}, tasmiṃ samaye "
              "phasso hoti…pe… avikkhepo hoti…pe… ime dhammā kusalā.")
        try:
            theirs = B.kusala_ru(kl)
        except Exception as e:
            theirs = f"<{type(e).__name__}: {e}>"
        mine = M.QUESTION(C.KUSALA) + " " + kusala_half(m.group(1), m.group(2))
        if theirs != mine:
            drift.append((bid, mine, theirs))
    for d in drift:
        print("DRIFT vs 2-01/2-02:", d)
    print("cross-check with build_2-01_2-02_ru.py:", "OK" if not drift else f"{len(drift)} differences")


MANUAL = {}

# ---- build ---------------------------------------------------------------------------------------------
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
    return s.count("–") + s.count("—"), s.count("?"), s.count("[")


LATIN = re.compile(r"[A-Za-zÀ-ɏḀ-ỿ]")


def build():
    pali = pali_segments(PALI_DIR / PART)
    used = set()
    out = []
    for bid, lines in pali:
        rl = []
        for i, line in enumerate(lines):
            if (bid, i) in MANUAL:
                ru = MANUAL[(bid, i)]
                used.add(("M", bid, i))
            elif line in HEAD:
                ru = HEAD[line]
            elif line in CLOSE:
                ru = CLOSE[line]
            else:
                ru = tr_qa(line) or tr_kotthasa(line) or tr_sangaha(line) or tr_sphere(line)
                if ru is None:
                    assert i == 0 and bid in OPEN, (bid, i, line[:80])
                    ru = tr_opening(line, OPEN[bid])
                    used.add(("O", bid))
            assert cnt(line) == cnt(ru), (bid, cnt(line), cnt(ru), ru)
            assert "—" not in ru and ":-" not in ru and "pe…" not in ru, (bid, ru)
            assert not LATIN.search(re.sub(r"\[[^\]]*\]", "", ru)), (bid, ru)
            assert ru[0].isupper() or ru.startswith("#"), (bid, ru)
            rl.append(ru)
        rl[-1] += f" ^{bid}"
        out.append("\n".join(rl))
    unused = [k for k in OPEN if ("O", k) not in used] + [k for k in MANUAL if ("M",) + k not in used]
    assert not unused, unused
    return "\n\n".join(out) + "\n", len(pali)


TEXT, NSEG = build()

if __name__ == "__main__":
    out = OUT_DIR / PART
    out.write_text(TEXT, encoding="utf-8", newline="\n")
    print("wrote", out, NSEG, "segments")
    check_against_2_02()
