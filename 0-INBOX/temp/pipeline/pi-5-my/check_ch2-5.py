"""Check the Burmese zero-shot of pi-5 chapters 2-5 (2-parihanikatha, 3-brahmacariyakatha, 4-jahatikatha,
5-sabbamatthitikatha) line by line against the Pāli (model: check_sample.py).

usage: python3 -I -X utf8 check_ch2-5.py
  A. rebuild: make_ch2-5.py regenerates the four files byte for byte (nothing written here);
  B. per line: B1 structure (equal non-empty lines, dashes, ellipses, «[», item numbers, digits, block IDs, no «?» «।»
     «:-», NFC, no code point U+1050-U+109F); B2 POLARITY per line: (a) upalabbhati, vattabba +/-, Āmantā, Na hevaṃ
     vattabbe (as check_sample); (b) parihāyati & co. «ဆုတ်ယုတ်» / «မဆုတ်ယုတ်»; (c) jahati & co. «စွန့်ပယ်» /
     «မစွန့်ပယ်»; (d) EVERY NEGATION: the Pāli negators (na, no, natthi, nanu, n-/nv- forms, the privative words of
     PRIV) = the Burmese negative «မ» (a «မ» that opens a syllable before a consonant, without the known non-negative
     words of NOT_NEG) + «မဲ့»-free; B3 Pāli number words -> Burmese number words; B4 quote nesting per segment;
     B5 every recurring Pāli sentence has the same Burmese at each occurrence; B6 headings / colophons / LINES values;
  C. reuse test (pi-1 … pi-4 FINAL rails texts): C1 topic names (khandha, āyatana, dhātu, indriya); C2 whole lines /
     headings shared with pi-1 … pi-4; C3 the reused terms of REUSE: a FINAL segment holds the Pāli and the Burmese
     (witness found here independently), and every chapter line whose Pāli has the term has the Burmese.
Prints the mismatches (0 expected) and the reuse counts n / n.
"""
import importlib.util
import pathlib
import re
import sys
import unicodedata

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
_spec = importlib.util.spec_from_file_location("make_ch2_5", HERE / "make_ch2-5.py")
MS = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(MS)
F = MS.F
NAMES = MS.NAMES_OUT
bad = []


def nonempty(p):
    return [l for l in p.read_text(encoding="utf-8-sig").splitlines() if l.strip()]


def body(l):
    return F.strip_id(l).strip()


def nobr(s):
    return re.sub(r" ?\[[^\]]*\]", "", s)


PAIRS = {name: (nonempty(MS.PALI / name), nonempty(MS.OUT / name)) for name in NAMES}

# ===================================================================================== A. rebuild
for name in NAMES:
    text, nbad = MS.run(name)
    if nbad or text != (MS.OUT / name).read_text(encoding="utf-8"):
        bad.append(f"A {name}: regenerated text differs")
print(f"A. rebuild: {len(NAMES)} / {len(NAMES)} files checked")

# ===================================================================================== B1 structure
n_lines = 0
for name, (P, M) in PAIRS.items():
    if len(P) != len(M):
        bad.append(f"B1 {name}: {len(P)} vs {len(M)} lines")
        continue
    raw = (MS.OUT / name).read_text(encoding="utf-8")
    if "\n\n\n" in raw:
        bad.append(f"B1 {name}: double blank line")
    if unicodedata.normalize("NFC", raw) != raw:
        bad.append(f"B1 {name}: not NFC")
    if any(0x1050 <= ord(c) <= 0x109F for c in raw):
        bad.append(f"B1 {name}: code point U+1050-U+109F")
    for i, (p, m) in enumerate(zip(P, M), 1):
        n_lines += 1
        e = MS.line_check(p, m)
        if F.ID_RE.search(p) and (not F.ID_RE.search(m) or F.ID_RE.search(p)[1] != F.ID_RE.search(m)[1]):
            e.append("block ID")
        if e:
            bad.append(f"B1 {name}:{i} {e}")
print(f"B1 structure: {n_lines} lines")


