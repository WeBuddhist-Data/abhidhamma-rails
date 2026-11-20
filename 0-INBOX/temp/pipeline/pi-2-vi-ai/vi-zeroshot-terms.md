# pi-2 Vibhaṅga: Vietnamese plain zero-shot, binding terms (from the chapter-1 sample)

Format: Pāli = tiếng Việt, one per line. Tags: [pi-1] = verbatim from the reviewed pi-1 Vietnamese rails text, its termbase, APPROVED.md or vi-core-terms.md; [pi-1 words] = built only from pi-1 words; [new] = settled here for pi-2.
Reuse every string verbatim: import build_ch1_sample_vi.py (AGG, ATTR, FIVE_AGGREGATES, KHANDHA_SPAN, KHANDHA_TOGETHER, TIME, SELF, MEMBERS, QUAL, FEEL, PRED, the frame functions, RUPA_* strings) instead of retyping. vietnamese-style.md applies unchanged (dash rule, “…” / ‘…’, variant brackets, sati = «sự tỉnh thức»).
`python -I -X utf8 build_ch1_sample_vi.py --check` asserts that the [pi-1] strings still occur byte for byte in the pi-1 Vietnamese and that the outputs match the build.

## 1. Book frame

Namo tassa bhagavato arahato sammāsambuddhassa = Kính lễ Đức Thế Tôn, bậc A-la-hán, bậc Tự Giác Ngộ Hoàn Toàn [pi-1]
# Abhidhammapiṭake = # Tạng Vi Diệu Pháp [pi-1]
## Vibhaṅgapāḷi = ## Phân tích các hiện tượng [new, proposal; pairs with pi-1 «Liệt kê các hiện tượng»; mid-sentence “Phân tích các hiện tượng”]
Vibhaṅgapāḷi, alternative 1 = Phân tích chi tiết [new]
Vibhaṅgapāḷi, alternative 2 = Sách phân tích [new]

## 2. Chapter headings (### level) [new; words from pi-1]

vibhaṅga (chapter title) = phân tích (pi-1 vibhatti, bhājanīya = «phân tích»)
Closing line "<X>vibhaṅgo niṭṭhito." = "<title> đã hoàn tất." [pi-1 pattern: «Ma trận đã hoàn tất.»]
Alternative pattern if the user prefers the pi-1 «Phần về …» headings: «Phần về các khối», «Phần về các lĩnh vực nhận biết» … (same nouns as below).
### Khandhavibhaṅgo = ### Phân tích các khối (khandha = khối [pi-1])
### Āyatanavibhaṅgo = ### Phân tích các lĩnh vực nhận biết (āyatana [pi-1])
### Dhātuvibhaṅgo = ### Phân tích các yếu tố (dhātu [pi-1])
### Saccavibhaṅgo = ### Phân tích các sự thật (sacca [pi-1])
### Indriyavibhaṅgo = ### Phân tích các năng lực (indriya [pi-1])
### Paṭiccasamuppādavibhaṅgo = ### Phân tích sự sinh khởi tùy thuộc vào điều kiện [pi-1 core]
### Satipaṭṭhānavibhaṅgo = ### Phân tích sự thiết lập tỉnh thức (pi-1 Cittuppādakaṇḍa, lokuttaraṃ satipaṭṭhānaṃ = «sự thiết lập tỉnh thức»)
### Sammappadhānavibhaṅgo = ### Phân tích các nỗ lực đúng đắn (APPROVED sammappadhāna = «nỗ lực đúng đắn»)
### Iddhipādavibhaṅgo = ### Phân tích các nền tảng thần thông (pi-1 iddhipāda = «nền tảng thần thông»)
### Bojjhaṅgavibhaṅgo = ### Phân tích các chi phần giác ngộ [pi-1 termbase]
### Maggaṅgavibhaṅgo = ### Phân tích các chi phần của con đường [pi-1 termbase]
### Jhānavibhaṅgo = ### Phân tích các tầng thiền [pi-1 core]
### Appamaññāvibhaṅgo = ### Phân tích các trạng thái không thể đo lường (pi-1 appamāṇa = «không thể đo lường»; open point)
### Sikkhāpadavibhaṅgo = ### Phân tích các điều tu học (pi-1 sikkhā = «sự tu học»; new)
### Paṭisambhidāvibhaṅgo = ### Phân tích các loại hiểu biết thông suốt (new; open point)
### Ñāṇavibhaṅgo = ### Phân tích các loại hiểu biết (ñāṇa = hiểu biết [pi-1])
### Khuddakavatthuvibhaṅgo = ### Phân tích các chủ đề nhỏ (new)
### Dhammahadayavibhaṅgo = ### Phân tích cốt lõi của các hiện tượng (new; open point; alternative «Phân tích cốt lõi của Giáo Pháp»)

