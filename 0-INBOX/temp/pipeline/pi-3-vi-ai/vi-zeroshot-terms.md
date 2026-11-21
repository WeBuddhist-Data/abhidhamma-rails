# pi-3 Dhātukathā: Vietnamese plain zero-shot, binding terms (from the sample: preamble, ch1, ch2)

Format: Pāli = tiếng Việt, one per line. Tags: [pi-1] / [pi-2] = verbatim from the reviewed pi-1 / pi-2 Vietnamese rails text (or their termbases / APPROVED.md); [pi-1 words] / [pi-2 words] = built only from words of that book; [new] = settled here for pi-3.
Reuse every string verbatim: `import build_sample_vi as B` (sys.path.insert the pi-3-vi-ai folder; importing writes nothing). `python -I -X utf8 build_sample_vi.py` asserts that every [pi-1] / [pi-2] string still occurs in those rails files, then rebuilds the sample.
vietnamese-style.md applies unchanged (dash rule, “…” / ‘…’, variant brackets, sati = «sự tỉnh thức»).

## 1. Book frame

Namo tassa bhagavato arahato sammāsambuddhassa = Kính lễ Đức Thế Tôn, bậc A-la-hán, bậc Tự Giác Ngộ Hoàn Toàn [pi-1]
# Abhidhammapiṭake = # Tạng Vi Diệu Pháp [pi-1]
## Dhātukathāpāḷi = ## Thảo luận về các yếu tố [new, proposal; pairs with «Liệt kê các hiện tượng», «Phân tích các hiện tượng»; mid-sentence “Thảo luận về các yếu tố”]
Dhātukathāpāḷi, alternative 1 = Bàn về các yếu tố [new]
Dhātukathāpāḷi, alternative 2 = Luận giải về các yếu tố [new]
Dhātukathāpakaraṇaṃ niṭṭhitaṃ. = Bộ “Thảo luận về các yếu tố” đã hoàn tất. [pi-1 ^1-1616 / pi-2 ^2-1044 pattern] (B.BOOK_END)
dhammasaṅgaṇī (the book, ^3-5) = “Liệt kê các hiện tượng” [pi-1]
dhātukathā (the book, ^3-5) = “Thảo luận về các yếu tố” [new]
vibha. (citation in a variant bracket) = Phân tích các hiện tượng [pi-2]

## 2. Chapter headings (### level)

### Uddeso = ### Phần nêu đề mục [pi-1 Rūpakaṇḍa ^1-2-1-0]
naya = phương pháp [new]
### Paṭhamanayo = ### Phương pháp thứ nhất [new]
### Dutiyanayo = ### Phương pháp thứ hai [new]
### Tatiyanayo = ### Phương pháp thứ ba [new]
### Catutthanayo = ### Phương pháp thứ tư [new]
### Pañcamanayo = ### Phương pháp thứ năm [new]
### Chaṭṭhanayo = ### Phương pháp thứ sáu [new]
### Sattamanayo = ### Phương pháp thứ bảy [new]
### Aṭṭhamanayo = ### Phương pháp thứ tám [new]
### Navamanayo = ### Phương pháp thứ chín [new]
### Dasamanayo = ### Phương pháp thứ mười [new]
### Ekādasamanayo = ### Phương pháp thứ mười một [new]
### Dvādasamanayo = ### Phương pháp thứ mười hai [new]
### Terasamanayo = ### Phương pháp thứ mười ba [new]
### Cuddasamanayo = ### Phương pháp thứ mười bốn [new]
(B.CHAPTER_TITLES: key = file number, 1 = Uddeso, 2..15 = methods 1..14; B.ORDINAL)

## 3. Section headings (#### level) and closings

