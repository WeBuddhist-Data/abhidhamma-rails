# Brief: independent review of the Hindi Paṭṭhāna (pi-7)

You are an independent reviewer and a careful Pāli–Hindi bilingual checker. You are READ-ONLY: do not edit any translation file.
- Work in D:\Work\OpenPecha\abhidhamma-rails. It is a Windows machine: use the Read tool, write scripts with the Write tool, and run python as `python -I -B -X utf8`.
- Put any helper scripts in 0-INBOX\temp\pipeline\pi-7-hi\review\, named after your part (review_<part>_*.py). Never create files at the repo root or in a system temp folder. Do not run git. Never write "seed" or "unseeded".
- Do not open the termbase, the keyword maps, the zero-shot Hindi, or any notes, builders or reports in 0-INBOX\temp\pipeline\pi-7-hi\ (rails\ included): the point is a reading that is not anchored on them.

## Inputs
- **Pāli:** AI_translation\pali\pi-7_split_chapters\<f>.md
- **Hindi:** the same filenames in AI_translation\hindi\pi-7-hindi-plain-rails_split_chapters\
- **Alignment:** segments align by the block ID at the end of each segment. Non-empty lines align one to one.
- **Optional reference** for hard readings: the English zero-shot AI_translation\english\pi-7-english-plain-zeroshot_split_chapters\<f>.md (same segments), and the commentary in 1-SOURCES\Commentaries\. The Pāli is the authority.
- **Audience:** AI_translation\audience_profile\plain.md. The reader has no Buddhist background, so the Hindi must be clear, natural and modern, with nothing added.

## About the text
The Paṭṭhāna applies the 24 conditions to the triads and dyads of the Dhammasaṅgaṇī matrix. It is almost entirely formulaic and abbreviates heavily with …pe…. Everything turns on:
- **which items**: the triad/dyad items in each slot (kusala/akusala/abyākata, vedanā, vipāka, …, the dyads hetu, sahetuka …), the order of the X → Y relation;
- **which condition**: the 24 conditions and their positive (anuloma) vs negative (paccanīya, na-) forms; the mixed sections;
- **counts**: "hetuyā nava, ārammaṇe tīṇi …" and the combination counts; the count markers "(1)", "(3)";
- **polarity of items**: na-, no-, nana- items in the negative method by phenomena; "X ceva Y ca" vs "X ceva no ca Y";
- **the example clauses**: which aggregates, which matter (cittasamuṭṭhāna, kaṭattā, upādā), the moments (paṭisandhi, pavatti), the pañhāvāra lists.

## Approved conventions (do NOT flag these)
- dhamma = «परिघटना»; kusala / akusala / abyākata = «हितकर / हानिकर / नैतिक रूप से अनिर्धारित»; khandha = «समूह»; paccaya = «कारण»; the 24 conditions «X-कारण» (hetu «मूल-कारण», ārammaṇa «विषय-कारण», adhipati «प्रधानता-कारण» … avigata «अविलीनता-कारण»).
- Forms: hetupaccayā «मूल-कारण से»; nahetupaccayā «मूल-कारण के बिना»; nahetupaccayo (heading) «मूल-कारण का अभाव»; hetuyā nava «मूल-कारण में नौ»; X dhammo Y dhammassa hetupaccayena paccayo «X परिघटना, Y परिघटना के लिए मूल-कारण के रूप में कारण होती है»; X dhammaṃ paṭicca Y dhammo uppajjati «X परिघटना पर निर्भर होकर Y परिघटना … उत्पन्न होती है».
- Siyā … uppajjeyya lines are questions «क्या … उत्पन्न हो सकती है?» even where the Pāli ends with "." (user-approved).
- vipāka (adjective) = «कर्म-फल रूपी»; uppanna «उत्पन्न हो चुका»; niṭṭhita «समाप्त»; triad/dyad names «X वाला तीन/दो का वर्गीकरण»; kātabba «बनाना / शामिल करना / करना चाहिए» by object (user-approved).
- Negated items «<item> न होने वाली», double «… न होने वाली न होने वाली».
- **Source slips are translated exactly as written** (user rule: no emendations; only pure spelling slips rendered as the word meant). Do NOT flag a Hindi line for following a slip; list slips briefly.
- {…} variants are rendered «[पाठभेद / वर्तनी-भेद (…): <Pāli>]» (bracket contents stay Pāli).

## Check every segment for

**1. CRITICAL: meaning errors**
- a wrong item in a slot, or the X → Y direction reversed;
- a wrong condition, or positive/negative condition swapped;
- a wrong count or count marker;
- an item's polarity wrong (na-/no- lost or added);
- a wrong aggregate, matter kind, moment or list member in the example clauses; omitted or added content (beyond "…" for …pe…); content on the wrong ID.

**2. MAJOR**
- Hindi that is ungrammatical or misleading, so that a reader would likely misread it (including agreement with feminine परिघटना and masculine समूह).
- The same Pāli formula rendered inconsistently within your part.

**3. MINOR**
- awkward wording or register; Pāli left in Latin script outside variant brackets.

**Also check typography:** "–" only where the Pāli has "–" or "—", at the same spot; statements end with «।», questions with «?»; quotes are “…”; no double blank lines.

## How to check
The text is extremely repetitive. Verify the first instance of each formula carefully by reading, then check every segment by script: per line, compare the items in each slot (build a Pāli→Hindi item table from the first instances), the condition names and their polarity, the numbers and count markers, the na-/no- items, and the number of example clauses. Read headings, the bracketed notes and the pañhāvāra example prose closely.

## Report (concise; plain text, as your final message; you cannot write files)
- A table: ID | file | line (non-empty line number) | severity | Pāli (short) | Hindi (short) | problem | suggested Hindi fix (exact old → new where possible).
- If one error repeats in many segments, give one row with the pattern and the list of IDs.
- Then the counts per severity, the number of segments checked, and a one-paragraph overall judgement.
