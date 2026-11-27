# pi-6 Burmese keyword mapping, PHASE 1: rules and review table (Yamaka «အတွဲလိုက် မေးဖြေခြင်း»: preamble, 1-mulayamaka, 2-01-khandhayamaka)

Written by `map_sample.py --table` with the shared module `map6_rules.py` (imported by the three phase-2 agents; no
work at import). Burmese from the FINAL text of this track only (`AI_translation/burmese/pi-6-burmese-plain-zeroshot_split_chapters`),
`my6-zeroshot-terms.md` and the final pi-1 … pi-5 Burmese mappings; no other Burmese source. The sample chapters need
no chapter table and no per-segment override: every value comes from the module.


## Numbers

- `preamble.mapped.md`: 3 lines, keyword preservation `bad []`, presence failures 0, «, » / «၊» / « / » in a value 0, (no direct equivalent) 0, chunks matched by an ending rule 1.
- `1-mulayamaka.mapped.md`: 139 lines, keyword preservation `bad []`, presence failures 0, «, » / «၊» / « / » in a value 0, (no direct equivalent) 0, chunks matched by an ending rule 189.
- `2-01-khandhayamaka.mapped.md`: 195 lines, keyword preservation `bad []`, presence failures 0, «, » / «၊» / « / » in a value 0, (no direct equivalent) 0, chunks matched by an ending rule 22.
- Keyword uses 1911: the same value as a pi-1 … pi-5 mapping of that keyword (or of its base form, R1) 975 (in 91 keywords); a keyword that pi-1 … pi-5 never mapped 856; a value different from pi-1 … pi-5 80 (in 16 keyword / value pairs, listed below with the reason).
- Source of the values (uses): stock 471, mula 388, khandha 371, verb 283, place 123, base 102, terms 97, frame 41, compose 28, heading 4, title 3 (frame / stock = the module tables; verb / khandha / mula / place / family = the morphology R2-R5, R8; base = R1 on a table value; terms = my6-zeroshot-terms; compose = members joined (Q3); heading = R6; title = rule 7).

## Rules used (binding, unchanged)

The value is the word or phrase of THAT segment's Burmese (the FINAL pi-6 text) that carries the keyword, in the
dictionary form of the approved Burmese mappings:

- **pi-1** rules 1-11 (approved 2026-11-17): nouns without final case particles / plural markers (rule 1; inner
  particles stay); a noun predicated of a subject = the noun (rule 2); adjectives / participles «…သော», gerundives /
  future participles «…မည့်» (rule 3); verbs «…သည်» (rule 4); «X dhammā» = «X သဘောတရား» (rule 5); sentence-final
  material and the «၊» inside a term dropped (rule 6: abyākata = ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော); titles
  whole (rule 7); a fragment that lost its negative = the positive part (rule 8); particles (rule 9); « … » for
  discontinuous parts, no « / », no «, » / «၊» in a value (rule 10); sense by context (rule 11). The agreed later
  pi-1 rules: absolutives keep «…၍»; relative pronouns = (no direct equivalent) where the Burmese builds the clause
  with «ရှိသော / ရှိသမျှ» (no relative pronoun is a keyword in the sample); one sense per segment; counts keep the
  text's classifier; caya = (no direct equivalent) where apacaya is one word (not in the sample).
- **pi-2** N1-N11 and the harmonise decisions (one Burmese word for two compound members: one member gets it, the
  other (no direct equivalent); «na uppajjati = … မဖြစ်ပေါ်»).
- **pi-3** M1-M9 (the « … » gap; the presence endings of M7); **pi-4** P1-P8 / A2 (person names, agent nouns «…သူ»
  (P6), the presence endings of P3, «X၍» against «မXဘဲ», «puggalo P» in text order (P8)).
- **pi-5** Q1-Q8 (Q1 presence endings «…သလော / …ပါ / …ပြီး», Q2 Āmantā = ဟုတ်ပါသည် whole, Q3 multiword keywords in
  text order with the finite verb last, Q4 the «လည်း» of ca is not part of a multiword keyword, Q5 negated verbs = the
  text's «မ + verb» without «သည်» and the bare positive of a negated segment keeps the positive), S1 (stem fallback),
  S3 / G3 (a negative inside a multiword keyword), G1 / G2 (the Pāli order of two composed members).
- **pi-1 … pi-5 values**: a keyword the module tables and the morphology below do not settle is looked up in the FINAL
  pi-1 … pi-5 mappings (`AI_translation/burmese/pi-{1,2,3,4,5}-keywords-by-reference-pali-burmese-plain.md`; order
  pi-2, pi-3, pi-4, pi-5, pi-1): the most frequent value the segment has as a phrase, then one whose chunks are all
  literal, then one present by an ending rule. The module tables themselves take the pi-1 … pi-5 value wherever the
  segment has it (khandha names, bare terms, kusala / akusala / abyākata, avasesa, ṭhapetvā, the preamble, Natthi,
  uppajjati / uppajjissati, anusaya, sacca, indriya and āyatana names).

## How the module is built (`map6_rules.py`)

Lookup per keyword: CTX[segment] → chapter table → FRAME → STOCK → chapter title (rule 7) → morphology (R2 verbs, R3
participles, R4 khandha and root compounds, R8 families, R5 planes) → «(X-mūlakaṃ)» labels (R4) → the tables for the
base form (R1) → the pi-5 chain (my6-zeroshot-terms, pi-1 … pi-5 value as a phrase, compose Q3-Q5, counts, pi-1 … pi-5
value by an ending rule) for the keyword, then for its base forms → stem fallback (S1) → heading rule (R6); every value
then passes R7. A value «@name» calls a context function (FUNCS); a tuple = the first value the segment has (alt).
Every morphological value is a list of candidates checked against the segment (`pick`): the text's own form wins.
`Mapper(chapter_tables=…, ctx=…, stem=make_stem([...]))` is the entry point, `verify_file(ch)` the verifier,
`frame_coverage.py` the whole-book check.

## NEW rules (beyond pi-1 … pi-5), for review

R1. **«-ti» and «ca» forms = the base form's value** (pi-1 rule 9 / pi-5 Q4 for one keyword): vedanākkhandhoti =
    ခံစားမှု အစုအဝေး, uppajjatīti = ဖြစ်ပေါ်သည်, uppajjitthāti = ဖြစ်ပေါ်ခဲ့သည်, rūpanti = ရုပ်, kusalañca = ကုသိုလ်,
    ekamūlañceva = တူညီသော အမြစ် ရှိသော, Viññāṇañca = သိစိတ် (not the pi-1 / pi-5 homograph viññāṇañc-āyatana). The
    question mark and the quotative have no Burmese word; the Yamaka repeats every term with «-ti» in its niddesa.
R2. **Pavatti verbs in every tense and polarity** (pi-1 rule 4, pi-1 uppajjissati, Q5 extended to the tenses): present
    «Sသည်», past «Sခဲ့သည်», future «Sလိမ့်မည်» (uppajjati ဖြစ်ပေါ်သည်, uppajjittha ဖြစ်ပေါ်ခဲ့သည်, uppajjissati
    ဖြစ်ပေါ်လိမ့်မည်); the negative = the text's «မ + S (+ ခဲ့ / လိမ့်မည်)» without «သည်» (nuppajjati မဖြစ်ပေါ်, nuppajjittha
    မဖြစ်ပေါ်ခဲ့, nuppajjissati မဖြစ်ပေါ်လိမ့်မည်; na nirujjhati မချုပ်ငြိမ်း; nappajahati မပယ်; nānuseti မကိန်းအောင်း); a
    future in a relative clause = the future participle «Sမည့်» (rule 3: parinibbāyissanti «… ပရိနိဗ္ဗာန် ပြုမည့်သူတို့»
    = ပရိနိဗ္ဗာန် ပြုမည့်; aggamaggaṃ paṭilabhissanti = အမြတ်ဆုံး မဂ်ကို ရရှိမည့်); the bare keyword of a negated Pāli
    clause («na nirujjhittha» -> nirujjhittha) keeps the positive (rule 8 / Q5). The short answers Uppajjati. /
    Uppajjittha. = the same verbs. Roots: uppajj ဖြစ်ပေါ်, nirujjh ချုပ်ငြိမ်း, upapajj ပြန်လည် ဖြစ်ပေါ်, cav စုတေ,
    parinibbāy ပရိနိဗ္ဗာန် ပြု (pi-2 / pi-5 termbase values), and for the later vāras pajah ပယ်, parijān ပိုင်းခြား သိ,
    bhāve ပွားများ, sacchikar မျက်မှောက်ပြု, paṭilabh ရရှိ, anuset ကိန်းအောင်း (the pi-6 text; pi-2 / pi-5 values).
