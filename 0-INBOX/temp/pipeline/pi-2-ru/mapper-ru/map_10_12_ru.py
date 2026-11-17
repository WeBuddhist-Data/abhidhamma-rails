"""Build the Pāli->Russian keyword maps for pi-2 (Vibhaṅga) chapters 10-bojjhangavibhango,
11-maggangavibhango and 12-jhanavibhango.

usage: python -I -X utf8 map_10_12_ru.py [PART ...]           (writes <part>.mapped.md and verifies; default: all three,
                                                             in book order)
       python -I -X utf8 map_10_12_ru.py --dump PART [--miss]  (prints every keyword=value with a presence flag;
                                                             --miss: only the flagged ones; no writing)

Resolution order per keyword: OVERRIDES[bid][kw]  ->  context rules (resolve())  ->  T (this file: map_7_9_ru.T + the
chapter 10-12 additions)  ->  pi-1 CH2 / MATRIX.
Conventions: ru-map-conventions-pi2.md (+ the pi-1 file and the pi-1 cleanup_map_ru.py), notes-map-2-3.md,
notes-map-4-5.md, notes-map-6.md, notes-map-7-9.md; new decisions: notes-map-10-12.md.
"""
import pathlib
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import map_7_9_ru as M79  # noqa: E402  (read-only: its table T, _PANHA, CHOICES, EXC)
from map_common_pi2_ru import (GAP, NDE, build_part, hetuko_value, lc, present,  # noqa: E402,F401
                               read_keywords, read_pali, read_russian, value, verify)

PARTS = ["10-bojjhangavibhango", "11-maggangavibhango", "12-jhanavibhango"]

# ---------------------------------------------------------------------------- table
T = dict(M79.T)
assert not any(v.startswith("классификация") for v in T.values())

