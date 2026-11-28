# notes-rails-G10b2: Indriyayamaka (10-09 … 10-13) frames

Format: Pāli = Russian, one per line. Builder: build_rails_G10b2_ru.py (importlib.import_module(
"build_rails_G10b2_ru"); importing writes nothing). Everything else is G10a / G2 / G8 / G3 / G45 / G9 verbatim
(see notes-rails-G10a.md); the eteneva bhāvena / ATTR_NOM / last-mind / ATTR + plane shapes are G10b1's strings,
copied so both groups agree. Import order: G9 first (it resets G45.UNITS; G6 via G9 resets G2.GROUP_RULES, which
install_units() rebuilds with G3's shapes); `--regress` re-renders 10-01 … 10-04 and must report OK.

## Person intros (mixed tenses)

Pacchimabhavikānaṃ pañcavokāraṃ upapajjantānaṃ ye ca arūpaṃ upapajjitvā parinibbāyissanti tesaṃ upapajjantānaṃ tesaṃ = У тех, кто в последний раз перерождается в существовании с пятью составляющими, и у тех перерождающихся, кто, переродившись в мире без форм, достигнет окончательного угасания,
Pacchimabhavikānaṃ pañcavokāraṃ upapajjantānaṃ ye ca rūpāvacaraṃ arūpāvacaraṃ upapajjitvā parinibbāyissanti ye ca purisā eteneva bhāvena katici bhave dassetvā parinibbāyissanti tesaṃ upapajjantānaṃ tesaṃ = У тех, кто в последний раз перерождается в существовании с пятью составляющими, у тех перерождающихся, кто, переродившись в мире форм и в мире без форм, достигнет окончательного угасания, и у тех перерождающихся мужчин, которые, пройдя в этом же состоянии несколько существований, достигнут окончательного угасания,
Pacchimabhavikānaṃ pañcavokāraṃ upapajjantānaṃ ye ca sacakkhukā upekkhāya upapajjitvā parinibbāyissanti tesaṃ upapajjantānaṃ tesaṃ = У тех, кто в последний раз перерождается в существовании с пятью составляющими, и у тех перерождающихся, кто, переродившись с глазом и с невозмутимостью, достигнет окончательного угасания,
Pacchimabhavikānaṃ itthīnaṃ upapajjantīnaṃ yā ca itthiyo upekkhāya upapajjitvā parinibbāyissanti tesaṃ upapajjantīnaṃ tesaṃ = У тех, кто в последний раз перерождается женщиной, и у тех перерождающихся женщин, которые, переродившись с невозмутимостью, достигнут окончательного угасания,
Pacchimabhavikānaṃ purisānaṃ upapajjantānaṃ ye ca purisā somanassena upapajjitvā parinibbāyissanti tesaṃ upapajjantānaṃ tesaṃ = У тех, кто в последний раз перерождается мужчиной, и у тех перерождающихся мужчин, которые, переродившись с радостью, достигнут окончательного угасания,
Pañcavokāre parinibbantānaṃ arūpe pacchimabhavikānaṃ ye ca upekkhāya upapajjitvā parinibbāyissanti tesaṃ cavantānaṃ tesaṃ = У тех, кто достигает окончательного угасания в существовании с пятью составляющими, у тех, кто живёт последней жизнью в мире без форм, и у тех умирающих, кто, переродившись с невозмутимостью, достигнет окончательного угасания,
Kāmāvacare parinibbantānaṃ rūpāvacare arūpāvacare pacchimabhavikānaṃ asaññasattānaṃ yā ca itthiyo somanassena upapajjitvā parinibbāyissanti tesaṃ cavantīnaṃ tesaṃ = У тех, кто достигает окончательного угасания в мире чувственных желаний, у тех, кто живёт последней жизнью в мире форм и в мире без форм, у существ без восприятия и у тех умирающих женщин, которые, переродившись с радостью, достигнут окончательного угасания,
Pacchimabhavikānaṃ kāmāvacaraṃ upapajjantānaṃ rūpāvacaraṃ upapajjantānaṃ tesaṃ = У тех, кто в последний раз перерождается в мире чувственных желаний, и у тех, кто перерождается в мире форм,
Pacchimacittassa uppādakkhaṇe yassa cittassa anantarā upekkhāsampayuttapacchimacittaṃ uppajjissati tassa cittassa uppādakkhaṇe tesaṃ = В момент возникновения последнего ума и у тех, у кого сразу после данного ума возникнет последний ум, связанный с невозмутимостью, в момент возникновения этого ума
Somanassasampayuttapacchimacittassa uppādakkhaṇe tesaṃ = В момент возникновения последнего ума, связанного с радостью, у них
Somanassasampayuttapacchimacittassa bhaṅgakkhaṇe upekkhāsampayuttapacchimacittasamaṅgīnaṃ yassa cittassa anantarā somanassasampayuttapacchimacittaṃ uppajjissati tassa cittassa bhaṅgakkhaṇe tesaṃ = В момент распада последнего ума, связанного с радостью, у обладающих последним умом, связанным с невозмутимостью, и у тех, у кого сразу после данного ума возникнет последний ум, связанный с радостью, в момент распада этого ума
ye (ca) ATTR… PLANE… upapajjitvā parinibbāyissanti tesaṃ upapajjantānaṃ / cavantānaṃ = у тех перерождающихся / умирающих, кто, переродившись …, достигнет окончательного угасания (G3 shape + G10b1 ATTR_NOM)
ye ca purisā / yā ca itthiyo (…) parinibbāyissanti tesaṃ upapajjantānaṃ / tāsaṃ cavantīnaṃ = у тех перерождающихся / умирающих мужчин / женщин, которые, …, достигнут окончательного угасания (G45 «у тех
  перерождающихся обычных людей, которые …»)
a participle after a run of ye-groups («ye … parinibbāyissanti ye ca … parinibbāyissanti tesaṃ upapajjantānaṃ») goes with each group (distribute())
X-sampayuttapacchimacittassa = последнего ума, связанного с X, (moment; termbase)
X-sampayuttapacchimacittasamaṅgīnaṃ = у обладающих последним умом, связанным с X, (termbase)
pacchimabhavikānaṃ purisānaṃ uppajjantānaṃ (^6-10-398, as written) = у тех, кто в последний раз возникает мужчиной

## Pavatti answers

Pacchimabhavikānaṃ pañcavokāraṃ upapajjantānaṃ ye ca arūpaṃ upapajjitvā parinibbāyissanti tesaṃ upapajjantānaṃ tesaṃ cakkhundriyaṃ uppajjati, no ca tesaṃ sotindriyaṃ uppajjissati. = У тех, кто в последний раз перерождается в существовании с пятью составляющими, и у тех перерождающихся, кто, переродившись в мире без форм, достигнет окончательного угасания, возникает способность глаза, но у них не возникнет способность уха.
Itarāsaṃ itthīnaṃ upapajjantīnaṃ tāsaṃ itthindriyañca uppajjati purisindriyañca uppajjissati. = У остальных, кто перерождается женщиной, и возникает способность женственности, и возникнет способность мужественности.
Pañcavokāre parinibbantānaṃ arūpe pacchimabhavikānaṃ tesaṃ cakkhundriyañca na uppajjati jīvitindriyañca na uppajjissati. = У тех, кто достигает окончательного угасания в существовании с пятью составляющими, и у тех, кто живёт последней жизнью в мире без форм, и не возникает способность глаза, и не возникнет жизненная способность.
Somanassasampayuttapacchimacittassa uppādakkhaṇe tesaṃ somanassindriyaṃ uppajjati, no ca tesaṃ manindriyaṃ uppajjissati. = В момент возникновения последнего ума, связанного с радостью, у них возникает способность радости, но у них не возникнет способность ума.
Yassa cakkhundriyaṃ uppajjati tassa purisindriyaṃ uppajjissatīti? (Sadisaṃ ) = У кого возникает способность глаза, у того возникнет способность мужественности? (Так же)
(Sadisaṃ ) = (Так же)  (sadisaṃ «the same»; no full stop in the Pāli)

## Pariññā (10-13)

verbs (termbase; G2 / G45 / G9 forms; past perfective by the subject's gender, «-ла» for «личность»):
  parijānāti = полностью понимает / полностью понимают; na parijānāti = не понимает полностью / не понимают полностью
  parijānittha = полностью понял / полностью поняли; na parijānittha = не понял полностью / не поняли полностью
  parijānissati = полностью поймёт / полностью поймут; na parijānissati = не поймёт полностью / не поймут полностью
  pajahati = устраняет / устраняют; na pajahati = не устраняет / не устраняют
  pajahittha = устранил / устранили; na pajahittha = не устранил / не устранили
  pajahissati = устранит / устранят; na pajahissati = не устранит / не устранят
  bhāveti = развивает / развивают; na bhāveti = не развивает / не развивают
  bhāvittha = развил / развили; na bhāvittha = не развил / не развили
  bhāvessati = разовьёт / разовьют; na bhāvessati = не разовьёт / не разовьют
  sacchikaroti = осуществляет / осуществляют; na sacchikaroti = не осуществляет / не осуществляют
  sacchikarittha = осуществил / осуществили; na sacchikarittha = не осуществил / не осуществили
  sacchikarissati = осуществит / осуществят; na sacchikarissati = не осуществит / не осуществят
  sacchākāsi = осуществил (in «Yo aggaphalaṃ sacchākāsi so»); -ittha serves both numbers (no slip)
persons:
  arahā = Архат
  aggamaggasamaṅgī = Обладающий высшим путём
  anāgāmimaggasamaṅgī = Обладающий путём невозвращения
  aṭṭhamako = Личность восьмой ступени
  anāgāmī = Невозвращающийся
  tayo maggasamaṅgino = Три обладающих путём
  yo aggaphalaṃ sacchikaroti so = Тот, кто осуществляет высший плод,
  yo aggaphalaṃ sacchākāsi so = Тот, кто осуществил высший плод,
  ye puthujjanā maggaṃ paṭilabhissanti te = Те обычные люди, которые обретут путь,
  ye puthujjanā maggaṃ na paṭilabhissanti te = Те обычные люди, которые не обретут путь,
  dve puggalā = Две личности
  tayo puggalā = Три личности
  cattāro puggalā = Четыре личности
  pañca puggalā = Пять личностей
  cha puggalā = Шесть личностей
  satta puggalā = Семь личностей
  aṭṭha puggalā = Восемь личностей
  dve maggasamaṅgino ṭhapetvā avasesā puggalā = Кроме двух обладающих путём, остальные личности
  tayo maggasamaṅgino ṭhapetvā avasesā puggalā = Кроме трёх обладающих путём, остальные личности
  cattāro maggasamaṅgino ṭhapetvā avasesā puggalā = Кроме четырёх обладающих путём, остальные личности
  tayo maggasamaṅgino ca arahantañca ṭhapetvā avasesā puggalā = Кроме трёх обладающих путём и архата, остальные личности
  anāgāmimaggasamaṅgiñca arahantañca ṭhapetvā avasesā puggalā = Кроме обладающего путём невозвращения и архата, остальные личности
  aṭṭhamakañca arahantañca ṭhapetvā avasesā puggalā = Кроме личности восьмой ступени и архата, остальные личности
  aggamaggasamaṅgiñca arahantañca ṭhapetvā avasesā puggalā = Кроме обладающего высшим путём и архата, остальные личности

(Ka) yo cakkhundriyaṃ parijānāti so domanassindriyaṃ pajahatīti? = (а) Кто полностью понимает способность глаза, тот устраняет способность уныния?
(Kha) yo vā pana anaññātaññassāmītindriyaṃ bhāveti so cakkhundriyaṃ parijānātīti? = (б) А кто развивает способность познания непознанного, тот полностью понимает способность глаза?
(Ka) yo cakkhundriyaṃ parijānittha so aññātāvindriyaṃ sacchikaritthāti? = (а) Кто полностью понял способность глаза, тот осуществил способность обладателя окончательного знания?
(Ka) yo domanassindriyaṃ nappajahissati so aññātāvindriyaṃ na sacchikarissatīti? = (а) Кто не устранит способность уныния, тот не осуществит способность обладателя окончательного знания?
Dve puggalā aññindriyaṃ bhāventi, no ca cakkhundriyaṃ parijānanti. = Две личности развивают способность окончательного знания, но не понимают полностью способность глаза.
Aggamaggasamaṅgī aññindriyañca bhāveti cakkhundriyañca parijānāti. = Обладающий высшим путём и развивает способность окончательного знания, и полностью понимает способность глаза.
Dve maggasamaṅgino ṭhapetvā avasesā puggalā cakkhundriyañca na parijānanti domanassindriyañca nappajahanti. = Кроме двух обладающих путём, остальные личности и не понимают полностью способность глаза, и не устраняют способность уныния.
Yo aggaphalaṃ sacchikaroti so cakkhundriyaṃ na parijānāti, no ca aññātāvindriyaṃ na sacchikaroti. = Тот, кто осуществляет высший плод, не понимает полностью способность глаза, но осуществляет способность обладателя окончательного знания.
Aṭṭhamako aññindriyaṃ na bhāvittha, no ca anaññātaññassāmītindriyaṃ na bhāveti. = Личность восьмой ступени не развила способность окончательного знания, но развивает способность познания непознанного.
Cattāro maggasamaṅgino ṭhapetvā avasesā puggalā aññindriyañca na bhāventi anaññātaññassāmītindriyañca na bhāventi. = Кроме четырёх обладающих путём, остальные личности не развивают ни способность окончательного знания, ни способность познания непознанного.
Ye puthujjanā maggaṃ paṭilabhissanti te cakkhundriyañca parijānissanti anaññātaññassāmītindriyañca bhāvessanti. = Те обычные люди, которые обретут путь, и полностью поймут способность глаза, и разовьют способность познания непознанного.
Cha [pañca (sī. syā. ka.)] puggalā aññindriyañca na bhāventi aññātāvindriyañca na sacchikarittha. = Шесть [вариант чтения (Sī., Syā., Ka.): pañca] личностей и не развивают способность окончательного знания, и не осуществили способность обладателя окончательного знания.
Pariññāvāro. = Раздел о полном понимании.
Indriyayamakaṃ niṭṭhitaṃ. = Парные вопросы о способностях завершены.
Yamakapakaraṇaṃ niṭṭhitaṃ. = Парные вопросы завершены.

## Slips (as written / as meant)

^6-10-369 «somanassindriyaṃ uppajjissati, tassa» = stray comma (the Russian question has one anyway)
^6-10-376 «Sacakkhukānaṃ … manindriyaṃ uppajjissati cakkhundriyañca uppajjati» = one «ca» missing: «возникнет способность ума и возникает способность глаза» (as written, G2 rule)
^6-10-385 «itthindriyaṃ na uppajjissanti» = не возникнет (plural verb, singular subject: Russian agreement)
^6-10-387 / ^6-10-452 / ^6-10-477 missing comma before «no ca» (as meant)
^6-10-393 missing full stop before «pacchimacittassa bhaṅgakkhaṇe» (as meant)
^6-10-398 Pacchimabhavikānaṃ purisānaṃ uppajjantānaṃ = у тех, кто в последний раз возникает мужчиной (as written)
^6-10-452 «…, pañca puggalā aññindriyañca bhavissanti …» = «…, пять личностей и будут способностью окончательного знания, и …» (bhavissanti and the comma as written)
^6-10-454 / ^6-10-459 / ^6-10-468 plural verb with a singular subject (Russian agreement)
^6-10-455 questions ending with «.» (as written)
^6-10-468 «… pajahanti anāgāmimaggasamaṅgi aññindriyañca bhāvessanti, domanassindriyañca pajahanti.» = full stop added, -samaṅgī (as meant), stray comma (Russian «и …, и …»)
^6-10-477 «(Kha) yo vā pana aññindriyaṃ bhāvessati. So …?» = «(б) А кто разовьёт способность окончательного знания. Тот развил …?» (full stop as written)
^6-10-480 nappajjahittha = не устранил (as meant, nappajahittha)
