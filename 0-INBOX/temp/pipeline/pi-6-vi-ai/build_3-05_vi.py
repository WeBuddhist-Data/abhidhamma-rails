# -*- coding: utf-8 -*-
"""pi-6 (Yamaka) Vietnamese zero-shot, chapter 3-05-ayatanayamaka.md (Āyatanayamaka, pavattivāra continued:
nirodhavāra (5) paccuppannānāgatavāra and (6) atītānāgatavāra; uppādanirodhavāra (1) paccuppannavāra and the start
of (2) atītavāra).

Frames: build_3-03_vi (who33, pe_q, tr_sentence), build_3-02_vi (who32, run_q), build_3-01_vi (members, «…pe…» lines,
attribute beings, mūlaka notes, headings), build_2-01_vi (families A / B), build_2-02_vi (Nirodhavāro., PE, who2) and
build_8_vi («Còn ở người nào…?», «Đúng vậy…»), all imported and used verbatim. New here (see notes-3-05.md): the
«<beings> tesaṃ [tattha]…pe…» answer fragment (TESAM_PE), the question cut before its verb «(Kha) yassa vā pana
[yattha] X…pe….» (pe_head), and three editorial notes.

    import sys, importlib; sys.path.insert(0, r"D:\\Work\\OpenPecha\\abhidhamma-rails\\0-INBOX\\temp\\pipeline\\pi-6-vi-ai")
    A35 = importlib.import_module("build_3-05_vi")
    A35.translate_line(line, ctx) / A35.tesam_pe(phrase) / A35.pe_head(sentence, ctx)

Importing writes nothing; run  python -I -X utf8 -B build_3-05_vi.py  to rebuild the chapter
(python -I -X utf8 -B build_3-05_vi.py --probe  lists unparsed lines without writing).
"""
import importlib
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai")
import build_sample_vi as S  # noqa: E402
F = importlib.import_module("build_2-01_vi")      # families A / B (frame-setter)
E = importlib.import_module("build_2-02_vi")      # Nirodhavāro., PE, who2 (frame-setter)
A3 = importlib.import_module("build_3-01_vi")     # Āyatana members, «…pe…», notes (frame-setter of this yamaka)
A32 = importlib.import_module("build_3-02_vi")    # who32, run_q
A33 = importlib.import_module("build_3-03_vi")    # who33, pe_q, tr_sentence
C8 = importlib.import_module("build_8_vi")        # «Còn ở người nào…?» (frame-setter, family D)

NAME = "3-05-ayatanayamaka.md"
cap, low = S.cap, S.low
LABEL = S.LABEL
PE = E.PE                                          # …pe… = … (sample)

# ================================================================ fragments (new)
# «<beings> tesaṃ [tattha]…pe…» = «Ở <beings>, thì ở những người ấy[, ở nơi ấy]…» (the head of the 7-01
# STATEMENT_RES frame; = 8 «Itaresaṃ … tesaṃ…pe…. = Ở những người khác, …, thì ở những người ấy…»)
RES_HEAD = "{head}, thì {res}"
assert F.STATEMENT_RES.startswith(RES_HEAD + " ")
TESAM_RE = re.compile(r"(?P<g>.+?) (?P<res>tesaṃ tattha|tesaṃ)")


def tesam_pe(body):
    mm = TESAM_RE.fullmatch(body)
    if not mm:
        return None
    out = RES_HEAD.format(head=A33.who33(mm["g"]), res=F.RES_VI[mm["res"]])
    return cap(out) if body[:1].isupper() else out


# a question cut before its verb: «(Kha) yassa vā pana [yattha] X…pe…» / «Yassa yattha X v…pe…» (new for the
# first; the head is 3-03 pe_q's «Còn ở người nào [, ở nơi nào] mà X»; with a verb = 3-01 b_head / 6-01)
HEAD_RE = re.compile(r"(?:\((?P<l>Ka|Kha)\) )?(?P<w>[Yy]assa vā pana yattha|[Yy]assa yattha|[Yy]assa vā pana|"
                     r"[Yy]attha|[Yy]assa) (?P<x>\S+āyatanaṃ)(?: (?P<v>(?:na )?\S+))?")


