# Brief: independent review of the Burmese Kathāvatthu (pi-5, «အငြင်းပွားရာ အကြောင်းအရာများကို ဆွေးနွေးခြင်း»)

You are an independent reviewer and a careful Pāli–Burmese bilingual checker. You are READ-ONLY: do not create, edit or delete any file.
- Work in /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails on macOS (zsh). Use the Read tool, Grep/Glob and Bash.
- Run any check scripts inline only, as `/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 - <<'EOF' … EOF` heredocs, without writing files (never /tmp or /private/tmp).
- Do NOT open the Burmese termbase, senses or keyword files, the zero-shot Burmese, or any notes or scripts in 0-INBOX: review the translation against the Pāli on its own.
- Do NOT open any existing Burmese translation or nissaya (never `0-INBOX/temp/language-priority/`), and do no web searches.

## Inputs
- **Pāli:** `AI_translation/pali/pi-5_split_chapters/<ch>.md`
- **Burmese:** the same filenames in `AI_translation/burmese/pi-5-burmese-plain-rails_split_chapters/`
- **Alignment:** segments align by the block ID at the end of each segment (e.g. ^5-112); lines align one to one within a segment.
- **Optional reference** for hard readings: the English zero-shot `AI_translation/english/pi-5-english-plain-zeroshot_split_chapters/<same file>` if it exists. The Pāli is the authority.
- **pi-1 … pi-4 consistency:** the finished Burmese `AI_translation/burmese/pi-{1,2,3,4}-burmese-plain-rails_split_chapters/` may be read to check that a pi-5 line or term whose Pāli is identical to pi-1 … pi-4 has the same Burmese (report differences as MAJOR consistency).
- **Audience:** `AI_translation/audience_profile/plain.md`: clear, natural, modern written Burmese, nothing added.

## About the text
The Kathāvatthu is a book of debates: each kathā is a controversy between the own side (sakavādī) and an opponent (paravādī), in question–answer frames: the opponent's or the own side's thesis «P-ti?», the answer «Āmantā.» or «Na hevaṃ vattabbe.», the refutation frames (anuloma / paṭikamma / niggaha / upanayana / nigamana: «Hañci P, tena vata re vattabbe – "Q"ti … Yaṃ tattha vadesi … micchā»), sutta quotations («Nanu vuttaṃ bhagavatā – "…"ti? Āmantā. Tena hi …»), and the vagga colophons and uddānas. Everything turns on:
- polarity in every clause (na / no / a-; «vattabbe» vs «no ca vattabbe»; the thesis vs its denial), and who says what (the answer must fit the question);
- the logic of each frame: which proposition is P and which is Q, kept in the right slot in all five clause forms (statement, question, condition, quoted, negated);
- the same Pāli frame = the same Burmese frame everywhere; the same proposition = the same Burmese wording in all its repetitions within a kathā;
- lists (path factors, fetters, realms, the ten crimes, the eight doubts …) item by item, and numbers;
- terms shared with pi-1 … pi-4 = their final Burmese.