#### Nayamātikā = #### Ma trận các phương pháp [new; mātikā = ma trận pi-1]
#### Abbhantaramātikā = #### Ma trận bên trong [new]
#### Nayamukhamātikā = #### Ma trận lối vào các phương pháp [new]
#### Lakkhaṇamātikā = #### Ma trận các đặc tính [new]
#### Bāhiramātikā = #### Ma trận bên ngoài [new]
padaniddeso = Giải thích đề mục về … [pi-1 niddeso «giải thích»; pada = «đề mục», pairs with Uddeso «Phần nêu đề mục»; new] (B.niddesa_heading(n))
<X>padaniddeso paṭhamo. (closing line) = Giải thích đề mục về <X>, phần thứ nhất. [new] (B.niddesa_closing(n); dutiyo … cuddasamo = phần thứ hai … phần thứ mười bốn)
#### Saṅgahāsaṅgahapadaniddeso = #### Giải thích đề mục về sự gộp vào và sự không gộp vào [new]
#### Saṅgahitenaasaṅgahitapadaniddeso = #### Giải thích đề mục về điều không được gộp vào dựa trên điều được gộp vào [new]
#### Asaṅgahitenasaṅgahitapadaniddeso = #### Giải thích đề mục về điều được gộp vào dựa trên điều không được gộp vào [new]
#### Saṅgahitenasaṅgahitapadaniddeso = #### Giải thích đề mục về điều được gộp vào dựa trên điều được gộp vào [new]
#### Asaṅgahitenaasaṅgahitapadaniddeso = #### Giải thích đề mục về điều không được gộp vào dựa trên điều không được gộp vào [new]
#### Sampayogavippayogapadaniddeso = #### Giải thích đề mục về sự gắn liền và sự không gắn liền [new]
#### Sampayuttenavippayuttapadaniddeso = #### Giải thích đề mục về điều không gắn liền dựa trên điều gắn liền [new]
#### Vippayuttenasampayuttapadaniddeso = #### Giải thích đề mục về điều gắn liền dựa trên điều không gắn liền [new]
#### Sampayuttenasampayuttapadaniddeso = #### Giải thích đề mục về điều gắn liền dựa trên điều gắn liền [new]
#### Vippayuttenavippayuttapadaniddeso = #### Giải thích đề mục về điều không gắn liền dựa trên điều không gắn liền [new]
#### Saṅgahitenasampayuttavippayuttapadaniddeso = #### Giải thích đề mục về điều gắn liền và điều không gắn liền dựa trên điều được gộp vào [new]
#### Sampayuttenasaṅgahitāsaṅgahitapadaniddeso = #### Giải thích đề mục về điều được gộp vào và điều không được gộp vào dựa trên điều gắn liền [new]
#### Asaṅgahitenasampayuttavippayuttapadaniddeso = #### Giải thích đề mục về điều gắn liền và điều không gắn liền dựa trên điều không được gộp vào [new]
#### Vippayuttenasaṅgahitāsaṅgahitapadaniddeso = #### Giải thích đề mục về điều được gộp vào và điều không được gộp vào dựa trên điều không gắn liền [new]
##### Khandho = ##### Các khối [new; khandha pi-1]
##### Āyatanaṃ = ##### Các lĩnh vực nhận biết [new; āyatana pi-1]
##### Dhātu = ##### Các yếu tố [new; dhātu pi-1]
##### Saccaṃ = ##### Các sự thật [new; sacca pi-1]
##### Indriyaṃ = ##### Các năng lực [new; indriya pi-1]
##### Paṭiccasamuppādādi = ##### Sự sinh khởi tùy thuộc vào điều kiện và các mục khác [pi-1 words]
##### Khandhādi = ##### Các khối và các mục khác [new]
##### Saccādi = ##### Các sự thật và các mục khác [new]
##### Phassādisattakaṃ = ##### Nhóm bảy mục bắt đầu bằng sự tiếp xúc [new]
##### Tikaṃ = ##### Bộ ba [pi-2 proposal, pi-1 «Ma trận bộ ba»]
##### Dukaṃ = ##### Bộ đôi [pi-2 proposal, pi-1 «Ma trận bộ đôi»]

## 4. Method matrix and method words (ch1 ^3-1, ^3-3, ^3-4)