# ===================================================================================== B2 polarity
def p_pol(p):
    s = nobr(body(p))
    sl = s.lower()
    neg_u = sl.count("nupalabbh") + sl.count("na upalabbh")
    pos_u = sl.count("upalabbh") - neg_u
    tot_v = len(re.findall(r"vattabb", sl))
    neg_v = len(re.findall(r"\b(?:no ca vata re|no ca|no ce pana|na hevaṃ|na) vattabb", sl))
    return (pos_u, neg_u, tot_v - neg_v, neg_v, sl.count("āmantā"), s.count("Na hevaṃ vattabbe"))


def m_pol(m):
    s = nobr(body(m))
    neg_u = s.count("မ" + F.FOUND)
    pos_u = s.count(F.FOUND) - neg_u
    neg_v = s.count("မဆိုသင့်")
    pos_v = s.count("ဆိုသင့်") - neg_v
    return (pos_u, neg_u, pos_v, neg_v, s.count(F.YES), s.count(F.NO_SAY))


def verb_pol(p, m, prx, my):
    """(positive, negative) counts of a Pāli verb family (negative = preceded by «na ») and of its Burmese stem."""
    s = nobr(body(p)).lower()
    tot = len(re.findall(prx, s))
    neg = len(re.findall(r"\bna " + prx, s))
    s = re.sub(r"\b(?:na hevaṃ vattabbe|na vattabbaṃ|no ca vata re vattabbe|no ca vattabbe|no ce pana vattabbe)\b",
               " ", s)
    neg = sum(1 for c in re.split(r"[,;?.…–]", s) for _ in re.findall(prx, c) if re.search(r"\bna\b", c))
    t = nobr(body(m))
    mneg = t.count("မ" + my)
    return (tot - neg, neg), (t.count(my) - mneg, mneg)


# (d) every negation. Pāli: free negators and the privative words that the Burmese renders with a negative «မ».
NEG_RX = re.compile(r"\b(?:na|no|nanu|neva|nevācinati|natthi|natthī\w*|natthaññatra|nappaṭibalā|nappavedhenti|"
                    r"nuppajj\w*|nvatth\w*|nvātīt\w*|nvānāgat\w*|nayidaṃ|natthikavādā)\b")
PRIV = {  # privative word (regex, full word) -> number of negative «မ» in its Burmese
    r"aniccaṃ|adhuvaṃ|asassataṃ|avipariṇāmadhammaṃ": 1, r"asamayavimutt\w*": 1, r"ahirik\w*|saahiriko": 1,
    r"anottapp\w*|saanottappī": 1, r"anabhāvaṅkat\w*|anuppādadhamm\w*": 1, r"arūparāg\w*": 1, r"avijj\w*": 1,
    r"aviññū|aviññātāresu": 1, r"ajaḷā|anelamūgā": 1, r"assaddhā|acchandikā|abhabbā|abhabba": 1,
    r"adinnādāy\w*": 1, r"abyāpannacittā": 1, r"anādāno": 1, r"aniṭṭhā": 1, r"appahīn\w*": 1,
    r"apariññātadukkho|asacchikatanirodho": 1, r"niraggaḷo": 1, r"antarāparinibbāyī": 1, r"appaṭividdhākuppo": 2, r"akupp\w*": 1,
    r"anohaṭabhāro": 1, r"apubbaṃ|acarimaṃ": 1, r"asaṅkhāraparinibbāyī": 1, r"aniyyāniko|anāsavo|asaṃyojaniyo|"
    r"aganthaniyo|anoghaniyo|ayoganiyo|anīvaraṇiyo|aparāmaṭṭho|anupādāniyo|asaṃkilesiyo": 1,
    r"appaṭisandhiyaṃ": 1, r"aniruddhaṃ|avigataṃ|avipariṇataṃ|ajātaṃ|abhūtaṃ|asañjātaṃ|anibbattaṃ|anabhinibbattaṃ|"
    r"apātubhūtaṃ": 1, r"ayogaṃ": 1, r"appiyaṃ": 1, r"aparimutto|ananubodhā|appaṭivedhā": 1,
    r"asaṅkiṇṇā|asaṅkiṇṇapubbā|appaṭikuṭṭhā|ahetukavādā|akiriyavādā": 1, r"appatiṭṭhitaṃ|avirūḷhaṃ": 1,
    r"asokaṃ|arajaṃ|anupāyāsaṃ|anupāyāsanti": 1,
}
PRIV_RX = [(re.compile(r"\b(?:" + k + r")(?:ti)?\b"), v) for k, v in PRIV.items()]
# harmonise B3: «ဆုံးမ» (ovāda, pi-4 ovadati) is no negation
NOT_NEG = ["ဆုံးမ", "မနော", "မထေရ်", "မဟာ", "မဂဓ", "ကာမ", "သို့မဟုတ်"]   # Burmese words opening with «မ» + consonant that are no negation
MY_NEG = re.compile(r"(?<![္])မ(?=[က-အ](?![့်္]))")


