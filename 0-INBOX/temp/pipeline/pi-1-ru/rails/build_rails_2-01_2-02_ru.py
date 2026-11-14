"""Builder for the Russian rails translation of pi-1 (Dhammasaṅgaṇī, plain audience),
chapters 2-01 (after the approved sample, ^1-1-1-2-0 onward) and 2-02.

Writes (only when run as a script):
  AI_translation/russian/pi-1-russian-plain-rails_split_chapters/2-01-cittuppadakandam.md
      (= sample-2-01/2-01-sample.md byte-for-byte + the rest of the chapter)
  AI_translation/russian/pi-1-russian-plain-rails_split_chapters/2-02-cittuppadakandam.md

Every line is translated from the Pāli by fixed strings: the sample constants (imported from
build_rails_sample_ru.py, never edited) plus the tables below. Unknown Pāli raises KeyError, so
nothing is guessed silently; identical Pāli gives byte-identical Russian.
Terms follow the locked termbase AI_translation/russian/pi-1-pali-russian-termbase-plain.md.
Later chapter builders may import this file (importing writes nothing): NAMES, STR, there_list,
name_list, tail_ru, qa_ru, kusala_ru, summary_ru, EXACT, ATTR_M, DESC_N, PIECES.

usage: python -I -X utf8 build_rails_2-01_2-02_ru.py
"""
import pathlib
import re
import sys

HERE = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-ru\rails")
sys.path.insert(0, str(HERE))
import build_rails_sample_ru as S  # noqa: E402  (importing writes nothing)

PALI = S.PALI
OUT = S.OUT
SAMPLE = HERE / "sample-2-01" / "2-01-sample.md"
PE, ELL, DASH = "…pe…", "…", "–"
cap = S.cap
TS = S.TS                                     # в это время

# =========================================================================================
# 1. Names: Pāli nominative -> Russian nominative (Q/A frames, lists, summaries)
# =========================================================================================
NAMES = dict(S.FN)
NAMES.update({
    "upekkhā": "невозмутимость",
    "upekkhindriyaṃ": "способность невозмутимости",
    "vedanākkhandho": "совокупность чувств",
    "saññākkhandho": "совокупность восприятия",
    "saṅkhārakkhandho": "совокупность формирующих факторов",
    "viññāṇakkhandho": "совокупность сознания",
    "manāyatanaṃ": "сфера ума",
    "dhammāyatanaṃ": "сфера объектов ума",
    "manoviññāṇadhātu": "элемент умственного сознания",
    "dhammadhātu": "элемент объектов ума",
    "phassāhāro": "питание контактом",
    "manosañcetanāhāro": "питание умственным намерением",
    "viññāṇāhāro": "питание сознанием",
    # Koṭṭhāsavāra: counted groups
    "cattāro khandhā": "четыре совокупности",
    "dvāyatanāni": "две сферы восприятия",
    "dve dhātuyo": "два элемента",
    "tayo āhārā": "три вида питания",
    "aṭṭhindriyāni": "восемь способностей",
    "sattindriyāni": "семь способностей",
    "satta balāni": "семь сил",
    "cha balāni": "шесть сил",
    "tayo hetū": "три корня",
    "dve hetū": "два корня",
    "pañcaṅgikaṃ jhānaṃ": "пятичастное медитативное погружение",
    "caturaṅgikaṃ jhānaṃ": "четырёхчастное медитативное погружение",
    "tivaṅgikaṃ jhānaṃ": "трёхчастное медитативное погружение",
    "duvaṅgikaṃ jhānaṃ": "двухчастное медитативное погружение",
    "pañcaṅgiko maggo": "пятичастный путь",
    "caturaṅgiko maggo": "четырёхчастный путь",
    # Koṭṭhāsavāra: «eko/ekā/ekaṃ X» (Russian gender of the Russian noun)
    "eko phasso": "один контакт",
    "ekā vedanā": "одно чувство",
    "ekā saññā": "одно восприятие",
    "ekā cetanā": "одно намерение",
    "ekaṃ cittaṃ": "один ум",
    "eko vedanākkhandho": "одна совокупность чувств",
    "eko saññākkhandho": "одна совокупность восприятия",
    "eko saṅkhārakkhandho": "одна совокупность формирующих факторов",
    "eko viññāṇakkhandho": "одна совокупность сознания",
    "ekaṃ manāyatanaṃ": "одна сфера ума",
    "ekaṃ manindriyaṃ": "одна способность ума",
    "ekā manoviññāṇadhātu": "один элемент умственного сознания",
    "ekaṃ dhammāyatanaṃ": "одна сфера объектов ума",
    "ekā dhammadhātu": "один элемент объектов ума",
    # Suññatavāra: bare group names
    "dhammā": "явления",
    "khandhā": "совокупности",
    "āyatanāni": "сферы восприятия",
    "dhātuyo": "элементы",
    "āhārā": "виды питания",
    "indriyāni": "способности",
    "jhānaṃ": "медитативное погружение",
    "maggo": "путь",
    "balāni": "силы",
    "hetū": "корни",
})


def name(p):
    p = p[0].lower() + p[1:]
    return NAMES[p]


# =========================================================================================
# 2. Synonym strings: Pāli (between «Yo/Yā/Yaṃ tasmiṃ samaye» and the dash) -> Russian body
# =========================================================================================
def _strip_prefix(s, prefix):
    assert s.startswith(prefix), (s, prefix)
    return s[len(prefix):]


S_SANNA_PLAIN = _strip_prefix(S.S_SANNA, S.TAJJA.format("ое") + " ")          # восприятие, узнавание, …
S_CETANA_PLAIN = _strip_prefix(S.S_CETANA, S.TAJJA.format("ое") + " ").replace(
    " " + S.reading("Syā.", "sañcetayitattaṃ"), "")                             # намерение, … (no variant)
S_JIVITA_PLAIN = S.S_JIVITA.replace(" " + S.spell("Sī.", "irīyanā"), "")       # без варианта irīyanā
assert "[" not in S_CETANA_PLAIN + S_JIVITA_PLAIN
S_UPEKKHA = ("душевное состояние, которое ни отрадно, ни безотрадно, "
             "рождённое контактом ума переживание, которое ни болезненно, ни приятно, "
             "рождённое контактом ума чувство, которое ни болезненно, ни приятно")
S_PANNA_ABBR = "мудрость, понимание… отсутствие заблуждения, исследование явлений, правильное воззрение"
assert S.S_PANNA.startswith("мудрость, понимание, ") and S.S_PANNA.endswith(
    ", отсутствие заблуждения, исследование явлений, правильное воззрение")

