# pi-2 Burmese zero-shot, chapters 5, 7, 8, 9, 10, 11: working notes

Brief: burmese-zeroshot-brief.md. Model: the approved pi-2 sample (my2_formulas.py, make_sample.py, check_sample.py).
Pāli only; no Burmese translation or nissaya opened; no web search. my2_formulas.py, my2-zeroshot-terms.md and pi-1-my
only read (no bytecode). Nothing committed.

## Status (2026-11-17): done
- [x] 5-indriyavibhango (11 segments), 7-satipatthanavibhango (45), 8-sammappadhanavibhango (47),
  9-iddhipadavibhango (49), 10-bojjhangavibhango (26), 11-maggangavibhango (28).
- check_chapter_ids / pi-6-mr/check_text_pe / pi-4-mr/check_marks: OK on all six (my chk-pe copies deleted).
- check_ch5-7-11.py: 0 mismatches on all six; consistency (same Pāli sentence = same Burmese, the six chapters and
  the sample chapter 1): 0 conflicts; pi-1 reuse 16 / 16 (ch5 2, ch7 6, ch8 2, ch9 2, ch10 2, ch11 2: headings
  Tikaṃ / Dukaṃ, «Tattha katamā sati?», «Tattha katamaṃ sampajaññaṃ?»).
- Regenerate: `python3 -I -X utf8 make_ch5-7-11.py [chapter …]` (rewrites the «New strings» section below).
  Check: `python3 -I -X utf8 check_ch5-7-11.py` (no arguments = the six chapters).
- The English pi-2 rails folder named in the brief does not exist yet; no meaning cross-check was possible there.

## Method
- make_ch5-7-11.py imports my2_formulas (F) and extends its tables IN MEMORY only (KH subjects, NOUN manindriya,
  HEAD, COLO, TERM_IRREG, EXTRA_RULES, a wrapper around F.term_my for «-ñcā» / «-ñceva» and free «na» + term).
- pi-1 FINAL Burmese is READ from the pi-1 rails text, sentence-aligned, and asserted (no retyping): the synonym lists
  (citta, vitakka, pīti, samādhi, vīriya, sati, saddhā, paññā with the three lokuttara heads, the three virati
  lists, passaddhi, rūpa / arūpa jīvita, itthi / purisa, the five feeling formulas, rāga), the indriya names
  (anaññātaññassāmītindriya, aññindriya, aññātāvindriya from the pi-1 closers), the lokuttara jhāna opening (2-03)
  and its vipāka (2-05), the four jhāna formulas (2-02, without the kasiṇa), the sammappadhāna formula (4-03
  «Saṃviggassa ca yoniso padhānaṃ»), the root / aggregate / kamma sentences (4-01), «Dukkhe ñāṇaṃ …» (4-01),
  the cakkhu / kāya definitions (3-02: first clause + last item around «…»), the hindrance names (4-02).
- Pañhāpucchaka: F's engine (sentence by sentence, first letter lowered, subjectless = plural) with the new subjects
  (indriya counts, single indriyas, bojjhaṅga / maggaṅga / iddhipāda subjects).
- Suttanta / abhidhamma prose: the generator's own clause engine (RULES, phrase table PH, list parser, quote rules).

## Choices (all strings in «New strings»)
- Chapter titles «X များကို ခွဲခြမ်းစိတ်ဖြာခြင်း» with the pi-1 words: indriya စွမ်းရည်, satipaṭṭhāna သတိပဋ္ဌာန်,
  sammappadhāna မှန်ကန်သော ကြိုးပမ်းအားထုတ်ခြင်း, iddhipāda ဣဒ္ဓိပါဒ်, bojjhaṅga ဗောဇ္ဈင်, maggaṅga မဂ်၏ အင်္ဂါ.
- -niddeso = «…ကို ဖွင့်ဆိုချက်» (heading and colophon).
- Satipaṭṭhāna: anupassī «အဖန်ဖန် ရှုသူ», anupassanā «အဖန်ဖန် ရှုခြင်း», viharati «နေ၏»; «kāye kāyānupassī viharati»
  = «ကိုယ်၌ ကိုယ်ကို အဖန်ဖန် ရှုသူ ဖြစ်လျက် နေ၏»; ātāpī «ထက်သန်သော လုံ့လ ရှိသူ» (ātāpa «ထက်သန်သော လုံ့လ», kept
  apart from vīriya / vāyāma / padhāna), sampajāno «ကောင်းစွာ ဆင်ခြင်သိမြင်သူ» (pi-1 sampajañña), satimā «သတိ ရှိသူ»
  (pi-1); vineyya … = «လောက၌ သူ့ဥစ္စာကို လိုချင်ခြင်းနှင့် စိတ်ဆင်းရဲမှုကို ပယ်ဖျောက်၍».
- ajjhattaṃ / bahiddhā / ajjhattabahiddhā = the pi-1 terms (မိမိ၌ ရှိသော …); «atthi me ajjhattaṃ» = «ငါ၏ အတွင်း၌»,
  «atthissa» = «ထိုသူ၌»; santaṃ / asantaṃ = «ရှိနေသော / မရှိနေသော»; X vā = «Xကိုဖြစ်စေ» (pi-1 «ဖြစ်စေ»).
- Feelings: sāmisa / nirāmisa = «ကာမဂုဏ်နှင့် စပ်သော / မစပ်သော» (also nirāmisā pīti, ch10).
- Mind states: the pi-1 terms for mahaggata, sauttara, anuttara; saṃkhitta «တွန့်ဆုတ်နေသော», vikkhitta «ပျံ့လွင့်နေသော»
  (vikkhepa = pi-1 ပျံ့လွင့်), samāhita «တည်ကြည်သော» (samādhiyati «တည်ကြည်၏»), vimutta «လွတ်မြောက်သော».
