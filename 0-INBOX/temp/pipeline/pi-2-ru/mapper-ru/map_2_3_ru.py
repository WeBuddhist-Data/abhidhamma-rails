"""Build the Pāli->Russian keyword maps for pi-2 (Vibhaṅga) chapters 2-ayatanavibhango and 3-dhatuvibhango.

usage: python -I -X utf8 map_2_3_ru.py          (writes the two <part>.mapped.md and verifies them)

Resolution order per keyword: OVERRIDES[bid][kw]  ->  hetuko / CHOICES context rules  ->  T (this file:
KH + the chapter 2/3 additions)  ->  pi-1 CH2 / MATRIX (via map_common_pi2_ru.value).
Conventions: ru-map-conventions-pi2.md (+ the pi-1 file); new decisions: notes-map-2-3.md.
"""
import pathlib
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import map_common_pi2_ru as M  # noqa: E402
from map_common_pi2_ru import (EXCEPTIONS, GAP, KH, NDE, build_part, hetuko_value, lc,  # noqa: E402,F401
                               present, read_keywords, read_pali, read_russian, value, verify)

PARTS = ["2-ayatanavibhango", "3-dhatuvibhango"]

# ---------------------------------------------------------------------------- table
T = dict(KH)
# user decision 2026-11-16: N-vidhena WITHOUT «классификация» (KH still carries the old frame strings;
# catubbidhena / chabbidhena included)
for _k, _v in M._ORD.items():
    T[{"cha": "chabbidhena", "catub": "catubbidhena"}.get(_k, f"{_k}vidhena")] = _v
for _kk, _g in M.AGG_GEN.items():
    _key = {"rūpa": "rūpakkhandho", "vedanā": "vedanākkhandho", "saññā": "saññākkhandho",
            "saṅkhāra": "saṅkhārakkhandho", "viññāṇa": "viññāṇakkhandho"}[_kk]
    T[f"dasavidhena {_key}"] = f"совокупность {_g} на десять видов"
    T[f"bahuvidhena {_key}"] = f"совокупность {_g} на многие виды"
assert not any(v.startswith("классификация") for v in T.values())

