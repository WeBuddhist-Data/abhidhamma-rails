"""pi-6 Yamaka, Vietnamese plain RAILS: chapter 6-01 (Saṅkhārayamaka: paṇṇattivāra + pavattivāra uppādavāra and
the start of the nirodhavāra) and the SAṄKHĀRA module that 6-02 imports.

Frames: families A, B from build_rails_2-01_vi; the shared answer shapes from build_rails_7-01_vi; moments / persons
from build_rails_8_vi; answer heads (Sabbesaṃ «Ở tất cả chúng sinh», «khi tâm … đang diễn ra», the anantarā shape)
from build_rails_9-01_vi / 9-02; plane-beings and the "P ye ca …" head from 3-01 / 3-02 / 3-03 / 2-02; editorial
note pieces and cut questions from 5-01. All imported READ-ONLY; nothing retyped.

Import READ-ONLY (importing writes nothing; outputs are written only under `if __name__ == "__main__":`):
    sys.path.insert(0, r"D:\\Work\\OpenPecha\\abhidhamma-rails\\0-INBOX\\temp\\pipeline\\pi-6-vi-ai\\rails")
    import importlib; SK = importlib.import_module("build_rails_6-01_vi")

What the module gives 6-02 (byte-fixed; never retype the strings):
  SANKHARA_TABLE / SANKHARA        the members (kāyo, vacī, cittaṃ, kāya- / vacī- / cittasaṅkhāro, saṅkhāro, saṅkhārā)
  X_PL, YAMAKA                     «tạo tác» (Suddhasaṅkhāravāro), "Saṅkhāra"
  UDDESA_PALI / UDDESA_VI          ^6-6-1
  BREATH, VITAKKA, SAVITAKKA, AVITAKKA, FINAL_MIND, BHUMI, JHANA / jhana_vi(), ATTAINING
  GEN / gen_vi() / moment()        genitives before a moment; «vinā X» = VINA «mà không có X» after the noun
  anantara_group()                 yassa cittassa anantarā [kāmāvacarānaṃ] [avitakkaavicāraṃ] pacchimacittaṃ uppajjissati
  EXTRA_PERSON, head_parts(), answer_head(), place_vi()
  self_not() / a_sentence() / b_sentence() / sentence() / sentences()
  pq_question() / cut_question() / cut_half()   the B shell, its cut forms
  NOTES / FIXED / heading() / tr_line() / build()
A line the parsers cannot place raises ValueError: there is no silent fallback.

usage: python -I -X utf8 -B build_rails_6-01_vi.py [--probe]
"""
import importlib
import pathlib
import re
import sys
import unicodedata

RAILS_DIR = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai\rails")
if str(RAILS_DIR) not in sys.path:
    sys.path.insert(0, str(RAILS_DIR))
import build_rails_sample_vi as S  # noqa: E402  (READ-ONLY)
B = importlib.import_module("build_rails_2-01_vi")    # families A, B (READ-ONLY)
C = importlib.import_module("build_rails_7-01_vi")    # shared answer shapes (READ-ONLY)
D = importlib.import_module("build_rails_8_vi")       # moments, persons (READ-ONLY)
DY = importlib.import_module("build_rails_9-01_vi")   # answer heads, anantarā shape (READ-ONLY)
DY2 = importlib.import_module("build_rails_9-02_vi")  # (READ-ONLY; checked against)
A = importlib.import_module("build_rails_3-01_vi")    # PLANES_AY (READ-ONLY)
A2 = importlib.import_module("build_rails_3-02_vi")   # person items (READ-ONLY)
A3 = importlib.import_module("build_rails_3-03_vi")   # ye-ca heads (READ-ONLY; checked against)
E = importlib.import_module("build_rails_2-02_vi")    # KHI_CAVANTA, YE_CA, b_cut (READ-ONLY)
T5 = importlib.import_module("build_rails_5-01_vi")   # note pieces, cut questions (READ-ONLY)
T10 = importlib.import_module("build_rails_10-01_vi")  # self_not (READ-ONLY; checked against)

CHAPTER = "6-01-sankharayamaka.md"
N = "6-01"
NOTES_MD = RAILS_DIR / f"notes-rails-{N}.md"
ADH_DIR = RAILS_DIR / f"adh-{N}"
cap = S.cap
PE = S.PE
lc = DY.lc
YAMAKA = "Saṅkhāra"
X_PL = "tạo tác"                          # Suddhasaṅkhāravāro «mục về các tạo tác thuần túy» (termbase)
PLANES = A.PLANES_AY                      # 2-01 planes + kāmāvacara / rūpāvacara / arūpāvacara (3-01)
SLIPS_SEEN = []

# ===============================================================================================================
# 1. Members (termbase: kāyo «thân», vacī «lời nói», cittaṃ «tâm», kāyasaṅkhāro «sự tạo tác bằng thân»,
#    vacīsaṅkhāro «sự tạo tác bằng lời nói», cittasaṅkhāro «sự tạo tác bằng tâm» (= the Yamaka's own definitions:
#    breathing / vitakka-vicāra / saññā-vedanā; pi-2 ^2-226 wording), saṅkhāro «sự tạo tác», saṅkhārā «tạo tác»)
# ===============================================================================================================
KAYA_S, VACI_S, CITTA_S = "sự tạo tác bằng thân", "sự tạo tác bằng lời nói", "sự tạo tác bằng tâm"
SANKHARA_TABLE = {
    "kāya": ("thân", "thân", ["kāyo", "kāyaṃ"]),
    "vacī": ("lời nói", "lời nói", ["vacī", "vaciñca"]),
    "citta": (D.MIND, D.MIND, ["cittaṃ"]),
    "kāyasaṅkhāra": (KAYA_S, KAYA_S, ["kāyasaṅkhāro", "kāyasaṅkhāraṃ"]),
    "vacīsaṅkhāra": (VACI_S, VACI_S, ["vacīsaṅkhāro", "vacīsaṅkhāraṃ"]),
    "cittasaṅkhāra": (CITTA_S, CITTA_S, ["cittasaṅkhāro", "cittasaṅkhāraṃ"]),
    "saṅkhāra": ("sự tạo tác", "sự tạo tác", ["saṅkhāro"]),
    "saṅkhārā": B.KHANDHA.vi["saṅkhārā"] + (["saṅkhārā", "saṅkhāre"],),   # «các tạo tác» / «tạo tác» (2-01)
}
SANKHARA = B.Members(SANKHARA_TABLE)
M = SANKHARA
MEMBER_SUBJ_RE = r"(?:kāya|vacī|citta)saṅkhāro"

