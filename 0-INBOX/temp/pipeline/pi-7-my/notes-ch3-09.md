# pi-7 3-09 mahantaraduka: Burmese zero-shot notes

PROGRESS: DONE (2026-11-24). Written to AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters/3-09-mahantaraduka.md
(1159 segments, 1867 lines). Checks: check_chapter_ids OK; check_marks OK; check_text (pi-3-mr/check_text.py on a
«…Pe…»-folded copy in pi-7-my/chk-pe/ch3-09/, deleted afterwards; check_text_pe7.py not run on the shared chk-pe/) OK,
dashes match; check_ch3-09.py 0 mismatches (S/P/C/O/N on 1867 lines, I 3259 sentences, T 99), reuse 81 / 81 terms +
855 / 855 sentences, identity with 1-01, 1-03 … 1-05, 2-03 … 2-06, 3-01 … 3-06 80 / 80, --sample identical, --mutate
11 / 11; make_ch3-09.py --regress: the sample (1-00, 1-02), 2-03 … 2-06, 3-01 … 3-02 and 3-03 … 3-06 regenerate
identical through this engine.

## Files
- make_ch3-09.py: generator. IMPORTS make_ch3-03-06.py (which imports make_ch3-01-02.py, which imports
  make_ch2-03-06.py: PRIMARY my7_formulas + make_sample + make_ch1-01, FALLBACK make_ch1-03-05) with its dyad
  machinery; no main() of another group runs, nothing of another group is written. `--dev` (chk-ch3-09/dev.txt;
  `--stub` gives unknown notes a placeholder, development only), `--regress`, `--slips`, `--pieces`, `--out DIR`.
- check_ch3-09.py: checker (adapted from check_ch3-03-06.py; own copy of the 14 dyads' Burmese, names and Pāli
  term regexes; the active dyad of a line from the Pāli dyad headings); `--sample --pe --mutate --groups`.
- chk-ch3-09/: my scratch (dev output, query scripts).

