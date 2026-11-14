"""Write ru-zeroshot-terms.md from the two Russian builders (pi-1 Dhammasaṅgaṇī, plain zero-shot).

usage: python -I -X utf8 build_terms_ru.py
Every heading of AI_translation/pali/pi-1_split_chapters/*.md must have a Russian form in HEADINGS
(the script stops otherwise), so the parallel chapter agents share one set of headings.
"""
import pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import build_matika_ru as M  # noqa: E402
import build_ch2_01_sample_ru as C  # noqa: E402

ROOT = HERE.parents[3]
PALI_DIR = ROOT / "AI_translation" / "pali" / "pi-1_split_chapters"
OUT = HERE / "ru-zeroshot-terms.md"

VAR_ARUPA = M.V("s", "Sī., Syā.", "arūpajjhānāni")

# Pāli heading text (without #) = Russian heading text. Level is kept from the Pāli line.
HEADINGS = {
    # preamble
    "Abhidhammapiṭake": "В корзине Абхидхаммы",
    "Dhammasaṅgaṇīpāḷi": "Перечисление явлений",
    # chapter 1 (as built)
    "Mātikā": M.H_MATIKA.lstrip("# "),
    "Tikamātikā": M.H_TIKA.lstrip("# "),
    "Dukamātikā": M.H_DUKA.lstrip("# "),
    # chapter 2
    "Cittuppādakaṇḍaṃ": C.H_CH2.lstrip("# "),
    "Kāmāvacarakusalaṃ": C.H_KAMA_KUSALA.lstrip("# "),
    "Padabhājanī": C.H_PADA.lstrip("# "),
    "Koṭṭhāsavāro": "Раздел о составных частях",
    "Suññatavāro": "Раздел о пустоте",
    "Rūpāvacarakusalaṃ": "Благой ум, относящийся к миру форм",
    "Catukkanayo": "Четверичный метод",
    "Pañcakanayo": "Пятеричный метод",
    "Catasso paṭipadā": "Четыре способа практики",
    "Cattāri ārammaṇāni": "Четыре вида объектов",
    "Dve ārammaṇāni": "Два вида объектов",
    "Soḷasakkhattukaṃ": "Шестнадцатикратный разбор",
    "Aṭṭhakkhattukaṃ": "Восьмикратный разбор",
    "Idampi aṭṭhakkhattukaṃ": "Это тоже восьмикратный разбор",
    "Aparampi aṭṭhakkhattukaṃ": "Ещё один восьмикратный разбор",
    "Aṭṭhakasiṇaṃ soḷasakkhattukaṃ": "Восемь всеохватных объектов, шестнадцатикратный разбор",
    "Abhibhāyatanāni parittāni": "Ограниченные сферы преодоления",
    "Appamāṇāni": "Безмерные",
    "Tīṇi vimokkhāni soḷasakkhattukāni": "Три освобождения, шестнадцатикратный разбор",
    "Cattāri brahmavihārajhānāni soḷasakkhattukāni":
        "Четыре медитативных погружения божественных обителей, шестнадцатикратный разбор",
    "Asubhajhānaṃ soḷasakkhattukaṃ": "Медитативное погружение на непривлекательном, шестнадцатикратный разбор",
    "Arūpāvacarakusalaṃ": "Благой ум, относящийся к миру без форм",
    "Cattāri arūpajhānāni [arūpajjhānāni (sī. syā.)] soḷasakkhattukāni":
        "Четыре медитативных погружения мира без форм" + VAR_ARUPA + ", шестнадцатикратный разбор",
    "Tebhūmakakusalaṃ": "Благой ум трёх миров",
    "Lokuttarakusalaṃ": "Надмирский благой ум",
    "Suddhikapaṭipadā": "Простой способ практики",
    "Suññataṃ": "Пустота",
    "Suññatamūlakapaṭipadā": "Способ практики, основанный на пустоте",
    "Appaṇihitaṃ": "Свободное от устремлений",
    "Appaṇihitamūlakapaṭipadā": "Способ практики, основанный на свободе от устремлений",
    "Vīsati mahānayā": "Двадцать великих методов",
    "Adhipati": "Преобладание",
    "Dvādasa akusalāni": "Двенадцать видов неблагого ума",
    "Abyākatavipāko": "Этически неопределённые результаты действий",
    "Kusalavipākapañcaviññāṇāni": "Пять видов сознания, являющихся результатом благих действий",
    "Kusalavipākamanodhātu": "Элемент ума, являющийся результатом благих действий",
    "Kusalavipākamanoviññāṇadhātusomanassasahagatā":
        "Элемент умственного сознания, являющийся результатом благих действий и сопровождаемый радостью",
    "Kusalavipākamanoviññāṇadhātuupekkhāsahagatā":
        "Элемент умственного сознания, являющийся результатом благих действий и сопровождаемый невозмутимостью",
    "Aṭṭhamahāvipākā": "Восемь великих результатов действий",
    "Rūpāvacaravipākā": "Результаты действий, относящиеся к миру форм",
    "Arūpāvacaravipākā": "Результаты действий, относящиеся к миру без форм",
    "Lokuttaravipāka-paṭhamamaggavipākā": "Надмирские результаты действий: результаты первого пути",
    "Suddhikasuññataṃ": "Простая пустота",
    "Suññatapaṭipadā": "Способ практики с пустотой",
    "Suddhikaappaṇihitaṃ": "Простое свободное от устремлений",
    "Appaṇihitapaṭipadā": "Способ практики со свободой от устремлений",
    "Chandādhipateyyasuddhikapaṭipadā": "Простой способ практики при преобладании желания",
    "Chandādhipateyyasuddhikasuññatā": "Простая пустота при преобладании желания",
    "Dutiyādimaggavipāko": "Результаты второго и последующих путей",
    "Akusalavipākaabyākataṃ": "Этически неопределённое, являющееся результатом неблагих действий",
    "Akusalavipākapañcaviññāṇāni": "Пять видов сознания, являющихся результатом неблагих действий",
    "Akusalavipākamanodhātu": "Элемент ума, являющийся результатом неблагих действий",
    "Akusalavipākamanoviññāṇadhātu": "Элемент умственного сознания, являющийся результатом неблагих действий",
    "Ahetukakiriyāabyākataṃ": "Этически неопределённое функциональное без корней",
    "Kiriyāmanodhātu": "Функциональный элемент ума",
    "Kiriyāmanoviññāṇadhātusomanassasahagatā": "Функциональный элемент умственного сознания, сопровождаемый радостью",
    "Kiriyāmanoviññāṇadhātuupekkhāsahagatā":
        "Функциональный элемент умственного сознания, сопровождаемый невозмутимостью",
    "Sahetukakāmāvacarakiriyā": "Функциональный ум с корнями, относящийся к миру чувственных желаний",
    "Rūpāvacarakiriyā": "Функциональный ум, относящийся к миру форм",
    "Arūpāvacarakiriyā": "Функциональный ум, относящийся к миру без форм",
    # chapter 3
    "Rūpakaṇḍaṃ": "Раздел о материальной форме",
    "Uddeso": "Перечень",
    "Ekakaṃ": "Классификация по одному",
    "Dukaṃ": "Классификация по два",
    "Tikaṃ": "Классификация по три",
    "Catukkaṃ": "Классификация по четыре",
    "Pañcakaṃ": "Классификация по пять",
    "Chakkaṃ": "Классификация по шесть",
    "Sattakaṃ": "Классификация по семь",
    "Aṭṭhakaṃ": "Классификация по восемь",
    "Navakaṃ": "Классификация по девять",
    "Dasakaṃ": "Классификация по десять",
    "Ekādasakaṃ": "Классификация по одиннадцать",
    "Rūpavibhatti": "Классификация материальной формы",
    "Ekakaniddeso": "Разъяснение классификации по одному",
    "Dukaniddeso": "Разъяснение классификации по два",
    "Tikaniddeso": "Разъяснение классификации по три",
    "Upādābhājanīyaṃ": "Разбор производной материальной формы",
    # chapter 4
    "Nikkhepakaṇḍaṃ": "Раздел сводок",
    "Tikanikkhepaṃ": "Сводка троек",
    "Dukanikkhepaṃ": "Сводка пар",
    "Suttantikadukanikkhepaṃ": "Сводка пар из наставлений",
    # chapter 5
    "Aṭṭhakathākaṇḍaṃ": "Раздел разъяснений",
    "Tikaatthuddhāro": "Разъяснение смысла троек",
    "Dukaatthuddhāro": "Разъяснение смысла пар",
}
GROUP_PALI = {
    "1-M-2-1-0": "Hetugocchakaṃ", "1-M-2-2-0": "Cūḷantaradukaṃ", "1-M-2-3-0": "Āsavagocchakaṃ",
    "1-M-2-4-0": "Saṃyojanagocchakaṃ", "1-M-2-5-0": "Ganthagocchakaṃ", "1-M-2-6-0": "Oghagocchakaṃ",
    "1-M-2-7-0": "Yogagocchakaṃ", "1-M-2-8-0": "Nīvaraṇagocchakaṃ", "1-M-2-9-0": "Parāmāsagocchakaṃ",
    "1-M-2-10-0": "Mahantaradukaṃ", "1-M-2-11-0": "Upādānagocchakaṃ", "1-M-2-12-0": "Kilesagocchakaṃ",
    "1-M-2-13-0": "Piṭṭhidukaṃ", "1-M-2-14-0": "Suttantikadukamātikā",
}
for gid, pali in GROUP_PALI.items():
    HEADINGS[pali] = M.GROUPS[gid][0].lstrip("# ")

