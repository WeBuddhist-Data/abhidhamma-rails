"""pi-6 Saṅkhārayamaka (6-01, 6-02): Pāli -> Hindi plain RAILS.

Uses the approved sample constants (build_rails_sample.py, imported read-only) and adds the Saṅkhāra
vocabulary (formations, breathing, thought, jhāna stages, moments, final mind). New recurring formulas are
listed in notes-6-01-6-02.md.

usage: python -I -X utf8 build_6_01_6_02.py [--dry]
"""
import re
import sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-hi\rails")
import build_rails_sample as S  # noqa: E402  (read-only)

FILES = ["6-01-sankharayamaka.md", "6-02-sankharayamaka.md"]

# ---------------------------------------------------------------------------------------------------
# Headings, closings
# ---------------------------------------------------------------------------------------------------
HEADINGS = dict(S.HEADINGS)
HEADINGS.update({
    "(Ṅa) paccanīkaokāsā": "(ङ) नकारात्मक: स्थान",       # 6-01 ^6-6-16-5-0 (plural form, same heading)
    "1-6. Paccuppannavārādi": "1-6. वर्तमान का खंड आदि",   # termbase Paccuppannavārādi
})
CLOSINGS = dict(S.CLOSINGS)
CLOSINGS.update({
    "Paṇṇattivāro.": "शब्दावली का खंड।",
    "Uppādavāro.": "उत्पन्न होने का खंड।",
    "Saṅkhārayamakaṃ niṭṭhitaṃ.": S.CHAPTER_END.format(title=S.CHAPTER_TITLES["Saṅkhārayamakaṃ"]),
})

# ---------------------------------------------------------------------------------------------------
# The three formations (process subjects, all feminine: «रचना»)
# ---------------------------------------------------------------------------------------------------
FORMATIONS = {
    "kāyasaṅkhāro": ("शरीर की रचना", "f"),
    "vacīsaṅkhāro": ("वाणी की रचना", "f"),
    "cittasaṅkhāro": ("मन की रचना", "f"),
}
FORM_ACC = {"kāyasaṅkhāraṃ": "kāyasaṅkhāro", "vacīsaṅkhāraṃ": "vacīsaṅkhāro", "cittasaṅkhāraṃ": "cittasaṅkhāro"}

# Paṇṇatti words: key -> (direct, oblique, number)
PW = {
    "kāyo": ("शरीर", "शरीर", "sg"),
    "vacī": ("वाणी", "वाणी", "sg"),
    "cittaṃ": ("मन", "मन", "sg"),
    "saṅkhāro": ("रचना", "रचना", "sg"),
    "saṅkhārā": ("रचनाएँ", "रचनाओं", "pl"),
    "kāyasaṅkhāro": ("शरीर की रचना", "शरीर की रचना", "sg"),
    "vacīsaṅkhāro": ("वाणी की रचना", "वाणी की रचना", "sg"),
    "cittasaṅkhāro": ("मन की रचना", "मन की रचना", "sg"),
}
PW_CA = {"kāyañca": "kāyo", "vaciñca": "vacī", "cittañca": "cittaṃ", "kāyasaṅkhārañca": "kāyasaṅkhāro",
         "vacīsaṅkhārañca": "vacīsaṅkhāro", "cittasaṅkhārañca": "cittasaṅkhāro"}

# ---------------------------------------------------------------------------------------------------
# Being / place / moment vocabulary
# ---------------------------------------------------------------------------------------------------
JHANA_ORD = {"paṭhama": "पहली", "dutiya": "दूसरी", "tatiya": "तीसरी", "catuttha": "चौथी"}
JHANA_ACC = {f"{k}jjhānaṃ": k for k in JHANA_ORD}
JHANA_LOC = {f"{k}jjhāne": k for k in JHANA_ORD}


def jhana(ords):
    """['dutiya', 'tatiya'] -> «ध्यान की दूसरी या तीसरी अवस्था» (one noun, ordinals joined «, » / «या»)."""
    h = [JHANA_ORD[o] for o in ords]
    s = h[0] if len(h) == 1 else ", ".join(h[:-1]) + " या " + h[-1]
    return f"ध्यान की {s} अवस्था"


