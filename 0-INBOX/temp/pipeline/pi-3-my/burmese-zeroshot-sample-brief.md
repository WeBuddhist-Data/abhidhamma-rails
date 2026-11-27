# Brief: Burmese zero-shot SAMPLE for pi-3 (Dhātukathā)

Work in /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails on macOS (zsh). Use the Read/Write tools for files and call Python as `/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8` (the system python3 is too old). Write helper scripts to files rather than inline `-c` with regexes. Scratch, scripts and notes only in `0-INBOX/temp/pipeline/pi-3-my/`. Never use the system temp directory. Do not commit. Never use the words for a planted starting value or its negative; say "sample" or "model".

You write the model that later agents copy for the rest of the book (16 files, 175 KB of Pāli), so the shared pieces (formula module, term list) matter as much as the text. Write part by part and save as soon as each passes: you may be paused for usage limits and resumed later. Keep your notes current. Stop after the sample: the user reviews it.

## Source rule (binding, user 2026-11-16/17)
Translate FROM THE PĀLI only. Never look up, open or copy any existing Burmese translation or nissaya (never open `0-INBOX/temp/language-priority/`), and do no web searches.

## Read first
- `0-INBOX/temp/pipeline/burmese-style.md`: binding rules, typography, the dash rule, the approved core terms and the locked pi-1 and pi-2 termbase sections.
- `AI_translation/skills/zeroshot-translator.md` and `AI_translation/audience_profile/plain.md`.
- **pi-1 and pi-2 Burmese are binding** wherever the Dhātukathā uses their terms and lists (the Abbhantaramātikā lists the Vibhaṅga topics: khandha, āyatana, dhātu, sacca, indriya, paṭiccasamuppāda, satipaṭṭhāna …; the Bāhiramātikā takes the whole Dhammasaṅgaṇī Mātikā): use the FINAL Burmese, i.e. the rails texts `AI_translation/burmese/pi-1-burmese-plain-rails_split_chapters/`, `AI_translation/burmese/pi-2-burmese-plain-rails_split_chapters/` and the locked termbases `AI_translation/burmese/pi-1-pali-burmese-termbase-plain.md`, `pi-2-pali-burmese-termbase-plain.md` (see `pi-1-my/termbase/APPROVED.md`, `pi-2-my/termbase/APPROVED.md`). The pi-2 module `0-INBOX/temp/pipeline/pi-2-my/my2_formulas.py` and its rails layer `pi-2-my/rails/my_formulas_rails.py` + `rails/build_rails.py` (and pi-1's `pi-1-my/my_formulas.py`, `pi-1-my/rails/`) show how the final strings are produced: import or copy them READ-ONLY (never edit anything in pi-1-my/ or pi-2-my/), so identical Pāli gets identical Burmese. Where the zero-shot module and the rails differ, the RAILS text wins.
- Method model (formula module + generator): `pi-2-my/make_sample.py`, `pi-2-my/check_sample.py`; the Marathi pi-3 run `0-INBOX/temp/pipeline/pi-3-mr/make_ch2.py`, `mr_formulas.py`, `notes-ch2.md` (method and frame inventory only, never Marathi words).
- Cross-check of MEANING only (never wording): the English pi-3 zero-shot `AI_translation/english/pi-3-english-plain-zeroshot_split_chapters/<same file>` and the Marathi pi-3 rails `AI_translation/marathi/pi-3-marathi-plain-rails_split_chapters/<same file>`.

## About the text
The Dhātukathā («Discourse on elements») classifies phenomena by inclusion (saṅgaha) and association (sampayoga) with the aggregates, bases and elements. It opens with the mātikās (Nayamātikā of 14 methods, Abbhantaramātikā of the topics, Nayamukhamātikā, Lakkhaṇamātikā, Bāhiramātikā), then the 14 methods (naya). Each item is a fixed question-and-answer frame, e.g. «Rūpakkhandho katihi khandhehi katihāyatanehi katihi dhātūhi saṅgahito? Rūpakkhandho ekena khandhena ekādasahāyatanehi ekādasahi dhātūhi saṅgahito. Katihi asaṅgahito? Catūhi khandhehi ekenāyatanena sattahi dhātūhi asaṅgahito.», with colophons «(Ekamūlakaṃ.)», «(Dukamūlakaṃ.)» … Everything turns on: the frames (each naya's question and answer, exactly the same Burmese each time); the NUMBERS (instrumental number words «ekena, dvīhi, catūhi, ekādasahi, sattarasahi …» → Burmese numbers; every count exact, check by script); saṅgahita / asaṅgahita and sampayutta / vippayutta polarity; the topic names (pi-1 / pi-2 final); the Mātikā terms.

## Your output
1. `AI_translation/burmese/pi-3-burmese-plain-zeroshot_split_chapters/preamble.md` (Pāli `AI_translation/pali/pi-3_split_chapters/preamble.md`; same frame as the pi-1 / pi-2 preambles).
2. The WHOLE of `1-uddeso.md` and `2-pathamanayo.md`, same filenames in that folder (save part by part).
3. `pi-3-my/my3_formulas.py`: the shared pi-3 module later agents import (topic names from pi-1 / pi-2 final; the frames of each naya so far; number words in the instrumental; naya names and headings; colophons; the Mātikā tables).
4. `pi-3-my/make_sample.py` (imports my3_formulas.py, writes the three files; every segment from frames and tables; stops on any unmatched sentence).
5. `pi-3-my/my3-zeroshot-terms.md`: every formula and term as «Pāli = Burmese», grouped. This is what the user reviews. Include the proposed Burmese book title for the Dhātukathā (plain, Burmese only), the five mātikā names, the 14 naya names and the frames.
6. `pi-3-my/check_sample.py`: per-line check (every number of every answer against the Pāli, saṅgahita / asaṅgahita and polarity, table values, 0 mismatches) plus a **pi-1 / pi-2 reuse test**: every topic name, mātikā term and Pāli sentence of the sample that also occurs in pi-1 or pi-2 must have exactly their final Burmese (report n / n identical).
7. `pi-3-my/notes-sample.md`: choices, unsure Pāli, source slips.

## Rules
- Identical Pāli = identical Burmese (within pi-3 and with pi-1 / pi-2 final). Each Pāli synonym its own Burmese.
- Polarity and numbers exact; check by script. Headings keep their #-level. Block IDs exact, one blank line between segments, the source's number of non-empty lines per segment, no double blank lines.
- «…pe…» / «…Pe…» become one «…». DASH RULE: «–» only where the Pāli line has one, same spot and count. No «।», no «:-», no «?»: questions end with their question particle (လော / နည်း) and «။». Statements end with «။».
- Digits as the Pāli, e.g. «(1)». Variant brackets as pi-1: «[ပါဌ်ကွဲ (Syā.): …]», «[စာလုံးပေါင်းကွဲ (…): …]».
- Natural plain Burmese; nothing added. Book title in Burmese only. Source slips: translate as written, flag in notes.

## Verify every file (all must pass)
```
/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 0-INBOX/temp/pipeline/check_chapter_ids.py AI_translation/pali/pi-3_split_chapters AI_translation/burmese/pi-3-burmese-plain-zeroshot_split_chapters <ch>.md
/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 0-INBOX/temp/pipeline/pi-6-mr/check_text_pe.py AI_translation/pali/pi-3_split_chapters/<ch>.md AI_translation/burmese/pi-3-burmese-plain-zeroshot_split_chapters/<ch>.md
/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 0-INBOX/temp/pipeline/pi-4-mr/check_marks.py AI_translation/pali/pi-3_split_chapters/<ch>.md AI_translation/burmese/pi-3-burmese-plain-zeroshot_split_chapters/<ch>.md
```
All must print OK (delete your chk-pe copies in `pi-6-mr/chk-pe/` afterwards). Plus your own check: 0 mismatches, and the reuse test n / n.

## Final report (short)
Checks per file, segment counts, your check result, the reuse test, the main choices (book title, mātikā and naya names, the frames, number words, what was reused from pi-1 / pi-2, new terms), unsure Pāli and source slips.
