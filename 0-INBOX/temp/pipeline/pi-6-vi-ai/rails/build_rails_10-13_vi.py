"""pi-6 Yamaka, Vietnamese plain RAILS: chapter 10-13 (Indriyayamaka, last part: the pariññāvāra) and the book's end.

Family E (pariññāvāra) from build_rails_2-02_vi (setter), unchanged: E.e_question / E.e_line / E.e_sentence with the
Indriya members (build_rails_10-01_vi INDRIYA) as objects and four verbs, all built by E.make_verbs (the family-B
tense rule): parijānāti (E.E_VERBS), pajahati (build_rails_5-03_vi PAJ_VERBS), and two verbs new in the Yamaka:
bhāveti «tu tập» and sacchikaroti «tự mình chứng nghiệm» (termbase; pi-5 «tu tập con đường», «tự mình chứng nghiệm»).
Persons: E.PERSONS.extended(...) with this chapter's heads; strings from 7-01 / 7-03 / 7-06 (hai / ba / bốn hạng
người, Anāgāmī, Aṭṭhamako, Anāgāmimaggasamaṅgī, «… người có được con đường») and pi-4 (năm … tám hạng người).

Imports (all READ-ONLY; importing writes nothing, outputs are written only under `if __name__ == "__main__":`):
  S   build_rails_sample_vi   labels, «…», checks, BOOK_END, yamaka_end
  E   build_rails_2-02_vi     family E setter
  I   build_rails_10-01_vi    Indriya members, ind_mulaka, heading
  B   build_rails_2-01_vi     parse_variant, join_and, denied_vi
  C   build_rails_7-01_vi     PERSON_GEN, write()
  T3  build_rails_7-03_vi     PERSON_NOM (Anāgāmī)
  R6  build_rails_7-06_vi     Anāgāmimaggasamaṅgī, Aṭṭhamako, «người có được con đường», «hạng người»
  R7  build_rails_7-07_vi     Verb frames (agreement check: PARIJ / PAJ)
  P53 build_rails_5-03_vi     PAJ_VERBS, AGGAPHALA

Exposed for later use: BHAVETI, SACCHIKAROTI, BHAV_VERBS, SACC_VERBS, VERBS_10, NUM_VI, num_persons, maggasamangi,
yo_head, ye_puthu_head, PERSONS_10, e_line10, line_vi, tr_line, build.
A line the parsers cannot place raises ValueError (no silent fallback).

usage: python -I -X utf8 -B build_rails_10-13_vi.py [--probe [--show]]
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

E = importlib.import_module("build_rails_2-02_vi")     # family E setter (READ-ONLY)
I = importlib.import_module("build_rails_10-01_vi")    # Indriya module (READ-ONLY)
B = importlib.import_module("build_rails_2-01_vi")     # families A / B (READ-ONLY)
C = importlib.import_module("build_rails_7-01_vi")     # family C, shared shapes (READ-ONLY)
T3 = importlib.import_module("build_rails_7-03_vi")    # nominative persons (READ-ONLY)
R6 = importlib.import_module("build_rails_7-06_vi")    # paṭiloma persons (READ-ONLY)
R7 = importlib.import_module("build_rails_7-07_vi")    # Verb frames (READ-ONLY)
P53 = importlib.import_module("build_rails_5-03_vi")   # pajahati table, aggaphala (READ-ONLY)

CH = "10-13-indriyayamaka.md"
N = "10-13"
NOTES_MD = RAILS_DIR / f"notes-rails-{N}.md"
ADH_DIR = RAILS_DIR / f"adh-{N}"
TERMBASE = S.ROOT / "AI_translation/vietnamese/pi-6-pali-vietnamese-termbase-plain.md"
cap = S.cap
M = I.INDRIYA
SEEN = []   # (block / line, what) reported in the notes

# ===============================================================================================================
# 1. Verbs (E.make_verbs: «V / không V», «đã V / chưa từng V», «sẽ V / sẽ không V»; after no ca E.denied)
# ===============================================================================================================
BHAVETI = "tu tập"                      # bhāveti / bhāventi (termbase; pi-5 «tu tập con đường»)
SACCHIKAROTI = "tự mình chứng nghiệm"   # sacchikaroti / sacchikaronti (termbase; pi-4 / pi-5)
BHAV_VERBS = E.make_verbs(BHAVETI, E.rows_na("bhāveti", "bhāventi", "bhāvittha", "bhāvessati", "bhāvessanti"))
SACC_VERBS = E.make_verbs(SACCHIKAROTI, E.rows_na("sacchikaroti", "sacchikaronti", "sacchikarittha",
                                                  "sacchikarissati", "sacchikarissanti"))
PAJ_VERBS = P53.PAJ_VERBS                # pajahati / nappajahati in every tense (5-03; = 7-05 / 7-06 «dứt bỏ»)
VERBS_10 = {**E.E_VERBS, **PAJ_VERBS, **BHAV_VERBS, **SACC_VERBS}
assert len(VERBS_10) == len(E.E_VERBS) + len(PAJ_VERBS) + len(BHAV_VERBS) + len(SACC_VERBS)

# ===============================================================================================================
# 2. Persons (heads of the answers)
# ===============================================================================================================
PUGGALA = R6.PUGGALA                     # puggalā «hạng người» (termbase)
NUM_VI = {"Dve": "hai", "Tayo": "ba", "Cattāro": "bốn", "Pañca": "năm", "Cha": "sáu", "Satta": "bảy", "Aṭṭha": "tám"}
MAGGASAMANGI = R6.MAGGASAMANGI           # maggasamaṅgino «người có được con đường» (termbase; 7-06)
ANAGAMIMAGGA = R6.ANAGAMIMAGGA           # Anāgāmimaggasamaṅgī «người có được con đường không trở lại» (7-06)
ATTHAMAKA = R6.PERSON_NOM["Aṭṭhamako"][0]   # «người thứ tám» (user: «Người thứ tám»)
ANAGAMI = T3.PERSON_NOM["Anāgāmī"][0]    # «bậc không trở lại» (7-03)
AGGAPHALA = P53.AGGAPHALA                # aggaphalaṃ «thành quả tối thượng» (termbase; 5-03)


def num_persons(num):                    # Dve puggalā «hai hạng người» (pi-4 / 7-01)
    return f"{NUM_VI[num]} {PUGGALA}"


def maggasamangi(num):                   # Dve maggasamaṅgino «hai người có được con đường» (7-06 Dvinnaṃ …)
    return f"{NUM_VI[num]} {MAGGASAMANGI}"


def yo_head(vp):
    """Yo <VP> so … «Người nào <VP>, thì người ấy …» (singular of 2-02's ye_head «Những người nào <VP>, thì những
    người ấy»; «người nào» / «người ấy» = the yo shell's words, C.Q_REL['yassa'])."""
    return f"{E.WHO} {vp}, {E.THEN} {E.THAT}"


def ye_puthu_head(vp):
    """Ye puthujjanā <VP> te … «Những người phàm phu nào <VP>, thì những người ấy …» (= the tail of 2-02's
    ye_ca_head «P và những người phàm phu nào <VP>, thì những người ấy»)."""
    return f"{E.PUTHUJJANA_PL} {E.REL} {vp}, {E.THEN} {E.TE}"


# heads that begin with a relative clause are replaced by a token before E.e_sentence (E.e_head reads "Ye … te"
# only with a bare verb phrase); the token is a registered nominative person
HEAD_TOKENS = {
    "Yo aggaphalaṃ sacchikaroti so": ("⟨yo-sacchikaroti⟩", yo_head(f"{SACCHIKAROTI} {AGGAPHALA}"), 1),
    "Yo aggaphalaṃ sacchākāsi so": ("⟨yo-sacchakasi⟩", yo_head(f"đã {SACCHIKAROTI} {AGGAPHALA}"), 1),
    "Ye puthujjanā maggaṃ paṭilabhissanti te": ("⟨ye-puthu-magga⟩", ye_puthu_head(E.MAGGAM_PATILABHISSANTI), 2),
    "Ye puthujjanā maggaṃ na paṭilabhissanti te": ("⟨ye-puthu-na-magga⟩",
                                                  ye_puthu_head(E.MAGGAM_NA_PATILABHISSANTI), 2),
}

PERSONS_10 = E.PERSONS.extended(
    nom={**{f"{n} puggalā": (num_persons(n), 2) for n in NUM_VI},
         "Tayo maggasamaṅgino": (maggasamangi("Tayo"), 2),
         "Anāgāmimaggasamaṅgī": (ANAGAMIMAGGA, 1),
         "Aṭṭhamako": (ATTHAMAKA, 1),
         "Anāgāmī": (ANAGAMI, 1),
         **{tok: (vi, n) for tok, vi, n in HEAD_TOKENS.values()}},
    acc={"Dve maggasamaṅgino": maggasamangi("Dve"),
         "Tayo maggasamaṅgino": maggasamangi("Tayo"),
         "Cattāro maggasamaṅgino": maggasamangi("Cattāro"),
         "Tayo maggasamaṅgino ca arahantañca": B.join_and([maggasamangi("Tayo"), E.ARAHA]),
         "Anāgāmimaggasamaṅgiṃ": ANAGAMIMAGGA,
         "Aṭṭhamakaṃ": ATTHAMAKA},
)

# ===============================================================================================================
# 3. Slips and punctuation (rendered as meant; each one must be used exactly once and is reported)
# ===============================================================================================================
FIXES = [   # (Pāli as written, Pāli as parsed, report)
    ("aññindriyañca bhavissanti domanassindriyañca pajahissanti",
     "aññindriyañca bhāvessanti domanassindriyañca pajahissanti",
     "^6-10-452 «bhavissanti» (will be) for «bhāvessanti» (will cultivate): spelling slip, rendered as meant"),
    ("Aggamaggasamaṅgī aññātāvindriyaṃ sacchikarissanti, no ca aññindriyaṃ bhāvessanti.",
     "Aggamaggasamaṅgī aññātāvindriyaṃ sacchikarissati, no ca aññindriyaṃ bhāvessati.",
     "^6-10-454 «Aggamaggasamaṅgī … sacchikarissanti, … bhāvessanti» (singular subject, plural verbs): the "
     "Vietnamese verb has no number; same wording"),
    ("Aggamaggasamaṅgī domanassindriyañca pajahittha cakkhundriyañca parijānanti.",
     "Aggamaggasamaṅgī domanassindriyañca pajahittha cakkhundriyañca parijānāti.",
     "^6-10-459 «Aggamaggasamaṅgī … parijānanti» (singular subject, plural verb): same wording"),
    ("no ca domanassindriyaṃ pajahanti anāgāmimaggasamaṅgi aññindriyañca bhāvessanti, domanassindriyañca pajahanti.",
     "no ca domanassindriyaṃ pajahanti. Anāgāmimaggasamaṅgī aññindriyañca bhāvessati domanassindriyañca pajahati.",
     "^6-10-468 «… pajahanti anāgāmimaggasamaṅgi aññindriyañca bhāvessanti, domanassindriyañca pajahanti.»: the "
     "full stop before the second sentence is missing (added, capital as meant); «anāgāmimaggasamaṅgi» short -i "
     "(termbase form) and plural verbs with a singular subject (same wording); the comma inside the both-frame is "
     "the frame's own «, cũng» (as 2-02)"),
    ("yo vā pana aññindriyaṃ bhāvessati. So anaññātaññassāmītindriyaṃ bhāvitthāti?",
     "yo vā pana aññindriyaṃ bhāvessati so anaññātaññassāmītindriyaṃ bhāvitthāti?",
     "^6-10-477 «(Kha) yo vā pana aññindriyaṃ bhāvessati. So …bhāvitthāti?»: stray full stop and capital inside the "
     "question; one question as meant"),
    ("so anaññātaññassāmītindriyaṃ na bhāvessatīti. Āmantā.",
     "so anaññātaññassāmītindriyaṃ na bhāvessatīti? Āmantā.",
     "^6-10-455 «(Ka) yo cakkhundriyaṃ na parijānissati so anaññātaññassāmītindriyaṃ na bhāvessatīti. Āmantā.»: "
     "the question ends with «.» in the Pāli; plainly a question (label, yo … so …ti): «… không?»"),
    ("so cakkhundriyaṃ na parijānissatīti.",
     "so cakkhundriyaṃ na parijānissatīti?",
     "^6-10-455 «(Kha) yo vā pana anaññātaññassāmītindriyaṃ na bhāvessati so cakkhundriyaṃ na parijānissatīti.»: "
     "the question ends with «.» in the Pāli; plainly a question: «… không?»"),
    ("domanassindriyaṃ nappajjahittha so", "domanassindriyaṃ nappajahittha so",
     "^6-10-480 «nappajjahittha» (double j) for «nappajahittha»: spelling slip, rendered as meant"),
    ("aññindriyaṃ bhāvessanti no ca domanassindriyaṃ pajahissanti,",
     "aññindriyaṃ bhāvessanti, no ca domanassindriyaṃ pajahissanti,",
     "^6-10-452 comma before «no ca» missing: added (coordinator rule)"),
    ("aññindriyaṃ bhāvessanti no ca anaññātaññassāmītindriyaṃ bhāvittha.",
     "aññindriyaṃ bhāvessanti, no ca anaññātaññassāmītindriyaṃ bhāvittha.",
     "^6-10-477 comma before «no ca» missing: added (coordinator rule)"),
]
# the first FIXES row is applied after the missing-comma row on the same line; order by line content
FIX_USED = {k: 0 for k, _, _ in FIXES}
# "…, pañca puggalā …" (^6-10-452): a comma, not a full stop, before the second answer sentence: kept as written
COMMA_JOIN_RE = re.compile(r", (?=(?:dve|tayo|cattāro|pañca|cha|satta|aṭṭha) puggalā )")

# variant brackets: Pāli → (kind, Vietnamese anchor before, anchor after); the bracket goes between the two
VARIANTS = {
    "[tayo puggalā (pī.)]": ("form", cap(maggasamangi("Tayo")), " "),
    "[aṭṭhamakañca tayo maggasamaṅgino ca (pī.)]": ("form", maggasamangi("Cattāro"), ","),
    "[satta (sī. syā. ka.)]": ("form", cap(NUM_VI["Aṭṭha"]), f" {PUGGALA}"),
    "[pañca (sī. syā. ka.)]": ("form", cap(NUM_VI["Cha"]), f" {PUGGALA}"),
}
VAR_RE = re.compile(r" (\[[^\]]+\])")


def fix_body(body):
    for old, new, why in FIXES:
        if old in body:
            if body.count(old) != 1:
                raise ValueError(f"fix {old!r} twice in {body!r}")
            body = body.replace(old, new)
            FIX_USED[old] += 1
            SEEN.append(why)
    return body


# ===============================================================================================================
# 4. Lines
# ===============================================================================================================
def tokenise(body):
    """Relative-clause heads at a sentence start → their registered tokens."""
    for k, (tok, _, _) in HEAD_TOKENS.items():
        body = re.sub(r"(^|(?<=\. ))" + re.escape(k) + r" ", lambda m: m.group(1) + tok + " ", body)
    return body


def e_line10(body):
    """A pariññāvāra line body → Vietnamese (E.e_line with this chapter's members, verbs and persons)."""
    out = E.e_line(body, M, VERBS_10, PERSONS_10)
    if out is None:
        raise ValueError(f"not a family-E line: {body!r}")
    return out


def line_vi(body):
    body = tokenise(body)
    if COMMA_JOIN_RE.search(body):          # "S1, pañca puggalā …" kept as one sentence with the Pāli's comma
        a, b = COMMA_JOIN_RE.split(body, maxsplit=1)
        if COMMA_JOIN_RE.search(b):
            raise ValueError(f"two comma joins in {body!r}")
        va = e_line10(a + ".")
        vb = e_line10(cap(b))
        assert va.endswith("."), va
        SEEN.append("^6-10-452 «…pajahissanti, pañca puggalā …»: comma (not «.») before the second answer "
                    "sentence; kept as written («…, năm hạng người …»)")
        return va[:-1] + ", " + vb[:1].lower() + vb[1:]
    return e_line10(body)


HEADINGS = dict(E.HEADINGS)              # Paccuppannavāro … Atītānāgatavāro (2-02)
FIXED = {
    "Pariññāvāro.": E.PARINNAVARO_CLOSE,                     # «Mục về sự hiểu biết trọn vẹn.» (2-02, 5-03)
    "Indriyayamakaṃ niṭṭhitaṃ.": S.yamaka_end(I.YAMAKA),     # «Phần các cặp câu hỏi về các năng lực đã hoàn tất.»
    "Yamakapakaraṇaṃ niṭṭhitaṃ.": S.BOOK_END,                 # «Bộ “Các cặp câu hỏi” đã hoàn tất.»
}
LABEL_RE = re.compile(r"(.+?) (\(\w+mūlakaṃ\)\.?)")


def heading(text):
    if text in HEADINGS:
        return HEADINGS[text]
    return I.heading(text)


def tr_line(p):
    m = re.search(r" (\^\S+)$", p)
    bid = m.group(1) if m else None
    body = p[:m.start()] if m else p
    if body.startswith("#"):
        hashes, text = body.split(" ", 1)
        out = f"{hashes} {heading(text)}"
    elif body in FIXED:
        out = FIXED[body]
    else:
        label = None
        if mm := LABEL_RE.fullmatch(body):
            body, label = mm.group(1), mm.group(2)
        body = fix_body(body)
        brs = VAR_RE.findall(body)
        body = VAR_RE.sub("", body)
        out = line_vi(body)
        for br in brs:
            if br not in VARIANTS:
                raise ValueError(f"undeclared variant {br!r}")
            kind, before, after = VARIANTS[br]
            anchor = before + after
            if out.count(anchor) != 1:
                raise ValueError(f"variant anchor {anchor!r} found {out.count(anchor)} times in {out!r}")
            out = out.replace(anchor, f"{before} {B.parse_variant(br, kind)}{after}")
        if label:
            lab = I.ind_mulaka(label)
            if lab is None:
                raise ValueError(f"unknown label {label!r}")
            out += " " + lab
    if "⟨" in out or "⟩" in out:
        raise ValueError(f"unplaced token in {out!r}")
    return f"{out} {bid}" if bid else out


def build(name=CH):
    segs = []
    for seg in S.segments_of(name):
        out = []
        for ln in seg:
            try:
                out.append(tr_line(ln))
            except (ValueError, KeyError) as e:
                raise ValueError(f"{name}: cannot place line {ln[:160]!r}: {e!r}") from None
        segs.append(out)
    return segs


def probe(name=CH):
    bad = 0
    for seg in S.segments_of(name):
        for ln in seg:
            try:
                v = tr_line(ln)
                if "--show" in sys.argv:
                    print("PI:", ln, "\nVI:", v, "\n")
            except (ValueError, KeyError, AssertionError) as e:
                bad += 1
                print("FAIL:", repr(e)[:400], "\n   ", ln[:220])
    print("failing lines:", bad)


# ===============================================================================================================
# 5. Assertions
# ===============================================================================================================
TERMBASE_USED = [
    ("bhāveti", BHAVETI), ("bhāvetīti", BHAVETI), ("bhāventi", BHAVETI), ("bhāvittha", "đã " + BHAVETI),
    ("bhāvitthāti", "đã " + BHAVETI), ("bhāvessati", "sẽ " + BHAVETI), ("bhāvessatīti", "sẽ " + BHAVETI),
    ("bhāvessanti", "sẽ " + BHAVETI),
    ("sacchikaroti", SACCHIKAROTI), ("sacchikarotīti", SACCHIKAROTI), ("sacchikaronti", SACCHIKAROTI),
    ("sacchikarittha", "đã " + SACCHIKAROTI), ("sacchikaritthāti", "đã " + SACCHIKAROTI),
    ("sacchākāsi", "đã " + SACCHIKAROTI), ("sacchikarissati", "sẽ " + SACCHIKAROTI),
    ("sacchikarissatīti", "sẽ " + SACCHIKAROTI), ("sacchikarissanti", "sẽ " + SACCHIKAROTI),
    ("pajahati", "dứt bỏ"), ("pajahatīti", "dứt bỏ"), ("pajahanti", "dứt bỏ"), ("nappajahati", "không dứt bỏ"),
    ("nappajahanti", "không dứt bỏ"), ("pajahittha", "đã dứt bỏ"), ("nappajahittha", "chưa từng dứt bỏ"),
    ("pajahissati", "sẽ dứt bỏ"), ("pajahissanti", "sẽ dứt bỏ"), ("nappajahissati", "sẽ không dứt bỏ"),
    ("nappajahissanti", "sẽ không dứt bỏ"),
    ("parijānāti", E.PARIJANATI), ("parijānanti", E.PARIJANATI), ("parijānittha", "đã " + E.PARIJANATI),
    ("parijānissati", "sẽ " + E.PARIJANATI), ("parijānissanti", "sẽ " + E.PARIJANATI),
    ("cakkhundriyaṃ", I.IND_NAME["cakkhu"]), ("domanassindriyaṃ", I.IND_NAME["domanassa"]),
    ("anaññātaññassāmītindriyaṃ", I.IND_NAME["anaññātaññassāmīti"]), ("aññindriyaṃ", I.IND_NAME["añña"]),
    ("aññātāvindriyaṃ", I.IND_NAME["aññātāvī"]),
    ("puggalā", PUGGALA), ("maggasamaṅgino", MAGGASAMANGI), ("Aggamaggasamaṅgī", E.AGGAMAGGASAMANGI),
    ("Aggamaggasamaṅgiñca", E.AGGAMAGGASAMANGI), ("Anāgāmimaggasamaṅgī", ANAGAMIMAGGA),
    ("Anāgāmimaggasamaṅgiñca", ANAGAMIMAGGA), ("anāgāmimaggasamaṅgi", ANAGAMIMAGGA), ("Aṭṭhamako", ATTHAMAKA),
    ("Anāgāmī", ANAGAMI), ("Arahā", E.ARAHA), ("arahantañca", E.ARAHA), ("aggaphalaṃ", AGGAPHALA),
    ("puthujjanā", "người phàm phu"), ("paṭilabhissanti", "sẽ đạt được"), ("Pariññāvāro", "mục về sự hiểu biết trọn vẹn"),
    ("Indriyayamakaṃ", "Các cặp câu hỏi về các năng lực"), ("Yamakapakaraṇaṃ", "Bộ “Các cặp câu hỏi”"),
    ("Cakkhundriyamūlakaṃ", "phần dựa trên năng lực mắt"), ("Domanassindriyamūlakaṃ", "phần dựa trên năng lực nỗi buồn"),
    ("Anaññātaññassāmītindriyamūlakaṃ", "phần dựa trên năng lực biết được điều chưa từng biết"),
    ("Aññindriyamūlakaṃ", "phần dựa trên năng lực hiểu biết trọn vẹn"),
]
REUSED = [   # (Pāli, Vietnamese, book): asserted to occur in that book's approved Vietnamese rails
    ("Pañca puggalā – (pi-4 1-matika)", "Năm hạng người", "4"),
    ("Cha puggalā –", "Sáu hạng người", "4"),
    ("Satta puggalā –", "Bảy hạng người", "4"),
    ("Aṭṭha puggalā –", "Tám hạng người", "4"),
    ("Dve / Tayo / Cattāro puggalā –", "Hai hạng người", "4"),
    ("maggaṃ bhāveti (pi-5 12-catutthavaggo)", f"{BHAVETI} con đường", "5"),
    ("nirodhaṃ sacchikaroti (pi-5 12-catutthavaggo)", SACCHIKAROTI, "5"),
    ("sotāpattiphalaṃ sacchikaroti (pi-4)", f"{SACCHIKAROTI} thành quả", "4"),
]


def check_assertions():
    tb = TERMBASE.read_text(encoding="utf-8")
    bad = [(p, v) for p, v in TERMBASE_USED
           if not re.search(r"^" + re.escape(p) + r": \{[^\n]*: " + re.escape(v) + r"[};]", tb, re.M | re.I)]
    assert not bad, "termbase strings not found: " + repr(bad)
    texts = {b: unicodedata.normalize("NFC", "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md"))))
             for b, d in S.RAILS.items()}
    bad = [(p, v, b) for p, v, b in REUSED if unicodedata.normalize("NFC", v) not in texts[b]]
    assert not bad, "reused strings not found in their rails: " + repr(bad)
    # verbs: the family-E tense rule; pajahati / parijānāti agree with 7-07's Verb frames and 5-03
    for v in (BHAV_VERBS, SACC_VERBS):
        for f, ev in v.items():
            assert ev.vi in (ev.pos_vi, ev.neg_vi)
    assert BHAV_VERBS["na bhāvittha"].vi == f"chưa từng {BHAVETI}"
    assert E.denied(BHAV_VERBS["na bhāveti"]) == f"vẫn {BHAVETI}"
    assert E.denied(SACC_VERBS["na sacchikarittha"]) == f"đã từng {SACCHIKAROTI}"
    assert E.denied(SACC_VERBS["na sacchikarissati"]) == f"vẫn sẽ {SACCHIKAROTI}"
    assert R7.PARIJ.pos == E.E_VERBS["parijānāti"].vi and R7.PARIJ.still == E.denied(E.E_VERBS["na parijānāti"])
    assert R7.PAJ.pos == PAJ_VERBS["pajahati"].vi and R7.PAJ.neg == PAJ_VERBS["nappajahati"].vi
    assert R7.PAJ.still == E.denied(PAJ_VERBS["nappajahati"]) == "vẫn dứt bỏ"
    # persons: strings of 7-01 / 7-03 / 7-06 / 2-02
    for n, g in (("Dve", "Dvinnaṃ puggalānaṃ"), ("Tayo", "Tiṇṇaṃ puggalānaṃ"), ("Cattāro", "Catunnaṃ puggalānaṃ")):
        assert num_persons(n) == C.PERSON_GEN[g][0], n
    assert maggasamangi("Dve") == R6.EXC_PERSON["dvinnaṃ maggasamaṅgīna"]
    assert PERSONS_10.acc["Aggamaggasamaṅgiṃ"] == R6.EXC_PERSON["aggamaggasamaṅgi"]
    assert E.except_head([PERSONS_10.acc["Tayo maggasamaṅgino ca arahantañca"]]) == \
        E.except_head([maggasamangi("Tayo"), E.ARAHA])
    assert E.except_head([maggasamangi("Dve")]) == f"{R6.EXCEPT} {maggasamangi('Dve')}, {R6.REST_PERSONS}"
    assert E.ye_ca_head("X", E.PUTHUJJANA_PL, E.MAGGAM_NA_PATILABHISSANTI) == \
        f"X {E.AND} {ye_puthu_head(E.MAGGAM_NA_PATILABHISSANTI)}"
    assert E.ye_head("Y") == f"{B.YE} Y, {E.THEN} {E.TE}" and yo_head("Y") == f"{E.WHO} Y, {E.THEN} {E.THAT}"
    assert (E.WHO, E.THAT) == C.Q_REL["yassa"]
    # headings, labels, closers
    assert heading("(Ka) anulomaṃ") == "(a) Chiều thuận" and heading("(Kha) paccanīkaṃ") == "(b) Chiều nghịch"
    assert heading("Paccuppannātītavāro") == "Mục về hiện tại và quá khứ"
    assert I.ind_mulaka("(Aññindriyamūlakaṃ).") == "(Phần dựa trên năng lực hiểu biết trọn vẹn)."
    assert FIXED["Indriyayamakaṃ niṭṭhitaṃ."] == "Phần các cặp câu hỏi về các năng lực đã hoàn tất."
    assert FIXED["Yamakapakaraṇaṃ niṭṭhitaṃ."] == "Bộ “Các cặp câu hỏi” đã hoàn tất."
    # the 2-02 frames with this chapter's members (one sample per frame)
    a, d = I.IND_NAME["cakkhu"], I.IND_NAME["domanassa"]
    assert e_line10("Arahā cakkhundriyaṃ na parijānāti, no ca domanassindriyaṃ nappajahittha.") == \
        E.e_noca(cap(E.ARAHA), a, "không hiểu biết trọn vẹn", f"đã từng dứt bỏ {d}") + ""
    # parsers still raise on unknown words / shapes
    for bad_s in ("Arahā cakkhundriyaṃ bhāventi.", "Nava puggalā cakkhundriyaṃ bhāventi.",
                  "Aṭṭhamako cakkhundriyañca bhāveti."):
        try:
            e_line10(bad_s)
        except ValueError:
            continue
        raise AssertionError(f"no error on {bad_s!r}")


