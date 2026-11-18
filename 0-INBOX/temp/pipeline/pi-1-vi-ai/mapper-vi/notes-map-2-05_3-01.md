# Notes: Pāli→Vietnamese keyword map, pi-1 parts 2-05 and 3-01 (new recurring decisions)

Script: map_2-05_3-01_vi.py. 2-05: OVERRIDES → context05() → the 2-04 / 2-02-2-03 context() → T05 (= the 2-04 table + ADD05, new keys only) via ch2_value. 3-01: OVERRIDES → ADD301 (= PRED301 + MEVA + headings) → MATRIX → T05 via ch2_value. Imports map_2-04_vi.py (which imports map_2-02_2-03_vi.py); importing writes nothing (earlier mapped files checked unchanged). Review helper: probe_2-05_3-01_vi.py.
2-05: 99 lines, `bad []`, 0 presence misses, 49 (no direct equivalent) = caya (fragment of apacaya, as 2-03). 3-01: 21 lines, `bad []`, 0 presence misses, 0 NDE.

## 2-05: headings and closing lines
suññataṃ / appaṇihitaṃ in the headings Suddhikasuññataṃ / Suddhikaappaṇihitaṃ (1-1-8-2-0, 1-1-8-4-0, closing 1-513) = sự trống rỗng / sự không mong cầu (as 2-03 CAPS); the body qualifier stays tính chất trống rỗng / tính chất không mong cầu
Suddhikaappaṇihitaṃ = sự không mong cầu đơn thuần; suññatā (Chandādhipateyyasuddhikasuññatā) = sự trống rỗng; adhipateyya / adhipateyyanti = làm yếu tố chủ đạo
abyākataṃ (headings Akusalavipākaabyākataṃ / Ahetukakiriyāabyākataṃ) = loại không xác định về mặt đạo đức (classifier kept, as parittāni = loại hạn hẹp); vipākaabyākataṃ = loại không xác định về mặt đạo đức là quả của nghiệp; kiriyāabyākataṃ = loại không xác định về mặt đạo đức mang tính chức năng
kiriyā abyākatā / Kiriyā abyākatā (closing «Các loại …, mang tính chức năng») = loại không xác định về mặt đạo đức mang tính chức năng; Vipākā abyākatā = quả của nghiệp không xác định về mặt đạo đức («Các» and comma dropped; as 2-04 Abyākatavipāko)
kiriyā / Kiriyā / kiriyaṃ = mang tính chức năng (the 2-03 table «làm» is the fragment of akiriyā: overridden in 2-05 by context05)
kiriyā = chức năng in «Tâm chức năng …» (Sahetuka-/Rūpāvacara-/Arūpāvacarakiriyā: 1-1-10-4/5/6-0, 1-578, 1-582; «tâm» implied, as 2-04 akusalāni = bất thiện)
Kiriyā(-)mano = ý mang tính chức năng («Yếu tố ý mang tính chức năng»); ý … mang tính chức năng where the Vietnamese has «ý thức mang tính chức năng» (1-1-10-2/3-0, 1-573, 1-575)
Kiriyā(-)manodhātu = yếu tố ý mang tính chức năng; Kiriyā(-)manoviññāṇa = ý thức mang tính chức năng; Kiriyā(-)manoviññāṇadhātu = yếu tố ý thức mang tính chức năng
dhātu(-)somanassasahagatā = yếu tố … có niềm vui đi kèm; manoviññāṇadhātu(-)somanassasahagatā = yếu tố ý thức … có niềm vui đi kèm (upekkhā- the same with «có sự bình thản đi kèm»)
hetuka / hetukā = có gốc rễ (Ahetuka- «không có gốc rễ»: fragment = the positive phrase; Sahetuka- «có gốc rễ»)
niṭṭhitaṃ = đã hoàn tất; Citta = tâm (Cittuppādakaṇḍaṃ niṭṭhitaṃ)

## 2-05: world-transcending results
bhāvitattā = tu tập («đã được tạo và tu tập»; katattā = đã được tạo)
kusalassa jhānassa = tầng thiền thiện; lokuttarassa kusalassa = thiện vượt thế gian; lokuttarassa kusalassa jhānassa = tầng thiền thiện vượt thế gian
animittaṃ = tính chất không có dấu hiệu (qualifier, as suññataṃ / appaṇihitaṃ)
X-nti (suññatanti, animittanti, appaṇihitanti, abhiññanti, dandhābhiññanti, adhipateyyanti) = the value of X (the quotation -nti has no word; «(thiện)» / «(quả của nghiệp)» belong to kusalaṃ / vipāko)
kusalaṃ in «…nti kusalaṃ» = thiện («(thiện)»)
aññātāvī = người đã hiểu biết trọn vẹn; aññā = hiểu biết trọn vẹn (2-03)
sati = tỉnh thức (SATI_BARE) in 1-528 / 1-552 (only inside «sự thiết lập tỉnh thức», as 2-03 1-357)

