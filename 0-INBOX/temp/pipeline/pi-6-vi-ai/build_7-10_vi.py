# -*- coding: utf-8 -*-
"""pi-6 (Yamaka) Vietnamese zero-shot, chapter 7-10-anusayayamaka.md.

Contents: Pahīnavāra paṭiloma (appahīno, place and person / place: ^6-7-308 … ^6-7-329), Uppajjanavāro
(^6-7-330 … ^6-7-331), (Ka) dhātupucchāvāro (^6-7-332 … ^6-7-340).

Frames come VERBATIM from the family-C frame-setter build_7-01_vi (question(), statement(), tl(), VERB, PERSON_VI,
PLACE_VI, headings, MULAKA, VARE_DIR) and from build_7-09_vi (na vattabbo, «; » clauses, «Āmantā …pe….»,
«<statement> …pe….»), whose sentence parser this builder calls unchanged for every pahīna / uppajjati sentence.
New here (listed in notes-7-10.md):

    (vitthāretabbaṃ) / (Vitthāretabbaṃ).          = (nên được trình bày chi tiết) / (Nên được trình bày chi tiết).
    Pahīnavāro. / Uppajjanavāro. / Dhātupucchāvāro. = the 7-01 section headings + «.»
    <P1>yā cutassa <P2>ṃ upapajjantassa kati anusayā anusenti, kati anusayā nānusenti, kati anusayā bhaṅgā?
        = Ở người chết ở <P1> rồi tái sinh vào <P2>, bao nhiêu khuynh hướng tiềm ẩn nằm sẵn, bao nhiêu khuynh
          hướng tiềm ẩn không nằm sẵn, bao nhiêu khuynh hướng tiềm ẩn phải phân chia?
    na <P> = nơi không phải là <P>; na <P1> na <P2> = nơi không phải là <P1> cũng không phải là <P2>
    (<X>dhātumūlakaṃ) = (Phần dựa trên <X>)

DASH RULE: no dash in the Pāli of this chapter; the frames add none. Quotes: the Pāli "pahīno"ti -> “…” (outer).
Importing writes nothing; run  python -I -X utf8 -B build_7-10_vi.py  to rebuild the chapter file.
"""
import importlib
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai")
import build_sample_vi as B  # noqa: E402

A = importlib.import_module("build_7-01_vi")   # family C frames (7-01)
P9 = importlib.import_module("build_7-09_vi")  # pahīna frames: na vattabbo, «; » clauses, …pe… (7-09)

CH = "7-10-anusayayamaka.md"
cap, low = B.cap, B.low
SLIPS = []

# ================================================================ closing lines
EXACT = {
    "Pahīnavāro.": A.SECTION["Pahīnavāro"] + ".",            # Mục về những gì đã được dứt bỏ. (7-04 «Sānusayavāro.» shape)
    "Uppajjanavāro.": A.SECTION["Uppajjanavāro"] + ".",      # Mục về sự sinh khởi. (7-01 proposed heading)
    "Dhātupucchāvāro.": cap(A.SECTION["dhātupucchāvāro"]) + ".",   # Mục hỏi theo các yếu tố. (7-01 proposed heading)
}

# ================================================================ (vitthāretabbaṃ)
VITTH = "(nên được trình bày chi tiết)"
# vitthāretabbaṃ: pi-5 «(evaṃ sabbaṃ vitthāretabbaṃ)» = «(tất cả nên được trình bày chi tiết như vậy)»,
# pi-2 «… vitthāretabbā» = «… cũng nên được trình bày chi tiết …»
VITTH_CAP = "(" + cap(VITTH[1:])                             # (Vitthāretabbaṃ). = (Nên được trình bày chi tiết).
VITTH_END_RE = re.compile(r"(?P<base>.+?) \(vitthāretabbaṃ\)\.")

