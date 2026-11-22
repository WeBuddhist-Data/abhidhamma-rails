# pi-6 rails 10-03 (Indriyayamaka 3): (Ga) anulomapuggalokāsā, (Gha) paccanīkapuggalo

Builder: build_rails_10-03_vi.py (import with importlib). Setter: build_rails_10-02_vi (ind_persons, ind_group, sex_vi, feel_vi, faculty_mind_gen, ind_answer_head, PRON_FEM, heading); 9-01 verb (separate na), PAVATTE, moment_vi, ALL_BEINGS, EXTRA_PERSON; 2-01 b_q / b_noca / b_both; 3-01 BQ_RE; 10-01 INDRIYA / ind_mulaka; all READ-ONLY. Every line 10-02 parses, every head 9-01 / 10-02 parse and every question 3-01 parses is asserted byte-identical. Exposed: `verb`, `split_mv`, `PART_READING`, `SEX_ALSO`, `sex_list_vi`, `persons10`, `head_parts10`, `answer_head10`, `question10`, `NEG_BOTH_RE`, `pv_sentence10`, `unit10`, `line10`, `tr_line`, `build`. Format: Pāli = tiếng Việt.


## Headings

(Ga) anulomapuggalokāsā = (c) Chiều thuận theo người và nơi chốn
(Gha) paccanīkapuggalo = (d) Chiều nghịch theo người

## Verbs and questions (separate na)

na uppajjati = không sinh khởi
no ca tesaṃ B na uppajjati = nhưng ở những người ấy B vẫn sinh khởi
(Ka) yassa cakkhundriyaṃ na uppajjati tassa sotindriyaṃ na uppajjatīti? = (a) Ở người nào mà năng lực mắt không sinh khởi, thì ở người ấy có phải năng lực tai không sinh khởi không?
(Kha) yassa vā pana sotindriyaṃ na uppajjati tassa cakkhundriyaṃ na uppajjatīti? = (b) Còn ở người nào mà năng lực tai không sinh khởi, thì ở người ấy có phải năng lực mắt không sinh khởi không?
(Ka) yassa yattha cakkhundriyaṃ uppajjati tassa tattha sotindriyaṃ uppajjatīti? = (a) Ở người nào, ở nơi nào mà năng lực mắt sinh khởi, thì ở người ấy, ở nơi ấy có phải năng lực tai sinh khởi không?

## Person words and heads new here

