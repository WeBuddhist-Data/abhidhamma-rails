# notes-10-05: Indriyayamaka, pavattivāra, uppādavāra (2) atītavāra (all six sections) and (3) anāgatavāra (Ka) anulomapuggalo

Builder: build_10-05_vi.py (`importlib.import_module("build_10-05_vi")`; importing writes nothing).
Imports and uses verbatim: build_10-02_vi (fm, ATTR10, citta_kind, split10, heading, MULAKA_RE, run_vi, translate_sentence for every place answer and «Āmantā …pe….»), build_2-01_vi (b_q / Q_FRAME, b_not, b_both, b_short, vparse, who, WHO_HEAD, LIST_SEP, BEINGS_OF, PLANE, PARTICIPLE, YE_UPAPAJJITVA, NATTHI), build_2-02_vi (YE_CA_JOIN, pe_end), build_3-01_vi (ATTR, ATTR_JOIN, MULAKA), build_3-02_vi (_ye_planes), build_5-01_vi (VATTAMANA, CITTA_KIND, _moment), build_6-01_vi (ANANTARA), build_8_vi (citta(last=True)). Labels: build_sample_vi.LABEL.
Byte-identity checks in the builder: 449 sentences = build_10-02_vi.translate_sentence, 342 = build_10-03_vi, 578 = build_10-04_vi; 60 answer heads = 5-01 head_vi (one known difference, below), 84 = 6-01 head(); 48 «…pe…» runs = 10-02 run_vi.
Format: Pāli = tiếng Việt. [N] = imported from build_N_vi; [new] = settled here.

## Reused unchanged
#### (2) Atītavāro = (2) Mục về quá khứ; #### (3) Anāgatavāro = (3) Mục về tương lai; the six section headings [sample SECTION via 2-01 heading]
uppajjittha / na uppajjittha = đã sinh khởi / chưa từng sinh khởi; after «no ca» on na uppajjittha = đã từng sinh khởi; uppajjissati = sẽ sinh khởi, after no ca = sẽ không sinh khởi [2-01]
Uppajjittha. (short answer) = Đã sinh khởi. [2-01 b_short]
Rūpāvacare / Kāmāvacare / Asaññasatte arūpe / Catuvokāre pañcavokāre … tattha = Trong cõi hình sắc / cõi dục lạc / cõi Vô Tưởng, cõi không hình sắc / cõi gồm bốn khối, cõi gồm năm khối …, thì ở nơi ấy [3-01 where3 via 10-02]
Rūpāvacarānaṃ arūpāvacarānaṃ tesaṃ tattha = Ở chúng sinh trong cõi hình sắc, cõi không hình sắc, thì ở những người ấy, ở nơi ấy [2-01 who over the whole run; = 6-01]
Asaññasattānaṃ arūpānaṃ = Ở chúng sinh Vô Tưởng, chúng sinh trong cõi không hình sắc; Suddhāvāsānaṃ asaññasattānaṃ arūpānaṃ = Ở chúng sinh trong cõi Tịnh Cư, chúng sinh Vô Tưởng, chúng sinh trong cõi không hình sắc [2-01 who]
Itaresaṃ catuvokārānaṃ pañcavokārānaṃ = Ở những chúng sinh khác trong cõi gồm bốn khối, cõi gồm năm khối [2-01 who; = 5-01]
Suddhāvāsānaṃ dutiye citte vattamāne [asaññasattānaṃ] = Ở chúng sinh trong cõi Tịnh Cư, khi tâm thứ hai đang diễn ra[, ở chúng sinh Vô Tưởng] [5-01 head_vi; = 6-01]
Suddhāvāsānaṃ upapatticittassa uppādakkhaṇe = Ở chúng sinh trong cõi Tịnh Cư, vào khoảnh khắc sinh khởi của tâm tái sinh [5-01]
Ye rūpāvacaraṃ [arūpāvacaraṃ] upapajjitvā parinibbāyissanti = Những người nào sau khi tái sinh vào cõi hình sắc[, cõi không hình sắc] sẽ nhập Niết-bàn trọn vẹn [2-01 / 3-02]; Itaresaṃ tesaṃ = Ở những người khác, thì ở những người ấy [2-01]
… ye ca … = … và … [2-02 YE_CA_JOIN]
Yassa cittassa anantarā <K> pacchimacittaṃ uppajjissati = Vào tâm mà ngay sau đó <tâm cuối cùng …> sẽ sinh khởi [6-01 ANANTARA]
Natthi …pe…. = Không có… [2-02 pe_end, the 7-04 rule]; Āmantā …pe…. = Đúng vậy… [7-04]

