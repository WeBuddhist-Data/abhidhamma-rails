# pi-6 rails: coordinator rules (binding for every chapter agent, 2026-11-22)

These extend vi-rails-brief.md. The coordinator adds to this file while chapter agents run: re-read it before you build and again before you report. Where this file and a finished chapter disagree, this file wins.

## The user's decisions (pi-6 termbase APPROVED.md, 2026-11-22; copy the wording)
- Verbs: the termbase gives the positive unbroken form (uppajjati «sinh khởi», uppajjittha «đã sinh khởi», uppajjissati «sẽ sinh khởi»; nirujjhati the same with «chấm dứt»); a fused negative keeps «không» (nuppajjati «không sinh khởi», nuppajjissati «sẽ không sinh khởi», nappajahissanti «sẽ không dứt bỏ»; nuppajjittha «chưa từng sinh khởi»). A separate "na" negates the positive term.
- After "no ca" a negative verb is denied, so it is said plainly with «vẫn»: «vẫn dứt bỏ», «vẫn hiểu biết trọn vẹn» (and the same for the other verbs).
- "no ca A ca B ca …" meaning "neither" = «không có A, cũng không có B» (not «không có A và B», which reads as "not both").
- kassaci = «ở một số chúng sinh» (pi-2).
- itthīnaṃ / purisānaṃ upapajjantānaṃ = «… tái sinh làm người nữ / người nam».
- 10-01 «Tai còn lại …» = «Phần tai còn lại không phải là năng lực» (avoid "the other ear").
- yassa cittassa anantarā … (6-01 and the chapters that repeat it): smooth Vietnamese, meaning unchanged; not the stiff «Vào tâm mà ngay sau đó …».
- kāyikaṃ / cetasikaṃ dukkhaṃ = «sự khó chịu nơi thân / trong tâm» (pi-1), also in the Sacca chapters. Bare dukkhaṃ follows its yamaka: the truth (Saccayamaka) «khổ đau», the faculty (Indriyayamaka dukkhindriya) «sự khó chịu».
- dhātupucchāvāro «Mục hỏi theo các cõi», dhātuvisajjanāvāro / Dhātuvisajjavāro «Mục trả lời theo các cõi» (dhātu = plane there; kāma- / rūpa- / arūpadhātu «cõi dục lạc / cõi hình sắc / cõi không hình sắc»).
- Beings in the genitive plural «chúng sinh trong cõi X», the plane itself «cõi X»; Itaresaṃ «người khác»; upapajjitvā «sau khi tái sinh»; Cittasamaṅgīnaṃ «người có được tâm»; paṭilabhissanti «sẽ đạt được»; upapajjissati (the Pāli slip for uppajjissati) «sẽ sinh khởi».
- Kept as built: sakkāya standalone «tự ngã»; Aṭṭhamako «Người thứ tám»; tadekaṭṭha «những gì cùng hiện diện với nó»; na vattabbo «không nên nói là …»; bhaṅgā «phải phân chia»; uppanna «ở trạng thái đã sinh khởi» (kept apart from uppajjittha «đã sinh khởi»); piyarūpa / diṭṭhisaññā / dibbacakkhu … in the «hiểu theo nghĩa …» frame; ñāṇasampayutta «gắn liền với hiểu biết»; eteneva bhāvena «trong chính trạng thái ấy»; bhava «kiếp sống» (apart from kappa «kiếp»); pavatte «trong đời sống»; anaññātaññassāmīti «sự biết được điều chưa từng biết»; samāpannānaṃ «người đang nhập»; sānusayo «có» (+ the anusaya); kāmadhātuṃyeva «chỉ … cõi dục lạc».

## Rules carried over from the zero-shot review (user-approved; rules, not wording)
- asammohantena = «mà không mê lầm» (pi-1 sammoha «sự mê lầm»), right after the verb, no «một cách».
- Two-part citta kinds (A-vippayutta B-vippayutta citta …) = «tâm <A part> và <B part>» in the Pāli order; never «tâm vừa … vừa …» (keep «vừa … vừa …» for "A ceva B ca" as the sample).
- A question cut by …pe… / … and ending in "?" = «… không?» (sample ^6-1-98); a cut line ending "…pe…." without "?" ends «…».
- sabbattha: «ở mọi nơi» where it means every plane; «ở mọi chỗ» where an editorial note means every case or section of the text.
- One «ở» for a run of person groups; a person group that follows a time phrase («vào khoảnh khắc …», «khi tâm … đang diễn ra») keeps its own «ở».
- "Pacchimabhavikānaṃ <A>ānaṃ <B>ānaṃ upapajjantānaṃ" is one group of persons.
- Plane before attribute: «sau khi tái sinh vào cõi X mà <attribute> …».
- A question the Pāli ends with "." stays as the Pāli has it unless it is plainly a question; report each.
- Identical Pāli = identical Vietnamese across all chapters of the book (and with pi-1 … pi-5 rails where the termbase does not decide otherwise).

