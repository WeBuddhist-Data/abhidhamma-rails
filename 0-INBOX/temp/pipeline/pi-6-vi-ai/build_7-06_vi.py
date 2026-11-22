# -*- coding: utf-8 -*-
"""pi-6 (Yamaka) Vietnamese zero-shot, chapter 7-06-anusayayamaka.md (Pajahanavāra, paṭiloma: nappajahati).

Family C frames come VERBATIM from the frame-setter build_7-01_vi (tendencies tl(), question_yo() with
YO_VERB["nappajahati"] = «không dứt bỏ {t}» / no ca … = «vẫn dứt bỏ {t}», places PLACE_VI, headings, mūlaka labels,
VARE_DIR). The answer frames, the demonstratives tato / so tato / te tato and the nominative persons
(Sveva puggalo …) are byte-identical with build_7-04_vi (imported; main() asserts it), the «…pe….» endings too.
New here (listed in notes-7-06.md): the path persons (Aggamaggasamaṅgī, Anāgāmimaggasamaṅgī, Aṭṭhamako), the
«X ṭhapetvā avasesā puggalā» exclusion frame, «no ca so» = «nhưng người ấy», the accusative «-ānusayañca» lists.

DASH RULE: no dash in this chapter, the frames add none. No quotes.
Importing writes nothing; run  python -I -X utf8 -B build_7-06_vi.py  to rebuild the chapter file.
"""
import importlib
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai")
import build_sample_vi as B  # noqa: E402

A = importlib.import_module("build_7-01_vi")     # family C frame-setter
N4 = importlib.import_module("build_7-04_vi")    # nominative persons, answer frames (yo / so chapters)

CH = "7-06-anusayayamaka.md"
cap, low = B.cap, B.low
SLIPS = []

# ================================================================ tendency lists (accusative «-ānusayañca» = «-ānusayaṃ ca»)
CA_RE = re.compile(r"ānusayañca\b")


def tl(phrase):
    return A.tl(CA_RE.sub("ānusayaṃ ca", phrase))


# ================================================================ persons as subjects (nominative)
MAGGI = "người có được con đường"                  # maggasamaṅgī (pi-5 ^5 18 «người có được con đường»; pi-4 plural)
AGGA = f"{MAGGI} tối thượng"                        # aggamaggasamaṅgī (= 7-05 «Người có được con đường tối thượng»)
ANAGAMI_M = f"{MAGGI} không trở lại"                # anāgāmimaggasamaṅgī (pi-2 / pi-5 «con đường không trở lại»)
ATTHAMAKA = "người thứ tám"                         # aṭṭhamako (pi-5 Aṭṭhamakakathā «người thứ tám»)
EXCLUDED_VI = {                                     # X ṭhapetvā (accusative)
    "Dvinnaṃ maggasamaṅgīnaṃ": f"hai {MAGGI}",
    "Dvinnaṃ maggasamaṅgīnañca aṭṭhamakañca": f"hai {MAGGI} và {ATTHAMAKA}",
    "Anāgāmimaggasamaṅgiṃ": ANAGAMI_M,
    "Aggamaggasamaṅgiṃ": AGGA,
    "Anāgāmimaggasamaṅgiñca aṭṭhamakañca": f"{ANAGAMI_M} và {ATTHAMAKA}",
    "Aggamaggasamaṅgiñca aṭṭhamakañca": f"{AGGA} và {ATTHAMAKA}",
}
EXCEPT = "Ngoại trừ {x}, những hạng người còn lại"   # X ṭhapetvā avasesā puggalā (pi-1 «Ngoại trừ …, … còn lại»)
PERSON_NOM_VI = dict(N4.PERSON_NOM_VI)              # Sveva puggalo = Chính hạng người ấy … (7-04 verbatim)
PERSON_NOM_VI.update({
    "Aggamaggasamaṅgī": cap(AGGA),
    "Anāgāmimaggasamaṅgī": cap(ANAGAMI_M),
    "Aṭṭhamako": cap(ATTHAMAKA),
})
PERSON_NOM_VI.update({f"{k} ṭhapetvā avasesā puggalā": EXCEPT.format(x=v) for k, v in EXCLUDED_VI.items()})
PERSONS = sorted(PERSON_NOM_VI, key=len, reverse=True)

# ================================================================ places (7-01 PLACE_VI verbatim)
PLACE_VI = dict(A.PLACE_VI)
PLACES = sorted(PLACE_VI, key=len, reverse=True)

# ================================================================ demonstratives of the answers (7-04 RES_VI + «so»)
RES_VI = dict(N4.RES_VI)                            # tato / so tato / te tato
DEM_VI = dict(RES_VI, so=A.YO_DEM_VI["so"])         # no ca so = nhưng người ấy (7-01 YO_DEM_VI «người ấy»)
NAP = A.YO_VERB["nappajahati"]                      # p = «không dứt bỏ {t}», no = «vẫn dứt bỏ {t}» (7-01)
V_RE = "nappajahati|nappajahanti"                   # nappajahanti (plural) = same Vietnamese

