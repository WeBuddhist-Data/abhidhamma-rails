# Brief: independent review of the Hindi Kathāvatthu (pi-5)

You are an independent reviewer and a careful Pāli–Hindi bilingual checker. READ-ONLY: do not edit any translation file.
- Work in D:\Work\OpenPecha\abhidhamma-rails. It is a Windows machine: use the Read tool, and run python as `python -I -X utf8`.
- Put any helper scripts in 0-INBOX\temp\pipeline\pi-5-hi\review\, named after your part.
- Return your full report as text.

## Inputs
- **Pāli:** AI_translation\pali\pi-5_split_chapters\<ch>.md
- **Hindi:** the same filenames in AI_translation\hindi\pi-5-hindi-plain-rails_split_chapters\
- Segments align by the block ID at the end of each segment (e.g. ^5-312).
- **Optional reference for hard readings:** an independent English translation, AI_translation\english\pi-5-english-plain.md. Find segments by block ID. The Pāli is the authority.
- **Audience:** AI_translation\audience_profile\plain.md. The reader has no Buddhist background, so the Hindi must be clear, natural and modern, with nothing added.

## About the text
This is a debate text. Each discussion states a thesis, and the opponent answers either «हाँ।» (Āmantā) or «ऐसा नहीं कहना चाहिए।» (Na hevaṃ vattabbe). The arguments turn on:
- exact negations;
- which side says what;
- the refutation formulas («यदि …, तो निश्चय ही यह कहना चाहिए – “…”।» and the like).

## Check every segment for
1. **CRITICAL:** meaning errors.
   - A thesis negated or un-negated wrongly (na / no / natthi / a- / an-).
   - Āmantā and Na hevaṃ vattabbe swapped.
   - sakavādī and paravādī (our school and the other school) swapped.
   - A wrong term for a doctrinal category, or a wrong number.
   - Content omitted or added (beyond "…" for …pe…).
   - Content on the wrong ID.
   - A quoted sutta or verse rendered with the wrong meaning.
2. **MAJOR:**
   - Ungrammatical or misleading Hindi that a reader would likely misread.
   - The same Pāli formula or term rendered inconsistently within your part.
3. **MINOR:**
   - Awkward wording or register.
   - Pāli left in Latin script outside variant or reference brackets.

**Also check:**
- dashes "–"/"—" appear only where the Pāli has one, with the same count per line;
- statements end with «।»;
- no double blank lines.

The text is extremely formulaic. Verify the first instance of each formula carefully, then scan later segments for deviations by script, e.g. by comparing the sequence of «हाँ।» / «ऐसा नहीं कहना चाहिए।» answers with the Āmantā / Na hevaṃ sequence in the Pāli. Read every quoted sutta and every summary verse (uddāna) closely.

## Report (concise)
- A table with the columns: ID | file | severity | Pāli (short) | Hindi (short) | problem | suggested Hindi fix.
- Then the counts per severity, the number of segments checked, and a one-paragraph overall judgement.
