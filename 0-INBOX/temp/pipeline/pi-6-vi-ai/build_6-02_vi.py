# -*- coding: utf-8 -*-
"""pi-6 (Yamaka) Vietnamese zero-shot, chapter 6-02-sankharayamaka.md (Saṅkhārayamaka, second part:
nirodhavāra (3)-(6), uppādanirodhavāra, pariññāvāra, the yamaka's closing lines).

Frames come VERBATIM from the frame-setters, by import:
    build_6-01_vi   (first half of this yamaka: members m(), answer heads head() / ITEMS, translate_sentence(),
                     fragments, editorial vocabulary YASSAKA / YATTHAKA / YASSAYATTHAKA / BOTH_SECTIONS / NIRODHA_CASE)
    build_2-01_vi   (family B frames, verbs, RES_VI, PLANE, BEINGS_OF)     via build_6-01_vi.F
    build_2-02_vi   (family E: translate_e, PARINNA_EXACT; Nirodhavāro. / Uppādanirodhavāro.; PE)  via .E
    build_8_vi      (moments, citta(last=True))                           via .C8
    build_sample_vi (labels, SECTION, ADI, yamaka_end, HOMAGE, AMANTA, line checks)
This module adds only what 6-01 did not meet: the «pacchimacittassa» moments, one source slip and the editorial
lines of this half. Importing writes nothing; run  python -I -X utf8 -B build_6-02_vi.py  to build the chapter.
"""
import importlib
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai")
import build_sample_vi as S  # noqa: E402

X = importlib.import_module("build_6-01_vi")     # first half of the Saṅkhārayamaka (frames copied by import)
F = importlib.import_module("build_2-01_vi")     # families A / B (frame-setter)
E = importlib.import_module("build_2-02_vi")     # family E (pariññāvāra frame-setter), family B additions
C8 = importlib.import_module("build_8_vi")       # family D (moments)
assert X.F is F and X.E is E and X.C8 is C8

NAME = "6-02-sankharayamaka.md"
cap, low = S.cap, S.low
LABEL_VI = S.LABEL
SLIPS = []

# ================================================================ answer heads: the moments 6-01 did not meet
LAST = C8.citta(last=True)                       # pacchimacitta = tâm cuối cùng (8; = C8.P_SUBJ «Pacchimacittassa …»)
MOMENT_OF = dict(X.MOMENT_OF, **{
    "pacchimacittassa": LAST,
    "avitakkaavicārapacchimacittassa": X.LAST_AVITAKKA,            # 6-01 «tâm cuối cùng không có …»
    "kāmāvacarānaṃ pacchimacittassa": X.ANANTARA_K["kāmāvacarānaṃ"],  # 6-01 «tâm cuối cùng của chúng sinh trong cõi dục lạc»
})
_MOM_KEYS = "|".join(sorted(MOMENT_OF, key=len, reverse=True))


def _moment(g):
    return C8.AT.format(x=C8.OF.format(x=C8.MOMENT[g["t"]], c=MOMENT_OF[g["g"]]))


NEW_ITEMS = [
    (re.compile(rf"(?:vinā (?P<w>assāsapassāsehi|vitakkavicārehi) )?(?P<g>{_MOM_KEYS}) (?P<t>uppāda|bhaṅga)kkhaṇe"
                r"(?= |$)"), "time",
     lambda g: (X.VINA.format(t=_moment(g), w=X.VINA_W[g["w"]]) if g["w"] else _moment(g))),
]
ITEMS = NEW_ITEMS + X.ITEMS


def head(phrase):
    """build_6-01_vi.head() with the extra moments (same algorithm, same joins)."""
    s = low(phrase)
    pieces = []
    while s:
        for rx, kind, f in ITEMS:
            mm = rx.match(s)
            if mm:
                v = f(mm)
                if kind == "beings":
                    if pieces and pieces[-1][0] == "beings":
                        pieces[-1][1].append(v)
                    else:
                        pieces.append(["beings", [v]])
                elif kind == "ye":
                    assert pieces and pieces[-1][0] == "beings", phrase
                    pieces[-1][1][-1] += E.YE_CA_JOIN + v
                else:
                    pieces.append([kind, v])
                s = s[mm.end():].lstrip()
                break
        else:
            raise ValueError(f"unparsed head {phrase!r} at {s!r}")
    out = [C8.for_(F.LIST_SEP.join(v)) if k == "beings" else v for k, v in pieces]
    return ", ".join(out)