# ================================================================ dhātupucchāvāro
PLANE = {"kāma": "cõi dục lạc", "rūpa": "cõi hình sắc", "arūpa": "cõi không hình sắc"}
# kāmadhātu / rūpadhātu / arūpadhātu (plane) = 7-01 PLACE_VI «trong cõi …» (pi-2)
NOT_ONE = "nơi không phải là {p}"                            # na kāmadhātuṃ (2-01 «không phải là», nouns)
NOT_TWO = "nơi không phải là {p1} cũng không phải là {p2}"   # na kāmadhātuṃ na arūpadhātuṃ (2-01 «không phải là A cũng không phải là B»)
CUTA_UPA = "Ở người chết ở {c} rồi tái sinh vào {u}"         # <P1>yā cutassa <P2>ṃ upapajjantassa
# 7-01 proposal «Kāmadhātuyā cuto … rūpadhātuṃ upapajjati = chết ở cõi dục lạc rồi tái sinh vào cõi hình sắc» (pi-5 frame)
BHANGA = "phải phân chia"
# bhaṅgā: aṭṭhakathā ^6-152 «kati anusayā bhaṅgāti kati anusayā anusenti nānusentīti evaṃ vibhajitabbāti attho»
# (= how many are to be divided into «lies latent / does not lie latent»); 7-11 «anusayā bhaṅgā natthi»
KATI = ("bao nhiêu {an} {v1}, bao nhiêu {an} {v2}, bao nhiêu {an} " + BHANGA)
# kati anusayā anusenti, kati anusayā nānusenti, kati anusayā bhaṅgā
# (pi-2 ^2-151 «… kati kusalā, kati akusalā …?» = «…, bao nhiêu khối là thiện, bao nhiêu khối là bất thiện …?»)
DHATU_Q = CUTA_UPA + ", " + KATI + "{end}"
MULAKA_DHATU = "(Phần dựa trên {p})"                          # (<X>dhātumūlakaṃ) (7-01 «(Phần dựa trên một mục)»)

PL_RE = r"(?:na )?(?:kāma|arūpa|rūpa)dhātu{c}(?: na (?:kāma|arūpa|rūpa)dhātu{c})?"
DHATU_RE = re.compile(
    rf"(?P<c>{PL_RE.format(c='yā')}) cutassa (?P<u>{PL_RE.format(c='ṃ')}) upapajjantassa "
    rf"kati anusayā anusenti, kati anusayā nānusenti, kati anusayā bhaṅgā(?P<end>[?.])")
MULAKA_DHATU_RE = re.compile(r"\((?P<x>(?:(?:Na|na)?(?:kāma|Kāma|arūpa|Arūpa|rūpa|Rūpa))+)dhātumūlakaṃ\)")


def plane_phrase(pairs):
    """[(neg, plane), …] -> Vietnamese place phrase."""
    if len(pairs) == 1:
        neg, p = pairs[0]
        return NOT_ONE.format(p=PLANE[p]) if neg else PLANE[p]
    (n1, p1), (n2, p2) = pairs
    assert n1 and n2, pairs
    return NOT_TWO.format(p1=PLANE[p1], p2=PLANE[p2])


def planes_of(pali):
    """«na kāmadhātuyā na arūpadhātuyā» / «rūpadhātuṃ» -> [(True, 'kāma'), (True, 'arūpa')] / [(False, 'rūpa')]."""
    return [(bool(n), p) for n, p in re.findall(r"(na )?(kāma|arūpa|rūpa)dhātu", pali)]


def dhatu_question(m):
    if m["end"] == ".":
        SLIPS.append("question ending in «.» (kept as written): «… kati anusayā bhaṅgā.» in " + m.group(0)[:50])
    an = A.ANUSAYA
    return DHATU_Q.format(c=plane_phrase(planes_of(m["c"])), u=plane_phrase(planes_of(m["u"])), an=an,
                          v1=A.VERB["anusenti"]["p"], v2=A.VERB["nānusenti"]["p"], end=m["end"])


def mulaka_dhatu(m):
    x = m["x"].lower()
    pairs = [(bool(n), p) for n, p in re.findall(r"(na)?(kāma|arūpa|rūpa)", x)]
    assert "".join(("na" if n else "") + p for n, p in pairs) == x, x
    return MULAKA_DHATU.format(p=plane_phrase(pairs))


