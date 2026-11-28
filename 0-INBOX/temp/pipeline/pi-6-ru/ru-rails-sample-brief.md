# Brief: RAILS Russian translation, plain audience, pi-6 (Yamaka): SAMPLE

## Setup
- Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write tools for files (write scripts with the Write tool at their full paths, never via a shell redirect or from PowerShell), PowerShell for commands, `python -I -X utf8 -B` (-B: no __pycache__). LF line endings: open(..., "w", encoding="utf-8", newline="\n").
- Write ONLY the outputs listed below plus helper scripts in 0-INBOX\temp\pipeline\pi-6-ru\rails\. Never create files at the repo root (not even an empty one) or in a system temp folder. Do not touch 1-SOURCES\ or 4-SYSTEM\, do not edit any pi-1 … pi-5 file, do not run git (not even git status), never write "seed" or "unseeded". Grep only the specific files named here, never a whole folder. No web access. Do not open any Vietnamese file. You cannot write report files for me: return your report as text.
- This sample is what the user reviews before the rest of the book is translated (three agents at a time, one group of chapters each). It sets every sentence formula the later agents will copy.

## Read first
- AI_translation\skills\rails-verse-translator.md. Follow it.
- 0-INBOX\temp\pipeline\russian-style.md: register, typography («…»/„…“, no «ли»), the strict DASH RULE, structure.
- Translate FRESH from the Pāli, consulting the locked termbase term by term.
- Do NOT open the Russian pi-6 zero-shot (AI_translation\russian\pi-6-russian-plain-zeroshot_split_chapters\, pi-6-russian-plain-zeroshot.md), the zero-shot builders and notes (build_*_ru.py, notes-*.md, harmonise_*.py in pi-6-ru\) or the Russian side of the keyword maps (pi-6-ru\mapper-ru\*.mapped.md, map_*.py, pi-6-keywords-by-reference-pali-russian-plain.md).
- You MAY open (user decisions, not the zero-shot): 0-INBOX\temp\pipeline\pi-6-ru\ru-zeroshot-terms.md (the book title «Парные вопросы», the ten yamaka headings, the recurring section headings, the pair-question frames, the answers and the partial-answer frames the user approved on 2026-11-27: keep them), the "User decisions" section of pi-6-ru\zeroshot-coordinator-rules.md, and pi-6-ru\termbase\APPROVED.md.
- Models of house style:
  - The approved Russian pi-1 and pi-2 rails (AI_translation\russian\pi-1-russian-plain.md, pi-2-russian-plain.md and their rails_split_chapters\; pi-1-ru\rails\ru-rails-formulas.md, pi-2-ru\rails\ru-rails-formulas.md with their build_rails_sample_ru.py, constants; importing writes nothing): kusala / akusala / abyākata, the roots, the matrix names. Where pi-6 has the same Pāli as pi-1 / pi-2, reuse their Russian unless the pi-6 termbase decides otherwise for that word; report each such difference.
  - The finished Russian rails of pi-3, pi-4, pi-5 (AI_translation\russian\pi-N-russian-plain.md): pi-5 has many Yamaka-like question frames («Да.», «Нет.», «Такого нет.»).
  - Cross-check of meaning and structure (translate FROM THE PĀLI): the English pi-6 rails AI_translation\english\pi-6-english-plain-rails_split_chapters\<ch>.md and the Hindi pi-6 rails AI_translation\hindi\pi-6-hindi-plain-rails_split_chapters\<ch>.md (same block IDs and lines); the commentary 1-SOURCES\Commentaries\pi-yamaka-atthakatha.md (Pāli; read-only) for hard readings.
  - Where any model disagrees with the pi-6 Russian termbase, the termbase wins.

