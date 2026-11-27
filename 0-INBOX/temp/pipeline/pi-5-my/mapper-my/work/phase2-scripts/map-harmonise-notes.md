# pi-5 Burmese keyword mapping, phase 1: keyword ambiguities and text inconsistencies

Scope: preamble and 1-puggalakatha (map_ch1.py with the shared module map5_rules.py), plus what the whole-book
frame check (frame_coverage.py) showed. The translation was not changed. Burmese only from this track's final pi-5
text, my5-zeroshot-terms.md and the final pi-1 … pi-4 mappings. pi-1-my … pi-4-my were only read.

## A. Text inconsistencies (for the rails step; translation not edited)

1. **uddāna and saṃkhitta share one word.** «(Saṃkhittaṃ)» = «(အကျဉ်းချုပ်)» (ch1 ^5-53, ^5-54, ^5-60, ^5-68, ^5-94,
   ^5-192, ^5-238) and «Tassuddānaṃ» = «ထို၏ အကျဉ်းချုပ်» (all 23 vagga uddānas). Two Pāli words, one Burmese word. The
   ch1 verse uddāna also has peyyāla = «အကျဉ်းချုံ့ချက်» (^5-238), a third, close form. Mapped as the text has them:
   Saṃkhittaṃ = uddānaṃ = အကျဉ်းချုပ်.
2. **nicca / dhuva in one list.** ^5-238: niccabhattaṃ «အမြဲ ထမင်း» and dhuvayāgū «အမြဲ ယာဂု» both «အမြဲ», while the
   same segment's «niccā dhuvā sassatā» = «မြဲသော၊ ခိုင်ခံ့သော၊ ထာဝရ တည်မြဲသော» (and ^5-235 nicco dhuvo). The synonym
   rule (each synonym its own word) is broken in the sutta's list of foods. Mapped by the first occurrence: CTX
   ^5-238 nicca = dhuva = အမြဲ.
3. **taṇhā.** ^5-75 (the sutta «taṇhāsaṃyojanānaṃ») = «တဏှာ နှောင်ကြိုး»; the cross-book term is «တပ်မက်မှု» (pi-1 …
   pi-4, 83 uses; elsewhere in pi-5). The module (STOCK taṇhā) takes «တပ်မက်မှု» where the text has it, else «တဏှာ».
4. **hita / attha in one sutta.** ^5-230 «bahujanahitāya … atthāya hitāya sukhāya devamanussānaṃ» = «လူအများ၏
   အကျိုးစီးပွားအတွက် … နတ်နှင့် လူတို့၏ အကျိုးအတွက်၊ စီးပွားအတွက် …»: hita is «အကျိုးစီးပွား» and «စီးပွား», attha
   is «အကျိုး»; in ^5-229 / ^5-22 … «attahitāya» hita is «အကျိုး» («မိမိ၏ အကျိုးအတွက်»). Mapped: hitāya = အကျိုး (13 ×
   attahitāya), အကျိုးစီးပွား (^5-230).
5. **añña.** «aññaṃ A añño B» = «Aနှင့် Bသည် တခြားစီ ဖြစ်» (the frame), but ^5-78 / ^5-80 «manussabhūto añño, devo añño»
   = «လူ ဖြစ်ခဲ့သူ တခြား၊ နတ် တခြား» (without «စီ») and ^5-89 «anañño» = «အခြား မဖြစ်ဘဲ», ^5-116 «añño» = «အခြားသူ».
   Mapped as the text has them (FRAME f_anna: တခြားစီ / တခြား / အခြား).
6. **suddha.** «Suddhasaccikaṭṭho» = «ရိုးရိုး အမှန်တကယ် အရာ», but the verse ^5-233 «Suddhasaṅkhārapuñjoyaṃ» = «သက်သက်
   ပြုပြင်ဖန်တီးမှုတို့၏ အစုအပုံ», and «kevalo» (^5-235) is also «သက်သက်». suddha and kevala share «သက်သက်».
7. **sandhāvataṃ saṃsarataṃ** (^5-75) = «ကူးသွား ကျင်လည်နေကြသော»: two participles with one ending. Mapped
   sandhāvataṃ = ကူးသွား (the bare stem the text has; no «…သော» of its own), saṃsarataṃ = ကျင်လည်နေသော.