SAMAPANNA = "{x} में लीन लोगों में"                    # <jhāna> samāpannānaṃ
NIRODHASAMAPANNA = "समाप्ति की ध्यान-अवस्था में लीन लोगों में"   # termbase
VV = "आरंभिक विचार और सतत विचार"                        # vitakkavicārā (termbase)
BREATH = "साँस लेना और छोड़ना"                           # assāsapassāsā (termbase)
BREATH_OBL = "साँस लेने और छोड़ने"
VINA = {"assāsapassāsehi": f"{BREATH_OBL} के बिना", "vitakkavicārehi": f"{VV} के बिना"}
MOMENT_GEN = {   # genitive noun before uppādakkhaṇe / bhaṅgakkhaṇe
    "cittassa": "मन के",
    "assāsapassāsānaṃ": f"{BREATH_OBL} के",
    "vitakkavicārānaṃ": f"{VV} के",
    "avitakkaavicāracittassa": f"{VV} से रहित मन के",
    "pacchimacittassa": "अंतिम मन के",
    "savitakkasavicārapacchimacittassa": f"{VV} वाले अंतिम मन के",
    "avitakkaavicārapacchimacittassa": f"{VV} से रहित अंतिम मन के",
}
KHANA = {"uppādakkhaṇe": "उत्पन्न होने के क्षण में", "bhaṅgakkhaṇe": "भंग होने के क्षण में"}
SABBESAM_GEN = "सभी के"                                  # Sabbesaṃ cittassa … (B5)
TESAMYEVA = "उन्हीं में"                                 # tesaṃyeva + moment
DUTIYE_CITTE = "दूसरे मन के चलते समय"                    # dutiye citte vattamāne (B4)
SAMANGI = {
    "pacchimacittasamaṅgīnaṃ": "अंतिम मन से युक्त लोगों में",
    "avitakkaavicārapacchimacittasamaṅgīnaṃ": f"{VV} से रहित अंतिम मन से युक्त लोगों में",
}
BHUMI = {"savitakkasavicārabhūmiyaṃ": f"{VV} वाले स्तर", "avitakkaavicārabhūmiyaṃ": f"{VV} से रहित स्तर"}
ANANTARA = "जिनमें इस मन के ठीक बाद {x} उत्पन्न होगा, उनमें"   # yassa cittassa anantarā X uppajjissati (B6)
ANANTARA_X = {
    "kāmāvacarānaṃ pacchimacittaṃ": "इंद्रिय-सुखों के लोक के प्राणियों का अंतिम मन",
    "avitakkaavicāraṃ pacchimacittaṃ": f"{VV} से रहित अंतिम मन",
}
ITARESAM_BHUMI = "{bhumi} में बाकी सबमें"               # Itaresaṃ savitakkasavicārabhūmiyaṃ
PLACE_LOC = {"kāmāvacare": "kāmāvacara", "rūpāvacare": "rūpāvacara", "arūpāvacare": "arūpāvacara",
             "asaññasatte": "asaññasatta"}
PLACE_ACC = {"suddhāvāsaṃ": "suddhāvāsa", "rūpāvacaraṃ": "rūpāvacara", "arūpāvacaraṃ": "arūpāvacara"}


def places_or(keys):
    """Several places inside one chunk: «A या B» (as «चार या पाँच समूहों वाले अस्तित्व», harmonise I3)."""
    h = [S.PLACE_NOUN[k] for k in keys]
    return h[0] if len(h) == 1 else ", ".join(h[:-1]) + " या " + h[-1]


