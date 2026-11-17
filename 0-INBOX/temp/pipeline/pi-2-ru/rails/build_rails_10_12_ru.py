"""Builder for the Russian rails translation of pi-2 (Vibhaṅga, plain audience), chapters 10, 11 and 12
(Bojjhaṅgavibhaṅgo ^2-10-0 … ^2-485, Maggaṅgavibhaṅgo ^2-11-0 … ^2-507, Jhānavibhaṅgo ^2-12-0 … ^2-641).

Writes (only when run as a script):
  AI_translation/russian/pi-2-russian-plain-rails_split_chapters/10-bojjhangavibhango.md
  AI_translation/russian/pi-2-russian-plain-rails_split_chapters/11-maggangavibhango.md
  AI_translation/russian/pi-2-russian-plain-rails_split_chapters/12-jhanavibhango.md
  0-INBOX/temp/pipeline/pi-2-ru/rails/notes-10-12.md   (new recurring formulas, Pāli = Russian)

Every Russian string comes from the fixed tables and functions below, so identical Pāli gives identical Russian.
Imported read-only: the approved sample builder (S) and the builders of chapters 1 (K1), 2-3 (K23), 4-5 (K45), 6 (K6)
and 7-9 (K79). Their tables are extended only in memory, here (the question-section engine also learns neuter
singular subjects: «Правильное воззрение», «Четвёртое медитативное погружение»).

Shared passages reuse the earlier Russian: the eightfold path of ch. 4 (^2-205 … ^2-211), the jhāna formula of pi-1 /
ch. 4, the right efforts and the foundations of mindfulness of ch. 7-8, the jhāna openers of ch. 6 / pi-1, and the
pi-1 Russian of the hindrance, sense-restraint and moderation passages (^1-1160 … ^1-1167, ^1-1352 … ^1-1355).

usage: python -I -X utf8 build_rails_10_12_ru.py
"""
import pathlib
import re
import sys

RAILS = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-ru\rails")
sys.path.insert(0, str(RAILS))
import build_rails_sample_ru as S  # noqa: E402  (importing writes nothing)
import build_rails_1_ru as K1      # noqa: E402
import build_rails_2_3_ru as K23   # noqa: E402
import build_rails_4_5_ru as K45   # noqa: E402
import build_rails_6_ru as K6      # noqa: E402
import build_rails_7_9_ru as K79   # noqa: E402

PARTS = {10: "10-bojjhangavibhango.md", 11: "11-maggangavibhango.md", 12: "12-jhanavibhango.md"}
NOTES_PATH = RAILS / "notes-10-12.md"
cap, low, nlist = S.cap, K1.low, K45.nlist
SLIPS = []
SID = {"sid": ""}


def slip(msg):
    if msg not in SLIPS:
        SLIPS.append(msg)


def strip_var(s):
    return re.sub(r" \[[^\]]*\]", "", s)


def p1(fname, sid):
    return K23.p1(fname, sid)


def p1_between(fname, sid, start, end):
    t = p1(fname, sid)
    a = t.index(start) + len(start)
    return t[a:t.index(end, a)]


# =========================================================================== shared strings (imported)
MONK = K45.MONK                   # Idha bhikkhu = Здесь монах
TENA = K6.TENA                    # Tena vuccati = Поэтому это называется:
AT_TIME = K6.AT_TIME              # tasmiṃ samaye = в это время
PATH_TAIL = K45.PATH_TAIL         # maggaṅgaṃ maggapariyāpannaṃ
UPETO, UPETO_PE = K79.UPETO, K79.UPETO_PE
UPETO_PE2 = "обладает, вполне обладает… наделён"          # upeto hoti samupeto…pe… samannāgato
CONTACT_PE = K6.CONTACT_PE        # phasso hoti…pe… avikkhepo hoti
ALL_THIS = K79.ALL_THIS           # Ime dhammā kusalā. = Это благие явления.
SUPRA_OPEN = K79.SUPRA_OPEN       # «В то время, когда здесь монах развивает »
IRIYATI = K79.SENT["Iriyati vattati pāleti yapeti yāpeti carati viharati."]
J1F, J2F, J3F, J4F = K45.JHANA1_P1, K45.JHANA2, K45.JHANA3_P1, K45.JHANA4_P1
J3F_ND = J3F.replace("говорят о нём – «", "говорят о нём: «")   # the Pāli of ^2-487 has no dash there
WISDOM_SHORT, SATI_LIST, SAMADHI_LIST = K45.WISDOM_SHORT, K45.SATI_LIST, K45.SAMADHI_LIST
SADDHA4 = K6.SADDHA4[len("То, что есть "):]
FEEL = K23.FEELING_P1
WISDOM_FULL = ("мудрость, понимание, исследование, тщательное исследование, исследование явлений, различение, "
               "распознавание, точное распознавание, учёность, умелость, тонкость, ясность суждения, размышление, "
               "проверка, широта ума, разумность, руководящая сила, прозрение, ясное понимание, стрекало, мудрость, "
               "способность мудрости, сила мудрости, меч мудрости, башня мудрости, свет мудрости, сияние мудрости, "
               "светоч мудрости, сокровище мудрости, отсутствие заблуждения, исследование явлений, правильное "
               "воззрение")                                               # pi-1 ^1-16 (formulas line 155)
VITAKKA_FULL = f"{K23.VITAKKA7}, правильный помысел"                      # pi-1 ^1-7
VICARA = ("движение мысли, удержание мысли, последовательное удержание мысли, пристальное удержание мысли, "
          "непрерывная связь ума с объектом, неотрывное наблюдение за объектом")          # pi-1 ^1-8
VICARA_ANU = VICARA.replace("удержание мысли, последовательное", "последовательное движение мысли, удержание мысли, "
                            "последовательное", 1)                     # ^2-576 cāro anucāro vicāro … (termbase anucāro)
PITI_LIST = ("восторг, ликование, веселье, оживление, весёлость, бурная весёлость, удовлетворённость, воодушевление, "
             "довольство ума")                                           # pi-1 ^1-9
SANNA_LIST = "восприятие, узнавание, состояние узнавания"                 # pi-1 ^1-4
UPEKKHA_LIST = "невозмутимость, проявление невозмутимости, полная невозмутимость, уравновешенность ума"   # termbase
CITTA_PE = f"{K23.CITTA_SHORT} {K23.TAJJA} {K23.DH['manoviññāṇa']}"       # cittaṃ mano mānasaṃ…pe… tajjā…
# pi-1 hindrance definitions (^1-1160 … ^1-1166), read from the pi-1 rails
BYAPADA_P1 = p1_between("4-02-nikkhepakandam.md", "1-1160", "То, что есть такая ", ", – это называется")
THINA_P1 = p1_between("4-02-nikkhepakandam.md", "1-1162", "То, что есть ", ", – это называется")
MIDDHA_P1 = p1_between("4-02-nikkhepakandam.md", "1-1163", "То, что есть ", ", – это называется")
UDDHACCA_P1 = p1_between("4-02-nikkhepakandam.md", "1-1165", "То, что есть ", ", – это называется")
KUKKUCCA_A = p1_between("4-02-nikkhepakandam.md", "1-1166", "угрызения? ", ". То, что есть")
KUKKUCCA_B = p1_between("4-02-nikkhepakandam.md", "1-1166", ". То, что есть ", ", – это называется")
BYAPADA_V = BYAPADA_P1.replace("состояние злобы, недоброжелательность",
                               "состояние злобы [вариант написания (Syā.): dūsanā dūsitattaṃ], недоброжелательность", 1)
THINA_V = THINA_P1.replace("состояние вялости ума", "состояние вялости [вариант написания (Sī., Syā.): thīyanā "
                                                    "thīyitattaṃ] ума", 1)
VICIKICCHA = strip_var(K6.VICIKICCHA)[len("То, что есть "):]
# pi-1 sense-restraint / moderation lines, made pi-2 style («…» around the term in «это называется»)
P1_1352 = p1("4-03-nikkhepakandam.md", "1-1352").replace("это называется неохранением врат чувств.",
                                                         "это называется «неохранением врат чувств».")
P1_1353 = p1("4-03-nikkhepakandam.md", "1-1353").replace("это называется незнанием меры в еде.",
                                                         "это называется «незнанием меры в еде».")
P1_1354 = p1("4-03-nikkhepakandam.md", "1-1354").replace("это называется охранением врат чувств.",
                                                         "это называется «охранением врат чувств».")
P1_1355 = p1("4-03-nikkhepakandam.md", "1-1355").replace("это называется знанием меры в еде.",
                                                         "это называется «знанием меры в еде».")

# =========================================================================== names
BJ = ["sati", "dhammavicaya", "vīriya", "pīti", "passaddhi", "samādhi", "upekkhā"]
BJ_RU = {k: f"фактор пробуждения {K79.BOJJH[k]}" for k in BJ}
BJ_INS = {k: f"фактором пробуждения {K79.BOJJH[k]}" for k in BJ}
SEVEN = "Семь факторов пробуждения"
SEVEN_LIST = f"{SEVEN} – " + nlist([BJ_RU[k] for k in BJ]) + "."
SEVEN_PE = f"{SEVEN} – {BJ_RU['sati']}… {BJ_RU['upekkhā']}."
PATH8_P, PATH8, PATH_INS = K45.PATH8_P, K45.PATH8, K45.PATH_INS
PATH_RU = dict(zip(PATH8_P, PATH8))
PATH_ACC = {"sammādiṭṭhiṃ": ("правильное воззрение", "n"), "sammāsaṅkappaṃ": ("правильный помысел", "m"),
            "sammāvācaṃ": ("правильную речь", "f"), "sammākammantaṃ": ("правильное действие", "n"),
            "sammāājīvaṃ": ("правильный образ жизни", "m"), "sammāvāyāmaṃ": ("правильное усилие", "n"),
            "sammāsatiṃ": ("правильную осознанность", "f"), "sammāsamādhiṃ": ("правильное сосредоточение", "n")}
PATH5_P = ["sammādiṭṭhi", "sammāsaṅkappo", "sammāvāyāmo", "sammāsati", "sammāsamādhi"]
EIGHT = "Восьмичастный путь"
FIVE = "Пятичастный путь"
NOBLE8 = f"Благородный восьмичастный путь, {K23.NAMELY} {nlist(PATH8)}."   # Ariyo aṭṭhaṅgiko maggo, seyyathidaṃ – …
EIGHT_LIST = f"{EIGHT} – {nlist(PATH8)}."
FIVE_LIST = f"{FIVE} – " + nlist([PATH_RU[k] for k in PATH5_P]) + "."
EIGHT_PE = f"{EIGHT} – {PATH8[0]}… {PATH8[-1]}."
JH_ORD = {"paṭhamaṃ": ("первое", "первым"), "dutiyaṃ": ("второе", "вторым"), "tatiyaṃ": ("третье", "третьим"),
          "catutthaṃ": ("четвёртое", "четвёртым"), "pañcamaṃ": ("пятое", "пятым")}
JH = "медитативное погружение"
FOUR_JH = (f"Четыре медитативных погружения – " + nlist([f"{JH_ORD[k][0]} {JH}" for k in
                                                         ("paṭhamaṃ", "dutiyaṃ", "tatiyaṃ", "catutthaṃ")]) + ".")
NISSITA = {"m": "опирающийся на уединение, опирающийся на бесстрастие, опирающийся на прекращение, ведущий к отказу",
           "n": "опирающееся на уединение, опирающееся на бесстрастие, опирающееся на прекращение, ведущее к отказу",
           "f": "опирающуюся на уединение, опирающуюся на бесстрастие, опирающуюся на прекращение, ведущую к отказу"}
NISSITA_P = "vivekanissitaṃ virāganissitaṃ nirodhanissitaṃ vossaggapariṇāmiṃ"
TOWARD = "ведущим к высшему знанию, к полному пробуждению, к нирване"     # abhiññāya sambodhāya nibbānāya saṃvattati

# question words (Tattha katamo X? = Что такое здесь X?) and «это называется «X(ins)»»
NOM, INS = {}, {}


def _term(p, nom, ins):
    NOM[p], INS[p] = nom, ins


for _k in BJ:
    _term(f"{_k}sambojjhaṅgo", BJ_RU[_k], BJ_INS[_k])
for _p, _r in zip(PATH8_P, PATH8):
    _term(_p, _r, PATH_INS[_p])
for _k, (_n, _i) in JH_ORD.items():
    _term(f"{_k} jhānaṃ", f"{_n} {JH}", f"{_i} медитативным погружением")
for _p, _n, _i in [
    ("satta bojjhaṅgā", "семь факторов пробуждения", "семью факторами пробуждения"),
    ("aṭṭhaṅgiko maggo", "восьмичастный путь", "восьмичастным путём"),
    ("pañcaṅgiko maggo", "пятичастный путь", "пятичастным путём"),
    ("anācāro", "неподобающее поведение", "неподобающим поведением"),
    ("ācāro", "подобающее поведение", "подобающим поведением"),
    ("agocaro", "неподходящее место посещения", "неподходящим местом посещения"),
    ("gocaro", "подходящее место посещения", "подходящим местом посещения"),
    ("aṇumattā vajjā", "малейшие проступки", "малейшими проступками"),
    ("sikkhā", "обучение", None), ("sikkhāyo", None, "видами обучения"),
    ("indriyesu aguttadvāratā", "неохранение врат чувств", "неохранением врат чувств"),
    ("indriyesu guttadvāratā", "охранение врат чувств", "охранением врат чувств"),
    ("aguttadvāratā", "неохранение врат чувств", "неохранением врат чувств"),
    ("bhojane amattaññutā", "незнание меры в еде", "незнанием меры в еде"),
    ("bhojane mattaññutā", "знание меры в еде", "знанием меры в еде"),
    ("bodhipakkhikā dhammā", "явления, способствующие пробуждению", "явлениями, способствующими пробуждению"),
    ("sati", "осознанность", "осознанностью"), ("sampajaññaṃ", "ясное понимание", "ясным пониманием"),
    ("abhijjhā", "алчность", "алчностью"), ("loko", "мир", "миром"), ("cittaṃ", "ум", "умом"),
    ("byāpādo", "недоброжелательность", "недоброжелательностью"), ("padoso", "сильная злоба", "сильной злобой"),
    ("thinaṃ", "вялость", "вялостью"), ("middhaṃ", "сонливость", "сонливостью"),
    ("saññā", "восприятие", "восприятием"), ("uddhaccaṃ", "беспокойство", "беспокойством"),
    ("kukkuccaṃ", "угрызения", "угрызениями"), ("vicikicchā", "колебание", "колебанием"),
    ("kāmā", "чувственные удовольствия", "чувственными удовольствиями"),
    ("akusalā dhammā", "неблагие явления", "неблагими явлениями"),
    ("vitakko", "направленная мысль", "направленной мыслью"), ("vicāro", "удержание мысли", "удержанием мысли"),
    ("pīti", "восторг", "восторгом"), ("sukhaṃ", "счастье", "счастьем"), ("dukkhaṃ", "болезненное", "болезненным"),
    ("somanassaṃ", "радость", "радостью"), ("domanassaṃ", "уныние", "унынием"),
    ("upekkhā", "невозмутимость", "невозмутимостью"), ("kāyo", "тело", "телом"), ("ariyā", "благородные", None),
    ("rūpasaññā", "восприятие материальной формы", None), ("rūpasaññāyo", None, "восприятиями материальной формы"),
    ("paṭighasaññā", "восприятие соударения", None), ("paṭighasaññāyo", None, "восприятиями соударения"),
    ("nānattasaññā", "восприятие разнообразия", None), ("nānattasaññāyo", None, "восприятиями разнообразия"),
    ("ākāso", "пространство", "пространством"),
]:
    if _n:
        NOM[_p] = _n
    if _i:
        INS[_p] = _i
NOM_594 = {"sukhaṃ": "приятное"}          # APPROVED: sukhaṃ of ^2-594 is bodily pleasure («приятное»)
INS_594 = {"sukhaṃ": "приятным"}

