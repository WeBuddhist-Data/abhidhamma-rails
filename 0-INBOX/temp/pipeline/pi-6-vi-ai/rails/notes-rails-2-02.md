# pi-6 rails 2-02 (Khandhayamaka 2): family E (pariññāvāra) frames; family B additions

Builder: build_rails_2-02_vi.py (family E setter; import with importlib). Family E API: `PARIJANATI`, `TENSE_VI`, `tense_vi`, `make_verbs`, `rows_na`, `rows_fused`, `E_VERBS`, `e_verb`, `denied`, `obj_vi`, `split_groups`, `Persons` / `PERSONS` (.extended(nom=, acc=, rel_np=, rel_vp=)), `e_head`, `except_head`, `ye_head`, `ye_ca_head`, `e_single`, `e_noca`, `e_both`, `e_sentence`, `yo_q`, `e_question`, `e_answers`, `e_line`. A later chapter passes its own `Members` (2-01 class), its verbs merged into E_VERBS (same tense rule) and its persons via PERSONS.extended(...). Families A / B come from build_rails_2-01_vi, family C shapes from build_rails_7-01_vi, unchanged. Format: Pāli = tiếng Việt.


## Family E: verbs (tense rule = family B's VERB_TABLE; asserted)

<V> present / past / future (positive) = «V» / «đã V» / «sẽ V»
<V> present / past / future (negative, separate na or fused) = «không V» / «chưa từng V» / «sẽ không V»
parijānāti = hiểu biết trọn vẹn
parijānanti = hiểu biết trọn vẹn
parijānittha = đã hiểu biết trọn vẹn
parijānissati = sẽ hiểu biết trọn vẹn
parijānissanti = sẽ hiểu biết trọn vẹn
na parijānāti = không hiểu biết trọn vẹn
na parijānanti = không hiểu biết trọn vẹn
na parijānittha = chưa từng hiểu biết trọn vẹn
na parijānissati = sẽ không hiểu biết trọn vẹn
na parijānissanti = sẽ không hiểu biết trọn vẹn
after no ca, negative verb (denied) = present «vẫn V», past «đã từng V», future «vẫn sẽ V» (B.denied_vi)
after no ca, positive verb = the verb's own negative: «không V» / «chưa từng V» / «sẽ không V»

## Family E: question shell (yo / so; = coordinator person shell without «ở», as 7-03)

(Ka) yo A V1 so B V2ti? = (a) Người nào mà V1 A, thì người ấy có phải V2 B không?
(Kha) yo vā pana B V1 so A V2ti? = (b) Còn người nào mà V1 B, thì người ấy có phải V2 A không?
Yo … so …ti? (no label) = Người nào mà V1 A, thì người ấy có phải V2 B không?
(Ka) yo rūpakkhandhaṃ parijānāti so vedanākkhandhaṃ parijānātīti? = (a) Người nào mà hiểu biết trọn vẹn khối vật chất, thì người ấy có phải hiểu biết trọn vẹn khối cảm giác không?
(Kha) yo vā pana vedanākkhandhaṃ na parijānittha so rūpakkhandhaṃ na parijānātīti? = (b) Còn người nào mà chưa từng hiểu biết trọn vẹn khối cảm giác, thì người ấy có phải không hiểu biết trọn vẹn khối vật chất không?
(Ka) yo rūpakkhandhaṃ na parijānāti so vedanākkhandhaṃ na parijānissatīti? = (a) Người nào mà không hiểu biết trọn vẹn khối vật chất, thì người ấy có phải sẽ không hiểu biết trọn vẹn khối cảm giác không?

## Family E: answer heads (nominative persons)

Arahā … (sg) = Bậc A-la-hán …
Aggamaggasamaṅgī … (sg) = Người có được con đường tối thượng …
X-ñca Y-ñca ṭhapetvā avasesā puggalā … = Ngoại trừ X và Y, những hạng người còn lại …
Aggamaggasamaṅgiñca arahantañca ṭhapetvā avasesā puggalā … = Ngoại trừ người có được con đường tối thượng và bậc A-la-hán, những hạng người còn lại …
Ye <VP> te … = Những người nào <VP>, thì những người ấy …
Ye maggaṃ paṭilabhissanti te … = Những người nào sẽ đạt được con đường, thì những người ấy …
<P> ye ca <NP> <VP> te … = <P> và <NP> nào <VP>, thì những người ấy …
Arahā ye ca puthujjanā maggaṃ na paṭilabhissanti te … = Bậc A-la-hán và những người phàm phu nào sẽ không đạt được con đường, thì những người ấy …
Aggamaggasamaṅgī ye ca puthujjanā maggaṃ na paṭilabhissanti te … = Người có được con đường tối thượng và những người phàm phu nào sẽ không đạt được con đường, thì những người ấy …
maggaṃ paṭilabhissanti = sẽ đạt được con đường
maggaṃ na paṭilabhissanti = sẽ không đạt được con đường

