"""English->Pali keyword map for pi-1 chapters 4-01-nikkhepakandam and 4-02-nikkhepakandam.

usage: python -I -X utf8 map_4-01_4-02.py [--dump]
Writes <ch>.mapped.md next to <ch>.keywords.md. Conventions: map-conventions.md (incl. section 8).

Resolution order per (segment, keyword), keyword looked up lowercased (case variants share a value):
  1. OV[segment]   per-segment literal values (segments read one by one)
  2. blocks        literal values for the recurring synonym strings (dosa, lobha, moha, ...), applied
                   to the segments listed with each block
  3. CTX           context rules: English phrase regex -> Pali candidates. Multiword keywords take the
                   context that occurs first in the English; single words collect every context found
                   and join different Pali words with " / " (conventions 4); None = no direct equivalent
  4. G             generic Pali candidates (regexes), earliest match in the segment's Pali wins
                   (conventions 4: first occurrence of the lemma)
A candidate is a regex (value = the matched text) or (regex, value) where value is a string (its first
letter follows the case of the match) or a function of the match. Pali spans never contain ", ": a
comma inside a span is dropped (span values like "vacīkammaṃ manokammaṃ").
"""
import pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
PALI = ROOT / "AI_translation" / "pali" / "pi-1_split_chapters"
ENG = ROOT / "AI_translation" / "english" / "pi-1-english-plain-zeroshot_split_chapters"
NDE = "(no direct equivalent)"
ID = re.compile(r"\s*\^([0-9A-Za-z-]+)\s*$")
CHS = ["4-01-nikkhepakandam", "4-02-nikkhepakandam"]


def segments(path, strip_brackets=True):
    segs, buf = {}, []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        mm = ID.search(line)
        buf.append(line[:mm.start()] if mm else line)
        if mm:
            t = " ".join(buf)
            if strip_brackets:
                t = re.sub(r"\[[^\]]*\]", " ", t)
            t = re.sub(r"^#+\s*|\s#+\s", " ", t)
            segs[mm.group(1)] = re.sub(r"\s+", " ", t).strip()
            buf = []
    return segs


def cap(v, m):
    s = m.group(0)
    if s[:1].isupper() and v[:1].islower():
        return v[0].upper() + v[1:]
    return v


def find(cands, pali):
    """earliest match of any candidate -> (pos, value) or None"""
    best = None
    for i, c in enumerate(cands):
        if isinstance(c, tuple):
            rx, val = c
        else:
            rx, val = c, None
        m = re.search(rx, pali, re.I)
        if not m:
            continue
        if val is None:
            v = m.group("v") if "v" in m.re.groupindex else m.group(0)
        elif callable(val):
            v = val(m)
        else:
            v = cap(val, m)
        v = v.replace(",", "").replace(";", "")
        v = re.sub(r"\s+", " ", v).strip()
        key = (m.start(), i)
        if best is None or key < best[0]:
            best = (key, v)
    return None if best is None else (best[0][0], best[1])


def eng_rx(kw):
    return r"(?<![\w-])" + re.escape(kw) + r"(?![\w-])"


