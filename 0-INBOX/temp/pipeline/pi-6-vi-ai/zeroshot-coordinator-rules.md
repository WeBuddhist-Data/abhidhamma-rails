# pi-6 zero-shot: coordinator rules (binding for every chapter agent)

The coordinator updates this file while chapter agents run. Re-read it before you build and again before you report.

## User decisions (2026-11-22, sample approved as proposed)
- Book title: «Các cặp câu hỏi». Yamaka headings «Các cặp câu hỏi về …» exactly as in vi-zeroshot-terms.md.
- mūlamūla = «cội rễ» (and the -mūlamūla / -mūlamūlaka compounds as in the sample).
- hetu inside the ten-term hetuvāra series = «nguyên nhân»; elsewhere sahetuka / ahetuka = «có / không có gốc rễ».
- The section headings listed in vi-zeroshot-terms.md under "Recurring section headings of the later chapters" are now approved: use them verbatim (uddeso «Phần nêu đề mục», niddeso «Phần giải thích», Paṇṇattivāro «Mục về sự định danh», Padasodhanavāro, …, Pavattivāro 1. uppādavāro, Pariññāvāro, the six time sections, the six person / place sections, paṭiloma «chiều ngược»).

## Labels (coordinator, 2026-11-22; replaces the a…h list in vi-zeroshot-terms.md)
- (Ka) (Kha) (Ga) (Gha) (Ṅa) (Ca) (Cha) (Ja) = (a) (b) (c) (d) (đ) (e) (g) (h): Vietnamese alphabet order, no f / j / w / z (verify_rails_vi rejects them). build_sample_vi.LABEL holds this; always take labels from B.LABEL, never type them.

## Frame families and who sets them
Wave 1 agents set the frames of a family; every later agent copies them verbatim from that agent's builder (import it) and notes file.
- Family A, paṇṇattivāra (padasodhana, padasodhanamūlacakka, suddha-X, suddha-X-mūlacakka; anuloma / paccanīka; the "X ti? … Y ti?" naming questions): set by 2-01-khandhayamaka (build_2-01_vi.py, notes-2-01.md).
- Family B, pavattivāra (yassa … tassa …, yattha … tattha …, yassa yattha … tassa tattha …; uppajjati / nirujjhati in present, past, future and the mixed tenses; the answer frames naming beings and planes): set by 2-01-khandhayamaka.
- Family C, anusayayamaka (uppattiṭṭhāna, anuseti, sānusaya, pajahati, pariññā, pahīna, uppajjati, dhātu): set by 7-01-anusayayamaka (build_7-01_vi.py, notes-7-01.md).
- Family D, cittayamaka (puggalavāra, dhammavāra, the fourteen time sections, uppajjamāna / nirujjhamāna, suttanta / abhidhamma mixtures): set by 8-cittayamaka (build_8_vi.py, notes-8.md).
- Family E, pariññāvāra (parijānāti frames): set by the first agent to finish a chapter containing it (2-02 normally); until then follow the English rails for structure and report your wording.

## Shared frames fixed by the coordinator
(added here as agents report)

### From 7-01 (finished 2026-11-22; builder build_7-01_vi.py, load with importlib.import_module("build_7-01_vi"); notes-7-01.md)
- Person / place question frame (the general shape every yamaka uses; 2-01 and 8 align to it):
  - (Ka) yassa A …, tassa B …ti? = (a) Ở người nào mà A …, thì ở người ấy có phải B … không?
  - (Kha) yassa vā pana B …, tassa A …ti? = (b) Còn ở người nào mà B …, thì ở người ấy có phải A … không?
  - yattha / tattha = ở nơi nào / ở nơi ấy; yassa yattha / tassa tattha = ở người nào, ở nơi nào / thì ở người ấy, ở nơi ấy.
- A …, no ca tassa B … = A …, nhưng ở người ấy B không …; A ca … B ca … = A …, đồng thời B cũng …; a denied negative verb is said plainly (no ca … nānuseti = «vẫn nằm sẵn»).
- Tesaññeva puggalānaṃ = Ở chính những hạng người ấy. No. = Không. Natthi. = Không có. (pi-3)
- Anusaya chapters 7-02 … 7-11: import build_7-01_vi; its slot-based frames cover the proposed nānuseti, pahīna / appahīna, uppajjati, sānusaya / pajahati / parijānāti forms; "…pe…" shortenings must be handled by your own builder.
### From 7-04 (finished 2026-11-22; build_7-04_vi.py, notes-7-04.md): person subjects for the anusaya chapters
- Anāgāmī = Bậc không trở lại; Arahā = Bậc A-la-hán; Puthujjano = Người phàm phu; Dve / Tayo / Cattāro puggalā = Hai / Ba / Bốn hạng người (pi-4); Teva puggalā = Chính những hạng người ấy; Sveva puggalo = Chính hạng người ấy.
- te tato = những người ấy, đối với nơi ấy; <places> tato … = <places>, thì đối với nơi ấy …; <person> sabbattha … = <person>, ở mọi nơi, …
- niranusayo = «không có X»; after "no ca" = «vẫn có X»; A ca niranusayo B ca niranusayo = «không có A, đồng thời cũng không có B».
- Āmantā …pe…. = «Đúng vậy…»; a statement ending "…pe…." ends in «…» without a period.

