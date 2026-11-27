# pi-4 Burmese zero-shot, chapter 5-catukkapuggalapannatti (the fours): notes

Status: DONE 2026-11-19 (zero-shot, brief burmese-zeroshot-brief.md). Not committed.

## Files
- Output: `AI_translation/burmese/pi-4-burmese-plain-zeroshot_split_chapters/5-catukkapuggalapannatti.md`
  (60 segments, 147 lines).
- Generator `make_ch5.py` (imports my4_formulas and make_sample read only; extends their tables IN MEMORY only;
  writes only the chapter file; never touches my4_formulas.py, make_sample.py, my4-zeroshot-terms.md).
  Run: `python3 -I -X utf8 make_ch5.py` (`--misses` lists unmatched units and writes nothing). The run stops on any
  unmatched unit and on any unused SENT5 key (coverage).
- Check `check_ch5.py` (adapted from check_sample.py; regeneration, typography, numbers, polarity, names, reuse).

## Checks (final run)
- check_chapter_ids: OK (60 segments); check_text_pe: OK (147 lines, dashes match); check_marks: OK. chk-pe copy
  of this chapter deleted.
- check_ch5.py: A 1/1 regenerated identical; B1 147 lines; B2 87 numbers (cardinals and ordinals); B3 377
  negations / pairs; B5 186 questions / closings / similes; 0 mismatches. Reuse 108 / 108 identical (C2 84/84 terms
  and clauses of pi-1 / pi-2 / pi-3 final, witnessed; C3 24/24 sentences and mātikā predicates of the approved
  sample). Mutation-tested (a dropped «မ» and a changed number are caught).

## Method
- Frames (RULES5): «Kathañca puggalo X hoti?» = «ပုဂ္ဂိုလ်သည် အဘယ်သို့ X ဖြစ်သနည်း။» (pi-2 ^2-523 pattern);
  «Evaṃ puggalo X hoti.» = «ဤသို့ ပုဂ္ဂိုလ်သည် X ဖြစ်၏။». X = the mātikā predicate of the sample (PRED_M, e.g.
  attahitāya …, attantapo …, ananuvicca …, bhūtaṃ tacchaṃ kālena, lābhī … cetosamathassa) or the person name
  (NAME) + «ဖြစ်၏»; a predicate ending «… မဟုတ်» gives «… မဟုတ်သနည်း». So question and closing always carry the
  same string as the mātikā (checked, B5).
- Simile groups (GROUP5): each member has one Burmese P; object «Pသော NOUN» (list after «Cattāro X –»), person
  name «Pသူ» (names line «Katame cattāro? …», question, closing), simile «ဥပမာအားဖြင့် ထိုNOUNသည် Pသကဲ့သို့
  ဤပုဂ္ဂိုလ်သည် ထိုNOUNနှင့် တူ၏။». Group lines: «Tattha katame cattāro G puggalā?» = «ထိုတို့အနက် G ပုဂ္ဂိုလ်
  လေးယောက် ဟူသည် အဘယ်တို့နည်း။»; «Evamevaṃ cattārome G puggalā santo saṃvijjamānā lokasmiṃ.» = «ထို့အတူပင် G
  ဤပုဂ္ဂိုလ် လေးယောက်တို့သည် လောက၌ ရှိကြ၏၊ ထင်ရှား ရှိကြ၏။»; «Katame cattāro?» = «အဘယ် လေးယောက်တို့နည်း။»
  (G = the sample GROUP adjective). Object counts «X လေးမျိုး».
- The ten courses (^4-132 … ^4-143) are built from one table (agent / act / abstention), so the five / ten
  clauses and the «attanā ca … parañca … samādapeti» forms are word for word parallel.
- Long passages that pi-1 / pi-2 already have are READ from the FINAL rails text and witnessed: the sense
  restraint (pi-1 ^1-1354), clear comprehension, solitude, the hindrances and the four jhānas (pi-2 ^2-508), the
  former lives and the divine eye (pi-2 ^2-829, ^2-830, honorific «တော်မူ» removed: here the subject is the monk),
  the arahant sentence (pi-2 ^2-831), the four truths (sample), stream-entry / once-return / non-return (sample).
  pi-2's «ထိုရဟန်းသည်» for «So» becomes the sample's «ထိုသူသည်»; the clause bodies are verbatim.
