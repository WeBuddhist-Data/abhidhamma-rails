# pi-7 (Paṭṭhāna) Burmese zero-shot: 2-07 parittattika, 2-08 parittārammaṇattika, 2-09 hīnattika, 2-10 micchattaniyatattika, 2-11 maggārammaṇattika — notes

Files: `AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters/` 2-07-parittattika.md,
2-08-parittarammanattika.md, 2-09-hinattika.md, 2-10-micchattaniyatattika.md, 2-11-maggarammanattika.md.
Translated from the Pāli only (no Burmese translation or nissaya opened, no web search, `language-priority/` not
opened). Meaning cross-checked only against the English pi-7 zero-shot (2-07 notes, 2-10 «yaṃ vatthuṃ
parāmasantassa»); the Marathi 2-07 … 2-11 notes used for the frame inventory / slip list only (no Marathi words).
Generator: `make_ch2-07-11.py` (imports `my7_formulas.py`, `make_sample.py` for its tables, and `make_ch2-01-02.py`,
which itself loads `make_ch1-03-05.py`; their main blocks never run, none of their files is edited or written).
Check: `check_ch2-07-11.py` (adapted from check_ch2-01-02.py). `make_ch2-07-11.py --dev --new` lists every string the
generator adds (the list at the end).

## Status (all pass, 2026-11-23)
| file | segments | lines | check_chapter_ids | check_text (own scratch chk-pe/ch2-07-11/, deleted) | check_marks | check_ch2-07-11 |
|---|---|---|---|---|---|---|
| 2-07-parittattika.md | 187 | 385 | OK | OK | OK | OK |
| 2-08-parittarammanattika.md | 85 | 143 | OK | OK | OK | OK |
| 2-09-hinattika.md | 10 | 14 | OK | OK | OK | OK |
| 2-10-micchattaniyatattika.md | 151 | 255 | OK | OK | OK | OK |
| 2-11-maggarammanattika.md | 104 | 213 | OK | OK | OK | OK |

check_ch2-07-11 (`--sample --pe --mutate`): 1010 lines × (structure, polarity, conditions, term order, numbers), 1941
sentences for identity (with the sample, 1-03 … 1-05 and 2-01 … 2-02 on disk), 92 table values: **0 mismatches**.
Reuse test: **78 / 78** pi-1 … pi-6 values identical wherever their Pāli occurs; sentences also in pi-1 … pi-6:
**530 / 530**. Regression: the sample (1-00, 1-02; raw and prep) and the groups 1-03 … 1-05 and 2-01 … 2-02 (each
with its own prep) regenerated in memory with all of this script's extensions = their files on disk. Mutation test
**9 / 9** caught (count, polarity, term order, condition, khandha count, term, digits, note, negative term).
No existing value of my7_formulas / make_sample / make_ch1-03-05 / make_ch2-01-02 was changed (`--new`: 0 CHANGED).
Info (not a failure): 65 sentences also occur in 1-01; 1 is rendered differently there (see «For the coordinator» 2).

## Triad terms (pi-1 final Mātikā ^1-M1-12 … ^1-M1-16, read by W())
- paritta = အကန့်အသတ် ရှိသော; mahaggata = ကြီးမြတ်သော; appamāṇa = အတိုင်းအဆ မရှိသော
- parittārammaṇa = အကန့်အသတ် ရှိသည်ကို အာရုံပြုသော; mahaggatārammaṇa = ကြီးမြတ်သည်ကို အာရုံပြုသော;
  appamāṇārammaṇa = အတိုင်းအဆ မရှိသည်ကို အာရုံပြုသော
- hīna = ယုတ်ညံ့သော; majjhima = အလယ်အလတ်; paṇīta = မွန်မြတ်သော
- micchattaniyata = မှားယွင်းမှု၌ ကျိန်းသေသော; sammattaniyata = မှန်ကန်မှု၌ ကျိန်းသေသော; aniyata = မကျိန်းသေသော
- maggārammaṇa = မဂ်ကို အာရုံပြုသော; maggahetuka = မဂ်ကို အမြစ်ပြုသော; maggādhipati = မဂ်ကို အကြီးအမှူးပြုသော
  (an i-stem: prep() reads its endings as the a-stem endings the frames know, -ī/-iṃ/-issa/-iñca/-īnaṃ … → -ā/-aṃ/-assa/
  -añca/-ānaṃ …; the Burmese of a term does not depend on its ending)
- triad names (NEW, the 1-03 … 1-05 pattern «<abstract noun> သုံးမျိုးတွဲ»): Parittattikaṃ = အကန့်အသတ် ရှိခြင်း သုံးမျိုးတွဲ;
  Parittārammaṇattikaṃ = အကန့်အသတ် ရှိသည်ကို အာရုံပြုခြင်း သုံးမျိုးတွဲ; Hīnattikaṃ = ယုတ်ညံ့ခြင်း သုံးမျိုးတွဲ;
  Micchattaniyatattikaṃ = မှားယွင်းမှု၌ ကျိန်းသေခြင်း သုံးမျိုးတွဲ; Maggārammaṇattikaṃ = မဂ်ကို အာရုံပြုခြင်း သုံးမျိုးတွဲ
- two terms in one compound before «-cittasamaṅgissa» («parittārammaṇaparittacittasamaṅgissa»,
  «maggahetukamaggādhipaticittasamaṅgissa»): both stacked on the mind with a space, as the module stacks two terms on
  one noun without «ca» («Appamāṇārammaṇe paritte khandhe»): «A B စိတ်နှင့် ပြည့်စုံသူ၏».
- two terms on one noun WITH «ca … ca» («maggārammaṇā ca maggādhipatī ca tayo khandhā», «maggārammaṇañca
  maggādhipatiñca ekaṃ khandhaṃ», «… -ānañca … -īnañca khandhānaṃ», «… ādhipati»): one slot, two stacked qualifiers
  «A၊ B N», as 2-01 … 2-02 «pītisahagatā ca sukhasahagatā ca tayo khandhā». With the noun dhamma (or no noun before a
  condition) the module's coordination stays («A သဘောတရားနှင့် B သဘောတရား»).

## Engine extensions (in memory, make_ch2-07-11.py)
- prep(): 2-01 … 2-02 prep (which runs 1-03 … 1-05 prep), the slips, the maggādhipati endings, «X-assa ca Y-assa ca
  Zpaccayena» with the noun left out = «… dhammassa» supplied (logged; as 1-03 … 1-05 for its terms), the «ca … ca»
  join above, «X-ādhipati» = «X-o adhipati», placeholders for notes holding condition / term words (NOTEP).
- counting lines with bare locatives sharing a count: 2-01 … 2-02's count_line() with a wider trigger (it did not see
  locatives with «ñ»: «nasamanantare naaññamaññe naupanissaye pañca»); same rendering.
- comma lists in a fragment (1-03 … 1-05 pairs2): split outside brackets; a part that is a bare condition chain with its
  notes is rendered by the chain («…, vatthuṃ paccayā X khandhā (note), adhipatipaccayā (note), anantarapaccayā…»).
- «Anulomaṃ.» closing the positive order = «အဟုတ်ပြ ပုံစံ။» (as 1-01), registered only while these chapters are
  translated (see «For the coordinator» 1).
- 2-01 … 2-02's unit frame for a missing full stop before «paṭisandhikkhaṇe…pe….» also fires on the regular
  «… dve khandhe…pe… paṭisandhikkhaṇe…pe….»: same Burmese, its (misleading) slip message is dropped.