R3. **Participles**: a person participle = the agent noun «Sဆဲသူ» (pi-4 P6; upapajjantānaṃ ပြန်လည် ဖြစ်ပေါ်ဆဲသူ,
    cavantānaṃ စုတေဆဲသူ, parinibbantānaṃ ပရိနိဗ္ဗာန် ပြုဆဲသူ); where the text puts the participle before another
    person noun without a marker, the text's «Sဆဲ» (rule 3: «ပြန်လည် ဖြစ်ပေါ်ဆဲ နောက်ဆုံး ဘဝ ရှိသူတို့»); -amāna things
    «Sဆဲ»; the absolutive «S၍» (upapajjitvā ပြန်လည် ဖြစ်ပေါ်၍ against the text's «…ပြီး», pi-5 Q1).
R4. **The ch. 1 root compounds** (my6-zeroshot-terms §7; the text builds two shapes):
    a root noun predicated with the copula «ဖြစ်ကြ» = the noun (rule 2): kusalamūlā / -mūlāni / -mūlena = ကုသိုလ်၏
    အမြစ် (the instrumental's «နှင့်» goes, rule 1), kusalamūlamūlā = ကုသိုလ်၏ အမြစ်၏ အမြစ်, aññamaññamūlā = အချင်းချင်း
    အမြစ်, aññamaññamūlamūlā = အချင်းချင်း အမြစ်၏ အမြစ်, abyākatamūlā = ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော
    အမြစ်, nāmamūlā = စိတ်ပိုင်း၏ အမြစ်, Mūlāni = အမြစ်; a possessive built with «ရှိ» and a «based on» adjective = the
    attributive (rule 3): ekamūlā / -mūlaṃ = တူညီသော အမြစ် ရှိသော, ekamūlamūlā = တူညီသော အမြစ်၏ အမြစ် ရှိသော,
    kusalamūlakā = ကုသိုလ်၏ အမြစ်ကို အခြေခံသော, ekamūlakā = တူညီသော အမြစ်ကို အခြေခံသော, aññamaññamūlakā =
    အချင်းချင်း အမြစ်ကို အခြေခံသော (the object «…ကို» stays, as pi-1 hetusampayutta-type compounds); Kusalasamuṭṭhānaṃ
    = ကုသိုလ်မှ ဖြစ်ပေါ်လာသော (pi-1 cittasamuṭṭhāna); kusalamūlasahajātā = ကုသိုလ်၏ အမြစ်နှင့်အတူ ပေါ်ပေါက်သော (pi-5
    sahajāta); Sahetukaṃ / Ahetukaṃ = အမြစ် ရှိသော / မရှိသော (pi-1); the hetuvāra predicates X-hetū … X-samudayā = «X၏ Y»
    with each synonym its own word (kusalahetū ကုသိုလ်၏ အကြောင်း, kusalanidānā … ဇာစ်မြစ်, -sambhavā ဖြစ်တည်ရာ, -ppabhavā
    ပေါ်ထွက်ရာ, -samuṭṭhānā ဖြစ်ပေါ်လာရာ, -āhārā အာဟာရ, -ārammaṇā အာရုံ, -paccayā အထောက်အပံ့, -samudayā ဖြစ်ပေါ်ခြင်း)
    and the verse words alone (hetu အကြောင်း, nidānaṃ ဇာစ်မြစ် … Samuṭṭhānāhārārammaṇā = ဖြစ်ပေါ်လာရာ အာဟာရ အာရုံ: the
    list's «၊» goes, rule 6). The later chapters' labels «(Cakkhāyatanamūlakaṃ)» «(မျက်စိ အာရုံခံ နယ်ပယ်ကို အခြေခံ၍)» =
    the term's value + «ကို အခြေခံသော» (the same adjective; the text's «၍» by the ending rule).
R5. **Planes and the beings of a plane**: a plane in any case = its name without the case particle (rule 1:
    Pañcavokāre / -vokāraṃ / -vokārā = အစုအဝေး ငါးပါး ရှိသော ဘဝ, Asaññasatte / -sattaṃ / -sattā = အသညသတ် ဘုံ, arūpe /
    arūpaṃ = ရုပ်မရှိသော ဘုံ, Suddhāvāse = သုဒ္ဓါဝါသ ဘုံ, kāmadhātuyā = ကာမဘုံ, rūpadhātuyā = သိမ်မွေ့သော ရုပ်ဘုံ); the
    beings of a plane (-ānaṃ) = the text's agent noun «P၌ ရှိသူ» (P6: Arūpānaṃ ရုပ်မရှိသော ဘုံ၌ ရှိသူ, Suddhāvāsānaṃ
    သုဒ္ဓါဝါသ ဘုံ၌ ရှိသူ), its attributive «P၌ ရှိသော» before another person noun (rule 3: «… ဘဝ၌ ရှိသော အခြားသူတို့»),
    the beings' own name where pi-2 has it (asaññasattānaṃ = အသညသတ်); where two planes share one «…၌ ရှိသူ», the first
    plane's value is «P … ရှိသူ» (rule 10); a plane adjective of a noun = «Pနှင့် ဆိုင်သော» (kāmāvacarānaṃ
    pacchimacittaṃ «ကာမဘုံနှင့် ဆိုင်သော နောက်ဆုံး စိတ်»). Persons: Itaresaṃ = အခြားသူ (the text's «အခြား ယောက်ျားတို့» = အခြား),
    Pacchimabhavikānaṃ = နောက်ဆုံး ဘဝ ရှိသူ (or the attributive «… ရှိသော» before a noun), Sabbesaṃ = အားလုံး.
R6. **Headings and colophons** (rule 7): a vāra / naya / uddesa heading keyword that IS a whole part of the heading
    (between the labels «(Ka) / (1) / 2.») = the text's whole part (Pavattivāro = ဖြစ်ပျက်ခြင်းအလိုက် ဖော်ပြချက်,
    uppādavāro = ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်); the named headings of my6-zeroshot-terms §2 (Mūlanayo = အမြစ်
    ခွဲနည်း, anulomapuggalo = ပုဂ္ဂိုလ်အလိုက် အဟုတ်ပြ ပုံစံ …); a colophon «X niṭṭhito» = the title inside «“ … ”»
    (Uddesavāro = အကျဉ်း ဖော်ပြချက်, Mūlayamakapāḷi = အမြစ်များကို အတွဲလိုက် မေးဖြေခြင်း); the chapter titles Xyamakaṃ =
    the approved «Xများကို အတွဲလိုက် မေးဖြေခြင်း» (my6-zeroshot-terms §1).