T.update({
    # ================================================================ ch. 10 Bojjhaṅga
    # ---- headings / names (pi-5 bojjhaṅgā = факторы пробуждения; stem singular as Khandha / Satipaṭṭhāna)
    "bojjhaṅga": "фактор пробуждения", "bojjhaṅgā": "факторы пробуждения",
    "bojjhaṅgānaṃ": "факторы пробуждения", "sambojjhaṅgo": "фактор пробуждения",
    "satisambojjhaṅga": "фактор пробуждения осознанности",
    "dhammavicayasambojjhaṅga": "фактор пробуждения исследования явлений",
    "vīriyasambojjhaṅga": "фактор пробуждения усердия", "pītisambojjhaṅga": "фактор пробуждения восторга",
    "passaddhisambojjhaṅga": "фактор пробуждения безмятежности",
    "samādhisambojjhaṅga": "фактор пробуждения сосредоточения",
    "upekkhāsambojjhaṅga": "фактор пробуждения невозмутимости",
    "pītisambojjhaṅgo": "фактор пробуждения восторга",
    "passaddhisambojjhaṅgo": "фактор пробуждения безмятежности",
    "upekkhāsambojjhaṅgo": "фактор пробуждения невозмутимости",
    "sambojjhaṅgaṃ bhāveti": "развивать фактор пробуждения",
    # ---- Suttanta 2-467: «Вот монах осознан, наделён высшей осознанностью и благоразумием, он помнит и припоминает
    # и то, что сделано давно, и то, что сказано давно …»
    "satimā": "осознанный", "paramena": "высший", "nepakkena": "благоразумие",
    "cirakatampi": "сделанный давно", "saritā": "помнить", "anussaritā": "припоминать",
    "viharanto": "пребывать", "dhammaṃ": "явление", "paññāya": "мудрость",
    "pavicinati": "исследовать", "pavicarati": "обдумывать",
    "parivīmaṃsamāpajjati": "подвергать" + GAP + "всестороннему изучению", "āpajjati": "подвергать",
    "āraddhaṃ": "пробуждённый", "asallīnaṃ": "неослабный", "nirāmisā": "неплотский",
    "pītimanassa": "ум полный восторга", "kāyopi": "тело", "passambhati": "утихать",
    "sukhino": "счастливый", "ajjhupekkhitā": "взирать с полной невозмутимостью",
    # ---- 2-469: «Есть осознанность в отношении внутренних явлений … И осознанность … является фактором пробуждения
    # осознанности и ведёт к высшему знанию, к полному пробуждению, к нирване»
    "ajjhattaṃ dhammesu": "внутренние явления", "tadapi": NDE, "abhiññāya": "высшее знание",
    "sambodhāya": "полное пробуждение", "saṃvattati": "вести",
    # ---- 2-471: «опирающийся на уединение, опирающийся на бесстрастие, опирающийся на прекращение, ведущий к отказу»
    "nirodha": "прекращение", "virāga": "бесстрастие", "vossagga": "отказ", "pariṇāmiṃ": "ведущий",
    # ---- Abhidhamma definitions (2-474 …): passaddhi / upekkhā strings
    "paṭippassambhanā": "полное утихание", "paṭippassambhitattaṃ": "состояние полного утихания",
    "upekkhanā": "проявление невозмутимости", "ajjhupekkhanā": "полная невозмутимость",
    "majjhattatā": "уравновешенность",
    # ---- Pañhāpucchaka (2-483 … 2-485)
    "lokuttarā": "надмирский", "na hetū": "не являющийся корнями",
    # ================================================================ ch. 11 Maggaṅga
    "aṅga": "фактор", "maggaṅga": "фактор пути", "maggaṅgā": "факторы пути", "maggaṅgānaṃ": "факторы пути",
    "aṅgānaṃ": "факторы", "ariyo": "благородный",
    # ---- Suttanta 2-487 (= ch. 4 2-205 path bodies; values kept)
    "musāvādā veramaṇī": "уклонение от лжи", "pāṇātipātā veramaṇī": "уклонение от убийства живых существ",
    "adinnādānā veramaṇī": "уклонение от взятия того что не дано",
    "kāmesumicchācārā veramaṇī": "уклонение от неправильного поведения в чувственных удовольствиях",
    "jīvikaṃ": "жизнь", "dhammesu dhammānupassī": "в явлениях созерцающий явления",
    "vitakkavicārānaṃ": "направленная мысль и удержание мысли",
    # ---- 2-489: «развивает правильное воззрение … правильный помысел …» (accusatives)
    "diṭṭhiṃ": "воззрение", "saṅkappaṃ": "помысел", "vācaṃ": "речь", "ājīvaṃ": "образ жизни",
    "vāyāmaṃ": "усилие", "satiṃ": "осознанность",
    # ---- 2-497, 2-503: «Остальные явления связаны с правильным помыслом / усилием / правильной осознанностью»
    "saṅkappena": "помысел", "vāyāmena": "усилие", "satiyā": "осознанность",
    # ---- Pañhāpucchaka (2-505 … 2-507)
    "anupādāniyā": "не служащий его объектом", "asaṃkilesikā": "не подверженный омрачению",
    "araṇāti": "свободный от борьбы",
    # ================================================================ ch. 12 Jhāna (new keys; ch. 12-only values of
    # keys already in the table are in CH12 below)
    "jhāna": "медитативное погружение", "jhānāni": "медитативные погружения",
    "jhānānaṃ": "медитативные погружения", "jhānassa": "медитативное погружение",
    "catutthassa jhānassa": "четвёртое медитативное погружение",
    "rūpāvacara": "относящийся к миру форм", "arūpāvacara": "относящийся к миру без форм",
    "ārūpāvacara": "относящийся к миру без форм", "lokuttara": "надмирский",
    "rūpārūpāvacarakiriyā": "функциональный ум относящийся к миру форм и к миру без форм",
    # ---- 2-508 / 2-511 …: «пребывает сдержанным сдержанностью свода монашеских правил, обладающим подобающим
    # поведением и подходящими местами посещения, видящим опасность в малейших проступках …»
    "pātimokkha": "свод монашеских правил", "saṃvara": "сдержанность", "saṃvuto": "сдержанный",
    "saṃvutoti": "сдержанный", "ācāra": "подобающее поведение", "gocara": "подходящее место посещения",
    "aṇumattesu": "малейший", "vajjesu": "проступок", "aṇumattesu vajjesu": "малейшие проступки",
    "bhaya": "опасность", "dassāvī": "видящий", "samādāya": "принимать на себя", "sikkhati": "обучаться",
    "sikkhā": "обучение", "padesu": "правила", "padesū": "правила", "dvāro": "врата",
    "mattaññū": "знающий меру", "bhojane mattaññū": "знающий меру в еде",
    "pubbarattāpararattaṃ": "в начале и в конце ночи", "anuyutto": "преданный",
    "jāgariyānuyogamanuyutto": "преданный бодрствованию", "sātaccaṃ": "постоянство", "sātacca": "постоянство",
    "nepakkaṃ": "благоразумие", "nepakka": "благоразумие", "bodhi": "пробуждение", "pakkhikānaṃ": "способствующий",
    "bodhipakkhikānaṃ": "способствующий пробуждению",
    "bodhipakkhikānaṃ dhammānaṃ": "явления способствующие пробуждению",
    "aṅgo": "фактор", "aṅgā": "факторы",
    # ---- «Идя вперёд и идя назад, он действует с ясным пониманием …» (2-508, 2-523, 2-525)
    "abhikkante": "идти вперёд", "paṭikkante": "идти назад", "abhikkamati": "идти вперёд",
    "paṭikkamati": "идти назад", "sampajānakārī": "действовать с ясным пониманием",
    "sato sampajānakārī": "осознанно действовать с ясным пониманием", "sampajāna": "ясное понимание",
    "ālokite": "смотреть прямо", "vilokite": "смотреть по сторонам", "āloketi": "смотреть прямо",
    "viloketi": "смотреть по сторонам", "samiñjite": "сгибать", "pasārite": "распрямлять",
    "samiñjeti": "сгибать", "pasāreti": "распрямлять", "saṅghāṭi": "накидка", "cīvara": "одеяние",
    "dhāraṇe": "носить", "asite": "есть", "pīte": "пить", "khāyite": "жевать", "sāyite": "пробовать на вкус",
    "uccāra": "большая" + GAP + "нужда", "passāva": "малая нужда",   # «большую и малую нужду»
    "gate": "ходить", "ṭhite": "стоять",
    "nisinne": "сидеть", "sutte": "засыпать", "jāgarite": "бодрствовать", "bhāsite": "говорить",
    "tuṇhībhāve": "молчать", "tuṇhī": "молчать",
    # ---- «Он выбирает уединённое жилище: лес, подножие дерева, гору, ущелье, горную пещеру, кладбище, лесную чащу,
    # открытое место, копну соломы, тихое, бесшумное, лишённое людской суеты, укрытое от людей, подходящее для
    # уединения» (2-508, 2-526 … 2-534)
    "bhajati": "выбирать", "vivittaṃ": "уединённый", "senāsanaṃ": "жилище",
    "vivittaṃ senāsanaṃ": "уединённое жилище", "araññaṃ": "лес", "arañña": "лес", "rukkha": "дерево",
    "pabbataṃ": "гора", "kandaraṃ": "ущелье", "kandarā": "ущелье", "guhaṃ": "пещера", "guhā": "пещера",
    "susānaṃ": "кладбище", "vanapatthaṃ": "лесная чаща", "patthaṃ": "чаща", "vanapattha": "лесная чаща",
    "pattha": "чаща", "abbhokāsaṃ": "открытое место", "abbhokāso": "открытое место", "palāla": "солома",
    "puñjaṃ": "копна", "puñjo": "копна", "nigghosaṃ": "шумный", "vijanavātaṃ": "лишённый людской суеты",
    "vātaṃ": "суета", "rāhasseyyakaṃ": "укрытый", "paṭisallāna": "уединение", "sāruppaṃ": "подходящий",
    "santike": "вблизи", "dūre": "вдали", "anākiṇṇaṃ": "не заполненный", "gahaṭṭhehi": "домохозяева",
    "pabbajitehi": "ушедшие в бездомность",
    "mañcopi": "ложе", "pīṭhampi": "сиденье", "bhisipi": "матрас", "bibbohanampi": "подушка",
    "vihāropi": "обитель", "aḍḍhayogopi": "навес", "pāsādopi": "дворец", "aṭṭopi": "башня",
    "māḷopi": "дом с островерхой крышей", "leṇampi": "скальная келья", "guhāpi": "пещера",
    "mūlampi": "подножие", "gumbopi": "роща", "yattha vā pana": "где бы ни", "bhikkhū": "монахи",
    "paṭikkamanti": "останавливаться",
    "sambhajati": "занимать", "sevati": "посещать", "nisevati": "часто посещать", "saṃsevati": "постоянно посещать",
    "bahi": "за пределами", "indakhīlā": "пограничный столб", "nikkhamitvā": NDE,
    "adhivacanaṃ": "наименование", "senāsanānaṃ": "жилища", "senāsanānaṃ adhivacanaṃ": "наименование" + GAP + "жилищ",
    "dūrānametaṃ": "отдалённый", "dūrānametaṃ senāsanānaṃ": "отдалённые жилища",
    "vanasaṇḍānametaṃ": "лесной", "bhīsanakānametaṃ": "пугающий", "salomahaṃsānametaṃ": "наводящий трепет",
    "salomahaṃsānametaṃ senāsanānaṃ": "наводящие трепет жилища",
    "pariyantānametaṃ": "находящийся на окраине",
    "pariyantānametaṃ senāsanānaṃ": "находящиеся на окраине жилища",
    "manussūpacārānametaṃ": "людские места", "ūpacārānametaṃ": "места",
    "durabhisambhavānametaṃ": "труднодоступный", "durabhisambhavānametaṃ senāsanānaṃ": "труднодоступные жилища",
    # ---- «Удалившись в лес … он садится, скрестив ноги, держа тело прямо, установив осознанность перед собой»
    "gato": "удалиться", "suññāgāragato": "удалиться" + GAP + "в пустой дом", "āgāra": "дом",
    "nisīdati": "садиться", "nisinno": "сидеть", "pallaṅkaṃ": "скрестить ноги", "ābhujitvā": "скрестить",
    "ujuṃ": "прямо", "ujuko": "прямой", "kāyaṃ": "тело", "ṭhito": "устойчивый", "paṇihito": "правильно поставленный",
    "parimukhaṃ": "перед собой", "upaṭṭhapetvā": "установить", "nāsikagge": "кончик носа", "agge": "кончик",
    "mukha": "рот", "nimitte": "область",
    # ---- «Оставив алчность в отношении мира, он пребывает с умом, свободным от алчности …» (2-508, 2-538 …)
    "abhijjhaṃ": "алчность", "abhijjhāya": "алчность", "vigatābhijjhena": "свободный от алчности",
    "ābhijjhena": "алчность", "cetasā": "ум", "vigatābhijjhena cetasā": "ум свободный от алчности",
    "parisodheti": "очищать", "cittaṃ parisodheti": "очищать ум", "parisodhetī": "очищать",
    "cittaṃ parisodhetī": "очищать ум", "sodheti": "очищать", "moceti": "освобождать",
    "vimoceti": "тщательно освобождать", "parimoceti": "полностью освобождать",
    "padosaṃ": "сильная злоба", "padoso": "сильная злоба", "byāpādo": "недоброжелательность",
    "kodho": "гнев", "kujjhitattaṃ": "состояние гнева", "virodho": "вражда",
    "abyāpannaṃ": "свободный от недоброжелательности", "abyāpannacitto": "ум свободный от недоброжелательности",
    "pāṇa": "живой", "bhūta": "существо", "ānukampī": "сострадающий",
    "hitānukampī": "сострадающий" + GAP + "желающий" + GAP + "блага",
    "thinamiddhaṃ pahāya": "оставить вялость и сонливость", "thinamiddhaṃ pahāyā": "оставить вялость и сонливость",
    "uddhaccakukkuccaṃ pahāya": "оставить беспокойство и угрызения",
    "uddhaccakukkuccaṃ pahāyā": "оставить беспокойство и угрызения",
    "vicikicchaṃ pahāya": "оставить колебание", "vicikicchaṃ pahāyā": "оставить колебание",
    "āloka": "свет", "ālokā": "светлый", "saññī": "воспринимающий", "anuddhato": "без беспокойства",
    "vūpasanta": "успокоенный", "vūpasantacitto": "успокоенный ум", "vūpasantaṃ": "умиротворённый",
    "samitaṃ": "усмирённый", "tiṇṇa": "преодолевший", "akathaṃkathī": "свободный от недоумений",
    "nīvaraṇe": "помехи", "nīvaraṇehi": "помехи", "upakkilese": "загрязнения", "dubbalīkaraṇe": "ослабляющий",
    "akusalehi": "неблагой", "akusalehi dhammehi": "неблагие явления", "dhammehi": "явления",
    "domanassānaṃ": "уныние",
    # ---- thina / middha (pi-1 strings), 2-546 / 2-547
    "thinaṃ": "вялость", "thiyanā": "проявление вялости", "akalyatā": "неготовность",
    "akammaññatā": "неработоспособность", "olīyanā": "оседание", "sallīyanā": "полное оседание", "līnaṃ": "косность",
    "līyanā": "проявление косности", "līyitattaṃ": "состояние косности", "onāho": "окутанность",
    "pariyonāho": "полная окутанность", "samorodho": "скованность", "suppaṃ": "дремота",
    "pacalāyikā": "клевание носом", "suppanā": "засыпание", "kāyassa": "тело",
    "vigata": "свободный", "thinamiddhassa": "вялость и сонливость", "middhassa": "сонливость",
    "thinamiddhā": "вялость и сонливость", "vantattā": "извергнутый", "muttattā": "отпущенный",
    "pahīnattā": "устранённый", "paṭinissaṭṭhattā": "отброшенный",
    # ---- 2-549, 2-597: «Это восприятие светлое, открытое, чистое, ясное»
    "vivaṭā": "открытый", "parisuddhā": "чистый", "pariyodātā": "ясный", "pārisuddhi": "чистота",
    # ---- kukkucca (pi-1), 2-552 / 2-553
    "akappiye": "недопустимый", "kappiye": "допустимый", "avajje": "безупречный", "vajje": "предосудительный",
    "saññitā": "восприятие", "evarūpaṃ": "такой", "kukkuccāyanā": "мучение угрызениями",
    "vippaṭisāro": "раскаяние", "vilekhā": "терзание",
    "uddhaccakukkuccassa": "беспокойство и угрызения", "kukkuccassa": "угрызения",
    "uddhaccakukkuccā": "беспокойство и угрызения",
    # ---- 2-558 / 2-559: «это колебание он преодолел, превозмог, полностью превозмог, переправился через него,
    # достиг другого берега» / «не сомневается, не колеблется, свободен от недоумений …»
    "tiṇṇo": "преодолеть", "nittiṇṇo": "полностью превозмочь", "pāra": "другой берег",
    "vicikicchāya": "колебание", "vicikicchati": "колебаться", "nikkathaṃkathī": "полностью свободный от недоумений",
    "vikathaṃkatho": "избавленный от недоумений",
    # ---- 2-564: kāmā
    "kāmo": "чувственное удовольствие", "chandarāgo": "страстное желание", "saṅkapparāgo": "страсть к помыслам",
    "kāmacchando": "чувственное желание",
    # ---- vitakka / vicāra strings (pi-1)
    "vuccati vicāro": "называться удержанием мысли", "anusandhanatā": "непрерывная связь" + GAP + "с объектом",
    "upavicāro": "пристальное удержание мысли", "anucāro": "последовательное движение мысли",
    # ---- 2-566 / 2-577: «они родились в этом уединении, зародились, возникли, полностью возникли, проявились»
    "viveke": "уединение", "samādhimhi": "сосредоточение", "sampasādo": "ясность",
    "sañjātā": "зародиться",
    # ---- 2-567: «Это счастье сопровождается этим восторгом, рождено вместе с ним, соединено с ним, связано с ним»
    "pītisukha": "восторг и счастье", "sahajātaṃ": "рождённый вместе",
    # ---- 2-568 …: «первое по порядку счёта. В него он входит первым»; 2-570 …: «Входит»: обретение …
    "gaṇanānupubbatā": "порядок счёта", "ānupubbatā": "порядок", "samāpajjatīti": "входить",
    "upasampajjā": "входить", "viharatī": "пребывать",
    "ajjhatta": "внутри себя", "sampasādana": "ясность", "ekodibhāva": "единение",
    # ---- 2-587 / 2-588
    "paṭisaṃvedetī": "испытывать", "buddhā": "будды", "sāvakā": "ученики", "desenti": "излагать",
    "paññapenti": "сообщать", "paṭṭhapenti": "устанавливать", "vivaranti": "раскрывать", "vibhajanti": "разбирать",
    "uttāniṃ": "прояснять", "pakāsenti": "разъяснять",
    "somanassaṃ": "радость",
    # ---- arūpa (2-508, 2-602 … 2-621)
    "samatikkamā": "преодоление", "samatikkammā": "преодолеть", "rūpasaññānaṃ": "восприятия материальной формы",
    "saññānaṃ": "восприятия", "paṭigha": "соударение", "paṭighasaññānaṃ": "восприятия соударения",
    "vuccanti paṭighasaññāyo": "называться восприятиями соударения",
    "nānatta": "разнообразие", "nānattasaññānaṃ": "восприятия разнообразия", "amanasikārā": "без внимания",
    "manasi karoti": "уделять внимание", "ananto": "бесконечный", "anantaṃ": "бесконечный",
    "ākāsānañcāyatanaṃ": "сфера бесконечного пространства", "viññāṇañcāyatanaṃ": "сфера бесконечного сознания",
    "nevasaññānāsaññāyatanaṃ": "сфера ни восприятия ни невосприятия", "natthi kiñcī": "нет ничего",
    "āyatanassa": "сфера", "ākāsānañcāyatanassa": "сфера бесконечного пространства",
    "viññāṇañcāyatanassa": "сфера бесконечного сознания", "ākiñcaññāyatanassa": "сфера отсутствия чего-либо",
    "nevasaññānāsaññāyatanassa": "сфера ни восприятия ни невосприятия",
    "samāpattiṃ": "медитативное достижение", "vihārissa": "пребывать",
    "sukhavihārissa": "пребывать" + GAP + "в счастье",   # «пребывает (в ней) в счастье»
    "upapannassa": "переродиться", "atikkanto": "преодолеть", "vītikkanto": "миновать",
    "samatikkanto": "полностью преодолеть", "asamāpannassa": "не войти в медитативное достижение",
    "samaṅgissa": "наделённый", "gataṃ": "считаться", "ṭhapeti": "устанавливать",
    "saṇṭhapeti": "прочно устанавливать", "pharati": "охватывать", "ākāsaṃ": "пространство",
    "phuṭṭhaṃ": "охваченный", "vibhāveti": "рассеивать", "santato": "спокойный",
    "saṅkhārāvasesasamāpattiṃ": "медитативное достижение с остатком формирующих факторов", "āvasesa": "остаток",
    "nevasaññīnāsaññī": "ни воспринимающий ни невоспринимающий", "nāsaññī": "невоспринимающий",
    # ---- Abhidhamma (2-623 …)
    "pañcaṅgikaṃ jhānaṃ": "пятичастное медитативное погружение",
    "caturaṅgikaṃ jhānaṃ": "четырёхчастное медитативное погружение",
    "tivaṅgikaṃ": "трёхчастный", "tivaṅgikaṃ jhānaṃ": "трёхчастное медитативное погружение",
    "duvaṅgikaṃ": "двухчастный", "duvaṅgikaṃ jhānaṃ": "двухчастное медитативное погружение",
    "rūpūpapattiyā maggaṃ": "путь к рождению в мире форм",
    "arūpūpapattiyā maggaṃ": "путь к рождению в мире без форм",
    "sukhavihāraṃ": "пребывание в счастье", "nākusalaṃ": "неблагой",
    "neva kusalaṃ nākusalaṃ": "ни благой ни неблагой",
    # ---- Pañhāpucchaka (2-639 … 2-641): «кроме возникшего в них приятного чувства …»
    "ācayagāmino": "ведущий к накоплению", "etthuppannaṃ": "возникший", "vedanaṃ": "чувство",
    "pītiṃ": "восторг", "upekkhaṃ": "невозмутимость", "vicāre": "удержание мысли",
    "vitakkavicāre": "направленная мысль и удержание мысли",
    "etthuppannaṃ sukhaṃ": "возникшее в них счастье", "etthuppannaṃ pītiṃ": "возникший в них восторг",
    "etthuppannaṃ upekkhaṃ": "возникшая в нём невозмутимость",
    "etthuppannaṃ vicāraṃ": "возникшее в нём удержание мысли",
    "etthuppanne vitakkavicāre": "возникшие в нём направленная мысль и удержание мысли",
    "atītārammaṇaṃ": "с прошлым объектом", "anāgatārammaṇaṃ": "с будущим объектом",
    "paccuppannārammaṇaṃ": "с настоящим объектом",
    # ---- definitions 2-509 … 2-518
    "diṭṭhiyā": "воззрение", "khantiyā": "приятие", "ruciyā": "предпочтение", "ādāye": "выбор",
    "vinaye": "дисциплина", "dhammavinaye": "Учение и дисциплина", "pāvacane": "слово",
    "brahmacariye": "святая жизнь", "cariye": "жизнь", "satthu": "Учитель", "sāsane": "наставление",
    "samaññāya": "общепринятое название", "paṭiññāya": "собственное заявление", "bhikkhatīti": "просить подаяние",
    "bhikkhakoti": "жить подаянием", "bhikkhā": "подаяние", "cariyaṃ": "жизнь", "bhinna": "лоскут",
    "paṭa": "одежда", "dharoti": "носить", "bhindati": "разрушать", "bhinnattā": "разрушенный",
    "odhiso": "частичный", "anodhiso": "полный", "kilesānaṃ": "омрачения", "aggo": "превосходный",
    "bhadro": "хороший", "sāro": "сердцевина", "samaggena saṅghena": "единая община", "saṅghena": "община",
    "ñatticatutthena": "с предложением и тремя объявлениями", "ñatti": "предложение", "kammena": "процедура",
    "akuppena": "неотменимый", "ṭhānārahena": "соответствующий правилам", "ārahena": "соответствующий",
    "upasampanno": "получивший полное посвящение",
    "sīlaṃ": "нравственность", "patiṭṭhā": "опора", "ādi": "начало", "caraṇaṃ": "поведение",
    "saṃyamo": "обуздание", "saṃvaro": "сдержанность", "mokkhaṃ": "главное", "pāmokkhaṃ": "первейшее",
    "kāyiko": "тело", "vācasiko": "речь", "avītikkamo": "отсутствие нарушений",
    "kāyiko avītikkamo": "отсутствие нарушений телом", "vītikkamo": "нарушение",
    "ācāro": "подобающее поведение", "anācāro": "неподобающее поведение", "dussīlyaṃ": "безнравственность",
    "veḷu": "бамбук", "dānena": "дарение", "sināna": "мыльный порошок", "dantakaṭṭha": "зубочистка",
    "cāṭukamyatāya": "лесть", "muggasūpyatāya": "угодничество", "pāribhaṭayatāya": "нянченье чужих детей",
    "jaṅgha": "побегушки", "pesanikena": "выполнение поручений", "buddha": "Будда", "paṭikuṭṭhena": "порицаемый",
    "ājīvena": "образ жизни",
    "gocaro": "подходящее место посещения", "agocaro": "неподходящее место посещения",
    "gocarena": "подходящее место посещения", "ācārena": "подобающее поведение",
    "vesiyā": "блудница", "vidhavā": "вдова", "thulla": "старый", "kumāri": "дева", "paṇḍaka": "евнух",
    "pānāgāra": "питейный дом", "saṃsaṭṭho": "общение", "ananulomikena": "неподобающий", "rājūhi": "цари",
    "rāja": "царский", "mahāmattehi": "сановники", "titthiyehi": "иноверцы", "sāvakehi": "ученики",
    "kulāni": "семьи", "saddhāni": "иметь веру", "bhūtāni": "служить", "akkosaka": "бранить",
    "paribhāsakāni": "поносить", "kāmāni": "желать", "hita": "благо", "khema": "безопасность",
    "kāsāva": "жёлтые одежды", "pajjotāni": "озарённый сиянием", "isi": "мудрец", "paṭivātāni": "овеянный",
    "payirupāsati": "почитать", "bhikkhūnaṃ": "монахи", "bhikkhunīnaṃ": "монахини", "upāsakānaṃ": "миряне",
    "upāsikānaṃ": "мирянки",
    "appamattakāni": "незначительный", "oramattakāni": "мелкий", "lahusāni": "лёгкий", "sammatāni": "считаться",
    "karaṇīyāni": "исправляться", "saṃyama": "обуздание",
    "cittuppādakaraṇīyāni": "исправляться решением ума", "paṭibaddhāni": "связанный", "vajja": "проступок",
    "ādīnava": "вред", "nissaraṇa": "выход",
    "sikkhāyo": "виды обучения", "sabbena sabbaṃ": "всецело", "sabbathā": "во всех отношениях",
    "asesaṃ": "без остатка", "nissesaṃ": "полностью",
    "guttadvāratā": "охранение врат", "gutti": "охрана", "agutti": "отсутствие охраны", "gopanā": "защита",
    "ārakkho": "присмотр", "viharantaṃ": "пребывать", "asaṃvutaṃ": "необузданный",
    "cakkhundriyaṃ asaṃvutaṃ": "необузданная способность глаза",
    "manindriyaṃ asaṃvutaṃ": "необузданная способность ума", "anvāssaveyyuṃ": "проникнуть",
    "gāhī": "цепляться", "nimitta": "общий облик", "domanassā": "уныние",
    "abhijjhādomanassā": "алчность и уныние", "pāpakā": "дурной", "saṃvarāya": "обуздать",
    "paṭipajjati": "стараться", "rakkhati": "охранять", "saṃvaraṃ āpajjati": "соблюдать сдержанность",
    "sutvā": "услышав", "ghāyitvā": "понюхав", "sāyitvā": "попробовав", "phusitvā": "коснувшись",
    "viññāya": "познав", "manasā": "ум",
    "bhojane mattaññutā": "знание меры в еде", "asantuṭṭhitā": "отсутствие довольства",
    "ayoniso": "неразумно", "davāya": "забава", "madāya": "упоение", "maṇḍanāya": "привлекательность",
    "vibhūsanāya": "украшение тела", "āhāreti": "принимать", "paṭisaṅkhā": "размышление",
    "yāpanāya": "поддержание", "vihiṃsūparatiyā": "прекращение мучений",
    "brahmacariyānuggahāya": "поддержка духовной жизни", "ānuggahāya": "поддержка", "iti": "так",
    "purāṇañca": "прежний", "yātrā": "продолжаться", "anavajjatā": "безупречно", "phāsu": "спокойно",
    "vihāro": "жить",
    # ---- 2-519: «днём, во время хождения и сидения, очищает ум от явлений, создающих препятствия; … в среднюю
    # стражу ночи ложится на правый бок в позе льва, положив ступню на ступню, … уделив внимание мысли о вставании»
    "caṅkamena": "хождение", "nisajjāya": "сидение", "āvaraṇīyehi": "создающий препятствия",
    "āvaraṇīyehi dhammehi": "явления создающие препятствия",
    "āvaraṇīyehi dhammehi cittaṃ": "ум от явлений создающих препятствия",
    "rattiyā": "ночь", "yāmaṃ": "стража", "majjhima": "средний", "dakkhiṇena": "правый", "passena": "бок",
    "sīha": "лев", "seyyaṃ": "поза", "pāde": "ступня", "accādhāya": "положить", "saññaṃ": "мысль",
    "manasikaritvā": "уделить внимание", "paccuṭṭhāya": "встать",
    "asammusanatā": "отсутствие забывчивости",
})

