# notes-6-01: Saṅkhārayamaka part 1 (6-01-sankharayamaka.md); frames 6-02 follows

Builder: build_6-01_vi.py (import with importlib: `X = importlib.import_module("build_6-01_vi")`; importing writes nothing).
It imports build_sample_vi, build_2-01_vi (families A / B verbatim), build_2-02_vi (pe_fragment, YE_CA_CAVANTA / YE_CA_JOIN)
and build_8_vi (moments, samaṅgī, nirodhasamāpanna). 6-02 should import X and use m(), head(), translate_sentence(), EXACT.
Format: Pāli = tiếng Việt. [pi-N] = from the approved pi-N rails (asserted); [2-01] / [2-02] / [8] = imported constant; [new] = set here.
Labels: always build_sample_vi.LABEL.

## Members (MEMBER, m())
kāyasaṅkhāro / -aṃ = sự tạo tác bằng thân; vacīsaṅkhāro / -aṃ = sự tạo tác bằng lời nói; cittasaṅkhāro / -aṃ = sự tạo tác bằng tâm [pi-2 ^2-226, pi-5]
kāyo / kāyaṃ = thân [pi-1]; vacī / vaciṃ = lời nói [pi-5]; cittaṃ = tâm [pi-1]
saṅkhāro = sự tạo tác [pi-2]; saṅkhārā = các tạo tác [2-01, pi-5]
Tayo saṅkhārā – … = Ba sự tạo tác – … [new]
assāsapassāsā = hơi thở vào và hơi thở ra [pi-5]; vitakkavicārā = sự hướng tâm và sự duy trì tâm [pi-1 / pi-5]; saññā ca vedanā ca = tri giác và cảm giác [pi-5]
Ṭhapetvā vitakkavicāre sabbepi cittasampayuttakā dhammā cittasaṅkhāro. = Ngoại trừ sự hướng tâm và sự duy trì tâm, tất cả các hiện tượng gắn liền với tâm đều là sự tạo tác bằng tâm. [pi-1 «các hiện tượng gắn liền với tâm»]

## Family A (2-01 frames with these members)
(Ka) kāyo kāyasaṅkhāro(ti)? = (a) Thân có phải là sự tạo tác bằng thân không? [2-01 a_q]
(Kha) saṅkhārā vacīsaṅkhāro? = (b) Các tạo tác có phải là sự tạo tác bằng lời nói không? [2-01]
Kāyasaṅkhāro na kāyo, kāyasaṅkhāro. = Sự tạo tác bằng thân thì không phải là thân, nhưng là sự tạo tác bằng thân. [2-01]
Vacīsaṅkhāro saṅkhāro ceva vacīsaṅkhāro ca. = Sự tạo tác bằng lời nói thì vừa là sự tạo tác vừa là sự tạo tác bằng lời nói. [2-01 a_both]
Avasesā saṅkhārā na vacīsaṅkhāro. = Các tạo tác còn lại không phải là sự tạo tác bằng lời nói. [2-01 a_rest]
Kāyañca kāyasaṅkhārañca ṭhapetvā avasesā na ceva kāyo na ca kāyasaṅkhāro. = Ngoại trừ thân và sự tạo tác bằng thân, những gì còn lại thì không phải là thân cũng không phải là sự tạo tác bằng thân. [2-01]
Suddhasaṅkhāravāro = Mục về các tạo tác thuần túy [new; = Suddhakhandhavāro pattern]
Paṇṇattivāro. = Mục về sự định danh. [sample SECTION]; Paṇṇattiuddesavāro. / Paṇṇattiniddesavāro. [2-01]
(Kha) paccanīkaṃ (plain line with ID) = (b) Chiều nghịch [sample]

## Answer heads (head(): items joined by ", "; a run of beings items shares one «ở» [2-01 WHO_HEAD, 8])
<G> uppādakkhaṇe / bhaṅgakkhaṇe = vào khoảnh khắc sinh khởi / tan rã của <G> [8 AT / OF, pi-5]
  G: assāsapassāsānaṃ = hơi thở vào và hơi thở ra; vitakkavicārānaṃ = sự hướng tâm và sự duy trì tâm; cittassa = tâm [8];
  avitakkaavicāracittassa = tâm không có sự hướng tâm cũng không có sự duy trì tâm [pi-1]; savitakkasavicārapacchimacittassa = tâm cuối cùng có sự hướng tâm và sự duy trì tâm [new]
