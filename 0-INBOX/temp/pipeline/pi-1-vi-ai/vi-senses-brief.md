# Brief: word-sense-grouper, Pāli→Vietnamese, pi-1 (Dhammasaṅgaṇī)

Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write tools for files (write scripts with the Write tool, never via a shell redirect), PowerShell for commands, `python -I -X utf8`. Write ONLY your own part files, plus helper scripts named after your part, in 0-INBOX\temp\pipeline\pi-1-vi-ai\senses\. Never create files at the repo root or in a system temp folder. Do not touch 1-SOURCES\ or 4-SYSTEM\, never run git (not even git status), never write "seed". You cannot write report files for me: return your report as text.

## FORBIDDEN (copyrighted reference translation)
Never open, grep or search: 1-SOURCES\Translations\Vietnamese\vi-*.md, 0-INBOX\raw-data\vi-*, 0-INBOX\temp\pipeline\pi-1-vi\, pi-2-vi\, pi-3-4-vi\, pi-5-vi\, pi-6-vi\, pi-7-vi\, pi-1-th-vi\, vi-tools\. No folder-wide searches over 0-INBOX\temp\pipeline\, 1-SOURCES\ or AI_translation\.

## Read first
- AI_translation\skills\word-sense-grouper.md, and follow it exactly.
- 0-INBOX\temp\pipeline\vietnamese-style.md (Vietnamese conventions, approved core terms, the review lessons on pairs that must stay distinct; sati = «sự tỉnh thức»).
- The keyword map conventions: 0-INBOX\temp\pipeline\pi-1-vi-ai\mapper-vi\vi-map-conventions.md and notes-map-*.md (they explain why one Pāli word has several Vietnamese values: segment wording, nominaliser «sự» kept or dropped, fragments, gapped values).
- **The closest model, the user-approved Russian senses of this same book:** AI_translation\russian\pi-1-pali-word-russian-senses-plain.md (grep it for each headword you meet), 0-INBOX\temp\pipeline\pi-1-ru\senses\senses-conventions.md (how pi-1's headwords were split: rūpa, dhamma, kāya, citta/mano, the matrix items, the synonym strings), senses_tool_ru.py and decisions-sample.txt (the build-from-decisions + verify tool). **Reuse the Russian file's English tags word for word wherever the Pāli headword has the same meaning**; the split into senses follows the meanings, which are the same in both languages, while the candidates are the Vietnamese values.

## Input
0-INBOX\temp\pipeline\pi-1-vi-ai\senses\agg-part<K>.tsv (the sample uses agg-sample.tsv = the first 120 headwords of part 1). One line per Pāli headword (case merged, order = first appearance in the map):
`headword <TAB> en≈ English hints <TAB> vietnamese_value=count[example ids] | … <TAB> NDE=<count>`
Column 2 is only a HINT (the English equivalents the English pi-1 map gives that headword).

## Output
0-INBOX\temp\pipeline\pi-1-vi-ai\senses\part<K>-senses.md (the sample: sample-senses.md), same headwords, same order, one line each:
`pali: {english sense tag: tiếng Việt a / tiếng Việt b; tag2: tiếng Việt c}`

## Guidance
- EVERY headword needs a real English tag: a short gloss of the meaning, with the grammatical role where useful. Never copy a Vietnamese value or the bare English hint as the tag. A script may draft tags from a table you write, but you write that table yourself, headword by headword (the Russian file gives most of them).
- Vietnamese has no inflection. Variants of ONE Vietnamese expression go in ONE sense, joined with " / ", most frequent first: with or without the nominaliser or classifier («sự hoài nghi» / «hoài nghi», «loại hạn hẹp» / «hạn hẹp», «sự bình thản» / «bình thản»), with or without a tense/aspect word («sinh khởi» / «đã sinh khởi» / «đang sinh khởi»), with or without «có» (having).
- Synonyms for the SAME meaning go in ONE sense as candidates (the termbase step picks one).
- Split into separate senses only for genuinely different meanings, as the Russian file does: e.g. rūpa as vật chất (material form) vs hình sắc (visible object) vs cõi hình sắc (the fine-material sphere); dhamma as hiện tượng vs đối tượng của ý vs Giáo Pháp; kāya as thân tinh thần (mental body) vs thân (physical body); dukkha as khó chịu (painful feeling) vs khó khăn (difficult, of practice) vs sự đau khổ / khổ đau (suffering); sukha as hạnh phúc / dễ chịu vs dễ dàng (easy, of practice). When unsure, look at the segments by their example ids in AI_translation\vietnamese\pi-1-vietnamese-plain-zeroshot_split_chapters\ and AI_translation\pali\pi-1_split_chapters\.
- Values containing " … " (gapped phrases) are kept as written; each is one candidate.
- A single candidate must not contain "; " or "/" except as the separator " / ". If an attested value contains " / ", write it with " và " instead and note it in the report.
- NDE occurrences are already excluded; don't add "(no direct equivalent)".

## Parts 1–4 (after the sample): binding
The user approved the sample (senses\sample-senses.md, decisions-sample.txt) on 2026-11-18, judgement calls included («hình sắc» under both rūpa senses; one combined sense for kāya / sukhaṃ / cittaṃ / kāma where the Vietnamese uses one value; «mạng sống» merged into jīvita, «có niềm tin» into saddhā). The parts run ONE AT A TIME, so read the finished earlier parts' decisions files too and keep their tags and splits for the same families.
- senses\senses-conventions.md (READ-ONLY) and senses\senses_tool_vi.py (`build|verify|todo|show|ru|words --part K`; READ-ONLY, call it, don't edit it). Write your decisions to senses\decisions-part<K>.txt and build with the tool.
- Part 1 contains the 120 sample headwords: copy their decisions from decisions-sample.txt unchanged.
- The same headword family gets the same tag wording as in the sample and earlier parts (X-indriyaṃ, X-balaṃ, citta-X, a-/an- negatives, the matrix items), and the Russian pi-1 senses file's tags wherever the meaning is the same.

## Sample only: also write (for the later agents)
- senses\senses-conventions.md: the split/merge conventions you settled for pi-1 Vietnamese (modelled on the Russian file), with the tags of the recurring headword families.
- senses\senses_tool_vi.py: build `<out>-senses.md` from a decisions file you write (decisions-<part>.txt) and verify it; usable by later agents with `--part K` (adapt senses_tool_ru.py).

## Verify (skill step 6) with a script
The headword list of your output equals the input's, same order, no duplicates; every attested Vietnamese value appears under its headword (allowing the " / "→" và " rewrite); no tag equals its value; every line parses as `hw: {tag: v / v; tag: v}`. Print counts and differences.

## Report (under 400 words, as text)
Headword count and verification result; how many headwords have more than one sense; how many senses have more than one candidate; the conventions you settled; 10–15 example lines for review (including the multi-sense ones); anything genuinely unclear.
