# pi-5 Burmese keyword mapping, PHASE 2, group ch2–15: notes

Script `map_ch2-15.py` (imports `map5_rules.py`, which was not edited; tables T_GROUP / T[ch], CTX, FUNCS2). Burmese only
from this track's FINAL pi-5 text, `my5-zeroshot-terms.md`, the phase-1 tables (`map_ch1.py`) and the final pi-1 … pi-4
mappings. pi-1-my … pi-4-my were not opened for writing; `map-table.md` / `map-harmonise-notes.md` untouched.

## Numbers

| chapter | lines | bad | presence failures | «, » / «၊» / « / » | (no direct equivalent) |
|---|---|---|---|---|---|
| 2-parihanikatha | 34 | [] | 0 | 0 | 11 |
| 3-brahmacariyakatha | 14 | [] | 0 | 0 | 2 |
| 4-jahatikatha | 6 | [] | 0 | 0 | 4 |
| 5-sabbamatthitikatha | 26 | [] | 0 | 0 | 6 |
| 6-atitakkhandhadikatha | 5 | [] | 0 | 0 | 0 |
| 7-ekaccam-atthitikatha | 5 | [] | 0 | 0 | 0 |
| 8-satipatthanakatha | 4 | [] | 0 | 0 | 2 |
| 9-hevatthikatha | 4 | [] | 0 | 0 | 0 |
| 10-dutiyavaggo | 69 | [] | 0 | 0 | 36 |
| 11-tatiyavaggo | 57 | [] | 0 | 0 | 23 |
| 12-catutthavaggo | 51 | [] | 0 | 0 | 13 |
| 13-pancamavaggo | 47 | [] | 0 | 0 | 4 |
| 14-chatthavaggo | 46 | [] | 0 | 0 | 1 |
| 15-sattamavaggo | 52 | [] | 0 | 0 | 4 |

420 lines, 9,241 keyword uses, 106 (no direct equivalent). The brief's preservation one-liner prints `bad []` for all 14.
Source of the values (uses): table 2654, pi-2 2477, frame 1028, compose 983, stem 726, stock 508, pi-4 428, terms 179,
pi-1 170, pi-3 78, ctx 10. 3,975 uses carry a value that pi-1 … pi-4 have for the same keyword.

## Rules used

All phase-1 rules unchanged: pi-1 rules 1–11 and the later agreed rules, pi-2 N1–N11 and decisions, pi-3 M1–M9, pi-4
P1–P8 / A2, the phase-1 Q1–Q8, and the coordinator's decisions (appiyaṃ «ဦးစားမပေး» + karitvā none; Āmantā whole;
-ī / -vādī «…သော», agent nouns «…သူ»; bhikkhave «ရဟန်း»). Most used: rule 1 (no final particles; inner particles of a
phrase stay), rule 3 (participles «…သော», gerundives «…မည့်»), rule 4 (verbs «…သည်»), rule 8 (a fragment that lost
its negative = the positive part: sañjātaṃ «ဖြစ်ပေါ်သော» from «မဖြစ်ပေါ်သေး»), rule 10 (« … »), pi-2 decision 4 (one
member of a compound gets the one Burmese word: jana, vaccha, pitaro, sata, vāla, aṅga(o), puna in punabbhava,
vissaṭṭhiṃ, pavane / vane …), pi-3 M2 (a word only inside a Roman variant / reference bracket: @roman), Q3 (members in
text order), Q5 (negated verbs «… မV»), Q8 (-ī adjectives «…သော»; person-type names stay names: kolaṅkolo,
ekabījī).

## NEW rules (group; for review in phase 3)

