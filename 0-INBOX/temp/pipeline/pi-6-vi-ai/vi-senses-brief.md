# Brief: word-sense-grouper, Pāli→Vietnamese, pi-6 (Yamaka)

Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write/Edit tools for files (write scripts with the Write tool at their full paths; never write any file from PowerShell, not even a temporary list), PowerShell for commands, `python -I -X utf8 -B` (-B: no __pycache__). Write ONLY your own files (named below), plus helper scripts named after your part, in 0-INBOX\temp\pipeline\pi-6-vi-ai\senses\, with LF line endings. Never create files at the repo root (not even an empty one), outside the repo or in a system temp folder. Do not touch 1-SOURCES\ or 4-SYSTEM\, do not edit any pi-1 … pi-5 file, never run git (not even git status), never write "seed". No web. You cannot write report files for me: return your report as text.

## FORBIDDEN (copyrighted reference translation)
Never open, grep or search: 1-SOURCES\Translations\Vietnamese\ (any file), 0-INBOX\raw-data\vi-*, 0-INBOX\temp\pipeline\pi-1-vi\, pi-2-vi\, pi-3-4-vi\, pi-5-vi\, pi-6-vi\, pi-7-vi\, pi-1-th-vi\, vi-tools\. No folder-wide searches over 0-INBOX\temp\pipeline\, 1-SOURCES\ or AI_translation\: Grep only the specific files named here.