def who(s):
    """Being / moment chain before 'tesaṃ' -> Hindi chunks, each ending «में», joined «, » / « और »."""
    s = s[0].lower() + s[1:]
    if s == "itaresaṃ":
        return S.ITARESAM_ALONE
    t = s.split(" ")
    chunks = []      # list of [text, kind]  kind: beings | moment | rel
    i = 0

    def moment_at(j):
        """Parse '[sabbesaṃ] [vinā X] GEN KHANA' at j -> (text, next j) or None."""
        pre = []
        k = j
        if t[k] == "sabbesaṃ":
            pre.append(SABBESAM_GEN)
            k += 1
        if k < len(t) and t[k] == "vinā":
            pre.append(VINA[t[k + 1]])
            k += 2
        if k + 1 < len(t) and t[k] in MOMENT_GEN and t[k + 1] in KHANA:
            return " ".join(pre + [MOMENT_GEN[t[k]], KHANA[t[k + 1]]]), k + 2
        return None

    while i < len(t):
        w = t[i]
        m = moment_at(i)
        if m:
            txt, i = m
            if chunks and chunks[-1][1] == "beings":
                # a moment right after beings belongs to the whole run of beings before it:
                # «A में और B में <moment>» (Paṭhamajjhānaṃ samāpannānaṃ kāmāvacarānaṃ assāsapassāsānaṃ …)
                k = len(chunks)
                while k > 0 and chunks[k - 1][1] == "beings":
                    k -= 1
                run = [c[0] for c in chunks[k:]]
                chunks[k:] = [[" और ".join(run) + " " + txt, "beings+moment"]]
            else:
                chunks.append([txt, "moment"])
            continue
        if w == "tesaṃyeva":
            m = moment_at(i + 1)
            chunks.append([f"{TESAMYEVA} {m[0]}", "moment"])
            i = m[1]
            continue
        if w == "itaresaṃ":
            nxt = t[i + 1]
            if nxt in BHUMI:
                chunks.append([ITARESAM_BHUMI.format(bhumi=BHUMI[nxt]), "beings"])
                i += 2
                continue
            m = moment_at(i + 1)
            if m:
                chunks.append([f"{S.ITARESAM_ALONE} {m[0]}", "moment"])
                i = m[1]
                continue
            # Itaresaṃ <beings>: «बाकी <beings>»
            sub = who(" ".join(t[i + 1:i + 2]))
            chunks.append([f"{S.ITARESAM} {sub}", "beings"])
            i += 2
            continue
        if w in JHANA_ACC:
            ords = []
            while t[i] in JHANA_ACC:
                ords.append(JHANA_ACC[t[i]])
                i += 1
            assert t[i] == "samāpannānaṃ", s
            chunks.append([SAMAPANNA.format(x=jhana(ords)), "beings"])
            i += 1
            continue
        if w == "nirodhasamāpannānaṃ":
            chunks.append([NIRODHASAMAPANNA, "beings"])
            i += 1
            continue
        if w in S.BEINGS:
            chunks.append([S.BEINGS[w], "beings"])
            i += 1
            continue
        if w in SAMANGI:
            chunks.append([SAMANGI[w], "beings"])
            i += 1
            continue
        if w == "dutiye" and t[i + 1:i + 3] == ["citte", "vattamāne"]:
            chunks[-1][0] += " " + DUTIYE_CITTE
            chunks[-1][1] = "beings+moment"
            i += 3
            continue
        if w == "yassa" and t[i + 1:i + 3] == ["cittassa", "anantarā"]:
            x = " ".join(t[i + 3:i + 5])
            assert t[i + 5] == "uppajjissati", s
            chunks.append([ANANTARA.format(x=ANANTARA_X[x]), "rel"])
            i += 6
            continue
        if w == "ye" and t[i + 1] == "ca":
            j = i + 2
            keys = []
            while t[j] in PLACE_ACC:
                keys.append(PLACE_ACC[t[j]])
                j += 1
            assert t[j:j + 3] == ["upapajjitvā", "parinibbāyissanti", "tesaṃ"], s
            txt = S.YE_PARINIBBAYISSANTI.format(place=places_or(keys)) + " से " + S.PARTICIPLES[t[j + 3]]
            chunks.append([txt, "rel"])
            i = j + 4
            continue
        if w in PLACE_LOC or w in BHUMI:
            # locative place(s) in front of a being / moment: «A या B में <rest>»
            keys, bh = [], None
            while i < len(t) and (t[i] in PLACE_LOC):
                keys.append(PLACE_LOC[t[i]])
                i += 1
            if not keys:
                bh = BHUMI[t[i]]
                i += 1
            place_txt = (places_or(keys) if keys else bh) + " में"
            if i < len(t) and t[i] in SAMANGI:
                chunks.append([f"{place_txt} {SAMANGI[t[i]]}", "beings"])
                i += 1
            elif i < len(t) and t[i] == "pacchimabhavikānaṃ":
                chunks.append([f"{place_txt} {S.PARTICIPLES['pacchimabhavikānaṃ']}", "beings"])
                i += 1
            elif i < len(t) and moment_at(i):
                txt, i = moment_at(i)
                chunks.append([f"{place_txt} {txt}", "moment"])
            elif i == len(t):
                chunks.append([place_txt, "beings"])      # bare plane / place before 'tesaṃ tattha'
            else:
                raise ValueError(f"who: place followed by {t[i]!r} in {s!r}")
            continue
        if w in PLACE_ACC and t[i + 1] == "upapajjantānaṃ":
            chunks.append([f"{S.PLACE_NOUN[PLACE_ACC[w]]} में {S.PARTICIPLES['upapajjantānaṃ']}", "beings"])
            i += 2
            continue
        raise ValueError(f"who: unknown token {w!r} in {s!r}")
    texts = [c[0] for c in chunks]
    if len(texts) == 1:
        return texts[0]
    return S.JOIN.join(texts[:-1]) + S.JOIN_LAST + texts[-1]


