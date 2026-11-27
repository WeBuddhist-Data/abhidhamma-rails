# pi-2 Burmese keyword mapping: rules and review table (Vibhaṅga «ခွဲခြမ်းစိတ်ဖြာခြင်း», SAMPLE: preamble, 1-khandhavibhango)

Written by map_all.py. Burmese from the FINAL pi-2 text of this track only (AI_translation/burmese/pi-2-burmese-plain-zeroshot_split_chapters); pi-1 values from AI_translation/burmese/pi-1-keywords-by-reference-pali-burmese-plain.md. No other Burmese source.

## Verification

| chapter | lines | keyword preservation | presence failures | comma / ၊ / « / » | rule-matched chunks | (no direct equivalent) |
|---|---|---|---|---|---|---|
| preamble | 3 | bad [] | 0 | [] | 1 | 1 |
| 1-khandhavibhango | 169 | bad [] | 0 | [] | 63 | 0 |

## Reuse of pi-1

- Keyword uses: 4132; distinct keywords: 649.
- Keywords that pi-1 also has: 283 distinct; their values taken **unchanged from pi-1**: 277 distinct keyword-value pairs, 1819 uses.
- Keywords new in pi-2 (not in the pi-1 mapping): 366 distinct.

### Values that differ from pi-1 for the same keyword

| keyword | pi-2 value (uses) | pi-1 value(s) | reason |
|---|---|---|---|
| ajjhattaṃ | မိမိ၌ ရှိသော (2) | မိမိ၌ (46) | pi-1 «မိမိ၌» is the jhāna adverb (ajjhattaṃ sampasādanaṃ); here the attributive qualifier of the question / the ajjhatta list item (pi-1 ^1-1050 wording), one sense per segment |
| ajjhattaṃ | မိမိ၏ အတွင်း၌ ဖြစ်သော (3) | မိမိ၌ (46) | pi-1 «မိမိ၌» is the jhāna adverb (ajjhattaṃ sampasādanaṃ); here the attributive qualifier of the question / the ajjhatta list item (pi-1 ^1-1050 wording), one sense per segment |
| bahiddhā | မိမိ၏ ပြင်ပ၌ (1) | ပြင်ပ၌ (45) · သူတစ်ပါး၌ (12) · အပြင်ဘက် (6) | pi-1 «သူတစ်ပါး၌ / ပြင်ပ၌ / အပြင်ဘက်» do not occur as the term: the pi-2 text's qualifier is «မိမိ၏ ပြင်ပ၌» |
| hīno | ယုတ်ညံ့သော (9) | ယုတ်ညံ့သူ (2) | pi-1 «ယုတ်ညံ့သူ» is a person; here the quality of a feeling (Mātikā hīnā «ယုတ်ညံ့သော») |
| paccayā | အကြောင်းပြု၍ (4) | ကြောင့် (1) | pi-1 «ကြောင့်» is the dependent-origination chain; here «X-samphassapaccayā» = «Xကို အကြောင်းပြု၍ ဖြစ်သော» |
| uppanno | ဖြစ်ပေါ်ပြီးသော (9) | ဖြစ်ပေါ်သော (7) | pi-1 «ဖြစ်ပေါ်သော» is «uppanno ca vicāro» (cittuppāda); here the Mātikā triad uppanna «ဖြစ်ပေါ်ပြီးသော» (pi-1 uppannā) |
| vuccati rūpaṃ | ရုပ်ဟု ခေါ်သည် (1) | ရုပ်ပိုင်းဟု ခေါ်သည် (1) | pi-1 «ရုပ်ပိုင်း» is the nāma-rūpa pair (^1-1317); here matter |

## Rules

The value is the word or phrase of THAT segment's Burmese (the FINAL pi-2 text) that carries the keyword, in the
dictionary form of the approved pi-1 Burmese mapping. **Binding and unchanged:** pi-1 `map-table.md` rules 1–11
(approved sample) and the agreed later pi-1 rules (`map-table-2-01 … -5.md`, `map-harmonise-notes.md`): absolutives
keep «…၍»; «samaye X» = «အချိန်၌ ရှိသော X» (no such keyword in this sample); relative pronouns Yo / Yā / Yaṃ =
(no direct equivalent) where the Burmese builds the clause with «ရှိသော / ရှိသမျှ» (no bare relative is a keyword
here); one sense per segment; no « / » alternatives; caya = (no direct equivalent) where apacaya is one word (no
bare caya here). pi-1 values are reused for the same keyword in the same kind of segment when they occur in the pi-2
segment (the script looks every keyword up in the final pi-1 mapping first, after its own table).

Rules this sample uses that pi-1 already had, applied to the Vibhaṅga's new shapes:

- **Nouns** (pi-1 rule 1): no case particle, no plural at the end: vedanāhi / saññāhi = ခံစားမှု / မှတ်သိမှု;
  khandhānaṃ = အစုအဝေး; parapuggalānaṃ = အခြား ပုဂ္ဂိုလ်; atītaṃsena = အတိတ် အပိုင်း. Inside a phrase the text's
  particles stay (atītaṃsena saṅgahitā = အတိတ် အပိုင်း၌ အကျုံးဝင်သော; tadekajjhaṃ = ထိုအားလုံးကို တစ်စုတည်း).
- **Predicated qualifiers** (pi-1 rule 3, the nominal «…သည်» normalised to «…သော»): «Akusalā vedanā oḷārikā» =
  «အကုသိုလ် ခံစားမှုသည် ရုန့်ရင်းသည်» gives oḷārikā = ရုန့်ရင်းသော, sukhumā = နုညံ့သော, the same values as the
  attributive oḷārikaṃ / sukhumaṃ of pi-1.
- **Inflected Mātikā items** (pi-1 3 rule 12): the masculine -o (kusalo, sāsavo, pahātabbahetuko …), the neuter -aṃ
  and the plural -ā of a Mātikā term keep the Mātikā value (head noun not included, rule 3); the cluster
  compounds follow pi-1 4 rule 14 (āsavavippayuttasāsavo = စိတ်အစွန်းအထင်းနှင့် ကင်းကွာသော … စိတ်အစွန်းအထင်း၏
  အာရုံ ဖြစ်နိုင်သော, the left-out «သဘောတရားများအနက်» is the gap) and the CEVA strings of pi-1 (hetu ceva
  hetusampayutto = အမြစ်လည်း ဖြစ် အမြစ်နှင့်လည်း ယှဉ်တွဲသော, «၊» dropped, rule 6).
- **«na / no X»** (pi-1 rule 5): the text's negative attributive «…သည် မဟုတ်သော» (na kāmāvacaro =
  ကာမဘုံနှင့် ဆိုင်သည် မဟုတ်သော).
- **Subject + predicate pairs** (pi-1 5 rule 21): «Rūpakkhandho hetuvippayutto» = ရုပ် အစုအဝေး … အမြစ်နှင့်
  ကင်းကွာသော; «khandhā siyā» = အစုအဝေး … တစ်ခါတစ်ရံ (the count «လေးပါး» belongs to Cattāro, not to the keyword,
  pi-1 5 rule 15).
- **Gerundives** (pi-1 pahātabbā = ပယ်ရမည့်, check «attr-fut»): daṭṭhabbā / daṭṭhabbaṃ = မှတ်ယူရမည့် (text
  «… မှတ်ယူရမည်»).
- **vuccati X** (pi-1 4 rule 13) = «Xဟု ခေါ်သည်»; bare vuccati / vuccanti = ခေါ်သည် (rule 4). The text keeps the plural
  inside «vuccanti saṅkhārā» = ပြုပြင်ဖန်တီးမှုများဟု ခေါ်သည် (rule 1 strips particles only at the end).
- **Fragments** (pi-1 rule 8): upakaṭṭhe (first in anupakaṭṭhe) = အနားကပ်သော; āpacaya = လျော့ပါးခြင်း; gāmī (from
  nevācayagāmināpacayagāmī) = ဦးတည်သော; ādhipati / ādhipatino = အကြီးအမှူး (rule 2); hetuko / hetukaṃ = အမြစ် (rule 2);
  ābhibhūtaṃ = လွှမ်းမိုးခံရသော; ānuparivatti = နောက်သို့ လိုက်ပါသော; viññāṇadhātu = သိစိတ် ဓာတ်; Tika = သုံးမျိုးတွဲ.
- **The time lists** (pi-1 4-01 rule 16): in a segment with all three lists the fragments jātaṃ, nibbattaṃ,
  abhinibbattaṃ, pātubhūtaṃ, uppannaṃ, uṭṭhitaṃ, samuṭṭhitaṃ occur whole only in the «arisen» list = «…ပြီးသော»
  (pi-1 1-1046): uppannaṃ / uppannā / uppanno = ဖြစ်ပေါ်ပြီးသော everywhere in this chapter (also the Mātikā uppannā).
- **Sense by context, one sense per segment** (pi-1 harmonise decision 3): rūpa follows the FIRST rūpa compound of
  the Pāli segment (all «ရုပ်» here: rūpakkhandho comes first); ajjhattaṃ = «မိမိ၌ ရှိသော» where its first occurrence is
  the question qualifier («rūpaṃ / viññāṇaṃ ajjhattaṃ?», ^2-4, ^2-28), «မိမိ၏ အတွင်း၌ ဖြစ်သော» (pi-1 ^1-1050 list
  item) where the ajjhatta list comes first (^2-10, ^2-16, ^2-22); uttaro (first in lokuttaro) = ကျော်လွန်သော.
- **Titles and headings** (pi-1 rule 7, decision 4): Vibhaṅgapāḷi / Vibhaṅga / vibhaṅgo = ခွဲခြမ်းစိတ်ဖြာခြင်း;
  Pañhāpucchakaṃ = မေးခွန်းများဖြင့် ဖော်ပြချက် (the heading whole); bhājanīyaṃ = ခွဲခြမ်း ဖော်ပြချက် (pi-1).

## NEW rules (for the user's review)

N1. **pāḷi** in the book title Vibhaṅgapāḷi = (no direct equivalent): the approved title «ခွဲခြမ်းစိတ်ဖြာခြင်း» has no
    word for «the canonical text» (the only (no direct equivalent) of the sample).
