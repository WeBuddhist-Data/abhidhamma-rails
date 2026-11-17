"""Builder for the Russian rails translation of pi-2 (Vibhaṅga, plain audience), chapter 6
(Paṭiccasamuppādavibhaṅgo, dependent origination, ^2-6-0 … ^2-354).

Writes (only when run as a script):
  AI_translation/russian/pi-2-russian-plain-rails_split_chapters/6-paticcasamuppadavibhango.md
  0-INBOX/temp/pipeline/pi-2-ru/rails/notes-6.md   (new recurring formulas, Pāli = Russian)

Every Russian string comes from the fixed tables and functions below, so identical Pāli gives identical Russian.
Imported read-only: the approved sample builder (S), the chapter-1 builder (K1), the chapters 2-3 builder (K23: q(),
sense-base names, the pi-1 feeling / citta / dosa lists, render()) and the chapters 4-5 builder (K45: the Suttanta
definitions of birth, ageing, death, sorrow, lamentation, despair, the wisdom lists). Passages shared with the
Dhammasaṅgaṇī take their Russian from the approved pi-1 rails; check_pi1() asserts that they occur there.

The dependent-origination chain follows the approved pi-1 wording of ^1-1343 («Неведением обусловлены формирующие
факторы, формирующими факторами обусловлено сознание, …»): a clause «Xpaccayā Y» is «X(ins) обусловлен(а/о/ы) Y»;
as a named term (questions, «это называется …») it is «Y, обусловленный X(ins)». saṅkhārapaccayā is plural
(«формирующими факторами») in the Suttanta method, where the text has saṅkhārā, and singular («формирующим
фактором», termbase) in the Abhidhamma method, where the text has saṅkhāro.

usage: python -I -X utf8 build_rails_6_ru.py
"""
import pathlib
import re
import sys

RAILS = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-ru\rails")
sys.path.insert(0, str(RAILS))
import build_rails_sample_ru as S  # noqa: E402  (importing writes nothing)
import build_rails_1_ru as K1      # noqa: E402  (importing writes nothing)
import build_rails_2_3_ru as K23   # noqa: E402  (importing writes nothing)
import build_rails_4_5_ru as K45   # noqa: E402  (importing writes nothing)

PART = "6-paticcasamuppadavibhango.md"
NOTES_PATH = RAILS / "notes-6.md"
cap = S.cap
SLIPS = []


def slip(msg):
    if msg not in SLIPS:
        SLIPS.append(msg)


def low(s):
    return s[:1].lower() + s[1:]


# =========================================================================== nouns of the chain
# key -> (nominative, instrumental, accusative, gender m/f/n/p)
N = {
    "avijjā": ("неведение", "неведением", "неведение", "n"),
    "saṅkhāro": ("формирующий фактор", "формирующим фактором", "формирующий фактор", "m"),
    "saṅkhārā": ("формирующие факторы", "формирующими факторами", "формирующие факторы", "p"),
    "viññāṇaṃ": ("сознание", "сознанием", "сознание", "n"),
    "nāmaṃ": ("умственное", "умственным", "умственное", "n"),
    "nāmarūpaṃ": ("умственное и материальная форма", "умственным и материальной формой",
                  "умственное и материальную форму", "p"),
    "chaṭṭhāyatanaṃ": ("шестая сфера восприятия", "шестой сферой восприятия", "шестую сферу восприятия", "f"),
    "saḷāyatanaṃ": ("шесть сфер восприятия", "шестью сферами восприятия", "шесть сфер восприятия", "p"),
    "phasso": ("контакт", "контактом", "контакт", "m"),
    "vedanā": ("чувство", "чувством", "чувство", "n"),
    "taṇhā": ("жажда", "жаждой", "жажду", "f"),
    "upādānaṃ": ("цепляние", "цеплянием", "цепляние", "n"),
    "bhavo": ("существование", "существованием", "существование", "n"),
    "jāti": ("рождение", "рождением", "рождение", "n"),
    "jarāmaraṇaṃ": ("старение и смерть", "старением и смертью", "старение и смерть", "p"),
    "adhimokkho": ("решимость", "решимостью", "решимость", "f"),          # no termbase entry (style file: решимость)
    "pasādo": ("ясная вера", "ясной верой", "ясную веру", "f"),
    "paṭighaṃ": ("неприязнь", "неприязнью", "неприязнь", "f"),
    "vicikicchā": ("колебание", "колебанием", "колебание", "n"),
    "uddhaccaṃ": ("беспокойство", "беспокойством", "беспокойство", "n"),
    "kusalamūlā": ("благие корни", "благими корнями", "благие корни", "p"),
    "akusalamūlā": ("неблагие корни", "неблагими корнями", "неблагие корни", "p"),
}
STEM = {  # compound stem (X-paccayā, X-hetuko, X-sampayutto) -> noun key
    "avijjā": "avijjā", "saṅkhāra": "saṅkhāro", "viññāṇa": "viññāṇaṃ", "nāma": "nāmaṃ", "nāmarūpa": "nāmarūpaṃ",
    "chaṭṭhāyatana": "chaṭṭhāyatanaṃ", "saḷāyatana": "saḷāyatanaṃ", "phassa": "phasso", "vedanā": "vedanā",
    "taṇhā": "taṇhā", "upādāna": "upādānaṃ", "bhava": "bhavo", "jāti": "jāti", "adhimokkha": "adhimokkho",
    "pasāda": "pasādo", "paṭigha": "paṭighaṃ", "vicikicchā": "vicikicchā", "uddhacca": "uddhaccaṃ",
    "kusalamūla": "kusalamūlā", "akusalamūla": "akusalamūlā",
}
COND_SHORT = {"m": "обусловлен", "f": "обусловлена", "n": "обусловлено", "p": "обусловлены"}
COND_NOM = {"m": "обусловленный", "f": "обусловленная", "n": "обусловленное", "p": "обусловленные"}
COND_INS = {"m": "обусловленным", "f": "обусловленной", "n": "обусловленным", "p": "обусловленными"}
HAV_NOM = {"m": "имеющий", "f": "имеющая", "n": "имеющее", "p": "имеющие"}
HAV_INS = {"m": "имеющим", "f": "имеющей", "n": "имеющим", "p": "имеющими"}
CON_NOM = {"m": "связанный", "f": "связанная", "n": "связанное", "p": "связанные"}
CON_INS = {"m": "связанным", "f": "связанной", "n": "связанным", "p": "связанными"}
CON_SHORT = {"m": "связан", "f": "связана", "n": "связано", "p": "связаны"}
CAUSE = "причиной"        # hetuko «имеющий причиной» (termbase, dependent-origination tetrads)
ALSO = "тоже"             # -paccayāpi (Aññamaññacatukka)
AND_ALSO = "а"            # «…, а формирующим фактором тоже обусловлено неведение» (avoids «и умственным и …»)
WHEREBY = "причём"        # «nāmarūpaṃ viññāṇasampayuttaṃ nāmaṃ»: the second noun names the part that is conjoined

CLAUSE_RX = re.compile(r"^(?P<c>\S+?)paccayā(?P<pi>pi)? (?P<r>\S+)"
                       r"(?: (?P<m>\S+?)(?P<mk>hetuk|sampayutt)(?:o|ā|aṃ))?(?: (?P<w>nāmaṃ|chaṭṭhāyatanaṃ))?$")


def noun(key, suttanta=False):
    if suttanta and key == "saṅkhāro":
        key = "saṅkhārā"
    return N[key]


def parse(t, suttanta=False):
    """«Xpaccayā[pi] Y [Zhetuko|Zsampayutto] [W]» -> dict"""
    m = CLAUSE_RX.match(t)
    assert m, t
    c = STEM[low(m.group("c"))]
    d = dict(c=noun(c, suttanta), r=N[m.group("r")], pi=bool(m.group("pi")),
             mk=m.group("mk"), z=N[STEM[m.group("m")]] if m.group("m") else None, w=m.group("w"))
    return d


def clause(t, suttanta=False):
    """chain clause: «неведением обусловлен формирующий фактор[, имеющий причиной неведение]»;
    -paccayāpi: «формирующим фактором тоже обусловлено неведение» (chain() adds «и»)"""
    d = parse(t, suttanta)
    cn, ci, ca, cg = d["c"]
    rn, ri, ra, rg = d["r"]
    if d["pi"]:
        return f"{ci} {ALSO} {COND_SHORT[rg]} {rn}"
    out = f"{ci} {COND_SHORT[rg]} {rn}"
    if d["w"]:
        wn, wi, wa, wg = N[d["w"]]
        return f"{out}, {WHEREBY} {wn} {CON_SHORT[wg]} с {d['z'][1]}"
    if d["mk"] == "hetuk":
        out += f", {HAV_NOM[rg]} {CAUSE} {d['z'][2]}"
    elif d["mk"] == "sampayutt":
        out += f", {CON_NOM[rg]} с {d['z'][1]}"
    return out


