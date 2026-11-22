# pi-6 rails 3-02 (Āyatanayamaka 2): future and present-past tenses on the 3-01 Āyatana module

Builder: build_rails_3-02_vi.py (import with importlib). Members, attributes, labels, notes, cuts and all frames are 3-01's (build_rails_3-01_vi, on 2-01 / 7-01); the 'P ye ca …' head is 2-02's. New here, exposed for 3-03 … 3-06: `ay_group`, `ay_person_items`, `ay_persons`, `ye_ca_head`, `answer_head`, `SADISA`, `IME_DVE`, `SADISAYEVA_HONTI`, `SADISA_NOTE`, `sadisa_note`, `SLIPS`, `b_sentence`, `sentence_vi`, `unit_vi`, `line_vi`, `tr_line`, `build`. Where 2-01 / 3-01 can parse a head, the builder asserts the string is theirs byte for byte. Format: Pāli = tiếng Việt.


## Person heads: āyatana attributes with planes (new shape)

Sacakkhukānaṃ kāmāvacaraṃ upapajjantānaṃ = những người có mắt đang tái sinh vào cõi dục lạc
Pañcavokārā cavantānaṃ acakkhukānaṃ kāmāvacaraṃ upapajjantānaṃ = những người đang chết đi khỏi cõi gồm năm khối và những người không có mắt đang tái sinh vào cõi dục lạc
Kāmāvacarā cavantānaṃ aghānakānaṃ kāmāvacaraṃ upapajjantānaṃ rūpāvacarānaṃ = những người đang chết đi khỏi cõi dục lạc, những người không có mũi đang tái sinh vào cõi dục lạc và chúng sinh trong cõi hình sắc
Pañcavokārā cavantānaṃ acakkhukānaṃ kāmāvacaraṃ upapajjantānaṃ asaññasattānaṃ = những người đang chết đi khỏi cõi gồm năm khối, những người không có mắt đang tái sinh vào cõi dục lạc và chúng sinh Vô Tưởng

## Person heads: a nested run of plane-beings is joined flat (new rule; 7-01 «A, B và C»)

Kāmāvacarā cavantānaṃ aghānakānaṃ kāmāvacaraṃ upapajjantānaṃ rūpāvacarānaṃ arūpāvacarānaṃ = những người đang chết đi khỏi cõi dục lạc, những người không có mũi đang tái sinh vào cõi dục lạc, chúng sinh trong cõi hình sắc và chúng sinh trong cõi không hình sắc
Pañcavokāre pacchimabhavikānaṃ asaññasattānaṃ arūpānaṃ = những người thuộc kiếp sống cuối cùng trong cõi gồm năm khối, chúng sinh Vô Tưởng và chúng sinh trong cõi không hình sắc
Suddhāvāse parinibbantānaṃ asaññasattānaṃ arūpānaṃ = những người đang nhập Niết-bàn trọn vẹn trong cõi Tịnh Cư, chúng sinh Vô Tưởng và chúng sinh trong cõi không hình sắc
Rūpāvacarā cavantānaṃ asaññasattānaṃ arūpānaṃ = những người đang chết đi khỏi cõi hình sắc, chúng sinh Vô Tưởng và chúng sinh trong cõi không hình sắc
(2-01's persons() would give «… và chúng sinh Vô Tưởng và chúng sinh trong cõi không hình sắc»; a head that is only a run keeps 2-01's being_run:)
Suddhāvāsānaṃ asaññasattānaṃ = chúng sinh trong cõi Tịnh Cư và cõi Vô Tưởng
Suddhāvāsānaṃ arūpānaṃ = chúng sinh trong cõi Tịnh Cư và cõi không hình sắc
Rūpāvacarānaṃ arūpāvacarānaṃ = chúng sinh trong cõi hình sắc và cõi không hình sắc
Asaññasattānaṃ arūpānaṃ = chúng sinh Vô Tưởng và chúng sinh trong cõi không hình sắc
Catuvokārānaṃ pañcavokārānaṃ = chúng sinh trong cõi gồm bốn khối và cõi gồm năm khối
Pañcavokārānaṃ asaññasattānaṃ = chúng sinh trong cõi gồm năm khối và cõi Vô Tưởng

## Ye-clause heads in the Āyatana chapters (2-01 ye_clause, 2-02 b_head)

Ye rūpāvacaraṃ upapajjitvā parinibbāyissanti tesaṃ … = Những người nào sau khi tái sinh vào cõi hình sắc sẽ nhập Niết-bàn trọn vẹn, thì ở những người ấy …
Ye rūpāvacaraṃ arūpāvacaraṃ upapajjitvā parinibbāyissanti tesaṃ … = Những người nào sau khi tái sinh vào cõi hình sắc và cõi không hình sắc sẽ nhập Niết-bàn trọn vẹn, thì ở những người ấy …
Ye arūpaṃ upapajjitvā parinibbāyissanti tesaṃ … = Những người nào sau khi tái sinh vào cõi không hình sắc sẽ nhập Niết-bàn trọn vẹn, thì ở những người ấy …
Pacchimabhavikānaṃ ye ca arūpaṃ upapajjitvā parinibbāyissanti tesaṃ … = Ở những người thuộc kiếp sống cuối cùng và những người nào sau khi tái sinh vào cõi không hình sắc sẽ nhập Niết-bàn trọn vẹn, thì ở những người ấy …
Itaresaṃ tesaṃ … = Ở những người khác, thì ở những người ấy …

