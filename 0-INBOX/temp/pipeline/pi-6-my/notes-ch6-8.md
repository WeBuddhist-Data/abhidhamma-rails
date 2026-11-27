# pi-6 Burmese zero-shot, group ch6-8: notes (6-01 / 6-02 Saṅkhārayamaka, 8 Cittayamaka)

Status: all three chapters generated and checked 2026-11-22. Not committed. Brief: burmese-zeroshot-brief.md.
Source rule kept: translated from the Pāli only; no Burmese translation or nissaya opened (0-INBOX/temp/language-priority/
not opened), no web search. pi-1 … pi-5 read only through their rails texts (FINAL) and locked termbases (via kwic6.py,
read-only); English / Marathi pi-6 rails and pi-6-mr notes-ch6-8.md read for meaning and frame inventory only.

## Files
- Output: `AI_translation/burmese/pi-6-burmese-plain-zeroshot_split_chapters/` 6-01-sankharayamaka.md (159 segments,
  473 lines), 6-02-sankharayamaka.md (130 segments, 345 lines), 8-cittayamaka.md (209 segments, 656 lines).
- `make_ch6-8.py` (generator; imports my6_formulas.py unchanged, extends its tables in memory; `--misses`),
  `check_ch6-8.py` (per-line check + reuse test; `--mutate` runs the mutation test).
- Run: `python3 -I -X utf8 make_ch6-8.py`, `python3 -I -X utf8 check_ch6-8.py --mutate`.

## Checks (final run)
- check_chapter_ids / check_text_pe / check_marks: OK for all three files (chk-pe copies deleted afterwards).
- check_ch6-8.py: A 3/3 regenerated identical; B1 1474 lines; B2 1909 negations, each one Burmese negative; B3 2807
  verbs and participles in order (root, tense / participle kind, polarity, double negative), 187 answers; B4 880
  labelled lines, every «vā pana» = «တစ်ဖန်»; B5 digits + 218 number words; B6 1264 distinct Pāli sentences, one
  Burmese each; B7 249 headings / colophons / table lines; 0 mismatches. Reuse test 5875 / 5875 identical (C2 whole
  lines and answers 161/161, C3 82 reused terms 5714/5714); 7 documented exceptions (below).
- Mutation test (--mutate): a dropped «မ» (B2), a dropped «ခဲ့» (B3), «ပြီး» -> «ဆဲ» (B3), a dropped «ကား မဟုတ်» (B2),
  a changed term (B7), a dropped «တစ်ဖန်» (B4), «ဟုတ်ပါသည်» -> «မဟုတ်ပါ» (B2), future -> present (B3): all caught.

## Method
- Module frames first (Q_PAV, A_BUT, A_BOTH, paṇṇatti P1 … P5, P_Q), then this group's frames (F.FRAMES extended):
  `sankhara_sentence` («X na Y, X.», pariññāvāra, the slip ^6-6-121) and `citta_sentence` (citta questions with
  yaṃ / taṃ, two-verb predicates, participles, (11) «no ca», (14) atikkantakāla, answers for persons, phenomena and
  the bare (12) / (13) lines). «…pe…» lines: `pe_line` (each piece between «…» translated; «…?» = «…။», as the sample).
- Person groups: the module's `group_my` / `place_my` are tried first (so every sample group comes out as in the
  sample); otherwise `items_of` / `units_of`: moments («X၏ ဖြစ်ခြင်း / ပြိုပျက်ခြင်း ခဏ၌»), persons, places before.
  RULE: a moment goes with the person group right before it («ADV P»); alone «ADV ရှိသူတို့»; sabbesaṃ «ADV ရှိသူ
  အားလုံးတို့»; itaresaṃ «ADV ရှိသော အခြားသူတို့»; tesaṃyeva «ADV ထိုသူတို့ပင်»; a locative place before a person or
  moment is put in front of it; a place alone before «tesaṃ» = «X၌ ရှိသူတို့»; units joined as the module («A၊ Bနှင့် C»).

