# pi-7 Burmese keyword mapping, phase 2, group g3 (part 3 gocchakas 3-01 … 3-08)

Script `map_g3.py` (imports `map7_rules.py`, md5 909bed2528b27eb55051c73f3ce28f81, unchanged). It holds the group table
`T_G3`, the generated item table (G1) and one per-segment override (`CTX`). The translation is not changed. Two runs
give byte-identical `.mapped.md` files.

## Numbers

| chapter | lines | bad | presence failures | «, » / «၊» / « / » | (no direct equivalent) | chunks by an ending rule |
|---|---|---|---|---|---|---|
| 3-01-hetugocchaka | 430 | [] | 0 | 0 | 4 | 127 |
| 3-02-culantaraduka | 467 | [] | 0 | 0 | 8 | 97 |
| 3-03-asavagocchaka | 296 | [] | 0 | 0 | 7 | 54 |
| 3-04-sannojanagocchaka | 269 | [] | 0 | 0 | 5 | 64 |
| 3-05-ganthagocchaka | 266 | [] | 0 | 0 | 6 | 72 |
| 3-06-oghayogagocchaka | 3 | [] | 0 | 0 | 0 | 1 |
| 3-07-nivaranagocchaka | 262 | [] | 0 | 0 | 6 | 60 |
| 3-08-paramasagocchaka | 224 | [] | 0 | 0 | 6 | 46 |
| total | 2217 | [] | 0 | 0 | 42 | 521 |