def p_negs(p):
    s = nobr(body(p)).lower()
    s0 = s
    s = re.sub(r"\b(?:na hevaṃ vattabbe|na vattabbaṃ|no ca vata re vattabbe|no ca vattabbe|no ce pana vattabbe)\b",
               " NEG ", s)                                             # the frames: one negation each
    n = s.count(" NEG ") + len(NEG_RX.findall(s))
    s = re.sub(r"nti\b", "ṃti", s)                                       # «…tanti» = «…taṃ» + ti
    for rx, k in PRIV_RX:
        n += k * len(rx.findall(s))
    return n


def m_negs(m):
    s = nobr(body(m))
    for w in NOT_NEG:
        s = s.replace(w, "")
    s = re.sub(r"မဆို(?!သင့်)", "", s)                                 # «…မဆို» = «whatever / whoever»
    return len(MY_NEG.findall(s))


n_pol = n_neg = 0
for name, (P, M) in PAIRS.items():
    for i, (p, m) in enumerate(zip(P, M), 1):
        if F.HEAD_RE.fullmatch(body(p)):
            continue
        a, b = p_pol(p), m_pol(m)
        n_pol += sum(a)
        if a != b:
            bad.append(f"B2a {name}:{i} polarity Pāli {a} vs Burmese {b}")
        if F.norm_pe(F.strip_q(F.BR_RE.sub("", body(p)))).rstrip(".") in F.COLO:
            continue
        for tag, prx, my in (("b", r"\bparih[āī]\w*", MS.PARIH), ("c", r"\bjah(?:ati|atī|itā)\w*", MS.JAHATI)):
            a, b = verb_pol(p, m, prx, my)
            n_pol += sum(a)
            if a != b:
                bad.append(f"B2{tag} {name}:{i} {my} Pāli {a} vs Burmese {b}")
        a, b = p_negs(p), m_negs(m)
        n_neg += a
        if a != b:
            msg = f"B2d {name}:{i} negations Pāli {a} vs Burmese {b}"
            if "--why" in sys.argv:
                t = nobr(body(m))
                for w in NOT_NEG:
                    t = t.replace(w, "")
                msg += "\n      M: " + " | ".join(t[max(0, x.start() - 8):x.start() + 7] for x in MY_NEG.finditer(t))
                sl = nobr(body(p)).lower()
                msg += "\n      P: " + " ".join(NEG_RX.findall(sl)) + " / " + " ".join(
                    x for rx, _ in PRIV_RX for x in rx.findall(sl))
            bad.append(msg)
print(f"B2 polarity: {n_pol} marks (a found / should say / Āmantā / Na hevaṃ, b parihāyati, c jahati); "
      f"B2d {n_neg} negations")

