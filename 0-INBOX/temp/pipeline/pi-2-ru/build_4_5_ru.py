# -*- coding: utf-8 -*-
"""pi-2 Vibhaṅga, Russian plain zero-shot: chapters 4 (Saccavibhaṅga) and 5 (Indriyavibhaṅga).

usage: python -I -X utf8 build_4_5_ru.py
Writes AI_translation\\russian\\pi-2-russian-plain-zeroshot_split_chapters\\4-saccavibhango.md and 5-indriyavibhango.md.
Reuses build_ch1_sample_ru (S), build_1_ru (B: ITEMS / SURF matrix lexicon, frames) and build_2_3_ru (T: line_q2
machinery, pi-1 lookup by block ID, sense-organ strings, feeling strings, manāyatana classification).
pi-1 strings (path factors, faculties, jhāna formula, lokuttara opening, ageing list …) are copied from the pi-1
Russian and asserted byte for byte. Unknown Pāli raises KeyError (nothing is guessed). Importing writes nothing.
"""
import os, re, sys

HERE = r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-ru"
sys.path.insert(0, HERE)
import build_ch1_sample_ru as S  # noqa: E402
import build_1_ru as B  # noqa: E402
import build_2_3_ru as T  # noqa: E402

DASH = S.DASH
cap, low = S.cap, S.low
PE = "\x01"
PI1 = T.PI1
PI1_ALL = "\n".join(open(os.path.join(S.PI1_RU_DIR, f), encoding="utf-8").read()
                    for f in sorted(os.listdir(S.PI1_RU_DIR)) if f.endswith(".md"))


def edit(s, old, new):
    assert old in s, (old, s[:80])
    return s.replace(old, new, 1)


def in_pi1(*parts):
    for p in parts:
        assert p in PI1_ALL, "not in pi-1: " + p[:90]


q = T.q            # Что такое здесь X?


def called(ins, quoted=True):
    return T.called(ins, quoted)


def enum(items):
    return T.enum(items)


# ================================================================ 1. truths (names)
SUFF = "страдания"
DUKKHA = ("страдание", "страданием")                                   # dukkha (truth / Abhidhamma)
SAMUDAYA = ("возникновение страдания", "возникновением страдания")     # dukkhasamudayo
NIRODHA = ("прекращение страдания", "прекращением страдания")          # dukkhanirodho
PATIPADA = ("способ практики, ведущий к прекращению страдания",        # dukkhanirodhagāminī paṭipadā [pi-1 ^1-1238 amoho]
            "способом практики, ведущим к прекращению страдания")
PATIPADA_INS_CLOSED = PATIPADA[1]
in_pi1("знание способа практики, ведущего к прекращению страдания")
ARIYA = {   # Pāli -> (nom, ins); ariyasacca = благородная истина [pi-5]
    "dukkhaṃ ariyasaccaṃ": ("благородная истина о страдании", "благородной истиной о страдании"),
    "dukkhasamudayaṃ ariyasaccaṃ": ("благородная истина о возникновении страдания", "благородной истиной о возникновении страдания"),
    "dukkhanirodhaṃ ariyasaccaṃ": ("благородная истина о прекращении страдания", "благородной истиной о прекращении страдания"),
    "dukkhanirodhagāminī paṭipadā ariyasaccaṃ": ("благородная истина о способе практики, ведущем к прекращению страдания",
                                                 "благородной истиной о способе практики, ведущем к прекращению страдания"),
}
SACCA = {   # Pañhāpucchaka subjects / headings (pi-3 «истина о страдании», «истина о пути»; samudaya = возникновение)
    "Dukkhasaccaṃ": ("Истина о страдании", "Истину о страдании"),
    "Samudayasaccaṃ": ("Истина о возникновении страдания", "Истину о возникновении страдания"),
    "Nirodhasaccaṃ": ("Истина о прекращении страдания", "Истину о прекращении страдания"),
    "Maggasaccaṃ": ("Истина о пути", "Истину о пути"),
}
FOUR_ARIYA = "Четыре благородные истины"
FOUR = "Четыре истины"

# ================================================================ 2. path factors [pi-1]
MAGGA = {
    "sammādiṭṭhi": ("правильное воззрение", "правильным воззрением"),
    "sammāsaṅkappo": ("правильный помысел", "правильным помыслом"),
    "sammāvācā": ("правильная речь", "правильной речью"),
    "sammākammanto": ("правильное действие", "правильным действием"),
    "sammāājīvo": ("правильный образ жизни", "правильным образом жизни"),
    "sammāvāyāmo": ("правильное усилие", "правильным усилием"),
    "sammāsati": ("правильная осознанность", "правильной осознанностью"),
    "sammāsamādhi": ("правильное сосредоточение", "правильным сосредоточением"),
}
EIGHT_FACTORS = ", ".join(MAGGA[k][0] for k in MAGGA)
FIVE_FACTORS = "правильное воззрение, правильный помысел, правильное усилие, правильная осознанность, правильное сосредоточение"
assert "Правильное воззрение, правильный помысел, правильное усилие, правильная осознанность, правильное сосредоточение." in PI1["^1-89"]
EIGHTFOLD = "восьмичастный путь"      # aṭṭhaṅgiko maggo [pi-1 ^1-337]
FIVEFOLD = "пятичастный путь"         # pañcaṅgiko maggo [pi-1 ^1-58]
in_pi1("есть " + EIGHTFOLD, "есть " + FIVEFOLD)


def pi1_def(bid, end):
    """pi-1 'То, что в это время есть …' body without «в это время» (pi-2 lacks tasmiṃ samaye)."""
    body = T.pi1_body(bid, end)
    return edit(body, "То, что в это время есть ", "То, что есть ")


def pe(body, n, tail_from):
    """head of n items … tail starting at `tail_from` (the Pāli …pe… abbreviation)."""
    pre = "То, что есть "
    assert body.startswith(pre)
    items = body[len(pre):].split(", ")
    return pre + ", ".join(items[:n]) + "… " + body[body.rindex(tail_from):]


DITTHI_L = pi1_def("^1-297", ", – это правильное воззрение в это время")     # … фактор пути, входящий в путь
SANKAPPA_L = pi1_def("^1-298", ", – это правильный помысел в это время")
VACA_L = pi1_def("^1-299", ", – это правильная речь в это время")
KAMMANTA_L = pi1_def("^1-300", ", – это правильное действие в это время")
AJIVA_L = pi1_def("^1-301", ", – это правильный образ жизни в это время")
VAYAMA_L = pi1_def("^1-302", ", – это правильное усилие в это время")
SATI_L = pi1_def("^1-303", ", – это правильная осознанность в это время")
SAMADHI_L = pi1_def("^1-304", ", – это правильное сосредоточение в это время")
VAR_VERAMANI = " [вариант написания (Ka.): veramaṇi; так же и далее]"          # [veramaṇi (ka.) evamuparipi]
VAR_VIRIYARAMBHO = " [вариант написания (Sī., Syā.): viriyārambho]"            # [viriyārambho (sī. syā.)]
in_pi1("усердия" + VAR_VIRIYARAMBHO)

