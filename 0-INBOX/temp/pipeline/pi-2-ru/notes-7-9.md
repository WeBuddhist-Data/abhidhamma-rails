# pi-2 Russian zero-shot, chapters 7 (Satipaṭṭhāna), 8 (Sammappadhāna), 9 (Iddhipāda): new terms and formulas

Builder: build_7_9_ru.py (imports build_ch1_sample_ru as S, build_1_ru as B, build_2_3_ru as T, build_4_5_ru as F, build_6_ru as G; extends T.SUBJ2 / T.ITEMS2 in memory only). Extra checks: check_7_9_ru.py. Scratch: probe_7_9_ru.py, probe_7_9_q.py.
Format: Pāli = Russian, one per line. [pi-1] = from the pi-1 Russian (asserted in the builder); [ch3] / [ch4] / [ch5] / [ch6] = earlier pi-2 groups; [new] = settled here.

## Reused
Cattāro sammappadhānā – idha bhikkhu … padahati = Четыре правильных усилия – вот монах ради невозникновения … прилагает старания; ради устранения …; … [pi-1 ^1-1377 via F.SP / F.SP_EFFORT]
ātāpī sampajāno satimā vineyya loke abhijjhādomanassaṃ = ревностный, ясно понимающий, осознанный, устранив алчность и уныние в отношении мира [ch4 F.SATI_TAIL]
kāye kāyānupassī viharati = пребывает в теле, созерцая тело (vedanāsu … чувствах, созерцая чувства; citte … в уме, созерцая ум; dhammesu … в явлениях, созерцая явления) [ch4]
Idha bhikkhu yasmiṃ samaye lokuttaraṃ jhānaṃ bhāveti … dukkhapaṭipadaṃ dandhābhiññaṃ = Вот в то время, когда монах развивает надмирское медитативное погружение, … и пребывает в нём [pi-1 ^1-277, ch4 F.LOKUTTARA]
Tasseva lokuttarassa kusalassa jhānassa katattā bhāvitattā vipākaṃ … suññataṃ = Вследствие того же совершённого и развитого надмирского благого медитативного погружения, в качестве его результата, когда монах, … пустое, и пребывает в нём [pi-1 ^1-505, «кто-либо» -> «монах» as ch4]
tasmiṃ samaye phasso hoti…pe… avikkhepo hoti. Ime dhammā kusalā. = в это время есть контакт… есть отсутствие отвлечения. Это благие явления. [ch4 / pi-1]
Path-factor bodies with …bojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ = ch4 F.FACTOR_BODY (pi-1 ^1-297, ^1-302, ^1-304)
Yā paññā pajānanā…pe… amoho dhammavicayo sammādiṭṭhi = То, что есть мудрость, понимание… отсутствие заблуждения, исследование явлений, правильное воззрение [ch5]
vīriya full list (… thāmo ṭhiti … vīriyabalaṃ sammāvāyāmo) = ch5 F.VIRIYA_B (pi-1 ^1-13; «стойкость, устойчивость»)
samādhi full list = ch5 F.SAMADHI_B (pi-1 ^1-15); Yā cittassa ṭhiti saṇṭhiti…pe… sammāsamādhi = То, что есть устойчивость ума, собранность… правильное сосредоточение
Yā sati anussati…pe… sammāsati = То, что есть осознанность, припоминание… правильная осознанность [pi-1 ^1-14 words]
Yo rāgo sārāgo…pe… cittassa sārāgo = То, что есть страсть, пристрастие… пристрастие ума [ch6]
Yaṃ cittaṃ mano mānasaṃ…pe… tajjāmanoviññāṇadhātu = То, что есть ум, разум, умственная деятельность… соответствующий элемент умственного сознания [ch6]
Yaṃ cetasikaṃ asātaṃ … cetosamphassajā asātā dukkhā vedanā = То, что есть душевная безотрадность, душевная боль, … [pi-1 ^1-415, ch3]
kesā lomā … mutta(ṃ) = волосы на голове, волосы на теле, … кал, желчь, слизь, … моча [ch3 T.LISTS pathavī/āpo internal]
Tīṇi akusalamūlāni – lobho, doso, moho. Tadekaṭṭhā ca kilesā. = Три неблагих корня – жадность, злоба, заблуждение. И омрачения, пребывающие вместе с ними. [pi-1 ^1-986]
Taṃsampayutto vedanākkhandho … taṃsamuṭṭhānaṃ kāyakammaṃ vacīkammaṃ manokammaṃ = Связанные с ними совокупность чувств, … и совокупность сознания; порождённые ими телесное действие, речевое действие и умственное действие [pi-1 ^1-985]
Tīṇi kusalamūlāni – alobho, adoso, amoho = Три благих корня – отсутствие жадности, отсутствие злобы, отсутствие заблуждения [pi-1 ^1-985]
pañcupādānakkhandhā = пять совокупностей, служащих объектом цепляния [ch4]
tadekajjhaṃ abhisaññūhitvā abhisaṅkhipitvā = всё вместе, собранное воедино и обобщённое [ch1 S.KHANDHA_TOGETHER n]
Tena vuccati "…"ti = Поэтому и говорится: «…» [ch6]; lemma "X"ti / Xti alone = «X». [ch6]
kāmacchanda = чувственное желание; byāpāda = недоброжелательность; thinamiddha = вялость и сонливость; uddhaccakukkucca = беспокойство и угрызения; vicikicchā = колебание [pi-1]
satisambojjhaṅga … samādhisambojjhaṅga = фактор пробуждения осознанности / исследования явлений / усердия / восторга / безмятежности / сосредоточения [pi-1]
chanda / vīriya / citta / vīmaṃsā = желание / усердие / ум / пытливость [pi-1 …ādhipateyya, termbase vīmaṃsā]
iddhi = сверхспособность; iddhipāda = основа сверхспособностей [pi-1 termbase, pi-5]
paggāho = напряжение сил [pi-1]

