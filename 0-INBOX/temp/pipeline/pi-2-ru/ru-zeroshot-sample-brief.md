# Brief: Russian zero-shot of pi-2 (Vibhaṅga), SAMPLE

Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write tools for files (write scripts with the Write tool, never via a shell redirect), PowerShell for commands, `python -I -X utf8`. Write ONLY the files named below plus helper scripts in 0-INBOX\temp\pipeline\pi-2-ru\. Never create files at the repo root or in a system temp folder. Do not touch 1-SOURCES\ or 4-SYSTEM\, do not run git, never write "seed" or "unseeded". You cannot write report files for me: return your report as text.

This is the SAMPLE the user reviews before the rest of the book is translated by other agents, who will copy your formulas verbatim. Be careful, exact and consistent.

## Read first (binding)
- 0-INBOX\temp\pipeline\russian-style.md: style, the strict DASH RULE, «…»/„…“, no «ли», core terms, review lessons, verify commands.
- AI_translation\skills\zeroshot-translator.md and AI_translation\audience_profile\plain.md.
- **Cross-book Russian (user-approved and reviewed):** pi-1 (Dhammasaṅgaṇī) is finished in Russian. The Vibhaṅga reuses its formulas heavily: the matrix triads and dyads, the aggregate definitions, the synonym strings, the material-form classifications, the question/answer frames. **Where the Pāli is identical or nearly identical to pi-1, reuse the pi-1 Russian wording.** Sources, in order:
  1. AI_translation\russian\pi-1-russian-plain-rails_split_chapters\ (the final, reviewed text; 1-matika.md has every matrix item, 3-0x-rupakandam.md the material-form classifications). Find matches by grepping the Pāli in AI_translation\pali\pi-1_split_chapters\ and reading the same line in the pi-1 Russian rails file (non-empty lines align one to one).
  2. AI_translation\russian\pi-1-pali-russian-termbase-plain.md and 0-INBOX\temp\pipeline\pi-1-ru\termbase\APPROVED.md (the user's decisions: «пристрастие» family, «Ненасытность», «часть для чтения вслух», «на N видов», «уровень» for bhūmi, «внутри себя / вовне», «пустой» …).
  3. The Russian pi-3/4/5 termbases and translations in AI_translation\russian\ (grep, don't read whole).
- **Cross-check of meaning and structure only (translate FROM THE PĀLI):** the English rails translation AI_translation\english\pi-2-english-plain-rails_split_chapters\<part>.md and the Hindi one AI_translation\hindi\pi-2-hindi-plain-rails_split_chapters\<part>.md (same segments and lines); the Hindi sample builder and term list of the same scope: 0-INBOX\temp\pipeline\pi-2-ru\ref\hi_build_ch1_sample_hi.py, ref\hi_hi-zeroshot-terms.md (its chapter-title proposals show the book's structure).

## Source and output
- Source: AI_translation\pali\pi-2_split_chapters\preamble.md and 1-khandhavibhango.md.
- Write:
  1. AI_translation\russian\pi-2-russian-plain-zeroshot_split_chapters\preamble.md (whole file; the folder exists).
  2. 0-INBOX\temp\pipeline\pi-2-ru\ch1-sample.md: the Russian of the Pāli slice 0-INBOX\temp\pipeline\pi-2-ru\ch1-sample-pali.md (the first 77 non-empty lines of 1-khandhavibhango.md, from `### Khandhavibhaṅgo ^2-1-0` to the line before `##### Vedanākkhandho ^2-1-2-2-0`), with the same blank lines. The agent who finishes chapter 1 later reuses it byte for byte.
  3. 0-INBOX\temp\pipeline\pi-2-ru\build_ch1_sample_ru.py: a builder with fixed formula strings (constants other agents can import: aggregate names, the past/future/present … strings, question/answer frames, classification frames). Importing it must not rewrite outputs (guard with `if __name__ == "__main__":`).
  4. 0-INBOX\temp\pipeline\pi-2-ru\ru-zeroshot-terms.md: every formula and key term you settled, "Pāli = Russian", one per line, grouped (book frame, chapter and section headings, aggregate formulas, classification frames, terms). Mark which come from pi-1 Russian and which are new.
- **Book and chapter titles:** propose the Russian title of the book (Vibhaṅgapāḷi) and Russian headings for ALL 18 chapters (Khandhavibhaṅga … Dhammahadayavibhaṅga) and the recurring section headings (Suttantabhājanīya, Abhidhammabhājanīya, Pañhāpucchaka) in the terms file. Russian only, no Pāli name and no bracketed gloss (russian-style.md "Book titles"). Give one or two alternatives for the book title. Earlier Russian books: «Перечисление явлений», «Беседа об элементах», «Описание типов людей», «Предметы обсуждения».

## Rules
- Identical Pāli = identical Russian, within the sample and with pi-1 Russian.
- Core: dhamma = явление; abyākata = этически неопределённый; kusala/akusala = благой/неблагой; khandha = совокупность; rūpa = материальная форма; saṅkhāra (aggregate) = формирующие факторы; mātikā = матрица.
- No notes or commentary of your own inside the translation. Variant brackets «[вариант написания (Sī., Syā.): <Pāli>]» for spelling-only variants, «[вариант чтения (…): <Pāli>]» otherwise. "…pe…" → "…". (Ka)/(Kha)/(Ga) → (а)/(б)/(в). Digits stay.
- No "—" or "–" unless the Pāli has one at that spot (same count per line); no ":-". «X – это …» without a comma after a plain noun or list; keep the comma only where it closes a clause or participial phrase. «ни … ни» with a participle or verb needs «не». No «ли» in questions.
- Translate the Pāli as written (user rule): no emendations; only plain spelling slips may be rendered as meant. Report suspected slips.

## Verify (all must pass before you report)
- preamble: `python -I -X utf8 0-INBOX\temp\pipeline\check_chapter_ids.py AI_translation\pali\pi-2_split_chapters AI_translation\russian\pi-2-russian-plain-zeroshot_split_chapters preamble.md` prints OK.
- `python -I -X utf8 0-INBOX\temp\pipeline\dashcheck.py <pali> <russian>` for the preamble and for (ch1-sample-pali.md, ch1-sample.md): equal line counts, 0 dash mismatches, 0 extra em-dashes.
- `python -I -X utf8 0-INBOX\temp\pipeline\pi-1-ru\verify_ru.py 0-INBOX\temp\pipeline\pi-2-ru\ch1-sample-pali.md 0-INBOX\temp\pipeline\pi-2-ru\ch1-sample.md` (IDs and line counts).
- No «ли», no Latin outside variant brackets, no double blank lines, no CR.

## Report (under 450 words, as text)
- Checks passed, segment count.
- The proposed book title (with alternatives) and the chapter/section headings.
- Key formulas and terms, and which were reused from pi-1 Russian.
- Pāli you were unsure about or that looks like a source slip (translated as written).
