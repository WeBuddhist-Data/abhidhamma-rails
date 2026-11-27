"""Classify every termbase-adherence miss of the pi-2 Burmese zero-shot: GENUINE / INFLECTION / ARTEFACT; and every
miss the rails introduce (a miss of the rails that the zero-shot did not have).

usage: python3 -I -X utf8 classify_misses.py   (after build_rails.py + apply_termbase.py + the rails adherence run)
Inputs: rails/adherence-zeroshot.txt (fixed input), rails/adherence-rails.txt, rails/layer-log.tsv, rails/apply-log.tsv,
the zero-shot keyword map AI_translation/burmese/pi-2-keywords-by-reference-pali-burmese-plain.md (the zero-shot's own
form of each keyword in each segment) and termbase/decisions-A.tsv (the decided senses).
Writes rails/adherence-classified.tsv (id, keyword, termbase term, text form, class, reason, ch, src).
  * GENUINE row (zero-shot miss): its keyword belongs to a family (FAM: keyword -> Lnn / Rnn) whose layer patch or
    residual rule was applied in this build (layer-log.tsv / apply-log.tsv); the zero-shot form (keyword map) occurs in
    the zero-shot segment (or the map says «no direct equivalent» and no termbase term occurs: a gap); and the keyword
    passes in the rails segment (the same occurrence test as adherence_my.py).
  * INFLECTION / ARTEFACT row: its text-form regex must match the segment (zero-shot; rails for src=rails) and its Pāli
    check, where given, must match the segment's Pāli (a leading «!» means it must NOT match).
  * CONFLICT row (ARTEFACT, termbase conflict): an undecided entry that keeps the zero-shot form, where the rails apply a
    decided entry of the same word (decisions-A.tsv); the decided entry must be in decisions-A.tsv and its term must
    occur in the rails segment.
Any other row is UNVERIFIED and the run fails (exit 1).
"""
import pathlib
import re
import sys
import unicodedata

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(HERE))
sys.dont_write_bytecode = True
import adherence_my as A  # noqa: E402

PALI = ROOT / "AI_translation/pali/pi-2_split_chapters"
ZS = ROOT / "AI_translation/burmese/pi-2-burmese-plain-zeroshot_split_chapters"
RL = ROOT / "AI_translation/burmese/pi-2-burmese-plain-rails_split_chapters"
TB = ROOT / "AI_translation/burmese/pi-2-pali-burmese-termbase-plain.md"
KMAP = ROOT / "AI_translation/burmese/pi-2-keywords-by-reference-pali-burmese-plain.md"
DEC = HERE.parent / "termbase/decisions-A.tsv"
OUT = HERE / "adherence-classified.tsv"
N = lambda s: unicodedata.normalize("NFC", s)

