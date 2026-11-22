# pi-6 rails 3-01 (Āyatanayamaka 1): the Āyatana module on top of families A / B (rails 2-01)

Builder: build_rails_3-01_vi.py (import with importlib). Every frame string is produced by build_rails_2-01_vi functions (name_q, name_q_neg, both_is, rest_not_is, special_is / special_not, except_*, b_q, b_noca, b_both, persons, place_head, heading, SHORT, CLOSING); this file only plugs in the members and adds the pieces listed here. Exposed for 3-02 … 3-06: `AYATANA`, `TWELVE`, `AY_NAME`, `AY_SPECIAL`, `AY_ATTRS`, `ATTR_JOIN`, `PLANES_AY`, `ay_persons`, `answer_head`, `mulaka_label`, `NOTES_AY`, `except_frag`, `naca_tail`, `na_tail`, `nq`, `except2_var`, `question_vi`, `sentence_vi`, `unit_vi`, `line_vi`, `var_vi`, `tr_line`, `build`. Format: Pāli = tiếng Việt.


## Members (termbase; pi-1 names)

cakkhu / cakkhuṃ ; cakkhāyatanaṃ = mắt ; lĩnh vực mắt
sotaṃ ; sotāyatanaṃ = tai ; lĩnh vực tai
ghānaṃ ; ghānāyatanaṃ = mũi ; lĩnh vực mũi
jivhā / jivhaṃ ; jivhāyatanaṃ = lưỡi ; lĩnh vực lưỡi
kāyo / kāyaṃ ; kāyāyatanaṃ = thân ; lĩnh vực thân
rūpaṃ ; rūpāyatanaṃ = vật chất ; lĩnh vực hình sắc
saddo / saddaṃ ; saddāyatanaṃ = âm thanh ; lĩnh vực âm thanh
gandho / gandhaṃ ; gandhāyatanaṃ = mùi ; lĩnh vực mùi
raso / rasaṃ ; rasāyatanaṃ = vị ; lĩnh vực vị
phoṭṭhabbo / phoṭṭhabbaṃ ; phoṭṭhabbāyatanaṃ = vật xúc chạm ; lĩnh vực vật xúc chạm
mano / manaṃ ; manāyatanaṃ = ý ; lĩnh vực ý
dhammo / dhammaṃ ; dhammāyatanaṃ = hiện tượng ; lĩnh vực đối tượng của ý
āyatanaṃ / āyatanā = lĩnh vực nhận biết / các lĩnh vực nhận biết (predicate: lĩnh vực nhận biết)
nāyatanaṃ / nāyatanā (fused na) = = na āyatana…: «(a) Những gì không phải là mắt thì không phải là lĩnh vực nhận biết, có phải không?»
Dvādasāyatanāni – … (uddesa, ^6-3-1) = Mười hai lĩnh vực nhận biết – lĩnh vực mắt, lĩnh vực tai, lĩnh vực mũi, lĩnh vực lưỡi, lĩnh vực thân, lĩnh vực hình sắc, lĩnh vực âm thanh, lĩnh vực mùi, lĩnh vực vị, lĩnh vực vật xúc chạm, lĩnh vực ý, lĩnh vực đối tượng của ý.

## Headings

Āyatanayamakaṃ = Các cặp câu hỏi về các lĩnh vực nhận biết
Suddhāyatanavāro = Mục về các lĩnh vực nhận biết thuần túy
Suddhāyatanamūlacakkavāro = Mục về vòng luân chuyển dựa trên các lĩnh vực nhận biết thuần túy

## Family A in this yamaka (2-01 frames)

