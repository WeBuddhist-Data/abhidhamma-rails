# Brief: RAILS Russian translation, plain audience, pi-1 (Dhammasaṅgaṇī): remaining chapters

## Setup
- Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write tools for files (write scripts with the Write tool, never via a shell redirect), PowerShell for commands, `python -I -X utf8`.
- Write ONLY your own chapter files, plus helper scripts and notes named after your chapters in 0-INBOX\temp\pipeline\pi-1-ru\rails\. Never create files at the repo root or in a system temp folder. Do not touch 1-SOURCES\ or 4-SYSTEM\, do not edit other agents' files, do not run git, never write "seed" or "unseeded". You cannot write report files for me: return your report as text.

## Read first
- AI_translation\skills\rails-verse-translator.md. Follow it.
- 0-INBOX\temp\pipeline\russian-style.md: register, typography («…»/„…“, no «ли»), the strict DASH RULE, structure. The book is «Перечисление явлений».
- Translate FRESH from the Pāli, consulting the locked termbase term by term.
- Do NOT open the Russian zero-shot (AI_translation\russian\pi-1-russian-plain-zeroshot_split_chapters\, pi-1-russian-plain-zeroshot.md), the zero-shot builders and notes in pi-1-ru\ (build_*_ru.py in the pi-1-ru folder itself, notes-*.md there, ru-zeroshot-terms.md, harmonise files) or the Russian side of the keyword maps.
- Models of house style and shared passages: the finished Russian rails translations of the other books (AI_translation\russian\pi-3-russian-plain.md, pi-4-russian-plain.md, pi-5-russian-plain.md); for how a part is structured, the Hindi pi-1 builders in 0-INBOX\temp\pipeline\pi-1-ru\ref\ (hi_build_<part>_hi.py) and the English ones (en_build_<part>.py). Where they disagree with the pi-1 Russian termbase, the termbase wins.

## Inputs
- **Source:** AI_translation\pali\pi-1_split_chapters\<ch>.md
- **Locked termbase (authoritative, user-approved 2026-11-14):** AI_translation\russian\pi-1-pali-russian-termbase-plain.md, `pali: {english tag: русский; …}`, plus 0-INBOX\temp\pipeline\pi-1-ru\termbase\APPROVED.md.
  - Look up each Pāli word; pick the sense by its tag. Compounds and phrases often have their own entries; a compound without an entry is built from its members' entries.
  - Inflect grammatically (case, number, gender, verb agreement, short/long adjective), but never swap in a synonym.
  - If no sense fits, use the closest sibling entry and REPORT it.
