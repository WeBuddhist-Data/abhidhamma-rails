# notes-4-01: 4-01-nikkhepakandam.md, Russian plain zero-shot

Builder: build_4-01_ru.py (imports build_matika_ru as M and build_ch2_01_sample_ru as C; every string below is a constant there).
Helper: helper_4-01_count.py (counts the words of the lobha string).
Matrix items, questions and answers: M.QUESTION / M.ANSWER / M.BARE / M.PRED verbatim. Synonym strings S_ALOBHA, S_ADOSA, S_PANNA from C verbatim.

## Frames
Katame dhammā X? = M.QUESTION(X)
– ime dhammā X. = – M.ANSWER(X)   (comma before the dash when a participial or relative clause precedes)
Ime dhammā X. (own line) = Это <M.BARE(X)>.
Tattha katamo/katamā/katamaṃ/katame X? = Что здесь является <X, творительный падеж>?
– ayaṃ/idaṃ vuccati X. = – это называется <X, творительный падеж>.
Tattha katamā X…pe… ayaṃ vuccati X. = Что здесь является X… это называется X.
Yo/Yā/Yaṃ S – ayaṃ vuccati X. = То, что есть S, – это называется X.
yo/yā/yaṃ evarūpo/evarūpā/evarūpaṃ S = то, что есть такая/такое S
Katame dhammā kenaci viññeyyā, kenaci na viññeyyā? = Какие явления познаются тем или иным видом сознания и не познаются тем или иным видом сознания?
Ime dhammā kenaci viññeyyā kenaci na viññeyyā. = Это явления, познаваемые тем или иным видом сознания и не познаваемые тем или иным видом сознания.
Ye te dhammā A-viññeyyā, na te dhammā B-viññeyyā; ye vā pana te dhammā B-viññeyyā, na te dhammā A-viññeyyā. = Явления, познаваемые A сознанием, не познаются B сознанием; а явления, познаваемые B сознанием, не познаются A сознанием.
cakkhu- / sota- / ghāna- / jivhā- / kāyaviññeyya = познаваемый зрительным / слуховым / обонятельным / вкусовым / осязательным сознанием
Teyeva āsavā āsavā ceva sāsavā ca. = Те же самые влечения являются влечениями и подвержены влечениям. (Tāneva saṃyojanāni …, Teva ganthā … likewise)
Yeva te dhammā sappaccayā, teva te dhammā saṅkhatā. = Те самые явления, которые имеют условия, и есть обусловленные явления.
Yo eva so dhammo appaccayo, so eva so dhammo asaṅkhato. = То самое явление, которое не имеет условий, и есть необусловленное явление.
Lobho mohena hetu ceva sahetuko ca = жадность является корнем и имеет корнем заблуждение
Lobho mohena hetu ceva hetusampayutto ca = жадность является корнем и связана с заблуждением как с корнем
alobho adoso amoho, te aññamaññaṃ hetū ceva sahetukā ca = отсутствие жадности, отсутствие злобы и отсутствие заблуждения являются корнями и имеют корнями друг друга (… связаны друг с другом как с корнями)
Kāmāsavo avijjāsavena āsavo ceva āsavasampayutto ca = влечение к чувственным удовольствиям является влечением и связано с влечением неведения как с влечением
X-saṃyojanaṃ Y-saṃyojanena saṃyojanañceva saṃyojanasampayuttañca = оковы X являются оковами и связаны с оковами Y как с оковами
X kāyagantho Y-kāyaganthena gantho ceva ganthasampayutto ca = телесные узы X являются узами и связаны с телесными узами Y как с узами
Tehi dhammehi ye dhammā sahetukā / ahetukā = Явления, которые имеют / не имеют эти явления своими корнями (… этих явлений …)
Tehi dhammehi ye dhammā sampayuttā / vippayuttā = Явления, которые связаны / не связаны с этими явлениями
Tehi dhammehi ye dhammā sahetukā / sampayuttā / sāsavā (saṃyojaniyā, ganthaniyā), te dhamme ṭhapetvā = Среди явлений, которые имеют эти явления своими корнями / связаны с этими явлениями / подвержены этим явлениям, за исключением этих явлений,
Tehi dhammehi ye dhammā vippayuttā sāsavā kusalākusalābyākatā dhammā … = Не связанные с этими явлениями подверженные влечениям благие, неблагие и этически неопределённые явления …
Te dhamme ṭhapetvā avasesā = За исключением этих явлений, остальные
ṭhapetvā = за исключением
Sabbāpi micchādiṭṭhi X = Всякое ложное воззрение является X
Ṭhapetvā sīlabbataparāmāsasaṃyojanaṃ sabbāpi micchādiṭṭhi diṭṭhisaṃyojanaṃ = За исключением оков приверженности обрядам и обетам, всякое ложное воззрение является оковами воззрений.
Tikaṃ. = Тройки.
Nikkhepakaṇḍe paṭhamabhāṇavāro. = Первый раздел для чтения вслух в разделе сводок.