saṅgaho / asaṅgaho = sự gộp vào / sự không gộp vào [new; pi-1 saṅgaho «phân loại» is the other sense, classification of matter]
saṅgahita / asaṅgahita = được gộp vào / không được gộp vào [pi-2 termbase saṅgahitaṃ «được gộp vào»]
saṅgahitaṃ / asaṅgahitaṃ (as method terms) = điều được gộp vào / điều không được gộp vào [new]
sampayogo / vippayogo = sự gắn liền / sự không gắn liền [new; pi-1 sampayutta «gắn liền với»]
sampayutta / vippayutta = gắn liền với / không gắn liền với [pi-1]
sampayuttaṃ / vippayuttaṃ (as method terms) = điều gắn liền / điều không gắn liền [new]
X-ena Y-aṃ (instrumental of the method) = Y dựa trên X, e.g. saṅgahitena asaṅgahitaṃ = điều không được gộp vào dựa trên điều được gộp vào [new]
two objects (saṅgahitaṃ asaṅgahitaṃ; sampayuttaṃ vippayuttaṃ) = joined with «và» [new]
(1) Saṅgaho asaṅgaho = (1) Sự gộp vào và sự không gộp vào [new]
Tīhi saṅgaho = sự gộp vào theo ba phương diện; tīhi asaṅgaho = sự không gộp vào theo ba phương diện [new]
catūhi sampayogo = sự gắn liền theo bốn phương diện; catūhi vippayogo = sự không gắn liền theo bốn phương diện [new]
sabhāgo / visabhāgo = cùng loại / khác loại [new]
mātikā = ma trận [pi-1]
Sabbāpi dhammasaṅgaṇī dhātukathāya mātikāti. = Toàn bộ “Liệt kê các hiện tượng” là ma trận của “Thảo luận về các yếu tố”. [new]

## 5. Inclusion frames (first method; B.segment_vi, B.incl, B.excl)

X katihi khandhehi katihāyatanehi katihi dhātūhi saṅgahito/-taṃ/-tā/-tāni? = X được gộp vào bao nhiêu khối, bao nhiêu lĩnh vực nhận biết, bao nhiêu yếu tố? [new; «bao nhiêu khối, bao nhiêu lĩnh vực nhận biết, bao nhiêu yếu tố» pi-2 ^2-978 frame] (B.Q_INCL)
X ekena khandhena ekādasahāyatanehi ekādasahi dhātūhi saṅgahito. = X được gộp vào một khối, mười một lĩnh vực nhận biết, mười một yếu tố. [new] (counts joined by commas, no «và»: the Pāli has no ca)
Katihi asaṅgahito/-taṃ/-tā/-tāni? = Không được gộp vào bao nhiêu? [new] (B.Q_EXCL)
Catūhi khandhehi ekenāyatanena sattahi dhātūhi asaṅgahito. = Không được gộp vào bốn khối, một lĩnh vực nhận biết, bảy yếu tố. [new]
Na kehici khandhehi na kehici āyatanehi na kāhici dhātūhi asaṅgahitā. = Không có khối nào, không có lĩnh vực nhận biết nào, không có yếu tố nào mà chúng không được gộp vào. [new]
na kehici … (singular subject: -to / -taṃ) = … mà nó không được gộp vào [new] (B.PRON_SG «nó», B.PRON_PL «chúng»)
Tīhi khandhehi(,) na kehici āyatanehi na kāhici dhātūhi asaṅgahitā. = Không được gộp vào ba khối, nhưng không có lĩnh vực nhận biết nào, không có yếu tố nào mà chúng không được gộp vào. [new]
Na kehici khandhehi(,) ekenāyatanena ekāya dhātuyā asaṅgahito. = Không có khối nào mà nó không được gộp vào, nhưng không được gộp vào một lĩnh vực nhận biết, một yếu tố. [new]
Na kehici khandhehi na kehici āyatanehi pañcahi dhātūhi asaṅgahitā. = Không có khối nào, không có lĩnh vực nhận biết nào mà chúng không được gộp vào, nhưng không được gộp vào năm yếu tố. [new]
X na kehici khandhehi ekenāyatanena ekāya dhātuyā saṅgahitaṃ. = X không được gộp vào khối nào, nhưng được gộp vào một lĩnh vực nhận biết, một yếu tố. [new]
X asaṅkhataṃ khandhato ṭhapetvā … saṅgahitā. = X, xét theo khối thì ngoại trừ điều không do điều kiện tạo thành, được gộp vào … [new; asaṅkhata pi-1 «không do điều kiện tạo thành», ṭhapetvā pi-2 «ngoại trừ»] (B.ASX)
Subject ending in «được» (sanidassanā «thấy được») + saṅgahitā = «… thấy được thì được gộp vào …» (no «được được») [new] (B.THI)
X ca Y ca = X và Y; X ca Y ca Z ca = X, Y và Z (cakkhāyatanañca, dukkhasaccañca, cakkhundriyañca: the same) [new] (B.join_ca)
X… Y… Z (members separated by "…" / "…pe…") = X… Y… Z; a trailing "…pe…" before the counts = "…" [style file]
Jāti dvīhi khandhehi… jarā dvīhi khandhehi… maraṇaṃ dvīhi khandhehi … = Sự sinh được gộp vào hai khối… sự lão hóa được gộp vào hai khối… sự chết được gộp vào hai khối, … [new]

