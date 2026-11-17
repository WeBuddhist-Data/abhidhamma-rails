# pi-2 Russian zero-shot, chapters 10 (Bojjhaṅga), 11 (Maggaṅga), 12 (Jhāna): new terms and formulas

Builder: build_10_12_ru.py (imports build_ch1_sample_ru as S, build_1_ru as B, build_2_3_ru as T, build_4_5_ru as F, build_6_ru as G, build_7_9_ru as Z; extends T.SUBJ2 / T.SURF2 / T.PRON in memory only). Extra checks: check_10_12_ru.py. Scratch: probe_10_12.py, probe_10_12b.py, lookup_10_12.py (pi-N Pāli + aligned Russian lookup).
Format: Pāli = Russian, one per line. [pi-1] = from the pi-1 Russian (asserted in the builder); [pi-4] = pi-4 Russian (asserted); [ch4] … [ch9] = earlier pi-2 groups; [new] = settled here.

## Reused
Path-factor bodies (…maggaṅgaṃ maggapariyāpannaṃ), Suttanta path definitions (sammādiṭṭhi … sammāājīvo) = ch4 F.FACTOR_BODY / F.sutta4 [pi-1 ^1-297 …]
Yā micchāājīvā ārati … (pi-2 ch. 11 spelling) = ch4 «То, что есть отстранение от неправильного образа жизни, …» (ch. 4 has "micchā ājīvā")
Four efforts, satipaṭṭhāna phrases = ch7/ch8 (Z.efforts, Z.dwell, Z.SATI_TAIL)
Jhāna formula = ch4 F.JH1 … F.JH4 [pi-1 ^1-160 …]; lokuttara opening / vipāka = ch7-9 Z.LOK_R / Z.VIP_R [pi-1 ^1-277, ^1-505]
rūpāvacara / arūpāvacara / kiriya openings = ch6 G.RUPA_K, G.RUPA_V, G.RUPA_F, G.ARUPA_K, G.ARUPA_V, G.ARUPA_F with «кто-либо» -> «монах» [pi-1 ^1-499, ^1-577, 2-04/2-05]
vitakkavicārānaṃ vūpasamā…pe… dutiyaṃ jhānaṃ…pe… … pañcamaṃ jhānaṃ = с затиханием направленной мысли и удержания мысли… второе медитативное погружение… … входит в пятое медитативное погружение [pi-1 2-02]
pañcaṅgikaṃ / caturaṅgikaṃ / tivaṅgikaṃ / duvaṅgikaṃ jhānaṃ = пятичастное / четырёхчастное / трёхчастное / двухчастное медитативное погружение [pi-1]
vitakko, vicāro, pīti, sukhaṃ, cittassekaggatā = направленная мысль, удержание мысли, восторг, счастье, однонаправленность ума [pi-1 ^1-83]
Definitions [pi-1]: vitakka ^1-7, vicāra ^1-8, pīti ^1-9 (+ pītisambojjhaṅgo ^1-285), sati ^1-14, paññā ^1-16, saddhā, saññā ^1-61, passaddhi ^1-40/41 words, thina ^1-1162, middha ^1-1163, uddhacca, kukkucca ^1-1166, vicikicchā, byāpāda (dosa list ^1-1066 without «такая»), ākāsa ^1-637, citta / rāga (ch6)
Sense restraint and moderation in food = pi-1 ^1-1352 … ^1-1355 (answer term quoted, as the pi-2 Pāli)
Kāyiko (a)vītikkamo … = нарушение телом … / отсутствие нарушений телом … [pi-1 ^1-1368, ^1-1370]
sampajānakārī situations (abhikkante paṭikkante …) = pi-4 ^4-182 Russian [pi-4]; «садится, скрестив ноги, держа тело прямо, установив осознанность перед собой» [pi-4]
cittacetasikā dhammā = ум и сопутствующие уму явления [pi-1 ^1-1029]
etthuppannaṃ X ṭhapetvā = кроме возникшего в них / в нём X [pi-1 ^1-1387 …]
Arūpa terms: sabbaso rūpasaññānaṃ samatikkamā = с полным преодолением восприятий материальной формы; paṭighasaññānaṃ atthaṅgamā = с исчезновением восприятий соударения; nānattasaññānaṃ amanasikārā = без внимания к восприятиям разнообразия; ākāsānañcāyatana / viññāṇañcāyatana / ākiñcaññāyatana / nevasaññānāsaññāyatana = сфера бесконечного пространства / бесконечного сознания / отсутствия чего-либо / ни восприятия, ни невосприятия [pi-1 ^1-265 …]
Headings: Rūpāvacarakusalaṃ = Благой ум, относящийся к миру форм; Arūpāvacarakusalaṃ = … к миру без форм; Lokuttarakusalaṃ = Надмирский благой ум; Rūpāvacaravipākā / Arūpāvacaravipākā = Результаты действий, относящиеся к миру форм / без форм [pi-1]; Mātikā = Матрица [pi-1, ch6]
Catukkaṃ. / Pañcakaṃ. (after the jhāna series) = Четверичный метод. / Пятеричный метод. [pi-1 Catukkanayo / Pañcakanayo]
rūpasaññā saddasaññā … phoṭṭhabbasaññā = восприятие видимых форм, восприятие звуков… восприятие осязаемого [ch4]