## Recurring lists
kāmāvacarā, rūpāvacarā, arūpāvacarā, apariyāpannā (after a noun) = относящиеся к миру чувственных желаний, к миру форм, к миру без форм и не принадлежащие к кругам существования (3-sphere form: … к миру форм и к миру без форм)
<X>bhūmiyaṃ kāmāvacare, rūpāvacare, arūpāvacare, apariyāpanne = На уровне <X> в мире чувственных желаний, в мире форм, в мире без форм и в том, что не принадлежит к кругам существования
Sukhabhūmiyaṃ = На уровне счастья (both ^1-988 and ^1-1004: identical Pāli); Dukkhabhūmiyaṃ = На уровне болезненного чувства; Adukkhamasukhabhūmiyaṃ = На уровне чувства, которое ни болезненно, ни приятно,; Savitakkasavicārabhūmiyaṃ = На уровне направленной мысли и удержания мысли; Avitakkavicāramattabhūmiyaṃ = На уровне без направленной мысли, только с удержанием мысли,; Avitakkaavicārabhūmiyaṃ = На уровне без направленной мысли и без удержания мысли; Pītibhūmiyaṃ = На уровне восторга; Upekkhābhūmiyaṃ = На уровне невозмутимости
Kusalākusalānaṃ dhammānaṃ vipākā = результаты благих и неблагих явлений; avipakkavipākānaṃ = чьи результаты ещё не созрели
kusalākusalābyākatā / kusalākusalā / kusalābyākatā dhammā = благие, неблагие и этически неопределённые явления / благие и неблагие явления / благие и этически неопределённые явления
sāsavā (before those) = подверженные влечениям
taṃsampayutto vedanākkhandho, saññākkhandho, saṅkhārakkhandho, viññāṇakkhandho = связанные с ними (с ним, с ней) совокупность чувств, совокупность восприятия, совокупность формирующих факторов, совокупность сознания
vedanākkhandho…pe… viññāṇakkhandho = совокупность чувств… совокупность сознания; rūpakkhandho…pe… = совокупность материальной формы… совокупность сознания
taṃsamuṭṭhānaṃ kāyakammaṃ, vacīkammaṃ, manokammaṃ = порождённые ими телесное действие, словесное действие, умственное действие
tadekaṭṭhā ca kilesā = и омрачения, пребывающие вместе с ними; tadekaṭṭho lobho, doso, moho = жадность, злоба, заблуждение, пребывающие вместе с ними
Tīṇi kusalamūlāni – alobho, adoso, amoho = Три благих корня – отсутствие жадности, отсутствие злобы, отсутствие заблуждения (akusala: Три неблагих корня – жадность, злоба, заблуждение)
Avaseso lobho, doso, moho = Оставшиеся жадность, злоба, заблуждение
ye ca dhammā kiriyā neva kusalā nākusalā na ca kammavipākā = и те функциональные явления, которые не являются ни благими, ни неблагими, ни результатами действий
kiriyābyākatesu dhammesu = в этически неопределённых функциональных явлениях
sabbañca rūpaṃ, asaṅkhatā ca dhātu = и вся материальная форма, и необусловленный элемент; asaṅkhatā dhātu = необусловленный элемент
yañca rūpaṃ (na) kammassa katattā = и та материальная форма, которая возникла (не) вследствие совершённого действия; … uppajjissati = которая возникнет вследствие совершённого действия
yañca rūpaṃ anidassanaṃ appaṭighaṃ dhammāyatanapariyāpannaṃ = и та материальная форма, которая невидима, не способна к соударению и входит в сферу объектов ума
Apariyāpannā maggā ca, maggaphalāni ca, asaṅkhatā ca dhātu = Пути, не принадлежащие к кругам существования, плоды путей и необусловленный элемент
Cattāro maggā apariyāpannā = Четыре пути, не принадлежащие к кругам существования
heṭṭhimāni ca tīṇi sāmaññaphalāni = и три низших плода отшельничества; Upariṭṭhimaṃ arahattaphalaṃ = Высший плод состояния архата
Paritte (etc.) dhamme ārabbha ye uppajjanti cittacetasikā dhammā = Ум и сопутствующие уму явления, которые возникают, имея объектом ограниченные (…) явления
Ariyamaggaṃ adhipatiṃ karitvā = сделав благородный путь главенствующим; ariyamaggasamaṅgissa = у того, кто обладает благородным путём
vīmaṃsādhipateyyaṃ maggaṃ bhāvayantassa = развивает путь, в котором преобладает исследование; vīmaṃsā = исследование (pi-5)
maggaṅgāni = факторы пути; maggahetū = корни пути; pahātabbahetū = корни, устраняемые … («это явления, являющиеся корнями, устраняемыми видением истины»)
Pañca kammāni ānantarikāni, yā ca micchādiṭṭhiniyatā = Пять действий с немедленным воздаянием и предопределённое ложное воззрение
jātā bhūtā sañjātā nibbattā abhinibbattā pātubhūtā uppannā samuppannā uṭṭhitā samuṭṭhitā = рождённые, ставшие, зародившиеся, появившиеся, полностью появившиеся, проявившиеся, возникшие, полностью возникшие, поднявшиеся, полностью поднявшиеся (negatives: нерождённые, неставшие, незародившиеся, непоявившиеся, не полностью появившиеся, непроявившиеся, невозникшие, не полностью возникшие, неподнявшиеся, не полностью поднявшиеся)
atītā niruddhā vigatā vipariṇatā atthaṅgatā abbhatthaṅgatā uppajjitvā vigatā = прошлые, прекратившиеся, исчезнувшие, изменившиеся, угасшие, полностью угасшие, исчезнувшие после возникновения
uppannā uppannaṃsena saṅgahitā = возникшие и включённые в категорию возникшего (невозникшего, прошлого, будущего, настоящего likewise)
tesaṃ tesaṃ sattānaṃ ajjhattaṃ paccattaṃ niyatā pāṭipuggalikā upādiṇṇā = у тех или иных существ являются внутренними, собственными, закреплёнными за ними, индивидуальными и охваченными цеплянием (niyatā here = «закреплённые за ними», not «предопределённые»); parasattānaṃ parapuggalānaṃ = других существ, других личностей
Tadubhayaṃ = И то и другое
Cattāro ca mahābhūtā catunnañca mahābhūtānaṃ upādāya rūpaṃ = Четыре великих элемента и материальная форма, производная от четырёх великих элементов
Pañcakkhandhā = Пять совокупностей
rūpāyatana / cakkhāyatana … phoṭṭhabbāyatana = сфера видимых форм / сфера глаза, уха, носа, языка, тела, звуков, запахов, вкусов, осязаемого (pi-3/pi-5)

