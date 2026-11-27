# pi-5 Burmese zero-shot: consistency pass (harmonise) log

Brief `harmonise-brief.md`, items `harmonise-todo.md` (A1-A4, B1-B7). Pāli only; no Burmese translation or nissaya
opened, no web search, nothing in 0-INBOX/temp/language-priority/ opened; pi-1-my … pi-4-my only read
(pi-4-my/harmonise_pi123.py, harmonise_diff.py, harmonise_scan.py, regen_zeroshot.sh as models). Nothing committed.
References below are chapter:line (non-empty-line numbering of align_check) or block IDs.

## How it was applied
- Backups before any edit: `harmonise-backup/` (the 8 generators, the 8 checks, my5_formulas.py, terms_my5.py,
  my5-zeroshot-terms.md) and `harmonise-backup/chapters/` (all 32 chapter files before the pass). A rebuild before
  any edit reproduced the 32 files byte for byte. Before outputs: `align-before.txt` (39 differing),
  `align-hidden-before.txt` (4 unmatched), `scratch/pi1234-before.txt` (identity: 25 differing).
- One place: my5_formulas.py, blocks marked «consistency pass (harmonise …)»: ORD_MY 11-23, KATHA_NAME, SUTTA_IS /
  SUTTA_TI, UPROOT, ANUSAHA, AVECCA, KAYENA, JAHATI, PAHINA_V, BHAVITA_V, VERSE_RATANA / RATANA_LAST, AVATTANA /
  AVATTANA_IN, SARAMMANA_TH, KSA, SAMMUKHA, FAR4_HEAD / FAR4_LAST, EPI_ARAHA, LIKE_GROW, KAYAKAMMA / VACIKAMMA /
  MANOKAMMA, STAY, KUSALABYAKATE, VERSE_SANGHABHEDA, SAPHALA / SAVIPAKA / APHALA / AVIPAKA, BODHAGAMI, KAMEYYA,
  SAMANNAPHALA, RUPA_SEEN, GHAYATI / SAYATI, OVADA / ANUSASANI / PAPAKAMMA, PATIPANNAKA, BANDHANA / bandhitum() /
  KANTHA5, PAGGAHA_UPAGA, TATHEVA, VERSE_ANUPUBBA; two engine rules in line_my(): (1) a sentence whose Pāli has no
  quote mark gets none (harm_noq(), NO_QUOTES; the sample's vagga colophon excepted; brackets keep their own marks);
  (2) a table line (LINES) opens with «“» exactly when its Pāli line opens with a quote mark (was a post-pass of
  make_ch13-16 only).
- Generators take these values from the module (comments «harmonise A… / B…»); no chapter file was edited by hand.
  Changed lines per file: make_sample 8, make_ch2-5 31, make_ch6-10 64, make_ch11-12 28, make_ch13-16 34,
  make_ch17-20 42, make_ch21-25 63, make_ch26-31 51, my5_formulas 137 (terms_my5.py unchanged; it rewrites
  my5-zeroshot-terms.md from the tables). Every generator still runs on its own.
- New scripts: `harmonise_pi1234.py` (pi-1 … pi-4 identity; EXPLAINED list), `harmonise_align_explained.py` (every
  difference left by align_check / align_hidden must be explained), `harmonise_scan.py` (+ `harmonise-table.tsv`,
  78 items), `harmonise_diff.py`, `regen_zeroshot.sh` (rebuild + every check; a second run changes no byte).
  Scratch helpers in `scratch/` (pk.py, ctx.py, bw.py, forms.py, qcount.py, qadd.py, props.py, hcolo.py, rb.sh, chk.sh).

## Items (chosen form; reason; generators changed; count = other-form uses removed, from harmonise_scan.py)

### Part A: the source as written
- A1 quote marks the Pāli does not have: engine rule harm_noq() (a shared lookup key no longer forces marks):
  ^5-332 (10:249) «… ဟောတော်မူသလော – တတိယ ဈာန်… … ရှိသည်။» (1); ^5-407 «… ပြည့်စုံသူကို သောတာပန်ဟု ဆိုသင့်သလော»
  (unquoted; the quoted ^5-394 keeps «“…”») (6 lines); ch17 ^5-556 «… ပုထုဇဉ်ကို ကိန်းအောင်းခြင်း ရှိသူဟု …» and ^5-558
  «… ရဟန္တာကို ဉာဏ် ရှိသူဟု …» (ch19, quoted, keeps the marks) (2); five «Na vattabbaṃ – P-ti?» without marks (ch13,
  14, 15, 27, 29) «ဤသို့ မဆိုသင့်သလော – P။» (5); ^5-514: the opening «“» of the twice-used verse line is now the module
  rule (ch13-16 post-pass removed; output unchanged); 10:314 asmimāna «ငါဟူသော မာန» (the added ‘…’ removed; 1).
- A2 the regular “…” / ‘…’ nesting (approved with the sample) in every generator; no pair added (A1 rule). Kept on
  purpose: the Pāli's unclosed / irregular marks are closed (33 lines have more marks than the Pāli, 50 before: the
  sample's ^5-1 … ^5-116, stanzas and quotations whose Pāli closing mark is missing, e.g. 23:51 «"addhā
  parinipphannoti?»); 10:258 «Dhunātha …» keeps «’» (checker B4 needs the balanced pair). Left (8 lines, the same 8 as
  before): 1:27, 10:157 / 251-253 / 342, 25:44, 26:130 have fewer marks than the Pāli: a quoted clause inside a compound
  («"P"ti, attheva suttanto, …», «Tena hi "P"ti.») is rendered by the sample's prop_my / _f_tenahi «Pဟူ၍၊» without
  marks (the lookup keys have no quotes); 26:130 two quoted clauses share one pair.
