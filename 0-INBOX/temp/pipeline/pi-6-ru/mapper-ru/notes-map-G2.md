# notes-map-G2: khandhayamaka keyword values (2-01, 2-02; frame-setter for the paṇṇatti, pavatti and pariññā frames)

Script: map_G2_ru.py (importable, writes nothing on import). Later groups: `table = {**G2.YM, **G2.G2_FRAME, **own}`; call `G2.frame_value(kw, pali, ru)` first (denied negative, pariññā word order, pacchimabhavika); `G2.frame_exceptions(part)` gives the self-checking presence exceptions of the frame verbs. Do NOT import G2_KHANDHA (rūpaṃ = форма is Khandha-only). Translation file is the truth; builders build_2-01_ru.py / build_2-02_ru.py, notes-2-01.md / notes-2-02.md. Agrees with notes-map-G8 (verbs, Natthi, itaresaṃ, asaññasattānaṃ, vāra headings).

## Pavatti frame: verbs (text verb -> infinitive; tense kept by aspect)
uppajjati / uppajjanti / uppajjatīti / Uppajjati = возникать (возникает / возникают)
uppajjittha / uppajjitthāti / Uppajjittha = возникать (возникал / возникала: imperfective past, same infinitive)
uppajjissati / uppajjissanti / uppajjissatīti / Uppajjissati = возникнуть (возникнет; presence exception «возникнуть ~ возникнет», self-checked)
nirujjhati / nirujjhanti / nirujjhatīti / Nirujjhati = прекращаться
nirujjhittha / nirujjhitthāti / Nirujjhittha = прекращаться (прекращалась); nirujjhattha (^6-2-111 slip) = прекращаться
nirujjhissati / nirujjhissanti / nirujjhissatīti = прекратиться (прекратится)
nuppajjati / nuppajjatīti = не возникать (questions «У кого не возникает …»; «не возникает ни X, ни Y»)
nuppajjittha / nuppajjitthāti = не возникать (не возникала); nuppajjissati / nuppajjissatīti = не возникнуть (не возникнет)
nuppajj- in a segment whose Russian has that tense only positively (denied negative «no ca tesaṃ Y nuppajjati» = «но у них возникает Y») = возникать / возникнуть (pv_neg_value; none occurred in 2-01 / 2-02)
nirujjhati after a separate «na» (na nirujjhati) = прекращаться (the keyword is the positive verb; «не» belongs to na)

## Answers and frame words
Āmantā = да; No = нет; Natthi = такого нет (YM has нет: overridden); na = не
Yattha = где («Где не прекращается …»); yatthakaṃ = раздел с «где» («(раздел с «где» следует изложить полностью)»)
ṭhapetvā = кроме; avasesā = остальной («остальное»); Avasesā khandhā = остальные совокупности
(no direct equivalent) as a listed keyword = (no direct equivalent) (kept as listed; same as G8)

## Planes (pavatti persons / places; the plane forms -aṃ / -e / -ā = the plane, -ānaṃ = its beings)
Pañcavokāraṃ / Pañcavokāre / Pañcavokārā = существование с пятью составляющими («перерождается / умирает в существовании …», «В существовании …: там»)
Pañcavokārānaṃ = существа с пятью составляющими («У существ с пятью составляющими»)
catuvokāra- = существование с четырьмя составляющими; -ānaṃ = существа с четырьмя составляющими (prepared, build_2-01 PLANES)
ekavokāra- = существование с одной составляющей; -ānaṃ = существа с одной составляющей (prepared)
Arūpaṃ / Arūpe / Arūpā = мир без форм («в мире без форм»); Arūpānaṃ = существа мира без форм
Asaññasattaṃ / Asaññasatte / Asaññasattā / Asaññasattānaṃ = существа без восприятия («среди существ без восприятия»)
Suddhāvāsaṃ / Suddhāvāse = Чистые обители («в Чистых обителях»); Suddhāvāsānaṃ = существа Чистых обителей
(arūpā / arūpaṃ as «нематериальный» outside the person / place frames is NOT covered: decide per segment)

