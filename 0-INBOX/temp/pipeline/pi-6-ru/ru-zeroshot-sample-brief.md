# Brief: Russian zero-shot of pi-6 (Yamaka), SAMPLE

Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write tools for files (write scripts with the Write tool at their full paths under D:\Work\OpenPecha\abhidhamma-rails, never via a shell redirect or from PowerShell), PowerShell for commands, `python -I -X utf8 -B` (-B: no __pycache__). LF line endings: open(..., "w", encoding="utf-8", newline="\n"). Write ONLY the files named below plus helper scripts in 0-INBOX\temp\pipeline\pi-6-ru\. Never create files at the repo root, outside the repo or in a system temp folder. Do not touch 1-SOURCES\ or 4-SYSTEM\, never run git (not even git status), never write "seed" or "unseeded" in any file you write. No web access. Grep only the specific files named here, never whole folders. You cannot write report files for me: return your report as text.

This is the SAMPLE the user reviews before the rest of the book is translated by other agents (three at a time, one chapter each), who will copy your formulas verbatim. Be careful, exact and consistent. If you run long, write the builder in several Write/Edit steps.

The sample is the preamble and chapter 1 (1-mulayamaka.md, the Yamaka of roots, 305 lines). It sets the book frame and the pair-question formulas the whole Yamaka repeats: the paired questions (Ka) / (Kha) («ye keci X, sabbe te Y?» / «ye vā pana Y, sabbe te X?»), the answers (Āmantā, the partial answers that name which ones are and which are not), the section headings (uddeso, niddeso, -vāro, -nayo …) and the closing lines.