## 3. Recurring section headings (#### level) [new]

The closing line repeats the heading with "." (pi-1: Padabhājanīyaṃ. = Phân tích từng từ.).
#### Suttantabhājanīyaṃ = #### Phân tích theo kinh (pi-1 Suttantika = «theo kinh», bhājanīya = «phân tích»)
Suttantabhājanīyaṃ. (closing line) = Phân tích theo kinh.
#### Abhidhammabhājanīyaṃ = #### Phân tích theo Vi Diệu Pháp (pi-1 Abhidhamma = «Vi Diệu Pháp»)
Abhidhammabhājanīyaṃ. (closing line) = Phân tích theo Vi Diệu Pháp.
#### Pañhāpucchakaṃ = #### Phần hỏi đáp
Pañhāpucchakaṃ. (closing line) = Phần hỏi đáp.
##### Tikaṃ / Dukaṃ (inside Pañhāpucchaka, the matrix triads/dyads) = ##### Bộ ba / Bộ đôi (proposal; pi-1 «Ma trận bộ ba / bộ đôi»)

## 4. Aggregates [pi-1]

##### Rūpakkhandho = ##### Khối vật chất
##### Vedanākkhandho = ##### Khối cảm giác
##### Saññākkhandho = ##### Khối tri giác
##### Saṅkhārakkhandho = ##### Khối tạo tác
##### Viññāṇakkhandho = ##### Khối thức
Pañcakkhandhā – rūpakkhandho, vedanākkhandho, saññākkhandho, saṅkhārakkhandho, viññāṇakkhandho. = Năm khối – khối vật chất, khối cảm giác, khối tri giác, khối tạo tác và khối thức. [pi-1 ^1-1089]
Nouns: rūpa = vật chất; vedanā = cảm giác; saññā = tri giác; saṅkhārā = các sự tạo tác (always with «các», as in pi-1); viññāṇa = thức [pi-1]

## 5. Question / answer frames

Tattha katamo/katamā/katamaṃ/katame <X>? = Ở đây, <X> là gì? [pi-1 ^1-584, ^1-1008]
… – idaṃ / ayaṃ vuccati <X>. ; … – ime vuccanti <X>. = … – đó được gọi là <X>. [pi-1; plural uses the same words, new]
Tattha katamo rūpakkhandho? = Ở đây, khối vật chất là gì? [pi-1 frame]
ayaṃ vuccati rūpakkhandho = đó được gọi là khối vật chất [pi-1 frame]
Tattha katamaṃ rūpaṃ atītaṃ? = Ở đây, vật chất thuộc quá khứ là gì? (attribute after the noun) [pi-1 frame]
Tattha katamā vedanā oḷārikā sukhumā? = Ở đây, cảm giác ở dạng thô và ở dạng vi tế là gì? [new]
Tattha katamā vedanā hīnā paṇītā? = Ở đây, cảm giác thấp kém và ưu việt là gì? [new]
Where the Pāli starts "Ayaṃ/Ime vuccati…" as a new sentence (no dash), so does the Vietnamese: «Đó được gọi là cảm giác ở gần.»
Member lists after the definition follow ":" (pi-1 ^1-1044 frame); «và» only where the Pāli has ca.

## 6. Attributes (always after the noun) [pi-1]

atīta / anāgata / paccuppanna = thuộc quá khứ / thuộc tương lai / thuộc hiện tại [pi-1 matrix]
ajjhatta / bahiddhā = ở nơi bản thân / ở bên ngoài bản thân [pi-1, APPROVED]
oḷārika / sukhuma = ở dạng thô / ở dạng vi tế [pi-1]
hīna / paṇīta = thấp kém / ưu việt [pi-1]
dūre / santike = ở xa / ở gần [pi-1 ^1-676/677]
ajjhattika / bāhira (rūpa) = thuộc phần bên trong / thuộc phần bên ngoài [pi-1] (kept apart from ajjhatta/bahiddhā)

## 7. Aggregate formulas