## New recurring terms and frames («Pāli = Burmese»; witness = FINAL rails segment checked at import)
- kāyasaṅkhāro = ကိုယ်၏ ပြုပြင်ဖန်တီးမှု (pi-5 ^5-458; see exception 1)
- vacīsaṅkhāro = နှုတ်၏ ပြုပြင်ဖန်တီးမှု (pi-5 ^5-458, ^5-332)
- cittasaṅkhāro = စိတ်၏ ပြုပြင်ဖန်တီးမှု (pi-5 ^5-458)
- saṅkhāro (bare) = ပြုပြင်ဖန်တီးမှု; saṅkhārā = ပြုပြင်ဖန်တီးမှုများ (module)
- kāyo = ကိုယ် (pi-2 ^2-226); vacī = နှုတ် (pi-5 ^5-332); cittaṃ = စိတ် (pi-1 ^1-6)
- Tayo saṅkhārā = ပြုပြင်ဖန်တီးမှု သုံးပါး
- assāsapassāsā = ဝင်လေ ထွက်လေ (pi-5 ^5-333); gen. = ဝင်လေ ထွက်လေတို့၏
- vitakkavicārā = စတင်ကြံစည်မှုနှင့် ဆက်လက်သုံးသပ်မှု (pi-5 ^5-332); vitakkavicārānaṃ = …ဆက်လက်သုံးသပ်မှုတို့၏ (pi-1 ^1-161)
- saññā ca vedanā ca = မှတ်သိမှုနှင့် ခံစားမှု (pi-5 ^5-333)
- sabbepi cittasampayuttakā dhammā = စိတ်နှင့် ယှဉ်တွဲသော သဘောတရား အားလုံးသည် (pi-1 ^1-M2-58, ^1-1308 pattern)
- savitakkasavicāra = စတင်ကြံစည်မှုနှင့် ဆက်လက်သုံးသပ်မှု ရှိသော (pi-1 ^1-M1-6)
- avitakkaavicāra = စတင်ကြံစည်မှုလည်း မရှိ၊ ဆက်လက်သုံးသပ်မှုလည်း မရှိသော (pi-1 ^1-1401)
- -bhūmiyaṃ = «… ရှိရာ အဆင့်၌» (pi-1 ^1-988 sukhabhūmiyaṃ): savitakkasavicārabhūmiyaṃ = စတင်ကြံစည်မှုနှင့်
  ဆက်လက်သုံးသပ်မှု ရှိရာ အဆင့်၌; avitakkaavicārabhūmiyaṃ = စတင်ကြံစည်မှုလည်း မရှိ၊ ဆက်လက်သုံးသပ်မှုလည်း မရှိရာ အဆင့်၌
- uppādakkhaṇe = ဖြစ်ခြင်း ခဏ၌; bhaṅgakkhaṇe = ပြိုပျက်ခြင်း ခဏ၌ (pi-5 ^5-366; see exception 2)
- uppādakkhaṇaṃ / bhaṅgakkhaṇaṃ (acc.) = ဖြစ်ခြင်း ခဏကို / ပြိုပျက်ခြင်း ခဏကို
- vinā X-ehi = X မပါဘဲ (pi-5 ^5-227)
- -samaṅgīnaṃ = «…နှင့် ပြည့်စုံသူတို့» (pi-2 ^2-809); itaresaṃ cittasamaṅgīnaṃ = စိတ်နှင့် ပြည့်စုံသော အခြားသူတို့
- pacchimacitta = နောက်ဆုံး စိတ် (NEW; pacchima as the sample «နောက်ဆုံး ဘဝ»); pacchimakusalacitta = နောက်ဆုံး ကုသိုလ်စိတ်;
  sarāgapacchimacitta = ရာဂ ရှိသော နောက်ဆုံး စိတ်; savitakkasavicāra- / avitakkaavicārapacchimacitta = … ရှိသော / မရှိသော နောက်ဆုံး စိတ်
- yassa cittassa anantarā X pacchimacittaṃ uppajjissati = မိမိ စိတ်၏ ချက်ချင်း နောက်၌ X နောက်ဆုံး စိတ် ဖြစ်ပေါ်မည့်သူတို့
  (anantarā «၏ ချက်ချင်း နောက်၌» pi-5 ^5-687; «မိမိ» NEW); X = avitakkaavicāraṃ «… မရှိသော», kāmāvacarānaṃ «ကာမဘုံနှင့်
  ဆိုင်သော» (pi-1 ^1-1 adjective)