def place(s):
    """Place list of the okāsa answers (before 'tattha'): every chunk «… में», jhāna runs joined «या»."""
    t = [w for w in (s[0].lower() + s[1:]).split(" ")]
    chunks, i = [], 0
    while i < len(t):
        if t[i] in JHANA_LOC:
            ords = []
            while i < len(t) and t[i] in JHANA_LOC:
                ords.append(JHANA_LOC[t[i]])
                i += 1
            chunks.append(jhana(ords) + " में")
            continue
        chunks.append(S.PLACE_NOUN[PLACE_LOC[t[i]]] + " में")
        i += 1
    return chunks[0] if len(chunks) == 1 else S.JOIN.join(chunks[:-1]) + S.JOIN_LAST + chunks[-1]


# ---------------------------------------------------------------------------------------------------
# Verbs
# ---------------------------------------------------------------------------------------------------
VERB_TI = set(S.VERB_FORMS) | set(S.VERB_SLIPS)


def verb_hi(tok, gender="f", flip=False):
    return S.verb_hi(tok, gender, flip)


def strip_verb(v):
    neg = v.startswith("na ")
    w = S.strip_ti(v[3:] if neg else v, VERB_TI)
    return ("na " if neg else "") + w


# ---------------------------------------------------------------------------------------------------
# Sentence handlers
# ---------------------------------------------------------------------------------------------------
LAB = r"(?:\((Ka|Kha)\) )?"
REL = r"([Yy]assa vā pana yattha|[Yy]assa yattha|[Yy]assa vā pana|[Yy]assa|[Yy]attha vā pana|[Yy]attha)"
COR = r"(tassa tattha|tassa|tattha)"
V = r"((?:na )?\S+)"


def rel_hi(rel):
    rel = rel[0].lower() + rel[1:]
    return {"yassa": "जिस व्यक्ति में", "yassa vā pana": "और जिस व्यक्ति में", "yattha": "जिस स्थान पर",
            "yattha vā pana": "और जिस स्थान पर", "yassa yattha": "जिस व्यक्ति में जिस स्थान पर",
            "yassa vā pana yattha": "और जिस व्यक्ति में जिस स्थान पर"}[rel]


COR_HI = {"tassa": "उसमें", "tattha": "वहाँ", "tassa tattha": "उसमें वहाँ"}

# Source slips read as the parallel passages (reported in notes-6-01-6-02.md)
QUESTION_SLIPS = {
    # 6-02 ^6-6-132 line 3: the answers presuppose "na nirujjhatīti"
    "(Ka) yassa kāyasaṅkhāro nuppajjati tassa cittasaṅkhāro nirujjhatīti?":
        "(Ka) yassa kāyasaṅkhāro nuppajjati tassa cittasaṅkhāro na nirujjhatīti?",
}
SENTENCE_SLIPS = {
    # 6-02 ^6-6-121 line 2: "na nirujjhittha" for "ca nirujjhittha" (cf. 6-01 ^6-6-72)
    "Paṭhamajjhānaṃ samāpannānaṃ itaresaṃ kāmāvacarānaṃ tesaṃ tattha kāyasaṅkhāro na nirujjhittha vacīsaṅkhāro ca nirujjhissati.":
        "Paṭhamajjhānaṃ samāpannānaṃ itaresaṃ kāmāvacarānaṃ tesaṃ tattha kāyasaṅkhāro ca nirujjhittha vacīsaṅkhāro ca nirujjhissati.",
}