# topics: «"X"ti …» (the quoted words of the Suttanta definitions of ch. 12)
TOP = {
    "idhā": "Здесь", "bhikkhū": "Монах", "pātimokkha": "Свод монашеских правил", "saṃvaro": "Сдержанность",
    "saṃvuto": "Сдержанный", "pātimokkhasaṃvarasaṃvuto": "Сдержанный сдержанностью свода монашеских правил",
    "viharatī": "Пребывает",
    "ācāragocarasampanno": "Оснащённый подобающим поведением и подходящим местом посещения",
    "gocaro": "Подходящее место посещения",
    "aṇumattesu vajjesu bhayadassāvī": "Видящий опасность в малейших проступках",
    "samādāya sikkhati sikkhāpadesū": "Приняв на себя правила обучения, обучается им",
    "indriyesu guttadvāro": "Охраняющий врата чувств", "bhojane mattaññū": "Знающий меру в еде",
    "sātacca": "Постоянство", "nepakka": "Благоразумие",
    "bodhipakkhikānaṃ dhammānaṃ bhāvanānuyogamanuyutto": "Предан развитию явлений, способствующих пробуждению",
    "sampajāno": "Ясно понимающий", "vivitta": "Уединённое", "senāsana": "Жилище",
    "vivittaṃ senāsanaṃ bhajatī": "Выбирает уединённое жилище", "arañña": "Лес", "rukkhamūla": "Подножие дерева",
    "vanapattha": "Лесная чаща", "appasadda": "Тихое", "appanigghosa": "Без шума голосов",
    "araññagato vā rukkhamūlagato vā suññāgāragato vā": "Удалившись в лес, или к подножию дерева, или в пустой дом",
    "nisīdati pallaṅkaṃ ābhujitvā": "Садится, скрестив ноги", "ujuṃ kāyaṃ paṇidhāyā": "Поставив тело прямо",
    "parimukhaṃ satiṃ upaṭṭhapetvā": "Установив осознанность перед собой",
    "abhijjhaṃ loke pahāyā": "Оставив алчность в отношении мира",
    "vigatābhijjhena cetasā": "С умом, свободным от алчности",
    "abhijjhāya cittaṃ parisodhetī": "Очищает ум от алчности",
    "byāpādapadosaṃ pahāyā": "Оставив недоброжелательность и сильную злобу",
    "abyāpannacitto": "С умом, свободным от недоброжелательности",
    "byāpādapadosā cittaṃ parisodhetī": "Очищает ум от недоброжелательности и сильной злобы",
    "thinamiddhaṃ pahāyā": "Оставив вялость и сонливость", "vigatathinamiddho": "Свободный от вялости и сонливости",
    "ālokasaññī": "Воспринимающий свет", "sato sampajāno": "Осознанный и ясно понимающий",
    "thinamiddhā cittaṃ parisodhetī": "Очищает ум от вялости и сонливости",
    "uddhaccakukkuccaṃ pahāyā": "Оставив беспокойство и угрызения", "anuddhato": "Без беспокойства",
    "vūpasantacitto": "С успокоенным умом", "ajjhattaṃ vūpasantacitto": "С внутренне успокоенным умом",
    "uddhaccakukkuccā cittaṃ parisodhetī": "Очищает ум от беспокойства и угрызений",
    "vicikicchaṃ pahāyā": "Оставив колебание", "tiṇṇavicikiccho": "Преодолевший колебание",
    "akathaṃkathī kusalesu dhammesū": "Свободный от недоумений в отношении благих явлений",
    "vicikicchāya cittaṃ parisodhetī": "Очищает ум от колебания",
    "ime pañca nīvaraṇe pahāyā": "Оставив эти пять помех", "cetaso upakkilese": "Загрязнения ума",
    "paññāya dubbalīkaraṇe": "Ослабляющие мудрость",
    "vivicceva kāmehi vivicca akusalehi dhammehī": ("Полностью уединившись от чувственных удовольствий, уединившись "
                                                    "от неблагих явлений"),
    "savitakkaṃ savicāra": "С направленной мыслью и удержанием мысли", "vivekaja": "Рождённые уединением",
    "pītisukha": "Восторг и счастье", "jhāna": "Медитативное погружение", "upasampajjā": "Входит",
    "vitakkavicārānaṃ vūpasamā": "С затиханием направленной мысли и удержания мысли", "ajjhatta": "Внутренний",
    "sampasādana": "Ясность", "cetaso ekodibhāva": "Единение ума",
    "avitakkaṃ avicāra": "Без направленной мысли и без удержания мысли", "samādhija": "Рождённые сосредоточением",
    "pītiyā ca virāgā": "С угасанием восторга", "upekkhako": "Невозмутимый", "sato ca sampajāno":
        "Осознанный и ясно понимающий", "sukhañca kāyena paṭisaṃvedetī": "Испытывает телом счастье",
    "yaṃ taṃ ariyā ācikkhantī": "Так что благородные говорят о нём",
    "upekkhako satimā sukhavihārī": "Невозмутимый, осознанный, пребывающий в счастье",
    "sukhassa ca pahānā dukkhassa ca pahānā": "С устранением приятного и с устранением болезненного",
    "pubbeva somanassadomanassānaṃ atthaṅgamā": "С исчезновением ещё прежде радости и уныния",
    "adukkhamasukha": "Которое ни болезненно, ни приятно",
    "upekkhāsatipārisuddhi": "С чистотой невозмутимости и осознанности",
    "sabbaso rūpasaññānaṃ samatikkamā": "С полным преодолением восприятий материальной формы",
    "paṭighasaññānaṃ atthaṅgamā": "С исчезновением восприятий соударения",
    "nānattasaññānaṃ amanasikārā": "Без внимания к восприятиям разнообразия",
    "ananto ākāso": "Пространство бесконечно", "ākāsānañcāyatana": "Сфера бесконечного пространства",
    "sabbaso ākāsānañcāyatanaṃ samatikkammā": "Полностью преодолев сферу бесконечного пространства",
    "anantaṃ viññāṇa": "Сознание бесконечно", "viññāṇañcāyatana": "Сфера бесконечного сознания",
    "sabbaso viññāṇañcāyatanaṃ samatikkammā": "Полностью преодолев сферу бесконечного сознания",
    "natthi kiñcī": "Нет ничего", "ākiñcaññāyatana": "Сфера отсутствия чего-либо",
    "sabbaso ākiñcaññāyatanaṃ samatikkammā": "Полностью преодолев сферу отсутствия чего-либо",
    "nevasaññīnāsaññī": "Ни воспринимающий, ни невоспринимающий",
    "nevasaññānāsaññāyatana": "Сфера ни восприятия, ни невосприятия",
}
for _k, (_n, _i) in JH_ORD.items():
    TOP[_k[:-1]] = cap(_n)                 # "Paṭhama"nti = «Первое»

# =========================================================================== fixed sentences
CALM = {   # santā hoti/honti samitā vūpasantā atthaṅgatā abbhatthaṅgatā appitā byappitā sositā visositā byantīkatā
    "f": ("успокоена, усмирена, умиротворена, угасла, полностью угасла, прекращена, полностью прекращена, иссушена, "
          "полностью иссушена, сведена на нет"),
    "m": ("успокоен, усмирён, умиротворён, угас, полностью угас, прекращён, полностью прекращён, иссушен, полностью "
          "иссушен, сведён на нет"),
    "n": ("успокоено, усмирено, умиротворено, угасло, полностью угасло, прекращено, полностью прекращено, иссушено, "
          "полностью иссушено, сведено на нет"),
    "p": ("успокоены, усмирены, умиротворены, угасли, полностью угасли, прекращены, полностью прекращены, иссушены, "
          "полностью иссушены, сведены на нет"),
}
CALM_SUBJ = {   # Pāli subject of «… santā hoti/honti …» -> (Russian, gender)
    "Ayaṃ abhijjhā imamhi loke": ("Эта алчность в этом мире", "f"),
    "Iti ayañca byāpādo ayañca padoso": ("Итак, эта недоброжелательность и эта сильная злоба", "p"),
    "Iti idañca thinaṃ idañca middhaṃ": ("Итак, эта вялость и эта сонливость", "p"),
    "Iti idañca uddhaccaṃ idañca kukkuccaṃ": ("Итак, это беспокойство и эти угрызения", "p"),
    "Ayaṃ vicikicchā": ("Это колебание", "n"),
    "Ime pañca nīvaraṇā": ("Эти пять помех", "p"),
    "Iti ayañca vitakko ayañca vicāro": ("Итак, эта направленная мысль и это удержание мысли", "p"),
    "Ayaṃ pīti": ("Этот восторг", "m"),
    "Iti idañca sukhaṃ idañca dukkhaṃ": ("Итак, это приятное и это болезненное", "p"),
    "Iti idañca somanassaṃ idañca domanassaṃ pubbeva": ("Итак, эта радость и это уныние ещё прежде", "p"),
    "Imā paṭighasaññāyo": ("Эти восприятия соударения", "p"),
}
SODHETI = "очищает от {x}, тщательно очищает, полностью очищает, освобождает, тщательно освобождает, полностью освобождает"
FROM = {"imāya abhijjhāya": "этой алчности", "imamhā byāpādapadosā": "этой недоброжелательности и сильной злобы",
        "imamhā thinamiddhā": "этих вялости и сонливости", "imamhā uddhaccakukkuccā": "этих беспокойства и угрызений",
        "imāya vicikicchāya": "этого колебания"}
INSTR = {   # <X> upeto hoti … = <X(ins)> он обладает …
    "Iminā pātimokkhasaṃvarena": "Этой сдержанностью свода монашеских правил",
    "Iti iminā ca ācārena iminā ca gocarena": "Итак, этим подобающим поведением и этим подходящим местом посещения",
    "Imāya indriyesu guttadvāratāya": "Этим охранением врат чувств",
    "Imāya bhojane mattaññutāya": "Этим знанием меры в еде",
    "Iti imāya ca satiyā iminā ca sampajaññena": "Итак, этой осознанностью и этим ясным пониманием",
    "Iti iminā ca vitakkena iminā ca vicārena": "Итак, этой направленной мыслью и этим удержанием мысли",
    "Imāya upekkhāya": "Этой невозмутимостью",
}
SAMP_INS = dict(BJ_INS)
SAMP_INS.update({"sattahi bojjhaṅgehi": "семью факторами пробуждения", "aṭṭhaṅgikena maggena": "восьмичастным путём",
                 "pañcaṅgikena maggena": "пятичастным путём", "sammādiṭṭhiyā": "правильным воззрением",
                 "sammāsaṅkappena": "правильным помыслом", "sammāvāyāmena": "правильным усилием",
                 "sammāsatiyā": "правильной осознанностью", "sammāsamādhinā": "правильным сосредоточением",
                 "jhāna": "медитативным погружением"})
ATTHI = {   # Atthi X, atthi Y.
    "ācāro": "подобающее поведение", "anācāro": "неподобающее поведение", "gocaro": "подходящее место посещения",
    "agocaro": "неподходящее место посещения", "indriyesu guttadvāratā": "охранение врат чувств",
    "aguttadvāratā": "неохранение врат чувств", "bhojane mattaññutā": "знание меры в еде",
    "bhojane amattaññutā": "незнание меры в еде", "byāpādo": "недоброжелательность", "padoso": "сильная злоба",
    "thinaṃ": "вялость", "thinaṃ [thīnaṃ (sī. syā.)]": "вялость [вариант написания (Sī., Syā.): thīnaṃ]",
    "middhaṃ": "сонливость", "uddhaccaṃ": "беспокойство", "kukkuccaṃ": "угрызения", "vitakko": "направленная мысль",
    "vicāro": "удержание мысли", "pīti": "восторг", "sukhaṃ": "счастье", "dukkhaṃ": "болезненное",
    "somanassaṃ": "радость", "domanassaṃ": "уныние",
    "ajjhattaṃ dhammesu sati": "осознанность во внутренних явлениях",
    "bahiddhā dhammesu sati": "осознанность во внешних явлениях",
    "ajjhattaṃ dhammesu pavicayo": "тщательное исследование во внутренних явлениях",
    "bahiddhā dhammesu pavicayo": "тщательное исследование во внешних явлениях",
    "kāyikaṃ vīriyaṃ": "телесное усердие", "cetasikaṃ vīriyaṃ": "душевное усердие",
    "savitakkasavicārā pīti": "восторг с направленной мыслью и удержанием мысли",
    "avitakkaavicārā pīti": "восторг без направленной мысли и без удержания мысли",
    "kāyapassaddhi": "безмятежность умственного тела", "cittapassaddhi": "безмятежность ума",
    "kāyapassaddhi [kāyappassaddhi (syā. ka.)]":
        "безмятежность умственного тела [вариант написания (Syā., Ka.): kāyappassaddhi]",
    "cittapassaddhi [cittappassaddhi (syā. ka.)]": "безмятежность ума [вариант написания (Syā., Ka.): cittappassaddhi]",
    "savitakko savicāro samādhi": "сосредоточение с направленной мыслью и удержанием мысли",
    "avitakko avicāro samādhi": "сосредоточение без направленной мысли и без удержания мысли",
    "ajjhattaṃ dhammesu upekkhā": "невозмутимость во внутренних явлениях",
    "bahiddhā dhammesu upekkhā": "невозмутимость во внешних явлениях",
}
ATTHI_594 = {"sukhaṃ": "приятное"}

