# Notes: pi-3 Burmese zero-shot SAMPLE (Dhātukathā)

Brief: `burmese-zeroshot-sample-brief.md`. Files: preamble.md, 1-uddeso.md, 2-pathamanayo.md in
`AI_translation/burmese/pi-3-burmese-plain-zeroshot_split_chapters/`; module `my3_formulas.py`, generator
`make_sample.py`, checker `check_sample.py`, terms `my3-zeroshot-terms.md`, segment viewer `seg.py` (read only).
Translated from the Pāli only; no Burmese translation or nissaya opened, no web search; pi-1-my / pi-2-my only read.

## Status
- preamble.md, 1-uddeso.md, 2-pathamanayo.md: generated, the three verifiers OK (see the final report).
- Stopped after the sample (user review).

## How the reuse works (for later agents)
- `my3_formulas.py` loads the FINAL pi-2 module (my2_formulas.py + the pi-2 rails FORMULA_PATCHES, in memory; it
  loads the final pi-1 module itself) and indexes the pi-1 / pi-2 RAILS texts by block ID (FINAL).
- Every topic name, mātikā term, heading and colophon that pi-1 / pi-2 already have is READ from the rails text:
  `items()` (list lines «Head – a, b, c»), `katame()` (pi-1 «Katame dhammā X?»), `matika()` (pi-1 Mātikā line),
  `tattha()` («Tattha katamo X?»), `heads()` (same heading / colophon), `witness()` (a value read by hand, asserted to
  occur in the named segment). WITNESS records where each value was read; the terms file prints it.
- Generator: one engine (translate_line) for all lines; a sentence no frame matches raises Miss and stops the run.
  Later methods: add frames to `F.EXTRA_RULES` (regex on one sentence) and entries to the tables.

## Choices (proposed, for review)
- Book title: Dhātukathāpāḷi = «ဓာတ်များအကြောင်း ဆွေးနွေးခြင်း» (kathā = discussion; pattern of pi-1 / pi-2 titles).
- saṅgaha / asaṅgaha = «အကျုံးဝင်ခြင်း / အကျုံးမဝင်ခြင်း»; saṅgahita = «အကျုံးဝင်» — reused from pi-1 ^1-1044
  (atītaṃsena saṅgahitā = «အတိတ် အပိုင်း၌ အကျုံးဝင်သော»). sampayoga / vippayoga = «ယှဉ်တွဲခြင်း / ကင်းကွာခြင်း»
  (pi-1 SAMP / VIPP).
- Nayamātikā items: «saṅgahitena asaṅgahitaṃ» = «အကျုံးဝင်သည့်အရာဖြင့် အကျုံးမဝင်သည့်အရာ» (instrumental «ဖြင့်»,
  the participle as «… သည့်အရာ»); the «…padaniddeso» headings = «X ပုဒ်ကို အကျယ် ဖော်ပြချက်» (niddeso as pi-1
  Ekakaniddeso; the two members of a compound pair joined by «နှင့်», in the list item by «၊»).
- nayo = «ခွဲနည်း» (pi-1 rails L07); the 14 ordinals are the Pāli loan ordinals ပထမ … ဒသမ, ဧကာဒသမ, ဒွါဒသမ,
  တေရသမ, စုဒ္ဒသမ (pi-1 ORD style). Doubt: 11-14 are less familiar to plain readers; alternative «ဆယ့်တစ်ခုမြောက်»….
- Mātikā names: Nayamātikā «ခွဲနည်း ခေါင်းစဉ်စာရင်း», Abbhantaramātikā «အတွင်း ခေါင်းစဉ်စာရင်း», Nayamukhamātikā
  «ခွဲနည်း၏ တံခါးဝ ခေါင်းစဉ်စာရင်း» (mukha = doorway), Lakkhaṇamātikā «လက္ခဏာ ခေါင်းစဉ်စာရင်း», Bāhiramātikā
  «ပြင်ပ ခေါင်းစဉ်စာရင်း» (bāhira = pi-1 «ပြင်ပ»). Uddeso = «အကျဉ်း ဖော်ပြချက်» (pi-1).
