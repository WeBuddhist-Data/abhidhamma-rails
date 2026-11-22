"""pi-6 Yamaka, Vietnamese plain RAILS: chapter 9-01 (Dhammayamaka 1: paṇṇattivāra + pavattivāra uppādavāra) and
the DHAMMA-YAMAKA module that 9-02 and 9-03 import.

Families: A (paṇṇattivāra) and B (pavattivāra) from build_rails_2-01_vi, the shared answer shapes from
build_rails_7-01_vi, the moment heads / persons / aspect forms from build_rails_8_vi. All three are imported
READ-ONLY; this file only plugs in the Dhammayamaka members and the answer heads that are new here.

Import READ-ONLY (importing writes nothing; outputs are written only under `if __name__ == "__main__":`):
    sys.path.insert(0, r"D:\\Work\\OpenPecha\\abhidhamma-rails\\0-INBOX\\temp\\pipeline\\pi-6-vi-ai\\rails")
    import importlib; DY = importlib.import_module("build_rails_9-01_vi")

What the module gives 9-02 / 9-03 (all byte-fixed; never retype the strings):
  DHAMMA (B.Members)               kusalā / akusalā / abyākatā, kusalā dhammā …, Kusalaṃ …, dhammā / dhamme
  DHAMMA_GEN / KIND_DHAMMAS        kusalānaṃ «các hiện tượng thiện» … (genitive pl. of a moment head)
  mind_gen()                       cittassa «tâm», kusalavippayuttacittassa «tâm không gắn liền với các hiện tượng
                                   thiện», two-part kinds «tâm <A> và <B>» (coordinator)
  MOMENT_GEN                       Aggamaggassa «con đường tối thượng»
  PAVATTE, ALL_BEINGS, ORDINAL,    pavatte «trong đời sống»; bare Sabbesaṃ «tất cả chúng sinh»; dutiye «thứ hai»;
  WHILE / OCCURRING                «khi tâm … đang diễn ra» (pi-5)
  ATTAIN_TOP / PERSON_ATTAIN /     yassa cittassa anantarā aggamaggaṃ paṭilabhissanti (person group) and
  that_mind_moment()               … tassa cittassa <moment> (moment)
  EXTRA_PERSON                     nirodhasamāpannānaṃ, pacchimacittasamaṅgīnaṃ (8), aggamaggasamaṅgīnaṃ, arahantānaṃ
  head_parts() / answer_head()     answer heads: persons, places, moments, pavatte, «khi …» (parts joined «, » as 8)
  verb() / split_mv()              B's VERB_TABLE + a separate "na" on any positive form; plural -ntīti handled
  pq_question() / name_question()  the B / A question frames with multi-word members (B.b_q, B.name_q, B.name_q_neg)
  a_sentence() / b_sentence()      answers (B.both_is, B.rest_not_is, B.a_sentence; B.b_noca, B.b_both)
  SECTION_END / FIXED / heading()  closings ("Uppādavāro." …), "(Kha) niddeso" as a line, numbered headings
  tr_line() / build()              the line translator
A line the parsers cannot place raises ValueError: there is no silent fallback.

usage: python -I -X utf8 -B build_rails_9-01_vi.py
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
B = importlib.import_module("build_rails_2-01_vi")   # families A, B (READ-ONLY)
C = importlib.import_module("build_rails_7-01_vi")   # shared answer shapes (READ-ONLY)
D = importlib.import_module("build_rails_8_vi")      # moments, persons, aspect forms (READ-ONLY)

CHAPTER = "9-01-dhammayamaka.md"
N = "9-01"
NOTES_MD = RAILS_DIR / f"notes-rails-{N}.md"
ADH_DIR = RAILS_DIR / f"adh-{N}"
cap = S.cap
PE = S.PE
YAMAKA = "Dhamma"
X_PL = "hiện tượng"                       # Suddhadhammavāro «Mục về các hiện tượng thuần túy» (termbase)


def lc(w):
    return w[:1].lower() + w[1:]


# ===============================================================================================================
# 1. Members (termbase: kusalā dhammā «hiện tượng thiện» …; sample X_SLOT / KIND / SUBJ)
# ===============================================================================================================
KINDS = ("kusala", "akusala", "abyākata")
WHAT = "những gì"                         # head of a bare adjective subject (= 2-01 REST «những gì còn lại», NEG_SUBJ)


def _member_table():
    t = {}
    for k in KINDS:
        stem = k[:-1]                                         # kusal / akusal / abyākat
        # bare adjective "kusalā": subject «những gì là thiện» (sample X_SLOT), predicate «thiện» (sample KIND)
        t[k] = (f"{WHAT} {S.X_SLOT[k]}", S.KIND[k], [f"{stem}ā"])
        # "kusalā dhammā": subject «các hiện tượng thiện», predicate «hiện tượng thiện» (termbase, sample SUBJ)
        t[f"{k} dhammā"] = (f"các {S.SUBJ[k]}", S.SUBJ[k], [f"{stem}ā dhammā"])
        # "Kusalaṃ (ṭhapetvā)", "Kusalañca": «hiện tượng thiện» (termbase Kusalañca dhamme / kusalaṃ dhammaṃ)
        t[f"{k} sg"] = (S.SUBJ[k], S.KIND[k], [f"{stem}aṃ"])
    t["dhammā"] = ("các hiện tượng", X_PL, ["dhammā", "dhamme"])   # termbase Kusalañca dhamme «… các hiện tượng»
    return t


MEMBER_TABLE = _member_table()
DHAMMA = B.Members(MEMBER_TABLE)
KIND_DHAMMAS = {k: MEMBER_TABLE[f"{k} dhammā"][0] for k in KINDS}       # «các hiện tượng thiện» …
DHAMMA_GEN = {f"{k[:-1]}ānaṃ": KIND_DHAMMAS[k] for k in KINDS}         # kusalānaṃ (uppādakkhaṇe) «… của các hiện tượng thiện»


def member_split(words, n=2):
    """Split a word list into n consecutive member phrases; exactly one split must fit (else ValueError)."""
    words = list(words)
    if n == 1:
        DHAMMA.key(" ".join(words))
        return [" ".join(words)]
    hits = []
    for i in range(1, len(words)):
        head = " ".join(words[:i])
        try:
            DHAMMA.key(head)
            rest = member_split(words[i:], n - 1)
        except ValueError:
            continue
        hits.append([head] + rest)
    if len(hits) != 1:
        raise ValueError(f"cannot split {' '.join(words)!r} into {n} members ({len(hits)} ways)")
    return hits[0]


# ===============================================================================================================
# 2. Verbs: B.VERB_TABLE (2-01) + a separate "na" on a positive form (= 8 VERB_NEG); -ntīti handled here
# ===============================================================================================================
def verb(w):
    """Pāli verb word(s) → B's tuple (vi, negative?, positive vi, negative vi). 'na uppajjanti' = «không sinh khởi»,
    'na uppajjittha' «chưa từng sinh khởi», 'na uppajjissanti' «sẽ không sinh khởi» (coordinator: a separate "na"
    negates the positive term). B.verb() finds two readings for plural -ntīti (ntīti→nti, īti→i): deduplicated."""
    if w.startswith("na "):
        p = verb(w[3:])
        if p[1]:
            raise ValueError(f"double negative {w!r}")
        return (p[3], True, p[2], p[3])
    cands = {w}
    for end, rep in (("ntīti", "nti"), ("īti", "i"), ("āti", "a")):
        if w.endswith(end):
            cands.add(w[:-len(end)] + rep)
    hits = {B.VERB[c] for c in cands if c in B.VERB}
    if len(hits) != 1:
        raise ValueError(f"unknown verb {w!r}")
    return hits.pop()


def is_verb(w):
    try:
        verb(w)
        return True
    except ValueError:
        return False


def split_mv(chunk):
    """'kusalā dhammā na uppajjanti' → («các hiện tượng thiện», verb tuple). Verb = last two words, else the last."""
    w = chunk.split()
    for k in (2, 1):
        if len(w) > k and is_verb(" ".join(w[-k:])):
            return DHAMMA.subj(" ".join(w[:-k])), verb(" ".join(w[-k:]))
    raise ValueError(f"no member + verb in {chunk!r}")


# ===============================================================================================================
# 3. Answer heads (persons, places, moments, pavatte, «khi … đang diễn ra»)
# ===============================================================================================================
VIPPAYUTTA = "không gắn liền với"         # -vippayutta (pi-1 «không gắn liền với …»; termbase)
MOMENT_GEN = {"aggamaggassa": "con đường tối thượng"}   # Aggamaggassa (termbase)
PAVATTE = "trong đời sống"                # pavatte (coordinator / termbase APPROVED)
ALL_BEINGS = "tất cả chúng sinh"          # bare Sabbesaṃ (coordinator «Ở tất cả chúng sinh»)
ORDINAL = {"dutiye": "thứ hai"}           # dutiye citte (no termbase entry; plain ordinal)
WHILE, OCCURRING = "khi", "đang diễn ra"  # citte vattamāne «khi tâm … đang diễn ra» (termbase; pi-5 17-navamavaggo)
ANANTARA = "ngay sau"                     # anantarā (termbase)
ATTAIN_TOP = "sẽ đạt được con đường tối thượng"   # aggamaggaṃ paṭilabhissanti (termbase)
THIS_MIND = f"{D.MIND} này"
# yassa cittassa anantarā aggamaggaṃ paṭilabhissanti (a person group, no correlative): smooth, meaning kept
# (coordinator: not the stiff «Vào tâm mà ngay sau đó …»)
PERSON_ATTAIN = f"{D.PEOPLE} {ATTAIN_TOP} {ANANTARA} {THIS_MIND}"
YASSA_CITTASSA = ["yassa", "cittassa", "anantarā", "aggamaggaṃ", "paṭilabhissanti"]
EXTRA_PERSON = {   # genitive plural persons not in 2-01's registry (lower-case first letter)
    "nirodhasamāpannānaṃ": D.PERSON["nirodhasamāpannānaṃ"],          # (8)
    "pacchimacittasamaṅgīnaṃ": D.PERSON["pacchimacittasamaṅgīnaṃ"],  # (8)
    "aggamaggasamaṅgīnaṃ": f"{D.PEOPLE} có được con đường tối thượng",   # termbase «người có được con đường tối thượng»
    "arahantānaṃ": "các bậc A-la-hán",                                 # termbase «bậc A-la-hán»; pi-5 «các bậc A-la-hán»
}


def moment_vi(moment_loc, gen_vi):
    """'uppādakkhaṇe' + «tâm …» → «vào khoảnh khắc sinh khởi của tâm …» (8 moment_phrase shape)."""
    return f"{D.AT_TIME} {D.MOMENT[lc(moment_loc)]} {D.OF} {gen_vi}"


def that_mind_moment(moment_loc):
    """yassa cittassa anantarā aggamaggaṃ paṭilabhissanti tassa cittassa <moment> →
    «vào khoảnh khắc … của tâm mà ngay sau đó sẽ đạt được con đường tối thượng»."""
    return moment_vi(moment_loc, f"{D.MIND} mà {ANANTARA} đó {ATTAIN_TOP}")


def mind_gen(word):
    """cittassa «tâm»; kusalavippayuttacittassa «tâm không gắn liền với các hiện tượng thiện»;
    kusalavippayuttaakusalavippayuttacittassa «tâm không gắn liền với các hiện tượng thiện và không gắn liền với
    các hiện tượng bất thiện» (two-part kinds «tâm <A> và <B>», coordinator; = termbase)."""
    w = lc(word)
    if not w.endswith("cittassa"):
        raise ValueError(f"not a mind genitive {word!r}")
    stem = w[:-len("cittassa")]
    if not stem:
        return D.MIND
    parts = stem.split("vippayutta")
    if parts[-1] != "" or any(p not in KINDS for p in parts[:-1]):
        raise ValueError(f"unknown kind of mind {word!r}")
    return f"{D.MIND} " + f" {C.AND} ".join(f"{VIPPAYUTTA} {KIND_DHAMMAS[p]}" for p in parts[:-1])


def gen_vi(word):
    """Genitive before a moment word → Vietnamese, or None."""
    w = lc(word)
    if w.endswith("cittassa"):
        return mind_gen(word)
    if w in DHAMMA_GEN:
        return DHAMMA_GEN[w]
    if w in MOMENT_GEN:
        return MOMENT_GEN[w]
    return None


def _is_b_person(toks, i):
    """Token i starts / continues a 2-01 person phrase (quantifier, participle, attribute, plane case)?"""
    t = lc(toks[i])
    nxt = lc(toks[i + 1]) if i + 1 < len(toks) else None
    if t in B.QUANT or t in B.PARTICIPLES or t in B.ATTRS:
        return True
    pt = B.plane_tok(t)
    if not pt:
        return False
    if pt[1] == "loc":                    # a locative plane is a place, unless a participle / attribute follows
        return nxt in B.PARTICIPLES or nxt in B.ATTRS
    return True


def head_parts(head):
    """Pāli answer head (before tesaṃ / tesaṃ tattha) → list of Vietnamese parts (first part capitalised by the
    caller). One «ở» for a run of persons; each place its own «ở»; moments «vào …»; pavatte «trong đời sống»;
    «khi tâm … đang diễn ra». A person run after a time phrase takes its own «ở» (coordinator)."""
    toks = head.split()
    parts, run, i = [], [], 0

    def flush():
        if run:
            if len(run) > 1 and any(f" {C.AND} " in g for g in run):
                raise ValueError(f"«và» inside a group of a longer person run: {head!r}")
            parts.append(f"{C.AT} {B.join_and(run)}")
            run.clear()

    while i < len(toks):
        t, lt = toks[i], lc(toks[i])
        if [lc(x) for x in toks[i:i + 5]] == YASSA_CITTASSA:
            if toks[i + 5:i + 7] == ["tassa", "cittassa"]:
                if i + 7 >= len(toks) or lc(toks[i + 7]) not in D.MOMENT:
                    raise ValueError(f"'tassa cittassa' without a moment in {head!r}")
                flush()
                parts.append(that_mind_moment(toks[i + 7]))
                i += 8
            else:
                run.append(PERSON_ATTAIN)
                i += 5
            continue
        if i + 1 < len(toks) and lc(toks[i + 1]) in D.MOMENT:
            g = gen_vi(t)
            if g is None:
                raise ValueError(f"unknown genitive {t!r} before a moment in {head!r}")
            flush()
            parts.append(moment_vi(toks[i + 1], g))
            i += 2
            continue
        if lt == "pavatte":
            flush()
            parts.append(PAVATTE)
            i += 1
            continue
        if lt in ORDINAL:                                     # dutiye [akusale] citte vattamāne
            j, adj = i + 1, ""
            if j < len(toks) and toks[j].endswith("e") and toks[j][:-1] + "a" in KINDS:
                adj = " " + S.KIND[toks[j][:-1] + "a"]
                j += 1
            if toks[j:j + 2] != ["citte", "vattamāne"]:
                raise ValueError(f"unknown time phrase in {head!r}")
            flush()
            parts.append(f"{WHILE} {D.MIND}{adj} {ORDINAL[lt]} {OCCURRING}")
            i = j + 2
            continue
        pt = B.plane_tok(t)
        if pt and pt[1] == "loc" and not _is_b_person(toks, i):
            flush()
            parts.append(f"{C.AT} {B.PLANES[pt[0]][0]}")
            i += 1
            continue
        if lt in EXTRA_PERSON:
            run.append(EXTRA_PERSON[lt])
            i += 1
            continue
        if lt == "sabbesaṃ" and not (i + 1 < len(toks) and _is_b_person(toks, i + 1)):
            run.append(ALL_BEINGS)
            i += 1
            continue
        if _is_b_person(toks, i):
            j = i + 1
            while j < len(toks) and _is_b_person(toks, j) and lc(toks[j]) not in B.QUANT \
                    and not (j + 1 < len(toks) and lc(toks[j + 1]) in D.MOMENT):
                j += 1
            run.append(B.persons(" ".join(toks[i:j])))
            i = j
            continue
        raise ValueError(f"unknown word {t!r} in answer head {head!r}")
    flush()
    if not parts:
        raise ValueError(f"empty answer head {head!r}")
    return parts


def answer_head(head, loc):
    if loc == "tattha":
        return B.place_head(head)                             # «Ở cõi X, ở cõi Y» (2-01 / 7-01)
    return cap(", ".join(head_parts(head)))


# ===============================================================================================================
# 4. Questions (family B shell = B.b_q / C.pair_q; family A naming questions = B.name_q / B.name_q_neg)
# ===============================================================================================================
PQ_RE = re.compile(r"(?:" + B.LABEL_RE + r" )?([Yy]assa|[Yy]attha)( vā pana)?( yattha)? (.+?) "
                   r"(tassa tattha|tassa|tattha) (.+?)\?(.*)")
CUT_AFTER_Q = "…Pe…."                     # "…ti?…Pe…." (anulomaokāso / paccanīkaokāso of the mixed tenses)


def pq_question(body):
    m = PQ_RE.fullmatch(body)
    if not m:
        return None
    label, w1, vapana, w2, c1, then, c2, rest = m.groups()
    if label is None and w1[0] != w1[0].upper():
        raise ValueError(f"unlabelled lower-case question {body!r}")
    who = lc(w1) + (w2 or "")
    a, v1 = split_mv(c1)
    b, v2 = split_mv(c2)
    return B.b_q(label, who, then, a, v1[0], b, v2[0], other=bool(vapana)), rest


NQ_RE = re.compile(B.LABEL_RE + r" ([^?]+)\?((?: .*)?)")


def name_question(body):
    """(Ka) A B? / (Ka) na A na B(ti)? with one- or two-word members."""
    m = NQ_RE.fullmatch(body)
    if not m:
        return None
    label, q, rest = m.groups()
    w = q.split()
    if w[0] == "na":
        if w.count("na") != 2 or "na" not in w[2:]:
            raise ValueError(f"half-negated naming question {body!r}")
        k = w.index("na", 1)
        a, b = " ".join(w[1:k]), " ".join(w[k + 1:])
        return B.name_q_neg(label, DHAMMA.pred(a), DHAMMA.pred(b)), rest
    if "na" in w:
        raise ValueError(f"half-negated naming question {body!r}")
    a, b = member_split(w)
    return B.name_q(label, DHAMMA.subj(a), DHAMMA.pred(b)), rest


# ===============================================================================================================
# 5. Answer sentences
# ===============================================================================================================
SECTION_END = dict(B.CLOSING) | {          # closings without niṭṭhito (9-01 ^6-9-98)
    "Uppādavāro.": f"{cap(B.UPPADAVARO)}.",
    "Nirodhavāro.": f"{cap(B.NIRODHAVARO)}.",
    "Uppādanirodhavāro.": f"{cap(B.UPPADANIRODHAVARO)}.",
}


def a_sentence(s):
    """Family A answers with multi-word members; the ṭhapetvā answers go to B.a_sentence (one-word members)."""
    if "ṭhapetvā" not in s and (m := re.fullmatch(r"(.+) ceva (.+) ca\.", s)):   # Akusalā dhammā dhammā ceva akusalā dhammā ca.
        a, b = member_split(m.group(1).split())
        return B.both_is(DHAMMA.subj(a), DHAMMA.pred(b), DHAMMA.pred(m.group(2)))
    if (m := re.fullmatch(r"Avasesā (.+?) na (.+)\.", s)) and "ṭhapetvā" not in s:   # Avasesā dhammā na akusalā dhammā.
        return B.rest_not_is(DHAMMA.subj(m.group(1)), DHAMMA.pred(m.group(2)))
    return B.a_sentence(s, DHAMMA)


LOC_RE = B.LOC_RE


def b_sentence(s):
    if m := re.fullmatch(r"(.+?) " + LOC_RE + r" (.+?), no ca \2 (.+?)\.", s):
        head, loc, c1, c2 = m.groups()
        a, v1 = split_mv(c1)
        b, v2 = split_mv(c2)
        return B.b_noca(answer_head(head, loc), loc, a, v1, b, v2)
    if m := re.fullmatch(r"(.+?) " + LOC_RE + r" (\S+) ca dhammā ((?:na )?\S+) (\S+) ca dhammā ((?:na )?\S+)\.", s):
        head, loc, k1, w1, k2, w2 = m.groups()
        return B.b_both(answer_head(head, loc), loc, DHAMMA.subj(f"{k1} dhammā"), verb(w1),
                        DHAMMA.subj(f"{k2} dhammā"), verb(w2))
    return None


def sentence(s):
    if s in B.SHORT:
        return B.SHORT[s]
    if s in SECTION_END:
        return SECTION_END[s]
    for f in (b_sentence, a_sentence):
        out = f(s)
        if out is not None:
            return out
    raise ValueError(f"unknown sentence {s!r}")


def sentences(rest):
    parts = [x for x in re.split(r"(?<=\.) ", rest.strip()) if x]
    return " ".join(sentence(x) for x in parts)


# ===============================================================================================================
# 6. Headings and fixed lines
# ===============================================================================================================
SECTION_HEAD = {
    "Pavattivāro": B.PAVATTIVARO,                              # Mục về sự diễn tiến
    "Uppādavāro": cap(B.UPPADAVARO),                           # Mục về sự sinh khởi
    "Nirodhavāro": cap(B.NIRODHAVARO),                         # Mục về sự chấm dứt
    "Uppādanirodhavāro": cap(B.UPPADANIRODHAVARO),             # Mục về sự sinh khởi và sự chấm dứt
}


def heading(text):
    if text in SECTION_HEAD:
        return SECTION_HEAD[text]
    if m := re.fullmatch(r"(\d+) (Suddha\w+vāro)", text):     # "3 Suddhadhammavāro" (number kept)
        return f"{m.group(1)} {B.heading(m.group(2), X_PL, YAMAKA)}"
    return B.heading(text, X_PL, YAMAKA)


FIXED = {
    "(Kha) niddeso": f"{S.LABEL['Kha']} {S.NIDDESO}",          # a heading run into segment ^6-9-16 as a line
}


# ===============================================================================================================
# 7. Line translator
# ===============================================================================================================
def tr_line(p):
    m = re.search(r" (\^\S+)$", p)
    bid = m.group(1) if m else None
    body = p[:m.start()] if m else p
    if "[" in body:
        raise ValueError(f"variant bracket not handled: {p!r}")
    if body.startswith("#"):
        hashes, text = body.split(" ", 1)
        out = f"{hashes} {heading(text)}"
    elif body in FIXED:
        out = FIXED[body]
    elif (q := pq_question(body)) or (q := name_question(body)):
        out, rest = q
        if rest.strip() == CUT_AFTER_Q:
            out += PE
        elif rest.strip():
            out += " " + sentences(rest)
    else:
        out = sentences(body)
    return f"{out} {bid}" if bid else out


def build(name=CHAPTER):
    return [[tr_line(ln) for ln in seg] for seg in S.segments_of(name)]


# ===============================================================================================================
# 8. Reuse assertions (pi-1 … pi-5 rails) and the shared strings
# ===============================================================================================================
REUSED = [
    ("hetuvippayuttā dhammā (-vippayutta)", "không gắn liền với", "1"),
    ("kusalābyākate citte vattamāne (pi-5 17-navamavaggo)", "đang diễn ra", "5"),
    ("arahantānaṃ (pi-5 2-parihanikatha)", "các bậc A-la-hán", "5"),
    ("Avasesā dhammā …", "Các hiện tượng còn lại", "2"),
]


def check_reused():
    texts = {b: unicodedata.normalize("NFC", "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md"))))
             for b, d in S.RAILS.items()}
    bad = [(p, v, b) for p, v, b in REUSED if unicodedata.normalize("NFC", v).lower() not in texts[b].lower()]
    assert not bad, "reused strings not found in their rails: " + repr(bad)


def check_shared():
    """Strings that must equal the setters' (sample, 2-01, 7-01, 8) byte for byte."""
    assert KIND_DHAMMAS["kusala"] == "các " + S.SUBJ["kusala"]
    assert D.MIND == "tâm" and D.AT_TIME == "vào" and D.OF == "của"
    assert B.AT == cap(C.AT) and D.AT == C.AT
    assert D.PEOPLE == B.PERSON
    assert verb("na uppajjanti")[0] == D.neg("uppajjati")
    assert verb("na uppajjittha")[0] == D.neg("uppajjittha")
    assert verb("na uppajjissanti")[0] == D.neg("uppajjissati")
    assert verb("uppajjantīti") == B.VERB["uppajjanti"]
    assert B.b_q("Ka", "yassa", "tassa", "A", "V1", "B", "V2") == "(a) " + C.pair_q("yassa", "A V1", "B V2")


