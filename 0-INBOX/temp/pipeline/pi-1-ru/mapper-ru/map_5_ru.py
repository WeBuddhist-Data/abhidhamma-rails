"""Pāli->Russian keyword map for pi-1 part 5-atthakathakandam (Aṭṭhakathākaṇḍaṃ).

usage: python -I -X utf8 map_5_ru.py          (writes 5-atthakathakandam.mapped.md and verifies it)
       python -I -X utf8 map_5_ru.py --pairs  (also prints every distinct kw=value pair with its count)

Resolution order per keyword: OVERRIDES[bid][kw] -> context rules (rule()) -> T5 (this part)
-> MATRIX -> CH2 (map_common_ru.py, read-only). Every value was checked against the segment's
Russian (see notes-map-5.md for the recurring decisions of this part).
"""
import collections
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_ru import CH2, CORE, MATRIX, NDE, build_part, lc, read_keywords, read_russian, verify  # noqa: E402

PART = "5-atthakathakandam"
RU = read_russian(PART)

# ------------------------------------------------------------------------------------------ table
T5 = {
    # headings / colophon
    "kaṇḍaṃ": "раздел", "aṭṭhakathā": "разъяснение", "atthuddhāro": "разъяснение смысла",
    "duka": "пары", "dukaṃ": "пары", "antara": "промежуточный", "antaradukaṃ": "промежуточные пары",
    "piṭṭhi": "заключительный", "hetu": "корень", "āsava": "влечение", "saṃyojana": "оковы",
    "gantha": "узы", "ogha": "поток", "yoga": "ярмо", "nīvaraṇa": "помеха", "parāmāsa": "искажение",
    "upādāna": "цепляние", "kilesa": "омрачение",
    "niṭṭhito": "завершённый", "saṅgaṇī": "перечисление", "dhammasaṅgaṇī": "Перечисление явлений",
    # mind classes
    "kusalaṃ": "благой ум", "akusalaṃ": "неблагой ум", "kusalesu": "благой ум",
    "akusalesu": "неблагой ум", "kusalassa": "благой ум", "akusalassa": "неблагой ум",
    "akusalato": "неблагой ум", "kiriyesu": "функциональный ум",
    "kusala": "благой", "akusala": "неблагой", "kusalā": "благой", "akusalā": "неблагой",
    "akusalacitta": "неблагой ум", "abyākata": "этически неопределённый",
    "abyākataṃ": "этически неопределённый", "abyākatā": "этически неопределённый",
    "kiriyā": "функциональный", "kiriya": "функциональный",
    "kiriyābyākataṃ": "этически неопределённый функциональный ум",
    "akusalābyākatā": "неблагой и этически неопределённый",
    "bhūmīsu": "мир", "sabbaṃ": "весь", "avasesaṃ": "остальной", "avasesaṃ akusalaṃ": "остальной неблагой ум",
    "avasesañca": "остальной", "avasesañca rūpaṃ": "остальная материальная форма",
    "dvādasa": "двенадцать", "ekādasa": "одиннадцать", "dasa": "десять",
    "citta": "ум", "cittā": "ум", "cittañca": "ум",
    "uppādā": "виды", "uppāde": "виды", "uppādesu": "виды", "uppādo": "вид",
    "cittuppādā": "виды ума", "cittuppāde": "виды ума", "cittuppādesu": "виды ума",
    "cittuppādo": "вид ума",
    "sahagatacitta": "ум сопровождаемый", "sahagatesu citta": "ум сопровождаемый",
    "sahagato citta": "ум сопровождаемый", "vippayuttacitta": "ум не связанный",
    "vippayutte citta": "ум не связанный", "ahetuke citta": "ум без корней",
    "sahagata": "сопровождаемый", "sahagatā": "сопровождаемый", "sahagataṃ": "сопровождаемый",
    "sahagato": "сопровождаемый", "sahagatesu": "сопровождаемый",
    "sampayutta": "связанный", "sampayuttā": "связанный", "sampayutte": "связанный",
    "sampayutto": "связанный",
    "vippayutta": "не связанный", "vippayuttā": "не связанный", "vippayutte": "не связанный",
    "ñāṇa": "знание", "ñāṇavippayutta": "не связанный со знанием",
    "ñāṇavippayutte": "не связанный со знанием",
    "diṭṭhigata": "приверженность воззрениям",
    "diṭṭhigatavippayutta": "не связанный с приверженностью воззрениям",
    "diṭṭhigatavippayuttā": "не связанный с приверженностью воззрениям",
    "lobha": "жадность", "vippayuttalobha": "жадность и не связанный",
    "vippayuttā lobha": "жадность и не связанный",
    "somanassa": "радость", "domanassa": "уныние", "upekkhā": "невозмутимость",
    "vicikicchā": "колебание", "uddhacca": "беспокойство", "pīti": "восторг", "sukha": "счастье",
    "dukkha": "боль", "mohaṃ": "заблуждение", "moho": "заблуждение",
    "sahagato moho": "заблуждение сопровождаемое", "sahagataṃ mohaṃ": "заблуждение сопровождаемое",
    "sahagataṃ uddhaccasahagataṃ mohaṃ": "заблуждение сопровождаемое беспокойством",
    "kāyaviññāṇaṃ": "осязательное сознание",
    "viññāṇāni": "виды сознания", "pañcaviññāṇāni": "пять видов сознания",
    "dhātu": "элемент", "dhātuyo": "элементы", "mano": "ум", "manodhātu": "элемент ума",
    "manodhātuyo": "элементы ума", "manoviññāṇa": "умственное сознание",
    "manoviññāṇadhātu": "элемент умственного сознания",
    "dhātu upekkhāsahagatā": "элемент … сопровождаемый невозмутимостью",
    "manoviññāṇadhātu upekkhāsahagatā": "элемент умственного сознания сопровождаемый невозмутимостью",
    "kiriyāmano": "функциональный … ум", "kiriyāmanodhātu": "функциональный элемент ума",
    "kiriyāhetukamanoviññāṇa": "функциональный … умственное сознание без корней",
    "kiriyāhetukamanoviññāṇadhātu": "функциональный элемент умственного сознания без корней",
    "hetuka": "корни",
    "kāma": "чувственные желания", "kāmāvacara": "относящийся к миру чувственных желаний",
    "kāmāvacaraṃ": "относящийся к миру чувственных желаний",
    "kāmāvacarā": "относящийся к миру чувственных желаний",
    "kāmāvacarassa": "относящийся к миру чувственных желаний",
    "rūpāvacara": "мир форм", "rūpāvacaraṃ": "мир форм", "rūpāvacarā": "относящийся к миру форм",
    "arūpa": "без форм", "arūpāvacarā": "относящийся к миру без форм",
    "vipāka": "результат действий",
    # absorptions
    "jhānaṃ": "медитативное погружение", "jhānā": "медитативные погружения",
    "jhāne": "медитативное погружение", "jhānassa": "медитативное погружение",
    "catutthaṃ jhānaṃ": "четвёртое медитативное погружение",
    "catutthassa jhānassa": "четвёртое медитативное погружение",
    "lokuttara": "надмирский", "lokuttaraṃ": "надмирский",
    "lokuttaraṃ catutthaṃ jhānaṃ": "четвёртое надмирское медитативное погружение",
    "lokuttaraṃ paṭhamaṃ jhānaṃ": "первое надмирское медитативное погружение",
    "lokuttarapañcakanaye dutiyaṃ jhānaṃ": "второе надмирское медитативное погружение по пятеричному методу",
    "lokuttaratikacatukkajjhānā":
        "три надмирских медитативных погружения по четверичному методу и четыре по пятеричному",
    "lokuttaratikatikajjhānā":
        "три надмирских медитативных погружения по четверичному методу и три по пятеричному",
    "lokuttaradukatikajjhānā":
        "два надмирских медитативных погружения по четверичному методу и три по пятеричному",
    "lokuttaradukadukajjhānā":
        "два надмирских медитативных погружения по четверичному методу и два по пятеричному",
    "lokuttaraekakadukajjhānā":
        "одно надмирское медитативное погружение по четверичному методу и два по пятеричному",
    "pañcaka": "пятеричный", "pañcakanaye": "пятеричный метод", "naye": "метод",
    "āruppā": "бесформенные состояния",
    "viññāṇañcāyatanaṃ": "сфера бесконечного сознания", "ānañcāyatanaṃ": "сфера бесконечного",
    "ānañca": "бесконечный", "ākāsa": "пространство", "ākiñcañña": "отсутствие чего-либо",
    "asaññā": "невосприятие", "saññā": "восприятие",
    "vitakka": "направленная мысль", "vitakkā": "направленная мысль",
    "vicāra": "удержание мысли", "vicārā": "удержание мысли",
    "uppanne vitakkavicāre": "возникшие в них направленная мысль и удержание мысли",
    "uppannaṃ vicāraṃ": "возникшее в них удержание мысли",
    "uppannaṃ vitakkaṃ": "возникшая в них направленная мысль",
    "uppanno ca vicāro": "удержание мысли возникшее", "sahajāto": "возникший вместе",
    "savitakkasavicāro": "с направленной мыслью и удержанием мысли",
    "pītikā": "с восторгом",
    # paths, fruits
    "maggā": "пути", "magga": "путь", "maggā apariyāpannā": "пути не принадлежащие к кругам существования",
    "apariyāpannā": "не принадлежащий к кругам существования",
    "sāmañña": "отшельничество", "phalāni": "плоды", "phalaṃ": "плод",
    "sāmaññaphalāni nibbānañca": "плоды отшельничества и нирвана",
    "arahatta": "состояние архата", "upariṭṭhimaṃ": "высший", "ariya": "благородный",
    "adhipatino": "находящийся под главенством",
    # material form
    "rūpaṃ": "материальная форма", "rūpañca": "материальная форма",
    "rūpañca nibbānañca": "материальная форма и нирвана", "rūpaṃ nibbānañca": "материальная форма и нирвана",
    "nibbānañca anārammaṇā": "нирвана … не иметь объекта",
    "yañca": "та … которая", "kammassa": "действие", "kammassa katattā": "вследствие совершённых действий",
    "baddha": "связанный", "indriya": "орган чувств",
    "indriyabaddharūpañca nibbānañca": "материальная форма связанная с органами чувств и нирвана",
    "cakkhu": "глаз", "cakkhāyatanaṃ": "сфера глаза", "phoṭṭhabba": "осязаемое",
    "phoṭṭhabbāyatanaṃ": "сфера осязаемого", "rūpāyatanaṃ": "сфера видимых форм",
    "sadda": "звук", "saddāyatanaṃ": "сфера звуков", "gandha": "запах", "gandhāyatanaṃ": "сфера запахов",
    "rasa": "вкус", "rasāyatanaṃ": "сфера вкусов", "dhammāyatana": "сфера объектов ума",
    "dhammāyatanaṃ": "сфера объектов ума", "manāyatanaṃ": "сфера ума",
    "anidassana": "невидимый", "anidassanaṃ": "невидимый", "anidassanā": "невидимый",
    "appaṭighaṃ": "не способный к соударению", "sanidassana": "видимый", "sanidassanā": "видимый",
    "sappaṭighā": "способный к соударению",
    "upādāya": "производный", "upādāya rūpaṃ": "материальная форма производная",
    "bhūtā": "элементы", "mahābhūtā": "великие элементы", "upādā": "производный",
    "kāya": "телесный", "vacī": "речевой", "viññatti": "внешнее выражение",
    "kāyaviññatti": "телесное внешнее выражение", "vacīviññatti": "речевое внешнее выражение",
    "cittajaṃ": "рождённый умом", "hetukaṃ": "вызванный", "yaṃ": "любой",
    "rūpassa lahutā": "лёгкость материальной формы", "rūpassa mudutā": "мягкость материальной формы",
    "rūpassa kammaññatā": "работоспособность материальной формы",
    "rūpassa upacayo": "рост материальной формы", "rūpassa santati": "непрерывность материальной формы",
    "lahutā": "лёгкость", "mudutā": "мягкость", "kammaññatā": "работоспособность", "santati": "непрерывность",
    "kabaḷīkāro": "съедаемый", "kabaḷīkāro āhāro": "съедаемая пища", "āhāro": "пища",
    "ākāsadhātu": "элемент пространства", "āpo": "вода", "āpodhātu": "элемент воды",
    "cakkhuviññāṇaṃ": "зрительное сознание", "sotaviññāṇaṃ": "слуховое сознание",
    "ghānaviññāṇaṃ": "обонятельное сознание", "jivhāviññāṇaṃ": "вкусовое сознание",
    "khandho": "совокупность", "vedanākkhandho": "совокупность чувств",
    "saññākkhandho": "совокупность восприятия", "saṅkhārakkhandho": "совокупность формирующих факторов",
    "vedanā": "чувство", "vedanāya": "чувство", "saṅkhāra": "формирующие факторы",
    # frame
    "ṭhapetvā": "кроме", "siyā": "иногда", "vattabbā": "определить", "vattabbaṃ": "определить",
    "vattabbo": "определить", "uppannaṃ": "возникший", "uppanno": "возникший", "uppanne": "возникший",
    "uppannā": "возникший", "uppādino": "возникнуть", "uppajjati": "возникать", "uppajjanti": "возникать",
    "ekato": "вместе", "niyogā": "непременно", "na": "не",
    "dhammā": "явления", "dhamma": "объекты ума",
    # triad / pair items
    "sukhāya": "приятный", "dukkhāya": "болезненный", "adukkhamasukhāya": "ни болезненный ни приятный",
    "sukhāya vedanāya": "приятное чувство", "dukkhāya vedanāya": "болезненное чувство",
    "upādiṇṇa": "охваченный цеплянием", "upādiṇṇā": "охваченный цеплянием",
    "upādāniyā": "служащий объектом цепляния",
    "saṃkiliṭṭha": "омрачённый", "saṃkiliṭṭhā": "омрачённый", "asaṃkiliṭṭha": "неомрачённый",
    "asaṃkiliṭṭhā": "неомрачённый", "saṃkilesikā": "подверженный омрачению",
    "dassanena": "видение истины", "pahātabbā": "устраняемый", "pahātabba": "устраняться",
    "bhāvanāya pahātabbā": "устраняемый развитием ума", "bhāvanāya pahātabba": "устраняться развитием ума",
    "hetukā": "чьи корни", "pahātabbahetukā": "чьи корни устраняются",
    "ācaya": "накопление", "apacaya": "убывание", "caya": NDE,
    "sekkhā": "относящийся к обучающимся", "sekkha": "относящийся к обучающимся",
    "asekkhā": "относящийся к завершившим обучение",
    "paritta": "ограниченный", "parittā": "ограниченный", "mahaggata": "возвышенный",
    "mahaggatā": "возвышенный", "appamāṇa": "безмерный", "appamāṇā": "безмерный",
    "ārammaṇā": "с … объектом", "parittārammaṇā": "с ограниченным объектом",
    "mahaggatārammaṇā": "с возвышенным объектом", "appamāṇārammaṇā": "с безмерным объектом",
    "atītārammaṇā": "с прошлым объектом", "anāgatārammaṇā": "с будущим объектом",
    "paccuppannārammaṇā": "с настоящим объектом",
    "hīnā": "низший", "majjhimā": "средний", "paṇītā": "высший", "niyatā": "предопределённый",
    "micchatta": "ложное", "sammatta": "правильное",
    "atītā": "прошлый", "anāgatā": "будущий", "paccuppannā": "настоящий", "bahiddhā": "внешний",
    "saṅkhatā": "обусловленный", "asaṅkhatā": "необусловленный", "rūpino": "материальный",
    "arūpino": "нематериальный", "lokiyā": "мирской", "uttarā": "надмирский", "viññeyyā": "познаваться",
    "sāsavā": "подверженный влечениям", "anāsavā": "свободный от влечений",
    "āsavavippayuttā": "не связанный с влечениями",
    "saṃyojaniyā": "подверженный оковам", "saṃyojanavippayuttā": "не связанный с оковами",
    "ganthaniyā": "подверженный узам", "ganthavippayuttā": "не связанный с узами",
    "nīvaraṇiyā": "подверженный помехам", "nīvaraṇavippayuttā": "не связанный с помехами",
    "parāmaṭṭhā": "затронутый искажениями", "parāmāsavippayuttā": "не связанный с искажениями",
    "upādānavippayuttā": "не связанный с цепляниями", "kilesavippayuttā": "не связанный с омрачениями",
    "cetasikā": "сопутствующий уму", "cittavippayuttā": "не связанный с умом",
    "saṃsaṭṭhā": "соединённый", "saṃsaṭṭha": "соединённый", "cittasaṃsaṭṭhā": "соединённый с умом",
    "cittavisaṃsaṭṭhā": "не соединённый с умом", "samuṭṭhānā": "порождённый", "samuṭṭhāna": "порождённый",
    "cittasamuṭṭhānā": "порождённый умом", "sahabhuno": "сосуществующий",
    "cittasahabhuno": "сосуществующий с умом", "anuparivattino": "следующий за",
    "cittānuparivattino": "следующий за умом",
    "cittasaṃsaṭṭhasamuṭṭhānā": "соединённый с умом и порождённый им",
    "cittasaṃsaṭṭhasamuṭṭhānānuparivattino": "соединённый с умом порождённый им и следующий за ним",
    "ajjhattikā": "относящийся к внутреннему", "bāhirā": "относящийся к внешнему",
    "niyyānikā": "ведущий к освобождению", "sauttarā": "над которым есть высшее",
    "anuttarā": "над которым нет высшего", "raṇā": "борьба",
    # roots (1-1441 ff.)
    "hetū": "корни", "kusalahetu": "благой корень", "kusalahetū": "благие корни",
    "akusalahetū": "неблагие корни", "abyākatahetū": "этически неопределённые корни",
    "vipākahetu": "корень являющийся результатом действий", "kiriyahetu": "функциональный корень",
    "lobho": "жадность", "doso": "злоба", "alobho": "отсутствие жадности", "adoso": "отсутствие злобы",
    "amoho": "отсутствие заблуждения",
    "uppanne hetū": "возникшие в них корни", "hetū ekato uppajjanti": "корни возникают вместе",
    # defilement lists
    "āsavo": "влечение", "āsavā": "влечения", "kāmāsavo": "влечение к чувственным удовольствиям",
    "bhavāsavo": "влечение к существованию", "diṭṭhāsavo": "влечение воззрений",
    "avijjāsavo": "влечение неведения", "bhava": "существование", "avijjā": "неведение",
    "diṭṭhi": "воззрение",
    "saṃyojanaṃ": "оковы", "saṃyojanā": "оковы", "kāmarāgasaṃyojanaṃ": "оковы чувственной страсти",
    "paṭighasaṃyojanaṃ": "оковы неприязни", "mānasaṃyojanaṃ": "оковы самомнения",
    "diṭṭhisaṃyojanaṃ": "оковы воззрений", "vicikicchāsaṃyojanaṃ": "оковы колебания",
    "parāmāsasaṃyojanaṃ": "оковы приверженности", "rāgasaṃyojanaṃ": "оковы страсти",
    "issāsaṃyojanaṃ": "оковы зависти", "macchariyasaṃyojanaṃ": "оковы скупости",
    "avijjāsaṃyojanaṃ": "оковы неведения", "paṭigha": "неприязнь", "paṭighaṃ": "неприязнь",
    "māna": "самомнение", "māno": "самомнение", "issā": "зависть", "macchariya": "скупость",
    "rāga": "страсть", "kāmarāga": "чувственная страсть",
    "sīlabbataparāmāsa": "приверженность обрядам и обетам", "sīlabbata": "обряды и обеты",
    "sīla": "обряд", "vata": "обет",
    "ganthā": "узы", "gantho": "узы", "kāyagantho": "телесные узы",
    "abhijjhākāyagantho": "телесные узы алчности", "byāpādo kāyagantho": "телесные узы недоброжелательности",
    "parāmāso kāyagantho": "телесные узы приверженности", "abhiniveso kāyagantho": "телесные узы убеждённости",
    "abhijjhā": "алчность", "byāpādo": "недоброжелательность", "abhiniveso": "убеждённость",
    "sīlabbataparāmāso": "приверженность обрядам и обетам", "sacca": "истинный",
    "oghā": "потоки", "yogā": "ярма",
    "nīvaraṇaṃ": "помеха", "nīvaraṇā": "помехи", "kāmacchandanīvaraṇaṃ": "помеха чувственного желания",
    "byāpādanīvaraṇaṃ": "помеха недоброжелательности", "thinamiddhanīvaraṇaṃ": "помеха вялости и сонливости",
    "uddhaccakukkuccanīvaraṇaṃ": "помеха беспокойства и угрызений",
    "kukkuccanīvaraṇaṃ": "помеха угрызений", "vicikicchānīvaraṇaṃ": "помеха колебания",
    "avijjānīvaraṇaṃ": "помеха неведения", "kāmacchanda": "чувственное желание", "chanda": "желание",
    "byāpāda": "недоброжелательность", "thina": "вялость", "middha": "сонливость",
    "kukkucca": "угрызения", "sasaṅkhārikesu": "с побуждением",
    "parāmāso": "искажение", "parāmāsā": "искажения", "parāmāsaṃ": "искажение",
    "diṭṭhiparāmāso": "искажение из-за воззрения",
    "upādānā": "цепляния", "kāmupādānaṃ": "цепляние за чувственные удовольствия",
    "diṭṭhupādānaṃ": "цепляние за воззрения", "sīlabbatupādānaṃ": "цепляние за обряды и обеты",
    "atta": "самость", "vāda": "учение",
    "kilesā": "омрачения", "vatthūni": "основы", "thinaṃ": "вялость", "uddhaccaṃ": "беспокойство",
    "ahirikaṃ": "бессовестность", "anottappaṃ": "отсутствие страха перед дурным",
    # "X ceva Y" / "X X" pairs (subject + predicate)
    "saṃyojanā ceva saṃyojaniyā": "являющийся оковами и подверженный оковам",
    "saṃyojanāni saṃyojanā": "оковы являются оковами",
    "ganthā ceva ganthaniyā": "являющийся узами и подверженный узам",
    "nīvaraṇā ceva nīvaraṇiyā": "являющийся помехами и подверженный помехам",
    "nīvaraṇāni nīvaraṇā": "помехи являются помехами",
    "upādānā ceva upādāniyā": "являющийся цепляниями и служащий объектом цепляния",
    "upādānāni upādānā": "цепляния являются цепляниями",
    "kilesā kilesā": "омрачения являются омрачениями",
    "saṃyojanavippayuttā saṃyojaniyā": "не связанный с оковами но подверженный оковам",
    "ganthavippayuttā ganthaniyā": "не связанный с узами но подверженный узам",
    "nīvaraṇavippayuttā nīvaraṇiyā": "не связанный с помехами но подверженный помехам",
    "upādānavippayuttā upādāniyā": "не связанный с цепляниями но служащий объектом цепляния",
    "kilesavippayuttā saṃkilesikā": "не связанный с омрачениями но подверженный омрачению",
    # "na vattabbā X" phrases
    "vattabbo savitakkasavicāro": "определить … как явления с направленной мыслью и удержанием мысли",
    "vattabbaṃ pītisahagatanti": "определить как явления сопровождаемые восторгом",
    "vattabbā parittārammaṇā": "определить … как явления с ограниченным объектом",
    "vattabbā maggārammaṇā": "определить … как явления имеющие объектом путь",
    "vattabbā anuppannā": "определить как невозникшие явления",
    "vattabbā atītārammaṇā": "определить … как явления с прошлым объектом",
    "vattabbaṃ ajjhattārammaṇanti": "определить … как явления с внутренним объектом",
    # dhammā phrases (nominative plural, Russian word order)
    "dhammā kusalā": "благие явления", "dhammā akusalā": "неблагие явления",
    "dhammā abyākatā": "этически неопределённые явления", "abyākatā dhammā": "этически неопределённые явления",
    "vipākadhamma": "способный приносить результаты",
    "vipākadhammadhammā": "явления способные приносить результаты",
    "upādiṇṇupādāniyā": "охваченный цеплянием и служащий его объектом",
    "anupādiṇṇupādāniyā": "не охваченный цеплянием но служащий его объектом",
    "dhammā upādiṇṇupādāniyā": "явления охваченные цеплянием и служащие его объектом",
    "dhammā anupādiṇṇupādāniyā": "явления не охваченные цеплянием но служащие его объектом",
    "dhammā anupādiṇṇaanupādāniyā": "явления не охваченные цеплянием и не служащие его объектом",
    "dhammā savitakkasavicārā": "явления с направленной мыслью и удержанием мысли",
    "dhammā avitakkavicāramattā": "явления без направленной мысли только с удержанием мысли",
    "dhammā avitakkaavicārā": "явления без направленной мысли и без удержания мысли",
    "dhammā pītisahagatā": "явления сопровождаемые восторгом",
    "dhammā sukhasahagatā": "явления сопровождаемые счастьем",
    "dhammā upekkhāsahagatā": "явления сопровождаемые невозмутимостью",
    "dhammā na pītisahagatā": "явления не сопровождаемые восторгом",
    "dhammā na sukhasahagatā": "явления не сопровождаемые счастьем",
    "dhammā na upekkhāsahagatā": "явления не сопровождаемые невозмутимостью",
    "dhammā dassanena pahātabbahetukā": "явления чьи корни устраняются видением истины",
    "dhammā bhāvanāya pahātabbahetukā": "явления чьи корни устраняются развитием ума",
    "dhammā ācayagāmino": "явления ведущие к накоплению",
    "dhammā apacayagāmino": "явления ведущие к убыванию",
    "dhammā nevācayagāmināpacayagāmino": "явления не ведущие ни к накоплению ни к убыванию",
    "dhammā parittā": "ограниченные явления", "dhammā mahaggatā": "возвышенные явления",
    "dhammā appamāṇā": "безмерные явления", "dhammā hīnā": "низшие явления",
    "dhammā majjhimā": "средние явления", "dhammā paṇītā": "высшие явления",
    "dhammā micchattaniyatā": "явления предопределённо ведущие к ложному",
    "dhammā sammattaniyatā": "явления предопределённо ведущие к правильному",
    "dhammā uppannā": "возникшие явления",
    "dhammā sahetukā": "явления имеющие корни", "dhammā ahetukā": "явления не имеющие корней",
    "ahetukā dhammā": "явления не имеющие корней", "dhammā hetuvippayuttā": "явления не связанные с корнями",
    "vippayuttā dhammā": "явления не связанные",
    "dhammā appaccayā": "явления не имеющие условий", "dhammā saṅkhatā": "обусловленные явления",
    "dhammā asaṅkhatā": "необусловленные явления", "dhammā sanidassanā": "видимые явления",
    "dhammā anidassanā": "невидимые явления", "dhammā sappaṭighā": "явления способные к соударению",
    "dhammā appaṭighā": "явления не способные к соударению", "dhammā rūpino": "материальные явления",
    "dhammā arūpino": "нематериальные явления", "dhammā lokiyā": "мирские явления",
    "dhammā lokuttarā": "надмирские явления",
    "dhammā kenaci viññeyyā": "явления познаются тем или иным видом сознания",
    "dhammā sāsavā": "явления подверженные влечениям", "dhammā anāsavā": "явления свободные от влечений",
    "anāsavā dhammā": "явления свободные от влечений",
    "dhammā āsavavippayuttā": "явления не связанные с влечениями",
    "dhammā saṃyojaniyā": "явления подверженные оковам",
    "dhammā asaṃyojaniyā": "явления не подверженные оковам",
    "asaṃyojaniyā dhammā": "явления не подверженные оковам",
    "dhammā saṃyojanavippayuttā": "явления не связанные с оковами",
    "dhammā ganthaniyā": "явления подверженные узам", "dhammā aganthaniyā": "явления не подверженные узам",
    "aganthaniyā dhammā": "явления не подверженные узам",
    "dhammā ganthavippayuttā": "явления не связанные с узами",
    "dhammā nīvaraṇiyā": "явления подверженные помехам",
    "dhammā anīvaraṇiyā": "явления не подверженные помехам",
    "anīvaraṇiyā dhammā": "явления не подверженные помехам",
    "dhammā nīvaraṇavippayuttā": "явления не связанные с помехами",
    "dhammā parāmaṭṭhā": "явления затронутые искажениями",
    "dhammā parāmāsavippayuttā": "явления не связанные с искажениями",
    "dhammā cittavippayuttā": "явления не связанные с умом",
    "dhammā cittasaṃsaṭṭhā": "явления соединённые с умом",
    "dhammā cittavisaṃsaṭṭhā": "явления не соединённые с умом",
    "dhammā cittasamuṭṭhānā": "явления порождённые умом",
    "dhammā no cittasamuṭṭhānā": "явления не порождённые умом",
    "dhammā cittasahabhuno": "явления сосуществующие с умом",
    "dhammā no cittasahabhuno": "явления не сосуществующие с умом",
    "dhammā cittānuparivattino": "явления следующие за умом",
    "dhammā no cittānuparivattino": "явления не следующие за умом",
    "dhammā cittasaṃsaṭṭhasamuṭṭhānā": "явления соединённые с умом и порождённые им",
    "dhammā no cittasaṃsaṭṭhasamuṭṭhānā": "явления не являющиеся соединёнными с умом и порождёнными им",
    "dhammā cittasaṃsaṭṭhasamuṭṭhānasahabhuno":
        "явления соединённые с умом порождённые им и сосуществующие с ним",
    "dhammā no cittasaṃsaṭṭhasamuṭṭhānasahabhuno":
        "явления не являющиеся соединёнными с умом порождёнными им и сосуществующими с ним",
    "dhammā cittasaṃsaṭṭhasamuṭṭhānānuparivattino":
        "явления соединённые с умом порождённые им и следующие за ним",
    "dhammā no cittasaṃsaṭṭhasamuṭṭhānānuparivattino":
        "явления не являющиеся соединёнными с умом порождёнными им и следующими за ним",
    "dhammā ajjhattikā": "явления относящиеся к внутреннему",
    "dhammā bāhirā": "явления относящиеся к внешнему", "dhammā upādā": "производные явления",
    "dhammā upādiṇṇā": "явления охваченные цеплянием",
    "dhammā anupādiṇṇā": "явления не охваченные цеплянием",
    "dhammā upādāniyā": "явления служащие объектом цепляния",
    "dhammā anupādāniyā": "явления не служащие объектом цепляния",
    "anupādāniyā dhammā": "явления не служащие объектом цепляния",
    "dhammā upādānavippayuttā": "явления не связанные с цепляниями",
    "dhammā saṃkilesikā": "явления подверженные омрачению",
    "dhammā asaṃkilesikā": "явления не подверженные омрачению",
    "asaṃkilesikā dhammā": "явления не подверженные омрачению",
    "dhammā saṃkiliṭṭhā": "омрачённые явления", "dhammā asaṃkiliṭṭhā": "неомрачённые явления",
    "asaṃkiliṭṭhā dhammā": "неомрачённые явления",
    "dhammā kilesavippayuttā": "явления не связанные с омрачениями",
    "dhammā savitakkā": "явления с направленной мыслью", "dhammā avitakkā": "явления без направленной мысли",
    "dhammā savicārā": "явления с удержанием мысли", "dhammā avicārā": "явления без удержания мысли",
    "dhammā sappītikā": "явления с восторгом", "dhammā appītikā": "явления без восторга",
    "dhammā pariyāpannā": "явления принадлежащие к кругам существования",
    "dhammā apariyāpannā": "явления не принадлежащие к кругам существования",
    "dhammā niyyānikā": "явления ведущие к освобождению", "dhammā niyatā": "предопределённые явления",
    "dhammā sauttarā": "явления над которыми есть высшее",
    "dhammā anuttarā": "явления над которыми нет высшего",
    "dhammā saraṇā": "явления сопряжённые с борьбой", "dhammā araṇā": "явления свободные от борьбы",
}

