"""Builder for the Russian rails translation of pi-2 (Vibhaṅga, plain audience), chapters 4 and 5
(Saccavibhaṅgo, Indriyavibhaṅgo).

Writes (only when run as a script):
  AI_translation/russian/pi-2-russian-plain-rails_split_chapters/4-saccavibhango.md
  AI_translation/russian/pi-2-russian-plain-rails_split_chapters/5-indriyavibhango.md
  0-INBOX/temp/pipeline/pi-2-ru/rails/notes-4-5.md   (new recurring formulas, Pāli = Russian)

Every Russian string comes from the fixed tables and functions below, so identical Pāli gives identical Russian.
Imported read-only: the approved sample builder (S), the chapter-1 builder (K1: matrix items, chain(), question
helpers, fixed strings) and the chapters 2-3 builder (K23: the question-section sentence engine, dh_pe(), the pi-1
feeling definitions). Their tables are extended only in memory, here. Passages shared with the Dhammasaṅgaṇī take
their Russian from the approved pi-1 rails (asserted to occur there by check_pi1()).

usage: python -I -X utf8 build_rails_4_5_ru.py
"""
import pathlib
import re
import sys

RAILS = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-ru\rails")
sys.path.insert(0, str(RAILS))
import build_rails_sample_ru as S  # noqa: E402  (importing writes nothing)
import build_rails_1_ru as K1      # noqa: E402  (importing writes nothing)
import build_rails_2_3_ru as K23   # noqa: E402  (importing writes nothing)

NOTES_PATH = RAILS / "notes-4-5.md"
cap, low, q = S.cap, K1.low, K23.q
SLIPS = []


def slip(msg):
    if msg not in SLIPS:
        SLIPS.append(msg)


def nlist(items):
    """«a, b и c»; a comma before «и» when the member before it ends in a participial clause"""
    if len(items) == 1:
        return items[0]
    sep = ", и " if ", " in items[-2] else " и "
    return ", ".join(items[:-1]) + sep + items[-1]


def called(ins, quoted=True):
    return f"это называется «{ins}»." if quoted else f"это называется {ins}."


# =========================================================================== shared pi-1 strings
WISDOM_SHORT = "мудрость, понимание… отсутствие заблуждения, исследование явлений, правильное воззрение"   # pi-1 ^1-1359
PATH_TAIL = "фактор пути, входящий в путь"                                                           # pi-1 ^1-283
WISDOM_PATH = f"{WISDOM_SHORT}, фактор пробуждения исследования явлений, {PATH_TAIL}"                  # pi-1 ^1-296 tail
SATI_LIST = ("осознанность, припоминание, воспоминание, осознанность, способность помнить, способность удерживать "
             "в памяти, отсутствие поверхностности, отсутствие забывчивости, осознанность, способность осознанности, "
             "сила осознанности, правильная осознанность")                                               # pi-1 ^1-1358
SAMADHI_LIST = ("устойчивость ума, собранность, стабильность, отсутствие рассеяния, отсутствие отвлечения, "
                "нерассеянность ума, успокоение, способность сосредоточения, сила сосредоточения, правильное "
                "сосредоточение")                                                                          # pi-1 ^1-11
SADDHA_LIST = "вера, доверие, уверенность, глубокая убеждённость, вера, способность веры, сила веры"   # pi-1 ^1-12
VIRIYA_HEAD = "душевное приложение усердия"                                                          # pi-1 ^1-22
VIRIYA_LIST_P1 = ("душевное приложение усердия, порыв, напор, старание, усилие, рвение, упорство, стойкость, "
                  "твёрдость, неослабевающий напор, неотступное желание, неотступное несение бремени, крепкое "
                  "удержание бремени, усердие, способность усердия, сила усердия")                       # pi-1 ^1-22
# pi-2 ^2-220 has «thāmo ṭhiti» where pi-1 has «thāmo dhiti»: ṭhiti translated as written (termbase «устойчивость»)
VIRIYA_LIST = VIRIYA_LIST_P1.replace("стойкость, твёрдость", "стойкость, устойчивость")
VITAKKA_SHORT = "мышление, направленная мысль"                                                       # pi-1 ^1-283
ABSTAIN = ("воздержание, полное воздержание, уклонение{v}, неделание, несовершение, невпадение в проступок, "
           "непереступание границы, разрушение моста")                                               # pi-1 ^1-299
VERAMANI_VAR = " [вариант написания (Ka.): veramaṇi, так же и далее]"   # [veramaṇi (ka.) evamuparipi]
LIFE_LIST = "срок жизни, сохранение, поддержание, продление, движение, течение, сбережение, жизнь, жизненная способность"
FEM_P1 = "женская внешность, женский признак, женское поведение, женская манера, женственность, женское свойство"
MASC_P1 = "мужская внешность, мужской признак, мужское поведение, мужская манера, мужественность, мужское свойство"
JARA_P1 = ("старение, одряхление, сломанные зубы, седые волосы, морщинистая кожа, сокращение срока жизни, "
           "изношенность способностей")                                                               # pi-1 ^1-643
FUNCTIONAL_P1 = "те функциональные явления, ни благие, ни неблагие и не являющиеся результатом действий"  # pi-1 ^1-583
ALL_RUPA = "вся материальная форма"                                                                   # pi-1 ^1-583
SUPRA_P1 = ("надмирское медитативное погружение, ведущее к освобождению и к убыванию, для устранения приверженности "
            "воззрениям, для достижения первой ступени и, полностью уединившись от чувственных удовольствий… входит "
            "в первое медитативное погружение, с трудным способом практики и медленным высшим знанием, и пребывает в "
            "нём, в это время")                                                                       # pi-1 ^1-277
JHANA1_P1 = ("полностью уединившись от чувственных удовольствий, уединившись от неблагих явлений, входит в первое "
             "медитативное погружение, с направленной мыслью и удержанием мысли, с восторгом и счастьем, рождёнными "
             "уединением")                                                                            # pi-1 ^1-160
JHANA2_P1 = ("с затиханием направленной мысли и удержания мысли входит во второе медитативное погружение, с ясностью "
             "внутри себя, с единением ума, без направленной мысли и без удержания мысли, с восторгом и счастьем, "
             "рождёнными сосредоточением")                                                            # pi-1 ^1-161
JHANA3_P1 = ("с угасанием восторга пребывает невозмутимым, осознанным и ясно понимающим, испытывает телом счастье, так "
             "что благородные говорят о нём – «Невозмутимый, осознанный, пребывающий в счастье», и входит в третье "
             "медитативное погружение")                                                               # pi-1 ^1-163
JHANA4_P1 = ("с устранением приятного и с устранением болезненного, с исчезновением ещё прежде радости и уныния входит "
             "в четвёртое медитативное погружение, которое ни болезненно, ни приятно, с чистотой невозмутимости и "
             "осознанности")                                                                          # pi-1 ^1-165
# pi-2 APPROVED: ajjhattaṃ = «внутренний» (pi-1 «внутри себя»)
JHANA2 = JHANA2_P1.replace("с ясностью внутри себя", "с внутренней ясностью")


def _assert(*strings):
    missing = [s for s in strings if s not in K23.PI1_ALL]
    assert not missing, f"not in pi-1 Russian: {missing}"


def check_pi1():
    K23.assert_pi1()                                           # loads K23.PI1_ALL
    jh = []
    for s in (JHANA1_P1, JHANA2_P1, JHANA3_P1, JHANA4_P1):      # pi-1 has a variant bracket after «погружение»
        a, b = s.split(" погружение", 1)
        jh += [a + " погружение", b.lstrip(",") if b.startswith(",") else b]
    missing = [s for s in jh if s.strip() and s not in K23.PI1_ALL]
    assert not missing, missing
    _assert(WISDOM_SHORT, "отсутствие заблуждения, исследование явлений, правильное воззрение, фактор "
                   "пробуждения исследования явлений, " + PATH_TAIL, SATI_LIST, SAMADHI_LIST, SADDHA_LIST, VIRIYA_LIST_P1,
                   VITAKKA_SHORT + ", помысел", ABSTAIN.format(v=""), LIFE_LIST, FEM_P1, MASC_P1, JARA_P1,
                   FUNCTIONAL_P1, ALL_RUPA, SUPRA_P1,
                   "отстранение от четырёх видов дурного речевого поведения",
                   "отстранение от трёх видов дурного телесного поведения", "отстранение от неправильного образа жизни",
                   "фактор пробуждения усердия, " + PATH_TAIL, "фактор пробуждения осознанности, " + PATH_TAIL,
                   "фактор пробуждения сосредоточения, " + PATH_TAIL, "у этих материальных явлений",
                   "у этих нематериальных явлений", "То, что у женщины есть", "То, что у мужчины есть",
                   "для непосредственного постижения тех явлений, которые не познаны, не увидены, не достигнуты, не "
                   "узнаны и не постигнуты непосредственно, есть мудрость, понимание",
                   "для непосредственного постижения тех явлений, которые познаны, увидены, достигнуты, узнаны и "
                   "постигнуты непосредственно, есть мудрость, понимание",
                   "есть контакт… есть отсутствие отвлечения", "есть пятичастный путь")


# =========================================================================== chapter 4: names
TRUTH = {  # the four truths as subjects (Abhidhamma names)
    "dukkhaṃ": "страдание", "dukkhasamudayo": "возникновение страдания", "dukkhanirodho": "прекращение страдания",
    "dukkhanirodhagāminī paṭipadā": "способ практики, ведущий к прекращению страдания",
}
TRUTH_INS = {"dukkhaṃ": "страданием", "dukkhasamudayo": "возникновением страдания",
             "dukkhanirodho": "прекращением страдания",
             "dukkhanirodhagāminī paṭipadā": "способом практики, ведущим к прекращению страдания"}
PATIPADA_PREP = "о способе практики, ведущем к прекращению страдания"
NOBLE = {  # «благородная истина о …» (dukkhaṃ ariyasaccaṃ …)
    "dukkhaṃ": "о страдании", "dukkhasamudayaṃ": "о возникновении страдания",
    "dukkhanirodhaṃ": "о прекращении страдания", "dukkhanirodhagāminī paṭipadā": PATIPADA_PREP,
}