# ===============================================================================================================
# 6. Notes file (Pāli = tiếng Việt)
# ===============================================================================================================
def notes():
    out = [f"# pi-6 rails {N} (Indriyayamaka, last part): pariññāvāra with four verbs; end of the book", "",
           "Builder: build_rails_10-13_vi.py. Imports READ-ONLY: build_rails_2-02_vi (family E setter: e_line / "
           "e_sentence / yo_q / make_verbs / rows_na / Persons), build_rails_10-01_vi (INDRIYA members, ind_mulaka, "
           "heading), build_rails_5-03_vi (PAJ_VERBS, AGGAPHALA), build_rails_7-06_vi / 7-03 / 7-01 (persons), "
           "build_rails_7-07_vi (Verb agreement check), build_rails_2-01_vi (parse_variant, join_and) and the sample "
           "builder (yamaka_end, BOOK_END). Exposed: BHAVETI, SACCHIKAROTI, BHAV_VERBS, SACC_VERBS, VERBS_10, NUM_VI, "
           "num_persons, maggasamangi, yo_head, ye_puthu_head, PERSONS_10, e_line10. Format: Pāli = tiếng Việt.", ""]

    def h(t):
        out.extend(["", f"## {t}", ""])

    def row(p, v):
        out.append(f"{p} = {v}")

    h("Verbs new in the Yamaka (termbase; family-E tense rule; after no ca E.denied)")
    for table in (BHAV_VERBS, SACC_VERBS):
        for f, v in table.items():
            row(f, v.vi)
    row("sacchākāsi (aorist, in the head «Yo aggaphalaṃ sacchākāsi so»)", f"đã {SACCHIKAROTI}")
    row("no ca … na bhāveti / na bhāvittha / na bhāvessati (denied)",
        " / ".join(E.denied(BHAV_VERBS[f]) for f in ("na bhāveti", "na bhāvittha", "na bhāvessati")))
    row("no ca … na sacchikaroti / na sacchikarittha / na sacchikarissati (denied)",
        " / ".join(E.denied(SACC_VERBS[f]) for f in ("na sacchikaroti", "na sacchikarittha", "na sacchikarissati")))
    row("no ca … bhāveti / bhāvittha / bhāvessati (positive: its negative)",
        " / ".join(E.denied(BHAV_VERBS[f]) for f in ("bhāveti", "bhāvittha", "bhāvessati")))
    h("Answer heads (nominative persons; registered in PERSONS_10)")
    for n in NUM_VI:
        row(f"{n} puggalā …", cap(num_persons(n)) + " …")
    row("Tayo maggasamaṅgino … (nominative)", cap(maggasamangi("Tayo")) + " …")
    for k in ("Anāgāmimaggasamaṅgī", "Aṭṭhamako", "Anāgāmī", "Aggamaggasamaṅgī", "Arahā"):
        row(f"{k} …", cap(PERSONS_10.nom[k][0]) + " …")
    for k, (_, vi, _) in HEAD_TOKENS.items():
        row(f"{k} …", cap(vi) + " …")
    for k in ("Dve maggasamaṅgino", "Tayo maggasamaṅgino", "Cattāro maggasamaṅgino",
              "Tayo maggasamaṅgino ca arahantañca"):
        row(f"{k} ṭhapetvā avasesā puggalā …", E.except_head([PERSONS_10.acc[k]]) + " …")
    for k in ("Aggamaggasamaṅgiñca arahantañca", "Anāgāmimaggasamaṅgiñca arahantañca", "Aṭṭhamakañca arahantañca"):
        row(f"{k} ṭhapetvā avasesā puggalā …", E.e_head(f"{k} ṭhapetvā avasesā puggalā x", PERSONS_10)[0] + " …")
    h("Examples (built by the module)")
    for s in ("(Ka) yo cakkhundriyaṃ parijānāti so domanassindriyaṃ pajahatīti? No.",
              "(Kha) yo vā pana aññātāvindriyaṃ na sacchikarittha so cakkhundriyaṃ na parijānitthāti?",
              "Dve puggalā aññindriyaṃ bhāventi, no ca cakkhundriyaṃ parijānanti. Aggamaggasamaṅgī aññindriyañca "
              "bhāveti cakkhundriyañca parijānāti.",
              "Aṭṭhamako cakkhundriyaṃ na parijānāti, no ca anaññātaññassāmītindriyaṃ na bhāveti. Dve maggasamaṅgino "
              "ṭhapetvā avasesā puggalā cakkhundriyañca na parijānanti anaññātaññassāmītindriyañca na bhāventi.",
              "Yo aggaphalaṃ sacchikaroti so cakkhundriyaṃ parijānittha, no ca aññātāvindriyaṃ sacchikarittha. Yo "
              "aggaphalaṃ sacchākāsi so cakkhundriyañca parijānittha aññātāvindriyañca sacchikarittha.",
              "Ye puthujjanā maggaṃ paṭilabhissanti te cakkhundriyaṃ na parijānanti, no ca "
              "anaññātaññassāmītindriyaṃ na bhāvessanti.",
              "Arahā aññātāvindriyaṃ na sacchikarissati, no ca cakkhundriyaṃ na parijānittha. Ye puthujjanā maggaṃ na "
              "paṭilabhissanti te aññātāvindriyañca na sacchikarissanti cakkhundriyañca na parijānittha."):
        row(s, line_vi(s))
    h("Variants, labels, closers")
    for br, (kind, before, after) in VARIANTS.items():
        row(br, f"{before} {B.parse_variant(br, kind)}{after}  (placed after the word it follows)")
    row("(Cakkhundriyamūlakaṃ) … (Aññindriyamūlakaṃ).", f"{I.ind_mulaka('(Cakkhundriyamūlakaṃ)')} … "
        f"{I.ind_mulaka('(Aññindriyamūlakaṃ).')}")
    for k, v in FIXED.items():
        row(k, v)
    h("Termbase misfits and gaps (for the coordinator)")
    out += [
        "- Numerals with puggalā (Pañca / Cha / Satta / Aṭṭha puggalā): no pi-6 headword; pi-4 «Năm / Sáu / Bảy / Tám "
        "hạng người» (asserted); Dve / Tayo / Cattāro = 7-01 / 7-03 «hai / ba / bốn hạng người».",
        "- Dve / Tayo / Cattāro maggasamaṅgino (accusative after ṭhapetvā; Tayo also nominative): «hai / ba / bốn người "
        "có được con đường» (termbase maggasamaṅgino; = 7-06 «hai người có được con đường» for Dvinnaṃ "
        "maggasamaṅgīnaṃ). pi-4 «Bốn hạng người có được con đường» renders «cattāro maggasamaṅgino puggalā» (with "
        "puggalā), so «hạng» is not added here.",
        "- Yo aggaphalaṃ sacchikaroti so / sacchākāsi so: no setter shape; the singular of 2-02's ye_head: «Người nào "
        "(đã) tự mình chứng nghiệm thành quả tối thượng, thì người ấy …».",
        "- Ye puthujjanā maggaṃ (na) paṭilabhissanti te: «Những người phàm phu nào sẽ (không) đạt được con đường, thì "
        "những người ấy …» (= 2-02's «… và những người phàm phu nào …» without the first person).",
        "- aññindriyaṃ «năng lực hiểu biết trọn vẹn» (termbase) sits next to parijānāti «hiểu biết trọn vẹn» in the "
        "same sentences («tu tập năng lực hiểu biết trọn vẹn, nhưng không hiểu biết trọn vẹn năng lực mắt»): both "
        "locked, kept; the reader may find the echo heavy.",
        "",
        "## Slips and punctuation (rendered as meant or as written; reported)",
        "",
    ]
    out += [f"- {x}" for x in dict.fromkeys(SEEN)]
    out += ["- ^6-10-442 (twice) «Tayo maggasamaṅgino ca arahantañca ṭhapetvā»: the first item has «ca» without "
            "«-ñca» on the noun; one list «Ngoại trừ ba người có được con đường và bậc A-la-hán, …».",
            "- ^6-10-482 «(Aññindriyamūlakaṃ).» with the Pāli's final «.» (kept).", ""]
    return "\n".join(out)


def main():
    if "--probe" in sys.argv:
        probe()
        return
    S.check_reused()
    B.check_reused()
    check_assertions()
    del SEEN[:]
    for k in FIX_USED:
        FIX_USED[k] = 0
    segs = build(CH)
    unused = [k for k, n in FIX_USED.items() if n != 1]
    assert not unused, f"fixes not used exactly once: {unused}"
    C.write(CH, segs, extra_dirs=(ADH_DIR,))
    NOTES_MD.write_text(unicodedata.normalize("NFC", notes()), encoding="utf-8", newline="\n")
    print("wrote", NOTES_MD)
    for x in dict.fromkeys(SEEN):
        print("reported:", x[:150])


if __name__ == "__main__":
    main()