# Abhidhammabhājanīya factor definitions: Pāli body (between "? " and " – ") -> Russian body
FACTOR_BODY = {
    "Yā paññā pajānanā…pe… amoho dhammavicayo sammādiṭṭhi dhammavicayasambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ":
        pe(DITTHI_L, 2, "отсутствие заблуждения"),
    "Yo takko vitakko…pe… sammāsaṅkappo maggaṅgaṃ maggapariyāpannaṃ": pe(SANKAPPA_L, 2, "правильный помысел"),
    "Yā catūhi vacīduccaritehi ārati virati paṭivirati veramaṇī [veramaṇi (ka.) evamuparipi] akiriyā akaraṇaṃ "
    "anajjhāpatti velāanatikkamo setughāto sammāvācā maggaṅgaṃ maggapariyāpannaṃ":
        edit(VACA_L, "уклонение,", "уклонение" + VAR_VERAMANI + ","),
    "Yā tīhi kāyaduccaritehi ārati virati paṭivirati veramaṇī akiriyā akaraṇaṃ anajjhāpatti velāanatikkamo setughāto "
    "sammākammanto maggaṅgaṃ maggapariyāpannaṃ": KAMMANTA_L,
    "Yā micchā ājīvā ārati virati paṭivirati veramaṇī akiriyā akaraṇaṃ anajjhāpatti velāanatikkamo setughāto "
    "sammāājīvo maggaṅgaṃ maggapariyāpannaṃ": AJIVA_L,
    "Yo cetasiko vīriyārambho [viriyārambho (sī. syā.)] …pe… sammāvāyāmo vīriyasambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ":
        edit(pe(VAYAMA_L, 1, "правильное усилие, фактор"), "усердия…", "усердия" + VAR_VIRIYARAMBHO + "…"),
    "Yo cetasiko vīriyārambho…pe… sammāvāyāmo vīriyasambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ":
        pe(VAYAMA_L, 1, "правильное усилие, фактор"),
    "Yā sati anussati…pe… sammāsati satisambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ": pe(SATI_L, 2, "правильная осознанность, фактор"),
    "Yā cittassa ṭhiti saṇṭhiti…pe… sammāsamādhi samādhisambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ":
        pe(SAMADHI_L, 2, "правильное сосредоточение, фактор"),
    "Yā cittassa ṭhiti…pe… sammāsamādhi samādhisambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ":
        pe(SAMADHI_L, 1, "правильное сосредоточение, фактор"),
}

# ================================================================ 3. Suttanta: dukkha
JATI_L = ("То, что у тех или иных существ в том или ином классе существ есть рождение, зарождение, вхождение, "
          "появление, проявление совокупностей, обретение сфер восприятия")
JARA_PI1 = T.pi1_body("^1-643", ", – это материальная форма")
JARA_ITEMS = JARA_PI1[len("То, что у материальной формы есть "):]          # старение, одряхление, … изношенность способностей
JARA_L = "То, что у тех или иных существ в том или ином классе существ есть " + JARA_ITEMS
MARANA_L = ("То, что у тех или иных существ есть уход из того или иного класса существ, выбывание, распад, исчезновение, "
            "гибель, смерть, кончина, распад совокупностей, оставление тела, прекращение жизненной способности")
BYASANA = ("У того, кого постигло несчастье с родными, или постигло несчастье с имуществом, или постигло несчастье болезни, "
           "или постигло несчастье в нравственности, или постигло несчастье в воззрениях, у того, кто охвачен тем или иным "
           "несчастьем, кого коснулось то или иное болезненное явление, есть ")
SOKA_L = BYASANA + ("печаль, горевание, состояние горевания, внутренняя печаль, глубокая внутренняя печаль, "
                    "изнурение ума, уныние, стрела печали")
PARIDEVA_L = BYASANA + ("плач, стенания, оплакивание, причитание, состояние плача, состояние стенаний, речь, болтовня, "
                        "бессвязная болтовня, сетование, проявление сетования, состояние сетования "
                        "[вариант написания (Syā.): lālapo lālapanā lālapitattaṃ]")
UPAYASA_L = BYASANA + "удручённость, отчаяние, состояние удручённости, состояние отчаяния"
GRIEF5 = "печаль, стенания, боль, уныние и отчаяние"                       # sokaparidevadukkhadomanassupāyāsā
GRIEF5_DAT = "печали, стенаниям, боли, унынию и отчаянию"
FIVE_OBJ_ADJ = "нежеланные, немилые, неприятные видимые формы, звуки, запахи, вкусы и осязаемое"   # aniṭṭhā akantā amanāpā rūpā …
FIVE_OBJ_ADJ_P = "желанные, милые, приятные видимые формы, звуки, запахи, вкусы и осязаемое"
APPIYA = ("соединение с неприятным, которое является страданием", "соединением с неприятным, которое является страданием")
PIYA = ("разлука с приятным, которая является страданием", "разлукой с приятным, которая является страданием")
YAMPI = ("неполучение желаемого, которое тоже является страданием", "неполучением желаемого, которое тоже является страданием")
UPK = "служащих объектом цепляния"                                          # upādāna(kkhandha) [pi-1 upādāniya]
SANKHITTENA = (f"пять совокупностей, {UPK}, которые, короче говоря, являются страданием",
               f"пятью совокупностями, служащими объектом цепляния, которые, короче говоря, являются страданием")
NOT_BY_WISH = "Но этого не достичь желанием."                              # Na kho panetaṃ icchāya pattabbaṃ.
THIS_TOO = f"Это тоже «{YAMPI[0]}»."                                         # Idampi "yampicchaṃ na labhati tampi dukkhaṃ".


def wish(subj_gen, what_dat, what_nom, pl):
    verb = "не приходили" if pl else "не приходило"
    return (f"У существ, подверженных {subj_gen}, возникает такое желание {DASH} «О, если бы мы не были подвержены "
            f"{what_dat}; и пусть бы {what_nom} {verb} к нам»!")


# ================================================================ 4. Suttanta: craving
CRAVING_FORMULA = ("Та жажда, ведущая к новому существованию [вариант написания (Syā., Ka.): ponobbhavikā], "
                   "сопровождаемая наслаждением и страстью, находящая радость то здесь, то там, а именно " + DASH +
                   " чувственная жажда, жажда существования, жажда несуществования.")   # pi-5 ^5-679 words; kāmataṇhā pi-1 ^1-1065
assert "чувственная жажда, жажда существования, жажда несуществования" in PI1["^1-1065"]
PIYARUPA = "привлекательным и отрадным"
ARISE = ("возникая, возникает", "укореняясь, укореняется")            # uppajjamānā uppajjati / nivisamānā nivisati
CEASE = ("устраняясь, устраняется", "прекращаясь, прекращается")       # pahīyamānā pahīyati / nirujjhamānā nirujjhati


def where_q(v):
    return f"А где эта жажда, {v[0].split(', ')[0]}, {v[0].split(', ')[1]}, где, {v[1]}?"


def there(v, cap_=True):
    s = f"там эта жажда, {v[0]}, там, {v[1]}"
    return cap(s) + "." if cap_ else s


DOORS6 = ["cakkhu", "sota", "ghāna", "jivhā", "kāya", "mano"]
DOOR_GEN = dict(zip(DOORS6, S.SIX_DOORS))
OBJ6 = ["rūpa", "sadda", "gandha", "rasa", "phoṭṭhabba", "dhamma"]
OBJ_GEN = {"rūpa": "видимых форм", "sadda": "звуков", "gandha": "запахов", "rasa": "вкусов",
           "phoṭṭhabba": "осязаемого", "dhamma": "объектов ума"}
OBJ_PREP = {"rūpa": "видимых формах", "sadda": "звуках", "gandha": "запахах", "rasa": "вкусах",
            "phoṭṭhabba": "осязаемом", "dhamma": "объектах ума"}
