# pi-6 Vietnamese rails: review fixes, stage 2, answer heads H1-H4 (2026-11-23)

Brief: ../vi-review-fixes-stage2-brief.md. Findings: ../review/review-findings.md A5, A6 (heads).
Script: review_fixes_heads_vi.py (`apply` / `dry` / `trans` / `diff` / `show`; builds from backup-pre-heads/, re-runnable).
Log: review-fixes-log-heads.tsv (2121 rows: file, block id, old head, new head, rules). Backups: backup-pre-heads/ (43 chapters, copied once).
A head = the text of a non-question sentence before «, thì », or a cut-answer chunk opening with «Ở / ở / Vào» before «…».
The script asserts that nothing outside the heads changes, that identical Pāli lines keep one Vietnamese line (0 → 0)
and identical Pāli heads one Vietnamese head (no new split), plus residue checks for every rule.

## Heads changed (a head can carry several rules)

| chapter | heads | H1 | H2 | H3 | H4 |
|---|---|---|---|---|---|
| 2-01 | 1 | 0 | 0 | 1 | 0 |
| 2-02 | 2 | 0 | 0 | 0 | 2 |
| 3-01 | 65 | 0 | 61 | 4 | 0 |
| 3-02 | 49 | 0 | 47 | 2 | 0 |
| 3-03 | 101 | 0 | 82 | 3 | 16 |
| 3-04 | 111 | 0 | 97 | 2 | 12 |
| 3-05 | 105 | 0 | 92 | 1 | 12 |
| 3-06 | 79 | 0 | 58 | 0 | 21 |
| 4 | 14 | 0 | 14 | 0 | 0 |
| 5-01 | 97 | 97 | 0 | 0 | 0 |
| 5-02 | 120 | 120 | 0 | 0 | 0 |
| 5-03 | 40 | 40 | 0 | 0 | 0 |
| 6-01 | 45 | 41 | 0 | 0 | 4 |
| 6-02 | 97 | 97 | 0 | 0 | 8 |
| 8 | 8 | 8 | 0 | 0 | 0 |
| 9-01 | 57 | 57 | 0 | 0 | 0 |
| 9-02 | 88 | 88 | 0 | 0 | 0 |
| 9-03 | 32 | 32 | 0 | 0 | 0 |
| 10-02 | 131 | 34 | 131 | 0 | 0 |
| 10-03 | 266 | 72 | 246 | 0 | 0 |
| 10-04 | 135 | 38 | 115 | 0 | 0 |
| 10-05 | 12 | 2 | 0 | 10 | 0 |
| 10-08 | 136 | 65 | 83 | 6 | 0 |
| 10-09 | 163 | 55 | 101 | 0 | 27 |
| 10-10 | 80 | 21 | 14 | 0 | 45 |
| 10-11 | 82 | 28 | 15 | 0 | 39 |
| 10-12 | 5 | 0 | 0 | 5 | 0 |
| total | 2121 | 895 | 1156 | 34 | 186 |

Unchanged: preamble, 1, 7-01 … 7-11, 10-01, 10-06, 10-07, 10-13.

## H1: head types and decisions (pieces split at «, »; a piece = persons / place / «trong đời sống» / moment)

New case, «và» added:
1. persons dying / being reborn + «trong đời sống» (also the ye tail «khi những người ấy đang …» and two-plane groups):
   «Ở tất cả những người đang chết đi, và trong đời sống, vào khoảnh khắc tan rã của tâm» (commentary ^6-89
   "cutipaṭisandhīsupi pavattepi"; ^6-90 "tasmiṃ upapattikkhaṇe taṇhāvippayuttacittuppattikkhaṇe cā").
2. after a moment: persons, place, «trong đời sống» or another moment: «Vào khoảnh khắc tan rã của tâm, và ở những người
   đang nhập thành tựu thiền chấm dứt và chúng sinh Vô Tưởng»; «Ở tất cả chúng sinh, vào khoảnh khắc tan rã của tâm, và vào
   khoảnh khắc sinh khởi của tâm không gắn liền với niềm tin»; «…, vào khoảnh khắc tan rã của khao khát, và khi tâm … đang diễn ra».
3. the anantarā moment («… của tâm mà ngay sau đó …», yassa cittassa anantarā … tassa cittassa …) always opens a case, even
   after persons (it brings its own persons; arahants cannot be those who will attain): «…, và ở các bậc A-la-hán, và vào
   khoảnh khắc tan rã của tâm mà ngay sau đó sẽ đạt được con đường tối thượng».
4. a place with its own moment after persons: «…, và ở những người đang chết đi khỏi cõi Vô Tưởng, và ở cõi không hình sắc,
   vào khoảnh khắc sinh khởi của con đường …».