# ===================================================================================== B3 number words
NUMW = [(r"\bcatūhi\b|\bcattāri\b|\bcatunnaṃ\b|\bcatūhapāyehi\b|\bcatu(?=paññāsa)", F.NUM_MY[4]),
        (r"\bpañca(?:me|orambhāgiyāni|uddhambhāgiyāni|kkhandhā)?\b|\bpañcime\b|\bpañcorambh|\bpañcuddhambh", F.NUM_MY[5]),
        (r"\btayo\b|\btayome\b|\btayassu\b|\btīṇi\b|\btīhi\b|\btiṇṇaṃ\b|\btissannaṃ\b|\btisso\b|\btiṇṇannaṃ\b",
         F.NUM_MY[3]),
        (r"\bcha\b|\bchaccābhiṭhānāni\b|\bchattiṃs|\bchasaṭṭh", F.NUM_MY[6]), (r"\bsattakkhattu", F.NUM_MY[7]),
        (r"\bekabījī\b|\bekagghano\b|\bekaguṇaṃ\b", F.NUM_MY[1]), (r"\bdiguṇaṃ\b", F.NUM_MY[2]),
        (r"\baṭṭhārasa\b", F.NUM_MY[18]), (r"\bdvādasāyatanāni\b", F.NUM_MY[12]), (r"\bbāvīsat", F.NUM_MY[22]),
        (r"\bpannarasa", "ဆယ့်ငါး"), (r"\bchattiṃsā", "သုံးဆယ့်ခြောက်"), (r"\bcatupaññāsa\b", "ငါးဆယ့်လေး"),
        (r"\bchasaṭṭhi", "ခြောက်ဆယ့်ခြောက်"), (r"pañcamehi\b", F.ORD_MY[5]), (r"\bsatasahass", "သိန်း")]
n_num = 0
for name, (P, M) in PAIRS.items():
    for i, (p, m) in enumerate(zip(P, M), 1):
        s = nobr(body(p)).lower()
        for rx, my in NUMW:
            k = len(re.findall(rx, s))
            if not k:
                continue
            n_num += k
            got = sum(m.count(w) for w in my.split("|"))
            if got < k:
                bad.append(f"B3 {name}:{i} «{rx}» {k}x, Burmese «{my}» {got}x")
print(f"B3 number words: {n_num}")


# ===================================================================================== B4 quote nesting
def quotes_ok(lines):
    stack = []
    for li, line in enumerate(lines):
        s = nobr(line)
        for ci, ch in enumerate(s):
            if ch == "“":
                if stack and stack[-1][0] == "“" and stack[-1][1] < li and ci == 0:
                    continue                      # a new stanza / paragraph continues the open quotation
                if len(stack) % 2:
                    return f"“ at odd depth (line {li + 1})"
                stack.append(("“", li))
            elif ch == "‘":
                if len(stack) % 2 == 0:
                    return f"‘ at even depth (line {li + 1})"
                stack.append(("‘", li))
            elif ch in "”’":
                want = "“" if ch == "”" else "‘"
                if not stack or stack[-1][0] != want:
                    return f"unbalanced {ch} (line {li + 1})"
                stack.pop()
    return None if not stack else f"{len(stack)} quote(s) left open"


n_seg = 0
for name, (P, M) in PAIRS.items():
    cur = []
    for m in M:
        cur.append(m)
        if F.ID_RE.search(m):
            n_seg += 1
            e = quotes_ok(cur)
            if e:
                bad.append(f"B4 {name} {F.ID_RE.search(m)[1]}: {e}")
            cur = []
print(f"B4 quote nesting: {n_seg} segments")

# ===================================================================================== B5 recurring sentences
occ = {}
for name, (P, M) in PAIRS.items():
    for i, (p, m) in enumerate(zip(P, M), 1):
        b = body(p)
        if F.HEAD_RE.fullmatch(b):
            continue
        clean = F.BR_RE.sub("", b)
        key_line = F.norm_pe(F.strip_q(clean))
        if key_line in F.LINES or any(rx.fullmatch(key_line) for rx, _ in F.LINE_FRAMES):
            continue
        for a, z in F.split_sents(clean):
            k = F.norm_pe(F.strip_q(clean[a:z].strip()))
            nq = F.harm_noq(clean[a:z].strip())   # harmonise A1: the Pāli marks decide
            occ.setdefault((k, nq), []).append((name, i, m))
