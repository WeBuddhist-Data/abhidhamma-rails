"""Build the Russian plain zero-shot of pi-1 parts 3-02 and 3-03 (Rūpakaṇḍa, Rūpavibhatti:
the pairs, the sets of three, four ... eleven).

usage: python -I -X utf8 build_3-02_3-03_ru.py
Structure mirrors ref/en_build_3-02_3-03.py. Every recurring string is a fixed constant, so every
repeat is byte-identical. Unknown Pāli raises an error instead of being guessed.
Imports build_matika_ru (V) and build_ch2_01_sample_ru (DASH, S_LAHUTA, S_MUDUTA, S_KAMMANNATA,
S_JIVITA, NAMES_C); importing them does not rewrite their outputs.
"""
import pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SRC = ROOT / "AI_translation" / "pali" / "pi-1_split_chapters"
OUT = ROOT / "AI_translation" / "russian" / "pi-1-russian-plain-zeroshot_split_chapters"
PARTS = ["3-02-rupakandam.md", "3-03-rupakandam.md"]

sys.path.insert(0, str(HERE))
import build_matika_ru as M  # noqa: E402
import build_ch2_01_sample_ru as C  # noqa: E402

V = M.V
DASH = C.DASH
S_LAHUTA, S_MUDUTA, S_KAMMANNATA, S_JIVITA = C.S_LAHUTA, C.S_MUDUTA, C.S_KAMMANNATA, C.S_JIVITA
LIFE = C.NAMES_C["jīvitindriyaṃ"]  # ("жизненная способность", "жизненной способностью")

RF = "материальная форма"  # rūpa (matter)
RF_G = "материальной формы"

# =====================================================================================
# 1. Item names of material form: Pāli = (nominative, instrumental, gender)
# =====================================================================================
ITEMS_C = {
    "cakkhāyatanaṃ": ("сфера глаза", "сферой глаза", "f"),
    "sotāyatanaṃ": ("сфера уха", "сферой уха", "f"),
    "ghānāyatanaṃ": ("сфера носа", "сферой носа", "f"),
    "jivhāyatanaṃ": ("сфера языка", "сферой языка", "f"),
    "kāyāyatanaṃ": ("сфера тела", "сферой тела", "f"),
    "rūpāyatanaṃ": ("сфера видимых форм", "сферой видимых форм", "f"),
    "saddāyatanaṃ": ("сфера звуков", "сферой звуков", "f"),
    "gandhāyatanaṃ": ("сфера запахов", "сферой запахов", "f"),
    "rasāyatanaṃ": ("сфера вкусов", "сферой вкусов", "f"),
    "phoṭṭhabbāyatanaṃ": ("сфера осязаемого", "сферой осязаемого", "f"),
    "cakkhudhātu": ("элемент глаза", "элементом глаза", "m"),
    "sotadhātu": ("элемент уха", "элементом уха", "m"),
    "ghānadhātu": ("элемент носа", "элементом носа", "m"),
    "jivhādhātu": ("элемент языка", "элементом языка", "m"),
    "kāyadhātu": ("элемент тела", "элементом тела", "m"),
    "rūpadhātu": ("элемент видимых форм", "элементом видимых форм", "m"),
    "saddadhātu": ("элемент звуков", "элементом звуков", "m"),
    "gandhadhātu": ("элемент запахов", "элементом запахов", "m"),
    "rasadhātu": ("элемент вкусов", "элементом вкусов", "m"),
    "phoṭṭhabbadhātu": ("элемент осязаемого", "элементом осязаемого", "m"),
    "cakkhundriyaṃ": ("способность глаза", "способностью глаза", "f"),
    "sotindriyaṃ": ("способность уха", "способностью уха", "f"),
    "ghānindriyaṃ": ("способность носа", "способностью носа", "f"),
    "jivhindriyaṃ": ("способность языка", "способностью языка", "f"),
    "kāyindriyaṃ": ("способность тела", "способностью тела", "f"),
    "itthindriyaṃ": ("способность женственности", "способностью женственности", "f"),
    "purisindriyaṃ": ("способность мужественности", "способностью мужественности", "f"),
    "jīvitindriyaṃ": (LIFE[0], LIFE[1], "f"),
    "kāyaviññatti": ("телесное внешнее выражение", "телесным внешним выражением", "n"),
    "vacīviññatti": ("речевое внешнее выражение", "речевым внешним выражением", "n"),
    "ākāsadhātu": ("элемент пространства", "элементом пространства", "m"),
    "pathavīdhātu": ("элемент земли", "элементом земли", "m"),
    "āpodhātu": ("элемент воды", "элементом воды", "m"),
    "tejodhātu": ("элемент огня", "элементом огня", "m"),
    "vāyodhātu": ("элемент ветра", "элементом ветра", "m"),
    "rūpassa lahutā": (f"лёгкость {RF_G}", f"лёгкостью {RF_G}", "f"),
    "rūpassa mudutā": (f"мягкость {RF_G}", f"мягкостью {RF_G}", "f"),
    "rūpassa kammaññatā": (f"работоспособность {RF_G}", f"работоспособностью {RF_G}", "f"),
    "rūpassa upacayo": (f"рост {RF_G}", f"ростом {RF_G}", "m"),
    "rūpassa santati": (f"непрерывность {RF_G}", f"непрерывностью {RF_G}", "f"),
    "rūpassa jaratā": (f"старение {RF_G}", f"старением {RF_G}", "n"),
    "rūpassa aniccatā": (f"непостоянство {RF_G}", f"непостоянством {RF_G}", "n"),
    "kabaḷīkāro āhāro": ("съедаемая пища", "съедаемой пищей", "f"),
}
ITEMS = {k: v[0] for k, v in ITEMS_C.items()}

