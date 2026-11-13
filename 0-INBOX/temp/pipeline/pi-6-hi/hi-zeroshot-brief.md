# Brief: Hindi zero-shot of pi-6 (Yamaka), all chapters

Work in D:\Work\OpenPecha\abhidhamma-rails. The machine is Windows: use the Read/Write tools for files and PowerShell for commands, run python as `python -I -X utf8`, and write helper scripts to files (inline `python -c` with regexes breaks in PowerShell). Several agents translate other chapter files in parallel (the user approved this). Write ONLY your own chapter files in the output folder, plus builder/helper scripts and notes named after your files inside 0-INBOX\temp\pipeline\pi-6-hi\. Never create files at the repo root. Do not touch 1-SOURCES\ or 4-SYSTEM\, do not edit any other agent's files, and do not run git.

The user approved the sample (2026-11-12): the preamble, the book title «प्रश्नों के जोड़े», the 10 chapter headings «X पर प्रश्नों के जोड़े», the section headings and every formula in the terms file. Continue in exactly the same style.

## Read first (binding)
- **0-INBOX\temp\pipeline\hindi-style.md**: style, the strict dash rule, quotes “…”, «।», cross-book core terms, verify commands.
- **0-INBOX\temp\pipeline\pi-6-hi\hi-zeroshot-terms.md** (READ-ONLY): book frame, chapter and section headings, question and answer frames, process vocabulary in every tense/polarity/gender, terms. Copy them verbatim.
- **The approved sample** (READ-ONLY): 0-INBOX\temp\pipeline\pi-6-hi\sample\ (s1-mula, s2-khandha-uddesa, s3-khandha-niddesa, s4-khandha-pavatti; each `<name>-pali.md` + `<name>.md`, line-aligned) and its builder 0-INBOX\temp\pipeline\pi-6-hi\build_sample_hi.py. Import it: `sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-hi"); import build_sample_hi as S` (import only; never edit or run it).
- Three approved choices: (1) the double negative "no ca … nuppajjati / na nirujjhati" is rendered as the positive («पर उनमें … उत्पन्न होता है»), and likewise for every tense; (2) in the word-checking (padasodhana) pairs, a bare word is rendered bare (rūpaṃ «रूप», saṅkhārā «रचनाएँ») while the khandha/āyatana/dhātu/… name gets the full term; (3) hetu = «हेतु», mūla = «मूल».
- AI_translation\skills\zeroshot-translator.md and AI_translation\audience_profile\plain.md.
- **Cross-book Hindi (user-approved, reviewed):** AI_translation\hindi\pi-1-hindi-plain-rails_split_chapters\ and pi-2-hindi-plain-rails_split_chapters\ (line-aligned with AI_translation\pali\pi-1_split_chapters\ and pi-2_split_chapters\), and the termbases AI_translation\hindi\pi-1-pali-hindi-termbase-plain.md and pi-2-pali-hindi-termbase-plain.md: use their terms for the āyatanas, dhātus, truths, saṅkhāras (kāya-/vacī-/cittasaṅkhāra), anusayas, indriyas and realms. pi-3/4/5 Hindi (AI_translation\hindi\) for anything else (grep, don't read whole).
- **Cross-check of meaning and structure only (translate FROM THE PĀLI):** the English rails translation AI_translation\english\pi-6-english-plain-rails_split_chapters\<file>.md (same segments and lines) and AI_translation\english\pi-6-pali-english-termbase-plain.md.

## Source and output
- Source: AI_translation\pali\pi-6_split_chapters\<file>.md
- Output: AI_translation\hindi\pi-6-hindi-plain-zeroshot_split_chapters\<file>.md, same filename (the folder exists; preamble.md is done).
- Lines already in the sample must come out byte-identical to the sample Hindi: 1-mulayamaka.md non-empty lines 1–122 = s1-mula.md; 2-01-khandhayamaka.md lines 1–27 = s2, lines 219–248 = s3, lines 518–547 = s4.
- The Yamaka is extremely repetitive (the same question/answer frames for every pair of items, every tense, positive and negative, person/place). Generate your files with a builder script (build_<file>_hi.py in pi-6-hi) that composes each line from fixed frames and an item table, so every repeat is byte-identical. Hand-typing repeats is how drift gets in. Read the segments first; then encode them.

## Rules
- Identical Pāli = identical Hindi, within your files, with the sample and terms file, and with pi-1/pi-2 Hindi for shared terms.
- Chapter headings and section headings exactly as in the terms file.
- Core: dhamma = परिघटना; kusala/akusala = हितकर/हानिकर; abyākata = नैतिक रूप से अनिर्धारित; khandha = समूह; rūpa = भौतिक रूप; mātikā = मूल सूची.
- A NEW recurring term or frame you settle goes into 0-INBOX\temp\pipeline\pi-6-hi\notes-<your files>.md, one "Pāli = Hindi" per line. Do NOT edit hi-zeroshot-terms.md or the sample.
- No notes or commentary of your own inside the translation. Variant brackets as in the sample: «[वर्तनी-भेद (Sī., Syā.): <Pāli>]» for spelling-only variants, «[पाठभेद (…): <Pāli>]» otherwise. "…pe…" → "…". (Ka)/(Kha)/(Ga)/(Gha)/(Ṅa)/(Ca)… → (क)/(ख)/(ग)/(घ)/(ङ)/(च)…. Digits stay as digits.
- No "—" or "–" unless the Pāli has one at that spot (same count per line). No ":-". Never write the words "seed" or "unseeded".

## Verify every file (all must pass before you report)
- `python -I 0-INBOX\temp\pipeline\check_chapter_ids.py AI_translation\pali\pi-6_split_chapters AI_translation\hindi\pi-6-hindi-plain-zeroshot_split_chapters <file>.md` prints OK.
- `python -I -X utf8 0-INBOX\temp\pipeline\pi-1-hi\verify_hi.py AI_translation\pali\pi-6_split_chapters\<file>.md AI_translation\hindi\pi-6-hindi-plain-zeroshot_split_chapters\<file>.md` passes.
- `python -I -X utf8 0-INBOX\temp\pipeline\pi-1-en\dashcheck.py <pali> <hindi>`: 0 mismatches.
- No Latin-script words left untranslated outside variant brackets, no double blank lines, no CR characters.
- Where your files contain sample lines: they equal the sample byte for byte.

## Final report (short, under 300 words)
- Per file: checks passed, segment count.
- Key new frames/terms (also in your notes file).
- Pāli you were unsure about or that looks like a source slip (translated as written).