## Family E: answer frames

P A V. = P V A.
A V. (bare answer, e.g. 7-07 «Tadekaṭṭhaṃ parijānāti.») = V A.
P A V1, no ca B V2 (V2 negative: denied) = P V1 A, nhưng vẫn V2 B / đã từng V2 B / vẫn sẽ V2 B.
P A V1, no ca B V2 (V2 positive) = P V1 A, nhưng không V2 B / chưa từng V2 B / sẽ không V2 B.
…, no ca B ca C ca V2 (positive; neither) = P V1 A, nhưng không V2 B, cũng không V2 C.
…, no ca B ca C ca na V2 (negative; the list denied) = P V1 A, nhưng vẫn V2 B và C.
P A ca B ca V. (one verb, a list) = P V A và B.
P A-ñca V1 B-ñca V2. = P V1 A, cũng V2 B.
Arahā rūpakkhandhaṃ na parijānāti, no ca vedanākkhandhaṃ na parijānittha. = Bậc A-la-hán không hiểu biết trọn vẹn khối vật chất, nhưng đã từng hiểu biết trọn vẹn khối cảm giác.
Aggamaggasamaṅgiñca arahantañca ṭhapetvā avasesā puggalā rūpakkhandhañca na parijānanti vedanākkhandhañca na parijānittha. = Ngoại trừ người có được con đường tối thượng và bậc A-la-hán, những hạng người còn lại không hiểu biết trọn vẹn khối vật chất, cũng chưa từng hiểu biết trọn vẹn khối cảm giác.
Ye maggaṃ paṭilabhissanti te rūpakkhandhaṃ na parijānanti, no ca vedanākkhandhaṃ na parijānissanti. = Những người nào sẽ đạt được con đường, thì những người ấy không hiểu biết trọn vẹn khối vật chất, nhưng vẫn sẽ hiểu biết trọn vẹn khối cảm giác.
Arahā ye ca puthujjanā maggaṃ na paṭilabhissanti te rūpakkhandhañca na parijānanti vedanākkhandhañca na parijānissanti. = Bậc A-la-hán và những người phàm phu nào sẽ không đạt được con đường, thì những người ấy không hiểu biết trọn vẹn khối vật chất, cũng sẽ không hiểu biết trọn vẹn khối cảm giác.
Aggamaggasamaṅgī vedanākkhandhaṃ na parijānissati, no ca rūpakkhandhaṃ na parijānāti. = Người có được con đường tối thượng sẽ không hiểu biết trọn vẹn khối cảm giác, nhưng vẫn hiểu biết trọn vẹn khối vật chất.

## Headings and closing lines

Uppādanirodhavāro = Mục về sự sinh khởi và sự chấm dứt
Pariññāvāro = Mục về sự hiểu biết trọn vẹn
Paccuppannavāro = Mục về hiện tại
Atītavāro = Mục về quá khứ
Anāgatavāro = Mục về tương lai
Paccuppannātītavāro = Mục về hiện tại và quá khứ
Paccuppannānāgatavāro = Mục về hiện tại và tương lai
Atītānāgatavāro = Mục về quá khứ và tương lai
Nirodhavāro. = Mục về sự chấm dứt.
Uppādanirodhavāro. = Mục về sự sinh khởi và sự chấm dứt.
Pariññāvāro. = Mục về sự hiểu biết trọn vẹn.
Khandhayamakapāḷi niṭṭhitā. = Phần các cặp câu hỏi về các khối đã hoàn tất.
Namo tassa bhagavato arahato sammāsambuddhassa = Kính lễ Đức Thế Tôn, bậc A-la-hán, bậc Tự Giác Ngộ Hoàn Toàn
(Yathā uppādavāre paccuppannātītaṃ vibhattaṃ tathā idha vibhajitabbaṃ). = (Mục về hiện tại và quá khứ như đã được phân tích trong mục về sự sinh khởi, ở đây cũng nên phân tích như vậy).

## Family B additions (2-01 frames, new heads / cut lines)

