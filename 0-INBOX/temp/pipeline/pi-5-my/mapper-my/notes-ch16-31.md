# pi-5 Burmese keyword mapping, PHASE 2, group ch16–31: notes

Script `map_ch16-31.py` (imports `map5_rules.py`, NOT edited, and the ch1 table of `map_ch1.py`, read only); output the 16
files `16-atthamavaggo.mapped.md` … `31-tevisatimavaggo.mapped.md`. Burmese only from this track's FINAL pi-5 text
(`AI_translation/burmese/pi-5-burmese-plain-zeroshot_split_chapters`), `my5-zeroshot-terms.md` (via the module) and the
final pi-1 … pi-4 mappings (via the module). pi-1-my … pi-4-my were only read through the module; nothing outside
`mapper-my/` was written. Helpers (read only, scratch): `work/diag1631.py`, `work/look1631.py`, `work/g1631.py`,
`work/sent1631.py` (sentence aligner), `work/pv1631.py`, `work/dupcheck1631.py`, `work/stats1631.py`, `work/diffm.py`.

## Numbers

| chapter | lines | `bad` | presence failures | «, » / «၊» / « / » in a value | ending-rule chunks | (no direct equivalent) |
|---|---|---|---|---|---|---|
| 16-atthamavaggo | 66 | [] | 0 | 0 | 64 | 7 |
| 17-navamavaggo | 46 | [] | 0 | 0 | 81 | 2 |
| 18-dasamavaggo | 56 | [] | 0 | 0 | 91 | 1 |
| 19-ekadasamavaggo | 41 | [] | 0 | 0 | 80 | 5 |
| 20-dvadasamavaggo | 44 | [] | 0 | 0 | 93 | 3 |
| 21-terasamavaggo | 52 | [] | 0 | 0 | 127 | 2 |
| 22-cuddasamavaggo | 43 | [] | 0 | 0 | 61 | 6 |
| 23-pannarasamavaggo | 54 | [] | 0 | 0 | 61 | 5 |
| 24-solasamavaggo | 53 | [] | 0 | 0 | 66 | 3 |
| 25-sattarasamavaggo | 48 | [] | 0 | 0 | 109 | 2 |
| 26-attharasamavaggo | 44 | [] | 0 | 0 | 102 | 0 |
| 27-ekunavisatimavaggo | 45 | [] | 0 | 0 | 45 | 7 |
| 28-visatimavaggo | 33 | [] | 0 | 0 | 76 | 8 |
| 29-ekavisatimavaggo | 30 | [] | 0 | 0 | 49 | 7 |
| 30-bavisatimavaggo | 32 | [] | 0 | 0 | 105 | 1 |
| 31-tevisatimavaggo | 21 | [] | 0 | 0 | 43 | 2 |
| **total** | **708** | **[]** | **0** | **0** | **1253** | **61** |

Preservation checked with the brief's exact command per chapter (all `bad []`); presence and punctuation with
`map5_rules.verify_file` (printed by the script). Every presence exception is a chunk matched by one of the module's
ending rules (Q1 and the pi-1 … pi-4 endings); none is unexplained.

Sources of the 10,687 values (uses): table 3288, pi-2 3012, frame 1778, compose 808, stock 479, group 429, terms 273, pi-4 237, ch1 124, pi-1 119, ctx 73, pi-3 64, neg 3 (table = this script's group / chapter tables; group = G4, another chapter's value of the group; ctx = per-segment override; frame / stock = the module tables; ch1 = the ch1 table; pi-N = the pi-N mapping; terms = my5-zeroshot-terms; compose = members joined; neg = G3).

## Rules used (binding, unchanged)

All phase-1 rules as approved by the coordinator (2026-11-20): pi-1 rules 1–11 and the agreed later pi-1 rules, pi-2
N1–N11 and decisions, pi-3 M1–M9, pi-4 P1–P8 / A2, pi-5 Q1–Q8 (`map-table.md`), with the coordinator's settlements
(Āmantā «ဟုတ်ပါသည်» whole; -ī adjectives / -vādī epithets «…သော», agent nouns «…သူ»; bhikkhave «ရဟန်း»; a keyword
that is itself negative keeps the text's negative, e.g. asañcicca «မရည်ရွယ်ဘဲ», ajaneti «မမွေးဖွားစေသည်», akataṃ
«မပြုသော»). In practice:
- one sense per segment (the first in the Pāli); compound members inside one Burmese word: one member gets the word,
  the other (no direct equivalent) (jano / janassa of puthujjana, aṅga of bojjhaṅga, sañña of asaññasatta, bhāvo of
  attabhāva, mātā of mātāpitaro, upame of laṭukikopama, āvāha of āvāhavivāha);
- a Roman-script variant or siglum = (no direct equivalent) (M2: potaliputtassa, vattabbe ^5-545, nibbattati ^5-692,
  viharanti ^5-798, kho ^5-851, dvākāre / duviññāpaye ^5-856, sabbattha ^5-525); a translated editors' note gets
  values (M9: paṭiññā, vādissa ^5-656; kathāyaṃ, lakkhaṇaṃ, dissanti ^5-652; dvayena ^5-786; dha ^5-887);
- fragments that lost a negative = the positive part (rule 8: the 26 aspects dhuvato / tāṇato / leṇato / saraṇato /
  attato; sañjātaṃ, phassakassa, ābhogassa, paṇidahantassa, vivitto, paṭisamo, sampajānassa …);
- verbs «…သည်» (rule 4, future and potential forms normalised: kathessāmi = ပြောဆိုသည်, tiṭṭheyya = တည်နေသည်),
  participles / adjectives «…သော», gerundives «…မည့်» (hantabbo = သတ်ရမည့်, pahātabbaṃ = ပယ်ရမည့်), absolutives
  «…၍» (Q1: samādiyitvā = ဆောက်တည်၍ against «ဆောက်တည်ပြီး၍»), counts with the text's classifier;
- the 26 aspects of ^5-547 (aniccato … vipariṇāmadhammato) without the quotative «ဟု» (rule 9), one form for the list.

## NEW rules (beyond phase 1), for review

G1. **The «ပင်» of eva / va is not part of a multiword keyword** (as Q4 for the «လည်း» of ca / pi): where two members
    of a composed keyword stand «Xပင် Y» in the text, the value is «X … Y» (kāmadhātu rūpadhātū ^5-516 «ထိုကာမဘုံပင်
    သိမ်မွေ့သော ရုပ်ဘုံ» = ကာမဘုံ … သိမ်မွေ့သော ရုပ်ဘုံ). `Mapper.pali_order`.
G2. **Two-member compose in the Pāli order** where the text has the members in that order and the other order is only
    a bare adjacency (no particle between them); an adjacency WITH a particle is the text's own construction and stays
    (rūpīnaṃ pālanā = ရုပ် ဖြစ်သော … စောင့်ရှောက်ခြင်း, not the neighbouring «စောင့်ရှောက်ခြင်း ရုပ် …»; rūpaṃ
    arūpāvacaraṃ = ရုပ် … ရုပ်မရှိသော ဘုံနှင့် ဆိုင်သော; but pahīnā duggati = ဆိုးသော လားရာကို ပယ်ပြီးသော;
    lokiyena samannāgato = လောကနှင့် သက်ဆိုင်သော … ပြည့်စုံသော). `Mapper.pali_order`.
