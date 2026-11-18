# Notes: Pāli→Vietnamese keyword map, pi-1 part 5-atthakathakandam (new recurring decisions)

Script: map_5_vi.py (OVERRIDES → SAME → context5() → ADD5 → the 4-02/4-03 tables `_val` (ADD402, then the 4-01 `_value`: ADD401, MATRIX, «dhammā X», the 3-02/3-03 value(), T05) → ch2_value(T05); `dump [miss]` lists every distinct pair). The earlier parts' segment rules (context functions) are not applied here; every value was checked in `dump`. Imports map_4-02_4-03_vi.py; importing writes nothing: the thirteen earlier mapped files hash the same before and after. Review helper: probe_5_vi.py.
249 lines, `bad []`, 0 presence misses, 5 (no direct equivalent): caya (1-1412, as 2-03 / 4-01), sekkhā (1-1415, copied from 4-01 ^1-1024), citta (1-1399, 1-1589, 1-1591: see below).
SAME: 1-1414 / 1-1415 = 4-01 ^1-1023 / ^1-1024; 1-1547 … 1-1549 = 4-02 ^1-1213 … 1215; 1-1602 / 1604 / 1606 = 4-02 ^1-1288 / 1290 / 1292 (same Pāli, same keywords: values copied, checked equal).
Matrix item names (questions, answers, siyā / na vattabbā clauses, «dhammā X») keep the MATRIX values; «hiện tượng … X» where «nào» intervenes (1-1426, 1-1430: no «đây là các hiện tượng …» answer).

## Planes and classes of mind
bhūmīsu = cõi (catūsu / tīsu bhūmīsu «thuộc bốn / ba cõi»)
kusalaṃ / kusalesu / kusalato / kusalassa = thiện; akusalaṃ / akusalesu / akusalato / akusalassa = bất thiện («tâm thiện / bất thiện …»: «tâm» implied, no keyword of its own, as 2-04 akusalāni, 2-05 kiriyā)
akusalacitta (Dvādasa akusalacittuppādā «Mười hai loại tâm bất thiện») = tâm bất thiện; citta = tâm
cittuppāda (countable class) = loại tâm: cittuppādā / -o / -e / -esu = loại tâm; the member uppādā / -o / -e / -esu = loại
citta = (no direct equivalent) and cittuppādā = loại in 1-1399, 1-1589, 1-1591: the only cittuppādā there is «kāmāvacarakusalassa vipākato ekādasa cittuppādā» = «mười một loại quả của nghiệp thiện …» (no «tâm»)
kiriyā = chức năng beside kiriyābyākataṃ («tâm chức năng không xác định về mặt đạo đức»); mang tính chức năng where it is the member of kiriyāmanodhātu / kiriyāhetuka… (1-1420, 1-1434)
kiriyābyākataṃ = chức năng không xác định về mặt đạo đức; abyākataṃ / abyākatā / abyākata = không xác định về mặt đạo đức (no «loại»: unlike the 2-05 headings)
kiriyato / kiriyesu = chức năng («loại tâm chức năng», «(thiện, quả của nghiệp và chức năng)»); kiriya = mang tính chức năng (kiriyahetu «gốc rễ mang tính chức năng», 4-01)
vipākato = quả của nghiệp («loại quả của nghiệp thiện …», «(…, quả của nghiệp …)»); vipāka (vipākahetu) = quả của nghiệp
vipākato ca kiriyato = quả của nghiệp và chức năng; kusalato ca vipākato = thiện và quả của nghiệp (the «(thiện và quả của nghiệp)» of the world-transcending absorptions, which every segment with this keyword has)
X-sahagata(-ā/-o/-aṃ/-esu) = có X đi kèm (somanassa niềm vui, upekkhā sự bình thản, domanassa nỗi buồn, lobha sự tham lam, vicikicchā sự hoài nghi, uddhacca sự xao động, pīti sự hân hoan, sukha hạnh phúc); sahagata(-…) = đi kèm
sahagatacitta / sahagato citta / sahagatesu citta = tâm … đi kèm («loại tâm có X đi kèm»); vippayuttacitta / vippayutte citta = tâm … không gắn liền; ahetuke citta = tâm … không có gốc rễ («các loại tâm chức năng thuộc cõi dục lạc không có gốc rễ»)
diṭṭhigata = sự mắc kẹt trong các quan điểm; diṭṭhigatavippayutta(-ā) = không gắn liền với sự mắc kẹt trong các quan điểm; vippayuttalobha / vippayuttā lobha = sự tham lam … không gắn liền («có sự tham lam đi kèm và không gắn liền với …»)
sahagato moho / sahagataṃ mohaṃ = sự si mê … đi kèm; sahagataṃ uddhaccasahagataṃ mohaṃ = sự si mê có sự xao động đi kèm
avasesaṃ = còn lại; avasesaṃ akusalaṃ = bất thiện còn lại («tâm bất thiện còn lại ngoại trừ …»); sabbaṃ = toàn bộ; sasaṅkhārikesu = có sự thúc đẩy
dukkha = sự đau khổ (dukkhasahagataṃ kāyaviññāṇaṃ «thức qua thân có sự đau khổ đi kèm», 2-05)
etthuppanna X ṭhapetvā: uppannaṃ / uppanne / uppanno = sinh khởi; uppanne vitakkavicāre = sự hướng tâm và sự duy trì tâm sinh khởi; uppannaṃ vicāraṃ / uppanno ca vicāro = sự duy trì tâm sinh khởi; uppannaṃ vitakkaṃ = sự hướng tâm sinh khởi; uppanne hetū = gốc rễ sinh khởi
hetū ekato uppajjanti = gốc rễ cùng sinh khởi; ekato = cùng; sahajāto = cùng sinh khởi
siyā = đôi khi; vattabbā / -o / -aṃ = nên nói; vattabb- X = nên nói … X («không nên nói rằng chúng / nó “X”»; «rằng chúng / nó» skipped): savitakkasavicāro, pītisahagatanti, parittārammaṇā, maggārammaṇā (lấy con đường làm đối tượng), anuppannā (chưa sinh khởi), atītārammaṇā, ajjhattārammaṇanti (có đối tượng thuộc về bản thân)
yañca = và loại; loại where the list is «;»-separated with no «và» before it (1-1440, 1-1458, 1-1460, 1-1552)

