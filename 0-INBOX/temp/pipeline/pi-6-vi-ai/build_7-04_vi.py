# -*- coding: utf-8 -*-
"""pi-6 (Yamaka) Vietnamese zero-shot, chapter 7-04-anusayayamaka.md (Sānusayavāra, paṭiloma: niranusayo).

Family C frames come VERBATIM from the frame-setter build_7-01_vi (tendencies tl(), the yo / so, yato / tato,
yo yato / so tato question frame question_yo(), YO_VERB["niranusayo"], places PLACE_VI, headings, mūlaka labels,
closing lines). New here (listed in notes-7-04.md): the nominative person subjects (Anāgāmī, Arahā, Puthujjano,
Dve / Tayo / Cattāro puggalā, Teva puggalā, Sveva puggalo), the answer frames with tato / so tato / te tato and
sabbattha, «te tato», and the «…pe….» endings.

DASH RULE: no dash in this chapter, the frames add none. No quotes.
Importing writes nothing; run  python -I -X utf8 -B build_7-04_vi.py  to rebuild the chapter file.
"""
import importlib
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai")
import build_sample_vi as B  # noqa: E402

A = importlib.import_module("build_7-01_vi")

CH = "7-04-anusayayamaka.md"
cap, low, tl = B.cap, B.low, A.tl
SLIPS = []

# ================================================================ persons as subjects (nominative)
# 7-01 has the genitive «Ở …» forms (Anāgāmissa = Ở bậc không trở lại); the nominative drops «Ở».
PERSON_NOM_VI = {
    "Anāgāmī": "Bậc không trở lại",                  # pi-4 «bậc không trở lại» (7-01 Anāgāmissa)
    "Arahā": "Bậc A-la-hán",                         # pi-5 «bậc A-la-hán» (7-01 Arahato, proposed)
    "Puthujjano": "Người phàm phu",                  # pi-1 / pi-4 «người phàm phu» (7-01 Puthujjanassa)
    "Dve puggalā": "Hai hạng người",                 # pi-4 «hai hạng người»
    "Tayo puggalā": "Ba hạng người",                 # pi-4 «Ba hạng người –»
    "Cattāro puggalā": "Bốn hạng người",             # pi-4 «Bốn hạng người –»
    "Teva puggalā": "Chính những hạng người ấy",     # 7-01 Tesaññeva puggalānaṃ «Ở chính những hạng người ấy»
    "Sveva puggalo": "Chính hạng người ấy",          # 7-01 Tasseva puggalassa «Ở chính hạng người ấy»
}
PERSONS = sorted(PERSON_NOM_VI, key=len, reverse=True)

# ================================================================ places (7-01 PLACE_VI verbatim)
PLACE_VI = dict(A.PLACE_VI)          # incl. apariyāpanne «nơi những gì không nằm trong các cõi tồn tại», sabbattha «ở mọi nơi»
PLACE_SLIP = {"ariyāpanne": "apariyāpanne"}     # ^6-7-130 «dukkhāya vedanāya ariyāpanne» (slip, rendered as meant)
PLACES = sorted(list(PLACE_VI) + list(PLACE_SLIP), key=len, reverse=True)

# ================================================================ demonstratives of the answers
# yato / tato frames of 7-01: YO_DEM_VI = {"so": "người ấy", "tato": "đối với nơi ấy", "so tato": "người ấy, đối với nơi ấy"}
RES_VI = {"tato": A.YO_DEM_VI["tato"], "so tato": A.YO_DEM_VI["so tato"],
          "te tato": "những người ấy, đối với nơi ấy"}      # te tato (plural of so tato; 7-01 tesaṃ tattha parallel)
NIR = A.YO_VERB["niranusayo"]                               # p = «không có {t}», no = «vẫn có {t}» (7-01 proposed)
V_RE = "niranusayo|niranusayā"                              # niranusayā (plural) = same Vietnamese

# ================================================================ answer frames
BUT_C = "{pa}, nhưng {dem}{no}"            # A niranusayo, no ca [tato / so tato / te tato] B niranusayo
BOTH_C = "{pa}, đồng thời cũng {pb}"       # A ca niranusayo B ca niranusayo (7-01 BOTH_C «đồng thời … cũng»)
STATEMENT_RES = "{head}, thì {res} {clause}."      # <person> <places> so tato / te tato / tato <clause>. (7-01 frame)
STATEMENT_PLACE = "{head}, {clause}."              # <person> sabbattha <clause>.
STATEMENT_PERSON = "{head} {clause}."              # <person> <clause>. (nominative subject: no comma)

BUT_RE = re.compile(rf"(?P<a>.+?) (?P<va>{V_RE})(?P<comma>,?) no ca (?:(?P<dem>so tato|te tato|tato) )?"
                    rf"(?P<b>.+?) (?P<vb>{V_RE})")