# --- GENUINE families: keyword -> layer patch (my_formulas_rails.py) / residual rule (apply_termbase.py)
FAM = {}
for _lid, _kws in {
    "L01": "Avasesā|Avasesā dhammā|avasesā|Avasesānaṃ",
    "L02": "niddeso",
    "L03": "pihakaṃ",
    "L04": "yapeti|yāpeti|iriyati",
    "L05": "paṭilābho|upasampadā|sacchikiriyā",
    "L06": "ajjhupekkhanā",
    "L07": "dāna|bhāvanā|Dānaṃ",
    "L08": "santā|samitā|vūpasantā|atthaṅgatā|abbhatthaṅgatā|appitā|byappitā|sositā|visositā|byantīkatā|samitaṃ|"
           "vūpasantaṃ|Vūpasanta|vūpasanta|jātā|sañjātā|nibbattā|pātubhūtā|jātaṃ",
    "L09": "upeto|samupeto|samannāgato|samannāgatā",
    "L10": "sakkāra|sakkāraṃ|garukāra|garukāraṃ|paṭibhāna|paṭibhānena|iriyāpathaṃ|iddhi|Iddhi",
    "L20": "mātā|anattha|anatthaṃ|Anatthaṃ|ahita",
    "L21": "asesa|virāga",
    "L22": "ātāpī|kāyānupassī viharati",
    "L23": "pariyantaṃ",
    "L24": "niruddha|samanantarā",
    "L25": "samannāhāro|āvaṭṭanā|ābhogo",
    "L26": "nāsaññī|Nevasaññīnāsaññī",
    "L27": "kāmāvacare",
    "L28": "bhajati|payirupāsanti",
    "L29": "khantiyā",
    "L30": "patta|phala|dānena|cāṭukamyatāya|muggasūpyatāya|pāribhaṭayatāya",
    "L31": "buddha|buddhe|buddhaṃ|sambuddho|sammāsambuddho|sammāsambuddhā|rāja",
    "L32": "seyyaṃ|kappeti",
    "L33": "āsevati|bahulīkaroti",
    "L34": "nimitte|nirujjhati|paññapenti",
    "L35": "samāpannassa",
    "L36": "abyāpajjo",
    "L37": "Hetu|vattati",
    "L38": "uppannā|dhātu uppannā",
    "L39": "kusalato",
    "L40": "Nānā|aññaṃ",
    "L41": "pajānāti",
    "L42": "itthī|puriso|aṭṭhamaṃ",
    "L43": "gāmī",
    "L44": "sātarūpaṃ|vipatti|āyu",
    "L45": "upapannā|upapajjati",
    "L46": "vedayita",
    "L47": "arahatta",
    "L48": "vipulaṃ|nirāmiso|santiṭṭhati",
    "L50": "paccaya",
    "L51": "nikkhitta",
    "L52": "icchatā|māno",
    "L53": "ārabbha",
    "L54": "ānudiṭṭhi|adhamma|nānatta|nānattasaññā",
    "L55": "meraya|majja",
    "L56": "kula|vaṇṇa",
    "L57": "saṅgo|saṅgā|ādīnavā",
    "L58": "vatthūni|kilesavatthūni|vatthu",
    "L59": "upekkhā",
    "L60": "muta|viññāta",
    "L61": "paṭivirodho",
    "L62": "sassata|sassato|uccheda",
    "L63": "Ajjhattikassa|ajjhattikassa|Bāhirassa|bāhirassa|Parapuggalaṃ|paṭilabhati",
    "L64": "kata|chando",
    "L65": "vipariṇāmadhammā|amanāpo|brahmacariyaṃ",
    "L66": "bhojanassa|ārabhati|vīriyaṃ ārabhati|maggo",
    "L67": "uppanno|kopañca",
    "L68": "chambhitattaṃ",
    "R01": "uparito",
}.items():
    for _k in _kws.split("|"):
        assert _k not in FAM, _k
        FAM[_k] = _lid