# ===============================================================================================================
# 2. Words of the answer heads (termbase; pi-1 / pi-2 / pi-5 rails)
# ===============================================================================================================
BREATH = "hơi thở vào và hơi thở ra"                         # Assāsapassāsā / -ānaṃ / -ehi (termbase; pi-5)
VITAKKA = "sự hướng tâm và sự duy trì tâm"                   # vitakkavicārā / -ānaṃ / -ehi / -e (termbase; pi-1)
SAVITAKKA = f"có {VITAKKA}"                                  # savitakkasavicāra- (pi-1 «có sự hướng tâm và …»)
AVITAKKA = "không có sự hướng tâm cũng không có sự duy trì tâm"   # avitakkaavicāra- (termbase; pi-1 ^1-M1-6)
FINAL_MIND = f"{D.MIND} {D.FINAL}"                           # pacchimacittaṃ «tâm cuối cùng» (termbase; 8)
BHUMI = "cấp độ"                                             # -bhūmiyaṃ (termbase «cấp độ có / không có …»)
JHANA = "tầng thiền"                                         # -jjhānaṃ / -jjhāne (termbase Catutthajjhāne; pi-2)
ORD = {"paṭhama": "thứ nhất", "dutiya": "thứ hai", "tatiya": "thứ ba", "catuttha": "thứ tư"}   # (pi-2 16-nanavibhango)
ATTAINING = "đang nhập"                                      # samāpannānaṃ «người đang nhập» (termbase = pi-5)
VINA = "mà không có"                                         # vinā X-ehi (pi-5 vinā rūpena «không có vật chất»;
                                                             #  «mà» as the sample's «X mà không có gốc rễ»)
INSTR = {"assāsapassāsehi": BREATH, "vitakkavicārehi": VITAKKA}
GEN = {   # genitive before a moment word (lower case) → Vietnamese (termbase locative phrases)
    "assāsapassāsānaṃ": BREATH,
    "vitakkavicārānaṃ": VITAKKA,
    "avitakkaavicāracittassa": f"{D.MIND} {AVITAKKA}",
    "savitakkasavicārapacchimacittassa": f"{FINAL_MIND} {SAVITAKKA}",   # termbase order «tâm cuối cùng có …»
    "avitakkaavicārapacchimacittassa": f"{FINAL_MIND} {AVITAKKA}",
}
EXTRA_PERSON = {   # genitive plural persons (lower case) not in 2-01's registry
    "nirodhasamāpannānaṃ": D.PERSON["nirodhasamāpannānaṃ"],                 # (8)
    "pacchimacittasamaṅgīnaṃ": D.PERSON["pacchimacittasamaṅgīnaṃ"],         # (8)
    "avitakkaavicārapacchimacittasamaṅgīnaṃ": f"{D.PERSON['pacchimacittasamaṅgīnaṃ']} {AVITAKKA}",   # termbase
    "tesaṃyeva": "chính những người ấy",                                    # termbase
}


def jhana_vi(word):
    """'Paṭhamajjhānaṃ' / 'dutiyajjhāne' → «tầng thiền thứ nhất» / «tầng thiền thứ hai» (acc. or loc.), else None."""
    m = re.fullmatch(r"(paṭhama|dutiya|tatiya|catuttha)jjhān(aṃ|e)", lc(word))
    return (f"{JHANA} {ORD[m.group(1)]}", m.group(2)) if m else None


def bhumi_vi(word):
    """Savitakkasavicārabhūmiyaṃ / Avitakkaavicārabhūmiyaṃ → «cấp độ có / không có …», else None."""
    w = lc(word)
    if w == "savitakkasavicārabhūmiyaṃ":
        return f"{BHUMI} {SAVITAKKA}"
    if w == "avitakkaavicārabhūmiyaṃ":
        return f"{BHUMI} {AVITAKKA}"
    return None


def gen_vi(word):
    w = lc(word)
    if w in GEN:
        return GEN[w]
    if w.endswith("cittassa"):
        return DY.mind_gen(word)              # cittassa «tâm» (9-01)
    return None


def moment(gen_word, moment_word, vina=None):
    """'assāsapassāsānaṃ' 'uppādakkhaṇe' [vinā 'vitakkavicārehi'] → «vào khoảnh khắc sinh khởi của hơi thở vào và
    hơi thở ra[ mà không có sự hướng tâm và sự duy trì tâm]» (9-01 moment_vi + VINA)."""
    g = gen_vi(gen_word)
    if g is None:
        raise ValueError(f"unknown genitive before a moment {gen_word!r}")
    out = DY.moment_vi(moment_word, g)
    return out + (f" {VINA} {INSTR[vina]}" if vina else "")


def anantara_group(being, avitakka):
    """yassa cittassa anantarā [kāmāvacarānaṃ] [avitakkaavicāraṃ] pacchimacittaṃ uppajjissati (a person group) →
    «<những người | chúng sinh trong cõi X> mà tâm cuối cùng [không có …] sẽ sinh khởi ngay sau tâm này»
    (9-01 PERSON_ATTAIN shape «… ngay sau tâm này»; user: smooth, meaning unchanged, not «Vào tâm mà ngay sau đó …»)."""
    head = PLANES[being][1] if being else D.PEOPLE
    mind = FINAL_MIND + (f" {AVITAKKA}" if avitakka else "")
    return f"{head} mà {mind} {B.VERB['uppajjissati'][0]} {DY.ANANTARA} {DY.THIS_MIND}"


# ===============================================================================================================
# 3. Answer heads
# ===============================================================================================================
YASSA_CITTASSA = ["yassa", "cittassa", "anantarā"]


def _b_token(toks, i):
    """Token i belongs to a 2-01 / 3-02 person phrase (quantifier before a person word, participle, attribute,
    non-locative plane case, or a locative plane run followed by an attribute / participle)."""
    t = lc(toks[i])
    if t in B.PARTICIPLES or t in B.ATTRS:
        return True
    if t in B.QUANT:
        return True
    pt = B.plane_tok(t, PLANES)
    if not pt:
        return False
    if pt[1] != "loc":
        return True
    j = i
    while j < len(toks) and (q := B.plane_tok(toks[j], PLANES)) and q[1] == "loc":
        j += 1
    return j < len(toks) and (lc(toks[j]) in B.ATTRS or lc(toks[j]) in B.PARTICIPLES)


def _flat(items):
    """3-02's ay_persons join over a whole person run: a run that is one run of plane-beings keeps 2-01's being_run;
    otherwise groups stay whole and runs of plane-beings are flattened (each «chúng sinh trong cõi X»); a run with
    a quantifier (Itaresaṃ X-ānaṃ Y-ānaṃ) keeps being_run's own pieces in the flat list."""
    if len(items) == 1 and items[0][0] == "run":
        return [B.being_run(items[0][1], items[0][2], PLANES)]
    flat = []
    for it in items:
        if it[0] == "group":
            flat.append(it[1])
        elif len(it[1]) == 1:
            flat.append(B.being_run(it[1], it[2], PLANES))
        elif it[2]:
            first = B.being_run(it[1][:1], it[2], PLANES)
            flat += [first] + [PLANES[k][0] for k in it[1][1:]]
            assert B.join_and(flat[-len(it[1]):]) == B.being_run(it[1], it[2], PLANES)
        else:
            flat += [PLANES[k][1] for k in it[1]]
    return flat


