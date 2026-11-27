"""Consistency pass (pi-5 Burmese, Kathāvatthu): every item of harmonise-todo.md, before vs now.
For each item the lines whose Pāli matches `pali` are taken (an item is counted only where the Pāli line has it); in
their Burmese the uses of the chosen form and of every other form are counted, in the chapter files before the pass
(harmonise-backup/chapters/) and now. An item fails if an other form is left now, or if a line that has the Pāli item
lacks the chosen form now. Model: pi-4-my/harmonise_scan.py (read only).
usage: python3 -I -X utf8 harmonise_scan.py [--table]   (--table also writes harmonise-table.tsv:
       Pāli<TAB>chosen Burmese<TAB>other forms (uses before)<TAB>chapters with an other form before)"""
import pathlib
import re
import sys

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import my5_formulas as F  # noqa: E402

ROOT = HERE.parents[3]
PD = ROOT / "AI_translation/pali/pi-5_split_chapters"
NOW = ROOT / "AI_translation/burmese/pi-5-burmese-plain-zeroshot_split_chapters"
BEFORE = HERE / "harmonise-backup/chapters"
E = re.escape
Q = '"'
ORD18 = "|".join(E(F.ORD_MY[n]) for n in range(18, 24))

# (item, Pāli label for the table, Pāli regex on the line, chosen Burmese (regex), [other forms (regex)], kind)
# kind: A = source as written, B = term / frame drift, R = rule kept (verified, nothing to change)
ITEMS = [
    # ---- Part A
    ("A1 ^5-332 (no quote in the Pāli)", "Saññāsamuṭṭhānā vācā vuttā bhagavatā – tatiyaṃ jhānaṃ…",
     r"Saññāsamuṭṭhānā vācā vuttā bhagavatā – tatiyaṃ", r"ဟောတော်မူသလော – တတိယ", [r"ဟောတော်မူသလော – “တတိယ"], "A"),
    ("A1 ^5-407 (unquoted «sotāpannoti vattabbo»)", "… samannāgato sotāpannoti / sakadāgāmīti / anāgāmīti vattabbo",
     r"samannāgato (?:sotāpanno|sakadāgāmī|anāgāmī)ti vattabbo", r"ပြည့်စုံသူကို (?:သောတာပန်|သကဒါဂါမ်|အနာဂါမ်)ဟု",
     [r"ပြည့်စုံသူကို “"], "A"),
    ("A1 ch17 ^5-556 (unquoted «sānusayoti / sarāgoti vattabbo»)", "Puthujjano kusalābyākate citte vattamāne sānusayoti …",
     r"vattamāne (?:sānusayo|sarāgo)ti vattabbo", r"ပုထုဇဉ်ကို (?:ကိန်းအောင်းခြင်း|ရာဂ) ရှိသူဟု", [r"ပုထုဇဉ်ကို “"], "A"),
    ("A1 ch17 ^5-558 (unquoted «ñāṇīti / paññavāti vattabbo»)", "Arahā cakkhuviññāṇasamaṅgī ñāṇīti / paññavāti vattabbo",
     r"cakkhuviññāṇasamaṅgī (?:ñāṇī|paññavā)ti vattabbo", r"ရဟန္တာကို (?:ဉာဏ်|ပညာ) ရှိသူဟု", [r"ရဟန္တာကို “"], "A"),
    ("A1 ^5-514 verse line opening «"+Q+"» = «“» (one rule in line_my)", '"Saṅkapparāgo purisassa kāmo,',
     r'^"Saṅkapparāgo purisassa kāmo', r"^“ယောကျ်ား၏", [], "R"),
    ("A1 «Na vattabbaṃ – P-ti?» without quotes (^5-445, ^5-465, ^5-475, ^5-853, ^5-885 …)", "Na vattabbaṃ – P-ti? (no marks)",
     r"Na vattabbaṃ – (?:pathavīkasiṇaṃ samāpattiṃ|tejodhātu|cetasiko dhammo dāna|patti asaṅkhatā|rūpaṃ rūpaṭṭhena)",
     r"ဤသို့ မဆိုသင့်သလော – [^“]", [r"ဤသို့ မဆိုသင့်သလော – “(?:မြေ ကသိုဏ်း|မီးဓာတ်|စိတ်၏ အဖော်|ရရှိခြင်း|ရုပ်သည် ရုပ်၏)"], "A"),
    ("A1 asmimāna «ငါဟူသော» (no quote pair added)", "Asmimānassa yo vinayo",
     r"Asmimānassa yo vinayo", r"ငါဟူသော မာန", [r"‘ငါ’ဟူသော"], "A"),
    ("A2 the sample's regular “…” / ‘…’ nesting kept; stanzas keep their own marks", "(quote nesting)", r"‘", r"‘", [], "R"),
    ("A3 Nirāmagandhā (no added «ကိလေသာ»)", "Nirāmagandhā karuṇedhimuttā", r"Nirāmagandhā", r"အပုပ်နံ့ ကင်းကြ",
     [r"ကိလေသာ အပုပ်နံ့"], "A"),
    ("A3 «Nanu "+Q+"paṭhamaṃ jhānaṃ … niruddhā hotī"+Q+"ti!» (no verb supplied)",
     'Nanu "paṭhamaṃ jhānaṃ samāpannassa vācā niruddhā hotī"ti!', r'Nanu "paṭhamaṃ jhānaṃ samāpannassa vācā',
     r"ချုပ်ငြိမ်းသွားသည်” မဟုတ်လော", [r"ဟူ၍ ဟောထားသည် မဟုတ်လော"], "A"),
    ("A3 «Atītaṃ khandhā» (the copula that a Burmese nominal question needs: kept)", "Atītaṃ khandhāti?",
     r"^Atītaṃ khandhāti\?", r"အတိတ်သည် အစုအဝေးတို့ ဖြစ်သလော", [], "R"),
    ("A3 «… nuppajjissatīti katvā pahīnaṃ» (no added «ထိုအရာကို»)", "… nuppajjissatīti katvā pahīnaṃ",
     r"nuppajjissatīti katvā pahīn", r"အကြောင်းပြု၍ ပယ်ပြီး ဖြစ်", [r"အကြောင်းပြု၍ ထိုအရာကို"], "A"),
    ("A3 sammukhībhūta (no added «နှောင်ကြိုးနှင့်»)", "sammukhībhūto", r"[Ss]ammukhībhūt", r"မျက်နှာချင်းဆိုင် ဖြစ်နေသူ",
     [r"နှောင်ကြိုးနှင့် မျက်နှာချင်းဆိုင်"], "A"),
    ("A4 ^5-43 (no comma before «cakkhāyatanañca»)", "… saccikaṭṭhaparamatthena cakkhāyatanañca …",
     r"saccikaṭṭhaparamatthena cakkhāyatanañca", r"တွေ့ရ၍ မျက်စိ", [r"တွေ့ရသည်၊ မျက်စိ"], "A"),
    ("A4 ^5-274 (no comma «… samannāgato ekadesaṃ …»)", "ariyakantehi sīlehi samannāgato ekadesaṃ …",
     r"sīlehi samannāgato ekadesaṃ", r"ပြည့်စုံ၍ တစ်စိတ်တစ်ဒေသ", [r"ပြည့်စုံ၏၊ တစ်စိတ်တစ်ဒေသ"], "A"),
    ("A4 ^5-292 (no comma «… atthi puthujjano tena …»)", "atītaṃ anottappaṃ atthi puthujjano tena …",
     r"anottappaṃ atthi puthujjano tena", r"မကြောက်ရွံ့မှု ရှိ၍ ပုထုဇဉ်သည်", [r"မကြောက်ရွံ့မှု ရှိသည်၊ ပုထုဇဉ်သည်"], "A"),
    ("A4 «X kusalampi akusalampi» (no comma: no «၊»)", "rūpaṃ / kāyakammaṃ vacīkammaṃ kusalampi akusalampi",
     r"kusalampi akusalampi", r"ကုသိုလ်လည်း ဖြစ် အကုသိုလ်လည်း", [r"ကုသိုလ်လည်း ဖြစ်၏၊ အကုသိုလ်လည်း"], "A"),
    ("A4 ^5-306 «Paṭhamavaggo» (no full stop: none added)", "Paṭhamavaggo", r"^Paṭhamavaggo$", r"^ပထမ ဝဂ်$",
     [r"^ပထမ ဝဂ်။"], "A"),
    ("A4 ^5-116 / ^5-164 / ^5-323 / ^5-379 / ^5-456 / ^5-509 (missing dash / …pe… / quotes: as written)", "(source slips)",
     r"tena vata re vattabbe \"cattāro|Na vattabbaṃ atthi antarābhavoti", r"ဆိုသင့်|မဆိုသင့်", [], "R"),
    # ---- B1
    ("B1 vagga ordinals 18-23 = the Pāli ordinals (pi-3 naya names)", "Aṭṭhārasamavaggo … Tevīsatimavaggo",
     r"(?:Aṭṭhārasama|Ekūnavīsatima|Vīsatima|Ekavīsatima|Bāvīsatima|Tevīsatima)vaggo",
     rf"(?:{ORD18}) {F.VAGGA_W}", [r"ခုမြောက် ဝဂ်"], "B"),
    ("B1 vagga ordinals 1-17 (Pāli ordinals, unchanged)", "Paṭhama … Sattarasamavaggo",
     r"^(?:#+ )?(?:Dutiya|Tatiya|Catuttha|Pañcama|Chaṭṭha|Sattama|Aṭṭhama|Navama|Dasama|Ekādasama|Dvādasama|Terasama|"
     r"Cuddasama|Pannarasama|Soḷasama|Sattarasama)vaggo",
     r"(?:ဒုတိယ|တတိယ|စတုတ္ထ|ပဉ္စမ|ဆဋ္ဌမ|သတ္တမ|အဋ္ဌမ|နဝမ|ဒသမ|ဧကာဒသမ|ဒွါဒသမ|တေရသမ|စုဒ္ဒသမ|ပန္နရသမ|သောဠသမ|သတ္တရသမ) ဝဂ်",
     [], "R"),
    # ---- B2
    ("B2 aveccappasāda", "buddhe aveccappasādena", r"aveccappasād", E(F.AVECCA), [r"မတုန်မလှုပ်သော ကြည်ညိုမှု"], "B"),
    ("B2 aṇusahagata", "aṇusahagata kāmarāga / byāpāda", r"aṇusahagat", E(F.ANUSAHA),
     [r"သိမ်မွေ့သော (?:ကာမရာဂ|ဖျက်ဆီးလိုစိတ်)"], "B"),
    ("B2 ucchinnamūla … anuppādadhamma", "ucchinnamūlo tālāvatthukato anabhāvaṅkato āyatiṃ anuppādadhammo",
     r"ucchinnamūl", r"အမြစ်ပြတ်စေပြီး", [r"ထန်းငုတ်ကဲ့သို့ ပြုထားပြီး"], "B"),
    ("B2 bodhagāmī", "bodhagāmī", r"bodhagām", r"ထိုးထွင်း သိခြင်းဆီသို့", [r"ဗောဓိဆီသို့"], "B"),
    ("B2 rūparāga / arūparāga (pi-2 ^2-U49)", "rūparāgaṃ, arūparāgaṃ", r"[Rr]ūparāg",
     r"(?:သိမ်မွေ့သော ရုပ်|ရုပ်မရှိသော )ဘဝကို တပ်မက်သော ရာဂ", [r"ရုပ်၌ တပ်မက်မှု", r"ရုပ်မဲ့၌"], "B"),
    ("B2 dukkhanirodhagāminī paṭipadā (pi-2 ^2-189)", "dukkhanirodhagāminī paṭipadā", r"dukkhanirodhagāmin",
     r"ချုပ်ငြိမ်းရာသို့ ရောက်စေသော ကျင့်စဉ်", [r"ချုပ်ငြိမ်းခြင်းသို့ ရောက်ကြောင်း အကျင့်"], "B"),
    ("B2 «dibbena cakkhunā rūpaṃ passati» (rūpa seen = «အဆင်းအရောင်», pi-2 ^2-517; the sample changes)",
     "dibbena cakkhunā (…) rūpaṃ passati", r"dibbena cakkhunā (?:visuddhena atikkantamānusakena )?rūpaṃ passati",
     r"နတ်မျက်စိဖြင့် အဆင်းအရောင်ကို", [r"နတ်မျက်စိဖြင့် ရုပ်ကို"], "B"),
    ("B2 jahati «စွန့်ပယ်» (kept apart from pajahati «ပယ်»)", "kiṃ jahati / … catubhāgaṃ jahati",
     r"(?:kiṃ|catubhāgaṃ) jahatī", r"စွန့်ပယ်", [r"အဘယ်ကို ပယ်", r"လေးပုံတစ်ပုံ ပယ်သည်"], "B"),
    ("B2 sāmaññaphala (pi-2 ^2-818)", "sāmaññaphala", r"sāmaññaphal", E(F.SAMANNAPHALA), [r"ရဟန်း၏ အကျိုး"], "B"),
    ("B2 (gandhaṃ) ghāyati (pi-1 ^1-1352 / pi-2 ^2-517)", "ghāyati", r"\bghāyati|gandhaṃ ghāy", E(F.GHAYATI),
     [r"အနံ့ ခံ", r"အနံ့ကို ခံ", r"အနံ့ကိုလည်း ခံ"], "B"),
    ("B2 (rasaṃ) sāyati (pi-1 ^1-1352 / pi-2 ^2-517)", "sāyati", r"\bsāyati|rasaṃ sāy", E(F.SAYATI),
     [r"အရသာ ခံ", r"အရသာကို ခံ", r"အရသာကိုလည်း ခံ"], "B"),
    ("B2 kameyya", "visaṃ kameyya, satthaṃ kameyya, aggi kameyya", r"visaṃ (?:na )?kameyya", r"ထိရောက်နိုင်",
     [r"တိုးဝင်ရာ"], "B"),
    ("B2 paṇṇāsaka «ငါးဆယ်အစု»", "Mahāpaṇṇāsako / Dutiyo … Catuttho paṇṇāsako", r"[Pp]aṇṇāsako\.",
     r"ငါးဆယ်(?:တစ်ဝက်)?အစု", [], "R"),
    ("B2 Saṅgaha (the paṇṇāsaka uddāna, ^5-604) = the ch15 heading", "Niyāmasaṅgahagatānisaṃsatā …",
     r"Niyāmasaṅgahagatānisaṃsatā", E(F.KATHA_NAME["saṅgaha"]), [r"စုစည်းခြင်း"], "B"),
    ("B2 Suttasādhanaṃ heading (ch5 / ch6 the same)", "Suttasādhanaṃ", r"^#+ Suttasādhanaṃ",
     r"သုတ္တန်ဖြင့် သက်သေပြခြင်း", [], "R"),
    ("B2 the vagga-1 uddāna = the kathā headings", "brahmacariyavāso odhiso / sabbatthivādo",
     r"brahmacariyavāso odhiso|sabbatthivādo", r"မြင့်မြတ်သော အကျင့်ကို ကျင့်သုံးခြင်း|အရာအားလုံး ရှိသည်ဟူသော ဝါဒ",
     [r"မြတ်သော အကျင့်ကို ကျင့်ခြင်း", r"အပိုင်းအခြားအားဖြင့်", r"၊ အားလုံး ရှိသည်ဟူသော"], "B"),
    ("B2 the paṇṇāsaka uddānas = the kathā headings (niggaho, puññasañcayo, Mahā, vavatthitā)",
     "Niggaho, puññasañcayo … / Mahāniyāmo … / … mūlañca vavatthitā", r"^Niggaho, puññasañcayo|^Mahāniyāmo|mūlañca vavatthitā",
     E(F.KATHA_NAME["niggaha"]) + "|" + E(F.KATHA_NAME["vavatthitā"]),
     [r"ချေပချက်၊", r"ကုသိုလ် စုဆောင်းခြင်း", r"ကြီးမြတ်သော အစု", r"ပိုင်းခြား သတ်မှတ်ခြင်း"], "B"),
    # ---- B3
    ("B3 ovāda / anusāsanī (natural words; «ဆုံးမ» in every checker's non-negation list)", "ovādo … anusāsanī",
     r"ovād|Ovād", E(F.OVADA) + r"|ဆုံးမ စကား", [r"ဩဝါဒ", r"အနုသာသနီ"], "B"),
    ("B3 pāpakamma = the sample's «ယုတ်မာသော ကံ»", "pāpakammaṃ", r"pāpakamm", E(F.PAPAKAMMA), [r"ဆိုးညစ်သော ကံ"], "B"),
    ("B3 avipāka «အကျိုး မရှိသော» (was avoided for the existence checker)", "avipāka", r"\bavipāk",
     E(F.AVIPAKA), [r"အကျိုး မပေးသော"], "B"),
    ("B3 gūtha / mutta «ကျင်ကြီး / ကျင်ငယ်» (natural; kept)", "uccārapassāva / gūtha", r"uccārapassāv",
     r"ကျင်ကြီး", [], "R"),
    # ---- B4
    ("B4 paṭipannaka = pi-4 «ကျင့်ကြံသူ» (apart from sekha «ကျင့်ကြံဆဲသူ»)", "paṭipannako", r"paṭipannak",
     E(F.PATIPANNAKA), [r"ကျင့်ကြံဆဲသူ"], "B"),
    ("B4 sekha «ကျင့်ကြံဆဲသူ» (pi-1)", "sekhassa", r"\bsekhassa", r"ကျင့်ကြံဆဲသူ", [], "R"),
    ("B4 saṅgahita «အကျုံးဝင်» / the ^5-472 simile «စုစည်းထား» (tied together: a sense difference, kept)",
     "goṇā dāmena saṅgahitā …", r"dāmena|yottena", r"စုစည်းထား", [], "R"),
    ("B4 bandhana «အနှောင်အဖွဲ့» (kept apart from saṃyojana «နှောင်ကြိုး»)", "addubandhanena bandhituṃ …",
     r"addubandhanena", r"အနှောင်အဖွဲ့ဖြင့် နှောင်ဖွဲ့ခြင်း", [r"အနှောင်ဖြင့်", r"ချည်နှောင်ရန်"], "B"),
    # ---- B5
    ("B5 «"+Q+"P"+Q+"ti – (n)attheva suttanto» = «“P”ဟု – ထိုသို့သော သုတ္တန် …»", '"P"ti – attheva suttanto',
     r'ti(?: \[[^\]]*\])? – n?attheva suttanto', r"”(?: \[[^\]]*\])?ဟု – ထိုသို့သော",
     [r"” – (?:ထိုသို့|ဤသို့)သော", r"ဤသို့သော သုတ္တန်", r"”ဟူ၍ – ထိုသို့သော"], "B"),
    ("B5 the closing «ti» of a quotation before the reference = «”» (sample)", '…"ti [ref].',
     r'"ti \[(?:[a-zāīūṃ]+\. )+[^\]]*\](?:\.|!| Attheva|$)',
     r"” \[|” မဟုတ်လော \[", [r"”ဟူ၍ \[(?!“ဒီဃနိကာယ်” 2\.91|“အင်္ဂုတ္တရနိကာယ်” 4\.21|“ဒီဃနိကာယ်” 2\.180)"], "B"),
    ("B5 «… ti – atthi adhippāyaiddhi» = «ဟု –»", '"P"ti – atthi adhippāyaiddhi', r"ti – atthi adhippāya",
     r"”?ဟု – ", [r"”ဟူ၍ – "], "B"),
    ("B5 «Nanu āyasmā sāriputto etadavoca –» = ch11 «… ဤသို့ ပြောခဲ့သည် မဟုတ်လော –»", "Nanu āyasmā sāriputto etadavoca",
     r"Nanu āyasmā sāriputto etadavoca", r"ဤသို့ ပြောခဲ့သည် မဟုတ်လော –", [r"ဤသို့ ဆိုခဲ့သည် မဟုတ်လော"], "B"),
    ("B5 «X-ti katvā P-ti?» = «Xဟု အကြောင်းပြု၍ Pသလော» (sample KATVA)", "X-ti katvā P-ti?", r"(?<!Ayogan)ti katvā",
     E(F.KATVA), [], "R"),
    # ---- B6
    ("B6 the āvaṭṭanā list (ch15)", "āvaṭṭanā … paṇidhi", r"paṇidhī?ti\?|paṇidhi,", E(F.AVATTANA[-1]),
     [r"ဆုတောင်းမှု", r"စိတ်ကို ထားရှိခြင်း", r"စိတ် ဦးတည်ထားခြင်း"], "B"),
    ("B6 «atthi / natthi tassa (tāya) āvaṭṭanā» = «ထိုအရာ၌ …»", "atthi tassa / tāya āvaṭṭanā",
     r"(?:atthi|natthi) (?:tassa|tāya) āvaṭṭanā", r"ထိုအရာ၌ စိတ်ကို လှည့်ဆောင်ခြင်း", [r"ထိုအရာ၏ စိတ်ကို", r"ထိုဓာတ်၌"], "B"),
    ("B6 (s)ārammaṇa as predicate = «အာရုံ (မ)ရှိသော အရာ (ဖြစ်)»", "X sārammaṇo / anārammaṇo",
     r"\b(?:sārammaṇ|anārammaṇ)(?:o|aṃ|ā)(?:ti|nti)?\b", r"အာရုံ (?:မ)?ရှိသော",
     [r"ထိုအရာသည် အာရုံ (?:မ)?ရှိ(?:သည်|သလော|၊)", r"သည် အာရုံ ရှိသလော"], "B"),
    ("B6 «kāyena phusitvā viharati» (pi-4 ^4-1)", "kāyena phusitvā viharati", r"kāyena phusitvā viharati",
     E(F.KAYENA), [r"တွေ့ထိ၍ နေ", r"မတွေ့ထိဘဲ နေ"], "B"),
    ("B6 the X-sotāpanno / phalappatto stock passage = ch3", "ekadesaṃ / catubhāgaṃ …ppatto paṭiladdho adhigato …",
     r"ppatto paṭiladdho adhigato sacchikato upasampajja", r"ရောက်ပြီး၊ ရရှိပြီး၊ ပိုင်ဆိုင်ပြီး",
     [r"ရောက်၍ ရ၍ ပြည့်မီ၍"], "B"),
    ("B6 the arahant's epithets = ch2", "ukkhittapaligho … niraggaḷo", r"ukkhittapaligho",
     r"တံခါးကျင်ကို ဖယ်ရှားပြီးသူ", [r"တံခါး ကန့်လန့်", r"တံခါး ဂျက်ကို"], "B"),
    ("B6 the Ratana verse (ch3)", "Sahāvassa dassanasampadāya,", r"Sahāvassa dassanasampadāya",
     r"ထိုသူ၏ အမြင် ပြည့်စုံခြင်းနှင့်", [r"သစ္စာကို မြင်ခြင်း ပြည့်စုံသည်နှင့်"], "B"),
    ("B6 the Dhammapada 239 verse (ch3)", "Anupubbena medhāvī", r"Anupubbena medhāvī",
     E(F.VERSE_ANUPUBBA[0]), [r"အနည်းငယ်၊ ခဏခဏ"], "B"),
    ("B6 «kusalākusalā sāvajjānavajjā hīnapaṇītā kaṇhasukkasappaṭibhāgā» (pi-4 ^4-104)", "kusalākusalā sāvajjānavajjā …",
     r"kusalākusalā sāvajjānavajjā", r"အပြစ် ရှိသော အပြစ် မရှိသော၊ ယုတ်ညံ့သော မွန်မြတ်သော",
     [r"အပြစ် ကင်းသော၊ ယုတ်ညံ့သော မြင့်မြတ်သော"], "B"),
    ("B6 sammukhībhāvaṃ āgacchanti (ch15)", "sammukhībhāvaṃ āgacchanti", r"sammukhībhāvaṃ āgacch",
     E(F.SAMMUKHA[0][:-3]), [r"မျက်မှောက်သို့ ရောက်လာကြ", r"မျက်နှာချင်းဆိုင် ဖြစ်လာကြ"], "B"),
    ("B6 the far-things sutta (a. ni. 4.47; ch15)", "cattārimāni, bhikkhave, suvidūravidūrāni …", r"suvidūravidūr",
     r"ဤအလွန် ဝေးကွာသော အရာ လေးပါးတို့", [r"အလွန် ဝေးကွာသော ဤအရာ", r"သူယုတ်မာတို့မှ", r"မြေကြီး –"], "B"),
    ("B6 «latā viya vaḍḍhati, māluvā viya …» (ch15)", "latā viya … māluvā viya … muñjapuñjo viya", r"māluvā viya",
     r"နွယ်ကြီးကဲ့သို့", [r"မာလုဝါ နွယ်", r"ဖြူဆံမြက် အပုံ"], "B"),
    ("B6 tāṇaṃ leṇaṃ saraṇaṃ parāyaṇaṃ accutaṃ amataṃ (ch10)", "… parāyaṇaṃ accutaṃ amataṃ", r"parāyaṇaṃ accutaṃ amata",
     r"မှီခိုရာ၊ မစုတေသော အရာ၊ အမြိုက်", [r"ဆုံးခန်းတိုင်ရာ", r"မသေသော အရာ"], "B"),
    ("B6 amata «အမြိုက်» (ch10 / ch17)", "amatogadha …", r"amatogadh", r"အမြိုက်", [r"မသေခြင်း"], "B"),
    ("B6 kāyakamma / vacīkamma (ch14 …)", "kāyakammaṃ vacīkammaṃ", r"kāyakammaṃ vacīkammaṃ|yañceva kāyakammaṃ",
     E(F.KAYAKAMMA), [r"ကာယကံ"], "B"),
    ("B6 saphala / savipāka = the sample", "saphalaṃ savipākaṃ / saphalo", r"\bsaphal",
     E(F.SAPHALA), [r"အကျိုး ရှိသော၊ အကျိုး ပေးသော", r"အကျိုး ရှိ၍ ကံ၏ အကျိုး"], "B"),
    ("B6 (kappaṃ) tiṭṭheyya «တည်နေရာ» (ch19)", "atītaṃ kappaṃ tiṭṭheyya", r"kappaṃ tiṭṭheyya",
     r"တည်နေရာ|ပတ်လုံး တည်ခြင်း", [r"တည်ရာ၍", r"ပတ်လုံး တည်ရာ"], "B"),
    ("B6 the saṅghabheda verse (ch21)", "Āpāyiko nerayiko, kappaṭṭho saṅghabhedako;", r"Āpāyiko nerayiko, kappaṭṭho",
     r"“သံဃာကို သင်းခွဲသူသည် အပါယ်သို့ ရောက်သူ", [r"ကမ္ဘာ တစ်ခုလုံး", r"“အပါယ်သို့ ရောက်မည့်"], "B"),
    ("B6 kusalābyākate citte vattamāne (ch19)", "kusalābyākate citte vattamāne", r"kusalābyākate citte vattamāne",
     E(F.KUSALABYAKATE), [r"ကုသိုလ် စိတ် သို့မဟုတ်"], "B"),
    ("B6 «Taṃ kissa hetu?» (pi-2 / pi-4)", "Taṃ kissa hetu?", r"Taṃ kissa hetu", r"ထိုသို့ အဘယ်ကြောင့်နည်း",
     [r"ထိုသို့ ဖြစ်ခြင်းသည် အဘယ်ကြောင့်"], "B"),
    ("B6 «Ratto rāgaṃ jahati, … / Rāgo cittasampayutto, …» (the sample's «P, Q» = «Pသည်၊ Q», ch27)",
     "Ratto rāgaṃ jahati, duṭṭho dosaṃ jahati …", r"Ratto rāgaṃ jahati|Rāgo cittasampayutto, maggo",
     r"စွန့်ပယ်သည်၊ ဒေါသ|ဖြစ်သည်၊ မဂ်သည်", [r"စွန့်ပယ်၍ ဒေါသ", r"အရာ ဖြစ်၍ မဂ်သည်"], "B"),
    ("B6 paggahaniggahupaga chedanabhedanupaga (ch5)", "paggahaniggahupago chedanabhedanupago", r"paggahaniggahupag",
     E(F.PAGGAHA_UPAGA), [r"နှိမ့်ချခြင်းကို ခံနိုင်သော"], "B"),
    # ---- B7
    ("B7 «-ti kathā» headings «…ဟူသော» (attached)", "Sabbamatthītikathā / Ariyantikathā",
     r"Sabbamatthītikathā|Ariyantikathā", r"ရှိသည်ဟူသော|အရိယာဟူသော", [r"ရှိသည် ဟူသော", r"အရိယာ ဟူသော"], "B"),
    ("B7 tatheva in the uddānas = the sample's «ထိုအတိုင်းပင်»", "tatheva (uddāna)",
     r"tatheva kāyakamma|tatheva asaṃvaro|tatheva sattamabhavik", E(F.TATHEVA), [r"ထိုနည်းတူပင်", r"ထို့အတူပင် ကိုယ်ဖြင့်"], "B"),
    ("B7 bhāṇavāra (pi-1 ^1-57)", "Pañcattiṃsabhāṇavāraṃ", r"bhāṇavār", r"ရွတ်ဖတ်ရန် အပိုင်း", [r"ရွတ်ဆိုရန်"], "B"),
    ("B7 the book colophon (pi-1 … pi-4 pattern)", "Kathāvatthupakaraṇaṃ niṭṭhitaṃ.", r"Kathāvatthupakaraṇaṃ niṭṭhitaṃ",
     E(F.BOOK_END), [], "R"),
    ("B7 kathā colophons «“X” ပြီးဆုံးပြီ။» = the heading names", "Xkathā niṭṭhitā.", r"kathā niṭṭhitā\.",
     r"” ပြီးဆုံးပြီ။", [], "R"),
]

