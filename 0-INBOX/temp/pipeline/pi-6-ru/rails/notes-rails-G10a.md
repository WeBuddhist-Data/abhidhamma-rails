# notes-rails-G10a: Indriyayamaka (10-01 … 10-04) frames

Format: Pāli = Russian, one per line. Builder: build_rails_G10a_ru.py (importlib.import_module(
"build_rails_G10a_ru"); importing writes nothing). Built on G2 (paṇṇatti / pavatti frames), G3 (sa-/a-X-ka
persons, mūlaka labels, «…pe…» questions, place lists) and G45 (intro_ru: person / time / place intros).
For G10b: FACULTIES, faculty_cases(), BARE, ATTR, GENDER, attrs_ru(), person_unit / UNITS_G10a (already
prepended to G45.UNITS on import), MOM_G10a, core(), translate_sentence(), translate_line(), render().

## The 22 faculties (termbase = pi-2 Indriyavibhaṅga; nom / gen / ins)

cakkhundriyaṃ = способность глаза / способности глаза / способностью глаза
sotindriyaṃ = способность уха / способности уха / способностью уха
ghānindriyaṃ = способность носа / способности носа / способностью носа
jivhindriyaṃ = способность языка / способности языка / способностью языка
kāyindriyaṃ = способность тела / способности тела / способностью тела
manindriyaṃ = способность ума / способности ума / способностью ума
itthindriyaṃ = способность женственности / способности женственности / способностью женственности
purisindriyaṃ = способность мужественности / способности мужественности / способностью мужественности
jīvitindriyaṃ = жизненная способность / жизненной способности / жизненной способностью (acc. жизненную способность)
sukhindriyaṃ = способность удовольствия / способности удовольствия / способностью удовольствия
dukkhindriyaṃ = способность боли / способности боли / способностью боли
somanassindriyaṃ = способность радости / способности радости / способностью радости
domanassindriyaṃ = способность уныния / способности уныния / способностью уныния
upekkhindriyaṃ = способность невозмутимости / способности невозмутимости / способностью невозмутимости
saddhindriyaṃ = способность веры / способности веры / способностью веры
vīriyindriyaṃ = способность усердия / способности усердия / способностью усердия
satindriyaṃ = способность осознанности / способности осознанности / способностью осознанности
samādhindriyaṃ = способность сосредоточения / способности сосредоточения / способностью сосредоточения
paññindriyaṃ = способность мудрости / способности мудрости / способностью мудрости
anaññātaññassāmītindriyaṃ = способность познания непознанного / способности познания непознанного / способностью познания непознанного
aññindriyaṃ = способность окончательного знания / способности окончательного знания / способностью окончательного знания
aññātāvindriyaṃ = способность обладателя окончательного знания / способности обладателя окончательного знания / способностью обладателя окончательного знания

## Bare words (term-analysis questions)

cakkhu = глаз / глаза / глазом
sotaṃ = ухо / уха / ухом
ghānaṃ = нос / носа / носом
jivhā = язык / языка / языком
kāyo = тело / тела / телом
mano = ум / ума / умом
itthī = женщина / женщины / женщиной
puriso = мужчина / мужчины / мужчиной
jīvitaṃ = жизнь / жизни / жизнью
sukhaṃ = удовольствие / удовольствия / удовольствием
dukkhaṃ = боль / боли / болью
somanassaṃ = радость / радости / радостью
domanassaṃ = уныние / уныния / унынием
upekkhā = невозмутимость / невозмутимости / невозмутимостью
saddhā = вера / веры / верой
vīriyaṃ = усердие / усердия / усердием
sati = осознанность / осознанности / осознанностью
samādhi = сосредоточение / сосредоточения / сосредоточением
paññā = мудрость / мудрости / мудростью
anaññātaññassāmīti = познание непознанного / познания непознанного / познанием непознанного
aññaṃ = окончательное знание / окончательного знания / окончательным знанием
aññātāvī = обладатель окончательного знания / обладателя окончательного знания / обладателем окончательного знания
indriyaṃ = способность / способности / способностью
indriyā = способности / способностей / способностями
dukkhaṃ = боль in this chapter (termbase sense for dukkhindriya), not «страдание» (Saccayamaka)
vīriyaṃ (no bare entry) = усердие (vīriyindriyaṃ «способность усердия»; style sheet vīriya = усердие)