## 2-05: results of the unwholesome, functional minds
akusalassa = bất thiện; akusalassa kammassa = nghiệp bất thiện
dukkhindriyaṃ = năng lực khó chịu; dukkha = khó chịu where dukkhindriyaṃ is in the segment (1-556, 1-560; elsewhere khó khăn of dukkhapaṭipadaṃ)
dukkhaṃ = khó chịu in the bodily feeling string (segments with dukkhā vedanā: «sự khó chịu nơi thân», «cảm nhận bứt rứt và khó chịu»); sự đau khổ in the heading 1-559 («sự đau khổ là gì?», as 2-04 1-416)
kāyasamphassa = sự tiếp xúc của thân; samphassa = sự tiếp xúc
kammavipākā / kammavipākaṃ = quả của nghiệp («cũng không phải là quả của nghiệp»)
kusalā nākusalā / kusalaṃ nākusalaṃ = không phải thiện không phải bất thiện (neva kusalā nākusalā; comma dropped); akusalaṃ = bất thiện
vihāraṃ = an trú; sukha = hạnh phúc in diṭṭhadhammasukhavihāraṃ («nhằm an trú trong hạnh phúc ngay trong đời này»; segments with vihāraṃ; elsewhere dễ dàng of sukhapaṭipadaṃ)
jhānaṃ bhāveti = tu tập tầng thiền; rūpāvacaraṃ = thuộc cõi hình sắc; arūpāvacaraṃ = thuộc cõi không hình sắc

## 3-01: headings and frames
Rūpa / rūpa / rūpaṃ (matter) = vật chất (Rūpakaṇḍaṃ «Phần về vật chất», rūpasaṅgaho, sabbaṃ rūpaṃ); rūpa = hình sắc in 1-583 (rūpāvacarā)
Uddeso = phần nêu đề mục; vibhatti = phân tích; niddeso = giải thích; kaṇḍaṃ = phần; Mātikā = ma trận
Dukaṃ = phân loại theo nhóm hai (MATRIX dukaṃ = bộ đôi, but here the heading / closing line words it «Phân loại theo nhóm hai»); Dasakaṃ / Ekādasakaṃ = phân loại theo nhóm mười / mười một; Dasa = mười; Ekādasa = mười một
saṅgaho = phân loại; rūpasaṅgaho = phân loại vật chất; vidhena = theo nhóm (<N>vidhena «theo nhóm <N>»; Catubbidhena = theo nhóm bốn, Chabbidhena = theo nhóm sáu)
Tattha = ở đây; eva = chắc chắn (1-594)
kiriyā = mang tính chức năng; asaṅkhatā ca dhātu = yếu tố không do điều kiện tạo thành

