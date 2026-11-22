# pi-6 Vietnamese rails: review fixes, stage 1, part r1 (2026-11-22)

Brief: 0-INBOX/temp/pipeline/pi-6-vi-ai/vi-review-fixes-brief.md. Part r1: preamble.md, 1-mulayamaka.md, 2-01, 2-02,
3-01 … 3-05. Script: review_fixes_r1_vi.py (builds from backup-pre-review/, re-runnable, asserted counts). Log:
review-fixes-log-r1.tsv (file, block id, old, new, rule). Backups (made once): backup-pre-review/<chapter>.

## Changes (345 lines)

| chapter | F2 | F3 | F4 | F7 | F8 |
|---|---|---|---|---|---|
| preamble | 0 | 0 | 0 | 0 | 0 |
| 1-mulayamaka | 0 | 0 | 0 | 2 | 0 |
| 2-01 | 0 | 0 | 50 | 0 | 0 |
| 2-02 | 0 | 0 | 48 | 0 | 0 |
| 3-01 | 1 | 0 | 38 | 0 | 0 |
| 3-02 | 0 | 0 | 39 | 0 | 0 |
| 3-03 | 0 | 0 | 70 | 0 | 0 |
| 3-04 | 0 | 0 | 43 | 0 | 1 |
| 3-05 | 0 | 0 | 53 | 0 | 0 |

- F2 ^6-3-23: «thì ở nơi ấy lĩnh vực ý và lĩnh vực đối tượng của ý giống hệt nhau, không có khác biệt, …» →
  «thì các câu hỏi về lĩnh vực ý và về lĩnh vực đối tượng của ý được trình bày giống hệt nhau, không có gì khác, …»
  (the brief's wording; «ở nơi ấy» for tattha is absorbed into «các câu hỏi»; rest and variants unchanged). The
  ekasadisaṃ note occurs only here in part r1 (^6-3-26 "yassakasadisaṃ" is a different note).
- F3: 0 in part r1 (no nirodhasamāpann- in these Pāli chapters; asserted).
- F4: 341 replacements in 341 lines (one per line), each matched to one Pāli "no ca … uppajj- / nirujjh-" with a
  positive verb on the same line (cross-checked line by line, 341 = 341). By tense: «không sinh khởi» 87, «chưa từng
  sinh khởi» 39, «sẽ không sinh khởi» 74, «không chấm dứt» 54, «chưa từng chấm dứt» 27, «sẽ không chấm dứt» 63.
  No "neither" form, no participle form in this part. 0 «không có <member> (đã |sẽ |đang )?(sinh khởi|chấm dứt)» left.
- F7 ^6-1-49, ^6-1-99 first lines: «… sự phát sinh thiện…» / «… sự phát sinh thuộc phần tinh thần…» → «… … không.»
  (the Pāli ends "…pe…." / "….": closed with «không», full stop kept, no «?»).
- F8 ^6-3-148 line 5: «…lĩnh vực ý vẫn sẽ chấm dứt, ở những người đang nhập Niết-bàn trọn vẹn …» → «… vẫn sẽ chấm dứt.
  Ở những người đang nhập Niết-bàn trọn vẹn …». Only instance of this Pāli comma in the part.

## Stale builder constants (not rebuilt; a rebuild would undo the fixes)

- build_rails_7-01_vi.py: NEITHER_FIRST «không có» used for "no ca <pron> B <positive verb>" (l. 159, 279).
- build_rails_2-01_vi.py: noca_vi (l. 340-343, positive branch «không có B V»), b_noca docstring (l. 583), the
  notes row (l. 781-782). Every pavatti builder of the part (2-02, 3-01 … 3-05) imports these.
- build_rails_3-01_vi.py l. 196: the ^6-3-23 note «… giống hệt nhau, không có khác biệt, …».
- build_rails_3-04_vi.py comma_join (l. 16, 148, 462): keeps the Pāli comma «…, ở …» at ^6-3-148.
- build_rails_sample_vi.py l. 373-375 and 385-388: series_run(…) ends the two cut questions with «…» without «không».

## Checks (all 9 files)

check_chapter_ids OK; dashcheck 0 mismatches; verify_rails_vi OK; no «—», «:-», «….», «được được», «là là»,
«chánh niệm», «vẫn đã», «seed», double spaces, CR; NFC; 0 remaining replaced strings; identical Pāli lines give
identical Vietnamese (asserted per line).
