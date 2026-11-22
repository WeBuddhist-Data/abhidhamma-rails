# pi-6 rails 10-05 (Indriyayamaka 5): (2) Atītavāro, (3) Anāgatavāro (Ka) anulomapuggalo

Builder: build_rails_10-05_vi.py (import with importlib). Setters: build_rails_10-04_vi (question11, tr_line), 10-03 (verb / split_mv, persons10, NEG_BOTH_RE), 10-02 (ind_persons, ind_answer_head, SEX, FEEL, faculty_mind_gen, PRON_FEM, NOCA_RE, heading, pv_unit), 10-01 (INDRIYA, ind_mulaka), 9-01 (verb, moment_vi, PAVATTE, ORDINAL, ANANTARA, THIS_MIND, EXTRA_PERSON), 5-01 (MIND_KIND['upapatti'], head_vi), 3-02 (ay_persons, ye_ca_head), 3-01 (PLANES_AY, AY_ATTRS), 2-02 (AND, REL), 2-01 (b_q, b_noca, b_both, ye_clause, place_head, SHORT), 7-01 (pair_q), 8 (MIND, PEOPLE, MOMENT); all READ-ONLY. Every line 10-04 parses is asserted byte-identical; every head 9-01 / 10-02 / 10-03 / 5-01 parse, likewise (exceptions listed below). Exposed for 10-06, 10-07, 10-12: `ETENEVA`, `BHAVE`, `KATICI`, `DASSETVA`, `KATICI_BHAVE`, `YE_REL`, `YE_CA_RE`, `YE_NOUN`, `YE_PERSON`, `ABS_JOIN`, `ye_clause12`, `ye_head12`, `is_ye_head`, `PACCHIMA_MIND`, `PACCHIMA_RE`, `ANANTARA_REL`, `pacchima_mind`, `anantara_group`, `plane_being_part`, `mind_gen12`, `head_parts12`, `answer_head12`, `question12`, `pv_sentence12`, `unit12`, `line12`, `tr_line`, `build`. Format: Pāli = tiếng Việt.


## Headings

(2) Atītavāro = (2) Mục về quá khứ
(3) Anāgatavāro = (3) Mục về tương lai
(Ka) anulomapuggalo = (a) Chiều thuận theo người
(Ga) anulomapuggalokāsā = (c) Chiều thuận theo người và nơi chốn
(Ca) paccanīkapuggalokāsā = (e) Chiều nghịch theo người và nơi chốn

## New: eteneva bhāvena / katici bhave dassetvā (Ye-clauses; user: eteneva bhāvena, bhava)

