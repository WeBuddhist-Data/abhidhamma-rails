# pi-7 Burmese keyword mapping, phase 2, group g5 (part 4: dukatika 4-02 … 4-14, tikaduka 4-15 … 4-21)

Script: `map_g5.py` (imports `map7_rules.py`, md5 909bed2528b27eb55051c73f3ce28f81, not edited). It holds one group
table (`GROUP`, 19 keys), no chapter-only tables, one per-segment override (`CTX`, 2 segments) and no context
function. Burmese comes from the FINAL pi-7 chapter files, the module, and the pi-1 … pi-6 mappings, and nothing else.
Helpers (read-only diagnostics) are in `work/dev_g5.py`, `work/pairs_g5.py`, `work/ctx_g5.py` and `work/diff_g5.py`.

## Numbers (the three checks of the phase-1 brief, per chapter)

| chapter | lines | bad | presence failures | «, » / «၊» / « / » | (no direct equivalent) |
|---|---|---|---|---|---|
| 4-02-dukatika-hetuduka | 1032 | [] | 0 | 0 | 0 |
| 4-03-dukatika-sahetukaduka | 229 | [] | 0 | 0 | 0 |
| 4-04-dukatika-sappaccayaduka | 136 | [] | 0 | 0 | 0 |
| 4-05-dukatika-asavaduka | 117 | [] | 0 | 0 | 4 |
| 4-06-dukatika-sannojanaduka | 90 | [] | 0 | 0 | 2 |
| 4-07-dukatika-ganthaduka | 69 | [] | 0 | 0 | 3 |
| 4-08-dukatika-nivaranaduka | 60 | [] | 0 | 0 | 3 |
| 4-09-dukatika-paramasaduka | 54 | [] | 0 | 0 | 4 |
| 4-10-dukatika-sarammanaduka | 163 | [] | 0 | 0 | 0 |
| 4-11-dukatika-upadanaduka | 54 | [] | 0 | 0 | 3 |
| 4-12-dukatika-kilesaduka | 57 | [] | 0 | 0 | 3 |
| 4-13-dukatika-dassanenapahatabbaduka | 167 | [] | 0 | 0 | 0 |
| 4-14-dukatika-saranaduka | 136 | [] | 0 | 0 | 0 |
| 4-15-tikaduka-hetuduka | 552 | [] | 0 | 0 | 0 |
| 4-16-tikaduka-sappaccayaduka | 91 | [] | 0 | 0 | 0 |
| 4-17-tikaduka-asavaduka | 64 | [] | 0 | 0 | 2 |
| 4-18-tikaduka-sarammanaduka | 60 | [] | 0 | 0 | 0 |
| 4-19-tikaduka-kilesaduka | 60 | [] | 0 | 0 | 2 |
| 4-20-tikaduka-dassanenapahatabbaduka | 101 | [] | 0 | 0 | 0 |
| 4-21-tikaduka-sauttaraduka | 157 | [] | 0 | 0 | 0 |
| **total** | **3449** | [] | **0** | **0** | **26** |

- Keyword uses: 33141, all mapped (0 unmapped).
- All 26 (no direct equivalent) values are the particle ceva (FRAME, pi-1 rule 9).
- Presence: every chunk of every value stands in its segment. 721 chunks match only by an approved ending rule of
  the verifier: attr-fut 472 (vitthāretabbā «ချဲ့ရမည့်» against the text's «ချဲ့ရမည်»), attr 224 (niṭṭhitaṃ
  «ပြီးဆုံးသော» against «ပြီးဆုံးပြီ»), verb 25 (labbhati «တွေ့ရသည်»). There are no other exceptions.
- Reproducibility: two runs give byte-identical `.mapped.md` files (md5 per file in the final report).

## Rules used

These are all binding and unchanged:
- pi-1 rules 1–11 and the later pi-1 rules;
- pi-2 N1–N11 and the harmonise decisions;
- pi-3 M1–M9;
- pi-4 P1–P8;
- pi-5 Q1–Q8, S1–S6 and G1–G5;
- pi-6 R1–R9 and the five phase-3 mechanics;
- the phase-1 module rules T1–T13, M1 and M2;
- the coordinator's U1–U5.