LISTS = dict(K79.LISTS)    # Yo / Yā / Yaṃ <list> = То, что есть <Russian>
LISTS.update({
    "sati anussati paṭissati sati saraṇatā dhāraṇatā apilāpanatā asammusanatā sati satindriyaṃ satibalaṃ sammāsati":
        SATI_LIST,
    "sati anussati paṭissati…pe… sammāsati": "осознанность, припоминание, воспоминание… правильная осознанность",
    "sati anussati sammāsati satisambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ":
        f"осознанность, припоминание, правильная осознанность, {BJ_RU['sati']}, {PATH_TAIL}",
    ("paññā pajānanā vicayo pavicayo dhammavicayo sallakkhaṇā upalakkhaṇā paccupalakkhaṇā paṇḍiccaṃ kosallaṃ "
     "nepuññaṃ vebhabyā cintā upaparikkhā bhūrīmedhā pariṇāyikā vipassanā sampajaññaṃ patodo paññā paññindriyaṃ "
     "paññābalaṃ paññāsatthaṃ paññāpāsādo paññāāloko paññāobhāso paññāpajjoto paññāratanaṃ amoho dhammavicayo "
     "sammādiṭṭhi"): WISDOM_FULL,
    "pīti pāmojjaṃ āmodanā pamodanā hāso pahāso vitti odagyaṃ attamanatā cittassa": PITI_LIST,
    ("pīti pāmojjaṃ āmodanā pamodanā hāso pahāso vitti odagyaṃ [odaggaṃ (sī.) dha. sa. 9] attamanatā cittassa "
     "pītisambojjhaṅgo"): PITI_LIST.replace("воодушевление,", "воодушевление [вариант написания (Sī.): odaggaṃ; см. "
                                                            "«Перечисление явлений», 9],", 1) + f", {BJ_RU['pīti']}",
    ("vedanākkhandhassa saññākkhandhassa saṅkhārakkhandhassa viññāṇakkhandhassa passaddhi paṭippassaddhi "
     "passambhanā paṭippassambhanā paṭippassambhitattaṃ passaddhisambojjhaṅgo"):
        ("безмятежность совокупности чувств, совокупности восприятия, совокупности формирующих факторов и "
         "совокупности сознания, полная безмятежность, утихание, полное утихание, состояние полного утихания, "
         f"{BJ_RU['passaddhi']}"),
    "upekkhā upekkhanā ajjhupekkhanā majjhattatā cittassa": UPEKKHA_LIST,
    "upekkhā upekkhanā ajjhupekkhanā majjhattatā cittassa upekkhāsambojjhaṅgo": f"{UPEKKHA_LIST}, {BJ_RU['upekkhā']}",
    "paññā pajānanā…pe… amoho dhammavicayo sammādiṭṭhi dhammavicayasambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ":
        K45.WISDOM_PATH,
    "takko vitakko saṅkappo appanā byappanā cetaso abhiniropanā sammāsaṅkappo maggaṅgaṃ maggapariyāpannaṃ":
        f"{VITAKKA_FULL}, {PATH_TAIL}",
    "takko vitakko…pe… sammāsaṅkappo maggaṅgaṃ maggapariyāpannaṃ": f"{K45.VITAKKA_SHORT}… правильный помысел, {PATH_TAIL}",
    "takko vitakko saṅkappo appanā byappanā cetaso abhiniropanā sammāsaṅkappo": VITAKKA_FULL,
    "takko vitakko…pe… sammāsaṅkappo": f"{K45.VITAKKA_SHORT}… правильный помысел",
    "cāro vicāro anuvicāro upavicāro cittassa anusandhanatā anupekkhanatā": VICARA,
    "cāro anucāro vicāro anuvicāro upavicāro cittassa anusandhanatā anupekkhanatā": VICARA_ANU,
    "catūhi vacīduccaritehi ārati virati paṭivirati veramaṇī akiriyā akaraṇaṃ anajjhāpatti velāanatikkamo setughāto "
    "sammāvācā maggaṅgaṃ maggapariyāpannaṃ": ("отстранение от четырёх видов дурного речевого поведения, "
                                              f"{K45.ABSTAIN.format(v='')}, правильная речь, {PATH_TAIL}"),
    "tīhi kāyaduccaritehi ārati virati paṭivirati veramaṇī akiriyā akaraṇaṃ anajjhāpatti velāanatikkamo setughāto "
    "sammākammanto maggaṅgaṃ maggapariyāpannaṃ": ("отстранение от трёх видов дурного телесного поведения, "
                                                  f"{K45.ABSTAIN.format(v='')}, правильное действие, {PATH_TAIL}"),
    "micchāājīvā ārati virati paṭivirati veramaṇī akiriyā akaraṇaṃ anajjhāpatti velāanatikkamo setughāto sammāājīvo "
    "maggaṅgaṃ maggapariyāpannaṃ": (f"отстранение от ложного образа жизни, {K45.ABSTAIN.format(v='')}, правильный "
                                    f"образ жизни, {PATH_TAIL}"),
    ("cittassa ṭhiti saṇṭhiti avaṭṭhiti avisāhāro avikkhepo avisāhaṭamānasatā samatho samādhindriyaṃ samādhibalaṃ "
     "sammāsamādhi samādhisambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ"):
        f"{SAMADHI_LIST}, {BJ_RU['samādhi']}, {PATH_TAIL}",
    "cittassa ṭhiti…pe… sammāsamādhi samādhisambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ":
        f"устойчивость ума… правильное сосредоточение, {BJ_RU['samādhi']}, {PATH_TAIL}",
    "cittassa ṭhiti…pe… sammāsamādhi": "устойчивость ума… правильное сосредоточение",
    "cittaṃ mano mānasaṃ…pe… tajjāmanoviññāṇadhātu": CITTA_PE,
    ("cittassa āghāto paṭighāto paṭighaṃ paṭivirodho kopo pakopo sampakopo doso padoso sampadoso cittassa byāpatti "
     "manopadoso kodho kujjhanā kujjhitattaṃ doso dussanā dussitattaṃ [dūsanā dūsitattaṃ (syā.)] byāpatti byāpajjanā "
     "byāpajjitattaṃ virodho paṭivirodho caṇḍikkaṃ asuropo anattamanatā cittassa"): BYAPADA_V,
    "cittassa āghāto…pe… caṇḍikkaṃ asuropo anattamanatā cittassa": "досада ума… свирепость, грубость, недовольство ума",
    ("cittassa akalyatā akammaññatā olīyanā sallīyanā līnaṃ līyanā līyitattaṃ thinaṃ thiyanā thiyitattaṃ "
     "[thīyanā thīyitattaṃ (sī. syā.)] cittassa"): THINA_V,
    ("kāyassa akalyatā akammaññatā onāho pariyonāho antosamorodho middhaṃ suppaṃ pacalāyikā suppaṃ suppanā "
     "suppitattaṃ"): MIDDHA_P1,
    "cittassa uddhaccaṃ avūpasamo cetaso vikkhepo bhantattaṃ cittassa": UDDHACCA_P1,
    ("kaṅkhā kaṅkhāyanā kaṅkhāyitattaṃ vimati vicikicchā dveḷhakaṃ dvidhāpatho saṃsayo anekaṃsaggāho āsappanā "
     "parisappanā apariyogāhaṇā chambhitattaṃ cittassa manovilekho"): VICIKICCHA,
    "kaṅkhā kaṅkhāyanā kaṅkhāyitattaṃ chambhitattaṃ cittassa manovilekho":
        "сомнение, проявление сомнения, состояние сомнения, оцепенелость ума, терзание ума",
    "saññā sañjānanā sañjānitattaṃ": SANNA_LIST,
    "cetasikaṃ sātaṃ cetasikaṃ sukhaṃ cetosamphassajaṃ sātaṃ sukhaṃ vedayitaṃ cetosamphassajā sātā sukhā vedanā":
        FEEL["somanassa"],
    "cetasikaṃ asātaṃ cetasikaṃ dukkhaṃ cetosamphassajaṃ asātaṃ dukkhaṃ vedayitaṃ cetosamphassajā asātā dukkhā vedanā":
        FEEL["domanassa"],
    "kāyikaṃ sātaṃ kāyikaṃ sukhaṃ kāyasamphassajaṃ sātaṃ sukhaṃ vedayitaṃ kāyasamphassajā sātā sukhā vedanā":
        FEEL["sukha"],
    "kāyikaṃ asātaṃ kāyikaṃ dukkhaṃ kāyasamphassajaṃ asātaṃ dukkhaṃ vedayitaṃ kāyasamphassajā asātā dukkhā vedanā":
        FEEL["dukkha"],
    ("cetasikaṃ neva sātaṃ nāsātaṃ cetosamphassajaṃ adukkhamasukhaṃ vedayitaṃ cetosamphassajā adukkhamasukhā "
     "vedanā"): FEEL["upekkhā"],
    "ākāso ākāsagataṃ aghaṃ aghagataṃ vivaro vivaragataṃ asamphuṭṭhaṃ catūhi mahābhūtehi":
        K23.CORE["ākāsa"].format(by=K23.BY_GREAT),
    "saddhā saddahanā okappanā abhippasādo": SADDHA4,
    "ajjhattaṃ paccattaṃ": "внутреннее, собственное",
})
UPASAMPADA = ("обретение {x}, получение, достижение, полное достижение, касание, непосредственное постижение, "
              "вхождение")    # yo X-assa lābho paṭilābho … upasampadā (K79 IDDHI_DEF wording)
UPA_GEN = {"paṭhamassa jhānassa": "первого медитативного погружения",
           "dutiyassa jhānassa": "второго медитативного погружения",
           "tatiyassa jhānassa": "третьего медитативного погружения",
           "catutthassa jhānassa": "четвёртого медитативного погружения",
           "ākāsānañcāyatanassa": "сферы бесконечного пространства",
           "viññāṇañcāyatanassa": "сферы бесконечного сознания", "ākiñcaññāyatanassa": "сферы отсутствия чего-либо",
           "nevasaññānāsaññāyatanassa": "сферы ни восприятия, ни невосприятия"}
ATTAIN = {"ākāsānañcāyatanaṃ": "сферу бесконечного пространства", "viññāṇañcāyatanaṃ": "сферу бесконечного сознания",
          "ākiñcaññāyatanaṃ": "сферу отсутствия чего-либо",
          "nevasaññānāsaññāyatanaṃ": "сферу ни восприятия, ни невосприятия"}
WHOSE = ("того, кто вошёл в {x}, или того, кто там переродился, или того, кто пребывает в счастье в этой жизни")
# samāpannassa vā upapannassa vā diṭṭhadhammasukhavihārissa vā
ARUPA1 = ("с полным преодолением восприятий материальной формы, с исчезновением восприятий соударения, без внимания к "
          "восприятиям разнообразия, думая: «Пространство бесконечно», входит в сферу бесконечного пространства и "
          "пребывает в ней")
ARUPA2 = ("полностью преодолев сферу бесконечного пространства, думая: «Сознание бесконечно», входит в сферу "
          "бесконечного сознания и пребывает в ней")
ARUPA3 = ("полностью преодолев сферу бесконечного сознания, думая: «Нет ничего», входит в сферу отсутствия чего-либо "
          "и пребывает в ней")
ARUPA4 = ("полностью преодолев сферу отсутствия чего-либо, входит в сферу ни восприятия, ни невосприятия и пребывает "
          "в ней")
JHANAS4 = f"{J1F}, и пребывает в нём; {J2F}, и пребывает в нём; {J3F} и пребывает в нём; {J4F}, и пребывает в нём"
CLEAR = "действует с ясным пониманием"            # sampajānakārī hoti
SATO_CLEAR = "осознанно действует с ясным пониманием"   # sato sampajānakārī hoti (termbase phrase)
SATO = "осознанный и ясно понимающий"              # sato sampajāno
WHEN_CLEAR = [   # the seven occasions of clear comprehension (abhikkante paṭikkante … tuṇhībhāve)
    "идя вперёд и идя назад", "смотря прямо и смотря по сторонам", "сгибая{v} и распрямляя конечности",
    "нося накидку, чашу для подаяния и одежду", "когда ест, пьёт, жуёт и пробует на вкус",
    "справляя большую и малую нужду", "когда ходит, стоит, сидит, засыпает, бодрствует, говорит и молчит"]
CLEAR_LIST = "; ".join(f"{CLEAR}, {w}" for w in WHEN_CLEAR)
SATO_ACTS = ["идёт вперёд", "идёт назад", "смотрит прямо", "смотрит по сторонам", "сгибает конечности",
             "распрямляет конечности"]


def sato_line(last_sato=True):
    """Idha / Evaṃ bhikkhu sato sampajāno abhikkamati, … tuṇhībhāve (sato) sampajānakārī hoti"""
    parts = [f"{SATO}, {a}" for a in SATO_ACTS] + [SATO_CLEAR]
    parts += [f"{SATO_CLEAR}, {w}" for w in WHEN_CLEAR[3:6]]
    parts.append(f"{SATO_CLEAR if last_sato else CLEAR}, {WHEN_CLEAR[6]}")
    return "; ".join(parts)


VAJJA_A = ("Вот человек поддерживает жизнь дарением бамбука, или дарением листьев, или дарением цветов, или дарением "
           "плодов, или дарением мыльного порошка, или дарением зубочисток, или лестью, или угодничеством{v}, или "
           "нянченьем чужих детей, или выполнением поручений на побегушках, или каким-либо иным ложным образом жизни, "
           "порицаемым Буддой")
VAJJA_N = ("Вот человек поддерживает жизнь не дарением бамбука, не дарением листьев, не дарением цветов, не дарением "
           "плодов, не дарением мыльного порошка, не дарением зубочисток, не лестью, не угодничеством, не нянченьем "
           "чужих детей, не выполнением поручений на побегушках, не каким-либо иным ложным образом жизни, порицаемым "
           "Буддой")
AGOCARA = ("Вот человек посещает блудниц, или вдов, или старых дев, или евнухов, или монахинь, или питейные дома; "
           "пребывает в тесном и неподобающем общении с царями, царскими сановниками, иноверцами и учениками "
           "иноверцев; или же посещает, выбирает и почитает такие семьи, которые лишены веры, лишены доверия, не "
           "служат колодцем, бранят и поносят монахов, монахинь, мирян и мирянок, желают им вреда, желают неблага, "
           "желают неудобства, желают, чтобы они лишились безопасности")
GOCARA = ("Вот человек не посещает ни блудниц, ни вдов, ни старых дев, ни евнухов, ни монахинь, ни питейных домов; "
          "не пребывает в тесном и неподобающем общении с царями, царскими сановниками, иноверцами и учениками "
          "иноверцев; или же посещает, выбирает и почитает такие семьи, которые имеют веру, имеют доверие, служат "
          "колодцем, озарены сиянием жёлтых одежд, овеяны дыханием мудрецов, желают монахам, монахиням, мирянам и "
          "мирянкам пользы, желают блага, желают удобства, желают безопасности")
WHY_GONE = "Потому что {x} оставлены, извергнуты, отпущены, устранены, отброшены, устранены и отброшены."
VARIANT = {"[manussarāhaseyyakaṃ (sī. syā.)]": "[вариант написания (Sī., Syā.): manussarāhaseyyakaṃ]",
           "[sammiñjite (sī. syā.)]": "[вариант написания (Sī., Syā.): sammiñjite]"}

