# pi-2 Russian zero-shot, chapters 13 (Appamaññā), 14 (Sikkhāpada), 15 (Paṭisambhidā): new terms and formulas

Builder: build_13_15_ru.py (imports build_10_12_ru as X and through it S, B, T, F, G, Z; extends X.ATERM / X.ADEF / X.QUAL / X.JH_HEAD / X.ASENT / X.PFIX, T.SUBJ2 / T.SURF2 / T.KEEP_OI, G.TOKENS and wraps X.pq_chunk, all in memory only). Scratch: probe_13_15.py.
Format: Pāli = Russian, one per line. [pi-1] = pi-1 Russian (asserted in the builder); [pi-4] / [pi-5] = those books; [ch3] … [ch12] = earlier pi-2 groups; [new] = settled here.

## Reused
Yā sattesu metti mettāyanā mettāyitattaṃ mettācetovimutti = То, что есть доброжелательность к существам, проявление доброжелательности, состояние доброжелательности, освобождение ума доброжелательностью [ch3 T.METTA]
Yā sattesu karuṇā karuṇāyanā karuṇāyitattaṃ karuṇācetovimutti = То, что есть сострадание к существам, … освобождение ума состраданием [ch3 T.KARUNA]
mettā / karuṇā / muditā / upekkhā = доброжелательность / сострадание / сорадование / невозмутимость [pi-1]
mettāsahagataṃ … jhānaṃ = входит в … медитативное погружение, сопровождаемое доброжелательностью (состраданием, сорадованием, невозмутимостью), и пребывает в нём [pi-1 ^1-251 …; ch12 openings X.opening]
Idha bhikkhu yasmiṃ samaye rūpūpapattiyā maggaṃ bhāveti … / Tasseva … vipākaṃ … / rūpāvacaraṃ jhānaṃ bhāveti kiriyaṃ … = ch12 strings («Вот в то время, когда монах …», «Вследствие того же …, когда монах …»)
Yasmiṃ samaye <mind type> (no subject) = «В то время, когда возникает …» / «В то время, когда кто-либо развивает …» [pi-1, ch6 G.desc / G.JHANA / G.TASSEVA]
Yaṃ cittaṃ mano mānasaṃ hadayaṃ … tajjāmanoviññāṇadhātu = pi-1 ^1-6 (ch6 G.BODY); …pe… form = ch12
"Viharatī"ti … = ch12 («Пребывает»: он принимает положения тела, …)
sabbena sabbaṃ sabbathā sabbaṃ asesaṃ nissesaṃ = всецело, во всех отношениях, без остатка, полностью [ch12]
ārati virati paṭivirati veramaṇī akiriyā akaraṇaṃ anajjhāpatti velāanatikkamo setughāto = отстранение от X, воздержание, полное воздержание, уклонение, неделание, несовершение, невпадение в проступок, непереступание границы, разрушение моста [pi-1 ^1-299 … ^1-301, ch4]
cetanā sañcetanā sañcetayitattaṃ = намерение, проявление намерения, состояние намеренности [pi-1 ^1-5]
phasso…pe… paggāho avikkhepo = контакт… напряжение сил, отсутствие отвлечения [pi-1]
hīnaṃ / majjhimaṃ / paṇītaṃ; chanda-/vīriya-/citta-/vīmaṃsādhipateyyaṃ = низший / средний / высший; с преобладанием желания / усердия / ума / пытливости [pi-1 ^1-269]
phasso hoti, vedanā hoti, … jīvitindriyaṃ hoti, ye vā pana tasmiṃ samaye aññepi atthi paṭiccasamuppannā arūpino dhammā = есть контакт, есть чувство, … есть жизненная способность, или же какие бы другие нематериальные явления, возникшие в зависимости от условий, ни были в это время [pi-1 ^1-443, ^1-469, ^1-556; sukhaṃ with sukhindriya = удовольствие, else счастье]
Katame dhammā kusalā / akusalā / abyākatā? = Что такое благие / неблагие / этически неопределённые явления? [pi-1]
cittuppāda = вид ума [pi-1 ^1-1385]
Pañhāpucchaka lexicon = B/T/ch12 (X.pq_line)