# ======================================================================= generic candidates
FORM = [r"saṅkhār(?:esu|e|ā|a)"]
RUPA = [r"\brūpaṃ", r"rūpa(?=kkhandh)", r"rūpassa", r"\brūpā\b", r"rūpasmiṃ"]
MAGGA = [r"\bmagg(?:o|aṃ|ā)\b", (r"magg(?=ārammaṇ|ādhipat)", "magga"), r"magga(?=[a-zāīūṅ])"]
G = {
    "aggregate": [r"khandh[oā]\b", r"khandha(?=dhātu)"],
    "aggregates": [r"khandhā\b", r"khandha(?=dhātu)"],
    "aggregate of feeling": [r"vedanākkhandh[oā]\b"],
    "aggregate of perception": [r"saññākkhandh[oā]\b"],
    "aggregate of mental": [r"saṅkhārakkhandh[oā]\b"],
    "aggregate of consciousness": [r"viññāṇakkhandh[oā]\b"],
    "aggregate of material": [r"rūpakkhandh[oā]\b"],
    "feeling": [r"vedan(?:āya|aṃ|ā)"],
    "perception": [r"saññ(?:āya|aṃ|ā)"],
    "formations": FORM, "mental formations": FORM,
    "consciousness": [r"viññāṇ(?:asmiṃ|aṃ|a)"],
    "material form": RUPA, "material": RUPA, "form": RUPA,
    "possessing material form": [r"rūpavantaṃ"], "possessing": [r"\w+vantaṃ"],
    # spheres
    "sense sphere": [r"kāmāvacara(?=het)", r"kāmāvacar[āe]\b"],
    "sense": [(r"kāmā(?=vacar)", "kāma")],
    "sphere": [(r"(?<=kām|rūp)āvacar(ā|e|a)(?=\b|het)", lambda m: "avacar" + m.group(1))],
    "fine-material sphere": [r"(?<!a)rūpāvacara(?=het)", r"(?<!a)rūpāvacar[āe]\b"],
    "fine-material": [(r"(?<!a)rūpā(?=vacar)", "rūpa")],
    "immaterial sphere": [r"arūpāvacara(?=het)", r"arūpāvacar[āe]\b"],
    "immaterial": [(r"arūpā(?=vacar)", "arūpa")],
    "plane": [r"bhūmiyaṃ"],
    "except": [r"ṭhapetvā"],
    "paths": [r"\bmaggā\b"],
    "paths not included": [r"apariyāpannā maggā", r"maggā apariyāpannā"],
    "fruits": [r"phalāni"],
    "element": [r"\bdhātu\b"],
    "unconditioned": [r"asaṅkhat\w+"],
    "unconditioned element": [r"asaṅkhatā (?:ca )?dhātu"],
    "functional": [r"\bkiriyā\b", (r"kiriy(?=ābyākat)", "kiriya")],
    # kusala triad
    "wholesome": [r"\bkusal(?:ā|ānaṃ|esu)\b", r"\bkusala(?=mūl|het)", (r"\bkusal(?=ākusal|ābyākat)", "kusala")],
    "unwholesome": [r"\bakusal(?:ā|ānaṃ|esu)\b", r"\bakusala(?=mūl|het)",
                    (r"(?<=kusal)ākusalānaṃ", "akusalānaṃ"), (r"(?<=kusal)ākusalā\b", "akusalā"),
                    (r"(?<=kusal)ākusal(?=ābyākat)", "akusala"), (r"(?<=\bn)ākusalā", "akusalā")],
    "indeterminate": [r"\babyākatā\b", r"\babyākata(?=het)", (r"(?<=kusal)ābyākatā", "abyākatā"),
                      (r"(?<=kiriy)ābyākatesu", "abyākatesu")],
    "wholesome states": [r"dhammā kusalā\b", r"\bkusalānaṃ (?:vā )?dhammānaṃ", r"\bkusalā dhammā"],
    "unwholesome states": [r"dhammā akusalā\b", (r"(?<=kusal)ākusalānaṃ dhammānaṃ", "akusalānaṃ dhammānaṃ"),
                           (r"(?<=kusal)ākusalā dhammā", "akusalā dhammā"), r"\bakusalānaṃ dhammānaṃ"],
    "indeterminate states": [r"dhammā abyākatā\b", (r"(?<=kusal)ābyākatā dhammā", "abyākatā dhammā"),
                             (r"(?<=kiriy)ābyākatesu vā dhammesu", "abyākatesu vā dhammesu")],
    "indeterminate states subject": [r"sāsavā kusal\w*ābyākatā dhammā"],
    "unwholesome states subject": [r"sāsavā kusalākusalā dhammā"],
    "unwholesome and indeterminate": [(r"(?<=kusal)ākusalābyākatā", "akusalābyākatā")],
    "wholesome nor unwholesome": [r"kusalā nākusalā"],
    "remaining wholesome": [(r"avasesā (?:sāsavā )?kusal(?=ākusal)", lambda m: m.group(0) + "a")],
    "remaining": [r"\bavases\w+"],
    "whatever": [r"\b(?:yañca|yaṃ|yā|yo)\b"],
    "kind": [r"evarūp\w+"],
    "therein": [r"\btattha\b"],
    # relation formulas
    "associated": [r"sampayutt(?:anti|añca|ā|o)"],
    "dissociated": [r"vippayutt(?:anti|ā|o)"],
    "states dissociated": [r"dhammā \w*vippayuttā"],
    "relation": [r"tehi dhammehi"],
    "subject to taints": [r"sāsavā\b"],
    "taints": [r"āsavā\b", r"āsava(?=[sv])"],
    "taint": [r"āsavo\b"],
    "free": [r"anāsavā"], "free of taints": [r"anāsavā"], "states free": [r"dhammā anāsavā"],
    "dissociated from taints": [r"āsavavippayuttā"],
    "dissociated from fetters": [r"saṃyojanavippayuttā"],
    "dissociated from ties": [r"ganthavippayuttā"],
    "dissociated from hindrances": [r"nīvaraṇavippayuttā"],
    "dissociated from clinging": [r"upādānavippayuttā"],
    "dissociated from defilements": [r"kilesavippayuttā"],
    "dissociated from misapprehension": [r"parāmāsavippayuttā"],
    "dissociated from mind": [r"cittavippayuttā"],
    "fetters but subject": [r"saṃyojanavippayuttā saṃyojaniyā"],
    "ties but subject": [r"ganthavippayuttā ganthaniyā"],
    "hindrances but subject": [r"nīvaraṇavippayuttā nīvaraṇiyā"],
    "clinging but subject": [r"upādānavippayuttā upādāniyā"],
    "defilements but subject": [r"kilesavippayuttā saṃkilesikā"],
    "fetters and subject": [r"saṃyojanā ceva saṃyojaniyā"],
    "ties and subject": [r"ganthā ceva ganthaniyā"],
    "hindrances and subject": [r"nīvaraṇā ceva nīvaraṇiyā"],
    "clinging and subject": [r"upādānā ceva upādāniyā"],
    "fetters are states": [r"saṃyojanāni"], "hindrances are states": [r"nīvaraṇāni"],
    "clinging are states": [r"upādānāni"], "defilements are states": [r"kilesā\b"],
    "states are fetters": [r"dhammā saṃyojanā\b"],
    "subject to fetters": [r"saṃyojaniyā"], "subject to ties": [r"ganthaniyā"],
    "subject to hindrances": [r"nīvaraṇiyā"], "subject to clinging": [r"upādāniyā"],
    "subject to defilement": [r"saṃkilesikā"], "subject to floods": [r"oghaniyā"],
    "subject to yokes": [r"yoganiyā"],
    "states not subject": [r"dhammā (?:asaṃyojaniyā|aganthaniyā|anīvaraṇiyā|anupādāniyā|asaṃkilesikā)\b"],
    "fetters": [r"saṃyojanā\b", r"saṃyojanāni", r"saṃyojana(?=[sv])", r"saṃyojaniyā"],
    "fetter": [r"saṃyojanaṃ", r"saṃyojanañceva"],
    "ties": [r"ganthā\b", r"gantha(?=[sv])", r"ganthaniyā"],
    "tie": [r"gantho\b"],
    "hindrances": [r"nīvaraṇā\b", r"nīvaraṇāni", r"nīvaraṇa(?=[sv])", r"nīvaraṇiyā"],
    "hindrance": [r"nīvaraṇaṃ", r"nīvaraṇañceva"],
    "clinging": [r"upādānā\b", r"upādānāni", r"upādāna(?=[sv])", r"upādāniyā", r"upādānaṃ"],
    "kinds": [r"upādānā\b", r"upādāna(?=[sv])", r"upādāniyā"],
    "kinds of clinging": [r"upādānā\b", r"upādāna(?=[sv])", r"upādāniyā"],
    "defilements": [r"kilesā\b", r"kilesa(?=[sv]\w*yutt)"],
    "defilement": [r"saṃkilesikā", r"kileso\b", r"kilesa(?=vatth)"],
    "defiled": [r"saṃkiliṭṭh(?:ā|a)"], "undefiled": [r"asaṃkiliṭṭh(?:ā|a)"],
    "defiled states": [r"dhammā saṃkiliṭṭhā"], "undefiled states": [r"dhammā asaṃkiliṭṭhā"],
    "misapprehensions": [r"parāmāsā\b"],
    "misapprehension": [r"parāmās(?:o|aṃ|ena)\b", r"parāmāsa(?=[sv])"],
    "misapprehended": [r"parāmaṭṭh(?:ā|o)\b"],
    "misapprehended states": [r"dhammā parāmaṭṭhā"],
    # fetter / taint / tie / hindrance / clinging names
    "taint of sensual": [r"kāmāsav\w+"], "taint of existence": [r"bhavāsav\w+"],
    "taint of views": [r"diṭṭhāsav\w+"], "taint of ignorance": [r"avijjāsav\w+"],
    "fetter of sensual": [r"kāmarāgasaṃyojan\w+"], "fetter of aversion": [r"paṭighasaṃyojan\w+"],
    "fetter of conceit": [r"mānasaṃyojan\w+"], "fetter of views": [r"diṭṭhisaṃyojan\w+"],
    "fetter of doubt": [r"vicikicchāsaṃyojan\w+"],
    "fetter of misapprehension": [r"sīlabbataparāmāsasaṃyojan\w+"],
    "fetter of lust": [r"bhavarāgasaṃyojan\w+"], "fetter of envy": [r"issāsaṃyojan\w+"],
    "fetter of stinginess": [r"macchariyasaṃyojan\w+"], "fetter of ignorance": [r"avijjāsaṃyojan\w+"],
    "bodily tie": [r"kāyagantho"],
    "tie of covetousness": [r"abhijjhā ?kāyagant\w+"], "tie of ill": [r"byāpādo kāyagantho"],
    "tie of misapprehension": [r"sīlabbataparāmās\w+ kāyagant\w+"],
    "tie of dogmatic": [r"idaṃ ?saccābhiniveso kāyagantho"],
    "hindrance of sensual": [r"kāmacchandanīvaraṇ\w+"], "hindrance of ill": [r"byāpādanīvaraṇ\w+"],
    "hindrance of sloth": [r"thinamiddhanīvaraṇ\w+"],
    "hindrance of restlessness": [r"uddhacca(?:kukkucca)?nīvaraṇ\w+"],
    "hindrance of remorse": [r"kukkuccanīvaraṇ\w+"],
    "hindrance of doubt": [r"vicikicchānīvaraṇ\w+"], "hindrance of ignorance": [r"avijjānīvaraṇ\w+"],
    "clinging to sensual": [r"kāmupādān\w+"], "clinging to views": [r"diṭṭhupādān\w+"],
    "clinging to rules": [r"sīlabbatupādān\w+"],
    "called the taint": [r"vuccati \w*āsavo"], "called the fetter": [r"vuccati \w*saṃyojanaṃ"],
    "called the bodily": [r"vuccati (?:\w+ )?kāya(?=gantho)"],
    "called the hindrance": [r"vuccati \w*nīvaraṇaṃ"], "called clinging": [r"vuccati \w*upādānaṃ"],
    # three fetters
    "identity": [(r"sakkāya(?=diṭṭhi)", "sakkāya")], "identity view": [r"sakkāyadiṭṭhi"],
    "doubt": [r"vicikicchā(?=saṃyoj|nīvar)", r"vicikicch(?:ā|āya)\b"],
    "misapprehension of rules": [r"sīlabbataparāmās(?:o|aṃ|ena)\b", r"sīlabbataparāmāsa(?=\w)"],
    "rules and observances": [(r"sīlabbat(?=a|u)", "sīlabbata"), r"sīlabbatena"],
    "rules": [(r"sīla(?=bbat)", "sīla"), r"sīlena"],
    "observances": [(r"(?<=sīla)bbat(?=a|u)", "vata"), r"vatena"],
    "view": [r"diṭṭhi", (r"diṭṭh(?=āsav|upādān)", "diṭṭhi")],
    "views": [r"diṭṭhi", (r"diṭṭh(?=āsav|upādān)", "diṭṭhi")],
    "wrong view": [r"micchādiṭṭhi"], "wrong views": [r"micchādiṭṭhi"],
    "seeing": [r"dassanena"],
    "abandoned": [r"pahātabbā\b", r"pahātabba(?=het)"],
    "abandoned by development": [r"bhāvanāya pahātabbā\b", r"bhāvanāya pahātabba(?=het)"],
    "states whose roots": [r"dhammā [^?–.]*?pahātabbahetukā"],
    "roots": [r"mūlāni", r"hetū\b", (r"hetu(?=[sv])", "hetu"), r"hetukā"],
    "wholesome roots": [r"kusalamūlāni", r"\bkusalahetū"],
    "unwholesome roots": [r"akusalamūlāni", r"akusalahetū"],
    "indeterminate roots": [r"abyākatahetū"],
    "non-greed": [r"alobho"], "non-hate": [r"adoso"], "non-delusion": [r"amoho"],
    "greed": [r"\blobh(?:o|ena)\b"], "hate": [r"\bdos(?:o|ena)\b"], "delusion": [r"\bmoh(?:o|ena)\b"],
    # kamma / tadekaṭṭha
    "bodily action": [r"kāyakammaṃ"], "verbal action": [r"vacīkammaṃ"], "mental action": [r"manokammaṃ"],
    "bodily": [(r"kāya(?=kamm|gantho|viññatti)", "kāya")],
    "verbal": [(r"vacī(?=kamm|viññatti)", "vacī")],
    "action and mental": [r"vacīkammaṃ,? manokammaṃ"],
    "action arising": [(r"(?<=taṃ)samuṭṭhānaṃ kāyakammaṃ", None)],
    "mental action arising": [(r"(?<=taṃ)samuṭṭhānaṃ kāyakammaṃ,? vacīkammaṃ,? manokammaṃ", None)],
    "arising": [(r"(?<=taṃ)samuṭṭhānaṃ", None), r"samudaye"],
    "occur": [r"ekaṭṭh[āo]"],
    "defilements that occur": [r"ekaṭṭhā ca kilesā"],
    # views string (diṭṭhi ... vipariyāsaggāho)
    "holding views": [r"diṭṭhigataṃ"], "thicket": [r"(?<=diṭṭhi)gahanaṃ"], "wilderness": [r"kantāro"],
    "contortion": [r"visūkāyikaṃ"], "vacillation": [r"vipphanditaṃ"], "grasping": [r"\bgāho\b"],
    "fixation": [r"paṭiggāho", r"patiṭṭhāho"], "adherence": [r"\babhiniveso"], "road": [r"(?<=kum)maggo"],
    "wrong path": [r"micchāpatho"], "wrongness": [r"micchatt(?:aṃ|a)"],
    "sectarian": [(r"titth(?=āyatan)", "tittha")], "doctrines": [(r"titth(?=āyatan)", "tittha")],
    "distorted": [r"vipariyāsa(?=g)"], "distorted grasp": [r"vipariyāsaggāho"],
    "grasp": [r"(?<=vipariyāsag)gāho"],
    # the ten views
    "eternal": [r"sassato"], "soul": [r"jīvaṃ"], "body": [r"sarīr\w+"], "thing": [r"\baññaṃ jīvaṃ"],
    "tathāgata exists": [r"hoti tathāgato"], "exists": [r"\bhoti\b"], "exist": [r"\bhoti\b"],
    "death": [r"maraṇ\w+"],
    # sakkāyadiṭṭhi body
    "uninstructed": [r"assutavā"], "ordinary": [r"puthujjano"], "person": [r"puthujjano"],
    "noble": [r"ariyānaṃ", r"ariya(?=magg|dhamm)"], "ones": [r"ariyānaṃ"],
    "unskilled": [r"akovido"], "undisciplined": [r"avinīto"], "teaching": [r"(?<=ariya)dhammassa"],
    "good people": [r"sappurisānaṃ"], "people": [(r"(?<=sap)purisānaṃ", "purisānaṃ")],
    "regards": [r"samanupassati"], "self": [r"attato"],
    # doubt string
    "teacher": [r"satthari"], "training": [r"sikkhāya"], "uncertain": [r"kaṅkhati"],
    "uncertainty": [r"\bkaṅkhā\b"], "perplexity": [r"vimati"], "indecision": [r"dveḷhakaṃ"],
    "forked": [r"dvedhāpatho"], "wavering": [r"saṃsayo"], "definite": [(r"(?<=an)ekaṃsa", "ekaṃsa")],
    "stand": [(r"(?<=anekaṃsag)gāho", "gāho")], "hesitation": [r"āsappanā"], "faltering": [r"parisappanā"],
    "fathom": [(r"(?<=a)pariyogāhanā", "pariyogāhanā")], "stiffness": [r"thambhitattaṃ"],
    "scratching": [(r"(?<=mano)vilekho", "vilekho")],
    "specific": [r"idappaccayatā"], "conditionality": [r"idappaccayatā"],
    "dependently": [(r"paṭicca(?=samuppann)", "paṭicca")],
    "dependently arisen": [r"paṭiccasamuppannesu"],
    "dependently arisen states": [r"paṭiccasamuppannesu dhammesu"],
    "arisen": [r"(?<=paṭicca)samuppannesu", r"uppannā"],
    "arisen states": [r"(?<=paṭicca)samuppannesu dhammesu", r"dhammā uppannā"],
    # knowledge strings
    "suffering": [r"dukkhe\b"], "knowledge of suffering": [r"dukkhe a?ñāṇaṃ"],
    "cessation": [(r"(?<=dukkha)nirodhe", "nirodhe")], "cessation of suffering": [r"dukkhanirodhe"],
    "knowledge": [(r"(?<=a)ññāṇaṃ", "ñāṇaṃ"), r"\bñāṇaṃ"],
    "lack of knowledge": [r"aññāṇaṃ"],
    "vision": [(r"(?<=a)dassanaṃ", "dassanaṃ")], "non-realisation": [r"anabhisamayo"],
    "understanding": [(r"(?<=an)anubodho", "anubodho"), r"pajānanā"],
    "awakening": [(r"(?<=a)sambodho", "sambodho"), (r"sambojjha(?=ṅg)", "sambojjha")],
    "non-penetration": [r"appaṭivedho"], "consider": [(r"(?<=a)samapekkhanā", "samapekkhanā")],
    "review": [(r"(?<=a)paccavekkhaṇā", "paccavekkhaṇā")],
    "oneself": [(r"(?<=a)paccakkhakammaṃ", "paccakkhakammaṃ")],
    "stupidity": [r"dummejjhaṃ"], "foolishness": [r"bālyaṃ"],
    "clear awareness": [(r"(?<=a)sampajaññaṃ", "sampajaññaṃ"), r"sampajaññaṃ"],
    "clear": [(r"(?<=a)sampajaññaṃ", "sampajaññaṃ"), r"sampajaññaṃ"],
    "awareness": [(r"(?<=a)sampajaññaṃ", "sampajaññaṃ"), r"sampajaññaṃ"],
    "deep": [r"pamoho"], "utter": [r"sammoho"], "ignorance": [r"avijjā"],
    "flood": [r"(?<=avijj)ogho", r"\bogho"], "yoke": [r"(?<=avijjā)yogo", r"\byogo"],
    "underlying": [(r"(?<=avijj)ānusayo", "anusayo"), r"\banusayo"],
    "tendency": [(r"(?<=avijj)ānusayo", "anusayo"), r"\banusayo"],
    "obsession": [r"pariyuṭṭhānaṃ"], "bar": [r"(?<=avijjā)laṅgī"],
    "root": [r"mūlaṃ"], "unwholesome root": [r"akusalamūlaṃ"], "wholesome root": [r"\bkusalamūlaṃ"],
    # wisdom string
    "wisdom": [r"\bpaññā\b"], "investigation": [r"\bvicayo"], "close investigation": [r"pavicayo"],
    "investigation of states": [r"dhammavicayo"], "discerning": [r"sallakkhaṇā"],
    "distinguishing": [r"\bupalakkhaṇā"], "differentiating": [r"paccupalakkhaṇā"],
    "learning": [r"paṇḍiccaṃ"], "skill": [r"kosallaṃ"], "subtlety": [r"nepuññaṃ"], "clarity": [r"vebhabyā"],
    "consideration": [r"cintā"], "examination": [r"upaparikkhā"], "breadth": [r"bhūrī"],
    "intelligence": [r"medhā"], "guidance": [r"pariṇāyikā"], "insight": [r"vipassanā"], "goad": [r"patodo"],
    "faculty": [(r"(?<=paññ)indriyaṃ", "indriyaṃ")], "faculty of wisdom": [r"paññindriyaṃ"],
    "power": [(r"(?<=paññā)balaṃ", "balaṃ")], "power of wisdom": [r"paññābalaṃ"],
    "sword": [(r"(?<=paññā)satthaṃ", "satthaṃ")], "sword of wisdom": [r"paññāsatthaṃ"],
    "tower": [(r"(?<=paññā)pāsādo", "pāsādo")], "tower of wisdom": [r"paññāpāsādo"],
    "light": [(r"(?<=paññā)āloko", "āloko")], "light of wisdom": [r"paññāāloko"],
    "radiance": [(r"(?<=paññā)obhāso", "obhāso")], "radiance of wisdom": [r"paññāobhāso"],
    "lamp": [(r"(?<=paññā)pajjoto", "pajjoto")], "lamp of wisdom": [r"paññāpajjoto"],
    "jewel": [(r"(?<=paññā)ratanaṃ", "ratanaṃ")], "jewel of wisdom": [r"paññāratanaṃ"],
    "right": [(r"sammā(?=diṭṭhi)", "sammā")],
    # object triads
    "mind and mental": [r"cittacetasikā"],
    "mental factors": [(r"(?<=citta)cetasikā", "cetasikā"), r"\bcetasikā"],
    "factors that arise": [r"uppajjanti cittacetasikā"],
    "arise": [r"uppādino", r"uppajj\w+"],
    "arise taking": [r"ārabbha ye uppajjanti"],
    "arise taking states": [r"dhamme ārabbha ye uppajjanti"],
    "taking": [r"ārabbha"],
    "taking states": [r"dhamme ārabbha"],
    "object": [r"ārammaṇā"],
    "states as object": [r"ārammaṇā"],
    "mind": [r"cittassa", r"\bcittaṃ", r"cittañca", r"cittena", r"\bcittā\b", (r"citta(?=\w)", "citta")],
    "together": [r"ekaṭṭh[āo]"],
}
for adj, p in (("limited", "paritt"), ("exalted", "mahaggat"), ("immeasurable", "appamāṇ"), ("past", "atīt"),
               ("future", "anāgat"), ("present", "paccuppann")):
    G[f"{adj} object"] = [rf"{p}ārammaṇā"]
    G[f"taking {adj} states"] = [rf"{p}e dhamme ārabbha"]
