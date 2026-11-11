# Brief: Hindi zero-shot of pi-1 (Dhammasaṅgaṇī), remaining parts

Work in D:\Work\OpenPecha\abhidhamma-rails. The machine is Windows: use the Read/Write tools for files and PowerShell for commands, run python as `python -I -X utf8`, and write helper scripts to files (inline `python -c` with regexes breaks in PowerShell). Several agents translate other parts in parallel (the user approved this). Write ONLY your own part files in the output folder, plus builder/helper scripts and notes named after your parts inside 0-INBOX\temp\pipeline\pi-1-hi\. Do not touch 1-SOURCES\ or 4-SYSTEM\, do not edit any other agent's files, and do not run git.

The user approved the Hindi chapter-1 sample (the matrix) and the opening of the consciousness chapter. Continue in exactly the same style.

## Read first (binding)
- **0-INBOX\temp\pipeline\hindi-style.md**: style, the strict dash rule, quotes “…”, «।», cross-book core terms, verify commands.
- **0-INBOX\temp\pipeline\pi-1-hi\hi-zeroshot-terms.md** (READ-ONLY): headings for all five chapters (including the proposed ones for chapters 2–5, which are now approved), every matrix item, the question/answer frames, factor names and genders, synonym strings, core terms, approved departures. Copy them verbatim.
- **The approved samples and their builders** (READ-ONLY, import, do not edit):
  - AI_translation\hindi\pi-1-hindi-plain-zeroshot_split_chapters\1-matika.md, built by 0-INBOX\temp\pipeline\pi-1-hi\build_matika_hi.py (`MATRIX_ITEMS_HI`, `BARE`, `QUESTION`, `ANSWER` for the chapter-4/5 question and answer forms).
  - 0-INBOX\temp\pipeline\pi-1-hi\ch2-01-sample.md (^1-1 … ^1-57), built by build_ch2_01_sample_hi.py (NAMES, GENDER, STRINGS, frame helpers, the closing «या उस समय जो भी दूसरी …» line …).
  - Import them: `sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-hi"); import build_matika_hi as M; import build_ch2_01_sample_hi as C`. Importing must not rewrite their outputs; if it does, copy the constants instead.
- AI_translation\skills\zeroshot-translator.md and AI_translation\audience_profile\plain.md.
- **Cross-check of meaning and structure only (translate FROM THE PĀLI):**
  - the approved English zero-shot of the same part, AI_translation\english\pi-1-english-plain-zeroshot_split_chapters\<part>.md, and its builder in 0-INBOX\temp\pipeline\pi-1-en\ (build_*.py, const_*.py, notes-*.md). The builders show exactly which Pāli formula produced which phrase and how the part is structured; mirror that structure in your Hindi builder.
  - the Hindi termbases AI_translation\hindi\pi-3/pi-4/pi-5-pali-hindi-termbase-plain.md and the Hindi pi-3/4/5 zero-shots (grep, don't read whole). Prefer an earlier Hindi rendering for a term the terms file does not settle, unless it clashes with the terms file.

## Source and output
- Source: AI_translation\pali\pi-1_split_chapters\<part>.md
- Output: AI_translation\hindi\pi-1-hindi-plain-zeroshot_split_chapters\<part>.md, same filename (the folder exists).
- 2-01-cittuppadakandam.md only: its first 122 non-empty source lines (^1-1-0 … ^1-57) are the approved sample. Reuse 0-INBOX\temp\pipeline\pi-1-hi\ch2-01-sample.md byte-for-byte as the start of the file and continue from the next segment (##### Koṭṭhāsavāro ^1-1-1-2-0).
- These chapters are extremely repetitive (the same mind-state lists, synonym strings and question/answer frames hundreds of times). Generate them with a builder script (build_<part>_hi.py in pi-1-hi) that uses fixed formula strings, so every repeat is byte-identical. Hand-typing repeats is how drift gets in.

## Rules
- Identical Pāli = identical Hindi, within your parts and with the approved samples and the terms file.
- Matrix item names are reused word for word wherever the later chapters name or define them (chapter 3's classifications of material form, chapter 4's summaries, chapter 5's explanations), with M.QUESTION / M.ANSWER for the question and answer frames.
- Core: dhamma = परिघटना; abyākata = नैतिक रूप से अनिर्धारित; kusala/akusala = हितकर/हानिकर; mātikā = मूल सूची.
- A NEW recurring term or formula you settle goes into 0-INBOX\temp\pipeline\pi-1-hi\notes-<your parts>.md, one "Pāli = Hindi" per line. Do NOT edit hi-zeroshot-terms.md or the approved samples/builders.
- No notes or commentary of your own inside the translation. Variant brackets as in the sample: «[वर्तनी-भेद (Sī., Syā.): <Pāli>]» for spelling-only variants, «[पाठभेद (…): <Pāli>]» otherwise. "…pe…" → "…". (Ka)/(Kha)/(Ga) → (क)/(ख)/(ग). Paragraph and list digits stay.
- No "—" or "–" unless the Pāli has one at that spot (same count per line). No ":-". Never write the words "seed" or "unseeded".

## Verify every part (all must pass before you report)
- `python -I -X utf8 0-INBOX\temp\pipeline\check_chapter_ids.py AI_translation\pali\pi-1_split_chapters AI_translation\hindi\pi-1-hindi-plain-zeroshot_split_chapters <part>.md` prints OK.
- `python -I -X utf8 0-INBOX\temp\pipeline\pi-1-en\dashcheck.py <pali part> <hindi part>`: equal line counts, 0 dash mismatches, 0 extra em-dashes.
- `python -I -X utf8 0-INBOX\temp\pipeline\pi-1-hi\verify_hi.py <pali part> <hindi part>` passes.
- No Latin-script words left untranslated outside variant brackets (except quoted Pāli titles if the sample does so), no double blank lines, no CR characters.
- 2-01 only: the first lines of your file equal ch2-01-sample.md exactly.

## Final report (short)
- Per part: checks passed, segment count.
- Key new terms/formulas (also in your notes file).
- Pāli you were unsure about or that looks like a source slip (translated as written).
