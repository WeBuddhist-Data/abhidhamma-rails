# notes-10-11: Indriyayamaka, pavattivāra, uppādavāra (5) paccuppannānāgatavāra, (Ca) paccanīkapuggalokāsā

Builder: build_10-11_vi.py (`importlib.import_module("build_10-11_vi")`; importing writes nothing).
Imports and uses verbatim: build_10-04_vi (translate_sentence for every «yassa yattha» question and «…pe…» run, mūlaka notes; P4_NOT / P4_BOTH), build_10-08_vi (_persons / _moment: every present-tense person stretch and «<kind>cittassa» moment), build_10-07_vi (head rule; last_kind), build_10-05_vi (YE_FRAME, BHAVA, BHAVA_AND, UPA_ATTR, YE_NOUN, YE_ATTR, SAHA, ye_bhava, ye_attr, last_citta), build_10-02_vi (fm, ATTR10, PAVATTE, split10, heading), build_2-01_vi (b_not / b_both, vparse, who, HEAD, PACCHIMA, PARTICIPLE, WHO_HEAD, LIST_SEP), build_2-02_vi (YE_CA_CAVANTA, YE_CA_JOIN), build_3-03_vi (YE_CA_UPAPAJJANTA), build_3-01_vi (ATTR_GROUP, ATTR_JOIN), build_5-01_vi (SABBESAM_ALONE), build_6-01_vi (ANANTARA), build_8_vi (AT / OF / MOMENT, when, SAMANGI, citta(last=True)). Labels: build_sample_vi.LABEL.
Byte-identity checks in the builder: sentences = 10-09 (163), 10-10 (185, one known difference below), 10-12 (96), 10-08 (132), 10-04 (78), 10-05 / 10-06 / 10-07 (71 each), 10-03 (62), 10-02 (9); heads = 10-09 head9 (92), 10-10 head10x (114), 10-08 head8 (61), 3-02 who32 (40), 3-01 who3 (27), 10-12 head12 (25), 10-04 head4 (7), 10-03 head13 (7).
Format: Pāli = tiếng Việt. [N] = imported from build_N_vi; [new] = settled here (all = 10-09, settled in the same run).

## Reused unchanged
##### (Ca) paccanīkapuggalokāsā = ##### (e) Chiều nghịch theo người và nơi chốn [sample SECTION, B.LABEL]
(Ka) yassa yattha X na uppajjati tassa tattha Y na uppajjissatīti? = (a) Ở người nào, ở nơi nào mà X không sinh khởi, thì ở người ấy, ở nơi ấy có phải Y sẽ không sinh khởi không? [2-01 / 10-04]
G tesaṃ tattha X na uppajjati, no ca tesaṃ tattha Y na uppajjissati. = G, thì ở những người ấy, ở nơi ấy X không sinh khởi, nhưng ở những người ấy, ở nơi ấy Y vẫn sẽ sinh khởi. [2-01 b_not]; …Xñca na uppajjati Yñca na uppajjissati = …, đồng thời Y cũng sẽ không sinh khởi [2-01 b_both]; tāsaṃ = tesaṃ [10-02]
Present heads (Pañcavokārā cavantānaṃ acakkhukānaṃ kāmāvacaraṃ upapajjantānaṃ, Sabbesaṃ cavantānaṃ acakkhukānaṃ upapajjantānaṃ, Kāmāvacarā cavantānaṃ na itthīnaṃ kāmāvacaraṃ upapajjantānaṃ, Catuvokārā pañcavokārā cavantānaṃ pavatte cittassa bhaṅgakkhaṇe, Sabbesaṃ cittassa bhaṅgakkhaṇe <kind>vippayuttacittassa uppādakkhaṇe …) [10-08 head8]
Pacchimacittassa uppādakkhaṇe / bhaṅgakkhaṇe = Vào khoảnh khắc sinh khởi / tan rã của tâm cuối cùng [8 P_SUBJ]
eteneva bhāvena katici bhave dassetvā …, sacakkhukā / saghānakā upekkhāya / somanassena upapajjitvā …, upekkhā- / somanassasampayuttapacchimacittaṃ = tâm cuối cùng gắn liền với sự bình thản / với niềm vui [10-05]
(Xmūlakaṃ) = (Phần dựa trên X) [3-01 / 10-02]

