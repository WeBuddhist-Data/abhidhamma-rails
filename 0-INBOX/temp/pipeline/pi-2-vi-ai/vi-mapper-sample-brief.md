# Brief: Pāli→Vietnamese keyword mapping, pi-2 (Vibhaṅga): SAMPLE

Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write/Edit tools for files (write scripts with the Write tool at full paths; never write files from PowerShell), PowerShell for commands, `python -I -X utf8`. Write ONLY inside 0-INBOX\temp\pipeline\pi-2-vi-ai\mapper-vi\. Never create files at the repo root or in a system temp folder. Do not touch 1-SOURCES\ or 4-SYSTEM\, do not edit the translation, never run git (not even git status), never write "seed". You cannot write report files for me: return your report as text.

This sample (preamble, 1-khandhavibhango) is what the user reviews before the remaining chapters are mapped (one agent at a time). It carries the approved pi-1 conventions into pi-2 and sets what the later agents copy.

## FORBIDDEN (copyrighted reference translation)
Never open, grep or search: 1-SOURCES\Translations\Vietnamese\ (any file), 0-INBOX\raw-data\vi-*, 0-INBOX\temp\pipeline\pi-1-vi\, pi-2-vi\, pi-3-4-vi\, pi-5-vi\, pi-6-vi\, pi-7-vi\, pi-1-th-vi\, vi-tools\. No folder-wide searches over 0-INBOX\temp\pipeline\, 1-SOURCES\ or AI_translation\.

## Read first (binding)
- AI_translation\skills\keyword-equivalence-mapper.md (the skill you execute).
- 0-INBOX\temp\pipeline\vietnamese-style.md (Vietnamese conventions, core terms, sati = «sự tỉnh thức»).
- **The user-approved pi-1 Vietnamese map conventions (2026-11-18):** 0-INBOX\temp\pipeline\pi-1-vi-ai\mapper-vi\vi-map-conventions.md and the notes of every pi-1 part (pi-1-vi-ai\mapper-vi\notes-map-*.md). They are binding for pi-2: value form (frame words «các» / «những», existential «có», predicate «là» dropped; nominalisers kept as the text has them), discontinuous values with " … ", compounds and members, fragments that lost a negative prefix = the positive Vietnamese word, `(no direct equivalent)` only as defined there, Yo/Yā/Yaṃ conventions, matrix items.
- The pi-1 tooling: pi-1-vi-ai\mapper-vi\map_common_vi.py (present(), build_part(), verify(), the CORE / CH2 / MATRIX tables) and the latest part script map_5_vi.py (its resolver chain holds all pi-1 tables). Import them READ-ONLY (`sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-vi-ai\mapper-vi")`); their path constants point at pi-1, so write a pi-2 common module (below) that reuses the functions and tables with pi-2 paths. Importing must not rewrite any pi-1 output (hash the pi-1 mapped files before and after).
- The pi-1 Vietnamese keyword map (AI_translation\vietnamese\pi-1-keywords-by-reference-pali-vietnamese-plain.md): where a pi-2 segment repeats pi-1 Pāli with the same Vietnamese, the same keyword gets the same value.
- Cross-check of how each Pāli keyword was read (meaning only): the Russian pi-2 map 0-INBOX\temp\pipeline\pi-2-ru\mapper-ru\<part>.mapped.md and ru-map conventions there; the English pi-2 map AI_translation\english\pi-2-keywords-by-reference-pali-english-plain.md (grep, don't read whole).

## Per part (preamble, 1-khandhavibhango)
- Keywords (Pāli): 0-INBOX\temp\pipeline\pi-2-vi-ai\mapper-vi\<part>.keywords.md, `[id] kw1, kw2, …`.
- Vietnamese translation: AI_translation\vietnamese\pi-2-vietnamese-plain-zeroshot_split_chapters\<part>.md (segments end with ^id). It is final for this step (harmonised); do not edit it.
- Pāli source, for context: AI_translation\pali\pi-2_split_chapters\<part>.md.
- Helpful: the Vietnamese was generated from the Pāli by builder scripts with fixed phrase tables (pi-2-vi-ai\build_ch1_sample_vi.py, build_1_vi.py, notes-1.md, vi-zeroshot-terms.md); the harmonise pass changed some strings afterwards (pi-2-vi-ai\harmonise-log.tsv); the TRANSLATION FILE is the truth.
- Output: mapper-vi\<part>.mapped.md: the same lines, in the same order, with the same Pāli keywords in the same order, each written `pāli=tiếng Việt`.

## Also write (for the later agents)
- mapper-vi\map_common_vi.py (pi-2): pi-2 paths; imports and reuses pi-1's present() logic and tables; build_part(), verify().
- mapper-vi\vi-map-conventions-pi2.md: only what pi-2 adds or changes against the pi-1 conventions (new recurring keywords and their values), so later agents read pi-1's file plus this one.
- mapper-vi\map_sample_vi.py: your table plus per-segment overrides for the two parts.

## Rules (user-approved)
- For each keyword, the word or phrase in THAT segment's Vietnamese that carries its meaning, copied as it stands there, in the pi-1 value form.
- Keep keywords exactly as given (multiword, capitalised, odd forms). Never add, drop, merge or reorder.
- `(no direct equivalent)` only as defined in the pi-1 conventions.
- Compare each segment for real; the same Pāli word may map differently by context; identical formulaic segments get identical mappings.
- No ", " inside a value (drop the comma, or " / " for alternatives).

## Verify each part (replace PART); it must print `bad []`
```
python -I -X utf8 -c "import pathlib;d=pathlib.Path('0-INBOX/temp/pipeline/pi-2-vi-ai/mapper-vi');ch='PART';a=[l.split('] ',1) for l in (d/f'{ch}.keywords.md').read_text(encoding='utf-8').splitlines()];b=[l.split('] ',1) for l in (d/f'{ch}.mapped.md').read_text(encoding='utf-8').splitlines()];assert [x[0] for x in a]==[x[0] for x in b];bad=[i for (i,x),(_,y) in zip(a,b) if [k.strip() for k in x.split(', ')]!=[k.split('=',1)[0] for k in y.split(', ')]];print(ch,'lines',len(a),'bad',bad)"
```
(If PowerShell mangles it, put the same code in mapper-vi\check_parts_vi.py taking parts as arguments, printing the structural result and verify()'s presence result, as pi-1's check_parts_vi.py does.) Plus the presence check: every Vietnamese value found in that segment's Vietnamese; exceptions listed with reasons.

## Report (under 400 words, as text)
Per part: line count, verifier result, number of (no direct equivalent), presence-check result. What pi-2 adds to the pi-1 conventions. 10–15 example mappings for review. Genuinely unclear mappings.
