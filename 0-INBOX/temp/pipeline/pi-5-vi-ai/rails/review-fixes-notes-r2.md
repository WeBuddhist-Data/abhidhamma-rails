# Review fixes, part r2 (ch3-ch10): notes for the coordinator (2026-11-22)

Script: rails\review_fixes_r2_vi.py (builds from rails\backup-pre-review\<ch>.md, asserted counts); log: rails\review-fixes-log-r2.tsv (145 rows).

## Lines changed
ch3 6, ch4 0, ch5 5, ch6 2, ch7 6, ch8 1, ch9 0, ch10 75. Replacements per decision: A7 78, A19 47, B8 21, minor (A20) 51, A2 1, A8/B7 1, B10 1.

## Final wordings
- A7 (^5-312, 316, 320, 324): sadhammakusala «thông thạo lĩnh vực của riêng mình», paradhammakusala «thông thạo cả các lĩnh vực khác» (39 + 39). Followed the summary wording; the reviewer's extra «chỉ» was not added.
- A8 / B7 (^5-308): «Vì lý do gì? Vì họ có ý: “Nào, chúng ta sẽ khiến vị ấy rơi vào sự phân vân”.» Handa hi answering «Theo nghĩa nào?» stays «Bởi vì» (^5-272 ch3, ^5-307 ch10).
- A19 (^5-326 … ^5-333): 41 bare samāpanna «người đang nhập» → «người đang nhập thiền»; 6 × «người đang nhập thành tựu thiền …» → «người đang nhập thiền …». Where an object follows (tầng thiền, đề mục bao trùm, lĩnh vực …, sự chấm dứt tri giác và cảm giác) it is unchanged.
- A2 (^5-303): «báu vật ngựa».
- B8 (^5-300): uppādino «có tính chất sinh khởi», anuppādino «không có tính chất sinh khởi»; uppajjissanti stays «sẽ sinh khởi» (the tautology at ^5-300 is gone).
- B10 (^5-295): «Có phải hiện tại tồn tại không? Đúng vậy.»
- B16: ch9 / ch10 uddānas already use commas between items; the line-end «;» mirror the Pāli line-end semicolons (as in ch11). Unchanged.
- Minor: ^5-274 / ^5-340 «(không) được trang bị giới hạnh …»; ^5-276 «Dứt bỏ cả các phiền não …»; verse ^5-278, ^5-317, ^5-346 «Và cả giới hạnh và nghi thức, bất cứ điều gì còn có;»; ^5-288 «đã có rồi lại có, …» / «chưa có thì không có, …»; ^5-296 «?» ×2; ^5-298 «…, những điều ấy không tồn tại», «phạm vi của sự định danh…»; ^5-333 «đứng ở cõi Phạm Thiên»; ^5-338 «đưa đến khổ đau, có quả trổ là khổ đau» / «đưa đến hạnh phúc, có quả trổ là hạnh phúc»; ^5-339 anupubbena «theo tuần tự»; ^5-346 «chứ không đột ngột dốc thẳng xuống như vực», «chứ không đột ngột có sự thấu triệt …»; ^5-352 «điều không phải con đường», «điều không phải vật chất». ^5-282 left as is (reviewer: optional).

## Strings shared with other parts (check there)
- assaratana «báu vật ngựa đực» (pi-5 elsewhere; termbase entry).
- The Ratana-sutta verse line «Hoặc bất cứ giới hạnh và nghi thức nào có;» if quoted in another chapter.
- dukkhudraya / sukhudraya «đưa đến sự khó chịu / dễ chịu, có quả trổ …» if the formula recurs.
- samāpanna bare (ch19, ch21, ch26 per A19); uppādino if it recurs.
- ^5-338 line «Chẳng phải “cái gì vô thường thì cái ấy là khổ đau …,” Đức Thế Tôn đã nói, “tất cả các tạo tác đều vô thường” … sao?» is the A6 construction (no dash in the Pāli here); not in the A6 list, left unchanged: coordinator to decide.

## Stale builder constants (not rebuilt)
build_rails_3_vi.py (ariyakanta / verse), build_rails_5_vi.py (^5-288, ^5-295/296), build_rails_6_vi.py (^5-298), build_rails_7_vi.py (uppādino), build_rails_8_vi.py (assaratana), build_rails_10_vi.py (sadhamma, samāpanna, ^5-308, verse, ^5-333, ^5-338-340, ^5-346, ^5-352).

## Checks
check_chapter_ids OK, dashcheck 0 mismatches, verify_rails_vi OK for all eight chapters; no «—», «:-», «….», «được được», «là là», «chánh niệm», «seed», double spaces, CR; 0 residues of the replaced strings.
