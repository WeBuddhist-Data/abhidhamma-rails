# Builders are stale (pi-2 Russian plain rails), 2026-11-17

The approved review fixes (findings-r1 … r6, plus the user decisions dhammacchando «благое желание как явление» and brahmacakkaṃ «высшее колесо») were applied to the chapter files by `review/apply_review_fixes_ru.py`, not to the builders. The builders (`rails/build_rails_*_ru.py`) therefore **no longer reproduce** the 19 files in `AI_translation/russian/pi-2-russian-plain-rails_split_chapters/`.

Pre-fix state: `review/backup-pre-fixes/` (the chapter files as they were just before the fixes). Change list: `review/fixes-log.tsv` (192 changed lines).

## To rebuild

1. Run the builder(s) (`rails/build_rails_*_ru.py`) as before.
2. Refresh `review/backup-pre-fixes/` with that builder output (copy the 19 files).
3. Run `python -I -X utf8 0-INBOX\temp\pipeline\pi-2-ru\review\apply_review_fixes_ru.py` on the chapter dir. It asserts every expected count, so it stops if the builder output has drifted; re-running it on already-fixed files does nothing.
4. Re-run the checks: `check_chapter_ids.py`, `dashcheck.py`, `rails/extra_checks.py`, `rails/find_divergences_rails_ru.py` ("diverging: 0").

Never run a builder alone over the chapter dir without step 3: it would silently revert the review fixes.
