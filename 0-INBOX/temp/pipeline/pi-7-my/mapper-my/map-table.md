# pi-7 Burmese keyword mapping, PHASE 1: rules and review table (Paṭṭhāna «အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ»: preamble, 1-00-paccaya, 1-02-vedanattika)

Written by `map_sample.py --table` with the shared module `map7_rules.py` (imported by the phase-2 agents; no work at
import). Burmese from the FINAL text of this track only (`AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters`),
its term list `my7-zeroshot-terms.md`, the term tables of its generators (`make_*.py`, `my7_formulas.py`: read as text,
never imported) and the final pi-1 … pi-6 Burmese mappings; no other Burmese source. The sample chapters need no
chapter table and one per-segment override (^7-3-53 saddhāpañcamakesu, a keyword of one segment of the book).

## Numbers

- `preamble.mapped.md`: 3 lines, keyword preservation `bad []`, presence failures 0, «, » / «၊» / « / » in a value 0, (no direct equivalent) 0, chunks matched by an ending rule 4.
- `1-00-paccaya.mapped.md`: 66 lines, keyword preservation `bad []`, presence failures 0, «, » / «၊» / « / » in a value 0, (no direct equivalent) 0, chunks matched by an ending rule 219.
- `1-02-vedanattika.mapped.md`: 228 lines, keyword preservation `bad []`, presence failures 0, «, » / «၊» / « / » in a value 0, (no direct equivalent) 3, chunks matched by an ending rule 27.
- Keyword uses 3656: **taken unchanged from pi-1 … pi-6** (the same value as a pi-1 … pi-6 mapping of that keyword or of its base form, R1) **1415** (in 194 keywords); a keyword that pi-1 … pi-6 never mapped 1843; a value different from pi-1 … pi-6 398 (in 42 keyword / value pairs, listed below with the reason).
- Source of the values (uses): cond 1544, pi-2 467, terms 458, stock 423, verb 233, frame 174, order 76, lex 73, count 58, base 52, headlex 30, pi-5 23, vara 21, term 17, pi-4 2, pi-3 2, title 1, pi-6 1, ctx 1 (frame / stock = the module tables; cond / vara / order / count / samutthana / title = the Paṭṭhāna families T1-T6, T12; headlex = the heading lexicon T9; verb = T10; terms = my7-zeroshot-terms (T11); lex = LEXW (T11); pi-N = a pi-N value; base = R1 on a table value; term = T7 / T8 / T12 / T13; ctx = the one per-segment override).

## Rules used (binding, unchanged)

The value is the word or phrase of THAT segment's Burmese (the FINAL pi-7 text) that carries the keyword, in the
dictionary form of the approved Burmese mappings:

- **pi-1** rules 1-11 (approved 2026-11-17): nouns without final case particles / plural markers (rule 1; inner
  particles stay: «အကြောင်းများ၏ အကျယ် ဖော်ပြချက်», «ထိုအရာနှင့် ယှဉ်တွဲသော»); a noun predicated = the noun (rule 2);
  adjectives / participles «…သော», gerundives «…မည့်» (rule 3: vitthāretabbaṃ «အကျယ် ချဲ့ရမည့်»); verbs «…သည်»
  (rule 4); «X dhammā» = «X သဘောတရား» (rule 5); sentence-final material and the «၊» inside a term dropped (rule 6:
  abyākata «ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော»); titles and headings whole (rule 7); particles (rule 9: ca, pi,
  ti, siyā = (no direct equivalent) where they stand alone); « … » for discontinuous parts, no « / », no «, » / «၊» in a
  value (rule 10); sense by context, one sense per segment (rule 11). The agreed later pi-1 rules: absolutives keep
  «…၍» (paṭicca «မှီ၍», ārabbha «အာရုံပြု၍»); counts keep the text's classifier.
- **pi-2** N1-N11 and the harmonise decisions: the ablative of cause keeps «ကြောင့်» (pi-2 avijjāpaccayā «အမှန်ကို
  မသိမှုကြောင့်»: here Xpaccayā «Nဟူသော အကြောင်းကြောင့်»); one Burmese word for two compound members: one member gets it,
  the other (no direct equivalent) (here karoti / katvā after an act compound).
- **pi-3** M1-M9 (the « … » gap; the presence endings of M7); **pi-4** P1-P8 (agent nouns «…သူ» P6: vuṭṭhahantassa
  «ထမြောက်နေသူ», vippaṭisārissa «နောင်တ ရသူ»; the presence endings P3; A2 «X၍» against «မXဘဲ»).
- **pi-5** Q1-Q8 (Q1 presence endings «…သလော / …ပါ / …ပြီး»: the pucchāvāra «ဖြစ်ပေါ်နိုင်သလော»; Q4 the «လည်း» of ca is
  not part of a keyword; Q5 negated verbs «မ + verb» without «သည်»), S1 (stem fallback, with the pi-7 guard M1 below).
- **pi-6** R1 («-ti» / «ca» / «pi» forms = the base form's value: Hetupaccayoti, taṃsampayuttakānañca, kusalañca,
  tikañca), R2 (verbs in every tense and polarity), R6 (headings), R7 (the «လည်း» gap inside one value), R8 (-samaṅgī
  «Xနှင့် ပြည့်စုံသူ», moments «… ခဏ» without «၌»), R9; the five phase-3 mechanics (the literal tier needs phrase_ok,
  base_forms skips a finite «-anti», …, the «Xပြီး မဟုတ်» ending); the pi-6 orders anuloma / paccanīka «အဟုတ်ပြ / အငြင်းပြ
  ပုံစံ» (reused by the pi-7 text, notes-sample).
- **pi-1 … pi-6 values**: a keyword the module tables and families do not settle is looked up in the FINAL pi-1 … pi-6
  mappings (`AI_translation/burmese/pi-{1,…,6}-keywords-by-reference-pali-burmese-plain.md`; order pi-2, pi-3, pi-4,
  pi-5, pi-6, pi-1): the most frequent value the segment has as a phrase, then one whose chunks are all literal and
  together, then one present by an ending rule. A pi-1 … pi-6 value that stands in the segment only inside another
  word or another phrase is not taken (it is not the keyword's word there; such cases are listed below).

## How the module is built (`map7_rules.py`)

Lookup per keyword (single-word keywords: the 75 keyword files have no multiword keyword): CTX[segment] → chapter table
→ FRAME → STOCK (a book-wide value is taken only where the segment has it) → the Paṭṭhāna families (T1-T6: conditions,
vāras, orders, counts, -samuṭṭhāna, titles) → the heading lexicon (T9) → verbs (T10) → the same for the base forms (R1)
→ pi-7 terms (T11) → a pi-1 … pi-6 value (contiguous) → LEXW (T11) → a pi-1 … pi-6 value (other tiers) → the term
family (T7 generator terms and case siblings, T8 na-X / no-X, T13 cluster dyads, T12 head compounds) → the heading rule
(R6) → the stem fallback (S1 with M1). Every family value is a list of candidates checked against the segment
(`pick_phrase`): the text's own form wins. A value «@name» calls a context function (FUNCS: f_rupam, f_paccayo,
f_natthi, f_karoti); a tuple = the first value the segment has (alt). Every value then gets R7 and loses a list comma
(rule 6). `Mapper(chapter_tables=…, ctx=…, stem=make_stem([FRAME, STOCK, LEXW, …]))` is the entry point,
`verify_file(ch)` the verifier, `frame_coverage.py` the whole-book check. Lookups are cached per segment.

## NEW rules (beyond pi-1 … pi-6), for review

T1. **The 24 condition names** (my7_formulas CONDS; notes-sample «The 24 names»): the bare name N (ghaṭanā lists and
    hyphen compounds: «Hetu-sahajāta-…-avigatanti tīṇi» «အမြစ်၊ အတူ ပေါ်ပေါက်ခြင်း၊ … ဟူသော ပေါင်းစပ်ချက်၌ သုံးခု»:
    sahajāta = အတူ ပေါ်ပေါက်ခြင်း); the name «Nဟူသော အကြောင်း» for Xpaccayo / Xpaccayoti / Xpaccayopi (R1, Q4: the
    «ကိုလည်း» goes) and for the instrumental Xpaccayena (pi-5 hetupaccayena «အမြစ်ဟူသော အကြောင်း», binding: the «ဖြင့်»
    goes, rule 1); the negative «Nဟူသော အကြောင်း မဟုတ်ခြင်း» (Nahetupaccayo); paccayo itself «အကြောင်း» (pi-5).
T2. **Cases of the counting frames**: the ablative Xpaccayā «Nဟူသော အကြောင်းကြောင့်» (pi-2: the cause marker «ကြောင့်»
    is the keyword's meaning and stays), naXpaccayā «Nဟူသော အကြောင်းကြောင့် မဟုတ်» (pi-1 rule 9 «… မဟုတ်»; the adverbial
    «ဘဲ» of «မဟုတ်ဘဲ» goes, rule 6); the counting locative Xe / Xyā «Nဟူသော အကြောင်း» (rule 1: «၌» goes), naXe / noXe
    «Nဟူသော အကြောင်း မဟုတ်ခြင်း». A locative that is not a condition in the segment (kamme, magge, jhāne in a deed)
    falls through to its plain value (one sense per segment: the condition wins where the segment has it).
T3. **«Xpaccayena paccayo»**: Xpaccayena = the name (T1), paccayo «အကြောင်း» (f_paccayo); the text's «ဖြင့် … ဖြစ်သည်»
    are case and sentence-final material.
T4. **Hyphen-compound parts take the compound's case** (compound_form): «Napacchājāta-naāsevanapaccayā» in a heading
    names the conditions (Napacchājāta «နောက်မှ ဖြစ်ပေါ်ခြင်းဟူသော အကြောင်း မဟုတ်ခြင်း»), before «-paccayā» in a body
    line it is the ablative («naārammaṇa-…-noatthipaccayā» naārammaṇa «အာရုံဟူသော အကြောင်းကြောင့် မဟုတ်»), in a ghaṭanā
    list the bare name; sa-X «(saupanissayaṃ)» «အားကြီးသော အမှီဟူသော အကြောင်း ပါဝင်သော», «Saindriya-maggaghaṭanā»
    Saindriya «စွမ်းရည်ဟူသော အကြောင်း … ပါဝင်သော» (rule 10: the text closes the compound with one «ပါဝင်သော»).
T5. **Vāras and orders** (my7-zeroshot-terms §2): a vāra in any case «Xအလိုက် ဖော်ပြချက်» (pi-2 / pi-6; rule 1 / Q4: the
    case particle and the «လည်း» of -pi go), -ādi «… စသည်», -sadisa «…နှင့် တူသည်» (rule 4; the text's «တူကြသည်» by the
    ending rule; its adverbial «…နှင့် တူအောင်» before an imperative); anuloma / paccanīya and their compounds with
    paccaya- / dhamma- (Paccayānulomaṃ «အကြောင်း အဟုတ်ပြ ပုံစံ», Dhammānulome «သဘောတရား အဟုတ်ပြ ပုံစံ»), -gaṇanā «…၏
    ရေတွက်ချက်», -mātikā «…၏ ခေါင်းစဉ်စာရင်း».
T6. **Counts**: an answer count = the text's number word + «ခု» (pi-1 decision 5: the text's classifier; Pāli
    compound numbers parsed: ekavīsa «နှစ်ဆယ့်တစ်ခု», sattatiṃsa «သုံးဆယ့်ခုနစ်ခု»), khandha / mahābhūta counts «… ပါး»;
    counting groups «Nမျိုးတွဲ» (pi-1 tika / duka); counted mūlakas «အကြောင်း Nခုကို အခြေခံခြင်း»; X-paṭṭhānaṃ titles
    «Xတို့၏ အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ».
T7. **Term qualifiers in any case**: the value of a triad / dyad term does not depend on its case (rule 1 / rule 3):
    the term tables of the pi-7 generators (the stems «upādinnupādāniy», «sanidassanasappaṭigh» … with a case ending;
    read as text), the pi-1 … pi-6 value of a case sibling (savitakkasavicāro ↔ -ā ↔ -aṃ; a-, i- and u-stems; pi-1's
    spelling «upādiṇṇ» for the pi-7 «upādinn»); the stacked qualifiers «A၊ B N» of the dukatika / tikaduka (harmonise
    H6) give each keyword its own attributive without the «၊» (rule 6).
T8. **na-X / no-X terms** (harmonise H21, the text's rule): na + an attributive «Xသော» = «Xသည် မဟုတ်သော» (naabyākato
    «ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သည် မဟုတ်သော»), na + a noun term «X» = «X မဟုတ်သော» (nakusalo «ကုသိုလ်
    မဟုတ်သော», nahetuṃ «အမြစ် မဟုတ်သော», nosaññojanaṃ «နှောင်ကြိုး မဟုတ်သော»).
T9. **The heading lexicon**: every heading line of the book whose Pāli and Burmese have the same number of parts gives
    its parts as a lexicon (rule 7: a heading keyword that is a whole heading part takes the whole part, in dictionary
    form: Vedanāttikaṃ «ခံစားမှု သုံးမျိုးတွဲ», Suddhaṃ «ရိုးရိုး», Paccanīyuddhāro «အငြင်းပြ ပုံစံအတွက် ထုတ်နုတ်ချက်»);
    the same keyword in a note takes the same value where the segment has it.
T10. **Verbs of the frames**: uppajjati / uppajjanti «ဖြစ်ပေါ်သည်» (pi-1 … pi-6; the plural «ကြ» by the ending rule);
    the optative uppajjeyya / uppajjeyyuṃ of «Siyā … uppajjeyya» = the text's potential «ဖြစ်ပေါ်နိုင်သည်» (Q1 ending
    «သလော»; siyā has no word: rule 9).
T11. **The pi-7 phrase lexicon word by word** (LEXW, reviewed; my7 LEX): each Pāli word of «dānaṃ datvā», «sīlaṃ
    samādiyitvā», «mātaraṃ jīvitā voropeti», «pariyiṭṭhimūlakaṃ dukkhaṃ paccanubhoti» … gets the part of the text's phrase
    that carries it; an act compound whose Burmese carries the verb («uposathakammaṃ» «ဥပုသ်ကို စောင့်ထိန်းသည်»,
    «gāmaghātaṃ» «ရွာကို ဖျက်ဆီး၍ လုယက်သည်», «ekāgārikaṃ») takes the verb, and karoti / katvā after it is (no direct
    equivalent) (pi-2 harmonise; f_karoti: only where every karoti / katvā of the segment follows such a compound);
    the kamma kinds sahajātā / nānākkhaṇikā = the adjective (the label's «ကံ» is the frame's head noun, harmonise H7).