## Unsure Pāli
- «yaṃ vatthuṃ parāmasantassa micchattaniyatā khandhā uppajjanti, taṃ vatthu …» (2-10): vatthu read as the physical
  base «မှီရာ ဝတ္ထု» (pi-5 value, and the English cross-check); parāmasantassa «မှားယွင်းစွာ ယူဆသူ၏» (pi-1 parāmāsa
  «မှားယွင်းသော ယူဆမှု»). The Marathi reads vatthu as the thing grasped; worth a look.
- «(tīṇi pañhā, micchattasadisaṃ)»: micchatta «မှားယွင်းမှု အပိုင်း» (the micchattaniyata part).
- «(cakkaṃ kātabbaṃ)» «(စက်ဝိုင်းကဲ့သို့ လှည့်ပတ်၍ ပြုရမည်)» (the "wheel": every item with every item in turn).
- «(paripuṇṇaṃ, vipākoti niddisitabbaṃ cittasamuṭṭhānaṃ rūpaṃ vipākoti na kātabbaṃ)»: niddisitabbaṃ «ညွှန်ပြရမည်»,
  na kātabbaṃ «မပြုရ»; «(paṭisandhivipākopi natthi)» «(ပဋိသန္ဓေ၌ ကံ၏ အကျိုးလည်း မရှိ)».
- «(naārammaṇe gahite pakatārammaṇampi upanissayārammaṇampi dvepi chijjanti)»: pakatārammaṇa «ပကတိ အာရုံ»,
  upanissayārammaṇa «အားကြီးသော အမှီ အာရုံ», chijjanti «ပြတ်ကြသည်».
- «(avasesā cha pañhā hetupaccayasadisā satta kātabbā)» = «(ကြွင်းသော ပြဿနာ ခြောက်ခုကို အမြစ်ဟူသော အကြောင်းနှင့် တူအောင်
  ခုနစ်ခု ပြုရမည်)».
- «X-parikammaṃ tasseva … āsevanapaccayena paccayo»: tasseva «ထိုအရာကိုယ်တိုင်အား».
- «{nevasaññānāsaññāyatanassa (?) aññesu tikesu oloketabbaṃ}» (editorial note): the sample's «(?)» variant form, then
  «အခြား သုံးမျိုးတွဲတို့၌ ကြည့်ရှုရမည်».

