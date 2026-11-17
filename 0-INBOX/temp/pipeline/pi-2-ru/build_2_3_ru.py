# -*- coding: utf-8 -*-
"""pi-2 Vibhaṅga, Russian plain zero-shot: chapters 2 (Āyatanavibhaṅga) and 3 (Dhātuvibhaṅga).

usage: python -I -X utf8 build_2_3_ru.py [--forms]
Writes AI_translation\\russian\\pi-2-russian-plain-zeroshot_split_chapters\\2-ayatanavibhango.md and 3-dhatuvibhango.md.
Reuses build_ch1_sample_ru (S) and build_1_ru (B): headings, frames, ITEMS / SURF matrix lexicon.
pi-1 definitions of the sense bases, the four elements, the citta synonym string, the moho, dosa
and kāma-world strings are taken byte for byte from the pi-1 Russian (looked up by block ID).
The Pañhāpucchaka is generated phrase by phrase from fixed tables; unknown Pāli raises KeyError.
Block IDs are copied from the Pāli lines. Importing this module writes nothing.
"""
import itertools, os, re, sys

HERE = r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-ru"
sys.path.insert(0, HERE)
import build_ch1_sample_ru as S  # noqa: E402
import build_1_ru as B  # noqa: E402

DASH = S.DASH
cap, low = S.cap, S.low
PE = "\x01"


# ---------------------------------------------------------------- 0. pi-1 Russian by block ID
def _pi1_lines():
    out = {}
    for fn in sorted(os.listdir(S.PI1_RU_DIR)):
        if fn.endswith(".md"):
            for line in open(os.path.join(S.PI1_RU_DIR, fn), encoding="utf-8").read().split("\n"):
                m = S.ID.search(line)
                if m:
                    out[m.group(1)] = S.ID.sub("", line)
    return out


PI1 = _pi1_lines()


def pi1_body(bid, end):
    """Text after the question mark and before `end` (the pi-1 answer frame)."""
    line = PI1[bid]
    body = line.split("? ", 1)[1]
    return body[:body.index(end)]


def edit(s, old, new):
    assert old in s, (old, s[:80])
    return s.replace(old, new, 1)


# ---------------------------------------------------------------- 1. names
AY = {  # āyatana: nominative, instrumental
    "cakkhu": ("сфера глаза", "сферой глаза"), "sota": ("сфера уха", "сферой уха"),
    "ghāna": ("сфера носа", "сферой носа"), "jivhā": ("сфера языка", "сферой языка"),
    "kāya": ("сфера тела", "сферой тела"), "mana": ("сфера ума", "сферой ума"),
    "rūpa": ("сфера видимых форм", "сферой видимых форм"), "sadda": ("сфера звуков", "сферой звуков"),
    "gandha": ("сфера запахов", "сферой запахов"), "rasa": ("сфера вкусов", "сферой вкусов"),
    "phoṭṭhabba": ("сфера осязаемого", "сферой осязаемого"), "dhamma": ("сфера объектов ума", "сферой объектов ума"),
}
DH = {  # dhātu (pi-1 «элемент …»): nominative, instrumental
    "cakkhu": "элемент глаза", "rūpa": "элемент видимых форм", "cakkhuviññāṇa": "элемент зрительного сознания",
    "sota": "элемент уха", "sadda": "элемент звуков", "sotaviññāṇa": "элемент слухового сознания",
    "ghāna": "элемент носа", "gandha": "элемент запахов", "ghānaviññāṇa": "элемент обонятельного сознания",
    "jivhā": "элемент языка", "rasa": "элемент вкусов", "jivhāviññāṇa": "элемент вкусового сознания",
    "kāya": "элемент тела", "phoṭṭhabba": "элемент осязаемого", "kāyaviññāṇa": "элемент осязательного сознания",
    "mano": "элемент ума", "dhamma": "элемент объектов ума", "manoviññāṇa": "элемент умственного сознания",
    "pathavī": "элемент земли", "āpo": "элемент воды", "tejo": "элемент огня", "vāyo": "элемент ветра",
    "ākāsa": "элемент пространства", "viññāṇa": "элемент сознания",
    "sukha": "элемент удовольствия", "dukkha": "элемент боли", "somanassa": "элемент радости",
    "domanassa": "элемент уныния", "upekkhā": "элемент невозмутимости", "avijjā": "элемент неведения",
    "kāma": "элемент чувственных желаний", "byāpāda": "элемент недоброжелательности",
    "vihiṃsā": "элемент жестокости", "nekkhamma": "элемент отречения",
    "abyāpāda": "элемент отсутствия недоброжелательности", "avihiṃsā": "элемент отсутствия жестокости",
}


def dh_ins(k):
    return "элементом" + DH[k][len("элемент"):]


def q(name):
    return f"{S.TATTHA} {name}?"


def called(ins, quoted=True):
    """ayaṃ / idaṃ vuccati "X" -> это называется «X (instrumental)»"""
    return f"{S.VUCCATI} «{ins}»" if quoted else f"{S.VUCCATI} {ins}"


def enum(items):  # opening enumeration "N things – a, b, c": «и» before the last (as S.FIVE_AGGREGATES)
    return ", ".join(items[:-1]) + " и " + items[-1]


AY12_A = ["cakkhu", "rūpa", "sota", "sadda", "ghāna", "gandha", "jivhā", "rasa", "kāya", "phoṭṭhabba", "mana", "dhamma"]
AY12_B = ["cakkhu", "sota", "ghāna", "jivhā", "kāya", "mana", "rūpa", "sadda", "gandha", "rasa", "phoṭṭhabba", "dhamma"]
DH18 = ["cakkhu", "rūpa", "cakkhuviññāṇa", "sota", "sadda", "sotaviññāṇa", "ghāna", "gandha", "ghānaviññāṇa",
        "jivhā", "rasa", "jivhāviññāṇa", "kāya", "phoṭṭhabba", "kāyaviññāṇa", "mano", "dhamma", "manoviññāṇa"]
TWELVE = "Двенадцать сфер восприятия"
EIGHTEEN = "Восемнадцать элементов"


def twelve(order):
    return f"{TWELVE} {DASH} " + enum([AY[k][0] for k in order]) + "."


EIGHTEEN_LINE = f"{EIGHTEEN} {DASH} " + enum([DH[k] for k in DH18]) + "."

# ---------------------------------------------------------------- 2. sense-base definitions (pi-1 ^1-596 …)
END = ", – это материальная форма, являющаяся "
EYE = edit(pi1_body("^1-596", END), "[вариант написания (Sī., Syā.): cakkhuṃ]",
           "[вариант написания (Sī., Syā., Ka.): cakkhuṃ; dha. sa. 596-599]")
