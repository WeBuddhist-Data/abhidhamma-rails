# Notes for part 3-01 (Vietnamese plain zero-shot, Rūpakaṇḍa: Uddeso, Mātikā, Ekakaniddeso, ^1-2-0 … ^1-594): new recurring terms and formulas

Builder: build_3-01_vi.py (imports build_matika_vi, build_ch2_01_sample_vi and the 2-01 … 2-05 builders unchanged; adds
nothing to their tables). `python -I -X utf8 build_3-01_vi.py` checks the 16 headings against vi-zeroshot-terms.md, then
writes the part. Every predicate that is a matrix item comes from M.PRED (or «(không) thuộc về» + M.BARE), never retyped;
Vietnamese does not inflect, so «các hiện tượng X» -> «vật chất X» needs no change. Checks: verify_vi_3-01.py.
Helper: dump_3-01_vi.py (prints the reused earlier strings). 29 segments.
Reusable pieces (import with importlib): RF, ALL_RF, KIND, HEAD, CLOSE, N, P, GEN, RUPASSA, MAHABHUTA, pred(),
s_atthi(), s_yam1(), s_yam2(), EKAKA, EKAKA_V, NIDDESA, LISTS, translate_line().

## Headings and closing lines (headings verbatim from vi-zeroshot-terms.md; closing line = heading + «.»)
#### Mātikā = #### Ma trận (### Mātikā of 1-matika one level down); Mātikā. = Ma trận.
<N>vidhena rūpasaṅgaho – = Phân loại vật chất theo nhóm <N> – (ekavidhena … ekādasavidhena = theo nhóm một … theo nhóm mười một, the heading words)
Evaṃ <N>vidhena rūpasaṅgaho. = Như vậy là phân loại vật chất theo nhóm <N>.

## Frames
rūpa (matter) = vật chất; sabbaṃ rūpaṃ = toàn bộ vật chất
Atthi rūpaṃ A, atthi rūpaṃ B. = Có loại vật chất A, có loại vật chất B.
Yaṃ taṃ rūpaṃ A, taṃ P. = Vật chất nào A thì P.
Yaṃ taṃ rūpaṃ A, taṃ atthi P, atthi Q. = Vật chất nào A thì có loại P, có loại Q.
yañca rūpaṃ X (closing a list) = và loại vật chất X
X…pe… Y…pe… Z (chain) = X… Y… Z (head «là chỗ dựa cho» / «là đối tượng của» once, before the chain); 'na X…pe… na Y' = không phải là X… không phải là Y; stray space before «…pe…» mirrored
Tattha katamaṃ sabbaṃ rūpaṃ? = Ở đây, toàn bộ vật chất là gì?
Cattāro ca mahābhūtā, catunnañca mahābhūtānaṃ upādāya rūpaṃ – idaṃ vuccati sabbaṃ rūpaṃ. = Bốn yếu tố cơ bản và vật chất phái sinh từ bốn yếu tố cơ bản – đây được gọi là toàn bộ vật chất.
upādāya (derived from) = phái sinh từ
idaṃ vuccati X = đây được gọi là X
-meva (^1-594) = chắc chắn <predicate>
Ekaka lists (^1-584, ^1-594): items separated by «;» (several items contain commas).
na <triad item> / no <pair item> (^1-584) = không thuộc về <M.BARE>; pahātabbahetukaṃ (triad 9 (c)) = thuộc về <M.BARE>

## Uddeso ^1-583
Kusalākusalānaṃ dhammānaṃ vipākā kāmāvacarā rūpāvacarā arūpāvacarā apariyāpannā vedanākkhandho … viññāṇakkhandho = Các quả của các hiện tượng thiện và bất thiện, thuộc cõi dục lạc, thuộc cõi hình sắc, thuộc cõi không hình sắc, không nằm trong các cõi tồn tại, tức là khối cảm giác, khối tri giác, khối tạo tác, khối thức
ye ca dhammā kiriyā neva kusalā nākusalā na ca kammavipākā = và những hiện tượng mang tính chức năng, không phải thiện, không phải bất thiện, cũng không phải là quả của nghiệp (2-05 KIRIYA_V)
sabbañca rūpaṃ = và toàn bộ vật chất
asaṅkhatā dhātu = yếu tố không do điều kiện tạo thành

