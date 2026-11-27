"""Check the Burmese zero-shot of pi-6 group ch6-8 (6-01 / 6-02 Saṅkhārayamaka, 8 Cittayamaka) line by line.

usage: python3 -I -X utf8 check_ch6-8.py [--mutate]
Adapted from check_sample.py (approved sample):
  A. rebuild: make_ch6-8.py regenerates the three files byte for byte (nothing written here);
  B. per line: B1 structure (equal non-empty lines, dashes, «…», «[», item numbers, labels, block IDs, heading levels,
     no «?» «।» «:-», final «။», NFC, no U+1050-U+109F); B2 POLARITY: every Pāli negation (na, no, nuppajjati,
     natthi) is one Burmese negative (မဟုတ် / မရှိ / မ + verb / မရ / မထည့်ရ), fixed terms with a privative masked
     (abyākata, ahetuka, arūpa, avitakkaavicāra, anuttara, araṇa); B3 VERBS AND PARTICIPLES: the sequence of
     uppajj- / nirujjh- finite verbs (tense, polarity, «no ca» double negative) AND of the participles uppanna /
     uppajjamāna / nirujjhamāna / niruddha (polarity, double negative) of each line equals the Burmese sequence;
     Āmantā / Natthi counted; B4 (Ka) / (Kha) labels in order, every «vā pana» = «တစ်ဖန်»; B5 digits and number
     words (tayo, tīṇi, the jhāna ordinals, pañca- / catu- / eka-); B6 every recurring Pāli sentence has one and the
     same Burmese; B7 headings / colophons / table lines come out as their table value;
  C. reuse test against the FINAL pi-1 … pi-5 rails texts, read here independently of my6_formulas:
     C2 whole lines / headings / Āmantā found in pi-1 … pi-5; C3 every reused term of REUSE (witness: a rails segment
     has the Pāli and the Burmese) is present in every line whose Pāli has it. Documented exceptions apart.
  --mutate: also run a mutation test (in memory): a dropped «မ», a dropped «ခဲ့», «ပြီး» -> «ဆဲ», a dropped
     «မဟုတ်», a changed term, «တစ်ဖန်» dropped; each must be caught.
Prints the mismatches (0 expected) and the counts; exit 1 on any mismatch.
"""
import importlib
import pathlib
import re
import sys
import unicodedata

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
MK = importlib.import_module("make_ch6-8")
F = MK.F
ROOT = HERE.parents[3]
NAMES = MK.NAMES_OUT
HEAD = re.compile(r"^#+ ")


def nonempty(text):
    return [l for l in text.splitlines() if l.strip()]


def body(l):
    return F.strip_id(l).strip()


def nobr(s):
    return re.sub(r" ?\[[^\]]*\]", "", s)


PAIRS0 = {n: (nonempty((MK.PALI / n).read_text(encoding="utf-8-sig")),
              nonempty((MK.OUT / n).read_text(encoding="utf-8"))) for n in NAMES}

# ===================================================================================== B2 / B3 helpers
MASK = [F.ABY, F.AHETUKA, F.PLACES["arūpa"], MK.AVV[:-len("သော")], MK.QUAL["anuttaraṃ"], MK.QUAL["araṇaṃ"],
        MK.QUAL["araṇaṃ"][:-len(" စိတ်")]]


def p_neg(p):
    s = nobr(body(p))
    return (len(re.findall(r"(?<![\w])(?:na|no|No|Na)(?![\w])", s)) + len(re.findall(r"nuppajj", s))
            + len(re.findall(r"\b[Nn]atthi\b", s)))


def m_neg(m):
    s = nobr(body(m))
    for t in sorted(MASK, key=len, reverse=True):
        s = s.replace(t, "")
    return (s.count("မဟုတ်") + s.count("မရှိ") + s.count("မအခြေခံ") + s.count("မဖြစ်ပေါ်") + s.count("မချုပ်ငြိမ်း")
            + len(re.findall(r"မရ(?=[။)၊ ])", s)) + s.count("မထည့်ရ")
            + s.count("မပြုရ"))          # harmonise B15: «… na kātabbaṃ» = «…ဟု မပြုရ» (ch2-02-4-5 note wording)