CLOSINGS = [  # closing lines (not headings) that later chapters will meet
    ("Tikamātikā.", M.END_TIKA),
    ("Abhidhammadukamātikā.", M.END_ABHI_DUKA),
    ("Mātikā niṭṭhitā.", M.END_MATIKA),
] + [(GROUP_PALI[g] + ".", M.GROUPS[g][1]) for g in GROUP_PALI] + [
    ("Padabhājanīyaṃ.", C.END_PADA),
    ("Paṭhamabhāṇavāro.", C.END_BHANA1),
    ("Dutiyabhāṇavāro. (proposed)", "Второй раздел для чтения вслух."),
    ("<X>kaṇḍaṃ niṭṭhitaṃ. (proposed)", "<раздел> завершён. e.g. Cittuppādakaṇḍaṃ niṭṭhitaṃ. = Раздел о возникновении ума завершён."),
    ("Nikkhepakaṇḍe dutiyabhāṇavāro. (proposed)", "Второй раздел для чтения вслух в разделе сводок."),
    ("Atthuddhāro niṭṭhito. (proposed)", "Разъяснение смысла завершено."),
    ("Abhidhammadukaṃ. (proposed)", "Пары Абхидхаммы."),
]

CORE = """\
dhamma (phenomenon; matrix items, ime dhammā) = явление; dhamma (the Teaching) = Учение
dhammārammaṇa = объект ума (pi-5 dhammāyatana = сфера объектов ума)
kusala / akusala / abyākata = благой / неблагой / этически неопределённый (never «нейтральный»)
vipāka / kiriya (abyākata) = результат действий / функциональный
citta / cittuppāda / cetasika = ум / возникновение ума / сопутствующий уму
mano (in the citta string) / mānasa / hadaya / paṇḍara = разум / умственная деятельность / сердце / чистота
viññāṇa / manoviññāṇadhātu / manodhātu = сознание / элемент умственного сознания / элемент ума
manāyatana / manindriya / cetosamphassa = сфера ума / способность ума / контакт ума
samaya (yasmiṃ … tasmiṃ samaye) = В то время, когда … , в это время …
kāmāvacara / rūpāvacara / arūpāvacara = относящийся к миру чувственных желаний / к миру форм / к миру без форм
lokiya / lokuttara = мирской / надмирский
somanassa / upekkhā = радость / невозмутимость; sukha (factor) = счастье; sukha / dukkha (feeling) = приятный / болезненный; sāta = отрада, отрадный
sahagata / sampayutta / vippayutta = сопровождаемый / связанный / не связанный
ñāṇa / vijjā / avijjā = знание / истинное знание / неведение
ārammaṇa / ārabbha = объект / имеющий объектом
rūpa / sadda / gandha / rasa / phoṭṭhabba (objects) = видимая форма / звук / запах / вкус / осязаемое
rūpa (matter) / rūpino / arūpino = материальная форма / материальные / нематериальные
khandha = совокупность (совокупность чувств, восприятия, формирующих факторов, сознания)
āyatana / dhātu / indriya / bala = сфера восприятия / элемент / способность / сила
phassa / vedanā / saññā / cetanā = контакт / чувство / восприятие / намерение
vitakka / vicāra / pīti / ekaggatā = направленная мысль / удержание мысли / восторг / однонаправленность (ума)
takka / saṅkappa / sammāsaṅkappa = мышление / помысел / правильный помысел (намерение is cetanā)
saddhā / vīriya / sati / samādhi / paññā = вера / усердие / осознанность / сосредоточение / мудрость
vāyāma / padhāna = усилие (vīriya = усердие only); paggāha = напряжение сил; chanda = желание
jīvitindriya = жизненная способность
hirī / ottappa; ahirika / anottappa = совестливость / страх перед дурным; бессовестность / отсутствие страха перед дурным
lobha / dosa / moha; alobha / adosa / amoha = жадность / злоба / заблуждение; отсутствие жадности / злобы / заблуждения
abhijjhā / byāpāda; anabhijjhā / abyāpāda = алчность / недоброжелательность; отсутствие алчности / недоброжелательности
sārāga = страсть; abyāpajja = отсутствие неприязни
hetu / kusalamūla = корень / благой корень
passaddhi / lahutā / mudutā / kammaññatā / pāguññatā / ujukatā = безмятежность / лёгкость / мягкость / работоспособность / натренированность / прямота
kāya- (kāyapassaddhi … kāyujukatā) = умственного тела; citta- = ума
sampajañña / asampajañña = ясное понимание / отсутствие ясного понимания
samatha / vipassanā / avikkhepa = успокоение / прозрение / отсутствие отвлечения
sammādiṭṭhi / sammāvāyāma / sammāsati / sammāsamādhi = правильное воззрение / правильное усилие / правильная осознанность / правильное сосредоточение
diṭṭhi = воззрение; sīla = нравственность; vipatti / sampadā / visuddhi = испорченность / безупречность / чистота
paṭiccasamuppanna / paṭiccasamuppāda = возникший в зависимости от условий / возникновение в зависимости от условий
upādiṇṇa / upādāniya / upādāna = охваченный цеплянием / служащий объектом цепляния / цепляние
āsava / saṃyojana / gantha / ogha / yoga / nīvaraṇa / parāmāsa / kilesa = влечение / оковы / узы / поток / ярмо / помеха / искажение / омрачение
sāsava / anāsava = подверженный влечениям / свободный от влечений; -niya = подверженный (оковам, узам, потокам, ярмам, помехам); parāmaṭṭha = затронутый искажениями
saṃkilesika / saṃkiliṭṭha = подверженный омрачению / омрачённый
dassana / bhāvanā (pahātabba) = видение истины / развитие ума (устраняемый)
sekkha / asekkha = обучающиеся / завершившие обучение
paritta / mahaggata / appamāṇa = ограниченный / возвышенный / безмерный
hīna / majjhima / paṇīta = низший / средний / высший
niyata / aniyata; micchatta / sammatta = предопределённый / непредопределённый; ложное / правильное
ajjhatta / bahiddhā (triads) = внутренний / внешний; ajjhattika / bāhira (pairs) = относящийся к внутреннему / к внешнему
sanidassana / sappaṭigha = видимый / способный к соударению
sappaccaya / saṅkhata / asaṅkhata = имеющий условия / обусловленный / необусловленный
upādā (rūpa) = производный
cittasaṃsaṭṭha / cittasamuṭṭhāna / cittasahabhū / cittānuparivattin = соединённый с умом / порождённый умом / сосуществующий с умом / следующий за умом
pariyāpanna = принадлежащий к кругам существования; niyyānika = ведущий к освобождению
sauttara / anuttara = над которыми есть высшее / нет высшего; saraṇa / araṇa = сопряжённый с борьбой / свободный от борьбы
adhivacana / nirutti / paññatti; -patha = наименование / выражение / обозначение; путь (как pi-5)
nāma / rūpa (pair 109) = умственное / материальная форма
samāpatti (meditative) = медитативное достижение; samāpatti (hirī string) = допускать в себе
nimitta = признак; yoniso = вдумчиво (pi-4); khaya / anuppāda = уничтожение / невозникновение
suttanta = наставление; gocchaka = группа; tika / duka = тройка / пара; bhāṇavāra = раздел для чтения вслух
uddesa = перечень; nikkhepa = сводка; atthuddhāra = разъяснение смысла; kaṇḍa = раздел
jhāna = медитативное погружение; paṭipadā = способ практики; adhipati = преобладание; appaṇihita = свободное от устремлений; suññata = пустота
Variant brackets = [вариант чтения (Sī.): …] when a word differs; [вариант написания (Syā.): …] for spelling only; sigla capitalised, comma-separated: (Sī., Syā.), (Sī., Ka.), (Ka.)
List markers (Ka) / (Kha) / (Ga) = (а) / (б) / (в)"""

