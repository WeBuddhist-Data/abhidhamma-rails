# Brief: word-sense-grouper, Pāli→Hindi, pi-2 (Vibhaṅga)

Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write tools for files, PowerShell for commands, `python -I -X utf8`, helper scripts written to files. Write ONLY your own part files (part<K>-senses.md, decisions-part<K>.txt), plus helper scripts named after your part, in 0-INBOX\temp\pipeline\pi-2-hi\senses\. Do not touch 1-SOURCES\ or 4-SYSTEM\, and do not run git.

**Read first:**
- AI_translation\skills\word-sense-grouper.md, and follow it exactly.
- 0-INBOX\temp\pipeline\hindi-style.md (Hindi conventions, core terms).
- **pi-1 (user-approved, binding for conventions):** 0-INBOX\temp\pipeline\pi-1-hi\senses\senses-conventions.md, and the finished file AI_translation\hindi\pi-1-pali-word-hindi-senses-plain.md. pi-2 shares much vocabulary with pi-1: for a headword that also exists in pi-1, reuse pi-1's English tag wording and sense split where the meaning is the same (grep it).
- For format: AI_translation\hindi\pi-4-pali-word-hindi-senses-plain.md and pi-5-…-plain.md (40 lines each).
- **The tool:** 0-INBOX\temp\pipeline\pi-2-hi\senses\senses_tool_pi2.py (build from a decisions file, verify, todo, show). Read its docstring. EVERY headword needs a decision line.

**Input:** 0-INBOX\temp\pipeline\pi-2-hi\senses\agg-part<K>.tsv. One line per Pāli headword (case merged, order = first appearance in the map):
`headword <TAB> en≈ English hints <TAB> hindi_value=count[example ids] | … <TAB> NDE=<count>`
pi-2 has NO English senses file. Column 2 is only a HINT: the English equivalents the English pi-2 map gives that headword (with counts). Use it to write good English tags; it is not a list of senses.

**Output:** 0-INBOX\temp\pipeline\pi-2-hi\senses\part<K>-senses.md (built by the tool from decisions-part<K>.txt), same headwords, same order, one line each:
`pali: {english sense tag: हिंदी_a / हिंदी_b; tag2: हिंदी_c}`

**Guidance:**
- EVERY headword needs a real English tag: a short gloss of the meaning, with the grammatical role where useful ("{wholesome, said of states (nominative pl.): हितकर}"). Never copy a Hindi value or the bare English hint as the tag. A script may draft tags from a table you write, but you must write that table yourself, headword by headword.
- Grammatical variants of one Hindi lemma (number, gender, oblique) are ONE sense; list them with " / ", most frequent first.
- Synonyms for the SAME meaning go in ONE sense as candidates (the termbase step picks one).
- Split into separate senses only for genuinely different meanings, e.g. rūpa as भौतिक रूप (material form) vs दृश्य रूप (visible form) vs सूक्ष्म भौतिक (fine-material sphere); dhamma as परिघटना vs मन के विषय vs शिक्षा; kāya as मानसिक काया vs शरीर; dhātu as तत्व vs लोक. When unsure, look at the segments with the tool's `show` command.
- Values containing " … " (gapped phrases) are kept as written; they are one candidate.
- A single candidate must not contain "; " or "/" except as the separator " / ". If an attested value contains " / ", write it with " और " instead and note it in the report.
- NDE occurrences are already excluded; don't add "(no direct equivalent)".

**Verify (skill step 6):** `python -I -X utf8 0-INBOX\temp\pipeline\pi-2-hi\senses\senses_tool_pi2.py verify <agg.tsv> <out.md>` must pass (same headwords and order, every attested value placed once, no tag equal to a value, every line parses).

**Final report (short):** headword count and verification result; how many headwords have more than one sense; how many senses have more than one candidate; the ~15 most consequential synonym clashes or splits in your part.
