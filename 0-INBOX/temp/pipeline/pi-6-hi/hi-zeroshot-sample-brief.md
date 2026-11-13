# Brief: Hindi zero-shot of pi-6 (Yamaka), SAMPLE

Work in D:\Work\OpenPecha\abhidhamma-rails. The machine is Windows: use the Read/Write tools for files and PowerShell for commands, run python as `python -I -X utf8`, and write helper scripts to files (inline `python -c` with regexes breaks in PowerShell). Write ONLY the files named below (all inside 0-INBOX\temp\pipeline\pi-6-hi\ except the preamble). Never create files at the repo root. Do not touch 1-SOURCES\ or 4-SYSTEM\, and do not run git.

This is the SAMPLE the user reviews before the rest of the book (43 chapter files, about 2 MB of Pāli) is translated in parallel by other agents, who will copy your formulas verbatim. Be careful, exact and consistent.

## About the Yamaka
The "Book of Pairs" asks every question twice, forward (Ka) and converse (Kha), and answers with fixed formulas: "Āmantā" (yes), a qualified answer naming the exceptions ("X, na Y. Y X ceva Y ca."), or, in the process sections (pavattivāra), answers about which beings (puggala) or places (okāsa) a thing arises in or ceases in, at rebirth (upapajjanta) or at death (cavanta), in the five-aggregate existence (pañcavokāra), the formless (arūpa) or the non-percipient beings (asaññasatta). Everything is a permutation: anuloma (positive) and paccanīka (negative, na/no), past/present/future tenses (uppajjittha / uppajjati / uppajjissati), person/place/person-and-place. The Hindi must make each question and answer readable to a plain reader while keeping every permutation exact.

