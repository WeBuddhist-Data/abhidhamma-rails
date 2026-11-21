# Brief: word-sense-grouper, Pāli→Vietnamese, pi-5 (Kathāvatthu)

Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write/Edit tools for files (write scripts with the Write tool at their full paths; never write any file from PowerShell, not even a temporary list), PowerShell for commands, `python -I -X utf8 -B` (-B: no __pycache__). Write ONLY your own files (named below), plus helper scripts named after your part, in 0-INBOX\temp\pipeline\pi-5-vi-ai\senses\, with LF line endings. Never create files at the repo root or in a system temp folder. Do not touch 1-SOURCES\ or 4-SYSTEM\, do not edit any pi-1 … pi-4 file, never run git (not even git status), never write "seed". No web. You cannot write report files for me: return your report as text.

## FORBIDDEN (copyrighted reference translation)
Never open, grep or search: 1-SOURCES\Translations\Vietnamese\ (any file), 0-INBOX\raw-data\vi-*, 0-INBOX\temp\pipeline\pi-1-vi\, pi-2-vi\, pi-3-4-vi\, pi-5-vi\, pi-6-vi\, pi-7-vi\, pi-1-th-vi\, vi-tools\. No folder-wide searches over 0-INBOX\temp\pipeline\, 1-SOURCES\ or AI_translation\: Grep only the specific files named here.