SENT = {   # Pāli sentence (as split by K45.split_sents; topics capitalised) = Russian
    # ---- chapter 10
    "Satta bojjhaṅgā – satisambojjhaṅgo, dhammavicayasambojjhaṅgo, vīriyasambojjhaṅgo, pītisambojjhaṅgo, "
    "passaddhisambojjhaṅgo, samādhisambojjhaṅgo, upekkhāsambojjhaṅgo.": SEVEN_LIST,
    "Satta bojjhaṅgā – satisambojjhaṅgo…pe… upekkhāsambojjhaṅgo.": SEVEN_PE,
    "Avasesā dhammā sattahi bojjhaṅgehi sampayuttā.": "Остальные явления связаны с семью факторами пробуждения.",
    # ---- chapter 11
    "Ariyo aṭṭhaṅgiko maggo, seyyathidaṃ – sammādiṭṭhi, sammāsaṅkappo, sammāvācā, sammākammanto, sammāājīvo, "
    "sammāvāyāmo, sammāsati, sammāsamādhi.": NOBLE8,
    "Aṭṭhaṅgiko maggo – sammādiṭṭhi, sammāsaṅkappo, sammāvācā, sammākammanto, sammāājīvo, sammāvāyāmo, sammāsati, "
    "sammāsamādhi.": EIGHT_LIST,
    "Pañcaṅgiko maggo – sammādiṭṭhi, sammāsaṅkappo, sammāvāyāmo, sammāsati, sammāsamādhi.": FIVE_LIST,
    "Aṭṭhaṅgiko maggo – sammādiṭṭhi…pe… sammāsamādhi.": EIGHT_PE,
    "Avasesā dhammā aṭṭhaṅgikena maggena sampayuttā.": "Остальные явления связаны с восьмичастным путём.",
    "Avasesā dhammā pañcaṅgikena maggena sampayuttā.": "Остальные явления связаны с пятичастным путём.",
    # ---- chapter 12, Suttanta: the summary passage (^2-508)
    ("Idha bhikkhu pātimokkhasaṃvarasaṃvuto viharati, ācāragocarasampanno, aṇumattesu vajjesu bhayadassāvī, samādāya "
     "sikkhati sikkhāpadesu indriyesu guttadvāro bhojane mattaññū pubbarattāpararattaṃ jāgariyānuyogamanuyutto "
     "sātaccaṃ nepakkaṃ bodhipakkhikānaṃ dhammānaṃ bhāvanānuyogamanuyutto."):
        (f"{MONK} пребывает сдержанным сдержанностью свода монашеских правил, оснащённым подобающим поведением и "
         "подходящим местом посещения, видящим опасность в малейших проступках; приняв на себя правила обучения, он "
         "обучается им, охраняет врата чувств, знает меру в еде, в начале и в конце ночи предан бодрствованию, с "
         "постоянством и благоразумием предан развитию явлений, способствующих пробуждению."),
    ("So abhikkante paṭikkante sampajānakārī hoti, ālokite vilokite sampajānakārī hoti, samiñjite [sammiñjite (sī. "
     "syā.)] pasārite sampajānakārī hoti, saṅghāṭipattacīvaradhāraṇe sampajānakārī hoti, asite pīte khāyite sāyite "
     "sampajānakārī hoti, uccārapassāvakamme sampajānakārī hoti, gate ṭhite nisinne sutte jāgarite bhāsite "
     "tuṇhībhāve sampajānakārī hoti."):
        "Он " + CLEAR_LIST.format(v=" " + VARIANT["[sammiñjite (sī. syā.)]"]) + ".",
    ("So vivittaṃ senāsanaṃ bhajati araññaṃ rukkhamūlaṃ pabbataṃ kandaraṃ giriguhaṃ susānaṃ vanapatthaṃ abbhokāsaṃ "
     "palālapuñjaṃ appasaddaṃ appanigghosaṃ vijanavātaṃ manussarāhasseyyakaṃ [manussarāhaseyyakaṃ (sī. syā.)] "
     "paṭisallānasāruppaṃ."):
        ("Он выбирает уединённое жилище: лес, подножие дерева, гору, ущелье, горную пещеру, кладбище, лесную чащу, "
         "открытое место, копну соломы, жилище тихое, без шума голосов, лишённое людской суеты, укрытое от людей "
         f"{VARIANT['[manussarāhaseyyakaṃ (sī. syā.)]']}, подходящее для уединения."),
    ("So araññagato vā rukkhamūlagato vā suññāgāragato vā nisīdati pallaṅkaṃ ābhujitvā ujuṃ kāyaṃ paṇidhāya "
     "parimukhaṃ satiṃ upaṭṭhapetvā."):
        ("Удалившись в лес, или к подножию дерева, или в пустой дом, он садится, скрестив ноги, поставив тело прямо, "
         "установив осознанность перед собой."),
    "So abhijjhaṃ loke pahāya vigatābhijjhena cetasā viharati, abhijjhāya cittaṃ parisodheti.":
        ("Оставив алчность в отношении мира, он пребывает с умом, свободным от алчности, очищает ум от алчности."),
    ("Byāpādapadosaṃ pahāya abyāpannacitto viharati sabbapāṇabhūtahitānukampī, byāpādapadosā cittaṃ parisodheti."):
        ("Оставив недоброжелательность и сильную злобу, он пребывает с умом, свободным от недоброжелательности, "
         "сострадающий и желающий блага всем живым существам, очищает ум от недоброжелательности и сильной злобы."),
    "Thinamiddhaṃ pahāya vigatathinamiddho viharati ālokasaññī sato sampajāno, thinamiddhā cittaṃ parisodheti.":
        ("Оставив вялость и сонливость, он пребывает свободным от вялости и сонливости, воспринимающим свет, "
         "осознанным и ясно понимающим, очищает ум от вялости и сонливости."),
    ("Uddhaccakukkuccaṃ pahāya anuddhato viharati ajjhattaṃ vūpasantacitto, uddhaccakukkuccā cittaṃ "
     "parisodheti."):
        ("Оставив беспокойство и угрызения, он пребывает без беспокойства, с внутренне успокоенным умом, очищает ум "
         "от беспокойства и угрызений."),
    "Vicikicchaṃ pahāya tiṇṇavicikiccho viharati akathaṃkathī kusalesu dhammesu, vicikicchāya cittaṃ parisodheti.":
        ("Оставив колебание, он пребывает преодолевшим колебание, свободным от недоумений в отношении благих "
         "явлений, очищает ум от колебания."),
    ("So ime pañca nīvaraṇe pahāya cetaso upakkilese paññāya dubbalīkaraṇe vivicceva kāmehi vivicca akusalehi "
     "dhammehi savitakkaṃ savicāraṃ vivekajaṃ pītisukhaṃ paṭhamaṃ jhānaṃ upasampajja viharati; vitakkavicārānaṃ "
     "vūpasamā ajjhattaṃ sampasādanaṃ cetaso ekodibhāvaṃ avitakkaṃ avicāraṃ samādhijaṃ pītisukhaṃ dutiyaṃ jhānaṃ "
     "upasampajja viharati; pītiyā ca virāgā upekkhako ca viharati sato ca sampajāno sukhañca kāyena "
     "paṭisaṃvedeti, yaṃ taṃ ariyā ācikkhanti – \"upekkhako satimā sukhavihārī\"ti tatiyaṃ jhānaṃ upasampajja "
     "viharati; sukhassa ca pahānā dukkhassa ca pahānā pubbeva somanassadomanassānaṃ atthaṅgamā adukkhamasukhaṃ "
     "upekkhāsatipārisuddhiṃ catutthaṃ jhānaṃ upasampajja viharati; sabbaso rūpasaññānaṃ samatikkamā "
     "paṭighasaññānaṃ atthaṅgamā nānattasaññānaṃ amanasikārā \"ananto ākāso\"ti ākāsānañcāyatanaṃ upasampajja "
     "viharati; sabbaso ākāsānañcāyatanaṃ samatikkamma \"anantaṃ viññāṇa\"nti viññāṇañcāyatanaṃ upasampajja "
     "viharati; sabbaso viññāṇañcāyatanaṃ samatikkamma \"natthi kiñcī\"ti ākiñcaññāyatanaṃ upasampajja viharati; sabbaso "
     "ākiñcaññāyatanaṃ samatikkamma nevasaññānāsaññāyatanaṃ upasampajja viharati."):
        (f"Оставив эти пять помех, загрязнения ума, ослабляющие мудрость, он, {JHANAS4}; {ARUPA1}; {ARUPA2}; "
         f"{ARUPA3}; {ARUPA4}."),
    # ---- definitions
    ("Imissā diṭṭhiyā, imissā khantiyā, imissā ruciyā, imasmiṃ ādāye, imasmiṃ dhamme, imasmiṃ vinaye, imasmiṃ "
     "dhammavinaye, imasmiṃ pāvacane, imasmiṃ brahmacariye, imasmiṃ satthusāsane."):
        ("В этом воззрении, в этом приятии, в этом предпочтении, в этом выборе, в этом Учении, в этой дисциплине, "
         "в этом Учении и дисциплине, в этом слове, в этой святой жизни, в этом наставлении Учителя."),
    ("Samaññāya bhikkhu, paṭiññāya bhikkhu, bhikkhatīti bhikkhu, bhikkhakoti bhikkhu, bhikkhācariyaṃ ajjhupagatoti "
     "bhikkhu, bhinnapaṭadharoti bhikkhu, bhindati pāpake akusale dhammeti bhikkhu, bhinnattā pāpakānaṃ akusalānaṃ "
     "dhammānaṃ bhikkhu, odhiso kilesānaṃ pahānā bhikkhu, anodhiso kilesānaṃ pahānā bhikkhu, sekkho bhikkhu, asekkho "
     "bhikkhu, nevasekkhanāsekkho bhikkhu, aggo bhikkhu, bhadro bhikkhu, maṇḍo bhikkhu, sāro bhikkhu, samaggena "
     "saṅghena ñatticatutthena kammena akuppena ṭhānārahena upasampanno bhikkhu."):
        ("Монах по общепринятому названию; монах по собственному заявлению; монах, потому что просит подаяние; "
         "монах, потому что живёт подаянием; монах, потому что избрал жизнь на подаянии;монах, потому что носит "
         "одежду из лоскутов; монах, потому что разрушает дурные неблагие явления; монах, потому что дурные "
         "неблагие явления у него разрушены; монах благодаря частичному устранению омрачений; монах благодаря "
         "полному устранению омрачений; монах, относящийся к обучающимся; монах, относящийся к завершившим "
         "обучение; монах, не относящийся ни к обучающимся, ни к завершившим обучение; превосходный монах; хороший "
         "монах; отборный монах; монах, являющийся сердцевиной; монах, получивший полное посвящение от единой "
         "общины посредством неотменимой и соответствующей правилам процедуры с предложением и тремя объявлениями."),
    "Sīlaṃ patiṭṭhā ādi caraṇaṃ saṃyamo saṃvaro mokkhaṃ pāmokkhaṃ kusalānaṃ dhammānaṃ samāpattiyā.":
        ("Нравственность, опора, начало, поведение, обуздание, сдержанность, главное, первейшее для достижения "
         "благих явлений."),
    "Kāyiko avītikkamo, vācasiko avītikkamo, kāyikavācasiko avītikkamo.":
        "Отсутствие нарушений телом, отсутствие нарушений речью, отсутствие нарушений телом и речью.",
    "Sabbampi dussīlyaṃ anācāro.": "Всякая безнравственность является неподобающим поведением.",
    "Sabbopi sīlasaṃvaro ācāro.": "Всякая нравственная сдержанность является подобающим поведением.",
    ("Iti imesu aṇumattesu vajjesu vajjadassāvī ca hoti bhayadassāvī ca ādīnavadassāvī ca nissaraṇadassāvī ca."):
        "Итак, в этих малейших проступках он видит проступок, видит опасность, видит вред и видит выход.",
    ("Catasso sikkhā – bhikkhūnaṃ bhikkhusikkhā, bhikkhunīnaṃ bhikkhunisikkhā, upāsakānaṃ upāsakasikkhā, "
     "upāsikānaṃ upāsikasikkhā."):
        ("Четыре вида обучения – обучение монахов для монахов, обучение монахинь для монахинь, обучение мирян для "
         "мирян и обучение мирянок для мирянок."),
    "Iti imāsu sikkhāsu sabbena sabbaṃ sabbathā sabbaṃ asesaṃ nissesaṃ samādāya vattati.":
        ("Итак, приняв на себя эти виды обучения всецело, во всех отношениях, без остатка, полностью, он следует "
         "им."),
    "Atthi indriyesu guttadvāratā, atthi aguttadvāratā.": "Есть охранение врат чувств, есть неохранение врат чувств.",
    "Kathañca bhikkhu pubbarattāpararattaṃ jāgariyānuyogamanuyutto hoti?":
        "И как монах в начале и в конце ночи предан бодрствованию?",
    ("Idha bhikkhu divasaṃ caṅkamena nisajjāya āvaraṇīyehi dhammehi cittaṃ parisodheti, rattiyā paṭhamayāmaṃ "
     "caṅkamena nisajjāya āvaraṇīyehi dhammehi cittaṃ parisodheti, rattiyā majjhimayāmaṃ dakkhiṇena passena "
     "sīhaseyyaṃ kappeti pāde pādaṃ [pādena pādaṃ (syā.)] accādhāya sato sampajāno uṭṭhānasaññaṃ manasikaritvā, "
     "rattiyā pacchimayāmaṃ paccuṭṭhāya caṅkamena nisajjāya āvaraṇīyehi dhammehi cittaṃ parisodheti."):
        (f"{MONK} днём хождением и сидением очищает ум от явлений, создающих препятствия; в первую стражу ночи "
         "хождением и сидением очищает ум от явлений, создающих препятствия; в среднюю стражу ночи ложится на "
         "правый бок в позе лежащего льва, положив ступню на ступню [вариант чтения (Syā.): pādena pādaṃ], осознанный и ясно "
         "понимающий, уделив внимание мысли о вставании; в последнюю стражу ночи, встав, хождением и сидением "
         "очищает ум от явлений, создающих препятствия."),
    "Evaṃ bhikkhu pubbarattāpararattaṃ jāgariyānuyogamanuyutto.":
        "Так монах в начале и в конце ночи предан бодрствованию.",
    "Tattha katame bodhipakkhikā dhammā?": f"Что такое {S.TATTHA} явления, способствующие пробуждению?",
    "Iti te bodhipakkhike dhamme āsevati bhāveti bahulīkaroti.":
        "Итак, эти явления, способствующие пробуждению, он практикует, развивает, многократно повторяет.",
    ("Kathañca bhikkhu abhikkante paṭikkante sampajānakārī hoti, ālokite vilokite sampajānakārī hoti, samiñjite "
     "pasārite sampajānakārī hoti, saṅghāṭipattacīvaradhāraṇe sampajānakārī hoti, asite pīte khāyite sāyite "
     "sampajānakārī hoti, uccārapassāvakamme sampajānakārī hoti; gate ṭhite nisinne sutte jāgarite bhāsite "
     "tuṇhībhāve sampajānakārī hoti?"):
        "И как монах " + CLEAR_LIST.format(v="") + "?",
    ("Idha bhikkhu sato sampajāno abhikkamati, sato sampajāno paṭikkamati, sato sampajāno āloketi, sato sampajāno "
     "viloketi, sato sampajāno samiñjeti, sato sampajāno pasāreti, sato sampajānakārī hoti, "
     "saṅghāṭipattacīvaradhāraṇe sato sampajānakārī hoti, asite pīte khāyite sāyite sato sampajānakārī hoti, "
     "uccārapassāvakamme sato sampajānakārī hoti, gate ṭhite nisinne sutte jāgarite bhāsite tuṇhībhāve sato "
     "sampajānakārī hotīti."): f"{MONK}, {sato_line()}.",
    ("Evaṃ bhikkhu sato sampajāno abhikkamati, sato sampajāno paṭikkamati, sato sampajāno āloketi, sato sampajāno "
     "viloketi, sato sampajāno samiñjeti, sato sampajāno pasāreti, sato sampajānakārī hoti, "
     "saṅghāṭipattacīvaradhāraṇe sato sampajānakārī hoti, asite pīte khāyite sāyite sato sampajānakārī hoti, "
     "uccārapassāvakamme sato sampajānakārī hoti, gate ṭhite nisinne sutte jāgarite bhāsite tuṇhībhāve "
     "sampajānakārī hoti."): f"Так монах, {sato_line(last_sato=False)}.",
    "Santike cepi senāsanaṃ hoti, tañca anākiṇṇaṃ gahaṭṭhehi pabbajitehi.":
        "Даже если жилище находится вблизи, оно не заполнено домохозяевами и ушедшими в бездомность.",
    "Dūre cepi senāsanaṃ hoti, tañca anākiṇṇaṃ gahaṭṭhehi pabbajitehi.":
        "Даже если жилище находится вдали, оно не заполнено домохозяевами и ушедшими в бездомность.",
    "Tena taṃ vivittaṃ.": "Поэтому оно уединённое.",
    "Tena taṃ appasaddaṃ.": "Поэтому оно тихое.",
    ("Mañcopi senāsanaṃ, pīṭhampi senāsanaṃ, bhisipi senāsanaṃ, bibbohanampi [bimbohanampi (sī. syā.)] senāsanaṃ, "
     "vihāropi senāsanaṃ, aḍḍhayogopi senāsanaṃ, pāsādopi senāsanaṃ, aṭṭopi senāsanaṃ, māḷopi senāsanaṃ, leṇampi "
     "senāsanaṃ, guhāpi senāsanaṃ, rukkhamūlampi senāsanaṃ, veḷugumbopi senāsanaṃ."):
        ("Ложе тоже является жилищем, сиденье тоже является жилищем, матрас тоже является жилищем, подушка "
         "[вариант написания (Sī., Syā.): bimbohanampi] тоже является жилищем, обитель тоже является жилищем, навес "
         "тоже является жилищем, дворец тоже является жилищем, башня тоже является жилищем, дом с островерхой "
         "крышей тоже является жилищем, скальная келья тоже является жилищем, пещера тоже является жилищем, "
         "подножие дерева тоже является жилищем, бамбуковая роща тоже является жилищем."),
    "Yattha vā pana bhikkhū paṭikkamanti sabbametaṃ senāsanaṃ.":
        "Где бы ни останавливались монахи, всё это является жилищем.",
    "Imaṃ vivittaṃ senāsanaṃ bhajati sambhajati sevati nisevati saṃsevati.":
        "Это уединённое жилище он выбирает, занимает, посещает, часто посещает, постоянно посещает.",
    "Nikkhamitvā bahi indakhīlā sabbametaṃ araññaṃ.":
        "Всё, что лежит за пределами пограничного столба, если выйти наружу, является лесом.",
    "Rukkhamūlaṃyeva rukkhamūlaṃ.": "Подножие дерева и есть подножие дерева.",
    "Pabbatoyeva pabbato.": "Гора и есть гора.",
    "Kandarāyeva kandarā.": "Ущелье и есть ущелье.",
    "Giriguhāyeva giriguhā.": "Горная пещера и есть горная пещера.",
    "Susānaṃyeva susānaṃ.": "Кладбище и есть кладбище.",
    "Abbhokāsoyeva abbhokāso.": "Открытое место и есть открытое место.",
    "Palālapuñjoyeva palālapuñjo.": "Копна соломы и есть копна соломы.",
    "Dūrānametaṃ senāsanānaṃ adhivacanaṃ.": "Это наименование отдалённых жилищ.",
    "Vanasaṇḍānametaṃ senāsanānaṃ adhivacanaṃ.": "Это наименование лесных жилищ.",
    "Bhīsanakānametaṃ [bhiṃsanakānametaṃ (sī. syā.)] senāsanānaṃ adhivacanaṃ.":
        "Это наименование пугающих [вариант написания (Sī., Syā.): bhiṃsanakānametaṃ] жилищ.",
    "Salomahaṃsānametaṃ senāsanānaṃ adhivacanaṃ.": "Это наименование наводящих трепет жилищ.",
    "Pariyantānametaṃ senāsanānaṃ adhivacanaṃ.": "Это наименование жилищ, находящихся на окраине.",
    "Na manussūpacārānametaṃ senāsanānaṃ adhivacanaṃ.": "Это наименование жилищ, не являющихся людскими местами.",
    "Durabhisambhavānametaṃ senāsanānaṃ adhivacanaṃ.": "Это наименование труднодоступных жилищ.",
    "Yadeva taṃ appasaddaṃ tadeva taṃ appanigghosaṃ.": "Что тихое, то и без шума голосов.",
    "Yadeva taṃ appanigghosaṃ tadeva taṃ vijanavātaṃ.": "Что без шума голосов, то и лишённое людской суеты.",
    "Yadeva taṃ vijanavātaṃ tadeva taṃ manussarāhasseyyakaṃ.": "Что лишённое людской суеты, то и укрытое от людей.",
    "Yadeva taṃ manussarāhasseyyakaṃ tadeva taṃ paṭisallānasāruppaṃ.":
        "Что укрытое от людей, то и подходящее для уединения.",
    "Araññagato vā hoti rukkhamūlagato vā suññāgāragato vā.": "Он удалился в лес, или к подножию дерева, или в пустой дом.",
    "Nisinno hoti pallaṅkaṃ ābhujitvā.": "Он сидит, скрестив ноги.",
    "Ujuko hoti kāyo ṭhito paṇihito.": "Тело прямое, устойчивое, правильно поставленное.",
    "Ayaṃ sati upaṭṭhitā hoti supaṭṭhitā nāsikagge vā mukhanimitte vā.":
        "Эта осознанность установлена, хорошо установлена у кончика носа или в области рта.",
    "Idaṃ cittaṃ vigatābhijjhaṃ hoti.": "Этот ум свободен от алчности.",
    "Yo byāpādo so padoso, yo padoso so byāpādo.":
        "Недоброжелательность и есть сильная злоба, сильная злоба и есть недоброжелательность.",
    "Idaṃ cittaṃ abyāpannaṃ hoti.": "Этот ум свободен от недоброжелательности.",
    "Tassa thinamiddhassa cattattā vantattā muttattā pahīnattā paṭinissaṭṭhattā pahīnapaṭinissaṭṭhattā.":
        WHY_GONE.format(x="его вялость и сонливость"),
    "Tassa uddhaccakukkuccassa cattattā vantattā muttattā pahīnattā paṭinissaṭṭhattā pahīnapaṭinissaṭṭhattā.":
        WHY_GONE.format(x="его беспокойство и угрызения"),
    "Ayaṃ saññā ālokā hoti vivaṭā parisuddhā pariyodātā.": "Это восприятие светлое, открытое, чистое, ясное.",
    "Idaṃ cittaṃ ajjhattaṃ santaṃ hoti samitaṃ vūpasantaṃ.": "Этот ум внутренне успокоен, усмирён, умиротворён.",
    "Imaṃ vicikicchaṃ tiṇṇo hoti uttiṇṇo nittiṇṇo pāraṅgato pāramanuppatto.":
        ("Это колебание он преодолел, превозмог, полностью превозмог, переправился через него на другой берег, "
         "достиг другого берега."),
    ("Imāya vicikicchāya kusalesu dhammesu na kaṅkhati na vicikicchati akathaṃkathī hoti nikkathaṃkathī "
     "vikathaṃkatho."):
        ("Он не сомневается и не колеблется этим колебанием в отношении благих явлений, свободен от недоумений, "
         "полностью свободен от недоумений, избавлен от недоумений."),
    "Ime pañca nīvaraṇā cittassa upakkilesā.": "Эти пять помех являются загрязнениями ума.",
    "Imehi pañcahi nīvaraṇehi anuppannā ceva paññā na uppajjati uppannā ca paññā nirujjhati.":
        "Из-за этих пяти помех невозникшая мудрость не возникает, а возникшая мудрость прекращается.",
    "Iti imehi ca kāmehi imehi ca akusalehi dhammehi vivitto hoti.":
        "Итак, от этих чувственных удовольствий и от этих неблагих явлений он уединён.",
    ("Vitakko, vicāro, pīti, sukhaṃ, cittassekaggatā – te imasmiṃ viveke jātā honti sañjātā nibbattā abhinibbattā "
     "pātubhūtā."):
        ("Направленная мысль, удержание мысли, восторг, счастье, однонаправленность ума – они в этом уединении "
         "рождены, зародились, появились, полностью появились, проявились."),
    "Idaṃ sukhaṃ imāya pītiyā sahagataṃ hoti sahajātaṃ saṃsaṭṭhaṃ sampayuttaṃ.":
        "Это счастье сопровождается этим восторгом, рождено вместе с ним, соединено с ним, связано с ним.",
    "Gaṇanānupubbatā [gaṇanānupubbato (syā.) evamuparipi] paṭhamaṃ.":
        "Первое по порядку счёта [вариант написания (Syā.): gaṇanānupubbato, так же и далее].",
    "Gaṇanānupubbatā dutiyaṃ.": "Второе по порядку счёта.",
    "Gaṇanānupubbatā tatiyaṃ.": "Третье по порядку счёта.",
    "Gaṇanānupubbatā catutthaṃ, idaṃ catutthaṃ samāpajjatīti catutthaṃ.":
        "Четвёртое по порядку счёта, четвёртое, потому что в него входят четвёртым.",
    "Vitakko, vicāro, pīti, sukhaṃ, cittassekaggatā.":
        "Направленная мысль, удержание мысли, восторг, счастье, однонаправленность ума.",
    "Sampasādo, pītisukhaṃ, cittassekaggatā.": "Ясность, восторг и счастье, однонаправленность ума.",
    "Upekkhā, sati, sampajaññaṃ, sukhaṃ, cittassekaggatā.":
        "Невозмутимость, осознанность, ясное понимание, счастье, однонаправленность ума.",
    "Upekkhā, sati, cittassekaggatā.": "Невозмутимость, осознанность, однонаправленность ума.",
    ("Sampasādo pītisukhaṃ – te imasmiṃ samādhimhi jātā honti sañjātā nibbattā abhinibbattā pātubhūtā."):
        ("Ясность, восторг и счастье – они в этом сосредоточении рождены, зародились, появились, полностью "
         "появились, проявились."),
    "Ariyā vuccanti buddhā ca buddhasāvakā ca.": "Благородными называются будды и ученики будд.",
    ("Te imaṃ ācikkhanti desenti paññapenti [paññāpenti (sī. syā.)] paṭṭhapenti vivaranti vibhajanti uttāniṃ "
     "karonti pakāsenti."):
        ("Они говорят об этом, излагают, провозглашают [вариант написания (Sī., Syā.): paññāpenti], устанавливают, "
         "раскрывают, разбирают, проясняют, разъясняют."),
    "Idaṃ sukhaṃ iminā kāyena paṭisaṃvedeti.": "Это счастье он испытывает этим телом.",
    ("Iti imāya ca upekkhāya imāya ca satiyā iminā ca sukhena samannāgato iriyati vattati pāleti yapeti yāpeti "
     "carati viharati."):
        ("Итак, наделённый этой невозмутимостью, этой осознанностью и этим счастьем, он " + low(IRIYATI)),
    "Ayaṃ sati imāya upekkhāya vivaṭā hoti parisuddhā pariyodātā.":
        "Эта осознанность благодаря этой невозмутимости открыта, чиста, ясна.",
    "Imā rūpasaññāyo atikkanto hoti vītikkanto samatikkanto.":
        "Эти восприятия материальной формы он преодолел, миновал, полностью преодолел.",
    "Imā nānattasaññāyo na manasi karoti.": "Этим восприятиям разнообразия он не уделяет внимания.",
    "Tasmiṃ ākāse cittaṃ ṭhapeti saṇṭhapeti anantaṃ pharati.":
        "В этом пространстве он устанавливает ум, прочно устанавливает, наполняет его как бесконечное.",
    "Taṃyeva ākāsaṃ viññāṇena phuṭṭhaṃ manasi karoti anantaṃ pharati.":
        "Тому самому пространству, охваченному сознанием, он уделяет внимание, наполняет его как бесконечное.",
    "Taṃyeva viññāṇaṃ bhāveti vibhāveti antarabhāveti, \"natthi kiñcī\"ti passati.":
        "То самое сознание он развивает, рассеивает, заставляет исчезнуть, видит: «Нет ничего».",
    "Taṃyeva ākiñcaññāyatanaṃ santato manasi karoti saṅkhārāvasesasamāpattiṃ bhāveti.":
        ("Той самой сфере отсутствия чего-либо он уделяет внимание как спокойной, развивает медитативное "
         "достижение с остатком формирующих факторов."),
    "Tena vuccati \"nevasaññīnāsaññī\"ti [ayaṃ pāṭho mātikāyaṃ natthi, niddese pana sabbapotthakesu dissati].":
        (f"{TENA} «{TOP['nevasaññīnāsaññī']}» [этого чтения нет в матрице, но в разъяснении оно встречается во всех "
         "рукописях]."),
    # ---- chapter 12, Abhidhamma
    "Cattāri jhānāni – paṭhamaṃ jhānaṃ, dutiyaṃ jhānaṃ, tatiyaṃ jhānaṃ, catutthaṃ jhānaṃ.": FOUR_JH,
    "Catukkaṃ.": "Четверичный метод.",
    "Pañcakaṃ.": "Пятеричный метод.",
    "Ime dhammā kusalā.": ALL_THIS,
    # ---- chapter 12, Pañhāpucchaka opener
    ("Cattāri jhānāni – idha bhikkhu vivicceva kāmehi vivicca akusalehi dhammehi savitakkaṃ savicāraṃ vivekajaṃ "
     "pītisukhaṃ paṭhamaṃ jhānaṃ upasampajja viharati…pe… vitakkavicārānaṃ vūpasamā ajjhattaṃ sampasādanaṃ cetaso "
     "ekodibhāvaṃ avitakkaṃ avicāraṃ samādhijaṃ pītisukhaṃ dutiyaṃ jhānaṃ upasampajja viharati…pe… pītiyā ca virāgā "
     "upekkhako ca viharati sato ca sampajāno sukhañca kāyena paṭisaṃvedeti, yaṃ taṃ ariyā ācikkhanti – "
     "\"upekkhako satimā sukhavihārī\"ti tatiyaṃ jhānaṃ upasampajja viharati…pe… sukhassa ca pahānā dukkhassa ca "
     "pahānā pubbeva somanassadomanassānaṃ atthaṅgamā adukkhamasukhaṃ upekkhāsatipārisuddhiṃ catutthaṃ jhānaṃ "
     "upasampajja viharati."):
        (f"Четыре медитативных погружения – здесь монах, {J1F}, и пребывает в нём… {J2F}, и пребывает в нём… {J3F} "
         f"и пребывает в нём… {J4F}, и пребывает в нём."),
    # ---- closing labels
    "Suttantabhājanīyaṃ.": f"{S.SUTTANTA_BH}.", "Abhidhammabhājanīyaṃ.": f"{S.ABHI_BH}.",
    "Pañhāpucchakaṃ.": f"{S.PANHA}.",
    "Bojjhaṅgavibhaṅgo niṭṭhito.": f"{S.CH_TITLE[10][1]} {S.DONE}.",
    "Maggaṅgavibhaṅgo niṭṭhito.": f"{S.CH_TITLE[11][1]} {S.DONE}.",
    "Jhānavibhaṅgo niṭṭhito.": f"{S.CH_TITLE[12][1]} {S.DONE}.",
}
SENT_SLIP = {   # source slips (Pāli as meant, note)
    "Ñatvādhikaraṇamenaṃ": ("Yatvādhikaraṇamenaṃ",
                            "^2-517 «Ñatvādhikaraṇamenaṃ» (for Yatvādhikaraṇamenaṃ, as in the eye clause and pi-1 "
                            "^1-1354): rendered as meant"),
    "ākiñcāyatanaṃ upasampajja": ("ākiñcaññāyatanaṃ upasampajja",
                                  "^2-508 «ākiñcāyatanaṃ» (for ākiñcaññāyatanaṃ): rendered as meant"),
}
BODY = {   # answers «<body> – ayaṃ vuccati "X".» (non-«Yo/Yā/Yaṃ» bodies): body -> (Russian, comma before the dash)
    # ---- ch. 10 (^2-467)
    "Idha bhikkhu satimā hoti paramena satinepakkena samannāgato, cirakatampi cirabhāsitampi saritā hoti anussaritā":
        (f"{MONK} осознан, наделён высшей осознанностью и благоразумием, помнит и припоминает даже то, что было "
         "сделано давно, и то, что было сказано давно", True),
    "So tathā sato viharanto taṃ dhammaṃ paññāya pavicinati pavicarati parivīmaṃsamāpajjati":
        ("Пребывая так осознанным, он исследует это явление мудростью, обдумывает его, подвергает его всестороннему "
         "изучению", False),
    "Tassa taṃ dhammaṃ paññāya pavicinato pavicarato parivīmaṃsamāpajjato āraddhaṃ hoti vīriyaṃ asallīnaṃ":
        ("Когда он исследует это явление мудростью, обдумывает его, подвергает его всестороннему изучению, у него "
         "пробуждено неослабное усердие", False),
    "Āraddhavīriyassa uppajjati pīti nirāmisā": ("У того, кто пробудил усердие, возникает неплотский восторг", False),
    "Pītimanassa kāyopi passambhati, cittampi passambhati":
        ("У того, чей ум полон восторга, утихает и тело, утихает и ум", False),
    "Passaddhakāyassa sukhino cittaṃ samādhiyati":
        ("У того, чьё тело утихло и кто счастлив, ум сосредотачивается", False),
    "So tathā samāhitaṃ cittaṃ sādhukaṃ ajjhupekkhitā hoti":
        ("Он хорошо взирает с полной невозмутимостью на так сосредоточенный ум", False),
    "Kāyiko vītikkamo, vācasiko vītikkamo, kāyikavācasiko vītikkamo":
        ("Нарушение телом, нарушение речью, нарушение телом и речью", False),
    "Kāyiko avītikkamo, vācasiko avītikkamo, kāyikavācasiko avītikkamo":
        ("Отсутствие нарушений телом, отсутствие нарушений речью, отсутствие нарушений телом и речью", False),
    ("Idhekacco veḷudānena vā pattadānena vā pupphadānena vā phaladānena vā sinānadānena vā dantakaṭṭhadānena vā "
     "cāṭukamyatāya vā muggasūpyatāya [muggasuppatāya (sī.)] vā pāribhaṭayatāya vā jaṅghapesanikena vā "
     "aññataraññatarena vā buddhapaṭikuṭṭhena micchāājīvena jīvikaṃ kappeti"):
        (VAJJA_A.format(v=" [вариант написания (Sī.): muggasuppatāya]"), True),
    ("Idhekacco na veḷudānena na pattadānena na pupphadānena na phaladānena na sinānadānena na dantakaṭṭhadānena na "
     "cāṭukamyatāya na muggasūpyatāya na pāribhaṭayatāya na jaṅghapesanikena na aññataraññatarena buddhapaṭikuṭṭhena "
     "micchāājīvena jīvikaṃ kappeti"): (VAJJA_N, True),
    ("Idhekacco vesiyāgocaro vā hoti vidhavāgocaro vā thullakumārigocaro vā paṇḍakagocaro vā bhikkhunigocaro vā "
     "pānāgāragocaro vā, saṃsaṭṭho viharati rājūhi rājamahāmattehi titthiyehi titthiyasāvakehi ananulomikena "
     "saṃsaggena; yāni vā pana tāni kulāni assaddhāni appasannāni anopānabhūtāni akkosakaparibhāsakāni "
     "anatthakāmāni ahitakāmāni aphāsukakāmāni ayogakkhemakāmāni bhikkhūnaṃ bhikkhunīnaṃ upāsakānaṃ upāsikānaṃ, "
     "tathārūpāni kulāni sevati bhajati payirupāsati"): (AGOCARA, True),
    ("Idhekacco na vesiyāgocaro hoti na vidhavāgocaro na thullakumārigocaro na paṇḍakagocaro na bhikkhunigocaro na "
     "pānāgāragocaro, asaṃsaṭṭho viharati rājūhi rājamahāmattehi titthiyehi titthiyasāvakehi ananulomikena "
     "saṃsaggena; yāni vā pana tāni kulāni saddhāni pasannāni opānabhūtāni kāsāvapajjotāni isivātapaṭivātāni "
     "atthakāmāni hitakāmāni phāsukakāmāni yogakkhemakāmāni bhikkhūnaṃ bhikkhunīnaṃ upāsakānaṃ upāsikānaṃ, "
     "tathārūpāni kulāni sevati bhajati payirupāsati"): (GOCARA, True),
    ("Yāni tāni vajjāni appamattakāni oramattakāni lahusāni lahusammatāni saṃyamakaraṇīyāni saṃvarakaraṇīyāni "
     "cittuppādakaraṇīyāni manasikārapaṭibaddhāni"):
        ("Те проступки, которые незначительны, мелки, лёгки, считаются лёгкими, исправляются обузданием, "
         "исправляются сдержанностью, исправляются решением ума, связаны со вниманием", True),
    "Pañcupādānakkhandhā loko": ("Пять совокупностей, служащих объектом цепляния, являются миром", False),
    ("Akappiye kappiyasaññitā, kappiye akappiyasaññitā, avajje vajjasaññitā, vajje avajjasaññitā, yaṃ evarūpaṃ "
     "kukkuccaṃ kukkuccāyanā kukkuccāyitattaṃ cetaso vippaṭisāro manovilekhā"):
        (f"{KUKKUCCA_A}; то, что есть {KUKKUCCA_B}", True),
    "Chando kāmo, rāgo kāmo, chandarāgo kāmo, saṅkappo kāmo, rāgo kāmo, saṅkapparāgo kāmo":
        ("Желание является чувственным удовольствием, страсть является чувственным удовольствием, страстное желание "
         "является чувственным удовольствием, помысел является чувственным удовольствием, страсть является "
         "чувственным удовольствием, страсть к помыслам является чувственным удовольствием", False),
    "Kāmacchando, byāpādo, thinaṃ, middhaṃ, uddhaccaṃ, kukkuccaṃ, vicikicchā":
        ("Чувственное желание, недоброжелательность, вялость, сонливость, беспокойство, угрызения, колебание", False),
    "Saññākkhandho, saṅkhārakkhandho, viññāṇakkhandho": (cap(K6.KH3_SNV), False),
    ("Rūpāvacarasamāpattiṃ samāpannassa vā upapannassa vā diṭṭhadhammasukhavihārissa vā saññā sañjānanā "
     "sañjānitattaṃ"):
        (f"{cap(SANNA_LIST)} " + WHOSE.format(x="медитативное достижение, относящееся к миру форм"), True),
    "Rūpasaññā saddasaññā…pe… phoṭṭhabbasaññā": ("Восприятие видимых форм, восприятие звуков… восприятие осязаемого",
                                                 False),
    ("Asamāpannassa manodhātu samaṅgissa vā manoviññāṇadhātu samaṅgissa vā saññā sañjānanā sañjānitattaṃ"):
        (f"{cap(SANNA_LIST)} того, кто не вошёл в медитативное достижение и обладает элементом ума или обладает "
         "элементом умственного сознания", True),
}
BODY.update({k: v for k, v in K45.BODY.items() if k in (
    "Dukkhe ñāṇaṃ, dukkhasamudaye ñāṇaṃ, dukkhanirodhe ñāṇaṃ, dukkhanirodhagāminiyā paṭipadāya ñāṇaṃ",
    "Nekkhammasaṅkappo, abyāpādasaṅkappo, avihiṃsāsaṅkappo",
    "Musāvādā veramaṇī, pisuṇāya vācāya veramaṇī, pharusāya vācāya veramaṇī, samphappalāpā veramaṇī",
    "Pāṇātipātā veramaṇī, adinnādānā veramaṇī, kāmesumicchācārā veramaṇī",
    "Idha ariyasāvako micchāājīvaṃ pahāya sammāājīvena jīvikaṃ kappeti")})