G["taking others' states"] = [r"bahiddhā dhamme ārabbha"]

# context rules: keyword -> [(english regex, [candidates] or None)]
CTX = {
    "mental": [(r"mental formations", FORM), (r"mental action", [(r"mano(?=kamm)", "mano")]),
               (r"mental factors", G["mental factors"]), (r"mental-object", [(r"dhamm(?=āyatan)", "dhamma")]),
               (r"mental hatred", [(r"mano(?=padoso)", "mano")]), (r"mental scratching", [(r"mano(?=vilekho)", "mano")]),
               (r"mental body", [r"kāyassa"]), (r"mental objects", [(r"dhamma(?=taṇhā)", "dhamma")])],
    "factors": [(r"mental factors", G["mental factors"]), (r"path factors", [(r"(?<=magg)aṅgāni", "aṅgāni")])],
    "wrong": [(r"wrong road", [r"kummaggo"]), (r"wrong (?:path|views?)", [(r"micchā(?=patho|diṭṭhi)", "micchā")])],
    "path": [(r"(?:wrong|forked) path", [r"(?<=micchā|dvedhā)patho"]),
             (r"(?<!wrong )(?<!forked )\bpath\b", MAGGA)],
    "existence": [(r"spheres of existence", None)],
    "spheres": [(r"spheres of existence", None)],
    "spheres of existence": [(r"spheres of existence", None)],
    "states subject": [(r"states subject to taints", [r"dhammā sāsavā\b", r"sāsavā kusal\w* dhammā"]),
                       (r"states subject to (?:fetters|ties|hindrances|clinging|defilement)",
                        [r"dhammā (?:saṃyojaniyā|ganthaniyā|nīvaraṇiyā|upādāniyā|saṃkilesikā)\b"])],
    "variant": [(r"variant", None)],
    "regard": [(r"with regard to", None)],
    "having": [(r"having", None)],
    "thought": [(r"at the thought", None)],
}


# ======================================================================= shared blocks
def blk(s):
    """'kw=val; kw=val' -> dict (values literal)"""
    d = {}
    for part in s.split(";"):
        part = part.strip()
        if part:
            k, v = part.split("=", 1)
            d[k.strip().lower()] = v.strip()
    return d


# lobha string (Yo rāgo sārāgo ... abhijjhā lobho akusalamūlaṃ)
LOBHA = blk("""lust=rāgo; passion=sārāgo; compliance=anunayo; accommodation=anurodho; delight=nandī;
 wanting=icchā; infatuation=mucchā; eagerness=gedho; intense=paligedho / pajappā; attachment=saṅgo; mire=paṅko;
 agitation=ejā; deceit=māyā; begetter=janikā; producer=sañjananī; seamstress=sibbinī; net-maker=jālinī;
 stream=saritā; entangler=visattikā; thread=suttaṃ; spreading=visaṭā; accumulator=āyūhinī; companion=dutiyā;
 aspiration=paṇidhi; conduit=netti; existence=bhava; forest=vanaṃ; undergrowth=vanatho; intimacy=santhavo;
 affection=sineho; concern=apekkhā; kinship=paṭibandhu; hope=āsā; hoping=āsisanā; visible=rūpa; forms=rūpa;
 visible forms=rūpa; sounds=sadda; smells=gandha; tastes=rasa; touches=phoṭṭhabba; wealth=dhana; children=putta;
 life=jīvita; hankering=jappā; extreme=abhijappā; act=jappanā; voracity=loluppaṃ; voracious=loluppāyanā;
 fawning=pucchañjikatā; wish=kamyatā; fine=sādhu; things=sādhu; unrighteous=adhamma; lawless=visama;
 liking=nikanti; desiring=nikāmanā; longing=patthanā; envying=pihanā; earnest=sampatthanā; sensual=kāma;
 craving=taṇhā; continued existence=bhava; non-existence=vibhava; fine-material=rūpa; immaterial=arūpa;
 cessation=nirodha; mental=dhamma; objects=dhamma; flood=ogho; yoke=yogo; tie=gantho; clinging=upādānaṃ;
 obstruction=āvaraṇaṃ; hindrance=nīvaraṇaṃ; covering=chādanaṃ; bond=bandhanaṃ; corruption=upakkileso;
 underlying=anusayo; tendency=anusayo; obsession=pariyuṭṭhānaṃ; creeper=latā; meanness=vevicchaṃ;
 root=mūlaṃ; suffering=dukkha; source=nidānaṃ; origin=pabhavo; snare=pāso; hook=baḷisaṃ; domain=visayo;
 river=nadī; leash=gaddulaṃ; ocean=samuddo; covetousness=abhijjhā; greed=lobho; unwholesome=akusala;
 unwholesome root=akusalamūlaṃ; mind=cittassa; whatever=Yo; therein=Tattha; variant=(no direct equivalent)""")

# dosa: frame "Anatthaṃ me acarīti āghāto jāyati ..." + string
DOSA = blk("""annoyance=āghāto; annoyance arises=āghāto jāyati; arises=jāyati; done=acarīti; doing=caratīti;
 harm=Anatthaṃ; dear=piyassa; someone=piyassa; pleasing=manāpassa; reason=aṭṭhāne; thought=(no direct equivalent);
 mind=cittassa; kind=evarūpo; whatever=Yo; resentment=paṭighāto; aversion=paṭighaṃ; antagonism=paṭivirodho;
 irritation=kopo; exasperation=pakopo; fury=sampakopo; hate=doso; hatred=padoso; intense=sampadoso;
 malice=byāpatti; mental=mano; anger=kodho; angry=kujjhanā; hating=dussanā; state of hating=dussitattaṃ;
 malicious=byāpajjanā; hostility=virodho; fierceness=caṇḍikkaṃ; abusiveness=asuropo; discontent=anattamanatā;
 therein=Tattha""")

