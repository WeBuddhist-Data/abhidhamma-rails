# notes-5-01: Saccayamaka (first part: paṇṇattivāra, uppādavāra), frames for 5-02 / 5-03

Builder: build_5-01_vi.py (`T = importlib.import_module("build_5-01_vi")`; importing writes nothing). It imports build_sample_vi, build_2-01_vi (families A / B verbatim), build_2-02_vi (E_YE, YE_CA_JOIN, pe_fragment, pe_end, AGGAMAGGA_NOM) and build_8_vi (citta moments: AT, OF, MOMENT, THEY, NIRODHA_PERSONS, SAMANGI, citta()). Only the members and the items below are new.
Format: Pāli = tiếng Việt. [pi-N] = from the approved pi-N Vietnamese rails (asserted by the builder); [2-01] / [2-02] / [3-01] / [8] / [sample] / [coord] = frame-setters / coordinator; [new] = settled here.
Labels: always build_sample_vi.LABEL.

## Members (SACCA_STEM, MEMBER, m())
Cattāri saccāni – dukkhasaccaṃ, samudayasaccaṃ nirodhasaccaṃ, maggasaccaṃ. = Bốn sự thật – sự thật về khổ đau, sự thật về sự phát sinh, sự thật về sự chấm dứt, sự thật về con đường. [pi-2 ^2-982; missing comma written]
dukkhasacca = sự thật về khổ đau; samudayasacca = sự thật về sự phát sinh; nirodhasacca = sự thật về sự chấm dứt; maggasacca = sự thật về con đường [pi-2]
dukkhaṃ = khổ đau; samudayo / samudayaṃ = sự phát sinh; nirodho / nirodhaṃ = sự chấm dứt; maggo / maggaṃ = con đường [pi-2 Saccavibhaṅga]
saccaṃ = sự thật; saccā = các sự thật (the Pāli number is kept, 2-01) [core]
Kāyikaṃ dukkhaṃ cetasikaṃ dukkhaṃ = khổ đau nơi thân, khổ đau trong tâm [new; pi-1 «nơi thân» / «trong tâm»; the member word «khổ đau» is kept (pi-1 says «sự khó chịu nơi thân» for the feeling) so the answer names the «dukkha» of the question]

## Family A (2-01 frames with sacca members)
Suddhasaccavāro = Mục về các sự thật thuần túy; Suddhasaccamūlacakkavāro = Mục về vòng luân chuyển dựa trên các sự thật thuần túy [new; = Suddhakhandhavāro, 3-01 Suddhāyatanavāro]
#### Paṇṇattivāra (^6-5-6-0, stem form before «(Kha) niddeso») = Mục về sự định danh [sample SECTION]
<X> ṭhapetvā avaseso / avasesaṃ / avasesā <A>, na <B>. = Ngoại trừ <X>, những gì còn lại thì là <A>, nhưng không phải là <B>. [2-01; = 3-01]
<X> ṭhapetvā avasesā saccā na <X>, saccā. = Ngoại trừ <X>, các sự thật còn lại thì không phải là <X>, nhưng là các sự thật. [2-01 A_EXCEPT_N]
<A>ñca <B>ñca ṭhapetvā avasesaṃ / avasesā / avaseso na ceva <A> na ca <B>. = Ngoại trừ <A> và <B>, những gì còn lại thì không phải là <A> cũng không phải là <B>. [2-01]
Samudayasaccaṃ samudayo ceva samudayasaccañca. = Sự thật về sự phát sinh thì vừa là sự phát sinh vừa là sự thật về sự phát sinh. [2-01 / sample BOTH]
Avasesā saccā na <Y>. = Các sự thật còn lại không phải là <Y>. [2-01 A_REST]
Samudayaṃ ṭhapetvā…pe… nirodhaṃ ṭhapetvā…pe…. = Ngoại trừ sự phát sinh… ngoại trừ sự chấm dứt… [= 3-01 «Ngoại trừ tai…»]
X?…pe… Y? / X? …pe… Y? = <question>? … <y question> (lowercase if the Pāli is) ; X?…pe…. = <question>? … [= 3-01; «?…» is never written]
Āmantā…pe…. / Āmantā.…Pe…. = Đúng vậy… [7-04, 3-01]