(Ka) cakkhu cakkhāyatanaṃ? = (a) Mắt có phải là lĩnh vực mắt không?
(Kha) āyatanā sotāyatanaṃ? = (b) Các lĩnh vực nhận biết có phải là lĩnh vực tai không?
(Ka) na cakkhu nāyatanaṃ? = (a) Những gì không phải là mắt thì không phải là lĩnh vực nhận biết, có phải không?
(Kha) nāyatanā na cakkhu? = (b) Những gì không phải là lĩnh vực nhận biết thì không phải là mắt, có phải không?
Cakkhu cakkhāyatananti? = Mắt có phải là lĩnh vực mắt không?
Na sotaṃ na sotāyatananti? = Những gì không phải là tai thì không phải là lĩnh vực tai, có phải không?
Dibbacakkhu paññācakkhu cakkhu, na cakkhāyatanaṃ. = Mắt hiểu theo nghĩa thiên nhãn, mắt trí tuệ thì là mắt, nhưng không phải là lĩnh vực mắt.
Dibbasotaṃ taṇhāsotaṃ sotaṃ, na sotāyatanaṃ. = Tai hiểu theo nghĩa thiên nhĩ, dòng chảy của khao khát thì là tai, nhưng không phải là lĩnh vực tai.
Sīlagandho samādhigandho paññāgandho gandho, na gandhāyatanaṃ. = Mùi hiểu theo nghĩa hương của giới hạnh, hương của định tâm, hương của trí tuệ thì là mùi, nhưng không phải là lĩnh vực mùi.
Attharaso dhammaraso vimuttiraso raso, na rasāyatanaṃ. = Vị hiểu theo nghĩa vị của ý nghĩa, vị của Giáo Pháp, vị của sự giải thoát thì là vị, nhưng không phải là lĩnh vực vị.
Dibbacakkhu paññācakkhu na cakkhāyatanaṃ, cakkhu. = Mắt hiểu theo nghĩa thiên nhãn, mắt trí tuệ thì không phải là lĩnh vực mắt, mà là mắt.
Cakkhāyatanaṃ cakkhu ceva cakkhāyatanañca. = Lĩnh vực mắt vừa là mắt vừa là lĩnh vực mắt.
Sotāyatanaṃ sotañceva sotāyatanañca. = Lĩnh vực tai vừa là tai vừa là lĩnh vực tai.
Sotāyatanaṃ āyatanañceva sotāyatanañca. = Lĩnh vực tai vừa là lĩnh vực nhận biết vừa là lĩnh vực tai.
Avasesā āyatanā na sotāyatanaṃ. = Các lĩnh vực nhận biết còn lại không phải là lĩnh vực tai.
Kāyāyatanaṃ ṭhapetvā avaseso kāyo, na kāyāyatanaṃ. = Ngoại trừ lĩnh vực thân, những gì còn lại là thân, nhưng không phải là lĩnh vực thân.
Rūpāyatanaṃ ṭhapetvā avasesaṃ rūpaṃ, na rūpāyatanaṃ. = Ngoại trừ lĩnh vực hình sắc, những gì còn lại là vật chất, nhưng không phải là lĩnh vực hình sắc.
Kāyāyatanaṃ ṭhapetvā avaseso na kāyāyatanaṃ, kāyo. = Ngoại trừ lĩnh vực thân, những gì còn lại không phải là lĩnh vực thân, mà là thân.
Rūpañca rūpāyatanañca ṭhapetvā avasesaṃ na ceva rūpaṃ na ca rūpāyatanaṃ. = Ngoại trừ vật chất và lĩnh vực hình sắc, những gì còn lại không phải là vật chất, cũng không phải là lĩnh vực hình sắc.
Cakkhuṃ ṭhapetvā avasesā āyatanā na cakkhu, āyatanā. = Ngoại trừ mắt, các lĩnh vực nhận biết còn lại không phải là mắt, mà là lĩnh vực nhận biết.
Cakkhuñca āyatanañca ṭhapetvā avasesā na ceva cakkhu na ca āyatanā. = Ngoại trừ mắt và lĩnh vực nhận biết, những gì còn lại không phải là mắt, cũng không phải là lĩnh vực nhận biết.
avaseso / avasesaṃ (= avasesā) = những gì còn lại
Cakkhuñca cakkhāyatanañca ṭhapetvā avasesaṃ [v] na ceva … = Ngoại trừ mắt và lĩnh vực mắt, những gì còn lại [v] không phải là mắt, cũng không phải là lĩnh vực mắt.