<persons> ye ca <plane-acc> upapajjitvā parinibbāyissanti tesaṃ … = Ở những người thuộc kiếp sống cuối cùng đang tái sinh và những người nào sau khi tái sinh vào cõi không hình sắc sẽ nhập Niết-bàn trọn vẹn, thì ở những người ấy …
<persons> ye ca <plane-acc> upapajjitvā parinibbāyissanti tesaṃ cavantānaṃ tesaṃ … = Ở những người thuộc kiếp sống cuối cùng đang tái sinh vào cõi không hình sắc và những người nào sau khi tái sinh vào cõi không hình sắc sẽ nhập Niết-bàn trọn vẹn, khi những người ấy đang chết đi, thì ở những người ấy …
tesaṃ cavantānaṃ (after a ye ca clause) = khi những người ấy đang chết đi
Yattha A V…pe…. = Ở nơi nào mà khối vật chất chấm dứt…
Yattha A V (yatthakaṃ paripuṇṇaṃ kātabbaṃ). = Ở nơi nào mà khối vật chất không chấm dứt (phần về nơi chốn nên được trình bày đầy đủ).
<sentence>…pe…. = <câu>…  (7-03 pe_tail)
A ca V1, B ca V2 (comma) / A ca V1 B V2 / A V1 B ca V2 (one ca missing) = the both-frame «A V1, B cũng V2»

## Termbase gaps and choices (for the coordinator)

- na parijānittha «chưa từng hiểu biết trọn vẹn»: no termbase entry for the negative past; built by the family-B rule (na nirujjhittha «chưa từng chấm dứt», nuppajjittha «chưa từng sinh khởi»). Likewise na parijānissati / na parijānissanti «sẽ không hiểu biết trọn vẹn», na parijānanti «không hiểu biết trọn vẹn».
- No-pronoun 'no ca' (person subject, transitive verb): denied negative «nhưng vẫn V B» / «nhưng đã từng V B» / «nhưng vẫn sẽ V B»; positive «nhưng không V B» (the verb's own negative; = 7-05 «nhưng không dứt bỏ A, cũng không dứt bỏ B»; 7-01's «không có B V» is the intransitive-subject frame and does not fit an object). A denied negative LIST «nhưng vẫn V B và C» is built by analogy with the coordinator's «A và B vẫn V» (not met in 2-02; for the coordinator to confirm).
- maggaṃ na paṭilabhissanti «sẽ không đạt được con đường» (termbase has only the positive; separate na).
- avasesā puggalā «những hạng người còn lại» (termbase Avasesā «còn lại» + puggalā «hạng người»).
- puthujjanā in «… ye ca puthujjanā … te» = «những người phàm phu nào …» (termbase «người phàm phu»).
- (yatthakaṃ paripuṇṇaṃ kātabbaṃ): termbase yatthakaṃ «phần về nơi chốn»; paripuṇṇaṃ kātabbaṃ has no entry: «nên được trình bày đầy đủ».
- (Yathā uppādavāre paccuppannātītaṃ vibhattaṃ tathā idha vibhajitabbaṃ): pi-2's «như đã được phân tích trong …, ở đây cũng nên phân tích như vậy»; paccuppannātītaṃ = «mục về hiện tại và quá khứ»; the Pāli has no comma, the Vietnamese clause break takes one; the Pāli's «).» kept.
- tesaṃ cavantānaṃ after a ye ca clause: «khi những người ấy đang chết đi» (the dying applies to the ye group).

## Slips (translated as written or as plainly meant)

- ^6-2-185 «vadanākkhandho» for vedanākkhandho (spelling slip; termbase lists it): «khối cảm giác».
- ^6-2-134 «saññākkhandho ca nirujjhissati vedanākkhandho nirujjhati» (second «ca» missing) and ^6-2-163 «rūpakkhandho nuppajjati vedanākkhandho ca na nirujjhati» (first «ca» missing): rendered as the both-frame «A V1, B cũng V2», as the parallel lines.
- ^6-2-151 «rūpakkhandho ca na nirujjhittha, vedanākkhandho ca na nirujjhissati»: the comma inside the both-frame is the frame's own «,».
- ^6-2-130 «Yattha … (yatthakaṃ paripuṇṇaṃ kātabbaṃ).» and ^6-2-135 … «Yattha … …pe….»: cut opening halves of the place question, no «?» in the Pāli: «Ở nơi nào mà …» + the note / «…».
- ^6-2-185 «…uppajjati…pe….» then the editorial note «(Yathā … vibhajitabbaṃ).»: kept as two lines.
