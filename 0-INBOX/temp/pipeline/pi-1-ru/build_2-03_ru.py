"""Build the Russian plain zero-shot of pi-1 part 2-03 (Lokuttarakusalaṃ, ^1-1-5-0 … ^1-364).

usage: python -I -X utf8 build_2-03_ru.py
Reuses the approved sample constants (build_ch2_01_sample_ru.py) and matrix frames (build_matika_ru.py)
unchanged; adds the formulas this part needs as fixed constants, so every repeat is byte-identical.
Every Pāli line is parsed and translated from fixed pieces; unknown material raises an error.
"""
import pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(HERE))
import build_matika_ru as M  # noqa: E402  (importing does not write files)
import build_ch2_01_sample_ru as C  # noqa: E402

PART = "2-03-cittuppadakandam.md"
PALI = ROOT / "AI_translation" / "pali" / "pi-1_split_chapters" / PART
OUT = ROOT / "AI_translation" / "russian" / "pi-1-russian-plain-zeroshot_split_chapters" / PART

DASH = C.DASH
PE = "…pe…"
ELL = "…"
TASMIM = C.TASMIM
KUSALA = C.KUSALA

# ---- factor names: sample names + new ones (nominative, instrumental) ----------------------
NAMES_C = dict(C.NAMES_C)
NEW_NAMES = {
    "anaññātaññassāmītindriyaṃ": ("способность познания непознанного", "способностью познания непознанного"),
    "aññindriyaṃ": ("способность окончательного знания", "способностью окончательного знания"),
    "sammāvācā": ("правильная речь", "правильной речью"),
    "sammākammanto": ("правильное действие", "правильным действием"),
    "sammāājīvo": ("правильный образ жизни", "правильным образом жизни"),
    "saṅkhārakkhandho": ("совокупность формирующих факторов", "совокупностью формирующих факторов"),
}
for k in NEW_NAMES:
    assert k not in NAMES_C, k
NAMES_C.update(NEW_NAMES)
N = {k: v[0] for k, v in NAMES_C.items()}
INS = {k: v[1] for k, v in NAMES_C.items()}

# ---- synonym strings: sample bases + suffix tokens ------------------------------------------
BASES = dict(C.STRINGS)
MAGGA = "фактор пути, принадлежащее к пути"  # maggaṅgaṃ maggapariyāpannaṃ


def BOJJH(gen):
    """X-sambojjhaṅgo = «фактор пробуждения X» (pi-5: satisambojjhaṅga = фактор пробуждения осознанности)."""
    return f"фактор пробуждения {gen}"


def ABST(obj):
    """'<obj> ārati virati paṭivirati veramaṇī akiriyā akaraṇaṃ anajjhāpatti velāanatikkamo setughāto'"""
    return (f"отстранение от {obj}, воздержание, полное воздержание, уклонение, неделание, несовершение, "
            "невпадение в проступок, непереступание границы, разрушение моста")


_ABST_PI = "ārati virati paṭivirati veramaṇī akiriyā akaraṇaṃ anajjhāpatti velāanatikkamo setughāto"
BASES.update({
    "catūhi vacīduccaritehi " + _ABST_PI: ABST("четырёх видов дурного поведения в речи"),
    "tīhi kāyaduccaritehi " + _ABST_PI: ABST("трёх видов дурного поведения телом"),
    "micchāājīvā " + _ABST_PI: ABST("неправильного образа жизни"),
})
TOKENS = {
    "maggaṅgaṃ maggapariyāpannaṃ": MAGGA,
    "pītisambojjhaṅgo": BOJJH("восторга"),
    "samādhisambojjhaṅgo": BOJJH("сосредоточения"),
    "vīriyasambojjhaṅgo": BOJJH("усердия"),
    "satisambojjhaṅgo": BOJJH("осознанности"),
    "dhammavicayasambojjhaṅgo": BOJJH("исследования явлений"),
    "passaddhisambojjhaṅgo": BOJJH("безмятежности"),
    "sammāvācā": N["sammāvācā"],
    "sammākammanto": N["sammākammanto"],
    "sammāājīvo": N["sammāājīvo"],
}
SHAME_STRINGS = {C.S_HIRI, C.S_OTTAPPA}