# moha string (Dukkhe aññāṇaṃ ... avijjālaṅgī moho akusalamūlaṃ)
MOHA = blk("""lack=aññāṇaṃ / adassanaṃ / ananubodho / asambodho / asampajaññaṃ;
 failure=asaṃgāhanā / apariyogāhanā / asamapekkhanā / apaccavekkhaṇā / apaccakkhakammaṃ;
 lack of knowledge=aññāṇaṃ; knowledge of suffering=Dukkhe aññāṇaṃ; fathom=pariyogāhanā; kind=evarūpaṃ;
 delusion=moho; root=mūlaṃ; unwholesome=akusala; therein=Tattha""")

# paññā string (Dukkhe ñāṇaṃ ... sammādiṭṭhi)
PANNA = blk("""knowledge of suffering=Dukkhe ñāṇaṃ; knowledge=ñāṇaṃ; whatever=yā; kind=evarūpā;
 understanding=pajānanā; non-delusion=amoho; therein=Tattha; view=diṭṭhi""")

# kaṅkhā string (Satthari kaṅkhati vicikicchati ... manovilekho)
KANKHA = blk("""teacher=Satthari; teaching=dhamme; training=sikkhāya; uncertain=kaṅkhati; kind=evarūpā;
 failure=anekaṃsaggāho / apariyogāhanā; fathom=pariyogāhanā; mind=cittassa; mental=mano; therein=Tattha""")

# views string after "yā evarūpā": diṭṭhi diṭṭhigataṃ ... vipariyāsaggāho
DS = blk("""kind=evarūpā; whatever=yā; path=patho; therein=Tattha""")

# the ten views (Sassato lokoti vā ...)
VIEWS10 = blk("""eternal=Sassato; soul=jīvaṃ; body=sarīranti; thing=aññaṃ; exists=hoti; exist=hoti;
 tathāgata exists=hoti tathāgato; death=maraṇāti""")

# sakkāyadiṭṭhi body (Idha assutavā puthujjano ...)
SAKKAYA = blk("""uninstructed=assutavā; ordinary=puthujjano; person=puthujjano; noble=ariyānaṃ; ones=ariyānaṃ;
 unskilled=akovido; teaching=dhammassa; undisciplined=avinīto; good people=sappurisānaṃ; people=purisānaṃ;
 regards=samanupassati; self=attato; possessing=rūpavantaṃ; possessing material form=rūpavantaṃ;
 material form=rūpaṃ; material=rūpaṃ; form=rūpaṃ""")

# sensual-desire string (Yo kāmesu kāmacchando ... kāmajjhosānaṃ)
KAMA = blk("""whatever=Yo; regard=(no direct equivalent); pleasures=kāmesu; sensual pleasures=kāmesu;
 sensual desire=kāmacchando; desire=chando; sensual lust=kāmarāgo; lust=rāgo; delight=nandī; craving=taṇhā;
 affection=sineho; fever=pariḷāho; infatuation=mucchā; sensual=kāma; therein=Tattha""")

# existence string (Yo bhavesu bhavachando ... bhavajjhosānaṃ)
BHAVA = blk("""whatever=Yo; regard=(no direct equivalent); desire=chando; lust=rāgo; delight=nandī; craving=taṇhā;
 continued existence=bhava; affection=sineho; fever=pariḷāho; infatuation=mucchā; existence=bhava;
 therein=Tattha; variant=(no direct equivalent); bhavacchando=(no direct equivalent)""")

# māna string
MANA = blk("""conceit=māno; equal=sadiso; inferior=hīno; kind=evarūpo; conceiving=maññanā;
 conceived=maññitattaṃ; having=(no direct equivalent); loftiness=unnati; haughtiness=unnamo; flag-raising=dhajo;
 self-exaltation=sampaggāho; mind=cittassa; wish=kamyatā; fly=ketukamyatā; banner=ketu; therein=Tattha;
 variant=(no direct equivalent)""")

# "Idha ... samaṇabrāhmaṇānaṃ sīlena suddhi" frame of sīlabbataparāmāsa
SIL = blk("""outside=bahiddhā; ascetics=samaṇa; brahmins=brāhmaṇānaṃ; purification=suddhi;
 comes=(no direct equivalent); teaching=Ito""")

# the seven abhidhamma-pair relation formulas: nothing special beyond G

BLOCKS = []  # (dict, [segment ids])


def use(d, ids):
    BLOCKS.append((d, ids.split()))


use(LOBHA, "1-1065 1-1141 1-1236")
use(DOSA, "1-1066 1-1120 1-1142 1-1160 1-1237")
use(MOHA, "1-1067 1-1106 1-1128 1-1168 1-1238")
use(PANNA, "1-1063 1-1076")
use(KANKHA, "1-1008 1-1123 1-1167 1-1241 1-1263 1-1270")
use(DS, "1-1007 1-1009 1-1105 1-1122 1-1124 1-1143 1-1144 1-1181 1-1221 1-1222 1-1223 1-1240 "
        "1-1262 1-1264 1-1269 1-1271")
use(VIEWS10, "1-1105 1-1122 1-1181 1-1240")
use(SAKKAYA, "1-1007 1-1223 1-1262 1-1269")
use(KAMA, "1-1103 1-1119 1-1159 1-1220")
use(BHAVA, "1-1104 1-1125")
use(MANA, "1-1121 1-1239")
use(SIL, "1-1009 1-1124 1-1143 1-1222 1-1264 1-1271")

# ======================================================================= per-segment overrides
OV = {}


def ov(ids, s):
    for i in ids.split():
        OV.setdefault(i, {}).update(blk(s))


# ---------------------------------------------------------------- 4-01 headings
ov("1-3-0", "chapter=kaṇḍaṃ; summaries=Nikkhepa")
ov("1-3-1-0", "summary=nikkhepaṃ")
ov("1-3-2-0", "pairs=Duka; summary=nikkhepaṃ")
ov("1-3-2-1-0", "roots=Hetu")
ov("1-3-2-2-0 1-3-2-10-0", "intermediate=antara; intermediate pairs=antaradukaṃ; pairs=dukaṃ")
ov("1-3-2-3-0", "taints=Āsava")
ov("1-3-2-4-0", "fetters=Saṃyojana")
ov("1-3-2-5-0", "ties=Gantha")
ov("1-3-2-6-0", "floods=Ogha")
ov("1-3-2-7-0", "yokes=Yoga")
ov("1-3-2-8-0", "hindrances=Nīvaraṇa")
ov("1-3-2-9-0", "misapprehension=Parāmāsa")
ov("1-3-2-11-0", "clinging=Upādāna")
ov("1-3-2-12-0", "defilements=Kilesa")
ov("1-3-2-13-0", "closing=Piṭṭhi; pairs=dukaṃ")

# ---------------------------------------------------------------- 4-01 triads
ov("1-985", "mental=saṅkhāra / mano")
ov("1-986", "mental=saṅkhāra / mano; together=ekaṭṭhā")
ov("1-987", "wholesome=Kusala; mental=saṅkhāra")
ov("1-988", "pleasant=sukhāya; pleasant feeling=sukhāya vedanāya; feeling=vedanāya")
ov("1-989", "painful=dukkhāya; painful feeling=dukkhāya vedanāya; feeling=vedanāya")
ov("1-990", "painful=adukkhamasukhāya; pleasant=adukkhamasukhāya; painful nor pleasant=adukkhamasukhāya;"
            "feeling=vedanāya")
ov("1-991", "wholesome=Kusala")
ov("1-992", "states that produce=vipākadhammadhammā; produce=vipākadhamma; produce results=vipākadhamma;"
            "wholesome=Kusala")
ov("1-993", "produce=vipākadhamma; produce results=vipākadhamma")
ov("1-994", "states produced=dhammā upādiṇṇupādāniyā; action and subject=upādiṇṇupādāniyā;"
            "past action=upādiṇṇa; produced=upādiṇṇa; produced by past=upādiṇṇa; due to past=kammassa katattā;"
            "clinging=upādāniyā; subject to clinging=upādāniyā; whatever=yañca")
ov("1-995", "states not produced=dhammā anupādiṇṇupādāniyā; action but subject=anupādiṇṇupādāniyā;"
            "past action=upādiṇṇa; produced=upādiṇṇa; produced by past=upādiṇṇa; due to past=kammassa katattā;"
            "clinging=upādāniyā; subject to clinging=upādāniyā; whatever=yañca;"
            "states subject=Sāsavā kusalākusalā dhammā")
ov("1-996", "states neither produced=dhammā anupādiṇṇaanupādāniyā; past action=upādiṇṇa; produced=upādiṇṇa;"
            "produced by past=upādiṇṇa; clinging=upādāniyā; subject to clinging=upādāniyā")
ov("1-997", "defiled=saṃkiliṭṭha; defilement=saṃkilesikā; together=ekaṭṭhā")
ov("1-998", "undefiled=asaṃkiliṭṭha; defilement=saṃkilesikā; mental=saṅkhāra;"
            "states subject=Sāsavā kusalābyākatā dhammā")
ov("1-999", "undefiled=asaṃkiliṭṭha; defilement=saṃkilesikā; subject to defilement=saṃkilesikā")
ov("1-1000", "applied=vitakka; applied thought=vitakka; sustained=vicāra; sustained thought=vicāra;"
             "thought=vitakka / vicāra; states with applied=dhammā savitakkasavicārā")
ov("1-1001", "applied=vitakka; applied thought=vitakka; sustained=vicāra; sustained thought=vicāra;"
             "thought=vitakka / vicāra; states without applied=dhammā avitakkavicāramattā")
ov("1-1002", "applied=vitakka; applied thought=vitakka; sustained=vicāra; sustained thought=vicāra;"
             "thought=vitakka / vicāra; states without applied=dhammā avitakkaavicārā")
ov("1-1003", "accompanied=sahagatā; accompanied by rapture=pītisahagatā; rapture=pīti;"
             "states accompanied=dhammā pītisahagatā")
ov("1-1004", "accompanied=sahagatā; accompanied by happiness=sukhasahagatā; happiness=sukha;"
             "states accompanied=dhammā sukhasahagatā; mental=saṅkhāra")
ov("1-1005", "accompanied=sahagatā; accompanied by equanimity=upekkhāsahagatā; equanimity=upekkhā;"
             "states accompanied=dhammā upekkhāsahagatā; mental=saṅkhāra")
ov("1-1006 1-1013 1-1261 1-1268", "fetters=saṃyojanāni")
ov("1-1007", "variant=(no direct equivalent); fetter=saṃyojanaṃ; view=diṭṭhi; views=diṭṭhi;"
             "feeling=Vedanaṃ; perception=Saññaṃ; formations=Saṅkhāre; mental formations=Saṅkhāre;"
             "mental=Saṅkhāre; consciousness=Viññāṇaṃ; wrong=kummaggo / micchā")