CHOICES = """\
- mātikā = «матрица» (pi-3: «перечень»). Reason: pi-4/pi-5 use «перечень» for uddesa, and Rūpakaṇḍa has both Uddeso and Mātikā, so they must differ; «матрица» matches the user's English "matrix" (and mātikā/matrix both come from "mother"). Alternative if «матрица» feels too technical: «основной перечень».
- vicāra = «удержание мысли» (pi-5). Reason: pairs with vitakka «направленная мысль»; pi-3 «обдумывание» would clash with takka/cintā.
- saṅkhāra (aggregate) = «формирующие факторы» (pi-5): совокупность формирующих факторов.
- dosa = «злоба» (pi-5); adosa = «отсутствие злобы».
- asaṅkhata = «необусловленные» (pi-5). Consequence: saṅkhata = «обусловленные», and sappaccaya / appaccaya (^1-M2-7) = «имеющие условия» / «не имеющие условий» (pi-3 used «обусловленные» there).
- paṭiccasamuppāda = «возникновение в зависимости от условий» (pi-5); paṭiccasamuppanna = «возникшие в зависимости от условий».

Further departures from the earlier Russian termbases:
- dassana (pahātabba) = «видением истины» (pi-3 «прозрением»). Reason: vipassanā = «прозрение» (pi-4) in the same book; «истины» is a wording clarification, as in the Hindi.
- saṅkappa = «помысел» (pi-5 «намерение»). Reason: cetanā = «намерение» stands in the same list; «устремление» is kept free for appaṇihita.
- passaddhi = «безмятежность» (pi-5 «успокоение»). Reason: samatha = «успокоение» (pi-4) in the same list.
- vijjā = «истинное знание» (pi-4 «знание»). Reason: ñāṇa = «знание» (ñāṇasampayutta).
- diṭṭhi = «воззрение» everywhere (pi-4 «взгляды»): the pi-4 paññā string is reused verbatim except «правильные взгляды» -> «правильное воззрение».
- hirī = «совестливость» (style; pi-4 rails «совесть»); the pi-4 hirī/ottappa strings are reused verbatim.
- sukha as a feeling quality = «приятный» (triad 2: приятным чувством), sāta = «отрада/отрадный», sukha as a factor = «счастье»."""

