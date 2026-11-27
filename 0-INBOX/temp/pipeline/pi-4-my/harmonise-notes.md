# pi-4 Burmese zero-shot: consistency pass (harmonise) log

Brief `harmonise-brief.md`, items `harmonise-todo.md` (A1-A5, B1-B8). Pāli only; no Burmese translation or nissaya
opened, no web search; pi-1-my / pi-2-my / pi-3-my only read (pi-3-my/harmonise_pi12.py and harmonise_scan.py as
models). Nothing committed.

## How it was applied
- Backups before any edit: `harmonise-backup/` (every generator, check and module, `my4-zeroshot-terms.md`) and
  `harmonise-backup/chapters/` (all 12 chapter files before the pass). Before outputs: `align-before.txt` (7 differing),
  `align-hidden-before.txt` (1 unmatched).
- One place: `my4_formulas.py`, new block «consistency pass (harmonise)» after the reused words: BHAGAVA, TATHAGATA,
  SO / TASSA / TASSA_EVAM, EVAMEVAM, SEYYA, SANTO_PL / SANTO_SG, LOKE, BHIKKHUSU, tathupamo_my(), tattha_katame_my(),
  katame_n_my(), ime_santo_my(), VUCCATI_BARE, DUSS_HOTI / SIL_HOTI, OFTEN_ANGRY / NOT_OFTEN_ANGRY, KODHO_LONG /
  KODHO_SHORT, NELA / NELA_C (pi-1 ^1-1350), SAMAHITE, ASAVA4, JANATO, VIMUTTASMIM, KHINA, VIPPATISARA / VIPPATISARI,
  VIPASSATI, KHIRA, SALLEKHA, IDHA_PANA, and the one bracket renderer var_all() (= var_my) with the merged VAR_KIND,
  SIGLA_ALL, REF, BR_NOTE_END, BR_NOTE. New witnesses: bhagavato (pi-1 ^T-1), evameva (pi-2 ^2-643), khīraṃ (pi-2
  ^2-174), cetaso vippaṭisāro (pi-1 ^1-1166), dussīlo / sīlavā (pi-2 ^2-851), the nelā list (pi-1 ^1-1350), evamuparipi
  (pi-2 ^2-796), (sabbattha) (pi-2 ^2-754), aṭṭhakathā (pi-2 ^2-811), ma. ni. / dī. ni. (pi-2 ^2-760 / ^2-924).
- Generators: make_sample.py (A1, B5 vippaṭisārī / vipassati; its other tables unchanged), make_ch3-4.py, make_ch5.py,
  make_ch6-11.py take the forms above from the module; the three generator bracket renderers (ch3-4 BR_MY / _VAR_RE2,
  ch5 BR5 / var5, ch6-11 SIGLA_X / NOTE / var_my_x) were removed (B7). No chapter file was edited by hand.
- Checks updated where a form was changed on purpose (each says so in the code): every check has a new test «H.
  harmonised forms» (check_ch5: bhagavā in the ^4-177 epithet list = «ဘုန်းတော်ရှင်», B4; the others: none left), the
  reuse items «tathāgat… = မြတ်စွာဘုရား» kept (check_ch3-4 + bhagavatā = «မြတ်စွာဘုရား» against pi-1 bhagavato); check_ch3-4 ADAPTED
  reasons for «Pubbakālaṃ kodho …» and «… saṅkappati» (A2); check_ch6-11 B5 closings: quotes only where the Pāli has
  them (B1 / A2), NOT_NEG + «သူမ» (she, B3).
- New scripts: `harmonise_pi123.py`, `harmonise_scan.py` (+ `harmonise-table.tsv`), `harmonise_diff.py`,
  `regen_zeroshot.sh` (rebuild + every check; a second run changes no byte). Scratch helpers in `scratch/`.

## Items (chosen form; reason; generators changed; count)

