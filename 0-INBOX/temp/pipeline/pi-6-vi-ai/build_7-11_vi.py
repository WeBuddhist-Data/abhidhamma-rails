# -*- coding: utf-8 -*-
"""pi-6 (Yamaka) Vietnamese zero-shot, chapter 7-11-anusayayamaka.md: (Kha) dhātuvisajjanāvāro, the close of the
Anusayayamaka.

Imports build_sample_vi (labels, headings, homage, yamaka_end, line checks) and build_7-01_vi (family C: tendency
word, verb «nằm sẵn», planes, headings, repeat check). The dhātu sentences are not covered by 7-01's parser; their
frames are fixed strings here (listed in notes-7-11.md):

    Xdhātuyā cutassa Ydhātuṃ upapajjantassa <answer>; anusayā bhaṅgā natthi.
    Xdhātuyā cutassa Ydhātuyā upapatti nāma natthi, heṭṭhā upapajjamāno kāmadhātuṃyeva upapajjati, satteva …
    (Xdhātumūlakaṃ)

DASH RULE: no dash in this chapter, the frames add none. No quotes.
Importing writes nothing; run  python -I -X utf8 -B build_7-11_vi.py  to rebuild the chapter file.
"""
import importlib
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai")
import build_sample_vi as B  # noqa: E402

A = importlib.import_module("build_7-01_vi")
CH = "7-11-anusayayamaka.md"
cap, low = B.cap, B.low
SLIPS = []

# ================================================================ planes (dhātu = plane «cõi», pi-2; 7-01 PLACE_VI)
PLANE_VI = {
    "kāma": "cõi dục lạc",                  # kāmadhātu (pi-2)
    "rūpa": "cõi hình sắc",                 # rūpadhātu (pi-2)
    "arūpa": "cõi không hình sắc",          # arūpadhātu (pi-2)
}
assert A.PLACE_VI["rūpadhātuyā"] == "trong " + PLANE_VI["rūpa"]
assert A.PLACE_VI["arūpadhātuyā"] == "trong " + PLANE_VI["arūpa"]
assert A.PLACE_VI["kāmadhātuyā dvīsu vedanāsu"].endswith("trong " + PLANE_VI["kāma"])
NOT_ONE = "nơi không phải là {a}"                          # na Xdhātuyā / na Xdhātuṃ
NOT_TWO = "nơi không phải là {a} cũng không phải là {b}"   # na X na Y (2-01 «không phải là A cũng không phải là B»)

ANUSAYA = A.ANUSAYA                                         # anusayā = khuynh hướng tiềm ẩn (7-01)
ANUSENTI = A.VERB["anusenti"]["p"]                          # anusenti = nằm sẵn (7-01)

# ================================================================ sentence frames
# Xdhātuyā cutassa Ydhātuṃ upapajjantassa: the same Pāli as the 7-10 dhātu questions; copied from build_7-10_vi
# CUTA_UPA (7-01 proposal «chết ở cõi dục lạc rồi tái sinh vào cõi hình sắc», pi-5 ^5-65 frame) and asserted
# byte-identical below whenever build_7-10_vi imports.
CUTA_UPA = "Ở người chết ở {c} rồi tái sinh vào {u}"         # Xdhātuyā cutassa Ydhātuṃ upapajjantassa (7-10)
FROM_C = "Ở người chết ở {c}"                               # Xdhātuyā cutassa (no upapajjantassa: upapatti natthi)
assert CUTA_UPA.startswith(FROM_C)
THEN = ", thì "
NUM = {"satta": "bảy", "pañca": "năm", "tayo": "ba"}
KASSACI = "ở một số người, {n} " + ANUSAYA + " " + ANUSENTI  # kassaci N anusayā anusenti
SATTEVA = "đúng bảy " + ANUSAYA + " " + ANUSENTI             # satteva anusayā anusenti
BHANGA = "phải phân chia"                                   # bhaṅgā (7-10 BHANGA; aṭṭhakathā ^6-152 «vibhajitabbā»)
BHANGA_NATTHI = "không có " + ANUSAYA + " nào " + BHANGA      # anusayā bhaṅgā natthi (aṭṭhakathā ^6-154)
NO_UPAPATTI = "không có cái gọi là sự tái sinh vào {y}"      # Ydhātuyā upapatti nāma natthi
HETTHA = "khi tái sinh xuống thấp hơn, người ấy chỉ tái sinh vào " + PLANE_VI["kāma"]
# heṭṭhā upapajjamāno kāmadhātuṃyeva upapajjati
MULAKA_C = "(Phần dựa trên {x})"                            # (Xdhātumūlakaṃ) (7-01 MULAKA «(Phần dựa trên …)»)
assert A.MULAKA["Eka"] == MULAKA_C.format(x="một mục")

PL = "kāma|arūpa|rūpa"