## Source slips (translated as written; normalised in memory only where a frame needs it; logged by the generator)
- 2-07: «avigate eka» for «ekaṃ»; «(evaṃ gaṇatabbaṃ)» for «gaṇetabbaṃ»; «vippassati» for «vipassati»;
  «53asaññasattānaṃ» (a number glued to the word, kept: «53အသညသတ်တို့၌»); «rūpaṃ.(2)», «…pe….(1)» and
  «āsevanapaccayā(vipākopi …» without a space (a space is put before the bracket); «(paṭiccavārasadisaṃ. Pañca).» a
  full stop inside the bracket (kept: two units).
- 2-08: «sampayuttapaccayena paccaya…», «vigatapaccayena paccaya…» read as «paccayo…».
- 2-10: «Micchattaniyato dhammo micchattaniyatassa ca aniyatassa ca atthipaccayena paccayo» without «dhammassa» (the
  noun supplied); «(sabbe paccayā iminā kāraṇena vitthāretabbā. Saṃkhittaṃ).» a full stop inside the bracket (kept).
- 2-11: «maggāhetukānañca» read as «maggahetukānañca»; «Maggādhipati dhammo maggārammaṇassa ca maggādhipatissa ca
  adhipatipaccayena paccayo» without «dhammassa» (supplied); «(anantarasadisaṃ. Nava pañhā kātabbā, āvajjanā na
  kātabbā).» a full stop inside the bracket (kept: two units).

## For the coordinator
1. «Anulomaṃ.» (the line closing the positive order) is «အဟုတ်ပြ ပုံစံ။» in 1-01 and here, but «လျော်ညီခြင်း စိတ်။» (the
   LEX noun anulomaṃ, the conformity mind) in 1-03 … 1-05 and 2-01 … 2-02 (12 lines: 1-03 ^7-4-74, ^7-4-84; 1-04
   ^7-U279, ^7-U281, ^7-5-48, ^7-U284; 1-05 ^7-6-32; 2-01 ^7-U290, ^7-7-62, ^7-7-138; 2-02 ^7-8-5, ^7-8-45). I followed
   1-01 (the meaning); the groups' lines look like a mistranslation for the consistency pass. check_ch2-07-11 lists
   it as a known split.
2. «… saṅghaṃ bhinditvā tassa paṭighātatthāya dānaṃ deti …» (2-10): «ထိုအမှုကို ချေဖျက်ရန်» (1-03 … 1-05, the chain
   used here) vs 1-01 «ထိုအမှုကို ပယ်ဖျက်ရန်အတွက်». The heinous deeds follow 1-03 … 1-05 / pi-5 («အမိကို သတ်ခြင်း ကံ»,
   «အဖကို သတ်ခြင်း ကံ», «ရဟန္တာကို သတ်ခြင်း ကံ», «ဘုရား၏ ကိုယ်တော်မှ သွေးကို ထွက်စေခြင်း ကံ», «သံဃာကို သင်းခွဲခြင်း ကံ»), where
   1-01 has «… သတ်သော ကံ»; the gerunds «mātaraṃ jīvitā voropetvā» … are the 1-01 values.
3. Two-term stacking: «A B N» without «ca» (module), «A၊ B N» with «ca … ca» (as 2-01 … 2-02). Worth a look with the
   2-01 … 2-02 point 1 in the consistency pass.
4. Sahajātā label: bare «အတူ ပေါ်ပေါက်ခြင်း –» outside the kamma section, «အတူ ပေါ်ပေါက်သည့် ကံ» in it (1-03 … 1-05 prep).

## New strings of this script («Pāli = Burmese», table in brackets; SK = whole-unit templates by their skeleton,
## «(frame)» = built from slots; [NEW] = the words of the frames, also inside the table entries)
- vatthussa = မှီရာ ဝတ္ထု  [LEX]
- tasseva = ထိုအရာကိုယ်တိုင်  [LEX]
- dibbaṃ cakkhuṃ = နတ်မျက်စိ  [LEX]
- dibbaṃ sotadhātuṃ = နတ်နား ဓာတ်  [LEX]
- iddhividhañāṇaṃ = တန်ခိုး အမျိုးမျိုးကို ပြနိုင်သော ဉာဏ်  [LEX]
- cetopariyañāṇaṃ = စိတ်ကို ပိုင်းခြား၍ သိသော ဉာဏ်  [LEX]
- pubbenivāsānussatiñāṇaṃ = ရှေးဘဝများကို အဖန်ဖန် အောက်မေ့နိုင်သော ဉာဏ်  [LEX]
- yathākammūpagañāṇaṃ = ကံအားလျော်စွာ ဖြစ်ပေါ်ပုံကို သိသော ဉာဏ်  [LEX]
- anāgataṃsañāṇaṃ = အနာဂတ်ကို သိသော ဉာဏ်  [LEX]
- maggapaccavekkhaṇaṃ = မဂ်ကို ပြန်လည် ဆင်ခြင်ခြင်း  [LEX]
- phalapaccavekkhaṇaṃ = ဖိုလ်ကို ပြန်လည် ဆင်ခြင်ခြင်း  [LEX]
- nibbānapaccavekkhaṇaṃ = နိဗ္ဗာန်ကို ပြန်လည် ဆင်ခြင်ခြင်း  [LEX]
- dibbacakkhupaccavekkhaṇaṃ = နတ်မျက်စိကို ပြန်လည် ဆင်ခြင်ခြင်း  [LEX]
- dibbasotadhātupaccavekkhaṇaṃ = နတ်နား ဓာတ်ကို ပြန်လည် ဆင်ခြင်ခြင်း  [LEX]
- ākāsānañcāyatanapaccavekkhaṇaṃ = အဆုံး မရှိသော ဟင်းလင်းပြင် နယ်ပယ်ကို ပြန်လည် ဆင်ခြင်ခြင်း  [LEX]
- viññāṇañcāyatanapaccavekkhaṇaṃ = အဆုံး မရှိသော သိစိတ် နယ်ပယ်ကို ပြန်လည် ဆင်ခြင်ခြင်း  [LEX]
- ākiñcaññāyatanapaccavekkhaṇaṃ = ဘာမျှ မရှိသော နယ်ပယ်ကို ပြန်လည် ဆင်ခြင်ခြင်း  [LEX]
- nevasaññānāsaññāyatanapaccavekkhaṇaṃ = မှတ်သိမှု ရှိသည်လည်း မဟုတ်၊ မှတ်သိမှု မရှိသည်လည်း မဟုတ်သော နယ်ပယ်ကို ပြန်လည် ဆင်ခြင်ခြင်း  [LEX]
- paṭhamajjhānapaccavekkhaṇaṃ = ပထမ ဈာန်ကို ပြန်လည် ဆင်ခြင်ခြင်း  [LEX]
- dutiyajjhānapaccavekkhaṇaṃ = ဒုတိယ ဈာန်ကို ပြန်လည် ဆင်ခြင်ခြင်း  [LEX]
- tatiyajjhānapaccavekkhaṇaṃ = တတိယ ဈာန်ကို ပြန်လည် ဆင်ခြင်ခြင်း  [LEX]
- catutthajjhānapaccavekkhaṇaṃ = စတုတ္ထ ဈာန်ကို ပြန်လည် ဆင်ခြင်ခြင်း  [LEX]
- iddhividhañāṇapaccavekkhaṇaṃ = တန်ခိုး အမျိုးမျိုးကို ပြနိုင်သော ဉာဏ်ကို ပြန်လည် ဆင်ခြင်ခြင်း  [LEX]
- cetopariyañāṇapaccavekkhaṇaṃ = စိတ်ကို ပိုင်းခြား၍ သိသော ဉာဏ်ကို ပြန်လည် ဆင်ခြင်ခြင်း  [LEX]
- pubbenivāsānussatiñāṇapaccavekkhaṇaṃ = ရှေးဘဝများကို အဖန်ဖန် အောက်မေ့နိုင်သော ဉာဏ်ကို ပြန်လည် ဆင်ခြင်ခြင်း  [LEX]
- yathākammūpagañāṇapaccavekkhaṇaṃ = ကံအားလျော်စွာ ဖြစ်ပေါ်ပုံကို သိသော ဉာဏ်ကို ပြန်လည် ဆင်ခြင်ခြင်း  [LEX]
- anāgataṃsañāṇapaccavekkhaṇaṃ = အနာဂတ်ကို သိသော ဉာဏ်ကို ပြန်လည် ဆင်ခြင်ခြင်း  [LEX]
- viññāṇañcāyatanaṃ = အဆုံး မရှိသော သိစိတ် နယ်ပယ်  [LEX]
- pitughātikammaṃ = အဖကို သတ်ခြင်း ကံ  [LEX]
- pitughātikammassa = အဖကို သတ်ခြင်း ကံ  [LEX]
- arahantaghātikammaṃ = ရဟန္တာကို သတ်ခြင်း ကံ  [LEX]
- arahantaghātikammassa = ရဟန္တာကို သတ်ခြင်း ကံ  [LEX]
- ruhiruppādakammaṃ = ဘုရား၏ ကိုယ်တော်မှ သွေးကို ထွက်စေခြင်း ကံ  [LEX]
- ruhiruppādakammassa = ဘုရား၏ ကိုယ်တော်မှ သွေးကို ထွက်စေခြင်း ကံ  [LEX]
- saṅghabhedakammaṃ = သံဃာကို သင်းခွဲခြင်း ကံ  [LEX]
- saṅghabhedakammassa = သံဃာကို သင်းခွဲခြင်း ကံ  [LEX]
- rūpajīvitindriyaṃ = ရုပ် အသက်၏ စွမ်းရည်  [LEX]
- domanassassa = စိတ်ဆင်းရဲမှု  [LEX]
- paccavekkhaṇāya = ပြန်လည် ဆင်ခြင်ခြင်း  [LEX]
- paccavekkhaṇā = ပြန်လည် ဆင်ခြင်ခြင်း  [LEX]
- aniyatamicchādiṭṭhi = မကျိန်းသေသော မှားယွင်းသော အယူ  [LEX]
- mātaraṃ jīvitā voropetvā = အမိကို အသက်မှ သတ်၍  [LEX]
- pitaraṃ jīvitā voropetvā = အဖကို အသက်မှ သတ်၍  [LEX]
- arahantaṃ jīvitā voropetvā = ရဟန္တာကို အသက်မှ သတ်၍  [LEX]
- duṭṭhena cittena tathāgatassa lohitaṃ uppādetvā = ပြစ်မှားသော စိတ်ဖြင့် မြတ်စွာဘုရား၏ သွေးကို ထွက်စေ၍  [LEX]
- uposathaṃ = ဥပုသ်  [LEX]
- uposathakammaṃ = ဥပုသ်  [LEX]
- (evaṃ gaṇetabbaṃ) = (ထိုနည်းတူ ရေတွက်ရမည်)  [NOTES]
- (sabbepi mahābhūtā kātabbā) = (မူလဓာတ်ကြီး အားလုံးကိုလည်း ပြုရမည်)  [NOTES]
- (sabbe mahābhūtā kātabbā) = (မူလဓာတ်ကြီး အားလုံးကို ပြုရမည်)  [NOTES]
- (tisso pañhā kātabbā) = (ပြဿနာ သုံးခု ပြုရမည်)  [NOTES]
- (vitthāretabbaṃ) = (အကျယ် ချဲ့ရမည်)  [NOTES]
- (paṭisandhikkhaṇe tīṇipi kātabbā) = (ပဋိသန္ဓေ နေသော ခဏ၌ သုံးခုလုံးကိုလည်း ပြုရမည်)  [NOTES]
- (paṭisandhi natthi, sattarasa pañhā paripuṇṇā) = (ပဋိသန္ဓေ မရှိ၊ ပြဿနာ ဆယ့်ခုနစ်ခု ပြည့်စုံကြသည်)  [NOTES]
- (paṭiccavārasadisā dvādasa pañhā) = (မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူသော ပြဿနာ ဆယ့်နှစ်ခု)  [NOTES]
- (paripuṇṇaṃ, vipākoti niddisitabbaṃ cittasamuṭṭhānaṃ rūpaṃ vipākoti na kātabbaṃ) = (ပြည့်စုံသည်၊ ကံ၏ အကျိုးဟု ညွှန်ပြရမည် စိတ်မှ ဖြစ်ပေါ်လာသော ရုပ်ကို ကံ၏ အကျိုးဟု မပြုရ)  [NOTES]
- (paṭisandhivipākopi natthi) = (ပဋိသန္ဓေ၌ ကံ၏ အကျိုးလည်း မရှိ)  [NOTES]
- (paṭisandhi natthi) = (ပဋိသန္ဓေ မရှိ)  [NOTES]
- (vipākopi paṭisandhipi natthi) = (ကံ၏ အကျိုးလည်း၊ ပဋိသန္ဓေလည်း မရှိ)  [NOTES]
- (pavattipaṭisandhi kātabbā) = (ဘဝ ဖြစ်ဆဲ ကာလနှင့် ပဋိသန္ဓေကို ပြုရမည်)  [NOTES]
- (tisso pañhā, pavattipaṭisandhi kātabbā) = (ပြဿနာ သုံးခု၊ ဘဝ ဖြစ်ဆဲ ကာလနှင့် ပဋိသန္ဓေကို ပြုရမည်)  [NOTES]
- (pavattimeva) = (ဘဝ ဖြစ်ဆဲ ကာလသာ)  [NOTES]
- (cakkaṃ kātabbaṃ) = (စက်ဝိုင်းကဲ့သို့ လှည့်ပတ်၍ ပြုရမည်)  [NOTES]
- (cakkaṃ kātabbaṃ kusalattikasadisaṃ) = (စက်ဝိုင်းကဲ့သို့ လှည့်ပတ်၍ ကုသိုလ် သုံးမျိုးတွဲနှင့် တူအောင် ပြုရမည်)  [NOTES]
- (paṭiccavārasadisaṃ = (မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူသည်  [NOTES]
- (paṭiccavārasadisā kātabbā) = (မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူအောင် ပြုရမည်)  [NOTES]
- (sabbe paccayā iminā kāraṇena vitthāretabbā = (အကြောင်း အားလုံးကို ဤနည်းလမ်းဖြင့် အကျယ် ချဲ့ရမည်  [NOTES]
- (saṃkhittaṃ, sabbāni paccayāni vitthāretabbāni) = (အကျဉ်းချုပ်၊ အကြောင်း အားလုံးကို အကျယ် ချဲ့ရမည်)  [NOTES]
- (tīṇi pañhā, micchattasadisaṃ) = (ပြဿနာ သုံးခု၊ မှားယွင်းမှု အပိုင်းနှင့် တူသည်)  [NOTES]
- (saṃkhittaṃ, kusalattike paccayavārasadisaṃ vibhajitabbaṃ) = (အကျဉ်းချုပ်၊ ကုသိုလ် သုံးမျိုးတွဲ၌ အကြောင်းပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူအောင် ခွဲခြမ်းစိတ်ဖြာရမည်)  [NOTES]
- (kusalattikasadisaṃ, pañca kātabbā) = (ကုသိုလ် သုံးမျိုးတွဲနှင့် တူသည်၊ ငါးခု ပြုရမည်)  [NOTES]
- (paripuṇṇaṃ) = (ပြည့်စုံသည်)  [NOTES]
- (paṭiccavārasadisaṃ, nava pañhā) = (မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူသည်၊ ပြဿနာ ကိုးခု)  [NOTES]
- (paṭiccavārasadisaṃ, tisso pañhā) = (မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူသည်၊ ပြဿနာ သုံးခု)  [NOTES]
- (kusalattikasadisā, terasa pañhā) = (ကုသိုလ် သုံးမျိုးတွဲနှင့် တူကြသည်၊ ပြဿနာ ဆယ့်သုံးခု)  [NOTES]
- (tisso pañhā) = (ပြဿနာ သုံးခု)  [NOTES]
- (paripuṇṇā dvepi) = (နှစ်ခုလုံးလည်း ပြည့်စုံကြသည်)  [NOTES]
- (pañca pañhā) = (ပြဿနာ ငါးခု)  [NOTES]
- (paṭhamaghaṭane tīṇi) = (ပထမ ပေါင်းစပ်ချက်၌ သုံးခု)  [NOTES]
- (dutiyaghaṭane tīṇi pañhā) = (ဒုတိယ ပေါင်းစပ်ချက်၌ ပြဿနာ သုံးခု)  [NOTES]
- (paripuṇṇaṃ, arūpanti niyāmetabbaṃ) = (ပြည့်စုံသည်၊ ရုပ် မဟုတ်သော သဘောတရားဟု သတ်မှတ်ရမည်)  [NOTES]
- (iminā kāraṇena sattarasa pañhā kātabbā) = (ဤနည်းလမ်းဖြင့် ပြဿနာ ဆယ့်ခုနစ်ခု ပြုရမည်)  [NOTES]
- (tīsupi sattarasa pañhā kātabbā) = (သုံးခုလုံး၌လည်း ပြဿနာ ဆယ့်ခုနစ်ခု ပြုရမည်)  [NOTES]
- (anantarasadisaṃ = (ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းနှင့် တူသည်  [NOTES]
- (nānākkhaṇikā natthi, sattarasa pañhā kātabbā) = (ခဏ ကွဲပြားသည့် ကံ မရှိ၊ ပြဿနာ ဆယ့်ခုနစ်ခု ပြုရမည်)  [NOTES]
- (ime satta paccayā sattarasa pañhā hetusadisā) = (ဤ အကြောင်း ခုနစ်ပါး၌ ပြဿနာ ဆယ့်ခုနစ်ခု အမြစ်နှင့် တူကြသည်)  [NOTES]
- (anantarasadisā) = (ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းနှင့် တူကြသည်)  [NOTES]
- (sattarasa pañhā) = (ပြဿနာ ဆယ့်ခုနစ်ခု)  [NOTES]
- (naārammaṇe gahite pakatārammaṇampi upanissayārammaṇampi dvepi chijjanti) = (အာရုံဟူသော အကြောင်း မဟုတ်ခြင်းကို ယူသောအခါ ပကတိ အာရုံလည်း၊ အားကြီးသော အမှီ အာရုံလည်း နှစ်ခုလုံး ပြတ်ကြသည်)  [NOTES]
- (⁑m0) = (ကြွင်းသော ပြဿနာ ခြောက်ခုကို အမြစ်ဟူသော အကြောင်းနှင့် တူအောင် ခုနစ်ခု ပြုရမည်)  [NOTES]
- (⁑m1) = (မူလဓာတ်ကြီး အားလုံးကို အကျယ် ချဲ့ရမည်၊ ရုပ်မရှိသော ဘုံ၌ အကန့်အသတ် ရှိသော သဘောတရားကို အခြေခံခြင်း၌ ပြဿနာ သုံးခု)  [NOTES]
- (⁑m2) = (ကြီးမြတ်သည်ကို အာရုံပြုသော သဘောတရား၌ ပဋိသန္ဓေ မရှိ)  [NOTES]
- (⁑m3) = (နောက်မှ ဖြစ်ပေါ်ခြင်းဟူသော အကြောင်း မဟုတ်ခြင်းလည်းကောင်း၊ အလေ့အကျင့် ပြုခြင်းဟူသော အကြောင်း မဟုတ်ခြင်းလည်းကောင်း အကြီးအမှူး မဟုတ်ခြင်းနှင့် တူသည်)  [NOTES]
- (⁑m4) = (ပြဿနာ နှစ်ခု မှားယွင်းမှု၌ ကျိန်းသေသော သဘောတရားနှင့် တူကြသည်)  [NOTES]
- Parittattikaṃ niṭṭhitaṃ. = “အကန့်အသတ် ရှိခြင်း သုံးမျိုးတွဲ” ပြီးဆုံးပြီ။  [HLINES]
- Parittārammaṇattikaṃ niṭṭhitaṃ. = “အကန့်အသတ် ရှိသည်ကို အာရုံပြုခြင်း သုံးမျိုးတွဲ” ပြီးဆုံးပြီ။  [HLINES]
- Hīnattikaṃ niṭṭhitaṃ. = “ယုတ်ညံ့ခြင်း သုံးမျိုးတွဲ” ပြီးဆုံးပြီ။  [HLINES]
- Micchattaniyatattikaṃ niṭṭhitaṃ. = “မှားယွင်းမှု၌ ကျိန်းသေခြင်း သုံးမျိုးတွဲ” ပြီးဆုံးပြီ။  [HLINES]
- Maggārammaṇattikaṃ niṭṭhitaṃ. = “မဂ်ကို အာရုံပြုခြင်း သုံးမျိုးတွဲ” ပြီးဆုံးပြီ။  [HLINES]
- pañca). = ငါးခု)။  [SK]
- paccayānulomaṃ. = အကြောင်း အဟုတ်ပြ ပုံစံ။  [SK]
- nava pañhā kātabbā, āvajjanā na kātabbā). = ပြဿနာ ကိုးခု ပြုရမည်၊ စိတ်ညွတ်ခြင်းကို မပြုရ)။  [SK]
- pañhāvāro. = ပြဿနာအလိုက် ဖော်ပြချက်။  [SK]
- (sahajātavāropi paṭiccavārasadiso.) = (အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်သည်လည်း မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူသည်။)  [SK]
- (nissayavāro paccayavārasadiso.) = (အမှီပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်သည် အကြောင်းပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူသည်။)  [SK]
- (sampayuttavāro saṃsaṭṭhavārasadiso). = (ယှဉ်တွဲခြင်းအလိုက် ဖော်ပြချက်သည် ရောနှောခြင်းအလိုက် ဖော်ပြချက်နှင့် တူသည်)။  [SK]
- (§C§aṃ anantarapaccayasadisaṃ.) = ({C1.n}သည် ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းဟူသော အကြောင်းနှင့် တူသည်။)  [SK]
- (hīnattikaṃ saṃkiliṭṭhattikasadisaṃ vitthāretabbaṃ paripuṇṇaṃ.) = (ယုတ်ညံ့ခြင်း သုံးမျိုးတွဲကို ကိလေသာဖြင့် ညစ်နွမ်းခြင်း သုံးမျိုးတွဲနှင့် တူအောင် ပြည့်စုံစွာ အကျယ် ချဲ့ရမည်။)  [SK]
- (sahajātavāropi paccayavāropi nissayavāropi saṃsaṭṭhavāropi sampayuttavāropi paṭiccavārasadiso). = (အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း၊ အကြောင်းပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်လည်း၊ အမှီပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်လည်း၊ ရောနှောခြင်းအလိုက် ဖော်ပြချက်လည်း၊ ယှဉ်တွဲခြင်းအလိုက် ဖော်ပြချက်လည်း မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူသည်)။  [SK]
- (sahajātavāro paṭiccavārasadiso.) = (အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်သည် မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူသည်။)  [SK]
- (sahajātavāropi paccayavāropi nissayavāropi saṃsaṭṭhavāropi sampayuttavāropi paṭiccavārasadiso.) = (အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း၊ အကြောင်းပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်လည်း၊ အမှီပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်လည်း၊ ရောနှောခြင်းအလိုက် ဖော်ပြချက်လည်း၊ ယှဉ်တွဲခြင်းအလိုက် ဖော်ပြချက်လည်း မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူသည်။)  [SK]
- (nissayavāro paccayavārasadiso). = (အမှီပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်သည် အကြောင်းပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူသည်)။  [SK]
- yaṃ vatthuṃ parāmasantassa §T§ā khandhā uppajjanti, taṃ vatthu §T§ānaṃ khandhānaṃ §C§ena paccayo. = အကြင် မှီရာ ဝတ္ထုကို မှားယွင်းစွာ ယူဆသူ၏ {T1} အစုအဝေးတို့သည် ဖြစ်ပေါ်ကြ၏၊ ထို မှီရာ ဝတ္ထုသည် {T2} အစုအဝေးတို့အား {C1.if}။  [SK]
- ahetukaṃ §T§aṃ = အမြစ် မရှိသော {T1}  [SKF]
- dve khandhā ca = အစုအဝေး နှစ်ပါးလည်းကောင်း  [SKF]
- 53asaññasattānaṃ = 53အသညသတ်တို့၌  [SKF]
- Parittattikaṃ = အကန့်အသတ် ရှိခြင်း သုံးမျိုးတွဲ  [TIKA_NAME]
- Parittārammaṇattikaṃ = အကန့်အသတ် ရှိသည်ကို အာရုံပြုခြင်း သုံးမျိုးတွဲ  [TIKA_NAME]
- Hīnattikaṃ = ယုတ်ညံ့ခြင်း သုံးမျိုးတွဲ  [TIKA_NAME]
- Micchattaniyatattikaṃ = မှားယွင်းမှု၌ ကျိန်းသေခြင်း သုံးမျိုးတွဲ  [TIKA_NAME]
- Maggārammaṇattikaṃ = မဂ်ကို အာရုံပြုခြင်း သုံးမျိုးတွဲ  [TIKA_NAME]
- paritta = {'paritt': 'အကန့်အသတ် ရှိသော', 'mahaggat': 'ကြီးမြတ်သော', 'appamāṇ': 'အတိုင်းအဆ မရှိသော'}  [TRIADS]
- parittarammana = {'parittārammaṇ': 'အကန့်အသတ် ရှိသည်ကို အာရုံပြုသော', 'mahaggatārammaṇ': 'ကြီးမြတ်သည်ကို အာရုံပြုသော', 'appamāṇārammaṇ': 'အတိုင်းအဆ မရှိသည်ကို အာရုံပြုသော'}  [TRIADS]
- hina = {'hīn': 'ယုတ်ညံ့သော', 'majjhim': 'အလယ်အလတ်', 'paṇīt': 'မွန်မြတ်သော'}  [TRIADS]
- micchatta = {'micchattaniyat': 'မှားယွင်းမှု၌ ကျိန်းသေသော', 'sammattaniyat': 'မှန်ကန်မှု၌ ကျိန်းသေသော', 'aniyat': 'မကျိန်းသေသော'}  [TRIADS]
- magga = {'maggārammaṇ': 'မဂ်ကို အာရုံပြုသော', 'maggahetuk': 'မဂ်ကို အမြစ်ပြုသော', 'maggādhipat': 'မဂ်ကို အကြီးအမှူးပြုသော'}  [TRIADS]
- combo = {'parittārammaṇaparitt': 'အကန့်အသတ် ရှိသည်ကို အာရုံပြုသော အကန့်အသတ် ရှိသော', 'parittārammaṇamahaggat': 'အကန့်အသတ် ရှိသည်ကို အာရုံပြုသော ကြီးမြတ်သော', 'parittārammaṇaappamāṇ': 'အကန့်အသတ် ရှိသည်ကို အာရုံပြုသော အတိုင်းအဆ မရှိသော', 'mahaggatārammaṇaparitt': 'ကြီးမြတ်သည်ကို အာရုံပြုသော အကန့်အသတ် ရှိသော', 'mahaggatārammaṇamahaggat': 'ကြီးမြတ်သည်ကို အာရုံပြုသော ကြီးမြတ်သော', 'mahaggatārammaṇaappamāṇ': 'ကြီးမြတ်သည်ကို အာရုံပြုသော အတိုင်းအဆ မရှိသော', 'appamāṇārammaṇaparitt': 'အတိုင်းအဆ မရှိသည်ကို အာရုံပြုသော အကန့်အသတ် ရှိသော', 'appamāṇārammaṇamahaggat': 'အတိုင်းအဆ မရှိသည်ကို အာရုံပြုသော ကြီးမြတ်သော', 'appamāṇārammaṇaappamāṇ': 'အတိုင်းအဆ မရှိသည်ကို အာရုံပြုသော အတိုင်းအဆ မရှိသော', 'maggahetukamaggādhipat': 'မဂ်ကို အမြစ်ပြုသော မဂ်ကို အကြီးအမှူးပြုသော', 'maggārammaṇcamaggādhipat': 'မဂ်ကို အာရုံပြုသော၊ မဂ်ကို အကြီးအမှူးပြုသော', 'maggahetukcamaggādhipat': 'မဂ်ကို အမြစ်ပြုသော၊ မဂ်ကို အကြီးအမှူးပြုသော'}  [TRIADS]
- paritta = (?:aṃ|o|ā|ānaṃ|añca|assa|e(?! (?:ekūnavīsati|catuvīsati|pannarasa|sattarasa|aṭṭhārasa|ekavīsati|dvāvīsati|bāvīsati|tevīsati|cattāri|ekādasa|dvādasa|cuddasa|terasa|soḷasa|vīsati|tevīsa|pañca|satta|aṭṭha|ekaṃ|tīṇi|nava|dasa|dve|cha)(?![\wāīūṃṅñṭḍṇḷ])(?! khandh))|āni|ena|opi|amūlakā|amūlake|agacchantena|āya|ādhipati|acittasamaṅgissa)(?![\wāīūṃṅñṭḍṇḷ])  [TRIAD_END]
- parittarammana = (?:aṃ|o|ā|ānaṃ|añca|assa|e(?! (?:ekūnavīsati|catuvīsati|pannarasa|sattarasa|aṭṭhārasa|ekavīsati|dvāvīsati|bāvīsati|tevīsati|cattāri|ekādasa|dvādasa|cuddasa|terasa|soḷasa|vīsati|tevīsa|pañca|satta|aṭṭha|ekaṃ|tīṇi|nava|dasa|dve|cha)(?![\wāīūṃṅñṭḍṇḷ])(?! khandh))|āni|ena|opi|amūlakā|amūlake|agacchantena|āya|ādhipati|acittasamaṅgissa)(?![\wāīūṃṅñṭḍṇḷ])  [TRIAD_END]
- hina = (?:aṃ|o|ā|ānaṃ|añca|assa|e(?! (?:ekūnavīsati|catuvīsati|pannarasa|sattarasa|aṭṭhārasa|ekavīsati|dvāvīsati|bāvīsati|tevīsati|cattāri|ekādasa|dvādasa|cuddasa|terasa|soḷasa|vīsati|tevīsa|pañca|satta|aṭṭha|ekaṃ|tīṇi|nava|dasa|dve|cha)(?![\wāīūṃṅñṭḍṇḷ])(?! khandh))|āni|ena|opi|amūlakā|amūlake|agacchantena|āya|ādhipati|acittasamaṅgissa)(?![\wāīūṃṅñṭḍṇḷ])  [TRIAD_END]
- micchatta = (?:aṃ|o|ā|ānaṃ|añca|assa|e(?! (?:ekūnavīsati|catuvīsati|pannarasa|sattarasa|aṭṭhārasa|ekavīsati|dvāvīsati|bāvīsati|tevīsati|cattāri|ekādasa|dvādasa|cuddasa|terasa|soḷasa|vīsati|tevīsa|pañca|satta|aṭṭha|ekaṃ|tīṇi|nava|dasa|dve|cha)(?![\wāīūṃṅñṭḍṇḷ])(?! khandh))|āni|ena|opi|amūlakā|amūlake|agacchantena|āya|ādhipati|acittasamaṅgissa)(?![\wāīūṃṅñṭḍṇḷ])  [TRIAD_END]
- magga = (?:aṃ|o|ā|ānaṃ|añca|assa|e(?! (?:ekūnavīsati|catuvīsati|pannarasa|sattarasa|aṭṭhārasa|ekavīsati|dvāvīsati|bāvīsati|tevīsati|cattāri|ekādasa|dvādasa|cuddasa|terasa|soḷasa|vīsati|tevīsa|pañca|satta|aṭṭha|ekaṃ|tīṇi|nava|dasa|dve|cha)(?![\wāīūṃṅñṭḍṇḷ])(?! khandh))|āni|ena|opi|amūlakā|amūlake|agacchantena|āya|ādhipati|acittasamaṅgissa)(?![\wāīūṃṅñṭḍṇḷ])  [TRIAD_END]
- combo = (?:aṃ|o|ā|ānaṃ|añca|assa|e(?! (?:ekūnavīsati|catuvīsati|pannarasa|sattarasa|aṭṭhārasa|ekavīsati|dvāvīsati|bāvīsati|tevīsati|cattāri|ekādasa|dvādasa|cuddasa|terasa|soḷasa|vīsati|tevīsa|pañca|satta|aṭṭha|ekaṃ|tīṇi|nava|dasa|dve|cha)(?![\wāīūṃṅñṭḍṇḷ])(?! khandh))|āni|ena|opi|amūlakā|amūlake|agacchantena|āya|ādhipati|acittasamaṅgissa)(?![\wāīūṃṅñṭḍṇḷ])  [TRIAD_END]
- Parittattikaṃ = အကန့်အသတ် ရှိခြင်း သုံးမျိုးတွဲ  [NEW]
- Parittārammaṇattikaṃ = အကန့်အသတ် ရှိသည်ကို အာရုံပြုခြင်း သုံးမျိုးတွဲ  [NEW]
- Hīnattikaṃ = ယုတ်ညံ့ခြင်း သုံးမျိုးတွဲ  [NEW]
- Micchattaniyatattikaṃ = မှားယွင်းမှု၌ ကျိန်းသေခြင်း သုံးမျိုးတွဲ  [NEW]
- Maggārammaṇattikaṃ = မဂ်ကို အာရုံပြုခြင်း သုံးမျိုးတွဲ  [NEW]
- niddisitabbaṃ = ညွှန်ပြရမည်  [NEW]
- na kātabbaṃ = မပြုရ  [NEW]
- cakkaṃ (kātabbaṃ) = စက်ဝိုင်းကဲ့သို့ လှည့်ပတ်၍  [NEW]
- (evaṃ gaṇetabbaṃ) = (ထိုနည်းတူ ရေတွက်ရမည်)  [NEW]
- (sabbepi mahābhūtā kātabbā) = (မူလဓာတ်ကြီး အားလုံးကိုလည်း ပြုရမည်)  [NEW]
- (sabbe mahābhūtā kātabbā) = (မူလဓာတ်ကြီး အားလုံးကို ပြုရမည်)  [NEW]
- (tisso pañhā kātabbā) = (ပြဿနာ သုံးခု ပြုရမည်)  [NEW]
- (terasa pañhā) = (ပြဿနာ ဆယ့်သုံးခု)  [NEW]
- (vitthāretabbaṃ) = (အကျယ် ချဲ့ရမည်)  [NEW]
- (paṭisandhikkhaṇe tīṇipi kātabbā) = (ပဋိသန္ဓေ နေသော ခဏ၌ သုံးခုလုံးကိုလည်း ပြုရမည်)  [NEW]
- (paṭisandhi natthi, sattarasa pañhā paripuṇṇā) = (ပဋိသန္ဓေ မရှိ၊ ပြဿနာ ဆယ့်ခုနစ်ခု ပြည့်စုံကြသည်)  [NEW]
- (paṭiccavārasadisā dvādasa pañhā) = (မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူသော ပြဿနာ ဆယ့်နှစ်ခု)  [NEW]
- (paripuṇṇaṃ, vipākoti niddisitabbaṃ cittasamuṭṭhānaṃ rūpaṃ vipākoti na kātabbaṃ) = (ပြည့်စုံသည်၊ ကံ၏ အကျိုးဟု ညွှန်ပြရမည် စိတ်မှ ဖြစ်ပေါ်လာသော ရုပ်ကို ကံ၏ အကျိုးဟု မပြုရ)  [NEW]
- (paṭisandhivipākopi natthi) = (ပဋိသန္ဓေ၌ ကံ၏ အကျိုးလည်း မရှိ)  [NEW]
- (paṭisandhi natthi) = (ပဋိသန္ဓေ မရှိ)  [NEW]
- (vipākopi paṭisandhipi natthi) = (ကံ၏ အကျိုးလည်း၊ ပဋိသန္ဓေလည်း မရှိ)  [NEW]
- (pavattipaṭisandhi kātabbā) = (ဘဝ ဖြစ်ဆဲ ကာလနှင့် ပဋိသန္ဓေကို ပြုရမည်)  [NEW]
- (tisso pañhā, pavattipaṭisandhi kātabbā) = (ပြဿနာ သုံးခု၊ ဘဝ ဖြစ်ဆဲ ကာလနှင့် ပဋိသန္ဓေကို ပြုရမည်)  [NEW]
- (pavattimeva) = (ဘဝ ဖြစ်ဆဲ ကာလသာ)  [NEW]
- (cakkaṃ kātabbaṃ) = (စက်ဝိုင်းကဲ့သို့ လှည့်ပတ်၍ ပြုရမည်)  [NEW]
- (cakkaṃ kātabbaṃ kusalattikasadisaṃ) = (စက်ဝိုင်းကဲ့သို့ လှည့်ပတ်၍ ကုသိုလ် သုံးမျိုးတွဲနှင့် တူအောင် ပြုရမည်)  [NEW]
- (paṭiccavārasadisaṃ = (မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူသည်  [NEW]
- (paṭiccavārasadisā kātabbā) = (မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူအောင် ပြုရမည်)  [NEW]
- (sabbe paccayā iminā kāraṇena vitthāretabbā = (အကြောင်း အားလုံးကို ဤနည်းလမ်းဖြင့် အကျယ် ချဲ့ရမည်  [NEW]
- (saṃkhittaṃ, sabbāni paccayāni vitthāretabbāni) = (အကျဉ်းချုပ်၊ အကြောင်း အားလုံးကို အကျယ် ချဲ့ရမည်)  [NEW]
- micchatta- (-sadisaṃ: the micchattaniyata part) = မှားယွင်းမှု အပိုင်း  [NEW]
- (tīṇi pañhā, micchattasadisaṃ) = (ပြဿနာ သုံးခု၊ မှားယွင်းမှု အပိုင်းနှင့် တူသည်)  [NEW]
- (saṃkhittaṃ, kusalattike paccayavārasadisaṃ vibhajitabbaṃ) = (အကျဉ်းချုပ်၊ ကုသိုလ် သုံးမျိုးတွဲ၌ အကြောင်းပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူအောင် ခွဲခြမ်းစိတ်ဖြာရမည်)  [NEW]
- (kusalattikasadisaṃ, pañca kātabbā) = (ကုသိုလ် သုံးမျိုးတွဲနှင့် တူသည်၊ ငါးခု ပြုရမည်)  [NEW]
- (paripuṇṇaṃ) = (ပြည့်စုံသည်)  [NEW]
- (paṭiccavārasadisaṃ, nava pañhā) = (မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူသည်၊ ပြဿနာ ကိုးခု)  [NEW]
- (paṭiccavārasadisaṃ, tisso pañhā) = (မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူသည်၊ ပြဿနာ သုံးခု)  [NEW]
- (kusalattikasadisā, terasa pañhā) = (ကုသိုလ် သုံးမျိုးတွဲနှင့် တူကြသည်၊ ပြဿနာ ဆယ့်သုံးခု)  [NEW]
- (tisso pañhā) = (ပြဿနာ သုံးခု)  [NEW]
- (paripuṇṇā dvepi) = (နှစ်ခုလုံးလည်း ပြည့်စုံကြသည်)  [NEW]
- (pañca pañhā) = (ပြဿနာ ငါးခု)  [NEW]
- (paṭhamaghaṭane tīṇi) = (ပထမ ပေါင်းစပ်ချက်၌ သုံးခု)  [NEW]
- (dutiyaghaṭane tīṇi pañhā) = (ဒုတိယ ပေါင်းစပ်ချက်၌ ပြဿနာ သုံးခု)  [NEW]
- (paripuṇṇaṃ, arūpanti niyāmetabbaṃ) = (ပြည့်စုံသည်၊ ရုပ် မဟုတ်သော သဘောတရားဟု သတ်မှတ်ရမည်)  [NEW]
- (iminā kāraṇena sattarasa pañhā kātabbā) = (ဤနည်းလမ်းဖြင့် ပြဿနာ ဆယ့်ခုနစ်ခု ပြုရမည်)  [NEW]
- (tīsupi sattarasa pañhā kātabbā) = (သုံးခုလုံး၌လည်း ပြဿနာ ဆယ့်ခုနစ်ခု ပြုရမည်)  [NEW]
- (anantarasadisaṃ = (ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းနှင့် တူသည်  [NEW]
- (nānākkhaṇikā natthi, sattarasa pañhā kātabbā) = (ခဏ ကွဲပြားသည့် ကံ မရှိ၊ ပြဿနာ ဆယ့်ခုနစ်ခု ပြုရမည်)  [NEW]
- (ime satta paccayā sattarasa pañhā hetusadisā) = (ဤ အကြောင်း ခုနစ်ပါး၌ ပြဿနာ ဆယ့်ခုနစ်ခု အမြစ်နှင့် တူကြသည်)  [NEW]
- (anantarasadisā) = (ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းနှင့် တူကြသည်)  [NEW]
- (sattarasa pañhā) = (ပြဿနာ ဆယ့်ခုနစ်ခု)  [NEW]
- pakatārammaṇa = ပကတိ အာရုံ  [NEW]
- upanissayārammaṇa = အားကြီးသော အမှီ အာရုံ  [NEW]
- gahite = ယူသောအခါ  [NEW]
- chijjanti = ပြတ်ကြသည်  [NEW]
- (naārammaṇe gahite pakatārammaṇampi upanissayārammaṇampi dvepi chijjanti) = (အာရုံဟူသော အကြောင်း မဟုတ်ခြင်းကို ယူသောအခါ ပကတိ အာရုံလည်း၊ အားကြီးသော အမှီ အာရုံလည်း နှစ်ခုလုံး ပြတ်ကြသည်)  [NEW]
- aññesu tikesu oloketabbaṃ = အခြား သုံးမျိုးတွဲတို့၌ ကြည့်ရှုရမည်  [NEW]
- {nevasaññānāsaññāyatanassa (?) aññesu tikesu oloketabbaṃ} = ပါဌ်ကွဲ ((မသေချာ)): nevasaññānāsaññāyatanassa အခြား သုံးမျိုးတွဲတို့၌ ကြည့်ရှုရမည်  [NEW]
- (Sahajātavāropi paṭiccavārasadiso.) = (အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်သည်လည်း မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူသည်။)  [NEW]
- (Nissayavāro paccayavārasadiso.) = (အမှီပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်သည် အကြောင်းပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူသည်။)  [NEW]
- (Sampayuttavāro saṃsaṭṭhavārasadiso). = (ယှဉ်တွဲခြင်းအလိုက် ဖော်ပြချက်သည် ရောနှောခြင်းအလိုက် ဖော်ပြချက်နှင့် တူသည်)။  [NEW]
- (Samanantarapaccayaṃ anantarapaccayasadisaṃ.) = ({C1.n}သည် ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းဟူသော အကြောင်းနှင့် တူသည်။)  [NEW]
- Anulomaṃ. (closing the positive order) = အဟုတ်ပြ ပုံစံ။  [NEW]
- (Hīnattikaṃ saṃkiliṭṭhattikasadisaṃ vitthāretabbaṃ paripuṇṇaṃ.) = (ယုတ်ညံ့ခြင်း သုံးမျိုးတွဲကို ကိလေသာဖြင့် ညစ်နွမ်းခြင်း သုံးမျိုးတွဲနှင့် တူအောင် ပြည့်စုံစွာ အကျယ် ချဲ့ရမည်။)  [NEW]
- (Sahajātavāropi paccayavāropi nissayavāropi saṃsaṭṭhavāropi sampayuttavāropi paṭiccavārasadiso). = (အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း၊ အကြောင်းပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်လည်း၊ အမှီပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်လည်း၊ ရောနှောခြင်းအလိုက် ဖော်ပြချက်လည်း၊ ယှဉ်တွဲခြင်းအလိုက် ဖော်ပြချက်လည်း မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူသည်)။  [NEW]
- (Sahajātavāro paṭiccavārasadiso.) = (အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်သည် မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူသည်။)  [NEW]
- (Sahajātavāropi paccayavāropi nissayavāropi saṃsaṭṭhavāropi sampayuttavāropi paṭiccavārasadiso.) = (အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း၊ အကြောင်းပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်လည်း၊ အမှီပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်လည်း၊ ရောနှောခြင်းအလိုက် ဖော်ပြချက်လည်း၊ ယှဉ်တွဲခြင်းအလိုက် ဖော်ပြချက်လည်း မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူသည်။)  [NEW]
- (Nissayavāro paccayavārasadiso). = (အမှီပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်သည် အကြောင်းပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူသည်)။  [NEW]
- parāmasantassa = မှားယွင်းစွာ ယူဆသူ၏  [NEW]
- Yaṃ vatthuṃ parāmasantassa micchattaniyatā khandhā uppajjanti, taṃ vatthu micchattaniyatānaṃ khandhānaṃ ārammaṇapaccayena paccayo. = အကြင် မှီရာ ဝတ္ထုကို မှားယွင်းစွာ ယူဆသူ၏ {T1} အစုအဝေးတို့သည် ဖြစ်ပေါ်ကြ၏၊ ထို မှီရာ ဝတ္ထုသည် {T2} အစုအဝေးတို့အား {C1.if}။  [NEW]
- tasseva = ထိုအရာကိုယ်တိုင်  [NEW]
- maggapaccavekkhaṇaṃ = မဂ်ကို ပြန်လည် ဆင်ခြင်ခြင်း  [NEW]
- phalapaccavekkhaṇaṃ = ဖိုလ်ကို ပြန်လည် ဆင်ခြင်ခြင်း  [NEW]
- nibbānapaccavekkhaṇaṃ = နိဗ္ဗာန်ကို ပြန်လည် ဆင်ခြင်ခြင်း  [NEW]
- dibbacakkhupaccavekkhaṇaṃ = နတ်မျက်စိကို ပြန်လည် ဆင်ခြင်ခြင်း  [NEW]
- dibbasotadhātupaccavekkhaṇaṃ = နတ်နား ဓာတ်ကို ပြန်လည် ဆင်ခြင်ခြင်း  [NEW]
- ākāsānañcāyatanapaccavekkhaṇaṃ = အဆုံး မရှိသော ဟင်းလင်းပြင် နယ်ပယ်ကို ပြန်လည် ဆင်ခြင်ခြင်း  [NEW]
- viññāṇañcāyatanapaccavekkhaṇaṃ = အဆုံး မရှိသော သိစိတ် နယ်ပယ်ကို ပြန်လည် ဆင်ခြင်ခြင်း  [NEW]
- ākiñcaññāyatanapaccavekkhaṇaṃ = ဘာမျှ မရှိသော နယ်ပယ်ကို ပြန်လည် ဆင်ခြင်ခြင်း  [NEW]
- nevasaññānāsaññāyatanapaccavekkhaṇaṃ = မှတ်သိမှု ရှိသည်လည်း မဟုတ်၊ မှတ်သိမှု မရှိသည်လည်း မဟုတ်သော နယ်ပယ်ကို ပြန်လည် ဆင်ခြင်ခြင်း  [NEW]
- paṭhamajjhānapaccavekkhaṇaṃ = ပထမ ဈာန်ကို ပြန်လည် ဆင်ခြင်ခြင်း  [NEW]
- dutiyajjhānapaccavekkhaṇaṃ = ဒုတိယ ဈာန်ကို ပြန်လည် ဆင်ခြင်ခြင်း  [NEW]
- tatiyajjhānapaccavekkhaṇaṃ = တတိယ ဈာန်ကို ပြန်လည် ဆင်ခြင်ခြင်း  [NEW]
- catutthajjhānapaccavekkhaṇaṃ = စတုတ္ထ ဈာန်ကို ပြန်လည် ဆင်ခြင်ခြင်း  [NEW]
- iddhividhañāṇapaccavekkhaṇaṃ = တန်ခိုး အမျိုးမျိုးကို ပြနိုင်သော ဉာဏ်ကို ပြန်လည် ဆင်ခြင်ခြင်း  [NEW]
- cetopariyañāṇapaccavekkhaṇaṃ = စိတ်ကို ပိုင်းခြား၍ သိသော ဉာဏ်ကို ပြန်လည် ဆင်ခြင်ခြင်း  [NEW]
- pubbenivāsānussatiñāṇapaccavekkhaṇaṃ = ရှေးဘဝများကို အဖန်ဖန် အောက်မေ့နိုင်သော ဉာဏ်ကို ပြန်လည် ဆင်ခြင်ခြင်း  [NEW]
- yathākammūpagañāṇapaccavekkhaṇaṃ = ကံအားလျော်စွာ ဖြစ်ပေါ်ပုံကို သိသော ဉာဏ်ကို ပြန်လည် ဆင်ခြင်ခြင်း  [NEW]
- anāgataṃsañāṇapaccavekkhaṇaṃ = အနာဂတ်ကို သိသော ဉာဏ်ကို ပြန်လည် ဆင်ခြင်ခြင်း  [NEW]
- (avasesā cha pañhā hetupaccayasadisā satta kātabbā) = (ကြွင်းသော ပြဿနာ ခြောက်ခုကို အမြစ်ဟူသော အကြောင်းနှင့် တူအောင် ခုနစ်ခု ပြုရမည်)  [NEW]
- (sabbe mahābhūtā vitthāretabbā, arūpe parittamūlake tisso pañhā) = (မူလဓာတ်ကြီး အားလုံးကို အကျယ် ချဲ့ရမည်၊ ရုပ်မရှိသော ဘုံ၌ အကန့်အသတ် ရှိသော သဘောတရားကို အခြေခံခြင်း၌ ပြဿနာ သုံးခု)  [NEW]
- (mahaggatārammaṇe paṭisandhi natthi) = (ကြီးမြတ်သည်ကို အာရုံပြုသော သဘောတရား၌ ပဋိသန္ဓေ မရှိ)  [NEW]
- (napacchājātapaccayañca naāsevanapaccayañca naadhipatisadisaṃ) = (နောက်မှ ဖြစ်ပေါ်ခြင်းဟူသော အကြောင်း မဟုတ်ခြင်းလည်းကောင်း၊ အလေ့အကျင့် ပြုခြင်းဟူသော အကြောင်း မဟုတ်ခြင်းလည်းကောင်း အကြီးအမှူး မဟုတ်ခြင်းနှင့် တူသည်)  [NEW]
- (dve pañhā micchattaniyatasadisā) = (ပြဿနာ နှစ်ခု မှားယွင်းမှု၌ ကျိန်းသေသော သဘောတရားနှင့် တူကြသည်)  [NEW]