P_UPEKKHA = "cetasikaṃ neva sātaṃ nāsātaṃ cetosamphassajaṃ adukkhamasukhaṃ vedayitaṃ cetosamphassajā adukkhamasukhā vedanā"
STR = {   # Pāli string -> Russian string (placed after «То, что в это время есть »)
    "phasso phusanā saṃphusanā saṃphusitattaṃ": S.S_PHASSA,
    "cetasikaṃ sātaṃ cetasikaṃ sukhaṃ cetosamphassajaṃ sātaṃ sukhaṃ vedayitaṃ cetosamphassajā sātā sukhā vedanā":
        S.S_SUKHA,
    "saññā sañjānanā sañjānitattaṃ": S_SANNA_PLAIN,
    "cetanā sañcetanā cetayitattaṃ": S_CETANA_PLAIN,
    "cittaṃ mano mānasaṃ hadayaṃ paṇḍaraṃ mano manāyatanaṃ manindriyaṃ viññāṇaṃ viññāṇakkhandho "
    "tajjāmanoviññāṇadhātu": S.S_CITTA,
    "takko vitakko saṅkappo appanā byappanā cetaso abhiniropanā sammāsaṅkappo": S.S_VITAKKA,
    "cāro vicāro anuvicāro upavicāro cittassa anusandhānatā anupekkhanatā": S.S_VICARA,
    "pīti pāmojjaṃ āmodanā pamodanā hāso pahāso vitti odagyaṃ attamanatā cittassa": S.S_PITI,
    "cittassa ṭhiti saṇṭhiti avaṭṭhiti avisāhāro avikkhepo avisāhaṭamānasatā samatho samādhindriyaṃ "
    "samādhibalaṃ sammāsamādhi": S.S_SAMADHI,
    "saddhā saddahanā okappanā abhippasādo saddhā saddhindriyaṃ saddhābalaṃ": S.S_SADDHA,
    "cetasiko vīriyārambho nikkamo parakkamo uyyāmo vāyāmo ussāho ussoḷhī thāmo dhiti asithilaparakkamatā "
    "anikkhittachandatā anikkhittadhuratā dhurasampaggāho vīriyaṃ vīriyindriyaṃ vīriyabalaṃ sammāvāyāmo":
        S.S_VIRIYA,
    "sati anussati paṭissati sati saraṇatā dhāraṇatā apilāpanatā asammussanatā sati satindriyaṃ satibalaṃ "
    "sammāsati": S.S_SATI,
    "paññā pajānanā vicayo pavicayo dhammavicayo sallakkhaṇā upalakkhaṇā paccupalakkhaṇā paṇḍiccaṃ kosallaṃ "
    "nepuññaṃ vebhabyā cintā upaparikkhā bhūrī medhā pariṇāyikā vipassanā sampajaññaṃ patodo paññā "
    "paññindriyaṃ paññābalaṃ paññāsatthaṃ paññāpāsādo paññāāloko paññāobhāso paññāpajjoto paññāratanaṃ "
    "amoho dhammavicayo sammādiṭṭhi": S.S_PANNA,
    "paññā pajānanā vicayo pavicayo dhammavicayo sallakkhaṇā upalakkhaṇā paccupalakkhaṇā paṇḍiccaṃ kosallaṃ "
    "nepuññaṃ vebhabyā cintā upaparikkhā bhūrī medhā pariṇāyikā vipassanā sampajaññaṃ patodo paññā "
    "paññindriyaṃ paññābalaṃ paññāsatthaṃ paññāpāsādo paññāāloko paññāobhāso paññāpajjoto paññāratanaṃ "
    "amoho dhammavicayo sammādiṭṭhi amoho kusalamūlaṃ": S.S_AMOHA,
    "paññā pajānanā…pe… amoho dhammavicayo sammādiṭṭhi": S_PANNA_ABBR,
    "alobho alubbhanā alubbhitattaṃ asārāgo asārajjanā asārajjitattaṃ anabhijjhā alobho kusalamūlaṃ":
        S.S_ALOBHA,
    "adoso adussanā adussitattaṃ abyāpādo abyāpajjo adoso kusalamūlaṃ": S.S_ADOSA,
    "tajjāmanoviññāṇadhātusamphassajaṃ cetasikaṃ sātaṃ cetasikaṃ sukhaṃ cetosamphassajaṃ sātaṃ sukhaṃ "
    "vedayitaṃ cetosamphassajā sātā sukhā vedanā": S.S_VEDANA,
    "tajjāmanoviññāṇadhātusamphassajā saññā sañjānanā sañjānitattaṃ": S.S_SANNA,
    P_UPEKKHA: S_UPEKKHA,
    "tajjāmanoviññāṇadhātusamphassajaṃ " + P_UPEKKHA: S.TAJJA.format("ое") + " " + S_UPEKKHA,
}
HIRI_P = "hirīyati hiriyitabbena hirīyati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā"
OTTAPPA_P = "ottappati ottappitabbena ottappati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā"
JIVITA_P = "āyu ṭhiti yapanā yāpanā iriyanā vattanā pālanā jīvitaṃ jīvitindriyaṃ"

# =========================================================================================
# 3. Tails: «ye vā pana …», «ayaṃ tasmiṃ samaye X hoti», «ime dhammā kusalā», «…pe…», dash
# =========================================================================================
YVP_P = "ye vā pana tasmiṃ samaye aññepi atthi paṭiccasamuppannā arūpino dhammā"
YVP_R = "или же " + S.OTHERS
THAP_P = "ṭhapetvā vedanākkhandhaṃ ṭhapetvā saññākkhandhaṃ ṭhapetvā viññāṇakkhandhaṃ"
THAP_R = "кроме совокупности чувств, кроме совокупности восприятия, кроме совокупности сознания"
THAP_PV = "ṭhapetvā [thapetvā (ka.)] vedanākkhandhaṃ ṭhapetvā saññākkhandhaṃ ṭhapetvā viññāṇakkhandhaṃ"
THAP_RV = THAP_R.replace("кроме ", "кроме " + S.spell("Ka.", "thapetvā") + " ", 1)
KUSALA_P = "ime dhammā kusalā"
KUSALA_R = S.A_KUSALA[:-1]                    # это благие явления
assert S.CLOSE_OTHERS == cap(YVP_R) + ", – " + KUSALA_R + "."


def this_ru(m):
    return f"это {name(m.group(2))} {TS}"