EAR = pi1_body("^1-600", END)
NOSE = pi1_body("^1-604", END)
TONGUE = pi1_body("^1-608", END)   # pi-2 jīvhindriyampetaṃ: spelling slip, rendered as meant
BODY = pi1_body("^1-612", END)
VIS = pi1_body("^1-616", END)
VIS = edit(VIS, "красное,", "красное [вариант написания (Sī.): pītaṃ lohitaṃ],")
VIS = edit(VIS, " [вариант написания (Sī., Ka.): caturassaṃ]", "")   # pi-2 has caturassaṃ without a variant
VIS = edit(VIS, "[вариант написания (Sī., Syā.): suriyamaṇḍalassa]", "[вариант написания (Sī., Syā., Kaṃ.): suriyamaṇḍalassa]")
SOUND = edit(pi1_body("^1-620", END), "звук малых барабанов,", "звук малых барабанов [вариант написания (Sī.): mutiṅgasaddho],")
SMELL = pi1_body("^1-624", END)   # pi-2 āmagandho = pi-1 āmakagandho
TASTE = edit(pi1_body("^1-628", END), "солёный, щелочной, кисловатый [вариант чтения (Sī.): lapilakaṃ],",
             "солёный [вариант чтения (Sī.): lapilakaṃ, (Ka., Sī.): lampikaṃ], щелочной, кисловатый,")
TOUCH = pi1_body("^1-647", END)
assert "[" not in EAR + NOSE + TONGUE + BODY + SMELL + TOUCH


def sense_def(k, body):
    """Tattha katamaṃ cakkhāyatanaṃ? … suñño gāmopeso. Idaṃ vuccati "cakkhāyatanaṃ"."""
    return f"{q(AY[k][0])} {body}. {cap(called(AY[k][1]))}."


def head(body):
    """pi-1 body up to «великих элементов» (where the pi-2 abbreviation …pe… starts)."""
    i = body.index("великих элементов") + len("великих элементов")
    return body[:i]


def head_sound(body):
    return body[:body.index(":")]


def tail(body):
    """last items «это …» before the dash (after the abbreviation)."""
    i = body.rindex("; ")
    return body[i + 2:]


def tail_last(body):
    return body[body.rindex(", это ") + 2:]


def dh_sense(k, ru):
    return f"{q(DH[k])} {ru}, {DASH} {called(dh_ins(k))}."


# ---------------------------------------------------------------- 3. citta synonyms, paṭicca formula (pi-1 ^1-6)
CITTA_SYN = "ум, разум, умственная деятельность, сердце, чистота, разум, сфера ума, способность ума, сознание, совокупность сознания"
CITTA_SHORT = "ум, разум, умственная деятельность"
assert CITTA_SYN + ", соответствующий элемент умственного сознания, – это ум" in PI1["^1-6"]
VINN_GEN = {"cakkhu": "зрительного", "sota": "слухового", "ghāna": "обонятельного", "jivhā": "вкусового",
            "kāya": "осязательного", "mano": "умственного"}
PATICCA = {"cakkhu": "глаза и видимых форм", "sota": "уха и звуков", "ghāna": "носа и запахов",
           "jivhā": "языка и вкусов", "kāya": "тела и осязаемого", "mano": "ума и объектов ума"}


def tajja(k):
    return f"соответствующий элемент {VINN_GEN[k]} сознания" if k != "manodhātu" else "соответствующий элемент ума"


def arises(what):
    return f"возникает {CITTA_SYN}, {what}"


def paticca(k):  # Cakkhuñca paṭicca rūpe ca uppajjati cittaṃ … tajjācakkhuviññāṇadhātu
    return f"В зависимости от {PATICCA[k]} " + arises(tajja(k))


def after(k):  # Cakkhuviññāṇadhātuyā uppajjitvā niruddhasamanantarā
    return f"сразу после возникновения и прекращения элемента {VINN_GEN[k]} сознания"


def after_gen(k):  # the abbreviated forms "sotaviññāṇadhātuyā…pe…"
    return f"элемента {VINN_GEN[k]} сознания"


# ---------------------------------------------------------------- 4. aggregates, dhammāyatana (Abhidhammabhājanīya)
REST_DHAMMA = ("Совокупность чувств, совокупность восприятия, совокупность формирующих факторов, "
               "и та материальная форма, которая является невидимой и не способной к соударению и принадлежит к сфере "
               "объектов ума, и необусловленный элемент.")   # pi-1 ^1-1094 / ^1-1096 words
assert "и та материальная форма, которая является невидимой и не способной к соударению и принадлежит к сфере объектов ума, и необусловленный элемент" in PI1["^1-1094"]
ANIDASSANA_RUPA = "невидимая материальная форма, не способная к соударению и принадлежащая к сфере объектов ума"  # pi-1 Katamaṃ taṃ rūpaṃ anidassanaṃ appaṭighaṃ dhammāyatanapariyāpannaṃ?
ANIDASSANA_RUPA_INS = "невидимой материальной формой, не способной к соударению и принадлежащей к сфере объектов ума"
assert "Что такое " + ANIDASSANA_RUPA + "?" in open(os.path.join(S.PI1_RU_DIR, "3-03-rupakandam.md"), encoding="utf-8").read()
ASANKHATA = "необусловленный элемент"   # pi-1 asaṅkhatā dhātu
ASANKHATA_INS = "необусловленным элементом"
KHAYA = "Уничтожение страсти, уничтожение злобы, уничтожение заблуждения"   # Rāgakkhayo, dosakkhayo, mohakkhayo
FEM_TO_FOOD2 = "Способность женственности, способность мужественности… съедаемая пища"   # Itthindriyaṃ purisindriyaṃ…pe… kabaḷīkāro āhāro


def agg_line(a, sankhara_pali_hetu="na hetu", final_dash=False):
    """Tattha katamo vedanākkhandho? Ekavidhena … – phassasampayutto. Duvidhena … Tividhena …pe… evaṃ dasavidhena …pe…
    evaṃ bahuvidhena vedanākkhandho. Ayaṃ vuccati "vedanākkhandho"."""
    if a == "sankhara":
        one = B.BARE["cittasampayutto"]
        two = f"бывает {B.ITEMS['hetu']['b']}, бывает {B.ITEMS['na_hetu']['b']}"
    else:
        one = B.BARE["phassasampayutto"]
        two = f"бывает {B.ITEMS['sahetuka']['b']}, бывает {B.ITEMS['ahetuka']['b']}"
    three = ", ".join("бывает " + B.ITEMS[k]["b"] for k in ("kusala", "akusala", "abyakata"))
    s = (f"{S.khandha_question(a)} {B.frame_open(a, 1)} {DASH} {one}. {B.frame_open(a, 2)} {DASH} {two}. "
         f"{B.frame_open(a, 3)} {DASH} {three}… {low(B.frame_close(a, 10))}… {low(B.frame_close(a, 'many'))}")
    ans = called(S.AGG[a]["khandha_ins"])
    return s + (f" {DASH} {ans}." if final_dash else f". {cap(ans)}.")