ov("1-1008", "doubt=vicikicchā; arisen=samuppannesu; arisen states=samuppannesu dhammesu")
ov("1-1009", "wrong=kummaggo / micchā; rules=sīla; observances=vata")
ov("1-1010", "together=ekaṭṭhā; fetters=saṃyojanāni; mental=mano")
ov("1-1011", "together=ekaṭṭhā; mental=mano; remaining=Avaseso")
ov("1-1017", "together=ekaṭṭhā; fetters=saṃyojanāni; mental=mano; roots=hetukā")
ov("1-1018", "together=ekaṭṭhā; mental=mano; remaining=Avaseso; roots=hetukā")
ov("1-1019", "roots=hetukā")
ov("1-1020", "accumulation=ācaya; states leading=dhammā ācayagāmino; states subject=Sāsavā kusalākusalā dhammā")
ov("1-1021", "accumulation=caya; away=apacaya; states leading=dhammā apacayagāmino")
ov("1-1022", "accumulation=ācaya; away=apacaya; states leading=dhammā neva ācayagāmi")
ov("1-1023", "training=sekkhā; contemplative=sāmañña; life=sāmañña")
ov("1-1024", "beyond=asekkhā; training=sekkhā; highest=Upariṭṭhimaṃ; fruit=phalaṃ; arahantship=arahatta;"
             "variant=(no direct equivalent)")
ov("1-1025", "beyond=asekkhā; training=sekkhā")
ov("1-1026", "limited=parittā; limited states=dhammā parittā")
ov("1-1027", "exalted=mahaggatā; exalted states=dhammā mahaggatā")
ov("1-1028", "immeasurable=appamāṇā; immeasurable states=dhammā appamāṇā")
ov("1-1029", "limited=paritta; limited states=Paritte dhamme; mind=citta; mental=cetasikā; factors=cetasikā")
ov("1-1030", "exalted=mahaggata; exalted states=Mahaggate dhamme; mind=citta; mental=cetasikā; factors=cetasikā")
ov("1-1031", "immeasurable=appamāṇa; immeasurable states=Appamāṇe dhamme; mind=citta; mental=cetasikā;"
             "factors=cetasikā")
ov("1-1032", "inferior=hīnā; inferior states=dhammā hīnā; together=ekaṭṭhā")
ov("1-1033", "middling=majjhimā; middling states=dhammā majjhimā; states subject=Sāsavā kusalābyākatā dhammā")
ov("1-1034", "superior=paṇītā; superior states=dhammā paṇītā")
ov("1-1035", "actions=kammāni; immediate=ānantarikāni; fixed=niyatā; states fixed=dhammā micchattaniyatā;"
             "wrongness=micchatta; wrong=micchā; views=diṭṭhi; wrong views=micchādiṭṭhi")
ov("1-1036", "fixed=niyatā; states fixed=dhammā sammattaniyatā; rightness=sammatta")
ov("1-1037", "fixed=niyatā")
ov("1-1038", "path=magga; noble=Ariya; noble path=Ariyamaggaṃ; mind=citta; mental=cetasikā; factors=cetasikā")
ov("1-1039", "path=magga; root=hetukā; roots=hetū; belong=maggahetū; noble=Ariya; noble path=Ariyamagga;"
             "possesses=samaṅgissa; factors=aṅgāni; right=sammā; view=diṭṭhi")
ov("1-1040", "path=magga; dominant=adhipatino; dominant factor=adhipatino; factor=adhipatino; noble=Ariya;"
             "noble path=Ariyamaggaṃ; possesses=samaṅgissa; develops=bhāvayantassa;"
             "develops the path=maggaṃ bhāvayantassa; inquiry=vīmaṃsā; mind=citta; mental=cetasikā;"
             "factors=cetasikā; arise=uppajjanti")
POS = ("born=jātā; produced=sañjātā; generated=nibbattā; fully generated=abhinibbattā; manifest=pātubhūtā;"
       "arisen=uppannā; fully arisen=samuppannā; risen=uṭṭhitā; fully risen=samuṭṭhitā;"
       "fully=abhinibbattā / samuppannā / samuṭṭhitā; heading=aṃsena; mental=saṅkhārā")
ov("1-1041", POS + "; arisen states=dhammā uppannā; editions=(no direct equivalent); variant=(no direct equivalent)")
ov("1-1042", POS)
ov("1-1045", POS + "; future states=dhammā anāgatā")
ov("1-1046", POS + "; present states=dhammā paccuppannā")
ov("1-1043", "arise=uppādino; bound=uppādino; ripened=avipakkavipākānaṃ; past action=kammassa;"
             "due to past=kammassa katattā; whatever=yañca; wholesome=Kusala")
ov("1-1044", "past states=dhammā atītā; ceased=niruddhā; gone=vigatā; changed=vipariṇatā;"
             "completely=abbhatthaṅgatā; arisen=uppajjitvā; having=(no direct equivalent); heading=aṃsena;"
             "mental=saṅkhārā")
ov("1-1047", "past states=Atīte dhamme; mind=citta; mental=cetasikā; factors=cetasikā")
ov("1-1048", "future states=Anāgate dhamme; mind=citta; mental=cetasikā; factors=cetasikā")
ov("1-1049", "present states=Paccuppanne dhamme; mind=citta; mental=cetasikā; factors=cetasikā")
ov("1-1050", "particular=tesaṃ tesaṃ; personal=paccattaṃ; bound=niyatā; individual=pāṭipuggalikā;"
             "produced=upādiṇṇā; produced by past=upādiṇṇā; past action=upādiṇṇā; mental=saṅkhārā")
ov("1-1051", "others=bahiddhā; others' states=dhammā bahiddhā; particular=tesaṃ tesaṃ;"
             "person=puggalānaṃ; personal=paccattaṃ; bound=niyatā; individual=pāṭipuggalikā;"
             "produced=upādiṇṇā; produced by past=upādiṇṇā; past action=upādiṇṇā; mental=saṅkhārā")
ov("1-1052", "others=bahiddhā")
ov("1-1053", "mind=citta; mental=cetasikā; factors=cetasikā")
ov("1-1054", "others=bahiddhā; others' states=bahiddhā; mind=citta; mental=cetasikā; factors=cetasikā")
ov("1-1055", "others=bahiddhā; others' states=bahiddhā; mind=citta; mental=cetasikā; factors=cetasikā")
ov("1-1056", "visible=sanidassana; make impact=sappaṭighā; visible-form=Rūpa; visible-form base=Rūpāyatanaṃ")
ov("1-1057", "invisible=anidassana; make impact=sappaṭighā; eye=Cakkhu; eye base=Cakkhāyatanaṃ; ear=sota;"
             "ear base=sotāyatanaṃ; nose=ghāna; nose base=ghānāyatanaṃ; tongue=jivhā;"
             "tongue base=jivhāyatanaṃ; body=kāya; body base=kāyāyatanaṃ; sound=sadda;"
             "sound base=saddāyatanaṃ; smell=gandha; smell base=gandhāyatanaṃ; taste=rasa;"
             "taste base=rasāyatanaṃ; touch=phoṭṭhabba; touch base=phoṭṭhabbāyatanaṃ")
RDH = ("invisible=anidassanaṃ; makes=appaṭighaṃ; makes no impact=appaṭighaṃ; mental-object=dhamma;"
       "mental-object base=dhammāyatana; whatever=yañca")
ov("1-1058", RDH + "; invisible=anidassana; mental=saṅkhāra / dhamma; material form=rūpaṃ; material=rūpaṃ;"
                   "form=rūpaṃ")

# ---------------------------------------------------------------- 4-01 roots group
ov("1-1059", "roots=hetū; wholesome roots=kusalahetū; wholesome=kusala; unwholesome roots=akusalahetū;"
             "unwholesome=akusala; indeterminate roots=abyākatahetū; indeterminate=abyākata;"
             "sense sphere=kāmāvacarahetū; roots not included=apariyāpannahetū")
ov("1-1060 1-1073", "roots=hetū; wholesome roots=kusalahetū; wholesome=kusala")
ov("1-1061 1-1074", "whatever=Yo; non-greed=alobho; greedy=lubbhanā; lusting=sārajjanā; non-lust=asārāgo;"
                    "non-covetousness=anabhijjhā; wholesome root=kusalamūlaṃ; wholesome=kusala; root=mūlaṃ")
ov("1-1062 1-1075", "whatever=Yo; non-hate=adoso; hating=dussanā; loving-kindness=metti; loving=mettāyanā;"
                    "kindness=anuddā; kind=anuddāyanā; others=hitesitā; welfare=hita; sympathy=anukampā;"
                    "non-ill-will=abyāpādo; absence=abyāpajjo; malice=byāpajjo; wholesome root=kusalamūlaṃ;"
                    "wholesome=kusala; root=mūlaṃ")
ov("1-1063 1-1076", "roots=hetū; wholesome roots=kusalahetū; wholesome=kusala; arising=samudaye")
ov("1-1076", "awakening=sambojjha; factor=aṅgo; path=magga; path factor=maggaṅgaṃ")
ov("1-1064", "roots=hetū; unwholesome roots=akusalahetū; unwholesome=akusala")
ov("1-1067", "roots=hetū; unwholesome roots=akusalahetū; arising=samudaye")
ov("1-1068", "roots=hetū; indeterminate roots=abyākatahetū; indeterminate=abyākata;"
             "arising=vipākato; wholesome=Kusalānaṃ; wholesome states=Kusalānaṃ vā dhammānaṃ;"
             "functional=kiriya; indeterminate states=abyākatesu vā dhammesu")
ov("1-1069", "roots=hetū; sense sphere=kāmāvacarahetū; sense=kāma; sphere=avacara;"
             "wholesome roots=kusalahetū; wholesome=kusala; unwholesome roots=akusalahetū; unwholesome=akusala;"
             "indeterminate roots=abyākatahetū; indeterminate=abyākata")
ov("1-1070", "roots=hetū; fine-material sphere=rūpāvacarahetū; fine-material=rūpa; sphere=avacara;"
             "wholesome roots=kusalahetū; wholesome=kusala; indeterminate roots=abyākatahetū; indeterminate=abyākata")
ov("1-1071", "roots=hetū; immaterial sphere=arūpāvacarahetū; immaterial=arūpa; sphere=avacara;"
             "wholesome roots=kusalahetū; wholesome=kusala; indeterminate roots=abyākatahetū; indeterminate=abyākata")
ov("1-1072", "roots=hetū; roots not included=apariyāpannahetū; wholesome roots=kusalahetū; wholesome=kusala;"
             "indeterminate roots=abyākatahetū; indeterminate=abyākata")
