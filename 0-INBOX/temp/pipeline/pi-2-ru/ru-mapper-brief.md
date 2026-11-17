# Brief: Pāli→Russian keyword mapping for pi-2 (Vibhaṅga), remaining chapters

Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write tools for files (write scripts with the Write tool, never via a shell redirect), PowerShell for commands, `python -I -X utf8`. Write ONLY your own mapped files, plus helper scripts and notes named after your chapters, inside 0-INBOX\temp\pipeline\pi-2-ru\mapper-ru\. Never create files at the repo root or in a system temp folder. Do not touch 1-SOURCES\ or 4-SYSTEM\, do not edit the translation or any pi-1 file, do not run git, never write "seed". You cannot write report files for me: return your report as text.

**The chapter groups run ONE AT A TIME, in book order (user).** Read the finished earlier groups' maps, scripts and notes in mapper-ru\ before you start, and keep their values for the same keyword in the same context.

## Read first (binding)
- AI_translation\skills\keyword-equivalence-mapper.md (the skill you execute).
- 0-INBOX\temp\pipeline\russian-style.md.
- The approved conventions: 0-INBOX\temp\pipeline\pi-1-ru\mapper-ru\ru-map-conventions.md (incl. the user decision at its end: non-word fragments, bare prepositions and keywords with no word of their own = `(no direct equivalent)`) and 0-INBOX\temp\pipeline\pi-2-ru\mapper-ru\ru-map-conventions-pi2.md (incl. the user decision of 2026-11-16: N-vidhena = «на два вида» etc., WITHOUT «классификация»).
- mapper-ru\map_common_pi2_ru.py (READ-ONLY): pi-2 paths, the pi-1 and sample tables, `value()`, `present()`, `build_part()`, `verify()`. Import it (`sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-ru\mapper-ru")`); extend its tables only in your own script.
- The approved sample maps (preamble / 1-khandhavibhango .mapped.md) and the assembled pi-1 map AI_translation\russian\pi-1-keywords-by-reference-pali-russian-plain.md: the same Pāli keyword in the same Russian context gets the same value (pi-2 repeats many pi-1 passages word for word; the pi-1 value wins there).
- Approved Russian maps of pi-3/4/5 (AI_translation\russian\pi-N-keywords-by-reference-pali-russian-plain.md): grep for terms you meet.

## Per chapter
- Keywords (Pāli): mapper-ru\<ch>.keywords.md, `[id] kw1, kw2, …`.
- Russian translation: AI_translation\russian\pi-2-russian-plain-zeroshot_split_chapters\<ch>.md (final: approved, harmonised; do not edit).
- Pāli source: AI_translation\pali\pi-2_split_chapters\<ch>.md.
- Helpful: the builders and notes in 0-INBOX\temp\pipeline\pi-2-ru\ (build_<ch>_ru.py, notes-<ch>.md) show which Pāli produced which Russian; the harmonise pass changed some strings afterwards (pi-2-ru\harmonise-log.tsv). The TRANSLATION FILE is the truth.
- Output: mapper-ru\<ch>.mapped.md (write it with `build_part()`): same lines, same order, same keywords in the same order, each `pāli=русский`.
- New recurring decisions go in mapper-ru\notes-map-<your chapters>.md, one "pāli = русский (context)" per line.

## Rules (user-approved)
- For each keyword, the word or phrase in THAT segment's Russian that carries its meaning, in dictionary form (see the conventions).
- Keep keywords exactly as given. Never add, drop, merge or reorder.
- `(no direct equivalent)` as defined in the conventions.
- Compare each segment for real; identical formulaic segments get identical mappings; a table plus per-segment overrides is fine after reading the segments.
- No ", " inside a value. No value that is a non-word made by cutting «не-/без-»; no bare preposition as a value.

## Verify each chapter (replace PART); it must print `bad []`
```
python -I -X utf8 -c "import pathlib;d=pathlib.Path('0-INBOX/temp/pipeline/pi-2-ru/mapper-ru');ch='PART';a=[l.split('] ',1) for l in (d/f'{ch}.keywords.md').read_text(encoding='utf-8').splitlines()];b=[l.split('] ',1) for l in (d/f'{ch}.mapped.md').read_text(encoding='utf-8').splitlines()];assert [x[0] for x in a]==[x[0] for x in b];bad=[i for (i,x),(_,y) in zip(a,b) if [k.strip() for k in x.split(', ')]!=[k.split('=',1)[0] for k in y.split(', ')]];print(ch,'lines',len(a),'bad',bad)"
```
Plus `verify(part)` from map_common_pi2_ru.py (presence check; list exceptions with reasons).

## Final report (short, as text)
Per chapter: line count, verifier result, number of (no direct equivalent), presence-check result. New conventions you needed. Genuinely unclear mappings.
