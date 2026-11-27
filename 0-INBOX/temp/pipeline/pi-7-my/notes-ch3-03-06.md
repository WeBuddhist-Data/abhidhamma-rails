# pi-7 3-03 āsavagocchaka, 3-04 saññojanagocchaka, 3-05 ganthagocchaka, 3-06 oghayogagocchaka: Burmese zero-shot notes

PROGRESS: DONE (2026-11-24). Written to AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters/:
3-03 (318 segments, 533 lines), 3-04 (288 segments, 457 lines), 3-05 (283 segments, 431 lines), 3-06 (4 segments,
5 lines). Checks (all four): check_chapter_ids OK; check_marks OK; check_text (pi-3-mr/check_text.py on a «…Pe…»-folded
copy in pi-7-my/chk-pe/ch3-03-06/, deleted afterwards; check_text_pe7.py not run on the shared chk-pe/) OK, dashes
match; check_ch3-03-06.py 0 mismatches (S/P/C/O/N on 1426 lines, I 2357 sentences, T 163), reuse 88 / 88 terms +
630 / 630 sentences, identity with 1-01, 1-03 … 1-05, 2-03 … 2-06, 3-01 … 3-02 77 / 77, --sample identical,
--mutate 10 / 10; make_ch3-03-06.py --regress: the sample (1-00, 1-02), 2-03 … 2-06 and 3-01 … 3-02 regenerate
identical through this engine.

## Files
- make_ch3-03-06.py: generator. IMPORTS make_ch3-01-02.py (which imports make_ch2-03-06.py: PRIMARY my7_formulas +
  make_sample + make_ch1-01, FALLBACK make_ch1-03-05) with its dyad machinery; nothing of another group is run or
  written (its main() does not run). `--dev` (chk-ch3-03-06/dev.txt), `--regress`, `--slips`, `--out DIR`.
- check_ch3-03-06.py: checker (adapted from check_ch3-01-02.py; own copy of the dyad terms, names and Pāli term
  regexes; the active dyad of a line from the Pāli dyad headings; 3-06 by its two sentences); `--sample --pe
  --mutate --groups`.
- chk-ch3-03-06/: my scratch (dev output, query scripts).

## How the clusters are run
- One table per cluster X (āsava, saññojana, gantha; ogha, yoga in 3-06) builds its six dyads and names from the pi-1
  final Mātikā ^1-M2-14 … ^1-M2-43 (W()): X / no X; S / a-S; X-sampayutta / X-vippayutta; «X ceva S ca» / «S ceva no
  ca X»; «X ceva X-sampayutta ca» / «X-sampayutta ceva no ca X»; «X-vippayutta S» / «X-vippayutta a-S».