### Part A: the source as written
- A1 ^4-1 / ^4-2 kālena kālaṃ samayena samayaṃ = «အခါအားလျော်စွာ အချိန်အလိုက်» (no «၊»: the Pāli has no mark; a sample
  string changed on the todo's order). make_sample.py UNIQUE. 2 lines (ch2).
- A2 (marks as in the Pāli, none added, none dropped; where the Pāli joins two clauses without a mark the Burmese joins
  them with the verb's connective form, no «၊»):
  * ^4-52 «… saṅkappati "mā maṃ jaññā"ti …» = «ကြံစည်၍ “…» (^4-72 has the comma: «ကြံစည်၏၊ “…», kept). make_ch3-4
    MAYA_Q52. 1 line.
  * ^4-46 / ^4-66 «Pubbakālaṃ kodho aparakālaṃ upanāho» (pi-2 ^2-891 has a comma) = «… အမျက်ဒေါသ ဖြစ်၍ နောက်ပိုင်း …»;
    ^4-66 «… upanāho yo evarūpo …» (no full stop) = «… သိုထားမှု ဖြစ်၍ ဤသို့ …». make_ch3-4 PUBBA. 2 lines.
  * ch8 ^4-204 and ch10 «… phusitvā viharati paññāya …» (no «;», ch2 has one) = «… ထိ၍ နေကာ ပညာဖြင့် …» /
    «… နေသည်ကား မဟုတ်ဘဲ ပညာဖြင့် …»; ch2 («;») and ch4 ^4-95 («,») keep «၊». make_ch6-11 _NoMark. 4 lines.
  * ch4 / ch5 / ch8 / ch10 «Ayaṃ vuccati puggalo X.» without quotes = «ဤပုဂ္ဂိုလ်ကို Xဟု ခေါ်သည်။» (no quotes; ch8 / ch10
    had added them). make_ch6-11 VNQ_RE, make_ch5 r_vuccati_plain (F.VUCCATI_BARE). 11 sentences (ch8 2, ch10 9).
  * confirmed, nothing changed: ^4-155 «ayaṃ vuccati, puggalo "…"» (the stray comma falls between subject and verb, which
    the Burmese frame «ဤပုဂ္ဂိုလ်ကို “…”ဟု ခေါ်သည်» does not separate: no place for a «၊»; explained); ^4-198 «… viharati,
    sabbapāṇabhūtahitānukampī byāpādapadosā …» (pi-2 / ch5 have the comma after «-anukampī»: one comma = one «၊», after
    the verb-final Burmese clause, pi-2 Burmese kept; «;» = «၊» as ch5); ^4-206 / ^4-208 the commas after
    «-ānusārī» = «၊», the closing «ti» of «… saddhāvimuttoti» has no quote to close (ch2 Burmese kept); ch10 «;» →
    «,» after abhisambujjhati = «၊». Not changed (not listed, the sample's clause break): «… pāpuṇāti balesu ca …»
    (mātikā, ch7, ch10, no comma) keeps the sample's «ရောက်၏၊» like ch2 (with comma).
- A3 added words: «သဘောထား၍» removed (ummujjati "…"ti = «“…”ဟု ပေါ်လာ၏»: «ဟု» renders «ti», the added verb is not in
  the Pāli; the same agent writes «“…”ဟု ဆွမ်းခံ၍သာ စားသူ ဖြစ်၏» elsewhere). make_ch6-11 _UMM_B. 6 lines (ch8).
  sallekha «ကိလေသာကို ခြစ်ခွာခြင်း» → «ခြိုးခြံခြင်း» (one plain word, no added object). F.SALLEKHA, make_ch6-11
  FOUR_B. 6 uses in 4 lines (ch6).
- A4 ^4-176 «puratthimena narassa» = «လူ၏ အရှေ့ဘက်၌» (as written; nagarassa «မြို့၏» was a different word). make_ch5.
  1 line. ^4-142 «samādiṭṭhi» kept as sammādiṭṭhi «မှန်ကန်သော အယူ ရှိသူ» (spelling only). ^4-166 «Idhekacco puggalo
  vaṇṇopi saṃvijjati avaṇṇopi saṃvijjati» (nominative) = «ဤလောက၌ အချို့သော ပုဂ္ဂိုလ်သည် ချီးမွမ်းဖွယ်လည်း ရှိ၏၊
  ကဲ့ရဲ့ဖွယ်လည်း ရှိ၏» («X သည် Y ရှိ၏» = X has Y; the reading «…၏ ရှေ့၌» "before" added a place not in the Pāli).
  make_ch5. 4 lines.
- A5 a space before «…» in the Pāli: «X…» everywhere; one ch5 «… …pe… "…"» (r_truths) had « … »: now «…» after the word.
  make_ch5. 1 line.

### Part B: one form per item
- B1 frames. Katamo ca puggalo X? (sample) 173 / 173 one form; Kathañca puggalo X (hoti)? / Evaṃ puggalo X (hoti). one
  form for each Pāli frame (79 / 80 lines: «…ဖြစ်သနည်း» with hoti, «…Vသနည်း» with a finite verb, as the Pāli);
  Tattha katamo X? (pi-1 / pi-2) one form. Changed: «Tattha katame N G puggalā?» = «ထိုတို့အနက် G ပုဂ္ဂိုလ် N-ယောက်
  ဟူသည် အဘယ် ပုဂ္ဂိုလ်တို့နည်း။» (ch3-4 and ch6-11 form, the plural of the sample's question; ch5 had «… အဘယ်တို့နည်း။»),
  9 lines (ch5); «Katame N?» = «အဘယ် N-ယောက်တို့နည်း။» (ch5 + ch6 form; the Pāli has no «puggalā»; ch4 had «အဘယ် ပုဂ္ဂိုလ်
  သုံးယောက်နည်း။»), 3 lines (ch4); the unquoted closings (A2), 11 sentences. F.tattha_katame_my / katame_n_my /
  VUCCATI_BARE; make_ch3-4, make_ch5, make_ch6-11.
- B2 shared sentences:
  * «yā sā vācā nelā kaṇṇasukhā … tathārūpiṃ vācaṃ bhāsitā hoti» = pi-1 ^1-1350 (neḷā …, the same words; binding over
    both agents' forms): «အပြစ်ကင်းသော၊ နား သာယာသော၊ ချစ်ခင်ဖွယ်ကောင်းသော၊ နှလုံးသားသို့ ရောက်သော၊ ယဉ်ယဉ်ကျေးကျေး
    ရှိသော၊ လူအများ နှစ်သက်သော၊ လူအများ စိတ်တွေ့သော စကား ရှိ၏ ထိုသို့သော စကားကို ပြောဆိုသူ ဖြစ်၏» (ch4 ^4-99 has a comma
    before tathārūpiṃ: «… ရှိ၏၊ ထိုသို့သော …»). F.NELA / NELA_C. 2 lines (ch4, ch5).
  * abhiṇhaṃ kujjhati = «ခဏခဏ အမျက်ဒေါသ (မ)ထွက်» (ch4; kodhano «အမျက်ဒေါသ ထွက်တတ်သူ»); So ca khvassa kodho (na) ciraṃ
    dīgharattaṃ anuseti = «ထိုသူ၏ ထိုအမျက်ဒေါသသည်ကား ကြာမြင့်စွာ ရှည်လျားသော ကာလပတ်လုံး ကိန်းအောင်း၏ / မကိန်းအောင်း»
    (ca kho = «ကား» as the sample's «So ca kho …» «ထိုသူသည်ကား»; anuseti = pi-2 «ကိန်းအောင်း», no added «နေ»). 6 lines
    (ch4 2, ch5 4).
  * dussīlo hoti pāpadhammo = «သီလ ပျက်သူ၊ ယုတ်မာသော သဘော ရှိသူ ဖြစ်၏», sīlavā hoti kalyāṇadhammo = «သီလ ရှိသူ၊
    ကောင်းမွန်သော သဘော ရှိသူ ဖြစ်၏» (pi-2 ^2-851 dussīla / sīlavā; «X hoti Y» = «X၊ Y ဖြစ်၏» as the sample's «…
    lābhī hoti akicchalābhī …»; ch3-4 had «… ဖြစ်၏၊ …», ch5 «သီလ ပျက်၍ …»; «Navo cepi bhikkhu hoti dussīlo …» = «… ဖြစ်အံ့»
    with the same nouns). 10 uses in 14 lines (ch3 2, ch4 8, ch5 4).
  * the arahant sentence: already one form (pi-2 ^2-831 without «တော်မူ», 12 / 12 lines); musāvādaṃ pahāya …: one form
    (ch4 = ch5); sense restraint (pi-1 ^1-1354): one form (ch3 = ch5); the hindrances and the first jhāna (pi-2 ^2-508):
    one form (ch5 = ch6, except «So», B3).
  * the knowledge passage of ch6 ^4-198 = ch5 ^4-183 … ^4-185 (three uses in ch5 against one in ch6): evaṃ samāhite
    citte … = SAMAHITE, «ime āsavā» plural «ဤသည်တို့ကား …», JANATO, VIMUTTASMIM (no added «သိသော»), KHINA («ပြုဖွယ်ကို»,
    no added «ကိစ္စ»). make_ch6-11. 2 lines (ch6).
  * santo saṃvijjamānā = «ရှိကြ၏၊ ထင်ရှား ရှိကြ၏» (ch5, 13 of the 25 sentences; saṃvijjati = «ရှိ» in ch5 / ch6),
    singular santo saṃvijjamāno = «ရှိ၏၊ ထင်ရှား ရှိ၏» (ch6 «ထင်ရှား ရှိနေသော»; the ordinal sentences now «ဤပထမ စစ်သည်သည်
    လောက၌ ရှိ၏၊ ထင်ရှား ရှိ၏။» as the plural frame), bhikkhūsu = «ရဟန်းတို့အတွင်း၌» (ch4; ch6 «…အထဲ၌»), «(Evamevaṃ)
    ime N G puggalā» = «G ဤပုဂ္ဂိုလ် N-ယောက်တို့သည်» (ch5; ch4 «ဤ G …»). ime_santo_my. 25 + 10 sentences (ch4, ch6).
  * evamevaṃ = «ထို့အတူပင်» (pi-2 evameva ^2-643; ch4 had «ဤအတူပင်»). 16 uses (ch4).
  * Seyyathāpi so X P, tathūpamo ayaṃ puggalo. = «ဥပမာအားဖြင့် ထိုXသည် Pသကဲ့သို့၊ ဤပုဂ္ဂိုလ်သည် ထိုXနှင့် တူ၏။»
    (ch6 form = the majority in each part: «ဥပမာအားဖြင့်» ch5 + ch6, the Pāli comma «၊» ch4 + ch6, «ထိုXနှင့်» ch5 + ch6).
    tathupamo_my. 44 sentences (ch4 12, ch5 32).
- B3 the person: So = «ထိုသူသည်», tassa / assa / taṃ = «ထိုသူ…» everywhere, also of a monk (ch4 the cloths, ch6 the
  warriors / monks, the ch6 training passage; pi-2 «ထိုရဟန်း…»); «bhikkhuṃ … upasaṅkamitvā» keeps «ထိုရဟန်းထံသို့» (the
  Pāli says bhikkhuṃ); ^4-196 «So taṃ disvā» = «ထိုသူသည် ထိုသူမကို မြင်၍» (taṃ = the woman). Tassa evaṃ hoti = «ထိုသူအား
  ဤသို့ အကြံ ဖြစ်၏» (ch6 had «ထိုသူ၌»). F.SO / TASSA / TASSA_EVAM; make_ch3-4, make_ch6-11. 12 + 45 + 1 uses.
  The pi-2 sentence «So araññagato vā …» (pi-2 ^2-508 «ထိုရဟန်းသည်») is the one explained pi-2 identity difference.
- B4 (revised by the coordinator after review, see «B4 revision» below): tathāgata (tathāgato, tathāgataṃ, tathāgatassa,
  tathāgate, tathāgatappavedita-) = «မြတ်စွာဘုရား» everywhere, as the locked pi-2 termbase (pi-2 ^2-760); bhagavā /
  bhagavatā in ordinary sentences (ch4 ^4-112 «… paṭicca bhagavatā …») = «မြတ်စွာဘုရား» (pi-1 bhagavato ^T-1, pi-2);
  ONLY in the ^4-177 epithet list «Idha tathāgato loke uppajjati … satthā devamanussānaṃ buddho bhagavā», where
  tathāgato is the subject of the same sentence, bhagavā = «ဘုန်းတော်ရှင်» (a context-specific epithet sense, kept apart
  from the subject «မြတ်စွာဘုရား»; ch5's form). buddho «သစ္စာတို့ကို သိတော်မူသူ» as before. The approved sample's
  Tathāgatappaveditā sentence is back to its pi-2-consistent form (byte-identical to before the pass). F.TATHAGATA (=
  W['tathagata']), F.BHAGAVA, F.BHAGAVA_EPITHET; make_ch3-4, make_ch5. Net against the backup: 0 lines (all as before).
- B5 vippaṭisāra = «နောင်တ ရခြင်း» (pi-1 / pi-2 termbase vippaṭisāro; kukkucca stays «နောင်တ ပူပန်မှု»), vippaṭisārī
  = «နောင်တ ရသူ», vippaṭisāraja = «နောင်တ ရခြင်းမှ ဖြစ်သော». make_sample REM, make_ch6-11 VIPPA_JA. 15 uses (ch1 1 line,
  ch6 4 lines). abhikkhaṇaṃ / abhiṇhaṃ «ခဏခဏ»: already one form (12 uses). vuṭṭhāti «ထမြောက်» (attainment) vs
  «ပျောက်ကင်း» (illness): already by sense. uttama «အထွတ်အထိပ်» / agga «အမြတ်ဆုံး»: already distinct. vipassati viloketi
  = «သေချာစွာ မြင်၍ ပတ်ဝန်းကျင်ကို ကြည့်» (ch8 form, no mark between the two verbs as in the Pāli; the mātikā had
  «မြင်၏၊ …»). make_sample, make_ch6-11 KATHA. 1 line (ch1).
- B6 simile and list vocabulary: the group names, members, the ascetic practices, the ten courses and the five sampadā
  were already one form per Pāli word (checked). Changed: khīra = «နွားနို့» (pi-1 / pi-2 termbase; ch5 ^4-176 had «နို့»),
  1 line; Idha pana(ekacco) = «တစ်ဖန် ဤလောက၌ …» (ch4; ch5 «ထို့ပြင်» is api ca in ch6), 3 lines (ch5); tathārūpa =
  «ထိုသို့သော» (pi-1 termbase; ch4 ^4-116 «ထိုသို့ သဘောရှိသော»), 1 line.
- B7 one renderer: my4_formulas.var_all() renders every bracket of the book (readings with or without sigla, several
  readings «[L (S1): a၊ (S2): b]» pi-2 ^2-832, sigla aṭṭhakathā «အဋ္ဌကထာ» / sabbattha «Sabbattha», references a. ni. /
  ma. ni. / dī. ni. / vibha., notes evamuparipi «နောက်တွင်လည်း ဤနည်းတူ», evaṃ tīsu ṭhānesupi «နေရာ သုံးခုလုံး၌လည်း
  ဤနည်းတူ», evaṃ …dukaniddesepi, padasiddhi …, rūpasiddhi …, passa …). It reproduces every earlier bracket byte for byte
  except one: ch5 «… kandarakasuttepi evameva» «… ၌လည်း ဤအတိုင်းပင် ဖြစ်သည်» = «… ၌လည်း ဤနည်းတူ» (the other «…pi
  likewise» notes). 1 line.
- B8 headings and colophons: already one form (Xuddeso, Xpuggalapaññatti, Xniddeso., Ekakaṃ … Dasakaṃ., the mātikā and
  book colophons on the pi-1 / pi-2 / pi-3 pattern). 0 lines.

## Numbers
- Lines changed: 126 (preamble 0, 1: 2, 2: 2, 3: 5, 4: 23, 5: 50, 6: 27, 7: 0, 8: 8, 9: 0, 10: 9, 11: 0).
- align_check: 7 differing before → 0; align_hidden: 1 unmatched before → 0.
- pi-1 identity 45 / 45; pi-2 35 / 36 + 1 explained (B3, «So araññagato …»); pi-3 2 / 2.
- harmonise_scan 75 / 75 items OK; agents' checks 0 mismatches: sample reuse 229 / 229, ch3-4 171 / 171 (14 adapted),
  ch5 108 / 108, ch6-11 74 / 74 (after the B4 revision: sample 230 / 230, ch3-4 174 / 174, ch5 108 / 108, ch6-11
  75 / 75; harmonised forms ch5 1 / 1, the others 0 / 0). check_chapter_ids / check_text_pe /
  check_marks OK for all 12 files; chk-pe copies deleted. regen_zeroshot.sh: ALL CHECKS PASSED, second run changes no
  byte.

## B4 revision (coordinator decision, 2026-11-19)
- The «တထာဂတ» proposal is withdrawn: tathāgata = «မြတ်စွာဘုရား» (pi-2 termbase), bhagavā / bhagavatā =
  «မြတ်စွာဘုရား» (pi-1 / pi-2), and only the ^4-177 epithet «… buddho bhagavā» = «ဘုန်းတော်ရှင်» (context-specific
  epithet, tathāgato the subject). my4_formulas TATHAGATA = W['tathagata'], new BHAGAVA_EPITHET; the shared SENT
  «Tathāgatappaveditā …» uses W['tathagata'] again (sample form); make_ch5 ^4-177 uses BHAGAVA_EPITHET.
- Checks: the tathāgata reuse items restored (check_sample, check_ch3-4, check_ch5, check_ch6-11), check_ch3-4 adds
  bhagavatā = «မြတ်စွာဘုရား»; «H. harmonised forms» = check_ch5 the ^4-177 epithet (1 / 1), the others none.
  harmonise_scan: three B4 items (bhagavā ordinary «မြတ်စွာဘုရား», the ^4-177 epithet, tathāgata «မြတ်စွာဘုရား»).
- Lines changed by this revision (against the files after the first pass): 12 (2: 2, 3: 1, 4: 6, 5: 1, 10: 2; the
  others 0); total against the pre-harmonise backup now 126.
- regen_zeroshot.sh run twice: ALL CHECKS PASSED; the second run changes no byte.