LOKE = {}   # Pāli (lower case, without " loke") -> (Russian, gender m/n/f/pl)
for p, r, g in (("cakkhuṃ", "глаз", "m"), ("sotaṃ", "ухо", "n"), ("ghānaṃ", "нос", "m"), ("jivhā", "язык", "m"),
                ("kāyo", "тело", "n"), ("mano", "ум", "m"), ("rūpā", "видимые формы", "pl"), ("saddā", "звуки", "pl"),
                ("gandhā", "запахи", "pl"), ("rasā", "вкусы", "pl"), ("phoṭṭhabbā", "осязаемое", "n"),
                ("dhammā", "объекты ума", "pl")):
    LOKE[p] = (r, g)
for d, ru in zip(DOORS6, ["зрительное сознание", "слуховое сознание", "обонятельное сознание", "вкусовое сознание",
                          "осязательное сознание", "умственное сознание"]):
    LOKE[d + "viññāṇaṃ"] = (ru, "n")
for d in DOORS6:
    LOKE[d + "samphasso"] = (f"контакт {DOOR_GEN[d]}", "m")
    LOKE[d + "samphassajā vedanā"] = (f"рождённое контактом {DOOR_GEN[d]} чувство", "n")
for o in OBJ6:
    LOKE[o + "saññā"] = (f"восприятие {OBJ_GEN[o]}", "n")
    LOKE[o + "sañcetanā"] = (f"намерение в отношении {OBJ_GEN[o]}", "n")
    LOKE[o + "taṇhā"] = (f"жажда {OBJ_GEN[o]}", "f")
    LOKE[o + "vitakko"] = (f"направленная мысль {'об' if OBJ_PREP[o][0] in 'аоэиуы' else 'о'} {OBJ_PREP[o]}", "f")
    LOKE[o + "vicāro"] = (f"удержание мысли на {OBJ_PREP[o]}", "n")
assert "жажда видимых форм, жажда звуков, жажда запахов, жажда вкусов, жажда осязаемого, жажда объектов ума" in PI1["^1-1065"]
PRED_LOKE = {"m": f"является {PIYARUPA}", "n": f"является {PIYARUPA}", "f": "является привлекательной и отрадной",
             "pl": "являются привлекательными и отрадными"}


def loke_sentence(s):
    """'Cakkhuṃ loke piyarūpaṃ sātarūpaṃ.' / 'Sotaṃ loke…pe… ghānaṃ loke… mano loke piyarūpaṃ sātarūpaṃ.'"""
    end = " piyarūpaṃ sātarūpaṃ."
    assert s.endswith(end), s
    toks = re.split(r"…pe… |… ", s[:-len(end)])
    ru, g = [], None
    for t in toks:
        assert t.endswith(" loke"), t
        key = t[:-len(" loke")]
        r, g = LOKE[low(key)]
        ru.append(f"{r} в мире")
    return cap("… ".join(ru)) + f" {PRED_LOKE[g]}."


def craving_line(t, v):
    """the lines 'Sā kho panesā …', 'Kiñca loke …', the object lines (^2-203, ^2-204)."""
    first = "Sā kho panesā taṇhā kattha "
    if t.startswith(first):
        return f"{where_q(v)} Что в мире является {PIYARUPA}, {there(v, cap_=False)}."
    out = []
    for sent in re.split(r"(?<=[.?]) (?=[A-ZĀ])", t):
        if sent == "Kiñca loke piyarūpaṃ sātarūpaṃ?":
            out.append(f"А что в мире является {PIYARUPA}?")
        elif sent.startswith("Etthesā taṇhā "):
            assert sent in ("Etthesā taṇhā uppajjamānā uppajjati, ettha nivisamānā nivisati.",
                            "Etthesā taṇhā pahīyamānā pahīyati, ettha nirujjhamānā nirujjhati."), sent
            assert ("uppajjamānā" in sent) == (v is ARISE)
            out.append(there(v))
        else:
            out.append(loke_sentence(sent))
    return " ".join(out)


# ================================================================ 5. Suttanta: path
SP_PI1 = PI1["^1-1377"]
SP_EFFORT = "порождает желание, прилагает усилие, пробуждает усердие, напрягает ум, прилагает старания"
SP = ["ради невозникновения невозникших дурных неблагих явлений", "ради устранения возникших дурных неблагих явлений",
      "ради возникновения невозникших благих явлений",
      "ради сохранения, неутраты, умножения, обширности, развития и завершённости возникших благих явлений"]
for _x in SP:
    assert f"{_x} {SP_EFFORT}" in SP_PI1, _x
VAYAMA_S = (f"Вот монах {SP[0]} {SP_EFFORT}. " + " ".join(f"{cap(x)} {SP_EFFORT}." for x in SP[1:]))
SATI_TAIL = "ревностный, ясно понимающий, осознанный, устранив алчность и уныние в отношении мира"   # ātāpī sampajāno satimā, vineyya loke abhijjhādomanassaṃ
SATI_S = (f"Вот монах пребывает в теле, созерцая тело, {SATI_TAIL}. В чувствах… в уме… в явлениях пребывает, "
          f"созерцая явления, {SATI_TAIL}.")
# jhāna formula, pi-1 ^1-160 and the next three lines (without «со всеохватным объектом земли» and the variants)
JH1 = ("полностью уединившись от чувственных удовольствий, уединившись от неблагих явлений, входит в первое медитативное "
       "погружение, с направленной мыслью и удержанием мысли, с восторгом и счастьем, рождёнными уединением, и пребывает в нём")
JH2 = ("с затиханием направленной мысли и удержания мысли входит во второе медитативное погружение, с ясностью внутри себя, "
       "с единением ума, без направленной мысли и без удержания мысли, с восторгом и счастьем, рождёнными сосредоточением, "
       "и пребывает в нём")
JH3 = (f"с угасанием восторга пребывает невозмутимым, осознанным и ясно понимающим, испытывает телом счастье, так что "
       f"благородные говорят о нём {DASH} «Невозмутимый, осознанный, пребывающий в счастье», и входит в третье медитативное "
       f"погружение и пребывает в нём")
JH4 = ("с устранением приятного и с устранением болезненного, с исчезновением ещё прежде радости и уныния входит в "
       "четвёртое медитативное погружение, которое ни болезненно, ни приятно, с чистотой невозмутимости и осознанности, "
       "и пребывает в нём")
in_pi1("полностью уединившись от чувственных удовольствий, уединившись от неблагих явлений, входит в первое медитативное погружение",
       "с направленной мыслью и удержанием мысли, с восторгом и счастьем, рождёнными уединением, со всеохватным объектом земли, и пребывает в нём",
       "с затиханием направленной мысли и удержания мысли входит во второе медитативное погружение",
       "с ясностью внутри себя, с единением ума, без направленной мысли и без удержания мысли, с восторгом и счастьем, рождёнными сосредоточением, со всеохватным объектом земли, и пребывает в нём",
       "с угасанием восторга пребывает невозмутимым, осознанным и ясно понимающим, испытывает телом счастье, так что благородные говорят о нём – «Невозмутимый, осознанный, пребывающий в счастье», и входит в третье медитативное погружение",
       "с устранением приятного и с устранением болезненного, с исчезновением ещё прежде радости и уныния входит в четвёртое медитативное погружение",
       "которое ни болезненно, ни приятно, с чистотой невозмутимости и осознанности, со всеохватным объектом земли, и пребывает в нём")
SAMADHI_S = f"Вот монах, {JH1}. {cap(JH2)}. {cap(JH3)}. {cap(JH4)}."

