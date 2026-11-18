# Brief: Pāli→Vietnamese keyword mapping for pi-1 (Dhammasaṅgaṇī), remaining parts

Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write tools for files (write scripts with the Write tool, never via a shell redirect), PowerShell for commands, `python -I -X utf8`. Agents map the parts ONE AT A TIME, in book order; earlier parts are finished. Write ONLY your own mapped files, plus helper scripts and notes named after your parts, inside 0-INBOX\temp\pipeline\pi-1-vi-ai\mapper-vi\. Never create files at the repo root or in a system temp folder. Do not touch 1-SOURCES\ or 4-SYSTEM\, do not edit the translation, do not edit earlier agents' files, never run git (not even git status), never write "seed". You cannot write report files for me: return your report as text.

## FORBIDDEN (copyrighted reference translation)
Never open, grep or search: 1-SOURCES\Translations\Vietnamese\vi-*.md, 0-INBOX\raw-data\vi-*, 0-INBOX\temp\pipeline\pi-1-vi\, pi-2-vi\, pi-3-4-vi\, pi-5-vi\, pi-6-vi\, pi-7-vi\, pi-1-th-vi\, vi-tools\. No folder-wide searches over 0-INBOX\temp\pipeline\, 1-SOURCES\ or AI_translation\ (search only the specific files named here).

## Read first (binding)
- AI_translation\skills\keyword-equivalence-mapper.md (the skill you execute).
- 0-INBOX\temp\pipeline\vietnamese-style.md (Vietnamese conventions, approved core terms, sati = «sự tỉnh thức»).
- **The user approved the sample (preamble, 1-matika, 2-01) on 2026-11-18.**
  - mapper-vi\vi-map-conventions.md (READ-ONLY): the settled conventions (value form: frame words «các»/«những», existential «có», predicate «là» dropped, nominalisers kept; discontinuous values with " … "; compounds and members; fragments that lost a negative prefix = the positive Vietnamese word; context rules; factor names; synonym strings; question frames; matrix items). Follow it exactly.
  - mapper-vi\map_common_vi.py (READ-ONLY): shared tables (CORE, CH2, MATRIX, SATI_BARE), `ch2_value()`, the presence check `present()`, `build_part()`, `verify()`. Import it (`sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-vi-ai\mapper-vi")`). Extend its tables in YOUR OWN script (`map_<parts>_vi.py`), never in the shared file. Earlier agents' scripts (map_<parts>_vi.py) can be imported the same way; importing must not rewrite their outputs.
  - The approved sample maps (preamble / 1-matika / 2-01-cittuppadakandam .mapped.md), map_sample_vi.py, and the mapped files and notes-map-*.md of earlier parts: the same Pāli keyword in the same Vietnamese context gets the same value.
- Cross-check of how each Pāli keyword was read (not of Vietnamese wording): the Russian map of the same parts, 0-INBOX\temp\pipeline\pi-1-ru\mapper-ru\<part>.mapped.md and notes-map-<parts>.md, and the English map AI_translation\english\pi-1-keywords-by-reference-pali-english-plain.md (grep, don't read whole).

## Per part
- Keywords (Pāli): mapper-vi\<part>.keywords.md, `[id] kw1, kw2, …`.
- Vietnamese translation: AI_translation\vietnamese\pi-1-vietnamese-plain-zeroshot_split_chapters\<part>.md (segments end with ^id). It is final (approved and harmonised); do not edit it.
- Pāli source, for context: AI_translation\pali\pi-1_split_chapters\<part>.md.
- Very helpful: the Vietnamese was generated from the Pāli by builder scripts with fixed phrase tables: 0-INBOX\temp\pipeline\pi-1-vi-ai\build_<part>_vi.py (see the file list there: build_2-01_2-02_vi.py, build_2-03_vi.py, build_2-04_vi.py, build_2-05_vi.py, build_3-01_vi.py, build_3-02_3-03_vi.py, build_4-01_vi.py, build_4-02_4-03_vi.py, build_5_vi.py), notes-<part>.md, vi-zeroshot-terms.md, vi-core-terms.md. The consistency pass changed some strings afterwards (harmonise-log.tsv lists every old → new, e.g. the 3-02/3-03 answer frame «– vật chất này …»); the TRANSLATION FILE is the truth.
- Output: mapper-vi\<part>.mapped.md: same lines, same order, the same Pāli keywords in the same order, each `pāli=tiếng Việt`. Write it with `build_part()`.
- New recurring decisions go in mapper-vi\notes-map-<your parts>.md, one "pāli = tiếng Việt (context)" per line.

## Rules (user-approved)
- For each keyword, the word or phrase in THAT segment's Vietnamese that carries its meaning, copied as it stands there, in the value form of the conventions file.
- Keep keywords exactly as given (multiword, capitalised, odd forms). Never add, drop, merge or reorder.
- `(no direct equivalent)` only as defined in the conventions file (particle with no Vietnamese word, word only inside a variant bracket kept in Pāli, fragment whose positive part is not a Vietnamese word, keyword with no word of its own in the Vietnamese).
- Compare each segment for real; the same Pāli word may map differently by context; identical formulaic segments get identical mappings. A table plus per-segment overrides is fine, but only after reading the segments.
- No ", " inside a value (drop the comma, or " / " for alternatives).
- Matrix item names reused in later chapters map to the same values as in `MATRIX`, unless that segment's Vietnamese words them differently (then copy what is there and note it).
- Core: dhamma = hiện tượng; kusala = thiện; akusala = bất thiện; abyākata = không xác định về mặt đạo đức; mātikā = ma trận; vitakka = sự hướng tâm; vicāra = sự duy trì tâm; sati = sự tỉnh thức (tỉnh thức inside năng lực / sức mạnh / … đúng đắn); rūpa (matter) = vật chất.

## Verify each part (replace PART); it must print `bad []`
```
python -I -X utf8 -c "import pathlib;d=pathlib.Path('0-INBOX/temp/pipeline/pi-1-vi-ai/mapper-vi');ch='PART';a=[l.split('] ',1) for l in (d/f'{ch}.keywords.md').read_text(encoding='utf-8').splitlines()];b=[l.split('] ',1) for l in (d/f'{ch}.mapped.md').read_text(encoding='utf-8').splitlines()];assert [x[0] for x in a]==[x[0] for x in b];bad=[i for (i,x),(_,y) in zip(a,b) if [k.strip() for k in x.split(', ')]!=[k.split('=',1)[0] for k in y.split(', ')]];print(ch,'lines',len(a),'bad',bad)"
```
(If PowerShell mangles the one-liner, put the same code in a script of your own taking the part as an argument.) Plus `verify(part)` from map_common_vi.py: every Vietnamese value found in that segment's Vietnamese; list any exception with its reason.

## Final report (short, as text, under 350 words)
Per part: line count, verifier result, number of (no direct equivalent), presence-check result. New conventions you needed (also in your notes file). Genuinely unclear mappings.
