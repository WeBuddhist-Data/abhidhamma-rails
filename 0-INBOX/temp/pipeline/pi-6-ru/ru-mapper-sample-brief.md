# Brief: Pāli→Russian keyword mapping, pi-6 (Yamaka): SAMPLE

Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write tools for files (write scripts with the Write tool at their full paths, never via a shell redirect or from PowerShell), PowerShell for commands, `python -I -X utf8 -B` (-B: no __pycache__). LF line endings. Write ONLY inside 0-INBOX\temp\pipeline\pi-6-ru\mapper-ru\. Never create files at the repo root (not even an empty one) or in a system temp folder. Do not touch 1-SOURCES\ or 4-SYSTEM\, do not edit the translation or any pi-1 / pi-2 file, do not run git, never write "seed" or "unseeded". Grep only the specific files named here, never a whole folder. No Vietnamese files. You cannot write report files for me: return your report as text.

This sample (preamble and chapter 1, 142 lines) is what the user reviews before the remaining chapters are mapped. It sets the conventions the later agents copy.

## Read first
- AI_translation\skills\keyword-equivalence-mapper.md (the skill you execute).
- 0-INBOX\temp\pipeline\russian-style.md.
- **The approved Russian pi-1 and pi-2 maps (binding conventions):**
  - 0-INBOX\temp\pipeline\pi-1-ru\mapper-ru\ru-map-conventions.md, including the user decision at its end: a fragment whose positive part is not a Russian word, a bare preposition, or a keyword with no word of its own in the Russian = `(no direct equivalent)`.
  - 0-INBOX\temp\pipeline\pi-2-ru\mapper-ru\ru-map-conventions-pi2.md (what pi-2 added: N-vidhena values without «классификация», gerunds kept where the text has a gerund, …).
  - 0-INBOX\temp\pipeline\pi-2-ru\mapper-ru\map_common_pi2_ru.py and 0-INBOX\temp\pipeline\pi-1-ru\mapper-ru\map_common_ru.py (presence check `present()`, `build_part()`, `verify()`, the shared tables): import them for the tooling, but their paths point to pi-1 / pi-2: wrap or copy the functions with pi-6 paths in your own module. Never edit them.
  - 0-INBOX\temp\pipeline\pi-2-ru\mapper-ru\cleanup_map_ru.py and pi-1-ru\mapper-ru\cleanup_map_ru.py: the coordinator's one-value-per-keyword decisions.
- Approved Russian maps AI_translation\russian\pi-1 … pi-5-keywords-by-reference-pali-russian-plain.md: the same Pāli keyword in the same Russian context gets the same value (kusala, mūla, the roots, aggregates, bases, elements, …). Grep them for terms you meet.

## Per part (preamble, 1-mulayamaka)
- Keywords (Pāli): mapper-ru\<part>.keywords.md, `[id] kw1, kw2, …`.
- Russian translation: AI_translation\russian\pi-6-russian-plain-zeroshot_split_chapters\<part>.md (final: approved and harmonised; do not edit).
- Pāli source: AI_translation\pali\pi-6_split_chapters\<part>.md.
- Very helpful: the Russian was generated from the Pāli by a builder with fixed phrase tables (0-INBOX\temp\pipeline\pi-6-ru\build_sample_ru.py, ru-zeroshot-terms.md, zeroshot-coordinator-rules.md). The TRANSLATION FILE is the truth.
- Output: mapper-ru\<part>.mapped.md: same lines, same order, same Pāli keywords in the same order, each `pāli=русский`.

## Also write (for the later agents)
- mapper-ru\ru-map-conventions-pi6.md: only what pi-6 adds to or changes from the pi-1 / pi-2 conventions. The Yamaka is built from pair questions, so settle, with reasons: the root compounds (ekamūla «имеющий общий корень», aññamaññamūla «имеющий взаимный корень», kusalamūlamūla …: one value each, the phrase the text uses), instrumental keywords like kusalamūlena (the Russian «с …» / «…ым корнем» phrase in dictionary form), section headings (uddeso «перечень», Mūlavāro, -nayo «метод», niddeso …), question particles and answers (Āmantā «да»; ye keci / sabbe te: NDE or a word, one rule), and how a heading keyword maps to a heading phrase.
- mapper-ru\map_common_pi6_ru.py: the pi-6 paths, your shared tables, and the presence check (re-using pi-1's `present()` logic). Later agents import it.
- mapper-ru\map_sample_ru.py: your table plus per-segment overrides.

## Rules (user-approved for the Russian maps)
- For each keyword, the word or phrase in THAT segment's Russian that carries its meaning, in dictionary form (nouns nominative; plural kept where the concept is plural; adjectives/participles nominative masculine singular unless plural; verbs infinitive, or the participle / gerund the text uses); `dhammā`-phrases in nominative plural as in pi-1.
- Keep keywords exactly as given. Never add, drop, merge or reorder.
- `(no direct equivalent)` as defined in the pi-1 conventions (incl. the user decision).
- Compare each segment for real; identical formulaic segments get identical mappings; a table plus per-segment overrides is fine after reading the segments.
- No ", " inside a value.
- Core: dhamma = явление; kusala = благой; akusala = неблагой; abyākata = этически неопределённый; mūla = корень; hetu = причина; khandha = совокупность; mātikā = матрица.

## Verify each part (replace PART); it must print `bad []`
```
python -I -X utf8 -c "import pathlib;d=pathlib.Path('0-INBOX/temp/pipeline/pi-6-ru/mapper-ru');ch='PART';a=[l.split('] ',1) for l in (d/f'{ch}.keywords.md').read_text(encoding='utf-8').splitlines()];b=[l.split('] ',1) for l in (d/f'{ch}.mapped.md').read_text(encoding='utf-8').splitlines()];assert [x[0] for x in a]==[x[0] for x in b];bad=[i for (i,x),(_,y) in zip(a,b) if [k.strip() for k in x.split(', ')]!=[k.split('=',1)[0] for k in y.split(', ')]];print(ch,'lines',len(a),'bad',bad)"
```
Plus the presence check (every Russian value found in that segment's Russian; exceptions listed with reasons), and: no value is a non-word made by cutting «не-/без-», no bare preposition as a value.

## Report (under 400 words, as text)
Per part: line count, verifier result, number of (no direct equivalent), presence-check result. What pi-6 needed beyond the pi-1 / pi-2 conventions. 10–15 example mappings for review. Genuinely unclear mappings.
