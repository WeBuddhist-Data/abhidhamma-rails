# Brief: Vietnamese zero-shot of pi-1 (Dhammasaṅgaṇī), remaining parts

Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: use the Read/Write tools for files and PowerShell for commands, run python as `python -I -X utf8`, and write helper scripts to files with the Write tool (inline `python -c` with regexes breaks in PowerShell; never write files via a shell redirect). Agents run ONE AT A TIME, in book order; earlier parts are finished and their builders can be imported. Write ONLY your own part files in the output folder, plus builder/helper scripts and notes named after your parts inside 0-INBOX\temp\pipeline\pi-1-vi-ai\. Never create files at the repo root or in a system temp folder. Do not touch 1-SOURCES\ or 4-SYSTEM\, do not edit earlier agents' files, do not run git, never write "seed" or "unseeded". You cannot write report files for me: return your report as text.

The user approved the Vietnamese sample (the matrix and the opening of the consciousness chapter) on 2026-11-17, with sati = «sự tỉnh thức». Continue in exactly the same style.

## FORBIDDEN (copyrighted reference translation)
Never open, grep or search: 1-SOURCES\Translations\Vietnamese\vi-*.md, 0-INBOX\raw-data\vi-*, 0-INBOX\temp\pipeline\pi-1-vi\, pi-2-vi\, pi-3-4-vi\, pi-5-vi\, pi-6-vi\, pi-7-vi\, pi-1-th-vi\, vi-tools\. No web searches for Vietnamese Abhidhamma translations. Do not run folder-wide searches over 0-INBOX\temp\pipeline\, 1-SOURCES\ or AI_translation\ (search only the specific files named here).

## Read first (binding)
- **0-INBOX\temp\pipeline\vietnamese-style.md**: style, the strict DASH RULE, quotes, review lessons, approved core terms, verify commands.
- **0-INBOX\temp\pipeline\pi-1-vi-ai\vi-core-terms.md** and **vi-zeroshot-terms.md** (READ-ONLY): the approved core terms; headings for all five chapters (the proposed ones for chapters 2–5 are approved), every matrix item with its question and answer form, the factor names, the synonym strings, the frames. Copy them verbatim.
- **Notes of earlier parts**: 0-INBOX\temp\pipeline\pi-1-vi-ai\notes-*.md (READ-ONLY). Terms settled there are binding for you too.
- **The approved samples and their builders** (READ-ONLY; import, do not edit):
  - AI_translation\vietnamese\pi-1-vietnamese-plain-zeroshot_split_chapters\1-matika.md, built by 0-INBOX\temp\pipeline\pi-1-vi-ai\build_matika_vi.py (ITEMS, BARE, PRED, QUESTION, ANSWER, ANSWER_BARE, MATRIX_ITEMS_VI).
  - 0-INBOX\temp\pipeline\pi-1-vi-ai\ch2-01-sample.md (^1-1-0 … ^1-57), built by build_ch2_01_sample_vi.py (factor names, synonym strings, frame helpers, the closing «hoặc bất cứ hiện tượng phi vật chất nào khác …» line).
  - Import them: `sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-vi-ai"); import build_matika_vi as M; import build_ch2_01_sample_vi as C`. Earlier part builders (build_<part>_vi.py) can be imported the same way; importing must not rewrite their outputs.
- AI_translation\skills\zeroshot-translator.md and AI_translation\audience_profile\plain.md.
- **Cross-check of meaning and structure only (translate FROM THE PĀLI):**
  - 0-INBOX\temp\pipeline\pi-1-ru\ref\ holds the approved English and Hindi builders and notes for every part (en_build_<part>.py, en_const_2_03_2_04.py, en_notes-<part>.md, hi_build_<part>_hi.py, hi_notes-<part>.md). They show which Pāli formula produced which phrase and how each part is structured.
  - The approved Russian builders for the same parts, the closest model: 0-INBOX\temp\pipeline\pi-1-ru\build_<part>_ru.py and notes-<part>.md.
  - Finished texts: AI_translation\english\pi-1-english-plain-zeroshot_split_chapters\ and AI_translation\russian\pi-1-russian-plain-zeroshot_split_chapters\ (same filenames).

## Source and output
- Source: AI_translation\pali\pi-1_split_chapters\<part>.md
- Output: AI_translation\vietnamese\pi-1-vietnamese-plain-zeroshot_split_chapters\<part>.md, same filename.
- 2-01-cittuppadakandam.md only: its first 122 non-empty source lines (^1-1-0 … ^1-57) are the approved sample. Reuse 0-INBOX\temp\pipeline\pi-1-vi-ai\ch2-01-sample.md byte-for-byte as the start of the file and continue from the next segment.
- These chapters are extremely repetitive. Generate them with a builder script (build_<part>_vi.py in pi-1-vi-ai) that uses fixed formula strings, so every repeat is byte-identical. Hand-typing repeats is how drift gets in.

## Rules
- Identical Pāli = identical Vietnamese, within your parts, with the approved samples, the terms file and the earlier parts.
- Matrix item names are reused word for word wherever later chapters name or define them (chapter 3's classifications of material form, chapter 4's summaries, chapter 5's explanations), with M.QUESTION / M.ANSWER for the question and answer frames.
- sati = «sự tỉnh thức» (năng lực tỉnh thức, sức mạnh tỉnh thức, tỉnh thức đúng đắn, micchāsati = tỉnh thức sai lầm). Never «chánh niệm».
- A NEW recurring term or formula you settle goes into 0-INBOX\temp\pipeline\pi-1-vi-ai\notes-<your parts>.md, one "Pāli = Vietnamese" per line. Do NOT edit vi-zeroshot-terms.md, vi-core-terms.md or the approved samples/builders.
- No notes or commentary of your own inside the translation. Variant brackets as in the sample: "[khác chính tả (Sī., Syā.): <Pāli>]" for spelling-only variants, "[dị bản (…): <Pāli>]" otherwise. "…pe…" → "…". (Ka)/(Kha)/(Ga) → (a)/(b)/(c). Paragraph and list digits stay.
- No "—" or "–" unless the Pāli has one at that spot (same count per line). No ":-".
- Translate the Pāli as written; report suspected source slips instead of fixing them (plain spelling slips may be rendered as meant).

## Verify every part (all must pass before you report)
- `python -I -X utf8 0-INBOX\temp\pipeline\check_chapter_ids.py AI_translation\pali\pi-1_split_chapters AI_translation\vietnamese\pi-1-vietnamese-plain-zeroshot_split_chapters <part>.md` prints OK.
- `python -I -X utf8 0-INBOX\temp\pipeline\dashcheck.py <pali part> <vietnamese part>`: equal line counts, 0 dash mismatches, 0 extra em-dashes.
- `python -I -X utf8 0-INBOX\temp\pipeline\pi-1-vi-ai\verify_vi.py` (read it first; extend it with a copy for your parts if it only covers the sample) passes for your parts.
- No Latin-script words outside variant brackets and citations, no double blank lines, no CR, NFC, no «chánh niệm».
- 2-01 only: the first lines of your file equal ch2-01-sample.md exactly.

## Final report (short, as text)
- Per part: checks passed, segment count.
- Key new terms/formulas (also in your notes file).
- Pāli you were unsure about or that looks like a source slip (translated as written).