## New
eteneva bhāvena katici bhave dassetvā = sau khi trải qua một số kiếp sống trong chính trạng thái ấy [new; aṭṭhakathā ^6-183 «etena purisabhāveneva … katici paṭisandhiyo gahetvā»; bhāva «trạng thái» as pi-1 itthibhāva / purisabhāva, bhava «kiếp sống» as 2-01 pacchimabhavika]
Ye purisā eteneva bhāvena katici bhave dassetvā parinibbāyissanti = Những người nam nào sau khi trải qua một số kiếp sống trong chính trạng thái ấy sẽ nhập Niết-bàn trọn vẹn [new; frame = 2-01 YE_UPAPAJJITVA]
Yā itthiyo … = Những người nữ nào …; tāsaṃ = ở những người ấy (as 10-02) [new]
… dassetvā upekkhāya / somanassena upapajjitvā parinibbāyissanti = … sau khi trải qua một số kiếp sống trong chính trạng thái ấy và tái sinh có sự bình thản / niềm vui đi kèm sẽ nhập Niết-bàn trọn vẹn [new; 10-02 ATTR10]
Ye sacakkhukā / saghānakā upekkhāya / somanassena upapajjitvā parinibbāyissanti = Những người nào sau khi tái sinh có mắt / có mũi và có sự bình thản / niềm vui đi kèm sẽ nhập Niết-bàn trọn vẹn [new; 3-01 ATTR + ATTR_JOIN, 10-02 order «tái sinh có mắt và …»]
upekkhāsampayuttapacchimacittaṃ / somanassasampayuttapacchimacittaṃ = tâm cuối cùng gắn liền với sự bình thản / với niềm vui [new; «cuối cùng» first as 6-01 LAST_AVITAKKA, kind from 10-02 citta_kind]
A run in the first slot (Yassa X…pe… Y… Z uppajjittha tassa W …) = «Ở người nào mà X… Y… Z đã sinh khởi, …»; a bare «…» between faculties = «…» as …pe… [new, 10-02 run_vi]

## Source points (translated as written)
^6-10-240 (line 10): «Yassa vā pana purisindriyaṃ uppajjittha tattha cakkhundriyaṃ …» has «tattha» for «tassa» in the person section; as written «thì ở nơi ấy …».
^6-10-256 (line 167): «manindriyaṃ ca uppajjittha» written apart (= manindriyañca); same Vietnamese.
^6-10-261 (line 195): «jīvitindriyaṃ …» with a space before «…»; «…» written without it.
^6-10-277 (line 330): «Suddhāvāsānaṃ upapajjantānaṃ» genitive (the parallels have «Suddhāvāsaṃ upapajjantānaṃ»); as written «Ở chúng sinh trong cõi Tịnh Cư đang tái sinh» (5-01 head_vi, which has no rule for it, would split it into two groups: not followed).
Lines 58 and 207: a new question starts on the line of an answer; kept on that line. Line 169: (Ka) on a question whose pair (line 170) has no label; kept.

## For review
«trong chính trạng thái ấy» (eteneva bhāvena = still as a man / woman, aṭṭhakathā); a plainer alternative «vẫn là người nam / nữ».
«Vào tâm mà ngay sau đó …» (6-01 frame) reads stiffly; any change belongs to the harmonise pass with 6-01.
