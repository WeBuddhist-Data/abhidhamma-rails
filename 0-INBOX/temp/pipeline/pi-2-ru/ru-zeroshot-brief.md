# Brief: Russian zero-shot of pi-2 (Vibhaṅga), remaining chapters

Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write tools for files (write scripts with the Write tool, never via a shell redirect), PowerShell for commands, `python -I -X utf8`. Write ONLY your own chapter files in the output folder, plus builder/helper scripts and notes named after your chapters inside 0-INBOX\temp\pipeline\pi-2-ru\. Never create files at the repo root or in a system temp folder. Do not touch 1-SOURCES\ or 4-SYSTEM\, do not edit any other agent's files, do not run git, never write "seed" or "unseeded". You cannot write report files for me: return your report as text.

The user approved the sample (preamble and chapter 1 through ^2-1-2-1) on 2026-11-14, with one fix: niyaka = pi-1 «закреплённый». **The chapter groups run ONE AT A TIME, in book order (user).** Continue in exactly the same style.

## Read first (binding)
- 0-INBOX\temp\pipeline\russian-style.md: style, DASH RULE, «…»/„…“, no «ли», core terms, verify commands.
- 0-INBOX\temp\pipeline\pi-2-ru\ru-zeroshot-terms.md (READ-ONLY): book title «Подробный разбор», all 18 chapter headings, the section headings («Разбор по наставлениям», «Разбор по Абхидхамме», «Раздел вопросов»), the aggregate formulas, classification frames and terms. Copy them verbatim.
- The approved sample and its builder (READ-ONLY; import, do not edit): 0-INBOX\temp\pipeline\pi-2-ru\ch1-sample.md, built by build_ch1_sample_ru.py (`sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-ru"); import build_ch1_sample_ru as S`). Importing writes nothing.
- **The finished earlier groups' builders, notes and output chapters** (0-INBOX\temp\pipeline\pi-2-ru\build_<chapters>_ru.py, notes-<chapters>.md, AI_translation\russian\pi-2-russian-plain-zeroshot_split_chapters\): the same Pāli must get the same Russian, so import or copy their strings.
- **Cross-book Russian (user-approved, reviewed): pi-1 Dhammasaṅgaṇī.** The Vibhaṅga reuses its matrix items, the mind-state definitions, the synonym strings, the jhāna formulas, the material-form lists and the question/answer frames. Where the Pāli is identical or nearly identical to pi-1, reuse the pi-1 Russian:
  1. AI_translation\russian\pi-1-russian-plain-rails_split_chapters\ (final text; find matches by grepping the Pāli in AI_translation\pali\pi-1_split_chapters\ and reading the same non-empty line in the Russian file; pi-2-ru\pi1_lookup.py prints the pi-1 Russian line for a Pāli match);
  2. AI_translation\russian\pi-1-pali-russian-termbase-plain.md and 0-INBOX\temp\pipeline\pi-1-ru\termbase\APPROVED.md (the user's decisions);
  3. the Russian pi-3/4/5 termbases and translations (grep, don't read whole). The Vibhaṅga quotes suttas and formulas that pi-4 (Puggalapaññatti) and pi-5 also have.
- AI_translation\skills\zeroshot-translator.md and AI_translation\audience_profile\plain.md.
- **Cross-check of meaning and structure only (translate FROM THE PĀLI):** the English rails translation AI_translation\english\pi-2-english-plain.md and the Hindi one AI_translation\hindi\pi-2-hindi-plain.md (find segments by block ID).

## Source and output
- Source: AI_translation\pali\pi-2_split_chapters\<ch>.md
- Output: AI_translation\russian\pi-2-russian-plain-zeroshot_split_chapters\<ch>.md (same filename; the folder exists).
- 1-khandhavibhango.md only: its first 77 non-empty lines are the approved sample. Reuse 0-INBOX\temp\pipeline\pi-2-ru\ch1-sample.md byte-for-byte as the start of the file and continue from ##### Vedanākkhandho ^2-1-2-2-0.
- These chapters are very repetitive (the same lists, synonym strings and question/answer frames many times). Generate them with a builder script with fixed formula strings, so every repeat is byte-identical.

## Rules
- Identical Pāli = identical Russian, within your chapters, with the approved sample, with the earlier groups and with pi-1 Russian.
- Core: dhamma = явление; abyākata = этически неопределённый; kusala/akusala = благой/неблагой; khandha = совокупность; rūpa = материальная форма; saṅkhāra (aggregate) = формирующие факторы; vicāra = удержание мысли; dosa = злоба; asaṅkhata = необусловленное; paṭiccasamuppāda = возникновение в зависимости от условий; bhāṇavāra = часть для чтения вслух.
- A NEW recurring term or formula you settle goes into 0-INBOX\temp\pipeline\pi-2-ru\notes-<your chapters>.md, one "Pāli = Russian" per line. Do NOT edit ru-zeroshot-terms.md or the sample builder.
- No notes or commentary of your own inside the translation. Variant brackets «[вариант написания (Sī., Syā.): <Pāli>]» for spelling-only variants, «[вариант чтения (…): <Pāli>]» otherwise. "…pe…" → "…". (Ka)/(Kha)/(Ga) → (а)/(б)/(в). Digits stay.
- No "—" or "–" unless the Pāli has one at that spot (same count per line); no ":-". «X – это …» without a comma after a plain noun or list; the comma stays only where it closes a clause, a «кроме» phrase or a participial phrase. «ни … ни» with a participle or verb needs «не». No «ли» in questions.
- Translate the Pāli as written (user rule): no emendations; only plain spelling slips may be rendered as meant. Report suspected slips.

## Verify every chapter (all must pass before you report)
- `python -I -X utf8 0-INBOX\temp\pipeline\check_chapter_ids.py AI_translation\pali\pi-2_split_chapters AI_translation\russian\pi-2-russian-plain-zeroshot_split_chapters <ch>.md` prints OK.
- `python -I -X utf8 0-INBOX\temp\pipeline\dashcheck.py <pali ch> <russian ch>`: equal line counts, 0 dash mismatches, 0 extra em-dashes.
- `python -I -X utf8 0-INBOX\temp\pipeline\pi-1-ru\verify_ru.py <pali ch> <russian ch>` passes.
- No «ли», no Latin outside variant brackets, no double blank lines, no CR. 1-khandhavibhango only: the file starts with ch1-sample.md exactly.

## Final report (short, as text)
- Per chapter: checks passed, segment count.
- Key new terms/formulas (also in your notes file) and what you reused from pi-1 / earlier groups.
- Pāli you were unsure about or that looks like a source slip (translated as written).
