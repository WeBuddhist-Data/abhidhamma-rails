# pi-7 4-01 kilesagocchaka (kilesa dyads + piṭṭhiduka): Burmese zero-shot notes

PROGRESS: DONE (2026-11-24). 4-01 (1191 segments, 1714 lines) written to
AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters/4-01-kilesagocchaka.md.
Checks: check_chapter_ids OK (1191 segments); check_marks OK; check_text (pi-3-mr/check_text.py on a «…Pe…»-folded
copy in pi-7-my/chk-pe/ch4-01/, deleted afterwards; check_text_pe7.py not run on the shared chk-pe/) OK, dashes match;
check_ch4-01.py 0 mismatches (S/P/C/O/N on 1714 lines, I 2985 sentences, T 147), reuse 91 / 91 terms + 586 / 586
sentences, identity with the finished groups 124 / 124, --sample identical, --mutate 12 / 12;
make_ch4-01.py --regress: 3-07, 3-08, 3-10 regenerate identical through the extended engine.

## Files
- make_ch4-01.py: generator. IMPORTS make_ch3-07-08-10.py (which imports make_ch3-01-02.py → make_ch2-03-06.py:
  PRIMARY my7_formulas + make_sample + make_ch1-01, FALLBACK make_ch1-03-05); no main block of another script runs,
  no file of the sample or of another group is edited. Its gocchaka glue (prep_mine for dyads 1/4/5/6 via GOC["kil"])
  and 3-01 … 3-02's dyad machinery are reused unchanged; this script adds DYADS / DYAD_OF entries (26 dyads), wraps
  prep_dyad and set_dyad (only for its own dyads), adds names, nouns, notes, unique sentences and a coordination
  fallback in the lexicon frame. `--dev`, `--regress`, `--slips`, `--out DIR` as 3-07-08-10.
- check_ch4-01.py: checker (adapted from check_ch3-07-08-10.py; own typed copy of the 26 dyads, names and the
  raw-Pāli term regexes; the sister dyads of the piṭṭhiduka are read as one family); `--sample --pe --mutate --groups`.
- chk-ch4-01/: my scratch (dev output, query scripts).

## How these dyads are run
- Kilesa dyads: kil1 (kilesa / no kilesa), kil2 (saṃkilesika), kilS (saṃkiliṭṭha), kilP (kilesasampayutta), kil4
  («kilesā ceva saṃkilesikā ca»), kilB («kilesā ceva saṃkiliṭṭhā ca», own glue prep_kilB in the pattern of dyad 4),
  kil5 («kilesā ceva kilesasampayuttā ca»), kil6 (kilesavippayutta saṃkilesika / asaṃkilesika). kil1 / 4 / 5 / 6 use
  3-07 … 3-10's prep_mine (GOC["kil"] = kiles / saṃkilesik / asaṃkilesik).
- The eighth kilesa dyad (= the sixth dyad of the other gocchakas) uses exactly the forms of 3-03-06 / 3-07-08-10:
  «ကိလေသာနှင့် ကင်းကွာသော်လည်း ကိလေသာ၏ အာရုံ ဖြစ်နိုင်သော» / «ကိလေသာနှင့် ကင်းကွာ၊ ကိလေသာ၏ အာရုံ မဖြစ်နိုင်သော».
- Piṭṭhiduka dyads: plain a-stem pairs (multi-word keys «dassanena pahātabb» / «nadassanena pahātabb» …); terms from
  the pi-1 final Mātikā ^1-M2-83 … ^1-M2-100.