# =========================================================================== jhāna frames (Abhidhammabhājanīya)
OPENER = {   # Idha bhikkhu yasmiṃ samaye <X> -> В то время, когда здесь монах развивает <Russian>
    "rūpūpapattiyā maggaṃ bhāveti": "путь к рождению в мире форм и",
    "arūpūpapattiyā maggaṃ bhāveti": "путь к рождению в мире без форм и",
    "lokuttaraṃ jhānaṃ bhāveti niyyānikaṃ apacayagāmiṃ diṭṭhigatānaṃ pahānāya paṭhamāya bhūmiyā pattiyā":
        K6.SUPRA.rstrip(", "),
    "rūpāvacaraṃ jhānaṃ bhāveti kiriyaṃ neva kusalaṃ nākusalaṃ na ca kammavipākaṃ diṭṭhadhammasukhavihāraṃ":
        f"медитативное погружение, относящееся к миру форм, {K6.KIRIYA_JH}",
    "arūpāvacaraṃ jhānaṃ bhāveti kiriyaṃ neva kusalaṃ nākusalaṃ na ca kammavipākaṃ diṭṭhadhammasukhavihāraṃ":
        f"медитативное погружение, относящееся к миру без форм, {K6.KIRIYA_JH}",
}
TASSEVA = {   # Tasseva … vipākaṃ -> Вследствие того же …, когда кто-либо
    "Tasseva rūpāvacarassa kusalassa kammassa katattā upacitattā vipākaṃ":
        ("Вследствие того же совершённого и накопленного благого действия, относящегося к миру форм, в качестве его "
         "результата, когда кто-либо"),
    "Tasseva arūpāvacarassa kusalassa kammassa katattā upacitattā vipākaṃ":
        ("Вследствие того же совершённого и накопленного благого действия, относящегося к миру без форм, в "
         "качестве его результата, когда кто-либо"),
    "Tasseva lokuttarassa kusalassa jhānassa katattā bhāvitattā vipākaṃ": K79.TASSEVA_OPEN.rstrip(", "),
}
J_PE = {"vitakkavicārānaṃ vūpasamā": "с затиханием направленной мысли и удержания мысли",
        "pītiyā ca virāgā": "с угасанием восторга", "sukhassa ca pahānā": "с устранением приятного"}