def question(s):
    s = QUESTION_SLIPS.get(s, s)
    m = re.fullmatch(rf"{LAB}{REL} (\S+) {V} {COR} (\S+) {V}\?", s)
    if m:
        lab, rel, k1, v1, cor, k2, v2 = m.groups()
        if k1 in FORMATIONS and k2 in FORMATIONS:
            v2 = strip_verb(v2)
            (k1h, g1), (k2h, g2) = FORMATIONS[k1], FORMATIONS[k2]
            head = (S.LABELS[f"({lab})"] + " ") if lab else ""
            return f"{head}{rel_hi(rel)} {k1h} {verb_hi(v1, g1)}, क्या {COR_HI[cor]} {k2h} {verb_hi(v2, g2)}?"
    # pariññā: (Ka) yo X parijānāti so Y parijānātīti?
    m = re.fullmatch(rf"{LAB}yo( vā pana)? (\S+) (\S+) so (\S+) (\S+)\?", s)
    if m and m.group(3) in FORM_ACC:
        lab, vp, o1, v1, o2, v2 = m.groups()
        v2 = S.strip_ti(v2, set(S.PARIJANATI))
        o1h, o2h = FORMATIONS[FORM_ACC[o1]][0], FORMATIONS[FORM_ACC[o2]][0]
        rel = ("और " if vp else "") + "जो व्यक्ति"
        return f"{S.LABELS[f'({lab})']} {rel} {o1h} को {S.PARIJANATI[v1][0]}, क्या वह {o2h} को {S.PARIJANATI[v2][0]}?"
    # abbreviated question: (Kha) yassa vā pana[ yattha| X]…pe…?  ('.' in 6-01 ^6-6-69 is a slip)
    m = re.fullmatch(rf"{LAB}{REL}(?: (\S+))?…pe…[?.]", s)
    if m:
        lab, rel, k = m.groups()
        head = (S.LABELS[f"({lab})"] + " ") if lab else ""
        mid = (" " + FORMATIONS[k][0]) if k else ""
        return f"{head}{rel_hi(rel)}{mid}…?"
    # padasodhana: (Ka) [na ]X [na ]Y?
    m = re.fullmatch(r"\((Ka|Kha)\) (na )?(\S+) (na )?(\S+?)\?", s)
    if m and bool(m.group(2)) == bool(m.group(4)) and m.group(3) in PW:
        lab = S.LABELS[f"({m.group(1)})"]
        a = m.group(3)
        b = S.strip_ti(m.group(5), set(PW))
        (ad, _, an), (bd, _, bn) = PW[a], PW[b]
        n2 = "pl" if "pl" in (an, bn) else "sg"
        if m.group(2):
            return f"{lab} जो {ad} नहीं {S.COP[an]}, क्या {S.PRON[an]} {bd} नहीं {S.COP[n2]}?"
        return f"{lab} क्या {ad}, {bd} {S.COP[n2]}?"
    return None


def pannatti_sentence(s):
    m = re.fullmatch(r"(\S+) na (\S+), (\S+)\.", s)                       # A na C, B.
    if m:
        a = m.group(1)[0].lower() + m.group(1)[1:]
        if a in PW and m.group(2) in PW and m.group(3) == a:
            n = PW[a][2]
            return f"{PW[a][0]}, {PW[m.group(2)][0]} नहीं {S.COP[n]}, पर {PW[a][0]} {S.COP[n]}।"
    m = re.fullmatch(r"(\S+) (\S+) ceva (\S+) ca\.", s)                    # C B ceva C ca.
    if m:
        c = m.group(1)[0].lower() + m.group(1)[1:]
        if c == m.group(3) and c in PW and m.group(2) in PW:
            b = PW[m.group(2)]
            n = "pl" if "pl" in (b[2], PW[c][2]) else "sg"
            return f"{PW[c][0]}, {b[0]} भी {S.COP[n]} और {PW[c][0]} भी।"
    m = re.fullmatch(r"(\S+) (\S+) ṭhapetvā avasesā na ceva (\S+) na ca (\S+)\.", s)
    if m:
        b = PW[PW_CA[m.group(1).lower()]]
        c = PW[PW_CA[m.group(2)]]
        return f"{b[1]} और {c[1]} को छोड़कर {S.AVASESA} न तो {PW[m.group(3)][0]} हैं, न {PW[m.group(4)][0]}।"
    m = re.fullmatch(r"Avasesā saṅkhārā( \[avasesā saṅkhārā saṅkhārā \(sī\. syā\. kaṃ\.\)\])? na (\S+)\.", s)
    if m:
        var = " [पाठभेद (Sī., Syā., Kaṃ.): avasesā saṅkhārā saṅkhārā]" if m.group(1) else ""
        return f"{S.AVASESA} रचनाएँ{var}, {PW[m.group(2)][0]} नहीं हैं।"
    return None


