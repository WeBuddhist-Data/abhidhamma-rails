# -*- coding: utf-8 -*-
"""pi-6 (Yamaka) Vietnamese zero-shot, chapter 3-03-ayatanayamaka.md (Āyatanayamaka, pavattivāra continued:
(5) paccuppannānāgatavāra and (6) atītānāgatavāra of the uppādavāra).

Frames: build_3-02_vi (who32, run_q, the sentence frames), build_3-01_vi (members, «…pe…» lines, attribute beings,
mūlaka notes, headings), build_2-01_vi (families A / B) and build_2-02_vi (who2, YE_CA_CAVANTA), all imported and used
verbatim. New here (see notes-3-03.md): «ye ca <P>ṃ [<P2>ṃ] upapajjitvā parinibbāyissanti tesaṃ upapajjantānaṃ»
(YE_CA_UPAPAJJANTA), plane lists inside the «ye ca …» groups, the question cut in its middle
«(Kha) yassa vā pana [yattha] [X]…pe… uppajjitthāti?» (pe_q), and «Uppādavāro.».

    import sys, importlib; sys.path.insert(0, r"D:\\Work\\OpenPecha\\abhidhamma-rails\\0-INBOX\\temp\\pipeline\\pi-6-vi-ai")
    A33 = importlib.import_module("build_3-03_vi")
    A33.who33(phrase) / A33.pe_q(sentence, ctx) / A33.translate_line(line, ctx)

Importing writes nothing; run  python -I -X utf8 -B build_3-03_vi.py  to rebuild the chapter
(python -I -X utf8 -B build_3-03_vi.py --probe  lists unparsed lines without writing).
"""
import importlib
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai")
import build_sample_vi as S  # noqa: E402
F = importlib.import_module("build_2-01_vi")      # families A / B (frame-setter)
E = importlib.import_module("build_2-02_vi")      # who2, YE_CA_CAVANTA, YE_CA_JOIN (frame-setter)
A3 = importlib.import_module("build_3-01_vi")     # Āyatana members, «…pe…», attribute beings (frame-setter)
A32 = importlib.import_module("build_3-02_vi")    # who32, run_q (frame-setter of this yamaka's pavattivāra)

NAME = "3-03-ayatanayamaka.md"
cap, low = S.cap, S.low
LABEL = S.LABEL
SLIPS = []

# ================================================================ beings (family B additions)
YE_CA_UPAPAJJANTA = "những người đang tái sinh mà sau khi tái sinh vào {p} sẽ nhập Niết-bàn trọn vẹn"
# ye ca <P>ṃ upapajjitvā parinibbāyissanti tesaṃ upapajjantānaṃ (new; = 2-02 YE_CA_CAVANTA with «đang tái sinh» for
# «đang chết đi»: the PARTICIPLE word of 2-01)
assert E.YE_CA_CAVANTA.replace(F.PARTICIPLE["cavantānaṃ"][0], F.PARTICIPLE["upapajjantānaṃ"][0]) == YE_CA_UPAPAJJANTA
YE_TAIL = {None: F.YE_UPAPAJJITVA, "cavantānaṃ": E.YE_CA_CAVANTA, "upapajjantānaṃ": YE_CA_UPAPAJJANTA}
YE_CA_RE = re.compile(r"(?P<ps>\S+(?: \S+)*?) upapajjitvā parinibbāyissanti(?: tesaṃ (?P<c>cavantānaṃ|upapajjantānaṃ))?")


def _acc_planes(ps, phrase):
    out = []
    for x in ps.split():
        case, stem = F._plane_case(low(x))
        assert case == "acc", phrase
        out.append(F.PLANE[stem])
    return F.LIST_SEP.join(out)                     # 2-01 LIST_SEP (3-02 «vào cõi hình sắc, cõi không hình sắc»)


def who33(phrase):
    """Beings phrase -> Vietnamese head. 3-02 who32 (hence 3-01 who3 / 2-02 who2 / 2-01 who) wherever it applies,
    byte-identical; new: the «ye ca …» group with a plane list or with «tesaṃ upapajjantānaṃ»."""
    if " ye ca " not in phrase:
        return A32.who32(phrase)
    left, right = phrase.split(" ye ca ", 1)
    mm = YE_CA_RE.fullmatch(right)
    if not mm:
        raise ValueError(f"unparsed ye ca group {phrase!r}")
    out = A32.who32(left) + E.YE_CA_JOIN + YE_TAIL[mm["c"]].format(p=_acc_planes(mm["ps"], phrase))
    try:
        old = E.who2(phrase)
    except (AssertionError, ValueError, KeyError):
        old = None
    if old is not None:
        assert old == out, (phrase, old, out)       # where 2-02 covers the phrase, say exactly what 2-02 says
    return out


# ================================================================ sentences (3-02 tr_sentence with who33)
V = A32.V
B_NOT_RE, B_BOTH_RE = A32.B_NOT_RE, A32.B_BOTH_RE