NEG_LABH = r"\bna labhati\b"
# --- INFLECTION / ARTEFACT families: (keyword regex, class, text-form regex, reason, Pāli check or None)
OTHER = [
    (r"daṭṭhabbaṃ|daṭṭhabbā", "INFLECTION", r"မှတ်ယူရမည်(?!့)",
     "finite predicate «… daṭṭhabbaṃ / daṭṭhabbā.» = «… မှတ်ယူရမည်။» of the termbase gerundive «မှတ်ယူရမည့်» (the attributive "
     "form; approved sample ch1)", r"daṭṭhabb[aā]ṃ?\."),
    (r"hīno", "INFLECTION", r"ယုတ်ညံ့သော",
     "attributive «atthi hīno (vedanākkhandho …)» = «ယုတ်ညံ့သော …» of the termbase person form «ယုတ်ညံ့သူ» ('I am inferior'); "
     "same lemma (approved sample ch1)", r"(?i)\batthi hīno\b"),
    (r"labhati", "ARTEFACT", r"မရခြင်း",
     "negation «yampicchaṃ na labhati» = «… မရခြင်း» (style rule: na = «မ…»)", NEG_LABH),
    (r"labhati|labhati samādhiṃ|gacchati|saṅkhyaṃ gacchati", "INFLECTION", r"ရ၏",
     "finite «… ရ၏» (literary present, as every verb of these passages) of the termbase «ရသည်»", r"\b(?:labhati|gacchati)\b"),
    (r"saṅkhārapaccayā", "INFLECTION", r"ပြုပြင်ဖန်တီးမှုများကြောင့်",
     "plural marker: the suttanta exposition «avijjāpaccayā saṅkhārā» (plural; pi-1 final 4-03 «ပြုပြင်ဖန်တီးမှုများကြောင့်», "
     "harmonise_align_kept KEPT) of the termbase «ပြုပြင်ဖန်တီးမှုကြောင့်»; not the abhidhamma exposition (avijjāpaccayā "
     "saṅkhāro, singular)", r"!avijjāpaccayā saṅkhāro\b"),
    (r"abhijānissanti|sevissanti", "INFLECTION", r"ကြလိမ့်မည်",
     "plural marker «ကြ» (3rd pl. subject) inside the termbase future «…လိမ့်မည်»", r"(?:abhijānissanti|sevissanti)"),
    (r"lābhiṃ", "INFLECTION", r"ရသူအား",
     "person form «ရသူအား» (to one who has gained) of the termbase attributive «ရသော» (as pi-1 Saṃviggassa)", r"\blābhiṃ\b"),
    (r"vuṭṭhito", "INFLECTION", r"ထပြီး",
     "the same verb «ထ» with the perfect «ပြီး … ဖြစ်၏» (gilānā vuṭṭhito hoti) of the termbase «ထသော»", r"vuṭṭhito"),
    (r"pītisukhaṃ", "INFLECTION", r"ပီတိနှင့် သာယာမှု",
     "the noun (jhāna factor list «sampasādo, pītisukhaṃ, cittassekaggatā») of the termbase «ပီတိနှင့် သာယာမှု ရှိသော» "
     "(the gloss: 'joy and pleasure, or having joy and pleasure'; the bahubbīhi takes «ရှိသော»)", r"sampasādo, pītisukhaṃ"),
    # ARTEFACT: privative / negation
    (r"ñāṇaṃ", "ARTEFACT", r"မသိခြင်း",
     "privative aññāṇaṃ has its own entry «မသိခြင်း» (pi-1 locked; style rule privative a- = «မ» + verb), which the text has; "
     "the ñāṇaṃ gloss «also in aññāṇaṃ» is reported (doubt)", r"\baññāṇaṃ"),
    (r"kamyatā", "ARTEFACT", r"မဖူးမြင်လိုခြင်း",
     "privative: ariyānaṃ adassanakamyatā «အရိယာတို့ကို မဖူးမြင်လိုခြင်း» (verb + desiderative «-လိုခြင်း», as the termbase "
     "asotukamyatā «မနာကြားလိုခြင်း», adaṭṭhukamyatā «မတွေ့မြင်လိုခြင်း»)", r"adassanakamyatā"),
    (r"kamyatā", "ARTEFACT", r"မနာကြားလိုခြင်း", "compound: asotukamyatā has its own entry «မနာကြားလိုခြင်း», which the text has",
     r"asotukamyatā"),
    (r"kamyatā", "ARTEFACT", r"ပြုလုပ်လိုခြင်း",
     "infinitive + kamyatā: kattukamyatā = verb + desiderative «ပြုလုပ်လိုခြင်း» (as the termbase asotukamyatā «မနာကြားလိုခြင်း», "
     "adaṭṭhukamyatā «မတွေ့မြင်လိုခြင်း»); kamyatā «လိုချင်ခြင်း» is the noun + kamyatā sense (sādhukamyatā, bhiyyokamyatā)",
     r"kattukamyatā"),
    (r"kamyatā", "ARTEFACT", r"အလံ ထူလိုခြင်း",
     "compound: ketukamyatā keeps pi-1's own entry «အလံ ထူလိုခြင်း» (decision kamyatā|0: «ketukamyatā keeps its own entry»; "
     "decisions-A «kept on purpose»)", r"ketukamyatā"),
    (r"samannāgatā", "ARTEFACT", r"မပြည့်စုံသော",
     "negation «na kammāvaraṇena samannāgatā …» = «… နှင့် မပြည့်စုံသော» (under negation «အပြည့်အဝ» would say 'not fully')",
     r"\bna kammāvaraṇena samannāgatā"),
    (r"avajāniṃsūti", "ARTEFACT", r"အထင်မသေး",
     "prohibitive negation «mā maṃ pare avajāniṃsu» = «… ငါ့ကို အထင်မသေး…» of the termbase «အထင်သေးသည်»", r"\bmā maṃ pare avajāniṃs"),
    (r"gāho", "ARTEFACT", r"တစ်ထစ်ချ မယူနိုင်ခြင်း",
     "compound in the approved pi-1 doubt list: anekaṃsaggāho «တစ်ထစ်ချ မယူနိုင်ခြင်း» (pi-1 locked own entry and ARTEFACT row; "
     "identical list items = identical Burmese); the gāho gloss «also … in anekaṃsaggāho» is reported (doubt)", r"anekaṃsaggāho"),
    # ARTEFACT: compound / own entry / other sense
    (r"chandaṃ", "ARTEFACT", r"ကာမကို လိုလားမှု",
     "compound: kāmacchandaṃ has its own entry «ကာမကို လိုလားမှု» (chando «as in kāmacchanda»), which the text has",
     r"kāmacchandaṃ"),
    (r"gataṃ", "ARTEFACT", r"အယူမှား", "compound: diṭṭhigataṃ has its own entry «အယူမှား», which the text has", r"diṭṭhigataṃ"),
    (r"samāpattiṃ", "ARTEFACT", r"ပြုပြင်ဖန်တီးမှု အကြွင်းအကျန်သာ ရှိသော ဈာန်",
     "compound: saṅkhārāvasesasamāpattiṃ has its own entry «ပြုပြင်ဖန်တီးမှု အကြွင်းအကျန်သာ ရှိသော ဈာန်», which the text has",
     r"saṅkhārāvasesasamāpattiṃ"),
    (r"samāpattiṃ", "ARTEFACT", r"ဈာန်ကို ဝင်စားသူ",
     "cognate object «rūpāvacarasamāpattiṃ samāpannassa» = «… ဈာန်ကို ဝင်စားသူ၏» (samāpannassa «ဈာန် ဝင်စားသော» holds both "
     "words; a second «ဈာန် ဝင်စားရာကို» would repeat the verb)", r"samāpattiṃ samāpannassa"),
    (r"vipākadhammadhammā|dhammā", "ARTEFACT", r"အကျိုး ပေးတတ်သော ပညာ",
     "the triad name as attribute of paññā («vipākadhammadhammā paññā»): the head noun «ပညာ» takes the place of the "
     "termbase's «သဘောတရား» (dhammā)", r"vipākadhammadhammā paññā"),
    (r"paṭicca", "ARTEFACT", r"ကိုလည်းကောင်း၊ [^၊]*ကိုလည်းကောင်း မှီ၍",
     "absolutive with its own objects «cakkhuñca paṭicca rūpe ca» = «…ကိုလည်းကောင်း … မှီ၍»; the termbase sense is the "
     "compound member of paṭiccasamuppāda / -samuppanna", r"\bpaṭicca rūpe ca\b"),
    (r"indriyānaṃ", "ARTEFACT", r"စွမ်းရည် နှစ်ဆယ့်နှစ်ပါး",
     "other sense: the twenty-two faculties (Indriyavibhaṅga «စွမ်းရည်», pi-1 indriya), not the sense organs of the termbase "
     "indriyānaṃ «အာရုံခံ အင်္ဂါ»", r"Bāvīsatīnaṃ indriyānaṃ"),
    (r"vijjā", "ARTEFACT", r"အသိပညာ ဌာန",
     "other sense: vijjāṭṭhāna 'branch of learning' («အသိပညာ ဌာန»); the termbase vijjā is the true knowledge «အမှန်သိမြင်မှု»",
     r"vijjāṭṭhānesu"),
    (r"yoga", "ARTEFACT", r"ဘေးကင်းရာ",
     "compound yogakkhema 'security' («ဘေးကင်းရာ», as ch4 yogakkhemakāmā «ဘေးကင်းမှု»); neither yoga sense (yokes, skill) applies",
     r"ayogakkhemakāmāni"),
    (r"mutta", "ARTEFACT", r"ဆီး ရှိ၏",
     "other sense: mutta = urine in the body-part list («ဆီး», ch7's own BODY32 item); the termbase has only the pearl "
     "(maṇisaṅkhamutta); the gap (H4) is fixed by L03", r'mutta"nti'),
    (r"sattā", "ARTEFACT", r"အသညသတ်",
     "proper name: Asaññasattā keeps the name (termbase asaññasattānaṃ «အသညသတ်»; decisions-A kept on purpose)", r"Asaññasattā"),
    (r"nimmāna", "ARTEFACT", r"နိမ္မာနရတီ",
     "proper name: Nimmānaratī keeps the name (termbase nimmānaratīnaṃ devānaṃ «နိမ္မာနရတီ နတ်»; decision nimmāna|0)",
     r"[Nn]immānaratī"),
    (r"dasa", "ARTEFACT", r"ဆယ်မျိုး",
     "compound with -vidhena: the count of kinds takes «မျိုး» («ဆယ်မျိုး»), not the classifier «ပါး» (pi-1 ARTEFACT row)",
     r"dasavidhena"),
    (r"soḷasa", "ARTEFACT", r"တစ်ထောင့်ခြောက်ရာ",
     "numeral compound «soḷasa vassasatāni» = sixteen hundred «တစ်ထောင့်ခြောက်ရာ» (decision Soḷasa|0: the other candidates "
     "carry the hundreds / thousands)", r"soḷasa vassasatāni"),
    (r"dvādasa", "ARTEFACT", r"ဆယ့်နှစ်လ",
     "compound dvādasamāsiyo «ဆယ့်နှစ်လ» (the month count joins the measure word «လ»)", r"dvādasamāsiyo"),
    (r"Soḷasa", "ARTEFACT", r"ဆယ့်ခြောက်ကမ္ဘာ",
     "measure word: «Soḷasa kappā» = «ဆယ့်ခြောက်ကမ္ဘာ», as every lifespan line («… ကမ္ဘာ», e.g. «ခြောက်ဆယ့်လေးကမ္ဘာ»): "
     "kappa is its own classifier, «ပါး» is not used", r"Soḷasa kappā"),
    (r"Soḷasa|Vīsati|kappasahassāni|sahassāni", "ARTEFACT", r"ကမ္ဘာ (?:တစ်သောင်းခြောက်ထောင်|နှစ်သောင်း|နှစ်ထောင်)",
     "decision kappasahassāni|0 (OUTSIDE): the numeral joins kappasahassāni («ကမ္ဘာ နှစ်ထောင်», «ကမ္ဘာ နှစ်သောင်း», «ကမ္ဘာ "
     "တစ်သောင်းခြောက်ထောင်»)", r"kappasahassāni"),
    # ARTEFACT: termbase conflict (undecided entry vs a decided entry the rails apply; termbase doubts)
]
CONFLICT = [  # (keyword regex, decided headword|sense applied, what)
    (r".*ānupassanāniddeso", "niddeso|0", "the undecided heading entries keep «… ဖွင့်ဆိုချက်»; H19"),
    (r"[Aa]tricchatā|[Mm]ahicchatā", "icchatā|0", "the undecided entries keep «လိုချင်…» (kamyatā's word)"),
    (r"attānudiṭṭhi", "ānudiṭṭhi|0", "the decision names attānudiṭṭhi"),
    (r"adhammacariyā", "adhamma|0", "pi-1 locked adhamma «မတရားသော»"),
    (r"upekkhupavicārā|[Uu]pekkhāṭṭhāniy\w*", "Upekkhā|0", "pi-1 locked upekkhā «ဥပေက္ခာ»"),
    (r"kusītavatthūni|kusītavatthu", "vatthu|0", "the vatthu gloss names kusītavatthu"),
    (r"kāye kāyānupassī", "kāyānupassī viharati|0", "H12: one form"),
    (r"rājūhi", "rāja|0", "«one word with rājā»"),
    (r"sahajātaṃ", "jātaṃ|0", "the decision: «sahajātaṃ then reads «အတူ မွေးဖွားပြီးသော»»"),
    (r"anābhogā", "ābhogo|0", "H18: one set; «ဆင်ခြင်ခြင်း» is paccavekkhaṇā's verb"),
    (r"vipattiṃ", "vipatti|0", "pi-1 locked vipatti"),
    (r"bhajiṃsu", "bhajati|0", "«one word with bhajanti»"),
    (r"iriyāpatha|iriyāpathassa", "iriyāpathaṃ|0", "«a word Burmese readers know»"),
    (r"paṭibhānaṃ", "paṭibhāna|0", "31 of 32 uses"),
    (r"iddhiṃ", "Iddhi|0", "pi-1 locked iddhi"),
    (r"Lābhasakkārasilokasannissit\w+", "sakkāra|0", "pi-1 locked sakkāra"),
    (r"mānaṃ paṭilabhati|chandaṃ paṭilabhati|diṭṭhiṃ paṭilabhati", "paṭilabhati|0", "«same lemma as paṭilābho»"),
]