## Chapter 13
Catasso appamaññāyo – … = Четыре безмерных состояния – … (T.enum, «и» before the last) [pi-3 «безмерное состояние»]
##### Mettā / Karuṇā / Muditā / Upekkhā = Доброжелательность / Сострадание / Сорадование / Невозмутимость
Yā sattesu muditā muditāyanā muditāyitattaṃ muditācetovimutti = То, что есть сорадование существам, проявление сорадования, состояние сорадования, освобождение ума сорадованием [new, ch3 pattern; «существам» for natural government]
Yā sattesu upekkhā upekkhāyanā upekkhāyitattaṃ upekkhācetovimutti = То, что есть невозмутимость по отношению к существам, проявление невозмутимости, состояние невозмутимости, освобождение ума невозмутимостью [new]
Yā (tasmiṃ samaye) metti mettāyanā … (Abhidhamma, no sattesu) = the same without «к существам» [new]
<X>sahagatena cetasā = умом, сопровождаемым <X-ins> [pi-1 sahagata]
ekaṃ disaṃ pharitvā viharati = пребывает, наполнив одну сторону света [new]
tathā dutiyaṃ, tathā tatiyaṃ, tathā catutthaṃ = так же вторую, так же третью, так же четвёртую [new]
Iti uddhamadho tiriyaṃ sabbadhi sabbattatāya sabbāvantaṃ lokaṃ … pharitvā viharati = Так вверх, вниз, в стороны, повсюду, ко всем как к себе, он пребывает, наполнив весь мир … [new; sabbattatāya with English rails "extending to all as to himself"]
vipulena mahaggatena appamāṇena averena abyāpajjena = обширным, возвышенным, безмерным, свободным от вражды, свободным от неприязни [pi-1 mahaggata, appamāṇa, abyāpajja «неприязнь»; pi-5 avera, vipula]
pharitvā adhimuccitvā = наполнив, утвердившись в решимости [new; adhimokkha = решимость]
puratthimā / pacchimā / uttarā / dakkhiṇā disā; uddhaṃ / adho / tiriyaṃ; vidisā = восточная / западная / северная / южная сторона света; вверх / вниз / в стороны; промежуточная сторона света [new]
Pariyādāyavacanametaṃ = Это выражение, охватывающее всё [new]
yaṃ vipulaṃ taṃ mahaggataṃ, … yo avero so abyāpajjo = то, что обширно, то и возвышенно; … то, что свободно от вражды, то и свободно от неприязни [new, ch12 «то, что …, то и …»]
Idaṃ cittaṃ imāya X sahagataṃ hoti sahajātaṃ saṃsaṭṭhaṃ sampayuttaṃ = Этот ум сопровождается этой/этим X, рождён вместе с ней/ним, соединён с ней/ним, связан с ней/ним [ch12 words, masculine]
Seyyathāpi nāma ekaṃ puggalaṃ piyaṃ manāpaṃ disvā mettāyeyya, evameva sabbe satte mettāya pharati = Подобно тому как кто-либо, увидев одного человека, дорогого и приятного, проникся бы к нему доброжелательностью, так же он наполняет доброжелательностью всех существ [new]; duggata durūpeta = бедствующий и обездоленный; mudito assa = порадовался бы за него; neva manāpaṃ na amanāpaṃ … upekkhako assa = ни приятного, ни неприятного, остался бы к нему невозмутимым
Avasesā dhammā mettāya (karuṇāya, muditāya, upekkhāya) sampayuttā = Остальные явления связаны с доброжелательностью (…) [ch12 frame]
sukhassa ca pahānā dukkhassa ca pahānā…pe… = с устранением приятного и с устранением болезненного… [pi-1 JH4 words]
Pañhāpucchaka subjects: Tisso appamaññāyo = Три безмерных состояния (pl); Mettā = Доброжелательность, Upekkhā = Невозмутимость (sg f); Catunnaṃ appamaññānaṃ = четырёх безмерных состояний

