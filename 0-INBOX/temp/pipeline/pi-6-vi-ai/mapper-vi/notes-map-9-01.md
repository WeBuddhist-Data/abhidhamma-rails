# notes-map-9-01: Dhammayamaka (9-01-dhammayamaka, paṇṇattivāra + uppādavāra); frame-setter of the Dhammayamaka members for 9-02 / 9-03

Script: map_9-01_vi.py (`D = importlib.import_module("map_9-01_vi")`; importing builds nothing). Tables: DHAMMA_ADJ, DHAMMA_NOUN, DHAMMA9, CITTA_KIND9, OWNER9, BHAVANA_STEMS, BHAVANA, HEAD9, TITLE9, T901; helpers dhamma_value(kw, vi, pi), citta9(word), moment9(kw, text), bhavana_value(kw, pali), value901(kw, kws, vi, pi, table) = your table -> T901 -> TITLE9 -> dhamma_value -> moment9 / citta9 -> bhavana_value -> map_5-01_vi T501 / NOUN_OF / paṭilabhissanti -> map_2-01_vi.value201 (members = DHAMMA9) -> value6.
Shared frames from map_2-01_vi (verb_value, planes / beings, Itaresaṃ, relatives, Paṇṇattiniddesavāro), map_2-02_vi (_polarity for the bhāvanā verbs), map_8_vi (MOMENT, norm, citta_value), map_5-01_vi (citta5, NOUN_OF, PERSONS5, PLANES5 pavatte, PATH).
Result: 165 lines, bad [], 0 (no direct equivalent), presence misses 0, no exceptions; verb_audit_vi.py 0 differences. Dry run of value901 on 9-02 (1058 keywords) and 9-03 (572): 0 misses.

## Members (DHAMMA9; first letter case-insensitive)
kusalā / kusalāti = thiện; akusalā / akusalāti = bất thiện; abyākatā / abyākatāti = không xác định về mặt đạo đức («Những gì là thiện …», «… có phải là thiện không?»: predicate «là» dropped)
kusalā dhammā / kusalā dhammāti / Kusalā dhammā = hiện tượng thiện (text «các hiện tượng thiện», contiguous: leading «các» dropped); same for akusalā / abyākatā; «hiện tượng … X» only where a segment splits it (sample rule; not met here)
kusalā ca dhammā / akusalā ca dhammā / abyākatā ca dhammā = hiện tượng thiện … («đồng thời các hiện tượng … cũng sinh khởi»: ca = frame, coordinator -ñca rule)
Kusalaṃ / Akusalaṃ / Abyākataṃ (first occurrence «Kusalaṃ ṭhapetvā» «Ngoại trừ hiện tượng thiện») = hiện tượng thiện / hiện tượng bất thiện / hiện tượng không xác định về mặt đạo đức (first-occurrence rule; the predicate «không phải là thiện» = thiện where that comes first)
Kusalañca / Abyākatañca = hiện tượng thiện / hiện tượng không xác định về mặt đạo đức (-ñca = member value)
Kusalañca dhamme / Akusalañca dhamme / Abyākatañca dhamme = hiện tượng thiện và các hiện tượng (… bất thiện …, … không xác định về mặt đạo đức …) (connective «và» and inner «các» kept, pi-1 rūpañca nibbānañca)
kusalaṃ dhammaṃ / akusalaṃ dhammaṃ = hiện tượng thiện / hiện tượng bất thiện (9-03 ^6-9-229); dhammā / dhamme / dhammaṃ alone = hiện tượng; kusalānaṃ alone = hiện tượng thiện
Avasesā / avasesā = còn lại; ṭhapetvā = ngoại trừ

## Moments and citta kinds («vào» of the locative is frame, = 8 / 5-01)
kusalānaṃ uppādakkhaṇe / Kusalānaṃ uppādakkhaṇe = khoảnh khắc sinh khởi của các hiện tượng thiện (inner «các» kept); akusalānaṃ … = … của các hiện tượng bất thiện
kusalavippayuttacittassa uppādakkhaṇe = khoảnh khắc sinh khởi của tâm không gắn liền với các hiện tượng thiện; akusalavippayutta- = … với các hiện tượng bất thiện
kusalavippayuttaakusalavippayuttacittassa uppādakkhaṇe = khoảnh khắc sinh khởi của tâm không gắn liền với các hiện tượng thiện và không gắn liền với các hiện tượng bất thiện; akusalavippayuttakusalavippayutta- = the same in that order
cittassa uppādakkhaṇe / cittassa bhaṅgakkhaṇe = khoảnh khắc sinh khởi / tan rã của tâm; Aggamaggassa = con đường tối thượng; citte = tâm; akusale citte = tâm bất thiện; vattamāne = khi … đang diễn ra; cittassa (yassa cittassa anantarā) = tâm; anantarā = ngay sau (= 5-01)

