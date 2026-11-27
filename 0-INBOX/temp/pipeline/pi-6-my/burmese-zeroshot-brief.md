# Brief: Burmese zero-shot, remaining chapters (pi-6, Yamaka «အတွဲလိုက် မေးဖြေခြင်း»)

Work in /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails on macOS (zsh). Python: `/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8` (scripts in files). Other agents translate other chapters in parallel. Write ONLY your own chapter files, plus your generator, check and notes named after your chapters, inside `0-INBOX/temp/pipeline/pi-6-my/`. Never use the system temp directory. Do not commit. Never use the words for a planted starting value or its negative.

You may be paused for usage limits and resumed later: generate chapter by chapter, save each chapter as soon as it passes, keep your notes current.

## Source rule (binding)
Translate FROM THE PĀLI only. Never open or copy any existing Burmese translation or nissaya (never open `0-INBOX/temp/language-priority/`); no web searches.

## Read first
- `0-INBOX/temp/pipeline/burmese-style.md` (binding; incl. the locked pi-1 … pi-5 termbase sections).
- `AI_translation/skills/zeroshot-translator.md`, `AI_translation/audience_profile/plain.md`.
- **The approved pi-6 sample (coordinator under the user's standing go-ahead, 2026-11-22), READ-ONLY, the model for everything:** `pi-6-my/my6_formulas.py` (import it; extend its tables in memory in YOUR script; never edit it; log every new string in your notes), `pi-6-my/make_sample.py` (copy functions; never run it: it rewrites shared files), `check_sample.py` (adapt as `check_<your chapters>.py`, incl. its polarity, quote-nesting, recurring-sentence and reuse tests), `my6-zeroshot-terms.md` (copy its strings verbatim: every question and answer frame in every tense and polarity, the answers Āmantā «ဟုတ်ပါသည်။», No «မဟုတ်ပါ။», Natthi «မရှိပါ။», the person / place types, the vāra / naya / uddesa / niddesa headings, anuloma / paccanīka «အဟုတ်ပြ ပုံစံ / အငြင်းပြ ပုံစံ», the chapter names proposed in the module, colophons), `notes-sample.md`, and the outputs `AI_translation/burmese/pi-6-burmese-plain-zeroshot_split_chapters/preamble.md`, `1-mulayamaka.md`, `2-01-khandhayamaka.md`. Approved: title «အတွဲလိုက် မေးဖြေခြင်း», the chapter names, the frames and tenses, hetu «အကြောင်း» in the hetuvāra list, cavati «စုတေ». The coordinator decisions are at the top of `pi-6-my/notes-sample.md`.
- **pi-1 … pi-5 final Burmese are binding for identical Pāli** (khandha / āyatana / dhātu / sacca / indriya names and lists, saṅkhāra, the anusayas, citta, the realms and person types, path and fruit): the rails texts `AI_translation/burmese/pi-{1,2,3,4,5}-burmese-plain-rails_split_chapters/`, the locked termbases `AI_translation/burmese/pi-{1,2,3,4,5}-pali-burmese-termbase-plain.md`, read the way the sample's module does. Never edit anything in `pi-1-my/` … `pi-6-my/`'s shared files (my6_formulas.py, make_sample.py, check_sample.py, my6-zeroshot-terms.md, notes-sample.md).
- Cross-check of MEANING only (never wording): the English pi-6 rails `AI_translation/english/pi-6-english-plain-rails_split_chapters/<same file>` and the Marathi pi-6 rails `AI_translation/marathi/pi-6-marathi-plain-rails_split_chapters/<same file>`; method model for the frames: `0-INBOX/temp/pipeline/pi-6-mr/make_<chapters>.py`, `notes-<chapters>.md` (frame inventory only, never Marathi words).

## About the text
Each Yamaka chapter repeats the sample's vāras and question / answer frames with that chapter's terms (āyatana, dhātu, sacca, saṅkhāra, anusaya, citta, dhamma, indriya), plus chapter-specific sections (e.g. the anusaya chapter's sections on the seven latent tendencies by person, place and plane; the citta chapter's mind-moments). Build each term and each person / place type once and fill the frames from them, so identical Pāli is identical Burmese; every polarity (uppajjati / nuppajjati, nirujjhati / na nirujjhati, atthi / natthi, anuseti / nānuseti, pajahati, pariññā, Āmantā / No) and every tense must match the Pāli exactly (checked by script).

## Source and output
- Source `AI_translation/pali/pi-6_split_chapters/<ch>.md`; output `AI_translation/burmese/pi-6-burmese-plain-zeroshot_split_chapters/<ch>.md`; generator `pi-6-my/make_<chapters>.py`; check `pi-6-my/check_<chapters>.py`; notes `pi-6-my/notes-<chapters>.md`.

## Rules
- Identical Pāli = identical Burmese (within pi-6, with the sample, and with pi-1 … pi-5 final). GENERATE every chapter by script: frames and tables for repeated parts, hand-written strings for unique prose kept in a table in the script (as the sample).
- Polarity and numbers exact (checked by script). Headings keep their #-level. Block IDs exact; the source's number of non-empty lines per segment; one blank line between segments; no double blank lines.
- A NEW recurring term or phrase: record it in your notes («Pāli = Burmese», one per line). Do not edit my6_formulas.py or my6-zeroshot-terms.md. A consistency pass aligns all agents afterwards.
- «…pe…» / «…Pe…» become one «…». DASH RULE: «–» only where the Pāli line has one, same spot and count. No «।», «:-», «?»: questions end with their particle (လော / နည်း) and «။». Statements end with «။». Digits as the Pāli. Variant brackets as the sample. Source slips: translate as written, log them.

## Verify every chapter (all must pass before you report)
```
/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 0-INBOX/temp/pipeline/check_chapter_ids.py AI_translation/pali/pi-6_split_chapters AI_translation/burmese/pi-6-burmese-plain-zeroshot_split_chapters <ch>.md
/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 0-INBOX/temp/pipeline/pi-6-mr/check_text_pe.py AI_translation/pali/pi-6_split_chapters/<ch>.md AI_translation/burmese/pi-6-burmese-plain-zeroshot_split_chapters/<ch>.md
/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 0-INBOX/temp/pipeline/pi-4-mr/check_marks.py AI_translation/pali/pi-6_split_chapters/<ch>.md AI_translation/burmese/pi-6-burmese-plain-zeroshot_split_chapters/<ch>.md
```
All must print OK (delete your chk-pe copies afterwards). Plus your own check: 0 mismatches, and the reuse test n / n.

## Final report (short)
Per chapter: checks, segment count, own check, reuse n / n; key new terms and frames (or point to your notes); unsure Pāli and source slips.

Never use /private/tmp or /tmp (no `cd /tmp` either). You may be paused for usage limits: save chapter by chapter.