# ---------------------------------------------------------------- 5. manāyatana classification (ch. 2)
MAN = "сферы ума"


def man_open(n):
    return f"Классификация {MAN} {B.HOW_MANY[n]}"


def man_close(n):
    return f"Такова классификация {MAN} {B.HOW_MANY[n]}"


def man_chunk(c, st):
    if c == "phassasampayuttaṃ":
        return "связанная с контактом"
    if c in B.SUBJ:
        return B.SUBJ[c][0]
    m = re.match(r"^atthi (.+)$", c)
    if m:
        x = m.group(1)
        return "бывает " + (B.ATTHI_N[x] if st["mode"] == "n" else ITEMS2[key_of(x)]["b"])
    m = re.match(r"^(.+?) atthi (.+)$", c)
    if m:
        st["mode"] = "n"
        s_ru, close = B.SUBJ[m.group(1)]
        return s_ru + ("," if close else "") + " бывает " + B.ATTHI_N[m.group(2)]
    raise KeyError("man chunk: " + c)


def man_line(t):
    pre = ""
    if t.startswith("Tattha katamaṃ manāyatanaṃ? "):
        pre = q(AY["mana"][0]) + " "
        t = t[len("Tattha katamaṃ manāyatanaṃ? "):]
    out = []
    for sent in re.split(r"(?<=\.) (?=[A-Z])", t):
        m = re.match(r"^Evaṃ (\w+?)[vb]idhena manāyatanaṃ\.$", sent)
        if m:
            out.append(man_close(B.NUM[m.group(1).lower()]) + ".")
            continue
        if sent == 'Idaṃ vuccati "manāyatanaṃ".':
            out.append(cap(called(AY["mana"][1])) + ".")
            continue
        m = re.match(r"^(\w+?)[vb]idhena manāyatanaṃ – (.+)\.$", sent)
        body = m.group(2).replace("…pe…", PE)
        st = {"mode": "f"}
        parts = re.split(r"(, |\x01)", body)
        ru = []
        for i, x in enumerate(parts):
            if i % 2:
                ru.append(x.replace(PE, "…"))
            elif x:
                ru.append(man_chunk(x, st))
        out.append(f"{man_open(B.NUM[m.group(1).lower()])} {DASH} " + "".join(ru) + ".")
    return pre + " ".join(out)


# ---------------------------------------------------------------- 6. the four elements and space (ch. 3 Suttanta)
INT_SELF = "внутреннее и собственное"            # ajjhattaṃ paccattaṃ
INT_CLUNG = "внутри охвачено цеплянием"           # ajjhattaṃ upādinnaṃ
EXT_SELF = "относящееся к внешнему"              # bāhiraṃ
EXT_CLUNG = "вовне не охвачено цеплянием"         # bahiddhā anupādinnaṃ
SUCH_AS = "а именно"                              # seyyathidaṃ [pi-5]
# pi-1 ^1-967 … ^1-970, ^1-637 (nominative strings, verbatim)
EARTH = "твёрдое, то, что считается жёстким, твёрдость, свойство твёрдости"
WATER = "вода, то, что считается водой, влага, то, что считается влагой, связующее свойство материальной формы"
FIRE = "огонь, то, что считается огнём, тепло, то, что считается теплом, жар, то, что считается жаром"
WIND = "ветер, то, что считается ветром, состояние напряжённости материальной формы"
SPACE = "пространство, то, что считается пространством, незаполненное, то, что считается незаполненным, просвет, то, что считается просветом"
for _s in (EARTH.replace("жёстким,", "жёстким [вариант написания (Ka.): kharigataṃ],"), WATER, FIRE, WIND, SPACE + ", не затронутое четырьмя великими элементами"):
    assert any(_s in v for v in PI1.values()), _s
SPACE_INT = SPACE + ", не затронутое плотью и кровью"
SPACE_EXT = SPACE + ", не затронутое четырьмя великими элементами"
VAR_SNEHO = " [вариант написания (Syā.): sneho snehagataṃ]"

ASITA = "съеденное, выпитое, разжёванное и отведанное"   # asitapītakhāyitasāyitaṃ [pi-5]
LISTS = {
    ("pathavī", "int"): ("волосы на голове, волосы на теле, ногти, зубы, кожа, плоть, сухожилия [вариант написания (Sī.): nahāru], "
                         "кости, костный мозг [вариант написания (Sī.): aṭṭhimiñjā], почки, сердце, печень, плевра, селезёнка, "
                         "лёгкие, кишечник, брыжейка, содержимое желудка, кал"),
    ("pathavī", "ext"): ("железо, медь, олово, свинец, серебро [вариант написания (Syā.): sajjhu], жемчуг, драгоценный камень, "
                         "берилл, раковина, кристалл, коралл, серебро, золото, рубин [вариант написания (Syā., Ka.): lohitaṅgo, "
                         "(?): lohitako], кошачий глаз, трава, дерево, гравий, черепки [вариант написания (Ka.): kathalaṃ], "
                         "земля, камень, гора"),
    ("āpo", "int"): "желчь, слизь, гной, кровь, пот, жир, слёзы, жидкий жир, слюна, сопли, суставная жидкость, моча",
    ("āpo", "ext"): ("сок корней, сок стеблей, сок коры, сок листьев, сок цветов, сок плодов, молоко, простокваша, "
                     "топлёное масло, сливочное масло, растительное масло, мёд, патока, воды в земле или воды в небе"),
    ("tejo", "int"): ("то, от чего согреваются, то, от чего стареют, то, от чего сгорают в жару, и то, благодаря чему "
                      f"{ASITA} правильно переваривается"),
    ("tejo", "ext"): ("огонь от дров, огонь от соломы [вариант чтения (все издания): sakalikaggi], огонь от травы, "
                      "огонь от навоза, огонь от мякины, огонь от мусора, огонь молнии, жар огня, жар солнца, "
                      "жар от кучи дров, жар от кучи травы, жар от кучи зерна, жар от кучи товаров"),
    ("vāyo", "int"): ("ветры, идущие вверх, ветры, идущие вниз, ветры в животе, ветры в кишечнике [вариант написания "
                      "(Sī., Syā.): koṭṭhasayā], ветры, проходящие по всем членам тела, ветры, режущие как нож, ветры, "
                      "режущие как бритва, колющие ветры, либо вдох и выдох"),
    ("vāyo", "ext"): ("восточные ветры, западные ветры, северные ветры, южные ветры, пыльные ветры, ветры без пыли, "
                      "холодные ветры, горячие ветры, слабые ветры, сильные ветры, грозовые ветры, ветры поднебесья, "
                      "ветры от крыльев, ветры от крыльев гаруды, ветры от опахала из пальмовых листьев, ветры от веера"),
    ("ākāsa", "int"): (f"ушное отверстие, носовое отверстие, ротовое отверстие, то, через что проглатывают {ASITA}, "
                       f"то, где пребывает {ASITA}, то, через что {ASITA} выходит вниз"),
}
EL_GEN_PL = {"pathavī": "Элементов земли", "āpo": "Элементов воды", "tejo": "Элементов огня",
             "vāyo": "Элементов ветра", "ākāsa": "Элементов пространства"}