n_rec = s_rec = 0
for (k, nq), lst in occ.items():
    if len(lst) < 2:
        continue
    my = F.unit_my(k).replace("⟦b⟧", "").replace("  ", " ")
    if nq:
        my = my.translate(F.NO_QUOTES)
    for name, i, m in lst:
        n_rec += 1
        if my in nobr(body(m)):
            s_rec += 1
        else:
            bad.append(f"B5 {name}:{i} recurring «{k[:60]}» not as «{my[:60]}»")
print(f"B5 recurring sentences: {s_rec} / {n_rec} occurrences identical "
      f"({sum(1 for v in occ.values() if len(v) > 1)} sentences)")

# ===================================================================================== B6 table values
n_tab = 0
for name, (P, M) in PAIRS.items():
    for i, (p, m) in enumerate(zip(P, M), 1):
        b, mb = body(p), body(m)
        h = F.HEAD_RE.fullmatch(b)
        if h:
            n_tab += 1
            if mb != f"{h['h']} {F.HEAD[h['t']]}":
                bad.append(f"B6 {name}:{i} heading")
            continue
        key = F.norm_pe(F.strip_q(F.BR_RE.sub("", b)))
        if key.rstrip(".") in F.COLO:
            n_tab += 1
            if mb != F.COLO[key.rstrip(".")] + F.END:
                bad.append(f"B6 {name}:{i} colophon")
        elif key in F.LINES:
            n_tab += 1
            val = re.sub(r" ?⟦\d⟧", "", F.LINES[key])
            if nobr(mb) != val:
                bad.append(f"B6 {name}:{i} LINES value")
print(f"B6 table values: {n_tab} headings / colophons / table lines")

# ===================================================================================== C. reuse test
# C1 topic names (rūpaṃ of ^5-289 «atītaṃ rūpaṃ passati» = a visible object «အဆင်းအရောင်», as rūpā in the sample)
n_c1 = s_c1 = 0
PER = {name: [0, 0] for name in NAMES}
for name, (P, M) in PAIRS.items():
    for i, (p, m) in enumerate(zip(P, M), 1):
        pl = nobr(body(p)).lower()
        words = re.findall(r"[^\W\d]+", pl)
        toks = set(words) | {f"{a} {b}" for a, b in zip(words, words[1:])}
        for form, (n, roles) in F.NOUN.items():
            if not (n in F.KHANDHA5 or n in F.AYATANA.values() or n in F.DHATU.values() or n in F.INDRIYA.values()):
                continue
            if form in ("rūpadhātuyā", "rūpadhātuṃ", "rūpā") or form not in toks:
                continue
            if form == "rūpaṃ" and re.search(r"rūpaṃ passat", pl) and "rūpaṃ atthi" not in pl:
                continue
            n_c1 += 1
            PER[name][1] += 1
            if n.my in m:
                s_c1 += 1
                PER[name][0] += 1
            else:
                bad.append(f"C1 {name}:{i} «{form}» -> «{n.my}» missing")
# C2 whole lines / headings
FIN_LINE = {}
for bk, k, f, p, m in F.FINAL.lines():
    FIN_LINE.setdefault(re.sub(r"^#+ ", "", body(p)), set()).add(re.sub(r"^#+ ", "", body(m)))
n_c2 = s_c2 = 0
for name, (P, M) in PAIRS.items():
    for i, (p, m) in enumerate(zip(P, M), 1):
        k = re.sub(r"^#+ ", "", body(p))
        if k in FIN_LINE:
            n_c2 += 1
            if re.sub(r"^#+ ", "", body(m)) in FIN_LINE[k]:
                s_c2 += 1
            else:
                bad.append(f"C2 {name}:{i} «{k}»: «{body(m)}» vs final {sorted(FIN_LINE[k])[:2]}")