def pavatti_sentence(s):
    s = SENTENCE_SLIPS.get(s, s)
    m = re.fullmatch(r"(.+?) (tesaṃ tattha|tesaṃ|tattha) (\S+) ((?:na )?\S+), no ca (?:tesaṃ tattha|tesaṃ|tattha) "
                     r"(\S+) ((?:na )?\S+)\.", s)
    if m:
        wh, t, k1, v1, k2, v2 = m.groups()
        (k1h, g1), (k2h, g2) = FORMATIONS[k1], FORMATIONS[k2]
        v1h, v2h = verb_hi(v1, g1), verb_hi(v2, g2, flip=True)
        if t == "tattha":
            return S.BUT_PLACE.format(place=place(wh), k1=k1h, v1=v1h, k2=k2h, v2=v2h)
        frame = S.BUT_BEINGS_T if t == "tesaṃ tattha" else S.BUT_BEINGS
        return frame.format(who=who(wh), k1=k1h, v1=v1h, k2=k2h, v2=v2h)
    m = re.fullmatch(r"(.+?) (tesaṃ tattha|tesaṃ|tattha) (\S+) ca ((?:na )?\S+) (\S+) ca ((?:na )?\S+)\.", s)
    if m:
        wh, t, k1, v1, k2, v2 = m.groups()
        (k1h, g1), (k2h, g2) = FORMATIONS[k1], FORMATIONS[k2]
        v1h, v2h = verb_hi(v1, g1), verb_hi(v2, g2)
        if t == "tattha":
            return S.BOTH_PLACE.format(place=place(wh), k1=k1h, v1=v1h, k2=k2h, v2=v2h)
        frame = S.BOTH_BEINGS_T if t == "tesaṃ tattha" else S.BOTH_BEINGS
        return frame.format(who=who(wh), k1=k1h, v1=v1h, k2=k2h, v2=v2h)
    return None


def abbreviated_statement(s):
    """'Yattha X V…pe….' / 'Yassa [vā pana ]yattha X V…pe….' -> «जिस स्थान पर X V…।» (no final '.' -> no «।»)."""
    m = re.fullmatch(rf"{REL} (\S+) {V}…pe…(\.?)", s)
    if m and m.group(2) in FORMATIONS:
        rel, k, v, dot = m.groups()
        kh, g = FORMATIONS[k]
        return f"{rel_hi(rel)} {kh} {verb_hi(v, g)}…" + ("।" if dot else "")
    return None


def short_answer(s):
    if s in ("Āmantā.", "No.", "Natthi."):
        return CLOSINGS[s]
    w = s[:-1]
    w = w[0].lower() + w[1:]
    if w in S.VERB_FORMS:
        return verb_hi(w, "f") + "।"
    return None


