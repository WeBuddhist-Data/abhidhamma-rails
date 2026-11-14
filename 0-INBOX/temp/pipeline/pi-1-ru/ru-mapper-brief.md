# Brief: Pāli→Russian keyword mapping for pi-1 (Dhammasaṅgaṇī), remaining parts

Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write tools for files (write scripts with the Write tool, never via a shell redirect), PowerShell for commands, `python -I -X utf8`. Several agents map other parts in parallel (user-approved). Write ONLY your own mapped files, plus helper scripts and notes named after your parts, inside 0-INBOX\temp\pipeline\pi-1-ru\mapper-ru\. Never create files at the repo root or in a system temp folder. Do not touch 1-SOURCES\ or 4-SYSTEM\, do not edit the translation, do not run git, never write "seed". You cannot write report files for me: return your report as text.

## Read first (binding)
- AI_translation\skills\keyword-equivalence-mapper.md (the skill you execute).
- 0-INBOX\temp\pipeline\russian-style.md (Russian conventions, core terms).
- **The user approved the sample (preamble, 1-matika, 2-01) on 2026-11-14.**
  - mapper-ru\ru-map-conventions.md (READ-ONLY): the settled conventions (dhammā = «явления» and dhammā-phrases in nominative plural; samaye X; compounds and members; fragments; particles; matrix item names; value forms) AND the user decision at its end: a fragment whose positive part is not a Russian word, or a keyword with no word of its own in the Russian, = `(no direct equivalent)`. Follow it exactly.
  - mapper-ru\map_common_ru.py (READ-ONLY): shared tables (CORE, CH2, MATRIX), the presence check `present()`, `build_part()`, `verify()`. Import it (`sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-ru\mapper-ru")`). Extend its tables in YOUR OWN script, never in the shared file.
  - The approved sample maps (preamble / 1-matika / 2-01-cittuppadakandam .mapped.md) and map_sample_ru.py: the same Pāli keyword in the same Russian context gets the same value.
- Approved Russian maps of earlier books, for terms you meet (grep, don't read whole): AI_translation\russian\pi-3/pi-4/pi-5-keywords-by-reference-pali-russian-plain.md.

## Per part
- Keywords (Pāli): mapper-ru\<part>.keywords.md, `[id] kw1, kw2, …`.
- Russian translation: AI_translation\russian\pi-1-russian-plain-zeroshot_split_chapters\<part>.md (segments end with ^id). It is final (approved, harmonised).
- Pāli source, for context: AI_translation\pali\pi-1_split_chapters\<part>.md.
- Very helpful: the Russian was generated from the Pāli by builder scripts with fixed phrase tables (0-INBOX\temp\pipeline\pi-1-ru\build_<part>_ru.py, notes-<part>.md, ru-zeroshot-terms.md). The consistency pass changed some strings afterwards (harmonise-log.tsv lists every old → new); the TRANSLATION FILE is the truth. The English map of the same book (AI_translation\english\pi-1-keywords-by-reference-pali-english-plain.md) shows how each Pāli keyword was read.
- Output: mapper-ru\<part>.mapped.md: same lines, same order, the same Pāli keywords in the same order, each `pāli=русский`. Write it with `build_part()`.
- New recurring decisions go in mapper-ru\notes-map-<your parts>.md, one "pāli = русский (context)" per line.

## Rules (user-approved)
- For each keyword, the word or phrase in THAT segment's Russian that carries its meaning, in dictionary form (see the conventions file).
- Keep keywords exactly as given. Never add, drop, merge or reorder.
- `(no direct equivalent)` as defined in the conventions file.
- Compare each segment for real; the same Pāli word may map differently by context; identical formulaic segments get identical mappings. A table plus per-segment overrides is fine, but only after reading the segments.
- No ", " inside a value.
- Core: dhamma = явление; kusala = благой; akusala = неблагой; abyākata = этически неопределённый; mātikā = матрица; vicāra = удержание мысли; saṅkhāra (aggregate) = формирующие факторы; dosa = злоба; asaṅkhata = необусловленное; cittuppāda = вид ума (ch5).

## Verify each part (replace PART); it must print `bad []`
```
python -I -X utf8 -c "import pathlib;d=pathlib.Path('0-INBOX/temp/pipeline/pi-1-ru/mapper-ru');ch='PART';a=[l.split('] ',1) for l in (d/f'{ch}.keywords.md').read_text(encoding='utf-8').splitlines()];b=[l.split('] ',1) for l in (d/f'{ch}.mapped.md').read_text(encoding='utf-8').splitlines()];assert [x[0] for x in a]==[x[0] for x in b];bad=[i for (i,x),(_,y) in zip(a,b) if [k.strip() for k in x.split(', ')]!=[k.split('=',1)[0] for k in y.split(', ')]];print(ch,'lines',len(a),'bad',bad)"
```
Plus `verify(part)` from map_common_ru.py (presence check: every Russian value found in that segment's Russian; list exceptions with reasons). Also make sure no value is a non-word made by cutting «не-/без-» off a Russian word.

## Final report (short, as text)
Per part: line count, verifier result, number of (no direct equivalent), presence-check result. New conventions you needed. Genuinely unclear mappings.
