# Brief: Hindi zero-shot of pi-2 (Vibhaṅga), SAMPLE

Work in D:\Work\OpenPecha\abhidhamma-rails. The machine is Windows: use the Read/Write tools for files and PowerShell for commands, run python as `python -I -X utf8`, and write helper scripts to files (inline `python -c` with regexes breaks in PowerShell). Write ONLY the files named below. Do not touch 1-SOURCES\ or 4-SYSTEM\, and do not run git.

This is the SAMPLE the user reviews before the rest of the book is translated in parallel by other agents, who will copy your formulas verbatim. Be careful, exact and consistent.

## Read first (binding)
- **0-INBOX\temp\pipeline\hindi-style.md**: style, the strict dash rule, quotes “…”, «।», cross-book core terms, verify commands.
- AI_translation\skills\zeroshot-translator.md and AI_translation\audience_profile\plain.md.
- **Cross-book Hindi (user-approved and reviewed):** pi-1 (Dhammasaṅgaṇī) is finished in Hindi. The Vibhaṅga reuses its formulas heavily: the matrix triads and dyads (kusalā dhammā, akusalā dhammā, abyākatā dhammā …), the aggregate definitions, the synonym strings, the question/answer frames. **Where the Pāli is identical or nearly identical to pi-1, reuse the pi-1 Hindi wording.** Sources, in order:
  1. AI_translation\hindi\pi-1-hindi-plain-rails_split_chapters\ (the final, reviewed text; 1-matika.md has every matrix item, 3-0x-rupakandam.md the material-form classifications);
  2. AI_translation\hindi\pi-1-pali-hindi-termbase-plain.md (one locked term per Pāli word);
  3. the pi-3/4/5 Hindi termbases and translations (AI_translation\hindi\), grep, don't read whole.
  Find matches by grepping the Pāli in AI_translation\pali\pi-1_split_chapters\ and reading the same line in the pi-1 Hindi rails file (lines align one to one).
- **Cross-check of meaning and structure only (translate FROM THE PĀLI):** the English zero-shot AI_translation\english\pi-2-english-plain-zeroshot_split_chapters\<part>.md (same segments and lines; it still has old paragraph numbers, ignore them).

## Source and output
- Source: AI_translation\pali\pi-2_split_chapters\preamble.md and 1-khandhavibhango.md.
- Write:
  1. AI_translation\hindi\pi-2-hindi-plain-zeroshot_split_chapters\preamble.md (whole file; create the folder).
  2. 0-INBOX\temp\pipeline\pi-2-hi\ch1-sample.md: the Hindi of the FIRST 77 NON-EMPTY LINES of 1-khandhavibhango.md (from `### Khandhavibhaṅgo ^2-1-0` through the last line before `##### Vedanākkhandho ^2-1-2-2-0`), with the same blank lines as the source. The agent who finishes chapter 1 later reuses it byte for byte.
  3. 0-INBOX\temp\pipeline\pi-2-hi\build_ch1_sample_hi.py: a builder with fixed formula strings (constants other agents can import: aggregate names, the past/future/present … synonym strings, question/answer frames, classification frames). Importing it must not rewrite outputs (guard with `if __name__ == "__main__":`).
  4. 0-INBOX\temp\pipeline\pi-2-hi\hi-zeroshot-terms.md: every formula and key term you settled, "Pāli = Hindi", one per line, grouped (book frame, chapter and section headings, aggregate formulas, classification frames, terms). Mark which ones come from pi-1 Hindi and which are new.
- **Book and chapter titles:** propose the Hindi title of the book (Vibhaṅgapāḷi) and Hindi headings for ALL 18 chapters (Khandhavibhaṅga … Dhammahadayavibhaṅga) and for the three recurring section headings (Suttantabhājanīya, Abhidhammabhājanīya, Pañhāpucchaka) in the terms file. Hindi only, no Pāli name and no bracketed gloss (see hindi-style.md "Book titles"). Give one or two alternatives for the book title.

## Rules
- Identical Pāli = identical Hindi, within the sample and with pi-1 Hindi.
- Core: dhamma = परिघटना; abyākata = नैतिक रूप से अनिर्धारित; kusala/akusala = हितकर/हानिकर; khandha = समूह; rūpa = भौतिक रूप.
- No notes or commentary of your own inside the translation. Variant brackets: «[वर्तनी-भेद (Sī., Syā.): <Pāli>]» for spelling-only variants, «[पाठभेद (…): <Pāli>]» otherwise. "…pe…" → "…". (Ka)/(Kha)/(Ga) → (क)/(ख)/(ग). Digits in the Pāli stay as digits.
- No "—" or "–" unless the Pāli has one at that spot (same count per line). No ":-". Never write the words "seed" or "unseeded".

## Verify (all must pass before you report)
- preamble: `python -I 0-INBOX\temp\pipeline\check_chapter_ids.py AI_translation\pali\pi-2_split_chapters AI_translation\hindi\pi-2-hindi-plain-zeroshot_split_chapters preamble.md` prints OK, and `python -I -X utf8 0-INBOX\temp\pipeline\pi-1-hi\verify_hi.py AI_translation\pali\pi-2_split_chapters\preamble.md AI_translation\hindi\pi-2-hindi-plain-zeroshot_split_chapters\preamble.md` passes.
- sample: write the first 77 non-empty Pāli lines (with their blank lines) to 0-INBOX\temp\pipeline\pi-2-hi\ch1-sample-pali.md, then run verify_hi.py and the dash one-liner from hindi-style.md on (ch1-sample-pali.md, ch1-sample.md).
- No Latin-script words left untranslated outside variant brackets, no double blank lines, no CR characters.

## Final report (short)
- Checks passed, segment count.
- The proposed book title (with alternatives) and the chapter/section headings.
- Key formulas and terms, and which were reused from pi-1 Hindi.
- Pāli you were unsure about or that looks like a source slip (translated as written).