eteneva bhāvena = trong chính trạng thái ấy
katici bhave dassetvā = sau khi trải qua một số kiếp sống
katici / bhave / dassetvā = một số / kiếp sống / sau khi trải qua
Ye purisā eteneva bhāvena katici bhave dassetvā parinibbāyissanti tesaṃ … = Những người nam nào trong chính trạng thái ấy, sau khi trải qua một số kiếp sống, sẽ nhập Niết-bàn trọn vẹn, thì ở những người ấy …
Yā itthiyo eteneva bhāvena katici bhave dassetvā parinibbāyissanti tesaṃ … = Những người nữ nào trong chính trạng thái ấy, sau khi trải qua một số kiếp sống, sẽ nhập Niết-bàn trọn vẹn, thì ở những người ấy …
Yā itthiyo eteneva bhāvena katici bhave dassetvā upekkhāya upapajjitvā parinibbāyissanti tesaṃ … = Những người nữ nào trong chính trạng thái ấy, sau khi trải qua một số kiếp sống, sau khi tái sinh có sự bình thản đi kèm, sẽ nhập Niết-bàn trọn vẹn, thì ở những người ấy …
Ye purisā eteneva bhāvena katici bhave dassetvā somanassena upapajjitvā parinibbāyissanti tesaṃ … = Những người nam nào trong chính trạng thái ấy, sau khi trải qua một số kiếp sống, sau khi tái sinh có niềm vui đi kèm, sẽ nhập Niết-bàn trọn vẹn, thì ở những người ấy …
Ye sacakkhukā upekkhāya upapajjitvā parinibbāyissanti tesaṃ … = Những người có mắt nào sau khi tái sinh có sự bình thản đi kèm sẽ nhập Niết-bàn trọn vẹn, thì ở những người ấy …
Ye saghānakā somanassena upapajjitvā parinibbāyissanti tesaṃ … = Những người có mũi nào sau khi tái sinh có niềm vui đi kèm sẽ nhập Niết-bàn trọn vẹn, thì ở những người ấy …
Ye rūpāvacaraṃ upapajjitvā parinibbāyissanti ye ca purisā eteneva bhāvena katici bhave dassetvā parinibbāyissanti tesaṃ … = Những người nào sau khi tái sinh vào cõi hình sắc sẽ nhập Niết-bàn trọn vẹn và những người nam nào trong chính trạng thái ấy, sau khi trải qua một số kiếp sống, sẽ nhập Niết-bàn trọn vẹn, thì ở những người ấy …
Ye rūpāvacaraṃ arūpāvacaraṃ upapajjitvā parinibbāyissanti yā ca itthiyo eteneva bhāvena katici bhave dassetvā upekkhāya upapajjitvā parinibbāyissanti tesaṃ … = Những người nào sau khi tái sinh vào cõi hình sắc và cõi không hình sắc sẽ nhập Niết-bàn trọn vẹn và những người nữ nào trong chính trạng thái ấy, sau khi trải qua một số kiếp sống, sau khi tái sinh có sự bình thản đi kèm, sẽ nhập Niết-bàn trọn vẹn, thì ở những người ấy …
(For 10-06 / 10-07 / 10-12: «P ye ca purisā …» = 3-02 / 3-03 «Ở P và những người nam nào …»; several groups and clauses form one flat list «Ở A, B và …» (3-03 flat_persons):)
Rūpāvacarānaṃ ye ca purisā eteneva bhāvena katici bhave dassetvā parinibbāyissanti tesaṃ … = Ở chúng sinh trong cõi hình sắc và những người nam nào trong chính trạng thái ấy, sau khi trải qua một số kiếp sống, sẽ nhập Niết-bàn trọn vẹn, thì ở những người ấy …
Pacchimabhavikānaṃ ye ca arūpaṃ upapajjitvā parinibbāyissanti yā ca itthiyo eteneva bhāvena katici bhave dassetvā parinibbāyissanti tesaṃ … = Ở những người thuộc kiếp sống cuối cùng, những người nào sau khi tái sinh vào cõi không hình sắc sẽ nhập Niết-bàn trọn vẹn và những người nữ nào trong chính trạng thái ấy, sau khi trải qua một số kiếp sống, sẽ nhập Niết-bàn trọn vẹn, thì ở những người ấy …

## New: anantarā heads (person group; user: smooth, meaning unchanged)

Yassa cittassa anantarā upekkhāsampayuttapacchimacittaṃ uppajjissati tesaṃ … = Ở những người mà tâm cuối cùng gắn liền với sự bình thản sẽ sinh khởi ngay sau tâm này, thì ở những người ấy …
Yassa cittassa anantarā somanassasampayuttapacchimacittaṃ uppajjissati tesaṃ … = Ở những người mà tâm cuối cùng gắn liền với niềm vui sẽ sinh khởi ngay sau tâm này, thì ở những người ấy …
Yassa cittassa anantarā somanassasampayuttapacchimacittaṃ uppajjissati asaññasattānaṃ tesaṃ … (10-06 / 10-07) = Ở những người mà tâm cuối cùng gắn liền với niềm vui sẽ sinh khởi ngay sau tâm này và chúng sinh Vô Tưởng, thì ở những người ấy …
Pacchimacittasamaṅgīnaṃ yassa cittassa anantarā upekkhāsampayuttapacchimacittaṃ uppajjissati tesaṃ … (10-12) = Ở những người có được tâm cuối cùng và những người mà tâm cuối cùng gắn liền với sự bình thản sẽ sinh khởi ngay sau tâm này, thì ở những người ấy …

## Heads new in the Indriya chapters (9-01 / 5-01 / 3-02 strings)

