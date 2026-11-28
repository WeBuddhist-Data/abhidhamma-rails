"""Russian plain zero-shot of pi-6 (Yamaka): chapter 5-03-saccayamaka.md (end of the Sacca uppādanirodhavāra,
the pariññāvāra, and the closing of the Saccayamaka).

Pavatti lines: build_5-02_ru (tr(), CFG, units_5_02()) on top of build_5-01_ru (Sacca members, SACCA_CFG,
pv_intro(), SC_UNITS, answer / question frames); none of those files is edited, the few additions below are applied
only inside units_5_03() (restores the imported modules afterwards).
Pariññā lines: family E of build_2-02_ru (PJ_RU, pj_pred frames, pj_subject(), PJ_* frames), extended with
pajahati «устраняет» (build_7-01_ru TRANSITIVE / build_7-05_ru) in the present, past and future (NEW, listed in
notes-5-03.md), and "no ca te …" with the resumptive pronoun (7-01 RES / NO_CA_POS_FRAME).

Run:    python -I -X utf8 -B 0-INBOX\\temp\\pipeline\\pi-6-ru\\build_5-03_ru.py [--probe [--show]]
Import: importlib.import_module("build_5-03_ru")   (importing never writes any file; only __main__ builds)
"""
import contextlib
import importlib
import pathlib
import re
import sys
import unicodedata

HERE = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-ru")
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
import build_sample_ru as B  # noqa: E402

T = importlib.import_module("build_5-02_ru")   # 5-02 additions, tr(), CFG
S = T.S                                         # build_5-01_ru: Sacca members and intros
A, E, C, D = S.A, S.E, S.C, S.D
G = importlib.import_module("build_7-05_ru")   # pajahati = «устраняет» (checked below)

CHAPTER = "5-03-saccayamaka.md"
PREV = ["5-01-saccayamaka.md", "5-02-saccayamaka.md"]
cap, lower1 = B.cap, C.lower1
SLIP_LOG = []

# =============================================================================================
# Pavatti additions
# =============================================================================================
UNITS_5_03 = [
    (r"aggaphalassa uppādakkhaṇe", f"{S.UPPADA} высшего плода", "adv", False),   # as «высшего пути» (SC_UNITS)
]


@contextlib.contextmanager
def units_5_03():
    """5-02's units plus UNITS_5_03, for the block only."""
    with T.units_5_02():
        old = list(S.ALL_UNITS)
        S.ALL_UNITS[:0] = UNITS_5_03
        try:
            yield
        finally:
            S.ALL_UNITS[:] = old


ATITANAGATA_PUCCHA = "вопросы о прошлом и будущем"          # atītānāgatā pucchā (Atītānāgatavāro, sample heading)
assert B.SECTION_HEADINGS["Atītānāgatavāro"] == "Раздел " + ATITANAGATA_PUCCHA.split(" ", 1)[1]
NOTE_6_5_164 = (f"(Как {T.IN_NIRODHA} разобраны {ATITANAGATA_PUCCHA} {T.ANULOMA_PACCANIKA}, так же следует "
                f"разбирать и {T.IN_UPPADANIRODHA}, {T.ASAMMOHANTENA}).")
NOTES_5_03 = {
    "(Yathā nirodhavāre atītānāgatā pucchā anulomampi paccanīkampi vibhattā evaṃ uppādanirodhavārepi "
    "asammohantena vibhajitabbaṃ).": NOTE_6_5_164,
}

