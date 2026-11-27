# pi-7 Burmese zero-shot: 4-15 … 4-21 (the TIKADUKA chapters: a triad combined with a dyad)

Translated from the Pāli only (no Burmese translation or nissaya opened, no web search, `language-priority/` not
opened). Meaning cross-checked with the English zero-shot only (the odd notes of 4-15 ^7-49-79 / ^7-49-179 and the
4-17 layout under heading 1-18). Generator `make_ch4-15-21.py`, check `check_ch4-15-21.py`. Scratch: `chk-ch4-15-21/`
(build_check.py = the one-off that derived the check from check_ch4-10-14.py; dev / probe helpers; new.txt).

## Status (all pass, 2026-11-24)
| file | segments | lines | check_chapter_ids | check_text (pe-folded, own folder chk-pe/ch4-15-21/) | check_marks |
|---|---|---|---|---|---|
| 4-15-tikaduka-hetuduka.md | 579 | 1350 | OK | OK | OK |
| 4-16-tikaduka-sappaccayaduka.md | 93 | 175 | OK | OK | OK |
| 4-17-tikaduka-asavaduka.md | 66 | 137 | OK | OK | OK |
| 4-18-tikaduka-sarammanaduka.md | 60 | 123 | OK | OK | OK |
| 4-19-tikaduka-kilesaduka.md | 60 | 105 | OK | OK | OK |
| 4-20-tikaduka-dassanenapahatabbaduka.md | 105 | 186 | OK | OK | OK |
| 4-21-tikaduka-sauttaraduka.md | 158 | 323 | OK | OK | OK |

check_ch4-15-21 (all seven): 2399 lines × S P C O N, 3301 sentences for identity, 473 table values: **0 mismatches**.
Reuse: **25 / 25** pi-1 … pi-6 values identical wherever their Pāli occurs (474 witnessed); sentences also in
pi-1 … pi-6: **534 / 534** identical. Sentences shared with the finished pi-7 groups: **74 / 78** identical (the 4
differences are with 5-01 / 5-02, see «For the consistency pass»; all 4 follow the dukatika models).
`--sample`: the approved sample (1-00, 1-02) regenerates identical (raw and prepped). `--regress`: 4-02 … 4-09
(make_ch4-02-09) and 4-10 … 4-14 (make_ch4-10-14) regenerate identical with this script's extensions loaded.
`--mutate`: **14 / 14** planted errors caught. check_text_pe7.py was NOT run (it deletes the shared chk-pe/); the text
check ran on `chk-pe/ch4-15-21/` only, deleted afterwards (`check_ch4-15-21.py --pe` does the same).

## Method
- `make_ch4-10-14.py` is IMPORTED as Y (it imports the model `make_ch4-02-09.py` as X; no main() runs): all dyads of
  worlds A (3-01 … 3-06), B (3-07, 3-08, 3-10), C (3-09), E (4-01), the triads, names, note pieces and the dyad
  engines are used as they are and extended in memory. No file of another group is written.
- Combined term in the Pāli order: «<triad term> <dyad term>» -> one synthetic a-stem term (the case of the triad
  word; for bahiddhā the dyad word's; a closing «-ñca» on a one-word dyad term = the conjunct «-añca»; in the
  two-member dyads «… ceva … ca» the «ca» belongs to the term) whose Burmese is «<triad term>၊ <dyad term>» (the
  dukatika «A၊ B N» with the terms in the Pāli order), e.g. «ကုသိုလ်၊ အမြစ် ဖြစ်သော သဘောတရား».
- Part names «<triad name>နှင့် <dyad name>»; group headings «X-ttika-Y-ādidukāni» «<triad name>နှင့် <Y dyad name>
  စသည်» (the pattern of Y's «Pītisahagatādidukaṃ»); pada headings «<dyad term> ပုဒ်» (also with stars, and the line
  «Nahetupadaṃ.»); colophons «“<triad name>နှင့် <dyad / cluster name>” ပြီးဆုံးပြီ။».
- Group parts (4-17 1-20-54, 4-18 1-58-65 / 1-69-74, 4-20 1-90-92): the dyads the Pāli uses there are active
  together, in their own world (4-17's 1-20-54 part runs in world B with the parāmāsa dyad; 4-18's 1-69-74 in world
  B with the upādāna dyad).
- Counts above 24 (ekavīsa … sattatiṃsa, 4-15): make_ch2-01-02's words (NUM_ADD) added to every world, and the term
  endings' «-e <count>» exclusion widened as make_ch2-01-02 does it (else «vipāke ekavīsa» read as the vipāka term).
