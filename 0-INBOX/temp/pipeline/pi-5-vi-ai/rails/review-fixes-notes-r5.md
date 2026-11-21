# pi-5 Vietnamese rails: review fixes, part r5 (ch23-ch31), 2026-11-22

Script: rails\review_fixes_r5_vi.py (builds from rails\backup-pre-review\<ch>.md, asserted counts). Log: rails\review-fixes-log-r5.tsv.

## Lines changed
ch23 3, ch24 1, ch25 7, ch26 11, ch27 1, ch28 8, ch29 0, ch30 9, ch31 3 (43 lines).
Replacements per decision: B3 16, B9 13, A19 11 (incl. 2 with the ^5-825 reason form, 1 in the ch26 uddāna), A6 6, B16 6 uddānas, B14 3, A3 2, A4 2, A5 2, B10 2, A2 1, B17 1, minor 20.

## Final wording
- A2 ^5-871: «người giữ voi, người giữ ngựa».
- A3 ^5-742: «Pun-na» in all three places.
- A4 ^5-870: «có con voi chúa có tên là Ê-ra-va-na, và cỗ xe cõi trời do một nghìn con kéo» (question and «Nếu» clause).
- A5 ^5-798: «Làm phước dẫn đến tái sinh, …» (both stanzas); typography: no close quote after stanza 1, stanza 3 opens with “.
- A6 ^5-787, ^5-917, ^5-918: «Chẳng phải Đức Thế Tôn đã nói rằng cái gì vô thường thì cái ấy là khổ đau [...], và đã nói – “X” sao?»; «Nếu Đức Thế Tôn đã nói rằng …, và đã nói – …, thì này bạn, …».
- A19 ch26 ^5-823–827: «người đang nhập thiền» (bare «người đang nhập» ^5-823 and every «người đang nhập thành tựu thiền»); objects kept (ch23 «người đang nhập sự chấm dứt tri giác và cảm giác», ^5-825 «người đang nhập lĩnh vực …»).
- B3 ^5-777, ^5-894: «tạo nghiệp dẫn đến …».
- B9 ch30 ^5-903–905: «Có phải không tồn tại bất cứ tính chất làm điều kiện thực hành nào không?» / «Vậy thì có tồn tại tính chất làm điều kiện thực hành nào đó.»; uddāna ^5-907 «không tồn tại bất cứ …».
- B10 ^5-738, ^5-742: «… không? Đúng vậy.» / «… không? Không nên nói như vậy…». ^5-905 already had «Có bài kinh như vậy thật không? Đúng vậy.» (no change).
- B14 ^5-861, ^5-862: kappaṭṭho «lưu lại suốt một kiếp» («không lưu lại suốt một kiếp»).
- B16: semicolons in the vagga uddānas of ch23, ch25, ch26, ch27, ch28, ch31 (each has an item containing a comma); ch24, ch29, ch30 and the fifty-group uddānas keep commas.
- B17 ^5-798: «Đế Thích, vua của chư thiên».
- Minor: ^5-770 «Chẳng phải vật chất do nghiệp thuộc cõi dục lạc đã được tạo là thuộc cõi dục lạc sao?» (and the «Nếu» clause / conclusion); ^5-809 «cơm và món đậu nấu»; ^5-820 paṭuppanna «đã sinh khởi» (4×); ^5-825 «Có phải vì Đức Thế Tôn đã nói …, nên người đang nhập thiền …», «…, nên người ấy có …»; ^5-826 touch branch «chạm vào / nhận biết rõ vật chất bằng vật chất»; ^5-868 kuṭhārī «rìu», vāsī «rìu lưỡi ngang»; ^5-877 «cần được dứt bỏ», fifty-group «các phiền não thuộc quá khứ»; ^5-892 «không có phiền não» (= ^5-881).

## Not applied / kept
- ^5-900 Tissopikathā «Cả ba phần bàn»: kept (B18), the reviewer's rename was optional.
- ^5-912 «Linh hồn và thân thể là một» / «Linh hồn là khác, thân thể là khác» already = pi-1 (B4, no change).
- ch24 «có vật chất thuộc cõi hình sắc …» (atthi rūpaṃ rūpāvacaraṃ) left «có»: not flagged; coordinator may decide under B9.
- ^5-798 stanza 1 «… ở đâu có quả lớn.» is a question but the Pāli has no «?»; left.

## For the coordinator (shared with other parts)
- r4 ch21 verse ^5-657 is the same verse as ^5-862: line 1 should read «Kẻ chia rẽ Tăng đoàn thuộc cõi khổ, là chúng sinh địa ngục, lưu lại suốt một kiếp;».
- ^5-742 fifty-group uddāna «Các khuynh hướng tiềm ẩn, sự thu thúc, kiếp, gốc rễ, và được xác định riêng biệt.» names ch19-ch23 by keyword («kiếp» for ch21); unchanged.
- ^5-877 fifty-group uddāna now «Sự chế ngự, sự tích lũy phước, đã sống, các phiền não thuộc quá khứ, và kẻ giết mẹ.».
- «tạo nghiệp dẫn đến cõi tái sinh / sự hiện hữu / quyền uy …» (arahant puññūpacaya list), «Đế Thích», «ngựa», «người đang nhập thiền», B9 and B16 forms should match the other parts.
- Termbase entries now stale: assa «ngựa đực»; sakko «Sakka»; opadhikaṃ «còn chấp trước»; kummāsaṃ «cháo»; vāsīhi «rìu»; kuṭhārīhi «búa»; ṭho (kappaṭṭho) «tồn tại»; kammaṃ karoti «làm nghiệp», kammaṃ karoti kāyena «làm nghiệp bằng thân», kammaṃ karonto «trong khi … làm nghiệp».

## Stale builders
build_rails_23 … 31_vi.py no longer match their chapters (old strings found in build_rails_23 (5 hits), 25 (3), 26 (6), 28 (9), 30 (5); the others compose the changed strings or uddānas from pieces). Do not rebuild these chapters from their builders.

## Checks (all nine chapters)
check_chapter_ids OK; dashcheck 0 mismatches; verify_rails_vi OK; no «—», «:-», «….», «được được», «là là», «chánh niệm», «seed», double spaces, CR; 0 hits of the replaced strings (asserted in the script).
