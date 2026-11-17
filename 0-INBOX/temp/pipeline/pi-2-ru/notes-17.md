# pi-2 Russian zero-shot, chapter 17 (Khuddakavatthuvibhaṅga): new terms and formulas

Builder: build_17_ru.py (imports build_ch1_sample_ru as S and build_4_5_ru as F; asserts reused strings against pi-1 / pi-4 / pi-2 ch1-16; reads the ch12 Russian line for sense restraint). Helpers: lookup_17.py (Pāli regex -> full aligned lines in pi-1..5 and pi-2 ch1-16), dump_17.py (aligned dump of one split file).
Format: Pāli = Russian, one per line. [pi-1] / [pi-4] / [pi-5] = those books; [chN] = earlier pi-2 groups; [new] = settled here.

## Reused (verbatim, asserted)
lobha list = pi-1 ^1-1141 with the pi-2 differences (sotaṃ «течение» for pi-1 suttaṃ «нить»; jappā abhijappā jappanā jappitattaṃ = «тяга, чрезмерная тяга, проявление тяги, состояние тяги»; order saddataṇhā rūpataṇhā kept) [pi-1]
dosa (āghāta sentences + list), moha, kāmāsava, bhavāsava, diṭṭhāsava, avijjāsava, kāmupādāna … attavādupādāna, sakkāyadiṭṭhi, vicikicchā, sīlabbataparāmāsa, issā, macchariya, māna string, thina = pi-1 4-01 / 4-02 [pi-1]
bhava/vibhava/sassata/uccheda/antavā/anantavā/pubbanta/aparantadiṭṭhi, ahirika, anottappa, dovacassatā, pāpamittatā, sīlavipatti, diṭṭhivipatti, muṭṭhassacca, asampajañña, bhojane amattaññutā = pi-1 4-03 ^1-1320 … ^1-1369, with the pi-2 quoted answer «это называется «X»» [pi-1, ch2-3 frame]
kodha = pi-1 ^1-1066 tail (kodho … anattamanatā cittassa) [pi-1; pi-4 «ненависть» not taken]
upanāha, makkha, paḷāsa, māyā, sāṭheyya bodies = pi-4 ^4-46 … ^4-52 [pi-4]
indriyesu aguttadvāratā = ch12 line (identical Pāli) [ch12]; byāpāda / vihiṃsā list = ch3 [ch3]; uddhacca = ch12; avijjā = ch6; somanassa/domanassa vedanā strings = ch12 ^2-567 / ^2-595; upekkhā vedanā = pi-1 ^1-152 [pi-1]
jhāna formulas (abbreviated) = ch4 F.JH1 … F.JH4; arūpa phrases = ch12 [ch4, ch12]
kilesavatthu (8/10), anusaya, saṃyojana, nīvaraṇa, sakkāya/vicikicchā/sīlabbata names = ch16 / pi-1 [ch16, pi-1]
lapanā: cāṭukamyatā / muggasūpyatā / pāribhaṭayatā = «лесть / угодничество / нянченье чужих детей» [ch12 ^2-512]