# =============================================================================================
# Pariññāvāra: family E (build_2-02_ru) + pajahati
# =============================================================================================
# pajahati = «устраняет» (7-01 TRANSITIVE, 7-05 TRANSITIVE_05; pi-5 «полностью понимает страдание, устраняет
# возникновение»). NEW tenses, as family E builds parijānittha / parijānissati: past = perfective «устранил /
# устранили», future = perfective «устранит / устранят». Negation «не » before the verb, object in the accusative.
PJ3_FORMS = dict(E.PJ_FORMS)
PJ3_FORMS.update({
    "pajahati": ("pajahati", "pres", "sg"), "pajahanti": ("pajahati", "pres", "pl"),
    "pajahittha": ("pajahati", "past", None),
    "pajahissati": ("pajahati", "fut", "sg"), "pajahissanti": ("pajahati", "fut", "pl"),
})
PJ3_RU = dict(E.PJ_RU)
PJ3_RU.update({
    ("pajahati", "pres", "sg"): ("устраняет", "не устраняет"),
    ("pajahati", "pres", "pl"): ("устраняют", "не устраняют"),
    ("pajahati", "past", "sg"): ("устранил", "не устранил"),
    ("pajahati", "past", "pl"): ("устранили", "не устранили"),
    ("pajahati", "fut", "sg"): ("устранит", "не устранит"),
    ("pajahati", "fut", "pl"): ("устранят", "не устранят"),
})
assert PJ3_RU[("pajahati", "pres", "sg")][0] == C.TRANSITIVE["pajahati"][0]
assert PJ3_RU[("pajahati", "pres", "pl")][0] == G.TRANSITIVE_05["pajahanti"][0]
assert all(PJ3_RU[k] == E.PJ_RU[k] for k in E.PJ_RU)

# Objects (accusative): «истину о страдании» (5-01 SACCA_K «истина о страдании»)
PJ3_OBJ = {}
for _m in S.SACCA_GENMOD:
    assert S.SACCA_K[_m]["nom"] == "истина " + S.SACCA_GENMOD[_m]
    PJ3_OBJ[_m + "saccaṃ"] = "истину " + S.SACCA_GENMOD[_m]

PJ3_V = E._alt(PJ3_FORMS)
NEG = r"(?:na |nap(?=pajah))"          # "na parijānāti" / "nappajahati" (fused negation)
PJ3_Q_RE = re.compile(r"yo(?P<vp> vā pana)? (?P<x>\S+) (?P<n1>" + NEG + r")?(?P<v1>" + PJ3_V + r") so (?P<y>\S+) "
                      r"(?P<n2>" + NEG + r")?(?P<v2>" + PJ3_V + r")")
PJ3_S1_RE = re.compile(r"(?P<subj>.+?) (?P<x>\S+) (?P<n1>" + NEG + r")?(?P<v1>" + PJ3_V + r"), no ca "
                       r"(?:(?P<res>te|so) )?(?P<y>\S+) (?P<n2>" + NEG + r")?(?P<v2>" + PJ3_V + r")")
PJ3_S2_RE = re.compile(r"(?P<subj>.+?) (?P<x>\S+) ca (?P<n1>" + NEG + r")?(?P<v1>" + PJ3_V + r") (?P<y>\S+) ca "
                       r"(?P<n2>" + NEG + r")?(?P<v2>" + PJ3_V + r")")


def pj3_forms(v, num):
    lemma, tense, _ = PJ3_FORMS[v]
    return PJ3_RU[(lemma, tense, num)]


def pj3_pred(v, obj_ru, num, neg):
    pos, negf = pj3_forms(v, num)
    return E.PJ_PRED.format(v=negf if neg else pos, obj=obj_ru)


def unti3(w):
    """pajahatīti -> pajahati; nappajahitthāti -> nappajahittha; parijānissatīti -> parijānissati."""
    for suf, rep in (("īti", "i"), ("āti", "a")):
        base = w[: -len(suf)] + rep
        if w.endswith(suf) and re.sub(r"^nap(?=pajah)", "", base) in PJ3_FORMS:
            return base
    return w


def pj3_question(body):
    words = body.split(" ")
    words[-1] = unti3(words[-1])
    m = PJ3_Q_RE.fullmatch(" ".join(words))
    if not m:
        raise ValueError(f"pariññā question not parsed: {body!r}")
    p1 = pj3_pred(m.group("v1"), PJ3_OBJ[m.group("x")], "sg", bool(m.group("n1")))
    p2 = pj3_pred(m.group("v2"), PJ3_OBJ[m.group("y")], "sg", bool(m.group("n2")))
    q = C.Q_WHO.format(p1=p1, p2=p2)
    return C.KHA_PREFIX + lower1(q) if m.group("vp") else q