vinā assāsapassāsehi / vinā vitakkavicārehi <G> Xkkhaṇe = vào khoảnh khắc … của <G> khi không có hơi thở vào và hơi thở ra / khi không có sự hướng tâm và sự duy trì tâm [new VINA]
<J>jjhānaṃ (…) samāpannānaṃ = những người đang nhập tầng thiền thứ nhất (, tầng thiền thứ hai …) [pi-5 «người đang nhập tầng thiền thứ …», pi-1 tầng thiền]
<J>jjhāne (place) = trong tầng thiền thứ … ; Catutthajjhāne asaññasatte = Trong tầng thiền thứ tư, cõi Vô Tưởng [new; 2-01 PLACE_IN, LIST_SEP]
kāmāvacare / rūpāvacare / arūpāvacare (place) = trong cõi dục lạc / cõi hình sắc / cõi không hình sắc [2-01 PLANE]
kāmāvacarānaṃ, rūpāvacarānaṃ arūpāvacarānaṃ, suddhāvāsānaṃ, itaresaṃ kāmāvacarānaṃ = chúng sinh trong cõi …; những chúng sinh khác trong cõi … [2-01 who]
sabbesaṃ (alone) = tất cả chúng sinh («Ở tất cả chúng sinh, vào khoảnh khắc tan rã của tâm, …») [pi-2 «ở tất cả chúng sinh»]
itaresaṃ = những người khác [8 / 2-01]; tesaṃyeva = chính những người ấy [new]
nirodhasamāpannānaṃ = những người nhập thành tựu thiền chấm dứt; asaññasattānaṃ = chúng sinh Vô Tưởng [8, pi-5]
pacchimacittasamaṅgīnaṃ = những người có được tâm cuối cùng [8]; avitakkaavicārapacchimacittasamaṅgīnaṃ = những người có được tâm cuối cùng không có sự hướng tâm cũng không có sự duy trì tâm [new]
<P>e pacchimacittasamaṅgīnaṃ = những người có được tâm cuối cùng trong <plane> [new, like 2-01 «<P>e pacchimabhavikānaṃ»]
yassa cittassa anantarā kāmāvacarānaṃ pacchimacittaṃ uppajjissati = vào tâm mà ngay sau đó tâm cuối cùng của chúng sinh trong cõi dục lạc sẽ sinh khởi [new ANANTARA]
yassa cittassa anantarā avitakkaavicāraṃ pacchimacittaṃ uppajjissati = vào tâm mà ngay sau đó tâm cuối cùng không có sự hướng tâm cũng không có sự duy trì tâm sẽ sinh khởi [new]
suddhāvāsānaṃ dutiye citte vattamāne = chúng sinh trong cõi Tịnh Cư, khi tâm thứ hai đang diễn ra [new; pi-5 «khi tâm … đang diễn ra»]
Savitakkasavicārabhūmiyaṃ / Avitakkaavicārabhūmiyaṃ = Ở cấp độ có sự hướng tâm và sự duy trì tâm / Ở cấp độ không có sự hướng tâm cũng không có sự duy trì tâm [pi-1 ^1-1000, ^1-1002]
ye ca rūpāvacaraṃ arūpāvacaraṃ upapajjitvā parinibbāyissanti tesaṃ cavantānaṃ = và những người đang chết đi mà sau khi tái sinh vào cõi hình sắc, cõi không hình sắc sẽ nhập Niết-bàn trọn vẹn [2-02 YE_CA_CAVANTA, plane list]
Answer clauses, questions, verbs, «no ca» forms, Natthi / No / Uppajjittha.: 2-01 b_q / b_not / b_both / b_short unchanged.

## Fragments and editorial lines
(Kha) yassa vā pana…pe…? / yattha vā pana…pe…? / yassa vā pana yattha…pe…? = (b) Còn ở người nào…? / Còn ở nơi nào…? / Còn ở người nào, ở nơi nào…? [8 «Còn ở người nào…?»]
(Kha) yassa vā pana cittasaṅkhāro…pe…? = (b) Còn ở người nào mà sự tạo tác bằng tâm…? [new]
Yassa yattha X v…pe…. / Yattha X v…pe… = Ở người nào, ở nơi nào mà X v… / Ở nơi nào mà X v… [2-02 pe_fragment]
Yassa vā pana yattha X v…pe…. = Còn ở người nào, ở nơi nào mà X v… [new]
<question>?…Pe…. = <question>?… [new; as the Pāli]
yassaka / yatthaka / yassayatthaka = phần về người / phần về nơi chốn / phần về người và nơi chốn [new; yatthaka 2-02]
(Yassakampi yassayatthakampi sadisaṃ.) = (Phần về người và phần về người và nơi chốn đều giống nhau.) [new]
(… sadisaṃ vitthāretabbaṃ, yassayatthake nirodhasamāpannānanti na labbhati.) = (Phần về người và phần về người và nơi chốn đều nên được trình bày chi tiết giống nhau, trong phần về người và nơi chốn thì không có trường hợp những người nhập thành tựu thiền chấm dứt.) [new; vitthāretabba pi-2]
(… na kātabbaṃ.) = (…, trong phần về người và nơi chốn thì không nên đưa vào trường hợp những người nhập thành tựu thiền chấm dứt.) [new]
(Yatthakampi sabbattha ekasadisaṃ). = (Phần về nơi chốn cũng giống nhau ở mọi chỗ). [new]
(Yathā uppādavāre atītā pucchā yassakampi yassayatthakampi anulomampi paccanīkampi vibhattaṃ evaṃ nirodhavārepi vibhajitabbaṃ, natthi nānākaraṇaṃ.) = (Như các câu hỏi về quá khứ, cả phần về người lẫn phần về người và nơi chốn, cả chiều thuận lẫn chiều nghịch, đã được phân tích trong mục về sự sinh khởi, trong mục về sự chấm dứt cũng nên phân tích như vậy, không có sự khác biệt.) [new; nānākaraṇa pi-5 «sự khác biệt»]
Uppādavāro. = Mục về sự sinh khởi.; #### Nirodhavāro = Mục về sự chấm dứt [sample SECTION]

## Source points (translated as written)
^6-6-2, ^6-6-4: «(Kha) paccanīkaṃ» is a plain line carrying the segment ID; kept plain.
^6-6-65: plain line «4 (Ṅa) paccanīkaokāso» (stray «4», the heading without ##### and ID) = «4 (đ) Chiều nghịch theo nơi chốn».
^6-6-16-5-0: «paccanīkaokāsā» = paccanīkaokāso (spelling), rendered as meant.
^6-6-69: «(Kha) yassa vā pana…pe….» ends with «.»; kept without «?».
^6-6-31: «…uppajjittha…pe…» has no final period; «(Yatthakampi sabbattha ekasadisaṃ).» period outside the bracket; both kept.
^6-6-81 / 82 / 86: unlabelled questions and «?…Pe…» (capital Pe); «?…» kept (builder whitelists the sample's «?…» check on these two lines).
^6-6-28 «na labbhati» vs ^6-6-86 «na kātabbaṃ»: rendered separately as written.