SUBJ_P = r"(?:(?:tesaṃ tattha|tesaṃ|tassa taṃ|tassa|taṃ|tattha) (?:(?:" + MK.QUALS + r") )?(?:cittaṃ|\S+saṅkhāro) )?"
P_VERB = re.compile(r"(?P<noca>no ca " + SUBJ_P + r")?(?P<na>na (?:ceva |ca )?)?(?:(?P<n>n)?(?P<r>uppajj|nirujjh)"
                    r"(?P<e>issanti|issati|issatīti|ittha|itthāti|attha|anti|ati|atīti)\b|(?<![\w])(?P<pp>uppann|niruddh|"
                    r"uppajjamān|nirujjhamān)(?:aṃ|anti|añceva|añca)(?![\w]))", re.I)
P_END = {"issanti": "fut", "issati": "fut", "issatīti": "fut", "ittha": "past", "itthāti": "past", "attha": "past",
         "anti": "pres", "ati": "pres", "atīti": "pres"}
P_PP = {"uppann": ("uppajj", "pp"), "niruddh": ("nirujjh", "pp"), "uppajjamān": ("uppajj", "prp"),
        "nirujjhamān": ("nirujjh", "prp")}
M_VERB = re.compile(r"(?<!ပြန်လည် )(?:(?P<r2>ဖြစ်ပေါ်|ချုပ်ငြိမ်း)(?P<k>ပြီး|ဆဲ)(?:လည်း)?"
                    r"(?: ခဏ ခဏကို လွန်မြောက်ပြီး ကာလ ကျော်လွန်ပြီး)?(?:သော|(?: (?P<pol>ဖြစ်|မဟုတ်)(?P<ns2>သည်ကား မဟုတ်)?))?"
                    r"|(?P<neg>မ)?(?P<r>ဖြစ်ပေါ်|ချုပ်ငြိမ်း)(?!လာ|ခြင်း|ပြီး|ဆဲ)(?:ကြ)?(?P<t>ခဲ့|လိမ့်မည်|မည့်)?"
                    r"(?P<ns>(?:သည်)?ကား မဟုတ်)?)")
M_ROOT = {"ဖြစ်ပေါ်": "uppajj", "ချုပ်ငြိမ်း": "nirujjh"}
M_T = {None: "pres", "ခဲ့": "past", "လိမ့်မည်": "fut", "မည့်": "fut"}


def p_verbs(s):
    out = []
    for x in P_VERB.finditer(s):
        noca = bool(x["noca"])
        if x["pp"]:
            root, kind = P_PP[x["pp"].lower()]
            neg = bool(x["na"])
            out.append((root, kind, neg or noca, neg and noca))
        else:
            neg = bool(x["na"] or x["n"])
            out.append((x["r"].lower(), P_END[x["e"]], neg or noca, neg and noca))
    return out


def m_verbs(s):
    out = []
    for y in M_VERB.finditer(s):
        if y["r2"]:
            kind = "pp" if y["k"] == "ပြီး" else "prp"
            out.append((M_ROOT[y["r2"]], kind, y["pol"] == "မဟုတ်", bool(y["ns2"])))
        else:
            out.append((M_ROOT[y["r"]], M_T[y["t"]], bool(y["neg"]), bool(y["ns"])))
    return out


NUMW = [(r"\b(?:Tīṇeva|Tayo eva|Tayo)\b", "သုံးပါး"), (r"\btīṇi\b", "သုံးခု"),
        (r"pañca(?=kkhandh|vokār)|Pañca(?=kkhandh|vokār)", "ငါးပါး"), (r"[Cc]atu(?=vokār)", "လေးပါး"),
        (r"[Ee]ka(?=vokār)", "တစ်ပါး"), (r"[Pp]aṭhamajjhān", "ပထမ"), (r"[Dd]utiy", "ဒုတိယ"),
        (r"[Tt]atiyajjhān", "တတိယ"), (r"[Cc]atutthajjhān", "စတုတ္ထ")]