## Absorptions
jhānaṃ / jhānā / jhāne / jhānassa = tầng thiền; catutthaṃ jhānaṃ / catutthassa jhānassa = tầng thiền thứ tư
lokuttara / lokuttaraṃ = vượt thế gian; lokuttaraṃ catutthaṃ / paṭhamaṃ jhānaṃ = tầng thiền thứ tư / thứ nhất vượt thế gian; lokuttarapañcakanaye dutiyaṃ jhānaṃ = tầng thiền thứ hai vượt thế gian theo phương pháp chia năm
lokuttara<a><b>jjhānā = «<a> tầng thiền vượt thế gian theo phương pháp chia bốn và <b> tầng thiền theo phương pháp chia năm» (ekaka một, duka hai, tika ba, catukka bốn, pañcaka năm)
pañcaka = chia năm; naye = phương pháp; pañcakanaye = theo phương pháp chia năm
āruppā = tầng thiền không hình sắc; arūpāvacarā = thuộc cõi không hình sắc (cattāro arūpāvacarā «bốn loại tâm thuộc cõi không hình sắc»)
rūpāvacara(-ṃ/-ā) = thuộc cõi hình sắc; rūpa = hình sắc; Kāmāvacara(-ṃ/-ā/-ssa) = thuộc cõi dục lạc; avacara(-…) = thuộc cõi
ānañcāyatanaṃ = lĩnh vực … vô tận (2-02); asaññā = không tri giác (2-04)

