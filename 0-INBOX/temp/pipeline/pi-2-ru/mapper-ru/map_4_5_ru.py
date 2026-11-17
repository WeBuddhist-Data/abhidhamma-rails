"""Build the Pāli->Russian keyword maps for pi-2 (Vibhaṅga) chapters 4-saccavibhango and 5-indriyavibhango.

usage: python -I -X utf8 map_4_5_ru.py [PART ...]     (writes <part>.mapped.md and verifies; default: both, in order)
       python -I -X utf8 map_4_5_ru.py --dump PART    (prints every keyword=value with a presence flag, no writing)

Resolution order per keyword: OVERRIDES[bid][kw]  ->  hetuko / CHOICES context rules  ->  T (this file:
map_2_3_ru.T (= KH + ch. 2/3, N-vidhena without «классификация») + the chapter 4/5 additions)  ->  pi-1 CH2 / MATRIX.
Conventions: ru-map-conventions-pi2.md (+ the pi-1 file), notes-map-2-3.md; new decisions: notes-map-4-5.md.
"""
import pathlib
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import map_2_3_ru as M23  # noqa: E402  (read-only: its table T and CHOICES)
from map_common_pi2_ru import (EXCEPTIONS, GAP, NDE, build_part, hetuko_value, lc,  # noqa: E402,F401
                               present, read_keywords, read_pali, read_russian, value, verify)

PARTS = ["4-saccavibhango", "5-indriyavibhango"]

# ---------------------------------------------------------------------------- table
T = dict(M23.T)
assert not any(v.startswith("классификация") for v in T.values())

