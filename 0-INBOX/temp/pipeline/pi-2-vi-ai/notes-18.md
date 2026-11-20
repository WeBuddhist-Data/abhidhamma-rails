# pi-2 Vietnamese zero-shot, chapter 18 (Dhammahadayavibhaṅga): new terms and formulas

Builder: build_18_vi.py (imports build_17_vi and through it S, B, T, F …; F.add_item extends T's item tables in memory only; writes only 18-dhammahadayavibhango.md; `--dry` writes nothing). Every non-empty Pāli line is matched in order against a key; the Pañhāpucchaka-type lines go through one parser (subject chains + matrix predicates), unknown Pāli raises KeyError. Asserted at build time: base / element / truth / faculty names in the ch2-5 outputs, pi-1 ^1-70 (nutriments), ^1-1059 / ^1-1060 / ^1-1064 / ^1-1068 / ^1-1077 (roots), 5-atthakatha «gốc rễ là quả của nghiệp», ^1-990 (realm words), ^1-1287 … ^1-1294 (realm definitions), ^1-1291 (formless gods), the pi-1 colophon, the human-count sums. Identity check: 104 Pāli sentences shared with ch1-17 get byte-identical Vietnamese (0 different). Scratch: probe_18_vi.py.
Format: Pāli = tiếng Việt, one per line. [pi-1] = pi-1 Vietnamese rails; [chN] = earlier pi-2 groups; [new] = settled here.

## Reused
khandha / āyatana / dhātu / sacca / indriya names = S / T / F strings (khối …, lĩnh vực …, yếu tố …, sự thật về …, năng lực …) [ch1-5]
Pañhāpucchaka predicates (kusala, vedanā, vipāka, upādinna, vitakka, rūpa, lokiya, sārammaṇa, pariyāpanna) = B / T items; «thì» after a single truth / faculty (F rule) [ch1-5]
cakkhusamphasso … = sự tiếp xúc của mắt …; manodhātusamphasso / manoviññāṇadhātusamphasso = sự tiếp xúc của yếu tố ý / của yếu tố ý thức [ch4, ch1 words]
X-samphassajā vedanā / saññā / cetanā = cảm giác / tri giác / chủ ý sinh từ sự tiếp xúc của … (B.SUBJ) [ch1]
Kabaḷīkāro āhāro / phassāhāro / manosañcetanāhāro / viññāṇāhāro = thức ăn / sự tiếp xúc / chủ ý của ý / thức trong vai trò dưỡng chất [pi-1 ^1-70, sample]
kusala- / akusala- / abyākatahetu (counted) = gốc rễ thiện / bất thiện / không xác định về mặt đạo đức [pi-1 ^1-1059]
Kusalānaṃ (vā) dhammānaṃ vipākato (kiriyābyākatesu vā dhammesu) alobho, adoso, amoho = pi-1 ^1-1068 / ^1-1077 [pi-1]
Bhūmantaradassanavāra (Katame dhammā kāmāvacarā? … apariyāpannā?) = pi-1 ^1-1287 … ^1-1294, pi-1 variants dropped, the five aggregates written out in ^1-1293 [pi-1]
avīciniraya = địa ngục Vô Gián; paranimmitavasavattī = Tha Hóa Tự Tại; brahmaloka = cõi Phạm Thiên; akaniṭṭha = Sắc Cứu Cánh; X-āyatanūpagā devā = chư thiên sinh vào lĩnh vực … [pi-1]
opapātika = hóa sinh [pi-1]; peta = ngạ quỷ; tiracchānagata = loài súc sinh; niraya = địa ngục; duggati = cõi xấu [ch16]
ñāṇasampayutta / ñāṇavippayutta = gắn liền với hiểu biết / không gắn liền với hiểu biết [pi-1]; sahetuka / ahetuka = có gốc rễ / không có gốc rễ [pi-1 matrix]
paritta / majjhima / paṇīta (jhāna bhāvetvā) = ở mức hạn hẹp / trung bình / ưu việt [pi-1 matrix words]
Colophon: Vibhaṅgapakaraṇaṃ niṭṭhitaṃ. = Bộ “Phân tích các hiện tượng” đã hoàn tất. [pi-1 pattern]; Dhammahadayavibhaṅgo niṭṭhito. = Phân tích cốt lõi của các hiện tượng đã hoàn tất. [sample]

## New: names
kāmadhātu / rūpadhātu / arūpadhātu (plane) = cõi dục lạc / cõi hình sắc / cõi không hình sắc (the element rūpadhātu stays «yếu tố hình sắc»)
apariyāpanne (plane, locative) = trong phần không nằm trong các cõi tồn tại; heading Apariyāpannaṃ = Phần không nằm trong các cõi tồn tại
X-dhātupariyāpanna / na … = nằm trong cõi … / không nằm trong cõi …
counted units: khandhā = khối; āyatanāni = lĩnh vực nhận biết (subjects in the Pañhāpucchaka: «lĩnh vực», ch2); dhātuyo = yếu tố; saccāni = sự thật; indriyāni = năng lực; hetū = gốc rễ; āhārā = loại dưỡng chất; phassā = loại tiếp xúc; vedanā / saññā / cetanā = loại cảm giác / tri giác / chủ ý; cittāni / cittā = loại tâm
kāyaviññāṇadhātusamphasso = sự tiếp xúc của yếu tố thức qua thân
alobho kusalahetu = sự không tham lam trong vai trò gốc rễ thiện (likewise akusalahetu; vipākahetu = … trong vai trò gốc rễ là quả của nghiệp; «trong vai trò» as pi-1 kabaḷīkāro āhāro, avoids «là … là»)
upapattikkhaṇa = khoảnh khắc tái sinh; pātubhavati = xuất hiện; sabbesaṃ / kassaci / kassa / etesaṃ = ở tất cả chúng sinh / ở một số chúng sinh / ở những ai / ở những chúng sinh ấy
kassaci ahetukā pātubhavanti = ở một số chúng sinh, sự xuất hiện không có gốc rễ; aparāni / aparā = … khác
kāmāvacarā devā = chư thiên thuộc cõi dục lạc; paṭhamakappikā manussā = loài người ở thời kỳ đầu của kiếp; gabbhaseyyakā sattā = những chúng sinh sinh ra từ bào thai; nerayika = chúng sinh địa ngục; paripuṇṇāyatana = có đầy đủ các lĩnh vực nhận biết; jaccandha / jaccabadhira / jaccandhabadhira = mù / điếc / vừa mù vừa điếc bẩm sinh; napuṃsaka = không có giới tính; asura = a-tu-la
asaññasattā devā = chư thiên Vô Tưởng (heading Asaññasattā = Chúng sinh Vô Tưởng); ahetukā anāhārā aphassakā … acittakā = mà không có gốc rễ, không có dưỡng chất, … không có tâm
god names (traditional, as pi-1 Tha Hóa Tự Tại / Sắc Cứu Cánh): Tứ Đại Thiên Vương, Ba Mươi Ba, Dạ Ma, Đâu Suất, Hóa Lạc, Tha Hóa Tự Tại, Phạm Chúng, Phạm Phụ, Đại Phạm, Thiểu Quang, Vô Lượng Quang, Quang Âm, Thiểu Tịnh, Vô Lượng Tịnh, Biến Tịnh, Vô Tưởng, Quảng Quả, Vô Phiền, Vô Nhiệt, Thiện Hiện, Thiện Kiến
sammuti- / upapatti- / visuddhidevā = chư thiên theo quy ước / do tái sinh / do sự trong sạch; X nāma – = X nghĩa là –
X-ānaṃ sahabyataṃ upapajjanti = tái sinh vào cộng đồng của X; appekacce = một số người; khattiya- / brāhmaṇa- / gahapatimahāsāla = những người quý tộc / những bà-la-môn / những gia chủ giàu có
dānaṃ datvā, sīlaṃ samādiyitvā, uposathakammaṃ katvā = sau khi bố thí, thọ trì giới hạnh, thực hiện việc giữ ngày trai giới
āyuppamāṇa = tuổi thọ; kittakaṃ? = là bao nhiêu?; rattindiva = một ngày một đêm; tāya rattiyā tiṃsa rattiyo māso = ba mươi đêm như thế là một tháng; dvādasamāsiyo saṃvaccharo = mười hai tháng như thế là một năm; dibba (vassa) = (năm) cõi trời; manussānaṃ gaṇanāya = theo cách tính của loài người
human-count totals computed into Vietnamese numerals (as the English / Russian rails): chín triệu … chín tỷ hai trăm mười sáu triệu năm; verse total 12 285 000 000 (mười hai tỷ năm, cùng hai trăm tám mươi triệu năm; thêm năm triệu năm)
kappassa tatiyo bhāgo / upaḍḍhakappo = một phần ba kiếp / nửa kiếp
ārammaṇa- / manasikāra- / chanda- / paṇidhi- / adhimokkha- / abhinīhāra- / paññānānattatā = do sự khác biệt về đối tượng, về sự chú tâm, về ý muốn, về sự mong cầu, về sự quyết định, về sự định hướng, về trí tuệ
mahesi = bậc Đại Hiền; bhavagga = đỉnh cao của sự hiện hữu; nibbānogadhagāmin = dẫn sâu vào Niết-bàn; parinibbanti = nhập Niết-bàn trọn vẹn

## New: predicates (Abhiññeyyādi / Sārammaṇa / Diṭṭhasutādi)
abhiññeyya / pariññeyya = cần được hiểu biết trực tiếp / cần được hiểu biết trọn vẹn
pahātabba / bhāvetabba / sacchikātabba = cần được dứt bỏ / cần được tu tập / cần được tự mình chứng nghiệm; na … = không cần được …
sārammaṇārammaṇa / anārammaṇārammaṇa = lấy những gì có đối tượng làm đối tượng / lấy những gì không có đối tượng làm đối tượng
diṭṭha / suta / muta / viññāta (predicate) = được thấy / được nghe / được cảm nhận / được nhận biết; na … = không được … (no conjunction added before a positive item)
na vattabbā Xtipi, Ytipi (no dash, no quotes in this chapter) = (thì) không nên nói rằng X, hay rằng Y [ch9 rule]
Tayo kusalahetū kusalā = Ba gốc rễ thiện thì thiện («thì» when the predicate repeats the subject's last word)

## New: headings and frames
Sabbasaṅgāhikavāro = Mục bao gồm tất cả; Uppattānuppattivāro = Mục về những gì sinh khởi và không sinh khởi; Pariyāpannāpariyāpannavāro = Mục về những gì nằm trong và không nằm trong; Dhammadassanavāro = Mục trình bày các hiện tượng; Bhūmantaradassanavāro = Mục trình bày sự khác biệt giữa các cõi; Uppādakakammaāyuppamāṇavāro = Mục về nghiệp tạo ra sự tái sinh và tuổi thọ; Abhiññeyyādivāro = Mục về những gì cần được hiểu biết trực tiếp và các điều khác; Sārammaṇānārammaṇavāro = Mục về những gì có đối tượng và không có đối tượng; Diṭṭhasutādidassanavāro = Mục trình bày những gì được thấy, được nghe và các điều khác; Tikādidassanavāro = Mục trình bày các bộ ba và các bộ khác
##### Pariyāpannāpariyāpannaṃ = Nằm trong và không nằm trong các cõi tồn tại; Uppādakakammaṃ = Nghiệp tạo ra sự tái sinh; Āyuppamāṇaṃ = Tuổi thọ
Kusalattikaṃ / Vedanātikaṃ / Vipākattikaṃ / Upādinnattikaṃ / Vitakkattikaṃ = Bộ ba về thiện / về cảm giác / về quả của nghiệp / về những gì do nghiệp tạo ra / về sự hướng tâm; Rūpadukaṃ / Lokiyadukaṃ = Bộ đôi về vật chất / về thế gian
Kati khandhā, …? = Có bao nhiêu khối, …?; Kāmadhātuyā kati khandhā …? = Trong cõi dục lạc có bao nhiêu khối …?; Kāmadhātuyā pañcakkhandhā, … = Trong cõi dục lạc có năm khối, …
Tattha katame kāmadhātuyā pañcakkhandhā? … – ime vuccanti "…" = Ở đây, năm khối trong cõi dục lạc là gì? … – đó được gọi là “năm khối trong cõi dục lạc”
– ime tayo kusalahetū = – đó là ba gốc rễ thiện (pi-1 ^1-1068 «– đó là ba gốc rễ …»)
Pañcannaṃ khandhānaṃ kati X…pe… sattannaṃ cittānaṃ kati X? = Trong năm khối, bao nhiêu khối X… trong bảy loại tâm, bao nhiêu loại tâm X?
Kāmadhātuyā upapattikkhaṇe kassa N pātubhavanti? = Trong cõi dục lạc, vào khoảnh khắc tái sinh, N xuất hiện ở những ai?; answer «Vào khoảnh khắc tái sinh của X, N xuất hiện – …. Trong cõi dục lạc, vào khoảnh khắc tái sinh, N này xuất hiện ở những chúng sinh ấy.»
… katame N pātubhavanti? = …, N nào xuất hiện (ở tất cả chúng sinh)?
uddāna "Abhiññā dve sārammaṇā, …" = Cần được hiểu biết trực tiếp, hai mục về đối tượng, được thấy, thiện, cảm giác; / Quả của nghiệp và do nghiệp tạo ra, sự hướng tâm, vật chất, thuộc thế gian.

## Variant brackets
[kabaḷiṃkāro āhāro (sī. syā.)], [sammatidevā (syā.)], [cātummahārājike (sī. syā.)] = khác chính tả; [rattidivo (ka.) a. ni. 3.71] = [khác chính tả (Ka.): rattidivo; a. ni. 3.71]
[keci (syā.)], [avasesā sattā (?)], [chapi te (syā.)], [eko kappo (syā.)], [bhavaggaṃ vāpi (syā.)], [puna gacchanti (syā.)] = dị bản; [appaṃ vā bhiyyo vā (syā. ka.) dī. ni. 2.7] = [dị bản (Syā., Ka.): appaṃ vā bhiyyo vā; dī. ni. 2.7]

## Review points
kāmadhātu / rūpadhātu / arūpadhātu as planes = «cõi …» here; ch3 has «yếu tố dục lạc» for kāmadhātu (the element of sensuality, also defined there by the realm).
Traditional god names (Sino-Vietnamese) follow pi-1 «Tha Hóa Tự Tại», «Sắc Cứu Cánh»; asaññasatta «Vô Tưởng».
Human-count totals computed (chín triệu năm …) rather than literal «chín mươi trăm nghìn năm».
abhiññeyya … sacchikātabba with «cần được …» (passive) vs the matrix «cần dứt bỏ bằng …».

## Pāli slips (all reported; printed by the builder)
Kept as written: ^2-1031 "Tīṇindriyā … siyā na bhāvetabbā, sacchikātabbā" (a "na" looks missing) = «đôi khi không cần được tu tập, cần được tự mình chứng nghiệm»; ^2-1039 "Moho akusalahetu … siyā dukkhamasukhāya vedanāya sampayutto" (a- missing) = «gắn liền với cảm giác khó chịu và không dễ chịu»; ^2-1041 stray digit "anupādinnupādāniyo 4." = «… 4.»; ^2-994 "Ime vuccanti rūpadhātuyā aṭṭha hetū." unquoted; ^2-1004 "Tīṇi saccāni na arūpadhātupariyāpannāni." on its own line.
Rendered as meant (spelling / punctuation only): ^2-992 "vuccatti", "Cakkhusamphasso sotasamphasso"; ^2-1000 "kāmadhātu pariyāpanno"; ^2-1009 … ^2-1012 comma missing between "tiracchānagatānaṃ" and "nerayikānaṃ"; ^2-1012 "kāyindriyaṃ manindriyaṃ"; ^2-1014 question closed with "."; ^2-1023 verse question "kittako." = «?»; ^2-1035, ^2-1040, ^2-1042 commas missing; ^2-1042 "avitakkaavicārā manodhātu"; ^2-1043 "satta cetanā satta cittā" (ellipsis); ^2-1039 "sampayuttoti pi"; closing "ti" dropped (^2-1023, ^2-1028, ^2-1029, ^2-1044).
