# Brief: independent review of the Burmese Dhātukathā (pi-3, «ဓာတ်များအကြောင်း ဆွေးနွေးခြင်း»)

You are an independent reviewer and a careful Pāli–Burmese bilingual checker. You are READ-ONLY: do not create, edit or delete any file.
- Work in /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails on macOS (zsh). Use the Read tool, Grep/Glob and Bash.
- Run any check scripts inline only, as `/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 - <<'EOF' … EOF` heredocs, without writing files.
- Do NOT open the Burmese termbase, senses or keyword files, the zero-shot Burmese, or any notes or scripts in 0-INBOX: review the translation against the Pāli on its own.
- Do NOT open any existing Burmese translation or nissaya (never `0-INBOX/temp/language-priority/`), and do no web searches.

## Inputs
- **Pāli:** `AI_translation/pali/pi-3_split_chapters/<ch>.md`
- **Burmese:** the same filenames in `AI_translation/burmese/pi-3-burmese-plain-rails_split_chapters/`
- **Alignment:** segments align by the block ID at the end of each segment (e.g. ^3-112); lines align one to one within a segment.
- **Optional reference** for hard readings: the English zero-shot `AI_translation/english/pi-3-english-plain-zeroshot_split_chapters/<same file>`. The Pāli is the authority.
- **Pi-1 / pi-2 consistency:** the finished Burmese Dhammasaṅgaṇī and Vibhaṅga `AI_translation/burmese/pi-1-burmese-plain-rails_split_chapters/`, `pi-2-burmese-plain-rails_split_chapters/` may be read to check that a pi-3 line or topic name whose Pāli is identical to pi-1 / pi-2 has the same Burmese (report differences as MAJOR consistency).
- **Audience:** `AI_translation/audience_profile/plain.md`: clear, natural, modern written Burmese, nothing added.

## About the text
The Dhātukathā classifies phenomena by inclusion (saṅgaha) and association (sampayoga) with the five aggregates, twelve bases and eighteen elements. It opens with the mātikās (Nayamātikā of 14 methods, Abbhantaramātikā of the topics, Nayamukhamātikā, Lakkhaṇamātikā, Bāhiramātikā = the Dhammasaṅgaṇī Mātikā), then the 14 methods (naya), each a fixed question-and-answer frame: «Rūpakkhandho katihi khandhehi katihāyatanehi katihi dhātūhi saṅgahito? … ekena khandhena ekādasahāyatanehi ekādasahi dhātūhi saṅgahito. Katihi asaṅgahito? Catūhi khandhehi ekenāyatanena sattahi dhātūhi asaṅgahito.»; later methods ask «Yaṃ … saṅgahitā, te dhammā … asaṅgahitā?», «… sampayutto / vippayutto?», with answers «natthi», «na kehici», «kehici». Each method ends with a summary verse (uddāna). Everything turns on:
- the NUMBERS in every answer (instrumental number words «ekena, dvīhi, catūhi, ekādasahi, sattarasahi …»), checked against the Pāli count by count;
- saṅgahita / asaṅgahita and sampayutta / vippayutta polarity, «natthi», «na kehici», «kehici»;
- the topic names (aggregates, bases, elements, truths, faculties, the dependent-arising links, the Mātikā triads / dyads) = pi-1 / pi-2 final Burmese;
- the summary verses (numbers, the items they list).