- Brackets: BR5 table (exact bracket -> Burmese), wrapping the sample's var_my in memory. New patterns: no sigla
  «[စာလုံးပေါင်းကွဲ: pisuṇāvāco]»; two readings «[ပါဌ်ကွဲ (Syā.): santāgāraṃ၊ (Sī.): yaññāgāraṃ]» (pi-2 ^2-832);
  refs «“ဒီဃနိကာယ်” 3.115», «“မဇ္ဈိမနိကာယ်” 2.7» (pi-2 ^2-760 / ^2-924); «passa …» = «… ကို ကြည့်ပါ»; the
  editorial note «[( ) natthi sīhaḷapotthake …]» translated (no «။» inside brackets).
- Negation counting of the check: privative words with a Burmese negation in PRIV; compounds naehibhaddantiko,
  natiṭṭhabhaddantiko, nābhihaṭaṃ, nānubyañjanaggāhī, nayidaṃ, nāparaṃ, sahitāsahitassa; adukkhamasukhaṃ = 2.
  Not negations in Burmese (NOT_NEG): မနော, ကာမ, မိန်းမ, သို့မဟုတ်, ကျွန်မ, မြင်းမ, နွားမ, မိမိ, ထောမနာ, ဆုံးမ.
  Lexical (no Burmese negation): avaṇṇa «ကဲ့ရဲ့», akusala, aneka «အမျိုးမျိုး / များစွာ», nelā «အပြစ် ကင်းသော»,
  nicchāto «ဆာလောင်မှု ကင်း», vigata- «ကင်း», appa- «နည်း», du- «ဆိုး» (dussīla «သီလ ပျက်», pi-1 ^1-1333).

## New recurring terms and frames (Pāli = Burmese)
- Kathañca puggalo X hoti? = ပုဂ္ဂိုလ်သည် အဘယ်သို့ X ဖြစ်သနည်း။
- Evaṃ puggalo X hoti. = ဤသို့ ပုဂ္ဂိုလ်သည် X ဖြစ်၏။
- Seyyathāpi so X …, tathūpamo ayaṃ puggalo. = ဥပမာအားဖြင့် ထိုXသည် …သကဲ့သို့ ဤပုဂ္ဂိုလ်သည် ထိုXနှင့် တူ၏။
- santo saṃvijjamānā lokasmiṃ = လောက၌ ရှိကြ၏၊ ထင်ရှား ရှိကြ၏
- Evamevaṃ = ထို့အတူပင် (pi-2 evameva); Tattha katame = ထိုတို့အနက် … ဟူသည် အဘယ်တို့နည်း (pi-2)
- Ayaṃ vuccati puggalo X. (no quotes) = ဤပုဂ္ဂိုလ်ကို Xဟု ခေါ်သည်။
- Idhekaccassa puggalassa = ဤလောက၌ အချို့သော ပုဂ္ဂိုလ်၏; Idha panekacco = ထို့ပြင် ဤလောက၌ အချို့သော
- valāhakā = မိုးတိမ်; gajjitā no vassitā = မိုး ချုန်း၍ မိုး မရွာသူ; vassitā no gajjitā = မိုး ရွာ၍ မိုး မချုန်းသူ;
  gajjitā ca vassitā ca = မိုးလည်း ချုန်း၍ မိုးလည်း ရွာသူ; neva gajjitā no vassitā = မိုးလည်း မချုန်း၊ မိုးလည်း မရွာသူ
- mūsikā = ကြွက်; gādhaṃ kattā no vasitā = တွင်း တူး၍ တွင်း၌ မနေသူ; vasitā no gādhaṃ kattā = တွင်း၌ နေ၍ တွင်း
  မတူးသူ; gādhaṃ kattā ca vasitā ca = တွင်းလည်း တူး၍ တွင်း၌လည်း နေသူ; neva … = တွင်းလည်း မတူး၊ တွင်း၌လည်း မနေသူ
- ambāni = သရက်သီး; āmo pakkavaṇṇī = စိမ်း၍ မှည့်သော အဆင်း ရှိသူ; pakko āmavaṇṇī = မှည့်၍ စိမ်းသော အဆင်း ရှိသူ;
  āmo āmavaṇṇī = စိမ်း၍ စိမ်းသော အဆင်း ရှိသူ; pakko pakkavaṇṇī = မှည့်၍ မှည့်သော အဆင်း ရှိသူ