# =====================================================================================
# 2. Classification terms: predicates of «Какая материальная форма <VP>?» /
#    «… – это материальная форма, которая <VP>.» Built on the matrix predicates
#    (^1-M2-9/10/60/61/62/66/67/68, ^1-M1-4), put in the feminine singular.
# =====================================================================================
IS = "является "
TERMS = {
    "upādā": "является производной",
    "no upādā": "не является производной",
    "upādiṇṇaṃ": "охвачена цеплянием",
    "anupādiṇṇaṃ": "не охвачена цеплянием",
    "upādiṇṇupādāniyaṃ": "охвачена цеплянием и служит его объектом",
    "anupādiṇṇupādāniyaṃ": "не охвачена цеплянием, но служит его объектом",
    "sanidassanaṃ": "является видимой",
    "anidassanaṃ": "является невидимой",
    "sappaṭighaṃ": "способна к соударению",
    "appaṭighaṃ": "не способна к соударению",
    "indriyaṃ": "является способностью",
    "na indriyaṃ": "не является способностью",
    "mahābhūtaṃ": "является великим элементом",
    "na mahābhūtaṃ": "не является великим элементом",
    "viññatti": "является внешним выражением",
    "na viññatti": "не является внешним выражением",
    "cittasamuṭṭhānaṃ": "порождена умом",
    "na cittasamuṭṭhānaṃ": "не порождена умом",
    "cittasahabhu": "сосуществует с умом",
    "na cittasahabhu": "не сосуществует с умом",
    "cittānuparivatti": "следует за умом",
    "na cittānuparivatti": "не следует за умом",
    "ajjhattikaṃ": "относится к внутреннему",
    "bāhiraṃ": "относится к внешнему",
    "oḷārikaṃ": "является грубой",
    "sukhumaṃ": "является тонкой",
    "dūre": "находится далеко",
    "santike": "находится близко",
    "anidassanaṃ appaṭighaṃ dhammāyatanapariyāpannaṃ":
        "невидима и не способна к соударению и входит в сферу объектов ума",
}
for k, (nom, ins, g) in ITEMS_C.items():
    TERMS[k] = IS + ins
    if k.startswith("rūpassa "):
        TERMS["rūpassa na " + k[len("rūpassa "):]] = "не " + IS + ins
    else:
        TERMS["na " + k] = "не " + IS + ins

# genitive members of the contact chains («служит основой для …», «служит объектом для …»)
# (wording as build_3-01_ru.py: «является основой контакта глаза», «является объектом …»)
GEN = {
    "cakkhusamphassassa": "контакта глаза",
    "sotasamphassassa": "контакта уха",
    "ghānasamphassassa": "контакта носа",
    "jivhāsamphassassa": "контакта языка",
    "kāyasamphassassa": "контакта тела",
    "cakkhusamphassajāya vedanāya": "чувства, рождённого контактом глаза",
    "kāyasamphassajāya vedanāya": "чувства, рождённого контактом тела",
    "saññāya": "восприятия",
    "cetanāya": "намерения",
    "cakkhuviññāṇassa": "зрительного сознания",
    "kāyaviññāṇassa": "осязательного сознания",
}
REL = {"vatthu": "является основой", "ārammaṇaṃ": "является объектом"}
COMPOSITE = {}
for g_, ge in GEN.items():
    for r, rr in REL.items():
        for neg in (False, True):
            key = f"{g_} {'na ' if neg else ''}{r}"
            COMPOSITE[key] = (g_, neg, r)
            TERMS[key] = f"{'не ' if neg else ''}{rr} {ge}"

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


# adjective predicates that may share one «является» («является производной и грубой»)
ADJ = {TERMS[k] for k in ("upādā", "sanidassanaṃ", "anidassanaṃ", "oḷārikaṃ", "sukhumaṃ")}


def combine(a, b):
    """Join two predicates of one subject («материальная форма»)."""
    if a in ADJ and b in ADJ:
        return a + " и " + b[len(IS):]
    if " и " in b and ", но " not in b:      # b = «охвачена цеплянием и служит его объектом»
        return a + ", " + b
    if " и " in a and ", но " not in a:      # a = «охвачена цеплянием и служит его объектом»
        i = a.rfind(" и ")
        return a[:i] + ", " + a[i + 3:] + " и " + b
    return a + " и " + b


PE = "…pe…"


def term_vp(q):
    """Pāli classification term(s) of a question/answer -> Russian predicate."""
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
        assert all(IS in v for v in vps), vps
        if all(v.startswith("не ") for v in vps):  # 'na X…pe… na Y' = «не является X… не является Y» (as 3-01)
            vp = "… ".join(vps)
        else:
            assert not any(v.startswith("не ") for v in vps), vps
            vp = vps[0] + "… " + "… ".join(v.replace(IS, "", 1) for v in vps[1:])
    else:
        assert all(c in GEN for c in chain[:-1]) and chain[-1] in COMPOSITE, chain
        g_, neg, r = COMPOSITE[chain[-1]]
        vp = f"{'не ' if neg else ''}{REL[r]} " + "… ".join(GEN[c] for c in chain[:-1] + [g_])
    for p in reversed(prefix):
        vp = combine(TERMS[p], vp)
    return vp