## Shared person / place question shell (coordinator, extends the approved sample frame; all yamakas)
- (Ka) Yassa A …, tassa B …ti? = «(a) Ở người nào mà A …, thì ở người ấy có phải B … không?»
- (Kha) Yassa vā pana B …, tassa A …ti? = «(b) Còn ở người nào mà B …, thì ở người ấy có phải A … không?»
- yattha / tattha = «ở nơi nào» / «ở nơi ấy» (same shell); yassa yattha / tassa tattha = «ở người nào, ở nơi nào» / «thì ở người ấy, ở nơi ấy».
- Everything inside the slots (verb tenses, answers, beings, planes, partial-answer frames) is set by the family setters below.

## Family setters (rails)
Wave 1 agents set the frames of a family; every later agent imports that agent's builder (READ-ONLY, `importlib.import_module("build_rails_<N>_vi")` with rails\ on sys.path) and copies its strings byte for byte, and reads its notes file.
- Family A, paṇṇattivāra (padasodhana, padasodhanamūlacakka, suddha-X, suddha-X-mūlacakka; anuloma / paccanīka; the "X ti? … Y ti?" naming questions): set by rails 2-01.
- Family B, pavattivāra (yassa / yattha questions in present, past, future and the mixed tenses; uppajjati / nirujjhati; answers naming beings and planes): set by rails 2-01.
- Family C, anusayayamaka (uppattiṭṭhāna, anuseti, sānusaya, pajahati, pariññā, pahīna, uppajjati, dhātu): set by rails 7-01.
- Family D, cittayamaka (puggalavāra, dhammavāra, the time sections, uppajjamāna / nirujjhamāna / uppanna, suttanta / abhidhamma mixtures): set by rails 8.
- Family E, pariññāvāra (parijānāti frames): set by rails 2-02 (after 2-01).
- Wave 1 (2-01, 7-01, 8) agents: where your family touches another wave-1 family (2-01 / 7-01 share person verbs; 8 uses B tenses), keep the shared strings as named constants in your builder and list them in your notes; the coordinator aligns them when you report.

## Shared frames fixed by the coordinator
(added here as agents report)

