"""Russian plain zero-shot of pi-6 (Yamaka): 7-02-anusayayamaka.md (Anusayavāra, paṭiloma: person / place /
person and place).

Family C frames come from build_7-01_ru (imported, never edited). New here (listed in notes-7-02.md):
  - paṭiloma "…, no ca tassa B nānuseti" = «…, но у него залегает B» (7-01's C.no_ca / NO_CA_POS_FRAME, coordinator
    "Negatives"); "A ca nānuseti B ca nānuseti" = «не залегает ни A, ни B» (7-01's C.clause / C.both_neg).
  - SABBATTHA: sabbattha = «везде» (pi-5 1-puggalakatha «личность везде обнаруживается»).
  - "…pe…." at the end of an answer -> "…" (sample rule); "(Kha) yattha vā pana…pe…?" = «(б) А где…?».
  - "Anusayavāre paṭilomaṃ." = 7-01's «Отрицательная форма в разделе о скрытых склонностях.» (paṭiloma* and
    paccanīka* headings share the sample's Russian); "Anusayavāro." = «Раздел о скрытых склонностях.».

Run:    python -I -X utf8 -B 0-INBOX\\temp\\pipeline\\pi-6-ru\\build_7-02_ru.py
Import: importlib.import_module("build_7-02_ru")   (importing never writes any file)
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

C = importlib.import_module("build_7-01_ru")

CHAPTER = "7-02-anusayayamaka.md"
cap = B.cap

# ---------------------------------------------------------------------------------------------
# New frames (7-02)
# ---------------------------------------------------------------------------------------------
SABBATTHA = "везде"                               # sabbattha (pi-5)
NO_CA_POS_FRAME = C.NO_CA_POS_FRAME               # ", no ca tassa B nānuseti": «, но у него залегает B» (C.no_ca)
# two negated predicates "A ca nānuseti B ca nānuseti": C.clause -> C.both_neg «не залегает ни A, ни B»
PE = "…pe…"
PE_END = "…"                                      # final "…pe…." -> "…" (sample)
Q_PE = {"yattha vā pana": "где", "yassa vā pana": "у кого", "yassa vā pana yattha": "у кого где"}

FIXED = dict(C.FIXED)
FIXED["Anusayavāre paṭilomaṃ."] = C.ANUSAYAVARE_FRAME.format(form=cap(B.SECTION_HEADINGS["paccanīkaṃ"]))
FIXED["Anusayavāro."] = C.VARO_CLOSING.format(heading=B.SECTION_HEADINGS["Anusayavāra"])


# ---------------------------------------------------------------------------------------------
# Questions
# ---------------------------------------------------------------------------------------------
def question(q):
    t = C.lower1(q.strip())
    if t.endswith(PE) and t[:-len(PE)] in Q_PE:      # "(Kha) yattha vā pana…pe…?" -> «А где…?»
        return C.KHA_PREFIX + Q_PE[t[:-len(PE)]] + "…?"
    return C.question(q)


# ---------------------------------------------------------------------------------------------
# Answers (7-01's answer_sentence + sabbattha + paṭiloma no-ca + final …pe…)
# ---------------------------------------------------------------------------------------------
RES_HEAD = {k: 0 for k in ("tassa tattha", "tesaṃ tattha", "ettha", "tattha")}
RES_NEG = {k: 0 for k in ("tassa tattha", "tesaṃ tattha", "tassa", "tesaṃ", "tattha")}


def _answer(s):
    if s in C.SIMPLE_ANSWERS:
        return C.SIMPLE_ANSWERS[s]
    assert s.endswith("."), s
    body = C.lower1(s[:-1])
    person, body = C._take(body, C.PERSON_GEN)
    sabb = False
    if body == "sabbattha" or body.startswith("sabbattha "):
        sabb, body = True, body[len("sabbattha"):].lstrip()
    loci = []
    while True:
        loc, body = C._take(body, C.LOCI)
        if not loc:
            break
        loci.append(loc)
    res, body = C._take(body, RES_HEAD)
    main, _, neg = body.partition(", no ca ")

    def res_ru(k):
        r = C.RES[k]
        return C.RES_FEM.get(r, r) if person in C.PERSON_FEM else r

    if sabb:
        assert person and not loci and res is None and not neg, s
        head = f"{C.PERSON_GEN[person]} {SABBATTHA}"
        if not main:                                   # "Arahato sabbattha…pe…." -> «У архата везде…»
            return cap(head) + "."
        head += " "
    elif person and loci:
        assert res in ("tassa tattha", "tesaṃ tattha"), s
        head = C.ANSWER_INTRO_PERSON_PLACE.format(person=C.PERSON_GEN[person],
                                                  loci=C.LOCI_SEP.join(C.LOCI[x] for x in loci), res=res_ru(res))
    elif loci:
        assert res in ("ettha", "tattha"), s
        head = C.ANSWER_INTRO_PLACE.format(loci=C.LOCI_SEP.join(C.LOCI[x] for x in loci), res=C.RES[res])
    elif person:
        assert res is None, s
        head = C.ANSWER_INTRO_PERSON.format(person=C.PERSON_GEN[person])
    else:
        raise ValueError(f"answer intro not parsed: {s!r}")
    out = head + C.clause(main)
    if neg:
        nres, neg = C._take(neg, RES_NEG)
        exp = {(True, True): ("tassa tattha", "tesaṃ tattha"), (False, True): ("tattha",),
               (True, False): ("tassa", "tesaṃ")}[(bool(person), bool(loci))]
        assert nres in exp, s
        segs = C.split_clause(neg, C.VERB)
        assert len(segs) == 1, s
        lst, v = segs[0]
        # "no" negates the verb that follows: no ca … anuseti = не залегает; no ca … nānuseti = залегает
        out += C.no_ca(v, C.parse_list(lst), res_ru(nres))
    return cap(out) + "."


def answer_sentence(s):
    pe = s.endswith(PE + ".")
    if pe:
        s = s[:-len(PE + ".")] + "."
    out = _answer(s)
    if pe:
        assert out.endswith("."), out
        out = out[:-1] + PE_END
    return out


def answers(a):
    sents = re.split(r"(?<=\.) (?=\S)", a.strip())
    return " ".join(answer_sentence(x) for x in sents)


# ---------------------------------------------------------------------------------------------
# Lines (7-01's tr_line with the functions above)
# ---------------------------------------------------------------------------------------------
def tr_line(body):
    if not body.strip():
        return ""
    if body in FIXED:
        return FIXED[body]
    if body.startswith("#"):
        return C.heading(body)
    text = C.preprocess(body)
    tail = ""
    m = C.MULAKA_RE.fullmatch(text)
    if m:
        text, tail = m.group(1), f" ({C.MULAKA[m.group(2)]})"
    label = ""
    m = C.LABEL_RE.fullmatch(text)
    if m and m.group(1) in B.LETTERS:
        label, text = f"({B.LETTERS[m.group(1)]}) ", m.group(2)
    if "?" in text:
        q, _, a = text.partition("?")
        out = label + question(q)
        if a.strip():
            out += " " + answers(a)
    else:
        out = label + answers(text)
    return out + tail


def translate_file(src_text):
    out = []
    for line in src_text.split("\n"):
        body, bid = B.ID_RE.match(line).groups()
        out.append(tr_line(body) + (bid or ""))
    return "\n".join(out)


# ---------------------------------------------------------------------------------------------
# Checks
# ---------------------------------------------------------------------------------------------
CROSSBOOK_02 = [
    ("5", "личность везде обнаруживается"),        # sabbattha = везде
]
FINISHED = ["1-mulayamaka.md", "7-01-anusayayamaka.md"]   # finished pi-6 chapters for the consistency check


def check_crossbook_02():
    cache, missing = {}, []
    for b, s in CROSSBOOK_02:
        if b not in cache:
            cache[b] = "\n".join(p.read_text(encoding="utf-8") for p in sorted(B.RAILS[b].glob("*.md")))
        if s not in cache[b]:
            missing.append((b, s))
    if missing:
        raise AssertionError(f"cross-book strings not found in the pi-1..5 rails: {missing}")
    return True


def seen_from_finished():
    seen = {}
    for name in FINISHED:
        p, r = B.PALI_DIR / name, B.OUT_DIR / name
        if r.exists():
            C.check_consistency(p.read_text(encoding="utf-8"), r.read_text(encoding="utf-8"), seen)
    return seen


def main():
    B.check_crossbook()
    C.check_crossbook_c()
    check_crossbook_02()
    src = (B.PALI_DIR / CHAPTER).read_text(encoding="utf-8")
    ru = unicodedata.normalize("NFC", translate_file(src))
    C.check_consistency(src, ru, seen_from_finished())
    B.check_pair(src, ru, CHAPTER)
    with open(B.OUT_DIR / CHAPTER, "w", encoding="utf-8", newline="\n") as f:
        f.write(ru)
    print("written", B.OUT_DIR / CHAPTER, "lines", len(ru.split("\n")))
    print("cross-book asserts OK; consistency OK; per-line checks OK")


if __name__ == "__main__":
    main()
