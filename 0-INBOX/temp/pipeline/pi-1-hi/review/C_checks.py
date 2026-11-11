import re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from C_load import pairs, vnum, FILES, HI, lines

# scope
def in_scope():
    out = []
    for fn in FILES:
        lo, hi = {"3-03-rupakandam.md": (870, 965), "4-01-nikkhepakandam.md": (1030, 99999)}.get(fn, (0, 99999))
        active = lo == 0
        for i, p, h in pairs(fn):
            v = vnum(i)
            if v is not None:
                active = lo <= v <= hi
            if active:
                out.append((fn, i, p, h))
    return out

S = in_scope()
last_id = None
ID = []
# give id-less lines a label "before next id"
for k, (fn, i, p, h) in enumerate(S):
    lab = i
    if lab is None:
        j = k
        while j < len(S) and S[j][1] is None:
            j += 1
        lab = "pre-" + (S[j][1] if j < len(S) else "END")
    ID.append(lab)
print("segments/lines in scope:", len(S), "with numeric id:", sum(1 for x in S if vnum(x[1]) is not None))

BR = re.compile(r"\s*\[[^\]]*\]")
def clean(s):
    return BR.sub("", re.sub(r"\s*\^[0-9a-z\-]+\s*$", "", s))

# ---- typography
print("\n== typography")
for k, (fn, i, p, h) in enumerate(S):
    cp, ch = clean(p), clean(h)
    for dash in "–—":
        if cp.count(dash) != ch.count(dash):
            print("DASH", ID[k], dash, cp.count(dash), ch.count(dash))
    if "—" in ch:
        print("EMDASH", ID[k])
    if ch.startswith("#"):
        continue
    if not re.search(r"[।?]$", ch.strip()):
        print("END", ID[k], repr(ch[-25:]))
    if re.search(r'["\']', ch):
        print("STRAIGHTQ", ID[k])
    if ch.count("“") != ch.count("”"):
        print("QUOTEBAL", ID[k])
    if re.search(r"[A-Za-zāīūṃṅñṭḍṇḷ]", ch):
        print("LATIN", ID[k], re.findall(r"[A-Za-zāīūṃṅñṭḍṇḷ]+", ch)[:5])
    if re.search(r"(?<![।?])\.(\s|$)", ch):
        print("ASCIIDOT", ID[k])
    if re.search(r"  +", h):
        print("DBLSPACE", ID[k])
    if re.search(r"(\S+) \1(?=[ ,।])", ch):
        for m in re.finditer(r"(\S+) \1(?=[ ,।])", ch):
            if m.group(1) not in ("दृष्टि",):
                print("REPEAT", ID[k], m.group(0))