## Known conventions you should NOT report as errors
- «…pe…» / «…Pe…» become one «…». Statements end with «။», lists use «၊», no «?» (questions end «…သလော။» / «…နည်း။»). Quotes “…” / ‘…’ only where the Pāli has them. Digits as the Pāli; item letters (က) (ခ) (ဂ).
- Book title «အငြင်းပွားရာ အကြောင်းအရာများကို ဆွေးနွေးခြင်း»; Xkathā «Xအကြောင်း ဆွေးနွေးချက်»; Xkathā niṭṭhitā «“X” ပြီးဆုံးပြီ။»; Xanuyogo «Xကို စစ်ဆေးမေးမြန်းခြင်း»; vagga «ဝဂ်», vagga ordinals in the Pāli series (ပထမ … ဧကာဒသမ … တေဝီသတိမ); (Saṃkhittaṃ) «(အကျဉ်းချုပ်)».
- Frames: Āmantā «ဟုတ်ပါသည်။», Natthi (answer) «မရှိပါ။», Na hevaṃ vattabbe «ဤသို့ မဆိုသင့်ပါ။», Vattabbaṃ «ဆိုသင့်ပါသည်။» (the polite answer register of the dialogue); Ājānāhi niggahaṃ / paṭikammaṃ «ချေပချက်ကို / ပြန်လှန် ချေပချက်ကို လက်ခံလော့။»; vata re «အမှန်ပင်»; Tena hi «သို့ဖြစ်လျှင်» / «သို့ဖြစ်၍»; micchā «မှားသည်»; saccikaṭṭhaparamatthena «အမှန်တကယ် အဆုံးစွန် အနက်အားဖြင့်»; Nanu vuttaṃ bhagavatā «မြတ်စွာဘုရား ဤသို့ ဟောတော်မူသည် မဟုတ်လော –»; Attheva suttantoti «ထိုသို့သော သုတ္တန် အမှန်ပင် ရှိသလော။»; sakavādī / paravādī «မိမိဘက် / တစ်ဖက်သား»; puggalo «ပုဂ္ဂိုလ်», upalabbhati «တွေ့ရ».
- Terms: tathāgata / bhagavā «မြတ်စွာဘုရား»; buddha «ဘုရားရှင်»; dhamma «သဘောတရား» (teaching «တရား»); kusala / akusala ကုသိုလ် / အကုသိုလ်; nibbāna; samāpatti «သမာပတ်», nirodhasamāpatti «ချုပ်ငြိမ်းခြင်း သမာပတ်»; paṭivedha «ထိုးဖောက်၍ သိခြင်း» vs vipassanā «ထိုးထွင်းသိမြင်ခြင်း»; abhisamaya «ထင်ထင်ရှားရှား သိမြင်ခြင်း»; thero «မထေရ်»; eva «ပင်» (restrictive uses may be «သာ»); sekha «ကျင့်ကြံဆဲသူ» vs paṭipannaka «ကျင့်ကြံသူ»; ghāyati / sāyati «နမ်း / လျက်»; the divine eye sees «အဆင်းအရောင်»; nāma-rūpa စိတ်ပိုင်း / ရုပ်ပိုင်း; dhātu as plane «ဘုံ» vs element «ဓာတ်»; proper names stay names.
- Variant brackets «[ပါဌ်ကွဲ (…): …]»; sigla stay in Roman script. Source slips are translated as written and are known; report one only if the Burmese is wrong for the intended reading. 8 lines are known to have fewer quote marks than the Pāli (1:27, 10:157, 10:251-253, 10:342, 25:44, 26:130): do not report them.

## Check every segment for
**1. CRITICAL: meaning errors**: polarity (a negation lost or added), P / Q swapped in a frame, an answer that contradicts the question, a wrong term, a list item lost, added, swapped or merged, a wrong number, omitted or added content, content on the wrong ID.
**2. MAJOR**: Burmese that is ungrammatical or misleading so a reader would likely misread it; the same Pāli frame, proposition or stock passage rendered inconsistently within your part (or against identical pi-1 … pi-4 Pāli).
**3. MINOR**: awkward wording, a heavy word where a plain one exists, Pāli left in Roman script outside variant brackets and sigla.
**Also typography:** dashes «–»/«—» only where the Pāli has them, same count per line; no «।», no «?»; no double blank lines.

## How to check
Check BY SCRIPT, per line: numbers and counts, polarity per clause (Pāli na / no / a- vs Burmese «မ» / «မဟုတ်» / «မရှိ»; Āmantā vs Na hevaṃ), frame shapes (each Pāli frame type vs its Burmese frame), list item counts (Pāli items vs Burmese items split on «၊»), dash and quote counts, and that each recurring Pāli line always gets the same Burmese. Use the results to find lines to read closely; then read closely every kathā opening (the first full round of the dialectic), every sutta quotation, every list and every flagged line, spread over all your chapters. The files are large: read them in parts, focus close reading on distinct (non-repeated) lines.

## Report (concise, as your final message: you cannot write files)
- A table: ID | file | severity | Pāli (short) | Burmese (short) | problem | suggested Burmese fix (the full corrected phrase). Number your rows with your letter (A1, A2 … or B1, B2 …).
- One row per recurring pattern, with the IDs or the count.
- Then the counts per severity, segments checked, script results, and a one-paragraph overall judgement.