## Person attributes (after «перерождается»)

sacakkhukānaṃ = с глазом
acakkhukānaṃ = без глаза
sasotakānaṃ = с ухом
asotakānaṃ = без уха
saghānakānaṃ = с носом
aghānakānaṃ = без носа
sacittakānaṃ = с умом
acittakānaṃ = без ума
sahetukānaṃ = с корнями
ahetukānaṃ = без корней
ñāṇasampayuttānaṃ = со знанием
ñāṇavippayuttānaṃ = без знания
somanassena = с радостью
vinā somanassena = без радости
upekkhāya = с невозмутимостью
vinā upekkhāya = без невозмутимости
itthīnaṃ = женщиной
na itthīnaṃ = не женщиной
purisānaṃ = мужчиной
na purisānaṃ = не мужчиной
order: the gender word first («женщиной с глазом»; negated with a comma «не женщиной, с глазом»;
  «не женщиной и не мужчиной»), the other attributes in the Pāli order joined «A и B» (G3);
  ahetukānaṃ / sahetukānaṃ: no entry, «без корней / с корнями» built from Ahetukaṃ / Sahetukaṃ
  «не имеющий / имеющий корни» on the pattern of sa-/a-cakkhuka «с глазом / без глаза»
tāsaṃ (feminine of tesaṃ) = у них (not rendered after a named person, as tesaṃ: G2)
uppajjantīnaṃ (^6-10-206, for upapajjantīnaṃ) = «кто возникает»: a one-letter slip, kept as written

Sacakkhukānaṃ asotakānaṃ upapajjantānaṃ tesaṃ = У тех, кто перерождается с глазом и без уха,
Sacakkhukānaṃ na itthīnaṃ upapajjantānaṃ tesaṃ = У тех, кто перерождается не женщиной, с глазом,
Sacakkhukānaṃ itthīnaṃ upapajjantīnaṃ tesaṃ = У тех, кто перерождается женщиной с глазом,
Itthīnaṃ acakkhukānaṃ upapajjantīnaṃ tesaṃ = У тех, кто перерождается женщиной без глаза,
Purisānaṃ vinā somanassena upapajjantānaṃ tesaṃ = У тех, кто перерождается мужчиной без радости,
Sahetukānaṃ na purisānaṃ upapajjantānaṃ tesaṃ = У тех, кто перерождается не мужчиной, с корнями,
Upekkhāya ñāṇasampayuttānaṃ upapajjantānaṃ tesaṃ = У тех, кто перерождается с невозмутимостью и со знанием,
Sabbesaṃ cavantānaṃ na itthīnaṃ na purisānaṃ upapajjantānaṃ tesaṃ = У всех, кто умирает, и у тех, кто перерождается не женщиной и не мужчиной,
Vinā somanassena upapajjantānaṃ pavatte somanassavippayuttacittassa uppādakkhaṇe tesaṃ = У тех, кто перерождается без радости, и в течение жизни в момент возникновения ума, не связанного с радостью,
Pavatte somanassasampayuttasaddhāvippayuttacittassa uppādakkhaṇe tesaṃ = В течение жизни в момент возникновения ума, связанного с радостью и не связанного с верой, у них
Ahetukānaṃ upekkhāya upapajjantānaṃ pavatte saddhāvippayuttaupekkhāsampayuttacittassa uppādakkhaṇe tesaṃ = У тех, кто перерождается без корней и с невозмутимостью, и в течение жизни в момент возникновения ума, не связанного с верой и связанного с невозмутимостью,
Sacittakānaṃ upapajjantānaṃ pavatte cittassa uppādakkhaṇe tesaṃ = У тех, кто перерождается с умом, и в течение жизни в момент возникновения ума
Sabbesaṃ cavantānaṃ pavatte cittassa bhaṅgakkhaṇe tesaṃ = У всех, кто умирает, и в течение жизни в момент распада ума
Sabbesaṃ cittassa bhaṅgakkhaṇe ñāṇavippayuttacittassa uppādakkhaṇe nirodhasamāpannānaṃ asaññasattānaṃ tesaṃ = У всех в момент распада ума, в момент возникновения ума, не связанного со знанием, у вошедших в медитативное достижение прекращения и у существ без восприятия
Itaresaṃ sacakkhukānaṃ upapajjantānaṃ tesaṃ = У остальных, кто перерождается с глазом,
Pacchimabhavikānaṃ itthīnaṃ upapajjantīnaṃ tesaṃ = У тех, кто в последний раз перерождается женщиной,