def term(t, case="nom", suttanta=False):
    """named term: «формирующий фактор, обусловленный неведением [и имеющий причиной неведение]»"""
    t = t.strip()
    if t in SIMPLE:
        return SIMPLE[t][0 if case == "nom" else 1]
    d = parse(t, suttanta)
    cn, ci, ca, cg = d["c"]
    rn, ri, ra, rg = d["r"]
    head = rn if case == "nom" else ri
    part = (COND_NOM if case == "nom" else COND_INS)[rg]
    if d["pi"]:
        return f"{head}, {ALSO} {part} {ci}"
    out = f"{head}, {part} {ci}"
    if d["w"]:
        wn, wi, wa, wg = N[d["w"]]
        return f"{out}, {WHEREBY} {wn} {CON_SHORT[wg]} с {d['z'][1]}"
    if d["mk"] == "hetuk":
        out += f" и {(HAV_NOM if case == 'nom' else HAV_INS)[rg]} {CAUSE} {d['z'][2]}"
    elif d["mk"] == "sampayutt":
        out += f" и {(CON_NOM if case == 'nom' else CON_INS)[rg]} с {d['z'][1]}"
    return out


# =========================================================================== simple named terms (nominative, instrumental)
PUNNA = "волевое действие, приносящее заслугу"              # Puññābhisaṅkhāro (termbase)
APUNNA = "волевое действие, не приносящее заслуги"          # apuññābhisaṅkhāro (termbase)
ANENJA = "волевое действие, ведущее к непоколебимому"       # āneñjābhisaṅkhāro (termbase)
SIMPLE = {
    "avijjā": ("неведение", "неведением"), "saṅkhāro": ("формирующий фактор", "формирующим фактором"),
    "nāmaṃ": ("умственное", "умственным"), "rūpaṃ": ("материальная форма", "материальной формой"),
    "nāmarūpaṃ": ("умственное и материальная форма", "умственным и материальной формой"),
    "jarā": ("старение", "старением"), "maraṇaṃ": ("смерть", "смертью"), "soko": ("печаль", "печалью"),
    "paridevo": ("стенания", "стенаниями"), "dukkhaṃ": ("боль", "болью"), "domanassaṃ": ("уныние", "унынием"),
    "upāyāso": ("отчаяние", "отчаянием"),
    "kammabhavo": ("существование как действие", "существованием как действием"),
    "upapattibhavo": ("существование как перерождение", "существованием как перерождением"),
    "puññābhisaṅkhāro": (PUNNA, "волевым действием, приносящим заслугу"),
    "apuññābhisaṅkhāro": (APUNNA, "волевым действием, не приносящим заслуги"),
    "āneñjābhisaṅkhāro": (ANENJA, "волевым действием, ведущим к непоколебимому"),
    "kāyasaṅkhāro": ("телесный формирующий фактор", "телесным формирующим фактором"),
    "alobho": ("отсутствие жадности", "отсутствием жадности"), "adoso": ("отсутствие злобы", "отсутствием злобы"),
    "amoho": ("отсутствие заблуждения", "отсутствием заблуждения"),
    "kusalamūlā": ("благие корни", "благими корнями"),
}

# =========================================================================== fixed strings
EVAM = "Так происходит возникновение всей этой совокупности страдания"     # pi-1 ^1-1343 (lower case there)
EVAM_DH = "Так происходит возникновение этих явлений"                     # Evametesaṃ dhammānaṃ samudayo hoti
EVAM_MEANS = ("так происходит сочетание всей этой совокупности страдания, происходит схождение, происходит "
              "соединение, происходит проявление")
EVAM_DH_MEANS = "так происходит сочетание этих явлений, происходит схождение, происходит соединение, происходит проявление"
# saṅgati «сочетание», samodhānaṃ «соединение», pātubhāvo «проявление» (termbase); samāgamo: termbase «общение»
# (meeting with persons) does not fit the mass of suffering: «схождение» (reported)
TENA = "Поэтому это называется:"                                         # Tena vuccati "…"ti (vuccati «называться»)
AT_TIME = "в это время"                                                   # tasmiṃ samaye (pi-1)
ITI_NR = "Итак, это умственное и эта материальная форма."                 # Iti idañca nāmaṃ, idañca rūpaṃ. (pi-1 ^1-1163 «Итак, …»)
ITI_JM = "Итак, это старение и эта смерть."                               # Iti ayañca jarā, idañca maraṇaṃ.
ITI_BH = "Итак, это существование как действие и это существование как перерождение."
ATTHI_NR = "Есть умственное, есть материальная форма."                    # Atthi nāmaṃ, atthi rūpaṃ.
ATTHI_JM = "Есть старение, есть смерть."                                  # Atthi jarā, atthi maraṇaṃ.
BHAVA2 = (f"Существование {K1.NUMW[2]} – есть существование как действие, есть существование как перерождение.")
ALL_KAMMA = "Всякое действие, ведущее к существованию, тоже является существованием как действием."
KAYA3 = ("Телесное проявление намерения является телесным формирующим фактором, речевое проявление намерения является "
         "речевым формирующим фактором, умственное проявление намерения является формирующим фактором ума.")
SANKHARA6 = (f"{cap(PUNNA)}; {APUNNA}; {ANENJA}; телесный формирующий фактор; речевой формирующий фактор и "
             "формирующий фактор ума.")
ROOTS3 = "Отсутствие жадности, отсутствие злобы и отсутствие заблуждения"
ROOTS2 = "Отсутствие жадности и отсутствие злобы"

SENT = {  # Pāli sentence (without the final punctuation handled by the caller) -> Russian
    "Atthi nāmaṃ, atthi rūpaṃ.": ATTHI_NR,
    "Atthi jarā, atthi maraṇaṃ.": ATTHI_JM,
    "Iti idañca nāmaṃ, idañca rūpaṃ.": ITI_NR,
    "Iti ayañca jarā, idañca maraṇaṃ.": ITI_JM,
    "Iti ayañca kammabhavo, ayañca upapattibhavo.": ITI_BH,
    "Bhavo duvidhena – atthi kammabhavo, atthi upapattibhavo.": BHAVA2,
    "Sabbampi bhavagāmikammaṃ kammabhavo.": ALL_KAMMA,
    "Kāyasañcetanā kāyasaṅkhāro, vacīsañcetanā vacīsaṅkhāro, manosañcetanā cittasaṅkhāro.": KAYA3,
    ("Puññābhisaṅkhāro, apuññābhisaṅkhāro, āneñjābhisaṅkhāro, kāyasaṅkhāro, vacīsaṅkhāro, cittasaṅkhāro."): SANKHARA6,
    "Alobho, adoso, amoho.": ROOTS3 + ".",
    "Alobho, adoso.": ROOTS2 + ".",
    "Evametassa kevalassa dukkhakkhandhassa samudayo hoti.": EVAM + ".",
    "Evametesaṃ dhammānaṃ samudayo hoti.": EVAM_DH + ".",
    ("Evametassa kevalassa dukkhakkhandhassa samudayo hotīti, evametassa kevalassa dukkhakkhandhassa saṅgati hoti, "
     "samāgamo hoti, samodhānaṃ hoti, pātubhāvo hoti."): f"«{EVAM}»: {EVAM_MEANS}.",
    "Evametassa kevalassa dukkhakkhandhassa samudayo hotīti.": f"«{EVAM}».",
    ("Evametassa kevalassa dukkhakkhandhassa saṅgati hoti, samāgamo hoti, samodhānaṃ hoti, pātubhāvo hoti."):
        cap(EVAM_MEANS) + ".",
    "Evametesaṃ dhammānaṃ samudayo hotīti.": f"«{EVAM_DH}».",
    "Evametesaṃ dhammānaṃ saṅgati hoti, samāgamo hoti, samodhānaṃ hoti, pātubhāvo hoti.": cap(EVAM_DH_MEANS) + ".",
    "Suttantabhājanīyaṃ.": f"{S.SUTTANTA_BH}.",
    "Abhidhammabhājanīyaṃ.": f"{S.ABHI_BH}.",
    "Paṭiccasamuppādavibhaṅgo [paccayākāravibhaṅgo (sī. syā.)] niṭṭhito.":
        f"{S.CH_TITLE[6][1]} [вариант чтения (Sī., Syā.): paccayākāravibhaṅgo] {S.DONE}.",
}

# headings (##### X) and the closing labels (X.) of the sub-sections
SUBHEAD = {
    "Paccayacatukkaṃ": "Четвёрка условий", "Hetucatukkaṃ": "Четвёрка причин",
    "Sampayuttacatukkaṃ": "Четвёрка связанности", "Aññamaññacatukkaṃ": "Четвёрка взаимной обусловленности",
    "Mātikā": "Матрица", "Akusalaniddeso": "Разъяснение неблагого", "Kusalaniddeso": "Разъяснение благого",
    "Abyākataniddeso": "Разъяснение этически неопределённого",
    "Avijjāmūlakakusalaniddeso": "Разъяснение благого на основе неведения",
    "Kusalamūlakavipākaniddeso": "Разъяснение результатов на основе благих корней",
    "Akusalamūlakavipākaniddeso": "Разъяснение результатов на основе неблагих корней",
}
for _p, _r in SUBHEAD.items():
    SENT[f"{_p}."] = f"{_r}."

