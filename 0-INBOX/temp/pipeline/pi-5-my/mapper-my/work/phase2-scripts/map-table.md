# pi-5 Burmese keyword mapping, PHASE 1: rules and review table (Kathāvatthu «အငြင်းပွားရာ အကြောင်းအရာများကို ဆွေးနွေးခြင်း»: preamble, 1-puggalakatha)

Written by `map_ch1.py` (tables of the preamble and the Puggalakathā) with the shared module `map5_rules.py`. Burmese from the FINAL text of this track only (`AI_translation/burmese/pi-5-burmese-plain-zeroshot_split_chapters`), `my5-zeroshot-terms.md` and the final pi-1 … pi-4 Burmese mappings; no other Burmese source.

## Numbers

- `preamble.mapped.md`: 3 lines, keyword preservation `bad []`, presence failures 0, «, » / «၊» / « / » in a value 0, (no direct equivalent) 0, chunks matched by an ending rule 1.
- `1-puggalakatha.mapped.md`: 269 lines, keyword preservation `bad []`, presence failures 0, «, » / «၊» / « / » in a value 0, (no direct equivalent) 10, chunks matched by an ending rule 491.
- Keyword uses 3874: the same value as a pi-1 … pi-4 mapping for that keyword 1265; a keyword that pi-1 … pi-4 never mapped 2199; a value different from pi-1 … pi-4 410 (in 71 keywords, listed below with the reason).
- Source of the values (uses): frame 1305, stock 732, table 639, pi-2 455, compose 408, terms 250, pi-4 62, pi-1 9, ctx 8, pi-3 6 (frame / stock = the module tables, table = the chapter table, ctx = per-segment override, pi-N = the pi-N mapping, terms = my5-zeroshot-terms, compose = members joined).

## Rules used (binding, unchanged)

The value is the word or phrase of THAT segment's Burmese (the FINAL pi-5 text) that carries the keyword, in the
dictionary form of the approved Burmese mappings:

- **pi-1** `map-table.md` rules 1–11 (approved 2026-11-17): rule 1 nouns without final case particles / plural markers
  (inner particles of a phrase stay); rule 2 a noun predicated of a subject = the noun; rule 3 adjectives / participles
  «…သော» (gerundives «…မည့်»); rule 4 verbs «…သည်»; rule 5 «X dhammā» and negatives; rule 6 sentence-final material
  dropped; rule 7 titles whole; rule 8 fragments that lost a negative = the positive part; rule 9 particles; rule 10
  discontinuous parts « … », no « / », no «, » / «၊» inside a value; rule 11 sense by context. The agreed later pi-1
  rules: absolutives keep «…၍»; relative pronouns = (no direct equivalent) where the Burmese builds the clause with
  «ရှိသော / ရှိသမျှ»; one sense per segment (decision 3); counts keep the text's classifier (decision 5).
- **pi-2** N1–N11 (approved 2026-11-18) and the harmonise decisions (compound members inside one Burmese word: one
  member gets the word, the other (no direct equivalent); «vuccati X» = «Xဟု ခေါ်သည်»; pi-2 «na uppajjati = … မဖြစ်ပေါ်»).
- **pi-3** M1–M9 (approved 2026-11-19): the « … » gap; a translated editors' note gets values, a Roman-script variant =
  (no direct equivalent) (M9 / M2); the presence check endings of M7.
- **pi-4** P1–P8 and A2: person-type names (P1), agent nouns «…သူ» (P6), the presence endings of P3, «X၍» against
  «မXဘဲ» (A2), «puggalo P» = «ပုဂ္ဂိုလ် … P» in text order (P8).
- **pi-1 … pi-4 values**: every keyword not in this run's tables is looked up in the FINAL pi-1 … pi-4 Burmese mappings
  (`AI_translation/burmese/pi-{1,2,3,4}-keywords-by-reference-pali-burmese-plain.md`; order pi-2, pi-3, pi-4, pi-1:
  pi-2 first where pi-1 and pi-2 differ, as the brief says): the most frequent value that the segment's Burmese has as a
  phrase, then one whose chunks are all literal, then (verbs, and phrases with another attributive ending) one present by
  an ending rule. A pi-1 … pi-4 multiword value present by an ending rule wins over a composed value.
- **pi-5 forms**: `my5-zeroshot-terms.md` single forms (persons, names, the propositions of §8 / §9), used where the
  segment has them.

## How the module is built (`map5_rules.py`, imported by phase 2)

Lookup per keyword: CTX[segment] → the chapter's own table → FRAME (dialectic machinery) → STOCK (core terms of the
book) → pi-5 terms (literal) → pi-1 … pi-4 value as a phrase → pi-5 terms (by an ending rule) → pi-1 … pi-4 multiword
value (by an ending rule) → compose (members joined, Q3 / Q4 / Q5) → counts → pi-1 … pi-4 value by an ending rule.
A value «@name» calls a context function (FUNCS) with the keyword, the Pāli segment and the Burmese segment; every
function checks its value against the text and falls back to the text's other word. Nothing runs on import (files are
read lazily); `Mapper(chapter_tables=…, ctx=…, funcs=…)` is the entry point, `verify_file(ch)` the verifier.

## NEW rules (beyond pi-1 … pi-4), for review

Q1. **Presence check, more endings** (`map5_rules.py`, each marked «pi-5»): «Xသော» and «Xသည်» also against the
    question form «Xသလော» (every proposition of the book is asked as «… ဖြစ်သလော / တွေ့ရသလော»); «Xသည်» also against
    the polite imperative «Xပါ» ([ṭīkā oloketabbā] «ဋီကာကို ကြည့်ပါ») and the elided series item «X…» (my5-zeroshot-
    terms §4: «… တွေ့ရ…»); an absolutive «X၍» also against the text's «Xပြီးမှ / Xပြီးလျှင် / Xပြီး / Xလျက်» (hutvā =
    ဖြစ်၍ against «လူ ဖြစ်ပြီးမှ»; sandhāvitvāna = ကူးသွား၍ against «ကူးသွားပြီးလျှင်») and the past negative
    «မXခဲ့ဘဲ» (pi-4 A2 extended: «na mātā hutvā» «အမိ မဖြစ်ခဲ့ဘဲ»).
Q2. **The answer formula** Āmantā = «ဟုတ်ပါသည်» whole (my5-zeroshot-terms §3 «Āmantā. = ဟုတ်ပါသည်။»): a fixed
    answer, not a verb whose ending rule 4 normalises (the full stop goes, rule 6).
Q3. **Multiword keywords in text order** (pi-1 rule 10, pi-4 P8): the members' values in the order of their tightest
    window in the segment's Burmese (the members of one phrase stand together); a finite verb «…သည်» goes last
    (Burmese is verb-final: Puggalo upalabbhati = ပုဂ္ဂိုလ် … တွေ့ရသည်, never «တွေ့ရသည် … ပုဂ္ဂိုလ်»); a part that has
    a value of its own is joined as a whole (nibbānassa paṭisaṃvedī upalabbhati = နိဗ္ဗာန်ကို ခံစားသူကို တွေ့ရသည်); an
    inner particle between adjacent members stays (rule 1: puggalassa paññatti = ပုဂ္ဂိုလ်၏ သတ်မှတ်ချက်, Rūpaṃ upādāya =
    ရုပ်ကို မှီ၍); members the text writes as one word join without a space (dibbena cakkhunā = နတ်မျက်စိ).
Q4. **The «လည်း» of ca / pi** is not part of a multiword keyword: where a member is followed by «…လည်း» the members
    are joined with « … » (rūpaṃ upalabbhati in «ရုပ်ကိုလည်း … တွေ့ရ» = ရုပ် … တွေ့ရသည်; puggalo saphalo «ပုဂ္ဂိုလ်သည်လည်း
    အသီးအပွင့် ရှိသော» = ပုဂ္ဂိုလ် … အသီးအပွင့် ရှိသော). The «လည်း» of «neither … nor» stays (pi-1 rule 6: puggalo neva
    saṅkhato = ပုဂ္ဂိုလ်သည် ပြုပြင်ဖန်တီးထားသော အရာလည်း မဟုတ်).
Q5. **Negated verbs**: a keyword with the negative (Puggalo nupalabbhati) = the text's «မ + verb» without «သည်» (pi-2
    «na uppajjati = … မဖြစ်ပေါ်»: Puggalo nupalabbhati = ပုဂ္ဂိုလ် … မတွေ့ရ); the bare upalabbhati of a negated
    segment keeps the positive «တွေ့ရသည်» (rule 8).
Q6. **The dialectic frame words** (FRAME table, one value book-wide; my5-zeroshot-terms §3 / §5): niggaha(ṃ) =
    ချေပချက်, paṭikamma(ṃ / e) = ပြန်လှန် ချေပချက်, upanayana = ဆက်စပ် အသုံးချချက်, niggamana = နိဂုံးချုပ်ချက်,
    paṭipādanā = ဆက်စပ် တင်ပြချက်; Ājānāhi = လက်ခံသည် (rule 4); vata of «vata re» = အမှန်ပင် (the vow vata keeps the pi-1
    «အကျင့်ဝတ်»); micchā = the verdict «…ti micchā» မှားသည် / «idaṃ te micchā» အမှား / the compound member
    မှားယွင်းသော (one sense per segment, the first in the Pāli); Tena hi = သို့ဖြစ်လျှင် (Tena hi P / na vattabbaṃ) or
    သို့ဖြစ်၍ (Tena hi ye kate niggahe …), the first in the text; Nanu = မဟုတ်လော; niggahetabbe / -ā = ချေပရမည့် (the
    text «… ချေပရမည်») or ချေပရသည် where the text has only «မချေပရ»; saccikaṭṭhaparamatthena = အမှန်တကယ် အဆုံးစွန်
    အနက် (the instrumental «အားဖြင့်» goes, rule 1), paramatthena = အဆုံးစွန် အနက်, atthena = အနက်, parama = အဆုံးစွန်,
    paramattho = အဆုံးစွန် အရာ, saccikaṭṭho = အမှန်တကယ် အရာ; the X-dhamma lists (khaya- / vaya- / virāga- /
    nirodhadhamma) = «Xတတ်သော သဘော … ရှိသော», the last (vipariṇāmadhamma) contiguous «… သဘော ရှိသော» (pi-2 value).
Q7. **Correlatives**: yo / yaṃ / yena = အကြင်သူ / အကြင်အရာ where the text has the correlative «အကြင်» (^5-118,
    ^5-119; pi-1 has «အကြင်» once); otherwise (no direct equivalent) (pi-1: the clause built with «…သူ / ရှိသော»).
Q8. **-ī adjectives** of the book (paṭisaṃvedī, vipākapaṭisaṃvedī, the -vādī epithets, kāmī, rūpavā) = «…သော»
    (pi-4 rule 3, parinibbāyī = ပရိနိဗ္ဗာန် ပြုသော; pi-4 paṭisaṃvedī = ခံစားသော), the text's «…သူ» normalised, even
    where my5-zeroshot-terms lists «…သူ»; agent nouns in -tar / -aka stay «…သူ» (pi-4 P6: kattā = ပြုလုပ်သူ, kāretā =
    ပြုလုပ်စေသူ, kārako = ပြုသူ); person-type names stay names (P1: dhammānusārī, kāyasakkhi, aññātāvī of pi-1).

## Frame and stock keywords (module tables, `map5_rules.FRAME` / `STOCK`) with their ch1 values

A value «@name» in the module is a context function; the column shows the values it gave in phase 1.