# lokuttara path opening, pi-1 ^1-277
_L = PI1["^1-277"]
LOKUTTARA = _L[_L.index("В то время, когда кто-либо"):_L.index("в это время есть контакт")]
LOKUTTARA = edit(LOKUTTARA, "В то время, когда кто-либо", "Вот в то время, когда монах")
assert LOKUTTARA.endswith("и пребывает в нём, ")
LOKUTTARA_P = ("Idha bhikkhu yasmiṃ samaye lokuttaraṃ jhānaṃ bhāveti niyyānikaṃ apacayagāmiṃ diṭṭhigatānaṃ pahānāya "
               "paṭhamāya bhūmiyā pattiyā vivicceva kāmehi…pe… paṭhamaṃ jhānaṃ upasampajja viharati dukkhapaṭipadaṃ "
               "dandhābhiññaṃ, tasmiṃ samaye ")
TAIL_SENT = {
    "aṭṭhaṅgiko maggo hoti sammādiṭṭhi…pe… sammāsamādhi.":   # no dash in the Pāli: a colon (reported)
        f"в это время есть {EIGHTFOLD}: правильное воззрение… правильное сосредоточение.",
    "aṭṭhaṅgiko maggo hoti – sammādiṭṭhi…pe… sammāsamādhi.":
        f"в это время есть {EIGHTFOLD} {DASH} правильное воззрение… правильное сосредоточение.",
    "pañcaṅgiko maggo hoti – sammādiṭṭhi, sammāsaṅkappo, sammāvāyāmo, sammāsati, sammāsamādhi.":
        f"в это время есть {FIVEFOLD} {DASH} {FIVE_FACTORS}.",
    "phasso hoti…pe… avikkhepo hoti.": "в это время есть контакт… есть отсутствие отвлечения.",   # [pi-1 2-01 l. 318]
    'Ayaṃ vuccati "dukkhanirodhagāminī paṭipadā".': cap(called(PATIPADA[1])) + ".",
    'Ayaṃ vuccati – "dukkhanirodhagāminī paṭipadā".': f"Это называется {DASH} «{PATIPADA[1]}».",
    "Avasesā dhammā dukkhanirodhagāminiyā paṭipadāya sampayuttā.":
        "Остальные явления связаны со способом практики, ведущим к прекращению страдания.",
}
in_pi1("в это время есть контакт… есть отсутствие отвлечения…")

# ================================================================ 6. Abhidhamma lists (dukkha / samudaya / nirodha)
NOM_ITEM = {   # (Russian, ends with a participial phrase)
    "Taṇhā": ("жажда", False),
    "avasesā kilesā": ("остальные омрачения", False),
    "avasesā akusalā dhammā": ("остальные неблагие явления", False),
    "tīṇi kusalamūlāni sāsavāni": ("три благих корня, подверженные влечениям", True),
    "avasesā sāsavā kusalā dhammā": ("остальные подверженные влечениям благие явления", False),
    "sāsavā kusalākusalānaṃ dhammānaṃ vipākā": ("подверженные влечениям результаты благих и неблагих явлений", False),
    "ye dhammā kiriyā neva kusalā nākusalā na ca kammavipākā":
        ("те функциональные явления, ни благие, ни неблагие и не являющиеся результатом действий", True),   # [pi-1 ^1-583]
    "sabbaṃ rūpaṃ": ("вся материальная форма", False),
}
in_pi1("и те функциональные явления, ни благие, ни неблагие и не являющиеся результатом действий, и вся материальная форма",
       "Три благих корня")
GEN_ITEM = {
    "Taṇhāya": ("жажды", False),
    "avasesānaṃ kilesānaṃ": ("остальных омрачений", False),
    "avasesānaṃ akusalānaṃ dhammānaṃ": ("остальных неблагих явлений", False),
    "tiṇṇaṃ kusalamūlānaṃ sāsavānaṃ": ("трёх благих корней, подверженных влечениям", True),
    "avasesānaṃ sāsavānaṃ kusalānaṃ dhammānaṃ": ("остальных подверженных влечениям благих явлений", False),
}
PAHANA = "Устранение"     # pahānaṃ


def nom_list(body):
    """'Avasesā ca kilesā, … sabbañca rūpaṃ' -> («И остальные омрачения, …, и вся материальная форма», closing comma)."""
    if body == "Taṇhā ca avasesā ca kilesā":
        return "Жажда и остальные омрачения", False
    if body == "Taṇhā":
        return "Жажда", False
    out, pp = [], False
    for piece in body.split(", "):
        has_ca = False
        if piece == "Taṇhā ca avasesā ca kilesā":
            out.append("жажда и остальные омрачения")
            continue
        if " ca " in piece:
            piece = piece.replace(" ca ", " ", 1)
            has_ca = True
        elif piece.endswith(" ca"):
            piece = piece[:-3]
            has_ca = True
        elif piece.startswith("sabbañca "):
            piece = "sabbaṃ " + piece[len("sabbañca "):]
            has_ca = True
        key = low(piece) if low(piece) in NOM_ITEM else piece
        ru, pp = NOM_ITEM[key]
        out.append(("и " if has_ca else "") + ru)
    return cap(", ".join(out)), pp


def gen_list(body):
    """'Taṇhāya ca, avasesānañca kilesānaṃ, … pahānaṃ' -> «Устранение и жажды, и остальных омрачений, …»."""
    assert body.endswith(" pahānaṃ"), body
    body = body[:-len(" pahānaṃ")]
    if body == "Taṇhāya":
        return f"{PAHANA} жажды", False
    out, pp = [], False
    for piece in body.split(", "):
        has_ca = False
        if piece.endswith(" ca"):
            piece, has_ca = piece[:-3], True
        else:
            m = re.match(r"^(\S+?)ñca (.+)$", piece)
            if m:
                piece, has_ca = m.group(1) + "ṃ " + m.group(2), True
        ru, pp = GEN_ITEM[piece]
        out.append(("и " if has_ca else "") + ru)
    return f"{PAHANA} " + ", ".join(out), pp


# ================================================================ 7. chapter 4
SEC = S.SECTION_TITLES
TERM = {  # Abhidhamma question terms: Pāli -> (nom, ins)
    "dukkhasamudayo": SAMUDAYA, "dukkhaṃ": DUKKHA, "dukkhanirodho": NIRODHA, "dukkhanirodhagāminī paṭipadā": PATIPADA,
}
TERM.update(MAGGA)
VUCC = re.compile(r'^(.*?)(,?) ' + DASH + r' (?:ayaṃ|idaṃ) vuccati "([^"]+)"\.(?: (.*))?$')


def tail_sents(rest):
    out = []
    for sent in re.split(r"(?<=\.) (?=[A-ZĀ])", rest):
        out.append(TAIL_SENT[sent])
    return " ".join(out)


def abhi4_line(t):
    if t.startswith("Cattāri saccāni " + DASH):
        assert t == "Cattāri saccāni – dukkhaṃ, dukkhasamudayo, dukkhanirodho, dukkhanirodhagāminī paṭipadā."
        return f"{FOUR} {DASH} " + enum([DUKKHA[0], SAMUDAYA[0], NIRODHA[0], PATIPADA[0]]) + "."
    if t == "Abhidhammabhājanīyaṃ.":
        return SEC["Abhidhammabhājanīyaṃ"] + "."
    m = re.match(r"^Tattha katam\S+ (.+?)\? (.*)$", t)
    term, rest = m.group(1), m.group(2)
    head = q(TERM[term][0])
    if rest.startswith("Idha bhikkhu yasmiṃ samaye"):
        r2 = rest.replace("pattiyā, vivicceva", "pattiyā vivicceva")
        assert r2.startswith(LOKUTTARA_P), rest[:200]
        return f"{head} {LOKUTTARA}{tail_sents(r2[len(LOKUTTARA_P):])}"
    m = VUCC.match(rest)
    body, ans, more = m.group(1), m.group(3), m.group(4)
    assert ans == term, (ans, term)
    if body in FACTOR_BODY:
        ru, comma = FACTOR_BODY[body], True
    elif term == "dukkhanirodho":
        ru, comma = gen_list(body)
    else:
        ru, comma = nom_list(body)
    line = f"{head} {ru}{',' if comma else ''} {DASH} {called(TERM[term][1])}."
    if more:
        line += " " + tail_sents(more)
    return line


