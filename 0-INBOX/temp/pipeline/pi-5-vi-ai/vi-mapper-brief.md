# Brief: Pāli→Vietnamese keyword mapping, pi-5 (Kathāvatthu): ONE chapter

Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write/Edit tools for files (write scripts with the Write tool at full paths under D:\Work\OpenPecha\abhidhamma-rails; never write files from PowerShell), PowerShell for commands, `python -I -X utf8 -B` (-B: write no __pycache__). Write ONLY these files inside 0-INBOX\temp\pipeline\pi-5-vi-ai\mapper-vi\, with LF line endings: `<part>.mapped.md`, `map_<N>_vi.py`, `notes-map-<N>.md` (N = your chapter number). Never create files at the repo root or in a system temp folder. Do not touch 1-SOURCES\ or 4-SYSTEM\, do not edit the translation or any other agent's files (map_common_vi.py, map_sample_vi.py, check_parts_vi.py and vi-map-conventions-pi5.md are READ-ONLY), never run git (not even git status), never write "seed". No web. You cannot write report files for me: return your report as text.

The user approved the map sample (preamble, 1-puggalakatha) on 2026-11-21, including its open calls as built (the presence check counts translated editorial brackets and variant labels as text; pathavī «địa» out of «đại địa»; «như một» kept in saccikaṭṭhaparamatthena; locatives as the text has them; discontinuous values with " … "; participles keep «khi»). **Three agents work at the same time, one chapter each.** Copy the sample's conventions exactly; same keyword in the same Vietnamese = same value.

## FORBIDDEN (copyrighted reference translation)
Never open, grep or search: 1-SOURCES\Translations\Vietnamese\ (any file), 0-INBOX\raw-data\vi-*, 0-INBOX\temp\pipeline\pi-1-vi\, pi-2-vi\, pi-3-4-vi\, pi-5-vi\, pi-6-vi\, pi-7-vi\, pi-1-th-vi\, vi-tools\. No folder-wide searches over 0-INBOX\temp\pipeline\, 1-SOURCES\ or AI_translation\: Grep only the specific files named here.

## Read first (binding)
- AI_translation\skills\keyword-equivalence-mapper.md; 0-INBOX\temp\pipeline\vietnamese-style.md.
- Conventions, in this order: 0-INBOX\temp\pipeline\pi-1-vi-ai\mapper-vi\vi-map-conventions.md, pi-2-vi-ai\mapper-vi\vi-map-conventions-pi2.md, pi-3-vi-ai\mapper-vi\vi-map-conventions-pi3.md, pi-4-vi-ai\mapper-vi\vi-map-conventions-pi4.md, pi-5-vi-ai\mapper-vi\vi-map-conventions-pi5.md (approved: the debate-formula values, two-word keywords in Vietnamese order keeping an inner «là», head noun before its genitive).
- Tooling: import 0-INBOX\temp\pipeline\pi-5-vi-ai\mapper-vi\map_common_vi.py and map_sample_vi.py READ-ONLY (`sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai\mapper-vi")`); use map_sample_vi.FORMULAS for every recurring debate frame; write map_<N>_vi.py that reuses their tables and adds yours. Importing must not rewrite any mapped file.
- Finished chapters of other pi-5 map agents (map_<M>_vi.py, notes-map-<M>.md, <part>.mapped.md in the same folder) may be read and must be followed for identical Pāli and Vietnamese.
- The pi-1 … pi-4 Vietnamese keyword maps (AI_translation\vietnamese\pi-N-keywords-by-reference-pali-vietnamese-plain.md) for cross-book keywords (grep, do not read whole).
- Meaning cross-check only: AI_translation\russian\pi-5-keywords-by-reference-pali-russian-plain.md, AI_translation\english\pi-5-keywords-by-reference-pali-english-plain.md (grep by block ID).

## Your chapter
- Keywords: mapper-vi\<part>.keywords.md (`[id] kw1, kw2, …`).
- Vietnamese: AI_translation\vietnamese\pi-5-vietnamese-plain-zeroshot_split_chapters\<part>.md: final for this step (harmonised); the TRANSLATION FILE is the truth (build_<N>_vi.py, notes-<N>.md and harmonise-log.tsv in pi-5-vi-ai\ help explain it).
- Pāli: AI_translation\pali\pi-5_split_chapters\<part>.md.
- Output: mapper-vi\<part>.mapped.md: same lines, same order, same Pāli keywords in the same order, each `pāli=tiếng Việt`.
- New recurring keywords and values: notes-map-<N>.md, one per line.

## Rules (user-approved)
- For each keyword, the word or phrase in THAT segment's Vietnamese that carries its meaning, copied as it stands there, in the approved value form.
- Keep keywords exactly as given. Never add, drop, merge or reorder.
- `(no direct equivalent)` only as the conventions define it.
- Compare each segment for real; identical formulaic segments get identical mappings.
- No ", " inside a value.

## Verify
`python -I -X utf8 -B 0-INBOX\temp\pipeline\pi-5-vi-ai\mapper-vi\check_parts_vi.py <part>`: `bad []`, presence misses 0 (or listed exceptions with reasons); the sample mapped files, other finished chapters and earlier books' maps unchanged.

## Report (under 300 words, as text)
Line count, verifier result, number of (no direct equivalent), presence result; new values (notes file); unclear mappings.