def canon(s):
    s = F.LABEL_RE.sub("", s.strip())
    s = re.sub(r"nti\?$", "ṃ?", s)
    s = re.sub(r"(?<=[āaoe])ti\?$", "?", s)
    s = re.sub(r"īti\?$", "i?", s)
    s = re.sub(r"āti\?$", "a?", s)
    return s.replace("ti. ", "? ") if s.endswith("ti.") else s


# ===================================================================================== C. FINAL texts, read here
ID_RE = re.compile(r" (\^[0-9A-Za-z-]+)\s*$")


def blocks(text):
    res, cur = {}, []
    for line in text.splitlines():
        if not line.strip():
            continue
        cur.append(line)
        mm = ID_RE.search(line)
        if mm:
            res[mm.group(1)] = cur
            cur = []
    return res


FIN, FIN_LINE = {}, {}
for bk in "12345":
    pd = ROOT / f"AI_translation/pali/pi-{bk}_split_chapters"
    bd = ROOT / f"AI_translation/burmese/pi-{bk}-burmese-plain-rails_split_chapters"
    d = {}
    for f in sorted(pd.glob("*.md")):
        if not (bd / f.name).exists():
            continue
        pb = blocks(f.read_text(encoding="utf-8-sig"))
        bb = blocks(unicodedata.normalize("NFC", (bd / f.name).read_text(encoding="utf-8-sig")))
        for k, v in pb.items():
            d[k] = (v, bb.get(k, []))
            for x, y in zip(v, bb.get(k, [])):
                FIN_LINE.setdefault(re.sub(r"^#+ ", "", body(x)), set()).add(re.sub(r"^#+ ", "", body(y)))
    FIN[bk] = d