## New
mada = опьянение; majjanā / majjitattaṃ = упоение / состояние упоения; jātimado … pāripūrimado = опьянение рождением, родом, здоровьем, молодостью, жизнью, приобретениями, почестями, уважением, первенством, окружением, богатством, красотой, учёностью, находчивостью, старшинством, тем, что питается подаянием, тем, что его не презирают, манерой держаться, сверхспособностью, славой, нравственностью, медитативным погружением, ремеслом, ростом, дородностью, телосложением, безупречностью тела
X-ṃ paṭicca (mada, bhaya) = из-за X (gen.)
pamāda = беспечность [ch14]; kosajja = лень; cittassa vossaggo vossaggānuppadānaṃ = распущенность ума, постоянное потакание распущенности; asakkacca- / asātacca- / anaṭṭhitakiriyatā = нетщательность / непостоянство / прерывистость действий (pi-1 ^1-1379 negated)
thambha = строптивость (not «упрямство», which pi-1 uses for dovacassiyaṃ); sārambha = задиристость; kakkhaḷiya / phārusiya / kakkhaḷatā / kaṭhinatā / ujucittatā = чёрствость / резкость / очерствелость / жёсткость / несгибаемость ума
atricchatā / mahicchatā / pāpicchatā = чрезмерные / большие / дурные желания [pi-4 pāpiccha «имея дурные желания»]; icchā icchāgatā = желание, охваченность желанием; asantuṭṭhassa bhiyyokamyatā = желание большего у того, кто не доволен [pi-1 ^1-1378]
itarītara-cīvara…parikkhāra = теми или иными одеждой, пищей из подаяний, жилищем, лекарствами и всем необходимым для больных [pi-4 words]
siṅga = щегольство; tintiṇa = привередливость; cāpalya = легкомыслие; asabhāgavutti = несогласное поведение; arati = неудовлетворённость; tandī = апатия; vijambhitā = потягивание; bhattasammada = осоловелость после еды; cetaso (ca) līnattaṃ = косность ума (pi-1 līnaṃ «косность»)
kuhanā / lapanā / nemittikatā / nippesikatā = лицемерие / заискивание / намёки / очернение; lābhena lābhaṃ nijigīsanatā = добывание приобретений приобретениями; lābhasakkārasilokasannissita pāpiccha icchāpakata = привязан к приобретениям, почестям и славе, имеет дурные желания и одолеваем желаниями
seyyo / sadiso / hīno-hamasmīti māno = самомнение «я лучше» / «я равный» / «я хуже» [pi-1]; seyyassa … māno = самомнение «я лучше» у того, кто лучше (… у того, кто равен / хуже)
omāna = самоуничижение (string: проявление самоуничижения, состояние самоуничижения, умаление себя, принижение себя, состояние принижения себя, пренебрежение собой, презрение к себе, унижение себя); atimāna = высокомерие; mānātimāna = нарастающее самомнение; adhimāna = переоценка себя; asmimāna = самомнение «я есть»; micchāmāna = ложное самомнение
jāti / gotta / kolaputtiya / vaṇṇapokkharatā / dhana / ajjhena / kammāyatana / sippāyatana / vijjāṭṭhāna / suta / paṭibhāna / aññataraññatara vatthu = рождение / род / знатность семьи / красота внешности / богатство / изучение текстов / занятие / ремесло / наука / учёность / находчивость / что-либо иное («из-за …» gen., «по …» dat.)
vitakka (in names) = мысль: ñāti- / janapada- / amara-vitakko = мысль о родственниках / о родной стране / о бессмертии; kāma- / byāpāda- / vihiṃsāvitakko = мысль о чувственных желаниях / о недоброжелательности / о жестокости [pi-5]; takko vitakko micchāsaṅkappo = мышление, направленная мысль, ложный помысел [pi-1]; gehasita = связанный с мирской жизнью
anajjava = отсутствие прямодушия; amaddava = отсутствие мягкости; akkhanti = нетерпение; asoracca = отсутствие кротости; asākhalya = неприветливость; appaṭisanthāra = отсутствие радушия (pi-1 positives negated)
ajjhatta- / bahiddhāsaṃyojana = внутренние / внешние оковы; orambhāgiya / uddhambhāgiya = низшие / высшие оковы [pi-4]
tisso esanā = три вида поиска (поиск чувственных удовольствий / существования / духовной жизни); vidhā = сравнение себя; tamāni = мрак; titthāyatana = сфера сектантских учений [pi-1]; kiñcana = обременение; aṅgaṇa = пятно; mala = скверна; visama = порочность; kasāva = нечистота
rūpa- / arūpadhātu (realm) = элемент мира форм / мира без форм; rūpa- / arūpataṇhā (realm) = жажда мира форм / мира без форм [pi-1 lobha list]
assāda- / attānu-diṭṭhi = воззрение о наслаждении / о наличии самости (sakkāyadiṭṭhi stays «воззрение о самости»)
vihesā = причинение мучений; adhammacariyā(visamacariyā) = неправедное (порочное) поведение; nānattasaññā = восприятие разнообразия [ch12]
anādariya = непочтительность; assaddhiya = отсутствие веры; avadaññutā = нещедрость; asaṃvara = несдержанность; dussīlya = безнравственность [pi-1]
ariyānaṃ adassanakamyatā / saddhammaṃ asotukamyatā / upārambhacittatā = нежелание видеть благородных / нежелание слушать истинное Учение / придирчивость ума; kummaggasevanā = следование кривой дорогой (kummagga pi-1 «кривая дорога»)
ayoniso manasikāra = неразумное внимание; vipariyāsa = превратность («принятие непостоянного за «постоянное»»)
taṇhuppāda = повод для возникновения жажды; agatigamana = следование неправедным путём; anariyavohāra = неблагородное высказывание
saṅga / salla = привязанность / стрела; cetokhila = огрубение ума; cetaso vinibandha = путы ума; vera = враждебность; byasana = несчастье [ch4]; akkhantiyā ādīnava = вред от нетерпения
diṭṭhadhammanibbānavāda = учение о нирване в этой жизни; bho = почтенный; evaṃvādī evaṃdiṭṭhī = придерживается такого учения, такого воззрения
vivādamūla = корень споров; chandarāga = страстное желание [ch12]; virodhavatthu = повод для вражды; taṇhākāya = группа жажды; agārava = неуважение; parihāniya dhamma = явление, ведущее к упадку; (somanassa-…)upavicāra = задерживание ума (вызывающий радость / уныние / невозмутимость); gehasita somanassa = радость, связанная с мирской жизнью
asaddhamma = недоброе качество; pariyuṭṭhāna = одержимость [pi-5]; kusītavatthu = повод для лени; lokadhamma = мирское явление; micchatta = вид ложности; purisadosa = недостаток человека; asaññī- / nevasaññīnāsaññīvāda = учение о невоспринимающем / о ни воспринимающем, ни невоспринимающем
āghātavatthu = повод для досады [ch3]; purisamala = скверна человека; taṇhāmūlaka dhamma = явление, коренящееся в жажде; iñjita / maññita / phandita / papañcita / saṅkhata = волнение / измышление / трепетание / разрастание мысли / построение; akusalakammapatha = неблагой путь действия; dasavatthukā (antaggāhikā) diṭṭhi = (держащееся крайностей) воззрение о десяти предметах
taṇhāvicarita = блуждание жажды; ajjhattikassa / bāhirassa upādāya = в связи с внутренним / с внешним; asmi, itthasmi, evasmi, aññathāsmi, bhavissaṃ…, asasmi, sātasmi, siyaṃ…, apāhaṃ siyaṃ… = я есть, я таков, я такой же, я иной, я буду…, я вечен, я преходящ, я мог бы быть…, пусть бы я был…; iminā = благодаря этому; (an)avakāriṃ karitvā = (не) разделяя; X-ti hoti = появляется мысль «X»; papañcita = разрастание мысли
khattiya / brāhmaṇa / vessa / sudda = кшатрий / брахман / вайшья / шудра; gahaṭṭha / pabbajita = домохозяин / ушедший в бездомность [ch12]
dvāsaṭṭhi diṭṭhigatāni brahmajāle veyyākaraṇe = шестьдесят два воззрения, о которых Благословенный сказал в наставлении «Сеть Брахмы»; sassatavāda … amarāvikkhepika … adhiccasamuppannika = учения о вечности … уклонения от ответа … о случайном возникновении
Lists "X, Y, Z – these are N …" are rendered without «и» before the last item (pi-1 style).