# ch. 12 values for keys that earlier chapters (or ch. 10/11) map differently; applied to ch. 12 only, after the
# per-segment OVERRIDES
CH12 = {
    "pahāya": "оставить", "pahāyā": "оставить",          # «Оставив …» (ch. 4/11 устранить)
    "ajjhattaṃ": "внутри себя",                          # jhāna formula; 2-555 внутри, 2-573 внутренний
    "sato": "осознанный",                                # 2-523 / 2-525 осознанно
    "sampanno": "обладающий",                            # «обладающим подобающим поведением»; 2-511 оснащённый
    "ekacco": "человек",                                 # «Вот человек …» (pi-1 ^1-1352)
    "micchā": "неправильный",                            # «неправильным образом жизни»
    "āyatanaṃ": "сфера",                                 # «сфера бесконечного пространства»
    "sahagataṃ": "сопровождение",                        # «в сопровождении восприятия сферы ни восприятия …»
    "mūlaṃ": "подножие", "mūla": "подножие",             # rukkhamūla «подножие дерева»
    "patta": "чаша для подаяния",                        # saṅghāṭipattacīvara; 2-513 листья
    "āpajjati": "соблюдать",                             # «соблюдает сдержанность» (pi-1 ^1-1352)
    "gutta": "охранение",                                # pi-1; 2-508 охранять
    "uppannā": "возникший",                              # «возникшая мудрость» (2-563)
}