# X-sahagata(…) compounds: prefix -> instrumental of the Russian noun
SAHAGATA = {"somanassa": "радостью", "upekkhā": "невозмутимостью", "domanassa": "унынием",
            "lobha": "жадностью", "vicikicchā": "колебанием", "uddhacca": "беспокойством",
            "pīti": "восторгом", "sukha": "счастьем"}

# ------------------------------------------------------------------------------------------ overrides
OVERRIDES = {
    # 1-1393: «служащие его объектом» (as 1-M1-4)
    "1-1393": {"upādāniyā": "служащий его объектом"},
    "1-1394": {"upādāniyā": "служащий его объектом"},
    "1-1395": {"upādāniyā": "служащий его объектом"},
    # sekkhā only as a fragment of asekkhā: the Russian «завершившим обучение» renders asekkhā alone
    "1-1415": {"sekkhā": NDE},
    # «имеют будущий объект» (no «с … объектом» in this segment)
    "1-1433": {"ārammaṇā": "объект", "anāgatārammaṇā": "имеющий будущий объект"},
    # 1-1429: «имеющие объектом путь» / «имеющие корнем путь» (as 1-M1-16)
    "1-1429": {"ārammaṇā": "имеющий объектом", "hetukā": "имеющий корнем"},
    # sahetukā / ahetukā: «имеющие корни» (as 1-M2-2)
    "1-1443": {"hetukā": "имеющий корни"},
    "1-1444": {"hetukā": "имеющий корни"},
    "1-1448": {"hetukā": "имеющий корни"},
    # hetusampayuttā / hetuvippayuttā: stem hetu = корень («с корнями»)
    # sārammaṇā / anārammaṇā: «имеющие объект» (as 1-M2-55)
    "1-1525": {"ārammaṇā": "имеющий объект"},
    "1-1526": {"ārammaṇā": "имеющий объект"},
    # na dassanena / na bhāvanāya pahātabbahetukā: «не имеющие корней, устраняемых …»
    "1-1586": {"pahātabba": "устраняемый", "hetukā": "имеющий корни",
               "pahātabbahetukā": "имеющий корни устраняемые"},
    "1-1588": {"pahātabba": "устраняемый", "hetukā": "имеющий корни",
               "pahātabbahetukā": "имеющий корни устраняемые"},
    # appītikā: «без восторга» -> positive part
    "1-1594": {"pītikā": "восторг"},
    # kāma in kāmāsava / kāmupādāna = «чувственные удовольствия»; in kāmarāga / kāmacchanda = «чувственный»
    "1-1465": {"kāma": "чувственные удовольствия"},
    "1-1553": {"kāma": "чувственные удовольствия"},
    "1-1477": {"kāma": "чувственный"},
    "1-1503": {"kāma": "чувственный"},
    # «не устраняются ни видением истины, ни развитием ума» (finite verb)
    "1-1407": {"pahātabbā": "устраняться"},
    # «не относятся ни к обучающимся, ни к завершившим обучение»
    "1-1416": {"sekkha": "относящийся … к обучающимся",
               "asekkhā": "относящийся … к завершившим обучение"},
    # colophon: Dhamma = stem of Dhammasaṅgaṇī
    "1-1616": {"dhamma": "явление"},
}