def noble(k, case="nom"):
    head = {"nom": "благородная истина", "ins": "благородной истиной"}[case]
    return f"{head} {NOBLE[k]}"


FOUR_NOBLE = (f"Четыре благородные истины – {noble('dukkhaṃ')}, {noble('dukkhasamudayaṃ')}{{v1}}, "
              f"{noble('dukkhanirodhaṃ')}{{v2}} и {noble('dukkhanirodhagāminī paṭipadā')}.")
FOUR_NOBLE_V = ("[вариант написания (Syā.): dukkhasamudayo]", "[вариант написания (Syā.): dukkhanirodho]")
FOUR_TRUTHS = ("Четыре истины – " + nlist([TRUTH[k] for k in ("dukkhaṃ", "dukkhasamudayo", "dukkhanirodho",
                                                              "dukkhanirodhagāminī paṭipadā")]) + ".")
SUB_H = {"Dukkhasaccaṃ": "Истина о страдании", "Samudayasaccaṃ": "Истина о возникновении",
         "Nirodhasaccaṃ": "Истина о прекращении", "Maggasaccaṃ": "Истина о пути"}

# ---- Suttantabhājanīya: the truth of suffering
UPADANA_KH = {"rūpa": "совокупность материальной формы", "vedana": "совокупность чувств",
              "sañña": "совокупность восприятия", "saṅkhāra": "совокупность формирующих факторов",
              "viññāṇa": "совокупность сознания"}
OBJ_CL = "служащая объектом цепляния"
FIVE_UPA = "пять совокупностей, служащих объектом цепляния"                         # pañcupādānakkhandhā
FIVE_UPA_DUKKHA = f"{FIVE_UPA}, которые, короче говоря, являются страданием"       # saṃkhittena … dukkhā (noun)
FIVE_UPA_DUKKHA_INS = "пятью совокупностями, служащими объектом цепляния, которые, короче говоря, являются страданием"
APPIYA = "связь с неприятным, являющаяся страданием"                               # appiyehi sampayogo dukkho
APPIYA_INS = "связью с неприятным, являющейся страданием"
PIYA = "разлука с приятным, являющаяся страданием"                                 # piyehi vippayogo dukkho
PIYA_INS = "разлукой с приятным, являющейся страданием"
YAMPI = "не обретать желаемого тоже является страданием"            # yampicchaṃ na labhati tampi dukkhaṃ (labhati «обретать»)
SOKA5 = "печаль, стенания, боль, уныние и отчаяние"                                 # sokaparidevadukkhadomanassupāyāsā
SOKA5_DAT = "печали, стенаниям, боли, унынию и отчаянию"
DUKKHA_LIST = (
    "Рождение тоже является страданием, старение тоже является страданием, смерть тоже является страданием, "
    f"{SOKA5} тоже являются страданием, связь с неприятным является страданием, разлука с приятным является "
    f"страданием, {YAMPI}, короче говоря, "
    f"{FIVE_UPA}, являются страданием.")
BEINGS_CLASS = f"{S.BEINGS} в том или ином классе существ"            # tesaṃ tesaṃ sattānaṃ tamhi tamhi sattanikāye
JATI_LIST = ("рождение, зарождение, вхождение, появление, проявление совокупностей, получение сфер восприятия")
MARANA_LIST = ("уход из того или иного класса существ, выбывание, распад, исчезновение, гибель, смерть, кончина, "
               "распад совокупностей, оставление тела, прекращение жизненной способности")
STRUCK = ("У того, кого постигло несчастье с родственниками, или несчастье с богатством, или несчастье болезни, или "
          "несчастье в нравственности, или несчастье в воззрениях, кто охвачен каким-либо несчастьем, кого постигло "
          "какое-либо болезненное явление, есть")
# Ñātibyasanena vā phuṭṭhassa … aññataraññatarena dukkhadhammena phuṭṭhassa
SOKA_LIST = ("печаль, горевание, состояние горевания, внутренняя печаль, глубокая внутренняя печаль, изнурение ума, "
             "уныние, стрела печали")
PARIDEVA_LIST = ("плач, стенания, оплакивание, проявление стенаний, состояние плача, состояние стенаний, речь, болтовня, "
                 "бессвязная болтовня, сетование, проявление сетования, состояние сетования "
                 "[вариант написания (Syā.): lālapo lālapanā lālapitattaṃ]")
UPAYASA_LIST = "удручённость, отчаяние, состояние удручённости, состояние отчаяния"
UNWANTED = ("Когда здесь у кого-то есть нежеланные, немилые, неприятные видимые формы, звуки, запахи, вкусы и "
            "осязаемое или же есть те, кто желает ему вреда, желает ему неблага, желает ему неудобства, желает ему "
            "лишиться безопасности; то, что с ними есть сочетание, общение, соединение, смешение")
WANTED = ("Когда здесь у кого-то есть желанные, милые, приятные видимые формы, звуки, запахи, вкусы и осязаемое или "
          "же есть те, кто желает ему пользы, желает ему блага, желает ему удобства, желает ему безопасности, будь то "
          "мать, или отец, или брат, или сестра, или друзья, или сотоварищи, или родственники, или кровные родные; "
          "то, что с ними есть отсутствие сочетания, отсутствие общения, несоединение, несмешение")
WISH = "возникает такое желание – «О, если бы мы не были подвержены {a} и если бы к нам не {b}!»"
SUBJECT_TO = "у существ, подверженных"

# ---- the truth of the origin / cessation: the sense series
ORG = {"cakkhuṃ": ("глаз", "m"), "sotaṃ": ("ухо", "n"), "ghānaṃ": ("нос", "m"), "jivhā": ("язык", "m"),
       "kāyo": ("тело", "n"), "mano": ("ум", "m")}
OBJ = {"rūpā": ("видимые формы", "p"), "saddā": ("звуки", "p"), "gandhā": ("запахи", "p"), "rasā": ("вкусы", "p"),
       "phoṭṭhabbā": ("осязаемое", "n"), "dhammā": ("объекты ума", "p")}
OBJ_GEN = {"rūpa": "видимых форм", "sadda": "звуков", "gandha": "запахов", "rasa": "вкусов",
           "phoṭṭhabba": "осязаемого", "dhamma": "объектов ума"}
OBJ_O = {"rūpa": "о видимых формах", "sadda": "о звуках", "gandha": "о запахах", "rasa": "о вкусах",
         "phoṭṭhabba": "об осязаемом", "dhamma": "об объектах ума"}
OBJ_NA = {"rūpa": "на видимых формах", "sadda": "на звуках", "gandha": "на запахах", "rasa": "на вкусах",
          "phoṭṭhabba": "на осязаемом", "dhamma": "на объектах ума"}
SER = {  # X + saññā / sañcetanā / taṇhā / vitakko / vicāro
    "saññā": (lambda o: f"восприятие {OBJ_GEN[o]}", "n"),
    "sañcetanā": (lambda o: f"проявление намерения в отношении {OBJ_GEN[o]}", "n"),
    "taṇhā": (lambda o: f"жажда {OBJ_GEN[o]}", "f"),        # APPROVED: «жажда видимых форм» in the sense-object lists
    "vitakko": (lambda o: f"направленная мысль {OBJ_O[o]}", "f"),
    "vicāro": (lambda o: f"удержание мысли {OBJ_NA[o]}", "n"),
}
DEAR = {"m": "привлекателен и отраден", "n": "привлекательно и отрадно", "f": "привлекательна и отрадна",
        "p": "привлекательны и отрадны"}        # piyarūpaṃ sātarūpaṃ (said of the item)
IN_WORLD = "в мире"                               # loke


def sense_np(w):
    w = w[:1].lower() + w[1:]
    if w in ORG:
        return ORG[w]
    if w in OBJ:
        return OBJ[w]
    m = re.match(r"^(cakkhu|sota|ghāna|jivhā|kāya|mano)viññāṇaṃ$", w)
    if m:
        return K1.VINN[m.group(1)], "n"
    m = re.match(r"^(cakkhu|sota|ghāna|jivhā|kāya|mano)samphasso$", w)
    if m:
        return f"контакт {K1.SENSE_GEN[m.group(1)]}", "m"
    m = re.match(r"^(cakkhu|sota|ghāna|jivhā|kāya|mano)samphassajā vedanā$", w)
    if m:
        return f"рождённое контактом {K1.SENSE_GEN[m.group(1)]} чувство", "n"
    m = re.match(r"^(rūpa|sadda|gandha|rasa|phoṭṭhabba|dhamma)(saññā|sañcetanā|taṇhā|vitakko|vicāro)$", w)
    if m:
        fn, g = SER[m.group(2)]
        return fn(m.group(1)), g
    raise KeyError(w)


def dear_sentence(s):
    """Cakkhuṃ loke piyarūpaṃ sātarūpaṃ. / Sotaṃ loke…pe… ghānaṃ loke… mano loke piyarūpaṃ sātarūpaṃ."""
    assert s.endswith(" loke piyarūpaṃ sātarūpaṃ."), s
    parts = re.split(r"(…pe… |… )", s[:-len(" piyarūpaṃ sātarūpaṃ.")])
    out, g = "", None
    for i, p in enumerate(parts):
        if i % 2 == 1:
            out += "… "
            continue
        assert p.endswith(" loke"), (p, s)
        ru, g = sense_np(p[:-len(" loke")])
        out += (cap(ru) if i == 0 else ru) + f" {IN_WORLD}"
    return f"{out} {DEAR[g]}."


ARISE = "Здесь эта жажда, возникая, возникает, здесь, укореняясь, укореняется."
CEASE = "Здесь эта жажда, устраняясь, устраняется, здесь, прекращаясь, прекращается."
WHAT_DEAR = f"А что {IN_WORLD} привлекательно и отрадно?"

# ---- the truth of the path (Suttanta)
PATH8 = ["правильное воззрение", "правильный помысел", "правильная речь", "правильное действие",
         "правильный образ жизни", "правильное усилие", "правильная осознанность", "правильное сосредоточение"]