- kumbhā = အိုး; tuccho pihito = ဗလာ ဖြစ်၍ အဖုံး ပိတ်ထားသူ; pūro vivaṭo = ပြည့်၍ အဖုံး ဖွင့်ထားသူ;
  tuccho vivaṭo = ဗလာ ဖြစ်၍ အဖုံး ဖွင့်ထားသူ; pūro pihito = ပြည့်၍ အဖုံး ပိတ်ထားသူ
- udakarahadā = ရေကန်; uttāno gambhīrobhāso = တိမ်၍ နက်ဟန် ထင်ရသူ; gambhīro uttānobhāso = နက်၍ တိမ်ဟန် ထင်ရသူ;
  uttāno uttānobhāso = တိမ်၍ တိမ်ဟန် ထင်ရသူ; gambhīro gambhīrobhāso = နက်၍ နက်ဟန် ထင်ရသူ
- balībaddā = နွားလား; sakagavacaṇḍo no paragavacaṇḍo = မိမိ အုပ်ရှိ နွားတို့ကို ကြမ်းကြုတ်၍ သူတစ်ပါး အုပ်ရှိ
  နွားတို့ကို မကြမ်းကြုတ်သူ (and the other three by the same parts)
- āsīvisā = မြွေဆိုး; āgataviso no ghoraviso = အဆိပ် လျင်မြန်စွာ တက်၍ အဆိပ် မပြင်းသူ (and the other three)
- rukkhā = သစ်ပင်; pheggu sāraparivāro = အကာ ဖြစ်၍ အနှစ် အခြံအရံ ရှိသူ (and the other three)
- dhammakathiko = တရား ဟောပြောသူ; sahita / asahita = အနက် ဆက်စပ်သည် / အနက် မဆက်စပ်သည်; parisā = ပရိသတ် (pi-2)
- bhāsitā / kattā = ပြောဆိုသူ / ပြုလုပ်သူ; sakaparisaṃ / paraparisaṃ ubbejitā = မိမိ / သူတစ်ပါး ပရိသတ်ကို
  ထိတ်လန့်စေသူ; abhiṇhaṃ kujjhati = ခဏခဏ အမျက်ထွက်၏; ciraṃ dīgharattaṃ anuseti = ကြာမြင့်စွာ ရှည်လျားသော
  ကာလပတ်လုံး ကိန်းအောင်း၍ နေ၏
- pāṇātipātī = သူ့အသက်ကို သတ်သူ; adinnādāyī = မပေးသည်ကို ယူသူ; kāmesumicchācārī = ကာမတို့၌ မှားယွင်းစွာ ကျင့်သူ;
  musāvādī = မုသား ပြောသူ; surāmerayamajjapamādaṭṭhāyī = သေရည် အရက် မူးယစ်ဖွယ်ဟူသော မေ့လျော့ခြင်း၏ အကြောင်းကို
  မှီဝဲသူ; pisuṇavāco / pharusavāco = ကုန်းတိုက်သော / ကြမ်းတမ်းသော စကားကို ပြောသူ; samphappalāpī = အကျိုးမဲ့
  ပြိန်ဖျင်းသော စကားကို ပြောသူ; abhijjhālu / anabhijjhālu = သူ့ဥစ္စာကို လိုချင်သူ / မလိုချင်သူ; byāpannacitto =
  ဖျက်ဆီးလိုစိတ် ရှိသော စိတ် ရှိသူ (abyāpannacitto pi-2 ^2-543); micchādiṭṭhi / sammādiṭṭhi (person) = မှားယွင်းသော
  / မှန်ကန်သော အယူ ရှိသူ (act nouns: pi-2 ^2-487 / ^2-703)
- paṭivirato = ရှောင်ကြဉ်သူ; veramaṇiyā = (… မှ) ကင်းဝေးခြင်း၌ (pi-2 veramaṇī); samādapeti = ဆောက်တည်စေ၏;
  attanā ca = မိမိကိုယ်တိုင်လည်း; parañca = သူတစ်ပါးကိုလည်း
