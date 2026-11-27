# Brief: Burmese zero-shot, remaining chapters (pi-4, Puggalapaññatti «ပုဂ္ဂိုလ်များကို သတ်မှတ်ဖော်ပြခြင်း»)

Work in /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails on macOS (zsh). Python: `/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8` (scripts in files). Other agents translate other chapters in parallel. Write ONLY your own chapter files, plus your generator, check and notes named after your chapters, inside `0-INBOX/temp/pipeline/pi-4-my/`. Never use the system temp directory. Do not commit. Never use the words for a planted starting value or its negative.

You may be paused for usage limits and resumed later: generate chapter by chapter, save each chapter as soon as it passes, keep your notes current.

## Source rule (binding)
Translate FROM THE PĀLI only. Never open or copy any existing Burmese translation or nissaya (never open `0-INBOX/temp/language-priority/`); no web searches.

## Read first
- `0-INBOX/temp/pipeline/burmese-style.md` (binding; incl. the locked pi-1, pi-2 and pi-3 termbase sections).
- `AI_translation/skills/zeroshot-translator.md`, `AI_translation/audience_profile/plain.md`.
- **The approved pi-4 sample (coordinator under the user's standing go-ahead, 2026-11-19), READ-ONLY, the model for everything:** `pi-4-my/my4_formulas.py` (import it; extend its tables in memory in YOUR script; never edit it; log every new string in your notes), `pi-4-my/make_sample.py` (copy functions; never run it: it rewrites shared files), `check_sample.py` (adapt as `check_<your chapters>.py`, incl. its reuse test, polarity and person-name checks), `my4-zeroshot-terms.md` (copy its strings verbatim; the PERSON-TYPE NAME TABLE for ones to tens is binding: each type keeps that exact Burmese name in heading, question and closing quote), `notes-sample.md` (method for later agents), and the outputs `AI_translation/burmese/pi-4-burmese-plain-zeroshot_split_chapters/preamble.md`, `1-matika.md`, `2-ekakapuggalapannatti.md`. Approved: title «ပုဂ္ဂိုလ်များကို သတ်မှတ်ဖော်ပြခြင်း», headings «N-မျိုးတွဲ ပုဂ္ဂိုလ် သတ်မှတ်ချက်», the frame «X ဟူသည် အဘယ် ပုဂ္ဂိုလ်နည်း။ ဤလောက၌ အချို့သော ပုဂ္ဂိုလ်သည် … – ဤပုဂ္ဂိုလ်ကို “X”ဟု ခေါ်သည်။», persons counted with «ယောက်», the negation rule (free na / no before a noun or clause «မဟုတ်», before a verb or agent noun «မ» + verb).
- **pi-1, pi-2 and pi-3 final Burmese are binding for identical Pāli** (topic names, kilesa / sīla / jhāna / path-and-fruit terms, the vices and virtues of the dukas, the fetters, realm names): the rails texts `AI_translation/burmese/pi-1-burmese-plain-rails_split_chapters/`, `pi-2-…`, `pi-3-burmese-plain-rails_split_chapters/`, the locked termbases `AI_translation/burmese/pi-{1,2,3}-pali-burmese-termbase-plain.md`, read the way the sample's module does. Never edit anything in `pi-1-my/`, `pi-2-my/` or `pi-3-my/`.
- Cross-check of MEANING only (never wording): the English pi-4 zero-shot `AI_translation/english/pi-4-english-plain-zeroshot_split_chapters/<same file>` and the Marathi pi-4 rails `AI_translation/marathi/pi-4-marathi-plain-rails_split_chapters/<same file>`; method model for the frames of each naya: `0-INBOX/temp/pipeline/pi-4-mr/make_<chapters>.py`, `notes-<chapters>.md` (frame inventory only, never Marathi words).

## About the text
The niddesa defines each person type in the approved frame; many types come in pairs or groups that differ only by a negation or one clause, and the fours and fives use similes (ponds, mangoes, mice, bulls, elephants, warriors, …). Build each repeated frame once and use it identically; keep paired definitions parallel word for word except where the Pāli differs; every number and every negation must match the Pāli exactly (checked by script); similes in plain, natural Burmese, nothing added.

## Source and output
- Source `AI_translation/pali/pi-4_split_chapters/<ch>.md`; output `AI_translation/burmese/pi-4-burmese-plain-zeroshot_split_chapters/<ch>.md`; generator `pi-4-my/make_<chapters>.py`; check `pi-4-my/check_<chapters>.py`; notes `pi-4-my/notes-<chapters>.md`.

## Rules
- Identical Pāli = identical Burmese (within pi-4, with the sample, and with pi-1 / pi-2 / pi-3 final). GENERATE every chapter by script: frames and tables for repeated parts, hand-written strings for unique prose kept in a table in the script (as the sample).
- Polarity and numbers exact (checked by script). Headings keep their #-level. Block IDs exact; the source's number of non-empty lines per segment; one blank line between segments; no double blank lines.
- A NEW recurring term or phrase: record it in your notes («Pāli = Burmese», one per line). Do not edit my4_formulas.py or my4-zeroshot-terms.md. A consistency pass aligns all agents afterwards.
- «…pe…» / «…Pe…» become one «…». DASH RULE: «–» only where the Pāli line has one, same spot and count. No «।», «:-», «?»: questions end with their particle (လော / နည်း) and «။». Statements end with «။». Digits as the Pāli. Variant brackets as the sample. Source slips: translate as written, log them.

## Verify every chapter (all must pass before you report)
```
/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 0-INBOX/temp/pipeline/check_chapter_ids.py AI_translation/pali/pi-4_split_chapters AI_translation/burmese/pi-4-burmese-plain-zeroshot_split_chapters <ch>.md
/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 0-INBOX/temp/pipeline/pi-6-mr/check_text_pe.py AI_translation/pali/pi-4_split_chapters/<ch>.md AI_translation/burmese/pi-4-burmese-plain-zeroshot_split_chapters/<ch>.md
/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 0-INBOX/temp/pipeline/pi-4-mr/check_marks.py AI_translation/pali/pi-4_split_chapters/<ch>.md AI_translation/burmese/pi-4-burmese-plain-zeroshot_split_chapters/<ch>.md
```
All must print OK (delete your chk-pe copies afterwards). Plus your own check: 0 mismatches, and the reuse test n / n.

## Final report (short)
Per chapter: checks, segment count, own check, reuse n / n; key new terms and frames (or point to your notes); unsure Pāli and source slips.