G3. **A negative inside a multiword keyword** («anāgāmī na parihāyati», «Sīlaṃ na cittānuparivattī»): Q5 applied to
    the last verb (the text's «မX» without «သည်»: အနာဂါမ် … မဆုတ်ယုတ်); with no verb, pi-1 rule 5 «… မဟုတ်» (သီလ …
    စိတ်နောက်သို့ လိုက်ပါသော … မဟုတ်). The module composes only an initial na / no. `negate_last`, `Mapper.lookup`.
G4. **A value settled in another chapter of this group** is used for the same keyword where the segment has it (after
    the chapter's own table, CTX, the group table and the module's FRAME / STOCK, before the ch1 table and the module's
    generic pi-1 … pi-4 lookup). A tuple value «(a, b, …)» = the first the segment has (presence), else the pi-1 …
    pi-4 value. Tuples are not used across chapters (they carry their own alternatives).
G5. **Duplicate members** («Maggasamaṅgī samannāgato», «chandādhipati adhipati», «Kusalena kammena kusalo»): the
    module's compose drops a member whose value repeats; these get explicit values with both members
    (မဂ်နှင့် ပြည့်စုံသော … ပြည့်စုံသော). Checked over the group with `work/dupcheck1631.py`.

## Module overrides (for the coordinator; the module was not edited)

1. **parinibbāyī**: the module's lookup takes the pi-5 terms value «ပရိနိဗ္ဗာန် ပြုသူ» before the pi-4 value; Q8 and
   pi-4 give «ပရိနိဗ္ဗာန် ပြုသော» (T_GROUP).
2. **sukhadukkhaṃ** (STOCK «ချမ်းသာနှင့် ဆင်းရဲ»): absent at ^5-539, ^5-742, ^5-801 (text «ချမ်းသာ ဆင်းရဲ», «သာယာမှု
   နာကျင်မှု», «သုခ ဒုက္ခ»); alternatives in T_GROUP / CTX.
3. **sukha / sukhaṃ** (STOCK @sukha): the Sukhānuppadāna kathā (ch24) and ch25 write «သုခ»; `sukha24` = «သုခ» where
   the text has it, else the module's f_sukha.
4. **antarikā** (STOCK @antarika «ကြားအပိုင်း»): jhānantarikā (ch26) = «အကြား ကာလ»; `antarika3`.
5. **aṅga / aṅgo / aṅgaṃ / aṅgā / aṅgānaṃ** (module @anga): the module gives «အင်္ဂါ» whenever the segment has
   «အင်္ဂါ» anywhere (e.g. maggaṅga «မဂ်၏ အင်္ဂါ») even where the keyword is the bojjhaṅga member; `anga3` decides by
   the FIRST aṅga compound of the Pāli (one sense per segment), the word-start pattern widened to «sambojjhaṅgo».
6. **parinibbuto** (STOCK «ပရိနိဗ္ဗာန် ပြုပြီးသော»): ^5-802, ^5-896 «ပရိနိဗ္ဗာန် ပြုတော်မူခဲ့သည်» → alternative
   «ပရိနိဗ္ဗာန် ပြုတော်မူခဲ့သော».
7. **bhāvito / bhāvitā** (STOCK @bhavito): ^5-623, ^5-903, ^5-904 «ပွားများထား…» → alternative «ပွားများထားသော».
8. **sabbadā / sabbattha** (FRAME): ^5-868 «အမြဲ» (tiṭṭhati sabbadā), ^5-525 the siglum «(Sabbattha)» left Roman = (no
   direct equivalent).
9. **anuyogo** (FRAME «စစ်ဆေးမေးမြန်းခြင်း»): ^5-897 jāgariyānuyogo = «နိုးကြားစွာ အားထုတ်ခြင်း».
10. **viharati** ^5-803 «နေတော်မူသည်» (honorific); **dhammo** (pi-4 «သဘော ရှိသော», a -dhammo compound value that the
    generic lookup took for the bare noun) = «သဘောတရား / တရား» (^5-599, ^5-603 «sataṃ dhammo» = တရား, ^5-908
    methuno dhammo = အကျင့်); **maggaṃ / magga / maggo** (the generic lookup took «လမ်း» from «လမ်းကြောင်း») =
    «မဂ်» first; **katvā** (FRAME @katva) ^5-539 / ^5-715 «ပြု၍»; **sakadāgāmi / anāgāmi** ^5-644 «သကဒါဂါမ် / အနာဂါမ်»;
    **para** ^5-875 parappavādā «အခြား»; **citta** ^5-911 cittiddhipāda «စိတ္တ»; **rāga / rāgo** ^5-21-8-1-0, ^5-675,
    ^5-685 asātarāga «တပ်မက်မှု»; **dānaṃ** ^5-658, ^5-779 «dānaṃ dadeyya» = «ဒါန ပြုရာ» (dānaṃ = ဒါန, dadeyya =
    ပြုသည်); **nirodho / nirodhaṃ** (ekanirodho) «အတူ ချုပ်သော» = «ချုပ်သော»; **samāpatti** «ဈာန် ဝင်စားခြင်း» /
    «သမာပတ်»; **dhātū** before «ti» (kāma- / rūpadhātūti) = «ဘုံ»; **dukkhā** → the module's @dukkha.
11. Frame-coverage failures of the 150 (frame-coverage.md) in this group, all settled: sukha / sukhaṃ (24, 25),
    antarikā (26), rāgo / rāga (21), dānaṃ (21, 25), nirodho (22, 24), viharati (26), bhāvito (30), sakadāgāmi /
    anāgāmi (20), citta (31), para (28), dhamma (26: dhammacakka «ဓမ္မ / စကြာ» as ch3).

## Values that differ from pi-1 … pi-4 or ch1 for the same keyword (reasons)

Of 10,687 keyword uses: 4,793 have the pi-1 … pi-4 (or ch1) value, 4,835 are keywords those never mapped, 1,059 (248
keywords) differ. In 224 of the 248 the earlier value does not occur in the segment's Burmese at all: the value is
the text's own word for this context (the full list is below, «absent»). The 24 where an earlier value does occur:
- kathā «ဆွေးနွေးချက်», koci «တစ်စုံတစ်ယောက်», arahatta «ရဟန္တာ အဖြစ်», sassato, dukkha / dukkhā / dukkhaṃ,
  sukhaṃ, gacchati: module (FRAME / STOCK) functions, unchanged.
- dhammo: the pi-4 value «သဘော ရှိသော» is the -dhammo compound value (override 10).
- Pañcaṅgiko / pañcaṅgiko maggo, dhammā niyatā, abyākatā dhammā, rūpino dhammā: the pi value's chunks occur, but not
  as the pi phrase; the text says «မဂ်သည် အင်္ဂါ ငါးပါး ရှိ…» (predicate), «သဘောတရား … ကျိန်းသေ…».