INT_ATTR, EXT_ATTR = "относящийся к внутреннему", "относящийся к внешнему"     # ajjhattika / bāhira [terms §6]
INT_ATTR_INS, EXT_ATTR_INS = "относящимся к внутреннему", "относящимся к внешнему"


def element_lines(k, x_int, x_ext, x_int_first=None):
    """two Pāli lines: (dvaya + internal), (external + both together)."""
    nom = DH[k]
    # a comma closes a final relative clause («то, что считается жаром») or participial phrase («не затронутое …»)
    cl = lambda x: x + ("," if x.endswith("жаром") or x.endswith("кровью") or x.endswith("элементами") else "")
    x_int, x_ext = cl(x_int), cl(x_ext)
    first = cl(x_int_first) if x_int_first else x_int
    int_def = (f"То {INT_SELF}, что есть {first} и {INT_CLUNG}, {SUCH_AS} {DASH} {LISTS[(k, 'int')]}, "
               f"а также всё другое {INT_SELF}, что есть {x_int} и {INT_CLUNG}, {DASH} "
               f"{called(dh_ins(k) + ', ' + INT_ATTR_INS)}.")
    l1 = (f"{q(nom)} {EL_GEN_PL[k]} два {DASH} есть {INT_ATTR}, есть {EXT_ATTR}. "
          f"{q(nom + ', ' + INT_ATTR)} {int_def}")
    if (k, "ext") in LISTS:
        ext_def = (f"То {EXT_SELF}, что есть {x_ext} и {EXT_CLUNG}, {SUCH_AS} {DASH} {LISTS[(k, 'ext')]}, "
                   f"а также всё другое {EXT_SELF}, что есть {x_ext} и {EXT_CLUNG}, {DASH} "
                   f"{called(dh_ins(k) + ', ' + EXT_ATTR_INS)}.")
    else:
        ext_def = f"То {EXT_SELF}, что есть {x_ext} и {EXT_CLUNG}, {DASH} {called(dh_ins(k) + ', ' + EXT_ATTR_INS)}."
    both = (f"И {nom}, {INT_ATTR}, и {nom}, {EXT_ATTR}, {S.KHANDHA_TOGETHER['pl']}, {DASH} {called(dh_ins(k))}.")
    l2 = f"{q(nom + ', ' + EXT_ATTR)} {ext_def} {both}"
    return [l1, l2]


# ---------------------------------------------------------------- 7. feeling and ignorance elements, thought elements
# pi-1 ^1-445, ^1-558, ^1-3, ^1-415, ^1-152 (without the tajjā… opening), ^1-390
FEEL = {
    "sukha": "телесная отрада, телесное удовольствие, рождённое контактом тела отрадное приятное переживание, рождённое контактом тела отрадное приятное чувство",
    "dukkha": "телесная безотрадность, телесная боль, рождённое контактом тела безотрадное болезненное переживание, рождённое контактом тела безотрадное болезненное чувство",
    "somanassa": "душевная отрада, душевное счастье, рождённое контактом ума отрадное приятное переживание, рождённое контактом ума отрадное приятное чувство",
    "domanassa": "душевная безотрадность, душевная боль, рождённое контактом ума безотрадное болезненное переживание, рождённое контактом ума безотрадное болезненное чувство",
    "upekkhā": "душевное состояние, которое ни отрадно, ни безотрадно, рождённое контактом ума переживание, которое ни болезненно, ни приятно, рождённое контактом ума чувство, которое ни болезненно, ни приятно",
}
for _k, _b in (("sukha", "^1-445"), ("dukkha", "^1-558"), ("somanassa", "^1-3"), ("domanassa", "^1-415"), ("upekkhā", "^1-152")):
    assert FEEL[_k] + ", – это чувство" in PI1[_b], _k
MOHA = pi1_body("^1-390", ", – это заблуждение")
MOHA = MOHA[len("То, что в это время есть "):]
THOUGHT = "мышление, направленная мысль, помысел, прикрепление мысли, усиленное прикрепление мысли, направление ума на объект"
assert THOUGHT + ", ложный помысел, – это" in PI1["^1-371"] and THOUGHT + ", правильный помысел, – это" in PI1["^1-7"]
WRONG, RIGHT = "ложный помысел", "правильный помысел"
CONNECTED = {"kāma": "Связанные с чувственными желаниями", "byāpāda": "Связанные с недоброжелательностью",
             "vihiṃsā": "Связанные с жестокостью", "nekkhamma": "Связанные с отречением",
             "abyāpāda": "Связанные с отсутствием недоброжелательности", "avihiṃsā": "Связанные с отсутствием жестокости"}
KAMA_WORLD = pi1_body("^1-1287", " – это явления, относящиеся к миру чувственных желаний")
KAMA_WORLD = edit(KAMA_WORLD, " [вариант написания (Sī., Ka.): paranimmitavasavattideve]", "")
KAMA_WORLD = edit(KAMA_WORLD, "материальная форма,", "материальная форма [вариант написания (Syā.): rūpaṃ],")
# Dasasu vā āghātavatthūsu cittassa āghāto … anattamanatā cittassa (pi-1 ^1-1066 words; pi-2 lacks byāpajjitattaṃ)
DOSA_PI1 = pi1_body("^1-1066", ", – это называется злобой")
DOSA_PI1 = DOSA_PI1[DOSA_PI1.index("То, что есть такая досада ума, ") + len("То, что есть такая досада ума, "):]
DOSA = edit(DOSA_PI1, "проявление недоброжелательности, состояние недоброжелательности, ", "проявление недоброжелательности, ")
DOSA = "Или же досада ума в отношении десяти поводов для досады, " + DOSA
VIHIMSA = ("Вот некто мучает существ рукой, комом земли, палкой, оружием, верёвкой или чем-либо ещё, и такое мучение, "
           "сильное мучение, насилие, жестокое обращение, досаждение, сильное досаждение, причинение вреда другим")
METTA = "То, что есть доброжелательность к существам, проявление доброжелательности, состояние доброжелательности, освобождение ума доброжелательностью"
KARUNA = "То, что есть сострадание к существам, проявление сострадания, состояние сострадания, освобождение ума состраданием"
assert "доброжелательность, проявление доброжелательности, состояние доброжелательности" in PI1["^1-1062"]