# C3 reused terms: (regex on the chapter Pāli, Burmese); the witness is searched in pi-1 … pi-4 FINAL here
REUSE = [
    (r"\barahā\b|\barahato\b|\barahatā\b", "ရဟန္တာ"), (r"sotāpann", "သောတာပန်"), (r"sakadāgām(?!iphal|imagg)", "သကဒါဂါမ်"),
    (r"\banāgām(?!iphal|imagg)", "အနာဂါမ်"), (r"puthujjan", "ပုထုဇဉ်"), (r"sotāpattiphal", "သောတာပတ္တိဖိုလ်"),
    (r"sakadāgāmiphal", "သကဒါဂါမိဖိုလ်"), (r"anāgāmiphal", "အနာဂါမိဖိုလ်"), (r"anāgāmimagg", "အနာဂါမိမဂ်"),
    (r"\bsamayavimutt", "အချိန်အလိုက် လွတ်မြောက်"), (r"asamayavimutt", "အချိန်အလိုက် မဟုတ်ဘဲ လွတ်မြောက်"),
    (r"kilesā|kilese\b|kilesappahān|kilesāvaraṇ", "ကိလေသာ"), (r"\brāgo\b|\brāgaṃ\b|\brāgena\b|\brāgapp", "ရာဂ"),
    (r"\bdoso\b|\bdosena\b|\bdosapp|\bdosapar", "ဒေါသ"), (r"\bmoho\b|\bmohena\b|\bmohapar", "မောဟ"),
    (r"\bthinaṃ\b|\bthinena\b", "ထိုင်းမှိုင်းမှု"), (r"\buddhacc", "ယောက်ယက်ခတ်မှု"),
    (r"\bahirik|saahirik", "ဒုစရိုက်ကို မရှက်မှု"), (r"anottapp", "ဒုစရိုက်ကို မကြောက်ရွံ့"),
    (r"sakkāyadiṭṭh", "ကိုယ်ကို အတ္တဟု ယူဆသော အယူ"), (r"sīlabbataparāmās", "သီလ အကျင့်ဝတ်ဆိုင်ရာ"),
    (r"\bvicikicch(?!ita)", "ယုံမှား"), (r"kāmarāg", "ကာမရာဂ"), (r"byāpād", "ဖျက်ဆီးလိုစိတ်"),
    (r"\boḷārik", "ရုန့်ရင်း"), (r"satipaṭṭhān", "သတိပဋ္ဌာန်"), (r"sammappadhān", "မှန်ကန်သော ကြိုးပမ်းအားထုတ်ခြင်း"),
    (r"iddhipād", "ဣဒ္ဓိပါဒ်"), (r"bojjhaṅg", "ဗောဇ္ဈင်"), (r"\bbalā\b|\bbalabhāvan", "စွမ်းအား", r"balāni"),
    (r"pañcorambhāgiy", "အောက်ပိုင်း ဘုံနှင့် ဆိုင်သော နှောင်ကြိုး ငါးပါး"),
    (r"pañcuddhambhāgiy", "အထက်ပိုင်း ဘုံနှင့် ဆိုင်သော နှောင်ကြိုး ငါးပါး"),
    (r"anusay", "ကိန်းအောင်းခြင်း"), (r"pariyuṭṭh", "ထကြွခြင်း"), (r"brahmacariy", "မြင့်မြတ်သော အကျင့်"),
    (r"asaññasatt", "အသညသတ်"), (r"sammāsambuddh|sammāsammuddh", "အမှန်ကို ကိုယ်တိုင် အပြည့်အဝ သိမြင်တော်မူသော ဘုရားရှင်"),
    (r"paccekasambuddh", "ပစ္စေကဗုဒ္ဓါ"), (r"sattakkhattuparam", "အများဆုံး ခုနစ်ကြိမ်သာ ပြန်လည် ဖြစ်ပေါ်သူ"),
    (r"kolaṅkol", "အမျိုးမှ အမျိုးသို့ ကူးသူ"), (r"ekabīj", "မျိုးစေ့ တစ်စေ့သာ ရှိသူ"),
    (r"antarāparinibb", "သက်တမ်း၏ အလယ်သို့ မရောက်မီ ပရိနိဗ္ဗာန် ပြုသူ"),
    (r"upahaccaparinibb", "သက်တမ်း၏ အလယ်ကို ကျော်ပြီးမှ ပရိနိဗ္ဗာန် ပြုသူ"),
    (r"asaṅkhāraparinibb", "တိုက်တွန်းမှု မရှိဘဲ ပရိနိဗ္ဗာန် ပြုသူ"),
    (r"sasaṅkhāraparinibb", "တိုက်တွန်းမှုဖြင့် ပရိနိဗ္ဗာန် ပြုသူ"),
    (r"uddhaṃsoto akaniṭṭhagāmī", "အထက်သို့ စီးဆင်း၍ အကနိဋ္ဌ ဘုံသို့ ရောက်သူ"), (r"parinibb", "ပရိနိဗ္ဗာန်"),
    (r"sacchikiriyāya paṭipann", "မျက်မှောက်ပြုရန် ကျင့်ကြံ"), (r"apubbaṃ acarimaṃ", "ရှေ့ မရှိ၊ နောက် မရှိဘဲ"),
    (r"idha vihāya niṭṭh", "ဤလောကကို စွန့်ခွာပြီးမှ"), (r"rūpāvacar", "သိမ်မွေ့သော ရုပ်ဘုံနှင့် ဆိုင်သော"),
    (r"\bniyyāniko\b", "လွတ်မြောက်ရာသို့ ပို့ဆောင်သော"), (r"apacayagām", "လျော့ပါးခြင်းဆီသို့"),
    (r"\banāsavo\b", "စိတ်အစွန်းအထင်း၏ အာရုံ မဖြစ်နိုင်သော"), (r"\bsāsavo\b", "စိတ်အစွန်းအထင်း၏ အာရုံ ဖြစ်နိုင်သော"),
    (r"asaṃkilesiyo", "ကိလေသာ၏ အာရုံ မဖြစ်နိုင်သော", r"asaṃkilesik"), (r"aparāmaṭṭho", "မှားယွင်းသော ယူဆမှု၏ အာရုံ"),
    (r"sāmaññaphal", "ရဟန်းအဖြစ်၏ ဖိုလ်"), (r"abhisamay|abhisamenti", "ထင်ထင်ရှားရှား", r"abhisamay"),
    (r"pāṇātipāt", "သူ့အသက်ကို သတ်"), (r"adinnādāy", "မပေးသည်ကို ယူသူ"),
    (r"kāmesumicchācār", "ကာမတို့၌ မှားယွင်းစွာ ကျင့်သူ"), (r"musāvād", "မုသား ပြောသူ"),
    (r"pisuṇ", "ကုန်းတိုက်သော စကားကို ပြောသူ"), (r"pharusāvācā", "ကြမ်းတမ်းသော စကားကို ပြောသူ", r"pharusavāco"),
    (r"samphappalāp", "အကျိုးမဲ့ ပြိန်ဖျင်းသော စကားကို ပြောသူ"), (r"abhijjhāl", "သူ့ဥစ္စာကို လိုချင်သူ"),
    (r"\bbyāpannacitt", "ဖျက်ဆီးလိုစိတ် ရှိသော စိတ် ရှိသူ"), (r"abyāpannacitt", "ဖျက်ဆီးလိုစိတ် မရှိသော စိတ် ရှိသူ"),
    (r"micchādiṭṭh", "မှားယွင်းသော အယူ"), (r"sammādiṭṭh", "မှန်ကန်သော အယူ"),
    (r"bhikkhūnaṃ bhikkhunīnaṃ upāsakānaṃ upāsikānaṃ", "ရဟန်းတို့၊ ဘိက္ခုနီတို့၊ ဥပါသကာတို့၊ ဥပါသိကာတို့"),
    (r"\batīt", "အတိတ်"), (r"\banāgat(?!āmī)", "အနာဂတ်"), (r"paccuppann", "ပစ္စုပ္ပန်"),
    (r"niccaṃ dhuvaṃ sassataṃ", "ထာဝရ တည်မြဲ", r"sassat"), (r"vipariṇāmadhamm", "ဖောက်ပြန်ပြောင်းလဲတတ်သော သဘော"),
    (r"\bnibbān", "နိဗ္ဗာန်"), (r"cakkhuviññāṇ", "မျက်စိ သိစိတ်"), (r"manoviññāṇ", "မနော သိစိတ်"),
    (r"\bāloko\b", "အလင်း"), (r"cakkavatt", "စကြဝတေး မင်း"), (r"atītānāgatapaccuppannaṃ ajjhattaṃ",
                                                              "အတိတ်ဖြစ်စေ၊ အနာဂတ်ဖြစ်စေ၊ ပစ္စုပ္ပန်ဖြစ်စေ၊ မိမိ၌ ရှိသည်ဖြစ်စေ"),
    (r"niruttipath", "စကားဖြင့် ဖော်ပြမှု၏ လမ်းကြောင်း"), (r"adhivacanapath", "အမည်ခေါ်ဝေါ်မှု၏ လမ်းကြောင်း"),
    (r"kabaḷīkār", "လုတ်ပြု၍ စားရသော အာဟာရ"), (r"nāmarūp", "စိတ်ပိုင်းနှင့် ရုပ်ပိုင်း"),
    (r"bhavataṇh", "ဘဝကို တပ်မက်မှု"), (r"\blobho\b", "လောဘ"), (r"brahmalok", "ဗြဟ္မာ့ပြည်"),
    (r"dukkhassantakar", "ဒုက္ခ၏ အဆုံးကို ပြု"), (r"\bapāy", "အပါယ်"), (r"\bevamevaṃ\b", "ထို့အတူပင်"),
    (r"bhagav", "မြတ်စွာဘုရား"), (r"suttant", "သုတ္တန်"), (r"saṅgh", "သံဃာ"), (r"\bdev", "နတ်"),
    (r"\bmanuss", "လူ"), (r"brāhmaṇ", "ပုဏ္ဏား"), (r"\bkāyena phusitvā", "ကိုယ်ဖြင့် ထိ၍"),
    (r"pahātabb", "ပယ်ရမည့်"), (r"\bcuto\b|\bcutassa\b", "သေ၍"),
]
W_FOUND = {}
REUSE = [x if len(x) == 3 else (x[0], x[1], x[0]) for x in REUSE]
for rx, my, wrx in REUSE:
    crx = re.compile(wrx, re.I)
    for bk, k, f, p, m in F.FINAL.lines():
        if crx.search(nobr(p)) and my in m:
            W_FOUND[rx] = (bk, k)
            break