### From 2-01 (finished 2026-11-22; build_2-01_vi.py, load with importlib.import_module("build_2-01_vi"); notes-2-01.md): families A and B
- Imports the 7-01 person / place shape (REL_VI, DEM_VI, NO_CA_VI, Q_FRAME, BUT_C, BOTH_C, STATEMENT_RES, NATTHI, NO), so A/B and C agree byte for byte.
- A: (Ka) X Y(ti)? = (a) X có phải là Y không?; (Ka) na X na Y(ti)? = (a) Những gì không phải là X thì không phải là Y, có đúng không?; Avasesā khandhā na Y = Các khối còn lại không phải là Y.; X ṭhapetvā avasesā = ngoại trừ X, những gì còn lại; na ceva A na ca B = không phải là A cũng không phải là B; piyarūpaṃ sātarūpaṃ = Vật chất hiểu theo nghĩa điều đáng yêu, điều khoan khoái; Diṭṭhisaññā = Tri giác hiểu theo nghĩa quan điểm.
- B verbs: uppajjati / uppajjittha / uppajjissati = sinh khởi / đã sinh khởi / sẽ sinh khởi; negative không / chưa từng / sẽ không; after «no ca» on a negative verb vẫn sinh khởi / đã từng sinh khởi / vẫn sẽ sinh khởi; nirujjhati «chấm dứt» the same way. Short answers Có sinh khởi. / Đã sinh khởi. / Sẽ sinh khởi.
- B beings and planes: Asaññasattaṃ upapajjantānaṃ = Ở những người đang tái sinh vào cõi Vô Tưởng, thì ở những người ấy …; place answers «Trong cõi …, thì ở nơi ấy …»; cõi không hình sắc; cõi gồm năm / bốn / một khối; đang chết đi khỏi; đang nhập Niết-bàn trọn vẹn; suddhāvāsa = cõi Tịnh Cư; pacchimabhavika = những người thuộc kiếp sống cuối cùng.
- Every later yamaka chapter (Khandha 2-02, Āyatana, Dhātu, Sacca, Saṅkhāra, Dhamma, Indriya) imports build_2-01_vi and substitutes its own members (āyatana, dhātu, sacca, saṅkhāra, dhamma, indriya names from pi-1 / pi-2) into these frames.

### From 8 (finished 2026-11-22; build_8_vi.py, notes-8.md): family D and the aspect forms
- uppajjamāna = đang sinh khởi (na: không đang sinh khởi); uppanna = ở trạng thái đã sinh khởi (na: không ở trạng thái đã sinh khởi); niruddha / nirujjhamāna the same with chấm dứt. uppajjittha stays «đã sinh khởi» (2-01). Any later chapter meeting these forms copies them.
- Two predicates in one clause (X na Y) = «X nhưng không Y»; na ceva A na ca B with verbs = «không A, cũng không B» (with nouns 2-01's «không phải là A cũng không phải là B»).

### Shared person terms (coordinator, 2026-11-22; all yamakas)
- Aggamaggasamaṅgī = Người có được con đường tối thượng (7-05…7-08; not «cao nhất»); Anāgāmimaggasamaṅgī = Người có được con đường không trở lại; Aṭṭhamako = Người thứ tám; maggasamaṅgī «có được» vs paṭilabhati «đạt được» (2-02).
- X ṭhapetvā avasesā puggalā = Ngoại trừ X, những hạng người còn lại (puggala = «hạng người» as pi-4 / 7-04; not «những người còn lại»).

- Sabbesaṃ + participle (Sabbesaṃ cavantānaṃ / upapajjantānaṃ …) = «Ở tất cả những người đang …» (2-01). Bare Sabbesaṃ (Sabbesaṃ cittassa …, Sabbesaṃ …) = «Ở tất cả chúng sinh» (pi-2, 6-01); not «tất cả mọi người».
- pavatte (in the course of existence, as against at rebirth) = «trong đời sống», set off by commas as 9-01 does («Ở tất cả những người đang tái sinh, trong đời sống, vào khoảnh khắc …»); not «trong quá trình diễn tiến».
- Two-part citta kinds (AvippayuttaBvippayuttacitta, AsampayuttaBvippayutta …) = «tâm <A part> và <B part>» in the Pāli order, e.g. «tâm không gắn liền với niềm vui và không gắn liền với sự bình thản» (5-01, 10-02, 10-03); not «tâm vừa … vừa …» (9-01 / 9-02 to be aligned in the harmonise pass).
- yassa cittassa anantarā … = «ngay sau tâm nào đó» (9-01, 6-01 «ngay sau đó»); not «liền sau».

### From 2-02 (finished 2026-11-22; build_2-02_vi.py, notes-2-02.md): family E and B additions
- Pariññā: parijānāti present from 7-01 («hiểu biết trọn vẹn X» / «không …» / after no ca «vẫn …»); past / future with 2-01's tense tables. Helpers for later chapters: e_q, e_vparse, e_pred / e_deny, e_subject, e_but / e_both, translate_e(sentence, member_fn), PARINNA_EXACT.
- Ye maggaṃ paṭilabhissanti = Những người nào sẽ đạt được con đường; «(yatthakaṃ paripuṇṇaṃ kātabbaṃ)» = «(phần về nơi chốn nên được trình bày đầy đủ)»; «(Yathā uppādavāre … vibhajitabbaṃ).» = pi-2 wording «(Như … đã được phân tích trong …, ở đây cũng nên phân tích như vậy).»; who2() for «ye ca <P>ṃ upapajjitvā parinibbāyissanti».

- Open for the termbase stop (keep as 7-01 has them for now, same everywhere): sakkāya standalone «tự ngã» (sabbasakkāyapariyāpanna); dhātupucchāvāro «Mục hỏi theo các yếu tố» (dhātu here = plane).
