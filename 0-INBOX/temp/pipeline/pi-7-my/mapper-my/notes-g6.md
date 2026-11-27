# pi-7 Burmese keyword mapping, phase 2, group g6 (part 5: 5-01-anuloma-tikatika … 5-20-paccaniyanuloma-dukaduka)

Script: `map_g6.py`. It imports `map7_rules.py`, which is unchanged (md5 909bed2528b27eb55051c73f3ce28f81). The script
holds one group table (`COMMON`, the same for all 20 chapters; `SPEC` is empty), two per-segment overrides (`CTX`) and
two new context functions (`f_nana`, `f_r1`). Helper scripts are in `work/`: `dev_g6.py`, `q_g6.py`, `kwic_g6.py`,
`pairs_g6.py`, `r1check_g6.py`. No other file was edited.

## Numbers

| chapter | lines | bad | presence failures | «, » / «၊» / « / » | (no direct equivalent) |
|---|---|---|---|---|---|
| 5-01-anuloma-tikatika | 277 | [] | 0 | 0 | 0 |
| 5-02-anuloma-dukaduka | 163 | [] | 0 | 0 | 0 |
| 5-03-paccaniya-tika | 84 | [] | 0 | 0 | 0 |
| 5-04-paccaniya-duka | 188 | [] | 0 | 0 | 0 |
| 5-05-paccaniya-dukatika | 119 | [] | 0 | 0 | 0 |
| 5-06-paccaniya-tikaduka | 114 | [] | 0 | 0 | 0 |
| 5-07-paccaniya-tikatika | 108 | [] | 0 | 0 | 0 |
| 5-08-paccaniya-dukaduka | 82 | [] | 0 | 0 | 0 |
| 5-09-anulomapaccaniya-tika | 144 | [] | 0 | 0 | 0 |
| 5-10-anulomapaccaniya-duka | 114 | [] | 0 | 0 | 1 |
| 5-11-anulomapaccaniya-dukatika | 203 | [] | 0 | 0 | 1 |
| 5-12-anulomapaccaniya-tikaduka | 252 | [] | 0 | 0 | 1 |
| 5-13-anulomapaccaniya-tikatika | 89 | [] | 0 | 0 | 0 |
| 5-14-anulomapaccaniya-dukaduka | 126 | [] | 0 | 0 | 1 |
| 5-15-paccaniyanuloma-tika | 66 | [] | 0 | 0 | 0 |
| 5-16-paccaniyanuloma-duka | 75 | [] | 0 | 0 | 0 |
| 5-17-paccaniyanuloma-dukatika | 199 | [] | 0 | 0 | 0 |
| 5-18-paccaniyanuloma-tikaduka | 154 | [] | 0 | 0 | 1 |
| 5-19-paccaniyanuloma-tikatika | 127 | [] | 0 | 0 | 0 |
| 5-20-paccaniyanuloma-dukaduka | 120 | [] | 0 | 0 | 0 |
| **total** | **2804** | | **0** | **0** | **5** |

- All five (no direct equivalent) values are the particle «ceva» (pi-1 rule 9, a FRAME value).
- Every presence chunk is literal or matched by one of the approved ending rules of the module verifier. There are no
  unexplained presence failures.
- Running the script twice gives byte-identical files (md5 per chapter printed by the script).
- Value sources (uses): term 3046, cond 2595, pi-2 2161, frame 2069, stock 1570, verb 1500, headlex 704, vara 446,
  count 311, pi-5 257, table 151, pi-6 73, order 71, terms 68, pi-3 51, title 34, samutthana 15, pi-1 14, stem 10
  (segment entries; 14 uses), base 8, ctx 2, pi-4 2.
- Against pi-1 … pi-6 (same keyword or its R1 base form): 11091 uses take the prior value unchanged, 14172 uses have a
  keyword that pi-1 … pi-6 never mapped, and 510 uses differ (see the section on differing values).

## Rules used

All as in phase 1 (`map-table.md`), unchanged:

- pi-1 rules 1–11 (rule 1 case and plural particles, rule 3 «…သော / …မည့်», rule 4 «…သည်», rule 6 the «၊», rule 7
  headings whole, rule 9 particles, rule 10 « … » gaps);
