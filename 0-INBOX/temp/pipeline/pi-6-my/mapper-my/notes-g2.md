# pi-6 Burmese keyword mapping, PHASE 2, group G2 (6-01 … 8): notes

Chapters 6-01 / 6-02 sankharayamaka, 7-01 … 7-11 anusayayamaka, 8-cittayamaka, mapped in chapter order by
`map_g2.py` (imports `map6_rules.py`, which is NOT edited; chapter tables T6 / T7 / T8, two new context functions).
Burmese from the FINAL pi-6 text, `my6-zeroshot-terms.md`, the zero-shot notes `notes-ch6-8.md` / `notes-ch7a.md` /
`notes-ch7b.md` and the final pi-1 … pi-5 mappings only. Not committed. Run:
`/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 map_g2.py [--report] [-v] [chapter-prefix …]`.
Read-only helpers: `work/g2_dump.py`, `work/g2_pairs.py`, `work/g2_grep.py` (and the phase-1 `work/show6.py`,
`work/prior6.py`).

## Numbers (verifier of the module + the brief's preservation command)

| chapter | lines | bad | presence failures | «, » / «၊» / « / » | (no direct equivalent) | chunks by an ending rule |
|---|---|---|---|---|---|---|
| 6-01-sankharayamaka | 152 | [] | 0 | 0 | 1 | verb 22, attr 4, abs 2 |
| 6-02-sankharayamaka | 122 | [] | 0 | 0 | 1 | verb 33, abs 4, attr 1 |
| 7-01-anusayayamaka | 41 | [] | 0 | 0 | 2 | verb 28 |
| 7-02-anusayayamaka | 34 | [] | 0 | 0 | 0 | - |
| 7-03-anusayayamaka | 37 | [] | 0 | 0 | 4 | verb 10 |
| 7-04-anusayayamaka | 37 | [] | 0 | 0 | 5 | - |
| 7-05-anusayayamaka | 37 | [] | 0 | 0 | 12 | verb 22 |
| 7-06-anusayayamaka | 37 | [] | 0 | 0 | 3 | - |
| 7-07-anusayayamaka | 62 | [] | 0 | 0 | 14 | verb 32 |
| 7-08-anusayayamaka | 12 | [] | 0 | 0 | 1 | verb 2 |
| 7-09-anusayayamaka | 50 | [] | 0 | 0 | 0 | attr 120, perf-pred 36, verb 10 |
| 7-10-anusayayamaka | 37 | [] | 0 | 0 | 2 | attr 110, verb 19 |
| 7-11-anusayayamaka | 10 | [] | 0 | 0 | 0 | verb 10, attr 9 |
| 8-cittayamaka | 205 | [] | 0 | 0 | 6 | verb 91, attr 41, perf-pred 15 |

- 873 lines; every (no direct equivalent) value is a keyword «(no direct equivalent)» of the keyword files (51 uses);
  no other keyword got (no direct equivalent).
- Presence: no failure and no exception; the chunks not found literally are matched by the approved ending rules of
  the verifier (pi-1 rules 3 / 4, pi-5 Q1 «abs», phase-3 «perf-pred» «Xပြီး ဖြစ်»). Values whose chunks stand in the
  text but not as one phrase are only the quoted cited sections (V3: the text has «“အကြင်သူအား” အပိုင်း», the value
  drops the quotation marks as the colophon titles of R6 do) and upapajjitvā «ပြန်လည် ဖြစ်ပေါ်၍» (R3, text «…ပြီး»).
- Values vs pi-1 … pi-5 (same keyword or its base form): 3497 uses the same, 3783 uses of keywords pi-1 … pi-5 never
  mapped, 339 uses (33 keyword / value pairs) different, listed below.
- Values vs the sample chapters (same keyword): one difference, uppajjissati = «ဖြစ်ပေါ်မည့်» (15, 6-02 ^6-6-88 …)
  against the sample's «ဖြစ်ပေါ်လိမ့်မည်»: R2, the future in a relative clause «… ဖြစ်ပေါ်မည့်သူတို့» (the segment
  has no «ဖြစ်ပေါ်လိမ့်မည်»; the module picks it).

## S1 review (stem fallback)

The module ALONE (no group table) maps 358 uses of the group by the stem fallback; each was checked against its
segment and the keyword's sense (`map_g2.py --report` recomputes the list):