## Moments

X-sampayutta-cittassa = ума, связанного с X,; X-vippayutta- = ума, не связанного с X,; two members:
  «ума, связанного с радостью и не связанного с верой,» (X: somanassa с радостью, upekkhā с невозмутимостью,
  saddhā с верой, ñāṇa со знанием; termbase phrases, G45 punctuation)

## Pavatti answers

Sacakkhukānaṃ na itthīnaṃ upapajjantānaṃ tesaṃ cakkhundriyaṃ uppajjati, no ca tesaṃ itthindriyaṃ uppajjati. = У тех, кто перерождается не женщиной, с глазом, возникает способность глаза, но у них не возникает способность женственности.
Sacakkhukānaṃ itthīnaṃ upapajjantīnaṃ tāsaṃ cakkhundriyañca uppajjati itthindriyañca uppajjati. = У тех, кто перерождается женщиной с глазом, и возникает способность глаза, и возникает способность женственности.
Itthīnaṃ acakkhukānaṃ upapajjantīnaṃ tāsaṃ itthindriyaṃ uppajjati, no ca tāsaṃ cakkhundriyaṃ uppajjati. = У тех, кто перерождается женщиной без глаза, возникает способность женственности, но у них не возникает способность глаза.
Vinā somanassena upapajjantānaṃ pavatte somanassavippayuttacittassa uppādakkhaṇe tesaṃ jīvitindriyaṃ uppajjati, no ca tesaṃ somanassindriyaṃ uppajjati. = У тех, кто перерождается без радости, и в течение жизни в момент возникновения ума, не связанного с радостью, возникает жизненная способность, но у них не возникает способность радости.
Pavatte somanassasampayuttasaddhāvippayuttacittassa uppādakkhaṇe tesaṃ somanassindriyaṃ uppajjati, no ca tesaṃ saddhindriyaṃ uppajjati. = В течение жизни в момент возникновения ума, связанного с радостью и не связанного с верой, у них возникает способность радости, но у них не возникает способность веры.
Acittakānaṃ upapajjantānaṃ tesaṃ jīvitindriyaṃ uppajjati, no ca tesaṃ manindriyaṃ uppajjati. = У тех, кто перерождается без ума, возникает жизненная способность, но у них не возникает способность ума.
Rūpāvacare arūpāvacare tattha jīvitindriyaṃ uppajjati, no ca tattha ghānindriyaṃ uppajjati. = В мире форм и в мире без форм возникает жизненная способность, но там не возникает способность носа.
Asaññasatte arūpe tattha jīvitindriyaṃ uppajjati, no ca tattha cakkhundriyaṃ uppajjati. = Среди существ без восприятия и в мире без форм возникает жизненная способность, но там не возникает способность глаза.
(Cakkhundriyamūlakaṃ) = (На основе способности глаза)

## Paṇṇatti

