"""The prose of map-table.md (imported by map_sample.py --table; no work at import)."""

HEAD = """# pi-6 Burmese keyword mapping, PHASE 1: rules and review table (Yamaka «အတွဲလိုက် မေးဖြေခြင်း»: preamble, 1-mulayamaka, 2-01-khandhayamaka)

Written by `map_sample.py --table` with the shared module `map6_rules.py` (imported by the three phase-2 agents; no
work at import). Burmese from the FINAL text of this track only (`AI_translation/burmese/pi-6-burmese-plain-zeroshot_split_chapters`),
`my6-zeroshot-terms.md` and the final pi-1 … pi-5 Burmese mappings; no other Burmese source. The sample chapters need
no chapter table and no per-segment override: every value comes from the module.

"""

RULES = """## Rules used (binding, unchanged)

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

"""