## Satipaṭṭhāna (ch. 7)
Cattāro satipaṭṭhānā = Четыре основы осознанности
ajjhattaṃ / bahiddhā / ajjhattabahiddhā kāye kāyānupassī viharati = пребывает во внутреннем / во внешнем / во внутреннем и внешнем теле, созерцая тело (чувствах, уме, явлениях accordingly) [new; ajjhatta pi-2 terms «внутренний»]
… dandhābhiññaṃ kāye kāyānupassī (no viharati, Abhidhamma) = … и пребывает в нём, в теле созерцая тело [new]
Kāyānupassanāniddeso / Vedanā… / Cittā… / Dhammā… = Разъяснение созерцания тела / чувств / ума / явлений [new; niddeso ch6]
anupassī / anupassanā = созерцая / созерцание [new]
viharati = пребывает; Iriyati vattati pāleti yapeti yāpeti carati viharati = Он принимает положения тела, живёт, оберегает себя, поддерживает себя, продлевает существование, действует, пребывает [new]
ātāpī / ātāpo = ревностный / ревностность [new; ussāha in the vīriya list stays «рвение»]
sampajāno / sampajaññaṃ = ясно понимающий / ясное понимание [pi-1, pi-4]
satimā = осознанный [ch4]
Imāya X-āya upeto hoti samupeto upāgato samupāgato upapanno sampanno samannāgato = Этим X-ом он обладает, вполне обладает, снабжён, вполне снабжён, обеспечен, оснащён, наделён [new]; …upeto hoti…pe… samannāgato = он обладает… наделён
uddhaṃ pādatalā adho kesamatthakā tacapariyantaṃ pūraṃ nānappakārassa asucino paccavekkhati = рассматривает … от подошв ног вверх и от кончиков волос на голове вниз, ограниченное кожей и полное разного рода нечистот [new]
atthi imasmiṃ kāye / atthissa kāye = В этом теле есть / В его теле есть [new]
So taṃ nimittaṃ āsevati bhāveti bahulīkaroti svāvatthitaṃ vavatthapeti = Этот признак он практикует, развивает, многократно повторяет, чётко устанавливает [new; nimitta pi-1 «признак»]
āsevitvā bhāvetvā bahulīkaritvā svāvatthitaṃ vavatthapetvā X cittaṃ upasaṃharati = После того как он практиковал этот признак, развил, многократно повторил и чётко установил его, он направляет ум на X [new]
Te dhamme āsevati bhāveti bahulīkaroti = Эти явления он практикует, развивает, многократно повторяет [new]
sāmisa / nirāmisa (vedanā) = плотский / неплотский [new]
sukhaṃ vedanaṃ vedayamāno "sukhaṃ vedanaṃ vedayāmī"ti pajānāti = испытывая приятное чувство, понимает: «Я испытываю приятное чувство» [new]
… vedayamānaṃ "… vedayatī"ti pajānāti = о том, кто испытывает …, понимает: «Он испытывает …» [new]
sukhaṃ vedanaṃ "sukhā vedanā"ti pajānāti = приятное чувство понимает как «приятное чувство» [new]
sarāgaṃ vā cittaṃ "sarāgaṃ me citta"nti pajānāti = когда ум охвачен страстью, понимает: «Мой ум охвачен страстью» (vāssa … "…massa citta" = когда ум кого-то …: «Его ум …»; both = «Ум …») [new]
sarāga / vītarāga, sadosa / vītadosa, samoha / vītamoha = охвачен страстью / свободен от страсти, охвачен злобой / свободен от злобы, охвачен заблуждением / свободен от заблуждения [new; vīta- pi-5]
saṃkhitta / vikkhitta = сжат / рассеян; mahaggata / amahaggata = возвышен / невозвышен; sauttara / anuttara = имеет над собой высшее / не имеет над собой высшего; samāhita / asamāhita = сосредоточен / несосредоточен; vimutta / avimutta = освобождён / неосвобождён [new; pi-1 mahaggata, anuttara]
santaṃ vā ajjhattaṃ X "atthi me ajjhattaṃ X"ti pajānāti = когда внутри него есть X, понимает: «Внутри меня есть X» (asantaṃ: нет X gen; vāssa / atthissa: у кого-то / «У него есть»; both: когда есть X / «Есть X») [new]
yathā ca anuppannassa X uppādo hoti tañca pajānāti = понимает и то, как происходит возникновение невозникшего X [new]
yathā ca uppannassa X pahānaṃ hoti … = понимает и то, как происходит устранение возникшего X [new]
yathā ca pahīnassa X āyatiṃ anuppādo hoti … = понимает и то, как в будущем не происходит возникновения устранённого X [new]
yathā ca uppannassa X bhāvanāya pāripūrī hoti … = понимает и то, как происходит завершённость развития возникшего X [new]
upekkhāsambojjhaṅga = фактор пробуждения невозмутимости [new; not in pi-1]
loko = мир; abhijjhā = алчность; domanassaṃ = уныние [ch4]
Sveva kāyo / Sāyeva vedanā / Taṃyeva cittaṃ / Teva dhammā loko = Само это тело / Само это чувство / Сам этот ум / Сами эти явления является (являются) миром [new]
Pañcapi upādānakkhandhā loko = И пять совокупностей, служащих объектом цепляния, являются миром [new]
Iti ayañca abhijjhā idañca domanassaṃ imamhi loke vinītā honti paṭivinītā santā samitā vūpasantā atthaṅgatā abbhatthaṅgatā appitā byappitā sositā visositā byantīkatā = Таким образом, и эта алчность, и это уныние в этом мире устранены, полностью устранены, успокоены, усмирены, умиротворены, угасли, полностью угасли, прекращены, полностью прекращены, иссушены, полностью иссушены, сведены на нет [new]
Avasesā dhammā satipaṭṭhānasampayuttā = Остальные явления связаны с основой осознанности [ch4 frame]
Catunnaṃ satipaṭṭhānānaṃ kati …? = Сколько из четырёх основ осознанности являются благими, …? [T.how_many_q]