T.update({
    # ---- ch. 2/3 values that do not fit chapters 4/5 (reset to the KH / pi-1 value)
    "ajjhattaṃ": "внутри себя", "rūpa": "материальная форма", "dhamma": "явление", "khandha": "совокупность",
    "uppajjitvā": "после возникновения", "yaṃ": "то что",
    # ---- truths (ch. 4)
    "sacca": "истина", "saccaṃ": "истина", "saccā": "истины", "saccāni": "истины", "saccānaṃ": "истины",
    "ariya": "благородный", "ariyā": "благородный", "ariyasaccaṃ": "благородная истина",
    "ariyasaccāni": "благородные истины", "ariyasaccānaṃ": "благородные истины",
    "dukkha": "страдание", "dukkhaṃ": "страдание", "dukkhasaccaṃ": "истина о страдании",
    "dukkhaṃ ariyasaccaṃ": "благородная истина о страдании",
    "samudaya": "возникновение", "samudayaṃ": "возникновение", "samudayo": "возникновение",
    "samudaye": "возникновение", "dukkhasamudayaṃ": "возникновение страдания",
    "dukkhasamudayo": "возникновение страдания", "dukkhasamudaye": "возникновение страдания",
    "dukkhanirodhaṃ": "прекращение страдания", "dukkhanirodho": "прекращение страдания",
    "dukkhanirodha": "прекращение страдания",
    # ---- suffering (2-190 … 2-202)
    "jātipi": "рождение", "jarāpi": "старение", "maraṇampi": "смерть", "upāyāsāpi": "отчаяние",
    "sokaparidevadukkhadomanassupāyāsāpi": "печаль стенания боль уныние и отчаяние",
    "sokaparidevadukkhadomanassupāyāsā": "печаль стенания боль уныние и отчаяние",
    "soka": "печаль", "parideva": "стенания", "upāyāsā": "отчаяние",
    "saṃkhittena": "короче говоря", "upādāna": "цепляние",
    "appiyehi": "неприятный", "piyehi": "приятный", "vippayogo": "разлука", "labhati": "получение",
    "picchaṃ": "желаемое",
    "jāti": "рождение", "sañjāti": "зарождение", "okkanti": "вхождение", "abhinibbatti": "появление",
    "pātubhāvo": "проявление", "paṭilābho": "обретение", "sattānaṃ": "существа", "nikāye": "класс",
    "nikāyā": "класс", "khandhānaṃ": "совокупности", "āyatanānaṃ": "сферы восприятия",
    "jarā": "старение", "jīraṇatā": "одряхление", "khaṇḍiccaṃ": "сломанные зубы", "pāliccaṃ": "седые волосы",
    "vali": "морщинистый", "taca": "кожа", "āyuno": "срок жизни", "indriyānaṃ": "способности",
    "paripāko": "изношенность",
    "cuti": "уход", "cavanatā": "выбывание", "bhedo": "распад", "antaradhānaṃ": "исчезновение",
    "maccu": "гибель", "maraṇaṃ": "смерть", "maraṇa": "смерть", "kālakiriyā": "кончина",
    "kaḷevarassa": "тело", "nikkhepo": "оставление", "jīvitindriyassupacchedo": "прекращение жизненной способности",
    "upacchedo": "прекращение", "jīvitindriya": "жизненная способность", "indriya": "способность",
    "ñāti": "родные", "byasanena": "несчастье", "phuṭṭhassa": "постигнуть",
    "byasanena vā phuṭṭhassa": "постигнуть несчастье", "bhoga": "имущество", "roga": "болезнь",
    "sīla": "нравственность", "diṭṭhi": "воззрение", "samannāgatassa": "охваченный",
    "dhammena": "явление",
    "soko": "печаль", "socanā": "горевание", "anto": "внутренний", "antoparisoko": "глубокая внутренняя печаль",
    "cetaso": "ум", "parijjhāyanā": "изнурение", "domanassaṃ": "уныние", "sallaṃ": "стрела",
    "ādevo": "плач", "paridevo": "стенания", "ādevanā": "оплакивание", "vācā": "речь", "palāpo": "болтовня",
    "vippalāpo": "бессвязная болтовня", "lālappo": "сетование",
    "kāyasamphassajā": "рождённый контактом тела", "cetosamphassajā": "рождённый контактом ума",
    "dukkhaṃ vedayitaṃ": "болезненное переживание", "dukkhā vedanā": "болезненное чувство",
    "āyāso": "удручённость", "upāyāso": "отчаяние",
    "yassa": "кто-то", "aniṭṭhā": "нежеланный", "akantā": "немилый", "amanāpā": "неприятный",
    "iṭṭhā": "желанный", "kantā": "милый", "manāpā": "приятный",
    "ye vā panassa": "или же" + GAP + "те кто", "kāmā": "желать",
    "anattha": "вред", "ahita": "неблаго", "aphāsuka": "неудобство",
    "ayogakkhemakāmā": "желать ему лишиться безопасности",
    "phāsuka": "удобство", "yogakkhema": "безопасность",
    "samāgamo": "общение", "samodhānaṃ": "соединение", "missībhāvo": "смешение",
    "asamāgamo": "отсутствие общения", "asamodhānaṃ": "несоединение", "amissībhāvo": "несмешение",
    "mātā": "мать", "pitā": "отец", "bhātā": "брат", "bhaginī": "сестра", "mittā": "друзья",
    "amaccā": "сотоварищи", "ñātī": "родственники", "sālohitā": "кровные родные",
    "dukkho": "страдание",
    "icchā": "желание", "icchāya": "желание", "uppajjati": "возникать", "pattabbaṃ": "достичь",
    "byādhi": "болезнь",
    "rūpupādānakkhandho": "совокупность материальной формы служащая объектом цепляния",
    "vedanupādānakkhandho": "совокупность чувств служащая объектом цепляния",
    "saññupādānakkhandho": "совокупность восприятия служащая объектом цепляния",
    "saṅkhārupādānakkhandho": "совокупность формирующих факторов служащая объектом цепляния",
    "viññāṇupādānakkhandho": "совокупность сознания служащая объектом цепляния",
    # ---- origin / cessation (2-203, 2-204)
    "taṇhā": "жажда", "ponobhavikā": "ведущий к новому существованию", "nandi": "наслаждение",
    "rāga": "страсть", "ābhinandinī": "находящий радость",
    "kāmataṇhā": "чувственная жажда", "bhavataṇhā": "жажда существования",
    "vibhavataṇhā": "жажда несуществования", "phoṭṭhabbataṇhā": "жажда осязаемого",
    "kāma": "чувственный", "bhava": "существование", "vibhava": "несуществование",
    "taṇhā uppajjamānā uppajjati": "жажда возникая возникать", "nivisati": "укореняться",
    "taṇhā pahīyamānā pahīyati": "жажда устраняясь устраняться", "pahīyati": "устраняться",
    "nirujjhati": "прекращаться",
    "piyarūpaṃ": "привлекательный", "sātarūpaṃ": "отрадный",
    "cakkhusamphasso": "контакт глаза", "sotasamphasso": "контакт уха", "ghānasamphasso": "контакт носа",
    "jivhāsamphasso": "контакт языка", "kāyasamphasso": "контакт тела", "manosamphasso": "контакт ума",
    "manosamphassajā": "рождённый контактом ума",
    "cakkhusamphassajā vedanā": "рождённое контактом глаза чувство",
    "sañcetanā": "намерение", "vitakko": "направленная мысль",
    "asesa": "без остатка", "virāga": "угасание", "cāgo": "отказ", "paṭinissaggo": "оставление",
    "mutti": "освобождение", "anālayo": "отсутствие привязанности",
    # ---- path, Suttanta (2-205; pi-1 ^1-160 … ^1-165, ^1-1377)
    "aṭṭhaṅgiko": "восьмичастный", "aṭṭhaṅgiko maggo": "восьмичастный путь", "maggo": "путь",
    "pañcaṅgiko": "пятичастный", "pañcaṅgiko maggo": "пятичастный путь",
    "ñāṇaṃ": "знание", "nekkhamma": "отречение", "abyāpāda": "отсутствие недоброжелательности",
    "avihiṃsā": "отсутствие жестокости",
    "veramaṇī": "уклонение", "musāvādā": "ложь", "musā": "ложь", "pisuṇāya": "сеющий раздор",
    "pharusāya": "грубый", "samphappalāpā": "пустая болтовня",
    "pāṇātipātā": "убийство живых существ", "ātipātā": "убийство", "ādānā": "взятие",
    "micchācārā": "неправильное поведение", "kāmesu": "чувственные удовольствия",
    "sāvako": "ученик", "micchā": "неправильный", "pahāya": "устранить", "ājīvo": "образ жизни",
    "kappeti": "поддерживать",
    "bhikkhu": "монах", "pāpakānaṃ": "дурной", "anuppādāya": "невозникновение", "chandaṃ": "желание",
    "janeti": "порождать", "chandaṃ janeti": "порождать желание", "vāyamati": "прилагать усилие",
    "ārabhati": "пробуждать", "paggaṇhāti": "напрягать", "padahati": "прилагать старания",
    "uppannānaṃ": "возникший", "pahānāya": "устранение", "uppādāya": "возникновение",
    "ṭhitiyā": "сохранение", "asammosāya": "неутрата", "vepullāya": "обширность", "pāripūriyā": "завершённость",
    "kāye": "тело", "kāyānupassī": "созерцающий тело", "ānupassī": "созерцающий",
    "kāye kāyānupassī": "в теле созерцающий тело", "kāyānupassī viharati": "пребывать" + GAP + "созерцающий тело",
    "ātāpī": "ревностный", "sampajāno": "ясно понимающий", "satimā": "осознанный", "vineyya": "устранить",
    "abhijjhā": "алчность", "vedanāsu": "чувства", "dhammesu": "явления",
    "vivicceva": "полностью уединиться", "vivicca": "уединиться",
    "vivicceva kāmehi": "полностью уединиться от чувственных удовольствий", "kāmehi": "чувственные удовольствия",
    "viveka": "уединение", "vivekajaṃ": "рождённый уединением", "vitakkaṃ": "направленная мысль",
    "savitakkaṃ savicāraṃ": "с направленной мыслью и удержанием мысли", "pītisukhaṃ": "восторг и счастье",
    "jhānaṃ": "медитативное погружение", "upasampajja": "входить",
    "upasampajja viharati": "входить" + GAP + "пребывать", "viharati": "пребывать",
    "vūpasamā": "затихание",
    "vitakkavicārānaṃ vūpasamā": "затихание направленной мысли и удержания мысли",
    "sampasādanaṃ": "ясность", "ekodibhāvaṃ": "единение", "samādhi": "сосредоточение",
    "virāgā": "угасание", "upekkhako": "невозмутимый", "sukhañca": "счастье", "paṭisaṃvedeti": "испытывать",
    "ācikkhanti": "говорить", "sukhavihārī": "пребывающий в счастье",
    "sukhassa": "приятное", "dukkhassa": "болезненное", "somanassa": "радость", "atthaṅgamā": "исчезновение",
    "pārisuddhiṃ": "чистота", "catutthaṃ jhānaṃ": "четвёртое медитативное погружение",
    "akusalānaṃ": "неблагой", "akusalānaṃ dhammānaṃ": "неблагие явления", "kusalānaṃ": "благой",
    "kusalānaṃ dhammānaṃ": "благие явления",
    # ---- path, Abhidhamma (2-206 … 2-214; pi-1 ^1-277, ^1-297 … ^1-304)
    "pahānaṃ": "устранение", "taṇhāya pahānaṃ": "устранение жажды", "taṇhāya": "жажда",
    "diṭṭhigatānaṃ": "приверженность воззрениям",
    "diṭṭhigatānaṃ pahānāya": "устранение приверженности воззрениям",
    "uttaraṃ": "надмирский", "bhāveti": "развивать", "jhānaṃ bhāveti": "развивать" + GAP + "медитативное погружение",
    "apacayagāmiṃ": "ведущий" + GAP + "к убыванию", "pattiyā": "достижение", "bhūmiyā": "ступень",
    "dukkhapaṭipadaṃ": "трудный способ практики", "dandhābhiññaṃ": "медленное высшее знание",
    "ābhiññaṃ": "высшее знание",
    "dukkhapaṭipadaṃ dandhābhiññaṃ": "трудный способ практики и медленное высшее знание",
    "samaye": "в это время",
    "sampayuttā": "связанный", "kilesā": "омрачения", "avasesā": "остальной",
    "avasesā ca kilesā": "остальные омрачения", "avasesā dhammā": "остальные явления",
    "avasesā ca akusalā": "остальные неблагие", "dhammā": "явления",
    "akusalā dhammā": "неблагие явления", "kusalā dhammā": "благие явления",
    "sāsavā kusalā dhammā": "подверженные влечениям благие явления",
    "kusalamūlāni": "благие корни", "mūlāni": "корни", "sāsavāni": "подверженный влечениям",
    "kusalamūlāni sāsavāni": "благие корни подверженные влечениям",
    "mūlāni sāsavāni": "корни подверженные влечениям",
    "kusalākusalānaṃ": "благие и неблагие", "dhammānaṃ": "явления",
    "kusalākusalānaṃ dhammānaṃ vipākā": "результаты благих и неблагих явлений",
    "sāsavā kusalākusalānaṃ dhammānaṃ": "подверженные влечениям" + GAP + "благие и неблагие явления",
    "kammavipākā": "результат действий", "neva kusalā nākusalā": "ни благие ни неблагие",
    "kiriyā": "функциональный", "rūpaṃ": "материальная форма",
    "ārati": "отстранение", "virati": "воздержание", "paṭivirati": "полное воздержание",
    "akaraṇaṃ": "несовершение", "akiriyā": "неделание", "anajjhāpatti": "невпадение в проступок", "velā": "граница",
    "anatikkamo": "непереступание", "setu": "мост", "ghāto": "разрушение",
    "vacī": "речевой", "vacīduccaritehi": "дурное речевое поведение", "duccaritehi": "дурное" + GAP + "поведение",
    "kāya": "телесный", "kāyaduccaritehi": "дурное телесное поведение",
    "maggaṅgaṃ": "фактор пути", "sambojjhaṅgo": "фактор пробуждения",
    "dhammavicayasambojjhaṅgo": "фактор пробуждения исследования явлений",
    "vīriyasambojjhaṅgo": "фактор пробуждения усердия", "satisambojjhaṅgo": "фактор пробуждения осознанности",
    "samādhisambojjhaṅgo": "фактор пробуждения сосредоточения",
    "amoho": "отсутствие заблуждения", "vicayo": "исследование", "dhammavicayo": "исследование явлений",
    "pajānanā": "понимание", "paññā": "мудрость", "takko": "мышление", "saṅkappo": "помысел",
    "ārambho": "приложение", "vāyāmo": "усилие", "anussati": "припоминание", "sati": "осознанность",
    "cittassa": "ум", "ṭhiti": "устойчивость", "saṇṭhiti": "собранность", "phasso": "контакт",
    "avikkhepo": "отсутствие отвлечения",
    # ---- pañhāpucchaka (2-216 … 2-218), as ch. 3 2-186 … 2-188
    "āsekkhā": "относящийся к завершившим обучение", "sekkhaṃ": "относящийся к обучающимся",
    "saṃkilesikaṃ": "подверженный омрачению", "mahaggataṃ": "возвышенный",
    "mahaggatārammaṇaṃ": "с возвышенным объектом", "bahiddhārammaṇaṃ": "с внешним объектом",
    "niyataṃ": "предопределённый", "hīnaṃ": "низший", "ajjhattārammaṇaṃ": "с внутренним объектом",
    "anidassanaappaṭighā": "невидимый и не способный к соударению", "gāmi": "ведущий",
    "parittārammaṇaṃ": "с ограниченным объектом", "appamāṇārammaṇaṃ": "с безмерным объектом",
    "majjhimaṃ": "средний", "majjhimā": "средний", "ārammaṇaṃ": "объект",
    "ajjhattabahiddhārammaṇaṃ": "с внутренним и внешним объектом",
    "appaṭighā": "не способный к соударению", "sanidassana": "видимый", "sanidassanaṃ": "видимый",
    "upādānaṃ": "цепляние", "saraṇaṃ": "сопряжённый с борьбой", "saṃkiliṭṭhaṃ": "омрачённый",
    "kileso": "омрачение", "vippayuttaṃ": "не связанный", "cetasikaṃ": "душевный",
    "rūpāvacaraṃ": "относящийся к миру форм", "arūpāvacaraṃ": "относящийся к миру без форм",
    "ogho": "поток", "yogo": "ярмо", "arūpāni": "нематериальный", "niyyānikaṃ": "ведущий к освобождению",
    "upādānañceva upādānasampayuttañca": "являющийся цеплянием и связанный с цепляниями",
    "kileso ceva kilesasampayuttañca": "являющийся омрачением и связанный с омрачениями",
    "saṃyojanañceva saṃyojanasampayuttañca": "являющийся оковами и связанный с оковами",
    "nīvaraṇañceva nīvaraṇasampayuttañca": "являющийся помехой и связанный с помехами",
    "hetu ceva hetusampayuttañca": "являющийся корнем и связанный с корнями",
    "āsavo ceva āsavasampayuttañca": "являющийся влечением и связанный с влечениями",
    "gantho ceva ganthasampayuttañca": "являющийся узами и связанный с узами",
    "asaṅkhataṃ": "необусловленный", "saccā araṇā": "истины свободные от борьбы",
    "saccāni appaṭighā": "истины не способные к соударению",
    # ---- faculties (ch. 5)
    "bāvīsatindriyāni": "двадцать две способности", "bāvīsatīnaṃ": "двадцать два",
    "bāvīsatīnaṃ indriyānaṃ": "двадцать две способности", "indriyāni": "способности",
    "indriyā": "способности", "indriyā siyā": "способности" + GAP + "иногда",
    "indriyā hetū": "способности" + GAP + "корни", "indriyā sappaṭighā": "способности способные к соударению",
    "cakkhundriyaṃ": "способность глаза", "manindriyaṃ": "способность ума",
    "saddhindriyaṃ": "способность веры", "vīriyindriyaṃ": "способность усердия",
    "satindriyaṃ": "способность осознанности", "samādhindriyaṃ": "способность сосредоточения",
    "paññindriyaṃ": "способность мудрости",
    "anaññātaññassāmītindriyaṃ": "способность познания непознанного",
    "aññindriyaṃ": "способность окончательного знания",
    "aññātāvindriyaṃ": "способность обладателя окончательного знания",
    "rūpajīvitindriyaṃ": "материальная жизненная способность",
    "arūpajīvitindriyaṃ": "нематериальная жизненная способность",
    "dvindriyā": "две способности", "tīṇindriyā": "три способности", "cattārindriyā": "четыре способности",
    "pañcindriyā": "пять способностей", "sattindriyā": "семь способностей", "aṭṭhindriyā": "восемь способностей",
    "navindriyā": "девять способностей", "dasindriyā": "десять способностей",
    "ekādasindriyā": "одиннадцать способностей", "dvādasindriyā": "двенадцать способностей",
    "terasindriyā": "тринадцать способностей", "cuddasindriyā": "четырнадцать способностей",
    "pannarasindriyā": "пятнадцать способностей", "soḷasindriyā": "шестнадцать способностей",
    "sattarasindriyā": "семнадцать способностей", "aṭṭhārasindriyā": "восемнадцать способностей",
    "ekavīsatindriyā": "двадцать одна способность",
    "kāyindriyaṃ": "способность тела", "cakkhu": "глаз", "kāyo": "тело", "pasādo": "чувствительность",
    "gāmopeso": "это" + GAP + "деревня",
    "sahetukaṃ": "имеющий корни", "phassasampayuttaṃ": "связанный с контактом",
    "itthiyā": "женщина", "itthi": "женственность", "itthattaṃ": "женственность", "liṅgaṃ": "внешность",
    "nimittaṃ": "признак", "ākappo": "манера", "purisassa": "мужчина", "purisa": "мужественность",
    "purisattaṃ": "мужественность",
    "rūpīnaṃ": "материальный", "āyu": "срок жизни", "yapanā": "поддержание", "yāpanā": "продление",
    "iriyanā": "движение", "vattanā": "течение", "pālanā": "сбережение", "jīvitaṃ": "жизнь",
    "kāyikaṃ": "телесный", "sātaṃ": "отрадный", "sukhaṃ": "удовольствие", "sukhā vedanā": "приятное чувство",
    "saddhā": "вера", "saddahanā": "доверие", "okappanā": "уверенность", "abhippasādo": "глубокая убеждённость",
    "balaṃ": "сила", "nikkamo": "порыв", "parakkamo": "напор", "uyyāmo": "старание", "ussāho": "рвение",
    "thāmo": "стойкость", "asithilaparakkamatā": "неослабевающий напор", "anikkhitta": NDE,
    "chanda": "желание", "dhura": "бремя", "sampaggāho": "крепкое удержание",
    "paṭissati": "воспоминание", "dhāraṇatā": "способность удерживать в памяти",
    "apilāpanatā": "отсутствие поверхностности", "asammussanatā": "отсутствие забывчивости",
    "avaṭṭhiti": "стабильность", "avisāhāro": "отсутствие рассеяния",
    "avisāhaṭamānasatā": "нерассеянность ума", "samatho": "успокоение", "sammā": "правильный",
    "ñātānaṃ": "познанный", "viditānaṃ": "узнанный", "sacchikatānaṃ": "постигнутый непосредственно",
    "sacchikiriyāya": "непосредственное постижение", "aṅgaṃ": "фактор", "magga": "путь",
    "anidassanā": "невидимый", "saṅkhatā": "обусловленный", "no": "не",
    "kileso ceva kilesasampayuttañcā": "являющийся омрачением и связанный с омрачениями",
    "saṃyojanañceva saṃyojanasampayuttañcā": "являющийся оковами и связанный с оковами",
    "nīvaraṇañceva nīvaraṇasampayuttañcā": "являющийся помехой и связанный с помехами",
    "āsavo ceva āsavasampayuttañcā": "являющийся влечением и связанный с влечениями",
    "gantho ceva ganthasampayutta": "являющийся узами и связанный с узами",
})