## Persons
upapajjantānaṃ = перерождаться («у тех, кто перерождается»; pi-2 / pi-5 upapajjati)
cavantānaṃ = умирать («кто умирает», «когда они умирают»)
parinibbantānaṃ / Parinibbantānaṃ = достигать окончательного угасания
parinibbāyissanti = достигнуть окончательного угасания («достигнет …»; presence exception, self-checked)
upapajjitvā = переродившись (gerund the text uses)
Itaresaṃ = остальной («У остальных», as avasesā); sabbesaṃ = все («У всех, кто …»; prepared)
Pacchimabhavikānaṃ = жить последней жизнью («у тех, кто живёт последней жизнью»)
Pacchimabhavikānaṃ before [Xaṃ] upapajjantānaṃ = в последний раз («кто (в последний раз) перерождается (в последний раз)»; pacchima_value decides by the exact-case Pāli occurrences)

## Pariññā frame
parijānāti / parijānātīti / parijānanti = полностью понимать (pi-5)
parijānittha / parijānitthāti = полностью понять («полностью понял / поняли», perfective)
parijānissati / parijānissatīti / parijānissanti = полностью понять («полностью поймёт / поймут»; presence exception, self-checked)
parijān- where the segment has that form only negated («не понимают полностью») = понимать полностью / понять полностью (Russian word order; pj_value; ^6-2-209, ^6-2-210 parijānanti)
parijān- after a separate «na» = the positive verb (the «не» belongs to na)
Arahā / arahantañca = архат (pi-5); Aggamaggasamaṅgī / Aggamaggasamaṅgiñca = обладающий высшим путём
puggalā = личности («остальные личности»); puthujjanā = обычные люди («те обычные люди, которые …»)
maggaṃ paṭilabhissanti = обрести путь; paṭilabhissanti = обрести («обретёт / обретут»; presence exception, self-checked)

## Headings and colophons (lower-case first letter, label / number dropped)
paṇṇattivāro = раздел об обозначениях; paṇṇattivāraniddesa = разъяснение раздела об обозначениях
paṇṇattiuddesavāro = раздел перечня обозначений; paṇṇattiniddesavāro = раздел разъяснения обозначений
padasodhanavāro = раздел уточнения слов; padasodhanamūlacakkavāro = круговой раздел на основе уточнения слов
anulomaṃ = утвердительная форма; paccanīkaṃ = отрицательная форма
anulomapuggalo / anulomaokāso / anulomapuggalokāsā = утвердительная форма по личности / по месту / по личности и месту
paccanīkapuggalo / paccanīkaokāso / paccanīkapuggalokāsā = отрицательная форма по личности / по месту / по личности и месту
pavattivāro = раздел о протекании; pavatti = протекание («Протекание 2. Раздел о прекращении»)
uppādavāro / uppādavāre = раздел о возникновении; nirodhavāro = раздел о прекращении; uppādanirodhavāro = раздел о возникновении и прекращении
atītānāgatavāro = раздел о прошлом и будущем; pariññāvāro = раздел о полном понимании
uddeso = перечень; niddeso = разъяснение (YM)

## Khandha members (G2_KHANDHA; chapter-specific)
khandhayamakaṃ / khandhayamakapāḷi = парные вопросы о совокупностях
suddhakhandhavāro = раздел о совокупностях как таковых; suddhakhandhamūlacakkavāro = круговой раздел на основе совокупностей как таковых
Pañcakkhandhā = пять совокупностей; khandho / khandhoti = совокупность; khandhā / khandhe = совокупности
rūpaṃ / rūpanti / Rūpañca / rūpañceva = форма (paṇṇattivāra bare word «Форма является …», incl. piyarūpa; not «материальная форма»)
vedanā / Vedanaṃ / Vedanañca = чувство; saññā / Saññaṃ / Saññañca = восприятие; saṅkhārā / Saṅkhāre = формирующие факторы; viññāṇaṃ / Viññāṇañca = сознание
X-kkhandho / -kkhandhaṃ / -kkhandhoti / -kkhandhañca = совокупность материальной формы / чувств / восприятия / формирующих факторов / сознания (pi-2); vadanākkhandho (^6-2-185 slip) = совокупность чувств
Diṭṭhisaññā = восприятие-воззрение