# =====================================================================================
# 3. Answer lists of items
# =====================================================================================
CLAUSE = "yaṃ vā panaññampi atthi rūpaṃ"
KAMMA = "вследствие совершённых действий"
QUALS = {  # feminine, agreeing with «любая другая материальная форма»
    "kammassa katattā": f"возникшая {KAMMA}",
    "na kammassa katattā": f"возникшая не {KAMMA}",
    "cittajaṃ cittahetukaṃ cittasamuṭṭhānaṃ": "рождённая умом, имеющая корнем ум, порождённая умом",
    "na cittajaṃ na cittahetukaṃ na cittasamuṭṭhānaṃ":
        "не рождённая умом, не имеющая корнем ум, не порождённая умом",
}
WHATEVER = f"или же любая другая {RF}, "
ARISEN = {"f": "возникшая", "m": "возникший", "n": "возникшее", "pl": "возникшие"}
LEAD = {"kammassa katattā": KAMMA, "na kammassa katattā": "не " + KAMMA}
LVOCAB = set(ITEMS) | {CLAUSE} | set(QUALS)


def list_ru(a):
    """Pāli item list -> (Russian, ends_with_participle)."""
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
    toks = [t for t in toks if t != ","]
    if toks[0] in LEAD:  # «Сфера осязаемого, элемент воды, возникшие вследствие совершённых действий»
        lead, items = toks[0], toks[1:]
        assert items and all(t in ITEMS for t in items), toks
        g = "pl" if len(items) > 1 else ITEMS_C[items[0]][2]
        out = ", ".join(ITEMS[t] for t in items) + f", {ARISEN[g]} {LEAD[lead]}"
        return out[0].upper() + out[1:], True
    out, prev = "", None  # prev: 'item' | 'pe' | 'colon' | None
    j = 0
    while j < len(toks):
        t = toks[j]
        if t == PE:
            out += "…"; prev = "pe"; j += 1; continue
        if t == CLAUSE:
            q = toks[j + 1]
            assert q in QUALS, toks
            out += ", " + WHATEVER + QUALS[q] + ":"
            prev = "colon"; j += 2; continue
        assert t in ITEMS, t
        if prev == "item":
            out += ", "
        elif prev in ("pe", "colon"):
            out += " "
        out += ITEMS[t]; prev = "item"; j += 1
    return out[0].upper() + out[1:], False


# =====================================================================================
# 4. Definitions
# =====================================================================================
IA = {"m": "невидимый и способный к соударению", "n": "невидимое и способное к соударению",
      "f": "невидимая и способная к соударению"}
VA_F = "видимая и способная к соударению"
VA_ACC = "видимую и способную к соударению"
IA_INS = "невидимым и способным к соударению"
STRIKE = {"m": "ударялся, ударяется, ударится или мог бы удариться",
          "f": "ударялась, ударяется, ударится или могла бы удариться",
          "n": "ударялось, ударяется, ударится или могло бы удариться"}
ARISE = {"m": "возникал, возникает, возникнет или мог бы возникнуть",
         "n": "возникало, возникает, возникнет или могло бы возникнуть"}
UPADAYA = "производн{} от четырёх великих элементов"  # catunnaṃ mahābhūtānaṃ upādāya
SENS = ("чувствительностью, " + UPADAYA.format("ой") + ", входящей в индивидуальное бытие, "
        "невидимой и способной к соударению")  # pasādo attabhāvapariyāpanno anidassano sappaṭigho
BEING = {"m": "являющийся", "n": "являющееся"}
REL_ABOUT = {"m": "о который", "n": "о которое", "f": "о которую"}
REL_NOM = {"m": "который", "n": "которое", "f": "которая"}
NAMES_COMMON = "это мир, это врата, это океан, это чистота, это поле, это основа"
NAMES_EYE = "это проводник, это вожатый"
NAMES_TAIL = "это ближний берег, это пустая деревня"
PE_RU = "…"
FEEL_CHAIN = "{feel}… восприятие… намерение… {cons}"

# sense organs: noun, gender, genitive, sense faculty, instrumental, «о …»,
#               verb forms, object (acc. + quality), object (nom. + quality, gender), «о object»,
#               «в связи с object», object for «имеющий объектом …», contact, contact (ins.), consciousness
ORGANS = {
    "cakkhu": dict(n="глаз", g="m", gen="глаза", fac="способность глаза", ins="глазом", about="о глаз",
                   verbs="видели, видят, увидят или могли бы увидеть",
                   obj_acc=f"видимую форму, {VA_ACC}", obj_nom=(f"видимая форма, {VA_F}", "f"),
                   obj_about=f"о видимую форму, {VA_ACC}", obj_with="с видимой формой",
                   obj_ar="видимую форму", contact="контакт глаза", contact_i="контактом глаза",
                   cons="зрительное сознание", eye=True),
    "sotaṃ": dict(n="ухо", g="n", gen="уха", fac="способность уха", ins="ухом", about="об ухо",
                  verbs="слышали, слышат, услышат или могли бы услышать",
                  obj_acc=f"звук, {IA['m']}", obj_nom=(f"звук, {IA['m']}", "m"),
                  obj_about=f"о звук, {IA['m']}", obj_with="со звуком",
                  obj_ar="звук", contact="контакт уха", contact_i="контактом уха",
                  cons="слуховое сознание", eye=False),
    "ghānaṃ": dict(n="нос", g="m", gen="носа", fac="способность носа", ins="носом", about="о нос",
                   verbs="обоняли, обоняют, будут обонять или могли бы обонять",
                   obj_acc=f"запах, {IA['m']}", obj_nom=(f"запах, {IA['m']}", "m"),
                   obj_about=f"о запах, {IA['m']}", obj_with="с запахом",
                   obj_ar="запах", contact="контакт носа", contact_i="контактом носа",
                   cons="обонятельное сознание", eye=False),
    "jivhā": dict(n="язык", g="m", gen="языка", fac="способность языка", ins="языком", about="о язык",
                  verbs="вкушали, вкушают, вкусят или могли бы вкусить",
                  obj_acc=f"вкус, {IA['m']}", obj_nom=(f"вкус, {IA['m']}", "m"),
                  obj_about=f"о вкус, {IA['m']}", obj_with="со вкусом",
                  obj_ar="вкус", contact="контакт языка", contact_i="контактом языка",
                  cons="вкусовое сознание", eye=False),
    "kāyo": dict(n="тело", g="n", gen="тела", fac="способность тела", ins="телом", about="о тело",
                 verbs="касались, касаются, коснутся или могли бы коснуться",
                 obj_acc="осязаемого, невидимого и способного к соударению",
                 obj_nom=(f"осязаемое, {IA['n']}", "n"),
                 obj_about=f"об осязаемое, {IA['n']}", obj_with="с осязаемым",
                 obj_ar="осязаемое", contact="контакт тела", contact_i="контактом тела",
                 cons="осязательное сознание", eye=False),
}