def tail_ru(t):
    t = t.replace(YVP_P + " " + THAP_PV, YVP_R + ", " + THAP_RV)
    t = t.replace(YVP_P + " " + THAP_P, YVP_R + ", " + THAP_R)
    t = t.replace(YVP_P, YVP_R)
    t = re.sub(r"(?<!\S)(ayaṃ|idaṃ|ime|imāni|imā) tasmiṃ samaye (.+?) (hoti|honti)", this_ru, t)
    t = t.replace(KUSALA_P, KUSALA_R)
    t = t.replace(PE, ELL)
    t = re.sub(r",? – ", ", – ", t)
    return t


# =========================================================================================
# 4. Lists
# =========================================================================================
def there_list(s):
    """'phasso hoti, vedanā hoti…pe… avikkhepo hoti' -> 'есть контакт, есть чувство… есть …'.
    A missing comma between two «… hoti» items (source slip) is rendered as meant (comma)."""
    parts = re.split(r"(?:(?<=hoti)|(?<=honti))(…pe…\s*|,\s*|\s+)", s.strip())
    out = []
    for i, p in enumerate(parts):
        if i % 2:
            out.append(ELL + " " if PE in p else ", ")
        else:
            m = re.fullmatch(r"(.+) (hoti|honti)", p)
            out.append("есть " + name(m.group(1)))
    return "".join(out)


def name_list(s):
    """'Phasso cetanā…pe… avikkhepo' / 'Vedanākkhandho, saññākkhandho' -> Russian names with commas"""
    parts = re.split(r"(…pe…\s*|,\s*|\s+)", s.strip())
    out = []
    for i, p in enumerate(parts):
        if i % 2:
            out.append(ELL + " " if PE in p else ", ")
        else:
            out.append(name(p))
    return cap("".join(out))


# =========================================================================================
# 5. Q/A frames (Koṭṭhāsavāra, Suññatavāra, «Katamo tasmiṃ samaye X hoti?» lines)
# =========================================================================================
QRE = re.compile(r"Katam(?:o|ā|aṃ|e|āni) tasmiṃ samaye (.+?) (hoti|honti)(\?|…pe…)\s*(.*)$")
ARE = re.compile(r"(?:Yo|Yā|Yaṃ) tasmiṃ samaye (.+?) – ((?:ayaṃ|idaṃ) tasmiṃ samaye .+)$")
JRE = re.compile(r"Yo tesaṃ arūpīnaṃ dhammānaṃ (.+?) – (idaṃ tasmiṃ samaye .+)$")
LRE = re.compile(r"(.+?)(\s–\s.*|;.*|\.)$")


def answer_ru(a):
    m = ARE.fullmatch(a)
    if m:
        s, rest = m.groups()
        if s == HIRI_P:
            bod = S.HIRI_BODY
        elif s == OTTAPPA_P:
            bod = S.OTTAPPA_BODY
        else:
            bod = f"То, что {TS} есть {STR[s]}"
        return bod + ", – " + tail_ru(rest)
    m = JRE.fullmatch(a)
    if m:
        s, rest = m.groups()
        assert s == JIVITA_P, s
        return f"То, что у этих нематериальных явлений есть {S_JIVITA_PLAIN}, – " + tail_ru(rest)
    m = LRE.fullmatch(a)
    names, rest = m.groups()
    return name_list(names) + tail_ru(rest)


def qa_ru(line):
    m = QRE.fullmatch(line)
    nm, _verb, mark, rest = m.groups()
    q = f"Что такое {name(nm)} {TS}"
    if mark == "?":
        return q + "? " + answer_ru(rest)
    return q + ELL + " " + tail_ru(rest)


def summary_ru(line):
    """'Tasmiṃ kho pana samaye cattāro khandhā honti, …; ye vā pana …' (Koṭṭhāsa/Suññata summaries)"""
    body = line[len("Tasmiṃ kho pana samaye "):]
    items, rest = body.split(";", 1)
    return f"И вот {TS} " + there_list(items) + ";" + tail_ru(rest)


# =========================================================================================
# 6. «Katame dhammā kusalā? Yasmiṃ samaye …» sentences
# =========================================================================================
SIGLA = {"sī.": "Sī.", "syā.": "Syā.", "ka.": "Ka.", "bahūsu": "во многих изданиях"}


def var_ru(br):
    """[word (sī. syā.)] -> [вариант написания (Sī., Syā.): word] (all variants here are spelling-only)"""
    m = re.fullmatch(r"\[(.+?) \(([^)]*)\)\]", br)
    words, sig = m.groups()
    sig = sig.strip()
    return S.spell(SIGLA[sig] if sig in SIGLA else ", ".join(SIGLA[s] for s in sig.split()), words)


def vars_in(text):
    return re.sub(r"\[[^\]]*\]", lambda m: var_ru(m.group(0)), text)


ORD = {"paṭhamaṃ": ("в", "первое"), "dutiyaṃ": ("во", "второе"), "tatiyaṃ": ("в", "третье"),
       "catutthaṃ": ("в", "четвёртое"), "pañcamaṃ": ("в", "пятое")}
JH = "медитативное погружение"

# piece kinds:
#   part  participial phrase (set off by commas)          pp    adverbial prepositional phrase
#   fin   finite clause (видит …)                          fin3  the third-absorption clause
#   conj  piece that starts with «и, …»                    enter «входит в … погружение … и пребывает в нём»
#   jh    bare absorption name in a …pe… run               desc  description of the absorption (neuter)
#   attr  attribute of the mind (masculine, sense-sphere sentences)
# (kind, russian, lead_comma): lead_comma = the piece opens with a participial phrase («и, …»)
Q_ = {"sukh": "с восторгом и счастьем, рождёнными уединением",
      "samj": "с восторгом и счастьем, рождёнными сосредоточением"}
QUALS_1 = ["с направленной мыслью и удержанием мысли", Q_["sukh"]]
QUALS_2 = ["с ясностью внутри себя", "с единением ума", "без направленной мысли и без удержания мысли",
           Q_["samj"]]
QUALS_2V = ["без направленной мысли, только с удержанием мысли", Q_["samj"]]
QUALS_4 = ["которое ни болезненно, ни приятно", "с чистотой невозмутимости и осознанности"]
PART_KAMA = ("part", "полностью уединившись от чувственных удовольствий", True)
PP_VITAKKA = ("pp", "с затиханием направленной мысли и удержания мысли", False)
PP_PITI = ("pp", "с угасанием восторга", False)
PP_SUKHA = ("pp", "с устранением приятного", False)
FIN3 = ("fin3", "с угасанием восторга пребывает невозмутимым, осознанным и ясно понимающим, испытывает "
                "телом счастье, о котором благородные говорят – «Невозмутимый, осознанный, пребывающий в "
                "счастье»", False)
