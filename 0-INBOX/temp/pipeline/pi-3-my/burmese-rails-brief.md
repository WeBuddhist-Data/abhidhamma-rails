# Brief: RAILS Burmese translation (pi-3, Dhātukathā «ဓာတ်များအကြောင်း ဆွေးနွေးခြင်း»)

Work in /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails on macOS (zsh). Python: `/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8`. Scripts in files. Write only in `0-INBOX/temp/pipeline/pi-3-my/rails/` and the output folder below. Never use the system temp directory (not even /private/tmp). Don't commit. Never use the words for a planted starting value or its negative. No existing Burmese translation, nissaya or web source (never open `0-INBOX/temp/language-priority/`).

## Read first
- `AI_translation/skills/rails-verse-translator.md`, and follow it.
- `0-INBOX/temp/pipeline/burmese-style.md` (binding, incl. the pi-1 / pi-2 / pi-3 termbase sections).
- `0-INBOX/temp/pipeline/pi-3-my/termbase/APPROVED.md`: the LOCKED termbase `AI_translation/burmese/pi-3-pali-burmese-termbase-plain.md` (sha256 a50f32e2d4c8c085259215fc37eec92dfe04e1f607fe553272371972912a8090) and the rules (proper names stay names; nāma-rūpa «စိတ်ပိုင်း / ရုပ်ပိုင်း»). Never edit the termbase; report doubts.
- **Method model: the approved pi-2 Burmese rails run** `0-INBOX/temp/pipeline/pi-2-my/rails/` (notes-rails.md, adherence_my.py, classify_misses.py, my_formulas_rails.py, build_rails.py, apply_termbase.py, apply_fixes.py, rails_misses_check.py, line_scan.py, pi1_identity.py, align_kept.py, regen_rails.sh) and `pi-2-my/review/fix-notes.md`. Copy and adapt; read only; never edit pi-1-my/ or pi-2-my/.

## Inputs (read only)
- Zero-shot (harmonised, final): `AI_translation/burmese/pi-3-burmese-plain-zeroshot_split_chapters/` and its generators `pi-3-my/make_sample.py`, `make_ch3-6-8-9.py`, `make_ch7-10-11.py`, `make_ch12-15.py` + `pi-3-my/my3_formulas.py` + `pi-3-my/regen_zeroshot.sh`. Do NOT change the zero-shot files or those scripts.
- Pāli: `AI_translation/pali/pi-3_split_chapters/`; keywords: `AI_translation/pali/pi-3-keywords-by-reference-pali-plain.md`; keyword map `AI_translation/burmese/pi-3-keywords-by-reference-pali-burmese-plain.md`.

## Output
`AI_translation/burmese/pi-3-burmese-plain-rails_split_chapters/` (16 files, same filenames), built reproducibly by `pi-3-my/rails/regen_rails.sh`.

## Method (as pi-2)
1. **Adherence on the zero-shot** (`rails/adherence_my.py`, pi-2's): save `rails/adherence-zeroshot.txt`.
2. **Classify every miss** (`rails/classify_misses.py` → `adherence-classified.tsv`): GENUINE / INFLECTION / ARTEFACT, each non-GENUINE row with a check that must match the segment; the run fails on any unverified row.
3. **Build the rails:** fix every GENUINE difference. Systematic changes in a RAILS layer (`rails/my_formulas_rails.py` patching my3_formulas / the generators in memory, with exact counts; `rails/build_rails.py`); residual single cases as explicit rules (`apply_termbase.py`, log `apply-log.tsv`). Keep identical Pāli = identical Burmese, the dash rule, structure.
4. **Also fix the text inconsistencies** logged in `pi-3-my/mapper-my/map-harmonise-notes.md` where the locked termbase decides them (maccu «သေခြင်း»; pucchake «ဖော်ပြချက်» vs pucchakena «မေးခွန်း» as two senses; arūpa spacing: planes «ရုပ်မရှိသော», non-material aggregates «ရုပ် မဟုတ်သော»; «တို့» / «များ» only where a termbase term decides it), each logged.
5. **Re-check:** GENUINE left 0; every remaining miss a known INFLECTION / ARTEFACT row (`rails_misses_check.py`); `line_scan.py` 0 left.

## Verify (all must pass; put everything in regen_rails.sh)
- For each of the 16 files: `check_chapter_ids.py`, `pi-6-mr/check_text_pe.py` (via a rails/chk-pe wrapper as pi-2), `pi-4-mr/check_marks.py` OK.
- Cross-chapter: `pi-1-my/align_check_my.py <pali_dir> <rails_dir> --all` → only the zero-shot's accepted differences (the 5 explained by the subject's number, `pi-3-my/harmonise_align_kept.py`), none new; `align_hidden_my.py` → 0 unmatched.
- **pi-1 / pi-2 identity:** every pi-3 sentence that also occurs in pi-1 or pi-2 keeps their FINAL rails Burmese (`pi-3-my/harmonise_pi12.py` with the rails folder, n / n). If a pi-3 termbase term would break that, report it instead.
- Adherence: GENUINE 0. line_scan: 0 left. Termbase hash = the lock. Protected md5s (termbase, zero-shot chapters and merged file, generators, my3_formulas.py, regen_zeroshot.sh, the pi-1 / pi-2 rails texts and termbases) unchanged. A plain build (no patches) reproduces the zero-shot byte for byte.
- A second run of regen_rails.sh changes no rails byte.

## Log and report
`rails/notes-rails.md` in the pi-2 format: method, files, misses by class (table), the rules / layer patches with counts, lines changed per chapter, checks, and «Termbase doubts (termbase not changed)». Final report short, numbers first: adherence before/after, GENUINE fixed, lines changed per chapter, all check results, termbase doubts.