T.update({
    # headings / frame
    "āyatana": "сфера восприятия", "dhātu": "элемент", "dasa": "десять",
    "āyatanaṃ": "сфера", "āyatanā": "сферы восприятия", "āyatanāni": "сферы восприятия",
    "āyatanānaṃ": "сферы восприятия",
    "dvādasāyatanāni": "двенадцать сфер восприятия", "dvādasannaṃ": "двенадцать",
    "dvādasannaṃ āyatanānaṃ": "двенадцать сфер восприятия",
    "dasāyatanā": "десять сфер восприятия", "ekādasāyatanā": "одиннадцать сфер восприятия",
    "āyatanā siyā": "сферы восприятия" + GAP + "иногда",
    "āyatanā anidassana": "сферы восприятия" + GAP + "невидимые",
    "āyatanā anidassanā": "сферы восприятия" + GAP + "невидимые",
    "āyatanā sappaṭighā": "сферы восприятия" + GAP + "способные к соударению",
    "dasāyatanā sappaṭighā": "десять сфер восприятия способные к соударению",
    "dhātuyo": "элементы", "dhātuyā": "элемент", "dhātuyo siyā": "элементы" + GAP + "иногда",
    "dhātuyo hetuvippayuttā": "элементы не связанные с корнями",
    "dhātuyo pariyāpannā": "элементы принадлежащие к кругам существования",
    "dhātuyo sappaṭighā": "элементы способные к соударению",
    "aṭṭhārasa": "восемнадцать", "aṭṭhārasa dhātuyo": "восемнадцать элементов",
    "sattarasa": "семнадцать", "sattarasa dhātuyo": "семнадцать элементов",
    "soḷasa": "шестнадцать", "soḷasa dhātuyo": "шестнадцать элементов",
    "pannarasa": "пятнадцать", "pannarasa dhātuyo": "пятнадцать элементов",
    "dvādasa": "двенадцать", "dvādasa dhātuyo": "двенадцать элементов",
    "ekādasa": "одиннадцать", "ekādasa dhātuyo": "одиннадцать элементов",
    "dasa dhātuyo": "десять элементов", "dasasu": "десять",
    # the twelve bases (2-154)
    "cakkhuṃ": "глаз", "cakkhu": "глаз", "cakkhunā": "глаз", "sotaṃ": "ухо", "sota": "ухо", "sotena": "ухо",
    "ghānaṃ": "нос", "ghāna": "нос", "ghānena": "нос", "jivhā": "язык", "jivhāya": "язык",
    "kāyo": "тело", "kāya": "тело", "kāyena": "тело", "mano": "ум",
    "dhammā": "явления", "dhamma": "объекты ума", "dhamme": "объекты ума", "dhammesu": "явления",
    "aniccaṃ": "непостоянный", "dukkhaṃ": "страдание", "anattā": "лишённый самости",
    "vipariṇāmadhammaṃ": "подверженный изменению",
    "manāyatanaṃ": "сфера ума", "dhammāyatanaṃ": "сфера объектов ума",
    # sense organs (2-156 … 2-160 = pi-1 ^1-596 …)
    "attabhāva": "индивидуальное бытие", "paṇḍara": "чистота", "paṇḍaraṃ": "чистота", "dvārā": "врата",
    "bhūtānaṃ": "элементы", "mahābhūtānaṃ": "великие элементы", "bhūtehi": "элементы",
    "mahābhūtehi": "великие элементы", "suñño": "пустой", "gāmo": "деревня",
    "gāmopeso": "это" + GAP + "деревня",
    "khetta": "поле", "netta": "проводник", "tīra": "берег", "samuddo": "океан",
    "pasādo": "чувствительность", "upādāya pasādo": "чувствительность производная",
    "anidassano": "невидимый", "anidassanena": "невидимый",
    "anidassano sappaṭigho": "невидимый и способный к соударению",
    "anidassanaṃ sappaṭighaṃ": "невидимый и способный к соударению",
    "anidassanena sappaṭighena": "невидимый и способный к соударению",
    "anidassanāya sappaṭighāya": "невидимый и способный к соударению",
    "sappaṭighena": "способный к соударению", "sappaṭighāya": "способный к соударению",
    "sappaṭigha": "способный к соударению", "sappaṭighā": "способный к соударению",
    "sanidassanaṃ sappaṭighaṃ": "видимый и способный к соударению",
    "cakkhudhātu": "элемент глаза", "sotadhātu": "элемент уха", "ghānadhātu": "элемент носа",
    "jivhādhātu": "элемент языка", "kāyadhātu": "элемент тела",
    "cakkhundriya": "способность глаза", "sotindriya": "способность уха", "ghānindriya": "способность носа",
    "jīvhindriya": "способность языка", "kāyindriya": "способность тела",
    "suṇissati": "услышать", "suṇi": "слышать", "suṇāti": "слышать",
    "ghāyi": "обонять", "ghāyati": "обонять", "sāyi": "вкушать", "sāyati": "вкушать",
    "phusissati": "коснуться", "phusi": "касаться", "phusati": "касаться",
    "saddaṃ": "звук", "gandhaṃ": "запах", "rasaṃ": "вкус", "phoṭṭhabbaṃ": "осязаемое",
    "phoṭṭhabba": "осязаемое",
    # mind base (2-161)
    "phassasampayuttaṃ": "связанный с контактом",
    # visible form (2-162 = pi-1 ^1-616)
    "kāḷakaṃ": "чёрный", "nīlaṃ": "синий", "pītakaṃ": "жёлтый", "lohitakaṃ": "красный", "odātaṃ": "белый",
    "veḷuriyassa": "берилл", "parimaṇḍalaṃ": "круглый", "abbhā": "облака", "vaṇṇa": "цвет",
    "saṅkha": "раковина", "mañjiṭṭhakaṃ": "малиновый", "andhakāro": "тьма", "maṇḍalassa": "диск",
    "rajo": "пыль", "aṭṭhaṃsaṃ": "восьмиугольный", "rūpadhātu": "элемент видимых форм",
    "maṇi": "драгоценные камни", "harivaṇṇaṃ": "зеленоватый", "hari": "зелёный", "āloko": "свет",
    "amba": "манго", "ādāsa": "зеркальный", "mahikā": "туман", "canda": "лунный", "mutta": "жемчуг",
    "vaṭṭaṃ": "округлый", "chāyā": "тень", "nibhā": "облик", "vaṇṇanibhā": "цвет и облик",
    "aṅkura": "побег", "rajatassa": "серебро", "chaḷaṃsaṃ": "шестиугольный",
    "soḷasaṃsaṃ": "шестнадцатиугольный", "dhūmo": "дым", "caturassaṃ": "четырёхугольный",
    "tārakarūpānaṃ": "звёзды", "sūriya": "солнечный", "ātapo": "солнечный свет",
    "yaṃ vā pana": "или же какой бы", "yo vā pana": "или же какой бы",
    # sound (2-163 = pi-1 ^1-620)
    "sattānaṃ": "существа", "sannighāta": "соударение", "nigghosa": "голоса", "samma": "тарелки",
    "bheri": "большие барабаны", "saddadhātu": "элемент звуков", "dhātūnaṃ": "предметы",
    "pāṇi": "хлопок в ладоши", "manussa": "люди", "vādita": "музыкальные инструменты",
    "amanussa": "нечеловеческие существа", "gīta": "пение", "saddo": "звук", "sadda": "звук",
    "paṇava": "бубны", "udaka": "вода", "vāta": "ветер",
    # smell / taste (2-164, 2-165 = pi-1 ^1-624, ^1-628)
    "taca": "кора", "gandhadhātu": "элемент запахов", "puppha": "цветы", "phala": "плоды",
    "sāra": "сердцевина дерева", "patta": "листья", "sugandho": "приятный запах", "vissa": "гниль",
    "āma": "сырое мясо", "mūla": "корни", "gandho": "запах", "duggandho": "неприятный запах",
    "lambikaṃ": "кисловатый", "khārikaṃ": "щелочной", "kasāvo": "вяжущий", "tittakaṃ": "горький",
    "rasadhātu": "элемент вкусов", "kaṭukaṃ": "острый", "loṇikaṃ": "солёный", "ambilaṃ": "кислый",
    "khandha": "стебли", "madhuraṃ": "сладкий", "raso": "вкус", "sādu": "вкусный", "asādu": "невкусный",
    # tangible (2-166 = pi-1 ^1-647)
    "phoṭṭhabbadhātu": "элемент осязаемого", "kakkhaḷaṃ": "твёрдый", "garukaṃ": "тяжёлый",
    "lahukaṃ": "лёгкий", "pharusaṃ": "шероховатый", "saṇhaṃ": "гладкий", "mudukaṃ": "мягкий",
    # dhammāyatana (2-167, 2-184 = pi-1 ^1-1094)
    "moha": "заблуждение", "rāga": "страсть", "dosa": "злоба", "itthi": "женственность",
    "anidassana": "невидимый", "anidassanaappaṭighaṃ": "невидимый и не способный к соударению",
    "anidassanaappaṭighā": "невидимый и не способный к соударению",
    "appaṭighaṃ": "не способный к соударению", "asaṅkhatā": "необусловленный",
    "asaṅkhatā dhātu": "необусловленный элемент", "asaṅkhataṃ": "необусловленный",
    # pañhāpucchaka (2-169 … 2-171, 2-186 … 2-188)
    "vattabbaṃ": "определить", "ārammaṇā": "объект",
    "anidassanasappaṭighā": "невидимый но способный к соударению",
    "nevavipākanavipākadhammadhammā": "не являющийся результатом действий и не способный приносить результаты",
    "vicāra": "удержание мысли", "vicārā": "удержание мысли", "vitakkā": "направленная мысль",
    "sahabhū": "сосуществующий", "acetasikā": "не сопутствующий уму", "sahetukā": "имеющий корни",
    "arūpaṃ": "нематериальный", "cittasampayuttaṃ": "связанный с умом", "saṃsaṭṭhaṃ": "соединённый",
    "cittasaṃsaṭṭhaṃ": "соединённый с умом", "anārammaṇā": "не имеющий объекта",
    "cittā": "ум", "āvacarā": "относящийся к миру",
    "hetu ceva hetusampayuttañca": "являющийся корнем и связанный с корнями",
    "hetu ceva hetusampayuttā": "являющийся корнем и связанный с корнями",
    "āsavo ceva āsavasampayuttañca": "являющийся влечением и связанный с влечениями",
    "āsavo ceva āsavasampayuttā": "являющийся влечением и связанный с влечениями",
    "saṃyojanañceva saṃyojanasampayuttañca": "являющийся оковами и связанный с оковами",
    "saṃyojanañceva saṃyojanasampayuttā": "являющийся оковами и связанный с оковами",
    "gantho ceva ganthasampayuttañca": "являющийся узами и связанный с узами",
    "gantho ceva ganthasampayuttā": "являющийся узами и связанный с узами",
    "nīvaraṇañceva nīvaraṇasampayuttañca": "являющийся помехой и связанный с помехами",
    "nīvaraṇañceva nīvaraṇasampayuttā": "являющийся помехой и связанный с помехами",
    "kileso ceva kilesasampayuttañca": "являющийся омрачением и связанный с омрачениями",
    "kileso ceva kilesasampayuttā": "являющийся омрачением и связанный с омрачениями",
    # six elements (2-172 … 2-177)
    "ākāsa": "пространство", "ākāsadhātu": "элемент пространства", "ākāso": "пространство",
    "dhātudvayaṃ": "элементов" + GAP + "два", "dvayaṃ": "два", "aññampi": "другой",
    "seyyathidaṃ": "а именно",
    "ajjhattaṃ": "внутренний", "kharigataṃ": "считаться жёстким", "kakkhaḷattaṃ": "твёрдость",
    "kesā": "волосы на голове", "lomā": "волосы на теле", "nakhā": "ногти", "dantā": "зубы", "taco": "кожа",
    "maṃsaṃ": "плоть", "nhāru": "сухожилия", "aṭṭhi": "кости", "miñjaṃ": "костный мозг", "vakkaṃ": "почки",
    "hadayaṃ": "сердце", "yakanaṃ": "печень", "kilomakaṃ": "плевра", "pihakaṃ": "селезёнка",
    "papphāsaṃ": "лёгкие", "antaṃ": "кишечник", "antaguṇaṃ": "брыжейка", "udariyaṃ": "содержимое желудка",
    "karīsaṃ": "кал",
    "ayo": "железо", "lohaṃ": "медь", "tipu": "олово", "sajjhaṃ": "серебро", "muttā": "жемчуг",
    "veḷuriyo": "берилл", "saṅkho": "раковина", "silā": "кристалл", "pavāḷaṃ": "коралл",
    "rajataṃ": "монеты", "lohitaṅko": "рубин", "masāragallaṃ": "кошачий глаз", "tiṇaṃ": "трава",
    "kaṭṭhaṃ": "дерево", "sakkharā": "гравий", "kaṭhalaṃ": "черепки", "bhūmi": "земля",
    "pāsāṇo": "камень", "pabbato": "гора",
    "āpo": "вода", "āpodhātu": "элемент воды", "āpogataṃ": "считаться водой", "sineho": "влага",
    "sinehagataṃ": "считаться влагой", "bandhanattaṃ": "связующее свойство", "rūpassa": "материальная форма",
    "pittaṃ": "желчь", "semhaṃ": "слизь", "pubbo": "гной", "lohitaṃ": "кровь", "sedo": "пот", "medo": "жир",
    "assu": "слёзы", "vasā": "жидкий жир", "kheḷo": "слюна", "siṅghāṇikā": "сопли",
    "lasikā": "суставная жидкость", "muttaṃ": "моча",
    "khīraṃ": "молоко", "dadhi": "простокваша", "sappi": "топлёное масло", "navanītaṃ": "сливочное масло",
    "madhu": "мёд", "phāṇitaṃ": "патока", "bhummāni": "в земле", "udakāni": "воды",
    "antalikkhāni": "в небе",
    "tejogataṃ": "считаться огнём", "usmā": "тепло", "usmāgataṃ": "считаться теплом", "usumaṃ": "жар",
    "usumagataṃ": "считаться жаром", "santappati": "согреваться", "jīrīyati": "стареть",
    "pariḍayhati": "сгорать в жару", "asita": "съеденное", "pīta": "выпитое", "khāyita": "разжёванное",
    "sāyitaṃ": "отведанное", "pariṇāmaṃ gacchati": "перевариваться",
    "kaṭṭhaggi": "огонь от дров", "palālaggi": "огонь от соломы", "tiṇaggi": "огонь от травы",
    "gomayaggi": "огонь от навоза", "thusaggi": "огонь от мякины", "saṅkāraggi": "огонь от мусора",
    "indaggi": "огонь молнии", "sannicaya": "куча",
    "vāyogataṃ": "считаться ветром", "thambhitattaṃ": "состояние напряжённости",
    "uddhaṅgamā": "идущий вверх", "adhogamā": "идущий вниз", "gamā": "идущий", "vātā": "ветры",
    "kucchisayā": "в животе", "koṭṭhāsayā": "в кишечнике",
    "aṅgamaṅgānusārino": "проходящий по всем членам тела", "ānusārino": "проходящий",
    "satthaka": "режущий как нож", "khuraka": "режущий как бритва", "uppalaka": "колющий",
    "assāso": "вдох", "puratthimā": "восточный", "sarajā": "пыльный", "arajā": "без пыли",
    "sītā": "холодный", "uṇhā": "горячий", "kāḷa": "грозовой", "verambha": "поднебесье",
    "pakkha": "крылья", "supaṇṇa": "гаруда", "tālavaṇṭa": "опахало из пальмовых листьев",
    "vidhūpana": "веер",
    "ākāsagataṃ": "считаться пространством", "aghaṃ": "незаполненный",
    "aghagataṃ": "считаться незаполненным", "vivaro": "просвет", "vivaragataṃ": "считаться просветом",
    "asamphuṭṭhaṃ": "не затронутый", "maṃsa": "плоть", "lohitehi": "кровь", "kaṇṇa": "ушной",
    "nāsa": "носовой", "mukha": "ротовой", "dvāraṃ": "отверстие", "ajjhoharati": "проглатывать",
    "santiṭṭhati": "пребывать", "nikkhamati": "выходить",
    # viññāṇadhātu, sukha … avijjā (2-178 … 2-180)
    "cakkhuviññāṇa": "зрительное сознание", "sotaviññāṇa": "слуховое сознание",
    "ghānaviññāṇa": "обонятельное сознание", "jivhāviññāṇa": "вкусовое сознание",
    "kāyaviññāṇa": "осязательное сознание",
    "cakkhuviññāṇadhātu": "элемент зрительного сознания", "sotaviññāṇadhātu": "элемент слухового сознания",
    "ghānaviññāṇadhātu": "элемент обонятельного сознания", "jivhāviññāṇadhātu": "элемент вкусового сознания",
    "kāyaviññāṇadhātu": "элемент осязательного сознания",
    "sukhadhātu": "элемент удовольствия", "dukkhadhātu": "элемент боли", "somanassa": "радость",
    "somanassadhātu": "элемент радости", "domanassa": "уныние", "domanassadhātu": "элемент уныния",
    "upekkhādhātu": "элемент невозмутимости", "avijjā": "неведение", "avijjādhātu": "элемент неведения",
    "kāyikaṃ": "телесный", "sātaṃ": "отрадный", "asātaṃ": "безотрадный", "vedayitaṃ": "переживание",
    "kāyasamphassajaṃ": "рождённый контактом тела", "cetosamphassajaṃ": "рождённый контактом ума",
    "cetosamphassa": "контакт ума",
    "cetasikaṃ sātaṃ": "душевная отрада", "cetasikaṃ asātaṃ": "душевная безотрадность",
    "cetasikaṃ dukkhaṃ": "душевная боль", "dukkhaṃ vedayitaṃ": "болезненное переживание",
    "adukkhamasukhaṃ": "ни болезненный ни приятный",
    "aññāṇaṃ": "незнание", "adassanaṃ": "отсутствие видения", "anabhisamayo": "отсутствие постижения",
    "ananubodho": "отсутствие понимания", "asambodho": "непробуждённость",
    "appaṭivedho": "отсутствие проникновения", "asaṅgāhaṇā": "неохватывание",
    "apariyogāhaṇā": "отсутствие углубления", "asamapekkhanā": "отсутствие рассмотрения",
    "apaccavekkhaṇā": "отсутствие обдумывания", "apaccakkhakammaṃ": "неспособность видеть воочию",
    "dummejjhaṃ": "тупость", "bālyaṃ": "глупость", "asampajaññaṃ": "отсутствие ясного понимания",
    "moho": "заблуждение", "pamoho": "сильное заблуждение", "sammoho": "полное заблуждение",
    "ogho": "поток", "yogo": "ярмо", "ānusayo": "скрытая склонность", "pariyuṭṭhānaṃ": "одержимость",
    "laṅgī": "засов", "mūlaṃ": "корень", "akusala": "неблагой",
    # kāma … avihiṃsā (2-181, 2-182)
    "kāma": "чувственные желания", "kāmadhātu": "элемент чувственных желаний",
    "byāpāda": "недоброжелательность", "byāpādadhātu": "элемент недоброжелательности",
    "vihiṃsā": "жестокость", "vihiṃsādhātu": "элемент жестокости", "nekkhamma": "отречение",
    "nekkhammadhātu": "элемент отречения", "abyāpāda": "отсутствие недоброжелательности",
    "abyāpādadhātu": "элемент отсутствия недоброжелательности", "avihiṃsā": "отсутствие жестокости",
    "avihiṃsādhātu": "элемент отсутствия жестокости",
    "kāmapaṭisaṃyutto": "связанный с чувственными желаниями", "paṭisaṃyutto": "связанный",
    "takko": "мышление", "vitakko": "направленная мысль", "saṅkappo": "помысел",
    "appanā": "прикрепление мысли", "byappanā": "усиленное прикрепление мысли",
    "abhiniropanā": "направление" + GAP + "на объект", "micchā": "ложный", "micchāsaṅkappo": "ложный помысел",
    "sammā": "правильный",
    "nirayaṃ": "ад", "pariyantaṃ": "граница", "karitvā": "взять", "uparito": "сверху",
    "nimmita": "творения", "vasavattī": "властвующий", "deve": "боги", "vasavattī deve": "боги властвующие",
    "yaṃ": "всё что", "saṅkhārā": "формирующие факторы",
    "vatthūsu": "поводы", "cittassa": "ум", "āghāto": "досада", "paṭighāto": "раздражение",
    "paṭighaṃ": "неприязнь", "paṭivirodho": "противодействие", "kopo": "негодование",
    "pakopo": "сильное негодование", "sampakopo": "крайнее негодование", "doso": "злоба",
    "sampadoso": "крайняя злоба", "manopadoso": "сильная злоба ума", "byāpatti": "недоброжелательность",
    "kujjhanā": "гневливость", "dussanā": "проявление злобы", "byāpajjanā": "проявление недоброжелательности",
    "caṇḍikkaṃ": "свирепость", "asuropo": "грубость", "anattamanatā": "недовольство",
    "ekacco": "некто", "pāṇinā": "рука", "leḍḍunā": "ком земли", "daṇḍena": "палка", "satthena": "оружие",
    "rajjuyā": "верёвка", "aññataraññatarena": "чем-либо ещё", "sattesu": "существа",
    "viheṭheti": "мучить", "heṭhanā": "мучение", "viheṭhanā": "сильное мучение", "hiṃsanā": "насилие",
    "vihiṃsanā": "жестокое обращение", "rosanā": "досаждение", "parūpaghāto": "причинение вреда другим",
    "ūpaghāto": "причинение вреда",
    "metti": "доброжелательность", "mettāyanā": "проявление доброжелательности",
    "mettācetovimutti": "освобождение ума доброжелательностью", "karuṇā": "сострадание",
    "karuṇāyitattaṃ": "состояние сострадания", "karuṇācetovimutti": "освобождение ума состраданием",
    "cetovimutti": "освобождение ума", "vimutti": "освобождение",
    "kusalā dhammā": "благие явления",
    # eighteen elements, Abhidhamma part (2-183, 2-184)
    "rūpa": "видимая форма", "gandha": "запах", "rasa": "вкус", "dhammadhātu": "элемент объектов ума",
    "mānasaṃ": "умственная деятельность", "uppajjati": "возникать", "uppajjati cittaṃ": "возникать ум",
    "uppajjitvā": "возникновение", "niruddha": "прекращение", "samanantarā": "сразу после",
    "samannāhāro": "обращение внимания", "tajjā": "соответствующий", "paṭicca": "в зависимости от",
    "manindriyaṃ": "способность ума", "rūpe": "видимые формы", "gandhe": "запахи", "sadde": "звуки",
    "rase": "вкусы", "phoṭṭhabbe": "осязаемое", "vā pana": "или же",
})

