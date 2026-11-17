"""Build the Pāli->Russian keyword map for pi-2 (Vibhaṅga) chapter 6-paticcasamuppadavibhango.

usage: python -I -X utf8 map_6_ru.py               (writes 6-paticcasamuppadavibhango.mapped.md and verifies it)
       python -I -X utf8 map_6_ru.py --dump [--miss]   (prints every keyword=value with a presence flag; --miss: only
                                                        the flagged ones; no writing)

Resolution order per keyword: OVERRIDES[bid][kw]  ->  context rules (resolve())  ->  PACCAYA (Xpaccayā: the form
present in the segment)  ->  T (this file: map_4_5_ru.T + the chapter 6 additions)  ->  pi-1 CH2 / MATRIX.
Conventions: ru-map-conventions-pi2.md (+ the pi-1 file), notes-map-2-3.md, notes-map-4-5.md; new decisions:
notes-map-6.md. The mind-type, jhāna, vipāka and kiriya openings and the definition strings repeat pi-1 word for
word: their values are the pi-1 map's (^1-1, ^1-390, ^1-425, ^1-429, ^1-431, ^1-455, ^1-176, ^1-266, ^1-277,
^1-505, ^1-577, ^1-1219, ^1-1343 …).
"""
import pathlib
import re
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import map_4_5_ru as M45  # noqa: E402  (read-only: its table T, EXC)
from map_common_pi2_ru import (GAP, NDE, build_part, lc, present, read_keywords,  # noqa: E402,F401
                               read_pali, read_russian, value, verify)

PART = "6-paticcasamuppadavibhango"

# ---------------------------------------------------------------------------- table
T = dict(M45.T)
assert not any(v.startswith("классификация") for v in T.values())

