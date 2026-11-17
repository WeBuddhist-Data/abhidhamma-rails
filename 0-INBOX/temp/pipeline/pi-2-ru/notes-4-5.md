# pi-2 Russian zero-shot, chapters 4 (Saccavibhaṅga) and 5 (Indriyavibhaṅga): new terms and formulas

Builder: build_4_5_ru.py (imports build_ch1_sample_ru as S, build_1_ru as B, build_2_3_ru as T; extends T.SUBJ2 / T.ITEMS2 in memory only). Extra checks: check_4_5_ru.py. Scratch lookup: probe_4_5_ru.py.
Format: Pāli = Russian, one per line. [pi-1] = from the pi-1 Russian (block ID given, asserted in the builder); [pi-3] / [pi-5] = from those books; [new] = settled here.

## Truths
ariyasacca = благородная истина [pi-5]
Cattāri ariyasaccāni – … = Четыре благородные истины – благородная истина о страдании, благородная истина о возникновении страдания, благородная истина о прекращении страдания и благородная истина о способе практики, ведущем к прекращению страдания [new; pi-5 words, paṭipadā pi-1]
dukkhanirodhagāminī paṭipadā = способ практики, ведущий к прекращению страдания [pi-1 ^1-1238 amoho list «знание способа практики, ведущего к прекращению страдания»; pi-5 had «практика»]
Cattāri saccāni – dukkhaṃ, dukkhasamudayo, dukkhanirodho, dukkhanirodhagāminī paṭipadā = Четыре истины – страдание, возникновение страдания, прекращение страдания и способ практики, ведущий к прекращению страдания [new]
##### Dukkhasaccaṃ / Samudayasaccaṃ / Nirodhasaccaṃ / Maggasaccaṃ = Истина о страдании / Истина о возникновении страдания / Истина о прекращении страдания / Истина о пути [pi-3, samudaya = возникновение]; the same as Pañhāpucchaka subjects (feminine: B.ITEMS sg forms; acc «Истину о …»)
Dve saccā / Tīṇi saccāni = Две истины / Три истины [new]
Catunnaṃ ariyasaccānaṃ kati …? = Сколько из четырёх благородных истин являются благими, …? [T.how_many_q]

## Suttanta: suffering
Jātipi dukkhā … saṃkhittena pañcupādānakkhandhā dukkhā = И рождение является страданием, и старение является страданием, и смерть является страданием, и печаль, стенания, боль, уныние и отчаяние являются страданием, соединение с неприятным является страданием, разлука с приятным является страданием, и неполучение желаемого тоже является страданием, короче говоря, пять совокупностей, служащих объектом цепляния, являются страданием [new]
sokaparidevadukkhadomanassupāyāsā = печаль, стенания, боль, уныние и отчаяние [pi-1 termbase soka, parideva; dukkha here = боль (^2-196 = dukkhindriya)]
pañcupādānakkhandhā = пять совокупностей, служащих объектом цепляния; rūpupādānakkhandho = совокупность материальной формы, служащая объектом цепляния [new; pi-1 upādāniya «служащий объектом цепляния»]
saṃkhittena = короче говоря [new]
appiyehi sampayogo dukkho = соединение с неприятным, которое является страданием [new]
piyehi vippayogo dukkho = разлука с приятным, которая является страданием [new]
yampicchaṃ na labhati tampi dukkhaṃ = неполучение желаемого, которое тоже является страданием [new]
tesaṃ tesaṃ sattānaṃ tamhi tamhi sattanikāye = у тех или иных существ в том или ином классе существ [new; S.SELF_WHO]
jāti sañjāti okkanti abhinibbatti khandhānaṃ pātubhāvo āyatanānaṃ paṭilābho = рождение, зарождение, вхождение, появление, проявление совокупностей, обретение сфер восприятия [new]
jarā … indriyānaṃ paripāko = старение, одряхление, сломанные зубы, седые волосы, морщинистая кожа, сокращение срока жизни, изношенность способностей [pi-1 ^1-643]
cuti cavanatā bhedo antaradhānaṃ maccu maraṇaṃ kālakiriyā khandhānaṃ bhedo kaḷevarassa nikkhepo jīvitindriyassupacchedo = уход из того или иного класса существ, выбывание, распад, исчезновение, гибель, смерть, кончина, распад совокупностей, оставление тела, прекращение жизненной способности [new]
Ñātibyasanena vā phuṭṭhassa … aññataraññatarena dukkhadhammena phuṭṭhassa = У того, кого постигло несчастье с родными, или постигло несчастье с имуществом, или постигло несчастье болезни, или постигло несчастье в нравственности, или постигло несчастье в воззрениях, у того, кто охвачен тем или иным несчастьем, кого коснулось то или иное болезненное явление, есть … [new; byasana = несчастье]
soko socanā socitattaṃ antosoko antoparisoko cetaso parijjhāyanā domanassaṃ sokasallaṃ = печаль, горевание, состояние горевания, внутренняя печаль, глубокая внутренняя печаль, изнурение ума, уныние, стрела печали [new]
ādevo paridevo ādevanā paridevanā ādevitattaṃ paridevitattaṃ vācā palāpo vippalāpo lālappo lālappanā lālappitattaṃ = плач, стенания, оплакивание, причитание, состояние плача, состояние стенаний, речь, болтовня, бессвязная болтовня, сетование, проявление сетования, состояние сетования [new]
āyāso upāyāso āyāsitattaṃ upāyāsitattaṃ = удручённость, отчаяние, состояние удручённости, состояние отчаяния [new; upāyāsa отчаяние pi-3/pi-5]
anatthakāmā ahitakāmā aphāsukakāmā ayogakkhemakāmā = (те, кто) желает ему вреда, желает ему неблага, желает ему неудобства, желает ему лишиться безопасности [new]
atthakāmā hitakāmā phāsukakāmā yogakkhemakāmā = желает ему пользы, желает ему блага, желает ему удобства, желает ему безопасности [new; yogakkhema plain «безопасность», pi-5 verse «свобода от уз» not used]
saṅgati samāgamo samodhānaṃ missībhāvo = встреча, общение, соединение, смешение; a- = отсутствие встречи, отсутствие общения, несоединение, несмешение [new]
mātā vā pitā vā bhātā vā bhaginī vā mittā vā amaccā vā ñātī vā sālohitā vā = мать, или отец, или брат, или сестра, или друзья, или сотоварищи, или родственники, или кровные родные [new]
X-dhammānaṃ sattānaṃ evaṃ icchā uppajjati – "aho vata, mayaṃ na X-dhammā assāma; na ca, vata, no X āgaccheyyā"ti! = У существ, подверженных X, возникает такое желание – «О, если бы мы не были подвержены X; и пусть бы X не приходило к нам»! [new]
Na kho panetaṃ icchāya pattabbaṃ. = Но этого не достичь желанием. [new]
Idampi "yampicchaṃ na labhati tampi dukkhaṃ". = Это тоже «неполучение желаемого, которое тоже является страданием». [new]