def organ_names(o):
    s = f"это {o['n']}, это сфера {o['gen']}, это элемент {o['gen']}, это {o['fac']}, " + NAMES_COMMON + ", "
    if o["eye"]:
        s += NAMES_EYE + ", "
    return s + NAMES_TAIL


def organ_def(key, variant, vbracket=""):
    o = ORGANS[key]
    n, g = o["n"], o["g"]
    N = n[0].upper() + n[1:]
    if variant == "abbr":
        return f"{N}, {BEING[g]} чувствительностью, {UPADAYA.format('ой')}{PE_RU} {NAMES_TAIL.split(', ')[-1]}"
    head = f"{N}{vbracket}, {BEING[g]} {SENS}"
    feel = f"чувство, рождённое {o['contact_i']}"
    if variant == "a":
        mid = f"{n}, {IA[g]}, которым {o['verbs']} {o['obj_acc']}"
    elif variant == "b":
        on, og = o["obj_nom"]
        mid = f"{n}, {IA[g]}, {REL_ABOUT[g]} {STRIKE[og]} {on}"
    elif variant == "c":
        mid = f"{n}, {IA[g]}, {REL_NOM[g]} {STRIKE[g]} {o['obj_about']}"
    elif variant == "d":
        w = f"в связи {o['obj_with']}"
        ar_m = f"имеющий объектом {o['obj_ar']}"
        ar_n = f"имеющее объектом {o['obj_ar']}"
        chain = FEEL_CHAIN.format(feel=feel, cons=o["cons"])
        chain_ar = FEEL_CHAIN.format(feel=f"чувство, {ar_n}, рождённое {o['contact_i']}", cons=o["cons"])
        mid = (f"{n}, в зависимости от которого, {w}, {o['contact']} {ARISE['m']}{PE_RU} "
               f"{n}, в зависимости от которого, {w}, {chain} {ARISE['n']}{PE_RU} "
               f"{n}, в зависимости от которого {o['contact']}, {ar_m}, {ARISE['m']}{PE_RU} "
               f"{n}, в зависимости от которого {chain_ar} {ARISE['n']}")
    else:
        raise ValueError(variant)
    return f"{head}; {mid}; {organ_names(o)}"


COLOURS = ("синее, жёлтое, красное, белое, чёрное, малиновое{v1}, зелёное, зеленоватое, цвета побегов манго, "
           "длинное, короткое, мелкое, крупное, округлое, круглое, четырёхугольное{v2}, шестиугольное, "
           "восьмиугольное, шестнадцатиугольное, низкое, высокое, тень, солнечный свет, свет, тьма, облака, "
           "туман, дым, пыль, цвет и облик лунного диска, цвет и облик солнечного диска{v3}, "
           "цвет и облик звёзд, цвет и облик зеркального диска, "
           "цвет и облик драгоценных камней, раковин, жемчуга и берилла, цвет и облик золота и серебра")
SOUNDS = ("звук больших барабанов, звук малых барабанов, звук раковин, звук бубнов, звук пения, "
          "звук музыкальных инструментов, звук тарелок, звук хлопков в ладоши, звук голосов живых существ, "
          "звук соударения предметов, звук ветра, звук воды, звук людей, звук нечеловеческих существ")
SMELLS = ("запах корней, запах сердцевины дерева, запах коры, запах листьев, запах цветов, запах плодов, "
          "запах сырого мяса, запах гнили, приятный запах, неприятный запах")
TASTES = ("вкус корней, вкус стеблей, вкус коры, вкус листьев, вкус цветов, вкус плодов, кислое, сладкое, "
          "горькое, острое, солёное, щелочное, кисловатое{v1}, вяжущее, вкусное, невкусное")
TOUCH_HEAD = ("Элемент земли, элемент огня, элемент ветра, твёрдое, мягкое, гладкое, шероховатое, "
              "приятное при контакте, болезненное при контакте, тяжёлое, лёгкое")