def head_parts(head):
    """Pāli answer head (before tesaṃ / tattha / tesaṃ tattha) → Vietnamese parts (joined «, » by the caller).
    One «ở» per run of persons; each place its own «ở»; moments «vào …»; «khi tâm … đang diễn ra»; a person run
    after a time phrase opens with its own «ở» (coordinator, 7-01, 9-01)."""
    toks = head.split()
    parts, run, i = [], [], 0

    def flush():
        if run:
            parts.append(f"{C.AT} {B.join_and(_flat(run))}")
            run.clear()

    while i < len(toks):
        t, lt = toks[i], lc(toks[i])
        nxt = lc(toks[i + 1]) if i + 1 < len(toks) else None
        if [lc(x) for x in toks[i:i + 3]] == YASSA_CITTASSA:              # anantarā person group
            j, being, avit = i + 3, None, False
            if j < len(toks) and (pt := B.plane_tok(toks[j], PLANES)) and pt[1] == "gen":
                being, j = pt[0], j + 1
            if j < len(toks) and toks[j] == "avitakkaavicāraṃ":
                avit, j = True, j + 1
            if toks[j:j + 2] != ["pacchimacittaṃ", "uppajjissati"]:
                raise ValueError(f"unknown anantarā phrase in {head!r}")
            run.append(("group", anantara_group(being, avit)))
            i = j + 2
            continue
        if lt == "ye" and nxt == "ca":                                     # ye ca … parinibbāyissanti [tesaṃ cavantānaṃ]
            k = toks.index("parinibbāyissanti", i)
            ye = B.ye_clause("Ye " + " ".join(toks[i + 2:k + 1]), PLANES)
            run.append(("group", ye[0].lower() + ye[1:]))
            i = k + 1
            if toks[i:i + 2] == ["tesaṃ", "cavantānaṃ"]:
                flush()
                parts.append(E.KHI_CAVANTA)
                i += 2
            continue
        if lt == "vinā":
            if toks[i + 1] not in INSTR or i + 3 >= len(toks) or lc(toks[i + 3]) not in D.MOMENT:
                raise ValueError(f"unknown vinā phrase in {head!r}")
            flush()
            parts.append(moment(toks[i + 2], toks[i + 3], vina=toks[i + 1]))
            i += 4
            continue
        if nxt in D.MOMENT:
            flush()
            parts.append(moment(t, toks[i + 1]))
            i += 2
            continue
        if lt in DY.ORDINAL:                                               # dutiye citte vattamāne (9-01)
            if toks[i + 1:i + 3] != ["citte", "vattamāne"]:
                raise ValueError(f"unknown time phrase in {head!r}")
            flush()
            parts.append(f"{DY.WHILE} {D.MIND} {DY.ORDINAL[lt]} {DY.OCCURRING}")
            i += 3
            continue
        if (jv := jhana_vi(t)) and jv[1] == "aṃ":                         # X-jjhānaṃ … samāpannānaṃ
            js, j = [], i
            while j < len(toks) and (q := jhana_vi(toks[j])) and q[1] == "aṃ":
                js.append(q[0])
                j += 1
            if j >= len(toks) or toks[j] != "samāpannānaṃ":
                raise ValueError(f"jhāna without samāpannānaṃ in {head!r}")
            run.append(("group", f"{D.PEOPLE} {ATTAINING} {B.join_and(js)}"))
            i = j + 1
            continue
        if (jv := jhana_vi(t)) or bhumi_vi(t):                             # places: X-jjhāne, -bhūmiyaṃ
            flush()
            parts.append(f"{C.AT} {jv[0] if jv else bhumi_vi(t)}")
            i += 1
            continue
        if lt in EXTRA_PERSON:
            run.append(("group", EXTRA_PERSON[lt]))
            i += 1
            continue
        if lt == "sabbesaṃ" and not (i + 1 < len(toks) and _b_token(toks, i + 1)):
            run.append(("group", DY.ALL_BEINGS))                          # bare Sabbesaṃ «tất cả chúng sinh» (9-01)
            i += 1
            continue
        if _b_token(toks, i):
            j = i + 1
            while j < len(toks) and _b_token(toks, j) and lc(toks[j]) not in B.QUANT:
                j += 1
            run.extend(A2.ay_person_items(" ".join(toks[i:j]), PLANES))
            i = j
            continue
        pt = B.plane_tok(t, PLANES)
        if pt and pt[1] == "loc":                                          # a plane as a place
            flush()
            parts.append(f"{C.AT} {PLANES[pt[0]][0]}")
            i += 1
            continue
        raise ValueError(f"unknown word {t!r} in answer head {head!r}")
    flush()
    if not parts:
        raise ValueError(f"empty answer head {head!r}")
    return parts


def answer_head(head):
    return cap(", ".join(head_parts(head)))


# ===============================================================================================================
# 4. Answer sentences
# ===============================================================================================================
def self_not(a, y):
    """Kāyasaṅkhāro na kāyo, kāyasaṅkhāro. = 2-01 special_not with the member as subject (= 10-01 self_not):
    «Sự tạo tác bằng thân thì không phải là thân, mà là sự tạo tác bằng thân.»"""
    return B.special_not(a, y, a)


def a_sentence(s):
    if m := re.fullmatch(r"(\S+) na (\S+), (\S+)\.", s):
        if M.key(m.group(1)) != M.key(m.group(3)):
            raise ValueError(f"'X na Y, Z.' with Z ≠ X: {s!r}")
        return self_not(M.subj(m.group(1)), M.pred(m.group(2)))
    return B.a_sentence(s, M)


LOC = r"(tesaṃ tattha|tesaṃ|tattha)"
B_RE = re.compile(r"(.+?) " + LOC + r" (?=" + MEMBER_SUBJ_RE + r" )(.+)\.")


def b_sentence(s):
    """H tesaṃ A V1, no ca tesaṃ B V2. / H tesaṃ A ca V1 B ca V2. (2-01 b_noca / b_both; heads above)."""
    m = B_RE.fullmatch(s)
    if not m:
        return None
    head, loc, rest = m.groups()
    head_vi = answer_head(head)
    if mm := re.fullmatch(r"(.+?), no ca " + re.escape(loc) + r" (.+)", rest):
        a, v1 = B.split_mv(mm.group(1), M)
        b, v2 = B.split_mv(mm.group(2), M)
        return B.b_noca(head_vi, loc, a, v1, b, v2)
    if mm := re.fullmatch(r"(\S+) ca ((?:na )?\S+) (\S+) ca ((?:na )?\S+)", rest):
        return B.b_both(head_vi, loc, M.subj(mm.group(1)), B.verb(mm.group(2)), M.subj(mm.group(3)),
                        B.verb(mm.group(4)))
    raise ValueError(f"unknown answer frame {s!r}")


