# Notes: pi-1 part 2-04 (Russian plain zero-shot: twelve unwholesome minds; results of the wholesome)

Builder: build_2-04_ru.py (imports build_matika_ru.py and build_ch2_01_sample_ru.py; sample names, strings and frames reused unchanged; the Q/A, jīvita and hirī frames are asserted byte-identical to the sample's). Mirrors ref/en_build_2-04.py + ref/en_const_2_03_2_04.py. The kusala half of ^1-499 … ^1-504 reuses the 2-02 phrases (copied from build_2-01_2-02_ru.py; the builder prints any drift against that module).
Format: Pāli = Russian, one per line.

## New factor names (nominative / instrumental)
micchādiṭṭhi = ложное воззрение / ложным воззрением (micchatta = ложное, terms file; sammā- = правильный)
micchāsaṅkappo = ложный помысел / ложным помыслом
micchāvāyāmo = ложное усилие / ложным усилием
micchāsamādhi = ложное сосредоточение / ложным сосредоточением
ahirikabalaṃ = сила бессовестности / силой бессовестности
anottappabalaṃ = сила отсутствия страха перед дурным / силой отсутствия страха перед дурным
ahirikaṃ = бессовестность; anottappaṃ = отсутствие страха перед дурным (matrix ^1-M2-115)
lobho = жадность; moho = заблуждение; abhijjhā = алчность; doso = злоба; byāpādo = недоброжелательность
vicikicchā = колебание; uddhaccaṃ = беспокойство (russian-style.md pairs)
upekkhā = невозмутимость; upekkhindriyaṃ = способность невозмутимости
dukkhaṃ (factor) = боль / болью; domanassindriyaṃ = способность уныния (domanassa = уныние, pi-3/4/5)
sukhindriyaṃ = способность удовольствия (pi-3 sukhindriya = удовольствие; pairs with 2-05 dukkhindriyaṃ = способность боли)
saṅkhārakkhandho = совокупность формирующих факторов / совокупностью формирующих факторов

## New synonym strings
akusalamūlaṃ = неблагой корень; abyākatamūlaṃ = этически неопределённый корень
lobho lubbhanā lubbhitattaṃ sārāgo sārajjanā sārajjitattaṃ abhijjhā lobho akusalamūlaṃ = жадность, проявление жадности, состояние жадности, страсть, проявление страсти, состояние страсти, алчность, жадность, неблагой корень
doso dussanā dussitattaṃ byāpatti byāpajjanā byāpajjitattaṃ virodho paṭivirodho caṇḍikkaṃ asuropo anattamanatā cittassa = злоба, проявление злобы, состояние злобы, недоброжелательность, проявление недоброжелательности, состояние недоброжелательности, вражда, противодействие, свирепость, грубость, недовольство ума (pi-4 ^4-45 with dosa = злоба)
aññāṇaṃ adassanaṃ … avijjālaṅgī moho akusalamūlaṃ = незнание, отсутствие видения, отсутствие постижения, отсутствие понимания, непробуждённость, отсутствие проникновения, неохватывание, отсутствие углубления, отсутствие рассмотрения, отсутствие обдумывания, неспособность видеть воочию, тупость, глупость, отсутствие ясного понимания, заблуждение, сильное заблуждение, полное заблуждение, неведение, поток неведения, ярмо неведения, скрытая склонность к неведению, одержимость неведением, засов неведения, заблуждение, неблагой корень (pi-4 ^4-60 verbatim)
diṭṭhi diṭṭhigataṃ diṭṭhigahanaṃ diṭṭhikantāro diṭṭhivisūkāyikaṃ diṭṭhivipphanditaṃ diṭṭhisaṃyojanaṃ gāho patiṭṭhāho abhiniveso parāmāso kummaggo micchāpatho micchattaṃ titthāyatanaṃ vipariyāsaggāho = воззрение, приверженность воззрениям, дебри воззрений, пустыня воззрений, изворотливость воззрений, метания воззрений, оковы воззрений, хватка, закрепление, упрямство, искажение, кривая дорога, ложный путь, ложность, прибежище сектантских учений, превратная хватка (pi-4 ^4-62 with diṭṭhi = воззрение; departures: parāmāso = искажение (core term), so diṭṭhivisūkāyikaṃ = изворотливость воззрений (pi-4 «искажение взглядов»); abhiniveso = упрямство (pi-4 «приверженность», which is diṭṭhigataṃ here); patiṭṭhāho = закрепление)
kaṅkhā kaṅkhāyanā kaṅkhāyitattaṃ vimati vicikicchā dveḷhakaṃ dvedhāpatho saṃsayo anekaṃsaggāho āsappanā parisappanā apariyogāhanā thambhitattaṃ cittassa manovilekho = сомнение, проявление сомнения, состояние сомнения, растерянность, колебание, двойственность, распутье, неуверенность, неспособность прийти к определённому выводу, шатание, нерешительность, отсутствие углубления, оцепенение ума, терзание ума (kaṅkhā сомнение / vicikicchā колебание kept apart; apariyogāhanā as in the moha string)
cittassa uddhaccaṃ avūpasamo cetaso vikkhepo bhantattaṃ cittassa = беспокойство ума, отсутствие затихания, отвлечение ума, взбудораженность ума (vūpasama = затихание, as 2-01/2-02 «с затиханием»; vikkhepa as avikkhepa = отсутствие отвлечения)
na hirīyati hiriyitabbena na hirīyati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā = человек не стыдится того, чего следует стыдиться, не стыдится допускать в себе дурные неблагие явления (pi-4 ^4-53 verbatim; frame as hirī)
na ottappati ottappitabbena na ottappati … = человек не боится того, чего следует бояться, не боится допускать в себе дурные неблагие явления (pi-4 ^4-54 verbatim)
cetasikaṃ neva sātaṃ nāsātaṃ cetosamphassajaṃ adukkhamasukhaṃ vedayitaṃ cetosamphassajā adukkhamasukhā vedanā = душевное состояние, которое ни отрадно, ни неотрадно, рождённое контактом ума переживание, которое ни болезненно, ни приятно, рождённое контактом ума чувство, которое ни болезненно, ни приятно (taken from build_2-01_2-02_ru.py)
cetasikaṃ asātaṃ cetasikaṃ dukkhaṃ cetosamphassajaṃ asātaṃ dukkhaṃ vedayitaṃ cetosamphassajā asātā dukkhā vedanā = душевная безотрадность, душевная боль, рождённое контактом ума безотрадное и болезненное переживание, рождённое контактом ума безотрадное и болезненное чувство (pattern of build_2-05_ru.py S_KAYA_DUKKHA)
kāyikaṃ sātaṃ kāyikaṃ sukhaṃ kāyasamphassajaṃ sātaṃ sukhaṃ vedayitaṃ kāyasamphassajā sātā sukhā vedanā = телесная отрада, телесное удовольствие, рождённое контактом тела отрадное и приятное переживание, рождённое контактом тела отрадное и приятное чувство
takko … cetaso abhiniropanā (+ micchāsaṅkappo) = the sample string without «, правильный помысел» (+ «, ложный помысел»); likewise the samādhi string + «ложное сосредоточение», the vīriya string + «ложное усилие»
cittassa ṭhiti (abbreviated string) = устойчивость ума
tajjācakkhuviññāṇadhātusamphassajaṃ/-jā = рождённое контактом соответствующего элемента зрительного сознания (likewise … элемента осязательного сознания, … элемента ума)
… viññāṇakkhandho tajjācakkhuviññāṇadhātu (end of the citta string) = … совокупность сознания, соответствующий элемент зрительного сознания (likewise осязательного сознания, ума)

## Opening clauses
Katame dhammā akusalā / abyākatā? = M.QUESTION: Какие явления являются неблагими / этически неопределёнными?
Yasmiṃ samaye akusalaṃ cittaṃ uppannaṃ hoti = В то время, когда возникает неблагой ум
somanassasahagataṃ diṭṭhigatasampayuttaṃ / diṭṭhigatavippayuttaṃ = сопровождаемый радостью и связанный / не связанный с приверженностью воззрениям (diṭṭhigata = приверженность воззрениям, pi-5)
upekkhāsahagataṃ = сопровождаемый невозмутимостью; domanassasahagataṃ paṭighasampayuttaṃ = сопровождаемый унынием и связанный с неприязнью (paṭigha = неприязнь, pi-5; paṭighasaññā = восприятие соударения)
vicikicchāsampayuttaṃ / uddhaccasampayuttaṃ = связанный с колебанием / связанный с беспокойством
sasaṅkhārena = с побуждением (as 2-01/2-02, 2-05)
rūpārammaṇaṃ vā…pe… dhammārammaṇaṃ vā yaṃ yaṃ vā panārabbha = имеющий объектом видимую форму… или объект ума, или что бы то ни было (…phoṭṭhabbārammaṇā vā = … или осязаемое, …; rūpārammaṇaṃ vā…pe… yaṃ yaṃ = имеющий объектом видимую форму… или что бы то ни было)
kāmāvacarassa kusalassa kammassa katattā upacitattā vipākaṃ cakkhuviññāṇaṃ uppannaṃ hoti = (В то время, когда) вследствие того, что благое действие, относящееся к миру чувственных желаний, было совершено и накоплено, возникает зрительное сознание, являющееся его результатом (shape of build_2-05_ru.py AKUS_KAMMA)
vipākā manodhātu / manoviññāṇadhātu uppannā hoti = возникает элемент ума / элемент умственного сознания, являющийся его результатом
cakkhu- / sota- / ghāna- / jivhā- / kāyaviññāṇaṃ = зрительное / слуховое / обонятельное / вкусовое / осязательное сознание (pi-3/4/5)
upekkhāsahagataṃ rūpārammaṇaṃ (after a viññāṇa) = сопровождаемое невозмутимостью, имеющее объектом видимую форму (звук, запах, вкус); sukhasahagataṃ phoṭṭhabbārammaṇaṃ = сопровождаемое счастьем, имеющее объектом осязаемое
Tasseva rūpāvacarassa (arūpāvacarassa) kusalassa kammassa katattā upacitattā vipākaṃ X = Когда вследствие того, что это же благое действие, относящееся к миру форм (без форм), было совершено и накоплено, человек в качестве его результата X (pattern of build_2-05_ru.py VIPAKA_OPEN)
rūpūpapattiyā / arūpūpapattiyā maggaṃ bhāveti and the absorption phrases = as build_2-01_2-02_ru.py (INTROS, PH, «и пребывает в нём» closing the qualifier chain):
  rūpūpapattiyā maggaṃ bhāveti = В то время, когда человек, развивая путь к рождению в мире форм, (… без форм)
  vivicceva kāmehi = полностью уединившись от чувственных удовольствий; vitakkavicārānaṃ vūpasamā = с затиханием направленной мысли и удержания мысли; sukhassa ca pahānā = с устранением приятного
  paṭhamaṃ jhānaṃ upasampajja viharati pathavīkasiṇaṃ = входит в первое медитативное погружение, на всеохватном объекте земли, и пребывает в нём
  sabbaso rūpasaññānaṃ samatikkamā paṭighasaññānaṃ atthaṅgamā nānattasaññānaṃ amanasikārā = полностью преодолев восприятия материальной формы, с исчезновением восприятий соударения, не уделяя внимания восприятиям разнообразия
  sabbaso X samatikkamma = полностью преодолев X; X-saññāsahagataṃ = с восприятием X (сферы бесконечного пространства / бесконечного сознания / отсутствия чего-либо / ни восприятия, ни невосприятия)
phasso hoti…pe… avikkhepo hoti…pe… ime dhammā abyākatā…pe… alobho abyākatamūlaṃ…pe… = есть контакт… есть отсутствие отвлечения… это этически неопределённые явления… отсутствие жадности, этически неопределённый корень…

## Frames shared with 2-01 / 2-03 / 2-05
Tasmiṃ kho pana samaye … = И в это время …
pañcindriyāni / cattāri indriyāni / tīṇindriyāni honti = есть пять / четыре / три способности
pañcaṅgikaṃ / caturaṅgikaṃ jhānaṃ hoti = есть пятичастное / четырёхчастное медитативное погружение (2-01 COUNTED)
caturaṅgiko / tivaṅgiko / duvaṅgiko maggo hoti = есть четырёхчастный / трёхчастный / двухчастный путь
cattāri / tīṇi balāni honti = есть четыре / три силы; dve hetū honti / eko hetu hoti = есть два корня / есть один корень
ekā cakkhuviññāṇadhātu / kāyaviññāṇadhātu / manodhātu / manoviññāṇadhātu hoti = есть один элемент зрительного сознания / осязательного сознания / ума / умственного сознания
ekaṃ dhammāyatanaṃ hoti, ekā dhammadhātu hoti = есть одна сфера объектов ума, есть один элемент объектов ума
koṭṭhāsa line: «…; или же любые другие …, какие есть в это время, кроме совокупности чувств, кроме совокупности восприятия, кроме совокупности сознания, – это и есть совокупность формирующих факторов в это время…»

## Headings and closing lines (headings from the terms file)
Dvādasa akusalacittāni. = Двенадцать видов неблагого ума.
Kusalavipākāni pañcaviññāṇāni. = Пять видов сознания, являющихся результатом благих действий.
Kusalavipākā manodhātu. = Элемент ума, являющийся результатом благих действий.
Kusalavipākā manoviññāṇadhātu somanassasahagatā. = Элемент умственного сознания, являющийся результатом благих действий и сопровождаемый радостью.
Kusalavipākā upekkhāsahagatā manoviññāṇadhātu. = Элемент умственного сознания, являющийся результатом благих действий и сопровождаемый невозмутимостью.
Aṭṭhamahāvipākā. = Восемь великих результатов действий.
Rūpāvacaravipākā. / Arūpāvacaravipākā. = Результаты действий, относящиеся к миру форм. / … к миру без форм.

## Source notes (translated as written)
- ^1-377: the answer ends with «hoti?» instead of «hoti.»; the Russian ends with «?».
- ^1-473: the question ends with «hoti.» instead of «hoti?»; the Russian question ends with «.».
- ^1-381: «patiṭṭhāho [paṭiggāho (sī. syā.)]»; pi-4 ^4-62 reads paṭiggāho in the main text. patiṭṭhāho may be a slip; rendered as written («закрепление»), the variant bracket keeps paṭiggāho.
- ^1-429: stray space before «…pe…» («hoti …pe… ye vā pana»); rendered like the other lines.
- ^1-433: the feeling of eye-consciousness is defined with the mental string (cetasikaṃ … cetosamphassajaṃ …), while ^1-445 (body-consciousness) has the bodily string; kept as written.
- ^1-501 to ^1-504: the immaterial absorptions lack «upekkhāsahagataṃ»; nothing added.
