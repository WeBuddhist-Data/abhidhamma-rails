# Brief: RAILS Burmese translation (pi-5, Kathāvatthu «အငြင်းပွားရာ အကြောင်းအရာများကို ဆွေးနွေးခြင်း»)

Work in /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails on macOS (zsh). Python: `/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8`. Scripts in files. Write only in `0-INBOX/temp/pipeline/pi-5-my/rails/` and the output folder below. Never use the system temp directory (not /tmp, not /private/tmp, no `cd /tmp`). Don't commit. Never use the words for a planted starting value or its negative. No existing Burmese translation, nissaya or web source (never open `0-INBOX/temp/language-priority/`).

## Read first
- `AI_translation/skills/rails-verse-translator.md`, and follow it.
- `0-INBOX/temp/pipeline/burmese-style.md` (binding, incl. the pi-1 … pi-5 termbase sections).
- `0-INBOX/temp/pipeline/pi-5-my/termbase/APPROVED.md`: the LOCKED termbase `AI_translation/burmese/pi-5-pali-burmese-termbase-plain.md` (sha256 6f2558f8460aa03fc03a458b36ce49d5fce7872d8c202febe03f030426e621de), its coordinator changes (paṭivedha family «ထိုးဖောက်၍ သိ…», abhisametuṃ, thero «မထေရ်») and its «For the rails step» notes (eva: the 10 restrictive uses may keep «သာ» as a context sense; ṭhiti in viññāṇaṭṭhiti, uppādeyya in methunaṃ uppādeyya, dānaṃ as the gift: render by context, log as context senses). Never edit the termbase; report doubts.
- **Method model: the approved pi-4 Burmese rails run** `0-INBOX/temp/pipeline/pi-4-my/rails/` (notes-rails.md, adherence_my.py, classify_misses.py, map_vs_termbase.py, my_formulas_rails.py, build_rails.py, apply_termbase.py, apply_fixes.py, rails_misses_check.py, line_scan.py, regen_rails.sh) and `pi-4-my/review/fix-notes.md`; also pi-3's and pi-2's. Copy and adapt; read only; never edit pi-1-my/ … pi-4-my/.

## Inputs (read only)
- Zero-shot (harmonised, final): `AI_translation/burmese/pi-5-burmese-plain-zeroshot_split_chapters/` (32 files) and its generators `pi-5-my/make_sample.py`, `make_ch2-5.py`, `make_ch6-10.py`, `make_ch11-12.py`, `make_ch13-16.py`, `make_ch17-20.py`, `make_ch21-25.py`, `make_ch26-31.py` + `pi-5-my/my5_formulas.py` (+ terms_my5.py) + `pi-5-my/regen_zeroshot.sh`. Do NOT change the zero-shot files or those scripts.
- Pāli: `AI_translation/pali/pi-5_split_chapters/`; keywords: `AI_translation/pali/pi-5-keywords-by-reference-pali-plain.md`; keyword map `AI_translation/burmese/pi-5-keywords-by-reference-pali-burmese-plain.md`.
- Text inconsistencies: `pi-5-my/mapper-my/map-harmonise-notes.md` §A (32 items) and the termbase report `pi-5-my/termbase/termbase-decisions.md` (26 decided by a term, 10 left for the rails step).

## Output
`AI_translation/burmese/pi-5-burmese-plain-rails_split_chapters/` (32 files, same filenames), built reproducibly by `pi-5-my/rails/regen_rails.sh`.

## Method (as pi-4)
1. **Adherence on the zero-shot** (`rails/adherence_my.py`): save `rails/adherence-zeroshot.txt`.
2. **Classify every miss** (`rails/classify_misses.py` → `adherence-classified.tsv`): GENUINE / INFLECTION / ARTEFACT, each non-GENUINE row with a check that must match the segment; the run fails on any unverified row. The book is large and formulaic: classify by rule (pattern + check), not row by row.
3. **Build the rails:** fix every GENUINE difference. Systematic changes in a RAILS layer (`rails/my_formulas_rails.py` patching my5_formulas / the generators in memory, with exact counts; `rails/build_rails.py`); residual single cases as explicit rules (`apply_termbase.py`, log `apply-log.tsv`). Keep identical Pāli = identical Burmese (a change to a repeated dialectic frame goes into the shared layer, so every instance changes together), the dash rule, the quote rule (no quote mark where the Pāli has none), structure.
4. **Also fix the text inconsistencies** of §A: the 26 a term decides (use the locked term), and the 10 left for rails where the Burmese can be made consistent without breaking the source-as-written rule (uddāna / saṃkhitta: keep the text; ^5-371 untranslated words: translate them from the Pāli; ^5-857 jīvitā: render it; ^5-918 Mahāniyāmo: one item; the siglum at ^5-525: as the other sigla; negation spacing and vagga ordinals: one form book-wide as the harmonise decided). Each logged. Also the 8 lines with fewer quote marks than the Pāli (harmonise notes «Left»: 1:27, 10:157, 10:251-253, 10:342, 25:44, 26:130): add the Pāli's quote marks if a layer patch can do it cleanly; otherwise log them.
5. **Re-check:** GENUINE left 0; every remaining miss a known INFLECTION / ARTEFACT row (`rails_misses_check.py`); `line_scan.py` 0 left.

## Verify (all must pass; put everything in regen_rails.sh)
- For each of the 32 files: `check_chapter_ids.py`, `pi-6-mr/check_text_pe.py` (via a rails/chk-pe wrapper as pi-4), `pi-4-mr/check_marks.py` OK.
- Cross-chapter: `pi-1-my/align_check_my.py <pali_dir> <rails_dir> --all` → only the zero-shot's accepted difference (1, explained by `pi-5-my/harmonise_align_explained.py`), none new; `align_hidden_my.py` → 0 unmatched.
- **pi-1 … pi-4 identity:** every pi-5 sentence that also occurs in pi-1 … pi-4 keeps their FINAL rails Burmese (`pi-5-my/harmonise_pi1234.py` with the rails folder: pi-1 2/2, pi-2 4/4, pi-3 2/21 + 19 explained, pi-4 5/7 + 2 explained). If a pi-5 termbase term would break that, report it instead.
- Adherence: GENUINE 0. line_scan: 0 left. Termbase hash = the lock. Protected md5s (termbase, zero-shot chapters and merged file, generators, my5_formulas.py, terms_my5.py, regen_zeroshot.sh, the pi-1 … pi-4 rails texts and termbases) unchanged. A plain build (no patches) reproduces the zero-shot byte for byte.
- A second run of regen_rails.sh changes no rails byte.

## Log and report
`rails/notes-rails.md` in the pi-4 format: method, files, misses by class (table), the rules / layer patches with counts, lines changed per chapter, the §A items (fixed / kept, why), checks, and «Termbase doubts (termbase not changed)». Final report short, numbers first: adherence before/after, GENUINE fixed, lines changed per chapter, all check results, termbase doubts.
