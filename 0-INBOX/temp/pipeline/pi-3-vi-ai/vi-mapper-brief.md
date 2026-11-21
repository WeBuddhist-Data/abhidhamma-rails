# Brief: Pāli→Vietnamese keyword mapping, pi-3 (Dhātukathā): ONE chapter

Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write/Edit tools for files (write scripts with the Write tool at full paths; never write files from PowerShell), PowerShell for commands, `python -I -X utf8`. Write ONLY these files inside 0-INBOX\temp\pipeline\pi-3-vi-ai\mapper-vi\: `<part>.mapped.md`, `map_<N>_vi.py`, `notes-map-<N>.md` (N = your chapter number). Never create files at the repo root or in a system temp folder. Do not touch 1-SOURCES\ or 4-SYSTEM\, do not edit the translation or any other agent's files (map_common_vi.py, map_sample_vi.py, check_parts_vi.py and vi-map-conventions-pi3.md are READ-ONLY), never run git (not even git status), never write "seed". No web. You cannot write report files for me: return your report as text.

The user approved the map sample (preamble, 1-uddeso, 2-pathamanayo) on 2026-11-20. **Three agents work at the same time, one chapter each.** Copy the sample's conventions exactly; same keyword in the same Vietnamese = same value.

## FORBIDDEN (copyrighted reference translation)
Never open, grep or search: 1-SOURCES\Translations\Vietnamese\ (any file), 0-INBOX\raw-data\vi-*, 0-INBOX\temp\pipeline\pi-1-vi\, pi-2-vi\, pi-3-4-vi\, pi-5-vi\, pi-6-vi\, pi-7-vi\, pi-1-th-vi\, vi-tools\. No folder-wide searches over 0-INBOX\temp\pipeline\, 1-SOURCES\ or AI_translation\: Grep only the specific files named here.

## Read first (binding)
- AI_translation\skills\keyword-equivalence-mapper.md; 0-INBOX\temp\pipeline\vietnamese-style.md.
- Conventions, in this order: 0-INBOX\temp\pipeline\pi-1-vi-ai\mapper-vi\vi-map-conventions.md, 0-INBOX\temp\pipeline\pi-2-vi-ai\mapper-vi\vi-map-conventions-pi2.md, 0-INBOX\temp\pipeline\pi-3-vi-ai\mapper-vi\vi-map-conventions-pi3.md (approved; its "proposed" items for ye dhammā, te dhammā, …saṅgahena, kehici: use them unless the text shows they do not fit, then say so).
- Tooling: import 0-INBOX\temp\pipeline\pi-3-vi-ai\mapper-vi\map_common_vi.py and map_sample_vi.py READ-ONLY (`sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-3-vi-ai\mapper-vi")`); write map_<N>_vi.py that reuses their tables and adds yours. Importing must not rewrite any mapped file.
- Finished chapters of other pi-3 map agents (map_<M>_vi.py, notes-map-<M>.md, <part>.mapped.md in the same folder) may be read and must be followed for identical Pāli and Vietnamese.
- The pi-1 / pi-2 Vietnamese keyword maps (AI_translation\vietnamese\pi-1-keywords-by-reference-pali-vietnamese-plain.md, pi-2-keywords-by-reference-pali-vietnamese-plain.md) for cross-book keywords (grep, do not read whole).
- Meaning cross-check only: AI_translation\russian\pi-3-keywords-by-reference-pali-russian-plain.md, AI_translation\english\pi-3-keywords-by-reference-pali-english-plain.md (grep by block ID).

## Your chapter
- Keywords: mapper-vi\<part>.keywords.md (`[id] kw1, kw2, …`).
- Vietnamese: AI_translation\vietnamese\pi-3-vietnamese-plain-zeroshot_split_chapters\<part>.md: final for this step (harmonised); the TRANSLATION FILE is the truth (builders build_<N>_vi.py and harmonise-log.tsv in pi-3-vi-ai\ help explain it).
- Pāli: AI_translation\pali\pi-3_split_chapters\<part>.md.
- Output: mapper-vi\<part>.mapped.md: same lines, same order, same Pāli keywords in the same order, each `pāli=tiếng Việt`.
- New recurring keywords and values: notes-map-<N>.md, one per line.

## Rules (user-approved)
- For each keyword, the word or phrase in THAT segment's Vietnamese that carries its meaning, copied as it stands there, in the approved value form.
- Keep keywords exactly as given. Never add, drop, merge or reorder.
- `(no direct equivalent)` only as the conventions define it.
- Compare each segment for real; identical formulaic segments get identical mappings.
- No ", " inside a value.

## Verify
`python -I -X utf8 0-INBOX\temp\pipeline\pi-3-vi-ai\mapper-vi\check_parts_vi.py <part>`: `bad []`, presence misses 0 (or listed exceptions with reasons); the sample mapped files and other finished chapters unchanged.

## Report (under 300 words, as text)
Line count, verifier result, number of (no direct equivalent), presence result; new values (notes file); unclear mappings.