# editorial notes (5-01 pieces: P_PERSON «phần về người», P_PERSON_PLACE «phần về người và nơi chốn», P_PLACE,
# VITTHARETABBAM «nên được trình bày chi tiết», SABBATTHA_SADISAM «ở mọi chỗ cũng đều giống nhau»; 3-01 ekasadisaṃ
# «giống hệt nhau»; pi-2 / 2-02 «như đã được phân tích trong …, … cũng nên phân tích như vậy»; pi-5 «sự khác biệt»)
BOTH_SECTIONS = f"Cả {T5.P_PERSON} lẫn {T5.P_PERSON_PLACE}"
NIRODHA_Q = f"“{D.PERSON['nirodhasamāpannānaṃ']}”"
IN_YY = f"ở {T5.P_PERSON_PLACE} thì"
NOTE_SADISA = f"({BOTH_SECTIONS} đều giống nhau.)"                                  # (Yassakampi yassayatthakampi sadisaṃ.)
NOTE_EKASADISA = f"({cap(T5.P_PLACE)} {T5.SABBATTHA_SADISAM.replace('giống nhau', 'giống hệt nhau')})."
NOTE_YASSAKA_CORE = T5.NOTE_YASSAKA[1:-len(").")]                                  # «Cả … giống nhau»
NOTE_NA_LABBHATI = f"({NOTE_YASSAKA_CORE}, {IN_YY} không có {NIRODHA_Q}.)"
NOTE_NA_KATABBAM = f"({NOTE_YASSAKA_CORE}, {IN_YY} không nên trình bày {NIRODHA_Q}.)"
NOTE_YATHA = (f"(Các {'câu hỏi'} về quá khứ, cả {T5.P_PERSON} lẫn {T5.P_PERSON_PLACE}, cả chiều thuận lẫn chiều "
              f"nghịch, như đã được phân tích trong {B.UPPADAVARO}, ở {B.NIRODHAVARO} cũng nên phân tích như vậy, "
              f"không có sự khác biệt.)")
NOTES = {
    "(Yassakampi yassayatthakampi sadisaṃ.)": NOTE_SADISA,
    "(Yatthakampi sabbattha ekasadisaṃ).": NOTE_EKASADISA,
    "(Yassakampi yassayatthakampi sadisaṃ vitthāretabbaṃ, yassayatthake nirodhasamāpannānanti na labbhati.)":
        NOTE_NA_LABBHATI,
    "(Yassakampi yassayatthakampi sadisaṃ vitthāretabbaṃ, yassayatthake nirodhasamāpannānanti na kātabbaṃ.)":
        NOTE_NA_KATABBAM,
    "(Yathā uppādavāre atītā pucchā yassakampi yassayatthakampi anulomampi paccanīkampi vibhattaṃ evaṃ "
    "nirodhavārepi vibhajitabbaṃ, natthi nānākaraṇaṃ.)": NOTE_YATHA,
}

SECTION_END = dict(DY.SECTION_END) | {"Paṇṇattivāro.": f"{B.PANNATTIVARO}."}   # «Mục về sự định danh.»


def sentence(s):
    if s in B.SHORT:
        return B.SHORT[s]
    if s in SECTION_END:
        return SECTION_END[s]
    if s in NOTES:
        return NOTES[s]
    out = b_sentence(s)
    if out is None:
        out = a_sentence(s)
    if out is None:
        raise ValueError(f"unknown sentence {s!r}")
    return out


def sentences(rest):
    """Sentences, and the notes «(…)» that end in «.)» or «).»."""
    rest = rest.strip()
    out = []
    while rest:
        if rest.startswith("("):
            k = rest.index(")") + 1
            if rest[k:k + 1] == ".":
                k += 1
            out.append(sentence(rest[:k]))
        else:
            m = re.match(r"(.+?\.)(?= |$)", rest)
            if not m:
                raise ValueError(f"no sentence end in {rest!r}")
            k = m.end()
            out.append(sentence(rest[:k]))
        rest = rest[k:].strip()
    return " ".join(out)


# ===============================================================================================================
# 5. Questions: the B shell (2-01 b_q = 7-01 pair_q), family A naming questions (2-01), cut forms
# ===============================================================================================================
PQ_RE = re.compile(r"(?:" + B.LABEL_RE + r" )?([Yy]assa|[Yy]attha)( vā pana)?( yattha)? (.+?) "
                   r"(tassa tattha|tassa|tattha) (.+?)\?(.*)")


def pq_question(body):
    """(Ka) yassa A V1 tassa B V2ti? (also unlabelled, capital Y) → (Vietnamese, rest) or None."""
    m = PQ_RE.fullmatch(body)
    if not m:
        return None
    label, w1, vapana, w2, c1, then, c2, rest = m.groups()
    if label is None and w1[0] != w1[0].upper():
        raise ValueError(f"unlabelled lower-case question {body!r}")
    if label and (label == "Kha") != bool(vapana):
        raise ValueError(f"label / vā pana mismatch {body!r}")
    who = lc(w1) + (w2 or "")
    a, v1 = B.split_mv(c1, M)
    b, v2 = B.split_mv(c2, M)
    return B.b_q(label, who, then, a, v1[0], b, v2[0], other=bool(vapana)), rest


def _shell_head(label, who, vapana):
    """The shell up to «mà» (B.b_q cut there; = 3-03 cut_pair_q, 5-01 b_cut_question)."""
    full = B.b_q(label, who, C.Q_COR[who], "⟨A⟩", "⟨V⟩", "⟨B⟩", "⟨W⟩", other=vapana)
    head, sep, _ = full.partition(" ⟨A⟩ ⟨V⟩")
    assert sep, full
    return head


CUTQ_RE = re.compile(r"\((Ka|Kha)\) (yassa|yattha)( vā pana)?( yattha)?(?: (\S+?))?…pe…([?.])(.*)")


def cut_question(body):
    """'(Kha) yassa vā pana[ yattha][ A]…pe…? Āmantā.' → «(b) Còn ở người nào[, ở nơi nào] mà[ A]… không? Đúng vậy.»
    (5-01 b_cut_question; 3-03 with a member). A cut ending «…pe….» (no «?») keeps the Pāli's shape: «…» (sample
    formula)."""
    m = CUTQ_RE.fullmatch(body)
    if not m:
        return None
    label, rel, vapana, y2, mem, end, rest = m.groups()
    who = rel + (y2 or "")
    if (label == "Kha") != bool(vapana):
        raise ValueError(f"label / vā pana mismatch {body!r}")
    out = _shell_head(label, who, bool(vapana)) + (f" {M.subj(mem)}" if mem else "") + PE
    if end == "?":
        out += " không?"
    else:
        SLIPS_SEEN.append(("cut question ending «…pe….» (no «?»): kept «…»", body))
    return out, rest


CUTH_RE = re.compile(r"([Yy]assa|[Yy]attha)( vā pana)?( yattha)? (.+?)…pe…(\.?)")


