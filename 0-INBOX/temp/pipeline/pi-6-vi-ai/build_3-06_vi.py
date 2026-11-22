# -*- coding: utf-8 -*-
"""pi-6 (Yamaka) Vietnamese zero-shot, chapter 3-06-ayatanayamaka.md (Āyatanayamaka, last part: uppādanirodhavāra
(3) anāgata … (6) atītānāgata, the close of the pavattivāra, the pariññāvāra and the yamaka's closing lines).

Frames: build_3-05_vi (tesam_pe, RES_HEAD, pe_head), build_3-04_vi (cut_q, the nirujjhati notes), build_3-03_vi
(who33, pe_q, sentence frames), build_3-02_vi (run_q), build_3-01_vi (members, «…pe…» lines, headings), build_2-01_vi
(families A / B), build_2-02_vi (family E: translate_e; YE_CA_CAVANTA; closing lines) and build_6-02_vi (the words of
the «(Yathā …)» notes), all imported and used verbatim. New here (see notes-3-06.md): «Ye <P>ṃ upapajjitvā
parinibbāyissanti tesaṃ cavantānaṃ» as the head of an answer (who36), the answer fragments «<beings> tesaṃ tattha X»
and «<beings> tesaṃ tattha X v, no ca tesaṃ tattha» before «…pe…», the unlabelled cut question «Yassa vā pana
X…pe…?», and two editorial notes.

    import sys, importlib; sys.path.insert(0, r"D:\\Work\\OpenPecha\\abhidhamma-rails\\0-INBOX\\temp\\pipeline\\pi-6-vi-ai")
    A36 = importlib.import_module("build_3-06_vi")
    A36.who36(phrase) / A36.frag(body, ctx) / A36.translate_line(line, ctx)

Importing writes nothing; run  python -I -X utf8 -B build_3-06_vi.py  to rebuild the chapter
(python -I -X utf8 -B build_3-06_vi.py --probe  lists unparsed lines without writing).
"""
import importlib
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai")
import build_sample_vi as S  # noqa: E402
F = importlib.import_module("build_2-01_vi")      # families A / B (frame-setter)
E = importlib.import_module("build_2-02_vi")      # family E, YE_CA_CAVANTA, closing lines (frame-setter)
A3 = importlib.import_module("build_3-01_vi")     # Āyatana members, «…pe…», headings (frame-setter of this yamaka)
A32 = importlib.import_module("build_3-02_vi")    # run_q
A33 = importlib.import_module("build_3-03_vi")    # who33, pe_q, B_NOT_RE / B_BOTH_RE
A34 = importlib.import_module("build_3-04_vi")    # cut_q, tr_sentence (nirodha pieces)
A35 = importlib.import_module("build_3-05_vi")    # tesam_pe, RES_HEAD, pe_head, heading
C62 = importlib.import_module("build_6-02_vi")    # PA_Q, AA_Q, ANU_PAC, UV, NV (the «(Yathā …)» notes)

NAME = "3-06-ayatanayamaka.md"
cap, low = S.cap, S.low
LABEL = S.LABEL

# ================================================================ beings (family B addition, new)
YE_CAVANTA_RE = re.compile(r"[Yy]e (?P<ps>\S+(?: \S+)*?) upapajjitvā parinibbāyissanti tesaṃ cavantānaṃ")


def who36(phrase):
    """A33.who33 (hence 3-02 / 3-01 / 2-02 / 2-01) wherever it applies; new: «Ye <P>ṃ upapajjitvā parinibbāyissanti
    tesaṃ cavantānaṃ» heading an answer = «Ở những người đang chết đi mà sau khi tái sinh vào <P> sẽ nhập Niết-bàn
    trọn vẹn» (2-01 WHO_HEAD + 2-02 YE_CA_CAVANTA, the same words as inside the «… ye ca …» group)."""
    mm = YE_CAVANTA_RE.fullmatch(phrase)
    if mm:
        return F.WHO_HEAD.format(g=E.YE_CA_CAVANTA.format(p=A33._acc_planes(mm["ps"], phrase)))
    return A33.who33(phrase)


