# pi-6 Burmese zero-shot, ch. 7 group a (Anusayayamaka 7-01 … 7-05) — notes

Status 2026-11-22: all five files generated; check_chapter_ids / check_text_pe / check_marks OK for each (chk-pe copies
deleted); check_ch7a.py 0 mismatches, reuse 8727 / 8727; mutation test 11 / 11 caught. Not committed.
Brief: burmese-zeroshot-brief.md. Source rule kept: translated from the Pāli only; no Burmese translation / nissaya /
web source opened (0-INBOX/temp/language-priority/ not opened). pi-1 … pi-5 read only through their rails texts (FINAL,
via kwic6.py / k.sh, read-only) and locked termbases. English pi-6 rails read for meaning only (yato / tato,
tadekaṭṭhaṃ, aṭṭhamaka, sānusaya); make_ch3.py / check_ch3.py / notes-ch3.md read as models (never run).

## Files
- Output: `AI_translation/burmese/pi-6-burmese-plain-zeroshot_split_chapters/7-01 … 7-05-anusayayamaka.md`
  (segments 41 / 34 / 37 / 37 / 37; lines 253 / 227 / 216 / 229 / 208).
- `make_ch7a.py` (generator; imports my6_formulas.py, extends F.VERB / F.H / COLO in memory only; `--misses`),
  `check_ch7a.py` (per-line check + reuse test; `--mutate` = mutation self-test).
- Run: `python3 -I -X utf8 make_ch7a.py` (writes the five files), `check_ch7a.py`, `check_ch7a.py --mutate`.

## For the agent of 7-06 … 7-11 (method)
- The TABLES block at the top of make_ch7a.py holds every anusaya term: ANUSAYA (the seven, read from pi-2 ^2-816 and
  checked against ^2-949), STEM + ENDING (nom -o, ins -ena, acc -aṃ, acc + ca -añca; a separate «ca» token adds
  «လည်း»), VERB_RE (anuseti / nānuseti / anusenti …, sānusayo / niranusayo / -ā / -ti, pajahati / pajahatīti /
  nappajahati), WHO (persons in dat. and nom., counts, «eva» forms), PLACE (planes and feelings), PRO / INTRO, notes,
  headings, colophons. `import make_ch7a` is side-effect free apart from F.VERB / F.H updates (nothing written).
- sentence_my() is a token translator: the Pāli order of the anusaya frames is the Burmese order, so each token (or
  fixed group) gives one piece; the verb form comes from its position (question first clause «၏», question verb
  «သလော», kattha «သနည်း», statement «သည်», after «no ca» negated, a negative after «no ca» = «… မVသည်ကား မဟုတ်»).
  Clause «၊» after a verb that another clause follows; list «၊» between «ca» members. Unknown token = Miss.
- Paṭiloma pajahana (7-06) will need «nappajahati» = «မပယ်» (already in VERB_RE / verb_my, untested on real text).

## New recurring terms and phrases (Pāli = Burmese; for the consistency pass)
- Anusayayamakaṃ = ကိန်းအောင်းခြင်းများကို အတွဲလိုက် မေးဖြေခြင်း (module TOPICS, proposed there)
- Sattānusayā – … = ကိန်းအောင်းခြင်း ခုနစ်ပါး – … (pi-2 ^2-816 / ^2-949, names read from the final text)
- kāmarāgānusayo = ကာမရာဂ ကိန်းအောင်းခြင်း; paṭighānusayo = မုန်းတီးမှု ကိန်းအောင်းခြင်း; mānānusayo = မာန ကိန်းအောင်းခြင်း;
  diṭṭhānusayo = အယူ ကိန်းအောင်းခြင်း; vicikicchānusayo = ယုံမှားမှု ကိန်းအောင်းခြင်း; bhavarāgānusayo = ဘဝရာဂ ကိန်းအောင်းခြင်း;
  avijjānusayo = အမှန်ကို မသိမှု ကိန်းအောင်းခြင်း (all pi-2 ^2-816)
- X-aṃ = Xကို; X-añca = Xကိုလည်း; X ca = Xလည်း; members joined «Aလည်း၊ Bလည်း V(ကြ)»
- anuseti = ကိန်းအောင်း (pi-2 ^2-816): ကိန်းအောင်းသည် / ကိန်းအောင်း၏ (first clause) / ကိန်းအောင်းသလော; anusenti = ကိန်းအောင်းကြသည်
  / ကိန်းအောင်းကြ၏ / ကိန်းအောင်းကြသလော; nānuseti = မကိန်းအောင်း (pi-4 ^4-114) / မကိန်းအောင်းသလော; nānusenti = မကိန်းအောင်းကြ
