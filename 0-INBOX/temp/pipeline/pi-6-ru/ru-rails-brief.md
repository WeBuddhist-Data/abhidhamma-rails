# Brief: RAILS Russian translation, plain audience, pi-6 (Yamaka): remaining chapters

## Setup
- Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write tools for files (write scripts with the Write tool at their full paths, never via a shell redirect or from PowerShell), PowerShell for commands, `python -I -X utf8 -B` (-B: no __pycache__). LF line endings: open(..., "w", encoding="utf-8", newline="\n").
- Write ONLY your own chapter files, plus helper scripts and notes named after your group in 0-INBOX\temp\pipeline\pi-6-ru\rails\. Never create files at the repo root (not even an empty one) or in a system temp folder. Do not touch 1-SOURCES\ or 4-SYSTEM\, do not edit other agents' files, the sample files or any pi-1 … pi-5 file, do not run git (not even git status), never write "seed" or "unseeded". Grep only the specific files named here, never a whole folder. No web access. Do not open any Vietnamese file. You cannot write report files for me: return your report as text. If you run long, write the builder in several Write/Edit steps.

**Groups (user: pi-6 runs three agents at a time).** Your group is named in your prompt.
- G2 khandha: 2-01-khandhayamaka, 2-02-khandhayamaka. **Frame-setter** for the paṇṇatti, pavatti and pariññā frames (the "X ti? … Y ti?" naming questions, yassa … tassa / yattha … tattha / yassa yattha … tassa tattha, uppajjati / nirujjhati in every tense and the mixed tenses, the person / plane answers, parijānāti).
- G7 anusaya: 7-01 … 7-11. **Frame-setter** for the anusaya frames (anuseti, sānusaya, niranusaya, pajahati, pariññā, pahīna, uppattiṭṭhāna, dhātu).
- G8 citta: 8-cittayamaka. **Frame-setter** for the cittayamaka frames (puggalavāra, dhammavāra, the time sections, uppajjamāna / nirujjhamāna, the suttanta / abhidhamma mixtures).
- Later groups import the frame-setters' builders and notes: G3 āyatana (3-01 … 3-06), G45 dhātu + sacca (4-dhatuyamaka, 5-01 … 5-03), G6 saṅkhāra (6-01, 6-02), G9 dhamma (9-01 … 9-03), G10a indriya (10-01 … 10-04), G10b indriya (10-05 … 10-13).
Before you start and again before you build, read the finished groups' rails builders and notes in 0-INBOX\temp\pipeline\pi-6-ru\rails\ (build_rails_<group>_ru.py, notes-rails-<group>.md) and their output chapters: identical Pāli must get identical Russian, so import their functions and strings (importlib.import_module; never edit their files).

## Coordinator notes (from the finished frame-setters; binding)
- G2 and G8 are finished. Import G2's builder: `importlib.import_module("build_rails_G2_ru")`; register your nouns with `register_term()`, then call `translate_line()`; extend `PL_ACC` / `PL_LOC` / `PL_ABL` / `BEINGS` and reset `GROUP_RULES = None`; extend `PERSONS`, `SUBJ`, `TVERB` as needed; `--probe <ch>` lists lines without a formula. Read notes-rails-G2.md (its import guide) and notes-rails-G8.md (moment phrases, participles «является возникшим / возникающим …», the past-time section).
- A tesaṃ / tattha that only repeats a person or place just named is not translated (G2); «у них» only when no person is named.
- pariññā: «полностью понимает / понял / поймёт»; the negative «не понимает полностью».