## Strings (new)
Dukkhe ñāṇaṃ … idappaccayatā paṭiccasamuppannesu dhammesu ñāṇaṃ = знание страдания, знание возникновения страдания, знание прекращения страдания, знание способа практики, ведущего к прекращению страдания, знание прошлого, знание будущего, знание прошлого и будущего, знание закона обусловленности и явлений, возникших в зависимости от условий (aññāṇaṃ = незнание …)
moha string (aññāṇaṃ … akusalamūlaṃ) = pi-4 ^4-60 verbatim: незнание, отсутствие видения, …, засов неведения, заблуждение, неблагой корень
paññā string + dhammavicayasambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ = …, исследование явлений как фактор пробуждения, фактор пути, то, что входит в путь
metti mettāyanā mettāyitattaṃ anuddā anuddāyanā anudāyitattaṃ hitesitā anukampā = доброжелательность, проявление доброжелательности, состояние доброжелательности, участие, проявление участия, состояние участия, желание блага, сострадание
lobha string (rāgo … akusalamūlaṃ, 102 items) = страсть, пристрастие, расположенность, …, алчность, жадность, неблагой корень (full list: build_4-01_ru.LOBHA_ITEMS); rāga = страсть, sārāga = пристрастие (alobha string keeps «отсутствие страсти»), rūpataṇhā (both times) = жажда форм, arūpataṇhā = жажда бесформенного, vevicchaṃ = скаредность, upakkileso = загрязнение
dosa opening (anatthaṃ me acarīti āghāto jāyati …) = При мысли «Он причинил мне вред» возникает досада, …, или же досада возникает без повода.
dosa string (cittassa āghāto … anattamanatā cittassa) = досада ума, раздражение, неприязнь, противодействие, …, недовольство ума (kodho … anattamanatā cittassa as pi-4 ^4-45, with doso = злоба)
diṭṭhi string (diṭṭhi diṭṭhigataṃ … vipariyāsaggāho) = pi-4 ^4-62 with взгляды -> воззрение, diṭṭhivisūkāyikaṃ = извращённость воззрений, parāmāso = искажение (matrix): воззрение, приверженность воззрениям, дебри воззрений, пустыня воззрений, извращённость воззрений, метания воззрений, оковы воззрений, хватка, цепкость, приверженность, искажение, кривая дорога, ложный путь, ложность, прибежище сектантских учений, превратная хватка
kaṅkhā string = сомнение, проявление сомнения, состояние сомнения, неуверенность, колебание, раздвоенность, распутье, нерешительность, неспособность прийти к определённости, блуждание, беспорядочное блуждание, отсутствие углубления, оцепенелость ума, терзание ума
Satthari … kaṅkhati vicikicchati = Человек сомневается и колеблется в отношении Учителя, … Учения, … Общины, … обучения, … прошлого, … будущего, … прошлого и будущего, … закона обусловленности и явлений, возникших в зависимости от условий
Idha assutavā puthujjano … rūpaṃ attato samanupassati … = Вот не слышавший Учения обычный человек, который не видит благородных, не сведущ в Учении благородных, не обучен Учению благородных, не видит достойных людей, … считает материальную форму самостью, или самость обладающей материальной формой, или материальную форму находящейся в самости, или самость находящейся в материальной форме.
Ito bahiddhā samaṇabrāhmaṇānaṃ sīlena suddhi … = Отшельники и брахманы вне этого Учения считают: «Чистота достигается обрядами, чистота достигается обетами, чистота достигается обрядами и обетами»
ten views (sassato loko … neva hoti na na hoti tathāgato paraṃ maraṇā) = «Мир вечен», или «Мир не вечен», или «Мир конечен», или «Мир бесконечен», или «Душа и тело одно и то же», или «Душа одно, а тело другое», или «Татхагата существует после смерти», или «Татхагата не существует после смерти», или «Татхагата и существует, и не существует после смерти», или «Татхагата ни существует, ни не существует после смерти»
idameva saccaṃ moghamaññaṃ = только это истинно, всё прочее ложно
Yo kāmesu kāmacchando kāmarāgo kāmanandī kāmataṇhā kāmasineho kāmapariḷāho kāmamucchā kāmajjhosānaṃ = То, что в отношении чувственных удовольствий есть чувственное желание, чувственная страсть, чувственное наслаждение, жажда чувственных удовольствий, чувственная приязнь, чувственный жар, чувственная одурманенность, чувственная поглощённость
Yo bhavesu bhavachando … bhavajjhosānaṃ = То, что в отношении видов существования есть желание существования, страсть к существованию, наслаждение существованием, жажда существования, приязнь к существованию, жар существования, одурманенность существованием, поглощённость существованием
māna (Seyyohamasmīti māno …) = Самомнение «Я лучше других», самомнение «Я равен другим», самомнение «Я хуже других». … самомнение, зазнайство, состояние зазнайства, превознесение, надменность, знамя, возвеличивание себя, желание ума поднять свой стяг
issā string = pi-4 ^4-49 with usūyā = ревность (pi-4 «ревнивая неприязнь»; paṭigha = неприязнь here)
macchariya string = pi-4 ^4-50 with vevicchaṃ = скаредность (pi-4 «жадность» = lobha here), aggahitattaṃ cittassa = зажатость ума (pi-4 «цепкость ума»; paṭiggāho = цепкость here), dhamma = Учение

