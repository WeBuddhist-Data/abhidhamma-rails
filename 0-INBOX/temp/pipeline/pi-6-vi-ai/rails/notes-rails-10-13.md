# pi-6 rails 10-13 (Indriyayamaka, last part): pariññāvāra with four verbs; end of the book

Builder: build_rails_10-13_vi.py. Imports READ-ONLY: build_rails_2-02_vi (family E setter: e_line / e_sentence / yo_q / make_verbs / rows_na / Persons), build_rails_10-01_vi (INDRIYA members, ind_mulaka, heading), build_rails_5-03_vi (PAJ_VERBS, AGGAPHALA), build_rails_7-06_vi / 7-03 / 7-01 (persons), build_rails_7-07_vi (Verb agreement check), build_rails_2-01_vi (parse_variant, join_and) and the sample builder (yamaka_end, BOOK_END). Exposed: BHAVETI, SACCHIKAROTI, BHAV_VERBS, SACC_VERBS, VERBS_10, NUM_VI, num_persons, maggasamangi, yo_head, ye_puthu_head, PERSONS_10, e_line10. Format: Pāli = tiếng Việt.


## Verbs new in the Yamaka (termbase; family-E tense rule; after no ca E.denied)

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
sacchikaroti = tự mình chứng nghiệm
sacchikaronti = tự mình chứng nghiệm
sacchikarittha = đã tự mình chứng nghiệm
sacchikarissati = sẽ tự mình chứng nghiệm
sacchikarissanti = sẽ tự mình chứng nghiệm
na sacchikaroti = không tự mình chứng nghiệm
na sacchikaronti = không tự mình chứng nghiệm
na sacchikarittha = chưa từng tự mình chứng nghiệm
na sacchikarissati = sẽ không tự mình chứng nghiệm
na sacchikarissanti = sẽ không tự mình chứng nghiệm
sacchākāsi (aorist, in the head «Yo aggaphalaṃ sacchākāsi so») = đã tự mình chứng nghiệm
no ca … na bhāveti / na bhāvittha / na bhāvessati (denied) = vẫn tu tập / đã từng tu tập / vẫn sẽ tu tập
no ca … na sacchikaroti / na sacchikarittha / na sacchikarissati (denied) = vẫn tự mình chứng nghiệm / đã từng tự mình chứng nghiệm / vẫn sẽ tự mình chứng nghiệm
no ca … bhāveti / bhāvittha / bhāvessati (positive: its negative) = không tu tập / chưa từng tu tập / sẽ không tu tập

## Answer heads (nominative persons; registered in PERSONS_10)

Dve puggalā … = Hai hạng người …
Tayo puggalā … = Ba hạng người …
Cattāro puggalā … = Bốn hạng người …
Pañca puggalā … = Năm hạng người …
Cha puggalā … = Sáu hạng người …
Satta puggalā … = Bảy hạng người …
Aṭṭha puggalā … = Tám hạng người …
Tayo maggasamaṅgino … (nominative) = Ba người có được con đường …
Anāgāmimaggasamaṅgī … = Người có được con đường không trở lại …
Aṭṭhamako … = Người thứ tám …
Anāgāmī … = Bậc không trở lại …
Aggamaggasamaṅgī … = Người có được con đường tối thượng …
Arahā … = Bậc A-la-hán …
Yo aggaphalaṃ sacchikaroti so … = Người nào tự mình chứng nghiệm thành quả tối thượng, thì người ấy …
Yo aggaphalaṃ sacchākāsi so … = Người nào đã tự mình chứng nghiệm thành quả tối thượng, thì người ấy …
Ye puthujjanā maggaṃ paṭilabhissanti te … = Những người phàm phu nào sẽ đạt được con đường, thì những người ấy …
Ye puthujjanā maggaṃ na paṭilabhissanti te … = Những người phàm phu nào sẽ không đạt được con đường, thì những người ấy …
Dve maggasamaṅgino ṭhapetvā avasesā puggalā … = Ngoại trừ hai người có được con đường, những hạng người còn lại …
Tayo maggasamaṅgino ṭhapetvā avasesā puggalā … = Ngoại trừ ba người có được con đường, những hạng người còn lại …
Cattāro maggasamaṅgino ṭhapetvā avasesā puggalā … = Ngoại trừ bốn người có được con đường, những hạng người còn lại …
Tayo maggasamaṅgino ca arahantañca ṭhapetvā avasesā puggalā … = Ngoại trừ ba người có được con đường và bậc A-la-hán, những hạng người còn lại …
Aggamaggasamaṅgiñca arahantañca ṭhapetvā avasesā puggalā … = Ngoại trừ người có được con đường tối thượng và bậc A-la-hán, những hạng người còn lại …
Anāgāmimaggasamaṅgiñca arahantañca ṭhapetvā avasesā puggalā … = Ngoại trừ người có được con đường không trở lại và bậc A-la-hán, những hạng người còn lại …
Aṭṭhamakañca arahantañca ṭhapetvā avasesā puggalā … = Ngoại trừ người thứ tám và bậc A-la-hán, những hạng người còn lại …