- no ca … anuseti = သို့သော် … မကိန်းအောင်း(ကြ); no ca … nānuseti = သို့သော် … မကိန်းအောင်း(ကြ)သည်ကား မဟုတ် (sample double negative)
- Kattha X anuseti? = မည်သည့်နေရာ၌ X ကိန်းအောင်းသနည်း (kattha pi-2 ^2-1024 «မည်သည့်နေရာ၌ … သနည်း»)
- sānusayo = … ရှိသူ (pi-5 ^5-606 «ကိန်းအောင်းခြင်း ရှိသူ»): X-ena sānusayo = X ရှိသူ ဖြစ်သည် / ဖြစ်၏ / ဖြစ်သလော;
  sānusayā = … ရှိသူများ ဖြစ်ကြသည်; no ca X-ena sānusayo = သို့သော် X ရှိသူ မဟုတ်(ကြ)
- niranusayo = … မရှိသူ (NEW: nir- = «မရှိ»): X မရှိသူ ဖြစ်သည် …; no ca X-ena niranusayo = သို့သော် X မရှိသူ မဟုတ်
- pajahati = ပယ် (pi-5 ^5-390): Xကို ပယ်သည် / ပယ်၏ / ပယ်သလော; no ca … pajahati = သို့သော် … မပယ်; nappajahati = မပယ် (prepared)
- tadekaṭṭhaṃ (pajahati) = ထိုအရာနှင့် တစ်နေရာတည်း တည်ရှိသည့် အနေဖြင့် (ပယ်သည်) (tadekaṭṭha pi-2 ^2-816 «ထိုအရာနှင့် တစ်နေရာတည်း
  တည်ရှိသော»; adverbial form NEW, the same in «Tadekaṭṭhaṃ pajahati.» and «Xကို … အနေဖြင့် ပယ်သည်»)
- Question frames: yassa … tassa = အကြင်သူအား … ၊ ထိုသူအား …; yattha … tattha = အကြင်နေရာ၌ … ၊ ထိုနေရာ၌ …; yassa yattha …
  tassa tattha = အကြင်သူအား အကြင်နေရာ၌ … ၊ ထိုသူအား ထိုနေရာ၌ … (module CL / FT); yo … so = အကြင်သူသည် … ၊ ထိုသူသည် … (ch3);
  yato … tato = အကြင်နေရာ၌ … ၊ ထိုနေရာ၌ … (NEW: as yattha, see Unsure); yo yato … so tato = အကြင်သူသည် အကြင်နေရာ၌ … ၊
  ထိုသူသည် ထိုနေရာ၌ …; vā pana = တစ်ဖန်
- Resumptive pronouns after «no ca»: tassa ထိုသူအား; tesaṃ ထိုသူတို့အား; tassa / tesaṃ tattha ထိုသူ(တို့)အား ထိုနေရာ၌; tattha / tato
  ထိုနေရာ၌; so ထိုသူသည်; te ထိုသူတို့သည်; so / te tato ထိုသူ(တို့)သည် ထိုနေရာ၌