# =========================================================================== definitions (answer bodies)
CITTA_PE = "То, что есть ум, разум, умственная деятельность… соответствующий {x}"     # Yaṃ cittaṃ mano mānasaṃ…pe… tajjā<X>
CETANA = "То, что есть намерение, проявление намерения, состояние намеренности"        # pi-1 ^1-5 (cetanā sañcetanā …)
PHASSA = "То, что есть контакт, касание, соприкосновение, состояние соприкосновения"    # pi-1 ^1-2
RAGA7 = "страсть, пристрастие, расположенность, потакание, наслаждение, страсть к наслаждению, пристрастие ума"  # pi-1 ^1-1065
DITTHI16 = ("воззрение, приверженность воззрениям, дебри воззрений, пустыня воззрений, извращённость воззрений, "
            "метания воззрений, оковы воззрений, хватка, закрепление, убеждённость, искажение, кривая дорога, ложный "
            "путь, ложность, сфера сектантских учений, превратная хватка")                 # pi-1 ^1-392
ADHIMOKKHA = "То, что есть решимость ума, проявление решимости, состояние решимости в отношении этого"
SADDHA4 = "То, что есть вера, доверие, уверенность, глубокая убеждённость"              # pi-1 ^1-12 (first four)
UDDHACCA = "То, что есть беспокойство ума, отсутствие затихания, отвлечение ума, взбудораженность ума"  # pi-1 ^1-1165
VICIKICCHA = ("То, что есть сомнение, проявление сомнения, состояние сомнения, неуверенность, колебание, раздвоенность, "
              "распутье [вариант написания (Sī., Syā.): dvedhāpatho], нерешительность, неспособность прийти к "
              "определённости, блуждание, беспорядочное блуждание, отсутствие углубления [вариант написания (Sī., Syā., "
              "Ka.): apariyogāhanā], оцепенелость ума, терзание ума")                     # pi-1 ^1-425
ALOBHA = ("То, что есть отсутствие жадности, отсутствие проявления жадности, отсутствие состояния жадности, отсутствие "
          "пристрастия, отсутствие проявления пристрастия, отсутствие состояния пристрастия, отсутствие алчности, "
          "отсутствие жадности как благой корень")                                         # pi-1 ^1-1061
ADOSA = ("То, что есть отсутствие злобы, отсутствие проявления злобы, отсутствие состояния злобы, отсутствие "
         "недоброжелательности, отсутствие неприязни, отсутствие злобы как благой корень")  # pi-1 ^1-1075 without «…»
MOHA_PE = "То, что есть незнание, отсутствие видения… засов неведения, заблуждение как неблагой корень"  # pi-1 ^1-1318
NOT_KNOW4 = ("Незнание страдания, незнание возникновения страдания, незнание прекращения страдания, незнание способа "
             "практики, ведущего к прекращению страдания")                                 # pi-1 ^1-1067
EXCEPT = {"upādānaṃ": "цепляния", "phassaṃ": "контакта", "adhimokkhaṃ": "решимости", "vicikicchaṃ": "колебания",
          "vedanaṃ": "чувства"}                                                           # Ṭhapetvā X «Кроме X(gen)»
KH4 = "совокупность чувств, совокупность восприятия, совокупность формирующих факторов и совокупность сознания"
KH3_SNV = "совокупность восприятия, совокупность формирующих факторов и совокупность сознания"
NAMA3 = "Совокупность чувств, совокупность восприятия и совокупность формирующих факторов"
UPACAYA5 = ("Рост сферы глаза, рост сферы уха, рост сферы носа, рост сферы языка, рост сферы тела или же какая бы "
            "другая материальная форма ни была рождённой умом, имеющей причиной ум, порождённой умом")  # pi-1 ^1-641, ^1-666
DEPENDS = "та материальная форма, в зависимости от которой действует элемент умственного сознания"
DH_OF = "у тех или иных явлений"                                                          # tesaṃ tesaṃ dhammānaṃ
PARIDEVA = K45.PARIDEVA_LIST.split(" [", 1)[0]       # ch. 4 list without the ch. 4 variant bracket
MARANA_V = K45.MARANA_LIST.replace("кончина", "кончина [вариант написания (Ka.): kālaṃkiriyā]")
BHAVA9 = ("Существование в мире чувственных желаний, существование в мире форм, существование в мире без форм, "
          "существование с восприятием, существование без восприятия, существование ни с восприятием, ни без "
          "восприятия, существование с одной составляющей, существование с четырьмя составляющими и существование с "
          "пятью составляющими")