PATH8_P = ["sammādiṭṭhi", "sammāsaṅkappo", "sammāvācā", "sammākammanto", "sammāājīvo", "sammāvāyāmo", "sammāsati",
           "sammāsamādhi"]
PATH_RU = dict(zip(PATH8_P, PATH8))
PATH_INS = dict(zip(PATH8_P, ["правильным воззрением", "правильным помыслом", "правильной речью",
                              "правильным действием", "правильным образом жизни", "правильным усилием",
                              "правильной осознанностью", "правильным сосредоточением"]))
EFFORT = "порождает желание, прилагает усилие, пробуждает усердие, напрягает ум, прилагает старания"
# chandaṃ janeti, vāyamati, vīriyaṃ ārabhati, cittaṃ paggaṇhāti, padahati
MONK = "Здесь монах"                                              # Idha bhikkhu
CONTEMPL = ("ревностный, ясно понимающий, осознанный, устранив алчность и уныние в отношении мира")
# ātāpī sampajāno satimā, vineyya loke abhijjhādomanassaṃ

SENT4 = {  # fixed sentences of chapter 4 (Pāli sentence = Russian)
    "Tattha katamaṃ dukkhaṃ ariyasaccaṃ?": q(noble("dukkhaṃ")),
    "Tattha katamaṃ dukkhasamudayaṃ ariyasaccaṃ?": q(noble("dukkhasamudayaṃ")),
    "Tattha katamaṃ dukkhanirodhaṃ ariyasaccaṃ?": q(noble("dukkhanirodhaṃ")),
    "Tattha katamaṃ dukkhanirodhagāminī paṭipadā ariyasaccaṃ?": q(noble("dukkhanirodhagāminī paṭipadā")),
    ("Jātipi dukkhā, jarāpi dukkhā, maraṇampi dukkhaṃ, sokaparidevadukkhadomanassupāyāsāpi dukkhā, appiyehi sampayogo "
     "dukkho, piyehi vippayogo dukkho, yaṃ picchaṃ na labhati tampi dukkhaṃ, saṃkhittena pañcupādānakkhandhā "
     "dukkhā."): DUKKHA_LIST,
    "Tattha katamā jāti?": q("рождение"),
    "Tattha katamā jarā?": q("старение"),
    "Tattha katamaṃ maraṇaṃ?": q("смерть"),
    "Tattha katamo soko?": q("печаль"),
    "Tattha katamo paridevo?": q("стенания"),
    "Tattha katamaṃ dukkhaṃ?#S": q("боль"),
    "Tattha katamaṃ dukkhaṃ?#A": q("страдание"),
    "Tattha katamaṃ domanassaṃ?": q("уныние"),
    "Tattha katamo upāyāso?": q("отчаяние"),
    "Tattha katamo appiyehi sampayogo dukkho?": q(APPIYA),
    "Tattha katamo piyehi vippayogo dukkho?": q(PIYA),
    "Tattha katamaṃ yampicchaṃ na labhati tampi dukkhaṃ?": f"Что значит {S.TATTHA}: {YAMPI}?",
    "Tattha katame saṃkhittena pañcupādānakkhandhā dukkhā?": q(FIVE_UPA_DUKKHA),
    ('Jātidhammānaṃ sattānaṃ evaṃ icchā uppajjati – "aho vata, mayaṃ na jātidhammā assāma; na ca, vata, no jāti '
     'āgaccheyyā"ti!'): f"{cap(SUBJECT_TO)} рождению, " + WISH.format(a="рождению", b="приходило рождение"),
    ("Jarādhammānaṃ sattānaṃ…pe… byādhidhammānaṃ sattānaṃ…pe… maraṇadhammānaṃ sattānaṃ…pe… "
     'sokaparidevadukkhadomanassupāyāsadhammānaṃ sattānaṃ evaṃ icchā uppajjati – "aho vata, mayaṃ na '
     'sokaparidevadukkhadomanassupāyāsadhammā assāma; na ca, vata, no sokaparidevadukkhadomanassupāyāsā '
     'āgaccheyyu"nti!'): (f"{cap(SUBJECT_TO)} старению… {SUBJECT_TO} болезни… {SUBJECT_TO} смерти… {SUBJECT_TO} "
                          f"{SOKA5_DAT}, " + WISH.format(a=SOKA5_DAT, b=f"приходили {SOKA5}")),
    "Na kho panetaṃ icchāya pattabbaṃ.": "Но этого невозможно достичь желанием.",
    'Idampi "yampicchaṃ na labhati tampi dukkhaṃ".': f"Это тоже: «{YAMPI}».",
    ("Seyyathidaṃ – rūpupādānakkhandho, vedanupādānakkhandho, saññupādānakkhandho, saṅkhārupādānakkhandho, "
     "viññāṇupādānakkhandho."): (f"{cap(K23.NAMELY)} "
                                 + nlist([f"{UPADANA_KH[k]}, {OBJ_CL}" for k in UPADANA_KH]) + "."),
    'Ime vuccanti "saṃkhittena pañcupādānakkhandhā dukkhā".': f"Это называется «{FIVE_UPA_DUKKHA_INS}».",
    'Idaṃ vuccati "dukkhaṃ ariyasaccaṃ".': f"Это называется «{noble('dukkhaṃ', 'ins')}».",
    'Idaṃ vuccati "dukkhasamudayaṃ ariyasaccaṃ".': f"Это называется «{noble('dukkhasamudayaṃ', 'ins')}».",
    'Idaṃ vuccati "dukkhanirodhaṃ ariyasaccaṃ".': f"Это называется «{noble('dukkhanirodhaṃ', 'ins')}».",
    'Idaṃ vuccati "dukkhanirodhagāminī paṭipadā ariyasaccaṃ".':
        f"Это называется «{noble('dukkhanirodhagāminī paṭipadā', 'ins')}».",
    ("Yāyaṃ taṇhā ponobhavikā [ponobbhavikā (syā. ka.)] nandirāgasahagatā tatratatrābhinandinī, seyyathidaṃ – "
     "kāmataṇhā, bhavataṇhā, vibhavataṇhā."):
        ("Та жажда, ведущая к новому существованию [вариант написания (Syā., Ka.): ponobbhavikā], сопровождаемая "
         "наслаждением и страстью, находящая радость то здесь, то там, а именно – "
         + nlist(["чувственная жажда", "жажда существования", "жажда несуществования"]) + "."),
    "Sā kho panesā taṇhā kattha uppajjamānā uppajjati, kattha nivisamānā nivisati?":
        "А где эта жажда, возникая, возникает, где, укореняясь, укореняется?",
    "Yaṃ loke piyarūpaṃ sātarūpaṃ, etthesā taṇhā uppajjamānā uppajjati, ettha nivisamānā nivisati.":
        f"Что {IN_WORLD} привлекательно и отрадно, здесь эта жажда, возникая, возникает, здесь, укореняясь, "
        "укореняется.",
    "Kiñca loke piyarūpaṃ sātarūpaṃ?": WHAT_DEAR,
    "Etthesā taṇhā uppajjamānā uppajjati, ettha nivisamānā nivisati.": ARISE,
    "Yo tassāyeva taṇhāya asesavirāganirodho cāgo paṭinissaggo mutti anālayo.":
        ("Угасание без остатка и прекращение этой самой жажды, отказ от неё, оставление её, освобождение от неё, "
         "отсутствие привязанности к ней."),
    "Sā kho panesā taṇhā kattha pahīyamānā pahīyati, kattha nirujjhamānā nirujjhati?":
        "А где эта жажда, устраняясь, устраняется, где, прекращаясь, прекращается?",
    "Yaṃ loke piyarūpaṃ sātarūpaṃ, etthesā taṇhā pahīyamānā pahīyati, ettha nirujjhamānā nirujjhati.":
        f"Что {IN_WORLD} привлекательно и отрадно, здесь эта жажда, устраняясь, устраняется, здесь, прекращаясь, "
        "прекращается.",
    "Etthesā taṇhā pahīyamānā pahīyati, ettha nirujjhamānā nirujjhati.": CEASE,
    ("Ayameva ariyo aṭṭhaṅgiko maggo, seyyathidaṃ – sammādiṭṭhi, sammāsaṅkappo, sammāvācā, sammākammanto, "
     "sammāājīvo, sammāvāyāmo, sammāsati, sammāsamādhi."):
        f"Это именно благородный восьмичастный путь, {K23.NAMELY} {nlist(PATH8)}.",
    "Idha ariyasāvako micchāājīvaṃ pahāya sammāājīvena jīvikaṃ kappeti":
        "Здесь благородный ученик, устранив ложный образ жизни, поддерживает жизнь правильным образом жизни",
    ("Idha bhikkhu anuppannānaṃ pāpakānaṃ akusalānaṃ dhammānaṃ anuppādāya chandaṃ janeti, vāyamati, vīriyaṃ "
     "ārabhati, cittaṃ paggaṇhāti, padahati."):
        f"{MONK} ради невозникновения невозникших дурных неблагих явлений {EFFORT}.",
    ("Uppannānaṃ pāpakānaṃ akusalānaṃ dhammānaṃ pahānāya chandaṃ janeti, vāyamati, vīriyaṃ ārabhati, cittaṃ "
     "paggaṇhāti, padahati."): f"Ради устранения возникших дурных неблагих явлений {EFFORT}.",
    ("Anuppannānaṃ kusalānaṃ dhammānaṃ uppādāya chandaṃ janeti, vāyamati, vīriyaṃ ārabhati, cittaṃ paggaṇhāti, "
     "padahati."): f"Ради возникновения невозникших благих явлений {EFFORT}.",
    ("Uppannānaṃ kusalānaṃ dhammānaṃ ṭhitiyā asammosāya bhiyyobhāvāya vepullāya bhāvanāya pāripūriyā chandaṃ "
     "janeti, vāyamati, vīriyaṃ ārabhati, cittaṃ paggaṇhāti, padahati."):
        ("Ради сохранения, неутраты, умножения, обширности, развития и завершённости возникших благих явлений "
         f"{EFFORT}."),
    ("Idha bhikkhu kāye kāyānupassī viharati ātāpī sampajāno satimā, vineyya loke abhijjhādomanassaṃ."):
        f"{MONK} пребывает, в теле созерцая тело, {CONTEMPL}.",
    ("Vedanāsu…pe… citte…pe… dhammesu dhammānupassī viharati ātāpī sampajāno satimā, vineyya loke "
     "abhijjhādomanassaṃ."): f"Он пребывает, в чувствах… в уме… в явлениях созерцая явления, {CONTEMPL}.",
    ("Idha bhikkhu vivicceva kāmehi, vivicca akusalehi dhammehi, savitakkaṃ savicāraṃ vivekajaṃ pītisukhaṃ paṭhamaṃ "
     "jhānaṃ upasampajja viharati."): f"{MONK}, {JHANA1_P1}, и пребывает в нём.",
    ("Vitakkavicārānaṃ vūpasamā, ajjhattaṃ sampasādanaṃ, cetaso ekodibhāvaṃ avitakkaṃ avicāraṃ samādhijaṃ "
     "pītisukhaṃ dutiyaṃ jhānaṃ upasampajja viharati."): f"{cap(JHANA2.replace('входит', 'он входит', 1))}, и пребывает в нём.",
    ("Pītiyā ca virāgā, upekkhako ca viharati, sato ca sampajāno, sukhañca kāyena paṭisaṃvedeti, yaṃ taṃ ariyā "
     'ācikkhanti – "upekkhako satimā sukhavihārī"ti, tatiyaṃ jhānaṃ upasampajja viharati.'):
        f"{cap(JHANA3_P1.replace('пребывает невозмутимым', 'он пребывает невозмутимым', 1))} и пребывает в нём.",
    ("Sukhassa ca pahānā, dukkhassa ca pahānā, pubbeva somanassadomanassānaṃ atthaṅgamā, adukkhamasukhaṃ "
     "upekkhāsatipārisuddhiṃ catutthaṃ jhānaṃ upasampajja viharati."):
        f"{cap(JHANA4_P1.replace('входит', 'он входит', 1))}, и пребывает в нём.",
    "Suttantabhājanīyaṃ.": f"{S.SUTTANTA_BH}.",
    "Abhidhammabhājanīyaṃ.": f"{S.ABHI_BH}.",
    "Pañhāpucchakaṃ.": f"{S.PANHA}.",
    "Saccavibhaṅgo niṭṭhito.": f"{S.CH_TITLE[4][1]} {S.DONE}.",
    "Indriyavibhaṅgo niṭṭhito.": f"{S.CH_TITLE[5][1]} {S.DONE}.",
    # ---- Abhidhammabhājanīya
    "Cattāri saccāni – dukkhaṃ, dukkhasamudayo, dukkhanirodho, dukkhanirodhagāminī paṭipadā.": FOUR_TRUTHS,
    "Tattha katamo dukkhasamudayo?": q(TRUTH["dukkhasamudayo"]),
    "Tattha katamo dukkhanirodho?": q(TRUTH["dukkhanirodho"]),
    "Tattha katamā dukkhanirodhagāminī paṭipadā?": q(TRUTH["dukkhanirodhagāminī paṭipadā"]),
    'Ayaṃ vuccati "dukkhanirodhagāminī paṭipadā".': f"Это называется «{TRUTH_INS['dukkhanirodhagāminī paṭipadā']}».",
    'Ayaṃ vuccati – "dukkhanirodhagāminī paṭipadā".':
        f"Это называется – «{TRUTH_INS['dukkhanirodhagāminī paṭipadā']}».",
    "Avasesā dhammā dukkhanirodhagāminiyā paṭipadāya sampayuttā.":
        "Остальные явления связаны со способом практики, ведущим к прекращению страдания.",
}
for _p, _r in zip(PATH8_P, PATH8):
    _w = {"sammādiṭṭhi": "katamā", "sammāvācā": "katamā", "sammāsati": "katamā"}.get(_p, "katamo")
    SENT4[f"Tattha {_w} {_p}?"] = q(_r)
    SENT4[f'Ayaṃ vuccati "{_p}".'] = f"Это называется «{PATH_INS[_p]}»."