Yaṃ kiñci rūpaṃ = Bất cứ vật chất nào; Yā kāci vedanā = Bất cứ cảm giác nào; Ye keci saṅkhārā = Bất cứ những sự tạo tác nào [new]
atītānāgatapaccuppannaṃ ajjhattaṃ vā bahiddhā vā oḷārikaṃ vā sukhumaṃ vā hīnaṃ vā paṇītaṃ vā yaṃ dūre santike vā = thuộc quá khứ, tương lai hay hiện tại, ở nơi bản thân hay ở bên ngoài bản thân, ở dạng thô hay ở dạng vi tế, thấp kém hay ưu việt, ở xa hay ở gần [new from pi-1 words] (KHANDHA_SPAN)
tadekajjhaṃ abhisaññūhitvā abhisaṅkhipitvā = khi gom tất cả lại làm một và thu tóm lại [new] (KHANDHA_TOGETHER)
Full: Ở đây, khối vật chất là gì? Bất cứ vật chất nào, <SPAN>, <TOGETHER> – đó được gọi là khối vật chất. (khandha_def)
atītaṃ niruddhaṃ vigataṃ vipariṇataṃ atthaṅgataṃ abbhatthaṅgataṃ uppajjitvā vigataṃ atītaṃ atītaṃsena saṅgahitaṃ = thuộc quá khứ, đã chấm dứt, đã mất đi, đã biến đổi, đã biến mất, đã biến mất hoàn toàn, đã mất đi sau khi sinh khởi, thuộc quá khứ, được gộp vào phần thuộc quá khứ [pi-1 ^1-1044]
ajātaṃ … anāgataṃ anāgataṃsena saṅgahitaṃ = chưa sinh ra, chưa trở thành, chưa sinh thành, chưa phát sinh, chưa phát sinh rõ rệt, chưa hiện ra, chưa sinh khởi, chưa sinh khởi trọn vẹn, chưa trỗi dậy, chưa trỗi dậy trọn vẹn, thuộc tương lai, được gộp vào phần thuộc tương lai [pi-1 ^1-1045]
jātaṃ … paccuppannaṃ paccuppannaṃsena saṅgahitaṃ = đã sinh ra, đã trở thành, đã sinh thành, đã phát sinh, đã phát sinh rõ rệt, đã hiện ra, đã sinh khởi, đã sinh khởi trọn vẹn, đã trỗi dậy, đã trỗi dậy trọn vẹn, thuộc hiện tại, được gộp vào phần thuộc hiện tại [pi-1 ^1-1046]
Yaṃ rūpaṃ <TIME>, <members> – = Vật chất <TIME>: <members> – [pi-1 frame «Những hiện tượng thuộc quá khứ, …: …»] (time_line)
tesaṃ tesaṃ sattānaṃ ajjhattaṃ paccattaṃ niyakaṃ pāṭipuggalikaṃ upādinnaṃ = của từng chúng sinh, ở nơi bản thân, riêng từng người, cố hữu, thuộc về cá nhân, do nghiệp tạo ra [pi-1 ^1-1050; pi-1 Pāli niyatā, pi-2 niyaka takes the same «cố hữu»]
tesaṃ tesaṃ parasattānaṃ parapuggalānaṃ ajjhattaṃ … = của từng chúng sinh khác, từng người khác, ở nơi bản thân của họ, riêng từng người, cố hữu, thuộc về cá nhân, do nghiệp tạo ra [pi-1 ^1-1051]
cattāro ca mahābhūtā catunnañca mahābhūtānaṃ upādāyarūpaṃ = bốn yếu tố cơ bản và vật chất phái sinh từ bốn yếu tố cơ bản [pi-1 ^1-584]
sukhā vedanā dukkhā vedanā adukkhamasukhā vedanā = cảm giác dễ chịu, cảm giác khó chịu, cảm giác không khó chịu cũng không dễ chịu [pi-1 words]
cakkhusamphassajā saññā … manosamphassajā saññā = tri giác sinh từ sự tiếp xúc của mắt, … của tai, … của mũi, … của lưỡi, … của thân, tri giác sinh từ sự tiếp xúc của ý [pi-1 words; manosamphassa = «sự tiếp xúc của ý» new, from pi-1 mano = ý]
cakkhusamphassajā cetanā … = chủ ý sinh từ sự tiếp xúc của mắt, …, chủ ý sinh từ sự tiếp xúc của ý [same]
cakkhuviññāṇaṃ … manoviññāṇaṃ = thức qua mắt, thức qua tai, thức qua mũi, thức qua lưỡi, thức qua thân, ý thức [pi-1 termbase]
Cakkhāyatanaṃ…pe… phoṭṭhabbāyatanaṃ = Lĩnh vực mắt… lĩnh vực vật xúc chạm [pi-1 ^1-674]
Itthindriyaṃ…pe… kabaḷīkāro āhāro = Năng lực nữ tính… thức ăn trong vai trò dưỡng chất [pi-1 ^1-675]
tesaṃ tesaṃ sattānaṃ (by whom despised / honoured) = mà đối với từng chúng sinh thì … [new]
uññātaṃ avaññātaṃ hīḷitaṃ paribhūtaṃ acittīkataṃ = bị coi thường, bị xem nhẹ, bị chê bai, bị khinh miệt, không được quý trọng [new]
anuññātaṃ anavaññātaṃ ahīḷitaṃ aparibhūtaṃ cittīkataṃ = không bị coi thường, không bị xem nhẹ, không bị chê bai, không bị khinh miệt, được quý trọng [new]
hīnaṃ hīnamataṃ hīnasammataṃ = thấp kém, được xem là thấp kém, được công nhận là thấp kém [new; hīna pi-1]
paṇītaṃ paṇītamataṃ paṇītasammataṃ = ưu việt, được xem là ưu việt, được công nhận là ưu việt [new; paṇīta pi-1]
aniṭṭhaṃ akantaṃ amanāpaṃ / iṭṭhaṃ kantaṃ manāpaṃ = không đáng mong muốn, không đáng yêu mến, không đáng ưa thích / đáng mong muốn, đáng yêu mến, đáng ưa thích [new; pi-1 kantā «yêu mến», manāpā «ưa thích»]
rūpā saddā gandhā rasā phoṭṭhabbā = hình sắc, âm thanh, mùi, vị, vật xúc chạm [pi-1 words]
yaṃ vā panaññampi atthi rūpaṃ anāsanne anupakaṭṭhe dūre asantike = hoặc còn có bất cứ vật chất nào khác không gần kề, không cận kề, ở xa, không ở gần [new; «hoặc còn có bất cứ … nào khác» from the pi-1 rūpāyatana definition]
… āsanne upakaṭṭhe avidūre santike = … gần kề, cận kề, không xa, ở gần [new]
Taṃ taṃ vā pana rūpaṃ upādāyupādāya rūpaṃ hīnaṃ paṇītaṃ daṭṭhabbaṃ. = Hoặc nữa, so với vật chất này hay vật chất kia, vật chất nên được xem là thấp kém hay ưu việt. [new] (tail())
  saṅkhārā: so với các sự tạo tác này hay các sự tạo tác kia, các sự tạo tác nên được xem là …; dūre santike: … là ở xa hay ở gần