na itthīnaṃ na purisānaṃ upapajjantānaṃ (two sex words, set here) = những người đang tái sinh không làm người nữ, cũng không làm người nam
uppajjantīnaṃ (termbase: the reading for upapajjantīnaṃ) = đang tái sinh
Sabbesaṃ cavantānaṃ acakkhukānaṃ asotakānaṃ upapajjantānaṃ = tất cả những người đang chết đi và những người không có mắt, không có tai đang tái sinh
Sabbesaṃ cavantānaṃ acakkhukānaṃ na itthīnaṃ upapajjantānaṃ = tất cả những người đang chết đi và những người không có mắt đang tái sinh không làm người nữ
Sabbesaṃ cavantānaṃ na itthīnaṃ acakkhukānaṃ upapajjantānaṃ = tất cả những người đang chết đi và những người không có mắt đang tái sinh không làm người nữ
Sabbesaṃ cavantānaṃ vinā somanassena acakkhukānaṃ upapajjantānaṃ = tất cả những người đang chết đi và những người không có mắt đang tái sinh không có niềm vui đi kèm
Sabbesaṃ cavantānaṃ acakkhukānaṃ vinā upekkhāya upapajjantānaṃ = tất cả những người đang chết đi và những người không có mắt đang tái sinh không có sự bình thản đi kèm
Sabbesaṃ cavantānaṃ vinā somanassena na itthīnaṃ upapajjantānaṃ = tất cả những người đang chết đi và những người đang tái sinh không làm người nữ, không có niềm vui đi kèm
Sabbesaṃ cavantānaṃ na itthīnaṃ vinā somanassena upapajjantānaṃ = tất cả những người đang chết đi và những người đang tái sinh không làm người nữ, không có niềm vui đi kèm
Sabbesaṃ cavantānaṃ na itthīnaṃ na purisānaṃ upapajjantānaṃ = tất cả những người đang chết đi và những người đang tái sinh không làm người nữ, cũng không làm người nam
Itthīnaṃ ñāṇasampayuttānaṃ uppajjantīnaṃ = những người gắn liền với hiểu biết đang tái sinh làm người nữ
Sabbesaṃ cavantānaṃ pavatte cittassa bhaṅgakkhaṇe tesaṃ … = Ở tất cả những người đang chết đi, trong đời sống, vào khoảnh khắc tan rã của tâm, thì ở những người ấy …
Sabbesaṃ cittassa bhaṅgakkhaṇe somanassavippayuttaupekkhāvippayuttacittassa uppādakkhaṇe nirodhasamāpannānaṃ asaññasattānaṃ tesaṃ … = Ở tất cả chúng sinh, vào khoảnh khắc tan rã của tâm, vào khoảnh khắc sinh khởi của tâm không gắn liền với niềm vui và không gắn liền với sự bình thản, ở những người nhập thành tựu thiền chấm dứt và chúng sinh Vô Tưởng, thì ở những người ấy …
Sabbesaṃ cittassa bhaṅgakkhaṇe nirodhasamāpannānaṃ asaññasattānaṃ tesaṃ … = Ở tất cả chúng sinh, vào khoảnh khắc tan rã của tâm, ở những người nhập thành tựu thiền chấm dứt và chúng sinh Vô Tưởng, thì ở những người ấy …
Pavatte saddhāvippayuttasomanassasampayuttacittassa uppādakkhaṇe tesaṃ … = Trong đời sống, vào khoảnh khắc sinh khởi của tâm không gắn liền với niềm tin và gắn liền với niềm vui, thì ở những người ấy …

## Sample lines

Acakkhukānaṃ sasotakānaṃ upapajjantānaṃ tesaṃ cakkhundriyaṃ na uppajjati, no ca tesaṃ sotindriyaṃ na uppajjati. Sabbesaṃ cavantānaṃ acakkhukānaṃ asotakānaṃ upapajjantānaṃ tesaṃ cakkhundriyañca na uppajjati sotindriyañca na uppajjati. = Ở những người không có mắt, có tai đang tái sinh, thì ở những người ấy năng lực mắt không sinh khởi, nhưng ở những người ấy năng lực tai vẫn sinh khởi. Ở tất cả những người đang chết đi và những người không có mắt, không có tai đang tái sinh, thì ở những người ấy năng lực mắt không sinh khởi, năng lực tai cũng không sinh khởi.
Purisānaṃ upapajjantānaṃ tesaṃ itthindriyaṃ na uppajjati, no ca tesaṃ purisindriyaṃ na uppajjati. Sabbesaṃ cavantānaṃ na itthīnaṃ na purisānaṃ upapajjantānaṃ tesaṃ itthindriyañca na uppajjati purisindriyañca na uppajjati. = Ở những người đang tái sinh làm người nam, thì ở những người ấy năng lực nữ tính không sinh khởi, nhưng ở những người ấy năng lực nam tính vẫn sinh khởi. Ở tất cả những người đang chết đi và những người đang tái sinh không làm người nữ, cũng không làm người nam, thì ở những người ấy năng lực nữ tính không sinh khởi, năng lực nam tính cũng không sinh khởi.
Upekkhāya upapajjantānaṃ pavatte upekkhāsampayuttacittassa uppādakkhaṇe tesaṃ somanassindriyaṃ na uppajjati, no ca tesaṃ upekkhindriyaṃ na uppajjati. Sabbesaṃ cittassa bhaṅgakkhaṇe somanassavippayuttaupekkhāvippayuttacittassa uppādakkhaṇe nirodhasamāpannānaṃ asaññasattānaṃ tesaṃ somanassindriyañca na uppajjati upekkhindriyañca na uppajjati. = Ở những người đang tái sinh có sự bình thản đi kèm, trong đời sống, vào khoảnh khắc sinh khởi của tâm gắn liền với sự bình thản, thì ở những người ấy năng lực niềm vui không sinh khởi, nhưng ở những người ấy năng lực bình thản vẫn sinh khởi. Ở tất cả chúng sinh, vào khoảnh khắc tan rã của tâm, vào khoảnh khắc sinh khởi của tâm không gắn liền với niềm vui và không gắn liền với sự bình thản, ở những người nhập thành tựu thiền chấm dứt và chúng sinh Vô Tưởng, thì ở những người ấy năng lực niềm vui không sinh khởi, năng lực bình thản cũng không sinh khởi.
Sacakkhukānaṃ itthīnaṃ upapajjantīnaṃ tāsaṃ tattha cakkhundriyañca uppajjati itthindriyañca uppajjati. = Ở những người có mắt đang tái sinh làm người nữ, thì ở những người ấy, ở nơi ấy năng lực mắt sinh khởi, năng lực nữ tính cũng sinh khởi.