BOTH_RE = re.compile(rf"(?P<a>.+? ca) (?P<va>{V_RE}) (?P<b>.+? ca) (?P<vb>{V_RE})")
BOTH_SLIP_RE = re.compile(rf"(?P<a>\S+ānusayena) (?P<va>{V_RE}) (?P<b>.+? ca) (?P<vb>{V_RE})")   # first «ca» missing


def lower1(s):
    return s[:1].lower() + s[1:]


def pv(phrase):
    return NIR["p"].format(t=tl(phrase))


def clause_of(body, s):
    m = BUT_RE.fullmatch(body)
    if m:
        if not m["comma"]:
            SLIPS.append("missing comma before «no ca»: " + s[:60])
        dem = RES_VI[m["dem"]] + " " if m["dem"] else ""
        if re.fullmatch(r"\S+ānusayena ca", m["b"]):
            SLIPS.append("stray «ca» after a single tendency in a «no ca» clause: " + s[:60])
        return BUT_C.format(pa=pv(m["a"]), dem=dem, no=NIR["no"].format(t=tl(m["b"])))
    m = BOTH_RE.fullmatch(body)
    if m:
        return BOTH_C.format(pa=pv(m["a"]), pb=pv(m["b"]))
    m = BOTH_SLIP_RE.fullmatch(body)
    if m:
        SLIPS.append("missing first «ca» (A niranusayo B ca niranusayo): " + s[:60])
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
        if hit in PLACE_SLIP:
            SLIPS.append(f"{hit} = {PLACE_SLIP[hit]}")
            places.append(PLACE_SLIP[hit])
        else:
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


# ================================================================ questions (7-01 question_yo verbatim)
Q_RE = re.compile(rf"(?:\((?P<l>Ka|Kha)\) )?(?P<y1>[Yy]o|[Yy]ato)(?P<vp> vā pana)?(?P<y2> yato)? "
                  rf"(?P<a>.+?) niranusayo (?P<d>so tato|so|tato) (?P<b>.+?) ?niranusayoti\?")

# ================================================================ closing lines, «…pe….» endings
EXACT = {"Sānusayavāro.": A.SECTION["Sānusayavāro"] + "."}     # Sānusayavāro. = Mục về sự có khuynh hướng tiềm ẩn.
PE_END_RE = re.compile(r"(?P<s>.*?) ?…pe…\.")                  # «… niranusayo …pe….», «Āmantā …pe….», «Āmantā…pe….»
PE = A.PE                                                       # …pe… = …


def translate_sentence(s):
    m = PE_END_RE.fullmatch(s)
    if m:
        inner = m["s"] + "."
        out = translate_sentence(inner)
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
        return A.question_yo(rel, m["d"], m["a"], m["b"], "niranusayo", m["l"], bool(m["vp"]))
    if "niranusay" in s:
        return parse_statement(s)
    return A.translate_sentence(s)          # Āmantā., (…mūlakaṃ), Sānusayavāre paṭilomaṃ.


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
    ("người phàm phu", 4), ("bậc A-la-hán", 5), ("có khuynh hướng tiềm ẩn", 5), ("mọi nơi", 2),
    ("không nằm trong các cõi tồn tại", 1), ("nơi cảm giác khó chịu", 5), ("trong cõi hình sắc", 2),
    ("trong cõi không hình sắc", 2), ("trong cõi dục lạc", 2), ("Đúng vậy.", 5),
]


def check_cross_book():
    A.check_cross_book()
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md")))
             for b, d in B.RAILS_DIR.items()}
    missing = [(s, b) for s, b in CROSS_BOOK if s not in texts[b]]
    for s, b in missing:
        print(f"CROSS-BOOK MISSING in pi-{b}: {s}")
    assert not missing, f"{len(missing)} cross-book strings not found"
    print(f"cross-book asserts (7-04): {len(CROSS_BOOK)} strings found in pi-1..5 rails")


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
    SLIPS.clear()
    A.SLIPS.clear()
    text = unicodedata.normalize("NFC", translate_file(CH))
    pali = (B.PALI_DIR / CH).read_text(encoding="utf-8")
    probs = B.check_lines(pali, text, CH)
    # the sample's foreign-letter check also hits the label «(f)» (= (Ca)); accept it only when the line is clean
    # once the label is removed
    vlines = [ln for ln in text.splitlines() if ln.strip()]

    def label_only(p):
        m = re.fullmatch(rf"{re.escape(CH)} line (\d+): foreign letter 'f'", p)
        return bool(m) and not B.FOREIGN.search(B._strip(re.sub(r"\([a-h]\)", "", vlines[int(m.group(1)) - 1])))

    probs = [p for p in probs if not label_only(p)]
    assert check_repeats(pali) == 0, "identical Pāli rendered differently"
    for bad in ("….", ".…", "?…", "  ", "là là"):
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