BODY = {  # Pāli answer body -> (Russian, comma before the dash)
    "Dukkhe aññāṇaṃ, dukkhasamudaye aññāṇaṃ, dukkhanirodhe aññāṇaṃ, dukkhanirodhagāminiyā paṭipadāya aññāṇaṃ":
        (NOT_KNOW4, True),
    "Kusalā cetanā kāmāvacarā rūpāvacarā dānamayā sīlamayā bhāvanāmayā":
        ("Благое намерение, относящееся к миру чувственных желаний, относящееся к миру форм, основанное на даянии, "
         "основанное на нравственности, основанное на развитии ума", True),
    "Akusalā cetanā kāmāvacarā": ("Неблагое намерение, относящееся к миру чувственных желаний", True),
    "Kusalā cetanā arūpāvacarā": ("Благое намерение, относящееся к миру без форм", True),
    "Cakkhuviññāṇaṃ, sotaviññāṇaṃ, ghānaviññāṇaṃ, jivhāviññāṇaṃ, kāyaviññāṇaṃ, manoviññāṇaṃ": (cap(S.VINNANA6), False),
    "Vedanākkhandho, saññākkhandho, saṅkhārakkhandho": (NAMA3, False),
    "Vedanākkhandho, saññākkhandho, saṅkhārakkhandho, viññāṇakkhandho": (cap(KH4), False),
    "Cattāro mahābhūtā, catunnañca mahābhūtānaṃ upādāya rūpaṃ": (cap(S.MAHABHUTA), True),
    "Cakkhāyatanaṃ, sotāyatanaṃ, ghānāyatanaṃ, jivhāyatanaṃ, kāyāyatanaṃ, manāyatanaṃ":
        (cap(K23.nlist([K23.AY[k] for k in ("cakkhu", "sota", "ghāna", "jivhā", "kāya", "mana")])), False),
    "Cakkhusamphasso sotasamphasso ghānasamphasso jivhāsamphasso kāyasamphasso manosamphasso":
        (cap(K23.nlist([f"контакт {s}" for s in S.SENSES])), False),
    ("Cakkhusamphassajā vedanā, sotasamphassajā vedanā, ghānasamphassajā vedanā, jivhāsamphassajā vedanā, "
     "kāyasamphassajā vedanā, manosamphassajā vedanā"): (cap(S.contact_list("чувство")), False),
    "Rūpataṇhā, saddataṇhā, gandhataṇhā, rasataṇhā, phoṭṭhabbataṇhā, dhammataṇhā":
        (cap(K23.nlist([f"жажда {K45.OBJ_GEN[o]}" for o in ("rūpa", "sadda", "gandha", "rasa", "phoṭṭhabba",
                                                             "dhamma")])), False),
    "Kāmupādānaṃ, diṭṭhupādānaṃ, sīlabbatupādānaṃ, attavādupādānaṃ":
        ("Цепляние за чувственные удовольствия, цепляние за воззрения, цепляние за обряды и обеты и цепляние за "
         "учение о самости", False),
    "Puññābhisaṅkhāro, apuññābhisaṅkhāro, āneñjābhisaṅkhāro": (f"{cap(PUNNA)}; {APUNNA}; {ANENJA}", True),
    ("Kāmabhavo, rūpabhavo, arūpabhavo, saññābhavo, asaññābhavo, nevasaññānāsaññābhavo, ekavokārabhavo, "
     "catuvokārabhavo, pañcavokārabhavo"): (BHAVA9, False),
    ("Yā tesaṃ tesaṃ sattānaṃ tamhi tamhi sattanikāye jāti sañjāti okkanti abhinibbatti, khandhānaṃ pātubhāvo, "
     "āyatanānaṃ paṭilābho"): (f"То, что {K45.BEINGS_CLASS} есть {K45.JATI_LIST}", True),
    ("Yā tesaṃ tesaṃ sattānaṃ tamhi tamhi sattanikāye jarā jīraṇatā khaṇḍiccaṃ pāliccaṃ valittacatā āyuno saṃhāni "
     "indriyānaṃ paripāko"): (f"То, что {K45.BEINGS_CLASS} есть {K45.JARA_P1}", True),
    ("Yā tesaṃ tesaṃ sattānaṃ tamhā tamhā sattanikāyā cuti cavanatā bhedo antaradhānaṃ maccu maraṇaṃ kālakiriyā "
     "[kālaṃkiriyā (ka.)] khandhānaṃ bhedo kaḷevarassa nikkhepo jīvitindriyassupacchedo"):
        (f"То, что {S.BEINGS} есть {MARANA_V}", True),
    ("Yaṃ kāyikaṃ asātaṃ kāyikaṃ dukkhaṃ kāyasamphassajaṃ asātaṃ dukkhaṃ vedayitaṃ kāyasamphassajā asātā dukkhā "
     "vedanā"): (f"То, что есть {K23.FEELING_P1['dukkha']}", True),
    ("Yaṃ cetasikaṃ asātaṃ, cetasikaṃ dukkhaṃ, cetosamphassajaṃ asātaṃ dukkhaṃ vedayitaṃ, cetosamphassajā asātā "
     "dukkhā vedanā"): (f"То, что есть {K23.FEELING_P1['domanassa']}", True),
    ("Yaṃ cetasikaṃ asātaṃ cetasikaṃ dukkhaṃ cetosamphassajaṃ asātaṃ dukkhaṃ vedayitaṃ cetosamphassajā asātā dukkhā "
     "vedanā"): (f"То, что есть {K23.FEELING_P1['domanassa']}", True),
    ("Yaṃ cetasikaṃ sātaṃ cetasikaṃ sukhaṃ cetosamphassajaṃ sātaṃ sukhaṃ vedayitaṃ cetosamphassajā sātā sukhā "
     "vedanā"): (f"То, что есть {K23.FEELING_P1['somanassa']}", True),
    ("Yaṃ cetasikaṃ neva sātaṃ nāsātaṃ cetosamphassajaṃ adukkhamasukhaṃ vedayitaṃ cetosamphassajā adukkhamasukhā "
     "vedanā"): (f"То, что есть {K23.FEELING_P1['upekkhā']}", True),
    ("Yaṃ cetasikaṃ neva sātaṃ nāsātaṃ cetosamphassajaṃ adukkhamasukhaṃ vedayitaṃ, cetosamphassajā adukkhamasukhā "
     "vedanā"): (f"То, что есть {K23.FEELING_P1['upekkhā']}", True),
    ("Yaṃ kāyikaṃ sātaṃ kāyikaṃ sukhaṃ kāyasamphassajaṃ sātaṃ sukhaṃ vedayitaṃ kāyasamphassajā sātā sukhā vedanā"):
        (f"То, что есть {K23.FEELING_P1['sukha']}", True),
    # Abhidhamma
    "Yaṃ aññāṇaṃ adassanaṃ…pe… avijjālaṅgī moho akusalamūlaṃ": (MOHA_PE, True),
    "Yaṃ aññāṇaṃ adassanaṃ…pe… avijjālaṅgī moho akusamūlaṃ": (MOHA_PE, True),      # ^2-276 slip (akusa-)
    "Yā cetanā sañcetanā sañcetayitattaṃ": (CETANA, True),
    "Yā cetanā sañcetanā sañcetayitattaṃ [cetayitattaṃ (sī. ka.)]":
        (f"{CETANA} [вариант чтения (Sī., Ka.): cetayitattaṃ]", True),
    ("Yaṃ cittaṃ mano mānasaṃ hadayaṃ paṇḍaraṃ mano manāyatanaṃ manindriyaṃ viññāṇaṃ viññāṇakkhandho "
     "tajjāmanoviññāṇadhātu"): (f"То, что есть {K23.CITTA_SYN}, соответствующий элемент умственного сознания", True),
    "Yo phasso phusanā samphusanā samphusitattaṃ": (PHASSA, True),
    "Yo rāgo sārāgo anunayo anurodho nandī nandirāgo cittassa sārāgo": (f"То, что есть {RAGA7}", True),
    "Yo rāgo sārāgo…pe… cittassa sārāgo": ("То, что есть страсть, пристрастие… пристрастие ума", True),
    "Yo rāgo…pe… cittassa sārāgo": ("То, что есть страсть… пристрастие ума", True),
    ("Yā diṭṭhi diṭṭhigataṃ diṭṭhigahanaṃ diṭṭhikantāro diṭṭhivisūkāyikaṃ diṭṭhivipphanditaṃ diṭṭhisaṃyojanaṃ gāho "
     "patiṭṭhāho abhiniveso parāmāso kummaggo micchāpatho micchattaṃ titthāyatanaṃ vipariyāsaggāho "
     "[vipariyesaggāho (bahūsu)]"):
        (f"То, что есть {DITTHI16} [вариант написания (во многих изданиях): vipariyesaggāho]", True),
    "Yā diṭṭhi diṭṭhigataṃ…pe… titthāyatanaṃ vipariyāsaggāho":
        ("То, что есть воззрение, приверженность воззрениям… сфера сектантских учений, превратная хватка", True),
    "Yā tesaṃ tesaṃ dhammānaṃ jāti sañjāti nibbatti abhinibbatti pātubhāvo":
        (f"То, что {DH_OF} есть рождение, зарождение, образование, появление, проявление", True),
    "Yā tesaṃ tesaṃ dhammānaṃ jāti sañjāti nibbatti abhinibbati pātubhāvo":          # ^2-273 abhinibbati
        (f"То, что {DH_OF} есть рождение, зарождение, образование, появление, проявление", True),
    "Yā tesaṃ tesaṃ dhammānaṃ jarā jīraṇatā āyuno saṃhāni":
        (f"То, что {DH_OF} есть старение, одряхление, сокращение срока жизни", True),
    "Yo tesaṃ tesaṃ dhammānaṃ khayo vayo bhedo paribhedo aniccatā antaradhānaṃ":
        (f"То, что {DH_OF} есть уничтожение, угасание, распад, полный распад, непостоянство, исчезновение", True),
    ("Cakkhāyatanassa upacayo, sotāyatanassa upacayo, ghānāyatanassa upacayo, jivhāyatanassa upacayo, "
     "kāyāyatanassa upacayo, yaṃ vā panaññampi atthi rūpaṃ cittajaṃ cittahetukaṃ cittasamuṭṭhānaṃ"): (UPACAYA5, True),
    "Yaṃ rūpaṃ nissāya manoviññāṇadhātu vattati": (cap(DEPENDS), True),
    "Cattāro ca mahābhūtā, yañca rūpaṃ nissāya manoviññāṇadhātu vattati":
        (f"Четыре великих элемента и {DEPENDS}", True),
    "Yo cittassa adhimokkho adhimuccanā tadadhimuttatā": (ADHIMOKKHA, True),
    "Yā saddhā saddahanā okappanā abhippasādo": (SADDHA4, True),
    "Yaṃ cittassa uddhaccaṃ avūpasamo cetaso vikkhepo bhantattaṃ cittassa": (UDDHACCA, True),
    "Yo cittassa āghāto…pe… caṇḍikkaṃ asuropo [asulopo (syā.)] anattamanatā cittassa":
        ("То, что есть досада ума… свирепость, грубость [вариант написания (Syā.): asulopo], недовольство ума", True),
    ("Yā kaṅkhā kaṅkhāyanā kaṅkhāyitattaṃ vimati vicikicchā dveḷhakaṃ dvidhāpatho [dvedhāpatho (sī. syā.)] saṃsayo "
     "anekaṃsaggāho āsappanā parisappanā apariyogāhaṇā [apariyogāhanā (sī. syā. ka.)] chambhitattaṃ cittassa "
     "manovilekho"): (VICIKICCHA, True),
    ("Yo alobho alubbhanā alubbhitattaṃ asārāgo asārajjanā asārajjitattaṃ anabhijjhā alobho kusalamūlaṃ"):
        (ALOBHA, True),
    "Yo adoso adussanā adussitattaṃ abyāpādo abyāpajjo adoso kusalamūlaṃ": (ADOSA, True),
    "Yā paññā pajānanā…pe… amoho dhammavicayo sammādiṭṭhi": (f"То, что есть {K45.WISDOM_SHORT}", True),
    ("Yā paññā pajānanā…pe… amoho dhammavicayo sammādiṭṭhi dhammavicayasambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ"):
        (f"То, что есть {K45.WISDOM_PATH}", True),
    "Alobho, adoso, amoho": (ROOTS3, False),
    "Alobho, adoso": (ROOTS2, False),
}
for _x in EXCEPT:
    _rest = KH3_SNV if _x == "vedanaṃ" else KH4
    _p = ("saññākkhandho saṅkhārakkhandho viññāṇakkhandho" if _x == "vedanaṃ"
          else "vedanākkhandho saññākkhandho saṅkhārakkhandho viññāṇakkhandho")
    BODY[f"Ṭhapetvā {_x}, {_p}"] = (f"Кроме {EXCEPT[_x]}, {_rest}", False)
BODY["Ṭhapetvā adhimokkhaṃ, vedanākkhandho saññākkhandho saṅkhārakkhandho, viññāṇakkhandho"] = \
    (f"Кроме {EXCEPT['adhimokkhaṃ']}, {KH4}", False)                                     # ^2-318 extra comma
CITTA_PE_RX = re.compile(r"^Yaṃ cittaṃ mano mānasaṃ ?…pe… tajjā(\S+?)dhātu$")
TAJJA_DH = {"mano": K23.DH["mano"], "manoviññāṇa": K23.DH["manoviññāṇa"],
            "cakkhuviññāṇa": K23.DH["cakkhuviññāṇa"], "kāyaviññāṇa": K23.DH["kāyaviññāṇa"]}