## Examples (built by the module)

(Ka) yo cakkhundriyaṃ parijānāti so domanassindriyaṃ pajahatīti? No. = (a) Người nào mà hiểu biết trọn vẹn năng lực mắt, thì người ấy có phải dứt bỏ năng lực nỗi buồn không? Không.
(Kha) yo vā pana aññātāvindriyaṃ na sacchikarittha so cakkhundriyaṃ na parijānitthāti? = (b) Còn người nào mà chưa từng tự mình chứng nghiệm năng lực của người đã hiểu biết trọn vẹn, thì người ấy có phải chưa từng hiểu biết trọn vẹn năng lực mắt không?
Dve puggalā aññindriyaṃ bhāventi, no ca cakkhundriyaṃ parijānanti. Aggamaggasamaṅgī aññindriyañca bhāveti cakkhundriyañca parijānāti. = Hai hạng người tu tập năng lực hiểu biết trọn vẹn, nhưng không hiểu biết trọn vẹn năng lực mắt. Người có được con đường tối thượng tu tập năng lực hiểu biết trọn vẹn, cũng hiểu biết trọn vẹn năng lực mắt.
Aṭṭhamako cakkhundriyaṃ na parijānāti, no ca anaññātaññassāmītindriyaṃ na bhāveti. Dve maggasamaṅgino ṭhapetvā avasesā puggalā cakkhundriyañca na parijānanti anaññātaññassāmītindriyañca na bhāventi. = Người thứ tám không hiểu biết trọn vẹn năng lực mắt, nhưng vẫn tu tập năng lực biết được điều chưa từng biết. Ngoại trừ hai người có được con đường, những hạng người còn lại không hiểu biết trọn vẹn năng lực mắt, cũng không tu tập năng lực biết được điều chưa từng biết.
Yo aggaphalaṃ sacchikaroti so cakkhundriyaṃ parijānittha, no ca aññātāvindriyaṃ sacchikarittha. Yo aggaphalaṃ sacchākāsi so cakkhundriyañca parijānittha aññātāvindriyañca sacchikarittha. = Người nào tự mình chứng nghiệm thành quả tối thượng, thì người ấy đã hiểu biết trọn vẹn năng lực mắt, nhưng chưa từng tự mình chứng nghiệm năng lực của người đã hiểu biết trọn vẹn. Người nào đã tự mình chứng nghiệm thành quả tối thượng, thì người ấy đã hiểu biết trọn vẹn năng lực mắt, cũng đã tự mình chứng nghiệm năng lực của người đã hiểu biết trọn vẹn.
Ye puthujjanā maggaṃ paṭilabhissanti te cakkhundriyaṃ na parijānanti, no ca anaññātaññassāmītindriyaṃ na bhāvessanti. = Những người phàm phu nào sẽ đạt được con đường, thì những người ấy không hiểu biết trọn vẹn năng lực mắt, nhưng vẫn sẽ tu tập năng lực biết được điều chưa từng biết.
Arahā aññātāvindriyaṃ na sacchikarissati, no ca cakkhundriyaṃ na parijānittha. Ye puthujjanā maggaṃ na paṭilabhissanti te aññātāvindriyañca na sacchikarissanti cakkhundriyañca na parijānittha. = Bậc A-la-hán sẽ không tự mình chứng nghiệm năng lực của người đã hiểu biết trọn vẹn, nhưng đã từng hiểu biết trọn vẹn năng lực mắt. Những người phàm phu nào sẽ không đạt được con đường, thì những người ấy sẽ không tự mình chứng nghiệm năng lực của người đã hiểu biết trọn vẹn, cũng chưa từng hiểu biết trọn vẹn năng lực mắt.

## Variants, labels, closers