- Each chapter is cut at its dyad headings (make_ch3-01-02's parts_of); only that dyad is active. 3-06 has no dyad
  heading: it is cut before «Oghaṃ dhammaṃ» (ogha) and «Yogaṃ dhammaṃ» (yoga).
- X is a dyad term only before a dhamma word (or coordinated with «no X» before one) and before the noun hetū
  («ganthā hetū» «အထုံး ဖြစ်သော အမြစ်တို့», «ganthā ca noganthā ca hetū» «အထုံး ဖြစ်သော၊ အထုံး မဟုတ်သော
  အမြစ်တို့», both members on one noun as 3-01-02); otherwise it is the noun («āsave paṭicca …» «စိတ်အစွန်းအထင်းတို့ကို
  မှီ၍»). In the other dyads «X-ā hetū» gets the same Burmese «X ဖြစ်သော အမြစ်». «X-sampayuttaka» = the term
  X-sampayutta in its dyad, and the same Burmese (a qualifier) elsewhere.
- pi-7 spells saññojana; the Burmese is the pi-1 saṃyojana Burmese (witnessed with the pi-1 spelling). saññojana is
  read as a neuter noun (-aṃ subject or object, as the āyatana names), also with the masculine -o of the Pāli.
- The gantha names written in two words («sīlabbataparāmāsaṃ kāyaganthaṃ», «idaṃsaccābhinivesaṃ kāyaganthaṃ») are
  read as the one-word compounds (same Burmese).
- Notes: plain ones in K.NOTE_FIXED; whole notes with condition / count words or several sentences as placeholders
  «(⁑d<i>)» (as 3-01-02's NOTEP). The link «saṃsaṭṭho» also for «saṃsaṭṭhaṃ / saṃsaṭṭhā».
- Coordinator decisions applied: «Anulomaṃ.» (order) «အဟုတ်ပြ ပုံစံ။» (21 lines); «anulomaṃ» (the mind moment
  before gotrabhu / vodāna) «လျော်ညီခြင်း စိတ်» (4 lines); «Sahajātā –» bare «အတူ ပေါ်ပေါက်ခြင်း –» (23), in the
  kamma section «အတူ ပေါ်ပေါက်သည့် ကံ –» (8, next to «ခဏ ကွဲပြားသည့် ကံ –»). No asaññasattānaṃ and no heinous deeds in
  these chapters.

## New terms and formulas (Pāli = Burmese)
### Dyad terms (pi-1 final, read with W())
āsava = စိတ်အစွန်းအထင်း ဖြစ်သော; no āsava = စိတ်အစွန်းအထင်း မဟုတ်သော (^1-M2-14)
sāsava = စိတ်အစွန်းအထင်း၏ အာရုံ ဖြစ်နိုင်သော; anāsava = စိတ်အစွန်းအထင်း၏ အာရုံ မဖြစ်နိုင်သော (^1-M2-15)
āsavasampayutta = စိတ်အစွန်းအထင်းနှင့် ယှဉ်တွဲသော; āsavavippayutta = စိတ်အစွန်းအထင်းနှင့် ကင်းကွာသော (^1-M2-16)
āsavo ceva sāsavo ca = စိတ်အစွန်းအထင်းလည်း ဖြစ်၊ စိတ်အစွန်းအထင်း၏ အာရုံလည်း ဖြစ်နိုင်သော; sāsavo ceva no ca āsavo = စိတ်အစွန်းအထင်း၏ အာရုံ ဖြစ်နိုင်သော်လည်း စိတ်အစွန်းအထင်း မဟုတ်သော (^1-M2-17)
āsavo ceva āsavasampayutto ca = စိတ်အစွန်းအထင်းလည်း ဖြစ်၊ စိတ်အစွန်းအထင်းနှင့်လည်း ယှဉ်တွဲသော; āsavasampayutto ceva no ca āsavo = စိတ်အစွန်းအထင်းနှင့် ယှဉ်တွဲသော်လည်း စိတ်အစွန်းအထင်း မဟုတ်သော (^1-M2-18)
āsavavippayutto sāsavo / anāsavo = NEW (pi-1 ^1-M2-19 is not attributive): the pattern of 3-01's «nahetu sahetuko /
ahetuko» (see the list below)
The same six pairs for saññojana (နှောင်ကြိုး, ^1-M2-20 … 25), gantha (အထုံး, ^1-M2-26 … 31), ogha (ရေအလျဉ်,
^1-M2-32 … 37), yoga (ထမ်းပိုး, ^1-M2-38 … 43); S = «N၏ အာရုံ ဖြစ်နိုင်သော».
### Cluster names (pi-1 final): Āsavagocchakaṃ = စိတ်အစွန်းအထင်းတို့၏ အစု; Saññojanagocchakaṃ = နှောင်ကြိုးတို့၏ အစု;
Ganthagocchakaṃ = အထုံးတို့၏ အစု; Ogha- = ရေအလျဉ်တို့၏ အစု; Yoga- = ထမ်းပိုးတို့၏ အစု.
### Nouns (pi-1 rails / termbase, W()): āsava = စိတ်အစွန်းအထင်း; saṃyojana = နှောင်ကြိုး; gantha = အထုံး; ogha =
ရေအလျဉ်; yoga = ထမ်းပိုး; paṭigha = မုန်းတီးမှု (^1-1066); domanassasahagata = စိတ်ဆင်းရဲမှုနှင့်အတူ ဖြစ်သော (^1-413);
diṭṭhigatavippayutta = အယူမှားနှင့် ကင်းကွာသော (^1-400); diṭṭhigatavippayutta-lobhasahagata = အယူမှားနှင့် ကင်းကွာသော၊
လောဘနှင့်အတူ ဖြစ်သော (^1-1406); domanassasahagatādhipati / diṭṭhigatavippayuttalobhasahagatādhipati = «Q အကြီးအမှူး»
(as chandādhipati); and the cluster members:
- kāmāsav = ကာမ စိတ်အစွန်းအထင်း
- bhavāsav = ဘဝ စိတ်အစွန်းအထင်း
- diṭṭhāsav = အယူ စိတ်အစွန်းအထင်း
- avijjāsav = အမှန်ကို မသိမှု စိတ်အစွန်းအထင်း
- kāmarāgasaññojan = ကာမရာဂ နှောင်ကြိုး
- paṭighasaññojan = မုန်းတီးမှု နှောင်ကြိုး
- mānasaññojan = မာန နှောင်ကြိုး
- diṭṭhisaññojan = အယူ နှောင်ကြိုး
- vicikicchāsaññojan = ယုံမှားမှု နှောင်ကြိုး
- sīlabbataparāmāsasaññojan = သီလ အကျင့်ဝတ်ဆိုင်ရာ မှားယွင်းသော ယူဆမှု နှောင်ကြိုး
- bhavarāgasaññojan = ဘဝရာဂ နှောင်ကြိုး
- issāsaññojan = ငြူစူမှု နှောင်ကြိုး
- macchariyasaññojan = ဝန်တိုမှု နှောင်ကြိုး
- avijjāsaññojan = အမှန်ကို မသိမှု နှောင်ကြိုး
- abhijjhākāyaganth = သူ့ဥစ္စာကို လိုချင်ခြင်းဟူသော ကိုယ် အထုံး
- byāpādakāyaganth = ဖျက်ဆီးလိုစိတ်ဟူသော ကိုယ် အထုံး
- sīlabbataparāmāsakāyaganth = သီလ အကျင့်ဝတ်ဆိုင်ရာ မှားယွင်းသော ယူဆမှုဟူသော ကိုယ် အထုံး
- idaṃsaccābhinivesakāyaganth = ဤအရာသာ အမှန်ဟု သက်ဝင်ယုံကြည်ခြင်းဟူသော ကိုယ် အထုံး
### Every new string of the generator (NEW, names, notes, placeholders, headings)
- āsavavippayutto sāsavo (dyad term) = စိတ်အစွန်းအထင်းနှင့် ကင်းကွာသော်လည်း စိတ်အစွန်းအထင်း၏ အာရုံ ဖြစ်နိုင်သော
- āsavavippayutto anāsavo (dyad term) = စိတ်အစွန်းအထင်းနှင့် ကင်းကွာ၊ စိတ်အစွန်းအထင်း၏ အာရုံ မဖြစ်နိုင်သော
- Āsavadukaṃ = စိတ်အစွန်းအထင်း နှစ်မျိုးတွဲ
- Sāsavadukaṃ = စိတ်အစွန်းအထင်း၏ အာရုံ ဖြစ်နိုင်ခြင်း နှစ်မျိုးတွဲ
- Āsavasampayuttadukaṃ = စိတ်အစွန်းအထင်းနှင့် ယှဉ်တွဲခြင်း နှစ်မျိုးတွဲ
- Āsavasāsavadukaṃ = စိတ်အစွန်းအထင်း ဖြစ်ခြင်းနှင့် စိတ်အစွန်းအထင်း၏ အာရုံ ဖြစ်နိုင်ခြင်း နှစ်မျိုးတွဲ
- Āsavaāsavasampayuttadukaṃ = စိတ်အစွန်းအထင်း ဖြစ်ခြင်းနှင့် စိတ်အစွန်းအထင်းနှင့် ယှဉ်တွဲခြင်း နှစ်မျိုးတွဲ
- Āsavavippayuttasāsavadukaṃ = စိတ်အစွန်းအထင်းနှင့် ကင်းကွာခြင်းနှင့် စိတ်အစွန်းအထင်း၏ အာရုံ ဖြစ်နိုင်ခြင်း နှစ်မျိုးတွဲ
- saññojanavippayutto saññojaniyo (dyad term) = နှောင်ကြိုးနှင့် ကင်းကွာသော်လည်း နှောင်ကြိုး၏ အာရုံ ဖြစ်နိုင်သော
- saññojanavippayutto asaññojaniyo (dyad term) = နှောင်ကြိုးနှင့် ကင်းကွာ၊ နှောင်ကြိုး၏ အာရုံ မဖြစ်နိုင်သော
- Saññojanadukaṃ = နှောင်ကြိုး နှစ်မျိုးတွဲ
- Saññojaniyadukaṃ = နှောင်ကြိုး၏ အာရုံ ဖြစ်နိုင်ခြင်း နှစ်မျိုးတွဲ
- Saññojanasampayuttadukaṃ = နှောင်ကြိုးနှင့် ယှဉ်တွဲခြင်း နှစ်မျိုးတွဲ
- Saññojanasaññojaniyadukaṃ = နှောင်ကြိုး ဖြစ်ခြင်းနှင့် နှောင်ကြိုး၏ အာရုံ ဖြစ်နိုင်ခြင်း နှစ်မျိုးတွဲ
- Saññojanasaññojanasampayuttadukaṃ = နှောင်ကြိုး ဖြစ်ခြင်းနှင့် နှောင်ကြိုးနှင့် ယှဉ်တွဲခြင်း နှစ်မျိုးတွဲ
- Saññojanavippayuttasaññojaniyadukaṃ = နှောင်ကြိုးနှင့် ကင်းကွာခြင်းနှင့် နှောင်ကြိုး၏ အာရုံ ဖြစ်နိုင်ခြင်း နှစ်မျိုးတွဲ
- ganthavippayutto ganthaniyo (dyad term) = အထုံးနှင့် ကင်းကွာသော်လည်း အထုံး၏ အာရုံ ဖြစ်နိုင်သော
- ganthavippayutto aganthaniyo (dyad term) = အထုံးနှင့် ကင်းကွာ၊ အထုံး၏ အာရုံ မဖြစ်နိုင်သော
- Ganthadukaṃ = အထုံး နှစ်မျိုးတွဲ
- Ganthaniyadukaṃ = အထုံး၏ အာရုံ ဖြစ်နိုင်ခြင်း နှစ်မျိုးတွဲ
- Ganthasampayuttadukaṃ = အထုံးနှင့် ယှဉ်တွဲခြင်း နှစ်မျိုးတွဲ
- Ganthaganthaniyadukaṃ = အထုံး ဖြစ်ခြင်းနှင့် အထုံး၏ အာရုံ ဖြစ်နိုင်ခြင်း နှစ်မျိုးတွဲ
- Ganthaganthasampayuttadukaṃ = အထုံး ဖြစ်ခြင်းနှင့် အထုံးနှင့် ယှဉ်တွဲခြင်း နှစ်မျိုးတွဲ
- Ganthavippayuttaganthaniyadukaṃ = အထုံးနှင့် ကင်းကွာခြင်းနှင့် အထုံး၏ အာရုံ ဖြစ်နိုင်ခြင်း နှစ်မျိုးတွဲ
- oghavippayutto oghaniyo (dyad term) = ရေအလျဉ်နှင့် ကင်းကွာသော်လည်း ရေအလျဉ်၏ အာရုံ ဖြစ်နိုင်သော
- oghavippayutto anoghaniyo (dyad term) = ရေအလျဉ်နှင့် ကင်းကွာ၊ ရေအလျဉ်၏ အာရုံ မဖြစ်နိုင်သော
- Oghadukaṃ = ရေအလျဉ် နှစ်မျိုးတွဲ
- Oghaniyadukaṃ = ရေအလျဉ်၏ အာရုံ ဖြစ်နိုင်ခြင်း နှစ်မျိုးတွဲ
- Oghasampayuttadukaṃ = ရေအလျဉ်နှင့် ယှဉ်တွဲခြင်း နှစ်မျိုးတွဲ
- Oghaoghaniyadukaṃ = ရေအလျဉ် ဖြစ်ခြင်းနှင့် ရေအလျဉ်၏ အာရုံ ဖြစ်နိုင်ခြင်း နှစ်မျိုးတွဲ
- Oghaoghasampayuttadukaṃ = ရေအလျဉ် ဖြစ်ခြင်းနှင့် ရေအလျဉ်နှင့် ယှဉ်တွဲခြင်း နှစ်မျိုးတွဲ
- Oghavippayuttaoghaniyadukaṃ = ရေအလျဉ်နှင့် ကင်းကွာခြင်းနှင့် ရေအလျဉ်၏ အာရုံ ဖြစ်နိုင်ခြင်း နှစ်မျိုးတွဲ
- yogavippayutto yoganiyo (dyad term) = ထမ်းပိုးနှင့် ကင်းကွာသော်လည်း ထမ်းပိုး၏ အာရုံ ဖြစ်နိုင်သော
- yogavippayutto ayoganiyo (dyad term) = ထမ်းပိုးနှင့် ကင်းကွာ၊ ထမ်းပိုး၏ အာရုံ မဖြစ်နိုင်သော
- Yogadukaṃ = ထမ်းပိုး နှစ်မျိုးတွဲ
- Yoganiyadukaṃ = ထမ်းပိုး၏ အာရုံ ဖြစ်နိုင်ခြင်း နှစ်မျိုးတွဲ
- Yogasampayuttadukaṃ = ထမ်းပိုးနှင့် ယှဉ်တွဲခြင်း နှစ်မျိုးတွဲ
- Yogayoganiyadukaṃ = ထမ်းပိုး ဖြစ်ခြင်းနှင့် ထမ်းပိုး၏ အာရုံ ဖြစ်နိုင်ခြင်း နှစ်မျိုးတွဲ
- Yogayogasampayuttadukaṃ = ထမ်းပိုး ဖြစ်ခြင်းနှင့် ထမ်းပိုးနှင့် ယှဉ်တွဲခြင်း နှစ်မျိုးတွဲ
- Yogavippayuttayoganiyadukaṃ = ထမ်းပိုးနှင့် ကင်းကွာခြင်းနှင့် ထမ်းပိုး၏ အာရုံ ဖြစ်နိုင်ခြင်း နှစ်မျိုးတွဲ
- garukārammaṇā = လေးစားဖွယ်ရာ အာရုံ
- assādanā = သာယာ နှစ်သက်ခြင်း
- vibhajanā = ခွဲခြမ်းစိတ်ဖြာခြင်း
- parivattetabbaṃ / -ā = လှည့်ပြောင်းရမည်
- na kātabbaṃ = မပြုရ
- sekhā (persons) = ကျင့်ကြံဆဲသူတို့သည်
- Oghayogagocchakaṃ = ရေအလျဉ်တို့၏ အစုနှင့် ထမ်းပိုးတို့၏ အစု
- 1-7. Paṭiccavārādi = 1-7. မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက် စသည်
- 1-7. Vārasattakaṃ = 1-7. ဖော်ပြချက် ခုနစ်မျိုးတွဲ
- 1-4. Paccayacatukkaṃ = 1-4. အကြောင်း လေးမျိုးတွဲ
- Oghādidukāni = ရေအလျဉ် စသည်တို့၏ နှစ်မျိုးတွဲများ
- vippayuttakā (cetanā) = ကင်းကွာသော
- vibhajitabbaṃ = ခွဲခြမ်းစိတ်ဖြာရမည်
- evaṃ kātabbaṃ = ဤသို့ ပြုရမည်
- anantarasadisaṃ = ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းနှင့် တူသည်
- āvajjanāpi vuṭṭhānampi natthi = စိတ်ညွတ်ခြင်းလည်း၊ ထမြောက်ခြင်း စိတ်လည်း မရှိ
- mūlā pucchitabbā = အခြေခံတို့ကို မေးရမည်
- āsavasadisaṃ = စိတ်အစွန်းအထင်းနှင့် တူသည်
- mahābhūtā = မူလဓာတ်ကြီးများ
- tīṇipi upanissayā = အားကြီးသော အမှီ သုံးခုလုံး
- mūlaṃ = အခြေခံ
- garukārammaṇā kātabbā = လေးစားဖွယ်ရာ အာရုံအဖြစ် ပြုရမည်
- anulomamātikā = အဟုတ်ပြ ပုံစံ၏ ခေါင်းစဉ်စာရင်း
- samuddiṭṭhaṃ saṃkhittaṃ = အကျဉ်းချုပ်၍ ဖော်ပြထားသည်
- nayena = နည်းအတိုင်း
- uddharitabbā = ထုတ်နုတ်ရမည်
- yattha yattha … labbhati, tattha tattha ninnetabbaṃ = တွေ့ရသည့် နေရာတိုင်း၊ ထိုထို နေရာ၌ ထည့်သွင်းရမည်
- ṭhapetvā = ချန်ထား၍
- majjhe = အလယ်၌
- vibhajantena = ခွဲခြမ်းစိတ်ဖြာလျက်
- paṭhamaṃ (first) = ပထမ
- pacchā = နောက်မှ
- vibhāgo = ခွဲခြားချက်
- gocchakā = အစု
- (ekekampi cakkaṃ kātabbaṃ) = (တစ်ခုစီကိုလည်း စက်ဝိုင်း ပြုရမည်)
- (āsavamūlakaṃ tīṇi, paṭiccasadisā) = (စိတ်အစွန်းအထင်း ဖြစ်သော သဘောတရားကို အခြေခံခြင်း၌ သုံးခု၊ မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူကြသည်)
- (evaṃ sabbe gaṇanā gaṇetabbā) = (ဤသို့ ရေတွက်ချက် အားလုံးကို ရေတွက်ရမည်)
- (Gaṇanāpi sampayuttavāropi saṃsaṭṭhavārasadiso.) = (ရေတွက်ချက်လည်း၊ ယှဉ်တွဲခြင်းအလိုက် ဖော်ပြချက်လည်း ရောနှောခြင်းအလိုက် ဖော်ပြချက်နှင့် တူသည်။)
- (dutiyagamanaṃ) = (ဒုတိယ သွားပုံ)
- (tīṇi ārammaṇasadisā, garukārammaṇā kātabbā) = (သုံးခု အာရုံဟူသော အကြောင်းနှင့် တူကြသည်၊ လေးစားဖွယ်ရာ အာရုံအဖြစ် ပြုရမည်)
- (tīṇi, garukārammaṇā) = (သုံးခု၊ လေးစားဖွယ်ရာ အာရုံ)
- (vatthu ca dassetabbaṃ) = (မှီရာ ဝတ္ထုကိုလည်း ပြသရမည်)
- (anulomapadā paripuṇṇā) = (အဟုတ်ပြ ပုံစံ၏ ပုဒ်တို့ ပြည့်စုံကြသည်)
- (anulomapadāni gaṇitabbāni) = (အဟုတ်ပြ ပုံစံ၏ ပုဒ်တို့ကို ရေတွက်ရမည်)
- (anulomapadāni kātabbāni) = (အဟုတ်ပြ ပုံစံ၏ ပုဒ်တို့ကို ပြုရမည်)
- (anulomapadāni paripuṇṇāni kātabbāni) = (အဟုတ်ပြ ပုံစံ၏ ပုဒ်တို့ကို ပြည့်စုံအောင် ပြုရမည်)
- (Yathā cūḷantaraduke lokiyadukaṃ evaṃ kātabbaṃ ninnānākaraṇaṃ.) = (ကြားညှပ် နှစ်မျိုးတွဲ အစုငယ်၌ လောကနှင့် သက်ဆိုင်ခြင်း နှစ်မျိုးတွဲကဲ့သို့ ထိုနည်းတူ ကွဲပြားချက် မရှိ ပြုရမည်။)
- (Yathā cūḷantaraduke lokiyadukaṃ evaṃ vitthāretabbaṃ ninnānākaraṇaṃ, saṃkhittaṃ.) = (ကြားညှပ် နှစ်မျိုးတွဲ အစုငယ်၌ လောကနှင့် သက်ဆိုင်ခြင်း နှစ်မျိုးတွဲကဲ့သို့ ထိုနည်းတူ ကွဲပြားချက် မရှိ အကျယ် ချဲ့ရမည်၊ အကျဉ်းချုပ်။)
- (yathā cūḷantaraduke lokiyadukaṃ evaṃ vitthāretabbaṃ ninnānākaraṇaṃ) = (ကြားညှပ် နှစ်မျိုးတွဲ အစုငယ်၌ လောကနှင့် သက်ဆိုင်ခြင်း နှစ်မျိုးတွဲကဲ့သို့ ထိုနည်းတူ ကွဲပြားချက် မရှိ အကျယ် ချဲ့ရမည်)
- (Yathā cūḷantaraduke lokiyadukaṃ evaṃ vibhajitabbaṃ ninnānākaraṇaṃ.) = (ကြားညှပ် နှစ်မျိုးတွဲ အစုငယ်၌ လောကနှင့် သက်ဆိုင်ခြင်း နှစ်မျိုးတွဲကဲ့သို့ ထိုနည်းတူ ကွဲပြားချက် မရှိ ခွဲခြမ်းစိတ်ဖြာရမည်။)
- (Cūḷantaraduke lokiyadukasadisaṃ, ninnānākaraṇaṃ.) = (ကြားညှပ် နှစ်မျိုးတွဲ အစုငယ်၌ လောကနှင့် သက်ဆိုင်ခြင်း နှစ်မျိုးတွဲနှင့် တူသည်၊ ကွဲပြားချက် မရှိ။)
- (Imaṃ dukaṃ cūḷantaraduke lokiyadukasadisaṃ ninnānākaraṇaṃ.) = (ဤ နှစ်မျိုးတွဲသည် ကွဲပြားချက် မရှိ ကြားညှပ် နှစ်မျိုးတွဲ အစုငယ်၌ လောကနှင့် သက်ဆိုင်ခြင်း နှစ်မျိုးတွဲနှင့် တူသည်။)
- (Evaṃ sabbe paccayā vitthāretabbā. Saṃkhittaṃ.) = (ဤသို့ အကြောင်း အားလုံးကို အကျယ် ချဲ့ရမည်။ အကျဉ်းချုပ်။)
- (Cakkaṃ. Evaṃ sabbe paccayā kātabbā.) = (စက်ဝိုင်း။ ဤသို့ အကြောင်း အားလုံးကို ပြုရမည်။)
- (Napacchājātapaccayā nava, naāsevanapaccayā nava.) = (နောက်မှ ဖြစ်ပေါ်ခြင်းဟူသော အကြောင်းကြောင့် မဟုတ်ဘဲ ကိုးခု၊ အလေ့အကျင့် ပြုခြင်းဟူသော အကြောင်းကြောင့် မဟုတ်ဘဲ ကိုးခု။)
- (Idha assādanā natthi) = (ဤနေရာ၌ သာယာ နှစ်သက်ခြင်း မရှိ)
- (Pucchitabbaṃ mūlaṃ) = (အခြေခံကို မေးရမည်)
- (evaṃ cakkaṃ bandhitabbaṃ) = (ဤသို့ စက်ဝိုင်း ဖွဲ့ရမည်)
- (sabbaṃ cakkaṃ) = (အားလုံး စက်ဝိုင်း)
- (Evaṃ paṭiccavāropi sahajātavāropi paccayavāropi nissayavāropi saṃsaṭṭhavāropi sampayuttavāropi yathā āsavadukaṃ evaṃ kātabbaṃ, ninnānaṃ.) = (ဤသို့ မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်ကိုလည်း၊ အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်ကိုလည်း၊ အကြောင်းပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်ကိုလည်း၊ အမှီပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်ကိုလည်း၊ ရောနှောခြင်းအလိုက် ဖော်ပြချက်ကိုလည်း၊ ယှဉ်တွဲခြင်းအလိုက် ဖော်ပြချက်ကိုလည်း စိတ်အစွန်းအထင်း နှစ်မျိုးတွဲကဲ့သို့ ထိုနည်းတူ ပြုရမည်၊ ကွဲပြားမှု မရှိ။)
- (Pañhāvāre hetupaccayepi ārammaṇapaccayepi lokuttaraṃ na kātabbaṃ, sekhā gotrabhuṃ paccavekkhanti, vodānaṃ paccavekkhantīti kātabbā. Adhipatipaccayampi sabbaṃ jānitvā kātabbaṃ.) = (ပြဿနာအလိုက် ဖော်ပြချက်၌ အမြစ်ဟူသော အကြောင်း၌လည်း၊ အာရုံဟူသော အကြောင်း၌လည်း လောကကို ကျော်လွန်သော သဘောတရားကို မပြုရ၊ ကျင့်ကြံဆဲသူတို့သည် အနွယ် ပြောင်းခြင်း စိတ်ကို ပြန်လည် ဆင်ခြင်ကြသည်၊ စင်ကြယ်ခြင်း စိတ်ကို ပြန်လည် ဆင်ခြင်ကြသည်ဟု ပြုရမည်။ အကြီးအမှူးဟူသော အကြောင်းကိုလည်း အားလုံး သိ၍ ပြုရမည်။)
- (evaṃ sabbaṃ vitthāretabbaṃ) = (ဤသို့ အားလုံးကို အကျယ် ချဲ့ရမည်)
- (Āsavadukepi anantaraṃ iminā sadisaṃ kātabbaṃ. Āvajjanāpi vuṭṭhānampi evaṃ samuddiṭṭhaṃ saṃkhittaṃ. Sabbaṃ paripuṇṇaṃ. Āsavadukasadisaṃ kātabbaṃ, ninnānaṃ.) = (စိတ်အစွန်းအထင်း နှစ်မျိုးတွဲ၌လည်း ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းဟူသော အကြောင်းကို ဤသည်နှင့် တူအောင် ပြုရမည်။ စိတ်ညွတ်ခြင်းလည်း၊ ထမြောက်ခြင်း စိတ်လည်း ဤသို့ အကျဉ်းချုပ်၍ ဖော်ပြထားသည်။ အားလုံး ပြည့်စုံသည်။ စိတ်အစွန်းအထင်း နှစ်မျိုးတွဲနှင့် တူအောင် ပြုရမည်၊ ကွဲပြားမှု မရှိ။)
- (vipākaṃ natthi) = (ကံ၏ အကျိုး မရှိ)
- (nahetumūlakaṃ natthi) = (အမြစ်ဟူသော အကြောင်း မဟုတ်ခြင်းကို အခြေခံခြင်း မရှိ)
- (Evaṃ itare dve gaṇanāpi sahajātavārampi paccayavārampi nissayavārampi saṃsaṭṭhavārampi sampayuttavārampi paripuṇṇaṃ paṭiccasadisā.) = (ဤသို့ အခြား ရေတွက်ချက် နှစ်ခုလည်း၊ အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း၊ အကြောင်းပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်လည်း၊ အမှီပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်လည်း၊ ရောနှောခြင်းအလိုက် ဖော်ပြချက်လည်း၊ ယှဉ်တွဲခြင်းအလိုက် ဖော်ပြချက်လည်း ပြည့်စုံစွာ မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူကြသည်။)
- (ārammaṇasadisā, garukārammaṇā) = (အာရုံဟူသော အကြောင်းနှင့် တူကြသည်၊ လေးစားဖွယ်ရာ အာရုံ)
- (ārammaṇasadisā, garukārammaṇā kātabbā) = (အာရုံဟူသော အကြောင်းနှင့် တူကြသည်၊ လေးစားဖွယ်ရာ အာရုံအဖြစ် ပြုရမည်)
- (ārammaṇasadisāyeva, purimā purimāti kātabbā.) = (အာရုံဟူသော အကြောင်းနှင့် တူကြသည်ပင်၊ ရှေးရှေးဟု ပြုရမည်။)
- (ārammaṇasadisaṃyeva, vibhajanā natthi… tīṇi. Upanissayaṃ sabbaṃ kātabbaṃ) = (အာရုံဟူသော အကြောင်းနှင့် တူသည်ပင်၊ ခွဲခြမ်းစိတ်ဖြာခြင်း မရှိ… သုံးခု။ အားကြီးသော အမှီဟူသော အကြောင်းကို အားလုံး ပြုရမည်)
- (evaṃ itarepi dve gaṇanā kātabbā) = (ဤသို့ အခြား ရေတွက်ချက် နှစ်ခုကိုလည်း ပြုရမည်)
- (vibhajitabbaṃ āsavasadisaṃ) = (စိတ်အစွန်းအထင်းနှင့် တူအောင် ခွဲခြမ်းစိတ်ဖြာရမည်)
- (yāva paṭisandhi) = (ပဋိသန္ဓေအထိ)
- (yāva mahābhūtā) = (မူလဓာတ်ကြီးတို့အထိ)
- (paṭiccasadisā) = (မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူကြသည်)
- (ārammaṇanayena kātabbā) = (အာရုံဟူသော အကြောင်း၏ နည်းအတိုင်း ပြုရမည်)
- (Ārammaṇapaccaye rūpaṃ natthi. Adhipatipaccayo hetusadiso, vicikicchāsaññojanaṃ natthi.) = (အာရုံဟူသော အကြောင်း၌ ရုပ် မရှိ။ အကြီးအမှူးဟူသော အကြောင်းသည် အမြစ်နှင့် တူသည်၊ ယုံမှားမှု နှောင်ကြိုး မရှိ။)
- (Saṃkhittaṃ. Āsavagocchakasadisaṃ. Naārammaṇāpi sabbe uddharitabbā.) = (အကျဉ်းချုပ်။ စိတ်အစွန်းအထင်းတို့၏ အစုနှင့် တူသည်။ အာရုံဟူသော အကြောင်း မဟုတ်ခြင်းတို့ကိုလည်း အားလုံး ထုတ်နုတ်ရမည်။)
- (evaṃ sabbaṃ gaṇetabbaṃ) = (ဤသို့ အားလုံးကို ရေတွက်ရမည်)
- (yattha yattha vatthu labbhati, tattha tattha ninnetabbaṃ) = (မှီရာ ဝတ္ထုကို တွေ့ရသည့် နေရာတိုင်း၊ ထိုထို နေရာ၌ ထည့်သွင်းရမည်)
- (Evaṃ itarepi dve gaṇanā ca nissayavāro ca kātabbo.) = (ဤသို့ အခြား ရေတွက်ချက် နှစ်ခုကိုလည်းကောင်း၊ အမှီပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်ကိုလည်းကောင်း ပြုရမည်။)
- (evaṃ nava pañhā. Arūpāyeva kātabbā) = (ဤသို့ ပြဿနာ ကိုးခု။ ရုပ် မဟုတ်သော သဘောတရားတို့ကိုသာ ပြုရမည်)
- (Saṃsaṭṭhavāropi sampayuttavāropi evaṃ kātabbā.) = (ရောနှောခြင်းအလိုက် ဖော်ပြချက်ကိုလည်း၊ ယှဉ်တွဲခြင်းအလိုက် ဖော်ပြချက်ကိုလည်း ဤသို့ ပြုရမည်။)
- (ārabbhayeva kātabbā) = (အာရုံပြု၍ဟုသာ ပြုရမည်)
- (ārabbha kātabbā) = (အာရုံပြု၍ဟု ပြုရမည်)
- (tiṇṇampi ārammaṇādhipati, sahajātādhipatipi kātabbā, vibhajitabbā tīṇipi) = (သုံးခုလုံး၌ အာရုံ အကြီးအမှူး၊ အတူ ပေါ်ပေါက်သော အကြီးအမှူးကိုလည်း ပြုရမည်၊ သုံးခုလုံးကို ခွဲခြမ်းစိတ်ဖြာရမည်)
- (evaṃ dvepi kātabbā) = (ဤသို့ နှစ်ခုလုံးကို ပြုရမည်)
- (evaṃ tīṇipi) = (ဤသို့ သုံးခုလုံး)
- (saṃkhittaṃ, evaṃ kātabbaṃ) = (အကျဉ်းချုပ်၊ ဤသို့ ပြုရမည်)
- (Itare dve gaṇanāpi sampayuttavāropi kātabbo.) = (အခြား ရေတွက်ချက် နှစ်ခုကိုလည်း၊ ယှဉ်တွဲခြင်းအလိုက် ဖော်ပြချက်ကိုလည်း ပြုရမည်။)
- (Saññojanagocchake paṭhamadukasadisaṃ.) = (နှောင်ကြိုးတို့၏ အစု၌ ပထမ နှစ်မျိုးတွဲနှင့် တူသည်။)
- (Evaṃ imampi dukaṃ vitthāretabbaṃ, ninnānākaraṇaṃ ṭhapetvā lokuttaraṃ) = (ဤသို့ ဤ နှစ်မျိုးတွဲကိုလည်း အကျယ် ချဲ့ရမည်၊ လောကကို ကျော်လွန်သော သဘောတရားကို ချန်ထား၍ ကွဲပြားချက် မရှိ)
- (Evaṃ itare dve gaṇanāpi sahajātavāropi kātabbo. Paccayavāropi nissayavāropi saṃsaṭṭhavāropi sampayuttavāropi paṭiccavārasadisā.) = (ဤသို့ အခြား ရေတွက်ချက် နှစ်ခုကိုလည်း၊ အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်ကိုလည်း ပြုရမည်။ အကြောင်းပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်လည်း၊ အမှီပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်လည်း၊ ရောနှောခြင်းအလိုက် ဖော်ပြချက်လည်း၊ ယှဉ်တွဲခြင်းအလိုက် ဖော်ပြချက်လည်း မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူကြသည်။)
- (imāsu tīsupi pañhāsu ārammaṇādhipatipi sahajātādhipatipi kātabbā) = (ဤ ပြဿနာ သုံးခုလုံး၌ အာရုံ အကြီးအမှူးကိုလည်း၊ အတူ ပေါ်ပေါက်သော အကြီးအမှူးကိုလည်း ပြုရမည်)
- (ninnānākaraṇaṃ, vibhajanā natthi. Ārammaṇasadisā) = (ကွဲပြားချက် မရှိ၊ ခွဲခြမ်းစိတ်ဖြာခြင်း မရှိ။ အာရုံဟူသော အကြောင်းနှင့် တူကြသည်)
- (Saṃkhittaṃ. Evaṃ nava pañhā kātabbā. Tīsuyeva padesu parivattetabbā, nānākkhaṇikā natthi.) = (အကျဉ်းချုပ်။ ဤသို့ ပြဿနာ ကိုးခုကို ပြုရမည်။ ပုဒ် သုံးခု၌သာ လှည့်ပြောင်းရမည်၊ ခဏ ကွဲပြားသည့် ကံ မရှိ။)
- (yāva asaññasattā, mahābhūtā) = (အသညသတ်တို့အထိ၊ မူလဓာတ်ကြီးများ)
- (arūpe sīlabbataparāmāso natthi, evaṃ nava pañhā kātabbā) = (ရုပ်မရှိသော ဘုံ၌ သီလ အကျင့်ဝတ်ဆိုင်ရာ မှားယွင်းသော ယူဆမှု မရှိ၊ ဤသို့ ပြဿနာ ကိုးခုကို ပြုရမည်)
- (Nissayavāro paccayavārasadisova. Saṃsaṭṭhavāropi sampayuttavāropi nava pañhā kātabbā, rūpaṃ natthi.) = (အမှီပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်သည် အကြောင်းပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူသည်ပင်။ ရောနှောခြင်းအလိုက် ဖော်ပြချက်လည်း၊ ယှဉ်တွဲခြင်းအလိုက် ဖော်ပြချက်လည်း ပြဿနာ ကိုးခုကို ပြုရမည်၊ ရုပ် မရှိ။)
- (dve āvajjanā kātabbā, paṭhamo natthi) = (စိတ်ညွတ်ခြင်း နှစ်ခုကို ပြုရမည်၊ ပထမ ပြဿနာ မရှိ)
- (ekampi vuṭṭhānaṃ kātabbaṃ, majjhe) = (ထမြောက်ခြင်း စိတ် တစ်ခုကိုလည်း ပြုရမည်၊ အလယ်၌)
- (napurejāte vibhajantena arūpaṃ paṭhamaṃ kātabbaṃ, rūpaṃ yattha labbhati pacchā kātabbaṃ, paṭighañca arūpe natthi) = (ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်းဟူသော အကြောင်း မဟုတ်ခြင်း၌ ခွဲခြမ်းစိတ်ဖြာလျက် ရုပ် မဟုတ်သော သဘောတရားကို ပထမ ပြုရမည်၊ ရုပ်ကို တွေ့ရသည့် နေရာ၌ နောက်မှ ပြုရမည်၊ ရုပ်မရှိသော ဘုံ၌ မုန်းတီးမှုလည်း မရှိ)
- (Sahajātavāropi evaṃ kātabbo.) = (အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်ကိုလည်း ဤသို့ ပြုရမည်။)
- (Tīsupi mūlā pucchitabbā) = (သုံးခုလုံး၌ အခြေခံတို့ကို မေးရမည်)
- (tīṇi upanissayā) = (အားကြီးသော အမှီ သုံးခု)
- (anulomamātikā vitthāretabbā) = (အဟုတ်ပြ ပုံစံ၏ ခေါင်းစဉ်စာရင်းကို အကျယ် ချဲ့ရမည်)
- (Paṭiccavārampi sahajātavārampi paccayavārampi nissayavārampi saṃsaṭṭhavārampi sampayuttavārampi ganthadukasadisaṃ ninnānākaraṇaṃ.) = (မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်လည်း၊ အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း၊ အကြောင်းပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်လည်း၊ အမှီပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်လည်း၊ ရောနှောခြင်းအလိုက် ဖော်ပြချက်လည်း၊ ယှဉ်တွဲခြင်းအလိုက် ဖော်ပြချက်လည်း ကွဲပြားချက် မရှိ အထုံး နှစ်မျိုးတွဲနှင့် တူသည်။)
- (evaṃ nava pañhā vitthāretabbā) = (ဤသို့ ပြဿနာ ကိုးခုကို အကျယ် ချဲ့ရမည်)
- (evaṃ itarepi tīṇi vitthāretabbā) = (ဤသို့ အခြား သုံးခုကိုလည်း အကျယ် ချဲ့ရမည်)
- (Ārabbha kātabbā. Imasmiṃ duke lokuttaraṃ natthi, ganthadukasadisaṃ, ninnānākaraṇaṃ. "Ganthaniya"nti niyāmetabbaṃ, magge nava pañhā kātabbā.) = (အာရုံပြု၍ဟု ပြုရမည်။ ဤ နှစ်မျိုးတွဲ၌ လောကကို ကျော်လွန်သော သဘောတရား မရှိ၊ အထုံး နှစ်မျိုးတွဲနှင့် တူသည်၊ ကွဲပြားချက် မရှိ။ “အထုံး၏ အာရုံ ဖြစ်နိုင်သည်”ဟု သတ်မှတ်ရမည်၊ မဂ်ဟူသော အကြောင်း၌ ပြဿနာ ကိုးခုကို ပြုရမည်။)
- (Idha nahetupaccayo natthi) = (ဤနေရာ၌ အမြစ်ဟူသော အကြောင်း မဟုတ်ခြင်း မရှိ)
- (Evaṃ itare dve gaṇanāpi sahajātavāropi paccayavāropi nissayavāropi saṃsaṭṭhavāropi sampayuttavāropi paṭiccavārasadisā.) = (ဤသို့ အခြား ရေတွက်ချက် နှစ်ခုလည်း၊ အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း၊ အကြောင်းပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်လည်း၊ အမှီပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်လည်း၊ ရောနှောခြင်းအလိုက် ဖော်ပြချက်လည်း၊ ယှဉ်တွဲခြင်းအလိုက် ဖော်ပြချက်လည်း မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူကြသည်။)
- (Evaṃ itarepi tīṇi pañhā kātabbā ārammaṇasadisaṃyeva. Adhipatiyāpi anantarepi upanissayepi vibhāgo natthi.) = (ဤသို့ အခြား ပြဿနာ သုံးခုကိုလည်း အာရုံဟူသော အကြောင်းနှင့် တူအောင်ပင် ပြုရမည်။ အကြီးအမှူးဟူသော အကြောင်း၌လည်း၊ ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းဟူသော အကြောင်း၌လည်း၊ အားကြီးသော အမှီဟူသော အကြောင်း၌လည်း ခွဲခြားချက် မရှိ။)
- (Arūpaṃyeva paccayaṃ, ekekassa tīṇi tīṇi kātabbā. Ārammaṇañca sahajātañca upanissayañca navasupi parivattetabbaṃ. Evaṃ pañhāvārepi sabbaṃ kātabbaṃ.) = (ရုပ် မဟုတ်သော သဘောတရားကိုသာ အကြောင်းအဖြစ်၊ တစ်ခုစီ၏ သုံးခု သုံးခုစီကို ပြုရမည်။ အာရုံဟူသော အကြောင်းကိုလည်းကောင်း၊ အတူ ပေါ်ပေါက်ခြင်းဟူသော အကြောင်းကိုလည်းကောင်း၊ အားကြီးသော အမှီဟူသော အကြောင်းကိုလည်းကောင်း ကိုးခုလုံး၌ လှည့်ပြောင်းရမည်။ ဤသို့ ပြဿနာအလိုက် ဖော်ပြချက်၌လည်း အားလုံးကို ပြုရမည်။)
- (Mūlaṃ, tīṇipi upanissayā) = (အခြေခံ၊ အားကြီးသော အမှီ သုံးခုလုံး)
- (dvepi gocchakā āsavagocchakasadisā ninnānākaraṇā) = (အစု နှစ်ခုလုံးသည် ကွဲပြားချက် မရှိ စိတ်အစွန်းအထင်းတို့၏ အစုနှင့် တူကြသည်)

## Unsure Pāli
- «Āsavañceva āsavasampayuttaṃ dhammaṃ paṭicca» (3-03, āsavaāsavasampayutta dyad, naadhipati line): the second term
  lacks its «-ñca»; read as «āsavasampayuttañca» (both terms, as the other lines of the dyad). Logged as a slip.
- «(dve āvajjanā kātabbā, paṭhamo natthi)» (3-05): «paṭhamo» read as «paṭhamo pañho» (masculine; the noun supplied:
  «ပထမ ပြဿနာ မရှိ»; H8 kind).
- «Arūpaṃyeva paccayaṃ, ekekassa tīṇi tīṇi kātabbā» (3-05): rendered «ရုပ် မဟုတ်သော သဘောတရားကိုသာ အကြောင်းအဖြစ်၊
  တစ်ခုစီ၏ သုံးခု သုံးခုစီကို ပြုရမည်» (only the immaterial as the conditioning; three for each).
- «(yattha yattha vatthu labbhati, tattha tattha ninnetabbaṃ)»: ninnetabbaṃ read as «to be brought in» «ထည့်သွင်းရမည်».
- «Āvajjanāpi vuṭṭhānampi evaṃ samuddiṭṭhaṃ saṃkhittaṃ»: «… ဤသို့ အကျဉ်းချုပ်၍ ဖော်ပြထားသည်».
- «vippayuttakā cetanā» (3-03 vippayutta-sāsava dyad, «āsavavippayutte khandhe paṭicca vippayuttakā cetanā»): as written
  «ကင်းကွာသော စေ့ဆော်မှု».
- «ārabbha kātabbā / ārabbhayeva kātabbā» read as «to be done with (the word) ārabbha»: «အာရုံပြု၍ဟု (သာ) ပြုရမည်».

## Source slips (translated as written; read in memory only where a frame needed it; logged by the generator)
- 3-03 «(yāva āsaññasattā)» read as «(yāva asaññasattā)» (Burmese «အသညသတ်တို့အထိ»).
- 3-03 «Āsavañceva āsavasampayuttaṃ dhammaṃ paṭicca» read as «… āsavasampayuttañca …» (above).
- 3-04 «saññojanasampayutte ceva no ca saññojane khandhe paṭicca saññojanā (2)»: no final «.»; read with it in memory
  and no «။» written (as the Pāli).
- Notes without a «,» inside lists, as the Pāli: «kāmāsavaṃ paṭicca diṭṭhāsavo avijjāsavo (cakkaṃ bandhitabbaṃ)
  bhavāsavaṃ paṭicca …» (3-03, one fragment, no «၊» added).

## For the consistency pass (harmonise)
- The vipp-S pair («X-vippayutto S-o» «…နှင့် ကင်းကွာသော်လည်း …» / «… ကင်းကွာ၊ … မဖြစ်နိုင်သော») follows 3-01's nahetu
  sahetuka pattern; align with whatever the pass decides for it.
- «ninnānākaraṇaṃ» without a Pāli comma after the verb («yathā cūḷantaraduke lokiyadukaṃ evaṃ kātabbaṃ
  ninnānākaraṇaṃ»): «… ကဲ့သို့ ထိုနည်းတူ ကွဲပြားချက် မရှိ ပြုရမည်» (no «၊» added; 3-01 «iminā kāraṇena … ninnānākaraṇaṃ»
  pattern); with a comma (3-01 «…, ninnānākaraṇaṃ») «…၊ ကွဲပြားချက် မရှိ».
- «garukārammaṇā» «လေးစားဖွယ်ရာ အာရုံ» (garuṃ katvā «လေးစားဖွယ်ရာ ပြု၍»); «-kātabbā» «…အဖြစ် ပြုရမည်».
- «(evaṃ gaṇetabbaṃ)» lineage «ဤသို့» used throughout (H14).
- «purimā purimā §T§ā khandhā pacchimānaṃ…» (3-04, cut by «…»): «… နောက်နောက်…» (the pair's Burmese; reuse test).
- «X-ā hetū» = «X ဖြစ်သော အမြစ်» in every dyad (also where X is not a dyad term).