def cut_half(body):
    """'Yattha A V…pe….' / 'Yassa yattha A V…pe….' / 'Yassa vā pana yattha A V…pe….' → «[Còn ]ở … mà A V…»
    (2-02 b_cut for the plain Yattha / Yassa form, asserted)."""
    m = CUTH_RE.fullmatch(body)
    if not m:
        return None
    w1, vapana, y2, c, _dot = m.groups()
    who = lc(w1) + (y2 or "")
    a, v = B.split_mv(c, M)
    out = f"{_shell_head(None, who, bool(vapana))} {a} {v[0]}{PE}"
    if not vapana and not y2 and _dot:
        assert out == E.b_cut(body, M), (out, E.b_cut(body, M))
    return out


# ===============================================================================================================
# 6. Headings and fixed lines
# ===============================================================================================================
SECTION_HEAD = dict(DY.SECTION_HEAD)


def heading(text):
    if text in SECTION_HEAD:
        return SECTION_HEAD[text]
    if m := re.fullmatch(r"\((\w+)\) paccanīkaokāsā", text):          # ^6-6-16-5-0: plural «okāsā» (termbase)
        return f"{S.LABEL[m.group(1)]} {B.ORDER['paccanīka']} {B.BY['okāso']}"
    return B.heading(text, X_PL, YAMAKA)


UDDESA_PALI = ("Tayo saṅkhārā – kāyasaṅkhāro, vacīsaṅkhāro, cittasaṅkhāroti. Assāsapassāsā kāyasaṅkhāro, "
               "vitakkavicārā vacīsaṅkhāro, saññā ca vedanā ca cittasaṅkhāro. Ṭhapetvā vitakkavicāre sabbepi "
               "cittasampayuttakā dhammā cittasaṅkhāro.")
THREE_KINDS = "Ba loại"                                     # Tayo / Tisso … – (pi-2 15-patisambhidavibhango «Ba loại …»)
CITTASAMPAYUTTA = "các hiện tượng gắn liền với tâm"          # cittasampayuttakā dhammā (termbase; pi-1 mātikā)
SANNA_VEDANA = f"{B.KHANDHA.subj('saññā')} {C.AND} {B.KHANDHA.subj('vedanā')}"   # saññā ca vedanā ca «tri giác và cảm giác»
UDDESA_VI = (f"{THREE_KINDS} {M.pred('saṅkhārā')} – {KAYA_S}, {VACI_S}, {CITTA_S}. {cap(BREATH)} là {KAYA_S}, "
             f"{VITAKKA} là {VACI_S}, {SANNA_VEDANA} là {CITTA_S}. {B.EXCEPT} {VITAKKA}, tất cả "
             f"{CITTASAMPAYUTTA} đều là {CITTA_S}.")
FIXED = {
    UDDESA_PALI: UDDESA_VI,
    "(Kha) paccanīkaṃ": B.heading("(Kha) paccanīkaṃ", X_PL, YAMAKA),     # a heading run into ^6-6-2 / ^6-6-4
    "4 (Ṅa) paccanīkaokāso": "4 " + B.heading("(Ṅa) paccanīkaokāso", X_PL, YAMAKA),   # ^6-6-65 (digit kept)
}
VARIANTS = {"[avasesā saṅkhārā saṅkhārā (sī. syā. kaṃ.)]": "form"}


# ===============================================================================================================
# 7. Line translator
# ===============================================================================================================
def line_vi(body):
    if body in FIXED:
        return FIXED[body]
    if (q := cut_question(body)) or (q := pq_question(body)) or (q := B.a_question(body, M)):
        out, rest = q
        r = rest.strip()
        if r.startswith(DY.CUT_AFTER_Q):                             # "…ti?…Pe…." (9-01)
            out += PE
            r = r[len(DY.CUT_AFTER_Q):].strip()
        if r:
            out += " " + sentences(r)
        return out
    if (c := cut_half(body)) is not None:
        return c
    return sentences(body)


def tr_line(p):
    m = re.search(r" (\^\S+)$", p)
    bid = m.group(1) if m else None
    body = p[:m.start()] if m else p
    if body.startswith("#"):
        hashes, text = body.split(" ", 1)
        out = f"{hashes} {heading(text)}"
    else:
        brs = re.findall(r"\[[^\]]*\]", body)
        for k, br in enumerate(brs):
            body = body.replace(br, f"⟦{k}⟧", 1)
        out = line_vi(body)
        for k, br in enumerate(brs):
            if br not in VARIANTS:
                raise ValueError(f"undeclared variant {br!r}")
            if out.count(f"⟦{k}⟧") != 1:
                raise ValueError(f"variant {br!r} lost in {p!r}")
            out = out.replace(f"⟦{k}⟧", B.parse_variant(br, VARIANTS[br]))
    if "⟦" in out:
        raise ValueError(f"unplaced variant in {p!r}")
    return f"{out} {bid}" if bid else out


def build(name=CHAPTER):
    segs = []
    for seg in S.segments_of(name):
        out = []
        for ln in seg:
            try:
                out.append(tr_line(ln))
            except (ValueError, KeyError, IndexError) as e:
                raise ValueError(f"{name}: cannot place line {ln[:160]!r}: {e!r}") from None
        segs.append(out)
    return segs


def probe(name=CHAPTER):
    bad = 0
    for seg in S.segments_of(name):
        for ln in seg:
            try:
                tr_line(ln)
            except Exception as e:  # noqa: BLE001
                bad += 1
                print("FAIL:", type(e).__name__, str(e)[:300], "\n   ", ln[:200])
    print("failing lines:", bad)


# ===============================================================================================================
# 8. Assertions: reused pi-N strings, the setters' strings
# ===============================================================================================================
REUSED = [
    ("kāyasaṅkhāro, vacīsaṅkhāro, cittasaṅkhāro (pi-2 ^2-226)", f"{KAYA_S}, {VACI_S}, {CITTA_S}", "2"),
    ("catutthaṃ jhānaṃ samāpannassa assāsapassāsā (pi-5 10-dutiyavaggo)", BREATH, "5"),
    ("paṭhamaṃ jhānaṃ samāpannassa (pi-5)", f"người {ATTAINING} {JHANA} {ORD['paṭhama']}", "5"),
    ("dutiyajjhānasamāpatti … (pi-2)", f"{JHANA} {ORD['dutiya']}", "2"),
    ("tatiyajjhānasamāpatti (pi-2)", f"{JHANA} {ORD['tatiya']}", "2"),
    ("catutthajjhānasamāpatti (pi-2)", f"{JHANA} {ORD['catuttha']}", "2"),
    ("savitakkasavicārā dhammā (pi-1 mātikā)", SAVITAKKA, "1"),
    ("avitakkaavicārā dhammā (pi-1 ^1-M1-6)", AVITAKKA, "1"),
    ("cittasampayuttā dhammā (pi-1 mātikā)", CITTASAMPAYUTTA, "1"),
    ("Tisso paṭisambhidā – (pi-2)", f"{THREE_KINDS} hiểu biết thông suốt –", "2"),
    ("vinā rūpena (pi-5 ^5-227)", "không có vật chất", "5"),
]


