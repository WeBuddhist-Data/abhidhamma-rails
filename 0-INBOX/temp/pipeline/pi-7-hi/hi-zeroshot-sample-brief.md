# Brief: Hindi zero-shot of pi-7 (Paṭṭhāna), SAMPLE

Work in D:\Work\OpenPecha\abhidhamma-rails. The machine is Windows: use the Read/Write tools for files and PowerShell for commands, run python as `python -I -B -X utf8`, and write helper scripts to files (inline `python -c` with regexes breaks in PowerShell). Write ONLY the files named below (all inside 0-INBOX\temp\pipeline\pi-7-hi\ except the preamble). Never create files at the repo root or in any system temp/scratchpad folder. Do not touch 1-SOURCES\ or 4-SYSTEM\, and do not run git. Never write the words "seed" or "unseeded". You cannot write report files for me: return your report as text.

This is the SAMPLE the user reviews before the rest of the book (75 files, about 4.7 MB of Pāli) is translated in parallel by other agents, who will copy your formulas verbatim. Be careful, exact and consistent.

## About the Paṭṭhāna
The "Book of Conditional Relations" applies the 24 conditions (paccaya: hetu, ārammaṇa, adhipati, anantara, samanantara, sahajāta, aññamañña, nissaya, upanissaya, purejāta, pacchājāta, āsevana, kamma, vipāka, āhāra, indriya, jhāna, magga, sampayutta, vippayutta, atthi, natthi, vigata, avigata) to the triads and dyads of the Dhammasaṅgaṇī matrix (kusalattika etc.). It is almost entirely formulaic:
- the conditions' list (uddesa) and their definitions (niddesa: "Hetupaccayoti – hetū hetusampayuttakānaṃ dhammānaṃ taṃsamuṭṭhānānañca rūpānaṃ hetupaccayena paccayo");
- the question section (pucchāvāra);
- the "dependent on" sections (paṭicca-, sahajāta-, paccaya-, nissaya-, saṃsaṭṭha-, sampayuttavāra): "Kusalaṃ dhammaṃ paṭicca kusalo dhammo uppajjati hetupaccayā – kusalaṃ ekaṃ khandhaṃ paṭicca tayo khandhā …";
- the counting sections (saṅkhyāvāra: "Hetuyā nava, ārammaṇe tīṇi …") and their combinations (dukaṃ, tikaṃ …);
- the negative and mixed sections (paccanīya "nahetupaccayā", anulomapaccanīya, paccanīyānuloma);
- the "question" section proper (pañhāvāra): "Kusalo dhammo kusalassa dhammassa hetupaccayena paccayo – kusalā hetū sampayuttakānaṃ khandhānaṃ hetupaccayena paccayo."
The Hindi must make each sentence readable to a plain reader while keeping every item, number and condition exact.

## Read first (binding)
- **0-INBOX\temp\pipeline\hindi-style.md**: style, the strict dash rule, quotes “…”, «।», cross-book core terms, verify commands.
- AI_translation\skills\zeroshot-translator.md and AI_translation\audience_profile\plain.md.
- **Cross-book Hindi (user-approved and reviewed):** pi-1 to pi-6 are finished in Hindi. Reuse their wording for shared Pāli, above all pi-1 (Dhammasaṅgaṇī: the matrix triads and dyads the Paṭṭhāna is built on) and pi-2 (Vibhaṅga): AI_translation\hindi\pi-1-hindi-plain-rails_split_chapters\1-matika.md and the other pi-1/pi-2 rails files (lines align one to one with AI_translation\pali\pi-1_split_chapters\ and pi-2_split_chapters\), the termbases AI_translation\hindi\pi-1-pali-hindi-termbase-plain.md, pi-2-…, pi-6-…. Grep, don't read whole files.
- Core terms: dhamma = परिघटना; kusala/akusala = हितकर/हानिकर; abyākata = नैतिक रूप से अनिर्धारित; khandha = समूह (the four mental aggregates: अनुभूति, पहचान, मानसिक रचनाएँ, चेतना); rūpa = भौतिक रूप; citta = मन; cittasamuṭṭhāna = मन से उत्पन्न (check pi-1/pi-2); hetu = मूल (as the root condition; check the pi-1 termbase); mātikā = मूल सूची; vipāka after हितकर/हानिकर = «हितकर कर्म के फल रूपी …»; khandha/āyatana/dhātu/indriya/jhāna/magga as in the pi-1/pi-2/pi-6 termbases. The word for paccaya (condition) and each of the 24 condition names are yours to propose: plain Hindi, consistent, and reusing pi-1/pi-2/pi-6 terms where the same Pāli word means the same thing (pi-6 used paccaya = कारण in the ten names of a root).
- **Cross-check of meaning and structure only (translate FROM THE PĀLI):** the English zero-shot AI_translation\english\pi-7-english-plain-zeroshot_split_chapters\<file>.md (same segments and lines).
- **Source slips:** translate the Pāli exactly as written, even where it looks like a slip (a missing "na", a wrong item or tense); only pure spelling slips are rendered as the word meant. List them in your report; do not fix them.