- A3 added words: 4:29 / 4:32 Nirāmagandhā «ကိလေသာ» removed «အပုပ်နံ့ ကင်းကြ၍ …» (make_ch2-5 NIRAMA; 2);
  10:251 «Nanu "paṭhamaṃ jhānaṃ … niruddhā hotī"ti!» «”ဟူ၍ ဟောထားသည် မဟုတ်လော» -> «” မဟုတ်လော» (no verb
  supplied; make_ch6-10; 1); 6:5 «Atītaṃ khandhā» «အတိတ်သည် အစုအဝေးတို့ ဖြစ်သလော» kept (the copula a Burmese nominal
  question needs, as the sample's «X ဖြစ်သလော»); ch11 «… nuppajjissatīti katvā pahīnaṃ» «ထိုအရာကို» removed
  (make_ch11-12; 10 uses in 4 lines); ch21 sammukhībhūta «နှောင်ကြိုးနှင့်» removed: «မျက်နှာချင်းဆိုင် ဖြစ်နေသူ» (heading,
  colophon, uddāna, body; make_ch21-25; 8 uses).
- A4 no comma / full stop added where the Pāli has none (the verb's connective form joins the clauses): ^5-43 (the
  sample, 1:193) «… တွေ့ရ၍ မျက်စိ …» (make_sample; 1); ^5-274 «… ပြည့်စုံ၍ တစ်စိတ်တစ်ဒေသ …» (make_ch2-5; 1); ^5-292
  (5:85) «… မကြောက်ရွံ့မှု ရှိ၍ ပုထုဇဉ်သည် …» (make_ch2-5 _r_exist_has: a comma = «သည်၊», none = «၍»; 1); «X kusalampi
  akusalampi» «ကုသိုလ်လည်း ဖြစ် အကုသိုလ်လည်း …» (was «ဖြစ်၏၊» ch16, «ဖြစ်၍» ch18; make_ch13-16, make_ch17-20; 4); the
  ch10 / ch11 «… sīlehi samannāgato catubhāgaṃ / ekadesaṃ na …»: without comma «ပြည့်စုံ၍», with comma «ပြည့်စုံသည်၊»
  (make_ch6-10 _SOT / _SOT_C); ^5-306 (9:23) «Paṭhamavaggo» without full stop = «ပထမ ဝဂ်» (make_ch6-10; 1). Confirmed as
  written, nothing changed: ^5-116, ^5-164, ^5-323, ^5-379, ^5-456, ^5-509.

### B1 vagga ordinals
- One series, the Pāli ordinals (pi-3 «ဧကာဒသမ … စုဒ္ဒသမ ခွဲနည်း»): F.ORD_MY 11-23 (15-23 in the same Pāli spelling:
  ပန္နရသမ, သောဠသမ, သတ္တရသမ, အဋ္ဌာရသမ, ဧကူနဝီသတိမ, ဝီသတိမ, ဧကဝီသတိမ, ဗာဝီသတိမ «Bāvīsatima» as written, တေဝီသတိမ);
  make_ch17-20 ORD11 / ORD12, make_ch21-25 ORD_X, make_ch26-31 vagga(). ch26-31 «N-ခုမြောက် ဝဂ်» -> Pāli ordinal: 50
  headings / colophons. The paṇṇāsaka ordinals (Dutiyo … Catuttho) are F.ORD_MY already.

### B2 one form per term (the todo's precedence)
- aveccappasāda «ခိုင်မြဲသော ကြည်ညိုမှု» (ch3; was «မတုန်မလှုပ်သော …» ch10 / ch11): F.AVECCA; make_ch2-5, make_ch6-10
  (ch11-12 via P6). 3.
- aṇusahagata «အနည်းငယ်မျှ ကျန်ရှိသော» (ch2-5; was «သိမ်မွေ့သော» ch10 / ch12): F.ANUSAHA; make_ch6-10, make_ch11-12. 18.
- ucchinnamūla … anuppādadhamma = ch2 «… အမြစ်ပြတ်စေပြီး၊ ငုတ်တို ထန်းပင်ကဲ့သို့ ပြုပြီး၊ မရှိတော့အောင် ပြုပြီး၊ နောင်အခါ
  မဖြစ်ပေါ်တော့သော သဘော ရှိစေပြီး ဖြစ်…» (F.UPROOT; was ch10 / ch12 «… ဖြစ်၍ နောင်အခါ …»); make_ch6-10 UCCH_MY. 15.
- bodhagāmī «ထိုးထွင်း သိခြင်းဆီသို့ ဦးတည်သော» (ch4 / ch27; was «ဗောဓိဆီသို့» ch8 / ch12): F.BODHAGAMI; make_ch2-5,
  make_ch6-10, make_ch11-12, make_ch26-31. 5.
- rūparāga / arūparāga = pi-2 ^2-U49 «သိမ်မွေ့သော ရုပ်ဘဝကို / ရုပ်မရှိသော ဘဝကို တပ်မက်သော ရာဂ» (ch10 had «ရုပ်၌ /
  ရုပ်မဲ့၌ တပ်မက်မှု»): make_ch6-10. 4.
- dukkhanirodhagāminī paṭipadā = pi-2 ^2-189 «ဒုက္ခ ချုပ်ငြိမ်းရာသို့ ရောက်စေသော ကျင့်စဉ်» (ch10 had «… ချုပ်ငြိမ်းခြင်းသို့
  ရောက်ကြောင်း အကျင့်»): make_ch6-10. 7.
- «dibbena cakkhunā rūpaṃ passati»: rūpa seen = «အဆင်းအရောင်» (pi-2 ^2-517 «cakkhunā rūpaṃ disvā» = «မျက်စိဖြင့်
  အဆင်းအရောင်ကို မြင်၍»; ch10 / ch11), F.RUPA_SEEN; THE SAMPLE CHANGES (todo B2): PROP_1 / SENT_1 «Rūpaṃ passati.» /
  REL (1:419-421, 1:573, 1:577); make_sample, make_ch11-12. 5. check_sample C1 («rūpaṃ» = «ရုပ်») exempts the seen
  rūpa: reuse 1278 -> 1276. For review: the sample's next question «Rūpaṃ puggalo?» keeps «ရုပ်» (the khandha).
- jahati «စွန့်ပယ်» (kept apart from pajahati «ပယ်»): F.JAHATI; ch10 «အဘယ်ကို ပယ်သနည်း», «… လေးပုံတစ်ပုံ ပယ်သည်» ->
  «အဘယ်အရာကို စွန့်ပယ်သနည်း» (= ch3), «… စွန့်ပယ်သည်»; make_ch6-10. 16.
- sāmaññaphala «ရဟန်းအဖြစ်၏ ဖိုလ်» (pi-2 ^2-818 / pi-1 ^1-1023, ch4; was «ရဟန်း၏ အကျိုး» ch12 / ch26 / ch27):
  F.SAMANNAPHALA; make_ch2-5, make_ch11-12 (ch26-31 follows); sāmañña «ရဟန်းအဖြစ်» (pi-1; was «ရဟန်း အဖြစ်»). 12.
- ghāyati / sāyati = pi-1 ^1-1352 / pi-2 ^2-517 «နှာခေါင်းဖြင့် အနံ့ကို နမ်း၍ … လျှာဖြင့် အရသာကို လျက်၍» (todo: pi-1 / pi-2
  first; = ch12 / ch18 / ch25): F.GHAYATI «နမ်း», F.SAYATI «လျက်»; was «(အနံ့ / အရသာ)ကို ခံ» ch10 / ch16 / ch22 / ch26
  and the sample's «yo ghāyati … / yo sāyati …» «အနံ့ ခံ / အရသာ ခံ» — THE SAMPLE CHANGES too (one form; its negative
  «မ» + verb gave the ungrammatical «မအနံ့ ခံ», 1:415); make_sample, make_ch2-5 (SEE), make_ch6-10 (SENSE),
  make_ch13-16, make_ch21-25. 25. For review: pi-1 ^1-608 «sāyati» (āyatana definition) is «မြည်း».
