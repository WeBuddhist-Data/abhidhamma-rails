# Brief: RAILS Burmese translation (pi-4, Puggalapaññatti «ပုဂ္ဂိုလ်များကို သတ်မှတ်ဖော်ပြခြင်း»)

Work in /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails on macOS (zsh). Python: `/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8`. Scripts in files. Write only in `0-INBOX/temp/pipeline/pi-4-my/rails/` and the output folder below. Never use the system temp directory (not even /private/tmp). Don't commit. Never use the words for a planted starting value or its negative. No existing Burmese translation, nissaya or web source (never open `0-INBOX/temp/language-priority/`).

## Read first
- `AI_translation/skills/rails-verse-translator.md`, and follow it.
- `0-INBOX/temp/pipeline/burmese-style.md` (binding, incl. the pi-1 … pi-4 termbase sections).
- `0-INBOX/temp/pipeline/pi-4-my/termbase/APPROVED.md`: the LOCKED termbase `AI_translation/burmese/pi-4-pali-burmese-termbase-plain.md` (sha256 c6a4e611fea053d20376b2418f0a83d7086d6ee99883d67146fb49033e7eb9e9) and its rules (person-type names binding; proper names stay names; nāma-rūpa; bahiddhā; the two rails-step notes indriyānaṃ ^4-M-6 and phalaṃ ^4-116 / ^4-117). Never edit the termbase; report doubts.
- **Method model: the approved pi-3 and pi-2 Burmese rails runs** `0-INBOX/temp/pipeline/pi-3-my/rails/` and `pi-2-my/rails/` (notes-rails.md, adherence_my.py, classify_misses.py, map_vs_termbase.py, my_formulas_rails.py, build_rails.py, apply_termbase.py, apply_fixes.py, rails_misses_check.py, line_scan.py, regen_rails.sh). Copy and adapt; read only; never edit pi-1-my/, pi-2-my/ or pi-3-my/.

## Inputs (read only)
- Zero-shot (harmonised, final): `AI_translation/burmese/pi-4-burmese-plain-zeroshot_split_chapters/` and its generators `pi-4-my/make_sample.py`, `make_ch3-4.py`, `make_ch5.py`, `make_ch6-11.py` + `pi-4-my/my4_formulas.py` (+ terms_my4.py) + `pi-4-my/regen_zeroshot.sh`. Do NOT change the zero-shot files or those scripts.
- Pāli: `AI_translation/pali/pi-4_split_chapters/`; keywords: `AI_translation/pali/pi-4-keywords-by-reference-pali-plain.md`; keyword map `AI_translation/burmese/pi-4-keywords-by-reference-pali-burmese-plain.md`.

## Output
`AI_translation/burmese/pi-4-burmese-plain-rails_split_chapters/` (12 files, same filenames), built reproducibly by `pi-4-my/rails/regen_rails.sh`.

## Method (as pi-2)
1. **Adherence on the zero-shot** (`rails/adherence_my.py`, pi-2's): save `rails/adherence-zeroshot.txt`.
2. **Classify every miss** (`rails/classify_misses.py` → `adherence-classified.tsv`): GENUINE / INFLECTION / ARTEFACT, each non-GENUINE row with a check that must match the segment; the run fails on any unverified row.
3. **Build the rails:** fix every GENUINE difference. Systematic changes in a RAILS layer (`rails/my_formulas_rails.py` patching my3_formulas / the generators in memory, with exact counts; `rails/build_rails.py`); residual single cases as explicit rules (`apply_termbase.py`, log `apply-log.tsv`). Keep identical Pāli = identical Burmese, the dash rule, structure.
4. **Also fix the text inconsistencies** logged in `pi-4-my/mapper-my/map-harmonise-notes.md` (15) where the locked termbase decides them (senāsana, sappi, dīgharattaṃ, paṭipanna, suṇāti, abhisamaya, nikati vs sāṭheyya, dubbaṇṇa, phale ṭhito, sātthaṃ sabyañjanaṃ …), plus ^4-M-14 «မဂ်နှင့် ပြည့်စုံသူ» (person-type name as approved), ^4-M-10 (22) / (23) (four Pāli names: give each its approved name if the table has four), ^4-198 gataṃ «မှား» (check the text: araññagataṃ etc. «ရောက်သော»; fix the text only if the Burmese is wrong), and the termbase's rails-step notes (indriyānaṃ ^4-M-6 «စွမ်းရည်»; phalaṃ ^4-116 / ^4-117 «အကျိုး»); each logged. The person-type names stay exactly as approved.
5. **Re-check:** GENUINE left 0; every remaining miss a known INFLECTION / ARTEFACT row (`rails_misses_check.py`); `line_scan.py` 0 left.

## Verify (all must pass; put everything in regen_rails.sh)
- For each of the 12 files: `check_chapter_ids.py`, `pi-6-mr/check_text_pe.py` (via a rails/chk-pe wrapper as pi-2), `pi-4-mr/check_marks.py` OK.
- Cross-chapter: `pi-1-my/align_check_my.py <pali_dir> <rails_dir> --all` → only the zero-shot's accepted differences (the zero-shot had 0 differing; none new); `align_hidden_my.py` → 0 unmatched.
- **pi-1 / pi-2 / pi-3 identity:** every pi-4 sentence that also occurs in pi-1, pi-2 or pi-3 keeps their FINAL rails Burmese (`pi-4-my/harmonise_pi123.py` with the rails folder: 45/45, 35/36 + 1 explained, 2/2). If a pi-4 termbase term would break that, report it instead.
- Adherence: GENUINE 0. line_scan: 0 left. Termbase hash = the lock. Protected md5s (termbase, zero-shot chapters and merged file, generators, my4_formulas.py, terms_my4.py, regen_zeroshot.sh, the pi-1 / pi-2 / pi-3 rails texts and termbases) unchanged. A plain build (no patches) reproduces the zero-shot byte for byte.
- A second run of regen_rails.sh changes no rails byte.

## Log and report
`rails/notes-rails.md` in the pi-3 format: method, files, misses by class (table), the rules / layer patches with counts, lines changed per chapter, checks, and «Termbase doubts (termbase not changed)». Final report short, numbers first: adherence before/after, GENUINE fixed, lines changed per chapter, all check results, termbase doubts.