# ================================================================ source slip (translated as written)
# ^6-6-121 (Ka), second answer: «… tesaṃ tattha kāyasaṅkhāro na nirujjhittha vacīsaṅkhāro ca nirujjhissati.»
# The both-frame elsewhere has «kāyasaṅkhāro ca nirujjhittha»; «na» for «ca» changes the sense, so it is NOT
# corrected: the negative verb is rendered as written inside the both-frame («… chưa từng chấm dứt, đồng thời …»).
B_NA_CA_RE = re.compile(rf"(?P<g>.+?) (?P<r>{X.RES}) (?P<x>{X.MEM}) (?P<v1>na \S+) (?P<y>{X.MEM}) ca (?P<v2>{X.V})\.")
# ^6-6-132 (Ka) «yassa kāyasaṅkhāro nuppajjati tassa cittasaṅkhāro nirujjhatīti?»: the series has «na nirujjhati»
# (the answer says «no ca … na nirujjhati»); the question is translated as written (positive «chấm dứt»).
Q_SLIP = "(Ka) yassa kāyasaṅkhāro nuppajjati tassa cittasaṅkhāro nirujjhatīti?"

# ================================================================ editorial lines, headings, closing lines
UV = S.SECTION["uppādavāro"]                      # mục về sự sinh khởi
NV = S.SECTION["nirodhavāro"]                     # mục về sự chấm dứt
UNV = low(S.SECTION["Uppādanirodhavāro"])         # mục về sự sinh khởi và sự chấm dứt
PARINNA = low(S.SECTION["Pariññāvāro"])           # mục về sự hiểu biết trọn vẹn
ATITA_Q = "các câu hỏi về quá khứ"                # atītā pucchā (6-01)
PA_Q = "các câu hỏi về hiện tại và quá khứ"       # paccuppannātītā pucchā (SECTION Paccuppannātītavāro)
AA_Q = "các câu hỏi về quá khứ và tương lai"      # atītānāgatā pucchā (SECTION Atītānāgatavāro)
ANU_PAC = f"cả {low(S.SECTION['anulomaṃ'])} lẫn {low(S.SECTION['paccanīkaṃ'])}"   # anulomampi paccanīkampi (6-01)
PART = "phần {x}"                                 # <X>yamaka (as in yamaka_end «Phần {x} đã hoàn tất.»)


def part(pali_title):
    return PART.format(x=low(S.YAMAKA[pali_title]))


ASAMMOHA = "một cách không nhầm lẫn"              # asammohantena (new)
NOTE = {                                          # «…pe… (note).» bracket notes after a fragment (lowercase, as the Pāli)
    "itaresaṃ yatthakānaṃ sadisaṃ": f"giống như các {X.YATTHAKA} khác",
    "yassakampi yassayatthakampi sadisaṃ": f"{X.BOTH_SECTIONS} đều giống nhau",
}
EXACT = {
    "Āmantā.": S.AMANTA,
    "Natthi.": F.NATTHI,
    "No.": F.NO,
    "Nirodhavāro.": E.EXACT["Nirodhavāro."],                       # Mục về sự chấm dứt.
    "Uppādanirodhavāro.": E.EXACT["Uppādanirodhavāro."],           # Mục về sự sinh khởi và sự chấm dứt.
    **E.PARINNA_EXACT,                                             # Pariññāvāro. = Mục về sự hiểu biết trọn vẹn.
    "Saṅkhārayamakaṃ niṭṭhitaṃ.": S.yamaka_end("Saṅkhārayamakaṃ"),  # Phần các cặp câu hỏi về các tạo tác đã hoàn tất.
    "Namo tassa bhagavato arahato sammāsambuddhassa": S.HOMAGE,
    "(Yassakampi yassayatthakampi sadisaṃ, yassayatthake nirodhasamāpannānanti na labbhati).":
        f"({cap(X.BOTH_SECTIONS)} đều giống nhau, trong {X.YASSAYATTHAKA} thì không có {X.NIRODHA_CASE}).",
    "(Atītā pucchā uppādavārepi nirodhavārepi uppādanirodhavārepi sadisaṃ vitthāretabbā).":
        f"({cap(ATITA_Q)}, cả trong {UV}, trong {NV} lẫn trong {UNV}, đều nên được trình bày chi tiết giống nhau).",
    ("(Yathā uppādavāre paccuppannātītā pucchā anulomampi paccanīkampi vibhattā evaṃ uppādavāranirodhavārepi "
     "paccuppannātītā pucchā anulomampi paccanīkampi vibhajitabbā.)"):
        (f"(Như {PA_Q}, {ANU_PAC}, đã được phân tích trong {UV}, trong {UNV}, {PA_Q}, {ANU_PAC}, cũng nên được "
         f"phân tích như vậy.)"),
    ("(Yathā nirodhavāre atītānāgatā pucchā anulomampi paccanīkampi evaṃ uppādanirodhavārepi atītānāgatā pucchā "
     "anulomampi paccanīkampi vibhajitabbaṃ asammohantena nirodhavārena sadisaṃ, natthi nānākaraṇaṃ.)"):
        (f"(Như {AA_Q}, {ANU_PAC}, trong {NV}, thì trong {UNV}, {AA_Q}, {ANU_PAC}, cũng nên được phân tích "
         f"{ASAMMOHA}, giống như {NV}, không có sự khác biệt.)"),
    "(Yathā khandhayamake pariññāvāraṃ vibhattaṃ evaṃ saṅkhārayamakepi pariññāvāraṃ vibhajitabbaṃ.)":
        (f"(Như {PARINNA} đã được phân tích trong {part('Khandhayamakaṃ')}, trong {part('Saṅkhārayamakaṃ')}, "
         f"{PARINNA} cũng nên được phân tích như vậy.)"),
}
NOTE_RE = re.compile(r"(?P<f>.+?…pe…) \((?P<n>[^)]+)\)\.")
PLACE_PE_RE = re.compile(r"(?P<g>.+?) tattha…pe…")              # Dutiyajjhāne tatiyajjhāne tattha…pe…
HEADING = {
    "Pavatti 3. uppādanirodhavāro": f"{S.SECTION['Pavatti']} 3. {UNV}",          # = «Pavatti 2. nirodhavāro» (2-01)
    "1-6. Paccuppannavārādi": f"1-6. {S.ADI.format(x=S.SECTION['Paccuppannavāro'])}",  # sample «2-10. Hetuvārādi»
}


