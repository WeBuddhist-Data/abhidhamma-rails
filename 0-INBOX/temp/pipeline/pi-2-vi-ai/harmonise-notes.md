# pi-2 Vietnamese zero-shot: harmonise pass notes (2026-11-18)

Scripts: vi_common.py, find_divergences_vi.py (divergences-pre.md = backup scan, divergences.md = after), harmonise_vi.py (log: harmonise-log.tsv; backup: backup-pre-harmonise/), check_strings_vi.py (decision 2), count_items_vi.py, probe_bojjh_vi.py, probe_namarupa_vi.py, probe_harm_vi.py, final_checks_vi.py. The builders were NOT rerun.

## Divergence scan before the pass
(a) inside pi-2: 3 segment / 3 line / 2 clause / 3 item groups, all deliberate (see "Kept"). (b) against pi-1: 2 segment groups (##### Tikaṃ / Dukaṃ), 4 clause groups («Ở đây, phần vật chất là gì?» ^1-1317; «… ba gốc rễ thiện / bất thiện / không xác định về mặt đạo đức là những gì?» ^1-1060 …). (c) recurring terms: uniform except the points decided below.

## Rules applied (harmonise_vi.py)
| rule | what | count |
|---|---|---|
| D1-171-negation | ^2-171 (ch2) «kilesasampayuttā ceva no ca na kilesā» now literal: «gắn liền với phiền não nhưng không phải là không phải là phiền não» | ch2 1 |
| D1-question-dot | «?» -> «.» where the Pāli closes the question with «.»: ^2-1014 (cattāro āhārā … pātubhavanti.), ^2-1023 verse (kittako.), and ^2-957 (Ja) «… byāvaṭā.» (same class, added under the rule) | ch17 1, ch18 2 |
| D5-vatthu | āghātavatthu / virodhavatthu «căn cứ của …» -> «chỗ dựa của …» | ch3 1, ch17 12 |
| D7-rajata | ^2-173 rajataṃ «bạc» -> «đồng tiền» | ch3 1 |
| D10-namarupa | ch6 nāmarūpa members: «phần vật chất» (4 strings × 21 lines) | ch6 84 |
| D10-nhung-gi | counted plural questions «Tattha katame <number> …?» -> «… là những gì?» | ch10 2, ch16 3, ch17 89, ch18 55 |

182 lines changed (ch2 1, ch3 2, ch6 21, ch10 2, ch16 3, ch17 96, ch18 57). Protected lines untouched (0 blocked).

## Decisions
1. As written: ^2-171 literal double negation; ^2-1014 / ^2-1023 / ^2-957 «.» restored. ^2-809 «atthato» read as attato («là tự ngã») left for the user. ^2-919 (Ga) «brahmacariyesanā,» (comma where «?» is expected) still rendered with «?»: left for the user.
2. Faculty strings: all 143 vīriya / sati / samādhi / paññā strings match their own Pāli line item for item (check_strings_vi.py; reverse count check 0). No added or missing item (the Russian ^2-220 error is not in the Vietnamese). Only spelling slips rendered as meant (^2-459 maggariyāpannaṃ, ^2-524 asammusanatā, ^2-525 bhūrīmedhā).
3. Catukkaṃ / Pañcakaṃ: kept both. ch12 closes the jhāna series counted as four or as five jhānas (the fourfold / fivefold jhāna method) = «Phương pháp chia bốn / năm»; ch16, ch17 and pi-1 rūpakaṇḍa close a section of classifications by fours / fives = «Phân loại theo nhóm bốn / năm».
4. kāmadhātu: kept both: «yếu tố dục lạc» (element beside byāpāda-/vihiṃsādhātu: ch3, ch17 ^2-912) and «cõi dục lạc» (plane: ch18; ch17 kāmadhātupaṭisaṃyutto rāgo ^2-916/917). ch3 ^2-182 defines the element also by the realm; the heading term keeps «yếu tố».
5. vatthu: pi-1 has no āghātavatthu; its vatthu compounds are the physical base and kilesavatthu, both «chỗ dựa». Same compound type (vatthu = ground of X) -> «chỗ dựa của sự oán giận», «chỗ dựa của sự chống đối» (now beside «chỗ dựa của phiền não / của sự lười biếng» in the same ch17 lists). Kept: dasavatthukā diṭṭhi «có mười chủ đề» (topics of the view), Khuddakavatthu «chủ đề nhỏ» (approved title), aññataraññatarena vatthunā «điều này hay điều khác».
6. dhamme ñāṇaṃ: kept both («về Giáo Pháp» ch16 catukka; «về các hiện tượng» in the paṭisambhidā formula ch15/16). ^2-724 «dhammaṃ jānāti» = «biết Giáo Pháp» kept: Vibhaṅga aṭṭhakathā (Pabhedavāra, pi-vibhanga-atthakatha ^2-1491) says the pariyattivāra shows «pariyattisaṅkhātassa … bhāsitassa dhammabhāvaṃ», i.e. dhamma there is the Teaching as text (sutta, geyya …).
7. sajjha / rajata: aṭṭhakathā (pi-vibhanga-atthakatha ^2-217): «Sajjhūti rajataṃ … Rajatanti kahāpaṇo». sajjhaṃ stays «bạc»; rajataṃ in this list = «đồng tiền». pi-1 has no such list; its jātarūparajata «vàng bạc» (^1-616 …) = ch2 ^2-162, unchanged.
8. kāmesumicchācāra: already one wording «hành vi sai trái trong các dục lạc» (ch4, 11, 14, 17). Realm names already uniform and equal to pi-1 (Sắc Cứu Cánh, cõi Phạm Thiên, Tha Hóa Tự Tại, địa ngục Vô Gián). pi-2 names that pi-1 lacks: Tứ Đại Thiên Vương, Ba Mươi Ba, Dạ Ma, Đâu Suất, Hóa Lạc, Phạm Chúng, Phạm Phụ, Đại Phạm, Thiểu Quang, Vô Lượng Quang, Quang Âm, Thiểu Tịnh, Vô Lượng Tịnh, Biến Tịnh, Quảng Quả, Vô Tưởng, Vô Phiền, Vô Nhiệt, Thiện Hiện, Thiện Kiến; also a-tu-la, ngạ quỷ, loài súc sinh.
9. Awakening-factor names as question topic or subject: only in ch10, already uniform: 22 topics «Ở đây, “chi phần giác ngộ là …” là gì?» and 10 Pañhāpucchaka subjects «“Chi phần giác ngộ là …” thì …», all quoted; 0 unquoted. No change.
10. pi-1 wins for identical Pāli: (a) ch6 nāmarūpa members as pi-1 ^1-1316/^1-1317: «Có phần tinh thần, có phần vật chất», «Ở đây, phần vật chất là gì?», «đó được gọi là “phần vật chất”», «và đây là phần vật chất»; the compound keeps pi-1 ^1-1343 «phần tinh thần và vật chất». (b) «Tattha katame tayo kusalahetū?» etc.: pi-1 «… là những gì?»; all nine pi-1 questions that name a number use it, so the frame was applied to all 149 counted pi-2 questions (ch10, 16, 17, 18) to keep one form; drop rule D10-nhung-gi to limit it to the three identical clauses.

## Kept on purpose (remaining (a)/(b) groups)
- viharati lemma «“Sống”» (ch12 ^2-512, 540, 544, 548, 554: conduct / hindrance passages) vs «“An trú”» (jhāna and appamaññā passages): notes-10-12 context split.
- «Tattha katamaṃ saṅkhārapaccayā viññāṇaṃ?» ^2-227 «các sự tạo tác» (Suttanta chain, plural saṅkhārā) vs Abhidhamma «sự tạo tác» (singular): notes-6.
- «Tattha katamaṃ sukhaṃ?» ^2-594 «sự dễ chịu» (defined as kāyikaṃ sukhaṃ, pi-1 formula «nhờ dứt bỏ sự dễ chịu») vs ^2-567 / ^2-589 «hạnh phúc» (cetasikaṃ sukhaṃ): the definitions differ.
- ##### Tikaṃ / Dukaṃ «Bộ ba / Bộ đôi» (Pañhāpucchaka on the matrix triads / dyads, terms file §3) vs pi-1 3-01 «Phân loại theo nhóm ba / hai» (rūpa classification by threes / twos): different units.
- (b4) item groups (9:2-434 …, 13:2-702) are alignment noise of the item splitter (pi-1 items shifted), not real divergences.

## Builder constants that would need the same change (if a chapter is ever rebuilt)
- build_2-3_vi.py: SLIP_ALIAS «kilesasampayuttā ceva no ca na kilesā» -> kilesa_samp_notN (literal double negation); "pathavi_ext" list «san hô, bạc, vàng» -> «đồng tiền»; line ~668 «mười căn cứ của sự oán giận».
- build_17_vi.py: N["āghātavatthu"], N["virodhavatthu"] («chỗ dựa của …»); the (Ja) purisadosa sentence (~line 1717) «như vậy. Bây giờ»; q() (~line 43) and the hard-coded h("Tattha katame …") questions for counted groups (« là những gì?»).
- build_18_vi.py: the ^2-1014 āhāra question («… chúng sinh.»; SLIPS note at ~515), h("Sabbesaṃ ekasaṅkhāto") «là bao nhiêu.», the counted questions (khandha / āyatana / dhātu / sacca / indriya / hetu / āhāra / phassa / vedanā … per plane).
- build_16_vi.py, build_10-12_vi.py: question builders for the counted questions (ch16 ^2-800 …, ch10 satta bojjhaṅgā).
- build_6_vi.py: N["rūpaṃ"] in the nāmarūpa member strings («phần vật chất»; the compound nāmarūpa unchanged).

## Checks after the pass
check_chapter_ids OK (19/19); dashcheck 0 mismatches, 0 extra (19/19); verify_rails_vi OK (19/19); preamble and the first 77 non-empty lines of 1-khandhavibhango identical to the backup (and to ch1-sample.md); no «—», «:-», «chánh niệm», «seed», «….», Latin letters outside brackets, CR, double blank lines; all NFC (final_checks_vi.py).