def pe_head(body, ctx):
    mm = HEAD_RE.fullmatch(body)
    if not mm:
        return None
    kind = low(mm["w"]).replace(" vā pana", "")
    head = F.REL_VI[kind] + f" mà {A3.m(mm['x'])}" + (f" {F.verb(*F.vparse(mm['v'], ctx))}" if mm["v"] else "")
    if "vā pana" in mm["w"]:
        head = F.VA_PANA + head
    out = cap(head) if (mm["l"] or body[:1].isupper()) else head
    return f"{LABEL[mm['l']]} {out}" if mm["l"] else out


# «(Kha) yassa vā pana…pe…?» = «(b) Còn ở người nào…?» (8; 5-01, 6-01)
PE_Q0_RE = re.compile(r"(?:\((?P<l>Ka|Kha)\) )?(?P<w>[Yy]assa vā pana yattha|[Yy]assa vā pana|[Yy]attha vā pana)"
                      r"…pe…\?")
PE_Q0 = "{h}" + PE + "?"
assert C8.EXACT_LINE["Yassa vā pana…pe…? Āmantā …pe…."].startswith(
    PE_Q0.format(h=cap(F.VA_PANA + F.REL_VI["yassa"])) + " ")


def pe_q0(s):
    mm = PE_Q0_RE.fullmatch(s)
    if not mm:
        return None
    kind = low(mm["w"]).replace(" vā pana", "")
    out = PE_Q0.format(h=cap(F.VA_PANA + F.REL_VI[kind]))
    return f"{LABEL[mm['l']]} {out}" if mm["l"] else out


# ================================================================ editorial notes and closing lines (new)
YASSAKA, YATTHAKA = A3.YASSAKA, A3.YATTHAKA                   # phần về người / phần về nơi chốn (3-01)
YASSAYATTHAKA = "phần về người và nơi chốn"                  # yassayatthaka (6-01)
TIME_PA = low(S.SECTION["Paccuppannātītavāro"])              # mục về hiện tại và quá khứ
NOTE_BODY = {
    # (yathā paccuppannātītepi tividhaṃ vitthāritaṃ evaṃ idampi vitthāretabbaṃ) ^6-3-171 (lowercase as the Pāli)
    "(yathā paccuppannātītepi tividhaṃ vitthāritaṃ evaṃ idampi vitthāretabbaṃ)":
        f"(như {TIME_PA} đã được trình bày chi tiết theo ba cách, phần này cũng nên được trình bày chi tiết "
        f"như vậy)",
    # ^6-3-201 (3-01 «nên trả lời: Đúng vậy» for āmantāti kātabbaṃ; 5-01 «nên được trình bày giống như»)
    ("(yatthakaṃ noti na kātabbaṃ, yatthakaṃ itaresaṃ yatthakānaṃ sadisaṃ kātabbaṃ, yatthakaṃ tīsupi vāresu "
     "sadisaṃ)"):
        f"(ở {YATTHAKA} không {A3.TABBA} trả lời: {F.NO[:-1]}, {YATTHAKA} {A3.TABBA} được trình bày giống như "
        f"các {YATTHAKA} khác, {YATTHAKA} thì giống nhau trong cả ba mục)",
    # ^6-3-209 (= 6-01 / 6-02 «(Phần về người và phần về người và nơi chốn đều giống nhau)»)
    "(Yassakampi yassayatthakampi sadisaṃ)": f"({cap(YASSAKA)} và {YASSAYATTHAKA} đều giống nhau)",
    # ^6-3-210 (6-01 / 6-02 / 3-04 «các câu hỏi về quá khứ», «cả chiều thuận lẫn chiều nghịch», «đều giống nhau»;
    # bare uppādepi … = 3-04 «ở sự sinh khởi, ở sự chấm dứt, ở sự sinh khởi và sự chấm dứt», not uppādavārepi …)
    "(Atītā pucchā uppādepi nirodhepi uppādanirodhepi anulomampi paccanīkampi sadisaṃ)":
        (f"(Các câu hỏi về quá khứ, ở sự sinh khởi, ở sự chấm dứt, ở sự sinh khởi và sự chấm dứt, cả "
         f"{low(S.SECTION['anulomaṃ'])} lẫn {low(S.SECTION['paccanīkaṃ'])}, đều giống nhau)"),
    "No": F.NO[:-1],                                           # Không (7-01)
}
EXACT_LINE = {
    "Nirodhavāro.": E.EXACT["Nirodhavāro."],                   # Mục về sự chấm dứt. (2-02)
}
UNV = low(S.SECTION["Uppādanirodhavāro"])                       # mục về sự sinh khởi và sự chấm dứt
HEAD5 = {"Pavatti 3. uppādanirodhavāro": f"{S.SECTION['Pavatti']} 3. {UNV}"}   # = 6-02