- **S1 stem fallback.** A single keyword that no table, module entry, pi-5 term or pi-1 … pi-4 value maps takes the
  value of a keyword of the same stem (pi-1 … pi-4, ch1, the module and this group's tables) that the segment's
  Burmese has as a phrase (`stem_value`; 726 uses, all reviewed by listing; wrong ones were overridden in the tables).
- **S2 every table value is checked against the segment.** Where the segment lacks a table value, the module's chain
  takes over (pi-1 … pi-4, stem, compose). A tuple («a», «b», …) gives per-segment alternatives (one sense per segment,
  the first the text has as a phrase, then one present by the ending rules).
- **S3 negated multiword keywords** («na / no V S», also «S na V», «S … na V»): the members in text order with the
  text's «မ + verb» and no «သည်» / «သော» (Q5 extended; `f_neg`), e.g. Na parihāyati anāgāmī = «အနာဂါမ် … မဆုတ်ယုတ်»,
  ekadesaṃ na samannāgato = «တစ်စိတ်တစ်ဒေသ … မပြည့်စုံ».
- **S4 the ch1 table is a book-wide fallback** (`f_ch1`): a T_CH1 keyword takes its ch1 value where the segment has it,
  else the module's chain.
- **S5 present participles** in -nta (passato, jānanto, dakkhanto, dadantassa …) = «…သော» (rule 3), the text's
  «…သူ / …လျက် / …စဉ်» normalised; **infinitives** keep the verb «…သည်» (abhisametuṃ, aññātuṃ) or the text's «…ရန်»
  where pi-1 … pi-4 have it (pahānāya «ပယ်ရန်» pattern: kātuṃ, pamocanāya, ocinituṃ …).
- **S6 privative compounds** that are keywords themselves keep the text's «မ…» (aviññū «နားမလည်တတ်သော», Aṭṭhānaṃ
  «အကြောင်း မဟုတ်», adiṭṭhaṃ «မမြင်ရသေးသော») as ch1 appiyaṃ; their extractor fragments without a- take the positive
  part (rule 8).

## Module overrides (for the coordinator; module not edited)

| keyword | module value | group value | where / why |
|---|---|---|---|
| Saṃkhittaṃ | FRAME «အကျဉ်းချုပ်» | «တွန့်ဆုတ်နေသော» | CTX ^5-436 «saṃkhittaṃ cittaṃ» (the citta adjective) |
| Sabbattha | FRAME «နေရာတိုင်း» | «ဘုံ အားလုံး» | ch11 ^5-355 sabbatthagāminiṃ |
| katvā | @katva | «မှတ်ယူ၍» | CTX ^5-282 «Ayoganti katvā» «မဆက်စပ်ဟု မှတ်ယူ၍» |
| karonti | @karoti | «ဆောက်သည်» | CTX ^5-461 gharāni karonti |
| vata | @vata | (no direct equivalent) | ^5-377 «Ime vata bhonto sattā» (phase-1 note); vata of sīlabbata = «အကျင့်ဝတ်» kept |
| paṇidhi | @panidhi | «ဆုတောင်းမှု» | ^5-378 Theragāthā verse |
| para | @para | «ကျော်» | CTX ^5-402 parosahassaṃ «တစ်ထောင်ကျော်» (first in the Pāli) |
| gati | @gati | «သွားလာခြင်း» | ^5-271 «yattha natthi gati bhikkhūnaṃ» |
| aññā | @anna_f | «သိ၍» / «ရဟန္တာ ဖိုလ်» | sammadaññāvimutto (^5-261, ^5-277 …); aññāpaṭivedho ^5-346 |
| parinibbuto | STOCK «ပရိနိဗ္ဗာန် ပြုပြီးသော» | «ပရိနိဗ္ဗာန် ပြုတော်မူသော» | ^5-281 text «ပြုတော်မူပြီ» |
| parinibbute | STOCK «… ပြုတော်မူပြီးသော» | «ပရိနိဗ္ဗာန် စံဝင်တော်မူပြီးသော» | ^5-296 |
| nirodhadhammaṃ | STOCK «ချုပ်ငြိမ်းတတ်သော သဘော … ရှိသော» | «ချုပ်ငြိမ်းခြင်း သဘော ရှိသော» | ch10 ^5-317, ^5-321, ^5-325, ^5-346 |
| sukhadukkhaṃ | STOCK «ချမ်းသာနှင့် ဆင်းရဲ» | «ချမ်းသာ ဆင်းရဲ» | ^5-488 |
| Sayaṃ | STOCK «မိမိ» | «ကိုယ်တိုင်» | ^5-405 «sayaṃ abhiññāya» |
| thero | pi-4 «ထေရ်» | «မထေရ်» | ch2, ch12 text «မထေရ်» («ထေရ်» kept where the text has it, ^5-346) |

