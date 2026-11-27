# Brief: Burmese zero-shot SAMPLE for pi-5 (Kathāvatthu)

Work in /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails on macOS (zsh). Use the Read/Write tools for files and call Python as `/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8` (the system python3 is too old). Write helper scripts to files rather than inline `-c` with regexes. Scratch, scripts and notes only in `0-INBOX/temp/pipeline/pi-5-my/`. Never use the system temp directory. Do not commit. Never use the words for a planted starting value or its negative; say "sample" or "model".

You write the model that later agents copy for the rest of the book (33 files, 924 KB of Pāli), so the shared pieces (formula module, term list) matter as much as the text. Write part by part and save as soon as each passes: you may be paused for usage limits and resumed later. Keep your notes current. Stop after the sample: the user reviews it.

## Source rule (binding, user 2026-11-16/17)
Translate FROM THE PĀLI only. Never look up, open or copy any existing Burmese translation or nissaya (never open `0-INBOX/temp/language-priority/`), and do no web searches.

## Read first
- `0-INBOX/temp/pipeline/burmese-style.md`: binding rules, typography, the dash rule, the approved core terms and the locked pi-1 and pi-2 termbase sections.
- `AI_translation/skills/zeroshot-translator.md` and `AI_translation/audience_profile/plain.md`.
- **pi-1, pi-2, pi-3 and pi-4 Burmese are binding** wherever the Kathāvatthu uses their terms, lists and sentences (khandha / āyatana / dhātu / indriya names, the Mātikā triads and dyads, path and fruit, the person types sotāpanna … arahant and the pi-4 person-type names, jhāna, kilesa, sīla, the realms): use the FINAL Burmese, i.e. the rails texts `AI_translation/burmese/pi-1-burmese-plain-rails_split_chapters/`, `AI_translation/burmese/pi-2-burmese-plain-rails_split_chapters/`, `AI_translation/burmese/pi-3-burmese-plain-rails_split_chapters/`, `AI_translation/burmese/pi-4-burmese-plain-rails_split_chapters/` and the locked termbases `AI_translation/burmese/pi-{1,2,3,4}-pali-burmese-termbase-plain.md` (see their `pi-N-my/termbase/APPROVED.md`). The pi-2 module `0-INBOX/temp/pipeline/pi-2-my/my2_formulas.py` and its rails layer `pi-2-my/rails/my_formulas_rails.py` + `rails/build_rails.py` (and pi-1's `pi-1-my/my_formulas.py`, `pi-1-my/rails/`) and the pi-3 / pi-4 modules `pi-3-my/my3_formulas.py`, `pi-4-my/my4_formulas.py` show how the final strings are produced: import or copy them READ-ONLY (never edit anything in pi-1-my/ … pi-4-my/), so identical Pāli gets identical Burmese. Where the zero-shot module and the rails differ, the RAILS text wins.
- Method model (formula module + generator): `pi-4-my/make_sample.py`, `pi-4-my/check_sample.py`, `pi-3-my/make_sample.py`; the Marathi pi-5 run `0-INBOX/temp/pipeline/pi-5-mr/make_ch1.py`, `mr_formulas.py` and its notes (method and frame inventory only, never Marathi words).
- Cross-check of MEANING only (never wording): the English pi-5 zero-shot `AI_translation/english/pi-5-english-plain-zeroshot_split_chapters/<same file>` and the Marathi pi-5 rails `AI_translation/marathi/pi-5-marathi-plain-rails_split_chapters/<same file>`.

## About the text
The Kathāvatthu («Points of Controversy») is a set of debates (kathā) between the orthodox speaker (sakavādī) and an opponent (paravādī), grouped in vaggas. Each debate is built from a few fixed dialectic formulas repeated with different propositions: the question «X … ti?», the answers «Āmantā.» / «Na hevaṃ vattabbe.», the refutation «Ājānāhi niggahaṃ. Hañci …, tena vata re vattabbe – "…"ti. Yaṃ tattha vadesi – "vattabbe kho – ‘…,’ no ca vattabbe – ‘…’"ti micchā.», «Ājānāhi paṭikammaṃ.», the five-fold sets (Anulomapañcakaṃ, Paccanīkapañcakaṃ …), the eight-fold refutations, then the sutta quotations («Nanu vuttaṃ bhagavatā – "…"ti? Āmantā. Teneva …»). The first debate, Puggalakathā, asks whether a person exists in the ultimate sense («Puggalo upalabbhati saccikaṭṭhaparamatthenāti?»).
Everything turns on: the dialectic frames (each the same Burmese every time, as a script table; questions with «လော» / «နည်း»); POLARITY (upalabbhati / nupalabbhati, vattabbe / no ca vattabbe, Āmantā / Na hevaṃ vattabbe: check every clause by script); the propositions (plain, exact, same Burmese wherever the Pāli proposition repeats); the sakavādī / paravādī labels and the bracketed editorial notes («[iminā lakkhaṇena …]»: translated); the quotes (“…” outer, ‘…’ inner, nested as in the Pāli); sutta quotations from pi-1 / pi-2 / pi-4 where they repeat.

## Your output
1. `AI_translation/burmese/pi-5-burmese-plain-zeroshot_split_chapters/preamble.md` (Pāli `AI_translation/pali/pi-5_split_chapters/preamble.md`; same frame as the earlier preambles).
2. The WHOLE of `1-puggalakatha.md` (119 KB), same filename in that folder (save part by part).
3. `pi-5-my/my5_formulas.py`: the shared pi-5 module later agents import (every dialectic formula as a function of its proposition(s); the answer words; the set names (Anulomapañcakaṃ …); sakavādī / paravādī; kathā and vagga headings, ordinals and colophons; the editorial-note table; proposition building blocks; reused terms).
4. `pi-5-my/make_sample.py` (imports my5_formulas.py, writes the two files; frames and tables for the repeated parts; hand-written strings for the unique propositions and quotations kept in a table in the script; stops on any unmatched sentence).
5. `pi-5-my/my5-zeroshot-terms.md`: every formula and term as «Pāli = Burmese», grouped: the proposed Burmese book title for the Kathāvatthu (plain, Burmese only), kathā / vagga heading patterns, all dialectic formulas, the set names, sakavādī / paravādī, the key propositions of the Puggalakathā.
6. `pi-5-my/check_sample.py`: per-line check (polarity per clause: upalabbhati / nupalabbhati, vattabbe / no ca vattabbe, Āmantā / Na hevaṃ; numbers; quote nesting; every recurring proposition the same Burmese; table values, 0 mismatches) plus a **pi-1 … pi-4 reuse test**: every term and Pāli sentence of the sample that also occurs in pi-1, pi-2, pi-3 or pi-4 must have exactly their final Burmese (report n / n identical).
7. `pi-5-my/notes-sample.md`: choices, unsure Pāli, source slips.

## Rules
- Identical Pāli = identical Burmese (within pi-5 and with pi-1 … pi-4 final). Each Pāli synonym its own Burmese.
- Polarity and numbers exact; check by script. Headings keep their #-level. Block IDs exact, one blank line between segments, the source's number of non-empty lines per segment, no double blank lines.
- «…pe…» / «…Pe…» become one «…». DASH RULE: «–» only where the Pāli line has one, same spot and count. No «।», no «:-», no «?»: questions end with their question particle (လော / နည်း) and «။». Statements end with «။».
- Digits as the Pāli, e.g. «(1)». Variant brackets as pi-1: «[ပါဌ်ကွဲ (Syā.): …]», «[စာလုံးပေါင်းကွဲ (…): …]».
- Natural plain Burmese; nothing added. Book title in Burmese only. Source slips: translate as written, flag in notes.

## Verify every file (all must pass)
```
/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 0-INBOX/temp/pipeline/check_chapter_ids.py AI_translation/pali/pi-5_split_chapters AI_translation/burmese/pi-5-burmese-plain-zeroshot_split_chapters <ch>.md
/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 0-INBOX/temp/pipeline/pi-6-mr/check_text_pe.py AI_translation/pali/pi-5_split_chapters/<ch>.md AI_translation/burmese/pi-5-burmese-plain-zeroshot_split_chapters/<ch>.md
/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 0-INBOX/temp/pipeline/pi-4-mr/check_marks.py AI_translation/pali/pi-5_split_chapters/<ch>.md AI_translation/burmese/pi-5-burmese-plain-zeroshot_split_chapters/<ch>.md
```
All must print OK (delete your chk-pe copies in `pi-6-mr/chk-pe/` afterwards). Plus your own check: 0 mismatches, and the reuse test n / n.

## Final report (short)
Checks per file, segment counts, your check result, the reuse test, the main choices (book title, headings, the dialectic formulas, what was reused from pi-1 … pi-4, new terms), unsure Pāli and source slips.

## Approval
The user has given a standing go-ahead (2026-11-19): the coordinator reviews and approves the sample; still stop after the sample and report.