def thought(k, right, pe):
    lst = (THOUGHT.split(", ")[0] + ", " + THOUGHT.split(", ")[1] + "… ") if pe else THOUGHT + ", "
    return f"{CONNECTED[k]} {lst}{right}"


# ---------------------------------------------------------------- 8. Pañhāpucchaka
ITEMS2 = {k: dict(v) for k, v in B.ITEMS.items()}
SURF2 = dict(B.SURF)


def alias(key, *surfaces):
    for x in surfaces:
        assert x not in SURF2 or SURF2[x] == key, (x, key)
        SURF2[x] = key


def new(key, surfaces, b=None, s=None, p=None, qs=None, qp=None):
    assert key not in ITEMS2
    ITEMS2[key] = dict(b=b, s=s, p=p, qs=qs, qp=qp)
    alias(key, *surfaces)


new("appaccaya", ["appaccayaṃ", "appaccayā"], None, "не имеет условий", "не имеют условий")
alias("sappaccaya", "sappaccayaṃ")
new("asankhata", ["asaṅkhataṃ", "asaṅkhatā"], "необусловленной", "является необусловленной", "являются необусловленными")
alias("sankhata", "saṅkhataṃ")
alias("rupi", "rūpā")
alias("arupi", "arūpaṃ")
alias("citta", "cittā")
alias("uppadi", "uppādi", "uppādinī")
alias("nahetu_ahetuka", "na hetūahetukā")
alias("cittanuparivatti", "cittānuparivattī")
alias("no_cittanuparivatti", "no cittānuparivattī")
alias("cssh", "cittasaṃsaṭṭhasamuṭṭhānasahabhū")
alias("no_cssh", "no cittasaṃsaṭṭhasamuṭṭhānasahabhū")
alias("cssa", "cittasaṃsaṭṭhasamuṭṭhānānuparivatti", "cittasaṃsaṭṭhasamuṭṭhānānuparivattī")
alias("no_cssa", "no cittasaṃsaṭṭhasamuṭṭhānānuparivatti", "no cittasaṃsaṭṭhasamuṭṭhānānuparivattī")
alias("ajjhattika", "ajjhattikā")
alias("no_cittasahabhu", "no cittasahabhuno")
alias("no_cittanuparivatti", "no cittānuparivattino")
# singular forms for the citta-cluster (Dhammāyatanaṃ / Dhammadhātu siyā …)
ITEMS2["css"]["s"] = "соединена с умом и порождена им"
ITEMS2["no_css"]["s"] = "не является соединённой с умом и порождённой им"
ITEMS2["cssh"]["s"] = "соединена с умом, порождена им и сосуществует с ним"
ITEMS2["no_cssh"]["s"] = "не является соединённой с умом, порождённой им и сосуществующей с ним"
ITEMS2["cssa"]["s"] = "соединена с умом, порождена им и следует за ним"
ITEMS2["no_cssa"]["s"] = "не является соединённой с умом, порождённой им и следующей за ним"
# quoted plural forms (pi-1 ^1-1198 words, plural)
for k, f in (("q_cittena_sampayutta", "связанные с умом"), ("q_cittena_vippayutta", "не связанные с умом"),
             ("q_cittena_samsattha", "соединённые с умом"), ("q_cittena_visamsattha", "не соединённые с умом")):
    ITEMS2[k]["qp"] = f
# quoted forms of the plain adjectives (pi-1 ^1-1430, ^1-1431: «возникшее явление», «прошлое явление» …)
for k, a_sg, a_pl in (("uppanna", "возникшее", "возникшие"), ("anuppanna", "невозникшее", "невозникшие"),
                      ("atita", "прошлое", "прошлые"), ("anagata", "будущее", "будущие"),
                      ("paccuppanna", "настоящее", "настоящие")):
    ITEMS2[k]["qs"], ITEMS2[k]["qp"] = f"{a_sg} явление", f"{a_pl} явления"
ITEMS2["uppadi"]["qs"], ITEMS2["uppadi"]["qp"] = "явление, которому предстоит возникнуть", "явления, которым предстоит возникнуть"
# Pāli as written (reported): Manāyatanaṃ na vattabbaṃ – "upādāniyañceva upādānasampayuttañcā"ti;
# Dvāyatanā siyā upādānasampayuttaupādāniyā
new("upadana_niya_samp", ["upādāniyo ceva upādānasampayutto ca"], qs="явление, служащее объектом цепляния и связанное с цепляниями")
new("upadana_samp_niya", ["upādānasampayuttaupādāniyā"], None, None, "связаны с цепляниями и служат объектом цепляния")

KEEP_CEVA = ("saṃyojanañceva", "nīvaraṇañceva", "upādānañceva")


def _alts(w):
    out = [w]
    if w in KEEP_CEVA:
        return out
    if w.endswith("añceva"):
        out.append(w[:-6] + "o ceva")
    elif w.endswith("añcā") or w.endswith("añca"):
        out.append(w[:-4] + "o ca")
    elif w == "cā":
        out.append("ca")
    elif w.endswith("aṃ"):
        out += [w[:-2] + "o", w[:-2] + "ā"]
    elif w.endswith("ā"):
        out.append(w[:-1] + "o")
    return out


def key_of(surface):
    if surface in SURF2:
        return SURF2[surface]
    words = surface.split(" ")
    for combo in itertools.product(*[_alts(w) for w in words]):
        c = " ".join(combo)
        if c in SURF2:
            return SURF2[c]
        if c + " ca" in SURF2:   # "saṃyojanañceva saṃyojaniya"ntipi (ca missing, reported)
            return SURF2[c + " ca"]
    raise KeyError("surface: " + surface)


SHORT_M = {"связана": "связан", "охвачена": "охвачен", "подвержена": "подвержен", "свободна": "свободен",
           "затронута": "затронут", "омрачена": "омрачён", "соединена": "соединён", "порождена": "порождён",
           "сопряжена": "сопряжён", "способна": "способен"}
KEEP_OI = {"помехой", "корней"}     # nouns in -ой / -ей
PREPS = {"без", "с", "со", "к", "от", "по"}   # an adjective after a preposition belongs to its noun phrase
MASC_SEEN = {}


def masc(s):
    """feminine singular predicate (subject «сфера», «совокупность») -> masculine (subject «элемент»)."""
    r = s.replace("такой, которой", "таким, которому")
    toks = re.split(r"([А-Яа-яЁё]+)", r)
    prev = ""
    for i in range(1, len(toks), 2):
        x = toks[i]
        if x in SHORT_M:
            toks[i] = SHORT_M[x]
        elif x not in KEEP_OI and prev not in PREPS and len(x) > 3 and (x.endswith("ой") or x.endswith("ей")):
            stem = x[:-2]
            toks[i] = stem + ("им" if x.endswith("ей") or stem[-1] in "кгхжшщч" else "ым")
        prev = x
    r = "".join(toks)
    MASC_SEEN[s] = r
    return r