## 8. Comparison qualifiers (coarse/subtle, inferior/superior, far/near paragraphs)

Every clause: <noun phrase> thì <predicate> (THI; keeps «A là đối tượng của ô nhiễm thì ở xa B» unambiguous) [new]
A oḷārikā, B sukhumā = A thì ở dạng thô, B thì ở dạng vi tế; hīna/paṇīta = thì thấp kém / thì ưu việt [new]
A B-ehi/-āya/-ā dūre = A thì ở xa B; A B-āya/-assa/-ānaṃ santike = A thì ở gần B [new]
Pāli ";" stays ";", "." stays ".".
akusala / kusala / abyākata = bất thiện / thiện / không xác định về mặt đạo đức [pi-1 core]
Pair compounds take «các» before the noun (none elsewhere): kusalābyākatā = các … thiện và không xác định về mặt đạo đức; akusalābyākatā = các … bất thiện và không xác định về mặt đạo đức; kusalākusalā = các … thiện và bất thiện; sukhadukkhā = các cảm giác dễ chịu và khó chịu [pi-1 words; «các» new]
sukhā / dukkhā / adukkhamasukhā vedanā = cảm giác dễ chịu / cảm giác khó chịu / cảm giác không khó chịu cũng không dễ chịu [pi-1 ^1-M1-2]
sukhā ca adukkhamasukhā ca vedanā = cảm giác dễ chịu và cảm giác không khó chịu cũng không dễ chịu [new]
dukkhāya vedanāya sampayuttā X = X gắn liền với cảm giác khó chịu [pi-1 sampayutta «gắn liền với»]
sukhāya ca adukkhamasukhāya ca vedanāhi sampayuttā X = X gắn liền với cảm giác dễ chịu và cảm giác không khó chịu cũng không dễ chịu [new]
sukhadukkhāhi vedanāhi sampayuttā X = X gắn liền với các cảm giác dễ chịu và khó chịu [new]
samāpannassa X = X của người đã chứng nhập [pi-1 termbase, ^1-1289]
asamāpannassa X = X của người chưa chứng nhập [new]
sāsava / anāsava = là đối tượng của ô nhiễm / không phải là đối tượng của ô nhiễm [pi-1]
paṭighasamphassajā saññā = tri giác sinh từ sự tiếp xúc có va chạm [new; pi-1 sappaṭigha «có tính va chạm»]
adhivacanasamphassajā saññā = tri giác sinh từ sự tiếp xúc qua tên gọi [new; pi-1 adhivacana «tên gọi»]