Module mechanics worth a look in phase 3 (worked around here): `neg_value` checks a gapped «S … မV» as one literal
phrase and so never finds it (S3 replaces it); `glue` joins «ရဟန္တာ၏ ဆုတ်ယုတ်…» from a «…ခြင်း» noun phrase
(CTX ^5-239); `phrase_ok` does not accept the perf-pred «Xပြီး ဖြစ်» that `presence` accepts, so «Xကို
ပွားများပြီးသော» was not glued (tuples maggo bhāvito / bojjhaṅgā bhāvitā).

## Values that differ from pi-1 … pi-4 or from ch1 (same keyword), with the reason

All are the pi-5 text's own words for the segment (presence-checked); the main groups:
- **Different sense / construction**: phalā «ဖိုလ်» (path fruit) vs ch1 «အသီးအပွင့်»; kamma «အလုပ်» (kammārāmatā)
  vs «ကံ»; dhamma «အရာ» (sadhammakusala), «ဓမ္မ» (dhammacakka) vs «သဘောတရား»; kusalassa «ကျွမ်းကျင်သော» vs
  «ကုသိုလ်»; sukka «သုက်» vs «ဖြူစင်သော»; assa «မြင်း» vs «ထိုသူ»; nāma «အမည်» vs «စိတ်ပိုင်း»; setu «သေတု» (name)
  vs «တံတား»; hatthako «ဟတ္ထက» (name) vs ch1 «လက်»; Citto «စိတ္တ» (name); maṃsa «ပကတိ» (maṃsacakkhu); saha
  «တစ်ပြိုင်နက်» (saha dassanuppādā) vs «အတူ»; bhedo «စကား ထွက်ခြင်း» (vacībheda) vs «ကွဲခြင်း»; āhāro «ဆိုခြင်း»
  (dukkhāhāra) vs «အာဟာရ»; ñāṇa «သိခြင်း» (aññāṇa headings); saraṇaṃ «ကိုးကွယ်ရာ»; dakkhiṇaṃ «အလှူ»; bho «အသျှင်»;
  vatthu «ငုတ်တို» (tālāvatthu); lohitaṃ «သွေး»; upādā «စွဲလမ်းမှု» (anupādā, phase-1 rule).
- **The pi-5 text's word for the same sense**: samāpannassa «သမာပတ်ကို ဝင်စားနေသော» vs pi «ဈာန် ဝင်စားသော»;
  upasampajja «ပြည့်စုံစွာ ဝင်ရောက်၍» vs «ဝင်စား၍»; pahīyanti «ပယ်သည်» vs «ပျောက်ကင်းသည်»; bhagavā «မြတ်စွာဘုရား»
  vs «ဘုန်းတော်ရှင်»; sammāsambuddhā «… ဘုရားရှင်» (preamble) vs pi-2 «… ဘုရား»; thero «မထေရ်»; samodhānaṃ
  «ပေါင်းဆုံခြင်း»; yāpenti «အသက်မွေးသည်»; cetasiko «စိတ်၏ အဖော်»; vimutti «လွတ်မြောက်ခြင်း»; jāto
  «ဖွားမြင်တော်မူသော» (the Buddha) vs ch1 «မွေးဖွားလာသော»; paññāpeti «သတ်မှတ်ဖော်ပြသည်» vs ch1 «ပညတ်သည်»;
  upacchedo «ဖြတ်တောက်ခြင်း» vs ch1 «ပြတ်ခြင်း»; tasmā «ထို့ကြောင့်» vs ch1 «သောကြောင့်»; pātubhavanti «ထင်ရှား
  ပေါ်လာသည်» vs ch1 «ပေါ်ပေါက်သည်».
- **Form rules**: participles «…သော» where pi has a noun or «…သူ» (vimuttaṃ, anottappī «… ရှိသော»); FRAME kathā
  «ဆွေးနွေးချက်» (156) and vata «အမှန်ပင်» (111) vs pi-1 … pi-4 (phase-1 decisions).

## Text inconsistencies (for the rails step; translation not edited)