## Inputs
- **Source:** AI_translation\pali\pi-6_split_chapters\preamble.md and 1-mulayamaka.md (305 non-empty lines).
- **Locked termbase (authoritative, user-approved 2026-11-27):** AI_translation\russian\pi-6-pali-russian-termbase-plain.md, `pali: {english tag: русский; …}`, plus pi-6-ru\termbase\APPROVED.md (the user's changes and its rails notes).
  - Look up each Pāli word; pick the sense by its tag. Compounds and phrases often have their own entries (the root compounds: ekamūla «имеющий общий корень», aññamaññamūla «имеющий взаимный корень», -mūlaka «основанный на … корне», kusalamūlena «благой корень» …); a compound without an entry is built from its members' entries.
  - Inflect grammatically (case, number, gender, verb agreement, short/long adjective), but never swap in a synonym. Terms are in dictionary form.
  - If no sense fits, use the closest sibling entry and REPORT it.
- **Audience:** AI_translation\audience_profile\plain.md

## What to produce
1. AI_translation\russian\pi-6-russian-plain-rails_split_chapters\preamble.md and 1-mulayamaka.md (the folder exists and is empty).
2. 0-INBOX\temp\pipeline\pi-6-ru\rails\ru-rails-formulas.md: every recurring sentence formula and fixed string of the sample (the pair questions (а) / (б) «ye keci X, sabbe te Y?» / «ye vā pana Y, sabbe te X?», the answers «Да.», the partial answers that name which ones are and which are not, the root-compound sentences «X, которые возникают вместе, имеют и A, и B.», the section headings uddeso / niddeso / -vāro / -nayo, the Hetuvārādi verse, the closing lines, the book title and the ten yamaka headings) as "Pāli = Russian", one per line. It becomes binding for the later agents. Mark each string taken unchanged from pi-1 / pi-2 with "(pi-1)" / "(pi-2)", and each user-approved frame with "(user)".
3. 0-INBOX\temp\pipeline\pi-6-ru\rails\build_rails_sample_ru.py: builds 1-2 from fixed formula strings (Python constants and functions the later agents can import: the question frames with their slots, the answers, the partial-answer frames, the headings, the labels (а) / (б) …; importing must not rewrite outputs: guard with `if __name__ == "__main__":`). It runs per-line dash / quote / NFC / id checks.

## Rules
- **Block IDs:** exact, at the end of the last line of each segment, in the same order.
- **Headings:** keep their #-level. In headings the first word after a label or number is capitalised («#### (а) Перечень»).
- **Segments:** each has the source's number of non-empty lines. One blank line between segments; no double blank lines.
- **DASH RULE (user):** "–" only where the Pāli has "–" or "—", same spot, same count on every line. Never add one; no ":-".
- **Punctuation:** "…pe…" becomes "…" (after a word with no space; never «….»). Statements end with "."; questions end with "?", never with «ли». Quotes «…» / „…“.
- **Brackets:** «[вариант написания (Sī.): …]» for spelling-only variants, «[вариант чтения (…): …]» otherwise; (Ka)/(Kha)/(Ga) → (а)/(б)/(в). Translate editorial notes. Follow the pi-1 Russian rails for the exact bracket wording.
- **Translate the Pāli as written** (user rule): no emendations, add nothing, drop nothing (a repeated word stays). Only plain spelling slips and missing punctuation may be rendered as meant. A WRONG punctuation mark (a comma where a full stop belongs, «.» ending a question), a doubled or missing negation, or a one-letter slip that makes another real word stays as written. Report suspected slips.
- **Formulas:** identical Pāli gets identical Russian.
- **Readability for a plain reader:** each pair question must be a clear Russian question (who / which ones), and a partial answer must say plainly which ones are and which are not. Never leave a term sitting ungrammatically; recast a sentence where a literal string reads badly, while keeping every term.

## Verify (all must pass)
```
python -I -X utf8 -B 0-INBOX\temp\pipeline\check_chapter_ids.py AI_translation\pali\pi-6_split_chapters AI_translation\russian\pi-6-russian-plain-rails_split_chapters preamble.md
python -I -X utf8 -B 0-INBOX\temp\pipeline\check_chapter_ids.py AI_translation\pali\pi-6_split_chapters AI_translation\russian\pi-6-russian-plain-rails_split_chapters 1-mulayamaka.md
python -I -X utf8 -B 0-INBOX\temp\pipeline\dashcheck.py AI_translation\pali\pi-6_split_chapters\1-mulayamaka.md AI_translation\russian\pi-6-russian-plain-rails_split_chapters\1-mulayamaka.md
python -I -X utf8 -B 0-INBOX\temp\pipeline\pi-1-ru\verify_ru.py AI_translation\pali\pi-6_split_chapters\1-mulayamaka.md AI_translation\russian\pi-6-russian-plain-rails_split_chapters\1-mulayamaka.md
```
(and the same dashcheck / verify_ru for preamble.md) plus: no «ли», no Latin outside variant brackets, no double blank lines, no CR, no em dash. Then termbase adherence:
```
python -I -X utf8 -B 0-INBOX\temp\pipeline\termbase_adherence.py AI_translation\pali\pi-6-keywords-by-reference-pali-plain.md AI_translation\russian\pi-6-pali-russian-termbase-plain.md AI_translation\russian\pi-6-russian-plain-rails_split_chapters
```
(it reads only the chapter files present). Read the misses with judgement (inflection and split phrases cause false misses) and fix the genuine ones.

## Report (under 450 words, as text)
- Checks passed; segment counts; adherence results.
- 10–15 key formulas as "Pāli = Russian" (the pair questions, the answers, a partial answer, the root-compound sentences, the section headings, the closing lines).
- Strings reused from pi-1 / pi-2 and any place where the pi-6 termbase made you differ from them.
- Termbase misfits (term, segment, why it does not fit, what you wrote) and terms the termbase lacks.
- Unsure Pāli or source slips.