- 31 body parts: plain everyday Burmese words; hadayaṃ (heart, organ) = «နှလုံး», kept apart from the pi-1 citta-list
  hadayaṃ «နှလုံးသား» (another sense).
- upeto … samannāgato (7 words) = «ယှဉ်သူ၊ ကောင်းစွာ ယှဉ်သူ၊ ချဉ်းကပ်သူ၊ ကောင်းစွာ ချဉ်းကပ်သူ၊ ရောက်ရှိသူ၊ ပြည့်စုံသူ၊
  အပြည့်အဝ ပြည့်စုံသူ ဖြစ်၏»; «Tena vuccati "X"ti» = «ထို့ကြောင့် “X”ဟု ဆိုသည်»; «X-ti.» = «X ဟူသည်။» (pi-1
  make_ch4 «Saṃvegoti»).
- Iddhipāda: chanda- / vīriya- / citta- / vīmaṃsāsamādhi = «ဆန္ဒ / ဝီရိယ / စိတ် / စုံစမ်းဆင်ခြင်မှု သမာဓိ»
  (vīmaṃsā = pi-1); padhānasaṅkhāra = «ကြိုးပမ်းအားထုတ်ခြင်း ပြုပြင်ဖန်တီးမှု»; samannāgata = «အပြည့်အဝ ပြည့်စုံ»;
  iddhi list new (11 items, all distinct).
- Bojjhaṅga: upekkhāsambojjhaṅgo «ဥပေက္ခာ ဗောဇ္ဈင်» (the other six from pi-1); the upekkhā list new; viveka-,
  virāga-, nirodha-nissita, vossaggapariṇāmī = «ကင်းဆိတ်ခြင်းကို / ပြယ်ပျောက်ခြင်းကို / ချုပ်ငြိမ်းခြင်းကို မှီသော၊
  စွန့်လွှတ်ခြင်းသို့ ညွတ်သော» (viveka, virāga as in the pi-1 jhāna formulas).
- Path: ariyo aṭṭhaṅgiko maggo «အင်္ဂါ ရှစ်ပါး ရှိသော အရိယာ မဂ်»; the nekkhamma / abyāpāda / avihiṃsā saṅkappas, the
  four speech and three body abstentions (veramaṇī = pi-1 ကင်းဝေးခြင်း), ariyasāvaka «အရိယာ တပည့်».
- Unquoted «na vattabbā A-tipi, B-tipi» (ch7-11, no quotes and no dash in the Pāli): rendered without quotes and
  without dash, as written: «A သဘောတရားဟုလည်းကောင်း၊ B …ဟုလည်းကောင်း ခေါ်ဆို၍ မရ».
- Free «na» + mātikā term not in the pi-1 table (na maggārammaṇā, na appamāṇārammaṇaṃ, na maggādhipatino) = pi-1
  rule no_(): «… သည် မဟုတ်သော».
- Pañhā subjects: «Dasindriyā» = «စွမ်းရည် ဆယ်ပါး»; 11-18 «ဆယ့်…», 21 «နှစ်ဆယ့်တစ်», 22 «နှစ်ဆယ့်နှစ်».

## Unsure Pāli / to confirm
- ch5 vīriya list: Vb «thāmo ṭhiti» where Dhs has «thāmo dhiti»: translated as written, ṭhiti = «တည်တံ့ခြင်း» (pi-1
  ṭhiti); dhiti («ဇွဲ») may be the intended reading.
- ch10 «Pītimanassa kāyopi passambhati»: kāya rendered plainly «ကိုယ်»; pi-1 renders kāya- in kāyapassaddhi as
  «စိတ်၏ အဖော်တို့» (the mental body). The line «Atthi kāyapassaddhi» keeps the pi-1 name.
- ch7 «Pañcapi upādānakkhandhā» = «စွဲလမ်းမှု၏ အာရုံ ဖြစ်သော အစုအဝေး ငါးပါး»: upādānakkhandha is new here; the sacca
  chapter (another agent) may choose otherwise (consistency pass).
- ch9 «Tathābhūtassa» = «ထိုသို့ ဖြစ်သူ၏» (of one who is in that state).

## Source slips (translated as written unless noted)
- ch5 ^2-219 block (line 18): «arūpajīvatindriyaṃ» read as arūpajīvitindriyaṃ.
- ch5 ^2-223 (line 49): «"mahaggatārammaṇa"nti pi» read as «…"ntipi».
- ch5 ^2-224 block (line 65): «"gantho ceva ganthasampayutta"ñcāti» read as «"… ganthasampayuttañcā"ti».
- ch5 line 49: «siyā parittārammaṇaṃ siyā mahaggatārammaṇaṃ» (comma missing): a «၊» added between the two.
- ch7 ^2-366 block (line 41): «Pañcapi upādānakkhandhā loko – tattha katamā abhijjhā?» (dash for a full stop, «Ayaṃ
  vuccati loko» missing): kept as written, dash kept.
- ch7 line 107: «sāsavācātipi», «āsavasampayuttācātipi» (fused) read as «sāsavā cātipi», «āsavasampayuttā cātipi».
- ch9 line 9: «abhisaññahitvā» beside «abhisaññūhitvā» (lines 21 …): same Burmese.
- ch9 line 52: «viññāṇakhandho» = viññāṇakkhandho; line 81: «Tathābhūtasa» = Tathābhūtassa; line 112:
  «maggariyāpannaṃ» = maggapariyāpannaṃ.
- ch9 ^2-455 (line 102): the last sentence has no full stop: no «။» either.
- ch10 ^2-478 block (line 51): «yo tasmiṃ samaye phasso hoti…pe… avikkhepo hoti – ime dhammā kusalā» (stray «yo», a dash
  for the full stop): «yo» not rendered, dash kept.