## Family B: answer heads (head_vi, HEAD_RULES)
Rule: person groups stand in one run under one «ở» (2-01 WHO_HEAD / LIST_SEP, 8 NIRODHA_ASANNA); each time or plane phrase stands alone; groups are joined with «, »; «ye ca …» joins its run with «và» (2-02); a sentence-initial «Ye …» relative takes no «ở» (2-01 YE_UPAPAJJITVA, 2-02 E_YE); an inner resumptive «tesaṃ» opens a new run «ở những người ấy». Commas inside the Pāli list change nothing.
pavatte = trong đời sống, set off by commas («Ở tất cả những người đang tái sinh, trong đời sống, vào khoảnh khắc sinh khởi của tâm …») [coord «Shared person terms»; = 9-01]
cittassa uppādakkhaṇe / bhaṅgakkhaṇe = vào khoảnh khắc sinh khởi / tan rã của tâm [8]
taṇhāya uppādakkhaṇe / bhaṅgakkhaṇe = vào khoảnh khắc sinh khởi / tan rã của khao khát [8 frame; taṇhā «khao khát» core]
maggassa / aggamaggassa / phalassa uppādakkhaṇe = … của con đường / của con đường tối thượng / của thành quả [phala «thành quả» core; aggamagga coord]
maggassa ca phalassa ca uppādakkhaṇe = vào khoảnh khắc sinh khởi của con đường và thành quả; aggamaggassa ca phalassa ca = … của con đường tối thượng và thành quả [new]
taṇhāvippayuttacittassa = của tâm không gắn liền với khao khát; maggavippayuttacittassa = của tâm không gắn liền với con đường [pi-1 vippayutta «không gắn liền với»]
taṇhāvippayuttamaggavippayuttacittassa = của tâm không gắn liền với khao khát và không gắn liền với con đường; maggavippayuttataṇhāvippayutta- = … con đường và không gắn liền với khao khát (order kept) [new]
upapatticittassa uppādakkhaṇe = vào khoảnh khắc sinh khởi của tâm tái sinh [new; upapajjati «tái sinh» pi-2]
dutiye citte vattamāne = khi tâm thứ hai đang diễn ra; dutiye akusale citte vattamāne = khi tâm bất thiện thứ hai đang diễn ra; taṇhāvippayuttacitte vattamāne = khi tâm không gắn liền với khao khát đang diễn ra [pi-5 «khi tâm … đang diễn ra»]
yassa cittassa anantarā aggamaggaṃ paṭilabhissanti = những người sẽ đạt được con đường tối thượng ngay sau tâm nào đó (a person group, with «ở») [coord: anantarā «ngay sau» = 9-01 / 6-01; aṭṭhakathā ^6-176]
tassa cittassa uppādakkhaṇe / bhaṅgakkhaṇe = vào khoảnh khắc sinh khởi / tan rã của tâm ấy [new; 8 «tâm nào … tâm ấy»]
ye caññe maggaṃ paṭilabhissanti = và những người khác nào sẽ đạt được con đường [2-02 E_YE + «khác»]
ye ca puthujjanā maggaṃ na paṭilabhissanti = và những người phàm phu nào sẽ không đạt được con đường [2-02]
Ye maggaṃ paṭilabhissanti tesaṃ … = Những người nào sẽ đạt được con đường, thì ở những người ấy … [2-02 / coord]
inner tesaṃ + time phrase = ở những người ấy, vào …; tesaṃ upapajjantānaṃ / tesaṃ cavantānaṃ (inner) = ở những người ấy khi đang tái sinh / khi đang chết đi [new]
Aggamaggasamaṅgīnaṃ = những người có được con đường tối thượng [coord]; arahantānaṃ = các bậc A-la-hán [pi-5]
abhisametāvīnaṃ / anabhisametāvīnaṃ = những người đã thấu hiểu / những người chưa thấu hiểu (+ upapajjantānaṃ / cavantānaṃ: «… đang tái sinh» / «… đang chết đi») [new; abhisameti «thấu hiểu» pi-5]
āpāyikānaṃ = chúng sinh trong cõi khổ; Apāye = Trong cõi khổ [pi-2 apāya «cõi khổ»; 2-01 BEINGS_OF / PLACE_IN]
Sabbesaṃ (bare, no participle) = Ở tất cả chúng sinh [coord «Shared person terms»; pi-2, 6-01]; Itaresaṃ (alone) = những người khác [2-01]
Pacchimacittasamaṅgīnaṃ = những người có được tâm cuối cùng [8]; nirodhasamāpannānaṃ = những người nhập thành tựu thiền chấm dứt [8]
Avasese catuvokāre pañcavokāre = Trong cõi gồm bốn khối, cõi gồm năm khối còn lại [new; 2-01 planes]
Sabbesaṃ / itaresaṃ / plane + upapajjantānaṃ / cavantānaṃ, suddhāvāsānaṃ, asaññasattānaṃ, itaresaṃ catuvokārānaṃ pañcavokārānaṃ = 2-01 who() verbatim

