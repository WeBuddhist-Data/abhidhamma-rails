# pi-7 Burmese zero-shot: 4-02 … 4-09 (the first DUKATIKA chapters: a dyad combined with a triad)

Translated from the Pāli only (no Burmese translation or nissaya opened, no web search, `language-priority/` not
opened). Meaning cross-checked with the English zero-shot only (e.g. «only registration is found», «in the middle
three»). Generator `make_ch4-02-09.py`, check `check_ch4-02-09.py`, read-only helper `kwic_ch4-02-09.py` (finished
pi-7 lines with their Burmese). Scratch: `chk-ch4-02-09/`.

## Status (all pass, 2026-11-24)
| file | segments | lines | check_chapter_ids | check_text (pe-folded) | check_marks |
|---|---|---|---|---|---|
| 4-02-dukatika-hetuduka.md | 1118 | 1808 | OK | OK | OK |
| 4-03-dukatika-sahetukaduka.md | 232 | 358 | OK | OK | OK |
| 4-04-dukatika-sappaccayaduka.md | 139 | 198 | OK | OK | OK |
| 4-05-dukatika-asavaduka.md | 117 | 170 | OK | OK | OK |
| 4-06-dukatika-sannojanaduka.md | 90 | 139 | OK | OK | OK |
| 4-07-dukatika-ganthaduka.md | 69 | 116 | OK | OK | OK |
| 4-08-dukatika-nivaranaduka.md | 60 | 89 | OK | OK | OK |
| 4-09-dukatika-paramasaduka.md | 54 | 79 | OK | OK | OK |

check_ch4-02-09 (all eight): 2957 lines × S P C O N, 3157 sentences for identity, 222 table values:
**0 mismatches**. Reuse: **33 / 33** pi-1 … pi-6 values identical wherever their Pāli occurs (379 witnessed);
sentences also in pi-1 … pi-6: **184 / 184** identical; sentences shared with the finished pi-7 groups: **32 / 32**
identical. `--sample`: the approved sample (1-00, 1-02) regenerates identical through world A with this script's
extensions (raw and prepped). `--mutate`: **11 / 11** planted errors caught (count, polarity, term order, condition,
dyad term, triad term, digits, note, part name, world-B term, pada name). The text check (pi-3-mr/check_text.py on a
«…Pe…»-folded copy in `chk-pe/ch4-02-09/`, deleted afterwards) is run by `check_ch4-02-09.py --pe`.

## Method
- Two engine worlds, each loaded on its OWN copies of my7_formulas / make_sample (sys.modules isolated per load; no
  file of another group edited or run as a script):
  world A = `make_ch3-03-06.py` (→ make_ch3-01-02 → make_ch2-03-06: primary 1-01, fallback 1-03 … 1-05) for 4-02 … 4-07;
  world B = `make_ch3-07-08-10.py` (→ make_ch3-01-02 the same way) for 4-08 … 4-09.
  Value sources only (tables read, nothing of them runs on A or B): `make_ch2-07-11.py` (with make_ch2-01-02 and
  make_ch1-03-05: the triads 1-03 … 2-02, 2-07 … 2-11) and `make_ch2-12-17.py` (2-12 … 2-17).
- Each chapter is cut at its dyad-triad headings («##### 1-1 Hetuduka-kusalattikaṃ», «###### 1-2. …»). In a part a
  combined term «<dyad term> <triad term>» («hetuṃ kusalaṃ», «sāsavañceva no ca āsavaṃ akusalañca»,
  «hetu maggādhipati», «hetussa bahiddhā») is rewritten before slotting into ONE synthetic a-stem term (ending of the
  triad word; -in / -i triad stems mapped ī/i→o, iṃ→aṃ, issa→assa, iñca→añca; the indeclinable «bahiddhā» takes the
  ending of the dyad word). Its Burmese = the two qualifiers stacked «<dyad term>၊ <triad term>» (coordinator: the
  stacking pattern «A၊ B N» of 2-01-02 / 2-07-11 / 3-01-02), e.g.
  hetu kusalo dhammo = အမြစ် ဖြစ်သော၊ ကုသိုလ် သဘောတရား. Only the part's term table is active (dyads and other
  triads off), so the dyad chapters' frames apply unchanged (coordination «A Nနှင့် B N», pañhā, counts …).
- Dyad terms: the finished 3-01 … 3-08 tables (world A M3.DYADS / 3-03-06 DYADS; world B DYADS_ADD), the sixth-dyad
  forms as in 3-03-06 / 3-07-08-10. Triad terms: the finished 1-01 … 2-17 tables. Both go back to the pi-1 final
  Mātikā. Dyad names: the finished DUKA_NAME; triad names: the finished TIKA_NAME; cluster names: 3-03-06 GNAME,
  3-07-08-10 GOCCHAKA.
- «-dhammadhamma» triad terms hold their noun: «hetu vipākadhammadhammo uppajjati» gets the noun after the synthetic
  term (as make_ch1-03-05 splits «vipākadhamma dhammo»); «A-añca B-añca paṭicca» (no separate noun) gets «dhammaṃ»,
  «A-o ca B-o ca nahetussa …» gets «dhammā» (the frame's noun; the noun is inside the compounds, not supplied).
- Notes the engine has no entry for are rendered whole by this script's note renderer (one placeholder per note, the
  sentences inside joined) from the finished groups' words; notes the engine knows stay the engine's.
- A bare locative (or a run of them) ending a counting fragment before «…» («kamme…pe… magge cattāri»,
  «nakamme navipāke…pe… namagge ekaṃ»): the condition in the locative alone, a run joined by «၊» (as 2-03-06 runs);
  installed as a wrapper on the module's chain() in both worlds (the sample still regenerates identical).
- Coordinator decisions applied: «(Anulomaṃ).» = «(အဟုတ်ပြ ပုံစံ)။» (the order); «sahajātakammameva» names a kind
  of kamma = «အတူ ပေါ်ပေါက်သည့် ကံသာ»; the sixth-dyad forms as 3-03-06. asaññasattānaṃ, the heinous deeds and the
  «Sahajātā –» label do not occur in these chapters. No word supplied except where logged below.