## 6. Closing labels of the rounds (B.LABELS)

(Ekamūlakaṃ.) = (Phần xét từng mục một.) [new]
(Dukamūlakaṃ.) = (Phần xét từng nhóm hai.) [new]
(Tikamūlakaṃ.) = (Phần xét từng nhóm ba.) [new]
(Catukkamūlakaṃ.) = (Phần xét từng nhóm bốn.) [new]
(Pañcakaṃ.) = (Phần xét cả năm.) [new]
(Catukkaṃ.) = (Phần xét cả bốn.) [new]
(Dvādasakaṃ.) = (Phần xét cả mười hai.) [new]
(Aṭṭhārasakaṃ.) = (Phần xét cả mười tám.) [new]

## 7. Counts (B.NUM, B.KH / B.AY / B.DH)

ekena / ekāya / ekenāyatanena = một [new]; dvīhi / dvīhāyatanehi = hai; tīhi / tīhāyatanehi = ba; catūhi = bốn; pañcahi / pañcahāyatanehi = năm; chahi / chahāyatanehi = sáu; sattahi / sattahāyatanehi = bảy; aṭṭhahi = tám; navahi / navahāyatanehi = chín; dasahi / dasahāyatanehi = mười; ekādasahi / ekādasahāyatanehi = mười một; dvādasahi / dvādasahāyatanehi / dvādasāyatanehi = mười hai; terasahi = mười ba; pannarasahi = mười lăm; soḷasahi = mười sáu; sattarasahi = mười bảy; aṭṭhārasahi = mười tám [new]
khandha / āyatana / dhātu as counted nouns = khối / lĩnh vực nhận biết / yếu tố [pi-1]
một khối … mười tám yếu tố: «<number word> <noun>», e.g. «năm khối, mười hai lĩnh vực nhận biết, mười tám yếu tố» [pi-2 ^2-978]

## 8. List members (B.KHANDHA, B.AYATANA, B.DHATU, B.SACCA, B.INDRIYA, B.TOTALS, B.PS, B.OTHER)