### From rails 7-01 (finished 2026-11-22; build_rails_7-01_vi.py, notes-rails-7-01.md): family C and the shared answer shapes
- Every chapter with person / place answers uses these shapes (2-01 and 8 align to them): answer head «Ở <person>, …» (one «ở» per run of persons); each place keeps its own «ở»; <places> ettha «Ở <nơi>, …, thì ở đó …»; tassa / tesaṃ tattha «thì ở người ấy / những người ấy, ở nơi ấy …»; both-frame "A ca V B ca V" = «A V, B cũng V»; "no ca tassa / tesaṃ / tattha A V" = «, nhưng ở người ấy / ở những người ấy / ở nơi ấy không có A V»; neither "no ca tassa A ca B ca V" = «, nhưng ở người ấy không có A, cũng không có B V»; No. «Không.»; Natthi. «Không có.»; Āmantā. «Đúng vậy.».
- After "no ca" a NEGATIVE verb with a list (no ca tassa A ca B ca na-V: both are denied the negation, so both do V) = «, nhưng ở người ấy A và B vẫn V» (one item: «A vẫn V»). Lists join as 7-01: «A và B», «A, B và C».
- (Eka- / Duka- / Tika- / Catukka- / Pañcaka- / Chakkamūlakaṃ) = «(Phần xét từng mục một / từng nhóm hai / … / từng nhóm sáu)» (pi-3 series).
- After "no ca" a denied negative verb by tense: present «vẫn V» (vẫn sinh khởi, vẫn chấm dứt, vẫn nằm sẵn, vẫn dứt bỏ); future «vẫn sẽ V»; PAST «đã từng V» (no «vẫn»: «vẫn đã …» is stiff; «đã từng» answers «chưa từng»): nuppajjittha / na nirujjhittha after no ca = «đã từng sinh khởi» / «đã từng chấm dứt» (coordinator, 2026-11-22).
### From rails 7-02 and 7-03 (finished 2026-11-22; build_rails_7-02_vi.py, build_rails_7-03_vi.py and their notes): the anusaya chapters copy these
- Nominative person frame (sānusaya, niranusaya, pajahati, parijānāti … with yo / so): yo … so …ti? = «(a) Người nào mà <pred A>, thì người ấy có phải <pred B> không?»; (Kha) «(b) Còn người nào mà …»; yato / tato = 7-01's yattha / tattha wording («Ở nơi nào mà …, thì ở nơi ấy …»); yo yato / so tato = «Người nào, ở nơi nào mà …, thì người ấy, ở nơi ấy …»; nominative person heads = 7-01's person words without «Ở» («Bậc không trở lại có …»); Teva puggalā «Chính những hạng người ấy», Sveva puggalo «Chính hạng người ấy»; resumptive tato «thì ở nơi ấy», so / te tato «thì người ấy / những người ấy, ở nơi ấy»; both «có A, cũng có B»; no ca «nhưng không có A, cũng không có B»; bare answers «Có A.» (7-03 yo_q, PERSON_NOM, pred_vi / neg_vi).
- Negative both-frame «A không V, B cũng không V»; apariyāpanne «ở những gì không nằm trong các cõi tồn tại» (pi-1 / pi-2 apariyāpanna); <person> sabbattha «Ở <người>, ở mọi nơi, …»; cuts as 7-02 («(b) Còn ở nơi nào mà… không?», «Đúng vậy …»).

- From 7-04 (build_rails_7-04_vi.py): "A-ena niranusayo" = «không có A»; a negative list / both-frame = «không có A, cũng không có B, cũng không có C» (one «cũng không có» per item, never «không có B và C»); "no ca … niranusayo" = «, nhưng vẫn có A [và B]»; nominative "<person> sabbattha" = «Hai hạng người, ở mọi nơi, …»; Arahā «Bậc A-la-hán» in the nominative person list.

- From 7-05 (build_rails_7-05_vi.py): A pajahati «dứt bỏ A»; both «dứt bỏ A, cũng dứt bỏ B»; no ca … A ca B ca pajahati «nhưng … không dứt bỏ A, cũng không dứt bỏ B»; standalone Tadekaṭṭhaṃ pajahati. «Dứt bỏ những gì cùng hiện diện với nó.»; "A tadekaṭṭhaṃ" (modifier, bare citation form) «A, vốn cùng hiện diện với nó»; Pajahanavāre anulomaṃ. «Chiều thuận trong mục về sự dứt bỏ.»; a missing comma before "no ca" is added.

- From 7-06 (build_rails_7-06_vi.py): nappajahati «không dứt bỏ A», lists «không dứt bỏ A, cũng không dứt bỏ B»; no ca so / tato / so tato + negative «, nhưng người ấy / ở nơi ấy / người ấy, ở nơi ấy vẫn dứt bỏ A [và B]»; "<X> ṭhapetvā avasesā puggalā [sabbattha]" «Ngoại trừ <X>, những hạng người còn lại[, ở mọi nơi,] …»; Dvinnaṃ maggasamaṅgīnaṃ «hai người có được con đường»; Anāgāmimaggasamaṅgī «người có được con đường không trở lại»; Pajahanāvāre paṭilomaṃ. «Chiều ngược trong mục về sự dứt bỏ.».

- From 7-07 (build_rails_7-07_vi.py): the 7-05 / 7-06 frames written once with the verb as a parameter (`Verb`: PARIJ «hiểu biết trọn vẹn», PAJ «dứt bỏ»); 7-08 … 7-11 use it for parijānāti / pajahati. "A-ñca V B-ñca [C-ñca] tadekaṭṭhaṃ V" «V A, cũng V B [và C], vốn cùng hiện diện với nó»; no ca so / tato / so tato «nhưng người ấy / ở nơi ấy … vẫn …». A Pāli line that looks inconsistent with its answer (^6-7-243, no "na" in the second slot) is translated as written and listed for review, never emended.