SEEN = "не воспринимая материальную форму внутри себя, видит вовне"
ABHIBHU = ("conj", "и, преодолев их с мыслью «Я знаю, я вижу»", False)


def colours(adj_pl, adj_gen, adj_ins):
    return f"{adj_pl}, {adj_gen} цвета, {adj_gen} вида, с {adj_ins} сиянием"


COL = {"nīl": colours("синие", "синего", "синим"), "pīt": colours("жёлтые", "жёлтого", "жёлтым"),
       "lohitak": colours("красные", "красного", "красным"), "odāt": colours("белые", "белого", "белым")}


def col_p(stem):
    return f"{stem}āni {stem}avaṇṇāni {stem}anidassanāni {stem}anibhāsāni"


def enter(o, quals=()):
    return ("enter", o, list(quals))


PIECES = {   # Pāli word sequence -> list of pieces (jhāna sentences)
    # --- the absorption formulas, in full
    "vivicceva kāmehi vivicca akusalehi dhammehi savitakkaṃ savicāraṃ vivekajaṃ pītisukhaṃ paṭhamaṃ jhānaṃ "
    "upasampajja viharati":
        [("part", "полностью уединившись от чувственных удовольствий, уединившись от неблагих явлений", True),
         enter("paṭhamaṃ", QUALS_1)],
    "vitakkavicārānaṃ vūpasamā ajjhattaṃ sampasādanaṃ cetaso ekodibhāvaṃ avitakkaṃ avicāraṃ samādhijaṃ "
    "pītisukhaṃ dutiyaṃ jhānaṃ upasampajja viharati":
        [PP_VITAKKA, enter("dutiyaṃ", QUALS_2)],
    "pītiyā ca virāgā upekkhako ca viharati sato ca sampajāno sukhañca kāyena paṭisaṃvedeti yaṃ taṃ ariyā "
    "ācikkhanti – \"upekkhako satimā sukhavihārī\"ti tatiyaṃ jhānaṃ upasampajja viharati":
        [FIN3, enter("tatiyaṃ")],
    "sukhassa ca pahānā dukkhassa ca pahānā pubbeva somanassadomanassānaṃ atthaṅgamā adukkhamasukhaṃ "
    "upekkhāsatipārisuddhiṃ catutthaṃ jhānaṃ upasampajja viharati":
        [("pp", "с устранением приятного и с устранением болезненного, с исчезновением ещё прежде радости "
                "и уныния", False), enter("catutthaṃ", QUALS_4)],
    "avitakkaṃ vicāramattaṃ samādhijaṃ pītisukhaṃ dutiyaṃ jhānaṃ upasampajja viharati":
        [enter("dutiyaṃ", QUALS_2V)],
    # --- opening words only (before …pe…)
    "vivicceva kāmehi": [PART_KAMA],
    "vitakkavicārānaṃ vūpasamā": [PP_VITAKKA],
    "pītiyā ca virāgā": [PP_PITI],
    "sukhassa ca pahānā": [PP_SUKHA],
    # --- bases of mastery and liberations
    "ajjhattaṃ arūpasaññī bahiddhā rūpāni passati": [("fin", SEEN + " видимые формы", True)],
    "ajjhattaṃ arūpasaññī bahiddhā rūpāni passati parittāni":
        [("fin", SEEN + " ограниченные видимые формы", True)],
    "ajjhattaṃ arūpasaññī bahiddhā rūpāni passati appamāṇāni":
        [("fin", SEEN + " безмерные видимые формы", True)],
    "ajjhattaṃ arūpasaññī bahiddhā rūpāni passati parittāni suvaṇṇadubbaṇṇāni":
        [("fin", SEEN + " ограниченные видимые формы, красивые и некрасивые", True)],
    "ajjhattaṃ arūpasaññī bahiddhā rūpāni passati appamāṇāni suvaṇṇadubbaṇṇāni":
        [("fin", SEEN + " безмерные видимые формы, красивые и некрасивые", True)],
    "ajjhattaṃ arūpasaññī bahiddhā rūpāni passati " + col_p("nīl"):
        [("fin", SEEN + " видимые формы, " + COL["nīl"], True)],
    "ajjhattaṃ arūpasaññī bahiddhā rūpāni passati " + col_p("pīt"):
        [("fin", SEEN + " видимые формы, " + COL["pīt"], True)],
    col_p("lohitak"): [("attr", COL["lohitak"], False)],
    col_p("odāt"): [("attr", COL["odāt"], False)],
    "tāni abhibhuyya jānāmi passāmīti": [ABHIBHU],
    "rūpī rūpāni passati": [("fin", "обладая материальной формой, видит видимые формы", True)],
    "subhanti": [("pp", "с мыслью «Прекрасно»", False)],
    # --- the immaterial absorptions
    "sabbaso rūpasaññānaṃ samatikkamā paṭighasaññānaṃ atthaṅgamā nānattasaññānaṃ amanasikārā":
        [("pp", "с полным преодолением восприятий материальной формы, с исчезновением восприятий "
                "соударения, без внимания к восприятиям разнообразия", False)],
    "ākāsānañcāyatanasaññāsahagataṃ":
        [("pp", "в сопровождении восприятия сферы бесконечного пространства", False)],
    "viññāṇañcāyatanasaññāsahagataṃ":
        [("pp", "в сопровождении восприятия сферы бесконечного сознания", False)],
    "ākiñcaññāyatanasaññāsahagataṃ":
        [("pp", "в сопровождении восприятия сферы отсутствия чего-либо", False)],
    "nevasaññānāsaññāyatanasaññāsahagataṃ":
        [("pp", "в сопровождении восприятия сферы ни восприятия, ни невосприятия", False)],
    "sabbaso ākāsānañcāyatanaṃ samatikkamma":
        [("part", "полностью преодолев сферу бесконечного пространства", True)],
    "sabbaso viññāṇañcāyatanaṃ samatikkamma":
        [("part", "полностью преодолев сферу бесконечного сознания", True)],
    "sabbaso ākiñcaññāyatanaṃ samatikkamma":
        [("part", "полностью преодолев сферу отсутствия чего-либо", True)],
}
for _p in ORD:
    PIECES[f"{_p} jhānaṃ upasampajja viharati"] = [enter(_p)]
    PIECES[f"{_p} jhānaṃ"] = [("jh", f"{ORD[_p][1]} {JH}{{V}}", False)]

