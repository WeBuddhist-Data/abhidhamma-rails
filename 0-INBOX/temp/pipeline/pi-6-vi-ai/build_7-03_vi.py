# -*- coding: utf-8 -*-
"""pi-6 (Yamaka) Vietnamese zero-shot, chapter 7-03-anusayayamaka.md (Sānusayavāro, anuloma: sānusayo).

Family C frames come VERBATIM from the frame-setter build_7-01_vi (tendencies tl(), the yo / so, yato / tato,
yo yato / so tato question frame question_yo(), YO_VERB["sānusayo"] = «có {t}» / «không có {t}», places PLACE_VI,
headings, mūlaka labels, «Sānusayavāre anulomaṃ.»). The nominative person subjects, the answer demonstratives
(tato / so tato / te tato) and the answer frames are byte-identical with the parallel paṭiloma chapter 7-04
(build_7-04_vi: PERSON_NOM_VI, RES_VI, BUT_C, BOTH_C, STATEMENT_*); main() asserts that they still agree.
New here (listed in notes-7-03.md): the subject-less answers «Mānānusayena sānusayo.» / «A ca B ca sānusayo.».

DASH RULE: no dash in this chapter, the frames add none. No quotes.
Importing writes nothing; run  python -I -X utf8 -B build_7-03_vi.py  to rebuild the chapter file.
"""
import importlib
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai")
import build_sample_vi as B  # noqa: E402

A = importlib.import_module("build_7-01_vi")

CH = "7-03-anusayayamaka.md"
cap, low, tl = B.cap, B.low, A.tl
SLIPS = []

# ================================================================ persons as subjects (nominative; = 7-04 PERSON_NOM_VI)
PERSON_NOM_VI = {
    "Anāgāmī": "Bậc không trở lại",                  # pi-4 «bậc không trở lại» (7-01 Anāgāmissa)
    "Puthujjano": "Người phàm phu",                  # pi-1 / pi-4 «người phàm phu» (7-01 Puthujjanassa)
    "Dve puggalā": "Hai hạng người",                 # pi-4 «hai hạng người»
    "Tayo puggalā": "Ba hạng người",                 # pi-4 «Ba hạng người –»
    "Cattāro puggalā": "Bốn hạng người",             # pi-4 «Bốn hạng người –»
    "Teva puggalā": "Chính những hạng người ấy",     # 7-01 Tesaññeva puggalānaṃ «Ở chính những hạng người ấy»
    "Sveva puggalo": "Chính hạng người ấy",          # 7-01 Tasseva puggalassa «Ở chính hạng người ấy»
}
PERSONS = sorted(PERSON_NOM_VI, key=len, reverse=True)

# ================================================================ places (7-01 PLACE_VI verbatim)
PLACE_VI = dict(A.PLACE_VI)
PLACES = sorted(PLACE_VI, key=len, reverse=True)

# ================================================================ demonstratives of the answers (= 7-04 RES_VI)
RES_VI = {"tato": A.YO_DEM_VI["tato"], "so tato": A.YO_DEM_VI["so tato"],
          "te tato": "những người ấy, đối với nơi ấy"}      # te tato (plural of so tato)
SAN = A.YO_VERB["sānusayo"]                                 # p = «có {t}», no = «không có {t}» (7-01)
V_RE = "sānusayo|sānusayā"                                  # sānusayā (plural) = same Vietnamese

# ================================================================ answer frames (= 7-04)
BUT_C = "{pa}, nhưng {dem}{no}"            # A sānusayo, no ca [tato / so tato / te tato] B sānusayo
BOTH_C = "{pa}, đồng thời cũng {pb}"       # A ca sānusayo B ca sānusayo (7-01 BOTH_C «đồng thời … cũng»)
STATEMENT_RES = "{head}, thì {res} {clause}."      # <person> <places> so tato / te tato / tato <clause>.
STATEMENT_PLACE = "{head}, {clause}."              # <places> <clause>. (not met in 7-03)
STATEMENT_PERSON = "{head} {clause}."              # <person> <clause>. (nominative subject: no comma)
STATEMENT_BARE = "{clause}."                       # NEW: Mānānusayena sānusayo. = Có khuynh hướng tiềm ẩn kiêu mạn.

BUT_RE = re.compile(rf"(?P<a>.+?) (?P<va>{V_RE})(?P<comma>,?) no ca (?:(?P<dem>so tato|te tato|tato) )?"
                    rf"(?P<b>.+?) (?P<vb>{V_RE})")
BOTH_RE = re.compile(rf"(?P<a>.+? ca) (?P<va>{V_RE}) (?P<b>.+? ca) (?P<vb>{V_RE})")
SIMPLE_RE = re.compile(rf"(?P<a>.+?) (?P<va>{V_RE})")


def lower1(s):
    return s[:1].lower() + s[1:]


def pv(phrase):
    return SAN["p"].format(t=tl(phrase))


