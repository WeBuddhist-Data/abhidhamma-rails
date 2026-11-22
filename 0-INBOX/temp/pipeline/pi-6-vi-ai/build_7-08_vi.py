# -*- coding: utf-8 -*-
"""pi-6 (Yamaka) Vietnamese zero-shot, chapter 7-08-anusayayamaka.md (Pariññāvāra, paṭiloma, person and place:
na parijānāti).

Family C frames come VERBATIM from the frame-setter build_7-01_vi (tendencies tl(), question_yo() with
YO_VERB["na parijānāti"] = «không hiểu biết trọn vẹn {t}» / no ca … = «vẫn hiểu biết trọn vẹn {t}», places PLACE_VI,
headings, mūlaka labels, VARE_DIR closing line, Āmantā). The answer frames, the demonstratives tato / so tato and the
nominative persons are byte-identical with build_7-04_vi / build_7-05_vi (imported); the path persons and the
«X ṭhapetvā avasesā puggalā» frame are those of 7-06 (notes-7-06.md; main() asserts equality when build_7-06_vi
imports). The «…pe….» endings are 7-04's. New here (notes-7-08.md): na parijānanti (plural), «Pariññāvāro.».

DASH RULE: no dash in this chapter, the frames add none. No quotes.
Importing writes nothing; run  python -I -X utf8 -B build_7-08_vi.py  to rebuild the chapter file.
"""
import importlib
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai")
import build_sample_vi as B  # noqa: E402

A = importlib.import_module("build_7-01_vi")     # family C frame-setter
N4 = importlib.import_module("build_7-04_vi")    # nominative persons, answer frames (yo / so chapters)
N5 = importlib.import_module("build_7-05_vi")    # Aggamaggasamaṅgī, Aṭṭhamako

CH = "7-08-anusayayamaka.md"
cap, low = B.cap, B.low
SLIPS = []

# ================================================================ tendency lists (accusative «-ānusayañca» = «-ānusayaṃ ca»)
CA_RE = re.compile(r"ānusayañca\b")


def unsandhi(s):
    return CA_RE.sub("ānusayaṃ ca", s)


def tl(phrase):
    return A.tl(unsandhi(phrase))


# ================================================================ persons as subjects (nominative)
MAGGI = "người có được con đường"                  # maggasamaṅgī (pi-5 «người có được con đường»; = 7-06)
AGGA = f"{MAGGI} tối thượng"                        # aggamaggasamaṅgī (= 7-05 / 7-06)
ANAGAMI_M = f"{MAGGI} không trở lại"                # anāgāmimaggasamaṅgī (= 7-06; pi-2 / pi-5 «con đường không trở lại»)
ATTHAMAKA = "người thứ tám"                         # aṭṭhamako (= 7-05 / 7-06; pi-5 «người thứ tám»)
EXCLUDED_VI = {                                     # X ṭhapetvā (accusative) (= 7-06)
    "Dvinnaṃ maggasamaṅgīnaṃ": f"hai {MAGGI}",
    "Dvinnaṃ maggasamaṅgīnañca aṭṭhamakañca": f"hai {MAGGI} và {ATTHAMAKA}",
    "Anāgāmimaggasamaṅgiṃ": ANAGAMI_M,
    "Aggamaggasamaṅgiṃ": AGGA,
    "Anāgāmimaggasamaṅgiñca aṭṭhamakañca": f"{ANAGAMI_M} và {ATTHAMAKA}",
    "Aggamaggasamaṅgiñca aṭṭhamakañca": f"{AGGA} và {ATTHAMAKA}",
}
EXCEPT = "Ngoại trừ {x}, những hạng người còn lại"   # X ṭhapetvā avasesā puggalā (= 7-06; pi-1 «Ngoại trừ …, … còn lại»)
PERSON_NOM_VI = dict(N5.PERSON_NOM_VI)              # 7-04 persons + Aggamaggasamaṅgī, Aṭṭhamako (7-05)
PERSON_NOM_VI.update({"Anāgāmimaggasamaṅgī": cap(ANAGAMI_M)})
PERSON_NOM_VI.update({f"{k} ṭhapetvā avasesā puggalā": EXCEPT.format(x=v) for k, v in EXCLUDED_VI.items()})
PERSONS = sorted(PERSON_NOM_VI, key=len, reverse=True)

