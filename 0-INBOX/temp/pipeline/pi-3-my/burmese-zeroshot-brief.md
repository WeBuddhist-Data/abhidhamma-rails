# Brief: Burmese zero-shot, remaining chapters (pi-3, Dhātukathā «ဓာတ်များအကြောင်း ဆွေးနွေးခြင်း»)

Work in /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails on macOS (zsh). Python: `/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8` (scripts in files). Other agents translate other chapters in parallel. Write ONLY your own chapter files, plus your generator, check and notes named after your chapters, inside `0-INBOX/temp/pipeline/pi-3-my/`. Never use the system temp directory. Do not commit. Never use the words for a planted starting value or its negative.

You may be paused for usage limits and resumed later: generate chapter by chapter, save each chapter as soon as it passes, keep your notes current.

## Source rule (binding)
Translate FROM THE PĀLI only. Never open or copy any existing Burmese translation or nissaya (never open `0-INBOX/temp/language-priority/`); no web searches.

## Read first
- `0-INBOX/temp/pipeline/burmese-style.md` (binding; incl. the locked pi-1 and pi-2 termbase sections).
- `AI_translation/skills/zeroshot-translator.md`, `AI_translation/audience_profile/plain.md`.
- **The approved pi-3 sample (user, 2026-11-18), READ-ONLY, the model for everything:** `pi-3-my/my3_formulas.py` (import it; extend its tables in memory in YOUR script; never edit it; log every new string in your notes), `pi-3-my/make_sample.py` (copy functions; never run it: it rewrites shared files), `check_sample.py` (adapt as `check_<your chapters>.py`, including its pi-1 / pi-2 reuse test and its per-count / polarity checks), `my3-zeroshot-terms.md` (copy its strings verbatim), `notes-sample.md`, and the output `AI_translation/burmese/pi-3-burmese-plain-zeroshot_split_chapters/preamble.md`, `1-uddeso.md`, `2-pathamanayo.md`. Approved: title «ဓာတ်များအကြောင်း ဆွေးနွေးခြင်း», the five mātikā names, the 14 naya names (Pāli ordinals «ပထမ … စုဒ္ဒသမ ခွဲနည်း»), saṅgaha / asaṅgaha «အကျုံးဝင်ခြင်း / အကျုံးမဝင်ခြင်း», sampayoga / vippayoga «ယှဉ်တွဲခြင်း / ကင်းကွာခြင်း», the question-and-answer frames, number words with «ပါး».
- **pi-1 and pi-2 final Burmese are binding for identical Pāli** (topic names, «X dhammā» Mātikā terms, the dependent-arising links, factor names): the rails texts `AI_translation/burmese/pi-1-burmese-plain-rails_split_chapters/`, `pi-2-burmese-plain-rails_split_chapters/`, the locked termbases `AI_translation/burmese/pi-1-pali-burmese-termbase-plain.md`, `pi-2-pali-burmese-termbase-plain.md`, read the way the sample's module does. Never edit anything in `pi-1-my/` or `pi-2-my/`.
- Cross-check of MEANING only (never wording): the English pi-3 zero-shot `AI_translation/english/pi-3-english-plain-zeroshot_split_chapters/<same file>` and the Marathi pi-3 rails `AI_translation/marathi/pi-3-marathi-plain-rails_split_chapters/<same file>`; method model for the frames of each naya: `0-INBOX/temp/pipeline/pi-3-mr/make_<chapters>.py`, `notes-<chapters>.md` (frame inventory only, never Marathi words).

## About the methods
Each naya has its own question / answer frames (saṅgahitena asaṅgahitaṃ, asaṅgahitena saṅgahitaṃ, sampayuttena vippayuttaṃ …: «Yaṃ … saṅgahitā, te dhammā … asaṅgahitā?» style questions and lists of topics as answers; «te dhammā katihi khandhehi … asaṅgahitā?»; «natthi», «na kehici» answers). Build each frame once, from the sample's pattern, and use it identically everywhere in your naya. Every number, every saṅgahita / asaṅgahita and sampayutta / vippayutta, every topic name in an answer list must match the Pāli exactly (checked by script).

## Source and output
- Source `AI_translation/pali/pi-3_split_chapters/<ch>.md`; output `AI_translation/burmese/pi-3-burmese-plain-zeroshot_split_chapters/<ch>.md`; generator `pi-3-my/make_<chapters>.py`; check `pi-3-my/check_<chapters>.py`; notes `pi-3-my/notes-<chapters>.md`.

## Rules
- Identical Pāli = identical Burmese (within pi-3, with the sample, and with pi-1 / pi-2 final). GENERATE every chapter by script from frames and tables.
- Polarity and numbers exact (checked by script). Headings keep their #-level. Block IDs exact; the source's number of non-empty lines per segment; one blank line between segments; no double blank lines.
- A NEW recurring term or phrase: record it in your notes («Pāli = Burmese», one per line). Do not edit my3_formulas.py or my3-zeroshot-terms.md. A consistency pass aligns all agents afterwards.
- «…pe…» / «…Pe…» become one «…». DASH RULE: «–» only where the Pāli line has one, same spot and count. No «।», «:-», «?»: questions end with their particle (လော / နည်း) and «။». Statements end with «။». Digits as the Pāli. Variant brackets as the sample. Source slips: translate as written, log them.

## Verify every chapter (all must pass before you report)
```
/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 0-INBOX/temp/pipeline/check_chapter_ids.py AI_translation/pali/pi-3_split_chapters AI_translation/burmese/pi-3-burmese-plain-zeroshot_split_chapters <ch>.md
/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 0-INBOX/temp/pipeline/pi-6-mr/check_text_pe.py AI_translation/pali/pi-3_split_chapters/<ch>.md AI_translation/burmese/pi-3-burmese-plain-zeroshot_split_chapters/<ch>.md
/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 0-INBOX/temp/pipeline/pi-4-mr/check_marks.py AI_translation/pali/pi-3_split_chapters/<ch>.md AI_translation/burmese/pi-3-burmese-plain-zeroshot_split_chapters/<ch>.md
```
All must print OK (delete your chk-pe copies afterwards). Plus your own check: 0 mismatches, and the reuse test n / n.

## Final report (short)
Per chapter: checks, segment count, own check, reuse n / n; key new terms and frames (or point to your notes); unsure Pāli and source slips.
