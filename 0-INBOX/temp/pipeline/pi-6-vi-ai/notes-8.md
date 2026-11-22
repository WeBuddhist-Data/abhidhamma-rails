# notes-8: family D frames (Cittayamaka), set by 8-cittayamaka.md

Builder: build_8_vi.py (`sys.path.insert(0, r"…\pi-6-vi-ai"); import build_8_vi as C`; importing writes nothing).
Every frame below is a constant or helper there (name in brackets). Later chapters with the same Pāli (Dhammayamaka 9-xx, Indriyayamaka 10-xx where they have uppajjamāna / uppanna sections) copy them verbatim.
Format: Pāli = tiếng Việt. [pi-N] = from the approved pi-N Vietnamese rails (asserted by the builder); [sample] = build_sample_vi; [7-01] / [2-01] = aligned with those frame-setters (coordinator rules); [new] = set here.
Labels: always build_sample_vi.LABEL.

## Tense / aspect (VERB, NEGVERB, DENIED): every form has its own Vietnamese
uppajjati = sinh khởi; na uppajjati = không sinh khởi [pi-5; 2-01]  (present: the citta is at its arising moment)
nirujjhati = chấm dứt; na nirujjhati = không chấm dứt [pi-5; 2-01]
uppajjittha = đã sinh khởi; na uppajjittha = chưa từng sinh khởi [2-01]  (past: it arose before)
nirujjhittha = đã chấm dứt; na nirujjhittha = chưa từng chấm dứt [2-01]
uppajjissati = sẽ sinh khởi; na uppajjissati = sẽ không sinh khởi [pi-5; 2-01]  (future)
nirujjhissati = sẽ chấm dứt; na nirujjhissati = sẽ không chấm dứt [2-01]
uppajjamānaṃ = đang sinh khởi; na uppajjamānaṃ = không đang sinh khởi [new; pi-5 vimuccamāna «đang được giải thoát»]  (present participle: in the course of arising)
nirujjhamānaṃ = đang chấm dứt; na nirujjhamānaṃ = không đang chấm dứt [new]
uppannaṃ = ở trạng thái đã sinh khởi; na uppannaṃ = không ở trạng thái đã sinh khởi [new]  (past participle = arisen and not yet ceased, aṭṭhakathā ^6-163 «uppādaṃ patvā aniruddha»; kept apart from uppajjittha «đã sinh khởi»; pi-5 has plain «đã sinh khởi» in other contexts)
niruddhaṃ = ở trạng thái đã chấm dứt; na niruddhaṃ = không ở trạng thái đã chấm dứt [new; symmetric with uppanna]
X na Y (two predicates in one clause) = X nhưng Y-neg: uppajjati na nirujjhati = sinh khởi nhưng không chấm dứt; na uppajjati nirujjhati = không sinh khởi nhưng chấm dứt [new JOIN; not «mà», which the person frame already uses]
no ca … + positive = the negative form: no ca tesaṃ cittaṃ uppajjati = nhưng ở những người ấy tâm không sinh khởi [7-01 / 2-01]
no ca … + na X = said plainly with «vẫn»: … na uppannaṃ = … vẫn ở trạng thái đã sinh khởi; … na uppajjissati = … vẫn sẽ sinh khởi; … na uppajjamānaṃ = … vẫn đang sinh khởi; past: … na uppajjittha = … đã từng sinh khởi (= 2-01 DENY_NEG) [7-01 / 2-01]
Uppajjati. / Nirujjhati. (answer) = Có sinh khởi. / Có chấm dứt. [2-01 SHORT]
Uppajjittha. / Nirujjhittha. / Uppajjissati. / Nirujjhissati. = Đã sinh khởi. / Đã chấm dứt. / Sẽ sinh khởi. / Sẽ chấm dứt. [2-01]
Uppannaṃ. (answer) = Ở trạng thái đã sinh khởi. [new]
Āmantā. = Đúng vậy. [sample]; No. = Không. [7-01]; Natthi. = Không có. [pi-3, 7-01]