# Pañhāpucchaka: finite verbs only («не сопровождается восторгом», «не устраняются»), as ch. 7-9 _PANHA
_PANHA = dict(M79._PANHA)
_PANHA.update({"sahagato": "сопровождаться", "pītisahagato": "сопровождаться восторгом",
               "sukhasahagato": "сопровождаться счастьем", "upekkhāsahagato": "сопровождаться невозмутимостью",
               "upekkhāsahagataṃ": "сопровождаться невозмутимостью"})
# «они родились в этом уединении / сосредоточении, зародились, возникли, полностью возникли, проявились» (2-566,
# 2-577): past-tense verbs -> infinitive
_BORN = {"jātā": "родиться", "sañjātā": "зародиться", "nibbattā": "возникнуть",
         "abhinibbattā": "полностью возникнуть", "pātubhūtā": "проявиться"}
# «Это счастье сопровождается этим восторгом, рождено вместе с ним …» (2-567, 2-578)
_WITH = {"sahagataṃ": "сопровождаться", "saha": "вместе"}
# «осознанно и с ясным пониманием идёт вперёд …» (2-523, 2-525)
_AWARE = {"sato": "осознанно"}

OVERRIDES = {
    # kāya of kāyapassaddhi «безмятежность умственного тела» (pi-1); kāyikaṃ = телесный
    "2-469": {"kāya": "умственное тело"},
    "2-484": dict(_PANHA), "2-485": {**_PANHA, "hetu": "корень"},
    # ch. 11: as ch. 4 2-205 / 2-206: ajjhattaṃ = внутри себя («с ясностью внутри себя»); micchā (micchāājīva
    # «неправильный образ жизни») = неправильный
    "2-487": {"ajjhattaṃ": "внутри себя", "micchā": "неправильный"},
    "2-492": {"micchā": "неправильный"},
    "2-506": dict(_PANHA), "2-507": {**_PANHA, "hetu": "корень"},
    # ---- ch. 12
    "2-508": {"gutta": "охранять", "saddaṃ": NDE},       # «охраняет врата чувств»; appasaddaṃ «тихое»
    "2-12-2-7-0": {"ārūpāvacara": "относящийся" + GAP + "к миру без форм"},   # «… к миру форм и к миру без форм»
    "2-509": {"dhamme": "Учение"},
    "2-519": {"kappeti": "ложиться"},                    # sīhaseyyaṃ kappeti «ложится … в позе льва»
    "2-558": {"gato": "переправиться"},                  # pāraṅgato «переправился через него»
    "2-510": {"sekkho": "обучающийся", "asekkho": "завершивший обучение"},   # «обучающийся монах»
    "2-511": {"sampanno": "оснащённый", "samāpattiyā": "достижение"},   # «для достижения благих явлений»
    "2-513": {"patta": "листья", "sīla": "нравственный", "veḷu": "бамбук"},  # «дарением листьев», «нравственная
    "2-514": {"vāta": "дыхание", "yoga": NDE},           # сдержанность»; «овеяны дыханием мудрецов»; yogakkhema
    "2-515": {"uppāda": "решение", "dassāvī": "видящий"},  # = «безопасность» (khema)
    "2-516": {"vattati": "следовать"},                   # «он следует им»
    "2-517": {"rūpaṃ": "видимая форма", "dhammaṃ": "объект ума"},
    "2-518": {"santuṭṭhitā": "довольство", "yoniso": "вдумчиво", "kāyassa": "тело"},   # = pi-1 ^1-1355
    "2-523": dict(_AWARE), "2-525": dict(_AWARE),
    "2-527": {"veḷu": "бамбуковый"},
    "2-532": {"saddaṃ": NDE}, "2-533": {"saddaṃ": NDE},
    "2-542": {"mano": "ум"}, "2-557": {"mano": "ум", "gāho": NDE},   # manopadoso / manovilekho; anekaṃsaggāho
    "2-546": {"kāyassa": "умственное тело"},             # «неготовность умственного тела» (pi-1)
    "2-555": {"ajjhattaṃ": "внутри"}, "2-573": {"ajjhattaṃ": "внутренний"},
    "2-566": dict(_BORN), "2-577": dict(_BORN),
    "2-567": dict(_WITH), "2-578": dict(_WITH),
    "2-594": {"sukhaṃ": "приятное", "dukkhaṃ": "болезненное"},   # «есть приятное, есть болезненное»
    "2-603": {"Rūpa": "видимая форма"},                  # «Восприятие видимых форм»
    "2-604": {"mano": "ум"},                             # manodhātu «элементом ума»
    "2-640": dict(_PANHA), "2-641": dict(_PANHA),
}
CHOICES = dict(M79.CHOICES)
EXC = {**M79.EXC,
       "pītimanassa": "ум полный восторга ~ «чей ум полон восторга» (short form, fleeting о)",
       "saṃvattati": "вести ~ ведёт (stem alternation), = pi-5 value",
       "saṅkappena": "помысел ~ помыслом (fleeting е)",
       # ch. 12: verbs rendered by a gerund or a finite form with a stem change (идти ~ идя / идёт, смотреть ~
       # смотря, носить ~ нося, пить ~ пьёт, сидеть ~ сидит, стоять ~ стоит, молчать ~ молчит)
       "abhikkante": "идти вперёд ~ идя вперёд (gerund)", "paṭikkante": "идти назад ~ идя назад (gerund)",
       "abhikkamati": "идти вперёд ~ идёт вперёд (stem alternation)",
       "paṭikkamati": "идти назад ~ идёт назад (stem alternation)",
       "ālokite": "смотреть прямо ~ смотря прямо (gerund)", "vilokite": "смотреть по сторонам ~ смотря (gerund)",
       "āloketi": "смотреть прямо ~ смотрит прямо (stem alternation)",
       "viloketi": "смотреть по сторонам ~ смотрит (stem alternation)",
       "dhāraṇe": "носить ~ нося (gerund)", "pīte": "пить ~ пьёт (stem alternation)",
       "nisinne": "сидеть ~ сидит (stem alternation)", "nisinno": "сидеть ~ сидит (stem alternation)",
       "ṭhite": "стоять ~ стоит (stem alternation)",
       "tuṇhībhāve": "молчать ~ молчит (stem alternation)", "tuṇhī": "молчать ~ молчит (stem alternation)",
       "nigghosaṃ": "шумный ~ «бесшумное» (positive part of a word with the negative prefix бес-)",
       "dantakaṭṭha": "зубочистка ~ зубочисток (fleeting о)", "upāsikānaṃ": "мирянки ~ мирянок (fleeting о)",
       "akkosaka": "бранить ~ бранят (verb stem)", "paribhāsakāni": "поносить ~ поносят (verb stem)",
       "bhūtāni": "служить ~ служат (verb stem)", "sīha": "лев ~ льва (fleeting е)",
       "nittiṇṇo": "полностью превозмочь ~ полностью превозмог (past stem)",
       "nikkathaṃkathī": "полностью свободный от недоумений ~ полностью свободен (short form, fleeting е)",
       "nibbattā": "возникнуть ~ возникли (past stem without -ну-)",
       "asamāpannassa": "не войти в медитативное достижение ~ не вошёл (suppletive past stem), as samāpannassa"}
