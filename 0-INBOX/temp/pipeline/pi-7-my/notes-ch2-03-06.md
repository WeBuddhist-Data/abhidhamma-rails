# pi-7 (Paṭṭhāna) Burmese zero-shot: 2-03 dassanenapahātabbattika, 2-04 dassanenapahātabbahetukattika, 2-05 ācayagāmittika, 2-06 sekkhattika — notes

Files: `AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters/` 2-03-dassanenapahatabbattika.md,
2-04-dassanenapahatabbahetukattika.md, 2-05-acayagamittika.md, 2-06-sekkhattika.md. Translated from the Pāli only (no
Burmese translation or nissaya opened, no web search, `language-priority/` not opened). Meaning cross-checked only against
the English pi-7 zero-shot (a few unclear notes). Generator: `make_ch2-03-06.py`. Check: `check_ch2-03-06.py` (adapted
from check_ch1-03-05.py + chk_mutate.py). No file of the sample, of 1-01, of 1-03 … 1-05 or of 2-01 … 2-02 was edited.

## Status (all pass, 2026-11-23)
| file | segments | lines | check_chapter_ids | check_text (pe, scratch chk-pe/ch2-03-06/) | check_marks | check_ch2-03-06 |
|---|---|---|---|---|---|---|
| 2-03-dassanenapahatabbattika.md | 215 | 380 | OK | OK | OK | OK |
| 2-04-dassanenapahatabbahetukattika.md | 222 | 476 | OK | OK | OK | OK |
| 2-05-acayagamittika.md | 180 | 337 | OK | OK | OK | OK |
| 2-06-sekkhattika.md | 174 | 310 | OK | OK | OK | OK |

check_ch2-03-06 (`--sample --pe --mutate`): 1503 lines × (structure, polarity, conditions, term order, numbers), 2692
sentences for identity (with the approved sample), 59 table values: **0 mismatches**. Reuse test: **89 / 89** pi-1 … pi-6
values identical wherever their Pāli occurs; sentences also in pi-1 … pi-6: **702 / 702**. Sample identity: 1-00 and
1-02 regenerated through this generator = the files on disk (raw and with prep()). Mutation test: **9 / 9** planted
errors caught (count, polarity, term order, condition, khandha count, term, digits, note, shared count).
`make_ch2-03-06.py --regress`: sample identical; 1-01 identical except the one known line (see Harmonise, 1).
Identity with the finished groups (informational): 98 / 101 sentences that also occur in 1-01 / 1-03 … 1-05 are
identical; the 3 others are listed under Harmonise.

## Engines (how the frames of 1-01 and 1-03 … 1-05 are both used)
- 1-01 and 1-03 … 1-05 cannot be loaded on the same module: each wraps my7_formulas' functions, and stacked they change
  each other's output (tested: the sample itself changed). So:
  - PRIMARY: my7_formulas + make_sample + make_ch1-01.py (its setup_*() frames register on import);
  - FALLBACK, per sentence unit: an isolated second copy of my7_formulas + make_sample with make_ch1-03-05.py loaded on
    it (its tables and wrappers act only on that copy). A unit the primary cannot match is tried there, after
    make_ch1-03-05's prep(). 49 units went that way (2-03 14, 2-04 1, 2-05 11, 2-06 23), mostly «X-o adhipati …»,
    «vipākaṃ X ekaṃ khandhaṃ …», «bāhiraṃ… asaññasattānaṃ …» fragments.
  - the 1-03 … 1-05 pañhā lexicon entries that 1-01 lacks are copied into the primary (setdefault: 1-01 values win).
- Only the chapter's own triad is active while it is translated (the 2-03 stems are a prefix of the 2-04 stems).

## Triad terms (pi-1 Mātikā ^1-M1-8 … ^1-M1-11, read from the FINAL rails by W())
- dassanena pahātabba = သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ရမည့်; bhāvanāya pahātabba = ဘာဝနာ ပွားများခြင်းဖြင့် ပယ်ရမည့်;
  nevadassanena nabhāvanāya pahātabba = သစ္စာကို မြင်ခြင်းဖြင့်လည်း ပယ်ရမည် မဟုတ်၊ ဘာဝနာ ပွားများခြင်းဖြင့်လည်း ပယ်ရမည် မဟုတ်သော
  (pi-1 spells «neva dassanena na bhāvanāya», pi-7 «nevadassanena nabhāvanāya»: same Burmese)