## Question frames (WHO, Q, Q_NOCA, Q_SHORT, Q_ATI, question(), translate_question())
(Ka) yassa cittaṃ A tassa cittaṃ B(ti)? = (a) Ở người nào mà tâm <A>, thì ở người ấy có phải tâm <B> không? [7-01 shape]
(Kha) yassa vā pana cittaṃ A tassa cittaṃ B(ti)? = (b) Còn ở người nào mà tâm <A>, thì ở người ấy có phải tâm <B> không? [7-01]
(Ka) yaṃ cittaṃ A taṃ cittaṃ B(ti)? = (a) Tâm nào <A>, thì có phải tâm ấy <B> không? [new]
(Kha) yaṃ vā pana cittaṃ A taṃ cittaṃ B(ti)? = (b) Còn tâm nào <A>, thì có phải tâm ấy <B> không? [new]
(Ka) yassa yaṃ cittaṃ A tassa taṃ cittaṃ B(ti)? = (a) Ở người nào mà tâm nào <A>, thì ở người ấy có phải tâm ấy <B> không? [new]
(Kha) yassa vā pana yaṃ cittaṃ A tassa taṃ cittaṃ B(ti)? = (b) Còn ở người nào mà tâm nào <A>, thì ở người ấy có phải tâm ấy <B> không? [new]
yassa K cittaṃ … tassa K cittaṃ … = Ở người nào mà tâm <K> …, thì ở người ấy có phải tâm <K> … không? [new; K = citta kind below]
(11) yassa cittaṃ A no ca tassa cittaṃ N, tassa cittaṃ B(ti)? = Ở người nào mà tâm <A>, nhưng ở người ấy tâm <denied N>, thì ở người ấy có phải tâm <B> không? (D: «Tâm nào <A>, nhưng tâm ấy <denied N>, thì có phải tâm ấy <B> không?»; PD: «…, nhưng ở người ấy tâm ấy …») [new Q_NOCA]
(12)/(13) (Ka) A B(ti)? = (a) Cái <A> thì có phải <B> không? (uppannaṃ uppajjamānaṃ? = Cái ở trạng thái đã sinh khởi thì có phải đang sinh khởi không?) [new Q_SHORT]
(14) yassa cittaṃ M1 khaṇaṃ khaṇaṃ vītikkantaṃ atikkantakālaṃ, M2 khaṇaṃ khaṇaṃ vītikkantaṃ atikkantakālaṃ tassa cittaṃ(ti)? = Ở người nào mà tâm, về <M1>, đã vượt qua khoảnh khắc ấy và thời của nó đã qua, về <M2>, đã vượt qua khoảnh khắc ấy và thời của nó đã qua, thì ở người ấy tâm có như vậy không? (D: «Tâm nào, …, thì tâm ấy có như vậy không?»; PD: «Ở người nào mà tâm nào, …, thì ở người ấy tâm ấy có như vậy không?») [new Q_ATI, ATI]
na M khaṇaṃ khaṇaṃ vītikkantaṃ atikkantakālaṃ = về <M>, không phải là đã vượt qua khoảnh khắc ấy và thời của nó đã qua [new ATI_NEG: one «na» over the whole phrase]
uppajjamānaṃ khaṇaṃ / nirujjhamānaṃ khaṇaṃ = khoảnh khắc đang sinh khởi / khoảnh khắc đang chấm dứt [new MOMENT_M; aṭṭhakathā ^6-165 = uppādakkhaṇa / nirodhakkhaṇa]
atikkantakāla = thời của nó đã qua; vītikkanta / avītikkanta = đã vượt qua / chưa vượt qua [new]

## Answer frames (P_ANS, D_ANS, PRED_*, pred(), translate_answer())
puggalavāra: G tesaṃ [K] cittaṃ P. = <G>, thì ở những người ấy tâm [K] <P>. [2-01 / 7-01 STATEMENT_RES]
dhammavāra / puggaladhammavāra: S cittaṃ P. = <S> thì <P>. [sample «thì»]
(12)/(13) without cittaṃ: Bhaṅgakkhaṇe P. / Uppādakkhaṇe P. = Vào khoảnh khắc tan rã thì <P>. / Vào khoảnh khắc sinh khởi thì <P>. [new]
P: A, no ca R B = <A>, nhưng <R> <denied B> (R: tesaṃ cittaṃ = ở những người ấy tâm; taṃ cittaṃ = tâm ấy; tassa taṃ cittaṃ = ở người ấy tâm ấy; none = —) [7-01 / 2-01]
P: Añceva Bñca / A ceva B ca = vừa <A> vừa <B> [sample BOTH]
P: na ceva A na ca B = <not A>, cũng <not B> [new]
P: A na B, C na D = <A nhưng không B>, <C nhưng không D>; A na B, C ceva D ca = <A nhưng không B>, vừa <C> vừa <D> [new]
Itaresaṃ Kcittassa uppādakkhaṇe tesaṃ…pe…. = Ở những người khác, vào khoảnh khắc sinh khởi của tâm <K>, thì ở những người ấy… [new]
Yassa vā pana…pe…? Āmantā …pe…. = Còn ở người nào…? Đúng vậy… [new; 7-04 «Đúng vậy…»]

