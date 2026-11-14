# Brief: independent review of the Hindi Dhātukathā (pi-3)

You are an independent reviewer and a careful Pāli–Hindi bilingual checker. You are READ-ONLY: do not edit any translation file.
- Work in D:\Work\OpenPecha\abhidhamma-rails. It is a Windows machine: use the Read tool, and run python as `python -I -X utf8`.
- Put any helper scripts in 0-INBOX\temp\pipeline\pi-3-hi\review\, named after your part.

## Inputs
- **Pāli:** AI_translation\pali\pi-3_split_chapters\<ch>.md
- **Hindi:** the same filenames in AI_translation\hindi\pi-3-hindi-plain-rails_split_chapters\
- **Alignment:** segments align by the block ID at the end of each segment (e.g. ^3-112).
- **Optional reference** for hard readings: an independent English translation, the merged file AI_translation\english\pi-3-english-plain.md (find segments by block ID). The Pāli is the authority.
- **Audience:** AI_translation\audience_profile\plain.md. The reader has no Buddhist background, so the Hindi must be clear, natural and modern, with nothing added.

## About the text
The Dhātukathā is a tabular text. It asks in how many aggregates (khandha), sense bases (āyatana) and elements (dhātu) a dhamma is included or excluded (saṅgaha / asaṅgaha), and with how many it is associated or dissociated (sampayoga / vippayoga). The answers are numbers. The fourteen methods differ in how the two steps combine. Everything turns on:
- exact numbers;
- included vs excluded and associated vs dissociated;
- negations (na kehici …);
- which list item is meant (the triads and dyads of the mātikā).

## Check every segment for

**1. CRITICAL: meaning errors**
- a wrong number;
- included and excluded swapped, or associated and dissociated swapped;
- a negation lost or added;
- the wrong triad or dyad item, e.g. kusala vs akusala, sahetuka vs hetu, upādinna vs upādāniya;
- the wrong step order in the two-step methods;
- omitted or added content (beyond "…" for …pe…);
- content placed on the wrong ID;
- a summary verse rendered with the wrong meaning.

**2. MAJOR**
- Hindi that is ungrammatical or misleading, so that a reader would likely misread it. This includes number and gender agreement with समूह / परिघटना etc.
- The same Pāli formula, item or term rendered inconsistently within your part.

**3. MINOR**
- awkward wording or register;
- Pāli left in Latin script outside variant brackets.

**Also check typography:**
- no dashes "–"/"—" (the Pāli has none);
- statements end with «।»;
- no double blank lines.

## How to check
The text is extremely repetitive. Verify the first instance of each formula carefully, then scan later segments for deviations. Check every number against the Pāli; a script that extracts and compares the numerals is a good idea. Read every summary verse closely.

## Report (concise)
- A table: ID | file | severity | Pāli (short) | Hindi (short) | problem | suggested Hindi fix.
- Then the counts per severity, the number of segments checked, and a one-paragraph overall judgement.