NOTES = """\
- ^1-33: the Pāli answer ends with «?» («ayaṃ tasmiṃ samaye adoso hoti?»), unlike every parallel; kept as «?» (looks like a source slip).
- ^1-M2-6, -19, -25, -31, -37, -43, -49, -54, -74, -82 (б): the Pāli line is elliptical (ahetukāpi, anāsavāpi …); the Russian writes the item in full, as the approved pi-3 does.
- ^1-M2-126 (б): the variant «[paṭisandhāro ca (ka.)]» stands after «ca»; kept at the end of the item.
- ^1-M2-138 (а) «diṭṭhivisuddhi kho pana»: «kho pana» is a connective; rendered «Чистота воззрения.» like ^1-M2-137 (б), with «И …» on the (б) line, as in the Hindi.
- ^1-M1-9: «pahātabbahetukā» = «явления, чьи корни устраняются …» / «чьи корни не устраняются ни …, ни …» (user 2026-11-14; question form «имеют корни, которые устраняются …»). ^1-M2-85-86 (б): «не имеющие корней, устраняемых …» (also covers rootless states).
- ^1-1: «yaṃ yaṃ vā panārabbha» = «или что бы то ни было» (the object list closes there)."""


def heading_lines():
    seen, out = set(), []
    for f in sorted(PALI_DIR.glob("*.md")):
        for line in f.read_text(encoding="utf-8").splitlines():
            m = re.match(r"(#+) (.*?)\s*\^[0-9A-Za-z-]+\s*$", line)
            if m and m.group(2) not in seen:
                seen.add(m.group(2))
                out.append((f.name, m.group(1), m.group(2)))
    return out


