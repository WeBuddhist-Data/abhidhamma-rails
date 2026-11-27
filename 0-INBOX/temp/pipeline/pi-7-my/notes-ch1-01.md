# pi-7 1-01-kusalattika Burmese zero-shot: notes

PROGRESS: DONE (2026-11-23). `AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters/1-01-kusalattika.md`,
1691 segments, 2551 lines. Translated from the Pāli only (no Burmese translation or nissaya opened, no web search,
`language-priority/` not opened). Meaning cross-checked with the English pi-7 zero-shot only.

## Status (all pass)
| check | result |
|---|---|
| check_chapter_ids.py | OK (1691 segments) |
| check_text (pi-3-mr) on a «…Pe…»-folded copy | OK (2551 lines, dashes match); run by `check_ch1-01.py --pe` (scratch `chk-pe/ch1-01/`, deleted) and by check_text_pe7.py |
| pi-4-mr/check_marks.py | OK |
| check_ch1-01.py | 0 mismatches: S/P/C/O/N 2551 lines each, I 3890 sentences (identity also against the sample 1-00 / 1-02), T 67 table values |
| reuse test | terms 112 / 112 identical (of 197 witnessed values); sentences in pi-1 … pi-6: 278 / 278 identical |
| check_ch1-01.py --mutate | 9 / 9 planted errors caught (count, count above ten, polarity, term order, condition, khandha number, digits, sa-X / a-X, group number) |
| make_ch1-01.py --regress | the approved sample (1-00, 1-02) regenerated through these frames is byte-identical to the published files |

## Files (all in pi-7-my/)
- `make_ch1-01.py`: generator. Imports my7_formulas (read-only) and make_sample (its tables only; its main() is never
  run), then `setup_*()` registers this chapter's frames. `--dev` lists unmatched skeletons in `chk-ch1-01/dev.txt`,
  `--regress` regenerates the sample in memory and compares, `--slips` prints the logged source slips. Reuse from a
  later chapter: `importlib.util.spec_from_file_location("ch101", ".../make_ch1-01.py")` + `exec_module` (setup runs on
  import, nothing is written, set `sys.dont_write_bytecode = True` first).
- `check_ch1-01.py`: independent checker (adapted from check_sample.py + chk_mutate.py); `--mutate`, `--pe`.
- `chk-ch1-01/`: scratch (dev lists, viewers); nothing in it is an output.

## Frames this chapter adds (clean functions of their terms; for the later triads / dyads)
- **NP engine** (`np_my2`, wraps F.np_my; sample output unchanged): commas in NP lists dropped; «Xñca» with a noun head
  = «Xṃ ca» (closing conjunct: «kusalaṃ ekaṃ khandhañca vatthuñca» = [kusalaṃ ekaṃ khandhaṃ] [vatthuṃ]); «A B ca»
  (one closing ca); term-free asyndetic lists «cittasamuṭṭhānaṃ rūpaṃ kaṭattārūpaṃ upādārūpaṃ» = «A၊ B၊ C».
- **Links with coordinated NPs** (`link_np`, `clause2`, `pairs2`): the link's marker inside each conjunct, as pi-2:
  «kusale khandhe ca mahābhūte ca paṭicca» = «ကုသိုလ် အစုအဝေးတို့ကိုလည်းကောင်း၊ မူလဓာတ်ကြီးတို့ကိုလည်းကောင်း မှီ၍»;
  paccayā «…ကြောင့်လည်းကောင်း၊ …ကြောင့်လည်းကောင်း»; sahajātaṃ «…နှင့်လည်းကောင်း၊ … အတူ ပေါ်ပေါက်သော».