- ch10 line 58: the vipāka opening without «suññataṃ»: rendered without «ဆိတ်သုဉ်းသော».
- ch10 line 74: «Anāsavā āsavavippayuttā.» (two terms, one sentence): one sentence with both terms; «Āsavā ceva
  āsavasampayuttā cātipi, …» without «na vattabbā»: rendered as written (no «ခေါ်ဆို၍ မရ»).
- Stray spaces before «…pe…» («kāmehi …pe…», «vīriyārambho …pe…», «Anupassīti …pe…») dropped.

## New strings («Pāli = Burmese»; generated by make_ch5-7-11.py)

tesaṃ dhammānaṃ aññātāvīnaṃ diṭṭhānaṃ pattānaṃ viditānaṃ sacchikatānaṃ sacchikiriyāya = အပြည့်အဝ သိမြင်ပြီး၊ မြင်ပြီး၊ ရောက်ပြီး၊ တွေ့ရှိပြီး၊ မျက်မှောက်ပြုပြီးသော ထို သဘောတရားတို့ကို မျက်မှောက်ပြုရန် ဖြစ်သော 
upekkhāsambojjhaṅgo = ဥပေက္ခာ ဗောဇ္ဈင်
satta bojjhaṅgā = ဗောဇ္ဈင် ခုနစ်ပါး
cha bojjhaṅgā = ဗောဇ္ဈင် ခြောက်ပါး
satta maggaṅgā = မဂ်၏ အင်္ဂါ ခုနစ်ပါး
aṭṭhannaṃ maggaṅgānaṃ = မဂ်၏ အင်္ဂါ ရှစ်ပါး
ariyo aṭṭhaṅgiko maggo = အင်္ဂါ ရှစ်ပါး ရှိသော အရိယာ မဂ်
-niddeso = ကို ဖွင့်ဆိုချက်
anupassī = အဖန်ဖန် ရှုသူ
anupassanā = အဖန်ဖန် ရှုခြင်း
Kāyānupassanāniddeso = ကိုယ်ကို အဖန်ဖန် ရှုခြင်းကို ဖွင့်ဆိုချက်
Vedanānupassanāniddeso = ခံစားမှုကို အဖန်ဖန် ရှုခြင်းကို ဖွင့်ဆိုချက်
Cittānupassanāniddeso = စိတ်ကို အဖန်ဖန် ရှုခြင်းကို ဖွင့်ဆိုချက်
Dhammānupassanāniddeso = သဘောတရားကို အဖန်ဖန် ရှုခြင်းကို ဖွင့်ဆိုချက်
padhānasaṅkhāro = ကြိုးပမ်းအားထုတ်ခြင်း ပြုပြင်ဖန်တီးမှု
chandasamādhi = ဆန္ဒ သမာဓိ
chandiddhipādo = ဆန္ဒ ဣဒ္ဓိပါဒ်
vīriyasamādhi = ဝီရိယ သမာဓိ
vīriyiddhipādo = ဝီရိယ ဣဒ္ဓိပါဒ်
cittasamādhi = စိတ် သမာဓိ
cittiddhipādo = စိတ် ဣဒ္ဓိပါဒ်
vīmaṃsāsamādhi = စုံစမ်းဆင်ခြင်မှု သမာဓိ
vīmaṃsiddhipādo = စုံစမ်းဆင်ခြင်မှု ဣဒ္ဓိပါဒ်
Indriyavibhaṅgo = စွမ်းရည်များကို ခွဲခြမ်းစိတ်ဖြာခြင်း
Satipaṭṭhānavibhaṅgo = သတိပဋ္ဌာန်များကို ခွဲခြမ်းစိတ်ဖြာခြင်း
Sammappadhānavibhaṅgo = မှန်ကန်သော ကြိုးပမ်းအားထုတ်ခြင်းများကို ခွဲခြမ်းစိတ်ဖြာခြင်း
Iddhipādavibhaṅgo = ဣဒ္ဓိပါဒ်များကို ခွဲခြမ်းစိတ်ဖြာခြင်း
Bojjhaṅgavibhaṅgo = ဗောဇ္ဈင်များကို ခွဲခြမ်းစိတ်ဖြာခြင်း
Maggaṅgavibhaṅgo = မဂ်၏ အင်္ဂါများကို ခွဲခြမ်းစိတ်ဖြာခြင်း
Chandiddhipādo = ဆန္ဒ ဣဒ္ဓိပါဒ်
Vīriyiddhipādo = ဝီရိယ ဣဒ္ဓိပါဒ်
Cittiddhipādo = စိတ် ဣဒ္ဓိပါဒ်
Vīmaṃsiddhipādo = စုံစမ်းဆင်ခြင်မှု ဣဒ္ဓိပါဒ်
evamuparipi (variant note) = နောက်ပိုင်း၌လည်း ဤနည်းတူ
dha. sa. 9 (variant note) = “သဘောတရားများကို စုစည်းရေတွက်ခြင်း” 9
chando = ဆန္ဒ
chandikatā = ဆန္ဒ ပြုခြင်း
kattukamyatā = ပြုလုပ်လိုခြင်း
kusalo dhammacchando = ကုသိုလ် သဘောတရားကို လိုလားသော ဆန္ဒ
upekkhanā = ဥပေက္ခာဖြင့် ရှုခြင်း
ajjhupekkhanā = ဥပေက္ခာဖြင့် လွန်စွာ ရှုခြင်း
majjhattatā cittassa = စိတ်၏ အလယ်အလတ်၌ တည်ခြင်း
iddhi = ဣဒ္ဓိ
samiddhi = ကောင်းစွာ ပြည့်စုံခြင်း
ijjhanā = ပြီးမြောက်ခြင်း
samijjhanā = ကောင်းစွာ ပြီးမြောက်ခြင်း
lābho = ရခြင်း
paṭilābho = ထပ်မံ ရခြင်း
patti = ရောက်ခြင်း
sampatti = ကောင်းစွာ ရောက်ခြင်း
sacchikiriyā = မျက်မှောက်ပြုခြင်း
upasampadā = ပြည့်စုံစွာ ရရှိခြင်း
vedanākkhandhassa saññākkhandhassa saṅkhārakkhandhassa viññāṇakkhandhassa = ခံစားမှု အစုအဝေး၊ မှတ်သိမှု အစုအဝေး၊ ပြုပြင်ဖန်တီးမှု အစုအဝေးနှင့် သိစိတ် အစုအဝေးတို့၏ 
tesaṃ dhammānaṃ (iddhi list) = ထို သဘောတရားတို့၏ 
vivicceva kāmehi vivicca akusalehi dhammehi savitakkaṃ savicāraṃ vivekajaṃ pītisukhaṃ paṭhamaṃ jhānaṃ upasampajja viharati (pi-1 pieces; finite verb) = ကာမတို့မှ ကင်းဆိတ်၍သာ၊ အကုသိုလ် သဘောတရားတို့မှ ကင်းဆိတ်၍၊ စတင်ကြံစည်မှု ရှိသော၊ ဆက်လက်သုံးသပ်မှု ရှိသော၊ ကင်းဆိတ်ခြင်းမှ ဖြစ်ပေါ်သော ပီတိနှင့် သာယာမှု ရှိသော ပထမ ဈာန်ကို ဝင်စား၍ နေ၏
vitakkavicārānaṃ vūpasamā ajjhattaṃ sampasādanaṃ cetaso ekodibhāvaṃ avitakkaṃ avicāraṃ samādhijaṃ pītisukhaṃ dutiyaṃ jhānaṃ upasampajja viharati (pi-1 pieces; finite verb) = စတင်ကြံစည်မှုနှင့် ဆက်လက်သုံးသပ်မှုတို့ ငြိမ်းသွားခြင်းကြောင့်၊ မိမိ၌ ကြည်လင်မှု ရှိသော၊ စိတ်ကို စုစည်း တည်ငြိမ်စေသော၊ စတင်ကြံစည်မှု မရှိသော၊ ဆက်လက်သုံးသပ်မှု မရှိသော၊ သမာဓိမှ ဖြစ်ပေါ်သော ပီတိနှင့် သာယာမှု ရှိသော ဒုတိယ ဈာန်ကို ဝင်စား၍ နေ၏
pītiyā ca virāgā upekkhako ca viharati sato ca sampajāno sukhañca kāyena paṭisaṃvedeti, yaṃ taṃ ariyā ācikkhanti "upekkhako satimā sukhavihārī"ti tatiyaṃ jhānaṃ upasampajja viharati (pi-1 pieces; finite verb) = ပီတိလည်း ပြယ်ပျောက်သွားခြင်းကြောင့်၊ ဥပေက္ခာ ရှိလျက်လည်း နေ၍၊ သတိ ရှိလျက် ကောင်းစွာ ဆင်ခြင်သိမြင်လျက်လည်း၊ သာယာမှုကိုလည်း စိတ်၏ အဖော်တို့ဖြင့် ခံစား၍၊ အရိယာတို့က “ဥပေက္ခာ ရှိသူ၊ သတိ ရှိသူ၊ သာယာစွာ နေသူ” ဟု ပြောကြားကြသော တတိယ ဈာန်ကို ဝင်စား၍ နေ၏
sukhassa ca pahānā dukkhassa ca pahānā pubbeva somanassadomanassānaṃ atthaṅgamā adukkhamasukhaṃ upekkhāsatipārisuddhiṃ catutthaṃ jhānaṃ upasampajja viharati (pi-1 pieces; finite verb) = သာယာမှုကိုလည်း ပယ်ခြင်းကြောင့်၊ နာကျင်မှုကိုလည်း ပယ်ခြင်းကြောင့်၊ ရှေးဦးကပင် ဝမ်းမြောက်မှုနှင့် စိတ်ဆင်းရဲမှုတို့ ချုပ်ငြိမ်းသွားခြင်းကြောင့်၊ မနာကျင် မသာယာသော၊ ဥပေက္ခာကြောင့် သတိ စင်ကြယ်သော စတုတ္ထ ဈာန်ကို ဝင်စား၍ နေ၏
ātāpo = ထက်သန်သော လုံ့လ
loko = လောက
abhijjhā = သူ့ဥစ္စာကို လိုချင်ခြင်း
domanassaṃ = စိတ်ဆင်းရဲမှု
padhānasaṅkhārā = ကြိုးပမ်းအားထုတ်ခြင်း ပြုပြင်ဖန်တီးမှုများ
rūpajīvitindriyaṃ = ရုပ် ဖြစ်သော အသက်၏ စွမ်းရည်
arūpajīvitindriyaṃ = ရုပ် မဟုတ်သော အသက်၏ စွမ်းရည်
chandasamādhipadhānasaṅkhāro = ဆန္ဒ သမာဓိနှင့် ကြိုးပမ်းအားထုတ်ခြင်း ပြုပြင်ဖန်တီးမှု
chandasamādhipadhānasaṅkhārasamannāgato = ဆန္ဒ သမာဓိနှင့် ကြိုးပမ်းအားထုတ်ခြင်း ပြုပြင်ဖန်တီးမှုတို့ဖြင့် အပြည့်အဝ ပြည့်စုံသူ
vīriyasamādhipadhānasaṅkhāro = ဝီရိယ သမာဓိနှင့် ကြိုးပမ်းအားထုတ်ခြင်း ပြုပြင်ဖန်တီးမှု
vīriyasamādhipadhānasaṅkhārasamannāgato = ဝီရိယ သမာဓိနှင့် ကြိုးပမ်းအားထုတ်ခြင်း ပြုပြင်ဖန်တီးမှုတို့ဖြင့် အပြည့်အဝ ပြည့်စုံသူ
cittasamādhipadhānasaṅkhāro = စိတ် သမာဓိနှင့် ကြိုးပမ်းအားထုတ်ခြင်း ပြုပြင်ဖန်တီးမှု
cittasamādhipadhānasaṅkhārasamannāgato = စိတ် သမာဓိနှင့် ကြိုးပမ်းအားထုတ်ခြင်း ပြုပြင်ဖန်တီးမှုတို့ဖြင့် အပြည့်အဝ ပြည့်စုံသူ
vīmaṃsāsamādhipadhānasaṅkhāro = စုံစမ်းဆင်ခြင်မှု သမာဓိနှင့် ကြိုးပမ်းအားထုတ်ခြင်း ပြုပြင်ဖန်တီးမှု
vīmaṃsāsamādhipadhānasaṅkhārasamannāgato = စုံစမ်းဆင်ခြင်မှု သမာဓိနှင့် ကြိုးပမ်းအားထုတ်ခြင်း ပြုပြင်ဖန်တီးမှုတို့ဖြင့် အပြည့်အဝ ပြည့်စုံသူ
ātāpī = ထက်သန်သော လုံ့လ ရှိသူ
sampajāno = ကောင်းစွာ ဆင်ခြင်သိမြင်သူ
viharati = နေ၏
vineyya loke abhijjhādomanassaṃ = လောက၌ သူ့ဥစ္စာကို လိုချင်ခြင်းနှင့် စိတ်ဆင်းရဲမှုကို ပယ်ဖျောက်၍
kāye kāyānupassī = ကိုယ်၌ ကိုယ်ကို အဖန်ဖန် ရှုသူ ဖြစ်လျက်
kesā (body part) = ဆံပင်
lomā (body part) = မွေးညင်း
nakhā (body part) = ခြေသည်းလက်သည်း
dantā (body part) = သွား
taco (body part) = အရေ
maṃsaṃ (body part) = အသား
nhāru (body part) = အကြော
aṭṭhi (body part) = အရိုး
aṭṭhimiñjaṃ (body part) = ရိုးတွင်းခြင်ဆီ
vakkaṃ (body part) = ကျောက်ကပ်
hadayaṃ (body part) = နှလုံး
yakanaṃ (body part) = အသည်း
kilomakaṃ (body part) = အမြှေး
pihakaṃ (body part) = အဖျဉ်း
papphāsaṃ (body part) = အဆုတ်
antaṃ (body part) = အူမ
antaguṇaṃ (body part) = အူသိမ်
udariyaṃ (body part) = အစာသစ်
karīsaṃ (body part) = အစာဟောင်း
pittaṃ (body part) = သည်းခြေ
semhaṃ (body part) = သလိပ်
pubbo (body part) = ပြည်
lohitaṃ (body part) = သွေး
sedo (body part) = ချွေး
medo (body part) = အဆီခဲ
assu (body part) = မျက်ရည်
vasā (body part) = အဆီကြည်
kheḷo (body part) = တံတွေး
siṅghāṇikā (body part) = နှပ်
lasikā (body part) = အစေး
mutta (body part) = ဆီး
sāmisa = ကာမဂုဏ်နှင့် စပ်သော
nirāmisa = ကာမဂုဏ်နှင့် မစပ်သော
pajānāti = ကွဲပြားစွာ သိ၏
sarāgaṃ cittaṃ = ရာဂ ရှိသော စိတ်
vītarāgaṃ cittaṃ = ရာဂ ကင်းသော စိတ်
sadosaṃ cittaṃ = ဒေါသ ရှိသော စိတ်
vītadosaṃ cittaṃ = ဒေါသ ကင်းသော စိတ်
samohaṃ cittaṃ = မောဟ ရှိသော စိတ်
vītamohaṃ cittaṃ = မောဟ ကင်းသော စိတ်
saṃkhittaṃ cittaṃ = တွန့်ဆုတ်နေသော စိတ်
vikkhittaṃ cittaṃ = ပျံ့လွင့်နေသော စိတ်
amahaggataṃ cittaṃ = မကြီးမြတ်သော စိတ်
samāhitaṃ cittaṃ = တည်ကြည်သော စိတ်
asamāhitaṃ cittaṃ = မတည်ကြည်သော စိတ်
vimuttaṃ cittaṃ = လွတ်မြောက်သော စိတ်
avimuttaṃ cittaṃ = မလွတ်မြောက်သော စိတ်
upeto hoti samupeto upāgato samupāgato upapanno sampanno samannāgato = ယှဉ်သူ၊ ကောင်းစွာ ယှဉ်သူ၊ ချဉ်းကပ်သူ၊ ကောင်းစွာ ချဉ်းကပ်သူ၊ ရောက်ရှိသူ၊ ပြည့်စုံသူ၊ အပြည့်အဝ ပြည့်စုံသူ ဖြစ်၏
abhiññāya sambodhāya nibbānāya saṃvattati = ထူးကဲစွာ သိခြင်း၊ ကောင်းစွာ သိမြင်ခြင်း၊ နိဗ္ဗာန်အတွက် ဖြစ်၏
vivekanissitaṃ virāganissitaṃ nirodhanissitaṃ vossaggapariṇāmiṃ = ကင်းဆိတ်ခြင်းကို မှီသော၊ ပြယ်ပျောက်ခြင်းကို မှီသော၊ ချုပ်ငြိမ်းခြင်းကို မှီသော၊ စွန့်လွှတ်ခြင်းသို့ ညွတ်သော
avasesā dhammā = ကြွင်းသော သဘောတရားများ
Bāvīsatindriyāni = စွမ်းရည် နှစ်ဆယ့်နှစ်ပါး
Cattāro satipaṭṭhānā = သတိပဋ္ဌာန် လေးပါး
Cattāro sammappadhānā = မှန်ကန်သော ကြိုးပမ်းအားထုတ်ခြင်း လေးပါး
Cattāro iddhipādā = ဣဒ္ဓိပါဒ် လေးပါး
Iti imesaṃ = ဤသို့ ဤ
Idha bhikkhu = ဤသာသနာ၌ ရဟန်းသည်
idha bhikkhu = ဤသာသနာ၌ ရဟန်းသည်
So = ထိုရဟန်းသည်
Evaṃ bhikkhu = ဤသို့ ရဟန်းသည်
Kathañca bhikkhu = 
tañca pajānāti = ကိုလည်း ကွဲပြားစွာ သိ၏
seyyathidaṃ = ဆိုလိုသည်မှာ
Ariyo aṭṭhaṅgiko maggo = အင်္ဂါ ရှစ်ပါး ရှိသော အရိယာ မဂ်
kāyaṃ uddhaṃ pādatalā adho kesamatthakā tacapariyantaṃ pūraṃ nānappakārassa asucino paccavekkhati = ကိုယ်ကို ခြေဖဝါးမှ အထက်၊ ဆံပင်ဖျားမှ အောက်၊ အရေဖြင့် ဝန်းရံထားသော၊ အမျိုးမျိုးသော မစင်ကြယ်သည့်အရာတို့ဖြင့် ပြည့်နေသည်ဟု ဆင်ခြင်၏
taṃ nimittaṃ āsevati bhāveti bahulīkaroti svāvatthitaṃ vavatthapeti = ထိုအမှတ်အသားကို အလေ့အကျင့် ပြု၏၊ ပွားများ၏၊ အကြိမ်ကြိမ် ပြု၏၊ ကောင်းစွာ ပိုင်းခြား သတ်မှတ်၏
taṃ nimittaṃ āsevitvā bhāvetvā bahulīkaritvā svāvatthitaṃ vavatthapetvā = ထိုအမှတ်အသားကို အလေ့အကျင့် ပြု၍၊ ပွားများ၍၊ အကြိမ်ကြိမ် ပြု၍၊ ကောင်းစွာ ပိုင်းခြား သတ်မှတ်၍
cittaṃ upasaṃharati = စိတ်ကို ညွှတ်ဆောင်၏
Iriyati vattati pāleti yapeti yāpeti carati viharati = လှုပ်ရှား၏၊ လည်ပတ်၏၊ စောင့်ရှောက်၏၊ ဆက်လက် ဖြစ်နေ၏၊ ဆက်လက် ရှင်သန်စေ၏၊ ကျင်လည်၏၊ နေ၏
Sveva kāyo loko = ထိုကိုယ်ပင် လောက ဖြစ်၏
Sāyeva vedanā loko = ထိုခံစားမှုပင် လောက ဖြစ်၏
Taṃyeva cittaṃ loko = ထိုစိတ်ပင် လောက ဖြစ်၏
Teva dhammā loko = ထိုသဘောတရားများပင် လောက ဖြစ်၏
Pañcapi upādānakkhandhā loko = စွဲလမ်းမှု၏ အာရုံ ဖြစ်သော အစုအဝေး ငါးပါးလည်း လောက ဖြစ်၏
Iti ayañca abhijjhā idañca domanassaṃ imamhi loke vinītā honti paṭivinītā santā samitā vūpasantā atthaṅgatā abbhatthaṅgatā appitā byappitā sositā visositā byantīkatā = ဤသို့ ဤ သူ့ဥစ္စာကို လိုချင်ခြင်းလည်း၊ ဤစိတ်ဆင်းရဲမှုလည်း ဤလောက၌ ပယ်ဖျောက်ပြီး၊ လုံးဝ ပယ်ဖျောက်ပြီး၊ ငြိမ်းပြီး၊ ငြိမ်သက်ပြီး၊ ကောင်းစွာ ငြိမ်သက်ပြီး၊ ကွယ်ပျောက်ပြီး၊ လုံးဝ ကွယ်ပျောက်ပြီး၊ ချုပ်ငြိမ်းစေပြီး၊ အပြီးတိုင် ချုပ်ငြိမ်းစေပြီး၊ ခြောက်ခန်းစေပြီး၊ လုံးဝ ခြောက်ခန်းစေပြီး၊ အဆုံးသတ်ပြီး ဖြစ်ကြ၏
Imaṃ chandaṃ janeti sañjaneti uṭṭhapeti samuṭṭhapeti = ဤဆန္ဒကို ဖြစ်စေ၏၊ ကောင်းစွာ ဖြစ်စေ၏၊ ထပေါ်စေ၏၊ ကောင်းစွာ ထပေါ်စေ၏
nibbatteti abhinibbatteti = ပေါ်ထွက်စေ၏၊ ထင်ရှားစွာ ပေါ်ထွက်စေ၏
Imaṃ vīriyaṃ ārabhati samārabhati āsevati bhāveti bahulīkaroti = ဤဝီရိယကို စတင်၏၊ ကောင်းစွာ စတင်၏၊ အလေ့အကျင့် ပြု၏၊ ပွားများ၏၊ အကြိမ်ကြိမ် ပြု၏
Imaṃ cittaṃ paggaṇhāti sampaggaṇhāti upatthambheti paccupatthambheti = ဤစိတ်ကို မြှင့်တင်၏၊ ကောင်းစွာ မြှင့်တင်၏၊ ထောက်ပံ့၏၊ အထပ်ထပ် ထောက်ပံ့၏
Yā ṭhiti so asammoso, yo asammoso so bhiyyobhāvo, yo bhiyyobhāvo taṃ vepullaṃ, yaṃ vepullaṃ sā bhāvanā, yā bhāvanā sā pāripūrī = အကြင် တည်တံ့ခြင်းသည် ထို မပျောက်ပျက်ခြင်း ဖြစ်၏၊ အကြင် မပျောက်ပျက်ခြင်းသည် ထို ပိုမို တိုးပွားခြင်း ဖြစ်၏၊ အကြင် ပိုမို တိုးပွားခြင်းသည် ထို ပြန့်ပြောခြင်း ဖြစ်၏၊ အကြင် ပြန့်ပြောခြင်းသည် ထို ပွားများခြင်း ဖြစ်၏၊ အကြင် ပွားများခြင်းသည် ထို ပြည့်စုံခြင်း ဖြစ်၏
Te dhamme āsevati bhāveti bahulīkaroti = ထိုသဘောတရားတို့ကို အလေ့အကျင့် ပြု၏၊ ပွားများ၏၊ အကြိမ်ကြိမ် ပြု၏
Tathābhūtassa = ထိုသို့ ဖြစ်သူ၏
Tathābhūtasa = ထိုသို့ ဖြစ်သူ၏
ime ca padhānasaṅkhārā = ဤကြိုးပမ်းအားထုတ်ခြင်း ပြုပြင်ဖန်တီးမှုများလည်း
taṃsamuṭṭhānaṃ kāyakammaṃ vacīkammaṃ manokammaṃ = ထိုတို့မှ ဖြစ်ပေါ်လာသော ကိုယ်ဖြင့် ပြုသော ကံ၊ နှုတ်ဖြင့် ပြုသော ကံ၊ မနောဖြင့် ပြုသော ကံ
Tadekajjhaṃ abhisaññahitvā abhisaṅkhipitvā = ထိုအားလုံးကို တစ်စုတည်း ပေါင်းစု၍ အကျဉ်းချုံ့၍
tadekajjhaṃ abhisaññūhitvā abhisaṅkhipitvā = ထိုအားလုံးကို တစ်စုတည်း ပေါင်းစု၍ အကျဉ်းချုံ့၍
saṅkhyaṃ = ဟူ၍သာ အမည်
gacchati = ရ၏
ce bhikkhu = 
adhipatiṃ karitvā labhati samādhiṃ = ကို အကြီးအမှူး ပြု၍ သမာဓိကို ရ၏
labhati cittassekaggataṃ = စိတ်၏ စူးစိုက်မှုကို ရ၏
Iti = ဤသို့
satimā hoti paramena satinepakkena samannāgato = သတိ ရှိသူ ဖြစ်၏၊ အမြတ်ဆုံးသော သတိနှင့် ရင့်ကျက်သော ဉာဏ်ဖြင့် အပြည့်အဝ ပြည့်စုံသူ ဖြစ်၏
cirakatampi cirabhāsitampi saritā hoti anussaritā = ကြာမြင့်စွာ ပြုခဲ့သည်ကိုလည်း၊ ကြာမြင့်စွာ ပြောခဲ့သည်ကိုလည်း အောက်မေ့သူ၊ အဖန်ဖန် အောက်မေ့သူ ဖြစ်၏
So tathā sato viharanto taṃ dhammaṃ paññāya pavicinati pavicarati parivīmaṃsamāpajjati = ထိုရဟန်းသည် ထိုသို့ သတိ ရှိလျက် နေစဉ် ထိုသဘောတရားကို ပညာဖြင့် သေချာစွာ စိစစ်၏၊ သေချာစွာ သုံးသပ်၏၊ ပတ်လည် စူးစမ်းဆန်းစစ်ခြင်းသို့ ရောက်၏
Tassa taṃ dhammaṃ paññāya pavicinato pavicarato parivīmaṃsamāpajjato āraddhaṃ hoti vīriyaṃ asallīnaṃ = ထိုသဘောတရားကို ပညာဖြင့် သေချာစွာ စိစစ်နေ၊ သေချာစွာ သုံးသပ်နေ၊ ပတ်လည် စူးစမ်းဆန်းစစ်ခြင်းသို့ ရောက်နေသော ထိုရဟန်း၌ မတွန့်ဆုတ်သော ဝီရိယကို စတင်ပြီး ဖြစ်၏
Āraddhavīriyassa uppajjati pīti nirāmisā = ဝီရိယကို စတင်ပြီးသူ၌ ကာမဂုဏ်နှင့် မစပ်သော ပီတိ ဖြစ်ပေါ်၏
Pītimanassa kāyopi passambhati, cittampi passambhati = ပီတိ ရှိသော စိတ် ရှိသူ၏ ကိုယ်လည်း ငြိမ်းအေး၏၊ စိတ်လည်း ငြိမ်းအေး၏
Passaddhakāyassa sukhino cittaṃ samādhiyati = ကိုယ် ငြိမ်းအေးပြီး သာယာမှု ရှိသူ၏ စိတ်သည် တည်ကြည်၏
So tathā samāhitaṃ cittaṃ sādhukaṃ ajjhupekkhitā hoti = ထိုရဟန်းသည် ထိုသို့ တည်ကြည်သော စိတ်ကို ကောင်းစွာ ဥပေက္ခာဖြင့် လွန်စွာ ရှုသူ ဖြစ်၏
kāyikaṃ vīriyaṃ = ကိုယ်ပိုင်းဆိုင်ရာ ဝီရိယ
cetasikaṃ vīriyaṃ = စိတ်ပိုင်းဆိုင်ရာ ဝီရိယ
savitakkasavicārā pīti = စတင်ကြံစည်မှုနှင့် ဆက်လက်သုံးသပ်မှု ရှိသော ပီတိ
avitakkaavicārā pīti = စတင်ကြံစည်မှုလည်း မရှိ၊ ဆက်လက်သုံးသပ်မှုလည်း မရှိသော ပီတိ
kāyapassaddhi = စိတ်၏ အဖော်တို့ ငြိမ်းအေးခြင်း
cittapassaddhi = စိတ် ငြိမ်းအေးခြင်း
savitakko savicāro samādhi = စတင်ကြံစည်မှု ရှိသော၊ ဆက်လက်သုံးသပ်မှု ရှိသော သမာဓိ
avitakko avicāro samādhi = စတင်ကြံစည်မှု မရှိသော၊ ဆက်လက်သုံးသပ်မှု မရှိသော သမာဓိ
bhāveti = ကို ပွားများ၏
Idha ariyasāvako micchāājīvaṃ pahāya sammāājīvena jīvikaṃ kappeti = ဤသာသနာ၌ အရိယာ တပည့်သည် မှားယွင်းသော အသက်မွေးမှုကို ပယ်၍ မှန်ကန်သော အသက်မွေးမှုဖြင့် အသက်မွေး၏
Dukkhe ñāṇaṃ, dukkhasamudaye ñāṇaṃ, dukkhanirodhe ñāṇaṃ, dukkhanirodhagāminiyā paṭipadāya ñāṇaṃ = ဒုက္ခကို သိသော ဉာဏ်၊ ဒုက္ခ ဖြစ်ပေါ်ခြင်းကို သိသော ဉာဏ်၊ ဒုက္ခ ချုပ်ငြိမ်းခြင်းကို သိသော ဉာဏ်၊ ဒုက္ခ ချုပ်ငြိမ်းရာသို့ ရောက်စေသော ကျင့်စဉ်ကို သိသော ဉာဏ်
Nekkhammasaṅkappo, abyāpādasaṅkappo, avihiṃsāsaṅkappo = ကာမမှ ထွက်မြောက်ခြင်းဆိုင်ရာ ကြံစည်မှု၊ ဖျက်ဆီးလိုစိတ် မရှိခြင်းဆိုင်ရာ ကြံစည်မှု၊ ညှဉ်းဆဲလိုစိတ် မရှိခြင်းဆိုင်ရာ ကြံစည်မှု
Musāvādā veramaṇī, pisuṇāya vācāya veramaṇī, pharusāya vācāya veramaṇī, samphappalāpā veramaṇī = မုသာ ပြောခြင်းမှ ကင်းဝေးခြင်း၊ ကုန်းချောသော စကားမှ ကင်းဝေးခြင်း၊ ကြမ်းတမ်းသော စကားမှ ကင်းဝေးခြင်း၊ အကျိုးမဲ့ ပြောခြင်းမှ ကင်းဝေးခြင်း
Pāṇātipātā veramaṇī, adinnādānā veramaṇī, kāmesumicchācārā veramaṇī = သူ့အသက်ကို သတ်ခြင်းမှ ကင်းဝေးခြင်း၊ မပေးသည်ကို ယူခြင်းမှ ကင်းဝေးခြင်း၊ ကာမတို့၌ မှားယွင်းစွာ ကျင့်ခြင်းမှ ကင်းဝေးခြင်း
Jīvitindriyaṃ duvidhena = အသက်၏ စွမ်းရည်ကို နှစ်မျိုးဖြင့် ကြည့်လျှင်
atthi rūpajīvitindriyaṃ = ရုပ် ဖြစ်သော အသက်၏ စွမ်းရည် ရှိသည်
atthi arūpajīvitindriyaṃ = ရုပ် မဟုတ်သော အသက်၏ စွမ်းရည် ရှိသည်
phassasampayuttaṃ = တွေ့ထိမှုနှင့် ယှဉ်တွဲသော သဘောတရား ဖြစ်သည်
dvindriyā = စွမ်းရည် နှစ်ပါး
tīṇindriyā = စွမ်းရည် သုံးပါး
cattārindriyā = စွမ်းရည် လေးပါး
pañcindriyā = စွမ်းရည် ငါးပါး
cha indriyā = စွမ်းရည် ခြောက်ပါး
sattindriyā = စွမ်းရည် ခုနစ်ပါး
aṭṭhindriyā = စွမ်းရည် ရှစ်ပါး
navindriyā = စွမ်းရည် ကိုးပါး
dasindriyā = စွမ်းရည် ဆယ်ပါး
ekādasindriyā = စွမ်းရည် ဆယ့်တစ်ပါး
dvādasindriyā = စွမ်းရည် ဆယ့်နှစ်ပါး
terasindriyā = စွမ်းရည် ဆယ့်သုံးပါး
cuddasindriyā = စွမ်းရည် ဆယ့်လေးပါး
pannarasindriyā = စွမ်းရည် ဆယ့်ငါးပါး
soḷasindriyā = စွမ်းရည် ဆယ့်ခြောက်ပါး
sattarasindriyā = စွမ်းရည် ဆယ့်ခုနစ်ပါး
aṭṭhārasindriyā = စွမ်းရည် ဆယ့်ရှစ်ပါး
ekavīsatindriyā = စွမ်းရည် နှစ်ဆယ့်တစ်ပါး
tayo iddhipādā = ဣဒ္ဓိပါဒ် သုံးပါး
na appamāṇārammaṇā = အတိုင်းအဆ မရှိသည်ကို အာရုံပြုသည် မဟုတ်သော
na maggārammaṇā = မဂ်ကို အာရုံပြုသည် မဟုတ်သော
na maggādhipatino = မဂ်ကို အကြီးအမှူးပြုသည် မဟုတ်သော
