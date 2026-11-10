# Brief: independent review of the Hindi Puggalapaññatti (pi-4)

You are an independent reviewer and a careful Pāli–Hindi bilingual checker. Treat this as READ-ONLY: do not edit any translation file.
- Work in D:\Work\OpenPecha\abhidhamma-rails. The machine runs Windows; use the Read tool, and run python as `python -I -X utf8`.
- Put any helper scripts in 0-INBOX\temp\pipeline\pi-4-hi\review\, named after your part.
- Return your full report as text. Subagents cannot write report files.

## Inputs
- **Pāli:** AI_translation\pali\pi-4_split_chapters\<ch>.md
- **Hindi:** the same filenames in AI_translation\hindi\pi-4-hindi-plain-rails_split_chapters\
- Segments align by the block ID at the end of each segment (e.g. ^4-112).
- **Optional reference for hard readings:** the independent English translation, AI_translation\english\pi-4-english-plain.md (find segments by block ID). The Pāli is the authority.
- **Audience:** AI_translation\audience_profile\plain.md. The reader has no Buddhist background. The Hindi should be clear, natural and modern, with nothing added.

## About the text
The Puggalapaññatti is a "Designation of Persons":
- Chapter 1 is the mātikā, a list of person types grouped in ones, twos, … tens.
- Chapters 2–11 define each type with "Katamo ca puggalo X? Idhekacco puggalo … – ayaṃ vuccati puggalo X."
- There are also similes (clouds, mice, mangoes, pots, ponds, bulls, snakes, trees).
- The noble-person definitions repeat across chapters 2, 4, 8 and 10.

## Check every segment for
**CRITICAL: meaning errors**
- a negation lost or added (na, a-/an-, no ce);
- the person type confused with its pair (kuppa/akuppa, sekkha/asekkha, attantapa/parantapa …);
- the wrong mātikā name;
- a wrong number;
- the wrong simile mapping (which half of the simile is which person);
- omitted or added content beyond "…" for …pe…;
- content on the wrong ID;
- a quoted verse rendered with the wrong meaning.

**MAJOR**
- Ungrammatical or misleading Hindi, i.e. a sentence a reader would likely misread.
- The same Pāli formula, name or term rendered inconsistently within your part. A mātikā name must read the same in the mātikā, the question and the closing line.

**MINOR**
- Awkward wording or register.
- Pāli left in Latin script outside variant or reference brackets.

**Also check:**
- dashes "–"/"—" only where the Pāli has them, with the same count per line;
- statements end with «।»;
- no double blank lines.

## Approach
The text is formulaic. Verify the first instance of each formula carefully, then scan later segments for deviations. For each definition, check by script that the name in the question and the closing line matches the mātikā (chapter 1) name. Read every simile and verse closely.

## Report (concise)
- A table: ID | file | severity | Pāli (short) | Hindi (short) | problem | suggested Hindi fix.
- Then counts per severity, the number of segments checked, and a one-paragraph overall judgement.