def heading(t):
    return HEADING[t] if t in HEADING else X.heading(t)


# ================================================================ sentence / line translation
def translate_sentence(s, ctx=""):
    if s in EXACT:
        return EXACT[s]
    if s == Q_SLIP:
        SLIPS.append((ctx, "(Ka) «… tassa cittasaṅkhāro nirujjhatīti?» without «na» (series and answer have "
                           "«na nirujjhati»); translated as written"))
    mm = NOTE_RE.fullmatch(s)
    if mm:
        f = mm["f"]
        mp = PLACE_PE_RE.fullmatch(f)
        if mp:
            frag = f"{cap(head(mp['g']))}, thì {F.RES_VI['tattha']}{E.PE}"
        else:
            frag = X.translate_sentence(f, ctx)
        return f"{frag} ({NOTE[mm['n']]})."
    r = E.translate_e(s, X.m)                     # family E (pariññāvāra)
    if r:
        return r
    mm = B_NA_CA_RE.fullmatch(s)
    if mm:
        SLIPS.append((ctx, "«kāyasaṅkhāro na nirujjhittha vacīsaṅkhāro ca nirujjhissati»: «na» where the both-frame "
                           "has «ca»; translated as written"))
        return F.b_both(mm["r"], head(mm["g"]), X.m(mm["x"]), F.vparse(mm["v1"], ctx), X.m(mm["y"]),
                        F.vparse(mm["v2"], ctx))
    for rx, both in ((X.B_NOT_RE, False), (X.B_BOTH_RE, True)):
        mm = rx.fullmatch(s)
        if mm:
            if not both:
                assert mm["r"] == mm["r2"], s
            f = F.b_both if both else F.b_not
            return f(mm["r"], head(mm["g"]), X.m(mm["x"]), F.vparse(mm["v1"], ctx), X.m(mm["y"]),
                     F.vparse(mm["v2"], ctx))
    return X.translate_sentence(s, ctx)


def translate_line(line, ctx=""):
    mm = re.match(r"^(?P<h>#+ )?(?P<t>.*?)(?P<id> \^[0-9A-Za-z-]+)?$", line)
    h, t, sid = mm["h"] or "", mm["t"], mm["id"] or ""
    if h:
        return h + heading(t) + sid
    if t in EXACT:
        return EXACT[t] + sid
    return " ".join(translate_sentence(s, ctx) for s in F.split_sentences(t)) + sid


def translate_file(name=NAME):
    src = (S.PALI_DIR / name).read_text(encoding="utf-8")
    out, seg = [], "start"
    for ln in src.splitlines():
        out.append(translate_line(ln, f"segment after ^{seg}") if ln.strip() else "")
        mid = re.search(r"\^([0-9A-Za-z-]+)\s*$", ln)
        if mid:
            seg = mid.group(1)
    text = "\n".join(out).rstrip("\n") + "\n"
    return re.sub(r"\n{3,}", "\n\n", text)


