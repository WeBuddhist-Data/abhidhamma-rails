# Brief: Hindi zero-shot of pi-2 (Vibhaṅga), remaining chapters

Work in D:\Work\OpenPecha\abhidhamma-rails. The machine is Windows: use the Read/Write tools for files and PowerShell for commands, run python as `python -I -X utf8`, and write helper scripts to files (inline `python -c` with regexes breaks in PowerShell). Several agents translate other chapters in parallel (the user approved this). Write ONLY your own chapter files in the output folder, plus builder/helper scripts and notes named after your chapters inside 0-INBOX\temp\pipeline\pi-2-hi\. Do not touch 1-SOURCES\ or 4-SYSTEM\, do not edit any other agent's files, and do not run git.

The user approved the sample (preamble, chapter 1 lines 1–77), the book title «विस्तृत विश्लेषण», all 18 chapter headings and the section headings. Continue in exactly the same style.

## Read first (binding)
- **0-INBOX\temp\pipeline\hindi-style.md**: style, the strict dash rule, quotes “…”, «।», cross-book core terms, verify commands.
- **0-INBOX\temp\pipeline\pi-2-hi\hi-zeroshot-terms.md** (READ-ONLY): book frame, all chapter and section headings, the aggregate formulas, the past/future/present, own/others', coarse/subtle, inferior/superior, far/near strings, question/answer and classification frames, terms. Copy them verbatim.
- **The approved sample and its builder** (READ-ONLY, import, do not edit): 0-INBOX\temp\pipeline\pi-2-hi\ch1-sample.md, built by build_ch1_sample_hi.py. Import with `sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-hi"); import build_ch1_sample_hi as S`. Importing does not rewrite outputs; if it ever does, copy the constants instead.
- AI_translation\skills\zeroshot-translator.md and AI_translation\audience_profile\plain.md.
- **Cross-book Hindi (user-approved and reviewed): pi-1 (Dhammasaṅgaṇī).** The Vibhaṅga reuses its formulas heavily: matrix triads/dyads (Abhidhammabhājanīya and Pañhāpucchaka sections), mind-state lists, synonym strings (lobha, dosa, moha, the factor definitions …), the jhāna formulas, the question/answer frames. **Where the Pāli is identical or nearly identical to pi-1, reuse the pi-1 Hindi wording.** Sources, in order:
  1. AI_translation\hindi\pi-1-hindi-plain-rails_split_chapters\ (final, reviewed; lines align one to one with AI_translation\pali\pi-1_split_chapters\, so grep the Pāli there and read the same line in the Hindi);
  2. AI_translation\hindi\pi-1-pali-hindi-termbase-plain.md (one locked term per Pāli word);
  3. the pi-3/4/5 Hindi termbases and translations in AI_translation\hindi\ (grep, don't read whole).
- **Cross-check of meaning and structure only (translate FROM THE PĀLI):** the English zero-shot AI_translation\english\pi-2-english-plain-zeroshot_split_chapters\<chapter>.md (same segments and lines; some lines still start with an old paragraph number, ignore it).

## Source and output
- Source: AI_translation\pali\pi-2_split_chapters\<chapter>.md
- Output: AI_translation\hindi\pi-2-hindi-plain-zeroshot_split_chapters\<chapter>.md, same filename (the folder exists).
- 1-khandhavibhango.md only: its first 77 non-empty source lines are the approved sample. Reuse 0-INBOX\temp\pipeline\pi-2-hi\ch1-sample.md byte for byte as the start of the file and continue from the next line (##### Vedanākkhandho ^2-1-2-2-0).
- These chapters are very repetitive (the same lists, synonym strings and frames many times). Generate them with a builder script (build_<chapter>_hi.py in pi-2-hi) that uses fixed formula strings, so every repeat is byte-identical. Hand-typing repeats is how drift gets in.

## Rules
- Identical Pāli = identical Hindi, within your chapters, with the approved sample and terms file, and with pi-1 Hindi.
- Chapter headings and the section headings (उपदेशों के अनुसार विश्लेषण / अभिधम्म के अनुसार विश्लेषण / प्रश्नोत्तर) exactly as in the terms file; the closing line of a chapter repeats its heading with «।» as the sample does.
- Core: dhamma = परिघटना (the Teaching = शिक्षा); abyākata = नैतिक रूप से अनिर्धारित; kusala/akusala = हितकर/हानिकर; khandha = समूह; rūpa = भौतिक रूप; sammappadhāna = सही प्रयत्न; vīriya = उत्साह; vāyāma = प्रयास.
- A NEW recurring term or formula you settle goes into 0-INBOX\temp\pipeline\pi-2-hi\notes-<your chapters>.md, one "Pāli = Hindi" per line. Do NOT edit hi-zeroshot-terms.md or the approved sample/builder.
- No notes or commentary of your own inside the translation. Variant brackets as in the sample: «[वर्तनी-भेद (Sī., Syā.): <Pāli>]» for spelling-only variants, «[पाठभेद (…): <Pāli>]» otherwise. "…pe…" → "…". (Ka)/(Kha)/(Ga) → (क)/(ख)/(ग). Digits in the Pāli stay as digits.
- No "—" or "–" unless the Pāli has one at that spot (same count per line). No ":-". Never write the words "seed" or "unseeded".

## Verify every chapter (all must pass before you report)
- `python -I 0-INBOX\temp\pipeline\check_chapter_ids.py AI_translation\pali\pi-2_split_chapters AI_translation\hindi\pi-2-hindi-plain-zeroshot_split_chapters <chapter>.md` prints OK.
- `python -I -X utf8 0-INBOX\temp\pipeline\pi-1-hi\verify_hi.py AI_translation\pali\pi-2_split_chapters\<chapter>.md AI_translation\hindi\pi-2-hindi-plain-zeroshot_split_chapters\<chapter>.md` passes (IDs, lines per segment, dashes, brackets, heading levels).
- No Latin-script words left untranslated outside variant brackets, no double blank lines, no CR characters.
- 1-khandhavibhango only: the first lines of your file equal ch1-sample.md exactly.

## Final report (short)
- Per chapter: checks passed, segment count.
- Key new terms/formulas (also in your notes file), and which pi-1 Hindi passages you reused.
- Pāli you were unsure about or that looks like a source slip (translated as written).
