"""pi-6 Yamaka, Vietnamese plain RAILS: chapter 5-02 (Saccayamaka, part 2: pavattivāra nirodhavāra + the start of the
uppādanirodhavāra).

Everything comes from the Saccayamaka module build_rails_5-01_vi (members, verbs, questions, answer heads, answer
frames, cut lines, headings) and, through it, 2-01 (families A, B), 7-01 (answer shapes), 8 (moments, kinds of mind),
2-02 (cuts, ye heads) and 9-01 (shared head parts); 9-02 for Pacchimacittassa bhaṅgakkhaṇe and 3-01 for
asammohantena. All are imported READ-ONLY (nothing in them is changed).

5-01's head parser has no entry for Pacchimacittassa: this file loads a PRIVATE second instance of build_rails_5-01_vi
(`TP`, its own module object; the shared module `T` and its dicts stay untouched) and gives that instance's own
MIND_KIND the one extra kind «tâm cuối cùng» (8's mind_gen_vi; = 9-02). The builder asserts that its translator
reproduces the 5-01 chapter byte for byte, so every string shared with 5-01 is 5-01's.

New here (exposed for 5-03): `FINAL_MIND`, `NOTES` (editorial notes), `VARIANTS`, `cut_answer` (an answer cut by
…pe… before its full stop), `cut_no_q` ("(Kha) yassa vā pana…pe…." without «?»), `yy_cut` ("Yassa yattha A V…pe…."),
`piece`, `chunk_vi`, `line_vi`, `tr_line`, `build`. A line the parsers cannot place raises ValueError.

usage: python -I -X utf8 -B build_rails_5-02_vi.py [--probe]
"""
import importlib
import importlib.util
import pathlib
import re
import sys
import unicodedata

RAILS_DIR = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai\rails")
if str(RAILS_DIR) not in sys.path:
    sys.path.insert(0, str(RAILS_DIR))
import build_rails_sample_vi as S  # noqa: E402  (READ-ONLY)
T = importlib.import_module("build_rails_5-01_vi")    # Saccayamaka module (READ-ONLY, shared)
B, C, D, E, T9 = T.B, T.C, T.D, T.E, T.T9               # 2-01, 7-01, 8, 2-02, 9-01 (READ-ONLY, the same objects)
DY2 = importlib.import_module("build_rails_9-02_vi")  # READ-ONLY: Pacchimacittassa bhaṅgakkhaṇe (9-02)
A3 = importlib.import_module("build_rails_3-01_vi")   # READ-ONLY: asammohantena (3-01)