Vietnamese has no cases: the same string serves every Pāli case; frames add «với», «của» … as needed.
pañcakkhandhā = năm khối; dvādasāyatanāni = mười hai lĩnh vực nhận biết; aṭṭhārasa dhātuyo = mười tám yếu tố; cattāri saccāni = bốn sự thật; bāvīsatindriyāni = hai mươi hai năng lực [pi-2 ^2-978]
rūpakkhandho, vedanākkhandho, saññākkhandho, saṅkhārakkhandho, viññāṇakkhandho = khối vật chất, khối cảm giác, khối tri giác, khối tạo tác, khối thức [pi-2 ^2-979]
cakkhāyatanaṃ, sotāyatanaṃ, ghānāyatanaṃ, jivhāyatanaṃ, kāyāyatanaṃ, rūpāyatanaṃ, saddāyatanaṃ, gandhāyatanaṃ, rasāyatanaṃ, phoṭṭhabbāyatanaṃ, manāyatanaṃ, dhammāyatanaṃ = lĩnh vực mắt, lĩnh vực tai, lĩnh vực mũi, lĩnh vực lưỡi, lĩnh vực thân, lĩnh vực hình sắc, lĩnh vực âm thanh, lĩnh vực mùi, lĩnh vực vị, lĩnh vực vật xúc chạm, lĩnh vực ý, lĩnh vực đối tượng của ý [pi-2 ^2-980]
cakkhudhātu … phoṭṭhabbadhātu = yếu tố mắt, yếu tố tai, yếu tố mũi, yếu tố lưỡi, yếu tố thân, yếu tố hình sắc, yếu tố âm thanh, yếu tố mùi, yếu tố vị, yếu tố vật xúc chạm [pi-2 ^2-981]
cakkhuviññāṇadhātu … kāyaviññāṇadhātu = yếu tố thức qua mắt, … qua tai, … qua mũi, … qua lưỡi, … qua thân; manodhātu = yếu tố ý; manoviññāṇadhātu = yếu tố ý thức; dhammadhātu = yếu tố đối tượng của ý [pi-2 ^2-981]
dukkhasaccaṃ, samudayasaccaṃ, nirodhasaccaṃ, maggasaccaṃ = sự thật về khổ đau, sự thật về sự phát sinh, sự thật về sự chấm dứt, sự thật về con đường [pi-2 ^2-982]
cakkhundriyaṃ … aññātāvindriyaṃ = năng lực mắt, năng lực tai, năng lực mũi, năng lực lưỡi, năng lực thân, năng lực ý, năng lực nữ tính, năng lực nam tính, năng lực sống, năng lực dễ chịu, năng lực khó chịu, năng lực niềm vui, năng lực nỗi buồn, năng lực bình thản, năng lực niềm tin, năng lực tinh tấn, năng lực tỉnh thức, năng lực định tâm, năng lực trí tuệ, năng lực biết được điều chưa từng biết, năng lực hiểu biết trọn vẹn, năng lực của người đã hiểu biết trọn vẹn [pi-2 ^2-983]
paṭiccasamuppādo = sự sinh khởi tùy thuộc vào điều kiện [pi-1]
avijjā = vô minh [pi-2]
avijjāpaccayā saṅkhārā = “vô minh làm điều kiện cho các sự tạo tác” [pi-2 ^2-226; the link name in “…”, as pi-2 quotes it]
saṅkhārapaccayā viññāṇaṃ = “các sự tạo tác làm điều kiện cho thức” [pi-2 ^2-227]
viññāṇapaccayā nāmarūpaṃ = “thức làm điều kiện cho phần tinh thần và vật chất” [pi-2 ^2-228]
nāmarūpapaccayā saḷāyatanaṃ = “phần tinh thần và vật chất làm điều kiện cho sáu lĩnh vực nhận biết” [pi-2 ^2-229]
saḷāyatanapaccayā phasso = “sáu lĩnh vực nhận biết làm điều kiện cho sự tiếp xúc” [pi-2 ^2-230]
phassapaccayā vedanā = “sự tiếp xúc làm điều kiện cho cảm giác” [pi-2 ^2-231]
vedanāpaccayā taṇhā = “cảm giác làm điều kiện cho khao khát” [pi-2 ^2-232]
taṇhāpaccayā upādānaṃ = “khao khát làm điều kiện cho sự bám víu” [pi-2 ^2-233]
kammabhavo / upapattibhavo = sự hiện hữu dưới dạng nghiệp / sự hiện hữu dưới dạng tái sinh [pi-2 ^2-234]
kāmabhavo / rūpabhavo / arūpabhavo = sự hiện hữu ở cõi dục lạc / ở cõi hình sắc / ở cõi không hình sắc [pi-2 ^2-234]
saññābhavo / asaññābhavo / nevasaññānāsaññābhavo = sự hiện hữu có tri giác / không có tri giác / không phải có tri giác cũng không phải không có tri giác [pi-2 ^2-234]
ekavokārabhavo / catuvokārabhavo / pañcavokārabhavo = sự hiện hữu gồm một khối / gồm bốn khối / gồm năm khối [pi-2 ^2-234]
jāti / jarā / maraṇaṃ = sự sinh / sự lão hóa / sự chết [pi-2]
soko / paridevo / dukkhaṃ / domanassaṃ / upāyāso = sự sầu muộn / sự than khóc / sự khó chịu / nỗi buồn / sự tuyệt vọng [pi-2 ^2-225]
satipaṭṭhānaṃ = sự thiết lập tỉnh thức; cattāro satipaṭṭhānā = bốn sự thiết lập tỉnh thức [pi-2 ^2-U26]
sammappadhānaṃ = nỗ lực đúng đắn; cattāro sammappadhānā = bốn nỗ lực đúng đắn [pi-2 ^2-U26]
iddhipādo = nền tảng thần thông; cattāro iddhipādā = bốn nền tảng thần thông [pi-2 ^2-U26]
jhānaṃ = tầng thiền; cattāri jhānāni = bốn tầng thiền [pi-2 ^2-623]
appamaññā = trạng thái không thể đo lường; catasso appamaññāyo = bốn trạng thái không thể đo lường [pi-2 Appamaññāvibhaṅga]
pañcindriyāni = năm năng lực; pañca balāni = năm sức mạnh; satta bojjhaṅgā = bảy chi phần giác ngộ [pi-2 ^2-U26]
ariyo aṭṭhaṅgiko maggo = con đường gồm tám chi phần cao quý [pi-2 ^2-486, Maggaṅgavibhaṅga; pi-2 ^2-U26 has «con đường cao quý gồm tám chi phần» once]
phasso / vedanā / saññā / cetanā / cittaṃ / adhimokkho / manasikāro = sự tiếp xúc / cảm giác / tri giác / chủ ý / tâm / sự quyết định / sự chú tâm [pi-1 core; adhimokkho pi-2 ^2-280]
Triad and dyad names (dhammā) = «các hiện tượng <predicate>», predicate verbatim from the pi-1 matrix (B.MATRIX_PRED: every predicate of ch2, e.g. kusalā = thiện, sukhāya vedanāya sampayuttā = gắn liền với cảm giác dễ chịu, hetū ceva sahetukā ca = vừa là gốc rễ vừa có gốc rễ, kenaci viññeyyā = mà một loại thức nào đó có thể nhận biết) [pi-1]
na hetū sahetukā = các hiện tượng không phải là gốc rễ nhưng có gốc rễ [pi-1 ^1-1087]
na hetū ahetukā = các hiện tượng không phải là gốc rễ và không có gốc rễ [pi-1 ^1-1088]
āsavavippayuttā sāsavā / anāsavā = các hiện tượng không gắn liền với ô nhiễm nhưng là đối tượng của ô nhiễm / … và không phải là đối tượng của ô nhiễm [pi-1 ^1-1116 ff.]
parāmāsavippayuttā parāmaṭṭhā / aparāmaṭṭhā = các hiện tượng không gắn liền với sự hiểu sai lệch nhưng bị sự hiểu sai lệch nắm giữ / … và không bị sự hiểu sai lệch nắm giữ [pi-1 ^1-1189, ^1-1190]
kilesavippayuttā saṃkilesikā / asaṃkilesikā = các hiện tượng không gắn liền với phiền não nhưng là đối tượng của phiền não / … và không phải là đối tượng của phiền não [pi-1 ^1-1259, ^1-1260]
upādinna (pi-3 spelling) = do nghiệp tạo ra (= pi-1 upādiṇṇa) [pi-1]