# ---------------------------------------------------------------------------- per-segment overrides
# Pañhāpucchaka: Tika (2-217, 2-223) as 2-152 / 2-187 (the text quotes the participle «сопровождаемое»);
# Duka (2-218, 2-224) as 2-153 / 2-188 (finite «сопровождается» only).
_DUKA = dict(M23._DUKA)
_DUKA.pop("rūpā")
_DUKA.pop("cetasikaṃ")
_DUKA.update({"rūpaṃ": "материальный", "rūpā": "материальный", "cetasikaṃ": "сопутствующий уму",
              "ajjhattaṃ": "внутренний", "vitakkaṃ": "направленная мысль", "vicāraṃ": "удержание мысли"})
# Suttanta frames: rūpaṃ only inside piyarūpaṃ / sātarūpaṃ (no word of its own); dhammā = объекты ума («объекты
# ума в мире»); Yaṃ = что («Что в мире является привлекательным …»)
_CRAVING = {"rūpaṃ": NDE, "dhammā": "объекты ума", "Yaṃ": "что", "dukkha": "страдание",
            "sahagatā": "сопровождаемый", "vedanā": "чувство", "saññā": "восприятие"}
# feeling strings (2-196, 2-197 = ch. 5 2-220 bodies): dukkhaṃ = боль (телесная / душевная боль)
_PAIN = {"dukkhaṃ": "боль", "dukkhā": "болезненный", "vedanā": "чувство"}
OVERRIDES = {
    "2-4-0": {"Sacca": "истина"},
    "2-4-1-1-0": {"Dukkha": "страдание", "Dukkhasaccaṃ": "истина о страдании"},
    "2-190": {"dukkha": "боль"},
    "2-193": {"indriya": "способность"},
    "2-194": {"dukkha": "болезненный"},
    "2-195": {"dukkha": "болезненный"},
    "2-196": dict(_PAIN),
    "2-197": dict(_PAIN),
    "2-198": {"dukkha": "болезненный"},
    "2-201": {"dukkha": "боль", "Jarā": "старение"},
    "2-202": {"dukkhā": "страдание"},
    "2-203": dict(_CRAVING),
    "2-204": dict(_CRAVING),
    "2-205": {"cittaṃ": "ум", "sukhaṃ": "счастье", "dukkha": "страдание"},
    # hetukaṃ: only pahātabbahetukaṃ («чьи корни») and maggahetukaṃ here, no sa-/ahetukaṃ (as hetukā)
    "2-217": {"pahātabbā": "устраняться", "hetukaṃ": "чьи корни", "āsekkhā": "относящийся" + GAP + "к завершившим обучение"},
    "2-218": dict(_DUKA),
    "2-220": {"dukkhaṃ": "боль", "dukkhā vedanā": "болезненное чувство", "vedanā": "чувство",
              "sahagataṃ": "сопровождаемый", "cetasikaṃ": "душевный", "indriyaṃ": "способность"},
    "2-223": {"pahātabbā": "устраняться"},
    "2-224": dict(_DUKA),
}