def sutta4(t):
    """Suttantabhājanīya lines of ch. 4 (fixed strings, one Pāli line each)."""
    W = lambda name, body, ins: f"{q(name)} {body}, {DASH} {called(ins)}."
    if t.startswith("Cattāri ariyasaccāni " + DASH):
        assert t == ("Cattāri ariyasaccāni – dukkhaṃ ariyasaccaṃ, dukkhasamudayaṃ [dukkhasamudayo (syā.)] ariyasaccaṃ, "
                     "dukkhanirodhaṃ [dukkhanirodho (syā.)] ariyasaccaṃ, dukkhanirodhagāminī paṭipadā ariyasaccaṃ."), t
        return (f"{FOUR_ARIYA} {DASH} " + enum([
            ARIYA["dukkhaṃ ariyasaccaṃ"][0],
            ARIYA["dukkhasamudayaṃ ariyasaccaṃ"][0] + " [вариант написания (Syā.): dukkhasamudayo]",
            ARIYA["dukkhanirodhaṃ ariyasaccaṃ"][0] + " [вариант написания (Syā.): dukkhanirodho]",
            ARIYA["dukkhanirodhagāminī paṭipadā ariyasaccaṃ"][0]]) + ".")
    if t.startswith("##### "):
        return "##### " + SACCA[t[6:]][0]
    if t == "Suttantabhājanīyaṃ.":
        return SEC["Suttantabhājanīyaṃ"] + "."
    m = re.match(r'^Idaṃ vuccati "(.+)"\.$', t)
    if m:
        return cap(called(ARIYA[m.group(1)][1])) + "."
    m = re.match(r"^Tattha katam\S+ (.+?)\? ", t)
    key = m.group(1) if m else None
    if key == "dukkhaṃ ariyasaccaṃ":
        assert t.endswith("saṃkhittena pañcupādānakkhandhā dukkhā.")
        return (f"{q(ARIYA[key][0])} И рождение является страданием, и старение является страданием, и смерть является "
                f"страданием, и {GRIEF5} являются страданием, {APPIYA[0].replace(', которое ', ' ')}, "
                f"{PIYA[0].replace(', которая ', ' ')}, и неполучение желаемого тоже является страданием, короче говоря, "
                f"пять совокупностей, {UPK}, являются страданием.")
    if key == "jāti":
        return W("рождение", JATI_L, "рождением")
    if key == "jarā":
        return W("старение", JARA_L, "старением")
    if key == "maraṇaṃ":
        return W("смерть", MARANA_L, "смертью")
    if key == "soko":
        return W("печаль", SOKA_L, "печалью")
    if key == "paridevo":
        return W("стенания", PARIDEVA_L, "стенаниями")
    if key == "dukkhaṃ":
        assert T.FEEL["dukkha"] and PALI3["dukkha"] in t
        return W("боль", "То, что есть " + T.FEEL["dukkha"], "болью")
    if key == "domanassaṃ":
        assert PALI3["domanassa"] in t
        return W("уныние", "То, что есть " + T.FEEL["domanassa"], "унынием")
    if key == "upāyāso":
        return W("отчаяние", UPAYASA_L, "отчаянием")
    if key == "appiyehi sampayogo dukkho":
        return (f"{q(APPIYA[0])} Вот у кого-то бывают {FIVE_OBJ_ADJ}, или же бывают те, кто желает ему вреда, желает ему "
                f"неблага, желает ему неудобства, желает ему лишиться безопасности; то, что есть встреча с ними, общение, "
                f"соединение, смешение, {DASH} {called(APPIYA[1])}.")
    if key == "piyehi vippayogo dukkho":
        return (f"{q(PIYA[0])} Вот у кого-то бывают {FIVE_OBJ_ADJ_P}, или же бывают те, кто желает ему пользы, желает ему "
                f"блага, желает ему удобства, желает ему безопасности: мать, или отец, или брат, или сестра, или друзья, "
                f"или сотоварищи, или родственники, или кровные родные; то, что есть отсутствие встречи с ними, отсутствие "
                f"общения, несоединение, несмешение, {DASH} {called(PIYA[1])}.")
    if key == "yampicchaṃ na labhati tampi dukkhaṃ":
        return (f"{q(YAMPI[0])} {wish('рождению', 'рождению', 'рождение', False)} {NOT_BY_WISH} {THIS_TOO}")
    if t.startswith("Jarādhammānaṃ sattānaṃ…pe…"):
        return ("У существ, подверженных старению… у существ, подверженных болезни… у существ, подверженных смерти… "
                + low(wish(GRIEF5_DAT, GRIEF5_DAT, GRIEF5, True)) + f" {NOT_BY_WISH} {THIS_TOO}")
    if key == "saṃkhittena pañcupādānakkhandhā dukkhā":
        five = ", ".join(f"{S.AGG[a]['khandha']}, служащая объектом цепляния"
                         for a in ("rupa", "vedana", "sanna", "sankhara", "vinnana"))
        return f"{q(SANKHITTENA[0])} А именно {DASH} {five}. {cap(called(SANKHITTENA[1]))}."
    if key == "dukkhasamudayaṃ ariyasaccaṃ":
        return f"{q(ARIYA[key][0])} {CRAVING_FORMULA}"
    if key == "dukkhanirodhaṃ ariyasaccaṃ":
        assert t.endswith("Yo tassāyeva taṇhāya asesavirāganirodho cāgo paṭinissaggo mutti anālayo.")
        return (f"{q(ARIYA[key][0])} То, что есть угасание без остатка и прекращение этой самой жажды, отказ от неё, "
                f"оставление её, освобождение от неё, отсутствие привязанности к ней.")
    if key == "dukkhanirodhagāminī paṭipadā ariyasaccaṃ":
        return (f"{q(ARIYA[key][0])} Это именно благородный {EIGHTFOLD}, а именно {DASH} {EIGHT_FACTORS}.")
    if key == "sammādiṭṭhi":
        return (f"{q(MAGGA[key][0])} Знание страдания, знание возникновения страдания, знание прекращения страдания, "
                f"знание способа практики, ведущего к прекращению страдания, {DASH} {called(MAGGA[key][1])}.")
    if key == "sammāsaṅkappo":
        return (f"{q(MAGGA[key][0])} Помысел об отречении, помысел об отсутствии недоброжелательности, помысел об отсутствии "
                f"жестокости {DASH} {called(MAGGA[key][1])}.")
    if key == "sammāvācā":
        return (f"{q(MAGGA[key][0])} Уклонение от лжи, уклонение от речи, сеющей раздор, уклонение от грубой речи, "
                f"уклонение от пустой болтовни {DASH} {called(MAGGA[key][1])}.")
    if key == "sammākammanto":
        return (f"{q(MAGGA[key][0])} Уклонение от убийства живых существ, уклонение от взятия того, что не дано, уклонение "
                f"от неправильного поведения в чувственных удовольствиях {DASH} {called(MAGGA[key][1])}.")
    if key == "sammāājīvo":
        return (f"{q(MAGGA[key][0])} Вот благородный ученик, устранив неправильный образ жизни, поддерживает жизнь правильным "
                f"образом жизни {DASH} {called(MAGGA[key][1])}.")
    if key == "sammāvāyāmo":
        return f"{q(MAGGA[key][0])} {VAYAMA_S} {cap(called(MAGGA[key][1]))}."
    if key == "sammāsati":
        return f"{q(MAGGA[key][0])} {SATI_S} {cap(called(MAGGA[key][1]))}."
    if key == "sammāsamādhi":
        return f"{q(MAGGA[key][0])} {SAMADHI_S} {cap(called(MAGGA[key][1]))}."
    raise KeyError("sutta4: " + t[:90])