# descriptions of the absorption (neuter, agree with «погружение»)
DESC_N = {
    "pathavīkasiṇaṃ": "со всеохватным объектом земли",
    "āpokasiṇaṃ": "со всеохватным объектом воды",
    "tejokasiṇaṃ": "со всеохватным объектом огня",
    "vāyokasiṇaṃ": "со всеохватным объектом ветра",
    "nīlakasiṇaṃ": "с синим всеохватным объектом",
    "pītakasiṇaṃ": "с жёлтым всеохватным объектом",
    "lohitakasiṇaṃ": "с красным всеохватным объектом",
    "odātakasiṇaṃ": "с белым всеохватным объектом",
    "dukkhapaṭipadaṃ dandhābhiññaṃ": "с трудным способом практики{V} и медленным высшим знанием",
    "dukkhapaṭipadaṃ khippābhiññaṃ": "с трудным способом практики{V} и быстрым высшим знанием",
    "sukhapaṭipadaṃ dandhābhiññaṃ": "с лёгким способом практики{V} и медленным высшим знанием",
    "sukhapaṭipadaṃ khippābhiññaṃ": "с лёгким способом практики{V} и быстрым высшим знанием",
    "parittaṃ parittārammaṇaṃ": "ограниченное и с ограниченным объектом",
    "parittaṃ appamāṇārammaṇaṃ": "ограниченное и с безмерным объектом",
    "appamāṇaṃ parittārammaṇaṃ": "безмерное и с ограниченным объектом",
    "appamāṇaṃ appamāṇārammaṇaṃ": "безмерное и с безмерным объектом",
    "mettāsahagataṃ": "сопровождаемое доброжелательностью",
    "karuṇāsahagataṃ": "сопровождаемое состраданием",
    "muditāsahagataṃ": "сопровождаемое сорадованием",
    "upekkhāsahagataṃ": "сопровождаемое невозмутимостью",
    "uddhumātakasaññāsahagataṃ": "сопровождаемое восприятием вздувшегося трупа",
    "vinīlakasaññāsahagataṃ": "сопровождаемое восприятием посиневшего трупа",
    "vipubbakasaññāsahagataṃ": "сопровождаемое восприятием гноящегося трупа",
    "vicchiddakasaññāsahagataṃ": "сопровождаемое восприятием разрубленного трупа",
    "vikkhāyitakasaññāsahagataṃ": "сопровождаемое восприятием объеденного трупа",
    "vikkhittakasaññāsahagataṃ": "сопровождаемое восприятием разбросанного трупа",
    "hatavikkhittakasaññāsahagataṃ": "сопровождаемое восприятием изрубленного и разбросанного трупа",
    "lohitakasaññāsahagataṃ": "сопровождаемое восприятием кровоточащего трупа",
    "puḷavakasaññāsahagataṃ": "сопровождаемое восприятием кишащего червями трупа",
    "aṭṭhikasaññāsahagataṃ": "сопровождаемое восприятием скелета",
    "hīnaṃ": "низшее",
    "majjhimaṃ": "среднее",
    "paṇītaṃ": "высшее",
}
ADHIP = {"chandādhipateyyaṃ": "с преобладанием желания", "vīriyādhipateyyaṃ": "с преобладанием усердия",
         "cittādhipateyyaṃ": "с преобладанием ума", "vīmaṃsādhipateyyaṃ": "с преобладанием пытливости"}
DESC_N.update(ADHIP)
for _k, _v in DESC_N.items():
    PIECES[_k] = [("desc", _v, False)]

# attributes of the sense-sphere mind (masculine, agree with «ум»)
OBJ_FULL_P = ("rūpārammaṇaṃ vā saddārammaṇaṃ vā gandhārammaṇaṃ vā rasārammaṇaṃ vā phoṭṭhabbārammaṇaṃ vā "
              "dhammārammaṇaṃ vā yaṃ yaṃ vā panārabbha")
OBJ_FULL_R = ("имеющий объектом видимую форму, или звук, или запах, или вкус, или осязаемое, или объект ума, "
              "или что бы то ни было")
ATTR_M = {
    "somanassasahagataṃ ñāṇasampayuttaṃ": "сопровождаемый радостью, связанный со знанием",
    "somanassasahagataṃ ñāṇavippayuttaṃ": "сопровождаемый радостью, не связанный со знанием",
    "upekkhāsahagataṃ ñāṇasampayuttaṃ": "сопровождаемый невозмутимостью, связанный со знанием",
    "upekkhāsahagataṃ ñāṇavippayuttaṃ": "сопровождаемый невозмутимостью, не связанный со знанием",
    "sasaṅkhārena": "с побуждением",
    OBJ_FULL_P: OBJ_FULL_R,
    "rūpārammaṇaṃ vā": "имеющий объектом видимую форму",
    "dhammārammaṇaṃ vā yaṃ yaṃ vā panārabbha": "или объект ума, или что бы то ни было",
    "hīnaṃ": "низший",
    "majjhimaṃ": "средний",
    "paṇītaṃ": "высший",
}
ATTR_M.update(ADHIP)
KAMA_P = "kāmāvacaraṃ kusalaṃ cittaṃ uppannaṃ hoti "
KAMA_R = "В то время, когда возникает благой ум, относящийся к миру чувственных желаний"
INTROS = {
    "rūpūpapattiyā maggaṃ bhāveti ": "В то время, когда кто-либо развивает путь к рождению в мире форм",
    "arūpūpapattiyā maggaṃ bhāveti ": "В то время, когда кто-либо развивает путь к рождению в мире без форм",
}
assert S.OPEN_1 == KAMA_R + ", " + ATTR_M["somanassasahagataṃ ñāṇasampayuttaṃ"] + ", " + OBJ_FULL_R + ","


def words_of(part):
    """split a pe-free Pāli chunk into [word, [variants]]"""
    words = []
    for t in re.findall(r"\[[^\]]*\]|[^\s\[]+", part):
        if t.startswith("["):
            words[-1][1].append(var_ru(t))
        else:
            words.append([t.rstrip(","), []])
    return words


def match(words, table):
    """greedy longest match; returns [(key, variants)]"""
    mx = max(len(k.split()) for k in table)
    res, i = [], 0
    while i < len(words):
        for L in range(min(mx, len(words) - i), 0, -1):
            key = " ".join(w for w, _ in words[i:i + L])
            if key in table:
                break
        else:
            raise KeyError("phrase: " + " ".join(w for w, _ in words[i:]))
        res.append((key, " ".join(v for _, vv in words[i:i + L] for v in vv)))
        i += L
    return res