- kameyya «ထိရောက်နိုင်» (ch5; was «တိုးဝင်ရာ» ch12 / ch23 / ch25; the «P, Q» join «သည်၊» as ch5): F.KAMEYYA;
  make_ch2-5, make_ch11-12, make_ch21-25. 30.
- paṇṇāsaka «ငါးဆယ်အစု» everywhere (already; Khuddako aḍḍhapaṇṇāsako «… ငါးဆယ်တစ်ဝက်အစု»): nothing changed.
- Saṅgaha (the 2nd paṇṇāsaka uddāna, ^5-604) = the ch15 heading «အကျုံးဝင်ခြင်း» (was «စုစည်းခြင်း»): KATHA_NAME;
  make_ch17-20. 1.
- Suttasādhanaṃ heading: ch5 = ch6 «သုတ္တန်ဖြင့် သက်သေပြခြင်း» (one form already).
- uddānas = the kathā headings: vagga 1 (9:19-20) brahmacariyavāso «မြင့်မြတ်သော အကျင့်ကို ကျင့်သုံးခြင်း» (ch3:5),
  odhiso «အပိုင်းအပိုင်း စွန့်ပယ်ခြင်း» (the Odhisokathā heading), sabbatthivādo «အရာအားလုံး ရှိသည်ဟူသော ဝါဒ» (the ch5
  heading); the paṇṇāsaka uddānas: niggaho «စိတ်ကို ချုပ်ကိုင်ခြင်း» (the (156) Niggahakathā heading; was the dialectic
  «ချေပချက်», a sense error; 28:104 ^5-877, 31:60), puññasañcayo «ကောင်းမှု စုဆောင်းခြင်း» (the ch25 heading; was
  «ကုသိုလ် …»), Mahā «ကြီးမားသော အစု» (Mahāpaṇṇāsako; was «ကြီးမြတ်သော»), vavatthitā «ပိုင်းခြား သတ်မှတ်ပြီး ဖြစ်ခြင်း»
  (= the ch23 uddāna); KATHA_NAME; make_ch6-10, make_ch21-25, make_ch26-31. 8 uses in 5 lines.