1. **^5-371 omission**: «Aṭṭhamako puggalo duppañño elamūgoti? Na hevaṃ vattabbe…pe…» has no Burmese (the text goes
   from «… ပညာ ရှိသလော» to the saddhā question). duppañño, elamūgo = (no direct equivalent) (CTX).
2. **dhammacakka**: ch3 ^5-270 «ဓမ္မစကြာ» vs ch12 ^5-405 «တရားစက်».
3. **ruhiruppādaka**: ch3 ^5-269 «ဘုရားရှင်၏ သွေးကို ထွက်စေသူ» vs ch10 ^5-333 «… သွေးကို စိမ်းစေသူ».
4. **The jāta / niruddha series**: ch5 ^5-283/^5-284 «မဖြစ်သေး / ကင်းကွာ / ကွယ်» vs ch7 ^5-299/^5-300 «မမွေးဖွားသေး /
   ကင်းပျောက် / ကွယ်ပျောက်» for the same Pāli lists (jātaṃ, vigataṃ, atthaṅgataṃ …); ch6 has «ကင်းပျောက်».
5. **parinibbuta**: ch4 ^5-281 «ပရိနိဗ္ဗာန် ပြုတော်မူပြီ», ch5 ^5-296 «ပရိနိဗ္ဗာန် စံဝင်တော်မူပြီးသော», module «ပြုပြီးသော».
6. **thera**: «မထေရ်» (ch2 ^5-264, ch12 ^5-389) vs «ထေရ်» (ch10 ^5-346 «ဂဝမ္ပတိ ထေရ်»).
7. **Spelling**: «ယောက်ျား» vs «ယောကျ်ား» (ch12 ^5-402 «ယောကျ်ားမြတ်», ch15 ^5-491 «ယောကျ်ားကောင်း»).
8. **paṭikuṭṭha**: ch5 ^5-296 «မကန့်ကွက်အပ်ကြ» vs ch15 ^5-480 «မကဲ့ရဲ့အပ်ကုန်» for the same formula.
9. **sukhadukkha**: «ချမ်းသာနှင့် ဆင်းရဲ» (ch1) vs «ချမ်းသာ ဆင်းရဲ» (ch15 ^5-488).
10. **nirodhadhamma**: «ချုပ်ငြိမ်းတတ်သော သဘော ရှိ» (ch3 ^5-278) vs «ချုပ်ငြိမ်းခြင်း သဘော ရှိ» (ch10) in the same
    stock phrase «yaṃ kiñci samudayadhammaṃ …».
11. **uddāna / pucchā**: the vagga headings «Catutthavaggo / Chaṭṭhavaggo / Sattamavaggo» are repeated on every kathā
    heading line (11 each) and map to «… ဝဂ်»; no change.

## Unclear mappings (for review)

- **satasahassa** «သိန်း» (^5-239): sahassehi = «သိန်း», sata = (no direct equivalent) (one Burmese word).
- **sukkavissaṭṭhiṃ** (accusative, ^5-308) «မစင်ကြယ်သော သုက်ကို»: sukkavissaṭṭhiṃ = «သုက်», vissaṭṭhiṃ = (no direct
  equivalent); the nominative keeps «သုက်ထွက်ခြင်း».
- **Taññeva** «ထို … ပင်»; **sabbena sabbaṃ / sabbathā** «အလုံးစုံ … လုံးဝ».
- **bhabba / abhabba**: «ထိုက်တန်သော / မထိုက်တန်» (pi), but in ch3 ^5-269 and ch13 the text's «…နိုင်» (sakkā):
  bhabbā «သက်ဆင်းနိုင်သော», abhabbā «မသက်ဆင်းနိုင်», abhabba «မစွမ်းနိုင်».
- **samāpanna** with a separately listed jhāna / samāpatti keyword: «သမာပတ်ကို ဝင်စားနေသော» includes the object; the
  alternative is «ဝင်စားနေသော» alone (used where the text has another object).
- **akkhāsi / bhonto / vediyā** in verses: the nearest Burmese word («ဟောကြားတော်မူခဲ့သည်», «အချင်း», «ဖြစ်သော»).
- **S1 stem values** (726 uses) are the least certain group; the review list is printed by
  `work/diag215.py <ch> uniq | grep '<stem>'`.