# answers «<body> – ayaṃ/idaṃ vuccati "<term>".»: body -> (Russian, comma before the dash)
BODY = {
    # Suttanta
    ("Yā tesaṃ tesaṃ sattānaṃ tamhi tamhi sattanikāye jāti sañjāti okkanti abhinibbatti khandhānaṃ pātubhāvo "
     "āyatanānaṃ paṭilābho"): (f"То, что {BEINGS_CLASS} есть {JATI_LIST}", True),
    ("Yā tesaṃ tesaṃ sattānaṃ tamhi tamhi sattanikāye jarā jīraṇatā khaṇḍiccaṃ pāliccaṃ valittacatā āyuno saṃhāni "
     "indriyānaṃ paripāko"): (f"То, что {BEINGS_CLASS} есть {JARA_P1}", True),
    ("Yā tesaṃ tesaṃ sattānaṃ tamhā tamhā sattanikāyā cuti cavanatā bhedo antaradhānaṃ maccu maraṇaṃ kālakiriyā "
     "khandhānaṃ bhedo kaḷevarassa nikkhepo jīvitindriyassupacchedo"): (f"То, что {S.BEINGS} есть {MARANA_LIST}", True),
    "#soka": (f"{STRUCK} {SOKA_LIST}", True),
    "#parideva": (f"{STRUCK} {PARIDEVA_LIST}", True),
    "#upayasa": (f"{STRUCK} {UPAYASA_LIST}", True),
    ("Yaṃ kāyikaṃ asātaṃ kāyikaṃ dukkhaṃ kāyasamphassajaṃ asātaṃ dukkhaṃ vedayitaṃ kāyasamphassajā asātā dukkhā "
     "vedanā"): (f"То, что есть {K23.FEELING_P1['dukkha']}", True),
    ("Yaṃ cetasikaṃ asātaṃ cetasikaṃ dukkhaṃ cetosamphassajaṃ asātaṃ dukkhaṃ vedayitaṃ cetosamphassajā asātā dukkhā "
     "vedanā"): (f"То, что есть {K23.FEELING_P1['domanassa']}", True),
    ("Yaṃ kāyikaṃ sātaṃ kāyikaṃ sukhaṃ kāyasamphassajaṃ sātaṃ sukhaṃ vedayitaṃ kāyasamphassajā sātā sukhā vedanā"):
        (f"То, что есть {K23.FEELING_P1['sukha']}", True),
    ("Yaṃ cetasikaṃ sātaṃ cetasikaṃ sukhaṃ cetosamphassajaṃ sātaṃ sukhaṃ vedayitaṃ cetosamphassajā sātā sukhā "
     "vedanā"): (f"То, что есть {K23.FEELING_P1['somanassa']}", True),
    ("Yaṃ cetasikaṃ neva sātaṃ nāsātaṃ cetosamphassajaṃ adukkhamasukhaṃ vedayitaṃ cetosamphassajā adukkhamasukhā "
     "vedanā"): (f"То, что есть {K23.FEELING_P1['upekkhā']}", True),
    ("Idha yassa te honti aniṭṭhā akantā amanāpā rūpā saddā gandhā rasā phoṭṭhabbā, ye vā panassa te honti "
     "anatthakāmā ahitakāmā aphāsukakāmā ayogakkhemakāmā; yā tehi saṅgati samāgamo samodhānaṃ missībhāvo"):
        (UNWANTED, True),
    ("Idha yassa te honti iṭṭhā kantā manāpā rūpā saddā gandhā rasā phoṭṭhabbā, ye vā panassa te honti atthakāmā "
     "hitakāmā phāsukakāmā yogakkhemakāmā mātā vā pitā vā bhātā vā bhaginī vā mittā vā amaccā vā ñātī vā sālohitā "
     "vā; yā tehi asaṅgati asamāgamo asamodhānaṃ amissībhāvo"): (WANTED, True),
    "Dukkhe ñāṇaṃ, dukkhasamudaye ñāṇaṃ, dukkhanirodhe ñāṇaṃ, dukkhanirodhagāminiyā paṭipadāya ñāṇaṃ":
        ("Знание о страдании, знание о возникновении страдания, знание о прекращении страдания, знание "
         f"{PATIPADA_PREP}", True),
    "Nekkhammasaṅkappo, abyāpādasaṅkappo, avihiṃsāsaṅkappo":
        ("Помысел об отречении, помысел об отсутствии недоброжелательности, помысел об отсутствии жестокости", False),
    "Musāvādā veramaṇī, pisuṇāya vācāya veramaṇī, pharusāya vācāya veramaṇī, samphappalāpā veramaṇī":
        ("Воздержание от лжи, воздержание от речи, сеющей раздор, воздержание от грубой речи, воздержание от пустой "
         "болтовни", False),
    "Pāṇātipātā veramaṇī, adinnādānā veramaṇī, kāmesumicchācārā veramaṇī":
        ("Воздержание от убийства живых существ, воздержание от взятия того, что не дано, воздержание от "
         "неправильного поведения в чувственных удовольствиях", False),
    "Idha ariyasāvako micchāājīvaṃ pahāya sammāājīvena jīvikaṃ kappeti":
        ("Здесь благородный ученик, устранив ложный образ жизни, поддерживает жизнь правильным образом жизни", False),
    # Abhidhamma
    ("Yā paññā pajānanā…pe… amoho dhammavicayo sammādiṭṭhi dhammavicayasambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ"):
        (f"То, что есть {WISDOM_PATH}", True),
    "Yo takko vitakko…pe… sammāsaṅkappo maggaṅgaṃ maggapariyāpannaṃ":
        (f"То, что есть {VITAKKA_SHORT}… правильный помысел, {PATH_TAIL}", True),
    ("Yā catūhi vacīduccaritehi ārati virati paṭivirati veramaṇī [veramaṇi (ka.) evamuparipi] akiriyā akaraṇaṃ "
     "anajjhāpatti velāanatikkamo setughāto sammāvācā maggaṅgaṃ maggapariyāpannaṃ"):
        ("То, что есть отстранение от четырёх видов дурного речевого поведения, "
         f"{ABSTAIN.format(v=VERAMANI_VAR)}, правильная речь, {PATH_TAIL}", True),
    ("Yā tīhi kāyaduccaritehi ārati virati paṭivirati veramaṇī akiriyā akaraṇaṃ anajjhāpatti velāanatikkamo "
     "setughāto sammākammanto maggaṅgaṃ maggapariyāpannaṃ"):
        ("То, что есть отстранение от трёх видов дурного телесного поведения, "
         f"{ABSTAIN.format(v='')}, правильное действие, {PATH_TAIL}", True),
    ("Yā micchā ājīvā ārati virati paṭivirati veramaṇī akiriyā akaraṇaṃ anajjhāpatti velāanatikkamo setughāto "
     "sammāājīvo maggaṅgaṃ maggapariyāpannaṃ"):
        (f"То, что есть отстранение от ложного образа жизни, {ABSTAIN.format(v='')}, правильный образ жизни, "
         f"{PATH_TAIL}", True),
    ("Yo cetasiko vīriyārambho [viriyārambho (sī. syā.)] …pe… sammāvāyāmo vīriyasambojjhaṅgo maggaṅgaṃ "
     "maggapariyāpannaṃ"):
        (f"То, что есть {VIRIYA_HEAD} [вариант написания (Sī., Syā.): viriyārambho]… правильное усилие, фактор "
         f"пробуждения усердия, {PATH_TAIL}", True),
    "Yo cetasiko vīriyārambho…pe… sammāvāyāmo vīriyasambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ":
        (f"То, что есть {VIRIYA_HEAD}… правильное усилие, фактор пробуждения усердия, {PATH_TAIL}", True),
    "Yā sati anussati…pe… sammāsati satisambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ":
        (f"То, что есть осознанность, припоминание… правильная осознанность, фактор пробуждения осознанности, "
         f"{PATH_TAIL}", True),
    "Yā cittassa ṭhiti saṇṭhiti…pe… sammāsamādhi samādhisambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ":
        (f"То, что есть устойчивость ума, собранность… правильное сосредоточение, фактор пробуждения "
         f"сосредоточения, {PATH_TAIL}", True),
    "Yā cittassa ṭhiti…pe… sammāsamādhi samādhisambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ":
        (f"То, что есть устойчивость ума… правильное сосредоточение, фактор пробуждения сосредоточения, "
         f"{PATH_TAIL}", True),
}
CALLED_S = {"jāti": "рождением", "jarā": "старением", "maraṇaṃ": "смертью", "soko": "печалью",
            "paridevo": "стенаниями", "dukkhaṃ": "болью", "domanassaṃ": "унынием", "upāyāso": "отчаянием",
            "appiyehi sampayogo dukkho": APPIYA_INS, "piyehi vippayogo dukkho": PIYA_INS}