def main():
    L = []
    w = L.append
    w("# pi-1 Dhammasaṅgaṇī: Russian plain zero-shot, binding terms")
    w("")
    w("Format: Pāli = Russian, one per line. Reuse every Russian string verbatim (copy or import it, do not retype it).")
    w("Generated by build_terms_ru.py from build_matika_ru.py and build_ch2_01_sample_ru.py; both modules hold the")
    w("strings as Python constants and can be imported by later chapter builders.")
    w("")
    w("## 1. Text frame and headings")
    w("")
    w("Namo tassa bhagavato arahato sammāsambuddhassa = Почтение Благословенному, Достойному, Полностью Пробуждённому Будде")
    missing = []
    cur = None
    for fname, hashes, pali in heading_lines():
        if fname != cur:
            cur = fname
            w(f"### {fname}")
        if pali not in HEADINGS:
            missing.append(pali)
            continue
        w(f"{hashes} {pali} = {hashes} {HEADINGS[pali]}")
    assert not missing, missing
    w("Same heading text at another level (e.g. ##### Kāmāvacarakusalaṃ in 2-02) = same Russian at that level.")
    w("")
    w("Closing lines:")
    for p, r in CLOSINGS:
        w(f"{p} = {r}")
    w("")
    w("## 2. Matrix items (exactly as in 1-matika.md; chapters 4 and 5 must reuse them verbatim)")
    w("")
    w("Line form: ^block-id (letter) Pāli = Russian matrix line ‖ Q = question frame ‖ A = answer frame.")
    w("Inside running sentences use the bare name (build_matika_ru.BARE): lower-case start, no variant bracket, no final «.».")
    w("Katame dhammā X? = «Какие явления <PRED>?» (build_matika_ru.QUESTION); ime dhammā X = «это <BARE>.» after the Pāli «–»")
    w("(build_matika_ru.ANSWER / ANSWER_BARE). Items ^1-M2-109 … 142 are nouns without a question frame.")
    w("")
    w("### Sets of three (triads)")
    for bid, letter, pali, ru in M.MATRIX_ITEMS_RU:
        if bid == "1-M2-1":
            w("")
            w("### Pairs")
        key = (bid, letter)
        tail = ""
        if M.PRED[key]:
            tail = f" ‖ Q = {M.QUESTION(key)} ‖ A = {C.DASH} {M.ANSWER(key)}"
        w(f"^{bid} ({letter}) {pali} = {ru}{tail}")
    w("")
    w("## 3. Recurring formulas (from the chapter-2 sample, ^1-1 to ^1-57)")
    w("")
    w("### 3a. Frames (X = factor name from 3c, nominative or instrumental; S = synonym string from 3b)")
    for p, r in C.FRAMES.items():
        w(f"{p} = {r}")
    w("ayaṃ / idaṃ / ime (in the answer) = это")
    w("")
    w("### 3b. Synonym strings (bare; the frame supplies «То, что в это время есть … , – это и есть X в это время.»)")
    for p, r in C.STRINGS.items():
        w(f"{p} = {r}")
    w(f"tajjāmanoviññāṇadhātusamphassajaṃ/-jā (before a string) = {C.TAJJA} (set off by commas after «в это время»)")
    w(f"vedanākkhandhassa saññākkhandhassa saṅkhārakkhandhassa = {C.G_KAYA}")
    w(f"viññāṇakkhandhassa = {C.G_CITTA}")
    w(f"tesaṃ arūpīnaṃ dhammānaṃ = {C.G_JIVITA}")
    w(f"paññā string + amoho kusalamūlaṃ = <paññā string>, {C.N['amoho']}, {C.ROOT}")
    w("Variant forms (first occurrences only, as in the Pāli): ^1-5, ^1-13, ^1-19, ^1-33, ^1-40; see S_CETANA_V, "
      "S_VIRIYA_V, S_JIVITA_V, S_ADOSA_V, S_PASSADDHI_V in the sample builder.")
    w("")
    w("### 3c. Factor names (nominative for «есть X» and «это и есть X»; instrumental for «является X»)")
    for k, (nom, ins) in C.NAMES_C.items():
        w(f"{k} = {nom} / {ins}")
    w("")
    w("## 4. Core terms")
    w("")
    L.extend(CORE.splitlines())
    w("")
    w("## 5. Term choices (the «rendered differently» list of russian-style.md) and other departures")
    w("")
    L.extend(CHOICES.splitlines())
    w("")
    w("## 6. Source notes (translated as written)")
    w("")
    L.extend(NOTES.splitlines())
    text = "\n".join(L) + "\n"
    assert "\n\n\n" not in text
    OUT.write_text(text, encoding="utf-8", newline="\n")
    print("wrote", OUT, "lines", len(L))


if __name__ == "__main__":
    main()