## Persons, beings, planes (= 2-01 / 5-01 / 8)
upapajjantānaṃ = đang tái sinh; cavantānaṃ = đang chết đi; nirodhasamāpannānaṃ = người nhập thành tựu thiền chấm dứt; asaññasattānaṃ = chúng sinh Vô Tưởng; Suddhāvāsānaṃ = chúng sinh trong cõi Tịnh Cư; Suddhāvāsaṃ = cõi Tịnh Cư
Arūpe / arūpe = cõi không hình sắc; Pañcavokāre / pañcavokāre = cõi gồm năm khối; Catuvokāre = cõi gồm bốn khối; Asaññasatte = cõi Vô Tưởng; pavatte = đời sống
Itaresaṃ = chúng sinh khác (before catuvokārānaṃ pañcavokārānaṃ; pañcavokārānaṃ then = cõi gồm năm khối) / người khác (alone)
Aggamaggasamaṅgīnaṃ = người có được con đường tối thượng; arahantānaṃ = bậc A-la-hán; Pacchimacittasamaṅgīnaṃ = người có được tâm cuối cùng; aggamaggaṃ paṭilabhissanti = sẽ đạt được con đường tối thượng
Natthi = không có

## Verbs (map_2-01_vi.verb_value, first rendering in the segment)
uppajjanti / uppajjantīti = sinh khởi; uppajjittha / uppajjitthāti = đã sinh khởi / chưa từng sinh khởi (under na); uppajjissanti / uppajjissantīti = sẽ sinh khởi / sẽ … sinh khởi (under na); Uppajjittha / Uppajjissanti (short answers) = đã sinh khởi / sẽ sinh khởi
bhāvanāvāra (9-03 ^6-9-229; BHAVANA, bhavana_value): bhāveti / bhāvetīti = tu tập (under a separate na «không tu tập»: na = không); pajahati / pajahatīti = dứt bỏ; nappajahati / nappajahatīti = không dứt bỏ (= 7-01 VERBS)

## Headings
Dhammayamakaṃ (heading) = Các cặp câu hỏi về các hiện tượng; in the closer «Phần các cặp câu hỏi về các hiện tượng đã hoàn tất» (9-03) = các cặp câu hỏi về các hiện tượng (lower case as written; TITLE9)
Paṇṇattivāro = mục về sự định danh; Paṇṇattiniddesavāro = mục giải thích về sự định danh; uddeso = phần nêu đề mục; niddeso = phần giải thích
Padasodhanavāro = mục về sự làm sáng tỏ thuật ngữ; Padasodhanamūlacakkavāro = mục về vòng luân chuyển dựa trên sự làm sáng tỏ thuật ngữ
Suddhadhammavāro = mục về các hiện tượng thuần túy; Suddhadhammamūlacakkavāro = mục về vòng luân chuyển dựa trên các hiện tượng thuần túy (inner «các» kept, = 5-01 Suddhasaccavāro)
anulomaṃ / paccanīkaṃ = chiều thuận / chiều nghịch; anulomapuggalo … paccanīkapuggalokāsā = chiều thuận / chiều nghịch theo người / theo nơi chốn / theo người và nơi chốn
Pavattivāro = mục về sự diễn tiến; Uppādavāro = mục về sự sinh khởi; Atītānāgatavāro = mục về quá khứ và tương lai; Nirodhavāro = mục về sự chấm dứt; Bhāvanāvāro (9-03) = mục về sự tu tập

## CROSSCHECK
Kusalaṃ / Akusalaṃ / Abyākataṃ = «hiện tượng X» here (first occurrence = object of ṭhapetvā) vs the sample's kusalaṃ = «thiện» (first occurrence = predicate): same first-occurrence rule, different first occurrence.
kusalā dhammā = contiguous «hiện tượng thiện» here (the Dhammayamaka questions write «các hiện tượng thiện») vs the sample's discontinuous «hiện tượng … thiện» (mūlayamaka «Bất cứ hiện tượng nào là thiện»).
kusalānaṃ uppādakkhaṇe and the -vippayutta cittas keep the inner «các» («của các hiện tượng thiện», «với các hiện tượng thiện»), as written.
uppajjissanti «sẽ sinh khởi» vs «sẽ … sinh khởi» (^6-9-63 … 68, 84, 85, 87, 88, 94, 95, 97); uppajjittha «đã sinh khởi» vs «chưa từng sinh khởi» (^6-9-51 … 56, 77, 78, 94 … 98): all from map_2-01_vi.verb_value (separate na first in the segment).
Itaresaṃ = chúng sinh khác (^6-9-49, 50, 61, 62, 92, 93) / người khác (elsewhere): 2-01 / coordinator position rule.
