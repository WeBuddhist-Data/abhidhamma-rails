# Brief: RAILS Burmese translation (pi-6, Yamaka «အတွဲလိုက် မေးဖြေခြင်း»)

## Setup and rules
- Work in /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails on macOS (zsh).
- Python: `/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8`. Call it by that full path, never through a quoted shell variable. Put scripts in files.
- Write only in `0-INBOX/temp/pipeline/pi-6-my/rails/` and the output folder below.
- Never use the system temp directory: not /tmp, not /private/tmp, no `cd /tmp`.
- Don't commit.
- Never use the words for a planted starting value or its negative.
- No existing Burmese translation, nissaya or web source. Never open `0-INBOX/temp/language-priority/`.

## Read first
- `AI_translation/skills/rails-verse-translator.md`. Follow it.
- `0-INBOX/temp/pipeline/burmese-style.md`. It is binding, including the pi-1 … pi-6 termbase sections.
- `0-INBOX/temp/pipeline/pi-6-my/termbase/APPROVED.md`. It covers:
  - the LOCKED termbase `AI_translation/burmese/pi-6-pali-burmese-termbase-plain.md`, sha256 847e49cdef8bc8c3f90d2de9f92fd0c6479f60e17a04c8243286b12602a86453;
  - its key choices;
  - the agent-noun rule: where the text has the attributive before a person noun, the miss is INFLECTION, not a change;
  - the answer register.

  Never edit the termbase; report doubts. Also read `pi-6-my/termbase/notes-part5.txt`, which has the rails notes and §A.
- **Method model: the approved pi-5 Burmese rails run** in `0-INBOX/temp/pipeline/pi-5-my/rails/`:
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

  Also read `pi-5-my/review/fix-notes.md` and pi-4's run. Copy and adapt; these are read only. Never edit pi-1-my/ … pi-5-my/.

## Inputs (read only)
- **Zero-shot (harmonised, final):** `AI_translation/burmese/pi-6-burmese-plain-zeroshot_split_chapters/` (44 files).
  - Its generators: `pi-6-my/make_sample.py`, `make_ch2-02-4-5.py`, `make_ch3.py`, `make_ch6-8.py`, `make_ch7a.py`, `make_ch7b.py`, `make_ch9-10a.py`, `make_ch10b.py`, `make_ch10c.py`.
  - The shared module `pi-6-my/my6_formulas.py` and `pi-6-my/regen_zeroshot.sh`.
  - Do NOT change the zero-shot files or those scripts.
- **Pāli:** `AI_translation/pali/pi-6_split_chapters/`.
- **Keywords:** `AI_translation/pali/pi-6-keywords-by-reference-pali-plain.md`.
- **Keyword map:** `AI_translation/burmese/pi-6-keywords-by-reference-pali-burmese-plain.md`.
- **Text inconsistencies:**
  - `pi-6-my/mapper-my/map-harmonise-notes.md` §A (14 items);
  - the termbase notes: items 2, 6 (keyed slips), 8–13 are decided by a term; 1, 3, 4, 5, 6 (punctuation / label slips), 7 and 14 are left for the rails step.

## Output
`AI_translation/burmese/pi-6-burmese-plain-rails_split_chapters/`: 44 files with the same filenames, built reproducibly by `pi-6-my/rails/regen_rails.sh`.

## Method (as pi-5)
1. **Adherence on the zero-shot:** run `rails/adherence_my.py` and save `rails/adherence-zeroshot.txt`.
2. **Classify every miss** with `rails/classify_misses.py`, writing `adherence-classified.tsv`.
   - Each miss is GENUINE, INFLECTION, ARTEFACT or CONTEXT. Every non-GENUINE row carries a check that must match the segment, and the run fails on any unverified row.
   - The Yamaka is extremely formulaic, so classify by rule (pattern + check), not row by row.
   - The agent-noun vs attributive forms of the beings / persons genitives are INFLECTION.
3. **Build the rails:** fix every GENUINE difference.
   - Systematic changes go in a RAILS layer: `rails/my_formulas_rails.py` patches my6_formulas / the generators in memory, with exact counts; `rails/build_rails.py` builds.
   - Residual single cases become explicit rules in `apply_termbase.py`, logged in `apply-log.tsv`.
   - Keep these rules:
     - identical Pāli = identical Burmese (a change to a repeated question frame goes into the shared layer, so every instance changes together);
     - the dash rule;
     - the quote rule;
     - «။» / «၊»;
     - the structure.
4. **Also fix the text inconsistencies of §A.**
   - Items decided by a term use the locked term.
   - Items left for rails are fixed where the Burmese can be made consistent without breaking the source-as-written rule. Source slips are translated as written; where only the spelling slipped, use the intended word.
   - The words the text adds that no keyword carries («အရာ», «သဘောတရား», «အတွဲ», «ပုဂ္ဂိုလ်», item 14) stay where Burmese needs a head noun. Log them.
   - Log each item: fixed or kept, and why.
5. **Termbase proposals:** if a phrase entry of the termbase is stale after a word-level decision, or a term is wrong, write it to `rails/termbase-proposals.tsv` with a reason. Do not change the termbase. The coordinator decides, as in pi-5.
6. **Re-check:**
   - GENUINE left: 0.
   - Every remaining miss is a known INFLECTION / ARTEFACT / CONTEXT row (`rails_misses_check.py`).
   - `line_scan.py`: 0 left.

## Verify (all must pass; put everything in regen_rails.sh)
- **For each of the 44 files:** `check_chapter_ids.py`, `pi-6-mr/check_text_pe.py` (via a rails wrapper, as pi-5) and `pi-4-mr/check_marks.py` must be OK.
- **Cross-chapter:**
  - `pi-1-my/align_check_my.py <pali_dir> <rails_dir> --all` must give 0 differing; the harmonised zero-shot had 0. Use `pi-6-my/harmonise_align_explained.py` if needed.
  - `align_hidden_my.py` must give 0 unmatched.
- **pi-1 … pi-5 identity:** every pi-6 sentence that also occurs in pi-1 … pi-5 keeps their FINAL rails Burmese. Check with `pi-6-my/harmonise_pi12345.py` pointed at the rails folder. The zero-shot gave pi-1 10/10, pi-2 14/14, pi-3 10/332 + 322 explained (answer register), pi-4 10/10, pi-5 2791/2791; none may get worse. If a pi-6 termbase term would break this, report it instead.
- **Other checks:**
  - Adherence: GENUINE 0.
  - line_scan: 0 left.
  - The termbase hash equals the lock.
  - The protected md5s are unchanged: termbase, zero-shot chapters and merged file, generators, my6_formulas.py, regen_zeroshot.sh, the pi-1 … pi-5 rails texts and termbases.
  - A plain build (no patches) reproduces the zero-shot byte for byte.
- **Stability:** a second run of regen_rails.sh changes no rails byte.

## Log and report
- Write `rails/notes-rails.md` in the pi-5 format: method, files, misses by class (table), the rules / layer patches with counts, lines changed per chapter, the §A items (fixed / kept, why), checks, termbase proposals, and «Termbase doubts (termbase not changed)».
- Keep the final report short, numbers first: adherence before/after, GENUINE fixed, lines changed per chapter, all check results, termbase proposals and doubts.
