# Brief: independent review of the Burmese Puggalapaññatti (pi-4, «ပုဂ္ဂိုလ်များကို သတ်မှတ်ဖော်ပြခြင်း»)

You are an independent reviewer and a careful Pāli–Burmese bilingual checker. You are READ-ONLY: do not create, edit or delete any file.
- Work in /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails on macOS (zsh). Use the Read tool, Grep/Glob and Bash.
- Run any check scripts inline only, as `/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 - <<'EOF' … EOF` heredocs, without writing files.
- Do NOT open the Burmese termbase, senses or keyword files, the zero-shot Burmese, or any notes or scripts in 0-INBOX: review the translation against the Pāli on its own.
- Do NOT open any existing Burmese translation or nissaya (never `0-INBOX/temp/language-priority/`), and do no web searches.

## Inputs
- **Pāli:** `AI_translation/pali/pi-4_split_chapters/<ch>.md`
- **Burmese:** the same filenames in `AI_translation/burmese/pi-4-burmese-plain-rails_split_chapters/`
- **Alignment:** segments align by the block ID at the end of each segment (e.g. ^4-112); lines align one to one within a segment.
- **Optional reference** for hard readings: the English zero-shot `AI_translation/english/pi-4-english-plain-zeroshot_split_chapters/<same file>`. The Pāli is the authority.
- **Pi-1 / pi-2 / pi-3 consistency:** the finished Burmese `AI_translation/burmese/pi-{1,2,3}-burmese-plain-rails_split_chapters/` may be read to check that a pi-4 line or term whose Pāli is identical to pi-1 / pi-2 / pi-3 has the same Burmese (report differences as MAJOR consistency).
- **Audience:** `AI_translation/audience_profile/plain.md`: clear, natural, modern written Burmese, nothing added.

## About the text
The Puggalapaññatti opens with a mātikā (the six designations, then the person types by ones … tens), then defines each type: «Katamo ca puggalo X? Idhekacco puggalo … – ayaṃ vuccati puggalo "X".», with paired types (X / a-X, sappurisa / asappurisa …), group questions («Tattha katame tayo puggalā?»), «Kathañca puggalo X hoti? … Evaṃ puggalo X hoti.», and similes (ponds, mangoes, mice, bulls, elephants, warriors, ascetic practices, the ten courses of action). Everything turns on:
- polarity (each na / no / a-, paired definitions that differ only by a negation), numbers and counts of persons;
- each person type keeps ONE Burmese name in mātikā, heading, question and closing quote;
- the simile pairs (which half is which) and the lists (vices, virtues, practices) item by item;
- terms shared with pi-1 / pi-2 / pi-3 (jhāna, vimokkha, āsava, sīla, path and fruit, fetters, realms) = their final Burmese.

## Known conventions you should NOT report as errors
- «…pe…» / «…Pe…» become one «…». Statements end with «။», lists use «၊», no «?». Quotes “…” / ‘…’. Digits as the Pāli; item letters (က) (ခ) (ဂ).
- Book title «ပုဂ္ဂိုလ်များကို သတ်မှတ်ဖော်ပြခြင်း»; headings «N-မျိုးတွဲ ပုဂ္ဂိုလ် သတ်မှတ်ချက်», «N-မျိုးတွဲ အကျဉ်း ဖော်ပြချက်»; paññatti «သတ်မှတ်ချက်»; persons counted with «ယောက်».
- Frames: «X ဟူသည် အဘယ် ပုဂ္ဂိုလ်နည်း။ ဤလောက၌ အချို့သော ပုဂ္ဂိုလ်သည် … – ဤပုဂ္ဂိုလ်ကို “X”ဟု ခေါ်သည်။» (quotes only where the Pāli has them); «ပုဂ္ဂိုလ်သည် အဘယ်သို့ X ဖြစ်သနည်း။ … ဤသို့ ပုဂ္ဂိုလ်သည် X ဖြစ်၏။»; simile «ဥပမာအားဖြင့် ထိုXသည် Pသကဲ့သို့၊ ဤပုဂ္ဂိုလ်သည် ထိုXနှင့် တူ၏။»; santo saṃvijjamānā «ရှိကြ၏၊ ထင်ရှား ရှိကြ၏»; So «ထိုသူသည်»; tathāgata / bhagavā «မြတ်စွာဘုရား», only the ^4-177 epithet bhagavā «ဘုန်းတော်ရှင်»; the arahant sentence is pi-2 ^2-831 without the honorific «တော်မူ».
- dhamma = သဘောတရား; kusala / akusala = ကုသိုလ် / အကုသိုလ်; abyākata = ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော; uppanna = ဖြစ်ပေါ်ပြီးသော, samuppanna = ဖြစ်ပေါ်လာသော; ajjhatta «မိမိ၌ ရှိသော», bahiddhā «မိမိ၏ ပြင်ပ၌ ရှိသော» (other bahiddhā senses: «ပြင်ပ၌», «အပြင်ဘက်»); phassa တွေ့ထိမှု, vedanā ခံစားမှု, saññā မှတ်သိမှု, saṅkhārā ပြုပြင်ဖန်တီးမှုများ, viññāṇa သိစိတ်, cetanā စေ့ဆော်မှု, vitakka / vicāra စတင်ကြံစည်မှု / ဆက်လက်သုံးသပ်မှု; -indriya X၏ စွမ်းရည်; ākāsa ဟင်းလင်းပြင်; paṭiccasamuppāda အကြောင်းတို့ကို မှီ၍ ဖြစ်ပေါ်ပုံ; nāma-rūpa စိတ်ပိုင်း / ရုပ်ပိုင်း; dhātu as plane «ဘုံ» vs element «ဓာတ်»; proper names stay names.
- Variant brackets «[ပါဌ်ကွဲ (Syā.): …]», «[စာလုံးပေါင်းကွဲ (…): …]». Source slips are translated as written and are known; report one only if the Burmese is wrong for the intended reading.

## Check every segment for
**1. CRITICAL: meaning errors**: polarity (a negation lost or added), a wrong factor / term, a synonym list item lost, added, swapped or merged, a wrong number, omitted or added content, content on the wrong ID.
**2. MAJOR**: Burmese that is ungrammatical or misleading so a reader would likely misread it; the same Pāli formula or synonym rendered inconsistently within your part (or against identical pi-1 Pāli).
**3. MINOR**: awkward wording, a heavy word where a plain one exists, Pāli left in Roman script outside variant brackets.
**Also typography:** dashes «–»/«—» only where the Pāli has them, same count per line; no «।», no «?»; no double blank lines.

## How to check
Check BY SCRIPT, per line: numbers and counts, polarity per clause (Pāli na / no / a- vs Burmese «မ» / «မဟုတ်» / «မရှိ»), paired definitions (the Burmese of X and a-X must differ exactly where the Pāli differs), each person-type name the same in mātikā / heading / question / closing, list item counts (Pāli items vs Burmese items split on «၊»), dash counts, and that each recurring Pāli line always gets the same Burmese. Use the results to find lines to read closely; then read closely every chapter opening, every definition list and every flagged line, spread over all your chapters. The files are large: read them in parts, focus close reading on distinct (non-repeated) lines.

## Report (concise, as your final message: you cannot write files)
- A table: ID | file | severity | Pāli (short) | Burmese (short) | problem | suggested Burmese fix (the full corrected phrase). Number your rows with your letter (A1, A2 … or B1, B2 …).
- One row per recurring pattern, with the IDs or the count.
- Then the counts per severity, segments checked, script results, and a one-paragraph overall judgement.