## Read first (binding)
- **0-INBOX\temp\pipeline\hindi-style.md**: style, the strict dash rule, quotes “…”, «।», cross-book core terms, verify commands.
- AI_translation\skills\zeroshot-translator.md and AI_translation\audience_profile\plain.md.
- **Cross-book Hindi (user-approved and reviewed):** pi-1 (Dhammasaṅgaṇī) and pi-2 (Vibhaṅga) are finished in Hindi. Reuse their wording for shared Pāli: AI_translation\hindi\pi-1-hindi-plain-rails_split_chapters\ and pi-2-hindi-plain-rails_split_chapters\ (final, reviewed; lines align one to one with AI_translation\pali\pi-1_split_chapters\ and pi-2_split_chapters\), and the termbases AI_translation\hindi\pi-1-pali-hindi-termbase-plain.md and pi-2-pali-hindi-termbase-plain.md. Core terms: dhamma = परिघटना; kusala/akusala = हितकर/हानिकर; abyākata = नैतिक रूप से अनिर्धारित; khandha = समूह (rūpakkhandha = भौतिक रूप का समूह, vedanā = अनुभूति, saññā = पहचान, saṅkhārā = मानसिक रचनाएँ, viññāṇa = चेतना); mūla/hetu = मूल; āyatana = इंद्रिय-क्षेत्र; dhātu = तत्व; sacca = सत्य; anusaya = सुप्त प्रवृत्ति (check pi-1/pi-2 termbases first); citta = मन; indriya = क्षमता; rūpa sphere = सूक्ष्म भौतिक लोक, arūpa = अभौतिक लोक; mātikā = मूल सूची. The pi-3/4/5 Hindi files (AI_translation\hindi\) for anything else (grep, don't read whole).
- **Cross-check of meaning and structure only (translate FROM THE PĀLI):** the English rails translation AI_translation\english\pi-6-english-plain-rails_split_chapters\<file>.md (same segments and lines) and the English termbase AI_translation\english\pi-6-pali-english-termbase-plain.md.

## Source and output
Source: AI_translation\pali\pi-6_split_chapters\. Write:
1. AI_translation\hindi\pi-6-hindi-plain-zeroshot_split_chapters\preamble.md (whole file).
2. Four excerpt pairs in 0-INBOX\temp\pipeline\pi-6-hi\sample\, each the Pāli excerpt (`<name>-pali.md`, copied exactly, with the same blank lines as the source) and its Hindi (`<name>.md`), counting NON-EMPTY lines of the source file:
   - `s1-mula`: 1-mulayamaka.md lines 1–122 (from `### Mūlayamakaṃ ^6-1-0` through the last line before `##### (Kha) niddeso ^6-1-11-1-0`).
   - `s2-khandha-uddesa`: 2-01-khandhayamaka.md lines 1–27 (through the last line before `#### Padasodhanamūlacakkavāro ^6-2-3-0`).
   - `s3-khandha-niddesa`: 2-01-khandhayamaka.md lines 219–248 (from `#### Paṇṇattivāraniddesa ^6-2-6-0` through the last line before `#### Padasodhanamūlacakkavāro ^6-2-8-0`).
   - `s4-khandha-pavatti`: 2-01-khandhayamaka.md lines 518–547 (from `#### Pavattivāro 1. uppādavāro ^6-2-11-0` through the last line before `#### (2) Atītavāro ^6-2-13-0`).
   The agents who later translate these chapters must produce identical Hindi for these lines.
3. 0-INBOX\temp\pipeline\pi-6-hi\build_sample_hi.py: a builder with fixed formula strings as importable constants (question frames Ka/Kha, "Āmantā", the qualified-answer frames, the person/place/person-and-place frames, tense forms of uppajjati / nirujjhati, rebirth/death/being-type phrases, the root (mūla) naya names, headings). Importing it must not rewrite outputs (guard with `if __name__ == "__main__":`).
4. 0-INBOX\temp\pipeline\pi-6-hi\hi-zeroshot-terms.md: every formula and key term you settled, "Pāli = Hindi", one per line, grouped (book frame; chapter headings; section headings: uddesa/niddesa, paṇṇattivāra, padasodhana(-mūlacakka)vāra, suddha…vāra, pavattivāra, uppāda/nirodha/uppādanirodhavāra, paccuppanna/atīta/anāgata…vāra, anuloma/paccanīka, puggala/okāsa; answer frames; terms). Mark which come from pi-1/pi-2 Hindi and which are new. Also give the Hindi for the process vocabulary in its past/present/future and negative forms (uppajjittha, uppajjati, uppajjissati, nuppajjati, nirujjhati …), even beyond the sample, so later agents can copy it.
- **Book and chapter titles:** propose the Hindi title of the book (Yamakapāḷi) with one or two alternatives, and Hindi headings for ALL 10 chapters (Mūla-, Khandha-, Āyatana-, Dhātu-, Sacca-, Saṅkhāra-, Anusaya-, Citta-, Dhamma-, Indriyayamaka). Hindi only, no Pāli name and no bracketed gloss (see hindi-style.md "Book titles"). Approved models: pi-1 «परिघटनाओं की गणना», pi-2 «विस्तृत विश्लेषण» with chapters «X का विश्लेषण».

## Rules
- Identical Pāli = identical Hindi, within the sample and with pi-1/pi-2 Hindi.
- Questions end with «?»; statements with «।». (Ka)/(Kha)/(Ga)/(Gha)/(Ṅa)/(Ca) → (क)/(ख)/(ग)/(घ)/(ङ)/(च). Numbers like "(1)", "2-10." stay as digits.
- No notes or commentary of your own inside the translation. Variant brackets: «[वर्तनी-भेद (Sī., Syā.): <Pāli>]» for spelling-only variants, «[पाठभेद (…): <Pāli>]» otherwise. "…pe…" → "…".
- No "—" or "–" unless the Pāli has one at that spot (same count per line). No ":-". Never write the words "seed" or "unseeded".

## Verify (all must pass before you report)
- preamble: `python -I 0-INBOX\temp\pipeline\check_chapter_ids.py AI_translation\pali\pi-6_split_chapters AI_translation\hindi\pi-6-hindi-plain-zeroshot_split_chapters preamble.md` prints OK, and `python -I -X utf8 0-INBOX\temp\pipeline\pi-1-hi\verify_hi.py AI_translation\pali\pi-6_split_chapters\preamble.md AI_translation\hindi\pi-6-hindi-plain-zeroshot_split_chapters\preamble.md` passes.
- each sample pair: `python -I -X utf8 0-INBOX\temp\pipeline\pi-1-hi\verify_hi.py <name>-pali.md <name>.md` and `python -I -X utf8 0-INBOX\temp\pipeline\pi-1-en\dashcheck.py <name>-pali.md <name>.md`.
- No Latin-script words left untranslated outside variant brackets, no double blank lines, no CR characters.

## Final report (short, under 350 words)
- Checks passed, segment counts.
- The proposed book title (with alternatives) and the 10 chapter headings; the main section headings.
- Key formulas and terms (the question frame, Āmantā, the qualified answer, the person/place frames, rebirth/death phrases), and which were reused from pi-1/pi-2 Hindi.
- Pāli you were unsure about or that looks like a source slip (translated as written).
