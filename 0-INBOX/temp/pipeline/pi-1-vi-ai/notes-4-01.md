# Notes for part 4-01 (Vietnamese plain zero-shot, Nikkhepakaṇḍa: summary of the triads and of the root, short intermediate, taint, fetter and tie groups, ^1-3-0 … ^1-1155): new recurring terms and formulas

Builder: build_4-01_vi.py (imports build_matika_vi, build_ch2_01_sample_vi, build_3-01_vi, build_3-02_3-03_vi and through
them the 2-01 … 2-05 builders, unchanged; adds nothing to their tables). `python -I -X utf8 build_4-01_vi.py` checks the
8 headings against vi-zeroshot-terms.md, then writes the part; per line it asserts the Pāli count of «–», «?», «[» and
«…pe…» (= «…»). Checks: verify_vi_4-01.py. Helper: probe_4-01_vi.py (prints the reused earlier strings). 179 segments.
Every matrix item, question and answer comes from M.QUESTION / M.ANSWER / M.BARE / M.PRED; reused strings: sample
(alobha, adosa, paññā, factor names), 2-03 (dhammavicayasambojjhaṅgo, maggaṅgaṃ maggapariyāpannaṃ), 2-04 (lobha, dosa,
moha, diṭṭhi, kaṅkhā strings and the names lobho / doso / moho / abhijjhā / byāpādo / vicikicchā / micchādiṭṭhi),
2-05 (kiriya phrase), 3-01 (sphere list, aggregates, «toàn bộ vật chất», «yếu tố không do điều kiện tạo thành»,
mahābhūta line, sense organs), 3-02 (kammassa katattā, the dhammāyatana class). ^1-987 = 3-01 ^1-583 byte for byte.

## Headings and closing lines (headings verbatim from vi-zeroshot-terms.md)
Nikkhepakaṇḍaṃ = Phần tóm lược; Tikanikkhepaṃ = Tóm lược các bộ ba; Dukanikkhepaṃ = Tóm lược các bộ đôi
##### Hetu- / Cūḷantara- / Āsava- / Saṃyojana- / Ganthagocchakaṃ = the matrix group headings (M.GROUPS)
Tikaṃ. (closing the triad summary) = Các bộ ba.  (3-01 «Tikaṃ.» = «Phân loại theo nhóm ba.» closes the rūpa classification; context differs, as the approved Russian)
Nikkhepakaṇḍe paṭhamabhāṇavāro. = Phần tụng đọc thứ nhất của phần tóm lược.

## Frames
Katame dhammā X? … – ime dhammā X. = M.QUESTION(X) … – M.ANSWER(X)
Tattha katamo / katamā / katamaṃ / katame X? = Ở đây, X là gì?  (3-01)
– ayaṃ / idaṃ vuccati X. = – đây được gọi là X.  (3-01)
Tattha katamā X…pe… ayaṃ vuccati X. = Ở đây, X là gì… đây được gọi là X.
Yo / Yā / Yaṃ S – ayaṃ vuccati X. = Bất cứ điều gì là S – đây được gọi là X.
yo / yā / yaṃ evarūpo / evarūpā / evarūpaṃ S = bất cứ điều gì thuộc loại như vậy, tức là S
Ime dhammā X. (own line) = Đây là <M.BARE(X)>.;  Ime tayo kusalahetū. = Đây là ba gốc rễ thiện.
ime dhammā <A>hetū (pahātabbahetū, maggahetū) = đây là các hiện tượng là gốc rễ cần dứt bỏ bằng sự thấy chân lý / sự tu tập; … là gốc rễ của con đường
ṭhapetvā = ngoại trừ (2-01); Te dhamme ṭhapetvā avasesā X = Ngoại trừ những hiện tượng ấy, X còn lại
Imāni tīṇi saṃyojanāni = Ba xiềng xích này; Ime cha apariyāpannahetū = Sáu gốc rễ không nằm trong các cõi tồn tại này
Tadubhayaṃ = Cả hai loại ấy
Yeva te dhammā sappaccayā, teva te dhammā saṅkhatā. = Những hiện tượng nào có điều kiện thì chính những hiện tượng ấy do điều kiện tạo thành. (Yo eva so dhammo appaccayo … = Hiện tượng nào không có điều kiện thì chính hiện tượng ấy không do điều kiện tạo thành.)
Teyeva āsavā āsavā ceva sāsavā ca. = Chính những ô nhiễm ấy vừa là ô nhiễm vừa là đối tượng của ô nhiễm. (Tāneva saṃyojanāni …, Teva ganthā … likewise)
Tehi dhammehi ye dhammā sahetukā / ahetukā = Những hiện tượng có / không có những hiện tượng ấy làm gốc rễ
Tehi dhammehi ye dhammā sampayuttā / vippayuttā = Những hiện tượng gắn liền / không gắn liền với những hiện tượng ấy
Tehi dhammehi ye dhammā na hetū sahetukā / ahetukā = Những hiện tượng không phải là gốc rễ nhưng có / và không có những hiện tượng ấy làm gốc rễ
Tehi dhammehi ye dhammā sahetukā / sampayuttā / sāsavā (saṃyojaniyā, ganthaniyā), te dhamme ṭhapetvā = Trong số những hiện tượng có những hiện tượng ấy làm gốc rễ / gắn liền với những hiện tượng ấy / là đối tượng của những hiện tượng ấy, ngoại trừ những hiện tượng ấy,
Tehi dhammehi ye dhammā vippayuttā sāsavā kusalākusalābyākatā dhammā … = Các hiện tượng thiện, bất thiện và không xác định về mặt đạo đức, không gắn liền với những hiện tượng ấy, là đối tượng của ô nhiễm, …
Lobho mohena hetu ceva sahetuko ca = Sự tham lam vừa là gốc rễ vừa có gốc rễ là sự si mê (hetusampayutto: … vừa gắn liền với gốc rễ là sự si mê)
alobho adoso amoho, te aññamaññaṃ hetū ceva sahetukā ca = sự không tham lam, sự không sân hận, sự không si mê, đối với nhau, chúng vừa là gốc rễ vừa có gốc rễ (… vừa gắn liền với gốc rễ)
A B-ena āsavo ceva āsavasampayutto ca = A vừa là ô nhiễm vừa gắn liền với B (fetters / ties likewise: «vừa là xiềng xích / nút thắt vừa gắn liền với B»)
Sabbāpi micchādiṭṭhi X = Mọi quan điểm sai lầm đều là X; Ṭhapetvā Y sabbāpi micchādiṭṭhi X = Ngoại trừ Y, mọi quan điểm sai lầm đều là X
Katame dhammā kenaci viññeyyā, kenaci na viññeyyā? = Những hiện tượng nào mà một loại thức nào đó có thể nhận biết, một loại thức nào đó không thể nhận biết? (Ime dhammā … = Đây là các hiện tượng mà một loại thức nào đó có thể nhận biết, một loại thức nào đó không thể nhận biết.)
Ye te dhammā A-viññeyyā, na te dhammā B-viññeyyā; ye vā pana te dhammā B-viññeyyā, na te dhammā A-viññeyyā. = Những hiện tượng mà A có thể nhận biết thì B không thể nhận biết; còn những hiện tượng mà B có thể nhận biết thì A không thể nhận biết. (A, B = mắt / tai / mũi / lưỡi / thân, as 3-01 «vật chất mà mắt có thể nhận biết»)

## Recurring lists
kāmāvacarā, rūpāvacarā, arūpāvacarā, apariyāpannā = thuộc cõi dục lạc, thuộc cõi hình sắc, thuộc cõi không hình sắc, không nằm trong các cõi tồn tại (3-01; three-sphere form without the last)
X <spheres>; vedanākkhandho … viññāṇakkhandho = X, <spheres>, tức là khối cảm giác, … (3-01 «tức là»)
vedanākkhandho…pe… viññāṇakkhandho = khối cảm giác… khối thức; rūpakkhandho = khối vật chất (new); rūpakkhandho…pe… = khối vật chất… khối thức; pañcakkhandhā = năm khối
kusalākusalābyākatā / kusalākusalā / kusalābyākatā dhammā = các hiện tượng thiện, bất thiện và không xác định về mặt đạo đức / các hiện tượng thiện và bất thiện / các hiện tượng thiện và không xác định về mặt đạo đức
kusalākusalānaṃ dhammānaṃ vipākā = các quả của các hiện tượng thiện và bất thiện (3-01); avipakkavipākānaṃ = có quả chưa chín muồi
sāsavā (before those, as a qualifier) = , là đối tượng của ô nhiễm, (matrix ^1-M2-15 (a); also in the fetter and tie groups, where the Pāli says sāsavā)
sabbeva kāmāvacarā … = Tất cả … , thuộc cõi dục lạc
taṃsampayutto vedanākkhandho … = những gì gắn liền với chúng / với nó, tức là khối cảm giác, … («chúng» after a plural antecedent: roots, fetters, vitakkavicārā, maggaṅgāni; «nó» after a singular one: a feeling, vicāra, pīti, sukha, upekkhā, sammādiṭṭhi, vīmaṃsā)
taṃsamuṭṭhānaṃ kāyakammaṃ, vacīkammaṃ, manokammaṃ = những gì do chúng sinh ra, tức là nghiệp bằng thân, nghiệp bằng lời nói, nghiệp bằng ý (samuṭṭhāna = do … sinh ra, matrix ^1-M2-60)
tadekaṭṭhā ca kilesā = và các phiền não cùng hiện diện với chúng; tadekaṭṭho lobho, doso, moho = sự tham lam, sự sân hận, sự si mê cùng hiện diện với chúng
Tīṇi kusalamūlāni – alobho, adoso, amoho = Ba gốc rễ thiện – sự không tham lam, sự không sân hận, sự không si mê (akusala: Ba gốc rễ bất thiện – sự tham lam, sự sân hận, sự si mê)
Avaseso lobho, doso, moho = Sự tham lam, sự sân hận, sự si mê còn lại
ye ca dhammā kiriyā neva kusalā nākusalā na ca kammavipākā = và những hiện tượng mang tính chức năng, không phải thiện, không phải bất thiện, cũng không phải là quả của nghiệp (3-01)
kiriyābyākatesu dhammesu = trong các hiện tượng không xác định về mặt đạo đức, mang tính chức năng; kusalānaṃ dhammānaṃ vipākato = trong các quả của các hiện tượng thiện
sabbañca rūpaṃ, asaṅkhatā ca dhātu = và toàn bộ vật chất; và yếu tố không do điều kiện tạo thành (3-01)
yañca rūpaṃ (na) kammassa katattā = và loại vật chất (không) sinh ra do nghiệp đã được tạo (3-02); … uppajjissati = và loại vật chất sẽ sinh khởi do nghiệp đã được tạo
yañca rūpaṃ anidassanaṃ appaṭighaṃ dhammāyatanapariyāpannaṃ = và loại vật chất không thấy được và không có tính va chạm, nằm trong lĩnh vực đối tượng của ý (3-02)
Apariyāpannā maggā ca, maggaphalāni ca, asaṅkhatā ca dhātu = Các con đường không nằm trong các cõi tồn tại, các thành quả của con đường, và yếu tố không do điều kiện tạo thành
Cattāro maggā apariyāpannā = Bốn con đường không nằm trong các cõi tồn tại
heṭṭhimāni ca tīṇi sāmaññaphalāni = và ba thành quả thấp hơn của đời sống sa-môn; Upariṭṭhimaṃ arahattaphalaṃ = Thành quả cao nhất, tức là thành quả A-la-hán
<X>bhūmiyaṃ kāmāvacare, rūpāvacare, … = Ở cấp độ có X, thuộc cõi dục lạc, thuộc cõi hình sắc, … (savitakkasavicāra- / avitakkavicāramatta- / avitakkaavicārabhūmiyaṃ = Ở cấp độ + matrix triad 6 predicate)
Sukhabhūmiyaṃ = Ở cấp độ có cảm giác dễ chịu (^1-988, triad 2, sukhā vedanā) / Ở cấp độ có hạnh phúc (^1-1004, triad 7, the factor): split by role as the core terms and the approved English
Paritte (etc.) dhamme ārabbha ye uppajjanti cittacetasikā dhammā = Tâm và các yếu tố đồng hành với tâm sinh khởi khi lấy <M.BARE> làm đối tượng (ārabbha as the sample's «… làm đối tượng»)
Ariyamaggaṃ adhipatiṃ karitvā = khi lấy con đường cao quý làm yếu tố chủ đạo; ariyamaggasamaṅgissa = Ở người có được con đường cao quý; vīmaṃsādhipateyyaṃ maggaṃ bhāvayantassa = đang tu tập con đường với sự thẩm xét làm yếu tố chủ đạo
maggaṅgāni = các chi phần của con đường; sammādiṭṭhi maggo ceva hetu ca = quan điểm đúng đắn vừa là con đường vừa là gốc rễ
Pañca kammāni ānantarikāni, yā ca micchādiṭṭhiniyatā = Năm nghiệp có quả không gián đoạn, và quan điểm sai lầm cố định
jātā bhūtā sañjātā nibbattā abhinibbattā pātubhūtā uppannā samuppannā uṭṭhitā samuṭṭhitā = đã sinh ra, đã thành, đã sinh thành, đã phát sinh, đã phát sinh rõ rệt, đã hiện ra, đã sinh khởi, đã sinh khởi trọn vẹn, đã trỗi dậy, đã trỗi dậy trọn vẹn (negatives with «chưa»)
atītā niruddhā vigatā vipariṇatā atthaṅgatā abbhatthaṅgatā uppajjitvā vigatā = thuộc quá khứ, đã chấm dứt, đã mất đi, đã biến đổi, đã biến mất, đã biến mất hoàn toàn, đã mất đi sau khi sinh khởi
X Xaṃsena saṅgahitā = X, được xếp vào phần X (đã sinh khởi / chưa sinh khởi / quá khứ / tương lai / hiện tại)
rūpaṃ, vedanā, saññā, saṅkhārā, viññāṇaṃ = vật chất, cảm giác, tri giác, các sự tạo tác, thức
tesaṃ tesaṃ sattānaṃ ajjhattaṃ paccattaṃ niyatā pāṭipuggalikā upādiṇṇā = của từng chúng sinh, vốn ở bên trong, riêng từng người, cố hữu, thuộc về cá nhân, do nghiệp tạo ra (niyatā here = cố hữu, not «cố định»); parasattānaṃ parapuggalānaṃ = của từng chúng sinh khác, từng người khác
Cattāro ca mahābhūtā catunnañca mahābhūtānaṃ upādāya rūpaṃ = Bốn yếu tố cơ bản và vật chất phái sinh từ bốn yếu tố cơ bản (3-01)
cittacetasikā dhammā = tâm và các yếu tố đồng hành với tâm

## Strings
Dukkhe ñāṇaṃ … idappaccayatā paṭiccasamuppannesu dhammesu ñāṇaṃ = hiểu biết về khổ đau, hiểu biết về sự phát sinh của khổ đau, hiểu biết về sự chấm dứt khổ đau, hiểu biết về cách thực hành dẫn đến sự chấm dứt khổ đau, hiểu biết về quá khứ, hiểu biết về tương lai, hiểu biết về cả quá khứ lẫn tương lai, hiểu biết về quy luật tùy thuộc vào điều kiện và các hiện tượng sinh khởi tùy thuộc vào điều kiện (aññāṇaṃ = sự không biết về …, the first word of the 2-04 moha string)
dukkha (truth) = khổ đau; samudaya = sự phát sinh; nirodha = sự chấm dứt; paṭipadā = cách thực hành (2-03); pubbanta / aparanta = quá khứ / tương lai (matrix ^1-M2-114)
paññā string + dhammavicayasambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ = sample string + «, chi phần giác ngộ là sự tìm hiểu các hiện tượng, chi phần của con đường, thuộc về con đường» (2-03)
metti mettāyanā mettāyitattaṃ anuddā anuddāyanā anudāyitattaṃ hitesitā anukampā = lòng từ ái, sự khởi lòng từ ái, trạng thái khởi lòng từ ái, lòng thương mến, sự khởi lòng thương mến, trạng thái khởi lòng thương mến, sự mong muốn điều lợi ích, lòng thương xót (inserted after the third word of the sample adosa string)
adoso adussanā adussitattaṃ…pe… abyāpādo … = sự không sân hận, sự không khởi sân, trạng thái không khởi sân… sự không ác ý, …
lobha string (rāgo … akusalamūlaṃ, 102 items) = sự tham đắm, sự say đắm, sự chiều theo, sự xuôi theo, sự thích thú, sự tham đắm thích thú, sự say đắm của tâm, … khao khát dục lạc, khao khát được hiện hữu, khao khát không còn hiện hữu, khao khát hình sắc, khao khát không hình sắc, khao khát sự chấm dứt, khao khát hình sắc, … dòng lũ, ách, nút thắt, sự bám víu, … khuynh hướng tiềm ẩn, sự ám ảnh, dây leo, sự bủn xỉn, … sự thèm muốn, sự tham lam, gốc rễ bất thiện (full list: build_4-01_vi.LOBHA_ITEMS). rāga = sự tham đắm (2-03), sārāga = sự say đắm (2-04), nandī = sự thích thú, icchā = sự mong muốn, mucchā = sự mê đắm, ajjhosāna = sự đắm chìm, gedha = sự thèm khát, sineha = sự luyến ái, āsā = sự mong mỏi, jappā = sự thèm thuồng, loluppa = sự ham hố, paṇidhi = sự mong cầu (appaṇihita, 2-03), rūpataṇhā (both times) = khao khát hình sắc, vevicchaṃ = sự bủn xỉn (also in the macchariya string), Māra = Ma vương
dosa opening (anatthaṃ me acarīti āghāto jāyati …) = Sự oán giận khởi lên khi nghĩ “Người ấy đã gây hại cho ta”, … “Người ấy đã gây hại cho người mà ta yêu quý và ưa thích… đang gây hại… sẽ gây hại”, … hoặc sự oán giận khởi lên một cách vô cớ. (āghāta = sự oán giận; piya / manāpa = yêu quý / ưa thích)
dosa string (cittassa āghāto … kujjhitattaṃ + the 2-04 string) = sự oán giận của tâm, sự phẫn uất, sự ác cảm, sự đối nghịch, sự nổi nóng, sự nổi nóng dữ dội, sự nổi nóng tột độ, sự sân hận, sự sân hận dữ dội, sự sân hận tột độ, sự thù hằn của tâm, sự sân hận dữ dội trong ý, sự giận dữ, sự khởi giận, trạng thái khởi giận, + 2-04 dosa string (paṭigha = sự ác cảm, 2-04; paṭivirodha = sự đối nghịch, byāpatti = sự thù hằn as in the 2-04 string; kopa = sự nổi nóng, kodha = sự giận dữ)
diṭṭhi string = the 2-04 string (patiṭṭhāho / paṭiggāho both «sự bám chặt»); diṭṭhivisūkāyikaṃ [diṭṭhivisūkāyitaṃ (sī.)] = sự quanh co của quan điểm [khác chính tả (Sī.): diṭṭhivisūkāyitaṃ]
kaṅkhā string = the 2-04 vicikicchā string
Satthari … kaṅkhati vicikicchati = Người ta nghi ngờ và hoài nghi về Bậc Đạo Sư, … về Giáo Pháp, … về Tăng đoàn, … về sự tu học, … về quá khứ, … về tương lai, … về cả quá khứ lẫn tương lai, … về quy luật tùy thuộc vào điều kiện và các hiện tượng sinh khởi tùy thuộc vào điều kiện
Idha assutavā puthujjano … rūpaṃ attato samanupassati … = Ở đời này, người phàm phu không được học hỏi, không gặp gỡ các bậc thánh, không thông thạo Giáo Pháp của các bậc thánh, không được rèn luyện trong Giáo Pháp của các bậc thánh, không gặp gỡ những người chân chính, … xem vật chất là tự ngã, hoặc xem tự ngã là có vật chất, hoặc xem vật chất ở trong tự ngã, hoặc xem tự ngã ở trong vật chất. Người ấy xem cảm giác là tự ngã, … (attā = tự ngã; sappurisa = người chân chính)
Ito bahiddhā samaṇabrāhmaṇānaṃ sīlena suddhi … = Các sa-môn và bà-la-môn bên ngoài Giáo Pháp này cho rằng “Trong sạch nhờ giới hạnh, trong sạch nhờ nghi thức, trong sạch nhờ giới hạnh và nghi thức” (suddhi = trong sạch, as visuddhi; vata = nghi thức)
ten views = “Thế giới là trường tồn”, hoặc “Thế giới không trường tồn”, hoặc “Thế giới là hữu hạn”, hoặc “Thế giới là vô hạn”, hoặc “Linh hồn và thân thể là một”, hoặc “Linh hồn là một, thân thể là khác”, hoặc “Như Lai còn tồn tại sau khi chết”, hoặc “Như Lai không còn tồn tại sau khi chết”, hoặc “Như Lai vừa còn tồn tại vừa không còn tồn tại sau khi chết”, hoặc “Như Lai không phải còn tồn tại cũng không phải không còn tồn tại sau khi chết” (sassata = trường tồn, antavā = hữu hạn as matrix ^1-M2-112 / 113; jīva = linh hồn; tathāgata = Như Lai)
idameva saccaṃ moghamaññaṃ = chỉ điều này là sự thật, mọi điều khác đều sai (views joined by «; hoặc »)
Yo kāmesu kāmacchando … kāmajjhosānaṃ = Bất cứ điều gì, đối với các dục lạc, là ý muốn dục lạc, sự tham đắm dục lạc, sự thích thú dục lạc, khao khát dục lạc, sự luyến ái dục lạc, sự nóng bỏng của dục lạc, sự mê đắm dục lạc, sự đắm chìm trong dục lạc
Yo bhavesu bhavachando … = Bất cứ điều gì, đối với sự hiện hữu, là ý muốn hiện hữu, sự tham đắm hiện hữu, sự thích thú hiện hữu, khao khát được hiện hữu (matrix ^1-M2-110 (b)), sự luyến ái hiện hữu, sự nóng bỏng của hiện hữu, sự mê đắm hiện hữu, sự đắm chìm trong hiện hữu
māna (Seyyohamasmīti māno …) = Sự kiêu mạn “Ta hơn người”, sự kiêu mạn “Ta bằng người”, sự kiêu mạn “Ta kém người”. … sự kiêu mạn, sự tự đánh giá mình, trạng thái tự đánh giá mình, sự tự cao, sự vênh vang, ngọn cờ, sự tự đề cao, sự mong muốn của tâm được giương cờ
issā string = sự ganh tị đối với lợi lộc, sự tôn vinh, sự kính trọng, sự quý trọng, sự đảnh lễ và sự cúng dường mà người khác nhận được, sự khởi ganh tị, trạng thái khởi ganh tị, sự đố kỵ, sự khởi đố kỵ, trạng thái khởi đố kỵ (usūyā = sự đố kỵ)
macchariya = Năm loại keo kiệt – keo kiệt về chỗ ở, … về gia đình, … về lợi lộc, … về lời khen, … về Giáo Pháp. … sự keo kiệt, sự khởi keo kiệt, trạng thái khởi keo kiệt, sự bủn xỉn, sự hà tiện, sự bo bo, trạng thái khép chặt của tâm

## Defilement names
sakkāyadiṭṭhi = quan điểm về tự ngã; vicikicchā = sự hoài nghi (2-04); sīlabbataparāmāsa = sự hiểu sai lệch về giới hạnh và nghi thức (parāmāsa = sự hiểu sai lệch, core; sīla = giới hạnh)
tīṇi / dasa saṃyojanāni = ba / mười xiềng xích; cattāro āsavā = bốn loại ô nhiễm; cattāro ganthā = bốn nút thắt
kāmāsava / bhavāsava / diṭṭhāsava / avijjāsava = ô nhiễm dục lạc / ô nhiễm hiện hữu / ô nhiễm quan điểm / ô nhiễm vô minh (as «dòng lũ vô minh», «xiềng xích quan điểm» in the 2-04 strings)
X-saṃyojanaṃ = xiềng xích X: tham đắm dục lạc / ác cảm / kiêu mạn / quan điểm / hoài nghi / hiểu sai lệch về giới hạnh và nghi thức / tham đắm hiện hữu / ganh tị / keo kiệt / vô minh
X kāyagantho = nút thắt của thân bằng X: sự thèm muốn / sự ác ý / sự hiểu sai lệch về giới hạnh và nghi thức / sự cố chấp rằng “chỉ điều này là sự thật” (idaṃsaccābhiniveso; abhinivesa = sự cố chấp, 2-04)
bhavarāga = sự tham đắm hiện hữu; issā = sự ganh tị; macchariya = sự keo kiệt; micchādiṭṭhi = quan điểm sai lầm (2-04)

## Choices to review
«Tikaṃ.» = «Các bộ ba.» here vs «Phân loại theo nhóm ba.» in 3-01 (closing different sections).
Sukhabhūmiyaṃ split (^1-988 «có cảm giác dễ chịu» / ^1-1004 «có hạnh phúc»), as the approved English; the Russian uses one word.
kāyagantha = «nút thắt của thân bằng X» (keeps the class noun of the matrix and avoids «là» inside the names of the «X là gì?» frame).
bhava = «hiện hữu» in the āsava / fetter names («ô nhiễm hiện hữu», «xiềng xích tham đắm hiện hữu»).
āsava pairs: «A vừa là ô nhiễm vừa gắn liền với B» (B names the taint); root pairs keep «… gắn liền với gốc rễ là B».
ānantarika = «có quả không gián đoạn».

## Source points translated as written
^1-1022: the question reads «neva ācayagāmi na apacayagāmino» (matrix: nevācayagāmināpacayagāmino); the matrix question (triad 10 (c)) is used.
^1-1106, ^1-1123, ^1-1128, ^1-1143, ^1-1144: a Devanāgarī visarga «ः» stands where a punctuation mark belongs; rendered as «;».
^1-1124, ^1-1143, ^1-1144: «patiṭṭhāho» in the diṭṭhi string (^1-1007 / ^1-1009 have paṭiggāho); the 2-04 string is used, which renders patiṭṭhāho «sự bám chặt» (= paṭiggāho).
^1-1142: «acarī ti» (stray space); same Vietnamese as ^1-1066.
^1-1041: «[rūpā (bahūsu)]» = «[dị bản (nhiều ấn bản): rūpā]» (number differs); ^1-1024 «[uparimaṃ (syā.)]» = dị bản (another word form).
^1-1130, 1135, 1138, 1146, 1151, 1154: the fetter and tie groups say «sāsavā» (subject to taints); kept («là đối tượng của ô nhiễm»).
^1-1108 lacks «sāsavā» before kusalākusalābyākatā (unlike ^1-1099 / ^1-1130); nothing added.
^1-1077: «Ime cha apariyāpannahetū – ime dhammā hetū.» translated as written.
^1-1039: «maggaṅgāni ṭhapetvā; taṃsampayutto …» kept with the semicolon.
^1-1019 «kāmāvacarā rūpāvacarā,», ^1-1059 «kāmāvacarahetū cha», ^1-1101 «kāyaviññeyyā na te», ^1-1107 «apariyāpannā vedanākkhandho», ^1-1149 / 1107 «rūpaṃ asaṅkhatā»: missing punctuation in the Pāli; normal Vietnamese punctuation. The Pāli's alternating «,» / «;» before the aggregates and before «sabbañca rūpaṃ» is rendered uniformly («, tức là …», «; và toàn bộ vật chất; và …»).
^1-1010 «kāyakammaṃ vacīkammaṃ manokammaṃ» without commas: same Vietnamese as elsewhere.