EXC_SEG = {("2-537", "mukha"): "рот ~ «в области рта» (fleeting о)"}


def resolver_for(part):
    ru, pi = read_russian(part), read_pali(part)

    def resolve(bid, kw, kws):
        k = lc(kw)
        text = ru.get(bid, "")
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        if k in ov:
            return ov[k]
        lkws = {lc(x) for x in kws}
        # «Он принимает положения тела, живёт, оберегает себя …» (Iriyati vattati …), as ch. 7 2-358
        if k == "vattati" and "iriyati" in lkws:
            return "жить"
        # «Этот ум он очищает …, тщательно очищает, полностью очищает» (sodheti visodheti parisodheti)
        if k == "parisodheti" and "sodheti" in lkws:
            return "полностью очищать"
        if part == "12-jhanavibhango" and k in CH12:
            return CH12[k]
        if kw == "hetuko":
            return hetuko_value(pi.get(bid, ""))
        if k in CHOICES:
            for cand in CHOICES[k]:
                if present(cand, text):
                    return cand
            return CHOICES[k][0]
        return value(kw, kws, T)
    return resolve


def allowed(part):
    out = {(bid, kw): EXC[lc(kw)] for bid, kws in read_keywords(part) for kw in kws if lc(kw) in EXC}
    out.update({(bid, kw): EXC_SEG[(bid, kw)] for bid, kws in read_keywords(part) for kw in kws
                if (bid, kw) in EXC_SEG})
    return out


def dump(part, only_miss=False):
    ru, res = read_russian(part), resolver_for(part)
    for bid, kws in read_keywords(part):
        out = []
        for kw in kws:
            try:
                v = res(bid, kw, kws)
            except KeyError:
                v = "???"
            bad = (v == "???" or not (v == NDE or present(v, ru.get(bid, "")))) and lc(kw) not in EXC \
                and (bid, kw) not in EXC_SEG
            if bad or not only_miss:
                out.append(f"{kw}={v}" + (" !!" if bad else ""))
        if out:
            print(f"[{bid}] " + " | ".join(out))


if __name__ == "__main__":
    args = sys.argv[1:]
    if args[:1] == ["--dump"]:
        for p in [a for a in args[1:] if not a.startswith("--")]:
            dump(p, only_miss="--miss" in args)
        sys.exit()
    for p in (args or PARTS):
        build_part(p, resolver_for(p))
        verify(p, show=300, allowed=allowed(p))