## Chapter 10
Satta bojjhaṅgā = Семь факторов пробуждения (list with «и» before the last, T.enum) [new; factor names pi-1 / ch7]
upekkhāsambojjhaṅga = фактор пробуждения невозмутимости [ch7]
satimā hoti paramena satinepakkena samannāgato = осознан, наделён высшей осознанностью и благоразумием [new; nepakka = благоразумие]
cirakatampi cirabhāsitampi saritā hoti anussaritā = он помнит и припоминает и то, что сделано давно, и то, что сказано давно [new]
paññāya pavicinati pavicarati parivīmaṃsamāpajjati = с помощью мудрости исследует …, обдумывает его, подвергает его всестороннему изучению [new]
āraddhaṃ hoti vīriyaṃ asallīnaṃ = у него пробуждено неослабное усердие [new]
pīti nirāmisā = неплотский восторг [ch7 nirāmisa]
kāyopi passambhati, cittampi passambhati = утихает и тело, утихает и ум [new; pi-1 passambhanā «утихание»]
Passaddhakāyassa sukhino cittaṃ samādhiyati = У счастливого, чьё тело безмятежно, ум сосредотачивается [new]
samāhitaṃ cittaṃ sādhukaṃ ajjhupekkhitā hoti = На так сосредоточенный ум он хорошо взирает с полной невозмутимостью [new]
ajjhattaṃ / bahiddhā dhammesu sati = осознанность в отношении внутренних / внешних явлений [new]; pavicayo = тщательное исследование [pi-1]
kāyikaṃ / cetasikaṃ vīriyaṃ = телесное / душевное усердие [new]
kāyapassaddhi / cittapassaddhi = безмятежность умственного тела / безмятежность ума [pi-1]
Yadapi A tadapi X abhiññāya sambodhāya nibbānāya saṃvattati = И A является X(ins) и ведёт к высшему знанию, к полному пробуждению, к нирване [new]
vivekanissitaṃ virāganissitaṃ nirodhanissitaṃ vossaggapariṇāmiṃ = опирающийся на уединение, опирающийся на бесстрастие, опирающийся на прекращение, ведущий к отказу (agreeing: -ее, -ую) [new]
Yā upekkhā upekkhanā ajjhupekkhanā majjhattatā cittassa = То, что есть невозмутимость, проявление невозмутимости, полная невозмутимость, уравновешенность ума [new; not in pi-1]
passaddhi body (four aggregates) = То, что у совокупности чувств, совокупности восприятия, совокупности формирующих факторов и совокупности сознания есть безмятежность, полная безмятежность, утихание, полное утихание, состояние полного утихания [new, pi-1 words]
Ime vuccanti (")satta bojjhaṅgā(") = Это называется («)семью факторами пробуждения(») [new]
Avasesā dhammā sattahi bojjhaṅgehi / X-sambojjhaṅga- sampayuttā = Остальные явления связаны с семью факторами пробуждения / с фактором пробуждения X [new, ch4 frame]
tasmiṃ samaye satta bojjhaṅgā honti – … = в это время есть семь факторов пробуждения – … [new]
Pañhāpucchaka subjects: Pītisambojjhaṅgo / Dhammavicayasambojjhaṅgo = Фактор пробуждения восторга / исследования явлений (masc. predicates via T.masc); cha bojjhaṅgā = шесть факторов пробуждения; Sattannaṃ bojjhaṅgānaṃ = семи факторов пробуждения [new]