ov("1-1077", "roots=hetū; indeterminate roots=abyākatahetū; indeterminate=abyākata; arising=vipākato;"
             "wholesome=Kusalānaṃ; wholesome states=Kusalānaṃ dhammānaṃ; roots not included=apariyāpannahetū")
ov("1-1078", "roots=hetū")
ov("1-1079", "roots=hetukā; states with roots=dhammā sahetukā")
ov("1-1080", "roots=hetukā; states without roots=dhammā ahetukā")
ov("1-1081", "roots=hetu")
ov("1-1082", "roots=hetu")
GM = "greed=Lobho; delusion=mohena; hate=doso; root=hetu; roots=hetū;" \
     "non-greed=alobho; non-hate=adoso; non-delusion=amoho"
ov("1-1083", GM + "; root through delusion=mohena hetu ceva sahetuko")
ov("1-1085", GM + "; associated=sampayuttā; root through delusion=mohena hetu ceva hetu")
ov("1-1084", "roots=hetukā")
ov("1-1086", "roots=hetu")
ov("1-1087", "roots=hetū")
ov("1-1088", "roots=hetū")

# ---------------------------------------------------------------- 4-01 short intermediate pairs
ov("1-1089", "aggregates=khandhā")
ov("1-1090", "states without conditions=dhammā appaccayā; element=dhātu; unconditioned=Asaṅkhatā;"
             "unconditioned element=Asaṅkhatā dhātu")
ov("1-1091", "conditioned=saṅkhatā; conditioned states=dhammā saṅkhatā; whatever=Yeva")
ov("1-1092", "unconditioned=asaṅkhatā; unconditioned states=dhammā asaṅkhatā; whatever=Yo")
ov("1-1093", "visible=sanidassanā; visible states=dhammā sanidassanā; visible-form=Rūpa;"
             "visible-form base=Rūpāyatanaṃ")
ov("1-1094", RDH + "; invisible=anidassanā; invisible states=dhammā anidassanā; eye=Cakkhu;"
                   "eye base=Cakkhāyatanaṃ; touch=phoṭṭhabba; touch base=phoṭṭhabbāyatanaṃ")
ov("1-1095", "make impact=sappaṭighā; states that make=dhammā sappaṭighā; eye=Cakkhu;"
             "eye base=Cakkhāyatanaṃ; touch=phoṭṭhabba; touch base=phoṭṭhabbāyatanaṃ")
ov("1-1096", RDH + "; states that make=dhammā appaṭighā")
ov("1-1097", "material states=dhammā rūpino; material=rūpino; great elements=mahābhūtā; elements=bhūtā;"
             "derived=upādāya; form derived=upādāya rūpaṃ; material form derived=upādāya rūpaṃ;"
             "material form=rūpaṃ; form=rūpaṃ")
ov("1-1098", "immaterial=arūpino; immaterial states=dhammā arūpino")
ov("1-1099", "worldly=lokiyā; worldly states=dhammā lokiyā")
ov("1-1100", "transcend=uttarā; states that transcend=dhammā lokuttarā")
KEN = ("kinds=(no direct equivalent); consciousness=(no direct equivalent); know=viññeyyā; cannot=na;"
       "eye-consciousness=cakkhu; ear-consciousness=sota; nose-consciousness=ghāna; tongue-consciousness=jivhā;"
       "body-consciousness=kāya; states that eye-consciousness=dhammā cakkhu;"
       "states that ear-consciousness=dhammā sota; states that nose-consciousness=dhammā ghāna;"
       "states that tongue-consciousness=dhammā jivhā; states that body-consciousness=dhammā kāya")
ov("1-1101", KEN)

# ---------------------------------------------------------------- 4-01 taints
ov("1-1102 1-1114", "sensual=kāma; desire=kāma; sensual desire=kāma; existence=bhava; views=diṭṭhi;"
                    "ignorance=avijjā; taints=āsavā")
ov("1-1114", "sensual=Kāma; desire=Kāma; sensual desire=Kāma")
ov("1-1103", "sensual=kāma; sensual desire=kāma; desire=kāma / chando")
ov("1-1104", "taint=āsavo")
ov("1-1105", "views=diṭṭhi; view=diṭṭhi; wrong=kummaggo / micchā; wrong view=micchādiṭṭhi; kind=evarūpā")
ov("1-1106", "taints=āsavā; ignorance=avijjā")
ov("1-1112", "taints=āsavā; subject to taints=sāsavā")
ov("1-1113", "states subject=sāsavā kusalākusalābyākatā dhammā")
ov("1-1117", "chapter=kaṇḍe; summaries=Nikkhepa; recitation=bhāṇa; section=vāro;"
             "free=anāsavā; free of taints=anāsavā")

# ---------------------------------------------------------------- 4-01 fetters
TEN_F = ("ten=Dasa; sensual=kāma; sensual lust=kāmarāga; lust=rāga; aversion=paṭigha; conceit=māna;"
         "views=diṭṭhi; doubt=vicikicchā; misapprehension=parāmāsa; misapprehension of rules=sīlabbataparāmāsa;"
         "rules=sīla; observances=vata; rules and observances=sīlabbata; existence=bhava; envy=issā;"
         "stinginess=macchariya; ignorance=avijjā")
ov("1-1118", TEN_F)
ov("1-1136", TEN_F.replace("ten=Dasa;", "") + "; fetters=saṃyojanā; associated=sampayuttā; sensual=Kāma;"
             "sensual lust=Kāmarāga")
ov("1-1119", "sensual lust=kāmarāga; lust=rāga")
ov("1-1120", "aversion=paṭigha")
ov("1-1121", "conceit=māna")
ov("1-1122", "views=diṭṭhi; view=diṭṭhi; wrong=kummaggo / micchā; wrong view=micchādiṭṭhi; except=Ṭhapetvā;"
             "misapprehension=parāmāso; rules=sīla; observances=vata")
ov("1-1123", "doubt=vicikicchā; arisen=samuppannesu; arisen states=samuppannesu dhammesu")
ov("1-1124", "wrong=kummaggo / micchā; rules=sīla; observances=vata")
ov("1-1125", "lust=rāga; fetter of lust=bhavarāgasaṃyojanaṃ; desire=chando")
ov("1-1126", "envy=issā; envying=issāyanā; jealousy=usūyā; jealous=usūyanā; others=para; honour=sakkāra;"
             "respect=garukāra; reverence=mānana; salutation=vandana; veneration=pūjanāsu; whatever=Yā;"
             "variant=(no direct equivalent)")
ov("1-1127", "stinginess=macchariya; kinds=macchariyāni; dwellings=āvāsa; families=kula; praise=vaṇṇa;"
             "teaching=dhamma; whatever=Yaṃ; kind=evarūpaṃ; stingy=maccharāyanā; meanness=vevicchaṃ;"
             "miserliness=kadariyaṃ; tight-fistedness=kaṭukañcukatā; tightness=aggahitattaṃ; mind=cittassa")
ov("1-1128", "fetters=saṃyojanā; states are fetters=dhammā saṃyojanā; ignorance=avijjā")
ov("1-1134", "fetters=saṃyojanā; fetters are states=saṃyojanāni")

# ---------------------------------------------------------------- 4-01 ties
FOUR_T = ("covetousness=abhijjhā; bodily=kāya; tie=gantho; ill=byāpādo; dogmatic=abhiniveso; belief=abhiniveso; true=sacca; alone=(no direct equivalent)")
ov("1-1140", FOUR_T + "; ties=ganthā; tie of dogmatic=idaṃ saccābhiniveso kāyagantho")
ov("1-1152", FOUR_T + "; ties=ganthā; associated=sampayuttā")
ov("1-1141", "tie=gantho; covetousness=abhijjhā")
ov("1-1142", "ill=byāpādo; done=acarī")
ov("1-1143", "wrong=kummaggo / micchā; rules=sīla; observances=vata; misapprehension=parāmāso")
ov("1-1144", "wrong=kummaggo / micchā; wrong view=micchādiṭṭhi; views=diṭṭhi; view=diṭṭhi; except=Ṭhapetvā;"
             "dogmatic=abhiniveso; belief=abhiniveso; true=sacca; alone=(no direct equivalent);"
             "anything=moghamaññanti; else=moghamaññanti; false=moghamaññanti; body=sarīraṃ; death=maraṇā;"
             "eternal=Sassato; soul=jīvaṃ; thing=aññaṃ; exists=hoti; exist=hoti; tathāgata exists=hoti tathāgato;"
             "ties=ganthā; misapprehension=parāmāso; rules=sīla; observances=vata")
ov("1-1150", "ties=ganthā")

# ---------------------------------------------------------------- 4-02 hindrances
SIX_H = ("hindrances=nīvaraṇā; hindrance=nīvaraṇaṃ; sensual=kāma; sensual desire=kāmacchanda; desire=chanda;"
         "ill=byāpāda; sloth=thina; torpor=middha; restlessness=uddhacca; remorse=kukkucca; doubt=vicikicchā;"
         "ignorance=avijjā")
ov("1-1158", SIX_H + "; variant=(no direct equivalent)")
ov("1-1176", SIX_H + "; associated=sampayuttā; sensual=Kāma; sensual desire=Kāmacchanda")
ov("1-1159", "sensual desire=kāmacchanda; desire=chanda")
ov("1-1160", "ill=byāpāda")
ov("1-1161", "sloth=thina; torpor=middha")
ov("1-1162 1-1242", "whatever=Yā; mind=cittassa; indisposition=akallatā; unworkability=akammaññatā;"
                    "drooping=olīyanā; sagging=sallīyanā; sluggishness=līnaṃ; sluggish=līyanā; sloth=thinaṃ;"
                    "slothful=thiyanā; slothful state=thiyitattaṃ")
ov("1-1163", "whatever=Yā; mental body=kāyassa; body=kāyassa; mental=kāyassa; indisposition=akallatā;"
             "unworkability=akammaññatā; enveloping=onāho; inner=antosamorodho; confinement=antosamorodho;"
             "torpor=middhaṃ; sleep=soppaṃ; drowsiness=pacalāyikā; sleeping=supanā; asleep=supitattaṃ;"
             "sloth=thinaṃ")
ov("1-1164", "restlessness=uddhacca; remorse=kukkucca")
ov("1-1165 1-1243", "whatever=Yaṃ; mind=cittassa / cetaso; restlessness=uddhaccaṃ; disquiet=avūpasamo;"
                    "distraction=vikkhepo; agitation=bhantattaṃ")
ov("1-1166", "perceiving=saññitā; allowable=kappiye; blameless=avajje; blameworthy=vajja; remorse=kukkuccaṃ;"
             "whatever=Yaṃ; kind=evarūpaṃ; remorseful=kukkuccāyanā; regret=vippaṭisāro; mind=cetaso;"
             "mental=mano; scratching=vilekho; restlessness=uddhacca")
ov("1-1167", "doubt=vicikicchā; arisen=samuppannesu; arisen states=samuppannesu dhammesu")
ov("1-1168", "hindrances=nīvaraṇā; ignorance=avijjā")
ov("1-1174", "hindrances=nīvaraṇā")