# ---------------------------------------------------------------------------------------------------
# Notes and unique lines (translated one by one)
# ---------------------------------------------------------------------------------------------------
YASSAKA_BOTH = "व्यक्ति वाला भाग भी और व्यक्ति और स्थान वाला भाग भी समान हैं"
YASSAYATTHAKE_NIRODHA = "व्यक्ति और स्थान वाले भाग में “समाप्ति की ध्यान-अवस्था में लीन लोगों में”"
NATTHI_NANAKARANA = "कोई अंतर नहीं है"   # natthi nānākaraṇaṃ (not the short answer)
FIXED_SENTENCES = {
    "(Yassakampi yassayatthakampi sadisaṃ.)": f"({YASSAKA_BOTH}।)",
    "(Yatthakampi sabbattha ekasadisaṃ).": "(स्थान वाला भाग भी हर जगह एक समान है)।",
    "(Yassakampi yassayatthakampi sadisaṃ vitthāretabbaṃ, yassayatthake nirodhasamāpannānanti na labbhati.)":
        "(व्यक्ति वाले भाग का भी और व्यक्ति और स्थान वाले भाग का भी समान रूप से विस्तार करना चाहिए, "
        f"{YASSAYATTHAKE_NIRODHA} नहीं मिलता।)",
    "(Yassakampi yassayatthakampi sadisaṃ vitthāretabbaṃ, yassayatthake nirodhasamāpannānanti na kātabbaṃ.)":
        "(व्यक्ति वाले भाग का भी और व्यक्ति और स्थान वाले भाग का भी समान रूप से विस्तार करना चाहिए, "
        f"{YASSAYATTHAKE_NIRODHA} नहीं जोड़ना चाहिए।)",
    "(Yassakampi yassayatthakampi sadisaṃ, yassayatthake nirodhasamāpannānanti na labbhati).":
        f"({YASSAKA_BOTH}, {YASSAYATTHAKE_NIRODHA} नहीं मिलता)।",
    "(Yathā uppādavāre atītā pucchā yassakampi yassayatthakampi anulomampi paccanīkampi vibhattaṃ evaṃ "
    "nirodhavārepi vibhajitabbaṃ, natthi nānākaraṇaṃ.)":
        "(जैसे उत्पन्न होने के खंड में अतीत के प्रश्नों का व्यक्ति वाला भाग भी, व्यक्ति और स्थान वाला भाग भी, "
        "सकारात्मक भी और नकारात्मक भी विभाजन किया गया है, वैसे ही समाप्त होने के खंड में भी विभाजन करना चाहिए, "
        f"{NATTHI_NANAKARANA}।)",
    "(Atītā pucchā uppādavārepi nirodhavārepi uppādanirodhavārepi sadisaṃ vitthāretabbā).":
        "(अतीत के प्रश्नों का उत्पन्न होने के खंड में भी, समाप्त होने के खंड में भी और उत्पन्न होने और समाप्त होने "
        "के खंड में भी समान रूप से विस्तार करना चाहिए)।",
    "(Yathā uppādavāre paccuppannātītā pucchā anulomampi paccanīkampi vibhattā evaṃ uppādavāranirodhavārepi "
    "paccuppannātītā pucchā anulomampi paccanīkampi vibhajitabbā.)":
        "(जैसे उत्पन्न होने के खंड में वर्तमान और अतीत के प्रश्नों का सकारात्मक भी और नकारात्मक भी विभाजन किया गया है, "
        "वैसे ही उत्पन्न होने और समाप्त होने के खंड में भी वर्तमान और अतीत के प्रश्नों का सकारात्मक भी और नकारात्मक "
        "भी विभाजन करना चाहिए।)",
    "(Yathā nirodhavāre atītānāgatā pucchā anulomampi paccanīkampi evaṃ uppādanirodhavārepi atītānāgatā pucchā "
    "anulomampi paccanīkampi vibhajitabbaṃ asammohantena nirodhavārena sadisaṃ, natthi nānākaraṇaṃ.)":
        "(जैसे समाप्त होने के खंड में अतीत और भविष्य के प्रश्न सकारात्मक भी और नकारात्मक भी हैं, वैसे ही उत्पन्न होने "
        "और समाप्त होने के खंड में भी अतीत और भविष्य के प्रश्नों का सकारात्मक भी और नकारात्मक भी, बिना भ्रम के, "
        f"समाप्त होने के खंड के समान विभाजन करना चाहिए, {NATTHI_NANAKARANA}।)",
    "(Yathā khandhayamake pariññāvāraṃ vibhattaṃ evaṃ saṅkhārayamakepi pariññāvāraṃ vibhajitabbaṃ.)":
        "(जैसे “समूहों पर प्रश्नों के जोड़े” में पूरी तरह समझने के खंड का विभाजन किया गया है, वैसे ही "
        "“रचनाओं पर प्रश्नों के जोड़े” में भी पूरी तरह समझने के खंड का विभाजन करना चाहिए।)",
    # abbreviated question + note on one line
    "Yassa yattha kāyasaṅkhāro nirujjhati tassa tattha vacīsaṅkhāro nirujjhatīti?…Pe….":
        "जिस व्यक्ति में जिस स्थान पर शरीर की रचना समाप्त होती है, क्या उसमें वहाँ वाणी की रचना समाप्त होती है?…",
    "Yattha kāyasaṅkhāro nirujjhati tattha vacīsaṅkhāro nirujjhatīti?…Pe….":
        "जिस स्थान पर शरीर की रचना समाप्त होती है, क्या वहाँ वाणी की रचना समाप्त होती है?…",
    "Dutiyajjhāne tatiyajjhāne tattha…pe… (itaresaṃ yatthakānaṃ sadisaṃ).":
        "ध्यान की दूसरी या तीसरी अवस्था में… (बाकी स्थान वाले भागों के समान)।",
    "Yassa yattha kāyasaṅkhāro uppajjati…pe… (yassakampi yassayatthakampi sadisaṃ).":
        f"जिस व्यक्ति में जिस स्थान पर शरीर की रचना उत्पन्न होती है… ({YASSAKA_BOTH})।",
    # Paṇṇatti uddesa ^6-6-1
    "Tayo saṅkhārā – kāyasaṅkhāro, vacīsaṅkhāro, cittasaṅkhāroti.":
        "तीन रचनाएँ – शरीर की रचना, वाणी की रचना, मन की रचना।",
    "Assāsapassāsā kāyasaṅkhāro, vitakkavicārā vacīsaṅkhāro, saññā ca vedanā ca cittasaṅkhāro.":
        f"{BREATH} शरीर की रचना है, {VV} वाणी की रचना हैं, पहचान और अनुभूति मन की रचना हैं।",
    "Ṭhapetvā vitakkavicāre sabbepi cittasampayuttakā dhammā cittasaṅkhāro.":
        f"{VV} को छोड़कर मन से जुड़ी सभी परिघटनाएँ मन की रचना हैं।",
}
FIXED_LINES = {
    "(Kha) paccanīkaṃ": "(ख) नकारात्मक",
    "4 (Ṅa) paccanīkaokāso": "4 (ङ) नकारात्मक: स्थान",     # source slip: '4' for '#####'
    "Namo tassa bhagavato arahato sammāsambuddhassa": S.NAMO,
}


