# pi-7 (Paṭṭhāna) Burmese zero-shot: 2-01 vitakkattika, 2-02 pītittika — notes

Files: `AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters/` 2-01-vitakkattika.md, 2-02-pitittika.md.
Translated from the Pāli only (no Burmese translation or nissaya opened, no web search, `language-priority/` not
opened). Meaning cross-checked only against the English pi-7 zero-shot (2-02 rapture lines). Generator:
`make_ch2-01-02.py` (imports `my7_formulas.py`, the sample's tables from `make_sample.py` and the in-memory extensions
of `make_ch1-03-05.py`; none of them is edited, nothing of theirs is written). Check: `check_ch2-01-02.py` (adapted
from check_ch1-03-05.py). `--new` lists every string the generator adds (the list below).

## Status (all pass, 2026-11-23)
| file | segments | lines | check_chapter_ids | check_text_pe7 (own scratch chk-pe/ch2-01-02/) | check_marks | check_ch2-01-02 |
|---|---|---|---|---|---|---|
| 2-01-vitakkattika.md | 244 | 732 | OK | OK | OK | OK |
| 2-02-pitittika.md | 103 | 203 | OK | OK | OK | OK |

check_ch2-01-02 (`--sample --pe --mutate`): 935 lines × (structure, polarity, conditions, term order, numbers), 2367
sentences for identity (with the sample and 1-03 … 1-05 on disk), 72 table values: **0 mismatches**. Reuse test:
**88 / 88** pi-1 … pi-6 values identical wherever their Pāli occurs; sentences also in pi-1 … pi-6: **461 / 461**.
Sample identity: 1-00 and 1-02 regenerated in memory with all extensions = the files on disk (raw and prep); the group
1-03 … 1-05 regenerated in memory (its own prep) with all of this script's extensions = its files on disk.
Mutation test 8 / 8 caught (count, polarity, term order, condition, khandha count, term, digits, note).
No existing value of my7_formulas / make_sample / make_ch1-03-05 was changed, except (in memory) the term-ending regex
of the 1-03 … 1-05 triads: its «-e <count>» exclusion now also knows the counts above 24, so «vipāke ekavīsa» stays the
condition (1-03 … 1-05 output unchanged).

