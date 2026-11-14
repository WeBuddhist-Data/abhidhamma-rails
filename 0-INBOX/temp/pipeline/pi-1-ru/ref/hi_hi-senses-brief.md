# Brief: word-sense-grouper, Pāli→Hindi, pi-1 (Dhammasaṅgaṇī)

Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write tools for files, PowerShell for commands, `python -I -X utf8`, helper scripts written to files. Write ONLY your own part files, plus helper scripts named after your part, in 0-INBOX\temp\pipeline\pi-1-hi\senses\. Do not touch 1-SOURCES\ or 4-SYSTEM\, and do not run git.

**Read first:**
- AI_translation\skills\word-sense-grouper.md, and follow it exactly.
- 0-INBOX\temp\pipeline\hindi-style.md (Hindi conventions, core terms).
- For format and granularity: the user-approved Hindi senses files of earlier books, AI_translation\hindi\pi-4-pali-word-hindi-senses-plain.md and pi-5-…-plain.md (look at 40 lines of each; grep them for headwords you meet, and reuse their tag wording where the meaning is the same).
- The tooling used for pi-4 (adapt, don't edit in place): 0-INBOX\temp\pipeline\pi-4-hi\senses\senses_tool.py (build from a decisions file + verify).

**Input:** 0-INBOX\temp\pipeline\pi-1-hi\senses\agg-part<K>.tsv. One line per Pāli headword (case merged, order = first appearance in the map):
`headword <TAB> en≈ English hints <TAB> hindi_value=count[example ids] | … <TAB> NDE=<count>`
pi-1 has NO English senses file. Column 2 is only a HINT: the English equivalents the English pi-1 map gives that headword (with counts). Use it to write good English tags; it is not a list of senses.

**Output:** 0-INBOX\temp\pipeline\pi-1-hi\senses\part<K>-senses.md, same headwords, same order, one line each:
`pali: {english sense tag: हिंदी_a / हिंदी_b; tag2: हिंदी_c}`

**Guidance:**
- EVERY headword needs a real English tag: a short gloss of the meaning, with the grammatical role where useful (as the pi-4/pi-5 files do: "{wholesome, said of states (nominative pl.): हितकर}"). Never copy a Hindi value or the bare English hint as the tag. A script may draft tags from a table you write, but you must write that table yourself, headword by headword.
- Grammatical variants of one Hindi lemma (number, gender, oblique) are ONE sense; list them with " / ", most frequent first.
- Synonyms for the SAME meaning go in ONE sense as candidates (the termbase step picks one).
- Split into separate senses only for genuinely different meanings, e.g. rūpa as भौतिक रूप (material form) vs दृश्य रूप (visible form, object of the eye) vs सूक्ष्म भौतिक (fine-material, of the sphere); dhamma as परिघटना vs मन के विषय vs शिक्षा; kāya as मानसिक काया (mental body) vs शरीर (physical body). When unsure, look at the segments by their example ids in AI_translation\hindi\pi-1-hindi-plain-zeroshot_split_chapters\ and AI_translation\pali\pi-1_split_chapters\.
- Values containing " … " (gapped phrases) are kept as written; they are one candidate.
- A single candidate must not contain "; " or "/" except as the separator " / ". If an attested value contains " / ", write it with " और " instead and note it in the report.
- NDE occurrences are already excluded; don't add "(no direct equivalent)".
- Tags in English, short, and never a copy of the value.

**Verify (skill step 6) with a script.** The headword list of your output equals the input's, same order, no duplicates; every attested Hindi value appears under its headword (allowing the " / "→" और " rewrite); no tag equals its value; every line parses as `hw: {tag: v / v; tag: v}`. Print counts and differences.

**Final report (short):** headword count and verification result; how many headwords have more than one sense; how many senses have more than one candidate; the ~15 most consequential synonym clashes or splits in your part.