# (regex on the Pāli line, Burmese that must be in the Burmese line, book, block id, Pāli witness in that segment)
REUSE = [
    (r"kāyasaṅkhār", MK.KAYA_S, "5", "^5-458", "kāyasaṅkhāro"),
    (r"vacīsaṅkhār", MK.VACI_S, "5", "^5-458", "vacīsaṅkhāro"),
    (r"cittasaṅkhār", MK.CITTA_S, "5", "^5-458", "cittasaṅkhāro"),
    (r"assāsapassās", "ဝင်လေ ထွက်လေ", "5", "^5-333", "assāsapassāsā"),
    (r"(?<![\w])vitakkavicār", "စတင်ကြံစည်မှုနှင့် ဆက်လက်သုံးသပ်မှု", "5", "^5-332", "Vitakkavicārā"),
    (r"savitakkasavicār", "စတင်ကြံစည်မှုနှင့် ဆက်လက်သုံးသပ်မှု ရှိ", "1", "^1-M1-6", "savitakkasavicārā"),
    (r"avitakkaavicār", "စတင်ကြံစည်မှုလည်း မရှိ၊ ဆက်လက်သုံးသပ်မှုလည်း မရှိ", "1", "^1-1401", "avitakkaavicārā"),
    (r"bhūmiyaṃ", "ရှိရာ အဆင့်၌", "1", "^1-988", "Sukhabhūmiyaṃ"),
    (r"uppādakkhaṇ", "ဖြစ်ခြင်း ခဏ", "5", "^5-366", "Uppādakkhaṇe"),
    (r"bhaṅgakkhaṇ", "ပြိုပျက်ခြင်း ခဏ", "5", "^5-366", "bhaṅgakkhaṇe"),
    (r"\bvinā\b", "မပါဘဲ", "5", "^5-227", "vinā rūpena"),
    (r"samaṅgīnaṃ", "နှင့် ပြည့်စုံ", "2", "^2-809", "kāyaduccaritasamaṅgī"),
    (r"\banantarā\b", "၏ ချက်ချင်း နောက်၌", "5", "^5-687", "anantarā"),
    (r"citte vattamāne", "စိတ် ဖြစ်နေစဉ်", "5", "^5-556", "citte vattamāne"),
    (r"nirodhasamāpann", "ချုပ်ငြိမ်းခြင်း သမာပတ်ကို ဝင်စားနေသူ", "5", "^5-458", "nirodhaṃ samāpajjantassa"),
    (r"jjhānaṃ samāpann", "ဈာန်ကို ဝင်စားနေသူ", "5", "^5-333", "jhānaṃ samāpannassa"),
    (r"paṭhamajjhān", "ပထမ ဈာန်", "5", "^5-332", "paṭhamaṃ jhānaṃ"),
    (r"dutiyajjhān", "ဒုတိယ ဈာန်", "5", "^5-333", "Dutiyassa jhānassa"),
    (r"tatiyajjhān", "တတိယ ဈာန်", "5", "^5-333", "Tatiyaṃ jhānaṃ"),
    (r"catutthajjhān", "စတုတ္ထ ဈာန်", "5", "^5-333", "catutthaṃ jhānaṃ"),
    (r"kāmāvacar", "ကာမဘုံ", "1", "^1-990", "kāmāvacare"),
    (r"(?<![aA])rūpāvacar", "သိမ်မွေ့သော ရုပ်ဘုံ", "1", "^1-990", "rūpāvacare"),
    (r"arūpāvacar", "ရုပ်မရှိသော ဘုံ", "1", "^1-990", "arūpāvacare"),
    (r"sukhāya vedanāya sampayutt", "သာယာသော ခံစားမှုနှင့် ယှဉ်တွဲသော", "1", "^1-988", "sukhāya vedanāya sampayuttā"),
    (r"cittasampayutt", "စိတ်နှင့် ယှဉ်တွဲသော", "1", "^1-M2-58", "cittasampayuttā"),
    (r"saññā ca vedanā ca", "မှတ်သိမှုနှင့် ခံစားမှု", "5", "^5-333", "saññā ca vedanā ca"),
    (r"(?<![\w])kusala(?:ṃ cittaṃ|citt)", "ကုသိုလ်စိတ်", "1", "^1-1", "kusalaṃ cittaṃ"),
    (r"(?<![\w])akusalaṃ cittaṃ", "အကုသိုလ်စိတ်", "1", "^1-365", "akusalaṃ cittaṃ"),
    (r"abyākataṃ cittaṃ", F.ABY + " စိတ်", "5", "^5-556", "kusalābyākate citte"),
    (r"\baraṇaṃ", "ပဋိပက္ခ မရှိသော", "1", "^1-M2-100", "araṇā"),
    (r"\bsaraṇa", "ပဋိပက္ခ ရှိသော", "1", "^1-M2-100", "saraṇā"),
    (r"\buppann", "ဖြစ်ပေါ်ပြီး", "1", "^1-1", "uppannaṃ"),
    (r"niruddh", "ချုပ်ငြိမ်းပြီး", "5", "^5-333", "niruddhā"),
    (r"uppajjamān|nirujjhamān", "ဆဲ", "5", "^5-366", "vimuccamānanti"),
    (r"parijān", "ပိုင်းခြား သိ", "5", "^5-390", "parijānāti"),
    (r"[Pp]ariññā", "ပိုင်းခြား သိခြင်း", "4", "^4-130", "pariññaṃ"),
    (r"vītikkant|vītakkant", "လွန်မြောက်", "2", "^2-609", "vītikkanto"),
    (r"atikkantakāl", "ကျော်လွန်", "2", "^2-609", "atikkanto"),
    (r"(?<![\w])n?uppajj", "ဖြစ်ပေါ်", "2", "^2-203", "uppajjamānā uppajjati"),
    (r"nirujjh", "ချုပ်ငြိမ်း", "2", "^2-204", "nirujjhamānā nirujjhati"),
    (r"upapajj", "ပြန်လည် ဖြစ်ပေါ်", "2", "^2-1024", "kattha upapajjanti"),
    (r"\bcavant", "စုတေ", "2", "^2-1029", "cavanti āyusaṅkhayā"),
    (r"parinibb", "ပရိနိဗ္ဗာန် ပြု", "4", "^4-M-7", "parinibbāyī"),
    (r"asaññasatt", "အသညသတ်", "2", "^2-18-4-3-0", "Asaññasattā"),
    (r"suddhāvās", "သုဒ္ဓါဝါသ", None, None, None),                      # sample (NEW there)
    (r"\byassa\b(?! cittassa anantarā)", "အကြင်သူအား", "2", "^2-199", "Idha yassa te honti"),
    (r"\byattha\b", "အကြင်နေရာ၌", None, None, None),             # sample (NEW there)
    (r"okās", "နေရာ", "4", "^4-M-11", "okās"),
    (r"\batīt", "အတိတ်", "1", "^1-M1-18", "atītā dhammā"),
    (r"\banāgat", "အနာဂတ်", "1", "^1-M1-18", "anāgatā dhammā"),
    (r"paccuppann", "ပစ္စုပ္ပန်", "1", "^1-M1-18", "paccuppannā dhammā"),
    (r"\buddes", "အကျဉ်း ဖော်ပြချက်", "3", "^3-1-0", "Uddeso"),
    (r"niddes", "အကျယ် ဖော်ပြချက်", "1", "^1-2-3-1-0", "Ekakaniddeso"),
    (r"suddha(?!vās)", "ရိုးရိုး", "5", "^5-1-1-0", "Suddh"),
    (r"paṇṇatti", "သတ်မှတ်ချက်", "1", "^1-M2-108", "paññatti"),
    (r"puggal", "ပုဂ္ဂိုလ်", "1", "^1-1050", "puggal"),
    (r"vārādi", "စသည်", "3", "^3-15-1-1-0", "Khandhādi"),
    (r"uppāda(?!kkhaṇ)", "ဖြစ်ပေါ်ခြင်း", "1", "^1-1-0", "Cittuppādakaṇḍaṃ"),
    (r"nirodha", "ချုပ်ငြိမ်းခြင်း", "1", "^1-1063", "nirodh"),
    (r"vāro\b|vāra(?!ṃ)", "ဖော်ပြချက်", "2", "^2-15-1-2-0", "Saccavāro"),
    (r"niṭṭhit", "” ပြီးဆုံးပြီ။", "2", "^2-153", "Khandhavibhaṅgo niṭṭhito"),
    (r"ṭhapetvā", "ချန်ထား၍", "2", "^2-796", "ṭhapetvā"),
    (r"\bavasesā\b", "ကြွင်းကျန်သော", "2", "^2-796", "avasesā paññā"),
    (r"\bkāy(?:o|añca|oti)\b", "ကိုယ်", "2", "^2-226", "Kāyasañcetanā"),
    (r"\bvac(?:ī|iñca|īti)\b", "နှုတ်", "5", "^5-332", "vacībhedo"),
    (r"\bsaṅkhār(?:o|ā)\b", "ပြုပြင်ဖန်တီးမှု", "1", "^1-40", "saṅkhār"),
]
for _q, _m in MK.QUAL.items():
    if " " not in _q and _q not in ("kusalaṃ", "akusalaṃ", "abyākataṃ", "araṇaṃ"):
        REUSE.append((rf"\b{_q[:-1]}(?:ṃ|cittassa)", _m, "2", "^2-365", _q))