8. **Gatianuyoga heading vs gati.** The heading «Gatianuyogo» = «လားရာကို စစ်ဆေးမေးမြန်းခြင်း» uses «လားရာ»; pi-2 ^2-U58
   had «လားရာ ဘဝ» for gati. One form in pi-5 («လားရာ»), different from pi-2: listed for the termbase.
9. **The «said» verbs.** «Vuttaṃ bhagavatā» = «… ဟောတော်မူသည်», «etadavoca» = «… ပြောခဲ့သည်» (^5-233 the nun) and «…
   လျှောက်ခဲ့သည်» (^5-234 Ānanda to the Buddha): by design (harmonise B5); no change.
10. **Spacing.** sacchikaroti: pi-4 value «မျက်မှောက် ပြုသည်», the text writes «မျက်မှောက်ပြုသူ» (^5-194, ^5-196) but
    «မျက်မှောက် မပြုသူ» in the negative (as pi-4 A4 unnaḷo / mukharo). Kept the pi-4 value.

## B. Keyword ambiguities (how they were settled)

- **aṭṭha**: «thing» (saccikaṭṭha = «အမှန်တကယ် အရာ») vs «eight»; FRAME @attha_thing («အရာ» where the Pāli has «-ṭṭh-»
  and the text «အရာ», else the count).
- **aññā**: «other» (fem.) vs «final knowledge» (aññindriya, aññātāvī «အပြည့်အဝ သိမြင်…»); f_anna_f by the first in the
  Pāli.
- **upādā**: Upādāpaññatti / upādāya «မှီ၍» vs the fragment of anupādā(parinibbāna) «စွဲလမ်းမှု မရှိဘဲ» = the positive
  part «စွဲလမ်းမှု» (rule 8; ^5-125 …). pi-1's upādā (derived matter) is a third sense, not present here.
- **vādī**: the speakers of the note «[iminā lakkhaṇena sakavādī/paravādīpucchā dassitā]» = «မိမိဘက် / တစ်ဖက်သား» (the
  one keyword vādī stands for the whole compound; saka / para are not keywords), vs the epithets saccavādī … «…
  ဆိုတော်မူသော» (Q8).
- **micchā**: verdict «မှားသည်» / «idaṃ te micchā» «အမှား» / compound «မှားယွင်းသော»; one sense per segment (first).
- **vata**: «vata re» «အမှန်ပင်» vs the vow «အကျင့်ဝတ်» (pi-1); the exclamation «Ime vata bhonto sattā» (ch11 ^5-377)
  is a third sense for phase 2.
- **Tena hi**: «သို့ဖြစ်လျှင်» (conclusion) vs «သို့ဖြစ်၍» (^5-5 / ^5-10 «Tena hi ye kate niggahe …», «Tena hi yaṃ
  niggaṇhāsi»): first in the text.
- **dhātuyā**: plane «ဘုံ» (rūpa- / arūpa- / kāmadhātuyā) vs element «ဓာတ်»; **rūpa**: plane «သိမ်မွေ့သော ရုပ်»
  (Rūpadhātuyā rūpī), visible object «အဆင်းအရောင်» (rūpāyatana, rūpadhātu as element), matter «ရုပ်».
- **rūpaṃ in ^5-122** mixes «rūpaṃ passati» (seen: «အဆင်းအရောင်», first in the Pāli) and «Rūpaṃ puggalo / rūpaṃ cavati»
  (matter «ရုပ်»): CTX ^5-122 gives the multiword keywords their own sense.
- **sukha / dukkha**: pleasure / pain «ချမ်းသာ / ဆင်းရဲ» (sukhadukkha, dibba sukha, āpāyika dukkha), feeling «သာယာသော /
  နာကျင်သော», the truth / the end «ဒုက္ခ» (dukkhassantakaro, dukkhameva); by the first compound, checked against the
  text.
- **para**: paracittaṃ «အခြားသူ», paraṃ lokaṃ «တမလွန်», paraṅkāra «သူတစ်ပါး», paravādī «တစ်ဖက်သား».
- **purisa**: «လူ» (purisakāra, purisayuga «လူ အတွဲ») vs «ယောက်ျား» (the male, ^5-117 puriso; ^5-21 purisindriya).
- **yo / yaṃ / yena**: «အကြင်သူ / အကြင်အရာ» where the text has the correlative (^5-118, ^5-119), else (no direct
  equivalent) (^5-195, ^5-196, ^5-220, ^5-224: «yo … so puggalo» = «…သူသည်ပင် ပုဂ္ဂိုလ်»).
