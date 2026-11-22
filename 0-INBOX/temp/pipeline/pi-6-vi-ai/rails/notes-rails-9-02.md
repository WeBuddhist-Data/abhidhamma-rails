# pi-6 rails 9-02 (Dhammayamaka 2): nirodhavāra and the start of the uppādanirodhavāra

Builder: build_rails_9-02_vi.py. Imports build_rails_9-01_vi READ-ONLY (and through it 2-01, 7-01, 8): members, verbs, questions, answer frames, headings and short answers are 9-01's strings byte for byte. New here: `NEW_GEN`, `gen_vi` (adds Pacchima…cittassa and kusalākusalānaṃ before a moment), `head_parts` / `answer_head` (9-01's parser with those parts cut in), `FIXED` (headings run into a segment as a line), `b_sentence`, `sentence`, `tr_line`, `build`. The builder asserts that its translator reproduces the 9-01 chapter byte for byte. Format: Pāli = tiếng Việt.


## New strings set here

Pacchimacittassa bhaṅgakkhaṇe = vào khoảnh khắc tan rã của tâm cuối cùng
kusalākusalānaṃ bhaṅgakkhaṇe = vào khoảnh khắc tan rã của các hiện tượng thiện và bất thiện
(Ca) paccanīkapuggalokāsā (line) = (e) Chiều nghịch theo người và nơi chốn
(Ga) anulomapuggalokāsā (line) = (c) Chiều thuận theo người và nơi chốn

## Headings, closings, short answers met here (9-01 / 2-01 strings)

(1) Paccuppannavāro = (1) Mục về hiện tại
(5) Paccuppannānāgatavāro = (5) Mục về hiện tại và tương lai
(6) Atītānāgatavāro = (6) Mục về quá khứ và tương lai
Uppādanirodhavāro = Mục về sự sinh khởi và sự chấm dứt
(Ca) paccanīkapuggalokāsā = (e) Chiều nghịch theo người và nơi chốn
Nirodhavāro. = Mục về sự chấm dứt.
Nirujjhanti. = Có chấm dứt.
Nirujjhittha. = Đã chấm dứt.
Nirujjhissanti. = Sẽ chấm dứt.
Āmantā. = Đúng vậy.
No. = Không.
Natthi. = Không có.
nirujjhanti / na nirujjhanti = chấm dứt / không chấm dứt
nirujjhittha / na nirujjhittha = đã chấm dứt / chưa từng chấm dứt
nirujjhissanti / na nirujjhissanti = sẽ chấm dứt / sẽ không chấm dứt

## Answer heads with the new parts

Pacchimacittassa bhaṅgakkhaṇe tesaṃ … = Vào khoảnh khắc tan rã của tâm cuối cùng, thì ở những người ấy …
Sabbesaṃ upapajjantānaṃ pavatte kusalavippayuttacittassa uppādakkhaṇe arūpe kusalākusalānaṃ bhaṅgakkhaṇe tesaṃ … = Ở tất cả những người đang tái sinh, trong đời sống, vào khoảnh khắc sinh khởi của tâm không gắn liền với các hiện tượng thiện, ở cõi không hình sắc, vào khoảnh khắc tan rã của các hiện tượng thiện và bất thiện, thì ở những người ấy …
Kusalavippayuttacittassa uppādakkhaṇe akusalavippayuttacittassa bhaṅgakkhaṇe nirodhasamāpannānaṃ asaññasattānaṃ tesaṃ … = Vào khoảnh khắc sinh khởi của tâm không gắn liền với các hiện tượng thiện, vào khoảnh khắc tan rã của tâm không gắn liền với các hiện tượng bất thiện, ở những người nhập thành tựu thiền chấm dứt và chúng sinh Vô Tưởng, thì ở những người ấy …
Itaresaṃ tesaṃ … = Ở những người khác, thì ở những người ấy …

## Sample lines as built

(Ka) yassa kusalā dhammā nirujjhanti tassa akusalā dhammā nirujjhantīti? No. = (a) Ở người nào mà các hiện tượng thiện chấm dứt, thì ở người ấy có phải các hiện tượng bất thiện chấm dứt không? Không.
(Ka) yattha kusalā dhammā na nirujjhanti tattha abyākatā dhammā na nirujjhantīti? Nirujjhanti. = (a) Ở nơi nào mà các hiện tượng thiện không chấm dứt, thì ở nơi ấy có phải các hiện tượng không xác định về mặt đạo đức không chấm dứt không? Có chấm dứt.
Pacchimacittassa bhaṅgakkhaṇe tesaṃ kusalā ca dhammā na nirujjhissanti abyākatā ca dhammā na nirujjhissanti. = Vào khoảnh khắc tan rã của tâm cuối cùng, thì ở những người ấy các hiện tượng thiện sẽ không chấm dứt, các hiện tượng không xác định về mặt đạo đức cũng sẽ không chấm dứt.
Akusalānaṃ bhaṅgakkhaṇe tesaṃ kusalā dhammā na uppajjanti, no ca tesaṃ akusalā dhammā na nirujjhanti. = Vào khoảnh khắc tan rã của các hiện tượng bất thiện, thì ở những người ấy các hiện tượng thiện không sinh khởi, nhưng ở những người ấy các hiện tượng bất thiện vẫn chấm dứt.
Asaññasatte tattha abyākatā dhammā nirujjhittha, no ca tattha kusalā dhammā uppajjittha. = Ở cõi Vô Tưởng, thì ở nơi ấy các hiện tượng không xác định về mặt đạo đức đã chấm dứt, nhưng ở nơi ấy không có các hiện tượng thiện đã sinh khởi.
Yattha kusalā dhammā nirujjhanti tattha akusalā dhammā nirujjhitthāti?…Pe…. = Ở nơi nào mà các hiện tượng thiện chấm dứt, thì ở nơi ấy có phải các hiện tượng bất thiện đã chấm dứt không?…

## Termbase misfits and gaps (for the coordinator)

- kusalākusalānaṃ (before bhaṅgakkhaṇe): termbase «hiện tượng thiện và bất thiện»; with 9-01's «các» (DHAMMA_GEN) and pi-1 ^1-994 «của các hiện tượng thiện và bất thiện».
- Pacchimacittassa: 8's mind_gen_vi «tâm cuối cùng» (termbase).

## Pāli as written (reported)

- ^6-9-120: the heading «(Ca) paccanīkapuggalokāsā» stands as the last line of the segment (after the paccanīkaokāso answers of the Atītavāra): kept as a line «(e) Chiều nghịch theo người và nơi chốn».
- ^6-9-135: «Yattha …ti?…Pe….» followed by the heading «(Ga) anulomapuggalokāsā» as a second line: kept as two lines, «… không?…» and «(c) Chiều thuận theo người và nơi chốn».
- ^6-9-125, ^6-9-130, ^6-9-135, ^6-9-140, ^6-9-145, ^6-9-150, ^6-9-155, ^6-9-160: unlabelled «Yattha …ti?…Pe….» = «… không?…» (9-01).
- ^6-9-162: «Nirodhavāro.» (no niṭṭhito) = «Mục về sự chấm dứt.» (9-01 SECTION_END).
- Termbase adherence: 16 misses, all «Itaresaṃ catuvokārānaṃ pañcavokārānaṃ» = 2-01's one group «chúng sinh khác trong cõi gồm bốn khối và cõi gồm năm khối» (as 9-01): not genuine.