def tr_sentence(s, ctx):
    if s in EXACT_LINE_BODY:
        return EXACT_LINE_BODY[s]
    body, punct = (s[:-1], s[-1]) if s and s[-1] in ".?" else (s, "")
    for rx, both in ((B_NOT_RE, False), (B_BOTH_RE, True)):
        mm = rx.fullmatch(body)
        if mm and punct == ".":
            res = mm["res"]
            if not both:
                assert res == mm["res2"], body
            head = A3.where3(mm["g"]) if res == "tattha" else who33(mm["g"])
            x = A3.m(mm["x"] + ("ṃ" if both else ""))
            y = A3.m(mm["y"] + ("ṃ" if both else ""))
            f = F.b_both if both else F.b_not
            return f(res, head, x, F.vparse(mm["v1"], ctx), y, F.vparse(mm["v2"], ctx))
    return A3.tr(body, punct, ctx)


def tr_sentences(text, ctx):
    return " ".join(tr_sentence(x.strip(), ctx) for x in F.split_sentences(text) if x.strip())


# a question cut in its middle: «(Kha) yassa vā pana [yattha] [X]…pe… uppajjitthāti?» (new)
PE_Q_RE = re.compile(r"(?:\((?P<l>Ka|Kha)\) )?(?P<w>[Yy]assa vā pana yattha|[Yy]assa vā pana)(?: (?P<x>\S+āyatanaṃ))?"
                     r"…pe… (?P<v>" + V + r")\?")
Q_TAIL = "{pb} không?"                    # the end of the 7-01 Q_FRAME «…, thì {dem} có phải {b} {pb} không?»
assert F.Q_FRAME.endswith(" " + Q_TAIL)


def pe_q(s, ctx):
    """(Kha) yassa vā pana…pe… uppajjitthāti? = (b) Còn ở người nào… đã sinh khởi không?  The head is 8 / 6-01
    «Còn ở người nào…» (+ «mà X» when X is written); the tail is the end of Q_FRAME."""
    mm = PE_Q_RE.fullmatch(s)
    if not mm:
        return None
    kind = low(mm["w"]).replace(" vā pana", "")
    head = F.VA_PANA + F.REL_VI[kind] + (f" mà {A3.m(mm['x'])}" if mm["x"] else "")
    out = cap(head) + E.PE + " " + Q_TAIL.format(pb=F.verb(*F.vparse(mm["v"], ctx)))
    return f"{LABEL[mm['l']]} {out}" if mm["l"] else out


# ================================================================ closing lines
EXACT_LINE_BODY = {
    "Uppādavāro.": cap(S.SECTION["uppādavāro"]) + ".",      # Mục về sự sinh khởi. (= 2-02 «Nirodhavāro.», 5-01, 6-01)
}

# ================================================================ source slips rendered as meant (each applies once)
SLIP_FIX = [
    ("tesaṃ manāyatanañca uppajjati, dhammāyatanañca uppajjissati.",
     "tesaṃ manāyatanañca uppajjati dhammāyatanañca uppajjissati.",
     "^6-3-89: comma inside the «A ca … B ca …» clause; the Vietnamese both-frame has its comma anyway (2-02 ^6-2-151)"),
    ("tesaṃ tattha manāyatanaṃ nuppajjissati cakkhāyatanañca nuppajjati.",
     "tesaṃ tattha manāyatanañca nuppajjissati cakkhāyatanañca nuppajjati.",
     "^6-3-100: «manāyatanaṃ nuppajjissati cakkhāyatanañca …»: first «ca» missing; rendered with the both-frame"),
    ("tesaṃ tattha cakkhāyatanañca nuppajjittha dhammāyatanaṃ nuppajjissati.",
     "tesaṃ tattha cakkhāyatanañca nuppajjittha dhammāyatanañca nuppajjissati.",
     "^6-3-116: «cakkhāyatanañca nuppajjittha dhammāyatanaṃ …»: second «ca» missing; rendered with the both-frame"),
    ("(Ka) yassa =93 yattha rūpāyatanaṃ", "(Ka) yassa yattha rūpāyatanaṃ",
     "^6-3-118: stray «=93» (a page / paragraph marker) inside the question; dropped"),
]
SLIP_USED = {}


def fix_slips(s):
    for a, b, why in SLIP_FIX:
        if a in s:
            s = s.replace(a, b)
            SLIP_USED[why] = SLIP_USED.get(why, 0) + 1
    return s


# ================================================================ lines
def translate_line(line, ctx):
    mm = re.match(r"^(?P<h>#+ )?(?P<t>.*?)(?P<id> \^[0-9A-Za-z-]+)?$", line)
    h, t, sid = mm["h"] or "", mm["t"], mm["id"] or ""
    if h:
        return h + A3.heading(t) + sid
    t = fix_slips(t)
    if t in EXACT_LINE_BODY:
        return EXACT_LINE_BODY[t] + sid
    r = A32.run_q(t, ctx)                            # «…pe…» runs inside one question (3-02)
    if r:
        return r + sid
    if "…" in t:
        sents = [x.strip() for x in F.split_sentences(t) if x.strip()]
        if any(PE_Q_RE.fullmatch(x) for x in sents):
            out = []
            for x in sents:
                out.append(pe_q(x, ctx) or (A3.tr_pe(x, ctx) if "…" in x else tr_sentence(x, ctx)))
            return " ".join(out) + sid
        return A3.tr_pe(t, ctx) + sid
    return tr_sentences(t, ctx) + sid


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
CROSS_BOOK = [("tái sinh", 2), ("nhập Niết-bàn trọn vẹn", 5), ("sau khi", 2), ("cõi không hình sắc", 1),
              ("cõi hình sắc", 1), ("cõi dục lạc", 1)]