def check_reused():
    texts = {b: unicodedata.normalize("NFC", "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md"))))
             for b, d in S.RAILS.items()}
    bad = [(p, v, b) for p, v, b in REUSED if unicodedata.normalize("NFC", v).lower() not in texts[b].lower()]
    assert not bad, "reused strings not found in their rails: " + repr(bad)
    t301 = (S.OUT_DIR / "3-01-ayatanayamaka.md").read_text(encoding="utf-8")
    assert "giống hệt nhau" in t301                                    # ekasadisaṃ (3-01)


def check_shared():
    """Strings that must equal the setters' byte for byte."""
    # 9-01 heads (where 9-01's parser can read the Pāli)
    for hd in ("Sabbesaṃ cittassa bhaṅgakkhaṇe nirodhasamāpannānaṃ asaññasattānaṃ", "Pacchimacittasamaṅgīnaṃ",
               "Suddhāvāsānaṃ dutiye citte vattamāne asaññasattānaṃ", "Itaresaṃ", "Suddhāvāsaṃ upapajjantānaṃ",
               "Sabbesaṃ cittassa uppādakkhaṇe nirodhasamāpannānaṃ asaññasattānaṃ",
               "Pacchimacittasamaṅgīnaṃ asaññasattānaṃ", "Suddhāvāsaṃ upapajjantānaṃ asaññasattānaṃ"):
        assert answer_head(hd) == DY.answer_head(hd, "tesaṃ") == DY2.answer_head(hd, "tesaṃ"), hd
    # 3-02 / 3-03 person heads and the ye-ca head
    for hd in ("Rūpāvacarānaṃ arūpāvacarānaṃ", "Itaresaṃ kāmāvacarānaṃ"):
        assert answer_head(hd) == f"{B.AT} {A2.ay_persons(hd, PLANES)}", hd
    hd = "Rūpāvacare arūpāvacare pacchimabhavikānaṃ ye ca rūpāvacaraṃ arūpāvacaraṃ upapajjitvā parinibbāyissanti " \
         "tesaṃ cavantānaṃ"
    assert answer_head(hd) == A3.ye_ca_head(hd, PLANES), (answer_head(hd), A3.ye_ca_head(hd, PLANES))
    # place heads (2-01 place_head)
    for hd in ("Rūpāvacare arūpāvacare", "Asaññasatte", "Kāmāvacare"):
        assert answer_head(hd) == B.place_head(hd, PLANES), hd
    # anantarā shape = 9-01 PERSON_ATTAIN («… ngay sau tâm này»)
    assert DY.PERSON_ATTAIN.endswith(f" {DY.ANANTARA} {DY.THIS_MIND}")
    assert anantara_group(None, True).endswith(f" {DY.ANANTARA} {DY.THIS_MIND}")
    # self_not = 10-01 self_not
    assert self_not(KAYA_S, "thân") == T10.self_not(KAYA_S, "thân")
    # cut question = 5-01 b_cut_question
    for q in ("(Kha) yassa vā pana…pe…? Āmantā.", "(Kha) yassa vā pana yattha…pe…? Āmantā.",
              "(Kha) yattha vā pana…pe…? Āmantā."):
        mine = cut_question(q)
        theirs = T5.b_cut_question(q, M)
        assert mine == theirs, (mine, theirs)
    # 9-01 verbs and short answers
    for w in ("uppajjatīti", "uppajjitthāti", "nuppajjissatīti", "na nirujjhatīti"):
        assert B.verb(w)[0] == DY.verb(w)[0], w
    assert M.subj("saṅkhārā") == B.KHANDHA.subj("saṅkhārā") and M.pred("saṅkhārā") == B.KHANDHA.pred("saṅkhārā")
    assert B.heading("Suddhasaṅkhāravāro", X_PL, YAMAKA) == cap("mục về các tạo tác thuần túy")   # termbase