- Sabhāgo, visabhāgo = «တူညီသော သဘော၊ ကွဲပြားသော သဘော».
- ^3-5 «Sabbāpi dhammasaṅgaṇī dhātukathāya mātikāti.» = «“သဘောတရားများကို စုစည်းရေတွက်ခြင်း” အားလုံးသည်လည်း
  “ဓာတ်များအကြောင်း ဆွေးနွေးခြင်း”၏ ခေါင်းစဉ်စာရင်း ဖြစ်သည်။» (book titles quoted mid-sentence; the closing «ti»
  of the outline is not rendered by a word).
- Frames (first method):
  * Q «S katihi khandhehi katihāyatanehi katihi dhātūhi saṅgahito?» = «Sသည် အစုအဝေး မည်မျှ၊ အာရုံခံ နယ်ပယ် မည်မျှ၊
    ဓာတ် မည်မျှတို့တွင် အကျုံးဝင်သနည်း။» (kati = «မည်မျှ», pi-2 ^2-978).
  * A «S COUNTS saṅgahito.» = «Sသည် A n-ပါး၊ B m-ပါးတို့တွင် အကျုံးဝင်သည်။».
  * «Katihi asaṅgahito?» = «မည်မျှတို့တွင် အကျုံးမဝင်သနည်း။»; answer «… တို့တွင် အကျုံးမဝင်။» (bare negative, the
    pi-1 / pi-2 convention «… မဟုတ်။», «… မဖြစ်ပေါ်။»).
  * na kehici / na kāhici («in none»): «အကျုံး(မ)ဝင်ရာ X၊ Y မရှိ» = «there is no X … where it is (not) included»;
    natural Burmese for the double negative «na kehici … asaṅgahito». Mixed answers keep the Pāli order, runs joined by «၊».
  * plural verbs «… ကြသည်», «… ကြသနည်း», «… မဝင်ကြ» follow the Pāli verb number (-ā: singular after a feminine
    singular subject such as dhātu, avijjā, vedanā, taṇhā, jāti, jarā).
  * «asaṅkhataṃ khandhato ṭhapetvā» = «ပြုပြင်ဖန်တီးထားခြင်း မရှိသော သဘောတရားကို အစုအဝေး ရေတွက်ရာမှ ချန်ထား၍»
    (asaṅkhata = pi-1 final; «ရေတွက်ရာမှ» = small clarification of khandhato: the unconditioned is left out of the
    aggregate count).
  * «A ca B ca» / «Añca Bñca» = «Aနှင့် Bတို့»; three or more «A၊ Bနှင့် Cတို့».
  * chains «S1… S2…pe… COUNTS»: every subject «Sသည်», each … / …pe… = one «…».
- Numbers: 1-10 pi-1 NUM; 11, 12, 18, 22 as pi-2 final (ဆယ့်တစ်, ဆယ့်နှစ်, ဆယ့်ရှစ်, နှစ်ဆယ့်နှစ်); 13, 15, 16, 17 the same
  pattern (ဆယ့်သုံး, ဆယ့်ငါး, ဆယ့်ခြောက်, ဆယ့်ခုနစ်), as pi-2 make_ch2-4 NUMW. Classifier «ပါး» (pi-1 / pi-2).
  Note: pi-1 ^1-262 writes «တစ်ဆယ့်ခြောက်ကြိမ်» (16 times); pi-2 and this sample use «ဆယ့်ခြောက်».
- Colophons: (Dukamūlakaṃ.) / (Tikamūlakaṃ.) / (Catukkaṃ.) / (Pañcakaṃ.) = pi-2 final, in round brackets;
  Ekamūlakaṃ, Catukkamūlakaṃ, Dvādasakaṃ, Aṭṭhārasakaṃ = the same pattern (new).
