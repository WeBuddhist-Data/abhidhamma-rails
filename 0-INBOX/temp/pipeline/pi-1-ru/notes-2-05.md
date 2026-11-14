# Notes: pi-1 part 2-05 (Russian plain zero-shot, ^1-1-8-0 … ^1-582: lokuttara vipāka, akusala vipāka, kiriyā)

Builder: build_2-05_ru.py (imports build_matika_ru.py and build_ch2_01_sample_ru.py; mirrors the English/Hindi 2-05 builders: each line is split at «…pe…» and every chunk is translated by fixed rules, so the same Pāli chunk always gives the same Russian). 99 segments.
Strings shared with other parts were copied from their builders as they stood on 2026-11-14 (marked [2-03] / [2-04] / [2-02] in the builder).
Format: Pāli = Russian, one per line.

## Frames
Katame dhammā abyākatā? = Какие явления являются этически неопределёнными? (M.QUESTION)
ime dhammā abyākatā = это этически неопределённые явления (M.ANSWER)
ye vā pana … – ime dhammā abyākatā = или же любые другие нематериальные явления, возникшие в зависимости от условий, какие есть в это время, – это этически неопределённые явления (C.YEVAPANA)
…pe…. (line end) = ….
Tasmiṃ kho pana samaye cattāro khandhā honti, dvāyatanāni honti, dve dhātuyo honti, tayo āhārā honti, tīṇindriyāni (pañcindriyāni) honti, eko phasso hoti = И в это время есть четыре совокупности, есть две сферы восприятия, есть два элемента, есть три вида питания, есть три способности (пять способностей), есть один контакт [as 2-03]
ekā kāyaviññāṇadhātu / manodhātu / manoviññāṇadhātu hoti = есть один элемент осязательного сознания / элемент ума / элемент умственного сознания
ekaṃ dhammāyatanaṃ hoti, ekā dhammadhātu hoti = есть одна сфера объектов ума, есть один элемент объектов ума [as 2-03]
Katamo tasmiṃ samaye saṅkhārakkhandho hoti? = Что в это время является совокупностью формирующих факторов?
ṭhapetvā vedanākkhandhaṃ ṭhapetvā saññākkhandhaṃ ṭhapetvā viññāṇakkhandhaṃ = кроме совокупности чувств, кроме совокупности восприятия, кроме совокупности сознания [as 2-03; 2-04 has «за исключением …»]
alobho / adoso / amoho abyākatamūlaṃ = отсутствие жадности / злобы / заблуждения, этически неопределённый корень

## New factor names (nominative / instrumental)
dukkhaṃ = боль / болью
dukkhindriyaṃ = способность боли / способностью боли
upekkhā = невозмутимость / невозмутимостью
upekkhindriyaṃ = способность невозмутимости / способностью невозмутимости
aññindriyaṃ = способность окончательного знания / способностью окончательного знания (pi-5, as 2-03)
aññātāvindriyaṃ = способность обладателя окончательного знания / способностью обладателя окончательного знания (pi-5 aññātāvī)
saṅkhārakkhandho = совокупность формирующих факторов / совокупностью формирующих факторов

## Strings
kāyikaṃ asātaṃ kāyikaṃ dukkhaṃ kāyasamphassajaṃ asātaṃ dukkhaṃ vedayitaṃ kāyasamphassajā asātā dukkhā vedanā = телесная безотрадность, телесная боль, рождённое контактом тела безотрадное и болезненное переживание, рождённое контактом тела безотрадное и болезненное чувство (asāta = безотрадный, as 2-04)
tajjākāyaviññāṇadhātusamphassajaṃ = рождённое контактом соответствующего элемента осязательного сознания (as 2-04)
samādhi / vīriya string without sammāsamādhi / sammāvāyāmo (functional mind) = the sample strings without «, правильное сосредоточение» / «, правильное усилие»
Yā tesaṃ aññātāvīnaṃ dhammānaṃ aññā S … = То, что у этих явлений, обладающих окончательным знанием, есть окончательное знание, S, …
aññā (before the paññā string) = окончательное знание
dhammavicayasambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ = фактор пробуждения исследования явлений, фактор пути, принадлежащее к пути (as 2-03)

## World-transcending results (kusala clause byte-identical with build_2-03_ru.py)
Yasmiṃ samaye lokuttaraṃ jhānaṃ bhāveti niyyānikaṃ apacayagāmiṃ = В то время, когда человек развивает надмирское медитативное погружение, ведущее к освобождению и ведущее к убыванию
diṭṭhigatānaṃ pahānāya paṭhamāya bhūmiyā pattiyā = для устранения приверженности воззрениям, для достижения первой ступени (stages 2–4 as 2-03)
<stage> vivicceva kāmehi = <stage> и, отстранившись от чувственных удовольствий; <stage> vitakkavicārānaṃ vūpasamā = <stage> и с успокоением направленной мысли и удержания мысли
X jhānaṃ upasampajja viharati = достигает X медитативного погружения и пребывает в нём; bare X jhānaṃ = X медитативного погружения (первого … пятого)
qualifiers of the absorption (after «и пребывает в нём») = «, в погружении с …» / «, в погружении, свободном от устремлений» / «, в пустом погружении»; later chunks of the same run carry the qualifiers alone
dukkhapaṭipadaṃ dandhābhiññaṃ (…) = с болезненным способом практики и медленным высшим знанием (быстрым; с приятным способом практики …) (as 2-03)
suññataṃ / animittaṃ / appaṇihitaṃ = пустом / не имеющем признаков / свободном от устремлений (animitta new: pi-5 «не имеющий признаков»)
chanda- / vīriya- / citta- / vīmaṃsādhipateyyaṃ = при преобладании желания / усердия / ума / исследования (as 2-03)
…nti kusalaṃ / …nti vipāko = … (благое) / … (результат)
Tasseva lokuttarassa kusalassa jhānassa katattā bhāvitattā vipākaṃ vivicceva kāmehi = Когда в результате того, что было совершено и развито это же надмирское благое медитативное погружение, человек, отстранившись от чувственных удовольствий
lokuttaraṃ X bhāveti (twenty methods) = развивает надмирский путь / надмирскую основу осознанности / надмирское правильное усилие / надмирскую основу сверхспособностей / … / надмирский ум, ведущий к освобождению и ведущий к убыванию (list as 2-03)

