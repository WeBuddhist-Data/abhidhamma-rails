# Brief: verify the fixed Hindi pi-1 against the audience profile and the scholar check

The Hindi translation of the Dhammasaṅgaṇī (pi-1) was corrected on 2026-11-27. Your job is to verify, independently, that the corrected text is **safe for its audience and holds up to a scholar's check**, and that the fixes did not break anything. It is read-only: change no translation, termbase or script. Write only your output file.

## Read first

1. `AI_translation/audience_profile/plain.md`: the profile the translation is for (readers with little or no Buddhist background; clear, modern, natural Hindi; minor clarification by wording allowed; nothing absent from the source).
2. `AI_translation/audience_profile/scholars.md`, adapted to this check. A scholar reads the uploaded text against the Pāli, so check that it is accurate, keeps distinctions, adds nothing beyond plain-profile clarification, and the structure is faithful. (Do not ask for Pāli transliteration in the text: that would be a separate scholar version, not this check.)
3. `0-INBOX/temp/pipeline/pi-1-hi-fix/fixes-log.md`: what was changed and why. Do not take its reasons on trust: check them.

## Inputs (read in parts, about 25 lines at a time)

- `review/changes.jsonl`: 97 items, two examples of each of the 52 kinds of change. Fields:
  - `old`, `new`: the changed words;
  - `occurrences`: how often this exact change was made;
  - `before`, `after`: about 10 words of context;
  - `pali`: the Pāli block.
- `review/sample-after.jsonl`: 166 blocks spread over the whole book, in their corrected form (`changed_by_fix` says whether the fix touched them). Use this to check whole sentences, not only the changed words.

## For each kind of change, decide

1. **Meaning:** does the new wording mean what the Pāli means here? Is it better than the old one, the same, or worse?
2. **Audience (plain.md):** can a reader with no Buddhist background understand it? Is it natural Hindi? In particular, judge विज्ञान for *viññāṇa*: everyday Hindi uses विज्ञान for "science". Does the context make the sense clear, or would a plain reader be misled?
3. **Scholar check:** accurate, distinctions kept, nothing added beyond what plain.md allows?
4. **Grammar:** gender and number agreement after the change (चेतना was feminine, विज्ञान is masculine; निडरता feminine, वृत्ति feminine), case, word order.

And in the 166 sample blocks: any sentence that is now ungrammatical, unclear or wrong because of a fix, and any problem the fixes missed that the profile would require fixing.

## Rules

- Be concrete: quote the Hindi, give the ref.
- Only real problems. Do not propose style preferences, and do not reopen the vocabulary-policy items that were left for reviewers on purpose. These are listed in fixes-log.md under "Not changed, on purpose": मन for *citta*/*mano*, एकाग्रता, मोह, क्लेश, समभाव, क्षमता, तत्परता, जकड़न, मानसिक क्रिया. Mention one only if a fix made it worse.
- For every problem, give the correction and the reason.

## Output

`review/verify-hi.md`, in English:

1. **Verdict:** is the corrected text safe for the plain audience (yes / yes with corrections / no), and does it hold up to the scholar check (yes / yes with corrections / no)? Give 2–4 lines of reasons each.
2. **Per change:** a table with columns kind of change | verdict (better / same / worse / wrong) | audience | scholar | note. One row per kind (52 at most; group trivially identical ones).
3. **Problems:** a table with columns ref | severity (major/minor) | current | suggested | reason.
4. **Regression check:** what you looked for in the 166 blocks, and what you found.

At the end, reply with only: the two verdicts, the number of problems by severity, and the most important 8 (one line each).
