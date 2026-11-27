"""Check the Burmese zero-shot of pi-5 chapters 17-20 line by line against the Pāli (adapted from check_ch11-12.py /
check_ch6-10.py / check_ch2-5.py / check_sample.py).

usage: python3 -I -X utf8 check_ch17-20.py [chapter.md ...] [--why]   (default: all four)
  A. rebuild: make_ch17-20.py regenerates every file byte for byte (nothing written here); A2: the imported chapters
     (1, 6-12) still rebuild byte-identical with the ch17-20 tables installed;
  B. per line: B1 structure (equal non-empty lines, dashes, ellipses, «[», item numbers, digits, no «?» «।» «:-»,
     NFC, no code point U+1050-U+109F that Zawgyi abuses, block IDs); B2 POLARITY per line: upalabbhati /
     nupalabbhati, vattabba positive / negative («ဆိုသင့်» / «မဆိုသင့်»), Āmantā («ဟုတ်ပါသည်»), Na hevaṃ vattabbe
     («ဤသို့ မဆိုသင့်ပါ»); B7 EXISTENCE polarity per line: every natthi / na atthi = one «မရှိ» (plus the Pāli
     words whose fixed Burmese has «မရှိ»: the arūpa bases, asaṅkhata, asaṅkhāraparinibbāyī), and the positive atthi
     forms are all there; B3 Pāli number words -> Burmese number words; B4 quote nesting per segment; B5 every
     recurring Pāli sentence has the same Burmese at each occurrence, in these chapters AND in the approved sample
     (preamble, 1-puggalakatha, read only); B6 table values (headings, LINES entries, colophons);
  C. reuse test (pi-1 … pi-4 FINAL rails texts): C1 topic names (khandha, āyatana, dhātu, indriya) wherever their
     Pāli forms occur; C2 whole lines / headings that also occur in pi-1 … pi-4; C3 every reused term of REUSE (the
     sample's list, narrowed where these chapters have another witnessed term, plus the terms of these chapters):
     witness in the rails segment, and every line whose Pāli has the term has the Burmese.
Prints the mismatches (0 expected) and the reuse counts n / n.
"""
import pathlib
import re
import sys
import unicodedata

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import importlib.util  # noqa: E402
_spec = importlib.util.spec_from_file_location("make_ch17_20", HERE / "make_ch17-20.py")
MS = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(MS)
F = MS.F
ROOT = HERE.parents[3]
NAMES = [a for a in sys.argv[1:] if a.endswith(".md")] or MS.NAMES_OUT
SAMPLE = ["preamble.md", "1-puggalakatha.md", "6-atitakkhandhadikatha.md", "7-ekaccam-atthitikatha.md",
          "8-satipatthanakatha.md", "9-hevatthikatha.md", "10-dutiyavaggo.md", "11-tatiyavaggo.md",
          "12-catutthavaggo.md"]   # approved sample + ch6-10 + ch11-12 (imported)
bad = []


def nonempty(p):
    return [l for l in p.read_text(encoding="utf-8-sig").splitlines() if l.strip()]


def body(l):
    return F.strip_id(l).strip()


def nobr(s):
    return re.sub(r" ?\[[^\]]*\]", "", s)


PAIRS = {}
for name in NAMES:
    P = nonempty(MS.PALI / name)
    M = nonempty(MS.OUT / name)
    PAIRS[name] = (P, M)

# ===================================================================================== A. rebuild
for name in NAMES:
    text, nbad = MS.run(name)
    if nbad or text != (MS.OUT / name).read_text(encoding="utf-8"):
        bad.append(f"A {name}: regenerated text differs")
for name in SAMPLE:
    if name == "preamble.md":
        continue
    text, nbad = MS.run(name, misses=True)
    if nbad or text != (MS.OUT / name).read_text(encoding="utf-8"):
        bad.append(f"A2 {name}: the imported chapter no longer rebuilds identically with the ch17-20 tables")
print(f"A. rebuild: {len(NAMES)} / {len(NAMES)} files checked; A2 {len(SAMPLE) - 1} imported chapters rebuild identically")

# ===================================================================================== B1 structure
n_lines = 0
for name, (P, M) in PAIRS.items():
    if len(P) != len(M):
        bad.append(f"B1 {name}: {len(P)} vs {len(M)} lines")
        continue
    raw = (MS.OUT / name).read_text(encoding="utf-8")
    if "  " in raw:
        bad.append(f"B1 {name}: double space")
    if "\n\n\n" in raw:
        bad.append(f"B1 {name}: double blank line")
    if unicodedata.normalize("NFC", raw) != raw:
        bad.append(f"B1 {name}: not NFC")
    if any(0x1050 <= ord(c) <= 0x109F for c in raw):
        bad.append(f"B1 {name}: code point U+1050-U+109F")
    for i, (p, m) in enumerate(zip(P, M), 1):
        n_lines += 1
        e = MS.MS.line_check(p, m)
        if F.ID_RE.search(p) and (not F.ID_RE.search(m) or F.ID_RE.search(p)[1] != F.ID_RE.search(m)[1]):
            e.append("block ID")
        if e:
            bad.append(f"B1 {name}:{i} {e}")
print(f"B1 structure: {n_lines} lines")


# ===================================================================================== B2 polarity
def p_pol(p):
    s = nobr(body(p))
    sl = s.lower()
    neg_u = sl.count("nupalabbh") + sl.count("na upalabbh") + sl.count("nayidha sattupalabbh")
    pos_u = sl.count("upalabbh") - neg_u
    tot_v = len(re.findall(r"vattabb", sl))
    neg_v = len(re.findall(r"\b(?:no ca vata re|no ca|no ce pana|na hevaṃ|na) vattabb", sl))
    return (pos_u, neg_u, tot_v - neg_v, neg_v, s.count("Āmantā"), s.count("Na hevaṃ vattabbe"))


def m_pol(m):
    s = nobr(body(m))
    neg_u = s.count("မ" + F.FOUND)
    pos_u = s.count(F.FOUND) - neg_u
    neg_v = s.count("မဆိုသင့်")
    pos_v = s.count("ဆိုသင့်") - neg_v
    return (pos_u, neg_u, pos_v, neg_v, s.count(F.YES), s.count(F.NO_SAY))


n_pol = 0
for name, (P, M) in PAIRS.items():
    for i, (p, m) in enumerate(zip(P, M), 1):
        a, b = p_pol(p), m_pol(m)
        n_pol += sum(a)
        if a != b:
            bad.append(f"B2 {name}:{i} polarity Pāli {a} vs Burmese {b}")
print(f"B2 polarity: {n_pol} marks (found / not found, should / should not say, Āmantā, Na hevaṃ)")