def put_v(text, v):
    if "{V}" in text:
        return text.replace("{V}", " " + v if v else "")
    return text + (" " + v if v else "")


def render_enter(o, quals, v):
    prep, word = ORD[o]
    s = f"входит {prep} {word} {JH}" + (" " + v if v else "")
    if quals:
        s += ", " + ", ".join(quals) + ","
    return s + " и пребывает в нём"


def chunk_pieces(part):
    """one pe-free chunk -> list of (kind, text, lead_comma); an «enter» absorbs the descriptions after it"""
    out = []
    for key, v in match(words_of(part), PIECES):
        takers = [p for p in PIECES[key] if p[0] in ("enter", "jh", "desc")]
        assert not v or len(takers) == 1, ("variant without a place", key)
        for p in PIECES[key]:
            pv = v if p in takers else ""
            if p[0] == "enter":
                out.append(["enter", p[1], list(p[2]), pv])
            elif p[0] == "desc" and out and out[-1][0] == "enter":
                out[-1][2].append(put_v(p[1], pv))
            elif p[0] in ("jh", "desc"):
                out.append([p[0], put_v(p[1], pv), p[2]])
            else:
                out.append([p[0], p[1], p[2]])
    res = []
    for p in out:
        if p[0] == "enter":
            res.append(("enter", render_enter(p[1], p[2], p[3]), False))
        else:
            res.append(tuple(p))
    return res


def join(prev, nxt):
    pk, nk = prev[0], nxt[0]
    if nk == "conj":   # a detached attribute list before «и, преодолев …» closes with a comma
        detached = pk == "attr" or prev[1].endswith(("некрасивые", "сиянием"))
        return ", " if detached else " "
    if pk in ("fin", "attr") and nk in ("part", "pp", "enter"):
        return " и, " if nxt[2] else " и "
    if pk == "fin3" and nk == "enter":
        return ", и "
    if pk == "pp" and nk == "enter":
        return " "
    return ", "


def x_jh(x):
    out, prev, first = [], None, True
    for i, part in enumerate(re.split(r"(\s*…pe…\s*)", x)):
        if i % 2:
            out.append(ELL + " ")
            prev = None
            continue
        if not part.strip():
            continue
        for p in chunk_pieces(part):
            if first:
                out.append((" и, " if p[2] else " и ") + p[1])
                first = False
            elif prev is None:
                out.append(p[1])
            else:
                out.append(join(prev, p) + p[1])
            prev = p
    return "".join(out)


def x_kama(x):
    out = []
    for i, part in enumerate(re.split(r"(\s*…pe…\s*)", x)):
        if i % 2:
            out.append(ELL + " ")
        elif part.strip():
            res = []
            for key, v in match(words_of(part), ATTR_M):
                assert not v
                res.append(ATTR_M[key])
            out.append(", ".join(res))
    return "".join(out)


def kusala_ru(line):
    body = line[len("Katame dhammā kusalā? Yasmiṃ samaye "):]
    if body.startswith(KAMA_P):
        body, intro, xf = body[len(KAMA_P):], KAMA_R + ", ", x_kama
    else:
        for p, r in INTROS.items():
            if body.startswith(p):
                body, intro, xf = body[len(p):], r, x_jh
                break
        else:
            raise KeyError("intro: " + body[:60])
    idx = body.index(" tasmiṃ samaye ")
    x, rest = body[:idx].rstrip(), body[idx + len(" tasmiṃ samaye "):]
    if x.endswith(DASH):
        sep, x = ", " + DASH, x[:-1].rstrip()
    else:
        sep = ","        # «,» in the Pāli; a missing comma (^1-189) is rendered as meant
        x = x[:-1] if x.endswith(",") else x
    m = re.fullmatch(r"(.*? hoti)(…pe… ime dhammā kusalā.*|; ye vā pana.*)", rest)
    return (S.Q_KUSALA + " " + intro + xf(x) + sep + f" {TS} " + there_list(m.group(1))
            + tail_ru(m.group(2)))


