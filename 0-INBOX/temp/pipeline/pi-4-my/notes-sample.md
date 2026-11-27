# pi-4 Burmese zero-shot SAMPLE: notes (preamble, 1-matika, 2-ekakapuggalapannatti)

Status: DONE 2026-11-19, waiting for review. Brief: burmese-zeroshot-sample-brief.md. Not committed.

## Files
- Output: `AI_translation/burmese/pi-4-burmese-plain-zeroshot_split_chapters/` preamble.md (3 segments),
  1-matika.md (27 segments, 185 lines), 2-ekakapuggalapannatti.md (46 segments, 47 lines).
- `my4_formulas.py` (shared module), `make_sample.py` (generator + unique prose tables), `terms_my4.py` (writes
  `my4-zeroshot-terms.md`), `check_sample.py` (per-line check + reuse test).
- Read-only lookup helpers (scratch, never used by the generator): kwic.py, short.py, heads_find.py, tb.py,
  wfind.py, overlap.py.
- Run: `python3 -I -X utf8 make_sample.py` (writes the 3 files + terms), then `check_sample.py`.

## Checks (final run)
- check_chapter_ids / check_text_pe / check_marks: OK for all three files (chk-pe copies deleted afterwards).
- check_sample.py: A 3/3 regenerated identical; B1 235 lines; B2 128 numbers; B3 248 negations / pairs; B4 66/66;
  B5 95 names; 0 mismatches. Reuse test 230 / 230 identical (C1 topic names 66/66, C2 whole lines / headings /
  colophons 14/14, C3 terms and clauses 150/150).
- The checker was mutation-tested (a changed number and a dropped «မဟုတ်» are both caught).

## Method (for the later agents)
- No pi-1/2/3 module is imported: my4_formulas builds its own index of the three RAILS texts (FINAL) and every
  reused value is read from it (heads(), items()) or checked against it (witness(): Pāli in the Pāli segment,
  Burmese in its rails Burmese). So the module fails at import if a reused value drifts from the final text.
- Engine: a line is a heading / colophon / fixed line / list head «N puggalā –» / numbered mātikā item / sentences.
  Sentences are split at «? » / «. » before a capital and at « – »; each unit goes through the frames (question,
  «ayaṃ vuccati», «ime vuccanti», kittāvatā / yāvatā) or the SENT table; else Miss (the run stops).
- Mātikā items: a list of names (greedy longest NAME / ALIAS key, optional «puggalo» = adjective, optional variant
  bracket), «A ca, B ca» pairs, group lines («Tayo X puggalā»), «atthekacco puggalo PRED, …» lines (PRED table or
  NAME + «ဖြစ်၏»), else LINES. Brackets inside table values are placeholders «⟦n⟧» filled by var_my().
- Later chapters: the niddesa questions use the same NAME keys (they are the niddesa question forms, the mātikā
  spellings are ALIAS). Group members (the four ponds, mangoes, bulls …) are not in NAME yet: add them in the
  chapter that defines them. Put shared sentences into my4_formulas.SENT, unique prose into the generator.

## Main choices
- Book title Puggalapaññattipāḷi = «ပုဂ္ဂိုလ်များကို သတ်မှတ်ဖော်ပြခြင်း» ("designating and describing persons";
  pattern of the pi-1/2/3 titles). paññatti inside the text = «သတ်မှတ်ချက်» (pi-1 ^1-M2-108, binding):
  khandhapaññatti «အစုအဝေး သတ်မှတ်ချက်» … puggalapaññatti «ပုဂ္ဂိုလ် သတ်မှတ်ချက်».
- Headings: Mātikā «ခေါင်းစဉ်စာရင်း», Ekakauddeso «တစ်မျိုးတွဲ အကျဉ်း ဖော်ပြချက်» (pi-1 Uddeso + Ekakaṃ), Niddeso
  «အကျယ် ဖော်ပြချက်», Ekakapuggalapaññatti «တစ်မျိုးတွဲ ပုဂ္ဂိုလ် သတ်မှတ်ချက်»; colophons Ekakaṃ … Dasakaṃ
  «N-မျိုးတွဲ» and Ekakaniddeso «တစ်မျိုးတွဲ အကျယ် ဖော်ပြချက်» are pi-1 / pi-2 final (Catukka- … Dasakaniddeso by
  the same pattern). Mātikā end «“ပုဂ္ဂိုလ် သတ်မှတ်ချက် ခေါင်းစဉ်စာရင်း” ပြီးဆုံးပြီ။».
- The frame: «Katamo ca puggalo X?» = «X ဟူသည် အဘယ် ပုဂ္ဂိုလ်နည်း။»; «– ayaṃ vuccati puggalo "X".» = «– ဤပုဂ္ဂိုလ်ကို
  “X”ဟု ခေါ်သည်။»; plural «ime vuccanti puggalā» = «ဤပုဂ္ဂိုလ်တို့ကို “X”ဟု ခေါ်သည်။» (the name stays as in the
  mātikā); «Idhekacco puggalo» = «ဤလောက၌ အချို့သော ပုဂ္ဂိုလ်သည်» (pi-2 ^2-925); mātikā «atthekacco puggalo X» =
  «အချို့သော ပုဂ္ဂိုလ်သည် X ဖြစ်၏».
