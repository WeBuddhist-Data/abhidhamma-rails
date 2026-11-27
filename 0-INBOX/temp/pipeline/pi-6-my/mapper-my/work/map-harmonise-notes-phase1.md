# pi-6 Burmese keyword mapping, PHASE 1: keyword ambiguities and text inconsistencies

Sample chapters preamble, 1-mulayamaka, 2-01-khandhayamaka (map_sample.py), plus what the whole-book frame-coverage
check (frame_coverage.py) showed. The translation was not changed. Rules R1-R9: map-table.md.

## A. Text inconsistencies (for the rails step)

A1. **«yassa cittassa anantarā»** has two Burmese forms in the book: «အကြင်စိတ်၏ ချက်ချင်း နောက်၌» (correlative, as the
    sample's «အကြင်သူအား»: 5-01 … 5-03, 9-01 … 9-03, 10-09 … 10-11; 166 places) and «မိမိ စိတ်၏ ချက်ချင်း နောက်၌» ("one's
    own citta": 6-01, 6-02, 10-05 … 10-07, 10-12; 92 places). Same Pāli, same frame. The mapping takes each segment's
    word (a phase-2 keyword «yassa» there would get «အကြင်» or (no direct equivalent) by pi-5 Q7); the rails step
    should choose one.
A2. **kāmāvacarānaṃ pacchimacittaṃ** (6-01 ^6-6-39, 6-02 ^6-6-88): «ကာမဘုံနှင့် ဆိုင်သော နောက်ဆုံး စိတ်» (the kāma-sphere
    last citta, an adjective), while the same genitive plural elsewhere is the beings «ကာမဘုံ၌ ရှိသူတို့» (30 places).
    Grammatically the Pāli is «the last citta of the kāma beings»; the mapping follows the text («ကာမဘုံနှင့် ဆိုင်သော»).
A3. **Colophons of the vāras**: «Uddesavāro / Niddesavāro niṭṭhito» = «“အကျဉ်း / အကျယ် ဖော်ပြချက်” ပြီးဆုံးပြီ» (no
    «…အလိုက်» and no word for vāro), while the headings «Mūlavāro» etc. are «Xအလိုက် ဖော်ပြချက်». Consistent with
    my6-zeroshot-terms §2 (approved), noted because the keyword vāro has no word of its own there.
A4. **Heading IDs**: in the keyword files the headings stand in ID order (e.g. ^6-2-18-0 «Pavatti 2. nirodhavāro»
    after ^6-2-18), not in text order; the chapter files are in text order. No effect on the mapping (each segment is
    looked up by its ID), noted for the assembly.
A5. **Keyword gaps** (no effect on the mapping): ^6-2-79 / ^6-2-81 key «pañcavokārā / pañcavokāraṃ» but not the first
    member «Catuvokārā / catuvokāraṃ» of «Catuvokārā pañcavokārā cavantānaṃ» (the shared «…ဘဝမှ» goes with both).
A6. Source slips already logged by the zero-shot run (notes-sample.md): ^6-2-36 «.» for «?», ^6-2-61 «(Ka)» for «(Kha)»,
    ^6-2-111 «nirujjhattha», ^6-1-99 «nāmahetū ti», ^6-2-44 split line. The keywords of these segments map normally
    (nirujjhattha is read as the past by R2, the slip ending «attha»).

## B. Keyword ambiguities and mapping choices (sample)

B1. **Two shapes of the root predicates** (R4): the text builds ekamūla with «ရှိ» (possessive: «တူညီသော အမြစ် ရှိကြ»)
    and aññamaññamūla with the copula «ဖြစ်ကြ» («အချင်းချင်း အမြစ် ဖြစ်ကြ»), so ekamūlā = «တူညီသော အမြစ် ရှိသော»
    (rule 3) but aññamaññamūlā = «အချင်းချင်း အမြစ်» (rule 2). Both follow the approved text; a reviewer may want one
    shape.
B2. **abyākata as a root base** is adjectival («ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော အမြစ်») while kusala / akusala /
    nāma are genitives («ကုသိုလ်၏ အမြစ်»): the text's construction (as pi-1 abyākatahetu), kept.
B3. **upapajjantānaṃ** = «ပြန်လည် ဖြစ်ပေါ်ဆဲသူ» (agent noun, P6), but «ပြန်လည် ဖြစ်ပေါ်ဆဲ» where the text puts the
    participle before «နောက်ဆုံး ဘဝ ရှိသူ» (^6-2-80 …): one form per segment, the text's.
B4. **pañcavokārānaṃ** = «… ဘဝ၌ ရှိသူ» (beings), «… ဘဝ၌ ရှိသော» before «အခြားသူ» (Itaresaṃ pañcavokārānaṃ): R5.
B5. **asaññasatta**: the plane (acc. / loc. / abl.) «အသညသတ် ဘုံ», the beings (gen. pl.) «အသညသတ်» (pi-2); the ablative
    «Asaññasattā cavantānaṃ» is the plane («အသညသတ် ဘုံမှ»), not the pi-2 nominative plural «Asaññasattā» (beings).
B6. **hetu / paccaya in the hetuvāra** (R4, departure 1 of the approved sample): hetu «အကြောင်း», paccaya «အထောက်အပံ့»
    (each synonym its own word); pi-1 / pi-2 hetu «အမြစ်», pi-5 paccayo «အကြောင်း» are not taken (map-table.md, values
    different from pi-1 … pi-5).
B7. **Samuṭṭhānāhārārammaṇā** (one Pāli word, three list items «ဖြစ်ပေါ်လာရာ၊ အာဟာရ၊ အာရုံ») = «ဖြစ်ပေါ်လာရာ အာဟာရ
    အာရုံ» (rule 6: the «၊» goes); the variant «[samuṭṭhānāhārārammaṇaṃ (ka.)]» has no keyword.
B8. **Answers**: Āmantā «ဟုတ်ပါသည်» whole (Q2), Natthi «မရှိသည်» (pi-1 … pi-5, rule 4), No «မဟုတ်ပါ» whole (R9, not in the
    sample): the pi-5 split is kept (Natthi is a verb, Āmantā / No are answer particles).
B9. **Viññāṇañca** (= viññāṇaṃ + ca) is a homograph of the pi-1 / pi-5 key viññāṇañca (of viññāṇañcāyatana «အဆုံး
    မရှိသော သိစိတ်»); R1 maps it to «သိစိတ်». Phase 2 (ch. 3 āyatana, ch. 7 anusaya planes) must keep the two apart:
    the āyatana name is the keyword «viññāṇañcāyatana…», never the bare «viññāṇañca».
B10. **nāma** = «စိတ်ပိုင်း» (mentality, ch. 1); pi-5 «nāmā = အမည်» is "name" (another sense, rule 11).

## C. For phase 2 (from the frame-coverage check)

C1. The frame keywords of the whole book (200 most frequent) reach 100% presence with the module alone; the groups the
    module does not yet cover (frame-coverage.md, «Whole-book dry run») need chapter tables: sānusaya / niranusaya,
    sacakkhuka-type persons, X-sampayutta / X-vippayutta citta compounds, avitakka-avicāra, abhisametāvī, the cited
    forms Yassakampi / yassayatthakampi, tesaṃyeva.
C2. The stem fallback (S1) gives present but unchecked values (88 keywords book-wide, frame-coverage.md); phase 2
    should look at them (e.g. Aṭṭhamako «အဋ္ဌမ»).
C3. Planes coordinated with one shared ending («သိမ်မွေ့သော ရုပ်ဘုံနှင့် ရုပ်မရှိသော ဘုံ၌ ရှိသူတို့») give the first plane
    «P … ရှိသူ» (R5); the second plane gets «P၌ ရှိသူ» as usual.
