# Brief: Pāli→Russian keyword mapping, pi-2 (Vibhaṅga): SAMPLE

Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write tools for files (write scripts with the Write tool, never via a shell redirect), PowerShell for commands, `python -I -X utf8`. Write ONLY inside 0-INBOX\temp\pipeline\pi-2-ru\mapper-ru\. Never create files at the repo root or in a system temp folder. Do not touch 1-SOURCES\ or 4-SYSTEM\, do not edit the translation, do not run git, never write "seed". You cannot write report files for me: return your report as text.

This sample (preamble and chapter 1, 172 lines) is what the user reviews before the remaining chapters are mapped, one at a time. It sets the conventions the later agents copy.

## Read first
- AI_translation\skills\keyword-equivalence-mapper.md (the skill you execute).
- 0-INBOX\temp\pipeline\russian-style.md.
- **The approved Russian pi-1 map (same book family, same conventions; binding):**
  - 0-INBOX\temp\pipeline\pi-1-ru\mapper-ru\ru-map-conventions.md, including the user decision at its end: a fragment whose positive part is not a Russian word, a bare preposition, or a keyword with no word of its own in the Russian = `(no direct equivalent)`.
  - 0-INBOX\temp\pipeline\pi-1-ru\mapper-ru\map_common_ru.py (presence check `present()`, `build_part()`, `verify()`, the CORE / CH2 / MATRIX tables): import it for the tooling (`sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-ru\mapper-ru")`), but its paths point to pi-1: wrap or copy the functions with pi-2 paths in your own module. Never edit pi-1 files.
  - The assembled pi-1 map AI_translation\russian\pi-1-keywords-by-reference-pali-russian-plain.md: the same Pāli keyword in the same Russian context gets the same value (pi-2 reuses pi-1's matrix items, aggregate names and synonym strings word for word).
  - 0-INBOX\temp\pipeline\pi-1-ru\mapper-ru\cleanup_map_ru.py: the coordinator's one-value-per-keyword decisions (e.g. upasampajja viharati «входить … пребывать», sahagataṃ in «с восприятием …» = NDE).
- Approved Russian maps of pi-3/4/5 (AI_translation\russian\pi-N-keywords-by-reference-pali-russian-plain.md): grep for terms you meet.

## Per part (preamble, 1-khandhavibhango)
- Keywords (Pāli): mapper-ru\<part>.keywords.md, `[id] kw1, kw2, …`.
- Russian translation: AI_translation\russian\pi-2-russian-plain-zeroshot_split_chapters\<part>.md (final: approved and harmonised; do not edit).
- Pāli source: AI_translation\pali\pi-2_split_chapters\<part>.md.
- Very helpful: the Russian was generated from the Pāli by builders with fixed phrase tables (0-INBOX\temp\pipeline\pi-2-ru\build_ch1_sample_ru.py, build_1_ru.py, ru-zeroshot-terms.md, notes-1.md); the consistency pass changed some strings afterwards (harmonise-log.tsv). The TRANSLATION FILE is the truth.
- Output: mapper-ru\<part>.mapped.md: same lines, same order, same Pāli keywords in the same order, each `pāli=русский`.

## Also write (for the later agents)
- mapper-ru\ru-map-conventions-pi2.md: only what pi-2 adds to or changes from the pi-1 conventions (e.g. «это называется «X»», the classification frames «Классификация … на N видов», the past/future/present strings, «бывает X, бывает Y»).
- mapper-ru\map_common_pi2_ru.py: the pi-2 paths, your shared tables, and the presence check (re-using pi-1's `present()` logic). Later agents import it.
- mapper-ru\map_sample_ru.py: your table plus per-segment overrides.

## Rules (user-approved for the Russian maps)
- For each keyword, the word or phrase in THAT segment's Russian that carries its meaning, in dictionary form (nouns nominative; plural kept where the concept is plural; adjectives/participles nominative masculine singular unless plural; verbs infinitive or the participle the text uses); `dhammā`-phrases in nominative plural as in pi-1.
- Keep keywords exactly as given. Never add, drop, merge or reorder.
- `(no direct equivalent)` as defined in the pi-1 conventions (incl. the user decision).
- Compare each segment for real; identical formulaic segments get identical mappings; a table plus per-segment overrides is fine after reading the segments.
- No ", " inside a value.
- Core: dhamma = явление; kusala = благой; akusala = неблагой; abyākata = этически неопределённый; khandha = совокупность; rūpa = материальная форма; saṅkhāra (aggregate) = формирующие факторы; mātikā = матрица.

## Verify each part (replace PART); it must print `bad []`
```
python -I -X utf8 -c "import pathlib;d=pathlib.Path('0-INBOX/temp/pipeline/pi-2-ru/mapper-ru');ch='PART';a=[l.split('] ',1) for l in (d/f'{ch}.keywords.md').read_text(encoding='utf-8').splitlines()];b=[l.split('] ',1) for l in (d/f'{ch}.mapped.md').read_text(encoding='utf-8').splitlines()];assert [x[0] for x in a]==[x[0] for x in b];bad=[i for (i,x),(_,y) in zip(a,b) if [k.strip() for k in x.split(', ')]!=[k.split('=',1)[0] for k in y.split(', ')]];print(ch,'lines',len(a),'bad',bad)"
```
Plus the presence check (every Russian value found in that segment's Russian; exceptions listed with reasons), and: no value is a non-word made by cutting «не-/без-», no bare preposition as a value.

## Report (under 400 words, as text)
Per part: line count, verifier result, number of (no direct equivalent), presence-check result. What pi-2 needed beyond the pi-1 conventions. 10–15 example mappings for review. Genuinely unclear mappings.