def tr_string(pi):
    """A bare synonym string: the longest matching base plus suffix tokens, comma-joined."""
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


# ---- answer qualifiers ------------------------------------------------------------------------
G_ANANNATA = ("для непосредственного постижения тех явлений, которые ещё не познаны, не увидены, "
              "не достигнуты, не узнаны и не постигнуты непосредственно")
G_ANNA = ("для непосредственного постижения тех явлений, которые познаны, увидены, достигнуты, "
          "узнаны и постигнуты непосредственно")
P_ANANNATA = "tesaṃ dhammānaṃ anaññātānaṃ adiṭṭhānaṃ appattānaṃ aviditānaṃ asacchikatānaṃ sacchikiriyāya "
P_ANNA = "tesaṃ dhammānaṃ ñātānaṃ diṭṭhānaṃ pattānaṃ viditānaṃ sacchikatānaṃ sacchikiriyāya "
PREFIXES = [
    (r"tajjāmanoviññāṇadhātusamphassaj(?:aṃ|ā) ", ", " + C.TAJJA + ","),
    (r"vedanākkhandhassa saññākkhandhassa saṅkhārakkhandhassa ", " " + C.G_KAYA),
    (r"viññāṇakkhandhassa ", " " + C.G_CITTA),
]

# ---- closing pieces -----------------------------------------------------------------------------
YEV_PI = "ye vā pana tasmiṃ samaye aññepi atthi paṭiccasamuppannā arūpino dhammā – ime dhammā "
ANS = M.ANSWER(KUSALA)            # «это благие явления.»
OR_YEV = "или же " + C.YEVAPANA()  # «или же любые другие …, – это благие явления.»
EXCEPT = "кроме совокупности чувств, кроме совокупности восприятия, кроме совокупности сознания"


def tr_tail(t):
    """The tail after '… X hoti' at the end of an answer or list."""
    if t == ".":
        return "."
    if t == "; " + YEV_PI + "kusalā.":
        return "; " + OR_YEV
    if t == PE + " ime dhammā kusalā.":
        return ELL + " " + ANS
    raise ValueError("unknown tail: " + repr(t))


# ---- question / answer lines ----------------------------------------------------------------------
QA_RX = re.compile(r"Katam(?:o|ā|aṃ) tasmiṃ samaye (\S+) hoti\? Y(?:o|ā|aṃ) (.*?) – (?:ayaṃ|idaṃ) "
                   r"tasmiṃ samaye (\S+) hoti(.*)")


def Q(key):
    return f"Что {TASMIM} является {INS[key]}?"


def ANSWER_END(key):
    return f"это и есть {N[key]} {TASMIM}"


def tr_qa(line):
    m = QA_RX.fullmatch(line)
    if not m:
        return None
    key, body, key2, tail = m.groups()
    assert key == key2, line
    if body.startswith("tasmiṃ samaye "):
        body = body[len("tasmiṃ samaye "):]
        mid = ""
        for rx, ru in PREFIXES:
            mm = re.match(rx, body)
            if mm:
                body, mid = body[mm.end():], ru
                break
        s = tr_string(body)
        if s in SHAME_STRINGS:
            assert not mid
            a = f"То, что {TASMIM} {s}, {DASH} {ANSWER_END(key)}"
        else:
            a = f"То, что {TASMIM}{mid} есть {s}, {DASH} {ANSWER_END(key)}"
    elif body.startswith("tesaṃ arūpīnaṃ dhammānaṃ "):
        s = tr_string(body[len("tesaṃ arūpīnaṃ dhammānaṃ "):])
        a = f"То, что {C.G_JIVITA} есть {s}, {DASH} {ANSWER_END(key)}"
    elif body.startswith(P_ANANNATA):
        s = tr_string(body[len(P_ANANNATA):])
        a = f"То, что {G_ANANNATA}, есть {s}, {DASH} {ANSWER_END(key)}"
    else:
        raise ValueError("unknown answer body: " + body)
    return Q(key) + " " + a + tr_tail(tail)