## Known conventions you should NOT report as errors
- «…pe…» / «…Pe…» become one «…». Statements end with «။», lists use «၊», no «?». Quotes “…” / ‘…’. Digits as the Pāli; item letters (က) (ခ) (ဂ).
- Book title «ဓာတ်များအကြောင်း ဆွေးနွေးခြင်း»; naya «ခွဲနည်း» with Pāli ordinals «ပထမ … စုဒ္ဒသမ ခွဲနည်း»; mātikā names «ခွဲနည်း / အတွင်း / ခွဲနည်း၏ တံခါးဝ / လက္ခဏာ / ပြင်ပ ခေါင်းစဉ်စာရင်း»; khandha = အစုအဝေး, āyatana = အာရုံခံ နယ်ပယ်, dhātu = ဓာတ်.
- Frames: saṅgaha / asaṅgaha «အကျုံးဝင်ခြင်း / အကျုံးမဝင်ခြင်း»; «Sသည် အစုအဝေး မည်မျှ၊ အာရုံခံ နယ်ပယ် မည်မျှ၊ ဓာတ် မည်မျှတို့တွင် အကျုံးဝင်သနည်း။»; answers «… N-ပါးတို့တွင် အကျုံးဝင်သည်။» / «… အကျုံးမဝင်။»; sampayutta / vippayutta «ယှဉ်တွဲ / ကင်းကွာ»; kehici «…တို့၏ အချို့နှင့်»; Natthi «မရှိ။»; plural «ကြ» only where the Pāli verb is plural; maccu «သေခြင်း» (verse); pucchake «ဖော်ပြချက်» vs pucchakena «မေးခွန်း».
- dhamma = သဘောတရား; kusala / akusala = ကုသိုလ် / အကုသိုလ်; abyākata = ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော; uppanna = ဖြစ်ပေါ်ပြီးသော, samuppanna = ဖြစ်ပေါ်လာသော; ajjhatta «မိမိ၌ ရှိသော», bahiddhā «မိမိ၏ ပြင်ပ၌ ရှိသော» (other bahiddhā senses: «ပြင်ပ၌», «အပြင်ဘက်»); phassa တွေ့ထိမှု, vedanā ခံစားမှု, saññā မှတ်သိမှု, saṅkhārā ပြုပြင်ဖန်တီးမှုများ, viññāṇa သိစိတ်, cetanā စေ့ဆော်မှု, vitakka / vicāra စတင်ကြံစည်မှု / ဆက်လက်သုံးသပ်မှု; -indriya X၏ စွမ်းရည်; ākāsa ဟင်းလင်းပြင်; paṭiccasamuppāda အကြောင်းတို့ကို မှီ၍ ဖြစ်ပေါ်ပုံ; nāma-rūpa စိတ်ပိုင်း / ရုပ်ပိုင်း; dhātu as plane «ဘုံ» vs element «ဓာတ်»; proper names stay names.
- Variant brackets «[ပါဌ်ကွဲ (Syā.): …]», «[စာလုံးပေါင်းကွဲ (…): …]». Source slips are translated as written and are known; report one only if the Burmese is wrong for the intended reading.

## Check every segment for
**1. CRITICAL: meaning errors**: polarity (a negation lost or added), a wrong factor / term, a synonym list item lost, added, swapped or merged, a wrong number, omitted or added content, content on the wrong ID.
**2. MAJOR**: Burmese that is ungrammatical or misleading so a reader would likely misread it; the same Pāli formula or synonym rendered inconsistently within your part (or against identical pi-1 Pāli).
**3. MINOR**: awkward wording, a heavy word where a plain one exists, Pāli left in Roman script outside variant brackets.
**Also typography:** dashes «–»/«—» only where the Pāli has them, same count per line; no «।», no «?»; no double blank lines.

## How to check
Check BY SCRIPT, per line: every count in every answer (Pāli instrumental number words vs Burmese number + «ပါး», per kind: khandha / āyatana / dhātu), saṅgahita / asaṅgahita and sampayutta / vippayutta polarity per clause, «natthi» / «na kehici» / «kehici», the topic items in answer lists (count and order), dash counts, and that each recurring Pāli line always gets the same Burmese. Use the results to find lines to read closely; then read closely every chapter opening, every definition list and every flagged line, spread over all your chapters. The files are large: read them in parts, focus close reading on distinct (non-repeated) lines.

## Report (concise, as your final message: you cannot write files)
- A table: ID | file | severity | Pāli (short) | Burmese (short) | problem | suggested Burmese fix (the full corrected phrase). Number your rows with your letter (A1, A2 … or B1, B2 …).
- One row per recurring pattern, with the IDs or the count.
- Then the counts per severity, segments checked, script results, and a one-paragraph overall judgement.