R7. **The «လည်း» gap inside one keyword's value** (rule 10 / Q4): a value the text has as a phrase only with the
    «လည်း» of ca inside it gets « … » at that place (e.g. «ကုသိုလ်၏ အမြစ်ကိုလည်း အခြေခံ» alone = ကုသိုလ်၏ အမြစ်ကို …
    အခြေခံသော); not used in the sample (each such segment also has the phrase whole in its question), kept for phase 2.
    The «လည်း» of «neither … nor» inside a term stays (rule 6). The phrase checks of the module ignore the list comma
    «၊» (rule 6), so abyākata compounds glue to their head («… မဟုတ်သော အမြစ်နှင့်အတူ ပေါ်ပေါက်သော သဘောတရား»).
R8. **Families of compound names** (found by the frame-coverage check, for phase 2): the seven anusayā in every case
    = «X ကိန်းအောင်းခြင်း» (pi-2 / pi-5); the four sacca = «X သစ္စာ» (dukkha ဒုက္ခ pi-2, nirodha ချုပ်ငြိမ်းခြင်း pi-5,
    samudaya ဖြစ်ပေါ်ခြင်း, magga မဂ် in the pi-6 text); X-samaṅgī / -samaṅgīnaṃ = «Xနှင့် ပြည့်စုံသူ» (agent noun P6;
    harmonise-table), attributive «…နှင့် ပြည့်စုံသော» before a noun (aggamagga အမြတ်ဆုံး မဂ်, pacchimacitta နောက်ဆုံး
    စိတ်, anāgāmimagga အနာဂါမိမဂ်, magga မဂ်); moment phrases = «… ခဏ» without the final «၌» (harmonise B1: cittassa
    bhaṅgakkhaṇe = စိတ်၏ ပြိုပျက်ခြင်း ခဏ, uppādakkhaṇe = ဖြစ်ခြင်း ခဏ), pavatte = ဘဝ တည်နေစဉ်; a count + noun keyword
    = the text's noun + count with its classifier (pi-1 decision 5: dvīsu vedanāsu = ခံစားမှု နှစ်ပါး).
R9. **Answers**: Āmantā = ဟုတ်ပါသည် (Q2); Natthi keeps the pi-1 … pi-5 value မရှိသည် (rule 4; the text «မရှိပါ။» by
    the ending «ပါ», Q1); the answer No = မဟုတ်ပါ whole, as Āmantā (Q2; the pi-2 «no = မဟုတ်» is the negative particle
    of a Mātikā compound, another kind of segment). A keyword «(no direct equivalent)» of the keyword files keeps that
    value.


## Values different from pi-1 … pi-5 (same keyword)

| keyword = pi-6 value | pi-1 … pi-5 value (uses here) | reason |
|---|---|---|
| nāmā = စိတ်ပိုင်း | အမည် (20) | rule 11 (sense): nāma = mentality «စိတ်ပိုင်း» (pi-1 nāma ^1-M2-109, my6-zeroshot-terms §7); pi-5 «အမည်» is 'name' and not in the segment |
| nāmāti = စိတ်ပိုင်း | အမည် (12) | rule 11 (sense): nāma = mentality «စိတ်ပိုင်း» (pi-1 nāma ^1-M2-109, my6-zeroshot-terms §7); pi-5 «အမည်» is 'name' and not in the segment |
| anulomaṃ = အဟုတ်ပြ ပုံစံ | အစဉ်အတိုင်း (8) | approved sample departure 2 (notes-sample): the Yamaka sense «အဟုတ်ပြ ပုံစံ» (affirmative form); pi-5 «အစဉ်အတိုင်း» is the debate order and not in the segment |
| paccanīkaṃ = အငြင်းပြ ပုံစံ | ပြောင်းပြန် (8) | as anulomaṃ: «အငြင်းပြ ပုံစံ» (negated form); pi-5 «ပြောင်းပြန်» not in the segment |
| arūpaṃ = ရုပ်မရှိသော ဘုံ | ရုပ် မဟုတ်သော (5) | rule 11 (sense): the plane «ရုပ်မရှိသော ဘုံ» (pi-5 arūpe, my6-zeroshot-terms §6); pi-2 / pi-5 «ရုပ် မဟုတ်သော» is the adjective 'non-material', not in the segment |
| ekamūlakaṃ = တူညီသော အမြစ်ကို အခြေခံသော | တစ်မျိုးတွဲကို အခြေခံသော (4) | the pi-6 text's word «တူညီသော အမြစ်ကို အခြေခံ» (eka = the same root, notes-sample); pi-3 «တစ်မျိုးတွဲကို အခြေခံသော» (Dhātukathā ekamūlaka) is not in the segment |
| Arūpaṃ = ရုပ်မရှိသော ဘုံ | ရုပ် မဟုတ်သော (4) | rule 11 (sense): the plane «ရုပ်မရှိသော ဘုံ» (pi-5 arūpe, my6-zeroshot-terms §6); pi-2 / pi-5 «ရုပ် မဟုတ်သော» is the adjective 'non-material', not in the segment |
| Arūpā = ရုပ်မရှိသော ဘုံ | ရုပ် မဟုတ်သော (4) | rule 11 (sense) / R5: the ablative of the plane «ရုပ်မရှိသော ဘုံမှ» (Arūpā cavantānaṃ); pi-2 «ရုပ် မဟုတ်သော» is the adjective 'non-material', not in the segment |
| ekamūlakañceva = တူညီသော အမြစ်ကို အခြေခံသော | တစ်မျိုးတွဲကို အခြေခံသော (3) | the pi-6 text's word «တူညီသော အမြစ်ကို အခြေခံ» (eka = the same root, notes-sample); pi-3 «တစ်မျိုးတွဲကို အခြေခံသော» (Dhātukathā ekamūlaka) is not in the segment |
| Nāmā = စိတ်ပိုင်း | အမည် (2) | rule 11 (sense): nāma = mentality «စိတ်ပိုင်း» (pi-1 nāma ^1-M2-109, my6-zeroshot-terms §7); pi-5 «အမည်» is 'name' and not in the segment |
| paccayo = အထောက်အပံ့ | အကြောင်း (2) | the hetuvāra list gives each of the ten synonyms its own word (notes-sample departure 1): paccaya «အထောက်အပံ့» (pi-1 ^1-1344); pi-5 «အကြောင်း» is hetu's word in the same verse |
| sambhavo = ဖြစ်တည်ရာ | ဖြစ်ပေါ်လာသော (2) | the hetuvāra word «ဖြစ်တည်ရာ» (NEW in the pi-6 text); pi-2 «ဖြစ်ပေါ်လာသော» not in the segment |
| kusalahetū = ကုသိုလ်၏ အကြောင်း | ကုသိုလ် အမြစ် (2) | approved sample departure 1: hetu «အကြောင်း» in the hetuvāra list; pi-1 / pi-2 «ကုသိုလ် အမြစ်» not in the segment |
| Viññāṇañca = သိစိတ် | အဆုံး မရှိသော သိစိတ် (2) | R1: viññāṇaṃ + ca «သိစိတ်»; the pi-1 / pi-5 key viññāṇañca is the homograph of viññāṇañc(āyatana) «အဆုံး မရှိသော သိစိတ်», not in the segment |
| kusalahetūti = ကုသိုလ်၏ အကြောင်း | ကုသိုလ် အမြစ် (1) | approved sample departure 1: hetu «အကြောင်း» in the hetuvāra list; pi-1 / pi-2 «ကုသိုလ် အမြစ်» not in the segment |
| nāmapaccayā = စိတ်ပိုင်း၏ အထောက်အပံ့ | စိတ်ပိုင်းကြောင့် (1) | the hetuvāra predicate «စိတ်ပိုင်း၏ အထောက်အပံ့» (X-paccayā = having X as support); pi-2 «စိတ်ပိုင်းကြောင့်» is the paṭiccasamuppāda ablative and not in the segment |