# ===================================================================================== B2d every negation (check_ch2-5.py method)
NEG_RX = re.compile(r"\b(?:na|no|nanu|neva|napi|natthi|natthī\w*|nuppajj\w*|mā|nāhaṃ|nātivattati|nātikkamantī\w*)\b")
# harmonise B2: anabhāvaṅkata = 1 «မ» (the ucchinnamūla string of ch2-5 «… မရှိတော့အောင် …», now book-wide)
PRIV = {  # privative word (regex, whole word) -> number of negative «မ» in its Burmese
    r"ṭhānāṭhān\w*": 1, r"sāvakaasādhāraṇ\w*": 1, r"anuppannassa|asañjātassa|anakkhātassa": 1,
    r"animitt\w*|appaṇihit\w*|appapaṇihit\w*": 1, r"avimutt\w*": 1, r"anaṅgaṇe|āneñjappatte": 1, r"avijj\w*": 1,
    r"arattañca|aduṭṭhañca|amūḷhañca|achinnañca|abhinnañca|akatañc[aā]": 1, r"appahīn\w*": 1, r"abhāvit\w*": 1,
    r"amaggena": 1, r"assaddh\w*": 1, r"asamāhit\w*": 1, r"anupādiṇṇ\w*": 1, r"arūpāvacar\w*": 1,
    r"apariyāpann\w*": 1, r"adibbacakkhuk\w*|appaṭiladdh\w*|anadhigat\w*|asacchikat\w*": 1, r"anupavādak\w*": 1,
    r"asaṃvar\w*": 1, r"adinnādāy\w*": 1, r"asañña(?!kath|-|satt(?!āvās))\w*": 1, r"antarāparinibbāy\w*|(?<!s)asaṅkhāraparinibbāy\w*": 1, r"nevasaññānāsaññāyatan\w*": 3,
    r"adukkhamasukh\w*": 2, r"avedanā": 1, r"ākāsānañcāyatan\w*|viññāṇañcāyatan\w*|ākiñcaññāyatan\w*": 1,
    r"(?<!arahā )anāsav\w*|aniyyānik\w*": 1, r"anuppādadhamm\w*": 1, r"anabhāvaṅkat\w*": 1, r"abbokiṇṇaṃ": 1,
    r"rūparāgaarūparāgamānauddhaccaavijjāya": 2, r"anottapp\w*": 1, r"abuddho": 1, r"asāvako": 1, r"ananussutesu": 1,
    r"aparihīno": 1, r"adaṇḍena|asatthena": 1, r"anupalitto": 1, r"appahāya": 1, r"anaññā": 1,
    r"asaṃkilesiy\w*|asaṃyojaniy\w*": 1,
    # ---- chapters 17-20
    r"anicc\w*": 1, r"addhuvato|atāṇato|aleṇato|asaraṇato|asaraṇībhūtato": 1, r"anatt[āa]\w*": 1,
    r"anārammaṇ\w*": 1, r"aganthaniy\w*|anoghaniy\w*|ayoganiy\w*|anīvaraṇiy\w*|anupādāniy\w*": 1,
    r"aññāṇakaraṇ\w*": 1, r"acakkhukaraṇ\w*": 1, r"anibbānasaṃvattaniy\w*": 1, r"avighātapakkhiy\w*": 1,
    r"\w*[aā]byākat\w*": 2, r"ahirik\w*": 1, r"avitakko": 1, r"avicāro": 1,
    r"aphassakassa|avedanakassa|acetanakassa|acittakassa": 1,
    r"anāvaṭṭentassa|appaṇidahantassa": 1, r"ajātaṃ|abhūtaṃ|asañjātaṃ|anibbattaṃ|anabhinibbattaṃ|apātubhūtaṃ": 1,
    r"aniruddhe": 1, r"asambhinn\w*": 1, r"asamannāhārā|amanasikārā|abbokiṇṇā|apubbaṃ|acarimaṃ": 1, r"anābhog\w*": 1,
    r"\w*akusal\w*": 0, r"sāvajjānavajj\w*": 1, r"asabbhi": 1, r"acetasik\w*": 1, r"aniṭṭhaphal\w*": 1,
    r"aphalaṃ": 1, r"avipāk\w*": 1, r"aviññatti": 1, r"apuññañca": 1, r"aññāṇe": 1, r"ahetuk\w*": 1,
    r"agāravo": 1, r"abhabbo": 1, r"aniñjamāno|abhāsamāno": 1, r"asati": 1, r"\w+[iu]ndriyaasaṃvar\w*": 1, r"anupādāparinibbān\w*": 1,
    r"appaṭisaṃviditvā": 1, r"amanussitthiyā": 1, r"aparāmaṭṭh\w*": 1, r"nānubyañjanaggāhī": 1, r"adinnādān\w*": 1,
}
PRIV_RX = [(re.compile(r"\b(?:" + k + r")(?:ti)?\b"), v) for k, v in PRIV.items()]
# harmonise B3: «ဆုံးမ» (ovāda, pi-4 ovadati) is no negation
NOT_NEG = ["ဆုံးမ", "မနော", "မထေရ်", "မဟာ", "မဂဓ", "ကာမ", "သို့မဟုတ်", "မတုန်မလှုပ်", "မဏိ", "မြင်းမ",
           "မာရ်", "မိန်းမ", "မနောဖြင့်", "အာမခံ"]   # nouns, not negations
MY_NEG = re.compile(r"(?<![္])မ(?=[က-အ](?![့်္]))")


def p_negs(p):
    s = nobr(body(p)).lower()
    s = re.sub(r"\b(?:na hevaṃ vattabbe|na vattabb(?:aṃ|ā|o)|no ca vata re vattabbe|no ca vattabbe|no ce pana vattabbe)\b",
               " NEG ", s)
    s = s.replace(", nanu pañcaviññāṇā", ", pañcaviññāṇā")          # ^5-576/580/584: «Nanu … nanu …» = one question
    n = s.count(" NEG ") + len(NEG_RX.findall(s))
    s = re.sub(r"nti\b", "ṃti", s)
    for rx, k in PRIV_RX:
        n += k * len(rx.findall(s))
    return n


def m_negs(m):
    s = nobr(body(m))
    for w in NOT_NEG:
        s = s.replace(w, "")
    s = re.sub(r"မဆို(?!သင့်)", "", s)
    return len(MY_NEG.findall(s))


n_neg = 0
for name, (P, M) in PAIRS.items():
    for i, (p, m) in enumerate(zip(P, M), 1):
        if F.HEAD_RE.fullmatch(body(p)) or F.norm_pe(F.strip_q(F.BR_RE.sub("", body(p)))).rstrip(".") in F.COLO:
            continue
        a, b = p_negs(p), m_negs(m)
        n_neg += a
        if a != b:
            msg = f"B2d {name}:{i} negations Pāli {a} vs Burmese {b}"
            if "--why" in sys.argv:
                t = nobr(body(m))
                for w in NOT_NEG:
                    t = t.replace(w, "")
                msg += "\n      M: " + " | ".join(t[max(0, x.start() - 8):x.start() + 7] for x in MY_NEG.finditer(t))
                sl = re.sub(r"nti\b", "ṃti", nobr(body(p)).lower())
                msg += "\n      P: " + " ".join(NEG_RX.findall(sl)) + " / " + " ".join(
                    x for rx, _ in PRIV_RX for x in rx.findall(sl))
            bad.append(msg)
print(f"B2d negations: {n_neg} (every Pāli negator / privative = one negative «မ»)")

# ===================================================================================== B7 existence polarity
EXEMPT = (r"ākāsānañc|viññāṇañc|ākiñcaññ|nāsaññ|(?<!s)asaṅkhāraparinibb|asaṅkhat|anabhāvaṅkat|niraggaḷ|\bavipāk|\baphal"      # fixed Burmese with «မရှိ» (+ anabhāvaṅkata, niraggaḷa «… မရှိသူ» of ch2-5, avipāka / aphala «… မရှိသော»: harmonise B2 / B3 / B6)
          r"|\banimitt|appaṇihit|appapaṇihit|anaṅgaṇ|\barūpāvacar|arūparāg|\bassaddh|adibbacakkhuk|\basañña(?!kath|-|satt(?!āvās))"
          r"|\bna vijjat"                                                      # ch11-12 words / «na vijjati»
          r"|\banārammaṇ|\baphassakassa|\bavedanakassa|\bacetanakassa|\bacittakassa|\bavitakk|\bavicār|anupādāparinibb"
          r"|\basamannāhār|\bapubbaṃ|\bacarimaṃ|\banābhogā|sāvajjānavajj|\baphalaṃ|\bahetuk|\basati\b")   # ch17-20 words
n_ex = 0
for name, (P, M) in PAIRS.items():
    for i, (p, m) in enumerate(zip(P, M), 1):
        s = nobr(body(p)).lower().replace("na me ācariyo atthi", "natthi me ācariyo")   # ^5-405 verse
        neg = len(re.findall(r"(?<![^\W\d_])natth|\bna atth(?=i|ī)", s)) + len(re.findall(EXEMPT, s))
        pos = len(re.findall(r"(?<![^\W\d_])atth(?:i|ī|aṭṭh|ibhāv)", s))
        mb = nobr(body(m))
        gneg = mb.count("မရှိ")
        gpos = mb.count("ရှိ") - gneg
        n_ex += neg + pos
        if gneg != neg or gpos < pos:
            bad.append(f"B7 {name}:{i} existence Pāli neg {neg} pos {pos} vs Burmese «မရှိ» {gneg} «ရှိ» {gpos}")
print(f"B7 existence polarity: {n_ex} marks (natthi = «မရှိ», atthi ≤ «ရှိ»)")


# ===================================================================================== B3 number words
NUMW = [(r"\bdvinnaṃ\b|\bdve\b|\bdvemā\b", F.NUM_MY[2]), (r"\bpañcannaṃ\b|\bpañca(?=vokār)|\bpañceva\b",
                                                          F.NUM_MY[5]),
        (r"\bdvādasannaṃ\b", F.NUM_MY[12]), (r"\baṭṭhārasannaṃ\b", F.NUM_MY[18]),
        (r"\bbāvīsatīnaṃ\b", F.NUM_MY[22]), (r"\bekassa\b|\bekova\b|\beka(?=vokār)|\bekapuggalo\b", F.NUM_MY[1]),
        (r"\bcatunnaṃ\b|\bcatu(?=vokār)|\bcattārova?\b", F.NUM_MY[4]), (r"\baṭṭha\b", F.NUM_MY[8]),
        (r"\btayo\b|\btīṇimāni\b", F.NUM_MY[3]), (r"\bsattakkhattu", F.NUM_MY[7]),
        (r"\bpaṭhamo\b", F.ORD_MY[1]), (r"\bdutiyo\b|\bdutiye\b", F.ORD_MY[2]), (r"\btatiyo\b|\btatiyā\b", F.ORD_MY[3]),
        (r"\bcatuttho\b", F.ORD_MY[4]), (r"\bpañcamo\b|\bpañcamaṃ\b", F.ORD_MY[5]), (r"\bchaṭṭho\b", F.ORD_MY[6]),
        (r"\bsattamo\b", F.ORD_MY[7]), (r"\bcattāro\b|\bcattāri\b|\bcatūhi\b", F.NUM_MY[4]),
        (r"\bdasa\b", F.NUM_MY[10]), (r"\bpañca\b|\bpañcime\b", F.NUM_MY[5]), (r"\bsattannaṃ\b", F.NUM_MY[7]),
        (r"\bdvinnaṃ\b", F.NUM_MY[2]), (r"\baṭṭhamo\b|\baṭṭhamaṃ\b|\baṭṭhaka", F.ORD_MY[8] + "|" + F.NUM_MY[8])]