Suddhāvāsānaṃ dutiye citte vattamāne asaññasattānaṃ tesaṃ tattha … = Ở chúng sinh trong cõi Tịnh Cư, khi tâm thứ hai đang diễn ra, ở chúng sinh Vô Tưởng, thì ở những người ấy, ở nơi ấy …
Itaresaṃ catuvokārānaṃ pañcavokārānaṃ tesaṃ tattha … = Ở chúng sinh khác trong cõi gồm bốn khối và cõi gồm năm khối, thì ở những người ấy, ở nơi ấy …
Suddhāvāsānaṃ upapatticittassa uppādakkhaṇe tesaṃ tattha … = Ở chúng sinh trong cõi Tịnh Cư, vào khoảnh khắc sinh khởi của tâm tái sinh, thì ở những người ấy, ở nơi ấy …
Suddhāvāsānaṃ upapajjantānaṃ asaññasattānaṃ tesaṃ tattha … = Ở chúng sinh trong cõi Tịnh Cư đang tái sinh và chúng sinh Vô Tưởng, thì ở những người ấy, ở nơi ấy …
Rūpāvacarānaṃ arūpāvacarānaṃ tesaṃ tattha … = Ở chúng sinh trong cõi hình sắc và cõi không hình sắc, thì ở những người ấy, ở nơi ấy …
Suddhāvāsānaṃ asaññasattānaṃ arūpānaṃ tesaṃ tattha … = Ở chúng sinh trong cõi Tịnh Cư, cõi Vô Tưởng và cõi không hình sắc, thì ở những người ấy, ở nơi ấy …
Itaresaṃ tesaṃ tattha … = Ở những người khác, thì ở những người ấy, ở nơi ấy …

## Sample lines

(Ka) yassa cakkhundriyaṃ uppajjittha tassa sotindriyaṃ uppajjitthāti? Āmantā. = (a) Ở người nào mà năng lực mắt đã sinh khởi, thì ở người ấy có phải năng lực tai đã sinh khởi không? Đúng vậy.
Rūpāvacare tattha cakkhundriyaṃ uppajjittha, no ca tattha ghānindriyaṃ uppajjittha. = Ở cõi hình sắc, thì ở nơi ấy năng lực mắt đã sinh khởi, nhưng ở nơi ấy không có năng lực mũi đã sinh khởi.
Asaññasatte arūpe tattha jīvitindriyaṃ uppajjittha, no ca tattha cakkhundriyaṃ uppajjittha. = Ở cõi Vô Tưởng, ở cõi không hình sắc, thì ở nơi ấy năng lực sống đã sinh khởi, nhưng ở nơi ấy không có năng lực mắt đã sinh khởi.
Rūpāvacare tattha ghānindriyaṃ na uppajjittha, no ca tattha cakkhundriyaṃ na uppajjittha. = Ở cõi hình sắc, thì ở nơi ấy năng lực mũi chưa từng sinh khởi, nhưng ở nơi ấy năng lực mắt đã từng sinh khởi.
Asaññasatte tattha cakkhundriyañca na uppajjittha upekkhindriyañca na uppajjittha. = Ở cõi Vô Tưởng, thì ở nơi ấy năng lực mắt chưa từng sinh khởi, năng lực bình thản cũng chưa từng sinh khởi.
(Ka) yattha cakkhundriyaṃ na uppajjittha tattha jīvitindriyaṃ na uppajjitthāti? Uppajjittha. = (a) Ở nơi nào mà năng lực mắt chưa từng sinh khởi, thì ở nơi ấy có phải năng lực sống chưa từng sinh khởi không? Đã sinh khởi.
Yassa cittassa anantarā upekkhāsampayuttapacchimacittaṃ uppajjissati tesaṃ jīvitindriyaṃ uppajjissati, no ca tesaṃ somanassindriyaṃ uppajjissati. = Ở những người mà tâm cuối cùng gắn liền với sự bình thản sẽ sinh khởi ngay sau tâm này, thì ở những người ấy năng lực sống sẽ sinh khởi, nhưng ở những người ấy không có năng lực niềm vui sẽ sinh khởi.
Itaresaṃ tesaṃ jīvitindriyañca uppajjissati somanassindriyañca uppajjissati. = Ở những người khác, thì ở những người ấy năng lực sống sẽ sinh khởi, năng lực niềm vui cũng sẽ sinh khởi.
Yā itthiyo eteneva bhāvena katici bhave dassetvā parinibbāyissanti tāsaṃ ghānindriyaṃ uppajjissati, no ca tāsaṃ purisindriyaṃ uppajjissati. = Những người nữ nào trong chính trạng thái ấy, sau khi trải qua một số kiếp sống, sẽ nhập Niết-bàn trọn vẹn, thì ở những người ấy năng lực mũi sẽ sinh khởi, nhưng ở những người ấy không có năng lực nam tính sẽ sinh khởi.

## Clashes between finished chapters (for the coordinator)