STRUCK_P = ("Ñātibyasanena vā phuṭṭhassa, bhogabyasanena vā phuṭṭhassa, rogabyasanena vā phuṭṭhassa, sīlabyasanena "
            "vā phuṭṭhassa, diṭṭhibyasanena vā phuṭṭhassa, aññataraññatarena byasanena samannāgatassa, "
            "aññataraññatarena dukkhadhammena phuṭṭhassa ")
STRUCK_TAIL = {
    "soko socanā socitattaṃ antosoko antoparisoko cetaso parijjhāyanā domanassaṃ sokasallaṃ": K45.SOKA_LIST,
    ("ādevo paridevo ādevanā paridevanā ādevitattaṃ paridevitattaṃ vācā palāpo vippalāpo lālappo lālappanā "
     "lālappitattaṃ"): PARIDEVA,
    "āyāso upāyāso āyāsitattaṃ upāyāsitattaṃ": K45.UPAYASA_LIST,
}


def body_ru(b):
    if "akusamūlaṃ" in b:
        slip("^2-277 «avijjālaṅgī moho akusamūlaṃ» (akusa- for akusala-): rendered as meant «неблагой корень»")
    if "abhinibbati " in b:
        slip("^2-273 «nibbatti abhinibbati» (abhinibbatti elsewhere; the termbase has both): «появление»")
    if b in BODY:
        return BODY[b]
    m = CITTA_PE_RX.match(b)
    if m:
        if "mānasaṃ …pe…" in b:
            slip("^2-269 «mānasaṃ …pe…»: space before …pe… (ignored)")
        return CITTA_PE.format(x=TAJJA_DH[m.group(1)]), True
    if b.startswith(STRUCK_P):
        return f"{K45.STRUCK} {STRUCK_TAIL[b[len(STRUCK_P):]]}", True
    raise KeyError(b)


# =========================================================================== mind-type openers (pi-1 shapes)
KIND_Q = {"akusalā": "Что такое неблагие явления?", "kusalā": "Что такое благие явления?",
          "abyākatā": "Что такое этически неопределённые явления?"}
WHEN = "В то время, когда"
SUBJ = {  # <X> uppann(aṃ|ā) hoti -> (Russian, gender)
    "akusalaṃ cittaṃ": ("неблагой ум", "m"),
    "kāmāvacaraṃ kusalaṃ cittaṃ": ("благой ум, относящийся к миру чувственных желаний", "m"),
    "cakkhuviññāṇaṃ": ("зрительное сознание", "n"), "sotaviññāṇaṃ": ("слуховое сознание", "n"),
    "ghānaviññāṇaṃ": ("обонятельное сознание", "n"), "jivhāviññāṇaṃ": ("вкусовое сознание", "n"),
    "kāyaviññāṇaṃ": ("осязательное сознание", "n"), "manodhātu": ("элемент ума", "m"),
    "manoviññāṇadhātu": ("элемент умственного сознания", "m"),
}
END = {"m": ("ый", "ий"), "n": ("ое", "ее")}                   # сопровождаем-, имеющ-
VIP = {"m": "являющийся результатом", "n": "являющееся результатом"}    # vipākaṃ / vipākā (pi-1 ^1-431, ^1-455)
SAHA = {"somanassa": "радостью", "upekkhā": "невозмутимостью", "domanassa": "унынием", "sukha": "удовольствием",
        "dukkha": "болью"}
SAMP = {"diṭṭhigata": "с приверженностью воззрениям", "paṭigha": "с неприязнью", "vicikicchā": "с колебанием",
        "uddhacca": "с беспокойством", "ñāṇa": "со знанием"}
OBJ = {"rūpa": "видимую форму", "sadda": "звук", "gandha": "запах", "rasa": "вкус", "phoṭṭhabba": "осязаемое",
       "dhamma": "объект ума"}
KAMMA = {"kāmāvacarassa kusalassa": "вследствие совершённого и накопленного благого действия, относящегося к миру "
                                    "чувственных желаний,",
         "akusalassa": "вследствие совершённого и накопленного неблагого действия"}
KIRIYA = {"m": "функциональный, ни благой, ни неблагой и не являющийся результатом действий"}   # pi-1 ^1-566


def quals(body):
    """the qualifier string of a mind-type opener (after «Yasmiṃ samaye»), pi-1 ^1-399 / ^1-431 / ^1-498 shapes"""
    m = re.match(r"^(kāmāvacarassa kusalassa|akusalassa) kammassa katattā upacitattā (.*)$", body)
    pre = ""
    if m:
        pre, body = KAMMA[m.group(1)] + " ", m.group(2)
    pieces = [p.strip() for p in body.split("…pe…")]
    g = "m"
    out = []
    for piece in pieces:
        toks = piece.split(" ")
        ru, i, objs = [], 0, 0
        only_obj = True
        while i < len(toks):
            t = toks[i]
            rest = " ".join(toks[i:])
            ms = re.match(r"^(vipākaṃ |vipākā )?(akusalaṃ cittaṃ|kāmāvacaraṃ kusalaṃ cittaṃ|\S+viññāṇaṃ|manodhātu|"
                          r"manoviññāṇadhātu) uppann(?:aṃ|ā) hoti", rest)
            if ms:
                subj, g = SUBJ[ms.group(2)]
                ru.append(f"возникает {subj}")
                if ms.group(1):
                    ru.append(VIP[g])
                i += len(ms.group(0).split(" "))
                only_obj = False
                continue
            if rest.startswith("kiriyā neva kusalā nākusalā na ca kammavipākā"):
                ru.append(KIRIYA[g])
                i += 7
                only_obj = False
                continue
            mt = re.match(r"^(\S+?)sahagat(?:aṃ|ā)$", t)
            if mt:
                ru.append(f"сопровождаем{END[g][0]} {SAHA[mt.group(1)]}")
                i += 1
                only_obj = False
                continue
            mt = re.match(r"^(\S+?)(sampayutt|vippayutt)(?:aṃ|ā)$", t)
            if mt:
                neg = "не " if mt.group(2) == "vippayutt" else ""
                ru.append(f"{neg}связанн{END[g][0]} {SAMP[mt.group(1)]}")
                i += 1
                only_obj = False
                continue
            if t == "sasaṅkhārena":
                ru.append("с побуждением")
                i += 1
                only_obj = False
                continue
            mt = re.match(r"^(\S+?)ārammaṇ(?:aṃ|ā)$", t)
            if mt:
                o = OBJ[mt.group(1) + "a"]          # rūpa + ārammaṇa = rūpārammaṇa
                if objs == 0 and not only_obj:
                    ru.append(f"имеющ{END[g][1]} объектом {o}")
                elif objs == 0 and only_obj and not out:
                    ru.append(f"имеющ{END[g][1]} объектом {o}")
                else:
                    ru.append(f"или {o}")
                objs += 1
                i += 1
                if i < len(toks) and toks[i] == "vā":
                    i += 1
                continue
            if rest == "yaṃ yaṃ vā panārabbha":
                ru.append("или что бы то ни было")
                break
            raise ValueError((t, piece))
        out.append(", ".join(ru))
    return pre + "… ".join(out)


# jhāna openers: pi-1 ^1-167 / ^1-268 / ^1-277 / ^1-499 / ^1-501 / ^1-505 / ^1-577 / ^1-579 wording
J1 = "полностью уединившись от чувственных удовольствий… входит в первое медитативное погружение"
J1_KASINA = f"{J1}, со всеохватным объектом земли{{v}}, и пребывает в нём"
J4_ARUPA = ("полностью преодолев сферу отсутствия чего-либо, в сопровождении восприятия сферы ни восприятия, ни "
            "невосприятия, с устранением приятного… входит в четвёртое медитативное погружение и пребывает в нём")
J1_SUPRA = f"{J1}, с трудным способом практики и медленным высшим знанием, {{s}}и пребывает в нём"
SUPRA = ("надмирское медитативное погружение, ведущее к освобождению и к убыванию, для устранения приверженности "
         "воззрениям, для достижения первой ступени и, ")
KASINA_V = " [вариант написания (Sī., Syā.): paṭhavīkasiṇaṃ]"
KIRIYA_JH = "функциональное, ни благое, ни неблагое и не являющееся результатом действий, для пребывания в счастье в этой жизни и"
P_J1 = "vivicceva kāmehi…pe… paṭhamaṃ jhānaṃ upasampajja viharati"
P_J4 = ("sabbaso ākiñcaññāyatanaṃ samatikkamma nevasaññānāsaññāyatanasaññāsahagataṃ sukhassa ca pahānā…pe… catutthaṃ "
        "jhānaṃ upasampajja viharati")