- dassanena pahātabbahetuka = သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ရမည့် အမြစ် ရှိသော; bhāvanāya pahātabbahetuka = ဘာဝနာ ပွားများခြင်းဖြင့်
  ပယ်ရမည့် အမြစ် ရှိသော; nevadassanena nabhāvanāya pahātabbahetuka = သစ္စာကို မြင်ခြင်းဖြင့်လည်း ပယ်ရမည့် အမြစ် ရှိသည် မဟုတ်၊
  ဘာဝနာ ပွားများခြင်းဖြင့်လည်း ပယ်ရမည့် အမြစ် ရှိသည် မဟုတ်သော
- ācayagāmī = စုပုံခြင်းဆီသို့ ဦးတည်သော; apacayagāmī = လျော့ပါးခြင်းဆီသို့ ဦးတည်သော; nevācayagāmināpacayagāmī =
  စုပုံခြင်းဆီသို့ ဦးတည်သည်လည်း မဟုတ်၊ လျော့ပါးခြင်းဆီသို့ ဦးတည်သည်လည်း မဟုတ်သော
- sekkha = ကျင့်ကြံဆဲသူ၏; asekkha = ကျင့်ကြံမှု ပြီးဆုံးသူ၏; nevasekkhanāsekkha = ကျင့်ကြံဆဲသူ၏လည်း မဟုတ်၊ ကျင့်ကြံမှု
  ပြီးဆုံးသူ၏လည်း မဟုတ်သော (in 2-05 «sekkhā maggaṃ upanissāya …» are persons: the 1-01 lexicon «ကျင့်ကြံဆဲသူ»)
- A term cut short by «…» («bhāvanāya…», «nevadassanena…», «nevadassanena nabhāvanāya…») gets the full term (the
  Pāli abbreviates the same term; the «…» follows). «X-ādhipati» = «X-o adhipati» (as 1-03 … 1-05 «vipāko adhipati»):
  «သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ရမည့် အကြီးအမှူး». A term named inside a note = term + သဘောတရား (the chapter's own:
  «dassanena sadisaṃ» = «သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ရမည့် [အမြစ် ရှိသော] သဘောတရားနှင့် တူသည်»; «sekkhamūlake tīṇi» =
  «ကျင့်ကြံဆဲသူ၏ သဘောတရားကို အခြေခံခြင်း၌ သုံးခု»; «ācayagāminayena kātabbaṃ» = «စုပုံခြင်းဆီသို့ ဦးတည်သော သဘောတရား၏
  နည်းအတိုင်း ပြုရမည်»).
- The -in stem ācayagāmī: prep() reads its endings in memory as the a-stem endings the frames know (ī -> o, iṃ -> aṃ,
  issa -> assa, iñca -> añca, īnaṃ -> ānaṃ, iyā -> āya); the Burmese term does not depend on the ending. Variants in
  braces are not touched.

