# Notes for part 5 (Vietnamese plain zero-shot, Aṭṭhakathākaṇḍa: the matrix explained by classes of mind, ^1-4-0 … ^1-1616): new recurring terms and formulas

Builder: build_5_vi.py (imports build_4-02_4-03_vi and through it build_4-01_vi, build_matika_vi, build_ch2_01_sample_vi,
build_3-01_vi, build_3-02_3-03_vi and the 2-0x builders, unchanged; adds nothing to their tables).
`python -I -X utf8 build_5_vi.py` checks the 16 headings and the closing line against vi-zeroshot-terms.md (and the
mind-class names against the approved headings), asserts per line the Pāli count of «–», «?», «[» and «…pe…» (= «…»),
checks that every «Katame dhammā X?» opens with the matrix question of X, and asserts that every segment whose Pāli
equals a segment of an earlier part (or of this part) has the same Vietnamese (43 segments, e.g. ^1-1414 = 4-01 ^1-1023,
^1-1547 … 1549 = 4-02 ^1-1213 … 1215, ^1-1602 / 1604 / 1606 = 4-02 ^1-1288 / 1290 / 1292). Checks: verify_vi_5.py.
Helper: probe_5_vi.py (prints the reused earlier strings). 249 segments.

## Headings and closing lines (terms file)
Aṭṭhakathākaṇḍaṃ = Phần giải thích
Tikaatthuddhāro = Giải thích ý nghĩa các bộ ba
Dukaatthuddhāro = Giải thích ý nghĩa các bộ đôi
##### Hetu- … Piṭṭhidukaṃ = the matrix group headings (M.GROUPS)
Tikaṃ. (closing the triads) = Các bộ ba. (4-01)
Atthuddhāro niṭṭhito. = Phần giải thích ý nghĩa đã hoàn tất.
Dhammasaṅgaṇīpakaraṇaṃ niṭṭhitaṃ. = Bộ sách “Liệt kê các hiện tượng” đã hoàn tất.

## Frames
Katame dhammā X? … – ime dhammā X. = M.QUESTION(X) … – M.ANSWER(X)
ime dhammā siyā X, siyā Y = những hiện tượng này đôi khi <PRED X>, đôi khi <PRED Y>
na X (inside a siyā list) = không <PRED X> (không phải <PRED> when PRED starts with «là»)
(ime dhammā) na vattabbā X-tipi, Y-tipi = (về những hiện tượng này,) không nên nói rằng chúng “<PRED X>”, cũng không nên nói rằng chúng “<PRED Y>”
<Subj> na vattabbo / -ā / -aṃ (–) X-tipi, Y-tipi = Về <subj>, không nên nói (–) rằng nó / chúng “<PRED X>”, cũng không nên nói rằng nó / chúng “<PRED Y>” (4-02 «Về tâm, không nên nói – …»)
siyā na vattabbā … = đôi khi không nên nói rằng chúng …
na vattabbā X-ti (one item) = không nên nói rằng chúng “<PRED X>”
Pīti na pītisahagatā, sukhasahagatā, na upekkhāsahagatā = Sự hân hoan không có sự hân hoan đi kèm, có hạnh phúc đi kèm, không có sự bình thản đi kèm
Teva āsavā / Tāneva saṃyojanāni / Teva ganthā / Tāneva nīvaraṇāni / Tāneva upādānāni / Teva kilesā … = Chính những ô nhiễm / xiềng xích / nút thắt / chướng ngại / sự bám víu / phiền não ấy <PRED> (4-01 SAME)
So eva parāmāso parāmāso ceva parāmaṭṭho ca = Chính sự hiểu sai lệch ấy vừa là sự hiểu sai lệch vừa bị sự hiểu sai lệch nắm giữ. (= 4-02 ^1-1187)
Yattha dve tayo hetū ekato uppajjanti = Ở nơi hai hoặc ba gốc rễ cùng sinh khởi (ô nhiễm, xiềng xích, chướng ngại, phiền não likewise)
Yattha diṭṭhi ca lobho ca ekato uppajjanti = Ở nơi quan điểm và sự tham lam cùng sinh khởi
X … cittuppādesu uppajjati / uppajjanti = X sinh khởi trong …
ṭhapetvā X = ngoại trừ X
etthuppannaṃ X ṭhapetvā = ngoại trừ X sinh khởi trong đó
Ṭhapetvā X avasesaṃ akusalaṃ = tâm bất thiện còn lại ngoại trừ X
Ṭhapetvā hetū, … = Ngoại trừ các gốc rễ, …
Rūpañca nibbānañca anārammaṇā = Vật chất và Niết-bàn không có đối tượng.
Niyogā anāgatārammaṇā natthi = Không có hiện tượng nào nhất thiết có đối tượng thuộc tương lai.
Nibbānaṃ ṭhapetvā sabbe dhammā siyā atītā … = Ngoại trừ Niết-bàn, tất cả các hiện tượng đôi khi thuộc quá khứ, đôi khi thuộc tương lai, đôi khi thuộc hiện tại.
Sabbe dhammā kenaci viññeyyā, kenaci na viññeyyā = Tất cả các hiện tượng đều là những hiện tượng mà một loại thức nào đó có thể nhận biết, một loại thức nào đó không thể nhận biết.
Katame dhammā oghā / yogā…pe…. = Những hiện tượng nào là dòng lũ / ách….

## Classes of mind
bhūmi (catūsu / tīsu bhūmīsu) = cõi (thuộc bốn cõi / thuộc ba cõi), as the approved heading «Tâm thiện thuộc ba cõi»
catūsu / tīsu bhūmīsu kusalaṃ = tâm thiện thuộc bốn cõi / thuộc ba cõi
catūsu bhūmīsu kusalesu = trong tâm thiện thuộc bốn cõi
akusalaṃ = tâm bất thiện; sabbaṃ akusalaṃ = toàn bộ tâm bất thiện; sabbākusalesu = trong toàn bộ tâm bất thiện
catūsu / tīsu bhūmīsu vipāko = quả nghiệp thuộc bốn cõi / thuộc ba cõi (headings «Các quả nghiệp thuộc …»); catūsu bhūmīsu vipākesu = trong quả nghiệp thuộc bốn cõi
tīsu bhūmīsu kiriyābyākataṃ = tâm chức năng không xác định về mặt đạo đức thuộc ba cõi
tīsu bhūmīsu kiriyesu = trong tâm chức năng thuộc ba cõi
kāmāvacarakusalaṃ / kāmāvacaraṃ kusalaṃ = tâm thiện thuộc cõi dục lạc (heading)
kāmāvacarakiriyābyākataṃ = tâm chức năng không xác định về mặt đạo đức thuộc cõi dục lạc
sabbo kāmāvacarassa vipāko = toàn bộ quả nghiệp thuộc cõi dục lạc
cittuppāda (countable class) = loại tâm; dvādasa akusalacittuppādā = mười hai loại tâm bất thiện (heading «Mười hai loại tâm bất thiện»)
kāmāvacarakusalato N (X-cittuppādā) = N loại tâm thiện thuộc cõi dục lạc (X)
akusalato N = N loại tâm bất thiện
kāmāvacarakusalassa vipākato N (cittuppādā) = N loại quả của nghiệp thiện thuộc cõi dục lạc
akusalassa vipākato N = N loại quả của nghiệp bất thiện
kiriyato N (X-cittuppādā) = N loại tâm chức năng (X)
kāmāvacarassa vipākato ahetuke cittuppāde = các loại quả nghiệp thuộc cõi dục lạc không có gốc rễ
kāmāvacarakiriyato ahetuke cittuppāde = các loại tâm chức năng thuộc cõi dục lạc không có gốc rễ
cattāro ñāṇavippayutte cittuppāde = bốn loại tâm không gắn liền với hiểu biết
ñāṇasampayutta / ñāṇavippayutta = gắn liền / không gắn liền với hiểu biết (2-01)
somanassa- / upekkhā- / domanassa-sahagata = có niềm vui / có sự bình thản / có nỗi buồn đi kèm (2-04)
lobhasahagata / vicikicchāsahagata / uddhaccasahagata = có sự tham lam / có sự hoài nghi / có sự xao động đi kèm
cattāro diṭṭhigatasampayuttacittuppādā = bốn loại tâm gắn liền với sự mắc kẹt trong các quan điểm
cattāro diṭṭhigatavippayutta(-)lobhasahagatacittuppādā = bốn loại tâm có sự tham lam đi kèm và không gắn liền với sự mắc kẹt trong các quan điểm
cattāro diṭṭhigatasampayuttalobhasahagatacittuppādā = bốn loại tâm có sự tham lam đi kèm và gắn liền với sự mắc kẹt trong các quan điểm
aṭṭha lobhasahagatacittuppādā = tám loại tâm có sự tham lam đi kèm
dve domanassasahagatacittuppādā = hai loại tâm có nỗi buồn đi kèm
vicikicchāsahagato / uddhaccasahagato cittuppādo = loại tâm có sự hoài nghi / có sự xao động đi kèm
vicikicchāsahagatesu / uddhaccasahagatesu cittuppādesu = trong các loại tâm có sự hoài nghi / có sự xao động đi kèm
vicikicchāsahagato / uddhaccasahagato moho = sự si mê có sự hoài nghi / có sự xao động đi kèm
dvīsu domanassasahagatesu cittuppādesu uppanno moho = sự si mê sinh khởi trong hai loại tâm có nỗi buồn đi kèm
sasaṅkhārikesu akusalesu = trong các loại tâm bất thiện có sự thúc đẩy
dvepañcaviññāṇāni = hai nhóm năm loại thức
tisso manodhātuyo = ba yếu tố ý; pañca ahetukamanoviññāṇadhātuyo = năm yếu tố ý thức không có gốc rễ
kiriyāmanodhātu = yếu tố ý mang tính chức năng (heading)
kiriyāhetukamanoviññāṇadhātu somanassa- / upekkhāsahagatā = yếu tố ý thức mang tính chức năng, không có gốc rễ, có niềm vui / có sự bình thản đi kèm
akusalassa vipākato manoviññāṇadhātu upekkhāsahagatā = yếu tố ý thức là quả của nghiệp bất thiện, có sự bình thản đi kèm
dukkhasahagataṃ kāyaviññāṇaṃ = thức qua thân có sự đau khổ đi kèm (2-05)
kusalato ca vipākato ca kiriyato ca = (thiện, quả của nghiệp và chức năng); kusalato ca vipākato ca = (thiện và quả của nghiệp); kusalato ca kiriyato ca = (thiện và chức năng) (as 2-05 «(thiện)» / «(quả của nghiệp)»)
kusalābyākatā (^1-1418) = cả thiện lẫn không xác định về mặt đạo đức
sabbeva kāmāvacarā kusalākusalābyākatā dhammā = tất cả các hiện tượng thiện, bất thiện và không xác định về mặt đạo đức, thuộc cõi dục lạc (4-01)
kusalahetu / akusalahetu / abyākatahetu = gốc rễ thiện / bất thiện / không xác định về mặt đạo đức
vipākahetu / kiriyahetu = gốc rễ là quả của nghiệp / gốc rễ mang tính chức năng
Alobho kusalahetu, adoso kusalahetu, … uppajjanti = Sự không tham lam, gốc rễ thiện, và sự không sân hận, gốc rễ thiện, sinh khởi … (apposition, as 2-04 «sự không tham lam, gốc rễ không xác định về mặt đạo đức»)
tisso vedanā = ba loại cảm giác; yā ca vedanā upekkhā = cảm giác là sự bình thản
vitakkasahajāto vicāro = sự duy trì tâm cùng sinh khởi với sự hướng tâm

## Absorptions
rūpāvacaraṃ paṭhamaṃ / catutthaṃ jhānaṃ = tầng thiền thứ nhất / thứ tư thuộc cõi hình sắc
lokuttaraṃ paṭhamaṃ / catutthaṃ jhānaṃ = tầng thiền thứ nhất / thứ tư vượt thế gian
(rūpāvacara / lokuttara) pañcakanaye dutiyaṃ jhānaṃ = tầng thiền thứ hai thuộc cõi hình sắc / vượt thế gian theo phương pháp chia năm
rūpāvacara-<a><b>-jjhānā = <a> tầng thiền thuộc cõi hình sắc theo phương pháp chia bốn và <b> tầng thiền theo phương pháp chia năm (lokuttara: «… tầng thiền vượt thế gian …»); ekakaduka 1/2, dukaduka 2/2, dukatika 2/3, tikatika 3/3, tikacatukka 3/4, catukkapañcaka 4/5
catutthassa jhānassa vipāko = quả nghiệp của tầng thiền thứ tư
cattāro āruppā = bốn tầng thiền không hình sắc (heading «Bốn tầng thiền không hình sắc»)
cattāro arūpāvacarā = bốn loại tâm thuộc cõi không hình sắc
ākāsānañcāyatana / viññāṇañcāyatana / ākiñcaññāyatana / nevasaññānāsaññāyatana = lĩnh vực không gian vô tận / lĩnh vực thức vô tận / lĩnh vực không có gì cả / lĩnh vực không phải tri giác cũng không phải không tri giác (2-02)

## Paths, fruits, material form, nibbāna
nibbānaṃ = Niết-bàn (core terms)
cattāro maggā apariyāpannā = bốn con đường không nằm trong các cõi tồn tại (4-01)
cattāri sāmaññaphalāni = bốn thành quả của đời sống sa-môn (4-01 «ba thành quả thấp hơn của đời sống sa-môn»)
cattāro ariyamaggā = bốn con đường cao quý
upariṭṭhimaṃ arahattaphalaṃ = Thành quả cao nhất, tức là thành quả A-la-hán (4-01)
yañca rūpaṃ (na) kammassa katattā = loại vật chất (không) sinh ra do nghiệp đã được tạo (3-02 / 4-01)
yañca rūpaṃ anidassanaṃ appaṭighaṃ dhammāyatanapariyāpannaṃ = loại vật chất không thấy được và không có tính va chạm, nằm trong lĩnh vực đối tượng của ý (4-01)
anindriyabaddharūpa = vật chất không gắn kết với các năng lực (indriya = năng lực, core)
sabbañca rūpaṃ = toàn bộ vật chất; avasesañca rūpaṃ = vật chất còn lại
rūpāyatanaṃ / cakkhāyatanaṃ…pe… phoṭṭhabbāyatanaṃ = Lĩnh vực hình sắc / Lĩnh vực mắt… lĩnh vực vật xúc chạm (4-01)
yaṃ vā panaññampi atthi rūpaṃ cittajaṃ cittahetukaṃ cittasamuṭṭhānaṃ – … = hoặc bất cứ loại vật chất nào khác sinh từ tâm, có tâm làm gốc rễ, do tâm sinh ra – … (4-02 has «:» there; here the Pāli has «–»)

## Lists of defilements (4-01 / 4-02 names)
Cattāro āsavā – … = Bốn loại ô nhiễm – ô nhiễm dục lạc, ô nhiễm hiện hữu, ô nhiễm quan điểm, ô nhiễm vô minh
Dasa saṃyojanāni – … = Mười xiềng xích – xiềng xích tham đắm dục lạc, …, xiềng xích vô minh
Cattāro ganthā – … = Bốn nút thắt – nút thắt của thân bằng sự thèm muốn, …
Cha nīvaraṇā – … = Sáu chướng ngại – chướng ngại ý muốn dục lạc, …; uddhacca- / kukkuccanīvaraṇaṃ = chướng ngại xao động / chướng ngại hối tiếc
diṭṭhiparāmāso = sự hiểu sai lệch dưới dạng quan điểm
Cattāri upādānāni – … = Bốn sự bám víu – sự bám víu vào dục lạc, …
Dasa kilesavatthūni – … = Mười chỗ dựa của phiền não – sự tham lam, …, sự không biết ghê sợ tội lỗi
paṭigha (aversion) = sự ác cảm (2-04)

## Choices to review
vipāka as a class of mind = «quả nghiệp» (the approved headings «Tám quả nghiệp lớn», «Các quả nghiệp thuộc cõi hình sắc»); kusalassa / akusalassa vipākato = «quả của nghiệp thiện / bất thiện» (2-04 / 2-05 frames).
kiriyābyākata = «tâm chức năng không xác định về mặt đạo đức» (keeps the abyākata lesson; no inner comma, so the long lists stay comma-separated).
cittuppāda = «loại tâm»; siyā = «đôi khi»; na vattabbā = the 4-02 «không nên nói rằng …» frame.
Ṭhapetvā X avasesaṃ akusalaṃ = «tâm bất thiện còn lại ngoại trừ X» (not «ngoại trừ X, tâm bất thiện còn lại», which would read as excluding X from the whole list).
dvepañcaviññāṇāni = «hai nhóm năm loại thức»; anindriyabaddha = «không gắn kết với các năng lực».
Book closing line «Bộ sách “Liệt kê các hiện tượng” đã hoàn tất.» (title in “…” mid-sentence, style file).

## Source points translated as written
^1-1389: «ya vedanāya sampayuttātipi» is a truncated «adukkhamasukhāya vedanāya sampayuttātipi» (spelling slip); written out as the matrix item (triad 2 (c)), as the English and Russian.
^1-1387: «akusalato cattāro kāmāvacarakusalassa vipākato ca kiriyato ca pañca» lacks a comma after «cattāro»; split by sense. The «pañca» for the results of the wholesome is as written («năm loại quả của nghiệp thiện thuộc cõi dục lạc và tâm chức năng»), although ^1-1403 counts six results (with body-consciousness accompanied by pleasure); possible slip, not changed.
^1-1478: the question ends with «.» («Katame dhammā no saṃyojanā.»); kept («Những hiện tượng nào không phải là xiềng xích.»).
^1-1401: «[dutiyajjhāne (sī.)]» = khác chính tả; missing commas («kiriyato ca lokuttara…», «vicāro rūpañca nibbānañca»): normal Vietnamese punctuation.
^1-1464: «[sabbeva (syā.)]» adds eva = dị bản.
^1-1501 / ^1-1502 (floods, yokes) are abridged in the Pāli («…pe….»); kept abridged.
^1-1465: no punctuation between the āsava sentences («… uppajjati bhavāsavo … uppajjati diṭṭhāsavo …»); commas written.
^1-1458: stray space before «…pe…»; mirrored («Lĩnh vực mắt … lĩnh vực vật xúc chạm»).
^1-1406, 1567, 1590, 1597, 1598, 1611 and others: missing commas in the Pāli lists; normal Vietnamese punctuation.