## Read first (binding)
- 0-INBOX\temp\pipeline\russian-style.md: style, the strict DASH RULE, «…» / „…“, no «ли», core terms, review lessons, verify commands.
- AI_translation\skills\zeroshot-translator.md and AI_translation\audience_profile\plain.md.
- **Cross-book Russian (user-approved and reviewed): pi-1 «Перечисление явлений», pi-2 «Подробный разбор», pi-3 «Беседа об элементах», pi-4 «Описание типов людей», pi-5 «Предметы обсуждения».** The Yamaka works with the categories of pi-1 / pi-2 (kusala / akusala / abyākata, the roots, aggregates, bases, elements, truths, formations, latent tendencies, mind, dhammas, faculties). **Reuse that wording exactly.** Sources:
  1. AI_translation\russian\pi-1 … pi-5-russian-plain-rails_split_chapters\ (final reviewed text). Lookup: `python -I -X utf8 -B 0-INBOX\temp\pipeline\pi-6-ru\find_pi12345r_ru.py "<Pāli regex>" [books] [max_hits]` prints the Pāli line and the same line of the Russian rails.
  2. Termbases AI_translation\russian\pi-1 … pi-5-pali-russian-termbase-plain.md (grep, don't read whole) and the user's decisions 0-INBOX\temp\pipeline\pi-1-ru\termbase\APPROVED.md, pi-2-ru\termbase\APPROVED.md. Cross-book terms follow pi-1 (pi-2 rule); person types follow pi-4.
- **Cross-check of meaning and structure only (translate FROM THE PĀLI):** the English pi-6 rails AI_translation\english\pi-6-english-plain-rails_split_chapters\<ch>.md and the Hindi pi-6 rails AI_translation\hindi\pi-6-hindi-plain-rails_split_chapters\<ch>.md (same block IDs and lines); the English termbase AI_translation\english\pi-6-pali-english-termbase-plain.md; the commentary 1-SOURCES\Commentaries\pi-yamaka-atthakatha.md for hard readings (Pāli; allowed). Do not open any Vietnamese file.

## Source and output
- Source: AI_translation\pali\pi-6_split_chapters\preamble.md, 1-mulayamaka.md.
- Write:
  1. AI_translation\russian\pi-6-russian-plain-zeroshot_split_chapters\preamble.md, 1-mulayamaka.md (create the folder).
  2. 0-INBOX\temp\pipeline\pi-6-ru\build_sample_ru.py: a builder with fixed formula strings exposed as constants other agents import (the pair-question frames with their slots, the answers, the partial-answer frames, the section-heading words, the labels, the closing lines). Importing it must not rewrite outputs (`if __name__ == "__main__":`). It must assert at build time that every string it claims to take from pi-1-5 Russian still occurs in those rails files, and run per-line dash / quote / NFC / id checks.
  3. 0-INBOX\temp\pipeline\pi-6-ru\ru-zeroshot-terms.md: every formula and key term you settled, "Pāli = Russian", one per line, grouped (book frame, headings, question frames, answers, terms). Mark which come from pi-1-5 and which are new.
- **Book and chapter titles:** propose the Russian title of the book (Yamakapāḷi; one or two alternatives) and Russian headings for ALL ten yamakas (read the first heading line of each of the 44 files: Mūla-, Khandha-, Āyatana-, Dhātu-, Sacca-, Saṅkhāra-, Anusaya-, Citta-, Dhamma-, Indriyayamaka) and the recurring section headings of the book (uddeso, niddeso, paṇṇattivāro, pavattivāro, pariññāvāro, the time and person / place sections, anuloma / paṭiloma …: read the heading lines of 2-01-khandhayamaka.md, 7-01-anusayayamaka.md and 8-cittayamaka.md for them) in the terms file. Russian only, no Pāli name and no bracketed gloss (russian-style.md "Book titles").

## Rules
- Identical Pāli = identical Russian, within the sample and with pi-1-5 Russian.
- Core: dhamma = явление; mūla = корень; kusala / akusala = благой / неблагой; abyākata = этически неопределённый; khandha = совокупность; saṅkhāra = формирующие факторы; anusaya: take pi-2 / pi-5 Russian; mātikā = матрица. Root compounds (ekamūla, aññamaññamūla, mūlamūla …): choose one rendering each and state it.
- (Ka) / (Kha) / (Ga) … → (а) / (б) / (в) … (Russian alphabet order; state the full list you use). Variant brackets «[вариант написания (Sī., Syā.): <Pāli>]» for spelling-only variants, «[вариант чтения (…): <Pāli>]» otherwise. "…pe…" → "…" (never «….»). Digits and numbering stay.
- **DASH RULE:** "–" exactly where the Pāli has "–", same count per line; never add one; no ":-". Questions end with "?"; no «ли» (russian-style.md gives the question shapes). «ни … ни» with a participle or verb needs «не».
- No notes or commentary of your own inside the translation.
- Translate the Pāli as written (user rule): no emendations, add nothing, drop nothing (a repeated word stays); only plain spelling slips and missing punctuation may be rendered as meant. Report suspected slips.
- Readability for a plain reader: the pair questions must be clear Russian questions (who / which ones), and a partial answer must say plainly which ones are and which are not. A predicate with no count of its own that covers a whole set restates the set (review lesson from pi-2).

## Verify every file (all must pass before you report)
- `python -I -X utf8 -B 0-INBOX\temp\pipeline\check_chapter_ids.py AI_translation\pali\pi-6_split_chapters AI_translation\russian\pi-6-russian-plain-zeroshot_split_chapters <file>.md` prints OK.
- `python -I -X utf8 -B 0-INBOX\temp\pipeline\dashcheck.py <pali> <russian>`: equal line counts, 0 dash mismatches, 0 extra em-dashes.
- `python -I -X utf8 -B 0-INBOX\temp\pipeline\pi-1-ru\verify_ru.py <pali> <russian>` (IDs and line counts).
- No «ли», no Latin outside variant brackets, no double blank lines, no CR. The builder's cross-book string asserts pass.

## Report (under 450 words, as text)
- Checks passed, segment count per file.
- The proposed book title (with alternatives), the ten yamaka headings, the recurring section headings.
- The question frames, the answers and the partial-answer frames as "Pāli = Russian".
- What was reused from pi-1-5; Pāli you were unsure about or source slips (translated as written).