## New recurring terms and phrases (Pāli = Burmese)
Dassanenapahātabbattikaṃ = သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ခြင်း သုံးမျိုးတွဲ
Dassanenapahātabbahetukattikaṃ = သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ရမည့် အမြစ် သုံးမျိုးတွဲ
Ācayagāmittikaṃ = စုပုံခြင်းဆီသို့ ဦးတည်ခြင်း သုံးမျိုးတွဲ
Sekkhattikaṃ = ကျင့်ကြံဆဲသူ သုံးမျိုးတွဲ
dassanattika (in notes) = သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ခြင်း သုံးမျိုးတွဲ
vicikicchāsahagataṃ / -ā / -ānaṃ / -assa / -e / -o = ယုံမှားမှုနှင့်အတူ ဖြစ်သော (pi-1; module value)
uddhaccasahagataṃ / -ā / -ānaṃ / -assa / -e / -o = ယောက်ယက်ခတ်မှုနှင့်အတူ ဖြစ်သော (pi-1; module value)
vicikicchāsahagataṃ uddhaccasahagataṃ mohaṃ = ယုံမှားမှုနှင့်အတူ ဖြစ်သော၊ ယောက်ယက်ခတ်မှုနှင့်အတူ ဖြစ်သော မောဟ (pi-1 ^1-1443)
moho / mohaṃ / mohassa = မောဟ (module)
khandhā ca moho ca = အစုအဝေးလည်းကောင်း၊ မောဟလည်းကောင်း
khandhe ca mohañca = အစုအဝေးတို့ကိုလည်းကောင်း၊ မောဟကိုလည်းကောင်း
khandhānaṃ mohassa ca = အစုအဝေးတို့အားလည်းကောင်း၊ မောဟအားလည်းကောင်း (prep: «A ca B ca», as 1-03 … 1-05 «khandhā vatthu ca»)
āvajjanāya mohassa ca = စိတ်ညွတ်ခြင်းအားလည်းကောင်း၊ မောဟအားလည်းကောင်း
senāsanaṃ moho ca = အိပ်ရာ နေရာလည်းကောင်း၊ မောဟလည်းကောင်း
sampayuttakā = ယှဉ်တွဲသော (module value of sampayuttakānaṃ)
purimo purimo = ရှေးရှေး; pacchimassa pacchimassa = နောက်နောက် (module values)
sakabhaṇḍe chandarāgo parabhaṇḍe chandarāgassa = မိမိ ပစ္စည်း၌ ဖြစ်သော ဆန္ဒရာဂသည် သူတစ်ပါး ပစ္စည်း၌ ဖြစ်သော ဆန္ဒရာဂအား
sakapariggahe … parapariggahe … = မိမိ သိမ်းပိုက်ခြင်း၌ ဖြစ်သော ဆန္ဒရာဂသည် သူတစ်ပါး သိမ်းပိုက်ခြင်း၌ ဖြစ်သော ဆန္ဒရာဂအား
chandarāga = ဆန္ဒရာဂ (pi-2 ^ jhānavibhaṅga); pariggaha = သိမ်းပိုက်ခြင်း (pi-2); bhaṇḍa = ပစ္စည်း; saka- = မိမိ; para- = သူတစ်ပါး
ajjhattikā (mahābhūtā) = အတွင်းပိုင်း ဖြစ်သော (pi-1)
uposathakammaṃ = ဥပုသ် စောင့်ထိန်းခြင်း (pi-2 «ဥပုသ်ကို စောင့်ထိန်း၍»)
abhiññaṃ = ထူးကဲစွာ သိခြင်း (module); samāpattiṃ = သမာပတ် (1-03 … 1-05); pubbe = ရှေးက (module)
kāyikaṃ… sukhaṃ… (the pair cut by «…») = ကိုယ်ပိုင်းဆိုင်ရာ… သာယာမှု…
kaṭattārūpānaṃ = ကံ ပြုခဲ့သောကြောင့် ဖြစ်သော ရုပ်တို့ (module noun, genitive added)
ekavīsa = နှစ်ဆယ့်တစ်ခု (short form of ekavīsati, 1-03 … 1-05)
anantare samanantare … dve (one count for several conditions) = Aဟူသော အကြောင်း၌၊ Bဟူသော အကြောင်း၌ … နှစ်ခု
X sabbattha N = Xဟူသော အကြောင်း၌ … နေရာတိုင်း၌ N (1-01 SABBATTHA)
variant «ācayagāmi (sī. syā.) evamuparipi» = {စာလုံးပေါင်းကွဲ (Sī., Syā.): ācayagāmi၊ နောက်တွင်လည်း ဤနည်းတူ} (pi-1 … pi-6 rails form)
variant «nevasekhānāsekho (sī.), nevasekkhānāsekkho (syā. ka.)» = {စာလုံးပေါင်းကွဲ (Sī.): nevasekhānāsekho၊ (Syā., Ka.): nevasekkhānāsekkho} (pi-1 rails form)

