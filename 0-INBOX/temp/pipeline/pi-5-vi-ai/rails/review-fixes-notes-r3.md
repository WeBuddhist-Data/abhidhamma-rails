# pi-5 Vietnamese rails: review fixes, part r3 (ch11-15), 2026-11-22

Brief: vi-review-fixes-brief.md (user decision "Approve as proposed"). Findings: review/findings-r3.md, review/findings-summary.md.
Script: review_fixes_r3_vi.py (explicit replacements, block-anchored where possible, every count asserted; runs from backup-pre-review/ so it can be re-run; `check` subcommand). Log: review-fixes-log-r3.tsv (113 replacements). Backups: backup-pre-review/11-…15-*.md (made once).

## Lines changed
ch11 20, ch12 19, ch13 13, ch14 2, ch15 14.

## Per decision
- A1 ^5-384 Nanu: full six-item list «… cõi tái sinh có tri giác, nơi cư trú của chúng sinh có tri giác, vòng luân hồi có tri giác, cách sinh có tri giác, sự có được …» (the Hañci clause keeps «…», = Pāli …pe…).
- A2 ^5-402 «báu vật ngựa»; ^5-387 hatthigavassavaḷavaṃ «voi, bò, ngựa và ngựa cái» (was «ngựa đực và ngựa cái»; the mare stays).
- A14 ch13 ^5-424–427, uddāna ^5-444: «hiểu biết sai lệch» (16×); heading / closing «Bàn về điều sai lệch» kept (reviewer).
- A15 ^5-367: «hoặc đã tham đắm hoặc không tham đắm, hoặc đã sân hận hoặc không sân hận, …» (Nanu and Hañci).
- A16 ^5-367: «đang bị phiền não làm vẩn đục».
- A17 ch13 ^5-421/422: «chạm đến bằng thân rồi an trú» (7×).
- A18 ^5-501: «Có phải như vậy, với quả ấy rồi quả của quả ấy nối tiếp nhau, không có sự đi đến tận cùng của khổ đau, …».
- B6 ch11 kathā 28: «thiên nhĩ» (19×: heading «Bàn về thiên nhĩ», theses, sutta, closing). Uddāna «Tai được hiện tượng hỗ trợ» has no dibbasota word: unchanged.
- B16: ch12 ^5-417 «…các tướng; Bồ-tát đã bước vào sự cố định, đã sống đời sống tu hành trong sạch; người đang thực hành …» (the one item with an inner comma); ch11 ^5-386 «…năm năng lực; mắt.» and evameva bhavaggaṃ «cũng vậy với đỉnh cao của sự hiện hữu» (= ch12 / ch14 «cũng vậy với …»; removes the inner comma). The ch11 verse uddāna keeps its line-final «;» because the Pāli verse has them (only Pāli commas are separators). Reading used: a separator next to an item that contains a comma is «;», the rest «,».
- Minor (A20): ^5-356 «[sự phủ nhận ở đây nhắm vào …]»; ^5-366 «một phần không được trang bị giới hạnh …»; ^5-369 amaggena «bằng cái không phải là con đường» (3×); ^5-372 «đứng ở phía người phàm phu» (2×); ^5-382 «nhưng không dùng tri giác ấy để làm việc của tri giác» (2×); ^5-392 «cái là đối tượng của ô nhiễm ấy» (8×, all four identical lines); ^5-396 / ^5-399 / ^5-412 «Có phải vì …, nên … không?» (13 questions); ^5-398 «nhưng không dùng sự giác ngộ ấy để …» (8×); ^5-405 «cần được dứt bỏ»; ^5-450, ^5-454 «“Này các tỳ-khưu»; cetasiko dhammo «hiện tượng đồng hành với tâm» in ch15 everywhere (kathā 65 and 66 theses, verse ^5-477 «các hiện tượng đồng hành với tâm», uddāna; 17×, so identical Pāli stays identical; cetasika as a noun / predicate «yếu tố đồng hành với tâm» and the heading unchanged); ^5-486 «định tâm không thể đo lường» (2×); ^5-491 l6 final «.».
- Kept by decision: ^5-392 l4 anāsava of the arahant (B15); ^5-373–376 dhammupatthaddhaṃ (B18); ^5-405 / ^5-425 source wording (B11).