## Family B: question shortenings
(Kha) yassa vā pana…pe…? / yattha vā pana…pe…? = (b) Còn ở người nào…? / (b) Còn ở nơi nào…? [8]
(Kha) yassa vā pana…pe… uppajjitthāti? = (b) Còn ở người nào… đã sinh khởi không? [new: the frame tail «<verb> không?»]
(Kha) yassa vā pana yattha X uppajjissati…pe… uppajjissatīti? = (b) Còn ở người nào, ở nơi nào mà X sẽ sinh khởi… sẽ sinh khởi không? [new]
Yattha X v…pe…. = Ở nơi nào mà X v… [2-02 pe_fragment]

## Editorial notes and closing lines
(Yassakampi yassayatthakampi sadisaṃ vitthāretabbaṃ). = (Phần về người và phần về người và nơi chốn cũng nên được trình bày chi tiết giống như vậy). [pi-2 «nên được trình bày chi tiết»; 3-01 yassaka, sadisa «giống»]
(Yatthakampi sabbattha sadisaṃ. Tantinānākaraṇaṃ heṭṭhā yatthakasadisaṃ). = (Phần về nơi chốn ở mọi chỗ cũng giống nhau. Sự khác biệt về câu chữ thì giống như phần về nơi chốn ở trên). [new; textual sabbattha «ở mọi chỗ» 3-01; tanti «câu chữ»; heṭṭhā «ở trên»]
(yatthakā sadisā sabbe) = (tất cả các phần về nơi chốn đều giống nhau) [new]
(yatthakampi yassayatthakasadisaṃ kātabbaṃ) = (phần về nơi chốn cũng nên được trình bày giống như phần về người và nơi chốn) [new; 2-02 kātabbaṃ]
Uppādavāro. = Mục về sự sinh khởi. [= 2-02 «Nirodhavāro.»]
Variant tails: evaṃ avasesesu tīsu saccesu = , cũng vậy ở ba sự thật còn lại; evaṃ puggalokāsepi nirodhavārepi = , cũng vậy ở phần về người và nơi chốn và ở mục về sự chấm dứt; puggalokāsavārepi = , cũng vậy ở mục về người và nơi chốn [new; 2-01 evamuparipi frame]

## Source points in 5-01 (translated as written)
^6-5-1: no comma between «samudayasaccaṃ» and «nirodhasaccaṃ»; comma written.
^6-5-11: «… avasesaṃ na dukkhaṃ [var] dukkhasaccaṃ.» has no comma after the bracket (^6-5-16 has «na dukkhaṃ, dukkhasaccaṃ»); the frame comma is written.
^6-5-22 / ^6-5-26: «Āmantā.…Pe….» (period before …pe…) rendered as ^6-5-20 «Āmantā…pe….» = «Đúng vậy…».
^6-5-69: the variant bracket stands between «ye» and «caññe»; in Vietnamese it follows the first group.
^6-5-74: «paṭilabhissānti» = paṭilabhissanti (spelling).
^6-5-76: «asaññattā cavantānaṃ» = asaññasattā (spelling); the head then names «asaññasattā cavantānaṃ» twice (before and after «arūpe aggamaggassa …»); both kept.
^6-5-77: «Aggamaggasamaṅgīnaṃ arahantānaṃ, āpāyikānaṃ …» and ^6-5-51 / ^6-5-79 «paṭilabhissanti, ye caññe»: stray commas, no effect.