SUBJ2 = {}   # Pāli -> (nominative, accusative, number, gender)
for p, n in (("Dasāyatanā", "Десять"), ("Pañcāyatanā", "Пять"), ("Ekādasāyatanā", "Одиннадцать"),
             ("Navāyatanā", "Девять"), ("Chāyatanā", "Шесть")):
    SUBJ2[p] = (f"{n} сфер восприятия", f"{n} сфер восприятия", "pl", None)
for p, n in (("Dvāyatanā", "Две"), ("Cattāro āyatanā", "Четыре")):
    SUBJ2[p] = (f"{n} сферы восприятия", f"{n} сферы восприятия", "pl", None)
for p, k in (("Manāyatanaṃ", "mana"), ("Dhammāyatanaṃ", "dhamma"), ("Saddāyatanaṃ", "sadda"), ("Rūpāyatanaṃ", "rūpa")):
    nom = cap(AY[k][0])
    SUBJ2[p] = (nom, "Сферу" + nom[len("Сфера"):], "sg", "f")
for p, n in (("Soḷasa", "Шестнадцать"), ("Dasa", "Десять"), ("Pañca", "Пять"), ("Pannarasa", "Пятнадцать"),
             ("Sattarasa", "Семнадцать"), ("Cha", "Шесть"), ("Nava", "Девять"), ("Aṭṭha", "Восемь"),
             ("Satta", "Семь"), ("Ekādasa", "Одиннадцать"), ("Dvādasa", "Двенадцать")):
    SUBJ2[p + " dhātuyo"] = (f"{n} элементов", f"{n} элементов", "pl", None)
SUBJ2["Sattadhātuyo"] = SUBJ2["Satta dhātuyo"]   # spacing slip in the Pāli (reported)
SUBJ2["Dve dhātuyo"] = ("Два элемента", "Два элемента", "pl", None)
SUBJ2["Tisso dhātuyo"] = ("Три элемента", "Три элемента", "pl", None)
for p, k in (("Kāyaviññāṇadhātu", "kāyaviññāṇa"), ("Manoviññāṇadhātu", "manoviññāṇa"), ("Dhammadhātu", "dhamma"),
             ("Manodhātu", "mano"), ("Saddadhātu", "sadda"), ("Rūpadhātu", "rūpa")):
    SUBJ2[p] = (cap(DH[k]), cap(DH[k]), "sg", "m")
SUBJ_RE2 = re.compile(r"^(" + "|".join(map(re.escape, sorted(SUBJ2, key=len, reverse=True))) + r") (.+)$")
PRON = {("sg", "f"): "её", ("sg", "m"): "его", ("pl", None): "их"}
NV = B.NV


def pred2(surface, st):
    key = key_of(surface)
    if st["num"] == "sg":
        r = ITEMS2[key]["s"]
        if r is not None and st["g"] == "m":
            r = masc(r)
    else:
        r = ITEMS2[key]["p"]
    if r is None:
        raise KeyError(f"no {st['num']} predicate: {surface}")
    return r


def quote2(c, st):
    qm = B.QUOTE_RE.match(c)
    if not qm:
        raise KeyError("quote: " + c)
    text = qm.group(1) + ("ṃ" if qm.group(2) else "")
    key = key_of(text)
    f = ITEMS2[key]["qs" if st["num"] == "sg" else "qp"]
    if f is None:
        raise KeyError(f"no {st['num']} quote form: {text}")
    return ("ни как" if qm.group(3) else "как") + " «" + f + "»"


def chunk_q2(c, st):
    subj = None
    m = SUBJ_RE2.match(c)
    if m:
        subj = SUBJ2[m.group(1)]
        st["num"], st["g"] = subj[2], subj[3]
        c = m.group(2)
    m = re.match(r"^(siyā )?na vattabb(?:o|ā|aṃ) " + DASH + r" (.+)$", c)
    if m:
        qt = quote2(m.group(2), st)
        if m.group(1):
            ru = f"иногда {PRON[(st['num'], st['g'])]} {NV} {DASH} {qt}"
        else:
            ru = f"{NV} {DASH} {qt}"
            if subj:
                return f"{subj[1]} {ru}"
    elif B.QUOTE_RE.match(c):
        ru = quote2(c, st)
    elif re.match(r'^"[^"]*"$', c):   # quoted, no "ti": an affirmative statement (as ch. 1, reported)
        ru = pred2(c[1:-1], st)
    elif c.startswith("siyā "):
        ru = "иногда " + pred2(c[5:], st)
    else:
        ru = pred2(c, st)
    return f"{subj[0]} {ru}" if subj else ru


FIXES = [  # punctuation / particle slips in the Pāli (reported); words translated as written
    ('"ti pi', '"tipi'),
    ("siyā araṇāti.", "siyā araṇā."),
    ('"parāmāsā ceva parāmaṭṭhā cāti parāmaṭṭhā ceva no ca parāmāsā".', '"parāmāsā ceva parāmaṭṭhā cā"ti, "parāmaṭṭhā ceva no ca parāmāsā".'),
    ('"kilesasampayuttā ceva no ca na kilesā"tipi', '"kilesasampayuttā ceva no ca kilesā"tipi'),
]


def line_q2(t):
    for a, b in FIXES:
        t = t.replace(a, b)
    out = []
    for sent in re.split(r"(?<=\.) (?=[A-ZĀ])", t):
        assert sent.endswith("."), sent[-40:]
        body = sent[:-1].replace("…pe…", PE)
        parts = re.split(r"(, |; |\x01 ?)", body)
        st = {"num": None, "g": None}
        ru = []
        for i, x in enumerate(parts):
            if i % 2:
                ru.append(x.replace(PE, "…"))
            else:
                ru.append(chunk_q2(x, st))
        out.append(cap("".join(ru)) + ".")
    return " ".join(out)


def how_many_q(of):
    s = B.LABELS["Pañcannaṃ khandhānaṃ kati kusalā, kati akusalā, kati abyākatā…pe… kati saraṇā, kati araṇā?"]
    return edit(s, "пяти совокупностей", of)


# ---------------------------------------------------------------- 9. chapter 2
SEC = S.SECTION_TITLES
MANO_VAR = None