# sense objects: noun (nom.), gender, quality, list, names, organ key, «в связи с которой/которым»,
#                «с которой/которым как с объектом», relative pronoun for the verb
OBJECTS = {
    "rūpa": dict(n="видимая форма", g="f", q=VA_F, organ="cakkhu",
                 names="это видимая форма, это сфера видимых форм, это элемент видимых форм",
                 with_="в связи с которой", as_obj="с которой как с объектом", rel_v="которую"),
    "sadda": dict(n="звук", g="m", q=IA["m"], organ="sotaṃ",
                  names="это звук, это сфера звуков, это элемент звуков",
                  with_="в связи с которым", as_obj="с которым как с объектом", rel_v="который"),
    "gandha": dict(n="запах", g="m", q=IA["m"], organ="ghānaṃ",
                   names="это запах, это сфера запахов, это элемент запахов",
                   with_="в связи с которым", as_obj="с которым как с объектом", rel_v="который"),
    "rasa": dict(n="вкус", g="m", q=IA["m"], organ="jivhā",
                 names="это вкус, это сфера вкусов, это элемент вкусов",
                 with_="в связи с которым", as_obj="с которым как с объектом", rel_v="который"),
    "phoṭṭhabba": dict(n="осязаемое", g="n", q=IA["n"], organ="kāyo",
                       names="это осязаемое, это сфера осязаемого, это элемент осязаемого",
                       with_="в связи с которым", as_obj="с которым как с объектом", rel_v="которого"),
}
COLOUR_LOOK = "являющаяся цветом и обликом"  # vaṇṇanibhā


def object_head(key, bracket_variants):
    ob = OBJECTS[key]
    if key == "rūpa":
        if bracket_variants:
            col = COLOURS.format(v1=V("s", "Sī., Syā.", "mañjeṭṭhakaṃ"), v2=V("s", "Sī., Ka.", "caturassaṃ"),
                                 v3=V("s", "Sī., Syā.", "suriyamaṇḍalassa"))
        else:
            col = COLOURS.format(v1="", v2="", v3="")
        d = f"{UPADAYA.format('ая')}, {COLOUR_LOOK}, {VA_F}"
        return f"Видимая форма, {d}: {col}, или же любая другая видимая форма, {d}"
    if key == "phoṭṭhabba":
        return TOUCH_HEAD
    lst = {"sadda": SOUNDS, "gandha": SMELLS, "rasa": TASTES}[key]
    if key == "rasa":
        lst = lst.format(v1=V("p", "Sī.", "lapilakaṃ") if bracket_variants else "")
    d = f"{UPADAYA.format('ый')}, {ob['q']}"
    N = ob["n"][0].upper() + ob["n"][1:]
    return f"{N}, {d}: {lst}, или же любой другой {ob['n']}, {d}"


def object_def(key, variant, bracket_variants=False):
    ob = OBJECTS[key]
    o = ORGANS[ob["organ"]]
    if variant == "abbr":
        if key == "rūpa":
            return f"Видимая форма, {UPADAYA.format('ая')}, {COLOUR_LOOK}{PE_RU} это элемент видимых форм"
        if key == "phoṭṭhabba":
            return f"Элемент земли{PE_RU} это элемент осязаемого"
        raise ValueError(key)
    head = object_head(key, bracket_variants)
    n, g, q = ob["n"], ob["g"], ob["q"]
    feel = f"чувство, рождённое {o['contact_i']}"
    chain = FEEL_CHAIN.format(feel=feel, cons=o["cons"])
    dep = f"в зависимости от {o['gen']}"
    if variant == "a":
        mid = f"{n}, {q}, {ob['rel_v']} {o['verbs']} {o['ins']}, {IA_INS}"
    elif variant == "b":
        mid = f"{n}, {q}, {REL_ABOUT[g]} {STRIKE[o['g']]} {o['n']}, {IA[o['g']]}"
    elif variant == "c":
        mid = f"{n}, {q}, {REL_NOM[g]} {STRIKE[g]} {o['about']}, {IA[o['g']]}"
    elif variant == "d":
        mid = (f"{n}, {ob['with_']}, {dep}, {o['contact']} {ARISE['m']}{PE_RU} "
               f"{n}, {ob['with_']}, {dep}, {chain} {ARISE['n']}{PE_RU} "
               f"{n}, {ob['as_obj']}, {dep}, {o['contact']} {ARISE['m']}{PE_RU} "
               f"{n}, {ob['as_obj']}, {dep}, {chain} {ARISE['n']}")
    else:
        raise ValueError(variant)
    return f"{head}; {mid}; {ob['names']}"


IN_RUPA = f"То, что у {RF_G} есть "
OWN_OTHERS = ", внутреннее или внешнее, охваченное цеплянием или не охваченное цеплянием"
SPEECH = ("речь, слово, способ речи, произнесение, голос, звучание голоса, речь, членораздельная речь")
MINDS = "при благом уме, или при неблагом уме, или при этически неопределённом уме"
INTIM = "внешнее выражение, оповещение, состояние оповещённости"  # viññatti viññāpanā viññāpitattaṃ
WATER = (f"То, что есть вода, то, что считается водой, влага, то, что считается влагой, "
         f"связующее свойство {RF_G}")
ITTHI = ("То, что у женщины есть женская внешность, женский признак, женское поведение, женская манера, "
         "женственность, женская природа")