N2. **«whatever» openers** Yaṃ kiñci / Yā kāci / Ye keci = «မည်သည့် … မဆို» (text «မည်သည့် ရုပ်မဆို»). Unlike the bare
    relative pronouns (pi-1: no direct equivalent), the text has words for them, so they get the discontinuous value.
    yaṃ vā panaññampi = «အခြား … ရှိသမျှလည်း» (the pi-1 frame «… အခြား ရုပ် ရှိသမျှလည်း»; ရှိသမျှ renders yaṃ … atthi).
N3. **Attributive pairs** «noun + qualifier» / «qualifier + noun» (rūpaṃ atītaṃ, vedanā oḷārikā, Sāsavā vedanā,
    cakkhusamphassajā saññā, abyākataṃ viññāṇaṃ …) = the Burmese order qualifier + noun, the text's noun phrase
    (rūpaṃ atītaṃ = အတိတ် ရုပ်); vuccati + pair = the pair + «ဟု ခေါ်သည်».
N4. **Numbers of kinds**: Ekavidhena … Bahuvidhena = «Nမျိုး» (the instrumental ဖြင့် goes, rule 1, as pi-1
    vidhena = မျိုး); the text's «ကြည့်လျှင်» (when viewed) is the frame, not the keyword. «dasavidhena Xkkhandho» =
    «ဆယ်မျိုး … X အစုအဝေး» (the frame word between is the gap, pi-1 rule 10).
N5. **Coordinated compounds with the head noun between the members** (kusalābyākatā, kusalākusalā, sukhadukkhā,
    akusalābyākatāhi saññāhi): «A … B» (text «ကုသိုလ် ခံစားမှုနှင့် ကုသိုလ်လည်း မဟုတ်၊ … မဟုတ်သော»): the head noun and
    its «နှင့်» fall in the gap, as pi-1 5 rule 16 does when a count stands between the members.
N6. **-dhammo / -dhammaṃ with the aggregate as head**: vipākadhammadhammo = «အကျိုး ပေးတတ်သော» (text «အကျိုး
    ပေးတတ်သော ခံစားမှု»: the final -dhamma has no word); the plural vipākadhammadhammā of the pañhāpucchaka keeps the
    pi-1 value «အကျိုး ပေးတတ်သော သဘောတရား» (rule 5).
