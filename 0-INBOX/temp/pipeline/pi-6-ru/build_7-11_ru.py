"""Russian plain zero-shot of pi-6 (Yamaka): 7-11-anusayayamaka.md ((Kha) dhātuvisajjanāvāra; the yamaka close).

Every frame shared with 7-10 is imported from build_7-10_ru (dhatu_who, planes_ru, DHATU_SRC_RU, BHANGA_RU,
DHATU_BHANGA_NATTHI10, MULAKA10, check_local10's base P.check_local9) and through it from build_7-01 … 7-09 and
build_sample_ru (all imported, never edited). New here (all listed in notes-7-11.md):
  - "kassaci N anusayā anusenti" = «в некоторых случаях залегают N скрытых склонностей» (after the generic
    singular «У того, кто …» of 7-10 a plural «у некоторых» (pi-2 kassaci) would not agree; the commentary
    ^6-153 reads kassaci as a person type: "puthujjanavasena", "sotāpannasakadāgāmivasena").
  - numbers: satta «семь скрытых склонностей» (pi-2), pañca «пять скрытых склонностей», tayo «три скрытые склонности».
  - "satteva anusayā anusenti" = «залегают ровно семь скрытых склонностей» (commentary ^6-155 "sattevāti
    niyametvā vuttaṃ").
  - "X cutassa Y upapatti nāma natthi, heṭṭhā upapajjamāno kāmadhātuṃyeva upapajjati, …" = «У того, кто умер X,
    перерождения Y не бывает, перерождаясь ниже, он перерождается только в мире чувственных желаний, у него …»
    (the Pāli commas kept, user punctuation rule).
  - closings "Dhātuvisajjavāro." «Раздел ответов об элементах.» (spelling slip for dhātuvisajjanā-, as the heading),
    "Anusayayamakaṃ niṭṭhitaṃ." «Парные вопросы о скрытых склонностях завершены.», "Namo …" = B.NAMO.

Run:    python -I -X utf8 -B 0-INBOX\\temp\\pipeline\\pi-6-ru\\build_7-11_ru.py [--dry]
Import: importlib.import_module("build_7-11_ru")   (importing never writes any file)
"""
import importlib
import pathlib
import re
import sys
import unicodedata

PIPE = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-ru")
if str(PIPE) not in sys.path:
    sys.path.insert(0, str(PIPE))
import build_sample_ru as B   # noqa: E402

T = importlib.import_module("build_7-10_ru")
C, P, M = T.C, T.P, T.M

CHAPTER = "7-11-anusayayamaka.md"
cap = B.cap

# ---------------------------------------------------------------------------------------------
# Answer frames
# ---------------------------------------------------------------------------------------------
NUM_RU = {   # N anusayā (nom.)
    "satta": "семь " + C.ANUSAYA_HEAD_PL["gen"],          # pi-2 «семь скрытых склонностей»
    "pañca": "пять " + C.ANUSAYA_HEAD_PL["gen"],
    "tayo": "три " + C.ANUSAYA_HEAD_PL["nom"],
}
assert NUM_RU["tayo"] == "три скрытые склонности"
ANUSENTI_PL = "залегают"                                   # anusenti (pl.; 7-01 VERB «залегает»)
assert C.VERB["anuseti"][0] == "залегает"
KASSACI = "в некоторых случаях"                            # kassaci (see the docstring)
KASSACI_FRAME = KASSACI + " " + ANUSENTI_PL + " {n}"       # kassaci N anusayā anusenti
SATTEVA = ANUSENTI_PL + " ровно " + NUM_RU["satta"]        # satteva anusayā anusenti
BHANGA_NATTHI = T.DHATU_BHANGA_NATTHI10                    # anusayā bhaṅgā natthi (coordinator, 7-10)
assert T.BHANGA_RU == "подлежит разделению" and BHANGA_NATTHI == "скрытых склонностей, подлежащих разделению, нет"

DHATU_CUTA_ONLY = "у того, кто умер {src}"                 # "X cutassa" with no upapajjantassa
NO_UPAPATTI = "перерождения {dst} не бывает"               # "Y upapatti nāma natthi"
HETTHA = "перерождаясь ниже, он перерождается только {kama}"   # heṭṭhā upapajjamāno kāmadhātuṃyeva upapajjati
HIS = "у него "                                            # the answer after HETTHA (cutassa)

PLANES = r"(?:na )?\w+dhātuyā(?: na \w+dhātuyā)*"
DST_ACC = r"(?:na )?\w+dhātuṃ(?: na \w+dhātuṃ)*"
ANS = r"satteva anusayā anusenti|kassaci \w+ anusayā anusenti(?:, kassaci \w+ anusayā anusenti)*"
RE_FULL = re.compile(rf"({PLANES}) cutassa ({DST_ACC}) upapajjantassa ({ANS}); anusayā bhaṅgā natthi\.")
RE_NOUP = re.compile(rf"({PLANES}) cutassa ({PLANES}) upapatti ?nāma natthi, heṭṭhā upapajjamāno "
                     rf"kāmadhātuṃyeva upapajjati, ({ANS}); anusayā bhaṅgā natthi\.")
SLIPS_11 = {"upapattināma": "upapatti nāma"}               # line 35: spelling only (joined), rendered as meant


def answer_ru(s):
    if s == "satteva anusayā anusenti":
        return SATTEVA
    parts = []
    for part in s.split(", "):
        m = re.fullmatch(r"kassaci (\w+) anusayā anusenti", part)
        parts.append(KASSACI_FRAME.format(n=NUM_RU[m.group(1)]))
    return ", ".join(parts)


