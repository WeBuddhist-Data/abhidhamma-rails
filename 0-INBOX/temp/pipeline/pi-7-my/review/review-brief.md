# Brief: independent review of the Burmese Paṭṭhāna (pi-7, «အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ»)

You are an independent reviewer and a careful Pāli–Burmese bilingual checker.

## Ground rules
- **Read only.** Do not create, edit or delete any file.
- **Where to work:** /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails on macOS (zsh). Use the Read tool, Grep/Glob and Bash.
- **Scripts:** run check scripts inline only, as `/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 - <<'EOF' … EOF` heredocs, without writing files. Never use /tmp or /private/tmp. Call python by that full path.
- **Files you must not open:**
  - the Burmese termbase, senses or keyword files, the zero-shot Burmese, or any notes or scripts in 0-INBOX (review the translation against the Pāli on its own);
  - any existing Burmese translation or nissaya (never `0-INBOX/temp/language-priority/`). Do no web searches.

## Inputs
- **Pāli:** `AI_translation/pali/pi-7_split_chapters/<ch>.md`.
- **Burmese:** the same filenames in `AI_translation/burmese/pi-7-burmese-plain-rails_split_chapters/`.
- **Alignment:** segments align by the block ID at the end of each segment (e.g. ^7-3-12). Within a segment, lines align one to one.
- **Optional reference for hard readings:** the English zero-shot `AI_translation/english/pi-7-english-plain-zeroshot_split_chapters/<same file>`. The Pāli is the authority.
- **Consistency with pi-1 … pi-6:** you may read the finished Burmese in `AI_translation/burmese/pi-{1,…,6}-burmese-plain-rails_split_chapters/`. Where a pi-7 line or term has Pāli identical to pi-1 … pi-6, its Burmese should be the same; report differences as MAJOR consistency.
- **Audience:** `AI_translation/audience_profile/plain.md`: clear, natural, modern written Burmese, with nothing added.

## About the text
The Paṭṭhāna has three layers:
- **The conditions:** the 24 conditions (paccaya), each with its definition («Hetupaccayoti – hetū hetusampayuttakānaṃ dhammānaṃ … hetupaccayena paccayo.»).
- **The combinations:** the conditions applied to the triads and dyads of the Mātikā, alone and combined (dukatika, tikaduka, tikatika, dukaduka).
- **The sections and orders:** seven sections (paṭicca-, sahajāta-, paccaya-, nissaya-, saṃsaṭṭha-, sampayutta-, pañhāvāra), in four orders (anuloma, paccanīya, anulomapaccanīya, paccanīyānuloma), each with its vibhaṅga and its counts («Hetuyā nava, ārammaṇe tīṇi …»).

Everything turns on:
- **Direction:** which state conditions which. Check the term order and case in «X paṭicca Y uppajjati» and «X Yassa … paccayena paccayo», and that the conditioning and conditioned are never swapped.
- **The condition named,** and its polarity: na-Xpaccayā, naXe, and the na-X terms of part 5.
- **Every number:** the counts, the khandha counts (ekaṃ / dve / tayo) and the mūlaka counts.
- **The terms:** each triad / dyad term and each combined (stacked) term.
- **Lists and stock passages:** the lists of states and the stock pañhāvāra passages (the deeds, jhāna, path, abhiññā …).
- **Consistency:** the same Pāli frame gets the same Burmese frame everywhere.

## Known conventions you should NOT report as errors
**Punctuation and layout**
- «…pe…» becomes one «…».
- Statements end with «။», lists use «၊», and there is no «?» (questions end «…လော။»).
- Quotes appear only where the Pāli has them, except the chapter-end form «“X” ပြီးဆုံးပြီ».
- Digits are as in the Pāli. Variants in braces «{ပါဌ်ကွဲ (…): …}», as the Pāli has them; sigla in Roman.

**Book title and condition frames**
- Book title «အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ».
- paccaya «အကြောင်း»; «Xpaccayena paccayo» «Nဟူသော အကြောင်းဖြင့် အကြောင်း ဖြစ်သည်».
- Xpaccayā «…ကြောင့်», naXpaccayā «…ကြောင့် မဟုတ်ဘဲ».
- Counts «Nဟူသော အကြောင်း၌ …ခု».
- paṭicca and nissāya are both «…ကို မှီ၍»; the sections are told apart by their headings.
- uppajjati «ဖြစ်ပေါ်သည်».

**Terms and stacking**
- Two qualifiers on one noun are stacked as «A၊ B N».
- The na-X rule: «…သည် မဟုတ်သော» / «X မဟုတ်သော», with double negatives applied twice.
- Gocchaka items are the bare noun.

**Section, order and other terms**
- vāra «Xအလိုက် ဖော်ပြချက်»; anuloma / paccanīya «အဟုတ်ပြ / အငြင်းပြ ပုံစံ»; the mind moment anuloma «လျော်ညီခြင်း စိတ်».
- samanantara «ကောင်းစွာ ချက်ချင်း နောက်»; vipāka «ကံ၏ အကျိုး»; avasesa «ကြွင်းကျန်သော»; nānākaraṇa «ကွဲပြားမှု».
- The label «Sahajātā –» is the bare name, but «အတူ ပေါ်ပေါက်သည့် ကံ» in kamma passages.
- asaññasattānaṃ «…တို့၏»; the heinous deeds as in pi-5 («အမိကို သတ်ခြင်း ကံ» …).

**Slips and head nouns**
- Source slips are translated as written and are known; report one only if the Burmese is wrong for the intended reading.
- Burmese adds a head noun («သဘောတရား», «စိတ်», «ရုပ်», «ပြဿနာ») where the Pāli has a bare adjective or an elliptic term. That is known; do not report it unless it changes the meaning.

## Your part
<PART>

## Check every segment for
1. **CRITICAL: meaning errors.**
   - The conditioning and conditioned swapped, or a case wrong in a way that changes who conditions whom.
   - The wrong condition.
   - Polarity: a negation lost or added.
   - A wrong number or count.
   - A wrong term: triad / dyad / combined, or a na-X form.
   - A list item lost, added, swapped or merged.
   - Omitted or added content, or content on the wrong ID.
2. **MAJOR.**
   - Burmese that is ungrammatical or misleading, so a reader would likely misread it.
   - The same Pāli frame, term or stock passage rendered inconsistently within your part, or against identical pi-1 … pi-6 Pāli.
3. **MINOR.**
   - Awkward wording, or a heavy word where a plain one exists.
   - Pāli left in Roman script outside the variant braces and sigla.

**Also typography:** dashes «–» / «—» only where the Pāli has them, with the same count per line; no «।» and no «?»; no double blank lines.

## How to check
1. **Check by script, per line.** The book is huge and extremely formulaic, so the scripts carry the load. Check:
   - numbers and counts;
   - the condition named, and its polarity per clause;
   - the term order (the conditioning term before the conditioned, or its case marker);
   - the stacked terms;
   - dash and quote counts;
   - that each recurring Pāli line always gets the same Burmese.
2. **Read closely:**
   - every line the scripts flag;
   - spread over all your chapters: every chapter opening, the first full round of each section in each order, every count block, every pañhāvāra stock passage, and the notes.
3. Read the files in parts; they are large.

## Report (concise, as your final message: you cannot write files)
- **A table:** ID | file | severity | Pāli (short) | Burmese (short) | problem | suggested Burmese fix (the full corrected phrase).
  - Number your rows with your letter (A1 … / B1 … / C1 …).
  - Give one row per recurring pattern, with the IDs or the count.
- **Then:** the counts per severity, the segments checked, the script results, and a one-paragraph overall judgement.