## 9. Terms

dhamma = hiện tượng; dhammā (in the matrix names) = các hiện tượng [pi-1]
asaṅkhataṃ (noun) = điều không do điều kiện tạo thành [pi-1 words]
ṭhapetvā = ngoại trừ [pi-2]
khandhato (in asaṅkhataṃ khandhato ṭhapetvā) = xét theo khối [new]

## 10. Variant / editorial brackets of the sample (B.VARIANTS)

kammabhavo [upādānapaccayā kammabhavo (sī. syā.)] = sự hiện hữu dưới dạng nghiệp [dị bản (Sī., Syā.): upādānapaccayā kammabhavo]
parittārammaṇā [parittāramaṇā (?)] = có đối tượng hạn hẹp [khác chính tả (?): parittāramaṇā]
na hetū ahetukā [na hetū ahetukā (syā. ka.) vibha. dukapañhāpucchakepi] = không phải là gốc rễ và không có gốc rễ [dị bản (Syā., Ka.): na hetū ahetukā; Phân tích các hiện tượng, cả trong phần hỏi đáp về bộ đôi] (pi-2 pattern ^2-924; dukapañhāpucchaka = «phần hỏi đáp về bộ đôi», pi-2 Pañhāpucchakaṃ «Phần hỏi đáp»)
