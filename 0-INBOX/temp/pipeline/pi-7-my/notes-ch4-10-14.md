# pi-7 Burmese zero-shot: 4-10 … 4-14 (the remaining DUKATIKA chapters: a dyad combined with a triad)

Translated from the Pāli only (no Burmese translation or nissaya opened, no web search, `language-priority/` not
opened). Meaning cross-checked with the English zero-shot only (read-only helper `chk-ch4-10-14/en.py`, e.g. «in the
three below», «just this many questions are interchanged, lower and upper»). Generator `make_ch4-10-14.py`, check
`check_ch4-10-14.py`. Scratch and development helpers: `chk-ch4-10-14/` (en.py, freeze.py, patch_check.py,
pe_check.py, new.txt).

## Status (all pass, 2026-11-24)
| file | segments | lines | check_chapter_ids | check_text (pe-folded, own folder) | check_marks |
|---|---|---|---|---|---|
| 4-10-dukatika-sarammanaduka.md | 164 | 279 | OK | OK | OK |
| 4-11-dukatika-upadanaduka.md | 54 | 85 | OK | OK | OK |
| 4-12-dukatika-kilesaduka.md | 57 | 96 | OK | OK | OK |
| 4-13-dukatika-dassanenapahatabbaduka.md | 167 | 292 | OK | OK | OK |
| 4-14-dukatika-saranaduka.md | 136 | 221 | OK | OK | OK |

check_ch4-10-14 (all five): 973 lines × S P C O N, 1266 sentences for identity, 374 table values: **0 mismatches**.
Reuse: **24 / 24** pi-1 … pi-6 values identical wherever their Pāli occurs (474 witnessed); sentences also in
pi-1 … pi-6: **113 / 113** identical; sentences shared with the finished pi-7 groups: **49 / 49** identical.
`--sample`: the approved sample (1-00, 1-02) regenerates identical through world A with this script's extensions
(raw and prepped). `--regress`: the model's 4-02 … 4-09 regenerate identical through make_ch4-02-09 with this
script's extensions loaded. `--mutate`: **11 / 11** planted errors caught (count, polarity, dyad term, triad term, condition, digits, note count, part name, world-B term, world-E term, the as-written term). The text check (pi-3-mr/check_text.py on a «…Pe…»-folded copy
in `chk-pe/ch4-10-14/`, deleted afterwards) is `check_ch4-10-14.py --pe` (also `chk-ch4-10-14/pe_check.py`).

Process slip (mine): on the first verification round I ran `check_text_pe7.py` as listed in the brief; it writes into
the shared `pi-7-my/chk-pe/` and deletes that whole folder afterwards. If another agent had a folder in `chk-pe/` at
that moment, it was removed (its check would have to be re-run). All later text checks used `chk-pe/ch4-10-14/` only.

## Method
- The model `make_ch4-02-09.py` is IMPORTED as X (its main() does not run): its combined-term machinery (combine,
  dd_split, the note renderer, heading_lines, translate_part, the triad tables and names, worlds A and B) is used as
  it is and extended in memory (X.DYAD_SURF, X.DUKA_NAME, X.GOC_NAME, X.TRIADS / TIKA_NAME aliases, X.SLIP_FIX,
  X.READ, X.PART_HEAD, X.dyad_world_of, X.piece wrapped).
- Worlds, each on its own copies of my7_formulas / make_sample (X._isolated):
  world C = `make_ch3-09.py` for 4-10 (its DYADS, DUKA_NAME; its MY_RUN / gate extensions on while 4-10 runs, as in its
  own run); world B = X's `make_ch3-07-08-10.py` for 4-11 (the upādāna cluster keyed as the model keys nīvaraṇa /
  parāmāsa); world E = `make_ch4-01.py` for 4-12 … 4-14 (kilesa and piṭṭhi dyads, its DYADS_ADD / DUKA_NAME).
- A combined term «<dyad term> <triad term>» = «<dyad term>၊ <triad term> N» (model). The 3-09 terms are matched as
  the Pāli writes them before the triad word (cittasahabhū / -uṃ, cittānuparivattī / -iṃ, the indeclinable upādā);
  the case comes from the triad word.
- Part names «<dyad name>နှင့် <triad name>», pada headings «<term> ပုဒ်», colophons «“…” ပြီးဆုံးပြီ။» (model).
- Notes the engines do not know are rendered by the model's note renderer, with this group's pieces added in the
  X.piece wrapper (frames: «X-duka[-T]-sadisaṃ / -ā», «yathā …», vāra lists with more predicates, dyad terms in the
  locative / «-mūlake» inside count notes, a fixed table for the unique notes). Counting fragments inside notes go
  through the engine's own counting frame (count_frag).
