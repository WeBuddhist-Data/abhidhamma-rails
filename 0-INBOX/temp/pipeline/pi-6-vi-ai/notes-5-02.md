# notes-5-02: Saccayamaka (nirodhavāra (1)-(6), uppādanirodhavāra (1)-(4)), frames for 5-03

Builder: build_5-02_vi.py (`importlib.import_module("build_5-02_vi")`; importing writes nothing). It imports build_5-01_vi (T: members, head_vi, the family A / B sentence parser), build_2-01_vi, build_2-02_vi, build_8_vi and build_6-01_vi (editorial-note words). Every answer, question and head frame is the 5-01 one; only the items below are new.
Additive, in-memory extensions of build_5-01_vi made on import: a HEAD_RULES_C entry for «pacchimacittassa …kkhaṇe», a VAR_TAIL entry, and T._groups accepts a variant bracket that closes a head. 5-03 gets them by importing build_5-02_vi.
Format: Pāli = tiếng Việt. [5-01] / [6-01] / [8] / [2-02] / [sample] = frame-setters and finished chapters; [pi-N] = approved pi-N rails; [new] = settled here.
Labels: always build_sample_vi.LABEL.

## Headings and closing lines
Pavatti 3. uppādanirodhavāro = Sự diễn tiến 3. mục về sự sinh khởi và sự chấm dứt [new; = sample «Pavatti 2. nirodhavāro» «Sự diễn tiến 2. mục về sự chấm dứt»]
Nirodhavāro. = Mục về sự chấm dứt. [2-02]

## Answer heads (additions to head_vi)
Pacchimacittassa uppādakkhaṇe / bhaṅgakkhaṇe = Vào khoảnh khắc sinh khởi / tan rã của tâm cuối cùng [8 citta(last=True); = 6-01]
<head> [variant] tesaṃ … (bracket closing the head) = <Vietnamese head> [dị bản …], thì ở những người ấy … [new]
variant tail «uppādavāre pana pāṭhantaraṃ natthi» = «, nhưng trong mục về sự sinh khởi thì không có dị bản» [new; pāṭhantara = the label «dị bản»]

## Shortened sentences
(Kha) yassa vā pana…pe…. / Yassa vā pana…pe…. = (b) Còn ở người nào… / Còn ở người nào… [6-01; «?» only where the Pāli has it]
Yattha / Yassa yattha X (na) v…pe…. = Ở nơi nào / Ở người nào, ở nơi nào mà X (không) v… [2-02 pe_fragment]
<Plane>e tattha X v…pe…. (half of a place answer) = Trong <cõi>, thì ở nơi ấy X v… [new; 2-01 STATEMENT_RES + 2-02 pe_end]
A whole answer ending «…pe….» = the answer with «…» for its period [2-02 pe_end]
<head1> tesaṃ tattha …pe… <head2> tesaṃ tattha…pe…. = <Head1>, thì ở những người ấy, ở nơi ấy … <head2>, thì ở những người ấy, ở nơi ấy… [new, ^6-5-148]