def planes(phrase, case):
    """«kāmadhātuṃ» / «na kāmadhātuṃ» / «na kāmadhātuṃ na arūpadhātuṃ» (case: 'abl' -dhātuyā, 'acc' -dhātuṃ)."""
    end = "dhātuyā" if case == "abl" else "dhātuṃ"
    m = re.fullmatch(rf"(?P<n1>na )?(?P<a>{PL}){end}(?: na (?P<b>{PL}){end})?", low(phrase))
    if not m:
        raise ValueError(f"unparsed planes: {phrase!r}")
    if m["b"]:
        assert m["n1"], phrase
        return NOT_TWO.format(a=PLANE_VI[m["a"]], b=PLANE_VI[m["b"]])
    return NOT_ONE.format(a=PLANE_VI[m["a"]]) if m["n1"] else PLANE_VI[m["a"]]


def answer(s):
    if s == "satteva anusayā anusenti":
        return SATTEVA
    parts = s.split(", ")
    out = []
    for p in parts:
        m = re.fullmatch(r"kassaci (satta|pañca|tayo) anusayā anusenti", p)
        if not m:
            raise ValueError(f"unparsed answer: {s!r}")
        out.append(KASSACI.format(n=NUM[m.group(1)]))
    return ", ".join(out)


SENT_RE = re.compile(rf"(?P<x>(?:[Nn]a )?(?:{PL}|Kāma|Rūpa|Arūpa)dhātuyā(?: na (?:{PL})dhātuyā)?) cutassa "
                     rf"(?P<y>(?:na )?(?:{PL})dhātuṃ(?: na (?:{PL})dhātuṃ)?) upapajjantassa "
                     rf"(?P<ans>.+?); anusayā bhaṅgā natthi\.")
NOUP_RE = re.compile(rf"(?P<x>(?:[Nn]a )?(?:{PL}|Kāma|Rūpa|Arūpa)dhātuyā(?: na (?:{PL})dhātuyā)?) cutassa "
                     rf"(?P<y>(?:na )?(?:{PL})dhātuyā(?: na (?:{PL})dhātuyā)?) upapatti(?P<sp> ?)nāma natthi, "
                     rf"heṭṭhā upapajjamāno kāmadhātuṃyeva upapajjati, (?P<ans>.+?); anusayā bhaṅgā natthi\.")
MULAKA_RE = re.compile(rf"\((?P<c>(?:(?:na|Na)?(?:{PL}|Kāma|Rūpa|Arūpa))+)dhātumūlakaṃ\)")

EXACT = {
    "Dhātuvisajjavāro.": B.SECTION["dhātuvisajjanāvāro"] + ".",   # closing line (spelling -visajja-, as the heading)
    "Anusayayamakaṃ niṭṭhitaṃ.": B.yamaka_end("Anusayayamakaṃ"),
    "Namo tassa bhagavato arahato sammāsambuddhassa": B.HOMAGE,
}


def mulaka(c):
    toks = re.findall(rf"(na)?({PL})", low(c))
    assert "".join(n + p for n, p in toks) == low(c), c
    if len(toks) == 1:
        n, p = toks[0]
        return MULAKA_C.format(x=NOT_ONE.format(a=PLANE_VI[p]) if n else PLANE_VI[p])
    assert len(toks) == 2 and all(n for n, _ in toks), c
    return MULAKA_C.format(x=NOT_TWO.format(a=PLANE_VI[toks[0][1]], b=PLANE_VI[toks[1][1]]))


def translate_sentence(s):
    if s in EXACT:
        return EXACT[s]
    m = MULAKA_RE.fullmatch(s)
    if m:
        return mulaka(m["c"])
    m = SENT_RE.fullmatch(s)
    if m:
        head = CUTA_UPA.format(c=planes(m["x"], "abl"), u=planes(m["y"], "acc"))
        return f"{head}{THEN}{answer(m['ans'])}; {BHANGA_NATTHI}."
    m = NOUP_RE.fullmatch(s)
    if m:
        if not m["sp"]:
            SLIPS.append("upapattināma")
        head = FROM_C.format(c=planes(m["x"], "abl"))
        return (f"{head}{THEN}{NO_UPAPATTI.format(y=planes(m['y'], 'abl'))}, {HETTHA}, {answer(m['ans'])}; "
                f"{BHANGA_NATTHI}.")
    raise ValueError(f"unmatched sentence: {s!r}")


SPLIT_RE = re.compile(r"(?<=[?.])\s+(?=\S)")


def translate_line(line):
    m = re.match(r"^(?P<h>#+ )?(?P<t>.*?)(?P<id> \^[0-9A-Za-z-]+)?$", line)
    h, t, sid = m["h"] or "", m["t"], m["id"] or ""
    if h:
        return h + A.heading(t) + sid
    if t in EXACT:
        return EXACT[t] + sid
    return " ".join(translate_sentence(s) for s in SPLIT_RE.split(t)) + sid