# ================================================================ sentences and lines
def translate_sentence(s):
    if s in EXACT:
        return EXACT[s]
    if s == "(Vitthāretabbaṃ).":
        return VITTH_CAP + "."
    m = VITTH_END_RE.fullmatch(s)
    if m:
        v = P9.translate_sentence(m["base"] + ".")
        assert v.endswith("."), v
        return v[:-1] + " " + VITTH + "."
    m = DHATU_RE.fullmatch(low(s))
    if m:
        return dhatu_question(m)
    m = MULAKA_DHATU_RE.fullmatch(s)
    if m:
        return mulaka_dhatu(m)
    return P9.translate_sentence(s)       # pahīna / uppajjati sentences, Āmantā, Natthi, (…mūlakaṃ), <X>vāre paṭilomaṃ.


def translate_line(line):
    m = re.match(r"^(?P<h>#+ )?(?P<t>.*?)(?P<id> \^[0-9A-Za-z-]+)?$", line)
    h, t, sid = m["h"] or "", m["t"], m["id"] or ""
    if h:
        return h + A.heading(t) + sid
    if re.fullmatch(r"\d+", t):           # ^6-7-311: a bare «9» line (digits stay)
        SLIPS.append(f"bare number line «{t}{sid}» (kept)")
        return t + sid
    return " ".join(translate_sentence(s) for s in A.SPLIT_RE.split(t)) + sid


def translate_file(name):
    src = (B.PALI_DIR / name).read_text(encoding="utf-8")
    out = [translate_line(line) if line.strip() else "" for line in src.splitlines()]
    text = "\n".join(out).rstrip("\n") + "\n"
    return re.sub(r"\n{3,}", "\n\n", text)


# ================================================================ checks
CROSS_BOOK = [
    ("nên được trình bày chi tiết", 5), ("nên được trình bày chi tiết", 2),
    ("chết ở cõi hình sắc rồi tái sinh vào cõi không hình sắc", 5), ("bao nhiêu", 2), ("bao nhiêu khối là thiện", 2), ("phân chia", 5),
    ("cõi dục lạc", 2), ("cõi hình sắc", 2), ("cõi không hình sắc", 2), ("không phải là", 1),
    ("đã được dứt bỏ", 5), ("chưa được dứt bỏ", 5), ("không nên nói", 1), ("sinh khởi", 1),
    ("bậc không trở lại", 4), ("bậc A-la-hán", 5), ("người phàm phu", 4), ("ba hạng người", 4),
    ("bốn hạng người", 4), ("hai hạng người", 4), ("Đúng vậy.", 5), ("Không có.", 3),
]


def check_cross_book():
    P9.check_cross_book()                 # 7-01 + 7-09 asserts
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md")))
             for b, d in B.RAILS_DIR.items()}
    missing = [(s, b) for s, b in CROSS_BOOK if s not in texts[b]]
    for s, b in missing:
        print(f"CROSS-BOOK MISSING in pi-{b}: {s}")
    assert not missing, f"{len(missing)} cross-book strings not found"
    print(f"cross-book asserts (7-10): {len(CROSS_BOOK)} strings found in pi-1..5 rails")


def sentences(pali):
    for p in pali.splitlines():
        if not p.strip() or p.startswith("#"):
            continue
        p = re.sub(r"\s*\^[\w-]+$", "", p)
        if re.fullmatch(r"\d+", p):
            continue
        yield from A.SPLIT_RE.split(p)


def check_repeats(pali):
    """Identical Pāli sentence -> identical Vietnamese sentence (within the chapter)."""
    seen, bad = {}, 0
    for s in sentences(pali):
        t = translate_sentence(s)
        if seen.setdefault(s, t) != t:
            print("REPEAT MISMATCH", s)
            bad += 1
    return bad


def check_vs_7_09_parser(pali):
    """Every sentence the 7-09 parser also handles gets exactly its Vietnamese."""
    same = 0
    for s in set(sentences(pali)):
        try:
            v9 = P9.translate_sentence(s)
        except Exception:                 # vitthāretabbaṃ, closing lines, dhātu questions: not covered by 7-09
            continue
        assert v9 == translate_sentence(s), f"differs from the 7-09 parser: {s!r}"
        same += 1
    return same