# the sample frames are reproduced exactly for the factors they cover
for _k, _s in (("phasso", C.S_PHASSA), ("vicāro", C.S_VICARA), ("saddhindriyaṃ", C.S_SADDHA)):
    assert f"{Q(_k)} То, что {TASMIM} есть {_s}, {DASH} {ANSWER_END(_k)}." == C.QA(_k, _s)
assert (f"{Q('vedanā')} То, что {TASMIM}, {C.TAJJA}, есть {C.S_SUKHA}, {DASH} {ANSWER_END('vedanā')}."
        == C.T("vedanā", C.S_SUKHA))
assert (f"{Q('kāyalahutā')} То, что {TASMIM} {C.G_KAYA} есть {C.S_LAHUTA}, {DASH} {ANSWER_END('kāyalahutā')}."
        == C.KAYA("kāyalahutā", C.S_LAHUTA))
assert (f"{Q('hirī')} То, что {TASMIM} {C.S_HIRI}, {DASH} {ANSWER_END('hirī')}." == C.SHAME("hirī", C.S_HIRI))
assert C.JIVITA("jīvitindriyaṃ", C.S_JIVITA) == (
    f"{Q('jīvitindriyaṃ')} То, что {C.G_JIVITA} есть {C.S_JIVITA}, {DASH} {ANSWER_END('jīvitindriyaṃ')}.")


# ---- lists of factors ------------------------------------------------------------------------------
def hoti_list(pali):
    """'phasso hoti, vedanā hoti, …, avikkhepo hoti' -> 'есть контакт, есть чувство, …'"""
    items = pali.split(" hoti, ")
    assert items[-1].endswith(" hoti"), pali
    items[-1] = items[-1][: -len(" hoti")]
    return ", ".join(f"есть {N[k]}" for k in items)


assert hoti_list("phasso hoti, vedanā hoti") == C.LIST_ITEM("phasso") + ", " + C.LIST_ITEM("vedanā")


def bare_list(pali):
    """'Phasso cetanā vitakko …' -> 'Контакт, намерение, направленная мысль, …'"""
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
    key = "saṅkhārakkhandho"
    return (f"{Q(key)} {bare_list(m.group(1))}; или же {C.YEVAPANA_BODY}, {EXCEPT}, {DASH} "
            f"{ANSWER_END(key)}" + tr_tail(m.group(2)))


# ---- 'Tasmiṃ kho pana samaye cattāro khandhā honti, …' ----------------------------------------------
SANGAHA_ITEMS = {
    "cattāro khandhā honti": "есть четыре совокупности",
    "dvāyatanāni honti": "есть две сферы восприятия",
    "dve dhātuyo honti": "есть два элемента",
    "tayo āhārā honti": "есть три вида питания",
    "navindriyāni honti": "есть девять способностей",
    "pañcaṅgikaṃ jhānaṃ hoti": "есть медитативное погружение из пяти факторов",
    "aṭṭhaṅgiko maggo hoti": "есть путь из восьми факторов",
    "satta balāni honti": "есть семь сил",
    "tayo hetū honti": "есть три корня",
    "eko phasso hoti": "есть один контакт",
    "ekā vedanā hoti": "есть одно чувство",
    "ekā saññā hoti": "есть одно восприятие",
    "ekā cetanā hoti": "есть одно намерение",
    "ekaṃ cittaṃ hoti": "есть один ум",
    "eko vedanākkhandho hoti": "есть одна совокупность чувств",
    "eko saññākkhandho hoti": "есть одна совокупность восприятия",
    "eko saṅkhārakkhandho hoti": "есть одна совокупность формирующих факторов",
    "eko viññāṇakkhandho hoti": "есть одна совокупность сознания",
    "ekaṃ manāyatanaṃ hoti": "есть одна сфера ума",
    "ekaṃ manindriyaṃ hoti": "есть одна способность ума",
    "ekā manoviññāṇadhātu hoti": "есть один элемент умственного сознания",
    "ekaṃ dhammāyatanaṃ hoti": "есть одна сфера объектов ума",
    "ekā dhammadhātu hoti": "есть один элемент объектов ума",
}
SANGAHA_HEAD_PI = "Tasmiṃ kho pana samaye "
SANGAHA_HEAD = "И в это время "