## Answer subjects (P_SUBJ, D_SUBJ, BARE_SUBJ, when(), for_())
uppādakkhaṇa / bhaṅgakkhaṇa = khoảnh khắc sinh khởi / khoảnh khắc tan rã [pi-5]
Cittassa uppādakkhaṇe / bhaṅgakkhaṇe = Vào khoảnh khắc sinh khởi / tan rã của tâm [new AT, OF]
Pacchimacittassa uppādakkhaṇe = Vào khoảnh khắc sinh khởi của tâm cuối cùng [new; pacchima «cuối cùng»]
Sarāgapacchimacittassa / Pacchimakusalacittassa uppādakkhaṇe = Vào khoảnh khắc sinh khởi của tâm có tham đắm cuối cùng / của tâm thiện cuối cùng [new]
Itaresaṃ = Ở những người khác [2-01 itaresaṃ «những người khác»]; Itaresaṃ cittassa uppādakkhaṇe = Ở những người khác, vào khoảnh khắc sinh khởi của tâm [new]
Nirodhasamāpannānaṃ asaññasattānaṃ = Ở những người nhập thành tựu thiền chấm dứt, chúng sinh Vô Tưởng [pi-5 «thành tựu thiền chấm dứt», «chúng sinh Vô Tưởng»; 2-01 WHO_HEAD / LIST_SEP]
Cittassa bhaṅgakkhaṇe nirodhasamāpannānaṃ asaññasattānaṃ = Vào khoảnh khắc tan rã của tâm, ở những người nhập thành tựu thiền chấm dứt, chúng sinh Vô Tưởng [new]
Cittasamaṅgīnaṃ / Pacchimacittasamaṅgīnaṃ / Itaresaṃ cittasamaṅgīnaṃ = Ở những người có được tâm / … có được tâm cuối cùng / Ở những người khác có được tâm [pi-5 samaṅgī «người có được»]
tesaṃ (resumptive) = ở những người ấy [7-01]
Bhaṅgakkhaṇe cittaṃ / Uppādakkhaṇe cittaṃ = Tâm vào khoảnh khắc tan rã / Tâm vào khoảnh khắc sinh khởi [new]
Atītaṃ / Anāgataṃ / Paccuppannaṃ cittaṃ = Tâm thuộc quá khứ / thuộc tương lai / thuộc hiện tại [pi-1 matrix]
Atītānāgataṃ cittaṃ = Tâm thuộc quá khứ và tương lai [new]
Uppādakkhaṇe anāgatañca cittaṃ = Tâm vào khoảnh khắc sinh khởi và tâm thuộc tương lai [new; aṭṭhakathā ^6-164: two cittas]; Bhaṅgakkhaṇe anāgatañca / atītañca cittaṃ = Tâm vào khoảnh khắc tan rã và tâm thuộc tương lai / … thuộc quá khứ
Uppādakkhaṇe anāgataṃ cittaṃ. (no ca) = Tâm vào khoảnh khắc sinh khởi, tâm thuộc tương lai. [new]

## Citta kinds (KIND, citta())
citta = tâm [pi-1 core]
sarāgaṃ / vītarāgaṃ / sadosaṃ / vītadosaṃ / samohaṃ / vītamohaṃ cittaṃ = tâm có tham đắm / đã lìa tham đắm / có sân hận / đã lìa sân hận / có si mê / đã lìa si mê [pi-2]
saṃkhittaṃ / vikkhittaṃ / mahaggataṃ / amahaggataṃ cittaṃ = tâm co rút / tán loạn / rộng lớn / không rộng lớn [pi-2]
sauttaraṃ / anuttaraṃ cittaṃ = tâm còn có điều cao hơn / không có điều gì cao hơn [pi-2]
samāhitaṃ / asamāhitaṃ / vimuttaṃ / avimuttaṃ cittaṃ = tâm được định tâm / không được định tâm / được giải thoát / không được giải thoát [pi-2]
kusalaṃ / akusalaṃ / abyākataṃ cittaṃ = tâm thiện / bất thiện / không xác định về mặt đạo đức [pi-1]
sukhāya vedanāya sampayuttaṃ cittaṃ = tâm gắn liền với cảm giác dễ chịu [pi-1 matrix]
saraṇa / araṇa (cittaṃ) = (tâm) có xung đột / không có xung đột [pi-1 matrix]; saraṇaaraṇā = các loại có xung đột và không có xung đột [new]