### Words of the notes (NEW unless marked)
evaṃ (alone: thus) = ဤသို့ (as 1-03 … 1-05 «evaṃ kātūna» «ဤသို့ ပြု၍»; the sample's «ထိုနည်းတူ» stays for «yathā … evaṃ»)
anumajjantena = ပြန်လည် စိစစ်လျက်
ñatvā = နားလည်၍
visuṃ = သီးခြား
X-nayena = X၏ နည်းအတိုင်း; dassitanayena = ပြထားသော နည်းအတိုင်း
gamanaṃ = သွားပုံ
sabbe / sabbepi = အားလုံး
upadhāretvā = သေချာ စဉ်းစား၍
na likhitā = မရေးထားသော
pāḷiyaṃ = ပါဠိတော်၌
ninnānaṃ = ကွဲပြားမှု မရှိ
pavattipaṭisandhi = ဘဝ ဖြစ်စဉ်၌လည်း၊ ပဋိသန္ဓေ၌လည်း
sahetukā (ime sahetukā kātabbā) = အမြစ် ရှိသည်များ
pahātabbaṃ (to be left out, in a note) = ပယ်ရမည်
niyāmetabbaṃ = သတ်မှတ်ရမည်
missagataṃ = ရောစပ်ချက်; missakapañhā = ရောစပ် ပြဿနာ (1-01 MISSAKA)
gaṇentena = ရေတွက်သူသည်; gaṇentānaṃ = ရေတွက်သူတို့၏
byañjanena na samenti = စကားလုံးနှင့် မညီကြ
pākaṭā honti = ထင်ရှားကြသည်
yadi saṃsayo uppajjati = သံသယ ဖြစ်ပေါ်သည်ဆိုလျှင် (keeps «uppajjati» = «ဖြစ်ပေါ်သည်», reuse test)
pekkhitabbaṃ = ကြည့်ရမည်
evamuparipi = နောက်တွင်လည်း ဤနည်းတူ (pi-1 … pi-6 rails variant note)
X-sadisaṃ / -sadiso = Xနှင့် တူသည်; X-sadisā / -sadisāni = Xနှင့် တူကြသည် (1-01); X-sadisaṃ kātabbaṃ = Xနှင့် တူအောင် ပြုရမည် (1-01)
Xvāro Yvārasadiso = X အလိုက် ဖော်ပြချက်သည် Y အလိုက် ဖော်ပြချက်နှင့် တူသည်; paccayasadiso (= the paccayavāra) = အကြောင်းပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူ…
bare stem «naārammaṇasadisaṃ» = အာရုံ မဟုတ်ခြင်းနှင့် တူသည် (bare name + the module's negation)
N pañhā = ပြဿနာ N; N kātabbā = Nကို ပြုရမည်; N pañhā paripuṇṇā = ပြဿနာ N ပြည့်စုံသည်; dvepi = နှစ်ခုလုံး; cattāripi = လေးခုလုံး

### Whole notes (hand-written, built from the words above)
(evaṃ gaṇetabbaṃ) = (ဤသို့ ရေတွက်ရမည်)
(evaṃ anumajjantena gaṇetabbaṃ) = (ဤသို့ ပြန်လည် စိစစ်လျက် ရေတွက်ရမည်)
(imāni padāni anumajjantena anulomaṃ gaṇetabbaṃ) = (ဤ ပုဒ်တို့ကို ပြန်လည် စိစစ်လျက် အဟုတ်ပြ ပုံစံကို ရေတွက်ရမည်)
(ñatvā gaṇetabbaṃ) = (နားလည်၍ ရေတွက်ရမည်)
(paṭisandhi natthi) = (ပဋိသန္ဓေ မရှိ); (vipākapaṭisandhi natthi) = (ကံ၏ အကျိုး ဖြစ်သော ပဋိသန္ဓေ မရှိ)
(paṭisandhi natthi, vipākañca) = (ပဋိသန္ဓေ မရှိ၊ ကံ၏ အကျိုးလည်း) (elliptic as the Pāli)
(paṭisandhikkhaṇe natthi) = (ပဋိသန္ဓေ နေသော ခဏ၌ မရှိ)
(paripuṇṇaṃ kātabbaṃ) = (ပြည့်စုံအောင် ပြုရမည်)
(mahābhūtā / sabbe mahābhūtā / sabbepi mahābhūtā kātabbā) = (မူလဓာတ်ကြီးတို့ကို / မူလဓာတ်ကြီး အားလုံးကို / … အားလုံးကိုလည်း ပြုရမည်)
(cittasamuṭṭhānampi kaṭattārūpampi upādārūpampi natthi) = (စိတ်မှ ဖြစ်ပေါ်လာသော ရုပ်လည်း၊ ကံ ပြုခဲ့သောကြောင့် ဖြစ်သော ရုပ်လည်း၊ မူလဓာတ်ကြီးတို့ကို မှီ၍ ဖြစ်သော ရုပ်လည်း မရှိ)
(sabbe ghaṭanā kātabbā) = (ပေါင်းစပ်ချက် အားလုံးကို ပြုရမည်); (ghaṭanā paripuṇṇā) = (ပေါင်းစပ်ချက် ပြည့်စုံသည်)
(visuṃ ghaṭanā natthi) = (သီးခြား ပေါင်းစပ်ချက် မရှိ); (cattāripi hi visuṃ ghaṭanā natthi) = (လေးခုလုံး၌ပင် သီးခြား ပေါင်းစပ်ချက် မရှိ)
(paṭisandhipi mahābhūtāpi sabbe) = (ပဋိသန္ဓေလည်း၊ မူလဓာတ်ကြီးလည်း အားလုံး)
(moho kātabbo) = (မောဟကို ပြုရမည်); (ime sahetukā kātabbā) = (ဤတို့ကို အမြစ် ရှိသည်များအဖြစ် ပြုရမည်)
(ajjhattikā ca asaññasattānañca mahābhūtā) = (အတွင်းပိုင်း ဖြစ်သော မူလဓာတ်ကြီးတို့လည်းကောင်း၊ အသညသတ်တို့၏ မူလဓာတ်ကြီးတို့လည်းကောင်း)
(ajjhattikā mahābhūtā ca āhārasamuṭṭhānañca) = (အတွင်းပိုင်း ဖြစ်သော မူလဓာတ်ကြီးတို့လည်းကောင်း၊ အာဟာရမှ ဖြစ်ပေါ်လာသော ရုပ်လည်းကောင်း) (noun «ရုပ်» supplied)
(Āsevanamūlake vuṭṭhānassapi āvajjanāyapi pahātabbaṃ, …) = (အလေ့အကျင့် ပြုခြင်းဟူသော အကြောင်းကို အခြေခံခြင်း၌ ထမြောက်ခြင်း စိတ်ကိုလည်း၊ စိတ်ညွတ်ခြင်းကိုလည်း ပယ်ရမည်၊ …)
("uddhacca"nti niyāmetabbaṃ) = (“ယောက်ယက်ခတ်မှု”ဟု သတ်မှတ်ရမည်) (the Pāli has the quote marks)
(Idha sahajātaṃ, purejātaṃ, missagataṃ atthi, pāḷiyaṃ kātabbaṃ. Gaṇanāya upadhāretvā gaṇetabbaṃ.) = (ဤနေရာ၌ အတူ ပေါ်ပေါက်ခြင်း၊ ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်း၊ ရောစပ်ချက် ရှိသည်၊ ပါဠိတော်၌ ပြုရမည်။ ရေတွက်ချက်၌ သေချာ စဉ်းစား၍ ရေတွက်ရမည်။)
(Idhāpi ārammaṇapaccayā upanissayapaccayā atthi, pāḷiyaṃ natthi. Gaṇentena upadhāretvā gaṇetabbaṃ.) = (ဤနေရာ၌လည်း အာရုံဟူသော အကြောင်း၊ အားကြီးသော အမှီဟူသော အကြောင်း ရှိသည်၊ ပါဠိတော်၌ မရှိ။ ရေတွက်သူသည် သေချာ စဉ်းစား၍ ရေတွက်ရမည်။)
(Idhāpi "sahajātaṃ, purejātaṃ" yaṃ missakapañhā atthi, pāḷiyaṃ kātabbaṃ) = (ဤနေရာ၌လည်း “အတူ ပေါ်ပေါက်ခြင်း၊ ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်း”ဟူသော ရောစပ် ပြဿနာ ရှိသည်၊ ပါဠိတော်၌ ပြုရမည်)
(idhāpi ārammaṇaupanissayā atthi) = (ဤနေရာ၌လည်း အာရုံဖြင့် အားကြီးသော အမှီ ရှိသည်)
(Idhāpi sahajātaṃ, purejātaṃ atthi. Ye te pañhā na likhitā, te pāḷiyaṃ gaṇentānaṃ byañjanena na samenti. Te pāḷiyaṃ na likhitā gaṇanā pākaṭā honti. Yadi saṃsayo uppajjati, anulome atthipaccaye pekkhitabbaṃ.) = (ဤနေရာ၌လည်း အတူ ပေါ်ပေါက်ခြင်း၊ ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်း ရှိသည်။ မရေးထားသော ထိုပြဿနာတို့သည် ပါဠိတော်၌ ရေတွက်သူတို့၏ စကားလုံးနှင့် မညီကြ။ ပါဠိတော်၌ မရေးထားသော ထိုရေတွက်ချက်တို့သည် ထင်ရှားကြသည်။ သံသယ ဖြစ်ပေါ်သည်ဆိုလျှင် အဟုတ်ပြ ပုံစံ၌ ရှိခြင်းဟူသော အကြောင်း၌ ကြည့်ရမည်။)
(Sahajātapaccaye paṭiccavāre sahajātavārasadisā nava pañhā. Aññamaññapaccaye paṭiccavāre aññamaññasadisaṃ tīṇi. Nissayapaccaye paccayavāre nissayavārasadisaṃ. Cattāripi hi visuṃ ghaṭanā natthi. Terasa pañhā.) = (အတူ ပေါ်ပေါက်ခြင်းဟူသော အကြောင်း၌ မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်၌ အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူသော ပြဿနာ ကိုးခု။ … ပြဿနာ ဆယ့်သုံးခု။)
(Nissayapaccaye kusalattike nissayapaccayasadisaṃ, terasa pañhā) = (အမှီဟူသော အကြောင်း၌ ကုသိုလ် သုံးမျိုးတွဲ၌ အမှီဟူသော အကြောင်းနှင့် တူသည်၊ ပြဿနာ ဆယ့်သုံးခု)
(ekaṃ, paripuṇṇaṃ, sekkhañca, nevasekkhanāsekkhañca, ghaṭanā paripuṇṇā, dvepi kātabbā. Nava) = (တစ်ခု၊ ပြည့်စုံသည်၊ ကျင့်ကြံဆဲသူ၏ သဘောတရားလည်းကောင်း၊ … သဘောတရားလည်းကောင်း၊ ပေါင်းစပ်ချက် ပြည့်စုံသည်၊ နှစ်ခုလုံးကို ပြုရမည်။ ကိုးခု)

## Engine extensions (in memory, in make_ch2-03-06.py)
- chain(): one count for a run of conditions («anantare samanantare sahajāte aññamaññe dve», «kamme sabbattha tīṇi»).
- notes: make_ch1-01's note_body / note_clause extended (my_clause: X-sadisaṃ with a place / subject / kātabbaṃ /
  vibhajitabbaṃ / gamanaṃ, sections, triads, terms; counts with pañhā / kātabbā; X-mūlake / -ghaṭanesu N; X-nayena);
  every note of a chapter is also registered for the chains, and the closing half of a note cut by a sentence end
  («Ninnānaṃ)…», «Nava) …», «Tisso pañhā, …)») is registered as its own note piece.
