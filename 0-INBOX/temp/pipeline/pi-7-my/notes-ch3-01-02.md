# pi-7 3-01 hetugocchaka, 3-02 cūḷantaraduka: Burmese zero-shot notes

PROGRESS: DONE (2026-11-23). 3-01 (467 segments, 805 lines) and 3-02 (499 segments, 734 lines) written to
AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters/.
Checks (both chapters): check_chapter_ids OK; check_marks OK; check_text (pi-3-mr/check_text.py on a «…Pe…»-folded
copy in pi-7-my/chk-pe/ch3-01-02/, deleted afterwards; the same as check_text_pe7.py, which writes into and deletes
the shared chk-pe/, so it was not run as is) OK, dashes match; check_ch3-01-02.py 0 mismatches (S/P/C/O/N on 1539
lines, I 2537 sentences, T 95), reuse 89 / 89 terms + 618 / 618 sentences, --sample identical, --mutate 10 / 10;
make_ch3-01-02.py --regress: the sample (1-00, 1-02) and 2-03 … 2-06 regenerate identical through this engine.

## Files
- make_ch3-01-02.py: generator. IMPORTS make_ch2-03-06.py (as make_ch2-12-17 does) for its engine: PRIMARY
  my7_formulas + make_sample + make_ch1-01, FALLBACK per unit an isolated copy with make_ch1-03-05; nothing of
  another group is run or written. `--dev` lists unmatched skeletons in chk-ch3-01-02/dev.txt; `--regress`;
  `--out DIR` writes review copies (chk-ch3-01-02/out/).
- check_ch3-01-02.py: checker (adapted from check_ch2-03-06.py; own copy of the dyad terms, names and Pāli term
  regexes; the active dyad of each line from the Pāli dyad headings); `--sample --pe --mutate --groups`.
- chk-ch3-01-02/: my scratch (dev output, review copies, query scripts).

## How the dyads are run (for the later dyad chapters)
- A chapter holds several dyads: it is cut before each «###### Xdukaṃ» heading and each part is translated with only
  its own dyad active in TRIADS (F and FG); parts joined with one blank line (as the source).
- Non-a-stem terms become pseudo a-stem words before slotting (prep_dyad): hetu / nahetu «hetudk / nahetudk» (u-stem),
  rūpī / arūpī «rūpdk / arūpdk» (i-stem), «hetu ceva sahetuko ca» «hetusahetukdk», «sahetuko ceva na ca hetu»
  «sahetukanahetudk», «hetu ceva hetusampayutto ca» / «hetusampayutto ceva na ca hetu», «nahetu sahetuko /
  ahetuko» glued «nahetusahetuk / nahetuahetuk». The ending only gives the slot tail; the noun carries case.
- «hetu» is a dyad term only before a dhamma word (or coordinated with nahetu before one); otherwise the noun «အမြစ်»
  (root): «hetuṃ paṭicca sampayuttakā khandhā» «အမြစ်ကို မှီ၍ …». nahetu is always the term.
- Both members on one noun that is not dhamma («sanidassanañca anidassanañca … rūpaṃ», «kenaci viññeyyā ca kenaci
  naviññeyyā ca tayo khandhā», «sappaṭighassa ca appaṭighassa ca kāyassa»): one slot «A_B_both», Burmese the stacked
  «A၊ B N» (the pattern of 2-07 … 2-11 / 2-01 … 2-02 for two terms on one noun; H6). With dhamma the module's «A
  သဘောတရားနှင့် B သဘောတရား» stays.