## Unwholesome results and functional minds
akusalassa kammassa katattā upacitattā vipākaṃ/vipākā X uppannaṃ/uppannā hoti = В то время, когда вследствие того, что было совершено и накоплено неблагое действие, возникает X как его результат (word order of the 2-04 kusala-vipāka frame)
cakkhu- / sota- / ghāna- / jivhā- / kāyaviññāṇaṃ = зрительное / слуховое / обонятельное / вкусовое / осязательное сознание (pi-3/4/5)
upekkhāsahagataṃ / dukkhasahagataṃ (a viññāṇa) = сопровождаемое невозмутимостью / сопровождаемое болью; with «элемент»: сопровождаемый …
rūpārammaṇā vā…pe… phoṭṭhabbārammaṇā (dhammārammaṇā) vā yaṃ yaṃ vā panārabbha = имеющий объектом видимую форму… или осязаемое (или объект ума), или что бы то ни было
kiriyā (kiriyaṃ) neva kusalā nākusalā na ca kammavipākā = функциональный (функциональное), не являющийся (не являющееся) ни благим, ни неблагим, ни результатом действий
sasaṅkhārena = с побуждением (as 2-01/2-04); ñāṇavippayutta = не связанный со знанием
rūpāvacaraṃ / arūpāvacaraṃ jhānaṃ bhāveti = человек развивает медитативное погружение, относящееся к миру форм / к миру без форм
diṭṭhadhammasukhavihāraṃ = для приятного пребывания в этой жизни (pi-5 «приятное пребывание в этой жизни»)
pathavīkasiṇaṃ = на всеохватном объекте земли (as 2-02; here «в погружении на всеохватном объекте земли»)
arūpa formulas = as build_2-01_2-02_ru.py (полностью преодолев …, с исчезновением восприятий соударения, не уделяя внимания восприятиям разнообразия, с восприятием сферы …); sukhassa ca pahānā = и с устранением приятного

## Headings and closing lines
Headings: terms file verbatim (Suddhikapaṭipadā, Vīsati mahānayā from the 2-03 list). Closing lines = heading text + «.», except:
Paṭhamamaggavipāko. = Результат первого пути.
Lokuttaravipāko. = Надмирский результат действий.
Vipākā abyākatā. = Этически неопределённые результаты действий. (= terms #### Abyākatavipāko)
Ahetukā kiriyā abyākatā. = Этически неопределённое функциональное без корней. (= heading Ahetukakiriyāabyākataṃ)
Kiriyā abyākatā. = Этически неопределённое функциональное.
Cittuppādakaṇḍaṃ niṭṭhitaṃ. = Раздел о возникновении ума завершён. (terms file)

## For the consistency pass (the parallel parts differ among themselves)
- vivicceva kāmehi: 2-03 «отстранившись от чувственных удовольствий» (used here) vs 2-02 «полностью уединившись от чувственных удовольствий» vs 2-04 «отстранившись от чувственных желаний».
- vitakkavicārānaṃ vūpasamā: 2-03 «с успокоением …» (used here, also in ^1-578) vs 2-02 «с затиханием …»; note samatha = «успокоение».
- upasampajja viharati: 2-03 «достигает … и пребывает в нём» (used here) vs 2-02 «входит в … и пребывает в нём»; 2-04 uses impersonal plural «развивают … достигают».
- vīmaṃsā = «исследование» (2-03, used here) coincides with vicaya = «исследование» in the paññā string.
- sammappadhāna = «правильное усилие» (2-03) coincides with sammāvāyāma.

## Source notes (translated as written)
- ^1-528: «ime dhammā kusalā tasseva …» has no full stop; rendered with a semicolon and lower case.
- ^1-553: «kāmarā gabyāpādānaṃ» split word; read as kāmarāgabyāpādānaṃ (spelling slip).
- ^1-553: the wholesome clause of the second to fourth paths lists aññindriyaṃ, the result clause aññātāvindriyaṃ (fits only the fourth path); kept.
- ^1-544 stray comma «viharati, animittaṃ»; ^1-574 missing comma «samādhindriyaṃ hoti manindriyaṃ»; ^1-579 no comma before «tasmiṃ samaye»: normal Russian punctuation.
- ^1-576: the Pāli has «…pe… ime dhammā abyākatā…pe… alobho abyākatamūlaṃ…» (two answers) and lists only alobho/adoso as roots (no amoho, although ñāṇasampayutta minds are included); kept.