- dutiye citte vattamāne = ဒုတိယ စိတ် ဖြစ်နေစဉ် (pi-5 ^5-556 citte vattamāne «စိတ် ဖြစ်နေစဉ်»; pi-1 ^1-146 dutiya)
- nirodhasamāpannānaṃ = ချုပ်ငြိမ်းခြင်း သမာပတ်ကို ဝင်စားနေသူတို့ (pi-5 ^5-458)
- X-jhānaṃ samāpannānaṃ = «X ဈာန်ကို ဝင်စားနေသူတို့» (pi-5 ^5-333); paṭhama / dutiya / tatiya / catutthajjhāna = ပထမ /
  ဒုတိယ / တတိယ / စတုတ္ထ ဈာန် (pi-5 ^5-332, ^5-333); loc. (okāsa) «… ဈာန်၌»; lists «Aနှင့် Bနှင့် C» (module join)
- kāmāvacara / rūpāvacara / arūpāvacara (plane) = ကာမဘုံ / သိမ်မွေ့သော ရုပ်ဘုံ / ရုပ်မရှိသော ဘုံ (pi-1 ^1-990; style-sheet
  plane names); gen. pl. «…၌ ရှိသူတို့» (sample pattern); see exception 3
- ye ca X Y upapajjitvā parinibbāyissanti tesaṃ cavantānaṃ = X နှင့် Y၌ ပြန်လည် ဖြစ်ပေါ်ပြီး ပရိနိဗ္ဗာန် ပြုမည့်သူတို့ထဲမှ
  စုတေဆဲသူတို့ (sample GROUP_ATOMS pattern; «ထဲမှ» NEW)
- tesaṃyeva = ထိုသူတို့ပင် (eva «ပင်» pi-5 ^5-241)
- uppannaṃ = ဖြစ်ပေါ်ပြီး (pi-1 ^1-1 «ဖြစ်ပေါ်ပြီးသော»); niruddhaṃ = ချုပ်ငြိမ်းပြီး (pi-5 ^5-333 «ချုပ်ငြိမ်းပြီး ဖြစ်သည်»);
  uppajjamānaṃ / nirujjhamānaṃ = ဖြစ်ပေါ်ဆဲ / ချုပ်ငြိမ်းဆဲ (-māna «ဆဲ» pi-5 ^5-366, pi-4)
- participle predicate: clause «P ဖြစ်၏» / «P မဟုတ်»; question «P ဖြစ်သလော» / «P မဟုတ်သလော»; statement «P ဖြစ်သည်» /
  «P မဟုတ်»; after «no ca»: «P မဟုတ်» / double negative «P မဟုတ်သည်ကား မဟုတ်»; attributive (12) / (13) «ဖြစ်ပေါ်ပြီးသော
  အရာ», «ဖြစ်ပေါ်ဆဲ အရာ», negative «… မဟုတ်သော အရာ»
- V1 na V2 / na V1 V2 (two finite verbs) = «V1သော်လည်း မV2» / «မV1သော်လည်း V2»; future «Vလိမ့်မည် ဖြစ်သော်လည်း …»
  (e.g. uppajjati na nirujjhati = ဖြစ်ပေါ်သော်လည်း မချုပ်ငြိမ်း; nirujjhissati na uppajjissati = ချုပ်ငြိမ်းလိမ့်မည်
  ဖြစ်သော်လည်း မဖြစ်ပေါ်လိမ့်မည်)
- A ceva B ca (verbs / participles, one subject) = «Aသည်လည်း ဖြစ်၊ Bသည်လည်း ဖြစ်သည်» (finite: «ဖြစ်ပေါ်ခဲ့သည်လည်း ဖြစ်»;
  participle: «ဖြစ်ပေါ်ပြီးလည်း ဖြစ်»); na ceva A na ca B = «မAသည်လည်း ဖြစ်၊ …» / participle «Pလည်း မဟုတ်» (each
  element its own form; one Burmese negative per Pāli na)