# ---- formula counts
print("\n== formula counts P vs H (per line)")
MAP = [
    (r"(?<![a-zāīū])kāmāvacar", r"इंद्रिय-सुखों के लोक से संबंधित"),
    (r"(?<![a-zāīū])rūpāvacar", r"सूक्ष्म भौतिक लोक से संबंधित"),
    (r"arūpāvacar", r"अभौतिक लोक से संबंधित"),
    (r"(?<![a-zāīū])apariyāpann", r"अस्तित्व के लोकों में न समा"),
    (r"kusalākusalābyākatā", r"हितकर, हानिकर और नैतिक रूप से अनिर्धारित"),
    (r"(?<![a-zāīū])kusalābyākatā", r"हितकर और नैतिक रूप से अनिर्धारित"),
    (r"sabbañca rūpaṃ", r"सारा भौतिक रूप"),
    (r"asaṅkhatā (ca )?dhātu", r"अनिर्मित तत्व"),
    (r"ṭhapetvā", r"छोड़कर"),
    (r"(?i)vedanākkhandho", r"अनुभूति का समूह"),
    (r"(?i)saññākkhandho", r"पहचान का समूह"),
    (r"(?i)saṅkhārakkhandho", r"मानसिक रचनाओं का समूह"),
    (r"(?i)viññāṇakkhandho", r"चेतना का समूह"),
    (r"(?i)rūpakkhandho", r"भौतिक रूप का समूह"),
    (r"…pe…", r"…"),
    (r"(?i)vippayutt", r"अलग"),
    (r"(?i)(?<!vip)(?<![a-zāīū]p)sampayutt", r"जुड़"),
    (r"(?i)maggaphalāni", r"मार्गों के फल"),
    (r"(?i)kabaḷīkāro", r"कौर-कौर"),
    (r"(?i)(?<![a-zāīū])cakkhāyatanaṃ", r"आँख का इंद्रिय-क्षेत्र"),
    (r"(?i)(?<![a-zāīū])kāyāyatanaṃ", r"शरीर का इंद्रिय-क्षेत्र"),
    (r"(?i)(?<![a-zāīū])rūpāyatanaṃ", r"दृश्य रूप का इंद्रिय-क्षेत्र"),
    (r"(?i)(?<![a-zāīū])rasāyatanaṃ", r"स्वाद का इंद्रिय-क्षेत्र"),
    (r"(?i)(?<![a-zāīū])gandhāyatanaṃ", r"गंध का इंद्रिय-क्षेत्र"),
    (r"(?i)phoṭṭhabbāyatanaṃ", r"स्पर्श का इंद्रिय-क्षेत्र"),
    (r"(?i)saddāyatanaṃ", r"ध्वनि का इंद्रिय-क्षेत्र"),
    (r"(?i)ākāsadhātu", r"आकाश तत्व"),
    (r"(?i)āpodhātu", r"जल तत्व"),
    (r"(?i)na kammassa katattā", r"कर्म किए जाने के कारण नहीं"),
]
n = 0
for k, (fn, i, p, h) in enumerate(S):
    cp, ch = clean(p), clean(h)
    for a, b in MAP:
        x, y = len(re.findall(a, cp)), len(re.findall(b, ch))
        if x != y:
            n += 1
            print("COUNT", ID[k], a, x, y)
print("count mismatches:", n)

NUMS = [(r"(?i)\btīṇi\b|\btayo\b|\btisso\b", "तीन"), (r"(?i)\bcattāro\b|\bcattāri\b", "चार"), (r"(?i)\bpañca\b|\bpañcapi\b", "पाँच"),
        (r"(?i)\bcha\b|\bchannaṃ\b", "छह"), (r"(?i)\bnava\b", "नौ"), (r"(?i)\bdasa\b", "दस"), (r"(?i)\bdve\b", r"\bदो\b|^दो | दो "),
        (r"(?i)aṭṭhārasa", "अठारह"), (r"(?i)dvādasa", "बारह"), (r"(?i)\bsatta(pi)?\b", "सात")]
print("\n== numerals")
for k, (fn, i, p, h) in enumerate(S):
    cp, ch = clean(p), clean(h)
    for a, b in NUMS:
        x, y = len(re.findall(a, cp)), len(re.findall(b, ch))
        if x != y:
            print("NUM", ID[k], a, x, y)

# ---- recurring strings
print("\n== recurring strings")
def strip_var(s):
    return clean(s)
def find_body(s, a, b):
    i = s.find(a)
    if i < 0:
        return None
    j = s.find(b, i)
    if j < 0:
        return None
    return s[i:j + len(b)]