- Headings: Khandho «အစုအဝေး», Āyatanaṃ «အာရုံခံ နယ်ပယ်», Dhātu «ဓာတ်», Saccaṃ «သစ္စာ», Indriyaṃ «စွမ်းရည်»,
  Paṭiccasamuppādādi «အကြောင်းတို့ကို မှီ၍ ဖြစ်ပေါ်ပုံ စသည်», Tikaṃ / Dukaṃ pi-2 final.

## Reused from pi-1 / pi-2 (final rails text)
- Aggregates ^2-1, bases ^2-155, elements ^2-183, faculties ^2-219, truths ^2-218 / ^2-206, dependent arising
  ^2-226 … ^2-233, existences ^2-234, birth … despair ^2-191 … ^2-198, the wings of awakening ^1-357 / ^2-U26,
  jhāna ^2-623, appamaññā ^2-683, adhimokkho ^2-281, manasikāro ^2-766, paṭiccasamuppādo ^2-6-0, phasso … cittaṃ
  (pi-1 NAMES); every «X dhammā» from pi-1 «Katame dhammā X?» (kenaci viññeyyā from the pi-1 Mātikā line).
- «dukkhaṃ» in the dependent-arising list = «ကိုယ်ဆင်းရဲခြင်း» (pi-2 ^2-196, the sacca sense, as in ^2-225), not the
  feeling sense «နာကျင်မှု» (^2-594).
- «saṅkhārapaccayā viññāṇaṃ» = «ပြုပြင်ဖန်တီးမှုများကြောင့် ဖြစ်သော သိစိတ်» (pi-2 ^2-227, suttanta list, plural
  saṅkhārā); pi-2 ^2-249 (abhidhamma part, one cetanā) has the singular «ပြုပြင်ဖန်တီးမှုကြောင့်»: the list sense
  was taken, as the Abbhantaramātikā topic is the twelve-link formula.
- saṅgaha: pi-1 rūpasaṅgaho (^1-584) = «ရုပ်ကို … စုစည်းခြင်း» is the «grouping / summary» sense; the Dhātukathā
  saṅgaha is the inclusion sense of the participle saṅgahita, which pi-1 already renders «အကျုံးဝင်» (^1-1044) and
  pi-1 pariyāpanna «ဘဝဘုံတို့၌ အကျုံးဝင်သော». So saṅgaho = «အကျုံးဝင်ခြင်း» (sense distinction, for review).

## Checks (sample)
- check_chapter_ids / check_text_pe / check_marks: OK for preamble.md (3 segments), 1-uddeso.md (11 segments),
  2-pathamanayo.md (175 segments, 193 lines). chk-pe copies deleted.
- check_sample.py: A regeneration 3 / 3; B 165 content lines, 515 verbs (polarity and number), 992 counts, 0
  mismatches; C reuse 308 / 308 topic names and mātikā terms, 14 / 14 headings / colophons / whole lines identical.

## Unsure Pāli
- ^3-20 «dvādasāyatanehi» (without -h-) read as dvādasahāyatanehi (12).
- ^3-67 «Upapattibhavo … kāmabhavo… saññābhavo… pañcavokārabhavo»: the chain lists items of different scope; the
  Burmese keeps the chain as written.

## Source slips (translated as written)
- ^3-112 variant «[na hetū ahetukā (syā. ka.) vibha. dukapañhāpucchakepi]» gives the same words as the main text
  (the edition probably meant a spacing variant such as «nahetū ahetukā»); kept as a word variant «ပါဌ်ကွဲ», with
  the note «“ခွဲခြမ်းစိတ်ဖြာခြင်း” နှစ်မျိုးတွဲ မေးခွန်းများဖြင့် ဖော်ပြချက်၌လည်း».
- ^3-97 «[parittāramaṇā (?)]»: spelling variant, sigla «(?)» = «(အမည်မသိ မူ)» as pi-2.
- Spelling: pi-3 «upādinn-» where pi-1 has «upādiṇṇ-» (pi-1 lists upādinn- as the Syā. spelling); same term, same
  Burmese (TERM_ALIAS).
- ^3-66 «kammabhavo [upādānapaccayā kammabhavo (sī. syā.)]»: the main text lacks «upādānapaccayā»; word variant.