## New recurring terms, names and frames (Pāli = Burmese)
Dhammānulome dukatikapaṭṭhānaṃ = သဘောတရား အဟုတ်ပြ ပုံစံ၌ နှစ်မျိုးတွဲနှင့် သုံးမျိုးတွဲတို့၏ အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ (sample «Dukaṃ tikañca» = နှစ်မျိုးတွဲနှင့် သုံးမျိုးတွဲ)
N-M. Xduka-Yttikaṃ = N-M. <X dyad name>နှင့် <Y triad name> (e.g. 1-2. Hetuduka-vedanāttikaṃ = 1-2. အမြစ် နှစ်မျိုးတွဲနှင့် ခံစားမှု သုံးမျိုးတွဲ)
XdukaYttikaṃ niṭṭhitaṃ. = “<X dyad name>နှင့် <Y triad name>” ပြီးဆုံးပြီ။
XgocchakaYttikaṃ niṭṭhitaṃ. = “<X cluster name>နှင့် <Y triad name>” ပြီးဆုံးပြီ။ (e.g. Saññojanagocchakakusalattikaṃ = နှောင်ကြိုးတို့၏ အစုနှင့် ကုသိုလ် သုံးမျိုးတွဲ)
<triad term>padaṃ = <triad term> ပုဒ် (the 1-01 «Kusalapadaṃ» = ကုသိုလ် ပုဒ် pattern; e.g. Sukhāyavedanāyasampayuttapadaṃ = သာယာသော ခံစားမှုနှင့် ယှဉ်တွဲသော ပုဒ်, Bahiddhāpadaṃ = မိမိ၏ ပြင်ပ၌ ရှိသော ပုဒ်)
1-2. Kusalākusalapadaṃ = 1-2. ကုသိုလ်နှင့် အကုသိုလ် ပုဒ် (module heading)
<dyad term> <triad term> dhammo = <dyad term>၊ <triad term> သဘောတရား (all combinations: `make_ch4-02-09.py --dump`)
*Paccayacatukkaṃ* = *အကြောင်း လေးမျိုးတွဲ* (= 1-03 … 1-05 «1-4. Paccayacatukkaṃ»)
1-6. Paṭiccavārādi = 1-6. မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက် စသည် (= 3-03 … 3-08 «1-7. …»; also «Paṭiccavārādi», «*1-7. Paṭiccavārādi*»)
*Hetu-ārammaṇapaccayādi* = *အမြစ်ဟူသော အကြောင်းနှင့် အာရုံဟူသော အကြောင်း စသည်*
*Nahetu-naārammaṇapaccayādi* = *အမြစ်ဟူသော အကြောင်း မဟုတ်ခြင်းနှင့် အာရုံဟူသော အကြောင်း မဟုတ်ခြင်း စသည်*
vāra lists in notes: Xvāropi / Xvārampi = Xလည်း (nominative, as 1-05 «… vitthāretabbo»); Xvārepi = X၌လည်း (as 3-02 «Saṃsaṭṭhavārepi sabbattha ekaṃ»); items joined by «၊», none next to «…»
… vitthāretabbā / -o / -aṃ = … အကျယ် ချဲ့ရမည်
… sabbattha vitthāretabbo / -ā / -aṃ = … နေရာတိုင်း၌ အကျယ် ချဲ့ရမည်
… paṭiccavārasadisā / -aṃ = … မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူကြသည် (3-01-02)
X-sadisā vitthāretabbā = Xနှင့် တူအောင် အကျယ် ချဲ့ရမည် (NEW «နှင့် တူအောင်»; 3-01-02 «… နှင့် တူအောင် ပြုရမည်»)
sabbattha sadisā = နေရာတိုင်း၌ တူကြသည်
(… -vārepi) sabbattha N = … နေရာတိုင်း၌ N
(saṃkhittaṃ, anulomaṃ / paccanīyaṃ / anulomapaccanīyaṃ / paccanīyānulomaṃ) = (အကျဉ်းချုပ်၊ <order>)
(paccanīyaṃ) / (Anulomaṃ) = (<order>) (= 3-09 / 4-01); Paccanīyaṃ. (inside a note) = အငြင်းပြ ပုံစံ။
Yathā kusalattike pañhāvārassa anulomampi paccanīyampi anulomapaccanīyampi paccanīyānulomampi gaṇitaṃ, evaṃ gaṇetabbaṃ = ကုသိုလ် သုံးမျိုးတွဲ၌ ပြဿနာအလိုက် ဖော်ပြချက်၏ အဟုတ်ပြ ပုံစံကိုလည်း၊ အငြင်းပြ ပုံစံကိုလည်း၊ အဟုတ်ပြ အငြင်းပြ ပုံစံကိုလည်း၊ အငြင်းပြ အဟုတ်ပြ ပုံစံကိုလည်း ရေတွက်ထားသည့်အတိုင်း ထိုနည်းတူ ရေတွက်ရမည် (the 1-03 … 1-05 «yathā kusalattike …» frame)
imamhi dukatike = ဤ နှစ်မျိုးတွဲနှင့် သုံးမျိုးတွဲ၌
(Imamhi dukatike <vāras>pi anuppannampi uppādīpi natthi) = … <vāras>လည်း၊ မဖြစ်ပေါ်သေးသော သဘောတရားလည်း၊ ဖြစ်ပေါ်လာမည့် သဘောတရားလည်း မရှိ (a term as a noun = term + သဘောတရား, as 1-01 «abyākataṃ»; also atītampi anāgatampi)
Ajjhattabahiddhā na labbhanti = မိမိ၌နှင့် မိမိ၏ ပြင်ပ၌ ရှိသော သဘောတရားများ မတွေ့ရ (na labbhati «မတွေ့ရ», module)
Appaccayampi asaṅkhatampi sanidassanampi na labbhati = အကြောင်း မရှိသော သဘောတရားလည်း၊ ပြုပြင်ဖန်တီးထားခြင်း မရှိသော သဘောတရားလည်း၊ မြင်နိုင်သော သဘောတရားလည်း မတွေ့ရ
labbhati = တွေ့ရသည် (= 3-09)
ārammaṇādhipatiyeva = အာရုံ အကြီးအမှူးသာ (= 3-07)
tadārammaṇāyeva labbhanti = ထိုအာရုံကိုပင် အာရုံပြုသော စိတ်တို့ကိုသာ တွေ့ရသည် (tadārammaṇā «ထိုအာရုံကိုပင် အာရုံပြုသော စိတ်», after 1-03 … 1-05 tadārammaṇatā)
sahajātādhipatiyeva labbhati, ārammaṇādhipati natthi = အတူ ပေါ်ပေါက်သော အကြီးအမှူးကိုသာ တွေ့ရသည်၊ အာရုံ အကြီးအမှူး မရှိ
itare dve anantarūpanissayo pakatūpanissayoyeva = အခြား နှစ်ခုသည် ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းဖြင့် အားကြီးသော အမှီနှင့် ပကတိ အားကြီးသော အမှီသာ
sahajātakammameva = အတူ ပေါ်ပေါက်သည့် ကံသာ
sabbe paccayā kātabbā = အကြောင်း အားလုံးကို ပြုရမည် (= 4-01 «Evaṃ sabbe paccayā kātabbā» without evaṃ)
Hetupaccayo natthi = အမြစ်ဟူသော အကြောင်း မရှိ
pañhāvārepi imesaṃ tiṇṇannaṃ hetupaccayo natthi = ပြဿနာအလိုက် ဖော်ပြချက်၌လည်း ဤ သုံးခုတို့၌ အမြစ်ဟူသော အကြောင်း မရှိ (imesaṃ tiṇṇannaṃ as 1-03 … 1-05)
majjhe tiṇṇaṃ = အလယ် သုံးခု၌; majjhe tiṇṇaṃ sahajātādhipati labbhati = အလယ် သုံးခု၌ အတူ ပေါ်ပေါက်သော အကြီးအမှူးကို တွေ့ရသည်
majjhime ca ante ca ārammaṇādhipati = အလယ်၌လည်းကောင်း၊ အဆုံး၌လည်းကောင်း အာရုံ အကြီးအမှူး (majjhime «အလယ်၌» as 3-05 «majjhe»; ante «အဆုံး၌»)
lokiyalokuttara = လောကနှင့် သက်ဆိုင်ခြင်းနှင့် လောကကို ကျော်လွန်ခြင်း; lokiyalokuttaraduka = … နှစ်မျိုးတွဲ
Lokiyadukasadisaṃ / Lokiyalokuttaradukasadisaṃ = <name>နှင့် တူသည်; lokiyalokuttaragamanasadisaṃ = လောကနှင့် သက်ဆိုင်ခြင်းနှင့် လောကကို ကျော်လွန်ခြင်း၏ သွားပုံနှင့် တူသည်
Cūḷantaraduke lokiyadukasadisaṃ. = ကြားညှပ် နှစ်မျိုးတွဲ အစုငယ်၌ လောကနှင့် သက်ဆိုင်ခြင်း နှစ်မျိုးတွဲနှင့် တူသည်။
Yathā cūḷantaraduke lokiyadukasadisaṃ = ကြားညှပ် နှစ်မျိုးတွဲ အစုငယ်၌ လောကနှင့် သက်ဆိုင်ခြင်း နှစ်မျိုးတွဲနှင့် တူသည့်အတိုင်း (3-01-02 «yathā paṭiccavārasadisaṃ»)
Yathā cūḷantaraduke lokiyadukagamanaṃ, evaṃ imampi ñātabbaṃ = ကြားညှပ် နှစ်မျိုးတွဲ အစုငယ်၌ လောကနှင့် သက်ဆိုင်ခြင်း နှစ်မျိုးတွဲ၏ သွားပုံအတိုင်း ဤသည်ကိုလည်း ထိုနည်းတူ သိရမည် (imampi «ဤသည်ကိုလည်း» = the sample's idampi; ñātabbaṃ «သိရမည်» NEW)
Sappaccayasadisaṃ vitthāretabbaṃ = အကြောင်း ရှိသော သဘောတရားနှင့် တူအောင် အကျယ် ချဲ့ရမည်
Kenaci viññeyyaṃ akusalampi kenaci viññeyyaṃ abyākatampi kenaci viññeyyakusalasadisaṃ vitthāretabbaṃ = <kenaci+akusala> သဘောတရားလည်း၊ <kenaci+abyākata> သဘောတရားလည်း <kenaci+kusala> သဘောတရားနှင့် တူအောင် အကျယ် ချဲ့ရမည်
Oghagocchakampi yogagocchakampi āsavagocchakakusalattikasadisaṃ = ရေအလျဉ်တို့၏ အစုလည်း၊ ထမ်းပိုးတို့၏ အစုလည်း စိတ်အစွန်းအထင်းတို့၏ အစုနှင့် ကုသိုလ် သုံးမျိုးတွဲနှင့် တူကြသည်

## Source slips (translated as the usual form; logged, Pāli untouched)
- 4-02: «nahetu asakkho dhammo» (for asekkho, Asekkhapadaṃ); «kamma nava» (for kamme, ^7-36-390); «avigata nava»
  (for avigate, ^7-36-534); «(saṃkhittaṃ, anuloma paccanīyaṃ)» (written apart); «paccanīyānulomampi naṇitaṃ» (14×, for
  gaṇitaṃ); heading «*Nahetunaārammaṇapaccayādi*» (no hyphen); «gaṇitaṃ evaṃ» without comma (no effect: no «၊» there);
  «vippayutte nava atthiyā nava» without comma (^7-36-109: Burmese without «၊» there too, as written).
- 4-03: «saṃsaṭṭhavāro» without «-pi» in the vāra list (^7-37-66; read with it: the list's form).
- 4-05: «Āsavo ceva sāsavoca» (fused «ca»).
- 4-06 / 4-07 / 4-08 / 4-09: «Saññojanañceva saññojanasampayuttaṃ», «Ganthañceva ganthaniyaṃ», «Nīvaraṇañceva
  nīvaraṇiyaṃ», «Parāmāsañceva parāmaṭṭhaṃ» (+ triad «akusalañca») without the closing «ca» of the second member
  (read with it).
- 4-08: «nīvaraṇo ca nīvaraṇiyo ca akusalo» for «nīvaraṇo ceva nīvaraṇiyo ca» (^7-42-25).
- 4-04: two headings numbered «11-1.» (Rūpīduka- and Lokiyaduka-kusalattikaṃ): kept as written.

## Readings (logged)
- 4-08 ^7-42-5: «Nīvaraṇañca nonīvaraṇañca akusalaṃ dhammaṃ» (one triad word shared by the two dyad terms) read as the
  two combined terms «Nīvaraṇaṃ akusalañca nonīvaraṇaṃ akusalañca dhammaṃ» = «အတားအဆီး ဖြစ်သော၊ အကုသိုလ်
  သဘောတရားနှင့် အတားအဆီး မဟုတ်သော၊ အကုသိုလ် သဘောတရား» (a stack «A၊ B၊ C» would say one phenomenon is both).
- «-dhammadhamma» terms: the noun inside the compound placed after the term (see Method); not a supplied word.

## Unsure
- «(tadārammaṇāyeva labbhanti)» = «only registration minds are found» (English zero-shot: "only registration is
  found"); rendered «ထိုအာရုံကိုပင် အာရုံပြုသော စိတ်တို့ကိုသာ တွေ့ရသည်».
- «Sappaccayasadisaṃ» read as «like the sappaccaya [term]» (term as a noun), not the dyad's name.
- «(majjhe tiṇṇaṃ sahajātādhipati labbhati)», «(majjhime ca ante ca ārammaṇādhipati)»: positions in the count,
  rendered literally.
- The spacing «nava …āsevana-» (^7-36-131): the engine gives «ကိုးခု…အလေ့အကျင့်» (no space before «…»; the «…» count
  is right; check_text passes).

## For the consistency pass
- Vāra lists before «vitthāretabba»: nominative «Xလည်း …» (1-05 lineage) is used here; 2-15 and 3-01-02 («evaṃ …»)
  have «Xကိုလည်း …».
- labbhati «တွေ့ရသည်» (3-09) vs 4-01 «ရသည်» (in progress).
- Shared-count runs keep the engine's pattern (no «၊» before the last locative + count; H13).

## Full list of the new strings of this run (generated by `make_ch4-02-09.py --new`)
X-sadisā vitthāretabbā (like X, to be expanded) = နှင့် တူအောင်
yathā … X-sadisaṃ = နှင့် တူသည့်အတိုင်း
lokiyalokuttara (the lokiya dyad named by both terms) = လောကနှင့် သက်ဆိုင်ခြင်းနှင့် လောကကို ကျော်လွန်ခြင်း
lokiyalokuttaraduka = လောကနှင့် သက်ဆိုင်ခြင်းနှင့် လောကကို ကျော်လွန်ခြင်း နှစ်မျိုးတွဲ
imamhi dukatike = ဤ နှစ်မျိုးတွဲနှင့် သုံးမျိုးတွဲ၌
labbhati = တွေ့ရသည်
majjhe tiṇṇaṃ = အလယ် သုံးခု၌
majjhime (in the middle) = အလယ်၌
ante (at the end) = အဆုံး၌
imampi = ဤသည်ကိုလည်း
ñātabbaṃ = သိရမည်
tadārammaṇā (the minds) = ထိုအာရုံကိုပင် အာရုံပြုသော စိတ်
sabbattha sadisā (alike everywhere) = တူကြသည်
Cūḷantaraduke lokiyadukasadisaṃ. = ကြားညှပ် နှစ်မျိုးတွဲ အစုငယ်၌ လောကနှင့် သက်ဆိုင်ခြင်း နှစ်မျိုးတွဲနှင့် တူသည်။
Dhammānulome dukatikapaṭṭhānaṃ = သဘောတရား အဟုတ်ပြ ပုံစံ၌ နှစ်မျိုးတွဲနှင့် သုံးမျိုးတွဲတို့၏ အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ
Paccayacatukkaṃ = *အကြောင်း လေးမျိုးတွဲ*
*Hetu-ārammaṇapaccayādi* = *အမြစ်ဟူသော အကြောင်းနှင့် အာရုံဟူသော အကြောင်း စသည်*
*Nahetu-naārammaṇapaccayādi* = *အမြစ်ဟူသော အကြောင်း မဟုတ်ခြင်းနှင့် အာရုံဟူသော အကြောင်း မဟုတ်ခြင်း စသည်*
Hetuduka-kusalattikaṃ = အမြစ် နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
Hetuduka-vedanāttikaṃ = အမြစ် နှစ်မျိုးတွဲနှင့် ခံစားမှု သုံးမျိုးတွဲ
Hetuduka-vipākattikaṃ = အမြစ် နှစ်မျိုးတွဲနှင့် ကံ၏ အကျိုး သုံးမျိုးတွဲ
Hetuduka-upādinnattikaṃ = အမြစ် နှစ်မျိုးတွဲနှင့် ကံကြောင့် ဖြစ်ခြင်း သုံးမျိုးတွဲ
Hetuduka-saṃkiliṭṭhattikaṃ = အမြစ် နှစ်မျိုးတွဲနှင့် ကိလေသာဖြင့် ညစ်နွမ်းခြင်း သုံးမျိုးတွဲ
Hetuduka-vitakkattikaṃ = အမြစ် နှစ်မျိုးတွဲနှင့် စတင်ကြံစည်မှု သုံးမျိုးတွဲ
Hetuduka-pītittikaṃ = အမြစ် နှစ်မျိုးတွဲနှင့် ပီတိ သုံးမျိုးတွဲ
Hetuduka-dassanenapahātabbattikaṃ = အမြစ် နှစ်မျိုးတွဲနှင့် သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ခြင်း သုံးမျိုးတွဲ
Hetuduka-dassanenapahātabbahetukattikaṃ = အမြစ် နှစ်မျိုးတွဲနှင့် သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ရမည့် အမြစ် သုံးမျိုးတွဲ
Hetuduka-ācayagāmittikaṃ = အမြစ် နှစ်မျိုးတွဲနှင့် စုပုံခြင်းဆီသို့ ဦးတည်ခြင်း သုံးမျိုးတွဲ
Hetuduka-sekkhattikaṃ = အမြစ် နှစ်မျိုးတွဲနှင့် ကျင့်ကြံဆဲသူ သုံးမျိုးတွဲ
Hetuduka-parittattikaṃ = အမြစ် နှစ်မျိုးတွဲနှင့် အကန့်အသတ် ရှိခြင်း သုံးမျိုးတွဲ
Hetuduka-parittārammaṇattikaṃ = အမြစ် နှစ်မျိုးတွဲနှင့် အကန့်အသတ် ရှိသည်ကို အာရုံပြုခြင်း သုံးမျိုးတွဲ
Hetuduka-hīnattikaṃ = အမြစ် နှစ်မျိုးတွဲနှင့် ယုတ်ညံ့ခြင်း သုံးမျိုးတွဲ
Hetuduka-micchattaniyatattikaṃ = အမြစ် နှစ်မျိုးတွဲနှင့် မှားယွင်းမှု၌ ကျိန်းသေခြင်း သုံးမျိုးတွဲ
Hetuduka-maggārammaṇattikaṃ = အမြစ် နှစ်မျိုးတွဲနှင့် မဂ်ကို အာရုံပြုခြင်း သုံးမျိုးတွဲ
Hetuduka-uppannattikaṃ = အမြစ် နှစ်မျိုးတွဲနှင့် ဖြစ်ပေါ်ပြီးခြင်း သုံးမျိုးတွဲ
Hetuduka-atītattikaṃ = အမြစ် နှစ်မျိုးတွဲနှင့် အတိတ် သုံးမျိုးတွဲ
Hetuduka-atītārammaṇattikaṃ = အမြစ် နှစ်မျိုးတွဲနှင့် အတိတ်ကို အာရုံပြုခြင်း သုံးမျိုးတွဲ
Hetuduka-ajjhattattikaṃ = အမြစ် နှစ်မျိုးတွဲနှင့် မိမိ၌ ရှိခြင်း သုံးမျိုးတွဲ
Hetuduka-ajjhattārammaṇattikaṃ = အမြစ် နှစ်မျိုးတွဲနှင့် မိမိ၌ ရှိသည်ကို အာရုံပြုခြင်း သုံးမျိုးတွဲ
Hetuduka-sanidassanasappaṭighattikaṃ = အမြစ် နှစ်မျိုးတွဲနှင့် မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိခြင်း သုံးမျိုးတွဲ
(anulomaṃ) = (အဟုတ်ပြ ပုံစံ)
(paccanīyaṃ) = (အငြင်းပြ ပုံစံ)
(saṃkhittaṃ, anulomapaccanīyaṃ) = (အကျဉ်းချုပ်၊ အဟုတ်ပြ အငြင်းပြ ပုံစံ)
(saṃkhittaṃ, paccanīyānulomaṃ) = (အကျဉ်းချုပ်၊ အငြင်းပြ အဟုတ်ပြ ပုံစံ)
(Sahajātavārampi paccayavārampi nissayavārampi saṃsaṭṭhavārampi sampayuttavārampi paṭiccavārasadisā vitthāretabbā.) = (အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း၊ အကြောင်းပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်လည်း၊ အမှီပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်လည်း၊ ရောနှောခြင်းအလိုက် ဖော်ပြချက်လည်း၊ ယှဉ်တွဲခြင်းအလိုက် ဖော်ပြချက်လည်း မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူအောင် အကျယ် ချဲ့ရမည်။)
(saṃkhittaṃ, paccanīyaṃ) = (အကျဉ်းချုပ်၊ အငြင်းပြ ပုံစံ)
(Yathā kusalattike pañhāvārassa anulomampi paccanīyampi anulomapaccanīyampi paccanīyānulomampi gaṇitaṃ, evaṃ gaṇetabbaṃ.) = (ကုသိုလ် သုံးမျိုးတွဲ၌ ပြဿနာအလိုက် ဖော်ပြချက်၏ အဟုတ်ပြ ပုံစံကိုလည်း၊ အငြင်းပြ ပုံစံကိုလည်း၊ အဟုတ်ပြ အငြင်းပြ ပုံစံကိုလည်း၊ အငြင်းပြ အဟုတ်ပြ ပုံစံကိုလည်း ရေတွက်ထားသည့်အတိုင်း ထိုနည်းတူ ရေတွက်ရမည်။)
(saṃkhittaṃ, anulomaṃ) = (အကျဉ်းချုပ်၊ အဟုတ်ပြ ပုံစံ)
(Sahajātavāropi paccayavāropi nissayavāropi saṃsaṭṭhavāropi sampayuttavāropi paṭiccavārasadisā vitthāretabbā.) = (အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း၊ အကြောင်းပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်လည်း၊ အမှီပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်လည်း၊ ရောနှောခြင်းအလိုက် ဖော်ပြချက်လည်း၊ ယှဉ်တွဲခြင်းအလိုက် ဖော်ပြချက်လည်း မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူအောင် အကျယ် ချဲ့ရမည်။)
(ārammaṇādhipatiyeva) = (အာရုံ အကြီးအမှူးသာ)
(Anulomaṃ) = (အဟုတ်ပြ ပုံစံ)
(tadārammaṇāyeva labbhanti) = (ထိုအာရုံကိုပင် အာရုံပြုသော စိတ်တို့ကိုသာ တွေ့ရသည်)
(sahajātādhipatiyeva labbhati, ārammaṇādhipati natthi) = (အတူ ပေါ်ပေါက်သော အကြီးအမှူးကိုသာ တွေ့ရသည်၊ အာရုံ အကြီးအမှူး မရှိ)
(itare dve anantarūpanissayo pakatūpanissayoyeva) = (အခြား နှစ်ခုသည် ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းဖြင့် အားကြီးသော အမှီနှင့် ပကတိ အားကြီးသော အမှီသာ)
(sahajātakammameva, saṃkhittaṃ) = (အတူ ပေါ်ပေါက်သည့် ကံသာ၊ အကျဉ်းချုပ်)
(Yathā kusalattike pañhāvārassa anulomampi paccanīyampi anulomapaccanīyampi paccanīyānulomampi gaṇitaṃ evaṃ gaṇetabbaṃ.) = (ကုသိုလ် သုံးမျိုးတွဲ၌ ပြဿနာအလိုက် ဖော်ပြချက်၏ အဟုတ်ပြ ပုံစံကိုလည်း၊ အငြင်းပြ ပုံစံကိုလည်း၊ အဟုတ်ပြ အငြင်းပြ ပုံစံကိုလည်း၊ အငြင်းပြ အဟုတ်ပြ ပုံစံကိုလည်း ရေတွက်ထားသည့်အတိုင်း ထိုနည်းတူ ရေတွက်ရမည်။)
(Yathā kusalattike pañhāvārassa anulomampi paccanīyampi anulomapaccanīyampi paccanīyānulomampi gaṇitaṃ, evaṃ gaṇetabbaṃ. Imamhi dukatike paṭiccavārampi sahajātavārampi paccayavārampi nissayavārampi saṃsaṭṭhavārampi sampayuttavārampi anuppannampi uppādīpi natthi.) = (ကုသိုလ် သုံးမျိုးတွဲ၌ ပြဿနာအလိုက် ဖော်ပြချက်၏ အဟုတ်ပြ ပုံစံကိုလည်း၊ အငြင်းပြ ပုံစံကိုလည်း၊ အဟုတ်ပြ အငြင်းပြ ပုံစံကိုလည်း၊ အငြင်းပြ အဟုတ်ပြ ပုံစံကိုလည်း ရေတွက်ထားသည့်အတိုင်း ထိုနည်းတူ ရေတွက်ရမည်။ ဤ နှစ်မျိုးတွဲနှင့် သုံးမျိုးတွဲ၌ မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်လည်း၊ အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း၊ အကြောင်းပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်လည်း၊ အမှီပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်လည်း၊ ရောနှောခြင်းအလိုက် ဖော်ပြချက်လည်း၊ ယှဉ်တွဲခြင်းအလိုက် ဖော်ပြချက်လည်း၊ မဖြစ်ပေါ်သေးသော သဘောတရားလည်း၊ ဖြစ်ပေါ်လာမည့် သဘောတရားလည်း မရှိ။)
(Yathā kusalattike pañhāvārassa anulomampi paccanīyampi anulomapaccanīyampi paccanīyānulomampi gaṇitaṃ, evaṃ gaṇetabbaṃ. Imamhi dukatike paṭiccavārampi sahajātavārampi paccayavārampi nissayavārampi saṃsaṭṭhavārampi sampayuttavārampi atītampi anāgatampi natthi.) = (ကုသိုလ် သုံးမျိုးတွဲ၌ ပြဿနာအလိုက် ဖော်ပြချက်၏ အဟုတ်ပြ ပုံစံကိုလည်း၊ အငြင်းပြ ပုံစံကိုလည်း၊ အဟုတ်ပြ အငြင်းပြ ပုံစံကိုလည်း၊ အငြင်းပြ အဟုတ်ပြ ပုံစံကိုလည်း ရေတွက်ထားသည့်အတိုင်း ထိုနည်းတူ ရေတွက်ရမည်။ ဤ နှစ်မျိုးတွဲနှင့် သုံးမျိုးတွဲ၌ မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်လည်း၊ အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း၊ အကြောင်းပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်လည်း၊ အမှီပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်လည်း၊ ရောနှောခြင်းအလိုက် ဖော်ပြချက်လည်း၊ ယှဉ်တွဲခြင်းအလိုက် ဖော်ပြချက်လည်း၊ အတိတ် သဘောတရားလည်း၊ အနာဂတ် သဘောတရားလည်း မရှိ။)
(Yathā kusalattike pañhāvārassa anulomampi paccanīyampi anulomapaccanīyampi paccanīyānulomampi gaṇitaṃ, evaṃ gaṇetabbaṃ. Ajjhattabahiddhā na labbhanti.) = (ကုသိုလ် သုံးမျိုးတွဲ၌ ပြဿနာအလိုက် ဖော်ပြချက်၏ အဟုတ်ပြ ပုံစံကိုလည်း၊ အငြင်းပြ ပုံစံကိုလည်း၊ အဟုတ်ပြ အငြင်းပြ ပုံစံကိုလည်း၊ အငြင်းပြ အဟုတ်ပြ ပုံစံကိုလည်း ရေတွက်ထားသည့်အတိုင်း ထိုနည်းတူ ရေတွက်ရမည်။ မိမိ၌နှင့် မိမိ၏ ပြင်ပ၌ ရှိသော သဘောတရားများ မတွေ့ရ။)
(sabbe paccayā kātabbā) = (အကြောင်း အားလုံးကို ပြုရမည်)
Sahetukaduka-kusalattikaṃ = အမြစ် ရှိခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
Hetusampayuttaduka-kusalattikaṃ = အမြစ်နှင့် ယှဉ်တွဲခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
Hetusahetukaduka-kusalattikaṃ = အမြစ် ဖြစ်ခြင်းနှင့် အမြစ် ရှိခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
Hetuhetusampayuttaduka-kusalattikaṃ = အမြစ် ဖြစ်ခြင်းနှင့် အမြစ်နှင့် ယှဉ်တွဲခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
Nahetusahetukaduka-kusalattikaṃ = အမြစ် မဟုတ်ခြင်းနှင့် အမြစ် ရှိခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
(pañhāvārepi sabbattha ekaṃ) = (ပြဿနာအလိုက် ဖော်ပြချက်၌လည်း နေရာတိုင်း၌ တစ်ခု)
(Hetupaccayo natthi. Pañhāvārepi sabbattha ekaṃ, pañhāvārepi imesaṃ tiṇṇannaṃ hetupaccayo natthi.) = (အမြစ်ဟူသော အကြောင်း မရှိ။ ပြဿနာအလိုက် ဖော်ပြချက်၌လည်း နေရာတိုင်း၌ တစ်ခု၊ ပြဿနာအလိုက် ဖော်ပြချက်၌လည်း ဤ သုံးခုတို့၌ အမြစ်ဟူသော အကြောင်း မရှိ။)
Sappaccayaduka-kusalattikaṃ = အကြောင်း ရှိခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
Saṅkhataduka-kusalattikaṃ = ပြုပြင်ဖန်တီးထားခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
Sanidassanaduka-kusalattikaṃ = မြင်နိုင်ခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
Sappaṭighaduka-kusalattikaṃ = ထိခိုက်မှု ရှိခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
Rūpīduka-kusalattikaṃ = ရုပ် ဖြစ်ခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
Lokiyaduka-kusalattikaṃ = လောကနှင့် သက်ဆိုင်ခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
Kenaciviññeyyaduka-kusalattikaṃ = တစ်စုံတစ်ခုသော စိတ်ဖြင့် သိနိုင်ခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
(Sahajātavārepi…pe… pañhāvārepi sabbattha ekaṃ) = (အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်၌လည်း… ပြဿနာအလိုက် ဖော်ပြချက်၌လည်း နေရာတိုင်း၌ တစ်ခု)
(sabbattha ekaṃ, saṃkhittaṃ) = (နေရာတိုင်း၌ တစ်ခု၊ အကျဉ်းချုပ်)
(saṃkhittaṃ. Sappaccayasadisaṃ vitthāretabbaṃ) = (အကျဉ်းချုပ်။ အကြောင်း ရှိသော သဘောတရားနှင့် တူအောင် အကျယ် ချဲ့ရမည်)
(Sahajātavārepi…pe… pañhāvārepi sabbattha ekaṃ.) = (အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်၌လည်း… ပြဿနာအလိုက် ဖော်ပြချက်၌လည်း နေရာတိုင်း၌ တစ်ခု။)
(Appaccayampi asaṅkhatampi sanidassanampi na labbhati.) = (အကြောင်း မရှိသော သဘောတရားလည်း၊ ပြုပြင်ဖန်တီးထားခြင်း မရှိသော သဘောတရားလည်း၊ မြင်နိုင်သော သဘောတရားလည်း မတွေ့ရ။)
(pañhāvārepi sabbattha ekaṃ.) = (ပြဿနာအလိုက် ဖော်ပြချက်၌လည်း နေရာတိုင်း၌ တစ်ခု။)
(sabbattha nava, saṃkhittaṃ) = (နေရာတိုင်း၌ ကိုးခု၊ အကျဉ်းချုပ်)
(saṃkhittaṃ. Sahajātavārepi…pe… pañhāvārepi sabbattha ekaṃ) = (အကျဉ်းချုပ်။ အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်၌လည်း… ပြဿနာအလိုက် ဖော်ပြချက်၌လည်း နေရာတိုင်း၌ တစ်ခု)
(saṃkhittaṃ, sahajātavāropi…pe… pañhāvāropi sabbattha sadisā) = (အကျဉ်းချုပ်၊ အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း… ပြဿနာအလိုက် ဖော်ပြချက်လည်း နေရာတိုင်း၌ တူကြသည်)
(Yathā kusalattike pañhāvārassa anulomampi paccanīyampi anulomapaccanīyampi paccanīyānulomampi gaṇitaṃ, evaṃ gaṇetabbaṃ. Kenaci viññeyyaṃ akusalampi kenaci viññeyyaṃ abyākatampi kenaci viññeyyakusalasadisaṃ vitthāretabbaṃ) = (ကုသိုလ် သုံးမျိုးတွဲ၌ ပြဿနာအလိုက် ဖော်ပြချက်၏ အဟုတ်ပြ ပုံစံကိုလည်း၊ အငြင်းပြ ပုံစံကိုလည်း၊ အဟုတ်ပြ အငြင်းပြ ပုံစံကိုလည်း၊ အငြင်းပြ အဟုတ်ပြ ပုံစံကိုလည်း ရေတွက်ထားသည့်အတိုင်း ထိုနည်းတူ ရေတွက်ရမည်။ တစ်စုံတစ်ခုသော စိတ်ဖြင့် သိနိုင်သော၊ အကုသိုလ် သဘောတရားလည်း၊ တစ်စုံတစ်ခုသော စိတ်ဖြင့် သိနိုင်သော၊ ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော သဘောတရားလည်း တစ်စုံတစ်ခုသော စိတ်ဖြင့် သိနိုင်သော၊ ကုသိုလ် သဘောတရားနှင့် တူအောင် အကျယ် ချဲ့ရမည်)
Āsavaduka-kusalattikaṃ = စိတ်အစွန်းအထင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
Sāsavaduka-kusalattikaṃ = စိတ်အစွန်းအထင်း၏ အာရုံ ဖြစ်နိုင်ခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
Āsavasampayuttaduka-kusalattikaṃ = စိတ်အစွန်းအထင်းနှင့် ယှဉ်တွဲခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
Āsavasāsavaduka-kusalattikaṃ = စိတ်အစွန်းအထင်း ဖြစ်ခြင်းနှင့် စိတ်အစွန်းအထင်း၏ အာရုံ ဖြစ်နိုင်ခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
Āsavaāsavasampayuttaduka-kusalattikaṃ = စိတ်အစွန်းအထင်း ဖြစ်ခြင်းနှင့် စိတ်အစွန်းအထင်းနှင့် ယှဉ်တွဲခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
Āsavavippayuttasāsavaduka-kusalattikaṃ = စိတ်အစွန်းအထင်းနှင့် ကင်းကွာခြင်းနှင့် စိတ်အစွန်းအထင်း၏ အာရုံ ဖြစ်နိုင်ခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
(Sahajātavāropi…pe… sampayuttavāropi sabbattha vitthāretabbo.) = (အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း… ယှဉ်တွဲခြင်းအလိုက် ဖော်ပြချက်လည်း နေရာတိုင်း၌ အကျယ် ချဲ့ရမည်။)
(majjhe tiṇṇaṃ sahajātādhipati labbhati) = (အလယ် သုံးခု၌ အတူ ပေါ်ပေါက်သော အကြီးအမှူးကို တွေ့ရသည်)
(Saṃkhittaṃ. Sahajātavārepi paccayavārepi…pe… pañhāvārepi sabbattha ekaṃ.) = (အကျဉ်းချုပ်။ အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်၌လည်း၊ အကြောင်းပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်၌လည်း… ပြဿနာအလိုက် ဖော်ပြချက်၌လည်း နေရာတိုင်း၌ တစ်ခု။)
(saṃkhittaṃ. Paccanīyaṃ. Sahajātavārepi…pe… sampayuttavārepi sabbattha dve) = (အကျဉ်းချုပ်။ အငြင်းပြ ပုံစံ။ အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်၌လည်း… ယှဉ်တွဲခြင်းအလိုက် ဖော်ပြချက်၌လည်း နေရာတိုင်း၌ နှစ်ခု)
(Sahajātavārepi …pe… pañhāvārepi sabbattha ekaṃ.) = (အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်၌လည်း … ပြဿနာအလိုက် ဖော်ပြချက်၌လည်း နေရာတိုင်း၌ တစ်ခု။)
(saṃkhittaṃ. Sahajātavārepi…pe… sampayuttavārepi sabbattha pañca.) = (အကျဉ်းချုပ်။ အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်၌လည်း… ယှဉ်တွဲခြင်းအလိုက် ဖော်ပြချက်၌လည်း နေရာတိုင်း၌ ငါးခု။)
(saṃkhittaṃ. Sahajātavārepi…pe… sampayuttavārepi sabbattha ekaṃ) = (အကျဉ်းချုပ်။ အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်၌လည်း… ယှဉ်တွဲခြင်းအလိုက် ဖော်ပြချက်၌လည်း နေရာတိုင်း၌ တစ်ခု)
(Sahajātavāropi paccayavāropi nissayavāropi saṃsaṭṭhavāropi sampayuttavāropi vitthāretabbā.) = (အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း၊ အကြောင်းပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်လည်း၊ အမှီပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်လည်း၊ ရောနှောခြင်းအလိုက် ဖော်ပြချက်လည်း၊ ယှဉ်တွဲခြင်းအလိုက် ဖော်ပြချက်လည်း အကျယ် ချဲ့ရမည်။)
(Sahajātavārepi… sampayuttavārepi sabbattha nava.) = (အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်၌လည်း… ယှဉ်တွဲခြင်းအလိုက် ဖော်ပြချက်၌လည်း နေရာတိုင်း၌ ကိုးခု။)
(Sahajātavāropi…pe… pañhāvāropi vitthāretabbo.) = (အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း… ပြဿနာအလိုက် ဖော်ပြချက်လည်း အကျယ် ချဲ့ရမည်။)
Saññojanaduka-kusalattikaṃ = နှောင်ကြိုး နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
Saññojaniyaduka-kusalattikaṃ = နှောင်ကြိုး၏ အာရုံ ဖြစ်နိုင်ခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
Saññojanasampayuttaduka-kusalattikaṃ = နှောင်ကြိုးနှင့် ယှဉ်တွဲခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
Saññojanasaññojaniyaduka-kusalattikaṃ = နှောင်ကြိုး ဖြစ်ခြင်းနှင့် နှောင်ကြိုး၏ အာရုံ ဖြစ်နိုင်ခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
Saññojanasaññojanasampayuttaduka-kusalattikaṃ = နှောင်ကြိုး ဖြစ်ခြင်းနှင့် နှောင်ကြိုးနှင့် ယှဉ်တွဲခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
Saññojanavippayuttasaññojaniyaduka-kusalattikaṃ = နှောင်ကြိုးနှင့် ကင်းကွာခြင်းနှင့် နှောင်ကြိုး၏ အာရုံ ဖြစ်နိုင်ခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
(Sahajātavāropi…pe… sampayuttavāropi paṭiccavārasadisā vitthāretabbā.) = (အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း… ယှဉ်တွဲခြင်းအလိုက် ဖော်ပြချက်လည်း မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူအောင် အကျယ် ချဲ့ရမည်။)
(Yathā cūḷantaraduke lokiyadukagamanaṃ, evaṃ imampi ñātabbaṃ. Sahajātavāropi…pe… pañhāvāropi vitthāretabbā.) = (ကြားညှပ် နှစ်မျိုးတွဲ အစုငယ်၌ လောကနှင့် သက်ဆိုင်ခြင်း နှစ်မျိုးတွဲ၏ သွားပုံအတိုင်း ဤသည်ကိုလည်း ထိုနည်းတူ သိရမည်။ အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း… ပြဿနာအလိုက် ဖော်ပြချက်လည်း အကျယ် ချဲ့ရမည်။)
(Sahajātavāropi…pe… sampayuttavāropi vitthāretabbā.) = (အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း… ယှဉ်တွဲခြင်းအလိုက် ဖော်ပြချက်လည်း အကျယ် ချဲ့ရမည်။)
(Sahajātavāropi…pe… sampayuttavāropi paṭiccavārasadisā.) = (အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း… ယှဉ်တွဲခြင်းအလိုက် ဖော်ပြချက်လည်း မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူကြသည်။)
(Sahajātavāropi… sampayuttavāropi paṭiccavārasadisā vitthāretabbā.) = (အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း… ယှဉ်တွဲခြင်းအလိုက် ဖော်ပြချက်လည်း မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူအောင် အကျယ် ချဲ့ရမည်။)
(Yathā cūḷantaraduke lokiyadukasadisaṃ. Sahajātavāropi…pe… pañhāvāropi sabbattha vitthāretabbā.) = (ကြားညှပ် နှစ်မျိုးတွဲ အစုငယ်၌ လောကနှင့် သက်ဆိုင်ခြင်း နှစ်မျိုးတွဲနှင့် တူသည့်အတိုင်း။ အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း… ပြဿနာအလိုက် ဖော်ပြချက်လည်း နေရာတိုင်း၌ အကျယ် ချဲ့ရမည်။)
Ganthaduka-kusalattikaṃ = အထုံး နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
Ganthaniyaduka-kusalattikaṃ = အထုံး၏ အာရုံ ဖြစ်နိုင်ခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
Ganthasampayuttaduka-kusalattikaṃ = အထုံးနှင့် ယှဉ်တွဲခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
Ganthaganthaniyaduka-kusalattikaṃ = အထုံး ဖြစ်ခြင်းနှင့် အထုံး၏ အာရုံ ဖြစ်နိုင်ခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
Ganthaganthasampayuttaduka-kusalattikaṃ = အထုံး ဖြစ်ခြင်းနှင့် အထုံးနှင့် ယှဉ်တွဲခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
Ganthavippayuttaganthaniyaduka-kusalattikaṃ = အထုံးနှင့် ကင်းကွာခြင်းနှင့် အထုံး၏ အာရုံ ဖြစ်နိုင်ခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
(Sahajātavārepi …pe… pañhāvārepi sabbattha ekaṃ) = (အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်၌လည်း … ပြဿနာအလိုက် ဖော်ပြချက်၌လည်း နေရာတိုင်း၌ တစ်ခု)
(saṃkhittaṃ, lokiyalokuttaragamanasadisaṃ) = (အကျဉ်းချုပ်၊ လောကနှင့် သက်ဆိုင်ခြင်းနှင့် လောကကို ကျော်လွန်ခြင်း၏ သွားပုံနှင့် တူသည်)
(Sahajātavāropi…pe… pañhāvāropi vitthāretabbā.) = (အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း… ပြဿနာအလိုက် ဖော်ပြချက်လည်း အကျယ် ချဲ့ရမည်။)
(Sahajātavārampi…pe… sampayuttavārampi paṭiccavārasadisaṃ vitthāretabbaṃ.) = (အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း… ယှဉ်တွဲခြင်းအလိုက် ဖော်ပြချက်လည်း မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူအောင် အကျယ် ချဲ့ရမည်။)
(Sahajātavāropi…pe… pañhāvāropi sabbattha vitthāretabbā.) = (အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း… ပြဿနာအလိုက် ဖော်ပြချက်လည်း နေရာတိုင်း၌ အကျယ် ချဲ့ရမည်။)
(Sahajātavārampi…pe… sampayuttavārampi paṭiccavārasadisaṃ.) = (အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း… ယှဉ်တွဲခြင်းအလိုက် ဖော်ပြချက်လည်း မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူကြသည်။)
(Oghagocchakampi yogagocchakampi āsavagocchakakusalattikasadisaṃ.) = (ရေအလျဉ်တို့၏ အစုလည်း၊ ထမ်းပိုးတို့၏ အစုလည်း စိတ်အစွန်းအထင်းတို့၏ အစုနှင့် ကုသိုလ် သုံးမျိုးတွဲနှင့် တူကြသည်။)
Nīvaraṇaduka-kusalattikaṃ = အတားအဆီး နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
Nīvaraṇiyaduka-kusalattikaṃ = အတားအဆီး၏ အာရုံ ဖြစ်နိုင်ခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
Nīvaraṇasampayuttaduka-kusalattikaṃ = အတားအဆီးနှင့် ယှဉ်တွဲခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
Nīvaraṇanīvaraṇiyaduka-kusalattikaṃ = အတားအဆီး ဖြစ်ခြင်းနှင့် အတားအဆီး၏ အာရုံ ဖြစ်နိုင်ခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
Nīvaraṇanīvaraṇasampayuttaduka-kusalattikaṃ = အတားအဆီး ဖြစ်ခြင်းနှင့် အတားအဆီးနှင့် ယှဉ်တွဲခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
Nīvaraṇavippayuttanīvaraṇiyaduka-kusalattikaṃ = အတားအဆီးနှင့် ကင်းကွာခြင်းနှင့် အတားအဆီး၏ အာရုံ ဖြစ်နိုင်ခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
(Yathā kusalattike pañhāvārassa anulomampi paccanīyampi anulomapaccanīyampi paccanīyānulomampi gaṇitaṃ, evaṃ gaṇetabbaṃ) = (ကုသိုလ် သုံးမျိုးတွဲ၌ ပြဿနာအလိုက် ဖော်ပြချက်၏ အဟုတ်ပြ ပုံစံကိုလည်း၊ အငြင်းပြ ပုံစံကိုလည်း၊ အဟုတ်ပြ အငြင်းပြ ပုံစံကိုလည်း၊ အငြင်းပြ အဟုတ်ပြ ပုံစံကိုလည်း ရေတွက်ထားသည့်အတိုင်း ထိုနည်းတူ ရေတွက်ရမည်)
(Sahajātavāropi…pe… pañhāvāropi vitthāretabbā) = (အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း… ပြဿနာအလိုက် ဖော်ပြချက်လည်း အကျယ် ချဲ့ရမည်)
(Sahajātavārepi…pe… pañhāvārepi sabbattha nava.) = (အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်၌လည်း… ပြဿနာအလိုက် ဖော်ပြချက်၌လည်း နေရာတိုင်း၌ ကိုးခု။)
(Sahajātavārepi …pe… pañhāvārepi sabbattha vitthāretabbaṃ.) = (အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်၌လည်း … ပြဿနာအလိုက် ဖော်ပြချက်၌လည်း နေရာတိုင်း၌ အကျယ် ချဲ့ရမည်။)
Parāmāsaduka-kusalattikaṃ = မှားယွင်းသော ယူဆမှု နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
Parāmaṭṭhaduka-kusalattikaṃ = မှားယွင်းသော ယူဆမှု၏ အာရုံ ဖြစ်နိုင်ခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
Parāmāsasampayuttaduka-kusalattikaṃ = မှားယွင်းသော ယူဆမှုနှင့် ယှဉ်တွဲခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
Parāmāsaparāmaṭṭhaduka-kusalattikaṃ = မှားယွင်းသော ယူဆမှု ဖြစ်ခြင်းနှင့် မှားယွင်းသော ယူဆမှု၏ အာရုံ ဖြစ်နိုင်ခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
Parāmāsavippayuttaparāmaṭṭhaduka-kusalattikaṃ = မှားယွင်းသော ယူဆမှုနှင့် ကင်းကွာခြင်းနှင့် မှားယွင်းသော ယူဆမှု၏ အာရုံ ဖြစ်နိုင်ခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
(Sahajātavārampi…pe… sampayuttavārampi vitthāretabbaṃ.) = (အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း… ယှဉ်တွဲခြင်းအလိုက် ဖော်ပြချက်လည်း အကျယ် ချဲ့ရမည်။)
(Sahajātavāropi …pe… pañhāvāropi vitthāretabbā.) = (အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း … ပြဿနာအလိုက် ဖော်ပြချက်လည်း အကျယ် ချဲ့ရမည်။)
(Sahajātavārampi…pe… pañhāvārampi vitthāretabbaṃ.) = (အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း… ပြဿနာအလိုက် ဖော်ပြချက်လည်း အကျယ် ချဲ့ရမည်။)
(majjhime ca ante ca ārammaṇādhipati) = (အလယ်၌လည်းကောင်း၊ အဆုံး၌လည်းကောင်း အာရုံ အကြီးအမှူး)
(saṃkhittaṃ. Lokiyalokuttaradukasadisaṃ. Sahajātavāropi…pe… pañhāvāropi vitthāretabbā.) = (အကျဉ်းချုပ်။ လောကနှင့် သက်ဆိုင်ခြင်းနှင့် လောကကို ကျော်လွန်ခြင်း နှစ်မျိုးတွဲနှင့် တူသည်။ အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း… ပြဿနာအလိုက် ဖော်ပြချက်လည်း အကျယ် ချဲ့ရမည်။)
(saṃkhittaṃ. Lokiyadukasadisaṃ. Sahajātavārampi…pe… pañhāvārampi vitthāretabbaṃ.) = (အကျဉ်းချုပ်။ လောကနှင့် သက်ဆိုင်ခြင်း နှစ်မျိုးတွဲနှင့် တူသည်။ အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း… ပြဿနာအလိုက် ဖော်ပြချက်လည်း အကျယ် ချဲ့ရမည်။)
