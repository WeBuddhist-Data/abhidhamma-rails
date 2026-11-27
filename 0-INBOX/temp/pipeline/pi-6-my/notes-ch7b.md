# pi-6 Burmese zero-shot, ch. 7 group b (Anusayayamaka 7-06 … 7-11) — notes

Status 2026-11-22: all six files generated; check_chapter_ids / check_text_pe / check_marks OK for each (chk-pe copies
deleted); check_ch7b.py 0 mismatches, reuse 10289 / 10289; mutation test 19 / 19 caught. Not committed.
Brief: burmese-zeroshot-brief.md. Source rule kept: translated from the Pāli only; no Burmese translation / nissaya /
web source opened (0-INBOX/temp/language-priority/ not opened). pi-1 … pi-5 read only through their rails texts (FINAL,
via k.sh / kwic6.py, read-only) and the witnesses of my6_formulas. English pi-6 rails 7-11 read for meaning only
(bhaṅgā "none are dissolved", upapatti nāma natthi). make_ch7a.py imported read-only (never run as a script);
make_ch3.py, make_ch6-8.py, make_ch10c.py (in progress, read only for anāgāmimaggasamaṅgī / pajahati) read as models.

## Files
- Output: `AI_translation/burmese/pi-6-burmese-plain-zeroshot_split_chapters/7-06 … 7-11-anusayayamaka.md`
  (segments 37 / 62 / 12 / 50 / 37 / 10; non-empty lines 252 / 359 / 103 / 288 / 216 / 31).
- `make_ch7b.py` (generator; imports make_ch7a.py — its TABLES and line_check — and my6_formulas.py; extends
  F.VERB / F.H in memory only; `--misses`), `check_ch7b.py` (per-line check + reuse test; `--mutate`).
- Run: `python3 -I -X utf8 make_ch7b.py` (writes the six files), `check_ch7b.py`, `check_ch7b.py --mutate`.

## Reused unchanged from ch7a (identical Pāli = identical Burmese)
The seven anusaya names, case endings (X-aṃ «Xကို», X-añca «Xကိုလည်း», X ca «Xလည်း»), the question frames (yo … so,
yato … tato, yo yato … so tato, yassa … tassa, yattha … tattha, yassa yattha … tassa tattha, vā pana «တစ်ဖန်»), the
persons (Aggamaggasamaṅgī, Aṭṭhamako, Anāgāmissa, Arahato, Puthujjanassa, Dvinnaṃ / Tiṇṇaṃ / Catunnaṃ puggalānaṃ,
Sveva puggalo, Tasseva puggalassa, Tesaññeva puggalānaṃ), the places (+ ettha / tattha / tato), sabbattha, tadekaṭṭhaṃ,
pajahati «ပယ်» with «no ca» negation and double negative, Āmantā / No / Natthi, the anuloma / paṭiloma headings, the
-mūlaka notes, Pajahanavāre paṭilomaṃ. / Pajahanavāro. colophons, «Anusayayamakaṃ niṭṭhitaṃ.» and «Namo tassa …» (module).

