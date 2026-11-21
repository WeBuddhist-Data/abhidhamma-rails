# Brief: Pāli→Vietnamese keyword mapping, pi-4 (Puggalapaññatti): SAMPLE

Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write/Edit tools for files (write scripts with the Write tool at full paths under D:\Work\OpenPecha\abhidhamma-rails; never write files from PowerShell), PowerShell for commands, `python -I -X utf8`. Write ONLY inside 0-INBOX\temp\pipeline\pi-4-vi-ai\mapper-vi\. Never create files at the repo root, outside the repo or in a system temp folder. Do not touch 1-SOURCES\ or 4-SYSTEM\, do not edit the translation, never run git (not even git status), never write "seed". No web. You cannot write report files for me: return your report as text.

This sample (preamble, 1-matika, 2-ekakapuggalapannatti) is what the user reviews before the remaining chapters are mapped (three agents at a time, one chapter each). It carries the approved pi-1 / pi-2 / pi-3 conventions into pi-4 and sets what the later agents copy.

## FORBIDDEN (copyrighted reference translation)
Never open, grep or search: 1-SOURCES\Translations\Vietnamese\ (any file), 0-INBOX\raw-data\vi-*, 0-INBOX\temp\pipeline\pi-1-vi\, pi-2-vi\, pi-3-4-vi\, pi-5-vi\, pi-6-vi\, pi-7-vi\, pi-1-th-vi\, vi-tools\. No folder-wide searches over 0-INBOX\temp\pipeline\, 1-SOURCES\ or AI_translation\: Grep only the specific files named here.

## Read first (binding)
- AI_translation\skills\keyword-equivalence-mapper.md (the skill you execute); 0-INBOX\temp\pipeline\vietnamese-style.md.
- **The user-approved map conventions:** 0-INBOX\temp\pipeline\pi-1-vi-ai\mapper-vi\vi-map-conventions.md, 0-INBOX\temp\pipeline\pi-2-vi-ai\mapper-vi\vi-map-conventions-pi2.md, 0-INBOX\temp\pipeline\pi-3-vi-ai\mapper-vi\vi-map-conventions-pi3.md (and their notes-map-*.md). Binding for pi-4: value form (frame words «các» / «những», existential «có», predicate «là» dropped; nominalisers kept as the text has them), discontinuous values with " … ", compounds and members, fragments that lost a negative prefix = the positive Vietnamese word, `(no direct equivalent)` only as defined there, two-word keywords valued in the Vietnamese order as it stands (pi-3 coordinator decision).
- The pi-3 tooling: 0-INBOX\temp\pipeline\pi-3-vi-ai\mapper-vi\map_common_vi.py, map_sample_vi.py, map_15_vi.py, check_parts_vi.py. Import them READ-ONLY (`sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-3-vi-ai\mapper-vi")`); their path constants point at pi-3, so write a pi-4 common module (below) that reuses the functions and tables with pi-4 paths. Importing must not rewrite any pi-1 / pi-2 / pi-3 output (hash the earlier mapped files before and after).
- The pi-1 / pi-2 / pi-3 Vietnamese keyword maps (AI_translation\vietnamese\pi-N-keywords-by-reference-pali-vietnamese-plain.md): same Pāli with the same Vietnamese = same value.
- Meaning cross-check only: AI_translation\russian\pi-4-keywords-by-reference-pali-russian-plain.md, AI_translation\english\pi-4-keywords-by-reference-pali-english-plain.md (grep by block ID).

## Per part (preamble, 1-matika, 2-ekakapuggalapannatti)
- Keywords (Pāli): 0-INBOX\temp\pipeline\pi-4-vi-ai\mapper-vi\<part>.keywords.md, `[id] kw1, kw2, …`.
- Vietnamese translation: AI_translation\vietnamese\pi-4-vietnamese-plain-zeroshot_split_chapters\<part>.md: final for this step (harmonised); do not edit it. The TRANSLATION FILE is the truth (the builders build_sample_vi.py and harmonise-log.tsv in pi-4-vi-ai\ help explain it).
- Pāli source, for context: AI_translation\pali\pi-4_split_chapters\<part>.md.
- Output: mapper-vi\<part>.mapped.md: same lines, same order, same Pāli keywords in the same order, each `pāli=tiếng Việt`.

## Also write (for the later agents)
- mapper-vi\map_common_vi.py (pi-4): pi-4 paths; reuses the pi-3 functions and tables; build_part(), verify().
- mapper-vi\vi-map-conventions-pi4.md: only what pi-4 adds or changes (the person-type names and their members, puggala «người» / «hạng người», paññatti «sự định danh», the definition frame words Katamo / Idhekacco / vuccati, the similes), so later agents read pi-1 + pi-2 + pi-3 + this file.
- mapper-vi\map_sample_vi.py: your table plus per-segment overrides for the three parts.
- mapper-vi\check_parts_vi.py (pi-4 paths; as pi-3's).

## Rules (user-approved)
- For each keyword, the word or phrase in THAT segment's Vietnamese that carries its meaning, copied as it stands there, in the approved value form.
- Keep keywords exactly as given. Never add, drop, merge or reorder.
- `(no direct equivalent)` only as the conventions define it.
- Compare each segment for real; identical formulaic segments get identical mappings.
- No ", " inside a value.

## Verify
`python -I -X utf8 0-INBOX\temp\pipeline\pi-4-vi-ai\mapper-vi\check_parts_vi.py preamble 1-matika 2-ekakapuggalapannatti`: structural `bad []` per part and the presence check (every value found in that segment's Vietnamese; exceptions listed with reasons). Earlier books' mapped files hash-unchanged.

## Report (under 400 words, as text)
Per part: line count, verifier result, number of (no direct equivalent), presence result. What pi-4 adds to the conventions. 10-15 example mappings for review. Genuinely unclear mappings.