## 3-01: matter predicates (PRED301; reuse in 3-02 / 3-03)
Value form: frame dropped («Có loại vật chất …», «Vật chất nào … thì …», predicate «là», the «không (phải là)» of a na / no item). Matrix items take the MATRIX value.
upādā = phái sinh; upādiṇṇaṃ = do nghiệp tạo ra; upādiṇṇupādāniyaṃ / anupādiṇṇupādāniyaṃ = MATRIX (a) / (b); upādāniyaṃ = đối tượng của sự bám víu
sanidassanaṃ / anidassanaṃ / anidassana = thấy được / không thấy được; sappaṭighaṃ / appaṭighaṃ = có tính va chạm / không có tính va chạm; anidassanaappaṭighaṃ = không thấy được và không có tính va chạm
indriyaṃ = năng lực; mahābhūtaṃ / mahābhūtā = yếu tố cơ bản; bhūtaṃ / bhūtā = yếu tố (member; mahā = cơ bản)
viññatti = sự biểu lộ; kāyaviññatti = sự biểu lộ bằng thân; vacīviññatti = sự biểu lộ bằng lời nói
samuṭṭhānaṃ = do … sinh ra; cittasamuṭṭhānaṃ = do tâm sinh ra; cittasahabhu = cùng tồn tại với tâm; anuparivatti = vận hành theo; cittānuparivatti = vận hành theo tâm
ajjhattikaṃ / bāhiraṃ = thuộc phần bên trong / thuộc phần bên ngoài; oḷārikaṃ / sukhumaṃ = ở dạng thô / ở dạng vi tế
ārammaṇaṃ = đối tượng («là đối tượng của …»); có đối tượng in the Ekaka list (fragment of anārammaṇaṃ «không có đối tượng», MATRIX ārammaṇā)
cakkhu mắt, sota tai, ghāna mũi, jivhā lưỡi, kāya thân (sense organ; not thân tinh thần); X-āyatanaṃ = lĩnh vực X; X-dhātu = yếu tố X (rūpa- hình sắc, sadda- âm thanh, gandha- mùi, rasa- vị, phoṭṭhabba- vật xúc chạm; pathavī- đất, āpo- nước, tejo- lửa, vāyo- gió, ākāsa- không gian); dhammāyatana = lĩnh vực đối tượng của ý
itthi = nữ tính; purisa = nam tính; itthindriyaṃ / purisindriyaṃ = năng lực nữ tính / nam tính
X-samphassassa = sự tiếp xúc của X; samphassajāya = sinh từ sự tiếp xúc; kāyasamphassajāya = sinh từ sự tiếp xúc của thân; vedanāya cảm giác, saññāya tri giác, cetanāya chủ ý; samphassajāya vedanāya = cảm giác sinh từ sự tiếp xúc; X-viññāṇassa = thức qua X
rūpassa X = «X của vật chất»: lahutā sự nhẹ nhàng, mudutā sự mềm mại, kammaññatā sự dễ vận dụng, upacayo sự tăng trưởng, santati sự liên tục, jaratā sự lão hóa, aniccatā tính vô thường
kabaḷīkāro = thức ăn; āhāro = dưỡng chất; kabaḷīkāro āhāro = thức ăn trong vai trò dưỡng chất
rūpaṃ X (Atthi rūpaṃ X) = vật chất X (rūpaṃ sappaṭighaṃ vật chất có tính va chạm, rūpaṃ cittasamuṭṭhānaṃ vật chất do tâm sinh ra …); vật chất … X where «nào» intervenes («Vật chất nào có tính va chạm thì …», 1-586)
viññeyyaṃ rūpaṃ = vật chất mà … có thể nhận biết; viññeyyaṃ = có thể nhận biết (lists) / có thể được … nhận biết («có thể được sáu loại thức nhận biết», 1-584); viññāṇehi = loại thức
sutaṃ được nghe, mutaṃ được cảm nhận, viññātaṃ được nhận biết; samphassaṃ = tiếp xúc («có loại tiếp xúc dễ chịu / khó chịu»); sukha / dukkha = dễ chịu / khó chịu there (1-590)

## 3-01: Ekaka list (^1-584) and -meva (^1-594)
Matrix items in their MATRIX value, without «là»; a negated item maps to its positive part (na / no / neva … na, a-fragments): pahātabbaṃ cần dứt bỏ, X-sahagataṃ có X đi kèm, asekkhaṃ / sekkha, cetasikaṃ đồng hành với tâm, niyataṃ cố định, niyyānikaṃ dẫn đến giải thoát, rūpāvacaraṃ / arūpāvacaraṃ, hetukaṃ có gốc rễ, apariyāpannaṃ không nằm trong các cõi tồn tại (of no apariyāpannaṃ)
X-niyaṃ / sāsavaṃ = đối tượng của X; āsavaṃ = ô nhiễm; parāmaṭṭhaṃ = bị sự hiểu sai lệch nắm giữ; abyākataṃ = không xác định về mặt đạo đức (in 2-05 headings: loại …); parittaṃ = hạn hẹp; aniccaṃ = vô thường; uppannaṃ = đã sinh khởi; gāmi = dẫn đến
jarā = sự lão hóa; abhibhūtaṃ = bị … chế ngự (jarābhibhūtaṃ «bị sự lão hóa chế ngự»); upādāya = phái sinh từ; upādāya rūpaṃ = vật chất phái sinh từ
X-meva = chắc chắn + the value of X («là» kept inside: chắc chắn là đối tượng của …, chắc chắn là hạn hẹp / vô thường / không xác định về mặt đạo đức); chắc chắn … X where the item's negation stands between (chắc chắn … cần dứt bỏ, chắc chắn … có đối tượng, chắc chắn … ô nhiễm)