## Chapter 14
Pañca sikkhāpadāni = Пять правил обучения [new; pi-5 sikkhā «обучение»]
X veramaṇī sikkhāpadaṃ = правило обучения о воздержании от X [new; pi-5 veramaṇī «воздержание»; the pi-1 synonym list keeps veramaṇī = «уклонение»]
pāṇātipātā = (от) убийства живых существ [pi-4/pi-5]; adinnādānā = взятия того, что не дано [pi-4 words]; kāmesumicchācārā = неподобающего поведения в чувственных удовольствиях [pi-4]; musāvādā = лжи [pi-4]; surāmerayamajjapamādaṭṭhānā = употребления спиртного, браги и опьяняющих напитков, ведущего к беспечности [pi-5 ^5-380 …]
X viramantassa (in the mind-type opening) = у того, кто воздерживается от X (placed after «В то время, когда») [new]
Avasesā dhammā veramaṇiyā / cetanāya sampayuttā = Остальные явления связаны с воздержанием / с намерением [new]
Katame dhammā sikkhā? = Какие явления являются обучением?; Ime dhammā sikkhā. = Эти явления являются обучением. [new]
Pañcannaṃ sikkhāpadānaṃ = пяти правил обучения
kusalāyeva = являются только благими [B]

## Chapter 15
paṭisambhidā = аналитическое знание [pi-5]; attha- / dhamma- / nirutti- / paṭibhāna- = смысла / явлений / выражений / находчивости [new; nirutti pi-1/pi-5 «выражение», paṭibhāna pi-4 «находчивый»]
Catasso / Tisso paṭisambhidā – … = Четыре / Три аналитических знания – … (T.enum)
X-e ñāṇaṃ Y-paṭisambhidā = знание X(gen) является Y(ins) [pi-5 frame «… является аналитическим знанием»]
tatra dhammaniruttābhilāpe ñāṇaṃ niruttipaṭisambhidā = знание высказывания этого выражения явлений является аналитическим знанием выражений [new; abhilāpa pi-1 «высказывание»]
Yāya niruttiyā tesaṃ dhammānaṃ paññatti hoti tatra dhammaniruttābhilāpe ñāṇaṃ niruttipaṭisambhidā = Знание высказывания того выражения явлений, которым эти явления обозначаются, является аналитическим знанием выражений [new]
ñāṇesu ñāṇaṃ paṭibhānapaṭisambhidā = знание знаний является аналитическим знанием находчивости [new]
Yena ñāṇena tāni ñāṇāni jānāti – "imāni ñāṇāni idamatthajotakānī"ti, ñāṇesu ñāṇaṃ paṭibhānapaṭisambhidā = Знание, которым он знает эти знания – «Эти знания проясняют этот смысл», то есть знание знаний, является аналитическим знанием находчивости [new]
Imesu dhammesu ñāṇaṃ / Tesaṃ vipāke ñāṇaṃ = Знание этих явлений / Знание их результата [new]
hetu / hetuphala = причина / плод причины [ch6 hetu «причина»]
jātā bhūtā sañjātā nibbattā abhinibbattā pātubhūtā = родились, стали существовать, зародились, возникли, полностью возникли, проявились [ch12 JATA + bhūtā]
dependent-origination links in the genitive = старения и смерти, рождения, существования, цепляния, жажды, чувства, контакта, шести сфер восприятия, умственного и материальной формы, сознания, формирующих факторов [ch6 G.N]
dhammaṃ jānāti – suttaṃ geyyaṃ veyyākaraṇaṃ gāthaṃ udānaṃ itivuttakaṃ jātakaṃ abbhutadhammaṃ vedallaṃ = знает Учение – беседы, прозу со стихами, разъяснения, строфы, вдохновенные изречения, изречения «Так было сказано», истории о прошлых рождениях, рассказы о чудесном, вопросы и ответы [new]
bhāsita = сказанное; tassa tasseva bhāsitassa atthaṃ = смысл того или иного сказанного [new]
vāra (section headings) = раздел: Saṅgaha- обобщения, Sacca- об истинах, Hetu- о причине, Dhamma- о явлениях, Paṭiccasamuppāda- о возникновении в зависимости от условий, Pariyatti- об изучении Учения, Kusala- о благом, Akusala- о неблагом, Vipāka- о результатах действий, Kiriya- о функциональном; "Ayaṃ X-vāro." = «Это раздел …» [new]
kāmāvacarakusalato / kiriyato catūsu ñāṇasampayuttesu cittuppādesu = в четырёх видах благого ума, относящегося к миру чувственных желаний, связанных со знанием / в четырёх видах функционального ума, связанных со знанием [new; «и» added between them]
catūsu maggesu catūsu phalesu = в четырёх путях и четырёх плодах [new]
Pañhāpucchaka subjects: Tisso paṭisambhidā = Три аналитических знания; dve paṭisambhidā = два аналитических знания (pl); atthapaṭisambhidā / Niruttipaṭisambhidā = аналитическое знание смысла / выражений (sg neuter); Catunnaṃ paṭisambhidānaṃ = четырёх аналитических знаний
X na vattabbā – Atipi, Btipi (unquoted, with a dash) = X нельзя определить – ни как «A», ни как «B» [new wrapper of the ch12 frame]
fem. sg forms ācayagāminī, apacayagāminī, nevācayagāmināpacayagāminī, maggādhipatinī = the -ino items (neuter predicates) [aliases]