CALLED_A = dict(TRUTH_INS)
CALLED_A.update(PATH_INS)
CALLED_S.update(PATH_INS)

# ---- Abhidhamma lists of the four truths (nominative / genitive members)
SAM_NOM = {
    "taṇhā": "жажда", "avasesā ca kilesā": "остальные омрачения",
    "avasesā ca akusalā dhammā": "остальные неблагие явления",
    "tīṇi ca kusalamūlāni sāsavāni": "три благих корня, подверженных влечениям",
    "avasesā ca sāsavā kusalā dhammā": "остальные подверженные влечениям благие явления",
    "sāsavā ca kusalākusalānaṃ dhammānaṃ vipākā": "подверженные влечениям результаты благих и неблагих явлений",
    "sāsavā kusalākusalānaṃ dhammānaṃ vipākā": "подверженные влечениям результаты благих и неблагих явлений",
    "ye ca dhammā kiriyā neva kusalā nākusalā na ca kammavipākā": FUNCTIONAL_P1,
    "sabbañca rūpaṃ": ALL_RUPA,
}
NIR_GEN = {
    "taṇhāya": "жажды", "avasesānañca kilesānaṃ": "остальных омрачений",
    "avasesānañca akusalānaṃ dhammānaṃ": "остальных неблагих явлений",
    "tiṇṇañca kusalamūlānaṃ sāsavānaṃ": "трёх благих корней, подверженных влечениям",
    "avasesānañca sāsavānaṃ kusalānaṃ dhammānaṃ": "остальных подверженных влечениям благих явлений",
}
ABANDON = "Устранение"     # pahānaṃ


def list_body(body):
    """Abhidhamma lists: «Taṇhā ca avasesā ca kilesā, …» / «Taṇhāya ca, avasesānañca kilesānaṃ … pahānaṃ»"""
    if body.endswith(" pahānaṃ"):
        b = body[:-len(" pahānaṃ")]
        b = re.sub(r"^Taṇhāya ca, ", "taṇhāya, ", b)
        b = re.sub(r"^Taṇhāya$", "taṇhāya", b)
        items = [NIR_GEN[x] for x in b.split(", ")]
        return f"{ABANDON} {nlist(items)}", ", " in items[-1]
    b = re.sub(r"^Taṇhā ca,? ", "taṇhā, ", body)
    b = re.sub(r"^Taṇhā$", "taṇhā", b)
    b = b[:1].lower() + b[1:]
    items = [SAM_NOM[x] for x in b.split(", ")]
    ru = nlist(items)
    return cap(ru), ", " in items[-1]


ANSWER_RX = re.compile(r'^(.*?) – (ayaṃ|idaṃ) vuccati "(.+)"\.$')
STRUCK_P = ("Ñātibyasanena vā phuṭṭhassa bhogabyasanena vā phuṭṭhassa rogabyasanena vā phuṭṭhassa sīlabyasanena vā "
            "phuṭṭhassa diṭṭhibyasanena vā phuṭṭhassa aññataraññatarena byasanena samannāgatassa aññataraññatarena "
            "dukkhadhammena phuṭṭhassa ")
STRUCK_KEY = {"soko socanā": "#soka", "ādevo paridevo": "#parideva", "āyāso upāyāso": "#upayasa"}

# the supramundane path frame of the Abhidhammabhājanīya
SUPRA_RX = re.compile(r"^Idha bhikkhu yasmiṃ samaye lokuttaraṃ jhānaṃ bhāveti niyyānikaṃ apacayagāmiṃ diṭṭhigatānaṃ "
                      r"pahānāya paṭhamāya bhūmiyā pattiyā,? vivicceva kāmehi…pe… paṭhamaṃ jhānaṃ upasampajja viharati "
                      r"dukkhapaṭipadaṃ dandhābhiññaṃ, tasmiṃ samaye (.*)$")
SUPRA_TAIL = {
    "aṭṭhaṅgiko maggo hoti sammādiṭṭhi…pe… sammāsamādhi.": "есть восьмичастный путь: правильное воззрение… правильное "
                                                           "сосредоточение.",
    "aṭṭhaṅgiko maggo hoti – sammādiṭṭhi…pe… sammāsamādhi.": "есть восьмичастный путь – правильное воззрение… "
                                                             "правильное сосредоточение.",
    "pañcaṅgiko maggo hoti – sammādiṭṭhi, sammāsaṅkappo, sammāvāyāmo, sammāsati, sammāsamādhi.":
        "есть пятичастный путь – " + nlist([PATH_RU[k] for k in ("sammādiṭṭhi", "sammāsaṅkappo", "sammāvāyāmo",
                                                                  "sammāsati", "sammāsamādhi")]) + ".",
    "phasso hoti…pe… avikkhepo hoti.": "есть контакт… есть отсутствие отвлечения.",
}
SUPRA_HEAD = f"В то время, когда здесь монах развивает {SUPRA_P1}"


def split_sents(line):
    pieces = re.split(r"(?<=[.?!]) ", line)
    out = []
    for p in pieces:
        if out and (p[:1].islower() or p[:1] in "…"):
            out[-1] += " " + p
        else:
            out.append(p)
    return out


def sent4(s, section):
    key = f"{s}#{section}"
    if key in SENT4:
        return SENT4[key]
    if s in SENT4:
        return SENT4[s]
    if s.endswith(" loke piyarūpaṃ sātarūpaṃ."):
        return dear_sentence(s)
    m = SUPRA_RX.match(s)
    if m:
        return f"{SUPRA_HEAD} {SUPRA_TAIL[m.group(1)]}"
    m = ANSWER_RX.match(s)
    if m:
        body, _, term = m.groups()
        if body.startswith(STRUCK_P):
            rest = body[len(STRUCK_P):]
            body = next(v for k, v in STRUCK_KEY.items() if rest.startswith(k))
            if "lālappitattaṃ [lālapo" in rest:
                pass
        if body in BODY:
            ru, comma = BODY[body]
        else:
            ru, comma = list_body(body)
        ins = (CALLED_S if section == "S" else CALLED_A)[term]
        return f"{ru}{',' if comma else ''} – {called(ins)}"
    raise KeyError(s)


def line4(ln, section):
    return " ".join(sent4(s, section) for s in split_sents(ln))