# =========================================================================================
# 7. Headings and closing lines (exact)
# =========================================================================================
SIXTEEN = "в шестнадцатикратном разборе"
H_RUPA_KUSALA = "Благой ум, относящийся к миру форм"
H_ARUPA_KUSALA = "Благой ум, относящийся к миру без форм"
BRAHMA = "Четыре медитативных погружения божественных обителей"
ASUBHA = "Медитативное погружение на основе непривлекательного"
ARUPA4 = "Четыре медитативных погружения мира без форм"
EXACT = {
    # 2-01
    "##### Koṭṭhāsavāro": "##### Раздел составных частей",
    "Koṭṭhāsavāro.": "Раздел составных частей.",
    "##### Suññatavāro": "##### Раздел пустоты",
    "Suññatavāro.": "Раздел пустоты.",
    "Paṭhamaṃ cittaṃ.": "Первый вид ума.",
    "Dutiyaṃ cittaṃ.": "Второй вид ума.",
    "Tatiyaṃ cittaṃ.": "Третий вид ума.",
    "Catutthaṃ cittaṃ.": "Четвёртый вид ума.",
    "Pañcamaṃ cittaṃ.": "Пятый вид ума.",
    "Chaṭṭhaṃ cittaṃ.": "Шестой вид ума.",
    "Sattamaṃ cittaṃ.": "Седьмой вид ума.",
    "Aṭṭhamaṃ cittaṃ.": "Восьмой вид ума.",
    "Aṭṭha kāmāvacaramahākusalacittāni.": "Восемь великих благих видов ума, относящихся к миру чувственных желаний.",
    "Dutiyabhāṇavāro.": "Второй раздел для чтения вслух.",
    # 2-02
    "#### Rūpāvacarakusalaṃ": f"#### {H_RUPA_KUSALA}",
    "#### Arūpāvacarakusalaṃ": f"#### {H_ARUPA_KUSALA}",
    "#### Tebhūmakakusalaṃ": "#### Благой ум трёх миров",
    "##### Kāmāvacarakusalaṃ": f"##### {S.H_KAMA_KUSALA}",
    "##### Rūpāvacarakusalaṃ": f"##### {H_RUPA_KUSALA}",
    "##### Arūpāvacarakusalaṃ": f"##### {H_ARUPA_KUSALA}",
    "Kāmāvacarakusalaṃ.": f"{S.H_KAMA_KUSALA}.",
    "Rūpāvacarakusalaṃ.": f"{H_RUPA_KUSALA}.",
    "Arūpāvacarakusalaṃ.": f"{H_ARUPA_KUSALA}.",
    "##### Catukkanayo": "##### Четверичный метод",
    "Catukkanayo.": "Четверичный метод.",
    "##### Pañcakanayo": "##### Пятеричный метод",
    "Pañcakanayo.": "Пятеричный метод.",
    "##### Catasso paṭipadā": "##### Четыре способа практики",
    "Catasso paṭipadā.": "Четыре способа практики.",
    "##### Cattāri ārammaṇāni": "##### Четыре вида объектов",
    "Cattāri ārammaṇāni.": "Четыре вида объектов.",
    "##### Dve ārammaṇāni": "##### Два вида объектов",
    "Dve ārammaṇāni.": "Два вида объектов.",
    "##### Soḷasakkhattukaṃ": "##### Шестнадцатикратный разбор",
    "Soḷasakkhattukaṃ.": "Шестнадцатикратный разбор.",
    "##### Aṭṭhakkhattukaṃ": "##### Восьмикратный разбор",
    "Aṭṭhakkhattukaṃ.": "Восьмикратный разбор.",
    "##### Idampi aṭṭhakkhattukaṃ": "##### Это тоже восьмикратный разбор",
    "Idampi aṭṭhakkhattukaṃ.": "Это тоже восьмикратный разбор.",
    "##### Aparampi aṭṭhakkhattukaṃ": "##### Ещё один восьмикратный разбор",
    "Aparampi aṭṭhakkhattukaṃ.": "Ещё один восьмикратный разбор.",
    "##### Aṭṭhakasiṇaṃ soḷasakkhattukaṃ": f"##### Восемь всеохватных объектов {SIXTEEN}",
    "Aṭṭhakasiṇaṃ soḷasakkhattukaṃ.": f"Восемь всеохватных объектов {SIXTEEN}.",
    "##### Abhibhāyatanāni parittāni": "##### Сферы преодоления: ограниченные видимые формы",
    "##### Appamāṇāni": "##### Безмерные видимые формы",
    "Imānipi abhibhāyatanāni soḷasakkhattukāni.": f"Это тоже сферы преодоления {SIXTEEN}.",
    "##### Tīṇi vimokkhāni soḷasakkhattukāni": f"##### Три освобождения {SIXTEEN}",
    "Imānipi tīṇi vimokkhāni soḷasakkhattukāni.": f"Это тоже три освобождения {SIXTEEN}.",
    "##### Cattāri brahmavihārajhānāni soḷasakkhattukāni": f"##### {BRAHMA} {SIXTEEN}",
    "Cattāri brahmavihārajhānāni [brahmavihārajjhānāni (sī. syā.)] soḷasakkhattukāni.":
        f"{BRAHMA} {S.spell('Sī., Syā.', 'brahmavihārajjhānāni')} {SIXTEEN}.",
    "##### Asubhajhānaṃ soḷasakkhattukaṃ": f"##### {ASUBHA} {SIXTEEN}",
    "Asubhajhānaṃ [asubhajjhānaṃ (sī. syā.)] soḷasakkhattukaṃ.":
        f"{ASUBHA} {S.spell('Sī., Syā.', 'asubhajjhānaṃ')} {SIXTEEN}.",
    "##### Cattāri arūpajhānāni [arūpajjhānāni (sī. syā.)] soḷasakkhattukāni":
        f"##### {ARUPA4} {S.spell('Sī., Syā.', 'arūpajjhānāni')} {SIXTEEN}",
    "Cattāri arūpajhānāni soḷasakkhattukāni.": f"{ARUPA4} {SIXTEEN}.",
}


# =========================================================================================
# 8. Line dispatch, segments, build
# =========================================================================================
def translate_line(line):
    if line in EXACT:
        return EXACT[line]
    if line.startswith("Katame dhammā kusalā? Yasmiṃ samaye "):
        return kusala_ru(line)
    if line.startswith("Tasmiṃ kho pana samaye "):
        return summary_ru(line)
    if QRE.fullmatch(line):
        return qa_ru(line)
    if line.startswith("Ye vā pana ") or re.match(r"(Ime|Imāni|Imā|Idaṃ|Ayaṃ) tasmiṃ samaye ", line):
        return cap(tail_ru(line[0].lower() + line[1:]))
    raise KeyError("line: " + line[:80])


PALI_CHARS = set("āīūṃṅñṭḍṇḷ") | set("abcdefghijklmnopqrstuvwxyz")


def check_ru(r):
    bare = re.sub(r"\[[^\]]*\]", "", r).lower()
    bad = PALI_CHARS & set(bare)
    assert not bad, (bad, r[:160])
    assert "—" not in r and ":-" not in r, r[:80]


def render(segs):
    blocks = []
    for sid, plines in segs:
        rlines = []
        for p in plines:
            r = cap(translate_line(p))
            check_ru(r)
            assert len(p) - len(p.lstrip("#")) == len(r) - len(r.lstrip("#")), sid
            assert p.count("–") + p.count("—") == r.count("–"), ("dash", sid, p[:60], r[:60])
            rlines.append(r)
        rlines[-1] += f" ^{sid}"
        blocks.append("\n".join(rlines))
    return blocks


def segments(path):
    out, buf = [], []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        m = S.ID.search(line)
        if m:
            buf.append(line[:m.start()].rstrip())
            out.append((m.group(1), buf))
            buf = []
        else:
            buf.append(line)
    assert not buf
    return out


def selftest():
    """Run the translators on the sample's Pāli; every line must equal the approved sample except the
    lines with variant brackets or slips handled by hand there (^1-1, ^1-5, ^1-13, ^1-19, ^1-33, ^1-40)
    and the definitions in the kāya/citta frame (^1-40 … ^1-51, sample-only frame)."""
    pal = segments(S.PIPE / "ref" / "ch2-01-pali-1-122.md")
    ru = segments(SAMPLE)
    skip = {"1-1-0", "1-1-1-0", "1-1-1-1-0", "1-1", "1-5", "1-13", "1-19", "1-33", "1-57"}
    skip |= {f"1-{i}" for i in range(40, 52)}
    ok = bad = 0
    for (b, pl), (b2, rl) in zip(pal, ru):
        assert b == b2
        if b in skip:
            continue
        for p, r in zip(pl, rl):
            if cap(translate_line(p)) == r:
                ok += 1
            else:
                bad += 1
                print("SELFTEST MISMATCH", b, "\n  got:", cap(translate_line(p)), "\n  exp:", r)
    # ^1-57 line 1 is a normal definition; lines 2-4 are closings
    p57, r57 = pal[-1][1], ru[-1][1]
    assert cap(translate_line(p57[0])) == r57[0] and cap(translate_line(p57[1])) == r57[1]
    print(f"selftest: {ok + 2} lines identical to the approved sample, {bad} mismatches")
    return bad == 0