## Suttanta: origin and cessation (craving)
yāyaṃ taṇhā ponobbhavikā nandirāgasahagatā tatratatrābhinandinī = та жажда, ведущая к новому существованию, сопровождаемая наслаждением и страстью, находящая радость то здесь, то там [pi-5 ^5-679]
kāmataṇhā, bhavataṇhā, vibhavataṇhā = чувственная жажда, жажда существования, жажда несуществования [pi-1 ^1-1065; pi-5 had «жажда чувственных удовольствий»]
rūpataṇhā … dhammataṇhā = жажда видимых форм … жажда объектов ума [pi-1 ^1-1065]
piyarūpaṃ sātarūpaṃ (loke) = (в мире) является привлекательным и отрадным (f: привлекательной и отрадной; pl: являются привлекательными и отрадными) [new; pi-5 piyarūpa «привлекательный», sāta pi-1 «отрада»]
Sā kho panesā taṇhā kattha uppajjamānā uppajjati, kattha nivisamānā nivisati? = А где эта жажда, возникая, возникает, где, укореняясь, укореняется? [new]
Etthesā taṇhā uppajjamānā uppajjati, ettha nivisamānā nivisati. = Там эта жажда, возникая, возникает, там, укореняясь, укореняется. [new]
Etthesā taṇhā pahīyamānā pahīyati, ettha nirujjhamānā nirujjhati. = Там эта жажда, устраняясь, устраняется, там, прекращаясь, прекращается. [new]
Kiñca loke piyarūpaṃ sātarūpaṃ? = А что в мире является привлекательным и отрадным? [new]
rūpasaññā / rūpasañcetanā / rūpavitakko / rūpavicāro = восприятие видимых форм / намерение в отношении видимых форм / направленная мысль о видимых формах / удержание мысли на видимых формах [new]
Yo tassāyeva taṇhāya asesavirāganirodho cāgo paṭinissaggo mutti anālayo = То, что есть угасание без остатка и прекращение этой самой жажды, отказ от неё, оставление её, освобождение от неё, отсутствие привязанности к ней [new]