### B3 natural words avoided because of a checker artefact
- ovāda «ဆုံးမခြင်း» / anusāsanī «သွန်သင်ခြင်း» (pi-4 ^4-191 «ovadiyamāna … anusāsiyamāna» = «ဆုံးမခံရ၍ … သွန်သင်ခံရ»;
  was «ဩဝါဒ / အနုသာသနီ» 26:21; the ch15 verse «Ovādakārī» «ဆုံးမ စကား», was «ဩဝါဒ စကား»): F.OVADA / ANUSASANI;
  make_ch26-31, make_ch13-16. «ဆုံးမ» added to NOT_NEG of every checker with a «မ» count (check_ch2-5, ch11-12,
  ch13-16, ch17-20, ch21-25, ch26-31; check_sample / check_ch6-10 have none). 3.
- pāpakamma: «ယုတ်မာသော ကံ» kept — it is the approved sample's word for pāpaka kamma (1-puggalakatha «ကောင်းမွန်သော
  ကံနှင့် ယုတ်မာသော ကံ»), not only an avoidance; ch18 «ဆိုးညစ်သော ကံ» -> «ယုတ်မာသော ကံ» (F.PAPAKAMMA, make_ch17-20; 2).
  «မကောင်းမှု» stays the word for apuñña (ch25).
