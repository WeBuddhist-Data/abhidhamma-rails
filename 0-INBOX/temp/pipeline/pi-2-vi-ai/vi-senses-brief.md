# Brief: word-sense-grouper, Pāli→Vietnamese, pi-2 (Vibhaṅga)

Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write/Edit tools for files (write scripts with the Write tool at their full paths; never write any file from PowerShell, not even a temporary list), PowerShell for commands, `python -I -X utf8`. Write ONLY your own part files, plus helper scripts named after your part, in 0-INBOX\temp\pipeline\pi-2-vi-ai\senses\. Never create files at the repo root or in a system temp folder. Do not touch 1-SOURCES\ or 4-SYSTEM\, do not edit any pi-1 file, never run git (not even git status), never write "seed". You cannot write report files for me: return your report as text.

## FORBIDDEN (copyrighted reference translation)
Never open, grep or search: 1-SOURCES\Translations\Vietnamese\ (any file), 0-INBOX\raw-data\vi-*, 0-INBOX\temp\pipeline\pi-1-vi\, pi-2-vi\, pi-3-4-vi\, pi-5-vi\, pi-6-vi\, pi-7-vi\, pi-1-th-vi\, vi-tools\. No folder-wide searches over 0-INBOX\temp\pipeline\, 1-SOURCES\ or AI_translation\ (search only the specific files named here).