[tayo puggalā (pī.)] = Ba người có được con đường [dị bản (Pī.): tayo puggalā]   (placed after the word it follows)
[aṭṭhamakañca tayo maggasamaṅgino ca (pī.)] = bốn người có được con đường [dị bản (Pī.): aṭṭhamakañca tayo maggasamaṅgino ca],  (placed after the word it follows)
[satta (sī. syā. ka.)] = Tám [dị bản (Sī., Syā., Ka.): satta] hạng người  (placed after the word it follows)
[pañca (sī. syā. ka.)] = Sáu [dị bản (Sī., Syā., Ka.): pañca] hạng người  (placed after the word it follows)
(Cakkhundriyamūlakaṃ) … (Aññindriyamūlakaṃ). = (Phần dựa trên năng lực mắt) … (Phần dựa trên năng lực hiểu biết trọn vẹn).
Pariññāvāro. = Mục về sự hiểu biết trọn vẹn.
Indriyayamakaṃ niṭṭhitaṃ. = Phần các cặp câu hỏi về các năng lực đã hoàn tất.
Yamakapakaraṇaṃ niṭṭhitaṃ. = Bộ “Các cặp câu hỏi” đã hoàn tất.

## Termbase misfits and gaps (for the coordinator)

- Numerals with puggalā (Pañca / Cha / Satta / Aṭṭha puggalā): no pi-6 headword; pi-4 «Năm / Sáu / Bảy / Tám hạng người» (asserted); Dve / Tayo / Cattāro = 7-01 / 7-03 «hai / ba / bốn hạng người».
- Dve / Tayo / Cattāro maggasamaṅgino (accusative after ṭhapetvā; Tayo also nominative): «hai / ba / bốn người có được con đường» (termbase maggasamaṅgino; = 7-06 «hai người có được con đường» for Dvinnaṃ maggasamaṅgīnaṃ). pi-4 «Bốn hạng người có được con đường» renders «cattāro maggasamaṅgino puggalā» (with puggalā), so «hạng» is not added here.
- Yo aggaphalaṃ sacchikaroti so / sacchākāsi so: no setter shape; the singular of 2-02's ye_head: «Người nào (đã) tự mình chứng nghiệm thành quả tối thượng, thì người ấy …».
- Ye puthujjanā maggaṃ (na) paṭilabhissanti te: «Những người phàm phu nào sẽ (không) đạt được con đường, thì những người ấy …» (= 2-02's «… và những người phàm phu nào …» without the first person).
- aññindriyaṃ «năng lực hiểu biết trọn vẹn» (termbase) sits next to parijānāti «hiểu biết trọn vẹn» in the same sentences («tu tập năng lực hiểu biết trọn vẹn, nhưng không hiểu biết trọn vẹn năng lực mắt»): both locked, kept; the reader may find the echo heavy.

## Slips and punctuation (rendered as meant or as written; reported)

- ^6-10-452 «bhavissanti» (will be) for «bhāvessanti» (will cultivate): spelling slip, rendered as meant
- ^6-10-452 comma before «no ca» missing: added (coordinator rule)
- ^6-10-452 «…pajahissanti, pañca puggalā …»: comma (not «.») before the second answer sentence; kept as written («…, năm hạng người …»)
- ^6-10-454 «Aggamaggasamaṅgī … sacchikarissanti, … bhāvessanti» (singular subject, plural verbs): the Vietnamese verb has no number; same wording
- ^6-10-455 «(Ka) yo cakkhundriyaṃ na parijānissati so anaññātaññassāmītindriyaṃ na bhāvessatīti. Āmantā.»: the question ends with «.» in the Pāli; plainly a question (label, yo … so …ti): «… không?»
- ^6-10-455 «(Kha) yo vā pana anaññātaññassāmītindriyaṃ na bhāvessati so cakkhundriyaṃ na parijānissatīti.»: the question ends with «.» in the Pāli; plainly a question: «… không?»
- ^6-10-459 «Aggamaggasamaṅgī … parijānanti» (singular subject, plural verb): same wording
- ^6-10-468 «… pajahanti anāgāmimaggasamaṅgi aññindriyañca bhāvessanti, domanassindriyañca pajahanti.»: the full stop before the second sentence is missing (added, capital as meant); «anāgāmimaggasamaṅgi» short -i (termbase form) and plural verbs with a singular subject (same wording); the comma inside the both-frame is the frame's own «, cũng» (as 2-02)
- ^6-10-477 «(Kha) yo vā pana aññindriyaṃ bhāvessati. So …bhāvitthāti?»: stray full stop and capital inside the question; one question as meant
- ^6-10-477 comma before «no ca» missing: added (coordinator rule)
- ^6-10-480 «nappajjahittha» (double j) for «nappajahittha»: spelling slip, rendered as meant
- ^6-10-442 (twice) «Tayo maggasamaṅgino ca arahantañca ṭhapetvā»: the first item has «ca» without «-ñca» on the noun; one list «Ngoại trừ ba người có được con đường và bậc A-la-hán, …».
- ^6-10-482 «(Aññindriyamūlakaṃ).» with the Pāli's final «.» (kept).