# =========================================================================== chapter 5: names
IND = {
    "cakkhu": "способность глаза", "sota": "способность уха", "ghāna": "способность носа",
    "jivhā": "способность языка", "kāya": "способность тела", "mana": "способность ума",
    "itthi": "способность женственности", "purisa": "способность мужественности", "jīvita": "жизненная способность",
    "sukha": "способность удовольствия", "dukkha": "способность боли", "somanassa": "способность радости",
    "domanassa": "способность уныния", "upekkhā": "способность невозмутимости", "saddhā": "способность веры",
    "vīriya": "способность усердия", "sati": "способность осознанности", "samādhi": "способность сосредоточения",
    "paññā": "способность мудрости", "anaññātaññassāmīta": "способность познания непознанного",
    "añña": "способность окончательного знания", "aññātāvi": "способность обладателя окончательного знания",
    "rūpajīvita": "материальная жизненная способность", "arūpajīvita": "нематериальная жизненная способность",
}
IND_P = {  # Pāli headword -> key
    "cakkhundriyaṃ": "cakkhu", "sotindriyaṃ": "sota", "ghānindriyaṃ": "ghāna", "jivhindriyaṃ": "jivhā",
    "kāyindriyaṃ": "kāya", "manindriyaṃ": "mana", "itthindriyaṃ": "itthi", "purisindriyaṃ": "purisa",
    "jīvitindriyaṃ": "jīvita", "sukhindriyaṃ": "sukha", "dukkhindriyaṃ": "dukkha", "somanassindriyaṃ": "somanassa",
    "domanassindriyaṃ": "domanassa", "upekkhindriyaṃ": "upekkhā", "saddhindriyaṃ": "saddhā",
    "vīriyindriyaṃ": "vīriya", "satindriyaṃ": "sati", "samādhindriyaṃ": "samādhi", "paññindriyaṃ": "paññā",
    "anaññātaññassāmītindriyaṃ": "anaññātaññassāmīta", "aññindriyaṃ": "añña", "aññātāvindriyaṃ": "aññātāvi",
    "rūpajīvitindriyaṃ": "rūpajīvita", "arūpajīvitindriyaṃ": "arūpajīvita",
    "arūpajīvatindriyaṃ": "arūpajīvita",       # ^2-220 slip of the source (jīvata), rendered as meant
}
IND22 = ["cakkhu", "sota", "ghāna", "jivhā", "kāya", "mana", "itthi", "purisa", "jīvita", "sukha", "dukkha",
         "somanassa", "domanassa", "upekkhā", "saddhā", "vīriya", "sati", "samādhi", "paññā", "anaññātaññassāmīta",
         "añña", "aññātāvi"]


def iins(k):
    """instrumental: «способностью глаза», «жизненной способностью», «материальной жизненной способностью»"""
    r = IND[k]
    r = re.sub(r"\bспособность\b", "способностью", r)
    r = re.sub(r"\b(\w+)ая\b", r"\1ой", r)
    return r


IND22_LINE = ("Двадцать две способности – " + nlist([IND[k] for k in IND22]) + ".")
IND22_LINE_V = IND22_LINE.replace("способность усердия,", "способность усердия [вариант написания (Sī., Syā.): "
                                                          "viriyindriyaṃ],")
UNKNOWN_HEAD = ("То, что для непосредственного постижения тех явлений, которые {x}, есть "
                f"{WISDOM_PATH}")
UNKNOWN_X = {"anaññātānaṃ adiṭṭhānaṃ appattānaṃ aviditānaṃ asacchikatānaṃ":
             "не познаны, не увидены, не достигнуты, не узнаны и не постигнуты непосредственно",   # pi-1 ^1-296
             "ñātānaṃ diṭṭhānaṃ pattānaṃ viditānaṃ sacchikatānaṃ":
             "познаны, увидены, достигнуты, узнаны и постигнуты непосредственно",                  # pi-1 ^1-364
             "aññātāvīnaṃ diṭṭhānaṃ pattānaṃ viditānaṃ sacchikatānaṃ":
             "познаны окончательным знанием, увидены, достигнуты, узнаны и постигнуты непосредственно"}  # pi-2 only

BODY5 = {
    "Yaṃ itthiyā itthiliṅgaṃ itthinimittaṃ itthikuttaṃ itthākappo itthattaṃ itthibhāvo": f"То, что у женщины есть {FEM_P1}",
    ("Yaṃ purisassa purisaliṅgaṃ purisanimittaṃ purisakuttaṃ purisākappo purisattaṃ purisabhāvo"):
        f"То, что у мужчины есть {MASC_P1}",
    ("Yo tesaṃ rūpīnaṃ dhammānaṃ āyu ṭhiti yapanā yāpanā iriyanā vattanā pālanā jīvitaṃ jīvitindriyaṃ"):
        f"То, что у этих материальных явлений есть {LIFE_LIST}",
    ("Yo tesaṃ arūpīnaṃ dhammānaṃ āyu ṭhiti yapanā yāpanā iriyanā vattanā pālanā jīvitaṃ jīvitindriyaṃ"):
        f"То, что у этих нематериальных явлений есть {LIFE_LIST}",
    "Yā saddhā saddahanā okappanā abhippasādo saddhā saddhindriyaṃ saddhābalaṃ": f"То, что есть {SADDHA_LIST}",
    ("Yo cetasiko vīriyārambho nikkamo parakkamo uyyāmo vāyāmo ussāho ussoḷhī thāmo ṭhiti asithilaparakkamatā "
     "anikkhittachandatā anikkhittadhuratā dhurasampaggāho vīriyaṃ vīriyindriyaṃ vīriyabalaṃ"):
        f"То, что есть {VIRIYA_LIST}",
    ("Yā sati anussati paṭissati sati saraṇatā dhāraṇatā apilāpanatā asammussanatā sati satindriyaṃ satibalaṃ "
     "sammāsati"): f"То, что есть {SATI_LIST}",
    ("Yā cittassa ṭhiti saṇṭhiti avaṭṭhiti avisāhāro avikkhepo avisāhaṭamānasatā samatho samādhindriyaṃ "
     "samādhibalaṃ sammāsamādhi"): f"То, что есть {SAMADHI_LIST}",
    "Yā paññā pajānanā…pe… amoho dhammavicayo sammādiṭṭhi": f"То, что есть {WISDOM_SHORT}",
}
for _x, _r in UNKNOWN_X.items():
    BODY5[f"Yā tesaṃ dhammānaṃ {_x} sacchikiriyāya paññā pajānanā…pe… amoho dhammavicayo sammādiṭṭhi "
          "dhammavicayasambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ"] = UNKNOWN_HEAD.format(x=_r)
for _k in ("sukha", "dukkha", "somanassa", "domanassa", "upekkhā"):
    _p = next(p for p, (r, c) in BODY.items() if r == f"То, что есть {K23.FEELING_P1[_k]}")
    BODY5[_p] = f"То, что есть {K23.FEELING_P1[_k]}"

ANSWER5_RX = re.compile(r'^(.*?) – idaṃ vuccati ("?)(\S+)\2\.$')
VIDHA_RX = re.compile(r"^(\S+?)[vb]idhena manindriyaṃ – (.*)$")
EVAM_RX = re.compile(r"^([Ee])vaṃ (\S+?)[vb]idhena manindriyaṃ$")
MANA = IND["mana"]


def vidha_sentence(s):
    """one sentence of the manindriya classification (K1.chain for the body)"""
    m = VIDHA_RX.match(s)
    if m:
        nw, body = m.groups()
        body = re.sub(r"^phassasampayuttaṃ\.", "phassasampayutto.", body)   # neuter of the K1 item key (as K23)
        return f"{cap(MANA)} {K1.NUMW[K1.NUMP[nw.lower()]]} – {K1.chain(body)}"
    parts = s[:-1].split("…pe… ")
    out = []
    for p in parts:
        me = EVAM_RX.match(p)
        assert me, s
        t = f"Такова {MANA} {K1.NUMW[K1.NUMP[me.group(2).lower()]]}"
        out.append(t if me.group(1) == "E" else low(t))
    return "… ".join(out) + "."


def sent5(s):
    if s in SENT4:
        return SENT4[s]
    m = re.match(r"^Tattha katamaṃ (\S+)\?$", s)
    if m:
        return q(IND[IND_P[m.group(1)]])
    if s.startswith("Tattha katamaṃ sotindriyaṃ…pe…"):
        names = re.findall(r"(\w+indriyaṃ)", s)
        return q("… ".join(IND[IND_P[n]] for n in names))
    if re.match(r"^\S+?[vb]idhena manindriyaṃ – ", s) or re.match(r"^[Ee]vaṃ \S+?[vb]idhena manindriyaṃ", s):
        return vidha_sentence(s)
    if s == "Jīvitindriyaṃ duvidhena – atthi rūpajīvitindriyaṃ, atthi arūpajīvitindriyaṃ.":
        return (f"{cap(IND['jīvita'])} {K1.NUMW[2]} – есть {IND['rūpajīvita']}, есть {IND['arūpajīvita']}.")
    m = re.match(r'^Idaṃ vuccati "(\S+)"\.$', s)
    if m:
        return f"Это называется «{iins(IND_P[m.group(1)])}»."
    m = ANSWER5_RX.match(s)
    if m:
        body, qt, term = m.groups()
        k = IND_P[term]
        if term == "arūpajīvatindriyaṃ":
            slip("^2-220 «idaṃ vuccati \"arūpajīvatindriyaṃ\"» (jīvata for jīvita): rendered as meant "
                 "«нематериальной жизненной способностью»")
        pm = re.match(r"^Y(?:aṃ|o) (cakkhu|kāyo) catunnaṃ mahābhūtānaṃ upādāya pasādo…pe… suñño gāmopeso$", body)
        if pm:
            ru = K23.dh_pe("cakkhu" if pm.group(1) == "cakkhu" else "kāya")
        else:
            ru = BODY5[body]
        if "thāmo ṭhiti" in body:
            slip("^2-220 vīriyindriya list «thāmo ṭhiti» (pi-1 ^1-22 «thāmo dhiti»): ṭhiti translated as written "
                 "(«устойчивость», pi-1 «твёрдость»)")
        if term == "aññātāvindriyaṃ":
            slip("^2-220 «Yā tesaṃ dhammānaṃ aññātāvīnaṃ diṭṭhānaṃ …» (pi-1 ^1-555 «tesaṃ aññātāvīnaṃ dhammānaṃ "
                 "aññā paññā …»): pi-2 wording translated as written, «которые познаны окончательным знанием, "
                 "увидены, …» (unsure)")
        if not qt:
            return f"{ru}, – {called(iins(k), quoted=False)}"
        return f"{ru}, – {called(iins(k))}"
    raise KeyError(s)


def line5(ln):
    return " ".join(sent5(s) for s in split_sents(ln))


