# -*- coding: utf-8 -*-
"""pi-6 (Yamaka) Vietnamese zero-shot, chapter 3-04-ayatanayamaka.md (Āyatanayamaka, pavattivāra:
the nirodhavāra, time sections (1) … (4)).

Frames: build_3-03_vi (who33, pe_q, Q_TAIL, the sentence translator), build_3-02_vi (who32, run_q), build_3-01_vi
(members, «…pe…» lines, attribute beings, mūlaka notes, headings), build_2-01_vi (families A / B: nirujjhati
«chấm dứt» in every tense), build_2-02_vi (who2, PE) and build_6-01_vi (the bare cut question «(Kha) yassa vā pana
yattha…pe…?»), all imported and used verbatim. New here (see notes-3-04.md): beings heads cut by «…pe…»
(«Rūpāvacarānaṃ…pe… kāmāvacarānaṃ…pe….»), the cut question with a member and no verb («(Ka) yassa yattha
manāyatanaṃ…pe…?»), the closing piece of a cut question «… dhammāyatanaṃ nirujjhatīti?», and five editorial notes.

    import sys, importlib; sys.path.insert(0, r"D:\\Work\\OpenPecha\\abhidhamma-rails\\0-INBOX\\temp\\pipeline\\pi-6-vi-ai")
    A34 = importlib.import_module("build_3-04_vi")
    A34.translate_line(line, ctx) / A34.tr_sentence(s, ctx) / A34.tr_pe(text, ctx)

Importing writes nothing; run  python -I -X utf8 -B build_3-04_vi.py  to rebuild the chapter
(python -I -X utf8 -B build_3-04_vi.py --probe  lists unparsed lines without writing).
"""
import importlib
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai")
import build_sample_vi as S  # noqa: E402
F = importlib.import_module("build_2-01_vi")      # families A / B (frame-setter)
E = importlib.import_module("build_2-02_vi")      # who2, PE (frame-setter)
A3 = importlib.import_module("build_3-01_vi")     # Āyatana members, «…pe…», attribute beings, notes (frame-setter)
A32 = importlib.import_module("build_3-02_vi")    # who32, run_q
A33 = importlib.import_module("build_3-03_vi")    # who33, pe_q, Q_TAIL, tr_sentence
C6 = importlib.import_module("build_6-01_vi")     # frag_question «(b) Còn ở người nào, ở nơi nào…?»

NAME = "3-04-ayatanayamaka.md"
cap, low = S.cap, S.low
LABEL = S.LABEL

# ================================================================ editorial notes (new; words from 3-01 / 6-01 / 5-01)
YASSAKA = A3.YASSAKA                              # phần về người (3-01)
YATTHAKA = A3.YATTHAKA                            # phần về nơi chốn (3-01 / 2-02)
YASSAYATTHAKA = C6.YASSAYATTHAKA                  # phần về người và nơi chốn (6-01)
assert YASSAYATTHAKA == f"{YASSAKA} và nơi chốn"
SABBATTHA_NOTE = A3.SABBATTHA_NOTE                # ở mọi chỗ (3-01, textual sabbattha)
VITTHARA = "nên được trình bày chi tiết"          # vitthāretabba (pi-2; 5-01 / 6-01)
UPPADA = low(S.SECTION["uppādavāro"]).replace("mục về ", "")               # sự sinh khởi
NIRODHA = low(S.SECTION["nirodhavāro"]).replace("mục về ", "")             # sự chấm dứt
UPPADANIRODHA = low(S.SECTION["Uppādanirodhavāro"]).replace("mục về ", "")  # sự sinh khởi và sự chấm dứt
ATITA_PUCCHA = "các câu hỏi về quá khứ"           # atītā pucchā (6-01)
ANAGATA_PUCCHA = "các câu hỏi về tương lai"       # anāgatā pucchā (6-01 pattern)
V_PACCANIYA = "[paccaniyampi (sī. syā. ka.)]"

