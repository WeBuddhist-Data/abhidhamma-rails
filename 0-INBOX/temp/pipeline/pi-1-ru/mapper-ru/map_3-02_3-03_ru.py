"""Pāli->Russian keyword maps for pi-1 parts 3-02-rupakandam and 3-03-rupakandam (Rūpavibhatti:
pairs ... elevens).

usage: python -I -X utf8 map_3-02_3-03_ru.py     (writes the two <part>.mapped.md and verifies them)

Resolution order per keyword: OVERRIDES[bid][kw] -> context rules (resolve) -> RUPA table.
Values follow ru-map-conventions.md and the fixed phrase tables of build_3-02_3-03_ru.py
(the Russian of these parts was generated from them; harmonise-log.tsv has no entry for them).
Decisions: notes-map-3-02_3-03.md.
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_ru import GAP, build_part, lc, read_russian, verify  # noqa: E402

PARTS = ["3-02-rupakandam", "3-03-rupakandam"]
RF = "материальная форма"
IA = "невидимый и способный к соударению"
SA = "способный к соударению"

# ------------------------------------------------------------------------------ default table
RUPA = {
    # frame, classification terms (predicates of «Какая материальная форма …?»)
    "rūpaṃ": RF, "upādā": "производный", "upādāya": "производный",
    "upādiṇṇaṃ": "охваченный цеплянием", "upādiṇṇa": "охваченный цеплянием",
    "upādāniyaṃ": "служащий его объектом",
    "upādiṇṇupādāniyaṃ": "охваченный цеплянием и служащий его объектом",
    "anupādiṇṇupādāniyaṃ": "не охваченный цеплянием но служащий его объектом",
    "sanidassanaṃ": "видимый", "sanidassanamhi": "видимый",
    "anidassanaṃ": "невидимый", "anidassano": "невидимый", "anidassanena": "невидимый",
    "anidassanamhi": "невидимый",
    "sappaṭighaṃ": SA, "sappaṭigho": SA, "sappaṭighamhi": SA, "appaṭighaṃ": "не " + SA,
    "anidassano sappaṭigho": IA, "anidassanaṃ sappaṭighaṃ": IA, "anidassanasappaṭighaṃ": IA,
    "anidassanamhi sappaṭighamhi": IA, "anidassanena sappaṭighena": IA,
    "sanidassanaṃ sappaṭighaṃ": "видимый и " + SA,
    "rūpaṃ sappaṭighaṃ": f"{RF} способная к соударению",
    "rūpaṃ appaṭighaṃ": f"{RF} не способная к соударению",
    "rūpaṃ cittasamuṭṭhānaṃ": f"{RF} порождённая умом",
    "rūpaṃ cittasahabhu": f"{RF} сосуществующая с умом",
    "rūpaṃ cittānuparivatti": f"{RF} следующая за умом",
    "upādā sappaṭighaṃ": "производный и " + SA, "upādā appaṭighaṃ": "производный и не " + SA,
    "upādiṇṇaṃ sappaṭighaṃ": "охваченный цеплянием и " + SA,
    "upādiṇṇaṃ appaṭighaṃ": "охваченный цеплянием и не " + SA,
    "bāhiraṃ sappaṭighaṃ": "относящийся к внешнему и " + SA,
    "bāhiraṃ appaṭighaṃ": "относящийся к внешнему и не " + SA,
    "indriyaṃ": "способность", "indriyānaṃ": "способности",
    "mahābhūtaṃ": "великий элемент", "bhūtaṃ": "элемент",
    "mahābhūtānaṃ": "великие элементы", "bhūtānaṃ": "элементы",
    "mahābhūtehi": "великие элементы", "bhūtehi": "элементы",
    "viññatti": "внешнее выражение",
    "cittasamuṭṭhānaṃ": "порождённый умом", "samuṭṭhānaṃ": "порождённый",
    "cittasahabhu": "сосуществующий с умом", "anuparivatti": "следующий за", "citta": "ум",
    "cittajaṃ": "рождённый умом", "hetukaṃ": "имеющий корнем",
    "ajjhattikaṃ": "относящийся к внутреннему", "bāhiraṃ": "относящийся к внешнему",
    "oḷārikaṃ": "грубый", "sukhumaṃ": "тонкий", "bahiddhā": "внешний",
    "kammassa katattā": "вследствие совершённых действий", "kammassa": "действие",
    "ārammaṇaṃ": "объект",
    # item names
    "cakkhu": "глаз", "cakkhuṃ": "глаз", "cakkhumhi": "глаз", "cakkhunā": "глаз",
    "sota": "ухо", "sotaṃ": "ухо", "sotamhi": "ухо", "sotena": "ухо",
    "ghāna": "нос", "ghānaṃ": "нос", "ghānamhi": "нос", "ghānena": "нос",
    "jivhā": "язык", "jivhaṃ": "язык", "jivhāya": "язык",
    "kāyo": "тело", "kāyaṃ": "тело", "kāyamhi": "тело", "kāyena": "тело", "kāyassa": "тело",
    "rūpa": "видимая форма", "rūpamhi": "видимая форма",
    "sadda": "звук", "saddaṃ": "звук", "saddo": "звук", "saddamhi": "звук",
    "gandha": "запах", "gandhaṃ": "запах", "gandho": "запах", "gandhamhi": "запах",
    "rasa": "вкус", "rasaṃ": "вкус", "raso": "вкус", "rasamhi": "вкус",
    "phoṭṭhabba": "осязаемое", "phoṭṭhabbaṃ": "осязаемое", "phoṭṭhabbo": "осязаемое",
    "phoṭṭhabbamhi": "осязаемое",
    "cakkhāyatanaṃ": "сфера глаза", "sotāyatanaṃ": "сфера уха", "ghānāyatanaṃ": "сфера носа",
    "jivhāyatanaṃ": "сфера языка", "kāyāyatanaṃ": "сфера тела", "rūpāyatanaṃ": "сфера видимых форм",
    "saddāyatanaṃ": "сфера звуков", "gandhāyatanaṃ": "сфера запахов", "rasāyatanaṃ": "сфера вкусов",
    "phoṭṭhabbāyatanaṃ": "сфера осязаемого",
    "dhātu": "элемент", "cakkhudhātu": "элемент глаза", "sotadhātu": "элемент уха",
    "ghānadhātu": "элемент носа", "jivhādhātu": "элемент языка", "kāyadhātu": "элемент тела",
    "rūpadhātu": "элемент видимых форм", "saddadhātu": "элемент звуков", "gandhadhātu": "элемент запахов",
    "rasadhātu": "элемент вкусов", "phoṭṭhabbadhātu": "элемент осязаемого",
    "ākāsa": "пространство", "ākāsadhātu": "элемент пространства",
    "pathavī": "земля", "pathavīdhātu": "элемент земли", "āpo": "вода", "āpodhātu": "элемент воды",
    "tejo": "огонь", "tejodhātu": "элемент огня", "vāyo": "ветер", "vāyodhātu": "элемент ветра",
    "itthi": "женственность", "itthindriyaṃ": "способность женственности",
    "purisa": "мужественность", "purisindriyaṃ": "способность мужественности",
    "jīvita": "жизненный", "jīvitindriyaṃ": "жизненная способность",
    "kāyaviññatti": "телесное внешнее выражение", "vacī": "речевой",
    "vacīviññatti": "речевое внешнее выражение",
    "lahutā": "лёгкость", "rūpassa lahutā": "лёгкость материальной формы",
    "mudutā": "мягкость", "rūpassa mudutā": "мягкость материальной формы",
    "kammaññatā": "работоспособность", "rūpassa kammaññatā": "работоспособность материальной формы",
    "rūpassa upacayo": "рост материальной формы",
    "santati": "непрерывность", "rūpassa santati": "непрерывность материальной формы",
    "jaratā": "старение", "rūpassa jaratā": "старение материальной формы",
    "aniccatā": "непостоянство", "rūpassa aniccatā": "непостоянство материальной формы",
    "kabaḷīkāro": "съедаемый", "kabaḷīkāro āhāro": "съедаемая пища", "āhāro": "пища",
    # contact chains
    "cakkhusamphasso": "контакт глаза", "sotasamphasso": "контакт уха", "ghānasamphasso": "контакт носа",
    "jivhāsamphasso": "контакт языка", "kāyasamphasso": "контакт тела",
    "cakkhusamphassassa": "контакт глаза", "sotasamphassassa": "контакт уха",
    "ghānasamphassassa": "контакт носа", "jivhāsamphassassa": "контакт языка",
    "kāyasamphassassa": "контакт тела",
    "cakkhusamphassajā": "рождённый контактом глаза", "sotasamphassajā": "рождённый контактом уха",
    "ghānasamphassajā": "рождённый контактом носа", "jivhāsamphassajā": "рождённый контактом языка",
    "kāyasamphassajā": "рождённый контактом тела",
    "cakkhusamphassajāya": "рождённый контактом глаза", "kāyasamphassajāya": "рождённый контактом тела",
    "cakkhusamphassajā vedanā": "чувство рождённое контактом глаза",
    "sotasamphassajā vedanā": "чувство рождённое контактом уха",
    "ghānasamphassajā vedanā": "чувство рождённое контактом носа",
    "jivhāsamphassajā vedanā": "чувство рождённое контактом языка",
    "kāyasamphassajā vedanā": "чувство рождённое контактом тела",
    "cakkhusamphassajāya vedanāya": "чувство рождённое контактом глаза",
    "kāyasamphassajāya vedanāya": "чувство рождённое контактом тела",
    "vedanā": "чувство", "vedanāya": "чувство", "saññā": "восприятие", "saññāya": "восприятие",
    "cetanā": "намерение", "cetanāya": "намерение",
    "cakkhuviññāṇaṃ": "зрительное сознание", "sotaviññāṇaṃ": "слуховое сознание",
    "ghānaviññāṇaṃ": "обонятельное сознание", "jivhāviññāṇaṃ": "вкусовое сознание",
    "kāyaviññāṇaṃ": "осязательное сознание",
    "cakkhuviññāṇassa": "зрительное сознание", "kāyaviññāṇassa": "осязательное сознание",
    "nissāya": "в зависимости от",
    "cakkhuṃ nissāya": "глаз в зависимости от которого", "sotaṃ nissāya": "ухо в зависимости от которого",
    "ghānaṃ nissāya": "нос в зависимости от которого", "jivhaṃ nissāya": "язык в зависимости от которого",
    "kāyaṃ nissāya": "тело в зависимости от которого",
    "uppajji": "возникать", "uppajjati": "возникать", "uppajjissati": "возникнуть",
    "paṭihaññi": "ударяться", "paṭihaññati": "ударяться", "paṭihaññissati": "удариться",
    "sappaṭighaṃ paṭihaññi": "ударяться … " + SA, "sappaṭigho paṭihaññi": "ударяться … " + SA,
    "suṇi": "слышать", "suṇāti": "слышать", "suṇissati": "услышать",
    "ghāyi": "обонять", "ghāyati": "обонять", "ghāyissati": "обонять",
    "sāyi": "вкушать", "sāyati": "вкушать", "sāyissati": "вкусить",
    "phusi": "касаться", "phusati": "касаться", "phusissati": "коснуться",
    # sense-organ definition and its names
    "pasādo": "чувствительность", "upādāya pasādo": "чувствительность производная",
    "attabhāva": "индивидуальное бытие",
    "dvārā": "врата", "samuddo": "океан", "paṇḍaraṃ": "чистота", "khettaṃ": "поле",
    "nettaṃ": "проводник", "nayanaṃ": "вожатый", "tīraṃ": "берег",
    "suñño": "пустой", "gāmo": "деревня", "suñño gāmo": "пустая деревня",
    # visible form
    "vaṇṇa": "цвет", "nibhā": "облик", "vaṇṇanibhā": "цвет и облик",
    "upādāya vaṇṇanibhā": "производный … цвет и облик",
    "nīlaṃ": "синий", "pītakaṃ": "жёлтый", "lohitakaṃ": "красный", "odātaṃ": "белый",
    "kāḷakaṃ": "чёрный", "mañjiṭṭhakaṃ": "малиновый", "hari": "зелёный", "harivaṇṇaṃ": "зеленоватый",
    "ambaṅkuravaṇṇaṃ": "цвета побегов манго", "amba": "манго", "aṅkura": "побег",
    "vaṭṭaṃ": "округлый", "parimaṇḍalaṃ": "круглый", "caturaṃsaṃ": "четырёхугольный",
    "chaḷaṃsaṃ": "шестиугольный", "aṭṭhaṃsaṃ": "восьмиугольный", "soḷasaṃsaṃ": "шестнадцатиугольный",
    "chāyā": "тень", "ātapo": "солнечный свет", "āloko": "свет", "andhakāro": "тьма",
    "abbhā": "облака", "mahikā": "туман", "dhūmo": "дым", "rajo": "пыль",
    "canda": "лунный", "sūriya": "солнечный", "maṇḍalassa": "диск", "tārakarūpānaṃ": "звёзды",
    "ādāsa": "зеркальный", "maṇi": "драгоценные камни", "saṅkha": "раковина", "muttā": "жемчуг",
    "veḷuriyassa": "берилл", "rajatassa": "серебро",
    "maṇisaṅkhamuttāveḷuriyassa vaṇṇanibhā": "цвет и облик драгоценных камней раковин жемчуга и берилла",
    "jātarūparajatassa vaṇṇanibhā": "цвет и облик золота и серебра",
    # sound
    "bheri": "большие барабаны", "bherisaddo": "звук больших барабанов",
    "mudiṅga": "малые барабаны", "mudiṅgasaddo": "звук малых барабанов",
    "saṅkhasaddo": "звук раковин", "paṇava": "бубны", "paṇavasaddo": "звук бубнов",
    "gīta": "пение", "gītasaddo": "звук пения",
    "vādita": "музыкальные инструменты", "vāditasaddo": "звук музыкальных инструментов",
    "samma": "тарелки", "sammasaddo": "звук тарелок",
    "pāṇi": "хлопок в ладоши", "pāṇisaddo": "звук хлопков в ладоши",
    "nigghosasaddo": "звук голосов",
    "dhātūnaṃ": "предметы", "sannighāta": "соударение",
    "dhātūnaṃ sannighātasaddo": "звук соударения предметов",
    "vāta": "ветер", "vātasaddo": "звук ветра", "udaka": "вода", "udakasaddo": "звук воды",
    "manussa": "люди", "manussasaddo": "звук людей",
    "amanussa": "нечеловеческие существа", "amanussasaddo": "звук нечеловеческих существ",
    # smell and taste
    "mūla": "корни", "sāra": "сердцевина дерева", "taca": "кора", "patta": "листья",
    "puppha": "цветы", "phala": "плоды", "āmaka": "сырое мясо", "vissa": "гниль",
    "khandha": "стебли",
    "mūlagandho": "запах корней", "sāragandho": "запах сердцевины дерева", "tacagandho": "запах коры",
    "pattagandho": "запах листьев", "pupphagandho": "запах цветов", "phalagandho": "запах плодов",
    "āmakagandho": "запах сырого мяса", "vissagandho": "запах гнили",
    "sugandho": "приятный запах", "duggandho": "неприятный запах",
    "mūlaraso": "вкус корней", "khandharaso": "вкус стеблей", "tacaraso": "вкус коры",
    "pattaraso": "вкус листьев", "puppharaso": "вкус цветов", "phalaraso": "вкус плодов",
    "ambilaṃ": "кислый", "madhuraṃ": "сладкий", "tittakaṃ": "горький", "kaṭukaṃ": "острый",
    "loṇikaṃ": "солёный", "khārikaṃ": "щелочной", "lambilaṃ": "кисловатый", "kasāvo": "вяжущий",
    "sādu": "вкусный",
    # tangible
    "kakkhaḷaṃ": "твёрдый", "kakkhaḷattaṃ": "твёрдость", "khara": "жёсткий",
    "mudukaṃ": "мягкий", "saṇhaṃ": "гладкий", "pharusaṃ": "шероховатый",
    "garukaṃ": "тяжёлый", "lahukaṃ": "лёгкий", "sukha": "приятный", "dukkha": "болезненный",
    "samphassaṃ": "контакт", "samphasso": "контакт",
    "manāpiyo": "желанный", "amanāpiyo": "нежеланный",
    "usmā": "тепло", "usumaṃ": "жар", "thambhitattaṃ": "состояние напряжённости",
    "sineho": "влага", "bandhanattaṃ": "связующее свойство",
    "bandhanattaṃ rūpassa": "связующее свойство материальной формы", "gataṃ": "считаться",
    # femininity / masculinity / life
    "itthiyā": "женщина", "purisassa": "мужчина", "liṅgaṃ": "внешность", "nimittaṃ": "признак",
    "kuttaṃ": "поведение", "ākappo": "манера",
    "rūpīnaṃ dhammānaṃ": "материальные явления", "āyu": "срок жизни", "ṭhiti": "сохранение",
    "yapanā": "поддержание", "yāpanā": "продление", "iriyanā": "движение", "vattanā": "течение",
    "pālanā": "сбережение",
    # intimation
    "kusala": "благой", "kusalacittassa": "благой ум", "akusala": "неблагой",
    "akusalacittassa": "неблагой ум", "abyākata": "этически неопределённый", "cittassa": "ум",
    "abhikkamantassa": "идти вперёд", "paṭikkamantassa": "идти назад",
    "ālokentassa": "смотреть прямо", "vilokentassa": "смотреть по сторонам",
    "samiñjentassa": "сгибать", "pasārentassa": "разгибать",
    "thambhanā": "напряжённость", "santhambhitattaṃ": "состояние полной напряжённости",
    "viññāpanā": "оповещение",
    "vācā": "речь", "girā": "слово", "byappatho": "способ речи", "udīraṇaṃ": "произнесение",
    "ghoso": "голос", "dhoso": "голос", "ghosakammaṃ": "звучание голоса",
    # space, lightness ..., ageing, impermanence
    "aghaṃ": "незаполненный", "vivaro": "просвет", "asamphuṭṭhaṃ": "не затронутый",
    "lahupariṇāmatā": "быстрота перемен", "adandhanatā": "отсутствие медлительности",
    "avitthanatā": "отсутствие скованности", "dandhanatā": "медлительность", "vitthanatā": "скованность",
    "maddavatā": "гибкость", "akakkhaḷatā": "отсутствие грубости", "akathinatā": "отсутствие жёсткости",
    "kakkhaḷatā": "грубость", "kathinatā": "жёсткость",
    "kammaññattaṃ": "состояние работоспособности", "bhāvo": "свойство",
    "ācayo": "накопление", "āyatanānaṃ": "сферы восприятия",
    "jīraṇatā": "одряхление", "khaṇḍiccaṃ": "сломанные зубы", "pāliccaṃ": "седые волосы",
    "valittacatā": "морщинистая кожа", "āyuno": "срок жизни", "saṃhāni": "сокращение",
    "paripāko": "изношенность",
    "khayo": "уничтожение", "vayo": "угасание", "paribhedo": "полный распад",
    "antaradhānaṃ": "исчезновение",
    # edible food
    "odano": "варёный рис", "kummāso": "каша", "sattu": "толокно", "maccho": "рыба", "maṃsaṃ": "мясо",
    "khīraṃ": "молоко", "dadhi": "простокваша", "sappi": "топлёное масло", "navanītaṃ": "сливочное масло",
    "madhu": "мёд", "phāṇitaṃ": "патока", "mukha": "рот", "āsiyaṃ": "есть", "danta": "зуб",
    "vikhādanaṃ": "разжёвывать", "gala": "горло", "ajjhoharaṇīyaṃ": "проглатывать", "kucchi": "живот",
    "vitthambhanaṃ": "наполнять", "ojāya": "питательная сущность",
    "yāpenti": "поддерживать свою жизнь",
    # four, six, eight (1-966, 1-972 ... 1-974)
    "sutaṃ": "услышанное", "mutaṃ": "ощущённое", "viññātaṃ": "познанный",
    "viññātaṃ rūpaṃ": f"{RF} познанная", "manasā": "ум", "mano": "ум",
    "viññeyyaṃ": "познаваемый", "viññeyyaṃ rūpaṃ": f"{RF} познаваемая",
    "manodhātu": "элемент ума", "manoviññāṇa": "умственное сознание",
    "manoviññāṇadhātu": "элемент умственного сознания",
    "āyatanaṃ cakkhuviññeyyaṃ rūpaṃ": f"сфера{GAP}есть {RF} познаваемая глазом",
    "āyatanaṃ manodhātuviññeyyaṃ rūpaṃ": f"сфера{GAP}есть {RF} познаваемая элементом ума",
    "rūpaṃ manoviññeyyaṃ rūpaṃ": f"{RF} есть {RF} познаваемая умом",
    "rūpaṃ manoviññāṇadhātuviññeyyaṃ rūpaṃ":
        f"{RF} есть {RF} познаваемая элементом умственного сознания",
    "dhamma": "объекты ума", "dhammāyatana": "сфера объектов ума",
    # headings and closing lines
    "niddeso": "разъяснение", "duka": "классификация по два", "saṅgaho": "классификация",
    "rūpasaṅgaho": "классификация материальной формы", "vidhena": "по",
    "bhājanīyaṃ": "разбор", "kaṇḍe": "раздел", "kaṇḍaṃ": "раздел", "bhāṇa": "чтение вслух",
    "vāro": "раздел", "aṭṭhama": "восьмой", "vibhatti": "классификация", "niṭṭhitaṃ": "завершённый",
    "dasa": "десять", "dasakaṃ": "классификация по десять",
    "ekādasa": "одиннадцать", "ekādasakaṃ": "классификация по одиннадцать",
}

KAYA_ORGAN = {"kāyāyatanaṃ", "kāyadhātu", "kāyaviññāṇaṃ", "kāyaviññāṇassa", "kāyasamphasso",
              "kāyasamphassassa", "kāyasamphassajā", "kāyasamphassajāya", "kāyaṃ", "kāyo",
              "kāyamhi", "kāyena", "kāyaṃ nissāya", "indriyaṃ", "viññeyyaṃ"}

OVERRIDES = {}
RU = {**read_russian(PARTS[0]), **read_russian(PARTS[1])}


def resolve(bid, kw, kws):
    ov = OVERRIDES.get(bid, {})
    if kw in ov:
        return ov[kw]
    s = set(lc(x) for x in kws)
    k = lc(kw)
    if k == "upādiṇṇupādāniyaṃ" and "цеплянием и служит" not in RU[bid]:
        # three predicates: «охвачена цеплянием, служит его объектом и является видимой»
        return "охваченный цеплянием" + GAP + "служащий его объектом"
    if kw in ("Yaṃ", "Yo", "Yā"):                 # «То, что …» opening a definition
        return "то что"
    if kw in ("yaṃ", "yo"):                       # yaṃ/yo vā panaññampi atthi … = «или же любая другая …»
        return "любой"
    if k == "kāya":                               # stem: «тело» (organ) / «телесный» (kāyaviññatti only)
        return "тело" if s & KAYA_ORGAN else ("телесный" if "kāyaviññatti" in s else "тело")
    if k == "ārammaṇo":                           # organ side «имеющий объектом …»; object side «с … как с объектом»
        return "имеющий объектом" if any(x.endswith(" nissāya") for x in s) else "объект"
    if k == "jīvita" and "āyu" in s:              # jīvitindriya string: «… жизнь, жизненная способность»
        return "жизнь"
    if k == "sattānaṃ":
        return "живые существа" if "nigghosasaddo" in s else "существа"
    if k == "bhedo":                              # vacībhedo «членораздельная речь» / bhedo «распад»
        return "членораздельный" if "vācā" in s else "распад"
    if k.startswith("rūpassa na "):               # «не является X материальной формы»
        return "не" + GAP + RUPA["rūpassa " + k[len("rūpassa na "):]]
    return RUPA[k]


if __name__ == "__main__":
    for p in PARTS:
        build_part(p, resolve)
        verify(p)