# ================================================================ fragments before «…pe…» (new, 3-05 RES_HEAD extended)
FRAG_RE = re.compile(r"(?P<g>.+?) (?P<res>tesaṃ tattha|tesaṃ)(?: (?P<x>\S+āyatanaṃ)(?: (?P<v>(?:na )?\S+), no ca "
                     r"(?P<res2>tesaṃ tattha|tesaṃ))?)?")
BUT_HEAD = F.BUT_C.split(" {b}")[0]               # «{a} {p}, nhưng {dem}» (the 7-01 BUT_C up to its second member)
assert F.BUT_C.startswith(BUT_HEAD + " {b} ")


def frag(body, ctx):
    """«<beings> tesaṃ [tattha]» = «Ở <beings>, thì ở những người ấy[, ở nơi ấy]» (3-05 tesam_pe);
    «… tesaṃ tattha X» = «…, thì ở những người ấy, ở nơi ấy X»;
    «… tesaṃ tattha X v, no ca tesaṃ tattha» = «…, thì ở những người ấy, ở nơi ấy X v, nhưng ở những người ấy, ở nơi ấy»."""
    mm = FRAG_RE.fullmatch(body)
    if not mm:
        return None
    try:
        head = who36(mm["g"])
    except (ValueError, AssertionError, KeyError):
        return None
    out = A35.RES_HEAD.format(head=head, res=F.RES_VI[mm["res"]])
    if mm["x"]:
        x = A3.m(mm["x"])
        if mm["v"]:
            assert mm["res2"] == mm["res"], body
            out += " " + BUT_HEAD.format(a=x, p=F.verb(*F.vparse(mm["v"], ctx)), dem=F.NO_CA_VI[mm["res2"]])
        else:
            out += " " + x
    out = cap(out) if body[:1].isupper() else out
    if not mm["x"]:
        assert out == A35.tesam_pe(body), (body, out)      # the bare fragment says exactly what 3-05 says
    return out


# ================================================================ cut questions «[(Ka)] Yassa vā pana [yattha] [X]…pe…?»
CUT_Q_RE = re.compile(r"(?:\((?P<l>Ka|Kha)\) )?(?P<w>[Yy]assa vā pana yattha|[Yy]assa yattha|[Yy]assa vā pana|"
                      r"[Yy]assa)(?: (?P<x>\S+āyatanaṃ))?…pe…\?")


def cut_q(s):
    """3-04 cut_q with the label optional: «Yassa vā pana dhammāyatanaṃ…pe…?» = «Còn ở người nào mà lĩnh vực đối
    tượng của ý…?» (same words as «(b) Còn ở người nào mà …?»)."""
    mm = CUT_Q_RE.fullmatch(s)
    if not mm:
        return None
    if mm["l"]:
        out = A34.cut_q(s)
        assert out, s
        return out
    kind = low(mm["w"]).replace(" vā pana", "")
    head = (F.VA_PANA if "vā pana" in mm["w"] else "") + F.REL_VI[kind] + (f" mà {A3.m(mm['x'])}" if mm["x"] else "")
    out = f"{cap(head)}{E.PE}?"
    assert out == A34.cut_q("(Kha) " + low(s[0]) + s[1:]).split(" ", 1)[1] or "vā pana" not in mm["w"], out
    return out


# ================================================================ editorial notes and closing lines
UPPADANIRODHA = A34.UPPADANIRODHA                 # sự sinh khởi và sự chấm dứt (uppādanirodhe, 3-04 / 3-05 «ở …»)
YASSAKA, YATTHAKA, YASSAYATTHAKA = A3.YASSAKA, A3.YATTHAKA, A34.YASSAYATTHAKA
V_VIBHAJ = "[vibhajitabbaṃ (sī. syā. ka.)]"       # the Pāli has «(sī syā. ka.)»: missing period after sī (slip)
V_ATITENA = "[atītenānāgatā (syā.)]"
NOTE_159_PALI = ("(Yathā uppādavāre paccuppannātītā pucchā vibhattā evaṃ uppādanirodhepi paccuppannātītā pucchā "
                 "anulomampi paccanīkampi vibhajitabbā [vibhajitabbaṃ (sī syā. ka.)] ).")