# ================================================================ places (7-01 PLACE_VI verbatim)
PLACE_VI = dict(A.PLACE_VI)
PLACES = sorted(PLACE_VI, key=len, reverse=True)

# ================================================================ demonstratives, verb
RES_VI = dict(N4.RES_VI)                            # tato / so tato / te tato (7-04)
DEM_VI = dict(RES_VI, so=A.YO_DEM_VI["so"])         # no ca so = nhưng người ấy (= 7-06)
NPJ = A.YO_VERB["na parijānāti"]                    # p = «không hiểu biết trọn vẹn {t}», no = «vẫn hiểu biết trọn vẹn {t}»
V_RE = "na parijānāti|na parijānanti"               # na parijānanti (plural) = same Vietnamese

# ================================================================ answer frames (= 7-04)
BUT_C = N4.BUT_C                    # "{pa}, nhưng {dem}{no}"
BOTH_C = N4.BOTH_C                  # "{pa}, đồng thời cũng {pb}"
STATEMENT_RES = N4.STATEMENT_RES    # "{head}, thì {res} {clause}."
STATEMENT_PLACE = N4.STATEMENT_PLACE  # "{head}, {clause}."
STATEMENT_PERSON = N4.STATEMENT_PERSON  # "{head} {clause}."

BUT_RE = re.compile(rf"(?P<a>.+?) (?P<va>{V_RE}), no ca (?:(?P<dem>so tato|te tato|tato|so) )?"
                    rf"(?P<b>.+?) (?P<vb>{V_RE})")
BOTH_RE = re.compile(rf"(?P<a>.+? ca) (?P<va>{V_RE}) (?P<b>.+? ca) (?P<vb>{V_RE})")


def lower1(s):
    return s[:1].lower() + s[1:]


def pv(phrase):
    return NPJ["p"].format(t=tl(phrase))


def clause_of(body, s):
    body = unsandhi(body)
    m = BUT_RE.fullmatch(body)
    if m:
        dem = DEM_VI[m["dem"]] + " " if m["dem"] else ""
        return BUT_C.format(pa=pv(m["a"]), dem=dem, no=NPJ["no"].format(t=tl(m["b"])))
    m = BOTH_RE.fullmatch(body)
    if m:
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
        hit = next((p for p in PLACES if lower1(t).startswith(p + " ") or lower1(t).startswith(p + ", ")), None)
        if not hit:
            break
        places.append(hit)
        t = t[len(hit):]
        if t.startswith(", "):
            # ^6-7-257 «kāmadhātuyā tīsu vedanāsu, apariyāpanne»: stray comma inside the place list; the
            # Vietnamese place list is joined with «, » anyway, so the rendering is unchanged
            SLIPS.append("stray comma inside the place list: " + s[:80])
            t = t[1:]
        t = t[1:]
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


# ================================================================ questions (7-01 question_yo verbatim)
Q_RE = re.compile(rf"(?:\((?P<l>Ka|Kha)\) )?(?P<y1>[Yy]o|[Yy]ato)(?P<vp> vā pana)?(?P<y2> yato)? "
                  rf"(?P<a>.+?) na parijānāti (?P<d>so tato|so|tato) (?P<b>.+?) ?na parijānātīti\?")

# ================================================================ closing lines, «…pe….» endings (= 7-04)
EXACT = {"Pariññāvāro.": A.SECTION["Pariññāvāro"] + "."}       # Pariññāvāro. = Mục về sự hiểu biết trọn vẹn.
PE_END_RE = N4.PE_END_RE                                        # «… na parijānanti …pe….», «Āmantā …pe….»
PE = A.PE                                                       # …pe… = …


def translate_sentence(s):
    m = PE_END_RE.fullmatch(s)
    if m:
        out = translate_sentence(m["s"] + ".")
        assert out.endswith("."), out
        return out[:-1] + PE                                    # «….» is never written: the period gives way to «…»
    if s in EXACT:
        return EXACT[s]
    m = Q_RE.fullmatch(s)
    if m:
        y1 = m["y1"].lower()
        rel = "yo yato" if m["y2"] else y1
        exp = {"yo": "so", "yato": "tato", "yo yato": "so tato"}[rel]
        assert m["d"] == exp, s
        return A.question_yo(rel, m["d"], unsandhi(m["a"]), unsandhi(m["b"]), "na parijānāti", m["l"], bool(m["vp"]))
    if "parijān" in s:
        return parse_statement(s)
    return A.translate_sentence(s)          # Āmantā., (…mūlakaṃ), Pariññāvāre paṭilomaṃ.


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
    ("hiểu biết trọn vẹn", 2), (MAGGI, 5), (f"hạng {MAGGI}", 4), (ATTHAMAKA, 5), ("con đường không trở lại", 5),
    ("Ngoại trừ", 1), ("còn lại", 1), ("tối thượng", 5), ("không nằm trong các cõi tồn tại", 1),
    ("nơi cảm giác khó chịu", 5), ("trong cõi hình sắc", 2), ("trong cõi không hình sắc", 2),
    ("trong cõi dục lạc", 2), ("Đúng vậy.", 5), ("mọi nơi", 2),
]