## Read first
- AI_translation\skills\rails-verse-translator.md. Follow it.
- 0-INBOX\temp\pipeline\russian-style.md: register, typography («…»/„…“, no «ли»), the strict DASH RULE, structure. The book is «Парные вопросы».
- Translate FRESH from the Pāli, consulting the locked termbase term by term.
- Do NOT open the Russian pi-6 zero-shot (AI_translation\russian\pi-6-russian-plain-zeroshot_split_chapters\, pi-6-russian-plain-zeroshot.md), the zero-shot builders and notes (build_*_ru.py, notes-*.md and harmonise_*.py in the pi-6-ru folder itself) or the Russian side of the keyword maps (pi-6-ru\mapper-ru\*.mapped.md, map_*.py, notes-map-*.md, pi-6-keywords-by-reference-pali-russian-plain.md).
- You MAY open (user decisions, not the zero-shot): pi-6-ru\ru-zeroshot-terms.md (the approved book title, yamaka headings, recurring section headings, question frames, answers and partial-answer frames: keep them) and the "User decisions", "Heading case", "Negatives" and "Shared phrases" sections of pi-6-ru\zeroshot-coordinator-rules.md (user-approved and coordinator frames; binding here too).
- Models of house style:
  - The approved Russian pi-1 … pi-5 rails (AI_translation\russian\pi-N-russian-plain.md, pi-N-russian-plain-rails_split_chapters\): the aggregates, bases, elements, truths, formations, latent tendencies, faculties, planes and persons; pi-5 has many Yamaka-like question frames. Where pi-6 has the same Pāli as an earlier book, reuse its Russian unless the pi-6 termbase or a pi-6 user decision says otherwise; report each such difference.
  - Cross-check of meaning and structure (translate FROM THE PĀLI): the English pi-6 rails AI_translation\english\pi-6-english-plain-rails_split_chapters\<ch>.md and the Hindi pi-6 rails AI_translation\hindi\pi-6-hindi-plain-rails_split_chapters\<ch>.md (same block IDs and lines); the commentary 1-SOURCES\Commentaries\pi-yamaka-atthakatha.md (Pāli; read-only) for hard readings.
  - Where any model disagrees with the pi-6 Russian termbase, the termbase wins.

## Inputs
- **Source:** AI_translation\pali\pi-6_split_chapters\<ch>.md
- **Locked termbase (authoritative, user-approved 2026-11-27):** AI_translation\russian\pi-6-pali-russian-termbase-plain.md, `pali: {english tag: русский; …}`, plus 0-INBOX\temp\pipeline\pi-6-ru\termbase\APPROVED.md:
  - kāyikaṃ / cetasikaṃ dukkhaṃ = «телесная / душевная боль» (Saccayamaka; user decision).
  - Anusaya chapter, dhātu = the three planes: dhātupucchāvāro «раздел вопросов о мирах», dhātuvisajjanāvāro «раздел ответов о мирах» (user decision). The Dhātuyamaka keeps «элементы».
  - Pacchimabhavikānaṃ «жить последней жизнью»; before «перерождается» the person group is «у тех, кто в последний раз перерождается (женщиной / мужчиной / в …)» (one group; coordinator rule). «Itaresaṃ … upapajjantānaṃ» = «У остальных, кто перерождается …», never «У остальных и у тех, кто …».
  - uppajjamānaṃ / nirujjhamānaṃ «возникающий / прекращающийся»; in the past-time section («uppajjamānaṃ khaṇaṃ vītikkantaṃ») the noun «момент возникновения / прекращения» stays.
  - Look up each Pāli word; pick the sense by its tag. Compounds and phrases often have their own entries; a compound without an entry is built from its members' entries. Inflect grammatically, never swap in a synonym. If no sense fits, use the closest sibling entry and REPORT it.
- **The approved sample (user-approved 2026-11-27): the model for everything.**
  - AI_translation\russian\pi-6-russian-plain-rails_split_chapters\preamble.md and 1-mulayamaka.md (done; do not rewrite them).
  - 0-INBOX\temp\pipeline\pi-6-ru\rails\ru-rails-formulas.md (READ-ONLY): every string in it is binding; copy it verbatim. 0-INBOX\temp\pipeline\pi-6-ru\rails\build_rails_sample_ru.py holds the same strings as Python constants and functions: import it (`sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-ru\rails"); import build_rails_sample_ru as S`) instead of retyping them. Never edit it; importing writes nothing.
- **Audience:** AI_translation\audience_profile\plain.md
- **Helper:** build your chapters with one builder (rails\build_rails_<group>_ru.py, e.g. build_rails_G2_ru.py) with fixed formula strings, so identical Pāli gives identical Russian. Importing it must not write anything (`if __name__ == "__main__":`); expose your frames as constants / functions later groups can import; it stops on Pāli it has no formula for and runs per-line dash / quote / NFC / id checks.
- Any NEW recurring formula goes in rails\notes-rails-<group>.md ("Pāli = Russian", one per line), not in the formulas file.