G = [
 ("lobha", "Yo rāgo sārāgo", "lobho akusalamūlaṃ", "जो राग, प्रबल राग", "लोभ रूपी हानिकर मूल"),
 ("dosa-triggers", "nattha", "aṭṭhāne vā pana āghāto jāyati", "“उसने मेरा अहित किया”", "या बिना कारण ही आक्रोश उत्पन्न होता है"),
 ("dosa", "cittassa āghāto paṭighāto", "anattamanatā cittassa", "मन का आक्रोश, प्रतिघात", "मन की अप्रसन्नता"),
 ("moha-objects", "Dukkhe aññāṇaṃ", "dhammesu aññāṇaṃ", "दुःख को न जानना", "परिघटनाओं को न जानना"),
 ("moha", "aññāṇaṃ adassanaṃ anabhisamayo", "moho akusalamūlaṃ", "जो न जानना, न देखना, सत्य", "मोह रूपी हानिकर मूल"),
 ("amoha-objects", "Dukkhe ñāṇaṃ", "dhammesu ñāṇaṃ", "दुःख का ज्ञान", "परिघटनाओं का ज्ञान"),
 ("amoha", "paññā pajānanā vicayo", "amoho dhammavicayo sammādiṭṭhi", "जो प्रज्ञा, जानना, छानबीन", "मोह का अभाव, परिघटनाओं की छानबीन, सही दृष्टि"),
 ("kama8", "Yo kāmesu kāmacchando", "kāmajjhosānaṃ", "इंद्रिय-सुखों में जो", "इंद्रिय-सुखों से चिपके रहना"),
 ("bhava8", "Yo bhavesu bhavachando", "bhavajjhosānaṃ", "अस्तित्वों में जो", "अस्तित्व से चिपके रहना"),
 ("views10", "Sassato lokoti vā", "paraṃ maraṇāti vā", "“लोक शाश्वत है”, या", "न नहीं रहते”"),
 ("viewsyn", "diṭṭhi diṭṭhigataṃ diṭṭhigahanaṃ", "vipariyāsaggāho", "जो दृष्टि, दृष्टियों में फँसना, दृष्टि का घना", "उलटी पकड़"),
 ("vicik-objects", "Satthari kaṅkhati vicikicchati, dhamme", "dhammesu kaṅkhati vicikicchati", "गुरु के बारे में शंका करता है, संशय करता है, शिक्षा", "परिघटनाओं के बारे में शंका करता है, संशय करता है"),
 ("vicik", "kaṅkhā kaṅkhāyanā", "manovilekho", "शंका, शंका करना", "मन की खरोंच"),
 ("mana", "yo evarūpo māno", "ketukamyatā cittassa", "इस प्रकार का जो अहंकार", "झंडा फहराने की चाह"),
 ("thina", "cittassa akallatā", "thiyitattaṃ cittassa", "मन की अस्वस्थता", "मन का आलस्य से भरा होना"),
 ("uddhacca", "cittassa uddhaccaṃ", "bhantattaṃ cittassa", "मन की बेचैनी", "डाँवाडोल होना"),
 ("attavada", "Idha assutavā", "viññāṇasmiṃ vā attānaṃ", "यहाँ अशिक्षित", "या चेतना में आत्मा को"),
 ("nihil", "atthi dinnaṃ", "sacchikatvā pavedent", "“दान देना व्यर्थ है", "बताते हों”"),
 ("sila-quote", "Ito bahiddhā", "suddhī", "इस शिक्षा से बाहर", "शुद्धि होती है”"),
]
def norm_h(t):
    return re.sub(r"\s+", " ", t.replace(";", ",").replace("।", ","))
def norm_p(t):
    t = t.replace("ः", ",").replace(";", ",").replace(".", ",")
    t = t.replace("patiṭṭhāho", "paṭiggāho").replace("acarī ti", "acarīti")
    t = re.sub(r",", "", t)
    return re.sub(r"\s+", " ", t)
for name, pa, pb, ha, hb in G:
    ps, hs = {}, {}
    ids = []
    missing = []
    for k, (fn, i, p, h) in enumerate(S):
        cp, ch = strip_var(p), strip_var(h)
        if name == "nihil":
            cp2 = cp.replace("Natthi dinnaṃ", "atthi dinnaṃ")
            bp = find_body(cp2, pa, pb)
            if bp and "Atthi dinnaṃ" in cp:
                bp = None
        elif name == "views10":
            i0 = cp.find(pa)
            bp = None
            if i0 >= 0:
                j0 = cp.find("neva hoti na na hoti tathāgato paraṃ maraṇāti vā", i0)
                bp = cp[i0:j0 + 48] if j0 >= 0 else None
        elif name == "dosa-triggers":
            i0 = cp.find("Anatthaṃ me acar")
            bp = None
            if i0 >= 0:
                bp = find_body(cp[i0:], "Anatthaṃ", pb)
        else:
            bp = find_body(cp, pa, pb)
        if bp:
            ids.append(ID[k])
            bh = find_body(ch, ha, hb)
            if bh is None:
                missing.append(ID[k])
                continue
            ps.setdefault(norm_p(bp), []).append(ID[k])
            hs.setdefault(norm_h(bh), []).append(ID[k])
    print(f"{name}: {len(ids)} occurrences {ids}")
    print(f"   distinct Pali={len(ps)} distinct Hindi={len(hs)} missing={missing}")
    if len(ps) > 1:
        for v, w in ps.items():
            print("   P-variant", w, v[:60], "...", v[-40:])
    if len(hs) > 1:
        vs = list(hs.items())
        base = vs[0][0]
        for v, w in vs[1:]:
            # first diff
            n0 = next((q for q in range(min(len(base), len(v))) if base[q] != v[q]), min(len(base), len(v)))
            print("   H-diff", vs[0][1][:2], "vs", w[:4], "at", n0, repr(base[max(0,n0-30):n0+30]), "||", repr(v[max(0,n0-30):n0+30]))

