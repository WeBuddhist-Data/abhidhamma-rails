# -*- coding: utf-8 -*-
"""pi-6 (Yamaka) Vietnamese zero-shot, chapter 7-05-anusayayamaka.md (Pajahanavāro, anuloma: pajahati).

Family C frames come VERBATIM from the frame-setter build_7-01_vi (tendencies tl(), question_yo() with
YO_VERB["pajahati"] «dứt bỏ {t}», TADEKATTHA «những gì cùng hiện diện với nó», places PLACE_VI, headings, mūlaka
labels, VARE_DIR closing line, Āmantā / No / Natthi) and from build_7-04_vi (nominative persons PERSON_NOM_VI,
answer demonstratives RES_VI «tato / so tato», BUT_C, BOTH_C, STATEMENT_RES, the «…pe….» endings).
New here (listed in notes-7-05.md): the persons Aṭṭhamako / Aggamaggasamaṅgī, the «tadekaṭṭhaṃ pajahati» answers
(standalone and attributive), the list-object form «A ca B ca pajahati», the subject-less answers.

DASH RULE: no dash in this chapter, the frames add none. No quotes.
Importing writes nothing; run  python -I -X utf8 -B build_7-05_vi.py  to rebuild the chapter file.
"""
import importlib
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai")
import build_sample_vi as B  # noqa: E402

A = importlib.import_module("build_7-01_vi")
C = importlib.import_module("build_7-04_vi")

CH = "7-05-anusayayamaka.md"
cap, low, tl = B.cap, B.low, A.tl
SLIPS = []

# ================================================================ verb (7-01 YO_VERB, proposal used as is)
PAJ = A.YO_VERB["pajahati"]                 # p = «dứt bỏ {t}», no = «không dứt bỏ {t}» (pi-1 pajahana «dứt bỏ»)
TADEKATTHA = A.TADEKATTHA                   # «những gì cùng hiện diện với nó» (pi-1 tadekaṭṭha «cùng hiện diện với»)
TADEK_ALONE = PAJ["p"].format(t=TADEKATTHA)  # Tadekaṭṭhaṃ pajahati = Dứt bỏ những gì cùng hiện diện với nó.
TADEK_ATTR = "{t} vốn cùng hiện diện với nó"
# X tadekaṭṭhaṃ pajahati = dứt bỏ X vốn cùng hiện diện với nó (aṭṭhakathā: «pahānekaṭṭhataṃ sandhāya vuttaṃ»)
TADEK_C = "{pa}, {pb}"                       # A pajahati B tadekaṭṭhaṃ pajahati (two verbs, no «ca» in the Pāli)

# ================================================================ persons (nominative; 7-04 PERSON_NOM_VI + new)
PERSON_NOM_VI = dict(C.PERSON_NOM_VI)
PERSON_NOM_VI.update({
    "Aṭṭhamako": "Người thứ tám",                                # pi-5 Aṭṭhamako puggalo «người thứ tám»
    "Aggamaggasamaṅgī": "Người có được con đường tối thượng",   # pi-5 maggasamaṅgī «người có được con đường»
})
PERSONS = sorted(PERSON_NOM_VI, key=len, reverse=True)
PLACE_VI = A.PLACE_VI
PLACES = sorted(PLACE_VI, key=len, reverse=True)
RES_VI = C.RES_VI                             # tato = đối với nơi ấy; so tato = người ấy, đối với nơi ấy
BUT_C = C.BUT_C                               # «{pa}, nhưng {dem}{no}»
BOTH_C = C.BOTH_C                             # «{pa}, đồng thời cũng {pb}»
STATEMENT_RES = C.STATEMENT_RES               # «{head}, thì {res} {clause}.»


def lower1(s):
    return s[:1].lower() + s[1:]


def unsandhi(s):
    """kāmarāgānusayañca -> kāmarāgānusayaṃ ca (tl() takes separate «ca» tokens)."""
    return re.sub(r"ānusayañca\b", "ānusayaṃ ca", s)


# ================================================================ verb phrases
UNIT_RE = re.compile(r"(?P<obj>.*?)(?P<td>(?:^| )tadekaṭṭhaṃ)? ?pajahati(?: |$)")


def units(x):
    """«<list> [tadekaṭṭhaṃ] pajahati» units of a clause, in order."""
    out, pos = [], 0
    while pos < len(x):
        m = UNIT_RE.match(x, pos)
        if not m or m.end() == pos:
            raise ValueError(f"unparsed verb phrase: {x!r}")
        out.append((m["obj"].strip(), bool(m["td"])))
        pos = m.end()
    return out


def vp(x, s):
    """Positive verb phrase of a clause (Vietnamese, lowercase)."""
    u = units(unsandhi(lower1(x)))
    if len(u) == 1:
        obj, td = u[0]
        if td and not obj:
            return TADEK_ALONE
        if td:
            raise ValueError(s)
        return PAJ["p"].format(t=tl(obj))
    if len(u) == 2:
        (o1, t1), (o2, t2) = u
        if not t1 and t2:
            return TADEK_C.format(pa=PAJ["p"].format(t=tl(o1)), pb=PAJ["p"].format(t=TADEK_ATTR.format(t=tl(o2))))
        if not t1 and not t2 and o1.endswith(" ca") and o2.endswith(" ca"):
            return BOTH_C.format(pa=PAJ["p"].format(t=tl(o1)), pb=PAJ["p"].format(t=tl(o2)))
    raise ValueError(f"unparsed verb phrase: {s!r}")