- Places + ettha / tattha / tato: «PLACES ဟူသော ဤနေရာ၌» (ettha) / «PLACES ဟူသော ထိုနေရာ၌» (tattha, tassa tattha, tesaṃ tattha,
  tato, so tato, te tato; the person part of the pronoun goes into WHO «…အား» / «…သည်», as the sample's who_my); places
  joined «Aနှင့် B», «A၊ Bနှင့် C» (NEW)
- Kāmadhātuyā dvīsu vedanāsu = ကာမဘုံရှိ ခံစားမှု နှစ်ပါး; Kāmadhātuyā tīsu vedanāsu = ကာမဘုံရှိ ခံစားမှု သုံးပါး (kāmadhātu
  pi-2 ^2-991 «ကာမဘုံ», «Xရှိ N» pi-1 ^1-1475 «ဘုံ သုံးပါးရှိ», dvīsu / tīsu pi-1); Kāmadhātuyā alone = ကာမဘုံ (prepared)
- Dukkhāya vedanāya = နာကျင်သော ခံစားမှု (pi-1 ^1-M1-2); Rūpadhātuyā = သိမ်မွေ့သော ရုပ်ဘုံ (pi-2 ^2-993); Arūpadhātuyā =
  ရုပ်မရှိသော ဘုံ (pi-2 ^2-995); Apariyāpanne = ဘဝဘုံတို့၌ အကျုံးမဝင်သော အရာ (pi-1 ^1-M2-96 + «အရာ»)
- Sabbasakkāyapariyāpannesu dhammesu = ကိုယ်၌ အကျုံးဝင်သော သဘောတရား အားလုံး (sakkāya pi-1 «ကိုယ်»; -pariyāpanna pi-1 ^1-283
  «… ၌ အကျုံးဝင်သော»; sabba «အားလုံး»)
- sabbattha = နေရာတိုင်း၌ (as ch3 / ch6-8 notes)
- Persons (dat. «အား» with anuseti; nom. «သည်» with sānusaya / pajahati): Anāgāmissa / Anāgāmī = အနာဂါမ်အား / အနာဂါမ်သည်
  (pi-4 ^4-M-7); Arahato / Arahā = ရဟန္တာအား / ရဟန္တာသည်; Puthujjanassa / Puthujjano = ပုထုဇဉ်အား / ပုထုဇဉ်သည်; Aṭṭhamako =
  အဋ္ဌမ ပုဂ္ဂိုလ်သည် (pi-5 ^5-368); Aggamaggasamaṅgī = အမြတ်ဆုံး မဂ်နှင့် ပြည့်စုံသူသည် (ch3); Dvinnaṃ / Tiṇṇaṃ / Catunnaṃ
  puggalānaṃ = ပုဂ္ဂိုလ် နှစ်ယောက် / သုံးယောက် / လေးယောက်တို့အား; Dve / Tayo / Cattāro puggalā = ပုဂ္ဂိုလ် နှစ်ယောက် / သုံးယောက် /
  လေးယောက်တို့သည် (pi-4 ^4-M-8 / 9 / 10); Tesaññeva puggalānaṃ = ထိုပုဂ္ဂိုလ်တို့အားပင်; Tasseva puggalassa = ထိုပုဂ္ဂိုလ်အားပင်;
  Teva puggalā = ထိုပုဂ္ဂိုလ်တို့သည်ပင်; Sveva puggalo = ထိုပုဂ္ဂိုလ်သည်ပင် (eva «ပင်» pi-5 ^5-241). Prepared (no occurrence yet):
  Aṭṭhamakassa = အဋ္ဌမ ပုဂ္ဂိုလ်အား; Aggamaggasamaṅgissa = အမြတ်ဆုံး မဂ်နှင့် ပြည့်စုံသူအား
- Āmantā …pe…. = ဟုတ်ပါသည် …။; a question cut before its verb «…pe…?» = «…လော။» (ch3)
- Headings: Uppattiṭṭhānavāro = ဖြစ်ပေါ်ရာ နေရာအလိုက် ဖော်ပြချက် (NEW); Mahāvāro 1. anusayavāro = ဖော်ပြချက်ကြီး 1.
  ကိန်းအောင်းခြင်းအလိုက် ဖော်ပြချက် (mahāvāra NEW); Anusayavāra / -vāro = ကိန်းအောင်းခြင်းအလိုက် ဖော်ပြချက်; Sānusayavāra / -vāro =
  ကိန်းအောင်းခြင်း ရှိသူအလိုက် ဖော်ပြချက်; Pajahanavāro = ပယ်ခြင်းအလိုက် ဖော်ပြချက် (pajahana NEW); anuloma- headings from the
  module H; paṭilomapuggalo / paṭilomaokāso / paṭilomapuggalokāsā = ပုဂ္ဂိုလ်အလိုက် / နေရာအလိုက် / ပုဂ္ဂိုလ်နှင့် နေရာအလိုက်
  အငြင်းပြ ပုံစံ (paṭiloma = paccanīka «အငြင်းပြ ပုံစံ», the Yamaka negated form; no pi-1 … pi-5 occurrence)
- Colophons: Uppattiṭṭhānavāro. = ဖြစ်ပေါ်ရာ နေရာအလိုက် ဖော်ပြချက်။; Anusayavāre anulomaṃ. = ကိန်းအောင်းခြင်းအလိုက် ဖော်ပြချက်၌
  အဟုတ်ပြ ပုံစံ။; Anusayavāre paṭilomaṃ. = … ၌ အငြင်းပြ ပုံစံ။; Anusayavāro. = ကိန်းအောင်းခြင်းအလိုက် ဖော်ပြချက်။; the same for
  Sānusaya-, Pajahana- (Pajahanavāre paṭilomaṃ. / Pajahanavāro. prepared); «Xvāro niṭṭhito.» = «“…” ပြီးဆုံးပြီ။» (prepared)
- Notes: (Ekamūlakaṃ) / (Dukamūlakaṃ) / (Tikamūlakaṃ) / (Catukkamūlakaṃ) / (Pañcakamūlakaṃ) / (Chakkamūlakaṃ) =
  (တစ်ပါးကို / နှစ်ပါးကို / သုံးပါးကို / လေးပါးကို / ငါးပါးကို / ခြောက်ပါးကို အခြေခံ၍) (NEW; «ကို အခြေခံ၍» as ch3 / module BASED)

## Checks (final run)
- A 5/5 regenerated identical; B1 1133 lines; B2 2292 negations, each one Burmese negative (place name «ရုပ်မရှိသော ဘုံ»
  masked; avijjā «အမှန်ကို မသိမှု» is not counted as it has no counted form); B3 3265 predicates (family, polarity,
  number, «no ca», double negative, verb form cl / q / wh / statement) in order, 421 answers; B4 532 labelled lines,
  every vā pana = «တစ်ဖန်»; B5 digits + 501 number words; B6 1636 distinct Pāli sentences, one Burmese each (also 476
  occurrences in the sample files and ch. 3); B7 120 headings / colophons / notes / list lines; 0 mismatches.
- Reuse 8727 / 8727 (C1 seven names 5067/5067; C2 whole lines and answers 269/269; C3 33 reused terms 3391/3391).
  Documented exceptions (not counted): anuloma / paṭiloma «အဟုတ်ပြ / အငြင်းပြ ပုံစံ», Natthi «မရှိပါ။» (89 lines).
- Mutation test: dropped «မ», dropped nir-, changed answer, changed anusaya name, dropped plural «ကြ», dropped double
  negative, changed label, changed number, changed place, pajahati polarity, question verb form: all caught.

## Unsure (for review)
- yato / tato = «အကြင်နေရာ၌ / ထိုနေရာ၌» (the same as yattha / tattha). The ablative «မှ» ("from where") is more literal and
  reads well with pajahati («ထိုနေရာမှ … ပယ်»), but badly with sānusaya («ထိုနေရာမှ … ရှိသူ»); English rails "wherever …
  there". One Burmese kept for both sections.
- sānusayo «… ရှိသူ ဖြစ်…» keeps the pi-5 noun «ကိန်းအောင်းခြင်း ရှိသူ»; a shorter «… ရှိ၏ / ရှိသလော» is possible.
  «Aလည်း၊ Bလည်း ရှိသူ မဟုတ်» (no ca X ca Y ca sānusayo) can be read "not one who has both"; the Pāli is as open.
- tadekaṭṭhaṃ pajahati = «ထိုအရာနှင့် တစ်နေရာတည်း တည်ရှိသည့် အနေဖြင့် ပယ်သည်» (abandons it as co-existent with that); the
  English rails read it as an object ("what is conjoined with it"); alternative «… တည်ရှိသော အရာကို ပယ်သည်».
- sakkāya «ကိုယ်» (pi-1 termbase compound member): «ကိုယ်၌ အကျုံးဝင်သော သဘောတရား» may be read as "body" only.
- Kāmadhātuyā dvīsu vedanāsu «ကာမဘုံရှိ ခံစားမှု နှစ်ပါး» (the two feelings of the sense sphere: which two is not said).
- «PLACES ဟူသော ဤနေရာ၌ / ထိုနေရာ၌» for «… ettha / tattha» (the Pāli apposition); Apariyāpanne «… အကျုံးမဝင်သော အရာ».
- mahāvāra «ဖော်ပြချက်ကြီး»; uppattiṭṭhāna «ဖြစ်ပေါ်ရာ နေရာ»; the -mūlaka notes «(တစ်ပါးကို အခြေခံ၍)» (based on one tendency).
- aṭṭhamaka «အဋ္ဌမ ပုဂ္ဂိုလ်» (pi-5) keeps the Pāli ordinal in Burmese script.

## Source slips (Pāli not changed; SLIPS in make_ch7a.py)
- 7-01 ^6-7-21 and ^6-7-25: «kāmārāgānusayo» for kāmarāgānusayo (read as kāmarāga).
- 7-01 ^6-7-35: «anusanti» for anusenti (read as anusenti, plural).
- 7-04 ^6-7-130: «dukkhāya vedanāya ariyāpanne» for apariyāpanne (read as apariyāpanne).
- 7-01 ^6-7-8: «(Ekamūlakaṃ )» with a space before «)»: the space kept in the Burmese note.
- 7-02 ^6-7-54: «(Kha) yattha vā pana…pe…? Āmantā.» (a question cut before its verb): «(ခ) တစ်ဖန် အကြင်နေရာ၌…လော။».
- No pronoun / number / case disagreement found in the Pāli (scanned: WHO case vs pronoun, verb family, plural).