- avipāka «အကျိုး မရှိသော» (the natural negative of the sample's savipāka «အကျိုး ရှိသော»; was «အကျိုး မပေးသော» ch7 /
  ch18, chosen only to keep «မရှိ» for natthi): F.AVIPAKA; make_ch6-10 (ch17-20 follows); avipāka (and aphala
  «အသီးအပွင့် မရှိသော» in check_ch11-12 …) added to the existence checks' EXEMPT. 18.
- searched the notes for others: gūtha / mutta «ကျင်ကြီး / ကျင်ငယ်» (ch13-16 avoided «မစင်») is the natural polite word
  too (= ch26 uccārapassāva): kept. No other avoidance found.

### B4 distinct terms
- paṭipannaka = pi-4 paṭipanna «ကျင့်ကြံသူ» (^4-M-7), sekha «ကျင့်ကြံဆဲသူ» (pi-1 ^1-M1-11) kept apart: F.PATIPANNAKA;
  make_ch6-10 (_PTK), make_ch11-12 (the ^5-417 uddāna). 13.
- saṅgahita «အကျုံးဝင်» / the ^5-472 simile «စုစည်းထား» (goṇā dāmena saṅgahitā: tied together): a sense difference, kept.
- bandhana «အနှောင်အဖွဲ့», kept apart from saṃyojana «နှောင်ကြိုး»; the stock sentence «labbhā X addubandhanena bandhituṃ
  … kaṇṭhapañcamehi bandhanehi bandhituṃ» = ch5's construction with «အနှောင်အဖွဲ့» (F.bandhitum, KANTHA5; ch5 had
  «အနှောင်», ch12 «… ချည်နှောင်ရန် …»); make_ch2-5, make_ch11-12. 20.

### B5 dialectic frames (the sample's words for the shared parts)
- «"P"ti – (n)attheva suttanto(ti?)» = «“P”ဟု – ထိုသို့သော သုတ္တန် အမှန်ပင် (မ)ရှိ…» (ch14, the earliest; ATTHEVA words;
  was «” –» ch18, «” – ဤသို့သော» ch22-23, «”ဟူ၍ –» ch28 / ch31): F.SUTTA_TI / SUTTA_IS; make_ch13-16, make_ch17-20,
  make_ch21-25, make_ch26-31. 36. The same «ti» before a dash elsewhere: the wish frame «"…"ti – atthi
  adhippāyaiddhi» «”ဟု –» (ch29; 7), 16:60 «… vucca"nti –» «”ဟု –».
