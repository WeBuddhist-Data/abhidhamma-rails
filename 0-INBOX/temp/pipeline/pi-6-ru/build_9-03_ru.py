"""Russian plain zero-shot of pi-6 (Yamaka): chapter 9-03-dhammayamaka.md (Dhammayamaka close: the last time
sections of the uppādanirodhavāra, the bhāvanāvāra and the book's closing lines).

The pavattivāra lines take every frame from build_9-02_ru (CFG, units_9_02()) and build_9-01_ru (tr(), DH_CFG,
the Dhamma members and moments; families A / B of build_2-01_ru, person / place shape of build_7-01_ru, moments of
build_8_ru, intros of build_5-01_ru). None of those files is edited.
NEW here (listed in notes-9-03.md):
  Bhāvanāvāro (heading) = «Раздел о развитии»; "Bhāvanāvāro." = «Раздел о развитии.» (7-01 VARO_CLOSING)
  bhāveti = «развивает» (pi-1 «развивает путь»); pajahati / nappajahati = «устраняет» / «не устраняет»
  (7-01 TRANSITIVE, 7-05, pi-5); the object keeps the accusative when negated (7-06).
  kusalaṃ dhammaṃ / akusalaṃ dhammaṃ (acc. sg.) = «благое явление» / «неблагое явление» (pi-2 «благого или
  неблагого явления», sg.)
  yo … so …? = 7-01 Q_WHO «Кто …, тот …?»; vā pana = KHA_PREFIX «А кто …» (as 2-02 pj_question)
  "Āmantā…pe…." = «Да…» (5-01, 7-04, 7-05); "Abhidhammapiṭake" (plain line) = B.ABHIDHAMMAPITAKE.

Run:    python -I -X utf8 -B 0-INBOX\\temp\\pipeline\\pi-6-ru\\build_9-03_ru.py
Probe:  python -I -X utf8 -B 0-INBOX\\temp\\pipeline\\pi-6-ru\\build_9-03_ru.py --probe   (prints, writes nothing)
Import: M = importlib.import_module("build_9-03_ru")   (importing never writes any file; only __main__ builds)
"""
import importlib
import pathlib
import re
import sys
import unicodedata

HERE = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-ru")
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
import build_sample_ru as B  # noqa: E402

M2 = importlib.import_module("build_9-02_ru")
N9 = M2.N9
A, C, S = N9.A, N9.C, N9.S

CHAPTER = "9-03-dhammayamaka.md"
cap, lower1 = B.cap, C.lower1

# =============================================================================================
# Bhāvanāvāra
# =============================================================================================
BHAVANAVARO = "Раздел о развитии"                         # Bhāvanāvāro (bhāveti = «развивает», pi-1)
assert B.SECTION_HEADINGS["Pariññāvāro"].startswith("Раздел о ")
BH_VERBS = {   # Pāli form -> (Russian verb, negated)
    "bhāveti": ("развивает", False),
    "pajahati": (C.TRANSITIVE["pajahati"][0], False),
    "nappajahati": (C.TRANSITIVE["nappajahati"][0], True),
}
assert BH_VERBS["pajahati"] == ("устраняет", False) and BH_VERBS["nappajahati"] == ("устраняет", True)
NEG = "не "
BH_NOUN_ACC = "явление"                                   # dhammaṃ (acc. sg.; pi-2 «благого или неблагого явления»)
BH_OBJ = {f"{N9.DH_PL[x][:-1]}aṃ dhammaṃ": f"{B.ADJ[x]['n_nom']} {BH_NOUN_ACC}" for x in ("kusala", "akusala")}
assert BH_OBJ == {"kusalaṃ dhammaṃ": "благое явление", "akusalaṃ dhammaṃ": "неблагое явление"}, BH_OBJ
BH_PRED = "{v} {obj}"                                     # verb before the object (2-02 PJ_PRED)
assert C.Q_WHO == "Кто {p1}, тот {p2}?" and C.KHA_PREFIX == "А "

_OBJ_RE = "(?:" + "|".join(re.escape(k) for k in sorted(BH_OBJ, key=len, reverse=True)) + ")"
_V_RE = "(?:" + "|".join(sorted(BH_VERBS, key=len, reverse=True)) + ")"
BH_Q_RE = re.compile(rf"yo(?P<vp> vā pana)? (?P<x>{_OBJ_RE}) (?P<n1>na )?(?P<v1>{_V_RE}) so (?P<y>{_OBJ_RE}) "
                     rf"(?P<n2>na )?(?P<v2>{_V_RE})")


def _unti(w):
    """pajahatīti -> pajahati; bhāvetīti -> bhāveti."""
    if w.endswith("īti") and w[:-3] + "i" in BH_VERBS:
        return w[:-3] + "i"
    return w


def bh_pred(v, obj, na):
    ru, neg = BH_VERBS[v]
    assert not (neg and na), v
    return BH_PRED.format(v=(NEG if (neg or na) else "") + ru, obj=BH_OBJ[obj])


def bh_question(body):
    """'yo X V so Y V-ti' -> «Кто {p1}, тот {p2}?»; 'vā pana' -> «А кто …»."""
    words = body.split(" ")
    words[-1] = _unti(words[-1])
    m = BH_Q_RE.fullmatch(" ".join(words))
    if not m:
        raise ValueError(f"bhāvanā question not parsed: {body!r}")
    q = C.Q_WHO.format(p1=bh_pred(m.group("v1"), m.group("x"), m.group("n1")),
                       p2=bh_pred(m.group("v2"), m.group("y"), m.group("n2")))
    return C.KHA_PREFIX + lower1(q) if m.group("vp") else q