# documented exceptions (not counted as identical; see notes-ch6-8.md «Departures»)
EXCEPT = [
    (r"kāyasaṅkhār|vacīsaṅkhār|cittasaṅkhār", "pi-2 ^2-226 «ကိုယ် / နှုတ် / စိတ် ပြုပြင်ဖန်တီးမှု» (volition sense, "
     "paṭiccasamuppāda)", "pi-5 ^5-458 «ကိုယ်၏ / နှုတ်၏ / စိတ်၏ ပြုပြင်ဖန်တီးမှု» (same sense as here: breathing, "
     "thought, perception and feeling)"),
    (r"uppādakkhaṇ", "sample uppāda «ဖြစ်ပေါ်ခြင်း» (pi-1 Cittuppāda)", "pi-5 ^5-366 uppādakkhaṇe «ဖြစ်ခြင်း ခဏ၌» "
     "(identical Pāli word)"),
    (r"kāmāvacare|rūpāvacare|arūpāvacare", "pi-1 ^1-988 kāmāvacare «ကာမဘုံနှင့် ဆိုင်သော စိတ်…၌» (adjective of citta)",
     "«ကာမဘုံ၌» … (a place, okāsa; the plane names of the style sheet)"),
    (r"yassa cittassa anantarā", "yassa «အကြင်သူအား» (correlative question)", "«မိမိ စိတ်၏ ချက်ချင်း နောက်၌» "
     "(relative inside a person group: 'right after whose mind')"),
    (r"\bNatthi\.", "pi-3 ^3-410 Natthi «မရှိ။»", "«မရှိပါ။» (sample: answer register)"),
    (r"anuloma|paccanīka", "pi-5 «အစဉ်အတိုင်း» / «ပြောင်းပြန်»", "«အဟုတ်ပြ ပုံစံ» / «အငြင်းပြ ပုံစံ» (sample)"),
    (r"\bcavant", "pi-2 termbase cavati «သေသည်»", "«စုတေ» (sample)"),
]