- aniccatā «မမြဲခြင်း သဘော» (pi «မမြဲခြင်း»): the text adds «သဘော» for -tā (as ṭhitatā «တည်နေခြင်း သဘော»).
- attato «အတ္တ» (pi «အတ္တဟု»): one form for the 26-aspect list (rule 9, «ဟု» goes).
- vipariṇataṃ «ဖောက်ပြန်ပြောင်းလဲပြီးသော» (pi with a space): the text writes it as one word.
- pariññāya «ပိုင်းခြား သိရန်» (pi absolutive «… သိ၍»): ^5-788 the dative «for full understanding».
- paṭivinodetvā «ပယ်ဖျောက်၍», pavaro «အထူးမြတ်ဆုံး», bhūtā «ဖြစ်စေနိုင်သော / ဓာတ်ကြီး»: by the text's order in the
  list (the pi word is a neighbour's).
Notable «absent» ones: kāyo ^5-504 asurakāyo «အပေါင်း»; pāṇaṃ ^5-648 … «သတ္တဝါ» (ch1 pāṇa «သူ့အသက်»); iṭṭha ch18
«လိုလားအပ်သော» (ch1 «လိုလားဖွယ်»); niruddhe; purisayugā «လူ အစုံ» (ch1 «လူ အတွဲ»); upacaya «စုဆောင်းမှု» (ch23) /
«စုဆောင်းခြင်း» (ch25); parinipphanna «ပြည့်စုံစွာ ဖြစ်ပေါ်ပြီး» (ch19) / «အမှန်တကယ် ဖြစ်ပေါ်ပြီး» (ch23) /
«ပြည့်စုံစွာ ပြီးမြောက်» (ch31); sacchikaronti kept pi-4 «မျက်မှောက် ပြုသည်» (text «မျက်မှောက်ပြု…» without a space, as
ch1 note A10).


### Full list (keyword | value here (uses) | pi-1 … pi-4 / ch1 value(s) | earlier value in the segment | chapters)

| keyword | value here | earlier value | in segment | chapters |
|---|---|---|---|---|
| kathā | ဆွေးနွေးချက် (290) | ဆွေးနွေးခြင်း ; စကား | present | 16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31 |
| vata | အမှန်ပင် (171) | အကျင့်ဝတ် | absent | 16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31 |
| paṇidhi | ဆုတောင်းခြင်း (33) | စိတ်ညွှတ်ခြင်း | absent | 16,17,18,20,22,24,26,27 |
| samodhānaṃ | ပေါင်းဆုံခြင်း (13) | ပေါင်းစည်းခြင်း | absent | 17,18,21,24,26,27 |
| samāpatti | ဈာန် ဝင်စားခြင်း (7) ; သမာပတ် (6) | ဈာန် ဝင်စားရာ ; ဈာန် ဝင်စားမှု | absent | 22,23,24 |
| samuṭṭhitaṃ | ဖြစ်ပေါ်သော (12) | ကောင်းစွာ ထပေါ်ပြီးသော | absent | 16 |
| dhammo | တရား (6) ; သဘောတရား (5) ; အကျင့် (1) | သဘော ရှိသော | present | 18,21,26,27,31 |
| vedayita | ခံစားရခြင်း (12) | ခံစားမှု | absent | 23 |
| atta | ကိုယ် (11) | အတ္တ ; မိမိ | absent | 16,19 |
| yoni | မွေးဖွားရာ အမျိုးအစား (9) ; မွေးဖွားရာ (1) | ဘဝ | absent | 16,30 |
| jano | (no direct equivalent) (10) | လူ | absent | 17,18,19,22,29 |
| eka | တစ်ပါး (5) ; တစ်ခု (2) ; တစ် (1) ; တူညီသော (1) | တစ်မျိုးတွဲ ; တစ်စေ့ | absent | 25,26,30,31 |
| antarā | ကြား (8) | သက်တမ်း၏ အလယ်သို့ မရောက်မီ ; ကြားညှပ် | absent | 16,20 |
| attabhāva | ကိုယ်ခန္ဓာ (8) | မိမိ ကိုယ်ခန္ဓာ | absent | 16,19 |
| jāto | ပေါ်ပေါက်သော (6) ; ဖွားမြင်တော်မူခဲ့သော (1) ; ဖွားမြင်တော်မူသော (1) | မွေးဖွားသော ; မွေးဖွားလာသော | absent | 22,23,24,26 |
| janassa | (no direct equivalent) (8) | လူ | absent | 27,28 |
| koci | တစ်စုံတစ်ယောက် (7) | တစ်စုံတစ်ရာ | present | 17,19,22,25,29 |
| arahatta | ရဟန္တာ အဖြစ် (7) | ရဟန္တာ ; အရဟတ္တ | present | 20,29,30 |
| dakkhiṇaṃ | အလှူ (7) | တောင် | absent | 25 |
| ṭhiti | တည်ရာ (6) | တည်တံ့ခြင်း | absent | 16 |
| diṭṭhadhamma | ယခုဘဝ (6) | မျက်မှောက်ဘဝ | absent | 22,24 |
| paccayatā | အကြောင်းဖြစ်ခြင်း (4) ; အကြောင်းဖြစ်ပုံ (2) | ဤအကြောင်းကြောင့် ဤအကျိုး ဖြစ်ပုံ | absent | 23,30 |
| bhagavā | မြတ်စွာဘုရား (6) | ဘုန်းတော်ရှင် | absent | 24,25,26,29,30 |
| asuci | မစင်ကြယ်သော သုက်ထွက်ခြင်း (4) ; မစင်ကြယ်သော သုက် (1) | စင်ကြယ်မှု မရှိသော | absent | 16,30 |
| maggaṃ bhāveti | မဂ်ကို ပွားများသည် (5) | လမ်းကို ပွားများသည် | absent | 18,24,28 |
| buddha | ဘုရား (5) | မြတ်စွာဘုရား | absent | 20,27,29,30 |
| āneñja | မတုန်လှုပ်သော (2) ; မတုန်မလှုပ်သော (2) ; အာနေဉ္ဇသပ္ပာယ (1) | မတုန်လှုပ်ခြင်း | absent | 21,25,27,30 |
| nirodhaṃ | ချုပ်ငြိမ်းရာ ဈာန် (3) ; ချုပ်သော (2) | ချုပ်ငြိမ်းခြင်း | absent | 23,24,26 |
| gāma | ရွာ (5) | ရွာသား | absent | 25,26,30,31 |
| Yaṃ kiñci | မှန်သမျှ (4) | မည်သည့် … မဆို | absent | 16 |
| samāpannassa | ဝင်စားနေသော (4) | ဈာန် ဝင်စားသော ; ဝင်စားသော | absent | 16,23,26 |
| gacchati | သွားသည် (3) ; ရောက်သည် (1) | လိုက်သည် ; ရသည် | present | 17,28,31 |
| niruddhe | ချုပ်ငြိမ်းသော (2) ; ချုပ်ငြိမ်းပြီးသော (2) | ချုပ်ငြိမ်းသွားသော | absent | 18 |
| jāti | ဖြစ်ခြင်း (3) ; မျိုး (1) | မွေးဖွားခြင်း ; ဇာတိ | absent | 19,23,26 |
| Rūpataṇhā | အဆင်းအရောင်ကို တပ်မက်မှု (4) | သိမ်မွေ့သော ရုပ်ဘဝကို တပ်မက်မှု | absent | 21 |
| anantara | ချက်ချင်း နောက်၌ ဖြစ်စေသော (4) | နောက်ဆက်တွဲ | absent | 22,23 |
| nirodho | ချုပ်သော (4) | ချုပ်ငြိမ်းခြင်း | absent | 22,24 |
| vihāro | နေခြင်း (4) | နေထိုင်မှု | absent | 22,24 |
| sukha | သုခ (4) | သာယာမှု ; လွယ်ကူသော | absent | 24,25 |
| sukhaṃ | သုခ (4) | သာယာမှု ; သာယာသော | present | 24 |
| paṭiggaṇhāti | ခံယူသည် (4) | လက်ခံသည် | absent | 25 |
| virāga | ပြယ်ပျောက် (4) | ပြယ်ပျောက်ခြင်း ; ကင်းပြတ် | absent | 25,27,31 |
| khettaṃ | လယ်မြေ (4) | လယ်ကွင်း | absent | 25 |
| yugā | အစုံ (4) | အတွဲ | absent | 25 |
| purisayugā | လူ အစုံ (4) | လူ အတွဲ | absent | 25 |
| anuttaraṃ | အမြတ်ဆုံး (4) | ထိုထက် သာလွန်သည် မရှိသော | absent | 25 |
| buddhānaṃ | ဘုရား (4) | ဘုရားရှင် | absent | 29 |
| katvā | ပြု၍ (2) ; အကြောင်းပြု၍ (1) | စောင့်ထိန်း၍ | absent | 16,23 |
| karaṇaṃ | ပြုတတ်သော (2) ; ကွဲပြားစေတတ်သော (1) | ပြုလုပ်ခြင်း | absent | 17,25 |
| jātā | ပေါ်ပေါက်သော (2) ; ဖြစ်ပေါ်သော (1) | မွေးဖွားပြီးသော ; မွေးဖွားသော | absent | 17,23,25 |
| manasikārā | နှလုံး သွင်း (3) | နှလုံး သွင်းခြင်း ; နှလုံးသွင်းခြင်း | absent | 18 |
| santati | အစဉ် (3) | ဆက်လက်ဖြစ်ပေါ်ခြင်း | absent | 19 |
| assa | မြင်း (3) | ထိုသူ | absent | 20,28 |
| buddho | ဘုရား (2) ; ဘုရားရှင် (1) | နားလည်အပ်သော | absent | 21,26,29 |
| dānaṃ | ဒါန (3) | အလှူ ; ပေးလှူခြင်း | absent | 21,25 |
| gandhaṃ | နံ့သာ (3) | အနံ့ | absent | 21,25,30 |
| kusalaṃ cittaṃ | ကုသိုလ် စိတ် (3) | ကုသိုလ်စိတ် | absent | 21 |
| aṅgaṃ | (no direct equivalent) (3) | အင်္ဂါ | absent | 21,24 |
| hīna | ယုတ်ခြင်း (2) ; ချို့ယွင်းသော (1) | ယုတ်ညံ့သော | absent | 22,29 |
| sassato | ထာဝရ တည်မြဲသော (3) | ထာဝရ တည်မြဲသည် ; ထာဝရ တည်သော | present | 22,31 |
| arūpadhātu | ရုပ်မရှိသော ဓာတ် (3) | ရုပ်မရှိသော ဘုံ | absent | 24 |
| bhūtā | ဖြစ်စေနိုင်သော (2) ; ဓာတ်ကြီး (1) | မူလဓာတ် | present | 24 |
| jīvitā | (no direct equivalent) (3) | အသက် | absent | 28 |
| saññī | မှတ်ထင်သော (3) | မှတ်သိသော ; မှတ်သိမှု ရှိသော | absent | 28 |
| pañcaṅgiko maggo | မဂ်သည် အင်္ဂါ ငါးပါး ရှိသော (3) | အင်္ဂါ ငါးပါး ရှိသော မဂ် | present | 28 |
| pisuṇaṃ | ကုန်းချောစကား (3) | ကုန်းတိုက်သော စကား | absent | 30,31 |
| dukkhā | ဆင်းရဲ (2) | နာကျင်သော ; ဒုက္ခ | present | 16,28 |
| manāpā | နှစ်သက်ဖွယ် ကောင်းသော (2) | စိတ်တွေ့သော ; စိတ်နှင့် တွေ့သော | absent | 16 |
| iṭṭhā | လိုလားဖွယ် ကောင်းသော (2) | လိုလားဖွယ်ကောင်းသော | absent | 16 |
| kantā | ချစ်ခင်ဖွယ် ကောင်းသော (2) | ချစ်ခင်ဖွယ်ကောင်းသော ; နှစ်သက်သော | absent | 16 |
| bhāvo | (no direct equivalent) (2) | သဘော | absent | 16 |
| sabbattha | (no direct equivalent) (1) ; နေရာတိုင်း (1) | ဘုံ အားလုံး | absent | 16,28 |
| dukkhaṃ | ဆင်းရဲ (2) | နာကျင်မှု ; ဒုက္ခ | present | 16,23 |
| bhijjati | ပျက်သည် (2) | ပြိုကွဲသည် | absent | 16,23 |
| dassāvī | ရှုမြင်သော (2) | မြင်လေ့ရှိသော | absent | 17 |
| ñāṇa | သိခြင်း (2) | ဉာဏ် | absent | 17 |
| micchā | မှားသည် (2) | မှားယွင်းသော | absent | 17 |
| kāmo | လို (2) | ကာမ | absent | 17 |
| pātubhūtaṃ | ထင်ရှား ပေါ်ပေါက်သော (2) | ထင်ရှားလာပြီးသော | absent | 17,27 |
| nibbattaṃ | ဖြစ်မြောက်သော (1) ; ဖြစ်ထွန်းသော (1) | ပေါ်ထွက်ပြီးသော | absent | 17,27 |
| dussilyaṃ | သီလ ပျက်ခြင်း (2) | သီလ ဖောက်ဖျက်မှု | absent | 18 |
| aniccatā | မမြဲခြင်း သဘော (2) | မမြဲခြင်း | present | 19 |
| pādā | ခြေ (2) | ပါဒ် | absent | 19,22 |
| upādā | စွဲလမ်းမှု (2) | မူလဓာတ်ကြီးများကို မှီ၍ ဖြစ်သော | absent | 19 |
| sattama | ခုနစ်ကြိမ်မြောက် (2) | သတ္တမ | absent | 20 |
| asaṃvaro | မစောင့်စည်းမှု (2) | မစောင့်စည်းခြင်း | absent | 20 |
| katānaṃ | ပြုခဲ့ (2) | ပြုခဲ့သော | absent | 20,25 |
| yaṃ | (no direct equivalent) (2) | ရှိသမျှ | absent | 20,22 |
| amanussa | လူ မဟုတ်သော (2) | လူ မဟုတ်သူ | absent | 20 |
| rato | မွေ့လျော်သော (2) | ပျော်ပိုက်သော | absent | 21,28 |
| pajānāti | သိသည် (2) | ကွဲပြားစွာ သိသည် ; သိတော်မူသည် | absent | 21,24 |
| rāgo | တပ်မက်မှု (2) | ရာဂ | absent | 21 |
| yaṃ kiñci | အကြင် (1) ; ဟူသမျှ (1) | မည်သည့် … မဆို | absent | 21,22 |
| avihiṃsā | မညှဉ်းပန်းခြင်း (2) | ညှဉ်းပန်းမှု မရှိခြင်း | absent | 22 |
| abyāpāda | မဖျက်ဆီးလိုခြင်း (2) | ဖျက်ဆီးလိုစိတ် မရှိခြင်း | absent | 22 |
| aññamañña | အချင်းချင်း (2) | အချင်းချင်း အကြောင်းဖြစ်ခြင်း | absent | 23 |
| Paccayatā | အကြောင်းဖြစ်ပုံ (2) | ဤအကြောင်းကြောင့် ဤအကျိုး ဖြစ်ပုံ | absent | 23 |
| satthaṃ | လက်နက် (2) | ဓား | absent | 23,25 |
| pāpaṃ | ယုတ်မာမှု (2) | ယုတ်မာသော | absent | 24 |
| vihāraṃ | နေခြင်း (2) | နေထိုင်ရန် | absent | 24 |
| sukhavihāraṃ | ချမ်းသာစွာ နေခြင်း (2) | သာယာစွာ နေထိုင်ရန် ဖြစ်သော | absent | 24 |
| rūpadhātu | သိမ်မွေ့သော ရုပ် ဓာတ် (2) | အဆင်းအရောင် ဓာတ် ; သိမ်မွေ့သော ရုပ်ဘုံ | absent | 24 |
| seṭṭho | မြတ်သော (1) ; အမြတ်ဆုံး (1) | အကောင်းဆုံး | absent | 25,28 |
| Buddho | ဘုရားရှင် (2) | နားလည်အပ်သော | absent | 26 |
| jāte | မျိုး (2) | တစ်မျိုးတည်းမှ ဖြစ်သော | absent | 26 |
| saraṇaṃ | ကိုးကွယ်ရာ (2) | ပဋိပက္ခ ရှိသော | absent | 27 |
| nimuggo | နစ်မြုပ်သော (2) | နစ်နေသော | absent | 27 |
| Pañcaṅgiko maggo | မဂ်သည် အင်္ဂါ ငါးပါး ရှိသော (2) | အင်္ဂါ ငါးပါး ရှိသော မဂ် | present | 28 |
| dhammā niyatā | သဘောတရား … ကျိန်းသေသော (2) | ကျိန်းသေသော သဘောတရား | present | 29 |
| dhammaṃ | အကျင့် (2) | သဘောတရား ; တရား | absent | 30,31 |
| Dukkhaṃ | ဆင်းရဲ (2) | နာကျင်မှု ; ဒုက္ခ | present | 31 |
| āhārā | အစာ (1) | အာဟာရ | absent | 16 |
| kāyo | အပေါင်း (1) | ကိုယ် ; စိတ်၏ အဖော်တို့ | absent | 16 |
| sāvaka | သာဝက (1) | တပည့် | absent | 16 |
| purisassa | ယောကျ်ား (1) | ယောက်ျား | absent | 16 |
| dhīrā | ပညာရှိ (1) | ပညာရှိသော | absent | 16 |
| rūpino dhammā | ရုပ် … သဘောတရား (1) | ရုပ် ဖြစ်သော သဘောတရား | present | 16 |
| su | မွှေးသော (1) | ကောင်းစွာ | absent | 16 |
| puriso | ယောကျ်ား (1) | အမျိုးသား ; သူတော်ကောင်း | absent | 16 |
| samiddhi | သမိဒ္ဓိ (1) | ကောင်းစွာ ပြည့်စုံခြင်း | absent | 16 |
| sattānaṃ | အသညသတ် (1) | သတ္တဝါ | absent | 16 |
| avaseso | အကြွင်း (1) | ကြွင်းကျန်သော | absent | 16 |
| phalā | ဖိုလ် (1) | အသီးအပွင့် | absent | 16 |
| uppāda | ထွက်စေခြင်း (1) | ဖြစ်ပေါ်ခြင်း | absent | 16 |
| vāda | ပြောခြင်း (1) | ဝါဒ | absent | 16 |
| ādāna | ယူခြင်း (1) | ကိုင်ခြင်း | absent | 16 |
| pahīyanti | ပယ်ခံရသည် (1) | ပျောက်ကင်းသည် | absent | 17 |
| attato | အတ္တ (1) | အတ္တဟု | present | 17 |
| samitaṃ | အစဉ်တစိုက် (1) | ငြိမ်းသော | absent | 17 |
| Sabbaso | အခါခပ်သိမ်း (1) | အလုံးစုံ | absent | 17 |
| uppādā | ဖြစ်ပေါ်သော (1) | ဖြစ်ပေါ်မှု ; ဖြစ်ပေါ်ရာ | absent | 17 |
| aññaṃ | အခြား (1) | တခြားစီ ; တခြား | absent | 17 |
| vipariṇataṃ | ဖောက်ပြန်ပြောင်းလဲပြီးသော (1) | ဖောက်ပြန် ပြောင်းလဲပြီးသော | present | 17 |
| abbhatthaṅgataṃ | လုံးဝ ကွယ်ပြီးသော (1) | လုံးဝ ကွယ်ပျောက်ပြီးသော | absent | 17 |
| abhinibbattaṃ | ထင်ရှားစွာ ဖြစ်မြောက်သော (1) | ထင်ရှားစွာ ပေါ်ထွက်ပြီးသော | absent | 17 |
| vigataṃ | ကင်းကွာပြီးသော (1) | ကင်းပျောက်ပြီးသော | absent | 17 |
| sabbaso | အခါခပ်သိမ်း (1) | အလုံးစုံ | absent | 17 |
| jhāyī | ဈာန်ဝင်သော (1) | ဈာန်ဝင်စားသူ | absent | 17 |
| lābhī | ရသော (1) | ရရှိသော | absent | 17 |
| iṭṭha | လိုလားအပ်သော (1) | လိုလားဖွယ် | absent | 18 |
| Aniṭṭha | မလိုလားအပ်သော (1) | မလိုလားဖွယ် | absent | 18 |
| gāmino | သွားသော (1) | ရောက်သော | absent | 18 |
| kammaṃ | ပြုမူခြင်း (1) | ပြုခြင်း ; ကံ | absent | 18 |
| āsana | နေရာ (1) | ထိုင်ခုံ | absent | 18 |
| Dussilyaṃ | သီလ ပျက်ခြင်း (1) | သီလ ဖောက်ဖျက်မှု | absent | 18 |
| avasesaṃ | အကြွင်း (1) | ကြွင်းကျန်သော | absent | 19 |
| ekanta | တစ်ထစ်ချ (1) | လုံးဝ ; စင်စစ် | absent | 19 |
| Eka | တစ် (1) | တစ်မျိုးတွဲ ; တစ်စေ့ | absent | 19 |
| Aniccatā | မမြဲခြင်း သဘော (1) | မမြဲခြင်း | present | 19 |
| bhedo | ပြိုပျက်ခြင်း (1) | ကွဲခြင်း ; ကွဲထွက်ခြင်း | absent | 19 |
| Asaṃvaro | မစောင့်စည်းမှု (1) | မစောင့်စည်းခြင်း | absent | 20 |
| bhāṇī | ပြောဆိုသော (1) | စကားပြောသော | absent | 20 |
| anāgāmi | အနာဂါမ် (1) | အနာဂါမိ | absent | 20 |
| sakadāgāmi | သကဒါဂါမ် (1) | သကဒါဂါမိ | absent | 20 |
| sikkhāya | သိက္ခာ (1) | ကျင့်စဉ် | absent | 20 |
| ṭhita | တည်မြဲသော (1) | တည်ငြိမ်သော ; တည်နေစေသော | absent | 20 |
| vādī | တစ်ဖက်သား (1) | ပြောသော | absent | 20 |
| rāga | တပ်မက်မှု (1) | ရာဂ | absent | 21 |
| vagga | ဝဂ် (1) | ဂိုဏ်းဖွဲ့၍ | absent | 21 |
| vuṭṭhānaṃ | ထမြောက်ရန် (1) | ထမြောက်ခြင်း | absent | 21 |
| uppāditaṃ | ဖြစ်ပေါ်စေခဲ့ပြီးသော (1) | ထွက်စေအပ်သော | absent | 21 |
| paṭivinodetvā | ပယ်ဖျောက်၍ (1) | ဖယ်ရှားပြီး | present | 21 |
| okkamituṃ | မသက်ဆင်းနိုင် (1) | သက်ဆင်းရန် | absent | 21 |
| Niyato | လမ်းကြောင်း သေချာပြီးသော (1) | ကျိန်းသေသော ; လမ်းကြောင်း ကျိန်းသေသူ | absent | 21 |
| Micchattaniyato | မှားယွင်းမှု၌ လမ်းကြောင်း သေချာပြီးသော (1) | မှားယွင်းမှု၌ ကျိန်းသေသော | absent | 21 |
| niyato | လမ်းကြောင်း သေချာပြီးသော (1) | ကျိန်းသေသော ; လမ်းကြောင်း ကျိန်းသေသူ | absent | 21 |
| mahā | မဟာ (1) | မြတ်သော | absent | 21 |
| sīsaṃ | ဦးခေါင်း (1) | ရှေ့တန်း | absent | 22 |
| saṇṭhāti | တည်သည် (1) | တည်နေသည် | absent | 22 |
| yāpeti | အသက် မွေးသည် (1) | မျှတစေသည် ; ဆက်လက် ရှင်သန်စေသည် | absent | 22 |
| Yaṃ | (no direct equivalent) (1) | ရှိသမျှ | absent | 22 |
| akusalaṃ cittaṃ | အကုသိုလ် စိတ် (1) | အကုသိုလ်စိတ် | absent | 22 |
| ahitāya | အစီးအပွား မဖြစ်ဖွယ်ရာ (1) | အစီးအပွား မရှိခြင်း | absent | 22 |
| dukkhāya | ဆင်းရဲဖွယ်ရာ (1) | နာကျင်သော ; ဆင်းရဲခြင်း | absent | 22 |
| abyākatā dhammā | ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော … သဘောတရား (1) | ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော သဘောတရား | present | 23 |
| aṅgānaṃ | (no direct equivalent) (1) | အင်္ဂါ | absent | 23 |
| jātaṃ | ပေါ်ပေါက်သော (1) | ဖြစ်ပေါ်သော ; မွေးဖွားပြီးသော | absent | 23 |
| kappo | ကမ္ဘာ (1) | သင့်လျော်သည် | absent | 23 |
| mano | စိတ် (1) | မနော | absent | 23 |
| upapajjati | ပြန်လည် ဖြစ်ပေါ်သည် (1) | ရောက်ရသည် | absent | 23 |
| Yo | (no direct equivalent) (1) | ရှိသမျှ ; အကြင် | absent | 25 |
| vattati | ဖြစ်သည် (1) | လည်ပတ်သည် ; ဖြစ်ပေါ်သည် | absent | 25 |
| pariññāya | ပိုင်းခြား သိရန် (1) | ပိုင်းခြား သိ၍ | present | 25 |
| ṭhitā | တည်ပြီးသော (1) | တည်နေသော | absent | 25 |
| appameyyo | အတိုင်းအဆ မရှိသော (1) | ချိန်ဆ၍ မရနိုင်သူ | absent | 25 |
| uddissa | ရည်စူး၍ (1) | ရည်ရွယ်၍ | absent | 25 |
| ṭhānaṃ | ဌာန (1) | အကြောင်း ; နေရာ | absent | 25 |
| samāhito | ပြည့်စုံသော (1) | တည်ကြည်သော | absent | 25 |
| paṭipannā | ကျင့်ကြံဆဲသော (1) | ကျင့်ကြံသော | absent | 25 |
| Vineyya | ဖယ်ရှား၍ (1) | ပယ်ဖျောက်၍ ; ပယ်ဖျောက်လျက် | absent | 25 |
| pavaro | အထူးမြတ်ဆုံး (1) | အမွန်မြတ်ဆုံး | present | 25 |
| veḷu | ဝေဠုဝန် (1) | ဝါး | absent | 26 |
| dhamma | ဓမ္မ (1) | သဘောတရား ; တရား | absent | 26 |
| vihāra | ကျောင်း (1) | နေထိုင်ရာ ; ဗြဟ္မစိုရ် | absent | 26 |
| cakkaṃ | စကြာ (1) | တရားစက် | absent | 26 |
| viharati | နေတော်မူသည် (1) | နေသည် | absent | 26 |
| dullabhā | ရှားပါးသော (1) | ရခဲသော | absent | 26 |
| abhiññāya | ထူးကဲစွာ သိ၍ (1) | ထူးကဲစွာ သိခြင်း | absent | 26 |
| samāpattiṃ | သမာပတ် (1) | ဈာန် ဝင်စားရာ ; ဈာန် | absent | 26 |
| Bhagavā | မြတ်စွာဘုရား (1) | ဘုန်းတော်ရှင် | absent | 26 |
| niruddhaṃ | ချုပ်ငြိမ်းပြီး (1) | ချုပ်ငြိမ်းပြီးသော | absent | 26 |
| paṭivijānāti | ခွဲခြား သိသည် (1) | ပိုင်းခြား၍ သိသည် | absent | 26 |
| patigādha | ခြေကုတ်ရာ မြေ (1) | ခြေကုပ်ရာ | absent | 27 |
| viloketi | ဝေ့ဝဲ ကြည့်သည် (1) | ပတ်ဝန်းကျင်ကို ကြည့်သည် ; ဘေးသို့ ကြည့်သည် | absent | 27 |
| dvākāre | (no direct equivalent) (1) | အခြင်းအရာ ဆိုးသော | absent | 27 |
| raja | မြူ (1) | ဖုန်လုံး ; မြူမှုန် | absent | 27 |
| suviññāpaye | သိအောင် ပြရ လွယ်ကူသော (1) | သိအောင် ပြောပြရ လွယ်သော | absent | 27 |
| duviññāpaye | (no direct equivalent) (1) | သိအောင် ပြောပြရ ခက်သော | absent | 27 |
| viññāpaye | သိအောင် ပြရ (1) | သိအောင် ပြောပြရ | absent | 27 |
| voropitā | သတ်ခဲ့ပြီးသော (1) | ချခံရသော | absent | 28 |
| Vagga | ဝဂ် (1) | ဂိုဏ်းဖွဲ့၍ | absent | 28 |
| tiriyaṃ | ဘေး (1) | ဖီလာ | absent | 28 |
| bandhanaṃ | အနှောင် (1) | အချည်အနှောင် | absent | 28 |
| pāde | ခြေ (1) | ခြေတစ်ဖက် | absent | 28 |
| kaṭukā | ခါးသက်သော (1) | နာကျင်စေသော ; ခါးသက်စေသော | absent | 28 |
| pharitvā | ပျံ့နှံ့၍ (1) | ပျံ့နှံ့စေ၍ | absent | 28 |
| tiṭṭhati | တည်နေသည် (1) | ရပ်တည်နေသည် ; တည်သည် | absent | 28 |
| makkhikā | ယင် (1) | ယင်ကောင် | absent | 28 |
| yuttaṃ | ကပ်ထားသော (1) | သင့်လျော်စွာ | absent | 28 |
| seyyathidaṃ | ယင်းမှာ (1) | ဆိုလိုသည်မှာ | absent | 28 |
| pāripūriṃ | ပြည့်စုံခြင်း (1) | ပြည့်စုံမှု ; ကိုယ်အင်္ဂါ ပြည့်စုံခြင်း | absent | 28 |
| para | အခြား (1) | သူတစ်ပါး ; ပရ | absent | 28 |
| nicca | အမြဲ (1) | မြဲသော | absent | 29 |
| pana | (no direct equivalent) (1) | တစ်ဖန် | absent | 29 |
| aṅga | (no direct equivalent) (1) | အင်္ဂါ | absent | 29 |
| upaṭṭhāko | အလုပ်အကျွေး (1) | လုပ်ကျွေးပြုစုသူ | absent | 29 |
| pattaṃ | သပိတ် (1) | ရောက် | absent | 29 |
| buddhā | ဘုရား (1) | ဘုရားရှင် | absent | 29 |
| dhāreti | ဆောင်သည် (1) | ဝတ်သည် | absent | 29 |
| mātā | (no direct equivalent) (1) | အမိ ; မိခင် | absent | 29 |
| dha | သဘောတရားများကို စုစည်းရေတွက်ခြင်း (1) | “ဓမ္မပဒ” | absent | 29 |
| upaṭṭhita | ထင်ရှား တည်သော (1) | တည်နေသော | absent | 30 |
| kiriyābyākate | ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော ကြိယာ (1) | ပြုရုံမျှသာ ဖြစ်သော ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော သဘောတရား | absent | 30 |
| samanantarā | ချက်ချင်း (1) | ချက်ချင်း နောက်၌ ; အခြားမဲ့ | absent | 30 |
| ratta | ညဉ့်ဦးယံ ညဉ့်နောက်ယံ (1) | ညဉ့်အခါ | absent | 30 |
| ghoso | အသံ (1) | အသံဗလံ | absent | 30 |
| kareyya | လုယက်သည် (1) | ပြုသည် | absent | 30 |
| pisuṇāya | ကုန်းချောစကား (1) | ကုန်းတိုက်သော | absent | 30 |
| saṃvattanikā | ပို့ဆောင်တတ်သော (1) | ဖြစ်စေသော ; ဖြစ်စေတတ်သော | absent | 30 |
| samannāhāro | နှလုံးသွင်းမှု (1) | နှလုံးသွင်းခြင်း ; စိတ်ကို ဆောင်ခြင်း | absent | 30 |
| ajjhattikaṃ | မိမိ၏ (1) | အတွင်းပိုင်း | absent | 30 |
| pātubhāvo | ထင်ရှား ဖြစ်ပေါ်ခြင်း (1) | ထင်ရှား လာခြင်း | absent | 30 |
| vipariṇāmadhammā | ဖောက်ပြန်ပြောင်းလဲခြင်း … သဘော ရှိသော (1) | ဖောက်ပြန်ခြင်း သဘော ရှိသော ; ဖောက်ပြန်ပြောင်းလဲတတ်သော သဘော ရှိသော | absent | 30 |
| vaṇṇa | အသွင် (1) | အဆင်းလှခြင်း ; အရောင် | absent | 31 |
| ghātako | ဖျက်ဆီးရမည့် (1) | သတ်သူ | absent | 31 |
| citta | စိတ္တ (1) | စိတ် | absent | 31 |
| upapajjeyya | ပြန်လည် ဖြစ်ပေါ်သည် (1) | ရောက်သည် | absent | 31 |
| samaye | အယူဝါဒ (1) | အချိန် | absent | 31 |

## (no direct equivalent) (61)

āvāha (^5-503); bhāvo (^5-519, ^5-523); sabbattha (^5-525); potaliputtassa (^5-539); sañña (^5-543, ^5-23-10-1-0); vattabbe (^5-545); jano (^5-556, ^5-587, ^5-606, ^5-608, ^5-613, ^5-701, ^5-710, ^5-879, ^5-880, ^5-891); aṅgo (^5-557, ^5-616, ^5-709, ^5-724, ^5-726, ^5-728); bhāva (^5-621); aṅgā (^5-642, ^5-643, ^5-878); yaṃ (^5-649, ^5-708); abhabbo (^5-661); aṅgaṃ (^5-663, ^5-743, ^5-745); nibbattati (^5-692); Yaṃ (^5-692); aṅgānaṃ (^5-726); upame (^5-748); Yo (^5-780); viharanti (^5-798); janassa (^5-847, ^5-848, ^5-851, ^5-856, ^5-863, ^5-864, ^5-865, ^5-877); kho (^5-851); dvākāre (^5-856); duviññāpaye (^5-856); jīvitā (^5-857, ^5-858, ^5-859); karonti (^5-868); pana (^5-884); aṅga (^5-885); mātā (^5-886); hareyya (^5-901); hātabbaṃ (^5-908); haranti (^5-909). Reasons: compound member inside one Burmese word (jano, janassa, aṅga*, bhāvo/bhāva, sañña, āvāha, mātā, upame); only in a Roman-script variant or siglum (sabbattha, potaliputtassa, vattabbe, nibbattati, viharanti, kho, dvākāre, duviññāpaye, karonti ^5-868); relative pronouns without the correlative (Yo, Yaṃ, yaṃ: Q7); one Burmese verb for two keywords (abhabbo ^5-661, hareyya, hātabbaṃ, haranti, jīvitā ^5-857 … ^5-859); particle (pana ^5-884).

## Text inconsistencies (for the rails step; the translation was not changed)

1. **ယောကျ်ား / ယောက်ျား**: ch16 ^5-514, ^5-539 spell «ယောကျ်ား» (purisassa, moghapuriso); ch1 and ch22 ^5-708
   «ယောက်ျား».
2. **The siglum «(sabbattha)»** stays Roman in the Burmese bracket ^5-525 «[ပါဌ်ကွဲ (Sabbattha): arūpadhātuyā]».
3. **iṭṭha**: «လိုလားဖွယ်» (ch1), «လိုလားဖွယ် ကောင်းသော» (^5-512), «လိုလားအပ်သော» (^5-591).
4. **parinipphanna** three renderings: «ပြည့်စုံစွာ ဖြစ်ပေါ်ပြီး» (ch19), «အမှန်တကယ် ဖြစ်ပေါ်ပြီး» (ch23 addhā …),
   «ပြည့်စုံစွာ ပြီးမြောက်» (ch31 Aparinipphanna).
5. **upacaya**: kammūpacaya «ကံ၏ စုဆောင်းမှု» (ch23) vs puññūpacaya «ကောင်းမှု စုဆောင်းခြင်း» (ch25, and
   puññasañcaya ch28).
6. **The same sutta passage, two wordings**: «sañcetanikānaṃ kammānaṃ … apare vā pariyāye» = «ရည်ရွယ်၍ … ထို့နောက်
   အခြား ဘဝ အလှည့်၌» (^5-635) vs «စေ့ဆော်၍ … နောက်ထပ် ဘဝအဆက်ဆက်၌» (^5-782); the arahant list ^5-778 (ch25)
   «စုပုံ / ဖြန့်ကြဲ / ဖြိုဖျက်» vs ^5-894 (ch30) «စုစည်း / ဖြန့်ကျက် / ဖျက်ဆီး»; saṃvattaniya «ရောက်စေတတ်သော»
   (^5-777) vs «ပို့ဆောင်တတ်သော» (^5-894, ^5-903); āneñja «မတုန်လှုပ်သော» (^5-777) vs «မတုန်မလှုပ်သော» (^5-894,
   ^5-896); sobhagya «ကောင်းသော ကံကြမ္မာ» vs «ကောင်းကျိုး ချမ်းသာ».
7. **The ten-crimes list** ^5-784 (ch25) vs ^5-901 (ch30) / ^5-908 (ch31): pisuṇaṃ «ကုန်းတိုက်သော စကား» vs
   «ကုန်းချောစကား»; samphaṃ «အကျိုးမဲ့ ပြိန်ဖျင်းသော စကား» vs «အကျိုးမဲ့ စကား»; nillopaṃ hareyya «ဓားပြ တိုက်» vs
   «လုယက်»; paripanthe tiṭṭheyya «လမ်း၌ စောင့်ဆိုင်းလုယက်» vs «လမ်း၌ ဓားပြ တိုက်»; ekāgārikaṃ «အိမ်တစ်အိမ်တည်းကို
   ဝိုင်းဝန်း၍» vs «အိမ်တစ်လုံးကို ဝိုင်းဝန်း»; bhojanīyaṃ «ဘောဇဉ်» vs «စားဖွယ်»; asuci «မစင်ကြယ်သော သုက်ထွက်ခြင်း»
   (^5-535) vs «မစင်ကြယ်သော သုက်».
8. **purisayuga** «လူ အတွဲ» (ch1) vs «လူ အစုံ» (^5-791); **dvipadānaṃ** «ခြေနှစ်ချောင်း» (^5-799) vs «ခြေ နှစ်ချောင်း»
   (^5-872); **āpāyiko / nerayiko** «အပါယ်သို့ ရောက်သူ / ငရဲ၌ ကျသူ» (^5-657) vs «… ရောက်မည့် / … ကျမည့်» (^5-861);
   **kāraṇikā** «ညှဉ်းပန်း နှိပ်စက်သူ» (^5-866) vs «လေ့ကျင့်ပေးသူ» (^5-871, different sense, correct).
9. **^5-858 / ^5-859 «mātaraṃ jīvitā voropetvā»** = «အမိကို သတ်၍» (jīvitā not rendered; ^5-857 likewise) while ch20
   ^5-641 «jīvitā voropito» = «အသက်မှ ချခံရ»; mapped jīvitā = (no direct equivalent) there.
10. **^5-918 uddāna** «Mahāniyāmo» = «ကြီးမားသော အစု၊ သေချာသော လမ်းကြောင်း» (the compound split in two items).
11. **The vagga ordinal spellings** follow the text (ဒသမ, ဧကာဒသမ … တေဝီသတိမ); dhammacakka «ဓမ္မစကြာ» as ch3.

## Unclear mappings (for review)

1. **mā** (^5-622 «mā nirujjhi») = «မ» (by analogy with pi-1 rule 9 «free na = the text's prefix မ»); the Burmese
   prohibitive is «မ … ပါစေနှင့်».
2. **abhabbo … okkamituṃ** (^5-661) = abhabbo (no direct equivalent), okkamituṃ «မသက်ဆင်းနိုင်» (one Burmese verb, as
   ch1 appiyaṃ karitvā); elsewhere Abhabbo «မထိုက်တန်သော» (^5-641).
3. **nillopaṃ hareyya / hātabbaṃ / haranti** (ch30, ch31) = nillopaṃ «လုယက်», the verb (no direct equivalent) (one
   Burmese verb «လုယက်…»); ^5-784 (ch25) keeps «ဓားပြ / တိုက်သည်» as that text has it.
4. **manasikārā** (^5-576 «na amanasikārā») = «နှလုံး သွင်း» (positive part of «နှလုံး မသွင်းဘဲ»); **katānaṃ**
   (^5-635) «ပြုခဲ့» bare (text «ပြုခဲ့ ဆည်းပူးခဲ့သော»); **apahattā / upahattā** (^5-748) «ဖယ်ရှားပေးတော်မူ /
   ဆောင်ယူပေးတော်မူ» (agent nouns rendered as verbs «…ပေးတော်မူခဲ့ပေစွ»; P6 «…သူ» is not in the text);
   **viharituṃ / iddhiyā paggahetuṃ / vādeti** bare stems as the text has them («နေ», «ဣဒ္ဓိဖြင့် ထိန်းထား», «တီးမှုတ်»).
5. **satta** ^5-626 «satta rattindivāni» = «ခုနစ်», rattindivāni «ရက် … ညဉ့်» (one written word «ခုနစ်ရက်ခုနစ်ညဉ့်»).
6. **sañña / satta / sattānaṃ** of asaññasatta (^5-508, ^5-543, ^5-23-10-1-0, ^5-735, ^5-736) = «အသညသတ်» for the one
   that carries it, the other (no direct equivalent).
7. **pana** ^5-884 (no direct equivalent); **bhāvo / bhāva** of attabhāva (no direct equivalent); atta of attabhāva =
   «ကိုယ်» (a member of «ကိုယ်ခန္ဓာ»).
8. **Kappaṭṭho** «ကမ္ဘာ ပတ်လုံး တည်ရမည့်သူ» and the person types kolaṅkolo / ekabījī / sattakkhattuparamo «…သူ» kept
   as names (P1); their -tāniyato «…၏ အဖြစ်၌ ကျိန်းသေသော».
9. **dha** = the reference sigla: ch1 «dha. pa.» «“ဓမ္မပဒ”», ^5-887 «dha. sa.» «သဘောတရားများကို စုစည်းရေတွက်ခြင်း»
   (as the text translates it).