# ---------------------------------------------------------------------------- per-segment overrides
# Pañhāpucchaka: Tika (2-170, 2-187) as the sample's 2-152 (the text quotes the participle «сопровождаемые»);
# Duka (2-171, 2-188) as the sample's 2-153 (finite «сопровождаются» only). pahātabbā = устраняться (text
# «устраняются» only).
_DUKA = {"pahātabbā": "устраняться", "sahagatā": "сопровождаться",
         "upekkhāsahagatā": "сопровождаться невозмутимостью", "sukhasahagatā": "сопровождаться счастьем",
         "pītisahagatā": "сопровождаться восторгом",
         "rūpā": "материальный", "cetasikaṃ": "сопутствующий уму", "asaṃkiliṭṭhā": "не омрачённый"}
# ch. 3 elements: «а также всё другое …» (yaṃ vā pana = а также всё, aññampi = другой)
_ALSO = {"yaṃ vā pana": "а также всё"}
_ELEM_ADJ = {  # «элемент X, относящийся к внутреннему / внешнему»
    "2-175": "огонь", "2-176": "ветер", "2-177": "пространство"}
OVERRIDES = {
    "2-154": {"Dhammā": "объекты ума"},
    "2-156": {"rūpaṃ": "видимая форма"},
    "2-161": {"sukha": "удовольствие", "dukkha": "боль"},
    "2-162": {"rūpaṃ": "видимая форма", "rūpa": "видимая форма"},
    "2-166": {"sukha": "доставляющий удовольствие", "dukkha": "болезненный"},
    "2-167": {"rūpaṃ": "материальная форма", "hetu": "корень"},
    "2-170": {"pahātabbā": "устраняться"},
    "2-171": dict(_DUKA),
    "2-172": {"viññāṇadhātu": "элемент сознания", "viññāṇa": "сознание"},
    "2-173": {**_ALSO, "maṇi": "драгоценный камень"},
    "2-174": {**_ALSO, "raso": "сок"},
    "2-175": {**_ALSO, "sūriya": "солнце", "sammā": "правильно"},
    "2-176": {**_ALSO, "parittā": "слабый"},
    "2-177": dict(_ALSO),
    "2-178": {"viññāṇadhātu": "элемент сознания", "viññāṇa": "сознание"},
    "2-179": {"sukha": "удовольствие", "dukkha": "боль"},
    "2-180": {"sukhaṃ": "удовольствие", "dukkhaṃ": "боль", "dukkhā": "болезненный",
              "cetasikaṃ": "душевный", "vedanā": "чувство", "upekkhā": "невозмутимость"},
    "2-182": {"khandha": "совокупность", "rūpā": "материальная форма", "vedanā": "чувство",
              "āvacarā": "относящийся к" + GAP + "миру"},
    "2-184": {"rūpaṃ": "материальная форма", "mano": "разум", "cittaṃ": "ум"},
    "2-187": {"pahātabbā": "устраняться"},
    "2-188": dict(_DUKA),
}
for _bid, _noun in _ELEM_ADJ.items():
    _p = {"огонь": "tejo", "ветер": "vāyo", "пространство": "ākāsa"}[_noun]
    _gen = {"огонь": "огня", "ветер": "ветра", "пространство": "пространства"}[_noun]
    OVERRIDES.setdefault(_bid, {}).update({
        f"ajjhattikā {_p}": f"{_noun}{GAP}относящийся к внутреннему",
        f"bāhirā {_p}": f"{_noun}{GAP}относящийся к внешнему",
        f"ajjhattikā {_p}dhātu": f"элемент {_gen} относящийся к внутреннему",
        f"bāhirā {_p}dhātu": f"элемент {_gen} относящийся к внешнему",
    })

