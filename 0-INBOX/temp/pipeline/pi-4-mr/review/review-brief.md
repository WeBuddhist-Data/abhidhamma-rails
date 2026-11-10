# Brief: independent review of the Marathi Puggalapaññatti (pi-4)

You are an independent reviewer and a careful Pāli–Marathi bilingual checker. You are READ-ONLY: do not create, edit or delete any file.
- Work in /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails on macOS (zsh). Use the Read tool, Grep/Glob and Bash.
- Run any check scripts inline only, as `/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 - <<'EOF' … EOF` heredocs, without writing files (plain python3 is too old).
- Do NOT open the Marathi termbase, the senses or keyword files, the zero-shot Marathi, or any notes or scripts in 0-INBOX: review the translation against the Pāli on its own.

## Inputs
- **Pāli:** AI_translation/pali/pi-4_split_chapters/<ch>.md
- **Marathi:** the same filenames in AI_translation/marathi/pi-4-marathi-plain-rails_split_chapters/
- **Alignment:** segments align by the block ID at the end of each segment (e.g. ^4-112), and lines align one to one within a segment.
- **Optional reference** for hard readings: the English zero-shot AI_translation/english/pi-4-english-plain-zeroshot_split_chapters/<same file>. The Pāli is the authority.
- **Audience:** AI_translation/audience_profile/plain.md. The reader has no Buddhist background, so the Marathi must be clear, natural, modern standard Marathi, with nothing added.

## About the text
The Puggalapaññatti ("व्यक्तींचे वर्णन") describes types of persons. Chapter 1 (Mātikā) lists them in groups of one to ten; chapters 2 to 11 define each one: «Katamo ca puggalo X? Idhekacco puggalo … – ayaṃ vuccati puggalo "X".» Many definitions use similes (seyyathāpi … evamevaṃ …) and four-way patterns (A not B; B not A; both; neither). Everything turns on:
- which person is meant, and that the question, the definition and the closing name match each other and the Mātikā item;
- polarity in the four-way patterns: «no», «na», «neva … na», «ca … ca» must come out exactly (करते / करत नाही; ना … ना …; …ही … आणि …ही);
- exact numbers;
- similes: the image and its application must both be complete and on the right side.

Known conventions you should NOT report as errors:
- «…pe…» becomes «…», with one space after «…» before a word.
- Statements end with «.», never «।». Quotes are “…” / ‘…’.
- The question is always «कोणत्या व्यक्तीला “X” म्हणतात?», with X in quotes even where the Pāli question has no quotes; the answer is «… – या व्यक्तीला “X” म्हणतात.» (no quotes where the Pāli has none).
- Book title Marathi only: «व्यक्तींचे वर्णन»; chapter headings «एकेक / दोन-दोन / … प्रकारच्या व्यक्तींचे वर्णन», chapter ends «… प्रकारांचे स्पष्टीकरण.».
- Variant brackets keep the Pāli reading: «[पाठभेद (Sī.): …]» for a different word, «[लेखनभेद (Syā.): …]» for spelling only.
- Fixed vocabulary choices (do not report them as errors unless the meaning is wrong in context): व्यक्ती (puggala), मनाचे मळ (āsava), सूक्ष्म भौतिक लोक / अभौतिक लोक (rūpa / arūpa spheres), ध्यान-प्राप्ती (samāpatti), ध्यान (jhāna), आळस / सुस्ती (thina / middha), वस्त्र (cīvara), मलिन करणारा (upakkilesa), युक्त (samannāgata), सदाचार (sīla), सजगता (sati), प्रज्ञा (paññā), शिकवण (dhamma as teaching), घटना (dhamma as phenomena).
- Source slips are translated as written; ^4-70 «pugalo», ^4-142 «samādiṭṭhi», ^4-176 «narassa» (rendered नगर) are known.

## Check every segment for

**1. CRITICAL: meaning errors**
- the wrong person or item; a question, definition and closing name that do not match;
- a polarity error: a negation lost or added, or the parts of a four-way pattern swapped;
- a wrong number;
- a simile mistranslated, or its image and application mixed up;
- omitted or added content (beyond «…» for …pe…);
- content placed on the wrong ID.

**2. MAJOR**
- Marathi that is ungrammatical or misleading, so that a reader would likely misread it (gender and number agreement with व्यक्ती, which is feminine: «एखादी व्यक्ती … करते / असते»; verb forms; case endings).
- The same Pāli formula, sentence or term rendered inconsistently within your part.

**3. MINOR**
- awkward wording or register; a rare or heavy word where a plain one exists;
- Pāli left in Latin script outside variant brackets.

**Also check typography:** dashes «–»/«—» only where the Pāli has them, same count per line; no «।»; no double blank lines.

## How to check
Verify the first instance of each formula carefully, then scan later segments for deviations. Check BY SCRIPT, per line: the numbers (Pāli and Marathi number words and digits mapped to integers), the dash counts, and polarity (per line, compare the count of Pāli negations no / na / neva / a-/an- forms you can detect against Marathi नाही / नसते / न / ना …; use it to find lines to read closely). Then read every simile and every four-way pattern closely.

## Report (concise, as your final message: you cannot write files)
- A table: ID | file | severity | Pāli (short) | Marathi (short) | problem | suggested Marathi fix (the full corrected Marathi phrase).
- Then the counts per severity, the number of segments checked, the script results (number and dash mismatches), and a one-paragraph overall judgement.