def check_cross_book():
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md")))
             for b, d in S.RAILS_DIR.items()}
    missing = [(s, b) for s, b in CROSS_BOOK if s not in texts[b]]
    for s, b in missing:
        print(f"CROSS-BOOK MISSING in pi-{b}: {s} (found in: {[k for k, v in texts.items() if s in v]})")
    assert not missing, f"{len(missing)} cross-book strings not found"
    print(f"cross-book asserts (3-03): {len(CROSS_BOOK)} strings found in pi-1..5 rails")


def _sentences(text):
    for p in text.splitlines():
        if not p.strip() or p.startswith("#") or "…" in p:
            continue
        p = re.sub(r"\s*\^[\w-]+$", "", fix_slips(p))
        yield from (x.strip() for x in F.split_sentences(p) if x.strip())


def check_repeats(pali):
    """Identical Pāli sentence -> identical Vietnamese, within 3-03 and against the 3-01 / 3-02 output files."""
    seen, bad = {}, 0
    for s in _sentences(pali):
        t = tr_sentence(s, "")
        if seen.setdefault(s, t) != t:
            bad += 1
    shared = 0
    for other, fix in (("3-01-ayatanayamaka.md", lambda x: x), ("3-02-ayatanayamaka.md", A32.fix_slips)):
        po = (S.PALI_DIR / other).read_text(encoding="utf-8").splitlines()
        vo = (S.OUT_DIR / other).read_text(encoding="utf-8").splitlines()
        assert len(po) == len(vo)
        for pl, vl in zip(po, vo):
            pl2 = re.sub(r"\s*\^[\w-]+$", "", fix(pl))
            vl2 = re.sub(r"\s*\^[\w-]+$", "", vl)
            if not pl2.strip() or pl.startswith("#") or "…" in pl or "sadisa" in pl2:
                continue
            ps = [x.strip() for x in F.split_sentences(pl2) if x.strip()]
            if not any(x in seen for x in ps):
                continue
            try:
                mine = " ".join(seen.get(x) or tr_sentence(x, "") for x in ps)
            except (ValueError, AssertionError, KeyError):
                print("NOT COMPARABLE:", other, pl2[:80])
                continue
            shared += 1
            if mine != vl2:
                print("DIFFERS FROM", other, ":", pl2[:80])
                bad += 1
    print(f"repeat check: {len(seen)} distinct sentences, {shared} lines shared with 3-01 / 3-02 checked")
    return bad


def probe(name=NAME):
    src = (S.PALI_DIR / name).read_text(encoding="utf-8")
    bad = 0
    for i, ln in enumerate(src.splitlines(), 1):
        if not ln.strip():
            continue
        try:
            translate_line(ln, f"line {i}")
        except Exception as ex:  # noqa: BLE001
            bad += 1
            print(f"FAIL line {i}: {type(ex).__name__}: {str(ex)[:200]}")
    print("probe failures:", bad)


def main():
    S.check_cross_book()
    F.check_cross_book()
    A3.check_cross_book()
    A32.check_cross_book()
    check_cross_book()
    SLIPS.clear(); F.SLIPS.clear(); SLIP_USED.clear()
    text = unicodedata.normalize("NFC", translate_file())
    used = dict(SLIP_USED)
    chapter_slips = list(F.SLIPS)
    pali = (S.PALI_DIR / NAME).read_text(encoding="utf-8")
    probs = S.check_lines(pali, text, NAME) + A3.check_extra(text)
    for bad in ("….", ".…", "?…", ",…", "  ", "là là", "—", ":-", "=93"):
        assert bad not in text, bad
    assert check_repeats(pali) == 0, "identical Pāli rendered differently"
    for a, b, why in SLIP_FIX:
        assert used.get(why) == 1, (why, used.get(why))
    with open(S.OUT_DIR / NAME, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    segs = len(re.findall(r"\^[0-9A-Za-z-]+\s*$", text, flags=re.M))
    print(f"wrote {NAME}: {len([x for x in text.splitlines() if x.strip()])} lines, {segs} segments")
    for why in used:
        print("SLIP", why)
    seen = set()
    for c, w in chapter_slips + [("", x) for x in SLIPS]:
        if (c, w) not in seen:
            seen.add((c, w))
            print("SLIP", c, "|", w)
    for p in probs[:80]:
        print("PROBLEM", p)
    print("line checks:", "OK" if not probs else f"{len(probs)} problems")
    sys.exit(1 if probs else 0)


if __name__ == "__main__":
    if "--probe" in sys.argv:
        probe()
    else:
        main()