## Presence: chunks matched by an ending rule (no other exception)

Every chunk of every value stands in its segment's Burmese, literally or by one of the approved ending rules of the verifier (pi-1 rules 3 / 4 / 8, pi-2 N11, pi-3 M7, pi-4 P3 / A2, pi-5 Q1): no presence failure and no exception outside these rules.

| rule | chunks | example |
|---|---|---|
| attr | 172 | ^6-1-2 ekamūlā: «ရှိသော» |
| verb | 38 | ^T-1 Namo: «ရှိခိုးသည်» |
| abs | 2 | ^6-2-62 upapajjitvā: «ဖြစ်ပေါ်၍» |

## Keyword → Burmese (sample chapters; uses; source)

| keyword | Burmese | uses | source |
|---|---|---|---|
| Abhidhammapiṭake | အဘိဓမ္မာပိဋက | 1 | frame |
| abyākatamūlakaṃ | ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော အမြစ်ကို အခြေခံသော | 1 | mula |
| abyākatamūlakā | ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော အမြစ်ကို အခြေခံသော | 2 | mula |
| abyākatamūlakāti | ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော အမြစ်ကို အခြေခံသော | 1 | mula |
| abyākatamūlamūlakaṃ | ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော အမြစ်၏ အမြစ်ကို အခြေခံသော | 1 | mula |
| abyākatamūlamūlakā | ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော အမြစ်၏ အမြစ်ကို အခြေခံသော | 2 | mula |
| abyākatamūlamūlakāti | ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော အမြစ်၏ အမြစ်ကို အခြေခံသော | 1 | mula |
| abyākatamūlamūlā | ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော အမြစ်၏ အမြစ် | 2 | mula |
| abyākatamūlamūlāni | ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော အမြစ်၏ အမြစ် | 1 | mula |
| abyākatamūlamūlāti | ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော အမြစ်၏ အမြစ် | 1 | mula |
| abyākatamūlasahajātā dhammā | ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော အမြစ်နှင့်အတူ ပေါ်ပေါက်သော သဘောတရား | 4 | compose |
| abyākatamūlena | ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော အမြစ် | 16 | mula |
| abyākatamūlā | ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော အမြစ် | 2 | mula |
| abyākatamūlāni | ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော အမြစ် | 5 | mula |
| abyākatamūlāti | ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော အမြစ် | 1 | mula |
| abyākataṃ | ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော | 6 | stock |
| abyākatā | ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော | 13 | stock |
| Abyākatā dhammā | ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော သဘောတရား | 2 | stock |
| abyākatā dhammā | ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော သဘောတရား | 16 | stock |
| abyākatāti | ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော | 12 | base:stock |
| Ahetukaṃ | အမြစ် မရှိသော | 18 | stock |
| akusalamūlakañceva | အကုသိုလ်၏ အမြစ်ကို အခြေခံသော | 1 | mula |
| akusalamūlakaṃ | အကုသိုလ်၏ အမြစ်ကို အခြေခံသော | 1 | mula |
| akusalamūlakā | အကုသိုလ်၏ အမြစ်ကို အခြေခံသော | 2 | mula |
| akusalamūlakāti | အကုသိုလ်၏ အမြစ်ကို အခြေခံသော | 1 | mula |
| akusalamūlamūlakañceva | အကုသိုလ်၏ အမြစ်၏ အမြစ်ကို အခြေခံသော | 1 | mula |
| akusalamūlamūlakaṃ | အကုသိုလ်၏ အမြစ်၏ အမြစ်ကို အခြေခံသော | 1 | mula |
| akusalamūlamūlakā | အကုသိုလ်၏ အမြစ်၏ အမြစ်ကို အခြေခံသော | 2 | mula |
| akusalamūlamūlakāti | အကုသိုလ်၏ အမြစ်၏ အမြစ်ကို အခြေခံသော | 1 | mula |
| akusalamūlamūlā | အကုသိုလ်၏ အမြစ်၏ အမြစ် | 2 | mula |
| akusalamūlamūlāni | အကုသိုလ်၏ အမြစ်၏ အမြစ် | 1 | mula |
| akusalamūlamūlāti | အကုသိုလ်၏ အမြစ်၏ အမြစ် | 1 | mula |
| akusalamūlasahajātā dhammā | အကုသိုလ်၏ အမြစ်နှင့်အတူ ပေါ်ပေါက်သော သဘောတရား | 4 | compose |
| akusalamūlena | အကုသိုလ်၏ အမြစ် | 16 | mula |
| akusalamūlā | အကုသိုလ်၏ အမြစ် | 2 | mula |
| akusalamūlāni | အကုသိုလ်၏ အမြစ် | 5 | mula |
| akusalamūlāti | အကုသိုလ်၏ အမြစ် | 1 | mula |
| Akusalasamuṭṭhānaṃ | အကုသိုလ်မှ ဖြစ်ပေါ်လာသော | 6 | mula |
| akusalañca | အကုသိုလ် | 6 | base:stock |
| akusalaṃ | အကုသိုလ် | 6 | stock |
| akusalā | အကုသိုလ် | 13 | stock |
| Akusalā dhammā | အကုသိုလ် သဘောတရား | 2 | stock |
| akusalā dhammā | အကုသိုလ် သဘောတရား | 16 | stock |
| akusalāti | အကုသိုလ် | 12 | base:stock |
| anulomaokāso | နေရာအလိုက် အဟုတ်ပြ ပုံစံ | 8 | terms |
| anulomapuggalo | ပုဂ္ဂိုလ်အလိုက် အဟုတ်ပြ ပုံစံ | 8 | terms |
| anulomapuggalokāsā | ပုဂ္ဂိုလ်နှင့် နေရာအလိုက် အဟုတ်ပြ ပုံစံ | 8 | terms |
| anulomaṃ | အဟုတ်ပြ ပုံစံ | 8 | frame |
| arahato | ရဟန္တာ | 2 | frame |
| Arūpaṃ | ရုပ်မရှိသော ဘုံ | 4 | place |
| arūpaṃ | ရုပ်မရှိသော ဘုံ | 5 | place |
| Arūpe | ရုပ်မရှိသော ဘုံ | 8 | place |
| arūpe | ရုပ်မရှိသော ဘုံ | 3 | place |
| Arūpā | ရုပ်မရှိသော ဘုံ | 4 | place |
| Arūpānaṃ | ရုပ်မရှိသော ဘုံ၌ ရှိသူ | 8 | place |
| arūpānaṃ | ရုပ်မရှိသော ဘုံ၌ ရှိသူ | 4 | place |
| Asaññasattaṃ | အသညသတ် ဘုံ | 4 | place |
| asaññasattaṃ | အသညသတ် ဘုံ | 9 | place |
| Asaññasatte | အသညသတ် ဘုံ | 8 | place |
| asaññasattā | အသညသတ် ဘုံ | 2 | place |
| Asaññasattā | အသညသတ် ဘုံ | 4 | place |
| Asaññasattānaṃ | အသညသတ် | 6 | place |
| asaññasattānaṃ | အသညသတ် | 5 | place |
| Atītānāgatavāro | အတိတ်နှင့် အနာဂတ်အလိုက် ဖော်ပြချက် | 1 | terms |
| Avasesā | ကြွင်းကျန်သော | 24 | stock |
| avasesā | ကြွင်းကျန်သော | 3 | stock |
| Avasesā khandhā | ကြွင်းကျန်သော အစုအဝေး | 11 | compose |
| avasesā khandhā | ကြွင်းကျန်သော အစုအဝေး | 5 | compose |
| aññamaññamūlakā | အချင်းချင်း အမြစ်ကို အခြေခံသော | 8 | mula |
| aññamaññamūlakāni | အချင်းချင်း အမြစ်ကို အခြေခံသော | 4 | mula |
| aññamaññamūlakāti | အချင်းချင်း အမြစ်ကို အခြေခံသော | 4 | mula |
| aññamaññamūlamūlakā | အချင်းချင်း အမြစ်၏ အမြစ်ကို အခြေခံသော | 8 | mula |
| aññamaññamūlamūlakāni | အချင်းချင်း အမြစ်၏ အမြစ်ကို အခြေခံသော | 4 | mula |
| aññamaññamūlamūlakāti | အချင်းချင်း အမြစ်၏ အမြစ်ကို အခြေခံသော | 4 | mula |
| aññamaññamūlamūlā | အချင်းချင်း အမြစ်၏ အမြစ် | 8 | mula |
| aññamaññamūlamūlāni | အချင်းချင်း အမြစ်၏ အမြစ် | 4 | mula |
| aññamaññamūlamūlāti | အချင်းချင်း အမြစ်၏ အမြစ် | 4 | mula |
| aññamaññamūlā | အချင်းချင်း အမြစ် | 8 | mula |
| aññamaññamūlāni | အချင်းချင်း အမြစ် | 4 | mula |
| aññamaññamūlāti | အချင်းချင်း အမြစ် | 4 | mula |
| bhagavato | မြတ်စွာဘုရား | 2 | frame |
| cavantānaṃ | စုတေဆဲသူ | 20 | verb |
| Diṭṭhisaññā | အယူ ဖြစ်သော မှတ်သိမှု | 3 | stock |
| ekamūlakañceva | တူညီသော အမြစ်ကို အခြေခံသော | 3 | mula |
| ekamūlakaṃ | တူညီသော အမြစ်ကို အခြေခံသော | 4 | mula |
| ekamūlakā | တူညီသော အမြစ်ကို အခြေခံသော | 16 | mula |
| ekamūlakāni | တူညီသော အမြစ်ကို အခြေခံသော | 4 | mula |
| ekamūlakāti | တူညီသော အမြစ်ကို အခြေခံသော | 4 | mula |
| ekamūlamūlakañceva | တူညီသော အမြစ်၏ အမြစ်ကို အခြေခံသော | 3 | mula |
| ekamūlamūlakaṃ | တူညီသော အမြစ်၏ အမြစ်ကို အခြေခံသော | 4 | mula |
| ekamūlamūlakā | တူညီသော အမြစ်၏ အမြစ်ကို အခြေခံသော | 16 | mula |
| ekamūlamūlakāni | တူညီသော အမြစ်၏ အမြစ်ကို အခြေခံသော | 4 | mula |
| ekamūlamūlakāti | တူညီသော အမြစ်၏ အမြစ်ကို အခြေခံသော | 4 | mula |
| ekamūlamūlañceva | တူညီသော အမြစ်၏ အမြစ် ရှိသော | 3 | mula |
| ekamūlamūlaṃ | တူညီသော အမြစ်၏ အမြစ် ရှိသော | 4 | mula |
| ekamūlamūlā | တူညီသော အမြစ်၏ အမြစ် ရှိသော | 16 | mula |
| ekamūlamūlāni | တူညီသော အမြစ်၏ အမြစ် ရှိသော | 4 | mula |
| ekamūlamūlāti | တူညီသော အမြစ်၏ အမြစ် ရှိသော | 4 | mula |
| ekamūlañceva | တူညီသော အမြစ် ရှိသော | 3 | mula |
| ekamūlaṃ | တူညီသော အမြစ် ရှိသော | 4 | mula |
| ekamūlā | တူညီသော အမြစ် ရှိသော | 16 | mula |
| ekamūlāni | တူညီသော အမြစ် ရှိသော | 4 | mula |
| ekamūlāti | တူညီသော အမြစ် ရှိသော | 4 | mula |
| hetu | အကြောင်း | 2 | stock |
| Hetuvārādi | အကြောင်းအလိုက် ဖော်ပြချက် စသည် | 2 | frame |
| Itaresaṃ | အခြားသူ | 11 | stock |
| Khandhayamakaṃ | အစုအဝေးများကို အတွဲလိုက် မေးဖြေခြင်း | 1 | title |
| khandhe | အစုအဝေး | 5 | stock |
| khandho | အစုအဝေး | 23 | stock |
| khandhoti | အစုအဝေး | 12 | base:stock |
| khandhā | အစုအဝေး | 28 | stock |
| kusalahetū | ကုသိုလ်၏ အကြောင်း | 2 | mula |
| kusalahetūti | ကုသိုလ်၏ အကြောင်း | 1 | mula |
| kusalamūlakañceva | ကုသိုလ်၏ အမြစ်ကို အခြေခံသော | 1 | mula |
| kusalamūlakaṃ | ကုသိုလ်၏ အမြစ်ကို အခြေခံသော | 1 | mula |
| kusalamūlakā | ကုသိုလ်၏ အမြစ်ကို အခြေခံသော | 2 | mula |
| kusalamūlakāti | ကုသိုလ်၏ အမြစ်ကို အခြေခံသော | 1 | mula |
| kusalamūlamūlakañceva | ကုသိုလ်၏ အမြစ်၏ အမြစ်ကို အခြေခံသော | 1 | mula |
| kusalamūlamūlakaṃ | ကုသိုလ်၏ အမြစ်၏ အမြစ်ကို အခြေခံသော | 1 | mula |
| kusalamūlamūlakā | ကုသိုလ်၏ အမြစ်၏ အမြစ်ကို အခြေခံသော | 2 | mula |
| kusalamūlamūlakāti | ကုသိုလ်၏ အမြစ်၏ အမြစ်ကို အခြေခံသော | 1 | mula |
| kusalamūlamūlā | ကုသိုလ်၏ အမြစ်၏ အမြစ် | 2 | mula |
| kusalamūlamūlāni | ကုသိုလ်၏ အမြစ်၏ အမြစ် | 1 | mula |
| kusalamūlamūlāti | ကုသိုလ်၏ အမြစ်၏ အမြစ် | 1 | mula |
| kusalamūlasahajātā dhammā | ကုသိုလ်၏ အမြစ်နှင့်အတူ ပေါ်ပေါက်သော သဘောတရား | 4 | compose |
| kusalamūlena | ကုသိုလ်၏ အမြစ် | 16 | mula |
| kusalamūlā | ကုသိုလ်၏ အမြစ် | 2 | mula |
| kusalamūlāni | ကုသိုလ်၏ အမြစ် | 5 | mula |
| kusalamūlāti | ကုသိုလ်၏ အမြစ် | 1 | mula |
| kusalanidānā | ကုသိုလ်၏ ဇာစ်မြစ် | 2 | mula |
| kusalapaccayā | ကုသိုလ်၏ အထောက်အပံ့ | 2 | mula |
| kusalappabhavā | ကုသိုလ်၏ ပေါ်ထွက်ရာ | 2 | mula |
| kusalasambhavā | ကုသိုလ်၏ ဖြစ်တည်ရာ | 2 | mula |
| kusalasamudayā | ကုသိုလ်၏ ဖြစ်ပေါ်ခြင်း | 2 | mula |
| Kusalasamuṭṭhānaṃ | ကုသိုလ်မှ ဖြစ်ပေါ်လာသော | 6 | mula |
| kusalasamuṭṭhānā | ကုသိုလ်၏ ဖြစ်ပေါ်လာရာ | 2 | mula |
| kusalañca | ကုသိုလ် | 6 | base:stock |
| kusalaṃ | ကုသိုလ် | 6 | stock |
| kusalā | ကုသိုလ် | 13 | stock |
| kusalā dhammā | ကုသိုလ် သဘောတရား | 17 | stock |
| Kusalā dhammā | ကုသိုလ် သဘောတရား | 2 | stock |
| kusalāhārā | ကုသိုလ်၏ အာဟာရ | 2 | mula |
| kusalārammaṇā | ကုသိုလ်၏ အာရုံ | 2 | mula |
| kusalāti | ကုသိုလ် | 12 | base:stock |
| Mūlakanayo | အမြစ်ကို အခြေခံခြင်း ခွဲနည်း | 8 | terms |
| Mūlamūlakanayo | အမြစ်၏ အမြစ်ကို အခြေခံခြင်း ခွဲနည်း | 8 | terms |
| Mūlamūlanayo | အမြစ်၏ အမြစ် ခွဲနည်း | 8 | terms |
| Mūlanayo | အမြစ် ခွဲနည်း | 1 | terms |
| mūlanayo | အမြစ် ခွဲနည်း | 7 | terms |
| Mūlavāraniddeso | အမြစ်အလိုက် ဖော်ပြချက်၏ အကျယ် ဖော်ပြချက် | 1 | terms |
| Mūlavārauddeso | အမြစ်အလိုက် ဖော်ပြချက်၏ အကျဉ်း ဖော်ပြချက် | 1 | terms |
| Mūlavāro | အမြစ်အလိုက် ဖော်ပြချက် | 2 | terms |
| Mūlayamakapāḷi | အမြစ်များကို အတွဲလိုက် မေးဖြေခြင်း | 1 | title |
| Mūlayamakaṃ | အမြစ်များကို အတွဲလိုက် မေးဖြေခြင်း | 1 | title |
| Mūlaṃ | အမြစ် | 2 | stock |
| Mūlāni | အမြစ် | 16 | stock |
| Namo | ရှိခိုးသည် | 2 | frame |
| Natthi | မရှိသည် | 6 | frame |
| Niddesavāro | အကျယ် ဖော်ပြချက် | 1 | frame |
| niddeso | အကျယ် ဖော်ပြချက် | 2 | frame |
| nidānañca | ဇာစ်မြစ် | 2 | base:stock |
| nirodhavāro | ချုပ်ငြိမ်းခြင်းအလိုက် ဖော်ပြချက် | 1 | heading |
| nirujjhati | ချုပ်ငြိမ်းသည် | 6 | verb |
| nirujjhatīti | ချုပ်ငြိမ်းသည် | 6 | verb |
| nirujjhittha | ချုပ်ငြိမ်းခဲ့သည် | 6 | verb |
| nirujjhitthāti | ချုပ်ငြိမ်းခဲ့သည် | 6 | verb |
| nuppajjati | မဖြစ်ပေါ် | 15 | verb |
| nuppajjatīti | မဖြစ်ပေါ် | 15 | verb |
| nuppajjissati | မဖြစ်ပေါ်လိမ့်မည် | 15 | verb |
| nuppajjissatīti | မဖြစ်ပေါ်လိမ့်မည် | 15 | verb |
| nuppajjittha | မဖြစ်ပေါ်ခဲ့ | 15 | verb |
| nuppajjitthāti | မဖြစ်ပေါ်ခဲ့ | 15 | verb |
| nāmahetū | စိတ်ပိုင်း၏ အကြောင်း | 1 | mula |
| nāmamūlakañceva | စိတ်ပိုင်း၏ အမြစ်ကို အခြေခံသော | 1 | mula |
| nāmamūlakaṃ | စိတ်ပိုင်း၏ အမြစ်ကို အခြေခံသော | 1 | mula |
| nāmamūlakā | စိတ်ပိုင်း၏ အမြစ်ကို အခြေခံသော | 2 | mula |
| nāmamūlakāti | စိတ်ပိုင်း၏ အမြစ်ကို အခြေခံသော | 1 | mula |
| nāmamūlamūlakañceva | စိတ်ပိုင်း၏ အမြစ်၏ အမြစ်ကို အခြေခံသော | 1 | mula |
| nāmamūlamūlakaṃ | စိတ်ပိုင်း၏ အမြစ်၏ အမြစ်ကို အခြေခံသော | 1 | mula |
| nāmamūlamūlakā | စိတ်ပိုင်း၏ အမြစ်၏ အမြစ်ကို အခြေခံသော | 2 | mula |
| nāmamūlamūlakāti | စိတ်ပိုင်း၏ အမြစ်၏ အမြစ်ကို အခြေခံသော | 1 | mula |
| nāmamūlamūlā | စိတ်ပိုင်း၏ အမြစ်၏ အမြစ် | 2 | mula |
| nāmamūlamūlāni | စိတ်ပိုင်း၏ အမြစ်၏ အမြစ် | 1 | mula |
| nāmamūlamūlāti | စိတ်ပိုင်း၏ အမြစ်၏ အမြစ် | 1 | mula |
| nāmamūlasahajātā | စိတ်ပိုင်း၏ အမြစ်နှင့်အတူ ပေါ်ပေါက်သော | 4 | mula |
| nāmamūlena | စိတ်ပိုင်း၏ အမြစ် | 16 | mula |
| nāmamūlā | စိတ်ပိုင်း၏ အမြစ် | 2 | mula |
| nāmamūlāni | စိတ်ပိုင်း၏ အမြစ် | 5 | mula |
| nāmamūlāti | စိတ်ပိုင်း၏ အမြစ် | 1 | mula |
| nāmanidānā | စိတ်ပိုင်း၏ ဇာစ်မြစ် | 1 | mula |
| nāmapaccayā | စိတ်ပိုင်း၏ အထောက်အပံ့ | 1 | mula |
| nāmappabhavā | စိတ်ပိုင်း၏ ပေါ်ထွက်ရာ | 1 | mula |
| nāmasambhavā | စိတ်ပိုင်း၏ ဖြစ်တည်ရာ | 1 | mula |
| nāmasamudayā | စိတ်ပိုင်း၏ ဖြစ်ပေါ်ခြင်း | 1 | mula |
| Nāmasamuṭṭhānaṃ | စိတ်ပိုင်းမှ ဖြစ်ပေါ်လာသော | 6 | mula |
| nāmasamuṭṭhānā | စိတ်ပိုင်း၏ ဖြစ်ပေါ်လာရာ | 1 | mula |
| nāmañca | စိတ်ပိုင်း | 6 | base:stock |
| nāmaṃ | စိတ်ပိုင်း | 6 | stock |
| Nāmā | စိတ်ပိုင်း | 2 | stock |
| nāmā | စိတ်ပိုင်း | 20 | stock |
| nāmāhārā | စိတ်ပိုင်း၏ အာဟာရ | 1 | mula |
| nāmārammaṇā | စိတ်ပိုင်း၏ အာရုံ | 1 | mula |
| nāmāti | စိတ်ပိုင်း | 12 | base:stock |
| pabhavena | ပေါ်ထွက်ရာ | 2 | stock |
| paccanīkaokāso | နေရာအလိုက် အငြင်းပြ ပုံစံ | 8 | terms |
| paccanīkapuggalo | ပုဂ္ဂိုလ်အလိုက် အငြင်းပြ ပုံစံ | 8 | terms |
| paccanīkapuggalokāsā | ပုဂ္ဂိုလ်နှင့် နေရာအလိုက် အငြင်းပြ ပုံစံ | 8 | terms |
| paccanīkaṃ | အငြင်းပြ ပုံစံ | 8 | frame |
| paccayo | အထောက်အပံ့ | 2 | stock |
| Pacchimabhavikānaṃ | နောက်ဆုံး ဘဝ ရှိသူ | 12 | stock |
| pacchimabhavikānaṃ | နောက်ဆုံး ဘဝ ရှိသူ | 4 | stock |
| Padasodhanamūlacakkavāro | စကားလုံးကို စိစစ်ခြင်းကို အခြေခံ၍ လှည့်ပတ်ခြင်း ဖော်ပြချက် | 2 | terms |
| Padasodhanavāro | စကားလုံးကို စိစစ်ခြင်း ဖော်ပြချက် | 2 | terms |
| parinibbantānaṃ | ပရိနိဗ္ဗာန် ပြုဆဲသူ | 4 | verb |
| Parinibbantānaṃ | ပရိနိဗ္ဗာန် ပြုဆဲသူ | 2 | verb |
| parinibbāyissanti | ပရိနိဗ္ဗာန် ပြုမည့် | 2 | verb |
| Pavatti | ဖြစ်ပျက်ခြင်း | 1 | frame |
| Pavattivāro | ဖြစ်ပျက်ခြင်းအလိုက် ဖော်ပြချက် | 1 | heading |
| Pañcakkhandhā | အစုအဝေး ငါးပါး | 1 | stock |
| Pañcavokāraṃ | အစုအဝေး ငါးပါး ရှိသော ဘဝ | 3 | place |
| pañcavokāraṃ | အစုအဝေး ငါးပါး ရှိသော ဘဝ | 9 | place |
| Pañcavokāre | အစုအဝေး ငါးပါး ရှိသော ဘဝ | 12 | place |
| Pañcavokārā | အစုအဝေး ငါးပါး ရှိသော ဘဝ | 6 | place |
| pañcavokārā | အစုအဝေး ငါးပါး ရှိသော ဘဝ | 4 | place |
| Pañcavokārānaṃ | အစုအဝေး ငါးပါး ရှိသော ဘဝ၌ ရှိသူ | 3 | place |
| pañcavokārānaṃ | အစုအဝေး ငါးပါး ရှိသော ဘဝ၌ ရှိသူ | 1 | place |
| pañcavokārānaṃ | အစုအဝေး ငါးပါး ရှိသော ဘဝ၌ ရှိသော | 1 | place |
| Paṇṇattiniddesavāro | သတ်မှတ်ချက်အလိုက် ဖော်ပြချက်၏ အကျယ် ဖော်ပြချက် | 1 | terms |
| Paṇṇattiuddesavāro | သတ်မှတ်ချက်အလိုက် ဖော်ပြချက်၏ အကျဉ်း ဖော်ပြချက် | 1 | terms |
| Paṇṇattivāraniddesa | သတ်မှတ်ချက်အလိုက် ဖော်ပြချက်၏ အကျယ် ဖော်ပြချက် | 1 | terms |
| Paṇṇattivāro | သတ်မှတ်ချက်အလိုက် ဖော်ပြချက် | 1 | terms |
| rūpakkhandhañca | ရုပ် အစုအဝေး | 1 | khandha |
| rūpakkhandho | ရုပ် အစုအဝေး | 64 | khandha |
| Rūpakkhandho | ရုပ် အစုအဝေး | 9 | khandha |
| rūpakkhandhoti | ရုပ် အစုအဝေး | 22 | khandha |
| rūpanti | ရုပ် | 2 | base:stock |
| Rūpañca | ရုပ် | 3 | base:stock |
| rūpañceva | ရုပ် | 2 | base:stock |
| rūpaṃ | ရုပ် | 42 | stock |
| Sahetukaṃ | အမြစ် ရှိသော | 18 | stock |
| sambhavo | ဖြစ်တည်ရာ | 2 | stock |
| sammāsambuddhassa | အမှန်ကို ကိုယ်တိုင် အပြည့်အဝ သိမြင်တော်မူသော ဘုရားရှင် | 2 | frame |
| samudayena | ဖြစ်ပေါ်ခြင်း | 2 | stock |
| Samuṭṭhānāhārārammaṇā | ဖြစ်ပေါ်လာရာ အာဟာရ အာရုံ | 2 | stock |
| Saññañca | မှတ်သိမှု | 3 | base:stock |
| Saññaṃ | မှတ်သိမှု | 2 | stock |
| saññā | မှတ်သိမှု | 24 | stock |
| saññākkhandhañca | မှတ်သိမှု အစုအဝေး | 1 | khandha |
| saññākkhandho | မှတ်သိမှု အစုအဝေး | 34 | khandha |
| Saññākkhandho | မှတ်သိမှု အစုအဝေး | 9 | khandha |
| saññākkhandhoti | မှတ်သိမှု အစုအဝေး | 22 | khandha |
| saññāti | မှတ်သိမှု | 2 | base:stock |
| saṅkhārakkhandhañca | ပြုပြင်ဖန်တီးမှု အစုအဝေး | 1 | khandha |
| Saṅkhārakkhandhaṃ | ပြုပြင်ဖန်တီးမှု အစုအဝေး | 3 | khandha |
| saṅkhārakkhandho | ပြုပြင်ဖန်တီးမှု အစုအဝေး | 16 | khandha |
| Saṅkhārakkhandho | ပြုပြင်ဖန်တီးမှု အစုအဝေး | 9 | khandha |
| saṅkhārakkhandhoti | ပြုပြင်ဖန်တီးမှု အစုအဝေး | 22 | khandha |
| Saṅkhāre | ပြုပြင်ဖန်တီးမှု | 1 | stock |
| saṅkhārā | ပြုပြင်ဖန်တီးမှု | 24 | stock |
| saṅkhārāti | ပြုပြင်ဖန်တီးမှု | 2 | base:stock |
| Suddhakhandhamūlacakkavāro | ရိုးရိုး အစုအဝေးကို အခြေခံ၍ လှည့်ပတ်ခြင်း ဖော်ပြချက် | 2 | terms |
| Suddhakhandhavāro | ရိုးရိုး အစုအဝေး ဖော်ပြချက် | 2 | terms |
| Suddhāvāsaṃ | သုဒ္ဓါဝါသ ဘုံ | 4 | place |
| Suddhāvāse | သုဒ္ဓါဝါသ ဘုံ | 2 | place |
| Suddhāvāsānaṃ | သုဒ္ဓါဝါသ ဘုံ၌ ရှိသူ | 4 | place |
| Uddesavāro | အကျဉ်း ဖော်ပြချက် | 1 | frame |
| uddeso | အကျဉ်း ဖော်ပြချက် | 2 | frame |
| upapajjantānaṃ | ပြန်လည် ဖြစ်ပေါ်ဆဲ | 1 | verb |
| upapajjantānaṃ | ပြန်လည် ဖြစ်ပေါ်ဆဲသူ | 19 | verb |
| upapajjitvā | ပြန်လည် ဖြစ်ပေါ်၍ | 2 | verb |
| uppajjanti | ဖြစ်ပေါ်သည် | 16 | verb |
| uppajjati | ဖြစ်ပေါ်သည် | 15 | verb |
| Uppajjati | ဖြစ်ပေါ်သည် | 3 | verb |
| uppajjatīti | ဖြစ်ပေါ်သည် | 15 | verb |
| uppajjissati | ဖြစ်ပေါ်လိမ့်မည် | 15 | verb |
| Uppajjissati | ဖြစ်ပေါ်လိမ့်မည် | 3 | verb |
| uppajjissatīti | ဖြစ်ပေါ်လိမ့်မည် | 15 | verb |
| uppajjittha | ဖြစ်ပေါ်ခဲ့သည် | 15 | verb |
| Uppajjittha | ဖြစ်ပေါ်ခဲ့သည် | 7 | verb |
| uppajjitthāti | ဖြစ်ပေါ်ခဲ့သည် | 15 | verb |
| uppādavāro | ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက် | 1 | heading |
| Uppādavāro | ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက် | 1 | heading |
| Vedanañca | ခံစားမှု | 2 | base:stock |
| Vedanaṃ | ခံစားမှု | 2 | stock |
| vedanā | ခံစားမှု | 24 | stock |
| vedanākkhandho | ခံစားမှု အစုအဝေး | 81 | khandha |
| Vedanākkhandho | ခံစားမှု အစုအဝေး | 9 | khandha |
| vedanākkhandhoti | ခံစားမှု အစုအဝေး | 22 | khandha |
| vedanāti | ခံစားမှု | 2 | base:stock |
| viññāṇakkhandho | သိစိတ် အစုအဝေး | 15 | khandha |
| Viññāṇakkhandho | သိစိတ် အစုအဝေး | 9 | khandha |
| viññāṇakkhandhoti | သိစိတ် အစုအဝေး | 22 | khandha |
| viññāṇanti | သိစိတ် | 2 | base:stock |
| Viññāṇañca | သိစိတ် | 2 | base:stock |
| viññāṇaṃ | သိစိတ် | 24 | stock |
| Yamakapāḷi | အတွဲလိုက် မေးဖြေခြင်း | 1 | frame |
| ṭhapetvā | ချန်ထား၍ | 8 | stock |
