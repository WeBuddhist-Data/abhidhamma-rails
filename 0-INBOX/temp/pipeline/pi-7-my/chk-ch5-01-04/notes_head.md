# pi-7 part 5, 5-01 … 5-04 (anuloma tikatika / dukaduka, paccanīya tika / duka): Burmese zero-shot notes

PROGRESS: DONE (2026-11-24). Written to AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters/:
5-01-anuloma-tikatika.md, 5-02-anuloma-dukaduka.md, 5-03-paccaniya-tika.md, 5-04-paccaniya-duka.md.
(Check results: see the end of this file.)

## Files
- make_ch5-01-04.py: generator. Engines (read-only, imported on their own copies of my7_formulas / make_sample,
  never run as scripts): world A = make_ch3-09.py (→ 3-03-06 → 3-01-02 → 2-03-06: PRIMARY 1-01, FALLBACK 1-03-05),
  the engine for 5-01, 5-03 and the A-dyads of 5-02 / 5-04; world B = make_ch4-01.py (→ 3-07-08-10 → 3-01-02) for
  the nīvaraṇa / parāmāsa / upādāna / kilesa / piṭṭhiduka parts; value sources only: make_ch2-07-11.py,
  make_ch2-12-17.py. No file of the sample or of another group is edited; no other group's main block runs.
  `--dev`, `--dump`, `--slips`, `--out DIR`.
- check_ch5-01-04.py: checker (structure, conditions and numbers from check_ch4-01.py with its typed tables; its own
  term-chain reader and composition; identity, tables, reuse; `--mutate`, `--pe`, `--groups`).
- chk-ch5-01-04/: scratch (dev output, probes, the full table dump notes_tables.md).

## How the chapters are run
- Each chapter is cut at its part headings (5-01 «1-1. Kusalattika-vedanāttikaṃ» …, 5-02 «1-1. Hetuduka-sahetukadukaṃ»
  … «83-1. Piṭṭhiduka-hetudukaṃ», 5-03 «Kusalattikaṃ» …, 5-04 «Hetudukaṃ» … «Saraṇadukaṃ»); a part runs with only
  its own terms active.
- Atoms: every triad / dyad term of the finished groups, by its Pāli surface (a-, u-, i-stems, and the indeclinable
  «bahiddhā» / «upādā», whose case is the neighbour's). Their Burmese is the finished groups' (pi-1 final Mātikā).
- A term chain (two terms on one noun, or a «ceva … ca» term, or both) is rewritten into ONE synthetic a-stem term
  whose Burmese is:
  * two terms side by side (triad × triad, dyad × dyad, «na-X» sixth dyads): the qualifiers stacked «A၊ B N»
    (coordinator: the stacking pattern of 2-01-02 / 2-07-11 / 3-01-02), e.g.
    «Kusalaṃ sukhāya vedanāya sampayuttaṃ dhammaṃ» = «ကုသိုလ်၊ သာယာသော ခံစားမှုနှင့် ယှဉ်တွဲသော သဘောတရား»;
  * a pair that is itself a pi-1 dyad term keeps that term (identity with 3-01 … 4-01): «nahetu sahetuko» =
    «အမြစ် မဟုတ်သော်လည်း အမြစ် ရှိသော», «nahetu ahetuko» = «အမြစ် မဟုတ်၊ အမြစ် မရှိသော» (3-01), the sixth dyad of each
    cluster («āsavavippayutto sāsavo / anāsavo» … 3-03-06 forms, coordinator), the «X ceva Y ca» / «Y ceva no ca X»
    dyads (3-01 … 4-01);
  * «na-X» (paccanīya) = the Burmese of X negated (free «na» = «… မဟုတ်»): «…သော» → «…သည် မဟုတ်သော»
    (pi-1 «na pītisahagatā» «ပီတိနှင့်အတူ ဖြစ်သည် မဟုတ်သော»); «… ပယ်ရမည့်» → «… ပယ်ရမည် မဟုတ်သော» (pi-1 «na
    dassanena pahātabbā»); «X ဖြစ်သော» (being X, a noun) → «X မဟုတ်သော» (pi-1 «hetū / na hetū» «အမြစ် ဖြစ်သော / အမြစ်
    မဟုတ်သော»; so «naāsava» = «noāsava» «စိတ်အစွန်းအထင်း မဟုတ်သော», «nacetasika» = «acetasika» «စိတ်၏ အဖော် မဟုတ်သော»);
    a noun → «X မဟုတ်သော» («nakusala» «ကုသိုလ် မဟုတ်သော»). Double negatives «na nahetu», «nanoāsava», «nanakenaci
    viññeyya», «nanapītisahagata» … are the rule applied twice («အမြစ် မဟုတ်သည် မဟုတ်သော»), as the Pāli writes them.
  * a negated «ceva … ca» term («nahetuñceva naahetukañca», «naanāsavo ceva nano ca āsavo»): its two members stacked.
- Two side-by-side terms are one chain only when their endings agree (the Pāli «Kusalo vipākadhammadhammo
  kusalassa …» is two chains).
- «-dhammadhamma» terms hold their noun: «Navipākadhammadhammaṃ paṭicca …» gets «သဘောတရား» after the term (as 1-03-05).
- Coordination «A-añca B-añca dhammaṃ» / «A-o ca B-o ca dhammā» stays the engine's («A သဘောတရားနှင့် B သဘောတရား»);
  in 5-04 the closer «ca» of a negated «ceva» term is also the coordinator when another term follows (or it closes a
  coordination); in 5-02 a «ceva» term followed by a term stacks with it («Hetuñceva sahetukañca hetuṃ dhammaṃ»).
- «… uppajjati hetupaccayā ekaṃ.» (a count after the condition without «…»): «… ဖြစ်ပေါ်သည် တစ်ခု။» (as «hetupaccayā
  (ekaṃ)» «… ဖြစ်ပေါ်သည် (တစ်ခု)», without the brackets the Pāli does not have).
- The notes (none of them is in a finished chapter) are composed from the finished groups' words: saṃkhittaṃ
  «အကျဉ်းချုပ်», sabbattha «နေရာတိုင်း၌», vitthāro «အကျယ် ချဲ့ခြင်း» (3-01), vitthāretabbaṃ «အကျယ် ချဲ့ရမည်»,
  «X-vārampi» «X ဖော်ပြချက်လည်း» (with «…sadisaṃ», «sabbattha vitthāro»; «…ကိုလည်း» before a verb), «X-vārepi»
  «X ဖော်ပြချက်၌လည်း», paṭiccavārasadisaṃ «မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူသည်» (+ verb: «… နှင့် တူအောင်
  …»), «yathā kusalattike pañhāvāraṃ evaṃ vitthāretabbaṃ» «ကုသိုလ် သုံးမျိုးတွဲ၌ ပြဿနာအလိုက် ဖော်ပြချက်အတိုင်း
  ထိုနည်းတူ အကျယ် ချဲ့ရမည်» (the 1-03 «yathā kusalattike gaṇanā, evaṃ gaṇetabbaṃ» pattern), evaṃ alone «ဤသို့»
  (2-03-06), vipākaṃ natthi «ကံ၏ အကျိုးဟူသော အကြောင်း မရှိ» (1-01). Each note is a placeholder for the engine.
- New numbers (5-01, 5-03): ekūnatiṃsa 29, tiṃsa 30, catuttiṃsa 34, pañcatiṃsa 35, chattiṃsa 36, sattatiṃsa 37;
  catuvīsa 24 as 2-12-17 (1-03-05 value).

## Coordinator decisions applied
- «Anulomaṃ.», the «Sahajātā –» label, asaññasattānaṃ and the heinous deeds do not occur in these chapters.
- The sixth-dyad forms are those of 3-03-06 (KNOWN_ADJ, read from world A / B).
- Stacking «A၊ B N» for two qualifiers on one noun (all four chapters).
- Supplied words: none beyond the engine's «သဘောတရား» after the «-dhammadhamma» compounds (the noun is in the
  compound).