J_INTO = {"dutiyaṃ": "во второе", "tatiyaṃ": "в третье", "catutthaṃ": "в четвёртое", "pañcamaṃ": "в пятое"}
J_BODY = {"vivicceva kāmehi…pe… paṭhamaṃ jhānaṃ upasampajja viharati": (", ", K6.J1)}   # pi-1 openers (^1-160 …)
for _a, _ar in J_PE.items():
    for _o, _or in J_INTO.items():
        J_BODY[f"{_a}…pe… {_o} jhānaṃ upasampajja viharati"] = (" ", f"{_ar}… входит {_or} {JH}")
J_BODY.update({   # Pāli jhāna clause -> (separator after the opener, Russian)
    ("vivicceva kāmehi vivicca akusalehi dhammehi avitakkaṃ vicāramattaṃ vivekajaṃ pītisukhaṃ dutiyaṃ jhānaṃ "
     "upasampajja viharati"):
        (", ", "полностью уединившись от чувственных удовольствий, уединившись от неблагих явлений, входит во второе "
               "медитативное погружение, без направленной мысли, только с удержанием мысли, с восторгом и счастьем, "
               "рождёнными уединением"),
    ("sabbaso ākiñcaññāyatanaṃ samatikkamma nevasaññānāsaññāyatanasaññāsahagataṃ sukhassa ca pahānā…pe… catutthaṃ "
     "jhānaṃ upasampajja viharati"): (", ", K6.J4_ARUPA[:-len(" и пребывает в нём")]),
    ("vitakkavicārānaṃ vūpasamā…pe… dutiyaṃ jhānaṃ…pe… tatiyaṃ jhānaṃ…pe… catutthaṃ jhānaṃ…pe… paṭhamaṃ "
     "jhānaṃ…pe… pañcamaṃ jhānaṃ upasampajja viharati"):
        (" ", "с затиханием направленной мысли и удержания мысли… второе медитативное погружение… третье "
              "медитативное погружение… четвёртое медитативное погружение… первое медитативное погружение… входит "
              "в пятое медитативное погружение"),
})
J_FIELD = {"pathavīkasiṇaṃ": ", со всеохватным объектом земли, и пребывает в нём",
           "dukkhapaṭipadaṃ dandhābhiññaṃ": ", с трудным способом практики и медленным высшим знанием, и пребывает в нём",
           "dukkhapaṭipadaṃ dandhābhiññaṃ suññataṃ": (", с трудным способом практики и медленным высшим знанием, "
                                                     "пустое, и пребывает в нём"),
           "": " и пребывает в нём"}
J_RX = ("(" + "|".join(re.escape(k) for k in sorted(J_BODY, key=len, reverse=True)) + ")(?: (pathavīkasiṇaṃ|"
        "dukkhapaṭipadaṃ dandhābhiññaṃ suññataṃ|dukkhapaṭipadaṃ dandhābhiññaṃ))?")
ANGA = {"pañc": "пятичастное", "catur": "четырёхчастное", "tiv": "трёхчастное", "duv": "двухчастное"}
FACTOR = {"vitakko": "направленная мысль", "vicāro": "удержание мысли", "pīti": "восторг", "sukhaṃ": "счастье",
          "cittassekaggatā": "однонаправленность ума", "upekkhā": "невозмутимость"}


def j_clause(body, field):
    sep, ru = J_BODY[body]
    return sep, ru + J_FIELD[field or ""]


def frame_head(s):
    """«Idha bhikkhu yasmiṃ samaye <opener> <jhāna>» / «Tasseva … vipākaṃ <jhāna>» -> (Russian, rest after «, »)"""
    m = re.match(r"^Idha bhikkhu yasmiṃ samaye (" + "|".join(re.escape(k) for k in OPENER) + r") " + J_RX
                 + r"(, (.*))?$", s)
    if m:
        sep, ru = j_clause(m.group(2), m.group(3))
        return f"{SUPRA_OPEN}{OPENER[m.group(1)]}{sep}{ru}", m.group(5)
    m = re.match(r"^(" + "|".join(re.escape(k) for k in TASSEVA) + r") " + J_RX + r"(, (.*))?$", s)
    if m:
        sep, ru = j_clause(m.group(2), m.group(3))
        return f"{TASSEVA[m.group(1)]}{sep}{ru}", m.group(5)
    return None, None


def frame_tail(t, sid):
    """the part after «…, »: «tasmiṃ samaye …» / «yā tasmiṃ samaye … – ayaṃ vuccati …»"""
    if t is None:
        return "."
    m = re.match(r"^tasmiṃ samaye (\S+?)aṅgikaṃ jhānaṃ hoti( – |(?= ))(.*)\.$", t)
    if m:
        kind, dash, fac = m.groups()
        if dash != " – ":
            fac = fac.strip()
            toks = fac.split(" ")
            slip(f"^{sid} «caturaṅgikaṃ jhānaṃ hoti vicāro pīti sukhaṃ cittassekaggatā»: no dash and no commas "
                 "(written with a colon and commas in Russian)")
            return f", {AT_TIME} есть {ANGA[kind]} {JH}: " + ", ".join(FACTOR[x] for x in toks) + "."
        toks = fac.split(", ")
        return f", {AT_TIME} есть {ANGA[kind]} {JH} – " + ", ".join(FACTOR[x] for x in toks) + "."
    if t == "tasmiṃ samaye phasso hoti…pe… avikkhepo hoti.":
        return f", {AT_TIME} {CONTACT_PE}."
    if t == "yo tasmiṃ samaye phasso hoti…pe… avikkhepo hoti – ime dhammā kusalā.":
        return f", то, что {AT_TIME} {CONTACT_PE}, – {low(ALL_THIS)}"
    if t == "tasmiṃ samaye satta bojjhaṅgā honti – satisambojjhaṅgo…pe… upekkhāsambojjhaṅgo.":
        return f", {AT_TIME} есть {low(SEVEN_PE)}"
    m = re.match(r"^tasmiṃ samaye ((?:aṭṭhaṅgiko|pañcaṅgiko) maggo hoti.*)$", t)
    if m:
        return f", {AT_TIME} {K45.SUPRA_TAIL[m.group(1)]}"
    m = re.match(r'^(?:yo|yā|yaṃ) tasmiṃ samaye (.*?) – (?:idaṃ|ayaṃ) vuccati (.+)\.$', t)
    if m:
        return f", {K79.WHAT_AT_TIME} {LISTS[m.group(1)]}, – {called(m.group(2), sid)}"
    raise KeyError(t)


# =========================================================================== sentence engine
def called(raw, sid, cap_=False):
    """X / "X" / "X"…pe… after «vuccati» -> «это называется «X(ins)»»"""
    t = raw.strip()
    tail = ""
    if t.endswith("…pe…"):
        t, tail = t[:-len("…pe…")], "…"
    if t.endswith('"ti'):
        slip(f"^{sid} «… vuccati {t}»: «ti» after the quoted term (not rendered)")
        t = t[:-2]
    quoted = t.startswith('"') and t.endswith('"')
    t = t.strip('"')
    ins = (INS_594 if sid == "2-594" and t in INS_594 else INS)[t]
    if not quoted:
        slip(f"^{sid} «… vuccati {t}» without quotation marks: rendered without «»")
        r = f"это называется {ins}{tail}."
    else:
        r = f"это называется «{ins}»{tail}."
    return cap(r) if cap_ else r


def body_ru(b, sid):
    m = re.match(r"^(Yo|Yā|Yaṃ) (.*)$", b)
    if m and m.group(2) in LISTS:
        return f"То, что есть {LISTS[m.group(2)]}", True
    if b in BODY:
        return BODY[b]
    if b in K45.BODY:                                          # ch. 4 path-factor bodies
        return K45.BODY[b]
    m = re.match(r"^Idha bhikkhu ((?:anuppannānaṃ|uppannānaṃ) .*)$", b)
    if m and "chandaṃ janeti" in b:
        return f"{MONK} {K79.efforts(m.group(1))}", False
    m = re.match(r"^Idha bhikkhu (kāye kāyānupassī viharati .*)$", b)
    if m:
        return f"{MONK} {K79.satip_list(m.group(1))}", False
    if b == ("Idha bhikkhu vivicceva kāmehi vivicca akusalehi dhammehi savitakkaṃ savicāraṃ vivekajaṃ pītisukhaṃ "
             "paṭhamaṃ jhānaṃ upasampajja viharati; vitakkavicārānaṃ vūpasamā ajjhattaṃ sampasādanaṃ cetaso "
             "ekodibhāvaṃ avitakkaṃ avicāraṃ samādhijaṃ pītisukhaṃ dutiyaṃ jhānaṃ upasampajja viharati; pītiyā ca "
             "virāgā upekkhako ca viharati sato ca sampajāno sukhañca kāyena paṭisaṃvedeti, yaṃ taṃ ariyā ācikkhanti "
             "\"upekkhako satimā sukhavihārī\"ti tatiyaṃ jhānaṃ upasampajja viharati; sukhassa ca pahānā dukkhassa ca "
             "pahānā pubbeva somanassadomanassānaṃ atthaṅgamā adukkhamasukhaṃ upekkhāsatipārisuddhiṃ catutthaṃ jhānaṃ "
             "upasampajja viharati"):
        return (f"{MONK}, {J1F}, и пребывает в нём; {J2F}, и пребывает в нём; {J3F_ND} и пребывает в нём; {J4F}, и "
                "пребывает в нём"), False
    raise KeyError(b)


def avasesa(s):
    """Avasesā dhammā Xsampayuttā…pe… avasesā dhammā Ysampayuttā. -> Остальные явления связаны с X(ins)… …"""
    body, tail = s[:-1], ""
    if body.endswith("…pe…"):
        body, tail = body[:-len("…pe…")], "…"
    out = []
    for piece in re.split(r"\s*…pe…\s*", body):
        m = re.match(r"^[Aa]vasesā dhammā (?:(\S+?)(?:sambojjhaṅga)?sampayuttā|(\S+(?: \S+)?) sampayuttā)(ti)?$", piece)
        assert m, piece
        key = m.group(1) if m.group(1) else m.group(2)
        out.append(f"остальные явления связаны с {SAMP_INS[key]}")
    return cap("… ".join(out)) + tail + "."


def topic_key(t):
    return low(t)