- the closing «ti» of a quotation before the reference / at the end = «”» (the sample; was «”ဟူ၍» in ch10-12, 15-16,
  21-22, 24-25, 28-29): make_ch6-10, ch11-12, ch13-16, ch21-25, ch26-31 (41 strings). 26 uses. «ဟူ၍» kept where the
  grammar needs it: «“ဣ”ဟူ၍လည်း …» (listing, ch19), «…ဟူ၍ဖြစ်စေ» (vā … vā, ch11), the three quotations of 26:7.
- «Nanu āyasmā sāriputto etadavoca –» = ch11 «… ဤသို့ ပြောခဲ့သည် မဟုတ်လော –» (ch30 had «ဆိုခဲ့»; «လျှောက်ခဲ့» stays for
  words addressed to the Buddha, as the sample): make_ch26-31. 2.
- checked, one form already: «Tena hi P-ti…pe….» (ch13-16 / ch17-20 «သို့ဖြစ်လျှင် P…»), «Na hevaṃ vattabbe…pe… "P"ti?»,
  «P, na vattabbaṃ – "Q"ti?» / «Tena hi P, na vattabbaṃ –» (ch21-25: the sample's «ဤသို့ မဆိုသင့်(သလော) –»), «X-ti katvā
  P-ti?» (KATVA), «Hañci P, no vata re vattabbe» (if_my neg), «Yathā A, evamevaṃ B» («Aသကဲ့သို့ ထို့အတူပင် B»).

### B6 stock passages and sutta quotations (identical Pāli = identical Burmese)
- align_check 39 -> 1 (explained), align_hidden 4 -> 0. Changed to the earlier chapter's (or pi-1 … pi-4's / the
  sample's) Burmese: the Ratana verse and Dhammapada 239 of ch10 = ch3 (F.VERSE_RATANA / VERSE_ANUPUBBA; make_ch2-5 and
  make_ch6-10 both take them); «X-phalasacchikiriyāya paṭipanno … dukkhadassanena kiṃ jahati» = ch3 (DASS, arahatta
  «ရဟန္တာ အဖြစ်» ARHT); «Nanu arahato rāgappahānāya maggo bhāvito» = ch2: pahīna / bhāvita «ပယ်ပြီး ဖြစ် / ပွားများပြီး
  ဖြစ်» (F.PAHINA_V / BHAVITA_V; was «…ပြီးသည်» ch10 / ch11 / ch20 / ch27); the «ekadesaṃ / catubhāgaṃ sotāpanno …
  phalappatto paṭiladdho … kāyena phusitvā viharati …» passage of ch10 / ch11 = ch3 («ဖြစ်သည်၊ … ရောက်ပြီး၊ ရရှိပြီး၊
  ပိုင်ဆိုင်ပြီး၊ မျက်မှောက်ပြုပြီး၍ ပြည့်စုံစွာ ဝင်ရောက်၍ နေသည်၊ ကိုယ်ဖြင့် ထိ၍ နေသည်၊ …»; kāyena phusitvā = pi-4
  «ကိုယ်ဖြင့် ထိ၍», F.KAYENA, also ch13; 27); the arahant's epithets of ch10 / ch11 = ch2 (F.EPI_ARAHA; 6) and
  «samudayo pahīno / nirodho sacchikato» «ဒုက္ခ ဖြစ်ပေါ်ခြင်း / ဒုက္ခ ချုပ်ငြိမ်းခြင်း …»; the āvaṭṭanā list = ch15
  (F.AVATTANA, paṇidhi «ဆုတောင်းခြင်း»: was «ဆုတောင်းမှု» ch18, «စိတ်ကို ထားရှိခြင်း» ch24, «စိတ် ဦးတည်ထားခြင်း» ch27; 164)
  with «atthi tassa / tāya» «ထိုအရာ၌» (was «ထိုအရာ၏» ch24, «ထိုဓာတ်၌» ch27; 60) and «…sārammaṇaṃ, atthi tassa …»
  «… အရာ ဖြစ်သည်၊ ထိုအရာ၌ …» (ch24 «ဖြစ်၍»); (s)ārammaṇa as predicate «အာရုံ (မ)ရှိသော အရာ (ဖြစ်)» (ch15 / ch16 / ch23 /
  ch24 / ch27; ch17-20 had «Xသည် အာရုံ (မ)ရှိ», 45, incl. the (86)-(88) headings «… အာရုံ ရှိသော / မရှိသော အရာ
  ဖြစ်သည်ဟူသော» and the ch17 uddāna); «kusalākusalā sāvajjānavajjā hīnapaṇītā kaṇhasukkasappaṭibhāgā dhammā» = pi-4
  ^4-104 (F.KSA; ch15 had «… အပြစ် ကင်းသော … မြင့်မြတ်သော … မည်းသော ဖြူသော») + «သဘောတရားတို့သည်»; sammukhībhāvaṃ
  āgacchanti = ch15 «မျက်နှာချင်း ဆိုင်ခြင်းသို့ ရောက်ကြ» (F.SAMMUKHA; was «မျက်မှောက်သို့ ရောက်လာကြ» ch18-19,
  «မျက်နှာချင်းဆိုင် ဖြစ်လာကြ» ch21 / ch27; 26); the sutta a. ni. 4.47 «cattārimāni … suvidūravidūrāni» = ch15
  (F.FAR4_*; ch21 had «သူယုတ်မာတို့မှ», ch27 «မြေကြီး»; 7); «latā viya vaḍḍhati, māluvā viya …» = ch15 (F.LIKE_GROW); the
  nibbāna epithets «tāṇaṃ … parāyaṇaṃ accutaṃ amataṃ» = ch10 (parāyaṇa «မှီခိုရာ», amata «အမြိုက်»; ch27 had
  «ဆုံးခန်းတိုင်ရာ», «မသေသော အရာ»; ch30 amatogadha «မသေခြင်း» -> «အမြိုက်»; check_ch26-31 PRIV amata = 0) and «X
  tāṇāni…pe… antarikā vā» = the series of ch10 / ch14; kāyakamma / vacīkamma / manokamma «ကိုယ် / နှုတ် / မနောဖြင့် ပြုသော
  ကံ» (ch14 …; was «ကာယကံ / ဝစီကံ / မနောကံ» ch22 / ch24, «ကိုယ်အမှု၊ နှုတ်အမှု» ch28); saphala / savipāka = the sample
  «အသီးအပွင့် ရှိသော၊ အကျိုး ရှိသော» (ch18 «အကျိုး ရှိသော၊ အကျိုး ပေးသော», ch22 «အကျိုး ရှိ၍ ကံ၏ အကျိုး ရှိသော», ch25
  saphalo); tiṭṭheyya «တည်နေရာ» (ch19, F.STAY; ch21 «တည်ရာ»); «kusalābyākate citte vattamāne» = ch19
  (F.KUSALABYAKATE; ch22 «… သို့မဟုတ် …», other order); the saṅghabheda verse of ch28 = ch21 (F.VERSE_SANGHABHEDA;
  saṅghabhedaka «သံဃာကို သင်းခွဲသူ» = ch10; the ch28 Upāli passage «… ငရဲ၌ ကျမည့်၊ ကမ္ဘာ ပတ်လုံး တည်ရမည့် …»); «Ratto
  rāgaṃ jahati, …», «rāgena rāgaṃ …», «Rāgo cittasampayutto, maggo …» = the sample's «P, Q» join «Pသည်၊ Q» (= ch27;
  ch21 had «၍»); paggahaniggahupaga chedanabhedanupaga = ch5 (F.PAGGAHA_UPAGA; ch15 «… နှိမ့်ချခြင်းကို ခံနိုင်သော»).
