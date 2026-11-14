# Brief: RAILS Russian translation, plain audience, pi-1 (Dhammasaṅgaṇī): SAMPLE

## Setup
- Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write tools for files (write scripts with the Write tool, never via a shell redirect), PowerShell for commands, `python -I -X utf8`.
- Write ONLY the outputs listed below plus helper scripts in 0-INBOX\temp\pipeline\pi-1-ru\rails\. Never create files at the repo root or in a system temp folder. Do not touch 1-SOURCES\ or 4-SYSTEM\, do not run git, never write "seed" or "unseeded". You cannot write report files for me: return your report as text.
- This sample is what the user reviews before the rest of the book is translated. It sets every sentence formula the later agents will copy.

## Read first
- AI_translation\skills\rails-verse-translator.md. Follow it.
- 0-INBOX\temp\pipeline\russian-style.md: register, typography («…»/„…“, no «ли»), the strict DASH RULE, structure. The book title is «Перечисление явлений».
- Translate FRESH from the Pāli, consulting the locked termbase term by term.
- Do NOT open the Russian zero-shot (AI_translation\russian\pi-1-russian-plain-zeroshot_split_chapters\, pi-1-russian-plain-zeroshot.md), the zero-shot builders and notes in pi-1-ru\ (build_*_ru.py, notes-*.md, ru-zeroshot-terms.md, harmonise files) or the Russian side of the keyword maps.
- You may use as models of house style and shared passages: the finished Russian rails translations of other books (AI_translation\russian\pi-3-russian-plain.md, pi-4-russian-plain.md, pi-5-russian-plain.md), and, for how the Dhammasaṅgaṇī sample was structured, the Hindi pi-1 rails sample builder and formulas file (0-INBOX\temp\pipeline\pi-1-ru\ref\hi_rails_build_rails_sample.py, ref\hi_rails_hi-rails-formulas.md). Where they disagree with the pi-1 Russian termbase, the termbase wins.

## Inputs
- **Source:** AI_translation\pali\pi-1_split_chapters\<ch>.md
- **Locked termbase (authoritative, user-approved 2026-11-14):** AI_translation\russian\pi-1-pali-russian-termbase-plain.md, `pali: {english tag: русский; …}`. See also 0-INBOX\temp\pipeline\pi-1-ru\termbase\APPROVED.md (the user's fixes: ujutā «прямизна», asārāgo «отсутствие пристрастия», Suññataṃ «пустой», ajjhattaṃ / bahiddhā «внутри себя» / «вовне»).
  - Look up each Pāli word; pick the sense by its tag. Compounds and phrases often have their own entries; a compound without an entry is built from its members' entries.
  - Inflect grammatically (case, number, gender, verb agreement, short/long adjective), but never swap in a synonym. Terms are in dictionary form.
  - If no sense fits, use the closest sibling entry and REPORT it.
- **Audience:** AI_translation\audience_profile\plain.md

## What to produce
1. AI_translation\russian\pi-1-russian-plain-rails_split_chapters\preamble.md (source preamble.md).
2. AI_translation\russian\pi-1-russian-plain-rails_split_chapters\1-matika.md: the whole matrix. It fixes every triad and pair name; chapters 4 and 5 will reuse them verbatim in their question and answer frames (Katame dhammā X? / ime dhammā X).
3. 0-INBOX\temp\pipeline\pi-1-ru\rails\sample-2-01\2-01-sample.md: chapter 2 from its start through ^1-57 (the first 122 non-empty Pāli lines; the Pāli slice is in 0-INBOX\temp\pipeline\pi-1-ru\ref\ch2-01-pali-1-122.md).
4. 0-INBOX\temp\pipeline\pi-1-ru\rails\ru-rails-formulas.md: every recurring sentence formula and fixed string (the matrix items with their question/answer forms, the «tasmiṃ samaye … hoti» frames, the factor names, every synonym string of ^1-1 … ^1-57, the closing line, the chapter headings for chapters 2–5) as "Pāli = Russian", one per line. It becomes binding for the later agents.
5. 0-INBOX\temp\pipeline\pi-1-ru\rails\build_rails_sample_ru.py: builds 1-3 from fixed formula strings (Python constants the later agents can import; importing must not rewrite outputs: guard with `if __name__ == "__main__":`).

## Rules
- **Block IDs:** exact, at the end of the last line of each segment, in the same order.
- **Headings:** keep their #-level.
- **Segments:** each has the source's number of non-empty lines. One blank line between segments; no double blank lines.
- **DASH RULE (user):** "–" only where the Pāli has "–" or "—", same spot, same count on every line. Never add one; no ":-". The Pāli of chapter 2 has "–" before «ime dhammā kusalā» / «ayaṃ tasmiṃ samaye …»: keep exactly that one.
- **Punctuation:** "…pe…" becomes "…". Statements end with ".". Questions end with "?", never with «ли». Quotes «…» / „…“.
- **Brackets:** «[вариант написания (Sī.): …]» for spelling-only variants, «[вариант чтения (…): …]» otherwise; (Ka)/(Kha)/(Ga) → (а)/(б)/(в). Translate editorial notes.
- **Translate the Pāli as written** (user rule): no emendations; only plain spelling slips may be rendered as meant. Report suspected slips.
- **Formulas:** identical Pāli gets identical Russian.
- **Readability for a plain reader:** the long lists and -pe- runs must read as Russian sentences. Never leave a term sitting ungrammatically; recast a sentence where a literal string reads badly, while keeping every term.

## Verify (all must pass)
```
python -I -X utf8 0-INBOX\temp\pipeline\check_chapter_ids.py AI_translation\pali\pi-1_split_chapters AI_translation\russian\pi-1-russian-plain-rails_split_chapters 1-matika.md
python -I -X utf8 0-INBOX\temp\pipeline\dashcheck.py <pali> <russian>     (preamble, 1-matika, and ref\ch2-01-pali-1-122.md vs sample-2-01\2-01-sample.md)
```
plus a check that the block IDs of 2-01-sample.md equal those of the Pāli slice, in order; no «ли», no Latin outside variant brackets, no double blank lines, no CR. Then termbase adherence for the matrix (it checks the segments in the folder):
```
python -I -X utf8 0-INBOX\temp\pipeline\termbase_adherence.py AI_translation\pali\pi-1-keywords-by-reference-pali-plain.md AI_translation\russian\pi-1-pali-russian-termbase-plain.md AI_translation\russian\pi-1-russian-plain-rails_split_chapters
```
and the same for the 2-01 sample (copy it into a scratch folder under pi-1-ru\rails\ named 2-01-cittuppadakandam.md to run the tool on it). Read the misses with judgement (inflection and split phrases cause false misses) and fix the genuine ones.

## Report (under 450 words, as text)
- Checks passed; segment counts; adherence results.
- 10–15 key formulas as "Pāli = Russian" (the kusala question/answer frame, «tasmiṃ samaye … hoti», a factor definition, a triad name, a dyad name, the closing line).
- Termbase misfits (term, segment, why it does not fit, what you wrote) and terms the termbase lacks.
- Unsure Pāli or source slips.
