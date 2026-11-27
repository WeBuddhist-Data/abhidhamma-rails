# pi-6 Burmese zero-shot SAMPLE: notes (preamble, 1-mulayamaka, 2-01-khandhayamaka)

Status: APPROVED by the coordinator 2026-11-22 (user's standing go-ahead), with one change, applied. Not committed.
Brief: burmese-zeroshot-sample-brief.md.

## Coordinator decisions 2026-11-22 (binding for the later pi-6 chapters)
- CHANGE: Natthi (answer) = «မရှိပါ။» (polite answer register, as Āmantā «ဟုတ်ပါသည်။» and No «မဟုတ်ပါ။»; pi-5 precedent,
  witness pi-5 ^5-355). pi-3 «မရှိ။» (^3-410) is now a listed exception «explained: answer register» in check_sample.py.
  Changed in my6_formulas.py (NATTHI, one place); files rebuilt, terms file regenerated, all checks pass again.
- APPROVED as proposed: book title «အတွဲလိုက် မေးဖြေခြင်း»; chapter names «Xများကို အတွဲလိုက် မေးဖြေခြင်း»; headings;
  question / answer frames; tenses («ဖြစ်ပေါ်» / «…ခဲ့» / «…လိမ့်မည်», negative «မ» + verb); hetu «အကြောင်း» in the hetuvāra
  list (each of the ten words its own Burmese; logged departure from pi-1); anuloma / paccanīka «အဟုတ်ပြ ပုံစံ / အငြင်းပြ
  ပုံစံ» (Yamaka sense, distinct from pi-5 debate order); cavati «စုတေ» (pi-5 / pi-2 ^2-1029).
Source rule kept: translated from the Pāli only; no Burmese translation or nissaya opened (0-INBOX/temp/language-priority/
not opened), no web search. pi-1 … pi-5 read only through their rails texts (FINAL) and locked termbases; English and
Marathi pi-6 rails read for meaning only (ch. 1 root predicates, hetuvāra).

## Files
- Output: `AI_translation/burmese/pi-6-burmese-plain-zeroshot_split_chapters/` preamble.md (3 segments, 3 lines),
  1-mulayamaka.md (139 segments, 305 lines: the whole Mūlayamaka ^6-1-0 … ^6-1-99), 2-01-khandhayamaka.md
  (202 segments, 788 lines: the whole file ^6-2-0 … ^6-2-115).
- `my6_formulas.py` (shared module), `make_sample.py` (generator; `--misses` lists unmatched lines, `--terms` writes
  `my6-zeroshot-terms.md`), `check_sample.py` (per-line check + reuse test).
- Read-only helpers (never used by the generator): kwic6.py / k.sh (search pi-1 … pi-5 final by Pāli regex),
  scratch/findw.py / fw.sh (find a rails segment with a Pāli regex and a Burmese string, for witnesses),
  scratch/who.py (lists the person / place groups), scratch/mutate.sh (mutation test of check_sample.py).
- Run: `python3 -I -X utf8 make_sample.py` (writes the three files), `make_sample.py --terms`, `check_sample.py`.

## Checks (final run)
- check_chapter_ids / check_text_pe / check_marks: OK for all three files (chk-pe copies deleted afterwards).
- check_sample.py: A 3/3 regenerated identical; B1 1096 lines; B2 930 negations, each one Burmese negative; B3 620
  verbs in order with root, tense, polarity and double negative, 185 answers; B4 724 labelled lines in order, every
  «vā pana» = «တစ်ဖန်»; B5 digits + 87 number words; B6 596 distinct Pāli sentences, one Burmese each; B7 144
  headings / colophons / table lines; 0 mismatches. Reuse test 2792 / 2792 identical (C1 khandha names and bare terms
  1069/1069, C2 whole lines and answers 181/181, C3 48 reused terms 1542/1542); 4 documented exceptions (below).
- Mutation test (scratch/mutate.sh): a dropped «မ» (B2, B3), a dropped «ခဲ့» (B3), three -> four (B5), a changed
  «ဟုတ်ပါသည်» (B3, B6, C2), a changed khandha name (B7, C1, C2) are all caught.

## Method (for the later agents)
- my6_formulas builds its own index of the pi-1 … pi-5 rails texts (FINAL); every reused value is read (heads(),
  items()) or checked (witness()) at import, so the module stops if a final text drifts. WITNESS lists them
  (terms §9).
- Engine (translate_line): heading table H (labels, «(1) …», «X dhammā (1) …» composed); colophons COLO; whole lines
  LINES (verse, the Pañcakkhandhā list); hetuvāra lines with «…» (hetu_line: each piece between «…» translated);
  otherwise the line is cut into sentences at «. » / «? » before a capital, brackets taken out (⟦n⟧) and put back by
  the frame; each sentence goes to the pavatti frames, then ch. 1, then the paṇṇatti frames. Nothing matched = Miss.
- Pavatti: my_verb(root, tense, neg, form) gives every verb form; q_pavatti (yassa / yattha / yassa yattha, vā pana),
  a_but («… no ca …», double negative «… မVသည်ကား မဟုတ်»), a_both, short answer; group_my() parses the person
  groups (sabbesaṃ, itaresaṃ, places in acc. / loc. / abl. / gen., the participles, pacchimabhavika + upapajjanta),
  place_my() the bare places. Later chapters: add_subject() for new subjects (āyatana, dhātu …), PLACES / PART /
  GROUP_ATOMS for new person types, and a new root in VERB / pali_verb if a new verb appears.
- Ch. 1 predicates: pred() parses every -mūla / -mūlamūla / -mūlaka / -mūlamūlaka form with eka / aññamañña and
  «X-mūlena»; Pred gives question, relative, statement, negative and «… လည်း» forms. The dhamma-type chapters (sacca,
  dhamma …) can reuse ye_keci / ye_va_pana.
- Paṇṇattivāra: term() reads every surface form; add_term() for the later chapters' terms; the frames P1 … P5, P_Q.

## Main choices
- Book title Yamakapāḷi = «အတွဲလိုက် မေးဖြေခြင်း» ("question and answer in pairs"; gerund pattern of the pi-2 / pi-5
  titles). Chapters «Xများကို အတွဲလိုက် မေးဖြေခြင်း»: Mūla «အမြစ်များကို …», Khandha «အစုအဝေးများကို …» (parallel to
  pi-2 «အစုအဝေးများကို ခွဲခြမ်းစိတ်ဖြာခြင်း»); the eight later names are PROPOSED in TOPICS. Colophons «“X” ပြီးဆုံးပြီ။».
- Headings: vāra «Xအလိုက် ဖော်ပြချက်» / «X ဖော်ပြချက်» (pi-1 / pi-2), naya «ခွဲနည်း» (pi-3), uddeso / niddeso
  «အကျဉ်း / အကျယ် ဖော်ပြချက်» (pi-1 / pi-3); paṇṇatti «သတ်မှတ်ချက်» (pi-1 paññatti); padasodhana «စကားလုံးကို
  စိစစ်ခြင်း» (NEW); -mūlacakka «…ကို အခြေခံ၍ လှည့်ပတ်ခြင်း» (NEW); suddha «ရိုးရိုး» (pi-5); pavatti «ဖြစ်ပျက်ခြင်း»
  (NEW); uppāda «ဖြစ်ပေါ်ခြင်း», nirodha «ချုပ်ငြိမ်းခြင်း» (pi-1); the three times «ပစ္စုပ္ပန် / အတိတ် / အနာဂတ်» (pi-1);
  puggala «ပုဂ္ဂိုလ်», okāsa «နေရာ» (pi-1 / pi-4).
- anuloma / paccanīka of a Yamaka question = «အဟုတ်ပြ ပုံစံ» / «အငြင်းပြ ပုံစံ» (affirmative / negated form): NEW
  sense; pi-5 «အစဉ်အတိုင်း» / «ပြောင်းပြန်» is the debate-order sense and would tell a plain reader "reversed order".
- Question frames: ye keci S dhammā, sabbe te P? = «S သဘောတရား မည်သည်တို့မဆို၊ ထိုအားလုံးတို့သည် P …ကြသလော။» (pi-5
  ^5-334 pattern «… မည်သူမဆို၊ ထိုသူ အားလုံးတို့သည် …» for persons); (Kha) ye vā pana P, sabbe te dhammā S? =
  «တစ်ဖန် P …ကြသော အရာ မည်သည်တို့မဆို၊ ထိုအားလုံးတို့သည် S သဘောတရားများ ဖြစ်ကြသလော။»; (Ka) X Y? = «Xသည် Y
  ဖြစ်(ကြ)သလော။»; (Ka) na X na Y? = «X မဟုတ်သော အရာသည် Y မဟုတ်သလော။»; yassa … tassa = «အကြင်သူအား … ၏၊ ထိုသူအား
  … သလော။» (pi-2 ^2-199 / pi-4 ^4-208 correlative), yattha … tattha «အကြင်နေရာ၌ … ၊ ထိုနေရာ၌ …», yassa yattha
  «အကြင်သူအား အကြင်နေရာ၌ …»; vā pana «တစ်ဖန်» (pi-5 «No ce pana» = «တစ်ဖန် …»). The «-ti» of the niddesa questions
  changes nothing (same Burmese as the uddesa question).
- Verbs: uppajjati «ဖြစ်ပေါ်» / nirujjhati «ချုပ်ငြိမ်း» (pi-2 / pi-5 termbases); past -ittha «…ခဲ့», future -issati
  «…လိမ့်မည်»; negative always «မ» + verb (မဖြစ်ပေါ်၊ မဖြစ်ပေါ်ခဲ့၊ မဖြစ်ပေါ်လိမ့်မည်), so one «မ» per Pāli «na / n-».
  «no ca tesaṃ Y uppajjati» = «သို့သော် ထိုသူတို့အား Y မဖြစ်ပေါ်။»; the double negative «no ca … nuppajjati» =
  «… မဖြစ်ပေါ်သည်ကား မဟုတ်။» (it is not that it does not arise). Short answers Uppajjati. = «ဖြစ်ပေါ်သည်။» etc.
- Answers: Āmantā «ဟုတ်ပါသည်။» (pi-5); Natthi «မရှိပါ။» (pi-5 ^5-355; coordinator change); No. «မဟုတ်ပါ။» PROPOSED.
- Persons / places: asaññasatta «အသညသတ်» (pi-2; place «အသညသတ် ဘုံ», beings «အသညသတ်တို့»); pañca- / catu- /
  ekavokāra «အစုအဝေး ငါး / လေး / တစ်ပါး ရှိသော ဘဝ» (pi-2 ^2-234); arūpa «ရုပ်မရှိသော ဘုံ» (core plane name);
  suddhāvāsa «သုဒ္ဓါဝါသ ဘုံ» (NEW, name kept as a name); upapajjantānaṃ «… ၌ ပြန်လည် ဖြစ်ပေါ်ဆဲသူတို့» (upapajjati
  pi-2 / pi-5 + pi-4 «-ဆဲ»), cavantānaṃ «… မှ စုတေဆဲသူတို့» (cavati pi-5), parinibbantānaṃ «… ၌ ပရိနိဗ္ဗာန် ပြုဆဲသူတို့»
  (pi-5); pacchimabhavika «နောက်ဆုံး ဘဝ ရှိသူ» (NEW), with upapajjanta «ပြန်လည် ဖြစ်ပေါ်ဆဲ နောက်ဆုံး ဘဝ ရှိသူတို့»;
  sabbesaṃ «… သူ အားလုံးတို့»; itaresaṃ «အခြားသူတို့» (NEW); beings of a place «X၌ ရှိသူတို့»; groups joined
  «Aနှင့် B», «A၊ Bနှင့် C», then «အား» (tesaṃ) and «ထိုနေရာ၌» (tattha).
- Ch. 1: kusala / akusala / abyākata / nāma = «ကုသိုလ် / အကုသိုလ် / ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော / စိတ်ပိုင်း»
  (pi-1); kusalamūla «ကုသိုလ်၏ အမြစ်» (pi-1), akusalamūla «အကုသိုလ်၏ အမြစ်» (pi-1 / pi-2), abyākatamūla «… မဟုတ်သော
  အမြစ်» (adjectival, as pi-1 abyākatahetu), nāmamūla «စိတ်ပိုင်း၏ အမြစ်»; mūlamūla «အမြစ်၏ အမြစ်», ekamūla «တူညီသော
  အမြစ် ရှိ» (the same root), aññamaññamūla «အချင်းချင်း အမြစ် ဖြစ်» (aññamañña pi-1 / pi-5), -mūlaka «…ကို အခြေခံ»
  (based on) (all NEW); ahetuka / sahetuka «အမြစ် မရှိသော / ရှိသော» (pi-1); kusalasamuṭṭhānaṃ rūpaṃ «ကုသိုလ်မှ
  ဖြစ်ပေါ်လာသော ရုပ်» (pi-1 cittasamuṭṭhāna); -sahajāta «…နှင့်အတူ ပေါ်ပေါက်သော» (pi-5); ekato «တစ်ပြိုင်နက်» (pi-1);
  avasesa «ကြွင်းကျန်သော», ṭhapetvā «ချန်ထား၍» (pi-2 ^2-796); Tīṇeva / Naveva X = «X သုံးပါးသာ / ကိုးပါးသာ ရှိသည်».
- Ch. 2: the khandha names and «အစုအဝေး ငါးပါး – …» line exactly pi-2 ^2-1; bare rūpaṃ / vedanā / saññā / saṅkhārā /
  viññāṇaṃ = «ရုပ် / ခံစားမှု / မှတ်သိမှု / ပြုပြင်ဖန်တီးမှုများ / သိစိတ်» (pi-1 ^1-1044); khandhā «အစုအဝေးတို့» (pi-5);
  piyarūpaṃ sātarūpaṃ = pi-2 ^2-203 «ချစ်ဖွယ် သဘော ရှိသော၊ နှစ်သက်ဖွယ်ကောင်းသော သဘော ရှိသော အရာ»; diṭṭhisaññā «အယူ
  ဖြစ်သော မှတ်သိမှု» (NEW); X rūpañceva Y ca = «Xသည် ရုပ်လည်း ဖြစ်၊ Yလည်း ဖြစ်သည်။» (pi-1 «…လည်း ဖြစ်၊ …လည်း» pattern);
  na ceva X na ca Y = «Xလည်း မဟုတ်၊ Yလည်း မဟုတ်။» (pi-1 neither-nor pattern); avasesā (bare) «ကြွင်းကျန်သော အရာများ».
- Variants as pi-1 / pi-2: «[ပါဌ်ကွဲ (Syā.): …]», «[ပါဌ်ကွဲ (Sī., Syā.): …]», evamuparipi «နောက်တွင်လည်း ဤနည်းတူ»
  (pi-2 ^2-718; pi-2 ^2-568 has «အောက်တွင်လည်း ဤနည်းအတိုင်း»: the final books are not uniform, the majority taken).
  A bracket inside a person group goes after «…အား» (^6-2-87).

## Departures from pi-1 … pi-5 (for the reviewer; listed by check_sample.py as exceptions, not counted)
1. hetu in the hetuvāra (^6-1-49, ^6-1-98, ^6-1-99): «အကြောင်း» (cause; pi-4 / pi-5 termbase sense), so kusalahetū =
   «ကုသိုလ်၏ အကြောင်း». pi-1 renders kusalahetu «ကုသိုလ် အမြစ်» (^1-1059) and mūla «အမြစ်» too; but the Yamaka sets
   mūla, hetu, nidāna … paccaya, samudaya side by side as ten separate words (the verse «Mūlaṃ hetu nidānañca …»),
   and the style rule «each synonym its own Burmese» wins in this list. The other nine: nidāna «ဇာစ်မြစ်», sambhava
   «ဖြစ်တည်ရာ», pabhava «ပေါ်ထွက်ရာ», samuṭṭhāna «ဖြစ်ပေါ်လာရာ» (all NEW), āhāra «အာဟာရ», ārammaṇa «အာရုံ», paccaya
   «အထောက်အပံ့», samudaya «ဖြစ်ပေါ်ခြင်း» (pi-1 / pi-2). ahetuka / sahetuka keep pi-1 «အမြစ် …» (hetu = root there).
   Alternative if the reviewer prefers pi-1 identity: hetu «အမြစ်» everywhere, then mūla needs another word.
2. anuloma / paccanīka (headings): «အဟုတ်ပြ ပုံစံ» / «အငြင်းပြ ပုံစံ» instead of pi-5 «အစဉ်အတိုင်း» / «ပြောင်းပြန်» (see
   above: another sense).
4. Natthi «မရှိပါ။» vs pi-3 «မရှိ။» (explained: answer register; coordinator 2026-11-22).
3. cavati: the termbases disagree (pi-2 «သေသည်», pi-5 «စုတေသည်»); «စုတေ» taken (pi-5, also pi-2 ^2-1029 «စုတေကြ»).

## Unsure Pāli / meaning
- ekamūla «တူညီသော အမြစ် ရှိ» (having the same root as …) and aññamaññamūla «အချင်းချင်း အမြစ် ဖြစ်» follow the English /
  Marathi rails meaning; mūlamūla «အမြစ်၏ အမြစ်» is literal (the commentary's sense not checked: no commentary read).
- «Mūlāni yāni ekato uppajjanti kusalamūlāni …» = «တစ်ပြိုင်နက် ဖြစ်ပေါ်ကြသော အမြစ်များ ဖြစ်သည့် ကုသိုလ်၏ အမြစ်များသည် …»
  (apposition kept; slightly heavy).
- piyarūpaṃ sātarūpaṃ: the pi-2 rendering has no «ရုပ်», so the Pāli wordplay (rūpa in «piyarūpa» is called rūpa but is
  not the rūpakkhandha) is not visible to a Burmese reader; kept for identity with pi-2. Same for diṭṭhisaññā (saññā
  is visible: «အယူ ဖြစ်သော မှတ်သိမှု»).
- «Saṅkhārakkhandhaṃ ṭhapetvā avasesā saṅkhārā, na saṅkhārakkhandho» read as «the remaining (things) are saṅkhārā»
  («ကြွင်းကျန်သော အရာများသည် ပြုပြင်ဖန်တီးမှုများ ဖြစ်ကြသည်»), as the Syā. variant spells out.
- Natthi «မရှိပါ။» after a person question means "there is no such person".
- itaresaṃ before two groups (^6-2-80 «Itaresaṃ pañcavokāraṃ upapajjantānaṃ asaññasattaṃ upapajjantānaṃ»): itara is
  applied to the first group only («… ပြန်လည် ဖြစ်ပေါ်ဆဲ အခြားသူတို့နှင့် အသညသတ် ဘုံ၌ ပြန်လည် ဖြစ်ပေါ်ဆဲသူတို့အား»).

## Source slips (translated as written)
- ^6-2-36 «(Ka) na saṅkhārā na saṅkhārakkhandhoti. Āmantā.»: «.» for «?»; rendered as the question.
- ^6-2-61 the second line is labelled «(Ka)» for «(Kha)»: kept «(က)».
- ^6-2-111 «nirujjhattha» for «nirujjhittha»: read as past («ချုပ်ငြိမ်းခဲ့»).
- ^6-1-99 «nāmahetū ti…» (space before «ti»): read as «nāmahetūti…».
- ^6-2-44 «(Ka) viññāṇaṃ khandhoti?» / «Āmantā.» split over two lines (kept: two Burmese lines).