P_SUPRA = "lokuttaraṃ jhānaṃ bhāveti niyyānikaṃ apacayagāmiṃ diṭṭhigatānaṃ pahānāya paṭhamāya bhūmiyā pattiyā"
JHANA = {  # Pāli (after «Yasmiṃ samaye» / «Tasseva») -> Russian (after «В то время, когда» / sentence start)
    f"rūpūpapattiyā maggaṃ bhāveti {P_J1} pathavīkasiṇaṃ [paṭhavīkasiṇaṃ (sī. syā.)]":
        f"кто-либо развивает путь к рождению в мире форм и, {J1_KASINA.format(v=KASINA_V)}",
    f"rūpūpapattiyā maggaṃ bhāveti {P_J1} pathavīkasiṇaṃ":
        f"кто-либо развивает путь к рождению в мире форм и, {J1_KASINA.format(v='')}",
    f"arūpūpapattiyā maggaṃ bhāveti {P_J4}": f"кто-либо развивает путь к рождению в мире без форм и, {J4_ARUPA}",
    f"{P_SUPRA} {P_J1} dukkhapaṭipadaṃ dandhābhiññaṃ": f"кто-либо развивает {SUPRA}{J1_SUPRA.format(s='')}",
    f"rūpāvacaraṃ jhānaṃ bhāveti kiriyaṃ neva kusalaṃ nākusalaṃ na ca kammavipākaṃ diṭṭhadhammasukhavihāraṃ {P_J1} "
    "pathavīkasiṇaṃ": (f"кто-либо развивает медитативное погружение, относящееся к миру форм, {KIRIYA_JH}, "
                       f"{J1_KASINA.format(v='')}"),
    f"arūpāvacaraṃ jhānaṃ bhāveti kiriyaṃ neva kusalaṃ nākusalaṃ na ca kammavipākaṃ diṭṭhadhammasukhavihāraṃ {P_J4}":
        f"кто-либо развивает медитативное погружение, относящееся к миру без форм, {KIRIYA_JH}, {J4_ARUPA}",
}
TASSEVA = {
    f"Tasseva rūpāvacarassa kusalassa kammassa katattā upacitattā vipākaṃ {P_J1} pathavīkasiṇaṃ":
        ("Вследствие того же совершённого и накопленного благого действия, относящегося к миру форм, в качестве его "
         f"результата, когда кто-либо, {J1_KASINA.format(v='')}"),
    f"Tasseva arūpāvacarassa kusalassa kammassa katattā upacitattā vipākaṃ {P_J4}":
        ("Вследствие того же совершённого и накопленного благого действия, относящегося к миру без форм, в качестве "
         f"его результата, когда кто-либо, {J4_ARUPA}"),
    f"Tasseva lokuttarassa kusalassa jhānassa katattā bhāvitattā vipākaṃ {P_J1} dukkhapaṭipadaṃ dandhābhiññaṃ":
        ("Вследствие того же совершённого и развитого надмирского благого медитативного погружения, в качестве его "
         f"результата, когда кто-либо, {J1_SUPRA.format(s='')}"),
    f"Tasseva lokuttarassa kusalassa jhānassa katattā bhāvitattā vipākaṃ {P_J1} dukkhapaṭipadaṃ dandhābhiññaṃ suññataṃ":
        ("Вследствие того же совершённого и развитого надмирского благого медитативного погружения, в качестве его "
         f"результата, когда кто-либо, {J1_SUPRA.format(s='пустое, ')}"),
}
CONTACT_PE = "есть контакт… есть отсутствие отвлечения"        # phasso hoti…pe… avikkhepo hoti (pi-1)


def head(p):
    """«Katame dhammā X? Yasmiṃ samaye …» / «Tasseva …» (everything before «, tasmiṃ samaye») -> Russian"""
    p = p.replace("kāmehi …pe…", "kāmehi…pe…")
    if p in TASSEVA:
        return TASSEVA[p]
    m = re.match(r"^Katame dhammā (\S+)\? Yasmiṃ samaye (.*)$", p)
    assert m, p
    kind, body = m.groups()
    if body in JHANA:
        return f"{KIND_Q[kind]} {WHEN} {JHANA[body]}"
    return f"{KIND_Q[kind]} {WHEN} {quals(body)}"


# =========================================================================== the chain
SEP_RX = re.compile(r"(…pe…\s?|;\s|,\s)")
SUTTA_CHAIN_P = ("Avijjāpaccayā saṅkhārā, saṅkhārapaccayā viññāṇaṃ, viññāṇapaccayā nāmarūpaṃ, nāmarūpapaccayā "
                 "saḷāyatanaṃ, saḷāyatanapaccayā phasso, phassapaccayā vedanā, vedanāpaccayā taṇhā, taṇhāpaccayā "
                 "upādānaṃ, upādānapaccayā bhavo, bhavapaccayā jāti, jātipaccayā jarāmaraṇaṃ "
                 "sokaparidevadukkhadomanassupāyāsā sambhavanti.")
SUTTA_CHAIN = None   # pi-1 ^1-1343 wording, read from the pi-1 rails in check_pi1()


def chain(text):
    """«Avijjāpaccayā saṅkhāro, …, jātipaccayā jarāmaraṇaṃ» (no final punctuation) -> Russian, lower case"""
    if "saṅkhārahetukaṃ viññāṇapaccayā" in text:
        text = text.replace("saṅkhārahetukaṃ viññāṇapaccayā", "saṅkhārahetukaṃ, viññāṇapaccayā")
        slip("^2-262 «saṅkhārahetukaṃ viññāṇapaccayā nāmarūpaṃ»: comma missing (added)")
    parts = SEP_RX.split(text)
    clauses, seps = parts[0::2], parts[1::2]
    ru = [(f"{AND_ALSO} " if CLAUSE_RX.match(c).group("pi") else "") + clause(c) for c in clauses]
    out = ru[0]
    for i, s in enumerate(seps):
        moded = bool(CLAUSE_RX.match(clauses[i]).group("mk")) or bool(CLAUSE_RX.match(clauses[i + 1]).group("mk"))
        if s.startswith("…pe…"):
            out += "… "
        elif s.startswith(";") or moded:
            out += "; "
        else:
            out += ", "
        out += ru[i + 1]
    if "upādānapaccayā upādānasampayuttaṃ" in text or "taṇhāpaccayā upādānaṃ upādānasampayuttaṃ" in text:
        slip("^2-245 «taṇhāpaccayā upādānaṃ upādānasampayuttaṃ» (the parallel lines have taṇhāsampayuttaṃ): "
             "translated as written, «связанное с цеплянием»")
    return low(out)


def chain_line(text):
    """«<chain>. Evametassa … hoti.» (the chain part may also be followed by nothing)"""
    m = re.match(r"^(.*?)\. (Evame\S+ .*)$", text)
    if m:
        return f"{chain(m.group(1))}. {SENT[m.group(2)]}"
    assert text.endswith("."), text
    return f"{chain(text[:-1])}."


# =========================================================================== sentences of the definitions
Q_RX = re.compile(r"^Tattha (?:katamo|katamā|katamaṃ|katame) (.+?)(\?)?$")
A_RX = re.compile(r"^(.*) – (?:ayaṃ|idaṃ|ime) (?:vuccati|vuccanti) (– )?(.*)$")
V_RX = re.compile(r"^(?:ayaṃ|idaṃ|ime|Ayaṃ|Idaṃ|Ime) (?:vuccati|vuccanti) (– )?(.*)$")
T_RX = re.compile(r"^[Tt]ena vuccati (.*)$")
TOPIC_RX = re.compile(r"^(\S+paccayā(?:pi)? .*?)(n?)ti\.$")


def term_of(raw, suttanta):
    """a quoted (or unquoted) term with its tail -> (Russian instrumental, quoted?, tail)"""
    tail = ""
    m = re.match(r"^(.*?)(…pe…)?(\.?)$", raw)
    t, pe, dot = m.groups()
    tail = ("…" if pe else "") + dot
    q1, q2 = t.startswith('"'), t.endswith('"')
    t = t.strip('"')
    return t, q1 or q2, (q1, q2), tail


def called(raw, suttanta, dash, sid):
    t, quoted, (q1, q2), tail = term_of(raw, suttanta)
    if q1 != q2:
        slip(f"^{sid} «… vuccati {raw[:60]}»: one quotation mark missing (rendered with both)")
    if not quoted:
        slip(f"^{sid} «… vuccati {t}» without quotation marks: rendered without «»")
    ins = term(t, "ins", suttanta)
    d = "– " if dash else ""
    return f"это называется {d}«{ins}»{tail}" if quoted else f"это называется {d}{ins}{tail}"


def tena(raw, sid):
    m = re.match(r'^("?)(evametassa kevalassa dukkhakkhandhassa samudayo hot[īi]|evametesaṃ dhammānaṃ samudayo hotī)"ti\.$',
                 raw)
    assert m, raw
    if not m.group(1):
        slip(f"^{sid} «Tena vuccati evametassa … hotī\"ti»: opening quotation mark missing (rendered with both)")
    if m.group(2).endswith("hoti"):
        slip(f"^{sid} «…samudayo hoti\"ti» (hotī elsewhere): same Russian")
    phrase = EVAM_DH if "evametesaṃ" in m.group(2) else EVAM
    return f"{TENA} «{phrase}»."