def segs(d):
    out = {}
    for p in sorted(d.glob("*.md")):
        buf = []
        for l in N(p.read_text(encoding="utf-8")).splitlines():
            if not l.strip():
                continue
            buf.append(l)
            m = A.ID.search(l)
            if m:
                out[m.group(1)] = (p.name.split("-")[0].split(".")[0], " ".join(buf))
                buf = []
    return out


def pali_ok(check, text):
    if check is None:
        return True
    if check.startswith("!"):
        return re.search(check[1:], text) is None
    return re.search(check, text) is not None


def misses(path):
    out = []
    for l in open(path, encoding="utf-8"):
        f = N(l).rstrip("\n").strip().split("\t")
        if len(f) == 3 and f[0][:1].isdigit():
            out.append(tuple(f))
    return out


def applied_ids():
    ids = set()
    for name in ("layer-log.tsv", "apply-log.tsv"):
        for l in open(HERE / name, encoding="utf-8").read().splitlines()[1:]:
            ids.update(re.findall(r"\b([LR]\d\d)\b", l.split("\t")[-1][:4]))
    return ids


def kmap():
    kv = {}
    for l in open(KMAP, encoding="utf-8"):
        m = re.match(r"^\[([^\]]+)\] (.*)$", N(l.strip()))
        if m:
            for x in m.group(2).split(", "):
                if "=" in x:
                    k, v = x.split("=", 1)
                    kv[(m.group(1), k)] = v
    return kv