def sentence(s, sid):
    """one Pāli sentence (Suttanta / Abhidhamma) -> Russian"""
    s = re.sub(r" …pe…", "…pe…", s)
    for bad, (good, note) in SENT_SLIP.items():
        if bad in s:
            s = s.replace(bad, good)
            slip(note)
    if s in SENT:
        return SENT[s]
    if s in K79.SENT:
        return K79.SENT[s]
    # ---- topics «"X"ti …»
    m = re.match(r'^"([^"]+)"(n?)ti([.,]?)(?: (.*)|(…pe…) (.*))?$', s)
    if m:
        top = TOP[topic_key(m.group(1))]
        if m.group(5):                                        # "X"ti…pe… tena vuccati "X"ti.
            return f"«{top}»… {low(sentence(cap(m.group(6)), sid))}"
        rest = m.group(4)
        if not rest:
            assert m.group(3) == ".", s
            return f"«{top}»."
        return f"«{top}»: {low(sentence(cap(rest), sid))}"
    m = re.match(r"^(Saṃvaro|Saṃvuto)ti\.$", s)
    if m:
        return f"«{TOP[low(m.group(1))]}»."
    m = re.match(r'^[Tt]ena vuccati "([^"]+)"(n?)ti\.$', s)
    if m:
        r = f"{TENA} «{TOP[topic_key(m.group(1))]}»."
        return r if s[0] == "T" else low(r)
    # ---- questions
    m = re.match(r"^Tattha katam(?:o|ā|aṃ|e) (.+?)\?$", s)
    if m:
        nom = (NOM_594 if sid == "2-594" and m.group(1) in NOM_594 else NOM)[m.group(1)]
        return f"Что такое {S.TATTHA} {nom}?"
    m = re.match(r'^Tattha katam(?:o|ā|aṃ|e) (\S+)…pe… (?:idaṃ|ayaṃ) vuccati (".+")\.$', s)
    if m:
        return f"Что такое {S.TATTHA} {NOM[m.group(1)]}… {called(m.group(2), sid)}"
    m = re.match(r"^Tattha katam(?:o|ā|aṃ|e) (.+?)\? (.*)$", s)
    if m:                                                     # «Tattha katame satta bojjhaṅgā? Idha bhikkhu …»
        return f"Что такое {S.TATTHA} {NOM[m.group(1)]}? {sentence(m.group(2), sid)}"
    # ---- jhāna / path frames
    head, rest = frame_head(s[:-1] if s.endswith(".") and ", " not in s else s)
    if head:
        if rest is None:
            assert s.endswith("."), s
            return head + "."
        return head + frame_tail(rest, sid)
    # ---- answers «<body> – ayaṃ vuccati "X".»
    m = re.match(r'^(.*) – (?:ayaṃ|idaṃ|ime|imā) (?:vuccati|vuccanti) (.+)\.$', s)
    if m:
        ru, comma = body_ru(m.group(1), sid)
        return f"{ru}{',' if comma else ''} – {called(m.group(2), sid)}"
    m = re.match(r'^(?:Ayaṃ|Idaṃ|Ime|Imā) (?:vuccati|vuccanti) (.+)\.$', s)
    if m:
        return called(m.group(1), sid, cap_=True)
    m = re.match(r"^(Yo|Yā|Yaṃ) (.*)\.$", s)
    if m and m.group(2) in LISTS:
        return f"То, что есть {LISTS[m.group(2)]}."
    m = re.match(r"^Yo (\S+ jhānassa|\S+āyatanassa) lābho paṭilābho patti sampatti phusanā sacchikiriyā "
                 r"upasampadā\.$", s)
    if m:
        return "То, что есть " + UPASAMPADA.format(x=UPA_GEN[m.group(1)]) + "."
    m = re.match(r"^(\S+āyatanaṃ) samāpannassa vā upapannassa vā diṭṭhadhammasukhavihārissa vā cittacetasikā "
                 r"dhammā\.$", s)
    if m:
        return "Ум и сопутствующие уму явления " + WHOSE.format(x=ATTAIN[low(m.group(1))]) + "."
    m = re.match(r"^Imaṃ (\S+āyatanaṃ) atikkanto hoti vītikkanto samatikkanto\.$", s)
    if m:
        return f"Эту {ATTAIN[m.group(1)]} он преодолел, миновал, полностью преодолел."
    m = re.match(r"^Idaṃ (paṭhamaṃ|dutiyaṃ|tatiyaṃ) samāpajjatīti \1\.$", s)
    if m:
        n, i = JH_ORD[m.group(1)]
        return f"{cap(n)}, потому что в него входят {i}."
    # ---- «Atthi X, atthi Y.»
    m = re.match(r"^Atthi (.+?),? atthi (.+)\.$", s)
    if m:
        d = dict(ATTHI)
        if sid == "2-594":
            d.update(ATTHI_594)
        return f"Есть {d[m.group(1)]}, есть {d[m.group(2)]}."
    # ---- ch. 10: «Yadapi X tadapi Ysambojjhaṅgo abhiññāya sambodhāya nibbānāya saṃvattati.»
    m = re.match(r"^Yadapi (.+?) tadapi (\S+)sambojjhaṅgo abhiññāya sambodhāya nibbānāya saṃvattati\.$", s)
    if m:
        return f"{cap(ATTHI[m.group(1)])} тоже является {BJ_INS[m.group(2)]}, {TOWARD}."
    # ---- calm / purify / possess
    m = re.match(r"^(.+?) santā (?:hoti|honti) samitā vūpasantā atthaṅgatā abbhatthaṅgatā appitā byappitā sositā "
                 r"visositā byantīkatā\.$", s)
    if m:
        subj, g = CALM_SUBJ[m.group(1)]
        if m.group(1) == "Iti ayañca vitakko ayañca vicāro" and " hoti " in s:
            slip(f"^{sid} «Iti ayañca vitakko ayañca vicāro santā hoti» (singular hoti with two subjects; honti "
                 "in ^2-572): rendered in the plural")
        return f"{subj} {CALM[g]}."
    m = re.match(r"^Idaṃ cittaṃ (imāya \S+|imamhā \S+) sodheti visodheti parisodheti moceti vimoceti parimoceti\.$", s)
    if m:
        return f"Этот ум он {SODHETI.format(x=FROM[m.group(1)])}."
    m = re.match(r"^(.*?) upeto hoti( samupeto upāgato samupāgato upapanno sampanno samannāgato|…pe… samannāgato| "
                 r"samupeto…pe… samannāgato)\.$", s)
    if m:
        u = {" samupeto upāgato samupāgato upapanno sampanno samannāgato": UPETO, "…pe… samannāgato": UPETO_PE,
             " samupeto…pe… samannāgato": UPETO_PE2}[m.group(2)]
        return f"{INSTR[m.group(1)]} он {u}."
    # ---- the rest
    if re.match(r"^[Aa]vasesā dhammā ", s):
        return avasesa(s)
    m = re.match(r"^Idha bhikkhu ((?:\S+sambojjhaṅgaṃ|sammā\S+) bhāveti .*)\.$", s)
    if m:
        return f"{MONK} {bhaveti_list(m.group(1))}."
    raise KeyError(s)


def bhaveti_list(body):
    """Xsambojjhaṅgaṃ / sammāXṃ bhāveti vivekanissitaṃ …, Y bhāveti…pe… Z bhāveti … (^2-471, ^2-489)"""
    toks = re.split(r"(, |…pe… |… )", body)
    res = ""
    for i in range(0, len(toks), 2):
        t = toks[i]
        sep = toks[i - 1] if i else ""
        m = re.match(r"^(\S+?)(sambojjhaṅgaṃ)? bhāveti( " + NISSITA_P + ")?$", t)
        assert m, t
        if m.group(2):
            obj, g = BJ_RU[m.group(1)], "m"
        else:
            obj, g = PATH_ACC[m.group(1)]
        piece = f"развивает {obj}" + (f", {NISSITA[g]}" if m.group(3) else "")
        res += ("" if not i else ("; " if sep == ", " else "… ")) + piece
    return res


def split_sents(line):
    """K45.split_sents, but never inside a variant bracket («[odaggaṃ (sī.) dha. sa. 9]»)"""
    masked = re.sub(r"\[[^\]]*\]", lambda m: m.group(0).replace(". ", ".\x00"), line)
    return [p.replace(".\x00", ". ") for p in K45.split_sents(masked)]


PI1_LINE = [   # (Pāli line start, end of the passage shared with pi-1, pi-1 Russian of that passage)
    ("Tattha katamā indriyesu aguttadvāratā?", '– ayaṃ vuccati "indriyesu aguttadvāratā".', P1_1352),
    ("Tattha katamā indriyesu guttadvāratā?", '– ayaṃ vuccati "indriyesu guttadvāratā".', P1_1354),
    ("Tattha katamā bhojane amattaññutā?", '– ayaṃ vuccati "bhojane amattaññutā"ti.', P1_1353),
    ("Tattha katamā bhojane mattaññutā?", '– ayaṃ vuccati "bhojane mattaññutā".', P1_1355),
]


def line_ru(ln, sid):
    if ln in SENT:
        return SENT[ln]
    for start, end, ru in PI1_LINE:
        if ln.startswith(start):
            shared, rest = ln.split(end, 1)
            if "Ñatvādhikaraṇamenaṃ" in shared:
                slip(SENT_SLIP["Ñatvādhikaraṇamenaṃ"][1])
            if end.endswith('"ti.'):
                slip(f"^{sid} «… vuccati \"bhojane amattaññutā\"ti.»: «ti» after the quoted term (not rendered)")
            rest = rest.strip()
            return ru + ((" " + " ".join(sentence(s, sid) for s in split_sents(rest))) if rest else "")
    return " ".join(sentence(s, sid) for s in split_sents(ln))


# =========================================================================== Pañhāpucchaka (K23 engine + neuter subjects)
GROUPS = dict(K79.GROUPS79)
GROUPS.update({"Sattannaṃ bojjhaṅgānaṃ": "из семи факторов пробуждения",
               "Aṭṭhannaṃ maggaṅgānaṃ": "из восьми факторов пути",
               "Catunnaṃ jhānānaṃ": "из четырёх медитативных погружений"})
SUBJ1012 = {   # Pāli subject -> (Russian nominative, number, gender, accusative)
    "Pītisambojjhaṅgo": (cap(BJ_RU["pīti"]), "s", "m", cap(BJ_RU["pīti"])),
    "Dhammavicayasambojjhaṅgo": (cap(BJ_RU["dhammavicaya"]), "s", "m", cap(BJ_RU["dhammavicaya"])),
    "Cha bojjhaṅgā": ("Шесть факторов пробуждения", "p", "p", "Шесть факторов пробуждения"),
    "Sammāsaṅkappo": ("Правильный помысел", "s", "m", "Правильный помысел"),
    "Sammādiṭṭhi": ("Правильное воззрение", "s", "n", "Правильное воззрение"),
    "Satta maggaṅgā": ("Семь факторов пути", "p", "p", "Семь факторов пути"),
    "Tīṇi jhānāni": ("Три медитативных погружения", "p", "p", "Три медитативных погружения"),
    "Dve jhānāni": ("Два медитативных погружения", "p", "p", "Два медитативных погружения"),
    "Catutthaṃ jhānaṃ": ("Четвёртое медитативное погружение", "s", "n", "Четвёртое медитативное погружение"),
    "Paṭhamaṃ jhānaṃ": ("Первое медитативное погружение", "s", "n", "Первое медитативное погружение"),
}
LOCAL1012 = {"savitakko savicāro": K1.ITEMS["savitakkasavicāro"]}   # "savitakkaṃ savicāraṃ" (^2-640, two words)
SUBJ_SPLIT = re.compile(r"(, |; )(?=(?:" + "|".join(low(k) for k in SUBJ1012) + r"|@@) )")
EXC = {   # etthuppannaṃ X ṭhapetvā = кроме возникшего в них / в нём X(gen)
    ("sukhaṃ vedanaṃ", "p"): "возникшего в них приятного чувства",
    ("adukkhamasukhaṃ vedanaṃ", "s"): "возникшего в нём чувства, которое ни болезненно, ни приятно",
    ("vitakkavicāre", "s"): "возникших в нём направленной мысли и удержания мысли",
    ("pītiṃ", "p"): "возникшего в них восторга", ("sukhaṃ", "p"): "возникшего в них счастья",
    ("upekkhaṃ", "s"): "возникшей в нём невозмутимости", ("vitakkaṃ", "s"): "возникшей в нём направленной мысли",
    ("vicāraṃ", "s"): "возникшего в нём удержания мысли",
}
_NSHORT = {"связана": "связано", "подвержена": "подвержено", "свободна": "свободно", "способна": "способно",
           "затронута": "затронуто", "охвачена": "охвачено", "омрачена": "омрачено", "соединена": "соединено",
           "порождена": "порождено", "познаваема": "познаваемо"}
_NSPECIAL = {"та": "то", "которой": "которому"}


def _nword(w):
    if w in _NSPECIAL:
        return _NSPECIAL[w]
    if w.endswith("аяся"):
        return w[:-4] + "ееся"
    if w.endswith("яя"):
        return w[:-2] + "ее"
    if w.endswith("ая"):
        s = w[:-2]
        return s + ("ее" if s[-1] in "щшжч" else "ое")
    return w


def neut_v(it):
    v = it["v"]
    if v == "является " + it["ins"]:
        return "является " + it["nins"]
    return re.sub(r"[А-Яа-яЁё]+", lambda m: _NSHORT.get(m.group(0), m.group(0)), v)


def neut_f(it):
    return re.sub(r"[А-Яа-яЁё]+", lambda m: _nword(m.group(0)), it["f"])


_ORIG_PRED, _ORIG_QUOTE = K23.pred, K23.quote


def pred_n(word, num, gen):
    if num == "s" and gen == "n":
        return neut_v(K23.get(K23.sg_key(word)))
    return _ORIG_PRED(word, num, gen)


def quote_n(key, num, gen):
    if num == "s" and gen == "n":
        return f"«{neut_f(K23.get(key))}»"
    return _ORIG_QUOTE(key, num, gen)


def install():
    K79.install()
    K23.SUBJ.update(SUBJ1012)
    K23.LOCAL.update(LOCAL1012)
    K23.PLK.update({"āsavavippayuttā sāsavā": "āsavavippayuttasāsavo",        # ^2-641, written as two words
                    "āsavavippayuttā anāsavā": "āsavavippayuttaanāsavo"})
    K23.PRON["n"] = "его"
    K23.pred, K23.quote = pred_n, quote_n


NV_RX = re.compile(r"^(?P<pre>.*?)(?P<nv>[Nn]a vattabb(?:o|ā|aṃ)) (?P<rest>.+)$")


def _qwrap(t):
    for suf in ("ntipi", "nti", "tipi", "ti"):
        if t.endswith(suf):
            return f'"{t[:-len(suf)]}"{suf}'
    raise ValueError(t)


def quote_nv(sent):
    """«na vattabbā X(cā)ti, Y» / «… Xtipi, Ytipi» without quotes and dash -> the K23 «na vattabbā – "X"ti» form"""
    toks = sent.split(", ")
    out, in_nv = [], False
    for t in toks:
        if ' – "' in t or t.startswith('"'):
            out.append(t)
            in_nv = t.endswith("tipi")
            continue
        m = NV_RX.match(t)
        if m:
            out.append(f'{m.group("pre")}{m.group("nv")} – {_qwrap(m.group("rest"))}')
            in_nv = True
            continue
        if in_nv and t.endswith("tipi"):
            out.append(_qwrap(t))
            continue
        in_nv = False
        out.append(t)
    return ", ".join(out)


def engine(clause):
    """one clause with or without a subject (K23 engine; subjectless = all items, K45 «@@»)"""
    r = K45.panha_sentence(quote_nv(clause), None)
    return r


def panha_clause(c):
    m = re.match(r"^(" + "|".join(SUBJ1012) + r") – etthuppann(?:aṃ|e) (.+?) ṭhapetvā (.+)$", c)
    if m:
        subj, x, pred = m.groups()
        ru_s, num, gen, _ = SUBJ1012[subj]
        rest = engine(f"{subj} {pred}")
        assert rest.startswith(ru_s + " "), rest
        return f"{ru_s} – кроме {EXC[(x, num)]}, {rest[len(ru_s) + 1:]}"
    if c.startswith("@@ "):
        r = K23.sentence(quote_nv(c))
        assert r.startswith("@@ "), r
        return r[3:]
    return engine(c)


PANHA_FIX = [   # (bad, good, note)
    ("Anāsavā āsavavippayuttā.", "Anāsavā. Āsavavippayuttā.",
     "^2-485 «Anāsavā āsavavippayuttā.»: full stop missing (two sentences, as in ^2-507)"),
    ('"āsavā ceva āsavasampayuttā cāti"pi, āsavasampayuttā ceva no ca āsavātipi',
     '"āsavā ceva āsavasampayuttā cā"tipi, "āsavasampayuttā ceva no ca āsavā"tipi',
     '^2-641 «"āsavā ceva āsavasampayuttā cāti"pi»: closing quote misplaced (= "…cā"tipi)'),
    ("maggahetukantipi maggādhipatītipi", "maggahetukantipi, maggādhipatītipi",
     "^2-640 «maggahetukantipi maggādhipatītipi»: comma missing (added)"),
    ("paccuppannāramaṇantipi", "paccuppannārammaṇantipi",
     "^2-640 «paccuppannāramaṇantipi» (for paccuppannārammaṇantipi): rendered as meant"),
    ("tīṇi jhānāni upekkhāsahagatā, na kāmāvacarā", "tīṇi jhānāni upekkhāsahagatā; @@ na kāmāvacarā", None),
    ("siyā na arūpāvacaraṃ, siyā pariyāpannā", "siyā na arūpāvacaraṃ; @@ siyā pariyāpannā", None),
]


