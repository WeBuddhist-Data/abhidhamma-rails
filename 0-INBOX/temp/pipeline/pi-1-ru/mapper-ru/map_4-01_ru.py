"""Pāli->Russian keyword map for pi-1 part 4-01-nikkhepakandam (Nikkhepakaṇḍa, triads + first four
pair clusters).

usage: python -I -X utf8 map_4-01_ru.py      (writes 4-01-nikkhepakandam.mapped.md and verifies it)

Resolution order per keyword: OVERRIDES[bid][kw]  ->  context rules (ctx)  ->  table T (lower-case
first letter). Every value is the word or phrase of THAT segment's Russian
(AI_translation/russian/pi-1-russian-plain-zeroshot_split_chapters/4-01-nikkhepakandam.md), in dictionary
form, following ru-map-conventions.md. Decisions new to this part: notes-map-4-01.md.
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_ru import GAP, NDE, build_part, lc, verify  # noqa: E402

PART = "4-01-nikkhepakandam"

# ------------------------------------------------------------------------------------------- recurring phrases
SAS = "подверженные влечениям"
NOT_INCL = "не принадлежащие к кругам существования"

T = {
    # ---- headings / colophon
    "kaṇḍaṃ": "раздел", "kaṇḍe": "раздел", "nikkhepa": "сводка", "nikkhepaṃ": "сводка",
    "duka": "пары", "dukaṃ": "пары", "antara": "промежуточный", "antaradukaṃ": "промежуточные пары",
    "hetu": "корень", "āsava": "влечение", "saṃyojana": "оковы", "gantha": "узы",
    "bhāṇa": "чтение вслух", "vāro": "раздел",
    # ---- frame
    "dhammā": "явления", "tattha": "здесь", "yo": "то что", "yā": "то что", "yaṃ": "то что",
    "yañca": "и та … которая", "evarūpā": "такой", "evarūpo": "такой", "evarūpaṃ": "такой",
    "ṭhapetvā": "кроме", "tehi dhammehi": "эти явления", "avasesā": "остальной", "avaseso": "оставшийся",
    "avasesā kusala": "остальной благой", "avasesā sāsavā kusala": "остальной подверженный влечениям благой",
    "dasa": "десять",
    # ---- ethical quality
    "kusala": "благой", "kusalā": "благой", "kusalānaṃ": "благой", "kusalānaṃ dhammānaṃ": "благие явления",
    "kusalānaṃ vā dhammānaṃ": "благие явления", "dhammā kusalā": "благие явления",
    "akusala": "неблагой", "akusalā": "неблагой", "akusalānaṃ": "неблагой",
    "akusalā dhammā": "неблагие явления", "dhammā akusalā": "неблагие явления",
    "akusalānaṃ dhammānaṃ": "неблагие явления",
    "kusalā nākusalā": "ни благой ни неблагой",
    "abyākata": "этически неопределённый", "abyākatā": "этически неопределённый",
    "abyākatā dhammā": "этически неопределённые явления", "dhammā abyākatā": "этически неопределённые явления",
    "abyākatesu vā dhammesu": "этически неопределённые … явления",
    "akusalābyākatā": "неблагой и этически неопределённый",
    "sāsavā": "подверженный влечениям", "āsavā": "влечения",
    "sāsavā kusalākusalā dhammā": f"{SAS} благие и неблагие явления",
    "sāsavā kusalābyākatā dhammā": f"{SAS} благие и этически неопределённые явления",
    "sāsavā kusalākusalābyākatā dhammā": f"{SAS} благие неблагие и этически неопределённые явления",
    "kiriyā": "функциональный", "kiriya": "функциональный", "vipākato": "результат",
    "vipākadhamma": "способный приносить результаты",
    "vipākadhammadhammā": "явления способные приносить результаты",
    # ---- roots, kamma
    "mūlāni": "корни", "mūlaṃ": "корень", "kusalamūlāni": "благие корни", "akusalamūlāni": "неблагие корни",
    "kusalamūlaṃ": "благой корень", "akusalamūlaṃ": "неблагой корень",
    "hetū": "корни", "kusalahetū": "благие корни", "akusalahetū": "неблагие корни",
    "abyākatahetū": "этически неопределённые корни",
    "kāmāvacarahetū": "корни относящиеся к миру чувственных желаний",
    "rūpāvacarahetū": "корни относящиеся к миру форм", "arūpāvacarahetū": "корни относящиеся к миру без форм",
    "apariyāpannahetū": f"корни {NOT_INCL}", "maggahetū": "корни пути",
    "alobho": "отсутствие жадности", "adoso": "отсутствие злобы", "amoho": "отсутствие заблуждения",
    "lobho": "жадность", "doso": "злоба", "moho": "заблуждение", "mohena": "заблуждение",
    "kilesā": "омрачения", "ekaṭṭhā": "пребывающий вместе",
    "ekaṭṭhā ca kilesā": "и омрачения пребывающие вместе",
    "samuṭṭhānaṃ": "порождённый", "samuṭṭhānaṃ kāyakammaṃ": f"порождённое{GAP}телесное действие",
    "kāyakammaṃ": "телесное действие", "vacī": "речевой", "vacīkammaṃ": "речевое действие",
    "manokammaṃ": "умственное действие", "vacīkammaṃ manokammaṃ": "речевое действие умственное действие",
    "kammassa katattā": "вследствие совершённых действий", "kammassa": "действие", "kammāni": "действия",
    # ---- aggregates and spheres
    "khandho": "совокупность", "khandhā": "совокупности",
    "viññāṇakkhandho": "совокупность сознания", "vedanākkhandho": "совокупность чувств",
    "saññākkhandho": "совокупность восприятия", "saṅkhārakkhandho": "совокупность формирующих факторов",
    "rūpakkhandho": "совокупность материальной формы",
    "viññāṇa": "сознание", "viññāṇaṃ": "сознание", "vedanā": "чувство", "vedanaṃ": "чувство",
    "vedanāya": "чувство", "saññā": "восприятие", "saññaṃ": "восприятие",
    "saṅkhāra": "формирующие факторы", "saṅkhārā": "формирующие факторы", "saṅkhāre": "формирующие факторы",
    "rūpaṃ": "материальная форма", "dhātu": "элемент",
    "asaṅkhatā": "необусловленный", "asaṅkhatā ca dhātu": "и необусловленный элемент",
    "asaṅkhatā dhātu": "необусловленный элемент",
    "sampayutto": "связанный", "sampayuttā": "связанный", "vippayuttā": "не связанный",
    "rūpāyatanaṃ": "сфера видимых форм", "cakkhu": "глаз", "cakkhāyatanaṃ": "сфера глаза",
    "sota": "ухо", "sotāyatanaṃ": "сфера уха", "ghāna": "нос", "ghānāyatanaṃ": "сфера носа",
    "jivhā": "язык", "jivhāyatanaṃ": "сфера языка", "kāyāyatanaṃ": "сфера тела",
    "sadda": "звук", "saddāyatanaṃ": "сфера звуков", "gandha": "запах", "gandhāyatanaṃ": "сфера запахов",
    "rasa": "вкус", "rasāyatanaṃ": "сфера вкусов", "phoṭṭhabba": "осязаемое",
    "phoṭṭhabbāyatanaṃ": "сфера осязаемого", "dhammāyatana": "сфера объектов ума",
    # ---- planes
    "kāmāvacarā": "относящийся к миру чувственных желаний", "avacarā": "относящийся к миру",
    "arūpāvacarā": f"относящийся{GAP}к миру без форм", "arūpa": "без форм",
    "kāmāvacare": "в мире чувственных желаний", "rūpāvacare": "в мире форм",
    "arūpāvacare": "в мире без форм", "avacare": "в мире", "bhūmiyaṃ": "уровень",
    "rūpāvacara": "относящийся к миру форм", "arūpāvacara": "относящийся к миру без форм",
    "avacara": "относящийся к миру",
    "maggā": "пути", "apariyāpannā maggā": f"пути {NOT_INCL}", "maggā apariyāpannā": f"пути {NOT_INCL}",
    "phalāni": "плоды", "phalaṃ": "плод",
    # ---- triad items
    "sukhāya": "приятный", "sukhāya vedanāya": "приятное чувство", "dukkhāya": "болезненный",
    "dukkhāya vedanāya": "болезненное чувство", "adukkhamasukhāya": "ни болезненный ни приятный",
    "upādiṇṇa": "охваченный цеплянием", "upādiṇṇā": "охваченный цеплянием",
    "upādāniyā": "служащий его объектом",
    "upādiṇṇupādāniyā": "охваченный цеплянием и служащий его объектом",
    "anupādiṇṇupādāniyā": "не охваченный цеплянием но служащий его объектом",
    "dhammā upādiṇṇupādāniyā": "явления охваченные цеплянием и служащие его объектом",
    "dhammā anupādiṇṇupādāniyā": "явления не охваченные цеплянием но служащие его объектом",
    "dhammā anupādiṇṇaanupādāniyā": "явления не охваченные цеплянием и не служащие его объектом",
    "saṃkiliṭṭha": "омрачённый", "asaṃkiliṭṭha": "неомрачённый", "saṃkilesikā": "подверженный омрачению",
    "vitakka": "направленная мысль", "vicāra": "удержание мысли",
    "dhammā savitakkasavicārā": "явления с направленной мыслью и удержанием мысли",
    "dhammā avitakkavicāramattā": "явления без направленной мысли только с удержанием мысли",
    "dhammā avitakkaavicārā": "явления без направленной мысли и без удержания мысли",
    "sahagatā": "сопровождаемый", "pītisahagatā": "сопровождаемый восторгом", "pīti": "восторг",
    "dhammā pītisahagatā": "явления сопровождаемые восторгом",
    "sukhasahagatā": "сопровождаемый счастьем", "sukha": "счастье",
    "dhammā sukhasahagatā": "явления сопровождаемые счастьем",
    "upekkhāsahagatā": "сопровождаемый невозмутимостью", "upekkhā": "невозмутимость",
    "dhammā upekkhāsahagatā": "явления сопровождаемые невозмутимостью",
    "pahātabbā": "устраняемый", "bhāvanāya pahātabbā": "устраняемый развитием ума",
    "pahātabba": "устраняться", "bhāvanāya pahātabba": "устраняться развитием ума",
    "dassanena": "видение истины", "hetukā": "чьи корни",
    "dhammā dassanena pahātabbahetukā": "явления чьи корни устраняются видением истины",
    "dhammā bhāvanāya pahātabbahetukā": "явления чьи корни устраняются развитием ума",
    "pahātabbahetukā": "чьи корни устраняются",
    "ācaya": "накопление", "apacaya": "убывание", "caya": NDE,
    "dhammā ācayagāmino": "явления ведущие к накоплению",
    "dhammā apacayagāmino": "явления ведущие к убыванию",
    "dhammā neva ācayagāmi": "явления не ведущие ни к накоплению",
    "sekkhā": "относящийся к обучающимся", "asekkhā": "относящийся к завершившим обучение",
    "sāmañña": "отшельничество", "arahatta": "состояние архата", "upariṭṭhimaṃ": "высший",
    "parittā": "ограниченный", "dhammā parittā": "ограниченные явления",
    "mahaggatā": "возвышенный", "dhammā mahaggatā": "возвышенные явления",
    "appamāṇā": "безмерный", "dhammā appamāṇā": "безмерные явления",
    "paritta": "ограниченный", "mahaggata": "возвышенный", "appamāṇa": "безмерный",
    "parittārammaṇā": "с ограниченным объектом", "mahaggatārammaṇā": "с возвышенным объектом",
    "appamāṇārammaṇā": "с безмерным объектом", "atītārammaṇā": "с прошлым объектом",
    "anāgatārammaṇā": "с будущим объектом", "paccuppannārammaṇā": "с настоящим объектом",
    "ārammaṇā": f"с{GAP}объектом", "ārabbha": "имеющий объектом",
    "paritte dhamme": "ограниченные явления", "mahaggate dhamme": "возвышенные явления",
    "appamāṇe dhamme": "безмерные явления", "atīte dhamme": "прошлые явления",
    "anāgate dhamme": "будущие явления", "paccuppanne dhamme": "настоящие явления",
    "paritte dhamme ārabbha": "имеющий объектом ограниченные явления",
    "mahaggate dhamme ārabbha": "имеющий объектом возвышенные явления",
    "appamāṇe dhamme ārabbha": "имеющий объектом безмерные явления",
    "atīte dhamme ārabbha": "имеющий объектом прошлые явления",
    "anāgate dhamme ārabbha": "имеющий объектом будущие явления",
    "paccuppanne dhamme ārabbha": "имеющий объектом настоящие явления",
    "bahiddhā dhamme ārabbha": "имеющий объектом внешние явления",
    "dhamme ārabbha": f"имеющий объектом{GAP}явления",
    "uppajjanti": "возникать", "ārabbha ye uppajjanti": "которые возникают имея объектом",
    "citta": "ум", "cetasikā": "сопутствующий уму", "cittacetasikā": "ум и сопутствующие уму",
    "uppajjanti cittacetasikā": f"ум и сопутствующие уму{GAP}возникать",
    "hīnā": "низший", "dhammā hīnā": "низшие явления", "majjhimā": "средний",
    "dhammā majjhimā": "средние явления", "paṇītā": "высший", "dhammā paṇītā": "высшие явления",
    "niyatā": "предопределённый", "ānantarikāni": "с немедленным воздаянием",
    "dhammā micchattaniyatā": "явления предопределённо ведущие к ложному", "micchatta": "ложное",
    "sammatta": "правильное", "dhammā sammattaniyatā": "явления предопределённо ведущие к правильному",
    "ariya": "благородный", "ariyamaggaṃ": "благородный путь", "ariyamagga": "благородный путь",
    "magga": "путь", "samaṅgissa": "обладать", "aṅgāni": "факторы", "adhipatino": "находящийся под главенством",
    "bhāvayantassa": "развивать", "maggaṃ bhāvayantassa": "развивать путь", "vīmaṃsā": "пытливость",
    "sammā": "правильный", "diṭṭhi": "воззрение",
    # ---- arisen / past / future / present
    "uppannā": "возникший", "dhammā uppannā": "возникшие явления", "jātā": "рождённый",
    "sañjātā": "зародившийся", "nibbattā": "появившийся", "abhinibbattā": "полностью появившийся",
    "pātubhūtā": "проявившийся", "samuppannā": "полностью возникший", "uṭṭhitā": "поднявшийся",
    "samuṭṭhitā": "полностью поднявшийся", "aṃsena": "категория",
    "uppādino": "возникнуть", "avipakkavipākānaṃ": "чьи результаты ещё не созрели",
    "niruddhā": "прекратившийся", "vigatā": "исчезнувший", "vipariṇatā": "изменившийся",
    "abbhatthaṅgatā": "полностью угасший", "uppajjitvā": "после возникновения",
    "dhammā atītā": "прошлые явления", "dhammā anāgatā": "будущие явления",
    "dhammā paccuppannā": "настоящие явления",
    "tesaṃ tesaṃ": "тот или иной", "paccattaṃ": "собственный", "pāṭipuggalikā": "индивидуальный",
    "puggalānaṃ": "личность", "bahiddhā": "внешний", "dhammā bahiddhā": "внешние явления",
    "dhamme": "явления",
    # ---- visible / impinging / material
    "sanidassana": "видимый", "anidassana": "невидимый", "sappaṭighā": "способный к соударению",
    "appaṭighaṃ": "не способный к соударению", "anidassanaṃ": "невидимый",
    "sanidassanā": "видимый", "dhammā sanidassanā": "видимые явления",
    "anidassanā": "невидимый", "dhammā anidassanā": "невидимые явления",
    "dhammā sappaṭighā": "явления способные к соударению",
    "dhammā appaṭighā": "явления не способные к соударению",
    "upādāya": "производный", "bhūtā": "элементы", "mahābhūtā": "великие элементы",
    "upādāya rūpaṃ": "материальная форма производная",
    "rūpino": "материальный", "dhammā rūpino": "материальные явления",
    "arūpino": "нематериальный", "dhammā arūpino": "нематериальные явления",
    "dhammā appaccayā": "явления не имеющие условий",
    "saṅkhatā": "обусловленный", "dhammā saṅkhatā": "обусловленные явления",
    "dhammā asaṅkhatā": "необусловленные явления", "yeva": "те самые",
    "lokiyā": "мирской", "dhammā lokiyā": "мирские явления", "dhammā lokuttarā": "надмирские явления",
    "uttarā": "надмирский",
    "na": "не", "viññeyyā": "познаваемый",
    "dhammā kāya": f"явления{GAP}осязательный", "dhammā sota": f"явления{GAP}слуховой",
    "dhammā cakkhu": f"явления{GAP}зрительный", "dhammā ghāna": f"явления{GAP}обонятельный",
    "dhammā jivhā": f"явления{GAP}вкусовой",
    # ---- root pairs
    "dhammā sahetukā": "явления имеющие корни", "dhammā ahetukā": "явления не имеющие корней",
    "dhammā hetuvippayuttā": "явления не связанные с корнями",
    # ---- three fetters / views
    "saṃyojanāni": "оковы", "sakkāya": "самость", "sakkāyadiṭṭhi": "воззрение о самости",
    "vicikicchā": "колебание", "parāmāso": "приверженность", "sīlabbataparāmāso": "приверженность обрядам и обетам",
    "parāmāsa": "приверженность", "sīlabbataparāmāsa": "приверженность обрядам и обетам",
    "sīlabbataparāmāsaṃ": "приверженность обрядам и обетам",
    "sīla": "обряд", "vata": "обет", "sīlabbata": "обряды и обеты",
    "assutavā": "не слышавший Учения", "puthujjano": "обычный человек", "ariyānaṃ": "благородные",
    "dhammassa": "Учение", "akovido": "не сведущий", "avinīto": "не обученный",
    "sappurisānaṃ": "достойные люди", "purisānaṃ": "люди", "samanupassati": "считать", "attato": "самость",
    "rūpavantaṃ": "обладающий материальной формой",
    "diṭṭhigataṃ": "приверженность воззрениям", "gahanaṃ": "дебри", "kantāro": "пустыня",
    "visūkāyikaṃ": "извращённость", "vipphanditaṃ": "метания", "saṃyojanaṃ": "оковы",
    "diṭṭhisaṃyojanaṃ": "оковы воззрений", "gāho": "хватка", "paṭiggāho": "цепкость",
    "patiṭṭhāho": "закрепление", "abhiniveso": "приверженность", "kummaggo": "кривая дорога",
    "maggo": "дорога", "micchā": "ложный", "micchāpatho": "ложный путь", "patho": "путь",
    "micchattaṃ": "ложность", "tittha": "сектантские учения", "vipariyāsa": "превратный",
    "vipariyāsaggāho": "превратная хватка", "micchādiṭṭhi": "ложное воззрение",
    # doubt
    "satthari": "Учитель", "sikkhāya": "обучение", "kaṅkhati": "сомневаться", "kaṅkhā": "сомнение",
    "vimati": "неуверенность", "dveḷhakaṃ": "раздвоенность", "dvedhāpatho": "распутье",
    "saṃsayo": "нерешительность", "anekaṃsaggāho": "неспособность прийти к определённости",
    "ekaṃsa": "определённость", "āsappanā": "блуждание", "parisappanā": "беспорядочное блуждание",
    "apariyogāhanā": "отсутствие углубления", "pariyogāhanā": "углубление",
    "thambhitattaṃ": "оцепенелость", "cittassa": "ум", "mano": "ум", "vilekho": "терзание",
    "idappaccayatā": "закон обусловленности", "samuppannesu": "возникший",
    "samuppannesu dhammesu": "явления возникшие", "paṭicca": "в зависимости от условий",
    "paṭiccasamuppannesu": "возникший в зависимости от условий",
    "paṭiccasamuppannesu dhammesu": "явления возникшие в зависимости от условий",
    # rules and observances
    "ito": "это", "samaṇa": "отшельник", "brāhmaṇānaṃ": "брахман", "suddhi": "чистота",
    # ---- alobha / adosa / amoha
    "lubbhanā": "проявление жадности", "sārajjanā": "проявление страсти", "anabhijjhā": "отсутствие алчности",
    "asārāgo": "отсутствие страсти", "abyāpajjo": "отсутствие неприязни", "byāpajjo": "неприязнь",
    "dussanā": "проявление злобы", "abyāpādo": "отсутствие недоброжелательности",
    "metti": "доброжелательность", "mettāyanā": "проявление доброжелательности", "anuddā": "участие",
    "anuddāyanā": "проявление участия", "hitesitā": "желание блага", "hita": "благо",
    "anukampā": "сострадание",
    "dukkhe": "страдание", "dukkhe ñāṇaṃ": "знание страдания", "ñāṇaṃ": "знание",
    "samudaye": "возникновение", "nirodhe": "прекращение", "dukkhanirodhe": "прекращение страдания",
    "paññā": "мудрость", "pajānanā": "понимание", "vicayo": "исследование",
    "pavicayo": "тщательное исследование", "dhammavicayo": "исследование явлений",
    "sallakkhaṇā": "различение", "upalakkhaṇā": "распознавание", "paccupalakkhaṇā": "точное распознавание",
    "paṇḍiccaṃ": "учёность", "kosallaṃ": "умелость", "nepuññaṃ": "тонкость", "vebhabyā": "ясность суждения",
    "cintā": "размышление", "upaparikkhā": "проверка", "bhūrī": "широта ума", "medhā": "разумность",
    "pariṇāyikā": "руководящая сила", "vipassanā": "прозрение", "sampajaññaṃ": "ясное понимание",
    "patodo": "стрекало", "indriyaṃ": "способность", "paññindriyaṃ": "способность мудрости",
    "balaṃ": "сила", "paññābalaṃ": "сила мудрости", "satthaṃ": "меч", "paññāsatthaṃ": "меч мудрости",
    "pāsādo": "башня", "paññāpāsādo": "башня мудрости", "āloko": "свет", "paññāāloko": "свет мудрости",
    "obhāso": "сияние", "paññāobhāso": "сияние мудрости", "pajjoto": "светоч",
    "paññāpajjoto": "светоч мудрости", "ratanaṃ": "сокровище", "paññāratanaṃ": "сокровище мудрости",
    "sambojjha": "пробуждение", "aṅgo": "фактор", "maggaṅgaṃ": "фактор пути",
    # ---- lobha string
    "rāgo": "страсть", "sārāgo": "пристрастие", "anunayo": "расположенность", "anurodho": "потакание",
    "nandī": "наслаждение", "icchā": "хотение", "mucchā": "одурманенность", "gedho": "жадное стремление",
    "paligedho": "сильное жадное стремление", "saṅgo": "привязанность", "paṅko": "трясина", "ejā": "трепет",
    "māyā": "наваждение", "janikā": "порождающая сила", "sañjananī": "производящая сила",
    "sibbinī": "сшивающая сила", "jālinī": "опутывающая сила", "saritā": "увлекающая сила",
    "visattikā": "липкая сила", "suttaṃ": "нить", "visaṭā": "расползающаяся сила",
    "āyūhinī": "побуждающая сила", "dutiyā": "спутница", "paṇidhi": "устремление", "netti": "проводник",
    "bhava": "существование", "vanaṃ": "лес", "vanatho": "чаща", "santhavo": "близость", "sineho": "приязнь",
    "apekkhā": "томление", "paṭibandhu": "родство", "āsā": "надежда", "āsisanā": "упование",
    "dhana": "богатство", "putta": "дети", "jīvita": "жизнь", "jappā": "тяга", "pajappā": "сильная тяга",
    "abhijappā": "чрезмерная тяга", "jappanā": "проявление тяги", "loluppaṃ": "падкость",
    "loluppāyanā": "проявление падкости", "pucchañjikatā": "угодливость", "sādhu": "лучшее",
    "kamyatā": "желание", "adhamma": "неправедный", "visama": "непомерный", "nikanti": "тяготение",
    "nikāmanā": "страстное желание", "patthanā": "чаяние", "pihanā": "вожделение",
    "sampatthanā": "сильное чаяние", "taṇhā": "жажда", "vibhava": "несуществование",
    "nirodha": "прекращение", "ogho": "поток", "yogo": "ярмо", "gantho": "узы", "upādānaṃ": "цепляние",
    "āvaraṇaṃ": "препятствие", "nīvaraṇaṃ": "помеха", "chādanaṃ": "покров", "bandhanaṃ": "путы",
    "upakkileso": "загрязнение", "anusayo": "скрытая склонность", "pariyuṭṭhānaṃ": "одержимость",
    "latā": "лиана", "vevicchaṃ": "скаредность", "dukkha": "страдание", "nidānaṃ": "источник",
    "pabhavo": "исток", "pāso": "силки", "baḷisaṃ": "крючок", "visayo": "владения", "nadī": "река",
    "gaddulaṃ": "привязь", "samuddo": "океан", "abhijjhā": "алчность",
    # ---- dosa string
    "anatthaṃ": "вред", "acarīti": "причинить", "acarī": "причинить", "caratīti": "причинять",
    "āghāto": "досада", "jāyati": "возникать", "āghāto jāyati": "возникать досада",
    "piyassa": "дорогой", "manāpassa": "приятный", "aṭṭhāne": "без повода",
    "paṭighāto": "раздражение", "paṭighaṃ": "неприязнь", "paṭivirodho": "противодействие",
    "kopo": "негодование", "pakopo": "сильное негодование", "sampakopo": "крайнее негодование",
    "padoso": "сильная злоба", "sampadoso": "крайняя злоба", "byāpatti": "недоброжелательность",
    "kodho": "гнев", "kujjhanā": "гневливость", "dussitattaṃ": "состояние злобы",
    "byāpajjanā": "проявление недоброжелательности", "virodho": "вражда", "caṇḍikkaṃ": "свирепость",
    "asuropo": "грубость", "anattamanatā": "недовольство",
    # ---- moha string
    "aññāṇaṃ": "незнание", "dukkhe aññāṇaṃ": "незнание страдания", "adassanaṃ": "отсутствие видения",
    "dassanaṃ": "видение", "anabhisamayo": "отсутствие постижения", "ananubodho": "отсутствие понимания",
    "anubodho": "понимание", "asambodho": "непробуждённость", "sambodho": "пробуждённость",
    "appaṭivedho": "отсутствие проникновения", "asaṃgāhanā": "неохватывание",
    "asamapekkhanā": "отсутствие рассмотрения", "samapekkhanā": "рассмотрение",
    "apaccavekkhaṇā": "отсутствие обдумывания", "paccavekkhaṇā": "обдумывание",
    "apaccakkhakammaṃ": "неспособность видеть воочию", "paccakkhakammaṃ": "способность видеть воочию",
    "dummejjhaṃ": "тупость", "bālyaṃ": "глупость", "asampajaññaṃ": "отсутствие ясного понимания",
    "pamoho": "сильное заблуждение", "sammoho": "полное заблуждение", "avijjā": "неведение",
    "laṅgī": "засов",
    # ---- taints
    "āsavo": "влечение", "kāmāsavo": "влечение к чувственным удовольствиям",
    "bhavāsavo": "влечение к существованию", "diṭṭhāsavo": "влечение воззрений",
    "avijjāsavo": "влечение неведения", "avijjāsavena": "влечение неведения",
    "kāmesu": "чувственные удовольствия", "chando": "желание", "kāmarāgo": "чувственная страсть",
    "pariḷāho": "жар",
    "vuccati kāmāsavo": "называется влечение к чувственным удовольствиям",
    "vuccati bhavāsavo": "называется влечение к существованию",
    "vuccati diṭṭhāsavo": "называется влечение воззрений",
    "vuccati avijjāsavo": "называется влечение неведения",
    "sassato": "вечный", "sarīranti": "плоть", "sarīraṃ": "плоть", "jīvaṃ": "душа", "aññaṃ": "другой",
    "hoti": "существовать", "hoti tathāgato": "Татхагата существовать", "maraṇāti": "смерть",
    "maraṇā": "смерть",
    "anāsavā": "свободный от влечений", "dhammā sāsavā": "явления подверженные влечениям",
    "dhammā anāsavā": "явления свободные от влечений",
    "āsavavippayuttā": "не связанный с влечениями",
    "dhammā āsavavippayuttā": "явления не связанные с влечениями",
    # ---- fetters
    "saṃyojanā": "оковы", "kāmarāgasaṃyojanaṃ": "оковы чувственной страсти",
    "paṭighasaṃyojanaṃ": "оковы неприязни", "mānasaṃyojanaṃ": "оковы самомнения",
    "vicikicchāsaṃyojanaṃ": "оковы колебания",
    "sīlabbataparāmāsasaṃyojanaṃ": "оковы приверженности обрядам и обетам",
    "bhavarāgasaṃyojanaṃ": "оковы страсти к существованию", "issāsaṃyojanaṃ": "оковы зависти",
    "macchariyasaṃyojanaṃ": "оковы скупости", "avijjāsaṃyojanaṃ": "оковы неведения",
    "avijjāsaṃyojanena": "оковы неведения",
    "paṭigha": "неприязнь", "māna": "самомнение", "issā": "зависть", "rāga": "страсть",
    "kāmarāga": "чувственная страсть", "macchariya": "скупость", "kāmacchando": "чувственное желание",
    "vuccati kāmarāgasaṃyojanaṃ": "называется оковы чувственной страсти",
    "vuccati paṭighasaṃyojanaṃ": "называется оковы неприязни",
    "vuccati mānasaṃyojanaṃ": "называется оковы самомнения",
    "vuccati diṭṭhisaṃyojanaṃ": "называется оковы воззрений",
    "vuccati vicikicchāsaṃyojanaṃ": "называется оковы колебания",
    "vuccati sīlabbataparāmāsasaṃyojanaṃ": "называется оковы приверженности обрядам и обетам",
    "vuccati bhavarāgasaṃyojanaṃ": "называется оковы страсти к существованию",
    "vuccati issāsaṃyojanaṃ": "называется оковы зависти",
    "vuccati macchariyasaṃyojanaṃ": "называется оковы скупости",
    "vuccati avijjāsaṃyojanaṃ": "называется оковы неведения",
    # conceit, envy, stinginess
    "maññanā": "зазнайство", "maññitattaṃ": "состояние зазнайства", "unnati": "превознесение",
    "unnamo": "надменность", "dhajo": "знамя", "sampaggāho": "возвеличивание себя",
    "ketukamyatā": f"желание{GAP}поднять свой стяг", "ketu": "стяг", "sadiso": "равный", "hīno": "хуже",
    "issāyanā": "проявление зависти", "usūyā": "ревность", "usūyanā": "проявление ревности",
    "para": "другие", "sakkāra": "почести", "garukāra": "уважение", "mānana": "почитание",
    "vandana": "поклоны", "pūjanāsu": "поклонение",
    "macchariyāni": "виды скупости", "āvāsa": "жилище", "kula": "семьи-покровители", "vaṇṇa": "похвала",
    "maccharāyanā": "проявление скупости", "kadariyaṃ": "прижимистость", "kaṭukañcukatā": "мелочность",
    "aggahitattaṃ": "зажатость",
    "dhammā saṃyojanā": "явления являющиеся оковами",
    "saṃyojaniyā": "подверженный оковам", "dhammā saṃyojaniyā": "явления подверженные оковам",
    "dhammā asaṃyojaniyā": "явления не подверженные оковам",
    "saṃyojanavippayuttā": "не связанный с оковами",
    "dhammā saṃyojanavippayuttā": "явления не связанные с оковами",
    "saṃyojanā ceva saṃyojaniyā": "оковы и подверженный оковам",
    "saṃyojanavippayuttā saṃyojaniyā": "не связанный с оковами но подверженный оковам",
    # ---- ties
    "kāyagantho": "телесные узы", "byāpādo": "недоброжелательность", "ganthā": "узы", "sacca": "истинный",
    "abhijjhā kāyagantho": "телесные узы алчности", "abhijjhākāyaganthena": "телесные узы алчности",
    "byāpādo kāyagantho": "телесные узы недоброжелательности",
    "sīlabbataparāmāso kāyagantho": "телесные узы приверженности обрядам и обетам",
    "sīlabbataparāmāsaṃ kāyaganthaṃ": "телесные узы приверженности обрядам и обетам",
    "idaṃ saccābhiniveso kāyagantho": "телесные узы приверженности убеждению «только это истинно»",
    "idaṃsaccābhiniveso kāyagantho": "телесные узы приверженности убеждению «только это истинно»",
    "vuccati abhijjhā kāya": f"называется телесные{GAP}алчность",
    "vuccati byāpādo kāya": f"называется телесные{GAP}недоброжелательность",
    "vuccati sīlabbataparāmāso kāya": f"называется телесные{GAP}приверженность обрядам и обетам",
    "vuccati idaṃsaccābhiniveso kāya":
        f"называется телесные{GAP}приверженность убеждению «только это истинно»",
    "moghamaññanti": "всё прочее ложно",
    "ganthaniyā": "подверженный узам", "dhammā ganthaniyā": "явления подверженные узам",
    "dhammā aganthaniyā": "явления не подверженные узам",
    "ganthavippayuttā": "не связанный с узами", "dhammā ganthavippayuttā": "явления не связанные с узами",
    "ganthā ceva ganthaniyā": "узы и подверженный узам",
    "ganthavippayuttā ganthaniyā": "не связанный с узами но подверженный узам",
}

# lobha-string segments (rūpāsā / rūpataṇhā …, kāmataṇhā, dhammataṇhā)
LOBHA = {"1-1065", "1-1141"}
SENSE_CONS = {"cakkhu": "зрительный", "sota": "слуховой", "ghāna": "обонятельный", "jivhā": "вкусовой"}


def ctx(bid, k, s):
    """Context rules; return None to fall through to the table."""
    if k == "rūpa":
        if any("rūpāvacar" in x for x in s):
            return "форма"
        if bid in LOBHA or "rūpāyatanaṃ" in s:
            return "видимая форма"
        return "материальная форма"
    if k == "rūpāvacarā":                              # contiguous only where no kāmāvacarā precedes
        return f"относящийся{GAP}к миру форм" if "kāmāvacarā" in s else "относящийся к миру форм"
    if k == "kāma":
        if any("āvacar" in x for x in s):
            return "чувственные желания"
        if "kāmesu" in s or any(x.startswith("kāmarāga") for x in s):
            return "чувственный"
        return "чувственные удовольствия"
    if k == "kāya":
        if "kāyagantho" in s or "kāyakammaṃ" in s:
            return "телесный"
        if "kāyāyatanaṃ" in s:
            return "тело"
        if "viññeyyā" in s:
            return "осязательный"
    if "viññeyyā" in s and k in SENSE_CONS:            # 1-1101: «познаваемые зрительным сознанием» …
        return SENSE_CONS[k]
    if k == "parāmāso":
        return "искажение" if "diṭṭhigataṃ" in s else "приверженность"
    if k == "mano" and "manokammaṃ" in s:
        return "умственный"
    if k == "dhamma":
        if bid in LOBHA or "dhammāyatana" in s:
            return "объекты ума"
        return "Учение"                                # 1-1127 dhammamacchariyaṃ
    if k == "dhamme" and "satthari" in s:
        return "Учение"
    if k == "niyatā" and "pāṭipuggalikā" in s:
        return "закреплённый"
    if k == "bahiddhā" and "samaṇa" in s:
        return "вне"
    if k in ("patho", "gāho") and "dvedhāpatho" in s:  # inside «распутье» / «неспособность прийти к …»
        return NDE
    return None


OVERRIDES = {
    # «Какие явления устраняются …?» with no participle in the segment
    "1-1006": {"pahātabbā": "устраняться"},
    "1-1012": {"pahātabbā": "устраняться"},
    # hetukā read by its Russian
    "1-1013": {"hetukā": "иметь корни",
               "dhammā dassanena pahātabbahetukā": "явления имеющие корни которые устраняются видением истины"},
    "1-1039": {"hetukā": "имеющий корнем"},
    "1-1079": {"hetukā": "имеющий корни"},
    "1-1080": {"hetukā": "имеющий корни"},
    "1-1084": {"hetukā": "иметь корни"},
    # maggārammaṇā: «имеющие объектом путь»
    "1-1038": {"ārammaṇā": "имеющий объектом"},
    # sekkhā only as the member of asekkhā («завершившие обучение»): no word of its own
    "1-1024": {"sekkhā": NDE},
    # «не относящиеся ни к обучающимся, ни к завершившим обучение»
    "1-1025": {"sekkhā": f"относящийся{GAP}к обучающимся",
               "asekkhā": f"относящийся{GAP}к завершившим обучение"},
    # «То самое явление, которое …»
    "1-1092": {"yo": "то самое", "Yo": "то самое"},
}


def resolve(bid, kw, kws):
    ov = OVERRIDES.get(bid, {})
    if kw in ov:
        return ov[kw]
    k = lc(kw)
    s = set(lc(x) for x in kws)
    v = ctx(bid, k, s)
    if v is not None:
        return v
    return T[k]


if __name__ == "__main__":
    build_part(PART, resolve)
    verify(PART, show=200)