- Ending-rule chunks are approved verifier rules only: attr-fut 219 (gerundive «…ရမည့်» against «…ရမည်»), verb 172
  («…သည်» against the text's ending), attr 130 («…သော» against «…သည် / …လျက် / …၍»). There are no other exceptions.
- The 42 (no direct equivalent) are: katvā / karoti after uposathakammaṃ (U2, f_karoti) and ceva (rule 9).
- **S1 review:** 115 stem-fallback uses, all checked by eye. 112 were kept and 3 corrected.
  - Kept: rūpī / Rūpī / rūpissa «ရုပ် ဖြစ်သော» 72 (as STOCK rūpino; the text's form), passati «မြင်သည်» 22,
    vibhajitabbaṃ «ခွဲခြမ်းစိတ်ဖြာရမည့်» 8 (FRAME vibhajitabbā), ganthasampayuttakā «အထုံးနှင့် ယှဉ်တွဲသော» 6,
    patthayamāno «တောင့်တသော» 1 (rule 3, text «တောင့်တလျက်» by the approved attr ending), lokuttarasa
    «လောကကို ကျော်လွန်သော» 1 (a Pāli slip for lokuttarassa), ekekampi «တစ်ခုစီ» 1, ninnānākaraṇā «ကွဲပြားချက် မရှိ» 2
    (FRAME ninnānākaraṇaṃ), itare «အခြား» 1.
  - Corrected:
    - suddhake: «ရိုးရိုး» to «ရိုးရိုး အပိုင်း»;
    - assādanā: a verb «သာယာ» given to a noun, corrected to the text's noun «သာယာ နှစ်သက်ခြင်း»;
    - paccavekkhitvā: «ဆင်ခြင်၍» to «ပြန်လည် ဆင်ခြင်၍» (U3, the pi-7 word).
- **Newly mapped:** 239 uses in 52 keywords that the module left unmapped. All are in `T_G3`, and the main ones are
  listed below.
- **Module values overridden:** 149 uses in 33 keyword / value pairs (`map_g3.py --over` lists them).
- **Against pi-1 … pi-6:** 11765 uses keep a pi-1 … pi-6 value of the keyword or its base form. 13509 uses have no
  prior value. 1065 uses differ, in 48 pairs (`work/diff_g3.py`). Almost all of these are the phase-1 module
  differences already approved (T1 / T2 condition names, U1 assādeti, U2 katvā, U3 paccavekkhati, datvā / deti,
  STOCK vatthu …). The ones this group adds are listed below.

## Rules used

- pi-1 rules 1–11 and the later pi-1 rules (absolutives «…၍», counts with the text's classifier).
- pi-2 N1–N11, pi-3 M1–M9, pi-4 P1–P8, pi-5 Q1–Q8 / S1, pi-6 R1–R9 and the phase-3 mechanics.
- The phase-1 rules T1–T13, M1 and M2, and the coordinator's decisions U1–U5, all unchanged, with one exception: the
  item value of T13 (G1 below).

## New rules (with reasons)

- **G1. The item term of a gocchaka dyad is the bare noun N in every case.** This covers āsava, saññojana, gantha,
  ogha, yoga, nīvaraṇa and parāmāsa (Āsavo / Āsavaṃ / āsavassa / Āsavañca / Saññojanañceva / nīvaraṇānañca …).
  - Its negative no-X is «N မဟုတ်သော» (T8).
  - The text's «N ဖြစ်သော» is the copula of the predicated noun: pi-1 rule 2, «a noun predicated = the noun».
  - The binding pi-1 mātikā values come from the same kind of segment, the dyad term: [1-M2-1] hetū «အမြစ်»,
    [1-M2-14] āsavā «စိတ်အစွန်းအထင်း», [1-M2-20] saṃyojanā «နှောင်ကြိုး» (spelling saṃyojana for saññojana, as T7's
    upādiṇṇa / upādinna). pi-2 has āsavo, gantho, nīvaraṇaṃ and parāmāso with the same value, and pi-5 has oghaṃ.
  - Why the change was needed: the module gave the bare noun wherever a pi value existed (Āsavo, Gantho, Nīvaraṇo,
    Parāmāso, Oghaṃ). It gave T13's «N ဖြစ်သော» elsewhere: every saññojana form, Yogaṃ, and the -ca / -ceva forms
    Āsavañca, Ganthañceva, Parāmāsañca. The same frame therefore came out two ways. The clearest case is 3-06, where
    «Oghaṃ dhammaṃ» got «ရေအလျဉ်» and «Yogaṃ dhammaṃ» got «ထမ်းပိုး ဖြစ်သော». R1 was also broken: Āsavañca
    «… ဖြစ်သော» against Āsavaṃ «စိတ်အစွန်းအထင်း».
  - G1 makes the item consistent across the group and agrees with pi-1. It overrides only T13's item example
    (saññojano «နှောင်ကြိုး ဖြစ်သော»). T13's X-sampayutta, X-vippayutta and X-iya values are unchanged.
- **G2. The named members of a gocchaka**, as the text writes them: «X နှောင်ကြိုး», «… ဟူသော ကိုယ် အထုံး».
  - kāmarāga / diṭṭhi / avijjā / vicikicchā / māna / sīlabbataparāmāsa-saññojanaṃ;
  - idaṃsaccābhinivesa(kāyaganthaṃ), on the model of pi-1 abhijjhākāyagantho «…ခြင်းဟူသော ကိုယ် အထုံး»;
  - when kāyaganthaṃ is its own keyword, idaṃsaccābhinivesaṃ is «ဤအရာသာ အမှန်ဟု သက်ဝင်ယုံကြည်ခြင်း» (rule 1: «ဟူသော»
    goes), as pi-5 sīlabbataparāmāsaṃ.
- **G3. Stacked qualifiers in one compound:** diṭṭhigatavippayuttalobhasahagata- is «အယူမှားနှင့် ကင်းကွာသော လောဘနှင့်အတူ
  ဖြစ်သော» (T7 / rule 6: the text's «၊» goes), 95 uses, and its -adhipati is «… အကြီးအမှူး» (T12).
- **G4. Gerundives of the notes** are rule 3 «…ရမည့်», the text's verb:
  - vajjetabbā «ဖယ်ရှားရမည့်», niyāmetabbaṃ «သတ်မှတ်ရမည့်», dassetabba- «ပြသရမည့်», bandhitabbaṃ «ဖွဲ့ရမည့်»;
  - uddharitabbā «ထုတ်နုတ်ရမည့်», ninnetabbaṃ «ထည့်သွင်းရမည့်», parivattetabbā «လှည့်ပြောင်းရမည့်», kātabbāni «ပြုရမည့်».
- **G5. The other new values**, all from the text:
  - -sadisa notes (T5): lokiyaduka- / paṭhamaduka- / ganthaduka- / parāmāsaduka-sadisaṃ «… နှစ်မျိုးတွဲနှင့် တူသည်»;
    dutiyagamanasadisaṃ, the adverbial «ဒုတိယ သွားပုံနှင့် တူအောင်» before «ပြုရမည်»; ekasadisā «တူညီသည်»;
  - pavatteyeva «ဘဝ ဖြစ်စဉ်» (eva «ပင်», rule 9); pavattipaṭisandhi «ဘဝ ဖြစ်စဉ် … ပဋိသန္ဓေ» (rule 10 / R7, the text's
    «…၌လည်း၊ …၌လည်း»);
  - (pañc)āyatanāni «အာရုံခံ နယ်ပယ် ငါးပါး»; garukārammaṇā «လေးစားဖွယ်ရာ အာရုံ»;
  - upanissayā in «(tīṇi upanissayā)» is «အားကြီးသော အမှီ»: the kind, not the condition name, which the text does not
    have there;
  - naviññeyyo / -aṃ «မသိနိုင်သော» (the text's form); nahetucittasamaṅgissa «အမြစ် မဟုတ်သော စိတ်နှင့် ပြည့်စုံသူ» (T12);
  - noganthādhipati «အထုံး မဟုတ်သော အကြီးအမှူး»; vibhajantena «ခွဲခြမ်းစိတ်ဖြာလျက်» (as FRAME anumajjantena, H10);
  - jānitvā «သိ၍», agge «ရှေ့ဆုံး», utu «ရာသီဥတု», vaṇṇasampadaṃ «အဆင်းအရောင် ပြည့်စုံခြင်း»;
  - ṭhānāṭhānakosallassa «ဖြစ်နိုင်ခြင်းနှင့် မဖြစ်နိုင်ခြင်း၌ ကျွမ်းကျင်ခြင်း»; Dvikkhattuṃ «နှစ်ကြိမ်», catukkhattuṃ
    «လေးကြိမ်», ubhopete «ထိုနှစ်ပါးလုံး».

## Module overrides (for phase 3)

| keyword | module | g3 | uses | reason |
|---|---|---|---|---|
| item forms of the 7 gocchakas (G1) | «N ဖြစ်သော» / «N … ဖြစ်သော» | «N» | 82 | G1: pi-1 rule 2 and the binding pi-1 mātikā values; consistency with the pi-2 / pi-5 items |
| nosaññojanañca, noganthañca | «N ဖြစ်သော … မဟုတ်» | «N မဟုတ်သော» | 3 | T8; the module's gapped pick joined two different terms |
| cakkaṃ | စက် | စက်ဝိုင်း | 45 | the text's word «(စက်ဝိုင်း)»; «စက်» is only part of it |
| tadārammaṇatā | စိတ်သည် | ထိုအာရုံကိုပင် အာရုံပြုသော အဖြစ် | 8 | module error: the generator value «စိတ်သည် + …» was read as the term. The same wrong value «စိတ်သည်» is in the phase-1 sample 1-02 (5 uses) |
| pañcaviññāṇaṃ | သိစိတ် | သိစိတ် ငါးပါး | 1 | the text's phrase |
| paripuṇṇo / paripuṇṇā | ပြည့်စုံ | ပြည့်စုံသော | 4 | rule 3, as FRAME paripuṇṇaṃ (text «ပြည့်စုံသည် / ပြည့်စုံကြသည်») |
| gaṇetabbā | ရေတွက်ရမည် | ရေတွက်ရမည့် | 3 | rule 3 gerundive, as FRAME gaṇetabbaṃ |
| uppādenti | ဖြစ်စေကြသည် | ဖြစ်စေသည် | 1 | rule 4, as LEXW uppādeti (the plural «ကြ» by the ending rule) |
| Nahetuṃ (^7-24-6) | အမြစ်ဟူသော အကြောင်းကြောင့် မဟုတ် | အမြစ် မဟုတ်သော | 1 | the dyad term «Nahetuṃ dhammaṃ» (T8), not the condition |
| Ārammaṇañca (^7-28-116, CTX) | အာရုံ | အာရုံဟူသော အကြောင်း | 1 | the note «Ārammaṇañca sahajātañca upanissayañca … parivattetabbaṃ» names conditions (T1, R1) |

The phase-3 module could take G1 as a change to cluster_cands and the R1 order, so that a -ca form takes its base
form's value. It could also take the tadārammaṇatā and cakkaṃ values.

## Values that differ from pi-1 … pi-6 (added by this group)

- cakkaṃ «စက်ဝိုင်း» (prior «လှည့်ပတ်ခြင်း», not in the segment).
- agge «ရှေ့ဆုံး» (pi-2 «ဖျား», not in the segment).
- pavatteyeva «ဘဝ ဖြစ်စဉ်» (pi-6 pavatte «ဘဝ တည်နေစဉ်», not in the segment).
- uppādenti «ဖြစ်စေသည်» (prior «ဖြစ်ပေါ်စေသည်», not in the segment).
- Yogaṃ «ထမ်းပိုး» (a prior (no direct equivalent) of another sense of yogaṃ).
- Ārammaṇañca «အာရုံဟူသော အကြောင်း» (prior «အာရုံ»: T1).
- rūpī / arūpī «ရုပ် ဖြစ်သော / ရုပ် မဟုတ်သော» (prior «ရုပ် ရှိသော / ရုပ် မရှိသော», not in the segments; the module's STOCK
  rūpino / arūpino).

The remaining differences come from the phase-1 module, for the reasons in `map-table.md`.

## Text inconsistencies (for the rails step)

1. **pavatti**: pi-7 «ဘဝ ဖြစ်စဉ်» (3-01 ^7-24-77, ^7-24-169, ^7-24-180; 3-02), against pi-6 pavatte «ဘဝ တည်နေစဉ်».
2. **naviññeyyo / -aṃ**: the text has «(…စိတ်ဖြင့်) မသိနိုင်သော», not the na-X form of harmonise H21 («သိနိုင်သည်
   မဟုတ်သော»). It is correct as Burmese. Only the na-X rule's consistency is in question.
3. **rūpī / arūpī**: pi-7 «ရုပ် ဖြစ်သော / ရုပ် မဟုတ်သော», against pi-1 … pi-6 «ရုပ် ရှိသော / ရုပ် မရှိသော».
4. **Pāli slips**, mapped as written:
   - lokuttarasa for lokuttarassa (3-02);
   - idaṃsaccābhinivesaṃ kāyaganthaṃ (two words) beside idaṃsaccābhinivesakāyaganthaṃ (3-05 ^7-28-1 / ^7-28-103).
5. **tadārammaṇatā**: the text writes «… ကံ၏ အကျိုး ဖြစ်သော စိတ်သည် ထိုအာရုံကိုပင် အာရုံပြုသော အဖြစ်ဖြင့်». The head noun
   «စိတ်» is supplied (as §A5 of phase 1).
6. **The -sadisa adverbial** «ဒုတိယ သွားပုံနှင့် တူအောင် ပြုရမည်» (^7-24-19) is the third shape of phase-1 §A4.

## Unclear mappings (for the coordinator)

- **G1 against T13**: the gocchaka item is mapped «N». The alternative is T13's «N ဖြစ်သော» everywhere, which would
  override the binding pi-1 / pi-2 / pi-5 values in about 200 more uses. Phase 3 should settle one value book-wide;
  3-09 upādāna and 4-01 kilesa have the same frame.
- **upanissayā** «(tīṇi upanissayā)» is «အားကြီးသော အမှီ», the bare kind. The text has no «…ဟူသော အကြောင်း» there.
- **patthayamāno** keeps «တောင့်တသော» (rule 3 with the approved «လျက်» ending). vibhajantena takes the text's
  «…လျက်», as FRAME anumajjantena. These are two participle forms with two precedents.
- **natthi** keeps the module's «မရှိသည်» (f_natthi, the pi-value by ending rule) in the notes «(… natthi)».