def clause_of(body, s):
    m = BUT_RE.fullmatch(body)
    if m:
        if not m["comma"]:
            SLIPS.append("missing comma before «no ca»: " + s[:60])
        dem = RES_VI[m["dem"]] + " " if m["dem"] else ""
        return BUT_C.format(pa=pv(m["a"]), dem=dem, no=SAN["no"].format(t=tl(m["b"])))
    m = BOTH_RE.fullmatch(body)
    if m:
        return BOTH_C.format(pa=pv(m["a"]), pb=pv(m["b"]))
    m = SIMPLE_RE.fullmatch(body)
    if m and " no ca " not in body:
        return pv(m["a"])
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
    if not per and not places and not res:
        t = lower1(t)                                           # «Mānānusayena sānusayo.» (subject-less answer)
    clause = clause_of(t, s)
    head = ", ".join(([PERSON_NOM_VI[per]] if per else []) + [PLACE_VI[p] for p in places])
    if res:
        assert head, s
        return cap(STATEMENT_RES.format(head=head, res=RES_VI[res], clause=clause))
    if places:
        return cap(STATEMENT_PLACE.format(head=head, clause=clause))
    if per:
        return cap(STATEMENT_PERSON.format(head=head, clause=clause))
    return cap(STATEMENT_BARE.format(clause=clause))


# ================================================================ questions (7-01 question_yo verbatim)
Q_RE = re.compile(rf"(?:\((?P<l>Ka|Kha)\) )?(?P<y1>[Yy]o|[Yy]ato)(?P<vp> vā pana)?(?P<y2> yato)? "
                  rf"(?P<a>.+?) sānusayo (?P<d>so tato|so|tato) (?P<b>.+?) ?sānusayoti\?")

# ================================================================ «…pe….» endings (= 7-04)
PE_END_RE = re.compile(r"(?P<s>.*?) ?…pe…\.")                  # «… sānusayo…pe….», «Āmantā …pe….»
PE = A.PE                                                       # …pe… = …


def translate_sentence(s):
    m = PE_END_RE.fullmatch(s)
    if m:
        out = translate_sentence(m["s"] + ".")
        assert out.endswith("."), out
        return out[:-1] + PE                                    # «….» is never written: the period gives way to «…»
    m = Q_RE.fullmatch(s)
    if m:
        y1 = m["y1"].lower()
        rel = "yo yato" if m["y2"] else y1
        exp = {"yo": "so", "yato": "tato", "yo yato": "so tato"}[rel]
        assert m["d"] == exp, s
        return A.question_yo(rel, m["d"], m["a"], m["b"], "sānusayo", m["l"], bool(m["vp"]))
    if "sānusay" in s and "vāre" not in s:
        return parse_statement(s)
    return A.translate_sentence(s)          # Āmantā., No., Natthi., (…mūlakaṃ), Sānusayavāre anulomaṃ.


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
    ("Ba hạng người", 4), ("Bốn hạng người", 4), ("hai hạng người", 4), ("bậc không trở lại", 4),
    ("người phàm phu", 4), ("có khuynh hướng tiềm ẩn", 5), ("nơi cảm giác khó chịu", 5),
    ("trong cõi hình sắc", 2), ("trong cõi không hình sắc", 2), ("trong cõi dục lạc", 2), ("Đúng vậy.", 5),
    ("Không có.", 3),
]


def check_cross_book():
    A.check_cross_book()
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md")))
             for b, d in B.RAILS_DIR.items()}
    missing = [(s, b) for s, b in CROSS_BOOK if s not in texts[b]]
    for s, b in missing:
        print(f"CROSS-BOOK MISSING in pi-{b}: {s}")
    assert not missing, f"{len(missing)} cross-book strings not found"
    print(f"cross-book asserts (7-03): {len(CROSS_BOOK)} strings found in pi-1..5 rails")


def check_7_04():
    """The frames shared with the paṭiloma chapter 7-04 must stay byte-identical."""
    try:
        N = importlib.import_module("build_7-04_vi")
    except Exception as e:  # noqa: BLE001
        print("WARNING: build_7-04_vi not importable, shared frames not compared:", e)
        return
    for name in ("RES_VI", "BUT_C", "BOTH_C", "STATEMENT_RES", "STATEMENT_PLACE", "STATEMENT_PERSON"):
        assert getattr(N, name) == globals()[name], f"7-04 {name} differs"
    for k, v in PERSON_NOM_VI.items():
        assert N.PERSON_NOM_VI.get(k) == v, f"7-04 PERSON_NOM_VI[{k}] differs"
    print("shared frames with 7-04: identical")


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
    SLIPS.clear()
    A.SLIPS.clear()
    text = unicodedata.normalize("NFC", translate_file(CH))
    pali = (B.PALI_DIR / CH).read_text(encoding="utf-8")
    probs = B.check_lines(pali, text, CH)
    assert check_repeats(pali) == 0, "identical Pāli rendered differently"
    for bad in ("….", ".…", "?…", "  ", "là là", "sānusay", "puggal"):
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