## Not applicable in r3 (checked)
A19 (no bare samāpanna; every samāpanna has an object), B3 (ch15 ^5-493 already «tạo nghiệp»), B4, B5, B7 (no handa), B8 (no uppādino), B10 (no "…ti, āmantā." without «?»), B14, B17 (no Sakka), A12, A13. B9: ch11 ^5-381–385 saññā atthi with a locative and ch15 natthi ariyadhammavipāko (possessor) keep «có»; ch13 existence theses already «tồn tại».

## For the coordinator / user
- A19 wording: ch13 kathā 45 "pathavīkasiṇaṃ samāpattiṃ samāpannassa" reads «người đang nhập thành tựu thiền với đề mục bao trùm là đất» (18×). «thành tựu thiền» here renders the Pāli object samāpattiṃ, so I kept it (brief: "where an object already follows, keep it"). If the coordinator wants «người đang nhập thiền …» there too, it is one rule; the same kasiṇa frame is in ch24 (r5).
- The formula "Xti, Yti?" = «Có phải nếu X, thì Y không?» (vi-rails-formulas.md) now has a reason-clause exception at ^5-396 / 399 / 412 (reviewer: the …ti gives a reason). Other parts keep the formula unless their reviewer asked.
- Strings that may also occur in other parts (same fixed wordings, not edited by me): dibbasota «thiên nhĩ» (any iddhi / abhiññā list); assa / hatthigavassavaḷava; amaggena; puthujjanapakkhe ṭhito (SN 5.488); kāyena phusitvā viharati «rồi an trú»; cetasiko dhammo; kilissamānaṃ.
- No kathā name changed except ch11 kathā 28 («Bàn về thiên nhĩ»); the ch13 fifty-group uddāna (^5-444) does not name it. No other part's uddāna is affected.
- Termbase entries now differing from the rails (for the termbase alignment, section C): dibbasota / dibbasotaṃ «tai thuộc cõi trời» → «thiên nhĩ»; viparīte ñāṇaṃ «hiểu biết về điều sai lệch» → «hiểu biết sai lệch»; kilissamānaṃ «… ô nhiễm» → «… vẩn đục»; amaggaṃ / amagge «đường sai» (amaggena now «cái không phải là con đường»); cetasiko «yếu tố đồng hành với tâm» (as an adjective of dhammo now «đồng hành với tâm»).

## Stale builder constants (builders not re-run)
build_rails_11_vi.py: «[ở đây, đây là sự phủ nhận …», «đang bị phiền não làm ô nhiễm», «bằng đường sai», «đứng vững ở phía người phàm phu», «tai thuộc cõi trời», «nhưng bằng tri giác ấy mà không …», plus the ^5-384 Nanu list, the «vừa … vừa» list, ^5-366, the uddāna lines.
build_rails_12_vi.py: «ngựa đực và ngựa cái», «báu vật ngựa đực», «ấy cần dứt bỏ’», plus ^5-392, ^5-396 / 399 / 412, ^5-398, ^5-417 (composed strings).
build_rails_13_vi.py: «bằng thân và an trú», «hiểu biết về điều sai lệch».
build_rails_14_vi.py: «“này các tỳ-khưu, có bốn điều này» (and the ^5-450 opening).
build_rails_15_vi.py: «định tâm không thể đo lường của tâm», «biết ơn, ghi nhớ ơn,», plus cetasiko dhammo and ^5-501 (composed strings).

## Checks (all five chapters)
check_chapter_ids.py OK; dashcheck.py 0 dash-line mismatches, 0 extra dashes; verify_rails_vi.py OK; no «—», «:-», «….», «được được», «là là», «chánh niệm», the forbidden word of the brief, double spaces, CR; NFC; 0 residual hits of the replaced strings (`review_fixes_r3_vi.py check`).