## Editorial notes
yassaka / yatthaka / yassayatthaka = phần về người / phần về nơi chốn / phần về người và nơi chốn [6-01]
sadisaṃ = đều giống nhau; natthi nānākaraṇaṃ = không có sự khác biệt [6-01; nānākaraṇa «sự khác biệt» pi-5]
Xampi Yampi = cả X lẫn Y (anulomampi paccanīkampi = cả chiều thuận lẫn chiều nghịch) [6-01]
uppāde / nirodhe / uppādanirodhe (bare) = ở sự sinh khởi / ở sự chấm dứt / ở sự sinh khởi và sự chấm dứt; uppādavāre / nirodhavāre / uppādanirodhavāre = ở / trong mục về sự sinh khởi / … sự chấm dứt / … sự sinh khởi và sự chấm dứt [new; sample SECTION]
(Yatthakaṃ uppādepi nirodhepi uppādanirodhepi sadisaṃ, natthi nānākaraṇaṃ). = (Phần về nơi chốn thì ở sự sinh khởi, ở sự chấm dứt, ở sự sinh khởi và sự chấm dứt đều giống nhau, không có sự khác biệt). [new; 3-01 «Phần về nơi chốn thì ở …, ở … đều giống nhau» shape]
(Yatthakaṃ uppādavārepi nirodhavārepi uppādanirodhavārepi sadisaṃ natthi nānākaraṇaṃ). = (Phần về nơi chốn thì ở mục về sự sinh khởi, ở mục về sự chấm dứt, ở mục về sự sinh khởi và sự chấm dứt đều giống nhau, không có sự khác biệt). [new]
(Yassayatthakampi sadisaṃ vitthāretabbaṃ). = (Phần về người và nơi chốn cũng nên được trình bày chi tiết giống như vậy). [= 5-01 «(Yassakampi yassayatthakampi …)»]
(Yassakampi yassayatthakampi sadisaṃ). = (Phần về người và phần về người và nơi chốn đều giống nhau). [6-01]
(Yassakampi yassayatthakampi sadisaṃ, yassayatthakepi nirodhasamāpannānanti na kātabbaṃ). = (Phần về người và phần về người và nơi chốn đều giống nhau, trong phần về người và nơi chốn cũng không nên đưa vào trường hợp những người nhập thành tựu thiền chấm dứt). [6-01 words]
(Yassakampi [var] yassayatthakampi sadisaṃ, yassayatthakepi nirodhasamāpannānanti cetaṃ na kātabbaṃ). = (Phần về người [dị bản (Sī., Syā.): yassakampi yatthakampi] và phần về người và nơi chốn đều giống nhau, và trong phần về người và nơi chốn cũng không nên đưa vào trường hợp …). [new; cetaṃ «và»]
(Yathā uppādavāre atītā pucchā anulomampi paccanīkampi vibhattā evaṃ nirodhepi vibhajitabbā, natthi nānākaraṇaṃ). = (Như các câu hỏi về quá khứ, cả chiều thuận lẫn chiều nghịch, đã được phân tích trong mục về sự sinh khởi, ở sự chấm dứt cũng nên phân tích như vậy, không có sự khác biệt). [6-01 frame]
(Atītā pucchā yathā uppādavāre vibhattā evaṃ uppādanirodhavārepi anulomampi paccanīkampi vibhajitabbaṃ). = (Như các câu hỏi về quá khứ đã được phân tích trong mục về sự sinh khởi, trong mục về sự sinh khởi và sự chấm dứt cũng nên phân tích như vậy, cả chiều thuận lẫn chiều nghịch). [6-01 frame]
samudayasaccaṃ maggasaccaṃ nānākaraṇaṃ = ở sự thật về sự phát sinh và sự thật về con đường thì có sự khác biệt [new, ^6-5-152; the example answer after it uses the normal B frame]
Paccuppannaatītā pucchā = Các câu hỏi về hiện tại và quá khứ [new; sample Paccuppannātītavāro]
asammohantena vibhajitabbā = nên phân tích mà không mê lầm [new; sammoha «sự mê lầm» pi-1]

## Source points in 5-02 (translated as written unless stated)
^6-5-125: «samudayasaccañca na nirujjhiti» = na nirujjhati (spelling; the question has «na nirujjhatīti»).
^6-5-130: the (Kha) question ends in «.»; written with «?» (missing punctuation); the builder whitelists this one «?» count (as 2-01 ^6-2-36).
^6-5-124: «asaññasattaṃ upapajjantānaṃ» stands twice in one head (before and after «arūpe aggamaggassa ca phalassa ca bhaṅgakkhaṇe»); both kept (as 5-01 ^6-5-76).
^6-5-97 / ^6-5-122: variant brackets close the answer head; they follow the last group in Vietnamese.
^6-5-138: no comma before «natthi nānākaraṇaṃ» (^6-5-90 has one); comma written. ^6-5-152: stray commas inside the head, no effect.
^6-5-148: «tesaṃ tattha …pe… itaresaṃ …» (two heads cut by …pe…) rendered with «…» at both points.
