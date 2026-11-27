"""Consistency pass (pi-4 Burmese, Puggalapaññatti): every item of harmonise-todo.md, before vs now.
For each item the lines whose Pāli matches `pali` are taken (an item is counted only where the Pāli line has it); in
their Burmese the uses of the chosen form and of every other form are counted, in the chapter files before the pass
(harmonise-backup/chapters/) and now. An item fails if an other form is left now, or if a line that has the Pāli item
lacks the chosen form now. Model: pi-3-my/harmonise_scan.py (read only).
usage: python3 -I -X utf8 harmonise_scan.py [--table]   (--table also writes harmonise-table.tsv)"""
import pathlib
import re
import sys

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import my4_formulas as F  # noqa: E402

ROOT = HERE.parents[3]
PD = ROOT / "AI_translation/pali/pi-4_split_chapters"
NOW = ROOT / "AI_translation/burmese/pi-4-burmese-plain-zeroshot_split_chapters"
BEFORE = HERE / "harmonise-backup/chapters"
E = re.escape
NUM3 = r"(?:သုံး|လေး|ငါး)"
Q = '"'

# (item, Pāli regex on the line, chosen Burmese (regex), [other forms (regex)], kind)
# kind: A = source as written, B = term / frame drift, R = rule kept (verified, nothing to change)
ITEMS = [
    # ---- Part A: the source as written
    ("A1 ^4-1 / ^4-2 kālena kālaṃ samayena samayaṃ (no mark: no «၊»)", r"kālena kālaṃ samayena samayaṃ",
     r"အခါအားလျော်စွာ အချိန်အလိုက်", [r"အခါအားလျော်စွာ၊ အချိန်အလိုက်"], "A"),
    ("A2 ^4-52 «… saṅkappati ‘mā maṃ jaññā’ti …» (no comma: «ကြံစည်၍»)", "saṅkappati " + Q + "mā maṃ",
     r"ကြံစည်၍ “", [r"ကြံစည်၏၊ “"], "A"),
    ("A2 ^4-72 «… saṅkappati, ‘mā maṃ jaññā’ti …» (the comma kept: «၊»)", "saṅkappati, " + Q + "mā maṃ",
     r"ကြံစည်၏၊ “", [], "R"),
    ("A2 ^4-46 / ^4-66 «Pubbakālaṃ kodho aparakālaṃ upanāho» (no comma: «ဖြစ်၍»)",
     r"Pubbakālaṃ kodho aparakālaṃ upanāho", r"အမျက်ဒေါသ ဖြစ်၍ နောက်ပိုင်း", [r"အမျက်ဒေါသ ဖြစ်၏၊ နောက်ပိုင်း"], "A"),
    ("A2 ^4-66 «… upanāho yo evarūpo …» (no full stop: «ဖြစ်၍», no «၊»)", r"aparakālaṃ upanāho yo evarūpo",
     r"သိုထားမှု ဖြစ်၍ ဤသို့ သဘောရှိသော", [r"သိုထားမှု ဖြစ်၏၊ ဤသို့", r"သိုထားမှု ဖြစ်၏။ ဤသို့"], "A"),
    ("A2 ch8 ^4-204 / ch10 «… phusitvā viharati paññāya …» (no «;»: «နေကာ» / «မဟုတ်ဘဲ»)",
     r"kāyena phusitvā viharati paññāya", r"နေကာ ပညာဖြင့်|နေသည်ကား မဟုတ်ဘဲ ပညာဖြင့်",
     [r"နေ၏၊ ပညာဖြင့်", r"မဟုတ်၊ ပညာဖြင့်"], "A"),
    ("A2 ch2 / ch4 «… phusitvā viharati; / , paññāya …» (the mark kept: «၊»)", r"kāyena phusitvā viharati[;,] paññāya",
     r"နေ၏၊ ပညာဖြင့်|မဟုတ်၊ ပညာဖြင့်", [r"နေကာ ပညာဖြင့်"], "R"),
    ("A2 ^4-155 «ayaṃ vuccati, puggalo ‘…’» (the stray comma has no place in the Burmese order: frame kept)",
     r"ayaṃ vuccati, puggalo", r"ဤပုဂ္ဂိုလ်ကို “", [], "R"),
    ("A2 ^4-198 «… viharati, sabbapāṇabhūtahitānukampī byāpādapadosā …» (one comma = one «၊», after the verb)",
     r"abyāpannacitto viharati, sabbapāṇabhūtahitānukampī byāpādapadosā", r"စာနာလျက် နေ၏၊ ဖျက်ဆီးလိုစိတ်နှင့်", [],
     "R"),
    ("A2 ^4-206 / ^4-208 «… -ānusārī, phale ṭhito …(ti)» (comma = «၊»; the closing «ti» without a quote: ch2 form)",
     r"(?:dhamm|saddh)ānusārī, phale ṭhito", r"အစဉ်လိုက်သူ ဖြစ်၏၊ ဖိုလ်၌ တည်သောအခါ", [], "R"),
    ("A2 / B1 ch4 / ch5 / ch8 / ch10 «Ayaṃ vuccati puggalo X.» without quotes = no quotes",
     "^(?!.*vuccati,? puggal[oā] " + Q + ").*[Aa]yaṃ vuccati puggalo [^" + Q + "]",
     r"ဤပုဂ္ဂိုလ်ကို [^“][^။]*ဟု ခေါ်သည်", [r"ဤပုဂ္ဂိုလ်ကို “[^။]*”ဟု ခေါ်သည်"], "A"),
    ("A3 ch8 ummujjati ‘…’ti = «“…”ဟု ပေါ်လာ၏» (no added «သဘောထား၍»)", "ummujjati " + Q, r"”ဟု ပေါ်လာ၏",
     [r"သဘောထား၍"], "A"),
    ("A3 ch6 sallekha = «ခြိုးခြံခြင်း» (no added object «ကိလေသာကို»)", r"sallekhaṃyeva", E(F.SALLEKHA) + "ကိုသာ",
     [r"ကိလေသာကို ခြစ်ခွာခြင်း"], "A"),
    ("A4 ^4-176 «puratthimena narassa» as written = «လူ၏ အရှေ့ဘက်၌» (not nagarassa)", r"puratthimena narassa",
     r"လူ၏ အရှေ့ဘက်၌", [r"မြို့၏ အရှေ့ဘက်"], "A"),
    ("A4 ^4-142 «samādiṭṭhi» (spelling only) = sammādiṭṭhi «မှန်ကန်သော အယူ ရှိသူ» (kept)", r"samādiṭṭhi hoti",
     r"မှန်ကန်သော အယူ ရှိသူ", [], "R"),
    ("A4 ^4-166 «Idhekacco puggalo vaṇṇopi saṃvijjati …» (nominative as written: no «…၏ ရှေ့၌»)",
     r"Idhekacco puggalo vaṇṇopi saṃvijjati", r"ပုဂ္ဂိုလ်သည် ချီးမွမ်းဖွယ်လည်း ရှိ၏", [r"ပုဂ္ဂိုလ်၏ ရှေ့၌"], "A"),
    ("A5 a space before «…» in the Pāli (typography: «X…»)", r" …", r"[^ ]…", [r" …"], "R"),
    # ---- B1 frames
    ("B1 Katamo ca puggalo X? = «X ဟူသည် အဘယ် ပုဂ္ဂိုလ်နည်း။» (sample)", r"Katamo ca pu[g]+alo",
     r"ဟူသည် အဘယ် ပုဂ္ဂိုလ်နည်း(?:။|…)", [], "R"),
    ("B1 Tattha katame N G puggalā? = «ထိုတို့အနက် G ပုဂ္ဂိုလ် N-ယောက် ဟူသည် အဘယ် ပုဂ္ဂိုလ်တို့နည်း။»",
     r"Tatt?[hr]a katame (?:tayo|cattāro|pañca) \S+ puggalā\?", r"ဟူသည် အဘယ် ပုဂ္ဂိုလ်တို့နည်း။",
     [r"ဟူသည် အဘယ်တို့နည်း။"], "B"),
    ("B1 Katame N? = «အဘယ် N-ယောက်တို့နည်း။» (no «puggalā» in the Pāli)", r"Katame (?:tayo|cattāro|pañca)\?",
     rf"အဘယ် {NUM3}ယောက်တို့နည်း။", [rf"အဘယ် ပုဂ္ဂိုလ် {NUM3}ယောက်နည်း"], "B"),
    ("B1 Tattha katamo X? = «ထိုတို့အနက် X ဟူသည် အဘယ်နည်း။» (pi-1 / pi-2)", r"Tattha katam[oā] ",
     r"ထိုတို့အနက် [^။]+ ဟူသည် အဘယ်နည်း။", [], "R"),
    ("B1 Kathañca puggalo X? = «ပုဂ္ဂိုလ်သည် အဘယ်သို့ …သနည်း။»", r"Kathañca puggalo", r"ပုဂ္ဂိုလ်သည် အဘယ်သို့ ", [], "R"),
    ("B1 Evaṃ puggalo X. = «ဤသို့ ပုဂ္ဂိုလ်သည် …၏။»", r"[Ee]vaṃ puggalo", r"ဤသို့ ပုဂ္ဂိုလ်သည် ", [], "R"),
    ("B1 ayaṃ vuccati puggalo ‘X’. = «ဤပုဂ္ဂိုလ်ကို “X”ဟု ခေါ်သည်။» (sample)", "vuccati,? puggalo " + Q,
     r"ဤပုဂ္ဂိုလ်ကို “[^”]+”ဟု ခေါ်သည်", [], "R"),
    # ---- B2 sentences shared between the chapters
    ("B2 yā sā vācā nelā kaṇṇasukhā … tathārūpiṃ vācaṃ bhāsitā hoti = pi-1 ^1-1350", r"nelā kaṇṇasukhā",
     E(F._NELA_A) + "၊? " + E(F._NELA_B), [r"နားကို သာယာစေသော", r"နားဝင် ချိုသော", r"ထိုကဲ့သို့သော စကား"], "B"),
    ("B2 abhiṇhaṃ kujjhati = «ခဏခဏ အမျက်ဒေါသ (မ)ထွက်»", r"abhiṇhaṃ kujjhati", r"ခဏခဏ အမျက်ဒေါသ (?:မ)?ထွက်",
     [r"ခဏခဏ အမျက်ထွက်", r"ခဏခဏ အမျက် မထွက်"], "B"),
    ("B2 So ca khvassa kodho (na) ciraṃ dīgharattaṃ anuseti = «ထိုသူ၏ ထိုအမျက်ဒေါသသည်ကား … (မ)ကိန်းအောင်း»",
     r"khvassa kodho", E(F.KODHO_LONG[:-len("ကိန်းအောင်း၏")]) + "(?:မ)?ကိန်းအောင်း",
     [r"အမျက်ဒေါသသည်လည်း ကြာမြင့်", r"ကိန်းအောင်း မနေ", r"ကိန်းအောင်း၍ နေ၏"], "B"),
    ("B2 dussīlo hoti pāpadhammo = «သီလ ပျက်သူ၊ ယုတ်မာသော သဘော ရှိသူ ဖြစ်၏» (pi-2 dussīla)",
     r"dussīlo hoti pāpadhammo|hoti dussīlo pāpadhammo", r"သီလ ပျက်သူ၊ ယုတ်မာသော သဘော ရှိသူ ဖြစ်",
     [r"သီလ ပျက်၍ ယုတ်မာသော သဘော ရှိသူ", r"သီလ ပျက်သူ ဖြစ်၏၊ ယုတ်မာ"], "B"),
    ("B2 sīlavā hoti kalyāṇadhammo = «သီလ ရှိသူ၊ ကောင်းမွန်သော သဘော ရှိသူ ဖြစ်၏» (pi-2 sīlavā)",
     r"sīlavā hoti kalyāṇadhammo|hoti sīlavā kalyāṇadhammo", r"သီလ ရှိသူ၊ ကောင်းမွန်သော သဘော ရှိသူ ဖြစ်",
     [r"သီလ ရှိ၍ ကောင်းမွန်သော သဘော ရှိသူ", r"သီလ ရှိသူ ဖြစ်၏၊ ကောင်းမွန်"], "B"),
    ("B2 the arahant sentence āsavānaṃ khayā anāsavaṃ … upasampajja viharati (pi-2 ^2-831 without «တော်မူ»)",
     r"āsavānaṃ khayā anāsavaṃ", E(F.W["asava"]) + r"တို့ ကုန်ခန်းခြင်းကြောင့် .* ဝင်စား၍ နေ", [r"နေတော်မူ"], "R"),
    ("B2 musāvādaṃ pahāya musāvādā paṭivirato hoti (ch4 = ch5)", r"[Mm]usāvādaṃ pahāya musāvādā paṭivirato hoti",
     r"မုသား ပြောခြင်းကို ပယ်၍ မုသား ပြောခြင်းမှ ရှောင်ကြဉ်သူ ဖြစ်၏", [], "R"),
    ("B2 sense restraint cakkhunā rūpaṃ disvā … (pi-1 ^1-1354; ch3 = ch5)", r"cakkhunā rūpaṃ disvā na nimittaggāhī",
     r"မျက်စိဖြင့် အဆင်းအရောင်ကို မြင်၍ အမှတ်အသားကို စွဲယူသူ မဟုတ်", [], "R"),
    ("B2 the hindrances and the jhānas (pi-2 ^2-508; ch5 = ch6)", r"So ime pañca nīvaraṇe pahāya",
     r"ဤအတားအဆီး ငါးပါးတို့ကို ပယ်၍ ကာမတို့မှ ကင်းဆိတ်၍သာ", [], "R"),
    ("B2 evaṃ samāhite citte … (ch6 = ch5)", r"evaṃ samāhite citte", E(F.SAMAHITE),
     [r"စိတ် တည်ကြည်၍ စင်ကြယ်ပြီး"], "B"),
    ("B2 ‘ime āsavā’ti … = «ဤသည်တို့ကား စိတ်အစွန်းအထင်းတို့» (ch6 = ch5)", Q + "ime āsavā" + Q + "ti",
     E(F.ASAVA4[0]) + "”", [r"ဤသည်ကား စိတ်အစွန်းအထင်းတို့”"], "B"),
    ("B2 Tassa evaṃ jānato evaṃ passato … (ch6 = ch5)", r"jānato evaṃ passato", E(F.JANATO[:-1]),
     [r"ဤသို့ သိ၍ ဤသို့ မြင်သော"], "B"),
    ("B2 Vimuttasmiṃ vimuttamiti ñāṇaṃ hoti (ch6 = ch5)", r"Vimuttasmiṃ vimuttamiti", E(F.VIMUTTASMIM[:-1]),
     [r"ဟု သိသော ဉာဏ်"], "B"),
    ("B2 ‘Khīṇā jāti … nāparaṃ itthattāyā’ti pajānāti (ch6 = ch5)", Q + "Khīṇā jāti", E(F.KHINA[:-1]),
     [r"ပြုဖွယ် ကိစ္စကို"], "B"),
    ("B2 santo saṃvijjamānā (lokasmiṃ / bhikkhūsu) = «ရှိကြ၏၊ ထင်ရှား ရှိကြ၏»", r"santo saṃvijjamānā",
     E(F.SANTO_PL), [r"ထင်ရှား တွေ့ရကြ", r"ထင်ရှား ရှိနေ"], "B"),
    ("B2 santo saṃvijjamāno (singular) = «ရှိ၏၊ ထင်ရှား ရှိ၏»", r"santo saṃvijjamāno", E(F.SANTO_SG),
     [r"ထင်ရှား ရှိနေသော"], "B"),
    ("B2 … santo saṃvijjamān- bhikkhūsu = «ရဟန်းတို့အတွင်း၌»", r"saṃvijjamān[oā] bhikkhūsu", E(F.BHIKKHUSU),
     [r"ရဟန်းတို့အထဲ၌"], "B"),
    ("B2 (Evamevaṃ) ime N G puggalā santo … = «G ဤပုဂ္ဂိုလ် N-ယောက်တို့သည်»",
     r"(?:[Ii]me (?:tayo|cattāro|pañca)|tayome|cattārome|pañcime) \S+ puggalā santo",
     rf"နှင့် တူသော ဤပုဂ္ဂိုလ် {NUM3}ယောက်တို့သည်", [r"ဤ (?:လူနာ|လျှော်ပိတ်စ|ကာသိ)"], "B"),
    ("B2 evamevaṃ = «ထို့အတူပင်» (pi-2 evameva)", r"[Ee]vamevaṃ", E(F.EVAMEVAM), [r"ဤအတူပင်"], "B"),
    ("B2 Seyyathāpi so X P, tathūpamo ayaṃ puggalo. = «ဥပမာအားဖြင့် ထိုXသည် Pသကဲ့သို့၊ ဤပုဂ္ဂိုလ်သည် ထိုXနှင့် တူ၏။»",
     r"tathūpamo ayaṃ puggalo", r"ဥပမာအားဖြင့် ထို[^။]*သကဲ့သို့၊ ဤပုဂ္ဂိုလ်သည် ထို[^။]+နှင့် တူ၏",
     [r"သကဲ့သို့ ဤပုဂ္ဂိုလ်သည်", r"ဤပုဂ္ဂိုလ်သည် ထိုနှင့် တူ၏", r"။ ထို(?:လျှော်ပိတ်စ|ကာသိ ပိတ်စ)သည်"], "B"),
    # ---- B3 the person
    ("B3 So (the person) = «ထိုသူသည်» (not pi-2 «ထိုရဟန်းသည်»)", r"(?:^|[.?!] |– )So (?!ca khvassa)", E(F.SO), [r"ထိုရဟန်းသည်"],
     "B"),
    ("B3 assa / taṃ (the person) = «ထိုသူ…» (bhikkhuṃ itself stays «ရဟန်း»)",
     r"[Kk]imassa|[Ii]damassa|Tamenaṃ|panassa|Tassa taṃ vacanaṃ|saṅgho taṃ", r"ထိုသူ",
     [r"ထိုရဟန်း(?!ထံသို့)"], "B"),
    ("B3 Tassa (na) evaṃ hoti = «ထိုသူအား ဤသို့ အကြံ (မ)ဖြစ်»", r"[Tt]assa (?:na )?evaṃ hoti", E(F.TASSA_EVAM),
     [r"ထိုသူ၌ ဤသို့ အကြံ", r"ထိုရဟန်းအား"], "B"),
    # ---- B4 the Buddha
    ("B4 bhagavā / bhagavatā in ordinary sentences = «မြတ်စွာဘုရား» (pi-1 / pi-2)", r"\bbhagav(?!ā\.)", E(F.BHAGAVA),
     [r"ဘုန်းတော်ရှင်"], "R"),
    ("B4 bhagavā in the ^4-177 epithet list (tathāgato the subject) = «ဘုန်းတော်ရှင်» (context-specific epithet)",
     r"buddho bhagavā", E(F.BHAGAVA_EPITHET) + " ဖြစ်တော်မူ၏", [], "B"),
    ("B4 tathāgata = «မြတ်စွာဘုရား» (pi-2 termbase; coordinator decision)", r"[Tt]athāgat", E(F.TATHAGATA),
     [r"တထာဂတ"], "R"),
    ("B4 buddho (the Buddha list) = «သစ္စာတို့ကို သိတော်မူသူ» (as before)", r"satthā devamanussānaṃ buddho",
     r"သစ္စာတို့ကို သိတော်မူသူ", [], "R"),
    # ---- B5 distinct terms
    ("B5 vippaṭisāra = «နောင်တ ရခြင်း» (pi-1 / pi-2 vippaṭisāro), vippaṭisārī = «နောင်တ ရသူ»", r"vippaṭisār",
     r"နောင်တ ရ(?:သူ|ခြင်း)", [r"နောင်တ ပူပန်သူ", r"နောင်တ ပူပန်မှုမှ ဖြစ်သော"], "B"),
    ("B5 kukkucca = «နောင်တ ပူပန်…» (pi-1 / pi-2, kept apart from vippaṭisāra)", r"kukkucc", r"နောင်တ (?:မ)?ပူပန်",
     [], "R"),
    ("B5 abhikkhaṇaṃ / abhiṇhaṃ = «ခဏခဏ»", r"abhikkhaṇaṃ|abhiṇhaṃ", r"ခဏခဏ", [r"မကြာခဏ"], "R"),
    ("B5 vuṭṭhāti tamhā ābādhā (recovers) = «ပျောက်ကင်း»", r"vuṭṭhāti tamhā ābādhā", r"ပျောက်ကင်း", [r"ထမြောက်"],
     "R"),
    ("B5 samāpajjatipi vuṭṭhātipi (from an attainment) = «ထမြောက်»", r"samāpajjatipi vuṭṭhātipi", r"ထမြောက်",
     [r"ပျောက်ကင်း"], "R"),
    ("B5 uttama = «အထွတ်အထိပ်» / agga = «အမြတ်ဆုံး» (kept apart)", r"aggo ca seṭṭho ca pāmokkho",
     r"အမြတ်ဆုံးလည်း၊ အကောင်းဆုံးလည်း၊ အကြီးမှူးလည်း(?: \[[^\]]+\])?၊ အထွတ်အထိပ်လည်း၊", [], "R"),
    ("B5 vipassati viloketi = «သေချာစွာ မြင်၍ ပတ်ဝန်းကျင်ကို ကြည့်» (mātikā = ch8)", r"vipassati viloketi",
     E(F.VIPASSATI), [r"မြင်၏၊ ပတ်ဝန်းကျင်"], "B"),
    # ---- B6 simile and list vocabulary
    ("B6 khīra = «နွားနို့» (pi-1 / pi-2 termbase)", r"khīraṃ", E(F.KHIRA), [r"(?<!နွား)နို့ဖြင့်"], "B"),
    ("B6 Idha pana(ekacco) = «တစ်ဖန် ဤလောက၌ …» (ch4 = ch5)", r"[Ii]dha panekacco", r"တစ်ဖန် ဤလောက၌",
     [r"ထို့ပြင် ဤလောက၌"], "B"),
    ("B6 tathārūpa = «ထိုသို့သော» (pi-1 termbase)", r"tathārūpiṃ vācaṃ", r"ထိုသို့သော စကားကို",
     [r"ထိုသို့ သဘောရှိသော စကား", r"ထိုကဲ့သို့သော စကား"], "B"),
    ("B6 the simile groups (valāhaka … rukkha, yodhājīva) = the sample's group names",
     r"(?:valāhak|mūsik|amb|kumbh|udakarahad|balībadd|āsīvis|rukkh|yodhājīv)ūpamā",
     r"(?:မိုးတိမ်|ကြွက်|သရက်သီး|အိုး|ရေကန်|နွားလား|မြွေဆိုး|သစ်ပင်|စစ်သည်)နှင့် တူသော", [], "R"),
    ("B6 the ascetic practices (mātikā = ch6)", r"piṇḍapātikā|sosānikā", r"ဆွမ်းခံ၍သာ စားသူ|သုသာန်၌ နေသူ", [], "R"),
    ("B6 the ten courses (abstention) = «… မှ ရှောင်ကြဉ်သူ»", r"pāṇātipātā paṭivirato",
     r"သူ့အသက်ကို သတ်ခြင်းမှ ရှောင်ကြဉ်သူ", [], "R"),
    ("B6 the five sampadā (sīla … vimuttiñāṇadassana) = «X ပြည့်စုံသူ / ပြည့်စုံခြင်း»", r"sīlasampann",
     r"သီလ ပြည့်စုံ", [], "R"),
    # ---- B7 variant brackets: one renderer (my4_formulas.var_my)
    ("B7 sigla (aṭṭhakathā) = «(အဋ္ဌကထာ)»", r"\(aṭṭhakathā\)", r"\(အဋ္ဌကထာ\)", [], "R"),
    ("B7 several readings in one bracket = «[L (S1): a၊ (S2): b …]» (pi-2 ^2-832)", r"\([a-zāī. ]+\), [^\[\]]+ \(",
     r"၊ \((?:Sī|Syā|Ka|Pī|အဋ္ဌကထာ)[^)]*\): ", [], "R"),
    ("B7 the editors' «evaṃ / evameva …pi» notes = «…လည်း ဤနည်းတူ»",
     r"evamuparipi|evaṃ tīsu ṭhānesupi|suttepi evameva|dukaniddesepi", r"လည်း ဤနည်းတူ\]",
     [r"ဤအတိုင်းပင် ဖြစ်သည်"], "B"),
    ("B7 sutta references «a. ni. / ma. ni. / dī. ni. / vibha. N» = «၊ “…” N»", r"\) (?:a|ma|dī)\. ni\. \d|\) vibha\. \d",
     r"၊ “[^”]+” [\d.]+", [], "R"),
    # ---- B8 headings and colophons
    ("B8 Xuddeso = «X-မျိုးတွဲ အကျဉ်း ဖော်ပြချက်»", r"^#### \w+uddeso", r"မျိုးတွဲ အကျဉ်း ဖော်ပြချက်", [], "R"),
    ("B8 Xpuggalapaññatti = «X-မျိုးတွဲ ပုဂ္ဂိုလ် သတ်မှတ်ချက်»", r"^#### \w+puggalapaññatti",
     r"မျိုးတွဲ ပုဂ္ဂိုလ် သတ်မှတ်ချက်", [], "R"),
    ("B8 Xniddeso. = «X-မျိုးတွဲ အကျယ် ဖော်ပြချက်။» (pi-1 / pi-2)", r"^\w+niddeso\.", r"မျိုးတွဲ အကျယ် ဖော်ပြချက်။",
     [], "R"),
    ("B8 Ekakaṃ … Dasakaṃ. = «N-မျိုးတွဲ။» (pi-1 / pi-2)", r"^[A-ZĀ][a-zāñṭ]*kaṃ\.", r"^[^ ]*မျိုးတွဲ။", [], "R"),
    ("B8 the book colophon = «“…” ကျမ်း ပြီးဆုံးပြီ။» (pi-1 / pi-2 / pi-3)", r"Puggalapaññattipakaraṇaṃ niṭṭhitaṃ",
     E(f"“{F.TITLE}” ကျမ်း ပြီးဆုံးပြီ။"), [], "R"),
    ("B8 the mātikā colophon", r"Puggalapaññattimātikā niṭṭhitā", r"ခေါင်းစဉ်စာရင်း” ပြီးဆုံးပြီ။", [], "R"),
]