SHORT_DEFS = {
    "Yaṃ itthiyā itthiliṅgaṃ itthinimittaṃ itthikuttaṃ itthākappo itthattaṃ itthibhāvo": ITTHI,
    "Yaṃ itthiyā itthiliṅgaṃ itthinimittaṃ itthikuttaṃ itthākappo itthattaṃ itthibhāvo "
    "[itthittaṃ itthībhāvo (syā.)]": ITTHI + V("s", "Syā.", "itthittaṃ itthībhāvo"),
    "Yaṃ purisassa purisaliṅgaṃ purisanimittaṃ purisakuttaṃ purisākappo purisattaṃ purisabhāvo":
        "То, что у мужчины есть мужская внешность, мужской признак, мужское поведение, мужская манера, "
        "мужественность, мужская природа",
    "Yo tesaṃ rūpīnaṃ dhammānaṃ āyu ṭhiti yapanā yāpanā iriyanā vattanā pālanā jīvitaṃ jīvitindriyaṃ":
        "То, что у этих материальных явлений есть " + S_JIVITA,
    "Yā kusalacittassa vā akusalacittassa vā abyākatacittassa vā abhikkamantassa vā paṭikkamantassa vā "
    "ālokentassa vā vilokentassa vā samiñjentassa vā pasārentassa vā kāyassa thambhanā santhambhanā "
    "santhambhitattaṃ viññatti viññāpanā viññāpitattaṃ":
        f"То, что {MINDS} у того, кто идёт вперёд, или идёт назад, или смотрит прямо, или смотрит по сторонам, "
        f"или сгибает, или разгибает, есть напряжённость тела, полная напряжённость, "
        f"состояние полной напряжённости, {INTIM}",
    "Yo ākāso ākāsagataṃ aghaṃ aghagataṃ vivaro vivaragataṃ asamphuṭṭhaṃ catūhi mahābhūtehi":
        "То, что есть пространство, то, что считается пространством, незаполненное, то, что считается "
        "незаполненным, просвет, то, что считается просветом, не затронутое четырьмя великими элементами",
    "Yaṃ āpo āpogataṃ sineho sinehagataṃ bandhanattaṃ rūpassa": WATER,
    "Yā rūpassa lahutā lahupariṇāmatā adandhanatā avitthanatā": IN_RUPA + S_LAHUTA,
    "Yā rūpassa mudutā maddavatā akakkhaḷatā akathinatā": IN_RUPA + S_MUDUTA,
    "Yā rūpassa kammaññatā kammaññattaṃ kammaññabhāvo": IN_RUPA + S_KAMMANNATA,
    "Yo āyatanānaṃ ācayo, so rūpassa upacayo":
        f"То, что является накоплением сфер восприятия, есть рост {RF_G}",
    "Yo rūpassa upacayo, sā rūpassa santati":
        f"То, что является ростом {RF_G}, есть непрерывность {RF_G}",
    "Yā rūpassa jarā jīraṇatā khaṇḍiccaṃ pāliccaṃ valittacatā āyuno saṃhāni indriyānaṃ paripāko":
        IN_RUPA + "старость, одряхление, сломанные зубы, седые волосы, морщинистая кожа, сокращение срока жизни, "
        "изношенность способностей",
    "Yo rūpassa khayo vayo bhedo paribhedo aniccatā antaradhānaṃ":
        IN_RUPA + "уничтожение, угасание, распад, полный распад, непостоянство, исчезновение",
    "Yaṃ kakkhaḷaṃ kharagataṃ [kharigataṃ (ka.)] kakkhaḷattaṃ kakkhaḷabhāvo ajjhattaṃ vā bahiddhā vā "
    "upādiṇṇaṃ vā anupādiṇṇaṃ vā":
        "То, что есть твёрдое, то, что считается жёстким" + V("s", "Ka.", "kharigataṃ")
        + ", твёрдость, состояние твёрдости" + OWN_OTHERS,
    "Yaṃ āpo āpogataṃ sineho sinehagataṃ bandhanattaṃ rūpassa ajjhattaṃ vā bahiddhā vā upādiṇṇaṃ vā "
    "anupādiṇṇaṃ vā": WATER + OWN_OTHERS,
    "Yaṃ tejo tejogataṃ usmā usmāgataṃ usumaṃ usumagataṃ ajjhattaṃ vā bahiddhā vā upādiṇṇaṃ vā anupādiṇṇaṃ vā":
        "То, что есть огонь, то, что считается огнём, тепло, то, что считается теплом, жар, "
        "то, что считается жаром" + OWN_OTHERS,
    "Yaṃ vāyo vāyogataṃ thambhitattaṃ rūpassa ajjhattaṃ vā bahiddhā vā upādiṇṇaṃ vā anupādiṇṇaṃ vā":
        f"То, что есть ветер, то, что считается ветром, состояние напряжённости {RF_G}" + OWN_OTHERS,
}
_VACI_HEAD = f"То, что {MINDS} есть {SPEECH}"
_VACI_TAIL = f"это называется речью. То, что посредством этой речи есть {INTIM}"
_KABALI = ("Варёный рис, каша, толокно, рыба, мясо, молоко, простокваша, топлёное масло, сливочное масло, "
           "растительное масло, мёд, патока, или же любая другая материальная форма, которую в той или иной "
           "местности те или иные существа едят ртом, разжёвывают зубами, проглатывают через горло и которая "
           "наполняет живот, питательная сущность, благодаря которой существа поддерживают свою жизнь")
_VACI_P = ("Yā kusalacittassa vā akusalacittassa vā abyākatacittassa vā vācā girā byappatho udīraṇaṃ {g} "
           "ghosakammaṃ vācā vacībhedo{sep} ayaṃ vuccati vācā. Yā tāya vācāya viññatti viññāpanā viññāpitattaṃ")