def tr_sangaha(line):
    if not line.startswith(SANGAHA_HEAD_PI + "cattāro khandhā honti"):
        return None
    body, tail = line[len(SANGAHA_HEAD_PI):].split("; ", 1)
    assert tail == YEV_PI + "kusalā" + PE + ".", tail
    items = ", ".join(SANGAHA_ITEMS[x] for x in body.split(", "))
    return SANGAHA_HEAD + items + "; " + OR_YEV[:-1] + ELL + "."


# ---- opening clauses ------------------------------------------------------------------------------
LEADS = "ведущее к освобождению и ведущее к убыванию"   # niyyānikaṃ apacayagāmiṃ (jhānaṃ, neuter)
LEADS_M = "ведущий к освобождению и ведущий к убыванию"  # the same after cittaṃ (masculine «ум»)
DEV_JHANA = f"человек развивает надмирское медитативное погружение, {LEADS}"
TWENTY_OBJ = [  # lokuttaraṃ X bhāveti (accusative)
    "надмирский путь", "надмирскую основу осознанности", "надмирское правильное усилие",
    "надмирскую основу сверхспособностей", "надмирскую способность", "надмирскую силу",
    "надмирский фактор пробуждения", "надмирскую истину", "надмирское успокоение", "надмирское явление",
    "надмирскую совокупность", "надмирскую сферу восприятия", "надмирский элемент", "надмирское питание",
    "надмирский контакт", "надмирское чувство", "надмирское восприятие", "надмирское намерение",
    "надмирский ум",
]
assert len(TWENTY_OBJ) == 19
DEV_TWENTY = ("человек развивает " + TWENTY_OBJ[0] + "".join(f"{ELL} развивает {o}" for o in TWENTY_OBJ[1:])
              + f", {LEADS_M}")
STAGE = {
    1: "для устранения приверженности воззрениям, для достижения первой ступени",
    2: "для ослабления чувственной страсти и недоброжелательности, для достижения второй ступени",
    3: "для полного устранения чувственной страсти и недоброжелательности, для достижения третьей ступени",
    4: ("для полного устранения страсти к миру форм, страсти к миру без форм, самомнения, беспокойства "
        "и неведения, для достижения четвёртой ступени"),
}
J = "медитативного погружения"
J1 = f"и, отстранившись от чувственных удовольствий{ELL} достигает первого {J} и пребывает в нём"
J5 = (f"и с успокоением направленной мысли и удержания мысли{ELL} второго {J}{ELL} третьего {J}{ELL} "
      f"четвёртого {J}{ELL} первого {J}{ELL} достигает пятого {J} и пребывает в нём")
IN_J = "в погружении"
PP = [
    "с болезненным способом практики и медленным высшим знанием",
    "с болезненным способом практики и быстрым высшим знанием",
    "с приятным способом практики и медленным высшим знанием",
    "с приятным способом практики и быстрым высшим знанием",
]
EMPTY = "пустом"                         # suññataṃ (agrees with «погружении»)
DESIRELESS = "свободном от устремлений"  # appaṇihitaṃ
ADHI = (ELL + " ").join(f"при преобладании {x}" for x in ("желания", "усердия", "ума", "исследования"))