def pali3_bodies():
    out = {}
    for l in open(os.path.join(S.PALI_DIR, "3-dhatuvibhango.md"), encoding="utf-8").read().split("\n"):
        m = re.match(r"^Tattha katamā (sukha|dukkha|somanassa|domanassa|upekkhā)dhātu\? (.+) – ayaṃ vuccati", l)
        if m:
            out[m.group(1)] = m.group(2)
    assert len(out) == 5
    return out


PALI3 = pali3_bodies()


def build_ch4(pali):
    out = []
    section = None
    craving = None
    for t in pali:
        if t == "### Saccavibhaṅgo":
            out.append("### " + S.CHAPTER_TITLES[4])
            continue
        if t.startswith("#### "):
            section = t[5:]
            out.append("#### " + SEC[section])
            continue
        if section == "Suttantabhājanīyaṃ":
            if t.startswith("##### Samudaya"):
                craving = ARISE
            elif t.startswith("##### Nirodha"):
                craving = CEASE
            elif t.startswith("##### "):
                craving = None
            if craving and (t.startswith("Sā kho panesā") or t.startswith("Kiñca loke") or " loke" in t.split(".")[0]):
                out.append(craving_line(t, craving))
            else:
                out.append(sutta4(t))
        elif section == "Abhidhammabhājanīyaṃ":
            out.append(abhi4_line(t))
        else:
            out.append(q_line(t, ch=4))
    return out


# ================================================================ 8. chapter 5
IND = {   # Pāli -> (nom, ins)  [pi-1]
    "cakkhundriyaṃ": ("способность глаза", "способностью глаза"), "sotindriyaṃ": ("способность уха", "способностью уха"),
    "ghānindriyaṃ": ("способность носа", "способностью носа"), "jivhindriyaṃ": ("способность языка", "способностью языка"),
    "kāyindriyaṃ": ("способность тела", "способностью тела"), "manindriyaṃ": ("способность ума", "способностью ума"),
    "itthindriyaṃ": ("способность женственности", "способностью женственности"),
    "purisindriyaṃ": ("способность мужественности", "способностью мужественности"),
    "jīvitindriyaṃ": ("жизненная способность", "жизненной способностью"),
    "sukhindriyaṃ": ("способность удовольствия", "способностью удовольствия"),
    "dukkhindriyaṃ": ("способность боли", "способностью боли"),
    "somanassindriyaṃ": ("способность радости", "способностью радости"),
    "domanassindriyaṃ": ("способность уныния", "способностью уныния"),
    "upekkhindriyaṃ": ("способность невозмутимости", "способностью невозмутимости"),
    "saddhindriyaṃ": ("способность веры", "способностью веры"),
    "vīriyindriyaṃ": ("способность усердия", "способностью усердия"),
    "satindriyaṃ": ("способность осознанности", "способностью осознанности"),
    "samādhindriyaṃ": ("способность сосредоточения", "способностью сосредоточения"),
    "paññindriyaṃ": ("способность мудрости", "способностью мудрости"),
    "anaññātaññassāmītindriyaṃ": ("способность познания непознанного", "способностью познания непознанного"),
    "aññindriyaṃ": ("способность окончательного знания", "способностью окончательного знания"),
    "aññātāvindriyaṃ": ("способность обладателя окончательного знания", "способностью обладателя окончательного знания"),
    "rūpajīvitindriyaṃ": ("материальная жизненная способность", "материальной жизненной способностью"),
    "arūpajīvitindriyaṃ": ("нематериальная жизненная способность", "нематериальной жизненной способностью"),
}
in_pi1(*[v[0] for k, v in IND.items() if "jīvitindriyaṃ" not in k or k == "jīvitindriyaṃ"])
IND22 = ["cakkhundriyaṃ", "sotindriyaṃ", "ghānindriyaṃ", "jivhindriyaṃ", "kāyindriyaṃ", "manindriyaṃ", "itthindriyaṃ",
         "purisindriyaṃ", "jīvitindriyaṃ", "sukhindriyaṃ", "dukkhindriyaṃ", "somanassindriyaṃ", "domanassindriyaṃ",
         "upekkhindriyaṃ", "saddhindriyaṃ", "vīriyindriyaṃ", "satindriyaṃ", "samādhindriyaṃ", "paññindriyaṃ",
         "anaññātaññassāmītindriyaṃ", "aññindriyaṃ", "aññātāvindriyaṃ"]
TWENTY_TWO = "Двадцать две способности"
VAR_VIRIYINDRIYA = " [вариант написания (Sī., Syā.): viriyindriyaṃ]"


def twenty_two(var=False):
    items = [IND[k][0] + (VAR_VIRIYINDRIYA if var and k == "vīriyindriyaṃ" else "") for k in IND22]
    return f"{TWENTY_TWO} {DASH} " + enum(items) + "."


def organ_body(body):
    return f"{T.head(body)}… {T.tail_last(body)}"


EYE_B = organ_body(T.EYE.replace(" [вариант написания (Sī., Syā., Ka.): cakkhuṃ; dha. sa. 596-599]", ""))
BODY_B = organ_body(T.BODY)
IN = lambda k: IND[k]


def ind_q(k):
    return q(IND[k][0])


# manindriya classification (as ch. 2 manāyatana; «способность» is feminine like «сфера»)
MI = "способности ума"


def mi_open(n):
    return f"Классификация {MI} {B.HOW_MANY[n]}"


def mi_close(n):
    return f"Такова классификация {MI} {B.HOW_MANY[n]}"


def mi_line(t):
    pre = ""
    if t.startswith("Tattha katamaṃ manindriyaṃ? "):
        pre = ind_q("manindriyaṃ") + " "
        t = t[len("Tattha katamaṃ manindriyaṃ? "):]
    out = []
    for sent in re.split(r"(?<=\.) (?=[A-Z])", t):
        if sent == 'Idaṃ vuccati "manindriyaṃ".':
            out.append(cap(called(IND["manindriyaṃ"][1])) + ".")
            continue
        m = re.match(r"^Evaṃ (\w+?)[vb]idhena manindriyaṃ(?:…pe… evaṃ (\w+?)[vb]idhena manindriyaṃ)?\.$", sent)
        if m:
            s = mi_close(B.NUM[m.group(1).lower()])
            if m.group(2):
                s += "… " + low(mi_close(B.NUM[m.group(2).lower()]))
            out.append(s + ".")
            continue
        m = re.match(r"^(\w+?)[vb]idhena manindriyaṃ – (.+)\.$", sent)
        body = m.group(2).replace("…pe…", PE)
        st = {"mode": "f"}
        parts = re.split(r"(, |\x01 ?)", body)
        ru = []
        for i, x in enumerate(parts):
            if i % 2:
                ru.append(x.replace(PE, "…"))
            elif x:
                ru.append(T.man_chunk(x, st))
        out.append(f"{mi_open(B.NUM[m.group(1).lower()])} {DASH} " + "".join(ru) + ".")
    return pre + " ".join(out)