## New (identical to the 10-09 frames)
ye ca / yā ca <clause> parinibbāyissanti tesaṃ cavantānaṃ / tāsaṃ cavantīnaṃ = và những <người / người nam / người nữ> đang chết đi mà sau khi <…> sẽ nhập Niết-bàn trọn vẹn [YE_PART = 2-02 YE_CA_CAVANTA shape, asserted]
… tesaṃ upapajjantānaṃ / tāsaṃ upapajjantīnaṃ = và những <…> đang tái sinh mà sau khi <…> sẽ nhập Niết-bàn trọn vẹn [3-03 YE_CA_UPAPAJJANTA shape, asserted; = 10-09]
 e.g. ye ca purisā eteneva bhāvena katici bhave dassetvā parinibbāyissanti tesaṃ cavantānaṃ = và những người nam đang chết đi mà sau khi trải qua một số kiếp sống trong chính trạng thái ấy sẽ nhập Niết-bàn trọn vẹn
 ye ca sacakkhukā upekkhāya upapajjitvā parinibbāyissanti tesaṃ cavantānaṃ = và những người đang chết đi mà sau khi tái sinh có mắt và có sự bình thản đi kèm sẽ nhập Niết-bàn trọn vẹn
ye ca upekkhāya / somanassena upapajjitvā … tesaṃ cavantānaṃ = và những người đang chết đi mà sau khi tái sinh có sự bình thản / niềm vui đi kèm sẽ … [10-05 UPA_ATTR + SAHA; = 10-12 without the participle]
ye ca purisā / yā ca itthiyo upekkhāya / somanassena upapajjitvā … tesaṃ / tāsaṃ <participle> = và những người nam / nữ đang <…> mà sau khi tái sinh có sự bình thản / niềm vui đi kèm sẽ … [10-05 YE_NOUN; = 10-09]
Pacchimabhavikānaṃ itthīnaṃ upapajjantīnaṃ / purisānaṃ upapajjantānaṃ / saghānakānaṃ upapajjantānaṃ = Ở những người thuộc kiếp sống cuối cùng đang tái sinh là người nữ / là người nam / có mũi [ONE group, as 2-01 who «Pacchimabhavikānaṃ <plane>ṃ upapajjantānaṃ»; = 10-09 head9]
<K>pacchimacittassa uppādakkhaṇe / bhaṅgakkhaṇe = vào khoảnh khắc sinh khởi / tan rã của tâm cuối cùng <K> [8 moment + 10-05 last_citta; = 10-09]
yassa cittassa anantarā <K>pacchimacittaṃ uppajjissati tassa cittassa uppādakkhaṇe / bhaṅgakkhaṇe = vào khoảnh khắc sinh khởi / tan rã của tâm mà ngay sau đó <tâm cuối cùng K> sẽ sinh khởi [6-01 ANANTARA relative under the 8 moment; = 10-09]
<K>pacchimacittasamaṅgīnaṃ = những người có được tâm cuối cùng <K> (upekkhāsampayutta- = gắn liền với sự bình thản) [8 SAMANGI + 10-05 last_citta]
Head rule head11: consecutive persons share one «ở» (2-01 / 10-07 / 10-08), a time phrase stands alone, «ye ca» joins the person before it with « và » (2-02), pieces joined «, ».

## Known difference (for the coordinator)
10-10 (same run, head10x / translate_sentence, unfinished when this was built) splits «Pacchimabhavikānaṃ saghānakānaṃ upapajjantānaṃ» into two groups («những người thuộc kiếp sống cuối cùng, những người đang tái sinh có mũi») while keeping «… itthīnaṃ upapajjantīnaṃ» as one; 10-09 and this chapter keep one group for both. 10-08 head8 / 3-02 who32 never met this Pāli.

## Source points (translated as written)
^6-10-398 (line 93): «Pacchimabhavikānaṃ purisānaṃ uppajjantānaṃ» (uppajjati «arise») where every parallel has upapajjantānaṃ («being reborn»); spelling slip, rendered as upapajjantānaṃ «đang tái sinh».
^6-10-396 (line 49): the (Ka) both-answer has «ye ca upekkhāya upapajjitvā …» without «saghānakā», though the (Kha) answer (line 51) has «ye ca saghānakā upekkhāya …»; as written.
^6-10-396 (line 59): «Pacchimabhavikānaṃ saghānakānaṃ upapajjantānaṃ» where the parallel rows have «… kāmāvacaraṃ upapajjantānaṃ»; as written.
^6-10-397 (line 64 …): «Pacchimabhavikānaṃ itthīnaṃ upapajjantīnaṃ … tāsaṃ tattha», then «tesaṃ tattha» after mixed groups; same Vietnamese.
Several pairs carry no (Ka) / (Kha) label (questions with a «…pe…» run); no label written, as 10-04 … 10-09.

## For review
«vào khoảnh khắc tan rã của tâm mà ngay sau đó tâm cuối cùng … sẽ sinh khởi» (one phrase, = 10-09) and the long heads with «và những người … đang chết đi mà sau khi …» clauses keep every Pāli clause but read heavily.