T12. **Compound terms with a known head**: «X-samuṭṭhāna» «Xမှ ဖြစ်ပေါ်လာသော» (pi-2 cittasamuṭṭhāna; utu «ရာသီဥတု»,
    āhāra «အာဟာရ»; the text's supplied «ရုပ်» is not part of the keyword, harmonise H8 item 4); «X-adhipati» «X
    အကြီးအမှူး» (ārammaṇādhipati «အာရုံ အကြီးအမှူး», sampayuttādhipati «ယှဉ်တွဲသော အကြီးအမှူး»; the triad term
    maggādhipati «မဂ်ကို အကြီးအမှူးပြုသော»); «X-cittasamaṅgissa» «X စိတ်နှင့် ပြည့်စုံသူ» (pi-6 R8, pi-4 P6); «X-purejātaṃ»
    «X ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်း» (vatthupurejātaṃ «မှီရာ ဝတ္ထု ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်း»); «X-sahagata» «Xနှင့်အတူ ဖြစ်သော»
    (pi-1).
T13. **The cluster dyads of the gocchakas** (burmese-style cluster names; pi-1 rule 3): the item «N ဖြစ်သော»,
    X-sampayutta «Nနှင့် ယှဉ်တွဲသော», X-vippayutta «Nနှင့် ကင်းကွာသော», X-iya / sa-X «N၏ အာရုံ ဖြစ်နိုင်သော» (saññojano
    «နှောင်ကြိုး ဖြစ်သော», sāsavo «စိတ်အစွန်းအထင်း၏ အာရုံ ဖြစ်နိုင်သော»).
M1. **S1 guard** (mechanic): a stem donor's value must have the keyword's grammatical shape: a verb value «…သည် / …၍»
    never goes to a noun keyword (the dry run had nibbānaṃ «ဖြစ်ပေါ်သည်» from nibbattati), a finite verb keyword gets
    «…သည်» (passati «မြင်သည်» from the participle «မြင်သော»), an absolutive «…၍» (bhinditvā «ဖြိုခွဲ၍»), a gerundive
    «…ရမည့်»; otherwise no value.
M2. **A book-wide table value is taken only where the segment has it** (FRAME / STOCK): otherwise the chain goes on
    (a CTX or chapter-table value is final).


## Values different from pi-1 … pi-6 (same keyword)

| keyword = pi-7 value | pi-1 … pi-6 value (uses here) | reason |
|---|---|---|
| uppajjeyya = ဖြစ်ပေါ်နိုင်သည် | ဖြစ်ပေါ်သည် (113) | T10: the optative of the pucchāvāra «Siyā … uppajjeyya» is the text's potential «ဖြစ်ပေါ်နိုင်သလော» (dictionary «ဖြစ်ပေါ်နိုင်သည်», Q1 ending «သလော»); the pi-2 / pi-5 «ဖြစ်ပေါ်သည်» is not in the segment |
| uppajjeyyuṃ = ဖြစ်ပေါ်နိုင်သည် | ဖြစ်ပေါ်သည် (95) | as uppajjeyya (the plural «ကြ» by the ending rule, rule 4) |
| vigate = ပျောက်ကွယ်ခြင်းဟူသော အကြောင်း | ကင်းသွားသော (18) | T1 / T2: the condition in the frame of the Paṭṭhāna (counting locative «Nဟူသော အကြောင်း၌ K», bare ghaṭanā name, ablative «…ကြောင့်»); the pi-1 … pi-6 value is the plain noun / verb of another kind of segment and stands in the pi-7 segment only as a part of the condition name |
| indriye = စွမ်းရည်ဟူသော အကြောင်း | စွမ်းရည် (18) | T1 / T2: the condition in the frame of the Paṭṭhāna (counting locative «Nဟူသော အကြောင်း၌ K», bare ghaṭanā name, ablative «…ကြောင့်»); the pi-1 … pi-6 value is the plain noun / verb of another kind of segment and stands in the pi-7 segment only as a part of the condition name |
| ārammaṇe = အာရုံဟူသော အကြောင်း | အာရုံ (17) | T1 / T2: the condition in the frame of the Paṭṭhāna (counting locative «Nဟူသော အကြောင်း၌ K», bare ghaṭanā name, ablative «…ကြောင့်»); the pi-1 … pi-6 value is the plain noun / verb of another kind of segment and stands in the pi-7 segment only as a part of the condition name |
| āhāre = အာဟာရဟူသော အကြောင်း | အာဟာရ (17) | T1 / T2: the condition in the frame of the Paṭṭhāna (counting locative «Nဟူသော အကြောင်း၌ K», bare ghaṭanā name, ablative «…ကြောင့်»); the pi-1 … pi-6 value is the plain noun / verb of another kind of segment and stands in the pi-7 segment only as a part of the condition name |
| magge = မဂ်ဟူသော အကြောင်း | မဂ် (15) | T1 / T2: the condition in the frame of the Paṭṭhāna (counting locative «Nဟူသော အကြောင်း၌ K», bare ghaṭanā name, ablative «…ကြောင့်»); the pi-1 … pi-6 value is the plain noun / verb of another kind of segment and stands in the pi-7 segment only as a part of the condition name |
| aññamañña = အချင်းချင်း ထောက်ပံ့ခြင်း | အချင်းချင်း အကြောင်းဖြစ်ခြင်း (13) | T1 / T2: the condition in the frame of the Paṭṭhāna (counting locative «Nဟူသော အကြောင်း၌ K», bare ghaṭanā name, ablative «…ကြောင့်»); the pi-1 … pi-6 value is the plain noun / verb of another kind of segment and stands in the pi-7 segment only as a part of the condition name |
| atthi = ရှိခြင်း | ရှိသည် (13) | T1 / T2: the condition in the frame of the Paṭṭhāna (counting locative «Nဟူသော အကြောင်း၌ K», bare ghaṭanā name, ablative «…ကြောင့်»); the pi-1 … pi-6 value is the plain noun / verb of another kind of segment and stands in the pi-7 segment only as a part of the condition name |
| uppādeti = ဖြစ်စေသည် | ဖြစ်ပေါ်မှု (9) | the text's «… ကို ဖြစ်စေသည်» (my7 LEX); the pi-5 «ဖြစ်ပေါ်မှု» (a noun) is not in the segment |
| assādeti = သာယာ | သာယာသည် (8) | T11: the text joins the two verbs «သာယာ နှစ်သက်သည်» with one «သည်»; the pi-5 «သာယာသည်» is not in the segment, the bare «သာယာ» is (unclear point U1) |
| kusalākusalaṃ = ကုသိုလ်နှင့် အကုသိုလ် | ကုသိုလ် အကုသိုလ် (6) | the text's «ကုသိုလ်နှင့် အကုသိုလ် ကံ» (my7 FIXED, pi-5 kusalākusale); the pi-1 «ကုသိုလ် အကုသိုလ်» is not in the segment as a phrase |
| vippayutte = ကင်းကွာခြင်းဟူသော အကြောင်း | ကင်းကွာသော (4) | T1 / T2: the condition in the frame of the Paṭṭhāna (counting locative «Nဟူသော အကြောင်း၌ K», bare ghaṭanā name, ablative «…ကြောင့်»); the pi-1 … pi-6 value is the plain noun / verb of another kind of segment and stands in the pi-7 segment only as a part of the condition name |
| datvā = ပြု၍ | ပေးပြီးနောက် (4) | T11: «dānaṃ datvā» = «ပေးလှူခြင်းကို ပြု၍»: the verb is «ပြု၍»; the pi-4 «ပေးပြီးနောက်» is not in the segment |
| paccavekkhati = ပြန်လည် ဆင်ခြင်သည် | ဆင်ခြင်သည် (4) | the pi-7 text's word «ပြန်လည် ဆင်ခြင်» (my7 LEX, the prefix paṭi- «ပြန်လည်»); the pi-2 / pi-5 «ဆင်ခြင်သည်» is only its second half |
| natthi = မရှိခြင်း | မရှိသည် (4) | T1 / T2: the condition in the frame of the Paṭṭhāna (counting locative «Nဟူသော အကြောင်း၌ K», bare ghaṭanā name, ablative «…ကြောင့်»); the pi-1 … pi-6 value is the plain noun / verb of another kind of segment and stands in the pi-7 segment only as a part of the condition name; in a note the verb «မရှိ» (Q5) |
| Ekamūlakaṃ = အကြောင်း တစ်ခုကို အခြေခံခြင်း | တစ်မျိုးတွဲကို အခြေခံသော (3) | T6: the counted mūlaka «အကြောင်း တစ်ခုကို အခြေခံခြင်း» (my7-zeroshot-terms §2); the pi-3 «တစ်မျိုးတွဲကို အခြေခံသော» (Dhātukathā) is not in the segment |
| vipassati = ထိုးထွင်း၍ ရှုသည် | ကြည့်ရှုသည် (3) | the text's «ထိုးထွင်း၍ ရှုသည်» (my7 LEX); the pi-5 «ကြည့်ရှုသည်» is not in the segment |
| deti = ပြုသည် | ပေးသည် (3) | T11: «dānaṃ deti» = «ပေးလှူခြင်းကို ပြုသည်»; the pi-4 «ပေးသည်» stands in the segment only inside «မပေးသည်ကို» (adinnaṃ), another phrase |
| anantara = ချက်ချင်း နောက်၌ ဖြစ်စေခြင်း | ချက်ချင်း နောက်၌ ဖြစ်စေသော (3) | T1 / T2: the condition in the frame of the Paṭṭhāna (counting locative «Nဟူသော အကြောင်း၌ K», bare ghaṭanā name, ablative «…ကြောင့်»); the pi-1 … pi-6 value is the plain noun / verb of another kind of segment and stands in the pi-7 segment only as a part of the condition name |
| āhāra = အာဟာရ | ဆိုခြင်း (3) | T1 / T2: the condition in the frame of the Paṭṭhāna (counting locative «Nဟူသော အကြောင်း၌ K», bare ghaṭanā name, ablative «…ကြောင့်»); the pi-1 … pi-6 value is the plain noun / verb of another kind of segment and stands in the pi-7 segment only as a part of the condition name |
| kiñci = အချို့သော | တစ်စုံတစ်ရာ (2) | «kiñci kāle» «အချို့သော အချိန်၌»; the pi-5 «တစ်စုံတစ်ရာ» is not in the segment |
| ekamūlakaṃ = အကြောင်း တစ်ခုကို အခြေခံခြင်း | တစ်မျိုးတွဲကို အခြေခံသော (2) | T6: the counted mūlaka «အကြောင်း တစ်ခုကို အခြေခံခြင်း» (my7-zeroshot-terms §2); the pi-3 «တစ်မျိုးတွဲကို အခြေခံသော» (Dhātukathā) is not in the segment |
| katvā = (no direct equivalent) | အကြောင်းပြု၍ (2) | T11 / pi-2 harmonise (one Burmese word for two members): after the act compound uposathakammaṃ the verb «စောင့်ထိန်း၍» belongs to the compound's value; the pi-5 «အကြောင်းပြု၍» is not in the segment |
| āsevana = အလေ့အကျင့် ပြုခြင်း | အဖန်ဖန် မှီဝဲခြင်း (2) | T1 / T2: the condition in the frame of the Paṭṭhāna (counting locative «Nဟူသော အကြောင်း၌ K», bare ghaṭanā name, ablative «…ကြောင့်»); the pi-1 … pi-6 value is the plain noun / verb of another kind of segment and stands in the pi-7 segment only as a part of the condition name |
| samanantarā = ကောင်းစွာ ချက်ချင်း နောက် | ချက်ချင်း နောက်၌ (1) | the pi-7 text gives the adverb its condition's word «ကောင်းစွာ ချက်ချင်း နောက်၌» (notes-sample point 2; rule 1: «၌» goes); the pi-5 «ချက်ချင်း နောက်၌» stands only as a part of it |
| Aññamañña = အချင်းချင်း ထောက်ပံ့ခြင်းဟူသော အကြောင်း | အချင်းချင်း အကြောင်းဖြစ်ခြင်း (1) | T1 / T2: the condition in the frame of the Paṭṭhāna (counting locative «Nဟူသော အကြောင်း၌ K», bare ghaṭanā name, ablative «…ကြောင့်»); the pi-1 … pi-6 value is the plain noun / verb of another kind of segment and stands in the pi-7 segment only as a part of the condition name |
| indriya = စွမ်းရည်ဟူသော အကြောင်း | စွမ်းရည် (1) | T1 / T2: the condition in the frame of the Paṭṭhāna (counting locative «Nဟူသော အကြောင်း၌ K», bare ghaṭanā name, ablative «…ကြောင့်»); the pi-1 … pi-6 value is the plain noun / verb of another kind of segment and stands in the pi-7 segment only as a part of the condition name |
| natthi = မရှိ | မရှိသည် (1) | T1 / T2: the condition in the frame of the Paṭṭhāna (counting locative «Nဟူသော အကြောင်း၌ K», bare ghaṭanā name, ablative «…ကြောင့်»); the pi-1 … pi-6 value is the plain noun / verb of another kind of segment and stands in the pi-7 segment only as a part of the condition name; in a note the verb «မရှိ» (Q5) |
| sahajāto = အတူ ပေါ်ပေါက်သော | အတူတကွ ဖြစ်ပေါ်သော (1) | my7-zeroshot-terms §4 link word «Xနှင့်အတူ ပေါ်ပေါက်သော»; the pi-2 «အတူတကွ ဖြစ်ပေါ်သော» is not in the segment |
| nirodhā = ချုပ်ငြိမ်းခြင်း သမာပတ် | ချုပ်ငြိမ်းသော (1) | my7 LEX «nirodhā vuṭṭhahantassa» «ချုပ်ငြိမ်းခြင်း သမာပတ်မှ ထမြောက်နေသူ» (rule 1: «မှ» goes); the pi-5 «ချုပ်ငြိမ်းသော» is not in the segment |
| vuṭṭhahantassa = ထမြောက်နေသူ | ထမြောက်နေသော (1) | pi-4 P6 / pi-6 R3: a person participle is the agent noun «…သူ» (the text's «ထမြောက်နေသူ»); the pi-5 attributive «ထမြောက်နေသော» stands only by an ending rule |
| bhaṇati = ပြောသည် | ပြောဆိုသည် (1) | the text's «ပြောသည်»; the pi-5 «ပြောဆိုသည်» is not in the segment |
| harati = လုယူသည် | ဆောင်သည် (1) | T11: «nillopaṃ harati» «ဥစ္စာကို လုယူသည်»; the pi-5 «ဆောင်သည်» is not in the segment |
| tiṭṭhati = ဓားပြ တိုက်သည် | တည်သည် (1) | T11: «paripanthe tiṭṭhati» «လမ်းခရီး၌ ဓားပြ တိုက်သည်»; the pi-5 «တည်သည်» stands in the segment only inside «ဆောက်တည်သည်» (samādiyati), another word |
| Anantara = ချက်ချင်း နောက်၌ ဖြစ်စေခြင်း | ချက်ချင်း နောက်၌ ဖြစ်စေသော (1) | T1 / T2: the condition in the frame of the Paṭṭhāna (counting locative «Nဟူသော အကြောင်း၌ K», bare ghaṭanā name, ablative «…ကြောင့်»); the pi-1 … pi-6 value is the plain noun / verb of another kind of segment and stands in the pi-7 segment only as a part of the condition name |
| jhāne = ဈာန်ဟူသော အကြောင်း | ဈာန် (1) | T1 / T2: the condition in the frame of the Paṭṭhāna (counting locative «Nဟူသော အကြောင်း၌ K», bare ghaṭanā name, ablative «…ကြောင့်»); the pi-1 … pi-6 value is the plain noun / verb of another kind of segment and stands in the pi-7 segment only as a part of the condition name |
| sampayutta = ယှဉ်တွဲခြင်း | ယှဉ်တွဲသော (1) | T1 / T2: the condition in the frame of the Paṭṭhāna (counting locative «Nဟူသော အကြောင်း၌ K», bare ghaṭanā name, ablative «…ကြောင့်»); the pi-1 … pi-6 value is the plain noun / verb of another kind of segment and stands in the pi-7 segment only as a part of the condition name |
| Āsevana = အလေ့အကျင့် ပြုခြင်း | အဖန်ဖန် မှီဝဲခြင်း (1) | T1 / T2: the condition in the frame of the Paṭṭhāna (counting locative «Nဟူသော အကြောင်း၌ K», bare ghaṭanā name, ablative «…ကြောင့်»); the pi-1 … pi-6 value is the plain noun / verb of another kind of segment and stands in the pi-7 segment only as a part of the condition name |
| Āhāra = အာဟာရ | ဆိုခြင်း (1) | T1 / T2: the condition in the frame of the Paṭṭhāna (counting locative «Nဟူသော အကြောင်း၌ K», bare ghaṭanā name, ablative «…ကြောင့်»); the pi-1 … pi-6 value is the plain noun / verb of another kind of segment and stands in the pi-7 segment only as a part of the condition name |
| Sampayutta = ယှဉ်တွဲခြင်း | ယှဉ်တွဲသော (1) | T1 / T2: the condition in the frame of the Paṭṭhāna (counting locative «Nဟူသော အကြောင်း၌ K», bare ghaṭanā name, ablative «…ကြောင့်»); the pi-1 … pi-6 value is the plain noun / verb of another kind of segment and stands in the pi-7 segment only as a part of the condition name |
| mūlakaṃ = အခြေခံ အကြောင်း | အခြေခံသော (1) | the note «(mūlakaṃ saṃkhittaṃ)» «(အခြေခံ အကြောင်းများကို အကျဉ်းချုပ်)» (rule 1); the pi-5 «အခြေခံသော» is not in the segment |

## Presence: chunks matched by an ending rule (no other exception)

Every chunk of every value stands in its segment's Burmese, literally or by one of the approved ending rules of the verifier (pi-1 rules 3 / 4 / 8, pi-2 N11, pi-3 M7, pi-4 P3 / A2, pi-5 Q1, pi-6 phase 3): no presence failure and no exception outside these rules.

| rule | chunks | example |
|---|---|---|
| verb | 227 | ^T-1 Namo: «ရှိခိုးသည်» |
| attr-fut | 12 | ^7-1-32 vitthāretabbo: «ချဲ့ရမည့်» |
| attr | 11 | ^7-3-9 paripuṇṇaṃ: «ပြည့်စုံသော» |

## Frame keywords → Burmese (the module's families; every phase-2 agent gets these)

### T1-T4: the 24 conditions (X = the Pāli stem; N = the bare name)

| X | N (bare, ghaṭanā) | Xpaccayo / -ena / -oti / -opi (name) | Xpaccayā (ablative) | Xe / Xyā (count) | naXpaccayo / naXe | naXpaccayā |
|---|---|---|---|---|---|---|
| hetu | အမြစ် | အမြစ်ဟူသော အကြောင်း | အမြစ်ဟူသော အကြောင်းကြောင့် | အမြစ်ဟူသော အကြောင်း | အမြစ်ဟူသော အကြောင်း မဟုတ်ခြင်း | အမြစ်ဟူသော အကြောင်းကြောင့် မဟုတ် |
| ārammaṇa | အာရုံ | အာရုံဟူသော အကြောင်း | အာရုံဟူသော အကြောင်းကြောင့် | အာရုံဟူသော အကြောင်း | အာရုံဟူသော အကြောင်း မဟုတ်ခြင်း | အာရုံဟူသော အကြောင်းကြောင့် မဟုတ် |
| adhipati | အကြီးအမှူး | အကြီးအမှူးဟူသော အကြောင်း | အကြီးအမှူးဟူသော အကြောင်းကြောင့် | အကြီးအမှူးဟူသော အကြောင်း | အကြီးအမှူးဟူသော အကြောင်း မဟုတ်ခြင်း | အကြီးအမှူးဟူသော အကြောင်းကြောင့် မဟုတ် |
| anantara | ချက်ချင်း နောက်၌ ဖြစ်စေခြင်း | ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းဟူသော အကြောင်း | ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းဟူသော အကြောင်းကြောင့် | ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းဟူသော အကြောင်း | ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းဟူသော အကြောင်း မဟုတ်ခြင်း | ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းဟူသော အကြောင်းကြောင့် မဟုတ် |
| samanantara | ကောင်းစွာ ချက်ချင်း နောက်၌ ဖြစ်စေခြင်း | ကောင်းစွာ ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းဟူသော အကြောင်း | ကောင်းစွာ ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းဟူသော အကြောင်းကြောင့် | ကောင်းစွာ ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းဟူသော အကြောင်း | ကောင်းစွာ ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းဟူသော အကြောင်း မဟုတ်ခြင်း | ကောင်းစွာ ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းဟူသော အကြောင်းကြောင့် မဟုတ် |
| sahajāta | အတူ ပေါ်ပေါက်ခြင်း | အတူ ပေါ်ပေါက်ခြင်းဟူသော အကြောင်း | အတူ ပေါ်ပေါက်ခြင်းဟူသော အကြောင်းကြောင့် | အတူ ပေါ်ပေါက်ခြင်းဟူသော အကြောင်း | အတူ ပေါ်ပေါက်ခြင်းဟူသော အကြောင်း မဟုတ်ခြင်း | အတူ ပေါ်ပေါက်ခြင်းဟူသော အကြောင်းကြောင့် မဟုတ် |
| aññamañña | အချင်းချင်း ထောက်ပံ့ခြင်း | အချင်းချင်း ထောက်ပံ့ခြင်းဟူသော အကြောင်း | အချင်းချင်း ထောက်ပံ့ခြင်းဟူသော အကြောင်းကြောင့် | အချင်းချင်း ထောက်ပံ့ခြင်းဟူသော အကြောင်း | အချင်းချင်း ထောက်ပံ့ခြင်းဟူသော အကြောင်း မဟုတ်ခြင်း | အချင်းချင်း ထောက်ပံ့ခြင်းဟူသော အကြောင်းကြောင့် မဟုတ် |
| nissaya | အမှီ | အမှီဟူသော အကြောင်း | အမှီဟူသော အကြောင်းကြောင့် | အမှီဟူသော အကြောင်း | အမှီဟူသော အကြောင်း မဟုတ်ခြင်း | အမှီဟူသော အကြောင်းကြောင့် မဟုတ် |
| upanissaya | အားကြီးသော အမှီ | အားကြီးသော အမှီဟူသော အကြောင်း | အားကြီးသော အမှီဟူသော အကြောင်းကြောင့် | အားကြီးသော အမှီဟူသော အကြောင်း | အားကြီးသော အမှီဟူသော အကြောင်း မဟုတ်ခြင်း | အားကြီးသော အမှီဟူသော အကြောင်းကြောင့် မဟုတ် |
| purejāta | ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်း | ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်းဟူသော အကြောင်း | ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်းဟူသော အကြောင်းကြောင့် | ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်းဟူသော အကြောင်း | ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်းဟူသော အကြောင်း မဟုတ်ခြင်း | ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်းဟူသော အကြောင်းကြောင့် မဟုတ် |
| pacchājāta | နောက်မှ ဖြစ်ပေါ်ခြင်း | နောက်မှ ဖြစ်ပေါ်ခြင်းဟူသော အကြောင်း | နောက်မှ ဖြစ်ပေါ်ခြင်းဟူသော အကြောင်းကြောင့် | နောက်မှ ဖြစ်ပေါ်ခြင်းဟူသော အကြောင်း | နောက်မှ ဖြစ်ပေါ်ခြင်းဟူသော အကြောင်း မဟုတ်ခြင်း | နောက်မှ ဖြစ်ပေါ်ခြင်းဟူသော အကြောင်းကြောင့် မဟုတ် |
| āsevana | အလေ့အကျင့် ပြုခြင်း | အလေ့အကျင့် ပြုခြင်းဟူသော အကြောင်း | အလေ့အကျင့် ပြုခြင်းဟူသော အကြောင်းကြောင့် | အလေ့အကျင့် ပြုခြင်းဟူသော အကြောင်း | အလေ့အကျင့် ပြုခြင်းဟူသော အကြောင်း မဟုတ်ခြင်း | အလေ့အကျင့် ပြုခြင်းဟူသော အကြောင်းကြောင့် မဟုတ် |
| kamma | ကံ | ကံဟူသော အကြောင်း | ကံဟူသော အကြောင်းကြောင့် | ကံဟူသော အကြောင်း | ကံဟူသော အကြောင်း မဟုတ်ခြင်း | ကံဟူသော အကြောင်းကြောင့် မဟုတ် |
| vipāka | ကံ၏ အကျိုး | ကံ၏ အကျိုးဟူသော အကြောင်း | ကံ၏ အကျိုးဟူသော အကြောင်းကြောင့် | ကံ၏ အကျိုးဟူသော အကြောင်း | ကံ၏ အကျိုးဟူသော အကြောင်း မဟုတ်ခြင်း | ကံ၏ အကျိုးဟူသော အကြောင်းကြောင့် မဟုတ် |
| āhāra | အာဟာရ | အာဟာရဟူသော အကြောင်း | အာဟာရဟူသော အကြောင်းကြောင့် | အာဟာရဟူသော အကြောင်း | အာဟာရဟူသော အကြောင်း မဟုတ်ခြင်း | အာဟာရဟူသော အကြောင်းကြောင့် မဟုတ် |
| indriya | စွမ်းရည် | စွမ်းရည်ဟူသော အကြောင်း | စွမ်းရည်ဟူသော အကြောင်းကြောင့် | စွမ်းရည်ဟူသော အကြောင်း | စွမ်းရည်ဟူသော အကြောင်း မဟုတ်ခြင်း | စွမ်းရည်ဟူသော အကြောင်းကြောင့် မဟုတ် |
| jhāna | ဈာန် | ဈာန်ဟူသော အကြောင်း | ဈာန်ဟူသော အကြောင်းကြောင့် | ဈာန်ဟူသော အကြောင်း | ဈာန်ဟူသော အကြောင်း မဟုတ်ခြင်း | ဈာန်ဟူသော အကြောင်းကြောင့် မဟုတ် |
| magga | မဂ် | မဂ်ဟူသော အကြောင်း | မဂ်ဟူသော အကြောင်းကြောင့် | မဂ်ဟူသော အကြောင်း | မဂ်ဟူသော အကြောင်း မဟုတ်ခြင်း | မဂ်ဟူသော အကြောင်းကြောင့် မဟုတ် |
| sampayutta | ယှဉ်တွဲခြင်း | ယှဉ်တွဲခြင်းဟူသော အကြောင်း | ယှဉ်တွဲခြင်းဟူသော အကြောင်းကြောင့် | ယှဉ်တွဲခြင်းဟူသော အကြောင်း | ယှဉ်တွဲခြင်းဟူသော အကြောင်း မဟုတ်ခြင်း | ယှဉ်တွဲခြင်းဟူသော အကြောင်းကြောင့် မဟုတ် |
| vippayutta | ကင်းကွာခြင်း | ကင်းကွာခြင်းဟူသော အကြောင်း | ကင်းကွာခြင်းဟူသော အကြောင်းကြောင့် | ကင်းကွာခြင်းဟူသော အကြောင်း | ကင်းကွာခြင်းဟူသော အကြောင်း မဟုတ်ခြင်း | ကင်းကွာခြင်းဟူသော အကြောင်းကြောင့် မဟုတ် |
| atthi | ရှိခြင်း | ရှိခြင်းဟူသော အကြောင်း | ရှိခြင်းဟူသော အကြောင်းကြောင့် | ရှိခြင်းဟူသော အကြောင်း | ရှိခြင်းဟူသော အကြောင်း မဟုတ်ခြင်း | ရှိခြင်းဟူသော အကြောင်းကြောင့် မဟုတ် |
| natthi | မရှိခြင်း | မရှိခြင်းဟူသော အကြောင်း | မရှိခြင်းဟူသော အကြောင်းကြောင့် | မရှိခြင်းဟူသော အကြောင်း | မရှိခြင်းဟူသော အကြောင်း မဟုတ်ခြင်း | မရှိခြင်းဟူသော အကြောင်းကြောင့် မဟုတ် |
| vigata | ပျောက်ကွယ်ခြင်း | ပျောက်ကွယ်ခြင်းဟူသော အကြောင်း | ပျောက်ကွယ်ခြင်းဟူသော အကြောင်းကြောင့် | ပျောက်ကွယ်ခြင်းဟူသော အကြောင်း | ပျောက်ကွယ်ခြင်းဟူသော အကြောင်း မဟုတ်ခြင်း | ပျောက်ကွယ်ခြင်းဟူသော အကြောင်းကြောင့် မဟုတ် |
| avigata | မပျောက်ကွယ်ခြင်း | မပျောက်ကွယ်ခြင်းဟူသော အကြောင်း | မပျောက်ကွယ်ခြင်းဟူသော အကြောင်းကြောင့် | မပျောက်ကွယ်ခြင်းဟူသော အကြောင်း | မပျောက်ကွယ်ခြင်းဟူသော အကြောင်း မဟုတ်ခြင်း | မပျောက်ကွယ်ခြင်းဟူသော အကြောင်းကြောင့် မဟုတ် |

Other condition forms (the same N): X-mūlakaṃ «Nဟူသော အကြောင်းကို အခြေခံခြင်း»; X-dukaṃ «Nဟူသော အကြောင်း၏ နှစ်မျိုးတွဲ» (naX «… မဟုတ်ခြင်း၏ …»); X-paccayādi «… စသည်»; X-sabhāgaṃ «Nဟူသော အကြောင်းနှင့် တွဲဖက်သည်» (rule 1: «များ» goes); X-ghaṭanā «Nဟူသော အကြောင်း၏ ပေါင်းစပ်ချက်»; sa-X «Nဟူသော အကြောင်း ပါဝင်သော» (in a hyphen compound «Nဟူသော အကြောင်း … ပါဝင်သော»); X-paccayasadisaṃ «Nဟူသော အကြောင်းနှင့် တူသည်», a bare X-sadisaṃ «Nနှင့် တူသည်» (harmonise H19), the text's adverbial «…နှင့် တူအောင်» before «ပြုရမည် / ချဲ့ရမည်»; a hyphen-compound part «Napacchājāta-» takes the case of the whole compound (T4: name in a heading, ablative before «-paccayā», bare in a ghaṭanā list «-nti»).

### T5: vāra names and orders

| Pāli | Burmese |
|---|---|
| paṭiccavāro (-vāre, -vārepi, -vārampi, -vāraṃ …) | မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက် |
| sahajātavāro (-vāre, -vārepi, -vārampi, -vāraṃ …) | အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက် |
| paccayavāro (-vāre, -vārepi, -vārampi, -vāraṃ …) | အကြောင်းပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက် |
| nissayavāro (-vāre, -vārepi, -vārampi, -vāraṃ …) | အမှီပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက် |
| saṃsaṭṭhavāro (-vāre, -vārepi, -vārampi, -vāraṃ …) | ရောနှောခြင်းအလိုက် ဖော်ပြချက် |
| sampayuttavāro (-vāre, -vārepi, -vārampi, -vāraṃ …) | ယှဉ်တွဲခြင်းအလိုက် ဖော်ပြချက် |
| pañhāvāro (-vāre, -vārepi, -vārampi, -vāraṃ …) | ပြဿနာအလိုက် ဖော်ပြချက် |
| pucchāvāro (-vāre, -vārepi, -vārampi, -vāraṃ …) | အမေးအလိုက် ဖော်ပြချက် |
| vibhaṅgavāro (-vāre, -vārepi, -vārampi, -vāraṃ …) | ခွဲခြမ်းစိတ်ဖြာခြင်းအလိုက် ဖော်ပြချက် |
| saṅkhyāvāro (-vāre, -vārepi, -vārampi, -vāraṃ …) | ရေတွက်ခြင်းအလိုက် ဖော်ပြချက် |
| hetupaccayavāro (-vāre, -vārepi, -vārampi, -vāraṃ …) | အမြစ်ဟူသော အကြောင်းအလိုက် ဖော်ပြချက် |
| X-vārādi | Xအလိုက် ဖော်ပြချက် စသည် |
| X-vārasadisaṃ / -ā / -o | Xအလိုက် ဖော်ပြချက်နှင့် တူသည် (adverbial «…နှင့် တူအောင်») |
| anulomaṃ | အဟုတ်ပြ ပုံစံ |
| paccanīyaṃ | အငြင်းပြ ပုံစံ |
| anulomapaccanīyaṃ | အဟုတ်ပြ အငြင်းပြ ပုံစံ |
| paccanīyānulomaṃ | အငြင်းပြ အဟုတ်ပြ ပုံစံ |
| Paccayānulomaṃ | အကြောင်း အဟုတ်ပြ ပုံစံ |
| Paccayapaccanīyaṃ | အကြောင်း အငြင်းပြ ပုံစံ |
| Paccayānulomapaccanīyaṃ | အကြောင်း အဟုတ်ပြ အငြင်းပြ ပုံစံ |
| Paccayapaccanīyānulomaṃ | အကြောင်း အငြင်းပြ အဟုတ်ပြ ပုံစံ |
| Dhammānulome | သဘောတရား အဟုတ်ပြ ပုံစံ |
| Dhammapaccanīye | သဘောတရား အငြင်းပြ ပုံစံ |
| anulome | အဟုတ်ပြ ပုံစံ |
| Paccanīyagaṇanā | အငြင်းပြ ပုံစံ၏ ရေတွက်ချက် |
| anulomamātikā | အဟုတ်ပြ ပုံစံ၏ ခေါင်းစဉ်စာရင်း |

### T6: counts and counting groups

| Pāli | Burmese |
|---|---|
| ekaṃ … dasa, ekādasa … ekūnapaññāsa (answers) | the text's count + «ခု» (တစ်ခု … ဆယ်ခု, ဆယ့်တစ်ခု, နှစ်ဆယ့်တစ်ခု, သုံးဆယ့်ခုနစ်ခု …) |
| eko / dve / tayo / cattāro (khandha, mahābhūta) | the text's count + «ပါး» |
| dukaṃ, tikaṃ, catukkaṃ … catuvīsakaṃ | နှစ်မျိုးတွဲ, သုံးမျိုးတွဲ, လေးမျိုးတွဲ … နှစ်ဆယ့်လေးမျိုးတွဲ |
| Paccayacatukkaṃ | အကြောင်း လေးမျိုးတွဲ |
| Ekamūlakaṃ / Dumūlakaṃ … tevīsatimūlakaṃ / Sabbamūlakaṃ | အကြောင်း တစ်ခုကို / နှစ်ခုကို … နှစ်ဆယ့်သုံးခုကို / အားလုံးကို အခြေခံခြင်း |
| Pañcamūlakādikā | အကြောင်း ငါးခုကို အခြေခံခြင်း စသည် |
| tevīsatipaccayā | အကြောင်း နှစ်ဆယ့်သုံးပါး |
| X-paṭṭhānaṃ (tika, duka, dukatika, tikaduka, tikatika, dukaduka) | Xတို့၏ အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ |

### Stock frame words (FRAME / STOCK / LEXW; the full lists are in map7_rules.py)

| Pāli | Burmese | Pāli | Burmese |
|---|---|---|---|
| ca | (no direct equivalent) | pana | (no direct equivalent) |
| vā | (no direct equivalent) | ti | (no direct equivalent) |
| pi | (no direct equivalent) | eva | (no direct equivalent) |
| yeva | (no direct equivalent) | siyā | (no direct equivalent) |
| Namo | ရှိခိုးသည် | bhagavato | မြတ်စွာဘုရား |
| arahato | ရဟန္တာ | sammāsambuddhassa | အမှန်ကို ကိုယ်တိုင် အပြည့်အဝ သိမြင်တော်မူသော ဘုရားရှင် |
| tassa | ထို / (no direct equivalent) (alt) | taṃ | ထိုအရာ / ထို (alt) |
| Abhidhammapiṭake | အဘိဓမ္မာပိဋက | Paṭṭhānapāḷi | အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ |
| paṭicca | မှီ၍ | nissāya | မှီ၍ |
| ārabbha | အာရုံပြု၍ | paccayo | context function paccayo |
| aññamaññaṃ | အချင်းချင်း | garuṃ | လေးစားဖွယ်ရာ |
| kiñci | အချို့သော | kāle | အချိန် |
| saṃkhittaṃ | အကျဉ်းချုပ် | Saṃkhittaṃ | အကျဉ်းချုပ် |
| saṃkhittā | အကျဉ်းချုပ် | vitthāretabbo | အကျယ် ချဲ့ရမည့် |
| vitthāretabbaṃ | အကျယ် ချဲ့ရမည့် | vitthāretabbā | အကျယ် ချဲ့ရမည့် |
| vitthārito | အကျယ် ချဲ့ထားသော | vācanāmaggena | ရွတ်ဆိုသည့် နည်းလမ်း |
| sajjhāyamaggena | သရဇ္ဈာယ်သည့် နည်းလမ်း | asammuyhantena | မရောထွေးစေဘဲ |
| gaṇetabbaṃ | ရေတွက်ရမည့် | evaṃ | ထိုနည်းတူ / ဤသို့ (alt) |
| paṭṭhānavaraṃ | မြတ်သော အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ | dukuttamaṃ | နှစ်မျိုးတွဲတို့၏ အမြတ်ဆုံး ဆက်စပ်ပုံ |
| ekekassa | တစ်ခုစီ | padassa | ပုဒ် |
| gaṇitā | ရေတွက်ထားသော | ātāpeti | ပူပန်စေသည် |
| paritāpeti | ပြင်းစွာ ပူပန်စေသည် | natthi | context function natthi |
| anantarā | ချက်ချင်း နောက် | samanantarā | ကောင်းစွာ ချက်ချင်း နောက် |
| mūlakaṃ | အခြေခံ အကြောင်း (alt) | paripuṇṇaṃ | ပြည့်စုံသော |
| karoti | context function karoti | katvā | context function katva |
| yāva | အထိ | ceva | (no direct equivalent) |
| cāti | (no direct equivalent) | pīti | (no direct equivalent) |
| kātabbā | ပြုရမည့် / ထည့်ရမည့် (alt) | kātabbaṃ | ပြုရမည့် / ထည့်ရမည့် (alt) |
| kātabbo | ပြုရမည့် / ထည့်ရမည့် (alt) | suciṇṇāni | ကောင်းစွာ ကျင့်ခဲ့ဖူးသော |
| ninnānākaraṇaṃ | ကွဲပြားချက် မရှိ | vibhajitabbā | ခွဲခြမ်းစိတ်ဖြာရမည့် |
| vibhattā | ခွဲခြမ်းစိတ်ဖြာထားသော | gaṇanā | ရေတွက်ချက် |
| Gaṇanā | ရေတွက်ချက် | gaṇanāpi | ရေတွက်ချက် |
| anumajjantena | ပြန်လည် စိစစ်လျက် | dhammo | သဘောတရား |
| dhammā | သဘောတရား | dhammaṃ | သဘောတရား |
| dhamme | သဘောတရား | dhammassa | သဘောတရား |
| dhammānaṃ | သဘောတရား | dhamma | သဘောတရား |
| khandho | အစုအဝေး | khandhā | အစုအဝေး |
| khandhaṃ | အစုအဝေး | khandhe | အစုအဝေး |
| khandhassa | အစုအဝေး | khandhānaṃ | အစုအဝေး |
| khandha | အစုအဝေး | rūpaṃ | context function rupam |
| rūpānaṃ | context function rupam | rūpa | context function rupam |
| rūpassa | context function rupam | mahābhūtā | မူလဓာတ်ကြီး |
| mahābhūtaṃ | မူလဓာတ်ကြီး | mahābhūte | မူလဓာတ်ကြီး |
| mahābhūtānaṃ | မူလဓာတ်ကြီး | mahābhūtassa | မူလဓာတ်ကြီး |
| cittacetasikā | စိတ်နှင့် စိတ်၏ အဖော် | cittacetasikānaṃ | စိတ်နှင့် စိတ်၏ အဖော် |
| cittacetasikaṃ | စိတ်နှင့် စိတ်၏ အဖော် | taṃsampayuttakā | ထိုအရာနှင့် ယှဉ်တွဲသော |
| taṃsampayuttakānaṃ | ထိုအရာနှင့် ယှဉ်တွဲသော | taṃsampayuttaka | ထိုအရာနှင့် ယှဉ်တွဲသော |
| taṃsamuṭṭhānānaṃ | ထိုအရာမှ ဖြစ်ပေါ်လာသော | cittasamuṭṭhānānaṃ | စိတ်မှ ဖြစ်ပေါ်လာသော |
| cittasamuṭṭhānaṃ | စိတ်မှ ဖြစ်ပေါ်လာသော | cittasamuṭṭhānā | စိတ်မှ ဖြစ်ပေါ်လာသော |
| arūpino | ရုပ် မဟုတ်သော | arūpīnaṃ | ရုပ် မဟုတ်သော |
| Arūpino | ရုပ် မဟုတ်သော | rūpino | ရုပ် ဖြစ်သော |
| rūpīnaṃ | ရုပ် ဖြစ်သော | Rūpino | ရုပ် ဖြစ်သော |
| upādārūpānaṃ | မူလဓာတ်ကြီးတို့ကို မှီ၍ ဖြစ်သော ရုပ် | upādārūpaṃ | မူလဓာတ်ကြီးတို့ကို မှီ၍ ဖြစ်သော ရုပ် |
| upādārūpā | မူလဓာတ်ကြီးတို့ကို မှီ၍ ဖြစ်သော ရုပ် | kaṭattārūpānaṃ | ကံ ပြုခဲ့သောကြောင့် ဖြစ်သော ရုပ် |
| kaṭattārūpaṃ | ကံ ပြုခဲ့သောကြောင့် ဖြစ်သော ရုပ် | kaṭattārūpā | ကံ ပြုခဲ့သောကြောင့် ဖြစ်သော ရုပ် |
| kaṭattā | ကံ ပြုခဲ့သောကြောင့် | okkantikkhaṇe | သန္ဓေ သက်ဆင်းသော ခဏ |
| paṭisandhikkhaṇe | ပဋိသန္ဓေ နေသော ခဏ | ahetukapaṭisandhikkhaṇe | အမြစ် မရှိသော ပဋိသန္ဓေ နေသော ခဏ |
| arūpe | ရုပ်မရှိသော ဘုံ | vatthuṃ | မှီရာ ဝတ္ထု |
| vatthu | မှီရာ ဝတ္ထု | purimā | ရှေးရှေး |
| pacchimānaṃ | နောက်နောက် | sampayuttakānaṃ | ယှဉ်တွဲသော |
| sampayuttā | ယှဉ်တွဲသော | sampayuttakā | ယှဉ်တွဲသော |
| sampayutto | ယှဉ်တွဲသော | sampayuttaṃ | ယှဉ်တွဲသော |
| vipāko | ကံ၏ အကျိုး ဖြစ်သော / ကံ၏ အကျိုး (alt) | vipākā | ကံ၏ အကျိုး ဖြစ်သော / ကံ၏ အကျိုး (alt) |
| vipākānaṃ | ကံ၏ အကျိုး ဖြစ်သော / ကံ၏ အကျိုး (alt) | vipākaṃ | ကံ၏ အကျိုး ဖြစ်သော / ကံ၏ အကျိုး (alt) |
| vipākassa | ကံ၏ အကျိုး ဖြစ်သော / ကံ၏ အကျိုး (alt) | kusalākusalaṃ | ကုသိုလ်နှင့် အကုသိုလ် |
| kammaṃ | ကံ | kabaḷīkāro | လုတ်ပြု၍ စားရသော |
| āhāro | အာဟာရ | imassa | ဤ |
| kāyassa | ကိုယ် | jhānaṅgāni | ဈာန်၏ အင်္ဂါ |
| maggaṅgāni | မဂ်၏ အင်္ဂါ | cetanā | စေ့ဆော်မှု |
| Cetanā | စေ့ဆော်မှု | pacchājātā | နောက်မှ ဖြစ်ပေါ်သော |
| samanantaraniruddhā | ချက်ချင်း ချုပ်ငြိမ်းပြီးသော | samanantaravigatā | ချက်ချင်း ပျောက်ကွယ်ပြီးသော |
| paṭuppannānaṃ | ပစ္စုပ္ပန် | sabbe | အားလုံး |
| maggaṃ | မဂ် / လမ်း (alt) | samāpattiṃ | သမာပတ် (alt) |
| deti | ပြုသည် (alt) | nillopaṃ | ဥစ္စာ (alt) |
| tiṭṭhati | ဓားပြ တိုက်သည် (alt) | sahajātā | အတူ ပေါ်ပေါက်သော (alt) |
| nānākkhaṇikā | ခဏ ကွဲပြားသော (alt) | nibbānaṃ | နိဗ္ဗာန် |
| nibbānassa | နိဗ္ဗာန် | nibbāne | နိဗ္ဗာန် |
| nibbāna | နိဗ္ဗာန် | Nibbānaṃ | နိဗ္ဗာန် |
| uposathakammaṃ | ဥပုသ်ကို စောင့်ထိန်းသည် / ဥပုသ် (alt) | parikammaṃ | ကြိုတင် ပြင်ဆင်မှု |
| kiriyaṃ | ပြုရုံမျှသာ ဖြစ်သော (alt) | paṭisandhi | ပဋိသန္ဓေ |
| paṭisandhiṃ | ပဋိသန္ဓေ | paṭisandhiyā | ပဋိသန္ဓေ |
| Paṭisandhi | ပဋိသန္ဓေ | ekāgārikaṃ | အိမ်တစ်လုံးတည်းကို ဝိုင်း၍ တိုက်သည် / အိမ်တစ်လုံးတည်း (alt) |

## Keyword → Burmese (sample chapters; uses; source)

| keyword | Burmese | uses | source |
|---|---|---|---|
| Abhidhammapiṭake | အဘိဓမ္မာပိဋက | 2 | frame |
| abhinandati | နှစ်သက်သည် | 4 | pi-5 |
| abhiññaṃ | ထူးကဲစွာ သိခြင်း | 3 | terms |
| Abyākatapadaṃ | ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော ပုဒ် | 1 | headlex |
| abyākataṃ | ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော | 2 | pi-2 |
| abyākato | ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော | 16 | pi-2 |
| abyākatānaṃ | ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော | 3 | term |
| adhipati | အကြီးအမှူး | 4 | cond |
| Adhipati | အကြီးအမှူး | 2 | cond |
| adhipatipaccayena | အကြီးအမှူးဟူသော အကြောင်း | 12 | cond |
| adhipatipaccayo | အကြီးအမှူးဟူသော အကြောင်း | 3 | cond |
| Adhipatipaccayo | အကြီးအမှူးဟူသော အကြောင်း | 3 | cond |
| Adhipatipaccayoti | အကြီးအမှူးဟူသော အကြောင်း | 1 | cond |
| adhipatipaccayā | အကြီးအမှူးဟူသော အကြောင်းကြောင့် | 38 | cond |
| Adhipatipaccayā | အကြီးအမှူးဟူသော အကြောင်းကြောင့် | 1 | cond |
| adhipatiyā | အကြီးအမှူးဟူသော အကြောင်း | 16 | cond |
| adinnaṃ | မပေးသည် | 3 | lex |
| Adukkhamasukhāya | မနာကျင် မသာယာသော | 34 | pi-2 |
| adukkhamasukhāya | မနာကျင် မသာယာသော | 20 | pi-2 |
| ahetukapaṭisandhikkhaṇe | အမြစ် မရှိသော ပဋိသန္ဓေ နေသော ခဏ | 2 | stock |
| ahetukaṃ | အမြစ် မရှိသော | 2 | terms |
| Akusalapadaṃ | အကုသိုလ် ပုဒ် | 1 | headlex |
| akusalaṃ | အကုသိုလ် | 4 | pi-2 |
| akusalo | အကုသိုလ် | 15 | pi-2 |
| akusalā | အကုသိုလ် | 3 | pi-2 |
| Akusalābyākatapadaṃ | အကုသိုလ်နှင့် ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော ပုဒ် | 1 | headlex |
| akusalānaṃ | အကုသိုလ် | 1 | pi-2 |
| Anantara | ချက်ချင်း နောက်၌ ဖြစ်စေခြင်း | 1 | cond |
| anantara | ချက်ချင်း နောက်၌ ဖြစ်စေခြင်း | 3 | cond |
| anantarapaccayena | ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းဟူသော အကြောင်း | 8 | cond |
| anantarapaccayo | ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းဟူသော အကြောင်း | 3 | cond |
| Anantarapaccayo | ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းဟူသော အကြောင်း | 3 | cond |
| Anantarapaccayoti | ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းဟူသော အကြောင်း | 1 | cond |
| anantarapaccayā | ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းဟူသော အကြောင်းကြောင့် | 30 | cond |
| Anantarapaccayā | ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းဟူသော အကြောင်းကြောင့် | 1 | cond |
| anantare | ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းဟူသော အကြောင်း | 18 | cond |
| anantarā | ချက်ချင်း နောက် | 1 | frame |
| anantarūpanissayo | ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းဖြင့် အားကြီးသော အမှီ | 3 | terms |
| anattato | အတ္တ မဟုတ် | 3 | lex |
| aniccato | မမြဲ | 9 | pi-5 |
| Anulomapaccanīyaṃ | အဟုတ်ပြ အငြင်းပြ ပုံစံ | 3 | order |
| anulomaṃ | အဟုတ်ပြ ပုံစံ | 3 | order |
| anulome | အဟုတ်ပြ ပုံစံ | 9 | order |
| anāgataṃsañāṇassa | အနာဂတ်ကို သိသော ဉာဏ် | 6 | terms |
| arahantaṃ | ရဟန္တာ | 1 | pi-5 |
| Ariyā | အရိယာ | 1 | terms |
| ariyā | အရိယာ | 2 | terms |
| arūpe | ရုပ်မရှိသော ဘုံ | 6 | stock |
| arūpino | ရုပ် မဟုတ်သော | 7 | stock |
| Arūpino | ရုပ် မဟုတ်သော | 1 | stock |
| arūpīnaṃ | ရုပ် မဟုတ်သော | 2 | stock |
| asammuyhantena | မရောထွေးစေဘဲ | 3 | frame |
| assādeti | သာယာ | 8 | lex |
| atthi | ရှိခြင်း | 13 | cond |
| atthipaccayena | ရှိခြင်းဟူသော အကြောင်း | 4 | cond |
| atthipaccayo | ရှိခြင်းဟူသော အကြောင်း | 3 | cond |
| atthipaccayā | ရှိခြင်းဟူသော အကြောင်းကြောင့် | 6 | cond |
| Atthipaccayā | ရှိခြင်းဟူသော အကြောင်းကြောင့် | 3 | cond |
| atthiyā | ရှိခြင်းဟူသော အကြောင်း | 21 | cond |
| attānaṃ | မိမိကိုယ် | 2 | terms |
| avigatanti | မပျောက်ကွယ်ခြင်း | 3 | cond |
| avigatapaccayena | မပျောက်ကွယ်ခြင်းဟူသော အကြောင်း | 8 | cond |
| avigatapaccayā | မပျောက်ကွယ်ခြင်းဟူသော အကြောင်းကြောင့် | 52 | cond |
| avigate | မပျောက်ကွယ်ခြင်းဟူသော အကြောင်း | 30 | cond |
| aññamañña | အချင်းချင်း ထောက်ပံ့ခြင်း | 13 | cond |
| Aññamañña | အချင်းချင်း ထောက်ပံ့ခြင်းဟူသော အကြောင်း | 1 | cond |
| aññamaññapaccayena | အချင်းချင်း ထောက်ပံ့ခြင်းဟူသော အကြောင်း | 5 | cond |
| aññamaññapaccayo | အချင်းချင်း ထောက်ပံ့ခြင်းဟူသော အကြောင်း | 3 | cond |
| aññamaññapaccayā | အချင်းချင်း ထောက်ပံ့ခြင်းဟူသော အကြောင်းကြောင့် | 11 | cond |
| aññamaññaṃ | အချင်းချင်း | 3 | frame |
| aññamaññe | အချင်းချင်း ထောက်ပံ့ခြင်းဟူသော အကြောင်း | 21 | cond |
| bhagavato | မြတ်စွာဘုရား | 1 | frame |
| bhavaṅgaṃ | ဘဝင် စိတ် | 2 | terms |
| bhaṇati | ပြောသည် | 1 | lex |
| bhindati | ဖြိုခွဲသည် | 3 | pi-2 |
| cakkhundriyaṃ | မျက်စိ၏ စွမ်းရည် | 1 | terms |
| cakkhuviññāṇadhātu | မျက်စိ သိစိတ် ဓာတ် | 14 | terms |
| Cakkhāyatanaṃ | မျက်စိ အာရုံခံ နယ်ပယ် | 9 | terms |
| cakkhāyatanaṃ | မျက်စိ အာရုံခံ နယ်ပယ် | 3 | terms |
| Catukkaṃ | လေးမျိုးတွဲ | 3 | count |
| Catumūlakaṃ | အကြောင်း လေးခုကို အခြေခံခြင်း | 1 | count |
| catumūlakaṃ | အကြောင်း လေးခုကို အခြေခံခြင်း | 2 | count |
| catuviññāṇasahagataṃ | သိစိတ် လေးပါးနှင့်အတူ ဖြစ်သော | 1 | terms |
| Catuvīsakaṃ | နှစ်ဆယ့်လေးမျိုးတွဲ | 4 | count |
| Cetanā | စေ့ဆော်မှု | 1 | stock |
| cetanā | စေ့ဆော်မှု | 4 | stock |
| cetopariyañāṇena | စိတ်ကို ပိုင်းခြား၍ သိသော ဉာဏ် | 9 | terms |
| Chakkaṃ | ခြောက်မျိုးတွဲ | 2 | count |
| chindati | ဖောက်ထွင်းသည် | 1 | lex |
| cittacetasikā | စိတ်နှင့် စိတ်၏ အဖော် | 21 | stock |
| Cittacetasikā | စိတ်နှင့် စိတ်၏ အဖော် | 12 | stock |
| cittasamuṭṭhānānaṃ | စိတ်မှ ဖြစ်ပေါ်လာသော | 4 | stock |
| cittena | စိတ် | 6 | terms |
| cāgaṃ | စွန့်လွှတ်ခြင်း | 2 | terms |
| Dasakaṃ | ဆယ်မျိုးတွဲ | 2 | count |
| datvā | ပြု၍ | 4 | lex |
| deti | ပြုသည် | 3 | stock |
| dhammaṃ | သဘောတရား | 57 | stock |
| dhammo | သဘောတရား | 27 | stock |
| dhammā | သဘောတရား | 12 | stock |
| dhammānaṃ | သဘောတရား | 9 | stock |
| Dhammānulome | သဘောတရား အဟုတ်ပြ ပုံစံ | 1 | order |
| diṭṭhi | အယူ | 26 | terms |
| diṭṭhiṃ | အယူ | 4 | terms |
| domanassaṃ | စိတ်ဆင်းရဲမှု | 4 | terms |
| dosassa | ဒေါသ | 2 | terms |
| dosaṃ | ဒေါသ | 2 | terms |
| dukkhasahagatassa | နာကျင်မှုနှင့်အတူ ဖြစ်သော | 6 | terms |
| dukkhasahagataṃ | နာကျင်မှုနှင့်အတူ ဖြစ်သော | 12 | terms |
| dukkhāya | နာကျင်သော | 3 | pi-2 |
| Dukkhāya | နာကျင်သော | 3 | pi-2 |
| dukuttamaṃ | နှစ်မျိုးတွဲတို့၏ အမြတ်ဆုံး ဆက်စပ်ပုံ | 4 | frame |
| Dumūlakaṃ | အကြောင်း နှစ်ခုကို အခြေခံခြင်း | 2 | count |
| dumūlakaṃ | အကြောင်း နှစ်ခုကို အခြေခံခြင်း | 3 | count |
| duṭṭhena | ပြစ်မှားသော | 1 | terms |
| dānaṃ | ပေးလှူခြင်း | 7 | pi-2 |
| Ekamūlakaṃ | အကြောင်း တစ်ခုကို အခြေခံခြင်း | 3 | count |
| ekamūlakaṃ | အကြောင်း တစ်ခုကို အခြေခံခြင်း | 2 | count |
| ekāgārikaṃ | အိမ်တစ်လုံးတည်းကို ဝိုင်း၍ တိုက်သည် | 1 | stock |
| Gandhāyatanaṃ | အနံ့ အာရုံခံ နယ်ပယ် | 8 | terms |
| garuṃ | လေးစားဖွယ်ရာ | 8 | frame |
| gaṇetabbaṃ | ရေတွက်ရမည့် | 4 | frame |
| gaṇhāti | စွဲယူသည် | 4 | lex |
| gaṇitā | ရေတွက်ထားသော | 1 | frame |
| gotrabhu | အနွယ် ပြောင်းခြင်း စိတ် | 3 | terms |
| gotrabhussa | အနွယ် ပြောင်းခြင်း စိတ် | 3 | terms |
| gāmaghātaṃ | ရွာကို ဖျက်ဆီး၍ လုယက်သည် | 1 | lex |
| hanati | သတ်သည် | 3 | pi-5 |
| harati | လုယူသည် | 1 | lex |
| Hetudukaṃ | အမြစ်ဟူသော အကြောင်း၏ နှစ်မျိုးတွဲ | 1 | cond |
| hetupaccayena | အမြစ်ဟူသော အကြောင်း | 6 | cond |
| hetupaccayo | အမြစ်ဟူသော အကြောင်း | 9 | cond |
| Hetupaccayo | အမြစ်ဟူသော အကြောင်း | 12 | cond |
| Hetupaccayoti | အမြစ်ဟူသော အကြောင်း | 1 | cond |
| hetupaccayā | အမြစ်ဟူသော အကြောင်းကြောင့် | 66 | cond |
| Hetupaccayā | အမြစ်ဟူသော အကြောင်းကြောင့် | 5 | cond |
| Hetuyā | အမြစ်ဟူသော အကြောင်း | 2 | cond |
| hetuyā | အမြစ်ဟူသော အကြောင်း | 11 | cond |
| iddhividhañāṇassa | တန်ခိုး အမျိုးမျိုးကို ပြနိုင်သော ဉာဏ် | 2 | terms |
| imassa | ဤ | 3 | stock |
| indriya | စွမ်းရည် | 6 | cond |
| Indriya | စွမ်းရည် | 1 | cond |
| indriya | စွမ်းရည်ဟူသော အကြောင်း | 1 | cond |
| indriyapaccayena | စွမ်းရည်ဟူသော အကြောင်း | 6 | cond |
| indriyapaccayo | စွမ်းရည်ဟူသော အကြောင်း | 3 | cond |
| indriyapaccayā | စွမ်းရည်ဟူသော အကြောင်းကြောင့် | 9 | cond |
| indriye | စွမ်းရည်ဟူသော အကြောင်း | 18 | cond |
| indriyā | စွမ်းရည် | 1 | pi-2 |
| jappeti | ဖြစ်ပေါ်စေသည် | 1 | pi-2 |
| jhānapaccayena | ဈာန်ဟူသော အကြောင်း | 4 | cond |
| jhānapaccayo | ဈာန်ဟူသော အကြောင်း | 2 | cond |
| jhānapaccayā | ဈာန်ဟူသော အကြောင်းကြောင့် | 6 | cond |
| jhānaṃ | ဈာန် | 1 | cond |
| jhānaṅgāni | ဈာန်၏ အင်္ဂါ | 1 | stock |
| jhāne | ဈာန်ဟူသော အကြောင်း | 1 | cond |
| jhānā | ဈာန် | 2 | terms |
| jānanti | သိသည် | 3 | terms |
| jānāti | သိသည် | 1 | terms |
| jīvitā | အသက် | 1 | pi-2 |
| kabaḷīkāro | လုတ်ပြု၍ စားရသော | 3 | stock |
| kamma | ကံ | 3 | cond |
| Kamma | ကံ | 2 | cond |
| kammapaccayena | ကံဟူသော အကြောင်း | 14 | cond |
| kammapaccayo | ကံဟူသော အကြောင်း | 3 | cond |
| Kammapaccayo | ကံဟူသော အကြောင်း | 3 | cond |
| kammapaccayā | ကံဟူသော အကြောင်းကြောင့် | 9 | cond |
| kammaṃ | ကံ | 1 | stock |
| kamme | ကံဟူသော အကြောင်း | 22 | cond |
| karoti | (no direct equivalent) | 1 | frame |
| katvā | (no direct equivalent) | 2 | frame |
| katvā | ပြု၍ | 3 | frame |
| kaṭattā | ကံ ပြုခဲ့သောကြောင့် | 1 | stock |
| kaṭattārūpānaṃ | ကံ ပြုခဲ့သောကြောင့် ဖြစ်သော ရုပ် | 2 | stock |
| khandhaṃ | အစုအဝေး | 10 | stock |
| khandhe | အစုအဝေး | 6 | stock |
| khandho | အစုအဝေး | 4 | stock |
| khandhā | အစုအဝေး | 11 | stock |
| khandhānaṃ | အစုအဝေး | 9 | stock |
| kilese | ကိလေသာ | 3 | terms |
| kiriyaṃ | ပြုရုံမျှသာ ဖြစ်သော | 5 | stock |
| kiriyābyākatā | ပြုရုံမျှသာ ဖြစ်သော ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော | 2 | terms |
| kiñci | အချို့သော | 2 | frame |
| Kusalapadaṃ | ကုသိုလ် ပုဒ် | 1 | headlex |
| kusalattikassa | ကုသိုလ် သုံးမျိုးတွဲ | 16 | terms |
| kusalattikaṃ | ကုသိုလ် သုံးမျိုးတွဲ | 4 | headlex |
| kusalañca | ကုသိုလ် | 1 | pi-6 |
| kusalaṃ | ကုသိုလ် | 44 | pi-2 |
| kusalo | ကုသိုလ် | 12 | pi-2 |
| kusalā | ကုသိုလ် | 4 | pi-2 |
| Kusalābyākatapadaṃ | ကုသိုလ်နှင့် ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော ပုဒ် | 1 | headlex |
| kusalākusalaṃ | ကုသိုလ်နှင့် အကုသိုလ် | 6 | stock |
| kāle | အချိန် | 2 | frame |
| kāyassa | ကိုယ် | 2 | stock |
| kāyaviññāṇasahagataṃ | ကိုယ် သိစိတ်နှင့်အတူ ဖြစ်သော | 4 | terms |
| kāyaviññāṇassa | ကိုယ် သိစိတ် | 1 | pi-2 |
| kāyaviññāṇaṃ | ကိုယ် သိစိတ် | 5 | terms |
| Kāyindriyaṃ | ကိုယ်၏ စွမ်းရည် | 2 | terms |
| Kāyāyatanaṃ | ကိုယ် အာရုံခံ နယ်ပယ် | 12 | terms |
| lohitaṃ | သွေး | 1 | terms |
| magga | မဂ် | 5 | cond |
| Magga | မဂ် | 1 | cond |
| maggapaccayena | မဂ်ဟူသော အကြောင်း | 4 | cond |
| maggapaccayo | မဂ်ဟူသော အကြောင်း | 2 | cond |
| maggapaccayā | မဂ်ဟူသော အကြောင်းကြောင့် | 6 | cond |
| maggassa | မဂ် | 3 | terms |
| maggaṃ | မဂ် | 1 | stock |
| maggaṅgāni | မဂ်၏ အင်္ဂါ | 1 | stock |
| magge | မဂ်ဟူသော အကြောင်း | 15 | cond |
| maggā | မဂ် | 4 | terms |
| mahābhūtā | မူလဓာတ်ကြီး | 10 | stock |
| manodhātuyā | မနော ဓာတ် | 28 | terms |
| manoviññāṇadhātu | မနော သိစိတ် ဓာတ် | 8 | terms |
| manoviññāṇadhātuyā | မနော သိစိတ် ဓာတ် | 1 | terms |
| mohaṃ | မောဟ | 2 | terms |
| Mohaṃ | မောဟ | 1 | terms |
| moho | မောဟ | 2 | terms |
| musā | မုသား | 1 | pi-2 |
| mānaṃ | မာန | 2 | terms |
| mātaraṃ | အမိ | 1 | pi-2 |
| mūlakaṃ | အခြေခံ အကြောင်း | 1 | frame |
| naadhipati | အကြီးအမှူးဟူသော အကြောင်းကြောင့် မဟုတ် | 1 | cond |
| Naadhipatidukaṃ | အကြီးအမှူးဟူသော အကြောင်း မဟုတ်ခြင်း၏ နှစ်မျိုးတွဲ | 2 | cond |
| Naadhipatipaccayo | အကြီးအမှူးဟူသော အကြောင်း မဟုတ်ခြင်း | 3 | cond |
| naadhipatipaccayā | အကြီးအမှူးဟူသော အကြောင်းကြောင့် မဟုတ် | 13 | cond |
| Naadhipatipaccayā | အကြီးအမှူးဟူသော အကြောင်းကြောင့် မဟုတ် | 1 | cond |
| naadhipatiyā | အကြီးအမှူးဟူသော အကြောင်း မဟုတ်ခြင်း | 17 | cond |
| naanantara | ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းဟူသော အကြောင်းကြောင့် မဟုတ် | 2 | cond |
| naanantare | ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းဟူသော အကြောင်း မဟုတ်ခြင်း | 2 | cond |
| naaññamañña | အချင်းချင်း ထောက်ပံ့ခြင်းဟူသော အကြောင်းကြောင့် မဟုတ် | 1 | cond |
| naaññamaññe | အချင်းချင်း ထောက်ပံ့ခြင်းဟူသော အကြောင်း မဟုတ်ခြင်း | 1 | cond |
| Nahetudukaṃ | အမြစ်ဟူသော အကြောင်း မဟုတ်ခြင်း၏ နှစ်မျိုးတွဲ | 4 | cond |
| Nahetupaccayo | အမြစ်ဟူသော အကြောင်း မဟုတ်ခြင်း | 1 | cond |
| Nahetupaccayā | အမြစ်ဟူသော အကြောင်းကြောင့် မဟုတ် | 31 | cond |
| nahetupaccayā | အမြစ်ဟူသော အကြောင်းကြောင့် မဟုတ် | 14 | cond |
| Nahetuyā | အမြစ်ဟူသော အကြောင်း မဟုတ်ခြင်း | 2 | cond |
| nahetuyā | အမြစ်ဟူသော အကြောင်း မဟုတ်ခြင်း | 8 | cond |
| naindriya | စွမ်းရည်ဟူသော အကြောင်းကြောင့် မဟုတ် | 2 | cond |
| naindriye | စွမ်းရည်ဟူသော အကြောင်း မဟုတ်ခြင်း | 2 | cond |
| Najhānadukaṃ | ဈာန်ဟူသော အကြောင်း မဟုတ်ခြင်း၏ နှစ်မျိုးတွဲ | 2 | cond |
| najhānapaccayā | ဈာန်ဟူသော အကြောင်းကြောင့် မဟုတ် | 4 | cond |
| najhāne | ဈာန်ဟူသော အကြောင်း မဟုတ်ခြင်း | 2 | cond |
| Nakammapaccayo | ကံဟူသော အကြောင်း မဟုတ်ခြင်း | 4 | cond |
| nakammapaccayā | ကံဟူသော အကြောင်းကြောင့် မဟုတ် | 4 | cond |
| nakamme | ကံဟူသော အကြောင်း မဟုတ်ခြင်း | 18 | cond |
| namagga | မဂ်ဟူသော အကြောင်းကြောင့် မဟုတ် | 1 | cond |
| Namaggadukaṃ | မဂ်ဟူသော အကြောင်း မဟုတ်ခြင်း၏ နှစ်မျိုးတွဲ | 2 | cond |
| Namaggapaccayo | မဂ်ဟူသော အကြောင်း မဟုတ်ခြင်း | 2 | cond |
| namaggapaccayā | မဂ်ဟူသော အကြောင်းကြောင့် မဟုတ် | 4 | cond |
| namagge | မဂ်ဟူသော အကြောင်း မဟုတ်ခြင်း | 27 | cond |
| Namo | ရှိခိုးသည် | 4 | frame |
| nanissaya | အမှီဟူသော အကြောင်းကြောင့် မဟုတ် | 4 | cond |
| nanissayapaccayā | အမှီဟူသော အကြောင်းကြောင့် မဟုတ် | 4 | cond |
| nanissaye | အမှီဟူသော အကြောင်း မဟုတ်ခြင်း | 2 | cond |
| Napacchājāta | နောက်မှ ဖြစ်ပေါ်ခြင်းဟူသော အကြောင်း မဟုတ်ခြင်း | 2 | cond |
| napacchājāta | နောက်မှ ဖြစ်ပေါ်ခြင်းဟူသော အကြောင်းကြောင့် မဟုတ် | 2 | cond |
| napacchājāte | နောက်မှ ဖြစ်ပေါ်ခြင်းဟူသော အကြောင်း မဟုတ်ခြင်း | 25 | cond |
| napurejāta | ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်းဟူသော အကြောင်းကြောင့် မဟုတ် | 1 | cond |
| Napurejātapaccayo | ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်းဟူသော အကြောင်း မဟုတ်ခြင်း | 2 | cond |
| napurejātapaccayā | ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်းဟူသော အကြောင်းကြောင့် မဟုတ် | 4 | cond |
| napurejāte | ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်းဟူသော အကြောင်း မဟုတ်ခြင်း | 16 | cond |
| nasamanantare | ကောင်းစွာ ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းဟူသော အကြောင်း မဟုတ်ခြင်း | 2 | cond |
| nasampayutta | ယှဉ်တွဲခြင်းဟူသော အကြောင်းကြောင့် မဟုတ် | 3 | cond |
| nasampayuttapaccayā | ယှဉ်တွဲခြင်းဟူသော အကြောင်းကြောင့် မဟုတ် | 2 | cond |
| nasampayutte | ယှဉ်တွဲခြင်းဟူသော အကြောင်း မဟုတ်ခြင်း | 1 | cond |
| natthi | မရှိ | 1 | frame |
| natthi | မရှိခြင်း | 4 | frame |
| natthipaccayena | မရှိခြင်းဟူသော အကြောင်း | 6 | cond |
| natthipaccayo | မရှိခြင်းဟူသော အကြောင်း | 3 | cond |
| natthipaccayā | မရှိခြင်းဟူသော အကြောင်းကြောင့် | 9 | cond |
| natthiyā | မရှိခြင်းဟူသော အကြောင်း | 18 | cond |
| naupanissaya | အားကြီးသော အမှီဟူသော အကြောင်းကြောင့် မဟုတ် | 1 | cond |
| naupanissaye | အားကြီးသော အမှီဟူသော အကြောင်း မဟုတ်ခြင်း | 4 | cond |
| Navakaṃ | ကိုးမျိုးတွဲ | 3 | count |
| navippayutta | ကင်းကွာခြင်းဟူသော အကြောင်းကြောင့် မဟုတ် | 1 | cond |
| Navippayuttadukaṃ | ကင်းကွာခြင်းဟူသော အကြောင်း မဟုတ်ခြင်း၏ နှစ်မျိုးတွဲ | 2 | cond |
| Navippayuttapaccayo | ကင်းကွာခြင်းဟူသော အကြောင်း မဟုတ်ခြင်း | 2 | cond |
| navippayuttapaccayā | ကင်းကွာခြင်းဟူသော အကြောင်းကြောင့် မဟုတ် | 4 | cond |
| navippayutte | ကင်းကွာခြင်းဟူသော အကြောင်း မဟုတ်ခြင်း | 29 | cond |
| Navipāka | ကံ၏ အကျိုးဟူသော အကြောင်း မဟုတ်ခြင်း | 1 | cond |
| navipākapaccayā | ကံ၏ အကျိုးဟူသော အကြောင်းကြောင့် မဟုတ် | 6 | cond |
| navipāke | ကံ၏ အကျိုးဟူသော အကြောင်း မဟုတ်ခြင်း | 21 | cond |
| naāhāre | အာဟာရဟူသော အကြောင်း မဟုတ်ခြင်း | 2 | cond |
| naārammaṇa | အာရုံဟူသော အကြောင်းကြောင့် မဟုတ် | 1 | cond |
| Naārammaṇapaccayā | အာရုံဟူသော အကြောင်းကြောင့် မဟုတ် | 1 | cond |
| naārammaṇapaccayā | အာရုံဟူသော အကြောင်းကြောင့် မဟုတ် | 9 | cond |
| naārammaṇe | အာရုံဟူသော အကြောင်း မဟုတ်ခြင်း | 4 | cond |
| naāsevana | အလေ့အကျင့် ပြုခြင်းဟူသော အကြောင်းကြောင့် မဟုတ် | 1 | cond |
| naāsevanapaccayā | အလေ့အကျင့် ပြုခြင်းဟူသော အကြောင်းကြောင့် မဟုတ် | 4 | cond |
| naāsevane | အလေ့အကျင့် ပြုခြင်းဟူသော အကြောင်း မဟုတ်ခြင်း | 20 | cond |
| nevasaññānāsaññāyatanassa | မှတ်သိမှု ရှိသည်လည်း မဟုတ် မှတ်သိမှု မရှိသည်လည်း မဟုတ်သော နယ်ပယ် | 2 | terms |
| nevasaññānāsaññāyatanaṃ | မှတ်သိမှု ရှိသည်လည်း မဟုတ် မှတ်သိမှု မရှိသည်လည်း မဟုတ်သော နယ်ပယ် | 2 | terms |
| nigamaghātaṃ | နိဂုံးကို ဖျက်ဆီး၍ လုယက်သည် | 9 | lex |
| nillopaṃ | ဥစ္စာ | 1 | stock |
| nirodhā | ချုပ်ငြိမ်းခြင်း သမာပတ် | 1 | lex |
| nissaya | အမှီ | 13 | cond |
| Nissaya | အမှီ | 1 | cond |
| nissayapaccayena | အမှီဟူသော အကြောင်း | 6 | cond |
| Nissayavāro | အမှီပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက် | 2 | vara |
| nissaye | အမှီဟူသော အကြောင်း | 2 | cond |
| nissāya | မှီ၍ | 1 | frame |
| niṭṭhitaṃ | ပြီးဆုံးသော | 2 | pi-3 |
| noatthiyā | ရှိခြင်းဟူသော အကြောင်း မဟုတ်ခြင်း | 1 | cond |
| noavigate | မပျောက်ကွယ်ခြင်းဟူသော အကြောင်း မဟုတ်ခြင်း | 7 | cond |
| nonatthipaccayā | မရှိခြင်းဟူသော အကြောင်းကြောင့် မဟုတ် | 2 | cond |
| nonatthiyā | မရှိခြင်းဟူသော အကြောင်း မဟုတ်ခြင်း | 2 | cond |
| novigatapaccayā | ပျောက်ကွယ်ခြင်းဟူသော အကြောင်းကြောင့် မဟုတ် | 2 | cond |
| novigate | ပျောက်ကွယ်ခြင်းဟူသော အကြောင်း မဟုတ်ခြင်း | 3 | cond |
| nānākkhaṇikā | ခဏ ကွဲပြားသော | 3 | stock |
| Okkantikkhaṇe | သန္ဓေ သက်ဆင်းသော ခဏ | 5 | stock |
| paccanubhoti | ခံစားသည် | 2 | pi-2 |
| Paccanīyagaṇanā | အငြင်းပြ ပုံစံ၏ ရေတွက်ချက် | 1 | order |
| Paccanīyaṃ | အငြင်းပြ ပုံစံ | 3 | order |
| Paccanīyuddhāro | အငြင်းပြ ပုံစံအတွက် ထုတ်နုတ်ချက် | 1 | headlex |
| Paccanīyānulomaṃ | အငြင်းပြ အဟုတ်ပြ ပုံစံ | 6 | order |
| paccavekkhanti | ပြန်လည် ဆင်ခြင်သည် | 3 | terms |
| paccavekkhati | ပြန်လည် ဆင်ခြင်သည် | 4 | terms |
| Paccayaniddeso | အကြောင်းများ၏ အကျယ် ဖော်ပြချက် | 2 | headlex |
| Paccayapaccanīyaṃ | အကြောင်း အငြင်းပြ ပုံစံ | 12 | order |
| Paccayapaccanīyānulomaṃ | အကြောင်း အငြင်းပြ အဟုတ်ပြ ပုံစံ | 9 | order |
| Paccayavāro | အကြောင်းပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက် | 2 | vara |
| paccayo | အကြောင်း | 37 | frame |
| paccayā | ကြောင့် | 1 | pi-2 |
| Paccayānulomapaccanīyaṃ | အကြောင်း အဟုတ်ပြ အငြင်းပြ ပုံစံ | 9 | order |
| Paccayānulomaṃ | အကြောင်း အဟုတ်ပြ ပုံစံ | 20 | order |
| pacchimānaṃ | နောက်နောက် | 4 | stock |
| pacchājātapaccayena | နောက်မှ ဖြစ်ပေါ်ခြင်းဟူသော အကြောင်း | 2 | cond |
| pacchājātapaccayo | နောက်မှ ဖြစ်ပေါ်ခြင်းဟူသော အကြောင်း | 3 | cond |
| pacchājātapaccayā | နောက်မှ ဖြစ်ပေါ်ခြင်းဟူသော အကြောင်းကြောင့် | 6 | cond |
| pacchājātā | နောက်မှ ဖြစ်ပေါ်သော | 1 | stock |
| pahīne | ပယ်ပြီးသော | 6 | lex |
| pakatūpanissayo | ပကတိ အားကြီးသော အမှီ | 9 | terms |
| Pakiṇṇakaghaṭanā | အထွေထွေ ပေါင်းစပ်ချက် | 4 | headlex |
| palapati | ပြောသည် | 1 | lex |
| paradāraṃ | သူတစ်ပါး၏ မယား | 1 | lex |
| parihīne | ဆုတ်ယုတ်သွားသော | 2 | terms |
| paripanthe | လမ်း | 1 | pi-5 |
| paripuṇṇaṃ | ပြည့်စုံသော | 2 | frame |
| paritāpeti | ပြင်းစွာ ပူပန်စေသည် | 2 | frame |
| pariyiṭṭhimūlakaṃ | ရှာမှီးခြင်းကို အရင်းခံသော | 2 | lex |
| patthanaṃ | တောင့်တခြင်း | 2 | terms |
| patthanāya | တောင့်တခြင်း | 1 | terms |
| Pañcakaṃ | ငါးမျိုးတွဲ | 2 | count |
| pañcamūlakaṃ | အကြောင်း ငါးခုကို အခြေခံခြင်း | 4 | count |
| Pañcamūlakādikā | အကြောင်း ငါးခုကို အခြေခံခြင်း စသည် | 1 | count |
| Pañhāvārassa | ပြဿနာအလိုက် ဖော်ပြချက် | 4 | vara |
| Pañhāvāro | ပြဿနာအလိုက် ဖော်ပြချက် | 4 | vara |
| paññaṃ | ပညာ | 2 | terms |
| paṭicca | မှီ၍ | 40 | frame |
| paṭisandhikkhaṇe | ပဋိသန္ဓေ နေသော ခဏ | 15 | stock |
| Paṭisandhikkhaṇe | ပဋိသန္ဓေ နေသော ခဏ | 15 | stock |
| Paṭṭhānapāḷi | အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ | 2 | frame |
| paṭṭhānavaraṃ | မြတ်သော အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ | 4 | frame |
| phalasamāpattiyā | ဖိုလ်သမာပတ် | 6 | terms |
| phalassa | ဖိုလ် | 2 | terms |
| phalā | ဖိုလ် | 4 | terms |
| pharusaṃ | ကြမ်းတမ်းသော စကား | 1 | pi-4 |
| Phoṭṭhabbāyatanaṃ | အထိအတွေ့ အာရုံခံ နယ်ပယ် | 8 | terms |
| pisuṇaṃ | ကုန်းတိုက်သော စကား | 1 | pi-4 |
| pitaraṃ | အဖ | 1 | pi-2 |
| pubbe | ရှေး | 3 | terms |
| pubbenivāsānussatiñāṇassa | ရှေးဘဝများကို အဖန်ဖန် အောက်မေ့နိုင်သော ဉာဏ် | 15 | terms |
| purejātapaccayena | ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်းဟူသော အကြောင်း | 3 | cond |
| purejātapaccayo | ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်းဟူသော အကြောင်း | 3 | cond |
| purejātapaccayā | ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်းဟူသော အကြောင်းကြောင့် | 9 | cond |
| purejāte | ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်းဟူသော အကြောင်း | 4 | cond |
| Purimā | ရှေးရှေး | 2 | stock |
| purimā | ရှေးရှေး | 6 | stock |
| pāṇaṃ | သတ္တဝါ | 3 | pi-5 |
| Rasāyatanaṃ | အရသာ အာရုံခံ နယ်ပယ် | 8 | terms |
| rāgaṃ | ရာဂ | 2 | terms |
| rāgo | ရာဂ | 4 | terms |
| Rūpajīvitindriyaṃ | ရုပ် အသက်၏ စွမ်းရည် | 2 | terms |
| rūpaṃ | ရုပ် | 1 | stock |
| Rūpino | ရုပ် ဖြစ်သော | 1 | stock |
| rūpino | ရုပ် ဖြစ်သော | 1 | stock |
| rūpānaṃ | ရုပ် | 41 | stock |
| rūpāyatanaṃ | အဆင်းအရောင် အာရုံခံ နယ်ပယ် | 2 | terms |
| Rūpāyatanaṃ | အဆင်းအရောင် အာရုံခံ နယ်ပယ် | 6 | terms |
| saddhaṃ | ယုံကြည်မှု | 2 | terms |
| saddhāpañcamakesu | ယုံကြည်မှု စသော ငါးပါး | 1 | ctx |
| saddhāya | ယုံကြည်မှု | 1 | terms |
| Saddāyatanaṃ | အသံ အာရုံခံ နယ်ပယ် | 4 | terms |
| sahajāta | အတူ ပေါ်ပေါက်ခြင်း | 13 | cond |
| Sahajātaghaṭanā | အတူ ပေါ်ပေါက်ခြင်းဟူသော အကြောင်း၏ ပေါင်းစပ်ချက် | 2 | cond |
| sahajātapaccayena | အတူ ပေါ်ပေါက်ခြင်းဟူသော အကြောင်း | 17 | cond |
| sahajātapaccayo | အတူ ပေါ်ပေါက်ခြင်းဟူသော အကြောင်း | 3 | cond |
| Sahajātapaccayo | အတူ ပေါ်ပေါက်ခြင်းဟူသော အကြောင်း | 3 | cond |
| sahajātapaccayā | အတူ ပေါ်ပေါက်ခြင်းဟူသော အကြောင်းကြောင့် | 15 | cond |
| sahajāte | အတူ ပေါ်ပေါက်ခြင်းဟူသော အကြောင်း | 22 | cond |
| sahajāto | အတူ ပေါ်ပေါက်သော | 1 | term |
| sahajātā | အတူ ပေါ်ပေါက်သော | 3 | stock |
| sahajātādhipati | အတူ ပေါ်ပေါက်သော အကြီးအမှူး | 4 | terms |
| Sahajātādhipati | အတူ ပေါ်ပေါက်သော အကြီးအမှူး | 2 | terms |
| Saindriya | စွမ်းရည်ဟူသော အကြောင်း … ပါဝင်သော | 1 | cond |
| sajjhāyamaggena | သရဇ္ဈာယ်သည့် နည်းလမ်း | 2 | frame |
| samanantara | ကောင်းစွာ ချက်ချင်း နောက်၌ ဖြစ်စေခြင်း | 4 | cond |
| samanantarapaccayena | ကောင်းစွာ ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းဟူသော အကြောင်း | 6 | cond |
| samanantarapaccayo | ကောင်းစွာ ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းဟူသော အကြောင်း | 3 | cond |
| Samanantarapaccayo | ကောင်းစွာ ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းဟူသော အကြောင်း | 3 | cond |
| Samanantarapaccayoti | ကောင်းစွာ ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းဟူသော အကြောင်း | 1 | cond |
| samanantarapaccayā | ကောင်းစွာ ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းဟူသော အကြောင်းကြောင့် | 17 | cond |
| Samanantarapaccayā | ကောင်းစွာ ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းဟူသော အကြောင်းကြောင့် | 2 | cond |
| samanantare | ကောင်းစွာ ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းဟူသော အကြောင်း | 18 | cond |
| samanantarā | ကောင်းစွာ ချက်ချင်း နောက် | 1 | frame |
| sammāsambuddhassa | အမှန်ကို ကိုယ်တိုင် အပြည့်အဝ သိမြင်တော်မူသော ဘုရားရှင် | 1 | frame |
| sampayutta | ယှဉ်တွဲခြင်း | 1 | cond |
| Sampayutta | ယှဉ်တွဲခြင်း | 1 | cond |
| sampayuttacittasamaṅgissa | ယှဉ်တွဲသော စိတ်နှင့် ပြည့်စုံသူ | 11 | term |
| sampayuttakānaṃ | ယှဉ်တွဲသော | 17 | stock |
| sampayuttapaccayena | ယှဉ်တွဲခြင်းဟူသော အကြောင်း | 4 | cond |
| sampayuttapaccayo | ယှဉ်တွဲခြင်းဟူသော အကြောင်း | 2 | cond |
| sampayuttapaccayā | ယှဉ်တွဲခြင်းဟူသော အကြောင်းကြောင့် | 6 | cond |
| sampayuttaṃ | ယှဉ်တွဲသော | 9 | stock |
| sampayutto | ယှဉ်တွဲသော | 18 | stock |
| sampayuttādhipati | ယှဉ်တွဲသော အကြီးအမှူး | 2 | term |
| samphaṃ | အကျိုးမဲ့ | 1 | pi-5 |
| samudāciṇṇe | ဖြစ်ခဲ့ဖူးသော | 3 | lex |
| samādiyati | ဆောက်တည်သည် | 4 | lex |
| samādiyitvā | ဆောက်တည်၍ | 16 | pi-2 |
| samāpattiṃ | သမာပတ် | 3 | stock |
| sandhiṃ | အိမ် | 1 | pi-5 |
| Sattakaṃ | ခုနစ်မျိုးတွဲ | 1 | count |
| saṃkhittaṃ | အကျဉ်းချုပ် | 18 | frame |
| saṃkhittā | အကျဉ်းချုပ် | 1 | frame |
| Saṃsaṭṭhavāro | ရောနှောခြင်းအလိုက် ဖော်ပြချက် | 2 | vara |
| saṃsaṭṭho | ရောနှောသော | 1 | pi-2 |
| saṅghaṃ | သံဃာ | 6 | terms |
| Saṅkhyāvāro | ရေတွက်ခြင်းအလိုက် ဖော်ပြချက် | 4 | vara |
| Sotaviññāṇadhātu | နား သိစိတ် ဓာတ် | 2 | terms |
| Sotāyatanaṃ | နား အာရုံခံ နယ်ပယ် | 20 | terms |
| Suddhaṃ | ရိုးရိုး | 8 | headlex |
| sukhasahagatassa | သာယာမှုနှင့်အတူ ဖြစ်သော | 2 | terms |
| Sukhasahagataṃ | သာယာမှုနှင့်အတူ ဖြစ်သော | 1 | terms |
| sukhasahagataṃ | သာယာမှုနှင့်အတူ ဖြစ်သော | 1 | terms |
| Sukhāya | သာယာသော | 6 | pi-2 |
| sukhāya | သာယာသော | 3 | pi-2 |
| sutaṃ | အကြားအမြင် | 2 | terms |
| Sādhipati | အကြီးအမှူးဟူသော အကြောင်း … ပါဝင်သော | 1 | cond |
| Sāmaññaghaṭanā | သာမန် ပေါင်းစပ်ချက် | 4 | headlex |
| sīlaṃ | သီလ | 6 | terms |
| tathāgatassa | မြတ်စွာဘုရား | 1 | lex |
| taṃsampayuttakā | ထိုအရာနှင့် ယှဉ်တွဲသော | 2 | stock |
| taṃsampayuttakānañca | ထိုအရာနှင့် ယှဉ်တွဲသော | 52 | base:stock |
| Tevīsakaṃ | နှစ်ဆယ့်သုံးမျိုးတွဲ | 1 | count |
| tevīsatimūlakaṃ | အကြောင်း နှစ်ဆယ့်သုံးခုကို အခြေခံခြင်း | 1 | count |
| Tikapaṭṭhānaṃ | သုံးမျိုးတွဲတို့၏ အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ | 1 | title |
| tikañca | သုံးမျိုးတွဲ | 4 | count |
| tikañceva | သုံးမျိုးတွဲ | 4 | count |
| Tikaṃ | သုံးမျိုးတွဲ | 9 | count |
| Timūlakaṃ | အကြောင်း သုံးခုကို အခြေခံခြင်း | 1 | count |
| timūlakaṃ | အကြောင်း သုံးခုကို အခြေခံခြင်း | 3 | count |
| tiṭṭhati | ဓားပြ တိုက်သည် | 1 | stock |
| uddhaccasahagate | ယောက်ယက်ခတ်မှုနှင့်အတူ ဖြစ်သော | 3 | terms |
| uddhaccaṃ | ယောက်ယက်ခတ်မှု | 2 | terms |
| upanissaya | အားကြီးသော အမှီ | 3 | cond |
| Upanissaya | အားကြီးသော အမှီ | 1 | cond |
| upanissayapaccayena | အားကြီးသော အမှီဟူသော အကြောင်း | 35 | cond |
| upanissayapaccayo | အားကြီးသော အမှီဟူသော အကြောင်း | 5 | cond |
| Upanissayapaccayo | အားကြီးသော အမှီဟူသော အကြောင်း | 5 | cond |
| upanissayapaccayā | အားကြီးသော အမှီဟူသော အကြောင်းကြောင့် | 15 | cond |
| Upanissayapaccayā | အားကြီးသော အမှီဟူသော အကြောင်းကြောင့် | 1 | cond |
| upanissaye | အားကြီးသော အမှီဟူသော အကြောင်း | 22 | cond |
| upanissāya | အားကြီးစွာ မှီ၍ | 3 | terms |
| upapatticittassa | ပြန်လည် ဖြစ်ပေါ်ခြင်း စိတ် | 4 | terms |
| uposathakammaṃ | ဥပုသ်ကို စောင့်ထိန်းသည် | 10 | stock |
| uppajjanti | ဖြစ်ပေါ်သည် | 7 | verb |
| uppajjati | ဖြစ်ပေါ်သည် | 18 | verb |
| uppajjeyya | ဖြစ်ပေါ်နိုင်သည် | 113 | verb |
| uppajjeyyuṃ | ဖြစ်ပေါ်နိုင်သည် | 95 | verb |
| uppādeti | ဖြစ်စေသည် | 9 | lex |
| upādārūpānaṃ | မူလဓာတ်ကြီးတို့ကို မှီ၍ ဖြစ်သော ရုပ် | 8 | stock |
| Vatthuṃ | မှီရာ ဝတ္ထု | 2 | stock |
| vatthuṃ | မှီရာ ဝတ္ထု | 2 | stock |
| Vedanāttikaṃ | ခံစားမှု သုံးမျိုးတွဲ | 2 | headlex |
| vedanāya | ခံစားမှု | 260 | pi-2 |
| Vibhaṅgavāro | ခွဲခြမ်းစိတ်ဖြာခြင်းအလိုက် ဖော်ပြချက် | 3 | vara |
| vicikicchā | ယုံမှားမှု | 6 | terms |
| vicikicchāsahagate | ယုံမှားမှုနှင့်အတူ ဖြစ်သော | 5 | terms |
| vigatapaccayena | ပျောက်ကွယ်ခြင်းဟူသော အကြောင်း | 4 | cond |
| vigatapaccayo | ပျောက်ကွယ်ခြင်းဟူသော အကြောင်း | 5 | cond |
| Vigatapaccayoti | ပျောက်ကွယ်ခြင်းဟူသော အကြောင်း | 1 | cond |
| vigatapaccayā | ပျောက်ကွယ်ခြင်းဟူသော အကြောင်းကြောင့် | 16 | cond |
| vigate | ပျောက်ကွယ်ခြင်းဟူသော အကြောင်း | 18 | cond |
| vikkhambhite | ခွာထားပြီးသော | 6 | lex |
| vipassanaṃ | ထိုးထွင်းသိမြင်ခြင်း | 2 | lex |
| vipassati | ထိုးထွင်း၍ ရှုသည် | 3 | terms |
| vippayuttapaccayena | ကင်းကွာခြင်းဟူသော အကြောင်း | 3 | cond |
| vippayuttapaccayo | ကင်းကွာခြင်းဟူသော အကြောင်း | 3 | cond |
| vippayuttapaccayā | ကင်းကွာခြင်းဟူသော အကြောင်းကြောင့် | 8 | cond |
| vippayutte | ကင်းကွာခြင်းဟူသော အကြောင်း | 4 | cond |
| vippaṭisārissa | နောင်တ ရသူ | 2 | terms |
| Vipākamanodhātu | ကံ၏ အကျိုး ဖြစ်သော မနော ဓာတ် | 1 | terms |
| vipākamanodhātuyā | ကံ၏ အကျိုး ဖြစ်သော မနော ဓာတ် | 5 | terms |
| vipākamanoviññāṇadhātu | ကံ၏ အကျိုး ဖြစ်သော မနော သိစိတ် ဓာတ် | 5 | terms |
| vipākapaccayena | ကံ၏ အကျိုးဟူသော အကြောင်း | 6 | cond |
| vipākapaccayo | ကံ၏ အကျိုးဟူသော အကြောင်း | 3 | cond |
| Vipākapaccayo | ကံ၏ အကျိုးဟူသော အကြောင်း | 3 | cond |
| vipākapaccayā | ကံ၏ အကျိုးဟူသော အကြောင်းကြောင့် | 9 | cond |
| vipāke | ကံ၏ အကျိုးဟူသော အကြောင်း | 2 | cond |
| vipāko | ကံ၏ အကျိုး ဖြစ်သော | 1 | stock |
| vipākā | ကံ၏ အကျိုး ဖြစ်သော | 1 | stock |
| vipākānaṃ | ကံ၏ အကျိုး ဖြစ်သော | 4 | stock |
| vitthāretabbaṃ | အကျယ် ချဲ့ရမည့် | 4 | frame |
| vitthāretabbo | အကျယ် ချဲ့ရမည့် | 3 | frame |
| vitthāretabbā | အကျယ် ချဲ့ရမည့် | 1 | frame |
| viññāṇañcāyatanassa | အဆုံး မရှိသော သိစိတ် နယ်ပယ် | 4 | terms |
| vodānassa | စင်ကြယ်ခြင်း စိတ် | 3 | terms |
| vuṭṭhahantassa | ထမြောက်နေသူ | 1 | lex |
| vuṭṭhahitvā | ထ၍ | 8 | terms |
| vuṭṭhānassa | ထမြောက်ခြင်း စိတ် | 3 | terms |
| vācanāmaggena | ရွတ်ဆိုသည့် နည်းလမ်း | 2 | frame |
| yathākammūpagañāṇassa | ကံအားလျော်စွာ ဖြစ်ပေါ်ပုံကို သိသော ဉာဏ် | 3 | terms |
| ādiyati | ယူသည် | 1 | lex |
| āhāra | အာဟာရ | 3 | cond |
| Āhāra | အာဟာရ | 1 | cond |
| āhārapaccayena | အာဟာရဟူသော အကြောင်း | 5 | cond |
| āhārapaccayo | အာဟာရဟူသော အကြောင်း | 3 | cond |
| āhārapaccayā | အာဟာရဟူသော အကြောင်းကြောင့် | 9 | cond |
| āhāre | အာဟာရဟူသော အကြောင်း | 17 | cond |
| āhāro | အာဟာရ | 1 | stock |
| Ākiñcaññāyatanaṃ | ဘာမျှ မရှိသော နယ်ပယ် | 2 | terms |
| Ākāsānañcāyatanaṃ | အဆုံး မရှိသော ဟင်းလင်းပြင် နယ်ပယ် | 1 | terms |
| ārabbha | အာရုံပြု၍ | 4 | frame |
| ārammaṇa | အာရုံ | 2 | cond |
| ārammaṇapaccayena | အာရုံဟူသော အကြောင်း | 21 | cond |
| ārammaṇapaccayo | အာရုံဟူသော အကြောင်း | 3 | cond |
| Ārammaṇapaccayo | အာရုံဟူသော အကြောင်း | 3 | cond |
| ārammaṇapaccayā | အာရုံဟူသော အကြောင်းကြောင့် | 37 | cond |
| Ārammaṇapaccayā | အာရုံဟူသော အကြောင်းကြောင့် | 1 | cond |
| ārammaṇe | အာရုံဟူသော အကြောင်း | 17 | cond |
| ārammaṇādhipati | အာရုံ အကြီးအမှူး | 2 | terms |
| Ārammaṇādhipati | အာရုံ အကြီးအမှူး | 1 | terms |
| ārammaṇūpanissayo | အာရုံဖြင့် အားကြီးသော အမှီ | 4 | terms |
| āsevana | အလေ့အကျင့် ပြုခြင်း | 2 | cond |
| Āsevana | အလေ့အကျင့် ပြုခြင်း | 1 | cond |
| āsevanapaccayena | အလေ့အကျင့် ပြုခြင်းဟူသော အကြောင်း | 5 | cond |
| āsevanapaccayo | အလေ့အကျင့် ပြုခြင်းဟူသော အကြောင်း | 3 | cond |
| Āsevanapaccayo | အလေ့အကျင့် ပြုခြင်းဟူသော အကြောင်း | 3 | cond |
| āsevanapaccayā | အလေ့အကျင့် ပြုခြင်းဟူသော အကြောင်းကြောင့် | 8 | cond |
| Āsevanapaccayā | အလေ့အကျင့် ပြုခြင်းဟူသော အကြောင်းကြောင့် | 1 | cond |
| āsevane | အလေ့အကျင့် ပြုခြင်းဟူသော အကြောင်း | 12 | cond |
| ātāpeti | ပူပန်စေသည် | 2 | frame |
| Āvajjanā | စိတ်ညွတ်ခြင်း | 1 | terms |
| āvajjanāya | စိတ်ညွတ်ခြင်း | 4 | terms |
