# -*- coding: utf-8 -*-
"""pi-6 (Yamaka) Vietnamese zero-shot, chapter 7-02-anusayayamaka.md (Anusayavāra, paṭiloma: nānuseti).

Every frame comes VERBATIM from the family-C frame-setter build_7-01_vi (imported, nothing redefined):
question(), statement(), parse_statement(), tl(), VERB (nānuseti / nānusenti = «không nằm sẵn»,
no ca … nānuseti = «vẫn nằm sẵn»), PERSON_VI (Arahato), PLACE_VI (apariyāpanne, sabbattha), headings, MULAKA.
This builder only adds the «…pe…» shortenings 7-01 did not meet (listed in notes-7-02.md):

    <statement>…pe….  /  <statement> …pe….   = <statement>…            (the clause, then «…», no final «.»)
    <person> sabbattha…pe….                    = <person>, ở mọi nơi…     (the head of the statement, then «…»)
    Āmantā …pe….                               = Đúng vậy…
    (Kha) yattha vā pana…pe…?                  = (b) Còn ở nơi nào… không?   (sample: «…?» = «… không?»)

DASH RULE: no dash in the Pāli of this chapter; the frames add none. No quotes.
Importing writes nothing; run  python -I -X utf8 -B build_7-02_vi.py  to rebuild the chapter file.
"""
import importlib
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai")
A = importlib.import_module("build_7-01_vi")   # family C frames (7-01)
B = A.B                                        # build_sample_vi

CH = "7-02-anusayayamaka.md"
PE = A.PE                                      # …pe… = … (sample rule)

# ================================================================ «…pe…» shortenings (new in 7-02)
PE_END_RE = re.compile(r"(?P<base>.+?) ?…pe…\.")                       # <statement>…pe…. / <statement> …pe….
PE_HEAD_RE = re.compile(rf"(?P<per>{A.PERSON_RE}) (?P<pl>sabbattha)…pe…\.")   # Arahato sabbattha…pe….
AMANTA_PE = A.AMANTA.rstrip(".") + PE                                   # Āmantā …pe…. = Đúng vậy…
Q_PE_KHA = "{label} " + B.cap(A.VA_PANA + "{rel}" + PE + " không?")     # (Kha) yattha vā pana…pe…?
Q_PE_RE = re.compile(r"\((?P<l>Ka|Kha)\) (?P<y>yassa yattha|yassa|yattha) vā pana…pe…\?")
SPACED_PE = []                                                          # « …pe….» with a space (reported)


def pe_head(per, places):
    """Head of a statement cut short by …pe…: «Ở bậc A-la-hán, ở mọi nơi…»."""
    return ", ".join([A.PERSON_VI[per]] + [A.PLACE_VI[p] for p in places]) + PE


def translate_sentence(s):
    if s == "Āmantā …pe….":
        return AMANTA_PE
    m = Q_PE_RE.fullmatch(s)
    if m:
        return Q_PE_KHA.format(label=B.LABEL[m["l"]], rel=A.REL_VI[m["y"]])
    m = PE_HEAD_RE.fullmatch(s)
    if m:
        per = next(k for k in A.PERSON_VI if k.lower() == m["per"].lower())
        return pe_head(per, [m["pl"]])
    m = PE_END_RE.fullmatch(s)
    if m:
        if s.endswith(" …pe…."):
            SPACED_PE.append(s)
        v = A.parse_statement(m["base"] + ".")
        assert v.endswith(".")
        return v[:-1] + PE
    return A.translate_sentence(s)


def translate_line(line):
    m = re.match(r"^(?P<h>#+ )?(?P<t>.*?)(?P<id> \^[0-9A-Za-z-]+)?$", line)
    h, t, sid = m["h"] or "", m["t"], m["id"] or ""
    if h:
        return h + A.heading(t) + sid
    if t in A.EXACT:
        return A.EXACT[t] + sid
    return " ".join(translate_sentence(s) for s in A.SPLIT_RE.split(t)) + sid


def translate_file(name):
    src = (B.PALI_DIR / name).read_text(encoding="utf-8")
    out = [translate_line(line) if line.strip() else "" for line in src.splitlines()]
    text = "\n".join(out).rstrip("\n") + "\n"
    return re.sub(r"\n{3,}", "\n\n", text)


# ================================================================ checks
def check_repeats(pali):
    """Identical Pāli sentence -> identical Vietnamese sentence, within 7-02 and with 7-01."""
    seen, bad = {}, 0
    for name, tr in ((A.CH, A.translate_sentence), (CH, translate_sentence)):
        txt = pali if name == CH else (B.PALI_DIR / name).read_text(encoding="utf-8")
        for p in txt.splitlines():
            if not p.strip() or p.startswith("#"):
                continue
            p = re.sub(r"\s*\^[\w-]+$", "", p)
            if p in A.EXACT:
                continue
            for s in A.SPLIT_RE.split(p):
                t = tr(s)
                if seen.setdefault(s, t) != t:
                    print("REPEAT MISMATCH", s)
                    bad += 1
    return bad


def check_vs_7_01_output():
    """Every Vietnamese sentence 7-01 produced for a Pāli sentence also met here is byte-identical."""
    vi01 = (B.OUT_DIR / A.CH).read_text(encoding="utf-8")
    pa01 = (B.PALI_DIR / A.CH).read_text(encoding="utf-8")
    ok = 0
    assert len([ln for ln in pa01.splitlines() if ln.strip()]) == len([ln for ln in vi01.splitlines() if ln.strip()])
    for p, v in zip([ln for ln in pa01.splitlines() if ln.strip()], [ln for ln in vi01.splitlines() if ln.strip()]):
        if p.startswith("#"):
            assert translate_line(p) == v, f"heading differs from 7-01 output: {p!r}"
            ok += 1
            continue
        assert translate_line(p) == v, f"7-01 line differs: {p!r}"
        ok += 1
    return ok


def main():
    A.check_cross_book()
    A.SLIPS.clear()
    n01 = check_vs_7_01_output()
    print(f"7-01 output lines reproduced byte-identically by this builder: {n01}")
    A.SLIPS.clear()
    SPACED_PE.clear()
    text = unicodedata.normalize("NFC", translate_file(CH))
    slips = sorted(set(A.SLIPS))
    pali = (B.PALI_DIR / CH).read_text(encoding="utf-8")
    probs = B.check_lines(pali, text, CH)
    # labels come only from B.LABEL (now (a)(b)(c)(d)(đ)(e)(g)(h)); the filter below is kept for an old «(f)» label
    # and accepts it only when the line without «(f)» is clean (same rule as 7-04); it matches nothing in 7-02 now
    vl = [ln for ln in text.splitlines() if ln.strip()]
    probs = [p for p in probs if not (p.endswith("foreign letter 'f'") and not B.FOREIGN.search(
        B._strip(vl[int(re.search(r"line (\d+):", p).group(1)) - 1].replace("(f)", ""))))]
    assert check_repeats(pali) == 0, "identical Pāli rendered differently"
    with open(B.OUT_DIR / CH, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    segs = len(re.findall(r"\^[0-9A-Za-z-]+\s*$", text, flags=re.M))
    print(f"wrote {CH}: {len([ln for ln in text.splitlines() if ln.strip()])} lines, {segs} segments")
    print("source slips rendered as meant (7-02):", slips)
    print("« …pe….» with a space before it (rendered «…» attached):", len(SPACED_PE))
    for p in probs[:80]:
        print("PROBLEM", p)
    print("line checks:", "OK" if not probs else f"{len(probs)} problems")
    sys.exit(1 if probs else 0)


if __name__ == "__main__":
    main()
