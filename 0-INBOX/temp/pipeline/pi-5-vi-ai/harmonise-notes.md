# pi-5 Vietnamese zero-shot: harmonise pass (2026-11-21), decisions and remaining divergences

Script: harmonise_vi.py (exact strings, scoped to one segment or one file, asserted counts; rules run in order; reads backup-pre-harmonise/, so rerunnable; dashes, ellipses, block IDs, heading levels and brackets asserted unchanged except the HB bracket rules, which keep every Pāli word). Log: harmonise-log.tsv (291 entries). Divergence finder: find_divergences_vi.py (divergences-pre.md = before, divergences.md = after). Helpers (pi-5 files only): vi_common.py, probe_vi.py, probe_terms_vi.py, builder_hits_vi.py. Adapted from the pi-4 tools (pi-4 files untouched). Precedence used: (1) the approved sample, (2) pi-1-4 wording (pi-1 first), (3) coordinator-rules.md, (4) majority / earliest pi-5 form. The sample (preamble, 1-puggalakatha) is byte-identical to the backup. Builders not rerun.

## Lines changed
ch3 21, ch4 4, ch5 8, ch6 13, ch7 8, ch10 18, ch11 15, ch12 14, ch13 5, ch15 16, ch16 17, ch17 10, ch18 1, ch19 7, ch20 10, ch21 2, ch22 11, ch24 4, ch25 2, ch26 1, ch27 3, ch28 3 (total 193). Unchanged: sample, ch2, ch8, ch9, ch14, ch23, ch29, ch30, ch31.

## Checks (after the pass)
All 32 files: check_chapter_ids OK (1,400 segments), dashcheck 0 mismatches / 0 extra em-dashes, pi-1-vi-ai\verify_rails_vi.py OK; NFC; no CR; no «—», «:-», «….», «là là», «được được», «chánh niệm».

## Named points: as written
- ch4 ^5-281 Sunetta: both ananubodhā appaṭivedhā restored in one sentence as the Pāli («… trí tuệ cao quý, do không hiểu ra, không thấu triệt sự giải thoát cao quý»; no «và», no ca); natthi dāni punabbhavo «nay không còn sự hiện hữu mới nữa» (pi-2, ch12).
- ch7 ^5-299 l.14: second dhammā restored («…, các hiện tượng một phần có quả chưa chín muồi …»).
- ch12 ^5-405 kamuddiseyyaṃ. → «Ta sẽ tôn xưng ai.» (Pāli full stop, question word kept).
- ch27 heading (188) 3: full stop removed («(188) 3 Bàn về …»).
- ch3 ^5-269 ruhiruppādaka: «kẻ làm chảy máu» (×2, «Như Lai» dropped).
- Added words: «chúng» ch7 ^5-299 (×2), ^5-300 (×2), ch15 ^5-476 (×4) dropped in the «vì cho rằng …» clause (no subject needed; ch11 form), kept as the main-clause subject («…, chúng thuộc hiện tại», «…, chúng là yếu tố đồng hành …»), which Vietnamese needs. «sẽ» in cakkavattisatta dropped (ch12 ×13, ch15 ×4: «người làm vua chuyển luân»; not needed, as bodhisatta «Bồ-tát»). «là bậc» in uḷāro dropped (ch13 ^5-423 ×4: «Đức Thế Tôn vĩ đại»; adjective predicate). ch3 ^5-274…277 «Có phải người ấy một phần …» → «Có phải một phần …» (×16; «người ấy» not in the Pāli; identical sentence in ch11 ^5-366).

## Named points: sample wins
- ch3 ^5-270 Āmantā? «Đúng vậy?».
- iṭṭhaphala family = sample ^5-98/99: «có kết quả đáng mong muốn, có kết quả đáng yêu mến, có kết quả đáng ưa thích, có kết quả không pha tạp, đưa đến sự dễ chịu, có quả trổ dễ chịu» and negatives (ch10 ^5-338, ch15 ^5-479, ^5-482; ch15 ^5-486 sukhavipāka; ch19 ^5-624 dukkhavipāka «có quả trổ khó chịu»). ch16, ch18 already sample.
- savipāka «có quả trổ», avipāka «không có quả trổ» (sample savipāka; ch18, ch22): ch7 ^5-299, ch15 ^5-499/500, ch20 ^5-633…635, ^5-653. saphala «có kết quả» was already uniform.
- parakataṃ sukhadukkhaṃ: ch15 ^5-488 → «sự dễ chịu và sự khó chịu do người khác làm ra» (sample ^5-173, ch25).
- Nanu vuttaṃ bhagavatā – "…"ti?: ch25 ^5-795 → «Chẳng phải Đức Thế Tôn đã nói thế này sao – “…”?» (sample NANU_VUTTAM; all other chapters already used it).
- The sukha / dukkha debate frames ((158) ch24 = sample ^5-179) needed no other change.