# ---------------------------------------------------------------- 4-02 misapprehension
ov("1-1180", "misapprehensions=parāmāsā; misapprehension=parāmāso; views=Diṭṭhi")
ov("1-1181", "misapprehensions=parāmāsā; misapprehension=parāmāso; views=diṭṭhi; view=diṭṭhi;"
             "wrong=kummaggo / micchā; wrong view=micchādiṭṭhi")
ov("1-1187", "misapprehensions=parāmāsā; misapprehension=parāmāso; misapprehended=parāmaṭṭhā")

# ---------------------------------------------------------------- 4-02 long intermediate pairs
ov("1-1191", "object=ārammaṇā; mental=saṅkhāra")
ov("1-1192", "object=ārammaṇā")
ov("1-1193", "mind=cittā / mano; eye-consciousness=Cakkhuviññāṇaṃ; ear-consciousness=sotaviññāṇaṃ;"
             "nose-consciousness=ghānaviññāṇaṃ; tongue-consciousness=jivhāviññāṇaṃ;"
             "body-consciousness=kāyaviññāṇaṃ; mind element=manodhātu; element=dhātu;"
             "mind-consciousness=manoviññāṇa; mind-consciousness element=manoviññāṇadhātu")
ov("1-1194", "mind=cittā; mental=saṅkhāra")
ov("1-1195", "mental factors=cetasikā; mental=cetasikā / saṅkhāra; factors=cetasikā")
ov("1-1196", "mental factors=cetasikā; mental=cetasikā; factors=cetasikā; mind=Cittañca")
ov("1-1197", "associated=sampayuttā; mind=citta; mental=saṅkhāra")
ov("1-1198", "dissociated=vippayuttā; states dissociated=dhammā cittavippayuttā; mind=citta;"
             "associated=sampayuttanti; described=vattabbaṃ")
ov("1-1199", "joined=saṃsaṭṭhā; states joined=dhammā cittasaṃsaṭṭhā; joined with mind=cittasaṃsaṭṭhā; mind=citta;"
             "mental=saṅkhāra")
ov("1-1200", "joined=saṃsaṭṭhā; states not joined=dhammā cittavisaṃsaṭṭhā; joined with mind=cittavisaṃsaṭṭhā;"
             "mind=citta; described=vattabbaṃ")
ov("1-1201", "arising=samuṭṭhānā; states arising=dhammā cittasamuṭṭhānā; arising from mind=cittasamuṭṭhānā;"
             "mind=citta; mental=saṅkhāra; bodily=kāya; bodily intimation=kāyaviññatti; verbal=vacī;"
             "verbal intimation=vacīviññatti; intimation=viññatti; whatever=yaṃ; born=cittajaṃ; caused=cittahetukaṃ;"
             "visible-form=rūpa; visible-form base=rūpāyatanaṃ; sound=sadda; sound base=saddāyatanaṃ;"
             "smell=gandha; smell base=gandhāyatanaṃ; taste=rasa; taste base=rasāyatanaṃ; touch=phoṭṭhabba;"
             "touch base=phoṭṭhabbāyatanaṃ; space=ākāsa; space element=ākāsadhātu; water=āpo;"
             "water element=āpodhātu; element=dhātu; lightness=lahutā; lightness of material=rūpassa lahutā;"
             "pliancy=mudutā; pliancy of material=rūpassa mudutā; workability=kammaññatā;"
             "workability of material=rūpassa kammaññatā; growth of material=rūpassa upacayo;"
             "continuity=santati; continuity of material=rūpassa santati; edible=kabaḷīkāro;"
             "edible food=kabaḷīkāro āhāro; food=āhāro")
NOTM = ("mind=Cittañca; remaining=avasesañca; remaining material=avasesañca rūpaṃ;"
        "remaining material form=avasesañca rūpaṃ")
ov("1-1202", NOTM + "; arising=samuṭṭhānā; arising from mind=cittasamuṭṭhānā;"
                    "states not arising=dhammā no cittasamuṭṭhānā")
ov("1-1203", "existing=cittasahabhuno; together=cittasahabhuno; states existing=dhammā cittasahabhuno; mind=citta;"
             "mental=saṅkhāra; bodily=kāya; bodily intimation=kāyaviññatti; verbal=vacī;"
             "verbal intimation=vacīviññatti; intimation=viññatti")
ov("1-1204", NOTM + "; existing=cittasahabhuno; together=cittasahabhuno;"
                    "states not existing=dhammā no cittasahabhuno")
ov("1-1205", "accompanying=anuparivattino; accompanying mind=cittānuparivattino;"
             "states accompanying=dhammā cittānuparivattino; states accompanying mind=dhammā cittānuparivattino;"
             "mind=citta; mental=saṅkhāra; bodily=kāya; bodily intimation=kāyaviññatti; verbal=vacī;"
             "verbal intimation=vacīviññatti; intimation=viññatti")
ov("1-1206", NOTM + "; accompanying=anuparivattino; accompanying mind=cittānuparivattino;"
                    "states not accompanying=dhammā no cittānuparivattino")
ov("1-1207", "joined=saṃsaṭṭha; arising=samuṭṭhānā; arising from mind=cittasaṃsaṭṭhasamuṭṭhānā; mind=citta;"
             "states joined=dhammā cittasaṃsaṭṭhasamuṭṭhānā; mental=saṅkhāra")
ov("1-1208", "joined=saṃsaṭṭha; arising=samuṭṭhānā; arising from mind=cittasaṃsaṭṭhasamuṭṭhānā; mind=citta;"
             "states not joined=dhammā no cittasaṃsaṭṭhasamuṭṭhānā")
ov("1-1209", "joined=saṃsaṭṭha; arising=samuṭṭhāna; existing=sahabhuno; together=sahabhuno; mind=citta;"
             "states joined=dhammā cittasaṃsaṭṭhasamuṭṭhānasahabhuno; mental=saṅkhāra")
ov("1-1210", "joined=saṃsaṭṭha; arising=samuṭṭhāna; existing=sahabhuno; together=sahabhuno; mind=citta;"
             "states not joined=dhammā no cittasaṃsaṭṭhasamuṭṭhānasahabhuno")
ov("1-1211", "joined=saṃsaṭṭha; arising=samuṭṭhāna; accompanying=anuparivattino;"
             "accompanying mind=cittasaṃsaṭṭhasamuṭṭhānānuparivattino; mind=citta;"
             "states joined=dhammā cittasaṃsaṭṭhasamuṭṭhānānuparivattino; mental=saṅkhāra")
ov("1-1212", "joined=saṃsaṭṭha; arising=samuṭṭhāna; accompanying=anuparivattino;"
             "accompanying mind=cittasaṃsaṭṭhasamuṭṭhānānuparivattino; mind=citta;"
             "states not joined=dhammā no cittasaṃsaṭṭhasamuṭṭhānānuparivattino")
ov("1-1213", "internal=ajjhattikā; internal states=dhammā ajjhattikā; eye=Cakkhu; eye base=Cakkhāyatanaṃ;"
             "mind=mano; mind base=manāyatanaṃ")
ov("1-1214", "external=bāhirā; external states=dhammā bāhirā; visible-form=Rūpa; visible-form base=Rūpāyatanaṃ;"
             "mental-object=dhamma; mental-object base=dhammāyatanaṃ")
ov("1-1215", "derived=upādā; derived states=dhammā upādā; eye=Cakkhu; eye base=Cakkhāyatanaṃ;"
             "edible=kabaḷīkāro; edible food=kabaḷīkāro āhāro; food=āhāro")
ov("1-1216", "derived=upādā; great elements=mahābhūtā; elements=bhūtā; mental=saṅkhāra")
ov("1-1217", "states produced=dhammā upādiṇṇā; past action=upādiṇṇā; produced=upādiṇṇā; produced by past=upādiṇṇā;"
             "due to past=kammassa katattā; whatever=yañca")
ov("1-1218", "states not produced=dhammā anupādiṇṇā; past action=upādiṇṇā; produced=upādiṇṇā;"
             "produced by past=upādiṇṇā; due to past=kammassa katattā; whatever=yañca;"
             "states subject=Sāsavā kusalākusalā dhammā")

# ---------------------------------------------------------------- 4-02 clinging
FOUR_C = ("clinging=upādānā; kinds=upādānā; kinds of clinging=upādānā; sensual=kāma; pleasures=kāma;"
          "sensual pleasures=kāma; views=diṭṭhi; rules=sīla; observances=vata; rules and observances=sīlabbata;"
          "doctrine=vāda; self=atta")
ov("1-1219", FOUR_C + "; variant=(no direct equivalent)")
ov("1-1231", FOUR_C + "; views=Diṭṭhi; associated=sampayuttā; kind=upādānañceva; kind of clinging=upādānañceva;"
                      "pleasures with clinging=kāmupādānaṃ diṭṭhupādānena")
ov("1-1220", "clinging=upādānaṃ; sensual=kāma; sensual pleasures=kāma; pleasures=kāma")
ov("1-1221", "clinging=upādānaṃ; views=diṭṭhi; view=diṭṭhi; wrong=kummaggo / micchā; wrong view=micchādiṭṭhi;"
             "except=Ṭhapetvā; clinging to rules=sīlabbatupādānañca; doctrine=vāda; self=atta;"
             "rules=sīla; observances=vata; rules and observances=sīlabbata;"
             "nothing=Natthi; exist=Natthi; sacrificed=hutaṃ; fruit=phalaṃ; bad=dukkaṭānaṃ; actions=kammānaṃ;"
             "mother=mātā; father=pitā; beings=sattā; spontaneously=opapātikā; reborn=opapātikā;"
             "ascetics=samaṇa; brahmins=brāhmaṇā; gone=gatā; rightly=sammā; practise=paṭipannā;"
             "having=(no direct equivalent); realised=sacchikatvā; direct=abhiññā; direct knowledge=abhiññā;"
             "knowledge=abhiññā; known=pavedentīti; variant=(no direct equivalent)")
ov("1-1222", "clinging=upādānaṃ; rules=sīla; observances=vata; wrong=kummaggo / micchā")
ov("1-1223", "clinging=upādānaṃ; kinds=upādānā; kinds of clinging=upādānā; doctrine=vāda; self=atta;"
             "wrong=kummaggo / micchā; feeling=Vedanaṃ; perception=saññaṃ; formations=saṅkhāre;"
             "mental formations=saṅkhāre; mental=saṅkhāre; consciousness=viññāṇaṃ")
ov("1-1229", "clinging=upādānā; clinging are states=upādānāni; kinds=upādānā; kinds of clinging=upādānā")
ov("1-1230 1-1232", "kinds=upādānā; kinds of clinging=upādānā")
ov("1-1234", "chapter=kaṇḍe; summaries=Nikkhepa; recitation=bhāṇa; section=vāro")

