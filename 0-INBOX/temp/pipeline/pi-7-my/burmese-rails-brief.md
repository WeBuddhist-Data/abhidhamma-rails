# Brief: RAILS Burmese translation (pi-7, Paṭṭhāna «အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ»)

## Setup and rules
- Work in /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails on macOS (zsh).
- Python: `/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8`. Call it by that full path, never through a quoted shell variable. Put scripts in files.
- Write only in `0-INBOX/temp/pipeline/pi-7-my/rails/` and the output folder below.
- Never use the system temp directory: not /tmp, not /private/tmp, no `cd /tmp`.
- Don't commit.
- Never use the words for a planted starting value or its negative.
- No existing Burmese translation, nissaya or web source. Never open `0-INBOX/temp/language-priority/`.

## Read first
- `AI_translation/skills/rails-verse-translator.md`. Follow it.
- `0-INBOX/temp/pipeline/burmese-style.md`. It is binding, including the pi-1 … pi-7 termbase sections.
- `0-INBOX/temp/pipeline/pi-7-my/termbase/APPROVED.md`. It covers:
  - the LOCKED termbase `AI_translation/burmese/pi-7-pali-burmese-termbase-plain.md`, sha256 faef9155a30b9755e5706b8065de9dfb7d946c603fc5c84657b4ef6b4a74e14a;
  - its key choices;
  - the answer register.

  Never edit the termbase; report doubts. Also read the termbase notes in `pi-7-my/termbase/` (rails notes and the §A items decided / left).
- **Method model: the approved pi-6 Burmese rails run** in `0-INBOX/temp/pipeline/pi-6-my/rails/`:
  - notes-rails.md
  - adherence_my.py
  - classify_misses.py and classify_rules.py
  - my_formulas_rails.py
  - build_rails.py
  - apply_termbase.py and apply_fixes.py
  - rails_misses_check.py
  - line_scan.py
  - pi1234_identity.py
  - regen_rails.sh
  - make_proposals*.py

  Also read `pi-6-my/review/fix-notes.md` and pi-5's run. Copy and adapt; these are read only. Never edit pi-1-my/ … pi-6-my/.

## Inputs (read only)
- **Zero-shot (harmonised, final):** `AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters/` (75 files).
  - Its 18 generators: `pi-7-my/make_sample.py`, `make_ch1-01.py`, `make_ch1-03-05.py`, `make_ch2-*.py` (4), `make_ch3-*.py` (4), `make_ch4-*.py` (4), `make_ch5-*.py` (3), plus the preamble table in `regen_zeroshot.sh`. They import each other in memory: map the import chain first (see `harmonise-notes.md`). The generators are slow: run long builds in the background with zsh.
  - The shared module `pi-7-my/my7_formulas.py` and `pi-7-my/regen_zeroshot.sh`.
  - Do NOT change the zero-shot files or those scripts.
- **Pāli:** `AI_translation/pali/pi-7_split_chapters/`.
- **Keywords:** `AI_translation/pali/pi-7-keywords-by-reference-pali-plain.md`.
- **Keyword map:** `AI_translation/burmese/pi-7-keywords-by-reference-pali-burmese-plain.md`.
- **Text inconsistencies:**
  - `pi-7-my/mapper-my/map-harmonise-notes.md` §A (38 items);
  - the termbase notes: items 2, 6 (keyed slips), 8–13 are decided by a term; 1, 3, 4, 5, 6 (punctuation / label slips), 7 and 14 are left for the rails step.

## Output
`AI_translation/burmese/pi-7-burmese-plain-rails_split_chapters/`: 75 files with the same filenames, built reproducibly by `pi-7-my/rails/regen_rails.sh`.

## Method (as pi-6)
1. **Adherence on the zero-shot:** run `rails/adherence_my.py` and save `rails/adherence-zeroshot.txt`.
2. **Classify every miss** with `rails/classify_misses.py`, writing `adherence-classified.tsv`.
   - Each miss is GENUINE, INFLECTION, ARTEFACT or CONTEXT. Every non-GENUINE row carries a check that must match the segment, and the run fails on any unverified row.
   - The Paṭṭhāna is extremely formulaic (180k keyword uses), so classify by rule (pattern + check), not row by row.
   - A condition name in its frame form (name / -paccayā / -paccayena / counting locative / na-X) and the stacked qualifiers «A၊ B N» are INFLECTION where the termbase term is their dictionary form.