def check_cross_book():
    N5.check_cross_book()                   # chains 7-04 and 7-01
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md")))
             for b, d in B.RAILS_DIR.items()}
    missing = [(s, b) for s, b in CROSS_BOOK if s not in texts[b]]
    for s, b in missing:
        print(f"CROSS-BOOK MISSING in pi-{b}: {s}")
    assert not missing, f"{len(missing)} cross-book strings not found"
    print(f"cross-book asserts (7-08): {len(CROSS_BOOK)} strings found in pi-1..5 rails")


def check_shared():
    """Frames shared with 7-04 / 7-05 / 7-06 must stay byte-identical."""
    for name in ("RES_VI", "BUT_C", "BOTH_C", "STATEMENT_RES", "STATEMENT_PLACE", "STATEMENT_PERSON"):
        assert getattr(N4, name) == globals()[name], f"7-04 {name} differs"
    for k, v in N5.PERSON_NOM_VI.items():
        assert PERSON_NOM_VI.get(k) == v, f"7-05 PERSON_NOM_VI[{k}] differs"
    try:
        F = importlib.import_module("build_7-06_vi")
    except Exception as e:  # noqa: BLE001
        print("WARNING: build_7-06_vi not importable, path persons not compared:", e)
        return
    common = [k for k in F.PERSON_NOM_VI if k in PERSON_NOM_VI]
    for k in common:
        assert F.PERSON_NOM_VI[k] == PERSON_NOM_VI[k], f"7-06 PERSON_NOM_VI[{k}] differs"
    for k in PERSON_NOM_VI:
        assert k in F.PERSON_NOM_VI, f"person not in 7-06: {k}"
    assert F.DEM_VI == DEM_VI and F.EXCEPT == EXCEPT and F.EXCLUDED_VI == EXCLUDED_VI, "7-06 frames differ"
    print(f"shared with 7-04 / 7-05 / 7-06: frames and {len(common)} persons identical")


def sentences(pali):
    for p in pali.splitlines():
        if not p.strip() or p.startswith("#"):
            continue
        yield from A.SPLIT_RE.split(re.sub(r"\s*\^[\w-]+$", "", p))


def check_repeats(pali):
    """Identical Pāli sentence -> identical Vietnamese, within the chapter and with the other anusaya chapters."""
    seen, bad = {}, 0
    for s in sentences(pali):
        if seen.setdefault(s, translate_sentence(s)) != translate_sentence(s):
            bad += 1
    others = [("7-01", A), ("7-04", N4), ("7-05", N5)]
    for n in ("7-06", "7-07"):
        try:
            others.append((n, importlib.import_module(f"build_{n}_vi")))
        except Exception as e:  # noqa: BLE001
            print(f"note: build_{n}_vi not importable, not compared:", type(e).__name__)
    for n, mod in others:
        p = B.PALI_DIR / f"{n}-anusayayamaka.md"
        for s in set(sentences(p.read_text(encoding="utf-8"))) & set(seen):
            if mod.translate_sentence(s) != seen[s]:
                print("CROSS-CHAPTER DIFF", n, s)
                bad += 1
    return bad


def main():
    check_cross_book()
    check_shared()
    SLIPS.clear()
    A.SLIPS.clear()
    text = unicodedata.normalize("NFC", translate_file(CH))
    pali = (B.PALI_DIR / CH).read_text(encoding="utf-8")
    probs = B.check_lines(pali, text, CH)
    assert check_repeats(pali) == 0, "identical Pāli rendered differently"
    for bad in ("….", ".…", "?…", "  ", "là là", "ānusay", "puggal", "samaṅg", "parijān", " ca ", ",,", ", ,"):
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