# Same Pāli fragment, different Russian wording by segment: the first candidate found in the
# segment's Russian wins (the order is the preference; as map_sample_ru.py).
CHOICES = {
    "upādāniyo": ["служащий объектом цепляния", "служащий его объектом"],
    "upādāniyā": ["служащий объектом цепляния", "служащий его объектом"],
}

# presence-check exceptions (value correct; inflection outside present()'s tolerance)
EXC = {**EXCEPTIONS,
       "samma": "тарелки ~ тарелок (fleeting vowel), = pi-1 ^1-620",
       "vāta": "ветер ~ ветра (fleeting vowel), = pi-1 ^1-620",
       "viheṭheti": "мучить ~ мучает (verb stem alternation)"}


def resolver_for(part):
    ru, pi = read_russian(part), read_pali(part)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        if lc(kw) in ov:
            return ov[lc(kw)]
        if kw == "hetuko":
            return hetuko_value(pi.get(bid, ""))
        if lc(kw) in CHOICES:
            for cand in CHOICES[lc(kw)]:
                if present(cand, ru.get(bid, "")):
                    return cand
            return CHOICES[lc(kw)][0]
        return value(kw, kws, T)
    return resolve


def allowed(part):
    return {(bid, kw): EXC[lc(kw)] for bid, kws in read_keywords(part) for kw in kws if lc(kw) in EXC}


if __name__ == "__main__":
    for p in PARTS:
        build_part(p, resolver_for(p))
        verify(p, show=300, allowed=allowed(p))