- align_check, explained (harmonise_align_explained.py): 1:426 «Tena hi na vattabbaṃ – "puggalo upalabbhati …"ti.» (the
  sample): the tool cuts the Pāli after «vattabbe.», so «…Pe….» opens the unit; the Burmese renders it where it stands.
- pi-1 … pi-4 identity (harmonise_pi1234.py): «Taṃ kissa hetu?» = pi-2 / pi-4 «ထိုသို့ အဘယ်ကြောင့်နည်း။» (make_ch2-5; 2).
  Explained: «Natthi.» «မရှိပါ။» (19; the sample's answer register «ဟုတ်ပါသည် / ဤသို့ မဆိုသင့်ပါ»; pi-3 answers a
  catechism question «မရှိ။») — for review; «Katame pañca? / Katame tayo?» «… ပါး» (2:135, 5:102: things here, persons
  in pi-4).

### B7 headings, colophons, uddānas, bhāṇavāra, book colophon
- -ti kathā headings / colophons «Xဟူသော» attached: Sabbamatthītikathā «အရာအားလုံး ရှိသည်ဟူသော» (make_ch2-5),
  Ariyantikathā «အရိယာဟူသော» (make_ch11-12). 4 lines.
- tatheva in the uddānas = the sample's «ထိုအတိုင်းပင်» (1:683; F.TATHEVA; was «ထို့အတူပင်» ch14, the word of evamevaṃ,
  and «ထိုနည်းတူပင်» ch17 / ch20): make_ch13-16, make_ch17-20. 4.