- Coordination readings (in memory, for the parser; the Burmese «…လည်းကောင်း» per conjunct is the module's):
  «X ca sampayuttakā ca khandhā» = «X ca sampayuttakā khandhā ca»; «tayo khandhā adoso amoho ca …» / «dve mahābhūtā
  āpodhātu ca» = «… khandhā ca … ca» (as 1-03 … 1-05 «khandhā vatthu ca», 2-03 … 2-06 «khandhā moho ca»);
  «hetuñca nahetuñca khandhe» = «hetuñca nahetuṃ khandhe ca»; a term before «cittasamuṭṭhānañca rūpaṃ» takes its
  «ca» («T-añca cittasamuṭṭhānaṃ rūpaṃ»); «T-aṃ kaṭattā ca rūpaṃ» = «T-añca kaṭattārūpaṃ» (same Burmese).
- A term before an asyndetic rūpa list («anidassanaṃ cittasamuṭṭhānaṃ rūpaṃ kaṭattārūpaṃ upādārūpaṃ»): the term
  before the list, as the Pāli (np wrapper over make_ch1-01's list rule).
- Notes with condition / term / count words get a placeholder «(⁑d<i>)» (as 2-07 … 2-11's NOTEP).
- «Sahajātā –» outside the kamma section: the bare name «အတူ ပေါ်ပေါက်ခြင်း –»; in the kamma section «အတူ
  ပေါ်ပေါက်သည့် ကံ» (coordinator decision; both come from the engines). «Anulomaṃ.» (order) «အဟုတ်ပြ ပုံစံ။» (27 lines);
  «anulomaṃ» (mind moment) «လျော်ညီခြင်း စိတ်» (19). asaññasattānaṃ «အသညသတ်တို့၏» (1-01). No heinous deeds here.

## New terms and formulas (Pāli = Burmese)
### Dyad terms (pi-1 final ^1-M2-1 … ^1-M2-13, read with W())
hetu (dyad) = အမြစ် ဖြစ်သော; na hetu = အမြစ် မဟုတ်သော
sahetuka = အမြစ် ရှိသော; ahetuka = အမြစ် မရှိသော (= the sample's qualifier ahetuka)
hetusampayutta = အမြစ်နှင့် ယှဉ်တွဲသော; hetuvippayutta = အမြစ်နှင့် ကင်းကွာသော
hetu ceva sahetuko ca = အမြစ်လည်း ဖြစ်၊ အမြစ်လည်း ရှိသော; sahetuko ceva na ca hetu = အမြစ် ရှိသော်လည်း အမြစ် မဟုတ်သော
hetu ceva hetusampayutto ca = အမြစ်လည်း ဖြစ်၊ အမြစ်နှင့်လည်း ယှဉ်တွဲသော; hetusampayutto ceva na ca hetu = အမြစ်နှင့် ယှဉ်တွဲသော်လည်း အမြစ် မဟုတ်သော
nahetu sahetuko = အမြစ် မဟုတ်သော်လည်း အမြစ် ရှိသော (NEW; pi-1 ^1-M2-6 is not attributive)
nahetu ahetuko = အမြစ် မဟုတ်၊ အမြစ် မရှိသော (NEW; keeps the pi-2 «အမြစ် မရှိသော» of ahetuka for the reuse test)
sappaccaya / appaccaya = အကြောင်း ရှိသော / အကြောင်း မရှိသော
saṅkhata / asaṅkhata = ပြုပြင်ဖန်တီးထားသော / ပြုပြင်ဖန်တီးထားခြင်း မရှိသော
sanidassana / anidassana = မြင်နိုင်သော / မမြင်နိုင်သော
sappaṭigha / appaṭigha = ထိခိုက်မှု ရှိသော / ထိခိုက်မှု မရှိသော
rūpī / arūpī = ရုပ် ဖြစ်သော / ရုပ် မဟုတ်သော (= the module's rūpino / arūpino)
lokiya / lokuttara = လောကနှင့် သက်ဆိုင်သော / လောကကို ကျော်လွန်သော
kenaci viññeyya / kenaci na viññeyya = တစ်စုံတစ်ခုသော စိတ်ဖြင့် သိနိုင်သော / တစ်စုံတစ်ခုသော စိတ်ဖြင့် မသိနိုင်သော
both members on one noun (not dhamma) = «A၊ B N»
### Cluster names (pi-1 final): Hetugocchakaṃ = အမြစ်တို့၏ အစု (^1-M-2-1-0); Cūḷantaradukaṃ = ကြားညှပ် နှစ်မျိုးတွဲ အစုငယ် (^1-M-2-2-0)
### Nouns (pi-1 / pi-2 termbases, W()): alobho = လောဘ မရှိခြင်း; adoso = ဒေါသ မရှိခြင်း; amoho = မောဟ မရှိခြင်း; lobho = လောဘ; doso = ဒေါသ; moho = မောဟ; hetu (noun) = အမြစ်; āpodhātu = ရေဓာတ်; itthindriya = မိန်းမ၏ စွမ်းရည်; purisindriya = ယောက်ျား၏ စွမ်းရည်; jīvitindriya = အသက်၏ စွမ်းရည်; Mātikā = ခေါင်းစဉ်စာရင်း
### Reused from other pi-7 groups: cakkaṃ = စက်ဝိုင်း (1-01); gamanaṃ = သွားပုံ, ninnānaṃ = ကွဲပြားမှု မရှိ, evaṃ (alone) = ဤသို့, pavattipaṭisandhi = ဘဝ ဖြစ်စဉ်၌လည်း၊ ပဋိသန္ဓေ၌လည်း, niyāmetabbaṃ = သတ်မှတ်ရမည် (2-03 … 2-06); iminā kāraṇena = ဤနည်းလမ်းဖြင့်, arūpa (noun) = ရုပ် မဟုတ်သော သဘောတရား, dassetabba = ပြသရမည် (2-01 … 2-02); 2-6 heading (1-03 … 1-05 / 2-01 … 2-02); vaṇṇasampadā = အဆင်းအရောင် ပြည့်စုံခြင်း, patthayamāno = တောင့်တလျက် (2-12 … 2-17, in progress: align in the consistency pass)
### Every new string of the generator (NEW, notes, placeholders, headings, unique sentences)
- nahetu sahetuko (dyad term) = အမြစ် မဟုတ်သော်လည်း အမြစ် ရှိသော
- nahetu ahetuko (dyad term) = အမြစ် မဟုတ်၊ အမြစ် မရှိသော
- Hetudukaṃ = အမြစ် နှစ်မျိုးတွဲ
- Sahetukadukaṃ = အမြစ် ရှိခြင်း နှစ်မျိုးတွဲ
- Hetusampayuttadukaṃ = အမြစ်နှင့် ယှဉ်တွဲခြင်း နှစ်မျိုးတွဲ
- Hetusahetukadukaṃ = အမြစ် ဖြစ်ခြင်းနှင့် အမြစ် ရှိခြင်း နှစ်မျိုးတွဲ
- Hetuhetusampayuttadukaṃ = အမြစ် ဖြစ်ခြင်းနှင့် အမြစ်နှင့် ယှဉ်တွဲခြင်း နှစ်မျိုးတွဲ
- Nahetusahetukadukaṃ = အမြစ် မဟုတ်ခြင်းနှင့် အမြစ် ရှိခြင်း နှစ်မျိုးတွဲ
- Sappaccayadukaṃ = အကြောင်း ရှိခြင်း နှစ်မျိုးတွဲ
- Saṅkhatadukaṃ = ပြုပြင်ဖန်တီးထားခြင်း နှစ်မျိုးတွဲ
- Sanidassanadukaṃ = မြင်နိုင်ခြင်း နှစ်မျိုးတွဲ
- Sappaṭighadukaṃ = ထိခိုက်မှု ရှိခြင်း နှစ်မျိုးတွဲ
- Rūpīdukaṃ = ရုပ် ဖြစ်ခြင်း နှစ်မျိုးတွဲ
- Lokiyadukaṃ = လောကနှင့် သက်ဆိုင်ခြင်း နှစ်မျိုးတွဲ
- Kenaciviññeyyadukaṃ = တစ်စုံတစ်ခုသော စိတ်ဖြင့် သိနိုင်ခြင်း နှစ်မျိုးတွဲ
- (Tatiyo bhāgo) = (တတိယ အပိုင်း)
- Dhammānulome dukapaṭṭhānaṃ = သဘောတရား အဟုတ်ပြ ပုံစံ၌ နှစ်မျိုးတွဲတို့၏ အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ
- 4-6. Nissaya-saṃsaṭṭha-sampayuttavāro = 4-6. အမှီပြု၍ ဖြစ်ပေါ်ခြင်း၊ ရောနှောခြင်းနှင့် ယှဉ်တွဲခြင်းအလိုက် ဖော်ပြချက်
- vaṇṇasampadā = အဆင်းအရောင် ပြည့်စုံခြင်း
- patthayamāno = တောင့်တလျက်
- hetu adhipati = အမြစ် အကြီးအမှူး
- yāva asaññasattā = အသညသတ်တို့အထိ
- iha / idha = ဤနေရာ၌
- ninnānākaraṇaṃ = ကွဲပြားချက် မရှိ
- iminā kāraṇena = ဤနည်းလမ်းဖြင့်
- mūla (the starting point of a series) = အခြေခံ
- pucchitabbaṃ / -āni = မေးရမည်
- ekasadisaṃ / -ā = တူညီကြသည်
- ekāyeva / ekoyeva pañhā = ပြဿနာ တစ်ခုတည်း
- itare (the others) = အခြား
- vajjetabbā = ဖယ်ရှားရမည်
- chaḍḍetvā = ဖယ်၍
- dassetabbāni = ပြသရမည်
- yathā labbhanti / yathā yathā labbhati = တွေ့ရသည့်အတိုင်း
- agge = ရှေ့ဆုံးတွင်
- pavatte (in the course of life) = ဘဝ ဖြစ်စဉ်၌
- anulomamātikā = အဟုတ်ပြ ပုံစံ၏ ခေါင်းစဉ်စာရင်း
- suddhake = ရိုးရိုး အပိုင်း၌
- evamuparipi tīsu ṭhānesu = နောက်တွင်လည်း နေရာ သုံးခု၌ ဤနည်းတူ
- paṭhamagamanaṃyeva = ပထမ သွားပုံအတိုင်းပင်
- vitthāretabbaṃ yāva = အောက်ပါအထိ အကျယ် ချဲ့ရမည်
- iminākārena = ဤ ပုံစံအတိုင်း
- vitthāro = အကျယ် ချဲ့ခြင်း
- pañcāyatanāni = အာရုံခံ နယ်ပယ် ငါးပါး
- jānitvā = သိ၍
- arūpapañhāyeva = ရုပ် မဟုတ်သော သဘောတရားဆိုင်ရာ ပြဿနာသာ
- vārā (sections) = ဖော်ပြချက်
- pakatikāyeva = ပကတိအတိုင်းပင်
- (adhipatiyā nava pañhā pavatteyeva) = (အကြီးအမှူးဟူသော အကြောင်း၌ ပြဿနာ ကိုးခု ဘဝ ဖြစ်စဉ်၌ပင်)
- (yathā hetupaccayā evaṃ vitthāretabbaṃ, navapi vipākanti niyāmetabbaṃ) = (အမြစ်ဟူသော အကြောင်းကဲ့သို့ ထိုနည်းတူ အကျယ် ချဲ့ရမည်၊ ကိုးခုလုံးကို ကံ၏ အကျိုးဟု သတ်မှတ်ရမည်)
- (jhānampi maggampi sahajātapaccayasadisā, bāhirā mahābhūtā natthi ) = (ဈာန်ဟူသော အကြောင်းလည်း၊ မဂ်ဟူသော အကြောင်းလည်း အတူ ပေါ်ပေါက်ခြင်းဟူသော အကြောင်းနှင့် တူကြသည်၊ ပြင်ပ မူလဓာတ်ကြီးတို့ မရှိ)
- (nahetupaccayā nava pañhā, ahetukanti niyāmetabbaṃ) = (အမြစ်ဟူသော အကြောင်းကြောင့် မဟုတ်ဘဲ ပြဿနာ ကိုးခု၊ အမြစ် မရှိသည်ဟု သတ်မှတ်ရမည်)
- (Sahajātapaccaye satta, iha ghaṭanā natthi. Aññamaññapaccaye cha, nissayapaccaye satta pañhā, iha ghaṭanā natthi) = (အတူ ပေါ်ပေါက်ခြင်းဟူသော အကြောင်း၌ ခုနစ်ခု၊ ဤနေရာ၌ ပေါင်းစပ်ချက် မရှိ။ အချင်းချင်း ထောက်ပံ့ခြင်းဟူသော အကြောင်း၌ ခြောက်ခု၊ အမှီဟူသော အကြောင်း၌ ပြဿနာ ခုနစ်ခု၊ ဤနေရာ၌ ပေါင်းစပ်ချက် မရှိ)
- (Saṃsaṭṭhavārepi sabbattha ekaṃ, saṃkhittaṃ. Avigatapaccayā, ekāyeva pañhā. Dvepi vārā kātabbā.) = (ရောနှောခြင်းအလိုက် ဖော်ပြချက်၌လည်း နေရာတိုင်း၌ တစ်ခု၊ အကျဉ်းချုပ်။ မပျောက်ကွယ်ခြင်းဟူသော အကြောင်းကြောင့်၊ ပြဿနာ တစ်ခုတည်း။ ဖော်ပြချက် နှစ်ခုလုံးကို ပြုရမည်။)
- (Appaṭighamūlakaṃ itarepi dve pañhā kātabbā. Ghaṭanepi tīṇi pañhā kātabbā. Ajjhattikā bāhirā mahābhūtā sabbe jānitvā kātabbā.) = (ထိခိုက်မှု မရှိသော သဘောတရားကို အခြေခံခြင်း၌ အခြား ပြဿနာ နှစ်ခုကိုလည်း ပြုရမည်။ ပေါင်းစပ်ချက်၌လည်း ပြဿနာ သုံးခုကို ပြုရမည်။ အတွင်းပိုင်း ဖြစ်သော၊ ပြင်ပ မူလဓာတ်ကြီး အားလုံးကို သိ၍ ပြုရမည်။)
- (saṃkhittaṃ. Yāva vatthu nahetū ca khandhā tāva kātabbaṃ) = (အကျဉ်းချုပ်။ မှီရာ ဝတ္ထုနှင့် အမြစ် မဟုတ်သော အစုအဝေးတို့အထိ ပြုရမည်)
- (yāva vatthu nahetū khandhā, ca tāva kātabbaṃ) = (မှီရာ ဝတ္ထုနှင့် အမြစ် မဟုတ်သော အစုအဝေးတို့အထိ ပြုရမည်)
- (vitthāretabbaṃ yāva. Nahetū khandhā) = (အောက်ပါအထိ အကျယ် ချဲ့ရမည်။ အမြစ် မဟုတ်သော အစုအဝေးများ)
- (lokuttare arūpe vipākanti niyāmetabbaṃ) = (လောကကို ကျော်လွန်သော သဘောတရား၌ ရုပ်မရှိသော ဘုံ၌ ကံ၏ အကျိုးဟု သတ်မှတ်ရမည်)
- (naāsevanamūlake lokuttare suddhake vipākoti niyāmetabbaṃ, avasesā pakatikāyeva) = (အလေ့အကျင့် ပြုခြင်းဟူသော အကြောင်း မဟုတ်ခြင်းကို အခြေခံခြင်း၌ လောကကို ကျော်လွန်သော သဘောတရား၏ ရိုးရိုး အပိုင်း၌ ကံ၏ အကျိုးဟု သတ်မှတ်ရမည်၊ ကြွင်းသည်တို့သည် ပကတိအတိုင်းပင်)
- niṭṭhitesu = ပြီးဆုံးသောအခါ
--- notes (K.NOTE_FIXED additions)
- (cakkaṃ) = (စက်ဝိုင်း)
- (paṭhamagamanaṃyeva) = (ပထမ သွားပုံအတိုင်းပင်)
- (yathā paṭhamagamanaṃ evaṃ ninnānaṃ) = (ပထမ သွားပုံကဲ့သို့ ထိုနည်းတူ ကွဲပြားမှု မရှိ)
- (āvajjanā natthi) = (စိတ်ညွတ်ခြင်း မရှိ)
- (imesu dvīsu nava) = (ဤ နှစ်ခု၌ ကိုးခု)
- (sahajātavāropi paccayavāropi nissayavāropi paṭiccavārasadisāyeva pañhā) = (အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း၊ အကြောင်းပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်လည်း၊ အမှီပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်လည်း မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူသော ပြဿနာများပင်)
- (saṃsaṭṭhavāropi sampayuttavāropi paripuṇṇo) = (ရောနှောခြင်းအလိုက် ဖော်ပြချက်လည်း၊ ယှဉ်တွဲခြင်းအလိုက် ဖော်ပြချက်လည်း ပြည့်စုံသည်)
- (rūpaṃ natthi , arūpameva) = (ရုပ် မရှိ၊ ရုပ် မဟုတ်သော သဘောတရားသာ)
- (dutiyaupanissayasadisaṃ) = (ဒုတိယ အားကြီးသော အမှီနှင့် တူသည်)
- (dvīsupi paṭisandhi natthi) = (နှစ်ခုလုံး၌ ပဋိသန္ဓေ မရှိ)
- (evaṃ indriyapaccayā vitthāretabbā) = (စွမ်းရည်ဟူသော အကြောင်းကို ဤသို့ အကျယ် ချဲ့ရမည်)
- (imaṃ nānaṃ) = (ဤသည် ကွဲပြားချက် ဖြစ်သည်)
- (ime dvepi paṭiccasadisā) = (ဤ နှစ်ခုလုံးသည် မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူကြသည်)
- (rūpaṃ chaḍḍetvā arūpeyeva nava pañhā) = (ရုပ်ကို ဖယ်၍ ရုပ်မရှိသော ဘုံ၌ပင် ပြဿနာ ကိုးခု)
- (sabbe mahābhūtā yāva asaññasattā) = (မူလဓာတ်ကြီး အားလုံး အသညသတ်တို့အထိ)
- (tattha tattha ṭhitena imaṃ kātabbaṃ dutiyagamanasadisaṃ) = (ထိုထို နေရာ၌ တည်၍ ဤသည်ကို ဒုတိယ သွားပုံနှင့် တူအောင် ပြုရမည်)
- (vitthāretabbaṃ yāva) = (အောက်ပါအထိ အကျယ် ချဲ့ရမည်)
- (vitthāretabbaṃ) = (အကျယ် ချဲ့ရမည်)
- (yathā hetusahetukadukaṃ evaṃ vitthāretabbaṃ , ninnānākaraṇaṃ) = (အမြစ် ဖြစ်ခြင်းနှင့် အမြစ် ရှိခြင်း နှစ်မျိုးတွဲကဲ့သို့ ထိုနည်းတူ အကျယ် ချဲ့ရမည်၊ ကွဲပြားချက် မရှိ)
- (iminā kāraṇena vitthāretabbaṃ yathā sahetukadukaṃ ninnānākaraṇaṃ) = (ဤနည်းလမ်းဖြင့် အမြစ် ရှိခြင်း နှစ်မျိုးတွဲကဲ့သို့ ကွဲပြားချက် မရှိ အကျယ် ချဲ့ရမည်)
- (dve mūlāni pucchitabbāni) = (အခြေခံ နှစ်ခုကို မေးရမည်)
- (mūlaṃ kātabbaṃ) = (အခြေခံကို ပြုရမည်)
- (mūlaṃ pucchitabbaṃ) = (အခြေခံကို မေးရမည်)
- (imesaṃ dvinnampi pañhānaṃ mūlāni pucchitabbāni) = (ဤ ပြဿနာ နှစ်ခုလုံး၏ အခြေခံတို့ကို မေးရမည်)
- (sahajātavāropi paccayavāropi nissayavāropi saṃsaṭṭhavāropi sampayuttavāropi paṭiccavārasadisā) = (အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း၊ အကြောင်းပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်လည်း၊ အမှီပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်လည်း၊ ရောနှောခြင်းအလိုက် ဖော်ပြချက်လည်း၊ ယှဉ်တွဲခြင်းအလိုက် ဖော်ပြချက်လည်း မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူကြသည်)
- (sahetuko ceva na ca hetumūlakaṃ tīṇipi ekasadisā) = (အမြစ် ရှိသော်လည်း အမြစ် မဟုတ်သော သဘောတရားကို အခြေခံခြင်း၌ သုံးခုလုံး တူညီကြသည်)
- (sahetuko ceva na ca hetumūlake iminākārena vitthāretabbā avasesā dve pañhā) = (အမြစ် ရှိသော်လည်း အမြစ် မဟုတ်သော သဘောတရားကို အခြေခံခြင်း၌ ကြွင်းသော ပြဿနာ နှစ်ခုကို ဤ ပုံစံအတိုင်း အကျယ် ချဲ့ရမည်)
- (evaṃ vitthāretabbaṃ) = (ဤသို့ အကျယ် ချဲ့ရမည်)
- (indriyanti niyāmetabbaṃ , navapi paripuṇṇaṃ) = (စွမ်းရည်ဟု သတ်မှတ်ရမည်၊ ကိုးခုလုံး ပြည့်စုံသည်)
- (paripuṇṇaṃ nava) = (ပြည့်စုံစွာ ကိုးခု)
- (tīṇipi paccayā paṭiccavāre hetusadisā) = (အကြောင်း သုံးခုလုံးသည် မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်၌ အမြစ်နှင့် တူကြသည်)
- (navapi vipākanti niyāmetabbaṃ) = (ကိုးခုလုံးကို ကံ၏ အကျိုးဟု သတ်မှတ်ရမည်)
- (yathā paṭiccavārasadisaṃ) = (မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူသည့်အတိုင်း)
- (evaṃ avasesāpi dve gaṇanā gaṇetabbā) = (ကြွင်းသော ရေတွက်ချက် နှစ်ခုကိုလည်း ဤသို့ ရေတွက်ရမည်)
- (sahajātavārepi evaṃ gaṇetabbaṃ) = (အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်၌လည်း ဤသို့ ရေတွက်ရမည်)
- (cattāripi kātabbāni) = (လေးခုလုံးကို ပြုရမည်)
- (ghaṭanā tīṇi , pavattipaṭisandhi paripuṇṇaṃ) = (ပေါင်းစပ်ချက် သုံးခု၊ ဘဝ ဖြစ်စဉ်၌လည်း၊ ပဋိသန္ဓေ၌လည်း ပြည့်စုံသည်)
- (iha ghaṭanā natthi , satta pañhā) = (ဤနေရာ၌ ပေါင်းစပ်ချက် မရှိ၊ ပြဿနာ ခုနစ်ခု)
- (pavattipaṭisandhi satta pañhā , iha ghaṭanā natthi) = (ဘဝ ဖြစ်စဉ်၌လည်း၊ ပဋိသန္ဓေ၌လည်း ပြဿနာ ခုနစ်ခု၊ ဤနေရာ၌ ပေါင်းစပ်ချက် မရှိ)
- (evaṃ vibhajitabbaṃ) = (ဤသို့ ခွဲခြမ်းစိတ်ဖြာရမည်)
- (yāva asaññasattā moho natthi) = (အသညသတ်တို့အထိ မောဟ မရှိ)
- (yāva asaññasattā) = (အသညသတ်တို့အထိ)
- (sabbaṃ yāva asaññasattā tāva kātabbaṃ) = (အားလုံးကို အသညသတ်တို့အထိ ပြုရမည်)
- (āvajjanampi bhavaṅgampi natthi , āsevanapaccaye vajjetabbā navapi) = (စိတ်ညွတ်ခြင်းလည်း၊ ဘဝင် စိတ်လည်း မရှိ၊ အလေ့အကျင့် ပြုခြင်းဟူသော အကြောင်း၌ ကိုးခုလုံးကို ဖယ်ရှားရမည်)
- (anulomasahajātasadisā) = (အဟုတ်ပြ ပုံစံ၏ အတူ ပေါ်ပေါက်ခြင်းဟူသော အကြောင်းနှင့် တူကြသည်)
- (ime pañca pañhā hetusadisā , ninnānaṃ) = (ဤ ပြဿနာ ငါးခုသည် အမြစ်နှင့် တူကြသည်၊ ကွဲပြားမှု မရှိ)
- (bāhirā mahābhūtā natthi) = (ပြင်ပ မူလဓာတ်ကြီးတို့ မရှိ)
- (paṭiccavārasadisaṃyeva) = (မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူသည်ပင်)
- (paṭiccavāre nissayapaccayasadisaṃ , iha ghaṭanā natthi) = (မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်၌ အမှီဟူသော အကြောင်းနှင့် တူသည်၊ ဤနေရာ၌ ပေါင်းစပ်ချက် မရှိ)
- (paṭiccavāre sahajātasadisaṃ , iha ghaṭanā natthi) = (မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်၌ အတူ ပေါ်ပေါက်ခြင်းဟူသော အကြောင်းနှင့် တူသည်၊ ဤနေရာ၌ ပေါင်းစပ်ချက် မရှိ)
- (paṭiccavāre sampayuttasadisā cha pañhā) = (မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်၌ ယှဉ်တွဲခြင်းဟူသော အကြောင်းနှင့် တူသော ပြဿနာ ခြောက်ခု)
- (sahetukamūlakaṃ paṭiccavārasadisaṃ) = (အမြစ် ရှိသော သဘောတရားကို အခြေခံခြင်းသည် မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူသည်)
- (saṃkhittaṃ , yāva asaññasattā) = (အကျဉ်းချုပ်၊ အသညသတ်တို့အထိ)
- (yāva asaññasattā kātabbaṃ) = (အသညသတ်တို့အထိ ပြုရမည်)
- (yāva asaññasattā tāva vitthāro) = (အသညသတ်တို့အထိ အကျယ် ချဲ့ခြင်း)
- (sahajātavāropi paccayavāropi nissayavāropi saṃsaṭṭhavāropi sampayuttavāropi evaṃ vitthāretabbā) = (အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်ကိုလည်း၊ အကြောင်းပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်ကိုလည်း၊ အမှီပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်ကိုလည်း၊ ရောနှောခြင်းအလိုက် ဖော်ပြချက်ကိုလည်း၊ ယှဉ်တွဲခြင်းအလိုက် ဖော်ပြချက်ကိုလည်း ဤသို့ အကျယ် ချဲ့ရမည်)
- (paccayavāre vatthu ca pañcāyatanāni ca dassetabbāni) = (အကြောင်းပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်၌ မှီရာ ဝတ္ထုကိုလည်းကောင်း၊ အာရုံခံ နယ်ပယ် ငါးပါးတို့ကိုလည်းကောင်း ပြသရမည်)
- (yathā yathā labbhati taṃ taṃ kātabbaṃ) = (တွေ့ရသည့်အတိုင်း ထိုထို အရာကို ပြုရမည်)
- (evaṃ cattāripi gaṇanā paripuṇṇā) = (ဤသို့ ရေတွက်ချက် လေးခုလုံး ပြည့်စုံကြသည်)
- (saṃsaṭṭhavāro evaṃ vitthāretabbo , saha gaṇanāhi dve pañhā) = (ရောနှောခြင်းအလိုက် ဖော်ပြချက်ကို ဤသို့ အကျယ် ချဲ့ရမည်၊ ရေတွက်ချက်တို့နှင့်တကွ ပြဿနာ နှစ်ခု)
- (anulomamātikā kātabbā) = (အဟုတ်ပြ ပုံစံ၏ ခေါင်းစဉ်စာရင်းကို ပြုရမည်)
- (anulomamātikā gaṇetabbā) = (အဟုတ်ပြ ပုံစံ၏ ခေါင်းစဉ်စာရင်းကို ရေတွက်ရမည်)
- (naanantarapadādī paccanīyasadisā) = (ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းဟူသော အကြောင်း မဟုတ်ခြင်း ပုဒ် စသည်တို့သည် အငြင်းပြ ပုံစံနှင့် တူကြသည်)
- (nasamanantarapadādī paccanīyasadisā) = (ကောင်းစွာ ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းဟူသော အကြောင်း မဟုတ်ခြင်း ပုဒ် စသည်တို့သည် အငြင်းပြ ပုံစံနှင့် တူကြသည်)
- (pañca pañhā , ghaṭanā natthi) = (ပြဿနာ ငါးခု၊ ပေါင်းစပ်ချက် မရှိ)
- (paṭisandhi kātabbā) = (ပဋိသန္ဓေကို ပြုရမည်)
- (evaṃ paccanīyādīni gaṇanāpi sampayuttavārepi sabbe kātabbā) = (ဤသို့ အငြင်းပြ ပုံစံ စသည်တို့၏ ရေတွက်ချက်တို့ကိုလည်း၊ ယှဉ်တွဲခြင်းအလိုက် ဖော်ပြချက်၌လည်း အားလုံးကို ပြုရမည်)
- (ekoyeva pañho) = (ပြဿနာ တစ်ခုတည်း)
- (ekāyeva pañhā) = (ပြဿနာ တစ်ခုတည်း)
- (nissayavāropi paccayavārasadiso) = (အမှီပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်သည်လည်း အကြောင်းပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူသည်)
- (sahajātavāropi paṭiccavārasadiso) = (အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်သည်လည်း မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူသည်)
- (sampayuttavāropi saṃsaṭṭhavārasadiso) = (ယှဉ်တွဲခြင်းအလိုက် ဖော်ပြချက်သည်လည်း ရောနှောခြင်းအလိုက် ဖော်ပြချက်နှင့် တူသည်)
- (evaṃ avasesā pañhā , pavattipaṭisandhi vibhajitabbā) = (ကြွင်းသော ပြဿနာတို့လည်း ဤသို့ပင်၊ ဘဝ ဖြစ်စဉ်၌လည်း၊ ပဋိသန္ဓေ၌လည်း ခွဲခြမ်းစိတ်ဖြာရမည်)
- (pavattipaṭisandhi kātabbā) = (ဘဝ ဖြစ်စဉ်၌လည်း၊ ပဋိသန္ဓေ၌လည်း ပြုရမည်)
- (paṭiccasadisaṃ) = (မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူသည်)
- (sabbe kātabbā) = (အားလုံးကို ပြုရမည်)
- (evaṃ sabbe kātabbā) = (ဤသို့ အားလုံးကို ပြုရမည်)
- (saṃkhittaṃ , sabbe kātabbā) = (အကျဉ်းချုပ်၊ အားလုံးကို ပြုရမည်)
- (nissayavāropi evaṃ kātabbo) = (အမှီပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်ကိုလည်း ဤသို့ ပြုရမည်)
- (itarepi dve kātabbā) = (အခြား နှစ်ခုကိုလည်း ပြုရမည်)
- (itarepi dve pañhā kātabbā) = (အခြား ပြဿနာ နှစ်ခုကိုလည်း ပြုရမည်)
- (tīsupi kabaḷīkāro āhāro kātabbo) = (သုံးခုလုံး၌ လုတ်ပြု၍ စားရသော အာဟာရကို ပြုရမည်)
- (tīsupi rūpajīvitindriyaṃ) = (သုံးခုလုံး၌ ရုပ် အသက်၏ စွမ်းရည်)
- (imaṃ dukaṃ yathā sappaccayadukaṃ , evaṃ gaṇetabbaṃ , ninnānākaraṇaṃ) = (ဤ နှစ်မျိုးတွဲကို အကြောင်း ရှိခြင်း နှစ်မျိုးတွဲကဲ့သို့ ထိုနည်းတူ ရေတွက်ရမည်၊ ကွဲပြားချက် မရှိ)
- (evaṃ paccayavāropi nissayavāropi saṃsaṭṭhavāropi sampayuttavāropi vitthāretabbo , sabbattha ekāyeva pañhā) = (ဤသို့ အကြောင်းပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်ကိုလည်း၊ အမှီပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်ကိုလည်း၊ ရောနှောခြင်းအလိုက် ဖော်ပြချက်ကိုလည်း၊ ယှဉ်တွဲခြင်းအလိုက် ဖော်ပြချက်ကိုလည်း အကျယ် ချဲ့ရမည်၊ နေရာတိုင်း၌ ပြဿနာ တစ်ခုတည်း)
- (dve pañhā upanissayamūlaṃ) = (အားကြီးသော အမှီဟူသော အကြောင်းကို အခြေခံခြင်း၌ ပြဿနာ နှစ်ခု)
- (sabbattha ekāyeva pañhā) = (နေရာတိုင်း၌ ပြဿနာ တစ်ခုတည်း)
- (avasesā pañca pañhā paṭiccavārasadisā) = (ကြွင်းသော ပြဿနာ ငါးခုသည် မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူကြသည်)
- (avasesā dvepi pañhā kātabbā , paṭisandhi kabaḷīkāro āhāro dvīsupi kātabbo agge) = (ကြွင်းသော ပြဿနာ နှစ်ခုလုံးကို ပြုရမည်၊ ပဋိသန္ဓေနှင့် လုတ်ပြု၍ စားရသော အာဟာရကို နှစ်ခုလုံး၌ ရှေ့ဆုံးတွင် ပြုရမည်)
- (dvinnampi mūlā kātabbā) = (နှစ်ခုလုံး၏ အခြေခံတို့ကို ပြုရမည်)
- (evaṃ paccanīyagaṇanāpi kātabbā) = (ဤသို့ အငြင်းပြ ပုံစံ၏ ရေတွက်ချက်ကိုလည်း ပြုရမည်)
- (ime ajjhattikabāhirā mahābhūtā kātabbā) = (ဤ အတွင်းပိုင်း ဖြစ်သော၊ ပြင်ပ မူလဓာတ်ကြီးတို့ကို ပြုရမည်)
- (paṭiccasadisaṃ yāva asaññasattā) = (အသညသတ်တို့အထိ မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူသည်)
- (paṭiccasadisā paṭhamapañhā) = (ပထမ ပြဿနာသည် မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူသည်)
- (paṭisandhi vajjetabbā , kaṭattārūpā ca) = (ပဋိသန္ဓေကိုလည်းကောင်း၊ ကံ ပြုခဲ့သောကြောင့် ဖြစ်သော ရုပ်တို့ကိုလည်းကောင်း ဖယ်ရှားရမည်)
- (sabbaṃ saṃkhittaṃ) = (အားလုံး အကျဉ်းချုပ်)
- (tīsupi jīvitindriyaṃ agge kātabbaṃ) = (သုံးခုလုံး၌ အသက်၏ စွမ်းရည်ကို ရှေ့ဆုံးတွင် ပြုရမည်)
- (ghaṭanepi tīṇi pañhā kātabbā) = (ပေါင်းစပ်ချက်၌လည်း ပြဿနာ သုံးခုကို ပြုရမည်)
- (ajjhattikā bāhirā mahābhūtā sabbe jānitvā kātabbā) = (အတွင်းပိုင်း ဖြစ်သော၊ ပြင်ပ မူလဓာတ်ကြီး အားလုံးကို သိ၍ ပြုရမည်)
- (arūpapañhāyeva) = (ရုပ် မဟုတ်သော သဘောတရားဆိုင်ရာ ပြဿနာသာ)
- (nahetumūlakaṃ tīṇipi ekasadisaṃ) = (အမြစ် မဟုတ်သော သဘောတရားကို အခြေခံခြင်း၌ သုံးခုလုံး တူညီကြသည်)
- (vipākavibhaṅge nava pañhā) = (ကံ၏ အကျိုးဟူသော အကြောင်း၏ ခွဲခြမ်းစိတ်ဖြာခြင်း၌ ပြဿနာ ကိုးခု)
- (sabbattha ekaṃ) = (နေရာတိုင်း၌ တစ်ခု)
- (sabbattha dve) = (နေရာတိုင်း၌ နှစ်ခု)
- (sabbattha tīṇi) = (နေရာတိုင်း၌ သုံးခု)
- (sabbattha cattāri) = (နေရာတိုင်း၌ လေးခု)
- (sabbattha pañca) = (နေရာတိုင်း၌ ငါးခု)
- (sabbattha cha) = (နေရာတိုင်း၌ ခြောက်ခု)
- (sabbattha satta) = (နေရာတိုင်း၌ ခုနစ်ခု)
- (sabbattha aṭṭha) = (နေရာတိုင်း၌ ရှစ်ခု)
- (sabbattha nava) = (နေရာတိုင်း၌ ကိုးခု)
- (sabbattha dasa) = (နေရာတိုင်း၌ ဆယ်ခု)
- (sabbattha ekādasa) = (နေရာတိုင်း၌ ဆယ့်တစ်ခု)
- (sabbattha dvādasa) = (နေရာတိုင်း၌ ဆယ့်နှစ်ခု)
- (sabbattha terasa) = (နေရာတိုင်း၌ ဆယ့်သုံးခု)
- (sabbattha cuddasa) = (နေရာတိုင်း၌ ဆယ့်လေးခု)
- (sabbattha pannarasa) = (နေရာတိုင်း၌ ဆယ့်ငါးခု)
- (sabbattha soḷasa) = (နေရာတိုင်း၌ ဆယ့်ခြောက်ခု)
- (sabbattha sattarasa) = (နေရာတိုင်း၌ ဆယ့်ခုနစ်ခု)
- (sabbattha aṭṭhārasa) = (နေရာတိုင်း၌ ဆယ့်ရှစ်ခု)
- (sabbattha ekavīsa) = (နေရာတိုင်း၌ နှစ်ဆယ့်တစ်ခု)
- (evaṃ sabbaṃ sappaccayagaṇanāhi saddhiṃ kātabbaṃ) = (ဤသို့ အားလုံးကို အကြောင်း ရှိခြင်း နှစ်မျိုးတွဲ၏ ရေတွက်ချက်တို့နှင့်အတူ ပြုရမည်)
- (dvepi vārā kātabbā) = (ဖော်ပြချက် နှစ်ခုလုံးကို ပြုရမည်)
--- NOTEP
- (adhipatiyā nava pañhā pavatteyeva) = (အကြီးအမှူးဟူသော အကြောင်း၌ ပြဿနာ ကိုးခု ဘဝ ဖြစ်စဉ်၌ပင်)
- (yathā hetupaccayā evaṃ vitthāretabbaṃ, navapi vipākanti niyāmetabbaṃ) = (အမြစ်ဟူသော အကြောင်းကဲ့သို့ ထိုနည်းတူ အကျယ် ချဲ့ရမည်၊ ကိုးခုလုံးကို ကံ၏ အကျိုးဟု သတ်မှတ်ရမည်)
- (jhānampi maggampi sahajātapaccayasadisā, bāhirā mahābhūtā natthi ) = (ဈာန်ဟူသော အကြောင်းလည်း၊ မဂ်ဟူသော အကြောင်းလည်း အတူ ပေါ်ပေါက်ခြင်းဟူသော အကြောင်းနှင့် တူကြသည်၊ ပြင်ပ မူလဓာတ်ကြီးတို့ မရှိ)
- (nahetupaccayā nava pañhā, ahetukanti niyāmetabbaṃ) = (အမြစ်ဟူသော အကြောင်းကြောင့် မဟုတ်ဘဲ ပြဿနာ ကိုးခု၊ အမြစ် မရှိသည်ဟု သတ်မှတ်ရမည်)
- (Sahajātapaccaye satta, iha ghaṭanā natthi. Aññamaññapaccaye cha, nissayapaccaye satta pañhā, iha ghaṭanā natthi) = (အတူ ပေါ်ပေါက်ခြင်းဟူသော အကြောင်း၌ ခုနစ်ခု၊ ဤနေရာ၌ ပေါင်းစပ်ချက် မရှိ။ အချင်းချင်း ထောက်ပံ့ခြင်းဟူသော အကြောင်း၌ ခြောက်ခု၊ အမှီဟူသော အကြောင်း၌ ပြဿနာ ခုနစ်ခု၊ ဤနေရာ၌ ပေါင်းစပ်ချက် မရှိ)
- (Saṃsaṭṭhavārepi sabbattha ekaṃ, saṃkhittaṃ. Avigatapaccayā, ekāyeva pañhā. Dvepi vārā kātabbā.) = (ရောနှောခြင်းအလိုက် ဖော်ပြချက်၌လည်း နေရာတိုင်း၌ တစ်ခု၊ အကျဉ်းချုပ်။ မပျောက်ကွယ်ခြင်းဟူသော အကြောင်းကြောင့်၊ ပြဿနာ တစ်ခုတည်း။ ဖော်ပြချက် နှစ်ခုလုံးကို ပြုရမည်။)
- (Appaṭighamūlakaṃ itarepi dve pañhā kātabbā. Ghaṭanepi tīṇi pañhā kātabbā. Ajjhattikā bāhirā mahābhūtā sabbe jānitvā kātabbā.) = (ထိခိုက်မှု မရှိသော သဘောတရားကို အခြေခံခြင်း၌ အခြား ပြဿနာ နှစ်ခုကိုလည်း ပြုရမည်။ ပေါင်းစပ်ချက်၌လည်း ပြဿနာ သုံးခုကို ပြုရမည်။ အတွင်းပိုင်း ဖြစ်သော၊ ပြင်ပ မူလဓာတ်ကြီး အားလုံးကို သိ၍ ပြုရမည်။)
- (saṃkhittaṃ. Yāva vatthu nahetū ca khandhā tāva kātabbaṃ) = (အကျဉ်းချုပ်။ မှီရာ ဝတ္ထုနှင့် အမြစ် မဟုတ်သော အစုအဝေးတို့အထိ ပြုရမည်)
- (yāva vatthu nahetū khandhā, ca tāva kātabbaṃ) = (မှီရာ ဝတ္ထုနှင့် အမြစ် မဟုတ်သော အစုအဝေးတို့အထိ ပြုရမည်)
- (vitthāretabbaṃ yāva. Nahetū khandhā) = (အောက်ပါအထိ အကျယ် ချဲ့ရမည်။ အမြစ် မဟုတ်သော အစုအဝေးများ)
- (lokuttare arūpe vipākanti niyāmetabbaṃ) = (လောကကို ကျော်လွန်သော သဘောတရား၌ ရုပ်မရှိသော ဘုံ၌ ကံ၏ အကျိုးဟု သတ်မှတ်ရမည်)
- (naāsevanamūlake lokuttare suddhake vipākoti niyāmetabbaṃ, avasesā pakatikāyeva) = (အလေ့အကျင့် ပြုခြင်းဟူသော အကြောင်း မဟုတ်ခြင်းကို အခြေခံခြင်း၌ လောကကို ကျော်လွန်သော သဘောတရား၏ ရိုးရိုး အပိုင်း၌ ကံ၏ အကျိုးဟု သတ်မှတ်ရမည်၊ ကြွင်းသည်တို့သည် ပကတိအတိုင်းပင်)
--- headings
- (Tatiyo bhāgo) = (တတိယ အပိုင်း)
- Dhammānulome dukapaṭṭhānaṃ = သဘောတရား အဟုတ်ပြ ပုံစံ၌ နှစ်မျိုးတွဲတို့၏ အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ
- 2-6 Sahajāta-paccaya-nissaya-saṃsaṭṭha-sampayuttavāro = 2-6 အတူ ပေါ်ပေါက်ခြင်း၊ အကြောင်းပြု၍ ဖြစ်ပေါ်ခြင်း၊ အမှီပြု၍ ဖြစ်ပေါ်ခြင်း၊ ရောနှောခြင်းနှင့် ယှဉ်တွဲခြင်းအလိုက် ဖော်ပြချက်
- 2-6. Sahajāta-paccaya-nissaya-saṃsaṭṭha-sampayuttavāro = 2-6. အတူ ပေါ်ပေါက်ခြင်း၊ အကြောင်းပြု၍ ဖြစ်ပေါ်ခြင်း၊ အမှီပြု၍ ဖြစ်ပေါ်ခြင်း၊ ရောနှောခြင်းနှင့် ယှဉ်တွဲခြင်းအလိုက် ဖော်ပြချက်
- 4-6. Nissaya-saṃsaṭṭha-sampayuttavāro = 4-6. အမှီပြု၍ ဖြစ်ပေါ်ခြင်း၊ ရောနှောခြင်းနှင့် ယှဉ်တွဲခြင်းအလိုက် ဖော်ပြချက်
- *Vipākāhārapaccayā* = *ကံ၏ အကျိုးဟူသော အကြောင်းနှင့် အာဟာရဟူသော အကြောင်း*
- Anulomapaccanīyaṃ = အဟုတ်ပြ အငြင်းပြ ပုံစံ
- Hetugocchakaṃ = အမြစ်တို့၏ အစု
- Cūḷantaradukaṃ = ကြားညှပ် နှစ်မျိုးတွဲ အစုငယ်
- Hetudukaṃ = အမြစ် နှစ်မျိုးတွဲ
- Sahetukadukaṃ = အမြစ် ရှိခြင်း နှစ်မျိုးတွဲ
- Hetusampayuttadukaṃ = အမြစ်နှင့် ယှဉ်တွဲခြင်း နှစ်မျိုးတွဲ
- Hetusahetukadukaṃ = အမြစ် ဖြစ်ခြင်းနှင့် အမြစ် ရှိခြင်း နှစ်မျိုးတွဲ
- Hetuhetusampayuttadukaṃ = အမြစ် ဖြစ်ခြင်းနှင့် အမြစ်နှင့် ယှဉ်တွဲခြင်း နှစ်မျိုးတွဲ
- Nahetusahetukadukaṃ = အမြစ် မဟုတ်ခြင်းနှင့် အမြစ် ရှိခြင်း နှစ်မျိုးတွဲ
- Sappaccayadukaṃ = အကြောင်း ရှိခြင်း နှစ်မျိုးတွဲ
- Saṅkhatadukaṃ = ပြုပြင်ဖန်တီးထားခြင်း နှစ်မျိုးတွဲ
- Sanidassanadukaṃ = မြင်နိုင်ခြင်း နှစ်မျိုးတွဲ
- Sappaṭighadukaṃ = ထိခိုက်မှု ရှိခြင်း နှစ်မျိုးတွဲ
- Rūpīdukaṃ = ရုပ် ဖြစ်ခြင်း နှစ်မျိုးတွဲ
- Lokiyadukaṃ = လောကနှင့် သက်ဆိုင်ခြင်း နှစ်မျိုးတွဲ
- Kenaciviññeyyadukaṃ = တစ်စုံတစ်ခုသော စိတ်ဖြင့် သိနိုင်ခြင်း နှစ်မျိုးတွဲ
- Hetudukaṃ niṭṭhitaṃ. = “အမြစ် နှစ်မျိုးတွဲ” ပြီးဆုံးပြီ။
- Sahetukadukaṃ niṭṭhitaṃ. = “အမြစ် ရှိခြင်း နှစ်မျိုးတွဲ” ပြီးဆုံးပြီ။
- Hetusampayuttadukaṃ niṭṭhitaṃ. = “အမြစ်နှင့် ယှဉ်တွဲခြင်း နှစ်မျိုးတွဲ” ပြီးဆုံးပြီ။
- Hetusahetukadukaṃ niṭṭhitaṃ. = “အမြစ် ဖြစ်ခြင်းနှင့် အမြစ် ရှိခြင်း နှစ်မျိုးတွဲ” ပြီးဆုံးပြီ။
- Hetuhetusampayuttadukaṃ niṭṭhitaṃ. = “အမြစ် ဖြစ်ခြင်းနှင့် အမြစ်နှင့် ယှဉ်တွဲခြင်း နှစ်မျိုးတွဲ” ပြီးဆုံးပြီ။
- Nahetusahetukadukaṃ niṭṭhitaṃ. = “အမြစ် မဟုတ်ခြင်းနှင့် အမြစ် ရှိခြင်း နှစ်မျိုးတွဲ” ပြီးဆုံးပြီ။
- Sappaccayadukaṃ niṭṭhitaṃ. = “အကြောင်း ရှိခြင်း နှစ်မျိုးတွဲ” ပြီးဆုံးပြီ။
- Saṅkhatadukaṃ niṭṭhitaṃ. = “ပြုပြင်ဖန်တီးထားခြင်း နှစ်မျိုးတွဲ” ပြီးဆုံးပြီ။
- Sanidassanadukaṃ niṭṭhitaṃ. = “မြင်နိုင်ခြင်း နှစ်မျိုးတွဲ” ပြီးဆုံးပြီ။
- Sappaṭighadukaṃ niṭṭhitaṃ. = “ထိခိုက်မှု ရှိခြင်း နှစ်မျိုးတွဲ” ပြီးဆုံးပြီ။
- Rūpīdukaṃ niṭṭhitaṃ. = “ရုပ် ဖြစ်ခြင်း နှစ်မျိုးတွဲ” ပြီးဆုံးပြီ။
- Lokiyadukaṃ niṭṭhitaṃ. = “လောကနှင့် သက်ဆိုင်ခြင်း နှစ်မျိုးတွဲ” ပြီးဆုံးပြီ။
- Kenaciviññeyyadukaṃ niṭṭhitaṃ. = “တစ်စုံတစ်ခုသော စိတ်ဖြင့် သိနိုင်ခြင်း နှစ်မျိုးတွဲ” ပြီးဆုံးပြီ။
- Hetugocchakaṃ niṭṭhitaṃ. = “အမြစ်တို့၏ အစု” ပြီးဆုံးပြီ။
- Cūḷantaradukaṃ niṭṭhitaṃ. = “ကြားညှပ် နှစ်မျိုးတွဲ အစုငယ်” ပြီးဆုံးပြီ။
--- SK/SKF
- mahābhūtesu niṭṭhitesu "vatthuṃ paccayā"ti kātabbā. = မူလဓာတ်ကြီးတို့ ပြီးဆုံးသောအခါ “မှီရာ ဝတ္ထုကြောင့်”ဟု ပြုရမည်။
- pañcāyatanāni anulomepi paccanīyepi yathā labbhanti tathā kātabbā. = အာရုံခံ နယ်ပယ် ငါးပါးတို့ကို အဟုတ်ပြ ပုံစံ၌လည်း၊ အငြင်းပြ ပုံစံ၌လည်း တွေ့ရသည့်အတိုင်း ပြုရမည်။
- rūpāyatanaṃ cakkhuviññāṇassa… phoṭṭhabbāyatanaṃ kāyaviññāṇassāti idaṃ natthi). = အဆင်းအရောင် အာရုံခံ နယ်ပယ်သည် မျက်စိ သိစိတ်အား… အထိအတွေ့ အာရုံခံ နယ်ပယ်သည် ကိုယ် သိစိတ်အားဟူသော ဤသည် မရှိ)။
- dve khandhā ca = အစုအဝေး နှစ်ပါးလည်းကောင်း
- §T§ā khandhā purejātassa = {T1} အစုအဝေးတို့သည် ရှေးဦးစွာ ဖြစ်ပေါ်ပြီးသော
- kabaḷīkāro āhāro imassa kāyassa = လုတ်ပြု၍ စားရသော အာဟာရသည် ဤကိုယ်အား
- §T§o eko khandho tiṇṇannaṃ khandhānaṃ §T§ānañca = {T1} အစုအဝေး တစ်ပါးသည် အစုအဝေး သုံးပါးတို့အားလည်းကောင်း၊ {T2}
--- dyads
- hetu: hetudk = အမြစ် ဖြစ်သော
- hetu: nahetudk = အမြစ် မဟုတ်သော
- hetu: hetudk_nahetudk_both = အမြစ် ဖြစ်သော၊ အမြစ် မဟုတ်သော
- sahetuka: sahetuk = အမြစ် ရှိသော
- sahetuka: ahetuk = အမြစ် မရှိသော
- sahetuka: sahetuk_ahetuk_both = အမြစ် ရှိသော၊ အမြစ် မရှိသော
- hetusamp: hetusampayutt = အမြစ်နှင့် ယှဉ်တွဲသော
- hetusamp: hetuvippayutt = အမြစ်နှင့် ကင်းကွာသော
- hetusamp: hetusampayutt_hetuvippayutt_both = အမြစ်နှင့် ယှဉ်တွဲသော၊ အမြစ်နှင့် ကင်းကွာသော
- hetusahetuka: hetusahetukdk = အမြစ်လည်း ဖြစ်၊ အမြစ်လည်း ရှိသော
- hetusahetuka: sahetukanahetudk = အမြစ် ရှိသော်လည်း အမြစ် မဟုတ်သော
- hetusahetuka: hetusahetukdk_sahetukanahetudk_both = အမြစ်လည်း ဖြစ်၊ အမြစ်လည်း ရှိသော၊ အမြစ် ရှိသော်လည်း အမြစ် မဟုတ်သော
- hetuhetusamp: hetuhetusampdk = အမြစ်လည်း ဖြစ်၊ အမြစ်နှင့်လည်း ယှဉ်တွဲသော
- hetuhetusamp: hetusampnahetudk = အမြစ်နှင့် ယှဉ်တွဲသော်လည်း အမြစ် မဟုတ်သော
- hetuhetusamp: hetuhetusampdk_hetusampnahetudk_both = အမြစ်လည်း ဖြစ်၊ အမြစ်နှင့်လည်း ယှဉ်တွဲသော၊ အမြစ်နှင့် ယှဉ်တွဲသော်လည်း အမြစ် မဟုတ်သော
- nahetusahetuka: nahetusahetuk = အမြစ် မဟုတ်သော်လည်း အမြစ် ရှိသော
- nahetusahetuka: nahetuahetuk = အမြစ် မဟုတ်၊ အမြစ် မရှိသော
- nahetusahetuka: nahetusahetuk_nahetuahetuk_both = အမြစ် မဟုတ်သော်လည်း အမြစ် ရှိသော၊ အမြစ် မဟုတ်၊ အမြစ် မရှိသော
- sappaccaya: sappaccay = အကြောင်း ရှိသော
- sappaccaya: appaccay = အကြောင်း မရှိသော
- sappaccaya: sappaccay_appaccay_both = အကြောင်း ရှိသော၊ အကြောင်း မရှိသော
- sankhata: saṅkhat = ပြုပြင်ဖန်တီးထားသော
- sankhata: asaṅkhat = ပြုပြင်ဖန်တီးထားခြင်း မရှိသော
- sankhata: saṅkhat_asaṅkhat_both = ပြုပြင်ဖန်တီးထားသော၊ ပြုပြင်ဖန်တီးထားခြင်း မရှိသော
- sanidassana: sanidassan = မြင်နိုင်သော
- sanidassana: anidassan = မမြင်နိုင်သော
- sanidassana: sanidassan_anidassan_both = မြင်နိုင်သော၊ မမြင်နိုင်သော
- sappatigha: sappaṭigh = ထိခိုက်မှု ရှိသော
- sappatigha: appaṭigh = ထိခိုက်မှု မရှိသော
- sappatigha: sappaṭigh_appaṭigh_both = ထိခိုက်မှု ရှိသော၊ ထိခိုက်မှု မရှိသော
- rupi: rūpdk = ရုပ် ဖြစ်သော
- rupi: arūpdk = ရုပ် မဟုတ်သော
- rupi: rūpdk_arūpdk_both = ရုပ် ဖြစ်သော၊ ရုပ် မဟုတ်သော
- lokiya: lokiy = လောကနှင့် သက်ဆိုင်သော
- lokiya: lokuttar = လောကကို ကျော်လွန်သော
- lokiya: lokiy_lokuttar_both = လောကနှင့် သက်ဆိုင်သော၊ လောကကို ကျော်လွန်သော
- kenaci: kenaci viññeyy = တစ်စုံတစ်ခုသော စိတ်ဖြင့် သိနိုင်သော
- kenaci: kenaci naviññeyy = တစ်စုံတစ်ခုသော စိတ်ဖြင့် မသိနိုင်သော
- kenaci: kenaci viññeyy_kenaci_naviññeyy_both = တစ်စုံတစ်ခုသော စိတ်ဖြင့် သိနိုင်သော၊ တစ်စုံတစ်ခုသော စိတ်ဖြင့် မသိနိုင်သော

## Unsure Pāli
- «(hetumūlake tīṇi)» after «Hetu dhammo hetussa dhammassa indriyapaccayena paccayo…» and «(nahetumūlakaṃ tīṇipi
  ekasadisaṃ)»: read as the series that starts from the dyad TERM (hetu / nahetu dhamma), not the hetu condition
  «(အမြစ် ဖြစ်သော သဘောတရားကို အခြေခံခြင်း၌ သုံးခု)»; likewise «Sahetuko ceva na ca hetumūlakaṃ / -e»,
  «sahetukamūlakaṃ», «Appaṭighamūlakaṃ».
- «hetuñca nahetuñca khandhe paṭicca» read as «the root and the non-root aggregates» (hetu the noun, nahetu the
  term on khandhe): «အမြစ်ကိုလည်းကောင်း၊ အမြစ် မဟုတ်သော အစုအဝေးတို့ကိုလည်းကောင်း မှီ၍».
- «(vitthāretabbaṃ yāva. Nahetū khandhā)»: the end point «nahetū khandhā» stands after the full stop; rendered
  «(အောက်ပါအထိ အကျယ် ချဲ့ရမည်။ အမြစ် မဟုတ်သော အစုအဝေးများ)» (SUPPLIED «အောက်ပါ» "the following", the one
  supplied word of this group, so that «yāva» has its object; check in the consistency pass).
- «sappaccayagaṇanāhi» (in the sanidassana dyad) read as the counts of the sappaccaya DYAD: «အကြောင်း ရှိခြင်း
  နှစ်မျိုးတွဲ၏ ရေတွက်ချက်တို့».
- «suddhake» (inside the lokiya note) = «ရိုးရိုး အပိုင်း၌» (the «Suddhaṃ» counting section).

## Source slips (translated as written; read in memory only where a frame needed it; logged by the generator)
- «Sahajātādhipati» without « – » (3-01 Hetuduka pañhāvāra adhipati, segment ^7-24-22): no dash added; the label then the clause.
- «ādhipatiyā cattāri» for «adhipatiyā cattāri» (3-01 Nahetusahetuka counting, segment ^7-24-201): read as adhipatiyā.
- «lokuttarasa dhammassa» for «lokuttarassa» (3-02 Lokiya upanissaya, segment ^7-25-156): read as lokuttarassa.
- «(yāva vatthu nahetū khandhā, ca tāva kātabbaṃ)»: the «, ca» misplaced; rendered as the parallel note
  «(… vatthu nahetū ca khandhā tāva kātabbaṃ)».
- «navapi )», «natthi )» (a space before «)»): the space is not kept in the Burmese.
- «….(1)», «.(n)» without a space: kept as written.
- 3-02 has «Rūpīdukaṃ» twice (^7-3-1-2-74-0 and ^7-3-1-2-100-0): both rendered, the second starts a new part
  with the same dyad.

## For the consistency pass (harmonise)
- H6 (stacked qualifiers): the both-members form «A၊ B N» is used here for two dyad terms on one noun (rūpa,
  khandha, kāya).
- 1-05 lines 81 / 116 «… cakkhāyatanaṃ cakkhuviññāṇassa…pe… kāyāyatanaṃ kāyaviññāṇassa purejātapaccayena …»
  are «မျက်စိ အာရုံခံ နယ်ပယ်၊ မျက်စိ သိစိတ်တို့အား…» there (the subject read as part of the recipient list); here
  «မျက်စိ အာရုံခံ နယ်ပယ်သည် မျက်စိ သိစိတ်အား…» (the primary engine; the only 2 of 29 shared sentences that differ).
- «(evaṃ gaṇetabbaṃ)» is «(ဤသို့ ရေတွက်ရမည်)» in the 2-03 … 2-06 lineage used here and «(ထိုနည်းတူ ရေတွက်ရမည်)» in
  2-07 … 2-11: one form.
- vaṇṇasampadā / patthayamāno follow the 2-12 … 2-17 drafts (not yet finished).
