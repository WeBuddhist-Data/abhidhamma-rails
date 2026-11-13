# Brief: Hindi zero-shot of pi-7 (Paṭṭhāna), all files

Work in D:\Work\OpenPecha\abhidhamma-rails. The machine is Windows: use the Read/Write tools for files and PowerShell for commands, run python as `python -I -B -X utf8`, and write helper scripts to files (inline `python -c` with regexes breaks in PowerShell). Several agents translate other files in parallel (the user approved this). Write ONLY your own files in the output folder, plus builder/helper scripts and notes named after your files inside 0-INBOX\temp\pipeline\pi-7-hi\. Never create files at the repo root or in any system temp/scratchpad folder (write scripts with the Write tool, never via a shell redirect). Do not touch 1-SOURCES\ or 4-SYSTEM\, do not edit any other agent's files, and do not run git. Never write the words "seed" or "unseeded". You cannot write report files for me: return your report as text.

The user approved the sample (2026-11-13): the preamble, the book title «कारण-संबंध», the division and section headings, the 24 condition names with «-कारण», and every frame in the terms file. Continue in exactly the same style.

## Read first (binding)
- **0-INBOX\temp\pipeline\hindi-style.md**: style, the strict dash rule, quotes “…”, «।», cross-book core terms.
- **0-INBOX\temp\pipeline\pi-7-hi\hi-zeroshot-terms.md** (READ-ONLY): book frame, division and section headings, the 24 conditions in every case form (positive, negative, count), the paṭicca / sahajāta / paccaya / nissaya / saṃsaṭṭha / sampayutta frames, the pañhāvāra frame, the Siyā question frame, the counting frames, the triad and dyad items, the frames for the later parts of the book. Copy them verbatim.
- **The approved sample** (READ-ONLY): AI_translation\hindi\pi-7-hindi-plain-zeroshot_split_chapters\preamble.md and 1-00-paccaya.md (done; do not rewrite), and 0-INBOX\temp\pipeline\pi-7-hi\sample\ (s2-paticca-anuloma, s3-paticca-paccaniya, s4-panha; each `<name>-pali.md` + `<name>.md`, line-aligned) with its builder 0-INBOX\temp\pipeline\pi-7-hi\build_sample_hi.py. Import it: `sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi"); import build_sample_hi as S` (import only; never edit it or run it as a script).
- AI_translation\skills\zeroshot-translator.md and AI_translation\audience_profile\plain.md.
- **Cross-book Hindi (user-approved, reviewed):** the matrix triads and dyads as in AI_translation\hindi\pi-1-hindi-plain-rails_split_chapters\1-matika.md and the pi-1 termbase AI_translation\hindi\pi-1-pali-hindi-termbase-plain.md (the Paṭṭhāna's triads and dyads ARE the Dhammasaṅgaṇī matrix: use those item names, inflected into the approved frames); pi-2 and pi-6 Hindi (rails files and termbases in AI_translation\hindi\) for other shared terms. Grep, don't read whole files.
- **Cross-check of meaning and structure only (translate FROM THE PĀLI):** the English zero-shot AI_translation\english\pi-7-english-plain-zeroshot_split_chapters\<file>.md (same segments and lines).

## Source and output
- Source: AI_translation\pali\pi-7_split_chapters\<file>.md
- Output: AI_translation\hindi\pi-7-hindi-plain-zeroshot_split_chapters\<file>.md, same filename (the folder exists).
- Lines already in the sample must come out byte-identical to the sample Hindi: 1-01-kusalattika.md non-empty lines 1–128 = s2-paticca-anuloma.md, lines 129–190 = s3-paticca-paccaniya.md, lines 1235–1262 = s4-panha.md.
- The Paṭṭhāna is extremely repetitive (the same frames for every triad/dyad item, every condition, positive and negative, every count). Generate your files with a builder script (build_<your files>_hi.py in pi-7-hi) that composes each line from fixed frames and item tables, so every repeat is byte-identical. Hand-typing repeats is how drift gets in. Read the segments first; then encode them; then read your output.

## Rules
- Identical Pāli = identical Hindi, within your files, with the sample and terms file, and with pi-1/pi-2/pi-6 Hindi for shared terms.
- Headings exactly as in the terms file; keep each heading's #-level and *…* italics.
- **Source slips: translate the Pāli exactly as written**, even where it looks like a slip (a missing "na", a wrong item, tense or number). Only pure spelling slips are rendered as the word meant; agreement slips stay grammatical Hindi. List every slip in your notes and report; do not fix it.
- Variant readings: the Pāli marks them with {…}; render them «[पाठभेद (Syā.): <Pāli>]» or, for spelling-only variants, «[वर्तनी-भेद (…): <Pāli>]», placed after the Hindi word concerned (as in the sample). "…pe…" → "…". (Ka)/(Kha)… → (क)/(ख)…; digits and count markers like "(3)" stay.
- Siyā questions in pucchāvāra-type lines: «क्या … उत्पन्न हो सकती है / हैं?» even where the Pāli ends with "." (user-approved).
- Dashes: "–" exactly where the Pāli has "–" or "—" (same spot, same count per line); never add one; never use ":-".
- A NEW recurring term or frame you settle goes into 0-INBOX\temp\pipeline\pi-7-hi\notes-<your files>.md, one "Pāli = Hindi" per line. Do NOT edit hi-zeroshot-terms.md or the sample.
- No notes or commentary of your own inside the translation.

## Verify every file (all must pass before you report)
- `python -I 0-INBOX\temp\pipeline\check_chapter_ids.py AI_translation\pali\pi-7_split_chapters AI_translation\hindi\pi-7-hindi-plain-zeroshot_split_chapters <file>.md` prints OK.
- `python -I -X utf8 0-INBOX\temp\pipeline\pi-1-hi\verify_hi.py <pali> <hindi>` passes, except two expected kinds of flag: bracket counts where the Pāli uses {…} for variants, and "?" counts on Siyā lines. List any other failure and fix it.
- `python -I -X utf8 0-INBOX\temp\pipeline\pi-1-en\dashcheck.py <pali> <hindi>`: 0 mismatches.
- No Latin-script words left untranslated outside variant brackets, no double blank lines, no CR characters.
- Where your files contain sample lines: they equal the sample byte for byte.

## Final report (short, under 300 words)
- Per file: checks passed, segment count.
- Key new frames/terms (also in your notes file).
- Source slips (translated as written) and Pāli you were unsure about.