- yaṃ cittaṃ … taṃ cittaṃ = အကြင်စိတ်သည် … ထိုစိတ်သည် … (no dative: subject with «သည်»); yassa yaṃ cittaṃ … tassa taṃ
  cittaṃ = အကြင်သူအား အကြင်စိတ် … ထိုသူအား ထိုစိတ် …; vā pana «တစ်ဖန်» (module)
- (11) yassa cittaṃ V no ca tassa cittaṃ uppannaṃ, tassa cittaṃ V2? = အကြင်သူအား စိတ် V၏၊ သို့သော် ထိုသူအား စိတ်
  ဖြစ်ပေါ်ပြီး မဟုတ်၊ ထိုသူအား စိတ် V2လော။
- (14) uppajjamānaṃ / nirujjhamānaṃ khaṇaṃ khaṇaṃ vītikkantaṃ atikkantakālaṃ = ဖြစ်ပေါ်ဆဲ / ချုပ်ငြိမ်းဆဲ ခဏ ခဏကို
  လွန်မြောက်ပြီး ကာလ ကျော်လွန်ပြီး (vītikkanta «လွန်မြောက်ပြီး», atikkanta «ကျော်လွန်ပြီး» pi-2 ^2-609); first «… ဖြစ်၍» /
  «… မဟုတ်ဘဲ», second «… ဖြစ်၏» / «… မဟုတ်»; «tassa cittaṃ?» = «ထိုသူအား စိတ် ထိုသို့ ဖြစ်သလော။» (NEW)
- (14) answers: vītikkantaṃ = လွန်မြောက်ပြီး ဖြစ်; avītikkantaṃ = မလွန်မြောက် (privative «မ» + verb)
- dhamma subjects: Bhaṅgakkhaṇe / Uppādakkhaṇe cittaṃ = ပြိုပျက်ခြင်း / ဖြစ်ခြင်း ခဏ၌ ရှိသော စိတ်; Atītaṃ / Anāgataṃ /
  Paccuppannaṃ cittaṃ = အတိတ် / အနာဂတ် / ပစ္စုပ္ပန် စိတ်; Atītānāgataṃ cittaṃ = အတိတ် စိတ်နှင့် အနာဂတ် စိတ်;
  Bhaṅgakkhaṇe anāgatañca cittaṃ = ပြိုပျက်ခြင်း ခဏ၌ ရှိသော စိတ်နှင့် အနာဂတ် စိတ် (same for atītañca, Uppādakkhaṇe …);
  bare (12) / (13) Bhaṅgakkhaṇe / Uppādakkhaṇe = ပြိုပျက်ခြင်း / ဖြစ်ခြင်း ခဏ၌
- citta qualifiers (pi-2 ^2-365): sarāgaṃ ရာဂ ရှိသော, vītarāgaṃ ရာဂ ကင်းသော, sadosaṃ / vītadosaṃ ဒေါသ ရှိသော / ကင်းသော,
  samohaṃ / vītamohaṃ မောဟ ရှိသော / ကင်းသော, saṃkhittaṃ တွန့်ဆုတ်နေသော, vikkhittaṃ ပျံ့လွင့်နေသော, mahaggataṃ /
  amahaggataṃ ကြီးမြတ်သော / မကြီးမြတ်သော, sauttaraṃ / anuttaraṃ ထိုထက် သာလွန်သည် ရှိသေးသော / မရှိသော, samāhitaṃ /
  asamāhitaṃ တည်ကြည်သော / မတည်ကြည်သော, vimuttaṃ / avimuttaṃ လွတ်မြောက်သော / မလွတ်မြောက်သော (+ «စိတ်»)
- kusalaṃ / akusalaṃ cittaṃ = ကုသိုလ်စိတ် / အကုသိုလ်စိတ် (pi-1 ^1-1, ^1-365); abyākataṃ cittaṃ = ကုသိုလ်လည်း မဟုတ်၊
  အကုသိုလ်လည်း မဟုတ်သော စိတ် (pi-5 ^5-556); sukhāya vedanāya sampayuttaṃ cittaṃ = သာယာသော ခံစားမှုနှင့် ယှဉ်တွဲသော စိတ်
  (pi-1 ^1-988); saraṇa / araṇa = ပဋိပက္ခ ရှိသော / မရှိသော (pi-1 ^1-M2-100)