- **Pieces** (`pieces`, after the sample's lex fails): a fragment split at «, » / «; » into: a count alone («… tīṇi.»),
  condition kinds, pairs «[prefix] NP LINK [NP]», «[NP-nom] NP-acc Xpaccayā» («khandhā vatthuṃ vippayuttapaccayā» =
  «အစုအဝေးတို့သည် မှီရာ ဝတ္ထုကို ကင်းကွာခြင်းဟူသော အကြောင်းကြောင့်», as the sample's «vatthuṃ vippayuttapaccayā»),
  «NP-nom NP-dat» («saddāyatanaṃ sotaviññāṇassa…»), a verb clause, a bare NP / qualifier / prefix before «…» (a bare
  accusative takes the unit's link marker: «akusalaṃ dhammaṃ…» = «အကုသိုလ် သဘောတရားနှင့်…» in the saṃsaṭṭha section).
- **Condition kinds** of the vibhaṅga (vippayutta / atthi / purejāta …): the bare name N, as the sample's adhipati /
  upanissaya kinds: sahajātaṃ / -o / -ā «အတူ ပေါ်ပေါက်ခြင်း», purejātaṃ «ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်း», pacchājātaṃ / -ā
  «နောက်မှ ဖြစ်ပေါ်ခြင်း», āhāraṃ «အာဟာရ», indriyaṃ «စွမ်းရည်», ārammaṇapurejātaṃ «အာရုံ ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်း»,
  vatthupurejātaṃ «မှီရာ ဝတ္ထု ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်း». In the kamma section the sample's «sahajātā = အတူ ပေါ်ပေါက်သည့်
  ကံ» stays (the generator tracks the current «Xpaccayo» heading).
- **Headings** (`heading_core`): counting groups above ten «Nမျိုးတွဲ»; «Tikādi» / «Chakkādi» «… စသည်»; «Xtikaṃ»
  «N၏ သုံးမျိုးတွဲ»; «Xādidukādi» «N စသည်တို့၏ နှစ်မျိုးတွဲ စသည်»; «X-Ydukāni» «Aနှင့် Bတို့၏ နှစ်မျိုးတွဲများ»;
  «Xādipaccayā» / «Naadhipatyādi» «N စသည်»; «Anulomaṃ – X» / «Paccanīyaṃ – X»; «Gaṇanā Xmūlakā»; ghaṭanā kinds
  «Xsāmaññaghaṭanā» «N၏ သာမန် ပေါင်းစပ်ချက်», «Xmissakaghaṭanā» «N၏ ရောစပ် ပေါင်းစပ်ချက်», «Xpakiṇṇakaghaṭanā»
  «N၏ အထွေထွေ ပေါင်းစပ်ချက်», «Sa-X(-Y)ghaṭanā» «A(၊ B)နှင့် C ပါဝင်သော ပေါင်းစပ်ချက်» (as the sample's
  Saindriya-maggaghaṭanā), «(Sahajāta-)chandādhipatighaṭanā» «(အတူ ပေါ်ပေါက်သော) ဆန္ဒ အကြီးအမှူး၏ ပေါင်းစပ်ချက်»;
  parens «(sāsevanaṃ)» … «(N ပါဝင်သော)» (as the sample's saupanissayaṃ).
- **Editorial notes** (`note_clause`): «(Yathā A, evaṃ [B] V.)» «(Aကဲ့သို့ ထိုနည်းတူ [Bကို] V။)», a place A «… ၌ ရှိသည့်
  အတိုင်း», a gaṇanā A «…အတိုင်း» (as the sample); «(B yathā A, evaṃ V)»; «(B yathā A)» «(Bသည် Aကဲ့သို့ ဖြစ်သည်)»;
  «(B X-sadisaṃ)» «(Bသည် Nနှင့် တူသည်)», -pi items «Nလည်း၊ Nလည်း …» (as the sample's NOTES), «-sadisāni» «… တူကြသည်»,
  «… kātabbaṃ» «… နှင့် တူအောင် ပြုရမည်», «L ṭhitena» «L၌ တည်၍»; «(L X natthi)» «(L၌ X မရှိ)»; «(L idaṃ
  nānākaraṇaṃ)» «(L၌ ဤသည် ကွဲပြားချက် ဖြစ်သည်)»; «(Xttaṃ nāma Yttaṃ …)» «(X ဟူသည် Y ဖြစ်သည်၊ …)»; «Xmūlakaṃ.»
  «Nကို အခြေခံခြင်း။»; «Xvāre ORDER.» «…ဖော်ပြချက်၌ ORDER။»; «Pañhāvārassa X.»; «(Savipākaṃ – 5)» «(N ပါဝင်သော – 5)»,
  «(Avipākaṃ – 4)» «(N မပါဝင်သော – 4)»; a note at the start / middle / end of a unit is split off.
- **Pañhā prose**: «X parikammaṃ Y …paccayena paccayo» «X၏ ကြိုတင် ပြင်ဆင်မှုသည် Yအား …»; «A ca, B ca» recipients
  «Aအားလည်းကောင်း၊ Bအားလည်းကောင်း» (generated for every recipient of LEX); a bare term used as a noun «kusalaṃ
  aniccato / assādeti / garuṃ katvā» «ကုသိုလ်ကို …», before a recipient «ကုသိုလ်သည် …».
- **Ghaṭanā**: «…atthīti / natthīti» and «…ādhipatīti» segmented; the ū-sandhi «ārammaṇūpanissaya»; ghaṭanā lines
  with «-īti» before negative counts.
- **Numbers**: ekādasa … aṭṭhārasa «ဆယ့်တစ်ခု … ဆယ့်ရှစ်ခု»; groups ekādasaka … bāvīsaka; «(sabbattha N)»
  «(နေရာတိုင်း၌ Nခု)»; tiṇṇannaṃ = 3 (khandha / mahābhūta «သုံးပါး»).

## New terms and phrases (Pāli = Burmese)
Generated families (one per condition / count, as the frames above): «(Xpaccayasadisaṃ)» = «(Nနှင့် တူသည်)»,
«(naXpaccayasadisaṃ)» = «(N မဟုတ်ခြင်းနှင့် တူသည်)»; «(sabbattha N)» = «(နေရာတိုင်း၌ Nခု)»; COUNT ekādasa = ဆယ့်တစ်ခု,
dvādasa = ဆယ့်နှစ်ခု, terasa = ဆယ့်သုံးခု, cuddasa = ဆယ့်လေးခု, pannarasa = ဆယ့်ငါးခု, soḷasa = ဆယ့်ခြောက်ခု,
sattarasa = ဆယ့်ခုနစ်ခု, aṭṭhārasa = ဆယ့်ရှစ်ခု; GROUP ekādasaka … aṭṭhārasaka = ဆယ့်တစ်မျိုးတွဲ … ဆယ့်ရှစ်မျိုးတွဲ,
vīsaka = နှစ်ဆယ်မျိုးတွဲ, ekavīsaka = နှစ်ဆယ့်တစ်မျိုးတွဲ, bāvīsaka = နှစ်ဆယ့်နှစ်မျိုးတွဲ; LINK sahajātā / sahajātaṃ =
«Xနှင့်အတူ ပေါ်ပေါက်သော» (as sahajāto), saṃsaṭṭhā = «Xနှင့် ရောနှောသော» (as saṃsaṭṭho).

Words of the frames: missaka = ရောစပ်; sa-X = Nဟူသော အကြောင်း ပါဝင်သော; a-X = Nဟူသော အကြောင်း မပါဝင်သော;
X-mūlakā (adjective) = Nဟူသော အကြောင်းကို အခြေခံသော; gaṇanā = ရေတွက်ချက် (sample); kātabbaṃ / kātabbo = ပြုရမည်;
ṭhitena = …၌ တည်၍; sabbattha = နေရာတိုင်း၌; pañhā / pañho = ပြဿနာ; nānākaraṇaṃ = ကွဲပြားချက်; natthi = မရှိ (sample);
atthi = ရှိ; avasesaṃ / avasesāni = ကြွင်းသည်; avasesāni padāni = ကြွင်းသော ပုဒ်; imāni padāni = ဤ ပုဒ်;
sabbāni padāni = ပုဒ် အားလုံး; ṭhapetvā = ချန်ထား၍ (pi-2); etenupāyena = ဤနည်းဖြင့်; sajjhāyantena = သရဇ္ဈာယ်လျက်;
paripuṇṇaṃ = ပြည့်စုံသည် / ပြည့်စုံစွာ / ပြည့်စုံအောင် (sample «ပြည့်စုံ»); cakkaṃ = စက်ဝိုင်း; bandhitabbaṃ = ဖွဲ့ရမည်;
-sadisāni = …နှင့် တူကြသည်; ekasadisāni = တူညီကြသည်; mūlāni = အခြေခံ; Xttaṃ nāma Yttaṃ = X ဟူသည် Y ဖြစ်သည်;
yāva X = Nအထိ; gaṇite = ရေတွက်သောအခါ; honti = ရှိသည်; alikhitesu = မရေးထားသော; paccanīyavibhaṅge = အငြင်းပြ ပုံစံ၏
ခွဲခြမ်းစိတ်ဖြာခြင်း၌; Paccanīyaṃ (line) = အငြင်းပြ ပုံစံ; Anulomaṃ (heading) = အဟုတ်ပြ ပုံစံ (pi-6).

Nouns, qualifiers and the pañhā lexicon (vipākābyākata and abyākata values are pi-5 rails; «၊» between the two
stacked abyākata qualifiers as pi-5 does between stacked qualifiers):
- (adhipati paṭisandhikkhaṇe natthi.) = (ပဋိသန္ဓေ နေသော ခဏ၌ အကြီးအမှူးဟူသော အကြောင်း မရှိ။)
- (imāni tīṇi mūlāni ekasadisāni) = (ဤ အခြေခံ သုံးခုတို့သည် တူညီကြသည်)
- (kātabbaṃ) = (ပြုရမည်)
- (naāsevanapaccayamūlakampi nahetumūlakasadisaṃ.) = (အလေ့အကျင့် ပြုခြင်းဟူသော အကြောင်း မဟုတ်ခြင်းကို အခြေခံခြင်းသည်လည်း အမြစ်ဟူသော အကြောင်း မဟုတ်ခြင်းကို အခြေခံခြင်းနှင့် တူသည်။)
- (saṃkhittaṃ.) = (အကျဉ်းချုပ်။)
- abhijjhā = သူ့ဥစ္စာကို လိုချင်ခြင်း
- abhijjhāya = သူ့ဥစ္စာကို လိုချင်ခြင်း
- abhinandati = နှစ်သက်သည်
- adinnaṃ ādiyitvā = မပေးသည်ကို ယူ၍
- adinnādānassa = မပေးသည်ကို ယူခြင်း
- adinnādānaṃ = မပေးသည်ကို ယူခြင်း
- adinnādāno = မပေးသည်ကို ယူခြင်း
- ahetukavipākābyākatā = အမြစ် မရှိသော ကံ၏ အကျိုး ဖြစ်သော ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော
- ahetukā = အမြစ် မရှိသော
- akusalacittasamaṅgissa = အကုသိုလ် စိတ်နှင့် ပြည့်စုံသူ
- akusalādhipati = အကုသိုလ် အကြီးအမှူး
- akusalāni = အကုသိုလ်
- anuppannaṃ kiriyasamāpattiṃ uppādeti = မဖြစ်ပေါ်သေးသော ပြုရုံမျှသာ ဖြစ်သော သမာပတ်ကို ဖြစ်စေသည်
- anuppannaṃ samāpattiṃ uppādenti = မဖြစ်ပေါ်သေးသော သမာပတ်ကို ဖြစ်စေကြသည်
- anāgataṃsañāṇaṃ = အနာဂတ်ကို သိသော ဉာဏ်
- arahantaghātikammassa = ရဟန္တာကို သတ်သော ကံ
- arahantaghātikammaṃ = ရဟန္တာကို သတ်သော ကံ
- arahantaṃ jīvitā voropetvā = ရဟန္တာကို အသက်မှ သတ်၍
- arahato = ရဟန္တာ
- arahā = ရဟန္တာ
- asaññasattānaṃ = အသညသတ်တို့၏
- assādeti = သာယာသည်
- atthappaṭisambhidāya = အကျိုးအနက်ကို ပိုင်းခြားသိသော ဉာဏ်
- bhojanaṃ = အစားအစာ
- byāpādassa = ဖျက်ဆီးလိုစိတ်
- byāpādaṃ = ဖျက်ဆီးလိုစိတ်
- byāpādo = ဖျက်ဆီးလိုစိတ်
- bāhiraṃ = ပြင်ပ
- bāhire = ပြင်ပ
- cakkhuviññāṇassa = မျက်စိ သိစိတ်
- cakkhuviññāṇaṃ = မျက်စိ သိစိတ်
- cakkhuṃ = မျက်စိ
- catutthassa jhānassa = စတုတ္ထ ဈာန်
- catutthassa maggassa = စတုတ္ထ မဂ်
- catutthaṃ jhānaṃ = စတုတ္ထ ဈာန်
- catuttho maggo = စတုတ္ထ မဂ်
- cetopariyañāṇaṃ = စိတ်ကို ပိုင်းခြား၍ သိသော ဉာဏ်
- cittasamuṭṭhānañca = စိတ်မှ ဖြစ်ပေါ်လာသော
- cittasamuṭṭhānaṃ = စိတ်မှ ဖြစ်ပေါ်လာသော
- dhammappaṭisambhidāya = တရားကို ပိုင်းခြားသိသော ဉာဏ်
- dibbacakkhu = နတ်မျက်စိ
- dibbasotadhātu = နတ်နား ဓာတ်
- dibbassa cakkhussa = နတ်မျက်စိ
- dibbena cakkhunā = နတ်မျက်စိ
- dibbāya sotadhātuyā = နတ်နား ဓာတ်
- dibbāya sotadhātuyā saddaṃ suṇanti = နတ်နား ဓာတ်ဖြင့် အသံကို ကြားကြသည်
- dibbāya sotadhātuyā saddaṃ suṇāti = နတ်နား ဓာတ်ဖြင့် အသံကို ကြားသည်
- dutiyassa jhānassa = ဒုတိယ ဈာန်
- dutiyassa maggassa = ဒုတိယ မဂ်
- dutiyaṃ jhānaṃ = ဒုတိယ ဈာန်
- dutiyo maggo = ဒုတိယ မဂ်
- duṭṭhena cittena tathāgatassa lohitaṃ uppādetvā = ပြစ်မှားသော စိတ်ဖြင့် မြတ်စွာဘုရား၏ သွေးကို ထွက်စေ၍
- ekāgārikaṃ karitvā = အိမ်တစ်လုံးတည်းကို ဝိုင်း၍ တိုက်ပြီး
- gandhe = အနံ့
- ghānaviññāṇassa = နှာခေါင်း သိစိတ်
- ghānaviññāṇaṃ = နှာခေါင်း သိစိတ်
- ghānaṃ = နှာခေါင်း
- gotrabhuṃ = အနွယ် ပြောင်းခြင်း စိတ်
- gāmaghātaṃ karitvā = ရွာကို ဖျက်ဆီး၍ လုယက်ပြီး
- iddhividhañāṇaṃ = တန်ခိုး အမျိုးမျိုးကို ပြနိုင်သော ဉာဏ်
- indriyā = စွမ်းရည်
- jhānaṃ = ဈာန်
- jivhaṃ = လျှာ
- jivhāviññāṇassa = လျှာ သိစိတ်
- jivhāviññāṇaṃ = လျှာ သိစိတ်
- kabaḷīkāro āhāro = လုတ်ပြု၍ စားရသော အာဟာရ
- kammaṃ = ကံ
- kaṭattā ca rūpaṃ = ကံ ပြုခဲ့သောကြောင့် ဖြစ်သော ရုပ်
- kaṭattārūpaṃ = ကံ ပြုခဲ့သောကြောင့် ဖြစ်သော ရုပ်
- kiriyassa = ပြုရုံမျှသာ ဖြစ်သော စိတ်
- kiriyābyākatassa = ပြုရုံမျှသာ ဖြစ်သော ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော
- kiriyābyākataṃ = ပြုရုံမျှသာ ဖြစ်သော ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော
- kiriyābyākate = ပြုရုံမျှသာ ဖြစ်သော ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော
- kiriyābyākato = ပြုရုံမျှသာ ဖြစ်သော ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော
- kiriyābyākatāni = ပြုရုံမျှသာ ဖြစ်သော ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော
- kusalacittasamaṅgissa = ကုသိုလ် စိတ်နှင့် ပြည့်စုံသူ
- kusalādhipati = ကုသိုလ် အကြီးအမှူး
- kusalāni = ကုသိုလ်
- kāmesumicchācārassa = ကာမတို့၌ မှားယွင်းစွာ ကျင့်ခြင်း
- kāmesumicchācāraṃ = ကာမတို့၌ မှားယွင်းစွာ ကျင့်ခြင်း
- kāmesumicchācāro = ကာမတို့၌ မှားယွင်းစွာ ကျင့်ခြင်း
- kāyaviññāṇassa = ကိုယ် သိစိတ်
- kāyaviññāṇaṃ = ကိုယ် သိစိတ်
- kāyaṃ = ကိုယ်
- kāyikassa dukkhassa = ကိုယ်ပိုင်းဆိုင်ရာ နာကျင်မှု
- kāyikassa sukhassa = ကိုယ်ပိုင်းဆိုင်ရာ သာယာမှု
- kāyikaṃ dukkhaṃ = ကိုယ်ပိုင်းဆိုင်ရာ နာကျင်မှု
- kāyikaṃ sukhaṃ = ကိုယ်ပိုင်းဆိုင်ရာ သာယာမှု
- maggaṃ = မဂ်
- mahābhūtassa = မူလဓာတ်ကြီး
- mahābhūtaṃ = မူလဓာတ်ကြီး
- mahābhūte = မူလဓာတ်ကြီး
- mahābhūtānaṃ = မူလဓာတ်ကြီး
- micchādiṭṭhi = မှားယွင်းသော အယူ
- micchādiṭṭhiyā = မှားယွင်းသော အယူ
- musā bhaṇitvā = မုသား ပြော၍
- musāvādassa = မုသား ပြောခြင်း
- musāvādaṃ = မုသား ပြောခြင်း
- musāvādo = မုသား ပြောခြင်း
- mātaraṃ jīvitā voropetvā = အမိကို အသက်မှ သတ်၍
- mātughātikammassa = အမိကို သတ်သော ကံ
- mātughātikammaṃ = အမိကို သတ်သော ကံ
- nevasaññānāsaññāyatanakiriyassa = မှတ်သိမှု ရှိသည်လည်း မဟုတ်၊ မှတ်သိမှု မရှိသည်လည်း မဟုတ်သော နယ်ပယ် ပြုရုံမျှသာ ဖြစ်သော စိတ်
- nevasaññānāsaññāyatanakiriyaṃ = မှတ်သိမှု ရှိသည်လည်း မဟုတ်၊ မှတ်သိမှု မရှိသည်လည်း မဟုတ်သော နယ်ပယ် ပြုရုံမျှသာ ဖြစ်သော စိတ်
- nevasaññānāsaññāyatanakusalassa = မှတ်သိမှု ရှိသည်လည်း မဟုတ်၊ မှတ်သိမှု မရှိသည်လည်း မဟုတ်သော နယ်ပယ် ကုသိုလ်
- nevasaññānāsaññāyatanakusalaṃ = မှတ်သိမှု ရှိသည်လည်း မဟုတ်၊ မှတ်သိမှု မရှိသည်လည်း မဟုတ်သော နယ်ပယ် ကုသိုလ်
- nevasaññānāsaññāyatanavipākassa = မှတ်သိမှု ရှိသည်လည်း မဟုတ်၊ မှတ်သိမှု မရှိသည်လည်း မဟုတ်သော နယ်ပယ် ကံ၏ အကျိုး
- nibbānaṃ = နိဗ္ဗာန်
- nigamaghātaṃ karitvā = နိဂုံးကို ဖျက်ဆီး၍ လုယက်ပြီး
- nillopaṃ haritvā = ဥစ္စာကို လုယူ၍
- niruddhe vipāko tadārammaṇatā uppajjati = ချုပ်ငြိမ်းသောအခါ ကံ၏ အကျိုး ဖြစ်သော စိတ်သည် ထိုအာရုံကို အာရုံပြုသည့် အနေဖြင့် ဖြစ်ပေါ်သည်
- niruttippaṭisambhidāya = စကားဖြင့် ဖော်ပြမှုကို ပိုင်းခြားသိသော ဉာဏ်
- niyatamicchādiṭṭhi = ကျိန်းသေသော မှားယွင်းသော အယူ
- niyatamicchādiṭṭhiyā = ကျိန်းသေသော မှားယွင်းသော အယူ
- paradāraṃ gantvā = သူတစ်ပါး၏ မယားထံ သွား၍
- parikammaṃ = ကြိုတင် ပြင်ဆင်မှု
- paripanthe ṭhatvā = လမ်းခရီး၌ ဓားပြ တိုက်ပြီး
- pañcaviññāṇasahagataṃ = သိစိတ် ငါးပါးနှင့်အတူ ဖြစ်သော
- paṭhamassa jhānassa = ပထမ ဈာန်
- paṭhamassa maggassa = ပထမ မဂ်
- paṭhamaṃ jhānaṃ = ပထမ ဈာန်
- paṭhamo maggo = ပထမ မဂ်
- paṭibhānappaṭisambhidāya = ဉာဏ်ပေါ်မှုကို ပိုင်းခြားသိသော ဉာဏ်
- phalasamāpatti = ဖိုလ်သမာပတ်
- pharusavācā = ကြမ်းတမ်းသော စကား
- pharusaṃ bhaṇitvā = ကြမ်းတမ်းသော စကားကို ပြော၍
- pharusāya vācāya = ကြမ်းတမ်းသော စကား
- phoṭṭhabbe = အထိအတွေ့
- pisuṇavācā = ကုန်းတိုက်သော စကား
- pisuṇaṃ bhaṇitvā = ကုန်းတိုက်သော စကားကို ပြော၍
- pisuṇāya vācāya = ကုန်းတိုက်သော စကား
- pitaraṃ jīvitā voropetvā = အဖကို အသက်မှ သတ်၍
- pitughātikammassa = အဖကို သတ်သော ကံ
- pitughātikammaṃ = အဖကို သတ်သော ကံ
- pubbe suciṇṇāni = ရှေးက ကောင်းစွာ ကျင့်ခဲ့ဖူးသော အမှု
- pubbenivāsānussatiñāṇaṃ = ရှေးဘဝများကို အဖန်ဖန် အောက်မေ့နိုင်သော ဉာဏ်
- purejātaṃ = ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်း
- purejātaṃ = ရှေးဦးစွာ ဖြစ်ပေါ်ပြီးသော
- pāṇaṃ hantvā = သတ္တဝါကို သတ်၍
- pāṇātipātassa = သူ့အသက်ကို သတ်ခြင်း
- pāṇātipātaṃ = သူ့အသက်ကို သတ်ခြင်း
- pāṇātipāto = သူ့အသက်ကို သတ်ခြင်း
- rase = အရသာ
- ruhiruppādakammassa = မြတ်စွာဘုရား၏ သွေးကို ထွက်စေသော ကံ
- ruhiruppādakammaṃ = မြတ်စွာဘုရား၏ သွေးကို ထွက်စေသော ကံ
- rūpaṃ passanti = အဆင်းအရောင်ကို မြင်ကြသည်
- rūpaṃ passati = အဆင်းအရောင်ကို မြင်သည်
- rūpe = အဆင်းအရောင်
- saddaṃ suṇanti = အသံကို ကြားကြသည်
- saddaṃ suṇāti = အသံကို ကြားသည်
- sadde = အသံ
- samphappalāpassa = အကျိုးမဲ့ ပြိန်ဖျင်းသော စကား
- samphappalāpaṃ = အကျိုးမဲ့ ပြိန်ဖျင်းသော စကား
- samphappalāpo = အကျိုးမဲ့ ပြိန်ဖျင်းသော စကား
- samphaṃ palapitvā = အကျိုးမဲ့ ပြိန်ဖျင်းသော စကားကို ပြော၍
- sandhiṃ chinditvā = အိမ်ကို ဖောက်ထွင်း၍
- saṅghabhedakammassa = သံဃာကို ဖြိုခွဲသော ကံ
- saṅghabhedakammaṃ = သံဃာကို ဖြိုခွဲသော ကံ
- saṅghaṃ bhinditvā = သံဃာကို ဖြိုခွဲ၍
- saṅkhāre = ပြုပြင်ဖန်တီးမှု
- sekkhā = ကျင့်ကြံဆဲသူ
- sekkhā vā puthujjanā vā = ကျင့်ကြံဆဲသူတို့သော်လည်းကောင်း၊ ပုထုဇဉ်တို့သော်လည်းကောင်း
- sekkhānaṃ = ကျင့်ကြံဆဲသူ
- sekkhāya = ကျင့်ကြံဆဲသူ၏
- sekkhāya phalasamāpattiyā = ကျင့်ကြံဆဲသူ၏ ဖိုလ်သမာပတ်
- senāsanaṃ = အိပ်ရာ နေရာ
- sotaviññāṇassa = နား သိစိတ်
- sotaviññāṇaṃ = နား သိစိတ်
- sotaṃ = နား
- tassa paṭighātatthāya = ထိုအမှုကို ပယ်ဖျက်ရန်အတွက်
- tatiyassa jhānassa = တတိယ ဈာန်
- tatiyassa maggassa = တတိယ မဂ်
- tatiyaṃ jhānaṃ = တတိယ ဈာန်
- tatiyo maggo = တတိယ မဂ်
- upanissaya = အားကြီးသော အမှီ
- uppannaṃ samāpajjanti = ဖြစ်ပေါ်ပြီးသော သမာပတ်ကို ဝင်စားကြသည်
- uppannaṃ samāpajjati = ဖြစ်ပေါ်ပြီးသော သမာပတ်ကို ဝင်စားသည်
- upādārūpaṃ = မူလဓာတ်ကြီးတို့ကို မှီ၍ ဖြစ်သော ရုပ်
- utu = ရာသီဥတု
- utusamuṭṭhānaṃ = ရာသီဥတုမှ ဖြစ်ပေါ်လာသော
- utusamuṭṭhāne = ရာသီဥတုမှ ဖြစ်ပေါ်လာသော
- utuṃ = ရာသီဥတု
- vatthu = မှီရာ ဝတ္ထု
- vatthussa = မှီရာ ဝတ္ထု
- vicikicchaṃ = ယုံမှားမှု
- vipassanti = ထိုးထွင်း၍ ရှုကြသည်
- vipākassa = ကံ၏ အကျိုး
- vipākābyākatakiriyābyākatacittasamaṅgissa = ကံ၏ အကျိုး ဖြစ်သော ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော၊ ပြုရုံမျှသာ ဖြစ်သော ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော စိတ်နှင့် ပြည့်စုံသူ
- vipākābyākatakiriyābyākatādhipati = ကံ၏ အကျိုး ဖြစ်သော ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော၊ ပြုရုံမျှသာ ဖြစ်သော ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော အကြီးအမှူး
- vipākābyākatassa = ကံ၏ အကျိုး ဖြစ်သော ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော
- vipākābyākataṃ = ကံ၏ အကျိုး ဖြစ်သော ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော
- vipākābyākate = ကံ၏ အကျိုး ဖြစ်သော ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော
- vipākābyākate kiriyābyākate khandhe = ကံ၏ အကျိုး ဖြစ်သော ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော၊ ပြုရုံမျှသာ ဖြစ်သော ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော အစုအဝေး
- vipākābyākato = ကံ၏ အကျိုး ဖြစ်သော ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော
- vipākābyākatā = ကံ၏ အကျိုး ဖြစ်သော ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော
- vipākābyākatānaṃ = ကံ၏ အကျိုး ဖြစ်သော ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော
- vipākābyākatāni = ကံ၏ အကျိုး ဖြစ်သော ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော
- viññāṇañcāyatanakiriyassa = အဆုံး မရှိသော သိစိတ် နယ်ပယ် ပြုရုံမျှသာ ဖြစ်သော စိတ်
- viññāṇañcāyatanakiriyaṃ = အဆုံး မရှိသော သိစိတ် နယ်ပယ် ပြုရုံမျှသာ ဖြစ်သော စိတ်
- viññāṇañcāyatanakusalassa = အဆုံး မရှိသော သိစိတ် နယ်ပယ် ကုသိုလ်
- viññāṇañcāyatanakusalaṃ = အဆုံး မရှိသော သိစိတ် နယ်ပယ် ကုသိုလ်
- viññāṇañcāyatanavipākassa = အဆုံး မရှိသော သိစိတ် နယ်ပယ် ကံ၏ အကျိုး
- viññāṇañcāyatanaṃ = အဆုံး မရှိသော သိစိတ် နယ်ပယ်
- yathākammūpagañāṇaṃ = ကံအားလျော်စွာ ဖြစ်ပေါ်ပုံကို သိသော ဉာဏ်
- āhārasamuṭṭhānaṃ = အာဟာရမှ ဖြစ်ပေါ်လာသော
- āhārasamuṭṭhāne = အာဟာရမှ ဖြစ်ပေါ်လာသော
- āhārā = အာဟာရ
- ākiñcaññāyatanakiriyassa = ဘာမျှ မရှိသော နယ်ပယ် ပြုရုံမျှသာ ဖြစ်သော စိတ်
- ākiñcaññāyatanakiriyaṃ = ဘာမျှ မရှိသော နယ်ပယ် ပြုရုံမျှသာ ဖြစ်သော စိတ်
- ākiñcaññāyatanakusalassa = ဘာမျှ မရှိသော နယ်ပယ် ကုသိုလ်
- ākiñcaññāyatanakusalaṃ = ဘာမျှ မရှိသော နယ်ပယ် ကုသိုလ်
- ākiñcaññāyatanassa = ဘာမျှ မရှိသော နယ်ပယ်
- ākiñcaññāyatanavipākassa = ဘာမျှ မရှိသော နယ်ပယ် ကံ၏ အကျိုး
- ākāsānañcāyatanakiriyassa = အဆုံး မရှိသော ဟင်းလင်းပြင် နယ်ပယ် ပြုရုံမျှသာ ဖြစ်သော စိတ်
- ākāsānañcāyatanakiriyaṃ = အဆုံး မရှိသော ဟင်းလင်းပြင် နယ်ပယ် ပြုရုံမျှသာ ဖြစ်သော စိတ်
- ākāsānañcāyatanakusalassa = အဆုံး မရှိသော ဟင်းလင်းပြင် နယ်ပယ် ကုသိုလ်
- ākāsānañcāyatanakusalaṃ = အဆုံး မရှိသော ဟင်းလင်းပြင် နယ်ပယ် ကုသိုလ်
- ākāsānañcāyatanassa = အဆုံး မရှိသော ဟင်းလင်းပြင် နယ်ပယ်
- ākāsānañcāyatanavipākassa = အဆုံး မရှိသော ဟင်းလင်းပြင် နယ်ပယ် ကံ၏ အကျိုး
- ṭhānāṭhānakosallassa = ဖြစ်နိုင်ခြင်းနှင့် မဖြစ်နိုင်ခြင်း၌ ကျွမ်းကျင်ခြင်း

## Points for the coordinator
1. Condition kinds (vippayutta / atthi / purejāta vibhaṅga) are named by the bare condition name N («Sahajātā –»
   «အတူ ပေါ်ပေါက်ခြင်း –»), apart from the sample's kamma kinds «အတူ ပေါ်ပေါက်သည့် ကံ», «ခဏ ကွဲပြားသည့် ကံ». The same Pāli
   word «sahajātā» therefore has two renderings by section (kamma vs the other conditions); the I-test (sentence
   identity) is not affected because the sentences differ.
2. «(Savipākaṃ – 5)» / «(Avipākaṃ – 4)» use the heading form «… ပါဝင်သော» / «… မပါဝင်သော» (attributive before a dash).
   Alternative: a predicate «… ပါဝင်သည်» in these brackets only.
3. vipākābyākataṃ kiriyābyākataṃ (two stacked qualifiers, «either … or») = «VIPAKABY၊ KIRIYABY» (a «၊» between them);
   with ahetuka in front no «၊» (it qualifies both), as the sample's «အမြစ် မရှိသော သာယာသော …».
4. «purejātaṃ» is a qualifier «ရှေးဦးစွာ ဖြစ်ပေါ်ပြီးသော» before a noun («purejātaṃ vatthu», pi-2) and a kind label
   «ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်း» before a sentence («Purejātaṃ sekkhā vā …», «purejātaṃ cakkhuṃ assādeti», no dash in the
   Pāli, so none in the Burmese).
5. tadārammaṇatā «ထိုအာရုံကို အာရုံပြုသည့် အနေဖြင့်» (plain; not the loan word တဒါရုံ).
6. parikamma «ကြိုတင် ပြင်ဆင်မှု» (the pi-5 termbase has parikamma «ပွတ်တိုက်ပေးခြင်း», massage, another sense).
7. asaññasattānaṃ (genitive before «ekaṃ mahābhūtaṃ») «အသညသတ်တို့၏» (pi-5 «အသညသတ်»).

## Unsure Pāli
- «(Yāvāsevanā sabbaṃ sadisaṃ, nakamme gaṇite pañca pañhā honti.)» read "up to āsevana all is the same; when na-kamma
  is counted there are five questions".
- «(Naadhipatimūlakaṃ nahetumhi ṭhitena nahetumūlakasadisaṃ kātabbaṃ.)» "standing at na-hetu, the na-adhipati series
  is to be made like the na-hetu series".
- «(Cakkaṃ bandhitabbaṃ / kātabbaṃ)» «စက်ဝိုင်း ဖွဲ့ရမည် / ပြုရမည်» (the deeds are to be linked in a wheel).
- «tassa paṭighātatthāya» «ထိုအမှုကို ပယ်ဖျက်ရန်အတွက်» (to counteract that deed).
- «Kusalo ca abyākato ca dhammā kusalassa dhammassa sahajātaṃ, purejātaṃ.» (paccanīyuddhāra, no «…paccayena paccayo»):
  «… သဘောတရားအား အတူ ပေါ်ပေါက်ခြင်း၊ ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်း။» (kinds of the atthi condition, as the Pāli lists them).
- «pubbe suciṇṇāni» «ရှေးက ကောင်းစွာ ကျင့်ခဲ့ဖူးသော အမှုတို့» (the noun «အမှု» is added for plain Burmese).

## Source slips (translated as the intended reading; logged by the generator, `--slips`)
- Negations written apart or with a hyphen: «na ārammaṇe», «na adhipatiyā», «na pacchājāte», «na āsevane», «na jhāne»,
  «na indriye», «no avigate», «na-ārammaṇe», «na aññamaññapaccayā», «na hetupaccayā», «Na jhāne idaṃ» (read naX);
  «Nadhipatipaccayā» (= Naadhipati-); «naṃindriye»; «naaññamañña-paccayā»; «naanantare sattaṃ» (= satta).
- «adhipati paccayena» (^7-2-415) written apart; «dve khandha nissāya» (nissayavāra) for «dve khandhe»;
  «vippassati / vippassanti» for «vipassati»; «paññaṃ upanissaya dānaṃ deti» (upanissaya section, Pāli line 2325) for «upanissāya»;
  «(Saṅkhitaṃ.» (^7-2-70) for «Saṃkhittaṃ»; «(yathā nahetumūlakaṃ {nahetumūlake (syā.)}.» without its closing bracket
  (kept without it).
- Ghaṭanā: 233 missing hyphens («sahajātaaññamañña», «vippayuttaatthi», «atthiavigata» …), spaces at hyphens («Hetu
  -sahajāta», «nissaya -vipāka» …), «vippayuttaṃ-» (ṃ), «Avigata āhāra-atthīti» (hyphen missing); all segmented by stem.
- Labels without a dash: «Purejātaṃ sekkhā vā …» (atthi section, Pāli line 2460), «Pacchājātā kusalā khandhā ca
  rūpajīvitindriyañca …» (line 2463; its pair line 2465 has «Pacchājātā –»): kept without a dash (dash rule).
- «akusale niruddhe vipāko …» and «kusale niruddhe vipāko …» kept as written (Marathi notes one possible kusala/akusala
  slip at ^7-2-409; not changed).