# ================================================================ answer frames (= 7-04)
BUT_C = N4.BUT_C                    # "{pa}, nhưng {dem}{no}"
BOTH_C = N4.BOTH_C                  # "{pa}, đồng thời cũng {pb}"
STATEMENT_RES = N4.STATEMENT_RES    # "{head}, thì {res} {clause}."
STATEMENT_PLACE = N4.STATEMENT_PLACE  # "{head}, {clause}."
STATEMENT_PERSON = N4.STATEMENT_PERSON  # "{head} {clause}."

BUT_RE = re.compile(rf"(?P<a>.+?) (?P<va>{V_RE}), no ca (?:(?P<dem>so tato|te tato|tato|so) )?"
                    rf"(?P<b>.+?) (?P<vb>{V_RE})")
BOTH_RE = re.compile(rf"(?P<a>.+? ?ca) (?P<va>{V_RE})(?P<comma>,?) (?P<b>.+? ?ca) (?P<vb>{V_RE})")


def lower1(s):
    return s[:1].lower() + s[1:]


def pv(phrase):
    return NAP["p"].format(t=tl(phrase))


def clause_of(body, s):
    body = CA_RE.sub("ānusayaṃ ca", body)
    m = BUT_RE.fullmatch(body)
    if m:
        dem = DEM_VI[m["dem"]] + " " if m["dem"] else ""
        return BUT_C.format(pa=pv(m["a"]), dem=dem, no=NAP["no"].format(t=tl(m["b"])))
    m = BOTH_RE.fullmatch(body)
    if m:
        if m["comma"]:
            SLIPS.append("comma inside «A ca nappajahati B ca nappajahati» (rendered with the usual frame): " + s[-90:])
        return BOTH_C.format(pa=pv(m["a"]), pb=pv(m["b"]))
    raise ValueError(f"unparsed clause: {s!r}")


def parse_statement(s):
    assert s.endswith(".") and not s.endswith(".."), s
    t = s[:-1]
    per = next((k for k in PERSONS if t.startswith(k + " ")), None)
    if per:
        t = t[len(per) + 1:]
    places = []
    while True:
        hit = next((p for p in PLACES if lower1(t).startswith(p + " ")), None)
        if not hit:
            break
        places.append(hit)
        t = t[len(hit) + 1:]
    res = next((r for r in ("so tato", "te tato", "tato") if t.startswith(r + " ")), None)
    if res:
        t = t[len(res) + 1:]
    clause = clause_of(t, s)
    head = ", ".join(([PERSON_NOM_VI[per]] if per else []) + [PLACE_VI[p] for p in places])
    if res:
        assert head, s
        return cap(STATEMENT_RES.format(head=head, res=RES_VI[res], clause=clause))
    if places:
        return cap(STATEMENT_PLACE.format(head=head, clause=clause))
    assert per, s
    return cap(STATEMENT_PERSON.format(head=head, clause=clause))


def parse_answer(s):
    """A statement; «X; apariyāpanne tato Y.» (^6-7-180, a semicolon between two clauses) keeps its «;»."""
    if "; " in s:
        first, second = s.split("; ")
        return parse_statement(first + ".")[:-1] + "; " + lower1(parse_statement(second))
    return parse_statement(s)


# ================================================================ questions (7-01 question_yo verbatim)
Q_RE = re.compile(rf"(?:\((?P<l>Ka|Kha)\) )?(?P<y1>[Yy]o|[Yy]ato)(?P<vp> vā pana)?(?P<y2> yato)? "
                  rf"(?P<a>.+?) nappajahati (?P<d>so tato|so|tato) (?P<b>.+?) ?nappajahatīti\?")

# ================================================================ closing lines, «…pe….» endings (= 7-04)
EXACT = {"Pajahanavāro.": A.SECTION["Pajahanavāro"] + "."}      # Pajahanavāro. = Mục về sự dứt bỏ.
VARE_SLIP = {"Pajahanāvāre paṭilomaṃ.": "Pajahanavāre paṭilomaṃ."}   # ^6-7-197 «Pajahanāvāre» (slip, as meant)
PE_END_RE = N4.PE_END_RE                                        # «… nappajahanti …pe….», «Āmantā …pe….»
PE = A.PE                                                       # …pe… = …


def translate_sentence(s):
    m = PE_END_RE.fullmatch(s)
    if m:
        out = translate_sentence(m["s"] + ".")
        assert out.endswith("."), out
        return out[:-1] + PE                                    # «….» is never written: the period gives way to «…»
    if s in EXACT:
        return EXACT[s]
    if s in VARE_SLIP:
        SLIPS.append(f"{s} = {VARE_SLIP[s]}")
        s = VARE_SLIP[s]
    m = Q_RE.fullmatch(s)
    if m:
        y1 = m["y1"].lower()
        rel = "yo yato" if m["y2"] else y1
        exp = {"yo": "so", "yato": "tato", "yo yato": "so tato"}[rel]
        assert m["d"] == exp, s
        return A.question_yo(rel, m["d"], CA_RE.sub("ānusayaṃ ca", m["a"]), CA_RE.sub("ānusayaṃ ca", m["b"]),
                             "nappajahati", m["l"], bool(m["vp"]))
    if "nappajah" in s:
        return parse_answer(s)
    return A.translate_sentence(s)          # Āmantā., (…mūlakaṃ), Pajahanavāre paṭilomaṃ.


