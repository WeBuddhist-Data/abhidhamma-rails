# notes-2-02: family E (pariññāvāra) frames, set by 2-02-khandhayamaka.md; family B additions

Builder: build_2-02_vi.py (import with importlib: `E = importlib.import_module("build_2-02_vi")`; importing writes nothing).
It imports build_sample_vi, build_2-01_vi (families A / B, verbatim), build_7-01_vi (yo / so frame, YO_VERB) and
build_7-04_vi (nominative person answer frames). Every frame below is a constant or helper there.
Format: Pāli = tiếng Việt. [pi-N] = from the approved pi-N rails (asserted); [2-01] / [7-01] / [7-04] = imported constant; [new] = set here.
Labels: always build_sample_vi.LABEL.

## Family E: verb (E_BASE, E_PRED, e_vparse, e_pred, e_deny; tenses = the 2-01 tables)
parijānāti / parijānanti = hiểu biết trọn vẹn X [pi-2 / pi-5; 7-01 YO_VERB, asserted byte-identical]
na parijānāti / na parijānanti = không hiểu biết trọn vẹn X [7-01]
no ca … na parijānāti = … vẫn hiểu biết trọn vẹn X [7-01]
parijānittha = đã hiểu biết trọn vẹn X; na parijānittha = chưa từng hiểu biết trọn vẹn X; no ca … na parijānittha = … đã từng hiểu biết trọn vẹn X [2-01 tense pattern]
parijānissati / parijānissanti = sẽ hiểu biết trọn vẹn X; na … = sẽ không hiểu biết trọn vẹn X; no ca … na … = … vẫn sẽ hiểu biết trọn vẹn X [2-01 tense pattern]
(plural = singular; the object follows the verb: rūpakkhandhaṃ / rūpakkhandhañca = khối vật chất)

## Family E: questions (e_q; 7-01 YO_Q_FRAME)
(Ka) yo X v1 so Y v2ti? = (a) Người nào <v1> X, thì có phải người ấy <v2> Y không? [7-01]
(Kha) yo vā pana Y v1 so X v2ti? = (b) Còn người nào <v1> Y, thì có phải người ấy <v2> X không? [7-01]
Answers: Āmantā. = Đúng vậy. [sample]; No. = Không. [7-01]

## Family E: answers (e_but, e_both, e_subject; 7-04 frames)
<Person> X v1, no ca Y v2. = <Person> <v1> X, nhưng <no-ca v2> Y. [7-04 BUT_C + STATEMENT_PERSON]
<Subject> Xñca v1 Yñca v2. = <Subject> <v1> X, đồng thời cũng <v2> Y. [7-04 BOTH_C]
<Relative subject> te <clause>. = <Relative subject>, thì những người ấy <clause>. [7-04 STATEMENT_RES; E_TE new]
Arahā = Bậc A-la-hán; arahantaṃ = bậc A-la-hán [pi-5; 7-04]
Aggamaggasamaṅgī = Người có được con đường tối thượng [coordinator «Shared person terms», = 7-05 … 7-08; pi-4 maggasamaṅgī «người có được con đường»]
Aggamaggasamaṅgiñca arahantañca ṭhapetvā avasesā puggalā = Ngoại trừ người có được con đường tối thượng và bậc A-la-hán, những hạng người còn lại [2-01 a_except_n + a_and; coordinator: puggala «hạng người»]
Ye maggaṃ paṭilabhissanti te = Những người nào sẽ đạt được con đường, thì những người ấy [new; magga «con đường» pi-4, paṭilabhati «đạt được» (kept apart from samaṅgī «có được»)]
X ye ca puthujjanā maggaṃ na paṭilabhissanti te = X và những người phàm phu nào sẽ không đạt được con đường, thì những người ấy [new; puthujjana pi-4 / pi-5]
Pariññāvāro (heading) / Pariññāvāro. = Mục về sự hiểu biết trọn vẹn / Mục về sự hiểu biết trọn vẹn. [terms; PARINNA_EXACT]
Paccuppannavāro … Atītānāgatavāro (unnumbered headings) = the approved time headings without number [sample SECTION]

## Family B additions (who2, pe_fragment, pe_end, PARIPUNNA, YATHA_VIBHATTA)
<beings> ye ca <P>ṃ upapajjitvā parinibbāyissanti tesaṃ cavantānaṃ (tesaṃ …) = Ở <beings> và những người đang chết đi mà sau khi tái sinh vào <plane> sẽ nhập Niết-bàn trọn vẹn, thì ở những người ấy … [new YE_CA_CAVANTA]
<beings> ye ca <P>ṃ upapajjitvā parinibbāyissanti tesaṃ … = Ở <beings> và những người nào sau khi tái sinh vào <plane> sẽ nhập Niết-bàn trọn vẹn, thì ở những người ấy … [2-01 YE_UPAPAJJITVA + YE_CA_JOIN]
Yattha X v…pe…. = Ở nơi nào mà X v… [new PE_FRAG; start of the 7-01 Q_FRAME]
Yattha X v (yatthakaṃ paripuṇṇaṃ kātabbaṃ). = Ở nơi nào mà X v (phần về nơi chốn nên được trình bày đầy đủ). [new PARIPUNNA]
<statement>…pe…. = <statement without its period>… [7-04 rule]
(Yathā uppādavāre paccuppannātītaṃ vibhattaṃ tathā idha vibhajitabbaṃ). = (Như mục về hiện tại và quá khứ đã được phân tích trong mục về sự sinh khởi, ở đây cũng nên phân tích như vậy). [pi-2 «(Như đã được phân tích trong …, ở đây cũng nên phân tích như vậy.)»]
Nirodhavāro. = Mục về sự chấm dứt.; Uppādanirodhavāro. = Mục về sự sinh khởi và sự chấm dứt.; Pavattivāro niṭṭhito. = Mục về sự diễn tiến đã hoàn tất. [sample SECTION + NITTHITA]
Khandhayamakapāḷi niṭṭhitā. = Phần các cặp câu hỏi về các khối đã hoàn tất. [sample yamaka_end]
Mixed verbs (uppajjati … nirujjhati in one question / answer): each verb from the 2-01 tables, no new frame.

## Source slips (rendered as meant)
^6-2-185: «vadanākkhandho» = vedanākkhandho.
^6-2-134: «saññākkhandho ca nirujjhissati vedanākkhandho nirujjhati»: second «ca» missing; both-frame used.
^6-2-163: «rūpakkhandho nuppajjati vedanākkhandho ca na nirujjhati»: first «ca» missing; both-frame used.
^6-2-151: comma inside «rūpakkhandho ca na nirujjhittha, vedanākkhandho ca …»; the Vietnamese frame has a comma there anyway.