SHORT_DEFS[_VACI_P.format(g="ghoso", sep=" –")] = f"{_VACI_HEAD}, {DASH} {_VACI_TAIL}"
SHORT_DEFS[_VACI_P.format(g="ghoso", sep=",")] = f"{_VACI_HEAD}, {_VACI_TAIL}"
SHORT_DEFS[_VACI_P.format(g="dhoso", sep=",")] = f"{_VACI_HEAD}, {_VACI_TAIL}"  # ^1-850 'dhoso' (slip)
_KAB_P = ("Odano kummāso sattu maccho maṃsaṃ khīraṃ dadhi sappi navanītaṃ telaṃ madhu phāṇitaṃ, yaṃ vā "
          "panaññampi atthi rūpaṃ yamhi yamhi janapade tesaṃ tesaṃ sattānaṃ mukhāsiyaṃ dantavikhādanaṃ "
          "galajjhoharaṇīyaṃ kucchivitthambhanaṃ{sep} yāya ojāya sattā yāpenti")
SHORT_DEFS[_KAB_P.format(sep=",")] = _KABALI
SHORT_DEFS[_KAB_P.format(sep="")] = _KABALI  # ^1-880: no comma before yāya

ORG_RE = re.compile(r"^(Yaṃ cakkhu|Yaṃ sotaṃ|Yaṃ ghānaṃ|Yā jivhā|Yo kāyo)( \[cakkhuṃ \(sī\. syā\.\)\])? "
                    r"catunnaṃ mahābhūtānaṃ upādāya pasādo")
OBJ_RE = re.compile(r"^(Yaṃ rūpaṃ|Yo saddo|Yo gandho|Yo raso) catunnaṃ mahābhūtānaṃ upādāya")
OBJ_KEY = {"Yaṃ rūpaṃ": "rūpa", "Yo saddo": "sadda", "Yo gandho": "gandha", "Yo raso": "rasa"}


def def_ru(a):
    """Russian of a definition answer, or None if `a` is an item list."""
    if a in SHORT_DEFS:
        return SHORT_DEFS[a]
    m = ORG_RE.match(a)
    if m:
        key = m.group(1).split()[1]
        vb = V("s", "Sī., Syā.", "cakkhuṃ") if m.group(2) else ""
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
# 5. Fixed lines and headings (ru-zeroshot-terms.md §1)
# =====================================================================================
NUM = [("du", "два"), ("ti", "три"), ("catub", "четыре"), ("pañca", "пять"), ("cha", "шесть"),
       ("satta", "семь"), ("aṭṭha", "восемь"), ("nava", "девять"), ("dasa", "десять"),
       ("ekādasa", "одиннадцать")]
CLS = "Классификация по {}"
HEADINGS = {
    "##### Dukaniddeso": "##### Разъяснение классификации по два",
    "###### Upādābhājanīyaṃ": "###### Разбор производной материальной формы",
    "##### Tikaniddeso": "##### Разъяснение классификации по три",
}
SETS = {"Catukkaṃ": "четыре", "Pañcakaṃ": "пять", "Chakkaṃ": "шесть", "Sattakaṃ": "семь", "Aṭṭhakaṃ": "восемь",
        "Navakaṃ": "девять", "Dasakaṃ": "десять", "Ekādasakaṃ": "одиннадцать"}
for p, r in SETS.items():
    HEADINGS[f"##### {p}"] = "##### " + CLS.format(r)

KN = "познаваемая"  # -viññeyya
LINES = {
    "Idaṃ taṃ rūpaṃ upādā.": f"Это {RF}, которая {TERMS['upādā']}.",
    "Upādābhājanīyaṃ.": "Разбор производной материальной формы.",
    "Rūpakaṇḍe paṭhamabhāṇavāro.": "Первый раздел для чтения вслух в разделе о материальной форме.",
    "Idaṃ taṃ rūpaṃ no upādā.": f"Это {RF}, которая {TERMS['no upādā']}.",
    "Dukaniddeso.": "Разъяснение классификации по два.",
    "Tikaniddeso.": "Разъяснение классификации по три.",
    "Aṭṭhamabhāṇavāro.": "Восьмой раздел для чтения вслух.",
    "Rūpavibhatti.": "Классификация материальной формы.",
    "Rūpakaṇḍaṃ niṭṭhitaṃ.": "Раздел о материальной форме завершён.",
    "Rūpāyatanaṃ diṭṭhaṃ, saddāyatanaṃ sutaṃ, gandhāyatanaṃ rasāyatanaṃ phoṭṭhabbāyatanaṃ mutaṃ, "
    "sabbaṃ rūpaṃ manasā viññātaṃ rūpaṃ.":
        "Сфера видимых форм есть увиденное, сфера звуков есть услышанное, сфера запахов, сфера вкусов и "
        f"сфера осязаемого есть ощущённое, и вся {RF} есть {RF}, познанная умом.",
}
for p, r in SETS.items():
    LINES[f"{p}."] = CLS.format(r) + "."
for p, r in NUM:
    LINES[f"Evaṃ {p}vidhena rūpasaṅgaho."] = f"Такова классификация {RF_G} по {r}."
LINES["Evaṃ catubbidhena rūpasaṅgaho."] = LINES.pop("Evaṃ catubvidhena rūpasaṅgaho.")
LINES["Evaṃ chabbidhena rūpasaṅgaho."] = LINES.pop("Evaṃ chavidhena rūpasaṅgaho.")


def _kn(subj, by):
    return f"{subj} есть {RF}, {KN} {by}"


_FIVE = ", ".join(_kn(ITEMS[s], b) for s, b in (("rūpāyatanaṃ", "глазом"), ("saddāyatanaṃ", "ухом"),
                                                 ("gandhāyatanaṃ", "носом"), ("rasāyatanaṃ", "языком")))