def _check_num(v, num, s):
    pn = PJ3_FORMS[v][2]
    assert pn is None or pn == num, f"verb number {v} vs subject {num}: {s!r}"


def pj3_sentence(s):
    """One Pāli pariññā answer sentence (final '.' removed) -> Russian sentence (with '.')."""
    if s + "." in C.SIMPLE_ANSWERS:
        return C.SIMPLE_ANSWERS[s + "."]
    s = A._norm(s)                                           # Xñca -> Xṃ ca
    for rx, kind in ((PJ3_S1_RE, 1), (PJ3_S2_RE, 2)):
        m = rx.fullmatch(s)
        if not m or m.group("x") not in PJ3_OBJ or m.group("y") not in PJ3_OBJ:
            continue
        subj, num = E.pj_subject(m.group("subj"))
        _check_num(m.group("v1"), num, s)
        _check_num(m.group("v2"), num, s)
        x, y = PJ3_OBJ[m.group("x")], PJ3_OBJ[m.group("y")]
        n1, n2 = bool(m.group("n1")), bool(m.group("n2"))
        p1 = pj3_pred(m.group("v1"), x, num, n1)
        if kind == 1:   # "no ca": the question's predicate is denied for Y (coordinator "Negatives")
            p2 = pj3_pred(m.group("v2"), y, num, not n2)
            if m.group("res"):                                   # "no ca te …": «, но они …» (7-01 RES)
                frame = C.NO_CA_POS_FRAME if n2 else C.NO_CA_FRAME
                tail = frame.format(res=C.RES[m.group("res")], **{("pos_pred" if n2 else "neg_pred"): p2})
            else:
                tail = E.PJ_NO_CA_FRAME.format(pred=p2)
            return f"{subj} {p1}{tail}."
        if n1 and n2:
            f1, f2 = pj3_forms(m.group("v1"), num)[1][3:], pj3_forms(m.group("v2"), num)[1][3:]
            both = (E.PJ_NEITHER_FRAME.format(v=f1, x=x, y=y) if f1 == f2
                    else E.PJ_NEG_MIXED_FRAME.format(v1=f1, x=x, v2=f2, y=y))
            return f"{subj} {both}."
        return f"{subj} {E.PJ_BOTH_FRAME.format(p1=p1, p2=pj3_pred(m.group('v2'), y, num, n2))}."
    raise ValueError(f"pariññā answer not parsed: {s!r}")


def pj3_answers(text):
    out = []
    for s in re.split(r"(?<=\.) (?=\S)", text.strip()):
        assert s.endswith("."), s
        out.append(pj3_sentence(s[:-1]))
    return " ".join(out)


PJ3_QA_RE = re.compile(r"\((Ka|Kha)\) (yo .+?)\?(?: (.+))?")
ABBR_YO = C.KHA_PREFIX + lower1(C.Q_WHO.split(" {")[0])          # «А кто» (as 5-01 PV_ABBR_HEAD «А у кого»)


def pj3_line(text):
    """A pariññāvāra line, or None when the line is not one."""
    m = PJ3_QA_RE.fullmatch(text)
    if m:
        lab, body, ans = m.groups()
        if body == "yo vā pana…pe…":                             # "(Kha) yo vā pana…pe…? Āmantā."
            out = f"({B.LETTERS[lab]}) {ABBR_YO}…?"
        else:
            out = f"({B.LETTERS[lab]}) {pj3_question(body)}"
        return out + (" " + pj3_answers(ans) if ans else "")
    if re.search(r"\bparijān", text):
        return pj3_answers(text)
    return None