## Sample sentences

Ye rūpāvacaraṃ upapajjitvā parinibbāyissanti tesaṃ cakkhāyatanaṃ uppajjissati, no ca tesaṃ ghānāyatanaṃ uppajjissati. = Những người nào sau khi tái sinh vào cõi hình sắc sẽ nhập Niết-bàn trọn vẹn, thì ở những người ấy lĩnh vực mắt sẽ sinh khởi, nhưng ở những người ấy không có lĩnh vực mũi sẽ sinh khởi.
Pacchimabhavikānaṃ ye ca arūpaṃ upapajjitvā parinibbāyissanti tesaṃ ghānāyatanañca nuppajjissati cakkhāyatanañca nuppajjissati. = Ở những người thuộc kiếp sống cuối cùng và những người nào sau khi tái sinh vào cõi không hình sắc sẽ nhập Niết-bàn trọn vẹn, thì ở những người ấy lĩnh vực mũi sẽ không sinh khởi, lĩnh vực mắt cũng sẽ không sinh khởi.
Pañcavokārā cavantānaṃ acakkhukānaṃ kāmāvacaraṃ upapajjantānaṃ tesaṃ tattha cakkhāyatanaṃ nuppajjati, no ca tesaṃ tattha sotāyatanaṃ nuppajjittha. = Ở những người đang chết đi khỏi cõi gồm năm khối và những người không có mắt đang tái sinh vào cõi dục lạc, thì ở những người ấy, ở nơi ấy lĩnh vực mắt không sinh khởi, nhưng ở những người ấy, ở nơi ấy lĩnh vực tai đã từng sinh khởi.
Suddhāvāse parinibbantānaṃ asaññasattānaṃ arūpānaṃ tesaṃ tattha cakkhāyatanañca nuppajjati sotāyatanañca nuppajjittha. = Ở những người đang nhập Niết-bàn trọn vẹn trong cõi Tịnh Cư, chúng sinh Vô Tưởng và chúng sinh trong cõi không hình sắc, thì ở những người ấy, ở nơi ấy lĩnh vực mắt không sinh khởi, lĩnh vực tai cũng chưa từng sinh khởi.

## Editorial note

Yassa cakkhāyatanaṃ uppajjissati (tassa manāyatanañca dhammāyatanañca sadisaṃ, ime dve sadisāyeva honti). = Ở người nào mà lĩnh vực mắt sẽ sinh khởi (thì ở người ấy lĩnh vực ý và lĩnh vực đối tượng của ý giống nhau, hai điều này đúng là giống nhau).
sadisaṃ / ime dve / sadisāyeva honti = giống nhau / hai điều này / đúng là giống nhau

## Termbase misfits and gaps (for the coordinator)

- sadisaṃ, ime dve, sadisāyeva honti: no entries; sadisaṃ «giống nhau» as 3-01's note («… đều giống nhau»; termbase -sadisaṃ «giống như …»); ime dve «hai điều này» (masculine plural in the Pāli: not narrowed to «hai lĩnh vực này»); eva «đúng là».
- Nested plane-being runs inside a longer head: joined flat («A, B và C»); 2-01 persons() would join the run inside the list («A và B và C»). No finished chapter has such a head. Please align (10-07 has the same Pāli 'Pañcavokāre pacchimabhavikānaṃ asaññasattānaṃ arūpānaṃ').

## Slips (rendered as meant or kept; reported)

- ^6-3-75 «rūpāyatanañca ca uppajjittha»: «ca» written twice; rendered as the both-frame («…, lĩnh vực hình sắc cũng đã sinh khởi»).
- ^6-3-54 «(Rūpāyatanamūlakaṃ).» has a final «.» (the other labels do not): kept «(Phần dựa trên lĩnh vực hình sắc).».
- ^6-3-74 «Āmantā.…Pe….»: the periods on both sides of the cut are absorbed (3-01).
- ^6-3-80 «Yassa ghānāyatanaṃ…pe… rūpāyatanaṃ… manāyatanaṃ nuppajjati tassa dhammāyatanaṃ …»: the cut list stands in the first clause; rendered in place «… lĩnh vực mũi… lĩnh vực hình sắc… lĩnh vực ý không sinh khởi …».
- Questions cut by …pe… and answered «Āmantā.» (^6-3-53, 54, 58, 61 …) keep their «?» (3-01 list question).