In g5 the module alone maps 33090 of the 33141 uses; 17 of those are overridden here (33073 module values kept), and 51 uses the module leaves unmapped are mapped by the g5 table.

## New rules (g5), with reasons

- **G5-1: the -sadisa notes of the dukatika / tikaduka** (51 uses in 21 keyword forms).
  - **Value.** A note «X-duka(-term)-sadisaṃ» takes the text's whole phrase «<the dyad>(၏ <its term>)နှင့် တူသည်». This is T5 / harmonise H19 extended to a dyad name with a term (Lokiyadukaabyākatasadisaṃ «လောကနှင့် သက်ဆိုင်ခြင်း နှစ်မျိုးတွဲ၏ ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော သဘောတရားနှင့် တူသည်»).
  - **Adverbial.** Before «အကျယ် ချဲ့ရမည်» the text's adverbial «…နှင့် တူအောင်» is used (^7-44-17, ^7-47-104). After yathā, the text's «တူသည့်အတိုင်း» (^7-47-76) is matched by the verb ending rule.
  - **Punctuation.** The «၊» inside the abyākata term goes (rule 6).
  - **Head noun.** The «သဘောတရား» that the text supplies before «နှင့် တူသည်» stays. It stands inside the phrase, so it cannot be dropped without a gap that begins with a particle. A5 drops only a final head noun.
  - **Forms.**
    - lokiya-duka;
    - lokiya-duka with an abyākata or kusala term;
    - lokiyalokuttara-gamana;
    - cittasaṃsaṭṭhasamuṭṭhāna-duka with an abyākata term;
    - citta-duka with a kusala term;
    - upādāna-duka and kilesa-duka with an akusala term;
    - kāmāvacara-duka with an abyākata term;
    - sappītika-duka;
    - sappaccaya-duka.
- **G5-2: nevadassanena** «သစ္စာကို မြင်ခြင်း … မဟုတ်» (7 uses). This is the module's T8 gap value of nadassanena «သစ္စာကို မြင်ခြင်း … မဟုတ်သော» and nabhāvanāya «ဘာဝနာ ပွားများခြင်း … မဟုတ်သော». The clause of neva- ends in the text's «… မဟုတ်၊» (the attributive «သော» belongs to the na- member), so the value has no «သော».
- **G5-3: naviññeyyo** «မသိနိုင်သော» (3 uses). «kenaci naviññeyyo» is the text's «… စိတ်ဖြင့် မသိနိုင်သော». The text's own negative wins over T8's «သိနိုင်သည် မဟုတ်သော», which is not in the segment.
- **G5-4: Imamhi** «ဤ» (2 uses) and **ādimhi** «အစ» (1 use). These are the text's words («ဤ နှစ်မျိုးတွဲနှင့် သုံးမျိုးတွဲ၌», «အစ၌»), the generator values of make_ch4-02-09 / make_ch4-10-14. Rule 1 drops the «၌».
- **G5-5: cetasikadukamūlā** «စိတ်၏ အဖော် ဖြစ်ခြင်း နှစ်မျိုးတွဲကို အခြေခံသော» (1 use, ^7-44-58). The adjective of «tīṇi gamanā» is the text's «… အခြေခံသော သွားပုံ» (rule 3). This differs on purpose from T6's noun mūlakaṃ «… အခြေခံခြင်း».
- **G5-6: saññojanādidukāni** «နှောင်ကြိုး နှစ်မျိုးတွဲ စသည်» (1 use, heading ^7-4-3-3-12-4-0). The heading part «Kusalattika-saññojanādidukāni» is T5 -ādi «… စသည်».

## Module overrides (for the coordinator, phase 3)