## «nappajahati» = «မပယ်» (prepared in ch7a, tested here)
7-06 uses it in every frame: first clause «… ကို မပယ်၊» (bare negative, as the module's negative first clause), question
«မပယ်သလော», statement «မပယ်» / plural nappajahanti «မပယ်ကြ», after «no ca» «မပယ်သည်ကား မဟုတ်» (double negative).
Checked by B2 / B3 of check_ch7b.py. It works without change.

## New recurring terms and phrases (Pāli = Burmese; for the consistency pass)
- parijānāti = ပိုင်းခြား သိ (pi-5 ^5-390; as make_ch3.py): ပိုင်းခြား သိသည် / သိ၏ (first clause) / သိသလော; parijānanti =
  ပိုင်းခြား သိကြသည်; na parijānāti = ပိုင်းခြား မသိ / မသိသလော; na parijānanti = ပိုင်းခြား မသိကြ; no ca … parijānāti =
  သို့သော် … ပိုင်းခြား မသိ; no ca … na parijānāti = သို့သော် … ပိုင်းခြား မသိသည်ကား မဟုတ်
- Tadekaṭṭhaṃ parijānāti. = ထိုအရာနှင့် တစ်နေရာတည်း တည်ရှိသည့် အနေဖြင့် ပိုင်းခြား သိသည်။ (ch7a TADEKA)
- pahīno / pahīnā = (Xကို) ပယ်ပြီး ဖြစ် (pi-4 ^4-65 «… ကို ပယ်ပြီး ဖြစ်၏»; pi-2 ^2-547 «ပယ်ပြီး»): ပယ်ပြီး ဖြစ်သည် /
  ဖြစ်၏ / ဖြစ်သလော; the anusaya before pahīno takes «ကို» (pi-4 / pi-5 ^5-310 «… ကို ပယ်ပြီး ဖြစ်သည်»); plural pahīnā
  without «ကြ» (pi-4 ^4-44 «… တို့ကို … ပယ်ပြီး ဖြစ်၏», the number is in the «Xကိုလည်း၊ Yကိုလည်း» members; checked)
- appahīno / appahīnā = (Xကို) မပယ်ရသေး (pi-4 ^4-45 «… ကို မပယ်ရသေး»): question မပယ်ရသေးသလော; no ca … pahīno =
  သို့သော် … မပယ်ရသေး; no ca … appahīno = သို့သော် … မပယ်ရသေးသည်ကား မဟုတ်
- (X) na vattabbo / na vattabbā "pahīno"ti vā "appahīno"ti vā = (Xကို) “ပယ်ပြီး”ဟူ၍ဖြစ်စေ၊ “မပယ်ရသေး”ဟူ၍ဖြစ်စေ ခေါ်ဆို၍ မရ
  (pi-2 ^2-641 na vattabbā "…"ti «“…”ဟု ခေါ်ဆို၍ မရ»; pi-5 ^5-386 "…"ti vā "…"ti vā «“…”ဟူ၍ဖြစ်စေ၊ “…”ဟူ၍ဖြစ်စေ»);
  "pahīnā" / "appahīnā" in the quotes = the same words
- uppajjati = ဖြစ်ပေါ် (module): Xလည်း ဖြစ်ပေါ်၏ / ဖြစ်ပေါ်သလော / ဖြစ်ပေါ်သည်; nuppajjati = မဖြစ်ပေါ်; no ca … nuppajjati =
  … မဖြစ်ပေါ်သည်ကား မဟုတ် (module not_so)
- ; = ၊ (pi-4 ^4-M-2 …)
- Anāgāmimaggasamaṅgī = အနာဂါမိမဂ်နှင့် ပြည့်စုံသူ(သည်) (anāgāmimagga pi-5 ^5-339; -samaṅgī «နှင့် ပြည့်စုံသူ» as ch6-8 /
  ch10c; same as ch10c's ANAGAMIMAGGA + SAMANGI)
- X(-ñca / -ṃ) [Y-ñca] ṭhapetvā avasesā puggalā = Xနှင့် Yကို ချန်ထား၍၊ ကြွင်းကျန်သော ပုဂ္ဂိုလ်တို့သည် (make_ch3.py PJ_SUBJ);
  members: Aggamaggasamaṅgiñca / -iṃ = အမြတ်ဆုံး မဂ်နှင့် ပြည့်စုံသူ; Anāgāmimaggasamaṅgiñca / -iṃ = အနာဂါမိမဂ်နှင့် ပြည့်စုံသူ;
  aṭṭhamakañca = အဋ္ဌမ ပုဂ္ဂိုလ်; Dvinnaṃ maggasamaṅgīnaṃ(ca) = မဂ်နှင့် ပြည့်စုံသူ နှစ်ယောက်တို့ (gen. pl. as ch7a's
  «Dvinnaṃ puggalānaṃ» «ပုဂ္ဂိုလ် နှစ်ယောက်တို့»; ch10c has acc. «Dve maggasamaṅgino» «မဂ်နှင့် ပြည့်စုံသူ နှစ်ယောက်»)
- (vitthāretabbaṃ) / (Vitthāretabbaṃ) = (အကျယ် ချဲ့ရမည်) (pi-5 ^5-839 «အကျယ် ချဲ့»; = make_ch3.py / ch2-02-4-5 «အကျယ်
  ချဲ့ရမည်»; ch6-8 has «အကျယ် ဖော်ပြရမည်»: for the consistency pass); «… uppajjati (vitthāretabbaṃ).» = «… ဖြစ်ပေါ်သည်
  (အကျယ် ချဲ့ရမည်)။»; «Āmantā. (Vitthāretabbaṃ).» = «ဟုတ်ပါသည်။ (အကျယ် ချဲ့ရမည်)။»
- Variant «[pahīno (sī. ka.) anusayavārena pana na sameti]» = «[ပါဌ်ကွဲ (Sī., Ka.): pahīno၊ ကိန်းအောင်းခြင်းအလိုက်
  ဖော်ပြချက်နှင့်ကား မညီ]» (pi-4 ^4-117 «… pana sameti» «… နှင့်ကား ညီ၏»)
- dhātupucchā / dhātuvisajjanā (planes = «ဘုံ» as kāmadhātu «ကာမဘုံ»):
  - X-āya cutassa Y-ṃ upapajjantassa = Xမှ စုတေ၍ Y၌ ပြန်လည် ဖြစ်ပေါ်ဆဲသူ(အား) (frame pi-5 ^5-65 «Xမှ သေ၍ Y၌ ပြန်လည်
    ဖြစ်ပေါ်»; cuta with the sample's cavati «စုတေ», see Unsure; upapajjanta «ပြန်လည် ဖြစ်ပေါ်ဆဲ» module PART)
  - na X (a plane) = X မဟုတ်သော ဘုံ; na X na Y = Xလည်း မဟုတ်၊ Yလည်း မဟုတ်သော ဘုံ (pi-5 ^5-386 «… ရှိသည်လည်း မဟုတ်၊ …
    မရှိသည်လည်း မဟုတ်သော»)
  - kati anusayā anusenti, kati anusayā nānusenti, kati anusayā bhaṅgā? = ကိန်းအောင်းခြင်း မည်မျှ ကိန်းအောင်းကြသနည်း၊
    ကိန်းအောင်းခြင်း မည်မျှ မကိန်းအောင်းကြသနည်း၊ ကိန်းအောင်းခြင်း မည်မျှ ပြိုပျက်ကြသနည်း။ (kati «မည်မျှ» pi-2 ^2-151;
    bhaṅga «ပြိုပျက်» pi-5 ^5-366 «ပြိုပျက်ခြင်း»)
  - kassaci N anusayā anusenti = (… ဆဲသူ) အချို့အား ကိန်းအောင်းခြင်း N ကိန်းအောင်းကြသည် (kassaci pi-2 ^2-1007 «အချို့အား»;
    the first after the person «…ဆဲသူ အချို့အား»); satta / pañca / tayo = ခုနစ်ပါး / ငါးပါး / သုံးပါး (pi-2 ^2-838)
  - satteva anusayā anusenti = ကိန်းအောင်းခြင်း ခုနစ်ပါးပင် ကိန်းအောင်းကြသည် (eva «ပင်» as ch7a)
  - anusayā bhaṅgā natthi = ပြိုပျက်သော ကိန်းအောင်းခြင်း မရှိ (NEW)
  - X-āya cutassa Y-āya upapatti nāma natthi, heṭṭhā upapajjamāno kāmadhātuṃyeva upapajjati = Xမှ စုတေသူအား Y၌ ပြန်လည်
    ဖြစ်ပေါ်ခြင်း ဟူ၍ မရှိ၊ အောက်၌ ပြန်လည် ဖြစ်ပေါ်ဆဲသူသည် ကာမဘုံ၌ပင် ပြန်လည် ဖြစ်ပေါ်သည် (upapatti «ပြန်လည် ဖြစ်ပေါ်ခြင်း»
    as ch2-02-4-5; heṭṭhā «အောက်၌» pi-1 ^1-1287 heṭṭhato; nāma natthi «ဟူ၍ မရှိ» NEW)
  - notes (Kāmadhātumūlakaṃ) = (ကာမဘုံကို အခြေခံ၍); (Nakāmadhātumūlakaṃ) = (ကာမဘုံ မဟုတ်သော ဘုံကို အခြေခံ၍);
    (Nakāmanaarūpadhātumūlakaṃ) = (ကာမဘုံလည်း မဟုတ်၊ ရုပ်မရှိသော ဘုံလည်း မဟုတ်သော ဘုံကို အခြေခံ၍); and the same for
    Rūpa-, Arūpa-, Narūpa-, Naarūpa-, Narūpanaarūpa-, Nakāmanarūpa- (as ch7a's «(တစ်ပါးကို အခြေခံ၍)»)
- Headings: Pariññāvāro / Pariññāvāra = ပိုင်းခြား သိခြင်းအလိုက် ဖော်ပြချက် (make_ch3.py); Pahīnavāro / Pahīnavāra = ပယ်ပြီး
  ဖြစ်ခြင်းအလိုက် ဖော်ပြချက် (NEW); Uppajjanavāro = ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက် (= the module's Uppādavāro: one
  Burmese for uppāda / uppajjana); (Ka) dhātupucchāvāro = (က) ဘုံများအကြောင်း အမေး ဖော်ပြချက် (pucchā «အမေး» pi-5
  ^5-652; NEW); (Kha) dhātuvisajjanāvāro = (ခ) ဘုံများအကြောင်း အဖြေ ဖော်ပြချက် (visajjanā «အဖြေ» NEW)
- Colophons: Pariññāvāre anulomaṃ. / paṭilomaṃ. = ပိုင်းခြား သိခြင်းအလိုက် ဖော်ပြချက်၌ အဟုတ်ပြ / အငြင်းပြ ပုံစံ။; Pariññāvāro. =
  … ဖော်ပြချက်။; the same for Pahīna-; Uppajjanavāro. = ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်။; Dhātupucchāvāro. = ဘုံများအကြောင်း
  အမေး ဖော်ပြချက်။; Dhātuvisajjavāro. (slip) = ဘုံများအကြောင်း အဖြေ ဖော်ပြချက်။

## Checks (final run)
- A 6/6 regenerated identical; B1 1249 lines, 443 quotation pairs (paired, not nested); B2 3842 negations, each one
  Burmese negative (masked: «ရုပ်မရှိသော ဘုံ», «အမှန်ကို မသိမှု»; variant brackets out); B3 3635 predicates (anuseti /
  sānusaya / pajahati / parijānāti / pahīna / uppajjati: family, polarity, number, «no ca», double negative, form
  cl / q / wh / statement) in order, B3b 1286 pahīna / vattabba numbers (plural iff two or more «ca» members), 339
  answers; B4 530 labelled lines, every vā pana = «တစ်ဖန်»; B5 digits + 1244 number words; B6 1862 distinct Pāli
  sentences, one Burmese each (also 784 occurrences in 7-01 … 7-05, the sample files and ch. 3); B7 147 headings /
  colophons / notes / variants; 0 mismatches.
- Reuse 10289 / 10289 (C1 seven names 5330/5330; C2 whole lines and answers 230/230; C3 43 reused terms 4729/4729).
  Documented exceptions (not counted): anuloma / paṭiloma, Natthi «မရှိပါ။», cutassa «စုတေ» (172 lines).
- Mutation test (19): dropped «မ» of nappajahati, dropped double negative, na parijānāti polarity, plural «ကြ», pahīno
  polarity, appahīno double negative, vattabba negation, swapped quote, uppajjati polarity, answer, anusaya name, label,
  person count, place, plane negation, number of tendencies, kati question verb, question verb form, ṭhapetvā member:
  all caught.

## Unsure (for review)
- cutassa «စုတေ၍ / စုတေသူ» follows the sample's cavati «စုတေ» (approved); pi-5 ^5-65 (FINAL) renders «rūpadhātuyā cuto
  arūpadhātuṃ upapajjati» «… မှ သေ၍ … ၌ ပြန်လည် ဖြစ်ပေါ်». Not identical Pāli (gen. participles here), but the consistency
  pass may prefer «သေ၍».
- pahīno «Xကို ပယ်ပြီး ဖြစ်…» with the Yamaka «အကြင်သူအား / ထိုသူအား» (the sample's yassa … tassa); pi-4 has «အကြင်
  ပုဂ္ဂိုလ်၏ … ကို ပယ်ပြီး ဖြစ်၏». «အား» kept for identical yassa / tassa in the whole chapter.
- appahīno «မပယ်ရသေး» (not yet abandoned, pi-4) also after «no ca … pahīno» (as ch7a's «no ca … anuseti» = «မကိန်းအောင်း»).
- Pahīnavāra «ပယ်ပြီး ဖြစ်ခြင်းအလိုက် ဖော်ပြချက်»; dhātupucchā / -visajjanā «ဘုံများအကြောင်း အမေး / အဖြေ ဖော်ပြချက်».
- bhaṅgā: question «ပြိုပျက်ကြသနည်း» (how many are dissolved), answer «ပြိုပျက်သော ကိန်းအောင်းခြင်း မရှိ» (English rails
  "none are dissolved").
- «na X» planes as «X မဟုတ်သော ဘုံ» (the English rails "what is not the X element").
- Uppajjanavāro = Uppādavāro's Burmese (one heading for two Pāli words).

## Source slips (Pāli not changed; SLIPS / LINES in make_ch7b.py)
- 7-06 ^6-7-197: «Pajahanāvāre paṭilomaṃ.» for Pajahanavāre (read as Pajahanavāre).
- 7-08 ^6-7-… (line 56): «kāmadhātuyā tīsu vedanāsu, apariyāpanne» with a stray «,» inside the place list (read without it).
- 7-10 ^6-7-311: a bare line «9» (kept as the digit «9»).
- 7-10 ^6-7-335: «… kati anusayā bhaṅgā.» with «.» for «?» at the end of the line (same Burmese; the line ends «။»).
- 7-11: «Dhātuvisajjavāro.» for Dhātuvisajjanāvāro (heading «dhātuvisajjanāvāro»); ^6-7-348 «upapattināma natthi»
  (spacing) read as «upapatti nāma natthi».
- 7-09 ^6-7-… (line 43): variant «[pahīno (sī. ka.) anusayavārena pana na sameti]» kept as a variant bracket (Pāli
  reading «pahīno» in Latin, as the module's variants).