## Suttanta: path
Ayameva ariyo aṭṭhaṅgiko maggo, seyyathidaṃ – … = Это именно благородный восьмичастный путь, а именно – … [pi-1 «восьмичастный путь» ^1-337; pi-3 had «восьмеричный»]
pañcaṅgiko maggo = пятичастный путь [pi-1 ^1-58]
Dukkhe ñāṇaṃ … paṭipadāya ñāṇaṃ = Знание страдания, знание возникновения страдания, знание прекращения страдания, знание способа практики, ведущего к прекращению страдания [pi-1 amoho]
Nekkhammasaṅkappo, abyāpādasaṅkappo, avihiṃsāsaṅkappo = Помысел об отречении, помысел об отсутствии недоброжелательности, помысел об отсутствии жестокости [new; ch. 3 words]
veramaṇī = уклонение [pi-1 termbase]; Musāvādā / pisuṇāya vācāya / pharusāya vācāya / samphappalāpā veramaṇī = Уклонение от лжи / от речи, сеющей раздор / от грубой речи / от пустой болтовни [pi-4 words]
Pāṇātipātā / adinnādānā / kāmesumicchācārā veramaṇī = Уклонение от убийства живых существ / от взятия того, что не дано / от неправильного поведения в чувственных удовольствиях [pi-5 words; kāma pi-1 «чувственные удовольствия»]
Idha ariyasāvako micchāājīvaṃ pahāya sammāājīvena jīvikaṃ kappeti = Вот благородный ученик, устранив неправильный образ жизни, поддерживает жизнь правильным образом жизни [new; ariyasāvaka pi-5]
Idha bhikkhu anuppannānaṃ … padahati = pi-1 ^1-1377 verbatim, one sentence per effort [pi-1]
Idha bhikkhu kāye kāyānupassī viharati ātāpī sampajāno satimā, vineyya loke abhijjhādomanassaṃ = Вот монах пребывает в теле, созерцая тело, ревностный, ясно понимающий, осознанный, устранив алчность и уныние в отношении мира [new; pi-5 «в теле пребывает, созерцая тело»; ātāpī «ревностный» to keep vīriya «усердие» apart]
Sutta jhāna formula (Idha bhikkhu vivicceva kāmehi … catutthaṃ jhānaṃ upasampajja viharati) = pi-1 ^1-160 and the following second/third/fourth-jhāna lines, without «со всеохватным объектом земли» [pi-1]

## Abhidhammabhājanīya (ch. 4)
Idha bhikkhu yasmiṃ samaye lokuttaraṃ jhānaṃ bhāveti … dukkhapaṭipadaṃ dandhābhiññaṃ, tasmiṃ samaye = Вот в то время, когда монах развивает надмирское медитативное погружение, … и пребывает в нём, в это время … [pi-1 ^1-277, «кто-либо» -> «монах»]
aṭṭhaṅgiko maggo hoti – sammādiṭṭhi…pe… sammāsamādhi = есть восьмичастный путь – правильное воззрение… правильное сосредоточение [pi-1 words]
phasso hoti…pe… avikkhepo hoti = есть контакт… есть отсутствие отвлечения [pi-1]
Path-factor definitions = pi-1 ^1-297 … ^1-304 without «в это время» [pi-1]
Avasesā dhammā dukkhanirodhagāminiyā paṭipadāya sampayuttā. = Остальные явления связаны со способом практики, ведущим к прекращению страдания. [new]
avasesā kilesā / avasesā akusalā dhammā = остальные омрачения / остальные неблагие явления [new]
tīṇi kusalamūlāni sāsavāni = три благих корня, подверженные влечениям [pi-1 ^1-985 words]
avasesā sāsavā kusalā dhammā = остальные подверженные влечениям благие явления [pi-1 ^1-1113 order]
sāsavā kusalākusalānaṃ dhammānaṃ vipākā = подверженные влечениям результаты благих и неблагих явлений [new]
ye ca dhammā kiriyā neva kusalā nākusalā na ca kammavipākā, sabbañca rūpaṃ = и те функциональные явления, ни благие, ни неблагие и не являющиеся результатом действий, и вся материальная форма [pi-1 ^1-583]
"X ca, Y ca …" lists = «И X, и Y, …» (first item capitalised); "Taṇhā ca avasesā ca kilesā" = Жажда и остальные омрачения
Taṇhāya ca, avasesānañca kilesānaṃ … pahānaṃ = Устранение и жажды, и остальных омрачений, … [new]; Taṇhāya pahānaṃ = Устранение жажды

