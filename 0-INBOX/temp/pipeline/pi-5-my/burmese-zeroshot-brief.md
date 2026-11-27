# Brief: Burmese zero-shot, remaining chapters (pi-5, Kathāvatthu «အငြင်းပွားရာ အကြောင်းအရာများကို ဆွေးနွေးခြင်း»)

Work in /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails on macOS (zsh). Python: `/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8` (scripts in files). Other agents translate other chapters in parallel. Write ONLY your own chapter files, plus your generator, check and notes named after your chapters, inside `0-INBOX/temp/pipeline/pi-5-my/`. Never use the system temp directory. Do not commit. Never use the words for a planted starting value or its negative.

You may be paused for usage limits and resumed later: generate chapter by chapter, save each chapter as soon as it passes, keep your notes current.

## Source rule (binding)
Translate FROM THE PĀLI only. Never open or copy any existing Burmese translation or nissaya (never open `0-INBOX/temp/language-priority/`); no web searches.

## Read first
- `0-INBOX/temp/pipeline/burmese-style.md` (binding; incl. the locked pi-1 … pi-4 termbase sections).
- `AI_translation/skills/zeroshot-translator.md`, `AI_translation/audience_profile/plain.md`.
- **The approved pi-5 sample (coordinator under the user's standing go-ahead, 2026-11-20), READ-ONLY, the model for everything:** `pi-5-my/my5_formulas.py` (import it; extend its tables in memory in YOUR script; never edit it; log every new string in your notes), `pi-5-my/make_sample.py` (copy functions; never run it: it rewrites shared files), `check_sample.py` (adapt as `check_<your chapters>.py`, incl. its polarity, quote-nesting, recurring-sentence and reuse tests), `my5-zeroshot-terms.md` (copy its strings verbatim: every dialectic formula, the answers «ဟုတ်ပါသည်။» / «ဤသို့ မဆိုသင့်ပါ။», vattabba «ဆိုသင့်» / «မဆိုသင့်», the set names, sakavādī / paravādī «မိမိဘက်» / «တစ်ဖက်သား», kathā «ဆွေးနွေးချက်», vagga «ဝဂ်», anuyoga, saṃsandana, colophons), `notes-sample.md`, and the outputs `AI_translation/burmese/pi-5-burmese-plain-zeroshot_split_chapters/preamble.md`, `1-puggalakatha.md`. Approved: title «အငြင်းပွားရာ အကြောင်းအရာများကို ဆွေးနွေးခြင်း», the frames and the regular quote nesting (“…” outer, ‘…’ inner).
- **pi-1 … pi-4 final Burmese are binding for identical Pāli** (topic names, Mātikā terms, person types, path and fruit, jhāna, kilesa, sīla, realms, sutta passages already translated): the rails texts `AI_translation/burmese/pi-{1,2,3,4}-burmese-plain-rails_split_chapters/`, the locked termbases `AI_translation/burmese/pi-{1,2,3,4}-pali-burmese-termbase-plain.md`, read the way the sample's module does. Never edit anything in `pi-1-my/` … `pi-5-my/`.
- Cross-check of MEANING only (never wording): the English pi-5 zero-shot `AI_translation/english/pi-5-english-plain-zeroshot_split_chapters/<same file>` and the Marathi pi-5 rails `AI_translation/marathi/pi-5-marathi-plain-rails_split_chapters/<same file>`; method model for the frames: `0-INBOX/temp/pipeline/pi-5-mr/make_<chapters>.py`, `notes-<chapters>.md` (frame inventory only, never Marathi words).

## About the text
Each kathā repeats the sample's dialectic formulas with new propositions (and new sutta quotations). Build each proposition once as a Burmese building block and fill the formulas from it, so the same proposition is the same Burmese in every formula; every polarity (upalabbhati / nupalabbhati, vattabbe / no ca vattabbe, Āmantā / Na hevaṃ, na / no / a- inside propositions) must match the Pāli exactly (checked by script); sutta quotations in plain Burmese, the same where they repeat.

## Source and output
- Source `AI_translation/pali/pi-5_split_chapters/<ch>.md`; output `AI_translation/burmese/pi-5-burmese-plain-zeroshot_split_chapters/<ch>.md`; generator `pi-5-my/make_<chapters>.py`; check `pi-5-my/check_<chapters>.py`; notes `pi-5-my/notes-<chapters>.md`.

## Rules
- Identical Pāli = identical Burmese (within pi-5, with the sample, and with pi-1 … pi-4 final). GENERATE every chapter by script: frames and tables for repeated parts, hand-written strings for unique prose kept in a table in the script (as the sample).
- Polarity and numbers exact (checked by script). Headings keep their #-level. Block IDs exact; the source's number of non-empty lines per segment; one blank line between segments; no double blank lines.
- A NEW recurring term or phrase: record it in your notes («Pāli = Burmese», one per line). Do not edit my5_formulas.py or my5-zeroshot-terms.md. A consistency pass aligns all agents afterwards.
- «…pe…» / «…Pe…» become one «…». DASH RULE: «–» only where the Pāli line has one, same spot and count. No «।», «:-», «?»: questions end with their particle (လော / နည်း) and «။». Statements end with «။». Digits as the Pāli. Variant brackets as the sample. Source slips: translate as written, log them.

## Verify every chapter (all must pass before you report)
```
/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 0-INBOX/temp/pipeline/check_chapter_ids.py AI_translation/pali/pi-5_split_chapters AI_translation/burmese/pi-5-burmese-plain-zeroshot_split_chapters <ch>.md
/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 0-INBOX/temp/pipeline/pi-6-mr/check_text_pe.py AI_translation/pali/pi-5_split_chapters/<ch>.md AI_translation/burmese/pi-5-burmese-plain-zeroshot_split_chapters/<ch>.md
/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 0-INBOX/temp/pipeline/pi-4-mr/check_marks.py AI_translation/pali/pi-5_split_chapters/<ch>.md AI_translation/burmese/pi-5-burmese-plain-zeroshot_split_chapters/<ch>.md
```
All must print OK (delete your chk-pe copies afterwards). Plus your own check: 0 mismatches, and the reuse test n / n.

## Final report (short)
Per chapter: checks, segment count, own check, reuse n / n; key new terms and frames (or point to your notes); unsure Pāli and source slips.

Never use /private/tmp or /tmp (no `cd /tmp` either). You may be paused for usage limits: save chapter by chapter.