## Termbase misfits and gaps (for the coordinator)

- Sex / feeling words beside cavantānaṃ: in this chapter they always belong to the following upapajjantānaṃ group («Sabbesaṃ cavantānaṃ na itthīnaṃ acakkhukānaṃ upapajjantānaṃ» beside «… acakkhukānaṃ na itthīnaṃ upapajjantānaṃ»), so 10-02's shape applies unchanged: «tất cả những người đang chết đi và những người không có mắt đang tái sinh không làm người nữ». No sex / feeling word goes with cavantānaṃ itself, and none with a plane (still not set; the builder raises).
- Two sex words in one group (na itthīnaṃ na purisānaṃ upapajjantānaṃ, ^6-10-215 block, both (Ka) and (Kha)): set here as «những người đang tái sinh không làm người nữ, cũng không làm người nam» (7-01 / 7-04 neither shape «không A, cũng không B»). Please confirm.
- na uppajjati (separate na, all of (Gha)): 9-01 verb «không sinh khởi»; after no ca «vẫn sinh khởi» (7-01); both-frame «A không sinh khởi, B cũng không sinh khởi» (2-01 b_both, 7-02).
- Sabbesaṃ before cittassa bhaṅgakkhaṇe: 9-01 «Ở tất cả chúng sinh, vào khoảnh khắc tan rã của tâm, …»; nirodhasamāpannānaṃ asaññasattānaṃ after the moments keep their own «ở» (coordinator).

## Pāli as written (reported)

- ^6-10-206 block (Ka) itthindriyaṃ … paññindriyaṃ: «Itthīnaṃ ñāṇasampayuttānaṃ uppajjantīnaṃ» (for upapajjantīnaṃ): the termbase reading entry uppajjantīnaṃ «đang tái sinh» is used (rendered as meant).
- ^6-10-204 last answer «Sacakkhukānaṃ upapajjantānaṃ …» (no sacittakānaṃ; the ghāna parallel ^6-10-205 has «Saghānakānaṃ upapajjantānaṃ …»): as written.
- ^6-10-213 … ^6-10-216 «Sabbesaṃ cavantānaṃ acittakānaṃ upapajjantānaṃ …» (manindriya): as written.
- ^6-10-218 / ^6-10-219 / ^6-10-220 / ^6-10-221 «Sabbesaṃ cittassa bhaṅgakkhaṇe nirodhasamāpannānaṃ asaññasattānaṃ …» (no mind kind before the second group where manindriya is named): as written.