(Ka) cakkhu cakkhundriyaṃ? = (а) Глаз является способностью глаза?
(Kha) indriyā sotindriyaṃ? = (б) Способности являются способностью уха?
(Ka) na cakkhu na indriyaṃ? = (а) То, что не является глазом, не является способностью?
(Kha) na indriyā na aññātāvī? = (б) То, что не является способностями, не является обладателем окончательного знания?
(Ka) jīvitaṃ jīvitindriyanti? = (а) Жизнь является жизненной способностью?
Dibbacakkhu paññācakkhu cakkhu, na cakkhundriyaṃ. = Божественный глаз, глаз мудрости является глазом, но не является способностью глаза.
Cakkhundriyaṃ cakkhu ceva cakkhundriyañca. = Способность глаза и является глазом, и является способностью глаза.
Sotindriyaṃ indriyañceva sotindriyañca. = Способность уха и является способностью, и является способностью уха.
Avasesā indriyā na sotindriyaṃ. = Остальные способности не являются способностью уха.
Itthindriyaṃ na itthī, itthindriyaṃ. = Способность женственности не является женщиной, но является способностью женственности.
Itthiñca itthindriyañca ṭhapetvā avasesā na ceva itthī na ca itthindriyaṃ. = Кроме женщины и способности женственности, остальные не являются ни женщиной, ни способностью женственности.
Upekkhindriyaṃ ṭhapetvā avasesā upekkhā, na upekkhindriyaṃ. = Кроме способности невозмутимости, остальное является невозмутимостью, но не является способностью невозмутимости.
Upekkhindriyaṃ ṭhapetvā avasesā na upekkhindriyaṃ, upekkhā. = Кроме способности невозмутимости, остальное не является способностью невозмутимости, но является невозмутимостью.
Kāyindriyaṃ ṭhapetvā avaseso na kāyindriyaṃ, kāyo. = Кроме способности тела, остальное не является способностью тела, но является телом.
Cakkhuṃ ṭhapetvā avasesā indriyā na cakkhu, indriyā. = Кроме глаза, остальные способности не являются глазом, но являются способностями.
Cakkhuñca indriye ca ṭhapetvā avasesā na ceva cakkhu na ca indriyā. = Кроме глаза и способностей, остальные не являются ни глазом, ни способностями.
Yaṃ sotaṃ indriyaṃ taṃ sotañceva indriyañca. = Ухо, которое является способностью, является и ухом, и способностью.
Avasesaṃ sotaṃ na indriyaṃ. = Остальное ухо не является способностью.
Yo kāyo indriyaṃ so kāyo ceva indriyañca. = Тело, которое является способностью, является и телом, и способностью.
Yā upekkhā indriyaṃ sā upekkhā ceva indriyañca. = Невозмутимость, которая является способностью, является и невозмутимостью, и способностью.
Avasesā upekkhā na indriyaṃ. = Остальная невозмутимость не является способностью.
Sotaṃ sotindriyaṃ? Indriyā cakkhundriyaṃ?…Pe…. = Ухо является способностью уха? Способности являются способностью глаза?…
(Kha) na indriyā na cakkhundriyaṃ? …Pe… na indriyā na aññātāvindriyaṃ? = (б) То, что не является способностями, не является способностью глаза? … то, что не является способностями, не является способностью обладателя окончательного знания?
Sukhaṃ sukhindriyanti? Āmantā …pe…. = Удовольствие является способностью удовольствия? Да…
Cakkhundriyaṃ indriyañceva cakkhundriyañca. Avasesā indriyā na cakkhundriyaṃ…pe…. = Способность глаза и является способностью, и является способностью глаза. Остальные способности не являются способностью глаза…
Yaṃ X indriyaṃ taṃ Xñceva indriyañca = «X, который / которая / которое является способностью, является и X,
  и способностью» (coordinator: one main verb after a relative clause); Avasesaṃ / Avaseso / Avasesā X =
  «Остальное / Остальной / Остальная X»; X ṭhapetvā avasesā + a singular noun (upekkhā) = «остальное» (sg.)

## Headings, lists

### Indriyayamakaṃ = ### Парные вопросы о способностях
#### Suddhindriyavāro = #### Раздел о способностях как таковых
#### Suddhindriyamūlacakkavāro = #### Круговой раздел на основе способностей как таковых
#### Pavattivāro = #### Раздел о протекании
#### Uppādavāro = #### Раздел о возникновении
##### (Ga) anulomapuggalokāsā = ##### (в) Утвердительная форма по личности и месту
##### (Ṅa) paccanīkaokāso = ##### (д) Отрицательная форма по месту
Bāvīsatindriyāni – cakkhundriyaṃ, … = Двадцать две способности – способность глаза, способность уха, способность носа, способность языка, способность тела, способность ума, способность женственности, способность мужественности, жизненная способность, способность удовольствия, способность боли, способность радости, способность уныния, способность невозмутимости, способность веры, способность усердия [вариант написания (Sī., Syā.): viriyindiyaṃ], способность осознанности, способность сосредоточения, способность мудрости, способность познания непознанного, способность окончательного знания, способность обладателя окончательного знания.