def heading(t):
    return HEAD5.get(t) or A3.heading(t)


# ================================================================ source slips rendered as meant (each applies once)
SLIP_FIX = [
    ("Kāmāvacare parinibbāntānaṃ tesaṃ tattha…pe….", "Kāmāvacare parinibbantānaṃ tesaṃ tattha…pe….",
     "^6-3-172: «parinibbāntānaṃ» = parinibbantānaṃ (spelling)"),
    ("tassa manāyatana…pe… dhammāyatanaṃ nirujjhissatīti?", "tassa manāyatanaṃ…pe… dhammāyatanaṃ nirujjhissatīti?",
     "^6-3-186: «manāyatana…pe…» lacks its «ṃ»; read as manāyatanaṃ"),
    ("asaññasattānaṃ tesaṃ tattha manāyatanañca na nirujjhissati, cakkhāyatanañca na nirujjhittha.",
     "asaññasattānaṃ tesaṃ tattha manāyatanañca na nirujjhissati cakkhāyatanañca na nirujjhittha.",
     "^6-3-195: comma inside the «A ca … B ca …» clause; the Vietnamese both-frame has its comma anyway (3-03 ^6-3-89)"),
]
SPACE_FIX = [   # «Āmantā …pe….» / «No …pe….»: the space before «…pe…» is dropped (8 ^6-8-61 / ^6-8-115 «Đúng vậy…»)
    ("? No …pe….", "? No…pe….", "^6-3-199, ^6-3-202: «No …pe….» rendered «Không…» (no space, as 8)"),
    ("? Āmantā …pe….", "? Āmantā…pe….", "^6-3-210: «Āmantā …pe….» rendered «Đúng vậy…» (as 8)"),
]
SLIP_USED = {}


def fix_slips(s):
    for a, b, why in SLIP_FIX + SPACE_FIX:
        if a in s:
            s = s.replace(a, b)
            SLIP_USED[why] = SLIP_USED.get(why, 0) + 1
    return s


# ================================================================ sentences
def tr_sentence(s, ctx, pe=False):
    """One Pāli sentence (with its final punctuation, if any). Whole sentences go to 3-03 tr_sentence (hence 3-02 /
    3-01 / 2-01 frames, byte-identical); the pieces of a «…pe…» line also try the fragments."""
    body, punct = (s[:-1], s[-1]) if s and s[-1] in ".?" else (s, "")
    if body in NOTE_BODY:
        return NOTE_BODY[body] + punct
    if pe and not punct:
        r = tesam_pe(body)
        if r:
            return r
    try:
        return A33.tr_sentence(s, ctx)
    except ValueError:
        if not pe:
            raise
    try:
        return A3.tr(body, punct, ctx, pe=True)
    except ValueError:
        pass
    r = pe_head(body, ctx)
    if r:
        return r + punct
    raise ValueError(f"unmatched piece {s!r} ({ctx})")


def tr_sentences(text, ctx, pe=False):
    return " ".join(tr_sentence(x.strip(), ctx, pe) for x in F.split_sentences(text) if x.strip())


