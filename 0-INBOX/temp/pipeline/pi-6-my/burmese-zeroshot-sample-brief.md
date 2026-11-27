# Brief: Burmese zero-shot SAMPLE for pi-6 (Yamaka)

Work in /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails on macOS (zsh). Use the Read/Write tools for files and call Python as `/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8` (the system python3 is too old). Write helper scripts to files rather than inline `-c` with regexes. Scratch, scripts and notes only in `0-INBOX/temp/pipeline/pi-6-my/`. Never use the system temp directory (not /tmp, not /private/tmp, no `cd /tmp`). Do not commit. Never use the words for a planted starting value or its negative; say "sample" or "model".

You write the model that later agents copy for the rest of the book (45 files, 1.9 MB of Pāli), so the shared pieces (formula module, term list) matter as much as the text. Write part by part and save as soon as each passes: you may be paused for usage limits and resumed later. Keep your notes current. Stop after the sample: the user reviews it.

## Source rule (binding, user 2026-11-16/17)
Translate FROM THE PĀLI only. Never look up, open or copy any existing Burmese translation or nissaya (never open `0-INBOX/temp/language-priority/`), and do no web searches.

## Read first
- `0-INBOX/temp/pipeline/burmese-style.md`: binding rules, typography, the dash rule, the approved core terms and the locked pi-1 and pi-2 termbase sections.
- `AI_translation/skills/zeroshot-translator.md` and `AI_translation/audience_profile/plain.md`.
- **pi-1 … pi-5 Burmese are binding** wherever the Yamaka uses their terms, lists and sentences (khandha / āyatana / dhātu / indriya names, the Mātikā triads and dyads, path and fruit, the anusayas, the 22 faculties, the truths, saṅkhāra, citta, the realms (kāma / rūpa / arūpa, asaññasatta), the person types, path and fruit; and the question–answer style of pi-3 Dhātukathā and pi-5 Kathāvatthu: Āmantā «ဟုတ်ပါသည်။» etc.): use the FINAL Burmese, i.e. the rails texts `AI_translation/burmese/pi-{1,2,3,4,5}-burmese-plain-rails_split_chapters/` and the locked termbases `AI_translation/burmese/pi-{1,2,3,4,5}-pali-burmese-termbase-plain.md` (see their `pi-N-my/termbase/APPROVED.md`). The pi-2 module `0-INBOX/temp/pipeline/pi-2-my/my2_formulas.py` and its rails layer `pi-2-my/rails/my_formulas_rails.py` + `rails/build_rails.py` (and pi-1's `pi-1-my/my_formulas.py`, `pi-1-my/rails/`) and the pi-3 / pi-4 / pi-5 modules `pi-3-my/my3_formulas.py`, `pi-4-my/my4_formulas.py`, `pi-5-my/my5_formulas.py` (+ its rails layer `pi-5-my/rails/`) show how the final strings are produced: import or copy them READ-ONLY (never edit anything in pi-1-my/ … pi-5-my/), so identical Pāli gets identical Burmese. Where the zero-shot module and the rails differ, the RAILS text wins.
- Method model (formula module + generator): `pi-5-my/make_sample.py`, `pi-5-my/check_sample.py`, `pi-3-my/make_sample.py`; the Marathi pi-6 run `0-INBOX/temp/pipeline/pi-6-mr/make_ch1-2-01_sample.py`, `mr_formulas.py` and its notes (method and frame inventory only, never Marathi words).
- Cross-check of MEANING only (never wording): the English pi-6 rails `AI_translation/english/pi-6-english-plain-rails_split_chapters/<same file>` and the Marathi pi-6 rails `AI_translation/marathi/pi-6-marathi-plain-rails_split_chapters/<same file>`.

## About the text
The Yamaka («Pairs») tests the scope of the Abhidhamma terms by paired questions in ten chapters (mūla, khandha, āyatana, dhātu, sacca, saṅkhāra, anusaya, citta, dhamma, indriya). Each chapter has fixed sections (vāras): paṇṇattivāra (uddesa / niddesa; padasodhana «(Ka) rūpaṃ rūpakkhandho? (Kha) rūpakkhandho rūpaṃ?», padasodhanamūlacakka, suddhakhandha …), pavattivāra (uppāda / nirodha / uppādanirodha, for persons «yassa …», places «yattha …», persons-and-places «yassa yattha …», in the three times and their combinations, anuloma and paccanīka), pariññāvāra. Each question has a fixed answer form: «Āmantā.», «No.», a partial answer «X Y ca, … ; Y … X ca …» / «… atthi … ; … natthi …», or a split answer per person / place type («Pañcavokāre … ; asaññasatte …; arūpe …»). Everything turns on: the question frames (each the same Burmese every time, as a script table; (Ka) / (Kha) pairs, anuloma / paccanīka); POLARITY in every clause (uppajjati / nuppajjati, nirujjhati / na nirujjhati, atthi / natthi, Āmantā / No: check by script); the three times (uppajjati / uppajjittha / uppajjissati, the -ittha / -issati forms and their combinations: one Burmese tense form each, exact); the person / place types (pañcavokāra, catuvokāra, ekavokāra, asaññasatta, arūpa, suddhāvāsa, those reborn / passing away, the eight persons …: one name each, from pi-1 … pi-5 where they exist); the term lists of each chapter (the 22 faculties in pi-1 / pi-2 order and Burmese).

## Your output
1. `AI_translation/burmese/pi-6-burmese-plain-zeroshot_split_chapters/preamble.md` (Pāli `AI_translation/pali/pi-6_split_chapters/preamble.md`; same frame as the earlier preambles).
2. The WHOLE of `1-mulayamaka.md` (26 KB) and `2-01-khandhayamaka.md` (59 KB), same filenames in that folder (save part by part).
3. `pi-6-my/my6_formulas.py`: the shared pi-6 module later agents import (every question frame as a function of its terms, in all tenses and polarities; the answer words and partial-answer frames; the person / place types; vāra and section headings; chapter names and colophons; the term lists; reused terms).
4. `pi-6-my/make_sample.py` (imports my6_formulas.py, writes the three files; frames and tables for the repeated parts; hand-written strings only for unique lines, in a table in the script; stops on any unmatched sentence).
5. `pi-6-my/my6-zeroshot-terms.md`: every formula and term as «Pāli = Burmese», grouped: the proposed Burmese book title for the Yamaka (plain, Burmese only), chapter / vāra heading patterns, all question and answer frames by tense and polarity, the person / place types, the term lists.
6. `pi-6-my/check_sample.py`: per-line check (polarity per clause; the tense of every verb; (Ka) / (Kha) pairs; numbers; every recurring question the same Burmese; table values, 0 mismatches) plus a **pi-1 … pi-5 reuse test**: every term and Pāli sentence of the sample that also occurs in pi-1 … pi-5 must have exactly their final Burmese (report n / n identical).
7. `pi-6-my/notes-sample.md`: choices, unsure Pāli, source slips.

## Rules
- Identical Pāli = identical Burmese (within pi-6 and with pi-1 … pi-5 final). Each Pāli synonym its own Burmese.
- Polarity and numbers exact; check by script. Headings keep their #-level. Block IDs exact, one blank line between segments, the source's number of non-empty lines per segment, no double blank lines.
- «…pe…» / «…Pe…» become one «…». DASH RULE: «–» only where the Pāli line has one, same spot and count. No «।», no «:-», no «?»: questions end with their question particle (လော / နည်း) and «။». Statements end with «။».
- Digits as the Pāli, e.g. «(1)». Variant brackets as pi-1: «[ပါဌ်ကွဲ (Syā.): …]», «[စာလုံးပေါင်းကွဲ (…): …]».
- Natural plain Burmese; nothing added. Book title in Burmese only. Source slips: translate as written, flag in notes.

## Verify every file (all must pass)
```
/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 0-INBOX/temp/pipeline/check_chapter_ids.py AI_translation/pali/pi-6_split_chapters AI_translation/burmese/pi-6-burmese-plain-zeroshot_split_chapters <ch>.md
/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 0-INBOX/temp/pipeline/pi-6-mr/check_text_pe.py AI_translation/pali/pi-6_split_chapters/<ch>.md AI_translation/burmese/pi-6-burmese-plain-zeroshot_split_chapters/<ch>.md
/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 0-INBOX/temp/pipeline/pi-4-mr/check_marks.py AI_translation/pali/pi-6_split_chapters/<ch>.md AI_translation/burmese/pi-6-burmese-plain-zeroshot_split_chapters/<ch>.md
```
All must print OK (delete your chk-pe copies in `pi-6-mr/chk-pe/` afterwards). Plus your own check: 0 mismatches, and the reuse test n / n.

## Final report (short)
Checks per file, segment counts, your check result, the reuse test, the main choices (book title, headings, the question and answer frames, what was reused from pi-1 … pi-5, new terms), unsure Pāli and source slips.

## Approval
The user has given a standing go-ahead (2026-11-19): the coordinator reviews and approves the sample; still stop after the sample and report.