# =========================================================================== Pañhāpucchaka (K23 engine, tables extended here)
SUBJ45 = {}   # Pāli subject -> (Russian nominative, number s/p, gender f/p, accusative)
for _p, _r in (("Samudayasaccaṃ", "Истина о возникновении"), ("Maggasaccaṃ", "Истина о пути"),
               ("Nirodhasaccaṃ", "Истина о прекращении"), ("Dukkhasaccaṃ", "Истина о страдании")):
    SUBJ45[_p] = (_r, "s", "f", _r.replace("Истина", "Истину", 1))
SUBJ45["Dve saccā"] = ("Две истины", "p", "p", "Две истины")
SUBJ45["Tīṇi saccāni"] = ("Три истины", "p", "p", "Три истины")
for _p, _r in (("Dvindriyā", "Две способности"), ("Tīṇindriyā", "Три способности"),
               ("Cattārindriyā", "Четыре способности"), ("Pañcindriyā", "Пять способностей"),
               ("Cha indriyā", "Шесть способностей"), ("Sattindriyā", "Семь способностей"),
               ("Aṭṭhindriyā", "Восемь способностей"), ("Navindriyā", "Девять способностей"),
               ("Dasindriyā", "Десять способностей"), ("Ekādasindriyā", "Одиннадцать способностей"),
               ("Dvādasindriyā", "Двенадцать способностей"), ("Terasindriyā", "Тринадцать способностей"),
               ("Cuddasindriyā", "Четырнадцать способностей"), ("Pannarasindriyā", "Пятнадцать способностей"),
               ("Soḷasindriyā", "Шестнадцать способностей"), ("Sattarasindriyā", "Семнадцать способностей"),
               ("Aṭṭhārasindriyā", "Восемнадцать способностей")):
    SUBJ45[_p] = (_r, "p", "p", _r)
SUBJ45["Ekavīsatindriyā"] = ("Двадцать одна способность", "s", "f", "Двадцать одну способность")
for _p in ("Domanassindriyaṃ", "Jīvitindriyaṃ", "Anaññātaññassāmītindriyaṃ", "Aññindriyaṃ", "Aññātāvindriyaṃ",
           "Somanassindriyaṃ", "Upekkhindriyaṃ", "Manindriyaṃ"):
    _r = cap(IND[IND_P[low(_p)]])
    SUBJ45[_p] = (_r, "s", "f", _r.replace("Жизненная", "Жизненную"))
ALL = "@@"                          # subjectless sentences of ch. 5 («Sappaccayā.», «No āsavā.» …): all 22 faculties
SUBJ45[ALL] = (ALL, "p", "p", ALL)
GROUPS45 = {"Catunnaṃ ariyasaccānaṃ": "из четырёх благородных истин",
            "Bāvīsatīnaṃ indriyānaṃ": "из двадцати двух способностей"}

LOCAL45 = {
    "na appamāṇārammaṇo": dict(f="не являющаяся явлением с безмерным объектом",
                               pl="не являющиеся явлениями с безмерным объектом",
                               ins="не явлением с безмерным объектом", insp="не явлениями с безмерным объектом",
                               nins="не явлением с безмерным объектом",
                               v="не является явлением с безмерным объектом",
                               vp="не являются явлениями с безмерным объектом"),
    "na maggārammaṇo": K1.A("не имеющая объектом путь", v="не имеет объектом путь"),
    "na maggahetuko": K1.A("не имеющая корнем путь", v="не имеет корнем путь"),
}
PANHA_FIX45 = [  # typographic slips of the source, rendered as meant (reported)
    ('"upādānañceva upādānasampayuttañcā" tipi', '"upādānañceva upādānasampayuttañcā"tipi',
     '^2-218 «"upādānañceva upādānasampayuttañcā" tipi»: space before tipi (ignored)'),
    ('"kileso ceva kilesasampayuttañcā" tipi', '"kileso ceva kilesasampayuttañcā"tipi',
     '^2-218 «"kileso ceva kilesasampayuttañcā" tipi»: space before tipi (ignored)'),
    ('"mahaggatārammaṇa"nti pi', '"mahaggatārammaṇa"ntipi',
     '^2-223 «"mahaggatārammaṇa"nti pi» written apart (= ntipi)'),
    ('"gantho ceva ganthasampayutta"ñcāti', '"gantho ceva ganthasampayuttañcā"ti',
     '^2-224 «"gantho ceva ganthasampayutta"ñcāti»: closing quote misplaced (= "…sampayuttañcā"ti)'),
    ("Dve saccā nīvaraṇiyā dve saccā anīvaraṇiyā.", "Dve saccā nīvaraṇiyā. Dve saccā anīvaraṇiyā.",
     "^2-218 «Dve saccā nīvaraṇiyā dve saccā anīvaraṇiyā»: full stop missing (two sentences in Russian)"),
    ("siyā parittārammaṇaṃ siyā mahaggatārammaṇaṃ", "siyā parittārammaṇaṃ, siyā mahaggatārammaṇaṃ",
     "^2-223 «siyā parittārammaṇaṃ siyā mahaggatārammaṇaṃ»: comma missing (added)"),
    ("siyā araṇanti.", "siyā araṇaṃ.", None),                         # closing «…ti» of the section
    ("siyā mahaggatārammaṇaṃ na appamāṇārammaṇaṃ", "siyā mahaggatārammaṇaṃ, na appamāṇārammaṇaṃ", None),
    ("na maggārammaṇaṃ maggahetukaṃ", "na maggārammaṇaṃ, maggahetukaṃ", None),
    ("siyā maggārammaṇaṃ na maggahetukaṃ", "siyā maggārammaṇaṃ, na maggahetukaṃ", None),
]


def install():
    """extend the K23 engine tables in memory (the K23 file is never edited)"""
    K23.SUBJ.update(SUBJ45)
    K23.LOCAL.update(LOCAL45)
    for k in LOCAL45:
        K23.PLK.setdefault(K1.pali_plural(k), k)
    K23.PLK.setdefault("arūpāni", "arūpo")          # Tīṇi saccāni arūpāni (neuter plural)


def panha_sentence(sent, prev_num):
    """K23.sentence with subjectless sentences (ch. 5) and a second subject after a comma (^2-223)"""
    if not re.match(r"^(" + "|".join(sorted(SUBJ45, key=len, reverse=True)) + r") ", sent) and \
            not re.match(r"^(" + "|".join(sorted(K23.SUBJ, key=len, reverse=True)) + r") ", sent):
        r = K23.sentence(f"{ALL} {low(sent)}")
        assert r.startswith(ALL + " "), r
        return cap(r[len(ALL) + 1:])
    m = re.match(r"^(.*?), (aṭṭhindriyā) (siyā .*)$", sent)
    if m:
        slip("^2-223 «…, aṭṭhindriyā siyā …»: a new sentence joined by a comma (kept, subject in lower case)")
        a = K23.sentence(m.group(1))
        b = K23.sentence(f"Aṭṭhindriyā {m.group(3)}")
        return f"{a}, {low(b)}"
    return K23.sentence(sent)


def panha_line(p):
    p = p.replace('"ti pi', '"tipi')
    for bad, good, note in PANHA_FIX45 + K23.PANHA_FIX:
        if bad in p:
            p = p.replace(bad, good)
            if note:
                slip(note)
    sents = re.split(r"(?<=\.) (?=[A-Z])", p)
    out = []
    for s in sents:
        assert s.endswith("."), s
        out.append(panha_sentence(s[:-1], None) + ".")
    return " ".join(out)


def panha_question(p):
    return K1.panha_question(p, GROUPS45)


# =========================================================================== chapters
def heading(ln):
    lvl, text = ln.split(" ", 1)
    T = {"Saccavibhaṅgo": S.CH_TITLE[4][1], "Indriyavibhaṅgo": S.CH_TITLE[5][1],
         "Suttantabhājanīyaṃ": S.SUTTANTA_BH, "Abhidhammabhājanīyaṃ": S.ABHI_BH, "Pañhāpucchakaṃ": S.PANHA,
         "Tikaṃ": S.TIKA_H, "Dukaṃ": S.DUKA_H}
    T.update(SUB_H)
    return f"{lvl} {T[text]}"