## Predicates (matrix ones from M.PRED)
upādā / no upādā = là phái sinh / không phải là phái sinh (^1-M2-67)
upādiṇṇaṃ / anupādiṇṇaṃ = do nghiệp tạo ra / không do nghiệp tạo ra (^1-M2-68)
upādiṇṇupādāniyaṃ / anupādiṇṇupādāniyaṃ = ^1-M1-4 (a) / (b)
sanidassanaṃ / anidassanaṃ = thấy được / không thấy được; sappaṭighaṃ / appaṭighaṃ = có tính va chạm / không có tính va chạm
cittasamuṭṭhānaṃ / cittasahabhu / cittānuparivatti = do tâm sinh ra / cùng tồn tại với tâm / vận hành theo tâm
ajjhattikaṃ / bāhiraṃ = thuộc phần bên trong / thuộc phần bên ngoài (^1-M2-66)
indriyaṃ / na indriyaṃ = là năng lực / không phải là năng lực
mahābhūta = yếu tố cơ bản (cattāro mahābhūtā = bốn yếu tố cơ bản)
viññatti = sự biểu lộ; kāyaviññatti = sự biểu lộ bằng thân; vacīviññatti = sự biểu lộ bằng lời nói
oḷārikaṃ / sukhumaṃ = ở dạng thô / ở dạng vi tế
dūre / santike = ở xa / ở gần
vatthu (of contact, consciousness) = chỗ dựa (là chỗ dựa cho …)
ārammaṇaṃ / nārammaṇaṃ = là đối tượng của … / không phải là đối tượng của …
cakkhu / sota / ghāna / jivhā / kāya (sense) = mắt / tai / mũi / lưỡi / thân
cakkhusamphassa … kāyasamphassa = sự tiếp xúc của mắt … sự tiếp xúc của thân (as «sự tiếp xúc của thân / của tâm», 2-04)
cakkhusamphassajā vedanā = cảm giác sinh từ sự tiếp xúc của mắt
cakkhuviññāṇa … kāyaviññāṇa = thức qua mắt … thức qua thân (2-04)
cakkhāyatana / sotā- / ghānā- / jivhā- / kāyāyatana = lĩnh vực mắt / tai / mũi / lưỡi / thân
rūpāyatana / saddā- / gandhā- / rasā- / phoṭṭhabbāyatana = lĩnh vực hình sắc / âm thanh / mùi / vị / vật xúc chạm (object words of the sample's ārammaṇa list)
cakkhudhātu … phoṭṭhabbadhātu = yếu tố mắt / tai / mũi / lưỡi / thân / hình sắc / âm thanh / mùi / vị / vật xúc chạm
cakkhundriya / sotindriya / ghānindriya / jivhindriya / kāyindriya = năng lực mắt / tai / mũi / lưỡi / thân
itthindriya / purisindriya = năng lực nữ tính / năng lực nam tính
pathavī- / āpo- / tejo- / vāyodhātu = yếu tố đất / nước / lửa / gió (kasiṇa words, 2-02)
ākāsadhātu = yếu tố không gian (ākāsa as ākāsānañcāyatana, 2-02)
rūpassa lahutā / mudutā / kammaññatā = sự nhẹ nhàng / sự mềm mại / sự dễ vận dụng của vật chất (sample words)
rūpassa upacayo = sự tăng trưởng của vật chất (not «sự tích lũy»: ācaya, matrix triad 10)
rūpassa santati = sự liên tục của vật chất (not «dòng»: ogha = dòng lũ)
rūpassa jaratā = sự lão hóa của vật chất; jarābhibhūtaṃ = bị sự lão hóa chế ngự (abhibhū = chế ngự, 2-02)
rūpassa aniccatā = tính vô thường của vật chất; aniccaṃ = là vô thường
kabaḷīkāro āhāro = thức ăn trong vai trò dưỡng chất (pattern of phassāhāro = sự tiếp xúc trong vai trò dưỡng chất, 2-01)

## Ekaka list extras (^1-584 / ^1-594)
rūpaṃ [rūpiyaṃ (sī.)] = thuộc vật chất [dị bản (Sī.): rūpiyaṃ] (^1-M2-11 (a))
na savitakkasavicāraṃ = không thuộc về các hiện tượng có sự hướng tâm và sự duy trì tâm (^1-M1-6 (a))
na avitakkavicāramattaṃ = không thuộc về các hiện tượng không có sự hướng tâm, chỉ có sự duy trì tâm (^1-M1-6 (b))
neva dassanena na bhāvanāya pahātabbahetukaṃ = thuộc về các hiện tượng có gốc rễ không cần dứt bỏ bằng sự thấy chân lý cũng không bằng sự tu tập (^1-M1-9 (c); material form has no roots)
no apariyāpannaṃ = không thuộc về các hiện tượng không nằm trong các cõi tồn tại (^1-M2-96 (b))
chahi viññāṇehi viññeyyaṃ = có thể được sáu loại thức nhận biết
uppannaṃ chahi viññāṇehi viññeyyameva (^1-594) = khi đã sinh khởi, chắc chắn có thể được sáu loại thức nhận biết

## Lists (^1-586 … ^1-593)
Diṭṭhaṃ sutaṃ mutaṃ viññātaṃ rūpaṃ = Vật chất được thấy, được nghe, được cảm nhận, được nhận biết
X-viññeyyaṃ rūpaṃ = vật chất mà X có thể nhận biết (mắt, tai, mũi, lưỡi, thân, ý, yếu tố ý, yếu tố ý thức; as ^1-M2-13 (a) «mà một loại thức nào đó có thể nhận biết»)
atthi sukhasamphassaṃ, atthi dukkhasamphassaṃ = có loại tiếp xúc dễ chịu, có loại tiếp xúc khó chịu
na indriyaṃ rūpaṃ atthi sappaṭighaṃ, atthi appaṭighaṃ = còn vật chất không phải là năng lực thì có loại có tính va chạm, có loại không có tính va chạm
anidassanaappaṭighaṃ [anidassanaṃ appaṭighaṃ (sī. syā.)] dhammāyatanapariyāpannaṃ = không thấy được và không có tính va chạm [khác chính tả (Sī., Syā.): anidassanaṃ appaṭighaṃ], nằm trong lĩnh vực đối tượng của ý (^1-M1-22 (c); pariyāpanna = nằm trong; dhammāyatana as 2-01)

## Choices to review
mahābhūta = «yếu tố cơ bản» (plain 'primary element'; «đại chủng / tứ đại» are specialist; pairs with upādā = phái sinh).
vatthu = «chỗ dựa» («nền tảng» is already iddhipāda / titthāyatana).
kabaḷīkāro āhāro = «thức ăn trong vai trò dưỡng chất»; oḷārika / sukhuma = «ở dạng thô / ở dạng vi tế»; viññatti = «sự biểu lộ».
-meva = «chắc chắn» (each item).

## Source points translated as written
^1-584 lists «uppannaṃ, chahi viññāṇehi viññeyyaṃ» as two items; ^1-594 has one item «uppannaṃ chahi viññāṇehi viññeyyameva» (no «uppannameva»); kept.
^1-591 / ^1-592: no comma after jivhindriyaṃ; ^1-586: «sappaṭighaṃ atthi appaṭighaṃ» without a comma: normal Vietnamese punctuation.
^1-U1 (line «… cetanāya …pe… kāyaviññāṇassa vatthu»): stray space before «…pe…», mirrored («chủ ý … thức qua thân»).
^1-U1: odd block ID in the source, kept.
