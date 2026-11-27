# Brief: RAILS Burmese translation (pi-1, Dhammasaṅgaṇī «သဘောတရားများကို စုစည်းရေတွက်ခြင်း»)

Work in /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails on macOS (zsh). Python: `/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8` (system python3 is too old). Scripts in files. Write only in `0-INBOX/temp/pipeline/pi-1-my/rails/` and the output folder below. Never use the system temp directory. Don't commit. Never use the words for a planted starting value or its negative. No existing Burmese translation, nissaya or web source (never open `0-INBOX/temp/language-priority/burmese-religious-affairs/`).

## Read first
- `AI_translation/skills/rails-verse-translator.md`, and follow it.
- `0-INBOX/temp/pipeline/burmese-style.md` (binding, incl. «pi-1 termbase (locked 2026-11-17)»).
- `0-INBOX/temp/pipeline/pi-1-my/termbase/APPROVED.md`: the LOCKED termbase `AI_translation/burmese/pi-1-pali-burmese-termbase-plain.md`, the approved wording changes, and the two rules (proper names stay names; nāma-rūpa = «စိတ်ပိုင်း / ရုပ်ပိုင်း»). Never edit the termbase; report doubts.
- Method model: the approved Marathi pi-1 rails run, `0-INBOX/temp/pipeline/pi-1-mr/rails/notes-rails.md` and its tools (classify_misses.py, apply_termbase.py, rails_misses_check.py, line_scan.py, regen_rails.sh) and `0-INBOX/temp/pipeline/pi-4-mr/rails/adherence_loose.py`. Copy and adapt; never copy Marathi wording.

## Inputs (read only)
- Zero-shot (harmonised, final): `AI_translation/burmese/pi-1-burmese-plain-zeroshot_split_chapters/` and its generators `pi-1-my/make_*.py` + `pi-1-my/my_formulas.py` + `pi-1-my/regen_zeroshot.sh`. Do NOT change the zero-shot files or those scripts.
- Pāli: `AI_translation/pali/pi-1_split_chapters/`; keywords: `AI_translation/pali/pi-1-keywords-by-reference-pali-plain.md`.

## Output
`AI_translation/burmese/pi-1-burmese-plain-rails_split_chapters/` (14 chapters, same filenames), built reproducibly by `pi-1-my/rails/regen_rails.sh`.

## Method
1. **Adherence on the zero-shot:** write `rails/adherence_my.py <keywords> <termbase> <split_dir> [report]` (Burmese version of adherence_loose.py: a keyword passes if ANY of its termbase senses' terms occurs in that segment; a term occurs if each of its content chunks occurs, after stripping the particles the mapping rules strip: ၏ ကို ၌ တွင် နှင့် မှ ဖြင့် အား သို့ သည် က များ တို့ and the attributive / verbal endings သော / သည် / ၍ / ခြင်း / မှု where the termbase form differs only by them). Save `rails/adherence-zeroshot.txt`.
2. **Classify every miss** (`rails/classify_misses.py` → `adherence-classified.tsv`): GENUINE (the text uses another word than the locked term in the same sense) / INFLECTION (same lemma, grammatical form) / ARTEFACT (compound stem, negation or privative, sense handled by another entry, proper name, nāma-rūpa rule). Each non-GENUINE row carries a check that must match the segment; the run fails on any unverified row.
3. **Build the rails:** fix every GENUINE difference.
   - Systematic changes (one Pāli formula or term repeated across many segments, e.g. uppanna = «ဖြစ်ပေါ်ပြီးသော» in the citta-opening formula and wherever uppannaṃ / uppannā stands; paṭiccasamuppāda = «အကြောင်းတို့ကို မှီ၍ ဖြစ်ပေါ်ပုံ»; Suññatavāro = «ဆိတ်သုဉ်းခြင်း ဖော်ပြချက်»; ākāsa = «ဟင်းလင်းပြင်» incl. the immaterial base; kusala-hetu «ကုသိုလ် အမြစ်»; vibhava; kodha; ñāṇa …): apply them in a RAILS layer of the generators, e.g. `rails/my_formulas_rails.py` overriding values of my_formulas.py in memory and `rails/build_rails.py` running the zero-shot generators' logic with that layer and writing to the rails folder. Never edit the zero-shot generators themselves.
   - Residual single cases: explicit rules as in the Marathi apply_termbase.py (segment ids, Pāli keyword check, exact replacement count; log every change in `rails/apply-log.tsv`).
   - Keep all of: identical Pāli = identical Burmese; synonym lists distinct; the two rules (proper names; nāma-rūpa); the dash rule; structure.
4. **Re-check:** adherence on the rails (`adherence-rails.txt`): GENUINE left 0; every remaining miss is a known INFLECTION / ARTEFACT row (`rails_misses_check.py`). Per-line scan of the GENUINE families (`line_scan.py`): required termbase form present, old form gone.

## Verify (all must pass; put everything in regen_rails.sh)
- For each of the 14 chapters: `0-INBOX/temp/pipeline/check_chapter_ids.py`, `pi-6-mr/check_text_pe.py`, `pi-4-mr/check_marks.py` print OK (delete chk-pe copies afterwards).
- Cross-chapter: `pi-1-my/align_check_my.py <pali_dir> <rails_dir> --all` → 0 differing; `pi-1-my/align_hidden_my.py` → 0 unmatched.
- Adherence: GENUINE 0. line_scan: 0 lines left.
- A second run of regen_rails.sh changes no rails byte; the zero-shot files are byte-identical to before (record their md5s first).

## Log and report
`rails/notes-rails.md` in the Marathi format: method, files, misses by class (table), the rules / layer overrides with counts, lines changed per chapter, checks, and «Termbase doubts (termbase not changed)». Final report short, numbers first: adherence before/after, GENUINE fixed, lines changed per chapter, all check results, termbase doubts.