NOTES = {
    # (uppādepi nirodhepi uppādanirodhepi yatthakaṃ sabbattha sadisaṃ) (3-01 NOTE_YATTHAKA shape «ở hiện tại, …»)
    "(uppādepi nirodhepi uppādanirodhepi yatthakaṃ sabbattha sadisaṃ).":
        f"(ở {UPPADA}, ở {NIRODHA}, ở {UPPADANIRODHA}, {YATTHAKA} {SABBATTHA_NOTE} đều giống nhau).",
    # (Yassa yatthakampi sadisaṃ vitthāretabbaṃ). (5-01 «(… cũng nên được trình bày chi tiết giống như vậy).»)
    "(Yassa yatthakampi sadisaṃ vitthāretabbaṃ).": f"({cap(YASSAYATTHAKA)} cũng {VITTHARA} giống như vậy).",
    # (yassa yatthakampi yassakasadisaṃ). (3-01 «giống như phần về người»)
    "(yassa yatthakampi yassakasadisaṃ).": f"({YASSAYATTHAKA} cũng giống như {YASSAKA}).",
    # 6-01 «cả chiều thuận lẫn chiều nghịch», «các câu hỏi về quá khứ», «trong mục về sự sinh khởi»
    f"(Uppādavārepi nirodhavārepi uppādanirodhavārepi atītā pucchā anulomampi paccanīkampi {V_PACCANIYA} sadisaṃ.)":
        (f"(Trong {S.SECTION['uppādavāro']}, trong {S.SECTION['nirodhavāro']}, trong "
         f"{low(S.SECTION['Uppādanirodhavāro'])}, {ATITA_PUCCHA}, cả {low(S.SECTION['anulomaṃ'])} lẫn "
         f"{low(S.SECTION['paccanīkaṃ'])} {F.variant(V_PACCANIYA, label=S.SPELL)}, đều giống nhau.)"),
    # 2-02 YATHA_VIBHATTA / 6-01 «(Như …, đã được phân tích trong mục về sự sinh khởi, … cũng nên … như vậy …)»
    "(Yathā uppādavāre yassa yatthake anāgatā pucchā vitthāritā, evaṃ nirodhepi vitthāretabbā).":
        (f"(Như {ANAGATA_PUCCHA} trong {YASSAYATTHAKA} đã được trình bày chi tiết trong {S.SECTION['uppādavāro']}, "
         f"ở {NIRODHA} cũng {VITTHARA} như vậy)."),
}

# ================================================================ source slips rendered as meant (each applies once)
SLIP_FIX = [
    ("rūpāyatanaṃ …pe… manāyatanaṃ", "rūpāyatanaṃ…pe… manāyatanaṃ",
     "^6-3-151: stray space before «…pe…» («rūpāyatanaṃ …pe…»); the run is written as the others"),
    ("na nirujjhatī ti…pe…", "na nirujjhatīti…pe…",
     "^6-3-131: «nirujjhatī ti» written apart; read «nirujjhatīti»"),
    ("tattha manāyatanaṃ na nirujjhissati, parinibbantānaṃ asaññasattānaṃ",
     "tattha manāyatanaṃ na nirujjhissati. Parinibbantānaṃ asaññasattānaṃ",
     "^6-3-148: comma for the full stop between the two answer sentences («…, parinibbantānaṃ …»); "
     "period written as in every parallel line"),
]
SLIP_USED = {}


def fix_slips(s):
    for a, b, why in SLIP_FIX:
        if a in s:
            s = s.replace(a, b)
            SLIP_USED[why] = SLIP_USED.get(why, 0) + 1
    return s


# ================================================================ new pieces
CUT_Q_RE = re.compile(r"\((?P<l>Ka|Kha)\) (?P<w>yassa vā pana yattha|yassa yattha|yassa vā pana|yassa)"
                      r"(?: (?P<x>\S+āyatanaṃ))?…pe…\?")
CLOSE_Q_RE = re.compile(r"(?P<x>\S+āyatanaṃ) (?P<v>" + A3.V + r")\?")


def cut_q(s):
    """(Kha) yassa vā pana yattha…pe…? = (b) Còn ở người nào, ở nơi nào…? (6-01 frag_question, asserted);
    (Ka) yassa yattha manāyatanaṃ…pe…? = (a) Ở người nào, ở nơi nào mà lĩnh vực ý…? (new, same shape)."""
    mm = CUT_Q_RE.fullmatch(s)
    if not mm:
        return None
    kha = "vā pana" in mm["w"]
    kind = mm["w"].replace(" vā pana", "")
    head = (F.VA_PANA if kha else "") + F.REL_VI[kind] + (f" mà {A3.m(mm['x'])}" if mm["x"] else "")
    out = f"{LABEL[mm['l']]} {cap(head)}{E.PE}?"
    if kha and not mm["x"]:
        assert out == C6.frag_question({"w": mm["w"], "x": None, "l": mm["l"], "p": "?"}), out
    return out


def close_q(s, ctx):
    """… dhammāyatanaṃ nirujjhatīti? (the last piece of a question cut by …pe…) = «lĩnh vực đối tượng của ý chấm dứt
    không?» (3-03 Q_TAIL, the end of the 7-01 Q_FRAME)."""
    mm = CLOSE_Q_RE.fullmatch(s)
    if not mm:
        return None
    return f"{A3.m(mm['x'])} " + A33.Q_TAIL.format(pb=F.verb(*F.vparse(mm["v"], ctx)))


def beings_head(body):
    """Rūpāvacarānaṃ / Asaññasattānaṃ arūpānaṃ / pañcavokārānaṃ asaññasattānaṃ (a beings head cut by …pe…) =
    «Ở chúng sinh trong cõi hình sắc» … (2-01 who / WHO_HEAD; lowercase when the Pāli piece is)."""
    ws = body.split()
    if not ws or not all(F._plane_case(low(w))[0] == "gen" for w in ws):
        return None
    out = A33.who33(body)
    return cap(out) if body[0].isupper() else out