def CL(qual, jh=J1, stage=1, dev=DEV_JHANA):
    """dev, stage, absorption, then the qualifiers of the absorption («в погружении …»)."""
    return f"{dev}, {STAGE[stage]} {jh}, {qual}"


def ALL4(suffix=""):
    return IN_J + " " + (ELL + " ").join(p + suffix for p in PP)


OPEN = {
    "1-277": CL(f"{IN_J} {PP[0]}"),
    "1-339": CL(f"{IN_J} {PP[1]}"),
    "1-340": CL(f"{IN_J} {PP[2]}"),
    "1-341": CL(f"{IN_J} {PP[3]}"),
    "1-342": CL(ALL4(), jh=J5),
    "1-343": CL(f"в {EMPTY} погружении"),
    "1-344": CL(f"в {EMPTY} погружении", jh=J5),
    "1-345": CL(f"{IN_J} {PP[0]}, {EMPTY}"),
    "1-346": CL(f"{IN_J} {PP[1]}, {EMPTY}"),
    "1-347": CL(f"{IN_J} {PP[2]}, {EMPTY}"),
    "1-348": CL(f"{IN_J} {PP[3]}, {EMPTY}"),
    "1-349": CL(ALL4(", " + EMPTY), jh=J5),
    "1-350": CL(f"{IN_J}, {DESIRELESS}"),
    "1-351": CL(f"{IN_J}, {DESIRELESS}", jh=J5),
    "1-352": CL(f"{IN_J} {PP[0]}, {DESIRELESS}"),
    "1-353": CL(f"{IN_J} {PP[1]}, {DESIRELESS}"),
    "1-354": CL(f"{IN_J} {PP[2]}, {DESIRELESS}"),
    "1-355": CL(f"{IN_J} {PP[3]}, {DESIRELESS}"),
    "1-356": CL(ALL4(", " + DESIRELESS), jh=J5),
    "1-357": CL(f"{IN_J} {PP[0]}", dev=DEV_TWENTY),
    "1-358": CL(f"{IN_J} {PP[0]}, {ADHI}"),
    "1-359": CL(f"{IN_J} {PP[0]}, {ADHI}", jh=J5),
    "1-360": CL(f"{IN_J} {PP[0]}, {ADHI}", dev=DEV_TWENTY),
    "1-361": CL(f"{IN_J} {PP[0]}", stage=2),
    "1-362": CL(f"{IN_J} {PP[0]}", stage=3),
    "1-363": CL(f"{IN_J} {PP[0]}", stage=4),
}

OPEN_RX = re.compile(r"Katame dhammā kusalā\? Yasmiṃ samaye (.*?), tasmiṃ samaye (.*)")


def tr_rest(rest):
    """The part after 'tasmiṃ samaye' in an opening sentence."""
    if "; " + YEV_PI in rest:
        lst, tail = rest.split("; ", 1)
        return TASMIM + " " + hoti_list(lst) + tr_tail("; " + tail)
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
            out.append("есть " + N[p[: -len(" hoti")]])
        elif p == "ime dhammā kusalā":
            out.append(M.ANSWER_BARE(KUSALA))
        else:
            raise ValueError("unknown piece: " + p)
    return TASMIM + " " + (ELL + " ").join(out) + end


def tr_opening(line, clause):
    m = OPEN_RX.fullmatch(line)
    assert m, line
    return f"{M.QUESTION(KUSALA)} В то время, когда {clause}, " + tr_rest(m.group(2))


# ---- headings and closing lines (terms file) ---------------------------------------------------------
HEAD = {
    "#### Lokuttarakusalaṃ": "#### Надмирский благой ум",
    "##### Suddhikapaṭipadā": "##### Простой способ практики",
    "##### Suññataṃ": "##### Пустота",
    "##### Suññatamūlakapaṭipadā": "##### Способ практики, основанный на пустоте",
    "##### Appaṇihitaṃ": "##### Свободное от устремлений",
    "##### Appaṇihitamūlakapaṭipadā": "##### Способ практики, основанный на свободе от устремлений",
    "##### Vīsati mahānayā": "##### Двадцать великих методов",
    "##### Adhipati": "##### Преобладание",
}
CLOSE = {k[6:] + ".": v[6:] + "." for k, v in HEAD.items() if k.startswith("##### ")}
CLOSE.update({
    "Paṭhamo maggo.": "Первый путь.",
    "Dutiyo maggo.": "Второй путь.",
    "Tatiyo maggo.": "Третий путь.",
    "Catuttho maggo.": "Четвёртый путь.",
    "Lokuttaraṃ cittaṃ.": "Надмирский ум.",
})