T.update({
    # ---- ch. 2-5 values that do not fit chapter 6 (pi-1 values back)
    "sukhaṃ": "счастье", "sukha": "счастье", "mano": "разум", "dukkha": "страдание", "dukkhaṃ": "боль",
    "kāma": "чувственные желания", "rūpa": "материальная форма", "samudaye": "возникновение",
    "saṅkhāra": "формирующие факторы",
    # ---- headings
    "vibhaṅgo": "разбор", "paṭicca": "в зависимости от условий", "samuppāda": "возникновение",
    "catukkaṃ": "четвёрка", "paccayacatukkaṃ": "четвёрка условий", "hetu": "причина",
    "sampayuttacatukkaṃ": "четвёрка связанности", "aññamañña": "взаимный",
    "aññamaññacatukkaṃ": "четвёрка взаимной обусловленности", "mātikā": "матрица",
    "niddeso": "разъяснение", "akusala": "неблагой", "abyākata": "этически неопределённый",
    "mūlaka": "основа", "vipākaniddeso": "разъяснение результатов", "mūlakavipāka": "результаты на основе",
    # ---- the chain (pi-1 ^1-1343; Abhidhamma singular saṅkhāro)
    "avijjā": "неведение", "saṅkhārā": "формирующие факторы", "saṅkhāro": "формирующий фактор",
    "viññāṇaṃ": "сознание", "viññāṇa": "сознание", "nāmarūpaṃ": "умственное и материальная форма",
    "nāmarūpa": "умственное и материальная форма", "nāmaṃ": "умственное", "nāma": "умственное",
    "rūpaṃ": "материальная форма", "saḷāyatanaṃ": "шесть сфер восприятия", "saḷāyatana": "шесть сфер восприятия",
    "chaṭṭhāyatanaṃ": "шестая сфера восприятия", "chaṭṭhāyatana": "шестая сфера восприятия",
    "āyatanaṃ": "сфера восприятия", "āyatana": "сфера восприятия",
    "phasso": "контакт", "vedanā": "чувство", "taṇhā": "жажда", "upādānaṃ": "цепляние", "upādāna": "цепляние",
    "bhavo": "существование", "bhava": "существование", "jāti": "рождение", "jarāmaraṇaṃ": "старение и смерть",
    "jarā": "старение", "maraṇaṃ": "смерть", "soka": "печаль", "parideva": "стенания",
    "domanassupāyāsā": "уныние и отчаяние", "upāyāsā": "отчаяние", "paccayā": "обусловленный",
    "kevalassa": "весь", "kevalassa dukkhakkhandhassa": "вся" + GAP + "совокупность страдания",
    "dukkhakkhandhassa": "совокупность страдания", "khandhassa": "совокупность", "samudayo": "возникновение",
    "adhimokkho": "решимость", "paṭighaṃ": "неприязнь", "pasādo": "ясная вера", "uddhaccaṃ": "беспокойство",
    "vicikicchā": "колебание",
    # hetu / sampayutta catukka (2-244, 2-245)
    "hetuko": "имеющий причиной", "hetukaṃ": "имеющий причиной",
    "saṅkhāro avijjāhetuko": "формирующий фактор имеющий причиной неведение",
    "vedanā phassahetukā": "чувство имеющее причиной контакт",
    "taṇhā vedanāhetukā": "жажда имеющая причиной чувство",
    "upādānaṃ taṇhāhetukaṃ": "цепляние имеющее причиной жажду",
    "sampayutto": "связанный",
    # ---- Suttanta definitions (2-226 … 2-242)
    "dukkhe": "страдание", "aññāṇaṃ": "незнание", "dukkhasamudaye": "возникновение страдания",
    "nirodhe": "прекращение", "dukkhanirodhe": "прекращение страдания",
    "puññābhisaṅkhāro": "волевое действие приносящее заслугу",
    "apuññābhisaṅkhāro": "волевое действие не приносящее заслуги",
    "āneñjābhisaṅkhāro": "волевое действие ведущее к непоколебимому", "ābhisaṅkhāro": "волевое действие",
    "kāyasaṅkhāro": "телесный формирующий фактор", "kāya": "телесный", "vacī": "речевой", "citta": "умственный",
    "cetanā": "намерение", "kāmāvacarā": "относящийся к миру чувственных желаний",
    "rūpāvacarā": "относящийся к миру форм", "arūpāvacarā": "относящийся к миру без форм",
    "āvacarā": "относящийся к миру", "dāna": "даяние", "sīla": "нравственность", "bhāvanā": "развитие ума",
    "mahābhūtā": "великие элементы", "bhūtā": "элементы", "upādāya": "производный",
    "upādāya rūpaṃ": "материальная форма производная", "khandho": "совокупность",
    "phassa": "контакт", "sadda": "звук", "gandha": "запах", "rasa": "вкус", "phoṭṭhabba": "осязаемое",
    "kāmupādānaṃ": "цепляние за чувственные удовольствия", "diṭṭhupādānaṃ": "цепляние за воззрения",
    "sīlabbatupādānaṃ": "цепляние за обряды и обеты", "attavādupādānaṃ": "цепляние за учение о самости",
    "atta": "самость",
    "kammabhavo": "существование как действие", "upapattibhavo": "существование как перерождение",
    "gāmi": "ведущий", "arūpa": "мир без форм", "saññā": "восприятие", "asaññā": "без восприятия",
    "nevasaññānāsaññā": "ни с восприятием ни без восприятия", "ekavokāra": "одна составляющая",
    "catuvokāra": "четыре составляющие", "pañcavokāra": "пять составляющих",
    "tesaṃ tesaṃ": "тот или иной", "sattānaṃ": "существа", "nikāye": "класс", "sañjāti": "зарождение",
    "okkanti": "вхождение", "abhinibbatti": "появление", "abhinibbati": "появление",
    "khandhānaṃ": "совокупности", "pātubhāvo": "проявление", "āyatanānaṃ": "сферы восприятия",
    "paṭilābho": "обретение",
    "parisoko": "глубокая" + GAP + "печаль",
    "asātaṃ": "безотрадный", "kāyikaṃ": "телесный", "vedayitaṃ": "переживание",
    "dukkhaṃ vedayitaṃ": "болезненное переживание", "dukkhā vedanā": "болезненное чувство",
    "asātaṃ dukkhaṃ": "безотрадный болезненный",
    "asātaṃ dukkhaṃ vedayitaṃ": "безотрадное болезненное переживание",
    "asātā dukkhā vedanā": "безотрадное болезненное чувство",
    "kāyasamphassa": "контакт тела", "kāyasamphassajaṃ": "рождённый контактом тела",
    "kāyasamphassajā": "рождённый контактом тела",
    "cetasikaṃ": "душевный", "cetasikaṃ asātaṃ": "душевная безотрадность", "cetasikaṃ dukkhaṃ": "душевная боль",
    "cetosamphassa": "контакт ума", "cetosamphassajaṃ": "рождённый контактом ума",
    "cetosamphassajā": "рождённый контактом ума",
    "saṅgati": "сочетание", "samodhānaṃ": "соединение", "tena": "поэтому",
    # ---- Abhidhamma definitions (pi-1 strings)
    "adassanaṃ": "отсутствие видения", "laṅgī": "засов", "moho": "заблуждение",
    "akusalamūlaṃ": "неблагой корень", "mūlaṃ": "корень", "ñāṇaṃ": "знание",
    "sañcetanā": "проявление намерения", "sañcetayitattaṃ": "состояние намеренности",
    "cittaṃ": "ум", "mānasaṃ": "умственная деятельность", "hadayaṃ": "сердце", "paṇḍaraṃ": "чистота",
    "manāyatanaṃ": "сфера ума", "manindriyaṃ": "способность ума", "viññāṇakkhandho": "совокупность сознания",
    "tajjā": "соответствующий", "manoviññāṇadhātu": "элемент умственного сознания",
    "manoviññāṇa": "умственное сознание", "dhātu": "элемент", "viññāṇadhātu": "элемент" + GAP + "сознания",
    "phusanā": "касание",
    "cetasikaṃ sātaṃ": "душевная отрада", "cetasikaṃ sukhaṃ": "душевное счастье", "sātaṃ": "отрадный",
    "sātaṃ sukhaṃ": "отрадный приятный", "sātaṃ sukhaṃ vedayitaṃ": "отрадное приятное переживание",
    "sātā sukhā vedanā": "отрадное приятное чувство", "sukhaṃ vedayitaṃ": "приятное переживание",
    "sukhā vedanā": "приятное чувство",
    "nāsātaṃ": "безотрадный", "adukkhamasukhaṃ": "ни болезненный ни приятный",
    "adukkhamasukhā vedanā": "чувство которое ни болезненно ни приятно",
    "rāgo": "страсть", "sārāgo": "пристрастие", "anunayo": "расположенность", "anurodho": "потакание",
    "nandī": "наслаждение", "nandirāgo": "страсть к наслаждению", "cittassa": "ум",
    "diṭṭhi": "воззрение", "diṭṭhigataṃ": "приверженность воззрениям", "gahanaṃ": "дебри", "kantāro": "пустыня",
    "visūkāyikaṃ": "извращённость", "vipphanditaṃ": "метания", "saṃyojanaṃ": "оковы", "gāho": "хватка",
    "abhiniveso": "убеждённость", "parāmāso": "искажение", "kummaggo": "кривая дорога",
    "micchāpatho": "ложный путь", "micchā": "ложный", "patho": "путь", "micchattaṃ": "ложность",
    "titthāyatanaṃ": "сфера сектантских учений", "vipariyāsaggāho": "превратная хватка",
    "vipariyāsa": "превратный", "ṭhapetvā": "кроме",
    "nibbatti": "образование", "khayo": "уничтожение", "vayo": "угасание", "bhedo": "распад",
    "paribhedo": "полный распад", "aniccatā": "непостоянство", "antaradhānaṃ": "исчезновение",
    "jīraṇatā": "одряхление", "āyuno": "срок жизни",
    "cakkhāyatanassa": "сфера глаза", "sotāyatanassa": "сфера уха", "ghānāyatanassa": "сфера носа",
    "jivhāyatanassa": "сфера языка", "kāyāyatanassa": "сфера тела", "yaṃ vā panaññampi": "или же какой бы другой",
    "cittajaṃ": "рождённый умом", "samuṭṭhānaṃ": "порождённый",
    "nissāya": "в зависимости от", "rūpaṃ nissāya": "материальная форма в зависимости от которой",
    "vattati": "действовать",
    "adhimuccanā": "проявление решимости", "tadadhimuttatā": "состояние решимости в отношении этого",
    "sasaṅkhārena": "с побуждением",
    "āghāto": "досада", "caṇḍikkaṃ": "свирепость", "asuropo": "грубость", "anattamanatā": "недовольство",
    "kaṅkhāyanā": "проявление сомнения", "vimati": "неуверенность", "dveḷhakaṃ": "раздвоенность",
    "dvidhāpatho": "распутье", "saṃsayo": "нерешительность",
    "anekaṃsa": "неспособность прийти к определённости", "āsappanā": "блуждание",
    "parisappanā": "беспорядочное блуждание", "apariyogāhaṇā": "отсутствие углубления",
    "chambhitattaṃ": "оцепенелость", "vilekho": "терзание",
    "avūpasamo": "отсутствие затихания", "cetaso vikkhepo": "отвлечение ума", "vikkhepo": "отвлечение",
    "bhantattaṃ": "взбудораженность",
    "alobho": "отсутствие жадности", "alubbhanā": "отсутствие проявления жадности",
    "asārāgo": "отсутствие пристрастия", "anabhijjhā": "отсутствие алчности", "adoso": "отсутствие злобы",
    "adussanā": "отсутствие проявления злобы", "abyāpādo": "отсутствие недоброжелательности",
    "abyāpajjo": "отсутствие неприязни", "amoho": "отсутствие заблуждения", "paññā": "мудрость",
    "pajānanā": "понимание", "dhammavicayo": "исследование явлений", "vicayo": "исследование",
    "sammā": "правильный", "kusalamūlaṃ": "благой корень", "kusalamūlā": "благие корни", "mūlā": "корни",
    "kusalamūla": "благие корни", "akusalamūla": "неблагие корни", "mūla": "корни",
    "saddahanā": "доверие", "okappanā": "уверенность", "dhamma": "явление", "dhammānaṃ": "явления",
    "sambojjhaṅgo": "фактор пробуждения", "vicayasambojjhaṅgo": "фактор пробуждения исследования",
    "maggaṅgaṃ": "фактор пути", "aṅgaṃ": "фактор", "maggapariyāpannaṃ": "входящий в путь",
    # ---- openings (pi-1 cittuppāda / jhāna / vipāka / kiriya)
    "dhammā": "явления", "dhammā akusalā": "неблагие явления", "dhammā kusalā": "благие явления",
    "dhammā abyākatā": "этически неопределённые явления",
    "akusalaṃ": "неблагой", "akusalaṃ cittaṃ": "неблагой ум", "kusalaṃ": "благой", "kusalaṃ cittaṃ": "благой ум",
    "uppannaṃ": "возникать", "uppannā": "возникать", "dhātu uppannā": "возникать элемент",
    "samaye": "в это время", "yaṃ yaṃ": "что бы то ни было",
    "sahagataṃ": "сопровождаемый", "sahagatā": "сопровождаемый", "somanassa": "радость",
    "somanassasahagataṃ": "сопровождаемый радостью", "somanassasahagatā": "сопровождаемый радостью",
    "upekkhā": "невозмутимость", "upekkhāsahagataṃ": "сопровождаемый невозмутимостью",
    "upekkhāsahagatā": "сопровождаемый невозмутимостью", "domanassa": "уныние",
    "sampayuttaṃ": "связанный", "sampayuttā": "связанный", "vippayuttaṃ": "не связанный",
    "vippayuttā": "не связанный", "diṭṭhigata": "приверженность воззрениям", "ñāṇa": "знание",
    "ñāṇavippayuttaṃ": "не связанный со знанием", "ñāṇavippayuttā": "не связанный со знанием",
    "kāmāvacaraṃ": "относящийся к миру чувственных желаний", "āvacaraṃ": "относящийся к миру",
    "ārammaṇaṃ": "объект", "ārammaṇā": "объект",
    "rūpārammaṇaṃ": "видимая форма", "saddārammaṇaṃ": "звук", "gandhārammaṇaṃ": "запах",
    "rasārammaṇaṃ": "вкус", "phoṭṭhabbārammaṇaṃ": "осязаемое", "dhammārammaṇaṃ": "объект ума",
    "rūpārammaṇā": "видимая форма", "saddārammaṇā": "звук", "gandhārammaṇā": "запах",
    "rasārammaṇā": "вкус", "phoṭṭhabbārammaṇā": "осязаемое", "dhammārammaṇā": "объект ума",
    "jhānaṃ": "медитативное погружение", "bhāveti": "развивать", "maggaṃ bhāveti": "развивать путь",
    "maggaṃ": "путь", "ūpapattiyā maggaṃ": "путь к рождению", "ūpapattiyā": "рождение",
    "rūpūpapattiyā": "рождение в мире форм", "arūpūpapattiyā": "рождение в мире без форм",
    "kāmehi": "чувственные удовольствия", "vivicceva": "полностью уединиться",
    "vivicceva kāmehi": "полностью уединиться от чувственных удовольствий",
    "upasampajja": "входить", "viharati": "пребывать", "upasampajja viharati": "входить" + GAP + "пребывать",
    "kasiṇaṃ": "всеохватный объект", "pathavī": "земля", "pathavīkasiṇaṃ": "всеохватный объект земли",
    "kusalā": "благой", "pahānā": "устранение", "sukhassa ca pahānā": "устранение приятного",
    "sukhassa": "приятное", "samatikkamma": "преодолеть", "sabbaso": "полностью",
    "ākiñcaññāyatanaṃ": "сфера отсутствия чего-либо",
    "nevasaññānāsaññāyatana": "сфера ни восприятия ни невосприятия",
    "catutthaṃ jhānaṃ": "четвёртое медитативное погружение",
    "lokuttaraṃ": "надмирский", "jhānaṃ bhāveti": "развивать" + GAP + "медитативное погружение",
    "apacaya": "убывание", "apacayagāmiṃ": "ведущий" + GAP + "к убыванию",
    "diṭṭhigatānaṃ": "приверженность воззрениям", "pahānāya": "устранение",
    "diṭṭhigatānaṃ pahānāya": "устранение приверженности воззрениям", "pattiyā": "достижение",
    "bhūmiyā": "ступень", "dukkhapaṭipadaṃ": "трудный способ практики", "paṭipadaṃ": "способ практики",
    "dandhābhiññaṃ": "медленное высшее знание", "ābhiññaṃ": "высшее знание",
    "paṭipadaṃ dandhābhiññaṃ": "способ практики и медленное высшее знание",
    "katattā": "совершённый", "upacitattā": "накопленный", "vipākaṃ": "являющийся результатом",
    "vipākā": "являющийся результатом", "kāmāvacarassa": "относящийся к миру чувственных желаний",
    "kāmāvacarassa kusalassa": "благой" + GAP + "относящийся к миру чувственных желаний",
    "kusalassa": "благой", "kusalassa kammassa": "благое действие", "akusalassa": "неблагой",
    "abyākatā": "этически неопределённый", "manodhātu": "элемент ума",
    "cakkhuviññāṇa": "зрительное сознание", "cakkhuviññāṇadhātu": "элемент зрительного сознания",
    "kāyaviññāṇa": "осязательное сознание", "kāyaviññāṇadhātu": "элемент осязательного сознания",
    "rūpāvacarassa": "относящийся к миру форм", "arūpāvacarassa": "относящийся к миру без форм",
    "āvacarassa": "относящийся к миру", "bhāvitattā": "развитый",
    "kusalassa jhānassa": "благое медитативное погружение",
    "rūpāvacaraṃ": "относящийся к миру форм", "arūpāvacaraṃ": "относящийся к миру без форм",
    "arūpāvacaraṃ jhānaṃ": "медитативное погружение относящееся к миру без форм",
    "kiriyaṃ": "функциональный", "kiriyā": "функциональный", "kusalaṃ nākusalaṃ": "ни благой ни неблагой",
    "kusalā nākusalā": "ни благой ни неблагой", "ākusalaṃ": "неблагой", "ākusalā": "неблагой",
    "vihāraṃ": "пребывание", "diṭṭhadhamma": "эта жизнь", "suññataṃ": "пустой",
    "avikkhepo": "отсутствие отвлечения", "niṭṭhito": "завершённый",
})