NOTE_322_PALI = ("(Yathā nirodhavāre atītānāgatā [atītenānāgatā (syā.)] pucchā yassakampi yatthakampi "
                 "yassayatthakampi anulomampi paccanīkampi vibhattaṃ, evaṃ uppādanirodhepi atītānāgatā pucchā "
                 "vibhajitabbā.)")
EXACT = {
    # 6-02 ^6-6-147 shape «(Như {PA_Q} … đã được phân tích trong {UV}, …, {PA_Q}, {ANU_PAC}, cũng nên được phân tích
    # như vậy.)»; bare uppādanirodhe = «ở sự sinh khởi và sự chấm dứt» (3-04); the variant follows its word
    NOTE_159_PALI:
        (f"(Như {C62.PA_Q} đã được phân tích trong {C62.UV}, ở {UPPADANIRODHA}, {C62.PA_Q}, {C62.ANU_PAC}, cũng "
         f"nên được phân tích {F.variant(V_VIBHAJ)} như vậy)."),
    # 6-02 ^6-6-147 / 6-01 ^6-6-87 («cả {YASSAKA} lẫn {YASSAYATTHAKA}, cả chiều thuận lẫn chiều nghịch»)
    NOTE_322_PALI:
        (f"(Như {C62.AA_Q} {F.variant(V_ATITENA)}, cả {YASSAKA}, {YATTHAKA} lẫn {YASSAYATTHAKA}, {C62.ANU_PAC}, "
         f"đã được phân tích trong {C62.NV}, ở {UPPADANIRODHA}, {C62.AA_Q} cũng nên được phân tích như vậy.)"),
    "Uppādanirodhavāro.": E.EXACT["Uppādanirodhavāro."],          # Mục về sự sinh khởi và sự chấm dứt. (2-02)
    "Pavattivāro niṭṭhito.": E.EXACT["Pavattivāro niṭṭhito."],    # Mục về sự diễn tiến đã hoàn tất. (2-02)
    **E.PARINNA_EXACT,                                            # Pariññāvāro. = Mục về sự hiểu biết trọn vẹn.
    "Āyatanayamakaṃ niṭṭhitaṃ.": S.yamaka_end("Āyatanayamakaṃ"),  # sample yamaka_end
    "Namo tassa bhagavato arahato sammāsambuddhassa": S.HOMAGE,    # sample / 2-02
    "No.": F.NO,                                                  # Không. (7-01)
    "Āmantā.": S.AMANTA,                                          # Đúng vậy. (sample)
}
SLIP_NOTES = {
    NOTE_159_PALI: ["^6-3-229: variant sigla «(sī syā. ka.)» lack the period after «sī»; read «Sī.»",
                    "^6-3-229: stray space before the closing «)» («… ka.)] ).»); not written"],
}

# ================================================================ source slips rendered as meant (each applies once)
SLIP_FIX = [
    ("no ca tesaṃ ghānāyatanaṃ upapajjissati.", "no ca tesaṃ ghānāyatanaṃ uppajjissati.",
     "^6-3-212: «upapajjissati» (tái sinh) for «uppajjissati» (sinh khởi) in the answer of a sinh khởi question; "
     "read uppajjissati (spelling)"),
    ("tassa tattha manāyatanaṃ …pe… dhammāyatanaṃ", "tassa tattha manāyatanaṃ…pe… dhammāyatanaṃ",
     "^6-3-217: stray space before «…pe…» («manāyatanaṃ …pe…»); the run is written as the others (3-04 ^6-3-151)"),
    ("arūpānaṃ tasaṃ tattha cakkhāyatanaṃ nuppajjati", "arūpānaṃ tesaṃ tattha cakkhāyatanaṃ nuppajjati",
     "^6-3-244: «tasaṃ» = tesaṃ (spelling)"),
]
SLIP_USED = {}