def translate_line(line):
    m = re.match(r"^(?P<h>#+ )?(?P<t>.*?)(?P<id> \^[0-9A-Za-z-]+)?$", line)
    h, t, sid = m["h"] or "", m["t"], m["id"] or ""
    if h:
        return h + A.heading(t) + sid
    return " ".join(translate_sentence(s) for s in A.SPLIT_RE.split(t)) + sid


def translate_file(name):
    src = (B.PALI_DIR / name).read_text(encoding="utf-8")
    out = [translate_line(line) if line.strip() else "" for line in src.splitlines()]
    text = "\n".join(out).rstrip("\n") + "\n"
    return re.sub(r"\n{3,}", "\n\n", text)


# ================================================================ checks
CROSS_BOOK = [
    (MAGGI, 5), (f"hạng {MAGGI}", 4), (ATTHAMAKA, 5), ("con đường không trở lại", 5), ("Ngoại trừ", 1),
    ("còn lại", 1), ("dứt bỏ", 5), ("tối thượng", 5), ("không nằm trong các cõi tồn tại", 1),
    ("nơi cảm giác khó chịu", 5), ("trong cõi hình sắc", 2), ("trong cõi không hình sắc", 2),
    ("trong cõi dục lạc", 2), ("Đúng vậy.", 5), ("mọi nơi", 2),
]


def check_cross_book():
    N4.check_cross_book()
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md")))
             for b, d in B.RAILS_DIR.items()}
    missing = [(s, b) for s, b in CROSS_BOOK if s not in texts[b]]
    for s, b in missing:
        print(f"CROSS-BOOK MISSING in pi-{b}: {s}")
    assert not missing, f"{len(missing)} cross-book strings not found"
    print(f"cross-book asserts (7-06): {len(CROSS_BOOK)} strings found in pi-1..5 rails")


def check_7_04():
    """The frames shared with 7-04 must stay byte-identical."""
    for name in ("RES_VI", "BUT_C", "BOTH_C", "STATEMENT_RES", "STATEMENT_PLACE", "STATEMENT_PERSON"):
        assert getattr(N4, name) == globals()[name], f"7-04 {name} differs"
    for k, v in N4.PERSON_NOM_VI.items():
        assert PERSON_NOM_VI.get(k) == v, f"7-04 PERSON_NOM_VI[{k}] differs"
    print("shared frames with 7-04: identical")


def check_7_05():
    """Persons shared with the parallel anuloma chapter 7-05 (identical Pāli) must be byte-identical."""
    try:
        F = importlib.import_module("build_7-05_vi")
    except Exception as e:  # noqa: BLE001
        print("WARNING: build_7-05_vi not importable, shared persons not compared:", e)
        return
    common = [k for k in F.PERSON_NOM_VI if k in PERSON_NOM_VI]
    for k in common:
        assert F.PERSON_NOM_VI[k] == PERSON_NOM_VI[k], f"7-05 PERSON_NOM_VI[{k}] differs"
    for name in ("RES_VI", "BUT_C", "BOTH_C", "STATEMENT_RES"):
        assert getattr(F, name) == globals()[name], f"7-05 {name} differs"
    print(f"shared with 7-05: {len(common)} persons and 4 frames identical")


def check_repeats(pali):
    """Identical Pāli sentence -> identical Vietnamese sentence (within the chapter)."""
    seen, bad = {}, 0
    for p in pali.splitlines():
        if not p.strip() or p.startswith("#"):
            continue
        p = re.sub(r"\s*\^[\w-]+$", "", p)
        for s in A.SPLIT_RE.split(p):
            t = translate_sentence(s)
            if seen.setdefault(s, t) != t:
                bad += 1
    return bad


def main():
    check_cross_book()
    check_7_04()
    check_7_05()
    SLIPS.clear()
    A.SLIPS.clear()
    text = unicodedata.normalize("NFC", translate_file(CH))
    pali = (B.PALI_DIR / CH).read_text(encoding="utf-8")
    probs = B.check_lines(pali, text, CH)
    assert check_repeats(pali) == 0, "identical Pāli rendered differently"
    for bad in ("….", ".…", "?…", "  ", "là là", "ānusay", "puggal", "samaṅg", "pajah", " ca ", ",,", ", ,"):
        assert bad not in text, bad
    with open(B.OUT_DIR / CH, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    segs = len(re.findall(r"\^[0-9A-Za-z-]+\s*$", text, flags=re.M))
    print(f"wrote {CH}: {len([ln for ln in text.splitlines() if ln.strip()])} lines, {segs} segments")
    print("source slips rendered as meant:")
    for s in sorted(set(SLIPS + A.SLIPS)):
        print("  ", s)
    for p in probs[:80]:
        print("PROBLEM", p)
    print("line checks:", "OK" if not probs else f"{len(probs)} problems")
    sys.exit(1 if probs else 0)


if __name__ == "__main__":
    main()