NUMW += [(r"\bnavannaṃ\b|\bnava\b|\bnavannaṃ\b", F.NUM_MY[9]), (r"\bdasannaṃ\b", F.NUM_MY[10]),
         (r"\bchannaṃ\b", F.NUM_MY[6]), (r"\bpannarasahi\b", "ဆယ့်ငါး"), (r"chattiṃs", "သုံးဆယ့်ခြောက်"),
         (r"catupaññās", "ငါးဆယ့်လေး"), (r"chasaṭṭh", "ခြောက်ဆယ့်ခြောက်"), (r"\bdvādasahi\b", F.NUM_MY[12]),
         (r"\baṭṭhārasahi\b", F.NUM_MY[18]), (r"\bpañcahi\b", F.NUM_MY[5]), (r"\bsatta\b", F.NUM_MY[7]),
         (r"\bcatunnaṃ\b", F.NUM_MY[4]), (r"\baṭṭhavimokkh", F.NUM_MY[8])]   # ch17-20
NUMW += [(r"\btīṇi\b|\btīṇeva\b|\btīhi\b|\btisso\b", F.NUM_MY[3]), (r"\bdvīhi\b|\bdveva\b", F.NUM_MY[2]),
         (r"\bchahi\b|\bcha\b", F.NUM_MY[6]), (r"\bekaṃyeva\b|\bekaññeva\b", F.NUM_MY[1])]   # ch11-12
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
    stack, err = [], None
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
    return err if not stack else f"{len(stack)} quote(s) left open"


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
ALLP = dict(PAIRS)
for name in SAMPLE:
    ALLP[name] = (nonempty(MS.PALI / name), nonempty(MS.OUT / name))
for name, (P, M) in ALLP.items():
    for i, (p, m) in enumerate(zip(P, M), 1):
        b = body(p)
        if F.HEAD_RE.fullmatch(b):
            continue
        clean = F.BR_RE.sub("", b)
        key_line = F.norm_pe(F.strip_q(clean))
        if key_line in F.LINES or key_line.rstrip(".") in F.COLO or any(rx.fullmatch(key_line) for rx, _ in F.LINE_FRAMES):
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
n_samp = sum(1 for _k, lst in occ.items() if len(lst) > 1 and {x[0] for x in lst} & set(SAMPLE)
             and {x[0] for x in lst} & set(NAMES))