- yo X-aṃ parijānāti so Y-aṃ parijānātīti? = အကြင်သူသည် Xကို ပိုင်းခြား သိ၏၊ ထိုသူသည် Yကို ပိုင်းခြား သိသလော။
  (parijānāti pi-5 ^5-390; yo … so «အကြင်သူသည် … ထိုသူသည်» NEW); pariññā = ပိုင်းခြား သိခြင်း (pi-4 ^4-130)
- X na Y, X. (any term as subject; sample P4 only for special subjects) = Xသည် Y မဟုတ်၊ X ဖြစ်သည်။
- suttanta = သုတ္တန် (pi-5 ^5-74); -sāmañña = အထွေထွေ (NEW)
- editorial notes (NEW): yassaka «“အကြင်သူ” မေးခွန်း», yatthaka «“အကြင်နေရာ” မေးခွန်း», yassayatthaka «“အကြင်သူ
  အကြင်နေရာ” မေးခွန်း», sadisaṃ «တူသည်», vitthāretabbaṃ «အကျယ် ဖော်ပြရမည်», vibhajitabbaṃ «ခွဲခြား ဖော်ပြရမည်», natthi
  nānākaraṇaṃ «ကွဲပြားချက် မရှိ», na labbhati «မရ», na kātabbaṃ «မထည့်ရ», asammohantena «မရောထွေးစေဘဲ», ekasadisaṃ
  «တစ်မျိုးတည်း တူသည်», yāva saraṇaaraṇā «“ပဋိပက္ခ ရှိသော” “ပဋိပက္ခ မရှိသော” အတွဲ တိုင်အောင်», uddharitabbā «ထုတ်ဖော်ရမည်»

## Headings and colophons (NEW, built from the module parts)
- Suddhasaṅkhāravāro = ရိုးရိုး ပြုပြင်ဖန်တီးမှု ဖော်ပြချက်
- Nirodhavāro / Uppādavāro = ချုပ်ငြိမ်းခြင်းအလိုက် / ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်; Uppādanirodhavāro = ဖြစ်ပေါ်ခြင်းနှင့်
  ချုပ်ငြိမ်းခြင်းအလိုက် ဖော်ပြချက်; Pavatti 3. uppādanirodhavāro = ဖြစ်ပျက်ခြင်း 3. ဖြစ်ပေါ်ခြင်းနှင့် ချုပ်ငြိမ်းခြင်းအလိုက် ဖော်ပြချက်
- Pariññāvāro = ပိုင်းခြား သိခြင်းအလိုက် ဖော်ပြချက်; 1-6. Paccuppannavārādi = 1-6. ပစ္စုပ္ပန်အလိုက် ဖော်ပြချက် စသည်
- Suddhacittasāmaññaṃ (and -sāmañña) = ရိုးရိုး စိတ် အထွေထွေ; Puggalavāro = ပုဂ္ဂိုလ်အလိုက် ဖော်ပြချက်; Dhammavāro =
  သဘောတရားအလိုက် ဖော်ပြချက်; Puggaladhammavāro = ပုဂ္ဂိုလ်နှင့် သဘောတရားအလိုက် ဖော်ပြချက်