_BODY = _kn(ITEMS["phoṭṭhabbāyatanaṃ"], "телом")
_MANODHATU = _kn("сфера видимых форм, сфера звуков, сфера запахов, сфера вкусов и сфера осязаемого",
                 "элементом ума")
_LAST = "и " + _kn(f"вся {RF}", "элементом умственного сознания") + "."
_AGREE = (_kn("желанное осязаемое, приятное при контакте,", "телом") + ", "
          + _kn("нежеланное осязаемое, болезненное при контакте,", "телом"))
_CAP = lambda s: s[0].upper() + s[1:]  # noqa: E731
LINES[("Rūpāyatanaṃ cakkhuviññeyyaṃ rūpaṃ, saddāyatanaṃ sotaviññeyyaṃ rūpaṃ, gandhāyatanaṃ ghānaviññeyyaṃ "
       "rūpaṃ, rasāyatanaṃ jivhāviññeyyaṃ rūpaṃ, phoṭṭhabbāyatanaṃ kāyaviññeyyaṃ rūpaṃ, sabbaṃ rūpaṃ "
       "manoviññeyyaṃ rūpaṃ.")] = \
    _CAP(_FIVE) + f", {_BODY}, и " + _kn(f"вся {RF}", "умом") + "."
LINES[("Rūpāyatanaṃ cakkhuviññeyyaṃ rūpaṃ, saddāyatanaṃ sotaviññeyyaṃ rūpaṃ, gandhāyatanaṃ ghānaviññeyyaṃ "
       "rūpaṃ, rasāyatanaṃ jivhāviññeyyaṃ rūpaṃ, phoṭṭhabbāyatanaṃ kāyaviññeyyaṃ rūpaṃ, rūpāyatanaṃ "
       "saddāyatanaṃ gandhāyatanaṃ rasāyatanaṃ phoṭṭhabbāyatanaṃ manodhātuviññeyyaṃ rūpaṃ, sabbaṃ rūpaṃ "
       "manoviññāṇadhātuviññeyyaṃ rūpaṃ.")] = \
    _CAP(_FIVE) + f", {_BODY}, {_MANODHATU}, {_LAST}"
LINES[("Rūpāyatanaṃ cakkhuviññeyyaṃ rūpaṃ, saddāyatanaṃ sotaviññeyyaṃ rūpaṃ, gandhāyatanaṃ ghānaviññeyyaṃ "
       "rūpaṃ, rasāyatanaṃ jivhāviññeyyaṃ rūpaṃ, manāpiyo phoṭṭhabbo sukhasamphasso kāyaviññeyyaṃ rūpaṃ, "
       "amanāpiyo phoṭṭhabbo dukkhasamphasso kāyaviññeyyaṃ rūpaṃ, rūpāyatanaṃ saddāyatanaṃ gandhāyatanaṃ "
       "rasāyatanaṃ phoṭṭhabbāyatanaṃ manodhātuviññeyyaṃ rūpaṃ, sabbaṃ rūpaṃ manoviññāṇadhātuviññeyyaṃ rūpaṃ.")] = \
    _CAP(_FIVE) + f", {_AGREE}, {_MANODHATU}, {_LAST}"

FRAME_Q = "Какая " + RF + " {}{}"
FRAME_A = "{}{}" + DASH + " это " + RF + ", которая {}{}"

QA_RE = re.compile(r"^Katamaṃ taṃ rūpaṃ (.+?)([?.]) (.+) – idaṃ taṃ rūpaṃ (.+?)([.?])$")
NOQ_RE = re.compile(r"^Katamaṃ taṃ rūpaṃ (\S+ \S+) (itthindriyaṃ…pe… kabaḷīkāro āhāro|"
                    r"cakkhāyatanaṃ…pe… kāyāyatanaṃ, .+) – idaṃ taṃ rūpaṃ (.+?)([.?])$")


def qa_ru(line):
    m = QA_RE.match(line)
    lower = False
    if m:
        q, qp, a, q2, ap = m.groups()
        qtext = FRAME_Q.format(term_vp(q), qp)
    elif " – " not in line:  # ^1-595, ^1-646: bare list answer, no closing formula
        m = re.match(r"^Katamaṃ taṃ rūpaṃ (.+?)\? (.+)\.$", line)
        lst, _ = list_ru(m.group(2))
        return FRAME_Q.format(term_vp(m.group(1)), "?") + " " + lst + "."
    else:  # ^1-895, ^1-939: no question mark after the question (source as written)
        m = NOQ_RE.match(line)
        if not m:
            raise ValueError(line)
        q, a, q2, ap = m.groups()
        qtext = FRAME_Q.format(term_vp(q), "")
        a = a[0].upper() + a[1:]
        lower = True
    ar = def_ru(a)
    sep = ", "
    if ar is None:
        ar, part = list_ru(a)
        sep = ", " if part else " "
    if lower:
        ar = ar[0].lower() + ar[1:]
    return qtext + " " + FRAME_A.format(ar, sep, term_vp(q2), ap)


def line_ru(line):
    if line.startswith("#"):
        return HEADINGS[line]
    if line.startswith("Katamaṃ taṃ rūpaṃ"):
        return qa_ru(line)
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
        ru = [line_ru(l.strip()) for l in lines]
        ru[-1] += f" ^{m.group(1)}"
        out.append("\n".join(ru))
    t = "\n\n".join(out) + "\n"
    assert "—" not in t and ":-" not in t
    return t


if __name__ == "__main__":
    for part in PARTS:
        t = build(part)
        (OUT / part).write_text(t, encoding="utf-8", newline="\n")
        print("wrote", OUT / part, t.count("\n\n") + 1, "segments")
