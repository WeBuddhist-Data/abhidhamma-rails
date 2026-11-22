# notes-map-5-01: Saccayamaka (5-01-saccayamaka, paṇṇattivāra + uppādavāra); member tables for 5-02 / 5-03

Script: map_5-01_vi.py (`T = importlib.import_module("map_5-01_vi")`; importing builds nothing). Tables: SACCA_STEM, SACCA, SUBJECT, CITTA_KIND5, NOUN_OF, PERSONS5, PLANES5, PATH, NOTES5, HEAD5, OTHER5, T501; helpers sacca_value(kw, text), citta5(word), moment5(kw, text), value501(kw, kws, vi, pi, table) = your table -> T501 -> NOUN_OF -> sacca_value -> moment5 / citta5 -> paṭilabhissanti -> map_2-01_vi.value201 (members = SACCA) -> value6.
Shared frames come from map_2-01_vi (verb_value, planes / beings, itaresaṃ, relatives) and map_8_vi (MOMENT, citta_value); 0 differences with them on identical Pāli and Vietnamese.
Result: 155 lines, bad [], 3 (no direct equivalent) (the placeholder keyword, ^6-5-70), presence misses 0, no exceptions.

## Members (every form: -aṃ, -nti, -ti, -ñca, -ñceva; first letter case-insensitive)
dukkhasaccaṃ = sự thật về khổ đau
samudayasaccaṃ = sự thật về sự phát sinh
nirodhasaccaṃ = sự thật về sự chấm dứt
maggasaccaṃ = sự thật về con đường
dukkhaṃ / dukkhanti / Dukkhañca / dukkhañceva = khổ đau (the truth; 10-01 bare dukkhaṃ «sự khó chịu» is the bodily-pain faculty)
samudayo / samudayoti / Samudayaṃ / Samudayañca = sự phát sinh
nirodho / nirodhoti / Nirodhaṃ / Nirodhañca = sự chấm dứt
maggo / maggoti / Maggaṃ / Maggañca = con đường (also maggaṃ of «maggaṃ na paṭilabhissanti»)
saccaṃ / saccanti / saccañca / saccañceva / saccā / saccāni = sự thật («Các sự thật», «Bốn sự thật»: leading «các» and the numeral of a keyword without it are frame)
Kāyikaṃ dukkhaṃ = khổ đau nơi thân; cetasikaṃ dukkhaṃ = khổ đau trong tâm (the member word «khổ đau» kept, as build_5-01 KAYIKA_CETASIKA)

## Citta kinds and moments («Vào» of the locative is frame, = 8)
cittassa uppādakkhaṇe / cittassa bhaṅgakkhaṇe = khoảnh khắc sinh khởi / khoảnh khắc tan rã của tâm (= 8)
taṇhāvippayuttacittassa uppādakkhaṇe = khoảnh khắc sinh khởi của tâm không gắn liền với khao khát
maggavippayuttacittassa uppādakkhaṇe = khoảnh khắc sinh khởi của tâm không gắn liền với con đường
taṇhāvippayuttamaggavippayuttacittassa uppādakkhaṇe = khoảnh khắc sinh khởi của tâm không gắn liền với khao khát và không gắn liền với con đường
maggavippayuttataṇhāvippayuttacittassa (uppādakkhaṇe) = (khoảnh khắc sinh khởi của) tâm không gắn liền với con đường và không gắn liền với khao khát (order kept)
upapatticittassa uppādakkhaṇe / bhaṅgakkhaṇe = khoảnh khắc sinh khởi / tan rã của tâm tái sinh
Taṇhāya uppādakkhaṇe / taṇhāya bhaṅgakkhaṇe = khoảnh khắc sinh khởi / tan rã của khao khát
taṇhāvippayuttacitte = tâm không gắn liền với khao khát; citte = tâm; akusale citte = tâm bất thiện («tâm bất thiện thứ hai»); vattamāne = khi … đang diễn ra (pi-5)
maggassa = con đường; Aggamaggassa = con đường tối thượng; phalassa = thành quả (owners of a moment: NOUN_OF; aggaphalassa = thành quả tối thượng proposal for 5-02)
cittassa (yassa cittassa anantarā) = tâm; anantarā = ngay sau
pavatte = đời sống («trong đời sống»: the locative «trong» is frame, as «Trong cõi …» and the «Vào» of the moments)