def panha_sentence(s, sid):
    body = s[:-1]
    if body == "Āsavā ceva āsavasampayuttā cātipi, āsavasampayuttā ceva no ca āsavātipi":
        slip("^2-485 «Āsavā ceva āsavasampayuttā cātipi, āsavasampayuttā ceva no ca āsavātipi.»: «Na vattabbā» "
             "missing (as in ^2-507); translated as written, continuing the previous sentence («Ни как …, ни как …»)")
        r = panha_sentence("Na vattabbā " + low(s), sid)
        assert r.startswith("Нельзя определить ни как"), r
        return "Ни как" + r[len("Нельзя определить ни как"):]
    if body.startswith("Dhammavicayasambojjhaṅgo hetu, cha bojjhaṅgā hetusampayuttā"):
        slip("^2-485 «Dhammavicayasambojjhaṅgo hetu, cha bojjhaṅgā hetusampayuttā.»: ^2-507 has «… na hetū. "
             "Sahetukā. Hetusampayuttā.» here (translated as written)")
    body = re.sub(r'([Nn]a vattabb(?:o|ā|aṃ)) "', r'\1 – "', body)
    parts = SUBJ_SPLIT.split(body)
    out = []
    for i in range(0, len(parts), 2):
        c = parts[i]
        sep = parts[i - 1] if i else ""
        if i:
            if not c.startswith("@@"):
                c = cap(c)
            r = panha_clause(c)
            out.append(sep + (r if c.startswith("@@") else low(r)))
        else:
            out.append(panha_clause(c))
    r = "".join(out) + "."
    nv = K1.NV.split(" ", 1)[1]                                # «определить –»
    return r.replace(f"{nv} ", nv[:-2] + " ")                  # the Pāli has no dash after na vattabbā here


def panha_line(p, sid):
    for bad, good, note in PANHA_FIX + K79.PANHA_FIX79:
        if bad in p:
            p = p.replace(bad, good)
            if note:
                slip(note)
    if "@@" in p:
        slip("^2-641 «…, tīṇi jhānāni upekkhāsahagatā, na kāmāvacarā …» and «catutthaṃ jhānaṃ … siyā na arūpāvacaraṃ, "
             "siyā pariyāpannā …»: plural predicates of all four jhānas run on after a subject; a «;» is set before "
             "them in Russian (no subject added)")
        if "tīṇi jhānāni upekkhāsahagatā" in p:
            slip("^2-641 «tīṇi jhānāni upekkhāsahagatā» (three jhānas accompanied by equanimity; the tika ^2-640 has "
                 "only the fourth): translated as written, possibly «na upekkhāsahagatā» meant")
    sents = re.split(r"(?<=\.) (?=[A-ZĀĪŪṬḌṆÑ])", p)
    return " ".join(panha_sentence(s, sid) for s in sents)


# =========================================================================== chapters
SUBHEAD = {"Mātikā": "Матрица", "Rūpāvacarakusalaṃ": "Благой ум, относящийся к миру форм",
           "Arūpāvacarakusalaṃ": "Благой ум, относящийся к миру без форм", "Lokuttarakusalaṃ": "Надмирский благой ум",
           "Rūpāvacaravipākā": "Результаты действий, относящиеся к миру форм",
           "Arūpāvacaravipākā": "Результаты действий, относящиеся к миру без форм",
           "Lokuttaravipākā": "Надмирские результаты действий",
           "Rūpārūpāvacarakiriyā": "Функциональный ум, относящийся к миру форм и к миру без форм"}


def heading(ln, ch):
    lvl, text = ln.split(" ", 1)
    T = {S.CH_TITLE[ch][0]: S.CH_TITLE[ch][1], "Suttantabhājanīyaṃ": S.SUTTANTA_BH, "Abhidhammabhājanīyaṃ": S.ABHI_BH,
         "Pañhāpucchakaṃ": S.PANHA, "Tikaṃ": S.TIKA_H, "Dukaṃ": S.DUKA_H}
    T.update(SUBHEAD)
    return f"{lvl} {T[text]}"


def build(ch):
    pali = (S.PALI / PARTS[ch]).read_text(encoding="utf-8")
    h, section = {}, None
    for sid, lines in S.segs(pali):
        SID["sid"] = sid
        lines = [re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", ln) for ln in lines]
        if lines[0].startswith("#"):
            assert len(lines) == 1
            text = lines[0].split(" ", 1)[1]
            if text in ("Suttantabhājanīyaṃ", "Abhidhammabhājanīyaṃ", "Pañhāpucchakaṃ"):
                section = text
            h[sid] = [heading(lines[0], ch)]
            continue
        ru = []
        for ln in lines:
            if ln in SENT:
                ru.append(SENT[ln])
            elif section == "Pañhāpucchakaṃ" and not ln.startswith(("Satta bojjhaṅgā", "Ariyo", "Cattāri jhānāni")):
                ru.append(K1.panha_question(ln, GROUPS) if ln.endswith("?") else panha_line(ln, sid))
            else:
                ru.append(line_ru(ln, sid))
        h[sid] = ru
    return pali, h


# =========================================================================== pi-1 / earlier-chapter checks
def check():
    K79.check_pi1()
    K23.assert_pi1(WISDOM_FULL, VITAKKA_FULL, VICARA, PITI_LIST, SANNA_LIST, "кроме совокупности чувств",
                   "Ум и сопутствующие уму явления", "с полным преодолением восприятий материальной формы, с "
                   "исчезновением восприятий соударения, без внимания к восприятиям разнообразия",
                   "полностью преодолев сферу бесконечного пространства", "Четверичный метод.", "Пятеричный метод.",
                   "Благой ум, относящийся к миру форм", "Благой ум, относящийся к миру без форм",
                   "Надмирский благой ум", "Результаты действий, относящиеся к миру форм",
                   "Результаты действий, относящиеся к миру без форм", "пятичастное медитативное погружение",
                   "с затиханием направленной мысли и удержания мысли… входит в третье медитативное погружение",
                   "с угасанием восторга… входит в четвёртое медитативное погружение",
                   "с устранением приятного… входит в пятое медитативное погружение",
                   "второе медитативное погружение… третье медитативное погружение… четвёртое медитативное погружение… "
                   "первое медитативное погружение… входит в пятое медитативное погружение",
                   "входит во второе медитативное погружение, без направленной мысли, только с удержанием мысли, с "
                   "восторгом и счастьем, рождёнными сосредоточением", "Вот человек", "безмятежность умственного тела",
                   "безмятежность ума", "направление ума на объект, правильный помысел",
                   "Всякая нравственная сдержанность является кротостью")
    ch4 = (S.OUT / "4-saccavibhango.md").read_text(encoding="utf-8")
    for s in (NOBLE8.split(", а именно")[1], f"{MONK}, {J1F}, и пребывает в нём."[len(MONK) + 2:],
              "в это время есть восьмичастный путь"):
        assert s in ch4, s


# =========================================================================== notes
def notes_md():
    L = ["# pi-2 Russian rails: new formulas of chapters 10, 11 and 12 (^2-466 … ^2-641)", "",
         "Generated by build_rails_10_12_ru.py; import it instead of retyping. Strings already in ru-rails-formulas.md "
         "(sample), notes-1.md, notes-2-3.md, notes-4-5.md, notes-6.md or notes-7-9.md are not repeated.", "",
         "## Headings and closing labels", ""]
    L += [f"##### {p} = ##### {r}" for p, r in SUBHEAD.items()]
    L += ["Catukkaṃ. = Четверичный метод.  Pañcakaṃ. = Пятеричный метод.  (pi-1 «Catukkanayo / Pañcakanayo»)", "",
          "## Factors of awakening (ch. 10)", "",
          f"Satta bojjhaṅgā – satisambojjhaṅgo, … upekkhāsambojjhaṅgo. = {SEVEN_LIST}",
          f"Satta bojjhaṅgā – satisambojjhaṅgo…pe… upekkhāsambojjhaṅgo. = {SEVEN_PE}",
          "Xsambojjhaṅgo = " + "; ".join(f"{k} = {BJ_RU[k]} (ins. {BJ_INS[k]})" for k in BJ),
          "Atthi X, atthi Y. = Есть X, есть Y.",
          f"Yadapi X tadapi Ysambojjhaṅgo abhiññāya sambodhāya nibbānāya saṃvattati. = X тоже является Y(ins), {TOWARD}.",
          "Atthi/Yadapi members: " + "; ".join(f"{k} = {v}" for k, v in ATTHI.items()),
          f"Xsambojjhaṅgaṃ bhāveti {NISSITA_P} = развивает X, {NISSITA['m']} (n.: {NISSITA['n']}); joined by «;», "
          "…pe… = «…»",
          "Ime vuccanti (\"satta bojjhaṅgā\"). = Это называется (\"семью факторами пробуждения\").",
          "Avasesā dhammā sattahi bojjhaṅgehi sampayuttā. = Остальные явления связаны с семью факторами пробуждения.",
          "Avasesā dhammā Xsambojjhaṅgasampayuttā…pe… avasesā dhammā … = Остальные явления связаны с X(ins)… "
          "остальные явления связаны с …",
          f"tasmiṃ samaye satta bojjhaṅgā honti – … = в это время есть {low(SEVEN_PE)}",
          "yo tasmiṃ samaye phasso hoti…pe… avikkhepo hoti – ime dhammā kusalā. = то, что в это время есть контакт… "
          "есть отсутствие отвлечения, – это благие явления.",
          "", "## Path factors (ch. 11)", "",
          f"Ariyo aṭṭhaṅgiko maggo, seyyathidaṃ – … = {NOBLE8}",
          f"Aṭṭhaṅgiko maggo – … = {EIGHT_LIST}", f"Pañcaṅgiko maggo – … = {FIVE_LIST}",
          f"Aṭṭhaṅgiko maggo – sammādiṭṭhi…pe… sammāsamādhi. = {EIGHT_PE}",
          "sammāXṃ bhāveti vivekanissitaṃ … = развивает правильное воззрение, опирающееся на уединение, … ведущее к "
          "отказу (agreeing with the factor)",
          "Avasesā dhammā aṭṭhaṅgikena / pañcaṅgikena maggena / sammādiṭṭhiyā / sammāsaṅkappena … sampayuttā. = "
          "Остальные явления связаны с восьмичастным / пятичастным путём / правильным воззрением / правильным "
          "помыслом …",
          "^2-487 sammāsamādhi without the dash of ch. 4 (yaṃ taṃ ariyā ācikkhanti \"…\"ti) = «так что благородные "
          "говорят о нём: «…»»",
          "", "## Jhāna (ch. 12), Suttanta definitions", "",
          "\"X\"ti … (the word explained, same sentence) = «X»: … ; \"X\"ti. = «X».; \"X\"ti…pe… tena vuccati \"X\"ti. "
          "= «X»… поэтому это называется: «X».",
          "topics: " + "; ".join(f"{k} = {v}" for k, v in TOP.items()),
          "Tattha katamo X? = Что такое здесь X? (" + "; ".join(f"{k} = {v}" for k, v in NOM.items()) + ")",
          "… vuccati \"X\" = это называется «X(ins)» (" + "; ".join(f"{k} = {v}" for k, v in INS.items()) + ")",
          "^2-594 sukhaṃ = приятное (APPROVED: bodily pleasure); dukkhaṃ = болезненное",
          "X santā hoti/honti samitā vūpasantā atthaṅgatā abbhatthaṅgatā appitā byappitā sositā visositā byantīkatā. "
          f"= X {CALM['p']}. (f.: {CALM['f']}; m.: {CALM['m']}; n.: {CALM['n']})",
          "subjects: " + "; ".join(f"{k} = {v[0]}" for k, v in CALM_SUBJ.items()),
          f"Idaṃ cittaṃ imāya/imamhā X sodheti visodheti parisodheti moceti vimoceti parimoceti. = Этот ум он "
          f"{SODHETI.format(x='X(gen)')}. (" + "; ".join(f"{k} = {v}" for k, v in FROM.items()) + ")",
          f"<X> upeto hoti samupeto…pe… samannāgato. = <X(ins)> он {UPETO_PE2}. (" + "; ".join(
              f"{k} = {v}" for k, v in INSTR.items()) + ")",
          f"Tassa X cattattā vantattā muttattā pahīnattā paṭinissaṭṭhattā pahīnapaṭinissaṭṭhattā. = "
          f"{WHY_GONE.format(x='его X')}",
          f"Yo X-assa lābho paṭilābho patti sampatti phusanā sacchikiriyā upasampadā. = То, что есть "
          f"{UPASAMPADA.format(x='X(gen)')}.",
          "Gaṇanānupubbatā paṭhamaṃ. Idaṃ paṭhamaṃ samāpajjatīti paṭhamaṃ. = Первое по порядку счёта. Первое, потому "
          "что в него входят первым.",
          f"X samāpannassa vā upapannassa vā diṭṭhadhammasukhavihārissa vā cittacetasikā dhammā. = Ум и сопутствующие "
          f"уму явления {WHOSE.format(x='X(acc)')}.",
          "Imaṃ Xāyatanaṃ atikkanto hoti vītikkanto samatikkanto. = Эту X он преодолел, миновал, полностью преодолел.",
          f"So abhikkante paṭikkante sampajānakārī hoti, … = Он {CLEAR_LIST.format(v='')}.",
          f"Idha bhikkhu sato sampajāno abhikkamati, … = {MONK}, {sato_line()}.",
          f"arūpa formula (^2-508): {ARUPA1}; {ARUPA2}; {ARUPA3}; {ARUPA4}",
          "lists after Yo / Yā / Yaṃ (= То, что есть …), new here: " + "; ".join(
              f"{k} = {v}" for k, v in LISTS.items() if k not in K79.LISTS),
          "", "## Jhāna (ch. 12), Abhidhamma", "",
          f"Cattāri jhānāni – paṭhamaṃ jhānaṃ, … = {FOUR_JH}",
          "Idha bhikkhu yasmiṃ samaye <opener> <jhāna> <field>, tasmiṃ samaye … = В то время, когда здесь монах "
          "развивает <opener><jhāna><field>, в это время …",
          "openers: " + "; ".join(f"{k} = {v}" for k, v in OPENER.items()),
          "jhāna clauses: " + "; ".join(f"{k} = {v[1]}" for k, v in J_BODY.items()),
          "fields: " + "; ".join(f"{k or '(none)'} = {v}" for k, v in J_FIELD.items()),
          "Tasseva …: " + "; ".join(f"{k} = {v}" for k, v in TASSEVA.items()),
          "tasmiṃ samaye pañcaṅgikaṃ / caturaṅgikaṃ / tivaṅgikaṃ / duvaṅgikaṃ jhānaṃ hoti – … = в это время есть "
          "пятичастное / четырёхчастное / трёхчастное / двухчастное медитативное погружение – … (factors: "
          + "; ".join(f"{k} = {v}" for k, v in FACTOR.items()) + ")",
          "Idaṃ vuccati \"paṭhamaṃ jhānaṃ\". = Это называется «первым медитативным погружением».",
          "Avasesā dhammā jhānasampayuttā. = Остальные явления связаны с медитативным погружением.",
          "", "## Pañhāpucchaka", "",
          "Sattannaṃ bojjhaṅgānaṃ / Aṭṭhannaṃ maggaṅgānaṃ / Catunnaṃ jhānānaṃ kati …? = Сколько из семи факторов "
          "пробуждения / из восьми факторов пути / из четырёх медитативных погружений являются …?",
          "subjects: " + "; ".join(f"{k} = {v[0]}" for k, v in SUBJ1012.items()),
          "neuter singular subjects: predicates «связано / подвержено …», «является X(nins)»; quotes «имеющее …», "
          "«находящееся …»; «иногда его нельзя определить …»",
          "X – etthuppannaṃ Y ṭhapetvā Z = X – кроме Y(gen), Z (" + "; ".join(f"{k[0]} = {v}" for k, v in EXC.items())
          + ")",
          "na vattabbā \"X\"ti (quotes, no dash, ch. 12) / na vattabbā Xti (no quotes, ch. 10-11) = нельзя "
          "определить как «X» (no dash)",
          ]
    return "\n".join(L) + "\n"


def main():
    install()
    check()
    for ch in (10, 11, 12):
        pali, h = build(ch)
        (S.OUT / PARTS[ch]).write_text(K23.render(pali, h), encoding="utf-8", newline="\n")
        print(f"wrote {PARTS[ch]}: {len(S.segs(pali))} segments")
    NOTES_PATH.write_text(notes_md(), encoding="utf-8", newline="\n")
    for s in SLIPS + K23.SLIPS + K1.SLIPS + K45.SLIPS + K79.SLIPS:
        print("slip:", s)


if __name__ == "__main__":
    main()