## Faculties (ch. 5) [pi-1 names]
Bāvīsatindriyāni = Двадцать две способности [pi-3]; Bāvīsatīnaṃ indriyānaṃ = из двадцати двух способностей
anaññātaññassāmītindriya / aññindriya / aññātāvindriya = способность познания непознанного / способность окончательного знания / способность обладателя окончательного знания [pi-1]
rūpajīvitindriya / arūpajīvitindriya = материальная жизненная способность / нематериальная жизненная способность [new]
Jīvitindriyaṃ duvidhena – atthi X, atthi Y = Классификация жизненной способности на два вида – есть X, есть Y [new, ch. 1 frame]
manindriya classification = ch. 2 manāyatana classification with «способности ума» (T.man_chunk) [ch. 2]
Yaṃ cakkhu catunnaṃ mahābhūtānaṃ upādāya pasādo…pe… suñño gāmopeso = Глаз, который является чувствительностью, производной от четырёх великих элементов… это пустая деревня [ch. 3]
itthindriya / purisindriya / jīvitindriya / saddhā / vīriya / sati / samādhi / paññā bodies = pi-1 ^1-714, ^1-716, ^1-718, ^1-19, ^1-12 … ^1-16 without «в это время» and without the pi-1 variants [pi-1]
thāmo ṭhiti (pi-2; pi-1 thāmo dhiti) = стойкость, устойчивость [as written; pi-1 «стойкость, твёрдость»]
Yā tesaṃ dhammānaṃ aññātāvīnaṃ diṭṭhānaṃ … sacchikiriyāya = То, что для непосредственного постижения тех явлений, которые обладают окончательным знанием, увидены, достигнуты, узнаны и постигнуты непосредственно, [new; pi-1 aññātāvin «обладающий окончательным знанием»]
Subjects: Dvindriyā / Tīṇindriyā / Cattārindriyā = Две / Три / Четыре способности; Pañcindriyā … Aṭṭhārasindriyā = Пять … Восемнадцать способностей; Ekavīsatindriyā = Двадцать одна способность (singular predicate) [new]

## Pañhāpucchaka additions
ācayagāmi / apacayagāmi / nevācayagāmināpacayagāmi (short -i) = as -ī [B.ITEMS]
maggādhipatī (quoted) = «явление, находящееся под главенством пути» [B.ITEMS]
arūpāni = являются нематериальными [B.ITEMS]
na maggārammaṇaṃ = не имеет объектом путь; na maggahetukaṃ = не имеет корнем путь; na appamāṇārammaṇaṃ = не имеет безмерного объекта [new]
"X na Y" (siyā mahaggatārammaṇaṃ na appamāṇārammaṇaṃ; na maggārammaṇaṃ maggahetukaṃ) = two predicates joined by a comma, as B piti_only [new]
Bare predicates without subject ("Sappaccayā. Saṅkhatā. Anidassanā.", "No āsavā.") = plural predicate, capitalised: «Имеют условия. Являются обусловленными. Являются невидимыми.», «Не являются влечениями.» [B.LABELS «Имеют условия, являются обусловленными.»]

## Pāli slips (all reported; words translated as written unless noted)
^2-218 "Dve saccā nīvaraṇiyā dve saccā anīvaraṇiyā." (full stop missing): two sentences.
^2-218 "siyā araṇanti." (closing "ti" of the question): «иногда свободна от борьбы.»
^2-218 "…sampayuttañcā" tipi" ×2 (space): punctuation only.
^2-218 "Dukkhasaccaṃ siyā ajjhattaṃ, siyā bāhiraṃ" (the ajjhattika/bāhira pair; ajjhattaṃ perhaps for ajjhattikaṃ): as written, «иногда является внутренней, иногда относится к внешнему».
^2-218 "Samudayasaccaṃ na vattabbaṃ – "parāmāso ceva parāmaṭṭhañcā"ti, parāmaṭṭhañceva no ca parāmāso." and the ch. 5 clusters "– "X"ti, Y." / "– "X"ti, "Y".": Y as an affirmative, unquoted (as ch. 1–3).
^2-206 "aṭṭhaṅgiko maggo hoti sammādiṭṭhi…" (no dash, the later repeats have one): a colon.
^2-220 "arūpajīvatindriyaṃ": spelling slip, rendered as meant (нематериальной жизненной способностью).
^2-220 aññindriya: answer "idaṃ vuccati aññindriyaṃ." without quotes: as written, unquoted.
^2-220 vīriyindriya "thāmo ṭhiti" (pi-1 "thāmo dhiti"; also ch. 9): as written, «устойчивость».
^2-223 "siyā parittārammaṇaṃ siyā mahaggatārammaṇaṃ, na appamāṇārammaṇaṃ" (comma missing); ""mahaggatārammaṇa"nti pi" (space): punctuation only.
^2-223/224 "Tīṇindriyā na vattabbā – "hetū ceva sahetukā cā"ti. Sahetukā ceva na ca hetū." (a full stop where the clusters have a comma): two sentences, the second without a subject.
^2-224 ""gantho ceva ganthasampayutta"ñcāti" (quote closed too early): punctuation only.
^2-224 "Navindriyā … siyā upādāniyā ceva no ca upādānā. Dasindriyā siyā upādāniyā ceva no ca upādānā, siyā na vattabbā …" (the numbers look shifted against the parallel clusters): as written.