def translate_sentence(s):
    if s in CLOSINGS:
        return CLOSINGS[s]
    if s in FIXED_SENTENCES:
        return FIXED_SENTENCES[s]
    for fn in (abbreviated_statement, question, pannatti_sentence, pavatti_sentence, short_answer):
        r = fn(s)
        if r:
            return r
    raise ValueError(f"no formula for: {s}")


SPLIT = re.compile(r"(?<=[.?]) (?=[A-ZĀĪŪṬḌṆÑṄ(])")


def translate_text_line(line):
    if line in FIXED_LINES:
        return FIXED_LINES[line]
    if line in FIXED_SENTENCES:
        return FIXED_SENTENCES[line]
    return " ".join(translate_sentence(s) for s in SPLIT.split(line))


def translate_line(line):
    if not line.strip():
        return ""
    bid = ""
    m = S.ID_RE.search(line)
    if m:
        bid = " " + m.group(1)
        line = line[: m.start()]
    line = line.strip()
    if line.startswith("#"):
        hashes, text = line.split(" ", 1)
        return f"{hashes} {HEADINGS[text]}{bid}"
    return translate_text_line(line) + bid


def translate_text(pali_text):
    out, prev_blank = [], True
    for line in pali_text.splitlines():
        if not line.strip():
            if not prev_blank:
                out.append("")
            prev_blank = True
            continue
        out.append(translate_line(line))
        prev_blank = False
    while out and out[-1] == "":
        out.pop()
    return "\n".join(out) + "\n"


def main():
    dry = "--dry" in sys.argv
    for f in FILES:
        src = (S.PALI_DIR / f).read_text(encoding="utf-8")
        hi = translate_text(src)
        if not dry:
            (S.HI_DIR / f).write_text(hi, encoding="utf-8", newline="\n")
        print(f, "lines", len([l for l in hi.splitlines() if l.strip()]), "(dry)" if dry else "written")


if __name__ == "__main__":
    main()