## 9. Classification frames (Abhidhammabhājanīya)

Ekavidhena rūpakkhandho – = Phân loại khối vật chất theo nhóm một – [new, from pi-1 «Phân loại vật chất theo nhóm một –»]
Evaṃ ekavidhena rūpakkhandho. = Như vậy là phân loại khối vật chất theo nhóm một. [new, pi-1 frame]
Duvidhena … Ekādasavidhena = theo nhóm hai, ba, bốn, năm, sáu, bảy, tám, chín, mười, mười một [pi-1]
Same frame for every aggregate: Phân loại khối cảm giác theo nhóm hai – … Như vậy là phân loại khối cảm giác theo nhóm hai. (class_open, class_close)
sabbaṃ rūpaṃ na hetu … jarābhibhūtaṃ = toàn bộ vật chất không phải là gốc rễ; … bị sự lão hóa chế ngự [pi-1 ^1-584 verbatim minus its rūpiyaṃ bracket; nevācayagāmināpacayagāmī = pi-1 neva ācayagāmi na apacayagāmi «không dẫn đến sự tích lũy cũng không dẫn đến sự giảm trừ»] (RUPA_EKAVIDHA)
Atthi rūpaṃ X, atthi rūpaṃ Y. = Có loại vật chất X, có loại vật chất Y. [pi-1 ^1-U1, RUPA_DUKA]
yaṃ taṃ rūpaṃ ajjhattikaṃ taṃ X, yaṃ taṃ rūpaṃ bāhiraṃ taṃ atthi Y, atthi Z = vật chất nào thuộc phần bên trong thì X; vật chất nào thuộc phần bên ngoài thì có loại Y, có loại Z [pi-1 ^1-585; «;» between the halves, new]
yaṃ taṃ rūpaṃ upādā taṃ atthi X, atthi Y; yaṃ taṃ rūpaṃ no upādā … = vật chất nào là phái sinh thì có loại X, có loại Y; vật chất nào không phải là phái sinh thì … [pi-1 ^1-586]
diṭṭhaṃ, sutaṃ, mutaṃ, viññātaṃ rūpaṃ = vật chất được thấy, được nghe, được cảm nhận, được nhận biết [pi-1]
Five- to elevenfold lists = RUPA_PANCA … RUPA_EKADASA [pi-1 ^1-587 … ^1-593 verbatim, first letter lowered]
(Yathā rūpakaṇḍe vibhattaṃ, tathā idha vibhajitabbaṃ.) = (Như đã phân tích trong phần về vật chất, ở đây cũng nên phân tích như vậy.) [new; pi-1 Rūpakaṇḍa «Phần về vật chất»]

## 10. Terms (pi-2 spelling or newly fixed)

upādinna (pi-2 spelling) = do nghiệp tạo ra (= pi-1 upādiṇṇa) [pi-1]
upādinnupādāniya = do nghiệp tạo ra và là đối tượng của sự bám víu [pi-1]
upādā / no upādā = phái sinh / không phải là phái sinh [pi-1]
mahābhūta = yếu tố cơ bản [pi-1]
kabaḷīkāro āhāro = thức ăn trong vai trò dưỡng chất [pi-1, APPROVED]
niyaka = cố hữu [pi-1 niyatā, same sense]
paccattaṃ = riêng từng người; pāṭipuggalika = thuộc về cá nhân [pi-1]
manosamphassa = sự tiếp xúc của ý [new]
samāpanna / asamāpanna = người đã chứng nhập / người chưa chứng nhập [pi-1 / new]
Variant brackets in the sample: kabaḷīkāro [kabaḷiṃkāro (sī. syā.)] = thức ăn trong vai trò dưỡng chất [khác chính tả (Sī., Syā.): kabaḷiṃkāro]; no upādā [nupādā (sī. ka.)] = không phải là phái sinh [khác chính tả (Sī., Ka.): nupādā]