## Source slips and unsure Pāli (translated as written unless stated)
- 5-04 ^7-58-37 «naasaññojaniyo ceva nanoasaññojano ca dhammo»: «nanoasaññojano» read as «nano ca saññojano» (the
  form of the same dyad in the same segment; «na-no-a-saññojana» is not a term). Logged by the generator.
- 5-04 ^7-58-39 «Saññojanavippayutto nasaññojaniyañca …»: the nominative read as the accusative
  «Saññojanavippayuttaṃ» (object of paṭicca; as the parallel ^7-58-33 / ^7-58-45). Logged by the generator.
- 5-02 ^7-56-17 / -18 «hetu hetu ceva sahetuko dhammo» (and «… hetusampayutto ca»): the first has no closing «ca»;
  read as the dyad term «hetu ceva sahetuko (ca)» (the Burmese is the same).
- 5-04 ^7-58-31 «noāsavo ceva naanāsavo ca …» inside the «na-» forms: as written («noāsava» = «စိတ်အစွန်းအထင်း
  မဟုတ်သော», which is also the Burmese of «naāsava» by the rule).
- 5-04 the paccanīya of the fourth / fifth dyads is written with the other dyads' terms («Nahetuñceva naahetukañca»,
  «Naāsavañceva naanāsavañca», «nano ca āsavo», «nanoāsavañca»): as written, members stacked.
- 5-02 7-1 «nakenaci viññeyyaṃ hetuṃ» (for «kenaci naviññeyyaṃ»): as written; the same Pāli in 5-04 is the
  paccanīya «na-kenaci viññeyya» «တစ်စုံတစ်ခုသော စိတ်ဖြင့် သိနိုင်သည် မဟုတ်သော», so both get that Burmese.
- 5-01 ^7-55-24 «Kusalaṃ anupādinnaanupādāniyaṃ dhammaṃ paṭicca kusalo anupādinnupādāniyo dhammo»: as written.
- 5-01 heading «Adukkhamasukhavedanāyasampayuttapadaṃ» (no «-āya»): the term «adukkhamasukhāya vedanāya sampayutta».
- 5-04 «nacittānuparivatti dhammo», «nacittasaṃsaṭṭhasamuṭṭhānānuparivatti dhammo» (short i): the term as usual.
- «naabyākata» «ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သည် မဟုတ်သော» (the rule on the pi-1 neither-nor): exact but heavy;
  worth a look by a reviewer (a lighter form would need a new rule for the neither-nor terms).
- 5-04 ^7-58-56 «(Paccanīyadukamattāni na vattabbaṃ dhammaṃ pūretuṃ nava nava pañhāni karotu.)»: «karotu» (3rd sg.
  imperative) «ပြုပါစေ»; «na vattabbaṃ dhammaṃ» as pi-1 vattabbaṃ «ခေါ်ဆို၍ ရ» negated.