## Sammappadhāna (ch. 8)
Cattāro sammappadhānā / sammappadhānaṃ = Четыре правильных усилия / правильное усилие [pi-1 APPROVED]
chandaṃ janeti / vāyamati / vīriyaṃ ārabhati / cittaṃ paggaṇhāti / padahati = порождает желание / прилагает усилие / пробуждает усердие / напрягает ум / прилагает старания [pi-1 ^1-1377]
chando = желание; vāyāmo = усилие; vīriyaṃ = усердие; cittaṃ = ум; padhānaṃ = усилие (core rule vīriya ≠ padhāna/vāyāma)
anuppannā / uppannā pāpakā akusalā dhammā = невозникшие / возникшие дурные неблагие явления; anuppannā / uppannā kusalā dhammā = невозникшие / возникшие благие явления [pi-1 ^1-1377 words]
Iti imesaṃ anuppannānaṃ … padahati = Таким образом, ради невозникновения этих невозникших дурных неблагих явлений он порождает желание, … [new]
Yo chando chandikatā kattukamyatā kusalo dhammacchando = То, что есть желание, проявление желания, желание действовать, благое стремление к Учению [new]
Imaṃ chandaṃ janeti sañjaneti uṭṭhapeti samuṭṭhapeti nibbatteti abhinibbatteti = Это желание он порождает, полностью порождает, поднимает, полностью поднимает, вызывает, полностью вызывает [new]
Imaṃ vīriyaṃ ārabhati samārabhati āsevati bhāveti bahulīkaroti = Это усердие он пробуждает, полностью пробуждает, практикует, развивает, многократно повторяет [new]
Imaṃ cittaṃ paggaṇhāti sampaggaṇhāti upatthambheti paccupatthambheti = Этот ум он напрягает, полностью напрягает, поддерживает, всячески поддерживает [new]
Ṭhitiyāti = «Ради сохранения»; Yā ṭhiti so asammoso, … yā bhāvanā sā pāripūrī = То, что есть сохранение, есть неутрата; то, что есть неутрата, есть умножение; … то, что есть развитие, есть завершённость [new; pi-1 words]
Abhidhamma: …, tasmiṃ samaye <effort> = …, в это время он ради … порождает желание, … [new]
Avasesā dhammā sammappadhānasampayuttā = Остальные явления связаны с правильным усилием