- Person-type names: one nominal «…သူ» per type (or the familiar noun: ပုထုဇဉ်, အရိယာ, သောတာပန်, သကဒါဂါမ်,
  အနာဂါမ်, ရဟန္တာ, ပစ္စေကဗုဒ္ဓါ, သူတော်ကောင်း), the same string in the mātikā, the question and the closing quote
  (checked, B5). Before «puggalo» the name becomes an adjective «…သော ပုဂ္ဂိုလ်». Persons are counted with «ယောက်»
  (pi-2 «ပုဂ္ဂိုလ် တစ်ယောက်»).
- Reused (pi-1 / pi-2 / pi-3 final, all witnessed): the topic lists (pi-2 ^2-1, ^2-154, ^2-183, ^2-206, ^2-218,
  ^2-219); sekkha / asekkha / nevasekkhanāsekkha (pi-1, pi-2 ^2-753); puthujjana, ariya, arahā, sammāsambuddha;
  vimokkha «လွတ်မြောက်ခြင်း» (aṭṭha = «ရှစ်ပါး», pi-2 ^2-828); āsava «စိတ်အစွန်းအထင်း»; samāpatti «ဈာန် ဝင်စားရာ»;
  samāpajjati / vuṭṭhāti; pamāda; the «aṭṭhānametaṃ anavakāso» / «ṭhānañca kho etaṃ vijjati» formulas (pi-2 ^2-809);
  apubbaṃ acarimaṃ; the āvaraṇa / bhabba / abhabba clauses of pi-2 ^2-826 / ^2-827 word for word; ānantarika
  (rails ^2-U55 «ချက်ချင်း အကျိုးပေးသော ကံ», the rails text wins over the termbase gloss «နောက်ဘဝ၌ …»); the four
  paths and fruits (pi-2 ^2-807); maggasamaṅgī / phalasamaṅgī (pi-1 ^1-1382 / ^1-1383); orambhāgiya saṃyojana
  (pi-2); the five higher fetters (pi-2 ^2-U49); kāmarāga, byāpāda, tanubhāvāya; the Suddhāvāsa names (pi-2
  ^2-1027); cetovimuttiṃ paññāvimuttiṃ, diṭṭheva dhamme (pi-2 ^2-831); tehi dhammehi (pi-3); the duka vices and
  virtues from the pi-1 Suttantika dukas and the pi-2 Khuddakavatthu headings (kodha, upanāha, makkha, paḷāsa,
  issā, macchariya, sāṭheyya, māyā, ahirika, anottappa, dovacassatā, pāpamittatā, aguttadvāratā, amattaññutā,
  muṭṭhassacca, asampajañña, sīla/diṭṭhi-vipatti/-sampadā, ajjhatta/bahiddhā-saṃyojana); -ūpama «Xနှင့် တူသော»
  (pi-1 vijjūpamā).
- New terms (proposed): the names above that pi-1/2/3 do not have (samayavimutta, kuppadhamma, cetanābhabba,
  gotrabhū «အရိယာ အနွယ်သို့ ပြောင်းသူ», bhayūparata, samasīsī, ṭhitakappī, kāyasakkhī, diṭṭhippatta «မှန်ကန်သော
  အယူသို့ ရောက်သူ», dhammānusārī / saddhānusārī, sattakkhattuparama, kolaṅkola, ekabījī, the five non-returners,
  paccekasambuddha «ပစ္စေကဗုဒ္ဓါ» …), the tika … dasaka names and the group names; parinibbāyī «ပရိနိဗ္ဗာန် ပြုသူ»;
  dukkhassantaṃ karoti «ဒုက္ခ၏ အဆုံးကို ပြု၏» (dukkha = the truth «ဒုက္ခ», not pi-1 «နာကျင်မှု» bodily pain);
  opapātika «အလိုအလျောက် ပေါ်လာသူ» (pi-2 adjective); sambodhi «အပြည့်အဝ သိမြင်ခြင်း» (from sambuddha).
- Senses kept apart: bhabba «ထိုက်တန်» (pi-2, with an infinitive) vs -bhabba «… ဖြင့် ထိန်းနိုင်သူ» in cetanābhabbo /
  anurakkhaṇābhabbo; dhamma «သဘောတရား» (phenomena: tehi dhammehi, akusalā dhammā) vs «တရား» (teaching:
  ananussutesu dhammesu, tathāgatappaveditā dhammā, dhammānusārī; pi-2 ariyadhamma); anavasesa «အကြွင်းမဲ့» vs
  aparisesa «အကြွင်းအကျန် မရှိဘဲ»; eḷa «နုံအ» vs manda «ထုံထိုင်း»; vajja «အပြစ်» vs avaṇṇa «ကဲ့ရဲ့» / vaṇṇa
  «ချီးမွမ်း»; vipassati (simile, "sees") «သေချာစွာ မြင်၏» vs vipassanā «ထိုးထွင်းသိမြင်ခြင်း».