# Xpaccayā: the conditioning term in the instrumental. The value is «обусловленный X» where the segment has the
# question / answer noun phrase («Что такое здесь сознание, обусловленное формирующим фактором?»), else
# «X обусловленный» (chain form «формирующим фактором обусловлено сознание»). Detected with the EXACT instrumental
# (present() cannot tell «обусловлено сознание» from «обусловленное сознанием», nor singular from plural).
# Fragments (rūpa of nāmarūpa, āyatana of chaṭṭhāyatana/saḷāyatana, mūla of kusalamūla): (detect, value) pairs.
INSTR = {
    "avijjā": ["неведением"], "saṅkhāra": ["формирующим фактором", "формирующими факторами"],
    "viññāṇa": ["сознанием"], "nāma": ["умственным"], "nāmarūpa": ["умственным и материальной формой"],
    "saḷāyatana": ["шестью сферами восприятия"], "chaṭṭhāyatana": ["шестой сферой восприятия"],
    "phassa": ["контактом"], "vedanā": ["чувством"], "taṇhā": ["жаждой"], "upādāna": ["цеплянием"],
    "bhava": ["существованием"], "jāti": ["рождением"], "adhimokkha": ["решимостью"],
    "paṭigha": ["неприязнью"], "vicikicchā": ["колебанием"], "uddhacca": ["беспокойством"],
    "pasāda": ["ясной верой"], "kusalamūla": ["благими корнями"], "akusalamūla": ["неблагими корнями"],
}
FRAG = {
    "rūpa": [("умственным и материальной формой", "материальной формой")],
    "āyatana": [("шестой сферой восприятия", "сферой восприятия"),
                ("шестью сферами восприятия", "сферами восприятия")],
    "mūla": [("благими корнями", "корнями"), ("неблагими корнями", "корнями")],
}
_CY = "а-яё"