- Nouns (pi-1): kilesa «ကိလေသာ» (^1-M2-75); the ten kilesas (^1-1565) lobha «လောဘ», dosa «ဒေါသ», moha «မောဟ», māna
  «မာန», diṭṭhi «အယူ», vicikicchā «ယုံမှားမှု», thina «ထိုင်းမှိုင်းမှု», uddhacca «ယောက်ယက်ခတ်မှု», ahirika «ဒုစရိုက်ကို
  မရှက်မှု», anottappa «ဒုစရိုက်ကို မကြောက်ရွံ့မှု»; vitakka «စတင်ကြံစည်မှု», vicāra «ဆက်လက်သုံးသပ်မှု», pīti «ပီတိ», sukha
  «သာယာမှု» (the module's sukhaṃ), upekkhā «ဥပေက္ခာ»; micchattaniyata «မှားယွင်းမှု၌ ကျိန်းသေသော».
  «mānaṃ» is NOT a FIXED noun (the module's noun parser would read it inside «dhammānaṃ» and the sample would stop).
- Coordinations with khandhas («khandhe ca vitakkañca», «khandhā ca vitakko ca», «khandhānaṃ (ca) vitakkassa ca»,
  «vitakko ca sampayuttakā khandhā ca» …) rendered once by the module's np_my (as 3-07 … 3-10's lobha).
- Coordination fallback in the lexicon frame: copied from make_ch2-01-02.py (b) (the group that first rendered
  vitakka / pīti coordinations), used ONLY where the engine's own lexicon frame fails (51 units); a group whose members
  are all nominative-or-accusative is accusative only before an object word (ārabbha, garuṃ katvā, paṭicca …),
  otherwise nominative (2-01-02's copy takes «ကို» there).
- Every note the engines do not render is a placeholder (D.NOTEP), its Burmese written from the shared words.
- Coordinator decisions: «Anulomaṃ.» (order) «အဟုတ်ပြ ပုံစံ။» (19 lines); «(anulomaṃ)» «(အဟုတ်ပြ ပုံစံ)»; «anulomaṃ»
  (mind moment) «လျော်ညီခြင်း စိတ်» (20); «Sahajātā –» bare «အတူ ပေါ်ပေါက်ခြင်း –» in atthi / vippayutta (11), in the
  kamma sentences «အတူ ပေါ်ပေါက်သည့် ကံ –» (19, incl. «Sahajātā (saṃkhittaṃ)»); the engine reads the kamma section from
  the «*Kammapaccayo*» heading only, so in kamma passages without that heading the label is marked by prep (parser token
  «Sahajātākamma», LEX = the module's «sahajātā»); asaññasattānaṃ «…တို့၏» (1); the heinous deeds as in pi-5 (in
  memory, this chapter only): mātughātikamma «အမိကို သတ်ခြင်း ကံ», pitughātikamma «အဖကို သတ်ခြင်း ကံ», arahantaghātikamma
  «ရဟန္တာကို သတ်ခြင်း ကံ», ruhiruppādakamma «ဘုရား၏ ကိုယ်တော်မှ သွေးကို ထွက်စေခြင်း ကံ», saṅghabhedakamma «သံဃာကို
  သင်းခွဲခြင်း ကံ» (all pi-5 ^16 witnessed); the verbs «mātaraṃ jīvitā voropeti …» keep the module's (1-01) Burmese.

## Readings for the parser (in memory; the Burmese is the module's rendering of the same members)
- «A, B, Xassa ca §C§» (comma before the last recipient with «ca»; X = vitakka / pīti / sukha / upekkhā): read «A, B
  Xassa ca» (as 2-03 … 2-06 «āvajjanāya mohassa ca»).
- «Xñca vitakko ca …» / «Xñca sukhañca …» (enclitic written together): «Xṃ ca vitakko ca» (= 2-01 … 2-02 NCA).
- «pīti ca cittasamuṭṭhānañca rūpaṃ» parsed as «pīti cittasamuṭṭhānañca rūpaṃ» (as «vitakko cittasamuṭṭhānañca rūpaṃ»).
- «khandhā ca sukhañca pacchim…» (anantara): nominative «sukhaṃ» marked (token «sukhaṃ_n»), else the engine took it as
  a recipient.
- «… khandhānaṃ vitakkassa ca» read «khandhānaṃ ca vitakkassa ca» (as 2-03 … 2-06 / 3-07 … 3-10).

## Source slips (translated as written)
- rūpāvacara dyad, paṭiccavāra naadhipati: «rūpāvacarādhipati vipākaṃ, rūpāvacaraṃ ekaṃ khandhaṃ» (comma after
  «vipākaṃ»; the kāmāvacara dyad has «…adhipati, vipākaṃ …»): «… အကြီးအမှူး ကံ၏ အကျိုး၊ … အစုအဝေး …».
- bhāvanāya pahātabbahetuka dyad, pañhāvāra: «…pe… novigatapaccayena paccayo.» closing an anuloma list (the others
  close with «avigata»): the negative frame «ပျောက်ကွယ်ခြင်းဟူသော အကြောင်းဖြင့် အကြောင်း ဖြစ်သည် မဟုတ်».
- End of the bhāvanāya pahātabbahetuka dyad: two sentences of the dassana / bhāvanā dyads («Nadassanena pahātabbo
  dhammo …», «Bhāvanāya pahātabbo dhammo nabhāvanāya …») stand there: written with those dyads' terms.
- sukha dyad, anantara: «… upapatticittassa sukhasahagataṃ bhavaṅgañca …» (no «…pe…» / comma between two members):
  rendered as written (no mark added).
- The engine's «negated count written apart / with a hyphen» slip rule fired (module).

## Supplied words (only for an obvious omission)
- «mahābhūte paccayā cittasamuṭṭhānaṃ.» (dassanena pahātabba, paccayavāra): «ရုပ်» supplied.
- Elliptic nouns in notes: «uddhaccasahagate (tīṇi)», «nabhāvanāya pahātabbahetukakāraṇā», «Nakāmāvacaraṃ
  (paṭiccavārasadisaṃ)», «nabhāvanāya pahātabbabhājana-», «sappītike / sappītikakaraṇena»: term + «သဘောတရား» (the
  term is attributive in Burmese; as D's TERM_REF convention).
- «yathā … ekoyeva moho», «yathā … hetupaccayasadisāyeva pañhā»: copula «ဖြစ်သကဲ့သို့».

## Unsure Pāli (for the reviewer)
- «Parantena» (note to the dassana / bhāvanā dyads): read «at the end» «အဆုံးပိုင်း၌».
- «arūpaduka» (notes of niyyānika / niyata / saraṇa): rendered as written «ရုပ်မရှိသော ဘုံ နှစ်မျိုးတွဲ» (probably the
  arūpāvacara dyad, which the same notes also name in full).
- «Itare dve anantarā …» (kil4 note): read «the other two anantara (conditions)» «အခြား ချက်ချင်း နောက်၌ ဖြစ်စေခြင်း နှစ်ခု»;
  «Ghaṭanānantarampi» = ghaṭanā + anantara (as 3-07 … 3-10's «ghaṭanādhipatipi»).
- «pañcaviññāṇā atirekā moho vitakkaṃ» (vitakka note): «သိစိတ် ငါးပါး ပိုသည်၊ မောဟ၊ စတင်ကြံစည်မှု» (elliptic list).
- «yaṃ vatthuṃ āmasantassa» (niyata, ārammaṇa): āmasati «စွဲကိုင်သူ၏».
- «(tīṇi, pacchājātā)»: «(သုံးခု၊ နောက်မှ ဖြစ်ပေါ်ခြင်း)».

## For the harmonise pass
- H7: the finished groups 3-07 (1), 3-08 (2), 3-10 (2) and 3-09 (6, other agent) have the bare «အတူ ပေါ်ပေါက်ခြင်း –»
  after «… ခဏ ကွဲပြားသည့် ကံ။» in kamma passages without a «*Kammapaccayo*» heading (same engine cause); 4-01 marks them.
- chandarāga: pi-2 termbase «လိုလားမှု ရာဂ» vs pi-7 2-03 … 2-06 SK «ဆန္ဒရာဂ» («sakabhaṇḍe chandarāgo» «မိမိ ပစ္စည်း၌ ဖြစ်သော
  ဆန္ဒရာဂ»); 4-01 follows pi-7 (the engine's line and my note agree).
- Heinous deeds: the module's 1-01 «… သတ်သော ကံ / သံဃာကို ဖြိုခွဲသော ကံ» replaced by the pi-5 forms in 4-01 only.
- «(sahajātaṃ sahajātasadisaṃ, purejātaṃ purejātasadisaṃ.)»: the engine's note frame gives «အတူ ပေါ်ပေါက်ခြင်းဟူသော
  အကြောင်းသည် …»; written as 3-10 «(imesu …)» with the bare names.
- Dyad names: the piṭṭhiduka names follow 2-03 / 2-04's triad names («… ပယ်ခြင်း», «… ပယ်ရမည့် အမြစ်») and 3-01's «X ရှိခြင်း».

## New terms and formulas (Pāli = Burmese)
### Cluster names (pi-1 final): Kilesagocchakaṃ = ကိလေသာတို့၏ အစု (^1-M-2-12-0); Piṭṭhidukaṃ = နောက်ဆုံး နှစ်မျိုးတွဲများ (^1-M-2-13-0)
### Dyad terms (pi-1 final ^1-M2-75 … ^1-M2-100; attributive, without « သဘောတရားများ»): see make_ch4-01.DYADS_ADD
### Every new string of the generator (NEW: terms, names, headings, words)
- kilesavippayutto saṃkilesiko (dyad term) = ကိလေသာနှင့် ကင်းကွာသော်လည်း ကိလေသာ၏ အာရုံ ဖြစ်နိုင်သော
- kilesavippayutto asaṃkilesiko (dyad term) = ကိလေသာနှင့် ကင်းကွာ၊ ကိလေသာ၏ အာရုံ မဖြစ်နိုင်သော
- Kilesadukaṃ = ကိလေသာ နှစ်မျိုးတွဲ
- Saṃkilesikadukaṃ = ကိလေသာ၏ အာရုံ ဖြစ်နိုင်ခြင်း နှစ်မျိုးတွဲ
- Saṃkiliṭṭhadukaṃ = ကိလေသာဖြင့် ညစ်နွမ်းခြင်း နှစ်မျိုးတွဲ
- Kilesasampayuttadukaṃ = ကိလေသာနှင့် ယှဉ်တွဲခြင်း နှစ်မျိုးတွဲ
- Kilesasaṃkilesikadukaṃ = ကိလေသာ ဖြစ်ခြင်းနှင့် ကိလေသာ၏ အာရုံ ဖြစ်နိုင်ခြင်း နှစ်မျိုးတွဲ
- Kilesasaṃkiliṭṭhadukaṃ = ကိလေသာ ဖြစ်ခြင်းနှင့် ကိလေသာဖြင့် ညစ်နွမ်းခြင်း နှစ်မျိုးတွဲ
- Kilesakilesasampayuttadukaṃ = ကိလေသာ ဖြစ်ခြင်းနှင့် ကိလေသာနှင့် ယှဉ်တွဲခြင်း နှစ်မျိုးတွဲ
- Kilesavippayuttasaṃkilesikadukaṃ = ကိလေသာနှင့် ကင်းကွာခြင်းနှင့် ကိလေသာ၏ အာရုံ ဖြစ်နိုင်ခြင်း နှစ်မျိုးတွဲ
- Dassanenapahātabbadukaṃ = သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ခြင်း နှစ်မျိုးတွဲ
- Bhāvanāyapahātabbadukaṃ = ဘာဝနာ ပွားများခြင်းဖြင့် ပယ်ခြင်း နှစ်မျိုးတွဲ
- Dassanenapahātabbahetukadukaṃ = သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ရမည့် အမြစ် နှစ်မျိုးတွဲ
- Bhāvanāyapahātabbahetukadukaṃ = ဘာဝနာ ပွားများခြင်းဖြင့် ပယ်ရမည့် အမြစ် နှစ်မျိုးတွဲ
- Savitakkadukaṃ = စတင်ကြံစည်မှု ရှိခြင်း နှစ်မျိုးတွဲ
- Savicāradukaṃ = ဆက်လက်သုံးသပ်မှု ရှိခြင်း နှစ်မျိုးတွဲ
- Sappītikadukaṃ = ပီတိ ရှိခြင်း နှစ်မျိုးတွဲ
- Pītisahagatadukaṃ = ပီတိနှင့်အတူ ဖြစ်ခြင်း နှစ်မျိုးတွဲ
- Sukhasahagatadukaṃ = သာယာမှုနှင့်အတူ ဖြစ်ခြင်း နှစ်မျိုးတွဲ
- Upekkhāsahagatadukaṃ = ဥပေက္ခာနှင့်အတူ ဖြစ်ခြင်း နှစ်မျိုးတွဲ
- Kāmāvacaradukaṃ = ကာမဘုံနှင့် ဆိုင်ခြင်း နှစ်မျိုးတွဲ
- Rūpāvacaradukaṃ = သိမ်မွေ့သော ရုပ်ဘုံနှင့် ဆိုင်ခြင်း နှစ်မျိုးတွဲ
- Arūpāvacaradukaṃ = ရုပ်မရှိသော ဘုံနှင့် ဆိုင်ခြင်း နှစ်မျိုးတွဲ
- Pariyāpannadukaṃ = ဘဝဘုံတို့၌ အကျုံးဝင်ခြင်း နှစ်မျိုးတွဲ
- Niyyānikadukaṃ = လွတ်မြောက်ရာသို့ ပို့ဆောင်ခြင်း နှစ်မျိုးတွဲ
- Niyatadukaṃ = ကျိန်းသေခြင်း နှစ်မျိုးတွဲ
- Sauttaradukaṃ = ထိုထက် သာလွန်သည် ရှိခြင်း နှစ်မျိုးတွဲ
- Saraṇadukaṃ = ပဋိပက္ခ ရှိခြင်း နှစ်မျိုးတွဲ
- 1-6. Paṭiccavārādi = 1-6. မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက် စသည်
- 4-5. Nissaya-saṃsaṭṭhavāro = 4-5. အမှီပြု၍ ဖြစ်ပေါ်ခြင်းနှင့် ရောနှောခြင်းအလိုက် ဖော်ပြချက်
- uddhacca = ယောက်ယက်ခတ်မှု
- vikkhambhite = ခွာထားပြီးသော
- dibbena = နတ်
- domanassassa = စိတ်ဆင်းရဲမှု
- ekaṃyeva = တစ်ခုတည်း
- nava pañhā = ပြဿနာ ကိုးခု
- sukhaṃ_n = သာယာမှု
- sahajātākamma = အတူ ပေါ်ပေါက်သည့် ကံ
- dibbaṃ cakkhuṃ = နတ်မျက်စိ
- dibbaṃ sotadhātuṃ = နတ်နား ဓာတ်
- kāyaviññāṇaṃ = ကိုယ် သိစိတ်
- rūpajīvitindriyaṃ = ရုပ် အသက်၏ စွမ်းရည်
- atthapaṭisambhidāya = အကျိုးအနက်ကို ပိုင်းခြားသိသော ဉာဏ်
- dhammapaṭisambhidāya = တရားကို ပိုင်းခြားသိသော ဉာဏ်
- niruttipaṭisambhidāya = စကားဖြင့် ဖော်ပြမှုကို ပိုင်းခြားသိသော ဉာဏ်
- sahajātā (a kind of kamma, in a note) = အတူ ပေါ်ပေါက်သည့် ကံ
- pavatti = ဘဝ ဖြစ်စဉ်
- ahetukā (inside a note, plural) = အမြစ် မရှိကြသည်
- uddharitabbo = ထုတ်နုတ်ရမည်
- ṭhapetabbo = ထားရမည်
- atirekā = ပိုသည်
- likhita = ရေးထားသော
- parantena = အဆုံးပိုင်း၌
- sakabhaṇḍachandarāgo = မိမိ ပစ္စည်း၌ ဖြစ်သော ဆန္ဒရာဂ
- yadipi … (concessive) = အကယ်၍
- nānāpadāyeva = ကွဲပြားသော ပုဒ်များပင်
- pākatikā = ပကတိအတိုင်း
- gahetabbā = ယူရမည်
- bhājanakāraṇe = ခွဲခြားသည့် နည်းလမ်း၌
- labbhati = ရသည်
- vibhāgo = ခွဲခြားချက်
- -karaṇena (by the treatment of) = ပြုပုံအတိုင်း
- daṭṭhabbaṃ = ရှုရမည်
- lekhaṃ = စာ
- passitvā = ကြည့်၍
- bhāvanā (inside a note) = ဘာဝနာ ပွားများခြင်း
- missake = ရောနှောသော အပိုင်း၌
- na sameti = မညီ
- arūpaduka (inside a note) = ရုပ်မရှိသော ဘုံ နှစ်မျိုးတွဲ
- āmasantassa = စွဲကိုင်သူ၏
### Notes written here (Pāli note = Burmese)
- (Catuttho bhāgo) = (စတုတ္ထ အပိုင်း)
- (arūpe dosamūlakaṃ natthi) = (ရုပ်မရှိသော ဘုံ၌ ဒေါသကို အခြေခံခြင်း မရှိ)
- (evaṃ navapi pañhā kātabbā) = (ဤသို့ ပြဿနာ ကိုးခုလုံးကို ပြုရမည်)
- (Evaṃ sabbe paccayā kātabbā.) = (ဤသို့ အကြောင်း အားလုံးကို ပြုရမည်။)
- (Evaṃ itare dve gaṇanāpi sahajātavāropi kātabbo.) = (ဤသို့ အခြား ရေတွက်ချက် နှစ်ခုကိုလည်း၊ အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်ကိုလည်း ပြုရမည်။)
- (Ārammaṇapaccaye nokilesamūle pañca viññāṇā kātabbā.) = (အာရုံဟူသော အကြောင်း၌ ကိလေသာ မဟုတ်သော သဘောတရားကို အခြေခံခြင်း၌ သိစိတ် ငါးပါးကို ပြုရမည်။)
- (Cakkaṃ. Evaṃ nava pañhā kātabbā.) = (စက်ဝိုင်း။ ဤသို့ ပြဿနာ ကိုးခုကို ပြုရမည်။)
- (evaṃ nahetupañhā cattāri kātabbā.) = (ဤသို့ အမြစ်ဟူသော အကြောင်း မဟုတ်ခြင်း၏ ပြဿနာ လေးခုကို ပြုရမည်။)
- (saṃkhittaṃ. Vitthāretabbaṃ.) = (အကျဉ်းချုပ်။ အကျယ် ချဲ့ရမည်။)
- (sahajātaṃ sahajātasadisaṃ, purejātaṃ purejātasadisaṃ.) = (အတူ ပေါ်ပေါက်ခြင်းသည် အတူ ပေါ်ပေါက်ခြင်းနှင့် တူသည်၊ ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်းသည် ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်းနှင့် တူသည်။)
- (saṃkhittaṃ. Sahajātaṃ sahajātasadisaṃ, purejātaṃ purejātasadisaṃ.) = (အကျဉ်းချုပ်။ အတူ ပေါ်ပေါက်ခြင်းသည် အတူ ပေါ်ပေါက်ခြင်းနှင့် တူသည်၊ ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်းသည် ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်းနှင့် တူသည်။)
- (yathā lokiyadukaṃ, evaṃ ninnānākaraṇaṃ.) = (လောကနှင့် သက်ဆိုင်ခြင်း နှစ်မျိုးတွဲကဲ့သို့ ထိုနည်းတူ ကွဲပြားချက် မရှိ။)
- (Yathā lokiyadukaṃ, evaṃ ninnānākaraṇaṃ.) = (လောကနှင့် သက်ဆိုင်ခြင်း နှစ်မျိုးတွဲကဲ့သို့ ထိုနည်းတူ ကွဲပြားချက် မရှိ။)
- (Kilesasampayuttadukaṃ saṃkiliṭṭhadukasadisaṃ, ninnānākaraṇaṃ.) = (ကိလေသာနှင့် ယှဉ်တွဲခြင်း နှစ်မျိုးတွဲသည် ကိလေသာဖြင့် ညစ်နွမ်းခြင်း နှစ်မျိုးတွဲနှင့် တူသည်၊ ကွဲပြားချက် မရှိ။)
- (Evaṃ paṭiccavāropi sahajātavāropi paccayavāropi nissayavāropi saṃsaṭṭhavāropi sampayuttavāropi kilesadukasadisā. Ninnānākaraṇaṃ. Āmasanaṃ nānaṃ.) = (ဤသို့ မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်လည်း၊ အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း၊ အကြောင်းပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်လည်း၊ အမှီပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်လည်း၊ ရောနှောခြင်းအလိုက် ဖော်ပြချက်လည်း၊ ယှဉ်တွဲခြင်းအလိုက် ဖော်ပြချက်လည်း ကိလေသာ နှစ်မျိုးတွဲနှင့် တူကြသည်။ ကွဲပြားချက် မရှိ။ ရည်ညွှန်းပုံသည် ကွဲပြားချက် ဖြစ်သည်။)
- (evaṃ cattāri, kilesadukasadisaṃ.) = (ဤသို့ လေးခု၊ ကိလေသာ နှစ်မျိုးတွဲနှင့် တူသည်။)
- (itare dve kilesadukasadisā, ghaṭanārammaṇāpi kilesadukasadisā) = (အခြား နှစ်ခုသည် ကိလေသာ နှစ်မျိုးတွဲနှင့် တူကြသည်၊ ပေါင်းစပ်ချက် အာရုံတို့သည်လည်း ကိလေသာ နှစ်မျိုးတွဲနှင့် တူကြသည်)
- (Itare dvepi kilesadukasadisā. Ghaṭanādhipatipi.) = (အခြား နှစ်ခုလုံးလည်း ကိလေသာ နှစ်မျိုးတွဲနှင့် တူကြသည်။ ပေါင်းစပ်ချက် အကြီးအမှူးလည်း။)
- (kilesadukasadisā) = (ကိလေသာ နှစ်မျိုးတွဲနှင့် တူကြသည်)
- (Itare dve anantarā kilesadukasadisā, ninnānākaraṇā. Ghaṭanānantarampi sabbe paccayā kilesadukasadisā, ninnānākaraṇā. Upanissaye lokuttaraṃ natthi, idaṃ dukaṃ kilesadukasadisaṃ, ninnānākaraṇaṃ.) = (အခြား ချက်ချင်း နောက်၌ ဖြစ်စေခြင်း နှစ်ခုသည် ကိလေသာ နှစ်မျိုးတွဲနှင့် တူကြသည်၊ ကွဲပြားချက် မရှိ။ ပေါင်းစပ်ချက် ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းလည်း၊ အကြောင်း အားလုံးတို့သည် ကိလေသာ နှစ်မျိုးတွဲနှင့် တူကြသည်၊ ကွဲပြားချက် မရှိ။ အားကြီးသော အမှီဟူသော အကြောင်း၌ လောကကို ကျော်လွန်သော သဘောတရား မရှိ၊ ဤ နှစ်မျိုးတွဲသည် ကိလေသာ နှစ်မျိုးတွဲနှင့် တူသည်၊ ကွဲပြားချက် မရှိ။)
- (Evaṃ itare dve gaṇanāpi sahajātavāropi paccayavāropi nissayavāropi saṃsaṭṭhavāropi sampayuttavāropi paṭiccavārasadisā.) = (ဤသို့ အခြား ရေတွက်ချက် နှစ်ခုလည်း၊ အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း၊ အကြောင်းပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်လည်း၊ အမှီပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်လည်း၊ ရောနှောခြင်းအလိုက် ဖော်ပြချက်လည်း၊ ယှဉ်တွဲခြင်းအလိုက် ဖော်ပြချက်လည်း မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူကြသည်။)
- (Itarepi tīṇi kātabbā.) = (အခြား သုံးခုကိုလည်း ပြုရမည်။)
- (Dve adhipati tīṇipi kātabbā, itare dvepi tīṇi kātabbā.) = (အကြီးအမှူး နှစ်ခု၌ သုံးခုလုံးကို ပြုရမည်၊ အခြား နှစ်ခုလုံး၌လည်း သုံးခုကို ပြုရမည်။)
- (navapi kātabbā, āvajjanāpi vuṭṭhānampi natthi) = (ကိုးခုလုံးကို ပြုရမည်၊ စိတ်ညွတ်ခြင်းလည်း၊ ထမြောက်ခြင်း စိတ်လည်း မရှိ)
- (purejātapaccayo pacchājātapaccayopi natthi) = (ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်းဟူသော အကြောင်း၊ နောက်မှ ဖြစ်ပေါ်ခြင်းဟူသော အကြောင်းလည်း မရှိ)
- (Navapi, tīṇiyeva padā kātabbā.) = (ကိုးခုလုံး၊ ပုဒ် သုံးခုကိုသာ ပြုရမည်။)
- (Kilesasaṃkiliṭṭhadukasadisaṃ ninnānākaraṇaṃ, sabbe vārā.) = (ကိလေသာ ဖြစ်ခြင်းနှင့် ကိလေသာဖြင့် ညစ်နွမ်းခြင်း နှစ်မျိုးတွဲနှင့် တူသည်၊ ကွဲပြားချက် မရှိ၊ ဖော်ပြချက် အားလုံး။)
- (Itare dve gaṇanāpi sahajātavāropi kātabbo.) = (အခြား ရေတွက်ချက် နှစ်ခုကိုလည်း၊ အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်ကိုလည်း ပြုရမည်။)
- (Itare dve gaṇanāpi nissayavāropi kātabbo.) = (အခြား ရေတွက်ချက် နှစ်ခုကိုလည်း၊ အမှီပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်ကိုလည်း ပြုရမည်။)
- (yathā dassanadukaṃ, evaṃ vitthāretabbaṃ, ninnānākaraṇaṃ) = (သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ခြင်း နှစ်မျိုးတွဲကဲ့သို့ ထိုနည်းတူ အကျယ် ချဲ့ရမည်၊ ကွဲပြားချက် မရှိ)
- (Paccayavārapaccanīye nahetupaccaye uddhaccasahagate tīṇi, moho uddharitabbo. Sabbepi vārā dassanadukasadisā, uddhaccapaccanīyampi nānaṃ.) = (အကြောင်းပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်၏ အငြင်းပြ ပုံစံ၌ အမြစ်ဟူသော အကြောင်း မဟုတ်ခြင်း၌ ယောက်ယက်ခတ်မှုနှင့်အတူ ဖြစ်သော သဘောတရား၌ သုံးခု၊ မောဟကို ထုတ်နုတ်ရမည်။ ဖော်ပြချက် အားလုံးလည်း သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ခြင်း နှစ်မျိုးတွဲနှင့် တူကြသည်၊ ယောက်ယက်ခတ်မှု၏ အငြင်းပြ ပုံစံလည်း ကွဲပြားချက် ဖြစ်သည်။)
- (dassanadukasadisā bhāvanā ninnānākaraṇā) = (သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ခြင်း နှစ်မျိုးတွဲနှင့် တူကြသည်၊ ဘာဝနာ ပွားများခြင်း၊ ကွဲပြားချက် မရှိ)
- (Sabbapaccayā dassanadukasadisā, bhāvanā ninnānākaraṇā.) = (အကြောင်း အားလုံးတို့သည် သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ခြင်း နှစ်မျိုးတွဲနှင့် တူကြသည်၊ ဘာဝနာ ပွားများခြင်း၊ ကွဲပြားချက် မရှိ။)
- (Paccanīyavibhaṅgo dassanadukasadiso vibhajitabbo. Evaṃ tīṇi gaṇanāpi gaṇetabbā.) = (အငြင်းပြ ပုံစံ၏ ခွဲခြမ်းစိတ်ဖြာခြင်းကို သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ခြင်း နှစ်မျိုးတွဲနှင့် တူအောင် ခွဲခြမ်းစိတ်ဖြာရမည်။ ဤသို့ ရေတွက်ချက် သုံးခုကိုလည်း ရေတွက်ရမည်။)
- (Avasesesu dvīsu anantarūpanissayo, pakatūpanissayo.) = (ကြွင်းသော နှစ်ခု၌ ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းဖြင့် အားကြီးသော အမှီ၊ ပကတိ အားကြီးသော အမှီ။)
- (Saṃkhittaṃ. Vatthupurejātaṃ saṃkhittaṃ.) = (အကျဉ်းချုပ်။ မှီရာ ဝတ္ထု ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်း အကျဉ်းချုပ်။)
- (Vatthupurejātaṃ saṃkhittaṃ.) = (မှီရာ ဝတ္ထု ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်း အကျဉ်းချုပ်။)
- (Evaṃ paṭiccavāropi sahajātavāropi paccayavāropi nissayavāropi saṃsaṭṭhavāropi sampayuttavāropi dassanena pahātabbahetukadukasadisā. Uddhaccasahagato moho vicikicchāsahagatamohaṭṭhāne ṭhapetabbo.) = (ဤသို့ မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်လည်း၊ အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း၊ အကြောင်းပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်လည်း၊ အမှီပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်လည်း၊ ရောနှောခြင်းအလိုက် ဖော်ပြချက်လည်း၊ ယှဉ်တွဲခြင်းအလိုက် ဖော်ပြချက်လည်း သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ရမည့် အမြစ် နှစ်မျိုးတွဲနှင့် တူကြသည်။ ယောက်ယက်ခတ်မှုနှင့်အတူ ဖြစ်သော မောဟကို ယုံမှားမှုနှင့်အတူ ဖြစ်သော မောဟ၏ နေရာ၌ ထားရမည်။)
- (dassanena pahātabbahetukadukasadisā) = (သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ရမည့် အမြစ် နှစ်မျိုးတွဲနှင့် တူကြသည်)
- (ārabbha dassanena pahātabbahetukadukasadisā) = (အာရုံပြု၍ သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ရမည့် အမြစ် နှစ်မျိုးတွဲနှင့် တူကြသည်)
- (ghaṭanārammaṇā tīṇipi kātabbā) = (ပေါင်းစပ်ချက် အာရုံ သုံးခုလုံးကို ပြုရမည်)
- (Anantarapaccaye nabhāvanāya pahātabbahetukakāraṇā vicikicchāsahagato moho na kātabbo, uddhaccasahagato moho kātabbo.) = (ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းဟူသော အကြောင်း၌ ဘာဝနာ ပွားများခြင်းဖြင့် ပယ်ရမည့် အမြစ် ရှိသည် မဟုတ်သော သဘောတရား ဖြစ်သည့် အကြောင်းကြောင့် ယုံမှားမှုနှင့်အတူ ဖြစ်သော မောဟကို မပြုရ၊ ယောက်ယက်ခတ်မှုနှင့်အတူ ဖြစ်သော မောဟကို ပြုရမည်။)
- (ghaṭanūpanissayāpi tīṇipi kātabbā) = (ပေါင်းစပ်ချက် အားကြီးသော အမှီလည်း သုံးခုလုံးကို ပြုရမည်)
- (nabhāvanāya pahātabbabhājanakāraṇe nānākkhaṇikā labbhati ) = (ဘာဝနာ ပွားများခြင်းဖြင့် ပယ်ရမည် မဟုတ်သော သဘောတရားကို ခွဲခြားသည့် နည်းလမ်း၌ ခဏ ကွဲပြားသည့် ကံကို ရသည်)
- (Saṃkhittaṃ. Yathā dassanena pahātabbahetukadukaṃ evaṃ bhāvanāya pahātabbahetukapaccayāpi paccanīyāpi vibhāgopi gaṇanāpi ninnānākaraṇā.) = (အကျဉ်းချုပ်။ သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ရမည့် အမြစ် နှစ်မျိုးတွဲကဲ့သို့ ထိုနည်းတူ ဘာဝနာ ပွားများခြင်းဖြင့် ပယ်ရမည့် အမြစ် ရှိသော သဘောတရား၏ အကြောင်းတို့လည်း၊ အငြင်းပြ ပုံစံတို့လည်း၊ ခွဲခြားချက်လည်း၊ ရေတွက်ချက်တို့လည်း ကွဲပြားချက် မရှိ။)
- (Parantena sakabhaṇḍachandarāgopi kātabbo.) = (အဆုံးပိုင်း၌ မိမိ ပစ္စည်း၌ ဖြစ်သော ဆန္ဒရာဂကိုလည်း ပြုရမည်။)
- (Parantena "sakabhaṇḍachandarāgo"ti kātabbaṃ.) = (အဆုံးပိုင်း၌ “မိမိ ပစ္စည်း၌ ဖြစ်သော ဆန္ဒရာဂ”ဟု ပြုရမည်။)
- (Savitakkamūlakā avasesā dve pañhā kātabbā, ahetukaṃ ninnānaṃ.) = (စတင်ကြံစည်မှု ရှိသော သဘောတရားကို အခြေခံခြင်း၌ ကြွင်းသော ပြဿနာ နှစ်ခုကို ပြုရမည်၊ အမြစ် မရှိသည်၊ ကွဲပြားမှု မရှိ။)
- (Saṃkhittaṃ. Hetupaccayasadisaṃ. "Ahetuka"nti niyāmetabbaṃ.) = (အကျဉ်းချုပ်။ အမြစ်ဟူသော အကြောင်းနှင့် တူသည်။ “အမြစ် မရှိသည်”ဟု သတ်မှတ်ရမည်။)
- (Avasesā dve pañhā hetupaccayasadisā ninnānā, ahetukanti niyāmetabbaṃ.) = (ကြွင်းသော ပြဿနာ နှစ်ခုသည် အမြစ်ဟူသော အကြောင်းနှင့် တူကြသည်၊ ကွဲပြားမှု မရှိ၊ အမြစ် မရှိသည်ဟု သတ်မှတ်ရမည်။)
- (paṭisandhiyāpi dve) = (ပဋိသန္ဓေ၌လည်း နှစ်ခု)
- (paṭisandhiyāpi pavattisadisāyeva) = (ပဋိသန္ဓေ၌လည်း ဘဝ ဖြစ်စဉ်နှင့် တူသည်ပင်)
- (paṭisandhikkhaṇe dve kātabbā) = (ပဋိသန္ဓေ နေသော ခဏ၌ နှစ်ခုကို ပြုရမည်)
- (tīṇi, paṭisandhiyāpi) = (သုံးခု၊ ပဋိသန္ဓေ၌လည်း)
- (Nava pañhā kātabbā. "Ahetukā"ti niyāmetabbā tīṇiyeva. Moho uddharitabbo, yathā paṭiccavāre hetupaccayasadisāyeva pañhā pañcaviññāṇā atirekā moho vitakkaṃ.) = (ပြဿနာ ကိုးခုကို ပြုရမည်။ “အမြစ် မရှိကြသည်”ဟု သုံးခုကိုသာ သတ်မှတ်ရမည်။ မောဟကို ထုတ်နုတ်ရမည်၊ မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်၌ အမြစ်ဟူသော အကြောင်းနှင့် တူသော ပြဿနာများပင် ဖြစ်သကဲ့သို့ သိစိတ် ငါးပါး ပိုသည်၊ မောဟ၊ စတင်ကြံစည်မှု။)
- (Evaṃ cha pañhā kātabbā anulomasadisā, ahetukāti niyāmetabbā, tīṇiyeva, moho uddharitabbo.) = (ဤသို့ ပြဿနာ ခြောက်ခုကို ပြုရမည်၊ အဟုတ်ပြ ပုံစံနှင့် တူကြသည်၊ အမြစ် မရှိကြသည်ဟု သတ်မှတ်ရမည်၊ သုံးခုသာ၊ မောဟကို ထုတ်နုတ်ရမည်။)
- (heṭṭhā likhitaṃ lekhaṃ iminā kāraṇena daṭṭhabbaṃ) = (အထက်၌ ရေးထားသော စာကို ဤနည်းလမ်းဖြင့် ရှုရမည်)
- (tīṇipi upanissayā sabbattha kātabbā) = (အားကြီးသော အမှီ သုံးခုလုံးကို နေရာတိုင်း၌ ပြုရမည်)
- (dutiyavāre likhitapadā sabbe kātabbā) = (ဒုတိယ ဖော်ပြချက်၌ ရေးထားသော ပုဒ် အားလုံးကို ပြုရမည်)
- (tīṇi, pacchājātā) = (သုံးခု၊ နောက်မှ ဖြစ်ပေါ်ခြင်း)
- (Evaṃ cattāri, sahajātāpi nānākkhaṇikāpi kātabbā.) = (ဤသို့ လေးခု၊ အတူ ပေါ်ပေါက်သည့် ကံကိုလည်း၊ ခဏ ကွဲပြားသည့် ကံကိုလည်း ပြုရမည်။)
- (paṭisandhikkhaṇe sahajātāpi dvepi kātabbā) = (ပဋိသန္ဓေ နေသော ခဏ၌ အတူ ပေါ်ပေါက်ခြင်း နှစ်ခုလုံးကိုလည်း ပြုရမည်)
- (paṭisandhikkhaṇe, tīṇi) = (ပဋိသန္ဓေ နေသော ခဏ၌၊ သုံးခု)
- (anulomamātikā vitthāretabbā) = (အဟုတ်ပြ ပုံစံ၏ ခေါင်းစဉ်စာရင်းကို အကျယ် ချဲ့ရမည်)
- (Yathā savitakkadukaṃ, evaṃ kātabbaṃ, ninnānākaraṇaṃ. Idha magge cattāri kātabbāni. Savicāraduke imaṃ nānākaraṇaṃ.) = (စတင်ကြံစည်မှု ရှိခြင်း နှစ်မျိုးတွဲကဲ့သို့ ထိုနည်းတူ ပြုရမည်၊ ကွဲပြားချက် မရှိ။ ဤနေရာ၌ မဂ်ဟူသော အကြောင်း၌ လေးခုကို ပြုရမည်။ ဆက်လက်သုံးသပ်မှု ရှိခြင်း နှစ်မျိုးတွဲ၌ ဤသည် ကွဲပြားချက် ဖြစ်သည်။)
- (Yathā savitakkadukaṃ sabbattha, evaṃ sappītikadukaṃ kātabbaṃ, sabbattha pavattipaṭisandhi navapi pañhā.) = (စတင်ကြံစည်မှု ရှိခြင်း နှစ်မျိုးတွဲကဲ့သို့ နေရာတိုင်း၌၊ ထိုနည်းတူ ပီတိ ရှိခြင်း နှစ်မျိုးတွဲကို ပြုရမည်၊ နေရာတိုင်း၌ ဘဝ ဖြစ်စဉ်၌လည်း၊ ပဋိသန္ဓေ၌လည်း ပြဿနာ ကိုးခုလုံး။)
- (yāva asaññasattāpi) = (အသညသတ်တို့အထိလည်း)
- (Saṃkhittaṃ. Yathā savitakkaduke anulomapaccayavāraṃ, evaṃ pavattipaṭisandhi nava pañhā paripuṇṇā pīti ninnānākaraṇā.) = (အကျဉ်းချုပ်။ စတင်ကြံစည်မှု ရှိခြင်း နှစ်မျိုးတွဲ၌ အဟုတ်ပြ ပုံစံ၏ အကြောင်းပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်ကဲ့သို့ ထိုနည်းတူ ဘဝ ဖြစ်စဉ်၌လည်း၊ ပဋိသန္ဓေ၌လည်း ပြဿနာ ကိုးခု ပြည့်စုံကြသည်၊ ပီတိ၊ ကွဲပြားချက် မရှိ။)
- (Pavattipaṭisandhi kātabbā paṭiccavārasadisā, yāva asaññasattā.) = (ဘဝ ဖြစ်စဉ်၌လည်း၊ ပဋိသန္ဓေ၌လည်း ပြုရမည်၊ မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူကြသည်၊ အသညသတ်တို့အထိ။)
- (Anulomasadisā nava pañhā, pavattiyeva paṭisandhi natthi, ekoyeva moho.) = (အဟုတ်ပြ ပုံစံနှင့် တူသော ပြဿနာ ကိုးခု၊ ဘဝ ဖြစ်စဉ်သာ၊ ပဋိသန္ဓေ မရှိ၊ မောဟ တစ်ခုတည်း။)
- (dutiyavārasadisaṃ) = (ဒုတိယ ဖော်ပြချက်နှင့် တူသည်)
- (tīṇipi upanissayā) = (အားကြီးသော အမှီ သုံးခုလုံး)
- (sahajātāpi nānākkhaṇikāpi kātabbā… dve nānākkhaṇikā) = (အတူ ပေါ်ပေါက်သည့် ကံကိုလည်း၊ ခဏ ကွဲပြားသည့် ကံကိုလည်း ပြုရမည်… ခဏ ကွဲပြားသည့် ကံ နှစ်ခု)
- (saṃkhittaṃ. Savitakkadukasadisaṃ kātabbaṃ.) = (အကျဉ်းချုပ်။ စတင်ကြံစည်မှု ရှိခြင်း နှစ်မျိုးတွဲနှင့် တူအောင် ပြုရမည်။)
- (Paccanīyavibhaṅgagaṇanāpi savitakkadukasadisā. Yadipi na sameti imaṃ anulomaṃ paccavekkhitvā gaṇetabbaṃ, itare dve gaṇanā gaṇetabbā.) = (အငြင်းပြ ပုံစံ၏ ခွဲခြမ်းစိတ်ဖြာခြင်းနှင့် ရေတွက်ချက်တို့သည်လည်း စတင်ကြံစည်မှု ရှိခြင်း နှစ်မျိုးတွဲနှင့် တူကြသည်။ အကယ်၍ မညီသော်လည်း ဤ အဟုတ်ပြ ပုံစံကို ပြန်လည် ဆင်ခြင်၍ ရေတွက်ရမည်၊ အခြား ရေတွက်ချက် နှစ်ခုကို ရေတွက်ရမည်။)
- (evaṃ pītisahagatadukaṃ vitthāretabbaṃ, sappītikadukasadisaṃ ninnānākaraṇaṃ, āmasanaṃ ninnānaṃ.) = (ဤသို့ ပီတိနှင့်အတူ ဖြစ်ခြင်း နှစ်မျိုးတွဲကို အကျယ် ချဲ့ရမည်၊ ပီတိ ရှိခြင်း နှစ်မျိုးတွဲနှင့် တူသည်၊ ကွဲပြားချက် မရှိ၊ ရည်ညွှန်းပုံသည် ကွဲပြားမှု မရှိ။)
- (Evaṃ sukhasahagatadukaṃ vitthāretabbaṃ, yathā sappītikadukassa anulomapaṭiccavāro.) = (ဤသို့ သာယာမှုနှင့်အတူ ဖြစ်ခြင်း နှစ်မျိုးတွဲကို အကျယ် ချဲ့ရမည်၊ ပီတိ ရှိခြင်း နှစ်မျိုးတွဲ၏ အဟုတ်ပြ ပုံစံ၏ မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်ကဲ့သို့။)
- (Yathā sappītike nahetupaccayasadisaṃ, ninnānaṃ sabbatthameva nava pañhā.) = (ပီတိ ရှိသော သဘောတရား၌ကဲ့သို့ အမြစ်ဟူသော အကြောင်း မဟုတ်ခြင်းနှင့် တူသည်၊ ကွဲပြားမှု မရှိ၊ နေရာတိုင်း၌ပင် ပြဿနာ ကိုးခု။)
- (Evaṃ itare dve gaṇanāpi sahajātavāropi paṭiccavārasadisā. Paccayavāre pavattipi paṭisandhipi vitthāretabbā, yathā sappītikadukapaccayavārapaccanīyepi pavatte vatthu ca vitthāretabbaṃ, yathā sappītikaduke ekoyeva moho, evaṃ itare dve gaṇanāpi nissayavāropi saṃsaṭṭhavāropi sampayuttavāropi yathā sappītikadukaṃ, evaṃ kātabbaṃ.) = (ဤသို့ အခြား ရေတွက်ချက် နှစ်ခုလည်း၊ အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူကြသည်။ အကြောင်းပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်၌ ဘဝ ဖြစ်စဉ်ကိုလည်း၊ ပဋိသန္ဓေကိုလည်း အကျယ် ချဲ့ရမည်၊ ပီတိ ရှိခြင်း နှစ်မျိုးတွဲ၏ အကြောင်းပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်၏ အငြင်းပြ ပုံစံ၌လည်းကဲ့သို့ ဘဝ ဖြစ်စဉ်၌ မှီရာ ဝတ္ထုကိုလည်းကောင်း အကျယ် ချဲ့ရမည်၊ ပီတိ ရှိခြင်း နှစ်မျိုးတွဲ၌ မောဟ တစ်ခုတည်း ဖြစ်သကဲ့သို့၊ ဤသို့ အခြား ရေတွက်ချက် နှစ်ခုကိုလည်း၊ အမှီပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်ကိုလည်း၊ ရောနှောခြင်းအလိုက် ဖော်ပြချက်ကိုလည်း၊ ယှဉ်တွဲခြင်းအလိုက် ဖော်ပြချက်ကိုလည်း ပီတိ ရှိခြင်း နှစ်မျိုးတွဲကဲ့သို့ ထိုနည်းတူ ပြုရမည်။)
- (Ārammaṇepi adhipatiyāpi sappītikadukasadisā, sukhanti nānākaraṇaṃ.) = (အာရုံဟူသော အကြောင်း၌လည်း၊ အကြီးအမှူးဟူသော အကြောင်း၌လည်း ပီတိ ရှိခြင်း နှစ်မျိုးတွဲနှင့် တူကြသည်၊ သာယာမှုဟူ၍ ကွဲပြားချက် ဖြစ်သည်။)
- (Mūlaṃ. Tīṇipi sappītikadukasadisā.) = (အခြေခံ။ သုံးခုလုံး ပီတိ ရှိခြင်း နှစ်မျိုးတွဲနှင့် တူကြသည်။)
- (dutiyagamanasadisaṃ) = (ဒုတိယ သွားပုံနှင့် တူသည်)
- (Cha kammāni cattāri sahajātāpi nānākkhaṇikāpi kātabbā, dve nānākkhaṇikā.) = (ကံ ခြောက်ခု၊ လေးခု၌ အတူ ပေါ်ပေါက်သည့် ကံကိုလည်း၊ ခဏ ကွဲပြားသည့် ကံကိုလည်း ပြုရမည်၊ နှစ်ခုသည် ခဏ ကွဲပြားသည့် ကံ။)
- (Evaṃ paccanīyavibhaṅgopi gaṇanāpi sappītikadukasadisaṃ kātabbaṃ, yadipi vimati atthi anulomaṃ passitvā gaṇetabbaṃ.) = (ဤသို့ အငြင်းပြ ပုံစံ၏ ခွဲခြမ်းစိတ်ဖြာခြင်းကိုလည်း၊ ရေတွက်ချက်တို့ကိုလည်း ပီတိ ရှိခြင်း နှစ်မျိုးတွဲနှင့် တူအောင် ပြုရမည်၊ အကယ်၍ စိတ်ရှုပ်ထွေးခြင်း ရှိသော်လည်း အဟုတ်ပြ ပုံစံကို ကြည့်၍ ရေတွက်ရမည်။)
- (Sappītikadukasadisaṃ, anulome navapi pañhā.) = (ပီတိ ရှိခြင်း နှစ်မျိုးတွဲနှင့် တူသည်၊ အဟုတ်ပြ ပုံစံ၌ ပြဿနာ ကိုးခုလုံး။)
- (yathā savitakkadukasadisaṃ paccayavāre nānākaraṇaṃ. "Upekkha"nti navapi pañhā kātabbā, paṭisandhipavattipi vatthupi.) = (စတင်ကြံစည်မှု ရှိခြင်း နှစ်မျိုးတွဲနှင့် တူသည့်အတိုင်း အကြောင်းပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်၌ ကွဲပြားချက်။ “ဥပေက္ခာ”ဟု ပြဿနာ ကိုးခုလုံးကို ပြုရမည်၊ ပဋိသန္ဓေ၌လည်း၊ ဘဝ ဖြစ်စဉ်၌လည်း၊ မှီရာ ဝတ္ထုလည်း။)
- (Evaṃ navapi pañhā pavattipaṭisandhiyo yathā savitakkadukassa evaṃ kātabbā. Tīṇiyeva moho, pavatte vatthupi kātabbā.) = (ဤသို့ ပြဿနာ ကိုးခုလုံးကို ဘဝ ဖြစ်စဉ်၌လည်း၊ ပဋိသန္ဓေ၌လည်း စတင်ကြံစည်မှု ရှိခြင်း နှစ်မျိုးတွဲ၌ကဲ့သို့ ထိုနည်းတူ ပြုရမည်။ မောဟ သုံးခုသာ၊ ဘဝ ဖြစ်စဉ်၌ မှီရာ ဝတ္ထုကိုလည်း ပြုရမည်။)
- (Yathā savitakkadukaṃ sampayuttavāro evaṃ kātabbo.) = (စတင်ကြံစည်မှု ရှိခြင်း နှစ်မျိုးတွဲ၏ ယှဉ်တွဲခြင်းအလိုက် ဖော်ပြချက်ကဲ့သို့ ထိုနည်းတူ ပြုရမည်။)
- (Evaṃ pañca pañhā yathā savitakkaduke evaṃ kātabbā.) = (ဤသို့ ပြဿနာ ငါးခုကို စတင်ကြံစည်မှု ရှိခြင်း နှစ်မျိုးတွဲ၌ကဲ့သို့ ထိုနည်းတူ ပြုရမည်။)
- (Evaṃ cattāri pañhā yathā savitakkadukassa.) = (ဤသို့ ပြဿနာ လေးခု၊ စတင်ကြံစည်မှု ရှိခြင်း နှစ်မျိုးတွဲ၌ကဲ့သို့။)
- (Yathā sappītikadukaṃ evaṃ ārammaṇampi adhipatipi vitthāretabbā, "upekkhā"ti nānaṃ.) = (ပီတိ ရှိခြင်း နှစ်မျိုးတွဲကဲ့သို့ ထိုနည်းတူ အာရုံကိုလည်း၊ အကြီးအမှူးကိုလည်း အကျယ် ချဲ့ရမည်၊ “ဥပေက္ခာ”ဟူ၍ ကွဲပြားချက် ဖြစ်သည်။)
- (tīṇi upanissayā dutiyagamanasadisā) = (အားကြီးသော အမှီ သုံးခုသည် ဒုတိယ သွားပုံနှင့် တူကြသည်)
- (sappītikadukasadisā) = (ပီတိ ရှိခြင်း နှစ်မျိုးတွဲနှင့် တူကြသည်)
- (Cattāri sahajātā nānākkhaṇikā kātabbā, dve nānākkhaṇikā ca.) = (လေးခု၌ အတူ ပေါ်ပေါက်သည့် ကံ၊ ခဏ ကွဲပြားသည့် ကံကို ပြုရမည်၊ နှစ်ခု၌ ခဏ ကွဲပြားသည့် ကံကိုလည်း။)
- (Imāni paccayāni sappītikakaraṇena vibhajitabbāni.) = (ဤ အကြောင်းတို့ကို ပီတိ ရှိသော သဘောတရား၏ ပြုပုံအတိုင်း ခွဲခြမ်းစိတ်ဖြာရမည်။)
- (Evaṃ paccanīyavibhaṅgopi itare tīṇi gaṇanāpi sappītikadukasadisā kātabbā.) = (ဤသို့ အငြင်းပြ ပုံစံ၏ ခွဲခြမ်းစိတ်ဖြာခြင်းကိုလည်း၊ အခြား ရေတွက်ချက် သုံးခုကိုလည်း ပီတိ ရှိခြင်း နှစ်မျိုးတွဲနှင့် တူအောင် ပြုရမည်။)
- (itare dve pākatikā) = (အခြား နှစ်ခုသည် ပကတိအတိုင်း)
- (Avasesā tīṇi pākatikā. Saṃkhittaṃ.) = (ကြွင်းသော သုံးခုသည် ပကတိအတိုင်း။ အကျဉ်းချုပ်။)
- (Avasesā gaṇanāpi sahajātavāropi kātabbo.) = (ကြွင်းသော ရေတွက်ချက်တို့ကိုလည်း၊ အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်ကိုလည်း ပြုရမည်။)
- (paṭiccasadisā. Mūlaṃ kātabbaṃ.) = (မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူကြသည်။ အခြေခံကို ပြုရမည်။)
- (suddhake arūpamissake ca "vipāka"nti niyāmetabbaṃ, rūpamissake natthi. Saṃkhittaṃ) = (ရိုးရိုး အပိုင်း၌လည်းကောင်း၊ ရုပ် မဟုတ်သော သဘောတရားနှင့် ရောနှောသော အပိုင်း၌လည်းကောင်း “ကံ၏ အကျိုး”ဟု သတ်မှတ်ရမည်၊ ရုပ်နှင့် ရောနှောသော အပိုင်း၌ မရှိ။ အကျဉ်းချုပ်)
- (Nakāmāvacaraṃ paṭiccavārasadisaṃ ninnānaṃ, idha sabbe mahābhūtā kātabbā.) = (ကာမဘုံနှင့် ဆိုင်သည် မဟုတ်သော သဘောတရားသည် မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူသည်၊ ကွဲပြားမှု မရှိ၊ ဤနေရာ၌ မူလဓာတ်ကြီး အားလုံးကို ပြုရမည်။)
- (yāva asaññasattā, itare pañcapi pañhā, anulomaṃ kātabbaṃ) = (အသညသတ်တို့အထိ၊ အခြား ပြဿနာ ငါးခုလုံး၊ အဟုတ်ပြ ပုံစံကို ပြုရမည်)
- (saṃkhittaṃ. Mūlaṃ. Itarepi pañhā kātabbā) = (အကျဉ်းချုပ်။ အခြေခံ။ အခြား ပြဿနာတို့ကိုလည်း ပြုရမည်)
- (yāva ajjhattikaṃ mahābhūtaṃ) = (အတွင်းပိုင်း ဖြစ်သော မူလဓာတ်ကြီးအထိ)
- (suddhike arūpe ca missake ca "vipāka"nti niyāmetabbaṃ) = (ရိုးရိုး အပိုင်း၌ ရုပ်မရှိသော ဘုံ၌လည်းကောင်း၊ ရောနှောသော အပိုင်း၌လည်းကောင်း “ကံ၏ အကျိုး”ဟု သတ်မှတ်ရမည်)
- (anulomaṃ) = (အဟုတ်ပြ ပုံစံ)
- (paccanīyaṃ) = (အငြင်းပြ ပုံစံ)
- (Yathā cūḷantaraduke lokiyadukaṃ. Evaṃ imampi dukaṃ kātabbaṃ, ninnānākaraṇaṃ.) = (ကြားညှပ် နှစ်မျိုးတွဲ အစုငယ်၌ လောကနှင့် သက်ဆိုင်ခြင်း နှစ်မျိုးတွဲကဲ့သို့။ ဤသို့ ဤ နှစ်မျိုးတွဲကိုလည်း ပြုရမည်၊ ကွဲပြားချက် မရှိ။)
- (yāva asaññasattā kātabbā) = (အသညသတ်တို့အထိ ပြုရမည်)
- (arūpadukasadisā kātabbā) = (ရုပ်မရှိသော ဘုံ နှစ်မျိုးတွဲနှင့် တူအောင် ပြုရမည်)
- (arūpadukasadisā kātabbā, āmasanā nānāpadāyeva) = (ရုပ်မရှိသော ဘုံ နှစ်မျိုးတွဲနှင့် တူအောင် ပြုရမည်၊ ရည်ညွှန်းပုံတို့သည် ကွဲပြားသော ပုဒ်များပင်)
- (saṃkhittaṃ. Pañcapi pañhā kātabbā. Yathā niyyānikadukaṃ evaṃ paṭiccavāropi sahajātavāropi paccayavāropi nissayavāropi saṃsaṭṭhavāropi sampayuttavāropi kātabbā, ninnānākaraṇaṃ āmasanaṃ nānaṃ) = (အကျဉ်းချုပ်။ ပြဿနာ ငါးခုလုံးကို ပြုရမည်။ လွတ်မြောက်ရာသို့ ပို့ဆောင်ခြင်း နှစ်မျိုးတွဲကဲ့သို့ ထိုနည်းတူ မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်ကိုလည်း၊ အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်ကိုလည်း၊ အကြောင်းပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်ကိုလည်း၊ အမှီပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်ကိုလည်း၊ ရောနှောခြင်းအလိုက် ဖော်ပြချက်ကိုလည်း၊ ယှဉ်တွဲခြင်းအလိုက် ဖော်ပြချက်ကိုလည်း ပြုရမည်၊ ကွဲပြားချက် မရှိ၊ ရည်ညွှန်းပုံသည် ကွဲပြားချက် ဖြစ်သည်)
- (niyyānikadukasadisā ninnānākaraṇā) = (လွတ်မြောက်ရာသို့ ပို့ဆောင်ခြင်း နှစ်မျိုးတွဲနှင့် တူကြသည်၊ ကွဲပြားချက် မရှိ)
- (arūpadukasadisaṃ) = (ရုပ်မရှိသော ဘုံ နှစ်မျိုးတွဲနှင့် တူသည်)
- (arūpāvacaradukasadisaṃ) = (ရုပ်မရှိသော ဘုံနှင့် ဆိုင်ခြင်း နှစ်မျိုးတွဲနှင့် တူသည်)
- (Yāva ajjhattikā mahābhūtā. Yathā cūḷantaraduke lokiyadukasadisaṃ ninnānākaraṇaṃ.) = (အတွင်းပိုင်း ဖြစ်သော မူလဓာတ်ကြီးတို့အထိ။ ကြားညှပ် နှစ်မျိုးတွဲ အစုငယ်၌ လောကနှင့် သက်ဆိုင်ခြင်း နှစ်မျိုးတွဲနှင့် တူသည့်အတိုင်း၊ ကွဲပြားချက် မရှိ။)
- (Pañca pañhā arūpāvacaradukasadisā, anulomapaṭiccasadisā.) = (ပြဿနာ ငါးခုသည် ရုပ်မရှိသော ဘုံနှင့် ဆိုင်ခြင်း နှစ်မျိုးတွဲနှင့် တူကြသည်၊ အဟုတ်ပြ ပုံစံ၏ မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူကြသည်။)
- (yathā arūpāvacaradukassa paccayavāropi evaṃ kātabbo) = (ရုပ်မရှိသော ဘုံနှင့် ဆိုင်ခြင်း နှစ်မျိုးတွဲ၌ကဲ့သို့ အကြောင်းပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်ကိုလည်း ထိုနည်းတူ ပြုရမည်)
- (Evaṃ itare dve gaṇanāpi nissayavāropi kātabbo, saṃsaṭṭhavārepi dve pañhā kātabbā sabbattha.) = (ဤသို့ အခြား ရေတွက်ချက် နှစ်ခုကိုလည်း၊ အမှီပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်ကိုလည်း ပြုရမည်၊ ရောနှောခြင်းအလိုက် ဖော်ပြချက်၌လည်း နေရာတိုင်း၌ ပြဿနာ နှစ်ခုကို ပြုရမည်။)
- (arūpadukasadisaṃ, cattāri) = (ရုပ်မရှိသော ဘုံ နှစ်မျိုးတွဲနှင့် တူသည်၊ လေးခု)
- (arūpadukasadisā) = (ရုပ်မရှိသော ဘုံ နှစ်မျိုးတွဲနှင့် တူကြသည်)
- (anulomamātikā gahetabbā) = (အဟုတ်ပြ ပုံစံ၏ ခေါင်းစဉ်စာရင်းကို ယူရမည်)