3. **Build the rails:** fix every GENUINE difference.
   - Systematic changes go in a RAILS layer: `rails/my_formulas_rails.py` patches my7_formulas / the generators in memory (respecting the import chain, so a patch reaches every downstream chapter), with exact counts; `rails/build_rails.py` builds.
   - Residual single cases become explicit rules in `apply_termbase.py`, logged in `apply-log.tsv`.
   - Keep these rules:
     - identical Pāli = identical Burmese (a change to a repeated condition frame or count frame goes into the shared layer, so every instance changes together);
     - the dash rule;
     - the quote rule;
     - «။» / «၊»;
     - the structure.
4. **Also fix the text inconsistencies of §A.**
   - Items decided by a term use the locked term.
   - Items left for rails are fixed where the Burmese can be made consistent without breaking the source-as-written rule. Source slips are translated as written; where only the spelling slipped, use the intended word.
   - The head nouns the text adds that no keyword carries («သဘောတရား», «စိတ်», «ကံ», «ရုပ်», «ပြဿနာ») stay where Burmese needs a head noun. Log them.
   - The drift the mapping found between groups (e.g. ṭhānāṭhānakosalla, suciṇṇāni, tadārammaṇatā, pavatti, nevadassanena, kātabba, the -sadisa shapes) gets ONE form book-wide, the termbase's where it decides, else the majority form.
   - Log each item: fixed or kept, and why.
5. **Termbase proposals:** if a phrase entry of the termbase is stale after a word-level decision, or a term is wrong, write it to `rails/termbase-proposals.tsv` with a reason. Do not change the termbase. The coordinator decides, as in pi-5.
6. **Re-check:**
   - GENUINE left: 0.
   - Every remaining miss is a known INFLECTION / ARTEFACT / CONTEXT row (`rails_misses_check.py`).
   - `line_scan.py`: 0 left.

## Verify (all must pass; put everything in regen_rails.sh)
- **For each of the 75 files:** `check_chapter_ids.py`, `pi-7-my/check_text_pe7.py` (run one at a time) and `pi-4-mr/check_marks.py` must be OK.
- **Cross-chapter:**
  - `pi-1-my/align_check_my.py <pali_dir> <rails_dir> --all` must give 0 differing; the harmonised zero-shot had 0. Use `pi-7-my/harmonise_align_explained.py` if needed.
  - `align_hidden_my.py` must give 0 unmatched.
- **pi-1 … pi-6 identity:** every pi-7 sentence that also occurs in pi-1 … pi-6 keeps their FINAL rails Burmese. Check with `pi-7-my/harmonise_pi123456.py` pointed at the rails folder. The zero-shot gave pi-1 12/12, pi-2 74/74, pi-3 2/2, pi-4 7230/7230, pi-5 6/6, pi-6 3/3; none may get worse. If a pi-6 termbase term would break this, report it instead.
- **Other checks:**
  - Adherence: GENUINE 0.
  - line_scan: 0 left.
  - The termbase hash equals the lock.
  - The protected md5s are unchanged: termbase, zero-shot chapters and merged file, generators, my7_formulas.py, regen_zeroshot.sh, the pi-1 … pi-6 rails texts and termbases.
  - A plain build (no patches) reproduces the zero-shot byte for byte.
- **Stability:** a second run of regen_rails.sh changes no rails byte.

## Log and report
- Write `rails/notes-rails.md` in the pi-6 format: method, files, misses by class (table), the rules / layer patches with counts, lines changed per chapter, the §A items (fixed / kept, why), checks, termbase proposals, and «Termbase doubts (termbase not changed)».
- Keep the final report short, numbers first: adherence before/after, GENUINE fixed, lines changed per chapter, all check results, termbase proposals and doubts.
