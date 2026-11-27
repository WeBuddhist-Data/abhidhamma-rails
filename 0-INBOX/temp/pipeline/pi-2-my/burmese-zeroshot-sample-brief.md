# Brief: Burmese zero-shot SAMPLE for pi-2 (Vibhaṅga)

Work in /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails on macOS (zsh). Use the Read/Write tools for files and call Python as `/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8` (the system python3 is too old). Write helper scripts to files rather than inline `-c` with regexes. Scratch, scripts and notes only in `0-INBOX/temp/pipeline/pi-2-my/`. Never use the system temp directory. Do not commit. Never use the words for a planted starting value or its negative; say "sample" or "model".

You write the model that later agents copy for the rest of the book (20 files, 900 KB of Pāli), so the shared pieces (formula module, term list) matter as much as the text. Write part by part and save as soon as each passes: you may be paused for usage limits and resumed later. Keep your notes current. Stop after the sample: the user reviews it.

## Source rule (binding, user 2026-11-16/17)
Translate FROM THE PĀLI only. Never look up, open or copy any existing Burmese translation or nissaya (never open `0-INBOX/temp/language-priority/`), and do no web searches.

## Read first
- `0-INBOX/temp/pipeline/burmese-style.md`: binding rules, typography, the dash rule, the approved core terms and the locked pi-1 termbase section.
- `AI_translation/skills/zeroshot-translator.md` and `AI_translation/audience_profile/plain.md`.
- **pi-1 Burmese is binding wherever the Vibhaṅga repeats the Dhammasaṅgaṇī** (the abhidhammabhājanīya quotes its definitions and synonym lists word for word; the pañhāpucchaka applies its Mātikā triads / dyads): use the FINAL pi-1 Burmese, i.e. the rails text `AI_translation/burmese/pi-1-burmese-plain-rails_split_chapters/` and the locked termbase `AI_translation/burmese/pi-1-pali-burmese-termbase-plain.md` (see `0-INBOX/temp/pipeline/pi-1-my/termbase/APPROVED.md`: uppanna «ဖြစ်ပေါ်ပြီးသော», the definition frame «ထိုအချိန်၌ A၊ B … ရှိသမျှ –», bahiddhā «မိမိ၏ ပြင်ပ၌», nāma-rūpa «စိတ်ပိုင်း / ရုပ်ပိုင်း», proper names stay names …). The pi-1 module `0-INBOX/temp/pipeline/pi-1-my/my_formulas.py` and its rails layer `pi-1-my/rails/my_formulas_rails.py` + `rails/build_rails.py` show how the final strings are produced: import or copy them READ-ONLY (never edit anything in pi-1-my/), so identical Pāli gets identical Burmese.
- Method model (formula module + generator): `pi-1-my/make_sample.py`, `make_ch2-01.py`, `check_ch2-01.py`; the Marathi pi-2 sample `0-INBOX/temp/pipeline/pi-2-mr/make_sample.py`, `mr_formulas.py`, `notes-sample.md` (method and frame inventory only, never Marathi words).
- Cross-check of MEANING only (never wording): the English pi-2 rails `AI_translation/english/pi-2-english-plain-rails_split_chapters/<same file>` and the Marathi pi-2 rails `AI_translation/marathi/pi-2-marathi-plain-rails_split_chapters/<same file>`.