# ^1-364: the Pāli joins this answer to the elided rest with a comma, not a dash (translated as written)
_PANNA_PI = ("paññā pajānanā vicayo pavicayo dhammavicayo sallakkhaṇā upalakkhaṇā paccupalakkhaṇā paṇḍiccaṃ "
             "kosallaṃ nepuññaṃ vebhabyā cintā upaparikkhā bhūrī medhā pariṇāyikā vipassanā sampajaññaṃ patodo "
             "paññā paññindriyaṃ paññābalaṃ paññāsatthaṃ paññāpāsādo paññāāloko paññāobhāso paññāpajjoto "
             "paññāratanaṃ amoho dhammavicayo sammādiṭṭhi dhammavicayasambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ")
_PALI_1_364 = ("Katamaṃ tasmiṃ samaye aññindriyaṃ hoti? Yā " + P_ANNA + _PANNA_PI
               + ", idaṃ tasmiṃ samaye aññindriyaṃ hoti…pe… avikkhepo hoti…pe… " + YEV_PI + "kusalā.")
MANUAL = {
    ("1-364", 0): (_PALI_1_364,
                   f"{Q('aññindriyaṃ')} То, что {G_ANNA}, есть {tr_string(_PANNA_PI)}, "
                   f"{ANSWER_END('aññindriyaṃ')}{ELL} есть {N['avikkhepo']}{ELL} {OR_YEV}"),
}


# ---- assembly ----------------------------------------------------------------------------------------
ID_RX = re.compile(r"\s\^([0-9A-Za-z-]+)\s*$")


def pali_segments(path):
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


def dashes(s):
    return s.count("–") + s.count("—")


def build():
    used, out = set(), []
    for bid, lines in pali_segments(PALI):
        rl = []
        for i, line in enumerate(lines):
            if (bid, i) in MANUAL:
                pali, ru = MANUAL[(bid, i)]
                assert line == pali, (bid, line)
                used.add(("M", bid, i))
            elif line in HEAD:
                ru = HEAD[line]
            elif line in CLOSE:
                ru = CLOSE[line]
            else:
                ru = tr_qa(line) or tr_kotthasa(line) or tr_sangaha(line)
                if ru is None:
                    assert i == 0 and bid in OPEN, (bid, i, line[:80])
                    ru = tr_opening(line, OPEN[bid])
                    used.add(("O", bid))
            assert dashes(line) == dashes(ru), (bid, i, dashes(line), dashes(ru), ru)
            assert line.count("?") == ru.count("?"), (bid, i, ru)
            assert "—" not in ru and ":-" not in ru and "pe…" not in ru, (bid, ru)
            assert not re.search(r"[A-Za-zāīūṃṅñṭḍṇḷ]", ru), (bid, ru)
            assert not re.search(r"(?<![А-Яа-яЁё])ли(?![А-Яа-яЁё])", ru), (bid, ru)
            rl.append(ru)
        rl[-1] += f" ^{bid}"
        out.append("\n".join(rl))
    unused = [k for k in OPEN if ("O", k) not in used] + [k for k in MANUAL if ("M",) + k not in used]
    assert not unused, unused
    return "\n\n".join(out) + "\n", len(out)


TEXT, NSEG = build()

if __name__ == "__main__":
    OUT.write_text(TEXT, encoding="utf-8", newline="\n")
    print("wrote", OUT, NSEG, "segments")
