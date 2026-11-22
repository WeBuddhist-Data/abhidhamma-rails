# pi-6 rails 9-03 (Dhammayamaka 3): end of the uppādanirodhavāra, the bhāvanāvāra, the closing lines

Builder: build_rails_9-03_vi.py. Imports build_rails_9-02_vi READ-ONLY (its translator, unchanged, for the whole pavattivāra; through it 9-01, 2-01, 7-01, 8) and build_rails_2-02_vi (family E: `yo_q`, `make_verbs`, `rows_na`, `rows_fused`, `e_verb`, `YO_RE`, `pe_tail`). New named constants: `BHAVETI`, `PAJAHATI`, `BHAVANA_VERBS`, `PAJAHANA_VERBS`, `BV_VERBS`, `BV_OBJECTS`, `bv_slot`, `bv_question`, `bv_answers`, `BHAVANAVARO`, `ABHI_LINE`, `HEADINGS`, `FIXED`, `LINE_SLIPS`, `tr_line`, `build`. The builder asserts that its translator reproduces the 9-01 and 9-02 chapters byte for byte. Format: Pāli = tiếng Việt.


## Bhāvanāvāra: verbs (family E tense rule, 2-02; bhāveti and pajahati distinct)

bhāveti = tu tập
bhāventi = tu tập
bhāvittha = đã tu tập
bhāvessati = sẽ tu tập
bhāvessanti = sẽ tu tập
na bhāveti = không tu tập
na bhāventi = không tu tập
na bhāvittha = chưa từng tu tập
na bhāvessati = sẽ không tu tập
na bhāvessanti = sẽ không tu tập
pajahati = dứt bỏ
pajahanti = dứt bỏ
pajahittha = đã dứt bỏ
pajahissati = sẽ dứt bỏ
pajahissanti = sẽ dứt bỏ
nappajahati = không dứt bỏ
nappajahanti = không dứt bỏ
nappajahittha = chưa từng dứt bỏ
nappajahissati = sẽ không dứt bỏ
nappajahissanti = sẽ không dứt bỏ
after no ca (not met here) = negative denied «vẫn V / đã từng V / vẫn sẽ V», positive «không V …» (2-02)

## Bhāvanāvāra: objects and questions (family E shell, 2-02 yo_q)

kusalaṃ dhammaṃ = hiện tượng thiện
akusalaṃ dhammaṃ = hiện tượng bất thiện
(Ka) yo kusalaṃ dhammaṃ bhāveti so akusalaṃ dhammaṃ pajahatīti? Āmantā. = (a) Người nào mà tu tập hiện tượng thiện, thì người ấy có phải dứt bỏ hiện tượng bất thiện không? Đúng vậy.
(Kha) yo vā pana akusalaṃ dhammaṃ pajahati so kusalaṃ dhammaṃ bhāvetīti? Āmantā. = (b) Còn người nào mà dứt bỏ hiện tượng bất thiện, thì người ấy có phải tu tập hiện tượng thiện không? Đúng vậy.
(Ka) yo kusalaṃ dhammaṃ na bhāveti so akusalaṃ dhammaṃ nappajahatīti? Āmantā. = (a) Người nào mà không tu tập hiện tượng thiện, thì người ấy có phải không dứt bỏ hiện tượng bất thiện không? Đúng vậy.
(Kha) yo vā pana akusalaṃ dhammaṃ nappajahati so kusalaṃ dhammaṃ na bhāvetīti? Āmantā…pe…. = (b) Còn người nào mà không dứt bỏ hiện tượng bất thiện, thì người ấy có phải không tu tập hiện tượng thiện không? Đúng vậy…

## Headings and closing lines

Bhāvanāvāro (heading) = Mục về sự tu tập
Bhāvanāvāro. = Mục về sự tu tập.
Dhammayamakaṃ niṭṭhitaṃ. = Phần các cặp câu hỏi về các hiện tượng đã hoàn tất.
Namo tassa bhagavato arahato sammāsambuddhassa = Kính lễ Đức Thế Tôn, bậc A-la-hán, bậc Tự Giác Ngộ Hoàn Toàn
Abhidhammapiṭake = Tạng Vi Diệu Pháp
(3) Anāgatavāro = (3) Mục về tương lai
(4) Paccuppannātītavāro = (4) Mục về hiện tại và quá khứ
(5) Paccuppannānāgatavāro = (5) Mục về hiện tại và tương lai
(6) Atītānāgatavāro = (6) Mục về quá khứ và tương lai
Uppādanirodhavāro. = Mục về sự sinh khởi và sự chấm dứt.
Pavattivāro niṭṭhito. = Mục về sự diễn tiến đã hoàn tất.