# ===============================================================================================================
# 9. Notes file (Pāli = tiếng Việt)
# ===============================================================================================================
def notes():
    out = [f"# pi-6 rails {N} (Dhammayamaka 1): members and answer heads for the Dhammayamaka (9-01 … 9-03)", "",
           "Builder: build_rails_9-01_vi.py (import with importlib: `DHAMMA`, `MEMBER_TABLE`, `KIND_DHAMMAS`, "
           "`DHAMMA_GEN`, `mind_gen`, `MOMENT_GEN`, `PAVATTE`, `ALL_BEINGS`, `ORDINAL`, `WHILE`, `OCCURRING`, "
           "`ATTAIN_TOP`, `PERSON_ATTAIN`, `that_mind_moment`, `EXTRA_PERSON`, `head_parts`, `answer_head`, `verb`, "
           "`split_mv`, `member_split`, `pq_question`, `name_question`, `a_sentence`, `b_sentence`, `sentence`, "
           "`SECTION_END`, `SECTION_HEAD`, `heading`, `FIXED`, `tr_line`, `build`). Frames are 2-01's (families A, B), "
           "7-01's answer shapes and 8's moments / persons, imported READ-ONLY; nothing retyped. Format: Pāli = tiếng Việt.",
           ""]

    def h(t):
        out.extend(["", f"## {t}", ""])

    def row(p, v):
        out.append(f"{p} = {v}")

    h("Members (DHAMMA, B.Members)")
    for key, (sv, pv, forms) in MEMBER_TABLE.items():
        row(" / ".join(forms) + " (subject / predicate)", f"{sv} / {pv}")
    for k, v in DHAMMA_GEN.items():
        row(f"{k} (genitive, before a moment)", v)
    h("Headings")
    for p in ("Dhammayamakaṃ", "Paṇṇattivāro", "(Ka) uddeso", "Padasodhanavāro", "Padasodhanamūlacakkavāro",
              "(Ka) anulomaṃ", "(Kha) paccanīkaṃ", "3 Suddhadhammavāro", "4 Suddhadhammamūlacakkavāro",
              "Suddhadhammavāro", "Suddhadhammamūlacakkavāro", "Pavattivāro", "Uppādavāro", "Nirodhavāro",
              "(1) Paccuppannavāro", "(4) Paccuppannātītavāro", "(Ga) anulomapuggalokāsā", "(Ṅa) paccanīkaokāso"):
        row(p, heading(p))
    for p, v in FIXED.items():
        row(p + " (line)", v)
    for p in ("Paṇṇattiniddesavāro.", "Uppādavāro.", "Nirodhavāro."):
        row(p, SECTION_END[p])
    h("Family A with these members (2-01 frames)")
    for q in ("(Ka) kusalā kusalā dhammā?", "(Kha) kusalā dhammā kusalā?", "(Ka) abyākatā abyākatā dhammā?",
              "(Kha) dhammā akusalā dhammā?", "(Ka) na kusalā na kusalā dhammā?", "(Kha) na dhammā na akusalā dhammā?",
              "(Ka) kusalā dhammā?", "(Kha) dhammā kusalā?", "(Ka) na kusalā na dhammā?", "(Kha) na dhammā na kusalā?",
              "(Kha) dhammā kusalā dhammāti?"):
        row(q, name_question(q)[0])
    for s in ("Akusalā dhammā dhammā ceva akusalā dhammā ca.", "Avasesā dhammā na akusalā dhammā.",
              "Kusalaṃ ṭhapetvā avasesā dhammā na kusalā, dhammā.",
              "Kusalañca dhamme ca ṭhapetvā avasesā na ceva kusalā na ca dhammā.",
              "Abyākataṃ ṭhapetvā avasesā dhammā na abyākatā, dhammā."):
        row(s, sentence(s))
    h("Family B with these members (2-01 / 7-01 frames)")
    for q in ("(Ka) yassa kusalā dhammā uppajjanti tassa akusalā dhammā uppajjantīti?",
              "(Kha) yassa vā pana akusalā dhammā na uppajjittha tassa kusalā dhammā na uppajjantīti?",
              "(Ka) yassa yattha kusalā dhammā na uppajjanti tassa tattha abyākatā dhammā na uppajjissantīti?",
              "Yattha kusalā dhammā uppajjanti tattha akusalā dhammā uppajjitthāti?…Pe…."):
        row(q, tr_line(q))
    row("na uppajjanti / na uppajjittha / na uppajjissanti (separate na)",
        " / ".join(verb(x)[0] for x in ("na uppajjanti", "na uppajjittha", "na uppajjissanti")))
    row("…ti?…Pe…. (a cut after a full question)", "… không?…")
    h("Answer heads set here (parts joined «, » as 8; one «ở» per person run; places / moments their own)")
    for w in ("cittassa", "kusalavippayuttacittassa", "akusalavippayuttacittassa",
              "kusalavippayuttaakusalavippayuttacittassa", "akusalavippayuttakusalavippayuttacittassa"):
        row(f"{w} uppādakkhaṇe", moment_vi("uppādakkhaṇe", mind_gen(w)))
    row("kusalānaṃ uppādakkhaṇe / bhaṅgakkhaṇe", f"{moment_vi('uppādakkhaṇe', DHAMMA_GEN['kusalānaṃ'])} / "
        f"{moment_vi('bhaṅgakkhaṇe', DHAMMA_GEN['kusalānaṃ'])}")
    row("Aggamaggassa uppādakkhaṇe", moment_vi("uppādakkhaṇe", MOMENT_GEN["aggamaggassa"]))
    row("yassa cittassa anantarā aggamaggaṃ paṭilabhissanti (person group)", PERSON_ATTAIN)
    row("yassa cittassa anantarā aggamaggaṃ paṭilabhissanti tassa cittassa uppādakkhaṇe", that_mind_moment("uppādakkhaṇe"))
    row("pavatte", PAVATTE)
    row("Sabbesaṃ (bare, before a moment)", f"{cap(C.AT)} {ALL_BEINGS}")
    row("dutiye citte vattamāne / dutiye akusale citte vattamāne",
        f"{WHILE} {D.MIND} {ORDINAL['dutiye']} {OCCURRING} / {WHILE} {D.MIND} {S.KIND['akusala']} {ORDINAL['dutiye']} {OCCURRING}")
    for k, v in EXTRA_PERSON.items():
        row(k, v)
    for hd in ("Arūpe kusalānaṃ uppādakkhaṇe", "Sabbesaṃ upapajjantānaṃ pavatte kusalavippayuttacittassa uppādakkhaṇe",
               "Sabbesaṃ cittassa bhaṅgakkhaṇe kusalavippayuttaakusalavippayuttacittassa uppādakkhaṇe "
               "nirodhasamāpannānaṃ asaññasattānaṃ",
               "Sabbesaṃ cavantānaṃ pavatte cittassa bhaṅgakkhaṇe arūpe akusalānaṃ uppādakkhaṇe",
               "Suddhāvāsānaṃ dutiye akusale citte vattamāne", "Suddhāvāsānaṃ dutiye citte vattamāne asaññasattānaṃ",
               "Itaresaṃ catuvokārānaṃ pañcavokārānaṃ", "Suddhāvāsaṃ upapajjantānaṃ",
               "Yassa cittassa anantarā aggamaggaṃ paṭilabhissanti", "Aggamaggasamaṅgīnaṃ arahantānaṃ",
               "Aggamaggasamaṅgīnaṃ arahantānaṃ yassa cittassa anantarā aggamaggaṃ paṭilabhissanti asaññasattānaṃ",
               "Pacchimacittasamaṅgīnaṃ", "Itaresaṃ kusalānaṃ uppādakkhaṇe",
               "Aggamaggassa uppādakkhaṇe yassa cittassa anantarā aggamaggaṃ paṭilabhissanti tassa cittassa uppādakkhaṇe",
               "Aggamaggassa bhaṅgakkhaṇe arahantānaṃ yassa cittassa anantarā aggamaggaṃ paṭilabhissanti tassa cittassa "
               "bhaṅgakkhaṇe asaññasattānaṃ"):
        row(f"{hd} tesaṃ …", f"{answer_head(hd, 'tesaṃ')}, {C.THEN} {B.L['tesaṃ']} …")
    row("Asaññasatte / Catuvokāre pañcavokāre tattha …", f"{answer_head('Asaññasatte', 'tattha')} / "
        f"{answer_head('Catuvokāre pañcavokāre', 'tattha')}, {C.THEN} {B.L['tattha']} …")
    h("Answer frames as built (2-01 b_noca / b_both)")
    for s in ("Arūpe kusalānaṃ uppādakkhaṇe tesaṃ kusalā dhammā uppajjanti, no ca tesaṃ abyākatā dhammā uppajjanti.",
              "Akusalānaṃ uppādakkhaṇe tesaṃ kusalā dhammā na uppajjanti, no ca tesaṃ akusalā dhammā na uppajjanti.",
              "Suddhāvāsānaṃ dutiye akusale citte vattamāne tesaṃ tattha kusalā dhammā na uppajjittha, no ca tesaṃ "
              "tattha akusalā dhammā na uppajjittha.",
              "Pañcavokāre kusalānaṃ uppādakkhaṇe tesaṃ kusalā ca dhammā uppajjanti abyākatā ca dhammā uppajjanti.",
              "Pacchimacittasamaṅgīnaṃ tesaṃ kusalā ca dhammā na uppajjissanti abyākatā ca dhammā na uppajjissanti."):
        row(s, sentence(s))
    h("Termbase misfits and gaps (for the coordinator)")
    out += [
        "- Kusalaṃ / Akusalaṃ / Abyākataṃ (ṭhapetvā): termbase kusalaṃ «thiện» (adjective); as the object of ṭhapetvā "
        "the sibling entries Kusalañca dhamme «hiện tượng thiện và các hiện tượng» / kusalaṃ dhammaṃ «hiện tượng thiện» "
        "are used: «Ngoại trừ hiện tượng thiện, …».",
        "- bare kusalā / akusalā / abyākatā as a subject (naming questions): «những gì là thiện / là bất thiện / không "
        "xác định về mặt đạo đức» (sample X_SLOT after 2-01's «những gì …»); as a predicate the sample KIND «thiện» …, so "
        "«có phải là không xác định về mặt đạo đức không?» and «Những gì không phải là không xác định về mặt đạo đức …» "
        "keep 2-01's «có phải là» / «không phải là» frame.",
        "- dutiye (citte): no termbase entry; «thứ hai».",
        "- arahantānaṃ in a person list: termbase «bậc A-la-hán», plural «các bậc A-la-hán» (pi-5).",
        "- yassa cittassa anantarā aggamaggaṃ paṭilabhissanti (no correlative, a person group): «những người sẽ đạt được "
        "con đường tối thượng ngay sau tâm này»; with tassa cittassa <moment>: «vào khoảnh khắc … của tâm mà ngay sau đó "
        "sẽ đạt được con đường tối thượng» (coordinator: smooth, not «Vào tâm mà ngay sau đó …»). 6-01 should align.",
        "- B.verb() raises on plural -ntīti (two readings); this module's verb() deduplicates (2-01 itself never meets it).",
        "",
        "## Pāli as written (reported)",
        "",
        "- ^6-9-71, ^6-9-76, ^6-9-81, ^6-9-86, ^6-9-91, ^6-9-96: unlabelled «Yattha …ti?…Pe….»: the question is kept "
        "whole («… không?») and the cut follows it («không?…»).",
        "- ^6-9-16: «(Kha) niddeso» stands as the last line of the segment, not as a heading: kept as a line «(b) Phần giải thích».",
        "- ^6-9-4-0 / ^6-9-5-0: headings «3 Suddhadhammavāro», «4 Suddhadhammamūlacakkavāro» keep their number.",
        "- ^6-9-98: «Uppādavāro.» (no niṭṭhito) = «Mục về sự sinh khởi.».",
        "- ^6-9-43: the (Kha) answer begins «Arūpe kusalānaṃ uppādakkhaṇe …»; ^6-9-55 «Suddhāvāsaṃ upapajjantānaṃ» "
        "(accusative plane): translated as written.",
        "",
    ]
    return "\n".join(out)


def main():
    S.check_reused()
    B.check_reused()
    check_reused()
    check_shared()
    segs = build()
    S.write(CHAPTER, segs)
    ADH_DIR.mkdir(exist_ok=True)
    (ADH_DIR / CHAPTER).write_bytes((S.OUT_DIR / CHAPTER).read_bytes())
    print("wrote", ADH_DIR / CHAPTER)
    NOTES_MD.write_text(unicodedata.normalize("NFC", notes()), encoding="utf-8", newline="\n")
    print("wrote", NOTES_MD)


if __name__ == "__main__":
    main()