## Mind elements, roots, material form, nibbāna
viññāṇāni = loại thức, pañcaviññāṇāni = năm loại thức (dvepañcaviññāṇāni «hai nhóm năm loại thức»); manodhātuyo = yếu tố ý; dhātuyo = yếu tố
hetuka (of ahetuka-) = có gốc rễ; kiriyāmano / kiriyāmanodhātu = ý / yếu tố ý mang tính chức năng; kiriyāhetukamanoviññāṇa(dhātu) = (yếu tố) ý thức mang tính chức năng không có gốc rễ (commas dropped)
dhātu upekkhāsahagatā / manoviññāṇadhātu upekkhāsahagatā = yếu tố (ý thức) … có sự bình thản đi kèm (as 2-05)
kusalahetu(-ū) / akusalahetū / abyākatahetū = gốc rễ thiện / bất thiện / không xác định về mặt đạo đức; vipākahetu = gốc rễ là quả của nghiệp; kiriyahetu = gốc rễ mang tính chức năng
hetukā = có gốc rễ; lấy … làm gốc rễ and ārammaṇā = lấy … làm đối tượng in 1-1429 (maggahetukā / maggārammaṇā, as 4-01); pahātabbahetukā = có gốc rễ cần dứt bỏ where contiguous, else có gốc rễ … cần dứt bỏ (4-02 rule)
rūpañca / rūpaṃ = vật chất; rūpañca nibbānañca = vật chất và Niết-bàn; rūpaṃ nibbānañca = vật chất … và Niết-bàn («vật chất còn lại và Niết-bàn»); nibbānañca anārammaṇā = Niết-bàn không có đối tượng; sāmaññaphalāni nibbānañca = thành quả của đời sống sa-môn và Niết-bàn
indriyabaddharūpañca nibbānañca = vật chất … gắn kết với các năng lực và Niết-bàn (positive part of anindriyabaddha «không gắn kết»); baddha = gắn kết; indriya = năng lực
ariya = cao quý (cattāro ariyamaggā); sekkha = thuộc về người còn đang tu học (nevasekkhanāsekkhā)
atītā / anāgatā / paccuppannā = thuộc quá khứ / tương lai / hiện tại; Niyogā = nhất thiết; niyatā = cố định (also the positive part of aniyatā)
dhammā nevācayagāmināpacayagāmino = hiện tượng không dẫn đến sự tích lũy cũng không dẫn đến sự giảm trừ; dhammā kenaci viññeyyā = hiện tượng … một loại thức nào đó có thể nhận biết; kenaci = một loại thức nào đó; dhammā (bare) = hiện tượng
kāya = thân (kāyaviññatti, kāyagantho; CH2 «thân tinh thần» is the six pairs)

## Defilement groups
«Teva / Tāneva X X ceva …»: saṃyojanāni saṃyojanā / nīvaraṇāni nīvaraṇā / upādānāni upādānā / kilesā kilesā = X … X («Chính những X ấy vừa là X …»)
fetter and hindrance stems without «sự» in the name lists (1-1477, 1-1503: paṭigha ác cảm, māna kiêu mạn, vicikicchā hoài nghi, issā ganh tị, rāga tham đắm, kāmarāga tham đắm dục lạc, parāmāsa hiểu sai lệch; uddhacca xao động), as 4-01 ^1-1118 / 4-02 ^1-1158
rāgasaṃyojanaṃ = xiềng xích tham đắm; parāmāsasaṃyojanaṃ = xiềng xích hiểu sai lệch; diṭṭhisaṃyojanaṃ = xiềng xích quan điểm
abhiniveso = sự cố chấp; abhiniveso kāyagantho = nút thắt của thân bằng sự cố chấp; parāmāso kāyagantho = nút thắt của thân bằng sự hiểu sai lệch
Diṭṭhiparāmāso = sự hiểu sai lệch dưới dạng quan điểm; parāmāsa / parāmāso / parāmāsā / parāmāsaṃ = sự hiểu sai lệch
oghā = dòng lũ; yogā = ách (1-1501 / 1-1502, abridged)

## Headings and closing lines
Aṭṭhakathā = giải thích («Phần giải thích»); kaṇḍaṃ = phần; atthuddhāro / Atthuddhāro = giải thích ý nghĩa («Phần» of «Phần giải thích ý nghĩa đã hoàn tất» has no keyword); niṭṭhito = đã hoàn tất
group headings: MATRIX values (Hetu gốc rễ, Āsava ô nhiễm …; antara xen giữa, antaradukaṃ bộ đôi xen giữa, dukaṃ / Duka bộ đôi, Piṭṭhi cuối)
1-1616 (book colophon): Dhammasaṅgaṇī = Liệt kê các hiện tượng, saṅgaṇī = liệt kê, Dhamma = hiện tượng (CORE, the preamble title)