- **hevameva** (^5-4): the main text «hevamevaṃ» «ဤနည်းအတိုင်းပင်», the variant «[hevameva (syā.)]» is the same word: the
  keyword gets the main text's Burmese. **suniggahitova** (^5-3) stands only in the variant: (no direct equivalent).
- **Extractor fragments** mapped to the part of the phrase they carry: tiṇa paṭisaṃvedī (tiṇakaṭṭhavanappatīnaṃ
  paṭisaṃvedī) «မြက် … ခံစားသော», kalyāṇa kāretā «ကောင်းမွန်သော … ပြုလုပ်စေသူ», kalyāṇa vipāko «ကောင်းမွန်သော …
  အကျိုး», kāraṃ dukkhaṃ «ဆင်းရဲ … ပြုသော», chinno hoti «ပြတ်သူ … ဖြစ်သည်», lokā upapanno «လောက … ပြန်လည်
  ဖြစ်ပေါ်သော», dha (the reference «dha. pa.») «“ဓမ္မပဒ”», khattu (sattakkhattu) «ကြိမ်», aṭṭhe / same / sama / jāte
  (esese ekaṭṭhe same samabhāge tajjāte) «အနက် တူသော / ညီမျှသော / တူသော / တစ်မျိုးတည်းမှ ဖြစ်သော».

## C. Genuinely unclear mappings (for review)

1. **appiyaṃ karitvā** (^5-67, ^5-68) = «… စကားကို ဦးစားမပေးဘဲ»: appiyaṃ = «ဦးစားမပေး» (the privative a- as the text's
   «မ…»), karitvā = (no direct equivalent) (one Burmese verb phrase, as pi-4 P4 / pi-1 caya). The alternative appiyaṃ =
   «ဦးစား», karitvā = «ပေး၍» (neg-abs) splits the negation from its word.
2. **Āmantā** = «ဟုတ်ပါသည်» whole (Q2), not «ဟုတ်သည်» by rule 4 (as Namo «ရှိခိုးပါ၏» = ရှိခိုးသည်).
3. **-ī adjectives** (Q8): paṭisaṃvedī = «ခံစားသော» and the -vādī epithets «… ဆိုတော်မူသော» follow pi-4 rule 3
   (pi-4 paṭisaṃvedī «ခံစားသော»), although my5-zeroshot-terms lists «ခံစားသူ / ဆိုတော်မူသူ» and the text uses the person
   noun. If the user prefers the person noun for this book, only STOCK (and the -vādī entries) change.
4. **bhikkhave** = «ရဟန်း» (rule 1: the vocative's «တို့» is the plural marker); the text has «ရဟန်းတို့၊».
5. **anamataggo** = «အစကို ရှာ၍ မတွေ့နိုင်» (the text's whole predicate, negative included: the Pāli word is itself
   a negative compound).
6. **sassato**: adjective «ထာဝရ တည်မြဲသော» (puggalo sassato, rule 3) where the pi-1 / pi-2 view-clause value «ထာဝရ
   တည်မြဲသည်» does not fit; the view clause («… တည်မြဲသည်ဟု …») keeps the pi-1 / pi-2 value (f_sassato).

## D. For phase 2

- Import `map5_rules` (`R.Mapper(chapter_tables={ch: T}, ctx=CTX, funcs=F)`; `R.verify_file(ch)`); do not edit the module
  in parallel: add chapter values to your own table; a value that should be book-wide goes to the phase-3 scan.
- `frame-coverage.md` lists, for the 150 most frequent keywords, where the module alone fails and why (19 keywords, 48
  of 8,057 uses): all are other compounds / senses / constructions to settle in the chapter tables.
- Helper scripts (read-only) in `work/`: `show.py CH ID…` (Pāli, Burmese, keywords of segments), `kw.py KW N STEM`
  (occurrences), `fails.py KW…` (module failures), `cand.py KW…` (candidate Burmese n-grams), `diag.py CH values`.