# ================================================================ sentences
def tr_sentence(s, ctx, pe=False):
    if s in NOTES:
        return NOTES[s]
    for f in (cut_q, lambda x: close_q(x, ctx)):
        r = f(s)
        if r:
            return r
    body = s[:-1] if s and s[-1] in ".?" else s
    if pe:
        r = beings_head(body)
        if r:
            return r + (s[-1] if s != body else "")
    try:
        out = A33.tr_sentence(s, ctx)
    except ValueError:
        if not pe:
            raise
        body, punct = (s[:-1], s[-1]) if s and s[-1] in ".?" else (s, "")
        out = A3.tr(body, punct, ctx, pe=True)
    if pe and s[:1].islower() and out.startswith("Ở "):
        out = low(out)              # a beings answer continuing after «…pe…» (Pāli lowercase)
    return out


def tr_sentences(text, ctx, pe=False):
    return " ".join(tr_sentence(x.strip(), ctx, pe) for x in F.split_sentences(text) if x.strip())


def tr_pe(text, ctx):
    """3-01 tr_pe with this chapter's sentence translator: each piece between the ellipses is translated in place,
    the ellipsis stays at its spot; a period before / after it gives way («Đúng vậy…»), «?…» is written «? …»."""
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


# ================================================================ lines
def translate_line(line, ctx):
    mm = re.match(r"^(?P<h>#+ )?(?P<t>.*?)(?P<id> \^[0-9A-Za-z-]+)?$", line)
    h, t, sid = mm["h"] or "", mm["t"], mm["id"] or ""
    if h:
        return h + A3.heading(t) + sid
    t = fix_slips(t)
    r = A32.run_q(t, ctx)                            # «…pe…» runs inside one question (3-02)
    if r:
        return r + sid
    if "…" in t:
        sents = [x.strip() for x in F.split_sentences(t) if x.strip()]
        if any(A33.PE_Q_RE.fullmatch(x) for x in sents):
            return " ".join(A33.pe_q(x, ctx) or tr_pe(x, ctx) for x in sents) + sid
        if all(CUT_Q_RE.fullmatch(x) or "…" not in x for x in sents):
            return tr_sentences(t, ctx) + sid
        return tr_pe(t, ctx) + sid
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
CROSS_BOOK = [("chấm dứt", 2), ("trình bày chi tiết", 2), ("giống như vậy", 2), ("câu hỏi", 3),
              ("nhập Niết-bàn trọn vẹn", 5), ("chết đi", 2), ("tái sinh", 2)]


def check_cross_book():
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md")))
             for b, d in S.RAILS_DIR.items()}
    missing = [(s, b) for s, b in CROSS_BOOK if s not in texts[b]]
    for s, b in missing:
        print(f"CROSS-BOOK MISSING in pi-{b}: {s} (found in: {[k for k, v in texts.items() if s in v]})")
    assert not missing, f"{len(missing)} cross-book strings not found"
    print(f"cross-book asserts (3-04): {len(CROSS_BOOK)} strings found in pi-1..5 rails")


def check_extra(text):
    probs = A3.check_extra(text)
    for i, ln in enumerate(text.splitlines(), 1):
        body = re.sub(r" ?\[[^\]]*\]", "", re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", ln))
        for bad in ("nirujjh", "pe…", "…pe", "ānaṃ", "sadis", "yattha"):
            if bad in body:
                probs.append(f"line {i}: «{bad}»")
    return probs


def _sentences(text):
    for p in text.splitlines():
        if not p.strip() or p.startswith("#") or "…" in p:
            continue
        p = re.sub(r"\s*\^[\w-]+$", "", fix_slips(p))
        yield from (x.strip() for x in F.split_sentences(p) if x.strip())


def check_repeats(pali):
    """Identical Pāli sentence -> identical Vietnamese, within 3-04 and against the 3-01 / 3-02 / 3-03 outputs."""
    seen, bad = {}, 0
    for s in _sentences(pali):
        t = tr_sentence(s, "")
        if seen.setdefault(s, t) != t:
            bad += 1
    shared = 0
    for other, fix in (("3-01-ayatanayamaka.md", lambda x: x), ("3-02-ayatanayamaka.md", A32.fix_slips),
                       ("3-03-ayatanayamaka.md", A33.fix_slips)):
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
    print(f"repeat check: {len(seen)} distinct sentences, {shared} lines shared with 3-01 / 3-02 / 3-03 checked")
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
    F.SLIPS.clear(); SLIP_USED.clear()
    text = unicodedata.normalize("NFC", translate_file())
    used = dict(SLIP_USED)
    chapter_slips = list(F.SLIPS)
    pali = (S.PALI_DIR / NAME).read_text(encoding="utf-8")
    probs = S.check_lines(pali, text, NAME) + check_extra(text)
    for bad in ("….", ".…", "?…", ",…", "  ", "là là", "—", ":-"):
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