- kāya- / vacī- / manokamma = ကိုယ်ဖြင့် / နှုတ်ဖြင့် / မနောဖြင့် ပြုသော ကံ (pattern of pi-2 kāyaduccarita);
  sāvajja / anavajja = အပြစ် ရှိသော / မရှိသော
- dhammābhisamayo = တရားကို ထိုးဖောက် သိမြင်ခြင်း (kept apart from vipassanā «ထိုးထွင်းသိမြင်ခြင်း»)
- pañhaṃ puṭṭho samāno = ပြဿနာကို မေးမြန်းခံရသောအခါ; yuttaṃ / sīghaṃ vadati = သင့်လျော်စွာ / လျင်မြန်စွာ ဖြေဆို၏
- pāsādika = ကြည်ညိုဖွယ်; pamāṇaṃ gahetvā pasādaṃ janeti = အတိုင်းအတာ ထား၍ ကြည်ညိုမှုကို ဖြစ်စေ၏
- ājīvo = အသက်မွေးမှု; nerayikā = ငရဲသား (pi-2 ^2-1009); paccājāto = ပြန်လည် မွေးဖွားသူ
- nīce / ucce kule = နိမ့်ကျသော / မြင့်မြတ်သော အမျိုး; khattiya- / brāhmaṇa- / gahapatimahāsāla = ကြွယ်ဝသော
  မင်းမျိုး / ပုဏ္ဏားမျိုး / သူကြွယ်မျိုး (pi-2 ^2-1021)
- sampadā / sampanna = ပြည့်စုံခြင်း / ပြည့်စုံသူ (pi-1 sīlasampadā); vimuttiñāṇadassana = လွတ်မြောက်မှုကို
  သိမြင်သော ဉာဏ်
- kesamassuṃ ohāretvā = ဆံပင်နှင့် မုတ်ဆိတ်ကို ရိတ်၍; kāsāyāni vatthāni acchādetvā = ဖန်ရည်စွန်းသော သင်္ကန်းတို့ကို
  ဝတ်ရုံ၍; agārasmā anagāriyaṃ pabbajati = အိမ်မှ ထွက်၍ အိမ်ရာ မရှိသော ရဟန်းအဖြစ်သို့ ကူး၏
- santuṭṭho = ရောင့်ရဲသူ; sīlakkhandha = သီလ အစုအဝေး; indriyasaṃvara = အာရုံခံ အင်္ဂါ စောင့်စည်းမှု;
  satisampajañña = သတိနှင့် ကောင်းစွာ ဆင်ခြင်သိမြင်ခြင်း
- samāhite citte … āneñjappatte = ဤသို့ စိတ်သည် တည်ကြည်၍ … မတုန်လှုပ်ခြင်းသို့ ရောက်သောအခါ; … ñāṇāya cittaṃ
  abhininnāmeti = … ဉာဏ်အတွက် စိတ်ကို ညွတ်စေ၏ (knowledge names pi-1 ^1-1380)
- ime āsavā / āsavasamudayo / āsavanirodho / āsavanirodhagāminī paṭipadā = ဤသည်တို့ကား စိတ်အစွန်းအထင်းတို့ /
  စိတ်အစွန်းအထင်း ဖြစ်ပေါ်ခြင်း / … ချုပ်ငြိမ်းခြင်း / … ချုပ်ငြိမ်းရာသို့ ရောက်စေသော ကျင့်စဉ် (dukkha pattern)
- lokuttaramaggassa vā phalassa vā = လောကကို ကျော်လွန်သော မဂ်ကိုဖြစ်စေ၊ ဖိုလ်ကိုဖြစ်စေ (pi-1 lokuttara)
- appahīno = မပယ်ရသေး (sample appahīnāni)
- dhammānudhammappaṭipanno = တရားနှင့် လျော်သော တရားကို ကျင့်သူ

## Source slips (translated as written, or as the evident reading)
- ^4-142 «samādiṭṭhi hoti» for sammādiṭṭhi: rendered «မှန်ကန်သော အယူ ရှိသူ ဖြစ်၏».
- ^4-155 «ayaṃ vuccati, puggalo "…"»: stray comma; standard closing.
- ^4-166 «Idhekacco puggalo vaṇṇopi saṃvijjati avaṇṇopi saṃvijjati» (nominative): read «… ပုဂ္ဂိုလ်၏ ရှေ့၌
  ချီးမွမ်းဖွယ်လည်း ရှိ၏၊ ကဲ့ရဲ့ဖွယ်လည်း ရှိ၏» (before this person there is …).
