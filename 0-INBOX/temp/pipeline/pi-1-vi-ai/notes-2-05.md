# Notes for part 2-05 (Vietnamese plain zero-shot, world-transcending results, results of the unwholesome, functional minds, ^1-1-8-0 … ^1-582): new recurring terms and formulas

Builder: build_2-05_vi.py (imports build_matika_vi, build_ch2_01_sample_vi, build_2-01_2-02_vi, build_2-03_vi and
build_2-04_vi unchanged; adds entries to their tables in memory only, never overwriting one). `python -I -X utf8
build_2-05_vi.py` checks the 60 headings against vi-zeroshot-terms.md, asserts that the 15 Pāli lines that also occur
in 2-01 … 2-04 get the published Vietnamese byte for byte, and re-renders 412 earlier lines (through 2-04's dispatcher
and through this one) to prove the added entries changed nothing. Checks: verify_vi_2-05.py. 99 segments.
Helper: show_2-05_vi.py (prints Pāli / Vietnamese pairs of a finished part).
Reusable pieces (import with importlib): NEW_NAMES, NEW_PH, NEW_OPEN, STAGES_234, TASSEVA_LOK, TAG, KIRIYA_V,
SUKHAVIHARA_V, ANIMITTA_Q, RESULT_AKUSALA, S_KAYADUKKHA, G_ANNATAVI, ANNA_V, x2_vi(), open2_vi(), lok_vi(),
annatavi_qa(), translate_line().

