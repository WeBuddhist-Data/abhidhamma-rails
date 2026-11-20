# pi-2 Vietnamese rails: review fixes (findings r1-r7, user decisions 2026-11-20)

Script: `review_fixes_vi.py` (rerunnable; reads `backup-pre-review/`, writes the 19 chapter files; `--dry` writes
nothing). Every rule declares its exact replacement count and the run aborts on any difference. Log:
`review-fixes-log.tsv`. Helpers: `review_fixes_lib.py`, `review_fixes_probe.py`, `review_fixes_probe2.py`,
`review_fixes_scan.py` (subset-adjacent subjectless sentences: 0 left), `review_fixes_find_builders.py`,
`review_fixes_adh_diff.py`. The copyrighted reference translation was not opened.

Result: 254 lines changed in 17 files (ch7 2 … ch16 54), 0 new identical-Pāli divergences (3 before, 3 after).

## Decisions and how they were applied
1. Scope pattern, one form book-wide: «Cả <N> <X> đều …» (also «Cả <N> <X> đều đôi khi …»; after «Không nên nói»:
   «Về cả <N> <X> thì không nên nói …»); «;» before a restated clause becomes «.». Applied to every subjectless
   predicate that directly followed a subset sentence (56 places: ch1 ^2-152/153, ch2 ^2-170/171, ch3 ^2-187/188,
   ch4 ^2-218, ch5 ^2-223/224, ch9 ^2-465, ch10 ^2-484/485, ch11 ^2-506/507, ch12 ^2-640/641, ch13 ^2-701/702,
   ch15 ^2-749/750). Subjectless predicates after whole-set sentences are unchanged (decision 12).
   ^2-749: «ba / hai loại hiểu biết thông suốt còn lại» (4).
2. ^2-809 atthato: unchanged.
3. ^2-803: «người đang có các hiện tượng ấy»; other source slips unchanged.
4. ch16: dhamme ñāṇaṃ «sự hiểu biết về chân lý», «Bằng chân lý này» (5); ñāṇavatthu «các loại hiểu biết theo nhóm N»,
   «bảy mươi bảy loại hiểu biết» (32; no «bốn mươi bốn» in pi-2; none in ch6/ch17). ^2-724 «Giáo Pháp» kept.
5. kamyatā: «sự mong muốn không thấy / nhìn / đến gần / hội họp với …», «sự mong muốn không nghe / lắng nghe / học hỏi /
   ghi nhớ …», matrix ^2-834, headings ^2-17-4-51-0, ^2-17-4-52-0; ^2-862 «sự mong muốn nịnh bợ». ^2-513
   cāṭukamyatāya (instrumental «bằng lời nịnh bợ») left: not named in the decision.
6. ^2-830 bhonto: «Quả thật, những chúng sinh đáng kính này …», «Hoặc những chúng sinh đáng kính này …».
7. ^2-511: «… cho việc đạt được các hiện tượng thiện».
8. pi-1 verbatim (built from the pi-1 file at run time): ^2-182 (= ^1-1287, variant bracket kept), ^2-517 (^1-1352,
   ^1-1354), ^2-518 (^1-1353, ^1-1355), ^2-905 (^1-1352, ^1-1353), ^2-U24 (^1-1352 body, own question
   «sự không thu thúc»). Pāli quote marks added. ^2-518: the pi-2 Pāli quotes the whole reflection, so the quote opens
   at «Không phải …» and pi-1 «, với ý nghĩ “Như vậy, ta sẽ …”» became «; như vậy, ta sẽ …» (only change of wording).
9. maccu maraṇaṃ: «sự tử vong, sự qua đời» (^2-193, ^2-236; pi-1 has no maraṇa definition).
10. Quotes added after «đó được gọi là» at ^2-259, 273, 279, 281, 283, 327, 354, 368, 376.
11. ^2-11 … ^2-31: «của người không ở trong / đang ở trong thành tựu thiền» (48).

## Other findings applied
r2: ^2-176 «gió như bứt tim», «gió mây đen»; ^2-190/199 «gặp gỡ những gì mình không yêu quý» (3); ^2-218 «phần bên
trong»; ^2-223 «nhưng không có đối tượng …». r3: samāgamo «sự hội tụ» (^2-242, 249, 273, 305, 354; also ^2-199, ^2-200
asamāgamo, decision 14). r4: ^2-640 «còn» dropped; ^2-701 new sentence «Đều không thuộc về …»; adhimuccitvā «sau khi
trải rộng trọn vẹn» (8); ^2-510; ^2-537 «môi trên»; ^2-508 «; chỗ ở ấy ít tiếng động»; ^2-467 «tâm trở nên an định»,
«tâm đã an định như vậy»; «Và» at ^2-643/653/663/673; ^2-516 «tất cả về mọi mặt»; ^2-619. r5: A2, A4, A5, A9 (keep-as-
written form «thì, xét theo đó, chính chúng là điều (không) thể xảy ra tương ứng»), A10 (pi-1 has no such string:
«gần gũi, kết giao, thân cận», 14), A11 (29), A12 (21), A13 (6), A14, A15, A16 (2), A17 (34, ch14 + ch17), A19.
r6: ^2-844, 854, 855, 904, U41, 939, 947/U67/U68, 949 (+ ^2-816 same Pāli), 976, 884, 901, 921 (3), 948 (one form:
the termbase phrase «quan điểm … khởi lên»), 953, 973-976 «Ước gì tôi» (72), U58, U9 (direction per aṭṭhakathā 925
for all three pairs). r7: ^2-1022, 1031, 1023 (2 verse lines), heading ^2-18-9-0, ^2-1009/1010/1012 (12).