| Pāli keyword | module entry | Burmese in preamble / ch1 (uses) |
|---|---|---|
| Āmantā | FRAME: ဟုတ်ပါသည် | ဟုတ်ပါသည် (205) |
| Ājānāhi | FRAME: လက်ခံသည် | လက်ခံသည် (33) |
| niggahaṃ | FRAME: function @niggaha | ချေပချက် (22) |
| niggaha | FRAME: function @niggaha | ချေပချက် (2) |
| niggaho | FRAME: function @niggaha | — |
| niggahe | FRAME: function @niggaha | — |
| paṭikammaṃ | FRAME: ပြန်လှန် ချေပချက် | ပြန်လှန် ချေပချက် (11) |
| paṭikamma | FRAME: ပြန်လှန် ချေပချက် | — |
| paṭikamme | FRAME: ပြန်လှန် ချေပချက် | ပြန်လှန် ချေပချက် (2) |
| upanayana | FRAME: ဆက်စပ် အသုံးချချက် | ဆက်စပ် အသုံးချချက် (2) |
| niggamana | FRAME: နိဂုံးချုပ်ချက် | နိဂုံးချုပ်ချက် (2) |
| paṭipādanā | FRAME: ဆက်စပ် တင်ပြချက် | ဆက်စပ် တင်ပြချက် (2) |
| anuloma | FRAME: အစဉ်အတိုင်း | အစဉ်အတိုင်း (5) |
| anulomaṃ | FRAME: အစဉ်အတိုင်း | အစဉ်အတိုင်း (4) |
| paccanīka | FRAME: ပြောင်းပြန် | ပြောင်းပြန် (5) |
| paccanīkaṃ | FRAME: ပြောင်းပြန် | ပြောင်းပြန် (4) |
| Anulomapaccanīkaṃ | FRAME: အစဉ်အတိုင်းနှင့် ပြောင်းပြန် | အစဉ်အတိုင်းနှင့် ပြောင်းပြန် (4) |
| Paccanīkānulomaṃ | FRAME: ပြောင်းပြန်နှင့် အစဉ်အတိုင်း | ပြောင်းပြန်နှင့် အစဉ်အတိုင်း (4) |
| paṭijānantaṃ | FRAME: ဝန်ခံနေသော | ဝန်ခံနေသော (2) |
| paṭijānantā | FRAME: ဝန်ခံနေသော | ဝန်ခံနေသော (2) |
| paṭiññāya | FRAME: ဝန်ခံချက် | ဝန်ခံချက် (4) |
| hetāya | FRAME: ထို | ထို (4) |
| niggaṇhāma | FRAME: ချေပသည် | ချေပသည် (2) |
| niggaṇhāsi | FRAME: ချေပသည် | ချေပသည် (4) |
| niggahetabbe | FRAME: function @niggahetabba | ချေပရမည့် (2); ချေပရသည် (2) |
| niggahetabbā | FRAME: function @niggahetabba | ချေပရသည် (2) |
| Suniggahito | FRAME: ကောင်းစွာ ချေပခြင်း ခံရသော | ကောင်းစွာ ချေပခြင်း ခံရသော (2) |
| Dunniggahitā | FRAME: မကောင်းစွာ ချေပခြင်း ခံရသော | မကောင်းစွာ ချေပခြင်း ခံရသော (2) |
| dunniggahite | FRAME: မကောင်းစွာ ချေပခြင်း | မကောင်းစွာ ချေပခြင်း (2) |
| niggahite | FRAME: ချေပခြင်း | ချေပခြင်း (2) |
| dukkaṭe | FRAME: မကောင်းစွာ ပြုခဲ့သော | မကောင်းစွာ ပြုခဲ့သော (2) |
| suniggahitova | FRAME: function @roman | (no direct equivalent) (1) |
| hevameva | FRAME: function @hevameva | ဤနည်းအတိုင်းပင် (1) |
| tava | FRAME: သင် | သင် (2) |
| ṭīkā | FRAME: ဋီကာ | ဋီကာ (1) |
| oloketabbā | FRAME: ကြည့်သည် | ကြည့်သည် (1) |
| vata | FRAME: function @vata | အမှန်ပင် (54) |
| micchā | FRAME: function @miccha | မှားသည် (39); မှားယွင်းသော (1) |
| Nanu | FRAME: မဟုတ်လော | မဟုတ်လော (25) |
| Tena hi | FRAME: function @tenahi | သို့ဖြစ်လျှင် (14); သို့ဖြစ်၍ (2) |
| hevaṃ | FRAME: ဤသို့ | ဤသို့ (2) |
| pucchā | FRAME: function @puccha | အမေး (3) |
| dassitā | FRAME: ပြထားသော | ပြထားသော (2) |
| lakkhaṇena | FRAME: အမှတ်အသား | အမှတ်အသား (2) |
| vādī | FRAME: function @vadi | ဆိုတော်မူသော (8); မိမိဘက် (1); တစ်ဖက်သား (1) |
| upalabbhati | FRAME: တွေ့ရသည် | တွေ့ရသည် (130) |
| upalabbhanti | FRAME: တွေ့ရသည် | တွေ့ရသည် (17) |
| nupalabbhati | FRAME: မတွေ့ရ | — |
| nupalabbhanti | FRAME: မတွေ့ရ | — |
| saccikaṭṭhaparamatthena | FRAME: အမှန်တကယ် အဆုံးစွန် အနက် | အမှန်တကယ် အဆုံးစွန် အနက် (92) |
| paramatthena | FRAME: အဆုံးစွန် အနက် | အဆုံးစွန် အနက် (92) |
| atthena | FRAME: function @atthena | အနက် (92) |
| parama | FRAME: function @parama | အဆုံးစွန် (92) |
| paramattho | FRAME: အဆုံးစွန် အရာ | အဆုံးစွန် အရာ (10) |
| saccikaṭṭho | FRAME: function @saccikattho | အမှန်တကယ် အရာ (9) |
| saccikaṭṭha | FRAME: function @saccikattho | အမှန်တကယ် အရာ (2) |
| aṭṭho | FRAME: အရာ | အရာ (9) |
| aṭṭha | FRAME: function @attha_thing | အရာ (1) |
| suddha | FRAME: function @suddha | ရိုးရိုး (2); သက်သက် (1) |
| okāsa | FRAME: နေရာ | နေရာ (2) |
| avayava | FRAME: အစိတ်အပိုင်း | အစိတ်အပိုင်း (2) |
| Sabbattha | FRAME: နေရာတိုင်း | နေရာတိုင်း (2) |
| Sabbadā | FRAME: အချိန်တိုင်း | အချိန်တိုင်း (1) |
| Sabbesu | FRAME: function @sabbesu | အရာအားလုံး (2) |
| Pañcamo | FRAME: ပဉ္စမ | ပဉ္စမ (1) |
| Chaṭṭho | FRAME: ဆဋ္ဌမ | ဆဋ္ဌမ (1) |
| Sattamo | FRAME: သတ္တမ | သတ္တမ (1) |
| aṭṭhaka | FRAME: ရှစ်ပါးအစု | ရှစ်ပါးအစု (2) |
| Saṃkhittaṃ | FRAME: အကျဉ်းချုပ် | အကျဉ်းချုပ် (7) |
| bhagavatā | FRAME: မြတ်စွာဘုရား | မြတ်စွာဘုရား (19) |
| suttanto | FRAME: သုတ္တန် | သုတ္တန် (13) |
| Vuttaṃ | FRAME: ဟောတော်မူသည် | ဟောတော်မူသည် (2) |
| vuttaṃ | FRAME: ဟောတော်မူသည် | — |
| Vuttaṃ bhagavatā | FRAME: မြတ်စွာဘုရား … ဟောတော်မူသည် | မြတ်စွာဘုရား … ဟောတော်မူသည် (2) |
| bhikkhave | FRAME: ရဟန်း | ရဟန်း (8) |
| bhante | FRAME: အသျှင်ဘုရား | အသျှင်ဘုရား (2) |
| kāraṇena | FRAME: အကြောင်း | အကြောင်း (12) |
| katvā | FRAME: function @katva | — |
| eva | FRAME: function @eva | ပင် (11); သာ (2) |
| kathā | FRAME: function @katha | ဆွေးနွေးချက် (4); ဆွေးနွေးခြင်း (1) |
| anuyogo | FRAME: စစ်ဆေးမေးမြန်းခြင်း | စစ်ဆေးမေးမြန်းခြင်း (16) |
| anuyoga | FRAME: စစ်ဆေးမေးမြန်းခြင်း | စစ်ဆေးမေးမြန်းခြင်း (1) |
| vaggo | FRAME: ဝဂ် | ဝဂ် (1) |
| niṭṭhitā | FRAME: ပြီးဆုံးသော | ပြီးဆုံးသော (1) |
| saṃsandanaṃ | FRAME: နှိုင်းယှဉ်ခြင်း | နှိုင်းယှဉ်ခြင်း (5) |
| saṃsandanā | FRAME: နှိုင်းယှဉ်ခြင်း | နှိုင်းယှဉ်ခြင်း (1) |
| suddhika | FRAME: ရိုးရိုး | ရိုးရိုး (2) |
| opamma | FRAME: ဥပမာ | ဥပမာ (2) |
| catukka | FRAME: လေးပါး | လေးပါး (2) |
| naya | FRAME: function @naya | နည်း (2) |
| sodhanaṃ | FRAME: စိစစ်ခြင်း | စိစစ်ခြင်း (2) |
| koci | FRAME: function @koci | တစ်စုံတစ်ယောက် (26) |
| Yo | FRAME: function @yo | (no direct equivalent) (4) |
| yo | FRAME: function @yo | အကြင်သူ (3) |
| yaṃ | FRAME: function @yam | အကြင်အရာ (3) |
| yena | FRAME: function @yena | အကြင်အရာ (3) |
| Aññaṃ | FRAME: function @anna | တခြားစီ (15) |
| aññaṃ | FRAME: function @anna | တခြားစီ (9) |
| añño | FRAME: function @anna | တခြားစီ (3); တခြား (2); အခြား (2) |
| Añño | FRAME: function @anna | တခြားစီ (5) |
| aññā | FRAME: function @anna_f | အပြည့်အဝ သိမြင်ခြင်း (2) |
| Aññā | FRAME: function @anna_f | တခြားစီ (1) |
| Aññe | FRAME: function @anna | တခြားစီ (1) |
| aññe | FRAME: function @anna | — |
| Aññāni | FRAME: function @anna | တခြားစီ (1) |
| hoti | FRAME: function @hoti | ဖြစ်သည် (14) |
| atthi | FRAME: ရှိသည် | ရှိသည် (25) |
| Atthi | FRAME: ရှိသည် | — |
| bhavati | FRAME: ဖြစ်သည် | ဖြစ်သည် (1) |
| puggala | STOCK: ပုဂ္ဂိုလ် | ပုဂ္ဂိုလ် (1) |
| puggalo | STOCK: ပုဂ္ဂိုလ် | ပုဂ္ဂိုလ် (63) |
| Puggalo | STOCK: ပုဂ္ဂိုလ် | ပုဂ္ဂိုလ် (67) |
| puggalassa | STOCK: ပုဂ္ဂိုလ် | ပုဂ္ဂိုလ် (18) |
| puggalā | STOCK: ပုဂ္ဂိုလ် | — |
| puggalaṃ | STOCK: ပုဂ္ဂိုလ် | — |
| puggalānaṃ | STOCK: ပုဂ္ဂိုလ် | ပုဂ္ဂိုလ် (5) |
| paññatti | STOCK: သတ်မှတ်ချက် | သတ်မှတ်ချက် (18) |
| paññatta | STOCK: သတ်မှတ်ချက် | သတ်မှတ်ချက် (4) |
| upādāya | STOCK: မှီ၍ | မှီ၍ (1) |
| upādā | STOCK: function @upada | စွဲလမ်းမှု (8); မှီ၍ (2) |
| nissāya | STOCK: မှီ၍ | မှီ၍ (1) |
| sandhāvati | STOCK: ကူးသွားသည် | ကူးသွားသည် (22) |
| sandhāvanti | STOCK: ကူးသွားသည် | — |
| upapajjati | STOCK: ပြန်လည် ဖြစ်ပေါ်သည် | ပြန်လည် ဖြစ်ပေါ်သည် (3) |
| paññāyati | STOCK: ထင်ရှားသည် | ထင်ရှားသည် (3) |
| cavati | STOCK: function @cavati | စုတေသည် (2) |
| cuto | STOCK: သေသော | သေသော (6) |
| kattā | STOCK: ပြုလုပ်သူ | ပြုလုပ်သူ (18) |
| kāretā | STOCK: ပြုလုပ်စေသူ | ပြုလုပ်စေသူ (18) |
| kattā kāretā | STOCK: ပြုလုပ်သူ … ပြုလုပ်စေသူ | ပြုလုပ်သူ … ပြုလုပ်စေသူ (18) |
| paṭisaṃvedī | STOCK: ခံစားသော | ခံစားသော (45) |
| vipākapaṭisaṃvedī | STOCK: အကျိုးကို ခံစားသော | အကျိုးကို ခံစားသော (16) |
| kārako | STOCK: ပြုသူ | ပြုသူ (7) |
| Kammakārako | STOCK: ကံကို ပြုသူ | ကံကို ပြုသူ (1) |
| kammakārako | STOCK: ကံကို ပြုသူ | ကံကို ပြုသူ (5) |
| paṭisaṃvedeti | STOCK: ခံစားသည် | ခံစားသည် (4) |
| paṭisaṃvedenti | STOCK: ခံစားသည် | ခံစားသည် (4) |
| karoti | STOCK: function @karoti | ပြုသည် (8); ပြုလုပ်သည် (1) |
| karonti | STOCK: function @karoti | ပြုသည် (4) |
| sukhadukkhaṃ | STOCK: ချမ်းသာနှင့် ဆင်းရဲ | ချမ်းသာနှင့် ဆင်းရဲ (5) |
| kalyāṇa | STOCK: ကောင်းမွန်သော | — |
| pāpakāni | STOCK: ယုတ်မာသော | ယုတ်မာသော (17) |
| pāpakānaṃ | STOCK: ယုတ်မာသော | ယုတ်မာသော (6) |
| Kalyāṇapāpakāni | STOCK: ကောင်းမွန်သော … ယုတ်မာသော | ကောင်းမွန်သော … ယုတ်မာသော (17) |
| Kalyāṇapāpakānaṃ | STOCK: ကောင်းမွန်သော … ယုတ်မာသော | ကောင်းမွန်သော … ယုတ်မာသော (6) |
| kammāni | STOCK: ကံ | ကံ (17) |
| kammānaṃ | STOCK: ကံ | ကံ (8) |
| vipāko | STOCK: အကျိုး | — |
| Vipāko | STOCK: အကျိုး | — |
| saṅkhato | STOCK: ပြုပြင်ဖန်တီးထားသော | ပြုပြင်ဖန်တီးထားသော (7) |
| asaṅkhato | STOCK: ပြုပြင်ဖန်တီးထားခြင်း မရှိသော | ပြုပြင်ဖန်တီးထားခြင်း မရှိသော (6) |
| sappaccayo | STOCK: အကြောင်း ရှိသော | အကြောင်း ရှိသော (2) |
| appaccayo | STOCK: အကြောင်း မရှိသော | — |
| sassato | STOCK: function @sassato | ထာဝရ တည်မြဲသော (5) |
| nimitto | STOCK: အမှတ်အသား ရှိသော | အမှတ်အသား ရှိသော (2) |
| animitto | STOCK: အမှတ်အသား မရှိသော | အမှတ်အသား မရှိသော (2) |
| vijjamāno | STOCK: ရှိနေသော | ရှိနေသော (1) |
| saṃvijjamāno | STOCK: ထင်ရှား ရှိနေသော | ထင်ရှား ရှိနေသော (1) |
| khayadhammaṃ | STOCK: ကုန်ခန်းတတ်သော သဘော … ရှိသော | ကုန်ခန်းတတ်သော သဘော … ရှိသော (3) |
| vayadhammaṃ | STOCK: ပျက်စီးတတ်သော သဘော … ရှိသော | ပျက်စီးတတ်သော သဘော … ရှိသော (3) |
| virāgadhammaṃ | STOCK: ပြယ်ပျောက်တတ်သော သဘော … ရှိသော | ပြယ်ပျောက်တတ်သော သဘော … ရှိသော (3) |
| nirodhadhammaṃ | STOCK: ချုပ်ငြိမ်းတတ်သော သဘော … ရှိသော | ချုပ်ငြိမ်းတတ်သော သဘော … ရှိသော (3) |
| vipariṇāmadhammaṃ | STOCK: ဖောက်ပြန်ပြောင်းလဲတတ်သော သဘော ရှိသော | ဖောက်ပြန်ပြောင်းလဲတတ်သော သဘော ရှိသော (3) |
| virāga | STOCK: function @viraga | ပြယ်ပျောက် (5) |
| sotāpanno | STOCK: သောတာပန် | သောတာပန် (2) |
| sakadāgāmī | STOCK: သကဒါဂါမ် | သကဒါဂါမ် (3) |
| anāgāmī | STOCK: အနာဂါမ် | အနာဂါမ် (3) |
| arahā | STOCK: ရဟန္တာ | ရဟန္တာ (2) |
| manusso | STOCK: လူ | လူ (8) |
| devo | STOCK: နတ် | နတ် (6) |
| hutvā | STOCK: ဖြစ်၍ | ဖြစ်၍ (14) |
| jīvaṃ | STOCK: အသက် | အသက် (6) |
| jīvo | STOCK: အသက် | အသက် (1) |
| sarīraṃ | STOCK: ကိုယ်ခန္ဓာ | ကိုယ်ခန္ဓာ (8) |
| rūpaṃ | STOCK: function @rupam | ရုပ် (14); အဆင်းအရောင် (3) |
| Rūpaṃ | STOCK: function @rupam | ရုပ် (12) |
| rūpa | STOCK: function @rupa | သိမ်မွေ့သော ရုပ် (4); အဆင်းအရောင် (3); ရုပ် (1) |
| dukkhaṃ | STOCK: function @dukkha | ဆင်းရဲ (16); နာကျင်သော (3); ဒုက္ခ (1) |
| Dukkhaṃ | STOCK: function @dukkha | ဒုက္ခ (1) |
| dukkha | STOCK: function @dukkha | ဆင်းရဲ (2); နာကျင်မှု (1) |
| sukhaṃ | STOCK: function @sukha | ချမ်းသာ (12); သာယာသော (4) |
| sukha | STOCK: function @sukha | ချမ်းသာ (7); သာယာမှု (1) |
| dhātuyā | STOCK: function @dhatuya | ဘုံ (6) |
| nibbānaṃ | STOCK: နိဗ္ဗာန် | — |
| Nibbānaṃ | STOCK: နိဗ္ဗာန် | — |
| nibbānassa | STOCK: နိဗ္ဗာန် | — |
| parinibbānaṃ | STOCK: ပရိနိဗ္ဗာန် ပြုခြင်း | ပရိနိဗ္ဗာန် ပြုခြင်း (8) |
| Parinibbuto | STOCK: ပရိနိဗ္ဗာန် ပြုပြီးသော | ပရိနိဗ္ဗာန် ပြုပြီးသော (1) |
| parinibbute | STOCK: ပရိနိဗ္ဗာန် ပြုတော်မူပြီးသော | ပရိနိဗ္ဗာန် ပြုတော်မူပြီးသော (1) |
| sayaṃ | STOCK: မိမိ | မိမိ (4) |
| para | STOCK: function @para | အခြားသူ (2); သူတစ်ပါး (1) |
| hitāya | STOCK: function @hitaya | အကျိုး (12); အကျိုးစီးပွား (1) |
| bhagavā | STOCK: မြတ်စွာဘုရား | မြတ်စွာဘုရား (8) |
| saccavādī | STOCK: မှန်သော စကားကို ဆိုတော်မူသော | မှန်သော စကားကို ဆိုတော်မူသော (8) |
| tathavādī | STOCK: ဟုတ်တိုင်း ဆိုတော်မူသော | ဟုတ်တိုင်း ဆိုတော်မူသော (8) |
| avitathavādī | STOCK: မမှားယွင်းဘဲ ဆိုတော်မူသော | မမှားယွင်းဘဲ ဆိုတော်မူသော (8) |
| anaññathavādī | STOCK: အခြားတစ်မျိုး မဆိုတော်မူသော | အခြားတစ်မျိုး မဆိုတော်မူသော (8) |
| sacca | STOCK: function @sacca | မှန်သော (8) |
| tatha | STOCK: ဟုတ်တိုင်း | ဟုတ်တိုင်း (8) |
| vitatha | STOCK: မှားယွင်း | မှားယွင်း (8) |
| aññatha | STOCK: အခြားတစ်မျိုး | အခြားတစ်မျိုး (8) |
| Khandhesu | STOCK: အစုအဝေး | အစုအဝေး (1) |
| khandhesu | STOCK: အစုအဝေး | အစုအဝေး (1) |
| Khandhā | STOCK: အစုအဝေး | အစုအဝေး (1) |
| jahati | STOCK: function @jahati | — |
| paṇidhi | STOCK: function @panidhi | — |
| uddānaṃ | STOCK: အကျဉ်းချုပ် | — |
| antarikā | STOCK: function @antarika | — |
| samodhānaṃ | STOCK: ပေါင်းဆုံခြင်း | — |
| vīta | STOCK: function @vita | — |
| bhāvito | STOCK: function @bhavito | — |
| bhāvitā | STOCK: function @bhavito | — |
| arahattā | STOCK: function @arahatta | — |
| arahatta | STOCK: function @arahatta | — |
| phalā | STOCK: function @phala | အသီးအပွင့် (2) |
| phala | STOCK: function @phala | — |
| phalaṃ | STOCK: function @phala | အသီးအပွင့် (2) |
| bojjha | STOCK: function @bojjha | — |
| aṅgā | STOCK: function @anga | — |
| gati | STOCK: function @gati | လားရာ (2) |
| taṇhā | STOCK: function @tanha | တဏှာ (1) |