def _private_5_01():
    """A second, private instance of build_rails_5-01_vi (own module object, own dicts)."""
    spec = importlib.util.spec_from_file_location("build_rails_5_01_private_for_5_02",
                                                  RAILS_DIR / "build_rails_5-01_vi.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


TP = _private_5_01()
FINAL_MIND = D.mind_gen_vi("Pacchimacittassa")        # «tâm cuối cùng» (8; termbase; = 9-02 gen_vi)
TP.MIND_KIND = {**TP.MIND_KIND, "pacchima": FINAL_MIND}   # the private instance only
assert "pacchima" not in T.MIND_KIND

CH = "5-02-saccayamaka.md"
N = "5-02"
NOTES_MD = RAILS_DIR / f"notes-rails-{N}.md"
ADH_DIR = RAILS_DIR / f"adh-{N}"
cap = S.cap
LABEL = S.LABEL
PE = S.PE
M = TP.SACCA_B

SLIPS = []   # (what, where) found by this file; TP.SLIPS_SEEN holds those found by 5-01's parsers


def _decap(s):
    return s[:1].lower() + s[1:]


# ===============================================================================================================
# 1. Editorial notes (termbase: yatthakaṃ «phần về nơi chốn», Yassakampi «phần về người», yassayatthakampi /
#    yassayatthakepi «phần về người và nơi chốn», uppādepi «sự sinh khởi», nirodhepi «sự chấm dứt», uppādanirodhepi
#    «sự sinh khởi và sự chấm dứt», uppādavāre(pi) / nirodhavārepi / uppādanirodhavārepi «mục về …», pucchā «câu hỏi»,
#    anulomampi «chiều thuận», paccanīkampi «chiều nghịch», nirodhasamāpannānanti «người nhập thành tựu thiền chấm
#    dứt», Natthi «không có»; pi-5 nānākaraṇaṃ «sự khác biệt»; pi-2 / 2-02 «như đã được phân tích trong …, … cũng
#    nên phân tích như vậy»; 5-01 «Cả … lẫn … đều … giống nhau», «nên được trình bày chi tiết»; 2-02 kātabbaṃ «nên được
#    trình bày»; 3-01 asammohantena «mà không mê lầm», the -pi … -pi lists «ở …, ở …»; 2-01 TIME)
# ===============================================================================================================
P_PERSON, P_PLACE, P_PERSON_PLACE = T.P_PERSON, T.P_PLACE, T.P_PERSON_PLACE
SADISA = "giống nhau"                                     # sadisaṃ (5-01 / 3-01 / 3-02)
NANAKARANA = "sự khác biệt"                               # nānākaraṇaṃ (pi-5; 5-01)
NATTHI_NANA = f"{_decap(C.ANS_NATTHI[:-1])} {NANAKARANA}"  # natthi nānākaraṇaṃ «không có sự khác biệt»
UPPADE, NIRODHE, UPPADANIRODHE = "sự sinh khởi", "sự chấm dứt", "sự sinh khởi và sự chấm dứt"   # -epi (termbase)
VIBHATTA = "như đã được phân tích trong"                  # yathā … vibhattā (pi-2; 2-02 YATHA_IDHA)
VIBHAJITABBA = "cũng nên phân tích như vậy"               # evaṃ … vibhajitabbā / -aṃ (pi-2; 2-02 YATHA_IDHA)
assert f"{VIBHATTA} {B.UPPADAVARO}, ở đây {VIBHAJITABBA}" in E.YATHA_IDHA
ATITA_PUCCHA = "Các câu hỏi về quá khứ"                   # atītā pucchā (pucchā «câu hỏi»; 2-01 TIME «quá khứ»)
PACC_ATITA_PUCCHA = f"Các câu hỏi về {B.TIME['Paccuppannātīta']}"   # Paccuppannaatītā pucchā
ANU_PACC = f"cả {B.ORDER['anuloma'].lower()} lẫn {B.ORDER['paccanīka'].lower()}"   # anulomampi paccanīkampi
NIRODHA_SAMAPANNA_Q = f"“{D.PERSON['nirodhasamāpannānaṃ']}”"   # nirodhasamāpannānanti (quoted word of the text)
NA_KATABBAM = "cũng không nên trình bày"                 # (-pi …) na kātabbaṃ (2-02 kātabbaṃ «nên được trình bày»)
ASAMMOHANTENA = A3.ASAMMOHANTENA                          # «mà không mê lầm» (coordinator; 3-01), after the verb
assert ASAMMOHANTENA == "mà không mê lầm"
BOTH_YY = f"Cả {P_PERSON} lẫn {P_PERSON_PLACE} đều {SADISA}"   # Yassakampi yassayatthakampi sadisaṃ (5-01 shape)
assert T.NOTE_YASSAKA.startswith(f"(Cả {P_PERSON} lẫn {P_PERSON_PLACE} đều ")

# ^6-5-152: the answer quoted inside the note (built by 5-01's answer parser; the comma inside the head absorbed)
_N152_PALI = ("aggamaggassa bhaṅgakkhaṇe, arahantānaṃ asaññasattānaṃ tesaṃ tattha maggasaccañca na nirujjhissati "
              "samudayasaccañca nuppajjissati")
N152_ANSWER = _decap(TP.b_sentence(cap(_N152_PALI) + ".")[:-1])

NOTES = {   # Pāli (variants protected as ⟦k⟧) → Vietnamese
    "(Yatthakaṃ uppādepi nirodhepi uppādanirodhepi sadisaṃ, natthi nānākaraṇaṃ).":
        f"({cap(P_PLACE)} ở {UPPADE}, ở {NIRODHE}, ở {UPPADANIRODHE} đều {SADISA}, {NATTHI_NANA}).",
    "(Yassayatthakampi sadisaṃ vitthāretabbaṃ).":
        f"({cap(P_PERSON_PLACE)} cũng {T.VITTHARETABBAM} {SADISA}).",
    "(Yassakampi ⟦0⟧ yassayatthakampi sadisaṃ, yassayatthakepi nirodhasamāpannānanti cetaṃ na kātabbaṃ).":
        f"(Cả {P_PERSON} ⟦0⟧ lẫn {P_PERSON_PLACE} đều {SADISA}, {C.AND} ở {P_PERSON_PLACE} {NA_KATABBAM} "
        f"điều này: {NIRODHA_SAMAPANNA_Q}).",
    "(Yathā uppādavāre atītā pucchā anulomampi paccanīkampi vibhattā evaṃ nirodhepi vibhajitabbā, "
    "natthi nānākaraṇaṃ).":
        f"({ATITA_PUCCHA}, {ANU_PACC}, {VIBHATTA} {B.UPPADAVARO}, ở {NIRODHE} {VIBHAJITABBA}, {NATTHI_NANA}).",
    "(Yassakampi yassayatthakampi sadisaṃ).": f"({BOTH_YY}).",
    "(Yatthakaṃ uppādavārepi nirodhavārepi uppādanirodhavārepi sadisaṃ natthi nānākaraṇaṃ).":
        f"({cap(P_PLACE)} ở {B.UPPADAVARO}, ở {B.NIRODHAVARO}, ở {B.UPPADANIRODHAVARO} đều {SADISA}, "
        f"{NATTHI_NANA}).",
    "(Yassakampi yassayatthakampi sadisaṃ, yassayatthakepi nirodhasamāpannānanti na kātabbaṃ).":
        f"({BOTH_YY}, ở {P_PERSON_PLACE} {NA_KATABBAM} {NIRODHA_SAMAPANNA_Q}).",
    "(Atītā pucchā yathā uppādavāre vibhattā evaṃ uppādanirodhavārepi anulomampi paccanīkampi vibhajitabbaṃ).":
        f"({ATITA_PUCCHA} {VIBHATTA} {B.UPPADAVARO}, ở {B.UPPADANIRODHAVARO} {VIBHAJITABBA}, {ANU_PACC}).",
    "(Yassakampi yassayatthakampi sadisaṃ, samudayasaccaṃ maggasaccaṃ nānākaraṇaṃ, " + _N152_PALI + ").":
        f"({BOTH_YY}, {T.TRUTH['samudayasacca']} {C.AND} {T.TRUTH['maggasacca']} có {NANAKARANA}, {N152_ANSWER}).",
    "(Paccuppannaatītā ⟦0⟧ pucchā uppādavārepi uppādanirodhavārepi yassakampi yatthakampi yassayatthakampi "
    "anulomampi paccanīkampi sadisaṃ, asammohantena vibhajitabbā).":
        f"({PACC_ATITA_PUCCHA} ⟦0⟧ ở cả {B.UPPADAVARO} lẫn {B.UPPADANIRODHAVARO}, ở cả {P_PERSON}, {P_PLACE} lẫn "
        f"{P_PERSON_PLACE}, ở {ANU_PACC} đều {SADISA}, nên phân tích {ASAMMOHANTENA}).",
}
NIRODHAVARO_CLOSE = cap(B.NIRODHAVARO) + "."             # Nirodhavāro. «Mục về sự chấm dứt.»
assert NIRODHAVARO_CLOSE == T9.SECTION_END["Nirodhavāro."]

# ===============================================================================================================
# 2. Variant brackets (5-01's, plus this chapter's)
# ===============================================================================================================
VARIANTS = dict(T.VARIANTS) | {
    "[paṭilabhissanti tassa cittassa uppādakkhaṇe (sī. syā.) uppādavāre pana pāṭhantaraṃ natthi]":
        S.var(T._sig("sī. syā."), f"paṭilabhissanti tassa cittassa uppādakkhaṇe, còn ở {B.UPPADAVARO} thì "
                                  f"{_decap(C.ANS_NATTHI[:-1])} dị bản"),
    "[yassakampi yatthakampi (sī. syā.)]": B.parse_variant("[yassakampi yatthakampi (sī. syā.)]", "form"),
    "[vattamāne, nirodhasamāpannānaṃ asaññasattānaṃ (sī. syā.)]":
        B.parse_variant("[vattamāne, nirodhasamāpannānaṃ asaññasattānaṃ (sī. syā.)]", "form"),
    "[paccuppannenātītā (syā.)]": B.parse_variant("[paccuppannenātītā (syā.)]", "form"),
}

# ===============================================================================================================
# 3. Cuts this chapter adds
# ===============================================================================================================
CUT_NOQ_RE = re.compile(r"(?:\((Kha)\) )?([Yy])assa vā pana…pe…\.((?: .*)?)")
YY_CUT_RE = re.compile(r"Yassa yattha (.+?)…pe…\.")
TI_DOT_RE = re.compile(r"\((?:Ka|Kha)\) (?:yassa|yattha) [^?…]+ti\.")
LOCS = ("tesaṃ tattha", "tesaṃ", "tattha")


def cut_no_q(body):
    """'(Kha) yassa vā pana…pe…. Āmantā.' / 'Yassa vā pana…pe….' (no «?» in the Pāli): the shell of 5-01's
    b_cut_question without «không?» (coordinator: a cut ending '…pe….' without '?' ends «…»)."""
    m = CUT_NOQ_RE.fullmatch(body)
    if not m:
        return None
    label, y, rest = m.groups()
    if bool(label) != (y == "y"):
        raise ValueError(f"label / capital mismatch: {body!r}")
    s = f"{C.VA_PANA} {C.AT} {C.Q_REL['yassa'][0]} mà{PE}"
    if label:
        s = f"{LABEL[label]} {s}"
        assert TP.b_cut_question("(Kha) yassa vā pana…pe…?")[0] == s + " không?"
    SLIPS.append(("cut question ends «…pe….» (no «?»): «…» kept, no «không?»", body[:50]))
    return s + (chunk_vi(rest) if rest else "")


def yy_cut(body):
    """'Yassa yattha A V…pe….' → «Ở người nào, ở nơi nào mà A V…» (= 2-02 b_cut with the yassa yattha shell)."""
    m = YY_CUT_RE.fullmatch(body)
    if not m:
        return None
    a, v = B.split_mv(m.group(1), M)
    return f"{cap(C.AT)} {C.Q_REL['yassa yattha'][0]} mà {a} {v[0]}{PE}"


def _member_at(w):
    return next((k for k, x in enumerate(w) if TP._is_member(x.rstrip(","), M)), None)


def cut_answer(core):
    """An answer piece cut by …pe… before its full stop (no «.»/«?»):
    '<head> <res>' → «<Head>, thì ở những người ấy[, ở nơi ấy]»;
    a whole no-ca / both sentence → 5-01's b_sentence without the «.»;
    '<head> <res> A V' → «<Head>, thì <res> A V» (the first half of 2-01's b_noca)."""
    w = core.split()
    lower = core[:1].islower()
    for loc in LOCS:
        n = len(loc.split())
        if len(w) > n and " ".join(w[-n:]) == loc and _member_at(w) is None:
            head = TP.head_vi(w[:-n])
            if loc == "tattha":
                raise ValueError(f"place head cut after 'tattha' not placed: {core!r}")
            out = f"{head}, {C.THEN} {B.L[loc]}"
            return _decap(out) if lower else out
    i = _member_at(w)
    if not i:
        return None
    if ", no ca " in core or w[i].endswith("ñca"):
        r = TP.b_sentence(cap(core) + ".")
        if r is None:
            return None
        return _decap(r[:-1]) if lower else r[:-1]
    if i >= 2 and " ".join(w[i - 2:i]) == "tesaṃ tattha":
        loc, h = "tesaṃ tattha", i - 2
    elif w[i - 1] in ("tesaṃ", "tattha"):
        loc, h = w[i - 1], i - 1
    else:
        raise ValueError(f"no resumptive before the member: {core!r}")
    head = w[:h]
    if loc == "tattha" and not all((pt := B.plane_tok(TP._lc(x), TP.PLANES)) and pt[1] == "loc" for x in head):
        raise ValueError(f"'tattha' after a non-place head: {core!r}")
    a, v = B.split_mv(" ".join(w[i:]), M)
    out = f"{TP.head_vi(head)}, {C.THEN} {B.L[loc]} {a} {v[0]}"
    full = TP.b_sentence(cap(core) + f", no ca {loc} {w[i]} {' '.join(w[i + 1:])}.")   # same first half as b_noca
    assert full.startswith(out + ", "), (out, full)
    return _decap(out) if lower else out


# ===============================================================================================================
# 4. Line translator (= 5-01's line_vi / tr_line, with the notes, the cuts above and the private head parser)
# ===============================================================================================================
def piece(p):
    core = p.strip()
    if core in NOTES:
        return NOTES[core]
    if core == "Nirodhavāro.":
        return NIRODHAVARO_CLOSE
    if not core.endswith(("?", ".")):
        try:
            return TP.piece(core)
        except ValueError:
            r = cut_answer(core)
            if r is None:
                raise
            return r
    return TP.piece(core)


def chunk_vi(chunk):
    lead = chunk[:len(chunk) - len(chunk.lstrip())]
    trail = chunk[len(chunk.rstrip()):]
    body = chunk.strip()
    if not body:
        return chunk
    parts = [x for x in re.split(r"(?<=[?.]) ", body) if x]
    return lead + " ".join(piece(x) for x in parts) + trail


def line_vi(body):
    if body in NOTES:
        return NOTES[body]
    if body in TP.FIXED:
        return TP.FIXED[body]
    if body == "Nirodhavāro.":
        return NIRODHAVARO_CLOSE
    if (c := cut_no_q(body)) is not None:
        return c
    if (c := yy_cut(body)) is not None:
        return c
    if TI_DOT_RE.fullmatch(body):
        SLIPS.append(("pair question ends «ti.» (plainly a question): «?»", body[:60]))
        q = TP.b_question(body[:-1] + "?")
        if q is None:
            raise ValueError(f"'ti.' question not placed: {body!r}")
        return q
    if (c := TP.b_cut_line(body)) is not None:
        return c
    pre = ""
    if (cq := TP.b_cut_question(body)) is not None:
        pre, body = cq
        if not body.strip():
            return pre
    pieces = TP.PE_SPLIT.split(body)
    out = []
    for k in range(0, len(pieces), 3):
        vi = chunk_vi(pieces[k])
        if k + 1 < len(pieces):
            if vi.endswith("."):
                SLIPS.append(("«.» right before …pe… (absorbed: never «.…»)", body[:60]))
                vi = vi[:-1]
            vi += pieces[k + 1] + PE
        out.append(vi)
    return pre + "".join(out)


VERB_SLIPS = {" nirujjhiti.": " nirujjhati."}            # termbase: nirujjhiti = variant spelling of nirujjhati


def tr_line(p):
    m = re.search(r" (\^\S+)$", p)
    bid = m.group(1) if m else None
    body = p[:m.start()] if m else p
    if body.startswith("#"):
        hashes, text = body.split(" ", 1)
        out = f"{hashes} {TP.heading(text)}"
    else:
        for bad, good in VERB_SLIPS.items():
            if bad in body:
                SLIPS.append((f"«{bad.strip()}» (termbase variant spelling of «{good.strip()}»)", bid or body[:40]))
                body = body.replace(bad, good)
        brs = TP.VAR_RE.findall(body)
        for k, br in enumerate(brs):
            body = body.replace(br, f"⟦{k}⟧", 1)
        out = line_vi(body)
        for k, br in enumerate(brs):
            if br not in VARIANTS:
                raise ValueError(f"undeclared variant {br!r}")
            if out.count(f"⟦{k}⟧") != 1:
                raise ValueError(f"variant {br!r} lost in {p!r}")
            out = out.replace(f"⟦{k}⟧", VARIANTS[br])
        if "⟦" in out or TP.KC_TOKEN in out:
            raise ValueError(f"unplaced token in {p!r}")
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
                tr_line(ln)
            except (ValueError, KeyError, AssertionError) as e:
                bad += 1
                print("FAIL:", repr(e)[:300], "\n   ", ln[:200])
    print("failing lines:", bad)


# ===============================================================================================================
# 5. Assertions: shared strings, reuse, and 5-01 reproduced byte for byte
# ===============================================================================================================
REUSED = [   # (Pāli, Vietnamese, book): asserted to occur in that book's Vietnamese rails
    ("(Yathā rūpakaṇḍe vibhattaṃ, tathā idha vibhajitabbaṃ.) (pi-2 1-khandhavibhango)", VIBHATTA, "2"),
    ("… tathā idha vibhajitabbaṃ (pi-2)", VIBHAJITABBA, "2"),
    ("nānākaraṇaṃ (pi-5)", NANAKARANA, "5"),
    ("sammoho (pi-1)", "sự mê lầm", "1"),
]
TERMBASE_USED = [
    ("yatthakaṃ", P_PLACE), ("Yassakampi", P_PERSON), ("yassayatthakampi", P_PERSON_PLACE),
    ("yassayatthakepi", P_PERSON_PLACE), ("yatthakampi", P_PLACE), ("uppādepi", UPPADE), ("nirodhepi", NIRODHE),
    ("uppādanirodhepi", UPPADANIRODHE), ("uppādavāre", B.UPPADAVARO), ("Uppādavārepi", B.UPPADAVARO),
    ("nirodhavārepi", B.NIRODHAVARO), ("uppādanirodhavārepi", B.UPPADANIRODHAVARO), ("pucchā", "câu hỏi"),
    ("anulomampi", B.ORDER["anuloma"].lower()), ("paccanīkampi", B.ORDER["paccanīka"].lower()),
    ("nirodhasamāpannānanti", "người nhập thành tựu thiền chấm dứt"), ("Natthi", "không có"),
    ("Pacchimacittassa bhaṅgakkhaṇe", f"khoảnh khắc tan rã của {FINAL_MIND}"), ("nirujjhiti", "chấm dứt"),
    ("nirodhavāro", B.NIRODHAVARO), ("nirujjhati", "chấm dứt"), ("nirujjhittha", "đã chấm dứt"),
    ("nirujjhissati", "sẽ chấm dứt"),
]


def check_assertions():
    tb = T.TERMBASE.read_text(encoding="utf-8")
    bad = [(p, v) for p, v in TERMBASE_USED
           if not re.search(r"^" + re.escape(p) + r": \{[^\n]*: " + re.escape(v) + r"[};]", tb, re.M | re.I)]
    assert not bad, "termbase strings not found: " + repr(bad)
    texts = {b: unicodedata.normalize("NFC", "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md"))))
             for b, d in S.RAILS.items()}
    bad = [(p, v, b) for p, v, b in REUSED if unicodedata.normalize("NFC", v).lower() not in texts[b].lower()]
    assert not bad, "reused strings not found in their rails: " + repr(bad)
    # Pacchimacittassa bhaṅgakkhaṇe = 9-02's head byte for byte
    assert TP.head_vi(["Pacchimacittassa", "bhaṅgakkhaṇe"]) == DY2.answer_head("Pacchimacittassa bhaṅgakkhaṇe", "tesaṃ")
    # the private instance = the shared one on 5-01's own heads
    for hd in ("Sabbesaṃ upapajjantānaṃ pavatte cittassa uppādakkhaṇe", "Pacchimacittasamaṅgīnaṃ",
               "Aggamaggassa bhaṅgakkhaṇe arahantānaṃ yassa cittassa anantarā aggamaggaṃ paṭilabhissanti tassa "
               "cittassa bhaṅgakkhaṇe asaññasattānaṃ"):
        assert TP.head_vi(hd.split()) == T.head_vi(hd.split()), hd
    # 5-01's chapter re-translates identically with this file's translator (identical Pāli = identical Vietnamese)
    vi01 = (S.OUT_DIR / T.CH).read_text(encoding="utf-8")
    redo = "\n\n".join("\n".join(tr_line(x) for x in seg) for seg in S.segments_of(T.CH)) + "\n"
    assert unicodedata.normalize("NFC", redo) == vi01, "5-01 not reproduced"
    del SLIPS[:]
    del TP.SLIPS_SEEN[:]
    # parsers still raise on unknown words
    for bad_s in ("Brahmānaṃ tesaṃ dukkhasaccaṃ nirujjhati", "Arūpe tesaṃ dukkhasaccaṃ nirujjhati tattha"):
        try:
            cut_answer(bad_s)
        except ValueError:
            continue
        raise AssertionError(f"no error on {bad_s!r}")