## Cuts (…pe… / …) inside a line

<question>?…pe… / <question>? …pe… = <câu hỏi> không?… / <câu hỏi> không? …
<sentence>…pe…. / Āmantā.…Pe…. / Natthi.…Pe…. = <câu>… / Đúng vậy… / Không có…  (the «.» on both sides of the cut is absorbed: never «.…» / «….»)
<naming question>ti…pe… / <naming question>…pe… (no «?») = «X có phải là Y không…» / «Những gì không phải là X thì không phải là Y, có phải không…» (2-01 frame, end «»)
Āyatanā ghānāyatananti…pe… āyatanā dhammāyatananti? = Các lĩnh vực nhận biết có phải là lĩnh vực mũi không… các lĩnh vực nhận biết có phải là lĩnh vực đối tượng của ý không?
X ṭhapetvā…pe… = Ngoại trừ X…
…pe… na ca Y. = … cũng không phải là Y.
…pe… na Y(.) = … không phải là Y(.)
ghānaṃ… jivhā… (member list) = mũi… lưỡi…  (lower case as the Pāli)
Yassa A V tassa B…pe… C… D Vti? = Ở người nào mà lĩnh vực mắt đã sinh khởi, thì ở người ấy có phải lĩnh vực mũi… lĩnh vực hình sắc… lĩnh vực ý… lĩnh vực đối tượng của ý đã sinh khởi không? Đúng vậy.
(Ka) yattha A V…pe… (pair question cut after its first clause) = (a) Ở nơi nào mà lĩnh vực mắt đã sinh khởi…
Yattha A nuppajjittha…pe…. = Ở nơi nào mà lĩnh vực mắt chưa từng sinh khởi…
a unit after a cut keeps the Pāli case = «… các lĩnh vực nhận biết còn lại không phải là …»

## Labels and editorial notes

(Cakkhāyatanamūlakaṃ) = (Phần dựa trên lĩnh vực mắt)
(Ghānāyatanamūlakaṃ) = (Phần dựa trên lĩnh vực mũi)
(Rūpāyatanamūlakaṃ) = (Phần dựa trên lĩnh vực hình sắc)
(Manāyatanamūlakaṃ) = (Phần dựa trên lĩnh vực ý)
(Cakkaṃ bandhitabbaṃ) = (Vòng luân chuyển nên được nối kết)
(Ekekapadamūlakaṃ cakkaṃ bandhitabbaṃ asammohantena). = (Vòng luân chuyển dựa trên từng thuật ngữ một nên được nối kết mà không mê lầm).
(Cakkaṃ bandhantena sabbattha āmantāti kātabbaṃ). = (Khi nối kết vòng luân chuyển, ở mọi chỗ nên trả lời là “Đúng vậy”).
(Yattha ghānāyatanaṃ uppajjati tattha manāyatanaṃ dhammāyatanañca ekasadisaṃ, nānaṃ natthi, upari pana vārasaṅkhepo [v] tīti jānitabbaṃ.) = (Ở nơi nào mà lĩnh vực mũi sinh khởi, thì ở nơi ấy lĩnh vực ý và lĩnh vực đối tượng của ý giống hệt nhau, không có khác biệt, còn ở phần sau thì có sự tóm lược các mục [v], nên hiểu như vậy.)
(saṃkhittaṃ yassakasadisaṃ [v] ) = (tóm lược, giống như phần về người [v])
(Saṃkhittaṃ). = (Tóm lược).
(yatthakaṃ paccuppannepi atītepi anāgatepi paccuppannātītepi paccuppannānāgatepi atītānāgatepi sabbattha sadisaṃ, uppajjati uppajjitthāti nāmaṃ atirekaṃ kātabbaṃ). = (phần về nơi chốn ở hiện tại, ở quá khứ, ở tương lai, ở hiện tại và quá khứ, ở hiện tại và tương lai, ở quá khứ và tương lai, ở mọi chỗ đều giống nhau, nên thêm vào tên gọi “sinh khởi”, “đã sinh khởi”).
[X (syā.), Y (sī. ka.)] (double variant) = [dị bản (Syā.): X; (Sī., Ka.): Y] (pi-2 format)