# ===================================================================================== the checks
def check(PAIRS, rebuild=True):
    bad = []
    if rebuild:
        for name in NAMES:
            text, nbad = MK.run(name)
            if nbad or text != (MK.OUT / name).read_text(encoding="utf-8"):
                bad.append(f"A {name}: regenerated text differs")
    cnt = dict.fromkeys(["lines", "neg", "verb", "ans", "pair", "num", "rec", "tab", "c2n", "c2s", "c3n", "c3s",
                         "ex"], 0)
    for name, (P, M) in PAIRS.items():
        # B1
        if len(P) != len(M):
            bad.append(f"B1 {name}: {len(P)} vs {len(M)} lines")
            continue
        raw = "\n".join(M)
        if unicodedata.normalize("NFC", raw) != raw:
            bad.append(f"B1 {name}: not NFC")
        if any(0x1050 <= ord(c) <= 0x109F for c in raw):
            bad.append(f"B1 {name}: code point U+1050-U+109F")
        lp = [F.LABEL_RE.match(p)[1] for p in P if F.LABEL_RE.match(p)]
        lm = [re.match(r"^\(([က-အ])\) ", m)[1] for m in M if re.match(r"^\(([က-အ])\) ", m)]
        cnt["pair"] += len(lp)
        if [F.AKKHARA[x] for x in lp] != lm:
            bad.append(f"B4 {name}: label sequence differs")
        for i, (p, m) in enumerate(zip(P, M), 1):
            cnt["lines"] += 1
            e = MK.line_check(p, m)
            if e:
                bad.append(f"B1 {name}:{i} {e}")
            if p.count("vā pana") != m.count(F.VA_PANA):
                bad.append(f"B4 {name}:{i} vā pana vs «{F.VA_PANA}»")
            s = nobr(body(p))
            if re.findall(r"\d", re.sub(r"\^\S+", "", p)) != re.findall(r"\d", re.sub(r"\^\S+", "", m)):
                bad.append(f"B5 {name}:{i} digits")
            for rx, my in NUMW:
                k = len(re.findall(rx, s))
                cnt["num"] += k
                if k != nobr(m).count(my):
                    bad.append(f"B5 {name}:{i} «{rx}» {k}x vs «{my}» {nobr(m).count(my)}x")
            if HEAD.match(p):
                continue
            a, b = p_neg(p), m_neg(m)
            cnt["neg"] += a
            if a != b:
                bad.append(f"B2 {name}:{i} negations Pāli {a} vs Burmese {b}")
            exp, got = p_verbs(s), m_verbs(nobr(body(m)))
            cnt["verb"] += len(exp)
            if exp != got:
                bad.append(f"B3 {name}:{i} verbs Pāli {exp} vs Burmese {got}")
            for pa, my in (("Āmantā", F.YES), ("Natthi.", F.NATTHI)):
                k = s.count(pa)
                cnt["ans"] += k
                g = body(m).count(my)
                if pa == "Āmantā":          # harmonise A4: «Āmantā …pe….» = «ဟုတ်ပါသည် …။» (ch7a / ch9-10a)
                    k2 = len(re.findall(r"Āmantā …[Pp]e…", s))
                    g += min(k2, body(m).count(F.YES[:-1] + " …"))
                if k != g:
                    bad.append(f"B3 {name}:{i} «{pa}» {k}x vs «{my}» {g}x")
    # B6 recurring sentences
    occ = {}
    for name, (P, M) in PAIRS.items():
        for i, (p, m) in enumerate(zip(P, M), 1):
            b, mb = body(p), body(m)
            if HEAD.match(b) or "…" in b or b in F.COLO or nobr(b) in F.LINES or F.BRACKET.sub("⟦v⟧", b) in F.LINES:
                continue
            lab = F.LABEL_RE.match(b)
            b = F.LABEL_RE.sub("", b)
            mb = re.sub(r"^\([က-အ]\) ", "", mb)
            ps = F.SPLIT.split(nobr(b))
            ms = [x if x.endswith("။") else x + "။" for x in re.split(r"(?<=။) ", nobr(mb))]
            if len(ps) != len(ms):
                bad.append(f"B6 {name}:{i} {len(ps)} Pāli vs {len(ms)} Burmese sentences")
                continue
            for j, (x, y) in enumerate(zip(ps, ms)):
                if j == 0 and lab and "vā pana" in x:
                    y = y.replace(F.VA_PANA + " ", "", 1)
                occ.setdefault(canon(x), set()).add(y)
    cnt["rec"] = len(occ)
    for k, v in occ.items():
        if len(v) > 1:
            bad.append(f"B6 «{k[:70]}» has {len(v)} Burmese renderings")
    # B7 table values
    for name, (P, M) in PAIRS.items():
        for i, (p, m) in enumerate(zip(P, M), 1):
            b, mb = body(p), body(m)
            h = re.match(r"^(#+) (.*)$", b)
            if h:
                cnt["tab"] += 1
                if mb != f"{h[1]} {F.heading(h[2])}":
                    bad.append(f"B7 {name}:{i} heading")
                continue
            if b in F.COLO:
                cnt["tab"] += 1
                if mb != F.COLO[b]:
                    bad.append(f"B7 {name}:{i} colophon")
            elif b in F.LINES:
                cnt["tab"] += 1
                if mb != F.LINES[b]:
                    bad.append(f"B7 {name}:{i} line table")
    # C2 whole lines / headings / Āmantā in the FINAL texts
    for name, (P, M) in PAIRS.items():
        for i, (p, m) in enumerate(zip(P, M), 1):
            k = F.LABEL_RE.sub("", re.sub(r"^#+ ", "", body(p)))
            if k in FIN_LINE:
                cnt["c2n"] += 1
                if re.sub(r"^\([က-အ]\) ", "", re.sub(r"^#+ ", "", body(m))) in FIN_LINE[k]:
                    cnt["c2s"] += 1
                else:
                    bad.append(f"C2 {name}:{i} «{k[:50]}»: «{body(m)[:50]}» vs final {sorted(FIN_LINE[k])[:2]}")
            n = nobr(body(p)).count("Āmantā")
            if n:
                cnt["c2n"] += n
                g = min(n, body(m).count("ဟုတ်ပါသည်။") + body(m).count("ဟုတ်ပါသည် …"))   # harmonise A4
                cnt["c2s"] += g
                if g < n:
                    bad.append(f"C2 {name}:{i} «Āmantā»")
    if "ဟုတ်ပါသည်" not in " ".join(FIN["5"]["^5-1"][1]):
        bad.append("C2 witness Āmantā")
    # C3 reused terms
    for rx, my, bk, bid, wit in REUSE:
        if bk:
            pl, ml = FIN[bk][bid]
            if wit.lower() not in " ".join(pl).lower() or my not in " ".join(ml):
                bad.append(f"C3 witness pi-{bk} {bid}: «{wit}» / «{my}»")
                continue
        for name, (P, M) in PAIRS.items():
            for i, (p, m) in enumerate(zip(P, M), 1):
                if re.search(rx, nobr(body(p)), re.I):
                    cnt["c3n"] += 1
                    if my in m:
                        cnt["c3s"] += 1
                    else:
                        bad.append(f"C3 {name}:{i} «{rx}» -> «{my}» missing")
    for rx, fin, ours in EXCEPT:
        cnt["ex"] += sum(1 for P, M in PAIRS.values() for p in P if re.search(rx, nobr(body(p)), re.I))
    return bad, cnt