- Uppādanirodhakālasambhedavāro = ဖြစ်ပေါ်ခြင်းနှင့် ချုပ်ငြိမ်းခြင်း၏ ကာလ ရောနှောခြင်း ဖော်ပြချက်
- Uppāduppannavāro = ဖြစ်ပေါ်ခြင်းနှင့် ဖြစ်ပေါ်ပြီးသော အရာ ဖော်ပြချက်; Nirodhuppannavāro = ချုပ်ငြိမ်းခြင်းနှင့် ဖြစ်ပေါ်ပြီးသော အရာ ဖော်ပြချက်
- Uppajjamāna-nanirodhavāro (and Uppajjamānananirodhavāro) = ဖြစ်ပေါ်ဆဲ အရာနှင့် မချုပ်ငြိမ်းခြင်း ဖော်ပြချက်
- Uppajjamānuppannavāro = ဖြစ်ပေါ်ဆဲ အရာနှင့် ဖြစ်ပေါ်ပြီးသော အရာ ဖော်ပြချက်; Nirujjhamānuppannavāro = ချုပ်ငြိမ်းဆဲ အရာနှင့်
  ဖြစ်ပေါ်ပြီးသော အရာ ဖော်ပြချက်; Uppannuppādavāro = ဖြစ်ပေါ်ပြီးသော အရာနှင့် ဖြစ်ပေါ်ခြင်း ဖော်ပြချက်; Uppannuppajjamānavāro =
  ဖြစ်ပေါ်ပြီးသော အရာနှင့် ဖြစ်ပေါ်ဆဲ အရာ ဖော်ပြချက်; Niruddhanirujjhamānavāro = ချုပ်ငြိမ်းပြီးသော အရာနှင့် ချုပ်ငြိမ်းဆဲ အရာ ဖော်ပြချက်
- Atikkantakālavāro = ကာလ ကျော်လွန်ပြီးခြင်း ဖော်ပြချက်
- Suttantacittamissakaviseso = သုတ္တန်လာ စိတ်များကို ရောစပ်သော ထူးခြားချက်; Abhidhammacittamissakaviseso = အဘိဓမ္မာလာ
  စိတ်များကို ရောစပ်သော ထူးခြားချက်
- colophons: Paṇṇattivāro. / Uppādavāro. / Nirodhavāro. / Uppādanirodhavāro. / Pariññāvāro. = «X ဖော်ပြချက်။»;
  Saṅkhārayamakaṃ / Cittayamakaṃ niṭṭhitaṃ. = module («“…” ပြီးဆုံးပြီ။»; chapter names as proposed in the module:
  «ပြုပြင်ဖန်တီးမှုများကို / စိတ်ကို အတွဲလိုက် မေးဖြေခြင်း»)

## Departures from pi-1 … pi-5 and the sample (listed by check_ch6-8.py as exceptions, not counted)
1. kāya- / vacī- / cittasaṅkhāra: pi-5 ^5-458 «ကိုယ်၏ / နှုတ်၏ / စိတ်၏ ပြုပြင်ဖန်တီးမှု» (the same sense as here:
   breathing, thought and reflection, perception and feeling; Kathāvatthu on nirodhasamāpatti) taken, not pi-2 ^2-226
   «ကိုယ် / နှုတ် / စိတ် ပြုပြင်ဖန်တီးမှု» (paṭiccasamuppāda: volition by body, speech, mind). (The pi-5 termbase line
   for kāyasaṅkhāro reads «ကိုယ် ပြုပြင်ဖန်တီးမှု» without «၏», but every pi-5 rails occurrence has «ကိုယ်၏».)
2. uppādakkhaṇe «ဖြစ်ခြင်း ခဏ၌» (pi-5 ^5-366, identical Pāli word) vs the sample's uppāda «ဖြစ်ပေါ်ခြင်း» in headings
   (pi-1 Cittuppāda). Kept apart: uppāda- headings «ဖြစ်ပေါ်ခြင်း», the moment «ဖြစ်ခြင်း ခဏ». If the consistency pass
   prefers one word: «ဖြစ်ပေါ်ခြင်း ခဏ».
3. kāmāvacare / rūpāvacare / arūpāvacare as places: «ကာမဘုံ၌ …» (style-sheet plane names; sample arūpa «ရုပ်မရှိသော
   ဘုံ»); pi-1 ^1-988 kāmāvacare there qualifies citta («ကာမဘုံနှင့် ဆိုင်သော စိတ်…၌»).
4. yassa cittassa anantarā (inside a person group) «မိမိ စိတ်၏ ချက်ချင်း နောက်၌»: yassa is not the correlative
   «အကြင်သူအား» here.
5. Natthi «မရှိပါ။», anuloma / paccanīka, cavati: as the sample.