def translate_file(name):
    src = (B.PALI_DIR / name).read_text(encoding="utf-8")
    out = [translate_line(line) if line.strip() else "" for line in src.splitlines()]
    text = "\n".join(out).rstrip("\n") + "\n"
    return re.sub(r"\n{3,}", "\n\n", text)


# ================================================================ cross-book asserts (pi-N rails contain the string)
CROSS_BOOK = [
    ("cõi dục lạc", 2), ("cõi hình sắc", 2), ("cõi không hình sắc", 2), ("ở một số chúng sinh", 2),
    ("khoảnh khắc tái sinh", 2), ("tái sinh vào cõi không hình sắc", 5), ("chết ở cõi hình sắc", 5),
    ("nằm sẵn", 2), (f"bảy {ANUSAYA}", 2), ("không phải là", 1), ("đã hoàn tất", 1), (B.HOMAGE, 1),
]


def check_cross_book():
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md")))
             for b, d in B.RAILS_DIR.items()}
    missing = [(s, b) for s, b in CROSS_BOOK if s not in texts[b]]
    for s, b in missing:
        print(f"CROSS-BOOK MISSING in pi-{b}: {s}")
    assert not missing, f"{len(missing)} cross-book strings not found"
    print(f"cross-book asserts: {len(CROSS_BOOK)} strings found in pi-1..5 rails")


def check_repeats(pali):
    """Identical Pāli sentence -> identical Vietnamese sentence (within the chapter)."""
    seen, bad = {}, 0
    for p in [ln for ln in pali.splitlines() if ln.strip() and not ln.startswith("#")]:
        p = re.sub(r"\s*\^[\w-]+$", "", p)
        for s in SPLIT_RE.split(p):
            t = translate_sentence(s.replace("upapattināma", "upapatti nāma"))
            if seen.setdefault(s.replace("upapattināma", "upapatti nāma"), t) != t:
                bad += 1
    return bad


def check_frames(text):
    """Every cutassa sentence starts with FROM_C, every one ends with BHANGA_NATTHI; no Latin left."""
    body = [ln for ln in text.splitlines() if ln.strip() and not ln.startswith("#")]
    n_from = sum(ln.count(FROM_C.format(c="")) for ln in body)
    n_end = sum(ln.count(f"; {BHANGA_NATTHI}.") for ln in body)
    return n_from, n_end


def check_7_10():
    """Same Pāli as the 7-10 dhātu questions -> same Vietnamese (only when build_7-10_vi imports)."""
    try:
        T = importlib.import_module("build_7-10_vi")
    except Exception as e:  # noqa: BLE001  (7-10 may be unfinished)
        print("build_7-10_vi not importable, frames copied as read:", type(e).__name__)
        return
    pairs = [(CUTA_UPA, T.CUTA_UPA), (NOT_ONE.format(a="{p}"), T.NOT_ONE),
             (NOT_TWO.format(a="{p1}", b="{p2}"), T.NOT_TWO), (MULAKA_C.format(x="{p}"), T.MULAKA_DHATU),
             (BHANGA, T.BHANGA), (PLANE_VI, T.PLANE)]
    bad = [p for p in pairs if p[0] != p[1]]
    assert not bad, f"frames differ from build_7-10_vi: {bad}"
    for c in ("(Kāmadhātumūlakaṃ)", "(Nakāmanaarūpadhātumūlakaṃ)", "(Narūpanaarūpadhātumūlakaṃ)"):
        assert translate_sentence(c) == T.translate_sentence(c), c
    print("7-10 frames: byte-identical (CUTA_UPA, NOT_ONE, NOT_TWO, MULAKA, BHANGA, PLANE)")


def main():
    A.check_cross_book()
    check_cross_book()
    check_7_10()
    SLIPS.clear()
    text = unicodedata.normalize("NFC", translate_file(CH))
    pali = (B.PALI_DIR / CH).read_text(encoding="utf-8")
    probs = B.check_lines(pali, text, CH)
    assert check_repeats(pali) == 0, "identical Pāli rendered differently"
    n_from, n_end = check_frames(text)
    p_from, p_end = pali.count("cutassa "), pali.count("; anusayā bhaṅgā natthi.")
    assert (n_from, n_end) == (p_from, p_end), ((n_from, n_end), (p_from, p_end))
    assert "–" not in text and "—" not in text
    with open(B.OUT_DIR / CH, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    segs = len(re.findall(r"\^[0-9A-Za-z-]+\s*$", text, flags=re.M))
    print(f"wrote {CH}: {len([ln for ln in text.splitlines() if ln.strip()])} lines, {segs} segments, "
          f"{n_from} dhātu sentences")
    print("source slips rendered as meant:", sorted(set(SLIPS)))
    for p in probs[:80]:
        print("PROBLEM", p)
    print("line checks:", "OK" if not probs else f"{len(probs)} problems")
    sys.exit(1 if probs else 0)


if __name__ == "__main__":
    main()