## Output
AI_translation\russian\pi-6-russian-plain-rails_split_chapters\<ch>.md (the folder exists).

## Rules
- **Block IDs:** exact, at the end of the last line of each segment, in the same order.
- **Headings:** keep their #-level. In headings the first word after a label or number is capitalised.
- **Segments:** each has the source's number of non-empty lines; one blank line between segments; no double blank lines.
- **DASH RULE (user):** "–" only where the Pāli has "–" or "—", same spot, same count on every line. Never add one; no ":-".
- **Punctuation:** "…pe…" becomes "…" (after a word with no space; after «?» / «.» as the Pāli spaces it; never «….»). Statements end with "."; questions end with "?", never with «ли». Quotes «…» / „…“.
- **Brackets:** «[вариант написания (Sī.): …]» for spelling-only variants, «[вариант чтения (…): …]» otherwise; (Ka)/(Kha)/(Ga)/(Gha)/(Ṅa)/(Ca) → (а)/(б)/(в)/(г)/(д)/(е) (the sample's LABEL). Translate editorial notes.
- **Translate the Pāli as written** (user rule): no emendations, add nothing, drop nothing (a repeated word stays). Only plain spelling slips and missing punctuation may be rendered as meant. A WRONG punctuation mark (a comma where a full stop belongs, «.» ending a question, a stray comma), a doubled or missing negation, or a one-letter slip that makes another real word (uppajjati / upapajjati swapped, bhavissanti for bhāvessanti) stays as written. A plural verb with a singular subject (or the reverse) is rendered with Russian agreement (coordinator; the user will confirm at the review). Report every suspected slip.
- **Negatives (coordinator rules):** «…, no ca tesaṃ Y nuppajjati» = «…, но у них возникает Y.» (never «но не так, что»); «X ca nuppajjati Y ca nuppajjati» = «не возникает ни X, ни Y»; the positive pair «и возникает X, и возникает Y».
- **Formulas:** identical Pāli gets identical Russian; where two segments differ only by a variant bracket or a numeral, the Russian differs only there.
- **Readability for a plain reader:** each pair question must be a clear Russian question (who / where / which ones), and a partial answer must say plainly which ones are and which are not.

## Verify each chapter (all must pass)
```
python -I -X utf8 -B 0-INBOX\temp\pipeline\check_chapter_ids.py AI_translation\pali\pi-6_split_chapters AI_translation\russian\pi-6-russian-plain-rails_split_chapters <ch>.md
python -I -X utf8 -B 0-INBOX\temp\pipeline\dashcheck.py AI_translation\pali\pi-6_split_chapters\<ch>.md AI_translation\russian\pi-6-russian-plain-rails_split_chapters\<ch>.md
python -I -X utf8 -B 0-INBOX\temp\pipeline\pi-1-ru\verify_ru.py AI_translation\pali\pi-6_split_chapters\<ch>.md AI_translation\russian\pi-6-russian-plain-rails_split_chapters\<ch>.md
```
Also: no «ли», no Latin outside variant brackets, no double blank lines, no CR, no em dash. Then termbase adherence on your chapters only (the script counts every chapter of the keyword file, so filter its output to your segment IDs, as the sample agent did with rails\kw_subset.py):
```
python -I -X utf8 -B 0-INBOX\temp\pipeline\termbase_adherence.py AI_translation\pali\pi-6-keywords-by-reference-pali-plain.md AI_translation\russian\pi-6-pali-russian-termbase-plain.md AI_translation\russian\pi-6-russian-plain-rails_split_chapters
```
Fix genuine misses in your chapters; inflection and split phrases cause false misses, so read them with judgement.

## Final report (short, as text, under 350 words)
- Per chapter: checks passed, segment count, adherence result for your chapters.
- New formulas (also in your notes file).
- Strings reused from earlier books and any place where the pi-6 termbase made you differ from them.
- Termbase misfits (term, segment, why it does not fit, what you wrote).
- Unsure Pāli or source slips (as written / as meant).