- bhāṇavāra = pi-1 ^1-57 «ရွတ်ဖတ်ရန် အပိုင်း» (was «ရွတ်ဆိုရန် …», ch31): make_ch26-31. 1.
- checked, one form: every kathā heading = its colophon (scratch/hcolo.py; ch19 «“ဤကား ဒုက္ခ”» / colophon «‘ဤကား ဒုက္ခ’»
  = the nesting inside «“…” ပြီးဆုံးပြီ»); the book colophon «“…” ကျမ်း ပြီးဆုံးပြီ။» (pi-1 … pi-3 pattern).

## Checks updated on purpose (each says so in the code)
- check_ch6-10 … check_ch26-31: EXEMPT (existence) + anabhāvaṅkata, niraggaḷa, avipāka (+ aphala from check_ch11-12 on;
  arūparāga in check_ch6-10); PRIV + anabhāvaṅkata (check_ch11-12 …), sāvajjānavajja (check_ch13-16), asabbhi
  (check_ch21-25), amata = 0 (check_ch26-31); NOT_NEG + «ဆုံးမ»; the B5 recurring-sentence test keyed with the Pāli
  quote marks (harm_noq) in all 8 checks; check_ch6-10 B6 tests LINES before COLO (as the engine); check_sample C1
  exempts the rūpa seen by the divine eye (F.RUPA_SEEN).

## Final numbers
- lines changed 450 (preamble 0, ch1 8, 2 0, 3 1, 4 3, 5 6, 6 0, 7 5, 8 2, 9 3, 10 74, 11 23, 12 24, 13 4, 14 2, 15 14,
  16 14, 17 35, 18 25, 19 1, 20 17, 21 20, 22 14, 23 5, 24 20, 25 9, 26 25, 27 36, 28 18, 29 16, 30 13, 31 13).
- check_chapter_ids / check_text_pe / check_marks OK × 32; the 8 agents' checks 0 mismatches, reuse 1276 / 1276, 1331 /
  1331, 882 / 882, 1115 / 1115, 1152 / 1152, 1063 / 1063, 1002 / 1002, 663 / 663; align 1 (explained), align_hidden 0;
  identity pi-1 2 / 2, pi-2 4 / 4, pi-3 2 / 21 + 19 explained, pi-4 5 / 7 + 2 explained; harmonise_scan 78 / 78;
  regen_zeroshot.sh run twice: no byte changed.