def pi1_q_body(bid, end):
    """pi-1 'Что такое X в это время? То, что в это время есть …, – это X' -> body without «в это время»."""
    b = T.pi1_body(bid, end)
    return b.replace("То, что в это время есть ", "То, что есть ", 1)


ITTHI_B = T.pi1_body("^1-714", ", – это материальная форма")
PURISA_B = T.pi1_body("^1-716", ", – это материальная форма")
JIVITA_R = T.pi1_body("^1-718", ", – это материальная форма")
JIVITA_A = edit(T.pi1_body("^1-19", ", – это жизненная способность"), " [вариант написания (Sī.): irīyanā]", "")
SADDHA_B = pi1_q_body("^1-12", ", – это способность веры")
VIRIYA_B = pi1_q_body("^1-13", ", – это способность усердия")
VIRIYA_B = edit(VIRIYA_B, VAR_VIRIYARAMBHO, "")
VIRIYA_B = edit(VIRIYA_B, " [вариант написания (Sī.): ussoḷhi]", "")
VIRIYA_B = edit(VIRIYA_B, "стойкость, твёрдость,", "стойкость, устойчивость,")   # pi-2 "thāmo ṭhiti" (pi-1 dhiti), as written
SATI_B = pi1_q_body("^1-14", ", – это способность осознанности")
SAMADHI_B = pi1_q_body("^1-15", ", – это способность сосредоточения")
PANNA_B = pe(pi1_q_body("^1-16", ", – это способность мудрости"), 2, "отсутствие заблуждения")
LOKUTTARA_PANNA = pe(DITTHI_L, 2, "отсутствие заблуждения")[len("То, что есть "):]
ANANNATA = T.pi1_body("^1-296", ", – это способность познания непознанного")
ANANNATA_HEAD = ANANNATA[:ANANNATA.index("есть мудрость")]
assert ANANNATA_HEAD == ("То, что для непосредственного постижения тех явлений, которые не познаны, не увидены, не достигнуты, "
                         "не узнаны и не постигнуты непосредственно, ")
ANNA_HEAD = ("То, что для непосредственного постижения тех явлений, которые познаны, увидены, достигнуты, узнаны и "
             "постигнуты непосредственно, ")
in_pi1(ANNA_HEAD + "есть мудрость")
ANNATAVI_HEAD = ("То, что для непосредственного постижения тех явлений, которые обладают окончательным знанием, увидены, "
                 "достигнуты, узнаны и постигнуты непосредственно, ")   # aññātāvīnaṃ: pi-1 «обладающих окончательным знанием»
in_pi1("обладающих окончательным знанием")


def abhi5_line(t):
    W = lambda k, body, quoted=True: f"{ind_q(k)} {body}, {DASH} {called(IND[k][1], quoted)}."
    if t.startswith("Bāvīsatindriyāni " + DASH):
        return twenty_two(var="[viriyindriyaṃ" in t)
    if t == "Abhidhammabhājanīyaṃ.":
        return SEC["Abhidhammabhājanīyaṃ"] + "."
    if t.startswith("Tattha katamaṃ manindriyaṃ?") or re.match(r"^\w+?[vb]idhena manindriyaṃ", t):
        return mi_line(t)
    m = re.match(r"^Tattha katamaṃ (\S+?)\? ", t)
    if t.startswith("Tattha katamaṃ sotindriyaṃ…pe…"):
        assert t.endswith('Yo kāyo catunnaṃ mahābhūtānaṃ upādāya pasādo…pe… suñño gāmopeso – idaṃ vuccati "kāyindriyaṃ".')
        names = "… ".join(IND[k][0] for k in ("sotindriyaṃ", "ghānindriyaṃ", "jivhindriyaṃ", "kāyindriyaṃ"))
        return f"{q(names)} {BODY_B}, {DASH} {called(IND['kāyindriyaṃ'][1])}."
    k = m.group(1)
    if k == "cakkhundriyaṃ":
        return W(k, EYE_B)
    if k == "itthindriyaṃ":
        return W(k, ITTHI_B)
    if k == "purisindriyaṃ":
        return W(k, PURISA_B)
    if k == "jīvitindriyaṃ":
        assert t.endswith("Jīvitindriyaṃ duvidhena – atthi rūpajīvitindriyaṃ, atthi arūpajīvitindriyaṃ.")
        return (f"{ind_q(k)} Классификация жизненной способности {B.HOW_MANY[2]} {DASH} есть "
                f"{IND['rūpajīvitindriyaṃ'][0]}, есть {IND['arūpajīvitindriyaṃ'][0]}.")
    if k == "rūpajīvitindriyaṃ":
        return W(k, JIVITA_R)
    if k == "arūpajīvitindriyaṃ":   # Pāli "arūpajīvatindriyaṃ" in the answer: spelling slip, rendered as meant (reported)
        assert t.endswith('– idaṃ vuccati "arūpajīvatindriyaṃ". Idaṃ vuccati "jīvitindriyaṃ".')
        return W(k, JIVITA_A)[:-1] + ". " + cap(called(IND["jīvitindriyaṃ"][1])) + "."
    for name, fk in (("sukhindriyaṃ", "sukha"), ("dukkhindriyaṃ", "dukkha"), ("somanassindriyaṃ", "somanassa"),
                     ("domanassindriyaṃ", "domanassa"), ("upekkhindriyaṃ", "upekkhā")):
        if k == name:
            assert PALI3[fk] in t
            return W(k, "То, что есть " + T.FEEL[fk])
    if k == "saddhindriyaṃ":
        return W(k, SADDHA_B)
    if k == "vīriyindriyaṃ":
        assert "thāmo ṭhiti asithilaparakkamatā" in t
        return W(k, VIRIYA_B)
    if k == "satindriyaṃ":
        return W(k, SATI_B)
    if k == "samādhindriyaṃ":
        return W(k, SAMADHI_B)
    if k == "paññindriyaṃ":
        return W(k, PANNA_B)
    if k == "anaññātaññassāmītindriyaṃ":
        return W(k, ANANNATA_HEAD + "есть " + LOKUTTARA_PANNA)
    if k == "aññindriyaṃ":   # answer without quotes in the Pāli: as written
        assert t.endswith("– idaṃ vuccati aññindriyaṃ.")
        return W(k, ANNA_HEAD + "есть " + LOKUTTARA_PANNA, quoted=False)
    if k == "aññātāvindriyaṃ":
        return W(k, ANNATAVI_HEAD + "есть " + LOKUTTARA_PANNA)
    raise KeyError("abhi5: " + t[:80])


def build_ch5(pali):
    out = []
    section = None
    for t in pali:
        if t == "### Indriyavibhaṅgo":
            out.append("### " + S.CHAPTER_TITLES[5])
        elif t.startswith("#### "):
            section = t[5:]
            out.append("#### " + SEC[section])
        elif section == "Abhidhammabhājanīyaṃ":
            out.append(abhi5_line(t))
        else:
            out.append(q_line(t, ch=5))
    return out


# ================================================================ 9. Pañhāpucchaka (both chapters)
def _subj(nom, acc, num, g):
    return (nom, acc, num, g)


NEW_SUBJ = {}
for p, (nom, acc) in SACCA.items():
    NEW_SUBJ[p] = (nom, acc, "sg", "f")
NEW_SUBJ["Dve saccā"] = ("Две истины", "Две истины", "pl", None)
NEW_SUBJ["Tīṇi saccāni"] = ("Три истины", "Три истины", "pl", None)
for p, n in (("Dvindriyā", "Две"), ("Tīṇindriyā", "Три"), ("Cattārindriyā", "Четыре")):
    NEW_SUBJ[p] = (f"{n} способности", f"{n} способности", "pl", None)