## Chapter 11
Ariyo aṭṭhaṅgiko maggo, seyyathidaṃ – … = Благородный восьмичастный путь, а именно – … (no «и», as ch4/pi-1) [ch4]
Aṭṭhaṅgiko / Pañcaṅgiko maggo – … = Восьмичастный / Пятичастный путь – … [pi-1 nominatives]
aṭṭhaṅgiko / pañcaṅgiko maggo (ins) = восьмичастным путём / пятичастным путём [new]
sammāsamādhi Suttanta without the dash before "upekkhako" = «так что благородные говорят о нём: «Невозмутимый, …»» (colon, dash rule) [new]
sammādiṭṭhiṃ bhāveti vivekanissitaṃ … = развивает правильное воззрение, опирающееся на уединение, … (правильную речь / правильную осознанность: опирающуюся …) [new]
Subjects: Sammāsaṅkappo = Правильный помысел (masc.); Sammādiṭṭhi = Правильное воззрение (neuter predicates: T.masc + short forms -о); satta maggaṅgā = семь факторов пути; Aṭṭhannaṃ maggaṅgānaṃ = восьми факторов пути [new]

## Chapter 12 Suttanta (word commentary)
Format: '"X"ti rest' = «X»: rest; '"X"nti.' = «X».; 'Tena vuccati "X"ti.' = Поэтому и говорится: «x». [ch7 format; colon new]
Idha (^2-508 and its lemma ^2-509) = Здесь (the commentary glosses idha as "in this teaching"); elsewhere Idha bhikkhu = Вот монах [new]
pātimokkha = свод монашеских правил; pātimokkhasaṃvarasaṃvuto = сдержанный сдержанностью свода монашеских правил; saṃvara = сдержанность; saṃyama = обуздание [new]
ācāra / anācāra = подобающее / неподобающее поведение; gocara / agocara = подходящее / неподходящее место посещения; ācāragocarasampanno = обладающий подобающим поведением и подходящими местами посещения [new]
Sabbampi dussīlyaṃ anācāro = Всякая безнравственность является неподобающим поведением; Sabbopi sīlasaṃvaro ācāro = Всякая нравственная сдержанность является подобающим поведением [pi-1 ^1-1368/1370 frame]
Idhekacco = Вот человек [pi-1]; jīvikaṃ kappeti = поддерживает жизнь [ch4]; buddhapaṭikuṭṭha micchāājīva = неправильный образ жизни, порицаемый Буддой [new]
aṇumattesu vajjesu bhayadassāvī = видящий опасность в малейших проступках; vajja/bhaya/ādīnava/nissaraṇa-dassāvī = видит проступок / опасность / вред / выход [new]
samādāya sikkhati sikkhāpadesu = принимает на себя правила обучения и обучается им; sikkhā / sikkhāyo = обучение / виды обучения [new]
indriyesu guttadvāro / (a)guttadvāratā = охраняющий врата чувств / (не)охранение врат чувств [pi-1, pi-4]
bhojane mattaññū / (a)mattaññutā = знающий меру в еде / (не)знание меры в еде [pi-1, pi-4]
pubbarattāpararattaṃ jāgariyānuyogamanuyutto = в начале и в конце ночи преданный бодрствованию [new]; āvaraṇīyā dhammā = явления, создающие препятствия [new]
sātaccaṃ = постоянство [pi-1 sātacca]; nepakkaṃ = благоразумие [new]
bodhipakkhikā dhammā = явления, способствующие пробуждению [new]
sampajānakārī = действует с ясным пониманием [pi-4]; sato sampajāno abhikkamati = осознанно и с ясным пониманием идёт вперёд [new]
vivittaṃ senāsanaṃ bhajati = выбирает уединённое жилище [pi-4]; senāsana = жилище [pi-4/pi-5]; rukkhamūla = подножие дерева [new; pi-4 «корни дерева»]
appasadda / appanigghosa / vijanavāta / manussarāhasseyyaka / paṭisallānasāruppa = тихое / бесшумное / лишённое людской суеты / укрытое от людей / подходящее для уединения [new]
vanapattha = лесная чаща [pi-4]; adhivacana = наименование [pi-1]
upeto hoti samupeto…pe… samannāgato = он обладает, вполне обладает… наделён [new, ch7 frame]
abhijjhaṃ loke pahāya = оставив алчность в отношении мира [pi-4 «оставив»; ch7 «в отношении мира»]
byāpādapadosa = недоброжелательность и сильная злоба (padosa = сильная злоба, as in the pi-1 dosa list) [new]
abyāpannacitto = с умом, свободным от недоброжелательности; vigatābhijjhena cetasā = с умом, свободным от алчности [new]
sabbapāṇabhūtahitānukampī = сострадая всем живым существам и желая им блага [pi-4 words]
vigatathinamiddho = свободный от вялости и сонливости; ālokasaññī = воспринимающий свет [pi-4]
anuddhato = без беспокойства [pi-4]; (ajjhattaṃ) vūpasantacitto = с (успокоенным) умом, успокоенным внутри [new]
tiṇṇavicikiccho = преодолевший колебание; akathaṃkathī = свободный от недоумений (kathaṃkathā = недоумение; nikkathaṃkathī = полностью свободен от недоумений; vikathaṃkatho = избавлен от недоумений) [new; pi-4 used «сомнение» for vicikicchā, not taken]
cittaṃ parisodheti / sodheti visodheti parisodheti moceti vimoceti parimoceti = очищает ум / очищает, тщательно очищает, полностью очищает, освобождает, тщательно освобождает, полностью освобождает [new]
santā hoti/honti samitā vūpasantā atthaṅgatā abbhatthaṅgatā appitā byappitā sositā visositā byantīkatā = успокоен(а/о/ы), усмирён, умиротворён, угас, полностью угас, прекращён, полностью прекращён, иссушен, полностью иссушен, сведён на нет (by gender) [ch7 Z.VINITA words]
cattattā vantattā muttattā pahīnattā paṭinissaṭṭhattā pahīnapaṭinissaṭṭhattā = оставлены, извергнуты, отпущены, устранены, отброшены, устранены и отброшены [new]
upakkilesa = загрязнение; paññāya dubbalīkaraṇa = ослабляющие мудрость [pi-4]
Chando kāmo, rāgo kāmo … = Чувственным удовольствием является желание, … (kāma kept as in the jhāna formula, «чувственные удовольствия») [new]
jātā honti sañjātā nibbattā abhinibbattā pātubhūtā = родились, зародились, возникли, полностью возникли, проявились [new]
sahagataṃ hoti sahajātaṃ saṃsaṭṭhaṃ sampayuttaṃ = сопровождается, рождено вместе с ним, соединено с ним, связано с ним [new]
gaṇanānupubbatā paṭhamaṃ; idaṃ paṭhamaṃ samāpajjatīti paṭhamaṃ = первое по порядку счёта; в него он входит первым, поэтому оно первое [new]
lābho paṭilābho patti sampatti phusanā sacchikiriyā upasampadā = обретение, получение, достижение, полное достижение, касание, непосредственное постижение, вхождение [ch9]
upasampajja (lemma) = входит; vivekaja / samādhija (lemma) = рождённые уединением / рождённые сосредоточением [pi-1 formula words]
yo cāro anucāro vicāro … = движение мысли, последовательное движение мысли, удержание мысли, … (anucāra new) [pi-1 + new]
sukhaṃ / dukkhaṃ in ^2-594 (bodily, after sukhassa ca pahānā dukkhassa ca pahānā) = приятное / болезненное (as the lemma); elsewhere sukhaṃ = счастье [pi-1 formula]
Tattha katamo kāyo? Saññākkhandho, saṅkhārakkhandho, viññāṇakkhandho = Что такое здесь тело? Совокупность восприятия, … [new]
Tattha katame ariyā? = Кто здесь благородные?; Ariyā vuccanti buddhā ca buddhasāvakā ca = Благородными называются будды и ученики будд [new]
ācikkhanti desenti paññapenti paṭṭhapenti vivaranti vibhajanti uttāniṃ karonti pakāsenti = говорят, излагают, сообщают, устанавливают, раскрывают, разбирают, проясняют, разъясняют [new]
ālokā / vivaṭā parisuddhā pariyodātā = светлое, открытое, чистое, ясное [new]
atikkanto hoti vītikkanto samatikkanto = преодолел, миновал, полностью преодолел [new]
samāpannassa vā upapannassa vā diṭṭhadhammasukhavihārissa vā = того, кто вошёл …, или того, кто переродился в ней (в мире форм), или того, кто пребывает в ней в счастье в этой жизни [new; pi-1 diṭṭhadhammasukhavihāra «для пребывания в счастье в этой жизни»]
"ananto ākāso"ti = с мыслью «Пространство бесконечно»; "anantaṃ viññāṇa"nti = с мыслью «Сознание бесконечно»; "natthi kiñcī"ti = с мыслью «Нет ничего» [new]
nevasaññīnāsaññī = ни воспринимающий, ни невоспринимающий; saṅkhārāvasesasamāpatti = медитативное достижение с остатком формирующих факторов [new]
[ayaṃ pāṭho mātikāyaṃ natthi, niddese pana sabbapotthakesu dissati] = [этого чтения нет в матрице, но в разъяснении оно встречается во всех рукописях]