def tr_pe(text, ctx):
    """A sentence with «…pe…» / «…» (3-01 tr_pe logic, with this chapter's pieces): each piece between the ellipses
    is translated in place; a period next to the ellipsis gives way to it; «?…» is written «? …»."""
    pieces = []
    for chunk in A3.PE_SPLIT.split(text):
        lead = chunk[:len(chunk) - len(chunk.lstrip())]
        trail = chunk[len(chunk.rstrip()):]
        core = chunk.strip()
        pieces.append(lead + (tr_sentences(core, ctx, pe=True) if core else "") + trail)
    out = "…".join(pieces)
    prev = None
    while prev != out:
        prev = out
        out = out.replace(".…", "…").replace("….", "…").replace("?…", "? …")
    return out


def translate_sentence(s, ctx):
    if s in EXACT_LINE:
        return EXACT_LINE[s]
    r = pe_q0(s)
    if r:
        return r
    if A33.PE_Q_RE.fullmatch(s):
        return A33.pe_q(s, ctx)
    if "…" in s:
        return tr_pe(s, ctx)
    return tr_sentence(s, ctx)


def run_q(t, ctx):
    """3-02 run_q (a «…pe…» run inside one question); the answer after it goes through this chapter's sentences."""
    mm = A32.RUN_Q_RE.fullmatch(t)
    if not mm or "…" not in mm["xs"] + mm["ys"]:
        return None
    rest = mm["rest"]
    q = A32.run_q(t[:len(t) - len(rest)], ctx)
    rest = rest.strip()
    return q + (" " + " ".join(translate_sentence(x.strip(), ctx) for x in F.split_sentences(rest) if x.strip())
                if rest else "")


def translate_line(line, ctx):
    mm = re.match(r"^(?P<h>#+ )?(?P<t>.*?)(?P<id> \^[0-9A-Za-z-]+)?$", line)
    h, t, sid = mm["h"] or "", mm["t"], mm["id"] or ""
    if h:
        return h + heading(t) + sid
    t = fix_slips(t)
    if t in EXACT_LINE:
        return EXACT_LINE[t] + sid
    r = run_q(t, ctx)
    if r:
        return r + sid
    return " ".join(translate_sentence(x.strip(), ctx) for x in F.split_sentences(t) if x.strip()) + sid


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
CROSS_BOOK = [("nên được trình bày chi tiết", 2), ("đã được trình bày chi tiết", 2), ("giống nhau", 5),
              ("tái sinh", 2), ("chết đi", 2), ("nhập Niết-bàn trọn vẹn", 5), ("cõi dục lạc", 1),
              ("cõi hình sắc", 1), ("cõi không hình sắc", 1), ("câu hỏi", 5), ("chi tiết", 2)]


def check_cross_book():
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md")))
             for b, d in S.RAILS_DIR.items()}
    missing = [(s, b) for s, b in CROSS_BOOK if s not in texts[b]]
    for s, b in missing:
        print(f"CROSS-BOOK MISSING in pi-{b}: {s} (found in: {[k for k, v in texts.items() if s in v]})")
    assert not missing, f"{len(missing)} cross-book strings not found"
    print(f"cross-book asserts (3-05): {len(CROSS_BOOK)} strings found in pi-1..5 rails")


def check_shared_notes():
    """The editorial notes this chapter shares with finished chapters say what those chapters say."""
    v601 = (S.OUT_DIR / "6-01-sankharayamaka.md").read_text(encoding="utf-8")
    assert NOTE_BODY["(Yassakampi yassayatthakampi sadisaṃ)"][:-1] in v601     # 6-01 ^6-6-23 (its «.» inside)
    v602 = (S.OUT_DIR / "6-02-sankharayamaka.md").read_text(encoding="utf-8")
    assert "(Các câu hỏi về quá khứ, cả trong " in v602
    p304 = S.OUT_DIR / "3-04-ayatanayamaka.md"
    if p304.exists():
        v304 = p304.read_text(encoding="utf-8")
        for piece in ("ở sự sinh khởi, ở sự chấm dứt, ở sự sinh khởi và sự chấm dứt", "các câu hỏi về quá khứ",
                      "cả chiều thuận lẫn chiều nghịch"):
            assert piece in v304, piece
    v801 = (S.OUT_DIR / "8-cittayamaka.md").read_text(encoding="utf-8")
    assert "Còn ở người nào…? Đúng vậy…" in v801 and "thì ở những người ấy…" in v801