## Named points: pi-1-4 wins
- punabbhava (ch4) above. gotrabhū ch11 «người chuyển đổi dòng dõi» (×2). nekkhamma ch10 «sự từ bỏ». kanta / manāpa = pi-2 «đáng yêu mến» / «đáng ưa thích» (ch10, ch15 ^5-486, ch16, ch22 ^5-708; manuñña = sample «đáng ưa thích»).
- patthanā = pi-1 «sự mong ước», pattheti «mong ước» (ch15, ch16, ch17 ^5-552, ch18 ^5-573, ch20 ^5-636; ch21 / ch22 already).
- apubbaṃ acarimaṃ = pi-2 «không trước không sau» (ch3 ^5-273 ×4, ch4 ^5-280 ×4; the agents-run said ch4, the long form was in both).
- Sense verbs = pi-2 order «thấy hình sắc bằng mắt …» (ch5 ^5-289 incl. «thuộc quá khứ …», ch10 ^5-336, ch12 ^5-397, ch16 ^5-521/522). paṭivijānāti «nhận biết rõ» (ch10 ^5-347, ^5-352; ch5 has only vijānāti «nhận biết»).
- ariyo aṭṭhaṅgiko maggo = pi-2 majority «con đường gồm tám chi phần cao quý» (4 of 5 in pi-2; pi-3 has the other order): ch28 ^5-874/875.
- ch6 "paññatti…pe…" kept «khái niệm…»: it is the truncated pi-1 triad niruttipatha / adhivacanapatha / paññattipatha, where pi-1 has paññatti «khái niệm», paññattipatha «phạm vi của khái niệm»; the sample's «sự định danh» is the debate's paññatti (designation of a person).
- Also found: pariyāpanna = pi-1 / pi-2 «nằm trong» (maggapariyāpanna «nằm trong con đường»): ch10 ^5-334, ch15 ^5-471, ch17, ch19, ch22 (incl. the (142) heading / closing «những gì nằm trong»); ch22 Pariyāpannakathā saddadhātu … phoṭṭhabbadhātu = pi-2 «yếu tố âm thanh … yếu tố vật xúc chạm», saddarāga … «sự tham đắm âm thanh …» (= ch24's identical phrases; rūpa- / arūpadhātu stay «cõi»).

## Named points: one word in one sense
- anāsava ch12 ^5-392 arahā anāsavo → «không phải là đối tượng của ô nhiễm» (one word through the argument; pi-1). ch10 ^5-338 sāsavaṃ / anāsavaṃ sukhaṃ «hạnh phúc còn / không còn ô nhiễm» kept (a list of kinds of happiness, not the argument's word; the predicate form would read as a sentence): listed below.
- ch26 (185) "Rūpena rūpaṃ paṭivijānātīti?" = «… nhận biết rõ vật chất bằng vật chất …» in both lines (paṭivijānāti is not a seeing verb; the next question Rūpaṃ manoviññāṇaṃ already has «vật chất»). passati keeps «thấy hình sắc bằng vật chất», phusati «chạm vật chất bằng vật chất».

## Named points: pick one
- yoni «cách sinh» (ch14 / ch16 majority; ch11 ×17 changed). sammukhībhāva: already one form («cùng hiện diện đối mặt nhau»; ch5 has sammukhībhāvo hoti, the others sammukhībhāvaṃ āgacchanti «đi đến chỗ …»: different Pāli), no change.
- sukhavedaniya «được cảm nhận là dễ chịu …» (ch15 earliest, 49 of 52): ch16 ^5-539.
- vipākābyākata «… không xác định về mặt đạo đức thuộc quả của nghiệp» (ch20 / ch30 majority): ch19 ^5-605, ch22 ^5-706 («thuộc loại quả» → «thuộc quả»), ch21 ^5-676 aligned to the same list; kiriyābyākata «… mang tính chức năng» (pi-1) unchanged.
- "X"ti vattabbo «nên gọi là» (sample): ch10 ×24, ch17 ×4; quotes only where the Pāli has them (already so).
- dhammappaṭisaraṇo «chỗ nương tựa của Giáo Pháp» (ch11 earliest, ch26): ch13 ^5-443, with the identical maggakovido list aligned to ch11.
- dadāti «cho», dānaṃ dadāti «thực hiện sự bố thí» (pi-4, ch15, ch25, ch28, ch30): ch13 ^5-432/434, ch25 ^5-798 (saṅghe dehi … dinne). āropeti «dâng (vòng hoa …)», anuppadeti, āhuneyya keep «dâng».
- buddho by sense: ch12 ^5-403 sāvako hutvā buddho hoti «trở thành Đức Phật» (the Bodhisatta becoming the Buddha); (38) bodhiyā buddho keeps the generic «bậc giác ngộ» (the bodhi / buddha play).
- samādhi / vīriya as list members = «sự định tâm» / «sự tinh tấn» (majority): ch11 ^5-371, ch16 ^5-527/532. A qualified samādhi (avitakko … samādhi, ariyo samādhi, the verse sīlaṃ samādhi paññā) keeps the core «định tâm».
- Variant labels: ch17 ^5-564 «[khác chính tả (Pī.): anāvaṭṭantassa; dị bản (Sī., Syā., Ka.): anāvajjantassa; …]» (spelling e/a vs other word, as ch15 / ch22).
- āneñja «trạng thái bất động» (pi-2): ch27 ^5-834 sutta title «Kinh Thích Hợp Với Trạng Thái Bất Động». ch11 ^5-367 and ch21 ^5-666 āneñjappatte «đạt đến sự bất động» kept: the identical formula is pi-4 wording (pi-4 ^4 Catukka / Pañcaka rails), which this pass does not change.
- saṇṭhāti by sense (no change): settling in a state / standing, enduring = «đứng vững» (ch2, ch4 fruits; ch30 ^5-906 the earth etc. "in one mind-moment"), coming into being = «hình thành» (ch15 the earth forms first, ch21 the eon, ch22 the sense organs in the womb).
- yoniso / ayoniso manasikāra: already one pair «chú tâm đúng cách / không đúng cách» (pi-1 / pi-4 yoniso «đúng cách»); pi-2 has ayoniso manasikāro «sự chú tâm không khôn ngoan» (listed below).
- Fifty-group closes: same frame in ch13, ch18, ch23, ch28, ch31 (name line, «Tóm tắt …», items); ch28 ^5-877 aṭṭhāsi «đã sống» (= ch26 thesis / uddāna); atītena «với quá khứ» kept (ch27 uses «quá khứ»; instrumental as written). ch31 navaṃ «Điều mới» and nibbuti «sự nhập Niết-bàn» kept: ch29 renders navaṃ kataṃ «đã được làm mới» (same word «mới»), and nibbuti has no pari- (ch30 parinibbāna «… trọn vẹn»); the other ch31 items already match the fifty-group names.
- anicca list as predicate: affirmative «X là vô thường, …» (sample ^5-95, ch25, ch31), negative «X không vô thường, …»: ch27 ^5-832 «khối tạo tác là vô thường» (×2).
- ch31 book end kept (accepted).

## Other divergences found and settled
- atīta / anāgata / paccuppanna as attribute = «thuộc quá khứ / thuộc tương lai / thuộc hiện tại» (pi-1, pi-2 rūpaṃ atītaṃ «vật chất thuộc quá khứ»; ch5, ch19): ch6 ^5-297/298 (the identical atītaṃ rūpaṃ atthīti in ch5), ch21 ^5-655 (= ch19 ^5-621), ch5 ^5-296 «các vị Phật thuộc quá khứ». The approved headings (Atītakkhandhādikathā «các khối quá khứ …», Atītacakkhurūpādikathā) are terms-file wording and stay.
- ch6 ^5-298 ye keci saṅkhārā «bất cứ các tạo tác nào» (= ch5 ^5-296).
- ch5 ^5-296 Phagguna's question ends "paññāpeyyāti." / "paññāpeyyā"ti.": Pāli full stop kept («… mô tả được không. …», «… không”.»), coordinator rule.
- samāpattesiya / upapattesiya «tìm cầu …» (ch12, ch16, ch18, ch22): ch24 ×41; the identical sentence in ch22 ^5-703/704 put in ch24's order (instrumentals before sahagato, as the Pāli, which keeps the …pe… cuts in place).

## Remaining divergences (divergences.md after the pass)
(a1) 0, (a2) 0, (b) 0. (a3) 7: ch1 ^5-229 statement vs question frame (sample, positional); katame / katamāni pañca / tayo / tīṇi with the classifier of what is counted («năm loại / hiện tượng / điều / năng lực», «ba bậc / điều / mắt»): kept, Vietnamese needs the classifier; ch3 ^5-272 two items: a sentence-split artefact (Pāli "Tattheva." answers). (a4) 33: positional artefacts of the …pe… split (a member that carries the next clause, a frame «đối với / vì cho rằng / là», negated repeats «không thể nhận …» in ch20 ^5-651, the genitive «của» in ch23 ^5-726), checked one by one; none is a different rendering of the same Pāli word. (d) 10: closing names whose Pāli differs from the heading (as written). (e) 7: ch1 ^5-234 and ch3 ^5-272 sentence-split artefacts (sample / as written).

## Builder constants that would need the same change (builders not rerun; builder_hits_vi.py, line numbers)
build_3 64, 79, 155 (+ assembled: ^5-270, ^5-274…277); build_4 90, 125, 128; build_5 190 (+ assembled sense / full-stop strings); build_6 53 (+ assembled time attributes); build_7 40 (+ assembled «chúng», dhammā); build_10 260, 293, 311, 315, 317, 361-374, 808-826, 900-999; build_11 221, 349 (+ ^5-371); build_12 205, 503, 533 (+ ^5-392, ^5-397); build_13 93, 94, 154, 223; build_15 72, 113, 119, 165, 167, 176-178, 328, 330 (+ ^5-488, ^5-499/500, cakkavatti); build_16 198, 316, 320 (+ ^5-521/522, ^5-539); build_17 60, 146, 148, 388-406, 507, 523 (+ ^5-564 bracket); build_18 (^5-573); build_19 52, 89, 191, 194, 450; build_20 84, 416 (+ ^5-636); build_21 213 (+ ^5-655); build_22 54, 281, 282, 344 (+ ^5-703/704/706); build_24 225, 226, 469; build_25 (assembled ^5-795, ^5-798); build_26 (^5-826); build_27 117 (+ heading (188), ^5-832); build_28 152, 220. Builders that import another chapter's constants may carry the old string too.

## For the user (not decided here)
- dukkha in kāyikaṃ / cetasikaṃ dukkhaṃ and sukha / dukkha as feelings: ch14 ^5-452 every dukkha «khổ đau» (incl. kāyikaṃ / cetasikaṃ dukkhaṃ, soka …), ch10 ^5-338 «khổ đau thuộc thân / thuộc tâm», «hạnh phúc thuộc thân / thuộc tâm», ch17 (90) «hạnh phúc / khổ đau»; pi-1 / pi-2 feeling terms «dễ chịu / khó chịu» (and «sự khó chịu» in the soka … list).
- Condition names (ch13, ch23): hetu «nguyên nhân» vs pi-1 «gốc rễ»; adhipati «chi phối» vs pi-1 «yếu tố chủ đạo»; samanantara ch13 «kế cận liền ngay» vs pi-2 «liền sau» (ch22 samanantarā «liền sau»); āsevanā (ch23 / ch30 «thực hành»); saṅkhārā «các sự tạo tác» (pi-2 paṭicca) vs «các tạo tác» (sample khandha).
- saṃvara «sự phòng hộ» (ch20) vs pi-1 indriyasaṃvara «sự thu thúc».
- niyata «cố định» (ch20, ch27, ch29) vs pi-4 «có hướng đi cố định».
- «một bậc A-la-hán» (pi-2 string, ch20) adds «một».
- dhammataṇhā ch21 «khao khát đối tượng của ý» (pi-1) loses the dhamma word play.
- upaṭṭhāka ch29 «người thị giả» vs pi-4 «người chăm sóc».
- tiṭṭhati «tồn tại» (ch19, ch21, ch29) collides with atthi «tồn tại».
- «Tóm tắt của chương này –» for Tassuddānaṃ («chương» not in the Pāli); byte-identical also where it introduces a fifty-group uddāna (ch18, ch23, ch28, ch31).
- kāraṇika split by context (ch28).
- (126) heading Kappaṭṭhakathā «Bàn về người tồn tại suốt một kiếp» makes the thesis tautologous (ch21).
- Also from this pass: ch10 ^5-338 sāsavaṃ / anāsavaṃ sukhaṃ «hạnh phúc còn / không còn ô nhiễm» (one-word rule would give «… là / không phải là đối tượng của ô nhiễm»); pi-2 ayoniso manasikāro «sự chú tâm không khôn ngoan» vs pi-5 «chú tâm không đúng cách»; ch22 dhātu: rūpa- / arūpadhātu «cõi» next to saddadhātu «yếu tố âm thanh» (the realm / element pun is lost, as ch24 notes).
- Names in Pāli spelling (other names are Vietnamised), with a proposed Vietnamese form: Seniya (sample ^5-236 the ascetic; ch29 ^5-884 vua Seniya Tần-bà-sa-la) «Sê-ni-gia»; Soma (ch28 ^5-867, the moon deity) «Sô-ma»; Yama (ch28 ^5-867, king of the dead) «Diêm-ma» (or «Dạ-ma»); Subhadda (ch28 ^5-875) «Tu-bạt-đà-la».
