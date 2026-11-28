# notes-map-G10a: indriyayamaka keyword values (10-01 … 10-04)

Script: map_G10a_ru.py (importable, writes nothing). For G10b: IN_FACULTY (22 faculties + indriyaṃ / indriyā / indriye + X-indriyamūlakaṃ), IN_BARE (bare paṇṇatti words + Āyatana qualifiers + ṭhapetvā / avasesā), IN_PERSON (person attributes and person verbs), IN_MOMENT + moment_value(kw) (associated-mind moments, also pacchimacittassa and bhaṅgakkhaṇe), IN_HEAD, G10A_TABLE = YM + G2_FRAME + G3 AY_PLANES + G8 TIME / PERSONS + these; resolver_for(part), exceptions_for(part). Imports map_G2_ru (G2_FRAME, frame_value, frame_exceptions, _fold_ti), map_G3_ru (AY_PLANES, AY_HAVE, qualifiers), map_G8_ru (TIME, PERSONS); G2_KHANDHA not imported; map_G6_ru read (its planes / persons agree with G2 / G3). Translation file is the truth; builders build_10-0N_ru.py, notes-10-0N.md. Verbs, answers, planes, persons, vāra headings: as notes-map-G2 / G3 / G8 (not repeated). Every case form takes one value; -ti / -nti / -ñca / -ñceva fold to the base form.

## Faculties (pi-2 ^2-221; every form: -ṃ, -nti, -ñca, capitalised)
cakkhundriyaṃ = способность глаза; sotindriyaṃ = способность уха; ghānindriyaṃ = способность носа; jivhindriyaṃ = способность языка; kāyindriyaṃ = способность тела; manindriyaṃ = способность ума
itthindriyaṃ = способность женственности; purisindriyaṃ = способность мужественности; jīvitindriyaṃ = жизненная способность
sukhindriyaṃ = способность удовольствия; dukkhindriyaṃ = способность боли; somanassindriyaṃ = способность радости; domanassindriyaṃ = способность уныния; upekkhindriyaṃ = способность невозмутимости
saddhindriyaṃ = способность веры; vīriyindriyaṃ = способность усердия; satindriyaṃ = способность осознанности; samādhindriyaṃ = способность сосредоточения; paññindriyaṃ = способность мудрости
anaññātaññassāmītindriyaṃ = способность познания непознанного; aññindriyaṃ = способность окончательного знания; aññātāvindriyaṃ = способность обладателя окончательного знания
indriyaṃ / indriyanti / indriyañca / indriyañceva = способность («является способностью», «является и способностью, и …»); indriyā / indriye = способности («Способности являются …», «Кроме глаза и способностей»)
(X-indriyamūlakaṃ) = на основе способности X («(На основе способности глаза)»); Jīvitindriyamūlakaṃ = на основе жизненной способности

## Bare words of the paṇṇattivāra (10-01, 10-02)
cakkhu / cakkhū / cakkhuṃ = глаз; sotaṃ = ухо; ghānaṃ = нос; jivhā / jivhaṃ = язык; kāyo / kāyaṃ = тело; mano / manaṃ = ум (as G3)
itthī / itthiṃ = женщина; puriso / purisaṃ = мужчина; jīvitaṃ = жизнь
sukhaṃ = удовольствие (as in «способность удовольствия», not «счастье»); dukkhaṃ = боль (not «страдание»); somanassaṃ = радость; domanassaṃ = уныние; upekkhā / upekkhaṃ = невозмутимость
saddhā / saddhaṃ = вера; vīriyaṃ = усердие; sati / satiṃ = осознанность; samādhi / samādhiṃ = сосредоточение; paññā / paññaṃ = мудрость
anaññātaññassāmīti / -tiṃ = познание непознанного (^6-10-3 slip anaññātaññāssāmīti the same, rendered as meant); aññaṃ = окончательное знание; aññātāvī / aññātāviṃ = обладатель окончательного знания
Dibbacakkhu / paññācakkhu / Dibbasotaṃ / taṇhāsotaṃ = божественный глаз / глаз мудрости / божественное ухо / поток жажды (G3); sotaṃ in «являются «ухом»» = ухо
ṭhapetvā = кроме; avasesā / avaseso / Avasesaṃ = остальной («остальное», «Остальные способности», «Остальное ухо»)

## Persons (pavatti frame; G3 sacakkhukānaṃ «с глазом» pattern)
itthīnaṃ = женщина; purisānaṃ = мужчина («перерождается (не) женщиной / мужчиной»; «не» belongs to the separate na)
somanassena = радость; upekkhāya = невозмутимость («с радостью», and after vinā «без радости»: instrumental keyword -> nominative noun, conventions-pi6 §3; vinā carries «без», the «с» belongs to the case)
ñāṇasampayuttānaṃ = со знанием; ñāṇavippayuttānaṃ = без знания (person attributes; the prepositional phrase carries sampayutta / vippayutta, as sa- / a- in G3)
sahetukānaṃ = с корнями; ahetukānaṃ = без корней (prepared; not listed in 10-01 … 10-04)
sacakkhukānaṃ / acakkhukānaṃ, sasotakānaṃ / asotakānaṃ, sacittakānaṃ / acittakānaṃ = с глазом / без глаза … (G3 AY_HAVE); sajivhakānaṃ / ajivhakānaṃ = с языком / без языка, sakāyakānaṃ / akāyakānaṃ = с телом / без тела (prepared)
upapajjantīnaṃ = перерождаться (feminine of upapajjantānaṃ, G2)
uppajjantīnaṃ (^6-10-206 «Itthīnaṃ … uppajjantīnaṃ», arise for be reborn; kept as written «кто возникает женщиной») = возникать
cavantānaṃ = умирать; nirodhasamāpannānaṃ = вошедший в медитативное достижение прекращения; asaññasattānaṃ = существа без восприятия (G2 / G8)
pavatte / Pavatte = течение жизни («в течение жизни», as G45)

## Moments (locative -> nominative noun phrase without «в», comma dropped; G8 / G45 rule)
cittassa uppādakkhaṇe / bhaṅgakkhaṇe = момент возникновения / распада ума (G8)
X-sampayuttacittassa uppādakkhaṇe = момент возникновения ума связанного с X; X-vippayutta- = … ума не связанного с X (X: somanassa с радостью, upekkhā с невозмутимостью, saddhā с верой, ñāṇa со знанием)
two members (somanassasampayuttasaddhāvippayuttacittassa uppādakkhaṇe) = момент возникновения ума связанного с радостью и не связанного с верой (Pāli order = Russian order)
X-…pacchimacittassa … = момент возникновения / распада последнего ума связанного с X (prepared, moment_value)

## Headings
Indriyayamakaṃ = парные вопросы о способностях; Suddhindriyavāro = раздел о способностях как таковых; Suddhindriyamūlacakkavāro = круговой раздел на основе способностей как таковых
Paṇṇatti- / Padasodhana- / Pavatti- / Uppāda- headings, anuloma- / paccanīka- puggalo / okāso / puggalokāsā, uddeso, niddeso = G2 HEAD_KW / YM
(no direct equivalent) as a listed keyword (^6-10-162) = (no direct equivalent) (kept as listed; G2, G8)

## Verbs and answers
uppajjati / uppajjatīti = возникать (also after a separate na, and in the denied negative «no ca tattha Y na uppajjati» = «но там возникает Y»: the keyword is the positive verb); Natthi = такого нет; Āmantā = да; No = нет (G2)