## Triad terms (pi-1 Mātikā ^1-M1-6 / ^1-M1-7, read from the FINAL rails by W())
- savitakkasavicāra = စတင်ကြံစည်မှုနှင့် ဆက်လက်သုံးသပ်မှု ရှိသော
- avitakkavicāramatta = စတင်ကြံစည်မှု မရှိဘဲ ဆက်လက်သုံးသပ်မှုသာ ရှိသော
- avitakkaavicāra = စတင်ကြံစည်မှုလည်း မရှိ၊ ဆက်လက်သုံးသပ်မှုလည်း မရှိသော
- pītisahagata = ပီတိနှင့်အတူ ဖြစ်သော; sukhasahagata = သာယာမှုနှင့်အတူ ဖြစ်သော (= the module's QUAL sukhasahagataṃ);
  upekkhāsahagata = ဥပေက္ခာနှင့်အတူ ဖြစ်သော
- Vitakkattikaṃ = စတင်ကြံစည်မှု သုံးမျိုးတွဲ (pi-2 ^2-18-10-5-0); Pītittikaṃ = ပီတိ သုံးမျိုးတွဲ (NEW, same pattern).
- nouns vitakka စတင်ကြံစည်မှု, vicāra ဆက်လက်သုံးသပ်မှု (pi-1).
- pīti + sukha on ONE noun («pītisahagatā ca sukhasahagatā ca tayo khandhā», «pītisahagatañca sukhasahagatañca ekaṃ
  khandhaṃ», «… cittena», «… maggassa», «pītisahagatasukhasahagatacittasamaṅgissa»): one aggregate accompanied by
  both = the two qualifiers stacked «ပီတိနှင့်အတူ ဖြစ်သော၊ သာယာမှုနှင့်အတူ ဖြစ်သော N» (the module's stacking of two
  sahagata qualifiers; English zero-shot: "accompanied by rapture and accompanied by happiness"). With the noun
  dhamma the module's coordination stays: «pītisahagatañca sukhasahagatañca dhammaṃ» = «A သဘောတရားနှင့် B သဘောတရား».

## Engine extensions (in memory, make_ch2-01-02.py)
- prep(): 1-03 … 1-05 prep, then the pīti+sukha join (one slot «pītisukhasahagat-»), «X-ādhipati» = «X-o adhipati» for
  these terms, placeholders for notes whose Pāli holds condition / term words (NOTEP), slips.
- coordination: «A B ca» (one «ca» after the last conjunct) and lists the module cannot split, by head nouns
  (_conj; not after a term «ca», conjuncts of one case); the same inside the lexicon frame (lex: «Aလည်းကောင်း၊
  Bလည်းကောင်း», recipient «Aအားလည်းကောင်း၊ …», object «Aကိုလည်းကောင်း၊ …»; «၊» between two adjacent groups).
- «[NP-nom] NP-acc Xpaccayā» (vippayutta) = «NP-သည် NP-ကို …ကြောင့်» (as 1-01 renders «Khandhā vatthuṃ vippayuttapaccayā»).
- counting lines with bare locatives sharing the next count («anantare samanantare … dasa», «… sabbattha dasa»,
  «… sabbe dasa»): «A၌၊ B၌ … N»; sabbattha «နေရာတိုင်း၌» (as 1-01), sabbe «အားလုံး».
- two pañhā sentences joined by «, » in one unit; a pañhā sentence followed by a note, or by «(note) count».
- counts above 24 and the short forms (ekavīsa 21, bāvīsa 22 …), Burmese number + «ခု».
- bare condition stems before «…» («āhāra… indriya…») = the bare names (as abbreviated in the Pāli).

## Unsure Pāli
- «Savitakkasavicāramūlakā … pañhā» = «… သဘောတရားကို အခြေခံသော ပြဿနာ»; «naadhipatiyā kātabbā» «… မဟုတ်ခြင်း၌ ပြုရမည်».
- «(Naāsevanamūlake avitakkavicāramattaṃ vipākena saha gacchantena napurejātasadisaṃ kātabbaṃ, avitakkavicāramattañca
  avitakkavicāramattagacchantena vipāko dassetabbo.)»: gacchantena «တွဲ၍ သွားစေလျက်»; the second clause read as «…ကိုလည်း
  … နှင့် တွဲ၍ သွားစေလျက် ကံ၏ အကျိုး ဖြစ်သော သဘောတရားကို ပြသရမည်».
- «Yattha avitakkavicāramattaṃ āgacchati tattha vipākaṃ kātabbaṃ» = «… ပါဝင်လာ၏ ထိုနေရာ၌ ကံ၏ အကျိုး ဖြစ်သော
  သဘောတရားအဖြစ် ပြုရမည်» (vipāka as the 1-03 term, «make it resultant»).
- «(paṭhamaudāharaṇe pavatte paṭisandhikkhaṇe …)»: udāharaṇa «ဥပမာ», pavatti «ဘဝ ဖြစ်ဆဲ ကာလ».
- «sattasu ṭhānesu satta mohā uddharitabbā mūlapadesuyeva» = «နေရာ ခုနစ်ခု၌ မောဟ ခုနစ်ခုကို မူလ ပုဒ်တို့၌သာ ထုတ်နုတ်ရမည်»;
  «Naārammaṇe satta cittasamuṭṭhānā uddharitabbā» adds «ရုပ်» («စိတ်မှ ဖြစ်ပေါ်လာသော ရုပ် ခုနစ်ခု», clarification).
- «(Tāniyeva ca gamanāni niyāmetabbāni.)» gamanāni «သွားပုံ»; «Pītinayaṃ» «ပီတိ နည်း»; «(sukhamūle tīṇi)» «(သာယာမှုကို
  အခြေခံခြင်း၌ သုံးခု)»; «arūpapañhameva» «ရုပ် မဟုတ်သော သဘောတရားဆိုင်ရာ ပြဿနာသာ»; «(Nissayampi ninnānaṃ)» «(…လည်း
  ကွဲပြားခြင်း မရှိ)»; anumajjantena «အစဉ်လိုက် သုံးသပ်လျက်».
- «pacchimānaṃ pacchimānaṃ pītisahagatānañca sukhasahagatānañca āsevanapaccayena» (no noun): the frame's noun
  «သဘောတရား» supplied (as 1-03 … 1-05 do for «X-assa ca Y-assa ca»).

## Source slips (translated as written; normalised only where a frame needs it; logged by the generator)
- 2-01 «… dve khandhā vicāro ca paṭisandhikkhaṇe…pe….» (^7-7-9): no full stop before «paṭisandhikkhaṇe»; none added.
- 2-01 «Paṭisandhikkhaṇe vatthuṃ paṭicca avitakkavicāramattā khandhā mahābhūte paṭicca kaṭattārūpaṃ»: no comma between
  the two pairs; none added (the pairs are joined by a space).
- 2-01 «… avitakkavicāramatto dhammo uppajjati naadhipatipaccayā, avitakkavicāramatte khandhe …»: a comma where the
  frame has «–»; rendered «၊», no dash added.
- 2-01 «gotrabhu ca vitakko ca savitakkasavicārassa ca maggassa ca vitakkassa ca» (an extra «ca» after the term; the
  next phrase has none): read as «savitakkasavicārassa maggassa ca».
- 2-01 «vicākānaṃ» = vipākānaṃ; «avitakka vicāramattassa» written apart; «nasampayuttanavippayutta» (no hyphen in the
  negated compound).
- 2-01 «parikammaṃ dibbāya sotadhātuyā…»: the recipient (genitive), not the instrumental of «dibbāya sotadhātuyā
  saddaṃ suṇāti» (a separate in-memory LEX key).

## For the coordinator
1. pīti + sukha on one noun is rendered as two stacked qualifiers «A၊ B N»; with dhamma as «A Nနှင့် B N» (module).
   Worth a look in the consistency pass together with the dukatika / tikaduka chapters.
2. Instruction vocabulary aligned with 1-01 where it exists (kātabbaṃ «ပြုရမည်», sabbattha «နေရာတိုင်း၌»,
   -sadisaṃ kātabbaṃ «နှင့် တူအောင် ပြုရမည်», -sadisā «နှင့် တူကြသည်»); the other words below are NEW.
3. «(naXsadisaṃ)» (bare) = «(N မဟုတ်ခြင်းနှင့် တူသည်)», parallel to the sample's bare «(Xsadisaṃ)» «(Nနှင့် တူသည်)».

## New strings of this script («Pāli = Burmese», table in brackets; SK = whole-unit templates by their skeleton,
## «(frame)» = built from slots; the 24 bare condition names before «…» are SKF entries = the bare names N)
- vitakko = စတင်ကြံစည်မှု  [NOUN]
- vitakkaṃ = စတင်ကြံစည်မှု  [NOUN]
- vitakkassa = စတင်ကြံစည်မှု  [NOUN]
- vicāro = ဆက်လက်သုံးသပ်မှု  [NOUN]
- vicāraṃ = ဆက်လက်သုံးသပ်မှု  [NOUN]
- vicārassa = ဆက်လက်သုံးသပ်မှု  [NOUN]
- purimo purimo = ရှေးရှေး  [QUAL]
- pacchimassa pacchimassa = နောက်နောက်  [QUAL]
- vicikicchāsahagataṃ = ယုံမှားမှုနှင့်အတူ ဖြစ်သော  [QUAL]
- uddhaccasahagataṃ = ယောက်ယက်ခတ်မှုနှင့်အတူ ဖြစ်သော  [QUAL]
- kaṭattā rūpānaṃ = ကံ ပြုခဲ့သောကြောင့် ဖြစ်သော ရုပ်  [FIXED]
- vitakko = စတင်ကြံစည်မှု  [LEX]
- vicāro = ဆက်လက်သုံးသပ်မှု  [LEX]
- vitakkaṃ = စတင်ကြံစည်မှု  [LEX]
- vicāraṃ = ဆက်လက်သုံးသပ်မှု  [LEX]
- vitakkassa = စတင်ကြံစည်မှု  [LEX]
- vicārassa = ဆက်လက်သုံးသပ်မှု  [LEX]
- kāyaviññāṇaṃ = ကိုယ် သိစိတ်  [LEX]
- kāyaviññāṇassa = ကိုယ် သိစိတ်  [LEX]
- jhānassa = ဈာန်  [LEX]
- dibbassa cakkhussa = နတ်မျက်စိ  [LEX]
- dibbāya·sotadhātuyā = နတ်နား ဓာတ်  [LEX]
- ākāsānañcāyatanassa = အဆုံး မရှိသော ဟင်းလင်းပြင် နယ်ပယ်  [LEX]
- ākiñcaññāyatanassa = ဘာမျှ မရှိသော နယ်ပယ်  [LEX]
- dibbāya sotadhātuyā parikammaṃ = နတ်နား ဓာတ်၏ ကြိုတင် ပြင်ဆင်မှု  [LEX]
- jhānassa parikammaṃ = ဈာန်၏ ကြိုတင် ပြင်ဆင်မှု  [LEX]
- dibbassa cakkhussa parikammaṃ = နတ်မျက်စိ၏ ကြိုတင် ပြင်ဆင်မှု  [LEX]
- ākāsānañcāyatanassa parikammaṃ = အဆုံး မရှိသော ဟင်းလင်းပြင် နယ်ပယ်၏ ကြိုတင် ပြင်ဆင်မှု  [LEX]
- viññāṇañcāyatanassa parikammaṃ = အဆုံး မရှိသော သိစိတ် နယ်ပယ်၏ ကြိုတင် ပြင်ဆင်မှု  [LEX]
- ākiñcaññāyatanassa parikammaṃ = ဘာမျှ မရှိသော နယ်ပယ်၏ ကြိုတင် ပြင်ဆင်မှု  [LEX]
- iddhividhañāṇassa parikammaṃ = တန်ခိုး အမျိုးမျိုးကို ပြနိုင်သော ဉာဏ်၏ ကြိုတင် ပြင်ဆင်မှု  [LEX]
- cetopariyañāṇassa parikammaṃ = စိတ်ကို ပိုင်းခြား၍ သိသော ဉာဏ်၏ ကြိုတင် ပြင်ဆင်မှု  [LEX]
- pubbenivāsānussatiñāṇassa parikammaṃ = ရှေးဘဝများကို အဖန်ဖန် အောက်မေ့နိုင်သော ဉာဏ်၏ ကြိုတင် ပြင်ဆင်မှု  [LEX]
- yathākammūpagañāṇassa parikammaṃ = ကံအားလျော်စွာ ဖြစ်ပေါ်ပုံကို သိသော ဉာဏ်၏ ကြိုတင် ပြင်ဆင်မှု  [LEX]
- anāgataṃsañāṇassa parikammaṃ = အနာဂတ်ကို သိသော ဉာဏ်၏ ကြိုတင် ပြင်ဆင်မှု  [LEX]
- paṭhame jhāne = ပထမ ဈာန်၌  [LEX]
- dutiye jhāne = ဒုတိယ ဈာန်၌  [LEX]
- tatiye jhāne = တတိယ ဈာန်၌  [LEX]
- catutthe jhāne = စတုတ္ထ ဈာန်၌  [LEX]
- rūpāyatanaṃ = အဆင်းအရောင် အာရုံခံ နယ်ပယ်  [LEX]
- phoṭṭhabbāyatanaṃ = အထိအတွေ့ အာရုံခံ နယ်ပယ်  [LEX]
- cakkhāyatanaṃ = မျက်စိ အာရုံခံ နယ်ပယ်  [LEX]
- kāyāyatanaṃ = ကိုယ် အာရုံခံ နယ်ပယ်  [LEX]
- phoṭṭhabbaṃ = အထိအတွေ့  [LEX]
- samāpattiṃ = သမာပတ်  [LEX]
- abhiññaṃ = ထူးကဲစွာ သိခြင်း  [LEX]
- cakkhuviññāṇassa = မျက်စိ သိစိတ်  [LEX]
- (paṭisandhikkhaṇe natthi) = (ပဋိသန္ဓေ နေသော ခဏ မရှိ)  [NOTES]
- (purejāte paṭisandhikkhaṇe natthi) = (ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်းဟူသော အကြောင်း၌ ပဋိသန္ဓေ နေသော ခဏ မရှိ)  [NOTES]
- (naadhipatipaṭisandhikkhaṇe paripuṇṇaṃ) = (အကြီးအမှူးဟူသော အကြောင်း မဟုတ်ခြင်း၌ ပဋိသန္ဓေ နေသော ခဏ၌ ပြည့်စုံသည်)  [NOTES]
- ("arūpe"ti niyāmetabbaṃ "paṭisandhikkhaṇe"ti ca) = (“ရုပ်မရှိသော ဘုံ၌”ဟုလည်းကောင်း၊ “ပဋိသန္ဓေ နေသော ခဏ၌”ဟုလည်းကောင်း သတ်မှတ်ရမည်)  [NOTES]
- (paripuṇṇaṃ, paṭisandhi natthi) = (ပြည့်စုံသည်၊ ပဋိသန္ဓေ မရှိ)  [NOTES]
- (paṭiccavārasadisā) = (မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူကြသည်)  [NOTES]
- (dasa pañhā vitthāretabbā) = (ပြဿနာ ဆယ်ခုကို အကျယ် ချဲ့ရမည်)  [NOTES]
- (dasa pañhā kātabbā) = (ပြဿနာ ဆယ်ခု ပြုရမည်)  [NOTES]
- (natthipi vigatampi anantarasadisaṃ) = (မရှိခြင်းလည်း၊ ပျောက်ကွယ်ခြင်းလည်း ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းနှင့် တူသည်)  [NOTES]
- (sukhamūle tīṇi) = (သာယာမှုကို အခြေခံခြင်း၌ သုံးခု)  [NOTES]
- (cattāripi gaṇanāni passitvā kātabbāni) = (ရေတွက်ချက် လေးခုလုံးကိုလည်း ကြည့်၍ ပြုရမည်)  [NOTES]
- (paripuṇṇaṃ kātabbaṃ) = (ပြည့်စုံအောင် ပြုရမည်)  [NOTES]
- (paccanīyaṃ paripuṇṇaṃ kātabbaṃ) = (အငြင်းပြ ပုံစံကို ပြည့်စုံအောင် ပြုရမည်)  [NOTES]
- (evaṃ paṭisandhikkhaṇe cattāro) = (ထိုနည်းတူ ပဋိသန္ဓေ နေသော ခဏ၌ လေးပါး)  [NOTES]
- (pavattipi, paṭisandhipi dīpetabbā) = (ဘဝ ဖြစ်ဆဲ ကာလကိုလည်း၊ ပဋိသန္ဓေကိုလည်း ဖော်ပြရမည်)  [NOTES]
- (dve vārā vitthāretabbā) = (ဖော်ပြချက် နှစ်ခုကို အကျယ် ချဲ့ရမည်)  [NOTES]
- (paṭhamaudāharaṇe pavatte paṭisandhikkhaṇe satta pañhā kātabbā) = (ပထမ ဥပမာ၌ ဘဝ ဖြစ်ဆဲ ကာလ၌၊ ပဋိသန္ဓေ နေသော ခဏ၌ ပြဿနာ ခုနစ်ခု ပြုရမည်)  [NOTES]
- (yathā paṭiccanaye tathā pañca pañhā kātabbā) = (မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်၏ နည်း၌ ပြုသကဲ့သို့ ထိုနည်းတူ ပြဿနာ ငါးခု ပြုရမည်)  [NOTES]
- (naārammaṇasadisaṃ) = (အာရုံ မဟုတ်ခြင်းနှင့် တူသည်)  [NOTES]
- (paṭisandhikāni cattāri. = (ပဋိသန္ဓေနှင့် ဆိုင်သည်တို့ လေးခု။  [NOTES]
- (⁑0) = (အလေ့အကျင့် ပြုခြင်းဟူသော အကြောင်း၌ ကံ၏ အကျိုး မရှိ)  [NOTES]
- (⁑1) = (ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းဟူသော အကြောင်းလည်း၊ ကောင်းစွာ ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းဟူသော အကြောင်းလည်း တူသည်)  [NOTES]
- (⁑2) = (မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူသည်၊ အတူ ပေါ်ပေါက်ခြင်းဟူသော အကြောင်း၌ ပြဿနာ ဆယ်ခု)  [NOTES]
- (⁑3) = (လေးခု ပြုရမည်၊ ပီတိနှင့်အတူ ဖြစ်သော သဘောတရားကို အစဉ်လိုက် သုံးသပ်လျက် ခွဲခြမ်းစိတ်ဖြာရမည်)  [NOTES]
- Vitakkattikaṃ niṭṭhitaṃ. = “စတင်ကြံစည်မှု သုံးမျိုးတွဲ” ပြီးဆုံးပြီ။  [HLINES]
- Pītittikaṃ niṭṭhitaṃ. = “ပီတိ သုံးမျိုးတွဲ” ပြီးဆုံးပြီ။  [HLINES]
- (Dutiyo bhāgo) = (ဒုတိယ အပိုင်း)  [HLINES]
- Paccanīye = အငြင်းပြ ပုံစံ၌  [HLINES]
- Paccanīyānulomaṃ = အငြင်းပြ အဟုတ်ပြ ပုံစံ  [HLINES]
- *Natthivigatāvigatapaccayā* = *မရှိခြင်းဟူသော အကြောင်း၊ ပျောက်ကွယ်ခြင်းဟူသော အကြောင်းနှင့် မပျောက်ကွယ်ခြင်းဟူသော အကြောင်း*  [HLINES]
- *2-6. Sahajāta-paccaya-nissaya-saṃsaṭṭha-sampayuttavāro* = *2-6. အတူ ပေါ်ပေါက်ခြင်း၊ အကြောင်းပြု၍ ဖြစ်ပေါ်ခြင်း၊ အမှီပြု၍ ဖြစ်ပေါ်ခြင်း၊ ရောနှောခြင်းနှင့် ယှဉ်တွဲခြင်းအလိုက် ဖော်ပြချက်*  [HLINES]
- §C§o = {C1.n}  [SK]
- (dve paccayā sajjhāyamaggena vibhattā, evaṃ avasesā vīsatipaccayā vibhajitabbā.) = (အကြောင်း နှစ်ပါးကို သရဇ္ဈာယ်သည့် နည်းလမ်းအတိုင်း ခွဲခြမ်းစိတ်ဖြာထားသည့်အတိုင်း ကြွင်းသော အကြောင်း နှစ်ဆယ်ပါးကိုလည်း ထိုနည်းတူ ခွဲခြမ်းစိတ်ဖြာရမည်။)  [SK]
- (napurejātamūlake yathā suddhikaṃ arūpaṃ, tathā arūpā kātabbā). = (ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်းဟူသော အကြောင်း မဟုတ်ခြင်းကို အခြေခံခြင်း၌ ရိုးရိုး ရုပ် မဟုတ်သော သဘောတရားကဲ့သို့၊ ထို့အတူ ရုပ် မဟုတ်သော သဘောတရားများကို ပြုရမည်)။  [SK]
- (naāsevanamūlake §T§aṃ vipākena saha gacchantena napurejātasadisaṃ kātabbaṃ, §T§añca §T§agacchantena §T§o dassetabbo.) = (အလေ့အကျင့် ပြုခြင်းဟူသော အကြောင်း မဟုတ်ခြင်းကို အခြေခံခြင်း၌ {T1} သဘောတရားကို ကံ၏ အကျိုးနှင့်အတူ တွဲ၍ သွားစေလျက် ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်း မဟုတ်ခြင်းနှင့် တူအောင် ပြုရမည်၊ {T2} သဘောတရားကိုလည်း {T3} သဘောတရားနှင့် တွဲ၍ သွားစေလျက် {T4} သဘောတရားကို ပြသရမည်။)  [SK]
- (sahajātavāropi paṭiccavārasadiso kātabbo.) = (အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်ကိုလည်း မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူအောင် ပြုရမည်။)  [SK]
- (avasesesu dvīsu ghaṭanesu pavatti paṭisandhi vitthāretabbā.) = (ကြွင်းသော ပေါင်းစပ်ချက် နှစ်ခုတို့၌ ဘဝ ဖြစ်ဆဲ ကာလနှင့် ပဋိသန္ဓေကို အကျယ် ချဲ့ရမည်။)  [SK]
- (§C§aṃ anumajjantena paccayavāro vitthāretabbo. = ({C1.obj} အစဉ်လိုက် သုံးသပ်လျက် အကြောင်းပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်ကို အကျယ် ချဲ့ရမည်။  [SK]
- yathā paṭiccagaṇanā evaṃ gaṇetabbā. = မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်၏ ရေတွက်ချက်အတိုင်း ထိုနည်းတူ ရေတွက်ရမည်။  [SK]
- §K§, purejāte ca āsevane ca ekavīsa, ayaṃ ettha viseso.) = {K1}၊ ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်းဟူသော အကြောင်း၌လည်းကောင်း၊ အလေ့အကျင့် ပြုခြင်းဟူသော အကြောင်း၌လည်းကောင်း နှစ်ဆယ့်တစ်ခု၊ ဤနေရာ၌ ဤသည်မှာ ထူးခြားချက် ဖြစ်သည်။)  [SK]
- paccanīye = အငြင်းပြ ပုံစံ၌  [SK]
- §K§ pañhā, sattasu ṭhānesu satta mohā uddharitabbā mūlapadesuyeva. = (frame)  [SK]
- §K§ cittasamuṭṭhānā uddharitabbā. = (frame)  [SK]
- §T§amūlakā satta pañhā naadhipatiyā kātabbā. = {T1} သဘောတရားကို အခြေခံသော ပြဿနာ ခုနစ်ခုကို အကြီးအမှူးဟူသော အကြောင်း မဟုတ်ခြင်း၌ ပြုရမည်။  [SK]
- (§T§amūlakā sattapi pañhā paripuṇṇā.) = ({T1} သဘောတရားကို အခြေခံသော ပြဿနာ ခုနစ်ခုလုံးလည်း ပြည့်စုံကြသည်။)  [SK]
- (§T§amūlakā pañca pañhā kātabbā, vipākanti niyāmetabbā.) = ({T1} သဘောတရားကို အခြေခံသော ပြဿနာ ငါးခု ပြုရမည်၊ ကံ၏ အကျိုးဟု သတ်မှတ်ရမည်။)  [SK]
- (§T§amūlakā iminā kāraṇena satta pañhā vibhajitabbā.) = ({T1} သဘောတရားကို အခြေခံသော ပြဿနာ ခုနစ်ခုကို ဤနည်းလမ်းဖြင့် ခွဲခြမ်းစိတ်ဖြာရမည်။)  [SK]
- (§T§amūlakā satta pañhā iminā kāraṇena vibhajitabbā.) = ({T1} သဘောတရားကို အခြေခံသော ပြဿနာ ခုနစ်ခုကို ဤနည်းလမ်းဖြင့် ခွဲခြမ်းစိတ်ဖြာရမည်။)  [SK]
- (§T§amūlakā iminā kāraṇena pañca pañhā vibhajitabbā.) = ({T1} သဘောတရားကို အခြေခံသော ပြဿနာ ငါးခုကို ဤနည်းလမ်းဖြင့် ခွဲခြမ်းစိတ်ဖြာရမည်။)  [SK]
- (§T§amūlakā pañca pañhā iminā kāraṇena vibhajitabbā.) = ({T1} သဘောတရားကို အခြေခံသော ပြဿနာ ငါးခုကို ဤနည်းလမ်းဖြင့် ခွဲခြမ်းစိတ်ဖြာရမည်။)  [SK]
- (§T§amūlake avasesā pañhā sahajātapaccayasadisā.) = ({T1} သဘောတရားကို အခြေခံခြင်း၌ ကြွင်းသော ပြဿနာတို့သည် အတူ ပေါ်ပေါက်ခြင်းဟူသော အကြောင်းနှင့် တူကြသည်။)  [SK]
- (§T§amūlakā pañca pañhā. = ({T1} သဘောတရားကို အခြေခံသော ပြဿနာ ငါးခု။  [SK]
- (paṭhamaghaṭanāyaṃ sampuṇṇā satta pañhā kātabbā.) = (ပထမ ပေါင်းစပ်ချက်၌ အပြည့်အစုံ ဖြစ်သော ပြဿနာ ခုနစ်ခု ပြုရမည်။)  [SK]
- (paṭisandhikkhaṇe pañca pañhā kātabbā. = (ပဋိသန္ဓေ နေသော ခဏ၌ ပြဿနာ ငါးခု ပြုရမည်။  [SK]
- yattha §T§aṃ āgacchati tattha §T§aṃ kātabbaṃ. = အကြင်နေရာ၌ {T1} သဘောတရား ပါဝင်လာ၏ ထိုနေရာ၌ {T2} သဘောတရားအဖြစ် ပြုရမည်။  [SK]
- yattha §T§opi āgacchati, tattha §T§ā kātabbā. = အကြင်နေရာ၌ {T1} သဘောတရားသည်လည်း ပါဝင်လာ၏၊ ထိုနေရာ၌ {T2} သဘောတရားများအဖြစ် ပြုရမည်။  [SK]
- naadhipatimūlake sattatiṃsa pañhā kātabbā.) = အကြီးအမှူးဟူသော အကြောင်း မဟုတ်ခြင်းကို အခြေခံခြင်း၌ ပြဿနာ သုံးဆယ့်ခုနစ်ခု ပြုရမည်။)  [SK]
- naanantarampi §V§ nasamanantarampi naaññamaññampi naupanissayampi satta pañhā rūpaṃyeva. = ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းဟူသော အကြောင်း မဟုတ်ခြင်း၌လည်း {V1}၊ ကောင်းစွာ ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းဟူသော အကြောင်း မဟုတ်ခြင်း၌လည်း၊ အချင်းချင်း ထောက်ပံ့ခြင်းဟူသော အကြောင်း မဟုတ်ခြင်း၌လည်း၊ အားကြီးသော အမှီဟူသော အကြောင်း မဟုတ်ခြင်း၌လည်း ပြဿနာ ခုနစ်ခု၊ ရုပ်သာ ဖြစ်သည်။  [SK]
- §K§ paṭiccavārapaccanīyasadisaṃ. = {K1}သည် မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်၏ အငြင်းပြ ပုံစံနှင့် တူသည်။  [SK]
- §K§, naāsevanepi sadisaṃ. = {K1}၊ အလေ့အကျင့် ပြုခြင်းဟူသော အကြောင်း မဟုတ်ခြင်း၌လည်း တူသည်။  [SK]
- (§K§ pañhā kātabbā. = (frame)  [SK]
- §C§ā §C§ā §C§ā §C§ā §C§ā §C§ā §C§ā §C§ā vitthāretabbā.) = (frame)  [SK]
- (nissayampi ninnānaṃ) = (အမှီဟူသော အကြောင်းသည်လည်း ကွဲပြားခြင်း မရှိ)  [SK]
- (§C§aṃ anumajjantena sabbe paccayā vitthāretabbā). = ({C1.obj} အစဉ်လိုက် သုံးသပ်လျက် အကြောင်း အားလုံးကို အကျယ် ချဲ့ရမည်)။  [SK]
- (paccanīyaṃ kātabbaṃ asammohantena.) = (အငြင်းပြ ပုံစံကို မရောထွေးစေဘဲ ပြုရမည်။)  [SK]
- avasesā sahajātapaccayasadisā.) = ကြွင်းသည်တို့သည် အတူ ပေါ်ပေါက်ခြင်းဟူသော အကြောင်းနှင့် တူကြသည်။)  [SK]
- (natthipaccayañca vigatapaccayañca anantarasadisaṃ, avigataṃ atthisadisaṃ.) = (မရှိခြင်းဟူသော အကြောင်းလည်းကောင်း၊ ပျောက်ကွယ်ခြင်းဟူသော အကြောင်းလည်းကောင်း ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းနှင့် တူသည်၊ မပျောက်ကွယ်ခြင်းသည် ရှိခြင်းနှင့် တူသည်။)  [SK]
- (ghaṭanā kusalattikasadisāyeva. = (ပေါင်းစပ်ချက်များသည် ကုသိုလ် သုံးမျိုးတွဲနှင့်ပင် တူကြသည်။  [SK]
- pañhāvāragaṇanaṃ evaṃ asammohantena gaṇetabbaṃ.) = ပြဿနာအလိုက် ဖော်ပြချက်၏ ရေတွက်ချက်ကို ဤသို့ မရောထွေးစေဘဲ ရေတွက်ရမည်။)  [SK]
- paccanīyuddhāro. = အငြင်းပြ ပုံစံအတွက် ထုတ်နုတ်ချက်။  [SK]
- (paccanīyaṃ gaṇentena imāni padāni anumajjantena gaṇetabbāni.) = (အငြင်းပြ ပုံစံကို ရေတွက်သောအခါ ဤ ပုဒ်တို့ကို အစဉ်လိုက် သုံးသပ်လျက် ရေတွက်ရမည်။)  [SK]
- (anulomapaccanīyagaṇanā iminā kāraṇena gaṇetabbā.) = (အဟုတ်ပြ အငြင်းပြ ပုံစံ၏ ရေတွက်ချက်ကို ဤနည်းလမ်းဖြင့် ရေတွက်ရမည်။)  [SK]
- (paccanīyānulomaṃ iminā kāraṇena vibhajitabbaṃ.) = (အငြင်းပြ အဟုတ်ပြ ပုံစံကို ဤနည်းလမ်းဖြင့် ခွဲခြမ်းစိတ်ဖြာရမည်။)  [SK]
- (evaṃ anulomagaṇanā gaṇetabbā.) = (ဤသို့ အဟုတ်ပြ ပုံစံ၏ ရေတွက်ချက်ကို ရေတွက်ရမည်။)  [SK]
- (iminā kāraṇena dasa pañhā vitthāretabbā.) = (ဤနည်းလမ်းဖြင့် ပြဿနာ ဆယ်ခုကို အကျယ် ချဲ့ရမည်။)  [SK]
- (§C§ā nahetupaccayasadisaṃ. = ({C1.ab} အမြစ်ဟူသော အကြောင်း မဟုတ်ခြင်းနှင့် တူသည်။  [SK]
- moho natthi. = မောဟ မရှိ။  [SK]
- §C§ā paripuṇṇaṃ arūpapañhameva.) = {C1.ab} ရုပ် မဟုတ်သော သဘောတရားဆိုင်ရာ ပြဿနာသာ ပြည့်စုံသည်။)  [SK]
- (anulomapaccanīyaṃ vitthārena gaṇetabbaṃ.) = (အဟုတ်ပြ အငြင်းပြ ပုံစံကို အကျယ်အားဖြင့် ရေတွက်ရမည်။)  [SK]
- (sahajātavāropi paccayavāropi nissayavāropi saṃsaṭṭhavāropi sampayuttavāropi paṭiccavārasadisā.) = (အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်လည်း၊ အကြောင်းပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်လည်း၊ အမှီပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်လည်း၊ ရောနှောခြင်းအလိုက် ဖော်ပြချက်လည်း၊ ယှဉ်တွဲခြင်းအလိုက် ဖော်ပြချက်လည်း မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် တူကြသည်။)  [SK]
- (iminā kāraṇena sabbesaṃ padānaṃ paccayoti dīpetabbo). = (ဤနည်းလမ်းဖြင့် ပုဒ် အားလုံးတို့အား အကြောင်း ဖြစ်သည်ဟု ဖော်ပြရမည်)။  [SK]
- (tāniyeva ca gamanāni niyāmetabbāni.) = (ထို သွားပုံများကိုပင်လည်း သတ်မှတ်ရမည်။)  [SK]
- pītinayaṃ passitvā kātabbaṃ). = ပီတိ နည်းကို ကြည့်၍ ပြုရမည်)။  [SK]
- (yathā paṭiccavāre hetupaccaye evaṃ vitthāretabbā dasa pañhā.) = (မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်၌ အမြစ်ဟူသော အကြောင်း၌ ပြုသကဲ့သို့ ထိုနည်းတူ ပြဿနာ ဆယ်ခုကို အကျယ် ချဲ့ရမည်။)  [SK]
- (kusalattikaṃ anulomaṃ anumajjantena gaṇetabbaṃ.) = (ကုသိုလ် သုံးမျိုးတွဲ၏ အဟုတ်ပြ ပုံစံကို အစဉ်လိုက် သုံးသပ်လျက် ရေတွက်ရမည်။)  [SK]
- (paccanīyaṃ anumajjantena gaṇetabbaṃ.) = (အငြင်းပြ ပုံစံကို အစဉ်လိုက် သုံးသပ်လျက် ရေတွက်ရမည်။)  [SK]
- (anulomapaccanīyaṃ anumajjantena gaṇetabbaṃ.) = (အဟုတ်ပြ အငြင်းပြ ပုံစံကို အစဉ်လိုက် သုံးသပ်လျက် ရေတွက်ရမည်။)  [SK]
- (paccanīyānulomaṃ anumajjantena gaṇetabbaṃ.) = (အငြင်းပြ အဟုတ်ပြ ပုံစံကို အစဉ်လိုက် သုံးသပ်လျက် ရေတွက်ရမည်။)  [SK]
- dve khandhe ca = အစုအဝေး နှစ်ပါးကိုလည်းကောင်း  [SKF]
- (paripuṇṇaṃ, paṭisandhi natthi) = (ပြည့်စုံသည်၊ ပဋိသန္ဓေ မရှိ)  [SKF]
- ekavīsa = နှစ်ဆယ့်တစ်ခု  [COUNT]
- pañcavīsa = နှစ်ဆယ့်ငါးခု  [COUNT]
- chabbīsa = နှစ်ဆယ့်ခြောက်ခု  [COUNT]
- sattavīsa = နှစ်ဆယ့်ခုနစ်ခု  [COUNT]
- aṭṭhavīsa = နှစ်ဆယ့်ရှစ်ခု  [COUNT]
- ekūnatiṃsa = နှစ်ဆယ့်ကိုးခု  [COUNT]
- tiṃsa = သုံးဆယ်ခု  [COUNT]
- ekatiṃsa = သုံးဆယ့်တစ်ခု  [COUNT]
- dvattiṃsa = သုံးဆယ့်နှစ်ခု  [COUNT]
- tettiṃsa = သုံးဆယ့်သုံးခု  [COUNT]
- catuttiṃsa = သုံးဆယ့်လေးခု  [COUNT]
- pañcatiṃsa = သုံးဆယ့်ငါးခု  [COUNT]
- chattiṃsa = သုံးဆယ့်ခြောက်ခု  [COUNT]
- sattatiṃsa = သုံးဆယ့်ခုနစ်ခု  [COUNT]
- bāvīsa = နှစ်ဆယ့်နှစ်ခု  [COUNT]
- Vitakkattikaṃ = စတင်ကြံစည်မှု သုံးမျိုးတွဲ  [TIKA_NAME]
- Pītittikaṃ = ပီတိ သုံးမျိုးတွဲ  [TIKA_NAME]
- sabbattha = နေရာတိုင်း၌  [NEW]
- sabbe (before a count) = အားလုံး  [NEW]
- Pītittikaṃ = ပီတိ သုံးမျိုးတွဲ  [NEW]
- kātabbaṃ / -ā / -o / -āni = ပြုရမည်  [NEW]
- anumajjantena = အစဉ်လိုက် သုံးသပ်လျက်  [NEW]
- niyāmetabbaṃ / -ā = သတ်မှတ်ရမည်  [NEW]
- uddharitabbā = ထုတ်နုတ်ရမည်  [NEW]
- dīpetabbo / -ā = ဖော်ပြရမည်  [NEW]
- dassetabbo = ပြသရမည်  [NEW]
- passitvā = ကြည့်၍  [NEW]
- sampuṇṇā = အပြည့်အစုံ ဖြစ်သော  [NEW]
- -sadisā (plural) = နှင့် တူကြသည်  [NEW]
- -sadisaṃ kātabbaṃ / -sadiso kātabbo = နှင့် တူအောင် ပြုရမည်  [NEW]
- avasesa- (attributive) = ကြွင်းသော  [NEW]
- iminā kāraṇena = ဤနည်းလမ်းဖြင့်  [NEW]
- viseso = ထူးခြားချက်  [NEW]
- pavatti / pavatte = ဘဝ ဖြစ်ဆဲ ကာလ  [NEW]
- udāharaṇa = ဥပမာ  [NEW]
- tattha = ထိုနေရာ  [NEW]
- āgacchati = ပါဝင်လာ၏  [NEW]
- naya = နည်း  [NEW]
- (Dutiyo bhāgo) = (ဒုတိယ အပိုင်း)  [NEW]
- tathā (after yathā) = ထို့အတူ  [NEW]
- evaṃ (thus) = ဤသို့  [NEW]
- -mūlakā (attributive) = ကို အခြေခံသော  [NEW]
- gacchantena (with saha / X-) = တွဲ၍ သွားစေလျက်  [NEW]
- gaṇentena = ရေတွက်သောအခါ  [NEW]
- gamanāni = သွားပုံ  [NEW]
