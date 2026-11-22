# notes-map-8: 8-cittayamaka keyword map (frame-setter: aspect forms, moments, citta kinds)

Script: map_8_vi.py (importing builds nothing; load with importlib). Named tables for later chapters: TENSE, TENSE_NEG, TENSE_FORMS, VERBS, ASPECT, ASPECT_NOUN, MOMENT, TIME, KIND, FEELING, PERSONS8, HEAD8, TITLE_RUNNING; helpers norm, polarity, tense_value, aspect_value, citta_value, moment_value, time_value, vara_value, value8.
Result: 205 lines, bad [], 6 (no direct equivalent), presence misses 0, no exceptions.

## Tense (shared with 2-01; same rule as map_2-01_vi.VERB_FORMS: polarity of the keyword's first occurrence in the Pāli)
uppajjati / uppajjatīti = sinh khởi
uppajjittha / uppajjitthāti = đã sinh khởi (after a separate na: chưa từng sinh khởi; denied na in «no ca»: đã từng sinh khởi)
uppajjissati / uppajjissatīti = sẽ sinh khởi; after a separate na = sẽ … sinh khởi («sẽ không sinh khởi»: «không» belongs to na)
nirujjhati / nirujjhatīti = chấm dứt
nirujjhittha / nirujjhitthāti = đã chấm dứt
nirujjhissati / nirujjhissatīti = sẽ chấm dứt; after a separate na = sẽ … chấm dứt
«no ca» clause ends at a comma as well as at . ? ! (question (11): «… no ca tassa cittaṃ uppannaṃ, tassa cittaṃ uppajjissatīti?» = plain sẽ sinh khởi); checked: map_2-01_vi.verb_value gives the same value for all 257 tense keywords of 8

## Aspect forms (participles; any case, -ti, -ñca, -ñceva dropped)
uppajjamānaṃ / uppajjamānanti / uppajjamānañca = đang sinh khởi
nirujjhamānaṃ / nirujjhamānanti / nirujjhamānañca = đang chấm dứt
uppannaṃ / uppannanti / uppannañca / uppannañceva = ở trạng thái đã sinh khởi (ASPECT second candidate đã sinh khởi for texts without «ở trạng thái»)
niruddhaṃ / niruddhanti = ở trạng thái đã chấm dứt
first occurrence = denied negative of a «no ca» clause: vẫn + the value (not met in 8)
heading members (bare stem) = the noun: Uppajjamāna = trạng thái đang sinh khởi (ASPECT_NOUN: trạng thái đang chấm dứt / trạng thái đã sinh khởi / trạng thái đã chấm dứt; uppāda sự sinh khởi, nirodha sự chấm dứt, nanirodha sự không chấm dứt)

## Moments and time of the citta («Vào» of the locative is frame)
uppādakkhaṇe / Uppādakkhaṇe / uppādakkhaṇaṃ / uppādakkhaṇañca = khoảnh khắc sinh khởi
bhaṅgakkhaṇe / Bhaṅgakkhaṇe / bhaṅgakkhaṇaṃ / bhaṅgakkhaṇañca = khoảnh khắc tan rã
khaṇaṃ = khoảnh khắc (uppajjamānaṃ khaṇaṃ «khoảnh khắc đang sinh khởi»: uppajjamānaṃ = đang sinh khởi)
Cittassa uppādakkhaṇe / cittassa uppādakkhaṇe = khoảnh khắc sinh khởi của tâm
Cittassa bhaṅgakkhaṇe / cittassa bhaṅgakkhaṇe = khoảnh khắc tan rã của tâm
Pacchimacittassa uppādakkhaṇe / bhaṅgakkhaṇe = khoảnh khắc sinh khởi / tan rã của tâm cuối cùng
Sarāgapacchimacittassa uppādakkhaṇe = khoảnh khắc sinh khởi của tâm có tham đắm cuối cùng
sarāgacittassa uppādakkhaṇe = khoảnh khắc sinh khởi của tâm có tham đắm
Pacchimacittassa = tâm cuối cùng; Pacchimakusalacittassa = tâm thiện cuối cùng; kusalacittassa = tâm thiện
Atītaṃ / atītaṃ / atītañca = thuộc quá khứ; Anāgataṃ / anāgataṃ / anāgatañca = thuộc tương lai; Paccuppannaṃ = thuộc hiện tại; Atītānāgataṃ = thuộc quá khứ và tương lai
atikkantakāla = thời của nó đã qua; vītikkanta / avītikkanta = đã vượt qua / chưa vượt qua (tables only: not keywords in 8)

