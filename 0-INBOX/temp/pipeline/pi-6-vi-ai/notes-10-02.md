# notes-10-02: Indriyayamaka, suddhindriyamūlacakka (end of paṇṇatti) and pavattivāra (1) paccuppannavāra

Builder: build_10-02_vi.py (`P = importlib.import_module("build_10-02_vi")`; importing writes nothing).
Imports and uses verbatim: build_10-01_vi (faculty table, translate_line() for every paṇṇatti line), build_2-01_vi (families A / B: b_q, b_not, b_both, vparse, WHO_HEAD, LIST_SEP, NO, PANNATTI_NIDDESAVARO), build_3-01_vi (ATTR, ATTR_JOIN, ATTR_GROUP, where3, MULAKA, the «…pe…» run inside one question), build_8_vi (AT / OF / MOMENT), build_5-01_vi (PAVATTE, PAVATTE_JOIN). Labels: build_sample_vi.LABEL.
Format: Pāli = tiếng Việt. [pi-N] = from the approved pi-N rails (asserted); [10-01] / [2-01] / [3-01] / [8] / [5-01] = imported; [new] = set here.

## Reused unchanged
Paṇṇatti lines ^6-10-142 … ^6-10-185 = 10-01 frames (253 lines that also occur in 10-01 asserted byte-identical). Paṇṇattiniddesavāro. = Mục giải thích về sự định danh. [2-01]
#### Uppādavāro (a heading by itself) = Mục về sự sinh khởi [sample SECTION, as 6-01 / 8]
Question frames, «no ca» verbs, Āmantā / No [2-01, 7-01]; Āmantā …pe…. = Đúng vậy… [7-04]
(Cakkhundriyamūlakaṃ) … = (Phần dựa trên năng lực mắt) … [3-01 MULAKA + 10-01 faculty names]
sacakkhukānaṃ / acakkhukānaṃ, sasotakānaṃ / asotakānaṃ, saghānakānaṃ / aghānakānaṃ, sacittakānaṃ / acittakānaṃ = có / không có mắt, tai, mũi, tâm; two attributes joined «và» [3-01]
Rūpāvacare arūpāvacare / Asaññasatte arūpe / Catuvokāre pañcavokāre tattha = Trong cõi hình sắc, cõi không hình sắc / … [3-01 where3]
Yattha X uppajjati tattha Y…pe… Z…pe… W uppajjatīti? = Ở nơi nào mà X sinh khởi, thì ở nơi ấy có phải Y… Z… W sinh khởi không? [3-01 / 3-02 run]
pavatte <kind>cittassa uppādakkhaṇe = trong đời sống, vào khoảnh khắc sinh khởi của <tâm …> [5-01 PAVATTE / PAVATTE_JOIN, now = 9-01; 8 moments]

## New: attributes of the beings (ATTR10, attr_group)
itthīnaṃ / na itthīnaṃ = là người nữ / không phải là người nữ [new; người nữ = 10-01 bare word, pi-2]
purisānaṃ / na purisānaṃ = là người nam / không phải là người nam [new]
somanassena / vinā somanassena = có niềm vui đi kèm / không có niềm vui đi kèm [new; pi-1 somanassasahagata «có niềm vui đi kèm»]
upekkhāya / vinā upekkhāya = có sự bình thản đi kèm / không có sự bình thản đi kèm [new; pi-1 upekkhāsahagata]
sahetukānaṃ / ahetukānaṃ = có gốc rễ / không có gốc rễ [coordinator; sample SAHETUKA / AHETUKA]
ñāṇasampayuttānaṃ / ñāṇavippayuttānaṃ = gắn liền với hiểu biết / không gắn liền với hiểu biết [pi-1]
upapajjantīnaṃ (fem.) = đang tái sinh; tāsaṃ = ở những người ấy (Vietnamese has no gender here) [new]
Sacakkhukānaṃ na itthīnaṃ upapajjantānaṃ = Ở những người đang tái sinh có mắt và không phải là người nữ [3-01 ATTR_GROUP + new]
Itthīnaṃ upapajjantīnaṃ = Ở những người đang tái sinh là người nữ [new]

## New: citta kinds (citta_kind)
<X>sampayuttacitta / <X>vippayuttacitta = tâm gắn liền với <X> / tâm không gắn liền với <X> (X: somanassa niềm vui, upekkhā sự bình thản, saddhā niềm tin, ñāṇa hiểu biết) [pi-1; 5-01 CITTA_KIND pattern]
somanassasampayuttasaddhāvippayuttacitta = tâm gắn liền với niềm vui và không gắn liền với niềm tin (parts joined «và», in the Pāli order) [5-01 pattern]
Pavatte <kind>cittassa uppādakkhaṇe tesaṃ … (no person group) = Trong đời sống, vào khoảnh khắc sinh khởi của <tâm …>, thì ở những người ấy … [new; 2-01 STATEMENT_RES]

## Source points (translated as written)
^6-10-142: «(Kha) indriyaṃ saddhindriyanti?» singular indriyaṃ (the parallel lines: indriyā) = «Năng lực có phải là năng lực niềm tin không?».
^6-10-146: the answer is split over two lines; kept.
^6-10-155, ^6-10-163: «na cakkhundriyaṃ …pe….» has a space before …pe…; «…» written without it (8 ^6-8-61).
^6-10-168 «(Ka) na kāyo na indriyanti? Āmantā.» without the explanation the other members get (as 10-01 ^6-10-141).
^6-10-169, ^6-10-180: question and answer on one line; kept.
^6-10-191: first answer «Pavatte somanassasampayuttasaddhāvippayutta…» has no rebirth group (the second has «Somanassena upapajjantānaṃ»); as written.
^6-10-198 / ^6-10-199: a new question begins on the same line as an answer; kept on that line.

## For review
«những người đang tái sinh gắn liền với hiểu biết» (ñāṇasampayuttānaṃ upapajjantānaṃ, persons «associated with knowledge»; literal, pi-1 term); alternative «có hiểu biết đi kèm».
«là người nữ» for itthīnaṃ (English rails «as women»); alternative «tái sinh làm người nữ».
