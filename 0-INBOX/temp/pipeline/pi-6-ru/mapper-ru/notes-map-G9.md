# notes-map-G9: dhammayamaka keyword values (9-01, 9-02, 9-03)

Script: map_G9_ru.py (importable, writes nothing; DH_MEMBERS, DH_MOMENTS, DH_PERSONS, DH_FRAME, citta_moment(), pj_value(), G9_TABLE = YM + G2_FRAME + G8 TENSE / TIME / PERSONS / HEADINGS + these; resolver_for(part), exceptions_for(part)). Frames imported from map_G2_ru (G2_FRAME, frame_value(), frame_exceptions(); not G2_KHANDHA) and map_G8_ru (moments, persons, headings). map_G3_ru read: none of its paṇṇatti additions (glued negated nouns, -pi / yassaka notes) occur here (the Dhamma paṇṇatti has a separate «na»). Sacca-type person units = the same values as map_G45_ru MOMENTS (set here, not imported: G45 ran at the same time). Translation file is the truth; builders build_9-0N_ru.py, notes-9-0N.md. -ti / -nti / -ñca / -ñceva fold to the base form.

## Members
kusalā / akusalā / abyākatā (bare, paṇṇattivāra «Благие являются …») = благой / неблагой / этически неопределённый (YM)
Kusalaṃ / Akusalaṃ / Abyākataṃ / Kusalañca («Кроме благого …») = благой / неблагой / этически неопределённый
kusalā dhammā / kusalā dhammāti / Kusalā dhammā = благие явления (неблагие явления, этически неопределённые явления)
kusalā ca dhammā / akusalā ca dhammā / abyākatā ca dhammā = благие явления … («и возникают благие явления, и возникают …»; ca = и, no word of its own)
Kusalañca dhamme / Akusalañca dhamme / Abyākatañca dhamme = благой и явления / неблагой и явления / этически неопределённый и явления («Кроме благого и явлений»; two-member keyword = whole phrase, nominative)
Avasesā / avasesā = остальной («Остальные явления», «остальное»); ṭhapetvā = кроме
kusalaṃ dhammaṃ / akusalaṃ dhammaṃ = благое явление / неблагое явление (bhāvanāvāra «Кто развивает благое явление»; singular as the Pāli)

## Moments (locative -> nominative noun phrase without «в», G8 rule; comma before «не связанного» dropped)
kusalānaṃ / akusalānaṃ uppādakkhaṇe = момент возникновения благих / неблагих явлений
kusalānaṃ / akusalānaṃ bhaṅgakkhaṇe = момент распада благих / неблагих явлений
kusalākusalānaṃ (keyword split from «kusalākusalānaṃ bhaṅgakkhaṇe») = благие и неблагие явления («в момент распада благих и неблагих явлений»)
kusalavippayuttacittassa uppādakkhaṇe = момент возникновения ума не связанного с благим (akusala- = с неблагим)
kusalavippayuttacittassa bhaṅgakkhaṇe = момент распада ума не связанного с благим (akusala- = с неблагим)
kusalavippayuttaakusalavippayuttacittassa uppāda- / bhaṅgakkhaṇe = момент возникновения / распада ума не связанного с благим и не связанного с неблагим (reverse order the same, reversed)
cittassa uppādakkhaṇe / cittassa bhaṅgakkhaṇe = момент возникновения ума / момент распада ума (where the Pāli segment has the plain unit «Sabbesaṃ cittassa …»)
cittassa uppādakkhaṇe / cittassa bhaṅgakkhaṇe = момент возникновения … ума / момент распада … ума (where the segment has only «tassa cittassa …» = «в момент возникновения этого ума»; «этого» renders the unlisted tassa; citta_moment())
uppādakkhaṇe / bhaṅgakkhaṇe (split from «Aggamaggassa …», «Pacchimacittassa …») = момент возникновения / момент распада (G8)
Pacchimacittassa = последний ум; Pacchimacittassa bhaṅgakkhaṇe = момент распада последнего ума (G8)
Aggamaggassa = высший путь («в момент возникновения / распада высшего пути»; G45)

## Persons and places
cittassa = ум («сразу после данного ума»); anantarā = сразу после; aggamaggaṃ paṭilabhissanti = обрести высший путь (presence exception «обретёт высший путь», self-checked) (all G45)
Aggamaggasamaṅgīnaṃ = обладающий высшим путём; arahantānaṃ = архаты («у архатов»); Pacchimacittasamaṅgīnaṃ = обладающий последним умом (G8)
nirodhasamāpannānaṃ = вошедший в медитативное достижение прекращения (G8); asaññasattānaṃ / Asaññasatte = существа без восприятия (G2 / G8)
pavatte = течение жизни; vattamāne = присутствовать («когда присутствует второй ум»); citte = ум; akusale citte = неблагой ум («второй неблагой ум») (G45)
Itaresaṃ = остальной; upapajjantānaṃ = перерождаться; cavantānaṃ = умирать (G2)
Pañcavokāre / Catuvokāre = существование с пятью / четырьмя составляющими; pañcavokārānaṃ = существа с пятью составляющими; Arūpe / arūpe = мир без форм; Suddhāvāsaṃ = Чистые обители; Suddhāvāsānaṃ = существа Чистых обителей (G2 PLANE_KW)

## Verbs and answers
uppajjanti / uppajjantīti / uppajjittha / uppajjitthāti = возникать; uppajjissanti / uppajjissantīti = возникнуть (G2)
nirujjhanti / nirujjhantīti / nirujjhittha / nirujjhitthāti = прекращаться (G2)
nirujjhissanti / nirujjhissantīti = прекратиться (G2; presence exception «прекратиться ~ прекратится/прекратятся», self-checked: plural stem change)
verbs after a separate «na» (and the denied negative «no ca tesaṃ Y na nirujjhanti» = «но у них прекращаются Y») = the positive verb
bare answers Uppajjanti. / Uppajjittha. / Nirujjhissanti. («Возникают.» …) = the verb's infinitive
Natthi = такого нет; Yattha / yattha = где
bhāveti / bhāvetīti = развивать («развивает»); pajahati / pajahatīti = устранять (G7 / G45)
nappajahati / nappajahatīti = не устранять («не устраняет»; glued n- as G2 nuppajjati; the positive verb where the Russian has it only positively)

## Headings and colophons (lower-case first letter, label / number dropped)
Dhammayamakaṃ = парные вопросы о явлениях (G8)
Suddhadhammavāro = раздел о явлениях как таковых («3 Раздел …»); Suddhadhammamūlacakkavāro = круговой раздел на основе явлений как таковых
Bhāvanāvāro (heading and closing) = раздел о развитии
paccanīkapuggalokāsā / anulomapuggalokāsā as plain lines (^6-9-120, ^6-9-135) = G2 heading values
Paṇṇattivāro, Padasodhana-, Pavattivāro, Uppādavāro, Nirodhavāro, Uppādanirodhavāro, Atītānāgatavāro, Paṇṇattiniddesavāro, uddeso, niddeso = G2 / YM values
Abhidhammapiṭake / Namo / bhagavato / arahato / sammāsambuddhassa (^6-9-229) = CORE
(no direct equivalent) as a listed keyword = (no direct equivalent) (kept as listed; G2, G8)