## Family B in this yamaka: person attributes and planes

sacakkhukānaṃ = những người có mắt …
acakkhukānaṃ = những người không có mắt …
sasotakānaṃ = những người có tai …
asotakānaṃ = những người không có tai …
saghānakānaṃ = những người có mũi …
aghānakānaṃ = những người không có mũi …
sarūpakānaṃ = những người có vật chất …
arūpakānaṃ = những người không có vật chất …
sacittakānaṃ = những người có tâm …
acittakānaṃ = những người không có tâm …
<attr> <attr> <participle> (one group) = những người <attr>, <attr> <participle>  (ATTR_JOIN «, »)
Sacakkhukānaṃ asotakānaṃ upapajjantānaṃ = những người có mắt, không có tai đang tái sinh
Sacakkhukānaṃ sasotakānaṃ upapajjantānaṃ = những người có mắt, có tai đang tái sinh
Sacakkhukānaṃ upapajjantānaṃ = những người có mắt đang tái sinh
Acittakānaṃ upapajjantānaṃ = những người không có tâm đang tái sinh
Sabbesaṃ cavantānaṃ acakkhukānaṃ asotakānaṃ upapajjantānaṃ = tất cả những người đang chết đi và những người không có mắt, không có tai đang tái sinh
Sabbesaṃ cavantānaṃ arūpakānaṃ upapajjantānaṃ = tất cả những người đang chết đi và những người không có vật chất đang tái sinh
Sabbesaṃ cavantānaṃ = tất cả những người đang chết đi
rūpāvacare / rūpāvacarānaṃ = cõi hình sắc / chúng sinh trong cõi hình sắc
kāmāvacare / kāmāvacarānaṃ = cõi dục lạc / chúng sinh trong cõi dục lạc
arūpāvacare / arūpāvacarānaṃ = cõi không hình sắc / chúng sinh trong cõi không hình sắc
Rūpāvacarānaṃ arūpāvacarānaṃ = chúng sinh trong cõi hình sắc và cõi không hình sắc
Suddhāvāsānaṃ asaññasattānaṃ arūpānaṃ = chúng sinh trong cõi Tịnh Cư, cõi Vô Tưởng và cõi không hình sắc
Asaññasattānaṃ arūpānaṃ = chúng sinh Vô Tưởng và chúng sinh trong cõi không hình sắc
Pañcavokārānaṃ asaññasattānaṃ = chúng sinh trong cõi gồm năm khối và cõi Vô Tưởng
Rūpāvacare arūpāvacare tattha … = Ở cõi hình sắc, ở cõi không hình sắc, thì ở nơi ấy …
Sacakkhukānaṃ asotakānaṃ upapajjantānaṃ tesaṃ cakkhāyatanaṃ uppajjati, no ca tesaṃ sotāyatanaṃ uppajjati. = Ở những người có mắt, không có tai đang tái sinh, thì ở những người ấy lĩnh vực mắt sinh khởi, nhưng ở những người ấy không có lĩnh vực tai sinh khởi.
Acakkhukānaṃ sasotakānaṃ upapajjantānaṃ tesaṃ cakkhāyatanaṃ nuppajjati, no ca tesaṃ sotāyatanaṃ nuppajjati. = Ở những người không có mắt, có tai đang tái sinh, thì ở những người ấy lĩnh vực mắt không sinh khởi, nhưng ở những người ấy lĩnh vực tai vẫn sinh khởi.
Sabbesaṃ cavantānaṃ tesaṃ cakkhāyatanañca nuppajjati dhammāyatanañca nuppajjati. = Ở tất cả những người đang chết đi, thì ở những người ấy lĩnh vực mắt không sinh khởi, lĩnh vực đối tượng của ý cũng không sinh khởi.
Rūpāvacare tattha ghānāyatanaṃ nuppajjati, no ca tattha cakkhāyatanaṃ nuppajjati. = Ở cõi hình sắc, thì ở nơi ấy lĩnh vực mũi không sinh khởi, nhưng ở nơi ấy lĩnh vực mắt vẫn sinh khởi.
Rūpāvacarānaṃ tesaṃ tattha cakkhāyatanaṃ uppajjittha, no ca tesaṃ tattha ghānāyatanaṃ uppajjittha. = Ở chúng sinh trong cõi hình sắc, thì ở những người ấy, ở nơi ấy lĩnh vực mắt đã sinh khởi, nhưng ở những người ấy, ở nơi ấy không có lĩnh vực mũi đã sinh khởi.