def _q(phrase, text):   # question / answer form: «обусловленн… X» with X in the exact instrumental
    return re.search(rf"обусловлен[{_CY}]*,? {re.escape(phrase)}(?![{_CY}])", text, re.I)


def _c(phrase, text):   # chain form: «X (тоже) обусловлен…»
    return re.search(rf"(?<![{_CY}]){re.escape(phrase)} (?:тоже )?обусловлен", text, re.I)


def paccaya_value(kw, ru):
    stem = lc(kw)[: -len("paccayā")]
    if stem in INSTR:
        for ins in INSTR[stem]:
            if _q(ins, ru):
                return f"обусловленный {ins}"
        for ins in INSTR[stem]:
            if _c(ins, ru):
                return f"{ins} обусловленный"
        raise KeyError(kw)
    if stem in FRAG:
        for det, ins in FRAG[stem]:
            if _q(det, ru):
                return f"обусловленный{GAP}{ins}"
        for det, ins in FRAG[stem]:
            if _c(det, ru):
                return f"{ins} обусловленный"
        raise KeyError(kw)
    return None


# ---------------------------------------------------------------------------- per-segment overrides
OVERRIDES = {
    "2-6-2-14-0": {"Kusala": "благой"},
    "2-6-2-15-0": {"Akusala": "неблагой"},
    "2-229": {"āyatanaṃ": "сфера"},
    "2-232": {"Rūpa": "видимая форма", "dhamma": "объект ума"},
    "2-233": {"sīla": "обряд"},
    "2-234": {"rūpa": "мир форм", "duvidhena": "на два вида"},
}