- A head that is only a run of plane-beings (Rūpāvacarānaṃ arūpāvacarānaṃ, Catuvokārānaṃ pañcavokārānaṃ, Suddhāvāsānaṃ asaññasattānaṃ [arūpānaṃ] … tesaṃ tattha): 10-02 ind_answer_head / 3-02 ay_persons / 2-01 / 9-01 / 5-01 give «Ở chúng sinh trong cõi hình sắc và cõi không hình sắc» (used in 2-01, 3-02 … 3-04, 5-01, 9-01); 10-03 head_parts10 would give «… và chúng sinh trong cõi không hình sắc» (never printed: 10-03 / 10-04 have no such head). Followed 10-02 / 3-02 (the earlier, printed form). Heads: Catuvokārānaṃ pañcavokārānaṃ, Rūpāvacarānaṃ arūpāvacarānaṃ, Suddhāvāsānaṃ asaññasattānaṃ, Suddhāvāsānaṃ asaññasattānaṃ arūpānaṃ.

## Termbase misfits and gaps (for the coordinator)

- katici «một số», dassetvā «sau khi trải qua» (no entries; commentary ^6-183: katici paṭisandhiyo gahetvā): katici bhave dassetvā «sau khi trải qua một số kiếp sống». Please confirm.
- Ye-clauses with eteneva bhāvena: the absolutives are set off by commas («Những người nam nào trong chính trạng thái ấy, sau khi trải qua một số kiếp sống, sẽ nhập Niết-bàn trọn vẹn»); without it 2-01's no-comma shape («Những người có mắt nào sau khi tái sinh có sự bình thản đi kèm sẽ nhập Niết-bàn trọn vẹn»).
- Ye sacakkhukā / saghānakā «Những người có mắt / có mũi nào» (termbase sacakkhukā «có mắt»; saghānakā has no entry: sibling Saghānakānaṃ «có mũi», 3-01). Ye purisā / Yā itthiyo «Những người nam / nữ nào» (termbase).
- somanassena / upekkhāya with upapajjitvā «sau khi tái sinh có niềm vui / có sự bình thản đi kèm» (10-02 feel_vi after the verb).
- yassa cittassa anantarā <X>pacchimacittaṃ uppajjissati: «những người mà tâm cuối cùng gắn liền với … sẽ sinh khởi ngay sau tâm này» = 6-01's anantara_group with the termbase kind of final mind (asserted); 9-01's «… ngay sau tâm này».
- Suddhāvāsānaṃ upapajjantānaṃ (genitive plane-being + participle; the English reads 'those being reborn in the Pure Abodes'): one group «chúng sinh trong cõi Tịnh Cư đang tái sinh» (9-01 / 10-02 parsers would split it into two groups «chúng sinh trong cõi Tịnh Cư, những người đang tái sinh …»): Suddhāvāsānaṃ upapajjantānaṃ asaññasattānaṃ (differs from: 10-02 head, 10-03 head, 5-01 head, 6-01 head, 9-01 head).

## Pāli as written (reported)

- ^6-10-240 «Yassa vā pana purisindriyaṃ uppajjittha tattha cakkhundriyaṃ uppajjitthāti?» (yassa … tattha; the parallels have tassa): translated as written «Còn ở người nào mà …, thì ở nơi ấy có phải … không?».
- ^6-10-256 «manindriyaṃ ca uppajjittha» (for manindriyañca): rendered as the both-frame.
- ^6-10-261 «jīvitindriyaṃ … somanassindriyaṃ» (space before the cut): «năng lực sống… năng lực niềm vui».
- ^6-10-243, ^6-10-263: an answer and the next (unlabelled) question with its answer stand on one line: kept.
- ^6-10-244 / 253 / 265 / 274 «Āmantā …pe….» = «Đúng vậy …» (10-01 / 10-02); ^6-10-261 «Natthi …pe….» = «Không có …».
- ^6-10-257 «(Ka) yassa yattha upekkhindriyaṃ … manindriyaṃ uppajjitthāti?» labelled (Ka), then an unlabelled «Yassa vā pana …»: kept as written.
- ^6-10-276 «Suddhāvāsānaṃ upapatticittassa uppādakkhaṇe tesaṃ tattha …»: «Ở chúng sinh trong cõi Tịnh Cư, vào khoảnh khắc sinh khởi của tâm tái sinh, …» (5-01).
- ^6-10-282, ^6-10-283 «Itaresaṃ tesaṃ …» after «Yā itthiyo … tāsaṃ»: «Ở những người khác, thì ở những người ấy …» (tāsaṃ = tesaṃ, 10-02).
