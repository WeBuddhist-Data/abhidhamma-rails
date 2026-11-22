# pi-6 Vietnamese rails: review fixes, stage 1, part r5 (10-03 … 10-13), 2026-11-22

Brief: ../vi-review-fixes-brief.md. Findings: ../review/review-findings.md (A3, A4).
Script: review_fixes_r5_vi.py (builds from backup-pre-review/<ch>, asserted counts per chapter, re-runnable).
Log: review-fixes-log-r5.tsv (500 rows: file, block id, old, new, rule).
Backups: backup-pre-review/10-03 … 10-13-indriyayamaka.md (copied once).

## Applied

| chapter | F3 lines | F4 lines (present / past / future) |
|---|---|---|
| 10-03 | 15 | 69 (69 / 0 / 0) |
| 10-04 | 0 | 0 |
| 10-05 | 0 | 70 (0 / 34 / 36) |
| 10-06 | 0 | 52 (0 / 0 / 52) |
| 10-07 | 0 | 0 |
| 10-08 | 7 | 70 (54 / 16 / 0) |
| 10-09 | 5 | 122 (61 / 0 / 61) |
| 10-10 | 5 | 0 |
| 10-11 | 0 | 0 |
| 10-12 | 0 | 85 (0 / 23 / 62) |
| 10-13 | 0 | 0 |
| total | 32 | 468 |

- F3: «những người nhập thành tựu thiền chấm dứt» → «những người đang nhập thành tựu thiền chấm dứt» (32 = the Pāli's
  32 nirodhasamāpannānaṃ; all in answer heads; none in notes).
- F4: after "no ca" with a positive uppajj- verb, «nhưng ở <pron>[, ở nơi ấy] không có X [đã |sẽ ]sinh khởi» →
  «… X không sinh khởi / X chưa từng sinh khởi / X sẽ không sinh khởi». Counts per tense equal the Pāli's "no ca"
  clauses with a positive verb, per chapter (asserted). X is always «năng lực …».
- Not present in this part: "no ca" + nirujjhati (the Indriya pavatti has the uppāda frames only), participle forms,
  the "neither" form after "no ca" + uppajjati. 10-13 "no ca" + parijānāti / bhāveti / sacchikaroti / pajahati: untouched
  (outside F4). Denied negatives («vẫn sinh khởi», «đã từng sinh khởi», «vẫn sẽ sinh khởi»): untouched.
- F1, F2, F5 … F9: no occurrence in this part (no ekasadisaṃ note, no Atikkantakāla, no heṭṭhā in the Pāli of 10-03 … 10-13).

## Stale builder constants (builders not edited, chapters not rebuilt)

- build_rails_2-01_vi.py `noca_vi` (≈ l. 341-343: positive verb → f"{C.NEITHER_FIRST} {b} {v[2]}", i.e. «không có B V»),
  its docstrings (b_noca ≈ l. 583) and the formula-table rows (≈ l. 781-782); used by the Indriya builders 10-03, 10-05,
  10-06, 10-08, 10-09, 10-12 through B.b_noca (via build_rails_10-02 / 10-03 setters). A rebuild would restore
  «không có X [đã |sẽ ]sinh khởi».
- build_rails_10-03_vi.py l. 329 ("nirodhasamāpannānaṃ", "người nhập thành tựu thiền chấm dứt") and the assert at
  l. 339 on DY.EXTRA_PERSON["nirodhasamāpannānaṃ"] (the setter module's EXTRA_PERSON holds the same old form).
- Termbase entry nirodhasamāpannānaṃ: still the old form (to the termbase alignment step, per the findings).

## Checks (all 11 chapters)

check_chapter_ids OK; dashcheck 0 mismatches; verify_rails_vi OK; no «—», «:-», «….», «được được», «là là»,
«chánh niệm», «vẫn đã», double spaces, CR; NFC; 0 residue of «nhập thành tựu thiền chấm dứt» without «đang» and of
«không có … [đã |sẽ |đang ]sinh khởi / chấm dứt» anywhere in the part; identical-Pāli line keys with two Vietnamese
forms: 0 before, 0 after.