## Variant brackets
[uṇṇati uṇṇāmo (syā. ka.) dha. sa. 1121] = [вариант написания (Syā., Ka.): uṇṇati uṇṇāmo; dha. sa. 1121]; [visadā (sī. ka.) dha. sa. 1141] = [вариант чтения …; dha. sa. 1141]; [paggahitattaṃ (sī. ka.) dha. sa. 1127] = [вариант чтения …]
[palāsāyanā palāsāyitattaṃ (syā.)] = [вариант чтения (Syā.): …] (it adds a word); [cetaso līnattaṃ (syā.)], [paccayapaṭisedhanasaṅkhātena (sī.)], [cetasovinibaddhā (ka.)], [codakasseva (syā.) a. ni. 8.14], [āpattikova (ka.) a. ni. 8.14] = вариант чтения
[katamāni tīṇi kiñcanāni (?) dī. ni. 3.305] = [вариант чтения (?): katamāni tīṇi kiñcanāni; dī. ni. 3.305]
[gilānavuṭṭhito (saddanībhi) a. ni. 6.16 pāḷiyā ṭīkā passitabbā] = [вариант написания (saddanī): gilānavuṭṭhito; a. ni. 6.16; следует свериться с подкомментарием к тексту]
[kumbhīrabhayaṃ, kumbhīḷabhayaṃ (?) (kumbha + īra + a = bhaya)] = [вариант написания (?): kumbhīrabhayaṃ, kumbhīḷabhayaṃ (kumbha + īra + a = bhaya)]
( ) [(tattha katamā bhavataṇhā)] = ( ) [(что такое здесь жажда существования)] (editorial note translated)
All other brackets: вариант написания.