## Read first
- AI_translation\skills\word-sense-grouper.md, and follow it exactly.
- 0-INBOX\temp\pipeline\vietnamese-style.md (core terms, pairs that must stay distinct; sati = «sự tỉnh thức»).
- **The approved Vietnamese runs of pi-1 … pi-4 (binding where pi-5 has the same headword in the same sense):**
  - AI_translation\vietnamese\pi-4-pali-word-vietnamese-senses-plain.md, pi-3-…, pi-2-… and pi-1-… (grep each headword; 1,700 of pi-5's 5,443 headwords have a line in one of them, 50 of the 120 sample headwords). Reuse their tag wording and splits where the Vietnamese values match (pi-4, then pi-3, pi-2, pi-1); add senses only for values they do not have.
  - 0-INBOX\temp\pipeline\pi-4-vi-ai\senses\senses-conventions.md, pi-3-vi-ai\senses\senses-conventions.md, pi-2-vi-ai\senses\senses-conventions.md and pi-1-vi-ai\senses\senses-conventions.md (split/merge conventions and family tags: variants of one Vietnamese expression with/without «sự», a classifier, a tense/aspect word or «có» are ONE sense).
  - 0-INBOX\temp\pipeline\pi-4-vi-ai\senses\senses_tool_vi.py (build|verify|todo|show|words|prior|reuse|sample) and pi-4 decisions-sample.txt (the decisions format).
  - 0-INBOX\temp\pipeline\pi-1-vi-ai\termbase\APPROVED.md … pi-4-vi-ai\termbase\APPROVED.md (the user's term decisions).
- **The approved pi-5 Russian senses of this same book** (which pi-5 headwords have more than one meaning; English tag wording): AI_translation\russian\pi-5-pali-word-russian-senses-plain.md (grep each headword). Reuse its English tags word for word where the meaning is the same and pi-1 … pi-4 Vietnamese have no line.
- pi-5 English senses AI_translation\english\pi-5-pali-word-english-senses-plain.md: tag wording hint only.
- The pi-5 keyword-map conventions (why one Pāli word has several Vietnamese values): 0-INBOX\temp\pipeline\pi-5-vi-ai\mapper-vi\vi-map-conventions-pi5.md, map-coordinator-rules.md, notes-map-*.md, crosscheck-values.tsv.

## Input
0-INBOX\temp\pipeline\pi-5-vi-ai\senses\agg-part<K>.tsv (K = 1..6, about 908 headwords each; the sample uses agg-sample.tsv: the first 90 rows of part 1 plus the next 30 multi-value rows, 120 rows, last headword «pathavī»). One line per Pāli headword (case merged, order = first appearance in the map):
`headword <TAB> en≈ English hints <TAB> vietnamese_value=count[example ids] | … <TAB> NDE=<count>`
Column 2 is only a HINT.

## Output
senses\part<K>-senses.md (the sample: sample-senses.md), same headwords, same order, one line each:
`pali: {english sense tag: tiếng Việt a / tiếng Việt b; tag2: tiếng Việt c}`

## Guidance
- EVERY headword needs a real English tag: a short gloss of the meaning, with the grammatical role where useful. Never copy a Vietnamese value or the bare English hint as the tag. A script may draft tags from a table you write, but you write that table yourself, headword by headword (copying a pi-1 … pi-4 Vietnamese or pi-5 Russian tag for the same headword and sense is fine).
- Variants of ONE Vietnamese expression go in ONE sense, joined with " / ", most frequent first (with/without nominaliser, classifier, aspect word, «có», «khi» / «trong khi» / «sau khi» on participles and gerunds, «điều» on method nouns, letter case).
- Synonyms for the SAME meaning go in ONE sense as candidates (the termbase step picks one).
- Split only for genuinely different meanings. Context splits in the pi-5 map (mapper-vi\crosscheck-values.tsv: 450 keywords with more than one value; most are variants of one expression or fragments, not separate meanings). Known real splits: niggaha «sự bác bỏ» (the debate's rebuttal) vs «sự chế ngự» (restraining the mind, ch24 / ch31); vata «chắc chắn» (vata re) vs «nghi thức» (sīlabbata) vs «quả thật»; micchā «sai» (verdict) vs «sai lầm» (path factors); eva («thật» in Attheva suttanto, «chỉ», «ngay», «cũng», «chính»); sukha «hạnh phúc» vs «dễ chịu»; dukkha «khổ đau» vs «khó chịu»; dhamma «hiện tượng» / «Giáo Pháp» / «đối tượng của ý» / «hành vi» / «lẽ phải»; rūpa «vật chất» vs «hình sắc» vs «cõi hình sắc»; dhātu «yếu tố» vs «cõi»; sammā «đúng đắn» vs «Hoàn Toàn» (sammāsambuddha); hetu «gốc rễ» vs «nguyên nhân». Earlier books' splits stay (their senses-conventions.md). When unsure, look at the segments by their example ids in AI_translation\vietnamese\pi-5-vietnamese-plain-zeroshot_split_chapters\ and AI_translation\pali\pi-5_split_chapters\ (grep the named chapter file).
- Values containing " … " are kept as written; each is one candidate.
- A single candidate must not contain "; " or "/" except as the separator " / ". If an attested value contains " / ", write it with " và " and note it.
- NDE occurrences are excluded; don't add "(no direct equivalent)".

## Sample only: also write (for the later parts)
- senses\senses-conventions.md: only what pi-5 adds or changes against the pi-4 … pi-1 Vietnamese conventions, with the tags of the recurring pi-5 headword families (the debate formula words: āmantā, nanu, ājānāhi, niggaha / paṭikamma, micchā, saccikaṭṭha / paramattha, upalabbhati, sakavādī / paravādī, the -ti / nu question particles, atthi «tồn tại»; the atīta / anāgata / paccuppanna family; the a-/an- negatives; the person words).
- senses\senses_tool_vi.py: the pi-4 tool adapted to pi-5 paths, `build|verify|todo|show|words|sample --part K` (K = 1..6), and `prior` printing the pi-4, pi-3, pi-2 and pi-1 Vietnamese and the pi-5 Russian senses lines for the headwords of a part. Write your decisions to senses\decisions-sample.txt and build with it.

## Parts 1-6 (after the sample is approved): binding
Three agents work at the same time, one part each (rolling). Use senses\senses-conventions.md and senses_tool_vi.py READ-ONLY (call, don't edit; in PowerShell write `-` for "any value"). Write decisions to senses\decisions-part<K>.txt and build with the tool. Part 1 contains the sample headwords: copy their decisions from decisions-sample.txt unchanged. The same headword family gets the same tag wording as in the sample. For every headword that pi-1 … pi-4 Vietnamese has, run `prior` and keep that tag where the Vietnamese values match.

## Verify (skill step 6) with the tool
Headword list equals the input's, same order, no duplicates; every attested Vietnamese value appears under its headword (allowing " / "→" và "); no tag equals its value; every line parses as `hw: {tag: v / v; tag: v}`. Print counts and differences.

## Report (under 400 words, as text)
Headword count and verification result; how many headwords have more than one sense; how many senses have more than one candidate; how many lines reuse a pi-1 … pi-4 Vietnamese tag; the conventions you settled; 10-15 example lines for review (including the multi-sense ones); anything genuinely unclear.