- Hand lines (built from the tables, 4-17 ^7-51-34): the cluster line «Akusalaṃ saññojanaṃ … nīvaraṇaṃ….», the
  line «Kusalaṃ noparāmāsaṃ … (Āsavagocchakasadisaṃ.) Diṭṭhiṃ paṭicca diṭṭhi na uppajjati.» (its first sentence
  through the world-B engine) and «Kusalattike cha gocchakaṃ niṭṭhitaṃ.».
- Coordinator decisions: «Anulomaṃ.», the «Sahajātā –» label, asaññasattānaṃ, the heinous deeds and the sixth-dyad
  forms do not occur as such in these chapters (the sixth dyads keep the finished groups' forms). Nothing supplied.

## New recurring terms, names and frames (Pāli = Burmese)
- nakenaci viññeyy- (4-16 ^7-50-48, as written; = 5-02 / 5-04) = တစ်စုံတစ်ခုသော စိတ်ဖြင့် သိနိုင်သည် မဟုတ်သော
- yathā sahajātavārampi… sampayuttavārampi evaṃ vitthāretabbaṃ = အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်… ယှဉ်တွဲခြင်းအလိုက် ဖော်ပြချက်တို့ကဲ့သို့ ထိုနည်းတူ အကျယ် ချဲ့ရမည်
- gocchakaṃ (the cluster) = အစု (= 5-01 … 5-04)
- na uppajjati = မဖြစ်ပေါ်
- *Hetu-ārammaṇa-adhipatipaccayā* = *အမြစ်ဟူသော အကြောင်း၊ အာရုံဟူသော အကြောင်းနှင့် အကြီးအမှူးဟူသော အကြောင်း*
- *Hetu-ārammaṇa-anantarapaccayā* = *အမြစ်ဟူသော အကြောင်း၊ အာရုံဟူသော အကြောင်းနှင့် ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းဟူသော အကြောင်း*
- *Ārammaṇa-adhipati-anantarapaccayā* = *အာရုံဟူသော အကြောင်း၊ အကြီးအမှူးဟူသော အကြောင်းနှင့် ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းဟူသော အကြောင်း*
- *Hetusahajātapaccayādi* = *အမြစ်ဟူသော အကြောင်းနှင့် အတူ ပေါ်ပေါက်ခြင်းဟူသော အကြောင်း စသည်*
- Dhammānulome tikadukapaṭṭhānaṃ = သဘောတရား အဟုတ်ပြ ပုံစံ၌ သုံးမျိုးတွဲနှင့် နှစ်မျိုးတွဲတို့၏ အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ
- Catuttho bhāgo niṭṭhito. = စတုတ္ထ အပိုင်း ပြီးဆုံးပြီ။
- *Nahetupadapaccayacatukkaṃ* = *အမြစ် မဟုတ်သော ပုဒ်၏ အကြောင်း လေးမျိုးတွဲ*
- aññamaññanissayapaccayā sahajātapaccayasadisā = အချင်းချင်း ထောက်ပံ့ခြင်းဟူသော အကြောင်းနှင့် အမှီဟူသော အကြောင်းတို့သည် အတူ ပေါ်ပေါက်ခြင်းဟူသော အကြောင်းနှင့် တူကြသည်
- yathā saṃkiliṭṭhattikahetudukaṃ, evaṃ vitthāretabbaṃ = ကိလေသာဖြင့် ညစ်နွမ်းခြင်း သုံးမျိုးတွဲနှင့် အမြစ် နှစ်မျိုးတွဲကဲ့သို့ ထိုနည်းတူ အကျယ် ချဲ့ရမည်
- kenaciviññeyyasadisaṃ = တစ်စုံတစ်ခုသော စိတ်ဖြင့် သိနိုင်သော သဘောတရားနှင့် တူသည်
- Kusalattika-saññojanādidukāni = ကုသိုလ် သုံးမျိုးတွဲနှင့် နှောင်ကြိုး နှစ်မျိုးတွဲ စသည်
- Akusalaṃ saññojanaṃ dhammaṃ paṭicca…pe… akusalaṃ ganthaṃ… oghaṃ… yogaṃ… nīvaraṇaṃ…. = အကုသိုလ်၊ နှောင်ကြိုး ဖြစ်သော သဘောတရားကို မှီ၍… အကုသိုလ်၊ အထုံး ဖြစ်သော… ရေအလျဉ် ဖြစ်သော… ထမ်းပိုး ဖြစ်သော… အတားအဆီး ဖြစ်သော…။
- Diṭṭhiṃ paṭicca diṭṭhi na uppajjati. = အယူကို မှီ၍ အယူသည် မဖြစ်ပေါ်။
- Kusalaṃ noparāmāsaṃ dhammaṃ paṭicca kusalo noparāmāso dhammo uppajjati hetupaccayā. (Āsavagocchakasadisaṃ.) Diṭṭhiṃ paṭicca diṭṭhi na uppajjati. = ကုသိုလ်၊ မှားယွင်းသော ယူဆမှု မဟုတ်သော သဘောတရားကို မှီ၍ ကုသိုလ်၊ မှားယွင်းသော ယူဆမှု မဟုတ်သော သဘောတရားသည် အမြစ်ဟူသော အကြောင်းကြောင့် ဖြစ်ပေါ်သည်။ (စိတ်အစွန်းအထင်းတို့၏ အစုနှင့် တူသည်။) အယူကို မှီ၍ အယူသည် မဖြစ်ပေါ်။
- Kusalattike cha gocchakaṃ = ကုသိုလ် သုံးမျိုးတွဲ၌ အစု ခြောက်ခု
- Kusalattike cha gocchakaṃ niṭṭhitaṃ. = “ကုသိုလ် သုံးမျိုးတွဲ၌ အစု ခြောက်ခု” ပြီးဆုံးပြီ။
- Kusalattika-cittasampayuttādidukāni = ကုသိုလ် သုံးမျိုးတွဲနှင့် စိတ်နှင့် ယှဉ်တွဲခြင်း နှစ်မျိုးတွဲ စသည်
- Kusalattika-upādānādidukāni = ကုသိုလ် သုံးမျိုးတွဲနှင့် စွဲလမ်းမှု နှစ်မျိုးတွဲ စသည်
- sahajātavārampi… pañhāvārampi evaṃ vitthāretabbaṃ = အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း… ပြဿနာအလိုက် ဖော်ပြချက်လည်း ထိုနည်းတူ အကျယ် ချဲ့ရမည်
- sahajātavārampi… sampayuttavārampi pañhāvārampi evaṃ vitthāretabbaṃ = အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း… ယှဉ်တွဲခြင်းအလိုက် ဖော်ပြချက်လည်း၊ ပြဿနာအလိုက် ဖော်ပြချက်လည်း ထိုနည်းတူ အကျယ် ချဲ့ရမည်
- upādānagocchakaṃ vitthāretabbaṃ = စွဲလမ်းမှုတို့၏ အစုကို အကျယ် ချဲ့ရမည်
- Kusalattika-pītisahagatādidukāni = ကုသိုလ် သုံးမျိုးတွဲနှင့် ပီတိနှင့်အတူ ဖြစ်ခြင်း နှစ်မျိုးတွဲ စသည်
- kusalasavitakkasadisaṃ = ကုသိုလ်၊ စတင်ကြံစည်မှု ရှိသော သဘောတရားနှင့် တူသည်
- sahajātavārepi… pañhāvārepi sabbattha vitthāro = အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်၌လည်း… ပြဿနာအလိုက် ဖော်ပြချက်၌လည်း နေရာတိုင်း၌ အကျယ် ချဲ့ခြင်း
- sahajātavārepi… pañhāvārepi tattakāva pañhā = အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်၌လည်း… ပြဿနာအလိုက် ဖော်ပြချက်၌လည်း ပြဿနာများသည် ထိုမျှသာ
- sahajātavārepi … pañhāvārepi sabbattha vitthāro = အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်၌လည်း … ပြဿနာအလိုက် ဖော်ပြချက်၌လည်း နေရာတိုင်း၌ အကျယ် ချဲ့ခြင်း

## Part names (Xttika-Ydukaṃ = <triad name>နှင့် <dyad name>), as used
- Kusalattika-hetudukaṃ = ကုသိုလ် သုံးမျိုးတွဲနှင့် အမြစ် နှစ်မျိုးတွဲ
- Vedanāttika-hetudukaṃ = ခံစားမှု သုံးမျိုးတွဲနှင့် အမြစ် နှစ်မျိုးတွဲ
- Vipākattika-hetudukaṃ = ကံ၏ အကျိုး သုံးမျိုးတွဲနှင့် အမြစ် နှစ်မျိုးတွဲ
- Upādinnattika-hetudukaṃ = ကံကြောင့် ဖြစ်ခြင်း သုံးမျိုးတွဲနှင့် အမြစ် နှစ်မျိုးတွဲ
- Saṃkiliṭṭhattika-hetudukaṃ = ကိလေသာဖြင့် ညစ်နွမ်းခြင်း သုံးမျိုးတွဲနှင့် အမြစ် နှစ်မျိုးတွဲ
- Vitakkattika-hetudukaṃ = စတင်ကြံစည်မှု သုံးမျိုးတွဲနှင့် အမြစ် နှစ်မျိုးတွဲ
- Pītittika-hetudukaṃ = ပီတိ သုံးမျိုးတွဲနှင့် အမြစ် နှစ်မျိုးတွဲ
- Dassanenapahātabbattika-hetudukaṃ = သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ခြင်း သုံးမျိုးတွဲနှင့် အမြစ် နှစ်မျိုးတွဲ
- Dassanenapahātabbahetukattika-hetudukaṃ = သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ရမည့် အမြစ် သုံးမျိုးတွဲနှင့် အမြစ် နှစ်မျိုးတွဲ
- Ācayagāmittika-hetudukaṃ = စုပုံခြင်းဆီသို့ ဦးတည်ခြင်း သုံးမျိုးတွဲနှင့် အမြစ် နှစ်မျိုးတွဲ
- Sekkhattika-hetudukaṃ = ကျင့်ကြံဆဲသူ သုံးမျိုးတွဲနှင့် အမြစ် နှစ်မျိုးတွဲ
- Parittattika-hetudukaṃ = အကန့်အသတ် ရှိခြင်း သုံးမျိုးတွဲနှင့် အမြစ် နှစ်မျိုးတွဲ
- Parittārammaṇattika-hetudukaṃ = အကန့်အသတ် ရှိသည်ကို အာရုံပြုခြင်း သုံးမျိုးတွဲနှင့် အမြစ် နှစ်မျိုးတွဲ
- Hīnattika-hetudukaṃ = ယုတ်ညံ့ခြင်း သုံးမျိုးတွဲနှင့် အမြစ် နှစ်မျိုးတွဲ
- Micchattaniyatattika-hetudukaṃ = မှားယွင်းမှု၌ ကျိန်းသေခြင်း သုံးမျိုးတွဲနှင့် အမြစ် နှစ်မျိုးတွဲ
- Maggārammaṇattika-hetudukaṃ = မဂ်ကို အာရုံပြုခြင်း သုံးမျိုးတွဲနှင့် အမြစ် နှစ်မျိုးတွဲ
- Uppannattika-hetudukaṃ = ဖြစ်ပေါ်ပြီးခြင်း သုံးမျိုးတွဲနှင့် အမြစ် နှစ်မျိုးတွဲ
- Atītattika-hetudukaṃ = အတိတ် သုံးမျိုးတွဲနှင့် အမြစ် နှစ်မျိုးတွဲ
- Atītārammaṇattika-hetudukaṃ = အတိတ်ကို အာရုံပြုခြင်း သုံးမျိုးတွဲနှင့် အမြစ် နှစ်မျိုးတွဲ
- Ajjhattattika-hetudukaṃ = မိမိ၌ ရှိခြင်း သုံးမျိုးတွဲနှင့် အမြစ် နှစ်မျိုးတွဲ
- Ajjhattārammaṇattika-hetudukaṃ = မိမိ၌ ရှိသည်ကို အာရုံပြုခြင်း သုံးမျိုးတွဲနှင့် အမြစ် နှစ်မျိုးတွဲ
- Sanidassanasappaṭighattika-hetudukaṃ = မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိခြင်း သုံးမျိုးတွဲနှင့် အမြစ် နှစ်မျိုးတွဲ
- Kusalattika-sahetukadukaṃ = ကုသိုလ် သုံးမျိုးတွဲနှင့် အမြစ် ရှိခြင်း နှစ်မျိုးတွဲ
- Kusalattika-hetusampayuttadukaṃ = ကုသိုလ် သုံးမျိုးတွဲနှင့် အမြစ်နှင့် ယှဉ်တွဲခြင်း နှစ်မျိုးတွဲ
- Kusalattika-hetusahetukadukaṃ = ကုသိုလ် သုံးမျိုးတွဲနှင့် အမြစ် ဖြစ်ခြင်းနှင့် အမြစ် ရှိခြင်း နှစ်မျိုးတွဲ
- Kusalattika-hetuhetusampayuttadukaṃ = ကုသိုလ် သုံးမျိုးတွဲနှင့် အမြစ် ဖြစ်ခြင်းနှင့် အမြစ်နှင့် ယှဉ်တွဲခြင်း နှစ်မျိုးတွဲ
- Kusalattika-nahetusahetukadukaṃ = ကုသိုလ် သုံးမျိုးတွဲနှင့် အမြစ် မဟုတ်ခြင်းနှင့် အမြစ် ရှိခြင်း နှစ်မျိုးတွဲ
- Kusalattika-sappaccayadukaṃ = ကုသိုလ် သုံးမျိုးတွဲနှင့် အကြောင်း ရှိခြင်း နှစ်မျိုးတွဲ
- Kusalattika-saṅkhatadukaṃ = ကုသိုလ် သုံးမျိုးတွဲနှင့် ပြုပြင်ဖန်တီးထားခြင်း နှစ်မျိုးတွဲ
- Kusalattika-sanidassanadukaṃ = ကုသိုလ် သုံးမျိုးတွဲနှင့် မြင်နိုင်ခြင်း နှစ်မျိုးတွဲ
- Kusalattika-sappaṭighadukaṃ = ကုသိုလ် သုံးမျိုးတွဲနှင့် ထိခိုက်မှု ရှိခြင်း နှစ်မျိုးတွဲ
- Kusalattika-rūpīdukaṃ = ကုသိုလ် သုံးမျိုးတွဲနှင့် ရုပ် ဖြစ်ခြင်း နှစ်မျိုးတွဲ
- Kusalattika-lokiyadukaṃ = ကုသိုလ် သုံးမျိုးတွဲနှင့် လောကနှင့် သက်ဆိုင်ခြင်း နှစ်မျိုးတွဲ
- Kusalattika-kenaciviññeyyadukaṃ = ကုသိုလ် သုံးမျိုးတွဲနှင့် တစ်စုံတစ်ခုသော စိတ်ဖြင့် သိနိုင်ခြင်း နှစ်မျိုးတွဲ
- Kusalattika-āsavadukaṃ = ကုသိုလ် သုံးမျိုးတွဲနှင့် စိတ်အစွန်းအထင်း နှစ်မျိုးတွဲ
- Kusalattika-sāsavadukaṃ = ကုသိုလ် သုံးမျိုးတွဲနှင့် စိတ်အစွန်းအထင်း၏ အာရုံ ဖြစ်နိုင်ခြင်း နှစ်မျိုးတွဲ
- Kusalattika-āsavasampayuttadukaṃ = ကုသိုလ် သုံးမျိုးတွဲနှင့် စိတ်အစွန်းအထင်းနှင့် ယှဉ်တွဲခြင်း နှစ်မျိုးတွဲ
- Kusalattika-āsavasāsavadukaṃ = ကုသိုလ် သုံးမျိုးတွဲနှင့် စိတ်အစွန်းအထင်း ဖြစ်ခြင်းနှင့် စိတ်အစွန်းအထင်း၏ အာရုံ ဖြစ်နိုင်ခြင်း နှစ်မျိုးတွဲ
- Kusalattika-āsavaāsavasampayuttadukaṃ = ကုသိုလ် သုံးမျိုးတွဲနှင့် စိတ်အစွန်းအထင်း ဖြစ်ခြင်းနှင့် စိတ်အစွန်းအထင်းနှင့် ယှဉ်တွဲခြင်း နှစ်မျိုးတွဲ
- Kusalattika-āsavavippayuttasāsavadukaṃ = ကုသိုလ် သုံးမျိုးတွဲနှင့် စိတ်အစွန်းအထင်းနှင့် ကင်းကွာခြင်းနှင့် စိတ်အစွန်းအထင်း၏ အာရုံ ဖြစ်နိုင်ခြင်း နှစ်မျိုးတွဲ
- Kusalattika-sārammaṇadukaṃ = ကုသိုလ် သုံးမျိုးတွဲနှင့် အာရုံ ရှိခြင်း နှစ်မျိုးတွဲ
- Kusalattika-cittadukaṃ = ကုသိုလ် သုံးမျိုးတွဲနှင့် စိတ် ဖြစ်ခြင်း နှစ်မျိုးတွဲ
- Kusalattika-cetasikadukaṃ = ကုသိုလ် သုံးမျိုးတွဲနှင့် စိတ်၏ အဖော် ဖြစ်ခြင်း နှစ်မျိုးတွဲ
- Kusalattika-ajjhattikadukaṃ = ကုသိုလ် သုံးမျိုးတွဲနှင့် အတွင်းပိုင်း ဖြစ်ခြင်း နှစ်မျိုးတွဲ
- Kusalattika-upādādukaṃ = ကုသိုလ် သုံးမျိုးတွဲနှင့် မူလဓာတ်ကြီးများကို မှီ၍ ဖြစ်ခြင်း နှစ်မျိုးတွဲ
- Kusalattika-upādinnadukaṃ = ကုသိုလ် သုံးမျိုးတွဲနှင့် ကံကြောင့် ဖြစ်ခြင်း နှစ်မျိုးတွဲ
- Kusalattika-kilesadukaṃ = ကုသိုလ် သုံးမျိုးတွဲနှင့် ကိလေသာ နှစ်မျိုးတွဲ
- Kusalattika-saṃkilesikadukaṃ = ကုသိုလ် သုံးမျိုးတွဲနှင့် ကိလေသာ၏ အာရုံ ဖြစ်နိုင်ခြင်း နှစ်မျိုးတွဲ
- Kusalattika-saṃkiliṭṭhadukaṃ = ကုသိုလ် သုံးမျိုးတွဲနှင့် ကိလေသာဖြင့် ညစ်နွမ်းခြင်း နှစ်မျိုးတွဲ
- Kusalattika-kilesasampayuttadukaṃ = ကုသိုလ် သုံးမျိုးတွဲနှင့် ကိလေသာနှင့် ယှဉ်တွဲခြင်း နှစ်မျိုးတွဲ
- Kusalattika-kilesasaṃkilesikadukaṃ = ကုသိုလ် သုံးမျိုးတွဲနှင့် ကိလေသာ ဖြစ်ခြင်းနှင့် ကိလေသာ၏ အာရုံ ဖြစ်နိုင်ခြင်း နှစ်မျိုးတွဲ
- Kusalattika-kilesasaṃkiliṭṭhadukaṃ = ကုသိုလ် သုံးမျိုးတွဲနှင့် ကိလေသာ ဖြစ်ခြင်းနှင့် ကိလေသာဖြင့် ညစ်နွမ်းခြင်း နှစ်မျိုးတွဲ
- Kusalattika-kilesakilesasampayuttadukaṃ = ကုသိုလ် သုံးမျိုးတွဲနှင့် ကိလေသာ ဖြစ်ခြင်းနှင့် ကိလေသာနှင့် ယှဉ်တွဲခြင်း နှစ်မျိုးတွဲ
- Kusalattika-kilesavippayuttasaṃkilesikadukaṃ = ကုသိုလ် သုံးမျိုးတွဲနှင့် ကိလေသာနှင့် ကင်းကွာခြင်းနှင့် ကိလေသာ၏ အာရုံ ဖြစ်နိုင်ခြင်း နှစ်မျိုးတွဲ
- Kusalattika-dassanenapahātabbadukaṃ = ကုသိုလ် သုံးမျိုးတွဲနှင့် သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ခြင်း နှစ်မျိုးတွဲ
- Kusalattika-bhāvanāyapahātabbadukaṃ = ကုသိုလ် သုံးမျိုးတွဲနှင့် ဘာဝနာ ပွားများခြင်းဖြင့် ပယ်ခြင်း နှစ်မျိုးတွဲ
- Kusalattika-dassanenapahātabbahetukadukaṃ = ကုသိုလ် သုံးမျိုးတွဲနှင့် သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ရမည့် အမြစ် နှစ်မျိုးတွဲ
- Kusalattika-bhāvanāyapahātabbahetukadukaṃ = ကုသိုလ် သုံးမျိုးတွဲနှင့် ဘာဝနာ ပွားများခြင်းဖြင့် ပယ်ရမည့် အမြစ် နှစ်မျိုးတွဲ
- Kusalattika-savitakkadukaṃ = ကုသိုလ် သုံးမျိုးတွဲနှင့် စတင်ကြံစည်မှု ရှိခြင်း နှစ်မျိုးတွဲ
- Kusalattika-savicāradukaṃ = ကုသိုလ် သုံးမျိုးတွဲနှင့် ဆက်လက်သုံးသပ်မှု ရှိခြင်း နှစ်မျိုးတွဲ
- Kusalattika-sappītikadukaṃ = ကုသိုလ် သုံးမျိုးတွဲနှင့် ပီတိ ရှိခြင်း နှစ်မျိုးတွဲ
- Kusalattika-kāmāvacaradukaṃ = ကုသိုလ် သုံးမျိုးတွဲနှင့် ကာမဘုံနှင့် ဆိုင်ခြင်း နှစ်မျိုးတွဲ
- Kusalattika-rūpāvacaradukaṃ = ကုသိုလ် သုံးမျိုးတွဲနှင့် သိမ်မွေ့သော ရုပ်ဘုံနှင့် ဆိုင်ခြင်း နှစ်မျိုးတွဲ
- Kusalattika-arūpāvacaradukaṃ = ကုသိုလ် သုံးမျိုးတွဲနှင့် ရုပ်မရှိသော ဘုံနှင့် ဆိုင်ခြင်း နှစ်မျိုးတွဲ
- Kusalattika-pariyāpannadukaṃ = ကုသိုလ် သုံးမျိုးတွဲနှင့် ဘဝဘုံတို့၌ အကျုံးဝင်ခြင်း နှစ်မျိုးတွဲ
- Kusalattika-niyyānikadukaṃ = ကုသိုလ် သုံးမျိုးတွဲနှင့် လွတ်မြောက်ရာသို့ ပို့ဆောင်ခြင်း နှစ်မျိုးတွဲ
- Kusalattika-niyatadukaṃ = ကုသိုလ် သုံးမျိုးတွဲနှင့် ကျိန်းသေခြင်း နှစ်မျိုးတွဲ
- Kusalattika-sauttaradukaṃ = ကုသိုလ် သုံးမျိုးတွဲနှင့် ထိုထက် သာလွန်သည် ရှိခြင်း နှစ်မျိုးတွဲ
- Kusalattika-saraṇadukaṃ = ကုသိုလ် သုံးမျိုးတွဲနှင့် ပဋိပက္ခ ရှိခြင်း နှစ်မျိုးတွဲ
- Vedanāttika-saraṇadukaṃ = ခံစားမှု သုံးမျိုးတွဲနှင့် ပဋိပက္ခ ရှိခြင်း နှစ်မျိုးတွဲ
- Vipākattika-saraṇadukaṃ = ကံ၏ အကျိုး သုံးမျိုးတွဲနှင့် ပဋိပက္ခ ရှိခြင်း နှစ်မျိုးတွဲ
- Upādinnattika-saraṇadukaṃ = ကံကြောင့် ဖြစ်ခြင်း သုံးမျိုးတွဲနှင့် ပဋိပက္ခ ရှိခြင်း နှစ်မျိုးတွဲ
- Saṃkiliṭṭhattika-saraṇadukaṃ = ကိလေသာဖြင့် ညစ်နွမ်းခြင်း သုံးမျိုးတွဲနှင့် ပဋိပက္ခ ရှိခြင်း နှစ်မျိုးတွဲ
- Vitakkattika-saraṇadukaṃ = စတင်ကြံစည်မှု သုံးမျိုးတွဲနှင့် ပဋိပက္ခ ရှိခြင်း နှစ်မျိုးတွဲ
- Pītittika-saraṇadukaṃ = ပီတိ သုံးမျိုးတွဲနှင့် ပဋိပက္ခ ရှိခြင်း နှစ်မျိုးတွဲ
- Dassanattika-saraṇadukaṃ = သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ခြင်း သုံးမျိုးတွဲနှင့် ပဋိပက္ခ ရှိခြင်း နှစ်မျိုးတွဲ
- Dassanahetuttika-saraṇadukaṃ = သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ရမည့် အမြစ် သုံးမျိုးတွဲနှင့် ပဋိပက္ခ ရှိခြင်း နှစ်မျိုးတွဲ
- Ācayagāmittika-saraṇadukaṃ = စုပုံခြင်းဆီသို့ ဦးတည်ခြင်း သုံးမျိုးတွဲနှင့် ပဋိပက္ခ ရှိခြင်း နှစ်မျိုးတွဲ
- Sekkhattika-saraṇadukaṃ = ကျင့်ကြံဆဲသူ သုံးမျိုးတွဲနှင့် ပဋိပက္ခ ရှိခြင်း နှစ်မျိုးတွဲ
- Parittattika-saraṇadukaṃ = အကန့်အသတ် ရှိခြင်း သုံးမျိုးတွဲနှင့် ပဋိပက္ခ ရှိခြင်း နှစ်မျိုးတွဲ
- Parittārammaṇattika-saraṇadukaṃ = အကန့်အသတ် ရှိသည်ကို အာရုံပြုခြင်း သုံးမျိုးတွဲနှင့် ပဋိပက္ခ ရှိခြင်း နှစ်မျိုးတွဲ
- Hīnattika-saraṇadukaṃ = ယုတ်ညံ့ခြင်း သုံးမျိုးတွဲနှင့် ပဋိပက္ခ ရှိခြင်း နှစ်မျိုးတွဲ
- Micchattaniyatattika-saraṇadukaṃ = မှားယွင်းမှု၌ ကျိန်းသေခြင်း သုံးမျိုးတွဲနှင့် ပဋိပက္ခ ရှိခြင်း နှစ်မျိုးတွဲ
- Maggārammaṇattika-saraṇadukaṃ = မဂ်ကို အာရုံပြုခြင်း သုံးမျိုးတွဲနှင့် ပဋိပက္ခ ရှိခြင်း နှစ်မျိုးတွဲ
- Uppannattika-saraṇadukaṃ = ဖြစ်ပေါ်ပြီးခြင်း သုံးမျိုးတွဲနှင့် ပဋိပက္ခ ရှိခြင်း နှစ်မျိုးတွဲ
- Atītattika-saraṇadukaṃ = အတိတ် သုံးမျိုးတွဲနှင့် ပဋိပက္ခ ရှိခြင်း နှစ်မျိုးတွဲ
- Atītārammaṇattika-saraṇadukaṃ = အတိတ်ကို အာရုံပြုခြင်း သုံးမျိုးတွဲနှင့် ပဋိပက္ခ ရှိခြင်း နှစ်မျိုးတွဲ
- Ajjhattattika-saraṇadukaṃ = မိမိ၌ ရှိခြင်း သုံးမျိုးတွဲနှင့် ပဋိပက္ခ ရှိခြင်း နှစ်မျိုးတွဲ
- Ajjhattārammaṇattika-saraṇadukaṃ = မိမိ၌ ရှိသည်ကို အာရုံပြုခြင်း သုံးမျိုးတွဲနှင့် ပဋိပက္ခ ရှိခြင်း နှစ်မျိုးတွဲ
- Sanidassanattika-saraṇadukaṃ = မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိခြင်း သုံးမျိုးတွဲနှင့် ပဋိပက္ခ ရှိခြင်း နှစ်မျိုးတွဲ

## Source slips (translated as the usual form or as written; logged, Pāli untouched)
- 4-15 «upekkhāsahagato nahetudhammo» (glued): read «nahetu dhammo».
- 4-15 ^7-49-141 «paṭiccavārasadisaṃ vitthārebbaṃ»: read «vitthāretabbaṃ».
- 4-15 «adhipatiyā pañca…pe. … avigate tīṇi»: read «…pe…»; the Burmese keeps the Pāli's two «…» («ငါးခု… … »).
- 4-15 heading «*Hetuārammaṇapaccayādi*» (no hyphen; Y's slip fix) and «*Hetuārammaṇapaccayā*», 4-18
  «*Hetusahajātapaccayādi*»: the conditions as named.
- 4-15 / 4-16 «*Paccanīyaṃ –nahetupaccayo*», «*Paccanīyaṃ –naadhipatipaccayo*» (no space after the dash): the module's
  «Paccanīyaṃ – X» heading (one «–», same spot).
- 4-15 part numbers «11-1.» twice (Sekkha and Paritta), 4-21 «11 -100.», «13 -100.», «14 -100.» (space): kept as
  written.
- 4-16 ^7-50-48 «nakenaci viññeyya» for «kenaci naviññeyya»: translated as written (the na-X rule of 5-01 … 5-04).
- 4-17 «āmammaṇe»: read «ārammaṇe».
- 4-21 short triad headings «Dassanattika», «Dassanahetuttika», «Sanidassanattika»: the full triads' terms and names.

## Readings (logged)
- 4-17: under the heading 1-18 (āsava + āsavasampayutta) the Pāli also has the first term of the 1-19 dyad
  («āsavavippayuttaṃ sāsavaṃ»); both dyads are active in that part (the 1-19 heading then has the other term).
- 4-15 ^7-49-79 «(Yathā sahajātavārampi… sampayuttavārampi evaṃ vitthāretabbaṃ.)»: the vāras as the model of the
  comparison («…တို့ကဲ့သို့ ထိုနည်းတူ»); their «-pi» is not rendered apart.
- 4-17 ^7-51-34 «… akusalaṃ ganthaṃ… oghaṃ… yogaṃ… nīvaraṇaṃ….»: the cluster terms as written (the first dyad term of
  each cluster; «oghaṃ …» without the triad word and without the noun).
- «Diṭṭhiṃ paṭicca diṭṭhi na uppajjati.» = «အယူကို မှီ၍ အယူသည် မဖြစ်ပေါ်။» (diṭṭhi the module's «အယူ»; nuppajjati pi-6).
- «Kusalattike cha gocchakaṃ niṭṭhitaṃ.» = «“ကုသိုလ် သုံးမျိုးတွဲ၌ အစု ခြောက်ခု” ပြီးဆုံးပြီ။».

## Unsure
- The 4-15 ^7-49-79 note (yathā without a stated model; English: «expanded in the same way as the co-arising …
  association sections»).
- «Kusalattike cha gocchakaṃ» (the six clusters in the wholesome triad) as one name.

## For the consistency pass
- 4 sentences differ from 5-01 / 5-02 (they follow the dukatika models X / Y): «…paṭiccavārasadisaṃ» «…နှင့်
  တူကြသည်» (X) vs 5-01 «…နှင့် တူသည်»; «Sahajātavārampi… pañhāvārampi evaṃ vitthāretabbaṃ» «…လည်း ထိုနည်းတူ» vs 5-02
  «…ကိုလည်း ဤသို့» (H14, H20); «Yathā kusalattike pañhāvāraṃ, evaṃ vitthāretabbaṃ» «…ကဲ့သို့» (X) vs 5-01 «…အတိုင်း».
- 5-12 has a line like 4-17 ^7-51-34 («Akusalaṃ saññojanaṃ … parāmāsaṃ»); the cluster-term rendering should agree.
- Stacked abyākata in the combined term «ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော၊ <dyad term>» (as the dukatika).

## Last check run
check_ch4-15-21.py --mutate: 0 mismatches; **14 / 14** planted errors caught (count, polarity, dyad term, triad term, condition, digits, part-name order, world-C / world-E terms, as-written term, pada heading, colophon, hand-line term).