## Termbase misfits and gaps (for the coordinator)

- dhammo / dhammaṃ (member word): no pi-6 entry; pi-1 core term dhamma «hiện tượng».
- sarūpakānaṃ, saghānakānaṃ, aghānakānaṃ: no entry; built as their termbase siblings (arūpakānaṃ «không có vật chất», Sacakkhukānaṃ «có mắt», acakkhukānaṃ «không có mắt»): «có vật chất», «có mũi», «không có mũi».
- Attribute runs (Sacakkhukānaṃ asotakānaṃ upapajjantānaṃ): one person group (as the coordinator's Pacchimabhavikānaṃ <A> <B> rule), attributes joined by «, »: «những người có mắt, không có tai đang tái sinh». New shape: please align.
- saṃkhittaṃ / Saṃkhittaṃ (abridged): the termbase sense «co rút» is the mind's (8); closest sibling vārasaṅkhepo «sự tóm lược các mục»: «tóm lược».
- Cakkaṃ bandhitabbaṃ / bandhantena, Ekekapadamūlakaṃ, ekasadisaṃ, nānaṃ natthi, jānitabbaṃ, atirekaṃ kātabbaṃ: no entries; wording above (Cakkaṃ «vòng luân chuyển», pada «thuật ngữ», mūlaka «dựa trên», Natthi «không có», yatthakaṃ «phần về nơi chốn», yassakasadisaṃ «giống như phần về người»).
- arūpāvacarānaṃ: termbase «cõi không hình sắc»; as the second plane of a beings run (Rūpāvacarānaṃ arūpāvacarānaṃ) 2-01's run gives «chúng sinh trong cõi hình sắc và cõi không hình sắc», which matches.

## Slips (rendered as meant or kept; reported)

- ^6-3-1 no comma after «sotāyatanaṃ»: comma supplied.
- ^6-3-13 «sotāyananti» for sotāyatananti (termbase lists it as a misspelling): «lĩnh vực tai».
- ^6-3-23 note «… vārasaṅkhepo [..] tīti jānitabbaṃ»: «tīti» read as «(hotī)ti»: «… thì có sự tóm lược các mục …, nên hiểu như vậy».
- The gerundive -tabbaṃ (bandhitabbaṃ, kātabbaṃ, jānitabbaṃ) = «nên …», as 2-02 (paripuṇṇaṃ kātabbaṃ «nên được trình bày đầy đủ») and pi-2 (vibhajitabbaṃ «nên phân tích»).
- ^6-3-26 «[…] )»: the stray space before «)» is dropped.
- ^6-3-43 «uppajjittharūpāyatanañca» (two words run together): «đã sinh khởi, lĩnh vực hình sắc …».
- ^6-3-50 the second question is labelled «(Ka)» (for «(Kha)»): label kept «(a)» (as 2-01 ^6-2-61).
- «Āmantā.…Pe….», «Natthi.…Pe….», «…pe….»: the periods on both sides of the cut are absorbed.