AMANTA_PE = C.AMANTA[:-1] + "…"                           # "Āmantā…pe…." = «Да…» (5-01, 7-04, 7-05)
assert AMANTA_PE == "Да…"
BH_ANSWERS = {"Āmantā.": C.AMANTA, "Āmantā…pe….": AMANTA_PE}


def bh_line(text):
    label = ""
    m = N9.LABEL_RE.fullmatch(text)
    if m:
        label, text = f"({B.LETTERS[m.group(1)]}) ", m.group(2)
    q, _, rest = text.partition("?")
    assert _ == "?", text
    rest = rest.strip()
    return label + bh_question(q) + (" " + BH_ANSWERS[rest] if rest else "")


# =============================================================================================
# Fixed lines, line driver
# =============================================================================================
FIXED_9_03 = dict(M2.CFG["fixed"])
FIXED_9_03.update({
    "#### Bhāvanāvāro": f"#### {BHAVANAVARO}",
    "Bhāvanāvāro.": C.VARO_CLOSING.format(heading=BHAVANAVARO),
    "Abhidhammapiṭake": B.ABHIDHAMMAPITAKE,
})
assert FIXED_9_03["Dhammayamakaṃ niṭṭhitaṃ."] == "Парные вопросы о явлениях завершены."
assert FIXED_9_03["Pavattivāro niṭṭhito."] == "Раздел о протекании завершён."
assert B.FIXED["Namo tassa bhagavato arahato sammāsambuddhassa"] == B.NAMO
CFG = dict(M2.CFG, fixed=FIXED_9_03)


def tr(body, cfg, mode):
    if mode == "bh" and body.strip() and body not in cfg["fixed"] and body not in B.FIXED:
        return bh_line(body)
    return N9.tr(body, cfg, mode)


def translate_text(src, cfg=None, mode="pv"):
    """9-03 continues the pavattivāra (mode "pv"); the bhāvanāvāra heading switches to mode "bh"."""
    cfg = cfg or CFG
    out = []
    with M2.units_9_02():
        for line in src.split("\n"):
            body, bid = B.ID_RE.match(line).groups()
            if body.startswith("#") and "Bhāvanā" in body:
                mode = "bh"
            out.append(tr(body, cfg, mode) + (bid or ""))
    return unicodedata.normalize("NFC", "\n".join(out))


# =============================================================================================
# Checks
# =============================================================================================
CROSSBOOK = [
    ("1", "развивает путь"),                  # bhāveti
    ("2", "благого или неблагого явления"),   # kusalaṃ / akusalaṃ dhammaṃ (sg.)
    ("5", "устраняет"),                       # pajahati
    ("1", B.ABHIDHAMMAPITAKE),
]


def check_against_finished(src, ru):
    """Identical Pāli line = identical Russian line, inside the chapter and against every finished pi-6 chapter."""
    seen = {}
    names = [p.name for p in sorted(B.OUT_DIR.glob("*.md")) if p.name != CHAPTER and (B.PALI_DIR / p.name).exists()]
    for n in names:
        p = (B.PALI_DIR / n).read_text(encoding="utf-8").split("\n")
        r = (B.OUT_DIR / n).read_text(encoding="utf-8").split("\n")
        if len(p) != len(r):
            continue
        for a, b in zip(p, r):
            pb, rb = B.ID_ANY.sub("", a).strip(), B.ID_ANY.sub("", b).strip()
            seen.setdefault(pb, {}).setdefault(rb, n)
    bad, shared, mine = [], 0, {}
    for a, b in zip(src.split("\n"), ru.split("\n")):
        pb, rb = B.ID_ANY.sub("", a).strip(), B.ID_ANY.sub("", b).strip()
        if pb in mine:
            assert mine[pb] == rb, f"inconsistent inside the chapter: {pb!r}"
        mine[pb] = rb
        if pb.strip() and pb in seen:
            shared += 1
            if rb not in seen[pb]:
                bad.append((pb, rb, seen[pb]))
    if bad:
        raise AssertionError("differs from finished chapters: " + repr(bad[:5]))
    return shared, names


def probe():
    src = (B.PALI_DIR / CHAPTER).read_text(encoding="utf-8")
    for i, line in enumerate(translate_text(src).split("\n"), 1):
        print(i, line)


def main():
    B.check_crossbook()
    A.check_crossbook()
    A.check_crossbook(S.CROSSBOOK)
    A.check_crossbook(N9.CROSSBOOK)
    A.check_crossbook(M2.CROSSBOOK)
    A.check_crossbook(CROSSBOOK)
    C.check_crossbook_c()
    src = (B.PALI_DIR / CHAPTER).read_text(encoding="utf-8")
    ru = translate_text(src)
    B.check_pair(src, ru, CHAPTER)
    shared, names = check_against_finished(src, ru)
    with open(B.OUT_DIR / CHAPTER, "w", encoding="utf-8", newline="\n") as f:
        f.write(ru)
    print("written", B.OUT_DIR / CHAPTER, "lines", len(ru.split("\n")))
    for s in N9.SLIP_LOG + S.SLIP_LOG + A.SLIP_LOG:
        print("slip:", s)
    print(f"cross-book asserts OK; per-line checks OK; {shared} lines shared with {len(names)} finished chapters agree")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--probe":
        probe()
    else:
        main()