# ===============================================================================================================
# 6. Notes file (Pāli = tiếng Việt)
# ===============================================================================================================
def notes():
    out = [f"# pi-6 rails {N} (Saccayamaka 2): nirodhavāra and the start of the uppādanirodhavāra", "",
           "Builder: build_rails_5-02_vi.py. Imports build_rails_5-01_vi READ-ONLY (and through it 2-01, 7-01, 8, 2-02, "
           "9-01), 9-02 (Pacchimacittassa bhaṅgakkhaṇe) and 3-01 (asammohantena). 5-01's head parser runs in a private "
           "second instance whose own MIND_KIND adds «tâm cuối cùng»; the builder asserts that its translator "
           "reproduces the 5-01 chapter byte for byte. Exposed for 5-03: `FINAL_MIND`, `NOTES`, `VARIANTS`, "
           "`cut_answer`, `cut_no_q`, `yy_cut`, `piece`, `chunk_vi`, `line_vi`, `tr_line`, `build`. "
           "Format: Pāli = tiếng Việt.", ""]

    def h(t):
        out.extend(["", f"## {t}", ""])

    def row(p, v):
        out.append(f"{p} = {v}")

    h("New strings set here")
    row("Pacchimacittassa bhaṅgakkhaṇe (head)", TP.head_vi(["Pacchimacittassa", "bhaṅgakkhaṇe"]) + "  (= 9-02)")
    row("Nirodhavāro.", NIRODHAVARO_CLOSE)
    for p, v in NOTES.items():
        row(p, v)
    for p, v in VARIANTS.items():
        if p not in T.VARIANTS:
            row(p, v)
    h("Cuts")
    for b in ("(Kha) yassa vā pana…pe…. Āmantā.", "Yassa vā pana…pe….", "Yassa yattha dukkhasaccaṃ nirujjhati…pe….",
              "Yassa yattha dukkhasaccaṃ na nirujjhati…pe….", "Asaññasatte tattha dukkhasaccaṃ nirujjhati…pe….",
              "Yattha dukkhasaccaṃ na nirujjhati…pe…."):
        row(b, line_vi(b))
    for c in ("Asaññasatte tattha dukkhasaccaṃ uppajjati, no ca tattha samudayasaccaṃ nirujjhati",
              "Itaresaṃ catuvokārānaṃ pañcavokārānaṃ tesaṃ tattha dukkhasaccañca nirujjhissati samudayasaccañca "
              "nirujjhissati",
              "Aggamaggasamaṅgīnaṃ arahantānaṃ yassa cittassa anantarā aggamaggaṃ paṭilabhissanti asaññasattānaṃ tesaṃ "
              "tattha", "itaresaṃ catuvokārānaṃ pañcavokārānaṃ tesaṃ tattha"):
        row(f"{c}…pe…", cut_answer(c) + PE)
    h("Sample lines as built")
    for s in ("(Ka) yassa dukkhasaccaṃ na nirujjhati tassa samudayasaccaṃ na nirujjhitthāti? Nirujjhittha.",
              "Pacchimacittassa bhaṅgakkhaṇe tesaṃ samudayasaccañca na nirujjhissati dukkhasaccañca na nirujjhissati.",
              "Taṇhāya bhaṅgakkhaṇe tesaṃ dukkhasaccaṃ nuppajjati, no ca tesaṃ samudayasaccaṃ na nirujjhati.",
              "Pacchimacittasamaṅgīnaṃ tesaṃ samudayasaccañca na nirujjhissati dukkhasaccañca nuppajjissati.",
              "(Ka) yassa yattha dukkhasaccaṃ na nirujjhittha tassa tattha samudayasaccaṃ na nirujjhissatīti? "
              "Nirujjhissati."):
        row(s, tr_line(s))
    h("Termbase misfits and gaps (for the coordinator)")
    out += [
        "- No termbase entries: vibhattā / vibhajitabbā(ṃ) (pi-2 / 2-02 «như đã được phân tích trong …, … cũng nên phân "
        "tích như vậy»); atītā pucchā «các câu hỏi về quá khứ», Paccuppannaatītā pucchā «các câu hỏi về hiện tại và quá "
        "khứ» (pucchā «câu hỏi»; 2-01 TIME); yassayatthakepi … (cetaṃ) na kātabbaṃ «ở phần về người và nơi chốn cũng "
        "không nên trình bày (điều này: ) “…”» (2-02 kātabbaṃ «nên được trình bày», -pi «cũng», ca «và», etaṃ «điều "
        "này»); pāṭhantaraṃ (in a variant) «dị bản» (S.var label word); pana "
        "«còn».",
        "- The -epi locatives of the notes (uppādepi / nirodhepi / uppādanirodhepi; uppādavārepi …) «ở …» each, as 3-01's "
        "«ở hiện tại, ở quá khứ …»; pairs and triples with «cả … lẫn …» as 5-01's NOTE_YASSAKA.",
        "- nirodhasamāpannānanti (a word of the text quoted in a note) «“những người nhập thành tựu thiền chấm dứt”» (8).",
        "- samudayasaccaṃ maggasaccaṃ nānākaraṇaṃ «sự thật về sự phát sinh và sự thật về con đường có sự khác biệt».",
        "",
        "## Pāli as written (reported)",
        "",
        "- ^6-5-90, ^6-5-100, ^6-5-148, ^6-5-138: answers cut by …pe… before their full stop (and ^6-5-148 «tesaṃ "
        "tattha …pe… itaresaṃ …»): the Vietnamese answer is cut at the same spot («…»), the space before …pe… kept.",
        "- ^6-5-138 note «sadisaṃ natthi nānākaraṇaṃ» without a comma: the clause break takes «, » (as 2-02).",
        "- ^6-5-152 note «aggamaggassa bhaṅgakkhaṇe, arahantānaṃ …»: the comma inside the quoted head absorbed by the "
        "list commas (as 5-01).",
        "- ^6-5-63 variant inside the head goes after «… ngay sau tâm này» (the Pāli it follows); ^6-5-122 variant "
        "after «… đang diễn ra» (5-01's placement rule).",
        "- ^6-5-124 first (Ka) answer, second sentence: «asaññasattaṃ upapajjantānaṃ» stands twice in the head: kept as "
        "written (the repeated group stays).",
        "- ^6-5-93, ^6-5-141: the two-part kinds «taṇhāvippayuttamaggavippayutta-» / «maggavippayuttataṇhāvippayutta-» "
        "keep the Pāli order («tâm A và B», coordinator).",
        "- Termbase adherence: 5 misses (946 occurrences), all «Itaresaṃ catuvokārānaṃ pañcavokārānaṃ» = 2-01's one "
        "group «chúng sinh khác trong cõi gồm bốn khối và cõi gồm năm khối» (as 5-01 / 9-02): not genuine.",
    ]
    return out


def main():
    if "--probe" in sys.argv:
        probe()
        return
    S.check_reused()
    B.check_reused()
    check_assertions()
    segs = build(CH)
    C.write(CH, segs, extra_dirs=(ADH_DIR,))
    slips = sorted(set(SLIPS) | set(TP.SLIPS_SEEN))
    lines = notes() + [f"- {p}: {v}" for p, v in slips] + [""]
    NOTES_MD.write_text(unicodedata.normalize("NFC", "\n".join(lines)), encoding="utf-8", newline="\n")
    print("wrote", NOTES_MD)
    for p, v in slips:
        print("slip:", p, "|", v)


if __name__ == "__main__":
    main()
