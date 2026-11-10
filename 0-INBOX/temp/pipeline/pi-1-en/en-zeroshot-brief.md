# Brief: English zero-shot of pi-1 (Dhammasaṅgaṇī), remaining parts

Work in D:\Work\OpenPecha\abhidhamma-rails. The machine is Windows: use the Read/Write tools for files and PowerShell for commands, run python as `python -I -X utf8`, and write helper scripts to files (inline `python -c` with regexes breaks in PowerShell). Several agents translate other parts in parallel (the user approved this). Write ONLY your own part files in the output folder, plus helper scripts and notes named after your parts inside 0-INBOX\temp\pipeline\pi-1-en\. Do not touch 1-SOURCES\ or 4-SYSTEM\, and do not run git.

The user approved the chapter-1 sample (the matrix) and the opening of the consciousness chapter. Continue in exactly the same style.

## Read first (binding)
- **0-INBOX\temp\pipeline\english-style.md**: style, the strict dash rule, structure rules, review lessons, verify commands.
- **0-INBOX\temp\pipeline\pi-1-en\en-zeroshot-terms.md** (READ-ONLY): headings for all five chapters, every matrix item keyed by block ID, the question/answer frames, the synonym strings, core terms, approved departures. Copy them verbatim.
- **The approved samples:**
  - AI_translation\english\pi-1-english-plain-zeroshot_split_chapters\1-matika.md (built by 0-INBOX\temp\pipeline\pi-1-en\build_matika.py; `MATRIX_ITEMS` holds every item).
  - 0-INBOX\temp\pipeline\pi-1-en\ch2-01-sample.md (^1-1 … ^1-57), built by build_ch2_01_sample.py. Its constants (NAMES, STRINGS / S_*, FRAMES, Q/A/QA helpers, YEVAPANA, TAJJA …) are importable: `sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-en"); import build_ch2_01_sample as C` (importing must not rebuild the sample; if it does, copy the constants instead of importing).
- AI_translation\skills\zeroshot-translator.md and AI_translation\audience_profile\plain.md.
- Cross-check of wording only (translate FROM THE PĀLI): the English zero-shots of pi-2 and pi-3 (AI_translation\english\pi-2-english-plain-zeroshot_split_chapters\, pi-3-…\) and the English termbases AI_translation\english\pi-3…pi-6-pali-english-termbase-plain.md (grep, don't read whole).

## Fixed decisions (user)
- mātikā is **"matrix"**, never "outline" (headings "The Matrix …", closing lines "The matrix of …").
- Book title: "The Enumeration of Phenomena". dhamma = "states" (running text); abyākata = "indeterminate", never "neutral"; samaya = "time" ("at that time").
- Matrix item names (triads ^1-M1-*, pairs ^1-M2-*) are reused word for word wherever the later chapters name or define them (chapter 3's classifications of material form, chapter 4's summaries, chapter 5's explanations).

## Source and output
- Source: AI_translation\pali\pi-1_split_chapters\<part>.md
- Output: AI_translation\english\pi-1-english-plain-zeroshot_split_chapters\<part>.md, same filename (the folder exists).
- 2-01-cittuppadakandam.md only: its first 122 source lines (^1-1-0 … ^1-57) are the approved sample. Reuse 0-INBOX\temp\pipeline\pi-1-en\ch2-01-sample.md byte-for-byte as the start of the file and continue from the next line (##### Koṭṭhāsavāro ^1-1-1-2-0).
- These chapters are extremely repetitive (the same mind-state lists, synonym strings and question/answer frames hundreds of times). Generate them with a builder script (build_<part>.py in the pi-1-en folder) that uses fixed formula strings, so every repeat is byte-identical. Hand-typing repeats is how drift gets in.

## Rules
- Identical Pāli = identical English, within your parts and with the approved samples and the term file.
- A NEW recurring term or formula you settle goes into 0-INBOX\temp\pipeline\pi-1-en\notes-<your parts>.md, one "Pāli = English" per line. Do NOT edit en-zeroshot-terms.md or the approved samples/builders.
- No notes or commentary of your own inside the translation. Variant brackets: "[variant: <Pāli> (Sī., Syā.)]". "…pe…" → "…". (Ka)/(Kha)/(Ga) → (a)/(b)/(c). Paragraph and list digits stay.

## Verify every part (all must pass before you report)
- `python -I 0-INBOX\temp\pipeline\check_chapter_ids.py AI_translation\pali\pi-1_split_chapters AI_translation\english\pi-1-english-plain-zeroshot_split_chapters <part>.md` prints OK.
- `python -I -X utf8 0-INBOX\temp\pipeline\pi-1-en\dashcheck.py <pali part> <english part>`: equal line counts, 0 dash mismatches.
- No "—" (unless the Pāli has one there), no ":-", no "outline", no double blank lines, no CR characters.
- 2-01 only: the first lines of your file equal ch2-01-sample.md exactly.

## Final report (short)
- Per part: checks passed, segment count.
- Key new terms/formulas (also in your notes file).
- Pāli you were unsure about or that looks like a source slip (translated as written).