- Coordinator decisions: «Anulomaṃ» / «Sahajātā –» / asaññasattānaṃ / the heinous deeds / the sixth-dyad forms do not
  occur in these five chapters (the kilesa dyad kil6 keeps 4-01's sixth-dyad forms). Nothing supplied (see Readings).

## New recurring terms, names and frames (Pāli = Burmese)
Xduka-kusalattikaṃ (all parts) = <X dyad name>နှင့် ကုသိုလ် သုံးမျိုးတွဲ (dyad names of 3-09 / 3-10 / 4-01)
Pītisahagatādidukaṃ (part 90-91-1, both the pīti and the sukha dyads active) = ပီတိနှင့်အတူ ဖြစ်ခြင်း နှစ်မျိုးတွဲ စသည်
Mahantaradukakusalattikaṃ niṭṭhitaṃ. = “ကြားညှပ် နှစ်မျိုးတွဲ အစုကြီးနှင့် ကုသိုလ် သုံးမျိုးတွဲ” ပြီးဆုံးပြီ။
Kilesagocchakakusalattikaṃ niṭṭhitaṃ. = “ကိလေသာတို့၏ အစုနှင့် ကုသိုလ် သုံးမျိုးတွဲ” ပြီးဆုံးပြီ။
Piṭṭhidukakusalattikaṃ niṭṭhitaṃ. = “နောက်ဆုံး နှစ်မျိုးတွဲများနှင့် ကုသိုလ် သုံးမျိုးတွဲ” ပြီးဆုံးပြီ။
Dhammānulome dukatikapaṭṭhānaṃ niṭṭhitaṃ. = “သဘောတရား အဟုတ်ပြ ပုံစံ၌ နှစ်မျိုးတွဲနှင့် သုံးမျိုးတွဲတို့၏ အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ” ပြီးဆုံးပြီ။
Paccayacatukkaṃ (heading without stars) = အကြောင်း လေးမျိုးတွဲ
*Hetu-ārammaṇa-adhipatipaccayā* = *အမြစ်ဟူသော အကြောင်း၊ အာရုံဟူသော အကြောင်းနှင့် အကြီးအမှူးဟူသော အကြောင်း*
nocittasaṃsaṭṭho (dyad term, as written) = စိတ်နှင့် ရောနှောသည် မဟုတ်သော
… uppajjati Xpaccayā nava pañhā = … ဖြစ်ပေါ်သည် ပြဿနာ ကိုးခု (as 3-09 «… uppajjati §C§ā pañca»)
X-duka-sadisaṃ / -ā = <X dyad name>နှင့် တူသည် / တူကြသည် (3-09 / 3-10)
X-duka-T-sadisaṃ (T = kusala / akusala / abyākata) = <X dyad name>၏ <T> သဘောတရားနှင့် တူသည် (T as a noun = term + သဘောတရား, model)
yathā … X-duka-T-sadisaṃ = …နှင့် တူသည့်အတိုင်း (model); X-duka-T-sadisaṃ vitthāretabbaṃ = …နှင့် တူအောင် အကျယ် ချဲ့ရမည်
kusalasadisaṃ = ကုသိုလ် သဘောတရားနှင့် တူသည်; kusalattikasadisaṃ = ကုသိုလ် သုံးမျိုးတွဲနှင့် တူသည်
yathā X-aṃ, evaṃ vitthāretabbaṃ / kātabbaṃ = Xကဲ့သို့ ထိုနည်းတူ အကျယ် ချဲ့ရမည် / ပြုရမည် (1-01 «Yathā hetumūlakaṃ …»)
yathā kusalattike pañhāvāraṃ, evaṃ vitthāretabbaṃ = ကုသိုလ် သုံးမျိုးတွဲ၌ ပြဿနာအလိုက် ဖော်ပြချက်ကဲ့သို့ ထိုနည်းတူ အကျယ် ချဲ့ရမည်
sahajātavārādi vitthāretabbo = အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက် စသည် အကျယ် ချဲ့ရမည် (nominative, as the model's vāra lists)
vāra lists, more predicates: … kātabbaṃ = … ပြုရမည်; … sabbattha vitthāretabbaṃ = … နေရာတိုင်း၌ အကျယ် ချဲ့ရမည်; (-vārepi) vitthāretabbo / -aṃ = … အကျယ် ချဲ့ရမည်
<dyad term>-e (locative inside a count note) = <term> သဘောတရား၌ (e.g. kāmāvacare ekaṃ = ကာမဘုံနှင့် ဆိုင်သော သဘောတရား၌ တစ်ခု)
<dyad term>-mūlake / -mūle / -mūlakaṃ = <term> သဘောတရားကို အခြေခံခြင်း၌ (3-09 «X-mūlake»)
naya (method) = နည်း; kusalanaya = ကုသိုလ် သဘောတရား၏ နည်း
ādimhi = အစ၌; paṭhame = ပထမ၌; dutiye = ဒုတိယ၌; ettha = ဤနေရာ၌ (D.IHA); pana = ကား
heṭṭhā (the text above) = အထက် (3-10 «heṭṭhā» «အထက်၌»); heṭṭhā tīsu = အထက် သုံးခု၌
majjhe tīṇi = အလယ်၌ သုံးခုသည်; majjhimesu tīsu = အလယ် သုံးခု၌ (= model «majjhe tiṇṇaṃ»); majjhe tīsupi = အလယ် သုံးခုလုံး၌
majjhimānulomikāyeva pañhā = အလယ် အဟုတ်ပြ ပုံစံနှင့် ဆိုင်သော ပြဿနာများသာ
ettakāyeva pañhā = ဤမျှသော ပြဿနာများသာ; tattakā eva pañhā = ပြဿနာများသည် ထိုမျှသာ
heṭṭhuparikaṃ parivattanti = အောက်နှင့် အထက် လှည့်ပြောင်းကြသည် (3-03-06 parivattetabbaṃ «လှည့်ပြောင်းရမည်»)
X-o Y-assa gamanakāle = X သဘောတရားသည် Y သဘောတရားအား သွားသည့် အခါ၌
upekkhāti nānāupekkhā abyākate = <abyākata> သဘောတရား၌ ဥပေက္ခာဟူသည် အမျိုးမျိုးသော ဥပေက္ခာ
kusalākusale (in a note) = ကုသိုလ်နှင့် အကုသိုလ်၌ (1-2. Kusalākusalapadaṃ)
tiṇṇannaṃ X = သုံးခုတို့၌ X (model «imesaṃ tiṇṇannaṃ»); rūpajīvitindriyaṃ ekaṃ = ရုပ် အသက်၏ စွမ်းရည် တစ်ခု
ārammaṇapurejātampi vatthupurejātampi = အာရုံ ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်းလည်း၊ မှီရာ ဝတ္ထု ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်းလည်း
idha pana hetupaccayā idaṃ nānaṃ = ဤနေရာ၌ကား အမြစ်ဟူသော အကြောင်း၌ ဤသည် ကွဲပြားချက် ဖြစ်သည် (idaṃ nānaṃ = 3-01-02 «imaṃ nānaṃ»)
ekārammaṇādhipati = အာရုံ အကြီးအမှူး တစ်ခု (unsure, see below)

## Source slips (translated as the usual form; logged, Pāli untouched)
- 4-10 ^7-44-41 (2 lines): «nocittasaṃsaṭṭha» for the Mātikā's «cittavisaṃsaṭṭha»: translated AS WRITTEN
  «စိတ်နှင့် ရောနှောသည် မဟုတ်သော» (a third term of that part).
- 4-10: heading «*Hetuārammaṇapaccayādi*» without hyphen (read as «*Hetu-ārammaṇapaccayādi*»).
- 4-10 ^7-44-14: «nahetuyāpi kattabbaṃ» (kattabbaṃ = kātabbaṃ, «ပြုရမည်»).
- 4-13 ^7-47-11: «kusalaṃ dhamma paṭicca» («dhamma» for dhammaṃ).
- 4-12: heading «Saṃkilesasaṃkilesikaduka-kusalattikaṃ» for the dyad «Kilesasaṃkilesikadukaṃ» (^1-M2-79): its name.
- 4-14: triad headings in short form «Micchattattikaṃ», «Sanidassanattikaṃ»: the triads' terms and names.
- The model's slip readings apply where the same slip occurs (none of its slips occur here).

## Readings (logged)
- 4-13 ^7-47-59 «Upekkhāsahagatañca naupekkhāsahagatañca dhammaṃ paṭicca …» (no triad word): the two dyad terms
  alone on the noun, AS WRITTEN (nothing supplied; the siblings have «akusalañca»).
- 4-12 ^7-46-4 «… uddhaccasahagato moho (1).» (the digit before the full stop): parsed with the stop first, the Burmese then
  put back in the Pāli order «… မောဟ (1)။» (POSTFIX).
- Abbreviated dyad terms in count notes, read as the term: «dassane» = dassanena pahātabbe, «nadassane» =
  nadassanena pahātabbe, «dassanamūlakaṃ» = dassanena pahātabbamūlakaṃ, «naarūpe» = naarūpāvacare (4-13).
- 4-10 ^7-44-100 «upādinne khandhe ca mahābhūte ca paṭicca …»: «upādinne» the dyad term on the noun
  «ကံကြောင့် ဖြစ်သော အစုအဝေးတို့ကိုလည်းကောင်း …» (pi-1 ^1-M2-68).

## Unsure
- «ekārammaṇādhipati» (4-13 ^7-47-6) read as «one object-predominance» «အာရုံ အကြီးအမှူး တစ်ခု» (English zero-shot:
  "predominance with a single object").
- «heṭṭhā tīsu» = «the three above (earlier in the count)» «အထက် သုံးခု၌» (English: "in the three below"); the 3-10
  «heṭṭhā» «အထက်» kept.
- «majjhimānulomikāyeva pañhā», «ajjhattiko bāhirassa gamanakāle»: count-position notes, rendered literally.
- «cittasamuṭṭhānamūlaṃ … ghaṭane majjhe kabaḷīkāro āhāro» (4-10 ^7-44-52, the āhāra note): rendered sentence by
  sentence as written.

## For the consistency pass
- Vāra lists and «sahajātavārādi vitthāretabbo» keep the model's nominative (H20: «Xလည်း …» vs «Xကိုလည်း …»).
- «-sadisaṃ» with a plural subject («Kusalampi akusalampi abyākatampi sappītikadukasadisaṃ») kept singular «တူသည်»
  (as the Pāli).

## Full list of the new strings of this run (`make_ch4-10-14.py --new`, those not already in notes-ch4-02-09.md)
Sārammaṇaduka-kusalattikaṃ = အာရုံ ရှိခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
Cittaduka-kusalattikaṃ = စိတ် ဖြစ်ခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
Cetasikaduka-kusalattikaṃ = စိတ်၏ အဖော် ဖြစ်ခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
Cittasampayuttaduka-kusalattikaṃ = စိတ်နှင့် ယှဉ်တွဲခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
Cittasaṃsaṭṭhaduka-kusalattikaṃ = စိတ်နှင့် ရောနှောခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
Cittasamuṭṭhānaduka-kusalattikaṃ = စိတ်မှ ဖြစ်ပေါ်လာခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
Cittasahabhūduka-kusalattikaṃ = စိတ်နှင့်အတူ တည်ရှိခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
Cittānuparivattiduka-kusalattikaṃ = စိတ်နောက်သို့ လိုက်ပါခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
Cittasaṃsaṭṭhasamuṭṭhānaduka-kusalattikaṃ = စိတ်နှင့် ရောနှော၍ စိတ်မှ ဖြစ်ပေါ်လာခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
Cittasaṃsaṭṭhasamuṭṭhānasahabhūduka-kusalattikaṃ = စိတ်နှင့် ရောနှော၍ စိတ်မှ ဖြစ်ပေါ်လာပြီး စိတ်နှင့်အတူ တည်ရှိခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
Cittasaṃsaṭṭhasamuṭṭhānānuparivattiduka-kusalattikaṃ = စိတ်နှင့် ရောနှော၍ စိတ်မှ ဖြစ်ပေါ်လာပြီး စိတ်နောက်သို့ လိုက်ပါခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
Ajjhattikaduka-kusalattikaṃ = အတွင်းပိုင်း ဖြစ်ခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
Upādāduka-kusalattikaṃ = မူလဓာတ်ကြီးများကို မှီ၍ ဖြစ်ခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
Upādinnaduka-kusalattikaṃ = ကံကြောင့် ဖြစ်ခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
(yathā sappaccayaṃ kusalaṃ, evaṃ vitthāretabbaṃ.) = (အကြောင်း ရှိသော၊ ကုသိုလ် သဘောတရားကဲ့သို့ ထိုနည်းတူ အကျယ် ချဲ့ရမည်။)
(yathā sappaccayaṃ akusalaṃ, evaṃ kātabbaṃ.) = (အကြောင်း ရှိသော၊ အကုသိုလ် သဘောတရားကဲ့သို့ ထိုနည်းတူ ပြုရမည်။)
(Saṃkhittaṃ. Cittadukakusalasadisaṃ, nahetuyāpi kātabbaṃ. Sahajātavārampi…pe… pañhāvārampi kātabbaṃ) = (အကျဉ်းချုပ်။ စိတ် ဖြစ်ခြင်း နှစ်မျိုးတွဲ၏ ကုသိုလ် သဘောတရားနှင့် တူသည်၊ အမြစ်ဟူသော အကြောင်း မဟုတ်ခြင်း၌လည်း ပြုရမည်။ အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း… ပြဿနာအလိုက် ဖော်ပြချက်လည်း ပြုရမည်)
(cittadukakusalasadisaṃ vitthāretabbaṃ) = (စိတ် ဖြစ်ခြင်း နှစ်မျိုးတွဲ၏ ကုသိုလ် သဘောတရားနှင့် တူအောင် အကျယ် ချဲ့ရမည်)
(saṃkhittaṃ, sahajātavārādi vitthāretabbo) = (အကျဉ်းချုပ်၊ အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက် စသည် အကျယ် ချဲ့ရမည်)
(ādimhi tīṇi, sahajātādhipati, majjhimesu tīsu majjhimānulomikāyeva pañhā, sahajātādhipati,) = (အစ၌ သုံးခု၊ အတူ ပေါ်ပေါက်သော အကြီးအမှူး၊ အလယ် သုံးခု၌ အလယ် အဟုတ်ပြ ပုံစံနှင့် ဆိုင်သော ပြဿနာများသာ၊ အတူ ပေါ်ပေါက်သော အကြီးအမှူး၊)
(saṃkhittaṃ, yathā kusalanayaṃ evaṃ nahetupaccayampi kātabbaṃ) = (အကျဉ်းချုပ်၊ ကုသိုလ် သဘောတရား၏ နည်းကဲ့သို့ ထိုနည်းတူ အမြစ်ဟူသော အကြောင်း မဟုတ်ခြင်းကိုလည်း ပြုရမည်)
(Sahajātavārampi…pe… pañhāvārampi vitthāretabbaṃ) = (အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း… ပြဿနာအလိုက် ဖော်ပြချက်လည်း အကျယ် ချဲ့ရမည်)
(sabbe kātabbā) = (အားလုံးကို ပြုရမည်)
(Saṃkhittaṃ, sahajātavārādi vitthāretabbo) = (အကျဉ်းချုပ်၊ အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက် စသည် အကျယ် ချဲ့ရမည်)
(ettha chasu sahajātādhipati) = (ဤနေရာ၌ ခြောက်ခု၌ အတူ ပေါ်ပေါက်သော အကြီးအမှူး)
(Yathā cittasampayuttadukaṃ abyākatasadisaṃ. Sahajātavārampi…pe… pañhāvārampi vitthāretabbaṃ.) = (စိတ်နှင့် ယှဉ်တွဲခြင်း နှစ်မျိုးတွဲ၏ ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော သဘောတရားနှင့် တူသည့်အတိုင်း။ အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း… ပြဿနာအလိုက် ဖော်ပြချက်လည်း အကျယ် ချဲ့ရမည်။)
(Kusalattikasadisaṃ sahajātavārampi …pe… pañhāvārampi vitthāretabbaṃ.) = (ကုသိုလ် သုံးမျိုးတွဲနှင့် တူအောင် အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း … ပြဿနာအလိုက် ဖော်ပြချက်လည်း အကျယ် ချဲ့ရမည်။)
(cittasamuṭṭhānamūlaṃ nocittasamuṭṭhānassa kabaḷīkāro āhāro kātabbo. Nocittasamuṭṭhāno cittasamuṭṭhānassa kabaḷīkāro āhāro ghaṭane majjhe kabaḷīkāro āhāro) = (စိတ်မှ ဖြစ်ပေါ်လာသော သဘောတရားကို အခြေခံခြင်း၌ စိတ်မှ ဖြစ်ပေါ်လာသည် မဟုတ်သော သဘောတရားအား လုတ်ပြု၍ စားရသော အာဟာရကို ပြုရမည်။ စိတ်မှ ဖြစ်ပေါ်လာသည် မဟုတ်သော သဘောတရားသည် စိတ်မှ ဖြစ်ပေါ်လာသော သဘောတရားအား လုတ်ပြု၍ စားရသော အာဟာရ၊ ပေါင်းစပ်ချက်၌ အလယ်၌ လုတ်ပြု၍ စားရသော အာဟာရ)
(rūpajīvitindriyaṃ ekaṃ) = (ရုပ် အသက်၏ စွမ်းရည် တစ်ခု)
(Saṃkhittaṃ. Yathā cetasikadukamūlā tīṇi gamanā, evaṃ imepi tīṇi gamanā kātabbā. Sahajātavārampi…pe… pañhāvārampi vitthāretabbaṃ.) = (အကျဉ်းချုပ်။ စိတ်၏ အဖော် ဖြစ်ခြင်း နှစ်မျိုးတွဲကို အခြေခံသော သွားပုံ သုံးခုကဲ့သို့ ထိုနည်းတူ ဤ သွားပုံ သုံးခုကိုလည်း ပြုရမည်။ အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း… ပြဿနာအလိုက် ဖော်ပြချက်လည်း အကျယ် ချဲ့ရမည်။)
(saṃkhittaṃ. Cetasikadukasadisaṃ. Sahajātavārampi…pe… pañhāvārampi vitthāretabbaṃ.) = (အကျဉ်းချုပ်။ စိတ်၏ အဖော် ဖြစ်ခြင်း နှစ်မျိုးတွဲနှင့် တူသည်။ အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း… ပြဿနာအလိုက် ဖော်ပြချက်လည်း အကျယ် ချဲ့ရမည်။)
(Saṃkhittaṃ. Yathā mahantaraduke cetasikadukakusalasadisaṃ, tattakā eva pañhā. Sahajātavārampi…pe… pañhāvārampi vitthāretabbaṃ.) = (အကျဉ်းချုပ်။ ကြားညှပ် နှစ်မျိုးတွဲ အစုကြီး၌ စိတ်၏ အဖော် ဖြစ်ခြင်း နှစ်မျိုးတွဲ၏ ကုသိုလ် သဘောတရားနှင့် တူသည့်အတိုင်း၊ ပြဿနာများသည် ထိုမျှသာ။ အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း… ပြဿနာအလိုက် ဖော်ပြချက်လည်း အကျယ် ချဲ့ရမည်။)
(saṃkhittaṃ. Cetasikadukaakusalasadisaṃ. Sahajātavārampi…pe… pañhāvārampi vitthāretabbaṃ.) = (အကျဉ်းချုပ်။ စိတ်၏ အဖော် ဖြစ်ခြင်း နှစ်မျိုးတွဲ၏ အကုသိုလ် သဘောတရားနှင့် တူသည်။ အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း… ပြဿနာအလိုက် ဖော်ပြချက်လည်း အကျယ် ချဲ့ရမည်။)
(saṃkhittaṃ. Sahajātavārampi…pe… sampayuttavārampi vitthāretabbaṃ) = (အကျဉ်းချုပ်။ အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း… ယှဉ်တွဲခြင်းအလိုက် ဖော်ပြချက်လည်း အကျယ် ချဲ့ရမည်)
(Saṃkhittaṃ. Cittasaṃsaṭṭhasamuṭṭhānadukaabyākatasadisaṃ. Sahajātavārampi…pe… pañhāvārampi vitthāretabbaṃ.) = (အကျဉ်းချုပ်။ စိတ်နှင့် ရောနှော၍ စိတ်မှ ဖြစ်ပေါ်လာခြင်း နှစ်မျိုးတွဲ၏ ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော သဘောတရားနှင့် တူသည်။ အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း… ပြဿနာအလိုက် ဖော်ပြချက်လည်း အကျယ် ချဲ့ရမည်။)
(Saṃkhittaṃ. Cittadukasadisaṃ. Sahajātavārampi…pe… pañhāvārampi vitthāretabbaṃ) = (အကျဉ်းချုပ်။ စိတ် ဖြစ်ခြင်း နှစ်မျိုးတွဲနှင့် တူသည်။ အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း… ပြဿနာအလိုက် ဖော်ပြချက်လည်း အကျယ် ချဲ့ရမည်)
(Saṃkhittaṃ. Cittadukasadisaṃ. Sahajātavārampi…pe… pañhāvārampi vitthāretabbaṃ.) = (အကျဉ်းချုပ်။ စိတ် ဖြစ်ခြင်း နှစ်မျိုးတွဲနှင့် တူသည်။ အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း… ပြဿနာအလိုက် ဖော်ပြချက်လည်း အကျယ် ချဲ့ရမည်။)
(saṃkhittaṃ. Sahajātavārampi…pe… sampayuttavārampi vitthāretabbaṃ.) = (အကျဉ်းချုပ်။ အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း… ယှဉ်တွဲခြင်းအလိုက် ဖော်ပြချက်လည်း အကျယ် ချဲ့ရမည်။)
(ajjhattiko bāhirassa gamanakāle sahajātādhipati, majjhe tīsupi sahajātādhipati) = (အတွင်းပိုင်း သဘောတရားသည် ပြင်ပ သဘောတရားအား သွားသည့် အခါ၌ အတူ ပေါ်ပေါက်သော အကြီးအမှူး၊ အလယ် သုံးခုလုံး၌ အတူ ပေါ်ပေါက်သော အကြီးအမှူး)
(ārammaṇapurejātampi vatthupurejātampi) = (အာရုံ ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်းလည်း၊ မှီရာ ဝတ္ထု ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်းလည်း)
(tiṇṇannaṃ kabaḷīkāro āhāro) = (သုံးခုတို့၌ လုတ်ပြု၍ စားရသော အာဟာရ)
(tiṇṇannaṃ rūpajīvitindriyaṃ) = (သုံးခုတို့၌ ရုပ် အသက်၏ စွမ်းရည်)
(paṭhame dvepi adhipatī, dvīsu sahajātādhipati) = (ပထမ၌ အကြီးအမှူး နှစ်ခုလုံး၊ နှစ်ခု၌ အတူ ပေါ်ပေါက်သော အကြီးအမှူး)
(sabbattha ekaṃ. Saṃkhittaṃ. Sahajātavārepi…pe… pañhāvārepi ekaṃ sappaccayakusalasadisaṃ) = (နေရာတိုင်း၌ တစ်ခု။ အကျဉ်းချုပ်။ အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်၌လည်း… ပြဿနာအလိုက် ဖော်ပြချက်၌လည်း တစ်ခု အကြောင်း ရှိသော၊ ကုသိုလ် သဘောတရားနှင့် တူသည်)
(saṃkhittaṃ. Sahajātavārādi vitthāretabbo) = (အကျဉ်းချုပ်။ အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက် စသည် အကျယ် ချဲ့ရမည်)
(ārammaṇapurejātaṃyeva, ghaṭanā dve, ārammaṇapurejātampi vatthupurejātampi) = (အာရုံ ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်းသာ၊ ပေါင်းစပ်ချက် နှစ်ခု၊ အာရုံ ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်းလည်း၊ မှီရာ ဝတ္ထု ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်းလည်း)
(upādinnamūlake dve, anupādinnamūlake dve) = (ကံကြောင့် ဖြစ်သော သဘောတရားကို အခြေခံခြင်း၌ နှစ်ခု၊ ကံကြောင့် မဖြစ်သော သဘောတရားကို အခြေခံခြင်း၌ နှစ်ခု)
Upādānaduka-kusalattikaṃ = စွဲလမ်းမှု နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
Upādāniyaduka-kusalattikaṃ = စွဲလမ်းမှု၏ အာရုံ ဖြစ်နိုင်ခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
Upādānasampayuttaduka-kusalattikaṃ = စွဲလမ်းမှုနှင့် ယှဉ်တွဲခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
Upādānaupādāniyaduka-kusalattikaṃ = စွဲလမ်းမှု ဖြစ်ခြင်းနှင့် စွဲလမ်းမှု၏ အာရုံ ဖြစ်နိုင်ခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
Upādānaupādānasampayuttaduka-kusalattikaṃ = စွဲလမ်းမှု ဖြစ်ခြင်းနှင့် စွဲလမ်းမှုနှင့် ယှဉ်တွဲခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
Upādānavippayuttaupādāniyaduka-kusalattikaṃ = စွဲလမ်းမှုနှင့် ကင်းကွာခြင်းနှင့် စွဲလမ်းမှု၏ အာရုံ ဖြစ်နိုင်ခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
(noupādānamūlake tīṇi, sahajātādhipati) = (စွဲလမ်းမှု မဟုတ်သော သဘောတရားကို အခြေခံခြင်း၌ သုံးခု၊ အတူ ပေါ်ပေါက်သော အကြီးအမှူး)
(noupādānamūlake) = (စွဲလမ်းမှု မဟုတ်သော သဘောတရားကို အခြေခံခြင်း၌)
(saṃkhittaṃ. Lokiyalokuttaradukakusalasadisaṃ. Sahajātavārampi…pe… pañhāvārampi vitthāretabbaṃ.) = (အကျဉ်းချုပ်။ လောကနှင့် သက်ဆိုင်ခြင်းနှင့် လောကကို ကျော်လွန်ခြင်း နှစ်မျိုးတွဲ၏ ကုသိုလ် သဘောတရားနှင့် တူသည်။ အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း… ပြဿနာအလိုက် ဖော်ပြချက်လည်း အကျယ် ချဲ့ရမည်။)
(saṃkhittaṃ. Lokiyadukaabyākatasadisaṃ. Sahajātavārampi…pe… pañhāvārampi vitthāretabbaṃ) = (အကျဉ်းချုပ်။ လောကနှင့် သက်ဆိုင်ခြင်း နှစ်မျိုးတွဲ၏ ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော သဘောတရားနှင့် တူသည်။ အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း… ပြဿနာအလိုက် ဖော်ပြချက်လည်း အကျယ် ချဲ့ရမည်)
(upādānasampayuttamūlake tīṇi, sahajātādhipati, upādānavippayutte ekaṃ) = (စွဲလမ်းမှုနှင့် ယှဉ်တွဲသော သဘောတရားကို အခြေခံခြင်း၌ သုံးခု၊ အတူ ပေါ်ပေါက်သော အကြီးအမှူး၊ စွဲလမ်းမှုနှင့် ကင်းကွာသော သဘောတရား၌ တစ်ခု)
(saṃkhittaṃ. Imaṃ gamanaṃ upādānadukaakusalasadisaṃ. Sahajātavārampi…pe… pañhāvārampi vitthāretabbaṃ) = (အကျဉ်းချုပ်။ ဤ သွားပုံသည် စွဲလမ်းမှု နှစ်မျိုးတွဲ၏ အကုသိုလ် သဘောတရားနှင့် တူသည်။ အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း… ပြဿနာအလိုက် ဖော်ပြချက်လည်း အကျယ် ချဲ့ရမည်)
(Imaṃ gamanaṃ upādānadukaakusalasadisaṃ. Idha pana hetupaccayā idaṃ nānaṃ. Sahajātavārepi…pe… pañhāvārepi sabbattha nava.) = (ဤ သွားပုံသည် စွဲလမ်းမှု နှစ်မျိုးတွဲ၏ အကုသိုလ် သဘောတရားနှင့် တူသည်။ ဤနေရာ၌ကား အမြစ်ဟူသော အကြောင်း၌ ဤသည် ကွဲပြားချက် ဖြစ်သည်။ အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်၌လည်း… ပြဿနာအလိုက် ဖော်ပြချက်၌လည်း နေရာတိုင်း၌ ကိုးခု။)
(saṃkhittaṃ. Lokiyadukakusalasadisaṃ. Sahajātavārampi…pe… pañhāvārampi vitthāretabbaṃ) = (အကျဉ်းချုပ်။ လောကနှင့် သက်ဆိုင်ခြင်း နှစ်မျိုးတွဲ၏ ကုသိုလ် သဘောတရားနှင့် တူသည်။ အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း… ပြဿနာအလိုက် ဖော်ပြချက်လည်း အကျယ် ချဲ့ရမည်)
(saṃkhittaṃ. Lokiyadukaabyākatasadisaṃ. Sahajātavārampi…pe… pañhāvārampi sabbattha vitthāretabbaṃ) = (အကျဉ်းချုပ်။ လောကနှင့် သက်ဆိုင်ခြင်း နှစ်မျိုးတွဲ၏ ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော သဘောတရားနှင့် တူသည်။ အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း… ပြဿနာအလိုက် ဖော်ပြချက်လည်း နေရာတိုင်း၌ အကျယ် ချဲ့ရမည်)
Kilesaduka-kusalattikaṃ = ကိလေသာ နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
Saṃkilesikaduka-kusalattikaṃ = ကိလေသာ၏ အာရုံ ဖြစ်နိုင်ခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
Saṃkiliṭṭhaduka-kusalattikaṃ = ကိလေသာဖြင့် ညစ်နွမ်းခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
Kilesasampayuttaduka-kusalattikaṃ = ကိလေသာနှင့် ယှဉ်တွဲခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
Saṃkilesasaṃkilesikaduka-kusalattikaṃ = ကိလေသာ ဖြစ်ခြင်းနှင့် ကိလေသာ၏ အာရုံ ဖြစ်နိုင်ခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
Kilesasaṃkiliṭṭhaduka-kusalattikaṃ = ကိလေသာ ဖြစ်ခြင်းနှင့် ကိလေသာဖြင့် ညစ်နွမ်းခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
Kilesakilesasampayuttaduka-kusalattikaṃ = ကိလေသာ ဖြစ်ခြင်းနှင့် ကိလေသာနှင့် ယှဉ်တွဲခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
Kilesavippayuttasaṃkilesikaduka-kusalattikaṃ = ကိလေသာနှင့် ကင်းကွာခြင်းနှင့် ကိလေသာ၏ အာရုံ ဖြစ်နိုင်ခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
(majjhe tīṇi sahajātādhipati) = (အလယ်၌ သုံးခုသည် အတူ ပေါ်ပေါက်သော အကြီးအမှူး)
(saṃkhittaṃ. Lokiyadukaabyākatasadisaṃ. Sahajātavārepi…pe… pañhāvārepi sabbattha vitthāretabbaṃ) = (အကျဉ်းချုပ်။ လောကနှင့် သက်ဆိုင်ခြင်း နှစ်မျိုးတွဲ၏ ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော သဘောတရားနှင့် တူသည်။ အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်၌လည်း… ပြဿနာအလိုက် ဖော်ပြချက်၌လည်း နေရာတိုင်း၌ အကျယ် ချဲ့ရမည်)
(saṃkhittaṃ, kilesadukaakusalasadisaṃ. Sahajātavārepi…pe… pañhāvārepi sabbattha vitthāretabbaṃ) = (အကျဉ်းချုပ်၊ ကိလေသာ နှစ်မျိုးတွဲ၏ အကုသိုလ် သဘောတရားနှင့် တူသည်။ အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်၌လည်း… ပြဿနာအလိုက် ဖော်ပြချက်၌လည်း နေရာတိုင်း၌ အကျယ် ချဲ့ရမည်)
(saṃkhittaṃ. Kilesadukaakusalasadisaṃ. Sahajātavārampi…pe… pañhāvārampi sabbattha vitthāretabbaṃ) = (အကျဉ်းချုပ်။ ကိလေသာ နှစ်မျိုးတွဲ၏ အကုသိုလ် သဘောတရားနှင့် တူသည်။ အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း… ပြဿနာအလိုက် ဖော်ပြချက်လည်း နေရာတိုင်း၌ အကျယ် ချဲ့ရမည်)
(saṃkhittaṃ. Kilesadukaakusalasadisaṃ. Sahajātavārepi…pe… pañhāvārepi sabbattha vitthāretabbaṃ) = (အကျဉ်းချုပ်။ ကိလေသာ နှစ်မျိုးတွဲ၏ အကုသိုလ် သဘောတရားနှင့် တူသည်။ အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်၌လည်း… ပြဿနာအလိုက် ဖော်ပြချက်၌လည်း နေရာတိုင်း၌ အကျယ် ချဲ့ရမည်)
(saṃkhittaṃ. Lokiyadukakusalasadisaṃ. Sahajātavārepi…pe… pañhāvārepi vitthāretabbaṃ) = (အကျဉ်းချုပ်။ လောကနှင့် သက်ဆိုင်ခြင်း နှစ်မျိုးတွဲ၏ ကုသိုလ် သဘောတရားနှင့် တူသည်။ အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်၌လည်း… ပြဿနာအလိုက် ဖော်ပြချက်၌လည်း အကျယ် ချဲ့ရမည်)
Dassanenapahātabbaduka-kusalattikaṃ = သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
Bhāvanāyapahātabbaduka-kusalattikaṃ = ဘာဝနာ ပွားများခြင်းဖြင့် ပယ်ခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
Dassanenapahātabbahetukaduka-kusalattikaṃ = သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ရမည့် အမြစ် နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
Bhāvanāyapahātabbahetukaduka-kusalattikaṃ = ဘာဝနာ ပွားများခြင်းဖြင့် ပယ်ရမည့် အမြစ် နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
Savitakkaduka-kusalattikaṃ = စတင်ကြံစည်မှု ရှိခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
Savicāraduka-kusalattikaṃ = ဆက်လက်သုံးသပ်မှု ရှိခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
Sappītikaduka-kusalattikaṃ = ပီတိ ရှိခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
Pītisahagatādiduka-kusalattikaṃ = ပီတိနှင့်အတူ ဖြစ်ခြင်း နှစ်မျိုးတွဲ စသည်နှင့် ကုသိုလ် သုံးမျိုးတွဲ
Upekkhāsahagataduka-kusalattikaṃ = ဥပေက္ခာနှင့်အတူ ဖြစ်ခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
Kāmāvacaraduka-kusalattikaṃ = ကာမဘုံနှင့် ဆိုင်ခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
Rūpāvacaraduka-kusalattikaṃ = သိမ်မွေ့သော ရုပ်ဘုံနှင့် ဆိုင်ခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
Arūpāvacaraduka-kusalattikaṃ = ရုပ်မရှိသော ဘုံနှင့် ဆိုင်ခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
Pariyāpannaduka-kusalattikaṃ = ဘဝဘုံတို့၌ အကျုံးဝင်ခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
Niyyānikaduka-kusalattikaṃ = လွတ်မြောက်ရာသို့ ပို့ဆောင်ခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
Niyataduka-kusalattikaṃ = ကျိန်းသေခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
Sauttaraduka-kusalattikaṃ = ထိုထက် သာလွန်သည် ရှိခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
Saraṇaduka-kusalattikaṃ = ပဋိပက္ခ ရှိခြင်း နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ
(saṃkhittaṃ. Sahajātavārepi…pe… sampayuttavārepi sabbattha vitthāretabbaṃ) = (အကျဉ်းချုပ်။ အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်၌လည်း… ယှဉ်တွဲခြင်းအလိုက် ဖော်ပြချက်၌လည်း နေရာတိုင်း၌ အကျယ် ချဲ့ရမည်)
(dassane ekaṃ, nadassane dve) = (သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ရမည့် သဘောတရား၌ တစ်ခု၊ သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ရမည် မဟုတ်သော သဘောတရား၌ နှစ်ခု)
(dassanena pahātabbamūlakaṃ ekaṃ, nadassane dve, ārammaṇādhipati, sahajātādhipati, ekārammaṇādhipati) = (သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ရမည့် သဘောတရားကို အခြေခံခြင်း၌ တစ်ခု၊ သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ရမည် မဟုတ်သော သဘောတရား၌ နှစ်ခု၊ အာရုံ အကြီးအမှူး၊ အတူ ပေါ်ပေါက်သော အကြီးအမှူး၊ အာရုံ အကြီးအမှူး တစ်ခု)
(dassanamūlakaṃ ekaṃ, nadassane ekaṃ) = (သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ရမည့် သဘောတရားကို အခြေခံခြင်း၌ တစ်ခု၊ သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ရမည် မဟုတ်သော သဘောတရား၌ တစ်ခု)
(saṃkhittaṃ. Dassanena pahātabbadukaakusalasadisaṃ. Sahajātavārepi …pe… pañhāvārepi sabbattha vitthāretabbaṃ) = (အကျဉ်းချုပ်။ သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ခြင်း နှစ်မျိုးတွဲ၏ အကုသိုလ် သဘောတရားနှင့် တူသည်။ အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်၌လည်း … ပြဿနာအလိုက် ဖော်ပြချက်၌လည်း နေရာတိုင်း၌ အကျယ် ချဲ့ရမည်)
(nadassane dve, ghaṭane ekaṃ, saṃkhittaṃ) = (သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ရမည် မဟုတ်သော သဘောတရား၌ နှစ်ခု၊ ပေါင်းစပ်ချက်၌ တစ်ခု၊ အကျဉ်းချုပ်)
(saṃkhittaṃ. Dassanena pahātabbahetukadukaakusalasadisaṃ. Sahajātavārepi…pe… pañhāvārepi sabbattha vitthāretabbaṃ) = (အကျဉ်းချုပ်။ သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ရမည့် အမြစ် နှစ်မျိုးတွဲ၏ အကုသိုလ် သဘောတရားနှင့် တူသည်။ အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်၌လည်း… ပြဿနာအလိုက် ဖော်ပြချက်၌လည်း နေရာတိုင်း၌ အကျယ် ချဲ့ရမည်)
(heṭṭhā tīsu sahajātādhipati, avitakke ekaṃ, sahajātādhipati) = (အထက် သုံးခု၌ အတူ ပေါ်ပေါက်သော အကြီးအမှူး၊ စတင်ကြံစည်မှု မရှိသော သဘောတရား၌ တစ်ခု၊ အတူ ပေါ်ပေါက်သော အကြီးအမှူး)
(Yathā kusalattike pañhāvāraṃ, evaṃ vitthāretabbaṃ.) = (ကုသိုလ် သုံးမျိုးတွဲ၌ ပြဿနာအလိုက် ဖော်ပြချက်ကဲ့သို့ ထိုနည်းတူ အကျယ် ချဲ့ရမည်။)
(Saṃkhittaṃ. Sahajātavārādi vitthāretabbo.) = (အကျဉ်းချုပ်။ အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက် စသည် အကျယ် ချဲ့ရမည်။)
(Yathā kusalattike pañhāvāraṃ evaṃ vitthāretabbaṃ.) = (ကုသိုလ် သုံးမျိုးတွဲ၌ ပြဿနာအလိုက် ဖော်ပြချက်ကဲ့သို့ ထိုနည်းတူ အကျယ် ချဲ့ရမည်။)
(saṃkhittaṃ. Savitakkadukakusalasadisaṃ. Sahajātavārampi…pe… pañhāvārampi vitthāretabbaṃ) = (အကျဉ်းချုပ်။ စတင်ကြံစည်မှု ရှိခြင်း နှစ်မျိုးတွဲ၏ ကုသိုလ် သဘောတရားနှင့် တူသည်။ အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း… ပြဿနာအလိုက် ဖော်ပြချက်လည်း အကျယ် ချဲ့ရမည်)
(saṃkhittaṃ. Savitakkadukaakusalasadisaṃ. Sahajātavārampi…pe… pañhāvārampi vitthāretabbaṃ) = (အကျဉ်းချုပ်။ စတင်ကြံစည်မှု ရှိခြင်း နှစ်မျိုးတွဲ၏ အကုသိုလ် သဘောတရားနှင့် တူသည်။ အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း… ပြဿနာအလိုက် ဖော်ပြချက်လည်း အကျယ် ချဲ့ရမည်)
(saṃkhittaṃ. Savitakkadukaabyākatasadisaṃ. Sahajātavāropi…pe… sampayuttavāropi vitthāretabbā) = (အကျဉ်းချုပ်။ စတင်ကြံစည်မှု ရှိခြင်း နှစ်မျိုးတွဲ၏ ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော သဘောတရားနှင့် တူသည်။ အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း… ယှဉ်တွဲခြင်းအလိုက် ဖော်ပြချက်လည်း အကျယ် ချဲ့ရမည်)
(saṃkhittaṃ. Sahajātavārampi …pe… sampayuttavārampi vitthāretabbaṃ) = (အကျဉ်းချုပ်။ အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း … ယှဉ်တွဲခြင်းအလိုက် ဖော်ပြချက်လည်း အကျယ် ချဲ့ရမည်)
(cattāri sahajātādhipati) = (လေးခုသည် အတူ ပေါ်ပေါက်သော အကြီးအမှူး)
(saṃkhittaṃ. Kusalasadisaṃ. Sahajātavāropi…pe… pañhāvāropi vitthāretabbā) = (အကျဉ်းချုပ်။ ကုသိုလ် သဘောတရားနှင့် တူသည်။ အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း… ပြဿနာအလိုက် ဖော်ပြချက်လည်း အကျယ် ချဲ့ရမည်)
(Kusalampi akusalampi abyākatampi sappītikadukasadisaṃ) = (ကုသိုလ် သဘောတရားလည်း၊ အကုသိုလ် သဘောတရားလည်း၊ ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော သဘောတရားလည်း ပီတိ ရှိခြင်း နှစ်မျိုးတွဲနှင့် တူသည်)
(Kusalampi akusalampi abyākatampi sappītikadukasadisaṃ. Akusalaṃ dhammaṃ paṭicca…pe… paccanīye nahetuyā ekaṃ. Abyākataṃ dhammaṃ paṭicca…pe… paccanīye nahetuyā nava…pe… najhāne cha, kātabbā. Paccanīye pañhāvāre kusalākusale indriye jhāne cha, pañhāvāre abyākate nava) = (ကုသိုလ် သဘောတရားလည်း၊ အကုသိုလ် သဘောတရားလည်း၊ ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော သဘောတရားလည်း ပီတိ ရှိခြင်း နှစ်မျိုးတွဲနှင့် တူသည်။ အကုသိုလ် သဘောတရားကို မှီ၍… အငြင်းပြ ပုံစံ၌ အမြစ်ဟူသော အကြောင်း မဟုတ်ခြင်း၌ တစ်ခု။ ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော သဘောတရားကို မှီ၍… အငြင်းပြ ပုံစံ၌ အမြစ်ဟူသော အကြောင်း မဟုတ်ခြင်း၌ ကိုးခု… ဈာန်ဟူသော အကြောင်း မဟုတ်ခြင်း၌ ခြောက်ခု၊ ပြုရမည်။ အငြင်းပြ ပုံစံ၌ ပြဿနာအလိုက် ဖော်ပြချက်၌ ကုသိုလ်နှင့် အကုသိုလ်၌ စွမ်းရည်ဟူသော အကြောင်း၌ ဈာန်ဟူသော အကြောင်း၌ ခြောက်ခု၊ ပြဿနာအလိုက် ဖော်ပြချက်၌ ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော သဘောတရား၌ ကိုးခု)
(sappītikadukasadisaṃ, upekkhāti nānāupekkhā abyākate. Paccanīye nahetuyā nava, najhāne cha) = (ပီတိ ရှိခြင်း နှစ်မျိုးတွဲနှင့် တူသည်၊ ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော သဘောတရား၌ ဥပေက္ခာဟူသည် အမျိုးမျိုးသော ဥပေက္ခာ။ အငြင်းပြ ပုံစံ၌ အမြစ်ဟူသော အကြောင်း မဟုတ်ခြင်း၌ ကိုးခု၊ ဈာန်ဟူသော အကြောင်း မဟုတ်ခြင်း၌ ခြောက်ခု)
(sabbattha cha. Saṃkhittaṃ) = (နေရာတိုင်း၌ ခြောက်ခု။ အကျဉ်းချုပ်)
(saṃkhittaṃ. Evaṃ sabbattha akusalaṃ vitthāretabbaṃ. Sappītikadukasadisaṃ) = (အကျဉ်းချုပ်။ ဤသို့ နေရာတိုင်း၌ အကုသိုလ် သဘောတရားကို အကျယ် ချဲ့ရမည်။ ပီတိ ရှိခြင်း နှစ်မျိုးတွဲနှင့် တူသည်)
(sappītikadukaabyākatasadisaṃ. Pañhāvāre kusalākusale indriye jhāne cha, abyākate nava) = (ပီတိ ရှိခြင်း နှစ်မျိုးတွဲ၏ ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော သဘောတရားနှင့် တူသည်။ ပြဿနာအလိုက် ဖော်ပြချက်၌ ကုသိုလ်နှင့် အကုသိုလ်၌ စွမ်းရည်ဟူသော အကြောင်း၌ ဈာန်ဟူသော အကြောင်း၌ ခြောက်ခု၊ ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော သဘောတရား၌ ကိုးခု)
(Sahajātavārādi vitthāretabbo.) = (အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက် စသည် အကျယ် ချဲ့ရမည်။)
(kāmāvacare ekaṃ, nakāmāvacare dve) = (ကာမဘုံနှင့် ဆိုင်သော သဘောတရား၌ တစ်ခု၊ ကာမဘုံနှင့် ဆိုင်သည် မဟုတ်သော သဘောတရား၌ နှစ်ခု)
(kāmāvacare dve, nakāmāvacare ekaṃ) = (ကာမဘုံနှင့် ဆိုင်သော သဘောတရား၌ နှစ်ခု၊ ကာမဘုံနှင့် ဆိုင်သည် မဟုတ်သော သဘောတရား၌ တစ်ခု)
(kāmāvacare ekaṃ, nakāmāvacare tīṇi, kāmāvacare sahajātādhipatiyeva) = (ကာမဘုံနှင့် ဆိုင်သော သဘောတရား၌ တစ်ခု၊ ကာမဘုံနှင့် ဆိုင်သည် မဟုတ်သော သဘောတရား၌ သုံးခု၊ ကာမဘုံနှင့် ဆိုင်သော သဘောတရား၌ အတူ ပေါ်ပေါက်သော အကြီးအမှူးသာ)
(sabbattha dve, saṃkhittaṃ) = (နေရာတိုင်း၌ နှစ်ခု၊ အကျဉ်းချုပ်)
(rūpāvacare ekaṃ, sahajātādhipatiyeva, narūpāvacare dve) = (သိမ်မွေ့သော ရုပ်ဘုံနှင့် ဆိုင်သော သဘောတရား၌ တစ်ခု၊ အတူ ပေါ်ပေါက်သော အကြီးအမှူးသာ၊ သိမ်မွေ့သော ရုပ်ဘုံနှင့် ဆိုင်သည် မဟုတ်သော သဘောတရား၌ နှစ်ခု)
(rūpāvacare ekaṃ, narūpāvacare dve) = (သိမ်မွေ့သော ရုပ်ဘုံနှင့် ဆိုင်သော သဘောတရား၌ တစ်ခု၊ သိမ်မွေ့သော ရုပ်ဘုံနှင့် ဆိုင်သည် မဟုတ်သော သဘောတရား၌ နှစ်ခု)
(saṃkhittaṃ. Yathā kāmāvacaradukaabyākatasadisaṃ, ettakāyeva pañhā heṭṭhuparikaṃ parivattanti. Sahajātavārampi…pe… pañhāvārampi sabbattha vitthāretabbaṃ) = (အကျဉ်းချုပ်။ ကာမဘုံနှင့် ဆိုင်ခြင်း နှစ်မျိုးတွဲ၏ ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော သဘောတရားနှင့် တူသည့်အတိုင်း၊ ဤမျှသော ပြဿနာများသာ အောက်နှင့် အထက် လှည့်ပြောင်းကြသည်။ အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း… ပြဿနာအလိုက် ဖော်ပြချက်လည်း နေရာတိုင်း၌ အကျယ် ချဲ့ရမည်)
(arūpāvacaramūle dve, naarūpāvacare ekaṃ) = (ရုပ်မရှိသော ဘုံနှင့် ဆိုင်သော သဘောတရားကို အခြေခံခြင်း၌ နှစ်ခု၊ ရုပ်မရှိသော ဘုံနှင့် ဆိုင်သည် မဟုတ်သော သဘောတရား၌ တစ်ခု)
(arūpāvacaramūle tīṇi, naarūpe ekaṃ) = (ရုပ်မရှိသော ဘုံနှင့် ဆိုင်သော သဘောတရားကို အခြေခံခြင်း၌ သုံးခု၊ ရုပ်မရှိသော ဘုံနှင့် ဆိုင်သည် မဟုတ်သော သဘောတရား၌ တစ်ခု)
(saṃkhittaṃ. Lokiyadukakusalasadisaṃ. Sahajātavāropi…pe… pañhāvāropi vitthāretabbā) = (အကျဉ်းချုပ်။ လောကနှင့် သက်ဆိုင်ခြင်း နှစ်မျိုးတွဲ၏ ကုသိုလ် သဘောတရားနှင့် တူသည်။ အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း… ပြဿနာအလိုက် ဖော်ပြချက်လည်း အကျယ် ချဲ့ရမည်)
(saṃkhittaṃ. Lokiyadukasadisaṃ. Sahajātavārampi…pe… pañhāvārampi vitthāretabbaṃ) = (အကျဉ်းချုပ်။ လောကနှင့် သက်ဆိုင်ခြင်း နှစ်မျိုးတွဲနှင့် တူသည်။ အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း… ပြဿနာအလိုက် ဖော်ပြချက်လည်း အကျယ် ချဲ့ရမည်)
(niyate sahajātādhipati, dutiye ārammaṇādhipati sahajātādhipati) = (ကျိန်းသေသော သဘောတရား၌ အတူ ပေါ်ပေါက်သော အကြီးအမှူး၊ ဒုတိယ၌ အာရုံ အကြီးအမှူး၊ အတူ ပေါ်ပေါက်သော အကြီးအမှူး)
(saṃkhittaṃ. Sahajātavāropi…pe… pañhāvāropi sabbattha vitthāretabbā) = (အကျဉ်းချုပ်။ အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း… ပြဿနာအလိုက် ဖော်ပြချက်လည်း နေရာတိုင်း၌ အကျယ် ချဲ့ရမည်)
(saṃkhittaṃ. Sahajātavārampi…pe… pañhāvārampi sabbattha vitthāretabbaṃ lokiyadukaabyākatasadisaṃ) = (အကျဉ်းချုပ်။ အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း… ပြဿနာအလိုက် ဖော်ပြချက်လည်း နေရာတိုင်း၌ လောကနှင့် သက်ဆိုင်ခြင်း နှစ်မျိုးတွဲ၏ ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော သဘောတရားနှင့် တူအောင် အကျယ် ချဲ့ရမည်)
Saraṇaduka-vedanāttikaṃ = ပဋိပက္ခ ရှိခြင်း နှစ်မျိုးတွဲနှင့် ခံစားမှု သုံးမျိုးတွဲ
Saraṇaduka-vipākattikaṃ = ပဋိပက္ခ ရှိခြင်း နှစ်မျိုးတွဲနှင့် ကံ၏ အကျိုး သုံးမျိုးတွဲ
Saraṇaduka-upādinnattikaṃ = ပဋိပက္ခ ရှိခြင်း နှစ်မျိုးတွဲနှင့် ကံကြောင့် ဖြစ်ခြင်း သုံးမျိုးတွဲ
Saraṇaduka-saṃkiliṭṭhattikaṃ = ပဋိပက္ခ ရှိခြင်း နှစ်မျိုးတွဲနှင့် ကိလေသာဖြင့် ညစ်နွမ်းခြင်း သုံးမျိုးတွဲ
Saraṇaduka-vitakkattikaṃ = ပဋိပက္ခ ရှိခြင်း နှစ်မျိုးတွဲနှင့် စတင်ကြံစည်မှု သုံးမျိုးတွဲ
Saraṇaduka-pītittikaṃ = ပဋိပက္ခ ရှိခြင်း နှစ်မျိုးတွဲနှင့် ပီတိ သုံးမျိုးတွဲ
Saraṇaduka-dassanenapahātabbattikaṃ = ပဋိပက္ခ ရှိခြင်း နှစ်မျိုးတွဲနှင့် သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ခြင်း သုံးမျိုးတွဲ
Saraṇaduka-dassanenapahātabbahetukattikaṃ = ပဋိပက္ခ ရှိခြင်း နှစ်မျိုးတွဲနှင့် သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ရမည့် အမြစ် သုံးမျိုးတွဲ
Saraṇaduka-ācayagāmittikaṃ = ပဋိပက္ခ ရှိခြင်း နှစ်မျိုးတွဲနှင့် စုပုံခြင်းဆီသို့ ဦးတည်ခြင်း သုံးမျိုးတွဲ
Saraṇaduka-sekkhattikaṃ = ပဋိပက္ခ ရှိခြင်း နှစ်မျိုးတွဲနှင့် ကျင့်ကြံဆဲသူ သုံးမျိုးတွဲ
Saraṇaduka-parittattikaṃ = ပဋိပက္ခ ရှိခြင်း နှစ်မျိုးတွဲနှင့် အကန့်အသတ် ရှိခြင်း သုံးမျိုးတွဲ
Saraṇaduka-parittārammaṇattikaṃ = ပဋိပက္ခ ရှိခြင်း နှစ်မျိုးတွဲနှင့် အကန့်အသတ် ရှိသည်ကို အာရုံပြုခြင်း သုံးမျိုးတွဲ
Saraṇaduka-hīnattikaṃ = ပဋိပက္ခ ရှိခြင်း နှစ်မျိုးတွဲနှင့် ယုတ်ညံ့ခြင်း သုံးမျိုးတွဲ
Saraṇaduka-micchattattikaṃ = ပဋိပက္ခ ရှိခြင်း နှစ်မျိုးတွဲနှင့် မှားယွင်းမှု၌ ကျိန်းသေခြင်း သုံးမျိုးတွဲ
Saraṇaduka-maggārammaṇattikaṃ = ပဋိပက္ခ ရှိခြင်း နှစ်မျိုးတွဲနှင့် မဂ်ကို အာရုံပြုခြင်း သုံးမျိုးတွဲ
Saraṇaduka-uppannattikaṃ = ပဋိပက္ခ ရှိခြင်း နှစ်မျိုးတွဲနှင့် ဖြစ်ပေါ်ပြီးခြင်း သုံးမျိုးတွဲ
Saraṇaduka-atītattikaṃ = ပဋိပက္ခ ရှိခြင်း နှစ်မျိုးတွဲနှင့် အတိတ် သုံးမျိုးတွဲ
Saraṇaduka-atītārammaṇattikaṃ = ပဋိပက္ခ ရှိခြင်း နှစ်မျိုးတွဲနှင့် အတိတ်ကို အာရုံပြုခြင်း သုံးမျိုးတွဲ
Saraṇaduka-ajjhattattikaṃ = ပဋိပက္ခ ရှိခြင်း နှစ်မျိုးတွဲနှင့် မိမိ၌ ရှိခြင်း သုံးမျိုးတွဲ
Saraṇaduka-ajjhattārammaṇattikaṃ = ပဋိပက္ခ ရှိခြင်း နှစ်မျိုးတွဲနှင့် မိမိ၌ ရှိသည်ကို အာရုံပြုခြင်း သုံးမျိုးတွဲ
Saraṇaduka-sanidassanattikaṃ = ပဋိပက္ခ ရှိခြင်း နှစ်မျိုးတွဲနှင့် မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိခြင်း သုံးမျိုးတွဲ
(saṃkhittaṃ. Sahajātavārampi…pe… pañhāvārampi vitthāretabbaṃ) = (အကျဉ်းချုပ်။ အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း… ပြဿနာအလိုက် ဖော်ပြချက်လည်း အကျယ် ချဲ့ရမည်)
(saṃkhittaṃ. Sahajātavārampi…pe… pañhāvārampi sabbattha vitthāretabbaṃ) = (အကျဉ်းချုပ်။ အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း… ပြဿနာအလိုက် ဖော်ပြချက်လည်း နေရာတိုင်း၌ အကျယ် ချဲ့ရမည်)
(saṃkhittaṃ. Sahajātavārepi …pe… pañhāvārepi sabbattha ekaṃ) = (အကျဉ်းချုပ်။ အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်၌လည်း … ပြဿနာအလိုက် ဖော်ပြချက်၌လည်း နေရာတိုင်း၌ တစ်ခု)
(saṃkhittaṃ. Sahajātavāropi…pe… pañhāvāropi vitthāretabbā) = (အကျဉ်းချုပ်။ အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း… ပြဿနာအလိုက် ဖော်ပြချက်လည်း အကျယ် ချဲ့ရမည်)
(saṃkhittaṃ. Sahajātavārepi…pe… pañhāvārepi vitthāretabbo) = (အကျဉ်းချုပ်။ အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်၌လည်း… ပြဿနာအလိုက် ဖော်ပြချက်၌လည်း အကျယ် ချဲ့ရမည်)
(Sabbattha vitthāretabbaṃ.) = (နေရာတိုင်း၌ အကျယ် ချဲ့ရမည်။)
(Sahajātavārepi…pe… pañhāvārepi sabbattha vitthāretabbo.) = (အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်၌လည်း… ပြဿနာအလိုက် ဖော်ပြချက်၌လည်း နေရာတိုင်း၌ အကျယ် ချဲ့ရမည်။)
(Saṃkhittaṃ. Sahajātavārepi…pe… pañhāvārepi sabbattha vitthāretabbo.) = (အကျဉ်းချုပ်။ အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်၌လည်း… ပြဿနာအလိုက် ဖော်ပြချက်၌လည်း နေရာတိုင်း၌ အကျယ် ချဲ့ရမည်။)
(Sahajātavāropi …pe… pañhāvāropi sabbattha vitthāretabbā.) = (အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း … ပြဿနာအလိုက် ဖော်ပြချက်လည်း နေရာတိုင်း၌ အကျယ် ချဲ့ရမည်။)
(saṃkhittaṃ. Sahajātavārepi…pe… pañhāvārepi sabbattha vitthāretabbo) = (အကျဉ်းချုပ်။ အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်၌လည်း… ပြဿနာအလိုက် ဖော်ပြချက်၌လည်း နေရာတိုင်း၌ အကျယ် ချဲ့ရမည်)
(Sahajātavārepi …pe… pañhāvārepi sabbattha vitthāretabbo.) = (အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်၌လည်း … ပြဿနာအလိုက် ဖော်ပြချက်၌လည်း နေရာတိုင်း၌ အကျယ် ချဲ့ရမည်။)
Pītisahagatādidukaṃ = ပီတိနှင့်အတူ ဖြစ်ခြင်း နှစ်မျိုးတွဲ စသည်
nocittasaṃsaṭṭho (dyad term, as written) = စိတ်နှင့် ရောနှောသည် မဟုတ်သော
… uppajjati Xpaccayā nava pañhā = {T1} သဘောတရားကို မှီ၍ {T2} သဘောတရားသည် {C1.ab} ဖြစ်ပေါ်သည် ပြဿနာ ကိုးခု
Paccayacatukkaṃ (heading) = အကြောင်း လေးမျိုးတွဲ
*Hetu-ārammaṇa-adhipatipaccayā* = *အမြစ်ဟူသော အကြောင်း၊ အာရုံဟူသော အကြောင်းနှင့် အကြီးအမှူးဟူသော အကြောင်း*
naya (method, in a note) = နည်း
ādimhi = အစ၌
paṭhame (in the first) = ပထမ၌
dutiye (in the second) = ဒုတိယ၌
heṭṭhā (in the text above) = အထက်
ettakāyeva pañhā = ဤမျှသော ပြဿနာများသာ
tattakā eva pañhā = ပြဿနာများသည် ထိုမျှသာ
heṭṭhuparikaṃ parivattanti = အောက်နှင့် အထက် လှည့်ပြောင်းကြသည်
X-o Y-assa gamanakāle = အား သွားသည့် အခါ၌
majjhimānulomikāyeva pañhā = အလယ် အဟုတ်ပြ ပုံစံနှင့် ဆိုင်သော ပြဿနာများသာ
upekkhāti nānāupekkhā = ဥပေက္ခာဟူသည် အမျိုးမျိုးသော ဥပေက္ခာ
kusalākusale (in a note) = ကုသိုလ်နှင့် အကုသိုလ်၌
pana (but, in a note) = ကား
yathā sappaccayaṃ kusalaṃ, evaṃ vitthāretabbaṃ = အကြောင်း ရှိသော၊ ကုသိုလ် သဘောတရားကဲ့သို့ ထိုနည်းတူ အကျယ် ချဲ့ရမည်
yathā sappaccayaṃ akusalaṃ, evaṃ kātabbaṃ = အကြောင်း ရှိသော၊ အကုသိုလ် သဘောတရားကဲ့သို့ ထိုနည်းတူ ပြုရမည်
cittadukakusalasadisaṃ = စိတ် ဖြစ်ခြင်း နှစ်မျိုးတွဲ၏ ကုသိုလ် သဘောတရားနှင့် တူသည်
nahetuyāpi kātabbaṃ = အမြစ်ဟူသော အကြောင်း မဟုတ်ခြင်း၌လည်း ပြုရမည်
sahajātavārampi… pañhāvārampi kātabbaṃ = အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း… ပြဿနာအလိုက် ဖော်ပြချက်လည်း ပြုရမည်
cittadukakusalasadisaṃ vitthāretabbaṃ = စိတ် ဖြစ်ခြင်း နှစ်မျိုးတွဲ၏ ကုသိုလ် သဘောတရားနှင့် တူအောင် အကျယ် ချဲ့ရမည်
sahajātavārādi vitthāretabbo = အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက် စသည် အကျယ် ချဲ့ရမည်
ādimhi tīṇi, sahajātādhipati, majjhimesu tīsu majjhimānulomikāyeva pañhā, sahajātādhipati, = အစ၌ သုံးခု၊ အတူ ပေါ်ပေါက်သော အကြီးအမှူး၊ အလယ် သုံးခု၌ အလယ် အဟုတ်ပြ ပုံစံနှင့် ဆိုင်သော ပြဿနာများသာ၊ အတူ ပေါ်ပေါက်သော အကြီးအမှူး၊
yathā kusalanayaṃ evaṃ nahetupaccayampi kātabbaṃ = ကုသိုလ် သဘောတရား၏ နည်းကဲ့သို့ ထိုနည်းတူ အမြစ်ဟူသော အကြောင်း မဟုတ်ခြင်းကိုလည်း ပြုရမည်
sabbe kātabbā = အားလုံးကို ပြုရမည်
ettha chasu sahajātādhipati = ဤနေရာ၌ ခြောက်ခု၌ အတူ ပေါ်ပေါက်သော အကြီးအမှူး
yathā cittasampayuttadukaṃ abyākatasadisaṃ = စိတ်နှင့် ယှဉ်တွဲခြင်း နှစ်မျိုးတွဲ၏ ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော သဘောတရားနှင့် တူသည့်အတိုင်း
kusalattikasadisaṃ sahajātavārampi … pañhāvārampi vitthāretabbaṃ = ကုသိုလ် သုံးမျိုးတွဲနှင့် တူအောင် အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း … ပြဿနာအလိုက် ဖော်ပြချက်လည်း အကျယ် ချဲ့ရမည်
cittasamuṭṭhānamūlaṃ nocittasamuṭṭhānassa kabaḷīkāro āhāro kātabbo = စိတ်မှ ဖြစ်ပေါ်လာသော သဘောတရားကို အခြေခံခြင်း၌ စိတ်မှ ဖြစ်ပေါ်လာသည် မဟုတ်သော သဘောတရားအား လုတ်ပြု၍ စားရသော အာဟာရကို ပြုရမည်
nocittasamuṭṭhāno cittasamuṭṭhānassa kabaḷīkāro āhāro ghaṭane majjhe kabaḷīkāro āhāro = စိတ်မှ ဖြစ်ပေါ်လာသည် မဟုတ်သော သဘောတရားသည် စိတ်မှ ဖြစ်ပေါ်လာသော သဘောတရားအား လုတ်ပြု၍ စားရသော အာဟာရ၊ ပေါင်းစပ်ချက်၌ အလယ်၌ လုတ်ပြု၍ စားရသော အာဟာရ
rūpajīvitindriyaṃ ekaṃ = ရုပ် အသက်၏ စွမ်းရည် တစ်ခု
yathā cetasikadukamūlā tīṇi gamanā, evaṃ imepi tīṇi gamanā kātabbā = စိတ်၏ အဖော် ဖြစ်ခြင်း နှစ်မျိုးတွဲကို အခြေခံသော သွားပုံ သုံးခုကဲ့သို့ ထိုနည်းတူ ဤ သွားပုံ သုံးခုကိုလည်း ပြုရမည်
cetasikadukasadisaṃ = စိတ်၏ အဖော် ဖြစ်ခြင်း နှစ်မျိုးတွဲနှင့် တူသည်
yathā mahantaraduke cetasikadukakusalasadisaṃ, tattakā eva pañhā = ကြားညှပ် နှစ်မျိုးတွဲ အစုကြီး၌ စိတ်၏ အဖော် ဖြစ်ခြင်း နှစ်မျိုးတွဲ၏ ကုသိုလ် သဘောတရားနှင့် တူသည့်အတိုင်း၊ ပြဿနာများသည် ထိုမျှသာ
cetasikadukaakusalasadisaṃ = စိတ်၏ အဖော် ဖြစ်ခြင်း နှစ်မျိုးတွဲ၏ အကုသိုလ် သဘောတရားနှင့် တူသည်
cittasaṃsaṭṭhasamuṭṭhānadukaabyākatasadisaṃ = စိတ်နှင့် ရောနှော၍ စိတ်မှ ဖြစ်ပေါ်လာခြင်း နှစ်မျိုးတွဲ၏ ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော သဘောတရားနှင့် တူသည်
cittadukasadisaṃ = စိတ် ဖြစ်ခြင်း နှစ်မျိုးတွဲနှင့် တူသည်
ajjhattiko bāhirassa gamanakāle sahajātādhipati, majjhe tīsupi sahajātādhipati = အတွင်းပိုင်း သဘောတရားသည် ပြင်ပ သဘောတရားအား သွားသည့် အခါ၌ အတူ ပေါ်ပေါက်သော အကြီးအမှူး၊ အလယ် သုံးခုလုံး၌ အတူ ပေါ်ပေါက်သော အကြီးအမှူး
ārammaṇapurejātampi vatthupurejātampi = အာရုံ ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်းလည်း၊ မှီရာ ဝတ္ထု ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်းလည်း
tiṇṇannaṃ kabaḷīkāro āhāro = သုံးခုတို့၌ လုတ်ပြု၍ စားရသော အာဟာရ
tiṇṇannaṃ rūpajīvitindriyaṃ = သုံးခုတို့၌ ရုပ် အသက်၏ စွမ်းရည်
paṭhame dvepi adhipatī, dvīsu sahajātādhipati = ပထမ၌ အကြီးအမှူး နှစ်ခုလုံး၊ နှစ်ခု၌ အတူ ပေါ်ပေါက်သော အကြီးအမှူး
sahajātavārepi… pañhāvārepi ekaṃ sappaccayakusalasadisaṃ = အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်၌လည်း… ပြဿနာအလိုက် ဖော်ပြချက်၌လည်း တစ်ခု အကြောင်း ရှိသော၊ ကုသိုလ် သဘောတရားနှင့် တူသည်
ārammaṇapurejātaṃyeva, ghaṭanā dve, ārammaṇapurejātampi vatthupurejātampi = အာရုံ ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်းသာ၊ ပေါင်းစပ်ချက် နှစ်ခု၊ အာရုံ ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်းလည်း၊ မှီရာ ဝတ္ထု ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်းလည်း
upādinnamūlake dve = ကံကြောင့် ဖြစ်သော သဘောတရားကို အခြေခံခြင်း၌ နှစ်ခု
anupādinnamūlake dve = ကံကြောင့် မဖြစ်သော သဘောတရားကို အခြေခံခြင်း၌ နှစ်ခု
noupādānamūlake tīṇi = စွဲလမ်းမှု မဟုတ်သော သဘောတရားကို အခြေခံခြင်း၌ သုံးခု
sahajātādhipati = အတူ ပေါ်ပေါက်သော အကြီးအမှူး
noupādānamūlake = စွဲလမ်းမှု မဟုတ်သော သဘောတရားကို အခြေခံခြင်း၌
lokiyalokuttaradukakusalasadisaṃ = လောကနှင့် သက်ဆိုင်ခြင်းနှင့် လောကကို ကျော်လွန်ခြင်း နှစ်မျိုးတွဲ၏ ကုသိုလ် သဘောတရားနှင့် တူသည်
lokiyadukaabyākatasadisaṃ = လောကနှင့် သက်ဆိုင်ခြင်း နှစ်မျိုးတွဲ၏ ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော သဘောတရားနှင့် တူသည်
upādānasampayuttamūlake tīṇi = စွဲလမ်းမှုနှင့် ယှဉ်တွဲသော သဘောတရားကို အခြေခံခြင်း၌ သုံးခု
upādānavippayutte ekaṃ = စွဲလမ်းမှုနှင့် ကင်းကွာသော သဘောတရား၌ တစ်ခု
imaṃ gamanaṃ upādānadukaakusalasadisaṃ = ဤ သွားပုံသည် စွဲလမ်းမှု နှစ်မျိုးတွဲ၏ အကုသိုလ် သဘောတရားနှင့် တူသည်
idha pana hetupaccayā idaṃ nānaṃ = ဤနေရာ၌ကား အမြစ်ဟူသော အကြောင်း၌ ဤသည် ကွဲပြားချက် ဖြစ်သည်
lokiyadukakusalasadisaṃ = လောကနှင့် သက်ဆိုင်ခြင်း နှစ်မျိုးတွဲ၏ ကုသိုလ် သဘောတရားနှင့် တူသည်
sahajātavārampi… pañhāvārampi sabbattha vitthāretabbaṃ = အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း… ပြဿနာအလိုက် ဖော်ပြချက်လည်း နေရာတိုင်း၌ အကျယ် ချဲ့ရမည်
majjhe tīṇi sahajātādhipati = အလယ်၌ သုံးခုသည် အတူ ပေါ်ပေါက်သော အကြီးအမှူး
kilesadukaakusalasadisaṃ = ကိလေသာ နှစ်မျိုးတွဲ၏ အကုသိုလ် သဘောတရားနှင့် တူသည်
sahajātavārepi… pañhāvārepi vitthāretabbaṃ = အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်၌လည်း… ပြဿနာအလိုက် ဖော်ပြချက်၌လည်း အကျယ် ချဲ့ရမည်
dassane ekaṃ = သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ရမည့် သဘောတရား၌ တစ်ခု
nadassane dve = သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ရမည် မဟုတ်သော သဘောတရား၌ နှစ်ခု
dassanena pahātabbamūlakaṃ ekaṃ, nadassane dve, ārammaṇādhipati, sahajātādhipati, ekārammaṇādhipati = သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ရမည့် သဘောတရားကို အခြေခံခြင်း၌ တစ်ခု၊ သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ရမည် မဟုတ်သော သဘောတရား၌ နှစ်ခု၊ အာရုံ အကြီးအမှူး၊ အတူ ပေါ်ပေါက်သော အကြီးအမှူး၊ အာရုံ အကြီးအမှူး တစ်ခု
dassanamūlakaṃ ekaṃ = သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ရမည့် သဘောတရားကို အခြေခံခြင်း၌ တစ်ခု
nadassane ekaṃ = သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ရမည် မဟုတ်သော သဘောတရား၌ တစ်ခု
dassanena pahātabbadukaakusalasadisaṃ = သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ခြင်း နှစ်မျိုးတွဲ၏ အကုသိုလ် သဘောတရားနှင့် တူသည်
ghaṭane ekaṃ = ပေါင်းစပ်ချက်၌ တစ်ခု
dassanena pahātabbahetukadukaakusalasadisaṃ = သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ရမည့် အမြစ် နှစ်မျိုးတွဲ၏ အကုသိုလ် သဘောတရားနှင့် တူသည်
heṭṭhā tīsu sahajātādhipati, avitakke ekaṃ, sahajātādhipati = အထက် သုံးခု၌ အတူ ပေါ်ပေါက်သော အကြီးအမှူး၊ စတင်ကြံစည်မှု မရှိသော သဘောတရား၌ တစ်ခု၊ အတူ ပေါ်ပေါက်သော အကြီးအမှူး
yathā kusalattike pañhāvāraṃ, evaṃ vitthāretabbaṃ = ကုသိုလ် သုံးမျိုးတွဲ၌ ပြဿနာအလိုက် ဖော်ပြချက်ကဲ့သို့ ထိုနည်းတူ အကျယ် ချဲ့ရမည်
yathā kusalattike pañhāvāraṃ evaṃ vitthāretabbaṃ = ကုသိုလ် သုံးမျိုးတွဲ၌ ပြဿနာအလိုက် ဖော်ပြချက်ကဲ့သို့ ထိုနည်းတူ အကျယ် ချဲ့ရမည်
savitakkadukakusalasadisaṃ = စတင်ကြံစည်မှု ရှိခြင်း နှစ်မျိုးတွဲ၏ ကုသိုလ် သဘောတရားနှင့် တူသည်
savitakkadukaakusalasadisaṃ = စတင်ကြံစည်မှု ရှိခြင်း နှစ်မျိုးတွဲ၏ အကုသိုလ် သဘောတရားနှင့် တူသည်
savitakkadukaabyākatasadisaṃ = စတင်ကြံစည်မှု ရှိခြင်း နှစ်မျိုးတွဲ၏ ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော သဘောတရားနှင့် တူသည်
cattāri sahajātādhipati = လေးခုသည် အတူ ပေါ်ပေါက်သော အကြီးအမှူး
kusalasadisaṃ = ကုသိုလ် သဘောတရားနှင့် တူသည်
kusalampi akusalampi abyākatampi sappītikadukasadisaṃ = ကုသိုလ် သဘောတရားလည်း၊ အကုသိုလ် သဘောတရားလည်း၊ ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော သဘောတရားလည်း ပီတိ ရှိခြင်း နှစ်မျိုးတွဲနှင့် တူသည်
akusalaṃ dhammaṃ paṭicca… paccanīye nahetuyā ekaṃ = အကုသိုလ် သဘောတရားကို မှီ၍… အငြင်းပြ ပုံစံ၌ အမြစ်ဟူသော အကြောင်း မဟုတ်ခြင်း၌ တစ်ခု
abyākataṃ dhammaṃ paṭicca… paccanīye nahetuyā nava… najhāne cha, kātabbā = ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော သဘောတရားကို မှီ၍… အငြင်းပြ ပုံစံ၌ အမြစ်ဟူသော အကြောင်း မဟုတ်ခြင်း၌ ကိုးခု… ဈာန်ဟူသော အကြောင်း မဟုတ်ခြင်း၌ ခြောက်ခု၊ ပြုရမည်
paccanīye pañhāvāre kusalākusale indriye jhāne cha, pañhāvāre abyākate nava = အငြင်းပြ ပုံစံ၌ ပြဿနာအလိုက် ဖော်ပြချက်၌ ကုသိုလ်နှင့် အကုသိုလ်၌ စွမ်းရည်ဟူသော အကြောင်း၌ ဈာန်ဟူသော အကြောင်း၌ ခြောက်ခု၊ ပြဿနာအလိုက် ဖော်ပြချက်၌ ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော သဘောတရား၌ ကိုးခု
sappītikadukasadisaṃ = ပီတိ ရှိခြင်း နှစ်မျိုးတွဲနှင့် တူသည်
upekkhāti nānāupekkhā abyākate = ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော သဘောတရား၌ ဥပေက္ခာဟူသည် အမျိုးမျိုးသော ဥပေက္ခာ
paccanīye nahetuyā nava, najhāne cha = အငြင်းပြ ပုံစံ၌ အမြစ်ဟူသော အကြောင်း မဟုတ်ခြင်း၌ ကိုးခု၊ ဈာန်ဟူသော အကြောင်း မဟုတ်ခြင်း၌ ခြောက်ခု
evaṃ sabbattha akusalaṃ vitthāretabbaṃ = ဤသို့ နေရာတိုင်း၌ အကုသိုလ် သဘောတရားကို အကျယ် ချဲ့ရမည်
sappītikadukaabyākatasadisaṃ = ပီတိ ရှိခြင်း နှစ်မျိုးတွဲ၏ ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော သဘောတရားနှင့် တူသည်
pañhāvāre kusalākusale indriye jhāne cha, abyākate nava = ပြဿနာအလိုက် ဖော်ပြချက်၌ ကုသိုလ်နှင့် အကုသိုလ်၌ စွမ်းရည်ဟူသော အကြောင်း၌ ဈာန်ဟူသော အကြောင်း၌ ခြောက်ခု၊ ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော သဘောတရား၌ ကိုးခု
kāmāvacare ekaṃ = ကာမဘုံနှင့် ဆိုင်သော သဘောတရား၌ တစ်ခု
nakāmāvacare dve = ကာမဘုံနှင့် ဆိုင်သည် မဟုတ်သော သဘောတရား၌ နှစ်ခု
kāmāvacare dve = ကာမဘုံနှင့် ဆိုင်သော သဘောတရား၌ နှစ်ခု
nakāmāvacare ekaṃ = ကာမဘုံနှင့် ဆိုင်သည် မဟုတ်သော သဘောတရား၌ တစ်ခု
nakāmāvacare tīṇi = ကာမဘုံနှင့် ဆိုင်သည် မဟုတ်သော သဘောတရား၌ သုံးခု
kāmāvacare sahajātādhipatiyeva = ကာမဘုံနှင့် ဆိုင်သော သဘောတရား၌ အတူ ပေါ်ပေါက်သော အကြီးအမှူးသာ
rūpāvacare ekaṃ = သိမ်မွေ့သော ရုပ်ဘုံနှင့် ဆိုင်သော သဘောတရား၌ တစ်ခု
sahajātādhipatiyeva = အတူ ပေါ်ပေါက်သော အကြီးအမှူးသာ
narūpāvacare dve = သိမ်မွေ့သော ရုပ်ဘုံနှင့် ဆိုင်သည် မဟုတ်သော သဘောတရား၌ နှစ်ခု
yathā kāmāvacaradukaabyākatasadisaṃ, ettakāyeva pañhā heṭṭhuparikaṃ parivattanti = ကာမဘုံနှင့် ဆိုင်ခြင်း နှစ်မျိုးတွဲ၏ ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော သဘောတရားနှင့် တူသည့်အတိုင်း၊ ဤမျှသော ပြဿနာများသာ အောက်နှင့် အထက် လှည့်ပြောင်းကြသည်
arūpāvacaramūle dve = ရုပ်မရှိသော ဘုံနှင့် ဆိုင်သော သဘောတရားကို အခြေခံခြင်း၌ နှစ်ခု
naarūpāvacare ekaṃ = ရုပ်မရှိသော ဘုံနှင့် ဆိုင်သည် မဟုတ်သော သဘောတရား၌ တစ်ခု
arūpāvacaramūle tīṇi = ရုပ်မရှိသော ဘုံနှင့် ဆိုင်သော သဘောတရားကို အခြေခံခြင်း၌ သုံးခု
naarūpe ekaṃ = ရုပ်မရှိသော ဘုံနှင့် ဆိုင်သည် မဟုတ်သော သဘောတရား၌ တစ်ခု
niyate sahajātādhipati, dutiye ārammaṇādhipati sahajātādhipati = ကျိန်းသေသော သဘောတရား၌ အတူ ပေါ်ပေါက်သော အကြီးအမှူး၊ ဒုတိယ၌ အာရုံ အကြီးအမှူး၊ အတူ ပေါ်ပေါက်သော အကြီးအမှူး
sahajātavārampi… pañhāvārampi sabbattha vitthāretabbaṃ lokiyadukaabyākatasadisaṃ = အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း… ပြဿနာအလိုက် ဖော်ပြချက်လည်း နေရာတိုင်း၌ လောကနှင့် သက်ဆိုင်ခြင်း နှစ်မျိုးတွဲ၏ ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော သဘောတရားနှင့် တူအောင် အကျယ် ချဲ့ရမည်
sahajātavārepi… pañhāvārepi vitthāretabbo = အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်၌လည်း… ပြဿနာအလိုက် ဖော်ပြချက်၌လည်း အကျယ် ချဲ့ရမည်
sabbattha vitthāretabbaṃ = နေရာတိုင်း၌ အကျယ် ချဲ့ရမည်
sahajātavārepi… pañhāvārepi sabbattha vitthāretabbo = အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်၌လည်း… ပြဿနာအလိုက် ဖော်ပြချက်၌လည်း နေရာတိုင်း၌ အကျယ် ချဲ့ရမည်
sahajātavārepi … pañhāvārepi sabbattha vitthāretabbo = အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်၌လည်း … ပြဿနာအလိုက် ဖော်ပြချက်၌လည်း နေရာတိုင်း၌ အကျယ် ချဲ့ရမည်
