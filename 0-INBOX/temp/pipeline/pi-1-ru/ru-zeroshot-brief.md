# Brief: Russian zero-shot of pi-1 (Dhammasaṅgaṇī), remaining parts

Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: use the Read/Write tools for files and PowerShell for commands, run python as `python -I -X utf8`, and write helper scripts to files with the Write tool (inline `python -c` with regexes breaks in PowerShell; never write files via a shell redirect). Several agents translate other parts in parallel (the user approved this). Write ONLY your own part files in the output folder, plus builder/helper scripts and notes named after your parts inside 0-INBOX\temp\pipeline\pi-1-ru\. Never create files at the repo root or in a system temp folder. Do not touch 1-SOURCES\ or 4-SYSTEM\, do not edit any other agent's files, do not run git, never write "seed" or "unseeded". You cannot write report files for me: return your report as text.

The user approved the Russian sample (the matrix and the opening of the consciousness chapter) on 2026-11-14. Continue in exactly the same style.

## Read first (binding)
- **0-INBOX\temp\pipeline\russian-style.md**: style, the strict DASH RULE, «…»/„…“ quotes, no «ли», core terms, review lessons, verify commands.
- **0-INBOX\temp\pipeline\pi-1-ru\ru-zeroshot-terms.md** (READ-ONLY): headings for all five chapters (the proposed ones for chapters 2–5 are approved), every matrix item with its question and answer form, the factor names, the synonym strings, the frames and the term choices. Copy them verbatim.
- **The approved samples and their builders** (READ-ONLY; import, do not edit):
  - AI_translation\russian\pi-1-russian-plain-zeroshot_split_chapters\1-matika.md, built by 0-INBOX\temp\pipeline\pi-1-ru\build_matika_ru.py (ITEMS, BARE, PRED, QUESTION, ANSWER, ANSWER_BARE for the chapter-4/5 question and answer forms).
  - 0-INBOX\temp\pipeline\pi-1-ru\ch2-01-sample.md (^1-1-0 … ^1-57), built by build_ch2_01_sample_ru.py (factor names with their case forms and genders, synonym strings, frame helpers, the closing «или же любые другие …» line).
  - Import them: `sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-ru"); import build_matika_ru as M; import build_ch2_01_sample_ru as C`. Importing does not rewrite their outputs.
- AI_translation\skills\zeroshot-translator.md and AI_translation\audience_profile\plain.md.
- **Cross-check of meaning and structure only (translate FROM THE PĀLI):** 0-INBOX\temp\pipeline\pi-1-ru\ref\ holds the approved English and Hindi builders and notes for every part (en_build_<part>.py, en_const_2_03_2_04.py, en_notes-<part>.md, hi_build_<part>_hi.py, hi_notes-<part>.md). They show exactly which Pāli formula produced which phrase and how each part is structured; mirror that structure in your Russian builder. The finished texts are in AI_translation\english\pi-1-english-plain-zeroshot_split_chapters\ and AI_translation\hindi\pi-1-hindi-plain-zeroshot_split_chapters\ (same filenames). For a term the terms file does not settle, prefer the Russian pi-3/4/5 termbases (AI_translation\russian\pi-*-pali-russian-termbase-plain.md; grep, don't read whole), unless russian-style.md says otherwise.

## Source and output
- Source: AI_translation\pali\pi-1_split_chapters\<part>.md
- Output: AI_translation\russian\pi-1-russian-plain-zeroshot_split_chapters\<part>.md, same filename (the folder exists).
- 2-01-cittuppadakandam.md only: its first 122 non-empty source lines (^1-1-0 … ^1-57) are the approved sample. Reuse 0-INBOX\temp\pipeline\pi-1-ru\ch2-01-sample.md byte-for-byte as the start of the file and continue from the next segment.
- These chapters are extremely repetitive (the same mind-state lists, synonym strings and question/answer frames hundreds of times). Generate them with a builder script (build_<part>_ru.py in pi-1-ru) that uses fixed formula strings, so every repeat is byte-identical. Hand-typing repeats is how drift gets in.

## Rules
- Identical Pāli = identical Russian, within your parts and with the approved samples and the terms file.
- Matrix item names are reused word for word wherever later chapters name or define them (chapter 3's classifications of material form, chapter 4's summaries, chapter 5's explanations), with M.QUESTION / M.ANSWER for the question and answer frames, inflected only where Russian grammar forces it (then build the inflected form once and reuse it).
- Core choices (approved): dhamma = явление; abyākata = этически неопределённый; kusala/akusala = благой/неблагой; mātikā = матрица; vicāra = удержание мысли; saṅkhāra (aggregate) = формирующие факторы; dosa = злоба; asaṅkhata = необусловленное; paṭiccasamuppāda = возникновение в зависимости от условий; pahātabbahetukā = «явления, чьи корни устраняются …» (user fix 2026-11-14).
- A NEW recurring term or formula you settle goes into 0-INBOX\temp\pipeline\pi-1-ru\notes-<your parts>.md, one "Pāli = Russian" per line. Do NOT edit ru-zeroshot-terms.md or the approved samples/builders.
- No notes or commentary of your own inside the translation. Variant brackets as in the sample: «[вариант написания (Sī., Syā.): <Pāli>]» for spelling-only variants, «[вариант чтения (…): <Pāli>]» otherwise. "…pe…" → "…". (Ka)/(Kha)/(Ga) → (а)/(б)/(в). Paragraph and list digits stay.
- No "—" or "–" unless the Pāli has one at that spot (same count per line). No ":-". No «ли» in questions.
- Translate the Pāli as written; report suspected source slips instead of fixing them (plain spelling slips may be rendered as meant).

## Verify every part (all must pass before you report)
- `python -I -X utf8 0-INBOX\temp\pipeline\check_chapter_ids.py AI_translation\pali\pi-1_split_chapters AI_translation\russian\pi-1-russian-plain-zeroshot_split_chapters <part>.md` prints OK.
- `python -I -X utf8 0-INBOX\temp\pipeline\dashcheck.py <pali part> <russian part>`: equal line counts, 0 dash mismatches, 0 extra em-dashes.
- `python -I -X utf8 0-INBOX\temp\pipeline\pi-1-ru\verify_ru.py` (read its usage line first) passes for your parts.
- No Latin-script words outside variant brackets, no «ли», no double blank lines, no CR characters.
- 2-01 only: the first lines of your file equal ch2-01-sample.md exactly.

## Final report (short, as text)
- Per part: checks passed, segment count.
- Key new terms/formulas (also in your notes file).
- Pāli you were unsure about or that looks like a source slip (translated as written).