# ---- clause order
print("\n== clause order")
def seq(text, table, idx):
    alts = sorted(table, key=len, reverse=True)
    rx = re.compile("|".join(re.escape(a) for a in alts))
    return [table[m.group(0)] for m in rx.finditer(text)]
def body(s):
    c = clean(s)
    c = c[c.find("?") + 1:]
    return c
def get(idv):
    for k, x in enumerate(S):
        if x[1] == idv:
            return x
T = {
 "1-1101": ({"cakkhuviññeyyā":"e","sotaviññeyyā":"s","ghānaviññeyyā":"n","jivhāviññeyyā":"t","kāyaviññeyyā":"b"},
            {"आँख से":"e","कान से":"s","नाक से":"n","जीभ से":"t","शरीर से":"b"}),
 "1-1114": ({"Kāmāsavo":"k","kāmāsavena":"k","Bhavāsavo":"b","bhavāsavo":"b","bhavāsavena":"b","diṭṭhāsavo":"d","diṭṭhāsavena":"d","avijjāsavo":"a","avijjāsavena":"a"},
            {"इंद्रिय-सुखों के मैल":"k","इंद्रिय-सुखों का मैल":"k","अस्तित्व का मैल":"b","अस्तित्व के मैल":"b","दृष्टि का मैल":"d","दृष्टि के मैल":"d","अज्ञान का मैल":"a","अज्ञान के मैल":"a"}),
 "1-1136": ({"Kāmarāgasaṃyojanaṃ":"k","kāmarāgasaṃyojanena":"k","paṭighasaṃyojanaṃ":"p","paṭighasaṃyojanena":"p","mānasaṃyojanaṃ":"m","mānasaṃyojanena":"m","diṭṭhisaṃyojanaṃ":"d","diṭṭhisaṃyojanena":"d","vicikicchāsaṃyojanaṃ":"v","vicikicchāsaṃyojanena":"v","sīlabbataparāmāsasaṃyojanaṃ":"s","sīlabbataparāmāsasaṃyojanena":"s","bhavarāgasaṃyojanaṃ":"b","bhavarāgasaṃyojanena":"b","issāsaṃyojanaṃ":"i","issāsaṃyojanena":"i","macchariyasaṃyojanaṃ":"c","macchariyasaṃyojanena":"c","avijjāsaṃyojanaṃ":"a","avijjāsaṃyojanena":"a"},
            {"इंद्रिय-सुखों के राग":"k","चिढ़ का":"p","चिढ़ के":"p","अहंकार का":"m","अहंकार के":"m","दृष्टि का":"d","दृष्टि के":"d","संशय का":"v","संशय के":"v","सदाचार और व्रतों":"s","अस्तित्व के राग":"b","ईर्ष्या का":"i","ईर्ष्या के":"i","कंजूसी का":"c","कंजूसी के":"c","अज्ञान का":"a","अज्ञान के":"a"}),
 "1-1152": ({"Sīlabbataparāmāso":"s","sīlabbataparāmāsena":"s","abhijjhākāyagantho":"a","abhijjhākāyaganthena":"a","idaṃsaccābhiniveso":"i","idaṃsaccābhinivesena":"i"},
            {"सदाचार और व्रतों":"s","लालच रूपी":"a","“केवल यही":"i"}),
 "1-1176": ({"Kāmacchandanīvaraṇaṃ":"k","kāmacchandanīvaraṇaṃ":"k","kāmacchandanīvaraṇena":"k","byāpādanīvaraṇaṃ":"b","byāpādanīvaraṇena":"b","thinamiddhanīvaraṇaṃ":"t","thinamiddhanīvaraṇena":"t","uddhaccanīvaraṇaṃ":"u","uddhaccanīvaraṇena":"u","kukkuccanīvaraṇaṃ":"c","kukkuccanīvaraṇena":"c","vicikicchānīvaraṇaṃ":"v","vicikicchānīvaraṇena":"v","avijjānīvaraṇaṃ":"a","avijjānīvaraṇena":"a"},
            {"इंद्रिय-सुखों की चाह":"k","दुर्भावना की":"b","आलस्य और तंद्रा":"t","बेचैनी की":"u","पछतावे की":"c","संशय की":"v","अज्ञान की":"a"}),
 "1-1231": ({"Diṭṭhupādānaṃ":"d","diṭṭhupādānaṃ":"d","diṭṭhupādānena":"d","kāmupādānaṃ":"k","kāmupādānena":"k","sīlabbatupādānaṃ":"s","sīlabbatupādānena":"s","attavādupādānaṃ":"a","attavādupādānena":"a"},
            {"दृष्टियों के प्रति":"d","इंद्रिय-सुखों के प्रति":"k","सदाचार और व्रतों के प्रति":"s","आत्मा के सिद्धांत":"a"}),
 "1-1257": ({"Lobho":"L","lobho":"L","lobhena":"L","doso":"D","dosena":"D","moho":"M","mohena":"M","māno":"N","mānena":"N","diṭṭhi ":"V","diṭṭhiyā":"V","vicikicchā ":"C","vicikicchāya":"C","thinaṃ":"T","thinena":"T","uddhaccaṃ":"U","uddhaccena":"U","ahirikaṃ":"A","ahirikena":"A","anottappaṃ":"O","anottappena":"O"},
            {"लोभ ":"L","द्वेष ":"D","मोह ":"M","अहंकार ":"N","दृष्टि ":"V","संशय ":"C","आलस्य ":"T","बेचैनी ":"U","निर्लज्जता ":"A","बुराई के प्रति निडरता ":"O"}),
}
for idv, (tp, th) in T.items():
    fn, i, p, h = get(idv)
    bp, bh = body(p), body(h)
    # cut closing formula
    bp = bp[:bp.rfind(" – ime")] if " – ime" in bp else bp[:bp.rfind("Ime dhammā")]
    bh = bh[:bh.rfind(" – ये")] if " – ये" in bh else bh[:bh.rfind("ये किसी एक")]
    a, b = seq(bp, tp, idv), seq(bh, th, idv)
    print(idv, "tokens", len(a), len(b), "IDENTICAL" if a == b else "DIFF")
    if a != b:
        n0 = next((q for q in range(min(len(a), len(b))) if a[q] != b[q]), min(len(a), len(b)))
        print("   first diff at", n0, a[max(0,n0-4):n0+6], b[max(0,n0-4):n0+6])
    if idv == "1-1101":
        print("   na te dhammā:", bp.count("na te dhammā"), "नहीं हैं:", bh.count("नहीं हैं"))
    if idv == "1-1257":
        cl = [c.strip() for c in bh.split(", ") if c.strip()]
        fem = ("दृष्टि ", "बेचैनी ", "निर्लज्जता ", "बुराई के प्रति निडरता ")
        bad = 0
        for c in cl:
            f = c.startswith(fem)
            if f and not c.endswith("जुड़ी भी") or (not f and not c.endswith("जुड़ा भी")):
                bad += 1
                print("   AGREE", c)
        print("   clauses", len(cl), "agreement problems", bad)

# ---- ःhandling
print("\n== visarga-as-colon in Pali, and Hindi at that junction")
for k, (fn, i, p, h) in enumerate(S):
    if "ः" in p:
        m = re.search(r"(.{12})(इस प्रकार (का|की) जो)", h)
        print(ID[k], repr(m.group(1)) if m else None)

# ---- other-chapter usage of terms in question (Hindi only)
print("\n== term usage across Hindi chapters")
for term in ["क्लेशों की ओर", "क्लेशों का विषय", "मानसिक काया", "आँख की इंद्रिय", "मन की इंद्रिय", "सारी ग़लत दृष्टि"]:
    res = []
    for f in sorted(os.listdir(HI)):
        t = open(os.path.join(HI, f), encoding="utf-8").read()
        c = t.count(term)
        if c:
            res.append(f"{f}:{c}")
    print(term, res)