## Unsure Pāli / meaning
- The moment phrase («… assāsapassāsānaṃ uppādakkhaṇe») is taken with the person group right before it (pi-6-mr
  rule; the English zero-shot reads it over all the groups before). E.g. «Paṭhamajjhānaṃ samāpannānaṃ kāmāvacarānaṃ
  assāsapassāsānaṃ uppādakkhaṇe» = «ပထမ ဈာန်ကို ဝင်စားနေသူတို့နှင့် ဝင်လေ ထွက်လေတို့၏ ဖြစ်ခြင်း ခဏ၌ ကာမဘုံ၌
  ရှိသူတို့». A commentary would settle it (none read).
- «yassa cittassa anantarā kāmāvacarānaṃ pacchimacittaṃ uppajjissati»: kāmāvacarānaṃ (gen. pl.) read as «the last
  mind belonging to the sense sphere» («ကာမဘုံနှင့် ဆိုင်သော နောက်ဆုံး စိတ်»); literally «the last mind of the
  sense-sphere beings».
- «suddhāvāsānaṃ dutiye citte vattamāne»: «ဒုတိယ စိတ် ဖြစ်နေစဉ် သုဒ္ဓါဝါသ ဘုံ၌ ရှိသူတို့» (the suddhāvāsa beings while
  their second mind is going on).
- «ye ca … parinibbāyissanti tesaṃ cavantānaṃ» = «… ပရိနိဗ္ဗာန် ပြုမည့်သူတို့ထဲမှ စုတေဆဲသူတို့» (those of them who are dying).
- tesaṃyeva in a list gives «… ထိုသူတို့ပင်နှင့် …» (10 lines): grammatical, slightly heavy.
- -bhūmiyaṃ «… ရှိရာ အဆင့်၌» (pi-1 sukhabhūmiyaṃ) is used also as a place before «tattha»; «ဘုံ» would be plainer.
- (14) «khaṇaṃ khaṇaṃ vītikkantaṃ atikkantakālaṃ» = «ခဏ ခဏကို လွန်မြောက်ပြီး ကာလ ကျော်လွန်ပြီး»; «tassa cittaṃ?» =
  «ထိုသူအား စိတ် ထိုသို့ ဖြစ်သလော» (is the mind so for them?), as the English / Marathi rails.
- «(Yassa cittake sakabhāvena niddiṭṭhe, yaṃ cittake ca yassa yaṃ cittake ca ekattena niddiṭṭhe.)» translated as
  «when the yassa-citta questions are set out in their own form and the yaṃ-citta and yassa-yaṃ-citta questions as
  one» (the note's purpose is not certain).
- Natthi after a dhamma question (yaṃ cittaṃ …) «မရှိပါ။» = there is no such case.

## Source slips (translated as written)
- ^6-6-121 «… tesaṃ tattha kāyasaṅkhāro na nirujjhittha vacīsaṅkhāro ca nirujjhissati.» («na» probably for «ca»):
  «… ကိုယ်၏ ပြုပြင်ဖန်တီးမှု မချုပ်ငြိမ်းခဲ့၊ နှုတ်၏ ပြုပြင်ဖန်တီးမှုလည်း ချုပ်ငြိမ်းလိမ့်မည်။»
- ^6-8-83 «vītakkantaṃ» = vītikkantaṃ (same Burmese).
- Headings standing as body lines: ^6-6-2 / ^6-6-4 «(Kha) paccanīkaṃ», ^6-6-65 «4 (Ṅa) paccanīkaokāso» (stray «4» kept),
  ^6-8-82 «(14) Atikkantakālavāro»: translated as the heading text, numbers kept.
- ^6-6-16-5-0 «paccanīkaokāsā» (plural spelling) = «paccanīkaokāso»; «Uppajjamānananirodhavāro» = «Uppajjamāna-nanirodhavāro»;
  «Suddhacittasāmañña» = «Suddhacittasāmaññaṃ».
- ^6-6-31 «Yattha kāyasaṅkhāro uppajjittha…pe…» has no final «.»: Burmese ends «…».
- ^6-6-69 «(Kha) yassa vā pana…pe…. Āmantā.» («.» for «?»): same Burmese as «…?».
- ^6-6-81 / ^6-6-82 capital «…Pe…» after a full question: one «…».
- ^6-8-83 «Uppādakkhaṇe anāgataṃ cittaṃ.» (no «ca») = «Uppādakkhaṇe anāgatañca cittaṃ» (same Burmese).