def _sentences(text):
    for p in text.splitlines():
        if not p.strip() or p.startswith("#") or "…" in p:
            continue
        p = re.sub(r"\s*\^[\w-]+$", "", fix_slips(p))
        yield from (x.strip() for x in F.split_sentences(p) if x.strip())


def check_repeats(pali):
    """Identical Pāli sentence -> identical Vietnamese, within 3-05 and against the 3-01 … 3-04 output files."""
    seen, bad = {}, 0
    for s in _sentences(pali):
        t = translate_sentence(s, "")
        if seen.setdefault(s, t) != t:
            bad += 1
    shared = 0
    others = [("3-01-ayatanayamaka.md", lambda x: x), ("3-02-ayatanayamaka.md", A32.fix_slips),
              ("3-03-ayatanayamaka.md", A33.fix_slips)]
    if (S.OUT_DIR / "3-04-ayatanayamaka.md").exists():
        others.append(("3-04-ayatanayamaka.md", lambda x: x))
    for other, fix in others:
        po = (S.PALI_DIR / other).read_text(encoding="utf-8").splitlines()
        vo = (S.OUT_DIR / other).read_text(encoding="utf-8").splitlines()
        if len(po) != len(vo):
            print("NOT COMPARABLE (line counts differ):", other)
            continue
        for pl, vl in zip(po, vo):
            pl2 = re.sub(r"\s*\^[\w-]+$", "", fix(pl))
            vl2 = re.sub(r"\s*\^[\w-]+$", "", vl)
            if not pl2.strip() or pl.startswith("#") or "…" in pl or "sadisa" in pl2:
                continue
            ps = [x.strip() for x in F.split_sentences(pl2) if x.strip()]
            if not any(x in seen for x in ps):
                continue
            try:
                mine = " ".join(seen.get(x) or translate_sentence(x, "") for x in ps)
            except (ValueError, AssertionError, KeyError):
                print("NOT COMPARABLE:", other, pl2[:80])
                continue
            shared += 1
            if mine != vl2:
                print("DIFFERS FROM", other, ":", pl2[:80])
                print("   mine :", mine[:200])
                print("   there:", vl2[:200])
                bad += 1
    print(f"repeat check: {len(seen)} distinct sentences, {shared} lines shared with 3-01 … 3-04 checked")
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
    A33.check_cross_book()
    check_cross_book()
    check_shared_notes()
    F.SLIPS.clear(); SLIP_USED.clear()
    text = unicodedata.normalize("NFC", translate_file())
    used = dict(SLIP_USED)
    chapter_slips = list(F.SLIPS)
    pali = (S.PALI_DIR / NAME).read_text(encoding="utf-8")
    probs = S.check_lines(pali, text, NAME) + A3.check_extra(text)
    for bad in ("….", ".…", "?…", ",…", "  ", "là là", "—", ":-"):
        assert bad not in text, bad
    assert check_repeats(pali) == 0, "identical Pāli rendered differently"
    for a, b, why in SLIP_FIX:
        assert used.get(why) == 1, (why, used.get(why))
    for a, b, why in SPACE_FIX:
        assert used.get(why), why
    with open(S.OUT_DIR / NAME, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    segs = len(re.findall(r"\^[0-9A-Za-z-]+\s*$", text, flags=re.M))
    print(f"wrote {NAME}: {len([x for x in text.splitlines() if x.strip()])} lines, {segs} segments")
    for why, n in used.items():
        print("SLIP", why, f"(x{n})")
    seen = set()
    for c, w in chapter_slips:
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