## Source and output
Source: AI_translation\pali\pi-7_split_chapters\. Write:
1. AI_translation\hindi\pi-7-hindi-plain-zeroshot_split_chapters\preamble.md (whole file).
2. AI_translation\hindi\pi-7-hindi-plain-zeroshot_split_chapters\1-00-paccaya.md (whole file: the conditions' list and definitions, and the question section).
3. Three excerpt pairs in 0-INBOX\temp\pipeline\pi-7-hi\sample\, each the Pāli excerpt (`<name>-pali.md`, copied exactly, with the same blank lines as the source) and its Hindi (`<name>.md`), counting NON-EMPTY lines of 1-01-kusalattika.md:
   - `s2-paticca-anuloma`: lines 1–128 (from `###### Kusalattikaṃ ^7-1-1-1-4-0` through the last line before `####### *Paccayapaccanīyaṃ* ^7-1-1-1-4-4-0`).
   - `s3-paticca-paccaniya`: lines 129–190 (from `####### *Paccayapaccanīyaṃ* ^7-1-1-1-4-4-0` through the last line before `####### *Paccayapaccanīyaṃ* ^7-1-1-1-4-5-0`).
   - `s4-panha`: lines 1235–1262 (from `####### *Pañhāvāro* ^7-1-1-1-4-51-0` through the last line before `######## *Anantarapaccayo* ^7-1-1-1-4-52-5-0`).
   The agents who later translate these files must produce identical Hindi for these lines.
4. 0-INBOX\temp\pipeline\pi-7-hi\build_sample_hi.py: a builder with fixed formula strings as importable constants (the 24 condition names in all the case forms used: hetupaccayo / hetupaccayā / hetupaccayena paccayo / nahetupaccayā / hetuyā (counts); the paṭicca frame; the pañhāvāra frame; the triad items in each case; the khandha-count phrases ekaṃ khandhaṃ / tayo khandhā …; numbers in the counting sections; headings). Importing it must not rewrite outputs (guard with `if __name__ == "__main__":`).
5. 0-INBOX\temp\pipeline\pi-7-hi\hi-zeroshot-terms.md: every formula and key term you settled, "Pāli = Hindi", one per line, grouped (book frame; division and section headings: bhāga, dhammānuloma, tikapaṭṭhāna, paccayuddesa/niddesa, pucchāvāra, paṭicca-/sahajāta-/paccaya-/nissaya-/saṃsaṭṭha-/sampayutta-/pañhāvāra, vibhaṅgavāra, saṅkhyāvāra, anuloma/paccanīya/anulomapaccanīya/paccanīyānuloma, ekamūlaka/dumūlaka …; the 24 conditions in every case form, positive and negative; frames; terms). Mark which come from pi-1/pi-2/pi-6 Hindi and which are new. Also give the Hindi for the frames that come later in the book (the other triads, the dyads, duka-tika / tika-duka combinations, all four paccanīya/anuloma sections) so later agents can copy them.
- **Book and division titles:** propose the Hindi title of the book (Paṭṭhānapāḷi) with one or two alternatives, and Hindi headings for its divisions (Tikapaṭṭhāna, Dukapaṭṭhāna, Duka-tika-, Tika-duka-, Tika-tika-, Duka-duka-paṭṭhāna, and the Dhammānuloma / Dhammapaccanīya / Dhammānulomapaccanīya / Dhammapaccanīyānuloma parts). Hindi only, no Pāli name and no bracketed gloss (see hindi-style.md "Book titles"). Approved models: pi-1 «परिघटनाओं की गणना», pi-2 «विस्तृत विश्लेषण», pi-6 «प्रश्नों के जोड़े».

## Rules
- Identical Pāli = identical Hindi, within the sample and with pi-1/pi-2/pi-6 Hindi.
- Questions end with «?»; statements with «।». (Ka)/(Kha)… → (क)/(ख)…; numbers like "(3)", "(1.)" stay as digits. Headings keep their #-level and their *…* italics.
- No notes or commentary of your own inside the translation. Variant brackets: «[वर्तनी-भेद (Sī., Syā.): <Pāli>]» for spelling-only variants, «[पाठभेद (…): <Pāli>]» otherwise. "…pe…" → "…".
- Dashes: "–" exactly where the Pāli has "–" or "—" (this book has many: keep each at the same spot, same count per line); never add one; never use ":-".

## Verify (all must pass before you report)
- preamble and 1-00-paccaya: `python -I 0-INBOX\temp\pipeline\check_chapter_ids.py AI_translation\pali\pi-7_split_chapters AI_translation\hindi\pi-7-hindi-plain-zeroshot_split_chapters <file>` prints OK, and `python -I -X utf8 0-INBOX\temp\pipeline\pi-1-hi\verify_hi.py <pali file> <hindi file>` and `python -I -X utf8 0-INBOX\temp\pipeline\pi-1-en\dashcheck.py <pali file> <hindi file>` pass.
- each sample pair: verify_hi.py and dashcheck.py on `<name>-pali.md` `<name>.md`.
- No Latin-script words left untranslated outside variant brackets, no double blank lines, no CR characters.

## Final report (short, under 400 words)
- Checks passed, segment counts.
- The proposed book title (with alternatives) and the division headings; the main section headings.
- The Hindi for paccaya and the 24 conditions (positive, negative and count forms), the paṭicca and pañhāvāra frames, and which terms were reused from pi-1/pi-2/pi-6 Hindi.
- Pāli you were unsure about or that looks like a source slip (translated as written).