- **The approved sample (user-approved 2026-11-14): the model for everything.**
  - AI_translation\russian\pi-1-russian-plain-rails_split_chapters\preamble.md and 1-matika.md (done; do not rewrite them). 1-matika fixes every triad and pair name: chapters 3–5 reuse them verbatim in their question and answer frames («Что такое X?» / «– это X.»).
  - 0-INBOX\temp\pipeline\pi-1-ru\rails\sample-2-01\2-01-sample.md: chapter 2 through ^1-57.
  - 0-INBOX\temp\pipeline\pi-1-ru\rails\ru-rails-formulas.md (READ-ONLY): every string in it is binding; copy it verbatim. 0-INBOX\temp\pipeline\pi-1-ru\rails\build_rails_sample_ru.py holds the same strings as Python constants: import it (`sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-ru\rails"); import build_rails_sample_ru as S`) instead of retyping them. Never edit it; importing writes nothing.
  - Terms the termbase lacks, as built in the sample (reuse them): byappanā «усиленное прикрепление мысли», anuvicāro «последовательное удержание мысли», upavicāro «пристальное удержание мысли», paṭipassaddhi «полная безмятежность», paṭipassambhanā «полное утихание», saṃphusitattaṃ «состояние соприкосновения», jīvitaṃ «жизнь», gocchaka «группа», hoti «есть» (the termbase's «существовать» belongs only to the Tathāgata views), ajjhattā dhammā «внутренние явления».
  - Source slips are translated as written (user): ^1-33 keeps the Pāli «?».
- **Audience:** AI_translation\audience_profile\plain.md
- **Helper:** a builder script with fixed formula strings guarantees identical Russian for identical Pāli. The Dhammasaṅgaṇī is extremely repetitive (synonym strings, jhāna formulas, the «samaye» lists, the -pe- runs): build your chapters with one (build_rails_<chapters>_ru.py).
- Any NEW recurring formula goes in rails\notes-<chapters>.md ("Pāli = Russian", one per line), not in the formulas file.
- **The chapter groups run ONE AT A TIME (user), in book order.** Before you start, read the finished earlier groups' rails builders and notes (0-INBOX\temp\pipeline\pi-1-ru\rails\build_rails_*_ru.py, rails\notes-*.md) and their output chapters: the same Pāli must get the same Russian, so import or copy their strings (never edit their files). Where your chapter repeats a passage an earlier rails chapter already has, reuse that Russian exactly.

## Output
AI_translation\russian\pi-1-russian-plain-rails_split_chapters\<ch>.md (the folder exists). 2-01-cittuppadakandam.md only: its first 122 non-empty Pāli lines (^1-1-0 … ^1-57) are the approved sample; reuse sample-2-01\2-01-sample.md byte-for-byte as the start of the file and continue from the next segment.

## Rules
- **Block IDs:** exact, at the end of the last line of each segment, in the same order (including the odd ^1-U1).
- **Headings:** keep their #-level.
- **Segments:** each has the source's number of non-empty lines; one blank line between segments; no double blank lines.
- **DASH RULE (user):** "–" only where the Pāli has "–" or "—", same spot, same count on every line. Never add one; no ":-".
- **Punctuation:** "…pe…" becomes "…". Statements end with ".". Questions end with "?", never with «ли». Quotes «…» / „…“.
- **Brackets:** «[вариант написания (Sī.): …]» for spelling-only variants, «[вариант чтения (…): …]» otherwise; (Ka)/(Kha)/(Ga) → (а)/(б)/(в). Translate editorial notes.
- **Translate the Pāli as written** (user rule): no emendations; only plain spelling slips may be rendered as meant. Report suspected slips.
- **Formulas:** identical Pāli gets identical Russian; where two segments differ only by a variant bracket or a numeral, the Russian differs only there.
- **Readability for a plain reader:** the long lists and -pe- runs must read as Russian sentences; recast where a literal string reads badly, keeping every term.

## Verify each chapter (all must pass)
```
python -I -X utf8 0-INBOX\temp\pipeline\check_chapter_ids.py AI_translation\pali\pi-1_split_chapters AI_translation\russian\pi-1-russian-plain-rails_split_chapters <ch>.md
python -I -X utf8 0-INBOX\temp\pipeline\dashcheck.py AI_translation\pali\pi-1_split_chapters\<ch>.md AI_translation\russian\pi-1-russian-plain-rails_split_chapters\<ch>.md
python -I -X utf8 0-INBOX\temp\pipeline\pi-1-ru\verify_ru.py AI_translation\pali\pi-1_split_chapters\<ch>.md AI_translation\russian\pi-1-russian-plain-rails_split_chapters\<ch>.md
```
Also: no «ли», no Latin outside variant brackets, no double blank lines, no CR; 2-01 starts with the sample byte-for-byte. Then termbase adherence (checks the segments present in the folder):
```
python -I -X utf8 0-INBOX\temp\pipeline\termbase_adherence.py AI_translation\pali\pi-1-keywords-by-reference-pali-plain.md AI_translation\russian\pi-1-pali-russian-termbase-plain.md AI_translation\russian\pi-1-russian-plain-rails_split_chapters
```
Fix genuine misses in your chapters; inflection and split phrases cause false misses, so read them with judgement.

## Final report (short, as text)
- Per chapter: checks passed, segment count, adherence result for your chapters.
- New formulas (also in your notes file).
- Termbase misfits (term, segment, why it does not fit, what you wrote).
- Unsure Pāli or source slips.
