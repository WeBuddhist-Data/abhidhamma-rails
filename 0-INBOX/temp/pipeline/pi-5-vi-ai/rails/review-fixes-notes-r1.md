# pi-5 Vietnamese rails: review fixes, part r1 (preamble.md, 1-puggalakatha.md, 2-parihanikatha.md)

2026-11-22. User decision "Approve as proposed" (review\findings-summary.md A + B, review\findings-r1.md).
Script: rails\review_fixes_r1_vi.py (builds from rails\backup-pre-review\, asserted counts, re-runnable).
Log: rails\review-fixes-log-r1.tsv (169 rows). Helpers used for reading only: review_show_r1.py, review_scan_r1.py.

## Applied
| decision | where | old | new | occurrences |
|---|---|---|---|---|
| B4 | ch1 ^5-91, 93, 227, 228 | «linh hồn cũng chính là thân thể» | «linh hồn và thân thể là một» (question «Có phải linh hồn và thân thể là một không?»); aññaṃ jīvaṃ aññaṃ sarīraṃ was already the pi-1 «linh hồn là khác, thân thể là khác» | 6 |
| A9 | ch1 ^5-104–106 | «“người có X đã chấm dứt”» | «“người có X ấy đã chấm dứt”» (every item written out) | 6 |
| A10 | ch1 ^5-195, 196 | «Ai …, có phải chính người ấy là người không? Ai không …, người ấy không phải là người sao?» | «Có phải ai … thì chính người ấy là người không? Có phải ai không … thì người ấy không phải là người không?» | 3 |
| B6 | ch1 ^5-194, 196 | «yếu tố tai thuộc cõi trời» | «yếu tố thiên nhĩ» | 2 |
| minor | ch1 ^5-91, 92 | «cùng với / không có sự tạo tác» | «cùng với / không có các tạo tác» | 2 |
| minor | ch1 ^5-214, 215 | «ba đặc tính (không) do điều kiện tạo thành của cái (không) do điều kiện tạo thành» | «ba đặc tính riêng của cái (không) do điều kiện tạo thành» | 2 |
| minor | ch1 ^5-227, 228 | «… có phải nếu nhìn …, thì linh hồn là khác …» | «… nhìn …. Có phải linh hồn là khác …» (the plain-answer form of ^5-216) | 2 |
| minor | ch1 ^5-232 | «khi sinh khởi thì sinh khởi» | «khi đang sinh khởi thì sinh khởi» | 1 |
| minor | ch1 ^5-234 | «trống rỗng tự ngã» | «trống rỗng, không có tự ngã» | 6 |
| minor | ch1 ^5-235 | «hoàn toàn là một giáo pháp của kẻ ngu si trọn vẹn» | «hoàn toàn là lối nghĩ trọn vẹn của kẻ ngu si» (the reviewer wrote «kẻ ngu»; «kẻ ngu si» kept for bāla) | 2 |
| minor | ch2 ^5-242–246 (Hañci) and ^5-247–263 | «…, bậc X sa sút khỏi …» | «… mà bậc X vẫn sa sút khỏi …» | 93 |
| minor | ch2 ^5-250, 254–259, 263 (na parihāyati) | «…, bậc X không sa sút khỏi …» | «…, thì bậc X không sa sút khỏi …» (same link need; the «thì» frame of ^5-220) | 50 |
| A11 | ch2 ^5-265 | «cạm bẫy của dòng lũ đã được nhổ bỏ» | «dòng lũ và cạm bẫy đã được nhổ bỏ» | 1 |
| minor | ch2 ^5-268 | upacayaṃ gacchati «đi đến sự tích lũy» | «tăng trưởng» (ācinati keeps «tích lũy») | 10 |

Changed lines: preamble 0, ch1 18, ch2 81.

## Not applied / nothing to do
- MINOR note ^5-3, ^5-5 and the pentads (idaṃ te micchā «là sai lầm của bạn»): the reviewer marked it optional and it is the approved sample frame used book-wide; left as is (needs the user if wanted).
- MINOR ch2 parihāni «sự sa sút»: B12 says keep.
- B5: ^5-229 already reads «Đức Thế Tôn»; no lowercase «đức Thế Tôn» anywhere in the part.
- A2 assa, A19 samāpanna, B3 kammaṃ karoti (kammakārako «người tạo nghiệp» is already right), B7 Handa hi, B8 uppādino, B9, B10 (no "…ti, āmantā." in the Pāli of ch1 / ch2), B16 (no uddāna in the part), B17 Sakka: no occurrence in this part.

## Strings shared with other parts (for the coordinator)
- B4 «linh hồn và thân thể là một», B6 «yếu tố thiên nhĩ»: the fixed wordings; other parts apply the same.
- upacayaṃ gacchati «tăng trưởng», suññaṃ attena vā attaniyena vā «trống rỗng, không có tự ngã hay những gì thuộc về tự ngã», uppajjamānaṃ «khi đang sinh khởi», kevalo paripūro bāladhammo «lối nghĩ trọn vẹn của kẻ ngu si»: if these recur in another part, align.
- The ch2 link «mà … vẫn sa sút» / «, thì … không sa sút» for "X diṭṭhaṃ / pahīnaṃ / bhāvitaṃ, parihāyati …": if the same frame recurs elsewhere, align.
- No kathā name changed in this part; no uddāna to update.

## Stale builder constants (not rebuilt; chapters fixed in place)
- build_rails_sample_vi.py (preamble + ch1): line 349 JIVA «linh hồn cũng chính là thân thể»; 765 «sự tạo tác» (sasaṅkhāro); 819–831 niruddha() quote «người có X đã chấm dứt»; 1048 «tai thuộc cõi trời»; 1056–1059 and the check string at 1390 (the ^5-195 / 196 «Ai …, … sao?» frame); 1127, 1131 «ba đặc tính …»; 1176, 1179 the ^5-227 / 228 second answer; 1192 «khi sinh khởi thì»; 1203 «trống rỗng tự ngã»; 1226 «giáo pháp của kẻ ngu si».
- build_rails_2_vi.py (ch2): 163 «đi đến sự tích lũy»; 254, 255, 265 the Hañci «nhiều hơn, / vượt trội hơn,» clause; the question frames around 142–148 and 225–229 («…, bậc X (không) sa sút khỏi»); 399 «cạm bẫy của dòng lũ».

## Checks (all three chapters)
check_chapter_ids OK; dashcheck 0 mismatches (ch1 489 / 489 dashes, ch2 34 / 34); verify_rails_vi OK; «?» Pāli = Vietnamese (ch1 572 / 572, ch2 286 / 286); no «—», «:-», «….», «được được», «là là», «chánh niệm», the banned English word, double spaces, CR; 0 remaining hits of the replaced strings; LF, final newline.
