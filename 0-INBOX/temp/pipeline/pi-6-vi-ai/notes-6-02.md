# notes-6-02: Saṅkhārayamaka part 2 (6-02-sankharayamaka.md)

Builder: build_6-02_vi.py (import with importlib: `importlib.import_module("build_6-02_vi")`; importing writes nothing).
It imports build_6-01_vi (members, head() items, translate_sentence, fragments, editorial vocabulary), and through it
build_2-01_vi (family B), build_2-02_vi (family E, Nirodhavāro. / Uppādanirodhavāro.), build_8_vi (moments) and
build_sample_vi (labels, SECTION, ADI, yamaka_end, HOMAGE). Its head() = 6-01's head() plus the moments below; the build
asserts that all 319 answer heads 6-01 can parse (6-01 and 6-02 Pāli) come out byte-identical.
Format: Pāli = tiếng Việt. [6-01] / [2-02] / [8] / [sample] = imported; [new] = settled here.

## Reused unchanged
Members, verbs, question / answer frames (b_q, b_not, b_both, b_short), beings, planes, jhānas, «vinā …», ANANTARA,
fragments «…pe…»: 6-01 / 2-01. Pariññā questions: 2-02 translate_e with 6-01 m(). Labels: build_sample_vi.LABEL.
Nirodhavāro. = Mục về sự chấm dứt.; Uppādanirodhavāro. = Mục về sự sinh khởi và sự chấm dứt.; Pariññāvāro. = Mục về sự hiểu biết trọn vẹn. [2-02]
Saṅkhārayamakaṃ niṭṭhitaṃ. = Phần các cặp câu hỏi về các tạo tác đã hoàn tất. [sample yamaka_end]
Namo tassa bhagavato arahato sammāsambuddhassa = Kính lễ Đức Thế Tôn, bậc A-la-hán, bậc Tự Giác Ngộ Hoàn Toàn [sample HOMAGE]
(Ka) yo kāyasaṅkhāraṃ parijānāti so vacīsaṅkhāraṃ parijānātīti? = (a) Người nào hiểu biết trọn vẹn sự tạo tác bằng thân, thì có phải người ấy hiểu biết trọn vẹn sự tạo tác bằng lời nói không? [2-02]

## Answer heads (new moments)
pacchimacittassa uppādakkhaṇe / bhaṅgakkhaṇe = vào khoảnh khắc sinh khởi / tan rã của tâm cuối cùng [8 P_SUBJ, asserted]
avitakkaavicārapacchimacittassa Xkkhaṇe = vào khoảnh khắc … của tâm cuối cùng không có sự hướng tâm cũng không có sự duy trì tâm [6-01 LAST_AVITAKKA]
kāmāvacarānaṃ pacchimacittassa uppādakkhaṇe = vào khoảnh khắc sinh khởi của tâm cuối cùng của chúng sinh trong cõi dục lạc [6-01 ANANTARA_K]
Kāmāvacare / Rūpāvacare arūpāvacare / Savitakkasavicārabhūmiyaṃ + pacchimacittassa bhaṅgakkhaṇe = Trong cõi dục lạc / Trong cõi hình sắc, cõi không hình sắc / Ở cấp độ có …, + vào khoảnh khắc tan rã của tâm cuối cùng [6-01 items joined by ", "]

## Headings
Pavatti 3. uppādanirodhavāro = Sự diễn tiến 3. mục về sự sinh khởi và sự chấm dứt [new; = «Pavatti 2. nirodhavāro» pattern, SECTION]
1-6. Paccuppannavārādi = 1-6. Mục về hiện tại và các mục khác [new; sample ADI «2-10. Hetuvārādi»]

## Editorial lines [new]
<place> tattha…pe… (itaresaṃ yatthakānaṃ sadisaṃ). = Trong tầng thiền thứ hai, tầng thiền thứ ba, thì ở nơi ấy… (giống như các phần về nơi chốn khác).
<fragment>…pe… (yassakampi yassayatthakampi sadisaṃ). = <fragment>… (phần về người và phần về người và nơi chốn đều giống nhau).
(Yassakampi yassayatthakampi sadisaṃ, yassayatthake nirodhasamāpannānanti na labbhati). = (Phần về người và phần về người và nơi chốn đều giống nhau, trong phần về người và nơi chốn thì không có trường hợp những người nhập thành tựu thiền chấm dứt).
(Atītā pucchā uppādavārepi nirodhavārepi uppādanirodhavārepi sadisaṃ vitthāretabbā). = (Các câu hỏi về quá khứ, cả trong mục về sự sinh khởi, trong mục về sự chấm dứt lẫn trong mục về sự sinh khởi và sự chấm dứt, đều nên được trình bày chi tiết giống nhau).
paccuppannātītā pucchā = các câu hỏi về hiện tại và quá khứ; atītānāgatā pucchā = các câu hỏi về quá khứ và tương lai; anulomampi paccanīkampi = cả chiều thuận lẫn chiều nghịch [6-01]
(Yathā uppādavāre paccuppannātītā pucchā … vibhattā evaṃ uppādavāranirodhavārepi … vibhajitabbā.) = (Như các câu hỏi về hiện tại và quá khứ, cả chiều thuận lẫn chiều nghịch, đã được phân tích trong mục về sự sinh khởi, trong mục về sự sinh khởi và sự chấm dứt, các câu hỏi về hiện tại và quá khứ, cả chiều thuận lẫn chiều nghịch, cũng nên được phân tích như vậy.)
(Yathā nirodhavāre atītānāgatā pucchā … evaṃ uppādanirodhavārepi … vibhajitabbaṃ asammohantena nirodhavārena sadisaṃ, natthi nānākaraṇaṃ.) = (Như …, trong mục về sự chấm dứt, thì trong mục về sự sinh khởi và sự chấm dứt, …, cũng nên được phân tích một cách không nhầm lẫn, giống như mục về sự chấm dứt, không có sự khác biệt.)
asammohantena = một cách không nhầm lẫn
(Yathā khandhayamake pariññāvāraṃ vibhattaṃ evaṃ saṅkhārayamakepi pariññāvāraṃ vibhajitabbaṃ.) = (Như mục về sự hiểu biết trọn vẹn đã được phân tích trong phần các cặp câu hỏi về các khối, trong phần các cặp câu hỏi về các tạo tác, mục về sự hiểu biết trọn vẹn cũng nên được phân tích như vậy.)
<X>yamake (inside a note) = trong phần <yamaka title, lowercase> (as yamaka_end; no “…”, since the Pāli has no quotes)

## Source points (translated as written)
^6-6-121 (Ka), 2nd answer: «kāyasaṅkhāro na nirujjhittha vacīsaṅkhāro ca nirujjhissati» («na» where the both-frame has «ca»; probably a slip) = «sự tạo tác bằng thân chưa từng chấm dứt, đồng thời sự tạo tác bằng lời nói cũng sẽ chấm dứt».
^6-6-132 (Ka): «yassa kāyasaṅkhāro nuppajjati tassa cittasaṅkhāro nirujjhatīti?» lacks «na» (series and answer have «na nirujjhati»); question kept positive.
^6-6-147: «uppādavāranirodhavārepi» (one compound, singular locative) read as the uppādanirodhavāra = «trong mục về sự sinh khởi và sự chấm dứt».
^6-6-130, ^6-6-136: unlabelled questions, kept unlabelled.