## Optional items
Skipped: r2 ^2-203/204 noun subject; r3 ^2-236 ablative re-ordering (adds «đời»); r4 ^2-564 «là dục» (splits the
kāma term inside one definition); r5 A18 apubbaṃ acarimaṃ (adds words), A20 (no wording given). Not applied per
decision 12: listed there.

## Termbase (AI_translation/vietnamese/pi-2-pali-vietnamese-termbase-plain.md) now overridden
Decision 4: ñāṇavatthu «chỗ dựa của sự hiểu biết» -> «loại hiểu biết»; vatthu (ñāṇavatthu sense) «chỗ dựa»; dhamme
(sense in dhamme ñāṇaṃ) «hiện tượng» -> «chân lý». Decision 5: adaṭṭhukamyatā, asamāgantukamyatā, asotukamyatā,
asavanakamyatā, anuggahetukamyatā, adhāretukamyatā («sự không muốn …» -> «sự mong muốn không …»), cāṭukamyatā
«lời nịnh bợ» -> «sự mong muốn nịnh bợ». Decision 6: no bhonto headword (vata «quả thật» unchanged). Others changed by
findings: samāpannassa / Asamāpannassa (decision 11), adhimuccitvā / pharitvā adhimuccitvā, paññatti / dhammānaṃ
paññatti, abhilāpe, samāgamo / asamāgamo, yoga (yogavihita sense «trí tuệ»), sasaṅkhāra(niggayhavāritagato),
visuddhiyā (^2-805), chambhitattaṃ (fear list only), sampavaṅkatā (^2-901), jeṭṭhe / bhātari, bhogaṃ / vaṇṇaṃ,
amanāpo (^2-U58), atthajāpikā / jāpitatthā paññā, payirupāsati / bhajati family, sekkho / asekkho (^2-510),
uppalaka, kāḷa, mukha / nimitte, samāhitaṃ (^2-467), ajjhattaṃ (^2-218), upādāya (^2-809), samāpattiyā (^2-511).
Adherence: 288 misses before, 478 after (+190, all on the headwords above; ^2-517/905/U24 «akusalā dhammā» and
^2-182 «rūpā» from the pi-1 copies; ^2-948 uppajjati/diṭṭhi uppajjati conflict: one miss either way).

## Builder constants that would need the same change (builders NOT rerun)
- build_rails_1_vi.py: 570 («Đều có điều kiện, đều do …», ^2-153), 679 («; chúng là những khối mà»).
- build_rails_2_3_vi.py: 341, 344 (vāta list), 477 (kāmadhātu definition, pi-1 wording), 386/389/392 (gehasita strings,
  check whether shared with ch17).
- build_rails_4_5_vi.py: 95 (appiyehi sampayogo), 129/134 (samāgamo / asamāgamo), 648-649 (^2-223 «nhưng không»);
  the maraṇa string, ^2-218 and the ch2-ch5 question-section scope sentences are assembled, not literal.
- build_rails_6_vi.py: 169 (samāgamo); quotes of D10 are built per line.
- build_rails_10_12_vi.py: 191 (^2-467), 877 (sevati …), 917/1088 (appasadda), 938 (^2-510), 943 (^2-511), 989
  (sabbena sabbaṃ), 1099 (mukhanimitta), 1271/1273 and 1009 (indriyesu aguttadvāratā / bhojane: replace with the pi-1
  strings); ^2-640/641 scope and «còn» assembled in the ch12 question section.
- build_rails_13_15_vi.py: 134/141/217/243/921 (adhimuccitvā), 350 (surāmeraya), 511/515 (abhilāpa), 518 (paññatti),
  769 (^2-750 «đều là những loại …»); ch13 / ch15 question-section scope sentences and A2 «còn lại».
- build_rails_16_vi.py: 215 (yāthāvakavatthu), 371 (atthajāpikā), 409/884/890 (dhamme ñāṇaṃ), 453 and the
  ñāṇavatthu heading/closing generator, 797-801 (yogavihita), 954-956 (sevanti), 1122 (upādāya), 1229/1263
  (bhavarāga), 1334/1335 (bhonto); ^2-803/804/805/828/829 assembled.
- build_rails_17_vi.py: 195/1108 (sampavaṅkatā: only the ^2-901 use changes), 278, 372, 388/391/394, 421/422
  (pi-1 copies), 434/435/1087/1092 (kamyatā), 696, 698, 718, 778, 1002, 1042, 1102/1103/1139-1141 (vipariyāsa),
  1210, 1392, 1508-1522 (apāhaṃ); ^2-904, ^2-939, ^2-948, ^2-976 assembled.
- build_rails_18_vi.py: 519 (heading), 719/721 (rebirth lists), 978/1000 (^2-1022), 1009/1010 (^2-1023), 1080 (^2-1031).