def report(bad, cnt):
    print(f"A. rebuild: {len(NAMES)} / {len(NAMES)} files regenerated identical" if not any(b.startswith("A ") for b in
                                                                                          bad) else "A. FAILED")
    print(f"B1 structure: {cnt['lines']} lines")
    print(f"B2 polarity: {cnt['neg']} negations, each one Burmese negative")
    print(f"B3 verbs and participles: {cnt['verb']} (root, tense / participle, polarity, double negative) in order; "
          f"{cnt['ans']} answers")
    print(f"B4 pairs: {cnt['pair']} labelled lines in order, every «vā pana» = «{F.VA_PANA}»")
    print(f"B5 numbers: digits per line equal; {cnt['num']} number words")
    print(f"B6 recurring sentences: {cnt['rec']} distinct Pāli sentences, each with one Burmese rendering")
    print(f"B7 table values: {cnt['tab']} headings / colophons / table lines")
    tn, ts = cnt["c2n"] + cnt["c3n"], cnt["c2s"] + cnt["c3s"]
    print(f"C. reuse test: {ts} / {tn} identical (C2 whole lines and answers {cnt['c2s']}/{cnt['c2n']}, C3 "
          f"{len(REUSE)} reused terms {cnt['c3s']}/{cnt['c3n']} line occurrences)")
    print(f"   documented exceptions (not counted): {len(EXCEPT)} terms on {cnt['ex']} lines")
    for rx, fin, ours in EXCEPT:
        print(f"   - {rx}: final {fin}; here {ours}")
    print(f"\nmismatches: {len(bad)}")
    for b in bad[:60]:
        print("  ", b)