def fix_slips(s):
    for a, b, why in SLIP_FIX:
        if a in s:
            s = s.replace(a, b)
            SLIP_USED[why] = SLIP_USED.get(why, 0) + 1
    for k, whys in SLIP_NOTES.items():
        if k in s:
            for why in whys:
                SLIP_USED[why] = SLIP_USED.get(why, 0) + 1
    return s


# ================================================================ sentences
def tr_sentence(s, ctx, pe=False):
    """One Pāli sentence (with its final punctuation, if any)."""
    if s in EXACT:
        return EXACT[s]
    body, punct = (s[:-1], s[-1]) if s and s[-1] in ".?" else (s, "")
    if body == "":
        return punct
    r = E.translate_e(s, A3.m)                                 # family E (2-02)
    if r:
        return r
    r = cut_q(s)
    if r:
        return r
    if pe and not punct:
        r = frag(body, ctx)
        if r:
            return r
    for rx, both in ((A33.B_NOT_RE, False), (A33.B_BOTH_RE, True)):   # 3-03 tr_sentence with who36
        mm = rx.fullmatch(body)
        if mm and punct == ".":
            res = mm["res"]
            if not both:
                assert res == mm["res2"], body
            head = A3.where3(mm["g"]) if res == "tattha" else who36(mm["g"])
            x = A3.m(mm["x"] + ("ṃ" if both else ""))
            y = A3.m(mm["y"] + ("ṃ" if both else ""))
            f = F.b_both if both else F.b_not
            out = f(res, head, x, F.vparse(mm["v1"], ctx), y, F.vparse(mm["v2"], ctx))
            if pe and s[:1].islower():
                out = low(out)            # an answer continuing after «…pe…» (Pāli lowercase)
            return out
    try:
        out = A34.tr_sentence(s, ctx, pe)
    except ValueError:
        if not pe:
            raise
        out = A35.pe_head(body, ctx)
        if not out:
            raise
        out += punct
    if pe and s[:1].islower() and out.startswith("Ở "):
        out = low(out)
    return out


def tr_sentences(text, ctx, pe=False):
    return " ".join(tr_sentence(x.strip(), ctx, pe) for x in F.split_sentences(text) if x.strip())


def tr_pe(text, ctx):
    """3-01 / 3-04 / 3-05 tr_pe with this chapter's pieces: each piece between the ellipses is translated in place;
    a period next to the ellipsis gives way to it; «?…» is written «? …»."""
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
    if s in EXACT:
        return EXACT[s]
    r = cut_q(s)
    if r:
        return r
    if A33.PE_Q_RE.fullmatch(s):
        return A33.pe_q(s, ctx)
    if "…" in s:
        return tr_pe(s, ctx)
    return tr_sentence(s, ctx)


# ================================================================ lines
def translate_line(line, ctx):
    mm = re.match(r"^(?P<h>#+ )?(?P<t>.*?)(?P<id> \^[0-9A-Za-z-]+)?$", line)
    h, t, sid = mm["h"] or "", mm["t"], mm["id"] or ""
    if h:
        return h + A35.heading(t) + sid
    t = fix_slips(t)
    if t in EXACT:
        return EXACT[t] + sid
    r = A32.run_q(t, ctx)                            # «…pe…» runs inside one question (3-02)
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
CROSS_BOOK = [("hiểu biết trọn vẹn", 2), ("Bậc A-la-hán", 4), ("con đường", 4), ("những người phàm phu", 4),
              ("đạt được", 2), ("chấm dứt", 2), ("sinh khởi", 1), ("tái sinh", 2), ("chết đi", 2),
              ("nhập Niết-bàn trọn vẹn", 5), ("sau khi", 2), ("câu hỏi", 3), ("được phân tích", 2),
              ("gồm năm khối", 2)]


def check_cross_book():
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md")))
             for b, d in S.RAILS_DIR.items()}
    missing = [(s, b) for s, b in CROSS_BOOK if s not in texts[b]]
    for s, b in missing:
        print(f"CROSS-BOOK MISSING in pi-{b}: {s} (found in: {[k for k, v in texts.items() if s in v]})")
    assert not missing, f"{len(missing)} cross-book strings not found"
    print(f"cross-book asserts (3-06): {len(CROSS_BOOK)} strings found in pi-1..5 rails")