CHOICES = dict(M23.CHOICES)
CHOICES["upādāniyaṃ"] = ["служащий объектом цепляния", "служащий его объектом"]

# presence-check exceptions (value correct; inflection outside present()'s tolerance)
EXC = {**M23.EXC,
       "phuṭṭhassa": "постигнуть ~ постигло (verb stem alternation)",
       "byasanena vā phuṭṭhassa": "постигнуть несчастье ~ постигло несчастье (verb stem alternation)",
       "yassa": "кто-то ~ кого-то (pronoun declension)",
       "ācikkhanti": "говорить ~ говорят (verb stem alternation), = pi-1 ^1-163",
       "musā": "ложь ~ лжи (fleeting vowel)", "musāvādā": "ложь ~ лжи (fleeting vowel)"}


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


def dump(part):
    ru, res = read_russian(part), resolver_for(part)
    for bid, kws in read_keywords(part):
        out = []
        for kw in kws:
            try:
                v = res(bid, kw, kws)
            except KeyError:
                v = "???"
            flag = "" if (v == NDE or present(v, ru.get(bid, ""))) else " !!"
            out.append(f"{kw}={v}{flag}")
        print(f"[{bid}] " + " | ".join(out))


if __name__ == "__main__":
    args = sys.argv[1:]
    if args[:1] == ["--dump"]:
        for p in args[1:]:
            dump(p)
        sys.exit()
    for p in (args or PARTS):
        build_part(p, resolver_for(p))
        verify(p, show=300, allowed=allowed(p))