# =============================================================================================
# Config, lines, chapter
# =============================================================================================
SACCA_CLOSING = B.YAMAKA_CLOSING_FRAME.format(title=B.YAMAKA_TITLES["Saccayamakaṃ"])
assert SACCA_CLOSING == "Парные вопросы об истинах завершены."
FIXED_5_03 = {
    "Pavattivāro niṭṭhito.": E.KH2_CFG["fixed"]["Pavattivāro niṭṭhito."],      # 2-02 «Раздел о протекании завершён.»
    "Saccayamakaṃ niṭṭhitaṃ.": SACCA_CLOSING,
}
# Variants of this chapter (default kind «вариант чтения»): anchor = the Russian the variant follows
ANCHORS_5_03 = {
    "atītenānāgatā (syā.)": ATITANAGATA_PUCCHA,                                # ^6-5-164 (as 5-02 paccuppannenātītā)
    "apāyā asaññasattā (syā.)": "умирает среди существ без восприятия",        # ^6-5-162 "asaññasattā cavantānaṃ"
    "apāyaṃ asaññasattaṃ (syā.)": "перерождается среди существ без восприятия",  # ^6-5-162 "asaññasattaṃ upapajjantānaṃ"
}
SLIPS_5_03 = []         # plain slips rendered as meant (none found)

CFG = dict(T.CFG)
CFG["slips"] = SLIPS_5_03
CFG["fixed"] = dict(T.CFG["fixed"], **FIXED_5_03)
CFG["variant_anchors"] = dict(T.CFG["variant_anchors"], **ANCHORS_5_03)

SPECIAL = {}            # Pāli line (variants removed) -> Russian; filled inside units_5_03()


def tr(text, cfg=None):
    """One Pāli line (block ID removed)."""
    cfg = cfg or CFG
    if not text.strip():
        return ""
    if text in cfg["fixed"] or text in B.FIXED or text.startswith("#"):
        return S.tr(text, cfg, "pv")
    r = pj3_line(text)
    if r is not None:
        return r
    variants, t = S._variants(text, cfg)
    if t in SPECIAL:
        return S._insert_variants(SPECIAL[t], variants, cfg)
    if t in NOTES_5_03:
        return S._insert_variants(NOTES_5_03[t], variants, cfg)
    return T.tr(text, cfg)


LINE_6_5_157_A = (
    "Aggamaggassa uppādakkhaṇe arahantānaṃ cittassa uppādakkhaṇe yassa cittassa anantarā aggamaggaṃ "
    "paṭilabhissanti tassa cittassa uppādakkhaṇe asaññasattaṃ upapajjantānaṃ tesaṃ tattha dukkhasaccaṃ…pe… "
    "itaresaṃ catuvokāraṃ pañcavokāraṃ upapajjantānaṃ pavatte cittassa uppādakkhaṇe tesaṃ tattha dukkhasaccaṃ…pe….")


def line_6_5_157_a():
    """^6-5-157 first answer: two intros, each with the subject and "…pe…" (verb and the rest elided);
    as 5-02's line_6_5_148 («… там … у остальных … там…»), with the subject the Pāli keeps."""
    x = S.SACCA_K["dukkha"]["nom"]
    i1 = S.pv_intro("Aggamaggassa uppādakkhaṇe arahantānaṃ cittassa uppādakkhaṇe yassa cittassa anantarā "
                    "aggamaggaṃ paṭilabhissanti tassa cittassa uppādakkhaṇe asaññasattaṃ upapajjantānaṃ", True)
    i2 = lower1(S.pv_intro("itaresaṃ catuvokāraṃ pañcavokāraṃ upapajjantānaṃ pavatte cittassa uppādakkhaṇe", True))
    return f"{i1}{x}… {i2}{x}…"


def fill_special():
    SPECIAL.clear()
    SPECIAL[LINE_6_5_157_A] = line_6_5_157_a()


def translate_text(src, cfg=None):
    cfg = cfg or CFG
    out = []
    with units_5_03():
        fill_special()
        for line in src.split("\n"):
            body, bid = B.ID_RE.match(line).groups()
            out.append(tr(body, cfg) + (bid or ""))
    return unicodedata.normalize("NFC", "\n".join(out))