N7. **Frame verbs and adverbs**: upādāyupādāya = «နှိုင်းယှဉ်၍» (absolutive, «၍» kept); paccayā in
    X-samphassapaccayā = «အကြောင်းပြု၍» (text «Xကို အကြောင်းပြု၍ ဖြစ်သော»: the conjunctive is the case meaning,
    as pi-1 keeps «ရန်» for datives); abhisaññūhitvā = ပေါင်းစု၍, abhisaṅkhipitvā = အကျဉ်းချုံ့၍; mattaṃ (from
    -vicāramatta) = «သာ» (the text's «only» suffix, as pi-1 eva = သာ); saha (fragment) = «အတူ».
N8. **Section words**: mūlakaṃ = «အခြေခံသော» (pi-1 mūlaka; the text's head «ခွဲနည်း» is not the keyword, rule 3),
    vaḍḍhakaṃ = «တိုးပွားသော», Ubhato = «နှစ်ဘက်စလုံး»; vitthāro = «အကျယ်»; vibhattaṃ = «ခွဲခြားထားသော».
N9. **kenaci** = «တစ်စုံတစ်ခုသော စိတ်» (text «တစ်စုံတစ်ခုသော စိတ်ဖြင့်»): the text names the pronoun's implied noun
    (by some consciousness); kenaci (na) viññeyyo = «တစ်စုံတစ်ခုသော စိတ်ဖြင့် (မ)သိနိုင်သော».
N10. **bahiddhā** (the adverb, also as the Mātikā item «siyā bahiddhā») = «မိမိ၏ ပြင်ပ၌», the pi-2 text's term
    (the eleven qualifiers of the Vibhaṅga), locative kept as pi-1 rule 11; the adjectives bahiddho = «မိမိ၏ ပြင်ပ၌
    ရှိသော», ajjhatto / ajjhattā = «မိမိ၌ ရှိသော», ajjhattabahiddho = «မိမိ၌နှင့် မိမိ၏ ပြင်ပ၌ ရှိသော».
N11. **Presence check, one more ending**: a chunk «Xသော» is accepted against the text's «Xသည့်» (vibhattaṃ in
    «ခွဲခြားထားသည့်အတိုင်း»); the other accepted endings are pi-1's (attr, verb, attr-fut, neg-infix, neg-attr).

## Presence: chunks matched by an ending rule (not literally in the segment)

Every other chunk of every value occurs literally in its segment's Burmese.

| segment | keyword | chunk | rule |
|---|---|---|---|
| T-1 | Namo | ရှိခိုးသည် | verb |
| 2-2 | oḷārikaṃ | ရုန့်ရင်းသော | attr |
| 2-2 | hīnaṃ | ယုတ်ညံ့သော | attr |
| 2-2 | sukhumaṃ | နုညံ့သော | attr |
| 2-2 | paṇītaṃ | မွန်မြတ်သော | attr |
| 2-6 | daṭṭhabbaṃ | မှတ်ယူရမည့် | attr-fut |
| 2-7 | daṭṭhabbaṃ | မှတ်ယူရမည့် | attr-fut |
| 2-8 | oḷārikā | ရုန့်ရင်းသော | attr |
| 2-8 | hīnā | ယုတ်ညံ့သော | attr |
| 2-8 | sukhumā | နုညံ့သော | attr |
| 2-8 | paṇītā | မွန်မြတ်သော | attr |
| 2-11 | samāpannassa | ဝင်စားသော | attr |
| 2-11 | daṭṭhabbā | မှတ်ယူရမည့် | attr-fut |
| 2-12 | samāpannassa | ဝင်စားသော | attr |
| 2-12 | daṭṭhabbā | မှတ်ယူရမည့် | attr-fut |
| 2-13 | samāpannassa | ဝင်စားသော | attr |
| 2-13 | daṭṭhabbā | မှတ်ယူရမည့် | attr-fut |
| 2-14 | oḷārikā | ရုန့်ရင်းသော | attr |
| 2-14 | hīnā | ယုတ်ညံ့သော | attr |
| 2-14 | sukhumā | နုညံ့သော | attr |
| 2-14 | paṇītā | မွန်မြတ်သော | attr |
| 2-17 | samāpannassa | ဝင်စားသော | attr |
| 2-17 | daṭṭhabbā | မှတ်ယူရမည့် | attr-fut |
| 2-18 | samāpannassa | ဝင်စားသော | attr |
| 2-18 | daṭṭhabbā | မှတ်ယူရမည့် | attr-fut |
| 2-19 | samāpannassa | ဝင်စားသော | attr |
| 2-19 | daṭṭhabbā | မှတ်ယူရမည့် | attr-fut |
| 2-20 | oḷārikā | ရုန့်ရင်းသော | attr |
| 2-20 | hīnā | ယုတ်ညံ့သော | attr |
| 2-20 | sukhumā | နုညံ့သော | attr |
| 2-20 | paṇītā | မွန်မြတ်သော | attr |
| 2-23 | samāpannassa | ဝင်စားသော | attr |
| 2-23 | daṭṭhabbā | မှတ်ယူရမည့် | attr-fut |
| 2-24 | samāpannassa | ဝင်စားသော | attr |
| 2-24 | daṭṭhabbā | မှတ်ယူရမည့် | attr-fut |
| 2-25 | samāpannassa | ဝင်စားသော | attr |
| 2-25 | daṭṭhabbā | မှတ်ယူရမည့် | attr-fut |
| 2-26 | oḷārikaṃ | ရုန့်ရင်းသော | attr |
| 2-26 | hīnaṃ | ယုတ်ညံ့သော | attr |
| 2-26 | sukhumaṃ | နုညံ့သော | attr |
| 2-26 | paṇītaṃ | မွန်မြတ်သော | attr |
| 2-29 | samāpannassa | ဝင်စားသော | attr |
| 2-29 | daṭṭhabbaṃ | မှတ်ယူရမည့် | attr-fut |
| 2-30 | samāpannassa | ဝင်စားသော | attr |
| 2-30 | daṭṭhabbaṃ | မှတ်ယူရမည့် | attr-fut |
| 2-31 | samāpannassa | ဝင်စားသော | attr |
| 2-31 | daṭṭhabbaṃ | မှတ်ယူရမည့် | attr-fut |
| 2-33 | jarābhibhūtaṃ | လွှမ်းမိုးခံရသော | attr |
| 2-33 | vibhattaṃ | ခွဲခြားထားသော | attr |
| 2-33 | uppannaṃ | ဖြစ်ပေါ်ပြီးသော | attr |
| 2-33 | saṅkhataṃ | ပြုပြင်ဖန်တီးထားသော | attr |
| 2-33 | vippayuttaṃ | ကင်းကွာသော | attr |
| 2-33 | rūpāvacaraṃ | ဆိုင်သော | attr |
| 2-33 | aniyataṃ | မကျိန်းသေသော | attr |
| 2-33 | arūpāvacaraṃ | ဆိုင်သော | attr |
| 2-33 | aniccaṃ | မမြဲသော | attr |
| 2-33 | gāmī | ဦးတည်သော | attr |
| 2-33 | apariyāpannaṃ | အကျုံးမဝင်သော | attr |
| 2-33 | ābhibhūtaṃ | လွှမ်းမိုးခံရသော | attr |
| 2-33 | vipākadhammadhammaṃ | ပေးတတ်သော | attr |
| 2-33 | kāmāvacaraṃ | ဆိုင်သော | attr |
| 2-33 | āvacaraṃ | ဆိုင်သော | attr |
| 2-33 | lokiyaṃ | သက်ဆိုင်သော | attr |
| 2-153 | niṭṭhito | ပြီးဆုံးသော | attr |

## Keyword → Burmese (uses)

«pi-1» = the value is a pi-1 value of the same keyword. Several values = the keyword reads differently by context.

| Pāli keyword | Burmese (uses) |
|---|---|
| abbhatthaṅgataṃ | လုံးဝ ကွယ်ပျောက်ပြီးသော (2) |
| abbhatthaṅgatā | လုံးဝ ကွယ်ပျောက်ပြီးသော (3, pi-1) |
| Abhidhamma | အဘိဓမ္မာ (3, pi-1) |
| Abhidhammapiṭake | အဘိဓမ္မာပိဋက (1, pi-1) |
| abhinibbattaṃ | ထင်ရှားစွာ ပေါ်ထွက်ပြီးသော (2) |
| abhinibbattā | ထင်ရှားစွာ ပေါ်ထွက်ပြီးသော (3, pi-1) |
| abhisaññūhitvā | ပေါင်းစု၍ (5) |
| abhisaṅkhipitvā | အကျဉ်းချုံ့၍ (5) |
| abyākataṃ | ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော (4, pi-1) |
| abyākataṃ viññāṇaṃ | ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော သိစိတ် (3) |
| abyākato | ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော (26) |
| abyākatā | ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော (10, pi-1) |
| abyākatā saññā | ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော မှတ်သိမှု (3) |
| abyākatā saṅkhārā | ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော ပြုပြင်ဖန်တီးမှု (3) |
| abyākatā vedanā | ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော ခံစားမှု (3) |
| acetasikaṃ | စိတ်၏ အဖော် မဟုတ်သော (1) |
| acittīkataṃ | အလေးမထားသော (1) |
| adhivacanasamphassa | အမည်ခေါ်ဝေါ်မှု၏ တွေ့ထိမှု (1) |
| adhivacanasamphassajā saññā | အမည်ခေါ်ဝေါ်မှု၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော မှတ်သိမှု (1) |
| adukkhamasukhā | မနာကျင် မသာယာသော (5) |
| adukkhamasukhāya | မနာကျင် မသာယာသော (23, pi-1) |
| aganthaniyo | အထုံး၏ အာရုံ မဖြစ်နိုင်သော (6) |
| ahetuko | အမြစ် မရှိသော (10) |
| ajjhattabahiddho | မိမိ၌နှင့် မိမိ၏ ပြင်ပ၌ ရှိသော (9) |
| ajjhattabahiddhā | မိမိ၌နှင့် မိမိ၏ ပြင်ပ၌ ရှိသော (1) |
| ajjhattabahiddhārammaṇo | မိမိ၌နှင့် မိမိ၏ ပြင်ပ၌ ရှိသည်ကို အာရုံပြုသော (20) |
| ajjhattabahiddhārammaṇā | မိမိ၌နှင့် မိမိ၏ ပြင်ပ၌ ရှိသည်ကို အာရုံပြုသော (1) |
| ajjhattaṃ | မိမိ၏ အတွင်း၌ ဖြစ်သော (3) · မိမိ၌ ရှိသော (2) |
| ajjhattikaṃ | အတွင်းပိုင်း (1, pi-1) |
| ajjhattiko | အတွင်းပိုင်း (1) |
| ajjhatto | မိမိ၌ ရှိသော (9) |
| ajjhattā | မိမိ၌ ရှိသော (1) |
| ajjhattārammaṇo | မိမိ၌ ရှိသည်ကို အာရုံပြုသော (20) |
| ajjhattārammaṇā | မိမိ၌ ရှိသည်ကို အာရုံပြုသော (1) |
| akantaṃ | ချစ်ခင်ဖွယ် မကောင်းသော (1) |
| Akusalaṃ | အကုသိုလ် (3, pi-1) |
| Akusalaṃ viññāṇaṃ | အကုသိုလ် သိစိတ် (3) |
| akusalo | အကုသိုလ် (25) |
| Akusalā | အကုသိုလ် (9, pi-1) |
| akusalā | အကုသိုလ် (2, pi-1) |
| Akusalā saññā | အကုသိုလ် မှတ်သိမှု (3) |
| Akusalā saṅkhārā | အကုသိုလ် ပြုပြင်ဖန်တီးမှု (3) |
| Akusalā vedanā | အကုသိုလ် ခံစားမှု (3) |
| akusalābyākatāhi saññāhi | အကုသိုလ် … ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော မှတ်သိမှု (1) |
| amanāpaṃ | စိတ်နှင့် မတွေ့သော (1) |
| aniccaṃ | မမြဲသော (1, pi-1) |
| anidassana | မမြင်နိုင်သော (1, pi-1) |
| anidassanasappaṭigho | မမြင်နိုင်သော်လည်း ထိခိုက်မှု ရှိသော (1) |
| anidassanaṃ | မမြင်နိုင်သော (1, pi-1) |
| anidassanā | မမြင်နိုင်သော (1, pi-1) |
| aniyataṃ | မကျိန်းသေသော (1) |
| aniyato | မကျိန်းသေသော (7) |
| aniṭṭhaṃ | လိုလားဖွယ် မကောင်းသော (1) |
| anoghaniyo | ရေအလျဉ်၏ အာရုံ မဖြစ်နိုင်သော (6) |
| anuttarā | ထိုထက် သာလွန်သည် မရှိသော (1, pi-1) |
| anāgataṃ | အနာဂတ် (2) |
| anāgato | အနာဂတ် (9) |
| anāgatā | အနာဂတ် (3, pi-1) |
| anāgatārammaṇo | အနာဂတ်ကို အာရုံပြုသော (9) |
| anāgatārammaṇā | အနာဂတ်ကို အာရုံပြုသော (1, pi-1) |
| anārammaṇaṃ | အာရုံ မရှိသော (1) |
| anārammaṇo | အာရုံ မရှိသော (2) |
| anāsavaṃ | စိတ်အစွန်းအထင်း၏ အာရုံ မဖြစ်နိုင်သော (3) |
| anāsavaṃ viññāṇaṃ | စိတ်အစွန်းအထင်း၏ အာရုံ မဖြစ်နိုင်သော သိစိတ် (3) |
| anāsavo | စိတ်အစွန်းအထင်း၏ အာရုံ မဖြစ်နိုင်သော (14) |
| anāsavā | စိတ်အစွန်းအထင်း၏ အာရုံ မဖြစ်နိုင်သော (10, pi-1) |
| anāsavā saññā | စိတ်အစွန်းအထင်း၏ အာရုံ မဖြစ်နိုင်သော မှတ်သိမှု (3) |
| anāsavā saṅkhārā | စိတ်အစွန်းအထင်း၏ အာရုံ မဖြစ်နိုင်သော ပြုပြင်ဖန်တီးမှု (3) |
| anāsavā vedanā | စိတ်အစွန်းအထင်း၏ အာရုံ မဖြစ်နိုင်သော ခံစားမှု (3) |
| anīvaraṇiyo | အတားအဆီး၏ အာရုံ မဖြစ်နိုင်သော (2) |
| apacaya | လျော့ပါးခြင်း (10, pi-1) |
| apacayagāmī | လျော့ပါးခြင်းဆီသို့ ဦးတည်သော (9) |
| apariyāpannaṃ | ဘဝဘုံတို့၌ အကျုံးမဝင်သော (1, pi-1) |
| apariyāpanno | ဘဝဘုံတို့၌ အကျုံးမဝင်သော (8) |
| apariyāpannā | ဘဝဘုံတို့၌ အကျုံးမဝင်သော (1, pi-1) |
| appamāṇo | အတိုင်းအဆ မရှိသော (9) |
| appamāṇā | အတိုင်းအဆ မရှိသော (1, pi-1) |
| appamāṇārammaṇo | အတိုင်းအဆ မရှိသည်ကို အာရုံပြုသော (9) |
| appamāṇārammaṇā | အတိုင်းအဆ မရှိသည်ကို အာရုံပြုသော (1, pi-1) |
| arahato | ရဟန္တာ (1, pi-1) |
| araṇo | ပဋိပက္ခ မရှိသော (10) |
| araṇā | ပဋိပက္ခ မရှိသော (1) |
| arūpā | ရုပ် မဟုတ်သော (1) |
| arūpāvacaraṃ | ရုပ်မရှိသော ဘုံနှင့် ဆိုင်သော (1, pi-1) |
| arūpāvacaro | ရုပ်မရှိသော ဘုံနှင့် ဆိုင်သော (13) |
| asaṃkiliṭṭha | ကိလေသာဖြင့် မညစ်နွမ်းသော (11, pi-1) |
| asaṃkiliṭṭhaasaṃkilesiko | ကိလေသာဖြင့်လည်း မညစ်နွမ်း ကိလေသာ၏ အာရုံလည်း မဖြစ်နိုင်သော (5) |
| asaṃkiliṭṭhasaṃkilesiko | ကိလေသာဖြင့် မညစ်နွမ်းသော်လည်း ကိလေသာ၏ အာရုံ ဖြစ်နိုင်သော (5) |
| asaṃkiliṭṭho | ကိလေသာဖြင့် မညစ်နွမ်းသော (5) |
| asaṃyojaniyo | နှောင်ကြိုး၏ အာရုံ မဖြစ်နိုင်သော (13) |
| asaṃyojaniyā | နှောင်ကြိုး၏ အာရုံ မဖြစ်နိုင်သော (1) |
| asekkho | ကျင့်ကြံမှု ပြီးဆုံးသူ၏ (9) |
| asekkhā | ကျင့်ကြံမှု ပြီးဆုံးသူ၏ (1, pi-1) |
| atītaṃ | အတိတ် (2) |
| atītaṃsena | အတိတ် အပိုင်း (5) |
| atītaṃsena saṅgahitaṃ | အတိတ် အပိုင်း၌ အကျုံးဝင်သော (2) |
| atītaṃsena saṅgahitā | အတိတ် အပိုင်း၌ အကျုံးဝင်သော (3) |
| atīto | အတိတ် (9) |
| atītā | အတိတ် (3, pi-1) |
| atītārammaṇo | အတိတ်ကို အာရုံပြုသော (9) |
| atītārammaṇā | အတိတ်ကို အာရုံပြုသော (1, pi-1) |
| avaññātaṃ | လျစ်လျူရှုထားသော (1) |
| avicāro | ဆက်လက်သုံးသပ်မှု မရှိသော (1) |
| avitakkavicāramatto | စတင်ကြံစည်မှု မရှိဘဲ ဆက်လက်သုံးသပ်မှုသာ ရှိသော (5) |
| avitakko | စတင်ကြံစည်မှု မရှိသော (3) |
| ayoganiyo | ထမ်းပိုး၏ အာရုံ မဖြစ်နိုင်သော (5) |
| Aṭṭhavidhena | ရှစ်မျိုး (5) |
| bahiddho | မိမိ၏ ပြင်ပ၌ ရှိသော (9) |
| bahiddhā | မိမိ၏ ပြင်ပ၌ (1) |
| bahiddhārammaṇo | မိမိ၏ ပြင်ပ၌ ရှိသည်ကို အာရုံပြုသော (20) |
| bahiddhārammaṇā | မိမိ၏ ပြင်ပ၌ ရှိသည်ကို အာရုံပြုသော (1) |
| Bahuvidhena | အမျိုးမျိုး (4) |
| bhagavato | မြတ်စွာဘုရား (1, pi-1) |
| bhājanīyaṃ | ခွဲခြမ်း ဖော်ပြချက် (4, pi-1) |
| bhāvanāya | ဘာဝနာ ပွားများခြင်း (16) |
| bhūtā | မူလဓာတ် (2, pi-1) |
| bāhiraṃ | ပြင်ပ (1, pi-1) |
| bāhirā | ပြင်ပ (1, pi-1) |
| cakkhundriyaṃ | မျက်စိ၏ စွမ်းရည် (1) |
| cakkhusamphassa | မျက်စိ၏ တွေ့ထိမှု (11) |
| cakkhusamphassajā | မျက်စိ၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော (10, pi-1) |
| cakkhusamphassajā cetanā | မျက်စိ၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော စေ့ဆော်မှု (4) |
| cakkhusamphassajā saññā | မျက်စိ၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော မှတ်သိမှု (4) |
| cakkhusamphassajā vedanā | မျက်စိ၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော ခံစားမှု (2, pi-1) |
| cakkhuviññeyyaṃ | မျက်စိဖြင့် သိနိုင်သော (1) |
| cakkhuviññāṇaṃ | မျက်စိ သိစိတ် (4, pi-1) |
| Cakkhāyatanaṃ | မျက်စိ အာရုံခံ နယ်ပယ် (2, pi-1) |
| cakkhāyatanaṃ | မျက်စိ အာရုံခံ နယ်ပယ် (1, pi-1) |
| Catubbidhena | လေးမျိုး (5, pi-1) |
| Catuvīsatividhena | နှစ်ဆယ့်လေးမျိုး (4) |
| cetanā | စေ့ဆော်မှု (4, pi-1) |
| cetasikā | စိတ်၏ အဖော် (1, pi-1) |
| Chabbidhena | ခြောက်မျိုး (5, pi-1) |
| citta | စိတ် (30, pi-1) |
| cittasampayutto | စိတ်နှင့် ယှဉ်တွဲသော (29) |
| cittasampayuttā | စိတ်နှင့် ယှဉ်တွဲသော (1) |
| cittasaṃsaṭṭhā | စိတ်နှင့် ရောနှောသော (1, pi-1) |
| cittaṃ | စိတ် (1, pi-1) |
| cittīkataṃ | အလေးထားသော (1) |
| Dasavidhena | ဆယ်မျိုး (5) |
| dasavidhena | ဆယ်မျိုး (112) |
| dasavidhena saññākkhandho | ဆယ်မျိုး … မှတ်သိမှု အစုအဝေး (29) |
| dasavidhena saṅkhārakkhandho | ဆယ်မျိုး … ပြုပြင်ဖန်တီးမှု အစုအဝေး (28) |
| dasavidhena vedanākkhandho | ဆယ်မျိုး … ခံစားမှု အစုအဝေး (27) |
| dasavidhena viññāṇakkhandho | ဆယ်မျိုး … သိစိတ် အစုအဝေး (28) |
| dassanena | သစ္စာကို မြင်ခြင်း (20, pi-1) |
| daṭṭhabbaṃ | မှတ်ယူရမည့် (5) |
| daṭṭhabbā | မှတ်ယူရမည့် (9) |
| dhammāyatana | သဘောတရား အာရုံခံ နယ်ပယ် (1, pi-1) |
| dhātu | ဓာတ် (5, pi-1) |
| domanassindriya | စိတ်ဆင်းရဲမှု၏ စွမ်းရည် (3) |
| domanassindriyaṃ | စိတ်ဆင်းရဲမှု၏ စွမ်းရည် (1) |
| Duka | နှစ်မျိုးတွဲ (4, pi-1) |
| Dukaṃ | နှစ်မျိုးတွဲ (1, pi-1) |
| dukkha | နာကျင်သော (1, pi-1) |
| dukkhindriya | နာကျင်မှု၏ စွမ်းရည် (3) |
| dukkhindriyaṃ | နာကျင်မှု၏ စွမ်းရည် (1, pi-1) |
| Dukkhā | နာကျင်သော (3) |
| dukkhā | နာကျင်သော (3) |
| Dukkhā vedanā | နာကျင်သော ခံစားမှု (3, pi-1) |
| dukkhā vedanā | နာကျင်သော ခံစားမှု (2, pi-1) |
| dukkhāhi vedanāhi | နာကျင်သော ခံစားမှု (10) |
| Dukkhāya | နာကျင်သော (9, pi-1) |
| dukkhāya | နာကျင်သော (14, pi-1) |
| Dukkhāya vedanāya | နာကျင်သော ခံစားမှု (9, pi-1) |
| dukkhāya vedanāya | နာကျင်သော ခံစားမှု (14, pi-1) |
| Dukkhāya vedanāya sampayuttaṃ | နာကျင်သော ခံစားမှုနှင့် ယှဉ်တွဲသော (3) |
| dukkhāya vedanāya sampayutto | နာကျင်သော ခံစားမှုနှင့် ယှဉ်တွဲသော (13) |
| Dukkhāya vedanāya sampayuttā | နာကျင်သော ခံစားမှုနှင့် ယှဉ်တွဲသော (6) |
| dukkhāya vedanāya sampayuttā | နာကျင်သော ခံစားမှုနှင့် ယှဉ်တွဲသော (1) |
| Duvidhena | နှစ်မျိုး (117) |
| Ekavidhena | တစ်မျိုး (117) |
| Ekādasavidhena | ဆယ့်တစ်မျိုး (1) |
| gandhā | အနံ့ (1) |
| gandhāyatanaṃ | အနံ့ အာရုံခံ နယ်ပယ် (1, pi-1) |
| gantha | အထုံး (10, pi-1) |
| ganthaniyaṃ | အထုံး၏ အာရုံ ဖြစ်နိုင်သော (1, pi-1) |
| ganthaniyo | အထုံး၏ အာရုံ ဖြစ်နိုင်သော (11) |
| ganthasampayutto | အထုံးနှင့် ယှဉ်တွဲသော (3) |
| ganthavippayuttaganthaniyo | အထုံးနှင့် ကင်းကွာသော … အထုံး၏ အာရုံ ဖြစ်နိုင်သော (3) |
| ganthavippayutto | အထုံးနှင့် ကင်းကွာသော (3) |
| gantho | အထုံး (2, pi-1) |
| gantho ceva ganthasampayutto | အထုံးလည်း ဖြစ် အထုံးနှင့်လည်း ယှဉ်တွဲသော (1) |
| ganthā | အထုံး (1, pi-1) |
| ganthā ceva ganthasampayuttā | အထုံးလည်း ဖြစ် အထုံးနှင့်လည်း ယှဉ်တွဲသော (1) |
| ghānasamphassa | နှာခေါင်း၏ တွေ့ထိမှု (11) |
| ghānasamphassajā | နှာခေါင်း၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော (10, pi-1) |
| ghānaviññeyyaṃ | နှာခေါင်းဖြင့် သိနိုင်သော (1) |
| ghānaviññāṇaṃ | နှာခေါင်း သိစိတ် (4, pi-1) |
| ghānindriyaṃ | နှာခေါင်း၏ စွမ်းရည် (1) |
| ghānāyatanaṃ | နှာခေါင်း အာရုံခံ နယ်ပယ် (1, pi-1) |
| gāmī | ဦးတည်သော (2) |
| hetu | အမြစ် (27, pi-1) |
| hetu ceva hetusampayutto | အမြစ်လည်း ဖြစ် အမြစ်နှင့်လည်း ယှဉ်တွဲသော (1) |
| hetukaṃ | အမြစ် (1, pi-1) |
| hetuko | အမြစ် (27) |
| hetukā | အမြစ် (1, pi-1) |
| hetusampayutto | အမြစ်နှင့် ယှဉ်တွဲသော (15) |
| hetusampayuttā | အမြစ်နှင့် ယှဉ်တွဲသော (1) |
| hetuvippayutto | အမြစ်နှင့် ကင်းကွာသော (11) |
| hetū | အမြစ် (1, pi-1) |
| hetū ceva hetusampayuttā | အမြစ်လည်း ဖြစ် အမြစ်နှင့်လည်း ယှဉ်တွဲသော (1) |
| hīnamataṃ | ယုတ်ညံ့သည်ဟု ယူဆထားသော (1) |
| hīnaṃ | ယုတ်ညံ့သော (4, pi-1) |
| hīno | ယုတ်ညံ့သော (9) |
| hīnā | ယုတ်ညံ့သော (7, pi-1) |
| hīḷitaṃ | ကဲ့ရဲ့ထားသော (1) |
| indriya | စွမ်းရည် (3, pi-1) |
| indriyaṃ | စွမ်းရည် (4, pi-1) |
| Itthindriyaṃ | မိန်းမ၏ စွမ်းရည် (2, pi-1) |
| itthindriyaṃ | မိန်းမ၏ စွမ်းရည် (1, pi-1) |
| iṭṭhaṃ | လိုလားဖွယ်ကောင်းသော (1) |
| jarābhibhūtaṃ | အိုခြင်း လွှမ်းမိုးခံရသော (1) |
| jivhindriyaṃ | လျှာ၏ စွမ်းရည် (1) |
| jivhāsamphassa | လျှာ၏ တွေ့ထိမှု (11) |
| jivhāsamphassajā | လျှာ၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော (10, pi-1) |
| jivhāviññeyyaṃ | လျှာဖြင့် သိနိုင်သော (1) |
| jivhāviññāṇaṃ | လျှာ သိစိတ် (4, pi-1) |
| jivhāyatanaṃ | လျှာ အာရုံခံ နယ်ပယ် (1, pi-1) |
| jātaṃ | မွေးဖွားပြီးသော (2) |
| jātā | မွေးဖွားပြီးသော (1, pi-1) |
| jīvitindriyaṃ | အသက်၏ စွမ်းရည် (1, pi-1) |
| kabaḷīkāro | လုတ်ပြု၍ စားရသော (3, pi-1) |
| kantaṃ | ချစ်ခင်ဖွယ်ကောင်းသော (1) |
| kaṇḍe | အခန်း (1, pi-1) |
| kenaci | တစ်စုံတစ်ခုသော စိတ် (11) |
| kenaci na viññeyyo | တစ်စုံတစ်ခုသော စိတ်ဖြင့် မသိနိုင်သော (6) |
| kenaci viññeyyo | တစ်စုံတစ်ခုသော စိတ်ဖြင့် သိနိုင်သော (6) |
| Khandha | အစုအဝေး (1, pi-1) |
| khandho | အစုအဝေး (137, pi-1) |
| khandhā | အစုအဝေး (5, pi-1) |
| khandhā cittasaṃsaṭṭhā | အစုအဝေး … စိတ်နှင့် ရောနှောသော (1) |
| khandhā siyā | အစုအဝေး … တစ်ခါတစ်ရံ (2) |
| khandhānaṃ | အစုအဝေး (1) |
| kilesa | ကိလေသာ (4, pi-1) |
| kilesasampayutto | ကိလေသာနှင့် ယှဉ်တွဲသော (1) |
| kilesavippayutto | ကိလေသာနှင့် ကင်းကွာသော (1) |
| kileso ceva kilesasampayutto | ကိလေသာလည်း ဖြစ် ကိလေသာနှင့်လည်း ယှဉ်တွဲသော (1) |
| kilesā | ကိလေသာ (1, pi-1) |
| kilesā ceva kilesasampayuttā | ကိလေသာလည်း ဖြစ် ကိလေသာနှင့်လည်း ယှဉ်တွဲသော (1) |
| kusala | ကုသိုလ် (1, pi-1) |
| kusalaṃ | ကုသိုလ် (1, pi-1) |
| kusalaṃ viññāṇaṃ | ကုသိုလ် သိစိတ် (1) |
| kusalo | ကုသိုလ် (25) |
| kusalā | ကုသိုလ် (5, pi-1) |
| kusalā saññā | ကုသိုလ် မှတ်သိမှု (1) |
| kusalā saṅkhārā | ကုသိုလ် ပြုပြင်ဖန်တီးမှု (1) |
| kusalā vedanā | ကုသိုလ် ခံစားမှု (1) |
| kusalābyākatā | ကုသိုလ် … ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော (12) |
| Kusalākusalā | ကုသိုလ် … အကုသိုလ် (8) |
| kusalākusalā | ကုသိုလ် … အကုသိုလ် (4) |
| kāmāvacaraṃ | ကာမဘုံနှင့် ဆိုင်သော (1, pi-1) |
| kāmāvacaro | ကာမဘုံနှင့် ဆိုင်သော (13) |
| kāyasamphassa | ကိုယ်၏ တွေ့ထိမှု (11, pi-1) |
| kāyasamphassajā | ကိုယ်၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော (10, pi-1) |
| kāyaviññeyyaṃ | ကိုယ်ဖြင့် သိနိုင်သော (1) |
| kāyaviññāṇaṃ | ကိုယ် သိစိတ် (4, pi-1) |
| kāyindriyaṃ | ကိုယ်၏ စွမ်းရည် (1) |
| kāyāyatanaṃ | ကိုယ် အာရုံခံ နယ်ပယ် (1, pi-1) |
| lokiyaṃ | လောကနှင့် သက်ဆိုင်သော (1, pi-1) |
| lokiyo | လောကနှင့် သက်ဆိုင်သော (11) |
| magga | မဂ် (10, pi-1) |
| mahaggato | ကြီးမြတ်သော (9) |
| mahaggatā | ကြီးမြတ်သော (1, pi-1) |
| mahaggatārammaṇo | ကြီးမြတ်သည်ကို အာရုံပြုသော (9) |
| mahaggatārammaṇā | ကြီးမြတ်သည်ကို အာရုံပြုသော (1, pi-1) |
| mahābhūtā | မူလဓာတ်ကြီး (2, pi-1) |
| majjhimo | အလယ်အလတ် (10) |
| mano | မနော (3, pi-1) |
| manodhātu | မနော ဓာတ် (5, pi-1) |
| manosamphassa | မနော၏ တွေ့ထိမှု (11) |
| manosamphassajā | မနော၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော (10) |
| manoviññāṇa | မနော သိစိတ် (4, pi-1) |
| manoviññāṇadhātu | မနော သိစိတ် ဓာတ် (5, pi-1) |
| manoviññāṇaṃ | မနော သိစိတ် (4) |
| manāpaṃ | စိတ်နှင့် တွေ့သော (1) |
| mattaṃ | သာ (1) |
| micchatta | မှားယွင်းမှု (10, pi-1) |
| micchattaniyato | မှားယွင်းမှု၌ ကျိန်းသေသော (9) |
| mutaṃ | နမ်း မြည်း ထိတွေ့ရသော (1, pi-1) |
| mūlakaṃ | အခြေခံသော (8) |
| na | မ (2, pi-1) |
| na kāmāvacaro | ကာမဘုံနှင့် ဆိုင်သည် မဟုတ်သော (4) |
| na pītisahagato | ပီတိနှင့်အတူ ဖြစ်သည် မဟုတ်သော (3) |
| Namo | ရှိခိုးသည် (1, pi-1) |
| Navavidhena | ကိုးမျိုး (5) |
| nibbattaṃ | ပေါ်ထွက်ပြီးသော (2) |
| nibbattā | ပေါ်ထွက်ပြီးသော (3, pi-1) |
| niruddhaṃ | ချုပ်ငြိမ်းပြီးသော (2) |
| niruddhā | ချုပ်ငြိမ်းပြီးသော (3, pi-1) |
| niyato | ကျိန်းသေသော (13) |
| niyatā | ကျိန်းသေသော (2, pi-1) |
| niyyāniko | လွတ်မြောက်ရာသို့ ပို့ဆောင်သော (3) |
| niṭṭhito | ပြီးဆုံးသော (1, pi-1) |
| nīvaraṇa | အတားအဆီး (1, pi-1) |
| nīvaraṇañceva nīvaraṇasampayutto | အတားအဆီးလည်း ဖြစ် အတားအဆီးနှင့်လည်း ယှဉ်တွဲသော (1) |
| nīvaraṇaṃ | အတားအဆီး (1, pi-1) |
| nīvaraṇiyaṃ | အတားအဆီး၏ အာရုံ ဖြစ်နိုင်သော (1, pi-1) |
| nīvaraṇiyo | အတားအဆီး၏ အာရုံ ဖြစ်နိုင်သော (7) |
| nīvaraṇā | အတားအဆီး (1, pi-1) |
| nīvaraṇā ceva nīvaraṇasampayuttā | အတားအဆီးလည်း ဖြစ် အတားအဆီးနှင့်လည်း ယှဉ်တွဲသော (1) |
| ogha | ရေအလျဉ် (7, pi-1) |
| oghaniyaṃ | ရေအလျဉ်၏ အာရုံ ဖြစ်နိုင်သော (1, pi-1) |
| oghaniyo | ရေအလျဉ်၏ အာရုံ ဖြစ်နိုင်သော (10) |
| oghasampayutto | ရေအလျဉ်နှင့် ယှဉ်တွဲသော (3) |
| oghavippayuttaoghaniyo | ရေအလျဉ်နှင့် ကင်းကွာသော … ရေအလျဉ်၏ အာရုံ ဖြစ်နိုင်သော (3) |
| oghavippayutto | ရေအလျဉ်နှင့် ကင်းကွာသော (3) |
| oghā | ရေအလျဉ် (1, pi-1) |
| oḷārikaṃ | ရုန့်ရင်းသော (5, pi-1) |
| oḷārikā | ရုန့်ရင်းသော (6) |
| paccattaṃ | ကိုယ်စီ ဖြစ်သော (5, pi-1) |
| paccayā | အကြောင်းပြု၍ (4) |
| paccuppannaṃ | ပစ္စုပ္ပန် (2) |
| paccuppanno | ပစ္စုပ္ပန် (9) |
| paccuppannā | ပစ္စုပ္ပန် (3, pi-1) |
| paccuppannārammaṇo | ပစ္စုပ္ပန်ကို အာရုံပြုသော (9) |
| paccuppannārammaṇā | ပစ္စုပ္ပန်ကို အာရုံပြုသော (1, pi-1) |
| pahātabba | ပယ်ရမည့် (4, pi-1) |
| pahātabbahetuko | ပယ်ရမည့် အမြစ် ရှိသော (13) |
| pahātabbaṃ | ပယ်ရမည့် (1, pi-1) |
| pahātabbo | ပယ်ရမည့် (15) |
| parapuggalānaṃ | အခြား ပုဂ္ဂိုလ် (5) |
| paribhūtaṃ | စော်ကားထားသော (1) |
| parittaṃ | အကန့်အသတ် ရှိသော (1, pi-1) |
| paritto | အကန့်အသတ် ရှိသော (10) |
| parittārammaṇo | အကန့်အသတ် ရှိသည်ကို အာရုံပြုသော (9) |
| parittārammaṇā | အကန့်အသတ် ရှိသည်ကို အာရုံပြုသော (1, pi-1) |
| pariyāpanno | ဘဝဘုံတို့၌ အကျုံးဝင်သော (3) |
| parāmaṭṭhaṃ | မှားယွင်းသော ယူဆမှု၏ အာရုံ ဖြစ်နိုင်သော (1, pi-1) |
| parāmaṭṭho | မှားယွင်းသော ယူဆမှု၏ အာရုံ ဖြစ်နိုင်သော (5) |
| parāmāsa | မှားယွင်းသော ယူဆမှု (4, pi-1) |
| parāmāsavippayutto | မှားယွင်းသော ယူဆမှုနှင့် ကင်းကွာသော (5) |
| parāmāso | မှားယွင်းသော ယူဆမှု (1, pi-1) |
| parāmāsā | မှားယွင်းသော ယူဆမှု (1, pi-1) |
| pathavī | မြေ (1, pi-1) |
| pathavīdhātu | မြေဓာတ် (1, pi-1) |
| Pañcavidhena | ငါးမျိုး (5) |
| Pañhā | မေးခွန်း (2) |
| Pañhāpucchakaṃ | မေးခွန်းများဖြင့် ဖော်ပြချက် (2) |
| paṇītaṃ | မွန်မြတ်သော (4, pi-1) |
| paṇīto | မွန်မြတ်သော (9) |
| paṇītā | မွန်မြတ်သော (7, pi-1) |
| Paṭighasamphassa | ထိခိုက်မှု၏ တွေ့ထိမှု (1) |
| Paṭighasamphassajā | ထိခိုက်မှု၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော (1) |
| Paṭighasamphassajā saññā | ထိခိုက်မှု၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော မှတ်သိမှု (1) |
| phassa | တွေ့ထိမှု (87, pi-1) |
| phassasampayutto | တွေ့ထိမှုနှင့် ယှဉ်တွဲသော (87) |
| phoṭṭhabbā | အထိအတွေ့ (1) |
| phoṭṭhabbāyatanaṃ | အထိအတွေ့ အာရုံခံ နယ်ပယ် (3, pi-1) |
| purisindriyaṃ | ယောက်ျား၏ စွမ်းရည် (1, pi-1) |
| pātubhūtaṃ | ထင်ရှားလာပြီးသော (2) |
| pātubhūtā | ထင်ရှားလာပြီးသော (3, pi-1) |
| pāḷi | (no direct equivalent) (1) |
| pāṭipuggalikaṃ | ပုဂ္ဂိုလ်တစ်ဦးချင်းစီ၏ ဖြစ်သော (2) |
| pāṭipuggalikā | ပုဂ္ဂိုလ်တစ်ဦးချင်းစီ၏ ဖြစ်သော (3, pi-1) |
| pīti | ပီတိ (13, pi-1) |
| pītisahagataṃ | ပီတိနှင့်အတူ ဖြစ်သော (1, pi-1) |
| pītisahagato | ပီတိနှင့်အတူ ဖြစ်သော (12) |
| rasā | အရသာ (1) |
| rasāyatanaṃ | အရသာ အာရုံခံ နယ်ပယ် (1, pi-1) |
| Rūpa | ရုပ် (4, pi-1) |
| rūpa | ရုပ် (3, pi-1) |
| Rūpakkhandho | ရုပ် အစုအဝေး (4, pi-1) |
| rūpakkhandho | ရုပ် အစုအဝေး (5, pi-1) |
| Rūpakkhandho hetuvippayutto | ရုပ် အစုအဝေး … အမြစ်နှင့် ကင်းကွာသော (1) |
| rūpaṃ | ရုပ် (7, pi-1) |
| rūpaṃ anāgataṃ | အနာဂတ် ရုပ် (1) |
| rūpaṃ atītaṃ | အတိတ် ရုပ် (1) |
| rūpaṃ cittasamuṭṭhānaṃ | စိတ်မှ ဖြစ်ပေါ်လာသော ရုပ် (1, pi-1) |
| rūpaṃ hīnaṃ | ယုတ်ညံ့သော ရုပ် (1) |
| rūpaṃ oḷārikaṃ | ရုန့်ရင်းသော ရုပ် (1) |
| rūpaṃ paccuppannaṃ | ပစ္စုပ္ပန် ရုပ် (1) |
| rūpaṃ paṇītaṃ | မွန်မြတ်သော ရုပ် (1) |
| rūpaṃ sukhumaṃ | နုညံ့သော ရုပ် (1) |
| rūpaṃ upādā | မူလဓာတ်ကြီးများကို မှီ၍ ဖြစ်သော ရုပ် (1) |
| rūpā | အဆင်းအရောင် (1) |
| rūpāvacaraṃ | သိမ်မွေ့သော ရုပ်ဘုံနှင့် ဆိုင်သော (1, pi-1) |
| rūpāvacaro | သိမ်မွေ့သော ရုပ်ဘုံနှင့် ဆိုင်သော (13) |
| rūpāyatanaṃ | အဆင်းအရောင် အာရုံခံ နယ်ပယ် (1, pi-1) |
| saddā | အသံ (1) |
| saddāyatanaṃ | အသံ အာရုံခံ နယ်ပယ် (1, pi-1) |
| saha | အတူ (2) |
| sahabhu | အတူ တည်ရှိသော (1) |
| sahabhuno | အတူ တည်ရှိသော (1, pi-1) |
| sahagataṃ | အတူ ဖြစ်သော (2, pi-1) |
| sahagato | အတူ ဖြစ်သော (12, pi-1) |
| sahagatā | အတူ ဖြစ်သော (2, pi-1) |
| sahetuko | အမြစ် ရှိသော (1) |
| sambuddhassa | အမှန်ကို ကိုယ်တိုင် … သိမြင်တော်မူသော ဘုရားရှင် (1, pi-1) |
| sammatta | မှန်ကန်မှု (10, pi-1) |
| sammā | အပြည့်အဝ (1, pi-1) |
| sammāsambuddhassa | အမှန်ကို ကိုယ်တိုင် အပြည့်အဝ သိမြင်တော်မူသော ဘုရားရှင် (1, pi-1) |
| sampayuttaṃ | ယှဉ်တွဲသော (3, pi-1) |
| sampayuttaṃ viññāṇaṃ | ယှဉ်တွဲသော သိစိတ် (3) |
| sampayutto | ယှဉ်တွဲသော (116, pi-1) |
| sampayuttā | ယှဉ်တွဲသော (10, pi-1) |
| sampayuttā saññā | ယှဉ်တွဲသော မှတ်သိမှု (3) |
| sampayuttā saṅkhārā | ယှဉ်တွဲသော ပြုပြင်ဖန်တီးမှု (3) |
| sampayuttāhi saññāhi | ယှဉ်တွဲသော မှတ်သိမှု (1) |
| samphassa | တွေ့ထိမှု (1, pi-1) |
| samphassajā | တွေ့ထိမှုမှ ဖြစ်ပေါ်သော (3, pi-1) |
| samphassaṃ | ထိတွေ့ရ (1, pi-1) |
| samuṭṭhitaṃ | ကောင်းစွာ ထပေါ်ပြီးသော (2) |
| samuṭṭhitā | ကောင်းစွာ ထပေါ်ပြီးသော (3, pi-1) |
| samuṭṭhānaṃ | ဖြစ်ပေါ်လာသော (1, pi-1) |
| samuṭṭhānā | ဖြစ်ပေါ်လာသော (1, pi-1) |
| samāpannassa | ဈာန် ဝင်စားသော (12, pi-1) |
| sanidassana | မြင်နိုင်သော (1, pi-1) |
| sanidassanaṃ | မြင်နိုင်သော (1, pi-1) |
| sanidassano | မြင်နိုင်သော (1) |
| sappaccayaṃ | အကြောင်း ရှိသော (1) |
| sappaṭighaṃ | ထိခိုက်မှု ရှိသော (1, pi-1) |
| sappaṭigho | ထိခိုက်မှု ရှိသော (2, pi-1) |
| saraṇo | ပဋိပက္ခ ရှိသော (16) |
| saraṇā | ပဋိပက္ခ ရှိသော (2) |
| Sattavidhena | ခုနစ်မျိုး (9) |
| sauttaro | ထိုထက် သာလွန်သည် ရှိသေးသော (5) |
| sauttarā | ထိုထက် သာလွန်သည် ရှိသေးသော (1, pi-1) |
| savicāro | ဆက်လက်သုံးသပ်မှု ရှိသော (8) |
| savitakkasavicāraṃ | စတင်ကြံစည်မှုနှင့် ဆက်လက်သုံးသပ်မှု ရှိသော (1) |
| savitakkasavicāro | စတင်ကြံစည်မှုနှင့် ဆက်လက်သုံးသပ်မှု ရှိသော (9, pi-1) |
| savitakkasavicārā | စတင်ကြံစည်မှုနှင့် ဆက်လက်သုံးသပ်မှု ရှိသော (1) |
| Saññā | မှတ်သိမှု (2, pi-1) |
| saññā | မှတ်သိမှု (39, pi-1) |
| saññā anāgatā | အနာဂတ် မှတ်သိမှု (1) |
| saññā atītā | အတိတ် မှတ်သိမှု (1) |
| saññā paccuppannā | ပစ္စုပ္ပန် မှတ်သိမှု (1) |
| saññāhi | မှတ်သိမှု (1) |
| Saññākkhandho | မှတ်သိမှု အစုအဝေး (2, pi-1) |
| saññākkhandho | မှတ်သိမှု အစုအဝေး (34, pi-1) |
| saṃkilesikaṃ | ကိလေသာ၏ အာရုံ ဖြစ်နိုင်သော (1, pi-1) |
| saṃkilesiko | ကိလေသာ၏ အာရုံ ဖြစ်နိုင်သော (15) |
| saṃkiliṭṭha | ကိလေသာဖြင့် ညစ်နွမ်းသော (10, pi-1) |
| saṃkiliṭṭho | ကိလေသာဖြင့် ညစ်နွမ်းသော (4) |
| saṃkiliṭṭhā | ကိလေသာဖြင့် ညစ်နွမ်းသော (1, pi-1) |
| saṃsaṭṭhā | ရောနှောသော (1, pi-1) |
| saṃyojana | နှောင်ကြိုး (11, pi-1) |
| saṃyojanasampayutto | နှောင်ကြိုးနှင့် ယှဉ်တွဲသော (7) |
| saṃyojanavippayuttasaṃyojaniyo | နှောင်ကြိုးနှင့် ကင်းကွာသော … နှောင်ကြိုး၏ အာရုံ ဖြစ်နိုင်သော (4) |
| saṃyojanavippayutto | နှောင်ကြိုးနှင့် ကင်းကွာသော (6) |
| saṃyojanañceva saṃyojanasampayutto | နှောင်ကြိုးလည်း ဖြစ် နှောင်ကြိုးနှင့်လည်း ယှဉ်တွဲသော (1) |
| saṃyojanaṃ | နှောင်ကြိုး (4, pi-1) |
| saṃyojaniyaṃ | နှောင်ကြိုး၏ အာရုံ ဖြစ်နိုင်သော (1, pi-1) |
| saṃyojaniyo | နှောင်ကြိုး၏ အာရုံ ဖြစ်နိုင်သော (15) |
| saṃyojaniyā | နှောင်ကြိုး၏ အာရုံ ဖြစ်နိုင်သော (1, pi-1) |
| saṃyojanā | နှောင်ကြိုး (1, pi-1) |
| saṃyojanā ceva saṃyojanasampayuttā | နှောင်ကြိုးလည်း ဖြစ် နှောင်ကြိုးနှင့်လည်း ယှဉ်တွဲသော (1) |
| saṅgahitaṃ | အကျုံးဝင်သော (2) |
| saṅgahitā | အကျုံးဝင်သော (3) |
| saṅkhataṃ | ပြုပြင်ဖန်တီးထားသော (1, pi-1) |
| saṅkhatā | ပြုပြင်ဖန်တီးထားသော (1, pi-1) |
| Saṅkhāra | ပြုပြင်ဖန်တီးမှု (4, pi-1) |
| saṅkhāra | ပြုပြင်ဖန်တီးမှု (32, pi-1) |
| Saṅkhārakkhandho | ပြုပြင်ဖန်တီးမှု အစုအဝေး (4, pi-1) |
| saṅkhārakkhandho | ပြုပြင်ဖန်တီးမှု အစုအဝေး (33, pi-1) |
| saṅkhārā | ပြုပြင်ဖန်တီးမှု (6, pi-1) |
| saṅkhārā oḷārikā | ရုန့်ရင်းသော ပြုပြင်ဖန်တီးမှု (1) |
| sekkha | ကျင့်ကြံဆဲသူ၏ (1, pi-1) |
| sekkho | ကျင့်ကြံဆဲသူ၏ (9) |
| sekkhā | ကျင့်ကြံဆဲသူ၏ (1, pi-1) |
| somanassindriya | ဝမ်းမြောက်မှု၏ စွမ်းရည် (3) |
| somanassindriyaṃ | ဝမ်းမြောက်မှု၏ စွမ်းရည် (1, pi-1) |
| sotasamphassa | နား၏ တွေ့ထိမှု (11) |
| sotasamphassajā | နား၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော (10, pi-1) |
| sotaviññeyyaṃ | နားဖြင့် သိနိုင်သော (1) |
| sotaviññāṇaṃ | နား သိစိတ် (4, pi-1) |
| sotindriyaṃ | နား၏ စွမ်းရည် (1) |
| sotāyatanaṃ | နား အာရုံခံ နယ်ပယ် (1, pi-1) |
| sukha | သာယာမှု (12, pi-1) |
| Sukhadukkhā | သာယာသော … နာကျင်သော (2) |
| sukhadukkhā | သာယာသော … နာကျင်သော (1) |
| Sukhadukkhāhi | သာယာသော … နာကျင်သော (6) |
| sukhadukkhāhi | သာယာသော … နာကျင်သော (3) |
| sukhasahagataṃ | သာယာမှုနှင့်အတူ ဖြစ်သော (1, pi-1) |
| sukhasahagato | သာယာမှုနှင့်အတူ ဖြစ်သော (10) |
| sukhasahagatā | သာယာမှုနှင့်အတူ ဖြစ်သော (1, pi-1) |
| sukhindriya | သာယာမှု၏ စွမ်းရည် (3) |
| sukhindriyasampayutto | သာယာမှု၏ စွမ်းရည်နှင့် ယှဉ်တွဲသော (3) |
| sukhindriyaṃ | သာယာမှု၏ စွမ်းရည် (1) |
| sukhumaṃ | နုညံ့သော (5, pi-1) |
| sukhumā | နုညံ့သော (6) |
| sukhā | သာယာသော (6, pi-1) |
| sukhā vedanā | သာယာသော ခံစားမှု (3, pi-1) |
| sukhāya | သာယာသော (24, pi-1) |
| sukhāya vedanāya | သာယာသော ခံစားမှု (18, pi-1) |
| sukhāya vedanāya sampayuttaṃ | သာယာသော ခံစားမှုနှင့် ယှဉ်တွဲသော (1) |
| sukhāya vedanāya sampayutto | သာယာသော ခံစားမှုနှင့် ယှဉ်တွဲသော (14) |
| sukhāya vedanāya sampayuttā | သာယာသော ခံစားမှုနှင့် ယှဉ်တွဲသော (3) |
| sutaṃ | ကြားရသော (1, pi-1) |
| Suttanta | သုတ္တန် (2) |
| sārammaṇā | အာရုံ ရှိသော (1) |
| Sāsavaṃ | စိတ်အစွန်းအထင်း၏ အာရုံ ဖြစ်နိုင်သော (3, pi-1) |
| Sāsavaṃ viññāṇaṃ | စိတ်အစွန်းအထင်း၏ အာရုံ ဖြစ်နိုင်သော သိစိတ် (3) |
| sāsavo | စိတ်အစွန်းအထင်း၏ အာရုံ ဖြစ်နိုင်သော (7) |
| Sāsavā | စိတ်အစွန်းအထင်း၏ အာရုံ ဖြစ်နိုင်သော (9, pi-1) |
| Sāsavā saññā | စိတ်အစွန်းအထင်း၏ အာရုံ ဖြစ်နိုင်သော မှတ်သိမှု (3) |
| Sāsavā saṅkhārā | စိတ်အစွန်းအထင်း၏ အာရုံ ဖြစ်နိုင်သော ပြုပြင်ဖန်တီးမှု (3) |
| Sāsavā vedanā | စိတ်အစွန်းအထင်း၏ အာရုံ ဖြစ်နိုင်သော ခံစားမှု (3) |
| tadekajjhaṃ | ထိုအားလုံးကို တစ်စုတည်း (5) |
| Tattha | ထိုတို့အနက် (35, pi-1) |
| tejo | မီး (1, pi-1) |
| tejodhātu | မီးဓာတ် (1, pi-1) |
| Tika | သုံးမျိုးတွဲ (4) |
| Tikaṃ | သုံးမျိုးတွဲ (1) |
| tike | သုံးမျိုးတွဲ (1) |
| tikā | သုံးမျိုးတွဲ (1) |
| Tividhena | သုံးမျိုး (117) |
| Tiṃsatividhena | သုံးဆယ်မျိုး (3) |
| Tiṃsavidhena | သုံးဆယ်မျိုး (1) |
| Ubhato | နှစ်ဘက်စလုံး (4) |
| upakaṭṭhe | အနားကပ်သော (1) |
| upekkhindriya | ဥပေက္ခာ၏ စွမ်းရည် (3) |
| upekkhindriyaṃ | ဥပေက္ခာ၏ စွမ်းရည် (1, pi-1) |
| upekkhā | ဥပေက္ခာ (12, pi-1) |
| upekkhāsahagataṃ | ဥပေက္ခာနှင့်အတူ ဖြစ်သော (1, pi-1) |
| upekkhāsahagato | ဥပေက္ခာနှင့်အတူ ဖြစ်သော (10) |
| upekkhāsahagatā | ဥပေက္ခာနှင့်အတူ ဖြစ်သော (1, pi-1) |
| uppajjitvā | ဖြစ်ပေါ်ပြီး (5, pi-1) |
| uppannaṃ | ဖြစ်ပေါ်ပြီးသော (3, pi-1) |
| uppanno | ဖြစ်ပေါ်ပြီးသော (9) |
| uppannā | ဖြစ်ပေါ်ပြီးသော (4, pi-1) |
| uppādino | ဖြစ်ပေါ်လာမည့် (1, pi-1) |
| uppādī | ဖြစ်ပေါ်လာမည့် (9) |
| upādā | မူလဓာတ်ကြီးများကို မှီ၍ ဖြစ်သော (2, pi-1) |
| upādāna | စွဲလမ်းမှု (4, pi-1) |
| upādānasampayutto | စွဲလမ်းမှုနှင့် ယှဉ်တွဲသော (4) |
| upādānasampayuttā | စွဲလမ်းမှုနှင့် ယှဉ်တွဲသော (1) |
| upādānavippayutto | စွဲလမ်းမှုနှင့် ကင်းကွာသော (5) |
| upādāniyaṃ | စွဲလမ်းမှု၏ အာရုံ ဖြစ်နိုင်သော (1, pi-1) |
| upādāniyo | စွဲလမ်းမှု၏ အာရုံ ဖြစ်နိုင်သော (16) |
| upādānā | စွဲလမ်းမှု (1, pi-1) |
| upādānā ceva upādānasampayuttā | စွဲလမ်းမှုလည်း ဖြစ် စွဲလမ်းမှုနှင့်လည်း ယှဉ်တွဲသော (1) |
| upādāya | မှီ၍ (2, pi-1) |
| upādāyarūpaṃ | မှီ၍ ဖြစ်သော ရုပ် (2) |
| upādāyupādāya | နှိုင်းယှဉ်၍ (14) |
| uttaro | ကျော်လွန်သော (10) |
| uttarā | ကျော်လွန်သော (1, pi-1) |
| uññātaṃ | အထင်သေးထားသော (1) |
| uṭṭhitaṃ | ထပေါ်ပြီးသော (2) |
| uṭṭhitā | ထပေါ်ပြီးသော (3, pi-1) |
| vattabbo | ခေါ်ဆို၍ ရ (2, pi-1) |
| vattabbā | ခေါ်ဆို၍ ရ (2, pi-1) |
| vaḍḍhakaṃ | တိုးပွားသော (4) |
| Vedanā | ခံစားမှု (2, pi-1) |
| vedanā | ခံစားမှု (37, pi-1) |
| vedanā anāgatā | အနာဂတ် ခံစားမှု (1) |
| vedanā atītā | အတိတ် ခံစားမှု (1) |
| vedanā hīnā | ယုတ်ညံ့သော ခံစားမှု (1) |
| vedanā oḷārikā | ရုန့်ရင်းသော ခံစားမှု (1) |
| vedanā paccuppannā | ပစ္စုပ္ပန် ခံစားမှု (1) |
| vedanā paṇītā | မွန်မြတ်သော ခံစားမှု (1) |
| vedanāhi | ခံစားမှု (10) |
| Vedanākkhandho | ခံစားမှု အစုအဝေး (3, pi-1) |
| vedanākkhandho | ခံစားမှု အစုအဝေး (32, pi-1) |
| vedanāya | ခံစားမှု (24, pi-1) |
| vedanāya sampayuttaṃ | ခံစားမှုနှင့် ယှဉ်တွဲသော (3) |
| vedanāya sampayutto | ခံစားမှုနှင့် ယှဉ်တွဲသော (13) |
| vedanāya sampayuttā | ခံစားမှုနှင့် ယှဉ်တွဲသော (7) |
| vibhattaṃ | ခွဲခြားထားသော (1) |
| Vibhaṅga | ခွဲခြမ်းစိတ်ဖြာခြင်း (1) |
| Vibhaṅgapāḷi | ခွဲခြမ်းစိတ်ဖြာခြင်း (1) |
| vibhaṅgo | ခွဲခြမ်းစိတ်ဖြာခြင်း (2) |
| vicāraṃ | ဆက်လက်သုံးသပ်မှု (1, pi-1) |
| vicāro | ဆက်လက်သုံးသပ်မှု (6, pi-1) |
| vidhena | မျိုး (117, pi-1) |
| vigataṃ | ကင်းပျောက်ပြီးသော (2) |
| vigatā | ကင်းပျောက်ပြီးသော (3, pi-1) |
| vipariṇataṃ | ဖောက်ပြန် ပြောင်းလဲပြီးသော (2) |
| vipariṇatā | ဖောက်ပြန် ပြောင်းလဲပြီးသော (3, pi-1) |
| vippayutta | ကင်းကွာသော (16, pi-1) |
| vippayuttaṃ | ကင်းကွာသော (1, pi-1) |
| vippayutto | ကင်းကွာသော (33) |
| vipākadhammadhammaṃ | အကျိုး ပေးတတ်သော (1) |
| vipākadhammadhammo | အကျိုး ပေးတတ်သော (11) |
| vipākadhammadhammā | အကျိုး ပေးတတ်သော သဘောတရား (1, pi-1) |
| vitakka | စတင်ကြံစည်မှု (11, pi-1) |
| vitakko | စတင်ကြံစည်မှု (4, pi-1) |
| vitthāro | အကျယ် (1) |
| viññatti | ထုတ်ဖော်ပြသမှု (1, pi-1) |
| viññeyyaṃ | သိနိုင်သော (1, pi-1) |
| viññeyyaṃ rūpaṃ | သိနိုင်သော ရုပ် (1, pi-1) |
| viññeyyo | သိနိုင်သော (10) |
| viññeyyā | သိနိုင်သော (1, pi-1) |
| viññātaṃ | သိရသော (1, pi-1) |
| Viññāṇa | သိစိတ် (2, pi-1) |
| viññāṇa | သိစိတ် (32, pi-1) |
| viññāṇadhātu | သိစိတ် ဓာတ် (5) |
| Viññāṇakkhandho | သိစိတ် အစုအဝေး (3, pi-1) |
| viññāṇakkhandho | သိစိတ် အစုအဝေး (33, pi-1) |
| viññāṇaṃ | သိစိတ် (6, pi-1) |
| viññāṇaṃ anāgataṃ | အနာဂတ် သိစိတ် (1) |
| viññāṇaṃ atītaṃ | အတိတ် သိစိတ် (1) |
| viññāṇaṃ oḷārikaṃ | ရုန့်ရင်းသော သိစိတ် (1) |
| viññāṇaṃ paccuppannaṃ | ပစ္စုပ္ပန် သိစိတ် (1) |
| viññāṇaṃ sukhumaṃ | နုညံ့သော သိစိတ် (1) |
| viññāṇehi | သိစိတ် (1, pi-1) |
| vuccanti | ခေါ်သည် (1) |
| vuccanti saṅkhārā | ပြုပြင်ဖန်တီးမှုများဟု ခေါ်သည် (1) |
| vuccati | ခေါ်သည် (4) |
| vuccati rūpakkhandho | ရုပ် အစုအဝေးဟု ခေါ်သည် (2) |
| vuccati rūpaṃ | ရုပ်ဟု ခေါ်သည် (1) |
| vuccati saññā | မှတ်သိမှုဟု ခေါ်သည် (1) |
| vuccati saññākkhandho | မှတ်သိမှု အစုအဝေးဟု ခေါ်သည် (2) |
| vuccati saṅkhārakkhandho | ပြုပြင်ဖန်တီးမှု အစုအဝေးဟု ခေါ်သည် (2) |
| vuccati vedanā | ခံစားမှုဟု ခေါ်သည် (1) |
| vuccati vedanā atītā | အတိတ် ခံစားမှုဟု ခေါ်သည် (1) |
| vuccati vedanākkhandho | ခံစားမှု အစုအဝေးဟု ခေါ်သည် (2) |
| vuccati viññāṇakkhandho | သိစိတ် အစုအဝေးဟု ခေါ်သည် (2) |
| vuccati viññāṇaṃ | သိစိတ်ဟု ခေါ်သည် (1) |
| vāyo | လေ (1, pi-1) |
| vāyodhātu | လေဓာတ် (1, pi-1) |
| Yaṃ kiñci | မည်သည့် … မဆို (2) |
| yaṃ vā panaññampi | အခြား … ရှိသမျှလည်း (1) |
| Ye keci | မည်သည့် … မဆို (1) |
| yoga | ထမ်းပိုး (6, pi-1) |
| yoganiyaṃ | ထမ်းပိုး၏ အာရုံ ဖြစ်နိုင်သော (1, pi-1) |
| yoganiyo | ထမ်းပိုး၏ အာရုံ ဖြစ်နိုင်သော (9) |
| yogasampayutto | ထမ်းပိုးနှင့် ယှဉ်တွဲသော (3) |
| yogavippayuttayoganiyo | ထမ်းပိုးနှင့် ကင်းကွာသော … ထမ်းပိုး၏ အာရုံ ဖြစ်နိုင်သော (2) |
| yogavippayutto | ထမ်းပိုးနှင့် ကင်းကွာသော (3) |
| yogā | ထမ်းပိုး (1, pi-1) |
| Yā kāci | မည်သည့် … မဆို (2) |
| ābhibhūtaṃ | လွှမ်းမိုးခံရသော (1) |
| ābyākatāhi saññāhi | ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော မှတ်သိမှု (1) |
| ābyākatāhi vedanāhi | ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော ခံစားမှု (1) |
| ācaya | စုပုံခြင်း (11, pi-1) |
| ācayagāmī | စုပုံခြင်းဆီသို့ ဦးတည်သော (9) |
| ādhipati | အကြီးအမှူး (9) |
| ādhipatino | အကြီးအမှူး (1) |
| āhāro | အာဟာရ (3, pi-1) |
| ānuparivatti | နောက်သို့ လိုက်ပါသော (1) |
| ānuparivattino | နောက်သို့ လိုက်ပါသော (1) |
| āpacaya | လျော့ပါးခြင်း (1) |
| āpo | ရေ (1, pi-1) |
| āpodhātu | ရေဓာတ် (1, pi-1) |
| ārammaṇo | အာရုံ (32, pi-1) |
| āsava | စိတ်အစွန်းအထင်း (15, pi-1) |
| āsavasampayutto | စိတ်အစွန်းအထင်းနှင့် ယှဉ်တွဲသော (6) |
| āsavavippayuttasāsavo | စိတ်အစွန်းအထင်းနှင့် ကင်းကွာသော … စိတ်အစွန်းအထင်း၏ အာရုံ ဖြစ်နိုင်သော (4) |
| āsavavippayutto | စိတ်အစွန်းအထင်းနှင့် ကင်းကွာသော (5) |
| āsavaṃ | စိတ်အစွန်းအထင်း (4, pi-1) |
| āsavo | စိတ်အစွန်းအထင်း (13, pi-1) |
| āsavo ceva āsavasampayutto | စိတ်အစွန်းအထင်းလည်း ဖြစ် စိတ်အစွန်းအထင်းနှင့်လည်း ယှဉ်တွဲသော (1) |
| āsavā | စိတ်အစွန်းအထင်း (10, pi-1) |
| āsavā ceva āsavasampayuttā | စိတ်အစွန်းအထင်းလည်း ဖြစ် စိတ်အစွန်းအထင်းနှင့်လည်း ယှဉ်တွဲသော (1) |
| āsekkhaṃ | ကျင့်ကြံမှု ပြီးဆုံးသူ၏ (1) |
| āvacaraṃ | ဘုံနှင့် ဆိုင်သော (1) |
| āvacaro | ဘုံနှင့် ဆိုင်သော (13) |
| āyatanaṃ | အာရုံခံ နယ်ပယ် (3, pi-1) |