- rūpasahagata / arūpasahagata samāpatti = «သိမ်မွေ့သော ရုပ်ဘုံ / ရုပ်မရှိသော ဘုံနှင့်အတူ ဖြစ်သော ဈာန် ဝင်စားရာ»
  (the plane names of the core terms; sahagata = «နှင့်အတူ ဖြစ်သော», pi-1).
- Negation convention (the core rule applied to pi-4's verbs and agent words): free na / no / neva before a noun or
  at clause level = «… မဟုတ်»; before a finite verb or an agent word = «မ» + verb, as pi-2 does (^2-932
  «မယုံကြည်»); privative a- = «မ» + verb or «X မဟုတ်သူ» (anariyo, asappuriso). Lexical antonyms without a
  negation: asekkha «ကျင့်ကြံမှု ပြီးဆုံးသူ» (pi-1), avaṇṇa «ကဲ့ရဲ့», anavasesa «အကြွင်းမဲ့»; Burmese negations
  without a Pāli one: dubbaco, nesajjika, khalupacchābhattika, lolo, antarāparinibbāyī (listed in check_sample LEX /
  B_EXTRA).
- Variant brackets: «[ပါဌ်ကွဲ (Sī.): X]» for a different word, «[စာလုံးပေါင်းကွဲ (…): X]» for spelling; sutta
  references «a. ni. 4.135» = «၊ “အင်္ဂုတ္တရနိကာယ်” 4.135» (pi-2 ^2-957). A bracket stands after the Burmese of
  the word it qualifies (after a whole name phrase when the word is inside a name).

## Unsure Pāli / to review
- Names that interpret by the definition (minor clarification): antarāparinibbāyī «သက်တမ်း၏ အလယ်သို့ မရောက်မီ
  …» and upahaccaparinibbāyī «သက်တမ်း၏ အလယ်ကို ကျော်ပြီးမှ …» (from ^4-36 / ^4-37); paṭipannako «မဂ်ကို
  ကျင့်ကြံနေသူ» (from ^4-15; kept apart from sekkha «ကျင့်ကြံဆဲသူ»); samasīsī «စိတ်အစွန်းအထင်းနှင့် အသက်
  တပြိုင်နက် ကုန်ဆုံးသူ»; bhabbāgamano «ရှေ့သို့ တိုးတက်ရန် ထိုက်တန်သူ»; gotrabhū.
- ārabhati / nārabhati (5-1) = «မှားယွင်းစွာ ပြုမူ၏ / မပြုမူ» (does wrong); ādheyyamukho «ကြားကာစကို ယုံလွယ်သူ»;
  padaparamo «စကားလုံးသာ အများဆုံး ရသူ»; potthaka «လျှော်ပိတ်စ»; balībadda «နွားလား»; sāvakapāramī «တပည့်
  ပါရမီ»; udakūpamā «ရေထဲရှိ လူနှင့် တူသော»; niṭṭhā (10-1) «ပြီးမြောက်ခြင်း», idha «ဤလောက၌».
- yuttappaṭibhāna / muttappaṭibhāna = «သင့်လျော်သော / လျင်မြန်သော ဉာဏ်ပေါ်မှု ရှိသူ» (paṭibhāna = pi-2
  «ဉာဏ်ပေါ်မှု»).

## Source slips (translated as written)
- 1-matika ^4-M-10 (17): «…kālena; vaṇṇārahassa ca … kālena, atthekacco …»: the «;» and «,» around the third
  person are swapped against the other three; kept as one predicate, both marks rendered «၊».
- 1-matika ^4-M-10 (6) and (22), (23): commas inside a type name («Yuttappaṭibhāno, no muttappaṭibhāno»,
  «Rūpappamāṇo, rūpappasanno»); the niddesa questions have the names without the comma (ALIAS).
- 1-matika ^4-M-7 (46) Uddhaṃsotoakaniṭṭhagāmī (one word) vs ^4-40 «uddhaṃsoto akaniṭṭhagāmī» (two words): one name.
- Order: mātikā (13) Bhabbāgamano, (14) Abhabbāgamano; the niddesa defines abhabbāgamano first (^4-12, ^4-13).
- ^4-17 «Ayaṃ vuccati» after a full stop (elsewhere after «–»); ^4-25, ^4-26 likewise: frame unchanged.
- ^4-44 has no block ID of its own line: the Ekakaniddeso colophon closes the segment (kept, 2 lines).
- ^4-M-16: «Dasakaṃ.» and the mātikā end are two lines of one segment (kept).