- From 7-09 (build_rails_7-09_vi.py; coordinator-confirmed): predicates ANUSETI / PAHINA (pahīno «đã được dứt bỏ», appahīno «chưa được dứt bỏ»); "no ca … appahīno" = «…, nhưng ở người ấy A [và B] đã được dứt bỏ» (no «vẫn»: «đã được» answers «chưa được», like «đã từng» / «chưa từng»); na vattabbo standalone «Không nên nói là “đã được dứt bỏ” hay “chưa được dứt bỏ”.», with a subject «A [và B] thì không nên nói là …»; "pana sameti" in variants «nhưng phù hợp với» (pi-4); Pahīnavāre anulomaṃ. «Chiều thuận trong mục về những gì đã được dứt bỏ.». 7-10, 7-11 import PAHINA, nv_vi, sentence, question.

- From 7-10 (build_rails_7-10_vi.py): UPPAJJ «sinh khởi / không sinh khởi / vẫn sinh khởi»; DHATU / parse_planes / dhatu_phrase: "na X [na Y]" «nơi không phải là cõi X [cũng không phải là cõi Y]»; dhatu_head "<fr> cutassa <to> upapajjantassa" «Ở người đã chết đi khỏi <fr> và đang tái sinh vào <to>, …» (cutassa: past «đã chết đi khỏi»); KATI_Q «bao nhiêu khuynh hướng tiềm ẩn nằm sẵn, bao nhiêu … không nằm sẵn, bao nhiêu … phải phân chia?» (pi-2 ^2-151); dhatu_label «(Phần dựa trên …)»; vitthāretabbaṃ «(nên được trình bày chi tiết)»; closers «Mục về sự sinh khởi.», «Mục hỏi theo các cõi.». 7-11 imports these.

### From rails 2-01 (finished 2026-11-22; build_rails_2-01_vi.py, notes-rails-2-01.md): families A and B
- Imports 7-01's shell and connectors, so A / B and C agree byte for byte. Every later yamaka chapter (Khandha 2-02, Āyatana, Dhātu, Sacca, Saṅkhāra, Dhamma, Indriya) imports build_rails_2-01_vi and plugs in its own members (a `Members`-style table from the termbase) into these frames.
- A: naming questions «(a) X có phải là Y không?», «Những gì không phải là X thì không phải là Y, có phải không?»; answers as 2-01.
- B: VERB_TABLE (fused / separate na; past negative «chưa từng V»; after no ca: present «vẫn V», future «vẫn sẽ V», past «đã từng V» via denied_vi / noca_vi); head parser (PLANES, PARTICIPLES, ATTRS, QUANT, the Ye-clause head «Những người nào …, thì ở những người ấy …»); heads keep the Pāli's tesaṃ / tattha («Ở <persons>, thì ở những người ấy, ở nơi ấy …»); planes in a person group take their preposition («tái sinh vào», «chết đi khỏi», «trong»); short verb answers «Có sinh khởi.» / «Đã sinh khởi.» / «Sẽ sinh khởi.».