| keyword | module value | g5 value | uses | reason |
|---|---|---|---|---|
| Noupādā / noupādā | မှီ၍ … မဟုတ်သော | မူလဓာတ်ကြီးများကို မှီ၍ ဖြစ်သည် မဟုတ်သော | 11 | (1) |
| asekkhassa / asekkhañca | ကျင့်ကြံမှု ပြီးဆုံးသူ | ကျင့်ကြံမှု ပြီးဆုံးသူ၏ | 2 | (2) |
| bhāgo | သဘော | အပိုင်း | 2 | (3) |
| dassane (CTX ^7-47-6, ^7-47-17) | မြင်ခြင်း | သစ္စာကို မြင်ခြင်း | 2 | (4) |

Reasons:

1. **Noupādā.** The module applied T8 to the pi-5 upādā value «မှီ၍», which comes from another kind of segment. T8 on the pi-1 / pi-2 / pi-3 upādā value «မူလဓာတ်ကြီးများကို မှီ၍ ဖြစ်သော» (64 uses) gives the text's own «… ဖြစ်သည် မဟုတ်သော». Suggested module fix: in term_values_any, rank the upādā term value of the dyad above pi-5's.
2. **asekkhassa / asekkhañca.** T7 says a term's value does not depend on its case. In g5, asekkho and asekkhaṃ take the binding pi-1 / pi-2 «…၏» form, the text has «ကျင့်ကြံမှု ပြီးဆုံးသူ၏၊», and so does the module's nevasekkhanāsekkha term. The generator value without «၏» won only for the genitive.
3. **bhāgo.** «Catuttho bhāgo niṭṭhito» is «စတုတ္ထ အပိုင်း ပြီးဆုံးပြီ». The module took the pi-3 bhāga «သဘော» (a case sibling, another sense) because «သဘော» stands inside «သဘောတရား». This follows one sense per segment and uses the text's word.
4. **dassane.** In the elliptic «(dassane ekaṃ, nadassane dve)», dassane takes the binding pi-1 / pi-2 / pi-3 value of the same lemma in the same term, dassanena «သစ္စာကို မြင်ခြင်း» (92 uses). The module also gives that value to dassanena in g5, and nadassane / nadassanena have «သစ္စာကို မြင်ခြင်း … မဟုတ်သော». The module's «မြင်ခြင်း» is pi-5's dassanena value from another kind of segment. The text's supplied «ဖြင့် ပယ်ရမည့် သဘောတရား၌» fills the Pāli ellipsis and has no keyword.

## Values that differ from pi-1 … pi-6 or the sample (same keyword)

- **bhāgo «အပိုင်း»** against pi-3 bhāga «သဘော» (case sibling): the reason is under Module overrides.
- **No other value set here differs.**
  - None of the g5 keywords is a sample (1-00 / 1-02) keyword with another value.
  - The g5 table keys have no pi-1 … pi-6 value of their own.
  - asekkhassa / asekkhañca now equal the pi-1 / pi-2 value of their siblings.
- **Module values.** The values the module gives (the T1–T13 families) are the phase-1 values; their pi-1 … pi-6 differences are listed in `map-table.md`.

## S1 (stem fallback) review

There are 56 uses in 4 keyword / value pairs. Each use was checked against its segment: **kept 56, corrected 0**.
- **gaṇitaṃ = «ရေတွက်ထားသော»** (49 uses): every one in «Yathā kusalattike … gaṇitaṃ, evaṃ gaṇetabbaṃ», where the text has «… ရေတွက်ထားသည့်အတိုင်း» (participle, rule 3).
- **Rūpiṃ / rūpiṃ = «ရုပ် ဖြစ်သော»** (3 + 3 uses): rūpī dhamma, «ရုပ် ဖြစ်သော»; arūpiṃ in the same segments is the module's «ရုပ် မဟုတ်သော».
- **cittasaṃsaṭṭhasamuṭṭhānaṃ = «စိတ်နှင့် ရောနှော၍ စိတ်မှ ဖြစ်ပေါ်လာသော»** (1 use, ^7-52-17): the text's term.

## Text inconsistencies (for the rails step; the translation is not changed)