- lex(): a fragment that starts with a post word («senāsanaṃ… upanissāya dānaṃ deti») gets the post word without its
  «ကို» (the object is in the fragment before «…»); «dve khandhe ca…» (cut) takes the unit's link case inside the
  conjunct («အစုအဝေး နှစ်ပါးကြောင့်လည်းကောင်း…»).
- unit fallbacks after both engines: «… rūpaṃ.(2)» (no space before the digits, kept); a closing note half
  («Ajjhattikā … mahābhūtā).»); a variant between a term and its noun («nevasekkhanāsekkho {…} dhammo»: put right
  after the term); condition kinds after the condition without a dash («… atthipaccayena paccayo sahajātaṃ,
  purejātaṃ.»); a note in the middle of a unit (both sides as units); comma parts each on their own, joined by «၊».

## Harmonise (for the consistency pass)
1. 1-01 line 2237 «Uddhaccaṃ ārabbha uddhaccaṃ uppajjati» = «ယောက်ယက်ခတ်မှုသည်ကို အာရုံပြု၍ …» (a stray «သည်», 1-01 slip). These
   chapters have the same Pāli (2-03, 2-04) and give «ယောက်ယက်ခတ်မှုကို အာရုံပြု၍» (the 1-03 … 1-05 lexicon entry). It is the
   only line where `--regress` differs from 1-01 (declared in KNOWN_DIFF).