def sentence_ru(s):
    s = C.lower1(s)
    m = RE_FULL.fullmatch(s)
    if m:
        src, dst, ans = m.groups()
        return cap(T.dhatu_who(src, dst)) + ", " + answer_ru(ans) + "; " + BHANGA_NATTHI + "."
    m = RE_NOUP.fullmatch(s)
    if m:
        src, dst, ans = m.groups()
        return (cap(DHATU_CUTA_ONLY.format(src=T.planes_ru(src, T.DHATU_SRC_RU))) + ", "
                + NO_UPAPATTI.format(dst=T.planes_ru(dst, T.DHATU_SRC_RU)) + ", "
                + HETTHA.format(kama=T.DHATU_DST_RU["kāmadhātuṃ"]) + ", "
                + HIS + answer_ru(ans) + "; " + BHANGA_NATTHI + ".")
    raise ValueError(f"dhātu answer not parsed: {s!r}")


FIXED11 = {
    "Dhātuvisajjavāro.": C.VARO_CLOSING.format(heading=cap(B.SECTION_HEADINGS["dhātuvisajjanāvāro"])),
    "Anusayayamakaṃ niṭṭhitaṃ.": B.YAMAKA_CLOSING_FRAME.format(title=B.YAMAKA_TITLES["Anusayayamakaṃ"]),
    "Namo tassa bhagavato arahato sammāsambuddhassa": B.NAMO,
}
assert FIXED11["Dhātuvisajjavāro."] == "Раздел ответов об элементах."
assert FIXED11["Anusayayamakaṃ niṭṭhitaṃ."] == "Парные вопросы о скрытых склонностях завершены."


def tr_line11(body):
    if not body.strip():
        return ""
    if body in FIXED11:
        return FIXED11[body]
    if body.startswith("#"):
        return P.heading9(body)
    tail = ""
    m = T.MULAKA_TAIL_RE.fullmatch(body)
    if m and m.group(2) in T.MULAKA10:
        body, tail = m.group(1), f" ({T.MULAKA10[m.group(2)]})"
    for a, b in SLIPS_11.items():
        body = body.replace(a, b)
    sents = re.split(r"(?<=natthi\.) (?=\S)", body.strip())
    return " ".join(sentence_ru(s) for s in sents) + tail


def translate_file(src_text):
    out = []
    for line in src_text.split("\n"):
        body, bid = B.ID_RE.match(line).groups()
        out.append(tr_line11(body) + (bid or ""))
    return "\n".join(out)


# ---------------------------------------------------------------------------------------------
# Checks
# ---------------------------------------------------------------------------------------------
CROSSBOOK_11 = [
    ("2", "семь скрытых склонностей"),                                   # satta anusayā
    ("2", "у некоторых появляются"),                                    # kassaci (pi-2; here «в некоторых случаях»)
]
FINISHED = T.FINISHED + ["7-10-anusayayamaka.md"]


def check_crossbook_11():
    cache, missing = {}, []
    for b, s in CROSSBOOK_11:
        if b not in cache:
            cache[b] = "\n".join(p.read_text(encoding="utf-8") for p in sorted(B.RAILS[b].glob("*.md")))
        if s not in cache[b]:
            missing.append((b, s))
    if missing:
        raise AssertionError(f"cross-book strings not found in the pi-1..5 rails: {missing}")
    return True


def check_local11(ru, src):
    P.check_local9(ru, src)
    for p, r in zip(src.split("\n"), ru.split("\n")):
        if p.startswith("#"):
            continue
        assert p.count("cutassa") == r.count("У того, кто"), r
        assert p.count("upapajjantassa") == r.count("кто, умерев ") == r.count(", перерождается "), r
        assert p.count("bhaṅgā natthi") == r.count(BHANGA_NATTHI), r
        assert p.count("kassaci") == r.count(KASSACI), r
        assert p.count("satteva") == r.count("ровно семь"), r
        assert p.count("kassaci satta") == r.count(KASSACI + " залегают семь "), r
        assert p.count("kassaci pañca") == r.count("пять "), r
        assert p.count("kassaci tayo") == r.count("три "), r
        assert p.count("upapatti") == r.count(" не бывает") == r.count("перерождаясь ниже"), r
        assert len(re.findall(r"\b[Nn]a ", p)) == r.count("не в мире "), r
        assert p.count("mūlakaṃ)") == r.count("(На основе "), r
        assert p.count(".") == r.count("."), r


def dry():
    src = (B.PALI_DIR / CHAPTER).read_text(encoding="utf-8")
    for i, r in enumerate(translate_file(src).split("\n"), 1):
        print(i, r)


def main():
    B.check_crossbook()
    C.check_crossbook_c()
    T.D.check_crossbook_02()
    T.E.check_crossbook_03()
    M.G.check_crossbook_05()
    M.check_crossbook_07()
    P.check_crossbook_09()
    T.check_crossbook_10()
    check_crossbook_11()
    src = (B.PALI_DIR / CHAPTER).read_text(encoding="utf-8")
    ru = unicodedata.normalize("NFC", translate_file(src))
    check_local11(ru, src)
    shared = M.check_consistency7(src, ru, FINISHED)
    B.check_pair(src, ru, CHAPTER)
    with open(B.OUT_DIR / CHAPTER, "w", encoding="utf-8", newline="\n") as f:
        f.write(ru)
    print("written", B.OUT_DIR / CHAPTER, "lines", len(ru.split("\n")), "| lines shared with finished chapters:",
          shared)
    print("cross-book asserts OK; consistency OK; per-line checks OK")


if __name__ == "__main__":
    if "--dry" in sys.argv:
        dry()
    else:
        main()