## Sample pavattivāra lines as built (9-02 / 9-01 strings)

Aggamaggasamaṅgīnaṃ arahantānaṃ tesaṃ abyākatā dhammā nirujjhissanti, no ca tesaṃ kusalā dhammā uppajjissanti. = Ở những người có được con đường tối thượng và các bậc A-la-hán, thì ở những người ấy các hiện tượng không xác định về mặt đạo đức sẽ chấm dứt, nhưng ở những người ấy không có các hiện tượng thiện sẽ sinh khởi.
Yassa cittassa anantarā aggamaggaṃ paṭilabhissanti tesaṃ akusalā dhammā na nirujjhissanti, no ca tesaṃ kusalā dhammā na uppajjissanti. = Ở những người sẽ đạt được con đường tối thượng ngay sau tâm này, thì ở những người ấy các hiện tượng bất thiện sẽ không chấm dứt, nhưng ở những người ấy các hiện tượng thiện vẫn sẽ sinh khởi.
Aggamaggassa bhaṅgakkhaṇe arahantānaṃ yassa cittassa anantarā aggamaggaṃ paṭilabhissanti tassa cittassa bhaṅgakkhaṇe tesaṃ akusalā ca dhammā na nirujjhissanti kusalā ca dhammā na uppajjanti. = Vào khoảnh khắc tan rã của con đường tối thượng, ở các bậc A-la-hán, vào khoảnh khắc tan rã của tâm mà ngay sau đó sẽ đạt được con đường tối thượng, thì ở những người ấy các hiện tượng bất thiện sẽ không chấm dứt, các hiện tượng thiện cũng không sinh khởi.
(Kha) yassa vā pana yattha abyākatā dhammā na nirujjhissanti tassa tattha kusalā dhammā na uppajjitthāti? Uppajjittha. = (b) Còn ở người nào, ở nơi nào mà các hiện tượng không xác định về mặt đạo đức sẽ không chấm dứt, thì ở người ấy, ở nơi ấy có phải các hiện tượng thiện chưa từng sinh khởi không? Đã sinh khởi.
Yattha kusalā dhammā na uppajjittha tattha akusalā dhammā na nirujjhissantīti?…Pe…. = Ở nơi nào mà các hiện tượng thiện chưa từng sinh khởi, thì ở nơi ấy có phải các hiện tượng bất thiện sẽ không chấm dứt không?…

## Termbase misfits and gaps (for the coordinator)

- bhāveti «tu tập», pajahati «dứt bỏ», kusalaṃ / akusalaṃ dhammaṃ «hiện tượng thiện / bất thiện», Bhāvanāvāro «mục về sự tu tập»: termbase, no misfit. The negative forms (na bhāveti «không tu tập», nappajahati «không dứt bỏ») follow the family E / B rule; the other tenses (bhāvittha, bhāvessati …, pajahittha …) are in the tables for later chapters, not met here.
- Abhidhammapiṭake as a plain last line (no #): «Tạng Vi Diệu Pháp» (termbase; pi-1 heading wording without the #).

## Pāli as written (reported)

- ^6-9-192: «… aggamaggaṃ paṭilabhissanti, asaññasattānaṃ tesaṃ tattha …»: a comma inside the person run (the parallel ^6-9-198 has none); absorbed, the head is the comma-less one: «Ở những người có được con đường tối thượng, các bậc A-la-hán, những người sẽ đạt được con đường tối thượng ngay sau tâm này và chúng sinh Vô Tưởng, …».
- ^6-9-192 (suspected slip): the question asks about akusalā, the 'no ca' part reads «no ca tesaṃ tattha kusalā dhammā uppajjissanti» (the parallel ^6-9-188 and the Itaresaṃ sentence have akusalā): translated as written, «… không có các hiện tượng thiện sẽ sinh khởi», for review.
- ^6-9-229: «Āmantā…pe….» = «Đúng vậy…»; the segment also holds «Bhāvanāvāro.», «Dhammayamakaṃ niṭṭhitaṃ.», the homage and «Abhidhammapiṭake» as lines (8 lines kept).
- ^6-9-228: «Uppādanirodhavāro.» (no niṭṭhito) then «Pavattivāro niṭṭhito.» (9-01 / 2-01 closings).
- ^6-9-201, ^6-9-206, ^6-9-211, ^6-9-216, ^6-9-221, ^6-9-226: unlabelled «Yattha …ti?…Pe….» = «… không?…» (9-01).