ID = re.compile(r"\s*\^[0-9A-Za-z-]+\s*$")


def pairs(md):
    for p in sorted(PD.glob("*.md")):
        ch = p.name.split("-")[0].split(".")[0]
        a = [ID.sub("", l) for l in p.read_text(encoding="utf-8-sig").splitlines() if l.strip()]
        b = [ID.sub("", l) for l in (md / p.name).read_text(encoding="utf-8").splitlines() if l.strip()]
        for x, y in zip(a, b):
            yield ch, x, y


def count(md, pali, chosen, others, item=""):
    nl = nc = miss = 0
    no = [0] * len(others)
    chs = [set() for _ in others]
    for ch, x, y in pairs(md):
        if not re.search(pali, x if item.startswith("B7") else re.sub(r" ?\[[^\]]*\]", "", x)):
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
    for item, pali, chosen, others, kind in ITEMS:
        nl, nc0, _, no0, ch0 = count(BEFORE, pali, chosen, others, item)
        nl1, nc1, miss1, no1, _ = count(NOW, pali, chosen, others, item)
        left = sum(no1)
        bad = left or not nl1 or miss1
        fails += bool(bad)
        chs = sorted(set().union(*ch0), key=lambda c: int(c) if c.isdigit() else 0) if others else []
        print(f"{'FAIL' if bad else 'OK  '} {item}: {nl1} lines; chosen {nc0} -> {nc1}"
              + (f"; other forms {sum(no0)} -> {left}" if others else "") + (f"; {miss1} lines without it" if miss1 else ""))
        rows.append((item, chosen, "; ".join(f"{o} ({n})" for o, n in zip(others, no0) if n) or "-",
                     ", ".join(chs) or "-"))
    if "--table" in argv:
        with open(HERE / "harmonise-table.tsv", "w", encoding="utf-8") as fh:
            fh.write("Pāli item\tchosen Burmese\tother forms before (uses)\tchapters changed\n")
            for r in rows:
                fh.write("\t".join(r) + "\n")
    print(f"{len(ITEMS) - fails} / {len(ITEMS)} items OK")
    return fails


if __name__ == "__main__":
    sys.exit(1 if main(sys.argv[1:]) else 0)