def build(part, chapter):
    pali = (S.PALI / part).read_text(encoding="utf-8")
    h = {}
    section = None
    for sid, lines in S.segs(pali):
        lines = [re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", ln) for ln in lines]
        if lines[0].startswith("#"):
            assert len(lines) == 1
            text = lines[0].split(" ", 1)[1]
            if text in ("Suttantabhājanīyaṃ", "Abhidhammabhājanīyaṃ", "Pañhāpucchakaṃ"):
                section = text
            h[sid] = [heading(lines[0])]
            continue
        ru = []
        for ln in lines:
            if ln in SENT4:
                ru.append(SENT4[ln])
            elif ln.startswith("Cattāri ariyasaccāni – "):
                if "[" in ln:
                    ru.append(FOUR_NOBLE.format(v1=" " + FOUR_NOBLE_V[0], v2=" " + FOUR_NOBLE_V[1]))
                else:
                    ru.append(FOUR_NOBLE.format(v1="", v2=""))
            elif ln.startswith("Bāvīsatindriyāni – "):
                ru.append(IND22_LINE_V if "[" in ln else IND22_LINE)
            elif section == "Pañhāpucchakaṃ":
                ru.append(panha_question(ln) if ln.endswith("?") else panha_line(ln))
            elif chapter == 4:
                ru.append(line4(ln, "S" if section == "Suttantabhājanīyaṃ" else "A"))
            else:
                ru.append(line5(ln))
        h[sid] = ru
    return pali, h


# =========================================================================== notes
def notes_md():
    L = ["# pi-2 Russian rails: new formulas of chapters 4 and 5 (^2-189 … ^2-224)", "",
         "Generated by build_rails_4_5_ru.py; import it instead of retyping. Strings already in ru-rails-formulas.md "
         "(sample), notes-1.md or notes-2-3.md are not repeated.", "",
         "## Saccavibhaṅga: headings and names", "",
         f"##### Dukkhasaccaṃ / Samudayasaccaṃ / Nirodhasaccaṃ / Maggasaccaṃ = ##### " + " / ".join(SUB_H.values()),
         f"dukkhaṃ ariyasaccaṃ = {noble('dukkhaṃ')} (ins. {noble('dukkhaṃ', 'ins')})",
         f"dukkhasamudayaṃ ariyasaccaṃ = {noble('dukkhasamudayaṃ')}",
         f"dukkhanirodhaṃ ariyasaccaṃ = {noble('dukkhanirodhaṃ')}",
         f"dukkhanirodhagāminī paṭipadā ariyasaccaṃ = {noble('dukkhanirodhagāminī paṭipadā')}",
         f"Cattāri ariyasaccāni – … = {FOUR_NOBLE.format(v1='', v2='')}",
         f"Cattāri saccāni – dukkhaṃ, dukkhasamudayo, dukkhanirodho, dukkhanirodhagāminī paṭipadā. = {FOUR_TRUTHS}",
         "dukkhasamudayo / dukkhanirodho / dukkhanirodhagāminī paṭipadā = " + " / ".join(
             TRUTH[k] for k in ("dukkhasamudayo", "dukkhanirodho", "dukkhanirodhagāminī paṭipadā")),
         "", "## Saccavibhaṅga: Suttantabhājanīya", "",
         f"Jātipi dukkhā, … saṃkhittena pañcupādānakkhandhā dukkhā. = {DUKKHA_LIST}",
         f"pañcupādānakkhandhā = {FIVE_UPA}; rūpupādānakkhandho … = {UPADANA_KH['rūpa']}, {OBJ_CL} …",
         f"appiyehi sampayogo dukkho = {APPIYA}; piyehi vippayogo dukkho = {PIYA}",
         f"yampicchaṃ na labhati tampi dukkhaṃ = {YAMPI}; Tattha katamaṃ yampicchaṃ …? = Что значит здесь: {YAMPI}?; "
         f"Idampi \"yampicchaṃ …\". = Это тоже: «{YAMPI}».",
         f"saṃkhittena pañcupādānakkhandhā dukkhā (question) = {FIVE_UPA_DUKKHA}",
         f"tesaṃ tesaṃ sattānaṃ tamhi tamhi sattanikāye = {BEINGS_CLASS}",
         f"jāti sañjāti okkanti abhinibbatti khandhānaṃ pātubhāvo āyatanānaṃ paṭilābho = {JATI_LIST}",
         f"jarā jīraṇatā … indriyānaṃ paripāko = {JARA_P1} (pi-1 ^1-643)",
         f"tamhā tamhā sattanikāyā cuti cavanatā … jīvitindriyassupacchedo = {MARANA_LIST}",
         f"Ñātibyasanena vā phuṭṭhassa … aññataraññatarena dukkhadhammena phuṭṭhassa = {STRUCK} …",
         f"soko socanā … sokasallaṃ = {SOKA_LIST}", f"ādevo paridevo … lālappitattaṃ = {PARIDEVA_LIST}",
         f"āyāso upāyāso āyāsitattaṃ upāyāsitattaṃ = {UPAYASA_LIST}",
         f"Idha yassa te honti aniṭṭhā … missībhāvo = {UNWANTED}", f"Idha yassa te honti iṭṭhā … amissībhāvo = {WANTED}",
         f"X-dhammānaṃ sattānaṃ evaṃ icchā uppajjati – \"aho vata …\"ti! = {cap(SUBJECT_TO)} X(dat), "
         + WISH.format(a="X(dat)", b="приходило X"),
         f"Na kho panetaṃ icchāya pattabbaṃ. = {SENT4['Na kho panetaṃ icchāya pattabbaṃ.']}",
         f"Ime vuccanti \"saṃkhittena pañcupādānakkhandhā dukkhā\". = Это называется «{FIVE_UPA_DUKKHA_INS}».",
         f"Yāyaṃ taṇhā ponobhavikā … vibhavataṇhā. = {SENT4[[k for k in SENT4 if k.startswith('Yāyaṃ taṇhā')][0]]}",
         f"Sā kho panesā taṇhā kattha uppajjamānā uppajjati, kattha nivisamānā nivisati? = "
         f"{SENT4['Sā kho panesā taṇhā kattha uppajjamānā uppajjati, kattha nivisamānā nivisati?']}",
         f"Etthesā taṇhā uppajjamānā uppajjati, ettha nivisamānā nivisati. = {ARISE}",
         f"Etthesā taṇhā pahīyamānā pahīyati, ettha nirujjhamānā nirujjhati. = {CEASE}",
         f"Kiñca loke piyarūpaṃ sātarūpaṃ? = {WHAT_DEAR}",
         f"X loke piyarūpaṃ sātarūpaṃ. = X в мире {DEAR['m']} / {DEAR['n']} / {DEAR['f']} / {DEAR['p']}.",
         "Rūpasaññā / Rūpasañcetanā / Rūpataṇhā / Rūpavitakko / Rūpavicāro = " + " / ".join(
             fn("rūpa") for fn, _ in SER.values()),
         f"Yo tassāyeva taṇhāya asesavirāganirodho … anālayo. = "
         f"{SENT4['Yo tassāyeva taṇhāya asesavirāganirodho cāgo paṭinissaggo mutti anālayo.']}",
         f"Ayameva ariyo aṭṭhaṅgiko maggo, seyyathidaṃ – … = "
         f"{SENT4[[k for k in SENT4 if k.startswith('Ayameva')][0]]}",
         f"chandaṃ janeti, vāyamati, vīriyaṃ ārabhati, cittaṃ paggaṇhāti, padahati = {EFFORT}",
         f"kāye kāyānupassī viharati ātāpī sampajāno satimā, vineyya loke abhijjhādomanassaṃ = пребывает, в теле "
         f"созерцая тело, {CONTEMPL}",
         f"the four jhānas (Idha bhikkhu vivicceva kāmehi …) = pi-1 ^1-160/161/163/165 wording + «и пребывает в нём»; "
         f"ajjhattaṃ sampasādanaṃ = с внутренней ясностью (pi-1 «с ясностью внутри себя»)",
         "Musāvādā veramaṇī … / Pāṇātipātā veramaṇī … = Воздержание от лжи … / Воздержание от убийства живых существ … "
         "(precept names: veramaṇī «воздержание», APPROVED)",
         "", "## Saccavibhaṅga: Abhidhammabhājanīya", "",
         f"Idha bhikkhu yasmiṃ samaye lokuttaraṃ jhānaṃ bhāveti … tasmiṃ samaye = {SUPRA_HEAD}",
         "aṭṭhaṅgiko maggo hoti (–) sammādiṭṭhi…pe… sammāsamādhi = есть восьмичастный путь: (–) правильное "
         "воззрение… правильное сосредоточение",
         f"pañcaṅgiko maggo hoti – … = {SUPRA_TAIL[[k for k in SUPRA_TAIL if k.startswith('pañca')][0]]}",
         f"Avasesā dhammā dukkhanirodhagāminiyā paṭipadāya sampayuttā. = "
         f"{SENT4['Avasesā dhammā dukkhanirodhagāminiyā paṭipadāya sampayuttā.']}",
         "list members (nominative): " + "; ".join(f"{k} = {v}" for k, v in SAM_NOM.items()),
         "list members (genitive, before pahānaṃ «Устранение»): " + "; ".join(f"{k} = {v}" for k, v in NIR_GEN.items()),
         f"Yā micchā ājīvā ārati … = То, что есть отстранение от ложного образа жизни, … (pi-1 «неправильного»)",
         f"[veramaṇi (ka.) evamuparipi] = {VERAMANI_VAR.strip()}",
         "", "## Indriyavibhaṅga", "",
         f"Bāvīsatindriyāni – … = {IND22_LINE}",
         "Tattha katamaṃ Xindriyaṃ? = Что такое здесь способность X?  |  idaṃ vuccati \"Xindriyaṃ\" = это называется "
         "«способностью X»",
         f"<N>vidhena manindriyaṃ – = {cap(MANA)} <N> –   |   Evaṃ <N>vidhena manindriyaṃ. = Такова {MANA} <N>.",
         f"Jīvitindriyaṃ duvidhena – atthi rūpajīvitindriyaṃ, atthi arūpajīvitindriyaṃ. = "
         f"{cap(IND['jīvita'])} {K1.NUMW[2]} – есть {IND['rūpajīvita']}, есть {IND['arūpajīvita']}.",
         f"Yā tesaṃ dhammānaṃ aññātāvīnaṃ diṭṭhānaṃ … = {UNKNOWN_HEAD.format(x=UNKNOWN_X[list(UNKNOWN_X)[2]])}",
         f"Bāvīsatīnaṃ indriyānaṃ kati …? = Сколько {GROUPS45['Bāvīsatīnaṃ indriyānaṃ']} являются …?",
         f"Catunnaṃ ariyasaccānaṃ kati …? = Сколько {GROUPS45['Catunnaṃ ariyasaccānaṃ']} являются …?",
         "question-section subjects: " + "; ".join(f"{k} = {v[0]}" for k, v in SUBJ45.items() if k != ALL),
         "subjectless sentences (Sappaccayā. / No āsavā. …) = the plural predicate alone: «Имеют условия.», "
         "«Не являются влечениями.»",
         "na appamāṇārammaṇaṃ / na maggārammaṇaṃ / na maggahetukaṃ = не является явлением с безмерным объектом / не "
         "имеет объектом путь / не имеет корнем путь",
         ]
    return "\n".join(L) + "\n"


def main():
    check_pi1()
    install()
    for part, ch in (("4-saccavibhango.md", 4), ("5-indriyavibhango.md", 5)):
        pali, h = build(part, ch)
        (S.OUT / part).write_text(K23.render(pali, h), encoding="utf-8", newline="\n")
        print(f"wrote {part}: {len(S.segs(pali))} segments")
    NOTES_PATH.write_text(notes_md(), encoding="utf-8", newline="\n")
    for s in SLIPS:
        print("slip:", s)
    for s in K23.SLIPS:
        print("engine note:", s)


if __name__ == "__main__":
    main()
