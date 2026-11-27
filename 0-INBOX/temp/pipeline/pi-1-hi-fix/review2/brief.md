# Brief: final review of the corrected Hindi pi-1, from two perspectives

The Hindi translation of the Dhammasaṅgaṇī (pi-1) was corrected on 2026-11-27. Review it from two perspectives, and suggest only the corrections that are necessary. It is read-only: change no translation, termbase or script. Write only your output file. Do **not** read `../review/verify-hi.md`, the earlier review: your judgement should be your own.

## 1. Audience profile

The audience is given in `AI_translation/audience_profile/plain.md`: readers with little or no Buddhist background; clear, modern, natural language; minor clarification by wording is allowed; nothing absent from the source. The text will be shown to them directly. Check language level, tone, terminology and understanding. Is it appropriate and easy for them to understand?

## 2. Scholar check

A scholar reading the uploaded text against the Pāli. Check:
- **accuracy;**
- **terminology:** consistent, with distinctions kept;
- **additions:** nothing added beyond plain-profile clarification;
- **structure:** faithful lists, numbering, …pe… abbreviations and variant-reading brackets;
- **display:** that it will display correctly.

Use `AI_translation/audience_profile/scholars.md` for what scholars need. Do not ask for Pāli transliteration in the running text: that belongs to a separate scholar version, not to this check.

## Read

- `0-INBOX/temp/pipeline/pi-1-hi-fix/fixes-log.md`: what was changed and why, including what was left on purpose for the human reviewers. Check the reasons rather than trusting them.
- `review2/changes.jsonl`: 105 items, examples of all 56 kinds of change. Fields:
  - `old`, `new`: the changed words;
  - `occurrences`: how often this exact change was made;
  - `before`, `after`: context;
  - `pali`: the Pāli block.
- `review2/sample.jsonl`: 163 blocks spread over the whole book, as they stand now, with the Pāli. `changed_by_fix` says whether a fix touched the block. Review the whole sentence, not only the changed words.
- Read in parts, about 25 lines at a time. You may also open `AI_translation/hindi/pi-1-hindi-plain.md`, the full current text, and `0-INBOX/temp/pipeline/pi-1-hi-fix/backup/pi-1-hindi-plain.md`, the text before the fixes.

## Rules

- **Necessary corrections only.** Each needs a clear justification: wrong meaning, misleading for this audience, ungrammatical, unclear, something added or lost, or a display or structure fault. Style preferences are not corrections.
- **Vocabulary-policy items** are listed in fixes-log.md under "Not changed, on purpose", for example मन for *citta* / *mano*, एकाग्रता, मोह, क्लेश, समभाव, क्षमता. Do not reopen them, except to note in one line if one is a real problem for this audience.
- **Be concrete:** give the ref, quote the Hindi, and give the correction.

## Output

`review2/final-review-hi.md`, in English:

1. **Verdicts:**
   - Audience: suitable / suitable with corrections / not suitable.
   - Scholar check: holds up / holds up with corrections / does not hold up.
   - 2–4 lines of reasons each.
2. **Necessary corrections:** a table with columns ref | perspective (audience/scholar/both) | severity (major/minor) | current | corrected | justification.
3. **Checked and fine:** what you looked at that needs no change (short).
4. **For the human reviewers:** the points only a native reader or a specialist can settle (short).

At the end, reply with only: the two verdicts, the count of corrections by severity, and the corrections themselves, one line each, if there are 10 or fewer, otherwise the 10 most important.
