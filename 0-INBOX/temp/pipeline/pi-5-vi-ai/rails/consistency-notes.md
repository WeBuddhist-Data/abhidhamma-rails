# pi-5 Vietnamese rails: consistency pass (2026-11-21)

Brief: consistency-brief.md. Script: consistency_fix_vi.py (explicit replacements with asserted counts, run from the pre-fix copies in consistency/, re-runnable). Log: consistency-log.tsv (one row per replacement: file, block id, old -> new, reason). Scan after the fix: divergences-rails.md (consistency_find_vi.py).

Precedence used: termbase / APPROVED.md > pi-1 … pi-4 rails > the approved sample (preamble, 1-puggalakatha) and vi-rails-formulas.md > the earlier chapter. The sample was not changed.

## Changes per chapter (50 replacements, 13 chapters)

| chapter | n | what |
|---|---|---|
| 5 | 3 | etadavoca «điều này sao» ×2; «[trong Tăng Chi Bộ Kinh]» |
| 10 | 1 | etadavoca «điều này sao» |
| 11 | 3 | etadavoca «điều này sao»; magga list «Có phải là …» ×2 |
| 13 | 5 | «Kinh Phật Tự Thuyết 76»; «chỗ nương tựa về Giáo Pháp»; plural satipaṭṭhānā … bojjhaṅgā list «các …» ×3 (^5-429) |
| 17 | 4 | sutta quote «“Ở đây, này các tỳ-khưu» (^5-548); «Nó nằm trong khối nào?» ×3 |
| 19 | 3 | «Nó nằm trong khối nào?» ×3 |
| 21 | 1 | «Đức Phật xuất hiện ở thế gian» (^5-654) |
| 22 | 1 | «[trong Tăng Chi Bộ Kinh]» |
| 23 | 5 | «“Ở đời này, này Pun-na, có người» (^5-742 segment); magga list «Có phải là …» ×3; «Có phải đó không phải là người đang nhập sự chấm dứt không?» (^5-732) |
| 24 | 12 | samāpattesiya frame in ch22 order ×11 (^5-768, 769, 771, 773); etadavoca «điều này sao» |
| 26 | 7 | «sự mong cầu ấy là để …» ×6; «… là người đang nhập không?» (^5-823 segment) |
| 29 | 3 | plural list «các nỗ lực đúng đắn… các nền tảng thần thông… …» ×3 (^5-878) |
| 30 | 2 | etadavoca «điều này sao» ×2 |

## Known clashes 1-15