# ================================================================ checks
CROSS_BOOK = [
    ("phân tích", 2), ("ở đây cũng nên phân tích như vậy", 2), ("sự khác biệt", 5),
    ("nên được trình bày chi tiết", 2), ("hiểu biết trọn vẹn", 2), ("cõi dục lạc", 1), ("tầng thiền thứ hai", 1),
]


def check_cross_book():
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md")))
             for b, d in S.RAILS_DIR.items()}
    missing = [(s, b) for s, b in CROSS_BOOK if s not in texts[b]]
    for s, b in missing:
        print(f"CROSS-BOOK MISSING in pi-{b}: {s}")
    assert not missing, f"{len(missing)} cross-book strings not found"
    print(f"cross-book asserts (6-02): {len(CROSS_BOOK)} strings found in pi-1..5 rails")


def _sentences(text):
    for p in text.splitlines():
        if not p.strip() or p.startswith("#"):
            continue
        p = re.sub(r"\s*\^[\w-]+$", "", p)
        if p in EXACT or p in getattr(X, "EXACT", {}):
            yield p
            continue
        yield from F.split_sentences(p)


def check_frame_setters():
    """Every answer head 6-01's head() can parse comes out byte-identical here (6-01 and 6-02 Pāli); the 8 heads too."""
    n = 0
    for name in (X.NAME, NAME):
        for s in _sentences((S.PALI_DIR / name).read_text(encoding="utf-8")):
            for rx in (X.B_NOT_RE, X.B_BOTH_RE, B_NA_CA_RE):
                mm = rx.fullmatch(s)
                if mm:
                    try:
                        old = X.head(mm["g"])
                    except ValueError:
                        break
                    assert head(mm["g"]) == old, (mm["g"], head(mm["g"]), old)
                    n += 1
                    break
    for p in ("Pacchimacittassa uppādakkhaṇe", "Pacchimacittassa bhaṅgakkhaṇe"):
        assert head(p) == C8.P_SUBJ[p], (p, head(p), C8.P_SUBJ[p])
    assert E.translate_e("(Ka) yo rūpakkhandhaṃ parijānāti so vedanākkhandhaṃ parijānātīti?", F.m) == \
        "(a) Người nào hiểu biết trọn vẹn khối vật chất, thì có phải người ấy hiểu biết trọn vẹn khối cảm giác không?"
    print(f"frame-setter checks: OK ({n} heads identical to build_6-01_vi.head)")


def check_repeats(pali):
    """Identical Pāli sentence -> identical Vietnamese, within 6-02 and against 6-01 / 2-01 / 2-02."""
    seen, bad = {}, 0
    for s in _sentences(pali):
        t = translate_sentence(s)
        if seen.setdefault(s, t) != t:
            print("DIFFERS WITHIN 6-02:", s)
            bad += 1
    shared = 0
    for mod in (X, F, E):
        other = set(_sentences((S.PALI_DIR / mod.NAME).read_text(encoding="utf-8")))
        for s in other & set(seen):
            shared += 1
            t = mod.EXACT[s] if s in getattr(mod, "EXACT", {}) else mod.translate_sentence(s, "")
            if t != seen[s]:
                print(f"DIFFERS FROM {mod.NAME}:", s, "|", t, "|", seen[s])
                bad += 1
    print(f"repeat check: {len(seen)} distinct sentences, {shared} shared with 6-01 / 2-01 / 2-02")
    return bad


def main():
    S.check_cross_book()
    F.check_cross_book()
    E.check_cross_book()
    X.check_cross_book()
    check_cross_book()
    check_frame_setters()
    SLIPS.clear(); X.SLIPS.clear(); F.SLIPS.clear(); E.SLIPS.clear()
    text = unicodedata.normalize("NFC", translate_file())
    slips = list(F.SLIPS + X.SLIPS + SLIPS) + [("", w) for w in E.SLIPS]
    pali = (S.PALI_DIR / NAME).read_text(encoding="utf-8")
    probs = S.check_lines(pali, text, NAME)
    for bad in ("….", ".…", "?…", ",…", "  ", "là là", "—", ":-", "f", "j", "w", "z"):
        assert bad not in text, bad
    assert check_repeats(pali) == 0, "identical Pāli rendered differently"
    with open(S.OUT_DIR / NAME, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    vl = [x for x in text.splitlines() if x.strip()]
    segs = len(re.findall(r"\^[0-9A-Za-z-]+\s*$", text, flags=re.M))
    print(f"wrote {NAME}: {len(vl)} lines, {segs} segments")
    for c, w in dict.fromkeys(slips):
        print("SLIP", c, "|", w)
    for p in probs[:80]:
        print("PROBLEM", p)
    print("line checks:", "OK" if not probs else f"{len(probs)} problems")
    sys.exit(1 if probs else 0)


if __name__ == "__main__":
    main()
