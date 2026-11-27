# Brief: last verification of the corrected Hindi pi-1 (audience and scholar)

This is the last check before the corrected Hindi translation of the Dhammasaṅgaṇī (pi-1) goes to human reviewers. Verify it independently. It is read-only: change no translation, termbase or script. Write only your output file. Do **not** read the earlier reviews (`../review/`, `../review2/`, `../scholar-compare/`): your judgement should be your own.

## The two perspectives

1. **Audience: `AI_translation/audience_profile/plain.md`.** These are readers with little or no Buddhist background. The translation should be clear, modern and natural; minor clarification by wording is allowed; nothing may be added that is absent from the source. The text goes to them directly: is it appropriate and easy to understand, and is the language level, tone and terminology right for them?
2. **Scholar: `AI_translation/audience_profile/scholars.md`.** A scholar reading the uploaded text against the Pāli. Check that it is accurate, that the terminology is consistent and distinctions are kept, that nothing is added beyond what plain.md allows, and that the structure and display are faithful (lists, numbering, …pe…, variant-reading brackets).
   - You may use the vault's commentary `1-SOURCES/Commentaries/pi-dhammasangani-atthakatha.md`.
   - You may also use the English scholarly termbase `pali-english/audience_requirments/termbase/termbase-pi-1-audience_scholarly.md`, but note that this termbase has errors of its own.
   - Do not ask for Pāli transliteration in the running text. That belongs to a separate scholar version, and this text was not made as one: say so once, in one line, and move on.

`0-INBOX/temp/pipeline/pi-1-hi-fix/fixes-log.md` says what was changed and why, and what was left for the human reviewers on purpose. Check its reasons rather than trusting them.

## Inputs (read in parts, about 25 lines at a time)

- `review3/changes.jsonl`: one example of each of the 62 kinds of change (`old`, `new`, `occurrences`, `before`, `after`, `pali`).
- `review3/sample.jsonl`: 140 blocks from across the book, none of them seen by earlier reviews, with the Pāli. Review whole sentences.
- You may open `AI_translation/hindi/pi-1-hindi-plain.md` (current) and `0-INBOX/temp/pipeline/pi-1-hi-fix/backup/pi-1-hindi-plain.md` (before the fixes).

## Rules

- Only necessary corrections, each with a clear reason: wrong meaning, misleading for this audience, ungrammatical, unclear, an addition or loss, or a structure/display fault. Style preferences are not corrections.
- Do not reopen the vocabulary-policy items listed under "Not changed, on purpose" in the fixes log, unless one is a real problem, and then say it in one line.
- Be concrete: ref, the Hindi quoted, the correction.

## Output

`review3/last-review-hi.md`, in English:
1. **Verdicts:** audience satisfied / satisfied with corrections / not satisfied; scholar check satisfied / satisfied with corrections / not satisfied, with 2–4 lines of reasons each.
2. **Necessary corrections:** a table with columns ref | perspective | severity | current | corrected | reason. Write "none" if there are none.
3. **Checked and fine** (short).
4. **For the human reviewers** (short).

At the end, reply with only: the two verdicts, the number of corrections by severity, and each correction in one line.