## Headings and closing lines (headings verbatim from vi-zeroshot-terms.md; closing line = heading + «.» unless listed)
Paṭhamamaggavipāko. = Quả của con đường thứ nhất.
Lokuttaravipāko. = Quả vượt thế gian.
Vipākā abyākatā. = Các quả của nghiệp, không xác định về mặt đạo đức. (plural of #### Abyākatavipāko, 2-04)
Akusalavipākapañcaviññāṇāni. / Akusalavipākā manodhātu. / Akusalavipākā manoviññāṇadhātu. = Năm loại thức / Yếu tố ý / Yếu tố ý thức là quả của nghiệp bất thiện.
Kiriyā manodhātu. = Yếu tố ý mang tính chức năng.
Kiriyā manoviññāṇadhātu somanassasahagatā. / upekkhāsahagatā. = Yếu tố ý thức mang tính chức năng, có niềm vui đi kèm. / có sự bình thản đi kèm.
Ahetukā kiriyā abyākatā. = Các loại không xác định về mặt đạo đức, mang tính chức năng, không có gốc rễ.
Kiriyā abyākatā. = Các loại không xác định về mặt đạo đức, mang tính chức năng.
Cittuppādakaṇḍaṃ niṭṭhitaṃ. = Phần về sự sinh khởi của tâm đã hoàn tất. (terms file)

## Frames
Tasseva lokuttarassa kusalassa jhānassa katattā bhāvitattā vipākaṃ X, tasmiṃ samaye … = Như là quả của chính tầng thiền thiện vượt thế gian ấy đã được tạo và tu tập, khi một người X, thì vào lúc ấy …  (pattern of the 2-04 TASSEVA frame; bhāvita = tu tập; the wholesome sentence before it = the 2-03 frame, B.kusala_vi)
…nti kusalaṃ / …nti vipāko (inside a run) = … (thiện) / … (quả của nghiệp)
akusalassa kammassa katattā upacitattā vipākaṃ cakkhuviññāṇaṃ / vipākā manodhātu / manoviññāṇadhātu uppannaṃ/uppannā hoti = (Vào lúc) thức qua mắt / yếu tố ý / yếu tố ý thức sinh khởi như là quả của nghiệp bất thiện đã được tạo và tích lũy
manodhātu / manoviññāṇadhātu uppannā hoti (functional) = (Vào lúc) yếu tố ý / yếu tố ý thức sinh khởi, …
kiriyā neva kusalā nākusalā na ca kammavipākā (also neuter kiriyaṃ … kammavipākaṃ) = mang tính chức năng, không phải thiện, không phải bất thiện, cũng không phải là quả của nghiệp
rūpāvacaraṃ / arūpāvacaraṃ jhānaṃ bhāveti = (Vào lúc) một người tu tập tầng thiền thuộc cõi hình sắc / cõi không hình sắc
diṭṭhadhammasukhavihāraṃ = nhằm an trú trong hạnh phúc ngay trong đời này (sukhavihāra as «sukhavihārī» = an trú trong hạnh phúc)
second to fourth path in one run (^1-553) = the 2-03 stage phrases joined with «…»
Yā tesaṃ aññātāvīnaṃ dhammānaṃ aññā S – idaṃ tasmiṃ samaye aññātāvindriyaṃ hoti = Điều có ở các hiện tượng ấy của người đã hiểu biết trọn vẹn, tức là sự hiểu biết trọn vẹn, S – đây là năng lực của người đã hiểu biết trọn vẹn vào lúc ấy  (frame of jīvitindriya; S = the 2-03 paññā string … maggapariyāpannaṃ)
amoho abyākatamūlaṃ = sự không si mê, gốc rễ không xác định về mặt đạo đức (as alobho / adoso, 2-04)

## Names and phrases
dukkhindriyaṃ = năng lực khó chịu (pairs with sukhindriyaṃ = năng lực dễ chịu, 2-04; the factor dukkhaṃ stays «sự đau khổ»)
aññātāvindriyaṃ = năng lực của người đã hiểu biết trọn vẹn (aññātāvī = người đã hiểu biết trọn vẹn)
aññā = sự hiểu biết trọn vẹn (as aññindriyaṃ = năng lực hiểu biết trọn vẹn, 2-03)
animittaṃ (qualifying the absorption) = với tính chất không có dấu hiệu (nimitta = dấu hiệu, matrix ^1-M2-133; as suññataṃ / appaṇihitaṃ)
dukkhasahagataṃ = có sự đau khổ đi kèm (cf. sukhasahagataṃ = có hạnh phúc đi kèm)
sotaviññāṇaṃ uppannaṃ hoti (after …pe…) = thức qua tai sinh khởi

## Strings
kāyikaṃ asātaṃ kāyikaṃ dukkhaṃ kāyasamphassajaṃ asātaṃ dukkhaṃ vedayitaṃ kāyasamphassajā asātā dukkhā vedanā = sự bứt rứt nơi thân, sự khó chịu nơi thân, cảm nhận bứt rứt và khó chịu sinh từ sự tiếp xúc của thân, cảm giác bứt rứt và khó chịu sinh từ sự tiếp xúc của thân

## Choices to review
«(thiện)» / «(quả của nghiệp)» for «…nti kusalaṃ» / «…nti vipāko» (as the English «(wholesome)» / «(result)»).
animitta = «không có dấu hiệu»; aññātāvindriya = «năng lực của người đã hiểu biết trọn vẹn».
Closing lines «Vipākā abyākatā.», «Ahetukā kiriyā abyākatā.», «Kiriyā abyākatā.» are plural («Các …»), the headings singular.

## Source points translated as written
^1-528: «ime dhammā kusalā tasseva …» has no full stop; a semicolon and lower case «như là quả …» are written.
^1-553: «kāmarā gabyāpādānaṃ»: split word, read as kāmarāgabyāpādānaṃ (spelling slip).
^1-553: the wholesome clause (second to fourth path) has aññindriyaṃ, the result clause aññātāvindriyaṃ; kept.
^1-505 … ^1-507: the first-path result lists aññindriyaṃ; kept.
^1-544: stray comma «viharati, animittaṃ»; ^1-574: no comma «samādhindriyaṃ hoti manindriyaṃ»; ^1-579: no comma before «tasmiṃ samaye»: normal Vietnamese punctuation.
^1-515, ^1-528: stray space «phasso hoti …pe…»; ^1-518, ^1-528, ^1-542, ^1-546, ^1-556, ^1-576: stray space before «…pe…»; spacing mirrored («có sự tiếp xúc …», «với tính chất không có dấu hiệu …»).
^1-576: «…pe… ime dhammā abyākatā…pe… alobho abyākatamūlaṃ…» lists only alobho / adoso as roots, although knowledge-associated minds are included (as 2-04 ^1-498); nothing added.
^1-554, 558, 559, 560, 562 … 574 (line ends): «…pe….» = «….» (four dots), as in the earlier parts.