## Persons, beings, planes («Ở» and the leading «những» / «các» frame)
Aggamaggasamaṅgīnaṃ = người có được con đường tối thượng (FORMULAS aggamaggasamaṅgī)
Abhisametāvīnaṃ / anabhisametāvīnaṃ = người đã thấu hiểu / người chưa thấu hiểu
puthujjanā = người phàm phu («những người phàm phu nào»)
arahantānaṃ = bậc A-la-hán («các bậc A-la-hán»)
āpāyikānaṃ = chúng sinh trong cõi khổ (2-01 BEINGS shape); Apāye = cõi khổ
Pacchimacittasamaṅgīnaṃ = người có được tâm cuối cùng (8); nirodhasamāpannānaṃ = người nhập thành tựu thiền chấm dứt (8)
caññe (ye caññe maggaṃ paṭilabhissanti «và những người khác nào …») = khác (ca «và» frame)
aggamaggaṃ paṭilabhissanti (and the slip paṭilabhissānti, ^6-5-74) = sẽ đạt được con đường tối thượng; maggaṃ paṭilabhissanti = sẽ đạt được con đường
paṭilabhissanti alone = sẽ đạt được; sẽ … đạt được where the segment has only «sẽ không đạt được» (^6-5-87)
Avasese (Avasese catuvokāre pañcavokāre «… cõi gồm năm khối còn lại») = còn lại; asaññattā (^6-5-76 slip for asaññasattā) = cõi Vô Tưởng
Itaresaṃ / pañcavokārānaṃ / Suddhāvāsānaṃ / Suddhāvāsaṃ / asaññasattaṃ / asaññasattā / pañcavokāraṃ / pañcavokārā = map_2-01_vi (người khác or chúng sinh khác; cõi gồm năm khối after Itaresaṃ catuvokārānaṃ; chúng sinh trong cõi Tịnh Cư; cõi …)

## Headings and editorial notes
Suddhasaccavāro = mục về các sự thật thuần túy; Suddhasaccamūlacakkavāro = mục về vòng luân chuyển dựa trên các sự thật thuần túy (inner «các» kept, = 3-01 Suddhāyatanavāro)
Paṇṇattivāra (^6-5-6-0 stem form) = mục về sự định danh
Yassakampi = phần về người; yassayatthakampi = phần về người và nơi chốn; Yatthakampi / yatthakampi = phần về nơi chốn; yatthakā = phần về nơi chốn (-pi «cũng» no word of its own)
yatthakasadisaṃ = giống như phần về nơi chốn; yassayatthakasadisaṃ = giống như phần về người và nơi chốn (= 3-01 yassakasadisaṃ)
avaseso / avasesaṃ / avasesā = còn lại; ṭhapetvā = ngoại trừ

## CROSSCHECK
dukkhaṃ / dukkhanti / Dukkhañca = khổ đau here vs 10-01 «sự khó chịu» (truth vs faculty; as the texts write them).
Moments without «vào» (8 rule) vs the approved pi-2 upapattikkhaṇe «vào khoảnh khắc tái sinh» (pi-1 / pi-2 samaye «vào lúc ấy»).
pavatte = đời sống (case word «trong» dropped); no earlier map value.
uppajjissati / uppajjissatīti = sẽ sinh khởi in all 5-01 segments by the current map_2-01_vi.verb_value (bare verb and -ti form one verb); 8-cittayamaka.mapped.md still has «sẽ … sinh khởi» in 17 places by its older per-token rule.
Itaresaṃ = chúng sinh khác (^6-5-41, 51, 81) / người khác (5 segments); pañcavokārānaṃ = cõi gồm năm khối (only after Itaresaṃ catuvokārānaṃ): both by the 2-01 / 3-02 position rules.