## Headings (HEAD, TIME_SECTION, GREAT_SECTION, MISSAKA)
Cittayamakaṃ = Các cặp câu hỏi về tâm [sample]
Suddhacittasāmaññaṃ / Suddhacittasāmañña = Tâm thuần túy nói chung [new; suddha pi-5]
Puggalavāro / Dhammavāro / Puggaladhammavāro = Mục về người / Mục về hiện tượng / Mục về người và hiện tượng [new]
(1) Uppādanirodhakālasambhedavāro = (1) Mục về sự kết hợp các thời của sự sinh khởi và sự chấm dứt [new]
(2) Uppāduppannavāro = (2) Mục về sự sinh khởi và trạng thái đã sinh khởi [new]
(3) Nirodhuppannavāro = (3) Mục về sự chấm dứt và trạng thái đã sinh khởi [new]
(4) Uppādavāro = (4) Mục về sự sinh khởi [sample SECTION]
(5) Nirodhavāro = (5) Mục về sự chấm dứt [sample SECTION]
(6) Uppādanirodhavāro = (6) Mục về sự sinh khởi và sự chấm dứt [sample SECTION]
(7) Uppajjamāna-nanirodhavāro / Uppajjamānananirodhavāro = (7) Mục về trạng thái đang sinh khởi và sự không chấm dứt [new; hyphen spelling only]
(8) Uppajjamānuppannavāro = (8) Mục về trạng thái đang sinh khởi và trạng thái đã sinh khởi [new]
(9) Nirujjhamānuppannavāro = (9) Mục về trạng thái đang chấm dứt và trạng thái đã sinh khởi [new]
(10) Uppannuppādavāro = (10) Mục về trạng thái đã sinh khởi và sự sinh khởi [new]
(11) Atītānāgatavāro = (11) Mục về quá khứ và tương lai [sample SECTION]
(12) Uppannuppajjamānavāro = (12) Mục về trạng thái đã sinh khởi và trạng thái đang sinh khởi [new]
(13) Niruddhanirujjhamānavāro = (13) Mục về trạng thái đã chấm dứt và trạng thái đang chấm dứt [new]
(14) Atikkantakālavāro = (14) Mục về thời đã qua [new]
Suttantacittamissakaviseso = Trường hợp đặc biệt kết hợp với các loại tâm theo kinh [new; «theo kinh» pi-1 / pi-2]
Abhidhammacittamissakaviseso = Trường hợp đặc biệt kết hợp với các loại tâm theo Vi Diệu Pháp [new; «theo Vi Diệu Pháp» pi-2]

## Editorial lines and closing
(Etena upāyena yāva saraṇaaraṇā uddharitabbā.) = (Theo cách này, cần trình bày cho đến các loại có xung đột và không có xung đột.) [new]
(Yassa cittake sakabhāvena niddiṭṭhe, yaṃ cittake ca yassa yaṃ cittake ca ekattena niddiṭṭhe.) = (Phần về tâm ở người nào được giải thích theo cách riêng của nó, phần về tâm nào và phần về tâm nào ở người nào được giải thích chung làm một.) [new]
(Mūlayamakaṃ cittayamakaṃ dhammayamakanti tīṇi yamakāni yāva saraṇaaraṇā gacchanti.) = (Ba phần, các cặp câu hỏi về gốc rễ, các cặp câu hỏi về tâm và các cặp câu hỏi về các hiện tượng, đều đi cho đến các loại có xung đột và không có xung đột.) [new]
Cittayamakaṃ niṭṭhitaṃ. = Phần các cặp câu hỏi về tâm đã hoàn tất. [sample yamaka_end]

## Source points in 8 (translated as written)
^6-8-83 «vītakkantaṃ» = vītikkantaṃ (spelling slip; ^6-8-104 has vītikkantaṃ), rendered «đã vượt qua».
^6-8-82 «(14) Atikkantakālavāro» is a plain line (no #####) inside the segment, unlike the other section titles; kept plain.
^6-8-61 «uppajjati …» has a space before «…»; rendered «…» without the space. ^6-8-115 «Āmantā …pe….» likewise «Đúng vậy…».
Uddesa heading (7) «Uppajjamāna-nanirodhavāro» vs niddesa «Uppajjamānananirodhavāro»: hyphen only, same Vietnamese.
Section (7) is titled uppajjamāna but its questions use uppajjati; the Vietnamese keeps «đang sinh khởi» in the title and «sinh khởi» in the questions, as the Pāli does.