def check_vs_finished(pali_lines, vi_lines):
    """Identical Pāli lines / sentences in the finished anusaya chapters 7-01 … 7-09 -> identical Vietnamese."""
    strip = lambda ln: re.sub(r"\s*\^[\w-]+$", "", ln)      # noqa: E731
    known_l, used = {}, []
    for n in range(1, 10):
        ch = f"7-0{n}-anusayayamaka.md"
        if not (B.OUT_DIR / ch).exists():
            continue
        pl = [ln for ln in (B.PALI_DIR / ch).read_text(encoding="utf-8").splitlines() if ln.strip()]
        vl = [ln for ln in (B.OUT_DIR / ch).read_text(encoding="utf-8").splitlines() if ln.strip()]
        if len(pl) != len(vl):
            print(f"skipped {ch} (line counts differ: unfinished?)")
            continue
        used.append(ch)
        for p, v in zip(pl, vl):
            known_l.setdefault(strip(p), set()).add(strip(v))
    hits = 0
    for p, v in zip(pali_lines, vi_lines):
        k = strip(p)
        if k in known_l:
            assert known_l[k] == {strip(v)}, f"differs from a finished chapter: {p!r} {known_l[k]} vs {strip(v)!r}"
            hits += 1
    return hits, used


def check_vs_7_11(pali):
    """The dhātu frames shared with 7-11 (same Pāli: cutassa / upapajjantassa, planes, bhaṅgā, mūlaka) agree byte for
    byte with build_7-11_vi (checked only when it imports)."""
    try:
        E = importlib.import_module("build_7-11_vi")
    except Exception as exc:                 # noqa: BLE001
        print("build_7-11_vi not importable, frames not compared:", exc)
        return 0
    assert E.CUTA_UPA == CUTA_UPA and E.BHANGA == BHANGA and E.PLANE_VI == PLANE
    assert E.NOT_ONE.format(a="X") == NOT_ONE.format(p="X")
    assert E.NOT_TWO.format(a="X", b="Y") == NOT_TWO.format(p1="X", p2="Y")
    n = 0
    for s in set(sentences(pali)):
        m = DHATU_RE.fullmatch(low(s))
        if m:
            assert E.planes(m["c"], "abl") == plane_phrase(planes_of(m["c"])), s
            assert E.planes(m["u"], "acc") == plane_phrase(planes_of(m["u"])), s
            n += 1
        m = MULAKA_DHATU_RE.fullmatch(s)
        if m:
            assert E.mulaka(m["x"]) == mulaka_dhatu(m), s
            n += 1
    return n


def main():
    check_cross_book()
    SLIPS.clear()
    A.SLIPS.clear()
    P9.SLIPS.clear()
    text = unicodedata.normalize("NFC", translate_file(CH))
    pali = (B.PALI_DIR / CH).read_text(encoding="utf-8")
    probs = B.check_lines(pali, text, CH)
    assert check_repeats(pali) == 0, "identical Pāli rendered differently"
    n9 = check_vs_7_09_parser(pali)
    pl = [ln for ln in pali.splitlines() if ln.strip()]
    vl = [ln for ln in text.splitlines() if ln.strip()]
    nf, used = check_vs_finished(pl, vl)
    n11 = check_vs_7_11(pali)
    print(f"dhātu frames identical with build_7-11_vi: {n11} sentences")
    for bad in ("….", ".…", "?…", ",…", "  ", "là là", '"', "—", "–", "(f)"):
        assert bad not in text, bad
    assert text.count("“") == text.count("”") and "‘" not in text
    with open(B.OUT_DIR / CH, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    segs = len(re.findall(r"\^[0-9A-Za-z-]+\s*$", text, flags=re.M))
    print(f"wrote {CH}: {len(vl)} lines, {segs} segments")
    print(f"sentences identical with the 7-09 parser: {n9}; lines identical with finished chapters: {nf} ({used})")
    print("source notes:")
    for s in sorted(set(SLIPS + A.SLIPS + P9.SLIPS)):
        print("  ", s)
    for p in probs[:80]:
        print("PROBLEM", p)
    print("line checks:", "OK" if not probs else f"{len(probs)} problems")
    sys.exit(1 if probs else 0)


if __name__ == "__main__":
    main()