- **kept 308 uses (46 chapter / keyword pairs)**: assāsapassāsā / -ānaṃ / -ehi «ဝင်လေ ထွက်လေ» (the text's word;
  pi-5 «ထွက်သက် ဝင်သက်» not in the text), catutthajjhānaṃ / -e «စတုတ္ထ ဈာန်», vitakkavicārehi «စတင်ကြံစည်မှုနှင့်
  ဆက်လက်သုံးသပ်မှု», cittasampayuttakā «စိတ်နှင့် ယှဉ်တွဲသော», vacī- / cittasaṅkhārañca, vacīsaṅkhāraṃ «နှုတ်၏ / စိတ်၏
  ပြုပြင်ဖန်တီးမှု», anulomampi / paccanīkampi «အဟုတ်ပြ / အငြင်းပြ ပုံစံ», Aṭṭhamako / aṭṭhamakañca «အဋ္ဌမ» (pi-5
  aṭṭhamakassa «အဋ္ဌမ», binding; the text's «ပုဂ္ဂိုလ်» after it has no keyword), pahīnā «ပယ်ပြီးသော», appahīnā
  «မပယ်ရသေးသော», kāma- / rūpa- / arūpadhātuṃ «ကာမဘုံ / သိမ်မွေ့သော ရုပ်ဘုံ / ရုပ်မရှိသော ဘုံ», araṇaṃ «ပဋိပက္ခ
  မရှိသော», khaṇaṃ «ခဏ», yamakāni «အတွဲလိုက် မေးဖြေခြင်း».
- **corrected 50 uses (20 pairs)**: samāpannānaṃ «ဝင်စားနေသော» -> «ဝင်စားနေသူ» (32; the agent noun P6, «… ဈာန်ကို
  ဝင်စားနေသူတို့»); the vāra names in body lines «ဖြစ်ပေါ်ခြင်း / ချုပ်ငြိမ်းခြင်း / ပိုင်းခြား သိခြင်း / ကိန်းအောင်းခြင်း /
  ပယ်ပြီးသော / ဖြစ်ခြင်း ခဏ» -> «Xအလိုက် ဖော်ပြချက်» (14; V1); paṭilomaṃ «ရသည်» -> «အငြင်းပြ ပုံစံ» (1); upapattināma
  «ပြန်လည် ဖြစ်ပေါ်သော» -> «ပြန်လည် ဖြစ်ပေါ်ခြင်း» (1; the text's noun «… ဖြစ်ပေါ်ခြင်း ဟူ၍»); cittake «စိတ်» ->
  «စိတ် အပိုင်း» (1; V3).
- In the final files 264 uses still come from the stem fallback, all of them in the «kept» list (the other 44 kept
  uses, pahīnā / appahīnā, now come from a group table with the same value).

## Rules used

pi-1 rules 1-11 and the agreed later pi-1 rules, pi-2 N1-N11, pi-3 M1-M9, pi-4 P1-P8 / A2, pi-5 Q1-Q8 / S1 / S3 / G1-G3
and the phase-1 rules R1-R9 (`map-table.md`), as settled by the coordinator 2026-11-22. Most used here: R1 (-ti / ca /
eva forms = the base's value: tesaṃyeva = tesaṃ «ထိုသူ», kāmadhātuṃyeva «ကာမဘုံ»), R2 (pajahati, parijānāti, anuseti,
nirujjhati in every tense and polarity; nānuseti «မကိန်းအောင်း»; the bare positive of a negated clause keeps the
positive), R3 (-amāna «…ဆဲ», -anta persons «…ဆဲသူ»), R5 (planes and beings, incl. the shared «P … ရှိသူ»), R6 (headings),
R8 (anusaya names in every case, -samaṅgī persons), rule 6 (the «၊» inside a term goes), rule 10 (« … »), P6 (agent nouns).

## NEW group rules (for review; the coordinator may move them into the module in phase 3)

V1. **vāra names in a body line** (R6 extended; f_vara): «X-vāro / -vāre / -vārepi / -vāraṃ / -vārena» in a colophon or
    an editorial note = «Xအလိုက် ဖော်ပြချက်», the heading form of the zero-shot notes (rule 1: the case particle «၌ / ကို /
    နှင့်» goes; Q4: api «လည်း» goes): uppāda ဖြစ်ပေါ်ခြင်း, nirodha ချုပ်ငြိမ်းခြင်း, uppādanirodha ဖြစ်ပေါ်ခြင်းနှင့်
    ချုပ်ငြိမ်းခြင်း, uppajjana ဖြစ်ပေါ်ခြင်း, pariññā ပိုင်းခြား သိခြင်း, pahīna ပယ်ပြီး ဖြစ်ခြင်း, pajahana ပယ်ခြင်း, anusaya
    ကိန်းအောင်းခြင်း, sānusaya ကိန်းအောင်းခြင်း ရှိသူ, uppattiṭṭhāna ဖြစ်ပေါ်ရာ နေရာ, puggala, dhamma, puggaladhamma; the
    compound «uppādavāranirodhavārepi» = «ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် ချုပ်ငြိမ်းခြင်းအလိုက် ဖော်ပြချက်» (the inner
    «နှင့်» stays). In a heading line the heading rule's whole part comes first. Every value is checked as a phrase.
V2. **sa- / nir-anusaya persons**: sānusayo / sānusayā = «ကိန်းအောင်းခြင်း ရှိသူ», niranusayo / niranusayā =
    «ကိန်းအောင်းခြင်း မရှိသူ» (agent noun P6; pi-5 ^5-606 «ကိန်းအောင်းခြင်း ရှိသူ»; the plural «များ» and the copula go). The
    anusaya in the instrumental keeps its R8 value «X ကိန်းအောင်းခြင်း», so «ကိန်းအောင်းခြင်း» stands in both values (see
    unclear U1).
V3. **cited sections of the editorial notes**: Yassakampi / yassakampi = «အကြင်သူအား အပိုင်း», yassayatthakampi /
    yassayatthake = «အကြင်သူအား အကြင်နေရာ၌ အပိုင်း», Yatthakampi / yatthakānaṃ = «အကြင်နေရာ၌ အပိုင်း», cittake (ch. 8
    «Yassa cittake …») = «စိတ် အပိုင်း»: the quoted lead of the text («“အကြင်သူအား” အပိုင်း») without the quotation
    marks + «အပိုင်း» (-ka); api / the locative «၌» / the plural «တို့» at the end go (Q4, rule 1); the lead keeps its own
    particles (they are the quoted words).
V4. **vitakka / vicāra qualifiers** (pi-1 ^1-M1-6, ^1-1401; rule 6): savitakkasavicāra = «စတင်ကြံစည်မှုနှင့်
    ဆက်လက်သုံးသပ်မှု ရှိသော», avitakkaavicāra = «စတင်ကြံစည်မှုလည်း မရှိ ဆက်လက်သုံးသပ်မှုလည်း မရှိသော» (the «၊» goes, the
    «လည်း» of «neither … nor» stays, as abyākata); with pacchimacitta / citta + moment = the whole phrase («… ရှိသော
    နောက်ဆုံး စိတ်၏ ဖြစ်ခြင်း ခဏ», harmonise B1 without «၌»), -samaṅgīnaṃ «… နောက်ဆုံး စိတ်နှင့် ပြည့်စုံသူ»;
    -bhūmiyaṃ = «… ရှိရာ အဆင့် / … မရှိရာ အဆင့်» (pi-1 sukhabhūmiyaṃ «…ရာ အဆင့်»). The same for sarāga- (ch. 8:
    «ရာဂ ရှိသော နောက်ဆုံး စိတ်၏ ဖြစ်ခြင်း ခဏ»), Pacchimakusalacittassa «နောက်ဆုံး ကုသိုလ်စိတ်».
V5. **dvandvas around a repeated noun**: Atītānāgataṃ (cittaṃ) «အတိတ် စိတ်နှင့် အနာဂတ် စိတ်» = «အတိတ် … အနာဂတ်»
    (rule 10; cittaṃ keeps its own keyword); saraṇaaraṇā «“ပဋိပက္ခ ရှိသော” “ပဋိပက္ခ မရှိသော” အတွဲ» = «ပဋိပက္ခ ရှိသော
    ပဋိပက္ခ မရှိသော အတွဲ» (the pair; the quotation marks and «တိုင်အောင်» of yāva go).
V6. **a plane genitive before pacchimacittaṃ** (f_plane_adj; harmonise A2): «yassa cittassa anantarā kāmāvacarānaṃ
    pacchimacittaṃ» = «ကာမဘုံနှင့် ဆိုင်သော» where the keyword's FIRST occurrence in the segment stands before
    «pacchimacittaṃ» (one sense per segment); otherwise the module's beings value («Kāmāvacarānaṃ pacchimacittassa
    uppādakkhaṇe» «ကာမဘုံ၌ ရှိသူတို့၊ နောက်ဆုံး စိတ်၏ …» is the beings).
V7. **other group values**: bhaṅgā = «ပြိုပျက်သော» (rule 3, a predicate adjective; the text's «ပြိုပျက်ကြသနည်း» by the
    ending rule, «ပြိုပျက်သော ကိန်းအောင်းခြင်း မရှိ»); the «na»-plane labels «(Nakāmadhātumūlakaṃ)» = the text's whole
    label as an adjective «ကာမဘုံ မဟုတ်သော ဘုံကို အခြေခံသော» (R4 mūlaka; rule 6 «၊» goes in the double ones); the cited
    chapter titles khandhayamake, saṅkhārayamakepi, dhammayamakanti = the approved titles (rule 7); Sattānusayā
    «ကိန်းအောင်းခြင်း ခုနစ်ပါး» (count with the text's classifier); paṭiloma- = paccanīka- «အငြင်းပြ ပုံစံ»; the ch. 8
    headings Suddhacittasāmañña(ṃ), Suttanta- / Abhidhammacittamissakaviseso, nanirodhavāro (the second half of the
    keyed «Uppajjamāna-nanirodhavāro»), Atikkantakālavāro = the text's whole heading (rule 7).

## Module overrides (map6_rules.py not edited; for phase 3)

O1. **kāyasaṅkhāro** (with -oti / -aṃ / -añca; 116 uses): the module takes the pi-2 / pi-5 key value «ကိုယ် ပြုပြင်ဖန်တီးမှု»
    by the «literal» tier of pi_get (its two chunks stand in the segment, but never as a phrase); override «ကိုယ်၏
    ပြုပြင်ဖန်တီးမှု», the text's phrase in every segment (= vacī- / cittasaṅkhāro «နှုတ်၏ / စိတ်၏», pi-5; the pi-5 rails
    have «ကိုယ်၏», zero-shot exception 1). Phase 3 may want pi_get's literal tier to require phrase_ok.
O2. **kāmāvacarānaṃ / rūpāvacarānaṃ / arūpāvacarānaṃ** (R5 shared_being): the regex «Pနှင့် … ၌ ရှိသူ» runs across
    other words of the clause, so «anantarā kāmāvacarānaṃ pacchimacittaṃ uppajjissati rūpāvacarānaṃ arūpāvacarānaṃ»
    gave «ကာမဘုံ … ရှိသူ» (the «ရှိသူ» of the other two planes, ^6-6-47); override V6 (3 uses of «ကာမဘုံနှင့် ဆိုင်သော»
    in the group, the other 28 kāmāvacarānaṃ the beings).
O3. **upapajjamāno** (7-11; 2): the module's -amāno «thing» form «ပြန်လည် ဖြစ်ပေါ်ဆဲ»; the person «heṭṭhā upapajjamāno»
    «အောက်၌ ပြန်လည် ဖြစ်ပေါ်ဆဲသူသည်» = «ပြန်လည် ဖြစ်ပေါ်ဆဲသူ» (P6). The module could treat -amāno (masc. nom.) as a person
    where the text has «…ဆဲသူ».
O4. **pahīnā** (7-09, 3): the pi-4 value «ပယ်ရသော» matched the negative «မပယ်ရသေး» by the ending rule «…သေး»;
    override «ပယ်ပြီးသော» (STOCK pahīno, pi-4 / pi-5; text «… ပယ်ပြီး ဖြစ်»).
O5. **uppannaṃ** (8; 39): the pi-1 value «ဖြစ်ပေါ်သော» stood only inside the concessive «ဖြစ်ပေါ်သော်လည်း» of uppajjati;
    override «ဖြစ်ပေါ်ပြီးသော» (pi-2), and the text's bare «ဖြစ်ပေါ်ပြီး» in the 5 segments that have the participle
    only before «မဟုတ်» («no ca tassa cittaṃ uppannaṃ» «… ဖြစ်ပေါ်ပြီး မဟုတ်»; see U4).
O6. **Yassa yattha / Yattha** (6; 8 uses): compose gave «အကြင်သူအား အကြင်» and pi-5 Yattha «အကြင်»; override «အကြင်သူအား
    အကြင်နေရာ» / «အကြင်နေရာ» (my6-zeroshot-terms §5 yattha = «အကြင်နေရာ၌», rule 1). pi-5's «အကြင်» is the bare
    relative before another noun (Kathāvatthu), not this okāsa lead.
O7. **vāra names in body lines** (V1): the module had no value (unmapped) or the stem value of the bare action noun
    («ဖြစ်ပေါ်ခြင်း», «ပိုင်းခြား သိခြင်း», «ပယ်ပြီးသော»; uppādavāre «ဖြစ်ခြင်း ခဏ»).
O8. **samāpannānaṃ** (6; 32): stem «ဝင်စားနေသော» -> «ဝင်စားနေသူ» (P6), «ဝင်စားနေသော» kept as the attributive alt.
O9. Gaps the module leaves (no value at all), filled by the tables: tesaṃyeva / kāmadhātuṃyeva (R1 has no base value),
    sānusaya / niranusaya, the vitakka / vicāra phrases, Sattānusayā, paṭiloma-, the cited sections, bhaṅgā, the
    dhātu labels and colophons, the ch. 8 headings, Atītānāgataṃ, saraṇaaraṇā, the source slips.

## Values different from pi-1 … pi-5 (same keyword), with the reason

| keyword = pi-6 value | pi-1 … pi-5 value (uses here) | reason |
|---|---|---|
| kāyasaṅkhāro (-oti, -aṃ, -añca, Kāya-) = ကိုယ်၏ ပြုပြင်ဖန်တီးမှု | ကိုယ် ပြုပြင်ဖန်တီးမှု (112); ကိုယ်ဖြင့် … (4) | O1: the text's phrase; the pi values are not a phrase of any segment |
| vacīsaṅkhārañca / -aṃ = နှုတ်၏ ပြုပြင်ဖန်တီးမှု | နှုတ်ဖြင့် ပြုပြင်ဖန်တီးမှု (5) | the pi-5 base value «နှုတ်၏» (vacīsaṅkhāro); «နှုတ်ဖြင့်» not in the text |
| kāmāvacarānaṃ / Kāmā- = ကာမဘုံ၌ ရှိသူ | ကာမဘုံနှင့် ဆိုင်သော (28) | R5 beings (gen. pl. of persons); pi-1's citta adjective is the other sense, kept where the text has it (V6) |
| arūpāvacare / -aṃ, rūpāvacare = (the plane) | …ဘုံနှင့် ဆိုင်သော (22) | R5: the plane as a place «…၌»; pi-1's adjective of citta not in the segment |
| kāma- / rūpa- / arūpadhātuṃ (-yeva) = ကာမဘုံ … | ကာမ ဓာတ် … (56) | the planes of the dhātupucchā «…ဘုံ၌» (pi-2 kāmadhātu «ကာမဘုံ»); «ဓာတ်» not in the segment |
| parijānanti = ပိုင်းခြား သိသည် | ပိုင်းခြား သိ၍ (19) | R2 finite verb (rule 4); the absolutive is not in the segment |
| uppajjamānaṃ / nirujjhamānaṃ (-nti, -ñca) = ဖြစ်ပေါ်ဆဲ / ချုပ်ငြိမ်းဆဲ | …သော (44) | R3 -amāna «…ဆဲ» (the text's word) |
| uppajjissati = ဖြစ်ပေါ်မည့် | ဖြစ်ပေါ်လိမ့်မည် (15) | R2: future in a relative clause (rule 3) |
| anulomaṃ / paccanīkaṃ = အဟုတ်ပြ / အငြင်းပြ ပုံစံ | အစဉ်အတိုင်း / ပြောင်းပြန် (17) | approved sample departure 2 |
| Atītānāgataṃ = အတိတ် … အနာဂတ် | အတိတ်နှင့် အနာဂတ် (9) | V5: «အတိတ် စိတ်နှင့် အနာဂတ် စိတ်»; the pi phrase not in the segment |
| uppannaṃ = ဖြစ်ပေါ်ပြီး | ဖြစ်ပေါ်ပြီးသော (5) | O5 / U4: the attributive not in these segments |
| Yattha = အကြင်နေရာ | (no direct equivalent) / အကြင် (2) | O6 |
| Assāsapassāsā = ဝင်လေ ထွက်လေ | ထွက်သက် ဝင်သက် (1) | the text's word (zero-shot notes: pi-5 ^5-333 rails); the pi-5 key value is not in the text |

## Text inconsistencies (for the rails step; the translation was not changed)

T1. (harmonise A2, extended) One segment reads the same genitive plural two ways: «Kāmāvacarānaṃ pacchimacittassa
    uppādakkhaṇe» = the beings «ကာမဘုံ၌ ရှိသူတို့၊ နောက်ဆုံး စိတ်၏ ဖြစ်ခြင်း ခဏ၌», «anantarā kāmāvacarānaṃ
    pacchimacittaṃ» = the adjective «ကာမဘုံနှင့် ဆိုင်သော နောက်ဆုံး စိတ်» (6-02 ^6-6-88, ^6-6-91, ^6-6-140 …).
T2. uppāda: the vāra headings and colophons «ဖြစ်ပေါ်ခြင်း(အလိုက်)», the moment «ဖြစ်ခြင်း ခဏ» (zero-shot exception 2);
    Uppajjanavāro (7-10) and Uppādavāro both «ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်»; Pahīnavāro «ပယ်ပြီး ဖြစ်ခြင်းအလိုက်».
T3. kāyasaṅkhāro: the pi-2 / pi-5 FINAL mappings «ကိုယ် ပြုပြင်ဖန်တီးမှု» against every pi-5 / pi-6 text «ကိုယ်၏» (O1).
T4. Source slips, mapped as the intended word: kāmārāgānusayo (7-01 ^6-7-21, 2), Pajahanāvāre (7-06 ^6-7-197),
    paccanīkaokāsā (6-01 ^6-6-16-5-0), Dhātuvisajjavāro (7-11 ^6-7-349); the heading «4 (Ṅa) paccanīkaokāso» standing in
    the body of ^6-6-65 and «(14) Atikkantakālavāro» in the body of ^6-8-82 (keys mapped to the heading text).
T5. Keyword gaps: the heading «Uppajjamāna-nanirodhavāro» is keyed as two parts «Uppajjamāna, nanirodhavāro» in four
    headings but as one «Uppajjamānananirodhavāro» in ^6-8-10-7-0 (each mapped to its part / the whole); «Yassa cittake
    … yaṃ cittake … yassa yaṃ cittake» (^6-8-113) has one keyword «cittake» for three cited sections; the second
    kāmāvacarānaṃ of ^6-6-88 has no keyword of its own.

## Unclear mappings (for review)

U1. sānusayo / niranusayo «ကိန်းအောင်းခြင်း ရှိသူ / မရှိသူ» share «ကိန်းအောင်းခြင်း» with the anusaya keyword before
    them; the alternative is the bare «ရှိသူ / မရှိသူ» (the anusaya element given to the anusaya keyword only, pi-2's
    one-word-two-members decision).
U2. The cited sections (V3) drop the quotation marks of «“အကြင်သူအား” အပိုင်း»; with the marks the value would be a
    literal phrase.
U3. saraṇaaraṇā includes the translator's «အတွဲ» (pair); without it «ပဋိပက္ခ ရှိသော … ပဋိပက္ခ မရှိသော».
U4. uppannaṃ «ဖြစ်ပေါ်ပြီး» (5 uses) has no dictionary ending: the presence check refuses «ဖြစ်ပေါ်ပြီးသော» where the
    text has only «ဖြစ်ပေါ်ပြီး မဟုတ်» (no ending rule for «Xပြီး မဟုတ်»). Phase 3 could add that ending («perf-pred»
    with «မဟုတ်») and use «ဖြစ်ပေါ်ပြီးသော» throughout.
U5. Aṭṭhamako «အဋ္ဌမ» follows pi-5 (binding) although the text always says «အဋ္ဌမ ပုဂ္ဂိုလ်» and no keyword takes «ပုဂ္ဂိုလ်».
U6. tesaṃyeva = «ထိုသူ» by R1 (eva has no word of its own), against harmonise B1's «ထိုသူတို့၏ပင်» (the text's form).
U7. vattamāne «ဖြစ်နေသော» (pi-5) against the text's «ဖြစ်နေစဉ်» (present by the ending rule «စဉ်»); bhaṅgā «ပြိုပျက်သော»
    against the text's verb «ပြိုပျက်ကြသနည်း» (ending rule «ကြ»).