## Chapter 12 Abhidhamma / Pañhāpucchaka
Cattāri jhānāni – paṭhamaṃ jhānaṃ, … = Четыре медитативных погружения – первое медитативное погружение, …, и четвёртое медитативное погружение (T.enum) [new]
Idaṃ vuccati "paṭhamaṃ jhānaṃ" = Это называется «первым медитативным погружением» [new]; Avasesā dhammā jhānasampayuttā = Остальные явления связаны с медитативным погружением [new]
Lokuttaravipākā = Надмирские результаты действий; Rūpārūpāvacarakiriyā = Функциональный ум, относящийся к миру форм и к миру без форм [new, pi-1 heading words]
vivicceva kāmehi vivicca akusalehi dhammehi avitakkaṃ vicāramattaṃ vivekajaṃ pītisukhaṃ dutiyaṃ jhānaṃ = полностью уединившись от чувственных удовольствий, уединившись от неблагих явлений, входит во второе медитативное погружение, без направленной мысли, только с удержанием мысли, с восторгом и счастьем, рождёнными уединением [new, pi-1 pieces]
Subjects: Tīṇi / Dve jhānāni = Три / Два медитативных погружения; Paṭhamaṃ / Catutthaṃ jhānaṃ = Первое / Четвёртое медитативное погружение (neuter; a plural Pāli predicate after it switches back to the plural, as the Pāli); Catunnaṃ jhānānaṃ = четырёх медитативных погружений [new]
X – etthuppannaṃ Y ṭhapetvā Z = X – кроме возникшего в них / в нём Y, Z [new; pi-1 «кроме возникшего в них …»]
Quoted "na vattabbā "…"ti" without a dash (ch. 12 Dukaṃ) = их нельзя определить как «…» (no dash) [new]

