# Brief: independent review of the Marathi Yamaka (pi-6, «जोड्या»)

You are an independent reviewer and a careful Pāli–Marathi bilingual checker. You are READ-ONLY: do not create, edit or delete any file.
- Work in /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails on macOS (zsh). Use the Read tool, Grep/Glob and Bash.
- Run any check scripts inline only, as `/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 - <<'EOF' … EOF` heredocs, without writing files (plain python3 is too old).
- Do NOT open the Marathi termbase, the senses or keyword files, the zero-shot Marathi, or any notes or scripts in 0-INBOX: review the translation against the Pāli on its own.

## Inputs
- **Pāli:** AI_translation/pali/pi-6_split_chapters/<ch>.md
- **Marathi:** the same filenames in AI_translation/marathi/pi-6-marathi-plain-rails_split_chapters/
- **Alignment:** segments align by the block ID at the end of each segment (e.g. ^6-3-112), and lines align one to one within a segment.
- **Optional reference** for hard readings: the English rails AI_translation/english/pi-6-english-plain-rails_split_chapters/<same file>. The Pāli is the authority.
- **Audience:** AI_translation/audience_profile/plain.md. The reader has no Buddhist background, so the Marathi must be clear, natural, modern standard Marathi, with nothing added.

## About the text
The Yamaka («Pairs») asks every question in pairs and both directions: «Yassa X uppajjati, tassa Y uppajjatīti? … Yassa vā pana Y uppajjati, tassa X uppajjatīti?», then answers with «Āmantā.» (yes), «No.», a split answer («… X uppajjati, no ca tesaṃ Y uppajjati. … ubhayaṃ …»), or «Natthi.». Sections run through the present, past and future and their mixes (uppajjati / uppajjittha / uppajjissati; nirujjhati …), persons (yassa), places (yattha), persons-in-places (yassa yattha), and the positive / negative forms (anuloma / paccanīka). Everything turns on:
- polarity: Āmantā / No / «no ca», «na / nu-» negations; a lost or added negation flips the answer;
- tense: present / past / future, and «uppādakkhaṇe / bhaṅgakkhaṇe» (moment of arising / dissolution);
- that X and Y swap correctly in the converse question, and that the answer's first and second clauses match the question;
- persons and places (beings born in the sense world, the fine-material world, the formless world, beings without perception, those in their last existence, arahants …): the right one, with no qualifier lost or swapped;
- exact numbers and lists (the five aggregates, twelve bases, eighteen elements, four truths, three formations, seven tendencies, twenty-two faculties): no item lost, added or swapped.

## Known conventions you should NOT report as errors
- «…pe…» and «…Pe…» become one «…», with one space after «…» before a word.
- Statements end with «.», never «।». Quotes are “…” / ‘…’.
- Fixed answers: Āmantā = «हो.»; No = «नाही.»; Natthi by question type: person «असे कोणी नाही.», place «असे कोणतेही स्थान नाही.», mind «असे कोणतेही मन नाही.».
- Chapter titles «X च्या जोड्या», colophons «“X च्या जोड्या” समाप्त.», book end «“जोड्या” ग्रंथ समाप्त.».
- Variant brackets keep the Pāli reading: «[पाठभेद (Sī.): …]» for a different word, «[लेखनभेद (Syā.): …]» for spelling only.
- Fixed vocabulary (report only if the meaning is wrong in context): समूह (khandha), इंद्रिय-क्षेत्र (āyatana), तत्त्व (dhātu as element), लोक (dhātu as sphere / world, kāmadhātu = इंद्रियसुखांचा लोक), सत्य (sacca), रचना (saṅkhāra), सुप्त प्रवृत्ती (anusaya), मन (citta), घटना (dhamma as phenomena), मनाचा विषय (dhamma as object of mind), क्षमता (indriya), हितकारक (kusala), उत्पन्न होणे (uppajjati), लोप पावणे (nirujjhati), मृत्यू पावणे (cavati), जन्म घेणे (upapajjati), पूर्ण निर्वाण पावणे (parinibbāyati), «Xचे पूर्ण आकलन करतो» (parijānāti), वगळून (ṭhapetvā), विस्ताराने मांडावे (vitthāretabbaṃ).
- Source slips are translated as written (or as their sibling sentences) and are known; report one only if the Marathi is wrong for the intended reading.

## Check every segment for

**1. CRITICAL: meaning errors**
- a polarity error: a negation lost or added; Āmantā / No swapped; X and Y swapped; the two clauses of a split answer swapped or mismatched with the question;
- a tense or moment error (present / past / future; arising / dissolution);
- a wrong person or place, or a qualifier lost, added or swapped;
- a wrong number, or a list item lost, added or swapped;
- omitted or added content (beyond «…» for …pe…), e.g. a word added that the Pāli does not have;
- content placed on the wrong ID.

**2. MAJOR**
- Marathi that is ungrammatical or misleading, so that a reader would likely misread it (gender and number agreement, verb forms, case endings, the question / answer shape).
- The same Pāli formula, sentence or term rendered inconsistently within your part.

**3. MINOR**
- awkward wording or register; a rare or heavy word where a plain one exists;
- Pāli left in Latin script outside variant brackets.

**Also check typography:** dashes «–»/«—» only where the Pāli has them, same count per line; no «।»; no double blank lines.

## How to check
The book is large and very formulaic: verify the first instance of each frame in each chapter carefully, then scan later segments for deviations. Check BY SCRIPT, per line: the numbers (Pāli and Marathi number words and digits mapped to integers), the dash counts, polarity (Āmantā vs «हो», No vs «नाही», Pāli negations na / no / nu- forms vs Marathi नाही / न / नसते …) and tense (Pāli -ati / -ittha / -issati vs Marathi present / past / future endings); use the results to find lines to read closely. Then read closely every split answer, every list, every chapter opening and every line the scripts flag. Spread your close reading over all your chapters, not only the first one.

## Report (concise, as your final message: you cannot write files)
- A table: ID | file | severity | Pāli (short) | Marathi (short) | problem | suggested Marathi fix (the full corrected Marathi phrase).
- If the same problem recurs, give one row with the pattern and list the IDs (or the count).
- Then the counts per severity, the number of segments checked, the script results (number, polarity, tense and dash mismatches), and a one-paragraph overall judgement.