### From rails 8 (finished 2026-11-22; build_rails_8_vi.py, notes-rails-8.md): family D and the aspect forms
- Any chapter meeting these forms imports build_rails_8_vi: uppanna «ở trạng thái đã sinh khởi», niruddha «ở trạng thái đã chấm dứt», uppajjamāna / nirujjhamāna «đang sinh khởi / đang chấm dứt»; with na «không ở trạng thái …» / «không phải đang …»; finite tenses from 2-01's VERB_TABLE.
- "A na B" (one subject, two predicates) = «A nhưng không B»; "V1 ceva V2 ca" = «vừa V1 vừa V2»; "na ceva A na ca B" with verbs = «không A, cũng không B» (with nouns 2-01's «không phải là A cũng không phải là B»).
- yaṃ cittaṃ … taṃ … = «Tâm nào …, thì có phải tâm ấy … không?»; yassa yaṃ … = «Ở người nào mà tâm nào …, thì ở người ấy có phải tâm ấy … không?»; moment heads «Vào khoảnh khắc sinh khởi của tâm (cuối cùng), …»; kinds of mind from pi-1 / pi-2.
- Termbase forms kept: asaññasattānaṃ «chúng sinh Vô Tưởng»; nirodhasamāpannānaṃ «những người nhập thành tựu thiền chấm dứt».

### From rails 5-01 (finished 2026-11-22; build_rails_5-01_vi.py, notes-rails-5-01.md): Sacca chapters 5-02, 5-03 import it
- TRUTH / SACCA_A / SACCA_B (pi-2: «sự thật về khổ đau / về sự phát sinh / về sự chấm dứt / về con đường»); bare dukkhaṃ «khổ đau»; Kāyikaṃ dukkhaṃ cetasikaṃ dukkhaṃ «sự khó chịu nơi thân và sự khó chịu trong tâm»; Cattāri saccāni «Bốn sự thật»; PLANES adds apāya «cõi khổ»; heads asserted equal to 9-01's answer_head.
- «ye ca puthujjanā … / ye caññe …» = «những người phàm phu nào … / những người khác nào …» (after a time phrase the group opens with «và ở»); inner tesaṃ «ở những người ấy»; tesaṃ upapajjantānaṃ «khi những người ấy đang tái sinh»; Avasese catuvokāre pañcavokāre «Ở cõi gồm bốn khối và cõi gồm năm khối còn lại» (one place item); maggassa ca phalassa ca «của con đường và thành quả»; notes: vitthāretabbaṃ «nên được trình bày chi tiết» (pi-5), Tantinānākaraṇaṃ «Sự khác biệt trong lời văn».

- From 5-02 (build_rails_5-02_vi.py): «tâm cuối cùng» heads (Pacchimacittassa bhaṅgakkhaṇe = 9-02's answer_head); notes with pi-2 / 2-02 «như đã được phân tích trong …, … cũng nên phân tích như vậy» and pi-5 «không có sự khác biệt»; atītā pucchā «các câu hỏi về quá khứ»; (cetaṃ) na kātabbaṃ «cũng không nên trình bày (điều này: “…”)»; pāṭhantaraṃ «dị bản»; a cut (Kha) without "?" «(b) Còn ở người nào mà… Đúng vậy.».

- From 5-03 (build_rails_5-03_vi.py): aggaphalassa uppādakkhaṇe «vào khoảnh khắc sinh khởi của thành quả tối thượng»; answer cut after the truth «…, thì ở những người ấy, ở nơi ấy sự thật về khổ đau…»; pariññā / pajahati after no ca «vẫn hiểu biết trọn vẹn», «đã từng hiểu biết trọn vẹn», «đã từng dứt bỏ», «vẫn sẽ dứt bỏ»; "…, no ca te B V" «…, nhưng những người ấy vẫn …»; «… cũng nên phân tích như vậy mà không mê lầm» (asammohantena after the verb phrase).

### From rails 9-02 (finished 2026-11-22; build_rails_9-02_vi.py, notes-rails-9-02.md)
- Extends 9-01's head parser: Pacchimacittassa bhaṅgakkhaṇe «vào khoảnh khắc tan rã của tâm cuối cùng» (8's mind_gen_vi); kusalākusalānaṃ bhaṅgakkhaṇe «vào khoảnh khắc tan rã của các hiện tượng thiện và bất thiện» (pi-1 ^1-994); short answers Nirujjhanti. «Có chấm dứt.», Nirujjhittha. «Đã chấm dứt.», Nirujjhissanti. «Sẽ chấm dứt.».

### From rails 6-01 (finished 2026-11-22; build_rails_6-01_vi.py, notes-rails-6-01.md): 6-02 imports it; 10-05 … 10-07, 10-12 align the anantarā groups
- SANKHARA_TABLE (termbase; kāya- / vacī- / cittasaṅkhāra = the Yamaka's own definitions); uddesa «Ba loại tạo tác – …»; vinā «mà không có X» after its noun; jhānas «tầng thiền thứ nhất … thứ tư» (pi-2 / pi-5); samāpannānaṃ «những người đang nhập»; bhūmi «cấp độ …»; labbhati «thì không có “…”».
- anantara_group: «chúng sinh trong cõi dục lạc mà tâm cuối cùng sẽ sinh khởi ngay sau tâm này»; «những người mà tâm cuối cùng không có … sẽ sinh khởi ngay sau tâm này» (the smooth form replacing «Vào tâm mà ngay sau đó …»).
- Open for the consistency pass (keep as is for now, same everywhere): an inner list keeps «và» inside a longer run of groups, giving two «và» («… tầng thiền thứ hai và tầng thiền thứ ba và chúng sinh trong cõi dục lạc»; 3-03 the same).

### From rails 10-01 (finished 2026-11-22; build_rails_10-01_vi.py, notes-rails-10-01.md): Indriya chapters 10-02 … 10-13 import it
- TWENTY_TWO / IND_NAME / INDRIYA members (uddesa = pi-2 ^2-221); ind_mulaka «(Phần dựa trên năng lực mắt)»; bare dukkhaṃ «sự khó chịu»; vīriyaṃ «sự tinh tấn» (pi-1); indriye «các năng lực».
- Avasesaṃ sotaṃ na indriyaṃ. «Phần tai còn lại không phải là năng lực.» (user); «Phần» only for body parts (tai, thân): Avasesā upekkhā «Sự bình thản còn lại …»; Yaṃ sotaṃ indriyaṃ taṃ … «Phần tai nào là năng lực, thì phần tai ấy vừa là tai vừa là năng lực.»; Itthindriyaṃ na itthī, itthindriyaṃ. «Năng lực nữ tính thì không phải là người nữ, mà là năng lực nữ tính.».

- From 10-02 (build_rails_10-02_vi.py; coordinator-confirmed): IND_ATTRS (ñāṇa(sam/vip)payuttānaṃ «(không) gắn liền với hiểu biết»; sahetukānaṃ / ahetukānaṃ «có / không có gốc rễ», pi-2); SEX / sex_vi «… đang tái sinh làm người nữ / người nam» (user), na itthīnaṃ «… đang tái sinh không làm người nữ»; FEEL / feel_vi «… đang tái sinh có niềm vui đi kèm», vinā somanassena «… không có niềm vui đi kèm», after a sex word «làm người nữ, có niềm vui đi kèm»; faculty_mind_gen «tâm gắn liền với niềm vui và không gắn liền với niềm tin»; tāsaṃ «những người ấy», upapajjantīnaṃ «đang tái sinh». Sex / feeling words with cavantānaṃ or a plane are not set yet: the first chapter that meets them sets the shape (sex / feeling word right after the participle, as above) and reports it.

- From 10-03 (build_rails_10-03_vi.py; coordinator-confirmed): na uppajjati «không sinh khởi», after no ca «vẫn sinh khởi», both «A không sinh khởi, B cũng không sinh khởi»; "na itthīnaṃ na purisānaṃ upapajjantānaṃ" «những người đang tái sinh không làm người nữ, cũng không làm người nam»; sex / feeling words after "Sabbesaṃ cavantānaṃ" belong to the next upapajjantānaṃ group («tất cả những người đang chết đi và những người không có mắt đang tái sinh không làm người nữ»).

- From 10-04 (build_rails_10-04_vi.py): member list cut by …pe… with a separate na «… có phải năng lực niềm tin… năng lực trí tuệ… năng lực ý không sinh khởi không?» (split_mv_cut / question11).
- From 7-11 (build_rails_7-11_vi.py): kassaci N anusayā anusenti «ở một số chúng sinh, bảy / năm / ba khuynh hướng tiềm ẩn nằm sẵn»; Numeral + eva «Chỉ có …» (sample Tīṇeva: satteva «chỉ có bảy …»); anusayā bhaṅgā natthi «không có khuynh hướng tiềm ẩn phải phân chia»; heṭṭhā «xuống phía dưới»; upapatti nāma «cái gọi là sự tái sinh».

- From 10-08 (build_rails_10-08_vi.py; coordinator-confirmed): sex word with a plane «những người đang tái sinh vào cõi dục lạc không làm người nữ» (plane after the participle as 3-02, then the sex word as 10-02); upapatticittassa «vào khoảnh khắc sinh khởi / tan rã của tâm tái sinh» (5-01); cut member lists with a mixed-tense separate na «… năng lực ý chưa từng sinh khởi không?». Where setters' head parsers disagree on plane-only heads, follow 10-02 / 3-02; "Suddhāvāse parinibbantānaṃ" «… trong cõi Tịnh Cư» (2-01 / 2-02 / 3-0x).

- From 10-05 (build_rails_10-05_vi.py): ETENEVA «trong chính trạng thái ấy» (user), KATICI_BHAVE «sau khi trải qua một số kiếp sống» (katici «một số», dassetvā «trải qua»); ye_clause12 «Những người nam / nữ / có mắt nào trong chính trạng thái ấy, sau khi trải qua một số kiếp sống, sau khi tái sinh có niềm vui đi kèm, sẽ nhập Niết-bàn trọn vẹn» (commas only in eteneva clauses); ye_head12; anantara_group (= 6-01) «những người mà tâm cuối cùng gắn liền với sự bình thản sẽ sinh khởi ngay sau tâm này»; Suddhāvāsānaṃ upapajjantānaṃ «chúng sinh trong cõi Tịnh Cư đang tái sinh» (one group); saghānakā «có mũi». 10-06, 10-07, 10-12 import it.

- From 10-10 (build_rails_10-10_vi.py; coordinator-accepted): that_mind_moment_x «vào khoảnh khắc tan rã của tâm mà ngay sau đó tâm cuối cùng gắn liền với sự bình thản sẽ sinh khởi» (9-01 shape with 10-05's mind); pacchima_gen «tâm cuối cùng gắn liền với niềm vui», samangi_person «những người có được tâm cuối cùng gắn liền với …»; pacchima_sex_group "Pacchimabhavikānaṃ itthīnaṃ upapajjantīnaṃ" «những người thuộc kiếp sống cuối cùng đang tái sinh làm người nữ»; ye_head: P [P2] + several ye clauses joined flat «A, B, những người nào … và những người nam nào …, khi những người ấy đang chết đi». 10-09, 10-11, 10-12 align to these.

### From rails 9-01 (finished 2026-11-22; build_rails_9-01_vi.py, notes-rails-9-01.md): Dhamma chapters 9-02, 9-03 import it; 6-01 / 6-02 / 10-xx align
- Bare kusalā «những gì là thiện», kusalā dhammā «các hiện tượng thiện»; Kusalaṃ ṭhapetvā «Ngoại trừ hiện tượng thiện»; answer heads joined with «, » as 8: «Ở tất cả chúng sinh, vào khoảnh khắc tan rã của tâm, …», pavatte «trong đời sống», «khi tâm bất thiện thứ hai đang diễn ra» (pi-5); two-part citta «tâm không gắn liền với các hiện tượng thiện và không gắn liền với …».
- yassa cittassa anantarā aggamaggaṃ paṭilabhissanti: as a person group «những người sẽ đạt được con đường tối thượng ngay sau tâm này»; with tassa cittassa + a moment «vào khoảnh khắc … của tâm mà ngay sau đó sẽ đạt được con đường tối thượng». 6-01 / 6-02 / 10-xx (the anantarā phrases, user: smooth, meaning unchanged) align to this shape.
- Unlabelled cut "Yattha …ti?…Pe…." = «… không?…»; dutiye «thứ hai»; arahantānaṃ in a list «các bậc A-la-hán» (pi-5).

### From rails 3-01 (finished 2026-11-22; build_rails_3-01_vi.py, notes-rails-3-01.md): Āyatana chapters 3-02 … 3-06 import it
- AYATANA / TWELVE / AY_NAME (pi-1 names «lĩnh vực mắt … lĩnh vực đối tượng của ý»); AY_SPECIAL («hiểu theo nghĩa …» with pi-5 «thiên nhãn / mắt trí tuệ / thiên nhĩ»); AY_ATTRS + ATTR_JOIN: attribute beings «những người có mắt, không có tai đang tái sinh» (any chapter with sa- / a-cakkhuka, sa- / a-sotaka, saghānaka … attributes copies this shape); PLANES_AY (rūpāvacara / kāmāvacara / arūpāvacara); mulaka_label «(Phần dựa trên lĩnh vực mắt)»; NOTES_AY editorial notes (-tabbaṃ «nên …», asammohantena «mà không mê lầm», sabbattha «ở mọi chỗ»); double variant «[dị bản (Syā.): X; (Sī., Ka.): Y]» (pi-2).
- Gaps chosen: dhammo «hiện tượng»; saṃkhittaṃ (of the text) «tóm lược»; sarūpakānaṃ / saghānakānaṃ / aghānakānaṃ from siblings; bandhitabbaṃ, Ekekapadamūlakaṃ, ekasadisaṃ, atirekaṃ kātabbaṃ: see the notes; copy them.

- From 3-02 (build_rails_3-02_vi.py): attributes with planes «những người không có mắt đang tái sinh vào cõi dục lạc»; Ye heads «Những người nào sau khi tái sinh vào cõi hình sắc sẽ nhập Niết-bàn trọn vẹn, thì ở những người ấy …»; nested runs of beings joined flat «A, B và C» (never «A và B và C»; 10-07 has the same Pāli); sadisaṃ «giống nhau», ime dve «hai điều này», eva «đúng là». Helpers ay_group / ay_persons / ye_ca_head / answer_head / sadisa_note for 3-03 … 3-06.
- From 3-03 (build_rails_3-03_vi.py): "… parinibbāyissanti tesaṃ upapajjantānaṃ" «…, khi những người ấy đang tái sinh»; several person groups before "ye ca" joined flat «Ở A, B và những người nào …»; a pair question cut before its last verb «(b) Còn ở người nào[, ở nơi nào] mà[ X]… đã sinh khởi không?»; "Uppādavāro." «Mục về sự sinh khởi.». Page-number debris (e.g. «=93») is dropped.
- From 3-04 (build_rails_3-04_vi.py): both-frame with a separate na «A không chấm dứt, B cũng không chấm dứt»; cut question with no verb «(b) Còn ở người nào, ở nơi nào mà… không?»; answers cut after the person head «Ở chúng sinh trong cõi hình sắc… ở chúng sinh trong cõi dục lạc…»; sadisaṃ with one subject «giống như vậy»; vitthāritā «đã được trình bày chi tiết»; uppāde / nirodhe «ở sự sinh khởi» / «ở sự chấm dứt».
- From 3-05 (build_rails_3-05_vi.py): cut_q_dot «(b) Còn ở người nào[, ở nơi nào] mà X…» (no "?"); loc_fragment / frag_line «Ở …, thì ở những người ấy[, ở nơi ấy]…»; notes: tividhaṃ «theo ba cách», idampi «phần này … cũng», "yatthakaṃ noti na kātabbaṃ" «ở phần về nơi chốn không nên trả lời là “Không”», tīsupi vāresu «ở cả ba mục», itaresaṃ yatthakānaṃ «các phần về nơi chốn khác».
- From 4 (build_rails_4_vi.py): eighteen dhātu names and «Mười tám yếu tố –» (pi-2 ^2-183); bare cut questions «<X> không?» / «Những gì không phải là <X>, có phải không?»; «Ngoại trừ X, các yếu tố còn lại không phải là Y.»; notes: aññehi yamakehi saṃsanditabbaṃ «nên đối chiếu với các phần cặp câu hỏi khác», sadisaṃ kātabbaṃ «nên được làm cho giống nhau», ubhato «ở cả hai chiều», bandhitaṃ «đã được nối kết»; yamaka titles inside notes in “…”.

### From rails 2-02 (finished 2026-11-22; build_rails_2-02_vi.py, notes-rails-2-02.md): family E (pariññā) and B additions
- Every chapter with a pariññāvāra (3-06, 5-03, 7-07, 7-08, 10-13 …) imports build_rails_2-02_vi (make_verbs / rows_na / rows_fused; PERSONS.extended): yo … so …ti? = 7-03's shell «Người nào mà V A, thì người ấy có phải V B không?»; tenses «V / không V», «đã V / chưa từng V», «sẽ V / sẽ không V» (= 2-01 VERB_TABLE); after no ca: negative «vẫn V / đã từng V / vẫn sẽ V», positive «không V B, cũng không V C»; both «V1 A, cũng V2 B»; Ye maggaṃ paṭilabhissanti «Những người nào sẽ đạt được con đường, thì những người ấy»; maggaṃ na paṭilabhissanti «sẽ không đạt được con đường»; avasesā puggalā «những hạng người còn lại»; paripuṇṇaṃ kātabbaṃ «nên được trình bày đầy đủ»; the (Yathā …) note = pi-2 «như đã được phân tích trong …, ở đây cũng nên phân tích như vậy»; "P ye ca … parinibbāyissanti tesaṃ cavantānaṃ" head with «, khi những người ấy đang chết đi».
- Denied negative list «vẫn V B và C» (by analogy with «A và B vẫn V»).

- Anusaya chapters 7-02 … 7-11: import build_rails_7-01_vi; its FAMILY_TERMS and the frames above cover the person / place / verb forms; handle "…pe…" cuts in your own builder.