## Defilement names
sakkāyadiṭṭhi / vicikicchā / sīlabbataparāmāsa = воззрение о самости / колебание / приверженность обрядам и обетам (pi-5); kaṅkhā = сомнение; vimati = неуверенность (pi-5)
attā = самость (pi-4); puthujjana = обычный человек; sappurisa = достойный человек; satthā / saṅgha / sikkhā = Учитель / Община / обучение
tīṇi / dasa saṃyojanāni = три / десять видов оков; cattāro ganthā = четыре вида уз; cattāro āsavā = четыре влечения
kāmāsava / bhavāsava / diṭṭhāsava / avijjāsava = влечение к чувственным удовольствиям / влечение к существованию (pi-4) / влечение воззрений / влечение неведения (pi-4)
kāmarāga- / paṭigha- / māna- / diṭṭhi- / vicikicchā- / sīlabbataparāmāsa- / bhavarāga- / issā- / macchariya- / avijjā-saṃyojanaṃ = оковы чувственной страсти / неприязни / самомнения / воззрений / колебания / приверженности обрядам и обетам / страсти к существованию / зависти / скупости / неведения
abhijjhā / byāpādo / sīlabbataparāmāso / idaṃsaccābhiniveso kāyagantho = телесные узы алчности / недоброжелательности / приверженности обрядам и обетам / приверженности убеждению «только это истинно»
micchādiṭṭhi = ложное воззрение (pi-5); tathāgata = Татхагата; Māra = Мара