def ch2_lines():
    L = []
    add = L.append
    add("### " + S.CHAPTER_TITLES[2])
    add("#### " + SEC["Suttantabhājanīyaṃ"])
    add(twelve(AY12_A))
    M = "непостоянен, является страданием, лишён самости, подвержен изменению"
    N = "непостоянно, является страданием, лишено самости, подвержено изменению"
    P = "непостоянны, являются страданием, лишены самости, подвержены изменению"
    add(" ".join(f"{s} {f}." for s, f in (
        ("Глаз", M), ("Видимые формы", P), ("Ухо", N), ("Звуки", P), ("Нос", M), ("Запахи", P), ("Язык", M),
        ("Вкусы", P), ("Тело", N), ("Осязаемое", N), ("Ум", M), ("Объекты ума", P))))
    add(SEC["Suttantabhājanīyaṃ"] + ".")
    add("#### " + SEC["Abhidhammabhājanīyaṃ"])
    add(twelve(AY12_B))
    for k, body in (("cakkhu", EYE), ("sota", EAR), ("ghāna", NOSE), ("jivhā", TONGUE), ("kāya", BODY)):
        add(sense_def(k, body))
    return L   # manāyatana lines and the rest are added in ch2_build (Pāli-driven)


def ch2_rest():
    return {
        "rupa": sense_def("rūpa", VIS), "sadda": sense_def("sadda", SOUND), "gandha": sense_def("gandha", SMELL),
        "rasa": sense_def("rasa", TASTE), "phot": sense_def("phoṭṭhabba", TOUCH),
    }


def build_ch2(pali):
    """pali: list of non-empty Pāli lines (IDs stripped). Returns the Russian lines."""
    head_lines = ch2_lines()
    rest = ch2_rest()
    out = list(head_lines)
    i = len(head_lines)
    while i < len(pali):
        t = pali[i]
        if "manāyatanaṃ –" in t:
            out.append(man_line(t))
        elif t.startswith("Tattha katamaṃ rūpāyatanaṃ?"):
            out.append(rest["rupa"])
        elif t.startswith("Tattha katamaṃ saddāyatanaṃ?"):
            out.append(rest["sadda"])
        elif t.startswith("Tattha katamaṃ gandhāyatanaṃ?"):
            out.append(rest["gandha"])
        elif t.startswith("Tattha katamaṃ rasāyatanaṃ?"):
            out.append(rest["rasa"])
        elif t.startswith("Tattha katamaṃ phoṭṭhabbāyatanaṃ?"):
            out.append(rest["phot"])
        elif t.startswith("Tattha katamaṃ dhammāyatanaṃ?"):
            out.append(f"{q(AY['dhamma'][0])} {REST_DHAMMA}")
        elif t.startswith("Tattha katamo vedanākkhandho?"):
            out.append(agg_line("vedana"))
        elif t.startswith("Tattha katamo saññākkhandho?"):
            out.append(agg_line("sanna"))
        elif t.startswith("Tattha katamo saṅkhārakkhandho?"):
            out.append(agg_line("sankhara"))
        elif t.startswith("Tattha katamaṃ rūpaṃ anidassanaappaṭighaṃ"):
            out.append(f"{q(ANIDASSANA_RUPA)} {FEM_TO_FOOD2}. {cap(called(ANIDASSANA_RUPA_INS))}.")
        elif t.startswith("Tattha katamā asaṅkhatā dhātu?"):
            out.append(f"{q(ASANKHATA)} {KHAYA} {DASH} {called(ASANKHATA_INS)}.")
        elif t == "Idaṃ vuccati dhammāyatanaṃ.":
            out.append(cap(called(AY["dhamma"][1], quoted=False)) + ".")
        elif t == "Abhidhammabhājanīyaṃ.":
            out.append(SEC["Abhidhammabhājanīyaṃ"] + ".")
        elif t == "#### Pañhāpucchakaṃ":
            out.append("#### " + SEC["Pañhāpucchakaṃ"])
        elif t.startswith("Dvādasāyatanāni – "):
            out.append(twelve(AY12_A))
        elif t.startswith("Dvādasannaṃ āyatanānaṃ kati"):
            out.append(how_many_q("двенадцати сфер восприятия"))
        elif t in ("##### Tikaṃ", "##### Dukaṃ"):
            out.append(B.LABELS[t])
        elif t == "Pañhāpucchakaṃ.":
            out.append(SEC["Pañhāpucchakaṃ"] + ".")
        elif t == "Āyatanavibhaṅgo niṭṭhito.":
            out.append(S.CHAPTER_CLOSING.format(title=S.CHAPTER_TITLES[2]))
        else:
            out.append(line_q2(t))
        i += 1
    return out