def build_2_01():
    segs = segments(PALI / "2-01-cittuppadakandam.md")
    ids = [b for b, _ in segs]
    k = ids.index("1-57") + 1
    sample = SAMPLE.read_bytes().decode("utf-8")
    assert sample.endswith(" ^1-57\n") and "\r" not in sample
    return sample + "\n" + "\n\n".join(render(segs[k:])) + "\n", len(segs)


def build_2_02():
    segs = segments(PALI / "2-02-cittuppadakandam.md")
    return "\n\n".join(render(segs)) + "\n", len(segs)


def notes():
    """New recurring formulas of 2-01/2-02 (Pāli = Russian), generated from the tables above."""
    sample_names = set(S.FN)
    L = ["# pi-1 Russian rails: new formulas of 2-01 (after ^1-57) and 2-02", "",
         "Generated by build_rails_2-01_2-02_ru.py from its fixed strings; import that file instead of "
         "retyping. Strings already in ru-rails-formulas.md are not repeated.", "",
         "## Frames", "",
         f"Tasmiṃ kho pana samaye X hoti/honti, …; ye vā pana … = И вот {TS} есть X, …; {YVP_R}, – …",
         f"Katamo/Katamā/Katamaṃ/Katame/Katamāni tasmiṃ samaye X hoti/honti? = Что такое X {TS}?",
         f"ayaṃ/idaṃ/ime/imāni/imā tasmiṃ samaye X hoti/honti = это X {TS}",
         f"Ime/Imāni/Imā/Idaṃ/Ayaṃ tasmiṃ samaye X honti/hoti. (own line) = Это X {TS}.",
         f"Katamo tasmiṃ samaye X hoti…pe… ayaṃ tasmiṃ samaye X hoti. = Что такое X {TS}… это X {TS}.",
         "Name lists (Phasso cetanā … / Vedanākkhandho, saññākkhandho …) = names joined with «, », first capitalised",
         f"Name list – idaṃ tasmiṃ samaye X hoti. = Name list, – это X {TS}.",
         f"{YVP_P} {THAP_P} = {YVP_R}, {THAP_R}",
         f"(^1-62 with variant) = {YVP_R}, {THAP_RV}",
         f"Yo tesaṃ arūpīnaṃ dhammānaṃ {JIVITA_P} – = То, что у этих нематериальных явлений есть {S_JIVITA_PLAIN}, –",
         f"– ime dhammā kusalā…pe…. = , – {KUSALA_R}….",
         "…pe… = … ; a missing comma between «X hoti Y hoti» (^1-150, ^1-165) and before «tasmiṃ samaye» (^1-189) "
         "is rendered as meant (comma); a space before «…pe…» is dropped",
         "", "## Synonym strings", ""]
    for p, r in STR.items():
        if r not in (S.S_PHASSA, S.S_SUKHA, S.S_VEDANA, S.S_SANNA, S.S_CITTA, S.S_VITAKKA, S.S_VICARA, S.S_PITI,
                     S.S_SAMADHI, S.S_SADDHA, S.S_VIRIYA, S.S_SATI, S.S_PANNA, S.S_AMOHA, S.S_ALOBHA, S.S_ADOSA):
            L.append(f"{p} = {r}")
    L += ["", "## Names (nominative)", ""]
    for p, r in NAMES.items():
        if p not in sample_names:
            L.append(f"{p} = {r}")
    L += ["", "## «Katame dhammā kusalā? Yasmiṃ samaye …» sentences", "",
          f"Yasmiṃ samaye kāmāvacaraṃ kusalaṃ cittaṃ uppannaṃ hoti … = {KAMA_R}, …",
          ]
    for p, r in INTROS.items():
        L.append(f"Yasmiṃ samaye {p.strip()} … = {r} и[,] …")
    L += [f"… tasmiṃ samaye (after the description) = …, {TS}  (after «–»: …, – {TS})",
          "Joining: the first piece after the intro follows «и» (« и, » before a participial phrase); "
          "«N jhānaṃ upasampajja viharati» + qualities and descriptions of the same …pe…-free stretch = "
          "«входит в N медитативное погружение[ вариант], качества, описания, и пребывает в нём»; "
          "descriptions after a «…» stand alone, separated by «…».",
          f"N jhānaṃ upasampajja viharati (no qualities) = {render_enter('paṭhamaṃ', [], '')} (N: "
          + ", ".join(f"{p} = {w}" for p, (_, w) in ORD.items()) + "; «во второе»)",
          f"N jhānaṃ (bare, in a …pe… run) = N {JH}"]
    for p, pcs in PIECES.items():
        if p in DESC_N or re.fullmatch(r"\S+ jhānaṃ(?: upasampajja viharati)?", p):
            continue
        out = []
        for pc in pcs:
            if pc[0] == "enter":
                out.append(render_enter(pc[1], pc[2], ""))
            else:
                out.append(pc[1])
        L.append(f"{p} = " + " | ".join(out))
    L += ["", "### Descriptions of the absorption (neuter)", ""]
    for p, r in DESC_N.items():
        L.append(f"{p} = {r.replace('{V}', '')}")
    L += ["", "### Attributes of the sense-sphere mind (masculine)", ""]
    for p, r in ATTR_M.items():
        L.append(f"{p} = {r}")
    L += ["", "## Headings and closing lines", ""]
    for p, r in EXACT.items():
        L.append(f"{p} = {r}")
    (HERE / "notes-2-01_2-02.md").write_text("\n".join(L) + "\n", encoding="utf-8", newline="\n")
    print("wrote", HERE / "notes-2-01_2-02.md")


def main():
    assert selftest()
    notes()
    for fn_name, fn in (("2-01-cittuppadakandam.md", build_2_01), ("2-02-cittuppadakandam.md", build_2_02)):
        text, n = fn()
        (OUT / fn_name).write_text(text, encoding="utf-8", newline="\n")
        print("wrote", OUT / fn_name, n, "segments")


if __name__ == "__main__":
    main()