## Read first
- AI_translation\skills\word-sense-grouper.md, and follow it exactly.
- 0-INBOX\temp\pipeline\vietnamese-style.md (core terms, pairs that must stay distinct; sati = «sự tỉnh thức»).
- **The approved Vietnamese runs of pi-1 … pi-5 (binding where pi-6 has the same headword in the same sense):**
  - AI_translation\vietnamese\pi-5-pali-word-vietnamese-senses-plain.md, pi-4-…, pi-3-…, pi-2-… and pi-1-… (grep each headword; 286 of pi-6's 1,126 headwords have a line in one of them, 23 of the 91 sample headwords). Reuse their tag wording and splits where the Vietnamese values match (pi-5, then pi-4, pi-3, pi-2, pi-1); add senses only for values they do not have.
  - 0-INBOX\temp\pipeline\pi-5-vi-ai\senses\senses-conventions.md, pi-4-vi-ai\senses\senses-conventions.md, pi-3-vi-ai\senses\senses-conventions.md, pi-2-vi-ai\senses\senses-conventions.md and pi-1-vi-ai\senses\senses-conventions.md (split/merge conventions and family tags: variants of one Vietnamese expression with/without «sự», a classifier, a tense/aspect word or «có» are ONE sense).
  - 0-INBOX\temp\pipeline\pi-5-vi-ai\senses\senses_tool_vi.py (build|verify|todo|show|words|prior|reuse|sample) and pi-5 decisions-sample.txt (the decisions format).
  - 0-INBOX\temp\pipeline\pi-1-vi-ai\termbase\APPROVED.md … pi-5-vi-ai\termbase\APPROVED.md (the user's term decisions).
- **The pi-6 English senses of this same book** (which pi-6 headwords have more than one meaning; English tag wording): AI_translation\english\pi-6-pali-word-english-senses-plain.md (grep each headword). Reuse its English tags word for word where the meaning is the same and pi-1 … pi-5 Vietnamese have no line. There is no Russian pi-6.
- The pi-6 keyword-map conventions (why one Pāli word has several Vietnamese values): 0-INBOX\temp\pipeline\pi-6-vi-ai\mapper-vi\vi-map-conventions-pi6.md, map-coordinator-rules.md, notes-map-*.md, crosscheck-values.tsv (52 keywords with more than one value).

## Input
0-INBOX\temp\pipeline\pi-6-vi-ai\senses\agg-part<K>.tsv (K = 1..5, about 226 headwords each; the sample uses agg-sample.tsv: the first 90 rows of part 1 plus the one further multi-value row, 91 rows, last headword «saṅkhārā»). One line per Pāli headword (case merged, order = first appearance in the map; the literal placeholder keyword "(no direct equivalent)" is not a headword):
`headword <TAB> en≈ English hints <TAB> vietnamese_value=count[example ids] | … <TAB> NDE=<count>`
Column 2 is only a HINT.

## Output
senses\part<K>-senses.md (the sample: sample-senses.md), same headwords, same order, one line each:
`pali: {english sense tag: tiếng Việt a / tiếng Việt b; tag2: tiếng Việt c}`

## Guidance
- EVERY headword needs a real English tag: a short gloss of the meaning, with the grammatical role where useful. Never copy a Vietnamese value or the bare English hint as the tag. A script may draft tags from a table you write, but you write that table yourself, headword by headword (copying a pi-1 … pi-5 Vietnamese or pi-6 English tag for the same headword and sense is fine).
- Variants of ONE Vietnamese expression go in ONE sense, joined with " / ", most frequent first (with/without nominaliser, classifier, aspect word, «có», «khi» / «trong khi» / «sau khi» on participles and gerunds, letter case; heading «Các cặp câu hỏi về …» vs closer «các cặp câu hỏi về …»).
- **The Yamaka's tense / polarity variants are ONE sense** per verb form: the map gives a verb the polarity of its first rendering in the segment (map-coordinator-rules.md), so uppajjissati has «sẽ sinh khởi» / «sẽ … sinh khởi», uppajjittha «đã sinh khởi» / «chưa từng sinh khởi», parijānissanti «sẽ …» / «vẫn sẽ …», and so on for nirujjhati, parijānāti, pajahati, bhāveti, sacchikaroti, paṭilabhati. One sense each, the variants as " / " candidates, most frequent first.
- **Position variants are ONE sense:** plane-beings «chúng sinh trong cõi X» / «cõi X» (kāmāvacarānaṃ, rūpāvacarānaṃ, arūpānaṃ, pañcavokārānaṃ); Itaresaṃ «người khác» / «chúng sinh khác»; kusalā dhammā «hiện tượng thiện» / «hiện tượng … thiện»; upapajjitvā «sau khi tái sinh» / «tái sinh».
- Synonyms for the SAME meaning go in ONE sense as candidates (the termbase step picks one).
- Split only for genuinely different meanings. Known real splits in pi-6: dukkha «khổ đau» (the truth of suffering, Saccayamaka) vs «sự khó chịu» (bodily pain, the faculty, Indriyayamaka); rūpadhātu «yếu tố hình sắc» (an element, Dhātuyamaka) vs rūpadhātuyā «cõi hình sắc» (a plane, Anusayayamaka); hetu «nguyên nhân» (hetuvāra series) vs «gốc rễ» (sahetuka / ahetuka); samuṭṭhāna «do … sinh ra» (beside rūpaṃ) vs «nguồn gốc» (the hetuvāra series); mūla «gốc rễ» vs mūlamūla «cội rễ»; kusalaṃ «thiện» (predicate) vs «hiện tượng thiện» (subject) — check whether this is a sense split or a variant of one expression (the sample decides). Earlier books' splits stay (their senses-conventions.md). When unsure, look at the segments by their example ids in AI_translation\vietnamese\pi-6-vietnamese-plain-zeroshot_split_chapters\ and AI_translation\pali\pi-6_split_chapters\ (grep the named chapter file).
- Values containing " … " are kept as written; each is one candidate.
- A single candidate must not contain "; " or "/" except as the separator " / ". If an attested value contains " / ", write it with " và " and note it.
- NDE occurrences are excluded; don't add "(no direct equivalent)".

## Sample only: also write (for the later parts)
- senses\senses-conventions.md: only what pi-6 adds or changes against the pi-5 … pi-1 Vietnamese conventions, with the tags of the recurring pi-6 headword families (the root compounds mūla / mūlamūla / -mūlaka / eka- / aññamañña-; the pair-question frame words ye keci / sabbe te / ye vā pana; āmantā, tīṇeva, avasesā; the verbs uppajjati / nirujjhati / anuseti / pajahati / parijānāti / bhāveti / sacchikaroti and their tense / polarity variants; the members of each yamaka (khandha, āyatana, dhātu, sacca, saṅkhāra, anusaya, citta, dhamma, indriya); the planes and beings; the persons; the section-heading words).
- senses\senses_tool_vi.py: the pi-5 tool adapted to pi-6 paths, `build|verify|todo|show|words|sample --part K` (K = 1..5), and `prior` printing the pi-5, pi-4, pi-3, pi-2 and pi-1 Vietnamese and the pi-6 English senses lines for the headwords of a part. Write your decisions to senses\decisions-sample.txt and build with it.

## Parts 1-5 (after the sample is approved): binding
Five agents work at the same time, one part each. Use senses\senses-conventions.md and senses_tool_vi.py READ-ONLY (call, don't edit; in PowerShell write `-` for "any value"). Write decisions to senses\decisions-part<K>.txt and build with the tool. Part 1 contains the sample headwords: copy their decisions from decisions-sample.txt unchanged. The same headword family gets the same tag wording as in the sample. For every headword that pi-1 … pi-5 Vietnamese has, run `prior` and keep that tag where the Vietnamese values match.

## Verify (skill step 6) with the tool
Headword list equals the input's, same order, no duplicates; every attested Vietnamese value appears under its headword (allowing " / "→" và "); no tag equals its value; every line parses as `hw: {tag: v / v; tag: v}`. Print counts and differences.

## Report (under 400 words, as text)
Headword count and verification result; how many headwords have more than one sense; how many senses have more than one candidate; how many lines reuse a pi-1 … pi-5 Vietnamese tag; the conventions you settled; 10-15 example lines for review (including the multi-sense ones); anything genuinely unclear.
