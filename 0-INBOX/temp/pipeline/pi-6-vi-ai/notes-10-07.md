# notes-10-07: Indriyayamaka, pavattivāra, uppādavāra (3) anāgatavāra, (Ca) paccanīkapuggalokāsā

Builder: build_10-07_vi.py (`importlib.import_module("build_10-07_vi")`; importing writes nothing).
Imports and uses verbatim: build_10-04_vi (translate_sentence for every «yassa yattha» question, Āmantā and mūlaka note; P4_NOT / P4_BOTH), build_10-02_vi (fm, run_vi, split10, heading, SAMPAYUTTA, KIND_NOUN), build_10-05_vi (ye_bhava, ye_attr, last_citta: settled there first for the same Pāli), build_2-01_vi (b_not / b_both res «tesaṃ tattha», vparse, who, WHO_HEAD, LIST_SEP), build_2-02_vi (YE_CA_JOIN), build_6-01_vi (ANANTARA), build_8_vi (SAMANGI, citta(last=True)), build_9-01_vi (head rule). Labels: build_sample_vi.LABEL.
Byte-identity checks in the builder: 97 sentences = build_10-04_vi.translate_sentence, 34 = build_10-02_vi, 133 = build_10-05_vi, 156 = build_10-06_vi (see the one warning below); answer heads: 37 = 10-05 head5, 60 = 10-06 head6 (same warning).
Format: Pāli = tiếng Việt. [N] = imported from build_N_vi; [new] = settled here.

## Reused unchanged
##### (Ca) paccanīkapuggalokāsā = (e) Chiều nghịch theo người và nơi chốn [sample SECTION, B.LABEL; = 10-04]
(Ka) yassa yattha X na uppajjissati tassa tattha Y na uppajjissatīti? = (a) Ở người nào, ở nơi nào mà X sẽ không sinh khởi, thì ở người ấy, ở nơi ấy có phải Y sẽ không sinh khởi không? [2-01 / 10-04]
G tesaṃ tattha X na uppajjissati, no ca tesaṃ tattha Y na uppajjissati. = G, thì ở những người ấy, ở nơi ấy X sẽ không sinh khởi, nhưng ở những người ấy, ở nơi ấy Y vẫn sẽ sinh khởi. [2-01 b_not, deny fut]
G tesaṃ tattha Xñca na uppajjissati Yñca na uppajjissati. = G, thì ở những người ấy, ở nơi ấy X sẽ không sinh khởi, đồng thời Y cũng sẽ không sinh khởi. [2-01 b_both]
tāsaṃ tattha = ở những người ấy, ở nơi ấy (as tesaṃ) [10-02 / 10-05]
Pacchimabhavikānaṃ / Pañcavokāre pacchimabhavikānaṃ / Kāmāvacare pacchimabhavikānaṃ = Ở những người thuộc kiếp sống cuối cùng [trong cõi gồm năm khối / trong cõi dục lạc] [2-01 who]
Rūpāvacarānaṃ arūpāvacarānaṃ = Ở chúng sinh trong cõi hình sắc, cõi không hình sắc; Asaññasattānaṃ arūpānaṃ = Ở chúng sinh Vô Tưởng, chúng sinh trong cõi không hình sắc [2-01 who over the whole run]
Pacchimacittasamaṅgīnaṃ = Ở những người có được tâm cuối cùng [8]
Yassa cittassa anantarā upekkhā- / somanassasampayuttapacchimacittaṃ uppajjissati = Vào tâm mà ngay sau đó tâm cuối cùng gắn liền với sự bình thản / với niềm vui sẽ sinh khởi [6-01 ANANTARA + 10-05 last_citta]; a time phrase stands alone, persons after it take their own «ở» [9-01 / 6-01]
Ye purisā / Yā itthiyo eteneva bhāvena katici bhave dassetvā [upekkhāya / somanassena upapajjitvā] parinibbāyissanti = Những người nam / nữ nào sau khi trải qua một số kiếp sống trong chính trạng thái ấy [và tái sinh có sự bình thản / niềm vui đi kèm] sẽ nhập Niết-bàn trọn vẹn [10-05 ye_bhava]
… ye ca purisā / yā ca itthiyo … = … và những người nam / nữ nào … [2-02 YE_CA_JOIN + 10-05]
Ye sacakkhukā / saghānakā upekkhāya / somanassena upapajjitvā parinibbāyissanti = Những người nào sau khi tái sinh có mắt / có mũi và có sự bình thản / niềm vui đi kèm sẽ nhập Niết-bàn trọn vẹn [10-05 ye_attr]
(Xmūlakaṃ) = (Phần dựa trên X) [3-01 / 10-02]

## New
No new frame: every head element of this chapter is a 2-01 / 6-01 / 8 / 10-05 frame; head7() only combines them by the 9-01 / 10-04 / 10-05 head rule (consecutive persons share one «ở», a time phrase stands alone, «ye ca» joins with « và », a nominative «ye …» head has no «ở»).

## Warning for the coordinator (10-06, running in parallel)
build_10-06_vi.head6 writes «ở» before each person element after the first: «Ở những người thuộc kiếp sống cuối cùng, ở chúng sinh Vô Tưởng» (Pacchimabhavikānaṃ asaññasattānaṃ), «Ở những người có được tâm cuối cùng, ở chúng sinh Vô Tưởng» (Pacchimacittasamaṅgīnaṃ asaññasattānaṃ). 2-01 who, 9-01, 10-04 head4, 10-05 head5 and 3-02 / 3-03 / 3-06 / 6-01 write one «ở» over the run; this chapter follows them. All other 10-06 sentences that also occur here are byte-identical.

## Source points (translated as written)
^6-10-326 … ^6-10-333: several pairs carry no (Ka) / (Kha) label (Yassa yattha … / Yassa vā pana yattha …); no label written.
^6-10-332: the closing question begins on the same line as the answer; kept on that line.
^6-10-328 / ^6-10-329: «Rūpāvacarānaṃ yā ca itthiyo … tesaṃ tattha» (masculine resumptive after a mixed group), «Yā itthiyo … tāsaṃ tattha»; same Vietnamese.
No spelling slips found.

## For review
Same as notes-10-05: «trong chính trạng thái ấy» (eteneva bhāvena), «Vào tâm mà ngay sau đó …» (6-01 frame).