def mutate():
    """each mutation of the real output must raise at least one mismatch."""
    muts = [("dropped «မ»", "မဖြစ်ပေါ်", "ဖြစ်ပေါ်"), ("dropped «ခဲ့»", "ဖြစ်ပေါ်ခဲ့", "ဖြစ်ပေါ်"),
            ("«ပြီး» -> «ဆဲ»", "ဖြစ်ပေါ်ပြီး ဖြစ်", "ဖြစ်ပေါ်ဆဲ ဖြစ်"), ("dropped «ကား မဟုတ်»", "သည်ကား မဟုတ်", "သည်"),
            ("changed term", MK.VACI_S, "နှုတ် ပြုပြင်ဖန်တီးမှု"), ("dropped «တစ်ဖန်»", F.VA_PANA + " ", ""),
            ("«ဟုတ်ပါသည်» -> «မဟုတ်ပါ»", F.YES, F.NO), ("future -> present", "ချုပ်ငြိမ်းလိမ့်မည်", "ချုပ်ငြိမ်းသည်")]
    ok = True
    for label, a, b in muts:
        hit = None
        for name, (P, M) in PAIRS0.items():
            for i, m in enumerate(M):
                if a in m:
                    hit = (name, i)
                    break
            if hit:
                break
        if not hit:
            print(f"   mutation «{label}»: not applicable")
            continue
        name, i = hit
        P, M = PAIRS0[name]
        M2 = list(M)
        M2[i] = M2[i].replace(a, b, 1)
        bad, _ = check({name: (P, M2)}, rebuild=False)
        print(f"   mutation «{label}» ({name}:{i + 1}): {'caught' if bad else 'NOT CAUGHT'} {bad[:1]}")
        ok &= bool(bad)
    return ok


if __name__ == "__main__":
    bad, cnt = check(PAIRS0)
    report(bad, cnt)
    if "--mutate" in sys.argv:
        print("\nmutation test:")
        if not mutate():
            bad.append("mutation not caught")
    sys.exit(1 if bad else 0)