# ---------------------------------------------------------------- 4-02 defilements
TEN_K = ("ten=Dasa; bases=vatthūni; defilement=kilesa; defilements=kilesā; greed=lobho; hate=doso; delusion=moho;"
         "conceit=māno; view=diṭṭhi; doubt=vicikicchā; sloth=thinaṃ; restlessness=uddhaccaṃ;"
         "shamelessness=ahirīkaṃ; fearlessness=anottappaṃ; fearlessness of wrongdoing=anottappaṃ;"
         "wrongdoing=anottappaṃ")
ov("1-1235", TEN_K)
ov("1-1257", TEN_K.replace("ten=Dasa; bases=vatthūni; defilement=kilesa;", "defilement=kileso;")
   .replace("shamelessness=ahirīkaṃ", "shamelessness=ahirikaṃ")
   + "; associated=sampayuttā; greed=Lobho; restlessness with fearlessness=uddhaccaṃ anottappena;"
     "restlessness with shamelessness=uddhaccaṃ ahirikena; shamelessness with fearlessness=ahirikaṃ anottappena;"
     "shamelessness with restlessness=ahirikaṃ uddhaccena; wrongdoing with restlessness=anottappaṃ uddhaccena;"
     "wrongdoing with shamelessness=anottappaṃ ahirikena")
ov("1-1239", "conceit=māno")
ov("1-1240", "views=diṭṭhi; view=diṭṭhi; wrong=kummaggo / micchā; wrong view=micchādiṭṭhi")
ov("1-1241", "doubt=vicikicchā; arisen=samuppannesu; arisen states=samuppannesu dhammesu")
ov("1-1244", "shamelessness=ahirikaṃ; ashamed=hirīyati; bad=pāpakānaṃ; unwholesome=akusalānaṃ;"
             "unwholesome states=akusalānaṃ dhammānaṃ; engaging=samāpattiyā")
ov("1-1245", "fearlessness=anottappaṃ; fearlessness of wrongdoing=anottappaṃ; wrongdoing=anottappaṃ;"
             "fear=ottappitabbena; fearing=ottappati; bad=pāpakānaṃ; unwholesome=akusalānaṃ;"
             "unwholesome states=akusalānaṃ dhammānaṃ; engaging=samāpattiyā; defilements=kilesā")
ov("1-1249", "defiled=saṃkiliṭṭhā; defiled states=dhammā saṃkiliṭṭhā; together=ekaṭṭhā; mental=mano")
ov("1-1250", "undefiled=asaṃkiliṭṭhā; undefiled states=dhammā asaṃkiliṭṭhā; wholesome=Kusala")
ov("1-1253", "defilements=kilesā; defilements are states=kilesā; defilement=saṃkilesikā")
ov("1-1255", "defilements=kilesā; defilements are states=kilesā; defiled=saṃkiliṭṭhā")
ov("1-1256", "defiled=saṃkiliṭṭhā; defilements=kilesā")

# ---------------------------------------------------------------- 4-02 closing pairs
ov("1-1262 1-1269", "view=diṭṭhi; views=diṭṭhi; feeling=Vedanaṃ; perception=saññaṃ; formations=saṅkhāre;"
                    "mental formations=saṅkhāre; mental=saṅkhāre; consciousness=viññāṇaṃ")
ov("1-1263 1-1270", "doubt=vicikicchā; uncertain=kaṅkhati; scratching=vilekho")
ov("1-1264", "fetters=saṃyojanāni; together=ekaṭṭhā; mental=mano; view=diṭṭhi; views=diṭṭhi; rules=sīla;"
             "observances=vata")
ov("1-1271", "fetters=saṃyojanāni; together=ekaṭṭhā; mental=mano; view=diṭṭhi; views=diṭṭhi; rules=sīla;"
             "observances=vata; roots=hetukā; greed=lobho; hate=doso; delusion=moho")
ov("1-1266", "together=ekaṭṭhā; mental=mano; remaining=Avaseso")
ov("1-1273", "together=ekaṭṭhā; mental=mano; remaining=Avaseso; roots=hetukā")
ov("1-1272 1-1274", "roots=hetukā")
ov("1-1275", "applied=vitakkā; applied thought=vitakkā; thought=vitakkā; states with applied=dhammā savitakkā")
ov("1-1276", "applied=vitakkā; applied thought=vitakkā; thought=vitakkā; states without applied=dhammā avitakkā")
ov("1-1277", "sustained=vicārā; sustained thought=vicārā; thought=vicārā; states with sustained=dhammā savicārā;"
             "mental=saṅkhāra")
ov("1-1278", "sustained=vicārā; sustained thought=vicārā; thought=vicārā;"
             "states without sustained=dhammā avicārā")
ov("1-1279", "rapture=pītikā; states with rapture=dhammā sappītikā")
ov("1-1280", "rapture=pītikā; states without rapture=dhammā appītikā")
ov("1-1281", "accompanied=sahagatā; accompanied by rapture=pītisahagatā; rapture=pīti;"
             "states accompanied=dhammā pītisahagatā")
ov("1-1282", "accompanied=sahagatā; accompanied by rapture=pītisahagatā; rapture=pīti;"
             "states not accompanied=dhammā na pītisahagatā")
ov("1-1283", "accompanied=sahagatā; accompanied by happiness=sukhasahagatā; happiness=sukha;"
             "states accompanied=dhammā sukhasahagatā; mental=saṅkhāra")
ov("1-1284", "accompanied=sahagatā; accompanied by happiness=sukhasahagatā; happiness=sukha;"
             "states not accompanied=dhammā na sukhasahagatā")
ov("1-1285", "accompanied=sahagatā; accompanied by equanimity=upekkhāsahagatā; equanimity=upekkhā;"
             "states accompanied=dhammā upekkhāsahagatā; mental=saṅkhāra")
ov("1-1286", "accompanied=sahagatā; accompanied by equanimity=upekkhāsahagatā; equanimity=upekkhā;"
             "states not accompanied=dhammā na upekkhāsahagatā")
ov("1-1287", "taking=karitvā; boundary=pariyantaṃ; hell=avicinirayaṃ; gods=deve; power=vasavattī;"
             "wield=vasavattī; creations=nimmita; others=para; sense=kāma / āyatanā; paranimmitavasavattideve=(no direct equivalent);"
             "variant=(no direct equivalent); whatever=yaṃ; aggregates=khandha; elements=dhātu; bases=āyatanā;"
             "sense bases=āyatanā; sense sphere=kāmāvacarā; sphere=avacarā; mental=saṅkhārā")
NOTK = "states not included=apariyāpannā"
ov("1-1288", NOTK)
ov("1-1290", NOTK)
ov("1-1292", NOTK)
RB = ("taking=karitvā; boundary=pariyantaṃ; gods=deve; whatever=yaṃ; mind=citta; mental=cetasikā; factors=cetasikā;"
      "mind and mental=cittacetasikā; mental factors=cetasikā; entered=samāpannassa; meditative=samāpannassa;"
      "attainment=samāpannassa; reborn=upapannassa; dwells=vihārissa; happily=sukha; life=diṭṭhadhamma")
ov("1-1289", RB + "; brahma=brahma; variant=(no direct equivalent)")
ov("1-1291", RB + "; base of infinite=ānañcāyatana; infinite=ānañca; space=ākāsa; perception=saññā;"
                  "non-perception=asaññā")
ov("1-1293", "states included=dhammā pariyāpannā")
ov("1-1294", "states not included=dhammā apariyāpannā; paths=Maggā")
ov("1-1295", "lead to liberation=niyyānikā; liberation=niyyānikā; states that lead=dhammā niyyānikā")
ov("1-1296", "lead to liberation=niyyānikā; liberation=niyyānikā")
ov("1-1297", "fixed=niyatā; fixed states=dhammā niyatā; actions=kammāni; immediate=ānantarikāni;"
             "wrong=micchā; wrong view=micchādiṭṭhi; view=diṭṭhi")
ov("1-1298", "fixed=niyatā")
ov("1-1299", "surpassable=sauttarā; surpassable states=dhammā sauttarā")
ov("1-1300", "unsurpassable=anuttarā; unsurpassable states=dhammā anuttarā")
ov("1-1301", "conflict=raṇā; states with conflict=dhammā saraṇā; together=ekaṭṭhā; mental=mano")
ov("1-1302", "conflict=raṇā; states without conflict=dhammā araṇā; abhidhamma=Abhidhamma; pairs=dukaṃ;"
             "wholesome=Kusala")
ov("1-1156", "floods=ogha; subject to floods=oghaniyā; states dissociated=dhammā oghavippayuttā")
ov("1-1157", "yokes=yoga; subject to yokes=yoganiyā; states dissociated=dhammā yogavippayuttā")


# ======================================================================= engine
def resolve(bid, kw, pali, eng, problems):
    k = kw.lower()
    if bid in OV and k in OV[bid]:
        return OV[bid][k]
    for d, ids in BLOCKS:
        if bid in ids and k in d:
            return d[k]
    if k in CTX and CTX[k]:
        hits = []
        for rx, cands in CTX[k]:
            me = re.search(rx, eng, re.I)
            if not me:
                continue
            if cands is None:
                hits.append((me.start(), None, None))
                continue
            r = find(cands, pali)
            if r is None:
                problems.append((bid, kw, f"context '{rx}' found in English but no Pali match"))
                continue
            hits.append((me.start(), r[0], r[1]))
        real = [h for h in hits if h[1] is not None]
        if not hits:
            pass
        elif not real:
            return NDE
        elif " " in k:
            return min(real)[2]
        else:
            vals = []
            for _, p, v in sorted(real, key=lambda h: h[1]):
                if v not in vals:
                    vals.append(v)
            return " / ".join(vals)
    if k in G:
        r = find(G[k], pali)
        if r:
            return r[1]
        problems.append((bid, kw, "generic: no Pali match"))
        return "???"
    problems.append((bid, kw, "no rule"))
    return "???"


def build(ch, dump=False):
    pali = segments(PALI / f"{ch}.md")
    eng = segments(ENG / f"{ch}.md", strip_brackets=False)
    src = (HERE / f"{ch}.keywords.md").read_text(encoding="utf-8").splitlines()
    out, problems = [], []
    for line in src:
        bid, rest = line.split("] ", 1)
        bid = bid[1:]
        kws = [k.strip() for k in rest.split(", ")]
        pairs = []
        for k in kws:
            v = resolve(bid, k, pali[bid], eng[bid], problems)
            assert ", " not in v, (bid, k, v)
            pairs.append(f"{v}={k}")
        out.append(f"[{bid}] " + ", ".join(pairs))
    (HERE / f"{ch}.mapped.md").write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")
    print(ch, "lines", len(out), "problems", len(problems))
    for p in problems:
        print("   ", *p)


if __name__ == "__main__":
    for ch in CHS:
        build(ch)