## Persons and beings («Ở» and the leading «những» are frame)
Itaresaṃ = người khác (= map_2-01_vi PERSONS itaresaṃ)
Nirodhasamāpannānaṃ / nirodhasamāpannānaṃ = người nhập thành tựu thiền chấm dứt
Cittasamaṅgīnaṃ = người có được tâm; Pacchimacittasamaṅgīnaṃ = người có được tâm cuối cùng
cittasamaṅgīnaṃ right after Itaresaṃ («Ở những người khác có được tâm», ^6-8-79) = có được tâm (the head «người» goes to Itaresaṃ, as 2-01 Itaresaṃ <P>ānaṃ)
asaññasattānaṃ = chúng sinh Vô Tưởng (sample FORMULAS)

## Citta kinds (KIND; «tâm <K>»)
sarāgaṃ có tham đắm, vītarāgaṃ đã lìa tham đắm, sadosaṃ có sân hận, samohaṃ có si mê, saṃkhittaṃ co rút, vikkhittaṃ tán loạn, mahaggataṃ rộng lớn, amahaggataṃ không rộng lớn, sauttaraṃ còn có điều cao hơn, anuttaraṃ không có điều gì cao hơn (not the pi-5 chain «vô thượng»), samāhitaṃ được định tâm, asamāhitaṃ không được định tâm, vimuttaṃ được giải thoát, avimuttaṃ không được giải thoát, araṇaṃ không có xung đột
kusalaṃ cittaṃ = tâm thiện; akusalaṃ cittaṃ = tâm bất thiện; abyākataṃ cittaṃ = tâm không xác định về mặt đạo đức
sukhāya vedanāya sampayuttaṃ: sampayuttaṃ = gắn liền, vedanāya = cảm giác
saraṇaaraṇā = loại có xung đột và không có xung đột («các loại …»: leading «các» dropped, classifier kept)
cittaṃ / cittanti / cittake = tâm

## Headings and editorial lines
Cittayamakaṃ (heading) = Các cặp câu hỏi về tâm; inside the closing parenthesis cittayamakaṃ = các cặp câu hỏi về tâm, Mūlayamakaṃ = các cặp câu hỏi về gốc rễ, dhammayamakanti = các cặp câu hỏi về các hiện tượng (lower case as written); yamakāni = phần («Ba phần»)
Suddhacittasāmaññaṃ / Suddhacittasāmañña = tâm thuần túy nói chung
Puggalavāro = mục về người; Dhammavāro = mục về hiện tượng (not the chain's «mục về các hiện tượng»); Puggaladhammavāro = mục về người và hiện tượng
Uppādanirodhakālasambhedavāro = mục về sự kết hợp các thời của sự sinh khởi và sự chấm dứt
<A><B>vāro (vara_value) = mục về <A noun> và <B noun>: Uppāduppannavāro, Nirodhuppannavāro, Uppajjamānuppannavāro, Nirujjhamānuppannavāro, Uppannuppādavāro, Uppannuppajjamānavāro, Niruddhanirujjhamānavāro, Uppajjamānananirodhavāro (= mục về trạng thái đang sinh khởi và sự không chấm dứt)
Uppajjamāna-nanirodhavāro split into two keywords: Uppajjamāna = trạng thái đang sinh khởi, nanirodhavāro = mục về … sự không chấm dứt
Atikkantakālavāro = mục về thời đã qua
Suttantacittamissakaviseso = trường hợp đặc biệt kết hợp với các loại tâm theo kinh; Abhidhammacittamissakaviseso = … theo Vi Diệu Pháp

## (no direct equivalent)
6: the placeholder keyword «(no direct equivalent)» itself (^6-8-7-15-0, 7-16-0, 14-6-0, 14-7-0, ^6-8-62, ^6-8-115) = (no direct equivalent) (coordinator rule).

## CROSSCHECK
uppajjissati / uppajjissatīti: «sẽ sinh khởi» (19 + 10) vs «sẽ … sinh khởi» (12 + 5) by the first-occurrence rule; identical formulaic segments agree (^6-8-1 / 21 / 41; ^6-8-84 / 105).
nirujjhissati: «sẽ chấm dứt» (28) vs «sẽ … chấm dứt» (3: ^6-8-70, 71, 74).
uppannaṃ = «ở trạng thái đã sinh khởi» here vs pi-2 / 2-01 «đã sinh khởi» (the 8-cittayamaka text keeps «ở trạng thái»).
Atītaṃ / Anāgataṃ = «thuộc quá khứ» / «thuộc tương lai» (pi-2), not the pi-5 chain's bare «quá khứ» / «tương lai».