## Source notes (translated as written)
- ^1-1022: the question reads «neva ācayagāmi na apacayagāmino» (matrix: nevācayagāmināpacayagāmino); the matrix question is used.
- ^1-1124, ^1-1143, ^1-1144: «patiṭṭhāho» in the diṭṭhi string stands for paṭiggāho; rendered as meant («цепкость»).
- ^1-1106, ^1-1123, ^1-1128, ^1-1143, ^1-1144: a Devanāgarī visarga «ः» stands where a punctuation mark belongs; rendered as «;».
- ^1-1041: variant «[rūpā (bahūsu)]» = «[вариант чтения (во многих изданиях): rūpā]».
- ^1-1024: «[uparimaṃ (syā.)]» treated as a reading variant (a different word form, not only spelling).
- ^1-1130, ^1-1146, ^1-1135, ^1-1151, ^1-1138, ^1-1154: the fetter and tie groups say «sāsavā» (subject to taints), not «subject to fetters/ties»; kept («подверженные влечениям»).
- ^1-1039: «maggaṅgāni ṭhapetvā; taṃsampayutto …» kept with the semicolon as in the Pāli.
- ^1-1077: «Ime cha apariyāpannahetū – ime dhammā hetū.» translated as written (the six unincluded roots stand for the whole answer).
