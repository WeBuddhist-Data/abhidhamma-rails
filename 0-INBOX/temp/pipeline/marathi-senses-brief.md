# Brief: word-sense-grouper, Pāli→Marathi (pi-3)

Work in /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails on macOS (zsh). Use the Read/Write tools for files and run Python as `python3 -I -X utf8`. Write helper scripts to files. Write ONLY your own part files and helper scripts named after your part, in 0-INBOX/temp/pipeline/pi-3-mr/senses/. Never use the system temp directory. Don't commit.

**Read first:**
- AI_translation/skills/word-sense-grouper.md, and follow it exactly.
- 0-INBOX/temp/pipeline/marathi-style.md for the Marathi conventions and core terms.
- 0-INBOX/temp/pipeline/pi-3-mr/harmonise-notes.md (the harmonised Pāli = Marathi table) and pi-3-mr/mapper-mr/align-mapped-notes.md.
- **The user-approved sample (binding format and granularity):** pi-3-mr/senses/sample-senses.md (the first 80 headwords), built by senses_sample.py from agg-sample.tsv and decisions-sample.txt.
- For format and granularity of the later headwords, the user-approved Hindi senses file of the same book: AI_translation/hindi/pi-3-pali-word-hindi-senses-plain.md. Same headwords, same English tags where the senses line up.

**Input:** pi-3-mr/senses/agg-part1.tsv (660 headwords). There is one line per Pāli headword; case is already merged, and spelling and order follow the English senses file. Each line reads:
`headword <TAB> english sense tags from the English pipeline (may be empty) <TAB> marathi_value=count[example ids] | … <TAB> NDE=<count of no-equivalent occurrences>`

**Method:** use senses_sample.py, the approved tool.
1. Copy decisions-sample.txt to decisions-part1.txt and keep its three lines unchanged.
2. Run `python3 -I -X utf8 senses_sample.py build agg-part1.tsv decisions-part1.txt part1-senses.md`. It fails with an UNRESOLVED list until every headword with an empty or multi-sense English tag has a decision line. It also prints a REVIEW list of single-tag headwords whose Marathi values were lumped into one sense.
3. Write a decision line for every UNRESOLVED headword. Check every REVIEW headword: if its values are different meanings rather than synonyms or grammatical variants, add a decision that splits them. Use the Hindi senses file's tags for the same headword where they fit.
4. Lines 1–80 of part1-senses.md must equal sample-senses.md byte-for-byte. Check this by script.

**Guidance:**
- Use the English tags as starting glosses where the Marathi senses line up, but cluster from the Marathi evidence.
- Grammatical variants of one Marathi lemma (number, gender, oblique) are ONE sense. List them with " / ", most frequent first; the tool sorts them.
- The Marathi was drafted by parallel agents and then harmonised, so few synonym clashes should remain. If you still see synonyms for the SAME meaning, put them in ONE sense as candidates; the termbase step picks one.
- Split into separate senses only for genuinely different meanings, such as dhamma as घटना vs मनाचे विषय, rūpa as भौतिक रूप vs दृश्य रूप vs सूक्ष्म भौतिक लोक, hetuka as मूळ असलेला vs मुळांसह असलेला vs मुळे असलेला, dukkha as दुःख vs दुःखद, or niyata. When unsure, check the segments by their example ids in AI_translation/marathi/pi-3-marathi-plain-zeroshot_split_chapters/ and AI_translation/pali/pi-3_split_chapters/.
- Write tags in English. Keep them short, and make each a real gloss, never a copy of the value.
- A single candidate must not contain "; " or "/" except as the candidate separator " / ". If an attested value itself contains " / " (a paired keyword such as "āyatanāni / pādā"), the tool writes it with " आणि " instead. Note this in your report.
- NDE occurrences are already excluded (skill step 4), so don't add "(no direct equivalent)".

**Verify (skill step 6):** `python3 -I -X utf8 senses_sample.py verify agg-part1.tsv part1-senses.md` must print VERIFY OK. It checks that the headword list equals the input's, in the same order and with no duplicates, that every attested value appears under its headword, and that no tag is in Devanagari or copies a value. Then also run the lines 1–80 equality check.

**Final report (short):**
- headword count and the verification result;
- how many headwords have more than one sense;
- how many senses have more than one candidate;
- the ~15 most consequential synonym clashes or splits, with the decision taken.
