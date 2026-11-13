# Brief: word-sense-grouper, Pāli→Hindi, pi-6 (Yamaka)

Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write tools for files, PowerShell for commands, `python -I -X utf8`, helper scripts written to files. Write ONLY your own part files (part<K>-senses.md, decisions-part<K>.txt; for the sample: sample-senses.md, decisions-sample.txt), plus helper scripts named after your part, in 0-INBOX\temp\pipeline\pi-6-hi\senses\. Never create files at the repo root. Do not touch 1-SOURCES\ or 4-SYSTEM\, and do not run git. Never write "seed" or "unseeded".

**Read first:**
- AI_translation\skills\word-sense-grouper.md, and follow it exactly.
- 0-INBOX\temp\pipeline\hindi-style.md (Hindi conventions, core terms).
- **Approved Hindi senses files (binding for conventions and granularity):** AI_translation\hindi\pi-1-pali-word-hindi-senses-plain.md and pi-2-pali-word-hindi-senses-plain.md, with 0-INBOX\temp\pipeline\pi-1-hi\senses\senses-conventions.md. For a headword that also exists there, reuse their English tag wording and sense split where the meaning is the same (grep them).
- **pi-6 keyword-map conventions:** 0-INBOX\temp\pipeline\pi-6-hi\mapper-hi\hi-map-conventions-pi6.md (how the process verbs, tenses, negatives, beings and places were mapped). It explains the values you will see.
- **The tool:** 0-INBOX\temp\pipeline\pi-6-hi\senses\senses_tool_pi6.py (build from a decisions file, verify, todo, show). Read its docstring. EVERY headword needs a decision line.
- **Once the sample is approved:** senses\sample-senses.md and decisions-sample.txt are binding; part 1 reuses the sample's decision lines verbatim for its first 120 headwords.

**Input:** 0-INBOX\temp\pipeline\pi-6-hi\senses\agg-part<K>.tsv (sample: agg-sample.tsv). One line per Pāli headword (case merged; spelling and order follow the English senses file):
`headword <TAB> English sense tags from the English pi-6 pipeline <TAB> hindi_value=count[example ids] | … <TAB> NDE=<count>`
Column 2 is the English senses file's tags for that headword: use them as starting glosses where the Hindi senses line up, but cluster from the Hindi evidence.

**Output:** 0-INBOX\temp\pipeline\pi-6-hi\senses\part<K>-senses.md (sample: sample-senses.md), built by the tool from your decisions file, same headwords, same order, one line each:
`pali: {english sense tag: हिंदी_a / हिंदी_b; tag2: हिंदी_c}`

**Guidance:**
- EVERY headword needs a real English tag: a short gloss of the meaning, with the grammatical role where useful ("{wholesome roots (nominative pl.): हितकर मूल}"). Never copy a Hindi value as the tag.
- Grammatical variants of one Hindi lemma (number, gender, oblique) are ONE sense; list them with " / ", most frequent first. In pi-6 this includes the process verbs' tense forms only when they are the same Pāli tense (the keyword already fixes the tense) and the «लोग» / bare-participle variants of the same being phrase (e.g. «समाप्ति की ध्यान-अवस्था में लीन लोग / समाप्ति की ध्यान-अवस्था में लीन»): one sense, candidates for the termbase.
- Synonyms for the SAME meaning go in ONE sense as candidates (the termbase step picks one).
- Split into separate senses only for genuinely different meanings. pi-6 cases: a bare word in the word-checking pairs vs the full term (rūpaṃ = रूप "the word 'form' in the term-checking pairs" vs भौतिक रूप "material form"); a realm vs its beings (Arūpaṃ अभौतिक लोक "the formless realm, as a place" vs Arūpānaṃ अभौतिक लोक के प्राणी — usually different headwords already); Itaresaṃ «बाकी सब» (the rest, standing alone) vs «बाकी» (before a group). When unsure, look at the segments with the tool's `show` command.
- Values containing " … " (gapped phrases) are kept as written; they are one candidate.
- A single candidate must not contain "; " or "/" except as the separator " / ". If an attested value contains " / ", write it with " और " instead and note it in the report.
- NDE occurrences are already excluded; don't add "(no direct equivalent)".

**Verify (skill step 6):** `python -I -X utf8 0-INBOX\temp\pipeline\pi-6-hi\senses\senses_tool_pi6.py verify <agg.tsv> <out.md>` must pass (same headwords and order, every attested value placed once, no tag equal to a value, every line parses).

**Final report (short):** headword count and verification result; how many headwords have more than one sense; how many senses have more than one candidate; the ~15 most consequential synonym clashes or splits in your part.