for p, n in (("Pañcindriyā", "Пять"), ("Cha indriyā", "Шесть"), ("Sattindriyā", "Семь"), ("Aṭṭhindriyā", "Восемь"),
             ("Navindriyā", "Девять"), ("Dasindriyā", "Десять"), ("Ekādasindriyā", "Одиннадцать"),
             ("Dvādasindriyā", "Двенадцать"), ("Terasindriyā", "Тринадцать"), ("Cuddasindriyā", "Четырнадцать"),
             ("Pannarasindriyā", "Пятнадцать"), ("Soḷasindriyā", "Шестнадцать"), ("Sattarasindriyā", "Семнадцать"),
             ("Aṭṭhārasindriyā", "Восемнадцать")):
    NEW_SUBJ[p] = (f"{n} способностей", f"{n} способностей", "pl", None)
NEW_SUBJ["Ekavīsatindriyā"] = ("Двадцать одна способность", "Двадцать одну способность", "sg", "f")
for k in ("domanassindriyaṃ", "anaññātaññassāmītindriyaṃ", "jīvitindriyaṃ", "aññindriyaṃ", "upekkhindriyaṃ",
          "somanassindriyaṃ", "aññātāvindriyaṃ", "manindriyaṃ"):
    nom = cap(IND[k][0])
    acc = nom.replace("Жизненная", "Жизненную")
    NEW_SUBJ[cap(k)] = (nom, acc, "sg", "f")
NEW_SUBJ["aṭṭhindriyā"] = (low(NEW_SUBJ["Aṭṭhindriyā"][0]), low(NEW_SUBJ["Aṭṭhindriyā"][1]), "pl", None)   # mid-sentence
for k, v in NEW_SUBJ.items():
    assert k not in T.SUBJ2 or T.SUBJ2[k] == v, k
    T.SUBJ2[k] = v
T.SUBJ_RE2 = re.compile(r"^(" + "|".join(map(re.escape, sorted(T.SUBJ2, key=len, reverse=True))) + r") (.+)$")

# new matrix surfaces / items (pi-2 spellings; feminine predicates as B.ITEMS)
T.alias("acaya", "ācayagāmi")
T.alias("apacaya", "apacayagāmi")
T.alias("nevacaya", "nevācayagāmināpacayagāmi")
T.alias("maggadhipati", "maggādhipatī")
T.alias("arupi", "arūpāni")
T.new("na_maggarammana", ["na maggārammaṇo", "na maggārammaṇā"], None, "не имеет объектом путь", "не имеют объектом путь")
T.new("na_maggahetuka", ["na maggahetuko", "na maggahetukā"], None, "не имеет корнем путь", "не имеют корнем путь")
T.new("na_appamanarammana", ["na appamāṇārammaṇo", "na appamāṇārammaṇā"], None, "не имеет безмерного объекта",
      "не имеют безмерного объекта")

FIXES = [  # punctuation slips in the Pāli (reported); the words are translated as written
    ('"nti pi', '"ntipi'),                     # "mahaggatārammaṇa"nti pi (ch. 5)
    ('" tipi', '"tipi'),                       # "…sampayuttañcā" tipi (ch. 4 ×2)
    ('"gantho ceva ganthasampayutta"ñcāti', '"gantho ceva ganthasampayuttañcā"ti'),   # ch. 5
    ("siyā araṇanti.", "siyā araṇaṃ."),        # closing "ti" of the question (ch. 4)
    ("Dve saccā nīvaraṇiyā dve saccā anīvaraṇiyā.", "Dve saccā nīvaraṇiyā. Dve saccā anīvaraṇiyā."),   # full stop missing
    ("siyā parittārammaṇaṃ siyā mahaggatārammaṇaṃ,", "siyā parittārammaṇaṃ, siyā mahaggatārammaṇaṃ,"),   # comma missing (ch. 5)
    # "X na Y": two predicates, the second without siyā; Russian joins them with a comma (as pi-1 piti_only)
    ("siyā mahaggatārammaṇaṃ na appamāṇārammaṇaṃ", "siyā mahaggatārammaṇaṃ, na appamāṇārammaṇaṃ"),
    ("Maggasaccaṃ na maggārammaṇaṃ maggahetukaṃ,", "Maggasaccaṃ na maggārammaṇaṃ, maggahetukaṃ,"),
    ("siyā maggārammaṇaṃ na maggahetukaṃ,", "siyā maggārammaṇaṃ, na maggahetukaṃ,"),
]
LABELS = {
    "##### Tikaṃ": B.LABELS["##### Tikaṃ"], "##### Dukaṃ": B.LABELS["##### Dukaṃ"],
    "Pañhāpucchakaṃ.": SEC["Pañhāpucchakaṃ"] + ".",
    "Saccavibhaṅgo niṭṭhito.": S.CHAPTER_CLOSING.format(title=S.CHAPTER_TITLES[4]),
    "Indriyavibhaṅgo niṭṭhito.": S.CHAPTER_CLOSING.format(title=S.CHAPTER_TITLES[5]),
    "Catunnaṃ ariyasaccānaṃ kati kusalā, kati akusalā, kati abyākatā…pe… kati saraṇā, kati araṇā?":
        T.how_many_q("четырёх благородных истин"),
    "Bāvīsatīnaṃ indriyānaṃ kati kusalā, kati akusalā, kati abyākatā…pe… kati saraṇā, kati araṇā?":
        T.how_many_q("двадцати двух способностей"),
    "Cattāri ariyasaccāni – dukkhaṃ ariyasaccaṃ, dukkhasamudayaṃ ariyasaccaṃ, dukkhanirodhaṃ ariyasaccaṃ, "
    "dukkhanirodhagāminī paṭipadā ariyasaccaṃ.":
        f"{FOUR_ARIYA} {DASH} " + enum([v[0] for v in ARIYA.values()]) + ".",
}


def chunk(c, st):
    try:
        return T.chunk_q2(c, st)
    except KeyError:
        if c[:1].isupper():   # a sentence without a subject ("Sahetukā ceva na ca hetū.", "No āsavā.")
            return T.chunk_q2(low(c), st)
        raise


def q_line(t, ch):
    if t in LABELS:
        return LABELS[t]
    if t.startswith("Bāvīsatindriyāni " + DASH):
        return twenty_two()
    for a, b in T.FIXES + FIXES:
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
                ru.append(chunk(x, st))
        out.append(cap("".join(ru)) + ".")
    return " ".join(out)


# ================================================================ 10. build and write
def build(fn, builder):
    pali = open(os.path.join(S.PALI_DIR, fn), encoding="utf-8").read().rstrip("\n").split("\n")
    nonempty = [S.ID.sub("", l).rstrip() for l in pali if l.strip()]
    ru = builder(nonempty)
    assert len(ru) == len(nonempty), (fn, len(ru), len(nonempty))
    for p, r in zip(nonempty, ru):
        assert p.count(DASH) + p.count("—") == r.count(DASH), ("dash count", p[:70], r[:70])
        assert "—" not in r and "\x01" not in r and "\x02" not in r, r[:80]
        assert p.startswith("#") == r.startswith("#") and p.split(" ")[0].count("#") == r.split(" ")[0].count("#"), (p[:40], r[:40])
    lines = S.attach_ids(pali, ru)
    S.write(os.path.join(S.RU_DIR, fn), lines)
    print("OK:", fn, "|", len(ru), "non-empty lines")


def main():
    build("4-saccavibhango.md", build_ch4)
    build("5-indriyavibhango.md", build_ch5)


if __name__ == "__main__":
    main()