def clause_of(body, s):
    m = re.fullmatch(r"(?P<a>.+?)(?P<comma>,?) no ca (?:(?P<dem>so tato|tato) )?(?P<b>.+ pajahati)", body)
    if m:
        if not m["comma"]:
            SLIPS.append("missing comma before «no ca»: " + s[:70])
        u = units(unsandhi(m["b"]))
        assert len(u) == 1 and not u[0][1], s
        dem = RES_VI[m["dem"]] + " " if m["dem"] else ""
        return BUT_C.format(pa=vp(m["a"], s), dem=dem, no=PAJ["no"].format(t=tl(u[0][0])))
    return vp(body, s)


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
    res = next((r for r in ("so tato", "tato") if t.startswith(r + " ")), None)
    if res:
        t = t[len(res) + 1:]
    clause = clause_of(t, s)
    head = ", ".join(([PERSON_NOM_VI[per]] if per else []) + [PLACE_VI[p] for p in places])
    if res:
        assert head and (res == "so tato") == bool(per), s
        return cap(STATEMENT_RES.format(head=head, res=RES_VI[res], clause=clause))
    assert not head, s                         # subject-less answer (7-03 «Có khuynh hướng tiềm ẩn kiêu mạn.»)
    return cap(clause) + "."


# ================================================================ questions (7-01 question_yo verbatim)
Q_RE = re.compile(r"(?:\((?P<l>Ka|Kha)\) )?(?P<y1>[Yy]o|[Yy]ato)(?P<vp> vā pana)?(?P<y2> yato)? "
                  r"(?P<a>.+?) pajahati (?P<d>so tato|so|tato) (?P<b>.+?) ?pajahatīti\?")


def translate_sentence(s):
    m = C.PE_END_RE.fullmatch(s)
    if m:
        out = translate_sentence(m["s"] + ".")
        assert out.endswith("."), out
        return out[:-1] + A.PE                  # «….» is never written: the period gives way to «…» (7-04)
    m = Q_RE.fullmatch(s)
    if m:
        y1 = m["y1"].lower()
        rel = "yo yato" if m["y2"] else y1
        assert m["d"] == {"yo": "so", "yato": "tato", "yo yato": "so tato"}[rel], s
        return A.question_yo(rel, m["d"], unsandhi(m["a"]), unsandhi(m["b"]), "pajahati", m["l"], bool(m["vp"]))
    if s.endswith("pajahati."):
        return parse_statement(s)
    return A.translate_sentence(s)              # Āmantā., No., Natthi., (…mūlakaṃ), Pajahanavāre anulomaṃ.


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
    ("dứt bỏ", 1), ("cùng hiện diện với", 1), ("người thứ tám", 5), ("người có được con đường", 5),
    ("người có được con đường", 1), ("tối thượng", 5), ("Không có.", 3), ("Đúng vậy.", 5),
]


def check_cross_book():
    C.check_cross_book()
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md")))
             for b, d in B.RAILS_DIR.items()}
    missing = [(s, b) for s, b in CROSS_BOOK if s not in texts[b]]
    for s, b in missing:
        print(f"CROSS-BOOK MISSING in pi-{b}: {s}")
    assert not missing, f"{len(missing)} cross-book strings not found"
    print(f"cross-book asserts (7-05): {len(CROSS_BOOK)} strings found in pi-1..5 rails")


def sentences(pali):
    for p in pali.splitlines():
        if not p.strip() or p.startswith("#"):
            continue
        yield from A.SPLIT_RE.split(re.sub(r"\s*\^[\w-]+$", "", p))


def check_repeats(pali):
    """Identical Pāli sentence -> identical Vietnamese, within the chapter and with 7-01 / 7-04."""
    seen, bad = {}, 0
    for s in sentences(pali):
        if seen.setdefault(s, translate_sentence(s)) != translate_sentence(s):
            bad += 1
    for other, mod in (("7-01-anusayayamaka.md", A), ("7-04-anusayayamaka.md", C)):
        for s in set(sentences((B.PALI_DIR / other).read_text(encoding="utf-8"))) & set(seen):
            if mod.translate_sentence(s) != seen[s]:
                print("CROSS-CHAPTER DIFF", other, s)
                bad += 1
    return bad


def main():
    check_cross_book()
    SLIPS.clear()
    A.SLIPS.clear()
    text = unicodedata.normalize("NFC", translate_file(CH))
    pali = (B.PALI_DIR / CH).read_text(encoding="utf-8")
    probs = B.check_lines(pali, text, CH)
    assert check_repeats(pali) == 0, "identical Pāli rendered differently"
    for bad in ("….", ".…", "?…", "  ", "là là", "pajah", "nusay"):
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