## Pāli slips and as-written readings (all reported)
Rendered as meant (spelling / punctuation only): ^2-933 "bhavantattaṃ" (= bhantattaṃ, «взбудораженность ума»); ^2-919 (Ka)-(Ga) second set "tattha katamā kāmesanā, kāmarāgo, …" (question mark missing); ^2-905 `"bhojane amattaññutā."` (full stop inside the quote); ^2-U23 commas "vossaggo, vossaggānuppadānaṃ kusalānaṃ dhammānaṃ, bhāvanāya …" rendered as ^2-U14; ^2-U55 "arahanto jīvitā voropito" (= arahā); ^2-957 (Ja) "byāvaṭā." rendered as a question; internal (7) "evaṃ bhavissanti hoti" (the parallel (13) has "evaṃ evaṃ siyanti") = «так появляется мысль «я буду таким же»».
As written: ^2-909 lobha "sotaṃ" (pi-1 suttaṃ «нить») = «течение»; "saddataṇhā rūpataṇhā" order; ^2-877 "hīnassa hīnohamasmīti" with "parehi sadisaṃ attānaṃ dahati" = «считает себя равным другим»; ^2-892 paḷāsa string lacks "paḷāsāyitattaṃ" (only in the Syā. variant); ^2-896 (Kha) "ayaṃ vuccati vibhavadiṭṭhi" unquoted; ^2-919 (Ga) dash in `"asassato loko"ti – vā…pe…` kept («или «мир не вечен» – или…»); ^2-943 (Ṅa) "sukhapīti cetaso ābhogo" (DN 1 has "sukhamiti") = «счастье и восторг, вовлечённость ума»; ^2-951 (Cha) "atthi kho pana eso attā" (no "bho") = «Есть же та самость»; the onefold matrix "(51) hīno hamasmīti" (space).
Unsure: amaravitakka «мысль о бессмертии» (the commentary links it also to the eel-wriggling views; English rails "thought about dying"); asasmi «я вечен» / sātasmi «я преходящ» (following their definitions); vidhā «сравнение себя»; cetokhila «огрубение ума»; visama «порочность»; kasāva «нечистота»; paccayapaṭisevanasaṅkhāta «так называемое пользование необходимым» (as written; Sī. paṭisedhana «отказ»).
Review: kāmesumicchācāra here «неправильное поведение в чувственных удовольствиях» (ch4, ch11, pi-5); ch14 has «неподобающее поведение» in the precept names.