2. «asaññasattānaṃ»: 1-01 «အသညသတ်တို့၏» (28×), 1-03 … 1-05 «အသညသတ်တို့၌» (31×). These chapters use one form throughout,
   1-01's genitive (set in the fallback copy too), 58×.
3. Sentences also in 1-03 … 1-05 that differ (mine = 1-01's engine): «rūpāyatanaṃ cakkhuviññāṇassa…pe…
   phoṭṭhabbāyatanaṃ kāyaviññāṇassa purejātapaccayena paccayo» and «kabaḷīkāro āhāro imassa kāyassa…pe…
   rūpajīvitindriyaṃ …» (1-05 has «… နယ်ပယ်၊ မျက်စိ သိစိတ်တို့အား…», «… အာဟာရ၊ ဤကိုယ်တို့အား…», which reads the subject as a
   list; here «… နယ်ပယ်သည် မျက်စိ သိစိတ်အား…»); «sekkhā vā puthujjanā vā» = 1-01 «ကျင့်ကြံဆဲသူတို့သော်လည်းကောင်း၊ ပုထုဇဉ်တို့သော်လည်းကောင်း»
   (1-03 «…တို့ဖြစ်စေ၊ …တို့ဖြစ်စေ»).
4. Other 1-01 / 1-03 … 1-05 lexicon pairs where these chapters follow 1-01: pubbe suciṇṇāni «ရှေးက ကောင်းစွာ ကျင့်ခဲ့ဖူးသော
   အမှု»; kusalākusale niruddhe «… ချုပ်ငြိမ်းသောအခါ»; tadārammaṇatā «ထိုအာရုံကို အာရုံပြုသည့် အနေဖြင့်»; formless bases
   «… နယ်ပယ် ကုသိုလ်»; ṭhānāṭhānakosalla «… ကျွမ်းကျင်ခြင်း».
5. The coordinator's Sahajātā decision is kept by the 1-01 frames: the kind label «Sahajātā –» = «အတူ ပေါ်ပေါက်ခြင်း»; in the
   kamma section «အတူ ပေါ်ပေါက်သည့် ကံ».

## Unsure Pāli
- «(vipākapaṭisandhi natthi)» (2-03, āsevana): read as «no resultant rebirth» «ကံ၏ အကျိုး ဖြစ်သော ပဋိသန္ဓေ မရှိ» (English
  zero-shot the same).
- «(paṭisandhi natthi, vipākañca)»: «and [no] vipāka», left elliptic «ကံ၏ အကျိုးလည်း».
- «(Āsevanamūlake vuṭṭhānassapi āvajjanāyapi pahātabbaṃ …)»: pahātabbaṃ = «to be left out» «ပယ်ရမည်».
- «(pavattipaṭisandhi)»: «in the course of existence and at rebirth» «ဘဝ ဖြစ်စဉ်၌လည်း၊ ပဋိသန္ဓေ၌လည်း».
- «missagataṃ» «ရောစပ်ချက်»; «yaṃ missakapañhā atthi» «…ဟူသော ရောစပ် ပြဿနာ ရှိသည်».
- «Ye te pañhā na likhitā, te pāḷiyaṃ gaṇentānaṃ byañjanena na samenti» = «the questions not written do not agree in
  wording for those counting in the text» «… ရေတွက်သူတို့၏ စကားလုံးနှင့် မညီကြ».
- «ārammaṇūpanissayo, 51anantarūpanissayo, …» (2-04): «51» is a stray number in the source (a page number?); kept as
  written «51ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းဖြင့် အားကြီးသော အမှီ».
- «(sabbāni padāni vitthāretabbāni tīṇi, tīṇi)» kept in the Pāli order «… အကျယ် ချဲ့ရမည် သုံးခု၊ သုံးခု».

## Source slips (translated as written; normalised in memory only where a frame needs it; logged by the generator)
- 2-04 «Nevadassanena … pahātabbahetukaṃ dhammaṃ nevadassanena … dhammo uppajjati vippayuttapaccayā» (paccayavāra): the
  link word is missing; «paccayā» supplied («…ကြောင့်»).
- 2-04 «Bhāvanāya pahātabbahetukañca … dhammaṃ bhāvanāya pahātabbahetuko dhammo uppajjati hetupaccayā» (saṃsaṭṭhavāra):
  link missing; «saṃsaṭṭho» supplied («…နှင့် ရောနှောသော»).
- 2-04 «aññamaññe sattārasa nissaye»: spelling and a missing comma: read as «aññamaññe sattarasa, nissaye».
- 2-05 «Nevācayagāmīnāpacayagāmī» read as «Nevācayagāmināpacayagāmī» (same Burmese).
- 2-06 «maggapaccaya…», «aññamaññapaccaya…» (no «ā»), «upanissayapaccayena paccaya –» (no «o»): read as the usual forms.
- 2-03 «utusamuṭṭhāna…» read as «utusamuṭṭhānaṃ…»; 2-03 heading «Natthivigatāvigatapaccayā» (no hyphen) = the
  1-03 … 1-05 heading «Natthi-vigatāvigatapaccayā».
- 2-04 / 2-06 «….(1)», «.(2)» without a space: kept without a space.
