# Brief: Burmese zero-shot, remaining chapters (pi-2, Vibhaṅga «ခွဲခြမ်းစိတ်ဖြာခြင်း»)

Work in /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails on macOS (zsh). Python: `/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8` (scripts in files). Other agents translate other chapters in parallel. Write ONLY your own chapter files, plus your generator, check and notes named after your chapters, inside `0-INBOX/temp/pipeline/pi-2-my/`. Never use the system temp directory. Do not commit. Never use the words for a planted starting value or its negative.

You may be paused for usage limits and resumed later: generate chapter by chapter, save each chapter as soon as it passes, keep your notes current.

## Source rule (binding)
Translate FROM THE PĀLI only. Never open or copy any existing Burmese translation or nissaya (never open `0-INBOX/temp/language-priority/`); no web searches.

## Read first
- `0-INBOX/temp/pipeline/burmese-style.md` (binding; incl. the locked pi-1 termbase section).
- `AI_translation/skills/zeroshot-translator.md`, `AI_translation/audience_profile/plain.md`.
- **The approved pi-2 sample (user, 2026-11-17), READ-ONLY, the model for everything:** `pi-2-my/my2_formulas.py` (import it; extend its tables in memory in YOUR script; never edit it; log every new string in your notes), `pi-2-my/make_sample.py` (copy functions; never run it: it rewrites shared files), `check_sample.py` (adapt as `check_<your chapters>.py`, including its pi-1 reuse test), `my2-zeroshot-terms.md` (copy its strings verbatim), `notes-sample.md`, and the output `AI_translation/burmese/pi-2-burmese-plain-zeroshot_split_chapters/preamble.md` and `1-khandhavibhango.md`. Approved: title «ခွဲခြမ်းစိတ်ဖြာခြင်း», chapter titles «X ကို ခွဲခြမ်းစိတ်ဖြာခြင်း», parts «သုတ္တန်အလိုက် ခွဲခြမ်း ဖော်ပြချက်» / «အဘိဓမ္မာအလိုက် ခွဲခြမ်း ဖော်ပြချက်» / «မေးခွန်းများဖြင့် ဖော်ပြချက်», the eleven qualifiers, the frames.
- **pi-1 final Burmese is binding for identical Pāli** (Dhammasaṅgaṇī definitions, synonym lists, Mātikā items, factor names, matter, jhāna and path formulas, the cittuppāda openings): the rails text `AI_translation/burmese/pi-1-burmese-plain-rails_split_chapters/`, the locked termbase `AI_translation/burmese/pi-1-pali-burmese-termbase-plain.md`, and (read-only) `pi-1-my/my_formulas.py` with its rails layer `pi-1-my/rails/my_formulas_rails.py` as the sample does. Never edit anything in `pi-1-my/`.
- Cross-check of MEANING only (never wording): the English pi-2 rails `AI_translation/english/pi-2-english-plain-rails_split_chapters/<same file>` and the Marathi pi-2 rails `AI_translation/marathi/pi-2-marathi-plain-rails_split_chapters/<same file>`.

## Source and output
- Source `AI_translation/pali/pi-2_split_chapters/<ch>.md`; output `AI_translation/burmese/pi-2-burmese-plain-zeroshot_split_chapters/<ch>.md`; generator `pi-2-my/make_<chapters>.py`; check `pi-2-my/check_<chapters>.py`; notes `pi-2-my/notes-<chapters>.md`.

## Rules
- Identical Pāli = identical Burmese (within pi-2, with the sample, and with pi-1 final). GENERATE every chapter by script from frames and tables.
- Synonym lists: each Pāli synonym its own Burmese, order and count kept; same as the sample / pi-1 table where it has one; no two synonyms of one list share a word unless the Pāli repeats it. New synonyms: a plain word distinct from existing values, logged.
- Polarity and numbers exact (checked by script). Headings keep their #-level. Block IDs exact; the source's number of non-empty lines per segment; one blank line between segments; no double blank lines.
- A NEW recurring term or phrase: record it in your notes («Pāli = Burmese», one per line). Do not edit my2_formulas.py or my2-zeroshot-terms.md. A consistency pass aligns all agents afterwards.
- «…pe…» / «…Pe…» become one «…». DASH RULE: «–» only where the Pāli line has one, same spot and count. No «।», «:-», «?». Statements end with «။». Variant brackets as the sample. Source slips: translate as written, log them.

## Verify every chapter (all must pass before you report)
```
/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 0-INBOX/temp/pipeline/check_chapter_ids.py AI_translation/pali/pi-2_split_chapters AI_translation/burmese/pi-2-burmese-plain-zeroshot_split_chapters <ch>.md
/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 0-INBOX/temp/pipeline/pi-6-mr/check_text_pe.py AI_translation/pali/pi-2_split_chapters/<ch>.md AI_translation/burmese/pi-2-burmese-plain-zeroshot_split_chapters/<ch>.md
/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 0-INBOX/temp/pipeline/pi-4-mr/check_marks.py AI_translation/pali/pi-2_split_chapters/<ch>.md AI_translation/burmese/pi-2-burmese-plain-zeroshot_split_chapters/<ch>.md
```
All must print OK (delete your chk-pe copies afterwards). Plus your own check: 0 mismatches, and the pi-1 reuse test n / n.

## Final report (short)
Per chapter: checks, segment count, own check, pi-1 reuse n / n; key new terms (or point to your notes); unsure Pāli and source slips.