## Iddhipāda (ch. 9)
Cattāro iddhipādā = Четыре основы сверхспособностей
chandiddhipādo / vīriyiddhipādo / cittiddhipādo / vīmaṃsiddhipādo = желание / усердие / ум / пытливость как основа сверхспособностей (ins: желанием как основой сверхспособностей …) [new; also the ##### headings]
chandasamādhi = сосредоточение через желание (усердие, ум, пытливость) [new]
padhānasaṅkhāro / padhānasaṅkhārā = формирующий фактор усилия / формирующие факторы усилия [new; saṅkhāra pi-5, padhāna = усилие]
chandasamādhipadhānasaṅkhārasamannāgataṃ iddhipādaṃ bhāveti = развивает основу сверхспособностей, наделённую сосредоточением через желание и формирующим фактором усилия [new]
Chandaṃ ce bhikkhu adhipatiṃ karitvā labhati samādhiṃ, labhati cittassekaggataṃ – ayaṃ vuccati "chandasamādhi" = Если монах, сделав желание главенствующим, обретает сосредоточение, обретает однонаправленность ума, – это называется «сосредоточением через желание» [new; cittekaggatā pi-1]
So anuppannānaṃ … padahati = Он ради невозникновения … прилагает старания; … [pi-1 ^1-1377]
Iti ayañca chandasamādhi, ime ca padhānasaṅkhārā = Таким образом, есть и это сосредоточение через желание, и эти формирующие факторы усилия [new; ch6 frame]
tadekajjhaṃ abhisaññūhitvā abhisaṅkhipitvā chandasamādhipadhānasaṅkhārotveva saṅkhyaṃ gacchati = всё вместе, собранное воедино и обобщённое, получает название «сосредоточение через желание и формирующий фактор усилия» [new]
Tena vuccati "chandasamādhipadhānasaṅkhārasamannāgato"ti = Поэтому и говорится: «наделённый сосредоточением через желание и формирующим фактором усилия» [new]
Iti iminā ca chandena, iminā ca samādhinā, iminā ca padhānasaṅkhārena upeto hoti … = Таким образом, и этим желанием, и этим сосредоточением, и этим формирующим фактором усилия он обладает, … [new]
Iddhīti. Yā tesaṃ dhammānaṃ iddhi samiddhi ijjhanā samijjhanā lābho paṭilābho patti sampatti phusanā sacchikiriyā upasampadā. = «Сверхспособность». То, что у этих явлений есть сверхспособность, успех, преуспевание, полное преуспевание, обретение, получение, достижение, полное достижение, касание, непосредственное постижение, вхождение. [new]
Iddhipādoti. Tathābhūtassa … = «Основа сверхспособностей». У того, кто таков, это … [new]
Iddhipādaṃ bhāvetīti = «Развивает основу сверхспособностей» [new]

## Pañhāpucchaka additions
Kusalāyeva = Являются только благими [new]
na maggādhipatino = не находятся под главенством пути [new]
Unquoted, dashless "na vattabbā X(n)ti(pi), Y(n)ti(pi)" (ch. 7–9 only) = «(иногда) их нельзя определить (ни) как «X», (ни как «Y»)» without the dash; «их» when the sentence has no subject; quote forms as B/T [new]
Subjects: Vīmaṃsiddhipādo = Пытливость как основа сверхспособностей (acc «… как основу …»); cittiddhipādo = ум как основа сверхспособностей (masc. predicates via T.masc); Tayo iddhipādā = Три основы сверхспособностей [new]
cittiddhipādo na vattabbo cittena sampayuttotipi, … = ум как основу сверхспособностей нельзя определить ни как «связанный с умом», ни как «не связанный с умом» (masc. quote forms; T has only fem./pl.) [new]

## Variant brackets
ātāpo [katamaṃ ātāpaṃ (sabbattha)] = ревностность [вариант чтения (все издания): katamaṃ ātāpaṃ]
thinamiddhaṃ [thīnamiddhaṃ (sī. syā.)] = вялость и сонливость [вариант написания (Sī., Syā.): thīnamiddhaṃ]
vīriyasambojjhaṅgaṃ [viriyasambojjhaṅgaṃ (sī. syā.)] = фактор пробуждения усердия [вариант написания (Sī., Syā.): viriyasambojjhaṅgaṃ]
nhāru [nahāru (sī.)], aṭṭhimiñjaṃ [aṭṭhimiñjā (sī.)] = ch3 strings
chandikatā [chandīkatā (syā.)] = проявление желания [вариант написания (Syā.): chandīkatā]
uṭṭhapeti samuṭṭhapeti [uṭṭhāpeti samuṭṭhāpeti (syā.) evamuparipi] = поднимает, полностью поднимает [вариант написания (Syā.): uṭṭhāpeti samuṭṭhāpeti; так же и далее]
cittassekaggataṃ [cittassa ekaggataṃ (sī. syā.)] = однонаправленность ума [вариант написания (Sī., Syā.): cittassa ekaggataṃ]
saṅkhyaṃ [saṅkhaṃ (sī.)] gacchati = получает название [вариант написания (Sī.): saṅkhaṃ]

## Pāli slips (all reported)
Rendered as meant (spelling / punctuation only): ^2-388 "Siyā vipākā siyā vipākadhammadhammā" (comma missing); ^2-389 "sāsavācātipi", "āsavasampayuttācātipi" (spaces missing); ^2-364 / ^2-367 (pītisambojjhaṅgaṃ …pe…) / ^2-404 / ^2-418 / ^2-442 / ^2-460 stray spaces before …pe…; ^2-443 "viññāṇakhandho"; ^2-450 "Tathābhūtasa"; ^2-459 "maggariyāpannaṃ"; ^2-455 final full stop missing; ^2-432 "abhisaññahitvā" (the later repeats have abhisaññūhitvā; same Russian).
As written: ^2-366 "Pañcapi upādānakkhandhā loko – tattha katamā abhijjhā?" (the parallels have ". Ayaṃ vuccati "loko". Tattha …"): the dash is kept, «… являются миром – что такое здесь алчность?», no «Это называется «миром»»; ^2-368 and ^2-376 answers without quotes (unquoted); ^2-388 / ^2-389 / ^2-429 / ^2-464 "na vattabbā" clusters without dash or quotes (no dash in the Russian); "Araṇāti." (closing ti of the question list) = «Свободны от борьбы.» as ch2–5.
Earlier group (not edited, reported): ch5 ^2-220 vīriyindriya Pāli ends "vīriyabalaṃ – idaṃ vuccati", but its Russian (F.VIRIYA_B from pi-1 ^1-13) ends «сила усердия, правильное усилие»; ch9 ^2-433 does have sammāvāyāmo, so the string is right here.