n_c3 = s_c3 = seen_terms = 0
for rx, my, wrx in REUSE:
    if rx not in W_FOUND:
        bad.append(f"C3 no FINAL witness for «{rx}» / «{my}»")
        continue
    hits = 0
    for name, (P, M) in PAIRS.items():
        for i, (p, m) in enumerate(zip(P, M), 1):
            if F.HEAD_RE.fullmatch(body(p)):
                continue
            if re.search(rx, nobr(body(p)), re.I):
                hits += 1
                n_c3 += 1
                PER[name][1] += 1
                if my in m:
                    s_c3 += 1
                    PER[name][0] += 1
                else:
                    bad.append(f"C3 {name}:{i} «{rx}» -> «{my}» missing")
    if hits:
        seen_terms += 1
print(f"C. reuse test: C1 topic names {s_c1} / {n_c1}; C2 whole lines / headings {s_c2} / {n_c2}; "
      f"C3 terms {s_c3} / {n_c3} occurrences ({seen_terms} terms) identical with pi-1 … pi-4 final")
tot_s, tot_n = s_c1 + s_c2 + s_c3, n_c1 + n_c2 + n_c3
print("   per chapter: " + "; ".join(f"{k} {a} / {b}" for k, (a, b) in PER.items()))
if bad:
    print(f"\n{len(bad)} MISMATCHES")
    for b in bad[:200]:
        print("  " + b)
    sys.exit(1)
print(f"\nOK: 0 mismatches; reuse {tot_s} / {tot_n} identical")