ID = re.compile(r"\s*\^[0-9A-Za-z-]+\s*$")


def pairs(md):
    key = lambda p: (int(p.name.split("-")[0]) if p.name[0].isdigit() else 0)
    for p in sorted(PD.glob("*.md"), key=key):
        ch = p.name.split("-")[0].split(".")[0]
        a = [ID.sub("", l) for l in p.read_text(encoding="utf-8-sig").splitlines() if l.strip()]
        b = [ID.sub("", l) for l in (md / p.name).read_text(encoding="utf-8").splitlines() if l.strip()]
        for x, y in zip(a, b):
            yield ch, x, y


def count(md, pali, chosen, others):
    nl = nc = miss = 0
    no = [0] * len(others)
    chs = [set() for _ in others]
    for ch, x, y in pairs(md):
        if not re.search(pali, x):
            continue
        nl += 1
        c = len(re.findall(chosen, y))
        nc += c
        miss += c == 0
        for i, o in enumerate(others):
            k = len(re.findall(o, y))
            no[i] += k
            if k:
                chs[i].add(ch)
    return nl, nc, miss, no, chs


def main(argv):
    rows, fails = [], 0
    for item, label, pali, chosen, others, kind in ITEMS:
        nl, nc0, _, no0, ch0 = count(BEFORE, pali, chosen, others)
        nl1, nc1, miss1, no1, _ = count(NOW, pali, chosen, others)
        left = sum(no1)
        bad = left or not nl1 or miss1
        fails += bool(bad)
        chs = sorted(set().union(*ch0), key=lambda c: int(c) if c.isdigit() else 0) if others else []
        print(f"{'FAIL' if bad else 'OK  '} {item}: {nl1} lines; chosen {nc0} -> {nc1}"
              + (f"; other forms {sum(no0)} -> {left}" if others else "")
              + (f"; {miss1} lines without it" if miss1 else ""))
        rows.append((label, chosen.replace("\\", ""), "; ".join(f"{o.replace(chr(92), '')} ({n})" for o, n in zip(others, no0) if n)
                     or "-", ", ".join(chs) or "-"))
    if "--table" in argv:
        with open(HERE / "harmonise-table.tsv", "w", encoding="utf-8") as fh:
            fh.write("Pāli\tchosen Burmese\tother forms (uses before the pass)\tchapters\n")
            for r in rows:
                fh.write("\t".join(r) + "\n")
    print(f"{len(ITEMS) - fails} / {len(ITEMS)} items OK")
    return fails


if __name__ == "__main__":
    sys.exit(1 if main(sys.argv[1:]) else 0)