def check_shared():
    """Frames this chapter shares with finished chapters say what those chapters say."""
    v202 = (S.OUT_DIR / "2-02-khandhayamaka.md").read_text(encoding="utf-8")
    for s in ("Mục về sự hiểu biết trọn vẹn.", "Kính lễ Đức Thế Tôn, bậc A-la-hán, bậc Tự Giác Ngộ Hoàn Toàn",
              "Mục về sự sinh khởi và sự chấm dứt.", "Mục về sự diễn tiến đã hoàn tất.",
              "Người có được con đường tối thượng và những người phàm phu nào sẽ không đạt được con đường, thì "
              "những người ấy"):
        assert s in v202, s
    v602 = (S.OUT_DIR / "6-02-sankharayamaka.md").read_text(encoding="utf-8")
    assert f"(Như {C62.PA_Q}, {C62.ANU_PAC}, đã được phân tích trong {C62.UV}" in v602
    v304 = (S.OUT_DIR / "3-04-ayatanayamaka.md").read_text(encoding="utf-8")
    assert f"ở {UPPADANIRODHA}" in v304
    # the pariññā questions and answers with Āyatana members = the 2-02 frames with the 3-01 members
    q = E.translate_e("(Ka) yo cakkhāyatanaṃ parijānāti so sotāyatanaṃ parijānitthāti?", A3.m)
    assert q == "(a) Người nào hiểu biết trọn vẹn lĩnh vực mắt, thì có phải người ấy đã hiểu biết trọn vẹn lĩnh vực tai không?", q


def check_extra(text):
    probs = A3.check_extra(text)
    for i, ln in enumerate(text.splitlines(), 1):
        body = re.sub(r" ?\[[^\]]*\]", "", re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", ln))
        for bad in ("nirujjh", "pe…", "…pe", "ānaṃ", "sadis", "yattha", "parijān", "tasaṃ", "upapajj", "ṭhapetvā"):
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
    """Identical Pāli sentence -> identical Vietnamese, within 3-06 and against the 3-01 … 3-05 outputs (3-05 is
    reported, not asserted, when its output was written by an earlier state of its builder)."""
    seen, bad, warn = {}, 0, 0
    for s in _sentences(pali):
        t = translate_sentence(s, "")
        if seen.setdefault(s, t) != t:
            bad += 1
    shared = 0
    others = [("3-01-ayatanayamaka.md", lambda x: x, True), ("3-02-ayatanayamaka.md", A32.fix_slips, True),
              ("3-03-ayatanayamaka.md", A33.fix_slips, True), ("3-04-ayatanayamaka.md", A34.fix_slips, True),
              ("3-05-ayatanayamaka.md", A35.fix_slips, False)]
    for other, fix, strict in others:
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
                if strict:
                    bad += 1
                else:
                    warn += 1
    print(f"repeat check: {len(seen)} distinct sentences, {shared} lines shared with 3-01 … 3-05 checked, "
          f"{warn} differences from 3-05 reported")
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
    E.check_cross_book()
    E.check_family_e()
    A3.check_cross_book()
    A32.check_cross_book()
    A33.check_cross_book()
    A34.check_cross_book()
    A35.check_cross_book()
    check_cross_book()
    check_shared()
    F.SLIPS.clear(); E.SLIPS.clear(); SLIP_USED.clear()
    text = unicodedata.normalize("NFC", translate_file())
    used = dict(SLIP_USED)
    chapter_slips = list(F.SLIPS) + [("", x) for x in E.SLIPS]
    pali = (S.PALI_DIR / NAME).read_text(encoding="utf-8")
    probs = S.check_lines(pali, text, NAME) + check_extra(text)
    for bad in ("….", ".…", "?…", ",…", "  ", "là là", "—", ":-", "Sī. Syā", "( "):
        assert bad not in text, bad
    assert check_repeats(pali) == 0, "identical Pāli rendered differently"
    for a, b, why in SLIP_FIX:
        assert used.get(why) == 1, (why, used.get(why))
    for whys in SLIP_NOTES.values():
        for why in whys:
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
