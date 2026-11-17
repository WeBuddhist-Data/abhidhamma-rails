# pi-2 Russian zero-shot, chapter 18 (Dhammahadayavibhaṅga): new terms and formulas

Builder: build_18_ru.py (imports build_ch1_sample_ru as S; asserts reused strings against pi-1 / pi-5 / pi-2 ch1-17; after building it checks that every Pāli sentence also found in a sentence-aligned line of pi-2 ch1-17 or pi-1 gets byte-identical Russian: 124 sentences). Helpers: lookup_18.py (Pāli regex -> aligned Russian in pi-1..5 and pi-2 ch1-17), probe_18.py (sentence-level coverage probe).
Format: Pāli = Russian, one per line. [pi-1] / [pi-5] / [chN] = reused; [new] = settled here.

## Reused
Pañhāpucchaka predicates (kusala, vedanā, vipāka, upādinna, vitakka, rūpa, lokiya, sārammaṇa) = ch1-5 Pañhāpucchaka wording [ch1-5]
Names of the 12 bases, 18 elements, 4 truths, 22 faculties = ch2 / ch3 / ch4 / ch5 [ch2-5]
Bhūmantaradassanavāra (kāmāvacara … apariyāpanna definitions) = pi-1 ^1-1287 … ^1-1294 without the pi-1 variant brackets; the pariyāpanna list written out in full [pi-1]
Tayo abyākatahetū definition = pi-1 ^1-1068 [pi-1]; vipākahetu = «отсутствие жадности как корень, являющийся результатом действий» [pi-1]
kāmāvacara / rūpāvacara / arūpāvacara = относящийся к миру чувственных желаний / форм / без форм; pariyāpanna / apariyāpanna = принадлежащий / не принадлежащий к кругам существования [pi-1]
God names = pi-5 10-dutiyavaggo (same list): богов Четырёх Великих Царей, Тридцати трёх, Ямы, Тушиты, богов, наслаждающихся творением, богов, властвующих над творениями других, свиты Брахмы, богов-советников Брахмы, Великих Брахм, ограниченного / безмерного / струящегося сияния, ограниченного / безмерного / сплошного великолепия, великого плода, богов, не отпадающих от своего мира, невозмутимых богов, богов прекрасного облика, богов ясного видения, высочайших богов, богов, достигших сферы бесконечного пространства (… сознания, … отсутствия чего-либо, … ни восприятия, ни невосприятия) [pi-5; the last three as ch17 «достигает сферы …»]
asaññasatta = без восприятия (богов без восприятия; heading «Существа без восприятия») [pi-5]
opapātika = рождающийся самопроизвольно [pi-1]; peta = дух умершего; asura = асур; tiracchānagata = животное; nerayika = обитатель ада [pi-5]
khattiya- / brāhmaṇa- / gahapatimahāsāla = богатые знатные правители / богатые брахманы / богатые домохозяева [pi-4]
āyuppamāṇa = продолжительность жизни; kappa = эпоха; kappassa tatiyo bhāgo = треть эпохи [pi-5]
uposatha = постный день [pi-5]; sīlaṃ samādiyitvā = взяв на себя нравственность [pi-5]; abhiññā = высшее знание [ch10]