- pi-2 N1–N11 and its harmonise decisions;
- pi-3 M1–M9;
- pi-4 P1–P8;
- pi-5 Q1–Q8 and S1;
- pi-6 R1, R6, R7 and the five phase-3 mechanics;
- pi-7 T1–T13, M1, M2 and the coordinator decisions U1–U5 (U3: a pi-1 … pi-6 value is kept where it stands in the
  segment as a phrase, otherwise the text's word is used).

## New rules (with reasons)

- **G6-1, double negation (`f_nana`; T8 applied twice).** na + a no-X or na-X term gives the na-X form of the inner
  term's value in the same segment: «X မဟုတ်သော» → «X မဟုတ်သည် မဟုတ်သော». Examples are nanoāsavo, nanosaññojanaṃ,
  nanoganthañca, nanoupādā and nanaaraṇo «ပဋိပက္ခ မရှိသည် မဟုတ်သည် မဟုတ်သော».
  - Reason: this is the text's own form (harmonise H21, applied to the inner na-X). The module leaves these keywords
    unmapped.
  - The ñca forms go through their base form first. An inner value with a « … » gap is not used (see G6-3).
- **G6-2, R1 enforced for -ñca forms (`f_r1`).** A «-ñca / -ñceva» keyword takes the value its base form gets in the
  same segment.
  - Reason: the module reaches the term family (T7) of the ñca form before the base form's binding pi-2 value. So in
    one segment Āsavaṃ is «စိတ်အစွန်းအထင်း» while Āsavañca is «စိတ်အစွန်းအထင်း ဖြစ်သော», which breaks R1 and the
    one-form-per-segment rule.
  - Applied to āsavañca / Āsavañca and Sekkhañca. `work/r1check_g6.py` now finds no R1 mismatch left in g6.
- **G6-3, no gapped na-X candidate where the plain na-X form stands.** The second candidate of the module's `neg_term`
  is «Nသော … မဟုတ်». It matches by accident in a segment that holds both the positive «N ဖြစ်သော» and some later
  «မဟုတ်», although the text renders the keyword as «N မဟုတ်သော». The plain form is set in the table.
- **G6-4, a prior value that renders another phrase is not taken.** At ^7-63-4, kusale (of «kusale khandhe») is
  «ကုသိုလ်», not the pi-2 «ကုသိုလ် သဘောတရား».
  - Reason: «ကုသိုလ် သဘောတရား» stands in that segment only as the rendering of «Kusalañca … dhammaṃ».
  - This is the same as the phase-1 principle for paripanthe / deti: a prior value present only as another phrase is
    not the keyword's word.
- **G6-5, eva and matta.**
  - X-eva forms take the base form's value without «သာ». This is R1 as the module's `base_forms` («meva», «yeva») has
    it: Ekapañhameva «ပြဿနာ တစ်ခု», Cittasamuṭṭhānarūpameva «စိတ်မှ ဖြစ်ပေါ်လာသော ရုပ်».
  - The compound member -matta is lexical («only»), so it keeps the text's «သာ», and the inner plural stays before
    it: Paccanīyadukamattāni «အငြင်းပြ ပုံစံ နှစ်မျိုးတွဲများသာ».
- **G6-6, notes with a supplied head noun.** The phase-1 rule §A5 (the noun the text adds is not part of the keyword)
  is applied to -sadisa and -mūla notes with a « … » gap:
  - atītasadisaṃ «အတိတ် … နှင့် တူသည်» (text «အတိတ် သဘောတရားနှင့် တူသည်»);
  - sappaccayasadisaṃ «အကြောင်း ရှိသော … နှင့် တူသည်»;
  - Abyākatamūlaṃ / -mūle «ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော … အခြေခံခြင်း».
  - The dyad-name form «Xနှင့် တူသည်» is tried first (a tuple), and is taken where the text has it.

## Module overrides (for the coordinator, phase 3)

| keyword | module value | g6 value | uses | where |
|---|---|---|---|---|
| noupādā / Noupādā | မှီ၍ … မဟုတ်သော | မူလဓာတ်ကြီးများကို မှီ၍ ဖြစ်သည် မဟုတ်သော | 19 | 5-02, 5-04 … (T8 on pi-2 upādā «မူလဓာတ်ကြီးများကို မှီ၍ ဖြစ်သော»; the module's value comes from a bare «မှီ၍») |
| noyogaṃ | ထမ်းပိုး ဖြစ်သော … မဟုတ် | ထမ်းပိုး မဟုတ်သော | 4 | 5-18 ^7-72-25 (G6-3) |
| noāsavañca | စိတ်အစွန်းအထင်း ဖြစ်သော … မဟုတ် | စိတ်အစွန်းအထင်း မဟုတ်သော | 1 | 5-10 ^7-64-16 (G6-3) |
| āsavañca / Āsavañca | စိတ်အစွန်းအထင်း ဖြစ်သော; စိတ်အစွန်းအထင်း … ဖြစ်သော | စိတ်အစွန်းအထင်း | 11 | 5-02 ^7-56-32, 5-10 ^7-64-16 / ^7-64-19 (G6-2) |
| Sekkhañca | ကျင့်ကြံဆဲသူ | ကျင့်ကြံဆဲသူ၏ | 1 | 5-09 ^7-63-39 (G6-2; pi-2 sekkhaṃ) |
| kusale | ကုသိုလ် သဘောတရား | ကုသိုလ် | 1 | 5-09 ^7-63-4 (G6-4, CTX) |

Module gaps that cause unmapped keywords (mapped here in the table):

- `pali_number` does not parse «chabbīsa / chabbīsati» (b for v); g6 gives «နှစ်ဆယ့်ခြောက်ခု».
- T8 does not fire for na + a stem-fallback term (Narūpiṃ) or for double negatives (G6-1).
- The «X-ādidukāni / -ādigocchakāni» heading parts have no heading-lexicon entry where the heading's parts do not
  align.

Suggested module changes:

- drop the gapped `neg_term` candidates when the plain «N မဟုတ်သော» stands in the segment;
- try R1 base forms before the term family;
- add «bīsa» to `pali_number`.

## Values that differ from pi-1 … pi-6 or from the sample

From the g6 tables:

- **Abyākatamūlaṃ (23), Abyākatamūle (2)** «… အခြေခံခြင်း» against the prior «ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း
  မဟုတ်သော အမြစ်». The pi-7 note renders mūla «သဘောတရားကို အခြေခံခြင်း» (T6 mūlaka). The prior «အမြစ်» is not in
  the segment.
- **vattabbaṃ** «ခေါ်ဆို၍ မရသော» (^7-58-56) against pi-1 / pi-2 «ခေါ်ဆို၍ ရ».
  - na is not a keyword in «na vattabbaṃ dhammaṃ», so vattabbaṃ carries the negative.
  - The prior value stands in the segment only by the negative infix, not as a phrase (U3).
- **kusale** «ကုသိုလ်» against pi-2 «ကုသိုလ် သဘောတရား» (G6-4).

From the module in g6 (text-driven: the prior value is not in the segment, or the Paṭṭhāna family wins, T1 / T2 /
T6, as approved in phase 1):

- the counting locatives ārammaṇe, vippayutte, āhāre, magge, indriye, vigate «Nဟူသော အကြောင်း»;
- the answer counts «…ခု» against pi-1 «…ပါး»;
- pañhā «ပြဿနာ» against «မေးခွန်း»;
- sammattaniyato «မှန်ကန်မှု၌ ကျိန်းသေသော»;
- anuttaro «ထိုထက် သာလွန်သည် မရှိသော» against «အတုမရှိသော»;
- arūpī «ရုပ် မဟုတ်သော» against «ရုပ် မရှိသော»;
- bāhiro «ပြင်ပ» against «သာသနာပ»;
- citto «စိတ်»;
- the stacked qualifiers without «သဘောတရား»: nevavipākanavipākadhammadhammo, kiriyābyākataṃ;
- R7 gaps «… » at the «လည်း» of ceva … ca: sāsavo, sahetuko, āsavasampayutto.

There are no differences from the sample chapters for the same keyword.

## S1 (stem fallback) review

All 14 stem-fallback uses were checked by eye against the segment and the keyword's sense. **14 kept, 0 corrected.**

- rūpiṃ / Rūpiṃ «ရုပ် ဖြစ်သော» (11 uses; 5-02, 5-10, 5-11, 5-12, 5-14: the positive «rūpiṃ dhammaṃ» «ရုပ် ဖြစ်သော
  သဘောတရား»);
- Cittasaṃsaṭṭhasamuṭṭhānaṃ / cittasaṃsaṭṭhasamuṭṭhānaṃ «စိတ်နှင့် ရောနှော၍ စိတ်မှ ဖြစ်ပေါ်လာသော» (2; 5-02 ^7-56-87,
  5-10 ^7-64-29);
- gaṇitaṃ «ရေတွက်ထားသော» (1; 5-03 ^7-57-34: «gaṇitaṃ evaṃ gaṇetabbaṃ» «ရေတွက်ထားသည့်အတိုင်း … ရေတွက်ရမည်»; rule 3).

## Keywords newly mapped (unmapped by the module)

There were 121 uses of 46 keywords. All are mapped now:

- Abyākatamūlaṃ (23), Abyākatamūle (2);
- the double negatives: nanoāsavo (7), nanoāsavañca (4), nanoāsavaṃ / Nanoāsavaṃ (2), nanoupādā (4), nanakenaci (4),
  nanosaññojanañca (2), nanosaññojanaṃ, nanoganthañca, nanaaraṇo;
- nevadassanena / Nevadassanena (9);
- the heading parts: saññojanādidukāni / Saññojanādidukāni / Saññojanādiduka (7), saññojanādigocchakāni /
  -gocchakaṃ (5), sahetukādidukāni / Sahetukādidukāni (6), hetvādidukāni, Hetusahetukadukādi;
- the titles: Kusalattikasanidassanattikaṃ (2), Anulomadukatikapaṭṭhānato;
- the -sadisa notes: lokiyadukasadisaṃ / Lokiyadukasadisaṃ (6), Sappaccayadukasadisaṃ / sappaccayadukasadisaṃ (3),
  sappaccayasadisaṃ (3), atītasadisaṃ (2);
- chabbīsa (6), chabbīsati;
- paccayavasena (3), āmasanaṃ (2);
- nocittasaṃsaṭṭhasamuṭṭhānasahabhuṃ / -bhū (3), Narūpiṃ, Narūpiñca;
- vattabbaṃ, Paccanīyadukamattāni, Ekapañhameva, Cittasamuṭṭhānarūpameva, Ete, purimanayena, ovattā.

The values are in `COMMON` and `CTX` of `map_g6.py`, each with its rule.

## Text inconsistencies (for the rails step; the translation is not changed)

1. **«nano ca X»** (5-04 ^7-58-32, ^7-58-37 and others): the Pāli writes the double negative as «nano ca āsavo / nano ca
   saññojano», against «nanoāsavo» elsewhere. The Burmese renders it as «… မဟုတ်သည် မဟုတ်သော». The keyword lists hold
   only the bare āsavo / saññojano / saññojanañca there, and these get the bare noun.
2. **ovattā** (5-18 ^7-72-57, «Nahetu nanahetu ovattā»): a form found only here in the book (elsewhere parivatta-).
   It may be a source slip. The Burmese has «… ပြောင်းပြန် ဖြစ်ကြသည်».
3. **The -sadisa / -mūla notes add the head noun «သဘောတရား»:**
   - sappaccayasadisaṃ (5-10 ^7-64-10, 5-20) «အကြောင်း ရှိသော သဘောတရားနှင့် တူသည်»;
   - atītasadisaṃ (5-13 ^7-67-29);
   - Abyākatamūlaṃ (5-11, 25 uses).

   Against these, Sappaccayadukasadisaṃ (5-02 ^7-56-22) has «အကြောင်း ရှိခြင်း နှစ်မျိုးတွဲနှင့် တူသည်». (This
   extends phase-1 §A4 / §A5.)
4. **Anulomadukatikapaṭṭhānato** (5-20 ^7-74-92) is one Pāli compound. The text splits it into the order and a quoted
   title, «အဟုတ်ပြ ပုံစံ၌ “နှစ်မျိုးတွဲနှင့် သုံးမျိုးတွဲတို့၏ …” မှ», so the value has a gap.
5. **nevadassanena** has two shapes in the text, by the list comma:
   - the first member «သစ္စာကို မြင်ခြင်းဖြင့်လည်း ပယ်ရမည် မဟုတ်၊»;
   - the na-X triad term (nadassanena) «… မဟုတ်သော».
6. **Heading number:** «saññojanādigocchakāni» is «… အစုများ» in most headings, but «… အစု» in 5-14 ^7-5-14-6-0
   (Pāli singular -gocchakaṃ). The value is the same after rule 1.

## Unclear mappings

- **nevadassanena «သစ္စာကို မြင်ခြင်း … မဟုတ်».** The alternative is «သစ္စာကို မြင်ခြင်း … မဟုတ်သော», like the
  module's nabhāvanāya / nadassanena. The keyword also stands in 2-03 / 2-04 (g2), 4-02 / 4-14 / 4-15 (g5) and
  g6, 35 unmapped uses book-wide, so phase 3 should align it.
- **Ete «ဤတို့».** Rule 1 strictly would leave «ဤ», which is the demonstrative adjective. The plural pronoun is kept
  whole.
- **ovattā «ပြောင်းပြန် ဖြစ်သော»** is a participle in dictionary form (rule 3). The text has the verb «ဖြစ်ကြသည်»; the
  alternative is «ပြောင်းပြန် ဖြစ်သည်».
- **purimanayena «ရှေ့နည်း».** The text's «အတိုင်း» is taken as the case of -ena (rule 1), like «ဖြင့်».
- **Paccanīyadukamattāni «အငြင်းပြ ပုံစံ နှစ်မျိုးတွဲများသာ»** (G6-5). The alternative drops «များ», but that gives a
  gapped «… နှစ်မျိုးတွဲ … သာ».
- **The head-noun gaps of G6-6 and nanakenaci «တစ်စုံတစ်ခုသော စိတ် … မဟုတ်သည် မဟုတ်သော».** The alternative is the
  whole phrase with «သဘောတရား» / «ဖြင့် သိနိုင်သည်» in it, but that would take another keyword's word (viññeyyaṃ
  «သိနိုင်သော») or the frame noun.
- **vattabbaṃ «ခေါ်ဆို၍ မရသော»**, with the negative of the non-keyword na.