def piece(p, sid, suttanta, first):
    """one fragment of a sentence (fragments are joined by …pe…)"""
    m = T_RX.match(p)
    if m:
        r = tena(m.group(1), sid)
        return r if p[0] == "T" else low(r)
    m = V_RX.match(p)
    if m:
        r = called(m.group(2), suttanta, m.group(1), sid)
        return cap(r) if p[0].isupper() else r
    m = A_RX.match(p)
    if m:
        body, dash, raw = m.groups()
        ru, comma = body_ru(body)
        return f"{ru}{',' if comma else ''} – {called(raw, suttanta, dash, sid)}"
    m = Q_RX.match(p)
    if m:
        t, qm = m.groups()
        names = "… ".join(term(x.strip(), "nom", suttanta) for x in t.split("…pe…"))
        return f"Что такое {S.TATTHA} {names}{'?' if qm else ''}"
    m = TOPIC_RX.match(p)
    if m:
        t = m.group(1) + ("ṃ" if m.group(2) else "")
        return f"«{cap(clause(t, suttanta))}»."
    if not first:
        return term(p, "nom", suttanta)          # a bare term inside a …pe… run of names
    raise KeyError(p)


def sentence(s, sid, suttanta):
    if s in SENT:
        return SENT[s]
    s = s.replace('" …pe…', '"…pe…')
    if s.startswith("Tattha katam") and "?" not in s:
        frags = [x.strip() for x in re.split(r"…pe…", s)]
        # last fragment may be «ayaṃ vuccati …» / «tena vuccati …»
        out = [piece(f, sid, suttanta, i == 0) for i, f in enumerate(frags)]
        r = "… ".join(out)
        return r
    frags = re.split(r"…pe…\s?(?=(?:tena|ayaṃ|idaṃ) vuccati)", s)
    return "… ".join(piece(f.strip(), sid, suttanta, i == 0) for i, f in enumerate(frags))


def def_line(ln, sid, suttanta):
    return " ".join(sentence(s, sid, suttanta) for s in K45.split_sents(ln))


# =========================================================================== lines and chapter
OPEN_RX = re.compile(r"^((?:Katame dhammā \S+\? Yasmiṃ samaye|Tasseva) .*?), tasmiṃ samaye (.*)$")
KUSALA_TAIL = "phasso hoti…pe… avikkhepo hoti – ime dhammā kusalā."


def line6(ln, sid, section):
    if ln in SENT:
        return SENT[ln]
    if ln == SUTTA_CHAIN_P.rstrip(".") + ". Evametassa kevalassa dukkhakkhandhassa samudayo hoti.":
        return f"{SUTTA_CHAIN}. {EVAM}."
    m = OPEN_RX.match(ln)
    if m:
        h, rest = m.groups()
        if rest == KUSALA_TAIL:
            return f"{head(h)}, {AT_TIME} {CONTACT_PE} – это благие явления."
        return f"{head(h)}, {AT_TIME} {chain_line(rest)}"
    m = re.match(r"^Tasmiṃ samaye (.*)$", ln)
    if m:
        return f"{cap(AT_TIME)} {chain_line(m.group(1))}"
    if re.match(r"^(Avijjāpaccayā|Saṅkhārapaccayā avijjā)", ln):
        return cap(chain_line(ln))
    return def_line(ln, sid, section == "Suttantabhājanīyaṃ")


def heading(ln):
    lvl, text = ln.split(" ", 1)
    T = {"Paṭiccasamuppādavibhaṅgo": S.CH_TITLE[6][1], "Suttantabhājanīyaṃ": S.SUTTANTA_BH,
         "Abhidhammabhājanīyaṃ": S.ABHI_BH}
    T.update(SUBHEAD)
    return f"{lvl} {T[text]}"