def probe(show=False):
    src = (B.PALI_DIR / CHAPTER).read_text(encoding="utf-8")
    bad = 0
    with units_5_03():
        fill_special()
        for n, line in enumerate(src.split("\n"), 1):
            body, _ = B.ID_RE.match(line).groups()
            try:
                r = tr(body)
                if show and r:
                    print(f"{n}: {r}")
            except Exception as ex:  # noqa: BLE001
                bad += 1
                print(f"{n}: {type(ex).__name__}: {str(ex)[:300]}")
    print("failing lines:", bad)


# Strings taken from the approved pi-1 … pi-5 Russian rails (book, exact substring)
CROSSBOOK = [
    ("5", "полностью понимает страдание, устраняет возникновение"),   # parijānāti / pajahati (pi-5)
    ("5", "не понимает полностью страдание"),                         # na parijānāti (2-02)
    ("5", "устраняют"), ("5", "архат"),
]


def check_previous_unchanged():
    """5-01 and 5-02 rebuilt inside units_5_03() give the files on disk byte for byte."""
    n = 0
    with units_5_03():
        for name, fn in ((PREV[0], lambda s: S.translate_text(s, S.SACCA_CFG)), (PREV[1], T.translate_text)):
            src = (B.PALI_DIR / name).read_text(encoding="utf-8")
            assert fn(src) == (B.OUT_DIR / name).read_text(encoding="utf-8"), f"{name} would change"
            n += 1
    S.SLIP_LOG.clear()
    T.SLIP_LOG.clear()
    A.SLIP_LOG.clear()
    return n


def check_parinna(src, ru):
    assert "не полностью" not in ru, "negated parijānāti = «не понимает полностью» (2-02)"
    for p, r in zip(src.split("\n"), ru.split("\n")):
        if "pajah" in p:
            assert "устран" in r, (p, r)
        if "parijān" in p:
            assert "полностью" in r, (p, r)
            if re.search(r"(?<!\S)na parijān", p):
                assert "понимает полностью" in r or "понял полностью" in r or "поймёт полностью" in r \
                    or "понимают полностью" in r or "поняли полностью" in r or "поймут полностью" in r, (p, r)


def main():
    if "--probe" in sys.argv:
        probe("--show" in sys.argv)
        return
    B.check_crossbook()
    A.check_crossbook()
    A.check_crossbook(S.CROSSBOOK)
    A.check_crossbook(T.CROSSBOOK)
    A.check_crossbook(E.CROSSBOOK)
    A.check_crossbook(CROSSBOOK)
    C.check_crossbook_c()
    assert T.ASAMMOHANTENA in (B.OUT_DIR / "3-01-ayatanayamaka.md").read_text(encoding="utf-8")
    nprev = check_previous_unchanged()
    src = (B.PALI_DIR / CHAPTER).read_text(encoding="utf-8")
    for old, _, note in SLIPS_5_03:
        assert S.VARIANT_RE.sub("", src).count(old) == 1, f"slip pattern must occur once: {note}"
    SLIP_LOG.clear()
    ru = translate_text(src)
    B.check_pair(src, ru, CHAPTER)
    check_parinna(src, ru)
    prev = [((B.PALI_DIR / f).read_text(encoding="utf-8"), (B.OUT_DIR / f).read_text(encoding="utf-8"))
            for f in B.SAMPLE_FILES + ["2-01-khandhayamaka.md", "2-02-khandhayamaka.md", "7-01-anusayayamaka.md",
                                       "8-cittayamaka.md"] + PREV]
    A.consistency(prev + [(src, ru)])
    with open(B.OUT_DIR / CHAPTER, "w", encoding="utf-8", newline="\n") as f:
        f.write(ru)
    print("written", B.OUT_DIR / CHAPTER, "lines", len(ru.split("\n")))
    print(f"5-01 / 5-02 rebuilt byte-identical inside units_5_03(): {nprev} files")
    for s in SLIP_LOG + T.SLIP_LOG + S.SLIP_LOG + A.SLIP_LOG:
        print("slip:", s)
    print("cross-book asserts OK; per-line checks OK; consistency OK (sample, 2-01, 2-02, 7-01, 8, 5-01, 5-02)")


if __name__ == "__main__":
    main()