## Variant brackets
[catutthiṃ (sī.)] = [вариант написания (Sī.): catutthiṃ]; [abyāpajjhena (sī. syā.)], [abyāpajjho (sī. syā.)] = [вариант написания (Sī., Syā.): …]
[paṭibhāṇapaṭisambhidā (syā.) evamuparipi] = [вариант написания (Syā.): paṭibhāṇapaṭisambhidā; так же и далее]
āsavo [āsavā (sī.) dhātuvibhaṅge pana pāṭhanānattaṃ natthi] = [вариант чтения (Sī.): āsavā; но в «Разборе элементов» разночтений нет] („…“ inside a «…» quote)

## Pāli slips and as-written readings (all reported)
Rendered as meant (spelling / punctuation only): ^2-672 '"Viharatī"ti …pe…' (space); ^2-688 "muditāyatanā" (= muditāyanā); ^2-706 "sikkhāpadaṃ, yasmiṃ samaye" (question mark); ^2-709 "majjhimaṃ … paṇītaṃ", ^2-710 "vīriyādhipateyyaṃ … cittādhipateyyaṃ", "sampayuttā …pe…" (spaces); ^2-711 "kāmāvacare kusalaṃ" (= kāmāvacaraṃ); ^2-717 "na hetu sahetūkā", "na bhāvanāyapahātabbā"; ^2-720 "dhammapaṭisambhidā niruttipaṭisambhidā" (comma); ^2-749 "Anidassanaapaṭighā"; ^2-750 "nahetūahetukātipi".
As written: ^2-686 line 2 karuṇā "pītiyā ca virāgā…pe… dutiyaṃ jhānaṃ" (mettā/muditā have vitakkavicārānaṃ vūpasamā) = «с угасанием восторга… входит во второе»; ^2-692 … ^2-694 vipāka series "dutiyaṃ… tatiyaṃ… paṭhamaṃ… dutiyaṃ… tatiyaṃ… catutthaṃ"; ^2-705 line 2 "viramantassa phasso…pe… paggāho avikkhepo" without "yo tasmiṃ samaye" = «…, контакт… напряжение сил, отсутствие отвлечения – это называется …»; ^2-711 "majjhimaṃ paṇītaṃ" without "…" = «средний, высший»; ^2-740 "Tasseva lokuttarassa kusalassa kammassa katattā bhāvitattā" (pi-1 has jhānassa) = «… надмирского благого действия»; ^2-725 ", ime dhammā kusalā" (comma, elsewhere a new sentence).
Context reading: ^2-750 "atthapaṭisambhidā siyā lokiyā, siyā lokuttarā, kenaci viññeyyā, kenaci na viññeyyā": the last two are plural in Russian (all four, as the English rails).