## About the text
The Vibhaṅga analyses one topic per chapter (khandha, āyatana, dhātu, sacca, indriya, paṭiccasamuppāda, satipaṭṭhāna, sammappadhāna, iddhipāda, bojjhaṅga, maggaṅga, jhāna, appamaññā, sikkhāpada, paṭisambhidā, ñāṇa, khuddakavatthu, dhammahadaya). Most chapters have three parts: suttantabhājanīya, abhidhammabhājanīya (quoting the Dhammasaṅgaṇī) and pañhāpucchaka (the Mātikā triads / dyads applied to the topic). The khandha chapter opens «Pañcakkhandhā – rūpakkhandho, vedanākkhandho, …» and analyses each aggregate with the eleven qualifiers («Yaṃ kiñci rūpaṃ atītānāgatapaccuppannaṃ ajjhattaṃ vā bahiddhā vā oḷārikaṃ vā sukhumaṃ vā hīnaṃ vā paṇītaṃ vā yaṃ dūre santike vā …»).
Everything turns on: the synonym lists and definitions (same Pāli = pi-1's final Burmese); the eleven qualifiers and their own definitions; the Mātikā terms in the pañhāpucchaka; polarity and numbers.

## Your output
1. `AI_translation/burmese/pi-2-burmese-plain-zeroshot_split_chapters/preamble.md` (Pāli `AI_translation/pali/pi-2_split_chapters/preamble.md`; same frame as the pi-1 preamble).
2. The WHOLE of `1-khandhavibhango.md` (all three parts), same filename in that folder (129 KB: save part by part).
3. `pi-2-my/my2_formulas.py`: the shared pi-2 module later agents import (khandha / āyatana / dhātu … names; the synonym table, pi-1 entries reused, new ones added; the frames of the three parts; the eleven qualifiers; the Mātikā tables from pi-1 final; number words; headings «Suttantabhājanīyaṃ», «Abhidhammabhājanīyaṃ», «Pañhāpucchakaṃ» …).
4. `pi-2-my/make_sample.py` (imports my2_formulas.py, writes both files; every segment from frames and tables; stops on any unmatched sentence).
5. `pi-2-my/my2-zeroshot-terms.md`: every formula and term as «Pāli = Burmese», grouped. This is what the user reviews. Include the proposed Burmese book title for the Vibhaṅga (plain, Burmese only) and the three part headings.
6. `pi-2-my/check_sample.py`: per-line check (numbers, negations, synonym counts, table values, 0 mismatches) plus a **pi-1 reuse test**: every Pāli sentence of the sample that also occurs in pi-1 must have exactly pi-1's final Burmese (report n / n identical).
7. `pi-2-my/notes-sample.md`: choices, unsure Pāli, source slips.

## Rules
- Identical Pāli = identical Burmese (within pi-2 and with pi-1 final). Each Pāli synonym its own Burmese; no two synonyms of one list share a word unless the Pāli repeats it.
- Polarity and numbers exact; check by script. Headings keep their #-level. Block IDs exact, one blank line between segments, the source's number of non-empty lines per segment, no double blank lines.
- «…pe…» / «…Pe…» become one «…». DASH RULE: «–» only where the Pāli line has one, same spot and count. No «।», no «:-», no «?». Statements end with «။».
- Variant brackets as pi-1: «[ပါဌ်ကွဲ (Syā.): …]», «[စာလုံးပေါင်းကွဲ (…): …]».
- Natural plain Burmese; nothing added. Book title in Burmese only. Source slips: translate as written, flag in notes.

## Verify every file (all must pass)
```
/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 0-INBOX/temp/pipeline/check_chapter_ids.py AI_translation/pali/pi-2_split_chapters AI_translation/burmese/pi-2-burmese-plain-zeroshot_split_chapters <ch>.md
/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 0-INBOX/temp/pipeline/pi-6-mr/check_text_pe.py AI_translation/pali/pi-2_split_chapters/<ch>.md AI_translation/burmese/pi-2-burmese-plain-zeroshot_split_chapters/<ch>.md
/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 0-INBOX/temp/pipeline/pi-4-mr/check_marks.py AI_translation/pali/pi-2_split_chapters/<ch>.md AI_translation/burmese/pi-2-burmese-plain-zeroshot_split_chapters/<ch>.md
```
All must print OK (delete your chk-pe copies in `pi-6-mr/chk-pe/` afterwards). Plus your own check: 0 mismatches, and the pi-1 reuse test n / n.

## Final report (short)
Checks per file, segment counts, your check result, the pi-1 reuse test, the main choices (book title, the three part headings, the eleven qualifiers, the frames, what was reused from pi-1, new terms), unsure Pāli and source slips.
