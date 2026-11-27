# pi-5 Burmese zero-shot SAMPLE: notes (preamble, 1-puggalakatha)

Status: DONE 2026-11-20, waiting for review. Brief: burmese-zeroshot-sample-brief.md. Not committed.
Source rule kept: translated from the Pāli only; no Burmese translation or nissaya opened, no web search; English
pi-5 zero-shot read for meaning only (first segments). pi-1 … pi-4 read only through their rails texts (FINAL).

## Files
- Output: `AI_translation/burmese/pi-5-burmese-plain-zeroshot_split_chapters/` preamble.md (3 segments, 3 lines),
  1-puggalakatha.md (269 segments, 430 lines: the whole Puggalakathā ^5-1-0 … ^5-238).
- `my5_formulas.py` (shared module), `make_sample.py` (generator + the Puggalakathā tables), `check_sample.py`
  (per-line check + reuse test), `terms_my5.py` (writes `my5-zeroshot-terms.md`).
- Read-only helpers (scratch, never used by the generator): kwic5.py / k.sh (search pi-1 … pi-4 final by Pāli),
  scratch/units.py (lists every unmatched unit), scratch/analyse.py.
- Run: `python3 -I -X utf8 make_sample.py` (writes both files), `check_sample.py`, `terms_my5.py`.

## Checks (final run)
- check_chapter_ids / check_text_pe / check_marks: OK for both files (chk-pe copies deleted afterwards).
- check_sample.py: A 2/2 regenerated identical; B1 433 lines; B2 1879 polarity marks; B3 81 number words; B4 272
  segments quote nesting; B5 964/964 occurrences of 111 recurring sentences identical; B6 78 table values;
  0 mismatches. Reuse test 1278 / 1278 identical (C1 topic names 438/438, C2 whole lines / headings 2/2,
  C3 95 reused terms, 838/838 occurrences).
- Mutation test: a dropped «မ» (polarity), a changed digit and a changed «ဟုတ်ပါသည်» are all caught.

## Method (for the later agents)
- my5_formulas builds its own index of the pi-1 … pi-4 rails texts (FINAL); every reused value is read (heads(),
  items()) or checked (witness()) at import, so the module stops if a final text drifts.
- Engine (translate_line): heading table; whole-line tables (LINES, verses / sutta lines); multi-sentence line
  frames (Tvaṃ ce pana …, Ese ce dunniggahite …, Na hevaṃ niggahetabbe. Tena hi …); otherwise the line is cut
  into sentences (at «. » / «? » / «! » before a capital or a quote, at even «"» parity, and after
  «vattabbe…pe… » / «Āmantā…pe… » before a small letter). Each sentence, with quotes and brackets removed, goes
  to SENT or to the FRAMES (generic «P-ti?» and «P…pe….» last). A frame slot is a proposition: prop_my() looks it
  up in PROP / RULES (canonical form: first letter small, final «ti» off, «…nti» -> «ṃ», long final vowel
  shortened) or cuts it at «, » / «; » / «… » into the longest known parts. Nothing matched = Miss, the run stops.
- Cl (a clause) keeps the final verb apart, so one table entry gives the statement (…သည် / မ…), the question
  (…သလော), the condition (…လျှင်), the bare series item and the «nanu» question (…သည် မဟုတ်လော). Quotation
  marks are set by depth («…» / ‹…› in table strings).
- Brackets are taken out before matching and put back into the Burmese sentence they came from: at its start
  (editorial notes, references before the question), after an ANCHOR word, at a slot ⟦b⟧ / ⟦n⟧, or before the
  final «။».
- Later kathās: add their propositions to the chapter's PROP table (or a RULE for a productive pattern), unique
  sentences to SENT / LINES, new nouns with add_noun(); the frames, answers, set names and clause forms are done.