## Variant brackets
odagyaṃ [odaggaṃ (sī.) dha. sa. 9] = воодушевление [вариант написания (Sī.): odaggaṃ; dha. sa. 9]
kāyapassaddhi [kāyappassaddhi (syā. ka.)], cittapassaddhi [cittappassaddhi (syā. ka.)] = [вариант написания (Syā., Ka.): …]
samiñjite [sammiñjite (sī. syā.)] = сгибая [вариант написания (Sī., Syā.): sammiñjite]
manussarāhasseyyakaṃ [manussarāhaseyyakaṃ (sī. syā.)], bibbohanampi [bimbohanampi (sī. syā.)], bhīsanakānametaṃ [bhiṃsanakānametaṃ (sī. syā.)], paññapenti [paññāpenti (sī. syā.)], thinaṃ [thīnaṃ (sī. syā.)], thiyanā thiyitattaṃ [thīyanā thīyitattaṃ (sī. syā.)], dussanā dussitattaṃ [dūsanā dūsitattaṃ (syā.)], muggasūpyatāya [muggasuppatāya (sī.)] = вариант написания
pāde pādaṃ [pādena pādaṃ (syā.)] = положив ступню на ступню [вариант чтения (Syā.): pādena pādaṃ]
gaṇanānupubbatā [gaṇanānupubbato (syā.) evamuparipi] = по порядку счёта [вариант написания (Syā.): gaṇanānupubbato; так же и далее]