## How the dyads are run
- The chapter is cut at its 14 dyad headings (make_ch3-01-02's parts_of); only that dyad is active.
- Dyad terms read from the pi-1 FINAL Mātikā ^1-M2-55 … ^1-M2-68 with W() (list below). Mahantaradukaṃ = pi-1
  heading «ကြားညှပ် နှစ်မျိုးတွဲ အစုကြီး» (^1-M-2-10-0; 3-02 Cūḷantara «… အစုငယ်»).
- Non a-stem terms are read as pseudo a-stems before slotting: cittasahabhū (u-stem), cittānuparivattī (i-stem), the
  two long -sahabhū / -ānuparivattī terms, upādā (indeclinable). Where the ending does not show case / number (-ū,
  -uno, -u, -ī, -ino, -i, upādā) the ending of the next noun is taken (stem cut off first, number words skipped); such
  a term with its own «ca» before an -aṃ / -ānaṃ noun takes «-ñca» («upādā ca noupādā ca cittasamuṭṭhānaṃ rūpaṃ» =
  both members on one noun «A၊ B N», make_ch3-01-02's both-members slot).
- «citta» is a dyad term only before a dhamma word (or coordinated with «nocitta» before one); otherwise the noun
  «စိတ်» (as 3-01 reads hetu). «nocitta» is always the term. citta (noun) is a neuter noun (-aṃ subject or object).
- «cittasampayuttaka» = the term cittasampayutta (as 3-03-06's X-sampayuttaka); the same Burmese as a qualifier
  elsewhere. «X-o kabaḷīkāro āhāro» (a term before the fixed noun) is read as one noun (same Burmese
  «လုတ်ပြု၍ စားရသော အာဟာရ»).
- One «ca» after the last member is read on every member (as make_ch3-01-02's _CA_AFTER): «T-ā khandhā kabaḷīkāro
  āhāro ca», «X-ānaṃ khandhānaṃ cittassa ca»; «cittaṃ sampayuttakā (ca) khandhā (ca)» = «cittañca sampayuttakā
  khandhā ca».
- A piece cut short before «…» without its link («…, dve khandhe ca…», «kāyāyatanaṃ ca…») takes the line's link
  («ကိုလည်းကောင်း» after paṭicca, «ကြောင့်လည်းကောင်း» after paccayā, «နှင့်လည်းကောင်း» after saṃsaṭṭha), as the module renders
  the fragment «dve khandhe ca…». This piece rule and the «X-viññāṇasahagata» qualifiers act only while 3-09 runs:
  with the qualifiers global, make_ch3-01-02 would read 3-02 line 565 otherwise than published (see Harmonise).
- Notes: whole notes (raw Pāli) as placeholders «(⁑d<i>)» (as 3-01-02's NOTEP), all listed below. A note the Pāli
  does not close (Pāli line 2977 «… (saṃkhittaṃ, yathā nikkhittapadāni vitthāretabbāni. (2)») is read with its «)»
  and the «)» removed again afterwards (no «)» written, «။» kept).
- Coordinator decisions applied: «Anulomaṃ.» (the order) «အဟုတ်ပြ ပုံစံ။» (13 lines), «(anulomaṃ)» / «(paccanīyaṃ)»
  (the orders) «(အဟုတ်ပြ ပုံစံ)» / «(အငြင်းပြ ပုံစံ)»; «anulomaṃ gotrabhussa» (the mind moment) «လျော်ညီခြင်း စိတ်» (4);
  «Sahajātā –» bare «အတူ ပေါ်ပေါက်ခြင်း –», in the kamma section «အတူ ပေါ်ပေါက်သည့် ကံ –» (18, also «Tīṇipi
  sahajātā, nānākkhaṇikā» in a kamma note); asaññasattānaṃ «အသညသတ်တို့၏» (26 / 26); no heinous deeds in 3-09.
- Supplied words (H8): «(yāva utusamuṭṭhānaṃ)» «ရာသီဥတုမှ ဖြစ်ပေါ်လာသော ရုပ်အထိ» (rūpa supplied: the adjective
  alone); «paṭhamasseva rūpajīvitindriyaṃ» «ပထမ ပြဿနာ၌သာ» (pañhā supplied, as 3-05 «paṭhamo natthi»).

## Dyad terms (pi-1 final, W())
sārammaṇa = အာရုံ ရှိသော; anārammaṇa = အာရုံ မရှိသော (^1-M2-55)
citta = စိတ် ဖြစ်သော; no citta = စိတ် မဟုတ်သော (^1-M2-56)
cetasika = စိတ်၏ အဖော် ဖြစ်သော; acetasika = စိတ်၏ အဖော် မဟုတ်သော (^1-M2-57)
cittasampayutta = စိတ်နှင့် ယှဉ်တွဲသော; cittavippayutta = စိတ်နှင့် ကင်းကွာသော (^1-M2-58)
cittasaṃsaṭṭha = စိတ်နှင့် ရောနှောသော; cittavisaṃsaṭṭha = စိတ်နှင့် မရောနှောသော (^1-M2-59)
cittasamuṭṭhāna = စိတ်မှ ဖြစ်ပေါ်လာသော; no cittasamuṭṭhāna = စိတ်မှ ဖြစ်ပေါ်လာသည် မဟုတ်သော (^1-M2-60)
cittasahabhū = စိတ်နှင့်အတူ တည်ရှိသော; no cittasahabhū = စိတ်နှင့်အတူ တည်ရှိသည် မဟုတ်သော (^1-M2-61)
cittānuparivattī = စိတ်နောက်သို့ လိုက်ပါသော; no cittānuparivattī = စိတ်နောက်သို့ လိုက်ပါသည် မဟုတ်သော (^1-M2-62)
cittasaṃsaṭṭhasamuṭṭhāna = စိတ်နှင့် ရောနှော၍ စိတ်မှ ဖြစ်ပေါ်လာသော; no … = … ဖြစ်ပေါ်လာသည် မဟုတ်သော (^1-M2-63)
cittasaṃsaṭṭhasamuṭṭhānasahabhū = စိတ်နှင့် ရောနှော၍ စိတ်မှ ဖြစ်ပေါ်လာပြီး စိတ်နှင့်အတူ တည်ရှိသော; no … = … တည်ရှိသည် မဟုတ်သော (^1-M2-64)
cittasaṃsaṭṭhasamuṭṭhānānuparivattī = စိတ်နှင့် ရောနှော၍ စိတ်မှ ဖြစ်ပေါ်လာပြီး စိတ်နောက်သို့ လိုက်ပါသော; no … = … လိုက်ပါသည် မဟုတ်သော (^1-M2-65)
ajjhattika = အတွင်းပိုင်း; bāhira = ပြင်ပ (^1-M2-66)
upādā = မူလဓာတ်ကြီးများကို မှီ၍ ဖြစ်သော; no upādā = မူလဓာတ်ကြီးများကို မှီ၍ ဖြစ်သည် မဟုတ်သော (^1-M2-67)
upādinna (pi-1 upādiṇṇa) = ကံကြောင့် ဖြစ်သော; anupādinna = ကံကြောင့် မဖြစ်သော (^1-M2-68)
(the term «X-ā / -assa / -acittasamaṅgissa» … keeps this Burmese; «X-asamaṅgissa» «X သဘောတရားနှင့် ပြည့်စုံသူ၏» NEW,
as the module's «-acittasamaṅgissa» «X စိတ်နှင့် ပြည့်စုံသူ၏»)

## Nouns and lexicon (reused; read with W() or from the module)
- citta (noun) = စိတ် (module LEX cittaṃ); kabaḷīkāro āhāro = လုတ်ပြု၍ စားရသော အာဟာရ (module).
- upekkhindriya = ဥပေက္ခာ၏ စွမ်းရည် (pi-6); sukhindriya = သာယာမှု၏ စွမ်းရည်, dukkhindriya = နာကျင်မှု၏ စွမ်းရည် (pi-2).
- X-viññāṇasahagata (all forms) = «X သိစိတ်နှင့်အတူ ဖြစ်သော» (3-01-02's -sahagataṃ / -sahagatānaṃ).
- X-sampadā = «X ပြည့်စုံခြင်း» (as make_ch2-12-17; pi-4 sīlasampadā).
- ahetuke (before a term) = အမြစ် မရှိသော (the fallback 1-03-05's qualifier, also in the primary).
- naadhipatiyā (cut by «…», no count) = အကြီးအမှူးဟူသော အကြောင်း မဟုတ်ခြင်း၌; pubbe samudāciṇṇe (cut) = ရှေးက ဖြစ်ခဲ့ဖူးသော.
- the asyndetic lists of the kinds of matter without «…» («bāhiraṃ āhārasamuṭṭhānaṃ utusamuṭṭhānaṃ asaññasattānaṃ»)
  = «ပြင်ပ၊ အာဟာရမှ ဖြစ်ပေါ်လာသော၊ ရာသီဥတုမှ ဖြစ်ပေါ်လာသော၊ အသညသတ်တို့၏» (with «…» the module's «ပြင်ပ… …»).
- *Pacchājātāsevanapaccayā* = the module's «X-Ypaccayā» heading (as 3-01-02's *Vipākāhārapaccayā*).

## New strings (Pāli = Burmese), one per line (names, words, whole notes, fragments)
Sārammaṇadukaṃ = အာရုံ ရှိခြင်း နှစ်မျိုးတွဲ
Cittadukaṃ = စိတ် ဖြစ်ခြင်း နှစ်မျိုးတွဲ
Cetasikadukaṃ = စိတ်၏ အဖော် ဖြစ်ခြင်း နှစ်မျိုးတွဲ
Cittasampayuttadukaṃ = စိတ်နှင့် ယှဉ်တွဲခြင်း နှစ်မျိုးတွဲ
Cittasaṃsaṭṭhadukaṃ = စိတ်နှင့် ရောနှောခြင်း နှစ်မျိုးတွဲ
Cittasamuṭṭhānadukaṃ = စိတ်မှ ဖြစ်ပေါ်လာခြင်း နှစ်မျိုးတွဲ
Cittasahabhūdukaṃ = စိတ်နှင့်အတူ တည်ရှိခြင်း နှစ်မျိုးတွဲ
Cittānuparivattidukaṃ = စိတ်နောက်သို့ လိုက်ပါခြင်း နှစ်မျိုးတွဲ
Cittasaṃsaṭṭhasamuṭṭhānadukaṃ = စိတ်နှင့် ရောနှော၍ စိတ်မှ ဖြစ်ပေါ်လာခြင်း နှစ်မျိုးတွဲ
Cittasaṃsaṭṭhasamuṭṭhānasahabhūdukaṃ = စိတ်နှင့် ရောနှော၍ စိတ်မှ ဖြစ်ပေါ်လာပြီး စိတ်နှင့်အတူ တည်ရှိခြင်း နှစ်မျိုးတွဲ
Cittasaṃsaṭṭhasamuṭṭhānānuparivattidukaṃ = စိတ်နှင့် ရောနှော၍ စိတ်မှ ဖြစ်ပေါ်လာပြီး စိတ်နောက်သို့ လိုက်ပါခြင်း နှစ်မျိုးတွဲ
Ajjhattikadukaṃ = အတွင်းပိုင်း ဖြစ်ခြင်း နှစ်မျိုးတွဲ
Upādādukaṃ = မူလဓာတ်ကြီးများကို မှီ၍ ဖြစ်ခြင်း နှစ်မျိုးတွဲ
Upādinnadukaṃ = ကံကြောင့် ဖြစ်ခြင်း နှစ်မျိုးတွဲ
vaṇṇasampadā = အဆင်းအရောင် ပြည့်စုံခြင်း
saddasampadā = အသံ ပြည့်စုံခြင်း
gandhasampadā = အနံ့ ပြည့်စုံခြင်း
rasasampadā = အရသာ ပြည့်စုံခြင်း
phoṭṭhabbasampadā = အထိအတွေ့ ပြည့်စုံခြင်း
cakkhusampadā = မျက်စိ ပြည့်စုံခြင်း
sotasampadā = နား ပြည့်စုံခြင်း
ghānasampadā = နှာခေါင်း ပြည့်စုံခြင်း
jivhāsampadā = လျှာ ပြည့်စုံခြင်း
kāyasampadā = ကိုယ် ပြည့်စုံခြင်း
yathā nikkhittapadāni = ချထားသော ပုဒ်များအတိုင်း
pūretukāmena = ပြည့်စုံစေလိုသူသည်
pūretvā / pūritvā = ပြည့်စုံစေ၍
purimagamanaṃ = ရှေး သွားပုံ
tīṇiyeva moho = မောဟနှင့် သုံးခုသာ
tīsuyeva moho = သုံးခု၌သာ မောဟ
mūlapade = အခြေခံ ပုဒ်၌
pavesetvā = ထည့်သွင်း၍
ante = အဆုံး၌
labbhati = တွေ့ရသည်
sabbaṭṭhāne = နေရာ အားလုံး၌
paṭhamaghaṭanānayena = ပထမ ပေါင်းစပ်ချက်၏ နည်းအတိုင်း
ekamūlānaṃ = တစ်ခုကို အခြေခံသည်တို့၏
(Evaṃ itare dve gaṇanāpi sampayuttavārāpi kātabbā.) = (ဤသို့ အခြား ရေတွက်ချက် နှစ်ခုကိုလည်း၊ ယှဉ်တွဲခြင်းအလိုက် ဖော်ပြချက်ကိုလည်း ပြုရမည်။)
(Evaṃ itare dve gaṇanāpi sampayuttavāropi sabbe kātabbā.) = (ဤသို့ အခြား ရေတွက်ချက် နှစ်ခုကိုလည်း၊ ယှဉ်တွဲခြင်းအလိုက် ဖော်ပြချက်ကိုလည်း အားလုံး ပြုရမည်။)
(paṭhamagamanasadisaṃ ninnānākaraṇaṃ, imaṃ nānaṃ) = (ပထမ သွားပုံနှင့် တူသည် ကွဲပြားချက် မရှိ၊ ဤသည် ကွဲပြားချက် ဖြစ်သည်)
(dvepi gamanā paṭhamagamanasadisaṃ ninnānākaraṇaṃ. Ārammaṇādhipati sahajātādhipati kātabbā) = (သွားပုံ နှစ်ခုလုံးသည် ပထမ သွားပုံနှင့် တူသည် ကွဲပြားချက် မရှိ။ အာရုံ အကြီးအမှူး၊ အတူ ပေါ်ပေါက်သော အကြီးအမှူးကို ပြုရမည်)
(tīṇipi garukārammaṇā kātabbā, ārammaṇādhipatiyeva) = (သုံးခုလုံးကို လေးစားဖွယ်ရာ အာရုံအဖြစ် ပြုရမည်၊ အာရုံ အကြီးအမှူးသာ)
(ime dve pūretukāmena kātabbā, purimagamanasadisaṃ) = (ဤ နှစ်ခုကို ပြည့်စုံစေလိုသူသည် ပြုရမည်၊ ရှေး သွားပုံနှင့် တူသည်)
(ime dvepi pūretukāmena sabbattha kātabbā, paṭhamagamanasadisaṃ ninnānākaraṇaṃ) = (ဤ နှစ်ခုလုံးကို ပြည့်စုံစေလိုသူသည် နေရာတိုင်း၌ ပြုရမည်၊ ပထမ သွားပုံနှင့် တူသည် ကွဲပြားချက် မရှိ)
(paṭisandhikkhaṇepi dve) = (ပဋိသန္ဓေ နေသော ခဏ၌လည်း နှစ်ခု)
(paṭisandhikkhaṇe dvepi kātabbā, saṃkhittaṃ) = (ပဋိသန္ဓေ နေသော ခဏ၌ နှစ်ခုလုံးကို ပြုရမည်၊ အကျဉ်းချုပ်)
(paṭisandhikkhaṇe dvepi kātabbā) = (ပဋိသန္ဓေ နေသော ခဏ၌ နှစ်ခုလုံးကို ပြုရမည်)
(paṭisandhikkhaṇe tīṇipi kātabbā) = (ပဋိသန္ဓေ နေသော ခဏ၌ သုံးခုလုံးကို ပြုရမည်)
(paṭisandhikkhaṇe ekaṃ) = (ပဋိသန္ဓေ နေသော ခဏ၌ တစ်ခု)
(paṭisandhikkhaṇe dve) = (ပဋိသန္ဓေ နေသော ခဏ၌ နှစ်ခု)
(paṭisandhikkhaṇe ekaṃ, saṃkhittaṃ) = (ပဋိသန္ဓေ နေသော ခဏ၌ တစ်ခု၊ အကျဉ်းချုပ်)
(Nava pañhā pañcaviññāṇampi yathā ārammaṇapaccayā evaṃ kātabbaṃ, tīsuyeva moho. Sabbe pañhā pavattipaṭisandhiyā kātabbā asammohantena.) = (ပြဿနာ ကိုးခု၊ သိစိတ် ငါးပါးကိုလည်း အာရုံဟူသော အကြောင်းကဲ့သို့ ထိုနည်းတူ ပြုရမည်၊ သုံးခု၌သာ မောဟ။ ပြဿနာ အားလုံးကို ဘဝ ဖြစ်စဉ်၌လည်း၊ ပဋိသန္ဓေ၌လည်း မရောထွေးစေဘဲ ပြုရမည်။)
(evaṃ pañcapi pañhā kātabbā, tīṇiyeva moho. Saṃkhittaṃ) = (ဤသို့ ပြဿနာ ငါးခုလုံးကို ပြုရမည်၊ မောဟနှင့် သုံးခုသာ။ အကျဉ်းချုပ်)
(Evaṃ itare dve gaṇanāpi sampayuttavāropi kātabbo.) = (ဤသို့ အခြား ရေတွက်ချက် နှစ်ခုကိုလည်း၊ ယှဉ်တွဲခြင်းအလိုက် ဖော်ပြချက်ကိုလည်း ပြုရမည်။)
(paṭhamagamanasadisaṃ) = (ပထမ သွားပုံနှင့် တူသည်)
(paṭhamagamanaṃ) = (ပထမ သွားပုံ)
(ārammaṇādhipatiyeva) = (အာရုံ အကြီးအမှူးသာ)
(evaṃ tīṇi kātabbāni, paṭhamagamanasadisaṃ. Pūritvā kātabbaṃ, ninnānākaraṇaṃ) = (ဤသို့ သုံးခုကို ပြုရမည်၊ ပထမ သွားပုံနှင့် တူသည်။ ပြည့်စုံစေ၍ ပြုရမည်၊ ကွဲပြားချက် မရှိ)
(Mūlaṃ pucchitabbaṃ, tīṇi upanissayā) = (အခြေခံကို မေးရမည်၊ အားကြီးသော အမှီ သုံးခု)
(tīṇi, paṭhamagamanasadisaṃ ninnānākaraṇaṃ) = (သုံးခု၊ ပထမ သွားပုံနှင့် တူသည် ကွဲပြားချက် မရှိ)
(purejātasadisaṃ ninnānākaraṇaṃ) = (ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်းဟူသော အကြောင်းနှင့် တူသည် ကွဲပြားချက် မရှိ)
(purejātasadisaṃ ninnānaṃ) = (ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်းဟူသော အကြောင်းနှင့် တူသည် ကွဲပြားမှု မရှိ)
(paṭisandhikkhaṇe) = (ပဋိသန္ဓေ နေသော ခဏ၌)
(paṭisandhiyā dve kātabbā) = (ပဋိသန္ဓေ၌ နှစ်ခုကို ပြုရမည်)
(Evaṃ navapi pañhā kātabbā. Ahetukanti sabbattha niyāmetabbaṃ, ekaṃyeva mohaṃ mūlapade.) = (ဤသို့ ပြဿနာ ကိုးခုလုံးကို ပြုရမည်။ အမြစ် မရှိသည်ဟု နေရာတိုင်း၌ သတ်မှတ်ရမည်၊ အခြေခံ ပုဒ်၌ မောဟ တစ်ခုတည်းကိုသာ။)
(Evaṃ dve pañhā pavattipaṭisandhi kātabbā. Saṃkhittaṃ.) = (ဤသို့ ပြဿနာ နှစ်ခုကို ဘဝ ဖြစ်စဉ်၌လည်း၊ ပဋိသန္ဓေ၌လည်း ပြုရမည်။ အကျဉ်းချုပ်။)
(paṭiccasadisā, pañhāghaṭanā natthi) = (မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူကြသည်၊ ပြဿနာ ပေါင်းစပ်ချက် မရှိ)
(paccayavārasadisā, pañhāghaṭanā natthi) = (အကြောင်းပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူကြသည်၊ ပြဿနာ ပေါင်းစပ်ချက် မရှိ)
(Cittasaṃsaṭṭhadukaṃ yathā cittasampayuttadukaṃ evaṃ kātabbaṃ, ninnānākaraṇaṃ.) = (စိတ်နှင့် ရောနှောခြင်း နှစ်မျိုးတွဲကို စိတ်နှင့် ယှဉ်တွဲခြင်း နှစ်မျိုးတွဲကဲ့သို့ ထိုနည်းတူ ပြုရမည်၊ ကွဲပြားချက် မရှိ။)
(yāva asaññasattā kātabbā) = (အသညသတ်တို့အထိ ပြုရမည်)
(paṭisandhikkhaṇe dvepi paṭiccavārasadisā) = (ပဋိသန္ဓေ နေသော ခဏ၌ နှစ်ခုလုံးသည် မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူကြသည်)
(paṭisandhikkhaṇe tīṇipi kātabbā paṭiccavārasadisā) = (ပဋိသန္ဓေ နေသော ခဏ၌ သုံးခုလုံးကို မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူအောင် ပြုရမည်)
(paṭisandhikkhaṇe dvepi kātabbā paṭiccavārasadisā) = (ပဋိသန္ဓေ နေသော ခဏ၌ နှစ်ခုလုံးကို မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူအောင် ပြုရမည်)
(paṭisandhikkhaṇe dvepi) = (ပဋိသန္ဓေ နေသော ခဏ၌ နှစ်ခုလုံး)
(Sabbe navapi pañhā kātabbā, paṭiccavārasadisā. Pañcaviññāṇampi kātabbaṃ. Tīṇiyeva moho.) = (ပြဿနာ ကိုးခုလုံး အားလုံးကို ပြုရမည်၊ မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူကြသည်။ သိစိတ် ငါးပါးကိုလည်း ပြုရမည်။ မောဟနှင့် သုံးခုသာ။)
(Evaṃ itare dve gaṇanāpi nissayavāropi kātabbo.) = (ဤသို့ အခြား ရေတွက်ချက် နှစ်ခုကိုလည်း၊ အမှီပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်ကိုလည်း ပြုရမည်။)
(pañca pañhā kātabbā. Tīṇi. Moho) = (ပြဿနာ ငါးခုကို ပြုရမည်။ သုံးခု။ မောဟ)
(tīṇipi ārammaṇādhipati, sahajātādhipatipi kātabbā) = (သုံးခုလုံး၌ အာရုံ အကြီးအမှူး၊ အတူ ပေါ်ပေါက်သော အကြီးအမှူးကိုလည်း ပြုရမည်)
(vuṭṭhānaṃ natthi) = (ထမြောက်ခြင်း စိတ် မရှိ)
(itare dve gaṇanā, imassa sadisāyeva kātabbā) = (အခြား ရေတွက်ချက် နှစ်ခု၊ ဤသည်နှင့် တူအောင်ပင် ပြုရမည်)
(tīṇi kātabbā, vuṭṭhānaṃ natthi) = (သုံးခုကို ပြုရမည်၊ ထမြောက်ခြင်း စိတ် မရှိ)
(iminākāreneva pacchājāto vitthāretabbo) = (ဤ ပုံစံအတိုင်းပင် နောက်မှ ဖြစ်ပေါ်ခြင်းဟူသော အကြောင်းကို အကျယ် ချဲ့ရမည်)
(paccayavārasadisaṃ paṭisandhipi pavattipi kātabbā sabbesampi pañhānaṃ.) = (အကြောင်းပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူသည် ပြဿနာ အားလုံး၏ ပဋိသန္ဓေကိုလည်း၊ ဘဝ ဖြစ်စဉ်ကိုလည်း ပြုရမည်။)
(anulomagaṇanā kātabbā) = (အဟုတ်ပြ ပုံစံ၏ ရေတွက်ချက်ကို ပြုရမည်)
(arūpaṃ sabbaṃ uddharitabbaṃ. Cittasamuṭṭhānadukasadisaṃ.) = (ရုပ် မဟုတ်သော သဘောတရားကို အားလုံး ထုတ်နုတ်ရမည်။ စိတ်မှ ဖြစ်ပေါ်လာခြင်း နှစ်မျိုးတွဲနှင့် တူသည်။)
(mahābhūtā chasupi pañhesu kātabbā, adhipatiyā tīsu natthi.) = (မူလဓာတ်ကြီးတို့ကို ပြဿနာ ခြောက်ခုလုံး၌ ပြုရမည်၊ အကြီးအမှူးဟူသော အကြောင်း၌ သုံးခု၌ မရှိ။)
(Evaṃ navapi pañhā kātabbā. "Ahetuka"nti niyāmetabbaṃ. Yathā anulome labbhati evaṃ kātabbaṃ. Tīṇi moho yathā cittasamuṭṭhānaduke evameva kātabbā.) = (ဤသို့ ပြဿနာ ကိုးခုလုံးကို ပြုရမည်။ “အမြစ် မရှိသည်”ဟု သတ်မှတ်ရမည်။ အဟုတ်ပြ ပုံစံ၌ တွေ့ရသည့်အတိုင်း ပြုရမည်။ သုံးခု မောဟကို စိတ်မှ ဖြစ်ပေါ်လာခြင်း နှစ်မျိုးတွဲ၌ကဲ့သို့ ထိုနည်းတူပင် ပြုရမည်။)
(evaṃ itare dvepi gaṇanā kātabbā) = (ဤသို့ အခြား ရေတွက်ချက် နှစ်ခုလုံးကို ပြုရမည်)
(paṭiccavārasadisaṃ, sabbe mahābhūtā) = (မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူသည်၊ မူလဓာတ်ကြီး အားလုံး)
(sabbe mahābhūtā paṭiccasadisaṃ) = (မူလဓာတ်ကြီး အားလုံး မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူသည်)
(paṭiccasadisaṃ, sabbe mahābhūtā) = (မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူသည်၊ မူလဓာတ်ကြီး အားလုံး)
(Imaṃ cittasamuṭṭhānadukaṃ paccayavāre ārammaṇasadisaṃ. Channampi imesaṃ pañcaviññāṇamūlā kātabbā. Saṃkhittaṃ.) = (ဤ စိတ်မှ ဖြစ်ပေါ်လာခြင်း နှစ်မျိုးတွဲသည် အကြောင်းပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်၌ အာရုံဟူသော အကြောင်းနှင့် တူသည်။ ဤ ခြောက်ခုလုံး၏ သိစိတ် ငါးပါးကို အခြေခံခြင်းတို့ကို ပြုရမည်။ အကျဉ်းချုပ်။)
(Saṃkhittaṃ. Sabbaṃ kātabbaṃ. Paccayavārassa pañcaviññāṇaṃ channampi mūlā kātabbā. Sabbe mahābhūte tīṇiyeva moho. Saṃkhittaṃ.) = (အကျဉ်းချုပ်။ အားလုံးကို ပြုရမည်။ အကြောင်းပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်၏ သိစိတ် ငါးပါး၊ ခြောက်ခုလုံး၏ အခြေခံတို့ကို ပြုရမည်။ မူလဓာတ်ကြီး အားလုံးကို မောဟနှင့် သုံးခုသာ။ အကျဉ်းချုပ်။)
(tīṇi, moho) = (သုံးခု၊ မောဟ)
(Itare dve gaṇanāpi sampayuttavāropi sabbaṃ kātabbaṃ.) = (အခြား ရေတွက်ချက် နှစ်ခုကိုလည်း၊ ယှဉ်တွဲခြင်းအလိုက် ဖော်ပြချက်ကိုလည်း အားလုံး ပြုရမည်။)
(cittasamuṭṭhānadukasadisaṃ, ninnānākaraṇaṃ) = (စိတ်မှ ဖြစ်ပေါ်လာခြင်း နှစ်မျိုးတွဲနှင့် တူသည်၊ ကွဲပြားချက် မရှိ)
(ārammaṇādhipatipi sahajātādhipatipi kātabbā) = (အာရုံ အကြီးအမှူးကိုလည်း၊ အတူ ပေါ်ပေါက်သော အကြီးအမှူးကိုလည်း ပြုရမည်)
(ārammaṇādhipatipi sahajātādhipatipi imesampi tiṇṇaṃ kātabbā. Navapi pañhā cittasamuṭṭhānadukasadisā. Ante tīṇi ārammaṇādhipatiyeva) = (အာရုံ အကြီးအမှူးကိုလည်း၊ အတူ ပေါ်ပေါက်သော အကြီးအမှူးကိုလည်း ဤ သုံးခုလုံး၌ ပြုရမည်။ ပြဿနာ ကိုးခုလုံးသည် စိတ်မှ ဖြစ်ပေါ်လာခြင်း နှစ်မျိုးတွဲနှင့် တူကြသည်။ အဆုံး၌ သုံးခုသည် အာရုံ အကြီးအမှူးသာ)
(cittasamuṭṭhānadukasadisā) = (စိတ်မှ ဖြစ်ပေါ်လာခြင်း နှစ်မျိုးတွဲနှင့် တူကြသည်)
(nocittasahabhū mūlaṃyeva labbhati, cittasamuṭṭhānadukasadisā. Tīṇipi ninnānākaraṇaṃ) = (စိတ်နှင့်အတူ တည်ရှိသည် မဟုတ်သော သဘောတရားကို အခြေခံခြင်းသာ တွေ့ရသည်၊ စိတ်မှ ဖြစ်ပေါ်လာခြင်း နှစ်မျိုးတွဲနှင့် တူကြသည်။ သုံးခုလုံး ကွဲပြားချက် မရှိ)
(cittasamuṭṭhānadukasadisaṃ) = (စိတ်မှ ဖြစ်ပေါ်လာခြင်း နှစ်မျိုးတွဲနှင့် တူသည်)
(cittasamuṭṭhānadukasadisā. Imampi ekaṃ kabaḷīkāraāhārasadisaṃ) = (စိတ်မှ ဖြစ်ပေါ်လာခြင်း နှစ်မျိုးတွဲနှင့် တူကြသည်။ ဤ တစ်ခုသည်လည်း လုတ်ပြု၍ စားရသော အာဟာရနှင့် တူသည်)
(sabbaṃ paṭisandhiyaṃ kātabbaṃ, sahajātaṃ purejātampi) = (အားလုံးကို ပဋိသန္ဓေ၌ ပြုရမည်၊ အတူ ပေါ်ပေါက်ခြင်း၊ ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်းလည်း)
(yathā cittasahabhūdukaṃ evaṃ imaṃ dukaṃ kātabbaṃ, ninnānākaraṇaṃ) = (စိတ်နှင့်အတူ တည်ရှိခြင်း နှစ်မျိုးတွဲကဲ့သို့ ထိုနည်းတူ ဤ နှစ်မျိုးတွဲကို ပြုရမည်၊ ကွဲပြားချက် မရှိ)
(ahetukapaṭisandhikkhaṇe dvepi kātabbā) = (အမြစ် မရှိသော ပဋိသန္ဓေ နေသော ခဏ၌ နှစ်ခုလုံးကို ပြုရမည်)
(paṭisandhikkhaṇe dve, saṃkhittaṃ) = (ပဋိသန္ဓေ နေသော ခဏ၌ နှစ်ခု၊ အကျဉ်းချုပ်)
(paṭisandhikkhaṇe ekaṃ kātabbaṃ) = (ပဋိသန္ဓေ နေသော ခဏ၌ တစ်ခုကို ပြုရမည်)
(paṭisandhikkhaṇe dve kātabbā) = (ပဋိသန္ဓေ နေသော ခဏ၌ နှစ်ခုကို ပြုရမည်)
(paṭisandhikkhaṇe ekaṃ kātabbaṃ, saṃkhittaṃ) = (ပဋိသန္ဓေ နေသော ခဏ၌ တစ်ခုကို ပြုရမည်၊ အကျဉ်းချုပ်)
(evaṃ nava pañhā kātabbā. Paccayavāre pañcaviññāṇampi kātabbaṃ, tīṇiyeva moho) = (ဤသို့ ပြဿနာ ကိုးခုကို ပြုရမည်။ အကြောင်းပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်၌ သိစိတ် ငါးပါးကိုလည်း ပြုရမည်၊ မောဟနှင့် သုံးခုသာ)
(saṃkhittaṃ. Tīṇiyeva moho) = (အကျဉ်းချုပ်။ မောဟနှင့် သုံးခုသာ)
(Saṃkhittaṃ. Yathā cittasahabhūduke ārammaṇaṃ evaṃ kātabbaṃ, ninnānākaraṇaṃ. Navapi pañhā.) = (အကျဉ်းချုပ်။ စိတ်နှင့်အတူ တည်ရှိခြင်း နှစ်မျိုးတွဲ၌ အာရုံဟူသော အကြောင်းကဲ့သို့ ထိုနည်းတူ ပြုရမည်၊ ကွဲပြားချက် မရှိ။ ပြဿနာ ကိုးခုလုံး။)
(dvepi adhipatī kātabbā) = (အကြီးအမှူး နှစ်ခုလုံးကို ပြုရမည်)
(dvepi adhipati kātabbā) = (အကြီးအမှူး နှစ်ခုလုံးကို ပြုရမည်)
(Ekāyeva adhipati kātabbā, navapi pañhā. Yathā cittasahabhūdukaṃ, evaṃ kātabbaṃ, ninnānākaraṇaṃ) = (အကြီးအမှူး တစ်ခုတည်းကိုသာ ပြုရမည်၊ ပြဿနာ ကိုးခုလုံး။ စိတ်နှင့်အတူ တည်ရှိခြင်း နှစ်မျိုးတွဲကဲ့သို့၊ ထိုနည်းတူ ပြုရမည်၊ ကွဲပြားချက် မရှိ)
(navapi pañhā cittasahabhūdukasadisā) = (ပြဿနာ ကိုးခုလုံးသည် စိတ်နှင့်အတူ တည်ရှိခြင်း နှစ်မျိုးတွဲနှင့် တူကြသည်)
(navapi pañhā cittasahabhūdukasadisā, ninnānākaraṇaṃ) = (ပြဿနာ ကိုးခုလုံးသည် စိတ်နှင့်အတူ တည်ရှိခြင်း နှစ်မျိုးတွဲနှင့် တူကြသည်၊ ကွဲပြားချက် မရှိ)
(cittasahabhūdukasadisā, ninnānākaraṇaṃ) = (စိတ်နှင့်အတူ တည်ရှိခြင်း နှစ်မျိုးတွဲနှင့် တူကြသည်၊ ကွဲပြားချက် မရှိ)
(cittasahabhūdukasadisā, ninnānākaraṇaṃ. Tīṇipi pacchājātā. Dve. Ekamūlānaṃ ekā ghaṭanā) = (စိတ်နှင့်အတူ တည်ရှိခြင်း နှစ်မျိုးတွဲနှင့် တူကြသည်၊ ကွဲပြားချက် မရှိ။ သုံးခုလုံး နောက်မှ ဖြစ်ပေါ်ခြင်း။ နှစ်ခု။ တစ်ခုကို အခြေခံသည်တို့၏ ပေါင်းစပ်ချက် တစ်ခု)
(cittasahabhūdukasadisā ninnānākaraṇā. Tīṇipi sahajātā, nānākkhaṇikā) = (စိတ်နှင့်အတူ တည်ရှိခြင်း နှစ်မျိုးတွဲနှင့် တူကြသည် ကွဲပြားချက် မရှိ။ သုံးခုလုံး အတူ ပေါ်ပေါက်သည့် ကံ၊ ခဏ ကွဲပြားသည့် ကံ)
(cittasahabhūgamanasadisā, ekaṃyeva kabaḷīkāraṃ āhāraṃ) = (စိတ်နှင့်အတူ တည်ရှိခြင်း နှစ်မျိုးတွဲ၏ သွားပုံနှင့် တူကြသည်၊ လုတ်ပြု၍ စားရသော အာဟာရ တစ်ခုတည်းကိုသာ)
(purejātasadisaṃ purejātaṃ kātabbaṃ. Sabbaṃ saṃkhittaṃ. Vitthāretabbaṃ) = (ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်းကို ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်းဟူသော အကြောင်းနှင့် တူအောင် ပြုရမည်။ အားလုံး အကျဉ်းချုပ်။ အကျယ် ချဲ့ရမည်)
(purejātasadisaṃ, ninnānākaraṇaṃ) = (ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်းဟူသော အကြောင်းနှင့် တူသည်၊ ကွဲပြားချက် မရှိ)
(paṭisandhikkhaṇe tīṇi kātabbā) = (ပဋိသန္ဓေ နေသော ခဏ၌ သုံးခုကို ပြုရမည်)
(yathā cittasaṃsaṭṭhasamuṭṭhānadukaṃ, evaṃ imampi dukaṃ, ninnānākaraṇaṃ) = (စိတ်နှင့် ရောနှော၍ စိတ်မှ ဖြစ်ပေါ်လာခြင်း နှစ်မျိုးတွဲကဲ့သို့၊ ထိုနည်းတူ ဤ နှစ်မျိုးတွဲကိုလည်း၊ ကွဲပြားချက် မရှိ)
(yathā cittasaṃsaṭṭhasamuṭṭhānadukasadisaṃ, ninnānākaraṇaṃ) = (စိတ်နှင့် ရောနှော၍ စိတ်မှ ဖြစ်ပေါ်လာခြင်း နှစ်မျိုးတွဲနှင့် တူသည့်အတိုင်း၊ ကွဲပြားချက် မရှိ)
(paṭisandhikkhaṇe dvepi kātabbā, yāva ajjhattikā mahābhūtā) = (ပဋိသန္ဓေ နေသော ခဏ၌ နှစ်ခုလုံးကို ပြုရမည်၊ အတွင်းပိုင်း မူလဓာတ်ကြီးတို့အထိ)
(Saṃkhittaṃ. Evaṃ navapi pañhā kātabbā. Pañcaviññāṇampi pavesetvā tīṇiyeva moho.) = (အကျဉ်းချုပ်။ ဤသို့ ပြဿနာ ကိုးခုလုံးကို ပြုရမည်။ သိစိတ် ငါးပါးကိုလည်း ထည့်သွင်း၍ မောဟနှင့် သုံးခုသာ။)
(anulomaṃ) = (အဟုတ်ပြ ပုံစံ)
(evaṃ pañca kātabbā, tīṇiyeva moho) = (ဤသို့ ငါးခုကို ပြုရမည်၊ မောဟနှင့် သုံးခုသာ)
(paccanīyaṃ) = (အငြင်းပြ ပုံစံ)
(dve adhipatī tiṇṇampi kātabbā) = (အကြီးအမှူး နှစ်ခုကို သုံးခုလုံး၌ ပြုရမည်)
(tiṇṇampi ekāyeva adhipati) = (သုံးခုလုံး၌ အကြီးအမှူး တစ်ခုတည်းသာ)
(tiṇṇampi ekasadisā) = (သုံးခုလုံး တူညီကြသည်)
(tīṇipi pūretvā kātabbā, cittassāti kātabbā, sampayuttakānañcāti kātabbā) = (သုံးခုလုံးကို ပြည့်စုံစေ၍ ပြုရမည်၊ စိတ်အားဟု ပြုရမည်၊ ယှဉ်တွဲသောတို့အားလည်းကောင်းဟု ပြုရမည်)
(evaṃ navapi pañhā kātabbā) = (ဤသို့ ပြဿနာ ကိုးခုလုံးကို ပြုရမည်)
(Idha atthi sabbaṭṭhāne sahajātaṃ paccayavārasadisaṃ. Purejātaṃ purejātasadisaṃ. Pacchājātaṃ pacchājātasadisaṃ kātabbaṃ, ninnānākaraṇaṃ) = (ဤနေရာ၌ ရှိခြင်းဟူသော အကြောင်း၏ နေရာ အားလုံး၌ အတူ ပေါ်ပေါက်ခြင်းသည် အကြောင်းပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူသည်။ ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်းသည် ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်းဟူသော အကြောင်းနှင့် တူသည်။ နောက်မှ ဖြစ်ပေါ်ခြင်းကို နောက်မှ ဖြစ်ပေါ်ခြင်းဟူသော အကြောင်းနှင့် တူအောင် ပြုရမည်၊ ကွဲပြားချက် မရှိ)
(sahajātapaccayavārasadisaṃ ninnānākaraṇaṃ, paṭhamagamanasadisaṃyeva. Sabbe padā paṭhamaghaṭanānayena vibhajitabbā) = (အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်နှင့် အကြောင်းပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်တို့နှင့် တူသည် ကွဲပြားချက် မရှိ၊ ပထမ သွားပုံနှင့် တူသည်ပင်။ ပုဒ် အားလုံးကို ပထမ ပေါင်းစပ်ချက်၏ နည်းအတိုင်း ခွဲခြမ်းစိတ်ဖြာရမည်)
(saṃkhittaṃ. Sabbe padā vibhajitabbā paṭhamaghaṭanānayena) = (အကျဉ်းချုပ်။ ပုဒ် အားလုံးကို ပထမ ပေါင်းစပ်ချက်၏ နည်းအတိုင်း ခွဲခြမ်းစိတ်ဖြာရမည်)
(yāva asaññasattā, evaṃ tīṇi noupādāmūlake) = (အသညသတ်တို့အထိ၊ ဤသို့ မူလဓာတ်ကြီးများကို မှီ၍ ဖြစ်သည် မဟုတ်သော သဘောတရားကို အခြေခံခြင်း၌ သုံးခု)
(noupādāmūlake tīṇipi paṭiccasadisā, ninnānākaraṇā) = (မူလဓာတ်ကြီးများကို မှီ၍ ဖြစ်သည် မဟုတ်သော သဘောတရားကို အခြေခံခြင်း၌ သုံးခုလုံးသည် မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူကြသည်၊ ကွဲပြားချက် မရှိ)
(tīṇipi paṭiccasadisā, ninnānākaraṇā) = (သုံးခုလုံးသည် မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူကြသည်၊ ကွဲပြားချက် မရှိ)
(noupādāmūlake tīṇi, paṭisandhikkhaṇe tīṇipi kātabbā) = (မူလဓာတ်ကြီးများကို မှီ၍ ဖြစ်သည် မဟုတ်သော သဘောတရားကို အခြေခံခြင်း၌ သုံးခု၊ ပဋိသန္ဓေ နေသော ခဏ၌ သုံးခုလုံးကို ပြုရမည်)
(saṃkhittaṃ. Purejātasadisaṃ ninnānākaraṇaṃ) = (အကျဉ်းချုပ်။ ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်းဟူသော အကြောင်းနှင့် တူသည် ကွဲပြားချက် မရှိ)
(yāva utusamuṭṭhānaṃ) = (ရာသီဥတုမှ ဖြစ်ပေါ်လာသော ရုပ်အထိ)
(nahetusadisaṃ, moho natthi) = (အမြစ်ဟူသော အကြောင်း မဟုတ်ခြင်းနှင့် တူသည်၊ မောဟ မရှိ)
(Evaṃ itare dve gaṇanāpi sampayuttavāropi kātabbā.) = (ဤသို့ အခြား ရေတွက်ချက် နှစ်ခုကိုလည်း၊ ယှဉ်တွဲခြင်းအလိုက် ဖော်ပြချက်ကိုလည်း ပြုရမည်။)
(saṃkhittaṃ. Upādinnamūlake tīṇi. ) = (အကျဉ်းချုပ်။ ကံကြောင့် ဖြစ်သော သဘောတရားကို အခြေခံခြင်း၌ သုံးခု။)
(upādinnamūlake tīṇi, paṭhamasseva rūpajīvitindriyaṃ, itaresu natthi) = (ကံကြောင့် ဖြစ်သော သဘောတရားကို အခြေခံခြင်း၌ သုံးခု၊ ပထမ ပြဿနာ၌သာ ရုပ် အသက်၏ စွမ်းရည်၊ အခြားတို့၌ မရှိ)
(saṃkhittaṃ. Yathā nikkhittapadāni vibhajitabbāni paripuṇṇāni) = (အကျဉ်းချုပ်။ ချထားသော ပုဒ်များအတိုင်း ပြည့်စုံအောင် ခွဲခြမ်းစိတ်ဖြာရမည်)
(saṃkhittaṃ, yathā nikkhittapadāni vitthāretabbāni) = (အကျဉ်းချုပ်၊ ချထားသော ပုဒ်များအတိုင်း အကျယ် ချဲ့ရမည်)
(saṃkhittaṃ, yathā nikkhittapadāni vibhajitabbāni) = (အကျဉ်းချုပ်၊ ချထားသော ပုဒ်များအတိုင်း ခွဲခြမ်းစိတ်ဖြာရမည်)
### SKF
ariyā maggā vuṭṭhahitvā maggaṃ garuṃ = အရိယာတို့သည် မဂ်မှ ထ၍ မဂ်ကို လေးစားဖွယ်ရာ
maggaṃ garuṃ = မဂ်ကို လေးစားဖွယ်ရာ
phalaṃ garuṃ = ဖိုလ်ကို လေးစားဖွယ်ရာ
purimā purimā §T§ā = ရှေးရှေး {T1}
purimaṃ purimaṃ cittaṃ pacchimassa pacchimassa = ရှေးရှေး စိတ်သည် နောက်နောက်
kāyindriyaṃ ca = ကိုယ်၏ စွမ်းရည်လည်းကောင်း
kāyaviññāṇasahagatā khandhā ca = ကိုယ် သိစိတ်နှင့်အတူ ဖြစ်သော အစုအဝေးလည်းကောင်း
§T§aṃ phoṭṭhabbāyatanaṃ ca = {T1} အထိအတွေ့ အာရုံခံ နယ်ပယ်လည်းကောင်း
§T§aṃ phoṭṭhabbāyatanañca vatthu ca = {T1} အထိအတွေ့ အာရုံခံ နယ်ပယ်လည်းကောင်း၊ မှီရာ ဝတ္ထုလည်းကောင်း
ahetukapaṭisandhikkhaṇe §T§aṃ ekaṃ khandhañca cittañca = (the objects with the line link)
§T§aṃ dhammaṃ paṭicca §T§o dhammo uppajjati §C§ā pañca = {T1} သဘောတရားကို မှီ၍ {T2} သဘောတရားသည် {C1.ab} ဖြစ်ပေါ်သည် ငါးခု
senāsanaṃ cittaṃ §T§ānaṃ khandhānaṃ ca cittassa ca §C§ena paccayo = အိပ်ရာ နေရာ၊ စိတ်သည် {T1} အစုအဝေးတို့အားလည်းကောင်း၊ စိတ်အားလည်းကောင်း {C1.if}
bāhiraṃ utusamuṭṭhānaṃ asaññasattānaṃ ekaṃ mahābhūtaṃ = ပြင်ပ၊ ရာသီဥတုမှ ဖြစ်ပေါ်လာသော၊ အသညသတ်တို့၏ မူလဓာတ်ကြီး တစ်ပါး
bāhiraṃ āhārasamuṭṭhānaṃ utusamuṭṭhānaṃ asaññasattānaṃ ekaṃ mahābhūtaṃ = ပြင်ပ၊ အာဟာရမှ ဖြစ်ပေါ်လာသော၊ ရာသီဥတုမှ ဖြစ်ပေါ်လာသော၊ အသညသတ်တို့၏ မူလဓာတ်ကြီး တစ်ပါး

## Source slips (translated as written / read as the obvious form; each logged by --slips)
- ^7-32-2 (3): «sārammaṇo ca anārammaṇo ca dhammo uppajjanti» (dhammo for dhammā): as written («…သဘောတရားသည် … ဖြစ်ပေါ်ကြသည်»).
- «na aññamaññe cha» (Pāli line 277) written apart: read as naaññamaññe.
- «ahetukā nocitte khandhā vicikicchāsahagate …» (Pāli line 413): read as «ahetukā nocittā khandhā, vicikicchāsahagate …».
- «khandhā uppajanti» (uppajjanti), «khandhañca citañca» (cittañca), «cittasahabhuṃ eka khandhañca» (ekaṃ),
  «cittaṃ kaṭattā rūpānaṃ» (kaṭattārūpānaṃ), «No upādā dhammo» (Noupādā).
- «cittasaṃsaṭṭhā sampayuttakā khandhā» (Pāli line 1333; elsewhere «cittaṃ saṃsaṭṭhā …»): as written
  «စိတ်နှင့် ရောနှောသော ယှဉ်တွဲသော အစုအဝေးများ».
- «cakkhuviññāṇasahagatā khandhā ca cakkhāyatanañca» written twice in one list (Ajjhattika atthi, Pāli line 2293):
  translated as written (twice).
- The note «(saṃkhittaṃ, yathā nikkhittapadāni vitthāretabbāni. (2)» is not closed: no «)» written.
- Notes «(dvepi adhipati kātabbā)» (adhipatī), «(yathā cittasaṃsaṭṭhasamuṭṭhānadukasadisaṃ, …)» (yathā + sadisaṃ:
  «…နှင့် တူသည့်အတိုင်း», as 3-01-02's «yathā paṭiccavārasadisaṃ»), «(saṃkhittaṃ. Upādinnamūlake tīṇi. )» (space).

## Unsure Pāli
- «tīṇiyeva moho» / «Tīṇi. Moho» / «tīsuyeva moho»: read as «only three [questions] with moha» / «moha only in three»:
  «မောဟနှင့် သုံးခုသာ» / «သုံးခု။ မောဟ» / «သုံးခု၌သာ မောဟ».
- «senāsanaṃ cittaṃ cittasamuṭṭhānānaṃ khandhānaṃ cittassa ca upanissayapaccayena» (Cittasamuṭṭhāna pañhā): citta read
  as the last support of the list «အိပ်ရာ နေရာ၊ စိတ်သည် …» (as the Marathi run); possibly a slip.
- «(Imaṃ cittasamuṭṭhānadukaṃ paccayavāre ārammaṇasadisaṃ …)» stands in the Cittasahabhū dyad: as written.
- «Sabbe mahābhūte tīṇiyeva moho» (a note): «မူလဓာတ်ကြီး အားလုံးကို မောဟနှင့် သုံးခုသာ» (as written).
- «sahajātapaccayavārasadisaṃ» read as «like the sahajāta- and paccaya-vāra» (as the Marathi run).
- «(Mūlaṃ kātabbaṃ / pucchitabbaṃ)»: mūla = the opening of the series «အခြေခံ» (3-01-02).

## Harmonise (for the consistency pass)
- 3-02 file line 565 «cakkhuviññāṇasahagato eko khandho ca cakkhāyatanañca tiṇṇannaṃ khandhānaṃ…» is published with the
  two conditioning members as recipients («… တစ်ပါးအားလည်းကောင်း၊ … နယ်ပယ်အားလည်းကောင်း၊ အစုအဝေး သုံးပါးတို့အားလည်းကောင်း»);
  3-09 has the same construction read as subject + recipient («… တစ်ပါးလည်းကောင်း၊ … နယ်ပယ်လည်းကောင်း အစုအဝေး
  နှစ်ပါးတို့အား»). The qualifiers that give this reading are applied only while 3-09 runs, so 3-02 regenerates as published.
- ajjhattika: the 3-09 dyad term is the pi-1 Mātikā «အတွင်းပိုင်း» (bare, as «ပြင်ပ»); 3-01-02 / 2-03-06 have
  «အတွင်းပိုင်း ဖြစ်သော» for «ajjhattikā (bāhirā) mahābhūtā» outside the dyad (pi-1 «rūpaṃ ajjhattikaṃ»).
- upādā (dyad term) «မူလဓာတ်ကြီးများကို မှီ၍ ဖြစ်သော» (pi-1 ^1-M2-67) vs the module's upādārūpa «မူလဓာတ်ကြီးတို့ကို မှီ၍ ဖြစ်သော ရုပ်».