## Main choices
- Book title Kathāvatthupāḷi = «အငြင်းပွားရာ အကြောင်းအရာများကို ဆွေးနွေးခြင်း» ("discussing the disputed
  points"; gerund pattern of the pi-2 / pi-4 titles); book end «“…” ကျမ်း ပြီးဆုံးပြီ။» (pi-1 … pi-3 pattern).
- Headings: kathā = «ဆွေးနွေးချက်» (Puggalakathā «ပုဂ္ဂိုလ်အကြောင်း ဆွေးနွေးချက်»); anuyoga = «…ကို စစ်ဆေးမေးမြန်းခြင်း»;
  saṃsandana = «နှိုင်းယှဉ်ခြင်း»; vagga = «ဝဂ်» (Kalyāṇavaggo paṭhamo = «ပထမ “ကောင်းမွန်သော” ဝဂ်»); section end
  «X niṭṭhitā» = «“X” ပြီးဆုံးပြီ။» (pi-1); a colophon repeating a section name = the name + «။».
- The proposition: saccikaṭṭhaparamatthena = «အမှန်တကယ် အဆုံးစွန် အနက်အားဖြင့်»; upalabbhati / nupalabbhati =
  «(ပုဂ္ဂိုလ်ကို) … တွေ့ရ(သည်)» / «… မတွေ့ရ»; «yo saccikaṭṭho paramattho, tato so puggalo …» = «အမှန်တကယ် အဆုံးစွန်
  အရာ ဖြစ်သည့်အတိုင်း ထိုပုဂ္ဂိုလ်ကို …» (no second «တွေ့ရ», so the polarity stays one per Pāli verb);
  saccikaṭṭho alone (headings, Vacanasodhana) = «အမှန်တကယ် အရာ».
- Frames: Āmantā «ဟုတ်ပါသည်။»; Na hevaṃ vattabbe «ဤသို့ မဆိုသင့်ပါ။»; vattabba always «ဆိုသင့်» / «မဆိုသင့်»
  (checked by script); Ājānāhi niggahaṃ / paṭikammaṃ «ချေပချက်ကို / ပြန်လှန် ချေပချက်ကို လက်ခံလော့။»;
  Hañci P, tena vata re vattabbe – "Q" «အကယ်၍ P…လျှင် ထို့ကြောင့် အမှန်ပင် ဤသို့ ဆိုသင့်သည် – “Q”။»;
  Yaṃ tattha vadesi – "…"ti micchā «ထိုအရာ၌ သင်ပြောသော စကား – “…”ဟူသည် မှားသည်။» (idaṃ te micchā «…ဟူသော
  ဤစကားသည် သင်၏ အမှား ဖြစ်သည်။»); No ce pana … «တစ်ဖန် အကယ်၍ ဤသို့ မဆိုသင့်လျှင် – “Q”၊ အမှန်ပင် ဤသို့လည်း
  မဆိုသင့် – “P”။»; the dash stays where the Pāli has it (the Burmese keeps the Pāli order «verb – quotation»).
  All frames are in terms §3 (rendered with P / Q by the real functions).
- Set names: -pañcaka / -catukka / aṭṭhaka- = «… ငါးပါးအစု / လေးပါးအစု / ရှစ်ပါးအစု»; niggaha «ချေပချက်», paṭikamma
  «ပြန်လှန် ချေပချက်», upanayana «ဆက်စပ် အသုံးချချက်», niggamana «နိဂုံးချုပ်ချက်»; Paṭhamo … Sattamo niggaho
  «ပထမ … သတ္တမ ချေပချက်»; Aṭṭhakaniggaho «ချေပချက် ရှစ်ပါးအစု» (aṭṭhaka = a set of eight, like pañcaka).
- sakavādī / paravādī = «မိမိဘက်» / «တစ်ဖက်သား»; [iminā lakkhaṇena …pucchā dassitā] = «[ဤအမှတ်အသားဖြင့် …၏ အမေးကို
  ပြထားသည်]»; ṭīkā oloketabbā «ဋီကာကို ကြည့်ပါ»; the (?) siglum «(မသေချာ)» (no «?» allowed); (bahūsu) «(အများစု၌)».
- Series «A…pe… B…pe… C-ti?»: every item takes the question form (each is an elided question); in a line ending
  «…pe….» without «ti?» the items are bare (neutral); before a later «, » part they are bare.
- Reused (pi-1 … pi-4 final, all witnessed; terms §11): the khandha / āyatana / dhātu / indriya names (pi-2 lists);
  taṃ jīvaṃ taṃ sarīraṃ / aññaṃ jīvaṃ aññaṃ sarīraṃ (pi-1 ^1-1105, also the pattern «Aနှင့် Bသည် တခြားစီ ဖြစ်» for
  every «aññaṃ A añño B»); sappaccaya, saṅkhata / asaṅkhata, sanidassana, sappaṭigha, nimitta, sassata (pi-1);
  upādāya «ကို မှီ၍», paññatti «သတ်မှတ်ချက်»; the person types sotāpanna … saddhānusārī (pi-4); attahitāya
  paṭipanno (pi-4); the divine-eye passage (pi-4 ^4-184), pubbenivāsa, paracitta, āsavakkhaya, iddhi (pi-2 / pi-4);
  kāye kāyānupassī … (pi-2); the eight wrong / right path factors (pi-2 ^2-U30 / pi-1); khattiya … sudda,
  gahaṭṭha, pabbajita, deva, manussa (pi-2 ^2-974); mātā … bhaginī; peta, tiracchāna, nerayika; ekavokāra …
  pañcavokāra bhava (pi-2 ^2-234); the anicca … vipariṇāmadhamma list (pi-1 / pi-2); the three teachers and
  sassatavādo (pi-4 ^4-131), santo saṃvijjamānā lokasmiṃ (pi-4); evamevaṃ «ထို့အတူပင်» (pi-4); vicikicchā / kaṅkhā
  kept apart («ယုံမှား» / «သံသယ», pi-1).
- New terms (proposed): sandhāvati «ကူးသွား» (pi-4 sandhāvitvā); kattā kāretā «ပြုလုပ်သူ၊ ပြုလုပ်စေသူ»; (vipāka)
  paṭisaṃvedī «(အကျိုးကို) ခံစားသူ»; kārako «ပြုသူ»; koci «တစ်စုံတစ်ယောက်»; vijjamāna «ရှိနေသော အရာ», saṃvijjamāna
  «ထင်ရှား ရှိနေသော အရာ» (pi-4 saṃvijjamāno «ထင်ရှား ရှိ»); kehici «အချို့အားဖြင့်»; cavati «စုတေ» (cuto stays pi-4
  «သေ၍», cavamāne pi-4 «သေဆဲ»; mīyati «သေဆုံး»); paññāyati «ထင်ရှား»; suñña «ဆိတ်သုဉ်း» (pi-1 Suññatavāro); the gati
  maims and animals; the kumbha list; the person words of ^5-116/117.

## Unsure Pāli / interpretation (for the reviewer)
- «Ese ce dunniggahite …» = «အကယ်၍ ဤသည် မကောင်းစွာ ချေပခြင်း ဖြစ်လျှင် …» (read as "if this refutation is badly
  made", as the English zero-shot); su- / du-niggahita = «ကောင်းစွာ / မကောင်းစွာ ချေပခြင်း ခံရ».
- «Sukatā paṭipādanā» = «ဆက်စပ် တင်ပြချက်ကို ကောင်းစွာ ပြုခဲ့သည်» (paṭipādanā = the conduct of the argument).
- «sabbattha / sabbadā / sabbesu puggalo nupalabbhati» keeps the same adverbs as the positive («နေရာတိုင်း၌ …
  မတွေ့ရ»), scope as ambiguous as the Pāli.
- «kāyaṃ appiyaṃ karitvā esese ekaṭṭhe same samabhāge tajjāte» = «ကိုယ်ဟူသော စကားကို ဦးစားမပေးဘဲ ဤစကားတို့သည်
  အနက် တူသော၊ ညီမျှသော၊ အချိုး တူသော၊ တစ်မျိုးတည်းမှ ဖြစ်သော စကားတို့» (the two words as synonyms).
- «tassa tasseva natthi dukkhassa antakiriyā …» = «ထိုထိုသူ၏ပင် … မရှိ» (the regress of agents / experiencers).
- Purisakārānuyogo = «လူ၏ ပြုလုပ်မှုကို စစ်ဆေးမေးမြန်းခြင်း» (literal purisa-kāra); Kalyāṇavagga named «“ကောင်းမွန်သော”».
- «yathā na nigaḷo negaḷiko, yassa nigaḷo so negaḷiko …» = «သံခြေချင်းသည် သံခြေချင်း ခတ်ထားသူ မဟုတ်၊ အကြင်သူ၌
  သံခြေချင်း ရှိ၏၊ ထိုသူသည် သံခြေချင်း ခတ်ထားသူ ဖြစ်သကဲ့သို့ …».
- «sappissa kumbhaṃ karoti» = «ထောပတ်ကြည်ဖြင့် အိုးကို ပြုလုပ်» (a pot made of ghee: the absurd reading the debate
  needs); the kumbha list item names (pānīyathālaka «သောက်ရေ ဗန်း», -kosaka «ခွက်», -sarāvaka «ပန်းကန်»,
  niccabhatta «အမြဲ ထမင်း», dhuvayāgu «အမြဲ ယာဂု»).
- The maims of ^5-86: aḷacchinna «လက်မ ပြတ်သူ», kaṇḍaracchinna «အကြော ပြတ်သူ», kuṇihatthaka «လက် ကောက်သူ»,
  phaṇahatthaka «လက်ချောင်းများ ကပ်နေသူ», kilāsiya «အရေပြား အဖြူကွက် ရောဂါ ရှိသူ», sosiya «ချောင်းဆိုး ပန်းနာ
  ရောဂါ ရှိသူ» (best guesses for plain readers).
- pi-1 renders «na vattabbaṃ» (classification) «ခေါ်ဆို၍ မရ»; the Kathāvatthu dialectic «(na) vattabba» is a different
  sense («should (not) be said») and gets «(မ)ဆိုသင့်» throughout.
- The uddāna (^5-238): «Aṭṭhakaniggahapeyyālā, sandhāvaniyā upādāya; Cittena pañcamaṃ kalyāṇaṃ,
  iddhisuttāharaṇena aṭṭhamaṃ» = section list; «upādāya» glossed «မှီ၍ သတ်မှတ်ချက်» (the Upādāpaññatti section).
- Verse stanzas keep the Pāli convention: each stanza opens «“», only the last closes (checker B4 accepts this).

## Source slips (translated as written; Pāli not changed)
- ^5-95 «…vipariṇāmadhammanti? Āmantā?»: «Āmantā» with «?» rendered as the statement «ဟုတ်ပါသည်။» (no «?»).
- ^5-43 «… saccikaṭṭhaparamatthena cakkhāyatanañca …» (no comma): the Burmese has «၊» between the two clauses.
- Irregular quote nesting in the Pāli, the regular depth-set marks used: ^5-1 … ^5-10 «…‘Q"’ti» (closing order),
  ^5-3 line 1 (the double quote never closes), ^5-5 / ^5-10 line 1 (three «"»), ^5-23 line 3 (‘ misplaced after
  «paṭipanno,’»), ^5-37 line 2 («tena vata re vattabbe – aññaṃ rūpaṃ añño puggaloti» without quotes), ^5-50 line 2
  («rūpaṃ puggaloti"’ micchā»), ^5-116 line 2 («"kumārakoti vā kumārikā"ti vā»).
- ^5-116 line 1 «na vattabbaṃ soti vā aññoti vā» without dash and quotes (^5-117 has both): rendered without dash
  and marks, the items before the verb.
- ^5-23 line 1 (vedanā without «saccikaṭṭhaparamatthena») and ^5-44 (sotadhātu with it): followed exactly.
- ^5-164 first line ends «Na hevaṃ vattabbe.» without «…pe…» (the parallels have it): as written.
- ^5-75, ^5-121, ^5-210: «!» after the reference: the Burmese sentence ends «။».
- ^5-238 «Na hevaṃ vattabbe.…Pe….» = «ဤသို့ မဆိုသင့်ပါ။ …».
- ^5-202 «kāyasakkhi» (short i; variant kāyasakkhī): the pi-4 name.
