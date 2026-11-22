# notes-7-04: Sānusayavāra, paṭiloma (niranusayo), 7-04-anusayayamaka.md

Builder: build_7-04_vi.py (imports build_sample_vi and build_7-01_vi; importing writes nothing).
Format: Pāli = tiếng Việt. [7-01] = frame-setter constant used verbatim; [7-01 proposed] = 7-01 proposal, now used; [new] = settled here.

## Reused from 7-01 (verbatim)
Tendencies, tl() lists (A ca B ca = A và B; A, B và C; A…pe… B = A… B) [7-01]
Xena niranusayo = không có X; no ca … niranusayo = … vẫn có X [7-01 proposed, YO_VERB]
niranusayā (plural) = same as niranusayo [new: Vietnamese has no number]
(Ka) yo A niranusayo so B niranusayoti? = (a) Người nào không có A, thì có phải người ấy không có B không? [7-01 proposed, question_yo]
(Kha) yo vā pana … = (b) Còn người nào … [7-01 proposed]
yato … tato …ti? = Đối với nơi nào mà không có A, thì có phải đối với nơi ấy không có B không? [7-01 proposed]
yo yato … so tato …ti? = Người nào, đối với nơi nào mà không có A, thì có phải người ấy, đối với nơi ấy không có B không? [7-01 proposed]
apariyāpanne = nơi những gì không nằm trong các cõi tồn tại [7-01 proposed]
sabbattha = ở mọi nơi [7-01 proposed]
dukkhāya vedanāya / kāmadhātuyā dvīsu (tīsu) vedanāsu / rūpadhātuyā / arūpadhātuyā [7-01 PLACE_VI]
Sānusayavāra (heading) = Mục về sự có khuynh hướng tiềm ẩn [7-01 proposed / terms]
(Gha) paṭilomapuggalo / (Ṅa) paṭilomaokāso / (Ca) paṭilomapuggalokāsā = (d) Chiều ngược theo người / (e) Chiều ngược theo nơi chốn / (f) Chiều ngược theo người và nơi chốn [terms]
Sānusayavāre paṭilomaṃ. = Chiều ngược trong mục về sự có khuynh hướng tiềm ẩn. [7-01 proposed VARE_DIR]
(Ekamūlakaṃ) … (Chakkamūlakaṃ) = (Phần dựa trên một mục) … (Phần dựa trên bộ sáu) [7-01]
Āmantā. = Đúng vậy. [sample]

## New frames (for the other yo / so chapters: 7-03, 7-05 … 7-08)
Persons as subjects (nominative = the 7-01 genitive form without «Ở»):
Anāgāmī = Bậc không trở lại [pi-4]
Arahā = Bậc A-la-hán [pi-5]
Puthujjano = Người phàm phu [pi-1 / pi-4]
Dve puggalā = Hai hạng người [pi-4]
Tayo puggalā = Ba hạng người [pi-4]
Cattāro puggalā = Bốn hạng người [pi-4]
Teva puggalā = Chính những hạng người ấy [new; 7-01 Tesaññeva puggalānaṃ]
Sveva puggalo = Chính hạng người ấy [new; 7-01 Tasseva puggalassa]
tato (answer) = đối với nơi ấy [7-01 YO_DEM_VI]
so tato (answer) = người ấy, đối với nơi ấy [7-01 YO_DEM_VI]
te tato = những người ấy, đối với nơi ấy [new]
<person> A niranusayo, no ca B niranusayo. = <person> không có A, nhưng vẫn có B. [new; nominative subject, no comma]
<person> A ca niranusayo B ca niranusayo. = <person> không có A, đồng thời cũng không có B. [new; 7-01 «đồng thời … cũng»]
<places> tato A niranusayo, no ca tato B niranusayo. = <places>, thì đối với nơi ấy không có A, nhưng đối với nơi ấy vẫn có B. [new]
<person> <places> so / te tato <clause>. = <person>, <places>, thì người ấy / những người ấy, đối với nơi ấy <clause>. [new; 7-01 shape]
no ca so tato / no ca te tato = nhưng người ấy, đối với nơi ấy / nhưng những người ấy, đối với nơi ấy [new]
<person> sabbattha <clause>. = <person>, ở mọi nơi, <clause>. [new]
Āmantā …pe…. / Āmantā…pe…. = Đúng vậy… [new; «….» is never written]
<statement> …pe…. = <statement without its period>… [new]
Sānusayavāro. = Mục về sự có khuynh hướng tiềm ẩn. [new; parallel to 7-01 «Anusayavāro.»]

## Source slips (rendered as meant, reported)
^6-7-130: «dukkhāya vedanāya ariyāpanne» = apariyāpanne.
^6-7-127: «Arahā sabbattha bhavarāgānusayena niranusayo kāmarāgānusayena ca paṭighānusayena ca niranusayo»: first «ca» missing; rendered with the «đồng thời cũng» frame like every parallel sentence.
^6-7-127: «no ca so tato mānānusayena ca niranusayo»: stray «ca» after a single tendency; nothing to render.
^6-7-122: «… niranusayo no ca so tato …»: comma missing before «no ca»; written with the comma.
«Āmantā …pe….» (^6-7-102, ^6-7-113, ^6-7-118) vs «Āmantā…pe….» (^6-7-124): spacing only, same Vietnamese.

## Tool note
check_lines (sample) and verify_rails_vi.py flag the letter f in the label «(f)» (= (Ca), terms file / B.LABEL). The builder accepts it only when the line is otherwise clean; verify_rails_vi.py still reports the heading line ^6-7-5-3-0.