## Values different from pi-1 … pi-4 for the same keyword

| keyword | pi-5 value (uses) | pi-1 … pi-4 values (uses) | reason |
|---|---|---|---|
| abhiññā | ထူးကဲစွာ သိခြင်း (2) | ထူးကဲစွာ သိ၍ (20); ထူးကဲစွာ သိရမည့် (1) | the heading noun «ထူးကဲစွာ သိခြင်း» (Abhiññānuyoga); pi-2 has the absolutive abhiññāya |
| anuyoga | စစ်ဆေးမေးမြန်းခြင်း (1) | (no direct equivalent) (6) | the heading word «စစ်ဆေးမေးမြန်းခြင်း» (Ñātakānuyogādi); pi-4 P4 (cognate object) does not apply |
| atthato | အဓိပ္ပာယ် (1) | အနှစ်သာရ ရှိသော (1) | «atthato ekaṃ» = «အဓိပ္ပာယ်အားဖြင့် တူသည်» (§6); pi-4 another sense |
| aññatra | အခြား (5) | လွဲ၍ (3) | «aññatra rūpā» = «ရုပ်မှ အခြား၌» (the text's word); pi-2 «လွဲ၍» another construction |
| Aññā | တခြားစီ (1) | အပြည့်အဝ သိမြင်ခြင်း (9) | the feminine «other» (aññaṃ … aññā vedanā), not aññā «final knowledge» |
| aṭṭhaka | ရှစ်ပါးအစု (2) | ရှစ်မျိုးတွဲ (7) | Aṭṭhakaniggaho = «ချေပချက် ရှစ်ပါးအစု» (§5); pi-2 «ရှစ်မျိုးတွဲ» is the table octad |
| bahiddhā | အပြင် (1) | ပြင်ပ၌ (45); မိမိ၏ ပြင်ပ၌ (35); သူတစ်ပါး၌ (12) | «bahiddhā nikkhamitvā» = «အပြင်သို့ ထွက်၍» (outside the body); pi-2 N10 is the qualifier «external» |
| bhagavā | မြတ်စွာဘုရား (8) | ဘုန်းတော်ရှင် (1) | the subject «မြတ်စွာဘုရား» (pi-1 bhagavato); pi-? «ဘုန်းတော်ရှင်» is the epithet in the iti pi so list |
| bhattaṃ | ထမင်း (1) | ဆွမ်းစား (1) | niccabhattaṃ «အမြဲ ထမင်း»; pi-? «ဆွမ်းစား» another compound |
| buddha | ဘုရား (1) | မြတ်စွာဘုရား (1) | «buddhuppāda» = «ဘုရား ပွင့်ပေါ်ခြင်း» (the text's word) |
| cakkhumā | မျက်စိ ရှိသော (1) | မျက်စိ ကောင်းသော (1) | my5-zeroshot-terms «cakkhumā puggalo = မျက်စိ ရှိသော ပုဂ္ဂိုလ်»; pi-4 «sharp-sighted» another sense |
| cakkhusamphasso | မျက်စိ တွေ့ထိမှု (1) | မျက်စိ၏ တွေ့ထိမှု (8) | the text has no genitive: «မျက်စိ တွေ့ထိမှု» |
| catukka | လေးပါး (2) | လေးမျိုးတွဲ (8); ဈာန် လေးပါး (2) | Catukkanaya = «နည်း လေးပါး» (the heading); pi-2 «လေးမျိုးတွဲ» is the tetrad |
| cavati | စုတေသည် (2) | သေသည် (2) | the text's «စုတေ» (my5-zeroshot-terms §7 cavati = စုတေ) |
| dhuvo | ခိုင်ခံ့သော (1) | ခိုင်မြဲသော (1) | the text's «ခိုင်ခံ့သော» |
| dukkhaṃ | ဆင်းရဲ (16) | နာကျင်မှု (24); ဒုက္ခ (17); ကိုယ်ဆင်းရဲခြင်း (2) | pain as the opposite of pleasure «ဆင်းရဲ» (sukhadukkha, āpāyika dukkha: my5-zeroshot-terms §7 / §8); f_dukkha keeps «ဒုက္ခ» / «နာကျင်သော» where the text has them |
| gati | လားရာ (2) | လားရာ ဘဝ (1) | the text's «လားရာ» (Gatianuyoga); pi-2 «လားရာ ဘဝ» is not in the segment |
| hitāya | အကျိုး (12); အကျိုးစီးပွား (1) | အစီးအပွား (1) | «attahitāya» = «မိမိ၏ အကျိုးအတွက်»; pi-? «အစီးအပွား» not in the segment |
| iddhiṃ | ဣဒ္ဓိ (2) | တန်ခိုး (1) | the text's «ဣဒ္ဓိ» (my5-zeroshot-terms §8) |
| jāto | မွေးဖွားလာသော (2) | မွေးဖွားသော (1) | the text's «မွေးဖွားလာ…» |
| jāyati | မွေးဖွားသည် (1) | ဖြစ်ပေါ်သည် (8) | «jāyati jīyati mīyati» = «မွေးဖွား၊ အို၊ သေဆုံး» (birth); pi-2 «ဖြစ်ပေါ်သည်» another sense |
| karitvā | (no direct equivalent) (2) | ပြု၍ (5) | «appiyaṃ karitvā» = «ဦးစားမပေးဘဲ»: one Burmese verb phrase renders appiyaṃ karitvā (pi-4 P4 / pi-1 caya) |
| karoti | ပြုသည် (8); ပြုလုပ်သည် (1) | (no direct equivalent) (1) | the text's verb (pi-4 had (no direct equivalent) where karoti stood only in a variant) |
| kathā | ဆွေးနွေးချက် (4) | ဆွေးနွေးခြင်း (3); စကား (1) | the heading word «ဆွေးနွေးချက်» (Xkathā = X အကြောင်း ဆွေးနွေးချက်, §2); «ဆွေးနွေးခြင်း» stays in the title |
| koci | တစ်စုံတစ်ယောက် (26) | တစ်စုံတစ်ရာ (1) | a person «တစ်စုံတစ်ယောက်» (§7); pi-2 «တစ်စုံတစ်ရာ» a thing |
| kumārikā | သူငယ်မ (1) | မိန်းကလေး (1) | the text's «သူငယ်မ» |
| lohitaṃ | အနီ (1) | သွေး (4) | the colour «အနီ»; pi-? «သွေး» (blood) another sense |
| manosamphasso | မနော တွေ့ထိမှု (1) | မနော၏ တွေ့ထိမှု (3) | likewise «မနော တွေ့ထိမှု» |
| micchā | မှားသည် (39) | မှားယွင်းသော (81) | Q6: the verdict «…ti micchā» = «မှားသည်»; the compound member keeps «မှားယွင်းသော» |
| Mānusakaṃ | လူ (6) | လူ့ (1) | the text's «လူတို့၏ ချမ်းသာ» (my5-zeroshot-terms); pi-2 «လူ့» is another compound |
| naya | နည်း (2) | ခွဲနည်း (1) | the text's «နည်း» (Catukkanaya); pi-3 M8 «ခွဲနည်း» was the pi-3 text's word |
| nicca | အမြဲ (1) | မြဲသော (2) | niccabhattaṃ «အမြဲ ထမင်း» (^5-238, first in the Pāli); «မြဲသော» elsewhere |
| nikkhamitvā | ထွက်၍ (1) | ထွက်ပြီး (1) | absolutive keeps «…၍» (pi-1), the text's «ထွက်၍» |
| paccaya | မှီသော (1) | အထောက်အပံ့ (4); ပစ္စည်း (1) | aparappaccaya «သူတစ်ပါးကို မမှီသော» (rule 8: the positive part «မှီသော») |
| pana | တစ်ဖန် (1) | (no direct equivalent) (2) | «Idha pana» = «တစ်ဖန် ဤလောက၌» (the text has a word; pi-4 had none) |
| para | အခြားသူ (2) | သူတစ်ပါး (15); ပရ (2) | paracittaṃ «အခြားသူ၏ စိတ်» (the text's word); «သူတစ်ပါး» stays for paraṅkāra |
| parama | အဆုံးစွန် (92) | အမြတ်ဆုံး (1) | the frame's «အဆုံးစွန်» (paramattha); pi-2 «အမြတ်ဆုံး» another sense |
| paṭiññāya | ဝန်ခံချက် (4) | ဝန်ခံခြင်း (1) | the text's noun «ဝန်ခံချက်» |
| puriso | ယောက်ျား (1) | အမျိုးသား (1); သူတော်ကောင်း (1) | the text's «ယောက်ျား» |
| puñjo | အစုအပုံ (1) | ပုံ (1) | the text's «အစုအပုံ» |
| pātubhavanti | ပေါ်ပေါက်သည် (1) | ထင်ရှားလာသည် (12) | the text's «ပေါ်ပေါက်» |
| Sabbattha | နေရာတိုင်း (2) | ဘုံ အားလုံး (2); (no direct equivalent) (2) | «everywhere» «နေရာတိုင်း» (my5-zeroshot-terms §7); pi-2 «in all planes» is another context |
| sacca | မှန်သော (8) | သစ္စာ (8); အမှန် (5) | saccavādī «မှန်သော စကားကို …»; the «အမှန်» of the segment belongs to saccikaṭṭha / vata, not sacca |
| sama | တူသော (2) | တပြိုင်နက် (2); ညီညီညွတ်ညွတ် (1) | samabhāge «အချိုး တူသော» (sama = «တူသော») |
| samasamo | အလွန် တူညီစွာ (1) | တန်းတူ ဖြစ်သော (1) | the text's «အလွန် တူညီစွာ» |
| sassato | ထာဝရ တည်မြဲသော (5) | ထာဝရ တည်မြဲသည် (11); ထာဝရ တည်သော (1) | the predicate adjective «ထာဝရ တည်မြဲသော» (rule 3; puggalo sassato); the view clause keeps «…သည်» |
| sayaṃ | မိမိ (4) | ကိုယ်တိုင် (14) | the text's «မိမိ» (sayaṃkataṃ) |
| Saṃkhittaṃ | အကျဉ်းချုပ် (7) | တွန့်ဆုတ်နေသော (2) | the editors' «(Saṃkhittaṃ)» = «(အကျဉ်းချုပ်)» (§3); pi-2 saṃkhittaṃ cittaṃ (contracted) is another sense |
| saṃvijjamāno | ထင်ရှား ရှိနေသော (1) | ထင်ရှား ရှိသော (5) | the text's «ထင်ရှား ရှိနေသော» |
| suddhika | ရိုးရိုး (2) | သက်သက် (12) | the heading «ရိုးရိုး နှိုင်းယှဉ်ခြင်း» |
| sukhāya | ချမ်းသာ (1) | သာယာသော (54); ချမ်းသာခြင်း (1) | bahujanasukhāya «လူအများ၏ ချမ်းသာအတွက်» (not feeling) |
| sāyati | လျက်သည် (2) | မြည်းသည် (4) | harmonise B2 F.SAYATI «လျက်» (pi-1 / pi-2 ^2-517 first); pi-1 ^1-608 «မြည်း» another passage |
| tasmā | သောကြောင့် (1) | ထို့ကြောင့် (1) | the text's «…သောကြောင့်» |
| taṇhā | တဏှာ (1) | တပ်မက်မှု (83) | the sutta's «တဏှာ နှောင်ကြိုး» (^5-75); «တပ်မက်မှု» elsewhere |
| tiṭṭhati | တည်သည် (2) | ရပ်တည်နေသည် (2) | the text's «တည်» |
| upacchedo | ပြတ်ခြင်း (8) | ပြတ်စဲခြင်း (2) | the text's «ပြတ်ခြင်း» |
| upapajjati | ပြန်လည် ဖြစ်ပေါ်သည် (3) | ရောက်ရသည် (1) | my5-zeroshot-terms §7 «ပြန်လည် ဖြစ်ပေါ်» |
| upapanno | ပြန်လည် ဖြစ်ပေါ်သော (2) | ရောက်ရှိသော (9); ပြည့်စုံသော (2); ရရှိသော (1) | likewise (devalokaṃ upapanno) |
| uppajjati | ပေါ်ပေါက်လာသည် (1) | ဖြစ်ပေါ်သည် (50); ဖြစ်ပေါ်လာသည် (1); ပွင့်ထွန်းတော်မူသည် (1) | ^5-230 «uppajjamāno uppajjati» = «ပေါ်ပေါက်လာ…» (CTX) |
| uppādo | ဖြစ်ခြင်း (2) | ဖြစ်ပေါ်မှု (20); ဖြစ်ပေါ်ခြင်း (1) | the text's «ဖြစ်ခြင်း» |
| upādā | စွဲလမ်းမှု (8); မှီ၍ (2) | မူလဓာတ်ကြီးများကို မှီ၍ ဖြစ်သော (64) | anupādāparinibbāna «စွဲလမ်းမှု မရှိဘဲ» (rule 8) / Upādāpaññatti «မှီ၍»; pi-1 upādā rūpa is another term |
| vata | အမှန်ပင် (54) | အကျင့်ဝတ် (24); (no direct equivalent) (1) | Q6: «vata re» «အမှန်ပင်»; the vow keeps pi-1 «အကျင့်ဝတ်» |
| vatthu | အငြင်းပွားရာ အကြောင်းအရာ (1) | အခြေခံ (19); အကြောင်းအရာ (2); အကြောင်း (2) | the book title member «အငြင်းပွားရာ အကြောင်းအရာ» (rule 7) |
| vedayitaṃ | ခံစားရမှု (1) | ခံစားရခြင်း (83) | the text's «ခံစားရမှု» |
| vipariṇāmadhammā | ဖောက်ပြန်ပြောင်းလဲတတ်သော သဘော ရှိသော (2) | ဖောက်ပြန်ခြင်း သဘော ရှိသော (1) | the text's «ဖောက်ပြန်ပြောင်းလဲတတ်သော သဘော ရှိသော» (= pi-2 vipariṇāmadhammaṃ) |
| virāga | ပြယ်ပျောက် (5) | ကင်းပြတ် (2); ပြယ်ပျောက်ခြင်း (2) | the list member «ပြယ်ပျောက်(တတ်သော)»; pi-2 «ပြယ်ပျောက်ခြင်း» not in the segment |
| vādī | ဆိုတော်မူသော (8); မိမိဘက် (1); တစ်ဖက်သား (1) | ပြောသော (5) | Q8 / the speakers' note «မိမိဘက် / တစ်ဖက်သား» (§6); pi-2 «ပြောသော» not in the segment |
| yaṃ | အကြင်အရာ (3) | (no direct equivalent) (107); ရှိသမျှ (56) | Q7 |
| yena | အကြင်အရာ (3) | (no direct equivalent) (1) | Q7 |
| yo | အကြင်သူ (3) | (no direct equivalent) (144); ရှိသမျှ (12); အကြင် (1) | Q7 |
| ṭhānaṃ | တည်ရာ (1) | အကြောင်း (2); နေရာ (1); ရပ်ခြင်း (1) | diṭṭhiṭṭhānaṃ «အယူ၏ တည်ရာ» (the text's word) |

## Presence: chunks matched by an ending rule (not literally in the segment)

Every other chunk occurs literally in its segment's Burmese. Counts per rule, with examples:

| rule | chunks | examples |
|---|---|---|
| verb | 239 | namo «ရှိခိုးသည်» ^T-1; oloketabbā «ကြည့်သည်» ^5-3; upalabbhati «တွေ့ရသည်» ^5-2; upalabbhati «တွေ့ရသည်» ^5-3; Ājānāhi «လက်ခံသည်» ^5-1; Ājānāhi «လက်ခံသည်» ^5-2 |
| attr | 233 | Dunniggahitā «ခံရသော» ^5-4; Dunniggahitā «ခံရသော» ^5-9; Suniggahito «ခံရသော» ^5-3; Suniggahito «ခံရသော» ^5-8; dassitā «ပြထားသော» ^5-1; dassitā «ပြထားသော» ^5-2 |
| abs | 10 | hutvā «ဖြစ်၍» ^5-77; hutvā «ဖြစ်၍» ^5-79; hutvā «ဖြစ်၍» ^5-81; hutvā «ဖြစ်၍» ^5-82; hutvā «ဖြစ်၍» ^5-83; sandhāvitvāna «ကူးသွား၍» ^5-74 |
| neg-abs | 5 | hutvā «ဖြစ်၍» ^5-199; hutvā «ဖြစ်၍» ^5-203; hutvā «ဖြစ်၍» ^5-204; hutvā «ဖြစ်၍» ^5-78; hutvā «ဖြစ်၍» ^5-80 |
| neg-verb | 3 | hoti «ဖြစ်သည်» ^5-199; hoti «ဖြစ်သည်» ^5-203; hoti «ဖြစ်သည်» ^5-204 |
| attr-fut | 2 | niggahetabbe «ချေပရမည့်» ^5-3; niggahetabbe «ချေပရမည့်» ^5-8 |

## (no direct equivalent)

| segment | keyword | why |
|---|---|---|
| ^5-3 | suniggahitova | only inside a Roman-script variant (pi-3 M2) |
| ^5-67 | karitvā | appiyaṃ karitvā = one verb phrase «ဦးစားမပေးဘဲ» (given to appiyaṃ) |
| ^5-68 | karitvā | appiyaṃ karitvā = one verb phrase «ဦးစားမပေးဘဲ» (given to appiyaṃ) |
| ^5-195 | Yo | the text builds the clause with «…သူ» (pi-1 rule) |
| ^5-196 | Yo | the text builds the clause with «…သူ» (pi-1 rule) |
| ^5-220 | Yo | the text builds the clause with «…သူ» (pi-1 rule) |
| ^5-224 | Yo | the text builds the clause with «…သူ» (pi-1 rule) |
| ^5-226 | ohacca | only inside a Roman-script variant |
| ^5-226 | uhacca | only inside a Roman-script variant |
| ^5-233 | sammati | only inside a Roman-script variant |

## Keyword → Burmese (preamble + ch1, number of uses)

Several values = the keyword reads differently by context (one sense per segment) or by construction.

| Pāli keyword | Burmese (uses) |
|---|---|
| abhidhamma | အဘိဓမ္မာ (1) |
| Abhidhammapiṭake | အဘိဓမ္မာပိဋက (1) |
| abhiññā | ထူးကဲစွာ သိခြင်း (2) |
| abyākatassa puggalassa | ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော ပုဂ္ဂိုလ် (2) |
| abyākatassa puggalassa paññatti | ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော ပုဂ္ဂိုလ်၏ သတ်မှတ်ချက် (2) |
| Abyākataṃ | ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော (2) |
| adhicca | အကြောင်းမဲ့ (2) |
| adukkhamasukhaṃ | မနာကျင် မသာယာသော (3) |
| adukkhamasukhaṃ vedanaṃ | မနာကျင် မသာယာသော ခံစားမှု (1) |
| adukkhamasukhā | မနာကျင် မသာယာသော (1) |
| akanta | မချစ်ခင်ဖွယ် (2) |
| akusalassa puggalassa | အကုသိုလ် ပုဂ္ဂိုလ် (2) |
| akusalassa puggalassa paññatti | အကုသိုလ် ပုဂ္ဂိုလ်၏ သတ်မှတ်ချက် (2) |
| Akusalaṃ | အကုသိုလ် (2) |
| akusale | အကုသိုလ် (2) |
| amanuñña | စိတ်နှင့် မတွေ့သော (2) |
| anamataggo | အစကို ရှာ၍ မတွေ့နိုင် (1) |
| anantara | နောက်ဆက်တွဲ (1) |
| anattā | အတ္တ မဟုတ်သော (1) |
| anaññathavādī | အခြားတစ်မျိုး မဆိုတော်မူသော (8) |
| aniccaṃ | မမြဲသော (3) |
| anicco | မမြဲသော (2) |
| aniccā | မမြဲသော (1) |
| anidassanaṃ | မမြင်နိုင်သော (1) |
| animitto | အမှတ်အသား မရှိသော (2) |
| aniṭṭha | မလိုလားဖွယ် (2) |
| anudiṭṭhiṃ | အယူ (1) |
| anukampāya | သနားခြင်း (1) |
| anuloma | အစဉ်အတိုင်း (5) |
| Anulomapaccanīkaṃ | အစဉ်အတိုင်းနှင့် ပြောင်းပြန် (4) |
| anulomaṃ | အစဉ်အတိုင်း (4) |
| anupassī | အဖန်ဖန် ရှုသော (4) |
| anussarati | အဖန်ဖန် အောက်မေ့သည် (2) |
| anuyoga | စစ်ဆေးမေးမြန်းခြင်း (1) |
| anuyogo | စစ်ဆေးမေးမြန်းခြင်း (16) |
| anāgāmī | အနာဂါမ် (3) |
| apamāriyo | ဝက်ရူး ပြန်သူ (2) |
| appaṭighassa | ထိခိုက်မှု မရှိသော (1) |
| appiyaṃ | ဦးစားမပေး (2) |
| arahato | ရဟန္တာ (1) |
| arahā | ရဟန္တာ (2) |
| arūpa | ရုပ်မရှိသော (4) |
| Arūpadhātuyā | ရုပ်မရှိသော ဘုံ (2) |
| arūpadhātuyā | ရုပ်မရှိသော ဘုံ (2) |
| asaṅkhataṃ | ပြုပြင်ဖန်တီးထားခြင်း မရှိသော (3) |
| asaṅkhato | ပြုပြင်ဖန်တီးထားခြင်း မရှိသော (6) |
| Asaṅkhatānaṃ dhammānaṃ | ပြုပြင်ဖန်တီးထားခြင်း မရှိသော သဘောတရား (1) |
| asecanaka | မရောနှောသော (2) |
| atikkanta | ကျော်လွန်သော (2) |
| atipāto | သတ်ခြင်း (2) |
| atta | အတ္တ (1) |
| attani | အတ္တ (1) |
| attaniyaṃ | အတ္တနှင့် ဆိုင်သော အရာ (1) |
| attaniyena | အတ္တနှင့် ဆိုင်သော အရာ (1) |
| attena | အတ္တ (1) |
| atthato | အဓိပ္ပာယ် (1) |
| atthatthamhi | ရှိခြင်း သဘော (1) |
| atthena | အနက် (92) |
| atthi | ရှိသည် (25) |
| attānaṃ | အတ္တ (1) |
| avayava | အစိတ်အပိုင်း (2) |
| avekkhantaṃ | ရှုမြင်နေသော (1) |
| avekkhassu | ရှုမြင်သည် (1) |
| avekkhati | ရှုမြင်သည် (2) |
| avijjā | အမှန်ကို မသိမှု (1) |
| avitathavādī | မမှားယွင်းဘဲ ဆိုတော်မူသော (8) |
| aññatha | အခြားတစ်မျိုး (8) |
| aññatra | အခြား (5) |
| Aññaṃ | တခြားစီ (15) |
| aññaṃ | တခြားစီ (9) |
| aññaṃ aññe saṅkhārā | ပြုပြင်ဖန်တီးမှု … တခြားစီ (1) |
| aññaṃ aññā vedanā | ခံစားမှု … တခြားစီ (2) |
| Aññaṃ rūpaṃ | ရုပ် … တခြားစီ (3) |
| aññaṃ rūpaṃ | ရုပ် … တခြားစီ (7) |
| Aññaṃ viññāṇaṃ | သိစိတ် … တခြားစီ (3) |
| aññaṃ viññāṇaṃ | သိစိတ်သည် တခြားစီ (1); သိစိတ် … တခြားစီ (1) |
| Aññe | တခြားစီ (1) |
| aññindriyaṃ | အပြည့်အဝ သိမြင်ခြင်း၏ စွမ်းရည် (4) |
| Añño | တခြားစီ (5) |
| añño | တခြားစီ (3); တခြား (2); အခြား (2) |
| aññā | အပြည့်အဝ သိမြင်ခြင်း (2) |
| Aññā | တခြားစီ (1) |
| Aññā vedanā | ခံစားမှု … တခြားစီ (1) |
| Aññāni | တခြားစီ (1) |
| aññāta | သိရသော (1) |
| aññātāvī | အပြည့်အဝ သိမြင်ပြီးသူ (6) |
| aññātāvī upalabbhati | အပြည့်အဝ သိမြင်ပြီးသူ၏ စွမ်းရည် … တွေ့ရသည် (4) |
| aḷa | လက်မ (2) |
| aṅga | အင်္ဂါ (1) |
| aṅguli | လက်ချောင်း (2) |
| aṭṭha | အရာ (1) |
| aṭṭhaka | ရှစ်ပါးအစု (2) |
| aṭṭhamaṃ | အဋ္ဌမ (1) |
| aṭṭhe | အနက် တူသော (2) |
| aṭṭho | အရာ (9) |
| Aṭṭhārasannaṃ | ဆယ့်ရှစ်ပါး (1) |
| bahiddhā | အပြင် (1) |
| bahūsu | အများစု (2) |
| bhagavantaṃ | မြတ်စွာဘုရား (1) |
| bhagavato | မြတ်စွာဘုရား (2) |
| bhagavatā | မြတ်စွာဘုရား (19) |
| bhagavā | မြတ်စွာဘုရား (8) |
| bhaginī | ညီအစ်မ (3) |
| bhante | အသျှင်ဘုရား (2) |
| bhattaṃ | ထမင်း (1) |
| bhavati | ဖြစ်သည် (1) |
| bhavaṃ | ဘဝ (1) |
| Bhavaṃ | ဘဝ (1) |
| bhijjamānesu | ပြိုကွဲကြသော (1) |
| bhijjati | ပြိုကွဲသည် (1) |
| bhikkhave | ရဟန်း (8) |
| bhikkhunī | ဘိက္ခုနီ (1) |
| bhāga | နှစ်ဖက်စလုံး (2) |
| bhātā | ညီအစ်ကို (3) |
| brāhmaṇo | ပုဏ္ဏား (7) |
| buddha | ဘုရား (1) |
| buddhena | ဘုရားရှင် (1) |
| bāla | လူမိုက် (1) |
| Bāvīsatīnaṃ | နှစ်ဆယ့်နှစ်ပါး (1) |
| cakkhu | မျက်စိ (17) |
| Cakkhudhātu | မျက်စိ ဓာတ် (6) |
| Cakkhudhātuṃ | မျက်စိ ဓာတ် (1) |
| cakkhumā | မျက်စိ ရှိသော (1) |
| Cakkhundriyaṃ | မျက်စိ၏ စွမ်းရည် (7) |
| Cakkhundriyaṃ upalabbhati | မျက်စိ၏ စွမ်းရည် … တွေ့ရသည် (3) |
| cakkhunā | မျက်စိ (4) |
| cakkhusamphasso | မျက်စိ တွေ့ထိမှု (1) |
| cakkhuviññāṇa | မျက်စိ သိစိတ် (2) |
| cakkhuviññāṇaṃ | မျက်စိ သိစိတ် (1) |
| Cakkhuṃ | မျက်စိ (2) |
| cakkhāyatanaṃ | မျက်စိ အာရုံခံ နယ်ပယ် (2) |
| Cakkhāyatanaṃ | မျက်စိ အာရုံခံ နယ်ပယ် (5) |
| catukka | လေးပါး (2) |
| catuvokāra | အစုအဝေး လေးပါး ရှိသော (1) |
| Catuvokārabhavaṃ | အစုအဝေး လေးပါး ရှိသော ဘဝ (1) |
| cavamāne | သေဆဲ (2) |
| cavati | စုတေသည် (2) |
| Chaṭṭho | ဆဋ္ဌမ (1) |
| chinno hoti | ပြတ်သူ … ဖြစ်သည် (2) |
| chāyāya | အရိပ် (1) |
| cittaṃ | စိတ် (3) |
| Citte | စိတ် (1) |
| citte | စိတ် (3) |
| citte uppanne | စိတ် ဖြစ်ပေါ်သော (2) |
| Cittena | စိတ် (1) |
| cuto | သေသော (6) |
| dassitā | ပြထားသော (2) |
| deva | နတ် (3) |
| devo | နတ် (6) |
| dha | “ဓမ္မပဒ” (1) |
| dhamma | သဘောတရား (12) |
| dhammadhātu | သဘောတရား ဓာတ် (6) |
| dhammadhātu upalabbhati | သဘောတရား ဓာတ် … တွေ့ရသည် (4) |
| dhammadhātuṃ | သဘောတရား ဓာတ် (1) |
| dhammapade | “ဓမ္မပဒ”၌ (1) |
| dhamme | ဘဝ (1) |
| dhammesu | သဘောတရား (2) |
| dhammesu dhammānupassī | သဘောတရားတို့၌ သဘောတရားကို အဖန်ဖန် ရှုသော (3) |
| dhammo | သဘော ရှိသော (1) |
| dhammā | သဘောတရား (2) |
| dhammānaṃ | သဘောတရား (2) |
| dhammānupassī | သဘောတရားကို အဖန်ဖန် ရှုသော (3) |
| dhammānupassī viharati | သဘောတရားကို အဖန်ဖန် ရှုသူ ဖြစ်လျက် နေသည် (1) |
| dhammānusārī | တရားကို အစဉ်လိုက်သူ (2) |
| dhammāyatanaṃ | သဘောတရား အာရုံခံ နယ်ပယ် (7) |
| dhammāyatanaṃ puggalo | သဘောတရား အာရုံခံ နယ်ပယ်သည် ပုဂ္ဂိုလ် (2) |
| dhammāyatanaṃ upalabbhati | သဘောတရား အာရုံခံ နယ်ပယ် … တွေ့ရသည် (4) |
| dhuva | အမြဲ (1) |
| dhuvo | ခိုင်ခံ့သော (1) |
| dhātu | ဓာတ် (8) |
| dhātu upalabbhati | ဓာတ် … တွေ့ရသည် (4) |
| dhātuyo | ဓာတ် (1) |
| dhātuyā | ဘုံ (6) |
| dhātuṃ | ဓာတ် (1) |
| dhātūnaṃ | ဓာတ် (1) |
| Dibbassa paṭisaṃvedī | နတ် … ခံစားသော (1) |
| dibbassa paṭisaṃvedī | နတ် … ခံစားသော (5) |
| Dibbassa sukhassa paṭisaṃvedī | နတ်တို့၏ ချမ်းသာကို ခံစားသော (1) |
| dibbassa sukhassa paṭisaṃvedī | နတ်တို့၏ ချမ်းသာကို ခံစားသော (5) |
| Dibbaṃ | နတ် (6) |
| Dibbaṃ sukhaṃ | နတ်တို့၏ ချမ်းသာ (6) |
| Dibbaṃ sukhaṃ upalabbhati | နတ်တို့၏ ချမ်းသာကို တွေ့ရသည် (6) |
| dibbena | နတ် (2) |
| dibbena cakkhunā | နတ်မျက်စိ (4) |
| dibbāya | နတ် (2) |
| dibbāya sotadhātuyā | နတ်နား ဓာတ် (2) |
| diṭṭhe dhamme | မျက်မှောက်ဘဝ (1) |
| diṭṭhi | အယူ (6) |
| diṭṭhigataṃ | အယူမှား (1) |
| diṭṭhiṃ | အယူ (2) |
| domanassa | စိတ်ဆင်းရဲမှု (1) |
| dubbaṇṇe | အဆင်း ဆိုးသော (2) |
| duggate | ဆိုးသော လားရာ ရှိသော (2) |
| dukkaṭe | မကောင်းစွာ ပြုခဲ့သော (2) |
| dukkha | ဆင်းရဲ (2); နာကျင်မှု (1) |
| dukkhassa | ဒုက္ခ (9) |
| dukkhassa antakiriyā | ဒုက္ခ၏ အဆုံးကို ပြုခြင်း (8) |
| dukkhassa paṭisaṃvedī | ဆင်းရဲကို ခံစားသော (11) |
| dukkhassanta | ဒုက္ခ၏ အဆုံး (1) |
| dukkhaṃ | ဆင်းရဲ (16); နာကျင်သော (3); ဒုက္ခ (1) |
| Dukkhaṃ | ဒုက္ခ (1) |
| dukkhaṃ vedanaṃ | နာကျင်သော ခံစားမှု (2) |
| dukkhā | နာကျင်သော (1) |
| dukkhā vedanā | နာကျင်သော ခံစားမှု (1) |
| dunniggahite | မကောင်းစွာ ချေပခြင်း (2) |
| Dunniggahitā | မကောင်းစွာ ချေပခြင်း ခံရသော (2) |
| Dvādasannaṃ | ဆယ့်နှစ်ပါး (1) |
| ekavokāra | အစုအဝေး တစ်ပါး ရှိသော (1) |
| Ekavokārabhavaṃ | အစုအဝေး တစ်ပါး ရှိသော ဘဝ (1) |
| Ettāvatā | ဤမျှဖြင့် (1) |
| eva | ပင် (11); သာ (2) |
| gadrabho | မြည်း (3) |
| gahaṭṭho | လူဝတ်ကြောင် (4) |
| gandha | အနံ့ (2) |
| gandhā | အနံ့ (1) |
| gandhāyatanaṃ | အနံ့ အာရုံခံ နယ်ပယ် (1) |
| gati | လားရာ (2) |
| gaṇḍiyo | အကျိတ်အနာ ရှိသူ (2) |
| ghāna | နှာခေါင်း (3) |
| ghānaviññāṇa | နှာခေါင်း သိစိတ် (1) |
| ghānaṃ | နှာခေါင်း (2) |
| ghānindriyaṃ | နှာခေါင်း၏ စွမ်းရည် (1) |
| ghānāyatanaṃ | နှာခေါင်း အာရုံခံ နယ်ပယ် (1) |
| ghāyati | နမ်းသည် (2) |
| gāmaṃ | ရွာ (1) |
| gāmikassa | ရွာသား (1) |
| hattha | လက် (2) |
| hatthako | လက် (2) |
| hetāya | ထို (4) |
| hevameva | ဤနည်းအတိုင်းပင် (1) |
| hevaṃ | ဤသို့ (2) |
| hitāya | အကျိုး (12); အကျိုးစီးပွား (1) |
| hoti | ဖြစ်သည် (14) |
| hutvā | ဖြစ်၍ (14) |
| iddhi | ဣဒ္ဓိ (1) |
| iddhiṃ | ဣဒ္ဓိ (2) |
| indriyaṃ | စွမ်းရည် (8) |
| indriyaṃ upalabbhati | စွမ်းရည် … တွေ့ရသည် (3) |
| indriyānaṃ | စွမ်းရည် (1) |
| itivu | “ဣတိဝုတ်” (1) |
| itivuttake | “ဣတိဝုတ်” (1) |
| itthi | မိန်းမ (1) |
| itthī | မိန်းမ (1) |
| iṭṭha | လိုလားဖွယ် (2) |
| jivhaṃ | လျှာ (1) |
| jivhindriyaṃ | လျှာ၏ စွမ်းရည် (1) |
| jivhā | လျှာ (4) |
| jivhāviññāṇa | လျှာ သိစိတ် (1) |
| jivhāyatanaṃ | လျှာ အာရုံခံ နယ်ပယ် (1) |
| jāte | တစ်မျိုးတည်းမှ ဖြစ်သော (2) |
| jāto | မွေးဖွားလာသော (2) |
| jāyati | မွေးဖွားသည် (1) |
| jīvaṃ | အသက် (6) |
| jīvita | အသက် (1) |
| jīvitindriyaṃ | အသက်၏ စွမ်းရည် (1) |
| jīvo | အသက် (1) |
| jīyati | အိုသည် (1) |
| kalyāṇa kāretā | ကောင်းမွန်သော … ပြုလုပ်စေသူ (17) |
| kalyāṇa vipāko | ကောင်းမွန်သော … အကျိုး (6) |
| Kalyāṇapāpakānaṃ | ကောင်းမွန်သော … ယုတ်မာသော (6) |
| Kalyāṇapāpakāni | ကောင်းမွန်သော … ယုတ်မာသော (17) |
| kamma | ကံ (2) |
| Kammakārako | ကံကို ပြုသူ (1) |
| kammakārako | ကံကို ပြုသူ (5) |
| kammavipāko | ကံ၏ အကျိုး (2) |
| Kammaṃ atthi | ကံ ရှိသည် (6) |
| kammānaṃ | ကံ (8) |
| kammānaṃ upalabbhati | ကံ … တွေ့ရသည် (6) |
| kammāni | ကံ (17) |
| kammāni upalabbhanti | ကံတို့ကို တွေ့ရသည် (17) |
| kanta | ချစ်ခင်ဖွယ် (2) |
| karitvā | (no direct equivalent) (2) |
| karo | ပြုသော (1) |
| karonti | ပြုသည် (4) |
| karoti | ပြုသည် (8); ပြုလုပ်သည် (1) |
| kataṃ dukkhaṃ | ဆင်းရဲ … ပြုထားသော (3) |
| kathā | ဆွေးနွေးချက် (4); ဆွေးနွေးခြင်း (1) |
| kathāvatthu | အငြင်းပွားရာ အကြောင်းအရာများကို ဆွေးနွေးခြင်း (1) |
| kattā | ပြုလုပ်သူ (18) |
| kattā kāretā | ပြုလုပ်သူ … ပြုလုပ်စေသူ (18) |
| katānaṃ | ပြုခဲ့သော (2) |
| kaṅkhati | သံသယ ဖြစ်သည် (1) |
| kaṇḍara | အကြော (2) |
| kaṇṇa | နား (2) |
| kaṭṭha | ထင်း (8) |
| kaṭṭhavanappatayo | ထင်း … သစ်ပင် (8) |
| kehici | အချို့ (5) |
| kehici puggalo | အချို့အားဖြင့် ပုဂ္ဂိုလ် (5) |
| kevalo | သက်သက် (1) |
| Khandhesu | အစုအဝေး (1) |
| khandhesu | အစုအဝေး (1) |
| Khandhā | အစုအဝေး (1) |
| khandhānaṃ | အစုအဝေး (1) |
| khattiyo | မင်းမျိုး (8) |
| khattu | ကြိမ် (1) |
| khaya | ကုန်ခန်း (5) |
| khayadhammaṃ | ကုန်ခန်းတတ်သော သဘော … ရှိသော (3) |
| khayadhammo | ကုန်ခန်းတတ်သော သဘော … ရှိသော (1) |
| khayadhammā | ကုန်ခန်းတတ်သော သဘော … ရှိသော (1) |
| khayaṃ | ကုန်ခန်းခြင်း (2) |
| khayā | ကုန်ခန်းခြင်း (1) |
| khīra | နွားနို့ (1) |
| kilāsiyo | အရေပြား အဖြူကွက် ရောဂါ ရှိသူ (2) |
| Kinnu | အဘယ်ကြောင့် (1) |
| koci | တစ်စုံတစ်ယောက် (26) |
| kosakaṃ | ခွက် (1) |
| koṭi | အစွန်း (2) |
| kumbho | အိုး (2) |
| kumārako | သူငယ် (1) |
| kumārikā | သူငယ်မ (1) |
| kusala | ကုသိုလ် (2) |
| kusalassa puggalassa | ကုသိုလ် ပုဂ္ဂိုလ် (2) |
| kusalassa puggalassa paññatti | ကုသိုလ် ပုဂ္ဂိုလ်၏ သတ်မှတ်ချက် (2) |
| Kusalaṃ | ကုသိုလ် (2) |
| kusalākusale | ကုသိုလ်နှင့် အကုသိုလ် (2) |
| kuṇi | ကောက်သော (2) |
| kuṭṭhiyo | နူနာ စွဲသူ (2) |
| kāma | ကာမ (4) |
| Kāmadhātuyā | ကာမဘုံ (4) |
| kāmino | ကာမ ရှိသော (2) |
| kāmī | ကာမ ရှိသော (2) |
| kārako | ပြုသူ (7) |
| kāraṃ dukkhaṃ | ဆင်းရဲ … ပြုသော (1) |
| kāraṇena | အကြောင်း (12) |
| kāretā | ပြုလုပ်စေသူ (18) |
| kāya | ကိုယ် (4) |
| kāyasakkhi | ကိုယ်ဖြင့် မျက်မှောက်ပြုသူ (2) |
| kāyaviññāṇa | ကိုယ် သိစိတ် (1) |
| kāyaṃ | ကိုယ် (1) |
| kāye | ကိုယ် (3) |
| kāyindriyaṃ | ကိုယ်၏ စွမ်းရည် (1) |
| Kāyo | ကိုယ် (2) |
| kāyo | ကိုယ် (1) |
| kāyānupassī | ကိုယ်ကို အဖန်ဖန် ရှုသော (3) |
| kāyānupassī viharati | ကိုယ်ကို အဖန်ဖန် ရှုသူ ဖြစ်လျက် နေသည် (3) |
| kāyāyatanaṃ | ကိုယ် အာရုံခံ နယ်ပယ် (1) |
| lakkhaṇa | လက္ခဏာ (2) |
| lakkhaṇena | အမှတ်အသား (2) |
| lakkhaṇāni | လက္ခဏာ (2) |
| lohitakaṃ | အနီ (1) |
| lohitaṃ | အနီ (1) |
| lokā upapanno | လောက … ပြန်လည် ဖြစ်ပေါ်သော (2) |
| maccu | သေမင်း (1) |
| madhu | ပျားရည် (1) |
| mahiso | ကျွဲ (1) |
| mahiṃso | ကျွဲ (4) |
| Mahāpathavī upalabbhati | မြေကြီးကို တွေ့ရသည် (6) |
| Mahāsamuddo upalabbhati | သမုဒ္ဒရာကို တွေ့ရသည် (1) |
| mahāsamuddo upalabbhati | သမုဒ္ဒရာကို တွေ့ရသည် (5) |
| mana | မနော (4) |
| manaṃ | မနော (1) |
| manindriyaṃ | မနော၏ စွမ်းရည် (1) |
| mano | မနော (2) |
| manosamphasso | မနော တွေ့ထိမှု (1) |
| manoviññāṇa | မနော သိစိတ် (4) |
| manoviññāṇaṃ | မနော သိစိတ် (1) |
| manussa | လူ (2) |
| manussalokā | လူ့လောက (2) |
| manusso | လူ (8) |
| manussānaṃ | လူ (1) |
| manuñña | စိတ်နှင့် တွေ့သော (2) |
| manāyatanaṃ | မနော အာရုံခံ နယ်ပယ် (3) |
| maraṇaṃ | သေခြင်း (2) |
| micchā | မှားသည် (39); မှားယွင်းသော (1) |
| micchādiṭṭhiyo puggalo | မှားယွင်းသော အယူ ရှိသော ပုဂ္ဂိုလ် (1) |
| Micchādiṭṭhiṃ | မှားယွင်းသော အယူ (1) |
| Micchādiṭṭhiṃ upādāya | မှားယွင်းသော အယူကို မှီ၍ (1) |
| Mānusakassa paṭisaṃvedī | လူ … ခံစားသော (1) |
| mānusakassa paṭisaṃvedī | လူ … ခံစားသော (5) |
| Mānusakassa sukhassa paṭisaṃvedī | လူတို့၏ ချမ်းသာကို ခံစားသော (1) |
| mānusakassa sukhassa paṭisaṃvedī | လူတို့၏ ချမ်းသာကို ခံစားသော (5) |
| Mānusakaṃ | လူ (6) |
| Mānusakaṃ sukhaṃ | လူတို့၏ ချမ်းသာ (6) |
| Mānusakaṃ sukhaṃ upalabbhati | လူတို့၏ ချမ်းသာကို တွေ့ရသည် (6) |
| mānusakena | လူ၏ မျက်စိ (2) |
| mātā | အမိ (1) |
| Mātā | အမိ (2) |
| mātā atthi | အမိ ရှိသည် (1) |
| Mātā atthi | အမိ ရှိသည် (2) |
| māṇava | လုလင် (1) |
| mīyati | သေဆုံးသည် (1) |
| namo | ရှိခိုးသည် (1) |
| Nanu | မဟုတ်လော (25) |
| naya | နည်း (2) |
| negaḷiko | သံခြေချင်း ခတ်ထားသူ (1) |
| Nerayikaṃ | ငရဲ (5) |
| Nerayikaṃ dukkhaṃ | ငရဲ၏ ဆင်းရဲ (5) |
| Nerayikaṃ upalabbhati | ငရဲ … တွေ့ရသည် (5) |
| nerayiko | ငရဲသား (1) |
| nibbānassa paṭisaṃvedī | နိဗ္ဗာန်ကို ခံစားသော (6) |
| nibbānassa paṭisaṃvedī atthi | နိဗ္ဗာန်ကို ခံစားသော … ရှိသည် (1) |
| nibbānassa paṭisaṃvedī upalabbhati | နိဗ္ဗာန်ကို ခံစားသော … တွေ့ရသည် (5) |
| nibbānaṃ asaṅkhataṃ | နိဗ္ဗာန်သည် ပြုပြင်ဖန်တီးထားခြင်း မရှိသော အရာ ဖြစ်သည် (2) |
| Nibbānaṃ atthi | နိဗ္ဗာန် ရှိသည် (2) |
| Nibbānaṃ upalabbhati | နိဗ္ဗာန်ကို တွေ့ရသည် (6) |
| nicca | အမြဲ (1) |
| nicco | မြဲသော (1) |
| niddesa | ဖွင့်ဆိုချက် (1) |
| nigaḷo | သံခြေချင်း (1) |
| niggaha | ချေပချက် (2) |
| niggahaṃ | ချေပချက် (22) |
| niggahetabbe | ချေပရမည့် (2); ချေပရသည် (2) |
| niggahetabbā | ချေပရသည် (2) |
| niggahite | ချေပခြင်း (2) |
| niggamana | နိဂုံးချုပ်ချက် (2) |
| niggaṇhāma | ချေပသည် (2) |
| niggaṇhāsi | ချေပသည် (4) |
| nikkhamitvā | ထွက်၍ (1) |
| nimitto | အမှတ်အသား ရှိသော (2) |
| nirodha | ချုပ်ငြိမ်း (5) |
| nirodhadhammaṃ | ချုပ်ငြိမ်းတတ်သော သဘော … ရှိသော (3) |
| nirodhadhammo | ချုပ်ငြိမ်းတတ်သော သဘော … ရှိသော (1) |
| nirodhadhammā | ချုပ်ငြိမ်းတတ်သော သဘော … ရှိသော (1) |
| niruddhe | ချုပ်ငြိမ်းသွားသော (1) |
| niruddhāya | ချုပ်ငြိမ်းသွားသော (2) |
| nirujjhamānaṃ | ချုပ်ငြိမ်းသော (1) |
| nirujjhati | ချုပ်ငြိမ်းသည် (2) |
| nissāya | မှီ၍ (1) |
| nivāsaṃ | ဘဝ (2) |
| niṭṭhitā | ပြီးဆုံးသော (1) |
| nānaṃ | ကွဲပြားသည် (1) |
| nāsa | နှာခေါင်း (2) |
| Nāññatra | တစ်ပါး (1) |
| Nīlaṃ | အပြာ (1) |
| nīlaṃ | အပြာ (1) |
| nīvaraṇānaṃ | အတားအဆီး (1) |
| odātaṃ | အဖြူ (2) |
| ohacca | (no direct equivalent) (1) |
| okāsa | နေရာ (2) |
| oloketabbā | ကြည့်သည် (1) |
| opamma | ဥပမာ (2) |
| oṭṭho | ကုလားအုတ် (3) |
| pabbajito | ရဟန်း (4) |
| pabbata | တောင် (8) |
| paccanīka | ပြောင်းပြန် (5) |
| paccanīkaṃ | ပြောင်းပြန် (4) |
| Paccanīkānulomaṃ | ပြောင်းပြန်နှင့် အစဉ်အတိုင်း (4) |
| paccaya | မှီသော (1) |
| paccayā | ကြောင့် (1) |
| paccesi | ယုံကြည်သည် (1) |
| pajānāmi | ကွဲပြားစွာ သိသည် (2) |
| pajānāti | ကွဲပြားစွာ သိသည် (4) |
| pana | တစ်ဖန် (1) |
| para | အခြားသူ (2); သူတစ်ပါး (1) |
| parama | အဆုံးစွန် (92) |
| paramatthena | အဆုံးစွန် အနက် (92) |
| paramattho | အဆုံးစွန် အရာ (10) |
| parinibbute | ပရိနိဗ္ဗာန် ပြုတော်မူပြီးသော (1) |
| Parinibbuto | ပရိနိဗ္ဗာန် ပြုပြီးသော (1) |
| parinibbānaṃ | ပရိနိဗ္ဗာန် ပြုခြင်း (8) |
| paripūro | ပြည့်စုံသော (1) |
| pathavī | မြေ (8) |
| pathavī atthi | မြေ … ရှိသည် (2) |
| pathavī upalabbhati | မြေ … တွေ့ရသည် (6) |
| patto | ရောက်သော (2) |
| pañcamaṃ | ပဉ္စမ (1) |
| Pañcamo | ပဉ္စမ (1) |
| pañcavokāra | အစုအဝေး ငါးပါး ရှိသော (1) |
| Pañcavokārabhavaṃ | အစုအဝေး ငါးပါး ရှိသော ဘဝ (1) |
| paññatta | သတ်မှတ်ချက် (4) |
| paññatti | သတ်မှတ်ချက် (18) |
| paññindriyaṃ | ပညာ၏ စွမ်းရည် (1) |
| paññā | ပညာ (3) |
| paññāpeti | ပညတ်သည် (1) |
| paññāyati | ထင်ရှားသည် (3) |
| paṭicca | အကြောင်းတို့ကို မှီ၍ (5) |
| paṭiccasamuppannaṃ | အကြောင်းတို့ကို မှီ၍ ဖြစ်ပေါ်လာသော (3) |
| paṭiccasamuppanno | အကြောင်းတို့ကို မှီ၍ ဖြစ်ပေါ်လာသော (1) |
| paṭiccasamuppannā | အကြောင်းတို့ကို မှီ၍ ဖြစ်ပေါ်လာသော (1) |
| paṭihaññati | ထိခိုက်သည် (1) |
| paṭijānantaṃ | ဝန်ခံနေသော (2) |
| paṭijānantā | ဝန်ခံနေသော (2) |
| paṭikammaṃ | ပြန်လှန် ချေပချက် (11) |
| paṭikamme | ပြန်လှန် ချေပချက် (2) |
| paṭipanno | ကျင့်ကြံသော (12) |
| paṭipādanā | ဆက်စပ် တင်ပြချက် (2) |
| paṭisaṃvedenti | ခံစားသည် (4) |
| paṭisaṃvedeti | ခံစားသည် (4) |
| paṭisaṃvedī | ခံစားသော (45) |
| paṭivedha | ထိုးထွင်း သိမြင်ခြင်း (2) |
| Paṭivedhānuyogo | ထိုးထွင်း သိမြင်ခြင်းကို စစ်ဆေးမေးမြန်းခြင်း (2) |
| paṭiññāya | ဝန်ခံချက် (4) |
| pecca | သေပြီးနောက် (1) |
| peto | ပြိတ္တာ (1) |
| peyyālā | အကျဉ်းချုံ့ချက် (1) |
| phalaṃ | အသီးအပွင့် (2) |
| phalā | အသီးအပွင့် (2) |
| phaṇa | လက်ချောင်းများ ကပ်နေသော (2) |
| phoṭṭhabba | အထိအတွေ့ (3) |
| phoṭṭhabbā | အထိအတွေ့ (1) |
| phoṭṭhabbāyatanaṃ | အထိအတွေ့ အာရုံခံ နယ်ပယ် (1) |
| phusati | ထိသည် (2) |
| phāṇita | တင်လဲ (1) |
| pitā | အဖ (3) |
| pucchā | အမေး (3) |
| puggala | ပုဂ္ဂိုလ် (1) |
| puggalassa | ပုဂ္ဂိုလ် (18) |
| Puggalassa | ပုဂ္ဂိုလ် (2) |
| puggalassa paññatti | ပုဂ္ဂိုလ်၏ သတ်မှတ်ချက် (17); ပုဂ္ဂိုလ် … သတ်မှတ်ချက် (1) |
| puggalassa paṭisaṃvedī | ပုဂ္ဂိုလ်ကို ခံစားသော (6) |
| Puggalo | ပုဂ္ဂိုလ် (67) |
| puggalo | ပုဂ္ဂိုလ် (63) |
| puggalo animitto | ပုဂ္ဂိုလ်သည် အမှတ်အသား မရှိသော အရာ (2) |
| puggalo asaṅkhato | ပုဂ္ဂိုလ်သည် ပြုပြင်ဖန်တီးထားခြင်း မရှိသော အရာ (3) |
| Puggalo asaṅkhato | ပုဂ္ဂိုလ်သည် ပြုပြင်ဖန်တီးထားခြင်း မရှိသော အရာ (1) |
| Puggalo atthi | ပုဂ္ဂိုလ် ရှိသည် (4) |
| puggalo neva saṅkhato | ပုဂ္ဂိုလ်သည် ပြုပြင်ဖန်တီးထားသော အရာလည်း မဟုတ် (3) |
| Puggalo neva saṅkhato | ပုဂ္ဂိုလ်သည် ပြုပြင်ဖန်တီးထားသော အရာလည်း မဟုတ် (2) |
| Puggalo nupalabbhati | ပုဂ္ဂိုလ် … မတွေ့ရ (13) |
| Puggalo rūpaṃ | ပုဂ္ဂိုလ် … ရုပ် (1) |
| Puggalo sandhāvati | ပုဂ္ဂိုလ် … ကူးသွားသည် (5); ပုဂ္ဂိုလ်သည် ကူးသွားသည် (1) |
| puggalo sandhāvati | ပုဂ္ဂိုလ် … ကူးသွားသည် (13) |
| puggalo saphalo | ပုဂ္ဂိုလ် … အသီးအပွင့် ရှိသော (4) |
| Puggalo sappaccayo | ပုဂ္ဂိုလ်သည် အကြောင်း ရှိသော အရာ (2) |
| puggalo sassato | ပုဂ္ဂိုလ်သည် ထာဝရ တည်မြဲသော အရာ (2) |
| puggalo saṅkhato | ပုဂ္ဂိုလ်သည် ပြုပြင်ဖန်တီးထားသော အရာ (2) |
| Puggalo saṅkhato | ပုဂ္ဂိုလ်သည် ပြုပြင်ဖန်တီးထားသော အရာ (2) |
| Puggalo upalabbhati | ပုဂ္ဂိုလ် … တွေ့ရသည် (28); ပုဂ္ဂိုလ်ကို တွေ့ရသည် (6) |
| puggalo upalabbhati | ပုဂ္ဂိုလ် … တွေ့ရသည် (56) |
| puggalānaṃ | ပုဂ္ဂိုလ် (5) |
| puggalānaṃ paññatti | ပုဂ္ဂိုလ်၏ သတ်မှတ်ချက် (4); ပုဂ္ဂိုလ် … သတ်မှတ်ချက် (1) |
| purisa | လူ (4); ယောက်ျား (1) |
| purisapuggalā | ပုဂ္ဂိုလ် (2) |
| purisayugā | လူ အတွဲ (2) |
| puriso | ယောက်ျား (1) |
| puñjo | အစုအပုံ (1) |
| pāda | ခြေ (2) |
| pānīya | သောက်ရေ (1) |
| pāpakānaṃ | ယုတ်မာသော (6) |
| pāpakānaṃ kammānaṃ | ယုတ်မာသော ကံ (6) |
| pāpakānaṃ kammānaṃ upalabbhati | ယုတ်မာသော ကံ … တွေ့ရသည် (6) |
| pāpakāni | ယုတ်မာသော (17) |
| pāpakāni kammāni | ယုတ်မာသော ကံ (17) |
| pāpakāni kammāni upalabbhanti | ယုတ်မာသော ကံတို့ကို တွေ့ရသည် (17) |
| pāpimantaṃ | မကောင်းမှု ပြုသော (1) |
| pātubhavanti | ပေါ်ပေါက်သည် (1) |
| pātubhāvā | ပွင့်ပေါ်ခြင်း (1) |
| pāṇa | သူ့အသက် (2) |
| pītakaṃ | အဝါ (1) |
| pītaṃ | အဝါ (1) |
| rasa | အရသာ (2) |
| rasā | အရသာ (1) |
| rasāyatanaṃ | အရသာ အာရုံခံ နယ်ပယ် (1) |
| ratho | ရထား (1) |
| rañño | မင်း (1) |
| raṭṭhaṃ | တိုင်းပြည် (1) |
| rukkhaṃ | သစ်ပင် (1) |
| rājā | မင်း (9) |
| rūpa | သိမ်မွေ့သော ရုပ် (4); အဆင်းအရောင် (3); ရုပ် (1) |
| rūpadhātu | အဆင်းအရောင် ဓာတ် (3) |
| Rūpadhātuyā | သိမ်မွေ့သော ရုပ်ဘုံ (4) |
| Rūpasmiṃ | ရုပ် (2) |
| rūpavā | ရုပ် ရှိသော (1) |
| rūpaṃ | ရုပ် (14); အဆင်းအရောင် (3) |
| Rūpaṃ | ရုပ် (12) |
| Rūpaṃ aniccaṃ | ရုပ်သည် မမြဲသော (1) |
| rūpaṃ aniccaṃ | ရုပ် … မမြဲသော (1) |
| rūpaṃ cavati | ရုပ်သည် စုတေသည် (1) |
| Rūpaṃ puggalo | ရုပ်သည် ပုဂ္ဂိုလ် (2); ရုပ် … ပုဂ္ဂိုလ် (1) |
| Rūpaṃ sandhāvati | ရုပ်သည် ကူးသွားသည် (1) |
| rūpaṃ upalabbhati | ရုပ် … တွေ့ရသည် (13) |
| Rūpaṃ upalabbhati | ရုပ် … တွေ့ရသည် (4) |
| Rūpaṃ upādāya | ရုပ်ကို မှီ၍ (3) |
| rūpaṃ upādāya | ရုပ်ကို မှီ၍ (3) |
| rūpena | ရုပ် (1) |
| rūpo | ရုပ် (2) |
| rūpā | အဆင်းအရောင် (1) |
| rūpāyatanaṃ | အဆင်းအရောင် အာရုံခံ နယ်ပယ် (2) |
| rūpī puggalo | ရုပ် ရှိသော ပုဂ္ဂိုလ် (1) |
| Sabbadā | အချိန်တိုင်း (1) |
| Sabbattha | နေရာတိုင်း (2) |
| Sabbesu | အရာအားလုံး (2) |
| sabbo | အားလုံး (1) |
| sabhāga | တူညီခြင်း (2) |
| sacca | မှန်သော (8) |
| saccato | အမှန်အားဖြင့် (2) |
| saccato thetato | အမှန်အားဖြင့် ခိုင်မြဲစွာ (2) |
| saccavādī | မှန်သော စကားကို ဆိုတော်မူသော (8) |
| sacchikaroti | မျက်မှောက် ပြုသည် (2) |
| saccikaṭṭha | အမှန်တကယ် အရာ (2) |
| saccikaṭṭhaparamatthena | အမှန်တကယ် အဆုံးစွန် အနက် (92) |
| saccikaṭṭho | အမှန်တကယ် အရာ (9) |
| sadda | အသံ (2) |
| saddadhātu | အသံ ဓာတ် (1) |
| saddaṃ | အသံ (2) |
| saddhindriyaṃ | ယုံကြည်မှု၏ စွမ်းရည် (1) |
| saddhā | ယုံကြည်မှု (3) |
| saddhānusārī | ယုံကြည်မှုကို အစဉ်လိုက်သူ (2) |
| saddo | အသံ (1) |
| saddā | အသံ (1) |
| saddāyatanaṃ | အသံ အာရုံခံ နယ်ပယ် (1) |
| sadā | အမြဲ (1) |
| Saha | အတူ (1) |
| sakadāgāmī | သကဒါဂါမ် (3) |
| sama | တူသော (2) |
| samasamo | အလွန် တူညီစွာ (1) |
| sambhoti | ဖြစ်ပေါ်သည် (1) |
| sambhārā | အစိတ်အပိုင်း (1) |
| sambuddha | အမှန်ကို ကိုယ်တိုင် … သိမြင်တော်မူသော ဘုရားရှင် (1) |
| sambuddho | အမှန်ကို ကိုယ်တိုင် … သိမြင်တော်မူသော ဘုရား (1) |
| same | ညီမျှသော (2) |
| sammati | (no direct equivalent) (1) |
| sammuti | သမုတ် (1) |
| sammā | အပြည့်အဝ (2); မှန်ကန်သော (2) |
| sammāsambuddhassa | အမှန်ကို ကိုယ်တိုင် အပြည့်အဝ သိမြင်တော်မူသော ဘုရားရှင် (1) |
| sammāsambuddho | အမှန်ကို ကိုယ်တိုင် အပြည့်အဝ သိမြင်တော်မူသော ဘုရား (1) |
| samuddo | သမုဒ္ဒရာ (8) |
| samuddo atthi | သမုဒ္ဒရာ ရှိသည် (2) |
| samuddo upalabbhati | သမုဒ္ဒရာကို တွေ့ရသည် (6) |
| samuppannaṃ | ဖြစ်ပေါ်လာသော (5) |
| samuppanno | ဖြစ်ပေါ်လာသော (1) |
| samuppannā | ဖြစ်ပေါ်လာသော (1) |
| samādhi | သမာဓိ (1) |
| samādhindriyaṃ | သမာဓိ၏ စွမ်းရည် (1) |
| samādhiṃ | သမာဓိ (2) |
| sandhāvaniyā | ကူးသွားခြင်း (1) |
| sandhāvataṃ | ကူးသွား (1) |
| sandhāvati | ကူးသွားသည် (22) |
| sandhāvitvāna | ကူးသွား၍ (1) |
| sanidassanaṃ | မြင်နိုင်သော (1) |
| saphalaṃ | အသီးအပွင့် ရှိသော (2) |
| saphalā | အသီးအပွင့် ရှိသော (2) |
| sappaccayo | အကြောင်း ရှိသော (2) |
| sappaṭighaṃ | ထိခိုက်မှု ရှိသော (1) |
| sappi | ထောပတ်ကြည် (1) |
| sarāvakaṃ | ပန်းကန် (1) |
| sarīraṃ | ကိုယ်ခန္ဓာ (8) |
| sassatavādo | ထာဝရ တည်မြဲသည်ဟု ဆိုသော ဝါဒ ရှိသော (1) |
| sassatisamaṃ | ထာဝရ တည်မြဲသည်နှင့် တူစွာ (1) |
| sassato | ထာဝရ တည်မြဲသော (5) |
| sassatā | ထာဝရ တည်မြဲသော (1) |
| sati | သတိ (1) |
| satindriyaṃ | သတိ၏ စွမ်းရည် (1) |
| satiṃ | သတိ (2) |
| sato | သတိ ရှိသော (1) |
| Sattamo | သတ္တမ (1) |
| satte | သတ္တဝါ (2) |
| satthā | ဆရာ (1) |
| satthāro | ဆရာ (1) |
| satthāro santo | ဆရာ … ရှိသည် (1) |
| sattā | သတ္တဝါ (3) |
| sattānaṃ | သတ္တဝါ (1) |
| sayaṃ | မိမိ (4) |
| saññaṃ | မှတ်သိမှု (2) |
| Saññaṃ | မှတ်သိမှု (1) |
| sañño | မှတ်သိမှု (2) |
| saññā | မှတ်သိမှု (13) |
| Saññā | မှတ်သိမှု (4) |
| saññā upalabbhati | မှတ်သိမှု … တွေ့ရသည် (10) |
| Saññā upalabbhati | မှတ်သိမှု … တွေ့ရသည် (2) |
| Saṃkhittaṃ | အကျဉ်းချုပ် (7) |
| saṃsandanaṃ | နှိုင်းယှဉ်ခြင်း (5) |
| saṃsandanā | နှိုင်းယှဉ်ခြင်း (1) |
| saṃsarataṃ | ကျင်လည်နေသော (1) |
| saṃsāro | သံသရာ (1) |
| saṃvijjamāno | ထင်ရှား ရှိနေသော (1) |
| saṃvijjamānā | ထင်ရှား ရှိသော (1) |
| saṃyojana | နှောင်ကြိုး (1) |
| saṃyojanānaṃ | နှောင်ကြိုး (1) |
| saṅkappaṃ | ကြံစည်မှု (2) |
| saṅkhataṃ | ပြုပြင်ဖန်တီးထားသော (4) |
| Saṅkhataṃ | ပြုပြင်ဖန်တီးထားသော (1) |
| saṅkhato | ပြုပြင်ဖန်တီးထားသော (7) |
| saṅkhatā | ပြုပြင်ဖန်တီးထားသော (2) |
| saṅkhāra | ပြုပြင်ဖန်တီးမှု (1) |
| saṅkhāre | ပြုပြင်ဖန်တီးမှု (3) |
| saṅkhāro | ပြုပြင်ဖန်တီးမှု (2) |
| saṅkhārā | ပြုပြင်ဖန်တီးမှု (13) |
| Saṅkhārā | ပြုပြင်ဖန်တီးမှု (4) |
| saṅkhārā upalabbhanti | ပြုပြင်ဖန်တီးမှု … တွေ့ရသည် (10) |
| Saṅkhārā upalabbhanti | ပြုပြင်ဖန်တီးမှု … တွေ့ရသည် (2) |
| secanaka | ရောနှောသော (2) |
| seniya | သေနိယ (1) |
| sineru | မြင့်မိုရ် (8) |
| sodhanaṃ | စိစစ်ခြင်း (2) |
| somanassa | ဝမ်းမြောက်မှု (1) |
| somanassindriyaṃ | ဝမ်းမြောက်မှု၏ စွမ်းရည် (1) |
| sosiyo | ချောင်းဆိုး ပန်းနာ ရောဂါ ရှိသူ (2) |
| sota | နား (14) |
| sotadhātuyā | နား ဓာတ် (2) |
| sotaviññāṇa | နား သိစိတ် (1) |
| sotaṃ | နား (2) |
| sotindriyaṃ | နား၏ စွမ်းရည် (5) |
| sotindriyaṃ upalabbhati | နား၏ စွမ်းရည်ကို တွေ့ရသည် (2); နား၏ စွမ်းရည် … တွေ့ရသည် (1) |
| sotāpanno | သောတာပန် (2) |
| Sotāpanno | သောတာပန် (3) |
| sotāpanno atthi | သောတာပန် ရှိသည် (1) |
| Sotāpanno atthi | သောတာပန် ရှိသည် (2) |
| sotāyatanaṃ | နား အာရုံခံ နယ်ပယ် (5) |
| suddha | ရိုးရိုး (2); သက်သက် (1) |
| suddhika | ရိုးရိုး (2) |
| suddo | သူဆင်းရဲမျိုး (7) |
| sugate | ကောင်းသော လားရာ ရှိသော (2) |
| sukha | ချမ်းသာ (7); သာယာမှု (1) |
| sukhadukkhaṃ | ချမ်းသာနှင့် ဆင်းရဲ (5) |
| sukhaṃ | ချမ်းသာ (12); သာယာသော (4) |
| sukhaṃ upalabbhati | ချမ်းသာကို တွေ့ရသည် (12) |
| sukhaṃ vedanaṃ | သာယာသော ခံစားမှု (3) |
| sukhaṃ vediyamāno | သာယာသော ခံစားမှုကို ခံစားနေသော (3) |
| sukhāya | ချမ်းသာ (1) |
| Suniggahito | ကောင်းစွာ ချေပခြင်း ခံရသော (2) |
| suniggahitova | (no direct equivalent) (1) |
| sutta | သုတ္တန် (1) |
| suttanto | သုတ္တန် (13) |
| suvaṇṇe | အဆင်း လှသော (2) |
| Suññato | ဆိတ်သုဉ်းသည် (1) |
| suñño | ဆိတ်သုဉ်းသော (1) |
| suṇāti | ကြားသည် (4) |
| sāyati | လျက်သည် (2) |
| sūkaro | ဝက် (3) |
| taro | ကူးမြောက်သူ (1) |
| tasmā | သောကြောင့် (1) |
| Tassa tasseva | ထိုထိုသူ၏ပင် (8) |
| tatha | ဟုတ်တိုင်း (8) |
| tathavādī | ဟုတ်တိုင်း ဆိုတော်မူသော (8) |
| tatheva | ထိုအတိုင်းပင် (1) |
| tava | သင် (2) |
| taṇhā | တဏှာ (1) |
| te | သင် (1) |
| Tejo | မီး (1) |
| tejo | မီး (7) |
| tejo atthi | မီး ရှိသည် (2) |
| Tejo upalabbhati | မီးကို တွေ့ရသည် (1) |
| tejo upalabbhati | မီးကို တွေ့ရသည် (5) |
| Tena hi | သို့ဖြစ်လျှင် (14); သို့ဖြစ်၍ (2) |
| tena hi | သို့ဖြစ်လျှင် (3) |
| thetato | ခိုင်မြဲစွာ (2) |
| thokaṃ | အနည်းငယ် (1) |
| thālakaṃ | ဗန်း (1) |
| tiracchānagato | တိရစ္ဆာန် (1) |
| tiṇa | မြက် (8) |
| tiṇa paṭisaṃvedī | မြက် … ခံစားသော (6) |
| tiṭṭhati | တည်သည် (2) |
| ucchedavādo | ပြတ်စဲသွားသည်ဟု ဆိုသော ဝါဒ ရှိသော (1) |
| Ucchedā | ပြတ်စဲခြင်း (1) |
| ucchinno | ပြတ်စဲသွားသော (1) |
| udaka | ရေ (1) |
| uhacca | (no direct equivalent) (1) |
| upacchedo | ပြတ်ခြင်း (8) |
| upage | ရောက်သွားသော (2) |
| upalabbhanti | တွေ့ရသည် (17) |
| upalabbhati | တွေ့ရသည် (130) |
| upanayana | ဆက်စပ် အသုံးချချက် (2) |
| upapajjamāne | ဖြစ်ပေါ်ဆဲ (2) |
| upapajjati | ပြန်လည် ဖြစ်ပေါ်သည် (3) |
| upapanno | ပြန်လည် ဖြစ်ပေါ်သော (2) |
| upekkhā | ဥပေက္ခာ (1) |
| uppajjamānaṃ | ဖြစ်ပေါ်သော (1) |
| uppajjamāno | ပေါ်ပေါက်လာသော (1) |
| uppajjati | ဖြစ်ပေါ်သည် (2); ပေါ်ပေါက်လာသည် (1) |
| uppanne | ဖြစ်ပေါ်သော (2) |
| uppādo | ဖြစ်ခြင်း (2) |
| upādā | စွဲလမ်းမှု (8); မှီ၍ (2) |
| upādāya | မှီ၍ (1) |
| vaggo | ဝဂ် (1) |
| vanappatayo | သစ်ပင် (8) |
| vanappatayo atthi | သစ်ပင်တို့ ရှိသည် (2) |
| vanappatayo upalabbhanti | သစ်ပင်တို့ကို တွေ့ရသည် (6) |
| vata | အမှန်ပင် (54) |
| vatthu | အငြင်းပွားရာ အကြောင်းအရာ (1) |
| vaya | ပျက်စီး (5) |
| vayadhammaṃ | ပျက်စီးတတ်သော သဘော … ရှိသော (3) |
| vayadhammo | ပျက်စီးတတ်သော သဘော … ရှိသော (1) |
| vayadhammā | ပျက်စီးတတ်သော သဘော … ရှိသော (1) |
| vayo | ပျက်ခြင်း (2) |
| vaṭṭa | သံသရာ စက်ဝန်း (8) |
| Vedanaṃ | ခံစားမှု (4) |
| vedanaṃ | ခံစားမှု (1) |
| Vedanaṃ upādāya | ခံစားမှုကို မှီ၍ (4) |
| vedanaṃ upādāya | ခံစားမှုကို မှီ၍ (1) |
| vedano | ခံစားမှု (2) |
| vedanā | ခံစားမှု (11) |
| Vedanā | ခံစားမှု (7) |
| vedanā upalabbhati | ခံစားမှု … တွေ့ရသည် (10) |
| Vedanā upalabbhati | ခံစားမှု … တွေ့ရသည် (2) |
| vedanāsu | ခံစားမှု (2) |
| vedanāsu viharati | ခံစားမှု … နေသည် (2) |
| vedayitaṃ | ခံစားရမှု (1) |
| vediyamāno | ခံစားနေသော (4) |
| vesso | ကုန်သည်မျိုး (7) |
| veti | ပျက်ကွယ်သည် (1) |
| vicikicchati | ယုံမှားသည် (1) |
| vigato | ကွယ်ပျောက်သော (2) |
| viharati | နေသည် (4) |
| vijjamāno | ရှိနေသော (1) |
| vijānāti | သိသည် (4) |
| vikubbati | ဖန်ဆင်းပြသည် (2) |
| vimutto | လွတ်မြောက်သော (2) |
| vipaccamāne | အကျိုး ပေးနေသော (2) |
| vipariṇāmadhammaṃ | ဖောက်ပြန်ပြောင်းလဲတတ်သော သဘော ရှိသော (3) |
| vipariṇāmadhammo | ဖောက်ပြန်ပြောင်းလဲတတ်သော သဘော ရှိသော (2) |
| vipariṇāmadhammā | ဖောက်ပြန်ပြောင်းလဲတတ်သော သဘော ရှိသော (2) |
| vipākapaṭisaṃvedī | အကျိုးကို ခံစားသော (16) |
| Vipākapaṭisaṃvedī | အကျိုးကို ခံစားသော (1) |
| Vipāko atthi | အကျိုး ရှိသည် (5) |
| vipāko atthi | အကျိုး ရှိသည် (1) |
| virāga | ပြယ်ပျောက် (5) |
| virāgadhammaṃ | ပြယ်ပျောက်တတ်သော သဘော … ရှိသော (3) |
| virāgadhammo | ပြယ်ပျောက်တတ်သော သဘော … ရှိသော (1) |
| virāgadhammā | ပြယ်ပျောက်တတ်သော သဘော … ရှိသော (1) |
| visadisaṃ | ကွဲပြားသည် (1) |
| visuddhena | စင်ကြယ်သော (2) |
| vitatha | မှားယွင်း (8) |
| vivajjitā | ပယ်ရှားတော်မူသော (1) |
| viññeyyaṃ | သိနိုင်သော (1) |
| viññāṇaṃ | သိစိတ် (16) |
| Viññāṇaṃ | သိစိတ် (6) |
| viññāṇaṃ sandhāvati | သိစိတ်သည် ကူးသွားသည် (1) |
| viññāṇaṃ upalabbhati | သိစိတ် … တွေ့ရသည် (11) |
| Viññāṇaṃ upalabbhati | သိစိတ် … တွေ့ရသည် (2) |
| viññāṇo | သိစိတ် (2) |
| Vuttaṃ | ဟောတော်မူသည် (2) |
| Vuttaṃ bhagavatā | မြတ်စွာဘုရား … ဟောတော်မူသည် (2) |
| vā pana | သို့မဟုတ် (2) |
| vācaṃ | စကား (2) |
| vādī | ဆိုတော်မူသော (8); မိမိဘက် (1); တစ်ဖက်သား (1) |
| vāra | အကြိမ် (1) |
| Vāyo | လေ (1) |
| vāyo | လေ (7) |
| vāyo atthi | လေ ရှိသည် (2) |
| Vāyo upalabbhati | လေကို တွေ့ရသည် (1) |
| vāyo upalabbhati | လေကို တွေ့ရသည် (5) |
| vāyāmaṃ | အားထုတ်မှု (2) |
| yakkho | ဘီလူး (1) |
| yampidaṃ | ရှိသမျှ (1) |
| yaṃ | အကြင်အရာ (3) |
| yena | အကြင်အရာ (3) |
| yo | အကြင်သူ (3) |
| Yo | (no direct equivalent) (4) |
| yugā | အတွဲ (2) |
| yāgū | ယာဂု (1) |
| ñassāmi | သိရတော့သည် (1) |
| ñātaka | ဆွေမျိုး (1) |
| ñāṇaṃ | ဉာဏ် (1) |
| āharaṇena | ကိုးကားခြင်း (1) |
| Ājānāhi | လက်ခံသည် (33) |
| ājīvaṃ | အသက်မွေးမှု (2) |
| ālapana | ခေါ်ဝေါ်ပုံ (1) |
| Āmantā | ဟုတ်ပါသည် (205) |
| āmantā | ဟုတ်ပါသည် (1) |
| Āpo | ရေ (1) |
| āpo | ရေ (7) |
| āpo atthi | ရေ ရှိသည် (2) |
| Āpo upalabbhati | ရေကို တွေ့ရသည် (1) |
| āpo upalabbhati | ရေကို တွေ့ရသည် (5) |
| Āpāyikaṃ | အပါယ် (6) |
| Āpāyikaṃ upalabbhati | အပါယ် … တွေ့ရသည် (6) |
| āsavānaṃ | စိတ်အစွန်းအထင်း (2) |
| āyasmā | အသျှင် (1) |
| āyasmā ānando | အသျှင် အာနန္ဒာ (1) |
| āyatanaṃ upalabbhati | အာရုံခံ နယ်ပယ် … တွေ့ရသည် (4) |
| āyatanānaṃ | အာရုံခံ နယ်ပယ် (1) |
| ūhacca | နှုတ်ပယ်၍ (1) |
| ṭhapetvā | ချန်ထား၍ (2) |
| ṭhassāmi | တည်သည် (1) |
| ṭhitassa | တည်နေသော (2) |
| ṭhānaṃ | တည်ရာ (1) |
| ṭīkā | ဋီကာ (1) |