- ^4-176 «puratthimena narassa»: read as nagarassa «မြို့၏ အရှေ့ဘက်၌».
- ^4-177 «pabbajeyya"nti! So aparena …»: the «!» is a sentence end, rendered «… ကောင်းလေစွ”ဟု ဆင်ခြင်၏။».
- ^4-171, ^4-172, ^4-188 «Ayaṃ vuccati puggalo X.» after a full stop, without quotes: closing without quotes;
  ^4-190 «… "samaṇesu samaṇasukhumālo"ti.»: standard closing.
- Slight differences from the mātikā (same Burmese): ^4-173 «hoti no parahitāya» (mātikā «hoti, no»); ^4-166 (4)
  «nopi» (mātikā «no ca»); ^4-166 (3) «,» (mātikā «;»); ^4-177 / ^4-185 «neva attantapo ca hoti» (mātikā without
  «ca»); ^4-167 closing «"uṭṭhānaphalūpajīvī, no puññaphalūpajīvī"» (comma; ALIAS); ^4-188 «opapātiko hoti tattha»
  without the comma of ch2.

## Unsure Pāli / to review
- bhagavā «ဘုန်းတော်ရှင်» and buddho «သစ္စာတို့ကို သိတော်မူသူ» in ^4-177, kept apart from tathāgato «မြတ်စွာဘုရား»
  (pi-1 NAMO renders bhagavā «မြတ်စွာဘုရား»); sugato «ကောင်းသော လားရာသို့ ကြွတော်မူသူ».
- The ascetic and sacrifice lists (^4-174, ^4-176): daddula «သားရေ အပိုင်းအစ», haṭa «ရေညှိ», saṅkittīsu «ငတ်မွတ်ချိန်၌
  စုဆောင်းထားသော ဆွမ်း», muttācāro «ကျင့်ဝတ်ကို စွန့်လွှတ်သူ», sāyatatiyaka «ညနေ အပါအဝင် နေ့စဉ် သုံးကြိမ်»,
  sandhāgāra «အဆောင်», kharājina «ကြမ်းသော သားရေ», haritupalittā «စိမ်းစိုသော နွားချေးဖြင့် လိမ်းကျံထားသော»,
  usabha / vacchatara / vacchatarī «နွားထီး / နွားထီးပေါက် / နွားမပေါက်», dabbha «မြက်», kusacīra «ကုသမြက်ဖြင့်
  ရက်သော အဝတ်».
- ^4-168 okoṭimako «ပုကွသူ», kāṇo «မျက်စိ ကွယ်သူ» (kept apart from andho «မျက်စိ ကန်းသူ»), kuṇī «လက် ကောက်သူ»,
  pakkhahato «လေဖြတ်သူ», caṇḍāla / nesāda / vena / rathakāra / pukkusa families.
- ^4-178 nelā «အပြစ် ကင်းသော», porī «ယဉ်ကျေးသော», theto «တည်ကြည်သူ», ārācārī «ဝေးကွာစွာ ကျင့်သူ», nidhānavatī
  «မှတ်သားထိုက်သော»; ^4-179 visūkadassana «ကုသိုလ်ကို ဆန့်ကျင်သော ပွဲသဘင်ကို ကြည့်ခြင်း», vikālabhojana «အချိန်လွန်
  စားခြင်း» (no negation word, as the Pāli).
- Group P strings (similes) are literal; persons get the same string + «သူ» (e.g. «ဗလာ ဖြစ်၍ အဖုံး ပိတ်ထားသူ»).
- «So» in the training passage = «ထိုသူသည်» (sample), where pi-2 ^2-508 has «ထိုရဟန်းသည်» for its «So».
- For the consistency pass (same Pāli in ch4, translated by another agent): «yā sā vācā nelā kaṇṇasukhā …» (ch4
  madhubhāṇī, spelling pemaniyā), «Idhekacco puggalo āsavānaṃ khayā anāsavaṃ …», «abhiṇhaṃ kujjhati», «sīlavā hoti
  kalyāṇadhammo», «dussīlo hoti pāpadhammo», «musāvādaṃ pahāya musāvādā paṭivirato hoti».