def rule(bid, kw, kws):
    """Context rules; return None when no rule applies."""
    k = lc(kw)
    s = set(lc(x) for x in kws)
    ru = RU.get(bid, "")
    low = ru.lower()
    if k in ("kusalato",):
        return "благой ум" if "из благого ума" in low else "в благом виде"
    if k == "kiriyato":
        return "функциональный ум" if "из функционального ума" in low else "в функциональном виде"
    if k == "vipākato":
        return "результаты" if "из результатов" in low else "в виде результатов действий"
    if k == "vipākato ca kiriyato":
        return "в виде результатов действий и в функциональном виде"
    if k == "kusalato ca vipākato":
        return "в благом виде и в виде результатов действий"
    if k in ("avacara", "avacarā", "avacaraṃ", "avacarassa"):
        return "относящийся к миру" if "относящ" in low else "мир"
    if k == "rūpa":
        return "видимая форма" if "rūpāyatanaṃ" in s else "форма"
    if k in ("parāmāsa", "parāmāso") and ("sīlabbata" in s or "sīlabbataparāmāsa" in s
                                           or "sīlabbataparāmāso" in s):
        return "приверженность"
    if k.endswith(("sahagata", "sahagatā", "sahagataṃ", "sahagato", "sahagatesu")) and k not in T5:
        for pre, ins in SAHAGATA.items():
            if k.startswith(pre):
                return "сопровождаемый " + ins
    return None


def resolve(bid, kw, kws):
    ov = OVERRIDES.get(bid, {})
    if kw in ov:
        return ov[kw]
    if lc(kw) in ov:
        return ov[lc(kw)]
    r = rule(bid, kw, kws)
    if r is not None:
        return r
    k = lc(kw)
    for table in (T5, MATRIX, CH2, CORE):
        if k in table:
            return table[k]
        if kw in table:
            return table[kw]
    raise KeyError(kw)


if __name__ == "__main__":
    build_part(PART, resolve)
    verify(PART, show=200)
    if "--pairs" in sys.argv:
        c = collections.Counter()
        for bid, kws in read_keywords(PART):
            for kw in kws:
                c[(kw, resolve(bid, kw, kws))] += 1
        for (kw, v), n in sorted(c.items(), key=lambda x: (lc(x[0][0]), x[0][1])):
            print(f"{n:4d}  {kw} = {v}")