# ===============================================================================================================
# 9. Notes file (Pāli = tiếng Việt)
# ===============================================================================================================
def notes():
    out = [f"# pi-6 rails {N} (Saṅkhārayamaka 1): the saṅkhāra members, the breathing / vitakka heads, the anantarā "
           "groups", "",
           "Builder: build_rails_6-01_vi.py (import with importlib for 6-02: `SANKHARA_TABLE`, `SANKHARA`, `X_PL`, "
           "`YAMAKA`, `UDDESA_PALI`, `UDDESA_VI`, `BREATH`, `VITAKKA`, `SAVITAKKA`, `AVITAKKA`, `FINAL_MIND`, `BHUMI`, "
           "`JHANA`, `ORD`, `jhana_vi`, `ATTAINING`, `VINA`, `INSTR`, `GEN`, `gen_vi`, `moment`, `anantara_group`, "
           "`EXTRA_PERSON`, `head_parts`, `answer_head`, `self_not`, `a_sentence`, `b_sentence`, `sentence`, "
           "`sentences`, `pq_question`, `cut_question`, `cut_half`, `NOTES`, `SECTION_END`, `FIXED`, `VARIANTS`, "
           "`heading`, `tr_line`, `build`). Frames are 2-01's (A, B), 7-01's shapes, 8's moments / persons, 9-01's "
           "heads, 3-02 / 3-03's person items and ye-ca head, 2-02's KHI_CAVANTA / b_cut, 5-01's note pieces and "
           "cut question, 10-01's self_not: imported READ-ONLY and asserted. Format: Pāli = tiếng Việt.", ""]

    def h(t):
        out.extend(["", f"## {t}", ""])

    def row(p, v):
        out.append(f"{p} = {v}")

    h("Members (SANKHARA, B.Members; subject / predicate)")
    for key, (sv, pv, forms) in SANKHARA_TABLE.items():
        row(" / ".join(forms), f"{sv} / {pv}")
    h("Uddesa, headings, closings, fixed lines")
    row(UDDESA_PALI, UDDESA_VI)
    for p in ("Saṅkhārayamakaṃ", "Paṇṇattivāro", "Padasodhanavāro", "Padasodhanamūlacakkavāro", "Suddhasaṅkhāravāro",
              "(Kha) niddeso", "Pavattivāro 1. uppādavāro", "Nirodhavāro", "(4) Paccuppannātītavāro",
              "(Ṅa) paccanīkaokāsā", "(Ca) paccanīkapuggalokāsā"):
        row(p, heading(p))
    for p, v in FIXED.items():
        if p != UDDESA_PALI:
            row(p + " (line)", v)
    for p in ("Paṇṇattiuddesavāro.", "Paṇṇattivāro.", "Paṇṇattiniddesavāro.", "Uppādavāro."):
        row(p, sentence(p))
    h("Family A with these members (2-01 frames)")
    for q in ("(Ka) kāyo kāyasaṅkhāro?", "(Kha) saṅkhārā vacīsaṅkhāro?", "(Ka) na vacī na vacīsaṅkhāro?",
              "(Kha) na saṅkhārā na cittasaṅkhāroti? Āmantā.", "(Kha) cittasaṅkhāro cittanti? No."):
        row(q, line_vi(q))
    for s in ("Kāyasaṅkhāro na kāyo, kāyasaṅkhāro.", "Cittaṃ na cittasaṅkhāro, cittaṃ.",
              "Vaciñca vacīsaṅkhārañca ṭhapetvā avasesā na ceva vacī na ca vacīsaṅkhāro.",
              "Vacīsaṅkhāro saṅkhāro ceva vacīsaṅkhāro ca.", "Avasesā saṅkhārā na cittasaṅkhāro."):
        row(s, sentence(s))
    row("[avasesā saṅkhārā saṅkhārā (sī. syā. kaṃ.)]", B.parse_variant("[avasesā saṅkhārā saṅkhārā (sī. syā. kaṃ.)]",
                                                                         "form"))
    h("Answer-head words set here")
    for w in ("assāsapassāsānaṃ uppādakkhaṇe", "vitakkavicārānaṃ bhaṅgakkhaṇe", "avitakkaavicāracittassa uppādakkhaṇe",
              "Savitakkasavicārapacchimacittassa uppādakkhaṇe", "Savitakkasavicārapacchimacittassa bhaṅgakkhaṇe"):
        g, mo = w.split()
        row(w, moment(g, mo))
    row("vinā vitakkavicārehi assāsapassāsānaṃ uppādakkhaṇe", moment("assāsapassāsānaṃ", "uppādakkhaṇe",
                                                                       "vitakkavicārehi"))
    row("vinā assāsapassāsehi cittassa uppādakkhaṇe", moment("cittassa", "uppādakkhaṇe", "assāsapassāsehi"))
    row("vinā assāsapassāsehi avitakkaavicāracittassa uppādakkhaṇe",
        moment("avitakkaavicāracittassa", "uppādakkhaṇe", "assāsapassāsehi"))
    row("Paṭhamajjhānaṃ samāpannānaṃ (person) / Paṭhamajjhāne (place)",
        f"{D.PEOPLE} {ATTAINING} {jhana_vi('paṭhamajjhānaṃ')[0]} / {C.AT} {jhana_vi('paṭhamajjhāne')[0]}")
    row("Savitakkasavicārabhūmiyaṃ / Avitakkaavicārabhūmiyaṃ (place)",
        f"{C.AT} {bhumi_vi('Savitakkasavicārabhūmiyaṃ')} / {C.AT} {bhumi_vi('Avitakkaavicārabhūmiyaṃ')}")
    for k, v in EXTRA_PERSON.items():
        row(k, v)
    row("yassa cittassa anantarā kāmāvacarānaṃ pacchimacittaṃ uppajjissati (person group)",
        anantara_group("kāmāvacar", False))
    row("yassa cittassa anantarā avitakkaavicāraṃ pacchimacittaṃ uppajjissati (person group)",
        anantara_group(None, True))
    h("Answer heads as built (… tesaṃ / tesaṃ tattha / tattha …)")
    for hd in ("Vinā vitakkavicārehi assāsapassāsānaṃ uppādakkhaṇe",
               "Paṭhamajjhānaṃ samāpannānaṃ kāmāvacarānaṃ assāsapassāsānaṃ uppādakkhaṇe",
               "Sabbesaṃ cittassa bhaṅgakkhaṇe vinā assāsapassāsehi avitakkaavicāracittassa uppādakkhaṇe "
               "nirodhasamāpannānaṃ asaññasattānaṃ",
               "Dutiyajjhāne tatiyajjhāne", "Paṭhamajjhāne kāmāvacare", "Catutthajjhāne asaññasatte",
               "Dutiyajjhānaṃ tatiyajjhānaṃ samāpannānaṃ", "Catutthajjhānaṃ samāpannānaṃ rūpāvacarānaṃ arūpāvacarānaṃ",
               "Paṭhamajjhānaṃ dutiyajjhānaṃ tatiyajjhānaṃ samāpannānaṃ kāmāvacarānaṃ",
               "Dutiyajjhānaṃ tatiyajjhānaṃ catutthajjhānaṃ samāpannānaṃ suddhāvāsānaṃ dutiye citte vattamāne",
               "Paṭhamajjhānaṃ samāpannānaṃ kāmāvacarānaṃ itaresaṃ rūpāvacarānaṃ arūpāvacarānaṃ",
               "Yassa cittassa anantarā kāmāvacarānaṃ pacchimacittaṃ uppajjissati rūpāvacare arūpāvacare "
               "pacchimabhavikānaṃ ye ca rūpāvacaraṃ arūpāvacaraṃ upapajjitvā parinibbāyissanti tesaṃ cavantānaṃ",
               "Yassa cittassa anantarā avitakkaavicāraṃ pacchimacittaṃ uppajjissati",
               "Pacchimacittasamaṅgīnaṃ yassa cittassa anantarā avitakkaavicāraṃ pacchimacittaṃ uppajjissati",
               "Paṭhamajjhānaṃ samāpannānaṃ itaresaṃ kāmāvacarānaṃ",
               "Paṭhamajjhānaṃ samāpannānaṃ kāmāvacarānaṃ assāsapassāsānaṃ bhaṅgakkhaṇe tesaṃyeva vinā "
               "assāsapassāsehi cittassa uppādakkhaṇe rūpāvacarānaṃ arūpāvacarānaṃ",
               "Itaresaṃ vitakkavicārānaṃ uppādakkhaṇe", "Savitakkasavicārapacchimacittassa uppādakkhaṇe",
               "Savitakkasavicārapacchimacittassa bhaṅgakkhaṇe avitakkaavicārapacchimacittasamaṅgīnaṃ",
               "Kāmāvacare pacchimacittasamaṅgīnaṃ dutiyajjhānaṃ tatiyajjhānaṃ samāpannānaṃ",
               "Savitakkasavicārabhūmiyaṃ pacchimacittasamaṅgīnaṃ", "Itaresaṃ savitakkasavicārabhūmiyaṃ",
               "Suddhāvāsaṃ upapajjantānaṃ asaññasattānaṃ", "Itaresaṃ"):
        row(hd, answer_head(hd) + ", …")
    h("Answer frames as built (2-01 b_noca / b_both)")
    for s in ("Vinā vitakkavicārehi assāsapassāsānaṃ uppādakkhaṇe tesaṃ kāyasaṅkhāro uppajjati, no ca tesaṃ "
              "vacīsaṅkhāro uppajjati.",
              "Vinā assāsapassāsehi vitakkavicārānaṃ uppādakkhaṇe tesaṃ kāyasaṅkhāro nuppajjati, no ca tesaṃ "
              "vacīsaṅkhāro nuppajjati.",
              "Rūpāvacarānaṃ arūpāvacarānaṃ tesaṃ tattha kāyasaṅkhāro nuppajjittha, no ca tesaṃ tattha vacīsaṅkhāro "
              "nuppajjittha.",
              "Asaññasatte tattha kāyasaṅkhāro ca nuppajjati cittasaṅkhāro ca nuppajjati.",
              "Itaresaṃ tesaṃ vacīsaṅkhāro ca uppajjissati kāyasaṅkhāro ca uppajjissati."):
        row(s, sentence(s))
    h("Cut lines and notes")
    for q in ("(Kha) yassa vā pana…pe…? Āmantā.", "(Kha) yassa vā pana cittasaṅkhāro…pe…? Āmantā.",
              "(Kha) yassa vā pana…pe…. Āmantā.", "Yassa yattha kāyasaṅkhāro uppajjati…pe….",
              "Yattha kāyasaṅkhāro uppajjittha…pe…", "Yassa vā pana yattha vacīsaṅkhāro na nirujjhati…pe….",
              "Yattha kāyasaṅkhāro nirujjhati tattha vacīsaṅkhāro nirujjhatīti?…Pe…."):
        row(q, line_vi(q))
    for p, v in NOTES.items():
        row(p, v)
    h("Termbase misfits and gaps (for the coordinator)")
    out += [
        "- Paṭhama- / Dutiya- / Tatiyajjhānaṃ, -jjhāne: only Catutthajjhānaṃ / -e «tầng thiền thứ tư» is in the termbase; "
        "«tầng thiền thứ nhất / thứ hai / thứ ba» from pi-2 / pi-5 rails.",
        "- vinā (assāsapassāsehi / vitakkavicārehi): no entry; pi-5 vinā rūpena «không có vật chất»; placed after the "
        "noun it qualifies with the sample's «mà» («… của hơi thở vào và hơi thở ra mà không có sự hướng tâm và sự duy "
        "trì tâm»; «… của tâm không có sự hướng tâm cũng không có sự duy trì tâm mà không có hơi thở vào và hơi thở ra»).",
        "- Tayo saṅkhārā: «Ba loại tạo tác –» (pi-2 «Ba loại … –»; termbase saṅkhārā «tạo tác»). saññā ca vedanā ca "
        "«tri giác và cảm giác» (2-01 members). sabbepi … dhammā «tất cả các hiện tượng … đều».",
        "- yassa cittassa anantarā … pacchimacittaṃ uppajjissati: a person group in 9-01's PERSON_ATTAIN shape: "
        "«những người mà tâm cuối cùng [không có …] sẽ sinh khởi ngay sau tâm này», with kāmāvacarānaṃ as the head noun "
        "«chúng sinh trong cõi dục lạc mà tâm cuối cùng sẽ sinh khởi ngay sau tâm này» (user: smooth, meaning kept).",
        "- Savitakkasavicārapacchimacittassa: termbase order «tâm cuối cùng có …» (not 8's «tâm <adj> cuối cùng»).",
        "- Kāmāvacare / Rūpāvacare arūpāvacare / -bhūmiyaṃ before pacchimacittasamaṅgīnaṃ: a place with its own «ở» "
        "(9-01 head_parts reads a locative plane as a place unless a 2-01 attribute / participle follows); before "
        "pacchimabhavikānaṃ a group «… trong cõi X» (2-01 / 3-03).",
        "- Lists inside one person group keep «và» («những người đang nhập tầng thiền thứ hai và tầng thiền thứ ba»); "
        "in a longer run the groups are joined once more («…, tầng thiền thứ ba và chúng sinh trong cõi dục lạc»): two "
        "«và» on two levels, as 3-03 «… trong cõi hình sắc và cõi không hình sắc và …». Runs of plane-beings are "
        "flattened (3-02); Itaresaṃ + a run keeps being_run's pieces («…, chúng sinh khác trong cõi hình sắc và cõi "
        "không hình sắc»). Please align if another shape is wanted.",
        "- labbhati (na labbhati) has no entry: «thì không có “…”»; na kātabbaṃ «thì không nên trình bày “…”» (5-02 "
        "wording without -pi); ekasadisaṃ «giống hệt nhau» (3-01).",
        "- Itaresaṃ + plane-beings «chúng sinh khác trong cõi X» (2-01): termbase «người khác» not literal (adherence "
        "misses expected, as 9-02).",
        "",
        "## Pāli as written (reported)",
        "",
        "- ^6-6-2, ^6-6-4: «(Kha) paccanīkaṃ» stands as the last line of the segment: kept as a line «(b) Chiều nghịch».",
        "- ^6-6-65: «4 (Ṅa) paccanīkaokāso» is a heading run into the segment with a stray «4»: kept as a line "
        "«4 (đ) Chiều nghịch theo nơi chốn» (digit kept, as 9-01 «3 Suddhadhammavāro»).",
        "- ^6-6-16-5-0: heading «(Ṅa) paccanīkaokāsā» (plural; termbase «chiều nghịch theo nơi chốn»).",
        "- ^6-6-69: «(Kha) yassa vā pana…pe…. Āmantā.» ends «.» not «?»: kept «(b) Còn ở người nào mà… Đúng vậy.» "
        "(sample formula: «không?» only where the Pāli has «?»; = 5-02).",
        "- ^6-6-31: «Yattha kāyasaṅkhāro uppajjittha…pe…» has no final «.»: «…»; the note «(…).» keeps its own «).».",
        "- ^6-6-81, ^6-6-82: unlabelled «Yattha / Yassa yattha … ti?…Pe….» = «… không?…» (9-01); ^6-6-82 has the "
        "note on the same line; ^6-6-86 unlabelled «Yassa yattha … ti?» and «Yassa vā pana yattha …pe….»: kept "
        "unlabelled.",
        "- ^6-6-23, ^6-6-28, ^6-6-82, ^6-6-86, ^6-6-87: notes ending «.)» keep the period inside the bracket; ^6-6-31 "
        "«).» kept.",
        "",
    ]
    return "\n".join(out)


def main():
    if "--probe" in sys.argv:
        probe()
        return
    S.check_reused()
    B.check_reused()
    DY.check_reused()
    check_reused()
    check_shared()
    segs = build()
    S.write(CHAPTER, segs)
    ADH_DIR.mkdir(exist_ok=True)
    (ADH_DIR / CHAPTER).write_bytes((S.OUT_DIR / CHAPTER).read_bytes())
    print("wrote", ADH_DIR / CHAPTER)
    NOTES_MD.write_text(unicodedata.normalize("NFC", notes()), encoding="utf-8", newline="\n")
    print("wrote", NOTES_MD)
    for s in SLIPS_SEEN:
        print("note:", s)


if __name__ == "__main__":
    main()