## Read first
- AI_translation\skills\word-sense-grouper.md, and follow it exactly.
- 0-INBOX\temp\pipeline\vietnamese-style.md (Vietnamese conventions, core terms, the review lessons on pairs that must stay distinct; sati = «sự tỉnh thức»).
- **The approved pi-1 Vietnamese run (binding where pi-2 has the same headword in the same sense; pi-2 repeats many pi-1 passages word for word):**
  - AI_translation\vietnamese\pi-1-pali-word-vietnamese-senses-plain.md (the merged approved senses: grep it for every headword you meet; 1,345 of pi-2's 4,971 headwords have a line there, 60 of the 120 sample headwords). Reuse its tag wording and splits where the Vietnamese values match; add senses only for values pi-1 does not have.
  - 0-INBOX\temp\pipeline\pi-1-vi-ai\senses\senses-conventions.md (the split/merge conventions and family tags: variants of one Vietnamese expression with/without «sự», a classifier, a tense/aspect word or «có» are ONE sense).
  - 0-INBOX\temp\pipeline\pi-1-vi-ai\senses\senses_tool_vi.py (build from a decisions file, verify, todo, show, words) and decisions-sample.txt (the decisions format).
  - 0-INBOX\temp\pipeline\pi-1-vi-ai\termbase\APPROVED.md (the user's term decisions; they explain some splits: sukha «hạnh phúc» (jhāna factor) vs «dễ chịu» (pleasant feeling); bodily pain dukkha «khó chịu»; vāra «mục» vs bhāṇavāra «phần»).
- **The approved pi-2 Russian senses of this same book** (for which pi-2 headwords have more than one meaning, and English tag wording): AI_translation\russian\pi-2-pali-word-russian-senses-plain.md (grep it for each headword) and 0-INBOX\temp\pipeline\pi-2-ru\senses\senses-conventions.md. Reuse its English tags word for word where the Pāli headword has the same meaning and pi-1 Vietnamese has no line. The split follows the meanings; the candidates are the Vietnamese values.
- pi-2 English senses AI_translation\english\pi-2-english-senses-plain.md: a hint for tag wording only.
- The pi-2 keyword-map conventions (why one Pāli word has several Vietnamese values: segment wording, nominaliser kept or dropped, fragments, gapped values, context splits): 0-INBOX\temp\pipeline\pi-2-vi-ai\mapper-vi\vi-map-conventions-pi2.md and notes-map-*.md.

## Input
0-INBOX\temp\pipeline\pi-2-vi-ai\senses\agg-part<K>.tsv (the sample uses agg-sample.tsv: the first 90 rows of part 1 plus the next 30 multi-value rows, last headword «icchatā»). One line per Pāli headword (case merged, order = first appearance in the map):
`headword <TAB> en≈ English hints <TAB> vietnamese_value=count[example ids] | … <TAB> NDE=<count>`
Column 2 is only a HINT (the English equivalents the English pi-2 map gives that headword). It is not a list of senses.

## Output
0-INBOX\temp\pipeline\pi-2-vi-ai\senses\part<K>-senses.md (the sample: sample-senses.md), same headwords, same order, one line each:
`pali: {english sense tag: tiếng Việt a / tiếng Việt b; tag2: tiếng Việt c}`

## Guidance
- EVERY headword needs a real English tag: a short gloss of the meaning, with the grammatical role where useful. Never copy a Vietnamese value or the bare English hint as the tag. A script may draft tags from a table you write, but you write that table yourself, headword by headword (copying a pi-1 Vietnamese or pi-2 Russian tag for the same headword and sense is fine).
- Vietnamese has no inflection. Variants of ONE Vietnamese expression go in ONE sense, joined with " / ", most frequent first: with or without the nominaliser or classifier («sự hoài nghi» / «hoài nghi», «loại tâm» / «tâm»), with or without a tense/aspect word («sinh khởi» / «đã sinh khởi»), with or without «có».
- Synonyms for the SAME meaning go in ONE sense as candidates (the termbase step picks one).
- Split into separate senses only for genuinely different meanings, as pi-1 Vietnamese and pi-2 Russian do. Known pi-2 splits (from the map): kāmadhātu «yếu tố dục lạc» (element, ch3) vs «cõi dục lạc» (plane, ch18); dhātu «yếu tố» vs «cõi»; dhamma «hiện tượng» vs «đối tượng của ý» vs «Giáo Pháp»; dukkha «khổ đau» (suffering, truth) vs «khó chịu» (painful feeling) vs «khó khăn» (of practice); sukha «hạnh phúc» vs «dễ chịu» vs «dễ dàng»; viharati «sống» (conduct) vs «an trú» (jhāna); hetu «gốc rễ» (root) vs «nguyên nhân» (cause); pasāda «chất nhạy cảm» (sense organ, pi-1) vs «lòng tin trong sáng» (confidence); vossagga «sự buông xả» (relinquishment, ch10) vs «sự buông lơi» (slackness, ch17); Catukkaṃ / Pañcakaṃ «phương pháp chia bốn» (jhāna method) vs «phân loại theo nhóm bốn» (classification). When unsure, look at the segments by their example ids in AI_translation\vietnamese\pi-2-vietnamese-plain-zeroshot_split_chapters\ and AI_translation\pali\pi-2_split_chapters\.
- Values containing " … " (gapped phrases) are kept as written; each is one candidate.
- A single candidate must not contain "; " or "/" except as the separator " / ". If an attested value contains " / ", write it with " và " instead and note it in the report.
- NDE occurrences are already excluded; don't add "(no direct equivalent)".

## Parts 1–8 (after the sample): binding
The user approved the sample (senses\sample-senses.md, decisions-sample.txt) AS IS on 2026-11-19, including the judgement calls: Jāti «sự sinh» / «xuất thân» (jātimada) split; Duka / Tika «bộ đôi / bộ ba» (matrix) vs «phân loại theo nhóm hai / ba» (niddesa and closing labels of ch16–17), tag "classification by Ns"; āhāro «dưỡng chất» / «thức ăn»; rūpaṃ «điều» (piyarūpaṃ); jātaṃ «sinh» merged with «đã sinh ra»; Dhātu «cõi» only in ch18. There are 8 parts of about 620 headwords. The parts run ONE AT A TIME (user), so read the finished earlier parts' decisions files too and keep their tags and splits for the same families.
- senses\senses-conventions.md (READ-ONLY) and senses\senses_tool_vi.py (`build|verify|todo|show|words|prior|reuse --part K`; READ-ONLY, call it, don't edit it; in PowerShell write `-` for "any value"). Write your decisions to senses\decisions-part<K>.txt and build with the tool.
- Part 1 contains the 120 sample headwords: copy their decisions from decisions-sample.txt unchanged.
- The same headword family gets the same tag wording as in the sample and earlier parts (X-indriyaṃ, X-balaṃ, citta-X, a-/an- negatives, the matrix items, the number headings).
- For every headword that pi-1 Vietnamese has, run `prior` and keep the pi-1 tag where the Vietnamese values match; otherwise the pi-2 Russian tag where the meaning is the same.

## Sample only: also write (for the later parts)
- senses\senses-conventions.md: the split/merge conventions for pi-2 Vietnamese (start from the pi-1 Vietnamese file; record only what pi-2 adds or changes), with the tags of the recurring headword families.
- senses\senses_tool_vi.py: the pi-1 Vietnamese tool adapted to pi-2 paths (map, Pāli and Vietnamese chapter folders, senses folder), `build|verify|todo|show|words --part K` plus `sample`, and a `prior` command printing the pi-1 Vietnamese senses line and the pi-2 Russian senses line for the headwords of a part. Write your decisions to senses\decisions-sample.txt and build with it.

## Verify (skill step 6) with the tool
The headword list of your output equals the input's, same order, no duplicates; every attested Vietnamese value appears under its headword (allowing the " / "→" và " rewrite); no tag equals its value; every line parses as `hw: {tag: v / v; tag: v}`. Print counts and differences.

## Report (under 400 words, as text)
Headword count and verification result; how many headwords have more than one sense; how many senses have more than one candidate; how many lines reuse a pi-1 Vietnamese tag; the conventions you settled; 10–15 example lines for review (including the multi-sense ones); anything genuinely unclear.