## Pāli slips and as-written readings (all reported)
Rendered as meant (spelling / punctuation only): ^2-478 "kāmehi …pe…", ^2-481 "sampayuttā …pe…", ^2-550 "anussati …pe…", ^2-554 / ^2-571 … "Viharatī"ti …pe…, ^2-628 "pahānā …pe…", ^2-634 "jhānaṃ …pe…" (stray spaces); ^2-485 "Anāsavā āsavavippayuttā." (comma added); ^2-508 "ākiñcāyatanaṃ" (= ākiñcaññāyatanaṃ); ^2-517 "Ñatvādhikaraṇamenaṃ" (= Yatvādhikaraṇamenaṃ); ^2-640 "maggahetukantipi maggādhipatītipi" (comma), "paccuppannāramaṇantipi"; ^2-641 '"āsavā ceva āsavasampayuttā cāti"pi' (quote placement), "āsavavippayuttā sāsavā / anāsavā" (two words); ^2-629 "caturaṅgikaṃ jhānaṃ hoti vicāro pīti sukhaṃ cittassekaggatā" (no dash, no commas: colon and commas in Russian); closing "ti" dropped in ^2-518 "bhojane amattaññutā"ti, ^2-637 "jhānasampayuttāti", "Araṇāti."
As written: ^2-478 "yo tasmiṃ samaye phasso hoti…pe… avikkhepo hoti – ime dhammā kusalā" (the parallels: "tasmiṃ samaye … hoti. Ime dhammā kusalā.") = «то, что в это время есть контакт… есть отсутствие отвлечения, – это благие явления»; ^2-474 "Ime vuccanti satta bojjhaṅgā" unquoted (^2-479 quoted); ^2-481 first vipāka without "suññataṃ"; ^2-485 "Āsavā ceva āsavasampayuttā cātipi, …" without "na vattabbā" = «Ни как «…», ни как «…»»; ^2-523 a bare "sato sampajānakārī hoti" after "pasāreti", and ^2-525 the last clause without "sato"; ^2-560 vicikicchā list "kaṅkhā kaṅkhāyanā kaṅkhāyitattaṃ chambhitattaṃ cittassa manovilekho" (short, no …pe…); ^2-564 "rāgo kāmo" twice; ^2-565 "ayaṃ vuccati vicāro" and ^2-603 "imā vuccanti paṭighasaññāyo" unquoted; ^2-576 "cāro anucāro vicāro" (anucāro only here) and "santā hoti" with two subjects (Russian plural); ^2-598 comma instead of a full stop; ^2-641 "tīṇi jhānāni upekkhāsahagatā" (the sense needs "na upekkhāsahagatā"; translated as written: «три медитативных погружения сопровождаются невозмутимостью»).