1. **Pāli slips:**
   - 4-02 ^7-36-338 «asakkho» for asekkho. It is not in the keyword list; the Burmese has asekkha.
   - 4-05 ^7-39-36 «sāsavoca» for «sāsavo ca». Because of it the keyword list lacks sāsavo there, and the list is mapped as given.
2. **The -sadisa notes in three shapes:**
   - «…နှင့် တူသည်» (most);
   - the adverbial «…နှင့် တူအောင် အကျယ် ချဲ့ရမည်» (^7-44-17, ^7-47-104);
   - «…နှင့် တူသည့်အတိုင်း» after yathā (^7-47-76).

   This is phase-1 A4, extended to g5.
3. **The supplied «သဘောတရား»** inside the X-kusala / akusala / abyākata-sadisaṃ notes («…၏ ကုသိုလ် သဘောတရားနှင့် တူသည်»), against the bare dyad name of «lokiyadukasadisaṃ».
4. **The dyad names inside the notes use two words for «belonging to»:**
   - lokiyaduka «လောကနှင့် သက်ဆိုင်ခြင်း»;
   - kāmāvacaraduka «ကာမဘုံနှင့် ဆိုင်ခြင်း».

   They are mapped as the text has them.
5. **The elliptic «(dassane ekaṃ, nadassane dve)»** (4-13 ^7-47-6, ^7-47-17) is spelled out in the text as the full term «သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ရမည့် / ပယ်ရမည် မဟုတ်သော သဘောတရား၌».

## Unclear mappings (for the coordinator)

- **U-g5-1: the dyad items as qualifiers.** Examples: «Hetuṃ kusalaṃ dhammaṃ», «Āsavo akusalo dhammo», «akusalaṃ ganthaṃ dhammaṃ», where the text has «N ဖြစ်သော၊ …».
  - **What the module does.** It gives two shapes:
    - the bare noun from the binding pi-1 / pi-2 / pi-5 value (U3): Hetuṃ / hetuṃ «အမြစ်» 57, Cittaṃ «စိတ်», āsavo / āsavaṃ «စိတ်အစွန်းအထင်း», kileso / kilesaṃ, gantho / ganthaṃ, nīvaraṇo / nīvaraṇaṃ, upādāno, parāmāsaṃ, oghaṃ;
    - T13's «N ဖြစ်သော» where no pi value is present: Saññojanaṃ / saññojano «နှောင်ကြိုး ဖြစ်သော», yogaṃ «ထမ်းပိုး ဖြစ်သော».
  - **What g5 does.** It keeps both shapes as the module gives them, by U3 (a pi-1 … pi-6 value present as a phrase is kept), so g5 follows the module here.
  - **An alternative that was tried.** A context function gave every cluster item «N ဖြစ်သော» (T13), keeping the bare N after «no ca». It changed 65 uses, which went against U3, so it was withdrawn.
  - **Phase 3 should pick one shape book-wide:**
    - rule 2 (a predicated noun = the noun), which would make saññojano / yogaṃ bare;
    - T13 «N ဖြစ်သော» for every item (hetu and citta included).
- **U-g5-2 (G5-1): the inner «သဘောတရား» in the -sadisa notes.** It is kept. The alternative is a gapped value «…၏ ကုသိုလ် … နှင့် တူသည်», whose second chunk begins with the particle «နှင့်».
- **U-g5-3 (G5-3): naviññeyyo «မသိနိုင်သော».** The text's form is used against T8. Other groups (2-xx, 3-02) may meet the same keyword (13 uses book-wide).
- **U-g5-4 (G5-2): nevadassanena «သစ္စာကို မြင်ခြင်း … မဟုတ်».** It has no final «သော», unlike nadassanena. The text's neva-clause ends in «မဟုတ်၊».
- **U-g5-5: nadassane.** The module value «သစ္စာကို မြင်ခြင်း … မဟုတ်သော» is kept (as nadassanena). The fuller «သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ရမည် မဟုတ်သော» would cover the text's expansion of the ellipsis.