## New
kāmadhātu / rūpadhātu / arūpadhātu (realm, here mostly locative) = мир чувственных желаний / мир форм / мир без форм (в мире …) [pi-5]; ch17 has «элемент мира форм» inside the compound rūpadhātupaṭisaṃyutta; the element rūpadhātu stays «элемент видимых форм»
apariyāpanne (realm) = в том, что не принадлежит к кругам существования; heading Apariyāpannaṃ = Не принадлежащее к кругам существования
X-dhātupariyāpanna = принадлежит к миру чувственных желаний / форм / без форм; na … = не принадлежит …
Kati khandhā, kati āyatanāni, … kati cittāni? = Сколько совокупностей, сколько сфер восприятия, сколько элементов, сколько истин, сколько способностей, сколько корней, сколько видов питания, сколько видов контакта, сколько чувств, сколько восприятий, сколько намерений, сколько видов ума?
phassā (counted) = виды контакта; vedanā / saññā / cetanā (counted) = чувства / восприятия / намерения; cittāni / cittā (the seven) = виды ума; ekaṃ cittaṃ = один вид ума; āhārā = виды питания [pi-1]
Tattha katame X? … – ime vuccanti "X" = Что такое здесь X? … – это называется «X (instr.)» [ch1 frame]
cakkhusamphasso … manodhātusamphasso, manoviññāṇadhātusamphasso = контакт глаза … контакт элемента ума, контакт элемента умственного сознания; manoviññāṇadhātusamphassajā vedanā = рождённое контактом элемента умственного сознания чувство
upapattikkhaṇe = в момент перерождения; pātubhavanti / pātubhavati = появляются / появляется; sabbesaṃ / kassaci / kassa = у всех / у некоторых / у кого; etesaṃ imāni = у них … эти
kassaci ahetukā pātubhavanti = у некоторых появление происходит без корней; avasesānaṃ sattānaṃ ahetukā pātubhavanti = у остальных существ появление происходит без корней
kāmāvacarā devā = боги, относящиеся к миру чувственных желаний; paṭhamakappikā manussā = люди первой эпохи; gabbhaseyyakā sattā = существа, рождающиеся из утробы; paripuṇṇāyatana = обладающий полным набором сфер восприятия; jaccandha / jaccabadhira / jaccandhabadhira = слепой / глухой / слепой и глухой от рождения; sahetuka ñāṇasampayutta / ñāṇavippayutta = имеющий корни и связанный / не связанный со знанием; ahetuka = не имеющий корней; napuṃsaka = бесполый; ṭhapetvā = кроме
X vā Y vā (faculty lists) = X или Y
abhiññeyya / pariññeyya / pahātabba / bhāvetabba / sacchikātabba = следует постичь высшим знанием / следует полностью понять / следует устранить / следует развивать / следует осуществить; na … = не следует устранять / развивать / осуществлять (subject in the accusative)
sārammaṇārammaṇa / anārammaṇārammaṇa = имеет объектом то, что имеет объект / … то, что не имеет объекта
diṭṭha / suta / muta / viññāta (predicate) = увиден / услышан / ощущён / познан (short forms; «но» before a positive item that follows a negative one: «не увидены, не услышаны, не ощущены, но познаны»)
na vattabbā …tipi (no dash, no quotes in this chapter's Pāli) = нельзя определить ни как «…», ни как «…», ни как «…» (the ch1-5 form without the dash)
devā: sammutidevā / upapattidevā / visuddhidevā = боги по общему признанию / боги по рождению / боги по чистоте; rājāno, deviyo, kumārā = цари, царицы и царевичи; arahanto vuccanti = так называют архатов
X-ānaṃ devānaṃ sahabyataṃ upapajjanti = перерождаются в обществе X; appekacce = некоторые
dānaṃ datvā, sīlaṃ samādiyitvā, uposathakammaṃ katvā = (те, кто) дал подаяние, взял на себя нравственность, соблюдал постный день
jhānaṃ parittaṃ / majjhimaṃ / paṇītaṃ bhāvetvā = развил медитативное погружение в ограниченной / в средней / в высшей мере
ārammaṇa- / manasikāra- / chanda- / paṇidhi- / adhimokkha- / abhinīhāra- / paññānānattatā = вследствие различия объектов, внимания, желания, устремления, решимости, направленности, мудрости
kittakaṃ āyuppamāṇaṃ? = Какова продолжительность жизни …?; rattindivo = сутки; tāya rattiyā tiṃsa rattiyo māso = Тридцать таких ночей составляют месяц; dvādasamāsiyo saṃvaccharo = Двенадцать таких месяцев составляют год; dibba = божественный; manussānaṃ gaṇanāya kittakaṃ hoti? = Сколько это по человеческому счёту?
Human-count numbers computed into Russian numerals (as the English rails text does): navuti vassasatasahassāni = девять миллионов лет; … nava ca vassakoṭisatāni ekavīsañca vassakoṭiyo saṭṭhi ca vassasatasahassāni = девять миллиардов двести шестнадцать миллионов лет; verse total 1200 koṭi + 28 koṭi + 50 lakh = двенадцать миллиардов, двести восемьдесят миллионов и пять миллионов (sum checked in the builder)
Section headings: Sabbasaṅgāhikavāro = Раздел, охватывающий всё; Uppattānuppattivāro = Раздел о том, что возникает и что не возникает; Pariyāpannāpariyāpannavāro = Раздел о принадлежащем и не принадлежащем; Dhammadassanavāro = Раздел о проявлении явлений; Bhūmantaradassanavāro = Раздел о различии уровней; Uppādakakammaāyuppamāṇavāro = Раздел о порождающих действиях и продолжительности жизни; Abhiññeyyādivāro = Раздел о том, что следует постичь высшим знанием, и прочем; Sārammaṇānārammaṇavāro = Раздел об имеющем объект и не имеющем объекта; Diṭṭhasutādidassanavāro = Раздел об увиденном, услышанном и прочем; Tikādidassanavāro = Раздел о тройках и прочем; Kusala- / Vedanā- / Vipāka- / Upādinna- / Vitakkattikaṃ = Тройка о благом / о чувстве / о результате действий / об охваченном цеплянием / о направленной мысли; Rūpa- / Lokiyadukaṃ = Пара о материальном / о мирском
Book colophon: Vibhaṅgapakaraṇaṃ niṭṭhitaṃ. = Книга «Подробный разбор» завершена. [pi-1 pattern]

## Variant brackets
[kabaḷiṃkāro āhāro (sī. syā.)], [sammatidevā (syā.)], [cātummahārājike (sī. syā.)], [rattidivo (ka.) a. ni. 3.71] = вариант написания (the reference kept after «;»)
[keci (syā.)], [avasesā sattā (?)], [appaṃ vā bhiyyo vā (syā. ka.) dī. ni. 2.7], [eko kappo (syā.)], [chapi te (syā.)], [bhavaggaṃ vāpi (syā.)], [puna gacchanti (syā.)] = вариант чтения

## Pāli slips and as-written readings (all reported)
Rendered as meant (spelling / punctuation only): ^2-992 "imā vuccatti" (= vuccanti); ^2-992 "Cakkhusamphasso sotasamphasso" (comma); ^2-1000 "siyā kāmadhātu pariyāpanno" (space); ^2-1012 "kāyindriyaṃ manindriyaṃ" (comma); ^2-1014 "katame cattāro āhārā pātubhavanti." rendered as a question; ^2-1035 "siyā sārammaṇārammaṇo siyā …", ^2-1040 "siyā vipākā siyā …", ^2-1042 "siyā avitakkaavicāro siyā na vattabbo" (commas); ^2-1039 "siyā dukkhamasukhāya" (= adukkhamasukhāya); ^2-1039 "sampayuttoti pi"; ^2-1042 "pañca cittā avitakkaavicārā manodhātu …" (a comma); ^2-1043 "satta cetanā satta cittā" (ellipsis).
As written: ^2-994 "Ime vuccanti rūpadhātuyā aṭṭha hetū." unquoted; ^2-993 "kati āyatanā" (= āyatanāni); the stray digit in ^2-1041 "anupādinnupādāniyo 4." kept («… служит его объектом 4.»); ^2-1009 / ^2-1010 the comma between "tiracchānagatānaṃ" and "nerayikānaṃ" is missing in several lines (rendered as a list); in ^2-1004 "Tīṇi saccāni na arūpadhātupariyāpannāni." and "Dukkhasaccaṃ siyā …" stand on two lines (kept).
Unsure: «Раздел о проявлении явлений» (Dhammadassana); «у некоторых появление происходит без корней» for "kassaci ahetukā pātubhavanti"; abhinīhāra «направленность»; «боги по общему признанию» (sammutideva); dibba «божественный».
Review: akaniṭṭha / ākāsānañcāyatanūpaga: pi-1 (reused verbatim in ^2-1020) has «богов Аканиттха», «богов, рождённых в сфере …»; the god list (^2-1021 … ^2-1028) follows pi-5 «высочайших богов», «богов, достигших сферы …». abhiññeyya «следует постичь высшим знанием» (pi-5 «то, что следует познать»).