def decided():
    d = {}
    for l in open(DEC, encoding="utf-8"):
        f = N(l).rstrip("\n").split("\t")
        if len(f) >= 2 and "|" in f[0] and not f[0].startswith("#"):
            d[f[0]] = f[1]
    return d


def main():
    tb = A.parse_termbase(TB)
    P, Z, R = segs(PALI), segs(ZS), segs(RL)
    done, KV, DECI = applied_ids(), kmap(), decided()
    zs = misses(HERE / "adherence-zeroshot.txt")
    rl = misses(HERE / "adherence-rails.txt")
    zkeys = {(i, k) for i, k, _ in zs}
    rkeys = {(i, k) for i, k, _ in rl}
    todo = [(r, "zeroshot") for r in zs] + [(r, "rails") for r in rl if (r[0], r[1]) not in zkeys]
    rows, counts, bad = [], {}, 0
    for (i, kw, term), src in todo:
        ch, zt = Z[i]
        rt, pt = R[i][1], P[i][1]
        left = (i, kw) in rkeys
        text = rt if left or src == "rails" else zt
        row = None
        if not left and src == "zeroshot":                      # fixed in the rails: must be a GENUINE family
            lid, old = FAM.get(kw), KV.get((i, kw), "")
            fixed = any(A.occurs(t, rt) for t in tb.get(kw.lower(), []))
            gap = old.startswith("(no direct")
            seen = (old and not gap and (A.occurs(old, zt) or re.sub(r"(?:သည်|၏)$", "", old) in zt)) or (gap and not any(A.occurs(t, zt) for t in tb.get(kw.lower(), [])))
            if lid and lid in done and fixed and seen:
                row = (i, kw, term, old, "GENUINE", f"{lid}: zero-shot «{old}» → termbase «{term}»")
        if row is None and (left or src == "rails"):
            for rkw, cls, form, reason, pcheck in OTHER:
                if re.fullmatch(rkw, kw):
                    fm = re.search(form, text)
                    if fm and pali_ok(pcheck, pt):
                        row = (i, kw, term, fm.group(0), cls, reason)
                        break
            if row is None:
                for rkw, dkey, what in CONFLICT:
                    dterm = DECI.get(dkey)
                    if re.fullmatch(rkw, kw) and dterm and A.occurs(dterm, rt) and \
                            re.search(rf"(?i){re.escape(kw.split()[-1])}", pt):
                        row = (i, kw, term, dterm, "ARTEFACT",
                               f"termbase conflict: the undecided entry «{term}» keeps the zero-shot form; the rails apply the "
                               f"decided {dkey} «{dterm}» ({what}); termbase doubt")
                        break
        if row is None:
            row = (i, kw, term, "", "UNVERIFIED", "no class")
        bad += row[4] == "UNVERIFIED"
        counts[row[4]] = counts.get(row[4], 0) + 1
        rows.append(row + (ch, src))
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("id\tkeyword\ttermbase term\ttext form\tclass\treason\tch\tsrc\n")
        for r in rows:
            f.write("\t".join(r) + "\n")
    nz = sum(1 for r in rows if r[7] == "zeroshot")
    print(f"{nz} zero-shot misses + {len(rows) - nz} rails-introduced:",
          ", ".join(f"{k} {v}" for k, v in sorted(counts.items())))
    for r in rows:
        if r[4] == "UNVERIFIED":
            print("UNVERIFIED", r[0], r[1], r[7], "|", r[2])
    sys.exit(1 if bad else 0)


main()