# ---------------------------------------------------------------- 10. chapter 3
def build_ch3(pali):
    out = []
    add = out.append
    add("### " + S.CHAPTER_TITLES[3])
    add("#### " + SEC["Suttantabhājanīyaṃ"])
    add(f"Шесть элементов {DASH} " + enum([DH["pathavī"] + " [вариант написания (Sī., Syā.): paṭhavīdhātu; так же и далее]",
                                             DH["āpo"], DH["tejo"], DH["vāyo"], DH["ākāsa"], DH["viññāṇa"]]) + ".")
    out += element_lines("pathavī", EARTH, EARTH)
    out += element_lines("āpo", WATER, WATER, x_int_first=WATER.replace("то, что считается влагой", "то, что считается влагой" + VAR_SNEHO))
    out += element_lines("tejo", FIRE, FIRE)
    out += element_lines("vāyo", WIND, WIND)
    out += element_lines("ākāsa", SPACE_INT, SPACE_EXT)
    vinn6 = ", ".join(DH[k + "viññāṇa"] for k in ("cakkhu", "sota", "ghāna", "jivhā", "kāya", "mano"))
    add(f"{q(DH['viññāṇa'])} {cap(vinn6)} {DASH} {called(dh_ins('viññāṇa'))}.")
    six = "Это шесть элементов."
    add(six)
    add(f"Ещё шесть элементов {DASH} " + enum([DH[k] for k in ("sukha", "dukkha", "somanassa", "domanassa", "upekkhā", "avijjā")]) + ".")
    for k in ("sukha", "dukkha", "somanassa", "domanassa", "upekkhā"):
        add(f"{q(DH[k])} То, что есть {FEEL[k]}, {DASH} {called(dh_ins(k))}.")
    add(f"{q(DH['avijjā'])} То, что есть {MOHA}, {DASH} {called(dh_ins('avijjā'))}.")
    add(six)
    add(f"Ещё шесть элементов {DASH} " + enum([DH[k] for k in ("kāma", "byāpāda", "vihiṃsā", "nekkhamma", "abyāpāda", "avihiṃsā")]) + ".")
    add(f"{q(DH['kāma'])} {thought('kāma', WRONG, False)} {DASH} {called(dh_ins('kāma'), quoted=False)}. "
        f"{KAMA_WORLD} {DASH} {called(dh_ins('kāma'))}.")
    add(f"{q(DH['byāpāda'])} {thought('byāpāda', WRONG, True)} {DASH} {called(dh_ins('byāpāda'))}. "
        f"{DOSA} {DASH} {called(dh_ins('byāpāda'))}.")
    add(f"{q(DH['vihiṃsā'])} {thought('vihiṃsā', WRONG, True)} {DASH} {called(dh_ins('vihiṃsā'))}. "
        f"{VIHIMSA} {DASH} {called(dh_ins('vihiṃsā'))}.")
    add(f"{q(DH['nekkhamma'])} {thought('nekkhamma', RIGHT, True)} {DASH} {called(dh_ins('nekkhamma'))}. "
        f"Все благие явления тоже являются «{dh_ins('nekkhamma')}».")
    add(f"{q(DH['abyāpāda'])} {thought('abyāpāda', RIGHT, True)} {DASH} {called(dh_ins('abyāpāda'))}. "
        f"{METTA}, {DASH} {called(dh_ins('abyāpāda'))}.")
    add(f"{q(DH['avihiṃsā'])} {thought('avihiṃsā', RIGHT, False)} {DASH} {called(dh_ins('avihiṃsā'))}. "
        f"{KARUNA}, {DASH} {called(dh_ins('avihiṃsā'))}.")
    add(six)
    add(f"Таким образом, эти три шестёрки, {S.KHANDHA_TOGETHER['pl']}, составляют восемнадцать элементов.")
    add(SEC["Suttantabhājanīyaṃ"] + ".")
    # ---- Abhidhammabhājanīya
    add("#### " + SEC["Abhidhammabhājanīyaṃ"])
    add(EIGHTEEN_LINE)
    def organ(k, body):
        return dh_sense(k, f"{head(body)}… {tail_last(body)}")
    def obj(k, h, body):
        return dh_sense(k, f"{h}… {tail_last(body)}")
    def vinn(k):
        return f"{q(DH[k + 'viññāṇa'])} {paticca(k)} {DASH} {called(dh_ins(k + 'viññāṇa'))}."
    add(organ("cakkhu", EYE.replace(" [вариант написания (Sī., Syā., Ka.): cakkhuṃ; dha. sa. 596-599]", "")))
    add(obj("rūpa", head(VIS), VIS))
    add(vinn("cakkhu"))
    add(organ("sota", EAR))
    add(obj("sadda", head_sound(SOUND), SOUND))
    add(vinn("sota"))
    add(organ("ghāna", NOSE))
    add(obj("gandha", head_sound(SMELL), SMELL))
    add(vinn("ghāna"))
    add(organ("jivhā", TONGUE))
    add(obj("rasa", head_sound(TASTE), TASTE))
    add(vinn("jivhā"))
    add(organ("kāya", BODY))
    add(obj("phoṭṭhabba", "Элемент земли", TOUCH))
    add(vinn("kāya"))
    mano_t = tajja("manodhātu")
    first = f"{cap(after('cakkhu'))} {arises(mano_t)}"
    mid = "… ".join(after_gen(k) for k in ("sota", "ghāna", "jivhā"))
    last = f"{after('kāya')} {arises(mano_t)}"
    adv = f"или же как первое обращение внимания на любые явления {arises(mano_t)}"
    add(f"{q(DH['mano'])} {first}; {mid}… {last}, {adv} {DASH} {called(dh_ins('mano'))}.")
    add(f"{q(DH['dhamma'])} {REST_DHAMMA}")
    add(agg_line("vedana"))
    add(agg_line("sanna"))
    add(agg_line("sankhara", final_dash=True))   # "atthi ahetu" (as "na hetu"); "– ayaṃ vuccati" (reported)
    add(f"{q(ANIDASSANA_RUPA)} {cap(S.FEMININITY_TO_FOOD)} {DASH} {called(ANIDASSANA_RUPA_INS)}.")
    add(f"{q(ASANKHATA)} {KHAYA} {DASH} {called(ASANKHATA_INS)}. {cap(called(dh_ins('dhamma')))}.")
    mv = tajja("mano")
    after_m = "сразу после возникновения и прекращения элемента ума"
    first = (f"{cap(after('cakkhu'))} возникает {DH['mano']}, {after_m} возникает {CITTA_SHORT}… {mv}")
    mid = "… ".join(after_gen(k) for k in ("sota", "ghāna", "jivhā"))
    last = (f"{after('kāya')} возникает {DH['mano']}, сразу после возникновения и прекращения также и элемента ума "
            f"возникает {CITTA_SHORT}… {mv}, {low(paticca('mano'))}")
    add(f"{q(DH['manoviññāṇa'])} {first}; {mid}… {last} {DASH} {called(dh_ins('manoviññāṇa'))}.")
    add(SEC["Abhidhammabhājanīyaṃ"] + ".")
    n_head = len(out)
    rest = []
    for t in pali[n_head:]:
        if t == "#### Pañhāpucchakaṃ":
            rest.append("#### " + SEC["Pañhāpucchakaṃ"])
        elif t.startswith("Aṭṭhārasa dhātuyo – "):
            rest.append(EIGHTEEN_LINE)
        elif t.startswith("Aṭṭhārasannaṃ dhātūnaṃ kati"):
            rest.append(how_many_q("восемнадцати элементов"))
        elif t in ("##### Tikaṃ", "##### Dukaṃ"):
            rest.append(B.LABELS[t])
        elif t == "Pañhāpucchakaṃ.":
            rest.append(SEC["Pañhāpucchakaṃ"] + ".")
        elif t == "Dhātuvibhaṅgo niṭṭhito.":
            rest.append(S.CHAPTER_CLOSING.format(title=S.CHAPTER_TITLES[3]))
        else:
            rest.append(line_q2(t))
    return out + rest


# ---------------------------------------------------------------- 11. build and write
def build(fn, builder):
    pali = open(os.path.join(S.PALI_DIR, fn), encoding="utf-8").read().rstrip("\n").split("\n")
    nonempty = [S.ID.sub("", l).rstrip() for l in pali if l.strip()]
    ru = builder(nonempty)
    assert len(ru) == len(nonempty), (fn, len(ru), len(nonempty))
    for p, r in zip(nonempty, ru):
        assert p.count(DASH) + p.count("—") == r.count(DASH), ("dash count", p[:70], r[:70])
        assert p.startswith("#") == r.startswith("#") and p.split(" ")[0].count("#") == r.split(" ")[0].count("#"), (p[:40], r[:40])
    lines = S.attach_ids(pali, ru)
    S.write(os.path.join(S.RU_DIR, fn), lines)
    print("OK:", fn, "|", len(ru), "non-empty lines")


def main():
    build("2-ayatanavibhango.md", build_ch2)
    build("3-dhatuvibhango.md", build_ch3)
    if "--forms" in sys.argv:
        for k, v in sorted(MASC_SEEN.items()):
            print("m:", k, "->", v)


if __name__ == "__main__":
    main()