# presence-check exceptions (value correct; inflection outside present()'s tolerance)
EXC = {**M45.EXC,
       "kevalassa": "весь ~ всей (suppletive pronoun stem), = pi-1 ^1-1343",
       "tesaṃ tesaṃ": "тот или иной ~ тех или иных (pronoun declension), = pi-1"}


def resolver_for(part):
    ru, pi = read_russian(part), read_pali(part)

    def resolve(bid, kw, kws):
        k = lc(kw)
        s = {lc(x) for x in kws}
        text = ru.get(bid, "")
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        if k in ov:
            return ov[k]
        if k.endswith("paccayā") and k != "paccayā":
            v = paccaya_value(kw, text)
            if v is not None:
                return v
        if k == "saṅkhāra":                              # stem of saṅkhārapaccayā (sg. in the Abhidhamma part)
            if "saṅkhārapaccayā" in s and "saṅkhārā" not in s and bid >= "2-243":
                return "формирующий фактор"
            return "формирующие факторы"
        if k == "dukkha":                                # dukkhakkhandha / dukkhapaṭipadā / dukkhadhamma
            if "dukkhakkhandhassa" in s:
                return "страдание"
            if "dukkhapaṭipadaṃ" in s:
                return "трудный"
            if "dhammena" in s:
                return "болезненный"
            return "страдание"
        if k == "mano" and "manodhātu" in s:             # «элемент ума»
            return "ум"
        if k == "cetasikaṃ" and "adukkhamasukhaṃ" in s:  # cetasikaṃ neva sātaṃ nāsātaṃ (pi-1 ^1-152)
            return "душевное состояние"
        if k == "gāho" and "anekaṃsa" in s:              # anekaṃsaggāho (pi-1 ^1-425)
            return NDE
        if k == "sahagataṃ" and not present("сопровождаемый", text):   # saññāsahagataṃ «в сопровождении»
            return "сопровождение"
        if k in ("sukha", "sukhasahagataṃ") and "kāyaviññāṇaṃ" in s:   # kāyaviññāṇa «сопровождаемое удовольствием»
            return {"sukha": "удовольствие", "sukhasahagataṃ": "сопровождаемый удовольствием"}[k]
        if k == "sukhaṃ" and "kāyikaṃ" in s:                         # kāyikaṃ sukhaṃ «телесное удовольствие»
            return "удовольствие"
        return value(kw, kws, T)
    return resolve


def allowed(part):
    return {(bid, kw): EXC[lc(kw)] for bid, kws in read_keywords(part) for kw in kws if lc(kw) in EXC}


def dump(part, only_miss=False):
    ru, res = read_russian(part), resolver_for(part)
    for bid, kws in read_keywords(part):
        out = []
        for kw in kws:
            try:
                v = res(bid, kw, kws)
            except KeyError:
                v = "???"
            bad = not (v == NDE or present(v, ru.get(bid, ""))) and lc(kw) not in EXC
            if bad or not only_miss:
                out.append(f"{kw}={v}" + (" !!" if bad else ""))
        if out:
            print(f"[{bid}] " + " | ".join(out))


if __name__ == "__main__":
    args = sys.argv[1:]
    if args[:1] == ["--dump"]:
        dump(PART, only_miss="--miss" in args)
        sys.exit()
    build_part(PART, resolver_for(PART))
    verify(PART, show=300, allowed=allowed(PART))