1. Nanu <name> bhagavantaṃ etadavoca: the sample (^5-234), ch12, ch25 «đã nói với Đức Thế Tôn điều này sao –»; ch5 changed. The same verb without bhagavantaṃ (ch5 Nandaka, ch10 Gavampati «với các tỳ-khưu», ch11 / ch30 Sāriputta, ch24 Udāyī) had «thế này sao»: aligned to the sample's «điều này sao» too (the Pāli etadavoca is the same; only the name / object slot differs). «Nanu vuttaṃ bhagavatā» (a different verb) keeps «đã nói thế này sao» everywhere.
2. udā. citation: «Kinh Phật Tự Thuyết» (ch10 ×5, ch19, ch20; every collection takes «Kinh …» in vi-rails-formulas.md); ch13 ^5-440 segment changed.
3. buddho loke uppajjati (ch21 ^5-654): «xuất hiện», by the termbase phrase entries sambuddhā / paccekasambuddhā uppajjanti «… xuất hiện» (the bare uppajjati «sinh khởi» entry is the generic sense), pi-4 «Như Lai xuất hiện ở thế gian», ch3, ch16.
4. "idha, bhikkhave …" sutta-quote opening: capitalised everywhere; ch17 changed. The ch14 «ở đây» is tatra inside a quote (not an opening: false hit); ch3 ^5-271 "idha brahmacariyavāso" is a thesis quote in lower case (kept: context).
5. idha … ekacco: «Ở đời này, … có người» (pi-1 idhekacco, pi-4, the sample ^5-236 «ở đời này, có bậc đạo sư», ch15 ^5-481, ch27). ch23 "idha, puṇṇa, ekacco" changed. "idha, bhikkhave, bhikkhu …" (no ekacco) keeps «Ở đây» (ch15, ch17, ch18, ch20, ch21, ch26): kept: context.
6. Tassa tasseva / Tāya tāyeva: ch19 refers to states (ṭhitatā, aniccatā, jarā, maraṇa: the regress of a state's own state) «từng cái»; the sample «từng người» refers to the person (kattā, paṭisaṃvedī): kept: context. Note for the user: ch15 ^5-501 (tassa vipāko vipākadhammadhammo) uses the sample's «từng người» although its referent is a result (a thing, as in ch19); left as written (it matches the sample).
7. Puṇṇa: ch22 ^5-707 (MN 2.79) and ch23 (MN 2.81) are both the Kukkuravatika sutta, the same Puṇṇa; not in the termbase, not in pi-1 … pi-4: the earlier chapter's «Pun-na»; ch23 changed («Phú-lâu-na» is the usual form of the other Puṇṇa, the Mantāṇiputta disciple).
8. Maggo phalaṃ nibbānaṃ … bojjhaṅgoti?: earlier chapter ch10 «Có phải là con đường, …» (ch12, ch22); ch11 ×2 and ch23 ×3 changed.
9. taṃ jīvaṃ taṃ sarīraṃ: sample differs. The sample (debate question, ^5-91 / 93 / 227 / 228) «linh hồn cũng chính là thân thể»; pi-1 (diṭṭhāsava / diṭṭhisaṃyojana lists), ch22 ^5-708 segment, ch31 ^5-913 «Linh hồn và thân thể là một» in the ten-views list. ch22 / ch31 follow pi-1 (precedence 2) and the sample is not edited; both wordings stay for the user.
10. samāpanno: termbase Samāpanno = «người đang nhập»; termbase phrases Samāpanno saddaṃ suṇāti / Samāpanno assādeti = «người đang nhập thành tựu thiền …» (ch21, ch26 follow them). The bare predicate "X-viññāṇasamaṅgī samāpannoti?" was ch19 «… là người đang nhập» vs ch26 «… là người đang nhập thành tựu thiền»: ch26 changed to the termbase / earlier wording. The phrase-entry subjects stay (termbase).
11. dhammappaṭisaraṇo: ch11 «chỗ nương tựa về Giáo Pháp» (ch26 follows); ch13 changed.
12. kammaṃ karoti / karonti: not identical Pāli, and the termbase has both: kammaṃ karoti «làm nghiệp» (ch16, ch21, ch22, ch25, ch30, pi-4), kammaṃ karonti «tạo nghiệp» (ch15 ^5-492 segment). Left for the user (termbase alignment).
13. cetiya / gift list: ch21 ^5-658, ch25 ^5-779 segment and ch30 ^5-901 already read identically (cho y phục … đảnh lễ bảo tháp, dâng vòng hoa lên bảo tháp, dâng hương thơm, dâng dầu thoa … đi nhiễu quanh bảo tháp theo chiều bên phải). The space before «…» in ch21 mirrors the Pāli's "dadeyya … khādanīyaṃ". No change.
14. Fifty-group uddānas: checked against the kathā names. ch18 ^5-604 Niyāma / saṅgaha / gati / ānisaṃsa / nirodha = «Sự cố định» (ch14) / «sự gộp vào» (ch15 uddāna Saṅgaho) / «cõi tái sinh» (ch16 «sáu cõi tái sinh») / «lợi ích» (ch17 «người thấy lợi ích») / «sự chấm dứt» (ch18). ch23 ^5-742 «Các khuynh hướng tiềm ẩn» (ch19) / «sự thu thúc» (ch20) / «kiếp» (ch21 Kappaṭṭha) / «gốc rễ» (ch22 uddāna Akusalamūlaṃ) / «được xác định riêng biệt» (ch23 uddāna). ch28 ^5-877 «Sự chế ngự» (ch24) / «sự tích lũy phước» (ch25) / «đã sống» (ch26 uddāna aṭṭhāsi) / «với quá khứ» (ch27 uddāna atīte) / «kẻ giết mẹ» (ch28 uddāna). ch31: «Mới» (ch29 uddāna navaṃ), «sự nhập Niết-bàn» (nibbuti, the catchword of ch30 Parinibbānakathā; the Pāli drops pari-, as gati drops cha- in ch18), «cùng một ý định» (ch31 Ekādhippāya). Paṇṇāsakuddānaṃ: «Nhóm năm mươi lớn» (= Mahāpaṇṇāsako close, ch13), «sự cố định», «các khuynh hướng tiềm ẩn», «sự chế ngự» (= the first catchwords of the 2nd-4th fifty-group uddānas), «nhóm nửa năm mươi nhỏ» (= Khuddako aḍḍhapaṇṇāsako close). All consistent; no change. Each vagga uddāna (ch9-31) was compared with its kathā headings / closing lines: where the Pāli catchword equals the kathā name, the wording is the same; the other uddāna members are thesis sentences (different Pāli).
15. Kathā names (heading vs closing line vs uddāna): every heading / closing pair with the same Pāli has the same wording (checked for all 31 chapters); a kathā name repeated in a later chapter keeps its wording (Vimutti ch11 / ch13, Niyāma ch13 / ch14, Nirodha ch10 / ch18, Ñāṇa ch19 / ch28 ×2, Kamma ch20 / ch29, Abyākata ch22 / ch30). Section (d) of the scan: 9 entries have a different Pāli name in the closing line; ch19 Tissopi anusayakathā and ch30 Tissopikathā are false hits (same wording; the scanner expects a «Bàn về …» heading).

## Remaining groups in divergences-rails.md (after the fix)

(a2) 2 groups
- tassuddānaṃ – «Tóm tắt của chương này –» vs «Tóm tắt của nhóm này –» (ch18, ch23, ch28, ch31 after a fifty-group close): left for the user.
- "yajamānānaṃ manussānaṃ … (ch25 ^5-798 segment): kept: context. The reply verse opens with “ at «Bốn bậc đang thực hành …» and closes at «… có quả lớn”»; the Pāli's second opening quote before the repeated line is not doubled (quote-order repair).

(a3) 7 groups
- vuttaṃ bhagavatā – "atthi puggalo attahitāya paṭipanno" (ch1 ^5-229 «đức Thế Tôn», lower case): sample differs (not changed).
- katame pañca / katamāni pañca / katamāni tīṇi / katame tayo: kept: context (the noun counted differs: hiện tượng, loại, năng lực, sự bố thí, lý do, chủ đề, loại mắt, bậc, phạm vi).
- vedanā… saññā… saṅkhārā… viññāṇaṃ hevatthi, heva natthīti (ch9): false hit (closing quote mark only).
- vipākābyākatā kiriyābyākatā rūpaṃ nibbānaṃ … (ch19 «những gì» vs ch21 «điều»; ch22 «điều»): kept: context (ch19 asks of the plural anusayā, ch21 / ch22 of a singular dhammataṇhā / diṭṭhigataṃ).

(a4) 53 groups, all kept:
- false hit (closing quote mark only): appaṇihitārammaṇanti, viññāṇaṃ hevatthi, viññāṇaṃ viññāṇaṭṭhena niyatanti, aparāpariyavedanīyaṃ … niyatanti.
- sample differs (both forms inside ch1, not changed): cakkhundriyañca upalabbhati …, saviññāṇo sandhāvatīti, aviññāṇo sandhāvatīti.
- kept: context (the member is cut out of a longer sentence; the extra or missing words belong to the frame around it, which is different Pāli): paṇidhīti / paṇidhī"ti (the X of «sự mong cầu ấy là để X sinh khởi»; now one frame), vedanā, sārammaṇaṃ / sārammaṇo, atthi tassa āvaṭṭanā («nó» supplied only where the Pāli sentence has no subject; ch18 "so ca sārammaṇo" «và nó …»), nibbānaṃ (ch27 «đó là» opens the list; ch18 a list member; the scanner lower-cases), gandharāgo («đối với» from the case frame), saṅghe (kính trọng … Tăng đoàn vs niềm tin nơi Tăng đoàn), sammappadhānaṃ, sammappadhānā («đối với» frame), the kasiṇa members tejo- / āpo- / vāyo- / nīla- / pīta- / lohita- / odātakasiṇaṃ (elided samāpattiṃ samāpannassa frame), aṭṭhamakassa puggalassa vicikicchānusayo (katvā frame «vì cho rằng»), saṃkilesiyenāti (verb after the list), bojjhaṅgāti (ch13 «… để đi đến sự cố định» frame), catutthaṃ jhānaṃ samāpannassa atthi / natthi vacībhedoti (lokiya vs lokuttara before the …pe…), arahattasacchikiriyāya paṭipannassa …, rūpāvacaraṃ, adoso / amoho / lobho / doso hetu (ch24 ^5-754: predicate of rūpa, «nó là gốc rễ không sân hận …»; ^5-755: subject), saññāvedayitanirodhaṃ samāpannassa … kaṇṭako vutto bhagavatā (ch26 names the Buddha once at the head of the list), dve nibbānānīti, bojjhaṅgā abhāvitāti, sakadāgāmi, anāgāmi, uppannā vedanā, sakadāgāmimaggassa / -phalassa, anāgāmimaggassa / -phalassa, arahattamaggassa jarāmaraṇaṃ arahattamaggoti, paññāti, paro parassa uppannā vedanā (niggaṇhāti «chế ngự» vs paggaṇhāti «nâng»), piṇḍapātassa, atthi lokiyaṃ vīriyaṃ, atthi kiñci sakkāyadiṭṭhiṃ appahāya (arahattappatti vs parinibbāna).
- left for the user: heṭṭhimāya disāya buddho tiṭṭhatīti (ch29 buddho tiṭṭhati «tồn tại»).

(b) 0 groups (the [aṅguttaranikāye] group was settled: «[trong Tăng Chi Bộ Kinh]», the earlier chapter ch3; ch5, ch22 changed).

(c) recurring terms: no clash left. Where a chapter shows more than one candidate, the context differs: saṇṭhāti «đứng vững» (a person stands firm in a fruit, ch2, ch4, ch30) vs «hình thành» (body / aeon forms, ch15, ch21, ch22); āneñjappatta «đạt đến sự bất động» vs āneñja «trạng thái bất động»; dadāti «cho» / «bố thí» / «dâng» by object; buddho «bậc giác ngộ» only in the Bodhiyā buddho thesis (termbase). The «none» counts are false hits (yoniso, saṃkilesiya, paññatta, cetasika as a noun …).

## Left for the user

- "Tassuddānaṃ –" after a fifty-group close «Tóm tắt của nhóm này –» (ch18, ch23, ch28, ch31) vs «Tóm tắt của chương này –» after a vagga close.
- ch29 buddho tiṭṭhati / buddhā tiṭṭhanti «tồn tại».
- kammaṃ karonti «tạo nghiệp» (ch15) vs kammaṃ karoti «làm nghiệp» (termbase has both).
- taṃ jīvaṃ taṃ sarīraṃ: sample differs (sample «linh hồn cũng chính là thân thể»; pi-1 / ch22 / ch31 «Linh hồn và thân thể là một»).
- ch1 ^5-229 «đức Thế Tôn» (lower case, inside the sample).
- ch15 ^5-501 «đối với từng người như vậy» for a result (see clash 6).
- uppajjati: the termbase's bare entry «sinh khởi» vs its phrase entries «xuất hiện» for Buddhas (now ch3, ch16, ch21 all «xuất hiện»), for the termbase alignment.

## Checks

After the fix, for all 32 files (preamble + 31 chapters): check_chapter_ids.py OK, dashcheck.py 0 dash-line mismatches and 0 extra dashes, verify_rails_vi.py OK. The script asserts every count, NFC, LF, and that «các các», «là là», «được được», «….», «.…», «:-», «chánh niệm» did not increase. consistency_find_vi.py re-run: (a1) 0, (a2) 2, (a3) 7, (a4) 53, (b) 0, (e) 0; all explained above.
