# Brief: Burmese zero-shot SAMPLE for pi-4 (Puggalapaññatti)

Work in /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails on macOS (zsh). Use the Read/Write tools for files and call Python as `/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8` (the system python3 is too old). Write helper scripts to files rather than inline `-c` with regexes. Scratch, scripts and notes only in `0-INBOX/temp/pipeline/pi-4-my/`. Never use the system temp directory. Do not commit. Never use the words for a planted starting value or its negative; say "sample" or "model".

You write the model that later agents copy for the rest of the book (12 files, 155 KB of Pāli), so the shared pieces (formula module, term list) matter as much as the text. Write part by part and save as soon as each passes: you may be paused for usage limits and resumed later. Keep your notes current. Stop after the sample: the user reviews it.

## Source rule (binding, user 2026-11-16/17)
Translate FROM THE PĀLI only. Never look up, open or copy any existing Burmese translation or nissaya (never open `0-INBOX/temp/language-priority/`), and do no web searches.

## Read first
- `0-INBOX/temp/pipeline/burmese-style.md`: binding rules, typography, the dash rule, the approved core terms and the locked pi-1 and pi-2 termbase sections.
- `AI_translation/skills/zeroshot-translator.md` and `AI_translation/audience_profile/plain.md`.
- **pi-1, pi-2 and pi-3 Burmese are binding** wherever the Puggalapaññatti uses their terms and lists (the mātikā lists the khandha / āyatana / dhātu / sacca / indriya names; the person types use the jhāna, vimokkha, āsava, path-and-fruit, sīla and kilesa terms of pi-1 / pi-2): use the FINAL Burmese, i.e. the rails texts `AI_translation/burmese/pi-1-burmese-plain-rails_split_chapters/`, `AI_translation/burmese/pi-2-burmese-plain-rails_split_chapters/`, `AI_translation/burmese/pi-3-burmese-plain-rails_split_chapters/` and the locked termbases `AI_translation/burmese/pi-1-pali-burmese-termbase-plain.md`, `pi-2-pali-burmese-termbase-plain.md`, `pi-3-pali-burmese-termbase-plain.md` (see their `pi-N-my/termbase/APPROVED.md`). The pi-2 module `0-INBOX/temp/pipeline/pi-2-my/my2_formulas.py` and its rails layer `pi-2-my/rails/my_formulas_rails.py` + `rails/build_rails.py` (and pi-1's `pi-1-my/my_formulas.py`, `pi-1-my/rails/`) and the pi-3 module `pi-3-my/my3_formulas.py` show how the final strings are produced: import or copy them READ-ONLY (never edit anything in pi-1-my/, pi-2-my/ or pi-3-my/), so identical Pāli gets identical Burmese. Where the zero-shot module and the rails differ, the RAILS text wins.
- Method model (formula module + generator): `pi-3-my/make_sample.py`, `pi-3-my/check_sample.py`, `pi-2-my/make_sample.py`; the Marathi pi-4 run `0-INBOX/temp/pipeline/pi-4-mr/make_ch1.py`, `make_ch2.py`, `mr_formulas.py`, `notes-ch2-3-4-6.md` (method and frame inventory only, never Marathi words).
- Cross-check of MEANING only (never wording): the English pi-4 zero-shot `AI_translation/english/pi-4-english-plain-zeroshot_split_chapters/<same file>` and the Marathi pi-4 rails `AI_translation/marathi/pi-4-marathi-plain-rails_split_chapters/<same file>`.

## About the text
The Puggalapaññatti («Designation of Persons») opens with a mātikā: the six designations (khandha, āyatana, dhātu, sacca, indriya, puggala paññatti, each «Kittāvatā … ? Yāvatā … ettāvatā …»), then the lists of person types by ones, twos, … tens. The exposition (niddesa) defines each type in a fixed frame: «Katamo ca puggalo X? Idhekacco puggalo … – ayaṃ vuccati puggalo "X".», often with similes (the four ponds, the four mangoes, the four bulls …) and lists of virtues and faults. Everything turns on: the frames (identical Burmese each time); the person-type names (plain Burmese, one name per type, the same in mātikā, heading and definition); the polarity and the many near-identical paired definitions (X / a-X, sappurisa / asappurisa); the numbers; the terms reused from pi-1 / pi-2 / pi-3 (vimokkha, āsava, jhāna, sīla, the eight attainments, path and fruit, sotāpanna … arahant); similes as plain, natural Burmese.

## Your output
1. `AI_translation/burmese/pi-4-burmese-plain-zeroshot_split_chapters/preamble.md` (Pāli `AI_translation/pali/pi-4_split_chapters/preamble.md`; same frame as the pi-1 / pi-2 preambles).
2. The WHOLE of `1-matika.md` and `2-ekakapuggalapannatti.md`, same filenames in that folder (save part by part).
3. `pi-4-my/my4_formulas.py`: the shared pi-4 module later agents import (the person-type name table for ALL types in the mātikā, ones to tens; the definition frame and its variants; the six designations; reused topic names; number words; headings and colophons).
4. `pi-4-my/make_sample.py` (imports my4_formulas.py, writes the three files; frames and tables for the repeated parts; hand-written strings for the unique prose kept in a table in the script; stops on any unmatched sentence).
5. `pi-4-my/my4-zeroshot-terms.md`: every formula and term as «Pāli = Burmese», grouped: the proposed Burmese book title for the Puggalapaññatti (plain, Burmese only), the chapter headings (Ekaka … Dasaka puggalapaññatti), the definition frame and EVERY person-type name of the mātikā.
6. `pi-4-my/check_sample.py`: per-line check (numbers, negations / polarity, the person-type name the same in mātikā, heading and definition, table values, 0 mismatches) plus a **pi-1 / pi-2 / pi-3 reuse test**: every topic name, term and Pāli sentence of the sample that also occurs in pi-1, pi-2 or pi-3 must have exactly their final Burmese (report n / n identical).
7. `pi-4-my/notes-sample.md`: choices, unsure Pāli, source slips.

## Rules
- Identical Pāli = identical Burmese (within pi-4 and with pi-1 / pi-2 / pi-3 final). Each Pāli synonym its own Burmese.
- Polarity and numbers exact; check by script. Headings keep their #-level. Block IDs exact, one blank line between segments, the source's number of non-empty lines per segment, no double blank lines.
- «…pe…» / «…Pe…» become one «…». DASH RULE: «–» only where the Pāli line has one, same spot and count. No «।», no «:-», no «?»: questions end with their question particle (လော / နည်း) and «။». Statements end with «။».
- Digits as the Pāli, e.g. «(1)». Variant brackets as pi-1: «[ပါဌ်ကွဲ (Syā.): …]», «[စာလုံးပေါင်းကွဲ (…): …]».
- Natural plain Burmese; nothing added. Book title in Burmese only. Source slips: translate as written, flag in notes.

## Verify every file (all must pass)
```
/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 0-INBOX/temp/pipeline/check_chapter_ids.py AI_translation/pali/pi-4_split_chapters AI_translation/burmese/pi-4-burmese-plain-zeroshot_split_chapters <ch>.md
/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 0-INBOX/temp/pipeline/pi-6-mr/check_text_pe.py AI_translation/pali/pi-4_split_chapters/<ch>.md AI_translation/burmese/pi-4-burmese-plain-zeroshot_split_chapters/<ch>.md
/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 0-INBOX/temp/pipeline/pi-4-mr/check_marks.py AI_translation/pali/pi-4_split_chapters/<ch>.md AI_translation/burmese/pi-4-burmese-plain-zeroshot_split_chapters/<ch>.md
```
All must print OK (delete your chk-pe copies in `pi-6-mr/chk-pe/` afterwards). Plus your own check: 0 mismatches, and the reuse test n / n.

## Final report (short)
Checks per file, segment counts, your check result, the reuse test, the main choices (book title, chapter headings, the frame, the person-type names, what was reused from pi-1 / pi-2 / pi-3, new terms), unsure Pāli and source slips.

## Approval
The user has given a standing go-ahead (2026-11-19): the coordinator reviews and approves the sample; still stop after the sample and report.
