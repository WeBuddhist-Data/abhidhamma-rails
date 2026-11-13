# Brief: word-sense-grouper, Pāli→Hindi, pi-7 (Paṭṭhāna)

Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write tools for files (write scripts with the Write tool, never via a shell redirect), PowerShell for commands, `python -I -B -X utf8`, helper scripts written to files. Write ONLY your own part files (part<K>-senses.md, decisions-part<K>.txt; for the sample: sample-senses.md, decisions-sample.txt), plus helper scripts named after your part, in 0-INBOX\temp\pipeline\pi-7-hi\senses\. Never create files at the repo root or in a system temp folder. Do not touch 1-SOURCES\ or 4-SYSTEM\, and do not run git. Never write "seed" or "unseeded". You cannot write report files for me: return your report as text.

**Read first:**
- AI_translation\skills\word-sense-grouper.md, and follow it exactly.
- 0-INBOX\temp\pipeline\hindi-style.md (Hindi conventions, core terms).
- **Approved Hindi senses files (binding for conventions and granularity):** AI_translation\hindi\pi-1-pali-word-hindi-senses-plain.md, pi-2-… and pi-6-pali-word-hindi-senses-plain.md, with 0-INBOX\temp\pipeline\pi-1-hi\senses\senses-conventions.md and 0-INBOX\temp\pipeline\pi-6-hi\senses\senses-conventions-pi6.md. For a headword that also exists there, reuse their English tag wording and sense split where the meaning is the same (grep them).
- **pi-7 keyword-map conventions:** 0-INBOX\temp\pipeline\pi-7-hi\mapper-hi\hi-map-conventions-pi7.md (how the condition names, their negative and count forms, the frame words and the items were mapped), and 0-INBOX\temp\pipeline\pi-7-hi\mapper-hi\map-reports.md (where agents chose context-dependent values). They explain the values you will see.
- **The tool:** 0-INBOX\temp\pipeline\pi-7-hi\senses\senses_tool_pi7.py (build from a decisions file, verify, todo, show). Read its docstring. EVERY headword needs a decision line.
- **Once the sample is approved:** senses\sample-senses.md and decisions-sample.txt are binding; a part that contains sample headwords reuses the sample's decision lines verbatim for them.

**Input:** 0-INBOX\temp\pipeline\pi-7-hi\senses\agg-part<K>.tsv (sample: agg-sample.tsv). One line per Pāli headword (case merged; order of first appearance in the map):
`headword <TAB> en≈ English hints from the English pi-7 map (top 5, with counts) <TAB> hindi_value=count[example ids] | … <TAB> NDE=<count>`
pi-7 has NO English senses file: column 2 is only a hint for glossing (the English map is a zero-shot reading and its keyword lists were back-mapped, so hints can be noisy). Cluster from the Hindi evidence.

**Output:** 0-INBOX\temp\pipeline\pi-7-hi\senses\part<K>-senses.md (sample: sample-senses.md), built by the tool from your decisions file, same headwords, same order, one line each:
`pali: {english sense tag: हिंदी_a / हिंदी_b; tag2: हिंदी_c}`

**Guidance:**
- EVERY headword needs a real English tag: a short gloss of the meaning, with the grammatical role where useful ("{root condition, as a named condition (nominative): मूल-कारण}"). Never copy a Hindi value or a bare English hint as the tag.
- Grammatical variants of one Hindi lemma (number, gender, oblique) are ONE sense; list them with " / ", most frequent first.
- Synonyms for the SAME meaning go in ONE sense as candidates (the termbase step picks one). In pi-7 this includes the drift between parallel agents (e.g. natthi «नहीं / नहीं है / नहीं होना», jappeti «करना / पालना», gaṇhāti «ग्रहण करना / पकड़ना / अपनाना», pāṇaṃ «जीव / प्राणी») and the gapped and ungapped forms of one phrase.
- Split into separate senses only for genuinely different meanings. pi-7 cases: a condition name vs the plain word (atthi «उपस्थिति-कारण» the presence condition vs «है» "there is"; natthi «अनुपस्थिति-कारण» vs «नहीं» "there is not"; adhipati «प्रधानता-कारण» vs «प्रधानता» the predominant state; āhāra «आहार-कारण» vs «भोजन» physical food vs «आहार» the label); the negative condition as an ablative «X-कारण के बिना» vs as a noun «X-कारण का अभाव» (two grammatical roles: split them, tagged by role); anuloma «सकारात्मक क्रम» (the positive method) vs «अनुरूपता» (the conformity moment); rūpaṃ «भौतिक रूप» vs «दृश्य रूप» (visible form); vipāko «कर्म-फल» (the result) vs «कर्म के फल रूपी» (resultant, adjective); a heading name vs the same word inside a sentence. When unsure, look at the segments with the tool's `show` command.
- Values containing " … " (gapped phrases) are kept as written; they are one candidate.
- A single candidate must not contain "; " or "/" except as the separator " / ". If an attested value contains " / ", write it with " और " instead and note it in the report.
- NDE occurrences are already excluded; don't add "(no direct equivalent)".

**Verify (skill step 6):** `python -I -B -X utf8 0-INBOX\temp\pipeline\pi-7-hi\senses\senses_tool_pi7.py verify <agg.tsv> <out.md>` must pass (same headwords and order, every attested value placed once, no tag equal to a value, every line parses).

**Final report (short):** headword count and verification result; how many headwords have more than one sense; how many senses have more than one candidate; the ~15 most consequential synonym clashes or splits in your part.

## SAMPLE (first agent only)
Input agg-sample.tsv (120 headwords: the first 90 of part 1 and 30 more of its multi-value headwords). Write decisions-sample.txt and build sample-senses.md, and write senses\senses-conventions-pi7.md: every convention you settled (tag style, which splits, which variants merge), with examples, so 4 parallel agents can group the rest identically. Report under 400 words.
