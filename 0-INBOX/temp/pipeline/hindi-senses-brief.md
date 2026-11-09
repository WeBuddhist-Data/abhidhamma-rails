# Brief: word-sense-grouper, Pāli→Hindi (pi-3, pi-4, pi-5)

Work in D:\Work\OpenPecha\abhidhamma-rails. It is a Windows machine: use the Read/Write tools for files and PowerShell for commands, and run python as `python -I -X utf8`. Other agents may do other parts in parallel. Write ONLY your own part files, plus helper scripts named after your part, in your book's scratch folder.

**Read first:**
- AI_translation\skills\word-sense-grouper.md, and follow it exactly.
- 0-INBOX\temp\pipeline\hindi-style.md for the Hindi conventions and core terms.
- For format and granularity only, the user-approved Russian senses file of the same book: AI_translation\russian\pi-N-pali-word-russian-senses-plain.md.

**Input:** 0-INBOX\temp\pipeline\pi-N-hi\senses\agg-part<K>.tsv. There is one line per Pāli headword; case is already merged, and spelling and order follow the English senses file. Each line reads:
`headword <TAB> english sense tags from the English pipeline (may be empty) <TAB> hindi_value=count[example ids] | … <TAB> NDE=<count of no-equivalent occurrences>`

**Output:** 0-INBOX\temp\pipeline\pi-N-hi\senses\part<K>-senses.md, with the same headwords in the same order, one line each:
`pali: {english sense tag: हिंदी_a / हिंदी_b; tag2: हिंदी_c}`

**Guidance:**
- Use the English tags as starting glosses where the Hindi senses line up, but cluster from the Hindi evidence.
- Grammatical variants of one Hindi lemma (number, gender, oblique) are ONE sense. List them with " / ", most frequent first.
- The Hindi was drafted by parallel agents and then harmonised, so you may still see synonyms for the SAME meaning. Examples: सूत्र / उपदेश, समाप्त / पूरी हुई, लोक से परे / लोकोत्तर, सुप्त प्रवृत्ति / छिपी प्रवृत्ति. Put synonyms for one meaning in ONE sense as candidates; the termbase step will pick one.
- Split into separate senses only for genuinely different meanings, such as dhamma as परिघटना vs शिक्षा vs मन के विषय, or rūpa as भौतिक रूप vs दृश्य रूप. When unsure, check the segments by their example ids in AI_translation\hindi\pi-N-hindi-plain-zeroshot_split_chapters\ and AI_translation\pali\pi-N_split_chapters\.
- Write tags in English. Keep them short, and make each a real gloss, never a copy of the value.
- A single candidate must not contain "; " or "/" except as the candidate separator " / ". If an attested value itself contains " / " (a paired keyword), keep it as one candidate by writing it with " और " instead, and note this in your report.
- NDE occurrences are already excluded (skill step 4), so don't add "(no direct equivalent)".

**Verify (skill step 6) with a script.** Check that:
- the headword list of your output equals the input's, in the same order and with no duplicates;
- every Hindi value attested in the input appears under its headword, allowing the " / "→" और " rewrite.

Print the counts and any differences.

**Final report (short):**
- headword count and the verification result;
- how many headwords have more than one sense;
- how many senses have more than one candidate;
- the ~15 most consequential synonym clashes in your part.
