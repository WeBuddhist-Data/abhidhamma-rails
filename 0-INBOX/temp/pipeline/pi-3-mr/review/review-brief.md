# Brief: independent review of the Marathi Dhātukathā (pi-3)

You are an independent reviewer and a careful Pāli–Marathi bilingual checker. You are READ-ONLY: do not create, edit or delete any file.
- Work in /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails on macOS (zsh). Use the Read tool, Grep/Glob and Bash.
- Run any check scripts inline only, as `python3 -I -X utf8 - <<'EOF' … EOF` heredocs, without writing files.
- Do NOT open the Marathi termbase, the senses or keyword files, the zero-shot Marathi, or any notes in 0-INBOX: review the translation against the Pāli on its own.

## Inputs
- **Pāli:** AI_translation/pali/pi-3_split_chapters/<ch>.md
- **Marathi:** the same filenames in AI_translation/marathi/pi-3-marathi-plain-rails_split_chapters/
- **Alignment:** segments align by the block ID at the end of each segment (e.g. ^3-112), and lines align one to one within a segment.
- **Optional reference** for hard readings: an independent English translation, the merged file AI_translation/english/pi-3-english-plain.md (find segments by block ID). The Pāli is the authority.
- **Audience:** AI_translation/audience_profile/plain.md. The reader has no Buddhist background, so the Marathi must be clear, natural and modern standard Marathi, with nothing added.

## About the text
The Dhātukathā is a tabular text. It asks in how many aggregates (khandha = समूह), sense bases (āyatana = इंद्रिय-क्षेत्र) and elements (dhātu = तत्त्व) a dhamma (घटना) is included or excluded (saṅgaha / asaṅgaha = समाविष्ट / बाहेर), and with how many it is associated or dissociated (sampayoga / vippayoga = जोडलेले / वेगळे). The answers are numbers. The fourteen methods differ in how the two steps combine. Everything turns on:
- exact numbers;
- included vs excluded and associated vs dissociated;
- negations (na kehici …; «Natthi» = «कशाशीही नाही»; «kehici» = «अंशतः», partly);
- which list item is meant (the triads and dyads of the mātikā).

Known conventions you should NOT report as errors:
- «…pe…» becomes «…», with one space after «…» before a word.
- Statements end with «.» (Marathi), never «।».
- Book titles are Marathi only, in quotes mid-sentence: «तत्त्वांवरील चर्चा», «घटनांची गणना», «विश्लेषण» (Vibhaṅga).
- Variant brackets keep the Pāli reading: «[पाठभेद (Sī.): …]» / «[लेखनभेद (Syā.): …]».
- Source slips are translated as written: ^3-447 «Rūpakkhandhā cattāro» = «भौतिक रूपाच्या समूहानंतरचे चार समूह»; ^3-450 «Natthi?» keeps «?».

## Check every segment for

**1. CRITICAL: meaning errors**
- a wrong number;
- included and excluded swapped, or associated and dissociated swapped;
- a negation lost or added;
- the wrong triad or dyad item, e.g. kusala vs akusala, sahetuka vs hetu, upādinna vs upādāniya;
- the wrong step order in the two-step methods;
- omitted or added content (beyond «…» for …pe…);
- content placed on the wrong ID;
- a summary verse rendered with the wrong meaning.

**2. MAJOR**
- Marathi that is ungrammatical or misleading, so that a reader would likely misread it. This includes number, gender and case agreement with समूह / घटना / इंद्रिय-क्षेत्र / तत्त्व / क्षमता (जोडलेला / जोडलेले / जोडलेल्या, वेगळा / वेगळ्या, आहे / आहेत).
- The same Pāli formula, item or term rendered inconsistently within your part.

**3. MINOR**
- awkward wording or register;
- Pāli left in Latin script outside variant brackets.

**Also check typography:**
- no dashes «–»/«—» (the Pāli has none);
- no «।»;
- no double blank lines.

## How to check
The text is extremely repetitive. Verify the first instance of each formula carefully, then scan later segments for deviations. Check every number against the Pāli BY SCRIPT: map the Pāli number words (ekena/eken…/ekāya = 1, dvīhi = 2, tīhi = 3, catūhi = 4, pañcahi = 5, chahi = 6, sattahi = 7, aṭṭhahi = 8, dasahi = 10, ekādasa… = 11, dvādasa… = 12, soḷasa… = 16, sattarasa… = 17, aṭṭhārasa… = 18) and the Marathi number words to integers, and compare per line. Check polarity BY SCRIPT too: per line, compare the counts of saṅgahit/asaṅgahit with समाविष्ट/बाहेर, sampayutt/vippayutt with जोडलेल/वेगळ, «Natthi» with «कशाशीही नाही», «kehici» with «अंशतः». Read every summary verse closely.

## Report (concise, as your final message: you cannot write files)
- A table: ID | file | severity | Pāli (short) | Marathi (short) | problem | suggested Marathi fix.
- Then the counts per severity, the number of segments checked, the script results (number and polarity mismatches), and a one-paragraph overall judgement.