def build():
    pali = (S.PALI / PART).read_text(encoding="utf-8")
    h, section = {}, None
    for sid, lines in S.segs(pali):
        lines = [re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", ln) for ln in lines]
        if lines[0].startswith("#"):
            assert len(lines) == 1
            text = lines[0].split(" ", 1)[1]
            if text in ("Suttantabhājanīyaṃ", "Abhidhammabhājanīyaṃ"):
                section = text
            h[sid] = [heading(lines[0])]
            continue
        h[sid] = [line6(ln, sid, section) for ln in lines]
    return pali, h


# =========================================================================== pi-1 checks
def check_pi1():
    global SUTTA_CHAIN
    K23.assert_pi1()
    t = K23.PI1_ALL
    i = t.index("«Неведением обусловлены формирующие факторы")
    j = t.index("; так происходит возникновение всей этой совокупности страдания", i)
    SUTTA_CHAIN = t[i + 1:j]
    K23.assert_pi1(low(EVAM), MOHA_PE.replace("То, что есть ", ""), "намерение, проявление намерения, состояние намеренности",
                   PHASSA.replace("То, что есть ", ""), RAGA7, DITTHI16, SADDHA4.replace("То, что есть ", ""),
                   UDDHACCA.replace("То, что есть ", ""), "сомнение, проявление сомнения, состояние сомнения, "
                   "неуверенность, колебание, раздвоенность, распутье", "нерешительность, неспособность прийти к "
                   "определённости, блуждание, беспорядочное блуждание, отсутствие углубления", "оцепенелость ума, "
                   "терзание ума", ALOBHA.replace("То, что есть ", ""), "отсутствие злобы, отсутствие проявления "
                   "злобы, отсутствие состояния злобы", "отсутствие недоброжелательности, отсутствие неприязни, "
                   "отсутствие злобы как благой корень", NOT_KNOW4, "уничтожение, угасание, распад, полный распад, "
                   "непостоянство, исчезновение", "или же какая бы другая материальная форма ни была рождённой умом, "
                   "имеющей причиной ум, порождённой умом", "Итак, эта вялость и эта сонливость",
                   "свирепость, грубость, недовольство ума", CONTACT_PE, J1, J4_ARUPA, "в качестве его результата, "
                   "когда кто-либо", "Вследствие того же совершённого и развитого надмирского благого медитативного "
                   "погружения", "Вследствие того же совершённого и накопленного благого действия, относящегося к "
                   "миру форм", "Вследствие того же совершённого и накопленного благого действия, относящегося к "
                   "миру без форм", f"кто-либо развивает {SUPRA}{J1}, с трудным способом практики и медленным высшим "
                   "знанием, и пребывает в нём", "с трудным способом практики и медленным высшим знанием, пустое, и "
                   "пребывает в нём", f"кто-либо развивает путь к рождению в мире форм и, {J1}, со всеохватным объектом "
                   "земли, и пребывает в нём", "кто-либо развивает путь к рождению в мире без форм и, полностью "
                   "преодолев сферу отсутствия чего-либо", f"относящееся к миру форм, {KIRIYA_JH}, полностью",
                   f"относящееся к миру без форм, {KIRIYA_JH}", "вследствие совершённого и накопленного благого "
                   "действия, относящегося к миру чувственных желаний, возникает зрительное сознание, являющееся "
                   "результатом, сопровождаемое невозмутимостью, имеющее объектом видимую форму",
                   "вследствие совершённого и накопленного неблагого действия возникает зрительное сознание",
                   "возникает элемент ума, " + KIRIYA["m"] + ", сопровождаемый невозмутимостью",
                   "соответствующий элемент зрительного сознания", "соответствующий элемент осязательного сознания",
                   "соответствующий элемент ума", "Четыре великих элемента и материальная форма, производная от "
                   "четырёх великих элементов, – это")


# =========================================================================== notes
def notes_md():
    ex = lambda t, s=False: term(t, "nom", s)            # noqa: E731
    exi = lambda t, s=False: term(t, "ins", s)           # noqa: E731
    L = ["# pi-2 Russian rails: new formulas of chapter 6 (^2-6-0 … ^2-354)", "",
         "Generated by build_rails_6_ru.py; import it instead of retyping. Strings already in ru-rails-formulas.md "
         "(sample), notes-1.md, notes-2-3.md or notes-4-5.md are not repeated.", "",
         "## Headings and closing labels", "",
         f"### Paṭiccasamuppādavibhaṅgo = ### {S.CH_TITLE[6][1]}"]
    L += [f"##### {p} = ##### {r}  (closing label «{p}.» = «{r}.»)" for p, r in SUBHEAD.items()]
    L += [f"Paṭiccasamuppādavibhaṅgo [paccayākāravibhaṅgo (sī. syā.)] niṭṭhito. = "
          f"{SENT['Paṭiccasamuppādavibhaṅgo [paccayākāravibhaṅgo (sī. syā.)] niṭṭhito.']}",
          "", "## The chain", "",
          f"Avijjāpaccayā saṅkhārā, … jātipaccayā jarāmaraṇaṃ sokaparidevadukkhadomanassupāyāsā sambhavanti. = "
          f"{SUTTA_CHAIN}. (pi-1 ^1-1343)",
          f"Evametassa kevalassa dukkhakkhandhassa samudayo hoti. = {EVAM}. (pi-1 ^1-1343)",
          f"Evametesaṃ dhammānaṃ samudayo hoti. = {EVAM_DH}.",
          "Xpaccayā Y (chain clause) = X(ins) обусловлен/обусловлена/обусловлено/обусловлены Y, e.g. "
          f"«{clause('avijjāpaccayā saṅkhāro')}», «{clause('nāmarūpapaccayā saḷāyatanaṃ')}»",
          f"Xpaccayā Y Xhetuko = «{clause('avijjāpaccayā saṅkhāro avijjāhetuko')}» (clauses joined by «;»)",
          f"Xpaccayā Y Xsampayutto = «{clause('avijjāpaccayā saṅkhāro avijjāsampayutto')}» (clauses joined by «;»)",
          f"viññāṇapaccayā nāmarūpaṃ viññāṇasampayuttaṃ nāmaṃ = «{clause('viññāṇapaccayā nāmarūpaṃ viññāṇasampayuttaṃ nāmaṃ')}»",
          f"nāmarūpapaccayā saḷāyatanaṃ nāmasampayuttaṃ chaṭṭhāyatanaṃ = "
          f"«{clause('nāmarūpapaccayā saḷāyatanaṃ nāmasampayuttaṃ chaṭṭhāyatanaṃ')}»",
          f"Xpaccayā Y, Ypaccayāpi X = «{clause('avijjāpaccayā saṅkhāro')}, {AND_ALSO} "
          f"{clause('saṅkhārapaccayāpi avijjā')}»",
          "Tasmiṃ samaye <chain> = В это время <chain>",
          "Xpaccayā Y (named term, nominative / instrumental) = Y, обусловленный X(ins) / Y(ins), обусловленным X(ins): "
          f"«{ex('avijjāpaccayā saṅkhāro')}» / «{exi('avijjāpaccayā saṅkhāro')}»; Suttanta plural "
          f"«{ex('avijjāpaccayā saṅkhārā', True)}», «{ex('saṅkhārapaccayā viññāṇaṃ', True)}»",
          f"Y Xhetuko (term) = «{ex('avijjāpaccayā saṅkhāro avijjāhetuko')}»",
          f"Y Xsampayutto (term) = «{ex('avijjāpaccayā saṅkhāro avijjāsampayutto')}»",
          f"Xpaccayāpi Y (term) = «{ex('saṅkhārapaccayāpi avijjā')}»",
          f"Nāmapaccayā phassoti. (topic line) = «{cap(clause('nāmapaccayā phasso'))}». (the chain clause quoted)",
          "chain nouns: " + "; ".join(f"{k} = {v[0]} (ins. {v[1]})" for k, v in N.items()),
          "", "## Frames", "",
          f"Atthi nāmaṃ, atthi rūpaṃ. = {ATTHI_NR}", f"Iti idañca nāmaṃ, idañca rūpaṃ. = {ITI_NR}",
          f"Atthi jarā, atthi maraṇaṃ. = {ATTHI_JM}", f"Iti ayañca jarā, idañca maraṇaṃ. = {ITI_JM}",
          f"Bhavo duvidhena – atthi kammabhavo, atthi upapattibhavo. = {BHAVA2}",
          f"Iti ayañca kammabhavo, ayañca upapattibhavo. = {ITI_BH}",
          f"Sabbampi bhavagāmikammaṃ kammabhavo. = {ALL_KAMMA}",
          f"Evametassa … samudayo hotīti[,/.] evametassa … saṅgati hoti, samāgamo hoti, samodhānaṃ hoti, pātubhāvo "
          f"hoti. = «{EVAM}»: {EVAM_MEANS}. / «{EVAM}». {cap(EVAM_MEANS)}.",
          f"Tena vuccati \"evametassa kevalassa dukkhakkhandhassa samudayo hotī\"ti. = {TENA} «{EVAM}».",
          f"Ṭhapetvā X, vedanākkhandho … viññāṇakkhandho = Кроме X(gen), {KH4}",
          f"tasmiṃ samaye phasso hoti…pe… avikkhepo hoti – ime dhammā kusalā. = {AT_TIME} {CONTACT_PE} – это благие "
          "явления.",
          "", "## Definitions", "",
          f"Dukkhe aññāṇaṃ, … paṭipadāya aññāṇaṃ = {NOT_KNOW4} (pi-1 ^1-1067)",
          f"Puññābhisaṅkhāro, … cittasaṅkhāro. = {SANKHARA6}",
          f"Kusalā cetanā kāmāvacarā rūpāvacarā dānamayā sīlamayā bhāvanāmayā = "
          f"{BODY['Kusalā cetanā kāmāvacarā rūpāvacarā dānamayā sīlamayā bhāvanāmayā'][0]}",
          f"Kāyasañcetanā kāyasaṅkhāro, … cittasaṅkhāro. = {KAYA3}",
          f"Kāmupādānaṃ, diṭṭhupādānaṃ, sīlabbatupādānaṃ, attavādupādānaṃ = "
          f"{BODY['Kāmupādānaṃ, diṭṭhupādānaṃ, sīlabbatupādānaṃ, attavādupādānaṃ'][0]}",
          f"Kāmabhavo, … pañcavokārabhavo = {BHAVA9}",
          f"Yaṃ aññāṇaṃ adassanaṃ…pe… avijjālaṅgī moho akusalamūlaṃ = {MOHA_PE} (pi-1 ^1-1318)",
          f"Yā cetanā sañcetanā sañcetayitattaṃ = {CETANA}",
          f"Yaṃ cittaṃ mano mānasaṃ…pe… tajjā<X>dhātu = {CITTA_PE.format(x='элемент …')}",
          f"Yo phasso phusanā samphusanā samphusitattaṃ = {PHASSA} (pi-1 ^1-2)",
          f"Yo rāgo sārāgo anunayo anurodho nandī nandirāgo cittassa sārāgo = То, что есть {RAGA7}",
          f"Yā diṭṭhi diṭṭhigataṃ … vipariyāsaggāho = То, что есть {DITTHI16} (pi-1 ^1-392)",
          f"Yo cittassa adhimokkho adhimuccanā tadadhimuttatā = {ADHIMOKKHA}",
          f"Yā saddhā saddahanā okappanā abhippasādo = {SADDHA4}",
          f"Yaṃ cittassa uddhaccaṃ avūpasamo cetaso vikkhepo bhantattaṃ cittassa = {UDDHACCA}",
          f"Yā kaṅkhā kaṅkhāyanā … manovilekho = {VICIKICCHA}",
          f"Yo cittassa āghāto…pe… caṇḍikkaṃ asuropo … anattamanatā cittassa = То, что есть досада ума… свирепость, "
          "грубость, недовольство ума",
          f"Yo alobho … alobho kusalamūlaṃ = {ALOBHA}", f"Yo adoso … adoso kusalamūlaṃ = {ADOSA}",
          f"Yā tesaṃ tesaṃ dhammānaṃ jāti sañjāti nibbatti abhinibbatti pātubhāvo = "
          f"{BODY['Yā tesaṃ tesaṃ dhammānaṃ jāti sañjāti nibbatti abhinibbatti pātubhāvo'][0]}",
          f"Yā tesaṃ tesaṃ dhammānaṃ jarā jīraṇatā āyuno saṃhāni = "
          f"{BODY['Yā tesaṃ tesaṃ dhammānaṃ jarā jīraṇatā āyuno saṃhāni'][0]}",
          f"Yo tesaṃ tesaṃ dhammānaṃ khayo vayo bhedo paribhedo aniccatā antaradhānaṃ = "
          f"{BODY['Yo tesaṃ tesaṃ dhammānaṃ khayo vayo bhedo paribhedo aniccatā antaradhānaṃ'][0]}",
          f"Cakkhāyatanassa upacayo, … cittasamuṭṭhānaṃ = {UPACAYA5}",
          f"Yaṃ rūpaṃ nissāya manoviññāṇadhātu vattati = {cap(DEPENDS)}",
          "", "## Mind-type openers (pi-1 ^1-1, 365, 399, 431, 455, 498, 556, 566 shapes)", "",
          "Katame dhammā akusalā / kusalā / abyākatā? = " + " / ".join(KIND_Q.values()),
          f"Yasmiṃ samaye … , tasmiṃ samaye = {WHEN} … , {AT_TIME}",
          "<X>sahagataṃ / <X>sampayuttaṃ / <X>vippayuttaṃ / sasaṅkhārena / <O>ārammaṇaṃ vā … yaṃ yaṃ vā panārabbha = "
          "сопровождаемый X / связанный с X / не связанный с X / с побуждением / имеющий объектом O, или …, или что "
          "бы то ни было (neuter for the five sense consciousnesses: сопровождаемое, имеющее)",
          f"kāmāvacarassa kusalassa kammassa katattā upacitattā vipākaṃ … = {KAMMA['kāmāvacarassa kusalassa']} "
          "возникает …, являющееся результатом",
          f"akusalassa kammassa katattā upacitattā vipākaṃ … = {KAMMA['akusalassa']} возникает …",
          f"kiriyā neva kusalā nākusalā na ca kammavipākā = {KIRIYA['m']}",
          "jhāna openers and Tasseva … vipākaṃ: pi-1 ^1-167, 268, 277, 499, 501, 505, 577, 579 wording (see JHANA / "
          "TASSEVA in the builder)",
          ]
    return "\n".join(L) + "\n"


def main():
    check_pi1()
    pali, h = build()
    (S.OUT / PART).write_text(K23.render(pali, h), encoding="utf-8", newline="\n")
    print(f"wrote {PART}: {len(S.segs(pali))} segments")
    NOTES_PATH.write_text(notes_md(), encoding="utf-8", newline="\n")
    for s in SLIPS:
        print("slip:", s)


if __name__ == "__main__":
    main()