One case, no «và»: persons + their moment («Ở những người khác, vào khoảnh khắc …»); place [+ «trong đời sống»] + moment;
«trong đời sống» + moment; place lists sharing a moment («Ở cõi hình sắc, ở cõi không hình sắc, vào khoảnh khắc tan rã của tâm
cuối cùng, …»); person + place lists with no moment (7-0x «Ở bậc A-la-hán, ở cảm giác khó chịu, ở cõi hình sắc …», 6-01 «Ở cõi
dục lạc, ở những người có được tâm cuối cùng»); runs of plain person groups; groups already opened by «và ở».

## H2 (1156 heads)
«những người[ khác| thuộc kiếp sống cuối cùng] đang <V>[ vào / khỏi cõi X][ sex word] mà <attributes>», attributes (eye, ear,
nose, mind, matter, roots, ñāṇa, feeling) in the Pāli order, read from the Pāli line (e.g. "Somanassena ñāṇasampayuttānaṃ"
«mà có niềm vui đi kèm, gắn liền với hiểu biết» vs "Ñāṇasampayuttānaṃ somanassena" «mà gắn liền với hiểu biết, có niềm vui đi
kèm»; before, both read alike). Each Vietnamese group is paired with its Pāli participle and the attribute sets are asserted.
Added (55 heads): a run item after a «mà …» group joins with «, và» («… mà không có mắt, và chúng sinh Vô Tưởng»), the
consistency pass's fallback, so the next group is not read as one more thing the persons lack.
Not moved: abhisametāvīnaṃ / anabhisametāvīnaṃ «những người đã / chưa thấu hiểu» (termbase person nouns; moving them raised
termbase misses by 16).

## H3 (34)
«chúng sinh trong cõi Tịnh Cư và chúng sinh Vô Tưởng» (14), «…, chúng sinh Vô Tưởng và chúng sinh trong cõi không hình sắc» (16),
«chúng sinh trong cõi gồm năm khối và chúng sinh Vô Tưởng» (4).

## H4 (186)
cavantānaṃ: «những người[ nam| nữ] đang chết đi mà [có mắt, ]sau khi tái sinh … sẽ nhập Niết-bàn trọn vẹn».
upapajjantānaṃ / tāsaṃ upapajjantīnaṃ: «những người … đang tái sinh mà sau khi tái sinh vào cõi X sẽ nhập …». The brief's
«đang tái sinh vào cõi X mà sau đó …» was not used: the ye plane is a later rebirth, not the current one (the English rails
^6-3-87 "those being reborn now who will be reborn in the formless sphere"; the P group pacchimabhavikā is separate).
eteneva / katici: «những người nam đang chết đi mà trong chính trạng thái ấy, sau khi trải qua một số kiếp sống, sẽ …».
Two ye clauses with one tail (10-09, 10-10, 10-11): the participle goes into both. Standalone (3-06 ^6-3-211, ^6-3-220): «Những người đang chết
đi mà sau khi tái sinh vào cõi hình sắc sẽ nhập Niết-bàn trọn vẹn, thì …».

## Not decided (left as they were, for the user)
- ye maggaṃ (na) paṭilabhissanti tails («những người phàm phu nào sẽ không đạt được con đường, khi những người ấy đang tái
  sinh, và trong đời sống, …»; ^6-5-68, 71, 73, 76, 116, 119, 121, 124, 154, 157, 159, 162): outside H4 (no
  parinibbāyissanti); only H1 applied. Where āpāyikānaṃ stands right before the ye group (^6-5-71, 76, 119, 124, 157, 162)
  the tail may read as covering «chúng sinh trong cõi khổ» too; the Pāli is open.
- a run of groups followed by a moment that may belong only to its last group (6-01 / 6-02 ^6-6-67, ^6-6-116, ^6-6-156).

## Stale builders (not edited, chapters not rebuilt)
The head pieces in build_rails_3-01 (AY_ATTRS / ATTR_JOIN), 3-02 … 3-06, 10-02 (SEX / FEEL), 10-03, 10-05 (ye_clause12),
10-08 … 10-11, 2-02 (ye tail), 5-01 / 9-01 / 8 (answer_head joins) still give the old heads.

## Checks (44 files)
check_chapter_ids 44 OK; dashcheck 0 mismatches; verify_rails_vi 44 OK; no «—», «:-», «….», «được được», «là là», «chánh
niệm», «vẫn đã», double spaces, CR; NFC. consistency_find_vi.py groups before / after: L0 S0 M2 H2 B2 P0 C0 Q5 V0 N0 (unchanged).
termbase_adherence_vi.py: 27 353 occurrences, misses 260 → 249 (asaññasattānaṃ 9 → 0, arūpānaṃ 3 → 1; no other change).