print(f"B5 recurring sentences: {s_rec} / {n_rec} occurrences identical; {n_samp} sentences shared with the sample "
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
# C1 topic names
n_c1 = s_c1 = 0
for name, (P, M) in PAIRS.items():
    for i, (p, m) in enumerate(zip(P, M), 1):
        words = re.findall(r"[^\W\d]+", nobr(body(p)).lower())
        toks = set(words) | {f"{a} {b}" for a, b in zip(words, words[1:])}
        for form, (n, roles) in F.NOUN.items():
            if not (n in F.KHANDHA5 or n in F.AYATANA.values() or n in F.DHATU.values() or n in F.INDRIYA.values()):
                continue
            # rūpadhātuyā = the fine-material realm; rūpā = abl. sg. or nom. pl. «visible forms» (C3, pi-2 ^2-154)
            if form in ("rūpadhātuyā", "rūpadhātuṃ", "rūpā") or form not in toks:
                continue
            if form == "rūpaṃ" and re.search(r"cakkhunā rūpaṃ", nobr(body(p))):
                continue          # «cakkhunā rūpaṃ passati» = «… အဆင်းအရောင်ကို မြင်» (pi-1 ^1-1352, visible form)
            n_c1 += 1
            if n.my in m or (n.pl and n.my[:-len("တို့")] in m):
                s_c1 += 1
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
# C3 reused terms: (regex on the sample Pāli, Burmese, book, block id, Pāli witness in that rails segment)
_SV = "ထာဝရ တည်မြဲသည်ဟု ဆိုသော ဝါဒ ရှိသော ဆရာ"
REUSE = [
    (r"puggal", F.PUGGALA, "2", "^2-643", "ekaṃ puggalaṃ"),
    (r"bhagav", F.BHAGAVA, "1", "^T-1", "bhagavato"),
    (r"taṃ jīvaṃ taṃ sarīr", "အသက်သည် ကိုယ်ခန္ဓာပင် ဖြစ်", "1", "^1-1105", "taṃ jīvaṃ taṃ sarīr"),
    (r"aññaṃ jīvaṃ,? aññaṃ sarīr", "အသက်နှင့် ကိုယ်ခန္ဓာသည် တခြားစီ ဖြစ်", "1", "^1-1105", "aññaṃ jīvaṃ aññaṃ sarīr"),
    (r"sappaccay", "အကြောင်း ရှိသော", "1", "^1-M2-7", "sappaccayā dhammā"),
    (r"saṅkhat(?!assa saṅkhatalakkhaṇāni)", "ပြုပြင်ဖန်တီးထား", "1", "^1-M2-8", "saṅkhatā dhammā"),
    (r"sanidassan", "မြင်နိုင်သော", "1", "^1-M2-9", "sanidassanā dhammā"),
    (r"sappaṭigh", "ထိခိုက်မှု ရှိသော", "1", "^1-M1-22", "anidassanasappaṭighā dhammā"),
    (r"nimitt", "အမှတ်အသား", "1", "^1-M2-133", "samathanimittañca"),
    (r"sassat", "ထာဝရ", "1", "^1-1105", "Sassato lokoti"),
    (r"nibbān", F.NIBBANA, "1", "^1-1386", "nibbānañca"),
    (r"\bsatt(?:o|ā|e|ānaṃ|upalabbhati)\b", F.SATTA, "1", "^1-645", "sattā yāpenti"),
    (r"khattiy", "မင်းမျိုး", "2", "^2-974", "Khattiyosmīti"),
    (r"brāhmaṇ", "ပုဏ္ဏား", "2", "^2-974", "brāhmaṇosmīti"),
    (r"\bvess", "ကုန်သည်မျိုး", "2", "^2-974", "vessosmīti"),
    (r"\bsuddo\b", "သူဆင်းရဲမျိုး", "2", "^2-974", "suddosmīti"),
    (r"gahaṭṭh", "လူဝတ်ကြောင်", "2", "^2-974", "gahaṭṭhosmīti"),
    (r"pabbajit", "ရဟန်း", "2", "^2-974", "pabbajitosmīti"),
    (r"\bmātā\b", "အမိ", "1", "^1-1221", "natthi mātā"),
    (r"\bpitā\b", "အဖ", "1", "^1-1221", "natthi pitā"),
    (r"\bbhātā\b", "ညီအစ်ကို", "2", "^2-200", "bhātā vā"),
    (r"\bbhaginī\b", "ညီအစ်မ", "2", "^2-200", "bhaginī vā"),
    (r"upādāya", "မှီ၍", "1", "^1-616", "catunnaṃ mahābhūtānaṃ upādāya"),
    (r"paññatt", "သတ်မှတ်", "1", "^1-M2-108", "paññatti dhammā"),
    (r"sotāpann", "သောတာပန်", "4", "^4-M-7", "Sotāpanno"),
    (r"sakadāgām(?!i(?:magg|phal))", "သကဒါဂါမ်", "4", "^4-M-7", "Sakadāgāmī"),
    (r"anāgām(?!i(?:magg|phal))", "အနာဂါမ်", "4", "^4-M-7", "Anāgāmī"),
    (r"\barahā\b", "ရဟန္တာ", "4", "^4-11", "Arahā abhayūparato"),
    (r"ubhatobhāgavimutt", "နှစ်ဖက်စလုံးမှ လွတ်မြောက်သူ", "4", "^4-M-7", "Ubhatobhāgavimutto"),
    (r"paññāvimutt", "ပညာဖြင့် လွတ်မြောက်သူ", "4", "^4-M-7", "Paññāvimutto"),
    (r"kāyasakkh", "ကိုယ်ဖြင့် မျက်မှောက်ပြုသူ", "4", "^4-M-7", "Kāyasakkhī"),
    (r"diṭṭhippatt", "မှန်ကန်သော အယူသို့ ရောက်သူ", "4", "^4-M-7", "Diṭṭhippatto"),
    (r"saddhāvimutt", "ယုံကြည်မှုဖြင့် လွတ်မြောက်သူ", "4", "^4-M-9", "saddhāvimutto"),
    (r"dhammānusār", "တရားကို အစဉ်လိုက်သူ", "4", "^4-M-7", "Dhammānusārī"),
    (r"saddhānusār", "ယုံကြည်မှုကို အစဉ်လိုက်သူ", "4", "^4-M-7", "Saddhānusārī"),
    (r"attahitāya paṭipann", "မိမိ၏ အကျိုးအတွက် ကျင့်ကြံ", "4", "^4-M-10", "attahitāya paṭipanno"),
    (r"suttant", "သုတ္တန်", "1", "^1-M-2-14-0", "Suttantikadukamātikā"),
    (r"dibbena cakkhunā visuddhena atikkantamānusakena", F.DIBBACAKKHU, "4", "^4-184",
     "dibbena cakkhunā visuddhena atikkantamānusakena"),
    (r"cavamāne upapajjamāne", F.CUTUPAPATA, "4", "^4-184", "cavamāne upapajjamāne hīne paṇīte"),
    (r"yathākammūpage satte", F.YATHAKAMMA, "4", "^4-184", "yathākammūpage satte pajānāti"),
    (r"pubbenivās", F.PUBBENIVASA, "4", "^4-183", "pubbenivāsaṃ anussarati"),
    (r"paracitt", F.PARACITTA, "2", "^2-805", "paracitte ñāṇaṃ"),
    (r"āsavānaṃ khay", F.ASAVAKHAYA, "2", "^2-805", "āsavānaṃ khaye ñāṇaṃ"),
    (r"iddhi", F.IDDHI, "2", "^2-805", "Iddhividhe ñāṇaṃ"),
    (r"sotadhātu", "နား ဓာတ်", "2", "^2-805", "sotadhātuvisuddhiyā ñāṇaṃ"),
    (r"kāye kāyānupass", "ကိုယ်၌ ကိုယ်ကို အဖန်ဖန် ရှုသူ", "2", "^2-205", "kāye kāyānupassī viharati"),
    (r"dhammesu dhammānupass", F.DHAMMANUPASSI, "2", "^2-487", "dhammesu dhammānupassī viharati"),
    (r"dukkhassa(?:nta| anta)", F.DUKKHA_END, "4", "^4-31", "dukkhassantaṃ karoti"),
    (r"sammādiṭṭhi", "မှန်ကန်သော အယူ", "1", "^1-1", "sammādiṭṭhi hoti"),
    (r"micchā(?:diṭṭhi|saṅkapp|vāc|kammant|ājīv|vāyām|sati|samādhi)", "မှားယွင်းသော", "2", "^2-U30",
     "Micchādiṭṭhi, micchāsaṅkappo"),
    (r"pāṇātipāt(?!ino)", "သူ့အသက်ကို သတ်ခြင်း", "2", "^2-487", "Pāṇātipātā veramaṇī"),
    (r"nerayik", "ငရဲ", "2", "^2-1009", "nerayikānaṃ"),
    (r"tiracchānagat", "တိရစ္ဆာန်", "2", "^2-1009", "tiracchānagatānaṃ"),
    (r"\bpeto\b", "ပြိတ္တာ", "2", "^2-1009", "petānaṃ"),
    (r"saṅgh", "သံဃာ", "2", "^2-932", "saṅghaṃ vā"),
    (r"kaṅkhati", "သံသယ", "1", "^1-425", "kaṅkhā"),
    (r"vicikicchati", "ယုံမှား", "1", "^1-425", "vicikicchā hoti"),
    (r"sappi", "ထောပတ်ကြည်", "1", "^1-645", "sappi"),
    (r"telakumbh", "ဆီ", "1", "^1-645", "telaṃ"),
    (r"madhukumbh", "ပျားရည်", "1", "^1-645", "madhu"),
    (r"phāṇitakumbh", "တင်လဲ", "1", "^1-645", "phāṇitaṃ"),
    (r"khīrakumbh", "နွားနို့", "1", "^1-645", "khīraṃ"),
    (r"nīlaṃ pītakaṃ lohitakaṃ odātaṃ", "အပြာ၊ အဝါ၊ အနီ၊ အဖြူ", "1", "^1-616", "nīlaṃ pītakaṃ lohitakaṃ odātaṃ"),
    (r"\bnīl", "အပြာ", "1", "^1-616", "nīlaṃ"),
    (r"cakkhuviññeyy", "မျက်စိဖြင့် သိနိုင်သော", "1", "^1-588", "Cakkhuviññeyyaṃ rūpaṃ"),
    (r"ekavokār", "အစုအဝေး တစ်ပါး ရှိသော ဘဝ", "2", "^2-234", "ekavokārabhavo"),
    (r"catuvokār", "အစုအဝေး လေးပါး ရှိသော ဘဝ", "2", "^2-234", "catuvokārabhavo"),
    (r"pañcavokār", "အစုအဝေး ငါးပါး ရှိသော ဘဝ", "2", "^2-234", "pañcavokārabhavo"),
    (r"attānaṃ saccato thetato", "အတ္တကို အမှန်အားဖြင့် ခိုင်မြဲစွာ", "4", "^4-131", "attānaṃ saccato thetato"),
    (r"santo saṃvijjamānā lokasmi", "လောက၌ ရှိကြ၏၊ ထင်ရှား ရှိကြ၏", "4", "^4-94", "santo saṃvijjamānā lokasmiṃ"),
    (r"diṭṭhe ceva dhamme|diṭṭheva dhamme", "မျက်မှောက်ဘဝ၌ပင်", "4", "^4-131", "diṭṭhe ceva dhamme"),
    (r"abhisamparāyañca", "တမလွန်ဘဝ၌လည်း", "4", "^4-131", "abhisamparāyañca"),
    (r"sassatavādo", _SV, "4", "^4-131", "sassatavādo satthā"),
    (r"ucchedavādo", "ပြတ်စဲသွားသည်ဟု ဆိုသော ဝါဒ", "2", "^2-977", "ucchedavādā"),
    (r"sammāsambuddh", "အမှန်ကို ကိုယ်တိုင် အပြည့်အဝ သိမြင်တော်မူသော ဘုရားရှင်", "1", "^T-1",
     "sammāsambuddhassa"),
    (r"\bevamevaṃ", "ထို့အတူပင်", "4", "^4-94", "Evamevaṃ"),
    (r"samphass", "တွေ့ထိမှု", "1", "^1-1", "phasso hoti"),
    (r"suññ", "ဆိတ်သုဉ်း", "1", "^1-1-1-3-0", "Suññatavāro"),
    (r"\bcuto\b", "သေ၍", "4", "^4-40", "avihā cuto"),
    (r"\brūpā suññā", "အဆင်းအရောင်တို့", "2", "^2-154", "Rūpā aniccā"),
    (r"adukkhamasukh", "မနာကျင် မသာယာ", "1", "^1-M1-2", "adukkhamasukhāya vedanāya"),
    (r"khandh", F.KHANDHA_W, "2", "^2-1", "Pañcakkhandhā"),
    (r"(?<!ānañc)(?<!ṇañc)(?<!ākiñcaññ)(?<!nāsaññ)(?<!phass)āyatan(?!ūpag)", F.AYATANA_W, "2", "^2-154", "Dvādasāyatanāni"),
    (r"indriy", F.INDRIYA_W, "2", "^2-219", "Bāvīsatindriyāni"),
    (r"vipariṇāmadhamm", "ဖောက်ပြန်ပြောင်းလဲတတ်သော သဘော", "2", "^2-943", "vipariṇāmadhammā"),
    (r"khayadhamm\S* vayadhamm\S* virāgadhamm\S* nirodhadhamm",
     "ကုန်ခန်းတတ်သော သဘော၊ ပျက်စီးတတ်သော သဘော၊ ပြယ်ပျောက်တတ်သော သဘော၊ ချုပ်ငြိမ်းတတ်သော သဘော", "2", "^2-806",
     "khayadhammaṃ vayadhammaṃ virāgadhammaṃ nirodhadhamma"),
    (r"paṭiccasamuppann", "အကြောင်းတို့ကို မှီ၍ ဖြစ်ပေါ်လာသော", "1", "^1-57", "paṭiccasamuppannā"),
    (r"\banicc", "မမြဲ", "2", "^2-154", "Cakkhuṃ aniccaṃ"),
    (r"anattā", "အတ္တ မဟုတ်", "2", "^2-154", "anattā"),
    (r"saṅkhār(?!aparinibb)", "ပြုပြင်ဖန်တီးမှု", "2", "^2-1", "saṅkhārakkhandho"),
    (r"vedan|(?<!saka)(?<!para)vediy|vedayit", "ခံစား", "2", "^2-1", "vedanākkhandho"),
    (r"\bsaññ|sasañño|asañño", "မှတ်သိမှု", "2", "^2-1", "saññākkhandho"),
    (r"viññāṇ(?!añcāyatan)", "သိစိတ်", "2", "^2-1", "viññāṇakkhandho"),
    (r"āsav", "စိတ်အစွန်းအထင်း", "2", "^2-805", "āsavānaṃ khaye"),
    (r"parinibb", "ပရိနိဗ္ဗာန် ပြု", "4", "^4-M-7", "parinibbāyī"),
    # ---- chapters 6 … 10
    (r"\batīt", "အတိတ်", "1", "^1-M1-18", "atītā dhammā"),
    (r"anāgat", "အနာဂတ်", "1", "^1-M1-18", "anāgatā dhammā"),
    (r"paccuppann", "ပစ္စုပ္ပန်", "1", "^1-M1-18", "paccuppannā dhammā"),
    (r"avipakkavipāk", "အကျိုး မရင့်ကျက်သေးသော", "1", "^1-1043", "avipakkavipākānaṃ"),
    (r"uppādino", "ဖြစ်ပေါ်လာမည့်", "1", "^1-1043", "dhammā uppādino"),
    (r"satipaṭṭhān", "သတိပဋ္ဌာန်", "2", "^2-7-0", "Satipaṭṭhānavibhaṅgo"),
    (r"(?<!bāvī)satindriy", "သတိ၏ စွမ်းရည်", "1", "^1-290", "satindriyaṃ"),
    (r"satibal", "သတိ၏ စွမ်းအား", "1", "^1-290", "satibalaṃ"),
    (r"sammāsati", "မှန်ကန်သော သတိ", "1", "^1-290", "sammāsati"),
    (r"satisambojjhaṅg", "သတိ ဗောဇ္ဈင်", "1", "^1-290", "satisambojjhaṅgo"),
    (r"(?<!na )apacayagām", "လျော့ပါးခြင်းဆီသို့ ဦးတည်သော", "1", "^1-M1-10", "apacayagāmino dhammā"),
    (r"\banāsav", "စိတ်အစွန်းအထင်း၏ အာရုံ မဖြစ်နိုင်သော", "1", "^1-M2-15", "anāsavā dhammā"),
    (r"aparāmaṭṭh", "မှားယွင်းသော ယူဆမှု၏ အာရုံ မဖြစ်နိုင်သော", "1", "^1-M2-51", "aparāmaṭṭhā dhammā"),
    (r"sammappadhān", "မှန်ကန်သော ကြိုးပမ်းအားထုတ်ခြင်း", "2", "^2-8-0", "Sammappadhānavibhaṅgo"),
    (r"iddhipād", "ဣဒ္ဓိပါဒ်", "2", "^2-9-0", "Iddhipādavibhaṅgo"),
    (r"bojjhaṅg", "ဗောဇ္ဈင်", "2", "^2-10-0", "Bojjhaṅgavibhaṅgo"),
    (r"\brāg", "ရာဂ", "1", "^1-361", "kāmarāgabyāpādānaṃ"),
    (r"\bdos", "ဒေါသ", "1", "^1-1235", "doso"),
    (r"\bmoh", "မောဟ", "1", "^1-1235", "moho"),
    (r"\bthin", "ထိုင်းမှိုင်းမှု", "1", "^1-1235", "thinaṃ"),
    (r"uddhacc", "ယောက်ယက်ခတ်မှု", "1", "^1-1235", "uddhaccaṃ"),
    (r"ahirik", "ဒုစရိုက်ကို မရှက်မှု", "1", "^1-1235", "ahirīkaṃ"),
    (r"anottapp", "ဒုစရိုက်ကို မကြောက်ရွံ့မှု", "1", "^1-1235", "anottappaṃ"),
    (r"dhammavicayasambojjhaṅg", "သဘောတရားများကို စိစစ်ခြင်း ဗောဇ္ဈင်", "2", "^2-466", "dhammavicayasambojjhaṅgo"),
    (r"passaddhisambojjhaṅg", "ငြိမ်းအေးခြင်း ဗောဇ္ဈင်", "2", "^2-466", "passaddhisambojjhaṅgo"),
    (r"satthari", "ဘုရားရှင်အပေါ်", "2", "^2-915", "Satthari kaṅkhati"),
    (r"idapp?accayatāpaṭiccasamuppannesu", "ဤအကြောင်းကြောင့် ဤအကျိုး ဖြစ်ပုံ", "2", "^2-915",
     "idappaccayatāpaṭiccasamuppannesu dhammesu"),
    (r"vimati", "စိတ်ရှုပ်ထွေးခြင်း", "1", "^1-1008", "vimati"),
    (r"sakkāyadiṭṭh", "ကိုယ်ကို အတ္တဟု ယူဆသော အယူ", "2", "^2-915", "sakkāyadiṭṭhi"),
    (r"sīlabbataparāmās", "သီလ အကျင့်ဝတ်ဆိုင်ရာ မှားယွင်းသော ယူဆမှု", "2", "^2-915", "sīlabbataparāmāso"),
    (r"cīvarapiṇḍapātasenāsanagilānapaccayabhesajjaparikkhār",
     "သင်္ကန်း၊ ဆွမ်း၊ ကျောင်းအိပ်ရာနေရာ၊ သူနာ၏ အထောက်အပံ့ ဖြစ်သော ဆေးအသုံးအဆောင်", "2", "^2-929",
     "cīvarapiṇḍapātasenāsanagilānapaccayabhesajjaparikkhārehi"),
    (r"sotāpattiphal", "သောတာပတ္တိဖိုလ်", "2", "^2-807", "sotāpattiphale"),
    (r"lokiy", "လောကနှင့် သက်ဆိုင်သော", "1", "^1-M2-12", "lokiyā dhammā"),
    (r"lokuttar", "လောကကို ကျော်လွန်သော", "1", "^1-M2-12", "lokuttarā dhammā"),
    (r"pathavīkasiṇ", "မြေ ကသိုဏ်း", "1", "^1-165", "pathavīkasiṇaṃ"),
    (r"viññāṇañcāyatan", "အဆုံး မရှိသော သိစိတ် နယ်ပယ်", "1", "^1-1432", "Viññāṇañcāyatanaṃ"),
    (r"nevasaññānāsaññāyatan", "မှတ်သိမှု ရှိသည်လည်း မဟုတ်၊ မှတ်သိမှု မရှိသည်လည်း မဟုတ်သော နယ်ပယ်", "1", "^1-1432",
     "nevasaññānāsaññāyatanaṃ"),
    (r"uccārapassāv", "ကျင်ကြီး ကျင်ငယ်", "2", "^2-508", "uccārapassāvakamme"),
    (r"tāvatiṃs", "တာဝတိံသာ", "2", "^2-1023", "Tāvatiṃsānaṃ"),
    (r"akaniṭṭhān", "အကနိဋ္ဌ", "2", "^2-1027", "Akaniṭṭhānaṃ"),
    (r"āyuppamāṇ", "သက်တမ်း အတိုင်းအတာ", "2", "^2-1027", "āyuppamāṇaṃ"),
    (r"catusaṭṭhi kapp", "ခြောက်ဆယ့်လေးကမ္ဘာ", "2", "^2-1026", "Catusaṭṭhi kappā"),
    (r"sattakkhattuparam", "အများဆုံး ခုနစ်ကြိမ်သာ ပြန်လည် ဖြစ်ပေါ်သူ", "4", "^4-M-7", "Sattakkhattuparamo"),
    (r"kolaṅkol", "အမျိုးမှ အမျိုးသို့ ကူးသူ", "4", "^4-M-7", "Kolaṅkolo"),
    (r"ekabīj", "မျိုးစေ့ တစ်စေ့သာ ရှိသူ", "4", "^4-M-7", "Ekabījī"),
    (r"antarāparinibb", "သက်တမ်း၏ အလယ်သို့ မရောက်မီ ပရိနိဗ္ဗာန် ပြုသူ", "4", "^4-M-7", "Antarāparinibbāyī"),
    (r"upahaccaparinibb", "သက်တမ်း၏ အလယ်ကို ကျော်ပြီးမှ ပရိနိဗ္ဗာန် ပြုသူ", "4", "^4-M-7", "Upahaccaparinibbāyī"),
    (r"(?<!s)asaṅkhāraparinibb", "တိုက်တွန်းမှု မရှိဘဲ ပရိနိဗ္ဗာန် ပြုသူ", "4", "^4-M-7", "Asaṅkhāraparinibbāyī"),
    (r"sasaṅkhāraparinibb", "တိုက်တွန်းမှုဖြင့် ပရိနိဗ္ဗာန် ပြုသူ", "4", "^4-M-7", "Sasaṅkhāraparinibbāyī"),
    (r"uddhaṃsoto akaniṭṭhagām", "အထက်သို့ စီးဆင်း၍ အကနိဋ္ဌ ဘုံသို့ ရောက်သူ", "4", "^4-M-7",
     "Uddhaṃsotoakaniṭṭhagāmī"),
    (r"sotāpattiphalasacchikiriyāya paṭipann", "သောတာပတ္တိဖိုလ်ကို မျက်မှောက်ပြုရန် ကျင့်ကြံ", "4", "^4-M-7",
     "Sotāpattiphalasacchikiriyāya paṭipanno"),
    (r"arahattaphal", "ရဟန္တာ ဖိုလ်", "1", "^1-1024", "arahattaphalaṃ"),
    (r"rūpasaññ", "ရုပ်ဟု မှတ်သိမှု", "1", "^1-265", "rūpasaññānaṃ"),
]
REUSE += [  # ---- chapters 11-12 (bid None: the first FINAL segment holding both is the witness)
    (r"tathāgatabal", "ဘုရားဆိုင်ရာ စွမ်းအား", "2", "^2-760", "tathāgatabalaṃ hoti"),
    (r"yathābhūtaṃ ñāṇaṃ", "ဟုတ်မှန်သည့်အတိုင်း သိသော ဉာဏ်", "2", "^2-809", "yathābhūtaṃ ñāṇaṃ"),
    (r"ṭhānāṭhān", "ဖြစ်နိုင်သော အကြောင်း", "2", "^2-760", "ṭhānañca ṭhānato aṭṭhānañca"),
    (r"kammasamādānānaṃ", "ကံ ဆောက်တည်မှုတို့၏ အကျိုးကို ဖြစ်ရာ အခြေအနေအားဖြင့်၊ အကြောင်းရင်းအားဖြင့်", "2", "^2-760",
     "kammasamādānānaṃ ṭhānaso hetuso vipākaṃ"),
    (r"sabbatthagāmin", "ဘုံ အားလုံးသို့ ရောက်စေသော ကျင့်စဉ်", "2", "^2-760", "sabbatthagāminiṃ paṭipadaṃ"),
    (r"anekadhātu", "ဓာတ် များပြား၍ ဓာတ် အမျိုးမျိုး ရှိသော လောက", "2", "^2-760", "anekadhātu nānādhātulokaṃ"),
    (r"nānādhimuttikat", "စိတ်ညွတ်ရာ အမျိုးမျိုး ကွဲပြားခြင်း", "2", "^2-760", "sattānaṃ nānādhimuttikataṃ"),
    (r"indriyaparopariyatt", "စွမ်းရည်တို့ မြင့်မြတ်ခြင်း နိမ့်ကျခြင်း", "2", "^2-760", "indriyaparopariyattaṃ"),
    (r"jhānavimokkhasamādhisamāpatt", "ဈာန်၊ လွတ်မြောက်ခြင်း၊ သမာဓိ၊ ဈာန် ဝင်စားရာတို့၏ ညစ်နွမ်းခြင်း၊ စင်ကြယ်ခြင်း၊ "
     "ထမြောက်ခြင်း", "2", "^2-760", "jhānavimokkhasamādhisamāpattīnaṃ saṃkilesaṃ vodānaṃ vuṭṭhānaṃ"),
    (r"cutūpapāt", "သတ္တဝါတို့၏ သေခြင်းနှင့် ဖြစ်ပေါ်ခြင်း", "2", "^2-760", "sattānaṃ cutūpapātaṃ"),
    (r"\bsarāg", "ရာဂ ရှိ", "2", "^2-796", "Sarāgaṃ vā cittaṃ"), (r"\bsados", "ဒေါသ ရှိ", "2", "^2-796", "sadosaṃ"),
    (r"\bsamoh(?!it)", "မောဟ ရှိ", "2", "^2-796", "samohaṃ"), (r"vītarāg", "ရာဂ ကင်း", "2", "^2-796", "vītarāgaṃ vā cittaṃ"),
    (r"sampayutt", "နှင့် ယှဉ်တွဲသော", "1", "^1-M2-58", "cittasampayuttā"),
    (r"saṃsaṭṭh", "နှင့် ရောနှောသော", "1", "^1-M2-59", "cittasaṃsaṭṭhā"),
    (r"sahabhu", "နှင့်အတူ တည်ရှိသော", "1", "^1-M2-61", "cittasahabhuno"),
    (r"ānuparivatt", "နောက်သို့ လိုက်ပါသော", "1", "^1-M2-62", "cittānuparivattino"),
    (r"\bsaṃyojaniy", "နှောင်ကြိုး၏ အာရုံ ဖြစ်နိုင်သော", "1", "^1-M2-21", "saṃyojaniyā dhammā"),
    (r"\bsaṃkilesiy", "ကိလေသာ၏ အာရုံ ဖြစ်နိုင်သော", "1", "^1-M2-76", "saṃkilesikā dhammā"),
    (r"(?<!a)niyyānik", "လွတ်မြောက်ရာသို့ ပို့ဆောင်သော", "1", "^1-343", "niyyānikaṃ"),
    (r"kāmāvacar", "ကာမဘုံနှင့် ဆိုင်သော", "1", "^1-M2-93", "kāmāvacarā dhammā"),
    (r"(?<!a)rūpāvacar", "သိမ်မွေ့သော ရုပ်ဘုံနှင့် ဆိုင်သော", "1", "^1-M2-94", "rūpāvacarā dhammā"),
    (r"arūpāvacar", "ရုပ်မရှိသော ဘုံနှင့် ဆိုင်သော", "1", "^1-M2-95", "arūpāvacarā dhammā"),
    (r"(?<!a)(?<!khandha)pariyāpann", "ဘဝဘုံတို့၌ အကျုံးဝင်သော", "1", "^1-M2-96", "pariyāpannā dhammā"),
    (r"(?<!khandh)apariyāpann", "ဘဝဘုံတို့၌ အကျုံးမဝင်သော", "1", "^1-M2-96", "apariyāpannā dhammā"),
    (r"\bupādiṇṇ", "ကံကြောင့် ဖြစ်", "1", "^1-M1-4", "upādiṇṇupādāniyā"),
    (r"gotrabhu", "အရိယာ အနွယ်သို့ ပြောင်း", "4", "^4-M-7", "Gotrabhū"),
    (r"\bassaddho", "ယုံကြည်မှု မရှိသူ", "2", "^2-851", "assaddho samāno"),
    (r"\bkusīto", "ပျင်းရိ", "2", "^2-851", "kusīto samāno"), (r"muṭṭhassat", "သတိ လစ်", "2", "^2-851", "muṭṭhassatī"),
    (r"\basamāhito", "စိတ် မတည်ကြည်", "2", "^2-851", "asamāhito samāno"),
    (r"duppañño", "ပညာ နည်း", "2", "^2-851", "duppañño samāno"),
    (r"pāṇātipātino", "သူ့အသက်ကို သတ်သူ", "4", "^4-132", "pāṇātipātī hoti"),
    (r"surāmerayamajjapamādaṭṭh", "သေရည် အရက် မူးယစ်ဖွယ်ဟူသော မေ့လျော့", "2", "^2-703",
     "surāmerayamajjapamādaṭṭhānā veramaṇī"),
    (r"asaññasatt(?!āvās)|asañña-satt", "အသညသတ်", "2", "^2-1015", "asaññasattānaṃ devānaṃ"),
    (r"ākāsānañcāyatan", "အဆုံး မရှိသော ဟင်းလင်းပြင် နယ်ပယ်", "1", "^1-266", "ākāsānañcāyatanaṃ"),
    (r"ākiñcaññāyatan", "ဘာမျှ မရှိသော နယ်ပယ်", "1", "^1-267", "ākiñcaññāyatanasaññāsahagataṃ"),
    (r"dibbena cakkhunā|dibbacakkh|dibbassa cakkhu", "နတ်မျက်စိ", "4", "^4-184", "dibbena cakkhunā"),
    (r"duccaritena samannāgatā", "ဖြင့် ပြုသော ဒုစရိုက်နှင့် အပြည့်အဝ ပြည့်စုံကြ", "4", "^4-184", "kāyaduccaritena"),
    (r"kāyassa bhedā", "ခန္ဓာကိုယ် ပြိုကွဲ၍", "4", "^4-184", "kāyassa bhedā"),
    (r"samāhite citte parisuddhe", "စိတ်သည် တည်ကြည်၍၊ စင်ကြယ်၍", "4", "^4-185", "samāhite citte parisuddhe"),
    (r"kāmāsav", "ကာမ စိတ်အစွန်းအထင်း", "4", "^4-185", "kāmāsavāpi"),
    (r"manasi kar", "နှလုံးသွင်း", None, None, "manasi karoti"),
    (r"niyāmaṃ okkam|okkantaniyām", "သေချာသော လမ်းကြောင်းသို့ သက်ဆင်း", "4", "^4-13", "niyāmaṃ okkamituṃ"),
    (r"caritabrahmacariy|brahmacariyaṃ acari", "မြင့်မြတ်သော အကျင့်", "2", "^2-509", "imasmiṃ brahmacariye"),
    (r"dukkarakār", "ပြုရခက်သော အကျင့်", "4", "^4-172", "dukkarakārikaṃ"),
    (r"ananussutesu", "ယခင်က မကြားဖူးသော တရားတို့၌", "4", "^4-M-12", "pubbe ananussutesu dhammesu"),
    (r"ariyasacc", "အရိယာ သစ္စာ", "2", "^2-189", "dukkhaṃ ariyasaccaṃ"),
    (r"rūparāgaarūparāg", "သိမ်မွေ့သော ရုပ်ဘဝကို တပ်မက်သော ရာဂ၊ ရုပ်မရှိသော ဘဝကို တပ်မက်သော ရာဂ", "2", "^2-U49",
     "Rūparāgo"),
    (r"upekkh", "ဥပေက္ခာ", "1", "^1-M1-7", "upekkhāsahagatā dhammā"),
    (r"\bgih", "လူဝတ်ကြောင်", "2", "^2-888", "gihīhi saṃsaṭṭho"),
    (r"cakkavattī\b", "စကြဝတေး မင်း", None, None, "rājā cakkavattī"),
]
REUSE += [  # ---- chapters 17-20
    (r"āvaṭṭanā", "စိတ်ကို လှည့်ဆောင်ခြင်း", "2", "^2-766", "āvaṭṭanā vā ābhogo"),
    (r"sārammaṇ", "အာရုံ ရှိ", "1", "^1-M2-55", "sārammaṇā dhammā"),
    (r"anārammaṇ", "အာရုံ မရှိ", "1", "^1-M2-55", "anārammaṇā dhammā"),
    (r"\bacetasik", "စိတ်၏ အဖော်", "1", "^1-M2-57", "acetasikā dhammā"),
    (r"(?<!a)cetasik", "စိတ်၏ အဖော်", "1", "^1-M2-57", "cetasikā dhammā"),
    (r"cittasampayutt", "စိတ်နှင့် ယှဉ်တွဲသော", "1", "^1-M2-58", "cittasampayuttā dhammā"),
    (r"cittavippayutt", "စိတ်နှင့် ကင်းကွာသော", "1", "^1-M2-58", "cittavippayuttā dhammā"),
    (r"cittasamuṭṭhān", "စိတ်မှ ဖြစ်ပေါ်လာသော", "1", "^1-M2-60", "cittasamuṭṭhānā dhammā"),
    (r"\bahetuk", "အမြစ် မရှိ", "2", "^2-751", "ahetukā"),
    (r"abyākat", "ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော", "1", "^1-431", "Katame dhammā abyākatā"),
    (r"\bkiriyā(?:byākat|ñāṇ|\b)", "ပြုရုံမျှသာ ဖြစ်သော", "1", "^1-567", "Kiriyā manodhātu"),
    (r"maggasamaṅg", "မဂ်နှင့် ပြည့်စုံသူ", "1", "^1-1373", "maggasamaṅgissa"),
    (r"kāmarāgānusay", "ကာမရာဂ ကိန်းအောင်းခြင်း", "2", "^2-949", "Kāmarāgānusayo"),
    (r"avijjānusay", "အမှန်ကို မသိမှု ကိန်းအောင်းခြင်း", "2", "^2-949", "avijjānusayo"),
    (r"kāmacchandanīvaraṇ", "ကာမကို လိုလားမှု အတားအဆီး", "1", "^1-1158", "kāmacchandanīvaraṇaṃ"),
    (r"kāmarāgasaṃyojan", "ကာမရာဂ နှောင်ကြိုး", "1", "^1-1118", "kāmarāgasaṃyojanaṃ"),
    (r"uppannavatthuk", "ဖြစ်ပေါ်ပြီးသော မှီရာ ရှိ၍ ဖြစ်ပေါ်ပြီးသော အာရုံ", "2", "^2-751", "Uppannavatthukā"),
    (r"pañcaviññāṇā anābhogā", "သိစိတ် ငါးပါးသည် စိတ်ညွတ်ခြင်း မရှိကြ", "2", "^2-751", "Pañca viññāṇā anābhogā"),
    (r"paṭicca rūpe ca uppajjati", "မျက်စိကိုလည်းကောင်း၊ အဆင်းအရောင်တို့ကိုလည်းကောင်း မှီ၍", "2", "^2-184",
     "Cakkhuñca paṭicca rūpe ca uppajjati"),
    (r"nimittaggāhī", "အမှတ်အသားကို စွဲယူသူ", "1", "^1-1354", "na nimittaggāhī hoti"),
    (r"cakkhunā rūpaṃ disvā", "မျက်စိဖြင့် အဆင်းအရောင်ကို မြင်၍", "1", "^1-1354", "cakkhunā rūpaṃ disvā"),
    (r"kāyakamm", "ကိုယ်ဖြင့် ပြုသော ကံ", "2", "^2-751", "na kāyakammaṃ"),
    (r"manokamm", "မနောဖြင့် ပြုသော ကံ", "1", "^1-985", "manokammaṃ"),
    (r"sāvajjānavajj", "အပြစ် ရှိသော အပြစ် မရှိသော", "4", "^4-104", "sāvajjānavajje dhamme"),
    (r"hīnapaṇīt", "ယုတ်ညံ့သော မွန်မြတ်သော", "4", "^4-104", "hīnappaṇīte dhamme"),
    (r"kaṇhasukkasappaṭibhāg", "မည်းနက်သော ဖြူစင်သော ဆန့်ကျင်ဘက် ရှိသော", "4", "^4-104", "kaṇhasukkasappaṭibhāge"),
    (r"kāmavitakk", "ကာမကို စတင်ကြံစည်မှု", "2", "^2-910", "Kāmavitakko"),
    (r"veramaṇī", "ကင်းဝေးခြင်း", "2", "^2-703", "pāṇātipātā veramaṇī"),
    (r"viññatti", "ထုတ်ဖော်ပြသမှု", "1", "^1-U1", "Atthi rūpaṃ viññatti"),
    (r"dussily|dussīly", "သီလ ပျက်ခြင်း", "2", "^2-513", "dussīlyaṃ"),
    (r"dussīlo", "သီလ ပျက်", "1", "^1-1333", "dussīlā"),
    (r"savitakko savicāro", "စတင်ကြံစည်မှုနှင့် ဆက်လက်သုံးသပ်မှု ရှိသော", "1", "^1-M1-6", "savitakkasavicārā dhammā"),
    (r"vicāramatt", "စတင်ကြံစည်မှု မရှိဘဲ ဆက်လက်သုံးသပ်မှုသာ ရှိသော", "1", "^1-M1-6", "avitakkavicāramattā dhammā"),
    (r"avitakko avicāro", "စတင်ကြံစည်မှုလည်း မရှိ၊ ဆက်လက်သုံးသပ်မှုလည်း မရှိသော", "1", "^1-M1-6", "avitakkaavicārā"),
    (r"sukhāya vedanāya sampayutt", "သာယာသော ခံစားမှုနှင့် ယှဉ်တွဲသော", "1", "^1-M1-2", "sukhāya vedanāya sampayuttā"),
    (r"diṭṭhisampann", "အယူ ပြည့်စုံသော ပုဂ္ဂိုလ်", "2", "^2-809", "diṭṭhisampanno puggalo"),
    (r"jīvitā voropit|jīvitā voropito", "အသက်မှ ချခံရ", "2", "^2-U55", "jīvitā voropitā hoti"),
    (r"jīvitā voropeyya", "အသက်မှ သတ်ရာ", "2", "^2-809", "pitaraṃ jīvitā voropeyya"),
    (r"saṅghaṃ bhindeyya", "သံဃာကို ခွဲရာ", "2", "^2-809", "saṅghaṃ bhindeyya"),
    (r"saṅgho bhinno", "သံဃာသည် ကွဲပြားစေခံရ", "2", "^2-U55", "saṅgho bhinno hoti"),
    (r"tiracchānayoni", "တိရစ္ဆာန် ဘဝ", "2", "^2-811", "tiracchānayonigāmī"),
    (r"pettivisay", "ပြိတ္တာ ဘုံ", "2", "^2-811", "pettivisayagāmī"),
    (r"duggat", "ဆိုးသော လားရာ", "2", "^2-809", "apāyaṃ duggatiṃ"),
    (r"niyato|niyatā", "ကျိန်းသေ", "1", "^1-M1-15", "sammattaniyatā dhammā"),
    (r"iddhipād", "ဣဒ္ဓိပါဒ်", "2", "^2-9-0", "Iddhipādavibhaṅgo"),
    (r"lokuttar", "လောကကို ကျော်လွန်သော", "1", "^1-M2-12", "lokuttarā dhammā"),
    (r"(?<!a)saṃyojaniy", "နှောင်ကြိုး၏ အာရုံ ဖြစ်နိုင်သော", "1", "^1-M2-21", "saṃyojaniyā dhammā"),
    (r"asaṃyojaniy", "နှောင်ကြိုး၏ အာရုံ မဖြစ်နိုင်သော", "1", "^1-M2-21", "asaṃyojaniyā dhammā"),
    (r"paññābal", "ပညာ၏ စွမ်းအား", "1", "^1-1", "paññābalaṃ hoti"),
    (r"paññindriy", "ပညာ၏ စွမ်းရည်", "1", "^1-1", "paññindriyaṃ hoti"),
    (r"\bsammāvāc", "မှန်ကန်သော စကား", "2", "^2-486", "sammāvācā"),
    (r"\bsammākammant", "မှန်ကန်သော အလုပ်", "2", "^2-486", "sammākammanto"),
    (r"\bsammāājīv", "မှန်ကန်သော အသက်မွေးမှု", "2", "^2-486", "sammāājīvo"),
    (r"\bsammāsaṅkapp", "မှန်ကန်သော ကြံစည်မှု", "2", "^2-486", "sammāsaṅkappo"),
    (r"\bsammāvāyām", "မှန်ကန်သော အားထုတ်မှု", "2", "^2-486", "sammāvāyāmo"),
    (r"\bsammāsamādh", "မှန်ကန်သော သမာဓိ", "2", "^2-486", "sammāsamādhi"),
    (r"cakkhundriy", "မျက်စိ၏ စွမ်းရည်", "2", "^2-219", "Bāvīsatindriyāni"),
    (r"\bvītarāg", "ရာဂ ကင်းသူ", None, None, "vītarāgo"),
]


def wit_find(pali, my):
    for bk_, k_, f_, p_, m_ in F.FINAL.lines():
        if pali.lower() in p_.lower() and my in m_:
            return bk_, F.ID_RE.search(p_)[1] if F.ID_RE.search(p_) else None
    return None, None


for _j, (_rx, _my, _bk, _bid, _wit) in enumerate(REUSE):
    if _bk is None:
        b_, k_ = wit_find(_wit, _my)
        if b_ is None:
            bad.append(f"C3 no FINAL witness «{_wit}» / «{_my}»")
            REUSE[_j] = None
            continue
        seg = next(kk for kk, (f_, pl, ml) in F.FINAL.SEG[b_].items()
                   if _wit.lower() in " ".join(pl).lower() and _my in " ".join(ml))
        REUSE[_j] = (_rx, _my, b_, seg, _wit)
REUSE = [x for x in REUSE if x]
n_c3 = s_c3 = 0
seen_terms = 0
for rx, my, bk, bid, wit in REUSE:
    f_, p_, m_ = F.FINAL.seg(bk, bid)
    if wit.lower() not in " ".join(p_).lower() or my not in " ".join(m_):
        bad.append(f"C3 witness «{wit}» / «{my}» not in pi-{bk} {bid}")
        continue
    hits = 0
    for name, (P, M) in PAIRS.items():
        for i, (p, m) in enumerate(zip(P, M), 1):
            if re.search(rx, nobr(body(p)), re.I):
                hits += 1
                n_c3 += 1
                if my in m:
                    s_c3 += 1
                else:
                    bad.append(f"C3 {name}:{i} «{rx}» -> «{my}» missing")
    if hits:
        seen_terms += 1
print(f"C. reuse test: C1 topic names {s_c1} / {n_c1}; C2 whole lines / headings {s_c2} / {n_c2}; "
      f"C3 terms {s_c3} / {n_c3} occurrences ({seen_terms} terms) identical with pi-1 … pi-4 final")
# ===================================================================================== D. strings copied from ch2-5
COPIED = [  # (regex in the ch2-5 Pāli, regex in ch11-12 Pāli, Burmese)
    (r"sāriputt", r"sāriputt", "သာရိပုတ္တရာ"), (r"sāriputto thero", r"sāriputto thero", "သာရိပုတ္တရာ မထေရ်"),
    (r"mahāmoggallāno thero", r"mahāmoggallāno thero", "မဟာမောဂ္ဂလ္လာန် မထေရ်"),
    (r"mahākassapo thero", r"mahākassapo thero", "မဟာကဿပ မထေရ်"),
    (r"mahākaccāyano thero", r"mahākaccāno thero", "မဟာကစ္စာယန မထေရ်"),
    (r"mahākoṭṭhiko thero", r"mahākoṭṭhiko thero", "မဟာကောဋ္ဌိက မထေရ်"),
    (r"mahāpanthako thero", r"mahāpanthako thero", "မဟာပန္ထက မထေရ်"),
    (r"apāyagamanīy", r"apāyagamanīy", "အပါယ်သို့ ရောက်စေတတ်သော"), (r"punabbhav", r"punabbhav", "ဘဝသစ်"),
    (r"anavases", r"anavases", "အကြွင်းမဲ့"), (r"\bāyasmā", r"\bāyasmā|\bāyasmato", "အသျှင်"),
    (r"dukkhaṃ parijānāti, samudayaṃ pajahati, nirodhaṃ sacchikaroti, maggaṃ bhāvet",
     r"dukkhaṃ parijānāti, samudayaṃ pajahati, nirodhaṃ sacchikaroti, maggaṃ bhāvet", MS.P11.DK_ALL_MY),
    (r"arahattaṃyeva", r"\barahatt(?:aṃ|anti)\b", "ရဟန္တာ အဖြစ်"),
    (r"niruddhaṃ vigataṃ vipariṇataṃ atthaṅgataṃ abbhatthaṅgat", r"niruddhaṃ vigataṃ vipariṇataṃ atthaṅgataṃ abbhatthaṅgat",
     "ချုပ်ငြိမ်းပြီး၊ ကင်းကွာပြီး၊ ဖောက်ပြန်ပြောင်းလဲပြီး၊ ကွယ်ပြီး၊ လုံးဝ ကွယ်ပြီးသော အရာ"),
    (r"ajātaṃ abhūtaṃ asañjātaṃ anibbattaṃ anabhinibbattaṃ apātubhūt", r"ajātaṃ abhūtaṃ asañjātaṃ anibbattaṃ anabhinibbattaṃ apātubhūt",
     "မဖြစ်သေး၊ မဖြစ်တည်သေး၊ မဖြစ်ပေါ်သေး၊ မဖြစ်မြောက်သေး၊ ထင်ရှားစွာ မဖြစ်မြောက်သေး၊ ထင်ရှား မပေါ်ပေါက်သေးသော အရာ"),
]
C25 = ["2-parihanikatha.md", "3-brahmacariyakatha.md", "4-jahatikatha.md", "5-sabbamatthitikatha.md"]
n_d = s_d = 0
for rx25, rx, my in COPIED:
    hits = [my in m for name in C25 for p, m in zip(nonempty(MS.PALI / name), nonempty(MS.OUT / name))
            if re.search(rx25, nobr(body(p)), re.I)]
    if not any(hits):
        bad.append(f"D «{rx25}» -> «{my}» not attested in the ch2-5 output (copy not verified)")
    for name, (P, M) in PAIRS.items():
        for i, (p, m) in enumerate(zip(P, M), 1):
            if re.search(rx, nobr(body(p)), re.I):
                n_d += 1
                if my in m:
                    s_d += 1
                else:
                    bad.append(f"D {name}:{i} «{rx}» -> «{my}» missing")
print(f"D. copies of ch2-5 strings: {s_d} / {n_d} occurrences identical ({len(COPIED)} strings, each verified in ch2-5)")
tot_s, tot_n = s_c1 + s_c2 + s_c3 + s_d, n_c1 + n_c2 + n_c3 + n_d
if bad:
    print(f"\n{len(bad)} MISMATCHES")
    for b in bad[:60]:
        print("  " + b)
    sys.exit(1)
print(f"\nOK: 0 mismatches; reuse {tot_s} / {tot_n} identical")
